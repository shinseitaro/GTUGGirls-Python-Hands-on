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
自己紹介

- [しんせいたろう](https://twitter.com/shinseitaro)
- 雰囲気でpython書いてる(10年以上)
- しごと
    - 米国株とれーだー
    - 時系列データ分析（株、暗号資産、為替）、投資ストラテジー作成
    - python の個別指導
- コミュニティ    
    - [GTUGGirls](https://gtuggirls.connpass.com/) (スタッフ)
    - [Fin-py](https://fin-py.connpass.com/) (准管理者)
    - [月刊Fintalk](https://fintalk.connpass.com/) (主宰)
    - [モグモグDjango](https://mogumogu-django.connpass.com/) (主宰)
---
### お願い
- わたしのメインマシンが Linux なので、Windowsの知識が弱いです
- なので、Windowsユーザの方にヘルプをお願いすることがあると思います。ご協力下さいませ。
- Mac は linux とほとんど同じだろうと思い込んでるフシがありますが、もし違ったらすぐに教えて下さい。
---
### Python :snake: を確認

- terminal / command prompt 立ち上げ
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
- Pythonはバージョンやディストリビューターで複数インストールすることが可

---

### 仮想環境構築

![bg 65%](https://i.imgur.com/6dJfgSZ.jpg)

---
#### 仮想環境とは
- ただのホルダ
- 仮想環境を作成とは
    - インストールしたPythonだけをプロジェクトディレクトリにコピーすること
- 仮想環境に入るとは
    - つくったコピー環境を使う
- なぜ仮想環境を作る？
    - 作成、削除、改変、なんでも出来る
    - 何かしらの理由で実行できなくなったとしても仮想環境ディレクトリを消して再作成すればいい
    - サードパーティライブラリのコンフリクトを防ぐ
    - 「自分のPythonでは動きません」という情弱行動を防げる
---

#### 仮想環境構築手順
- 例： `myproject` というプロジェクトディレクトリ配下で仮想環境を作る
    - お作法
        - デスクトップに作らない
        - root ディレクトリ直下には作らない
        - 半角英数字のみで作成(日本語は使わんで)
---

1. プロジェクトディレクトリ作成
    ```bash
    mkdir myproject
    cd myproject
    ```
1. 仮想環境構築
    ```python
    python -m venv .venv`
    ``` 
    
1. `.venv` ディレクトリ作成確認
1. 仮想環境に入る    
    - (linux / mac) `source .venv/bin/activate` 
    - (win) `venv\Script\activate` 

- プロジェクトディレクトリ＝レポジトリの感覚
- レポジトリがわからないひとにはただのホルダでオッケ


---

#### 以後、必ずするクセ付けて
- (linux / mac) 
    ```
    $ source .venv/bin/activate
    $ which python
    ```
- (win) 
    ```
    venv\Script\activate
    where python 
    ``` 
---

### ライブラリインストール

#### pip とは

---

### ライブラリインストール

- `pip install ライブラリ名` するのは最初の一回だけ、`pip install -U pip `
```bash
touch requirements.txt 
``` 
```bash
# linux / mac
$ which python 
# windows
$ where python 
```
```bash
$ pip install -r requirements.txt
```

---
## 演習
1. ディレクトリ `gtugtest` 作成
1. その中に python の仮想環境を作成
1. 以下のライブラリを仮想環境下にインストール
1. `gtugtest` 削除
---
### Anaconda / miniconda について

---

### Python は jupyter notebook ではない

- jupyter を python と思ってるひとが多数
- jupyter でしか python を実行出来ないひと多数
- ヤメて
---

## エラーは読んで

```python
>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

- エラーメッセージは下から上に読んでいく

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

## DRY 

- 概念がわかってないとかけないPythonの哲学

---
## 部品を作ってループで回す


---
---
### Pythonista がこのむ python らしい書き方

- 内包表記
- アンパック代入
- 高階関数（lambda, map, filter）
- f-リテラル
---

## test


---

## python 概念と pythonist らしいコードの例

### 構造

- 私が「キレイ」だと思ったpythonのfile構造
- モジュールの説明も兼ねる
- main.py を実行ファイルとして、あとのファイルには関数群を作る


### python はオブジェクト

- beautifulsoup でスクレイピングしたデータを
- pandas に流し込んで 
- 可視化

---

### VSCode の設定

```json
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}/venv/bin/python",
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

### VSCode の設定
```json
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}\\venv\\Scripts\\python.exe",
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
---
