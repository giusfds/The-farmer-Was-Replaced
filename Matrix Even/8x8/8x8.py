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
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if i < 3 and j < 3:  # superior esquerdo
                    # trigo
                    harvest()
                elif i < 3 and j >= 3:  # superior direito
                    # cenoura
                    if can_harvest():
                        harvest()
                    if num_items(Items.Carrot_Seed) < 1:
                        buycarrots(9)
                    if groudType():
                        till()
                    plant(Entities.Carrots)
                elif i >= 3 and j < 3:  # inferior esquerdo
                    # abóbora
                    if can_harvest():
                        harvest()
                    if num_items(Items.Pumpkin_Seed) < 1:
                        buyPumpkin(9)
                    if groudType():
                        till()
                    plant(Entities.Pumpkin)
                elif i >= 3 and j >= 3:  # inferior direito
                    # árvore
                    if can_harvest():
                        harvest()
                    plant(Entities.Bush)
                move(North)
            move(East)