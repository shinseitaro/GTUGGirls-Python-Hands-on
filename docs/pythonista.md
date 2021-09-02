---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---

# Pythonista が好んで使いがちな記法
- 内包表記
- アンパック代入
- enumerate
- f-リテラル
- 高階関数（lambda, map, filter）

---
## 内包表記
- [6-1. 内包表記](https://utokyo-ipp.github.io/6/6-1.html?highlight=%E5%86%85%E5%8C%85)
- for loop を ワンライナーで書く記法
- 例：リスト `colors` に入った文字列を全部大文字に変換した新しいリストを作りたい
    ```python
    colors = ["black", "yellow", "black", "blue"]

    # 普通の書き方
    l = list() # 空のリストを作成
    for color in colors:
        l.append(color.upper()) # 要素一つずつを大文字にしながら リストに追加
    print(l)
    ```
    ```python
    # 内包表記
    l = [color.upper() for color in colors] 
    print(l)
    ```    
    - リストの中でforを回している状態。
    - for が入れ子になる場合はしないほうがいい


---
## アンパック代入
- 変数の代入をワンライナーで行う
- 例： x, y, z へ代入
    ```python 
    x, y, z = 1,10,100
    ```
- enumerate や zip とよく使われる
---
## enumerate関数
- [3-2. 繰り返し enumerate](https://utokyo-ipp.github.io/3/3-2.html?highlight=enumerate#enumerate)
- リストをインデックスと要素のタプルで返す関数
- 返り値は `enumerate` オブジェクト
- `enumerate` オブジェクトをリスト関数に渡すとデータを確認できる
- 例：
    ```python
    enumerate(colors)
    # <enumerate object at 0x7f5bb28fec80>

    list(enumerate(colors))
    # [(0, 'black'), (1, 'yellow'), (2, 'black'), (3, 'blue')]

    # アンパック代入して使う
    for i, color in enumerate(colors):
        print(i, color)
   
    # 0 black
    # 1 yellow
    # 2 black
    # 3 blue
    ```
---    
## zip関数
- 2つ以上の要素数が同じシーケンスを要素の位置の組み合わせでタプルにしてシーケンスにする関数
- 返り値は `zip` オブジェクト
- `zip` オブジェクトをリスト関数に渡すとデータを確認できる
- 例：
    ```python
    zip([10, 12, 14, 16, 18], [0, 2, 4, 6, 8])
    # <zip object at 0x7fe72ef29f80> 
    list(zip([10, 12, 14, 16, 18], [0, 2, 4, 6, 8]))
    # [(10, 0), (12, 2), (14, 4), (16, 6), (18, 8)]
    ```
- 例２：アンパック代入と使う
    ```python 
    for x, y in zip([10, 12, 14, 16, 18], [0, 2, 4, 6, 8]):
        print(x * y)
    # 0
    # 24
    # :

    print([x * y for x, y in zip([10, 12, 14, 16, 18], [0, 2, 4, 6, 8])])
    # [0, 24, 56, 96, 144]
    ```
---

## f-リテラル
- 変数や関数呼び出しを文字列としてわたし、そのデータや返り値を文字列フォーマットする方法
- 桁合わせやゼロ埋めなども可
- 例：
    ```python
    name = "shinseitaro"
    print(f"Hello, {name}")
    # Hello, shinseitaro

    print(f"Hello, {name.upper()}")
    # Hello, SHINSEITARO

    num1 = 0.0546
    print(f"{num1:.2%}")
    # 5.46%

    num2 = 5
    print(f"{num2:0=3}")
    # 005
    ```

---
## 高階関数（lambda, map, filter）
- [6-2. 高階関数 ](https://utokyo-ipp.github.io/6/6-2.html?highlight=lambda)
- かなりよく使うが今回はパス

