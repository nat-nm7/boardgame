'''
グレート・ウエスタン・トレイルランダムタイル配置生成ツール

Created on 2021/12/10
@author: なっと
'''
import random

print("こんにちは！GWTランダムタイル配置生成ツールです。")
print()
print("・私有建物タイル")
for i in range(1, 13):
    # 0か1の乱数を生成
    flag = random.randint(0, 1)
    # 出力
    if i < 10:
        print(' ', end='')
    if flag:
        print(f'{i}a', end='  ')
    else:
        print(f'{i}b', end='  ')
    if i == 6 or i == 12:
        print()

print()
print("・共有建物タイル")
# AからGを内包するリストを作成
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# リストをシャッフル
random.shuffle(tiles)
# 出力
for i in range(7):
    print(tiles[i], end='')
print()
print()
print('以上')