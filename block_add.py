import pygame
import os
from random import randint

status = {
    'right': False,
    'left': False,
    'up': False,
    'down': False,
}


def all_blocks():
    list_bl = [[Nonee, 'Nonee'], [Grass, 'Grass'], [Wood_2, 'Wood_2'], [Spruce, 'Spruce'], 
               [Bush, 'Bush'], [Flower_white, 'Flower_white'], [Stone, 'Stone'], 
               [Barrel, 'Barrel'], [Brick, 'Brick'], [Anvil, 'Anvil'], [Table, 'Table'], 
               [Vase, 'Vase'], [Blue_pottery, 'Blue_pottery'], [Boiler, 'Boiler'], 
               [Bonfire, 'Bonfire'], [Cobblestone, 'Cobblestone'], [Fence, 'Fence'], 
               [White_wall, 'White_wall'], [Door, 'Door'], [Chair, 'Chair'], 
               [Chest, 'Chest'], [Test_wood, 'Test_wood']]

    return list_bl



class BaseBlock():
    def __init__(self, x, y, name, str_name, priority, strength, colision, block, block_ico,
                  state='nonstretched', img_last=0, resources=None, craft=False, content=[], stack=100):
        self.x = x
        self.y = y
        self.priority = priority
        self.name = name
        self.str_name = str_name
        self.strength = strength
        self.base_strength = strength
        self.colision = colision
        self.block = block
        self.block_ico = block_ico
        self.state = state
        self.img_last = img_last
        self.content = content
        self.resources = resources
        self.craft = craft
        self.stack = stack
        self.animcount = 0



    def getCoordinate(self, x=0, delta=0):
        return x * 64 + delta
    
    def record(self, block):
        res = (f'{block.y} {block.x} {block.str_name} {block.strength} {block.img_last} {block.colision} ')
        return res



# Приоритет - 0
class Nonee(BaseBlock):
    def __init__(self, x, y):

        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        
        img_non = (f'./Spritse/Block/pit/pit_{sal}.png')
        img = pygame.image.load(img_non)
        super().__init__(x, y, Nonee, "Nonee", 1, 9999999, True, img, img, "stretched", img_non)



# Приоритет - 1
class Grass(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Grass_02.png')
        super().__init__(x, y, Grass, "Grass", 1, 70, False, img, img, resources=['Dirt', 15], craft=['Dirt', 15])

class Wood_2(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Wood_2.png')
        super().__init__(x, y, Wood_2, "Wood_2", 2, 50, False, img, img)


'''class Blue_pottery(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Blue_pottery.png')
        super().__init__(x, y, Blue_pottery, "Blue_pottery", 2, 15, False, img, img)'''

# Приоритет - 2
class Spruce(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Spruce.png')
        super().__init__(x, y, Spruce, "Spruce", 3, 20, True, img, img, resources=['Wood', randint(3, 9)])


class Test_wood(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Test wood/Test_wood_0.png')
        img_ico = pygame.image.load('./Spritse/Block/Test wood/Test_wood_1.png')
        super().__init__(x, y, Test_wood, "Test_wood", 3, 50, True, img, img_ico, state='high_block', resources=['Wood', randint(3, 9)])


class Bush(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Bush.png')
        super().__init__(x, y, Bush, "Bush", 3, 20, True, img, img, resources=['Wood', randint(1, 3)])

class Flower_white(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for vy in range(12):
            img_cbl = f'./Spritse/Block/Flower white/Flower_white_{vy}.png'
            block_list.append(img_cbl)


        img_cbl = block_list[randint(0, len(block_list)-1)]

        img = pygame.image.load(img_cbl)
        super().__init__(x, y, Flower_white, "Flower_white", 3, 1, False, img, img)

class Stone(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Stone.png')
        super().__init__(x, y, Stone, "Stone", 3, 100, True, img, img, resources=['Pebbles', randint(3, 9)])

        

class Barrel(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Barrel.png')
        super().__init__(x, y, Barrel, "Barrel", 3, 40, True, img, img)


class Brick(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for vy in range(6):
            img_cbl = f'./Spritse/Block/Brick/Brick_{vy}.png'
            block_list.append(img_cbl)


        img_cbl = block_list[randint(0, len(block_list)-1)]

        img = pygame.image.load(img_cbl)
        super().__init__(x, y, Brick, "Brick", 3, 30, False, img, block_list, img_cbl, resources=['Pebbles', randint(1, 3)])


'''class Chest(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Chest/Chest.png')
        super().__init__(x, y, Chest, "Chest", 3, 20, True, img, img)'''


class Anvil(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Anvil.png')
        super().__init__(x, y, Anvil, "Anvil", 3, 40, True, img, img)


class Table(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Table.png')
        super().__init__(x, y, Table, "Table", 3, 30, True, img, img, craft=['Wood', 20])


class Vase(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Vase.png')
        super().__init__(x, y, Vase, "Vase", 4, 3, True, img, img)



class Blue_pottery(BaseBlock):
    def __init__(self, x, y):
        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        img_cbl = (f'./Spritse/Block/Blue_pottery(1)/blue_pottery_{sal}.png')
        Cobblestone_img = pygame.image.load(img_cbl)

        super().__init__(x, y, Blue_pottery, "Blue_pottery", 2, 15, False, Cobblestone_img, Cobblestone_img, 'stretched', img_cbl)



class Boiler(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for vy in range(4):
            img_cbl = pygame.image.load(f'./Spritse/Block/Boiler/Boiler_{vy}.png')
            block_list.append(img_cbl)

        img = pygame.image.load('./Spritse/Block/Boiler.png')
        super().__init__(x, y, Boiler, "Boiler", 3, 30, True, img, block_list, 'animation')


class Bonfire(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for vy in range(4):
            img_cbl = pygame.image.load(f'./Spritse/Block/Bonfire/Bonfire_{vy}.png')
            block_list.append(img_cbl)

        img = pygame.image.load('./Spritse/Block/Bonfire/Bonfire_0.png')
        super().__init__(x, y, Bonfire, "Bonfire", 3, 15, True, img, block_list, 'animation')





class Cobblestone(BaseBlock):
    def __init__(self, x, y):
        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        img_cbl = (f'./Spritse/Block/Cobblestone/Cobblestone_{sal}.png')
        Cobblestone_img = pygame.image.load(img_cbl)

        super().__init__(x, y, Cobblestone, "Cobblestone", 3, 150, True, Cobblestone_img, Cobblestone_img, 'stretched', img_cbl, craft=['Pebbles', 20])





class Fence(BaseBlock):
    def __init__(self, x, y):
        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        img_cbl = (f'./Spritse/Block/Fence/Fence_{sal}.png')
        Fence_img = pygame.image.load(img_cbl)

        super().__init__(x, y, Fence, "Fence", 3, 50, True, Fence_img, Fence_img, 'stretched', img_cbl)




class White_wall(BaseBlock):
    def __init__(self, x, y):
        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        img_cbl = (f'./Spritse/Block/White wall/White_wall_{sal}.png')
        img = pygame.image.load(img_cbl)

        super().__init__(x, y, White_wall, "White_wall", 3, 100, True, img, img, 'stretched')




class Door(BaseBlock):
    def __init__(self, x, y):
        code = []
        for key in status:
            if status[key]:
                code.append(key)

        sal = "_".join(code)
        img_cbl = (f'./Spritse/Block/Door/Door_{sal}.png')
        
        if os.path.exists(img_cbl):
            img = pygame.image.load(img_cbl)
        else:
            img = pygame.image.load('./Spritse/Block/Door/Door_.png')
            img_cbl = './Spritse/Block/Door/Door_.png'
            

        lot = [['./Spritse/Block/Door/Door_.png', './Spritse/Block/Door/Door_open.png'],
               ['./Spritse/Block/Door/Door_up_down.png', './Spritse/Block/Door/Door_up_down_open.png']]

        super().__init__(x, y, Door, "Door", 3, 100, True, img, lot, 'stretched', img_cbl, craft=['Wood', 20])



'''class Cobblestone(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for key in range(3):
            esf = pygame.image.load(f'./Spritse/Block/Wall/Wall_{key}.png')
            block_list.append(esf)

        img = pygame.image.load('./Spritse/Block/Wall/Wall_0.png')

        super().__init__(x, y, Cobblestone, "Cobblestone", 3, 15, True, img, block_list, 'manual_control')'''




class Chair(BaseBlock):
    def __init__(self, x, y):

        block_list = []
        for key in range(4):
            esf = (f'./Spritse/Block/Chair/Chair_{key}.png')
            block_list.append(esf)


        img = pygame.image.load('./Spritse/Block/Chair/Chair_0.png')

        super().__init__(x, y, Chair, "Chair", 3, 20, True, img, block_list, 'manual_control', craft=['Wood', 20])


class Chest(BaseBlock):
    def __init__(self, x, y):
        img = pygame.image.load('./Spritse/Block/Chest/Chest.png')
        super().__init__(x, y, Chest, "Chest", 3, 25, True, img, img, 'Interaction')