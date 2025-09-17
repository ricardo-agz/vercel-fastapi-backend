from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("public/vercel.svg")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vercel + FastAPI</title>
        <link rel="icon" type="image/x-icon" href="/vercel.svg">
    </head>
    <body>
        <h1>Vercel + FastAPI</h1>
    </body>
    </html>
    """

@app.get("/temp")
def write_and_read_temp():
    """
    Write text to a temporary file under /tmp, then read it back.
    Returns the file path and the content read.
    """
    import tempfile
    import os

    text_to_write = "Hello from the temp file!"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, dir="/tmp", suffix=".txt") as tmp_file:
        tmp_file.write(text_to_write)
        temp_path = tmp_file.name

    with open(temp_path, "r") as file_handle:
        read_back_text = file_handle.read()

    try:
        os.unlink(temp_path)
        cleaned_up = True
    except Exception:
        cleaned_up = False

    return {"temp_path": temp_path, "written": text_to_write, "read_back": read_back_text, "deleted": cleaned_up}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
