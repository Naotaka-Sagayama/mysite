import this #パイソニスタの心得

help("keywords")    #pythonでの予約文字（変数名として使用不可）を表示

#Pythonでは変数自体はデータ型をもたず、メモリも固定されず、ただの参照手段である
#そのためPythonでは型宣言をせずに使用可能
x = 5
y = x + 12.0
print(type(x), x, type(y), y)

#複数の変数名に代入可能
#このときすべての変数は'2'のオブジェクトを参照している
two = deux = zwei = 2
print(two, deux, zwei)
two = 2.0   #'two'のみ参照先を変更
print(two, deux, zwei)

#listはミュータブルなオブジェクトである
#list aを変更するとlist bまで変更されている
a = [2, 4, 6]
b = a
print(type(a), a, type(b), b)
a[0] = 99
print(a, b)