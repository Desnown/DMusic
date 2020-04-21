from os import chdir, getcwd
from termcolor import cprint

caminho_music = '/home/desnown/Music/'
caminho_proj = getcwd()
chdir(caminho_proj)


def namefile(file):
    '''Retorna somente o nome da musica.
    '''

    file = file.replace('\n', '')

    try:
        return ' '.join(file.split('.')[:-1])
    except Exception as error:
        cprint(error, 'red', attrs=['bold'])


def search_music_path(pasta='/Music'):
    '''Funcao responsavel por procurar todos os arquivos de musicas
    `.wav; .ogg; .mp3; .m4a`  na pasta e retorna-los.
    '''

    from os import listdir
    from glob2 import glob

    all_musics = []
    _extensoes = ['*.wav', '*.ogg', '*.mp3', '*.m4a']

    try:
        # Este caminho nn é o correto( argumento pasta é o correto)
        # Vai ser arrumado posteriormente usando o filechooser(kivy)
        chdir(home_user() + pasta)

    except Exception as error:
        cprint(error, 'red', attrs=['bold'])

    for ext in _extensoes:
        file = glob(ext)  # irá retornar uma lista
        if file == []:
            continue

        for music in file:  # percorrendo cada valor
            all_musics.append(music)

    return all_musics

# def shorten_music(music):
#     music = namefile(music)
#     if len(music) > 30:
#         return music[:30]+'...'

#     return music


def home_user():
    '''Encontra a pasta $HOME do usuario'''
    from os.path import expanduser
    return expanduser('~')
