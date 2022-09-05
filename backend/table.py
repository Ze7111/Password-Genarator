from rich import console; print = console.Console().print
from rich.table import Table

class table:
    def __init__(self):
        self.table = Table(style="#9770ed", show_header=True, header_style="#febaf9")
        self.table.add_column("Device Name", justify="center", style="bold #9770ed")
        self.table.add_column("Password", justify="center", style="bold #9770ed")
        self.table.add_column("Input Params", justify="center", style="bold #9770ed")

    def add(self, name, description, input_params):
        self.table.add_row(name, description, input_params)

    def print(self):
        print(self.table, style= "#9770ed")