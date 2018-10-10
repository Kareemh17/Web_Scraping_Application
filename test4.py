import pandas as pd
NASDAQ_File = pd.read_csv('NASDAQ_Company_List.csv')
Industry = NASDAQ_File['Industry']
count = 0
for i in range(len(Industry)):
    if 'Biotechnology' in str(Industry[i]) or 'Pharma' in str(Industry[i]):
        count +=1
print(count)