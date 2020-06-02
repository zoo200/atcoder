## DFS

* [ATC001_A_DFS](/ATC001_A_DFS.py)  
https://atc001.contest.atcoder.jp/tasks/dfs_a  

* [ABC146_D_ColoringEdgesonTree](ABC146_D_ColoringEdgesonTree.py)  
https://atcoder.jp/contests/abc146/tasks/abc146_d  
※ツリー構造はDFSで処理するものらしい

* https://atcoder.jp/contests/abc138/submissions/12989520  
※入力が多すぎてinput でTLEした  



## BFS

* [ABC007_C_BFS](/ABC007_C_BFS.py)  
https://abc007.contest.atcoder.jp/tasks/abc007_3

* [AGC033_A_Darker_and_Darker](/AGC033_A_Darker_and_Darker.py)  
https://atcoder.jp/contests/agc033/tasks/agc033_a

## DP

* [ABC129_C_TypicalStairs](/ABC129_C_TypicalStairs.py)  
https://atcoder.jp/contests/abc129/tasks/abc129_c

* [ABC154_E_AlmostEverywhereZero](/ABC154_E_AlmostEverywhereZero.py)  
https://atcoder.jp/contests/abc154/tasks/abc154_e

## ２分探索

* [ABC146_C_Buy_an_Integer](/ABC146_C_Buy_an_Integer.py)  
https://atcoder.jp/contests/abc146/tasks/abc146_c  
x以下の最大の数=left(ok)を返す

* [ARC037_C_Okumasu](/ARC037_C_Okumasu.py)  
https://atcoder.jp/contests/arc037/tasks/arc037_c  
x以上の最小の数=right(ok)を返す (x番目に位置する値 = xより小さいのはng)

## UnionFind

* [ABC157_D_Friend_Suggestions](/ABC157_D_Friend_Suggestions.py)  
https://atcoder.jp/contests/abc157/tasks/abc157_d

## 尺取方
* [ABC032_C_TwoPointer](/ABC032_C_TwoPointer.py)  
https://atcoder.jp/contests/abc032/tasks/abc032_c  
別解というか130やってそれっぽく  
https://atcoder.jp/contests/abc032/submissions/13602546

* 下段のほうがわかりやすいかも  
https://atcoder.jp/contests/abc130/submissions/13137345  
https://atcoder.jp/contests/abc130/submissions/13137206  

## bit演算

* [ABC081_B_Shift-only](/ABC081_B_Shift-only.py)  
https://atcoder.jp/contests/abc081/tasks/abc081_b

## bit全探索

* [ABC147_C_HonestOrUnkind2](/ABC147_C_HonestOrUnkind2.py)  
https://atcoder.jp/contests/abc147/tasks/abc147_c  

* https://atcoder.jp/contests/abc128/submissions/12830044  

## XOR
* https://atcoder.jp/contests/abc121/tasks/abc121_d  
https://qiita.com/vain0x/items/9faf89f843f96d8c46cd  
* https://atcoder.jp/contests/abc147/tasks/abc147_d  


## 組み合わせ

* [ABC156_D_Bouquet](/ABC156_D_Bouquet.py)  
https://atcoder.jp/contests/abc156/tasks/abc156_d  
& 余剰、フェルマーの小定理、逆元

* https://atcoder.jp/contests/abc132/submissions/13274015  
公式解説とはcmbの部分が違う。↑の以前のメソッドを利用した。  
あと重複組合せの公式　ｎＨｒ＝n+r-1Cｒ　の考えを  
f(x,y){x個の玉をyグループに分ける場合の数を返す} の引数に利用した。  
{y種類の玉をx個選ぶと同義}　なので  
y H x = x+y-1 C x  
↓　どれか一つ必ず選ぶパターンはまずy種類からそれぞれ１個ずつ選択するのでx-y する  
y H x-y  = x-1 C x-y  
となる

* https://atcoder.jp/contests/abc156/submissions/13762865  
ｎCr　nが小さければ（5,6乗?) こっちのほうがいい。  
この問題は↑のcmbだとTLEする。  
逆に↑の問題だとnが大きすぎてこっちの事前階乗計算のやり方だとTLEする。要使い分け。  

## ベン図

* [ABC131_C_Anti-Division](/ABC131_C_Anti-Division.py)  
https://atcoder.jp/contests/abc131/tasks/abc131_c  
& lcm , gcd 

## 優先度付キュー

* https://atcoder.jp/contests/abc141/submissions/12965269


## その他

### 剰余の考え方(合同)
* [ABC133_C_RemainderMinimization2019](/ABC133_C_RemainderMinimization2019.py)  
https://atcoder.jp/contests/abc133/tasks/abc133_c


### 逆を考える

逆、双対、補集合などの考え方。

* 例1:https://atcoder.jp/contests/abc140/tasks/abc140_c  
何かわからないAの最大（無限に考えられる可能性）よりも  
はっきりと与えられるBの最小（わかってる）から考えたほうがやりやすい。

* 例2:https://atcoder.jp/contests/abc162/tasks/abc162_d  
条件の２つ目、＝じゃないってのは求めにくい。感覚的に。ので＝を求める。  
そして全体から＝を引いて≠を求める。

* 参考:
https://qiita.com/gnbrganchan/items/a3c3c69ba29707b62321


### 浮動小数点

* [ABC169_C_Multiplication3](/ABC169_C_Multiplication3.py)  
https://atcoder.jp/contests/abc169/tasks/abc169_c  
