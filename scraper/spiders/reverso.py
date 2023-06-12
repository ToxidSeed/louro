import scrapy
from scraper.items import ScraperItem


class ContextReversoSpider(scrapy.Spider):
    name="ContextReverso"

    def parse(self, response):
        page = response.url.split("/")[-2]
    
        contenedor_resultados = response.css('div#translations-content')
        if len(contenedor_resultados) == 1:
            contenedor_resultados = contenedor_resultados[0]

        lista_elem_traducciones = contenedor_resultados.css(".translation")
        lista_traducciones = {}

        new_item = ScraperItem()

        for elem in lista_elem_traducciones:
            traduccion = elem.attrib["data-term"]
            grupo = elem.attrib.get("data-posgroup")

            if grupo not in lista_traducciones:
                lista_traducciones[grupo] = [traduccion]
            else:
                lista_traducciones[grupo].append(traduccion)

        new_item["traducciones"] = lista_traducciones
        yield new_item

        #traducciones = contenedor_resultados.css(".translation").getall()
        #animals = [item.root for item in results]
        #print(results)
        #filename = f'quotes-{page}.html'
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log(f'Saved file {filename}')


