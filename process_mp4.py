#Convert Videos into Mp3
import os
import subprocess

files=os.listdir("videos")

for file in files:
    v_num=file.split(".")[0].split("-")[0].split("_")[1]
    file_name=file.split("-")[1].split(".")[0]
    print(f"{v_num} {file_name}")
    subprocess.run(["ffmpeg", "-i", f"videos/{file}",f"audioes/{v_num}_{file_name}.mp3"])