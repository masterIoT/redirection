from flask import Flask, redirect, request
import requests
import socket 
import os

app = Flask(__name__)

# Récupérer l'adresse IP de l'hôte depuis une variable d'environnement
ip_address = os.getenv("HOST_IP", "127.0.0.1")

# Adresse de l'application principale et du site de maintenance
MAIN_APP_URL = f"http://{ip_address}:8080"  # Utiliser l'adresse IP récupérée
MAINTENANCE_URL = f"http://{ip_address}:5002"  # Utiliser l'adresse IP récupérée

def is_main_app_available():
    """Teste si l'application principale est disponible."""
    try:
        response = requests.get(MAIN_APP_URL, timeout=1)
        if response.status_code == 200 or response.status_code == 302:
            return True
    except requests.ConnectionError:
        return False

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_user(path):
    """Redirige les utilisateurs vers l'application principale ou le site de maintenance."""
    if is_main_app_available():
        # Si l'application principale est disponible, rediriger vers elle
        return redirect(f"{MAIN_APP_URL}/{path}")
    else:
        # Sinon, rediriger vers le site de maintenance
        return redirect(f"{MAINTENANCE_URL}/{path}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
