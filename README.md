# 🔁 Cross-Lingual Prompt Roundtrip Evaluator

A lightweight tool to evaluate whether a translated prompt retains its semantic meaning using back-translation and similarity scoring.

## 🔧 Features
- Translates prompt → English → original language
- Computes:
  - Token-level edit distance
  - Char-level BLEU score
  - Final explainability score (0–1)
- CLI-style output

## 💡 Technologies Used
- Hugging Face Transformers
- BLEU (nltk)
- SequenceMatcher (edit distance)

## 🧪 Use Cases
- Translation QA
- Prompt engineering validation
- Multilingual semantic alignment

## 📋 Example Output
```txt
Token Edit Distance: 0.0
Char-level BLEU Score: 1.0
Explainability Score: 1.0
