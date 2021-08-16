#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""お釣りの計算プログラム
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.0'
__date__ = '2021/07/07 (Created: 2021/07/07)'

import sys
import doctest


def change_print(product_price, amount):
    """お釣りを計算して画面にお釣りの枚数を表示
    引数が整数（int）でない場合は、それ以上処理をしない

    Args:
        product_price (int): 商品の値段
        amount (int)： 支払った金額
    >>> change_print(1120, 10000)
    商品の値段：1120
    支払った金額：10000
    お釣りの金額：8880
    <内訳>
    5000：1
    1000：3
    500：1
    100：3
    50：1
    10：3
    5：0
    1：0
    >>> change_print(100, 100)
    商品の値段：100
    支払った金額：100
    お釣りはありません
    >>> change_print(1000, 100)
    商品の値段：1000
    支払った金額：100
    金額が足りません：900
    >>> change_print('1000', 100)
    引数が不正です
    >>> change_print(1000, '100')
    引数が不正です
    """

    ### ここを作成

    for arg in (product_price,amount):
        if not isinstance(arg,int):
            print('引数が不正です')
            return

    change=amount-product_price#おつり
    print('商品の値段：{}'.format(product_price))
    print('支払った金額：{}'.format(amount))

    if change<0:
        print('金額が足りません：{}'.format(-change))
        return

    if change==0:
        print('お釣りはありません')
        return

    print('お釣りの金額：{}'.format(change))
    print('<内訳>')

    for money in (5000,1000,500,100,50,10,5,1):
        num,change=divmod(change,money)#商と余りをまとめて計算する
        print('{}：{}'.format(money,num))

    ### ここまでを作成
    return




def main():
    """お釣りの計算プログラムの問題

    Returns:
        int:
            結果（リターンコード：終了ステータス、0は正常終了）を応答する。
    >>> main()
    商品の値段：1120
    支払った金額：10000
    お釣りの金額：8880
    <内訳>
    5000：1
    1000：3
    500：1
    100：3
    50：1
    10：3
    5：0
    1：0
    商品の値段：100
    支払った金額：100
    お釣りはありません
    商品の値段：1000
    支払った金額：100
    金額が足りません：900
    引数が不正です
    引数が不正です
    0
    """

    change_print(1120, 10000)
    change_print(100, 100)
    change_print(1000, 100)
    change_print('1000', 100)
    change_print(1000, '100')

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
