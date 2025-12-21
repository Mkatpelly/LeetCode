class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = defaultdict(int)

        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)

            parts = domain.split('.')
            # Build subdomains from right to left
            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                counts[sub] += count

        # Build the answer in the required "count domain" format
        return ["{} {}".format(cnt, dom) for dom, cnt in counts.items()]