def main():
    """
    Asks the user to enter a phone number social, security number, and zip code.

    Parameters:
        None

    Variables:
        phone_number (list): A list of phone numbers.
        social_security (list): A list of social security numbers.
        zip_code (list): A list of zip codes.
        phone (str): The phone number entered by the user.
        social (str): The social security number entered by the user.
        zip (str): The zip code entered by the user.

    Logic:
        1. Asks the user for an input for a phone number, social security number, and a zip code.
        2. Stores the inputs into the correct list.
        3. Calls the validation function to validate the stored inputs.

    Return:
        None
    """

    phone_number = []
    social_security = []
    zip_code = []

    while True:
        phone = input("Enter your phone number or stop to end: ")
        if phone == "stop":
            break

        social = input("Enter your social security number: ")
        zip = input("Enter your zip code: ")

        #Stores the inputs into the correct list.
        phone_number.append(phone)
        social_security.append(social)
        zip_code.append(zip)

    #Calls the validation function
    validation(phone_number, social_security, zip_code)


def validation(phone_number, social_security, zip_code):
    """
    Checks to see if the phone number, social security number, and zip code is valid.

    Parameters:
        phone_number (list): A list of phone numbers.
        social_security (list): A list of social security numbers.
        zip_code (list): A list of zip codes.

    Variables:
        phone_match (str): Regular expression pattern for phone number validation.
        social_match (str): Regular expression pattern for social security number validation.
        zip_code_match (str): Regular expression pattern for zip code validation.

    Logic:
        1. Use a regular expression to validate the phone number, social security number, and zip code.
        2. Loops through all of the inputs.
        3. Prints if the phone number, social security number, and zip code is valid.

    Return:
        None
    """
    import re

    #Regular expressions that defines what makes the input valid.
    phone_match = r'^\d{3}-\d{3}-\d{4}$'
    social_match = r'^\d{3}-\d{2}-\d{4}$'
    zip_code_match = r'^\d{5}(-\d{4})?$'

    #Loops through all the stored inputs and determines if they are valid..
    for i in range(len(phone_number)):

        if re.match(phone_match, phone_number[i]):
            print(phone_number[i], "is a valid phone number.")
        else:
            print(phone_number[i], "is not a valid phone number.")

        if re.match(social_match, social_security[i]):
            print(social_security[i], "is a valid social security number.")
        else:
            print(social_security[i], "is not a valid social security number.")

        if re.match(zip_code_match , zip_code[i]):
            print(zip_code[i], "is a valid zip code.")
        else:
            print(zip_code[i], "is not a valid zip code.")

    return

if __name__ == "__main__":
    main()
