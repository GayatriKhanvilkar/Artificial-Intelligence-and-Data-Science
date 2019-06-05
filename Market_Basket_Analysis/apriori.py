import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_excel('Online Retail.xlsx')
# print(df.head())

df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)  # drop row where InvoiceNo is null
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]  #remove the credit transactions from InvoiceNo

basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
# print(basket_sets.['POSTAGE'])
basket_sets.drop('POSTAGE', inplace=True, axis=1)

frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules.head())

# 2 itemset
rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]

# 3 itemsets
rules['antecedents_len'] = rules['antecedents'].apply(lambda  x: len(x))

r = rules[ (rules['antecedents_len'] >= 2) & (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]
print(r)
print(basket['ALARM CLOCK BAKELIKE GREEN'].sum())

print(basket['ALARM CLOCK BAKELIKE RED'].sum())

basket2 = (df[df['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

basket_sets2 = basket2.applymap(encode_units)
basket_sets2.drop('POSTAGE', inplace=True, axis=1)
frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

rules2[ (rules2['lift'] >= 4) &
        (rules2['confidence'] >= 0.5)]

