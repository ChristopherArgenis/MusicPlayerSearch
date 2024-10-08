import csv
import random


#Funcion de busqueda de canciones
def search_keywords_in_csv(csv_file, searchLength, searchYear, searchArtist, searchGenre):
    global matchSongs
    matchSongs=[]

    with open(csv_file, 'r', newline='', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  

        for row in reader:
            musArtist=row[1].lower()
            musYear=int(row[2])
            musLength=int(row[3])
            musGenre=row[17].lower()
            musName=row[0]

            if (searchLength[0]<=musLength<=searchLength[1]) and (searchArtist=="" or musArtist==searchArtist.lower()) and (searchYear[0]<=musYear<=searchYear[1]) and (searchGenre=="" or musGenre==searchGenre.lower()):
                matchSongs.append(musName)

    return matchSongs

#Localizacion del archivo CSV
csv_file = "ClassicHit.csv"

#Declaracion de variables de busqueda
searchArtist=""
searchLength=(0,999999999)
searchYear=(0,999999999)
searchGenre=""
validGenres=["alt. rock","pop","metal","r&b","country","rock","blues","disco","edm","folk","funk","gospel","jazz","punk","rap","reggae","ska","today","world"]

#Ciclo para la busqueda de la cancion
found=False

#Variables para imprimir las palabras de busqueda que quiere usar el usuario
artistQuery="Vacio"
yearQuery="Vacio"
lengthQuery="Vacio"
genreQuery="Vacio"



#Mecanismo de búsqueda
print("Bienvenido al buscador de canciones")

while found==False:
    order=False
    genreNotValid=True

    #Aqui se imprimen las palabras que esta buscando el usuario
    print(f"Artista: {artistQuery}\nRango de años: {yearQuery}\nLongitud de canción: {lengthQuery}\nGenero: {genreQuery}")

    #Menu
    ans=int(input("\nQue accion desea hacer ahora:\n1) Recibir una cancion\n2) Insertar palabra para busqueda?\n3) Reinicar palabras de busqueda? \n4) Salir \nRespuesta: "))
    match ans:

        #Se busca y se elige la cancion a partir de las palabras del usuario
        case 1:
            matchedSongs = search_keywords_in_csv(csv_file, searchLength, searchYear, searchArtist, searchGenre)
            if matchedSongs:
                print(f"Dado a los resultados de su busqueda, una de sus canciones ideales es: {random.choice(matchSongs)}")
                print("Muchas gracias por usar el programa")
                found=True
            else:
                print("Desafortunadamente no hemos encontrado una cancion que cumpla con las características que busca")

        #Aqui el usuario va a insertar las palabras que va a quere usar para la busqueda de su cancion
        case 2:
            ans=int(input("\nEn que tipo de categoria desearia buscar:\n1) Artista o banda\n2) Año de publicacion\n3) Longitud de cancion \n4) Genero \nRespuesta: "))
            match ans:
                case 1:
                    searchArtist=input("Escriba el nombre del artista o banda que quisiera buscar: ")
                    artistQuery=searchArtist
                case 2:
                    while order==False:
                        yearMin=int(input("A partir de que año quiere agregar en su busqueda: "))
                        yearMax=int(input("Hasta que año quiere agregar en su busqueda: "))
                        searchYear=(yearMin,yearMax)
                        if yearMin<yearMax:
                            order=True
                            yearQuery=("De "+str(yearMin)+" a "+str(yearMax))
                        elif yearMin==yearMax:
                            order=True
                            yearQuery=yearMax
                        else:
                            print("Sus años no estan correctamente ordenados o no estan bien redactados... intente de nuevo")
                case 3:
                    while order==False:
                        lengthMin=int(input("Cual es la longitud minima en minutos de la cacnion que busca:"))
                        lengthMax=int(input("Cual es la longitud maxima en minutos"))
                        searchLength=(lengthMin*60000,lengthMax*60000)
                        if lengthMin<lengthMax:
                            order=True
                            lengthQuery=("De "+str(lengthMin)+" minutos a "+str(lengthMax)+" minutos")
                        elif lengthMin==lengthMax:
                            order=True
                            lengthQuery=(str(lengthMax)+" minutos")
                        else:
                            print("Su rango de tiempo no esta correctamente ordenado o no esta bien redactado... intente de nuevo")
                case 4:
                    while genreNotValid==True:
                        searchGenre=input("Escriba el genero de musica que quisiera buscar\nopciones: alt. rock, pop, metal, r&b, country, rock, blues, disco, edm, folk, funk, gospel, jazz, punk, rap, reggae, ska, today, world\nRespuesta: ")
                        if searchGenre.lower() in validGenres:
                            genreNotValid=False
                            genreQuery=searchGenre
                        else:
                            print("Por favor elija un genero valido")
                case _:
                    print("Por favor elija una respuesta valida")
        
        #Aqui se reinician las variables de busqueda si el usuario no se encuentra satisfecho con las palabras que eligió
        case 3:
            searchArtist=""
            searchLength=(0,999999999)
            searchYear=(0,999999999)
            searchGenre=""
            artistQuery="Vacio"
            yearQuery="Vacio"
            lengthQuery="Vacio"
            genreQuery="Vacio"
        
        #Mensaje de salida por si el usuario quiere salir y no encontro su cancion
        case 4:
            print("Muchas gracias por usar el programa")
            found=True
        
        case _:
            print("Por favor escriba una opcion valida")# Code ->
