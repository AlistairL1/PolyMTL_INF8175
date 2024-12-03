from player_divercite import PlayerDivercite
from seahorse.game.action import Action
from seahorse.game.game_state import GameState
from game_state_divercite import GameStateDivercite
from seahorse.utils.custom_exceptions import MethodNotImplementedError
import random

class MyPlayer(PlayerDivercite):
    """
    Player class for Divercite game that makes random moves.

    Attributes:
        piece_type (str): piece type of the player
    """

    def __init__(self, piece_type: str, name: str = "MyPlayer"):
        """
        Initialize the PlayerDivercite instance.

        Args:
            piece_type (str): Type of the player's game piece
            name (str, optional): Name of the player (default is "bob")
            time_limit (float, optional): the time limit in (s)
        """
        super().__init__(piece_type, name)
    


    def heuristic(self, current_state):
        if self == current_state.players[0]:
            opponent = current_state.players[1]
        else:
            opponent = current_state.players[0]

        
        possible_actions = current_state.generate_possible_heavy_actions()

        best_score = float('-inf')
        for action in possible_actions:
            score = action.get_next_game_state().scores[self.get_id()] - action.get_next_game_state().scores[opponent.get_id()]
            if best_score == None or score > best_score:
                best_score = score

        return best_score
    
    
        
    

    def maxValue(self, current_state, alpha, beta, depth):
        
        if depth >= 4:
            return self.heuristic(current_state), None
        best_value = float('-inf')
        best_action = None
        
        for action in current_state.generate_possible_light_actions():
        
            new_state = current_state.apply_action(action)
            if current_state.get_step() >= 38:
                value, _ = self.minValue(new_state, alpha, beta, 2)
            else:
                value, _ = self.minValue(new_state, alpha, beta, depth+1)
            if value > best_value:
                best_value = value
                best_action = action
                alpha = max(alpha, best_value)
                if best_value >= beta: 
                    return best_value, best_action
        return best_value, best_action
    
    def minValue(self, current_state, alpha, beta, depth):
        
        
        if depth >= 4:
            return self.heuristic(current_state), None
        best_value = float('inf')
        best_action = None
        
        for action in current_state.generate_possible_light_actions():
            new_state = current_state.apply_action(action)
            if current_state.get_step() >= 38:
                value, _ = self.minValue(new_state, alpha, beta, 2)
            else:
                value, _ = self.minValue(new_state, alpha, beta, depth+1)
            if value < best_value:
                best_value = value
                best_action = action
                beta = min(beta, best_value)
                if best_value <= alpha:
                    return best_value, best_action
        return best_value, best_action


    def compute_action(self, current_state: GameState, remaining_time: int = 1e9, **kwargs) -> Action:
        """
        Use the minimax algorithm to choose the best action based on the heuristic evaluation of game states.

        Args:
            current_state (GameState): The current game state.

        Returns:
            Action: The best action as determined by minimax.
        """
        if current_state.get_step() <=2:
            possible_actions = current_state.get_possible_light_actions()
            return random.choice(list(possible_actions))
        elif current_state.get_step() > 2 and current_state.get_step() < 25:
            best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=1)
            return best_action
        elif current_state.get_step() >= 25 and current_state.get_step() < 36:
            best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=0)
            return best_action
        else:
            best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=1)
            return best_action
        



    
    

