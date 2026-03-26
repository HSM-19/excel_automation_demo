###1. charger CSV
import pandas as pd

df = pd.read_csv("input.csv", sep=";", encoding="latin1")
print("Nombre de lignes AVANT nettoyage  :", len(df))


###2. supprimer les doublons
#df.drop_duplicates(keep = 'first', inplace=True)
#df.drop_duplicates(subset ="nom", keep = 'first', inplace=True) --> selon une colonne
df = df.drop_duplicates()
#print ("2. Nombre de lignes :", len(df))


###3. supprimer lignes sans abonnes_in
df = df.dropna(subset=["abonnes_in"]) #print(df_subset)
#print ("3. Nombre de lignes :", len(df))
print("Nombre de lignes APRÈS nettoyage :", len(df))


###4. calculer moyenne
df["abonnes_in"] = pd.to_numeric(df["abonnes_in"], errors="coerce")
moy = df['abonnes_in'].mean()
print("Le nombre moyen d'abonnés est :",moy)


###5. sauvegarde
df.to_csv("output.csv", sep=";", index=False, encoding="utf-8-sig")
print("\nFichier nettoyé sauvegardé : output_clean.csv")


###6. Calculs simples
# # Moyenne par ville
# df_ville = df.groupby("ville")["abonnes_in"].mean().reset_index()
# # Trier (classement)
# df_ville = df_ville.sort_values(by="abonnes_in", ascending=False)

moyenne = df["abonnes_in"].mean()
top_villes = df["ville"].value_counts().head(3)

print("\nMoyenne abonnes_in :", moyenne)
print("\nTop villes :")
print(top_villes)


