from wordcloud import WordCloud
import matplotlib.pyplot as plt

#font_path = "DroidSansMono.ttf"  # フォントのパス
#font_path= '/Library/Fonts//Arial Unicode.ttf'
font_path = 'examples/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'
your_text_here = "i am super man"  # ワードクラウドを生成するテキスト

# ワードクラウドを生成
wc = WordCloud(font_path=font_path, background_color='white').generate(your_text_here)

# プロットして表示
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
