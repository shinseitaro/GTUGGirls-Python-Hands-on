# 名前空間

- [3-3. 関数 変数とスコープ](https://utokyo-ipp.github.io/3/3-3.html#%E5%A4%89%E6%95%B0%E3%81%A8%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97)
- ここでスコープにすこし触れられているが、全く足りないので追加します

## 名前空間（ネームスペース）
- 変数、関数、クラスなどが定義されている場所のこと。

## スコープ
- 変数、関数、クラスなどが有効な範囲
- 3つのスコープがある

1. ビルドインスコープ
    + `+`、 `>` 、 `def` `type()` `max()` など、どこでも使える関数などが所属
2. モジュールスコープ
    + `.py`ファイルに記述された変数や関数やクラスが所属
    + トップレベル(グローバル)とも呼ぶ
3. ローカルスコープ
    + ファイル記述された関数やクラスの「内部」のみが所属

![bg right:60%](https://i.imgur.com/xOdTeLq.jpg)

### 意識してローカルスコープを使おう
+ 図の例でいえば、`func` 関数の中の 引数 `a` などは、**func 関数のなかでしか使えない**
+ もし、別の関数やクラスで同じ名前の引数を使っていてもローカルスコープだけで有効なので、コンフリクトしない

### モジュール間のスコープ
- モジュール(`.py`ファイル)が違えばスコープは違う
- 違うモジュールに定義した関数やクラスはどうやって使う？

### 同じ階層に定義している場合
- 例：`src/hoge.py` の関数を `src/moge.py` で呼び出す
    ```bash
    └── src
        ├── hoge.py
        ├── moge.py
    ```
    ```python
    # src/hoge.py
    def callme(name):
        return f"Hello {name}"
    ```
    ```python
    # src/moge.py
    import moge 
    print(moge.callme("shinseitaro"))
    ```

### 違う階層に定義している場合１
- 例：`src/child/huga.py` に記述した関数を `src/moge.py` で呼び出す
- `moge.py` からみたら、同列の `child` の配下の huga なのでそのまま `child.huga` でインポート可
    ```bash
    └── src
        ├── child
        │   └── huga.py
        ├── hoge.py
        ├── moge.py
    ```  
- `src/child/huga.py` に関数定義
    ```python
    def ringmeup(name):
        return f"Hello {name}"
    ```
- `src/moge.py` で呼び出し
    ```python
    import child.huga
    print(child.huga.ringmeup("sehinseitaro"))
    ```


### 違う階層に定義している場合２
- 例： `src/hoge.py` に記述した関数を `src/child/huge.py` で呼び出す
    ```bash
    └── src
        ├── child
        │   └── huga.py # ここからhogeは二階層上のディレクトリ配下にある
        ├── hoge.py
        ├── moge.py
    ```  
- `huga.py` から見たら、`hoge.py` は 2階層上の `src` の配下にある
- `src/child/huge.py` モジュールの親の親ディレクトリ(`src`)をルートディレクトリとして一時的にPATHに追加
- これで、`src/hoge.py` を `src/child/huge.py`で import 出来るようになる
    ```python 
    # src/child/huge.py
    import sys
    import os

    # src/child/huge.pyの dirname の dirname を返すから rootdir は "src"
    rootdir = os.path.dirname(os.path.dirname("__file__"))
    # src を一時的にPATHに入れる
    sys.path.append(rootdir)
    # これで、src に入っている hoge を import することができる
    import hoge
    print(hoge.callme("ﾌｶﾞﾌｶﾞ"))
    ```
    - `__file__` は組み込み属性と呼ばれる特別なアトリビュートで当該ファイルパスを返す

