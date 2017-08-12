#!python3
#encoding: utf-8
import os.path
class Includer(object):
    def __init__(self):
        self.__text = None
        self.__num_lines = 0
        
    """
    指定ファイルパスの指定行数を取得する。
    @param {str} pathは読み取りたいファイルのパス。
    @param {tuple} linesは読み取りたいファイルの行数。(start,end)           ((start,end),(start,end),(start,end),...)
    行数の書式は以下のパターンがある。
    [3:5] 3〜5行目の間のみ
    [3:] 3行目から末尾行まで
    [:5] 1行目から5行目までの間のみ
    [3:-1] 3行目から末尾行-1行目の間まで
    [:-5] 1行目から末尾行-5行目の間まで
    [-5:] 末尾行-5行目から末尾行まで
    [-5:-2] 末尾行-5行目から末尾行-2行目まで
    (未記入) ファイル内容すべて
    以下、エラーの場合。
    * 左辺値 < 右辺値（正数,負数問わず）
    * 左辺値と右辺値に-と数字以外の文字がある
    * 区切り文字:がない
    tupleにするときは以下のようにする。
    * 空値は`0`で代用する。必ず(start,end)の形とする
    """
    def Include(self, path, lines=None):
        self.__CheckLines(lines)
        self.__OpenFile(path)
        return self.__ReadFile(self.__AbsoluteLines(lines))
        
    def __CheckLines(self, lines):
        if lines and 2 != len(lines):
            raise Exception('引数linesはlist型で[start, end]の2つの整数値を指定してください。')
        if lines and (not isinstance(lines[0], int) or not isinstance(lines[1], int)):
            raise Exception('引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。')
            
    def __OpenFile(self, path):
        if not os.path.isfile(path):
            raise Exception('Includeしたいファイルが存在しません。: {0}'.format(path))
        with open(path) as f:
            self.__text = f.read()
#            print(self.__text)
            self.__num_lines = sum(1 for line in open(path))
#            print(self.__num_lines)
    
    def __AbsoluteLines(self, lines):
        # 両方とも0なら全体を取得する
        if None is lines or (0 == lines[0] and 0 == lines[1]):
            return None
        if 0 == lines[0]:
            lines[0] = 1
        if 0 == lines[1]:
            lines[1] = self.__num_lines
        # 負数なら絶対行数に変換する
        for i, line in enumerate(lines):
            if line < 0:
                lines[i] = self.__num_lines + line
        if lines[1] < lines[0]:
            raise Exception('引数linesは 左辺値 <= 右辺値 である必要があります。')
        return lines
    
    def __ReadFile(self, lines):
        if not lines:
            return self.__text
        select_text = ''
        count = 0
        for line in self.__text.split('\n'):
            count += 1
            if count < lines[0] or lines[1] < count:
                continue
            select_text += line + '\n'
        return select_text[:-1]


if __name__ == '__main__':
    c = Includer()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
    lines = [3, 6]
#    lines = [0, 0]
#    lines = None
#    lines = [0, -5]
#    lines = [-5, 0]
#    lines = [5, 2] # Exception: 引数linesは 左辺値 <= 右辺値 である必要があります。
#    lines = [5, -2]
#    lines = [-5, 2] # Exception: 引数linesは 左辺値 <= 右辺値 である必要があります。
#    lines = [-7, -2]
#    lines = [-7] # Exception: 引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。
#    lines = [None, None] # Exception: 引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。
    print(c.Include(path, lines=lines))

