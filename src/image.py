from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'une image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W),dtype=np.uint8))
        
        for i in range (self.H):
            for j in range (self.W):
                if self.pixels[i][j] >= S :
                    im_bin.pixels[i][j] = 255
                else :
                    im_bin.pixels[i][j] = 0
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        c_min = 100000 
        c_max = 0
        l_min = 0
        l_max = 100000
        im_bin=Image()
        im_bin.set_pixels(self.pixels)
        
        for i in range (self.H):
           for j in range (self.W):
               if self.pixels[i][j] == 0 and j < c_min:
                   c_min = j
                  
        for i in range (self.H-1,0,-1):
            for j in range (self.W-1,0,-1):
                if self.pixels[i][j] == 0 and j > c_max:
                   c_max = j
                   
        for j in range (self.W-1,0,-1):
           for i in range (self.H-1,0,-1):
               if self.pixels[i][j] == 0 and i > l_min:
                   l_min = i
                   
        for j in range (self.W):
           for i in range (self.H):
               if self.pixels[i][j] == 0 and i < l_max:
                   l_max = i 
        print(c_max,c_min,l_max,l_min)
        
        im_bin.pixels=im_bin.pixels[l_max:l_min,c_min:c_max]
        return im_bin
               

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self,new_H,new_W):
        im_res=Image()
        im_res.pixels=resize(self.pixels,(new_H,new_W),0)
        im_res.pixels=np.uint8(im_res.pixels*255)
        im_res.H = new_H
        im_res.W = new_W
        return im_res
 

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self,image):
        pixel_id=0
        im_sim=Image()
        im_sim.pixels=resize(image.pixels,(self.H,self.W),0)
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j]==im_sim.pixels[i][j]:
                    pixel_id+=1       
        return (pixel_id/(self.H*self.W))
