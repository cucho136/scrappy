import scrapy
import csv

from paginasAmarilla.items import PaginasamarillaItem


class ContratistaSpiders(scrapy.Spider) :
    name="contratista"
    allowed_domains = ["www.yellowpages.com"]
    custom_settings = {'LOG_LEVEL':'INFO'}

    def ObtenerNumeros(self,file):
        numeros = []
        with open(file, newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                numeros.append(row)
        return numeros

    def start_requests(self):
        urls=[]
        web="https://people.yellowpages.com/whitepages/phone-lookup?phone="
        numeros =self.ObtenerNumeros('phones.csv')
        for numero in numeros:
            info=web+numero[0]
            urls.append(info)
        for url in urls:
            #print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        output_data=PaginasamarillaItem()
        try:
            output_data['name']=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/a[1]/text()').extract_first()
            direccion=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/p[1]/text()').extract_first()
            output_data['phone']=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/p[2]/text()').extract_first()
            try:
                ubicacion=direccion.split(',')
                output_data['address']=ubicacion[0]
                estado=ubicacion[2].split(' ')
                output_data['city']= ubicacion[1]
                output_data['state'] =estado[1]
                output_data['ZIP'] =estado[2]
                output_data['phone']=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/p[2]/text()').extract_first()
                yield output_data
            except:
                pass

        except:
            pass
