
# 🏏 IPL Match Prediction

A Flask web application that predicts IPL (Indian Premier League) match outcomes using a Logistic Regression model trained on historical match data, with results logged to a PostgreSQL database. The whole stack runs via Docker Compose.

---

## 📌 Project Overview

The app offers two prediction modes:

- **Single Match Prediction** — pick two teams and a venue, and get the predicted winner along with a win probability, plus a simulated toss result and decision (bat/field).
- **Tournament Simulation** — run a full simulated IPL season across the league fixtures and see the output.

Every prediction made through the web UI is logged to a PostgreSQL database and can be viewed on a **History** page.

---

## 🚀 Features

- Web dashboard with links to each prediction mode
- Single-match winner prediction with win probability, toss winner, and toss decision
- Full tournament simulation
- Prediction history stored in and retrieved from PostgreSQL
- Fully containerized with Docker Compose (Flask app + Postgres DB)

---

## 📂 Repository Structure

```
IPL-match-prediction/
├── app/
│   ├── app.py                    # Flask routes (home, single, tournament, history)
│   ├── core.py                   # Data loading, model training, and prediction logic
│   ├── Match_Info.csv            # Historical IPL match data
│   ├── ipl_2025_deliveries.csv   # Ball-by-ball data for the 2025 season
│   ├── schedule_2025.csv         # 2025 season fixture schedule
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── static/
│   │   └── tailwind.css
│   └── templates/
│       ├── index.html
│       ├── single.html
│       ├── tournament.html
│       └── history.html
├── db/
│   └── init.sql                  # Creates the `predictions` table
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Flask
- pandas / NumPy
- scikit-learn (`LogisticRegression`)
- PostgreSQL (via `psycopg2`)
- Docker & Docker Compose
- Tailwind CSS (via CDN, for styling)

---

## 📊 How It Works

1. `core.py` loads historical match data (`Match_Info.csv`) and the 2025 schedule (`schedule_2025.csv`)
2. Team codes in the schedule are mapped to full team names, and placeholder fixtures (e.g. qualifiers, finals not yet decided) are filtered out
3. A `LogisticRegression` model is trained on the historical data to estimate win probabilities
4. The Flask app exposes this through:
   - `/single` — predict a specific matchup and venue
   - `/tournament` — simulate the full season
   - `/history` — view past predictions, pulled from PostgreSQL

---

## ▶️ Running the Project

This project is designed to run with Docker Compose.

```bash
git clone https://github.com/satyammaurya1946-hash/IPL-match-prediction.git
cd IPL-match-prediction
```

Create a `.env` file inside `app/` with your Postgres credentials (used by both the Flask app and the `db` service):

```
POSTGRES_DB=ipl_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

Then start the stack:

```bash
docker-compose up --build
```

The app will be available at **http://localhost:5000**.

---

## 🎯 Future Improvements

- Add data visualizations (win probability trends, team performance charts)
- Try additional models (Random Forest, Decision Tree) and compare performance
- Add authentication for the history page
- Deploy to a cloud platform

---

## 👨‍💻 Author

**Satyam Maurya**
GitHub: [@satyammaurya1946-hash](https://github.com/satyammaurya1946-hash)
