# -*- coding: utf-8 -*-
import os
import sys
import unittest
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
sys.path.insert(0, BASE_DIR + '/spiders')

from ozodlik_spider1 import OzodlikSpider
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request, TextResponse, Response, HtmlResponse



class OzodlikTestCase(unittest.TestCase):

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + str(self.shortDescription()) + "]")
        self.spider = OzodlikSpider()
        self.testfile = open('features_ozodlik_1.html', errors='ignore')
        self.testdata = self.testfile.read()

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + str(self.shortDescription()) + "]")
        print("")
        self.testfile.close()

    def test_upper(self):
        """Uppercase operation test"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Uppercase assertTrue/assertFalse test"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Split operation test"""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def _test_item_results(self, results, expected_length):
        count = 0
        for item in results:
            if not self.assertIsNotNone(item['title']):
                count += 1
        self.assertEqual(count, expected_length)

    def fake_response(self, file_name=None):
        request = Request(url='http://www.example.com')
        return HtmlResponse(
            url='http://www.example.com',
            request=request,
            body=self.testdata,
            encoding='utf-8'
        )

    def online_response(self, url=None):
        request = Request(url=url)
        return HtmlResponse(
            url=url,
            request=request,
            body=requests.get(url).text,
            encoding='utf-8'
        )

    def test_file_parse(self):
        """Parse fake response test"""
        print("id: " + self.id())
        results = self.spider.parse(self.fake_response(file_name='features_ozodlik_1.html'))
        self._test_item_results(results, 10)

    def test_requests_parse(self):
        """Parse requests test"""
        print("id: " + self.id())
        results = self.spider.parse(self.online_response(url='https://www.rferl.org/s?k=USA&tab=all&pi=1&r=any&pp=10'))
        self._test_item_results(results, 10)

    def str_par(self):
        return 'This is a monkey function'

    def test_monkey(self):
        """Monkey patching"""
        print("id: " + self.id())
        self.spider.parse = self.str_par
        results = self.spider.parse()
        self.assertEqual(results, 'This is a monkey')


if __name__ == '__main__':
    unittest.main()
