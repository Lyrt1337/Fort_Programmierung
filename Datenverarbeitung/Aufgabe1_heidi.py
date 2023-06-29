import re

with open("data/heidi.md", "r", encoding="utf-8") as f:
    heidi_data = f.read()

new_name = "Mia"
heidi_data_changed = re.sub(r"Heidi", new_name, heidi_data)

with open(f"data/{new_name}.md", "w", encoding="utf-8") as w:
    w.write(heidi_data_changed)
