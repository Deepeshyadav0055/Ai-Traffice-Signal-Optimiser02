import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.index import app as api_app

# Create the main app
app = FastAPI()

# Add CORS middleware to allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Mount the backend API
# NOTE: The original Vercel setup likely mapped /api/index.py -> /api
# We want our local server to respond to /api/... just like the frontend expects.
# The frontend makes calls to `${API_BASE}/api/optimize/vehicles` where API_BASE is localhost:8000
# So we need to ensure the route becomes /api/api/optimize if we just mount it at /api,
# OR we need to see how api.index defines its routes.
# api/index.py defines endpoints like @app.post("/api/optimize")
# So if we mount api_app at "/", then "/api/optimize" will work.
# If we mount api_app at "/api", we'd get "/api/api/optimize".
# The frontend code uses `${API_BASE}/api/optimize`, so we want `http://localhost:8000/api/optimize` to be the valid URL.
# Since the FastAPI app in api/index.py ALREADY includes the `/api` prefix in its decorators,
# we should mount it at the root "/" but check possible conflicts with static files.
# However, FastAPI mounts match by order. We should mount the API first.

app.include_router(api_app.router)

# 2. Serve static files (frontend)
# We mount this at root "/" to serve index.html, script.js, etc.
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    print("Starting local server at http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
