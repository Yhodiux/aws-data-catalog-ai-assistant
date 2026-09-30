import os

import boto3


DEFAULT_REGION = "us-east-1"
DEFAULT_MODEL_ID = "us.amazon.nova-2-lite-v1:0"

REGION = os.getenv("AWS_REGION", DEFAULT_REGION)
MODEL_ID = os.getenv("BEDROCK_MODEL_ID", DEFAULT_MODEL_ID)


def invoke_model(prompt):
    client = boto3.client(
        "bedrock-runtime",
        region_name=REGION
    )

    response = client.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 1500,
            "temperature": 0.2
        }
    )

    return response["output"]["message"]["content"][0]["text"]