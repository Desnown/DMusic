from kivy.config import Config
Config.set("graphics","width",500)
Config.set("graphics","height",500)


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Inicial(FloatLayout):
	pass


class MyApp(App):
	def build(self):
		return Inicial()



if __name__ == "__main__":
    MyApp().run()
