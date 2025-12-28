import os
import re

path = "./srv/downloads"

movies = []
series = []
move = "mv"
remove = "rm -rf"
remove_directories = "rmdir"

scan = os.scandir(path)
m = []

for entry in scan:
        z = entry.name.lower().endswith(('.mp4', '.avi', '.mkv'))
        zx = entry.name.lower().startswith(".")
#       z = re.search("mkv", entry.name)      
        if not entry.name.startswith(".") and z:
                x = re.search("[0-9]x[0-9][0-9]", entry.name)
                if x:
                        print( entry.name , "es una serie")
                        os.system(move + f" ./srv/downloads/{entry.name}" + " ./srv/media/series")
                else:
                        print( entry.name , "es una pelicula")
                        os.system(move + f" ./srv/downloads/{entry.name}" + " ./srv/media/movies")
        else:
            print( entry.name , "no es un archivo multimedia")
            if not entry.name.startswith("."):
                path = f"./srv/downloads/{entry.name}" + "/"
                scan = os.scandir(path)
                for entry in scan:
                    z = re.search("mkv", entry.name)
                    if z:
                        x = re.search("[0-9]x[0-9][0-9]", entry.name)
                        if x:
                            print( entry.name , "es una serie")
                            os.system(move + f" '{path}''{entry.name}'" + " ./srv/media/series")
                        else:
                            print( entry.name , "es una pelicula")
                            os.system(move + f" '{path}''{entry.name}'" + " ./srv/media/movies")
                    else:
                        print( entry.name , "no es un archivo multimedia")
                        os.system(remove + f" '{path}''{entry.name}'")
        # vale es aqui
        if not path.endswith("downloads"):
            os.system(f"{remove_directories} '{path}'") 
        else:
             print("Archivos borrados")
        
scan.close()
