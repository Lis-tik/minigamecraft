import pygame
from random import randint


def all_tools():
    list_all = [[Axe, 'Axe']]
    return list_all


def damage_calculation(resoures, active_tool):
    if resoures:
        if active_tool == Axe and resoures == 'Wood':
            return Axe(0, 0).damage
        
        elif active_tool == Pickaxe and resoures == 'Pebbles':
            return Pickaxe(0, 0).damage
    
    return 1

class BaseTools():
    def __init__(self, x, y, name, str_name, strength, block, block_ico, damage=None, radius=None,
                  state='nonstretched', resources=None, craft=False, aim=0, stack=1):
        
        self.x = x
        self.y = y

        self.name = name
        self.str_name = str_name

        self.strength = strength
        self.base_strength = strength

        self.block = block
        self.block_ico = block_ico

        self.state = state

        self.resources = resources
        self.craft = craft

        self.damage = damage
        self.radius = radius

        self.aim = aim

        self.stack = stack

        self.animcount = 0

    
            
        


class Axe(BaseTools):
    def __init__(self, x , y):
        img = pygame.image.load('./Spritse/tools/Axe/Axe.png')
        super().__init__(x, y, Axe, "Axe", 100, img, img, 15, 1, craft=['Iron', 20])

    
class Pickaxe(BaseTools):
    def __init__(self):
        img = pygame.image.load('./Spritse/tools/Sword.png')
        super().__init__(Pickaxe, "Pickaxe", 100, img, img, 15, 1, craft=['Pebbles', 20])


class Bow(BaseTools):
    def __init__(self):
        img = pygame.image.load('./Spritse/tools/Bow.png')
        super().__init__(Bow, "Bow", 100, img, img, 10, 70)

    def aim(self, coordinates):
        aim = coordinates
