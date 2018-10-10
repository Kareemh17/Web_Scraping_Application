s = 'Adamas Pharmaceuticals Inc (ADMS) Receives $47.71 Average  Price Target from Analysts'
list_1 = ['%',  'clinical']
if any(n in list_1 for n in s.lower()):
    print(s.lower())
