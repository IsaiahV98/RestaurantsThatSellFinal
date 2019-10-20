import pandas
df = pandas.read_csv('tacosAndBurritos.csv')
df = df.dropna(subset=['latitude'])
df = df.dropna(subset=['longitude'])
del df['dateAdded']
del df['dateUpdated']
del df['menus.dateSeen']
df = df.drop_duplicates(['latitude', 'longitude'])
df.to_csv('tacosAndBurritosModFinal.csv')


