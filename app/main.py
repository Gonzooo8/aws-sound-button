from pathlib import Path

import boto3
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

AWS_REGION = "ap-northeast-1"
DYNAMODB_TABLE_NAME = "aws-sound-button-button-count"

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
button_count_table = dynamodb.Table(DYNAMODB_TABLE_NAME)

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
