# 💓 Heart Disease Prediction App

A machine learning web application that predicts the risk of heart disease based on a patient's health metrics.

---

## 📌 About The Project

This project was built as part of a Machine Learning assignment. It uses a **Decision Tree Classifier** trained on the Cleveland Heart Disease dataset to predict whether a person is at risk of heart disease or not.

The model takes 13 medical inputs from the user and gives an instant prediction through a simple and interactive web interface built with **Streamlit**.

---

## 🧠 How The Model Works

1. **Dataset** — The model was trained on the `heart.csv` dataset (Cleveland Heart Disease dataset from UCI ML Repository)
2. **Algorithm** — Decision Tree Classifier (from scikit-learn)
3. **Training** — Features (13 columns) were used to predict the `target` column (1 = Heart Disease, 0 = No Heart Disease)
4. **Saved Model** — The trained model is saved as `heart_model.joblib` using the `joblib` library

---

## 📊 Input Features

| Feature | Description |
|--------|-------------|
| Age | Age of the patient |
| Sex | Gender (1 = Male, 0 = Female) |
| CP | Chest Pain type (0–3) |
| Trestbps | Resting Blood Pressure (mm Hg) |
| Chol | Serum Cholesterol (mg/dl) |
| FBS | Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False) |
| Restecg | Resting ECG results (0, 1, 2) |
| Thalach | Maximum Heart Rate achieved |
| Exang | Exercise Induced Angina (1 = Yes, 0 = No) |
| Oldpeak | ST depression induced by exercise |
| Slope | Slope of peak exercise ST segment (0, 1, 2) |
| CA | Number of major vessels (0–4) |
| Thal | Thalassemia type (0–3) |

---

## 🎯 Output

- 🔴 **High Risk** — "Warning: The model predicts a high risk of heart disease."
- 🟢 **No Risk** — "Good news: The model predicts no heart disease."

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming Language |
| scikit-learn | Machine Learning (Decision Tree) |
| joblib | Model Saving & Loading |
| Streamlit | Web App Interface |
| NumPy | Numerical Operations |

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── app.py                  # Streamlit web app (main file)
├── heart_model.joblib      # Trained Decision Tree model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ▶️ How To Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/heart-disease-prediction.git

# 2. Go into the folder
cd heart-disease-prediction

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 🌐 Live Demo

👉 [Click here to open the app](https://your-app-link.streamlit.app)

*(Update this link after deploying on Streamlit Cloud)*

---

## 👨‍💻 Author

**Your Name**  
Assignment Project — Machine Learning
