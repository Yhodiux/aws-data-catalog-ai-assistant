import sys
from pathlib import Path
from unittest.mock import MagicMock, patch


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from bedrock_client import invoke_model


@patch("bedrock_client.boto3.client")
def test_invoke_model(mock_boto_client):
    mock_client = MagicMock()
    mock_boto_client.return_value = mock_client

    mock_client.converse.return_value = {
        "output": {
            "message": {
                "content": [
                    {
                        "text": "Generated metadata documentation"
                    }
                ]
            }
        }
    }

    result = invoke_model("Test prompt")

    assert result == "Generated metadata documentation"

    mock_boto_client.assert_called_once_with(
        "bedrock-runtime",
        region_name="us-east-1"
    )

    mock_client.converse.assert_called_once()