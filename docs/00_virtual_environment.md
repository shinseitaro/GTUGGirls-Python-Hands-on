# 仮想環境構築

- 始める前に Windows の方へのお願い
    - Windows Anaconda で Python をインストールした方
        - Anaconda Prompt を使う
        - Anaconda PowerShell Prompt ではない
        - ![bg right:60%](https://i.imgur.com/gne0Np7.png)

    - Windows Store で python をインストールした方
        - コマンドプロンプト を使う
        - PowerShell ではない
        - ![bg right:60%](https://i.imgur.com/glju8h4.png)


## 仮想環境とは

![bg 65%](https://i.imgur.com/6dJfgSZ.jpg)

- ただのホルダ
- 仮想環境を作成とは
    - プロジェクトディレクトリにPythonをコピー(もどき)すること
- 仮想環境に入る（アクティベートする）とは
    - つくったコピー環境のPythonを使うこと
- なぜ仮想環境を作る？
    - 何かしらの理由でPythonを実行できなくなったとしても仮想環境ディレクトリを消して再作成すればいい
    - サードパーティライブラリのコンフリクトにすぐ対応出来る
    - 「自分のPythonではinstall出来ません」という情弱行動を防げる

## 現在有効な Python を確認

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

## 仮想環境構築手順
- 例： `myproject` というプロジェクトディレクトリ配下で仮想環境を作る
    - お作法
        - デスクトップに作らない
        - root ディレクトリ直下には作らない
        - 半角英数字のみで作成(日本語は使わんで)
- プロジェクトディレクトリ＝レポジトリの感覚
- レポジトリがわからないひとにはただのホルダでオッケ


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
    .venv\Scripts\activate # \ は ￥で表示されると思います
    where python
    ```

#### 以後、当該のプロジェクトディレクトリでターミナルを開いたら必ずアクティベート＆確認する
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

## 仮想環境ホルダの中をみてみよう

- `myproject` をエディタで開く
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


## サードパーティライブラリインストール

### pip とは
- Pythonで書かれたソフトウェアをインストール、管理するためのパッケージ管理システム

### 文法
```bash
pip install ライブラリ名
``` 
>【コラム】 むやみに、pip install して不幸になるひとの行動パターン
> 1. 仮想環境作らずに、いきなり `pip install ライブラリ名` するひと
> 1. jupyter notebook 上で `!pip install ライブラリ名` するひと
> - pip は ライブラリ同士の依存関係を管理しない。よってコンフリクトを起こして「自分のPythonではinstall出来ません」という情弱行動になる

### pip のUpdate
- 仮想環境構築した後、`pip` のUpdateする
    ```bash
    # `which python` / `where python` で確認後
    pip install -U pip 
    ```

### サードパーティライブラリインストール    
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
    - 作業途中で追加のインストールが必要になった場合も、`requirements.txt` に追記してインストールすればOK。新しく追加されたものだけインストールしてくれる。
    
1. インストールを確認
    ```bash
    pip freeze 
    ```

### よくある質問

- どこそこに仮想環境を作ることになって、容量食いませんか？
    - 消せばいいよ( .venv だけ)
    - 気になるひとは → pipxのススメ - podhmo's diary https://pod.hatenablog.com/entry/2021/06/23/221537

### 仮想環境構築まとめ

- mac / linux 
    ```bash
    mkdir myproject
    cd myproject 

    python -m venv .venv
    source .venv/bin/activate # アクティベート
    which python

    pip install -U pip
    # requirements.txt を作成して必要なライブラリ名を記載したあと
    pip install -r requirements.txt
    ```
- windows 
    ```bash
    mkdir myproject
    cd myproject 

    python -m venv .venv
    .venv\Scripts\activate # アクティベート
    where python 

    pip install -U pip
    # requirements.txt を作成して必要なライブラリ名を記載したあと
    pip install -r requirements.txt
    ```
