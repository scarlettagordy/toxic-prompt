# file: categorize_meaning_shifts_v2.py
import difflib
import re
import csv

# --- Helper functions ---

def sentiment_hint(text: str) -> float:
    """Very simple positive/negative hint score from keywords (heuristic)."""
    pos_words = ["thanks", "appreciate", "great", "thoughtful", "helpful", "glad"]
    neg_words = ["stupid", "useless", "loser", "disgrace", "get lost", "insensitive", "dismissive", "annoyed", "frustrating"]
    t = text.lower()
    score = 0
    for w in pos_words: 
        if w in t: score += 1
    for w in neg_words:
        if w in t: score -= 1
    return score

def addressed_target(text: str) -> str:
    """Rough guess of target: second-person 'you' vs neutral/first-person."""
    t = text.lower()
    if "you" in t or "you're" in t or "you " in t:
        return "you-directed"
    return "not-you-directed"

def classify_shift(original: str, detox: str) -> dict:
    """Return a dict with similarity, coarse shift (Minor/Moderate/Major), and type label."""
    sim = difflib.SequenceMatcher(None, original, detox).ratio()

    # Coarse magnitude
    if sim >= 0.95:
        magnitude = "No/Minor"
    elif sim >= 0.70:
        magnitude = "Moderate"
    else:
        magnitude = "Major"

    # Sentiment / polarity hints
    s_orig = sentiment_hint(original)
    s_detox = sentiment_hint(detox)
    polarity_flip = (s_orig > 0 and s_detox < 0) or (s_orig < 0 and s_detox > 0)

    # Target change: who is being addressed?
    tgt_orig = addressed_target(original)
    tgt_detox = addressed_target(detox)
    target_changed = (tgt_orig != tgt_detox)

    # Tone softening (common in detox)
    toned_down = (s_orig < s_detox) if s_orig < 0 else ("stupid" in original.lower() or "loser" in original.lower())

    # Build a label set
    labels = []
    if polarity_flip:
        labels.append("Polarity Flip")
    if target_changed:
        labels.append("Subject/Target Change")
    if toned_down:
        labels.append("Tone Softened")

    # If nothing specific triggered, classify from magnitude
    if not labels:
        if magnitude == "No/Minor":
            labels.append("Minor Rephrasing")
        elif magnitude == "Moderate":
            labels.append("Moderate Paraphrase")
        else:
            labels.append("Meaning Shift (Unclassified)")

    return {
        "similarity": round(sim, 3),
        "magnitude": magnitude,
        "labels": "; ".join(labels),
        "sentiment_hint_original": s_orig,
        "sentiment_hint_detox": s_detox,
        "target_original": tgt_orig,
        "target_detox": tgt_detox
    }

# --- Load data ---

with open("sample_outputs_v2.txt", "r", encoding="utf-8") as f:
    originals = [line.strip() for line in f if line.strip()]

with open("sample_outputs_v2_detoxified.txt", "r", encoding="utf-8") as f:
    detoxified_raw = [line.strip() for line in f if line.strip()]

# The detoxified file may have "1. ...", "2. ..." prefixes — strip them
detoxified = []
for line in detoxified_raw:
    line = re.sub(r"^\d+\.\s*", "", line)
    detoxified.append(line)

assert len(originals) == len(detoxified), f"Line count mismatch: {len(originals)} vs {len(detoxified)}"

# --- Compare and export ---

rows = []
txt_lines = []
for i, (orig, det) in enumerate(zip(originals, detoxified), start=1):
    info = classify_shift(orig, det)
    rows.append({
        "id": i,
        "original": orig,
        "detoxified": det,
        "similarity": info["similarity"],
        "magnitude": info["magnitude"],
        "labels": info["labels"],
        "sentiment_hint_original": info["sentiment_hint_original"],
        "sentiment_hint_detox": info["sentiment_hint_detox"],
        "target_original": info["target_original"],
        "target_detox": info["target_detox"],
    })

    txt_lines.append(
        f"{i}. similarity={info['similarity']} | magnitude={info['magnitude']} | labels={info['labels']}\n"
        f"   Original:   {orig}\n"
        f"   Detoxified: {det}\n"
    )

# Save CSV
with open("meaning_shift_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

# Save human-readable TXT
with open("meaning_shift_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(txt_lines))

print("Done. Wrote meaning_shift_report.csv and meaning_shift_report.txt")