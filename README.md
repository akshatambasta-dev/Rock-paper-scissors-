# Rock-Paper-Scissors

A simple Rock-Paper-Scissors game with an HTML/CSS/JavaScript frontend and a Python Flask backend.

## Run locally

1. Install Python 3.
2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python app.py
   ```

4. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Deploy to Render

This repository is configured for a Python web service.

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

Render will provide the port automatically. The app binds to `0.0.0.0` when run directly, and Gunicorn serves it in production.
