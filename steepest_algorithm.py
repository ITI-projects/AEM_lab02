from delta import *
from swap import *
import numpy as np

def SteepestVerticlesAlgorithm(path, outside, matrix):
    combinations_to_swap_inside = generate_inside_swap_combinations(path)
    combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
    np.random.shuffle(combinations_to_swap_inside)
    np.random.shuffle(combinations_to_swap_outside)
    best_delta_inside = 1
    best_delta_outside = 1
    while (best_delta_inside > 0) or (best_delta_outside > 0):
        all_deltas = []
        for index in range(len(combinations_to_swap_outside)):
            vertices_to_swap = combinations_to_swap_outside[index]
            delta = calculate_delta_outside(path, outside, vertices_to_swap, matrix)
            all_deltas.append(delta)
        best_delta_outside = np.max(all_deltas)
        best_index_outside = combinations_to_swap_outside[np.argmax(all_deltas)]

        all_deltas.clear()
        for index in range(len(combinations_to_swap_inside)):
            vertices_to_swap = combinations_to_swap_inside[index]
            delta = calculate_delta_inside_vertices(path, vertices_to_swap, matrix)
            all_deltas.append(delta)
        best_delta_inside = np.max(all_deltas)
        best_index_inside = combinations_to_swap_inside[np.argmax(all_deltas)]

        if (best_delta_inside > 0) or (best_delta_outside > 0):
            if best_delta_outside > best_delta_inside:
                temp = path[best_index_outside[0]]
                path[best_index_outside[0]] = outside[best_index_outside[1]]
                outside[best_index_outside[1]] = temp
            else:
                path[best_index_inside[0]], path[best_index_inside[1]] = \
                    path[best_index_inside[1]], path[best_index_inside[0]]

        combinations_to_swap_inside = generate_inside_swap_combinations(path)
        combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
        np.random.shuffle(combinations_to_swap_inside)
        np.random.shuffle(combinations_to_swap_outside)

    return path


def SteepestEdgesAlgorithm(path, outside, matrix):
    combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
    combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)
    best_delta_inside = 1
    best_delta_outside = 1
    while (best_delta_inside > 0) or (best_delta_outside > 0):

        all_deltas = []
        for index in range(len(combinations_to_swap_outside)):
            vertices_to_swap = combinations_to_swap_outside[index]
            delta = calculate_delta_outside(path, outside, vertices_to_swap, matrix)
            all_deltas.append(delta)
        best_delta_outside = np.max(all_deltas)
        best_index_outside = combinations_to_swap_outside[np.argmax(all_deltas)]

        all_deltas.clear()
        for index in range(len(combinations_to_swap_inside)):
            vertices_to_swap = combinations_to_swap_inside[index]
            delta = calculate_delta_inside_edges(path, vertices_to_swap, matrix)
            all_deltas.append(delta)
        best_delta_inside = np.max(all_deltas)
        best_index_inside = combinations_to_swap_inside[np.argmax(all_deltas)]

        if (best_delta_inside > 0) or (best_delta_outside > 0):
            if best_delta_outside > best_delta_inside:
                temp = path[best_index_outside[0]]
                path[best_index_outside[0]] = outside[best_index_outside[1]]
                outside[best_index_outside[1]] = temp
            else:
                a = path[best_index_inside[0]:best_index_inside[1] + 1]
                a = np.flip(a)
                path[best_index_inside[0]:best_index_inside[1] + 1] = a
        combinations_to_swap_inside = generate_inside_swap_edge_combinations(path)
        combinations_to_swap_outside = generate_outside_swap_combinations(path, outside)

    return path
