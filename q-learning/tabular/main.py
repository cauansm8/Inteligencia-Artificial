"""
treinamento e teste gerado por IA
"""


from environment import Pegue_a_Fruta
from agent import AgentCestaDeFrutas

env = Pegue_a_Fruta()
agent = AgentCestaDeFrutas()

episodes = 20000
successes = 0

print("Iniciando o treinamento do agente...")

for episode in range(episodes):
    state = env.reset()
    done = False
    episode_reward = 0
    
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        
        agent.learn(state, action, reward, next_state, done)
        state = next_state
        episode_reward = reward
        

    if episode_reward > 0:
        successes += 1
            
    agent.decay_epsilon()

print(f"Treinamento concluído!")
print(f"Taxa de sucesso nos últimos episódios: {(successes / episodes) * 100:.2f}%")

# Testando o agente
print("\n--- Testando o Agente Treinado ---")
state = env.reset()
done = False
agent.epsilon = 0

while not done:
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    
    # Cria a grade visual
    grid = [["." for _ in range(env.largura)] for _ in range(env.altura)]
    
    f_y = int(env.fruta_y)
    f_x = int(env.fruta_x)
    b_x = int(env.cesta_x)
    
    # Limita o índice para o último válido da grade caso tenha chegado no fim
    f_y_safe = min(f_y, env.altura - 1)
    
    # Desenha os elementos na matriz
    grid[f_y_safe][f_x] = "🍎"
    grid[env.altura - 1][b_x] = "🧺"
    
    print(f"Ação tomada: {['Esquerda', 'Parado', 'Direita'][action]}")
    for row in grid:
        print(" ".join(row))
    print("-" * 15)
    
    state = next_state

if reward > 0:
    print("Resultado: Sucesso! 🧺🍎")
else:
    print("Resultado: Fruta caiu no chão! 💥")
