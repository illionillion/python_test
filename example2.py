#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
print関数の例題
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.0'
__date__ = '2021/06/19 (Created: 2021/06/19)'

print(__author__)

# モジュールをインポート（モジュールを使用できるように）
import sys
import doctest


def main():
    """
    print関数の実行例
    >>> main()
    Hello world!
    Hello world!
    Hello world!
    Hello,world!
    100 [1, 2, 3] (1, 2, 3)
    0
    """

    # 文字列の出力
    print('Hello world!')

    text1 = 'Hello'
    text2 = 'world!'

    # 終端の変更（改行の変更）
    print(text1, end=' ')
    print(text2)

    # 変数を複数出力（スペース区切り）
    print(text1, text2)

    # 変数を複数出力（カンマ区切り）
    print(text1, text2, sep=',')

    # 文字列以外を出力（数値、リスト、タプル）
    num = 100
    num_list = [1, 2, 3]
    num_tuple = (1, 2, 3)
    print(num, num_list, num_tuple)

    # return文を用いて関数の実行結果を呼び出し元に返す（戻り値）
    # 今回は結果（リターンコード：終了ステータス、0は正常終了）を応答する。
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

print(__name__)