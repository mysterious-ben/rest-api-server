from typing import Optional

from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/data/sample")
def read_data_sample(json: bool = True):
    if json:
        return {"data": "Here is a sentence for you"}
    else:
        return "Here is a sentence for you."


@app.get("/data/raise")
def read_data_withcode(code: int = 404, error: bool = True):
    # response.headers["X-Cat-Dog"] = "alone in the world"
    if error:
        raise HTTPException(code, f"raise exception with {code=}")
    else:
        return {"data": "ssdfsd3sdff333f", "code": code, "with_error": error}


@app.get("/data/wronglength")
def read_data_length(error: bool = True):
    content = (
        b'{"success": true, "result": {"records": [], "fields": [{"type": "int4", "id": "_id"}]}'
    )
    headers = {
        "Date": "Thu, 09 Dec 2021 09:06:50 GMT",
        "Content-Type": "application/json;charset=utf-8",
        "Content-Length": "86",
    }
    if error:
        headers["Content-Length"] = "629"
    return Response(content=content, headers=headers)
