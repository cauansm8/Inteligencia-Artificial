import environment as env
import numpy as np

epsilon_decay = 0.998
min_epsilon = 0.01
actions_count = 3

class AgentCestaDeFrutas:

    def __init__(self, alpha = 0.5, gamma = 0.99, epsilon = 1.0):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def _get_q_values(self, state):
        
        # converte o estado para tupla caso ele venha como dicionário ou array (tava dando problema)
        if isinstance(state, dict):
            state = tuple(state.values())
        elif isinstance(state, np.ndarray):
            state = tuple(state)
        
        if state not in self.q_table:
            self.q_table[state] = np.zeros(actions_count)

        return self.q_table[state]

    # e-greedy
    def choose_action (self, state):
        acao = np.random.rand()

        # exploração -> aprender caminhos
        if acao < self.epsilon:
            return np.random.randint(0, actions_count)
        
        # explotação -> usar o conhecimento
        else:
            q_values = self._get_q_values(state)
            
            # encontra o maior valor Q
            max_q = np.max(q_values)
            
            # pega todas as ações que possuem esse mesmo valor máximo (evita o vício no índice 0 - dá vies)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            
            # escolhe aleatoriamente entre as melhores ações empatadas
            return np.random.choice(best_actions)

    # atualizando os q_valores da q_tabela
    def learn (self, state, action, reward, next_state, done):
        
        q_value_state = self._get_q_values(state)
        q_value_next_state = self._get_q_values(next_state)

        if done == True:
            q_value_next_state = 0
        else:
            q_value_next_state = np.max(q_value_next_state)


        q_value_state[action] += self.alpha * (reward + self.gamma * q_value_next_state - q_value_state[action])

    # diminuindo para que possa depois ter mais explotação que exploração
    def decay_epsilon (self):
        if self.epsilon > min_epsilon:
            self.epsilon *= epsilon_decay



