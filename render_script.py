
# Fonction pour maintenir les projets render disponible à tout moment.
import requests
import schedule
import time

render_links = [
    "https://chatbot-tdn.onrender.com/", "https://danymeteo.onrender.com/Meteo/",
]

def reload(urls):
    results = {}
    for url in urls:
        try:
            res = requests.get(url, timeout=10) 
            results[url] = res.status_code == 200
            print(f"Ping réussi pour {url}. Statut: {res.status_code}")
        except requests.RequestException as e:
            results[url] = False
            print(f"Échec du ping pour {url}. Erreur: {e}")
    return results


# Appel récurant de la fonction reload
schedule.every(10).minutes.do(reload, urls = render_links)

while True:
    schedule.run_pending() #Vérification et exécution de tâche.
    time.sleep(1)