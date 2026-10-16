a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1]) # p =3 ** 2 = 9
all_num = [a, b, dm[0], dm[1], p] # [17, 5, 3, 2, 9]
min_all = min(all_num) # 2
max_all = max(all_num) # 17
sum_all = sum(all_num) # 36
print(f'{min_all}, {max_all}, {sum_all}')

'''ノート欄
divmod()関数とは商と余りをタプルで返す
pow(x, y)関数とははべき乗(xのy乗)を取得
min()関数とは最小値
max()関数とは最大値
sum()関数とは要素の合計を返す関数
'''