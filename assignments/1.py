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
    x = max(df['Gold'])
    ans = df[df['Gold'] == x].index.tolist()
    return ans[0]

answer_one()

def answer_two():
    x = max(df['Gold'] - df['Gold.1'])
    ans = df[(df['Gold'] - df['Gold.1']) == x].index.tolist()
    return ans[0]
answer_two()

def answer_three():
    df_gold = df[(df['Gold']>0) & (df['Gold.1']>0)]
    df_max_diff = (abs(df_gold['Gold']-df_gold['Gold.1'])/df_gold['Gold.2'])
    return df_max_diff.idxmax()
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
    counties_df = census_df[census_df['SUMLEV'] == 50]
    counties_df['pop_change'] = abs(counties_df['POPESTIMATE2015'] - counties_df['POPESTIMATE2014'])+abs(counties_df['POPESTIMATE2014'] - counties_df['POPESTIMATE2013'])+abs(counties_df['POPESTIMATE2013'] - counties_df['POPESTIMATE2012'])+abs(counties_df['POPESTIMATE2012'] - counties_df['POPESTIMATE2011'])+abs(counties_df['POPESTIMATE2011'] - counties_df['POPESTIMATE2010'])
    a = max(counties_df['pop_change'])
    ans = counties_df['CTYNAME'][counties_df['pop_change']==a].tolist()
    return ans[0]


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