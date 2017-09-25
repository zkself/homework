#-*- coding: utf-8 -*-
import random
from fractions import Fraction
import sys
import getopt

typeString = sys.getfilesystemencoding()


def ran_num():
    return random.randint(1, 100)


def ran_op():
    return random.randint(0, 3)


def judgeLevel(op1, op2):
    if op1 == 'x' and op2 == '+':
        return True
    if op1 == 'x' and op2 == '-':
        return True
    if op1 == '/' and op2 == '+':
        return True
    if op1 == '/' and op2 == '-':
        return True
    return False


def backExp(exp1):
    stack = []
    bck = []
    for i in range(len(exp1)):
        if type(exp1[i]) == int:
            bck.append(exp1[i])
        if type(exp1[i]) == str:
            if stack:
                if judgeLevel(exp1[i], stack[-1]):
                    stack.append(exp1[i])
                else:
                    bck.append(stack[-1])
                    stack.pop()
                    if stack and not judgeLevel(exp1[i], stack[-1]):
                        bck.append(stack[-1])
                        stack.pop()
                    stack.append(exp1[i])
            else:
                stack.append(exp1[i])
    if stack:
        stack = stack[::-1]
        bck.extend(stack)
    return bck


def calculate(op, num1, num2):
    if op == '+':
        res = Fraction(num1, 1) + Fraction(num2, 1)
    if op == '-':
        res = Fraction(num1, 1) - Fraction(num2, 1)
    if op == 'x':
        res = Fraction(num1, 1) * Fraction(num2, 1)
    if op == '/':
        res = Fraction(num1, 1) / Fraction(num2, 1)
    return res


global operators
operators = ('+', '-', 'x', '/')
n = 0
ratio = 0
try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:')
except getopt.GetoptError:
    print "please input arg"
for opt, value in opts:
    if opt == '-n':
        n = int(value)
for i in range(n):
    nums = (str(ran_num()), str(ran_num()), str(ran_num()), str(ran_num()))
    ops = (operators[ran_op()], operators[ran_op()], operators[ran_op()])
    exp = nums[0] + ops[0] + nums[1] + ops[1] + nums[2] + ops[2] + nums[3]
    exp1 = [int(nums[0]), ops[0], int(nums[1]), ops[1],
            int(nums[2]), ops[2], int(nums[3])]
    print exp + '=',
    ures = raw_input()
    bac = backExp(exp1)
    print bac

    new_stack = []
    for i in range(len(bac)):
        if type(bac[i]) == int:
            new_stack.append(bac[i])
        if type(bac[i]) == str:
            tmp = calculate(bac[i], new_stack[-2], new_stack[-1])
            new_stack.pop()
            new_stack.pop()
            new_stack.append(tmp)
            print new_stack
    # print new_stack[0]
    if(ures == str(new_stack[0])):
        print u'正确'.encode(typeString)
        ratio += 1
    else:
        print u'错误,正确答案='.encode(typeString) + str(new_stack[0])
print u'本次得分:' + str(100.0 / n * ratio)
