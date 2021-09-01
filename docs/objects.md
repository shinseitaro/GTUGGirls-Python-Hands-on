---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---


# python の オブジェクト

- [1-3. 論理・比較演算と条件分岐の基礎 — オブジェクト](https://utokyo-ipp.github.io/1/1-3.html#%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88)
- 説明が全然足りない


---

## オブジェクト指向プログラミングと命令型プログラミング

---
### オブジェクト指向
+ **データと命令を一つのオブジェクトに打ち込んでおこうという発想**
+ データじたいが、自分自身は何をすることが出来るか（=**メソッド**）を持つ
+ データにメソッドがブラブラぶら下がる
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**

---
```python
# s に文字列を格納
>>> s = "shinseitaro"
```
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
---
- `s` は "shinseitaro" というデータを持つ
- dir(s) で確認できたアトリビュートは、`.` で利用できる
- . で呼び出せる命令のことを **メソッド** という（関数という人がいるけどメソッドです）
- アトリビュートがデータの場合は `.データ名` で呼び出し可
```python
# 全部を大文字にする upper メソッド
>>> s.upper()
'SHINSEITARO'

# 第一引数の文字列で始まるかどうか真偽値を返す startswith メソッド
>>> s.startswith("m")
False
```
https://docs.python.org/ja/3/library/stdtypes.html#string-methods

---
### 命令型プログラミング
+ 関数型プログラミングとも言う
+ **データと命令をはっきりと分ける**
+ メソッドのように、データが自分自身は何をすることが出来るか（メソッド）を持つという発想はない
+ データにメソッドがぶら下がったりしない

---
clojureの例
```clojure
;; 引数が文字列かどうか返す strings? 関数
user=> (string? "abc")
true
;; 引数を全部大文字で返す upper-case 関数
user=> (clojure.string/upper-case "abc")
"ABC"
```

---

### Pythonは、命令型もオブジェクト指向もある
- データにひっついた関数をメソッド
- そうではない命令を関数と呼ぶ

```python 
# リスト作成
>>> colors = ['black', 'yellow', 'black', 'blue']
# リストの要素数を返す len関数
>>> len(colors)
4
# 第一引数に渡された要素がリストの中にいくつあるか返す count メソッド
>>> colors.count('black')
2

# ユーザ定義の関数
def tashizan(x,y):
    return x + y
```


---
## オブジェクト

- python の オブジェクトとはデータとメソッドをひとかたまりで持っている構造
- 文字列や数値など python で評価(eval)したタイミングで全てオブジェクトに変わる
- だから、ユーザーが定義しなくても組み込まれたメソッドが使える




