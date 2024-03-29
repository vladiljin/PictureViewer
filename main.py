import kivy
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty

kivy.require('1.0.6')

class Picture(Scatter):
    source = StringProperty(None)

class PicturesApp(App):

    def build(self):
        root = self.root

        # get any files into images directory
        curdir = dirname(__file__)
        for filename in glob(join(curdir, 'data', '*')):
            try:
                picture = Picture(source=filename, rotation=randint(-30, 30))
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

    def on_pause(self):
        return True

if __name__ == '__main__':
    PicturesApp().run()
