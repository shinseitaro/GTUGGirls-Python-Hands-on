
A = 1
B = 1

# ファイルに定義される関数やクラスは、モジュールスコープに属する
def func(a, b):
    # + などの関数はPythonの中ならどこでも使えるビルドインスコープに属しているので
    # ここですぐに使うことが出来る
    x = a + b 
    return x 

class BookMark:
    def __init__(self, title, url, author):
        self.title = title 
        self.url = url 
        self.author = author 

    def get_title(self):
        return self.title

class SongList:
    def __init__(self, title, url, artist):
        self.title = title 
        self.url = url 
        self.artist = artist 

    def get_title(self):
        return self.title.upper()


