import MeCab as mc
from wordcloud import WordCloud
import os
import re
import matplotlib
matplotlib.use('Agg')  # フォント関連のエラーを回避するための設定


def strip_CRLF_from_Text(text):
    """テキストファイルの改行，タブを削除し，形態素解析を実行する．
    改行前後が日本語文字の場合は改行を削除する．
    それ以外はスペースに置換する．
    """
    # 改行前後の文字が日本語文字の場合は改行を削除する
    plaintext = re.sub('([ぁ-んー]+|[ァ-ンー]+|[\\u4e00-\\u9FFF]+|[ぁ-んァ-ンー\\u4e00-\\u9FFF]+)(\n)([ぁ-んー]+|[ァ-ンー]+|[\\u4e00-\\u9FFF]+|[ぁ-んァ-ンー\\u4e00-\\u9FFF]+)',
                       r'\1\3',
                       text)
    # 残った改行とタブ記号はスペースに置換する
    plaintext = plaintext.replace('\n', ' ').replace('\t', ' ')
    return plaintext

def mecab_wakati(text):
    t = mc.Tagger()

    node = t.parseToNode(text)
#     print(node)
    sent = ""
    while(node):
#         print(node.surface, node.feature)
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            # 名詞だけをリストに追加する
            if word_type in ["名詞"]:
                 sent += node.surface + " "  # node.surface は「表層形」
            # 動詞（の原型），形容詞，副詞もリストに加えたい場合は次の２行を有効にする
            if word_type in [ "動詞", "形容詞","副詞"]:
                sent += node.feature.split(",")[6] + " " # node.feature.split(",")[6] は形態素解析結果の「原型」
        node = node.next
        if node is None:
            break
    return sent

# テキストファイル読み込み
f = open(os.path.sep.join(['es_text.txt']), encoding='utf-8')
raw = f.read()
f.close()
#print(raw)
text = strip_CRLF_from_Text(raw)
#print(text)
sent = mecab_wakati(text)
print(sent)
stop_words = ['ある','する','こと','とても','いる','できる','よう','思う','ため','なる','それ','私','自分','れる','られる','の','たち','考える']


# フォントの保存先を指定する（環境によって書き換えてください）
#font_path = "C:\\WINDOWS\\FONTS\\MEIRYO.TTC"    ## Windows 版はこちら
font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"

wc = WordCloud(
    font_path=font_path,
    width=900, height=600,   # default width=400, height=200
    background_color="white",   # default=”black”
    stopwords=set(stop_words),
    max_words=500,   # default=200
    min_font_size=4,   #default=4
    collocations = False   #default = True
    ).generate(sent)
wc.to_file("test.png")
# WordCloud画像を生成する
#wc.to_file("wc-5.png")
