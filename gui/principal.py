import click
import configparser
import scraper.crawler as crawler
import os
from config import settings_ini_file

@click.command()
@click.option('-f',help="Idioma en el que se encuentra el texto")
@click.option('-t',help="Idioma al que se debe traducir")
@click.option('--defaults','defaults',is_flag=True,show_default=True,default=False,help="True si se quiere guardar la configuracion")
@click.option('--debug','debug',is_flag=True,show_default=True,default=False,help="True para depurar")
@click.argument('texto', required=False)

def init(f, t, defaults, debug, texto):    
    if defaults:
        guardar_defaults(f, t)

    if texto is None:
        texto = click.prompt('Ingresar texto para trducir')   
    
    urls = [build_url(f,t,texto)]

    if debug:
        print(urls)

    crawler.start(urls)
    
def obtener_idioma(cod_idioma, tipo=""):
    if tipo not in ["from","to"]:
        raise Exception("no un tipo de idioma para traducción valido, valor: {}".format(tipo))

    config = configparser.ConfigParser()
    config.read(settings_ini_file)        

    langs = config["LANGUAGES"]
    trans = config["TRANSLATION"]

    nom_idioma = ""
    if cod_idioma not in ["",None]:
        nom_idioma = langs[cod_idioma]
    else:
        nom_idioma = langs[trans[tipo]]

    return nom_idioma

def build_url(idioma_origen_codigo, idioma_destino_codigo, texto):
    idioma_origen_nombre = obtener_idioma(idioma_origen_codigo,"from")
    idioma_destino_nombre = obtener_idioma(idioma_destino_codigo,"to")
    texto = texto.replace(" ","+")    
    return "https://context.reverso.net/translation/{0}-{1}/{2}".format(idioma_origen_nombre, idioma_destino_nombre, texto)    

def validar_idioma(lang):
    if lang in [None,""]:
        return

    config = configparser.ConfigParser()
    config.read(settings_ini_file)
    sections = config.sections()
    if "LANGUAGES" not in config:
        raise Exception("No se encuentra la configuración de lenguajes")

    lista_de_idiomas = config["LANGUAGES"]
    if lang not in lista_de_idiomas:
        raise Exception("Idioma {0} no soportado".format(lang))

def guardar_defaults(_from, _to):
    validar_idioma(_from)
    validar_idioma(_to)

    config = configparser.ConfigParser()
    config.read(settings_ini_file)
    sections = config.sections()
    if "TRANSLATION" not in sections:
        config["TRANSLATION"] = {}

    if _from not in ["",None]:
        config["TRANSLATION"]["from"] = _from

    if _to not in ["",None]:
        config["TRANSLATION"]["to"] = _to

    with open(settings_ini_file,"w") as configfile:
        config.write(configfile)
    


