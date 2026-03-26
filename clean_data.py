###1. charger CSV
import pandas as pd

df = pd.read_csv("input.csv", sep=";", encoding="latin1")
#print ("1. Nombre de lignes :", len(df)) #print(df.head())print(df.columns)
print("Nombre de lignes de input.csv :", len(df))


###2. supprimer les doublons
df.drop_duplicates(keep = 'first', inplace=True)
#df.drop_duplicates(subset ="nom", keep = 'first', inplace=True) --> selon une colonne
#print ("2. Nombre de lignes :", len(df))


###4. calculer moyenne
#print stats
df["abonnes_in"] = pd.to_numeric(df["abonnes_in"], errors="coerce")
moy = df['abonnes_in'].mean()
#print("4. Moyenne :",moy)


###3. supprimer lignes sans abonnes_in
df = df.dropna(subset=["abonnes_in"]) #print(df_subset)
#print ("3. Nombre de lignes :", len(df))
print("Nombre de lignes de output.csv :", len(df))

###5. sauvegarder output_clean.csv
df.to_csv("output.csv", sep=";", index=False, encoding="utf-8-sig")


##moyenne nb abo
print("Le nombre moyen d'abonnés est :",moy)

###top ville
# Moyenne par ville
df_ville = df.groupby("ville")["abonnes_in"].mean().reset_index()
# Trier (classement)
df_ville = df_ville.sort_values(by="abonnes_in", ascending=False)


print("La Top ville est :", )
print(df_ville)