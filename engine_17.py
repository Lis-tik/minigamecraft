import pygame
import sys
#import win_up as wup
import win_update as wup
import inventory as inv
import Character_handler as runc
from time import sleep



fps_track = 0


# 12 - 7
x_pers = 768
y_pers = 448




active_move = ''

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


corset = {
    'active': True,
    'hand_slots_flag': True,
    'invent': False,
    'menu': False,
    'storage_contents': False
}

speed_v2 = 4
dismount = 0


# Коллизия
black_list = []

# персонаж
damage = 50
dist_dam = 3


form = 0


# 25 14
# Генерация мира

'''file_exp = open('./worlds/New world/world.txt', 'r', encoding='UTF8')
exception_coordinates = file_exp.read()'''


# print(exception_coordinates[0][10][10].getCoordinateX(10, 12))


def ret_active_win():
    return corset


go_active = runc.Handler_move()

clock = pygame.time.Clock()
run = True
while run:
    '''     temp_X = (self.x_map / 64)
            temp_Y = (self.y_map / 64)

            fps = clock.get_fps() // 1

            fps_screen = f2.render(str(fps), 1, (0, 0, 0))
            pygame.draw.rect(win, (255, 255, 255), (1400, 800, 60, 25))

            Xcord_temp = f2.render(str(temp_X), 1, (0, 0, 0))
            Ycord_temp = f2.render(str(temp_Y), 1, (0, 0, 0))

            coord_screen_X = f2.render(str(self.x_map), 1, (0, 0, 0))
            coord_screen_Y = f2.render(str(self.y_map), 1, (0, 0, 0))
            pygame.draw.rect(win, (255, 255, 255), (10, 15, 320, 90))

            deltaX_screen = f2.render(str(self.deltaX), 1, (0, 0, 0))
            deltaY_screen = f2.render(str(self.deltaY), 1, (0, 0, 0))

            win.blit(fps_screen, (1400, 800))
            win.blit(coord_screen_X, (20, 20))
            win.blit(coord_screen_Y, (200, 20))

            win.blit(Xcord_temp, (20, 50))
            win.blit(Ycord_temp, (200, 50))

            win.blit(deltaX_screen, (20, 80))
            win.blit(deltaY_screen, (200, 80))'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


#        elif event.type == pygame.MOUSEBUTTONUP:
#           if event.button == 1:
#                if corset['invent']:
#                    Mouse_hold = False
#                    print(Mouse_hold)




        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                x = (mx // 64)
                y = (my // 64)
                print('Подробные координаты: ', mx, my)
                print('Сокращённые координаты: ', x, y)
                if corset['menu']:
                    if wup.Exit_rect.collidepoint(mx, my):
                        print('EXIT')
                        runc.close_thread()
                        sys.exit()

                if corset['active']:
                    go_active.delBlock(mx, my)
 
                if corset['invent']:
                    go_active.call_inventory(mx, my)


                if corset['storage_contents']:
                    go_active.manual_control(None, wup.storage_contents(mx, my))



            if event.button == 3:
                mx, my = pygame.mouse.get_pos()
                x = (mx // 64)
                y = (my // 64)
                print('Подробные координаты: ', mx, my)
                print('Сокращённые координаты: ', x, y)

                if corset['active']:
                    go_active.stuck_block(mx, my, x, y)




        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                corset['menu'] = not corset['menu']
                corset['active'] = not corset['active']

                wup.menu()



            if event.key == pygame.K_F7:
                go_active.technical_panel(fps_track)



            if event.key == pygame.K_TAB:
                corset['invent'] = not corset['invent']
                corset['active'] = not corset['active']

                go_active.call_inventory()
                go_active.manual_control()

                print(corset['invent'])




            if event.key == pygame.K_r and corset['active']:
                go_active.manual_control(manual_split=True)



            if event.key == pygame.K_e:
                
                if go_active.interaction(active_move) != False:
                    corset['storage_contents'] = not corset['storage_contents']
                    corset['active'] = not corset['active']

                    wup.storage_contents(go_active.interaction(active_move))


            '''if event.key == pygame.K_RETURN:
                if inv.ret_active_craft():
                    go_active.add_craft_item(inv.ret_active_craft())'''
      


            if corset['hand_slots_flag']:
                if event.key == pygame.K_1:
                    go_active.manual_control(0)
                if event.key == pygame.K_2:
                    go_active.manual_control(1)
                if event.key == pygame.K_3:
                    go_active.manual_control(2)
                if event.key == pygame.K_4:
                    go_active.manual_control(3)
                if event.key == pygame.K_5:
                    go_active.manual_control(4)
                if event.key == pygame.K_6:
                    go_active.manual_control(5)

                    


    keys = pygame.key.get_pressed()

    if corset['invent']:
        if keys[pygame.K_RETURN]:
            if inv.ret_active_craft():
                go_active.add_craft_item(inv.ret_active_craft())
            #sleep(0.1)

    if corset['active']:
        
        if keys[pygame.K_LSHIFT]:
            dismount = 4
        else:
            dismount = 0

        if keys[pygame.K_d]:
            active_move = 'right'
            go_active.right(speed_v2 + dismount)

        elif keys[pygame.K_a]:
            active_move = 'left'
            go_active.left(speed_v2 + dismount)

        elif keys[pygame.K_w]:
            active_move = 'up'
            go_active.up(speed_v2 + dismount)

        elif keys[pygame.K_s]:
            active_move = 'down'
            go_active.down(speed_v2 + dismount)

        else:
            go_active.stay()


    fps_track = clock.tick(60)

