import block_add as bl
import threading
import pygame



all_blocks = bl.all_blocks()

def ret_character(info):

    world_rol = open('./world start.txt', 'r')
    world_temp = str(world_rol.read())
    world_rol.close()

    file_read = open(f'./worlds/{world_temp}/character.txt', 'r')

    for x in file_read:
        if x[0] == info[0]:
            return int(x[-4:-1])




def start_world(long_size=None, Hp=False):
    all_list_cord = []

    world_rol = open('./world start.txt', 'r')
    world_temp = str(world_rol.read())
    world_rol.close()

    file_read = open(f'./worlds/{world_temp}/world.txt', 'r')
    file_optitinal = open(f'./worlds/{world_temp}/list.txt', 'r')


    for pork in file_read:
        tmp_str = str()
        tmp_list = []
        for lenko in pork:
            if lenko != ' ':
                tmp_str += lenko
            else:
                tmp_list.append(tmp_str)
                tmp_str = str()

        all_list_cord.append(tmp_list)


    
    for leq in file_optitinal:
        if leq[0] == 'S':
            size = leq[-2:]
            break



    if int(size) == 0:
        long = 30
    elif int(size) == 1:
        long = 50
    elif int(size) == 2:
        long = 100



    exception_coordinates = []

    for y in range(long):
        exception_coordinates.append([])
        for x in range(long):
            exception_coordinates[y].append([])



    for lofg in all_list_cord:
        x = int(lofg[1])
        y = int(lofg[0])

        for search in all_blocks:
            if search[1] == lofg[2]:
                name = search[0]

        exception_coordinates[y][x].append(name(x, y))

        exception_coordinates[y][x][-1].strength = int(lofg[3])

        if lofg[4] != "0":
            exception_coordinates[y][x][-1].block = pygame.image.load(lofg[4])
            exception_coordinates[y][x][-1].img_last = lofg[4]

        if lofg[5] == 'False':
            exception_coordinates[y][x][-1].colision = False
        else:
            exception_coordinates[y][x][-1].colision = True
            

    file_read.close()

    if long_size:
        return long
    else:
        return exception_coordinates
    
    

def save_changes(exception_coordinates):

    world_rol = open('./world start.txt', 'r')
    world_temp = str(world_rol.read())
    world_rol.close()

    file_read = open(f'./worlds/{world_temp}/world.txt', 'w', encoding='utf-8')

    x = 0
    y = -1

    for ly in exception_coordinates:
        y += 1
        x = -1
        for lx in ly:
            x += 1
            for block in lx:
                wr_str = (f"{y} {x} {block.str_name} {block.strength} {block.img_last} {block.colision} \n")
                file_read.write(str(wr_str))
                
                #print(block.y, block.x, block.str_name, block.strength)
    file_read.close()




