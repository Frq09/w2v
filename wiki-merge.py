import os

# フォルダ内のファイルを再帰的に検索
for root, dirs, files in os.walk("text/"):
    for file in files:
        # ファイル名に「wiki」という文字列が含まれるか確認
        if "wiki" in file:
            # ファイルを開いて、内容を`wiki.txt`に追記
            with open(os.path.join(root, file), "r", encoding='utf-8') as f:
                with open("wiki.txt", "a", encoding='utf-8') as wf:
                    wf.write(f.read())
