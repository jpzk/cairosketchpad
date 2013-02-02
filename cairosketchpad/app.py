#!/bin/env python

''' 
This file is part of cairo-sketchpad.

Copyright 2013, Jendrik Poloczek

cairo-sketchpad is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

cairo-sketchpad is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
cairo-sketchpad.  If not, see <http://www.gnu.org/licenses/>.
'''

from gi.repository import Gtk, GLib,  Gdk, cairo 
import math
import sys
import time
import threading
import os
import argparse

# Python/Cairo Live Coding Sketchpad

WATCH_IDLE_TIME = 1
WIDTH = 600
HEIGHT = 600

class WatchThread(threading.Thread):
    def __init__(self, window, filename, mod):
        threading.Thread.__init__(self)
        self._window = window
        self._mod = mod
        self._filename = filename
        self.start_time = os.stat(self._filename).st_mtime
        self.stopthread = threading.Event()

    def run(self):
        while not self.stopthread.isSet(): 
            if(os.stat(self._filename).st_mtime > self.start_time):
                Gdk.threads_enter()
                reload(self._mod)
                h = self._window.get_allocated_height()
                w = self._window.get_allocated_width()
                self._window.queue_draw_area(0,0, w, h) 
                Gdk.threads_leave()
                self.start_time = os.stat(self._filename).st_mtime
            else:                
                time.sleep(WATCH_IDLE_TIME)

    def stop(self):
        self.stopthread.set()

class Livecode(Gtk.DrawingArea):
    def __init__(self, mod):
        Gtk.DrawingArea.__init__(self)
        self.set_size_request (WIDTH, HEIGHT)
        self.connect('draw', self.do_draw_cb)
        self._mod = mod
       
    def do_draw_cb(self, widget, cr):
        h = self.get_allocated_height()            
        w = self.get_allocated_width()
        self._mod.draw(cr,w, h)

class GtkApp():
    def __init__(self, filename):  
        self._mod = __import__(filename.split('.')[0])
        self._livecode = Livecode(self._mod)
        self._watchthread = WatchThread(self._livecode, filename, self._mod)

        window = Gtk.Window()
        window.set_title ("cairo-sketchpad on %s" % filename)
        window.add(self._livecode)
        window.show_all()
        window.connect_after('destroy', self._destroy)

    def _destroy(self, event):
        self._watchthread.stop() 
        Gtk.main_quit()

def main():
    sys.path.append(os.getenv("PWD"))
    parser = argparse.ArgumentParser()
    parser.add_argument('sketch', help = 'run a livecoding sketch')
    parser.add_argument('--create', action = 'store_true', dest = 'create', default = False)    
    args = parser.parse_args()

    if(args.create):
        head = "def draw(cr, width, height):\n"
        body1 = " " * 4 + "cr.rectangle(width/2.0 - 50, height/2.0 - 50, 100, 100)\n"
        body2 = " " * 4 + "cr.stroke()\n"
        sketch_file = open(args.sketch, "w")
        sketch_file.writelines([head, body1, body2])
        sketch_file.close()
        print "Created sketch: %s" % args.sketch 

    else:
        GLib.threads_init()
        gt = GtkApp(args.sketch)
        gt._watchthread.start()
        Gdk.threads_enter()
        Gtk.main()
        Gdk.threads_leave()
 
if __name__ == "__main__":
    sys.exit(main()) 
