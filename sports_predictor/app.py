from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "change-me"

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATA_PATH = os.path.join(DATA_DIR, 'upcoming_games.csv')

def load_games():
    if os.path.exists(DATA_PATH):
        try:
            return pd.read_csv(DATA_PATH)
        except Exception:
            return pd.DataFrame(columns=['date','home_team','away_team'])
    return pd.DataFrame(columns=['date','home_team','away_team'])

@app.route('/', methods=['GET','POST'])
def index():
    df = load_games()
    predictions = None
    if request.method == 'POST':
        # Simple placeholder predictor: predict "Home" if home_team length >= away_team length, else "Away"
        predictions = []
        for _, row in df.iterrows():
            h = str(row.get('home_team',''))
            a = str(row.get('away_team',''))
            if len(h) >= len(a):
                predictions.append('Home')
            else:
                predictions.append('Away')
    return render_template('index.html', games=df.to_dict(orient='records'), predictions=predictions)

@app.route('/upload', methods=['POST'])
def upload():
    # Accept a CSV file uploaded through the form and replace upcoming_games.csv
    f = request.files.get('file')
    if not f:
        flash('No file uploaded')
        return redirect(url_for('index'))
    os.makedirs(DATA_DIR, exist_ok=True)
    save_path = DATA_PATH
    f.save(save_path)
    flash('File uploaded')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # for local debugging
    app.run(debug=True, host='0.0.0.0', port=5000)
