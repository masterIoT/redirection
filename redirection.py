from flask import Flask, redirect, request
import requests

app = Flask(__name__)

# Adresse de l'application principale et du site de maintenance
MAIN_APP_URL = "http://host.docker.internal:8080"
MAINTENANCE_URL = "http://host.docker.internal:5002"

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
    app.run(host="0.0.0.0", port=5003)
