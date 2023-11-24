import xml.etree.ElementTree as ET
import requests
import concurrent.futures

def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

def process_xml_from_url(url):
    # Télécharger le contenu XML depuis l'URL
    response = requests.get(url)
    
    if response.status_code == 200:
        xml_content = response.content

        # Parsing du XML
        root = ET.fromstring(xml_content)

        # Liste pour stocker les URLs
        urls = []

        # Récupérer les URLs depuis le XML
        for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            urls.append(loc.text)

        # Utiliser concurrent.futures.ThreadPoolExecutor pour effectuer les requêtes en parallèle
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(fetch_url, urls)
    elif response.status_code == 404:
         print("Une réponse 200, n'a pas été obtenue." 
        "\n   Le chemin de l'url n'existe pas")

    else:
        print("Une réponse 200, n'a pas été obtenue." 
        "\n   Vous n'avez pas les autorisations néccessaies pour effectuer le parsing"
        "\n 403 Forbidden.")

def main():
    # Liste des URLs à traiter
    urls = [
        'https://ecom-prod.galerieslafayette.com/siteMap/Homepage-fr-EUR.xml',
        'https://ecom-prod.galerieslafayette.com/siteMap/Category-fr-EUR.xml',
    ]

    # Appliquer la logique pour chaque URL
    for url in urls:
        process_xml_from_url(url)

if __name__ == "__main__":
    main()
