import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re

def scrape(url):
    # Hacemos la petición a la URL y parseamos el contenido con BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Buscamos todas las etiquetas donde podrían estar los números
    tags = soup.find_all(['li', 'p', 'span'])

    # Usamos una expresión regular para identificar las series de 6 números
    pattern = re.compile(r'(\d{1,2} - ){5}\d{1,2}')

    numbers_set = set()  # Usamos un conjunto para evitar duplicados
    for tag in tags:
        match = pattern.search(tag.get_text())
        if match:
            numbers_set.add(match.group())

    return list(numbers_set)  # Convertimos el conjunto a lista para devolverlo


def main(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(scrape, urls))

    for url, numbers_list in zip(urls, results):
        for numbers in numbers_list:
            print(numbers)

if __name__ == "__main__":
    BASE_URL = "https://chile.as.com/actualidad/resultados-loto-chile-hoy-numeros-que-cayeron-y-premios-del-sorteo-{}-ganadores-{}-n/"
    endpoints = [
(4698, '21-de-septiembre'),
(4699, '24-de-septiembre'),
(4700, '26-de-septiembre'),
(4701, '28-de-septiembre'),
(4702, '01-de-octubre'),
(4703, '03-de-octubre'),
(4704, '05-de-octubre'),
(4705, '08-de-octubre'),
(4706, '10-de-octubre'),
(4707, '12-de-octubre'),
(4708, '15-de-octubre'),
(4709, '17-de-octubre'),
(4710, '19-de-octubre'),
(4711, '22-de-octubre'),
(4712, '24-de-octubre'),
(4713, '26-de-octubre'),
(4714, '29-de-octubre'),
    ]
    urls_to_scrape = [BASE_URL.format(sorteo, fecha) for sorteo, fecha in endpoints]
    main(urls_to_scrape)
