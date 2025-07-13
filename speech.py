#import subprocess

#def speak(text):
#    subprocess.run([
#        "open_jtalk",
#        "-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic",
#        "-m", "/usr/share/hts-voice/mei/mei_normal.htsvoice",
#        "-ow", "/tmp/voice.wav"
#    ], input=text.encode("utf-8"))
#    subprocess.run(["aplay", "/tmp/voice.wav"])

import subprocess
import os

def speak(word):
    filepath = f"/home/s1310064/Typing-game/voice/{word}.wav"
    if not os.path.exists(filepath):
        print(f"[警告] 音声ファイルが存在しません: {filepath}")
        return
    subprocess.run(["aplay", filepath])
