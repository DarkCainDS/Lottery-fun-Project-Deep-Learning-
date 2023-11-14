import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def scrape(url):
    # Hacemos la petición a la URL y parseamos el contenido con BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Buscamos el div con la clase 'comodin'
    comodin_div = soup.find('div', class_='comodin')
    if comodin_div:  # Comprobar si el div fue encontrado
        comodin_number = comodin_div.get_text().strip()  # Obtenemos el texto dentro del div
        return comodin_number
    return None  # Si no encontramos el div, retornamos None

# ... Resto de tu código

def main(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(scrape, urls))

    for comodin_number in results:
        if comodin_number:  # Si el número no es None
            print(comodin_number)

if __name__ == "__main__":
    BASE_URL = "https://www.prensadigital.cl/resultados-del-loto-sorteo-{}-del-{}.html"
    endpoints = [
        # Formato: (numero_sorteo, fecha)
        
(5016, '03-de-octubre-de-2023'),
        # ... agregar otros endpoints según necesites
    ]

    urls_to_scrape = [BASE_URL.format(sorteo, fecha) for sorteo, fecha in endpoints]
    main(urls_to_scrape)
