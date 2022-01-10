from image import Image
import numpy as np

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


"""def reconnaissance_chiffre(image, liste_modeles, S):
    image=image.binarisation(S)
    image=image.localisation()
    sim_max=0
    indice=0
    for i in range (liste_modeles):
        image.pixels=image.resize(liste_modeles[i].pixels.shape)
        image.pixels=np.uint8(image.pixels*255)
        image=image.similitude(liste_modeles[i])
        if image>indice :
            indice = i
            sim_max=image.similitude(liste_modeles[i])
    return indice, sim_max"""
    
def reconnaissance_chiffre(image, liste_modeles, S):
    sim_max=0
    indice=0
    image = image.binarisation(S)
    image = image.localisation()
    for img in liste_modeles:
        img = img.binarisation(150)
        img = img.localisation()
        img = img.resize(200,200)
        img.pixels=np.uint8(img.pixels*255)
        image = image.resize(200,200)
        image.pixels=np.uint8(image.pixels*255)
        taux_sim=image.similitude(img)
        if taux_sim > sim_max :
           sim_max = taux_sim
           indice = img
    return indice.pixels, sim_max
