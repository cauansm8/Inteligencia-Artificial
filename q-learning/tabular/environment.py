"""
Jogo: a fruta nasce no topo e cada cada passo desce um degrau

Objetivo: cesta esteja na posição x correta para pegar a fruta
"""


import numpy as np

class Pegue_a_Fruta:
    def __init__(self):
        self.altura = 6
        self.largura = 3 
        self.reset()

    def reset(self):
        self.cesta_x = 1

        self.fruta_x = np.random.randint(0, self.largura)
        # fruta no topo
        self.fruta_y = 0

        return self._get_state()
    
    def _get_state(self):
        return (self.cesta_x, self.fruta_x, self.fruta_y)

    def step(self, action):
        
        # distancia anterior ao movimento
        distancia_antes = abs(self.cesta_x - self.fruta_x)

        # esquerda
        if action == 0 and self.cesta_x > 0:
            self.cesta_x -= 1
        
        # direita
        elif action == 2 and self.cesta_x < self.largura - 1:
            self.cesta_x += 1
        
        # 2. A fruta desce uma linha
        self.fruta_y += 1
        
        recompensa = 0
        done = False

        # distancia pos movimento
        distancia_depois = abs(self.cesta_x - self.fruta_x)

        # verifica se chegou na ultima linha
        if self.fruta_y == self.altura - 1:
            done = True
            if self.cesta_x == self.fruta_x:
                recompensa = 10
            else:
                recompensa = -10 
        else:
            # recompensa intermediaria
            if distancia_depois < distancia_antes:
                recompensa = 0.5
            elif distancia_depois > distancia_antes:
                recompensa = -0.5

        return self._get_state(), recompensa, done