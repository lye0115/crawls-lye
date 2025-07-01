# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        txt_file_path = os.path.join(os.path.dirname(__file__),'assets/douban250.txt')
        with open(txt_file_path, 'a', encoding='utf-8') as f:
            # f.write(str(item)+'\n')
            f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

