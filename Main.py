## Made By troy
print("Made by troy. use this as a base. so not copy and present it.")



from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn
import matplotlib.pyplot as plt

df = read_csv("./student_depression_dataset.csv", index_col=0)

print(df.shape)

dfclean = df.replace({"Male": 0, "Female":1, "Others": -1, "Unhealthy": 0,
 "Moderate": 1, "Healthy": 2, "'More than 8 hours'": 9,"'5-6 hours'": 5.5,
  "'Less than 5 hours'": 4,"'7-8 hours'": 7.5,
   "?": 0, "Yes": 1, "No": 0, "Pass": 1, "Fail": 0}).infer_objects(copy=False)

M=0
F=0
for i in dfclean["Gender"]:
    if i == 1:
        F+=1
    elif i == 0:
        M+=1


X = dfclean[["Study Satisfaction" ,"Financial Stress", "Dietary Habits", "Age", "Sleep Duration", 
"suicidal thoughts", "Family History of Mental Illness" , "CGPA", "Academic Pressure"]]
y = df["Depression"]




print(X)
model = LogisticRegression()
model.fit(X, y)

predicshun = model.predict(X)

cmatrix = confusion_matrix(y, predicshun)

plt.figure(figsize=(8, 6))
seaborn.heatmap(cmatrix, annot=True, fmt="d")
plt.xlabel('Predicted Depression Status')
plt.ylabel('Actual Depression Status')
plt.title('Confusion Matrix: Student Depression Prediction')
plt.show()
plt.clf()

plt.bar([1], [M], color="green", label=f"Male ({M})")
plt.bar([2], [F], color="pink", label=f"Female ({F})")
plt.legend()
plt.show()

acc = accuracy_score(y, predicshun)


#acc = accuracy_score(sss, y)
print(y)
print("Accuracy" ,acc*100, "%")
print("Intercept:", model.intercept_)











