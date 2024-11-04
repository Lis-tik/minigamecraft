import pygame
from time import sleep
import inventory as inv
import data_base_control as db
import block_add as bl
import tools_add as tl
import win_update as win


x_pers = 768
y_pers = 448


exception_coordinates = []

def ex_info_map(coord, long, width):
    global exception_coordinates, long_map, width_map
    exception_coordinates = coord
    long_map = long
    width_map = width
    



class Pleer():
    def __init__(self, name) -> None:
        self.name = name
        self.x_map = 0 #- speed_v2
        self.y_map = 0 #- speed_v2
        self.dist_dam = 3
        self.deltaX = 64
        self.deltaY = 64
        self.hp = 100
        self.animCount = 0
        self.num_conrl = 0
        self.mode_block = 0
        self.damage = 100
        self.inventory = []
        self.move = {'right': False,'left': False,'up': False,'down': False}
        self.inventory_contents = {'Wood': 5000, 'Pebbles': 5000, 'Dirt': 5000, 'Iron': 5000}
        self.hand_slots = [None, None, None, None, None, None]


    def control_inventory(self, resources):
        if resources:
            self.inventory_contents[resources[0]] += resources[1]


    def call_inventory(self, mx=0, my=0):
        self.manual_control(None, inv.inventory_func(self.inventory_contents, self.inventory, mx, my))


    def right(self, speed):
        self.x_map += speed
        self.deltaX -= speed
        if self.x_map // 64 > long_map - 14:
            self.x_map = (x_pers + 64) * -1
            self.deltaX += 64
        elif self.deltaX <= 0:
            self.deltaX += 64
        elif self.funC():
            self.x_map -= speed
            self.deltaX += speed
        self.WinUpdate('right')


    def left(self, speed):
        self.x_map -= speed
        self.deltaX += speed
        if self.x_map // 64 < -13:
            self.x_map = (long_map - 13) * 64 - speed
            self.deltaX = speed
        elif self.deltaX >= 65:
            self.deltaX -= 64
        elif self.funC():
            self.x_map += speed
            self.deltaX -= speed
        self.WinUpdate('left')

    def up(self, speed):
        self.y_map -= speed
        self.deltaY += speed
        if self.y_map // 64 < -8:
            self.y_map = (width_map - 8) * 64 - speed
            self.deltaY = speed
        elif self.deltaY >= 65:
            self.deltaY -= 64
        elif self.funC():
            self.y_map += speed
            self.deltaY -= speed
        self.WinUpdate('up')


    def down(self, speed):
        self.y_map += speed
        self.deltaY -= speed
        if self.y_map // 64 > width_map - 9:
            self.y_map = (y_pers + 64) * -1
            self.deltaY += 64
        elif self.deltaY <= 0:
            self.deltaY += 64
        elif self.funC():
            self.y_map -= speed
            self.deltaY += speed
        self.WinUpdate('down')

    def stay(self):
        self.WinUpdate('stay')




    def funC(self):
        basicX = (self.x_map // 64) - 11
        basicY = (self.y_map // 64) - 7
        for y_res in range((self.y_map // 64) - 1, (self.y_map // 64) + 2):
            for x_res in range((self.x_map // 64) - 1, (self.x_map // 64) + 2):
                block = exception_coordinates[y_res][x_res][-1]
                if block.colision:
                    black_list = pygame.Rect(block.getCoordinate(x_res - basicX, self.deltaX),
                                             block.getCoordinate(y_res - basicY, self.deltaY), 64, 64)
                    if black_list.collidepoint(x_pers + 13, y_pers + 45) or black_list.collidepoint(x_pers + 48,
                                                                                                    y_pers + 45):
                        self.move['up'] = False
                        print('up')
                        return True

                    elif black_list.collidepoint(x_pers + 11, y_pers + 45) or black_list.collidepoint(x_pers + 11,
                                                                                                      y_pers + 61):
                        self.move['left'] = False
                        print('left')
                        return True

                    elif black_list.collidepoint(x_pers + 9, y_pers + 61) or black_list.collidepoint(x_pers + 48,
                                                                                                     y_pers + 61):
                        self.move['down'] = False
                        print('down')
                        return True

                    elif black_list.collidepoint(x_pers + 48, y_pers + 45) or black_list.collidepoint(x_pers + 48,
                                                                                                      y_pers + 61):
                        self.move['right'] = False
                        print('right')
                        return True

                    else:
                        self.move['right'] = False
                        self.move['left'] = False
                        self.move['up'] = False
                        self.move['down'] = False

                # return False                 


    


    def stuck_block(self, mx, my, x, y):
        if self.hand_slots[self.num_conrl] != None:

            active_block = self.hand_slots[self.num_conrl][1].name(x, y)
            type_bl = str(active_block.__class__.__base__.__name__)

            if type_bl == 'BaseBlock':
            
                basicX = (self.x_map // 64) - 11
                basicY = (self.y_map // 64) - 7
                for y_res in range((self.y_map // 64) - self.dist_dam, (self.y_map // 64) + self.dist_dam):
                    for x_res in range((self.x_map // 64) - self.dist_dam, (self.x_map // 64) + self.dist_dam):
                        block = exception_coordinates[y_res][x_res][-1]
                        black_list = pygame.Rect(block.getCoordinate(x_res - basicX, self.deltaX),
                                                block.getCoordinate(y_res - basicY, self.deltaY), 64, 64)
                        if black_list.collidepoint(mx, my):

                            if block.priority < active_block.priority:
                                if active_block.state == 'stretched':
                                    self.fun_reg(x_res, y_res, active_block.name, True)

                                else:
                                    print(x_res, y_res, active_block, '>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                    exception_coordinates[y_res][x_res].append(active_block)

                                if active_block.state == 'manual_control':
                                    active_block.block = self.hand_slots[self.num_conrl][1].block
                                    active_block.img_last = self.hand_slots[self.num_conrl][1].img_last

                                if active_block.str_name == 'Chest':
                                    self.storage_list.append([x_res, y_res, []])
                                    print('chest creat', x_res, y_res)


                                for key in self.inventory:
                                    if key[0] == self.hand_slots[self.num_conrl][1].name:
                                        key[1] -= 1
                                        if key[1] == 0:
                                            del key[1]
                                        break

                                self.hand_slots[self.num_conrl][0] -= 1
                                if self.hand_slots[self.num_conrl][0] == 0:
                                    self.hand_slots[self.num_conrl] = None



                            elif block.name == bl.Nonee and active_block.priority == 1:
                                exception_coordinates[y_res][x_res].clear()
                                if active_block.name == bl.Grass:
                                    self.fun_reg(x_res, y_res, active_block.name, True)
                                else:
                                    exception_coordinates[y_res][x_res].append(active_block.name(x_res, y_res))


                            else:
                                print('exception block')


    def delBlock(self, mx, my):
        basicX = (self.x_map // 64) - 11
        basicY = (self.y_map // 64) - 7
        for y_res in range((self.y_map // 64) - self.dist_dam - 1, (self.y_map // 64) + self.dist_dam):
            for x_res in range((self.x_map // 64) - self.dist_dam, (self.x_map // 64) + self.dist_dam + 1):
                block = exception_coordinates[y_res][x_res][-1]
                black_list = pygame.Rect(block.getCoordinate(x_res - basicX, self.deltaX),
                                         block.getCoordinate(y_res - basicY, self.deltaY), 64, 64)
                if black_list.collidepoint(mx, my):
                    if self.hand_slots[self.num_conrl] and block.resources:
                        self.damage = tl.damage_calculation(block.resources[0], self.hand_slots[self.num_conrl][1].name)
                    else:
                        self.damage = 1
                    
                    block.strength -= self.damage

                    print('Damage: ', self.damage)
                    if block.strength <= 0:
                        if len(exception_coordinates[y_res][x_res]) > 1:
                            if block.state == 'stretched' and block.name != bl.Nonee:
                                exception_coordinates[y_res][x_res].pop()
                                self.fun_reg(x_res, y_res, block.name, False)

                            else:
                                exception_coordinates[y_res][x_res].pop()
                                print('Сломанный блок:', block.name)

                            if block.resources:
                                self.control_inventory(block.resources)


                        elif len(exception_coordinates[y_res][x_res]) == 1:
                            block.strength = block.base_strength
                            self.fun_reg(x_res, y_res, bl.Nonee, True)




class Admin(Pleer):
    def __init__(self):
        super().__init__('Admin')





