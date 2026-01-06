import requests
import os

START = 1
END = 16

VIDEO_URL = "https://storage.googleapis.com/finger-interactive/trending/{}.mp4"
THUMB_URL = "https://storage.googleapis.com/finger-interactive/trending/thumb/{}.webp"

# thư mục lưu ảnh
os.makedirs("thumb", exist_ok=True)

for i in range(START, END + 1):

    # ---------- VIDEO ----------
    video_url = VIDEO_URL.format(i)
    video_name = f"{i}.mp4"

    print(f"Downloading video: {video_url} -> {video_name}")
    rv = requests.get(video_url, stream=True)

    if rv.status_code == 200:
        with open(video_name, "wb") as f:
            for chunk in rv.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✔ Saved video: {video_name}")
    else:
        print(f"✘ Failed video ({rv.status_code})")

    # ---------- THUMB ----------
    thumb_url = THUMB_URL.format(i)
    thumb_name = f"thumb/{i}.webp"

    print(f"Downloading thumb: {thumb_url} -> {thumb_name}")
    rt = requests.get(thumb_url, stream=True)

    if rt.status_code == 200:
        with open(thumb_name, "wb") as f:
            for chunk in rt.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✔ Saved thumb: {thumb_name}")
    else:
        print(f"✘ Failed thumb ({rt.status_code})")

print("DONE!")
