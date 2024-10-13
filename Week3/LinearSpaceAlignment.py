import sys
import math
from os import listdir
from os.path import isfile, join


def middle_edge(string1, string2, match_mismatch_mat, indel_penalty):
    n = len(string1)
    m = len(string2)
    prev_col_from_source_s = [0]
    for i in range(1, n+1):
        prev_col_from_source_s.append(prev_col_from_source_s[i-1]-indel_penalty)
    
    curr_col_from_source_s = list(prev_col_from_source_s)
    curr_col_from_source_backtrack = [None]*(n+1)
    j = 1
    middle_col = math.floor(m/2)
    while j <= middle_col+1:
        prev_col_from_source_s = list(curr_col_from_source_s)
        
        for i in range(0, n+1):
            match_score = match_mismatch_mat[string1[i-1]][string2[j-1]]
            max_val = prev_col_from_source_s[i]-indel_penalty  # right
            max_direction = "right"
            if i>0 and curr_col_from_source_s[i-1]-indel_penalty > max_val:
                max_val = curr_col_from_source_s[i-1]-indel_penalty  # down
                max_direction = "down"
            if i>0 and prev_col_from_source_s[i-1]+match_score > max_val:
                max_val = prev_col_from_source_s[i-1]+match_score  # diag
                max_direction = "diag"

            curr_col_from_source_s[i] = max_val
            curr_col_from_source_backtrack[i] = max_direction
        
        j += 1
    
    from_source_end_j = j-1
    
    prev_col_to_sink_s = [0]*(n+1)
    for i_inc in range(1, n+1):
        i = n - i_inc
        prev_col_to_sink_s[i] = prev_col_to_sink_s[i+1]-indel_penalty
    
    curr_col_to_sink_s = list(prev_col_to_sink_s)
    j = m-1
    while j >= middle_col:
        prev_col_to_sink_s = list(curr_col_to_sink_s)
        
        for i_inc in range(0, n+1):
            i = n - i_inc
            match_score = None
            if i<n:
                match_score = match_mismatch_mat[string1[i]][string2[j]]
            max_val = prev_col_to_sink_s[i]-indel_penalty  # left
            max_direction = "left"
            if i<n and curr_col_to_sink_s[i+1]-indel_penalty > max_val:
                max_val = curr_col_to_sink_s[i+1]-indel_penalty  # up
                max_direction = "up"
            if i<n and prev_col_to_sink_s[i+1]+match_score > max_val:
                max_val = prev_col_to_sink_s[i+1]+match_score  # diag
                max_direction = "diag"
            
            curr_col_to_sink_s[i] = max_val
        
        j -= 1
    
    to_sink_end_j = j + 1
    assert(from_source_end_j == to_sink_end_j + 1)
    
    max_middle_col_score = None
    max_middle_col_i = None
    for i in range(0, n+1):
        middle_col_score = prev_col_from_source_s[i] + curr_col_to_sink_s[i]
        middle_next_col_score = curr_col_from_source_s[i] + prev_col_to_sink_s[i]
        if max_middle_col_score is None or middle_col_score > max_middle_col_score:
            max_middle_col_score = middle_col_score
            max_middle_col_i = i
    
    middle_edge_end_i = None
    middle_edge_end_j = None
    options = []
    options.append(("right", curr_col_from_source_s[max_middle_col_i] + prev_col_to_sink_s[max_middle_col_i]))
    if max_middle_col_i < n:
        # down and diag are possible
        options.append(("down", prev_col_from_source_s[max_middle_col_i + 1] + curr_col_to_sink_s[max_middle_col_i + 1]))
        options.append(("diag", curr_col_from_source_s[max_middle_col_i + 1] + prev_col_to_sink_s[max_middle_col_i + 1]))
    
    best_option = list(sorted(options, key=lambda x: -x[1]))[0]
    if best_option[0] == "right":
        assert(curr_col_from_source_backtrack[max_middle_col_i] == "right")
        middle_edge_end_i = max_middle_col_i
        middle_edge_end_j = middle_col + 1
    elif best_option[0] == "diag":
        assert(curr_col_from_source_backtrack[max_middle_col_i + 1] == "diag")
        middle_edge_end_i = max_middle_col_i + 1
        middle_edge_end_j = middle_col + 1
    elif best_option[0] == "down":
        # we cannot assert backtrack since we saved backtracks only for curr_col, not prev_col where I store the middle column scores
        middle_edge_end_i = max_middle_col_i + 1
        middle_edge_end_j = middle_col

    edge_start_score = prev_col_from_source_s[max_middle_col_i] + curr_col_to_sink_s[max_middle_col_i]
    edge_end_score = best_option[1]
    
    return (max_middle_col_i, middle_col, edge_start_score), (middle_edge_end_i, middle_edge_end_j, edge_end_score)


# LinearSpaceAlignment(v, w, top, bottom, left, right)
#     if left = right
#         output path formed by bottom − top vertical edges
#     if top = bottom
#         output path formed by right − left horizontal edges
#     middle ← ⌊ (left + right)/2⌋
#     midEdge ← MiddleEdge(v, w, top, bottom, left, right)
#     midNode ← vertical coordinate of the initial node of midEdge 
#     LinearSpaceAlignment(v, w, top, midNode, left, middle)
#     output midEdge
#     if midEdge = "→" or midEdge = "↘"
#         middle ← middle + 1
#     if midEdge = "↓" or midEdge ="↘"
#         midNode ← midNode + 1 
#     LinearSpaceAlignment(v, w, midNode, bottom, middle, right)

def linear_space_alignment_seq(string1, string2, match_mismatch_mat, indel_penalty, string1_idx_from, string1_idx_to, string2_idx_from, string2_idx_to):
    if string2_idx_from == string2_idx_to:
        alignment_seq = ["V"]*(string1_idx_to-string1_idx_from)
        return alignment_seq, 0
    if string1_idx_from == string1_idx_to:
        alignment_seq = ["H"]*(string2_idx_to-string2_idx_from)
        return alignment_seq, 0
    
    assert (string1_idx_to > string1_idx_from)
    assert (string2_idx_to > string2_idx_from)
    middle = math.floor((string2_idx_from + string2_idx_to)/2)
    middle_edge_start, middle_edge_end = middle_edge(string1[string1_idx_from : string1_idx_to], string2[string2_idx_from : string2_idx_to], match_mismatch_mat, indel_penalty)
    middle_edge_start_i = middle_edge_start[0] + string1_idx_from
    middle_edge_start_j = middle_edge_start[1] + string2_idx_from
    middle_edge_start_score = middle_edge_start[2]
    middle_edge_end_i = middle_edge_end[0] + string1_idx_from
    middle_edge_end_j = middle_edge_end[1] + string2_idx_from
    middle_edge_end_score = middle_edge_end[2]
    assert (middle == middle_edge_start_j)
    alignment_seq_left_upper_square, _ = linear_space_alignment_seq(string1, string2, match_mismatch_mat, indel_penalty, string1_idx_from, middle_edge_start_i, string2_idx_from, middle_edge_start_j)
    alignment_seq_right_lower_square, _ = linear_space_alignment_seq(string1, string2, match_mismatch_mat, indel_penalty, middle_edge_end_i, string1_idx_to, middle_edge_end_j, string2_idx_to)
    middle_edge_alignment_symbol = None
    if middle_edge_end[0] - middle_edge_start[0] == 1 and middle_edge_end[1] - middle_edge_start[1] == 1:
        middle_edge_alignment_symbol = "D"
    elif middle_edge_end[0] - middle_edge_start[0] == 0 and middle_edge_end[1] - middle_edge_start[1] == 1:
        middle_edge_alignment_symbol = "H"
    elif middle_edge_end[0] - middle_edge_start[0] == 1 and middle_edge_end[1] - middle_edge_start[1] == 0:
        middle_edge_alignment_symbol = "V"
    assert (middle_edge_alignment_symbol is not None)
    return alignment_seq_left_upper_square + [middle_edge_alignment_symbol] + alignment_seq_right_lower_square, middle_edge_start_score


def linear_space_alignment(string1, string2, match_mismatch_mat, indel_penalty):
    n = len(string1)
    m = len(string2)
    alignment_seq, alignment_score = linear_space_alignment_seq(string1, string2, match_mismatch_mat, indel_penalty, 0, n, 0, m)
        
    alignment1 = []
    alignment2 = []
    i = 0
    j = 0
    for symbol in alignment_seq:
        if symbol == "V":
            alignment1.append(string1[i])
            alignment2.append("-")
            i += 1
        elif symbol == "H":
            alignment1.append("-")
            alignment2.append(string2[j])
            j += 1
        elif symbol == "D":
            alignment1.append(string1[i])
            alignment2.append(string2[j])
            i += 1
            j += 1
        else:
            raise ValueError(f"Unxpected symbol = {symbol}")
    
    return alignment_score, "".join(alignment1), "".join(alignment2)
    

if __name__ == "__main__":

    #with open("BLOSUM62.txt", mode='r') as f:
    #    file_contents = f.read()
    #
    #file_lines = file_contents.split("\n")
    #
    #letters = [v.strip() for v in file_lines[0].strip().split(" ") if len(v.strip()) > 0]
    #
    #match_mismatch_mat = dict()
    #for line in file_lines[1:]:
    #    line_splitted = [v.strip() for v in line.split(" ") if len(v.strip()) > 0]
    #    letter_from = line_splitted[0]
    #    match_mismatch_mat[letter_from] = dict()
    #    assert(len(letters) == len(line_splitted[1:]))
    #    for letter_to_idx, letter_to in enumerate(letters):
    #        match_mismatch_mat[letter_from][letter_to] = int(line_splitted[letter_to_idx+1])
    
    if sys.argv[1] == "--test":
        inputs_files = [f for f in listdir("inputs") if isfile(join("inputs", f))]
        outputs_files = [f for f in listdir("outputs") if isfile(join("outputs", f))]
        
        for input_file in inputs_files:
            output_file = input_file.replace("input", "output")
            
            with open("inputs/"+input_file, mode='r') as f:
                file_contents = f.read()
            
            file_lines = file_contents.split("\n")
            first_line_splitted = file_lines[0].split(" ")
            match_reward = int(first_line_splitted[0])
            mismatch_penalty = int(first_line_splitted[1])
            indel_penalty = int(first_line_splitted[2])
            string1 = file_lines[1].strip()
            string2 = file_lines[2].strip()
            
            letters = set(list(string1+string2))
            
            match_mismatch_mat = dict()
            for letter_from in letters:
                match_mismatch_mat[letter_from] = dict()
                for letter_to in letters:
                    match_score = 0
                    if letter_from == letter_to:
                        match_score = match_reward
                    else:
                        match_score = -mismatch_penalty
                    match_mismatch_mat[letter_from][letter_to] = match_score
            
            alignemnt_score, alignment1, alignment2 = linear_space_alignment(string1, string2, match_mismatch_mat, indel_penalty)
            output_str = "\n".join([str(alignemnt_score), alignment1, alignment2])
            
            with open("outputs/"+output_file, mode='r') as f:
                file_contents = f.read()
            
            expected_output = file_contents.strip()
            
            if expected_output == output_str:
                print(f"{input_file} test PASSED")
            else:
                print(f"{input_file} test FAILED  expecting:\n{expected_output}\nbut got:\n{output_str}")
                

    else:
        with open(sys.argv[1], mode='r') as f:
            file_contents = f.read()
        
        file_lines = file_contents.split("\n")
        first_line_splitted = file_lines[0].split(" ")
        match_reward = int(first_line_splitted[0])
        mismatch_penalty = int(first_line_splitted[1])
        indel_penalty = int(first_line_splitted[2])
        string1 = file_lines[1].strip()
        string2 = file_lines[2].strip()
        
        letters = set(list(string1+string2))
        
        match_mismatch_mat = dict()
        for letter_from in letters:
            match_mismatch_mat[letter_from] = dict()
            for letter_to in letters:
                match_score = 0
                if letter_from == letter_to:
                    match_score = match_reward
                else:
                    match_score = -mismatch_penalty
                match_mismatch_mat[letter_from][letter_to] = match_score
        
        alignemnt_score, alignment1, alignment2 = linear_space_alignment(string1, string2, match_mismatch_mat, indel_penalty)
        
        print(f"output:")
        print(f"{alignemnt_score}")
        print(f"{alignment1}")
        print(f"{alignment2}")