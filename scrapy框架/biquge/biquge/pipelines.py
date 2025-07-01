# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter



class BiqugePipeline:
    def process_item(self, item, spider):
        dir_path = os.path.dirname(os.path.abspath(__file__),'..','assets')
        with open(os.path.join(dir_path,f'{item["title"]}.txt'), 'a', encoding='utf-8') as f:
            f.write(item['content'] + '\n')
        return item
