from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # CSVを読み込む（ヘッダーなし）
        df = pd.read_csv('results.csv', header=None)

        # 列名を設定
        df.columns = ["date", "accuracy", "time"]

        # 並べ替え（正答率降順、時間昇順）
        df = df.sort_values(by=["accuracy", "time"], ascending=[False, True])

        # 最新の行（最後に追加されたスコア）
        latest_row = df.tail(1).iloc[0]

        # テンプレートに渡すために辞書化
        results = df.to_dict(orient='records')
        latest = latest_row.to_dict()

    except Exception as e:
        return f"エラーが発生しました: {e}"

    return render_template('ranking.html', results=results, latest=latest)

if __name__ == '__main__':
    app.run()
