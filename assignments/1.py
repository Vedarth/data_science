import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    max_gold = 0
    for i in range(len(df)):
        if max_gold < df.iloc[i].iloc[1]:
            max_gold = df.iloc[i].iloc[1]
            con = df.iloc[i]
    return con

def answer_one():
    for i in range(len(df)):
        if max_gold < df.iloc[i].iloc[1]:
            max_gold = df.iloc[i].iloc[1]
            con = df.iloc[i]
    return con

def answer_two():
    dif = 0
    for i in range(len(df)):
        if dif < (df.iloc[1] - df.iloc[6]):
            dif = df.iloc[1] - df.iloc[6]
            con = df.iloc[i]
    return str(dif)
