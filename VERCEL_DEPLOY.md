# Deploy AI Traffic Signal Optimizer on Vercel

## Project Structure (Vercel-ready)

```
ai-traffic-signal/
├── api/
│   └── index.py          # Python backend (FastAPI) - REQUIRED for Vercel
├── index.py              # Vercel entry point (imports api.index)
├── public/
│   ├── index.html        # Login page (served at /)
│   ├── dashboard.html    # Main dashboard
│   ├── style.css
│   ├── login.css
│   ├── script.js
│   └── login.js
├── pyproject.toml        # Points Vercel to api.index:app
├── requirements.txt      # Python dependencies (fastapi, pydantic)
└── vercel.json
```

## Deploy Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Vercel deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com) → New Project
   - Import your GitHub repository
   - Vercel auto-detects Python + FastAPI from `api/index.py` and `pyproject.toml`
   - Click Deploy

3. **After deploy**
   - `/` → Login page
   - `/dashboard.html` → Main app (after login)
   - `/api/optimize/vehicles` → Backend API
   - `/api/health` → Health check

## Local Development

- **Frontend only**: Open `public/index.html` in browser (or use a static server)
- **With backend**: Run `uvicorn api.index:app --reload` in `backend/` for local API, or use `vercel dev` for full local simulation
