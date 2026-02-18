import json
import os

if os.path.exists("wyniki.json"):
    os.remove("wyniki.json")

with open("zj1/teksty.json", encoding="utf-8") as file:
    data = json.load(file)

texts = [list(item.values())[0] for item in data["teksty"]]
combined_text = " ".join(texts)

combined_text = combined_text.lower()

combined_text = combined_text.replace(".", "").replace(",", "")

words = combined_text.split()

modified_words = [
    word[:-1] + word[-1].upper() if len(word) > 0 else word for word in words
]

filtered_words = [word for word in modified_words if "a" in word.lower()]

unique_words = set(filtered_words)

word_counts = {}
for word in filtered_words:
    word_counts[word] = word_counts.get(word, 0) + 1

results = {
    "połączony_tekst": combined_text,
    "lista_wyrazów": filtered_words,
    "unikatowe_wyrazy": list(unique_words),
    "liczba_wystąpień": word_counts,
}

with open("wyniki.json", "w", encoding="utf-8") as output_file:
    json.dump(results, output_file, indent=4, ensure_ascii=False)

print("Wyniki zapisano w pliku 'wyniki.json'")
