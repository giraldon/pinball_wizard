import scrapy
import pandas as pd
import numpy as np

class PinballWizard(scrapy.Spider):
    name = 'Pinball_Machines'

    custom_settings = {
            "DOWNLOAD_DELAY": 3,
            "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
            "HTTPCACHE_ENABLED": True
        }

    def start_requests(self):
        domain = "http://ipdb.org/machine.cgi?gid="
        for i in range(1, 6550):
            yield scrapy.Request(url=domain+str(i), callback=self.parse)
            print(i)

    def parse(self, response):
        try:
            name = (
                response.xpath('//font[contains(@size, "+3")]/b/text()').extract()
            )
        except:
            name = np.nan
        try:
            rating = (
                response.xpath('//a[contains(@target, "showrate")]/b/text()').extract()
            )
        except:
            rating = np.nan
        try:    
            number_of_ratings = (
                str(response.xpath(
                    '//b[contains(text(),"Average Fun Rating")]/../following-sibling::td/a[2]/text()').extract())[2:5]
            )
        except:
            number_of_ratings = np.nan
        try:    
            manufacturer = (
                response.xpath(
                    '//b[contains(text(),"Manufacturer")]/../following-sibling::td/span/a/text()').extract()[0]
            )
        except:
            manufacturer = np.nan    
        try:
            manufacture_date = (
                response.xpath(
                    '//b[contains(text(),"Date Of Manufacture")]/../following-sibling::td/text()').extract()
            )
        except:
            manufacture_date = np.nan    
        try:     
            machine_type = (
                response.xpath(
                    '//b[contains(text(),"Type")]/../following-sibling::td/text()').extract()
            )
        except:
            machine_type = np.nan  
        try:    
            mpu = (
                response.xpath(
                    '//b[contains(text(),"MPU")]/../following-sibling::td/span/a/text()').extract()
            )
        except:
            mpu = np.nan
        try:    
            production = (
                response.xpath(
                    '//b[contains(text(),"Production")]/../following-sibling::td/text()').extract()
            )
        except:
            production = np.nan
        try:    
            theme = (
                response.xpath(
                    '//b[contains(text(),"Theme")]/../following-sibling::td/text()').extract()
            )
        except:
            theme = np.nan
        try:    
            specialty = (
                response.xpath('//b[contains(text(),"Specialty")]/../following-sibling::td/text()').extract()[0]
            )
        except:
            specialty = np.nan
        try:   
            special = (
                len(response.xpath(
                    '//b[contains(text(),"Notable Features")]/../following-sibling::td/a/text()').extract())
            )
        except:
            special = np.nan 

        yield {
                'name':name,
                'rating': rating,
                'number of ratings': number_of_ratings,
                'manufacturer': manufacturer,
                'manufacture date': manufacture_date,
                'machine type': machine_type,
                'mpu': mpu,
                'production': production,
                'theme': theme,
                'specialty': specialty,
                'features': special
            }

