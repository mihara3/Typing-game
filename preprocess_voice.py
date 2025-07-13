import os
import subprocess

# 出力ディレクトリ
os.makedirs("voice", exist_ok=True)

# 読み込む問題一覧（JSONと同じ内容を使う）
from question_loader import load_questions
words = load_questions("/home/s1310064/Typing-game/words.json")

# 一括生成
for word in words:
    outfile = f"/home/s1310064/Typing-game/voice/{word}.wav"
    if os.path.exists(outfile):
        continue  # 既にある場合はスキップ

    print(f"音声生成中: {word}")
    subprocess.run([
        "open_jtalk",
        "-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic",
        "-m", "/usr/share/hts-voice/mei/mei_normal.htsvoice",
        "-ow", outfile
    ], input=word.encode("utf-8"))
