import re
from urllib.request import urljoin
from bs4 import BeautifulSoup


class HtmlParser:

    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容， 抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return:
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'/item/.+'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回有效数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text() if title is not None else ''
        summary = soup.find('div', class_='lemma-summary')
        # 获取tag中包含的所有文本内容， 包括子孙tag中的内容， 并将结果作为字符串返回
        data['summary'] = summary.get_text() if summary is not None else ''

        return data
