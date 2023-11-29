def sheet(input_word=str, input_width=int):
    """create template with defined word and width"""
    
    signs: str = "=" * input_width
    center_word: int = (input_width - len(input_word)) // 2
    binary_signs: str = "01" * (len(input_word)  // 2)
    center_signs: str = "=" * center_word
    output: str =(f"     {signs}\n"
             f"     {center_signs}{binary_signs}{center_signs}\n"
             f"     {center_signs}{input_word}{center_signs}\n"
             f"     {center_signs}{binary_signs}{center_signs}\n"
             f"     {signs}"
             )
    print(output)
    print()
    