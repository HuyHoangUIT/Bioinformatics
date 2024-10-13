def build_suffix_array(text):
    """
    Construct the full suffix array of the input text.
    """
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()  # Sort lexicographically by suffix
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def partial_suffix_array(text, k):
    """
    Construct a partial suffix array for the given text with entries at indices that are multiples of k.
    """
    # Build the full suffix array
    suffix_array = build_suffix_array(text)
    
    # Collect only the entries where the index in the suffix array is a multiple of k
    partial_suffix_array = [(i, suffix_array[i]) for i in range(len(suffix_array)) if suffix_array[i] % k == 0]
    
    return partial_suffix_array

# Read input from input.txt
with open("input.txt", "r") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())

# Get the result of the partial suffix array
result = partial_suffix_array(text, k)

# Write output to output.txt
with open("output.txt", "w") as file:
    for i, pos in result:
        file.write(f"{i} {pos}\n")
