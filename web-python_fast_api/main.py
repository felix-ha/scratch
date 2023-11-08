from typing import List
from fastapi import FastAPI, Form, UploadFile, File
import tempfile
from pathlib import Path
import shutil
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(module)s %(levelname)s - %(message)s")

app = FastAPI()

@app.get("/")
def read_root():
    logging.info("got request")
    return {"message": "Hello, World"}


@app.get("/status")
def status():
    return {"online": "true"}


@app.post("/post")
def post(body: dict):
    return body


@app.post("/increment")
def increment(body: dict):
    value = body['value']
    result = value + 1
    return {'result': result}


@app.post("/upload/payloads_and_file")
def create_upload_file(name: str = Form(...), 
                        point: float = Form(...),
                        is_accepted: bool = Form(...),
                        optional_value: bool = Form(None),
                        file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as temp_dir:
        file_name = Path(temp_dir) / file.filename
        with open(file_name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_extension = file_name.suffix

        if file_extension == ".txt":
            with open(file_name, "rb") as buffer:
                content = buffer.read()
        else:
                content = None

    return {"name": name, "point": point, "is_accepted": is_accepted, "optional_value": optional_value,  "file_name": file_name.name, "file_extension": file_extension, "content": content}



@app.post("/upload/files")
def create_upload_file(files: List[UploadFile] = File(...)):
    with tempfile.TemporaryDirectory() as temp_dir:

        file_names = []
        contents = []

        for file_current in files:
            file_current_name = Path(temp_dir) / file_current.filename
            with open(file_current_name, "wb") as buffer:
                shutil.copyfileobj(file_current.file, buffer)

            with open(file_current_name, "rb") as buffer:
                contents.append(buffer.read())

            file_names.append(file_current.filename)

    return {'file_names': file_names, 'contents': contents}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
