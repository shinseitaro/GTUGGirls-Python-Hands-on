---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---
# 雰囲気でPythonを使っている人のための<br>Python再入門

2021/09/04
GTUGGirls ハンズオン

---
## 自己紹介

- [しんせいたろう](https://twitter.com/shinseitaro)
- 雰囲気でpython書いてる(10年以上)
- しごと
    - 米国株とれーだー
    - 時系列データ分析（株、暗号資産、為替）、投資ストラテジー作成
    - ニュースのスクレイピングとレポート作り
    - python の個別指導
- コミュニティ    
    - [GTUGGirls](https://gtuggirls.connpass.com/) (スタッフ)
    - [Fin-py](https://fin-py.connpass.com/) (准管理者)
    - [月刊Fintalk](https://fintalk.connpass.com/) (主宰)
    - [モグモグDjango](https://mogumogu-django.connpass.com/) (主宰)
---
## 今日やること
1. 仮想環境作成
1. Python完全に理解した、からちょっと脱却して、チョットデキルひとになる最初の一歩
1. 勉強した内容を踏まえて scraping と 可視化のデモ
1. VSCode の便利な設定

## 今日やらないこと
1. [Pythonプログラミング入門 — Pythonプログラミング入門 documentation](https://utokyo-ipp.github.io/)を一緒に読む、解く
    - 自主的にやった方が早いから
    - 引っかかったら、いつでも質問ウェルカムです

---
(始める前に Windows の方へのお願い)
## ターミナルについて
- コマンドプロンプトやPowershellなどのことを今日はまとめてターミナルと呼びます。
### Windows Anaconda で Python をインストールした方
![bg right:60%](https://i.imgur.com/gne0Np7.png)
- Anaconda Prompt を使う
- Anaconda PowerShell Prompt ではない

---
### Windows Store で python をインストールした方
![bg right:60%](https://i.imgur.com/glju8h4.png)

- コマンドプロンプト を使う
- PowerShell ではない

---
# 仮想環境構築

---
今日伝えたいことはたったひとつ

## とりあえずPythonの仮想環境作ってください。<br>心からのお願いです。
---

### Python :snake: を確認

- ターミナルを立ち上げる
- windows:
    ```bash
    where python
    ```
    - 一番上にでてきた python へのパスが有効
- mac / linux 
    ```bash
    which python
    ```
    - 有効な python パスのみ出てくる

---

### 仮想環境構築

![bg 65%](https://i.imgur.com/6dJfgSZ.jpg)

---
#### 仮想環境とは
- ただのホルダ
- 仮想環境を作成とは
    - プロジェクトディレクトリにPythonをコピーすること
- 仮想環境に入る（アクティベートする）とは
    - つくったコピー環境のPythonを使うこと
- なぜ仮想環境を作る？
    - 何かしらの理由でPythonを実行できなくなったとしても仮想環境ディレクトリを消して再作成すればいい
    - サードパーティライブラリのコンフリクトにすぐ対応出来る
    - 「自分のPythonではinstall出来ません」という情弱行動を防げる :point_left: :satisfied:
---

#### 仮想環境構築手順
- 例： `myproject` というプロジェクトディレクトリ配下で仮想環境を作る
    - お作法
        - デスクトップに作らない
        - root ディレクトリ直下には作らない
        - 半角英数字のみで作成(日本語は使わんで)
- プロジェクトディレクトリ＝レポジトリの感覚
- レポジトリがわからないひとにはただのホルダでオッケ

---
#### 仮想環境構築手順 Mac / Linux

1. プロジェクトディレクトリに入る
    ```bash
    cd myproject
    ```
1. 現在のPythonを確認する（任意）
    ```bash
    which python
    ```    
1. 仮想環境構築
    ```bash
    # python -m venv <仮想環境ディレクトリの名前>
    python -m venv .venv
    ``` 
    - ディレクトリ名でよく使われるもの： `.venv` `venv` `myenv` `myvenv`
1. 仮想環境のPythonを使うよう設定（アクティベート）し、確認
    ```bash
    source .venv/bin/activate
    which python
    ```
    
---
#### 仮想環境構築手順 Windows

1. プロジェクトディレクトリに入る
    ```bash
    cd myproject
    ```
1. 現在のPythonを確認する（任意）
    ```bash
    where python
    ```    
1. 仮想環境構築
    ```bash
    # python -m venv <仮想環境ディレクトリの名前>
    python -m venv .venv
    ```
    - 注意：ファイルエクスプローラの設定によって `.` 始まりのホルダは「隠しホルダ」とみなされ表示されないことがあります。その場合は `venv` など適当に名前は変えて下さい
1. 仮想環境のPythonを使うよう設定（アクティベート）し、確認
    ```bash
    .venv\Script\activate # \ は ￥で表示されると思います
    where python
    ```
---

#### 実行

1. インタラクティブシェル
    ```bash
    python 
    Python 3.8.3 (default, May 19 2020, 18:47:26) 
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print("Hello")
    Hello 

    >>> exit()
    ```
1. ファイル実行
    - エディタで `myproject` を開いて下さい
    - `src/hoge.py` を新規作成して下のコードを入力保存して下さい
        ```python
        print("Hello")
        ```
    - ターミナルで下記を実行して下さい
        ```bash
        python src/hoge.py
        ```

---

#### 以後、ターミナルを開いたらアクティベート＆確認する
- (linux / mac) 
    ```bash
    source .venv/bin/activate
    which python
    ```
- (win) 
    ```bash
    venv\Script\activate
    where python 
    ``` 
---
#### 仮想環境ホルダの中をみてみよう

- myprojectをエディタで開いてください

```bash
.venv
├── bin
│   ├── activate
│   ├── pip # サードライブラリインストールツール pip
│   ├── pip3
│   ├── pip3.8
│   ├── pygmentize
│   ├── python -> /home/shinseitaro/miniconda3/bin/python
│   └── python3 -> python # このPythonを使う
├── include
├── lib
│   └── python3.8
├── lib64 -> lib
```
(一部抜粋)

---

### ライブラリインストール

#### pip とは
- Pythonで書かれたソフトウェアをインストール、管理するためのパッケージ管理システム
#### 文法
```bash
pip install ライブラリ名
``` 
###### 【コラム】 むやみに、pip install して不幸になるひとの行動パターン
> 1. 仮想環境作らずに、いきなり `pip install ライブラリ名` するひと
> 1. jupyter notebook 上で `!pip install ライブラリ名` するひと
> - pip は ライブラリ同士の依存関係を管理しない。よってコンフリクトを起こして「自分のPythonではinstall出来ません」という情弱行動になる（二回目） :point_left: :satisfied:

---

### ライブラリインストール

#### pip じたいのUpdate
- 仮想環境構築した後、pip じたいのUpdateをおこなう。
    ```bash
    # `which python` / `where python` で確認後
    pip install -U pip 
    ```
---    
#### サードライブラリインストール    
1. `requirements.txt` 新規作成(慣習的にこの名前だが違ってもOK)
    ```bash
    touch requirements.txt 
    ``` 
1. `requirements.txt` にインストールしたいライブラリ名を書く
    ```bash
    # 一行に一つ
    beautifulsoup4
    # バージョン指定も可
    requests-html == 0.10.0
    ```
    - その他の記法はこちら：[pip install - pip documentation v21.3.dev0](https://pip.pypa.io/en/latest/cli/pip_install/#example-requirements-file)

1. `-r` オプションでインストール
    ```bash
    pip install -r requirements.txt
    ```
- 作業途中で追加のインストールが必要になった時も、`requirements.txt` に追記してインストールすればOK。新しく追加されたものだけインストールしてくれる。
    
---
### ライブラリインストール 確認

```bash
pip freeze 
```

### .venv を覗く :eyes: 

### .venv を削除してもう一回インストール
---
### よくある質問

- どこそこに仮想環境を作ることになって、容量食いませんか？
    - 消せばいいよ( .venv だけ)
    - 気になるひとは → pipxのススメ - podhmo's diary https://pod.hatenablog.com/entry/2021/06/23/221537

---
### 仮想環境構築まとめ

- mac / linux 
    ```bash
    mkdir myproject
    cd myproject 

    python -m venv .venv
    source .venv/bin/activate # アクティベート
    which python

    pip install -U pip
    ```
- windows 
    ```bash
    mkdir myproject
    cd myproject 

    python -m venv .venv
    .venv\Script\activate # アクティベート
    where python 

    pip install -U pip
    ```

---
## 演習
1. ディレクトリ `gtugtest` 作成
1. その中に python の仮想環境を作成
1. 以下のライブラリを仮想環境下にインストール
    > djangorestframework
    > Django
1. `gtugtest` 削除

---
# 「Python完全に理解した」からちょっと脱却して<br>「チョットデキル」ひとになる最初の一歩
---
### Python は jupyter notebook ではない

- jupyter を python と思ってるひとが多数
- jupyter でしか python を実行出来ないひと多数
- ヤメて
---

### エラーは読んで

```python
>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
- エラーメッセージは下から上に読んでいく
- 上記の場合 `ZeroDivisionError: division by zero` がエラーの根幹
- 質問する時は、エラーメッセージを全部コピペして、問題ない範囲でコードを渡して再現してもらおう

---
## python の概念,キーワード,知らないとツライ単語
- オブジェクト
    - メソッド 
    - 関数
- クラス
    - インスタンス
- スコープ
    - モジュール
---


# オブジェクト
- [1-3. 論理・比較演算と条件分岐の基礎 — オブジェクト](https://utokyo-ipp.github.io/1/1-3.html#%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88)

### オブジェクト指向
+ **データと、そのデータを使った処理を一つのオブジェクトにまとめておこうという発想**
+ データじたいが、自分自身は何をすることが出来るか（=**メソッド**）を持つイメージ
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**

---
```python
# s に文字列を格納
>>> s = "shinseitaro"
```
- s という変数に入れたのは "shinseitaro"という文字列をpython が評価したタイミングで、文字列オブジェクトが作成され、データは "shinseitaro", メソッドに文字列に対して出来る色々なことが実装された状態になる
    
```python
# type関数で、s の型を調べる
>>> type(s)
<class 'str'>
```
```python
# テキストシーケンス型 s が持つ アトリビュートを調べる.(長いので一部省略しています)
>>> dir(s)
['__add__',...,
'capitalize', 'casefold', 'center', 'count', ...,
'find', 'format', 'format_map', 'index', ..., 
'isdigit', 'isidentifier', 'islower', 'isnumeric', ...,
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
- https://docs.python.org/ja/3/library/stdtypes.html#string-methods
---
![](https://i.imgur.com/PKgmwAS.png)

- `s` は "shinseitaro" というデータを持つ
- データに対する処理は `.` で呼び出せる
- . で呼び出せる処理のことを **メソッド** という
    ```python
    # オブジェクトのデータを大文字で返す .upper() メソッド
    >>> s.upper()
    'SHINSEITARO'
    ```

---
## メソッドと関数
- オブジェクトのデータに対して、オブジェクトが持つ処理命令を「**メソッド**」
- 引数として外から渡されたデータの処理命令を「**関数**」

### 見た目の違い
- メソッド
    - `データ.メソッド()` 
        ```python 
        s = "shinseitaro"
        s.upper() # オブジェクトのデータを大文字で返すメソッド
        s.replace("taro", "jiro") # オブジェクトのデータを置換して値を返すメソッド
        ```
- 関数
    - `関数名(引数)`
        ```python
        max([2,5,8]) # 渡されたデータで最大値を返す関数
        len([2,5,8]) # 渡されたデータの個数を返す関数
        str(12345) #  渡されたデータを文字列で返す関数
        ```

---
## 文
- 通常1行で書く命令
    ```python
    import os 
    return v
    ```
- メソッドや関数のように呼び出しための `()` がついていない命令
- メモ
    - python２系では print は文
    - python３系では print は関数
        ```python 
        # ２.ｘ
        print "Hello"
        ```
        ```python 
        # ３.ｘ以降
        print("Hello")
        ```

---
## オブジェクトまとめ
- オブジェクトとは
    - データとメソッドをひとかたまりで持っている構造
    - 文字列や数値など python で評価(eval)したタイミングで全てオブジェクトに変わる
    - だから、ユーザーが定義しなくても組み込まれたメソッドが使える
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
- 例：`src/hoge.py` の関数を `src/moge.py` で呼び出す
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
- 例：`src/child/huga.py` に記述した関数を `src/moge.py` で呼び出す
- moge.py からみたら、同列の child の配下の huga なのでそのまま `child.huga` でインポート可
    ```bash
    └── src
        ├── child
        │   └── huga.py
        ├── hoge.py
        ├── moge.py
    ```  
- `src/child/huga.py` に関数定義
    ```python
    # src/child/huga.py
    def ringmeup(name):
        return f"Hello {name}"    
    ```
- `src/moge.py` で呼び出し
    ```python
    import child.huga
    print(child.huga.ringmeup("sehinseitaro"))
    ```

---
##### 違う階層に定義している場合２
- 例： `src/hoge.py` で定義した関数を `src/child/huge.py` で呼び出す
    ```bash
    └── src
        ├── child
        │   └── huga.py # ここからhogeは二階層上のディレクトリ配下にある
        ├── hoge.py
        ├── moge.py
    ```  
- `huga.py` から見たら、`hoge.py` は 2階層上の src の配下にある
- この src を 一時的にPATHに入れるという方法をとります

---
- このモジュールの親の親(`src`)をルートディレクトリとして一時的にPATHに追加
- その配下にある `hoge.py` を import 出来るようにする
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
    - `__file__` は組み込み属性と呼ばれる特別なアトリビュートで当該ファイルパスを返す

---

## 実践Python スクレイピングと可視化

- お伝えしたPythonの概念を体感してもらう
- [shinseitaro/GTUGGirls-Python-Hands-on-test-project: GTUGGirls-Python-Hands-on 用テストプロジェクト](https://github.com/shinseitaro/GTUGGirls-Python-Hands-on-test-project)

--- 
## VSCode の設定

1. requirements.txt に以下3つを入れてインストール
    ```
    isort 
    black 
    flake8
    ```
1. ファイル＞ユーザー設定＞設定＞ワークスペースを押下＞右上のファイルボタンを押す
    ![](https://i.imgur.com/2YevRXp.jpg)
---
### mac / linux 
```json
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
    // 仮想環境にインストールしたファイルは監視対象から除外する
    "files.watcherExclude": {
        "**/venv/**": true
    },
    // リンタでPyLintは使わない
    "python.linting.pylintEnabled": false,
    // リンタでFlake8を使う
    "python.linting.flake8Enabled": true,
    // コードフォーマッタでBlackを使う
    "python.formatting.provider": "black",
    // Blackは貼り付け時の整形に対応していないので無効にする
    "editor.formatOnPaste": false,
    // 1行の文字数を88文字とする
    "python.linting.flake8Args": ["--max-line-length", "88"],
    // languageServerにPylanceを使う
    "python.languageServer": "Pylance",
    // Pylanceの型チェックをbasicにする
    "python.analysis.typeCheckingMode": "basic",
    // Pylanceの括弧補完を有効にする
    "python.analysis.completeFunctionParens": true,
}
```
---
### windows
```json
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
    // 仮想環境にインストールしたファイルは監視対象から除外する
    "files.watcherExclude": {
        "**/venv/**": true
    },
    // リンタでPyLintは使わない
    "python.linting.pylintEnabled": false,
    // リンタでFlake8を使う
    "python.linting.flake8Enabled": true,
    // コードフォーマッタでBlackを使う
    "python.formatting.provider": "black",
    // Blackは貼り付け時の整形に対応していないので無効にする
    "editor.formatOnPaste": false,
    // 1行の文字数を88文字とする
    "python.linting.flake8Args": ["--max-line-length", "88"],
    // languageServerにPylanceを使う
    "python.languageServer": "Pylance",
    // Pylanceの型チェックをbasicにする
    "python.analysis.typeCheckingMode": "basic",
    // Pylanceの括弧補完を有効にする
    "python.analysis.completeFunctionParens": true
}
```
