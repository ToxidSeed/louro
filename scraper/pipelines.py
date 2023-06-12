# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from gui.console import console
import configparser

class ScraperPipeline:
    def process_item(self, item, spider):
        self.print_traducciones(item.get('traducciones'))
        return item

    def print_traducciones(self, grupos_traducciones={}):        
        config = configparser.ConfigParser()
        config.read("settings.ini")
        colors = config["COLORS"]        

        num_grupo = 1
        for key, grupo in grupos_traducciones.items():
            nombre_grupo = "grupo_{0}".format(num_grupo)
            color_grupo = colors.get(nombre_grupo)
            if color_grupo is None:
                color_grupo = colors.get("default")

            grupo = " ".join(self.escapar_traducciones(grupo))
            console.print("[{0}]{1}".format(color_grupo, grupo))
            num_grupo+=1
            

    def escapar_traducciones(self, grupo=[]):
        grupo_escapado = []
        word = ""
        for texto in grupo:
            word = "'{0}'".format(texto) if len(texto.split()) > 1 else texto
            grupo_escapado.append(word)
        return grupo_escapado
        