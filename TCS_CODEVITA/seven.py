def calculate_legal_piece_movements(chess_piece, current_position, chess_board):
    """Calculate valid moves for a piece given current board state"""
    legal_moves = set()
    column, row = ord(current_position[0]) - ord('A'), int(current_position[1]) - 1
    
    movement_patterns = {
        'Q': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)],
        'R': [(0,1), (1,0), (0,-1), (-1,0)],
        'B': [(1,1), (-1,-1), (1,-1), (-1,1)]
    }
    
    for delta_x, delta_y in movement_patterns[chess_piece]:
        current_column, current_row = column, row
        while True:
            current_column, current_row = current_column + delta_x, current_row + delta_y
            if not (0 <= current_column < 8 and 0 <= current_row < 8):
                break
            new_position = chr(current_column + ord('A')) + str(current_row + 1)
            if new_position not in chess_board:
                legal_moves.add(new_position)
            else:
                break
                
    return legal_moves

from functools import lru_cache

@lru_cache(maxsize=None)
def count_possible_configurations(chess_pieces, moves_ahead):
    if not chess_pieces or moves_ahead < 0:
        return 0
    if moves_ahead == 0:
        return 1
        
    chess_pieces = tuple(sorted(chess_pieces))  # Ensure consistent ordering
    current_board_state = {piece[1:]: piece[0] for piece in chess_pieces}
    possible_board_positions = set()
    
    for piece_location, piece_type in current_board_state.items():
        possible_moves = calculate_legal_piece_movements(piece_type, piece_location, current_board_state)
        
        for next_move in possible_moves:
            updated_board = current_board_state.copy()
            del updated_board[piece_location]
            updated_board[next_move] = piece_type
            
            board_configuration = tuple(sorted((piece_type + position) for position, piece_type in updated_board.items()))
            possible_board_positions.add(board_configuration)
            
    if moves_ahead == 1:
        return len(possible_board_positions)
    
    total_configurations = 0
    for new_configuration in possible_board_positions:
        total_configurations += count_possible_configurations(new_configuration, moves_ahead - 1)
    
    return total_configurations

def process_game():
    try:
        chess_pieces = input().split()
        moves_to_calculate = int(input())
        if moves_to_calculate < 0:
            print(0)
            return
        
        # Validate chess pieces format
        for piece in chess_pieces:
            if len(piece) != 3 or piece[0] not in 'QRB' or not ('A' <= piece[1] <= 'H') or not ('1' <= piece[2] <= '8'):
                print(0)
                return
        
        final_result = count_possible_configurations(tuple(chess_pieces), moves_to_calculate)
        print(final_result)
    except:
        print(0)

if __name__ == "__main__":
    process_game()
