from math import *
import random

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c

def read_cities(file_name):
    '''Read in the cities from the given file_name, and
    return them as a list of four-tuples:
    [(state, city, latitude, longitude), ...]'''

    file_path = "./" + file_name
    city_stream = open(file_path,'r')
    city_list = city_stream.readlines()
    road_map = []

    '''Read in lines and store city locations in tuples'''
    for line in city_list:
        line_list = line.strip().split('\t')
        line_tuple = (line_list[0], line_list[1], line_list[2], line_list[3])
        road_map.append(line_tuple)
        
    return road_map
 
def print_cities(road_map):
    '''Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.'''

    print('{:15}{:18}{:10}{:10}'.format('State','City','Latitude','Longtitude'))
    table_line = '-'*60
    print(table_line)
    
    for city_tup in road_map:
        print('{:15}{:15}{:10.2f}{:10.2f}'.format(city_tup[0], city_tup[1],
                                                  float(city_tup[2]),
                                                  float(city_tup[3])))
                 
def compute_total_distance(road_map):
    '''Returns, as a floating point number, the sum of the distances
    of all the connections in the road_map.'''
    tot_dist = 0
    for i in range(0,len(road_map)):
        lat1deg = float(road_map[i][2])
        long1deg = float(road_map[i][3])
        if i == len(road_map)-1:
            lat2deg = float(road_map[0][2])
            long2deg = float(road_map[0][3])
        else:
            lat2deg = float(road_map[i+1][2])
            long2deg = float(road_map[i+1][3])
        dist = distance(lat1deg, long1deg, lat2deg, long2deg)
        tot_dist = tot_dist + dist

    return tot_dist
    
def swap_adjacent_cities(road_map, index):
    '''Take the city at location index in the road_map,
    and the city at location index+1 (or at 0, if index refers to the last element in the list),
    swap their positions in the road_map,
    compute the new total distance, and
    return the tuple (new_road_map, new_total_distance).'''

    new_road_map = road_map
    if index+1 > len(road_map)-1:
        index2 = 0
    else:
        index2 = index+1
    
    new_tup = swap_cities(roadmap, index1, index2)
    return new_tup
    
def swap_cities(road_map, index1, index2):
    '''Take the city at location index in the road_map,
    and the city at location index2,
    swap their positions in the road_map,
    compute the new total distance, and
    return the tuple (new_road_map, new_total_distance).
    Allow the possibility that index1=index2, and handle this case correctly.'''

    new_road_map = road_map

    try:
        assert index1 != index2
        temp = road_map[index2]
        new_road_map[index2] = road_map[index1]
        new_road_map[index1] = temp
        new_tot_dist = compute_total_distance(new_road_map)
        return (new_road_map, new_tot_dist)

    except AssertionError:
        print("Cannot swab the same city, return the same road map")
        new_tot_dist = compute_total_distance(new_road_map)
        return (new_road_map, new_tot_dist)
                     
def find_best_cycle(road_map):
    '''Using a combination of swap_cities and swap_adjacent_cities,
    try 10000 swaps, and each time keep the best cycle found so far.
    After 10000 swaps, return the best cycle found so far.'''

    '''Shuffle the road map for n times to find the best starting map'''
    n = 100
    tot_dist = compute_total_distance(road_map)
    for index in range(0,n):
        new_road_map = road_map
        random.shuffle(new_road_map)
        new_tot_dist = compute_total_distance(new_road_map)
        if new_tot_dist < tot_dist:
            tot_dist = new_tot_dist
            best_road_map = new_road_map
    print("Best shuffle distance:\t", tot_dist)
    #nswaps = 10000
    ncities = len(road_map)
    
    for cur_index in range(0,ncities):
        for j in range(cur_index+1,ncities):
            (new_road_map, new_tot_dist) = swap_cities(best_road_map, cur_index, j)
            if new_tot_dist < tot_dist:
                tot_dist = new_tot_dist
                best_road_map = new_road_map
                print("CURRENT BEST DISTANCE:\t", tot_dist)
        print(new_tot_dist)
        

    return (best_road_map, tot_dist)          
              
def print_map(road_map):
    '''Prints, in an easily understandable format, the cities and their connections,
    along with the cost for each connection and the total cost.'''
    pass
              
def main():
    '''Reads in and prints out the city data,
    then creates the "best" cycle and prints it out.'''

    '''Read in city info'''
    road_map = read_cities('city-data.txt')

    '''Print city road map'''
    print_cities(road_map)

    '''Find the best road map'''
    (best_road_map, tot_dist) = find_best_cycle(road_map)
    print_cities(best_road_map)
    print(tot_dist)
    '''Print map'''
    
if __name__ == "__main__":
    main()              
