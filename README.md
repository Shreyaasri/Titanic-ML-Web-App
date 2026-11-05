# 🚢 Titanic Survival Predictor

### An Interactive Machine Learning Web App

A modern, interactive web application that estimates the probability of survival for a Titanic passenger using a trained Decision Tree Classifier.

Built with Python, Streamlit, Pandas, and Scikit-learn as part of the **InternCircle Data Science & AI Project 05**.

## ✨ Features

- 🎟️ **Ticket Class Selection** — Choose first, second, or third class.
- 👤 **Passenger Details** — Select passenger sex and age.
- 💳 **Fare Input** — Adjust the ticket fare using an interactive slider.
- 🤖 **Machine Learning Prediction** — Generate an estimated survival probability.
- 📊 **Interactive Results** — View the probability and prediction summary.
- 🎨 **Custom UI Design** — Ocean-inspired dark theme with teal and gold accents.
- ⚡ **Cached Model Loading** — Load the trained model efficiently using Streamlit caching.
- 🛡️ **Error Handling** — Display a friendly message if the model file is missing or prediction fails.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Custom CSS

## 📂 Project Structure

```text
Titanic-ML-Web-App/
├── app.py
├── model.joblib
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Titanic-ML-Web-App.git
cd Titanic-ML-Web-App
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

The application will provide a local URL that you can open in your browser.

## 🧠 How It Works

1. The user selects passenger class, sex, age, and fare.
2. The application prepares these values in the feature order expected by the trained model.
3. The saved Decision Tree model loads from `model.joblib`.
4. The model calculates the estimated survival probability.
5. The application displays the probability and a prediction summary.

## 📊 Model Information

The model was trained using the Titanic dataset available through Seaborn. The input features are:

- `pclass`
- `sex`
- `age`
- `fare`

The model was developed and evaluated in Project 04 before being integrated into this interactive web application.

## ⚠️ Limitations

- The model uses only four passenger features.
- Records with missing age values were excluded during preprocessing.
- The dataset represents historical Titanic passengers.
- Predictions are estimates based on learned patterns and are not guarantees of actual outcomes.

## 👩‍💻 Author

**Shreya Kumari**

Data Science & AI | InternCircle Project 05

## 📄 Disclaimer

This project is for educational purposes only. It demonstrates how a trained machine learning model can be integrated into a web application. It should not be used to make real-world decisions.
