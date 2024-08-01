def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	                  #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

#TODO:
def z_score(x, mu, sigma):
    """

    z = ((x-mu)/sigma)

    x is the population array element
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """

    # 1. Review the starter code shown below. Your task is to complete the function at the bottom of the code so that it emulates the given formula.
    # 2. Review and refine your existing plan to allocate the work among your team members. For example, you might decide that one student will write the first draft of the algorithm, another will check it and write tests, and the third can implement the algorithm in Python. 
    # 3. Draw up your testing plans (your test cases and method for obtaining expected outputs). You may use Sheets like in Exercise 3, use other software instead, or do it by hand. 
    # 4. Write an algorithm to solve the problem and create either pseudocode or a flowchart to represent it.
    # 5. Complete the program so that the function produces the correct output using the given parameters. Do not change the function name or parameters, or any of the other functions in the code. It is OK if you want to add additional functions, such as functions that help automate your testing processes. You can do this work directly in the Snippet, or you can use another IDE of you want.
    # 6. Test your code and document the test results. Your documented tests (in your report) should include at least 2 cases that aren't already in the grader's test_z_score_function() in the starter code.
    # 7. Adjust the script as needed until the tests produce the expected output.
    
    # Participating group member names go in this comment
    # Kareem Mckenzie
    # Daniel Aguilar
    # Nghia Vo



    # Your code goes between this comment and the return

    return ((x-mu)/sigma)

def zScoreCalculator(populationArray: dict) -> float:
    popAvg = mean(populationArray)
    popStdDev = stdev(populationArray, popAvg)

    print(popAvg)

    for item in populationArray:
        print(z_score(item,popAvg,popStdDev))        

zScoreCalculator(population2)

'''
part 1: calculate population mean
    - calculated through mean function (pass it the entire array)
    - save this value to a variable
part 2: calculate population's std deviation
    - pass the population array and the mean from part 1
    - save this to a varaible
part 3: caclculate zScore of item
    - while looping through an array, pass the current element to the z_score function, the varaible saved in part 1, and the variable saved in part 2
    - print/return the result of each z score
'''