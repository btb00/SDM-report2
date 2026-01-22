#!/usr/bin/python3
import re

def calc(A,B):
        # 1. 整数かどうかチェック (isinstanceを使用)
        # 仕様: 誤って整数以外の文字列等が入力された場合にも、出力Cに-1を返す
        if not isinstance(A, int) or not isinstance(B, int):
                return -1
        
        # 2. 範囲チェック (1〜999)
        # 仕様: 1から999までの整数
        if not (1 <= A <= 999) or not (1 <= B <= 999):
                return -1
        
        # 3. 計算実行
        return A * B
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()