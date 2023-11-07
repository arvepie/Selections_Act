# define a function to determine the Chinese zodiac sign for a given year
def chinese_zodiac(year):
    # define a list of zodiac animal names
    zodiac_animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse",
                      "Sheep"]

    # the start year of the Chinese zodiac cycle
    start_year = 1924

    # dheck if the provided year is before the start of the Chinese zodiac cycle
    if year < start_year:
        print("The Chinese zodiac doesn't cover years before 1924.")
    else:
        # calculate the zodiac sign index for the given year
        year_index = (year - start_year) % 12

        # get the corresponding zodiac sign from the list
        zodiac_sign = zodiac_animals[year_index]

        # display the result to the user
        print(f"The Chinese zodiac sign for the year {year} is {zodiac_sign}.")


# main program execution
if __name__ == "__main__":
    try:
        # prompt the user to enter a year
        year = int(input("Enter a year: "))

        # call the chinese_zodiac function to find and display the zodiac sign
        chinese_zodiac(year)
    except ValueError:
        print("Please enter a valid year.")