from pathlib import Path

import pandas as pd


def profile_dataset(file_path):
    file_path = Path(file_path)

    df = pd.read_csv(file_path)

    profile = {
        "dataset": {
            "name": file_path.stem,
            "row_count": len(df),
            "column_count": len(df.columns)
        },
        "columns": []
    }

    for column_name in df.columns:
        column = df[column_name]

        sample_values = (
            column
            .dropna()
            .drop_duplicates()
            .head(3)
            .tolist()
        )

        column_profile = {
            "name": column_name,
            "type": str(column.dtype),
            "null_count": int(column.isna().sum()),
            "null_percentage": round(
            column.isna().mean() * 100,
                2
            ),
            "distinct_count": int(column.nunique(dropna=True)),
            "sample_values": [
                str(value) for value in sample_values
            ]
        }
        
        profile["columns"].append(column_profile)

    return profile
    
if __name__ == "__main__":
    import json

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    DATASET_PATH = PROJECT_ROOT / "examples" / "nyc_311_sample.csv"

    result = profile_dataset(DATASET_PATH)

    OUTPUT_PATH = PROJECT_ROOT / "output" / "nyc_311_metadata.json"
    OUTPUT_PATH.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Metadata profile generated: {OUTPUT_PATH}")