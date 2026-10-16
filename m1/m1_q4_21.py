num = 12
list_s = [] # 空のリスト
s = 2 # ↓のコメントは１回目のループでの処理イメージ
while s <= num: # 2 <= 12はTrue
    if num % s == 0: # 12 % 2 == 0はTrue
        num //= s # //=は整数除算(切り捨て除算)して代入、つまり12 // 2 =6←これがnumに代入される
        if s not in list_s: # sはlist_sにないのでTrue
            list_s.append(s) # [2]となる
    else: # １回目のループでは実行されない
        s += 1
print(list_s)

"""計算欄
１回目のループ後: num=6 list_s=[2] s=2
２回めのループ後: num=3 list_2=[2] s=2
３回目のループ後: num=3 list_2=[2] s=3
４回目のループ後: num=1 list_2=[2,3] s=3
while 3 <= 1 はFalseなのでループ終了
よって答えは[2,3]となる
"""