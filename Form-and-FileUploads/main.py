from fastapi import FastAPI, Form, UploadFile, File
from typing import Annotated, List
app = FastAPI()


'''==========>Login route<==========='''
# @app.post("/login")
# def login(username: str = Form(), password: str = Form()):
#     return {
#         "username": username,
#         "message": "Login successful"
#     }

'''==========>File upload route<==========='''
# @app.post("/uploadfile")
# async def upload_file(file: UploadFile = File()):
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "size": len(await file.read())
#     }

'''==========>Saving the Uploaded File<==========='''
# @app.post("/uploadfile")
# async def upload_file(file: UploadFile = File()):
#     with open(f"uploads/{file.filename}", "wb") as f:
#         f.write(await file.read())
        
#         return{
#             "message": "File upload successfully",
#             "filename": file.filename,
#         }
        
        
'''==========>Multiple File Uploads<==========='''
@app.post("/upload-multiple")
async def upload_multiple(
    files: list[UploadFile] = File()
):
    return {
        "files": [file.filename for file in files]
    }