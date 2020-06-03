def main():
    #write your code below this line
    points = int(input("Enter the amount of points you have [0-100]: "))
    if points < 0:
        print("Impossible!")
    elif points >= 0 and points <= 49:
        print("Grade: Failed")
    elif points >= 50 and points <= 59:
        print("Grade: 1")
    elif points >= 60 and points <= 69:
        print("Grade: 2")
    elif points >= 70 and points <= 79:
        print("Grade: 3")
    elif points >= 80 and points <= 89:
        print("Grade: 4")
    elif points >= 90 and points <= 100:
        print("Grade: 5")
    elif points > 100:
        print("Incredible!")

if __name__ == '__main__':
    main()
