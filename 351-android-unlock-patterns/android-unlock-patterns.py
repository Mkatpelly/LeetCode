class Solution:
    def __init__(self) : 
        self.cant_skip = [[0 for __ in range(10)] for _ in range(10)]
        # cannot go 1 to 3 or 3 to 1 without 2 
        self.cant_skip[1][3] = self.cant_skip[3][1] = 2
        # similar for below 
        self.cant_skip[1][7] = self.cant_skip[7][1] = 4 
        self.cant_skip[3][9] = self.cant_skip[9][3] = 6
        self.cant_skip[7][9] = self.cant_skip[9][7] = 8 
        # deal with the ridiculousness that is 5 being able to reach everywhere 
        # cross pattern 
        self.cant_skip[2][8] = self.cant_skip[4][6] = self.cant_skip[8][2] = self.cant_skip[6][4] = 5
        # x pattern 
        self.cant_skip[1][9] = self.cant_skip[9][1] = self.cant_skip[7][3] = self.cant_skip[3][7] = 5
        self.visited = [0 for _ in range(10)]
        # 1 represents the pieces at diagonal corners of 5 
        # 2 represents the pieces at horizontal and vertical corners of 5 
        # and 5 represents itself. 
        # we can speed up simulation by taking additive results of these sectors 
        self.cell_types = [1, 2, 5]

    def valid_selection(self, candidate, key_pad_number) : 
        # if we have a 0, we can visit 
        can_visit = not self.visited[candidate]
        # unless it is the same thing 
        same = candidate == key_pad_number 
        # weather or not there is a center value we cannot skip 
        can_skip_center = self.cant_skip[key_pad_number][candidate]
        # we can only skip the center value if there is no center value or we already visited it 
        can_be_skipped = not can_skip_center or self.visited[can_skip_center]
        # it's only valid if we can visit it, we do have a value we can skip or we do not have a value to worry about skipping and they are not the same
        return can_visit and can_be_skipped and not same
    
    def backtracking(self, key_pad_number, number_of_key_presses, key_presses_needed) : 
        # succesful combination 
        if number_of_key_presses == key_presses_needed : 
            return 1 
        # recursively count 
        number_of_combinations = 0
        # press this number 
        self.visited[key_pad_number] = 1 
        # candidates 
        for candidate in range(1, 10) : 
            # get candidates that are valid 
            if self.valid_selection(candidate, key_pad_number) : 
                # and increment by their result if we go forward 
                number_of_combinations += self.backtracking(candidate, number_of_key_presses + 1, key_presses_needed)
        # pretend you didn't press this number 
        self.visited[key_pad_number] = 0
        # return combinations 
        return number_of_combinations 

    def numberOfPatterns(self, m: int, n: int) -> int:
        # number of patterns starts at 0 
        number_of_patterns = 0 
        # loop over range of key presses needed 
        for key_presses_needed in range(m, n+1) : 
            # get sum of cell types all told 
            cumulative_sum = 0
            # for either the center spot, or for either of the two types of edges 
            for cell in self.cell_types : 
                # get the backtracking result 
                backtracking_result = self.backtracking(cell, 1, key_presses_needed)
                if cell != 5 : 
                    # if not the center spot, you actually have 4 of these combinations you can combine 
                    backtracking_result = backtracking_result + backtracking_result + backtracking_result + backtracking_result
                # update the cumulative sum 
                cumulative_sum += backtracking_result
            # update the number of patterns 
            number_of_patterns += cumulative_sum 
        # return when done 
        return number_of_patterns