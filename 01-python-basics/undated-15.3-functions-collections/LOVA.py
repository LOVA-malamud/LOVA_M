

list_1 = ["apple","banana","kiwi","grape","kiwi"]

def get_len_word(list1: list) -> dict:
    len_word = {}
    for i in list1:
        len_word[i] = len(i)
    return len_word
print(get_len_word(list_1))

list_2 = {"Tom":80, "Anna":95, "John":70}
def get_max(dict1: dict) -> tuple:
    max_name = None
    max_grade = 0

    for name, grades in dict1.items():
        if grades > max_grade:
            max_name = name
            max_grade = grades
    return max_name, max_grade
print(f'{get_max(list_2)}')

list_3 = [4, 2, 1, 2, 3, -1, 3, 2, 2]
def get_count(list1: list) -> dict:
    count_dict = {}
    for num in list1:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict
print(get_count(list_3))

list_4 = {"apple":5, "banana":6, "kiwi":4}
def reverse_dict(dict1: dict) -> dict:
    new_dict = {}
    for k, v in dict1.items():
        new_dict[v] = k
    return new_dict
print(reverse_dict(list_4))

list_5 = [1,2,3,4,5,6]
def count_even_odd(nums: list) -> dict:
    count_even = 0
    count_odd = 0
    for num in nums:
        if num % 2 == 0:
            count_odd += 1

            count_odd += 1
    return (f'{count_even},evens and {count_odd}, odds')
print(count_even_odd(list_5))

cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}


def get_cities_sorted_by_population(cities: dict) -> list:
    temp_cities = []
    for city, city_info in cities.items():
        pop = city_info["population"]
        temp_cities.append((pop, city))
    temp_cities.sort()

    result = []
    for pop, name in temp_cities:
        result.append((name, pop))

    return result
print(get_cities_sorted_by_population(cities))

words_list = ["apple","banana","avocado","blueberry","apricot","corn"]


def group_by_letter(words):
    result = {}
    for word in words:
        first_letter = word[0]

        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]


print(group_by_letter(words_list))






