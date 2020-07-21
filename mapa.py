from kivy.app import App
from kivy_garden.mapview import MapMarkerPopup, MapView, MapMarker
from kivy.uix.popup import Popup
from pymongo import MongoClient
from math import *
from kivy.uix.button import Button
from kivy_garden.mapview.geojson import GeoJsonMapLayer
from kivy_garden.mapview.view import MapLayer, MIN_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE, MAX_LONGITUDE
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget,Builder
from kivy.graphics import Color, Line, SmoothLine, MatrixInstruction
from kivy.graphics.context_instructions import Translate, Scale
from kivy_garden.mapview.utils import clamp
from kivy_garden.mapview.geojson import GeoJsonMapLayer
from kivy_garden.mapview.utils import get_zoom_for_radius, haversine, clamp
from kivy.uix.floatlayout import FloatLayout



class Manager(ScreenManager):
    pass

class Map(MapView):
    pass

class MenuMapa(Screen):
    pass


class BuscaTipo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pesquisa(self):

        for i in range(10):
            marker = MapMarkerPopup(lat=-10 - i, lon=-47 - i,source="places.png")
            self.ids.mapview.add_widget(marker)



class Desenha(Screen):

    def __init__(self, **kwargs):
        super(Desenha, self).__init__(**kwargs)

    def desenha(self):
        source="bairro.json"
        layer = GeoJsonMapLayer(source=source)
        self.ids.mapview.add_layer(layer)

class Mapa(App):
    def build(self):
        return Manager()


Mapa().run()
