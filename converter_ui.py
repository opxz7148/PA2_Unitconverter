import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from unittype import UnitType, LengthUnits


class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes 
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self, unit_type):
        super().__init__()

        # Setting up menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        self.unit = tk.StringVar()

        # Create all component for GUI
        self.l_combo = FieldCombo(self)
        self.r_combo = FieldCombo(self)
        self.label = tk.Label(self, text=" = ")
        self.convert_button = tk.Button(self, text="convert", command=self.convert_handler)
        self.clear_button = tk.Button(self, text="clear", command=self.clear_handler)


        # Setting up unit menu
        unit_list = tk.Menu(menubar)

        # Load all unit
        for unit in UnitType:
            unit_list.add_radiobutton(
                label=unit.value[0],
                value=unit.value[0],
                variable=self.unit,
                command=self.change_unit
            )

        unit_list.add_radiobutton(label="Exit", command=self.destroy)

        menubar.add_cascade(
            label="unit",
            menu=unit_list,
        )
        self.use_unit = unit_type
        self.load_units()



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
        units = self.use_unit.get_units()

        #TODO put the unit names (strings) in the comboboxes
        #TODO and select which unit to display

        self.l_combo.combobox['values'] = units
        self.r_combo.combobox['values'] = units

        self.l_combo.combobox.current(newindex=0)
        self.r_combo.combobox.current(newindex=0)


    def convert_handler(self, *args):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        #TODO 1. Convert from left side to right side
        #TODO 2. When that works, intelligently decide to convert
        #        left-to-right or right-to-left

        self.r_combo.field['fg'] = 'black'
        self.l_combo.field['fg'] = 'black'

        if not self.l_combo.field_val.get() and not self.r_combo.field_val.get():
            return

        if self.l_combo.field_val.get():
            try:
                result = self.use_unit.convert(
                    float(self.l_combo.field_val.get()),
                    self.l_combo.combo_val.get().replace(" ", "_"),
                    self.r_combo.combo_val.get().replace(" ", "_")
                )
            except ValueError:
                self.l_combo.field['fg'] = 'red'
                self.r_combo.field.delete(0, tk.END)
                return

            self.r_combo.field.delete(0, tk.END)
            self.r_combo.field.insert(0, f"{result:.5g}")
            return

        else:
            try:
                result = self.use_unit.convert(
                    float(self.r_combo.field_val.get()),
                    self.r_combo.combo_val.get().replace(" ", "_"),
                    self.l_combo.combo_val.get().replace(" ", "_")
                )
            except ValueError:
                self.r_combo.field['fg'] = 'red'
                self.l_combo.field.delete(0, tk.END)
                return

            self.l_combo.field.delete(0, tk.END)
            self.l_combo.field.insert(0, f"{result:.5g}")
            return

    def clear_handler(self, *args):
        self.l_combo.field.delete(0, tk.END)
        self.r_combo.field.delete(0, tk.END)
        self.r_combo.field['fg'] = 'black'
        self.l_combo.field['fg'] = 'black'
        return

    def change_unit(self, *args):
        print(self.unit.get())
        self.use_unit = UnitType[self.unit.get().upper()]
        self.load_units()
        self.clear_handler()

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
   ui = ConverterUI(UnitType["LENGTH"])
   ui.run()


