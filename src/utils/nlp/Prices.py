import re
from currency_converter import CurrencyConverter

class Prices:
    def __init__(self):
        pass
    
    def get_prices(self,text):
        pattern = r'\d+\s*(?:[A-Z]{3}|[A-Z]{2,4})\s*(?:-\s*\d+\s*(?:[A-Z]{3}|[A-Z]{2,4}))?|\d+\s*(?:[A-Z]{3}|[A-Z]{2,4})/Hr\s*(?:-\s*\d+\s*(?:[A-Z]{3}|[A-Z]{2,4})/Hr)?'
        matches = re.findall(pattern, text)
        if not matches:
            print("Cannot find rate")
            return []
        else:
            if len(matches) >=1:
                res = matches[0].split("-")
                currency = self.extract_currency(res)
                res = self.extract_price(res)
                return res,currency
            else:
                return []

    def extract_price(self,arr):
        res = []
        for i in arr:
            i = i.strip()
            price = i[0:len(i)-3]
            res.append(price)
        return res

    def extract_currency(self,arr):
        sample = arr[0].strip()
        return sample[-3:]
    
    def convert_currency(self,amount,from_cur,to_curr):
        c = CurrencyConverter()
        return c.convert(amount,from_cur, to_curr)        
