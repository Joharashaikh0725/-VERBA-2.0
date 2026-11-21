
# 🌐 VERBA – Multilingual Translator with RAG

### Connecting Languages, Connecting People

VERBA is an AI-powered multilingual translation platform designed to help people communicate across different languages. It uses Meta AI's **NLLB-200 Distilled 600M** pretrained translation model and Retrieval-Augmented Generation (RAG) to improve translation consistency through verified terminology and stored translations.

## 🚀 Project Overview

VERBA combines multilingual machine translation with a Retrieval-Augmented Generation (RAG) system. It uses a vector database to retrieve relevant glossary terms, previously verified translations, and reference documents before generating translations.

The project aims to support communication across Indian and international languages, with particular interest in local terminology relevant to Palghar district, Maharashtra.

## ✨ Features

- **Multilingual Translation:** Supports 22 language options.
- **AI Translation Engine:** Uses Meta AI's NLLB-200 Distilled 600M model.
- **RAG Integration:** Retrieves relevant information before translation.
- **Vector Database:** Uses ChromaDB to store and retrieve language information.
- **Smart Glossary:** Maintains approved translations for important terms and local names.
- **Translation Memory:** Stores verified translations for future reuse.
- **PDF and TXT Support:** Loads reference documents into the knowledge base.
- **Term Protection:** Protects verified glossary terms during translation.
- **Language Swapping:** Easily switches source and target languages.
- **Translation Benchmarking:** Measures translation speed and performance.
- **Interactive Interface:** Built using Gradio.

## 🌍 Supported Languages

VERBA currently provides 22 language options:

**Indian Languages**

- English
- Hindi
- Marathi
- Gujarati
- Bengali
- Tamil
- Telugu
- Punjabi
- Kannada
- Malayalam
- Urdu

**Asian Languages**

- Japanese
- Chinese
- Korean
- Thai
- Indonesian

**European Languages**

- Spanish
- French
- German
- Italian
- Portuguese
- Russian

## 🛠️ Technologies Used

| Technology                | Purpose                           |
| ------------------------- | --------------------------------- |
| Python                    | Main programming language         |
| PyTorch                   | Deep learning framework           |
| Hugging Face Transformers | Pretrained translation model      |
| NLLB-200                  | Multilingual translation          |
| Gradio                    | User interface                    |
| LangChain                 | RAG integration                   |
| ChromaDB                  | Vector database                   |
| Sentence Transformers     | Text embeddings                   |
| MiniLM                    | Semantic similarity and retrieval |
| PyPDF                     | PDF text extraction               |
| Google Colab              | Development environment           |
| Google Drive              | Model and database storage        |

## 🧠 How VERBA Works

1. **User Input:** Enter text and select source and target languages.
2. **RAG Retrieval:** Search the vector database for relevant glossary terms, translation memory, and reference information.
3. **Term Protection:** Protect approved glossary terms using placeholders.
4. **Translation:** The NLLB-200 model generates the translation.
5. **Term Restoration:** Restore the approved translations into the generated result.
6. **Translation Memory:** Save verified translations for future use.
7. **Output:** Display the final translated text.

## 🗂️ RAG Knowledge Base

VERBA uses three main types of knowledge sources:

- `glossary.csv` – Stores approved translations of important terms.
- `translation_memory.csv` – Stores previously verified sentence translations.
- `knowledge_base/` – Contains reference documents in TXT and PDF formats.

The system uses **ChromaDB** with the `all-MiniLM-L6-v2` embedding model for semantic retrieval.

## ⚙️ Installation and Setup

VERBA is developed in Google Colab.

### Step 1: Open the Notebook

Upload and open `DEVELOPING_VERBA_with_RAG.ipynb` in Google Colab.

### Step 2: Install Dependencies

Run the installation cells in the notebook.

```python
%pip install -q "transformers<5" sentencepiece accelerate gradio
```

Install RAG dependencies:

```python
%pip install -q langchain-core langchain-chroma langchain-text-splitters chromadb pypdf sentence-transformers "transformers<5" "huggingface-hub<1.0"
```

### Step 3: Connect Google Drive

Run the Google Drive mounting cell and allow access to your Google account.

### Step 4: Load the Translation Model

The notebook downloads and loads:

`facebook/nllb-200-distilled-600M`

### Step 5: Execute the Notebook

Run the notebook cells in their original order to:

- Load the translation model.
- Configure supported languages.
- Initialize the RAG system.
- Build the ChromaDB vector stores.
- Start the translation interface.

### Step 6: Launch VERBA

Run the final Gradio application cell to launch the translator interface.

## 📊 Performance Evaluation

VERBA includes a translation benchmark to evaluate:

- Average translation time.
- Median translation time.
- Fastest translation.
- Slowest translation.
- Language-wise average latency.
- Peak GPU memory usage when CUDA is available.

The benchmark results are saved as a CSV report in Google Drive.

## 🎯 Project Objective

The main objective of VERBA is to make multilingual communication easier by combining pretrained translation technology with a retrieval-based knowledge system.

The project also explores how verified local terminology and translation memory can improve consistency for regional communication, particularly in areas such as Palghar district.

## 🔮 Future Scope

- Add verified Warli and Kokna language datasets.
- Improve translation quality using locally collected parallel datasets.
- Expand the regional terminology database.
- Add more regional languages.
- Improve translation accuracy through human verification.
- Develop a standalone web application.

## ⚠️ Disclaimer

VERBA is an academic translation prototype. Its translations may contain errors, particularly for regional languages and specialized terminology. Important translations should be checked by fluent speakers or qualified reviewers.

## 👩‍💻 Project Information

**Project Name:** VERBA  
**Project Type:** Multilingual Translation System  
**Core Technology:** NLLB-200 + RAG + ChromaDB  
**Development Environment:** Google Colab  
**Interface:** Gradio

### Connecting Languages, Connecting People 🌐
