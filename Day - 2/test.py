# def convert_add(lst):
#     sum = 0
#     for a in lst:
#         a = int(a)
#         sum = sum + a
#     return sum 

# l1 = ["1","2","3.5"]
# print(convert_add(l1))         

# More robust version 

# from typing import List, Union

# def convert_add(lst: List[Union[str, int, float]]) -> int:
#     total = 0
#     for item in lst:
#         try:
#             total += int(float(item))  # Handles "2.5", 2.0, etc.
#         except (ValueError, TypeError):
#             print(f"Skipping invalid item: {item}")
#             continue
#     return total

# # Example usage
# l1 = ["1", "2", "3", "bad", 4.5, None]
# print(convert_add(l1))  # Output: 10




# Extra question - 

def check_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            print(f"Duplicate found: {item}")
            return True
        seen.add(item)
    print("No duplicates found")
    return False

list1 = [1,2,3,4,5,5]
check_duplicate(list1)

list2 = ["a","b","c","d"]
check_duplicate(list2)