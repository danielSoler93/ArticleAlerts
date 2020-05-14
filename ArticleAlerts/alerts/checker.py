from . import custom_errors as ce

class Checker:

    def __init__(self, html):
        self.html = html

    def check(self):
        self.check_html()

    def check_html(self):
        if "cuando Google detecta" in self.html:
            raise ce.MaxRequests("You reach the maximum request per day to googleschoolar. Please try the script a bit later")