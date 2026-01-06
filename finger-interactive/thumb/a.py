import requests

START = 1
END = 44

BASE_URL = "https://storage.googleapis.com/finger-interactive/finger_interactive/thumb/{}.webp"

for i in range(START, END + 1):
    url = BASE_URL.format(i)
    filename = f"{i}.webp"

    print(f"Downloading {url} -> {filename}")

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✔ Saved: {filename}")
    else:
        print(f"✘ Failed ({r.status_code}) for {url}")
