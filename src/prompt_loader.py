from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = PROJECT_ROOT / "prompts" / "metadata_documentation_v1.txt"


def load_prompt():
    return PROMPT_PATH.read_text(encoding="utf-8")


if __name__ == "__main__":
    print(load_prompt())