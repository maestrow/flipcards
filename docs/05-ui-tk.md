- https://docs.python.org/3/faq/gui.html
-> https://docs.python.org/3/library/tk.html#tkinter
-> https://docs.python.org/3/library/tkinter.html
-> https://wiki.python.org/moin/TkInter
-> https://tkdocs.com/tutorial/index.html

- https://tkdocs.com/shipman/ Reference

```py
from tkinter import *   # loads the Tk library on your system
from tkinter import ttk # themed widgets

# Main Application Window
root = Tk()
root.title("Feet to Meters")

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)   # creating a widget: pass parent and options
feet_entry.grid(column=2, row=1, sticky=(W, E))                 # where to place widget

# Methods are chainable: create widget, then place it.
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Finally, we need to tell Tk to enter its event loop, which is necessary for everything to appear onscreen and allow users to interact with it.
root.mainloop()
```

```py
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)
```


## Configuration options 

```py
% python
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
create a button, passing two options:
>>> button = ttk.Button(root, text="Hello", command="buttonpressed")
>>> button.grid()
check the current value of the text option:
>>> button['text']
'Hello'
change the value of the text option:
>>> button['text'] = 'goodbye'
another way to do the same thing:
>>> button.configure(text='goodbye')
check the current value of the text option:
>>> button['text']
'goodbye'
get all information about the text option:
>>> button.configure('text')
('text', 'text', 'Text', '', 'goodbye')
get information on all options for this widget:
>>> button.configure()
{'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''), 
'default': ('default', 'default', 'Default', <index object at 0x00DFFD10>, <index object at 0x00DFFD10>), 
'text': ('text', 'text', 'Text', '', 'goodbye'), 'image': ('image', 'image', 'Image', '', ''), 
'class': ('class', '', '', '', ''), 'padding': ('padding', 'padding', 'Pad', '', ''), 
'width': ('width', 'width', 'Width', '', ''), 
'state': ('state', 'state', 'State', <index object at 0x0167FA20>, <index object at 0x0167FA20>), 
'command': ('command', 'command' , 'Command', '', 'buttonpressed'), 
'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 
'compound': ('compound', 'compound', 'Compound', <index object at 0x0167FA08>, <index object at 0x0167FA08>), 
'underline': ('underline', 'underline', 'Underline', -1, -1), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', 'ttk::takefocus')}
```

## Widget Introspection

```py
def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)
print_hierarchy(root)
```

winfo_class:
a class identifying the type of widget, e.g. TButton for a themed button
winfo_children:
a list of widgets that are the direct children of a widget in the hierarchy
winfo_parent:
parent of the widget in the hierarchy
winfo_toplevel:
the toplevel window containing this widget
winfo_width, winfo_height:
current width and height of the widget; not accurate until appears onscreen
winfo_reqwidth, winfo_reqheight:
the width and height the widget requests of the geometry manager (more on this shortly)
winfo_x, winfo_y:
the position of the top-left corner of the widget relative to its parent
winfo_rootx, winfo_rooty:
the position of the top-left corner of the widget relative to the entire screen
winfo_vieweable:
whether the widget is displayed or hidden (all its ancestors in the hierarchy must be viewable for it to be viewable)


## Geometry Management

grid:
- columnconfigure
- rowconfigure
- row, column, sticky options

## Binding to Events

```py
from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()
```

to capture two keys pressed in a row: <KeyPress-A><KeyPress-B> or simply <ab>.

## Style

```py
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()
```

## Layout

anchor: e, se, s, sw, w, nw or center.
https://tkdocs.com/shipman/anchors.html


### Grid

- https://tkdocs.com/shipman/grid.html
- https://tkdocs.com/tutorial/grid.html
- https://tcl.tk/man/tcl8.6/TkCmd/grid.htm

`column` and `row` number - where you want the widget placed, counting from zero. The default value is zero. You don't have to start at 0 and can leave gaps in column and row numbers (e.g., column 1, 2, 10, 11, 12, 20, 21). This is useful if you plan to add more widgets in the middle of the user interface later.

`grid` method options: 
- column, row
- colspan, rowspan
- sticky
- anchor
- padx, pady

columnconfigure and rowconfigure methods of grid

#### Querying and Changing Grid Options

```sh
>>> content.grid_slaves()
[<tkinter.ttk.Button object .!frame.!button2>, <tkinter.ttk.Button object .!frame.!button>,
<tkinter.ttk.Checkbutton object .!frame.!checkbutton3>, <tkinter.ttk.Checkbutton object .!frame.!checkbutton2>,
<tkinter.ttk.Checkbutton object .!frame.!checkbutton>, <tkinter.ttk.Entry object .!frame.!entry>, 
<tkinter.ttk.Label object .!frame.!label>, <tkinter.ttk.Frame object .!frame.!frame>]
>>> for w in content.grid_slaves(): print(w)
...
.!frame.!button2
.!frame.!button
.!frame.!checkbutton3
.!frame.!checkbutton2
.!frame.!checkbutton
.!frame.!entry
.!frame.!label
.!frame.!frame
>>> for w in content.grid_slaves(row=3): print(w)
...
.!frame.!button2
.!frame.!button
.!frame.!checkbutton3
.!frame.!checkbutton2
.!frame.!checkbutton
>>> for w in content.grid_slaves(column=0): print(w)
...
.!frame.!checkbutton
.!frame.!frame
>>> namelbl.grid_info()
{'in': <tkinter.ttk.Frame object .!frame>, 'column': 3, 'row': 0, 'columnspan': 2, 'rowspan': 1, 
'ipadx': 0, 'ipady': 0, 'padx': 5, 'pady': 0, 'sticky': 'nw'}
>>> namelbl.grid_configure(sticky=(E,W))
>>> namelbl.grid_info()
{'in': <tkinter.ttk.Frame object .!frame>, 'column': 3, 'row': 0, 'columnspan': 2, 'rowspan': 1, 
'ipadx': 0, 'ipady': 0, 'padx': 5, 'pady': 0, 'sticky': 'ew'}
```


## The Command Callback

```py
action = ttk.Button(root, text="Action", default="active", command=myaction)
root.bind('<Return>', lambda e: action.invoke())
```

## Button State

```py
b.state(['disabled'])          # set the disabled flag
b.state(['!disabled'])         # clear the disabled flag
b.instate(['disabled'])        # true if disabled, else false
b.instate(['!disabled'])       # true if not disabled, else false
b.instate(['!disabled'], cmd)  # execute 'cmd' if not disabled
```

states: active, disabled, focus, pressed, selected, background, readonly, alternate, and invalid.

## Variables to bind

```py
s = StringVar(value="abc")   # default value is ''
b = BooleanVar(value=True)   # default is False
i = IntVar(value=10)         # default is 0
d = DoubleVar(value=10.5)    # default is 0.0
```