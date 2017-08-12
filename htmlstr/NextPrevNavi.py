#!python3
#encoding: utf-8
import HtmlWrapper
class NextPrevNavi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
    
    """
    前後ナビのHTML文字列を生成する。
    "<前 次>"のパターンのみ。
    @param {str} prevは左または上に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    @param {str} nextは右または下に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    """
    def CreateHtml(self, prev, next):
        if not prev or not next:
            raise Exception("引数エラー1。prev, nextは`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
        if not 'text' in prev or not 'href' in prev or not 'text' in next or not 'href' in next:
            raise Exception("引数エラー2。prev, nextは`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
        if not prev['text'] or not prev['href'] or not next['text'] or not next['href']:
            raise Exception('引数エラー3。prev, nextの各キーに値を指定してください。')
        return self.__wrapper.Wrap(self.__CreateInnerHtml(prev, next), 'ul', id_='NextPrevNavi')
    
    """
    パンくずリストのHTML文字列を生成するためにdict引数を分解して内部メソッドに渡す。
    @param {str} prevは左または上に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    @param {str} nextは右または下に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    """
    def __CreateInnerHtml(self, prev, next):
        is_left = True
        li_str = ''
        for data in (prev, next):
            text_node_value, attrs = self.__SplitTextNodeAndAttributes(data)
            li_str += self.__wrapper.Wrap(
                self.__AppendDirectionalIcon(
                    is_left, 
                    self.__wrapper.CreateElement('a', text_node_value=text_node_value, **attrs)
                ), 'li')
            is_left = not(is_left)
        return li_str
    
    def __SplitTextNodeAndAttributes(self, data):
        text_node_value = data['text']
        del data['text']
        return (text_node_value, data)
    
    def __AppendDirectionalIcon(self, is_left, a_str):
        if is_left:
            a_str = self.__CreateDirectionalIcon(is_left=is_left) + a_str
        else:
            a_str += self.__CreateDirectionalIcon(is_left=is_left)
        return a_str
    
    def __CreateDirectionalIcon(self, is_left=False):
        if self.__directional_icon_type == "FontAwesome":
            return self.__CreateDirectionalIcon_FontAwesome(is_left)
        else:
            return self.__CreateDirectionalIcon_Character(is_left)
    
    def __CreateDirectionalIcon_FontAwesome(self, is_left=False):
        if is_left:
            return '<i class="fa fa-angle-left" aria-hidden="true"></i>'
        else:
            return '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    
    def __CreateDirectionalIcon_Character(self, is_left=False):
        text_node_value = ''
        if is_left:
            text_node_value = '&lt;'
        else:
            text_node_value = '&gt;'
        return self.__wrapper.CreateElement('span', text_node_value=text_node_value, class_='DirectionalIcon')


if __name__ == '__main__':
    n = NextPrevNavi()
    html = n.CreateHtml(
        prev={'text': '前のページ', 'href': 'http://prev'},
        next={'text': '次のページ', 'href': 'http://next'})
    print(html)

