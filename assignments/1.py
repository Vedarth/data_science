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
    Points = 3*df['Gold.2'] + 2*df['Silver.2'] + 1*df['Bronze.2']
    return Points
answer_four()

def answer_five():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    x = counties_df.groupby('STNAME').count()['SUMLEV']
    ans = x.idxmax()
    return ans

answer_five()

def answer_six():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    top_counties_df = counties_df.sort_values(by=['STNAME','CENSUS2010POP'],ascending=False).groupby('STNAME').head(3)
    ans = top_counties_df.groupby('STNAME').sum().sort_values(by='CENSUS2010POP', ascending=False).head(3).index.tolist()
    return ans
answer_six()

def answer_seven():
    max_abs_change = 0
    abs_changes = list()
    abs_change = 0
    for i in range(3193):
        abs_change = 0
        abs_changes = []
        for j in range(6):
            abs_changes.append(census_df.iloc[i][9+j])
            abs_change = abs(max(abs_changes) - min(abs_changes))
        if max_abs_change < abs_change:
            max_abs_change = abs_change
            st = census_df.iloc[i].iloc[6]
    return st
answer_seven()

def answer_eight():
    index_o = list()
    stname = list()
    ctyname = list()
    for i in range(len(census_df)):
        if census_df.iloc[i][1] == 2 or census_df.iloc[i][1] == 1:
            if str(census_df.iloc[i][6]).split()[0] == 'Washington':
                if census_df.iloc[i][14] > census_df.iloc[i][13]:
                    stname.append(census_df.iloc[i][5])
                    ctyname.append(census_df.iloc[i][6])
                    index_o.append(census_df.index[i])
    
    standct = list()
    for i in range(len(stname)):
        st,ct = stname[i], ctyname[i]
        st_ct = pd.Series({'STNAME':st, 'CTYNAME':ct})
        standct.append(st_ct)
    df = pd.DataFrame(standct, index =index_o)
    return df
answer_eight()