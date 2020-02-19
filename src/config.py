import json
from PIL import Image, ImageDraw

class Layer:
    def __init__(self, layer_key: str, bindings: dict):
        self.layer_key = layer_key
        self.bindings = bindings

    def draw(self, kbformat: str, name: str):
        layout = json.load(open(f'img/{kbformat}.json', 'r'))
        kbimage = Image.open(f'img/{kbformat}.png')
        kbimage = kbimage.convert(mode="RGB")
        draw = ImageDraw.Draw(kbimage)
        layer_key_location = layout[self.layer_key]
        draw.text(layer_key_location, "ACTIVATE", fill=(201, 10, 36))
        for key in self.bindings:
            location = layout[key]
            draw.multiline_text(location, self.bindings[key], fill=(0, 0, 0))
        kbimage.save(f'{self.layer_key}-{name}.png')



class Bindings:
    def __init__(self, name:str, binding_file: str):
        self.layers = []
        self.name = name
        config = json.load(open(binding_file, 'r'))
        for layer in config:
            self.layers.append(Layer(layer['layer_key'], layer['bindings']))

    def draw_all(self, kbformat: str):
        for layer in self.layers:
            layer.draw(kbformat, self.name)

Bindings("test", "test.json").draw_all("60")
