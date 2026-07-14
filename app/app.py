from flask import Flask, render_template, request
import core
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )

def log_prediction(team1, team2, venue, winner):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO predictions (team1, team2, venue, predicted_winner) VALUES (%s, %s, %s, %s)",
            (team1, team2, venue, winner)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB log failed: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/single", methods=["GET", "POST"])
def single():
    teams = sorted(core.CURRENT_TEAMS.values())
    venues = sorted(core.venue_encoding.keys())
    result = None
    if request.method == "POST":
        t1 = request.form.get("team1")
        t2 = request.form.get("team2")
        v = request.form.get("venue")
        winner, meta = core.predict_single_match(t1, t2, v)
        result = {
            "winner": winner,
            "prob": round(meta["p_win_team1"], 2),
            "toss": meta["toss_winner"],
            "decision": meta["toss_decision"]
        }
        log_prediction(t1, t2, v, winner)
    return render_template("single.html", teams=teams, venues=venues, result=result)

@app.route("/tournament", methods=["GET", "POST"])
def tournament():
    output = None
    if request.method == "POST":
        import io
        from contextlib import redirect_stdout
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            core.run_one_tournament()
        output = buffer.getvalue()
        log_prediction("Tournament", "All Teams", "Various", "See output")
    return render_template("tournament.html", output=output)

@app.route("/history")
def history():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT team1, team2, venue, predicted_winner, created_at FROM predictions ORDER BY created_at DESC LIMIT 20")
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        rows = []
        print(f"DB fetch failed: {e}")
    return render_template("history.html", predictions=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)