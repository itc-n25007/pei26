num = 12 # 素因数分解する数
list_s = [] # 素因数を保存するリスト
s = 2 # 割り算を試す数
while s <= num: # sがnum以下の間、繰り返す
    if num % s == 0:  # numがsで割り切れるか確認
        num //= s  # numをsで割る
        print(num) # 割り算後のnumを表示
        if s not in list_s: # sがリストにない場合、追加する
            list_s.append(s)   # numが3になったとき、3を表示
        if num == 3:
            print(num)
    else: 
        # 割り切れない場合はsを1増やす
        s += 1
print(list_s)

