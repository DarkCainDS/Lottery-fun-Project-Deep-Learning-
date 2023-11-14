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

    numbers = []
    for tag in tags:
        match = pattern.search(tag.get_text())
        if match:
            numbers.append(match.group())

    return numbers

def main(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(scrape, urls))

    for url, numbers_list in zip(urls, results):
        print(f"URL: {url}")
        for numbers in numbers_list:
            print(numbers)
        print("----")

if __name__ == "__main__":
    BASE_URL = "https://chile.as.com/actualidad/resultados-loto-chile-hoy-numeros-que-cayeron-y-premios-del-sorteo-{}-ganadores-{}-n/"
    endpoints = [
        (5015, "01-de-octubre"),
        (5014, "28-de-septiembre"),
        (5013, "26-de-septiembre"),
        (5012, "24-de-septiembre"),
        (5011, "21-de-septiembre"),
        (5010, "19-de-septiembre"),
        (5009, "17-de-septiembre"),
        (5008, "14-de-septiembre"),
        (5007, "12-de-septiembre")
    ]
    urls_to_scrape = [BASE_URL.format(sorteo, fecha) for sorteo, fecha in endpoints]
    main(urls_to_scrape)
