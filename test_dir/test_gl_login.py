import os,time
import seldom
from seldom import testdata

class Login(seldom.TestCase):


    def test_login(self):
        self.open("http://124.172.188.110:31907/#/")
        self.type(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div/div/input',text="gree")
        self.type(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[2]/div/div/div/input',text="abcd4321")
        self.click(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[3]/div/button')
        self.click(xpath='//*[@id="app"]/section/section/div/div[1]/div[1]/div/ul/div[2]/li/div/span')
        self.click(xpath='//*[@id="app"]/section/section/div/div[1]/div[1]/div/ul/div[2]/li/ul/li[1]/span')
        self.type(xpath='//*[@id="app"]/div/div[2]/div[1]/div/form[1]/div[1]/div/div/input',
                  text="SP1000247")
        self.click(xpath='//*[@id="app"]/div/div[2]/div[1]/div/form[1]/div[7]/div/button[1]')
        self.assertText('SP1000247')
        time.sleep(3)






if __name__ == '__main__':
    seldom.main(debug=True)