import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper') #57 itens
        

        for product in products:
            prices= product.css('span.andes-money-amount__fraction::text').getall()
            cents= product.css('span.andes-money-amount__cents::text').getall()
            rating = product.css('span.poly-component__review-compacted span::text').getall()
            yield{
                'title' : product.css('a.poly-component__title::text').get(),
                'brand' : product.css('span.poly-phrase-label.poly-fw-semibold::text').get(),
                'reviews_rating_number' : rating[0] if len(rating) > 1 else None,
                'sell_amount' : rating[1] if len(rating) > 1 else None,
                'old_price_amount' : prices[0] if len(prices) > 0 else None,
                'old_price_cents' : cents[0] if len(cents) > 0 else None,
                'price_amount' : prices[1] if len(prices) > 1 else None,
                'price_cents' : cents[1] if len(cents) > 1 else None,
            }
        
        if self.page_count <= self.max_pages:

            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count +=1
                yield scrapy.Request(url=next_page, callback=self.parse)
                

            
