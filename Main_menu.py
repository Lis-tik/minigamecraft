import pygame
import sys
import os
import block_add as bl
from random import randint
from datetime import datetime
import subprocess




pygame.init()
win = pygame.display.set_mode((1600, 900))

fon_main_menu = pygame.image.load('./Spritse/Inventory.png')



f0 = pygame.font.Font(None, 70)
f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 40)
f3 = pygame.font.Font(None, 20)
f4 = pygame.font.Font(None, 30)


class Button():
    def __init__(self, width=0, height=0, color=None, text=None, color_text=None, link=None, method=None):
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.color_text = color_text
        self.link = link
        self.method = method
        self.colision = []



    def win_creat(self, x, y):
        actual_button = pygame.Rect(x, y, self.width, self.height)
        self.colision = [actual_button, self.link, self.method]
        actual_text = f1.render(str(self.text), 1, (self.color_text))
        pygame.draw.rect(win, (self.color), actual_button)
        win.blit(actual_text, (x + 15, y + 15))



class Win_update():
    def win_cup(self):
        win.blit(fon_main_menu, (0, 0))

        Open_world_text = f0.render('Главное меню', 1, (255, 255, 255))
        win.blit(Open_world_text, (30, 30))

        self.open_world_botton = Button(550, 60, (255, 255, 255), 'Открыть существующий мир', (0, 0, 0), Open_world)
        self.open_world_botton.win_creat(50, 100)

        self.creat_world_botton = Button(550, 60, (255, 255, 255), 'Создать мир', (0, 0, 0), Creat_world)
        self.creat_world_botton.win_creat(50, 200)

        self.edit_character_botton = Button(550, 60, (255, 255, 255), 'Редактировать персонажа', (0, 0, 0), Edit_character)
        self.edit_character_botton.win_creat(50, 300)

        self.exit_game_botton = Button(550, 60, (255, 255, 255), 'Выйти из игры', (0, 0, 0), Exit)
        self.exit_game_botton.win_creat(50, 400)

        pygame.display.update()

    def return_list(self):
        black_list = [self.open_world_botton.colision, self.creat_world_botton.colision, self.edit_character_botton.colision, self.exit_game_botton.colision]
        return black_list




class Exit():
    def win_cup(self):
        sys.exit()


class Open_world():
    def win_cup(self):

        self.tmp_list = []

        win.blit(fon_main_menu, (0, 0))

        Open_world_text = f0.render('Открыть существующий мир', 1, (255, 255, 255))
        win.blit(Open_world_text, (30, 30))

        self.back_button = Button(150, 60, (255, 255, 255), 'Назад', (0, 0, 0), Win_update)
        self.back_button.win_creat(50, 785)
        self.tmp_list.append(self.back_button.colision)

        files = os.listdir('./worlds')

        flag = 0

        for f in files:

            self.f = Button(600, 100, (240, 240, 240), str(f), (0, 0, 0), Open_world, str(f))
            self.f.win_creat(50, (100 + flag * 150))

            self.tmp_list.append(self.f.colision)
            
            flag += 1

        pygame.display.update()


    def return_list(self):
        return self.tmp_list



class Creat_world():
    def __init__(self):
        self.difficult = 1
        self.size = 0
        self.mode = 1
        self.name = 'New world'

        self.Name = 'Lopi'
        self.Skin = 'Crash' 
        self.Hp = '100'
        self.Inventory = []

    def win_cup(self):
        list_mode = ['Креатив', 'Выживание']
        list_diffic = ['Лёгкая', 'Нормальная', 'Сложная', 'Очень сложная']
        list_size = ['Маленький', 'Средний', 'Большой']

        win.blit(fon_main_menu, (0, 0))

        creat_world_text = f0.render('Создать мир', 1, (255, 255, 255))
        win.blit(creat_world_text, (30, 30))

        fon_txt = pygame.Rect(50, 100, 600, 60)
        pygame.draw.rect(win, (240, 240, 240), fon_txt)

        line_name = f1.render((f'Имя мира: {self.name}'), 1, (15, 15, 15))
        win.blit(line_name, (65, 115))

        self.dificult_button = Button(600, 60, (32, 32, 32), (f'Сложность игры: {list_diffic[self.difficult]}'), (255, 255, 255), Creat_world, self.return_diff)
        self.dificult_button.win_creat(50, 200)

        self.size_world_button = Button(600, 60, (32, 32, 32), (f'Размер мира: {list_size[self.size]}'), (255, 255, 255), Creat_world, self.return_size)
        self.size_world_button.win_creat(50, 300)

        self.mode_world_button = Button(600, 60, (32, 32, 32), (f'Режим игры: {list_mode[self.mode]}'), (255, 255, 255), Creat_world, self.return_mode)
        self.mode_world_button.win_creat(50, 400)

        self.creat_world_botton = Button(600, 60, (32, 32, 32), 'Создать мир', (0, 153, 0), Creat_world, self.save_world)
        self.creat_world_botton.win_creat(50, 500)

        self.back_button = Button(150, 60, (255, 255, 255), 'Назад', (0, 0, 0), Win_update)
        self.back_button.win_creat(50, 785)

        pygame.display.update()

    def return_diff(self):
        self.difficult += 1
        if self.difficult > 3:
            self.difficult = 0

    def return_size(self):
        self.size += 1
        if self.size > 2:
            self.size = 0
        print(self.size)

    def return_mode(self):
        self.mode += 1
        if self.mode > 1:
            self.mode = 0

    def return_name(self, mode_read):
        if mode_read == 'del':
            self.name = self.name[:-1]
        else:
            self.name += mode_read
        print(self.name)

    def save_world(self):
        load_text = f2.render('Загрузка...', 1, (0, 100, 0))
        win.blit(load_text, (50, 580))
        pygame.display.update()

        exception_coordinates = str()
        mobs_data = str()
        #exception_coordinates += ('50\n')
        #exception_coordinates += ('50\n')

        if self.size == 0:
            long = 30
        elif self.size == 1:
            long = 50
        elif self.size == 2:
            long = 100

        for y in range(long):
            for x in range(long):

                grass = bl.Grass(x, y)
                exception_coordinates += (f'{grass.record(grass)}\n')
                sprus_pro = randint(0, 20)
                if sprus_pro == 0 or sprus_pro == 5: 
                    test_wood = bl.Test_wood(x, y)
                    exception_coordinates += (f'{test_wood.record(test_wood)}\n')
                    
                if sprus_pro == 1:
                    bush = bl.Bush(x, y)
                    exception_coordinates += (f'{bush.record(bush)}\n')

                if sprus_pro == 2:
                    flower_white = bl.Flower_white(x, y)
                    exception_coordinates += (f'{flower_white.record(flower_white)}\n')

                if sprus_pro == 3:
                    stone = bl.Stone(x, y)
                    exception_coordinates += (f'{stone.record(stone)}\n')

                if sprus_pro == 4:
                    brick = bl.Brick(x, y)
                    exception_coordinates += (f'{brick.record(brick)}\n')



        

        os.mkdir(f"worlds/{self.name}")

        file = open(f'./worlds/{self.name}/world.txt', 'w', encoding="utf-8")
        file.write(str(exception_coordinates))

        character = open(f'./worlds/{self.name}/character.txt', 'w', encoding="utf-8")
        character_list = {'Name': self.Name, 'Skin': self.Skin, 'Hp': self.Hp, 'Inventory': self.Inventory}

        for logIn, logOn in list(character_list.items()):
            character.write(str(f'{logIn} = {logOn}\n'))

        profile = open(f'./worlds/{self.name}/list.txt', 'w', encoding="utf-8")
        profile_list = {'Name': self.name, 'difficult': self.difficult, 'Mode': self.mode, 'Size': self.size, 'Time': datetime.now()}

        for logIn, logOn in list(profile_list.items()):
            profile.write(str(f'{logIn} = {logOn}\n'))

        mobs = open(f'./worlds/{self.name}/mobs.txt', 'w', encoding="utf-8")
        mobs.write(str(mobs_data))

        file.close()
        profile.close()
        character.close()
        mobs.close()


    def return_list(self):
        black_list = [self.back_button.colision, self.dificult_button.colision, self.size_world_button.colision, self.mode_world_button.colision, self.creat_world_botton.colision]
        return black_list


class Edit_character():
    def win_cup(self):
        win.blit(fon_main_menu, (0, 0))

        edit_character_text = f0.render('Редактировать персонажа', 1, (255, 255, 255))
        win.blit(edit_character_text, (30, 30))

        self.back_button = Button(150, 60, (255, 255, 255), 'Назад', (0, 0, 0), Win_update)
        self.back_button.win_creat(50, 785)

        pygame.display.update()



    def return_list(self):
        black_list = [self.back_button.colision]
        return black_list


active = Win_update()
active.win_cup()



def start_world(world):
    filein = open('./world start.txt', 'w', encoding='utf-8')
    filein.write(str(world))
    filein.close()

    subprocess.run(["python", "./engine_17.py"])



run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                print('Подробные координаты: ', mx, my)

                for x in active.return_list():
                    if x[0].collidepoint(mx, my):
                        if type(x[2]) == str:
                            start_world(x[2])
                        elif x[2]:
                            x[2]()

                        else:
                            active = x[1]()
                        active.win_cup()
                        break


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                active.return_name('del')
            else:
                active.return_name(event.dict['unicode'])

            active.win_cup()


