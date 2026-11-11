import os
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect, LangDetectException
from indic_transliteration.sanscript import transliterate, DEVANAGARI, ITRANS

MODEL_NAME = "facebook/nllb-200-distilled-600M"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Bengali": "ben_Beng",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Punjabi": "pan_Guru",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Urdu": "urd_Arab",
    "Japanese": "jpn_Jpan",
    "Chinese": "zho_Hans",
    "Korean": "kor_Hang",
    "Thai": "tha_Thai",
    "Indonesian": "ind_Latn",
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Italian": "ita_Latn",
    "Portuguese": "por_Latn",
    "Russian": "rus_Cyrl"
}

DETECT_CODES = {
    "en": "English", "hi": "Hindi", "mr": "Marathi", "gu": "Gujarati",
    "bn": "Bengali", "ta": "Tamil", "te": "Telugu", "pa": "Punjabi",
    "kn": "Kannada", "ml": "Malayalam", "ur": "Urdu", "es": "Spanish",
    "fr": "French", "de": "German", "it": "Italian", "pt": "Portuguese",
    "ru": "Russian", "ja": "Japanese", "zh-cn": "Chinese", "zh-tw": "Chinese"
}

print("Loading VERBA model. First startup may take several minutes...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
dtype = torch.float16 if DEVICE == "cuda" else torch.float32
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=dtype,
    low_cpu_mem_usage=True
)
model.to(DEVICE)
model.eval()
print(f"VERBA is ready on {DEVICE}.")

def detect_source_language(text):
    try:
        detected_code = detect(text)
        return DETECT_CODES.get(detected_code, "English")
    except LangDetectException:
        return "English"

def translate(text, source_language, target_language):
    if not isinstance(text, str) or not text.strip():
        raise gr.Error("Please enter text to translate.")
    if len(text) > 5000:
        raise gr.Error("Please keep the text within 5,000 characters.")
    if target_language not in LANGUAGES:
        raise gr.Error("Please select a supported target language.")

    if source_language == "Auto Detect":
        source_language = detect_source_language(text)
    if source_language not in LANGUAGES:
        raise gr.Error("Could not identify the source language. Please select it manually.")
    if source_language == target_language:
        return text

    tokenizer.src_lang = LANGUAGES[source_language]
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(DEVICE)

    target_id = tokenizer.convert_tokens_to_ids(LANGUAGES[target_language])
    if target_id == tokenizer.unk_token_id:
        raise gr.Error("Target language code is not available.")

    with torch.inference_mode():
        generated = model.generate(
            **inputs,
            forced_bos_token_id=target_id,
            max_new_tokens=160,
            num_beams=3
        )
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

def roman_hindi(text):
    if not text:
        return ""
    try:
        return transliterate(text, DEVANAGARI, ITRANS)
    except Exception:
        return ""

def run_translation(text, source_language, target_language):
    result = translate(text, source_language, target_language)
    roman = roman_hindi(result) if target_language == "Hindi" else ""
    return result, roman

def swap_languages(source, target):
    if source == "Auto Detect":
        return target, "English"
    return target, source

def clear_fields():
    return "", "", ""

custom_css = """
.gradio-container {background: linear-gradient(135deg, #10172e, #20204a, #301b52);}
#main-title {text-align:center; padding:24px; border-radius:18px; background:linear-gradient(90deg,#292e63,#663399);}
#main-title h1 {font-size:42px; color:white;}
#main-title p {color:#e1dcff;}
.gr-button-primary {background:linear-gradient(90deg,#6255e7,#9b59d0) !important; border:none !important;}
"""

with gr.Blocks(title="VERBA 2.0", css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.HTML("""
    <div id="main-title">
      <h1>🌐 VERBA</h1>
      <p>Connecting Languages, Connecting People</p>
      <p>Multilingual Translation Platform</p>
    </div>
    """)
    with gr.Row():
        source = gr.Dropdown(
            ["Auto Detect"] + list(LANGUAGES.keys()),
            value="Auto Detect",
            label="Translate From"
        )
        swap = gr.Button("⇄ Swap")
        target = gr.Dropdown(
            list(LANGUAGES.keys()),
            value="Marathi",
            label="Translate To"
        )
    input_box = gr.Textbox(
        label="Enter Your Text",
        placeholder="Type up to 5,000 characters...",
        lines=7,
        max_lines=12,
        max_length=5000
    )
    output_box = gr.Textbox(label="Translation Result", lines=7, interactive=False)
    roman_box = gr.Textbox(
        label="Hindi Transliteration (Roman Hindi)",
        lines=2,
        interactive=False
    )
    with gr.Row():
        translate_btn = gr.Button("Translate", variant="primary")
        clear_btn = gr.Button("Clear")

    gr.Markdown(
        "Academic prototype powered by Meta NLLB-200 Distilled 600M. "
        "Please verify translations before important use. Warli, Kokna and "
        "other local languages are future data-development goals, not currently "
        "verified translation options."
    )
    translate_btn.click(
        run_translation,
        inputs=[input_box, source, target],
        outputs=[output_box, roman_box]
    )
    swap.click(swap_languages, inputs=[source, target], outputs=[source, target])
    clear_btn.click(clear_fields, inputs=[], outputs=[input_box, output_box, roman_box])

demo.queue().launch(server_name="0.0.0.0", server_port=7860)
