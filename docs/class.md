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
+ データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ
+ データにメソッドがブラブラぶら下がる
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**
+ 仕組みを提供しているのが**クラス**

---
### クラスからオブジェクト（インスタンス）を作る
+ 設計図（型）であるクラスは、そのままでは使えない
+ かならず、**実体化（インスタンス化）** する必要がある
+ 実体化したものをインスタンスオブジェクトと呼ぶ
    + 参照：[オブジェクト指向とクラス — Pythonオンライン学習サービス PyQ](https://docs.pyq.jp/python/library/class.html#id6)

---
#### 組み込みクラスのインスタンス化
+ Pythonには、最初から組み込みでクラスがたくさん用意されている
- 組み込みクラス
    - 明示的に呼び出さなくても使える組み込みクラス: [文字列クラス](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/collections/__init__.py#L1299), [整数型クラス](https://github.com/python/cpython/blob/4aa63d65a9971d14f1a2131b989dca0dab514a9d/Lib/numbers.py#L12)...
        ```python
        s = "shinseitaro"
        i = 1000
        ```
    - クラスが定義されているモジュールを明示的に呼び出して( **import** する)使う組み込みクラス: [datetime](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/datetime.py#L1563), [Decimal](https://github.com/python/cpython/blob/3527569f1cd0df697242b68a8a837f08904872fe/Lib/_pydecimal.py#L513), .... たくさん
---

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
    - この変数 `c` を`インスタンスオブジェクト`と呼ぶ

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
        def メソッド名１(self, 引数, ...): # そのクラスに属するメソッド
            実行文
        def メソッド名２(self, 引数, ...):
            実行文
    ```
+ お作法としてクラス名は**大文字**で始める
- メソッドの第一引数は `self` 
    - `self` は クラス自分自身 ⇐ :question: :thinking: :pleading_face: ですよね

---
例：
```python
class HelloForEver:
    def readline(self):
        return 'Hello.\n'
    def readline_v2(self, name):
        return 'Hello ' + name + ' .\n'
```

---
- インスタンス化
    ```python
    >>> f = HelloForEver()
    >>> dir(f)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
    '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
    'readline', 'readline_v2']
    ```
    - 定義した `'readline', 'readline_v2'` が入っているのが確認できる
- メソッド呼び出し
    ```python
    # readline を呼び出し
    >>> f.readline()
    'Hello.\n'

    # readline_v2 を呼び出し
    >>> f.readline_v2("taro")
    'Hello taro .\n'
    ```
    - `self` は、`.` で自分自身のメソッドにアクセスする仕組みのために定義
    - インスタンス化した時に、クラスに定義されたメソッドは自分自身を第一引数に取得する仕組みになっている
---
- 試しに self 無しで定義してインスタンス化してみるとわかりやすい
    ```python
    >>> class HelloForEver:
    ...     def readline():
    ...         return 'Hello.\n'
    ...     def readline_v2(name):
    ...         return 'Hello ' + name + ' .\n'
    ... 
    >>> c = HelloForEver()
    >>> c.readline()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: readline() takes 0 positional arguments but 1 was given
    >>> 
    ```
    - インスタンス化された時に自分自身を引数にとる仕組みがあるので、`readline() は 引数を0個とるハズなのに１与えられたので例外です` というエラーメッセージを出す
---
## 初期化と属性

- [6-3. クラス](https://utokyo-ipp.github.io/6/6-3.html#%E5%88%9D%E6%9C%9F%E5%8C%96%E3%81%A8%E5%B1%9E%E6%80%A7)
- クラスをインスタンス化する時に渡したい初期値の定義
- 初期値は `__init__` メソッド内に定義
- 通常クラスを作る時は、`__init__` メソッドを定義する。
- `__init__` が無いクラスはほとんど見かけない

---

```python
class HelloFile:
    def __init__(self, n):
        self.n = n # selfの属性として n を登録
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return 'Hello.\n'
```
- `__init__ ` 関数の第一引数も必ず `self` 
- 第二引数以降、いくつでも引数を追加出来る
- 第二引数に追加した引数は、インスタンス化のタイミングで**必ず渡す引数**になる
- `self.n` でselfの属性として n を登録しているので、このクラスに定義されている他のメソッドで `self.n` を利用できる
---

（教材の例が分かりづらかったので、書き直してみた）

```python
class Hello:
    def __init__(self, name):
        self.name = name # selfの属性として name を登録
    def say(self):
        if type(self.name) == str:
            return f'Hello, {self.name}!!'
        return 'Hello!!'
```
- 初期値として `name` を要求
- メソッド `say` 
    - もし`self.name` が文字列なら返り値 `Hello <名前> !!`
    - そうでなければ 返り値 `Hello!!`
---
```python
# インスタンス化する時に初期値を渡さないとエラー
>>> h = Hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'name'

# インスタンス化成功
>>> h = Hello("Taro")
```

```python
# メソッド呼び出し
>>> h.say()
'Hello, Taro!!'
```
```python
# 数値を初期値にしてインスタンス化
>>> h = Hello(123)
# メソッド呼び出し
>>> h.say()
'Hello!!'
```
