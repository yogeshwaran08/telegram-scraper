sentence = """
Captación de Clientes para Agencias de marketing digital  -- 2 (https://freelancer.com/projects/social-media-marketing/captaci-clientes-para-agencias-marketing.html)
Llevas tiempo buscando clientes o no te acaba de gustar el proceso de captar clientes, hablar con ellos, agendas llamadas, reuniones... Deja de perder tu tiempo y deja que nosotros encontremos los clientes para ti. Somos una agencia especializada en captación de clientes para Agencias de Marketing Digital. Te ahorramos muchísimo tiempo que puedes estar invirtiendo en hacer tus proyectos como especialista en marketing que eres. Queremos que seas exitoso y es por eso mismo que debes estar enfocado en tus estrategias para mejorar las empresas de tus clientes. Así que nosotros nos encargaremos de encontrar los clientes ideales para tu agencia por ti.

Skills required
Advertising, Facebook Marketing, Internet Marketing, Marketing, Social Media Marketing
💰250EUR - 750EUR
👤Juanmii2004 (https://freelancer.com/u/Juanmii2004.html) from Mahon , Spain
"""


import spacy
from .data import technology_keywords, places_keyword
import re

nlp = spacy.load("en_core_web_sm")

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
        sample = arr[0]
        return sample[-3:]


def extract_technology_keywords(text):
    doc = nlp(text)
    
    found_technologies = []

    for word in doc:
        if word.text.upper() in technology_keywords:
            found_technologies.append(word.text)
    
    return found_technologies

def extract_place_keywords(text):
    doc = nlp(text)
    found_places = []
    
    for word in doc:
        if word.text in places_keyword:
            found_places.append(word.text)
    
    return found_places

def extract_freelancer_links(text):
    # Define the regular expression pattern to match URLs
    pattern = r'https://freelancer\.com/projects/\S+'
    
    # Use the findall function to extract all matching URLs
    matches = re.findall(pattern, text)
    
    return matches
            
def get_links(msg):
    pattern = r'https?://\S+|www\.\S+'
    pattern = r"r'/u/(\w+\.html)'"
    pattern = r'https://freelancer\.com/u/([a-zA-Z0-9_-]+)'

    # Use re.findall to find all links in the message
    links = re.findall(pattern, msg)
    
    if len(links) >= 1:
        return links[0]
    else:
        return []


if __name__ == "__main__":
    # technology_keywords = extract_technology_keywords(sentence)
    
    # print("\nTechnology keywords mentioned:")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # if technology_keywords:
    #     for keyword in technology_keywords:
    #         print(keyword)
    # else:
    #     print("No technology keywords found in the message.")
        
    # places_keywords = extract_place_keywords(sentence)
    
    # print("\nPlace keyword found mentioned")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # if places_keywords:
    #     for keyword in places_keywords:
    #         print(keyword)
    # else:
    #     print("No place keyword found")

    # print("links")
    # print(get_links(sentence))
    print(extract_freelancer_links(sentence))
