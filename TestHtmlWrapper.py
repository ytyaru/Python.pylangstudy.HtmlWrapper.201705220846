import unittest
import os.path
import HtmlWrapper
class TestHtmlWrapper(unittest.TestCase):
#    def __init__(self):
#        pass
    def test_CreateElement_html(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html')
        self.assertEqual(html, '<html></html>')

    def test_Wrap_html(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.Wrap(w.CreateElement('html'), w.CreateElement('body'))
        self.assertEqual(html, '<html><body></body></html>')

    def test_Wrap_nest3(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html')
        body = w.CreateElement('body')
        ul = w.CreateElement('ul')
        lis = ''
        for count in range(1, 4):
            lis += w.CreateElement('li', text_node_value='項目{0}'.format(count))
        ul = w.Wrap(ul, lis)
        body = w.Wrap(body, ul)
        html = w.Wrap(html, body)
        self.assertEqual(html, '<html><body><ul><li>項目1</li><li>項目2</li><li>項目3</li></ul></body></html>')

    def test_CreateElement_Attributes(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', lang='ja')
        self.assertEqual(html, '<html lang="ja"></html>')
    
    def test_CreateElement_Attributes_dict(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', **{'lang': 'ja'})
        self.assertEqual(html, '<html lang="ja"></html>')
    
    def test_CreateElement_Attributes_id_(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', id_='id1')
        self.assertEqual(html, '<html id="id1"></html>')
    
    def test_CreateElement_Attributes_class_(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', class_='cls1 cls2')
        self.assertEqual(html, '<html class="cls1 cls2"></html>')
    
    def test_CreateElement_Attributes_id_class_(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', id_='id1', class_='cls1 cls2')
        self.assertIn(html, ['<html id="id1" class="cls1 cls2"></html>', '<html class="cls1 cls2" id="id1"></html>'])
    
    def test_CreateElement_Attributes_id(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', **{'id': 'id1'})
        self.assertEqual(html, '<html id="id1"></html>')
    
    def test_CreateElement_Attributes_class(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', **{'class': 'cls1 cls2'})
        self.assertEqual(html, '<html class="cls1 cls2"></html>')
    
    def test_CreateElement_Attributes_id_class(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', **{'id': 'id1', 'class': 'cls1 cls2'})
        self.assertIn(html, ['<html id="id1" class="cls1 cls2"></html>', '<html class="cls1 cls2" id="id1"></html>'])
    
    def test_CreateElement_Attributes_id_id(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', id_='id1', **{'id': 'id2'})
        self.assertEqual(html, '<html id="id1"></html>')
        
    def test_CreateElement_Attributes_class_class(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', class_='cls1 cls2', **{'class': 'cls3 cls4'})
        self.assertEqual(html, '<html class="cls1 cls2"></html>')
    
    def test_CreateElement_Attributes_id_id_class_class(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', id_='id1', class_='cls1 cls2', **{'id': 'id2', 'class': 'cls3 cls4'})
        self.assertIn(html, ['<html id="id1" class="cls1 cls2"></html>', '<html class="cls1 cls2" id="id1"></html>'])

    def test_CreateElement_Attributes_dict(self):
        w = HtmlWrapper.HtmlWrapper()
        html = w.CreateElement('html', **{'id': 'id1', 'class': 'cls1 cls2', 'lang': 'ja'})
        self.assertIn(html, [
            '<html id="id1" class="cls1 cls2" lang="ja"></html>',
            '<html id="id1" lang="ja" class="cls1 cls2"></html>',
            '<html lang="ja" id="id1" class="cls1 cls2"></html>',
            '<html lang="ja" class="cls1 cls2" id="id1"></html>',
            '<html class="cls1 cls2" lang="ja" id="id1"></html>',
            '<html class="cls1 cls2" id="id1" lang="ja"></html>'
        ])
    
    def test_CreateElement_None(self):
        w = HtmlWrapper.HtmlWrapper()
        element_name = None
        with self.assertRaises(Exception) as e:
            html = w.CreateElement(element_name)
            self.assertEqual(e.msg, '要素名を指定してください。: element_name = {0}'.format(element_name))

    def test_CreateElement_blank(self):
        w = HtmlWrapper.HtmlWrapper()
        element_name = ''
        with self.assertRaises(Exception) as e:
            html = w.CreateElement(element_name)
            self.assertEqual(e.msg, '要素名を指定してください。: element_name = {0}'.format(element_name))

    def test_CreateElement_space(self):
        w = HtmlWrapper.HtmlWrapper()
        element_name = '    '
        with self.assertRaises(Exception) as e:
            html = w.CreateElement(element_name)
            self.assertEqual(e.msg, '要素名を指定してください。: element_name = {0}'.format(element_name))

