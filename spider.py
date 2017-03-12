#coding:utf-8

import url_manager, html_parser, html_downloader, html_outputer
import time

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print count, new_url

                if count > 20:
                    break
                count += 1

            except Exception, e:
                print e
                print "crawl fail"

        self.outputer.output_html()

if __name__ == "__main__":
    start = time.time()
    root_url = "http://baike.baidu.com/view/21087.htm"
    object_spider = Spider()
    object_spider.crawl(root_url)
    end = time.time()
    print "const all time: %s" % (end-start)


