from os import system
packages = ['glob2', 'kivy', 'kivymd', 'python-vlc', 'termcolor']

for pack in packages:
    try:    
        system(f'python3 -m pip install {pack} --user')
    except:
        pass
