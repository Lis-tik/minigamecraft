
import pygame
import random 
from time import sleep
import threading
import data_base_control as db
import Person_Control as pc




width_map = db.start_world(True)
long_map = db.start_world(True)

exception_coordinates = []


def ex_pleers(pleers):
    global pleer
    pleer = pleers

def ex_cord(coord):
    global exception_coordinates
    exception_coordinates = coord




class Essences():
    def __init__(self, x, y, name, str_name, hp, damage, speed, active_move, img, animlist, thread, state):
        self.x = x
        self.y = y

        self.name = name
        self.str_name = str_name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.direction = {'right': True, 'left': True, 'up': True, 'down': True}
        self.active_move = active_move
        self.img = img
        self.animlist = animlist
        self.animcount = 0
        self.thread = thread
        self.state = state
    



class Zombie(Essences):
    def __init__(self, x, y):
        animlist = {'right': [], 'left': [], 'up': [], 'down': []}

        for dir in ['right', 'left', 'up', 'down']:
            for num in range(4):
                img_cbl = pygame.image.load(f'./Spritse/Essences/Enemy/{dir}/Enemy_{num}.png')
                animlist[dir].append(img_cbl)

        img_non = (f'./Spritse/Essences/Enemy/Enemy_.png')
        img = pygame.image.load(img_non)
        
        thread = threading.Thread(target=self.goin, name="Zombie")
        super().__init__(x, y, Zombie, "Zombie", 100, 10, 1, ['stay'], img, animlist, thread, 'pursuit')


                      
                

    def colize(self):
        # Не знаю почему это так работает, но координаты моба начинается с левого нижнего угла

        for key, move in self.direction.items():

            if key == 'right':
                x_mob = ((self.x + 32 + self.speed) // 64)
                y_mob = (self.y) // 64

            elif key == 'up':
                x_mob = (self.x + 32) // 64
                y_mob = ((self.y - self.speed) // 64)

            elif key == 'left':
                x_mob = ((self.x + 32 - self.speed) // 64)
                y_mob = (self.y) // 64

            elif key == 'down':
                x_mob = (self.x + 32) // 64
                y_mob = ((self.y + self.speed) // 64)


            block = exception_coordinates[y_mob][x_mob][-1]
            self.direction[key] = not block.colision

            if block.str_name == 'Door':
                if block.strength <= 0:
                    exception_coordinates[y_mob][x_mob].pop()

                self.breaking(block)



        #     print(key, self.direction[key], block.str_name)
        # print('----------------------------------')

    def breaking(self, block):
        while block.strength > 0 and block.colision:
            block.strength -= self.damage
            sleep(3)
            print('Удар по двери, прочность: ', block.strength)


    def damage_dist(self, person):
        while abs(pleer.y_map - self.y) < 30 and abs(pleer.x_map - self.x) < 30:  
            print("KICK------------")
            self.active_move.append('attack')
            pleer.hp -= self.damage
            sleep(4)
            self.active_move.clear()
            





    def stuck(self, prior):
        if not self.direction['right']:
            while not self.direction['right']:
                if ('up' in prior) and self.direction['up']:
                    self.y -= self.speed
                    self.active_move.append('up')
                    sleep(0.01)

                elif ('down' in prior) and self.direction['down']:
                    self.y += self.speed
                    self.active_move.append('down')
                    sleep(0.01)
                else:
                    break
                self.colize()



        if not self.direction['left']:
            while not self.direction['left']:
                if ('up' in prior) and self.direction['up']:
                    self.y -= self.speed
                    self.active_move.append('up')
                    sleep(0.01)

                elif ('down' in prior) and self.direction['down']:
                    self.y += self.speed
                    self.active_move.append('down')
                    sleep(0.01)

                else:
                    break
                self.colize()
                

        if not self.direction['up']:
            while not self.direction['up']:
                if ('left' in prior) and self.direction['left']:
                    self.x -= self.speed
                    self.active_move.append('left')
                    sleep(0.01)

                elif ('right' in prior) and self.direction['right']:
                    self.x += self.speed
                    self.active_move.append('right')
                    sleep(0.01)
                else:
                    break
                self.colize()


        if not self.direction['down']:
            while not self.direction['down']:
                if ('left' in prior) and self.direction['left']:
                    self.x -= self.speed
                    self.active_move.append('left')
                    sleep(0.01)

                elif ('right' in prior) and self.direction['right']:
                    self.x += self.speed
                    self.active_move.append('right')
                    sleep(0.01)
                else:
                    break
                self.colize()

        self.active_move.clear()
        self.damage_dist()



    def goin(self):
        while True:
            if self.state == 'pursuit':

                prior = []

                if self.y > pleer.y_map:
                    prior.append('up')
                        
                if self.x < pleer.x_map:
                    prior.append('right')

                if self.y < pleer.y_map:
                    prior.append('down')

                if self.x > pleer.x_map:
                    prior.append('left')


                if self.direction['up'] and ('up' in prior):
                    self.y -= self.speed
                    self.active_move.append('up')
                    sleep(0.01)
                else:
                    self.stuck(prior)
                
                if self.direction['right'] and ('right' in prior):
                    self.x += self.speed
                    self.active_move.append('right')
                    sleep(0.01)
                else:
                    self.stuck(prior)

                if self.direction['down'] and ('down' in prior):
                    self.y += self.speed
                    self.active_move.append('down')
                    sleep(0.01)
                else:
                    self.stuck(prior)

                if self.direction['left'] and ('left' in prior):
                    self.x -= self.speed
                    self.active_move.append('left')
                    sleep(0.01)

                else:
                    self.stuck(prior)

                self.active_move.clear()
                self.colize()
                self.damage_dist()



                
                
                



                
            
