from .models import Computadora, Hardware, Periferico, Diferencias, Softwares, Programs
from django.contrib import messages

def print_errors(req, msgs):
    if msgs:
        for i in msgs:
            messages.error(req, i)

def crear_hard(req, computadora = None, nombre = None, fabricante = None, modelo = None, capacidad_gb = None, velocidad = None, num_de_serie = None ):
    hards = Hardware.objects.filter(baja = 0)
    myMsgs = []

    try:
        hards.create(
            computadora = computadora,
            nombre = nombre,
            fabricante = fabricante,
            modelo = modelo,
            capacidad_gb = capacidad_gb,
            velocidad = velocidad,
            num_de_serie = num_de_serie,
        )
    except:
        myMsgs.append(f"No se pudo crear {nombre} para {computadora}.")
    print_errors(req, myMsgs)

def crear_peri(req, computadora = None,nombre = None,fabricante = None,modelo = None,num_inventario = None,num_de_serie = None):
    peris = Periferico.objects.all()
    myMsgs = []

    try:
        peris.create(
            computadora=computadora,
            nombre=nombre,
            fabricante=fabricante,
            modelo=modelo,
            num_inventario=num_inventario,
            num_de_serie=num_de_serie,
        )
    except:
        myMsgs.append(f"No se pudo crear {nombre} para {computadora}.")
    print_errors(req, myMsgs)

def crear_diferencia(computadora, campo, cambio):
    dife = Diferencias.objects.filter(computadora=computadora)
    flag = False
    for i in dife:
        # print(i.campo , campo , i.cambio , cambio)
        if i.campo == campo and i.cambio == cambio:
            flag = True
    if flag == False:
        try:
            dife.create(
                computadora=computadora,
                campo=campo,
                cambio=cambio,
            )
        except:
            # print("+++++++++++++++Error++++++++++++++++++++")
            # print(f"diferencia {computadora} {campo} {cambio}")        
            # print("+++++++++++++++Error++++++++++++++++++++")
            pass

def get_dif(value1, value2):
    if value1 != value2:
        dif = value1 - value2
        dif = str(dif) if dif < 0 else f"+{dif}"
        return dif

def create_storages(req, dom, new_comp):
    storages = dom.find_all('STORAGES')
    res = [i for i in storages if i.find('DESCRIPTION', text="Unidad de disco") and i.find('TYPE', text="Fixed hard disk media")]

    for s in res:
        if s.DISKSIZE.getText():
            if s.SERIALNUMBER.getText() :
                    crear_hard(req, new_comp, "Disco", s.MANUFACTURER.getText(), s.NAME.getText(), s.DISKSIZE.getText(), None, s.SERIALNUMBER.getText())
            else:
                crear_hard(req, new_comp, "Disco", s.MANUFACTURER.getText(), s.NAME.getText(), s.DISKSIZE.getText(), None, None)
    
def check_storage(existing_comp, existing_hard, dom):
    current_storage = existing_hard.filter(nombre = 'Disco')
    storages = dom.find_all('STORAGES')
    new_storage = [i for i in storages if i.find('DESCRIPTION', text="Unidad de disco") and i.find('TYPE', text="Fixed hard disk media") and not i.find('DISKSIZE', text="")]
    
    # comprobar cant de discos #ok
    dif = get_dif(len(new_storage), current_storage.count())
    if dif:
        crear_diferencia(existing_comp, "Diferencia en cant de discos", dif)
    # comprobar capacidad de discos #ok
    current_cap = 0
    for i in current_storage:
        current_cap += int(str(i.capacidad_gb).split(" ")[0])
    new_cap = 0
    for i in new_storage:
        new_cap += int(i.DISKSIZE.getText())
    
    dif = get_dif(new_cap, current_cap)
    if dif:
        crear_diferencia(existing_comp, "Diferencia en capacidad de discos", dif)    

def create_ram(req, dom, new_comp):
    memories = dom.findAll("MEMORIES")
    rams = [i for i in memories if i.CAPACITY.getText() != "0"]
    for s in rams:
        if s.SERIALNUMBER.getText():
            crear_hard(req, new_comp,"RAM",None,None,s.CAPACITY.getText(),s.SPEED.getText(), s.SERIALNUMBER.getText())
        else:
            crear_hard(req, new_comp,"RAM",None,None,s.CAPACITY.getText(),s.SPEED.getText(), None)

def check_ram(existing_comp, existing_hard, dom):
    memories = dom.findAll("MEMORIES")
    new_rams = [i for i in memories if i.CAPACITY.getText() != "0"]

    current_ram = existing_hard.filter(nombre = 'RAM')
    # comprobar cant de ram
    dif = get_dif(len(new_rams), current_ram.count())
    if dif:
        crear_diferencia(existing_comp, "Diferencia en cant de ram", dif)
    # comprobar capacidad de ram
    current_cap = 0
    for i in current_ram:
        current_cap += int(i.capacidad_gb)
    new_cap = 0
    for i in new_rams:
        new_cap += int(i.CAPACITY.getText())

    dif = get_dif(new_cap, current_cap)
    if dif:
        crear_diferencia(existing_comp, "Diferencia en capacidad de ram", dif)
    # deberia agregar diferencia en velocidad y en tipo de ram pero me pesa

def create_cpu(req, dom, new_comp):
    cpu = dom.CPUS
    crear_hard(req, new_comp, "CPU", cpu.MANUFACTURER.getText(), cpu.TYPE.getText(), cpu.CORES.getText() + " cores", cpu.SPEED.getText(), None)

def check_cpu(existing_comp, existing_hard, dom):
    curr_cpu = existing_hard.filter(nombre = "CPU").first()
    
    cpu = dom.CPUS
    if curr_cpu:
        if cpu.TYPE.getText() != curr_cpu.modelo:
            crear_diferencia(existing_comp, "Cambio de Cpu", cpu.TYPE.getText())
    else:
        if cpu.TYPE.getText():
            crear_diferencia(existing_comp, "Agrego de Cpu", cpu.TYPE.getText())

def create_board(req, dom, new_comp):
    board = dom.BIOS
    if board.SSN.getText():
        crear_hard(req, new_comp, "BOARD", board.SMANUFACTURER.getText(), board.SMODEL.getText(), None, None, board.SSN.getText())
    else:
        crear_hard(req, new_comp, "BOARD", board.SMANUFACTURER.getText(), board.SMODEL.getText(), None, None, None)

def check_board(existing_comp, existing_hard, dom):
    curr_board = existing_hard.filter(nombre = "BOARD").first()
    board = dom.BIOS
    if curr_board:
        if board.SMODEL.getText() != curr_board.modelo:
            crear_diferencia(existing_comp, "Cambio de board", board.SMODEL.getText())
    else:
        if board.SMODEL.getText():
            crear_diferencia(existing_comp, "Agrego de board", board.SMODEL.getText())

def create_teclados(req, dom, new_comp):
    teclados = dom.findAll("INPUTS")
    tecs = [i for i in teclados if "DameWare" not in i.DESCRIPTION.getText() and i.TYPE.getText() == "Keyboard"]
    # return len(tecs)
    for i in range(len(tecs)):
        crear_peri(req, new_comp, "Teclado", None, None, None, None)

def check_teclado(existing_comp, existing_peri, dom):
    curr_key = existing_peri.filter(nombre = 'Teclado')
    teclados = dom.findAll("INPUTS")
    new_key = [i for i in teclados if "DameWare" not in i.DESCRIPTION.getText() and i.TYPE.getText() == "Keyboard"]

    dif = get_dif(len(new_key), curr_key.count())
    if dif:
        crear_diferencia(existing_comp, "Diferencia en cant de teclados", dif)

def create_mouse(req, dom, new_comp):
    mouses = dom.findAll("INPUTS")
    mos = [i for i in mouses if i.TYPE.getText() == "Pointing"]    
    # return len(mos)    
    for i in range(len(mos)):
        crear_peri(req, new_comp, "Mouse", None, None, None, None)

def check_mouse(existing_comp, existing_peri, dom):
    curr_mou = existing_peri.filter(nombre = 'Mouse')
    mouses = dom.findAll("INPUTS")
    new_mou = [i for i in mouses if i.TYPE.getText() == "Pointing"]    

    dif = get_dif(len(new_mou), curr_mou.count())
    if dif:
        crear_diferencia(existing_comp, "Diferencia en cant de mouse", dif)

def create_monitors(req, dom, new_comp):
    for i in dom.findAll("MONITORS"):
        if i.SERIAL.getText():
            crear_peri(req, new_comp, "Monitor", i.MANUFACTURER.getText(), i.CAPTION.getText(), None, i.SERIAL.getText())
        else:
            crear_peri(req, new_comp, "Monitor", i.MANUFACTURER.getText(), i.CAPTION.getText(), None, None)

def check_monitor(existing_comp, existing_peri, dom):#ver si funciona si existing_comp
    # cant de monitores #ok
    curr_mon = existing_peri.filter(nombre = "Monitor")
    new_mon = dom.findAll("MONITORS")
    dif = get_dif(len(new_mon), curr_mon.count())
    if dif:
        crear_diferencia(existing_comp, "Diferencia en cant de monitores", dif)
    # modelo
    for cur, new in zip(curr_mon, new_mon):
        if cur.modelo != new.CAPTION.getText():
            crear_diferencia(existing_comp, "Cambio de modelo de monitor", new.CAPTION.getText())

def create_progs(req, dom, new_comp):
    """Looks for each program in Programs and if present pass it to a res list, 
    from said list, creates a soft later"""
    myMsgs = []
    progs = Programs.objects.all()
    softs = Softwares.objects.filter(computadora = new_comp)
    comp_softwares = dom.findAll("SOFTWARES")
    
    if progs:
        for p in progs:
            for i in comp_softwares:
                # check if computer has program
                if p.nombre.lower() in str(i.NAME.getText()).lower():
                    # check if computer was restrated to program
                    if not softs.filter(nombre=p):
                        try:
                            softs.create(
                                computadora = new_comp,
                                nombre = p,            
                            )
                        except:
                            myMsgs.append(f"No se pudo crear {p.nombre} para {new_comp}.")
                    break
    print_errors(req, myMsgs)

def get_ip(dom):
    network = dom.findAll("NETWORKS")
    ip = [i.IPADDRESS.getText() for i in network if i.STATUS.getText() == "Up" and i.TYPE.getText() == "Ethernet"]
    return ip[0]