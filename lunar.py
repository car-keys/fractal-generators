import matplotlib.pyplot as plt

#lunar addition of intergers
def ladd(a, b):
    output = []
    if len(digits(a)) > len(digits(b)):
        larg = digits(a)[::-1]
        smol = digits(b)[::-1]
    else:
        larg = digits(b)[::-1]
        smol = digits(a)[::-1]
    for i in range(len(larg)):
        if i < len(smol):
            output.append(max(larg[i], smol[i]))
        else:
            output.append(larg[i])
    return int(''.join(str(e) for e in output[::-1]))

#lunar multiplication of intergers    
def lmul(a, b):
    digit_lists = []
    for _ in range(len(digits(b)) + len(digits(a)) - 1):
        digit_lists.append([])
    
    for i, bdigit in enumerate(digits(b)[::-1]):
        for m, adigit in enumerate(digits(a)[::-1]):
            digit_lists[i + m].append(min(bdigit, adigit))
    final_digits = []
    for lis in digit_lists:
        if lis != []:
            final_digits.append(max(lis))
    return int(''.join(str(e) for e in final_digits[::-1]))

#list of digits left to right, int only
def digits(num):
    return [int(s) for s in str(num)]
    
#interger that follows lunar rules for + and *
class lunar:
    def __init__(self, num):
        if not isinstance(num, int):
            raise TypeError('Value must be Interger')
        if num <= 0:
            raise ValueError('Value must be Positive')
        self.val = num
        
    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return f'lunar({self.val})'
        
    def __add__(self, other):
        return lunar(ladd(self.val, other.val))
        
    def __mul__(self, other):
        return lunar(lmul(self.val, other.val))
xs = list(range(100000))
plt.plot(xs, [lmul(x, x) for x in xs])
plt.legend(['lunar square'])
plt.show()
