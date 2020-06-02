from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
  def sign_up(self):
    print("Sign up button pressed!")
    self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
  pass

class SignUpScreen(Screen):
  pass
  
class MainApp(App):
  def build(self):
    return RootWidget()

if __name__ == "__main__":
  MainApp().run()