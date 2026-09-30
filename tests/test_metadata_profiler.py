import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from metadata_profiler import profile_dataset


def test_profile_dataset(tmp_path):
    dataset_path = tmp_path / "sample.csv"

    df = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4],
            "state": ["MX", "MX", "US", None],
            "sales": [100.0, 200.0, 150.0, 50.0],
        }
    )

    df.to_csv(dataset_path, index=False)

    profile = profile_dataset(dataset_path)

    assert profile["dataset"]["name"] == "sample"
    assert profile["dataset"]["row_count"] == 4
    assert profile["dataset"]["column_count"] == 3

    state_profile = next(
        column
        for column in profile["columns"]
        if column["name"] == "state"
    )

    assert state_profile["null_count"] == 1
    assert state_profile["null_percentage"] == 25.0
    assert state_profile["distinct_count"] == 2
    assert state_profile["sample_values"] == ["MX", "US"]