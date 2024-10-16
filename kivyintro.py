import kivy
import mysql.connector as ms
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

mycon=ms.connect(host='localhost' , user='root' , passwd='12345678' , database='appdev')
mycursor=mycon.cursor()
class spartangrid(GridLayout):
    def __init__(self,**kwargs):
        super(spartangrid,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Student name::"))
        self.s_name=TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student class::"))
        self.s_class=TextInput(multiline=False)
        self.add_widget(self.s_class)

        self.add_widget(Label(text="Student section::"))
        self.s_sec=TextInput(multiline=False)
        self.add_widget(self.s_sec)

        self.press=Button(text="submit")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        query=f"insert into collegedata values( '{self.s_name.text}','{self.s_class.text}' ,'{self.s_sec.text}')"
        mycursor.execute(query)
        mycon.commit()


    
class Spartanapp(App):   
    def build(self):
        return spartangrid()

if __name__=="__main__":
    Spartanapp().run()