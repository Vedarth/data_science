costs = df['Cost']
costs

costs+=2
costs

df

!cat olympics.csv

df = pd.read_csv('olympics.csv')
df.head()

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()

df.columns

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()

df['country'] = df.index
df = df.set_index('Gold')
df.head()

df = df.reset_index()
df.head()

df = pd.read_csv('census.csv')
df.head()

df['SUMLEV'].unique()

df=df[df['SUMLEV'] == 50]
df.head()

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME', 'CTYNAME'])
df.head()

df.loc['Michigan', 'Washtenaw County']

df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]
