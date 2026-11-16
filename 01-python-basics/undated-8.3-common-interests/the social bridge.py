def find_common(person_a, person_b) -> tuple:
    set_a = set(person_a)
    set_b = set(person_b)

    common_interests = set_a.intersection(set_b)
    sorted_list = sorted(list(common_interests))
    count = len(sorted_list)

    return (sorted_list, count)

person_a = ["coding", "hiking", "cooking", "surfing"]
person_b = ["hiking", "gaming", "coding"]

result = find_common(person_a, person_b)
print(result)
