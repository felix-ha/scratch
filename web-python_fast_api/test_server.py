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
        # create test .txt file
        file_name = "upload.txt"
        file_path = str(Path(temp_dir) / file_name)
        with open(file_path, "wb") as buffer:
            buffer.write(b"This is a test file!")

        # load file
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}

            # send to server
            response = client.post("/uploadfile", files=files)

        expected = {'file_name': file_name, 'file_extension': '.txt', 'content': 'This is a test file!'}
        actual = response.json()

    assert response.status_code == 200
    assert expected == actual