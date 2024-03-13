import os
from moviepy.editor import VideoFileClip
import whisper

# Set the paths
base_dir = ""

video_folder = base_dir
video_filename = ""  # Replace with your actual video file name
video_path = os.path.join(video_folder, video_filename)

audio_folder = base_dir
output_audio_path = os.path.join(audio_folder, "temp_audio.mp3")

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

