import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from prompt_builder import build_prompt


def test_build_prompt_contains_metadata():
    metadata = {
        "dataset": {
            "name": "test_dataset",
            "row_count": 10,
            "column_count": 1
        },
        "columns": [
            {
                "name": "customer_id",
                "type": "int64",
                "null_count": 0,
                "null_percentage": 0.0,
                "distinct_count": 10,
                "sample_values": ["1", "2", "3"]
            }
        ]
    }

    prompt = build_prompt(metadata)

    assert "You are a data governance and metadata assistant." in prompt
    assert "test_dataset" in prompt
    assert "customer_id" in prompt
    assert '"row_count": 10' in prompt
    assert '"distinct_count": 10' in prompt