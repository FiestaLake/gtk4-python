#!/bin/python3

import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Gdk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(600, 250)
        self.set_title("MyApp")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Hello")
        self.button.connect("clicked", self.hello)
        self.check = Gtk.CheckButton(label="And goodbye?")

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.box2.append(
            self.button
        )  # Put button in the first of the two vertial boxes
        self.box2.append(self.check)
        
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.switch = Gtk.Switch()
        self.switch.set_active(True)  # Let's default it to on
        self.switch.connect("state-set", self.switch_switched) # Lets trigger a function

        self.switch_box.append(self.switch)
        self.box2.append(self.switch_box)
        
        self.label = Gtk.Label(label="A switch")
        self.switch_box.append(self.label)
        self.switch_box.set_spacing(5)

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def hello(self, button):
        if self.check.get_active():
            print("Goodbye world!")
            self.close()
        else:
            print("Hello world")


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
