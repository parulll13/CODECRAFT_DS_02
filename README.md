# CODECRAFT_DS_02

## 🚢 Titanic Dataset Exploratory Data Analysis (EDA)

This project performs data cleaning and exploratory data analysis (EDA) on the Titanic dataset to uncover patterns related to passenger survival.

---

## 📁 Files

- `titanic_eda.py` — Python script that performs data cleaning and various visualizations.
- `train.csv` — Titanic dataset used for analysis (should be placed in the same folder or a `data/` directory).

---

## 🧹 Data Cleaning Steps

- Filled missing `Age` values with the median.
- Filled missing `Embarked` values with the mode.
- Dropped `Cabin` due to excessive missing data.
- Removed columns not useful for visualization: `PassengerId`, `Name`, `Ticket`.

---

## 📊 EDA Visualizations

1. **Survival Distribution**  
   - Countplot of survived vs. not survived passengers.

2. **Survival by Gender**  
   - Comparison of survival rates between male and female passengers.

3. **Survival by Passenger Class**  
   - Analysis of survival trends based on passenger class (1st, 2nd, 3rd).

4. **Age Distribution**  
   - Histogram showing the age distribution of passengers.

5. **Age vs. Survival**  
   - Boxplot comparing age of survivors vs. non-survivors.

6. **Fare vs. Survival**  
   - Boxplot comparing fare paid by survivors vs. non-survivors.

7. **Survival by Embarked Port**  
   - Countplot of survival rates based on the port of embarkation.

8. **Correlation Matrix**  
   - Heatmap showing correlation between numeric variables.

---

## 🛠️ Libraries Used

- `pandas`
- `seaborn`
- `matplotlib`

Install them via:
```bash
pip install pandas seaborn matplotlib
