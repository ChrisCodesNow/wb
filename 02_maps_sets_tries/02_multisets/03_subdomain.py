'''
Approach 1:
    Get domain visit count, visit domain, implicitly visit parent domains
Runtime: O(nw), for n count pair domain strings, each of size O(w)
Space Complexity: O(n)
'''
from collections import defaultdict
from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = self.get_visit_count(cpdomains)
        count_subdomains = self.visit_domain(visit_count)
        self.implicit_visit_parent_domains(visit_count, count_subdomains)
        count_domain_pairs = self.format_pair_domains(count_subdomains)

        return count_domain_pairs


    # Array strings -> Array [count, domain]
    # Runtime: O(nw), for n subdomains strings of length O(w)
    # Space: O(nw)
    def get_visit_count(self, cpdomains):
        visit_count = []
        for pair in cpdomains:
            count, domain = pair.split(" ")
            count = int(count)      # string to int
            visit_count.append([count, domain])

        return visit_count


    # Array [count, domain] -> Dict domain: count
    # Runtime: O(n)
    # Space: O(n)
    def visit_domain(self, visit_count):
        count_visits = defaultdict(int)
        for count, domain in visit_count:
            count_visits[domain] += count

        return count_visits


    # Array [count, domain]
    # Update Dict domain: count
    # Runtime: O(nw), for n words of size O(w)
    def implicit_visit_parent_domains(self, visit_count, count_subdomains):
        for count, domain in visit_count:
            domain_parts = domain.split(".")[1:]
            for i in range(len(domain_parts)):
                implied_domain = ".".join(domain_parts[i:])

                count_subdomains[implied_domain] += count

        
    # Dict domain: count -> Dict str(count domain)
    # Runtime: O(n)
    # Space: O(n)
    def format_pair_domains(self, count_subdomains):
        count_domain = []
        for domain, count in count_subdomains.items():
            count = str(count)
            count_domain.append(count + ' ' + domain)

        return count_domain
        

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


    cpdomains = ["9001 discuss.leetcode.com"]
    t.run(sorted(s.subdomainVisits(cpdomains)) == sorted(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]))
    
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    t.run(sorted(s.subdomainVisits(cpdomains)) == sorted(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]))