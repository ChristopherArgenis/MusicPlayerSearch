import pandas as pd

df = pd.read_csv("ClassicHit.csv")

# Dataframe a partir de las columnas del csv
Music_db = df[["Track", "Artist", "Year", "Duration", "Popularity", "Genre", "Energy", "Danceability"]]

def uniques(db):
  for i in db.columns:
    temp = db[i].unique()
    print(f"Columna: {i}, valores unicos: {len(temp)}")

# Approved
def year_filter(df, select=None, year1=None, year2=None):
    match select:
        case "Igual":
            return df[df["Year"] == year1]
        case "Intervalo":
            return df[(df["Year"] > year1) & (df["Year"] < year2)]
        case "Apartir":
            return df[df["Year"] > year1]

# Approved
def proba_year(yf_df):
    if len(yf_df) < 125:
        proba = ((len(yf_df)/len(Music_db))*100)
        print(f"{proba:.2f}% de Probabilidad")
    else:
        proba = int((len(yf_df)/len(Music_db))*100)
        print(f"{proba}% de Probabilidad")

# yf_df = year_filter(Music_db, "Igual", 2021)
# proba_year(yf_df)
# uniques(Music_db)
# - - - - - - - - - - - - - - - - - - - - - - - - - -

def option(df, column):
    df = df[column].unique()
    return df

list_opcion = option(Music_db, "Year")
list_opcion.sort()
# print(list_opcion)

def artist_filter(df, name):
    df = df[df["Artist"] == name]
    return df

def genre(df, genre):
    df = df[df["Genre"] == genre]
    return df

# print(option(Music_db, "Genre"))
genre_df = genre(Music_db, "Pop")
print(genre_df)
# art_df = artist_filter(Music_db, '3 Doors Down')
print(len(Music_db))