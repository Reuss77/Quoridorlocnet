import numpy as np


class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate, discount_factor, epsilon):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            # Exploration : Choix d'une action aléatoire
            action = np.random.randint(self.num_actions)
        else:
            # Exploitation : Choix de l'action avec la plus grande valeur Q
            action = np.argmax(self.q_table[state])
        return action

    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[state, action]
        max_future_q = np.max(self.q_table[next_state])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * \
            (reward + self.discount_factor * max_future_q)
        self.q_table[state, action] = new_q


# Définition des hyperparamètres
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.8

# Initialisation de l'agent Q-learning
num_states = 100  # Remplacez par le nombre d'états réel de votre jeu Quoridor
num_actions = 4  # Remplacez par le nombre d'actions possibles réel de votre jeu Quoridor
agent = QLearningAgent(num_states, num_actions,
                       learning_rate, discount_factor, epsilon)

# Boucle d'apprentissage
num_episodes = 1000  # Nombre d'épisodes d'apprentissage
for episode in range(num_episodes):
    state = env.reset()  # Remplacez "env" par votre environnement de jeu Quoridor
    done = False
    while not done:
        action = agent.choose_action(state)
        # Remplacez "env" par votre environnement de jeu Quoridor
        next_state, reward, done = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        state = next_state

# Après l'apprentissage, vous pouvez utiliser l'agent entraîné pour jouer au Quoridor
state = env.reset()
done = False
while not done:
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    state = next_state
    # Effectuer l'action choisie dans votre jeu Quoridor et mettre à jour l'état du jeu


# # crée un tuple "winer" avec le nom du joueur gagnant et le nombre de tours
# # crée une liste de tuples "winners" avec les noms des joueurs gagnants et leurs nombres de tours

# winners = [("paul", 8), ("pierre", 9)]


# def display_winner(self):
#     message = ""
#     num_winners = len(self.winner)

#     if num_winners == 1:
#         name, tour = self.winner[0]
#         message = f"Bravo à {name.capitalize()} qui finit 1er en {tour} tour."
#     elif num_winners == 2:
#         names, tours = zip(*self.winner)
#         if len(set(tours)) == 1:
#             message = f"{', '.join(name.capitalize() for name in names)} ont tous deux gagné au tour {tours[0]}."
#         else:
#             message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()} a gagné au tour {tours[1]}."
#     elif num_winners == 3:
#         names, tours = zip(*self.winner)
#         if len(set(tours)) == 1:
#             message = f"{', '.join(name.capitalize() for name in names)} ont tous trois gagné au tour {tours[0]}."
#         elif len(set(tours[:2])) == 1:
#             message = f"{names[0].capitalize()} et {names[1].capitalize()} ont tous deux gagné au tour {tours[0]} et {names[2].capitalize()} a gagné au tour {tours[2]}."
#         elif len(set(tours[1:])) == 1:
#             message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()} et {names[2].capitalize()} ont tous deux gagné au tour {tours[1]}."
#         else:
#             message = f"{names[0].capitalize()} a gagné au tour {tours[0]}, {names[1].capitalize()} a gagné au tour {tours[1]} et {names[2].capitalize()} a gagné au tour {tours[2]}."
#     elif num_winners == 4:
#         names, tours = zip(*self.winner)
#         if len(set(tours)) == 1:
#             message = f"{', '.join(name.capitalize() for name in names)} ont tous quatre gagné au tour {tours[0]}."
#         elif len(set(tours[:2])) == 1 and len(set(tours[2:])) == 1:
#             message = f"{names[0].capitalize()} et {names[1].capitalize()} ont tous deux gagné au tour {tours[0]} et {names[2].capitalize()} et {names[3].capitalize()} ont tous deux gagné au tour {tours[2]}."
#         elif len(set(tours[:3])) == 1 and len(set(tours[3:])) == 1:
#             message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()}, {names[2].capitalize()} et {names[3].capitalize()} ont tous trois gagné au tour {tours[2]}."
#         else:
#             message = f"{names[0].capitalize()} a gagné au tour {tours[0]}, {names[1].capitalize()} a gagné au tour {tours[1]}, {names[2].capitalize()} a gagné au tour {tours[2]} et {names[3].capitalize()} a gagné au tour {tours[3]}."

#     return message


# print(display_winner(winners))