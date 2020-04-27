class ShowPlayer():


    def __init__(self,window,draw_map_function,game_canvas,player_photoimage,outputbox,x_limit,y_limit):

        self.game_canvas = game_canvas

        self.draw_map = draw_map_function

        self.player_photoimage = player_photoimage

        self.outputbox = outputbox

        self.window = window

        height = self.game_canvas.winfo_height()
        width = self.game_canvas.winfo_width()

        nbr_colonnes = width // 70
        nbr_lignes = height // 70

        self.pos_x = nbr_colonnes / 2 - 1.3
        self.pos_y = nbr_lignes / 2 - 1.3

        self.x_limit = x_limit - self.pos_x
        self.y_limit = y_limit - self.pos_y - 1



    def draw(self,x_map,y_map):
        self.x_map = x_map
        self.y_map = y_map
        self.game_canvas.delete("player")
        height = self.game_canvas.winfo_height()
        width = self.game_canvas.winfo_width()

        self.game_canvas.create_image(  self.pos_x*70,
                                        70+self.pos_y*70,
                                        image=self.player_photoimage,
                                        anchor="nw",
                                        tags=("player"))


        # Pour "get_collisions" plus tard
        self.x1 = self.pos_x*70
        self.y1 = 70+self.pos_y*70

        self.x2 = self.x1 + self.player_photoimage.width()
        self.y2 = self.y1 + self.player_photoimage.height()




    def move_left(self,*args):
        if self.x_map - 1 >= (-self.pos_x):
            self.x_map -= 1

        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)



    def move_right(self,*args):
        if self.x_map + 1 <= self.x_limit:
            self.x_map += 1

        #self.game_canvas.delete("all")
        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)


    def jump(self,*args):
        if self.y_map - 1 >= (-self.pos_y-2):
            self.y_map -= 1

        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)

    def go_down(self,*args):
        if self.y_map + 1 <= self.y_limit:
            self.y_map += 1

        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)


    def check_usable(self,*args):
        self.outputbox.add_text(text=f"{self.get_collisions()}")


    def get_collisions(self):
        # Renvoie un tuple contenant les items qui croisent le rectangle
        # (x1,y1) coin supérieur gauche
        # (x2,y2) coin inférieur droit

        (x1,y1,x2,y2) = (self.x1,self.y1,self.x2,self.y2)

        collision_tuple = self.game_canvas.find_overlapping(x1,y1,x2,y2)

        collision_dic = {'collision':False,'usable':False,'itemlist':[],'taglist':[]}

        for item in collision_tuple:
            tag_tuple = self.game_canvas.gettags(item)
            if "collision" in tag_tuple:
                collision_dic['collision'] = True
            if "usable" in tag_tuple:
                collision_dic['usable'] = True

            for tag in tag_tuple:
                if tag not in ['collision','usable',"player"] and len(tag)>0 :
                    collision_dic['itemlist'].append(item)
                    collision_dic['taglist'].append(tag)
        return(collision_dic)

    def myloop(self):
        self.move_right()


        self.window.after(1,self.myloop)