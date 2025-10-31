import json
import re

NB_PATH = "main.ipynb"
SOLUTIONS_URL = "https://github.com/ches-001/NeurIPS-2025---Google-Code-Golf-Solutions/tree/main/tasks"

if __name__ == "__main__":
    with open(NB_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    pattern = re.compile(r"# Task (\d{1,3})")
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            new_source = []
            for line in cell["source"]:
                m = pattern.search(line)
                if m and not SOLUTIONS_URL in line:
                    num = int(m.group(1))
                    formatted = f"{num:03d}"
                    replacement = f"# [Task {formatted}]({SOLUTIONS_URL}/task{formatted}.py)"
                    line = pattern.sub(replacement, line)
                new_source.append(line)
            cell["source"] = new_source

    with open(NB_PATH, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)