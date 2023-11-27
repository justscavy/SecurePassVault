import random
"""
def sheet(input_word="Password-manager", input_width=28):
    signs = "=" * input_width
    center_word = (input_width - len(input_word)) // 2
    center_signs = "=" * center_word
    output = f"          {signs}\n          {signs}\n          {center_signs}{input_word}{center_signs}\n          {signs}\n          {signs}"
    print(output)
    print()
    print()
"""



def sheet(input_word="PASSWORD-MANAGER", input_width=28):
    signs = "=" * input_width
    center_word = (input_width - len(input_word)) // 2
    binary_signs = "01" * (len(input_word)  // 2)
    center_signs = "=" * center_word
    output =(f"          {signs}\n"
             f"          {center_signs}{binary_signs}{center_signs}\n"
             f"          {center_signs}{input_word}{center_signs}\n"
             f"          {center_signs}{binary_signs}{center_signs}\n"
             f"          {signs}"
             )
    print(output)
    print()
    print()




