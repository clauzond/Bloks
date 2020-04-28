import math
from time import time

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

        self.keyhistory = []

        self.speedx = 0
        self.speedy = 0

        # Pour "get_collisions" plus tard
        self.x1 = self.pos_x*70
        self.y1 = 70+self.pos_y*70

        self.x2 = self.x1 + self.player_photoimage.width()
        self.y2 = self.y1 + self.player_photoimage.height()

        self.loop = False


    def draw(self,x_map,y_map):
        self.x_map = x_map
        self.y_map = y_map

        self.game_canvas.create_image(  self.pos_x*70,
                                        70+self.pos_y*70,
                                        image=self.player_photoimage,
                                        anchor="nw",
                                        tags=("player"))


        if not self.loop:
            self.loop = True
            self.jumptime = 0
            self.current_time = time()
            self.go_on_ground(0)
            self.myloop()





    def keydown(self,*args):
        event = args[0]
        if not event.keysym in self.keyhistory and event.keysym in ['Up','Left','Down','Right','space']:
            self.keyhistory.append(event.keysym)

    def keyrelease(self,*args):
        event = args[0]
        if event.keysym in self.keyhistory:
            self.keyhistory.pop(self.keyhistory.index(event.keysym))





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


    def get_collisions(self,*args):
        # Renvoie un tuple contenant les items qui croisent le rectangle
        # (x1,y1) coin supérieur gauche
        # (x2,y2) coin inférieur droit

        if len(args)==0:
            (x1,y1,x2,y2) = (self.x1,self.y1,self.x2,self.y2)
        else:
            (x1,y1,x2,y2) = (args[0],args[1],args[2],args[3])

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

    def is_colliding(self,*args):
        (x1,y1,x2,y2) = (args[0],args[1],args[2],args[3])
        collision_tuple = self.game_canvas.find_overlapping(x1,y1,x2,y2)
        for item in collision_tuple:
            tag_tuple = self.game_canvas.gettags(item)
            if "collision" in tag_tuple:
                return(True)
        return(False)

    def distance_colliding(self,*args):
        (x1,y1,x2,y2) = (args[0],args[1],args[2],args[3])
        collision_tuple = self.game_canvas.find_overlapping(x1,y1,x2,y2)
        player = self.game_canvas.find_withtag("player")[0]
        x,y = self.game_canvas.coords(player)


        for item in collision_tuple:
            tag_tuple = self.game_canvas.gettags(item)
            if "collision" in tag_tuple:
                m,n = self.game_canvas.coords(item)


                distance = n-y - self.player_photoimage.height() - 70# le bloc est défini en sw, le joueur en nw
                return(distance)
        return(None)

    def canjump(self):
        self.can_jump = True

    def go_on_ground(self,dy):
        distance = self.distance_colliding(self.x1,self.y1+dy*70,self.x2,self.y2+dy*70)/70

        if type(distance) is float:
            self.y_map += distance
            self.draw_map(self.x_map,self.y_map)
            self.draw(self.x_map,self.y_map)
            self.on_ground = True
            self.can_jump = True
            self.jump_nbr = 0

    def myloop(self):
        # nb : on code en "bloc par seconde" pour la vitesse
        dt = time() - self.current_time # pas de temps en s
        self.current_time = time()
        if dt>0.1:
            dt=0.1



        dx = 0


        for keysym in self.keyhistory:

            if keysym == "Left":
                dx = -0.4
            if keysym == "Right":
                dx = 0.4
            if keysym == "space":
                if (self.on_ground or self.jump_nbr < 2) and self.can_jump:
                    self.speedy = -10
                    self.on_ground = False
                    self.can_jump = False
                    self.window.after(500,self.canjump)
                    self.jump_nbr += 1


        self.speedy += 1
        if self.speedy > 10:
            self.speedy = 10

        dy = self.speedy*dt




        x1, y1, x2, y2 = self.x1, self.y1 + dy*70, self.x2, self.y2 + dy*70
        if abs(dy)>0:
            if self.distance_colliding(x1,y1,x2,y2) is None:
                if -self.pos_y-2 <= self.y_map + dy <= self.y_limit:
                    self.y_map += dy
            # C'est une chute et il y a collision -> sol
            elif dy>0:
                self.go_on_ground(dy)
                self.speedy = 0
                self.on_ground = True
                self.jump_nbr = 0
                self.can_jump = True

        if abs(dx)>0:
            if self.distance_colliding(self.x1+dx*70,self.y1,self.x2+dx*70,self.y2) is None:
                if -self.pos_x <= self.x_map + dx <= self.x_limit:
                    self.x_map += dx
        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)

        #self.game_canvas.create_rectangle(self.x1+dx*70,self.y1 + dy*70,self.x2+dx*70,self.y2+dy*70)


        self.window.after(1,self.myloop)