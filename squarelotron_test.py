'''CIT590 HW5 - SquareLotron_test
    Pimkhuan (Pim) Hannanta-anan
    Due 10/4/2016 '''

import unittest
from squarelotron import *

class squarelotron_test(unittest.TestCase):
    
    def test_make_squarelotron(self):
        num_list = list(range(1,26))
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        self.assertListEqual(squarelotron, make_squarelotron(num_list))
        print_squarelotron(squarelotron)
        
    def test_make_list(self):       
        num_list = list(range(1,26))
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        self.assertListEqual(num_list, make_list(squarelotron))
        
    def test_upside_down_flip(self):
        #RETURN NEW SQUARELOTRON, DO NOT MODIFY THE ORIGINAL ONE
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        squarelotron_oflip = [[21,22,23,24,25],
                            [6,7,8,9,10],
                            [11,12,13,14,15],
                            [16,17,18,19,20],
                            [1,2,3,4,5]]
        squarelotron_iflip = [[1,2,3,4,5],
                            [16,17,18,19,20],
                            [11,12,13,14,15],
                            [6,7,8,9,10],
                            [21,22,23,24,25]]
        self.assertListEqual(squarelotron_oflip,
                             upside_down_flip(squarelotron,'O'))
        self.assertNotEqual(squarelotron_oflip,squarelotron)
        self.assertListEqual(squarelotron_iflip,
                             upside_down_flip(squarelotron,'I'))
        self.assertNotEqual(squarelotron_iflip,squarelotron)
        
    def test_left_right_flip(self):
        #RETURN NEW SQUARELOTRON, DO NOT MODIFY THE ORIGINAL ONE
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        squarelotron_oflip = [[5,2,3,4,1],
                            [10,7,8,9,6],
                            [15,12,13,14,11],
                            [20,17,18,19,16],
                            [25,22,23,24,21]]
        squarelotron_iflip = [[1,4,3,2,5],
                            [6,9,8,7,10],
                            [11,14,13,12,15],
                            [16,19,18,17,20],
                            [21,24,23,22,25]]
        self.assertListEqual(squarelotron_oflip,
                             left_right_flip(squarelotron,'O'))
        self.assertNotEqual(squarelotron_oflip,squarelotron)
        self.assertListEqual(squarelotron_iflip,
                             left_right_flip(squarelotron,'I'))
        self.assertNotEqual(squarelotron_iflip,squarelotron)
                              
    def test_inverse_diagonal_flip(self):
        #RETURN NEW SQUARELOTRON, DO NOT MODIFY THE ORIGINAL ONE
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        squarelotron_oflip = [[1,2,3,4,21],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [5,22,23,24,25]]
        squarelotron_iflip = [[1,2,3,4,5],
                        [6,7,8,17,10],
                        [11,12,13,14,15],
                        [16,9,18,19,20],
                        [21,22,23,24,25]]
        self.assertListEqual(squarelotron_oflip,
                             inverse_diagonal_flip(squarelotron,'O'))
        self.assertNotEqual(squarelotron_oflip,squarelotron)
        self.assertListEqual(squarelotron_iflip,
                             inverse_diagonal_flip(squarelotron,'I'))
        self.assertNotEqual(squarelotron_iflip,squarelotron)
        
    def test_main_diagonal_flip(self):
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        squarelotron_oflip = [[25,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,1]]
        squarelotron_iflip = [[1,2,3,4,5],
                        [6,19,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,7,20],
                        [21,22,23,24,25]]
        self.assertListEqual(squarelotron_oflip,
                             main_diagonal_flip(squarelotron,'O'))
        self.assertNotEqual(squarelotron_oflip,squarelotron)
        self.assertListEqual(squarelotron_iflip,
                             main_diagonal_flip(squarelotron,'I'))
        self.assertNotEqual(squarelotron_iflip,squarelotron)

    def test_isvalid_ring(self):
        self.assertTrue(isvalid_ring('I'))
        self.assertTrue(isvalid_ring('O'))
        self.assertFalse(isvalid_ring('Q'))
        
    def test_isvalid_flip(self):
        self.assertTrue(isvalid_flip('UD'))
        self.assertTrue(isvalid_flip('LR'))
        self.assertTrue(isvalid_flip('ID'))
        self.assertTrue(isvalid_flip('MD'))
        
    def test_isvalid_input(self):
        self.assertTrue(isvalid_input('UDI'))
        self.assertTrue(isvalid_input('UDO'))
        self.assertTrue(isvalid_input('LRI'))
        self.assertTrue(isvalid_input('LRO'))
        self.assertTrue(isvalid_input('IDI'))
        self.assertTrue(isvalid_input('IDO'))
        self.assertTrue(isvalid_input('MDI'))
        self.assertTrue(isvalid_input('MDO'))

    def test_make_move(self):
        squarelotron = [[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]]
        self.assertListEqual([[21,22,23,24,25],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [1,2,3,4,5]], make_move(squarelotron,'UDO'))
        self.assertListEqual([[1,2,3,4,5],
                        [16,17,18,19,20],
                        [11,12,13,14,15],
                        [6,7,8,9,10],
                        [21,22,23,24,25]], make_move(squarelotron,'UDI'))
        self.assertListEqual([[5,2,3,4,1],
                            [10,7,8,9,6],
                            [15,12,13,14,11],
                            [20,17,18,19,16],
                            [25,22,23,24,21]], make_move(squarelotron,'LRO'))
        self.assertListEqual([[1,4,3,2,5],
                            [6,9,8,7,10],
                            [11,14,13,12,15],
                            [16,19,18,17,20],
                            [21,24,23,22,25]], make_move(squarelotron,'LRI'))
        self.assertListEqual([[1,2,3,4,21],
                            [6,7,8,9,10],
                            [11,12,13,14,15],
                            [16,17,18,19,20],
                            [5,22,23,24,25]], make_move(squarelotron,'IDO'))
        self.assertListEqual([[1,2,3,4,5],
                            [6,7,8,17,10],
                            [11,12,13,14,15],
                            [16,9,18,19,20],
                            [21,22,23,24,25]], make_move(squarelotron,'IDI'))
        self.assertListEqual([[25,2,3,4,5],
                            [6,7,8,9,10],
                            [11,12,13,14,15],
                            [16,17,18,19,20],
                            [21,22,23,24,1]], make_move(squarelotron,'MDO'))
        self.assertListEqual([[1,2,3,4,5],
                            [6,19,8,9,10],
                            [11,12,13,14,15],
                            [16,17,18,7,20],
                            [21,22,23,24,25]], make_move(squarelotron,'MDI'))

    
unittest.main()
