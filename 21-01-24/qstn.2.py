"""The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example
a=3
b=5
The result of the integer division .
The result of the float division is .
Print:

0
0.6
Input Format

The first line contains the first integer 3//5=0.
The second line contains the second integer 3/5=0.6.

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333 """
output: python3

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

output:pypy3

Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
den = int(input())

print(num//den)
print(num/den)
