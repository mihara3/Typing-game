import json

def load_questions(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # JSONがオブジェクト（辞書）形式だった場合は、キーだけ取り出す
        if isinstance(data, dict):
            return list(data.keys())
        elif isinstance(data, list):
            return data
        else:
            raise ValueError("不明なJSONフォーマットです")

    except FileNotFoundError:
        print(f"[ERROR] ファイルが見つかりません: {json_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSONの読み込みに失敗しました: {e}")
        return []
