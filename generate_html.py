#import pandas as pd

#def generate_html(csv_path, output_path):
#    df = pd.read_csv(csv_path)
#    html = df.to_html(index=False, justify="center", border=1)

#    with open(output_path, "w", encoding="utf-8") as f:
 #       f.write("""
 #       <html>
#        <head>
#            <meta charset="utf-8">
#            <title>タイピングランキング</title>
#            <style>
#                body { font-family: sans-serif; text-align: center; }
#                table { margin: auto; border-collapse: collapse; }
#                th, td { padding: 8px; border: 1px solid #999; }
#                th { background-color: #f0f0f0; }
#            </style>
#        </head>
#        <body>
#            <h1>タイピングランキング</h1>
#            %s
#        </body>
#        </html>
#        """ % html)

#import pandas as pd

#def generate_html(csv_path, output_path):
#    df = pd.read_csv(csv_path)

 #   with open(output_path, "w", encoding="utf-8") as f:
#        f.write("""
#        <html>
#        <head>
#            <meta charset="utf-8">
#            <title>タイピング ランキング</title>
#            <style>
#                body { font-family: sans-serif; background: #f4f4f4; padding: 2em; }
#                table { border-collapse: collapse; width: 80%; margin: auto; background: #fff; }
#                th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
#                th { background: #e0e0e0; }
#                h1 { text-align: center; }
#            </style>
#        </head>
#        <body>
#            <h1>タイピング ランキング</h1>
#            <table>
#                <tr><th>日時</th><th>正答率（%）</th><th>時間（秒）</th></tr>
#                """)
#
#                # 各行をHTMLテーブルのtr/tdで書き出し
#        for _, row in df.iterrows():
#            f.write(f"        <tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n")
#
#        f.write("""
#            </table>
#        </body>
#        </html>
#        """)



import pandas as pd

def generate_html(csv_path, output_path):
    # ヘッダーなしのCSVを読み込む（列番号で読み込まれる）
    df = pd.read_csv(csv_path, header=None)

    # 列名を明示的に指定（順番に注意）
    df.columns = ["日時", "正答率", "時間"]

    # 最新スコア（最後の行）
    latest_row = df.tail(1).iloc[0]

    # 並べ替え（正答率は降順、時間は昇順）
    df = df.sort_values(by=["正答率", "時間"], ascending=[False, True])

    # HTML出力
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("""
<html>
<head>
    <meta charset="utf-8">
    <title>タイピング ランキング</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; padding: 2em; }
        table { border-collapse: collapse; width: 80%; margin: auto; background: #fff; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
        th { background: #e0e0e0; }
        h1 { text-align: center; }
        .highlight { background-color: #ffffcc; }
    </style>
</head>
<body>
    <h1>タイピング ランキング</h1>
    <table>
        <tr><th>順位</th><th>日時</th><th>正答率（%）</th><th>時間（秒）</th></tr>
""")

        for i, (_, row) in enumerate(df.iterrows(), start=1):
            is_latest = (
                row["日時"] == latest_row["日時"] and
                row["正答率"] == latest_row["正答率"] and
                row["時間"] == latest_row["時間"]
            )
            highlight_class = ' class="highlight"' if is_latest else ''
            f.write(f'  <tr{highlight_class}><td>{i}</td><td>{row["日時"]}</td><td>{row["正答率"]}</td><td>{row["時間"]}</td></tr>\n')

        f.write("""
    </table>
</body>
</html>
""")
