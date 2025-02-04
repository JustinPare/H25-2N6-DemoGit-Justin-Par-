# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os
os.chdir("C:\\Users\\2477415\\OneDrive - Cégep Édouard-Montpetit\\Prog 2\\R03 Exercices Depart\\Ex3 Videos")
for dossier in os.listdir() :
    extention = os.path.splitext(dossier)[1]
    filename = os.path.splitext(dossier)[0]
    titre = filename.split("_")[0]
    cours = filename.split("_")[1]
    numCours = filename.split("_")[2]
    titre2 = titre.strip(" ")
    numCours2 = numCours.strip(" ")
    numCours3 = numCours2[1:]
    numCours4 = numCours3.zfill(2)


