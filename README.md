---
title: VERBA 2.0
emoji: 🌐
colorFrom: purple
colorTo: indigo
sdk: gradio
sdk_version: 5.29.0
app_file: app.py
pinned: false
---

# VERBA 2.0

Connecting Languages, Connecting People.

A multilingual translation prototype powered by Meta NLLB-200 Distilled 600M.

## Notes
- The model is downloaded from Hugging Face when the Space starts for the first time.
- First startup can take several minutes.
- The app currently offers 22 language choices supported by the configured NLLB tokenizer.
- Warli, Kokna, and other local Palghar languages are future development goals and are not currently verified translation options.
- This academic prototype should not be relied on for legal, medical, or other high-stakes translations.

## Model license
The model repository specifies CC-BY-NC-4.0. Check the model card and license terms before public or commercial deployment:
https://huggingface.co/facebook/nllb-200-distilled-600M
