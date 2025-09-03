# FastAPI Hello World

A minimal FastAPI app that returns a JSON "Hello, World!" response.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- The app will start at `http://127.0.0.1:8000/`.
- Try `GET /` for the hello message and `GET /health` for a simple health check.
