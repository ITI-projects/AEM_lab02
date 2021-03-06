from datetime import datetime
import time
from preparedata import *
from draw import *
from greedy_algorithm import *
from steepest_algorithm import *


def generate_random_path(length, dataset_size):
    points = np.arange(dataset_size)
    np.random.shuffle(points)
    return points[:length], points[length:]


def calculate_distance(matrix, visited_vertexes):
    sum_of_distance = 0
    for i in range(len(visited_vertexes) - 1):
        sum_of_distance += matrix[visited_vertexes[i]][visited_vertexes[i + 1]]
    sum_of_distance += matrix[visited_vertexes[-1]][visited_vertexes[0]]
    return sum_of_distance


def test(matrix, alg, number_of_tests, path_length):
    all_paths = []
    all_distances = []
    all_times = []
    for i in range(number_of_tests):
        path_in, out = generate_random_path(path_length, len(matrix[0]))
        start = datetime.now()
        path_in = alg(path_in, out, matrix)
        stop = datetime.now()
        current_len = calculate_distance(matrix, path_in)
        all_distances.append(current_len)
        all_paths.append(path_in)
        all_times.append(stop - start)

    print("Distances")
    best, worst, mean = results(np.asarray(all_distances))
    print(all_distances[best])
    print(all_distances[worst])
    print(mean)
    print("Times")
    best_time, worst_time, mean_time = results(np.asarray(all_times))
    print(all_times[best_time])
    print(all_times[worst_time])
    print(mean_time)

    return all_paths[best]

def test_random(matrix, path_length):
    all_paths = []
    all_distances = []
    # Average time of the slowest local search algorithm
    timeout = 1.083495
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        path_in, out = generate_random_path(path_length, len(matrix[0]))
        current_len = calculate_distance(matrix, path_in)
        all_distances.append(current_len)
        all_paths.append(path_in)


    print("Distances")
    best, worst, mean = results(np.asarray(all_distances))
    print(all_distances[best])
    print(all_distances[worst])
    print(mean)

    return all_paths[best]


def results(all_distance):
    best = all_distance.argmin(axis=0)
    mean = all_distance.mean(axis=0)
    worst = all_distance.argmax(axis=0)
    return best, worst, mean


def main(path):
    loaded_data = PrepareData(path)
    coordinates = loaded_data.get_coords()
    drawing = DrawPlot(coordinates)
    matrix = loaded_data.calculate_distance_matrix()
    number_of_tests = 100
    path_length = 50
    print("Random")
    random = test_random(matrix, path_length)
    drawing.draw_results(random,"images/random" + path + ".png", 'random_' + path)
    print("Greedy ver")
    min_path = test(matrix, GreedyVerticlesAlgorithm, number_of_tests,path_length)
    drawing.draw_results(min_path, "images/greed_ver" + path + ".png", 'greed_ver_' + path)
    print("Greedy edge")
    min_path = test(matrix, GreedyEdgesAlgorithm, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/greed_edge" + path + ".png", 'greed_edge_' + path)
    print("Steepest ver")
    min_path = test(matrix, SteepestVerticlesAlgorithm, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/steepest_ver" + path + ".png", 'steepest_ver_' + path)
    print("Steepest edge")
    min_path = test(matrix, SteepestEdgesAlgorithm, number_of_tests, path_length)
    drawing.draw_results(min_path, "images/steepest_edge" + path + ".png", 'steepest_edge_' + path)



if __name__ == '__main__':
    print("kroA100")
    main(pathA)
    print("kroB100")
    main(pathB)
