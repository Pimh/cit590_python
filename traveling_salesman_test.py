import unittest
from traveling_salesman import *

class TestTravelingSalesman(unittest.TestCase):

    def test_distance(self):
        pass
    
    def test_read_cities(self):
        road_map = read_cities('city-data.txt')
        city_tup1 = ('Alabama', 'Montgomery', '32.361538', '-86.279118')
        self.assertTrue('List', type(road_map)) 
        self.assertEqual(city_tup1, road_map[0])
        self.assertEqual(50, len(road_map))
        
    def test_print_cities(self):
        pass
    
    def test_compute_total_distance(self):
        road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844')]
        self.assertAlmostEqual(6346.5596363,compute_total_distance(road_map))
    
    def test_compute_two_cities_distance(self):
        city1 = ('California', 'Sacramento', '38.555605', '-121.468926')
        city2 = ('Hawaii', 'Honolulu', '21.30895', '-157.826182')
        self.assertAlmostEqual(2457.2223838, compute_two_cities_distance(city1,
                                                                         city2))

    def test_swap_adjacent_cities(self):
        road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        road_map_swap = [('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        road_map_swap_last = [('California', 'Sacramento', '38.555605', '-121.468926'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('Alabama', 'Montgomery', '32.361538', '-86.279118')]
        
        self.assertListEqual(road_map_swap, swap_adjacent_cities(road_map,0)[0])
        self.assertListEqual(road_map_swap_last, swap_adjacent_cities(road_map,4)[0])
        self.assertAlmostEqual(8583.00777947, swap_adjacent_cities(road_map,0)[1])
        self.assertAlmostEqual(7011.75403176, swap_adjacent_cities(road_map,4)[1])

    def test_swap_cities(self):
        road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        road_map_swap = [('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        road_map_swap_last = [('California', 'Sacramento', '38.555605', '-121.468926'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('Alabama', 'Montgomery', '32.361538', '-86.279118')]
        
        self.assertListEqual(road_map_swap, swap_cities(road_map,0,1)[0])
        self.assertListEqual(road_map_swap_last, swap_cities(road_map,4,0)[0])
        self.assertListEqual(road_map, swap_cities(road_map,0,0)[0])
        self.assertAlmostEqual(8583.00777947, swap_cities(road_map,0,1)[1])
        self.assertAlmostEqual(7011.75403176, swap_cities(road_map,4,0)[1])
        self.assertAlmostEqual(9624.20836699, swap_cities(road_map,0,0)[1])
        
    def test_find_best_cycle(self):
        road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        best_road_map = set([('California', 'Sacramento', '38.555605', '-121.468926'),
                         ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                         ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                         ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                         ('Alaska', 'Juneau', '58.301935', '-134.41974')])
        
        self.assertSetEqual(best_road_map, set(find_best_cycle(road_map)))

    def test_hill_climbing(self):
        road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                    ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                    ('California', 'Sacramento', '38.555605', '-121.468926')]
        
        best_road_map = set([('California', 'Sacramento', '38.555605', '-121.468926'),
                         ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                         ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                         ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                         ('Alaska', 'Juneau', '58.301935', '-134.41974')])
        
        self.assertLessEqual(6477.6236205, hill_climbing(road_map)[1])
        self.assertSetEqual(best_road_map, set(hill_climbing(road_map)[0]))
        
    def test_select_indices(self):
        self.assertGreater((50,50),select_indices(50))
        self.assertLessEqual((0,0),select_indices(50))
        self.assertNotEqual(select_indices(50)[0], select_indices(50)[1])
        
    def test_print_map(self):
        pass
    
unittest.main()
