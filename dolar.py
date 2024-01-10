import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
from dateutil import parser

response = requests.get("https://dolarapi.com/v1/dolares")

table = Table(title="🤑 Dólar estadounidense hoy en Argentina🤑")

table.add_column("Tipo de cambio", justify="left", style="cyan", no_wrap=True)
table.add_column("Venta", justify="right", style="cyan", no_wrap=True)
table.add_column("Compra", justify="right", style="cyan", no_wrap=True)
table.add_column("Actualizado", justify="right", style="cyan", no_wrap=True)

for dollar in response.json():
  date = parser.parse(dollar['fechaActualizacion']).strftime("%d/%m/%Y %H:%M:%S")
  table.add_row(str(dollar['nombre']), '$' + str( dollar['venta']), '$' + str(dollar['compra']), date + 'HS')

text = Text("👍 Informacion obtenida en https://dolarapi.com")
text.stylize("bold magenta", 0)

console = Console()
console.print(table)
console.print(text)

