import requests
import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
self.browser.open(url)
self.browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
self.browser.form['email'] = YourLogin
self.browser.form['pass'] = YourPassw
response = self.browser.submit()



###

form = "https://www.facebook.com/ads/lead_gen/export_csv/?id=254886885252436&type=form&source_type=graph_api"

data = requests.get(form)

with open("df/lunarena123.csv", "wb") as f:
    f.write(data.content)
