import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from unittype import UnitType
from converter import UnitConverter, LengthConverter

class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes 
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self, converter: UnitConverter):
        super().__init__()

        # Set initialize converter.
        self.converter = converter

        # # Setting up menubar
        # menubar = tk.Menu(self)
        # self.config()

        # Create all component for GUI
        self.l_combo = FieldCombo(self)
        self.r_combo = FieldCombo(self)
        self.label = tk.Label(self, text=" = ")
        self.convert_button = tk.Button(self, text="convert", command=self.convert_handler)
        self.clear_button = tk.Button(self, text="clear", command=self.clear_handler)

        # Call init_component to set thing up
        self.init_components()

    def init_components(self):
        """Create components and layout the UI."""
        # use a frame as internal container
        # this will help later when the UI gets more complex

        # Set window title.
        self.title("Converter")

        # Load unit into combobox
        self.load_units()

        # Place component on window.
        self.l_combo.set_to_the_left()
        self.label.pack(side=tk.LEFT)
        self.r_combo.set_to_the_left()
        self.convert_button.pack(side=tk.LEFT)
        self.clear_button.pack(side=tk.LEFT)

        # Binding function
        self.l_combo.field.bind('<Return>', self.convert_handler)
        self.r_combo.field.bind('<Return>', self.convert_handler)


    def load_units(self):
        """Load units of the requested unittype into the comboboxes."""
        units = self.converter.get_units()
        #TODO put the unit names (strings) in the comboboxes
        #TODO and select which unit to display

        self.l_combo.combobox['values'] = units
        self.r_combo.combobox['values'] = units

    def convert_handler(self, *args):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        #TODO 1. Convert from left side to right side
        #TODO 2. When that works, intelligently decide to convert
        #        left-to-right or right-to-left

        if not self.l_combo.field_val.get() and not self.r_combo.field_val.get():
            messagebox.showerror(title="Value Error", message="Field can't be blank")

        if self.l_combo.field_val.get():
            try:
                result = self.converter.convert(
                    float(self.l_combo.field_val.get()),
                    self.l_combo.combo_val.get(),
                    self.r_combo.combo_val.get()
                )
            except ValueError:
                messagebox.showerror(title="Value Error", message="Must fill only number in the field")
                self.l_combo.field.delete(0, tk.END)
                return

            self.r_combo.field.delete(0, tk.END)
            self.r_combo.field.insert(0, f"{result:.5g}")
            return

        else:
            try:
                result = self.converter.convert(
                    float(self.r_combo.field_val.get()),
                    self.r_combo.combo_val.get(),
                    self.l_combo.combo_val.get()
                )
            except ValueError:
                messagebox.showerror(title="Value Error", message="Must fill only number in the field")
                self.r_combo.field.delete(0, tk.END)
                return

            self.l_combo.field.delete(0, tk.END)
            self.l_combo.field.insert(0, f"{result:.5g}")
            return

    def clear_handler(self, *args):
        self.l_combo.field.delete(0, tk.END)
        self.r_combo.field.delete(0, tk.END)
        return

    def run(self):
        # start the app, wait for events 
        #TODO
        self.mainloop()


class FieldCombo:

    def __init__(self, root):

        self.field_val = tk.StringVar()
        self.field = tk.Entry(root, textvariable=self.field_val)

        self.combo_val = tk.StringVar()
        self.combobox = ttk.Combobox(root, textvariable=self.combo_val)
        self.combobox['state'] = 'readonly'


    def set_to_the_left(self):
        self.field.pack(side=tk.LEFT, expand=True, fill="x")
        self.combobox.pack(side=tk.LEFT, expand=True, fill="x")
        self.combobox.current(newindex=0)
        self.combobox.set(self.combo_val.get())



if __name__ == "__main__":
    ui = ConverterUI(LengthConverter())
    ui.run()

