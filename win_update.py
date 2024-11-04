import pygame
import block_add as bl
from random import randint

pygame.init()
#1600 900
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Main menu')


# 12 - 7
x_pers = 768
y_pers = 448


# Текст
f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 40)
f3 = pygame.font.Font(None, 20)
f4 = pygame.font.Font(None, 30)

MagPersImg = pygame.image.load('./Spritse/Mag_collision.png')



# Инвентарь
hand_slots_ico = pygame.image.load('./Spritse/hand_slots_flag.png')
Inventory = pygame.image.load('./Spritse/Inventory.png')
inventory_x = 0
inventory_y = 0


# Меню
Menu = pygame.image.load('./Spritse/Menu.png')
Exit_rect = pygame.Rect(30, 30, 450, 60)

#Меню креатива
creative_menu = [bl.Bush, bl.Spruce, bl.Grass, bl.Flower_white, bl.Stone, bl.Chest, bl.Barrel, bl.Brick, bl.Blue_pottery, 
                 bl.Boiler, bl.Anvil, bl.Table, bl.Bonfire, bl.Door, bl.Wood_2, bl.Fence, bl.Cobblestone, bl.Chair, bl.Vase,
                 bl.White_wall]





black_list = []
flag_menu = False



def ainvent(x=0, y=0):
    #if type(x) == int and type(y) == int:
    #txt = f1.render('Креатив меню', 1, (0, 0, 0))
    #win.blit(txt, (25, 25))
    win.blit(Inventory, (inventory_x, inventory_y))
    fol_x = inventory_x + 25
    fol_y = inventory_y + 25

    for b in range(1, len(creative_menu)):
        blo = creative_menu[b]

        baseBlock = blo(fol_x, fol_y) 
        colise = pygame.Rect(fol_x, fol_y, 64, 64)
        black_list.append([baseBlock, colise])

        win.blit(baseBlock.block, (baseBlock.x, baseBlock.y))

        fol_x += 74

        if b % 10 == 0 and b != 0:
            fol_y += 74
            fol_x = inventory_x + 25
        

    for lont in black_list:
        if lont[1].collidepoint(x, y):
            win.blit(hand_slots_ico, (lont[0].x - 3, lont[0].y - 3))
            return lont[0].name
    pygame.display.update()


def menu(flag_menu):
    flag_menu = True
    win.blit(Menu, (0, 0))
    pygame.draw.rect(win, (255, 255, 255), Exit_rect)
    menu_exit_text = f1.render('Выйти из игры', 1, (0, 0, 0))
    win.blit(menu_exit_text, (50, 50))
    pygame.display.update()



def storage_contents(inventory, x=0, y=0):
    win.blit(Inventory, (inventory_x, inventory_y))
    fol_x = inventory_x + 850
    fol_y = inventory_y + 25
    for b in range(1, len(inventory)):
        blo = creative_menu[b]

        baseBlock = blo(fol_x, fol_y) 
        colise = pygame.Rect(fol_x, fol_y, 64, 64)
        black_list.append([baseBlock, colise])

        win.blit(baseBlock.block, (baseBlock.x, baseBlock.y))

        fol_x += 74

        if b % 10 == 0 and b != 0:
            fol_y += 74
            fol_x = inventory_x + 25

    for lont in black_list:
        if lont[1].collidepoint(x, y):
            win.blit(hand_slots_ico, (lont[0].x - 3, lont[0].y - 3))
            return lont[0].name
            
    pygame.display.update()



def technical_panel(hp, stamina):
    hp_txt = f1.render(str(hp), 1, (0, 0, 0))
    win.blit(hp_txt, (100, 100))











