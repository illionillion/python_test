#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""フィボナッチ数列の例題プログラム
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2021/07/24 (Created: 2021/07/24)'

import sys
import doctest
import inspect
from functools import lru_cache



def print_result(arg, result):
    """フィボナッチ数列の計算結果を出力
    Args:
        arg (int): フィボナッチ数列の引数
        result (int): フィボナッチ数列の計算結果
    """

    function_name = inspect.stack()[1][3]
    print('{}({}) = {}'.format(function_name, arg, result))


def fibonacci_is(num):
    """フィボナッチ数列を計算する関数（反復スタイル：IS：Iteration Style）
    Args:
        num (int): 計算対象の整数
    Returns:
        フィボナッチ数列の計算結果
    >>> fibonacci_is(10)
    fibonacci_is(1) = 1
    fibonacci_is(2) = 1
    fibonacci_is(3) = 2
    fibonacci_is(4) = 3
    fibonacci_is(5) = 5
    fibonacci_is(6) = 8
    fibonacci_is(7) = 13
    fibonacci_is(8) = 21
    fibonacci_is(9) = 34
    fibonacci_is(10) = 55
    55
    """

    ## ここから作成

    result_list=[1,1]
    for index,result in enumerate(result_list):
        print_result(index+1,result)

    for index in range(2, num):

        result_list.append(result_list[index-2]+result_list[index-1])
        print_result(index+1,result_list[index])

    return result_list[num-1]

    # pass
    ## ここまでを作成

@lru_cache
def fibonacci_rs(num):
    """フィボナッチ数列を計算する関数（再帰スタイル：RS：Recursion Style）
    Args:
        num (int): 計算対象の整数
    Returns:
        フィボナッチ数列の計算結果
    >>> fibonacci_rs(10)
    fibonacci_rs(2) = 1
    fibonacci_rs(1) = 1
    fibonacci_rs(3) = 2
    fibonacci_rs(4) = 3
    fibonacci_rs(5) = 5
    fibonacci_rs(6) = 8
    fibonacci_rs(7) = 13
    fibonacci_rs(8) = 21
    fibonacci_rs(9) = 34
    fibonacci_rs(10) = 55
    55
    >>> fibonacci_rs.cache_clear()
    """

    ## ここから作成
    if num in (1,2):
        print_result(num,1)
        return 1

    result = fibonacci_rs(num-2) + fibonacci_rs(num-1)
    print_result(num,result)

    return result

    # pass
    ## ここまでを作成


def fibonacci_cps(num, function=lambda result: result):
    """フィボナッチ数列を計算する関数（継続渡しスタイル：CPS：Continuation Passing Style）
    Args:
        num (int): 計算対象の整数
    Returns:
        フィボナッチ数列の計算結果
    >>> fibonacci_cps(10)
    55
    """

    if num in (1, 2):
        return function(1)

    return fibonacci_cps(
        num - 1, lambda a: fibonacci_cps(num - 2, lambda b: function(a + b)))


def main():
    """例題プログラム

    Returns:
        int:
            結果（リターンコード：終了ステータス、0は正常終了）を応答する。
    """

    print('ISスタイル')
    fibonacci_is(10)

    print('RSスタイル')
    fibonacci_rs(10)

    print('CPSスタイル')
    print(fibonacci_cps(10))

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
