---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---

# クラス

---
## オブジェクトとクラス

### オブジェクト（指向）とは
+ データと処理をひとまとめにしておこうという発想
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**
+ 仕組みを提供しているのが**クラス**

### クラスがオブジェクトを提供する仕組み
- [文字列クラス](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/collections/__init__.py#L1299)のソースコードを見てみましょう
- さっき `dir()` 関数で確認したメソッドの定義がある
- 文字列クラスが文字列オブジェクトを作る時このクラスが実行されている。
    1.  `s = "shinseitaro"` と pythonで実行すると、
    1. [文字列クラス](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/collections/__init__.py#L1299)に "shinseitaro"という文字列が渡される
    1. ⇑で定義されている全てのメソッドを持った状態のオブジェクトを生成して変数`s` に格納

---
### クラスからオブジェクト（インスタンス）を作る
- つまり、クラスはデータを引き取ってメソッドをくっつけてオブジェクトを返す（データの引き取りが無い場合もある）
+ そういう意味でクラスは雛形（設計図）と呼ばれたりする。
+ クラスからオブジェクトを作ることを、**実体化（インスタンス化）** という。
+ 実体化したものをインスタンスオブジェクトと呼ぶ
    + 参照：[オブジェクト指向とクラス — Pythonオンライン学習サービス PyQ](https://docs.pyq.jp/python/library/class.html#id6)

---
### 組み込みクラスのインスタンス化
+ Pythonには、最初から組み込みでクラスがたくさんある
- モジュール（定義されているファイル）をインポートして使う
#### import 文の書き方
- 明示的に呼び出すには、**import 文**を書く    
- 呼び出し方は、以下2通り
    1. クラスが定義されているモジュール(ファイル)全体をインポート
        ```python 
        import モジュール
        c = モジュール.使いたいクラス()
        ```
    1. 使いたいクラスだけインポート
        ```python
        from モジュール import 使いたいクラス
        c = 使いたいクラス()
        ```

---
+ 例：十進固定及び浮動小数点数の算術演算のためのモジュール decimal の中にある `Decimal` クラスのインポート
    1. 1の方法
        ```python 
        import decimal 
        d = decimal.Decimal(10)
        ```
    1. 2の方法
        ```python 
        from decimal import Decimal 
        d = Decimal(10)
        ```
    - `d` はインスタンスオブジェクト。dir関数で属性（データやメソッド）を確認できる
        ```python
        >>> dir(d)
        ['__abs__', '__add__', ...,
        'adjusted', 'as_integer_ratio', 'as_tuple', 'canonical',...,
        'max', 'max_mag', 'min', 'min_mag', ...,
        'shift', 'sqrt', 'to_eng_string', 'to_integral', 
        'to_integral_exact', 'to_integral_value']

        >>> d.sqrt() # dの平方根を出すメソッド .sqrt()を呼び出す
        Decimal('3.162277660168379331998893544')
        ```
---

## クラスを作る
- クラスを自作すると、どういう型のデータを持つか、そのデータにどういう処理をするかを定義出来る
- 開発者は、自分が扱うデータに対する処理を定義しておけば、何度も同じコードを書く必要がなくなる
- 何のためのクラスを作るのか？
    - 同じようなコードを繰り返し書くことを防ぐため
    - **Don't Repeat Yourself (DRY)** というPythonの哲学
--- 
### クラスを定義する

- [6-3. クラス](https://utokyo-ipp.github.io/6/6-3.html#%E3%82%AF%E3%83%A9%E3%82%B9%E5%AE%9A%E7%BE%A9)
- 基本文法
    ```python
    class クラス名: # クラス名
        def __init__(self,  引数, ...): # 初期値を設定する特別なメソッド
            実行文
        def メソッド名１(self, 引数, ...): # そのクラスに属するメソッド
            実行文
        def メソッド名２(self, 引数, ...):
            実行文
    ```
+ お作法としてクラス名は**大文字**で始める
- メソッドの第一引数は `self` 
    - `self` は クラス自分自身 ⇐ :question: :thinking: :pleading_face: ですよね

---

```python
class Hello:
    def __init__(self, name, address):
        self.name = name # selfの属性として name を登録
        self.address = address

    def say(self):
        return "Hello " + self.name

    def home(self):
        return "your address is " + self.address
```
- `__init__` メソッドの第一引数も必ず `self` 
- 初期値は `__init__` メソッドを作ってその中に定義
- 第二引数以降、いくつでも引数を追加出来る
- 第二引数に追加した引数は、インスタンス化のタイミングで**必ず渡すデータ**
- 取得した初期値は、`__init__ ` メソッド内で **selfの属性として登録**
- 他のメソッドで、`self` を通じて使えるデータになる
---
- インスタンス化する時に初期値を渡さないとエラー
    ```python
    h = Hello()
    print(h.say())
    ```
    ```bash
    python src/hoge.py

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: __init__() missing 2 required positional arguments: 'name' and 'address'
    ```
- 初期値を渡してインスタンス化
    ```python
    h = Hello("Taro", "Tokyo")
    print(h.say())
    ```
    ```bash
    python src/hoge.py 
    
    Hello Taro
    ```
