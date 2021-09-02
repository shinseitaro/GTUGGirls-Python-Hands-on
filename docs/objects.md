---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---

# オブジェクト

- [1-3. 論理・比較演算と条件分岐の基礎 — オブジェクト](https://utokyo-ipp.github.io/1/1-3.html#%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88)
- 説明が全然足りない

### オブジェクト指向
+ **データとデータの処理を一つのオブジェクトにまとめておこうという発想**
+ データじたいが、自分自身は何をすることが出来るか（=**メソッド**）を持つイメージ
+ 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**


---
```python
# s に文字列を格納
>>> s = "shinseitaro"
```
- s という変数に入れたのは "shinseitaro"という文字列とpython が評価したタイミングで、sというオブジェクトが作成され、s はデータは "shinseitaro", メソッドに文字列に対して出来る色々なことが実装された状態になる
    
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
- . で呼び出せる処理のことを **メソッド** という（関数という人がいるけどメソッドです）
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
## メソッドと関数
- オブジェクト自身が、オブジェクトのデータに対して出来る処理を「**メソッド**」
- 外から渡されたデータの処理を「**関数**」

### 見た目の違い
- メソッド
    ```python 
    s = "shinseitaro"
    s.upper() # オブジェクトのデータを大文字で返すメソッド
    s.replace("taro", "jiro") # オブジェクトのデータを置換して値を返すメソッド
    ```
    - `データ.メソッド()` 
    - データのメソッドがぶら下がってる
- 関数
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
    raise 10/0, "0で割り算出来ません"
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
## まとめ
- オブジェクトとは
    - データとメソッドをひとかたまりで持っている構造
    - 文字列や数値など python で評価(eval)したタイミングで全てオブジェクトに変わる
    - だから、ユーザーが定義しなくても組み込まれたメソッドが使える




