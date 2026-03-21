def main():
    """
    Prompts the user to enter a paragraph.

    Parameters:
        None

    Variables:
        s (str): Contains the paragraph entered by the user.
        pat (str): Regular expression pattern used to identify sentences.
        m (list): List of sentences in the paragraph.

    Logic:
        1. Prompts the user to enter a paragraph.
        2. Uses regular expressions to identify sentences.
        3. Passes the list of sentences in the paragraph to the display_results function.

    Return:
        None
    """
    import re

    s = input("Enter a paragraph: ")

    #Enables the user to enter an input starting with a number or letter and accept it.
    pat = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

    display_results(m)


    """
    test with 7 sentences and make sure to include sentences starting with numbers.
    """

def display_results(m):
    """
    Shows each sentence in the paragraph and tells the user how many sentences there are.

    Parameters:
        m (list): List of sentences in the paragraph.

    Variables:
        None

    Logic:
        1. Loops through the sentences in the paragraph and prints them.
        2. Counts the number of sentences in the paragraph and prints the result.

    Return:
        None
    """

    #A loop that runs through each sentence and then prints the sentence.
    for i in m:
        print('->', i)

    print("Total number of sentences:", len(m))

if __name__ == "__main__":
    main()