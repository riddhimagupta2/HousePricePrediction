# 🏠 House Price Prediction using Machine Learning

## 📖 Overview

This project predicts house prices using Machine Learning based on various house features such as living area, overall quality, garage capacity, basement area, year built, and number of bedrooms.

The model is trained using the Kaggle House Prices dataset and deployed through a Streamlit web application for real-time predictions.

---

## 🚀 Features

- House price prediction using Machine Learning
- Data preprocessing and feature engineering
- Interactive Streamlit web application
- Real-time predictions
- User-friendly interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```text
HousePricePrediction/
│
├── dataset/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
│
├── train_model.py
├── app.py
├── house_price_model.pkl
├── columns.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Dataset

Dataset: Kaggle House Prices - Advanced Regression Techniques

The dataset contains:

- Overall Quality
- Living Area
- Garage Capacity
- Basement Area
- Year Built
- Bedrooms
- Sale Price (Target Variable)

---

## ⚙️ Data Preprocessing

- Missing value handling
- Categorical feature encoding
- Feature selection
- Train-test split
- Model training

---

## 🤖 Machine Learning Model

Model Used:

- Random Forest Regressor

Why Random Forest?

- High prediction accuracy
- Handles large datasets efficiently
- Reduces overfitting
- Works well with mixed data types

---

## 📈 Evaluation Metric

The model is evaluated using:

- Mean Absolute Error (MAE)

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/riddhimagupta2/HousePricePrediction.git
cd HousePricePrediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train_model.py
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Open the Streamlit application.
2. Enter house details.
3. Click **Predict Price**.
4. View the predicted house price.

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Additional regression models
- Data visualization dashboard
- Cloud deployment
- Model explainability

---

## 👩‍💻 Author

**Riddhima Gupta**

GitHub: https://github.com/riddhimagupta2

---

## 📜 License

This project is created for educational and learning purposes.