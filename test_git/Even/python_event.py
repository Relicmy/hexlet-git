def sum_txt(path_txt:str)-> int:
    """input path to file with extension txt,
    output sum of numbers from file and their arithmetic mean"""
    sum_char = 0
    count_char = 0
    arifmetic_sum = 0
    if not isinstance(path_txt, str):
        raise TypeError("Invalid format path")
    if not path_txt.endswith(".txt"):
        raise TypeError("Invalid extension format")
    with open(path_txt, "r") as file:
        for char in file:
            if int(char):
                sum_char += int(char)
                count_char += 1
            else:
                continue
    if count_char == 0:
        raise ValueError("file is not in char") 
    arifmetic_sum = sum_char / count_char
    return sum_char, arifmetic_sum


if __name__ == "__main__":
    path_txt = "Even/numbers.txt"
    try:
        sum_char, arifmetic_sum = sum_txt(path_txt)
        print(f"sum char = {sum_char}", f"arithmetic mean = {arifmetic_sum}", sep="\n")
    except (TypeError, ValueError) as e:
        print(e)
        
    
        
                    
                    
    
            