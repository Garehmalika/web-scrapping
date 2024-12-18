import requests
from bs4 import BeautifulSoup
import json

# URL de l'article
url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

# Ajouter des headers pour imiter un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Faire une requête HTTP avec les headers
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    html_content = response.text
    
    # Charger le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extraire le titre de l'article
    title_tag = soup.find('h1')  # Adapter en fonction de la structure HTML du site
    title = title_tag.text if title_tag else "Titre non trouvé"

    # Extraire le contenu principal
    content_tag = soup.find('div', class_='article-content')  # Adapter la classe CSS
    content = content_tag.text if content_tag else "Contenu non trouvé"

    # Structurer les données
    article_data = {
        "title": title,
        "content": content
    }

    # Afficher les données sous forme JSON
    print(json.dumps(article_data, indent=4))
elif response.status_code == 403:
    print("Accès interdit (403). Essayez d'ajouter des headers ou vérifiez les permissions du site.")
elif response.status_code == 404:
    print("Page non trouvée (404). Vérifiez l'URL.")
else:
    print(f"Erreur : {response.status_code}")
