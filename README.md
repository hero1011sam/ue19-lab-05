# UE19-lab-05 
## Joke App

Petite application Python 3 qui utilise la librairie
[requests](https://docs.python-requests.org/en/latest/index.html) pour interroger
l'API publique [Official Joke API](https://official-joke-api.appspot.com/random_joke)
et afficher une blague aléatoire (en anglais).

## Fichiers

- `app.py` : le programme qui interroge l'API
- `requirements.txt` : dépendances (requests)
- `Dockerfile` : création de l'image du conteneur

## Installation et lancement

```bash
pip install -r requirements.txt
python app.py
```

## Avec Docker

```bash
docker build -t joke-app .
docker run --rm joke-app
```

## Exemple de sortie

```
What do you call a bear with no teeth?
A gummy bear.
```
