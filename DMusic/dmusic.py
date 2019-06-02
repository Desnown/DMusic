#! -*- coding: utf-8 -*-

#IMPORT KIVY
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import ListProperty, StringProperty

#IMPORT KIVYMD
from kivymd.theming import ThemeManager
from kivymd.button import MDFillRoundFlatButton, MDRaisedButton
from kivymd.label import MDLabel
from kivymd.list import MDList

#IMPORTS OTHERS
from functool_music import namefile, search_music_path, read_file, caminho_proj
from pdb import set_trace
from vlc import MediaPlayer

from termcolor import cprint



#DECLARATION
cor_cinza = [.125, .125, .125, 1]
cor_azul = [.129,.588,.953, 1]


# Window.icon = 'Imagem/icone.png'

class Main(ScreenManager):
    pass

    
class Abertura(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        # print(key)
        if key == 27:
            self.sair()
        if key == 118:
            self.manager.current = 'Abertura'
        return True

    def sair(self,*args, **kwargs):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        botoes = BoxLayout(padding=(35,7), spacing=10)
        pop = Popup(title='Deseja mesmo sair ?',
                    content=box,
                    size_hint=(None, None),
                    size=(200,200),
                    separator_color=cor_azul,
                    title_align='center',
                    auto_dismiss=False,
                    title_color=[1,1,1,1])
                    # background='Imagem/back.png')

        img = Image(source='Imagem/att.png')
        yes = MDFillRoundFlatButton(text='Sim', on_release=App.get_running_app().stop)
        no = MDFillRoundFlatButton(text="Não", on_release=pop.dismiss)

        botoes.add_widget(yes)
        botoes.add_widget(no)

        box.add_widget(img)
        box.add_widget(botoes)

        aumentar_tela = Animation(size=(300,180), t='out_back', d=.4)
        aumentar_tela.start(pop)

        pop.open()
        return True


class Player(Screen):
    '''
    Screen responsavel pela parte da musica, `read musics, play, pause, left,
    next, stop, etc`
    '''
    musics = ListProperty([])
    song = StringProperty('')
    bt_primary = 'play'
    bt_secundary = 'pause'
    chamou = False
    contador = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = MediaPlayer()
        self.new = []


    def on_pre_leave(self):
        self.ids.box_music.clear_widgets()


    def load(self, win='nova', *args):   
        '''Metodo responsavel por ler a pasta(nova ou a usada anteriormente - 
           'velha') e adiciona-las no programa( add_widget ).
        '''     
        if win == 'nova':
            self.musics = search_music_path()

        else:
            self.musics = read_file()
            
        self.musics.sort()
        for music in self.musics: 
            #Dando uma pausa para o programa para que os widgets nn fiquem
            #  tudo 'encavalado'.          
            Clock.usleep(300000)
            self.ids.box_music.add_widget(MYRaisedButton(text=namefile(music)))
            self.new.append(music+'\n') 
            self.contador+=1     
            
        self.adicionar_musics()
          

    def play(self, song):
        '''Metodo responsavel por reproduzir as musicas.
        '''
        if song != None:
            self.song = song
            try:
                #Pausando o player para que nn toque multiplas musicas
                self.stop()
                self.sound = MediaPlayer(self.song)
                self.sound.play()
                self.button()
                MYRaisedButton().exchange_name(self.song)
                self.chamou = True
                # self.button() Arrumar ainda '-'
                self.print_music(self.song)
                # Clock.schedule_once(self.next, )

            except Exception as error:
                print(error)

    def back(self):
        '''Metodo responsavel por reproduzir a musica anterior.
        '''
        self.play(self.index(-1))

    def pause(self):
        '''Metodo responsavel por pausar a musica.
        '''
        if self.chamou:
            self.button('play')
            self.chamou = False
        else:
            self.button('pause')
            self.chamou = True

        self.sound.pause()

    def next(self, *args):
        '''Metodo responsavel por reproduzir a musica seguinte.
        '''
        self.play(self.index())

    def stop(self):
        '''Metodo responsavel por parar a musica.
        '''
        self.sound.stop()

    def lenght_music(self):
        return self.sound.get_length()/60000


    def button(self, _button='pause'):
        '''Metodo responsavel por trocar o botao na hora que ele
            'e' pressionado.
        '''
        if _button == 'pause':
            self.bt_primary = 'pause'

        else:            
            self.bt_primary = 'play'

        self.children[0].children[0].ids.play.icon = self.bt_primary

    def index(self, arg=1):
        '''Metodo responsavel por pegar o indice da musica atual
           e devolvar o indice da musica anterior(-1) ou posterior(1).
        '''
        try:
            if self.musics.index(self.song) == len(self.musics) and arg==1:
                print(self.musics[0])
                return self.musics[0]

            return self.musics[self.musics.index(self.song)+arg]
        except:
            pass


    def adicionar_musics(self):
        '''Adicionar(txt) as novas musicas lidas na pasta selecionada.
        '''
        with open(f'{caminho_proj}/Songs.txt', 'w') as self.save:
            # for new in self.new:
            #     self.save.write(new+self.adic)
            self.save.writelines(self.new)

    def print_music(self, song):
        '''Metodo nn muito importante, mas print no terminal o nome da musica
           que esta sendo tocada
        '''
        print('[', end='')
        cprint('INFO', 'green', attrs=['bold'], end='')
        print(f'   ] [Audio       ] Song Played: {self.song}')


class BarPlayer(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     if len(self.ids.label_music.text)>30:
    #         self.ids.
    pass

class MYRaisedButton(MDRaisedButton):
    def exchange_name(self, texto):
        App.get_running_app().root.get_screen('Player').children[0].\
        children[0].ids.label_music.text=namefile(texto)



class DMusic(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.primary_hue = '500'
    theme_cls.theme_style ='Dark'

    def build(self):
        self.icon = 'icone.png'
        return Main()

    def on_stop(self):
        Player().stop()


DMusic().run()