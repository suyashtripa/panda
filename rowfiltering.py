import pandas as pd
data = {
    "Name": ['suaysh','suns','satyam','shrs'],
    "Age": [25, 26, 27, 28],
    "Salary":[5000000,666666,666666,555555],
    "Perdirmense_Score": [68,99,69,66]
}
df = pd.DataFrame(data)
high_salary = df[df['Salary']>50000]
print('Empoyee with salry > 50000')
print(high_salary)
# filtering row salry > 50k &age 40
filtered = df[(df['Age']>30) & (df['Salary']>90000)]
print(f'Employee list age> 30 + Salary > 50000')
print(filtered)