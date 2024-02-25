"""File to launch the clock application."""

from converter_ui import ConverterUI
from converter import UnitConverter

if __name__ == '__main__':
 
    # Create a unit converter and give it to the ConverterUI
    # via the constructor. This is called Dependency Injection.
    ui = ConverterUI(UnitConverter)
    ui.run()
