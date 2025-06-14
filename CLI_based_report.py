from translation_pipeline import cycle_translate
from scoring_module import token_edit_distance, char_bleu_score, explainability_score

def run_evaluation(prompt, lang="zh"):
    print("🔍 Original Prompt:", prompt)

    en, back = cycle_translate(prompt, lang)
    print("🗣️ Translated (EN):", en)
    print("🔁 Back-Translated:", back)

    edit_dist, tok1, tok2 = token_edit_distance(prompt, back)
    bleu = char_bleu_score(prompt, back)
    score = explainability_score(edit_dist, bleu)

    print("\n📊 Evaluation:")
    print("  Token Edit Distance:", edit_dist)
    print("  Char-level BLEU Score:", bleu)
    print("  Explainability Score:", score)

    print("\n📌 Token Comparison:")
    print("  Original:", tok1)
    print("  Back    :", tok2)

if __name__ == "__main__":
    test_prompt = "我喜欢蓝色的天空"
    run_evaluation(test_prompt, lang="zh")