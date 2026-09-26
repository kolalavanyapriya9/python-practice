'''
import pandas as pd
print("Pandas version:", pd.__version__)
print("Everything is working perfectly!")
#series with string
df=pd.Series(["ram","rani","pavan","sai"],index=[1,2,3,4])
print(df)
#series with dictionary
df=pd.Series({"name":"john","age":78})
print(df)
#list of list dataframe
df=pd.DataFrame([["ram","rani","pavan","sai"],[129,34,56,86]])
print(df)
df=pd.DataFrame([["sai",897,"hindi"],["john",876,"telugu"],["bhanu",546,"maths"]],columns=["names","marks","subject"],index=[101,201,301])
print(df)
#list of dictionary
df=pd.DataFrame({"name":["sai","bhanu","venkat"],"marks":[45,None,23],"subjects":["telugu","english","maths"]})
print(df)
print(df.isnull())
print(df.dropna())
df=df.reset_index()
print(df)
print(dir(df))
df=pd.DataFrame([["sai",897,"hindi"],["john",876,"telugu"],["bhanu",None,"maths"],["nikku",565,"science"],["nandu",789,"social"],["sri",345,"draiwng"]],columns=["names","marks","subject"])
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.dropna())
import openpyxl
df=pd.read_excel(r"C:\Users\inpro\OneDrive\Documents\Online Retail.xlsx")
print(df)
df["salary"]=0
print(df)
df.drop(["salary"],axis=1,inplace=True)
print(df)
df.drop(0,axis=0)
print(df)

'''
import matplotlib.pyplot as plt
x=["sai","bhanu","venkat"]
y=[45,78,23]
plt.plot(x,y,marker="*")
plt.title("marks of students")
plt.xlabel("names")