import manipulate_xml as x
import manipulate_json as j


class Map():

    # mapdic et tiledic sont les json, sauvegardés et ouverts comme indiqué plus bas
    def __init__(self,mapdic,tiledic,imgdir):

        self.mapdic = mapdic
        self.tiledic = tiledic

        self.layerlist = self.mapdic['map']['layer']
        self.tilelist = self.tiledic['tileset']['tile']

        self.map_by_layer = self.load_map()
        self.imgdic = self.load_imgdic(imgdir)

        self.loaded_map = None

        self.x_limit = len(self.map_by_layer[0][0]) -1
        self.y_limit = len(self.map_by_layer[0]) - 1


    # Dans Tiled, la layer la plus en bas est indexé à 0 (background = 0, calque dessus = 1, ...)
    # layer = calque
    def layer(self,number):
        return(self.layerlist[number]['data']['#text'].split('\n'))


    # On s'assurera toujours que nos tiles (dans le fichier .tsx) ont des ID "correctes"
    # Par "correctes" j'entend l'ID i est à la place i [vérifiable dans le .json]
    def get_tile_imgname(self,_id):
        _id = int(_id)

        # L'ID affiché sur la map est "id+1"
        if _id == 0:
            return("empty.gif")
        _id -= 1
        this_tile = self.tilelist[_id]
        this_tile_name = this_tile['@type']
        this_tile_imgname = this_tile['image']['@source'].split('/')[-1]
        return(this_tile_imgname)

    def get_tile_taglist(self,_id):
        _id = int(_id)
        if _id == 0:
            return([''])
        _id -= 1
        this_tile = self.tilelist[_id]

        # Si c'est une liste, il y a plusieurs catégories de tags.
        if type(this_tile['properties']['property']) == type([]):
            for _property in this_tile['properties']['property']:
                if _property['@name'] == "tag":
                    this_tile_taglist = _property['@value'].split(',')

        # Alors c'est un dictionnaire, il y une seule catégorie de tags
        else:
            this_tile_taglist = this_tile['properties']['property']['@value'].split(',')

        return(this_tile_taglist)

    def get_tile_name(self,_id):
        _id = int(_id)

        # L'ID affiché sur la map est "id+1"
        if _id == 0:
            return("empty.gif")
        _id -= 1
        this_tile = self.tilelist[_id]
        this_tile_name = this_tile['@type']
        return(this_tile_name)


    # Renvoie une liste dont le ième élément est la ième layer, et donc la ième layer est une matrice qui correspond aux éléments dans la map
    # Cette fonction ayant une grande complexité, on ne l'appellera que pour passer d'une map à l'autre
    def load_map(self):

        mbl = []

        # Layer par layer
        for i in range(len(self.layerlist)):
            layer = self.layer(i)

            # La matrice qui correspond à toute la map, dont le j-ème élément est la j-ème ligne
            matrix_layer = []
            # Ligne par ligne (de la couche actuelle)
            for j in range(len(layer)):
                # Le dernier élément est vide
                ligne_liste = layer[j].split(',')[:-1]

                matrix_layer.append(ligne_liste)

            mbl.append(matrix_layer)


        self.loaded_map = mbl
        return(mbl)

    def load_imgdic(self,imgdir):
        from tkinter import PhotoImage

        mydic = {}

        mypath = imgdir
        from os import listdir
        from os.path import isfile, join
        # Chaque élément de onlyfiles est un nom en .gif correspondant à une image de bloc
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for filename in onlyfiles:
            mydic[filename] = PhotoImage(file=f"{mypath}/{filename}")
        return(mydic)




    # On ne load pas à nouveau la map !
    # (x,y) fournie sont les coordonnées (ligne,colonne) du bloc en haut à gauche
    # Donc 1,1 correspond au bloc ligne 1, colonne 1
    # Cela marche aussi avec des flottants : 0.5 , 0 correspond à la moitié (en x) du bloc en haut à gauche
    def draw_map(self,canvas,x_debut=0,y_debut=0):
        canvas.delete('all')



        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # NOTE : il faudrait peut-être rajouter 1. On testera
        nbr_colonnes = width // 70  + 1
        nbr_lignes = height // 70  + 1

        self.x_limit = len(self.map_by_layer[0][0]) -1
        self.y_limit = len(self.map_by_layer[0]) - 1


        x_int = int(x_debut)
        y_int = int(y_debut)

        x_frac = x_debut - x_int
        y_frac = y_debut - y_int

        if x_frac > 0:
            nbr_lignes += 1
        if y_frac > 0:
            nbr_colonnes += 1



        a = False
        b = False


        # Ces deux conditions sont faites pour décaler l'écran hors-map
        if x_int < 0:
            nbr_colonnes = nbr_colonnes + x_int
            old_x=x_int
            x_int = 0
            a=True
        if y_int < 0:
            nbr_lignes = nbr_lignes + y_int
            old_y=y_int
            y_int=0
            b=True

        # Chaque élément est une matrice de map, la première est la layer 0
        # On dessinera dans l'ordre croissant des layer, comme ça le background est bien dessinné en premier
        for layer in self.map_by_layer:

            # layer est une liste de "lignes" ; on ne prend que celles visibles à l'écran

            this_layer = layer[y_int:y_int+nbr_lignes+1]

            # On parcourt chaque ligne, on a donc le numéro de la ligne = y
            for y in range(len(this_layer)):
                # this_layer[y] est une ligne de blocs ; on ne prend que ceux visibles à l'écran


                this_ligne = this_layer[y][x_int:x_int+nbr_colonnes]

                if b:
                    y += abs(old_y)

                # On parcourt chaque élément de la ligne, on a donc le numéro de la colonne = x
                for x in range(len(this_ligne)):
                    bloc_id = this_ligne[x]

                    if a:
                        x += abs(old_x)

                    tag_tuple = tuple(self.get_tile_taglist(bloc_id))
                    imgname = self.get_tile_imgname(bloc_id)
                    if imgname != "empty.gif":
                        canvas.create_image(x_frac*(-70)+x*70,
                                            y_frac*(-70)+70+y*70,
                                            image=self.imgdic[imgname],
                                            anchor='sw',
                                            tags=tag_tuple)
        return


def test():

    _map_ = "img/stock/_tiles/Tiled software/my_first_map.tmx"
    _tileset_ = "img/stock/_tiles/Tiled software/bloks.tsx"

    _jsonmap_ = "img/stock/_tiles/Tiled software/map.json"
    _jsontileset_ = "img/stock/_tiles/Tiled software/bloks.json"

    x.xml_to_json(opendir=_map_,savedir=_jsonmap_)
    x.xml_to_json(opendir=_tileset_,savedir=_jsontileset_)

    _mapdic_ = j.load_file(fulldir=_jsonmap_)
    _tilesetdic_ =j.load_file(fulldir=_jsontileset_)


    return(_mapdic_,_tilesetdic_)

# On charge les données d'une map : la map et son tileset
# On rend l'objet 'myMap' de classe 'Map' pour load complètement la map et accéder aux fonctions utiles
def load_map(mapdir,mapname,tilename,imgdir):
    import manipulate_xml as x
    import manipulate_json as j

    o_fullmapdir = f"{mapdir}/{mapname}.tmx"
    o_fulltiledir = f"{mapdir}/{tilename}.tsx"

    s_fullmapdir = f"{mapdir}/{mapname}.json"
    s_fulltiledir = f"{mapdir}/{tilename}.json"
    if s_fullmapdir == s_fulltiledir:
        raise Exception("Impossible de mettre le même nom !")


    x.xml_to_json(opendir=o_fullmapdir,savedir=s_fullmapdir)
    x.xml_to_json(opendir=o_fulltiledir,savedir=s_fulltiledir)

    mapdic = j.load_file(fulldir=s_fullmapdir)
    tiledic = j.load_file(fulldir=s_fulltiledir)

    myMap = Map(mapdic,tiledic,imgdir)

    return(myMap)


if __name__ == '__main__':
    #global myMap

    mapdir = "img/stock/_tiles/Tiled software"
    mapname = "my_first_map"
    tilename = "bloks"
    imgdir = "img/stock/_tiles/resized"

    myMap = load_map(mapdir,mapname,tilename,imgdir)