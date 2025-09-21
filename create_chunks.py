import whisper
import os
import json

model = whisper.load_model("large-v2")
audioes = os.listdir("audioes")

for audio in audioes:
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number,title)
        result = model.transribe(audio = "audioes/sample.mp3", language = "hi", task="translate", word_timestamps=false)
        # result = model.transribe(audio = f"audioes/{audio}", language = "hi", task="translate", word_timestamps=false)
        chunks=[]
        for segments in result["segments"]:
            chunks.append({"number" : number, "title" : title,"start":segments["start"], "end":segments["end"], "text":segments["text"]})
        chunks_with_metadata = {"chunks":chunks,"text":result["text"]}

        with open(f"json/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata,f)