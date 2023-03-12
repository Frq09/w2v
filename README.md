# Word2Vecの学習

word2vecの学習のためのプログラムを作成・公開いたしました。

# Requirement

筆者の当時の実行環境は以下の通りです。

* Python 3.6.9
* CPU　Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz   2.80 GHz
* GPU　NVIDIA Geforce RTX 3070
* メモリ　32GB

# Usage

私のはてなブログにて詳しく説明しておりますが、ここでも一通り説明いたします。

### ・日本語wikipediaコーパスのダウンロード
~~~
curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o jawiki-latest-pages-articles.xml.bz2
~~~

### ・WikiExtractorのインストール
~~~
pip install wikiextractor
~~~

### ・WikiExtractorの実行
~~~
python -m wikiextractor.WikiExtractor jawiki-latest-pages-articles.xml.bz2
~~~

### ・ファイルの統合
~~~
python merge.py
~~~

### ・テキストクリーニング
~~~
python wiki-delete-tags.py
~~~

### ・学習（train-word2vec.ipynb）
~~~
from gensim.models import word2vec
import MeCab
import re
import logging
from tqdm import tqdm
from multiprocessing import Pool

with open("wiki.txt", "r", encoding='utf-8') as f:
    text = f.read()

sentences = []
for s in tqdm(re.split("[\n。]", text)):
    s = s.strip()
    if s:
        sentences.append(s + "。")

sentences = list(filter(None, sentences))
print(len(sentences))

def tokenize(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text).strip().split()

def tokenize_list(text_list):
    with Pool() as pool:
        results = list(tqdm(pool.imap(tokenize, text_list), total=len(text_list)))
    return results

w2v_train_data = tokenize_list(sentences)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = Word2Vec(w2v_train_data, size=200, window=5, sample=1e-3, negative=5, hs=0)
model.save("word2vec.model")
~~~

# Note

質問があれば、私のメールアドレスまでご連絡お願いします。

Git初学者のため何かとお見苦しい部分はあるとは思いますが、何卒ご容赦ください。

# Auther

* 作成者：Frq09
* E-mail：drs0928jp@outlook.com

# License

MIT License
