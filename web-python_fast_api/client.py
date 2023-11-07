# request for the server defined in web-python_fast_api/main.py
import requests
from pathlib import Path
import tempfile


if __name__ == "__main__":
    url = "http://localhost:8000"
    response = requests.get(url)
    #print(response.json())

    response = requests.get(url + "/status")
    #print(response.json())

    response = requests.post(url + "/post", json={"foo": "bar", "zip": 3})
    #print(response.json())

    response = requests.post(url + "/increment", json={"value": 3})
    #print(response.json())


    # setup file to upload
  #  with tempfile.TemporaryDirectory() as temp_dir:
  #      file_name = Path(temp_dir) / "upload.txt"
  #      with open(file_name, "wb") as buffer:
   #         buffer.write(b"This is a test file!")

    import os
    print(os.listdir(os.getcwd()))
    file_name = str(Path().resolve() / "web-python_fast_api" / "test" / "upload.txt")
    #file_name = str(Path().resolve() / "web-python_fast_api" / "test" / "dice.jpg")

    with open(file_name, 'rb') as file:
        files = {'file': (file_name, file)}

        response = requests.post(url + "/uploadfile", files=files)
        print(response.json())