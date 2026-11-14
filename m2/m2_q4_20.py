num = 3
list_a = []
while num < 5: # numが3,4のときに実行される、計２回繰り返す
    for i in range(num, 10, 3): # numから10未満までの3ずつ増やしたあたりを順番に取得する
        i -= 6 # iを変更しても、次の繰り返しではrange()から次の値が代入する
        list_a.append(i) # 変更されたiの値がlist_aに追加される
    num += 1
print(sum(list_a))

'''
num=3のときのforループ処理
3, 6, 9それぞれ-6してappendするので[-3, 0, 3]となる

num=4
4, 7それぞれ-6してapeendするので[-2, 1]となる

最終的にlist_aのo内容は([-3, 0 , 3, -2, 1]) = -1
'''