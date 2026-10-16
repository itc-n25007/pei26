animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0

print(f'totalの値は{total}') # 繰り返し処理の開始前に、totalの初期値を表示する

for animal in animals: # animalsから動物の名前を1つずつ取り出して繰り返す
    from_D = animal.startswith('D')  # 動物の名前が'D'で始まるか確認する
    is_long = len(animal) > 5  # 動物の名前が6文字より長いか確認する
    if from_D and is_long:   # 'D'で始まり、かつ6文字より長い場合は繰り返しを終了する
        break
    elif not from_D and is_long: # 'D'で始まらず、かつ6文字より長い場合
        total += animal.find('b') # 文字列の中で'b'が最初に現れる位置をtotalに加算する
    else:
        total += len(animal)   # 動物の名前の文字数をtotalに加算する

    print(f'totalの値は{total}')# 1回の繰り返し処理が終わるたびにtotalを表示する
    
print(total) 

    