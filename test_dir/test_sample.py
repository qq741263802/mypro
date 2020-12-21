import os
import seldom
from seldom import file_data
CASE_DIR = os.path.dirname(os.path.abspath(__file__))
# data file path
YAML_FILE = os.path.join(CASE_DIR, "data.json")


class SampleTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.get("http://www.itest.info")
        self.assertInUrl("itest.info")


class BaiduTest(seldom.TestCase):

    @file_data(file=YAML_FILE, key="baidu")
    def test_data_driver(self, _, keyword):
        """ data driver case """
        self.get("https://www.baidu.com")
        self.type(id_="kw", text=keyword)
        self.click(css="#su")
        self.assertInTitle(keyword)


if __name__ == '__main__':
    seldom.main(debug=True)

