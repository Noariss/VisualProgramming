from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.theming import ThemeManager
from kivy.uix.label import Label


class Input(BoxLayout):
	def save(self):
		MyFile = open('e:/test.txt', 'a+') #запись в файл с инпута
		written = str(self.vvod.text)
		written = written + '\n'
		MyFile.write(written)

class Output(BoxLayout):
	def saveout(self): #запись в файл с выводом
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.vivod.text)
		written = "print(" + written + ")\n"
		MyFile.write(written)

class Chicl(BoxLayout): #запись в файл for i in range()
	def add_chicl(self):
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.chicl.text)
		written = 'for i in range(' + written + '):\n'
		MyFile.write(written)

class ChiclAfter(BoxLayout): # действие в цикле
	def chiclsave(self):
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.chiclafter.text)
		written = "    "  + written + '\n'
		MyFile.write(written)

class Choice(BoxLayout):
	def choice_add(self): # запись в файл условия
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.choice.text)
		written = "if " + written + ":\n"
		MyFile.write(written)


class ChoiceAfter(BoxLayout):
	def choice_yes(self): # запись условия +
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.yes.text)
		written = "    " + written + "\n"
		MyFile.write(written)

	def choice_no(self): # запись условия -
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.no.text)
		MyFile.write('else:\n')
		written = "    " + written + "\n"
		MyFile.write(written)

class Action(BoxLayout):
	def give_action(self): #запись действия
		MyFile = open('e:/test.txt', 'a+')
		written = str(self.action.text)
		written = written + "\n"
		MyFile.write(written)


class Container(BoxLayout):
	square = ObjectProperty()
	def add_button1(self): #создание инпута
		self.space.add_widget(Input())

	def add_button2(self): #создание вывода
		self.space.add_widget(Output())

	def add_button3(self): #создание цикла
		self.space.add_widget(Chicl())
		self.space.add_widget(ChiclAfter())
	def add_button4(self): #создание выбора
		self.space.add_widget(Choice())
		self.space.add_widget(ChoiceAfter())
	def add_button5(self): #создание действия
		self.space.add_widget(Action())
	def show_result(self): #показ результатов
		MyFile = open('e:/test.txt', 'r')
		result = MyFile.read()
		self.results.text = result

class ProjectApp(App):
	theme_cls = ThemeManager()
	title = 'Project'
	def build(self):
		self.theme_cls.theme_style = 'Light'
		return Container()	

if __name__ == "__main__": #просто запуск
	ProjectApp().run()	