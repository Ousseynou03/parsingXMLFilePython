import xml.etree.ElementTree as ET
import requests
import concurrent.futures

def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

def main():
    # URL du fichier XML
    urlXml = 'https://ecom-prod.galerieslafayette.com/siteMap/Homepage-fr-EUR.xml'

    # Télécharger le contenu XML depuis l'URL
    response = requests.get(urlXml)
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

if __name__ == "__main__":
    main()
