cairosketchpad 0.1
==================

cairosketchpad is a live coding sketchpad for Python/Cairo. See the [screencast](https://www.youtube.com/watch?v=gmYdJuwVxYQ&feature=youtu.be) for an explanation.

## Example

<pre>
$ cairosketchpad --create sketch.py
</pre>

Now sketch.py contains:

<pre>
def draw(cr, width, height):
    cr.rectangle(width/2.0 - 50, height/2.0 - 50, 100, 100)
    cr.stroke()
</pre>

Now observe the sketch script by starting cairosketchpad.

<pre>
$ cairosketchpad sketch.py
</pre>

Now open your favourite editor and edit sketch.py the code is automatically updated in your view. Have fun! :) 

## Installation

Be sure you have GTK+3, PyGObject and Python 2.7 or greater installed.

<pre>
$ git clone git://github.com/jpzk/cairosketchpad.git
$ cd cairosketchpad
$ sudo python setup.py install
</pre>

## Requirements

PyGObject is a Python module that enables developers to access GObject-based libraries such as GTK+ within Python. It exclusively supports GTK+ version 3 or later. 




