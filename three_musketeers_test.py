import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        # Replace with tests
        self.assertEqual(string_to_location('A1'),(0,0))

    def test_location_to_string(self):
        # Replace with tests
        self.assertEqual(location_to_string((1,1)),'B2')

    def test_at(self):
        # Replace with tests
        self.assertEqual(at((0,0)), '-')
        self.assertEqual(at((2,1)), 'R')
        self.assertEqual(at((0,3)), 'M')
        
    def test_all_locations(self):
        # Replace with tests
        self.assertEqual([(0,0), (0,1), (0,2), (0,3), (0,4),
               (1,0), (1,1), (1,2), (1,3), (1,4),
               (2,0), (2,1), (2,2), (2,3), (2,4),
               (3,0), (3,1), (3,2), (3,3), (3,4),
               (4,0), (4,1), (4,2), (4,3), (4,4),], all_locations())

    def test_adjacent_location(self):
        # Replace with tests
        self.assertEqual(adjacent_location((2,2), 'left'), (2,1))
        self.assertEqual(adjacent_location((2,2), 'right'), (2,3))
        self.assertEqual(adjacent_location((2,2), 'up'), (1,2))
        self.assertEqual(adjacent_location((2,2), 'down'), (3,2))
        
    def test_is_legal_move_by_musketeer(self):
        # Replace with tests
        self.assertFalse(is_legal_move_by_musketeer((0,3), 'left'))
        self.assertTrue(is_legal_move_by_musketeer((1,3), 'left'))
        
    def test_is_legal_move_by_enemy(self):
        # Replace with tests
        self.assertTrue(is_legal_move_by_enemy((2,1), 'up'))
        self.assertFalse(is_legal_move_by_enemy((2,1), 'right'))                
        self.assertFalse(is_legal_move_by_enemy((2,1), 'down'))
                         
    def test_is_legal_move(self):
        # Replace with tests
        self.assertTrue(is_legal_move((1,3), 'left'))
        self.assertFalse(is_legal_move((1,3), 'up'))
        self.assertFalse(is_legal_move((1,3), 'right'))
        self.assertFalse(is_legal_move((0,3), 'up'))
        self.assertTrue(is_legal_move((2,1), 'up'))
        self.assertFalse(is_legal_move((2,1), 'right'))
        self.assertFalse(is_legal_move((2,1), 'down'))
        self.assertFalse(is_legal_move((4,3), 'down'))
        self.assertFalse(is_legal_move((0,0), 'right'))
        
    def test_can_move_piece_at(self):
        # Replace with tests
        set_board([ [R, R, _, M, _],
                    [R, R, R, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(can_move_piece_at((1,2)))
        self.assertFalse(can_move_piece_at((0,0)))
        self.assertTrue(can_move_piece_at((2,2)))
        self.assertFalse(can_move_piece_at((0,3)))
        self.assertFalse(can_move_piece_at((3,0)))
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        # Put additional tests here
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, M, _, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([ [R, R, M, _, _],
                    [M, M, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertFalse(has_some_legal_move_somewhere('R'))
        
    def test_possible_moves_from(self):
        # Replace with tests
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(possible_moves_from((0,0)),[])
        self.assertEqual(possible_moves_from((0,3)),[])
        self.assertIn('left', possible_moves_from((1,3)))
        self.assertIn('down', possible_moves_from((1,3)))
        self.assertNotIn('right', possible_moves_from((1,3)))
        self.assertNotIn('up', possible_moves_from((1,3)))
        self.assertIn('left', possible_moves_from((1,2)))
        self.assertIn('up', possible_moves_from((1,2)))
        self.assertNotIn('right', possible_moves_from((1,2)))
        self.assertNotIn('down', possible_moves_from((1,2)))
        
    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        # Replace with tests
        self.assertFalse(can_move_piece_at((0,0)))
        self.assertTrue(can_move_piece_at((2,2)))
        self.assertFalse(can_move_piece_at((0,4)))
        self.assertTrue(can_move_piece_at((0,3)))
        self.assertFalse(can_move_piece_at((1,3)))
        
    def test_is_legal_location(self):
        # Replace with tests
        self.assertTrue(is_legal_location((0,0)))
        self.assertFalse(is_legal_location((0,5)))
        self.assertFalse(is_legal_location((5,0)))
        self.assertFalse(is_legal_location((5,5)))
        
    def test_is_within_board(self):
        # Replace with tests
        self.assertTrue(is_within_board((0,4), 'left'))
        self.assertFalse(is_within_board((0,4), 'right'))
        self.assertFalse(is_within_board((0,4), 'up'))
        
    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        # Replace with tests
        R_pos_moves = [((0,2), 'left'), ((0,2), 'down')]
        self.assertCountEqual(all_possible_moves_for('R'), R_pos_moves)
        M_pos_moves = [((0,3), 'right'), ((0,3), 'left'), ((1,4), 'up')]
        self.assertCountEqual(all_possible_moves_for('M'), M_pos_moves)
        
    def test_make_move(self):
        # Replace with tests
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        make_move((0,2), 'left')
        new_board = ([ [_, R, _, M, R],
                     [_, _, _, M, M],
                     [_, _, _, _, _],
                     [_, _, _, _, _],
                     [_, _, _, _, _] ] )
        board = get_board()
        self.assertEqual(board,new_board)
        
    def test_choose_computer_move(self):
        # Replace with tests; should work for both 'M' and 'R'
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        R_pos_moves = [((0,2), 'left'), ((0,2), 'down')]
        self.assertIn(choose_computer_move('R'), R_pos_moves)
        M_pos_moves = [((0,3), 'right'), ((0,3), 'left'), ((1,4), 'up')]
        self.assertIn(choose_computer_move('M'), M_pos_moves)
        
    def test_is_enemy_win(self):
        # Replace with tests
        set_board([ [_, R, M, M, M],
                    [_, _, _, R, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [M, R, _, M, M],
                    [_, _, _, R, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, R, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, R, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, R, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, M, _],
                    [_, _, _, R, _],
                    [_, _, _, M, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, M, _, M],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, R, _, R, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, M, _, _],
                    [_, _, _, M, _],
                    [M, R, _, _, _],
                    [_, R, _, R, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())
unittest.main()
