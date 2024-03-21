class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for cpdomain in cpdomains:
            count,domain = cpdomain.split()
            count = int(count)
            domain = domain.split(".")
            for i in range(len(domain)):
                domains[".".join(domain[i:])] += count
                
        return[f"{count} {domain}" for domain,count in domains.items()]

        