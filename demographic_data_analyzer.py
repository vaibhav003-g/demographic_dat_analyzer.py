import pandas as pd
import numpy as np
data={
    "age": [39,50,38,53,28],
    "workclass":["State-gov","Self-emp-not-inc","Private","Private","Private"],
    "fnlwgt":[77516,83311,215646,234721,338409],
    "education":["Bachelors","Bachelors","HS-grad","11th","Bachelors"],
    "education-num":[13,13,9,7,13],
    "marital-status":["Never-married","Married-civ-spouse","Divorced","Married-civ-spouse","Married-civ-spouse"],
    "occupation":["Adm-clerical","Exec-managerial","Handlers-cleaners","Handle-cleaners","Prof-specialty"],
    "relationship":["Not-in-family","Husband","Not-in-family","Husband","Wife"],
    "race":["White","White","White","Black","Black"],
    "sex":["Male","Male","Male","Male","Female"],
    "capital-gain":[2174,0,0,0,0],
    "capital-loss":[0,0,0,0,0],
    "hours-per-week":[40,13,40,40,40],
    "native-country":["United States","United States","United States","United States","Cuba"],
    "salary":["<=50K","<=50K","<=50K","<=50K","<=50K"]
    }

df=pd.DataFrame(data)
print(df)

l=len(df)
c=0
r=input("ENTER YOUR RACE:")
for i in range(l):
    if r=="White" and df["race"][i]=="White":
        c=c+1
        print("NUMBER OF WHITE PEOPLE:",c)
    elif r=="Black" and df["race"][i]=="Black":
        c=c+1
        print("NUMBER OF BLACK PEOPLE:",c)

s=input("Enter your SEX:") 
for i in range(l):
    if s=="Male" and df["sex"][i]=="Male":
        a=np.mean(df["age"][df["sex"]=="Male"])
        print("AVERAGE AGE OF MEN:",a)
    elif s=="Female" and df["sex"][i]=="Female":
        a=np.mean(df["age"][df["sex"]=="Female"])
        print("AVERAGE AGE OF WOMEN:",a)

e=input("ENTER YOUR EDUCATION:")
b=0
for i in range(l):
    if e=="Bachelors" and df["education"][i]=="Bachelors":
        b=b+1
        p=(b/5)*100
        print("PERCENTAGE OF BACHELORS:",p)
    elif e=="Masters" and df["education"][i]=="Masters":
        b=b+1
        p=(b/5)*100
        print("PERCENTAGE OF MASTERS:",p)
    elif e=="Doctorate" and df["education"][i]=="Doctorate":
        b=b+1
        p=(b/5)*100
        print("PERCENTAGE OF DOCTORATE:",p)

sal=input("ENTER YOUR SALARY:") 
x=0       
for i in range(l):
    if sal=="<=50K" and df["salary"][i]=="<=50K":
        x=x+1
        p=(x/5)*100
        print("PERCENTAGE OF <=50K:",p)
    elif sal==">50K" and df["salary"][i]==">50K":
        x=x+1
        p=(x/5)*100
        print("PERCENTAGE OF >50K:",p)

y=0
c=df["hours-per-week"].min()
print("MINIMUM HOURS PER WEEK:",c)
if sal==">50K" and df["salary"][i]==">50K":
    y=y+1
    d=(c/y)*100
    print("PERCENTAGE OF >50K with minimum hours per week:",d)

cn=input("ENTER YOUR COUNTRY:")
for i in range(l):
    if sal==">50K" and df["salary"][i]==">50K":
        z=z+1
        if cn=="United States" and df["native-country"][i]=="United States":
            a=a+1
            f=(z/a)*100
            print("PERCENTAGE OF >50K with native country:",f)
        elif cn=="India" and df["native-country"][i]=="India":
            a=a+1
            f=(z/a)*100
            print("PERCENTAGE OF >50K with native country:",f)    


