list_a = [] # 空のリスト

a = 2 # 変数aに2を代入

for i in range(6): # リストの要素を6個作るため、6回繰り返す
    # aの値をリストの末尾に追加する
    list_a.append(a) # append()はリストの最後に要素を追加する
    # 次の繰り返しに向けて、aの値を2倍にする
    a = a * 2

print(list_a) 