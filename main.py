#matplotlib 
#図形を書くためのライブラリ

import matplotlib.pyplot as plt

result = [100,200,400,250,500]
number = [1,2,3,4,5]

#グラフを書く
plt.plot(number,result)

#グラフのタイトル
plt.title("result / number")

#x軸のラベル
plt.xlabel("number")

#y軸のラベル
plt.ylabel("result")

#表示する
plt.show()