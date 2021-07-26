#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
Pythonコードの構造について

Pythonでは、分岐、ループ、関数、クラスなどのコード上の
論理的なブロックは　:（コロン）以降の行にインデントをつけることで表現する。
PEP8では半角スペース4つが推奨されている。
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.0'
__date__ = '2021/06/19 (Created: 2021/06/19)'

# モジュールをインポート（モジュールを使用できるように）
import sys
import doctest


def main():
    """
    ダブルクォート3つでdocstringとなる
    ここには関数の説明を記述する
    >>> main()
    Hello world!
    1
    2
    3
    numは2より大きいです
    0
    """

    # 1行のコメントには#を使用
    # 通常の文と同様にインデントを合わせる必要がある
    print('Hello world!')

    # if文ではインデントする
    num = 100
    if num > 100:
        print('100より大きいです。')

    # for文でもインデントします
    num_list = [1, 2, 3]
    for num in num_list:
        # ブロック内部ではコメントもインデントする
        print(num)

        # 入れ子の場合はその文のインデントを追加する
        if num > 2:
            print('numは2より大きいです')

    # インデント内部に処理がない場合はpassを記述
    for num in num_list:
        # passは何もしない文
        pass

    # return文を用いて関数の実行結果を呼び出し元に返す（戻り値）
    # 今回は結果（リターンコード：終了ステータス、0は正常終了）を応答する。
    return 0


if __name__ == "__main__":#__name__ってどこ？

    # このスクリプトファイルが起動された時にだけ実行する部分
    # $ python このスクリプトファイル名

    # 単体テスト：モジュールのdocstringに記載されたすべての対話実行例が書かれている通りに動作するかを検証
    # $ python このスクリプトファイル名 -v
    # オプション -v がある時のみ検証される（オプションがない場合は検証されない）
    doctest.testmod()

    # main関数を呼び出して、結果（リターンコード：終了ステータス）を得て、その結果でPythonシステムを終了
    sys.exit(main())