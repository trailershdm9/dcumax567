# Flask + Vercel (Fresh Starter)

A minimal Flask app that runs on **Vercel** using `@vercel/python`.

## Features
- `/` — A simple page with a form
- `/api/convert` — POST JSON `{ "url": "..." }` → returns a converted URL on your current domain
- `/dl` — Demo endpoint to represent redirect/stream logic

> The converter is a **safe demo**. Replace `transform_url` in `app.py` with your real logic if needed.

## Local run
```bash
pip install -r requirements.txt
python -m flask --app app run --reload
# open http://127.0.0.1:5000
```

## Deploy on Vercel
1. Create a new project in Vercel and **Import** this folder (or push to GitHub and import).
2. No extra build settings required; `vercel.json` is included.
3. Deploy. Your app should be live at `https://your-project-name.vercel.app`.
