import rumps
import string, random
import pyperclip


class PyPasswordApp(object):
    def __init__(self):
        self.all_char = string.ascii_letters + string.digits + "!#$%&*@"
        self.password = ""
        self.config = {
            "app_name": "pyPassword",
            "generate": "Generate a new password",
            "settings": "Settings",
            "password_length": 12,
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.generate_password_button = rumps.MenuItem(title=self.config["generate"], callback=self.get_new_password)
        self.settings_button = rumps.MenuItem(title=self.config["settings"], callback=None)
        self.app.menu = [self.generate_password_button, self.settings_button]

    def set_up_menu(self):
        self.app.title = "🍙"
        self.password = ""

    def get_new_password(self, sender):
        self.set_up_menu()

        for index in range(self.config["password_length"]):
            self.password = self.password + random.choice(self.all_char)
        print("Password generated: {}".format(self.password))
        pyperclip.copy(self.password)



    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = PyPasswordApp()
    app.run()