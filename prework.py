# Question 1: Write a function to print "Hello_USERNAME!"
def hello_name(user_name):
    print("Hello_" + user_name.upper() +"!")

hello_name("Terrell")

# Question 2: Print the first odd numbers between 1 and 100 

def first_odds():
    for i in range(1,101):
        if i % 2 == 1:
            print(i)

# first_odds()

def first_odds2():
    print(list(range(1,101, 2)))

first_odds2()

# Question 3: Write the function that returns the max number in a given list

def max_num_in_list(a_list):
    max = a_list[0]

    for number in a_list:
        if max < number:
            max = number
    return max

print(max_num_in_list([2,3,5,8,12]))

def max_num(a_list):
    return max(a_list)

print(max_num([2,5,7,20,6]))

# Question 4: Write a function to return (True) if the given year is a leap year or (False) if it isn't.

def is_leap_year(a_year):
    if a_year % 100 != 0 and a_year % 400 == 0 or a_year % 4 == 0:
        return True
    else:
        return False

# print(is_leap_year(2022))
# print(is_leap_year(2020))

# Question 5: Write a function that checks if all numbers in th list are consecutive.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

print(is_consecutive([3,4,5,6,7,8]))
print(is_consecutive([3,4,5,4,6,7,8]))

def is_consecutive_again(a_list):
    i = 0
    status = True

    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1] or a_list[i] -1 == a_list[i+1]:
            i += 1
        else:
            status = False
            break
    
    # For loop version
    # for j in range(len(a_list)-1):


    return status

print("consecutive 2: ", is_consecutive_again([5,4,3,2,1]))
