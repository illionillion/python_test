#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
printの練習問題
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.0'
__date__ = '2021/06/23 (Created: 2021/06/23)'

# モジュールをインポート（モジュールを使用できるように）
import doctest


def practice1():
    """
    練習問題1

    printメソッドを1つ用いて
    doctestでエラーがでないようにすること

    >>> practice1()
    090-5132-1996
    """

    text1 = '090'
    text2 = '5132'
    text3 = '1996'

    # ここにprintを1行書く
    print(text1,text2,text3,sep="-")

def practice2():
    """
    練習問題2

    printメソッドを3つ用いて
    doctestでエラーがでないようにすること

    >>> practice2()
    090-5132-1996
    """

    text1 = '090'
    text2 = '5132'
    text3 = '1996'

    # ここにprintを3行書く
    print(text1,end="-")
    print(text2,end="-")
    print(text3)

if __name__ == "__main__":

    # 練習問題1
    practice1()

    # 練習問題2
    practice2()

    doctest.testmod()
