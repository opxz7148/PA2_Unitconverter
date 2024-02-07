import tkinter as tk
from tkinter import ttk
from unittype import UnitType
from converter import UnitConverter

class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes 
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self, converter: UnitConverter):
        super().__init__()


    def init_components(self):
        """Create components and layout the UI."""
        # use a frame as internal container
        # this will help later when the UI gets more complex
    
    def load_units(self, unittype: UnitType):
        """Load units of the requested unittype into the comboboxes."""
        units = self.converter.get_units(unittype)
        #TODO put the unit names (strings) in the comboboxes
        #TODO and select which unit to display

    def convert_handler(self):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        #TODO 1. Convert from left side to right side
        #TODO 2. When that works, intelligently decide to convert
        #        left-to-right or right-to-left
        pass

    def run(self):
        # start the app, wait for events 
        #TODO

