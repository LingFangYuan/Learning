'''lxmld的XPath解析'''
from lxml import etree
 

html_str = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     <p class="title"><b id="b1">The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>
     <p class="story">...</p>
     """

html = etree.HTML(html_str)
#html = etree.parse('index.html')
result = etree.tostring(html)
print(result)
print(html.xpath('.//*[@class="sister"]/@href'))
