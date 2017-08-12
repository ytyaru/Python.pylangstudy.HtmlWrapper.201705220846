#!python3
#encoding: utf-8
import HtmlWrapper
import Breadcrumbs
import MetaNavi
import NextPrevNavi
class HeaderNavi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
        
    def CreateHtml(self):
        return self.__CreateHeaderNavi() + '\n\n' + self.__CreateNextPrevNavi()
        
    def __CreateHeaderNavi(self):
        b = Breadcrumbs.Breadcrumbs()
        m = MetaNavi.MetaNavi()
        breadcrumbs = b.CreateHtml([
            {'text': '孫', 'href': 'http://2'},
            {'text': '子', 'href': 'http://1'},
            {'text': '親', 'href': 'http://0'}], is_child_first=True)
        metaNavi = m.CreateHtml(
            {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
            {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
            {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'})
        headerNavi = self.__wrapper.Wrap(breadcrumbs + metaNavi, 'div', id_='HeaderNavi')
        return headerNavi
        
    def __CreateNextPrevNavi(self):
        n = NextPrevNavi.NextPrevNavi()
        return n.CreateHtml(
            {'text': '前のページ', 'href': 'http://prev'},
            {'text': '次のページ', 'href': 'http://next'})


if __name__ == '__main__':
    n = HeaderNavi()
    html = n.CreateHtml()
    print(html)

