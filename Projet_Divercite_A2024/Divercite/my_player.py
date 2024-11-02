from player_divercite import PlayerDivercite
from seahorse.game.action import Action
from seahorse.game.game_state import GameState
from game_state_divercite import GameStateDivercite
from seahorse.utils.custom_exceptions import MethodNotImplementedError

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
        for action in GameState.generate_possible_light_actions
        scores = GameStateDivercite.get_scores
        
        return score

    def maxValue(self, current_state, alpha, beta, depth):
        if depth >= 4:
            return self.heuristic(current_state, player), None
        best_value = float('-inf')
        best_action = None
        for action in GameState.generate_possible_heavy_actions(current_state):
            new_state = GameState.apply_action(current_state, action)
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
            return self.heuristic(current_state, player), None
        best_value = float('inf')
        best_action = None
        for action in GameState.generate_possible_heavy_actions(current_state):
            new_state = GameState.apply_action(current_state, action)
            value, _ = self.maxValue(new_state, alpha, beta, depth+1)
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

        #TODO
        raise MethodNotImplementedError()
