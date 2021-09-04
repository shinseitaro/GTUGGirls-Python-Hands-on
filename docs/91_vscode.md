## VSCode の設定

### ターミナルから VSCode を起動できるようにする
- [Setup - vscode-docs](https://vscode-docs.readthedocs.io/en/latest/editor/setup/)
- 表示 > コマンドパレット > `shell` と書くと **シェルコマンド: PATH内に'code'コマンドをインストールします** がでてくるので選択
- ![](https://vscode-docs.readthedocs.io/en/latest/editor/images/setup/shell-command.png)
- 任意のディレクトリに入って、 `code .` を実行
    ```bash
    $ cd 任意のディレクトリ
    $ code . 
    ```
### 拡張機能

- 拡張機能ボタンをおして、以下二つをインストール
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- ![](https://i.imgur.com/JtR2UCS.png)

### リンタやフォーマッタをインストール

- `requirements.txt` に以下3つを入れてインストール
    ```
    isort 
    black 
    flake8
    ```

### ワークスペースの設定    

- ファイル＞ユーザー設定＞設定＞ワークスペースを押下＞右上のファイルボタンを押す
    ![](https://i.imgur.com/2YevRXp.jpg)


### mac / linux 
- `.venv` の部分はご自身の仮想環境ホルダ名に合わせてください
```
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
    // 仮想環境にインストールしたファイルは監視対象から除外する
    "files.watcherExclude": {
        "**/.venv/**": true
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

### windows
- `.venv` の部分はご自身の仮想環境ホルダ名に合わせてください

```
{
    // PythonのPATHをワークスペースの仮想環境にする
    "python.pythonPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
    // 仮想環境にインストールしたファイルは監視対象から除外する
    "files.watcherExclude": {
        "**/.venv/**": true
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
