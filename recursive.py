def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            print(f"展开子列表: {item}")
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, 2, [3, 4, [5, 6]], 7, [8]]))