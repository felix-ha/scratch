from fastapi.testclient import TestClient
from main import app  
import pytest
from pathlib import Path
import tempfile


@pytest.fixture
def client():
    return TestClient(app)

def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"online": "true"}

def test_post(client):
    dictionary = {"foo": "bar", "zip": 3}
    response = client.post("/post", json=dictionary)
    expected = dictionary
    actual = response.json()

    assert response.status_code == 200
    assert expected == actual

def test_increment(client):
    dictionary = {"value": 3}
    response = client.post("/increment", json=dictionary)
    expected = {"result": 4}
    actual = response.json()

    assert response.status_code == 200
    assert expected == actual


def test_uploadfile(client):
    with tempfile.TemporaryDirectory() as temp_dir:
        # setup payload
        payload ={"name": "foo", "point": 3.1415, "is_accepted": True}

        # create test .txt file
        file_name = "upload.txt"
        file_path = str(Path(temp_dir) / file_name)
        with open(file_path, "wb") as buffer:
            buffer.write(b"This is a test file!")

        # load file
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}

           # send to server
            response = client.post("/upload/payloads_and_file", data=payload, files=files)

        expected = {'name': 'foo', 'point': 3.1415, 'is_accepted': True, 'optional_value': None,'file_name': file_name, 'file_extension': '.txt', 'content': 'This is a test file!'}
        actual = response.json()

    assert response.status_code == 200
    assert expected == actual


def test_upload_files(client):
    with tempfile.TemporaryDirectory() as temp_dir:
        # create test .txt files
        file_name_1 = "upload.txt"
        file_path_1 = str(Path(temp_dir) / file_name_1)
        with open(file_path_1, "wb") as buffer:
            buffer.write(b"This is a test file!")

        file_name_2 = "upload_2.txt"
        file_path_2 = str(Path(temp_dir) / file_name_2)
        with open(file_path_2, "wb") as buffer:
            buffer.write(b"This is also a test file!")
        
        # TODO open files with context manager
        files = [('files', open(file_path_1, 'rb')), ('files', open(file_path_2, 'rb'))]

        # send to server
        response = client.post("/upload/files", files=files)
        result = response.json()

    assert result == {'file_names': [file_name_1, file_name_2], 'contents': ["This is a test file!", "This is also a test file!"]}
