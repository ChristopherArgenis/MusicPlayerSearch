import pywhatkit as pwt

class Consulta:
    def __init__(self, df):
        self.df = df

    def ft_year(self, select=None, year1=None, year2=None):
        self.year1 = year1
        self.year2 = year2
        self.select = select
        match self.select:
            case "Igual":
                self.df = self.df[self.df["Year"] == year1]
            case "Intervalo":
                self.df = self.df[(self.df["Year"] > year1) & (self.df["Year"] < year2)]
            case "Apartir":
                self.df = self.df[self.df["Year"] > year1]

    def ft_artist(self, artist):
        self.artist = artist
        self.df = self.df[self.df["Artist"] == self.artist]

    def ft_genre(self, genre):
        self.genre = genre
        self.df = self.df[self.df["Genre"] == self.genre]

class proba:
    def __init__(self, df_Mod):
        self.dfM = df_Mod

    def proba_total(self, df):
        self.df = df
        self.proba = 0
        if len(self.dfM) < 125:
            self.proba = ((len(self.dfM)/len(self.df))*100)
            print(f"{self.proba:.2f}% de Probabilidad")
        else:
            self.proba = int((len(self.dfM)/len(self.df))*100)
            print(f"{self.proba}% de Probabilidad")

class link_yt:
    def __init__(self, name:str):
        self.name = name

    def url_yt(self):
        pwt.playonyt(self.name)