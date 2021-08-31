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
+ データと命令を一つにしておこうという発想
+ データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ
+ データにメソッドがブラブラぶら下がる
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**
+ 仕組みを提供しているのが**クラス**
+ 同じような性質を持ったオブジェクトをまとめてクラスという仕組みに突っ込んでおけば、楽だよね？！っていう考え

---
### あとでやる（実際のソースコードへのリンク。number sys os time とか）
+ Pythonには、最初から組み込みでクラスがたくさん用意されている
    + 例：文字列クラス https://docs.python.org/ja/3/library/stdtypes.html#str
        + 文字列クラス
        + 文字列メソッド
        + ソースコードは多分[これ](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/collections/__init__.py#L1299)
    
---

### クラスからオブジェクト（インスタンス）を作る
+ 設計図（型）であるクラスは、そのままでは使えない
+ かならず、**実体化（インスタンス化）** する必要がある
+ このインスタンスもオブジェクト
    + 参照：[オブジェクト指向とクラス — Pythonオンライン学習サービス PyQ（パイキュー）ドキュメント](https://docs.pyq.jp/python/library/class.html#id6)

---    
#### 組み込みクラスのインスタンス化
1. クラス全体をインポート
    ```python 
    import 組み込みクラス名
    c = 組み込みクラス名.使いたいクラス()
    ```
1. 使いたいクラスだけインポート
    ```python
    from 組み込みクラス名 import 使いたいクラス
    c = 使いたいクラス()
    ```
    この変数 `c` をインスタンスと呼ぶ

---
+ 例：
    ```python 
    import decimal
    d = decimal.Decimal(10)
    ```
    もしくは
    ```python 
    from decimal import Decimal 
    d = Decimal(10)
    ```
    ```python
    # d はインスタンスオブジェクト。データとメソッドを持つ
    >>> dir(d)
    ['__abs__', '__add__', ...,
    'adjusted', 'as_integer_ratio', 'as_tuple', 'canonical',...,
    'max', 'max_mag', 'min', 'min_mag', ...,
    'shift', 'sqrt', 'to_eng_string', 'to_integral', 
    'to_integral_exact', 'to_integral_value']
    ```
---

## クラスを作る

- [6-3. クラス — Pythonプログラミング入門 documentation](https://utokyo-ipp.github.io/6/6-3.html#%E3%82%AF%E3%83%A9%E3%82%B9%E5%AE%9A%E7%BE%A9)
- クラスはデータ構造設計図
- テンプレート

--- 

### クラスを定義する


```python
class クラス名: # クラス名
    def メソッド名１(self, 引数, ...): # そのクラスに属するメソッド
        実行文
    def メソッド名２(self, 引数, ...):
        実行文
```
+ お作法としてクラス名は**大文字**で始める
- メソッドの第一引数は `self` 
- `self` は クラス自分自身 ⇐？？？ですよね

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
試しに self 無しで定義してインスタンス化してみるとわかりやすい
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
- __init__ メソッド内に定義
- 通常、クラスを作る時は、__init__ メソッドを定義する。（__init__ が無いクラスはほとんど見かけない）
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
- メソッド `say` で、もし`self.name` 
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
---