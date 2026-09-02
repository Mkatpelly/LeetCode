import itertools

class Solution:
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    
    def strongPasswordChecker(self, s: str) -> int:
        characters = set(s)
        
        needs_lowercase = not (characters & self.lowercase)
        needs_uppercase = not (characters & self.uppercase)
        needs_digit = not (characters & self.digit)
        num_required_type_replaces = int(needs_lowercase + needs_uppercase + needs_digit)
        
        num_required_inserts = max(0, 6 - len(s))
        num_required_deletes = max(0, len(s) - 20)
        
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(num_required_deletes):
            apply_best_delete()
        
        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )
        
        return (
            num_required_deletes
            + max(
                num_required_type_replaces,
                num_required_group_replaces,
                num_required_inserts,
            )
        )