#!python3
#encoding: utf-8
import urllib.parse
import HtmlWrapper
class MetaNavi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
    
    """
    Python学習サイトにおける記事のメタデータHTML文字列を生成する。
    Python文書、環境構築、リポジトリ、のURL。
    @param {str} pydocは左または上に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    @param {str} githubは右または下に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    """
    def CreateHtml(self, pydoc, env, github):
        for param in (pydoc, env, github):
            if not param:
                raise Exception("引数エラー1。引数は`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
            if not 'text' in param or not 'href' in param:
                raise Exception("引数エラー2。引数は`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
            if not param['text'] or not param['href']:
                raise Exception('引数エラー3。引数の各キーに値を指定してください。')
        return '<span id="MetaNavi">' + self.__CreatePyDocLink(pydoc) + ' | ' + self.__CreateEnvLink(env) + ' | ' + self.__CreateGithubLink(github) + '</span>'
    
    def __CreatePyDocLink(self, pydoc):
        return self.__wrapper.Wrap(
            self.__wrapper.CreateElement('img', src=self.__CreatePythonIconBase64(), width="16px", height="16px"),
            'a', text_node_value=pydoc['text'], href=pydoc['href'], title=urllib.parse.urlparse(pydoc['href']).netloc)

    def __CreatePythonIconBase64(self):
        return "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMSBUaW55Ly9FTicgICdodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS10aW55LmR0ZCc+PHN2ZyBiYXNlUHJvZmlsZT0idGlueSIgaGVpZ2h0PSI1MTJweCIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjUxMnB4IiB4bWw6c3BhY2U9InByZXNlcnZlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48ZyBpZD0iTGF5ZXJfNyI+PGc+PHBhdGggZD0iTTI1My44MDYsMS43ODNjLTIwLjY3OCwwLjA5OC00MC40MjYsMS44NTktNTcuODAzLDQuOTM1Yy01MS4xODcsOS4wNDQtNjAuNDgsMjcuOTctNjAuNDgsNjIuODc3djQ2LjEwMyAgICBoMTIwLjk2M3YxNS4zNjZIMTM1LjUyMkg5MC4xMjZjLTM1LjE1NSwwLTY1LjkzNywyMS4xMy03NS41NjMsNjEuMzI1Yy0xMS4xMDcsNDYuMDc1LTExLjYwMyw3NC44MywwLDEyMi45MzkgICAgYzguNTk5LDM1LjgwOCwyOS4xMyw2MS4zMjQsNjQuMjg2LDYxLjMyNGg0MS41ODl2LTU1LjI2OWMwLTM5LjkyMSwzNC41NDQtNzUuMTQzLDc1LjU2NC03NS4xNDNoMTIwLjgyMiAgICBjMzMuNjMyLDAsNjAuNDc5LTI3LjY4OSw2MC40NzktNjEuNDY2VjY5LjU5NGMwLTMyLjc3Ni0yNy42NTMtNTcuNDA2LTYwLjQ3OS02Mi44NzdDMjk2LjA0NSwzLjI1NywyNzQuNDgzLDEuNjg0LDI1My44MDYsMS43ODN6ICAgICBNMTg4LjM5MSwzOC44NmMxMi40OTQsMCwyMi42OTksMTAuMzcsMjIuNjk5LDIzLjEyYzAsMTIuNzA1LTEwLjIwNSwyMi45ODItMjIuNjk5LDIyLjk4MmMtMTIuNTQyLDAtMjIuNjk5LTEwLjI3Ny0yMi42OTktMjIuOTgyICAgIEMxNjUuNjkyLDQ5LjIzLDE3NS44NDksMzguODYsMTg4LjM5MSwzOC44NnoiIGlkPSJwYXRoMTk0OF8xXyIvPjxwYXRoIGQ9Ik0zOTIuMzg3LDEzMS4wNjJ2NTMuNzEyYzAsNDEuNjQ4LTM1LjMwMyw3Ni42OTItNzUuNTYyLDc2LjY5MkgxOTYuMDAyICAgIGMtMzMuMDk0LDAtNjAuNDgsMjguMzI3LTYwLjQ4LDYxLjQ2OXYxMTUuMTg2YzAsMzIuNzc3LDI4LjUwMyw1Mi4wNjMsNjAuNDgsNjEuNDYzYzM4LjI5MSwxMS4yNTksNzUuMDA0LDEzLjMsMTIwLjgyMiwwICAgIGMzMC40NTEtOC44MTIsNjAuNDc5LTI2LjU2MSw2MC40NzktNjEuNDYzdi00Ni4xMDVIMjU2LjQ4NXYtMTUuMzY0aDEyMC44MTdoNjAuNDc5YzM1LjE1NywwLDQ4LjI2LTI0LjUxOSw2MC40ODItNjEuMzI0ICAgIGMxMi42MjktMzcuODk1LDEyLjA5My03NC4zMzUsMC0xMjIuOTM5Yy04LjY4Ny0zNC45OTMtMjUuMjgxLTYxLjMyNS02MC40ODItNjEuMzI1SDM5Mi4zODd6IE0zMjQuNDM4LDQyMi43NSAgICBjMTIuNTM5LDAsMjIuNjk4LDEwLjI2OSwyMi42OTgsMjIuOTc1YzAsMTIuNzQ5LTEwLjE1OSwyMy4xMjQtMjIuNjk4LDIzLjEyNGMtMTIuNDkzLDAtMjIuNjk2LTEwLjM3NS0yMi42OTYtMjMuMTI0ICAgIEMzMDEuNzQxLDQzMy4wMTksMzExLjk0NCw0MjIuNzUsMzI0LjQzOCw0MjIuNzV6IiBpZD0icGF0aDE5NTBfMV8iLz48L2c+PC9nPjwvc3ZnPg=="

    def __CreateEnvLink(self, env):
        return self.__wrapper.Wrap(
            '<i class="fa fa-television" aria-hidden="true"></i>',
            'a', href=env['href'], title=env['text'])
        
    def __CreateGithubLink(self, github):
        return self.__wrapper.Wrap(
            '<i class="fa fa-github" aria-hidden="true"></i>',
            'a', text_node_value=github['text'], href=github['href'], title=urllib.parse.urlparse(github['href']).netloc)


if __name__ == '__main__':
    m = MetaNavi()
    html = m.CreateHtml(
        {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
        {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
        {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'})
    print(html)

