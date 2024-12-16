# Utiliser une image de base Python
FROM python:3.10-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip à la dernière version
RUN pip install --upgrade pip

# Créer un répertoire de travail
WORKDIR /

# Copier les fichiers du projet
COPY . /

# Installer les dépendances Python depuis requirements.txt
RUN pip install flask requests

# Exposer le port utilisé par le serveur
EXPOSE 80

# Définir la commande de lancement
CMD ["python", "redirection.py"]
