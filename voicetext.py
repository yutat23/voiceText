import os
from moviepy.editor import VideoFileClip
import whisper
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py video_filename")
    sys.exit(1)

video_path = sys.argv[1]

output_audio_path = "temp_audio.mp3"

# Extract audio from the video
video = VideoFileClip(video_path)
video.audio.write_audiofile(output_audio_path)

# Load the Whisper ASR model
model = whisper.load_model("small")

# Transcribe the extracted audio
result = model.transcribe(output_audio_path)
print(result["text"])

# Remove the temporary audio file
os.remove(output_audio_path)
