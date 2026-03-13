import requests
import pandas as pd

# URL pública de tu hoja (la de "Publicar en la web")
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQz9qplNu-EFCzgi_2nqd6fYGZGZcxMCmCiEBItg8E1Jmx7EpAK8PtYRTZIGXjG225QLkwF8104TQCi/pub?gid=0&single=true&output=csv"

response = requests.get(url)
response.encoding = 'utf-8'

# Si quieres guardar como CSV directamente
with open("datos.csv", "w", encoding="utf-8") as f:
    f.write(response.text)

# Opcional: convertir a JSON
df = pd.read_csv(pd.compat.StringIO(response.text))
df.to_json("datos.json", orient="records", indent=2, force_ascii=False)
