from backend.write import write_csv as wc
from backend.prompts import prompt as qp
from backend.table import table
from backend.code import code as cd
from backend.algo import algo as al
from rich import console

try:
    import rich, pandas, subprocess
except ModuleNotFoundError:
    try:
        try:
            import os
            os.system("pip install rich")
            os.system("pip install pandas")
            os.system("pip install subprocess")
        except:
            os.system("pip3 install rich")
            os.system("pip3 install pandas")
            os.system("pip3 install subprocess")
    except:
        import sys
        print("Please install rich, subprocess and pandas manually")
        print("Press enter to exit...")
        sys.exit()

def start():
    print2 = console.Console().print
    print2("Welcome to the Password Generator", style="#9770ed")
    print2("This program will generate passwords for you", style="#9770ed")
    print2("Please press enter to continue...", style="#9770ed")
    if input("") == "r": cd.decode()
    
    datalist: list = qp()
    finallist: list = []
    tb = table()
    org_device, org_ram, org_hdd, org_cpu, org_gpu, org_os = '', '', '', '', '', ''
    
    print2(f"How many digits do you want in your password? :", style="bold red", end=" ")
    digits = int(input(""))
    print2(f"\n--------------------- Password Generation ---------------------", style="#9770ed")
    
    for i in datalist:
        org_device = i.split(",")[0]
        org_ram = i.split(",")[1]
        org_hdd = i.split(",")[2]
        org_cpu = i.split(",")[3]
        org_gpu = i.split(",")[4]
        org_os = i.split(",")[5]
        org_imput_params = f"{org_ram} ,{org_hdd} ,{org_cpu} ,{org_gpu} ,{org_os}"
        
        print2(f"Generating password for [red]{org_device}[/red]...", style="#9770ed")
        
        device_name = cd.encode(i.split(",")[0])
        ram = cd.encode(i.split(",")[1])
        hdd = cd.encode(i.split(",")[2])
        cpu = cd.encode(i.split(",")[3])
        gpu = cd.encode(i.split(",")[4])
        os_ver = cd.encode(i.split(",")[5])
        input_params = f"{ram}, {hdd}, {cpu}, {gpu}, {os_ver}"
        
        finallist.append(wc(device_name, cd.encode(al(ram, hdd, cpu, gpu, os_ver, digits)), input_params))
        tb.add(f"{org_device}", f"{al(ram, hdd, cpu, gpu, os_ver, digits)}", f"{org_imput_params}")
    
    tb.print()
    return finallist