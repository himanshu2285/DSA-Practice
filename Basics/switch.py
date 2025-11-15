'''Given the integer day denoting the day number, print on the screen which day of the week it is.
Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

Ensure only the 1st letter of the answer is capitalised.'''

class Solution:
    def dayOfTheWeek(self, day):
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case _:
                return "Invalid"

obj = Solution()
day = int(input("Enter the day number (1-7): "))
result = obj.dayOfTheWeek(day)
print(result)