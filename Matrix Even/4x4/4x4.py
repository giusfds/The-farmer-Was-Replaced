def groudType():
    if get_ground_type() != Grounds.Soil:
        return True
    else:
        return False

def buycarrots(qnt):
    for cenouras in range(qnt):
        trade(Items.Carrot_Seed)

def buyPumpkin(qnt):
    for aboboras in range(qnt):
        trade(Items.Pumpkin_Seed)

while True:
        for i in range(4):
            for j in range(4):
                if i < 2 and j < 2:  # superior esquerdo
                    # trigo
                    harvest()
                elif i < 2 and j >= 2:  # superior direito
                    # cenoura
                    if can_harvest():
                        harvest()
                    if num_items(Items.Carrot_Seed) < 4:
                        buycarrots(4)
                    if groudType():
                        till()
                    plant(Entities.Carrots)
                elif i >= 2 and j < 2:  # inferior esquerdo
                    # abóbora
                    if can_harvest():
                        harvest()
                    if num_items(Items.Pumpkin_Seed) < 4:
                        buyPumpkin(4)
                    if groudType():
                        till()
                    plant(Entities.Pumpkin)
                elif i >= 2 and j >= 2:  # inferior direito
                    # árvore
                    if can_harvest():
                        harvest()
                    plant(Entities.Bush)
                move(North)
            move(East)