"""
Autor: Samuel Rincón
"""

import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text

console = Console()

dadoD4 = 4
dadoD6 = 6
dadoD8 = 8
dadoD10 = 10
dadoD12 = 12
dadoD20 = 20

while True:
    console.print("\n[bold cyan]  SIMULADOR DE LANZAMIENTO DE DADOS [/bold cyan]")
    console.print("1. Lanzar dados")
    console.print("2. Ver estadísticas (Algún día se añadirá)")
    console.print("3. Salir")
    
    opcionMenu = input("\nElige una opción (1-3): ")
    
    try:
        opcionMenuNum = int(opcionMenu)
    except ValueError:
        console.print("[bold red]Error: Debes introducir un número válido (1, 2 o 3).[/bold red]")
        continue
        
    if opcionMenuNum == 1:

        console.print("\n[yellow]Tipos de dados disponibles:[/yellow]")
        console.print("1. D4 (4 caras)")
        console.print("2. D6 (6 caras)")
        console.print("3. D8 (8 caras)")
        console.print("4. D10 (10 caras)")
        console.print("5. D12 (12 caras)")
        console.print("6. D20 (20 caras)")
        
        eleccion = input("Selecciona el tipo de dado (1-6): ")
        
        try:
            tipoNum = int(eleccion)
        except ValueError:
            console.print("[bold red]Error: Tipo de dado no válido. Volviendo al menú.[/bold red]")
            continue
            
        if tipoNum == 1:
            caras = dadoD4
        elif tipoNum == 2:
            caras = dadoD6
        elif tipoNum == 3:
            caras = dadoD8
        elif tipoNum == 4:
            caras = dadoD10
        elif tipoNum == 5:
            caras = dadoD12
        elif tipoNum == 6:
            caras = dadoD20
        else:
            console.print("[bold red]Error: Opcion fuera de rango [/bold red]")
            continue
            
        cantidad = False
        cantidadDados = 0
        while not cantidad:
            entrada = input("Cuántos dados quieres lanzar (entero positivo): ")
            try:
                cantidadDados = int(entrada)
                if cantidadDados > 0:
                    cantidad = True
                else:
                    console.print("[bold red] La cantidad debe ser mayor que 0.[/bold red]")
            except ValueError:
                console.print("[bold red] Entrada no numérica. Introduce un número entero válido.[/bold red]")
                
        console.print("\n[cyan] Lanzando dados [/cyan]")
        with Live(Panel("Rodando dados...", title="Animación", border_style="cyan"), refresh_per_second=10) as live:
            for i in range(15):
                animTexto = " ".join(str(random.randint(1, caras)) for _ in range(min(cantidadDados, 5)))
                live.update(Panel(f"[yellow]{animTexto}[/yellow]", title="Animación en curso", border_style="cyan"))
                time.sleep(0.1)
                
        sumaTotal = 0
        resultadosTexto = Text()
        
        contador = 0
        while contador < cantidadDados:
            resultadoDado = random.randint(1, caras)
            sumaTotal = sumaTotal + resultadoDado
            
            if resultadoDado == caras:
                colorStr = "bold green"
            elif resultadoDado == 1:
                colorStr = "bold red"
            else:
                colorStr = "yellow"
                
            resultadosTexto.append(f"{resultadoDado} ", style=colorStr)
            contador = contador + 1
            
        promedio = sumaTotal / cantidadDados
        
        panelContenido = Text("Resultados individuales: \n")
        panelContenido.append(resultadosTexto)
        panelContenido.append("\nSuma Total: ", style="bold white")
        panelContenido.append(f"{sumaTotal}\n", style="bold cyan")
        panelContenido.append("Promedio: ", style="bold white")
        panelContenido.append(f"{promedio:.2f}", style="bold cyan")
        
        console.print(Panel(panelContenido, title=f"Resultado de la tirada ({cantidadDados}D{caras})", border_style="green"))
        
    elif opcionMenuNum == 2:
        pass
        console.print("[yellow]La opción de estadísticas estará disponible en futuras versiones.[/yellow]")
        
    elif opcionMenuNum == 3:
        console.print("[bold green]  Saliendo...[/bold green]")
        break
    else:
        console.print("[bold red] Opción incorrecta, pon una opción entre 1 y 3 anda.[/bold red]")