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
    con = df.iloc[0]
    return str(con)
answer_zero()

def answer_one():
    max_gold = 0
    for i in range(len(df)):
        if max_gold < df.iloc[i].iloc[1]:
            max_gold = df.iloc[i].iloc[1]
            con = df.iloc[i]
    return con
answer_one()

def answer_two():
    dif = 0
    for i in range(len(df)):
        if dif < (df.iloc[i][1] - df.iloc[i][6]):
            dif = df.iloc[i][1] - df.iloc[i][6]
            con = df.iloc[i]
    return str(dif)
answer_two()

def answer_three():
    lar_diff = 0
    for i in range(len(df)):
        summ_gold = df.iloc[i][1]
        win_gold = df.iloc[i][6]
        diff = (summ_gold - win_gold)/(summ_gold + win_gold)
        if (lar_dif < diff) and (summ_gold>=1) and (win_gold>=1):
            lar_diff = diff
            con = df.iloc[i]
    return str(con)
answer_three()

def answer_four():
    Points = list()
    for i in range(len(df)):
        Points.append(df.iloc[i][11]*3 + df.iloc[i][12] + df.iloc[i][13])
    Points = pd.Series(Points) 
    return Points
answer_four()

def answer_five():
    county = 0
    max_county = 0
    j=1
    st = len(census_df)
    for i in range(3193):
        county = 0
        while census_df.iloc[i].iloc[3] == j:
            county += (census_df.iloc[i]).iloc[4]
            i+=1
        j+=1
        if max_county<county:
            max_county = county
            st = census_df.iloc[i][5]
    return st
answer_five()
