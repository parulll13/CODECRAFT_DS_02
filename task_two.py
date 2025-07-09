import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up Seaborn style
sns.set(style="whitegrid")

df = pd.read_csv("train.csv")

# Data Cleaning

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin due to too many missing values
df.drop('Cabin', axis=1, inplace=True)

# Drop columns not needed for EDA
df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# Exploratory Data Analysis (EDA)

# Survival Distribution
sns.countplot(x='Survived', data=df)
plt.title('Survival Distribution')
plt.show()

# Survival by Gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival by Gender')
plt.show()

# Survival by Passenger Class
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival by Passenger Class')
plt.show()

# Age Distribution
sns.histplot(data=df, x='Age', kde=True, bins=30)
plt.title('Age Distribution')
plt.show()

# Age vs Survival
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.show()

# Fare vs Survival
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare vs Survival')
plt.show()

# Survival by Embarked Port
sns.countplot(x='Survived', hue='Embarked', data=df)
plt.title('Survival by Embarkation Point')
plt.show()

# Correlation Matrix (Numeric Only)
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
