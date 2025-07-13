import pandas as pd

def generate_html(csv_path, output_path):
    df = pd.read_csv(csv_path)
    html = df.to_html(index=False, justify="center", border=1)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("""
        <html>
        <head>
            <meta charset="utf-8">
            <title>タイピングランキング</title>
            <style>
                body { font-family: sans-serif; text-align: center; }
                table { margin: auto; border-collapse: collapse; }
                th, td { padding: 8px; border: 1px solid #999; }
                th { background-color: #f0f0f0; }
            </style>
        </head>
        <body>
            <h1>タイピングランキング</h1>
            %s
        </body>
        </html>
        """ % html)
