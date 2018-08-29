
if __name__ == '__main__':
    """
    The input in the range(argument) is the the 1st numerical input that is
    given, and once this input is taken in, the range has its argument.
    Now the for iteration starts.
    In each iteration, the string(name of student) and
    the succeding numerical value that is fed as input is read.
    And a list of proper sorted data is prepared-->(a--list),
    as below:
    a = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    """
    a = [[input(), float(input())] for i in range(int(input()))]
    """
    The 2nd element in the sublists is the numerical data of the student.
    It is accessed in the below for list comprehension in the set().
    The set removes the duplicates and then sorted() is used to sort the numerical data.
    And we will have the 2nd lowest as x[1].
    s = {37.2,37.21,39,41}
    """
    s = sorted(set([x[1] for x in a]))
    """
    In the list comprehension below, the numerciacl data of student is checked of equality with       the 2nd lowest numercial score in the s[:] list and when there is a match, the element(student     string) corresponding to the the sublist i.e x[:] is returned and an iterator of student names     who have the 2nd lowest score is generated and it is then sorted of alphabetical order of         students in the new iterator that is formed, the student names are dynamically printed out         from the dynamic iterator
    """
    for name in sorted(x[0] for x in a if x[1] == s[1]):
        print(name)
        """
 Sample Input 0:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0:

Berry
Harry


        """
