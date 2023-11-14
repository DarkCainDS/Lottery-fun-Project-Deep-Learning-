import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def scrape(url):
    # Hacemos la petición a la URL y parseamos el contenido con BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Buscamos todos los div con la clase 'bolitas'
    number_divs = soup.find_all('div', class_='bolitas')

    numbers_list = [] # Una lista para guardar los números
    for div in number_divs:
        numbers = div.get_text().strip().split() # Separamos cada número por espacio
        
        # Solo agregamos a la lista si hay exactamente 6 números
        if len(numbers) == 6:
            numbers_list.append(numbers)

    return numbers_list

def main(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(scrape, urls))

    for url, numbers_sets in zip(urls, results):
        for numbers in numbers_sets:
            print(" - ".join(numbers))

if __name__ == "__main__":
    BASE_URL = "https://www.prensadigital.cl/resultados-del-loto-sorteo-{}-del-{}.html"
    endpoints = [
        # Formato: (numero_sorteo, fecha)

(5016, '03-de-octubre-de-2023'),

      # ... agregar otros endpoints según necesites
    ]

    urls_to_scrape = [BASE_URL.format(sorteo, fecha) for sorteo, fecha in endpoints]
    main(urls_to_scrape)
