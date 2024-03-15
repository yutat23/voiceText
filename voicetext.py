### 動画ファイルから音声を抽出し、音声認識を行い、テキストファイルに保存するスクリプト
### options: -o output_filename で出力ファイル名を指定可能
import os
from moviepy.editor import VideoFileClip
import whisper
import sys

# 処理時間を記録する
import time
start = time.time()

if len(sys.argv) < 2:
    print("Usage: python script.py video_filename [-o output_filename]")
    sys.exit(1)

video_path = sys.argv[1]

# oオプションをチェックする
output_file = None
if "-o" in sys.argv:
    output_index = sys.argv.index("-o") + 1
    if output_index < len(sys.argv):
        output_file = sys.argv[output_index]

output_audio_path = "temp_audio.mp3"

# ビデオから音声を抽出する
video = VideoFileClip(video_path)
video.audio.write_audiofile(output_audio_path)

# モデルの読み込み
model = whisper.load_model("small")

# モデルによる音声認識実行
# それなりに時間がかかる
result = model.transcribe(output_audio_path)

# 句点で改行による分割
genereatedText = result["text"].replace("。", "。\n")

# テキストファイルに保存する
if output_file:
    with open(output_file, 'w') as file:
        file.write(genereatedText)

print(genereatedText)

# 処理完了 処理時間を表示する
print("Transcription complete")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# 一時音声ファイルを削除する
os.remove(output_audio_path)
