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
