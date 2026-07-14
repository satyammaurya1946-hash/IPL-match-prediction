CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    venue VARCHAR(100),
    predicted_winner VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);