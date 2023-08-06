import heapq

def highest_3_values(input_dict):
    top_3_items = heapq.nlargest(3, input_dict.items(), key=lambda item: item[1])

    result_dict = dict(top_3_items)

    return result_dict


sample_dict = {
    'a': 15,
    'b': 20,
    'c': 10,
    'd': 25,
    'e': 5,
    'anand':170
}

result_dict = highest_3_values(sample_dict)

print(result_dict)
