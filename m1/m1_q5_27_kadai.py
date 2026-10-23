
# 果物のリストを作成する
list_fruits = ['マンゴー', 'パイナップル', 'バンシルー']

# 好きな果物を取り出して、変数favoriteに代入する
favorite = list_fruits.pop(1)  # インデックス1のパイナップルを取り出して削除する

# パイナップルが好きな理由：甘くておいしいから
print(favorite)

# 果物を取り出した後の残りのリストを表示する
print(list_fruits)
