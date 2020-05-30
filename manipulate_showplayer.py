import manipulate_tiles


class ShowPlayer():
    def __init__(self, window, myMap, game_canvas, player_name, player_photoimage, outputbox, x_limit, y_limit):

        self.game_canvas = game_canvas

        self.myMap = myMap

        self.player_name = player_name
        self.player_photoimage = player_photoimage

        self.outputbox = outputbox

        self.window = window

        height = self.game_canvas.winfo_height()
        width = self.game_canvas.winfo_width()

        nbr_colonnes = width // 70
        nbr_lignes = height // 70

        self.pos_x = nbr_colonnes // 2 - self.player_photoimage.width() / 70
        self.pos_y = nbr_lignes // 2 - self.player_photoimage.height() / 70

        self.x_limit = x_limit - self.pos_x
        self.y_limit = y_limit - self.pos_y - 1

        # Pour "get_collisions" plus loin
        self.x1 = self.pos_x * 70
        self.y1 = 70 + self.pos_y * 70

        self.x2 = self.x1 + self.player_photoimage.width()
        self.y2 = self.y1 + self.player_photoimage.height()

        self.bind_active = False

        self.x_map = None
        self.y_map = None

    def draw(self, x_map, y_map):
        self.x_map = x_map
        self.y_map = y_map

        self.bind_active = True

        self.game_canvas.create_image(self.pos_x * 70,
                                      70 + self.pos_y * 70,
                                      image=self.player_photoimage,
                                      anchor="nw",
                                      tags=("player"))
        self.game_canvas.update()

    def coords(self):
        return(self.x_map, self.y_map)

    def coords_to_ligo(self):
        """
        Renvoie les coordonnées en (ligne,colonne) du joueur
        Sachant que (0,0) est le bloc tout en haut à gauche de l'écran
        """
        li = int(self.y_map + self.pos_y + 1)
        go = int(self.x_map + self.pos_x)
        return(li, go)

    def get_block_taglist(self, layer, li, go):
        """
        Récupère la taglist d'un bloc donné
        :layer -> int de la layer
        :li -> int de la ligne
        :go -> int de la colonne
        """
        return(self.myMap.get_tile_taglist(self.myMap.map_by_layer[layer][li][go]))

    def check_blocks_around_player(self, layer):
        """
        Check les blocks dans un rayon de 1 autour du joueur (joueur compris)
        """
        li, go = self.coords_to_ligo()

        liste = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # liste[i][j] indique la position (ligne,colonne) et la taglist
        liste[0][0] = (
            li - 1, go - 1, self.get_block_taglist(layer, li - 1, go - 1))
        liste[0][1] = (li - 1, go, self.get_block_taglist(layer, li - 1, go))
        liste[0][2] = (
            li - 1, go + 1, self.get_block_taglist(layer, li - 1, go + 1))

        liste[1][0] = (li, go - 1, self.get_block_taglist(layer, li, go - 1))
        liste[1][1] = (li, go, self.get_block_taglist(layer, li, go))
        liste[1][2] = (li, go + 1, self.get_block_taglist(layer, li, go + 1))

        liste[2][0] = (
            li + 1, go - 1, self.get_block_taglist(layer, li + 1, go - 1))
        liste[2][1] = (li + 1, go, self.get_block_taglist(layer, li + 1, go))
        liste[2][2] = (
            li + 1, go + 1, self.get_block_taglist(layer, li + 1, go + 1))

        return(liste)

    def check_collision(self, direction):
        """
        Renvoie un booléen correspond à "IL Y A COLLISION"
        direction -> "left","right","up","down"
        """
        li, go = self.coords_to_ligo()
        if direction == "left":
            taglist1 = self.get_block_taglist(layer=1, li=li, go=go - 1)
            taglist2 = self.get_block_taglist(layer=2, li=li, go=go - 1)
            taglist3 = self.get_block_taglist(layer=3, li=li, go=go - 1)
        elif direction == "right":
            taglist1 = self.get_block_taglist(layer=1, li=li, go=go + 1)
            taglist2 = self.get_block_taglist(layer=2, li=li, go=go + 1)
            taglist3 = self.get_block_taglist(layer=3, li=li, go=go + 1)
        elif direction == "up":
            taglist1 = self.get_block_taglist(layer=1, li=li - 1, go=go)
            taglist2 = self.get_block_taglist(layer=2, li=li - 1, go=go)
            taglist3 = self.get_block_taglist(layer=3, li=li - 1, go=go)
        elif direction == "down":
            taglist1 = self.get_block_taglist(layer=1, li=li + 1, go=go)
            taglist2 = self.get_block_taglist(layer=2, li=li + 1, go=go)
            taglist3 = self.get_block_taglist(layer=3, li=li + 1, go=go)

        return("collision" in taglist1 or "collision" in taglist2 or "collision" in taglist3)

    def check_for_everything(self):
        """
        layer 1 = celles où les items "non disappearing" sont
        layer 2 = celles où les items "disappearing" sont
        layer 3 = celles où les monstres sont
        """
        if not self.bind_active:
            return
        self.check_items(layer=1)
        self.check_items(layer=2)
        self.check_items(layer=3)

    def check_items(self, layer):
        myList = self.check_blocks_around_player(layer)

        for i in range(0, 3):
            for j in range(0, 3):
                li, go, taglist = myList[i][j]
                if len(taglist) > 0:
                    if layer == 1:
                        self.use_normal_item(li=li, go=go, taglist=taglist)
                    elif layer == 2:
                        self.use_disappearing_item(
                            li=li, go=go, taglist=taglist)
                    elif layer == 3:
                        self.use_enemy(li=li, go=go, taglist=taglist)
        return

    def use_normal_item(self, li, go, taglist):
        pass

    def use_disappearing_item(self, li, go, taglist):
        manipulate_tiles.use_disappearing_item(
            layer=2, li=li, go=go, taglist=taglist, player_name=self.player_name, myMap=self.myMap)
        self.myMap.draw_map(canvas=self.game_canvas,
                            x_debut=self.x_map, y_debut=self.y_map)
        self.draw(self.x_map, self.y_map)

        pass

    def use_enemy(self, li, go, taglist):
        pass

    def turn_bind_off(self):
        self.bind_active = False

    def turn_bind_on(self):
        self.bind_active = True

    def move_left(self, *args):
        if not self.bind_active:
            return

        if not self.check_collision(direction="left"):
            if self.x_map - 1 >= (-self.pos_x):
                self.x_map -= 1
                self.myMap.draw_map(canvas=self.game_canvas,
                                    x_debut=self.x_map, y_debut=self.y_map)
                self.draw(self.x_map, self.y_map)

    def move_right(self, *args):
        if not self.bind_active:
            return
        if not self.check_collision(direction="right"):
            if self.x_map + 1 <= self.x_limit:
                self.x_map += 1
                self.myMap.draw_map(canvas=self.game_canvas,
                                    x_debut=self.x_map, y_debut=self.y_map)
                self.draw(self.x_map, self.y_map)

    def move_up(self, *args):
        if not self.bind_active:
            return
        if not self.check_collision(direction="up"):
            if self.y_map - 1 >= (-self.pos_y - 1):
                self.y_map -= 1
                self.myMap.draw_map(canvas=self.game_canvas,
                                    x_debut=self.x_map, y_debut=self.y_map)
                self.draw(self.x_map, self.y_map)

    def move_down(self, *args):
        if not self.bind_active:
            return
        if not self.check_collision(direction="down"):
            if self.y_map + 1 <= self.y_limit:
                self.y_map += 1
                self.myMap.draw_map(canvas=self.game_canvas,
                                    x_debut=self.x_map, y_debut=self.y_map)
                self.draw(self.x_map, self.y_map)
