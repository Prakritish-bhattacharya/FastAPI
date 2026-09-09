# FastAPI — File Uploads & Forms
## Interview Preparation Notes

> **Goal:** Revise the important FastAPI concepts around Forms and File Uploads without unnecessary theory.

---

## 1. Form Data

FastAPI normally expects JSON for request bodies when using a Pydantic model.

For HTML form data, use `Form`.

```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
def login(
    username: str = Form(),
    password: str = Form()
):
    return {
        "username": username,
        "message": "Login successful"
    }
```

### Key Interview Point

`Form()` tells FastAPI that the value should come from **form data**, not JSON.

---

## 2. File Upload

Use `UploadFile` and `File` for uploaded files.

```python
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File()):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
```

### Important

- `UploadFile` represents the uploaded file.
- `File()` tells FastAPI to receive the value as a file upload.
- The endpoint is usually `async` because file operations can be asynchronous.

---

## 3. Important `UploadFile` Attributes

```python
file.filename
file.content_type
file.file
```

| Attribute | Meaning |
|---|---|
| `filename` | Original name of the uploaded file |
| `content_type` | MIME type, e.g. `image/png` |
| `file` | Underlying file-like object |

Example:

```python
@app.post("/upload")
async def upload_file(file: UploadFile = File()):
    return {
        "name": file.filename,
        "type": file.content_type
    }
```

---

## 4. Reading an Uploaded File

```python
contents = await file.read()
```

Then:

```python
with open("uploads/example.png", "wb") as f:
    f.write(contents)
```

### ⚠️ Important Interview Trap

Do **not** unnecessarily read the file twice:

```python
print(await file.read())
f.write(await file.read())
```

The first `read()` consumes the stream. The second read may return empty data.

Better:

```python
contents = await file.read()

with open("uploads/example.png", "wb") as f:
    f.write(contents)
```

---

## 5. Saving Uploaded Files

Basic approach:

```python
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File()):

    contents = await file.read()

    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }
```

### Common Error

If `uploads/` does not exist:

```text
FileNotFoundError
```

Create the directory first.

Better approach:

```python
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
```

---

# 6. `UploadFile` vs `bytes`

FastAPI supports both approaches.

### Using `bytes`

```python
from fastapi import File

@app.post("/upload")
async def upload_file(file: bytes = File()):
    return {"size": len(file)}
```

### Using `UploadFile`

```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload_file(file: UploadFile = File()):
    return {"filename": file.filename}
```

### Interview Answer

**Why prefer `UploadFile`?**

`UploadFile` provides useful metadata such as filename and content type and is designed for file uploads without requiring the entire file to be represented directly as a `bytes` value.

---

# 7. Multiple File Uploads

Use `list[UploadFile]`.

```python
@app.post("/upload-multiple")
async def upload_files(
    files: list[UploadFile] = File()
):
    return [
        {
            "filename": file.filename,
            "content_type": file.content_type
        }
        for file in files
    ]
```

---

# 8. File + Form Data

You can receive form fields and files together.

```python
from fastapi import FastAPI, File, Form, UploadFile

@app.post("/upload")
async def upload(
    username: str = Form(),
    file: UploadFile = File()
):
    return {
        "username": username,
        "filename": file.filename
    }
```

### Important

File uploads and form fields use **`multipart/form-data`**.

---

# 9. Required Dependency

For forms and file uploads, FastAPI requires:

```bash
pip install python-multipart
```

Without it, form/file parsing will not work correctly.

---

# 10. `multipart/form-data`

### Interview Question

**What content type is normally used for file uploads?**

Answer:

```text
multipart/form-data
```

It allows a request to contain multiple parts, such as:

- text/form fields
- files

---

# 11. File Validation

Never blindly trust an uploaded file.

Important things to validate:

- File size
- File type
- File extension
- Filename
- Allowed formats

Example:

```python
ALLOWED_TYPES = {
    "image/png",
    "image/jpeg"
}

if file.content_type not in ALLOWED_TYPES:
    raise HTTPException(
        status_code=400,
        detail="Unsupported file type"
    )
```

---

# 12. Filename Security

Avoid blindly using:

```python
f"uploads/{file.filename}"
```

In production, filenames should be sanitized or replaced with a generated unique filename.

Example idea:

```python
from uuid import uuid4

filename = f"{uuid4()}_{file.filename}"
```

### Interview Point

Never assume the client-provided filename is safe.

---

# 13. Reading Large Files

For large files, avoid unnecessarily loading the entire file into memory:

```python
contents = await file.read()
```

Instead, process the file in chunks when appropriate.

```python
while chunk := await file.read(1024 * 1024):
    # process chunk
    pass
```

This helps reduce memory usage.

---

# 14. Common Interview Questions

### Q1. What is `UploadFile`?

`UploadFile` is FastAPI's file-upload abstraction that provides file metadata and a file-like interface.

### Q2. What is `File()`?

`File()` tells FastAPI that a parameter should be received from uploaded file data.

### Q3. What is `Form()`?

`Form()` tells FastAPI that a parameter should come from form data.

### Q4. What content type is used for file uploads?

```text
multipart/form-data
```

### Q5. Why use `async def` with file uploads?

It allows asynchronous file operations such as:

```python
await file.read()
```

### Q6. What happens if you call `file.read()` twice?

The first read consumes the available stream data. A subsequent read may return empty data unless the file position is reset.

### Q7. How do you upload multiple files?

```python
files: list[UploadFile] = File()
```

### Q8. What package is required for forms and multipart requests?

```bash
python-multipart
```

---

# 15. Quick Revision

```text
Form Data
    ↓
Form()

File Upload
    ↓
UploadFile + File()

Multiple Files
    ↓
list[UploadFile]

File + Form
    ↓
Form() + File()

Request Content Type
    ↓
multipart/form-data

Required Package
    ↓
python-multipart

Read File
    ↓
await file.read()
```

---

# 16. Interview Checklist

Before moving on, be able to explain:

- [ ] `Form()`
- [ ] `File()`
- [ ] `UploadFile`
- [ ] `UploadFile.filename`
- [ ] `UploadFile.content_type`
- [ ] `await file.read()`
- [ ] Why reading twice is a problem
- [ ] Multiple file uploads
- [ ] File + form data
- [ ] `multipart/form-data`
- [ ] `python-multipart`
- [ ] Basic file validation
- [ ] Filename security
- [ ] Handling large files
