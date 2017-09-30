from icrawler.builtin import GoogleImageCrawler
import sys

search_term = sys.argv[1]
folder_name = sys.argv[2]


google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': folder_name})


google_crawler.crawl(keyword=search_term, max_num=100,
                     date_min=None, date_max=None,
                     min_size=(640,480), max_size=None)
