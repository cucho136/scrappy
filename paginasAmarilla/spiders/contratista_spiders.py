import scrapy
import csv


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
        try:
            nombre=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/a[1]/text()').extract_first()
            direccion=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/p[1]/text()').extract_first()
            phone=response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[2]/div[1]/p[2]/text()').extract_first()
            #print(nombre)
            ubicacion=direccion.split(',')
            direccion=ubicacion[0]
            estado=ubicacion[2].split(' ')
            yield {
                'name':nombre ,
                'address': direccion,
                'city': ubicacion[1],
                'state': estado[1],
                'ZIP':estado[2],
                'phone': phone,
                }
        except:
            pass
