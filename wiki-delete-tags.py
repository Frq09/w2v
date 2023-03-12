import re

# 空のHTMLタグを削除する
with open('wiki.txt', 'r+', encoding='utf-8') as file:
    content = file.read()
    new_content = re.sub(r'^<[^>]*>$', '', content, flags=re.MULTILINE)
    file.seek(0)
    file.write(new_content)
    file.truncate()

# 空行を削除する
with open('wiki.txt', 'r+', encoding='utf-8') as file:
    content = file.read()
    new_content = re.sub(r'^\n', '', content, flags=re.MULTILINE)
    file.seek(0)
    file.write(new_content)
    file.truncate()