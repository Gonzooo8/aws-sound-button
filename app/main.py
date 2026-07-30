from pathlib import Path

import boto3
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

AWS_REGION = "ap-northeast-1"
DYNAMODB_TABLE_NAME = "aws-sound-button-button-count"
S3_BUCKET_NAME = "aws-sound-button-audio-392789867247"
S3_AUDIO_KEY = "audio/duck-toy-sound.mp3"

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
button_count_table = dynamodb.Table(DYNAMODB_TABLE_NAME)
s3 = boto3.client("s3", region_name=AWS_REGION)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


@app.get("/")
def read_root():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/api/count")
def get_count():
    response = button_count_table.get_item(
        Key={"id": "button"}
    )

    item = response.get("Item")

    if item is None:
        return {"count": 0}

    return {"count": int(item["count"])}


@app.post("/api/count")
def increment_count():
    response = button_count_table.update_item(
        Key={"id": "button"},
        UpdateExpression="ADD #count :increment",
        ExpressionAttributeNames={
            "#count": "count",
        },
        ExpressionAttributeValues={
            ":increment": 1,
        },
        ReturnValues="UPDATED_NEW",
    )

    return {"count": int(response["Attributes"]["count"])}


@app.get("/api/audio")
def get_audio():
    response = s3.get_object(
        Bucket=S3_BUCKET_NAME,
        Key=S3_AUDIO_KEY,
    )

    return StreamingResponse(
        response["Body"],
        media_type=response.get("ContentType", "audio/mpeg"),
    )
