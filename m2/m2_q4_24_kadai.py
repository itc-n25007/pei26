def func(x, y):
    return [bool(x), bool(y), bool(x + y)]

a = func(-5, -6)

z = a

print(z)

# bool()関数は値をTrueまたはFalseに変換する関数。
# 0や空のリスト、空文字などはFalseになる。
# 0以外の数値や空でない文字列などはTrueになる。