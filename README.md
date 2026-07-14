# IPL-match-prediction
# 🏏 IPL Match Winner Prediction

A Machine Learning project that predicts the winner of an IPL (Indian Premier League) cricket match based on match conditions such as batting team, bowling team, city, target score, current score, overs completed, wickets lost, and other match statistics.

---

## 📌 Project Overview

The goal of this project is to build a machine learning model that predicts the probability of each team winning during the second innings of an IPL match.

The model analyzes historical IPL match data and provides real-time winning probabilities for both teams.

---

## 🚀 Features

- Predicts IPL match winners
- Real-time winning probability
- User-friendly interface
- Data preprocessing and feature engineering
- Machine Learning model training
- Interactive prediction system

---

## 📂 Dataset

The project uses historical IPL datasets:

- `matches.csv`
- `deliveries.csv`

These datasets contain information about:

- Teams
- Cities
- Venues
- Match results
- Ball-by-ball deliveries
- Runs scored
- Wickets
- Overs

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Pickle

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Prediction
8. Deployment using Streamlit

---

## 📈 Input Features

The model takes the following inputs:

- Batting Team
- Bowling Team
- Host City
- Target Score
- Current Score
- Overs Completed
- Wickets Lost

From these values, additional features like:

- Runs Left
- Balls Left
- Current Run Rate (CRR)
- Required Run Rate (RRR)

are calculated automatically.

---

## 📉 Model Performance

The model was trained using historical IPL data and evaluated using standard machine learning metrics.

Algorithms tested include:

- Logistic Regression
- Random Forest
- Decision Tree

The best-performing model was selected for prediction.

---

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/your-username/IPL-Winner-Prediction.git
```

### Navigate to the project folder

```bash
cd IPL-Winner-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
IPL-Winner-Prediction/
│
├── app.py
├── pipe.pkl
├── matches.csv
├── deliveries.csv
├── requirements.txt
├── README.md
└── notebooks/
```

---

## 📷 Screenshots

Add screenshots of your application here.

Example:

- Home Page
- Prediction Page
- Result Page

---

## 🎯 Future Improvements

- Deep Learning model
- Live IPL API integration
- Better feature engineering
- Win probability graph
- Player performance analysis

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Satyam Maurya**

B.Tech (Information Technology)

Data Science & Machine Learning Enthusiast

GitHub: https://github.com/satyammaurya1946-hash
