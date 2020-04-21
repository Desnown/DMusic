#! -*- coding: utf-8 -*-

# IMPORTS
from kivy.app import App
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivymd.button import MDFillRoundFlatButton
from kivymd.theming import ThemeManager


# VARIAVEIS
cor_default = [0.153, 0.361, 0.541, 1]
cor_default_2 = [0.259, 0.647, 0.961, 1]


class Manager(ScreenManager):
    pass


class Init(Screen):
    def on_enter(self):
        Window.bind(on_keyboard=self.options)

    def options(self, window, key, *args):
        if key == 27:
            self.sair()
            return True

    def sair(self):
        box = BoxLayout(orientation="vertical", spacing=dp(5))
        botoes = BoxLayout(pos_hint={'right': 1.15}, spacing=dp(5))
        pop = Popup(title='Deseja mesmo sair ?',
                    content=box,
                    size_hint=(None, None),
                    size=(200, 200),
                    separator_color=cor_default,
                    title_align='center',
                    auto_dismiss=False,
                    title_color=cor_default,
                    background='')

        img = Image(source='Imagem/att.png')
        yes = MDFillRoundFlatButton(
            text='Sim', on_release=App.get_running_app().stop, _radius=dp(14))
        yes.text_color = [1, 1, 1, 1]

        no = MDFillRoundFlatButton(
            text="Não", on_release=pop.dismiss, _radius=dp(14))
        no.text_color = [1, 1, 1, 1]

        botoes.add_widget(yes)
        botoes.add_widget(no)

        box.add_widget(img)
        box.add_widget(botoes)

        aumentar_tela = Animation(size=(280, 160), t='out_back', d=.4)
        aumentar_tela.start(pop)

        pop.open()
        return True


class DMusic(App):
    '''Classe principal.'''

    icon = 'icone.png'
    title = 'DMusic Player'

    # Theme Kivymd
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.primary_hue = '600'
    theme_cls.theme_style = 'Dark'

    def build(self):
        return Manager()


DMusic().run()
