from fastapi import FastAPI
import uvicorn
from datetime import datetime, timezone

app = FastAPI()

# Runs when container starts
print(f"QA-DEPLOY-LOG-TEST-{datetime.now(timezone.utc).isoformat()}", flush=True)

@app.get("/ping")
async def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)