import hoge
from yarl import URL

# このファイルにも同名のクラスを作ってみる
class BookMark:
    def __init__(self, url):
        self.url = url 
    def get_parent(self):
        return URL(self.url).parent
    def get_human_readable(self):
        return URL(self.url).human_repr()


# hoge モジュールからインポートした定数やクラス、メソッドの呼び出し
print(hoge.A)

b1 = hoge.BookMark("ノルウェイの森", "https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A4%E3%81%AE%E6%A3%AE", "村上春樹")
s1 = hoge.SongList("Norwegian Wood", "https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%BC%E3%81%AE%E6%A3%AE", "Beatles, The")

print(b1.get_title())
print(s1.get_title())

# このファイルで定義したクラスの呼び出し
b2 = BookMark("https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A4%E3%81%AE%E6%A3%AE")
print(b2.get_human_readable())




