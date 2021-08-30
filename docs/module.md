---
marp: true
theme: test
footer: "by **＠しんせいたろう**"
paginate: true
---

# 名前空間

- [3-3. 関数 変数とスコープ](https://utokyo-ipp.github.io/3/3-3.html#%E5%A4%89%E6%95%B0%E3%81%A8%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97)
- ここでスコープにすこし触れられているが、全く足りないので追加します


## 名前空間（ネームスペース）
変数、関数、クラスなどが定義されている場所のこと。

## スコープ
変数、関数、クラスなどが有効な範囲

---

![bg right:60%](https://i.imgur.com/xOdTeLq.jpg)

##### ビルドインスコープ
+ `+`、 `>` 、 `def` などいきなり使える python のコード
##### モジュールスコープ
+ ファイルに書く、変数や関数やクラス
+ トップレベルとも呼ぶ
+ グローバルと呼ぶひともいる
##### ローカルスコープ
+ ファイル記述された関数やクラスの「内部」のみ

---
#### 意識してローカルスコープを使おう
+ 図の例でいえば、`func` 関数の中の 引数 `a` などは、**func 関数のなかでしか使えない**
+ もし、別の関数やクラスで同じ名前の引数を使っていてもローカルスコープだけで有効。    
+ これがもっとも安全（＝エラー処理が楽）な方法
---