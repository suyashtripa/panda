import pandas as pd

data = {
    "Name": ["suyash","sans","yash","satya","sun"],
    "Age": [22,23,23,24,20],
    "Gender": ["Male","Female","Male","Female","Male"],
    "Salary" :[40000,555555,55555,444444,444556]
}
df = pd.DataFrame(data)
print(pd)
df["Bonous"]=df['Salary']*0.1
print(df)