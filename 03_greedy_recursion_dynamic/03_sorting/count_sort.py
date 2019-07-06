'''
Approach 1:
    Get histogram with frequency of each number.
    Build sorted list from histogram:
        Each index is the numeric value, each element is the 
        count of times that value should be present in the sorted list.
Runtime: O(n)
Space Complexity: O(n)
'''
def count_sort(L, range_size):
    histogram = get_histogram(L, range_size)
    return get_sorted_list(histogram)


def get_histogram(L, range_size):
    histogram = [0 for _ in range(range_size)]
    for num in L:
        histogram[num] += 1
    
    return histogram


def get_sorted_list(histogram):
    L = []
    for num,count in enumerate(histogram):
        for _ in range(count):
            L.append(num)

    return L


# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
if __name__ == '__main__':
    test = Test()

    nums = [1, 4, 1, 2, 7, 5, 2]
    range_size = 10 # 0 to 9
    result = [1, 1, 2, 2, 4, 5, 7]
    my_result = count_sort(nums, range_size)
    test.run(result == my_result)