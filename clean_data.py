###1. charger CSV
import pandas as pd

df = pd.read_csv("input.csv", sep=";")
print ("1. Nombre de lignes :", len(df)) #print(df.head())print(df.columns)


###2. supprimer les doublons
df.drop_duplicates(keep = 'first', inplace=True)
#df.drop_duplicates(subset ="nom", keep = 'first', inplace=True) --> selon une colonne
print ("2. Nombre de lignes :", len(df))

###3. supprimer lignes sans abonnes_in
df = df.dropna(subset=["abonnes_in"]) #print(df_subset)
print ("3. Nombre de lignes :", len(df))


###4. calculer moyenne
#print stats
moy = df['abonnes_in'].mean()
print(moy)

###5. sauvegarder output_clean.csv
#to_csv