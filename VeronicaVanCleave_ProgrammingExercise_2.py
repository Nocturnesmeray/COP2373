def spamscore():
    """
    Determines how likely a message is spam.

    Parameters:
        None

    Variables:
        spam_score (int): The spam score.
        message (str): The message being tested.

    Logic:
        1. Ask the user to input the message.
        2. Converts the message to lowercase and removes extra characters.
        3. Calls spamscorer() to calculate the spam score.
        4. Display the spam score and indicates how likely a message is spam.

    Return:
        message (str): The message being tested.
    """

    message = input('Please enter the message: ').lower().strip()

    spam_score = spamscorer(message)

    #tells the user how many spam words/phrases are in the message and how likely the message is spam.
    if spam_score <= 10:
        print(f"Your message's score is {spam_score}. Your message is not spam.")
    elif spam_score <= 20:
        print(f"Your message's score is {spam_score}. Your message might be spam.")
    else:
        print(f"Your message's score is {spam_score}. Your message is spam.")

    return message

def spamscorer(message):
    """
    Checks a message against a list of 30 words and phrases found in spam messages.

    Parameters:
        message (str): The message being tested.


    Variables:
        spam_score (int): The spam score.
        spam_words (list): A list of words and phrases found in spam messages.

    Logic:
        1. Create a list with 30 words and phrases found in spam messages.
        2. Create an accumulator for spam_score.
        3. Return the spam score.

    Return:
        spam_score (int): The spam score.
    """

    spam_score = 0

    spam_words = [
        "50% off", "debt", "free", "giveaway", "loan",
        "best deal", "click here", "get it now", "limited time", "no catch",
        "no strings attached", "pure profit", "risk-free", "special offer", "once in a lifetime",
        "urgent", "will not believe", "claim now", "contact us immediately", "expire",
        "don't delete", "final call", "don't hesitate", "offer expires", "data breach",
        "free trial", "action required", "last warning", "security update", "verify account", ]

    # checks for each spam word and phrase increasing by one when found
    for word in spam_words:
        if word.lower() in message:
            spam_score += 1

    return spam_score

if __name__ == "__main__":
    spamscore()