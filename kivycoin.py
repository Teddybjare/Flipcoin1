from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import random


class coin(App):
    def build(self):
        self.game = 0
        self.counter1 = 0
        self.counter2 = 0
        layout1 = BoxLayout(orientation="vertical")
        layout2 = BoxLayout(orientation="vertical")
        layout3 = BoxLayout(orientation="horizontal")
        layout4 = BoxLayout(orientation = "vertical")
        self.good_toss = Label(text = "0", color = "green", font_size = 40)
        self.bad_toss = Label(text = "0", color = "red", font_size = 40)
        choose_heads = Button(text="heads")
        choose_tails = Button(text="tails")
        self.result = Button(text="result", font_size = 50)
        self.guess = 0
        self.coinresult = 0
        if self.coinresult == 1:
            self.coinresult ='heads.png'
            self.result.text = "heads"
        elif self.coinresult == 2:
            self.coinresult = 'tails.png'
            self.result.text = "tails"
        self.resultimgage = Image()
        if self.coinresult != 0:
            self.resultimgage = Image(source = self.coinresult)
        layout4.add_widget(self.good_toss)
        layout4.add_widget(self.bad_toss)
        layout1.add_widget(self.resultimgage)
        layout1.add_widget(layout2)
        layout3.add_widget(choose_heads)
        layout3.add_widget(layout4)
        layout3.add_widget(choose_tails)
        layout2.add_widget(layout3)#t
        layout2.add_widget(self.result)#r
        choose_heads.bind(on_press=self.head_toss)#i
        choose_tails.bind(on_press=self.tail_toss)#s
        self.result.bind(on_press=self.reset)#t
        if self.counter1 == 10:#a
            self.game = 1#n
        if self.counter2 == 10:
            self.game = 2
        return layout1
 
    def tail_toss(self, btn):
        if self.game == 0:
            self.guess = 2
            self.coinresult = random.randint(1,2)
            if self.coinresult == 1:
                self.coinresult ='heads.png'
                self.result.text = "heads"
                self.counter2 = self.counter2 + 1
                self.bad_toss.text = str(self.counter2)
            elif self.coinresult == 2:
                self.coinresult = 'tails.png'
                self.result.text = "tails"
                self.counter1 = self.counter1 + 1
                self.good_toss.text = str(self.counter1)
            self.resultimgage.source = self.coinresult
        if self.counter1 == 10:
            self.game = 1
        if self.counter2 == 10:
            self.game = 2
        if self.game == 1:
            self.result.text = "winner"
        if self.game == 2:
            self.result.text = "loser"
   
    def head_toss(self, btn):
        if self.game == 0:
            self.guess = 1
            self.coinresult = random.randint(1,2)
            if self.coinresult == 1:
                self.coinresult ='heads.png'
                self.result.text = "heads"
                self.counter1 = self.counter1 + 1
                self.good_toss.text = str(self.counter1)
            elif self.coinresult == 2:
                self.coinresult = 'tails.png'
                self.result.text = "tails"
                self.counter2 = self.counter2 + 1
                self.bad_toss.text = str(self.counter2)
            self.resultimgage.source = self.coinresult
        if self.counter1 == 10:
            self.game = 1
        if self.counter2 == 10:
            self.game = 2
        if self.game == 1:
            self.result.text = "winner"
        if self.game == 2:
            self.result.text = "loser"
    def reset(self, btn):
        if self.game != 0:
            self.counter1 = 0
            self.counter2 = 0
            self.game = 0
            self.good_toss.text = str(self.counter1)
            self.bad_toss.text = str(self.counter2)
            self.result.text = "result"
coin().run()
