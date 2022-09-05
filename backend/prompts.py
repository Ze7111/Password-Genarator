from rich import console; print = console.Console().print
from backend.revert import clear

def prompt():
    clear()
    print("How many passwords do you want to generate? :", style="#9770ed", end=" ")
    loop_times = int(input(""))
    alldata: list = []
    for i in range(loop_times):
        print(f"\n--------------------- Device [red]{i+1}[/red] ---------------------", style="#9770ed")
        print(f"What's the name of device [red]{i+1}[/red]? :", style="#bcbcff", end=" "); device_name = input("")
        if device_name == "": device_name = "Generic Device"
        
        print(f"What's the RAM in [red]'{device_name}'[/red] :", style="#bcbcff", end=" "); ram = input("")
        if ram == "": ram = "0"
        
        print(f"What's the HDD in [red]'{device_name}'[/red] :", style="#bcbcff", end=" "); hdd = input("")
        if hdd == "": hdd = "0"
        
        print(f"What's the CPU model in [red]'{device_name}'[/red] (int only):", style="#bcbcff", end=" "); cpu = input("")
        if cpu == "": cpu = "0"
        
        print(f"What's the GPU model in [red]'{device_name}'[/red] (int only):", style="#bcbcff", end=" "); gpu = input("")
        if gpu == "": gpu = "0"
        
        print(f"What's the OS Version in [red]'{device_name}'[/red] :", style="#bcbcff", end=" "); os_ver = input("")
        if os_ver == "": os_ver = "0"
        
        if device_name == "Generic Device" or ram == "0" or hdd == "0" or cpu == "0" or gpu == "0" or os_ver == "0": 
            print(f"[red]You didn't enter all the data for [bold]{device_name}[/bold][/red]"); print(f"[red]The data will be saved [bold]as is[/bold][/red]")
            
        combined = f"{device_name},{ram},{hdd},{cpu},{gpu},{os_ver}"
        
        alldata.append(combined)
        
    return alldata