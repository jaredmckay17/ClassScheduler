import json
import sys


def read_in_json_file_to_graph_dict(json_file):
    graph_dict = dict()
    try:
        with open(json_file) as f:
            class_prerequisite_data = json.load(f)
    except ValueError as e:
        sys.exit("Error: Invalid JSON file. JSON file could not be read with following error message: " + str(e))
    for item in class_prerequisite_data:
        if item['name'] is None or item['prerequisites'] is None:
            sys.exit("Error: Invalid courses provided. Each object in the JSON file must have a course name and "
                     "a list of prerequisites")
        else:
            graph_dict[item['name']] = item['prerequisites']
    return graph_dict


def topological_sort(graph_dict):
    visited_nodes = set()
    reverse_post_order = list()
    for node in graph_dict.keys():
        if node not in visited_nodes:
            depth_first_search(graph_dict, node, visited_nodes, reverse_post_order)
    return reverse_post_order


def depth_first_search(graph_dict, start_node, visited_nodes, reverse_post_order):
    if start_node not in visited_nodes:
        visited_nodes.add(start_node)
        for node in graph_dict[start_node]:
            depth_first_search(graph_dict, node, visited_nodes, reverse_post_order)
        reverse_post_order.append(start_node)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Error: No arguments provided - please provide JSON file as argument to 'scheduler'")

    final_course_schedule = topological_sort(read_in_json_file_to_graph_dict(sys.argv[1]))

    for courses in final_course_schedule:
        print(courses)
