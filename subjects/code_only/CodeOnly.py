#!python3
#encoding: utf-8
import HtmlWrapper
import HeaderNavi
#import Breadcrumbs
#import MetaNavi
import NextPrevNavi
class HeaderNavi(object):
    def __init__(self):
        nav_head = HeaderNavi.HeaderNavi(directional_icon_type='FontAwesome')
        nav_next = NextPrevNavi.NextPrevNavi()
    def CreateHtml(self):
        return self.__CreateHeaderNavi() + '\n\n' + self.__CreateNextPrevNavi()

