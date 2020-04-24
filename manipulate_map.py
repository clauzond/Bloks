import manipulate_xml as x
import manipulate_json as j


class Map():

    # mapdic et tiledic sont les json, sauvegardés et ouverts comme indiqué plus bas
    def __init__(self,mapdic,tiledic):

        self.mapdic = mapdic
        self.tiledic = tiledic

        self.layerlist = self.mapdic['map']['layer']
        self.tilelist = self.tiledic['tileset']['tile']

        self.map_by_layer = self.get_mbl_matrix()

        self.loaded_map = None


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




def collect():

    _map_ = "img/stock/_tiles/Tiled software/my_first_map.tmx"
    _tileset_ = "img/stock/_tiles/Tiled software/bloks.tsx"

    _jsonmap_ = "img/stock/_tiles/Tiled software/map.json"
    _jsontileset_ = "img/stock/_tiles/Tiled software/bloks.json"

    x.xml_to_json(opendir=_map_,savedir=_jsonmap_)
    x.xml_to_json(opendir=_tileset_,savedir=_jsontileset_)

    _mapdic_ = j.load_file(fulldir=_jsonmap_)
    _tilesetdic_ =j.load_file(fulldir=_jsontileset_)


    return(_mapdic_,_tilesetdic_)


if __name__ == '__main__':
    global mymap
    a,b = collect()

    mymap = Map(a,b)