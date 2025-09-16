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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
