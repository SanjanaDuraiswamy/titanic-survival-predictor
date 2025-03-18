# titanic-survival-predictor

This project is a **Machine Learning web app** built with **Streamlit** that predicts whether a passenger would have survived the Titanic disaster, based on input features like age, sex, ticket class, and more.



##  Project Overview

- **Goal**: Predict survival outcomes from the Titanic dataset.
- **Model**: Trained using `scikit-learn` with feature engineering and preprocessing.
- **App**: Built using `Streamlit` for an interactive user interface.

---

##  Features

- Takes user inputs like:
  - Ticket Class
  - Sex
  - Age
  - Number of siblings/spouses and parents/children aboard
  - Fare
  - Embarkation port
- Performs feature engineering (e.g., `who`, `alone`, `adult_male`)
- Displays prediction: **Survived** or **Did Not Survive**
- Clean visualization of feature importance



## Tech Stack

- Python
- scikit-learn
- pandas
- Streamlit
- matplotlib (for visualization)
- Git & GitHub



##  How to Run the App Locally

1. **Clone the repo**  
```bash
git clone https://github.com/SanjanaDuraiswamy/titanic-survival-predictor.git
cd titanic-survival-predictor

```markdown
2. **Create & activate a virtual environment**  
```bash
python -m venv titanic_venv
titanic_venv\Scripts\activate

3.**Run the app**

streamlit run app.py

