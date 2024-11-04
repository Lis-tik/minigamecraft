# import pygame
# import block_add as bl
# from random import randint

# pygame.init()
# #1600 900
# win = pygame.display.set_mode((1600, 900))
# pygame.display.set_caption('Main menu')


# # 12 - 7
# x_pers = 768
# y_pers = 448


# # Текст
# f1 = pygame.font.Font(None, 50)
# f2 = pygame.font.Font(None, 40)
# f3 = pygame.font.Font(None, 20)
# f4 = pygame.font.Font(None, 30)

# MagPersImg = pygame.image.load('./Spritse/Mag_collision.png')



# # Инвентарь
# hand_slots_ico = pygame.image.load('./Spritse/hand_slots_flag.png')
# Inventory = pygame.image.load('./Spritse/Inventory.png')
# inventory_x = 0
# inventory_y = 0


# # Меню
# Menu = pygame.image.load('./Spritse/Menu.png')
# Exit_rect = pygame.Rect(30, 30, 450, 60)

# #Меню креатива
# creative_menu = [bl.Bush, bl.Spruce, bl.Grass, bl.Flower_white, bl.Stone, bl.Chest, bl.Barrel, bl.Brick, bl.Blue_pottery, 
#                  bl.Boiler, bl.Anvil, bl.Table, bl.Bonfire, bl.Door, bl.Wood_2, bl.Fence, bl.Cobblestone, bl.Chair, bl.Vase,
#                  bl.White_wall]





# move_right = []
# move_left = []
# move_up = []
# move_down = []




# as_core = {
#     'right': move_right,
#     'left': move_left,
#     'up': move_up,
#     'down': move_down
# }

# as_core_put = (as_core.items())

# for bor, bor_op in as_core_put:
#     for vy in range(2):
#         img_cbl = pygame.image.load(f'./Spritse/Skins/PersonTST/{bor}/Person_{vy}.png')
#         bor_op.append(img_cbl)

# #print(move_right, move_left, move_up, move_down)


# animCount = 0

# def person_up(lok):
#     if lok == 'stay':
#         win.blit(pygame.image.load(f'./Spritse/Skins/PersonTST/Person_.png'), (x_pers, y_pers))

#     else:
#         global animCount
#         img_cbl = as_core[lok]

#         if animCount + 1 >= 12:
#             animCount = 0


#         animCount += 1
#         win.blit(img_cbl[animCount // 6], (x_pers, y_pers))

#     pygame.display.update()


# class WinUpdate:
#     def __init__(self, x_map, y_map):
#         self.x_map = x_map
#         self.y_map = y_map
#         self.black_list = []
#         self.flag_menu = False


            


#     def ainvent(self, x=0, y=0):
#         #if type(x) == int and type(y) == int:
#         #txt = f1.render('Креатив меню', 1, (0, 0, 0))
#         #win.blit(txt, (25, 25))
#         win.blit(Inventory, (inventory_x, inventory_y))
#         fol_x = inventory_x + 25
#         fol_y = inventory_y + 25

#         for b in range(1, len(creative_menu)):
#             blo = creative_menu[b]

#             baseBlock = blo(fol_x, fol_y) 
#             colise = pygame.Rect(fol_x, fol_y, 64, 64)
#             self.black_list.append([baseBlock, colise])

#             win.blit(baseBlock.block, (baseBlock.x, baseBlock.y))

#             fol_x += 74

#             if b % 10 == 0 and b != 0:
#                 fol_y += 74
#                 fol_x = inventory_x + 25
            

#         for lont in self.black_list:
#             if lont[1].collidepoint(x, y):
#                 win.blit(hand_slots_ico, (lont[0].x - 3, lont[0].y - 3))
#                 return lont[0].name
            


                
#         pygame.display.update()


#     def menu(self):
#         self.flag_menu = True
#         win.blit(Menu, (0, 0))
#         pygame.draw.rect(win, (255, 255, 255), Exit_rect)
#         menu_exit_text = f1.render('Выйти из игры', 1, (0, 0, 0))
#         win.blit(menu_exit_text, (50, 50))
#         pygame.display.update()



#     def storage_contents(self, inventory, x=0, y=0):
        
#         win.blit(Inventory, (inventory_x, inventory_y))
        
#         fol_x = inventory_x + 850

#         fol_y = inventory_y + 25

#         for b in range(1, len(inventory)):
#             blo = creative_menu[b]

#             baseBlock = blo(fol_x, fol_y) 
#             colise = pygame.Rect(fol_x, fol_y, 64, 64)
#             self.black_list.append([baseBlock, colise])

#             win.blit(baseBlock.block, (baseBlock.x, baseBlock.y))

#             fol_x += 74

#             if b % 10 == 0 and b != 0:
#                 fol_y += 74
#                 fol_x = inventory_x + 25

#         for lont in self.black_list:
#             if lont[1].collidepoint(x, y):
#                 win.blit(hand_slots_ico, (lont[0].x - 3, lont[0].y - 3))
#                 return lont[0].name
                
#         pygame.display.update()

    

#     def technical_panel(self, hp, stamina):
#         hp_txt = f1.render(str(hp), 1, (0, 0, 0))
#         win.blit(hp_txt, (100, 100))






