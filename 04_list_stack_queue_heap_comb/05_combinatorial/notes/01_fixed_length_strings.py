def length_strings(A, n):
    if n == 0:
        return ['']
    else:
        previous = length_strings(A, n - 1)
        current = []
        for prefix in A:
            for posfix in previous:
                print(prefix, posfix)
                current.append(prefix + posfix)
        
        return current


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
    t = Test()

    A = ['0', '1', '2']
    n = 2
    output = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    t.run(length_strings(A, n) == output)