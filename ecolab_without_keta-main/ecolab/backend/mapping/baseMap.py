import folium

class Map:
    def __init__(self , map , height , width):
        self.map = map
        self.height = height
        self.width = width
    def notNull(self):
        if self.height == "-":
            self.height = 500
        if self.width == "-":
            self.width = 500
    def html(self):
        self.map = folium.Map(
            location=[45.523, -122.675],
            width=self.width,
            height=self.height,
            zoom_start=2)

