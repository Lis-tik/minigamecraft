import pygame
import block_add as bl
import tools_add as tl

pygame.init()
# Текст
f0 = pygame.font.Font(None, 60)
f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 40)
f3 = pygame.font.Font(None, 30)
f4 = pygame.font.Font(None, 20)



pygame.init()
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('RPG engine 0')


#Инвентарь
Inventory = pygame.image.load('./Spritse/Inventory_main_menu.png')
info_craft = pygame.image.load('./Spritse/info_craft.png')
hand_slots_ico = pygame.image.load('./Spritse/hand_slots_flag.png')
inventory_x = 0
inventory_y = 0

wood_ic = pygame.image.load('./Spritse/resources/wood_lot.png')
pebbles_ic = pygame.image.load('./Spritse/resources/Pebbles.png') 
dirt_ic = pygame.image.load('./Spritse/resources/Dirt.png') 
iron_ic = pygame.image.load('./Spritse/resources/Iron.png') 



active_craft = False
type_click = False


def ret_active_craft():
    return active_craft


def summary(inventory_contents):
    global active_craft
    block = active_craft

    win.blit(block.block, (1400, 25))
    
    available = inventory_contents[block.craft[0]]


    if block.craft[0] == 'Wood':
        win.blit(wood_ic, (1300, 80))

    elif block.craft[0] == 'Pebbles':
        win.blit(pebbles_ic, (1300, 80))

    if available >= block.craft[1]:
        color = (0, 255, 127)
        message = 'Скрафтить ENTER'

    else:
        color = (220, 20, 60)
        message = 'Недостаточно ресурсов'



    materials_str = f2.render((f'{available}/{block.craft[1]}'), 1, (0, 0, 0))

    control_message = f2.render((f'{message}'), 1, (color))
    
    win.blit(materials_str, (1360, 100))
    win.blit(control_message, (1300, 700))
        




def inventory_func(inventory_contents, inventory, x=0, y=0, hand_slots=None):

    global active_craft
    global type_click

    inv_str = f1.render('Инвентарь', 1, (0, 0, 0))
    crft_str = f1.render('Крафт предметов', 1, (0, 0, 0))
    win.blit(Inventory, (inventory_x, inventory_y))

    win.blit(inv_str, (25, 25))
    win.blit(crft_str, (815, 25))


    #Wood resource
    wood_ic_str = f2.render(str(inventory_contents['Wood']), 1, (0, 0, 0))

    win.blit(wood_ic, (50, 750))
    win.blit(wood_ic_str, (120, 765))

    #Pebble resource
    pebbles_ic_str = f2.render(str(inventory_contents['Pebbles']), 1, (0, 0, 0))

    win.blit(pebbles_ic, (50, 800))
    win.blit(pebbles_ic_str, (120, 815))

    #Dirt resource
    dirt_ic_str = f2.render(str(inventory_contents['Dirt']), 1, (0, 0, 0))

    win.blit(dirt_ic, (200, 750))
    win.blit(dirt_ic_str, (270, 765))

    
    #Iron resource
    iron_ic_str = f2.render(str(inventory_contents['Iron']), 1, (0, 0, 0))

    win.blit(iron_ic, (200, 800))
    win.blit(iron_ic_str, (270, 815))


    #Craft  
    fol_x = 815
    fol_y = 80

    all_list_craft = []

    for log in bl.all_blocks(), tl.all_tools():
        for ter in log:
            if ter[0](0, 0).craft:
                if (fol_x - 825) // 64 >= 5:
                    fol_y += 64 + 15

                    fol_x = 825

                block_win = ter[0](fol_x, fol_y)
                all_list_craft.append([block_win, pygame.Rect(fol_x, fol_y, 64, 64), 'craft'])
                #quantity_txt = f4.render(str(self.inventory_contents['Wood']), 1, (0, 0, 0))

                win.blit(block_win.block, (block_win.x, block_win.y))
                fol_x += 64 + 25



    #Inventory
    fol_x = 25
    fol_y = 80

    for key in inventory:

        if (fol_x - 25) // 64 >= 11:
            fol_y += 64 + 15

            fol_x = 25

        block_win = key[0]
        block_win.x = fol_x
        block_win.y = fol_y
        all_list_craft.append([block_win, pygame.Rect(fol_x, fol_y, 64, 64), 'inventory'])

        quantity_txt = f3.render(str(key[1]), 1, (0, 0, 0))
        
        win.blit(block_win.block, (block_win.x, block_win.y))
        win.blit(quantity_txt, (block_win.x, block_win.y + 70))
        fol_x += 64 + 25


            

    if x or y:
        for lont in all_list_craft:
            if lont[1].collidepoint(x, y):
                active_craft = lont[0]
                type_click = lont[2]
                break             
        else:
            active_craft = False


    if active_craft:
        if type_click == 'craft':
            win.blit(hand_slots_ico, (active_craft.x - 3, active_craft.y - 3))
            summary(inventory_contents)

        elif type_click == 'inventory':
            win.blit(hand_slots_ico, (active_craft.x - 3, active_craft.y - 3))

        pygame.display.update() 
        return active_craft
    
    #pygame.display.update() 