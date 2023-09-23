import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox

df = pd.read_csv('GooglePlayStore_wild.csv')

category = ''
max_rating = 0
min_rating = 0
type_ = ''
max_price = 0
min_price = 0
content_rating = ''

def print_dataframe(dataframe):
    nombres = dataframe['App'].tolist()
    categorias = dataframe['Category'].tolist()
    precios = dataframe['Price'].tolist()
    evaluacion = dataframe['Rating'].tolist()
    tamano = dataframe['Size'].tolist()
    descargas = dataframe['Installs'].tolist()
    texto = ''
    for i in range(len(nombres)):
        texto += str(nombres[i]) + ' ' + str(precios[i]) + ' ' + str(evaluacion[i]) + ' ' + str(tamano[i]) + ' ' + str(descargas[i]) + '\n'
    return texto

class PrimeraPantalla(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(spacing = 10, orientation='vertical')
        self.texto = Label(text='Bienvenido al buscador de aplicaciones')
        self.boton = Button(text='Empezar', background_color = (0,1,0,1), size_hint = (0.5, 0.5), pos_hint = {'x':.25, 'y':.25})
        self.boton.on_press = self.next
        layout.add_widget(self.texto)
        layout.add_widget(self.boton)
        self.add_widget(layout)

    def next(self):
        self.manager.current = 'screen2'

class SegundaPantalla(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(spacing = 5, orientation='vertical')
        self.layout1 = BoxLayout(spacing = 1, orientation='vertical')
        self.layout2 = BoxLayout(spacing = 1, orientation='vertical')
        self.layout3 = BoxLayout(spacing = 10, orientation='horizontal')
        self.texto = Label(text='Elige la categoría que quieras')
        scroll = ScrollView(size_hint=(1, 1))
        self.boton1 = Button(text='FAMILY')
        self.boton2 = Button(text='GAME')
        self.boton3 = Button(text='TOOLS')
        self.boton4 = Button(text='MEDICAL')
        self.boton5 = Button(text='BUSINESS')
        self.boton6 = Button(text='PRODUCTIVITY')
        self.boton7 = Button(text='PERSONALIZATION')
        self.boton8 = Button(text='COMMUNICATION')
        self.boton9 = Button(text='SPORTS')
        self.boton10 = Button(text='LIFESTYLE')
        self.boton11 = Button(text='FINANCE')
        self.boton12 = Button(text='HEALTH_AND_FITNESS')
        self.boton13 = Button(text='PHOTOGRAPHY')
        self.boton14 = Button(text='SOCIAL')
        self.boton15 = Button(text='NEWS_AND_MAGAZINES')
        self.boton16 = Button(text='SHOPPING')
        self.boton17 = Button(text='TRAVEL_AND_LOCAL')
        self.boton18 = Button(text='DATING')
        self.boton19 = Button(text='BOOKS_AND_REFERENCE')
        self.boton20 = Button(text='VIDEO_PLAYERS')
        self.boton21 = Button(text='EDUCATION')
        self.boton22 = Button(text='ENTERTAINMENT')
        self.boton23 = Button(text='MAPS_AND_NAVIGATION')
        self.boton24 = Button(text='FOOD_AND_DRINK')
        self.boton25 = Button(text='HOUSE_AND_HOME')
        self.boton26 = Button(text='AUTO_AND_VEHICLES')
        self.boton27 = Button(text='LIBRARIES_AND_DEMO')
        self.boton28 = Button(text='WEATHER')
        self.boton29 = Button(text='ART_AND_DESIGN')
        self.boton30 = Button(text='EVENTS')
        self.boton31 = Button(text='PARENTING')
        self.boton32 = Button(text='COMICS')
        self.boton33 = Button(text='BEAUTY')
        self.boton1.bind(on_press = self.guardar_category)
        self.boton2.bind(on_press = self.guardar_category)
        self.boton3.bind(on_press = self.guardar_category)
        self.boton4.bind(on_press = self.guardar_category)
        self.boton5.bind(on_press = self.guardar_category)
        self.boton6.bind(on_press = self.guardar_category)
        self.boton7.bind(on_press = self.guardar_category)
        self.boton8.bind(on_press = self.guardar_category)
        self.boton9.bind(on_press = self.guardar_category)
        self.boton10.bind(on_press = self.guardar_category)
        self.boton11.bind(on_press = self.guardar_category)
        self.boton12.bind(on_press = self.guardar_category)
        self.boton13.bind(on_press = self.guardar_category)
        self.boton14.bind(on_press = self.guardar_category)
        self.boton15.bind(on_press = self.guardar_category)
        self.boton16.bind(on_press = self.guardar_category)
        self.boton17.bind(on_press = self.guardar_category)
        self.boton18.bind(on_press = self.guardar_category)
        self.boton19.bind(on_press = self.guardar_category)
        self.boton20.bind(on_press = self.guardar_category)
        self.boton21.bind(on_press = self.guardar_category)
        self.boton22.bind(on_press = self.guardar_category)
        self.boton23.bind(on_press = self.guardar_category)
        self.boton24.bind(on_press = self.guardar_category)
        self.boton25.bind(on_press = self.guardar_category)
        self.boton26.bind(on_press = self.guardar_category)
        self.boton27.bind(on_press = self.guardar_category)
        self.boton28.bind(on_press = self.guardar_category)
        self.boton29.bind(on_press = self.guardar_category)
        self.boton30.bind(on_press = self.guardar_category)
        self.boton31.bind(on_press = self.guardar_category)
        self.boton32.bind(on_press = self.guardar_category)
        self.boton33.bind(on_press = self.guardar_category)
        self.lista = []
        self.siguiente = Button(text='Siguiente', background_color = (0,1,0,1), size_hint = (0.15, 0.15), pos_hint = {'x':.42, 'y':.5})
        self.siguiente.on_press = self.next
        self.layout1.add_widget(self.boton1)
        self.layout1.add_widget(self.boton2)
        self.layout1.add_widget(self.boton3)
        self.layout1.add_widget(self.boton4)
        self.layout1.add_widget(self.boton5)
        self.layout1.add_widget(self.boton6)
        self.layout1.add_widget(self.boton7)
        self.layout1.add_widget(self.boton8)
        self.layout1.add_widget(self.boton9)
        self.layout1.add_widget(self.boton10)
        self.layout1.add_widget(self.boton11)
        self.layout1.add_widget(self.boton12)
        self.layout1.add_widget(self.boton13)
        self.layout1.add_widget(self.boton14)
        self.layout1.add_widget(self.boton15)
        self.layout1.add_widget(self.boton16)
        self.layout1.add_widget(self.boton17)
        self.layout2.add_widget(self.boton18)
        self.layout2.add_widget(self.boton19)
        self.layout2.add_widget(self.boton20)
        self.layout2.add_widget(self.boton21)
        self.layout2.add_widget(self.boton22)
        self.layout2.add_widget(self.boton23)
        self.layout2.add_widget(self.boton24)
        self.layout2.add_widget(self.boton25)
        self.layout2.add_widget(self.boton26)
        self.layout2.add_widget(self.boton27)
        self.layout2.add_widget(self.boton28)
        self.layout2.add_widget(self.boton29)
        self.layout2.add_widget(self.boton30)
        self.layout2.add_widget(self.boton31)
        self.layout2.add_widget(self.boton32)
        self.layout2.add_widget(self.boton33)
        self.layout3.add_widget(self.layout1)
        self.layout3.add_widget(self.layout2)
        self.layout.add_widget(self.texto)
        self.layout.add_widget(self.layout3)
        self.layout.add_widget(self.siguiente)
        scroll.add_widget(self.layout)
        self.add_widget(scroll)
    
    def next(self):
        self.manager.current = 'screen3'

    def guardar_category(self, intance):
        self.lista.append(intance.text)
        self.category = self.lista[-1]

class TerceraPantalla(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(spacing = 5, orientation='vertical')
        self.layout_rating = BoxLayout(spacing = 5, orientation='vertical')
        self.layout2 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout3 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout4 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout5 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout6 = BoxLayout(spacing = 3, orientation='horizontal')
        label_rating = Label(text='RATING')
        label_rating1 = Label(text='5.0 - 4.0')
        label_rating2 = Label(text='4.0 - 3.0')
        label_rating3 = Label(text='3.0 - 2.0')
        label_rating4 = Label(text='2.0 - 1.0')
        label_rating5 = Label(text='1.0 - 0.0')
        self.checkbox_rating1 = CheckBox(active = True)
        self.checkbox_rating2 = CheckBox(active = False)
        self.checkbox_rating3 = CheckBox(active = False)
        self.checkbox_rating4 = CheckBox(active = False)
        self.checkbox_rating5 = CheckBox(active = False)
        self.layout_rating.add_widget(label_rating)
        self.layout2.add_widget(label_rating1)
        self.layout2.add_widget(self.checkbox_rating1)
        self.layout3.add_widget(label_rating2)
        self.layout3.add_widget(self.checkbox_rating2)
        self.layout4.add_widget(label_rating3)
        self.layout4.add_widget(self.checkbox_rating3)
        self.layout5.add_widget(label_rating4)
        self.layout5.add_widget(self.checkbox_rating4)
        self.layout6.add_widget(label_rating5)
        self.layout6.add_widget(self.checkbox_rating5)
        self.layout_rating.add_widget(self.layout2)
        self.layout_rating.add_widget(self.layout3)
        self.layout_rating.add_widget(self.layout4)
        self.layout_rating.add_widget(self.layout5)
        self.layout_rating.add_widget(self.layout6)
        self.layout.add_widget(self.layout_rating)
        self.layout_type = BoxLayout(spacing = 5, orientation='vertical')
        self.layout7 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout8 = BoxLayout(spacing = 3, orientation='horizontal')
        label_type = Label(text='TYPE')
        label_type1 = Label(text='Free')
        label_type2 = Label(text='Paid')
        checkbox_type1 = CheckBox(active = False)
        checkbox_type2 = CheckBox(active = False)
        self.layout_type.add_widget(label_type)
        self.layout7.add_widget(label_type1)
        self.layout7.add_widget(checkbox_type1)
        self.layout8.add_widget(label_type2)
        self.layout8.add_widget(checkbox_type2)
        self.layout_type.add_widget(self.layout7)
        self.layout_type.add_widget(self.layout8)
        self.layout.add_widget(self.layout_type)
        self.layout_content = BoxLayout(spacing = 5, orientation='vertical')
        self.layout9 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout10 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout11 = BoxLayout(spacing = 3, orientation='horizontal')
        label_content = Label(text='CONTENT RATING')
        label_content1 = Label(text='Everyone')
        label_content2 = Label(text='Everyone 10+')
        label_content3 = Label(text='Adults only 18+')
        checkbox_content1 = CheckBox(active = False)
        checkbox_content2 = CheckBox(active = False)
        checkbox_content3 = CheckBox(active = False)
        self.layout_type.add_widget(label_content)
        self.layout9.add_widget(label_content1)
        self.layout9.add_widget(checkbox_content1)
        self.layout10.add_widget(label_content2)
        self.layout10.add_widget(checkbox_content2)
        self.layout11.add_widget(label_content3)
        self.layout11.add_widget(checkbox_content3)
        self.layout_content.add_widget(self.layout9)
        self.layout_content.add_widget(self.layout10)
        self.layout_content.add_widget(self.layout11)
        self.layout.add_widget(self.layout_content)
        self.layout_price = BoxLayout(spacing = 5, orientation='vertical')
        self.layout12 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout13 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout14 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout15 = BoxLayout(spacing = 3, orientation='horizontal')
        self.layout16 = BoxLayout(spacing = 3, orientation='horizontal')
        label_price = Label(text='PRICE')
        label_price1 = Label(text='$100 >')
        label_price2 = Label(text='$100 - $50')
        label_price3 = Label(text='$50 - $20')
        label_price4 = Label(text='$20 - $5')
        label_price5 = Label(text='$5 - $0')
        checkbox_price1 = CheckBox(active = False)
        checkbox_price2 = CheckBox(active = False)
        checkbox_price3 = CheckBox(active = False)
        checkbox_price4 = CheckBox(active = False)
        checkbox_price5 = CheckBox(active = False)
        self.layout_price.add_widget(label_price)
        self.layout12.add_widget(label_price1)
        self.layout12.add_widget(checkbox_price1)
        self.layout13.add_widget(label_price2)
        self.layout13.add_widget(checkbox_price2)
        self.layout14.add_widget(label_price3)
        self.layout14.add_widget(checkbox_price3)
        self.layout15.add_widget(label_price4)
        self.layout15.add_widget(checkbox_price4)
        self.layout16.add_widget(label_price5)
        self.layout16.add_widget(checkbox_price5)
        self.layout_price.add_widget(self.layout12)
        self.layout_price.add_widget(self.layout13)
        self.layout_price.add_widget(self.layout14)
        self.layout_price.add_widget(self.layout15)
        self.layout_price.add_widget(self.layout16)
        self.layout.add_widget(self.layout_price)
        self.buscar = Button(text='Buscar', background_color = (0,1,0,1), size_hint = (0.15, 0.15), pos_hint = {'x':.42, 'y':.5})
        self.buscar.on_press = self.guardar_rating
        self.layout.add_widget(self.buscar)
        self.add_widget(self.layout)

    def next(self):
        self.manager.current = 'screen4'
        a = self.manager.current_screen
        a.refresh()

    def guardar_rating(self):
        global max_rating, min_rating
        if self.checkbox_rating1.active == True:
            max_rating = 5
            min_rating = 4
        elif self.checkbox_rating2.active == True:
            max_rating = 4
            min_rating = 3
        elif self.checkbox_rating3.active == True:
            max_rating = 3
            min_rating = 2
        elif self.checkbox_rating4.active == True:
            max_rating = 2
            min_rating = 1
        elif self.checkbox_rating5.active == True:
            max_rating = 1
            min_rating = 0
        self.next()
        
    
    def guradar_type(self):
        if self.checkbox_type1.active == True:
            self.type_ = 'Free'
        elif self.checkbox_type2.active == True:
            self.type_ = 'Paid'
    
    def guardar_content(self):
        if self.checkbox_content1.active == True:
            self.content = 'Everyone'
        elif self.checkbox_content2.active == True:
            self.content = 'Everyone 10+'
        elif self.checkbox_content3.active == True:
            self.content = 'Adults only 18+'
    
    def guardar_price(self):
        if self.checkbox_price1.active == True:
            self.max_price = 1000000
            self.max_price = 100
        elif self.checkbox_price2.active == True:
            self.max_price = 100
            self.max_price = 50
        elif self.checkbox_price3.active == True:
            self.max_price = 50
            self.max_price = 20
        elif self.checkbox_price4.active == True:
            self.max_price = 20
            self.max_price = 5
        elif self.checkbox_price5.active == True:
            self.max_price = 5
            self.max_price = 0

class CuartaPantalla(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.label = Label(text = '')
        self.add_widget(self.label)

    def refresh(self):
        self.label.text = print_dataframe(df[(df['Rating'] < max_rating) & (df['Rating'] > min_rating)].head(6))
        print(max_rating)
        print(min_rating)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PrimeraPantalla(name = 'screen1'))
        sm.add_widget(SegundaPantalla(name = 'screen2'))
        sm.add_widget(TerceraPantalla(name = 'screen3'))
        sm.add_widget(CuartaPantalla(name = 'screen4'))
        return sm

MyApp().run()


'''if self.category == self.categorias[i]:
        elif self.max_price < self.precios[i] and self.min_price > self.precios[i]:
            elif self.type_ == self.tipos[i]:
                elif self.content == self.contenidos[i]:
                    texto = self.nombres[i] + ' ' + self.precios[i] + ' ' + self.evaluacion[i] + ' ' + self.tamano[i] + ' ' + self.descargas[i]
    else:
        texto = ''
    return texto'''