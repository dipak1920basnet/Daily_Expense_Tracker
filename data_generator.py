# This code is generated with Chatgpt. 

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

rows = 1500

categories = [
    "Groceries","Transport","Dining","Entertainment","Rent",
    "Utilities","Shopping","Fuel","Health","Subscriptions",
    "groccery","entertaiment","utilties",""
]

payment_modes = ["UPI","upi","Upi","Cash","cash","Credit Card","Debit Card","Bank Transfer","UPI ",""]

start_date = datetime(2024,1,1)

data = []

for i in range(rows):
    date = start_date + timedelta(days=random.randint(0,450))
    date_formats = [
        date.strftime("%Y-%m-%d"),
        date.strftime("%d-%m-%y"),
        date.strftime("%Y/%m/%d"),
        date.strftime("%b %d %Y")
    ]
    
    row = [
        random.choice(date_formats),
        random.choice(categories),
        round(random.uniform(-500, 85000),2),
        random.choice(payment_modes)
    ]
    
    if random.random() < 0.05:
        data.append(row)  # duplicates
        
    data.append(row)

df = pd.DataFrame(data, columns=["Date","Category","Amount","Payment_Mode"])

df.loc[df.sample(frac=0.04).index, "Amount"] = 0
df.loc[df.sample(frac=0.03).index, "Category"] = None

df.to_csv("messy_expense_dataset.csv", index=False)

print("messy_expense_dataset.csv generated successfully!")
