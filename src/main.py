import sys
from pathlib import Path

from botocore.exceptions import BotoCoreError, ClientError
from pandas.errors import EmptyDataError, ParserError

from metadata_profiler import profile_dataset
from prompt_builder import build_prompt
from bedrock_client import invoke_model


def main():
    if len(sys.argv) != 2:
        print("Usage: python src\\main.py <dataset.csv>")
        sys.exit(1)

    dataset_path = Path(sys.argv[1])

    if not dataset_path.exists():
        print(f"Error: file not found: {dataset_path}")
        sys.exit(1)

    try:
        print(f"Loading dataset: {dataset_path}")
        print("Profiling metadata...")
        metadata = profile_dataset(dataset_path)

        print("Building prompt...")
        prompt = build_prompt(metadata)

        print("Invoking Amazon Bedrock...")
        response = invoke_model(prompt)

    except (EmptyDataError, ParserError) as error:
        print(f"Error reading dataset: {error}")
        sys.exit(1)

    except (BotoCoreError, ClientError) as error:
        print(f"Error invoking Amazon Bedrock: {error}")
        sys.exit(1)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"{dataset_path.stem}_documentation.md"

    output_path.write_text(
        response,
        encoding="utf-8"
    )

    print("\n=== AI-GENERATED DOCUMENTATION ===\n")
    print(response)

    print(f"\nDocumentation saved to: {output_path}")


if __name__ == "__main__":
    main()