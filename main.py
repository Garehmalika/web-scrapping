import requests
from bs4 import BeautifulSoup
import sys

# Fonction pour récupérer le contenu HTML
def get_html_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.cnn.com/",
        "Accept-Language": "en-US,en;q=0.5"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Lève une exception pour les codes HTTP 4xx/5xx
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return None

# Fonction pour analyser et extraire l'article
def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extraire le titre
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'Titre introuvable'

    # Extraire le contenu des paragraphes
    article_content = soup.find_all('p')
    if not article_content:
        article_text = "Aucun contenu d'article trouvé"
    else:
        article_text = '\n\n'.join([p.get_text(strip=True) for p in article_content])

    return title, article_text

# Fonction pour sauvegarder l'article dans un fichier texte
def save_to_file(title, article_text):
    try:
        with open('text.txt', 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n{article_text}")
        print("\nArticle sauvegardé dans 'text.txt'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

# Fonction principale
def main():
    url = input("Entrez le lien de l'article CNN : ").strip()
    
    # Validation de l'entrée utilisateur
    if not url:
        print("Erreur : Aucun lien fourni. Veuillez entrer une URL valide.")
        sys.exit(1)
    if not url.startswith("http"):
        print("Erreur : L'URL doit commencer par 'http' ou 'https'.")
        sys.exit(1)
    
    html_content = get_html_content(url)
    if html_content:
        title, article_text = parse_article(html_content)
        print(f"\nTitre : {title}\n")
        print(article_text)
        save_to_file(title, article_text)

# Exécution du script
if __name__ == "__main__":
    main()
