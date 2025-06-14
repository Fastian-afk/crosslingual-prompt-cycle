from transformers import pipeline


def get_translation_pipeline(src_lang, tgt_lang):
    model_map = {
        ("zh", "en"): "Helsinki-NLP/opus-mt-zh-en",
        ("en", "zh"): "Helsinki-NLP/opus-mt-en-zh"
    }
    model_name = model_map.get((src_lang, tgt_lang))
    if not model_name:
        raise ValueError(f"Unsupported language pair: {src_lang} → {tgt_lang}")

    return pipeline("translation", model=model_name)


def cycle_translate(prompt, src_lang="zh"):
    to_en = get_translation_pipeline(src_lang, "en")
    en_translation = to_en(prompt, max_length=512)[0]["translation_text"]

    back = get_translation_pipeline("en", src_lang)
    back_translation = back(en_translation, max_length=512)[0]["translation_text"]

    return en_translation, back_translation