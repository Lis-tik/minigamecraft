import pygame
import block_add as bl
import inventory as inv
import data_base_control as db
import creature as ct
import tools_add as tl
import Person_Control as pc


x_pers = 768
y_pers = 448


dist_dam = 3



move = {
    'right': False,
    'left': False,
    'up': False,
    'down': False,
}


status_one = {
    'rt': False,
    'lt': False,
    'up': False,
    'dn': False,
}

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

#Свет
light_01 = pygame.image.load('./Spritse/light_01.png')


# ПРОЧНОСТЬ
strength_01 = pygame.image.load('./Spritse/strength/strength_01.png')
strength_02 = pygame.image.load('./Spritse/strength/strength_02.png')
strength_03 = pygame.image.load('./Spritse/strength/strength_03.png')
strength_04 = pygame.image.load('./Spritse/strength/strength_04.png')


#Слот рук
hand_slots_img = pygame.image.load('./Spritse/hand_slots.png')
hand_slots_ico = pygame.image.load('./Spritse/hand_slots_flag.png')
pos_hand_slots_X = 600
pos_hand_slots_Y = 800







'''exception_coordinates = []
for y in range(50):
    exception_coordinates.append([])
    for x in range(50):
        exception_coordinates[y].append([])

        exception_coordinates[y][x].append(bl.Grass(x, y))
        sprus_pro = randint(0, 20)
        if sprus_pro == 0:
            exception_coordinates[y][x].append(bl.Spruce(x, y))
        if sprus_pro == 1:
            exception_coordinates[y][x].append(bl.Bush(x, y))
        if sprus_pro == 2:
            exception_coordinates[y][x].append(bl.Flower_white(x, y))
        if sprus_pro == 3:
            exception_coordinates[y][x].append(bl.Stone(x, y))'''




#thread1.join()

exception_coordinates = db.start_world()

width_map = db.start_world(True)
long_map = db.start_world(True)

person_hp = db.ret_character('Hp')


ct.ex_cord(exception_coordinates)


#print(exception_coordinates)

such = [ct.Zombie(0, 0)]

for fog in such:
    fog.thread.start()



move_right = []
move_left = []
move_up = []
move_down = []



as_core = {
    'right': move_right,
    'left': move_left,
    'up': move_up,
    'down': move_down
}

as_core_put = (as_core.items())

for bor, bor_op in as_core_put:
    for vy in range(4):
        img_cbl = pygame.image.load(f'./Spritse/Skins/Person/{bor}/Person_{vy}.png')
        bor_op.append(img_cbl)

#print(move_right, move_left, move_up, move_down)



class Handler_move:
    def __init__(self):
        self.x_map = 0 #- speed_v2
        self.y_map = 0 #- speed_v2
        self.deltaX = 64
        self.deltaY = 64
        self.hp = person_hp
        self.storage_list = []
        self.ec = exception_coordinates
        self.animCount = 0
        self.num_conrl = 0
        self.mode_block = 0
        self.damage = 1
        self.inventory = []
        self.inventory_contents = {'Wood': 5000, 'Pebbles': 5000, 'Dirt': 5000, 'Iron': 5000}
        self.hand_slots = [None, None, None, None, None, None]


    def control_inventory(self, resources):
        if resources:
            self.inventory_contents[resources[0]] += resources[1]


    def call_inventory(self, mx=0, my=0):
        self.manual_control(None, inv.inventory_func(self.inventory_contents, self.inventory, mx, my))




    def add_craft_item(self, item):
        if not self.inventory_contents[item.craft[0]] - item.craft[1] < 0:
            self.inventory_contents[item.craft[0]] -= item.craft[1]


            for loot in self.inventory:
                if item.name == loot[0].name:
                    if loot[1] != item.stack:
                        loot[1] += 1
                        break

            else:
                if len(self.inventory) <= 71:
                    toolbl = inv.inventory_func(self.inventory_contents, self.inventory)
                    self.inventory.append([toolbl.name(toolbl.x, toolbl.y), 1])

            print(self.inventory)
            inv.inventory_func(self.inventory_contents, self.inventory)



    def WinUpdate(self, lok=None):

        basicX = (self.x_map // 64) - 11
        basicY = (self.y_map // 64) - 7


        for y_res in range((self.y_map // 64) - 8, (self.y_map // 64) + 9):
            for x_res in range((self.x_map // 64) - 12, (self.x_map // 64) + 14):
                for block in exception_coordinates[y_res][x_res]:

                    if block.state == 'animation':
                        if block.animcount + 1 >= 16:
                            block.animcount = 0

                        block.animcount += 1
                        block.block = block.block_ico[block.animcount // 4]

                    elif block.state == 'high_block':
                        win.blit(block.block, (block.getCoordinate(x_res - basicX, self.deltaX),
                                               block.getCoordinate(y_res - basicY, self.deltaY)))
                        
                        win.blit(block.block_ico, (block.getCoordinate(x_res - basicX, self.deltaX),
                                                   block.getCoordinate((y_res - 1) - basicY, self.deltaY)))
                        

                    else:
                        win.blit(block.block, (block.getCoordinate(x_res - basicX, self.deltaX), block.getCoordinate(y_res - basicY, self.deltaY)))


                    if block.strength <= 3 / 4 * block.base_strength:
                        win.blit(strength_01, (block.getCoordinate(x_res - basicX, self.deltaX), block.getCoordinate(y_res - basicY, self.deltaY)))
                    if block.strength <= 2 / 4 * block.base_strength:
                        win.blit(strength_02, (block.getCoordinate(x_res - basicX, self.deltaX), block.getCoordinate(y_res - basicY, self.deltaY)))
                    if block.strength <= 1 / 4 * block.base_strength:
                        win.blit(strength_03, (block.getCoordinate(x_res - basicX, self.deltaX), block.getCoordinate(y_res - basicY, self.deltaY)))


        ct.ex_cord(exception_coordinates)
        #ct.ex_pleers()
        #ct.ex_person(self.x_map, self.y_map, self.hp)

        self.person_up(lok)
        self.win_tools(lok)
        self.essences_up(such)
        self.manual_control()
        #self.damage_pers()
        self.aim_win()
        pygame.display.update()



    def aim_win(self):
        x, y = pygame.mouse.get_pos()
        pygame.draw.line(win, (230, 50, 230), [x_pers + 32, y_pers + 32], [x, y])

    
    def win_tools(self, lok):

        if lok != 'up':
            if self.hand_slots[self.num_conrl]:
                tol_act = self.hand_slots[self.num_conrl][1].name(x_pers + 32, y_pers + 32)

                if str(tol_act.__class__.__base__.__name__) == 'BaseTools':
                    win.blit(tol_act.block, (tol_act.x - 32, tol_act.y - 32))
                    


    def essences_up(self, such):
        basicX = self.x_map - x_pers
        basicY = self.y_map - y_pers
        #print(self.x_map, basicX // 64)
        for essences in such:
            if 'stay' in essences.active_move:
                win.blit(essences.img, ((essences.x - basicX), (essences.y - basicY)))

            else:
                if 'up' in essences.active_move:
                    img_cbl = essences.animlist['up']

                elif 'down' in essences.active_move:
                    img_cbl = essences.animlist['down']

                elif 'right' in essences.active_move:
                    img_cbl = essences.animlist['right']

                elif 'left' in essences.active_move:
                    img_cbl = essences.animlist['left']

                else:
                    img_cbl = essences.animlist['right']


                if essences.animcount + 1 >= 16:
                    essences.animcount = 0

                essences.animcount += 1
                win.blit(img_cbl[essences.animcount // 4], ((essences.x - basicX), (essences.y - basicY)))
                
                #win.blit(essences.img, ((essences.x - basicX), (essences.y - basicY)))



    def person_up(self, lok):
        loco_x = ((self.x_map + 32) // 64)
        loco_y = ((self.y_map - 1) // 64)

        basicX = (self.x_map // 64) - 11
        basicY = (self.y_map // 64) - 7
        
        
        tmp_bl = exception_coordinates[loco_y + 1][loco_x][-1]

        if lok == 'stay' or None:
            win.blit(pygame.image.load(f'./Spritse/Skins/Person/Person_.png'), (x_pers, y_pers))


        else:
            img_cbl = as_core[lok]

            if self.animCount + 1 >= 24:
                self.animCount = 0

            self.animCount += 1
            win.blit(img_cbl[self.animCount // 7], (x_pers, y_pers))
        


        if tmp_bl.state == 'high_block':
            x_lo = tmp_bl.getCoordinate(loco_x - basicX, self.deltaX)
            y_lo = tmp_bl.getCoordinate(loco_y - basicY, self.deltaY)

            win.blit(tmp_bl.block_ico, (x_lo, y_lo))




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



    def stuck_block(self, mx, my, x, y):
        if self.hand_slots[self.num_conrl] != None:

            active_block = self.hand_slots[self.num_conrl][1].name(x, y)
            type_bl = str(active_block.__class__.__base__.__name__)

            if type_bl == 'BaseBlock':
            
                basicX = (self.x_map // 64) - 11
                basicY = (self.y_map // 64) - 7
                for y_res in range((self.y_map // 64) - dist_dam, (self.y_map // 64) + dist_dam):
                    for x_res in range((self.x_map // 64) - dist_dam, (self.x_map // 64) + dist_dam):
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
                        move['up'] = False
                        print('up')
                        return True

                    elif black_list.collidepoint(x_pers + 11, y_pers + 45) or black_list.collidepoint(x_pers + 11,
                                                                                                      y_pers + 61):
                        move['left'] = False
                        print('left')
                        return True

                    elif black_list.collidepoint(x_pers + 9, y_pers + 61) or black_list.collidepoint(x_pers + 48,
                                                                                                     y_pers + 61):
                        move['down'] = False
                        print('down')
                        return True

                    elif black_list.collidepoint(x_pers + 48, y_pers + 45) or black_list.collidepoint(x_pers + 48,
                                                                                                      y_pers + 61):
                        move['right'] = False
                        print('right')
                        return True

                    else:
                        move['right'] = False
                        move['left'] = False
                        move['up'] = False
                        move['down'] = False

                # return False                 


    def delBlock(self, mx, my):
        
        basicX = (self.x_map // 64) - 11
        basicY = (self.y_map // 64) - 7
        for y_res in range((self.y_map // 64) - dist_dam - 1, (self.y_map // 64) + dist_dam):
            for x_res in range((self.x_map // 64) - dist_dam, (self.x_map // 64) + dist_dam + 1):
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


    def fun_reg(self, x_res, y_res, block_lon, satline):
        carsen = block_lon(x_res, y_res).priority

        for one_z in range(len(exception_coordinates[y_res][x_res + 1])):
            one_lot = exception_coordinates[y_res][x_res + 1][one_z]
            if one_lot.state == 'stretched' and one_lot.priority == carsen:
                print(one_z)
                bl.status['right'] = True
                status_one['rt'] = True
                break

        for two_z in range(len(exception_coordinates[y_res][x_res - 1])):
            two_lot = exception_coordinates[y_res][x_res - 1][two_z]
            if two_lot.state == 'stretched' and two_lot.priority == carsen:
                bl.status['left'] = True
                status_one['lt'] = True
                break

        for three_z in range(len(exception_coordinates[y_res + 1][x_res])):
            three_lot = exception_coordinates[y_res + 1][x_res][three_z]
            if three_lot.state == 'stretched' and three_lot.priority == carsen:
                bl.status['down'] = True
                status_one['dn'] = True
                break

        for four_z in range(len(exception_coordinates[y_res - 1][x_res])):
            four_lot = exception_coordinates[y_res - 1][x_res][four_z]
            if four_lot.state == 'stretched' and four_lot.priority == carsen:
                bl.status['up'] = True
                status_one['up'] = True
                break

        if satline:
            exception_coordinates[y_res][x_res].append(block_lon(x_res, y_res))

        if status_one['rt']:
            self.fun_reg_fin(x_res + 1, y_res, one_z)
        if status_one['lt']:
            self.fun_reg_fin(x_res - 1, y_res, two_z)
        if status_one['dn']:
            self.fun_reg_fin(x_res, y_res + 1, three_z)
        if status_one['up']:
            self.fun_reg_fin(x_res, y_res - 1, four_z)

        for x in status_one:
            status_one[x] = False



    def fun_reg_fin(self, x_res, y_res, z_res):

        alib = exception_coordinates[y_res][x_res][z_res]
        
        
        exception_coordinates[y_res][x_res].pop(z_res)


        for x in bl.status:
            bl.status[x] = False


        for one_lot in exception_coordinates[y_res][x_res + 1]:
            if one_lot.state == 'stretched' and one_lot.priority == alib.priority:
                bl.status['right'] = True

        for two_lot in exception_coordinates[y_res][x_res - 1]:
            if two_lot.state == 'stretched' and two_lot.priority == alib.priority:
                bl.status['left'] = True

        for three_lot in exception_coordinates[y_res + 1][x_res]:
            if three_lot.state == 'stretched' and three_lot.priority == alib.priority:
                bl.status['down'] = True

        for four_lot in exception_coordinates[y_res - 1][x_res]:
            if four_lot.state == 'stretched' and four_lot.priority == alib.priority:
                bl.status['up'] = True

        exception_coordinates[y_res][x_res].insert(z_res, alib.name(x_res, y_res))


        for x in bl.status:
            bl.status[x] = False







    def manual_control(self, num=None, block=None, manual_split=False):

        if type(num) == int:
            self.num_conrl = num

        if block != None:
            for tmp_del in range(len(self.inventory)):
                if block == self.inventory[tmp_del][0]:

                    self.hand_slots[self.num_conrl] = [self.inventory[tmp_del][1], self.inventory[tmp_del][0]]

                    block.x = pos_hand_slots_X + (self.num_conrl * (64 + 3)) + 3
                    block.y = pos_hand_slots_Y + 3

                    print(self.inventory[tmp_del][1])
                    self.inventory.pop(tmp_del)
                    inv.inventory_func(self.inventory_contents, self.inventory)
                    break
                        

   

        win.blit(hand_slots_img, (pos_hand_slots_X, pos_hand_slots_Y))
        
        for ran in range(len(self.hand_slots)):
            BaseBlock = self.hand_slots[ran]

            if BaseBlock != None:
                BaseBlock = self.hand_slots[ran][1]
                stat = self.hand_slots[ran][0]

                win.blit(BaseBlock.block, (BaseBlock.x, BaseBlock.y))
                quan_txt = f2.render(str(stat), 1, (0, 0, 0))
                win.blit(quan_txt, (BaseBlock.x, BaseBlock.y + 50))

                if BaseBlock.state == 'manual_control':
                    if manual_split:
                        BaseBlock.animcount += 1
                        if BaseBlock.animcount > len(BaseBlock.block_ico) - 1:
                            BaseBlock.animcount = 0

                        BaseBlock.block = pygame.image.load(BaseBlock.block_ico[BaseBlock.animcount])
                        BaseBlock.img_last = BaseBlock.block_ico[BaseBlock.animcount]

                    txt = f1.render('R', 1, (0, 0, 0))
                    win.blit(txt, (BaseBlock.x, BaseBlock.y))

            if ran == self.num_conrl:
                win.blit(hand_slots_ico, (pos_hand_slots_X + (ran * (64 + 3)), pos_hand_slots_Y))

        pygame.display.update()





    def interaction(self, pool):
        loco_x = ((self.x_map + 32) // 64)
        loco_y = ((self.y_map - 5) // 64)

        block = exception_coordinates[loco_y][loco_x][-1]

        if pool == 'right':
            loco_x += 1
            block = exception_coordinates[loco_y][loco_x][-1]

        elif pool == 'left':
            loco_x -= 1
            block = exception_coordinates[loco_y][loco_x][-1]

        elif pool == 'up':
            loco_y -= 1
            block = exception_coordinates[loco_y][loco_x][-1]

        elif pool == 'down':
            loco_y += 1
            block = exception_coordinates[loco_y][loco_x][-1]


        print(block)

        if block.state == 'Interaction':
            coord_0 = (loco_x, loco_y)

            for f in self.storage_list:
                coord_1 = (f[0], f[1])
                print(coord_0, coord_1)
                if coord_0 == coord_1:
                    return f[2]
                
            return False
        
        if block.str_name == 'Door':
            block.colision = not block.colision

            
            if block.img_last == block.block_ico[1][0] or block.img_last ==  block.block_ico[1][1]:
                print('БОК', block.img_last, block.block_ico[1][0], block.block_ico[1][1])
                
                if block.colision:
                    block.img_last = block.block_ico[1][0] 
                    block.block = pygame.image.load(block.img_last)
                    
                else:
                    block.img_last = block.block_ico[1][1] 
                    block.block = pygame.image.load(block.img_last)

            else:
                print('ПЕРЕД')
                if block.colision:
                    block.img_last = block.block_ico[0][0] 
                    block.block = pygame.image.load(block.img_last)
                else:
                    block.img_last = block.block_ico[0][1] 
                    block.block = pygame.image.load(block.img_last)




        return False
        

def close_thread():
    '''global such
    
    for got in such:
        got.thread.join()'''

    db.save_changes(exception_coordinates)
    print("close_thread close_thread close_thread close_thread")




    

        

