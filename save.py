import pandas as pd
data={
    "Name": ["suaysh","suydf","Sdefc"],
    "Age" : [12,33,34],
    "city" : ["kanpur","new","svffvv"]

}
df = pd.DataFrame(data)
print(df)
df.to_json("output.json",index=True)

