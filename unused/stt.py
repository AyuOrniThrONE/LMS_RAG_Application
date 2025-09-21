import whisper

model = whisper.load_model("large-v2")
result = model.transcribe(audio= "audioes/sample.mp3", language = "hi", task="translate", word_timestamps=false)


chunks=[]
for segments in result["segments"]:
    chunks.append([start=segments["start"], end=segments["end"], text=segments["text"]])
print(chunks)