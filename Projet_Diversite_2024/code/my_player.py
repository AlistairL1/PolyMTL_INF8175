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

    def compute_action(self, current_state: GameState, remaining_time: int = 1e9, **kwargs) -> Action:
        """
        Use the minimax algorithm to choose the best action based on the heuristic evaluation of game states.

        Args:
            current_state (GameState): The current game state.

        Returns:
            Action: The best action as determined by minimax.
        """

        def evaluate(self, state: GameState) -> int:
            """
            Evaluation function to assess the desirability of a game state.
            For simplicity, this function will need to be adapted based on the game's specific rules.

            Args:
                state (GameState): The current game state.

            Returns:
                int: Score representing the desirability of the state.
            """
            # TODO: Define a proper evaluation function based on the game
            return state.get_score(self.piece_type)  # Placeholder

        def minimax(self, state: GameState, depth: int, maximizing_player: bool) -> int:
            """
            The minimax algorithm to evaluate the game state.

            Args:
                state (GameState): The current game state.
                depth (int): The depth limit for the minimax recursion.
                maximizing_player (bool): Boolean indicating if we are maximizing or minimizing.

            Returns:
                int: The best score the current player can achieve from this state.
            """
            if depth == 0 or state.is_done():
                return self.evaluate(state)

            if maximizing_player:
                max_eval = float('-inf')
                for action in state.get_legal_actions(self.piece_type):
                    new_state = state.generate_successor(self.piece_type, action)
                    eval = self.minimax(new_state, depth - 1, False)
                    max_eval = max(max_eval, eval)
                return max_eval
            else:
                min_eval = float('inf')
                opponent_piece_type = 'X' if self.piece_type == 'O' else 'O'
                for action in state.get_legal_actions(opponent_piece_type):
                    new_state = state.generate_successor(opponent_piece_type, action)
                    eval = self.minimax(new_state, depth - 1, True)
                    min_eval = min(min_eval, eval)
                return min_eval

        def compute_action(self, current_state: GameState, remaining_time: int = 1e9, **kwargs) -> Action:
            """
            Use the minimax algorithm to choose the best action based on the heuristic evaluation of game states.

            Args:
                current_state (GameState): The current game state.

            Returns:
                Action: The best action as determined by minimax.
            """
            best_action = None
            best_value = float('-inf')

            # Iterate over possible actions
            for action in current_state.get_legal_actions(self.piece_type):
                # Generate successor state for the action
                new_state = current_state.generate_successor(self.piece_type, action)
                # Use minimax to evaluate the outcome of the action
                action_value = self.minimax(new_state, depth=3, maximizing_player=False)

                # Keep track of the best action
                if action_value > best_value:
                    best_value = action_value
                    best_action = action

            return best_action
        