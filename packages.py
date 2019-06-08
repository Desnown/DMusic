#! -*- coding: utf-8 -*-

def install_module():
    '''Função resp. por fazer a instalação dos módulos.
    '''

    from os import system

    print("\nFazendo a instalação dos módulos necessários.")
    packages = {'glob2':'glob2', 'kivy':'kivy',
                'kivymd':'kivymd', 'termcolor':'termcolor',
                'vlc':'python-vlc'}


    while True:
        try:
            import glob2, kivy, kivymd, termcolor, vlc
            break
        except ModuleNotFoundError as module_error:
            system(f'python3 -m pip install {packages[module_error.name]} --user')