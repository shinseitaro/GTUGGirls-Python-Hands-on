---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---

# 名前空間

- [3-3. 関数 変数とスコープ](https://utokyo-ipp.github.io/3/3-3.html#%E5%A4%89%E6%95%B0%E3%81%A8%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97)
- ここでスコープにすこし触れられているが、全く足りないので追加します

## 名前空間（ネームスペース）
- 変数、関数、クラスなどが定義されている場所のこと。

## スコープ
- 変数、関数、クラスなどが有効な範囲

---
## スコープ
![bg right:60%](https://i.imgur.com/xOdTeLq.jpg)

##### ビルドインスコープ
+ `+`、 `>` 、 `def` `type()` `max()` などいきなり使える python のコードが所属
##### モジュールスコープ
+ `.py`ファイルに書く変数や関数やクラスが所属
+ トップレベル(グローバル)とも呼ぶ

##### ローカルスコープ
+ ファイル記述された関数やクラスの「内部」のみが所属

---
#### 意識してローカルスコープを使おう
+ 図の例でいえば、`func` 関数の中の 引数 `a` などは、**func 関数のなかでしか使えない**
+ もし、別の関数やクラスで同じ名前の引数を使っていてもローカルスコープだけで有効なので、コンフリクトしない
+ これがもっとも安全（＝エラー処理が楽）な方法

---
#### モジュール間のスコープ
- モジュール(`.py`ファイル)が違えばスコープは違う
- 違うモジュールに定義した関数やクラスはどうやって使う？
##### 同じ階層に定義している場合
- 例：srcディレクトリ配下に設置した hoge.py の関数を moge.py で呼び出す
    ```bash
    └── src
        ├── hoge.py
        ├── moge.py
    ```
    ```python
    # hoge.py
    def callme(name):
        return f"Hello {name}"
    ```
    ```python
    # moge.py
    import moge 
    print(moge.callme("shinseitaro"))
    ```
---
##### 違う階層に定義している場合１
- 例：`src/child` 配下に設置した huga.py の関数を moge.py で呼び出す
    ```bash
    └── src
        ├── child
        │   └── huga.py
        ├── hoge.py
        ├── moge.py
    ```    
    ```python
    # src/child/huga.py
    def ringmeup(name):
        return f"Hello {name}"    
    ```
---
##### 違う階層に定義している場合２
- 例： hoge.py で定義した関数を `src/child/huge.py` で呼び出す
- かなりトリッキー
- huga.py から見たら、hoge.py は 2階層上の src の配下にある
- この src を 一時的にPATHに入れるという方法をとります
- `__file__` は組み込み属性と呼ばれる特別なアトリビュートで当該ファイルパスを返す
    ```python 
    # src/child/huge.py
    import sys
    import os

    # src/child/huge.pyの dirname の dirname を返すから rootdir は "src"
    rootdir = os.path.dirname(os.path.dirname(__file__))
    # "src" を一時的にPATHに入れる
    sys.path.append(rootdir)
    # よって、src に入っている hoge を import することができる
    import hoge
    print(hoge.callme("ﾌｶﾞﾌｶﾞ"))
    ```

---
(あとで考える。時間次第ではやらない)
## 演習

- 1. 作業ディレクトリ配下に以下の構成でファイルを作成してください
    ```bash
    └── src
        ├── hoge.py
        ├── moge.py
        └── test.py
    ```
---
- 2. `src/hoge.py` に以下を定義
    ```python
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
    ```
---
- 3. 