#coding:utf-8

from bs4 import BeautifulSoup
import urlparse, re

class HtmlParser(object):
    def parse(self, page_url, content):
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        urls = self._get_new_urls(page_url, soup)
        data = self._get_new_data(page_url, soup)
        return urls, data

    def _get_new_urls(self, page_url, soup):
        new_urls = []
        links = soup.find_all('a', href=re.compile(r"view/\d+\.(html|htm)"))
        for link in links:
            url = link['href']
            url = urlparse.urljoin(page_url, url)
            new_urls.append(url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        data['summary'] = summary_node.get_text()
        data['url'] = page_url
        return data
