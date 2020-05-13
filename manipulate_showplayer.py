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

        self.bind_active = False

        self.x_map = None
        self.y_map = None


    def draw(self,x_map,y_map):
        self.x_map = x_map
        self.y_map = y_map

        self.bind_active = True

        self.game_canvas.create_image(  self.pos_x*70,
                                        70+self.pos_y*70,
                                        image=self.player_photoimage,
                                        anchor="nw",
                                        tags=("player"))
        self.game_canvas.update()



    def coords(self):
        return(self.x_map,self.y_map)


    def keydown(self,*args):
        if not self.bind_active:
            return

        event = args[0]
        if not event.keysym in self.keyhistory and event.keysym in ['Up','Left','Down','Right','space']:
            self.keyhistory.append(event.keysym)

    def keyrelease(self,*args):
        if not self.bind_active:
            return

        event = args[0]
        if event.keysym in self.keyhistory:
            self.keyhistory.pop(self.keyhistory.index(event.keysym))


    def turn_bind_off(self):
        self.bind_active = False

    def turn_bind_on(self):
        self.bind_active = True



    def move_left(self,*args):
        if not self.bind_active:
            return


        if not self.is_colliding(self.x1+(-0.5)*70,self.y1,self.x2+(-0.5)*70,self.y2):
            if self.x_map - 0.5 >= (-self.pos_x):
                self.x_map -= 0.5
                self.draw_map(self.x_map,self.y_map)
                self.draw(self.x_map,self.y_map)





    def move_right(self,*args):
        if not self.bind_active:
            return
        if not self.is_colliding(self.x1+(0.5)*70,self.y1,self.x2+(0.5)*70,self.y2):
            if self.x_map + 0.5 <= self.x_limit:
                self.x_map += 0.5
                self.draw_map(self.x_map,self.y_map)
                self.draw(self.x_map,self.y_map)


    def move_up(self,*args):
        if not self.bind_active:
            return
        if not self.is_colliding(self.x1,self.y1+(-0.5)*70,self.x2,self.y2+(-0.5)*70):
            if self.y_map - 0.5 >= (-self.pos_y-1):
                self.y_map -= 0.5
                self.draw_map(self.x_map,self.y_map)
                self.draw(self.x_map,self.y_map)

    def move_down(self,*args):
        if not self.bind_active:
            return
        if not self.is_colliding(self.x1,self.y1+(0.5)*70,self.x2,self.y2+(0.5)*70):
            if self.y_map + 0.5 <= self.y_limit:
                self.y_map += 0.5
                self.draw_map(self.x_map,self.y_map)
                self.draw(self.x_map,self.y_map)


    def check_usable(self,*args):
        if not self.bind_active:
            return
        # coordonnées sur le canvas du rectangle du joueur
        # Rappel : un bloc fait 70*70 pixels
        x1,y1,x2,y2 = self.x1,self.y1,self.x2,self.y2

        distance_check = 20
        x1 -= distance_check
        y1 -= distance_check
        x2 += distance_check
        y2 += distance_check

        self.outputbox.add_text(text=f"{self.get_collisions(x1,y1,x2,y2)}")
        self.game_canvas.create_rectangle(x1,y1,x2,y2)




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
            if "collision" in tag_tuple or "enemy" in tag_tuple:
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


    def myloop(self):
        if not self.loop:
            return


        # nb : on code en "bloc par seconde" pour la vitesse
        dt = time() - self.current_time # pas de temps en s
        self.current_time = time()
        if dt>0.1:
            dt=0.1

        for keysym in self.keyhistory:

            if keysym == "Left":
                if self.speedx > -5:
                    self.speedx -= 1
            if keysym == "Right":
                if self.speedx < 5:
                    self.speedx += 1
            if keysym == "Up":
                if self.speedy > -5:
                    self.speedy -=1
            if keysym == "Down":
                if self.speedy < 5:
                    self.speedy +=1
            if keysym == "space":
                self.check_usable()




        if "Left" not in self.keyhistory and "Right" not in self.keyhistory:
            if self.speedx < 0:
                self.speedx += 1
            elif self.speedx >0:
                self.speedx -= 1
        if "Up" not in self.keyhistory and "Down" not in self.keyhistory:
            if self.speedy < 0:
                self.speedy += 1
            elif self.speedy > 0:
                self.speedy -=1

        dx = self.speedx*dt
        dy = self.speedy*dt


        if abs(dx)>0:
            if self.is_colliding(self.x1+dx*70,self.y1,self.x2+dx*70,self.y2) is False:
                if -self.pos_x <= self.x_map + dx <= self.x_limit:
                    self.x_map += dx
        x1, y1, x2, y2 = self.x1, self.y1 + dy*70, self.x2, self.y2 + dy*70
        if abs(dy)>0:
            if self.is_colliding(x1,y1,x2,y2) is False:
                if -self.pos_y-2 <= self.y_map + dy <= self.y_limit:
                    self.y_map += dy
        self.draw_map(self.x_map,self.y_map)
        self.draw(self.x_map,self.y_map)

        #self.game_canvas.create_rectangle(self.x1+dx*70,self.y1 + dy*70,self.x2+dx*70,self.y2+dy*70)
        self.window.after(1,self.myloop)