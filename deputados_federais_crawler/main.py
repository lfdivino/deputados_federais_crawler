from scrapy import cmdline
cmdline.execute("scrapy crawl congressmen -o congressmen_data.json".split())
