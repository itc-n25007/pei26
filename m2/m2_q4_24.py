def func(a, b):  # 関数の定義
    if a ** b <= 64:
        return 1
    else:
        return 0

a = func(-5, -6)  # 関数の戻り値を変数aに代入

z = [bool(a), bool(func(3, 4)), bool(func(4, 3))]

print(z)

# bool()関数について
# bool()は値をTrueまたはFalseに変換する関数。
# 0はFalse、0以外の数値はTrueになる。
    