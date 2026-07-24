import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

plt.scatter(df["Hours"], df["Score"])
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")

plt.show()