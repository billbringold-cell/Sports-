This adds a minimal Flask-based website for the sports predictor.

How it works
- Run the app (see below) and open the homepage.
- Upload a CSV (columns: date, home_team, away_team) or use the sample data provided.
- Click "Run Predictor" to see simple placeholder predictions. Replace the logic in sports_predictor/app.py with your trained model when ready.

Run locally
1. python -m venv .venv
2. source .venv/bin/activate   (Windows: .venv\Scripts\activate)
3. pip install -r requirements.txt
4. export FLASK_APP=sports_predictor/app.py
5. flask run

Or run directly:
    python -m sports_predictor.app
