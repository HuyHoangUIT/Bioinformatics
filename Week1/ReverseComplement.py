def ReverseComplement(Text):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join(complement[base] for base in reversed(Text))
def main():
    print(ReverseComplement("ATGGCC"))

main()