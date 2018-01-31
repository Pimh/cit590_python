from math import *
import random
import matplotlib.pyplot as plt

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

    city_stream.close()       
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
    ncities = len(road_map)
    for i in range(0,ncities):
        city1 = road_map[i]
        city2 = road_map[(i+1)%ncities]
        dist = compute_two_cities_distance(city1,city2)
        tot_dist = tot_dist + dist

    return tot_dist

def compute_two_cities_distance(city1,city2):
    '''Compute a distance between two cities'''
    lat1deg = float(city1[2])
    long1deg = float(city1[3])
    lat2deg = float(city2[2])
    long2deg = float(city2[3])
    dist = distance(lat1deg, long1deg, lat2deg, long2deg)

    return dist
        
def swap_adjacent_cities(road_map, index):
    '''Take the city at location index in the road_map,
    and the city at location index+1 (or at 0, if index refers to the last element in the list),
    swap their positions in the road_map,
    compute the new total distance, and
    return the tuple (new_road_map, new_total_distance).'''

    ncities = len(road_map)
    index1 = index
    index2 = (index+1) % ncities
    (new_road_map, new_tot_dist) = swap_cities(road_map, index1, index2)

    return (new_road_map, new_tot_dist)
    
def swap_cities(road_map, index1, index2):
    '''Take the city at location index in the road_map,
    and the city at location index2,
    swap their positions in the road_map,
    compute the new total distance, and
    return the tuple (new_road_map, new_total_distance).
    Allow the possibility that index1=index2, and handle this case correctly.'''

    new_road_map = road_map[:]

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

    '''Shuffle the road map to randomize a starting map.
    Path optimization heavily depends on its initial map'''
    n = 10
    tot_dist = compute_total_distance(road_map)
    best_road_map = road_map[:]
    best_tot_dist = tot_dist
    print("\nOptimizing the traveling path...\n")
    
    for index in range(0,n):
        new_road_map = road_map[:]
        random.shuffle(new_road_map)
        tot_dist = compute_total_distance(new_road_map)
        (best_hill_road_map, hill_tot_dist) = hill_climbing(new_road_map)
        
        if hill_tot_dist < best_tot_dist:
            best_tot_dist = hill_tot_dist
            best_road_map = best_hill_road_map
            print("Current best distance:\t", best_tot_dist, "\n")
            
    print("Finished hill climbing!")

    return best_road_map

def hill_climbing(road_map):
    '''Implement hill climbing method, iterate through rounds of cities swapping and
    update the road map if the total distance is shortened'''
    nswaps = 10000
    ncities = len(road_map)
    tot_dist = compute_total_distance(road_map)
    best_road_map = road_map[:]
    
    for cur_index in range(0,nswaps):
        '''swab cities'''
        (index1, index2) = select_indices(ncities)
        if cur_index % 10 == 0:
            (new_road_map, new_tot_dist) = swap_adjacent_cities(best_road_map, index1)
        else:
            (new_road_map, new_tot_dist) = swap_cities(best_road_map, index1, index2)

        if new_tot_dist < tot_dist:
            tot_dist = new_tot_dist
            best_road_map = new_road_map[:]
         
    return (best_road_map, tot_dist)          

def select_indices(ncities):
    '''select two city indices for swapping two cities'''
    index1 = floor(ncities*random.random())
    index2 = floor(ncities*random.random())   
    while (index1 == index2) :
        index2 = floor(ncities*random.random())
    return (int(index1),int(index2))        
              
def print_map(road_map):
    '''Prints, in an easily understandable format, the cities and their connections,
    along with the cost for each connection and the total cost.'''
    lat_list = []
    longt_list =[]    
    for index in range(0,len(road_map)):  
        lat = float(road_map[index][2])
        longt = float(road_map[index][3])
        lat_list.append(lat)
        longt_list.append(longt)
        plt.plot(lat,longt,'ro')
        plt.show()
    plt.plot(lat_list, longt_list)
    plt.show()
              
def main():
    '''Reads in and prints out the city data,
    then creates the "best" cycle and prints it out.'''

    '''Read in city info'''
    road_map = read_cities('city_data_cut.txt')

    '''Print city road map'''
    print_cities(road_map)

    '''Find the best road map'''
    best_road_map = find_best_cycle(road_map)
    
    '''Print map'''
    print_map(best_road_map)
    
if __name__ == "__main__":
    main() 
