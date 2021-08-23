#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""基数変換の例題プログラム
"""

__author__ = 'Taku Ikegami'
__version__ = '4.0.2'
__date__ = '2021/07/19 (Created: 2021/06/05)'

import sys
import doctest


def convert(number):
    """9より大きく36未満の数字をアルファベットに変換
    Args:
        number (int): 変換対象の整数
    Returns:
        10以上の数字をアルファベットに変換した値
    >>> convert(9)
    '9'
    >>> convert(10)
    'A'
    >>> convert(35)
    'Z'
    >>> convert(36)
    '36'
    """
    if 9 < number < 36:
        return chr(ord('A') + number - 10)

    return str(number)


def radix_conversion_from_dec(dividend, base_number):
    """10進数からn進数に変換（2から16進数まで）
    変換する際の途中式を全て出力する

    Args:
        dividend (int): 基数変換する対象
        base_number (int): 変換先の進数（2から16進数）
    >>> radix_conversion_from_dec(26, 17)
    2から16進数を指定してください
    >>> radix_conversion_from_dec(26, 1)
    2から16進数を指定してください
    >>> radix_conversion_from_dec(26, 2)
    26
    26 / 2 = 13 ・・・ 0
    13 / 2 = 6 ・・・ 1
    6 / 2 = 3 ・・・ 0
    3 / 2 = 1 ・・・ 1
    1 / 2 = 0 ・・・ 1
    11010
    >>> radix_conversion_from_dec(-26, 2)
    -26
    26 / 2 = 13 ・・・ 0
    13 / 2 = 6 ・・・ 1
    6 / 2 = 3 ・・・ 0
    3 / 2 = 1 ・・・ 1
    1 / 2 = 0 ・・・ 1
    -11010
    >>> radix_conversion_from_dec(0, 2)
    0
    0
    >>> radix_conversion_from_dec(26, 8)
    26
    26 / 8 = 3 ・・・ 2
    3 / 8 = 0 ・・・ 3
    32
    >>> radix_conversion_from_dec(26, 16)
    26
    26 / 16 = 1 ・・・ 10
    1 / 16 = 0 ・・・ 1
    1A
    >>> radix_conversion_from_dec(31, 16)
    31
    31 / 16 = 1 ・・・ 15
    1 / 16 = 0 ・・・ 1
    1F
    """

    # 引数チェック
    if not base_number in range(2, 17):
        print('2から16進数を指定してください')
        return

    # 基数変換対象が負の数の場合の処理
    print(dividend)
    flag=False
    if dividend<0:
        dividend=abs(dividend)
        flag=True

    # 整数部分の計算処理
    #quotient, remainder #商と余り

    result_list=[]

    while dividend:
        quotient, remainder =divmod(dividend,base_number)
        print('{} / {} = {} ・・・ {}'.format(dividend,base_number,quotient,remainder))
        result_list.append(convert(remainder))
        dividend=quotient
    if not result_list:
        result_list.append('0')

    # print('26 / 2 = 13 ・・・ 0')
    # print(num)
    # print(dividend)


    # 計算結果の出力処理
    # result_list[::-1]
    result="".join(result_list[::-1])
    if flag:
        result='-'+result

    print(result)
    return


def main():
    """例題プログラム

    Returns:
        int:
            結果（リターンコード：終了ステータス、0は正常終了）を応答する。
    """
    radix_conversion_from_dec(26, 17)
    radix_conversion_from_dec(26, 1)
    radix_conversion_from_dec(0, 2)
    radix_conversion_from_dec(26, 2)
    radix_conversion_from_dec(-26, 2)
    radix_conversion_from_dec(26, 8)
    radix_conversion_from_dec(26, 16)
    radix_conversion_from_dec(31, 16)

    # 結果（リターンコード：終了ステータス）を応答する。
    return 0


if __name__ == "__main__":
    # このスクリプトファイルが起動された時にだけ実行する部分
    # $ python このスクリプトファイル名

    # 単体テスト：モジュールのdocstringに記載されたすべての対話実行例が書かれている通りに動作するかを検証
    # $ python このスクリプトファイル名 -v
    # オプション -v がある時のみ実行される
    doctest.testmod()

    # main関数を呼び出して、結果（リターンコード：終了ステータス）を得て、その結果でPythonシステムを終了
    sys.exit(main())
