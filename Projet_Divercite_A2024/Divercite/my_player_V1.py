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

        '''n_cities = [0,0,0,0]
        n_resources = [0,0,0,0]
        for piece, n_piece in current_state.players_pieces_left[self.get_id()].items():
            color = piece[0]
            res_city = piece[1]
            if res_city == 'R':
                if color == 'R':
                    n_resources[0] +=1
                if color == 'G':
                    n_resources[1] +=1
                if color == 'B':
                    n_resources[2] +=1
                if color == 'Y':
                    n_resources[3] +=1
            if res_city == 'C':
                if color == 'R':
                    n_cities[0] +=1
                if color == 'G':
                    n_cities[1] +=1
                if color == 'B':
                    n_cities[2] +=1
                if color == 'Y':
                    n_cities[3] +=1'''
                
        

        if self == current_state.players[0]:
            opponent = current_state.players[1]
        else:
            opponent = current_state.players[0]

        
        possible_actions = current_state.generate_possible_heavy_actions()

        

        best_score = float('-inf')
        for action in possible_actions:
            
            score = action.get_next_game_state().scores[self.get_id()] - action.get_next_game_state().scores[opponent.get_id()] #- sum(n_cities) + min(n_cities) + min(n_resources)

            if best_score == None or score > best_score:
                best_score = score

        return best_score
    
    def exhaustive_search(self, current_state):
        def recursion(state, depth):

            if self == current_state.players[0]:
                opponent = current_state.players[1]
            else:
                opponent = current_state.players[0]
        
            if state.is_done():
                
                return state.scores[self.get_id()] - state.scores[opponent.get_id()], None

            best_value = float('-inf') if state.next_player == self else float('inf')
            best_action = None

            for action in state.generate_possible_light_actions():
                next_state = state.apply_action(action)
                value, _ = recursion(next_state, depth + 1)

                if state.next_player == self: 
                    if value > best_value:
                        best_value = value
                        best_action = action
                else:  
                    if value < best_value:
                        best_value = value
                        best_action = action

            return best_value, best_action

    
        return recursion(current_state, 0)    
    

    def maxValue(self, current_state, alpha, beta, depth):
        
        if depth >= 4:
            return self.heuristic(current_state), None
        best_value = float('-inf')
        best_action = None
        
        for action in current_state.generate_possible_light_actions():
        
            new_state = current_state.apply_action(action)
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
        #if current_state.get_step() == 36:
            #print("36")
            #best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=3)
        #elif current_state.get_step() == 37:
            #best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=3)
        #elif current_state.get_step() >= 37:
            #print(">37")
            #best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=4)
        if current_state.get_step() >= 37:
            print("Exhaustive search triggered")
            best_value, best_action = self.exhaustive_search(current_state)
        else:
            print(current_state.get_step())
            best_value, best_action = self.maxValue(current_state, float('-inf'), float('inf'), depth=1)
        return best_action
        



    
    

