# Inicializando a matriz de 8x8 com um dicionário
#O(1)
matriz_estado = {(i, j): {'harvested': False, 'tilled': False} for i in range(8) for j in range(8)}

def moveSup():
    move(North)

def moveFrontP(espacos):
    for i in range(espacos):
        move(North)

def moveInf():
    move(South)

def moveBackP(espacos):
    for i in range(espacos):
        move(South)

def moveDir():
    move(East)

def moveDirP(espacos):
    for i in range(espacos):
        move(East)

def moveEsq():
    move(West)

def VoltarCasa():
    while get_pos_x() > 0:
        move(West)
    while get_pos_y() > 0:
        move(South)

def colher(x, y):
    if not matriz_estado[(x, y)]['harvested']:
        harvest()
        matriz_estado[(x, y)]['harvested'] = True

def tipoDeSolo(x, y):
    return get_ground_type() != Grounds.Soil

def tilling(x, y):
    if tipoDeSolo(x, y):
        till()
        matriz_estado[(x, y)]['tilled'] = True

def compraCenoura(qnt):
    for cenouras in range(qnt):
        trade(Items.Carrot_Seed)

def comprarAbobora(qnt):
    for aboboras in range(qnt):
        trade(Items.Pumpkin_Seed)

def plantar(x, y, tipo):
    if tipo == 'carrot':
        if can_harvest():
            harvest()
        if num_items(Items.Carrot_Seed) < 1:
            compraCenoura(9)
        tilling(x, y)
        plant(Entities.Carrots)
    elif tipo == 'pumpkin':
        if can_harvest():
            harvest()
        if num_items(Items.Pumpkin_Seed) < 1:
            comprarAbobora(9)
        tilling(x, y)
        plant(Entities.Pumpkin)
    elif tipo == 'bush':
        if can_harvest():
            harvest()
        plant(Entities.Bush)

def manage_farm():
    while True:
        for x in range(8):
            for y in range(8):
                if x < 4 and y < 4:  # superior esquerdo
                    colher(x, y)
                elif x < 4 and y >= 4:  # superior direito
                    plantar(x, y, 'carrot')
                elif x >= 4 and y < 4:  # inferior esquerdo
                    plantar(x, y, 'pumpkin')
                elif x >= 4 and y >= 4:  # inferior direito
                    plantar(x, y, 'bush')
                move(North)
            move(East)
