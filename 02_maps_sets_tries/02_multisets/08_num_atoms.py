'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms_frequency = self.parse_atoms(formula)
        return self.atom_count_format(atoms_frequency)

    
    def parse_atoms(self, formula):
        pass

    
    def atom_count_format(self, atoms_frequency):
        atoms_frequency = sorted(list(atoms_frequency.items()))

        pretty_formula = ""
        for element,count in atoms_frequency:
            pretty_formula += self.print_format(element, count)

        return pretty_formula

    
    def print_format(self, element, count):
        if count == 1:
            return element
        else:
            return f"{element}{count}"


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
    s = Solution()
    t = Test()

    # formula = "H2O"
    # output = "H2O"
    # actual_output = s.countOfAtoms(formula)
    # t.run(actual_output == output)


    # formula = "Mg(OH)2"
    # output = "H2MgO2"
    # actual_output = s.countOfAtoms(formula)
    # t.run(actual_output == output)


    # formula = "K4(ON(SO3)2)2"
    # output = "K4N2O14S4"
    # actual_output = s.countOfAtoms(formula)
    # t.run(actual_output == output)