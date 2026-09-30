import json
from pathlib import Path

from prompt_loader import load_prompt


PROJECT_ROOT = Path(__file__).resolve().parent.parent
METADATA_PATH = PROJECT_ROOT / "examples" / "sales_by_state.json"


def load_metadata(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_prompt(metadata):
    instructions = load_prompt()

    metadata_json = json.dumps(
        metadata,
        indent=2,
        ensure_ascii=False
    )

    return f"""{instructions}

Dataset metadata:

{metadata_json}
"""


if __name__ == "__main__":
    metadata = load_metadata(METADATA_PATH)
    final_prompt = build_prompt(metadata)

    print(final_prompt)