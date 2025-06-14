from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from difflib import SequenceMatcher

def token_edit_distance(orig, back):
    orig_tokens = orig.strip().split()
    back_tokens = back.strip().split()
    sm = SequenceMatcher(None, orig_tokens, back_tokens)
    edits = 1 - sm.ratio()
    return round(edits, 3), orig_tokens, back_tokens

def char_bleu_score(orig, back):
    reference = [list(orig.strip())]
    candidate = list(back.strip())
    bleu = sentence_bleu(reference, candidate, smoothing_function=SmoothingFunction().method1)
    return round(bleu, 3)

def explainability_score(edit_dist, bleu):
    score = (1 - edit_dist) * 0.5 + bleu * 0.5
    return round(score, 3)