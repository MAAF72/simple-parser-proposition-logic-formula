class Stack:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def move(self, items):
        self.items.pop()
        self.items.extend(reversed(items))
            
    def show(self):
        return self.items
            
class Proposition:
    def __init__(self, text):
        self.text = text
        self.words = self.get_words()
        self.tokens = self.get_tokens()
        self.valid = self.check_valid()
        
    def get_words(self):
        words = []
        temp = ''
        for c in self.text:
            if c in [' ', '(', ')']:
                if temp != '':
                    words.append(temp)
                    temp = ''
                if c in ['(', ')']:
                    words.append(str(c))
            else:
                temp += str(c)

        if temp != '':
            words.append(temp)
            
        return words
        
    def get_tokens(self):
        tokens = []
        
        for word in self.words:
            state = 'q0'
            for c in word:
                if state == 'error':
                    break
                elif state == 'q0':
                    if c in ['p', 'q', 'r', 's']:
                        state = 'q1'
                    elif c == 'a':
                        state = 'q4'
                    elif c == 'i':
                        state = 'q7'
                    elif c == 'n':
                        state = 'q10'
                    elif c == 'o':
                        state = 'q13'
                    elif c == 't':
                        state = 'q15'
                    elif c == 'x':
                        state = 'q19'
                    elif c == '(':
                        state = 'q2'
                    elif c == ')':
                        state = 'q3'
                    else:
                        state == 'error'
                elif state == 'q4' and c == 'n':
                    state = 'q5'
                elif state == 'q5' and c == 'd':
                    state = 'q6'
                elif state == 'q7' and c == 'f':
                    state = 'q8'
                elif state == 'q8' and c == 'f':
                    state = 'q9'
                elif state == 'q10' and c == 'o':
                    state = 'q11'
                elif state == 'q11' and c == 't':
                    state = 'q12'
                elif state == 'q13' and c == 'r':
                    state = 'q14'
                elif state == 'q15' and c == 'h':
                    state = 'q16'
                elif state == 'q16' and c == 'e':
                    state = 'q17'
                elif state == 'q17' and c == 'n':
                    state = 'q18'
                elif state == 'q19' and c == 'o':
                    state = 'q20'
                elif state == 'q20' and c == 'r':
                    state = 'q21'
                else:
                    state = 'error'
 
            if state == 'q1':
                tokens.append(1)
            elif state == 'q12':
                tokens.append(2)
            elif state == 'q6':
                tokens.append(3)
            elif state == 'q14':
                tokens.append(4)
            elif state == 'q21':
                tokens.append(5)
            elif state == 'q8':
                tokens.append(6)
            elif state == 'q18':
                tokens.append(7)
            elif state == 'q9':
                tokens.append(8)
            elif state == 'q2':
                tokens.append(9)
            elif state == 'q3':
                tokens.append(10)
            else:
                tokens.append("error") #error
                break

        return tokens

    def check_valid(self):
        if self.tokens[-1] == "error":
            return False
            
        #print(self.words)
        #print(self.tokens)
        valid = True
        stack = Stack()
        state = 'i'
        stack.push('#')
        state = 'p'
        stack.push('S')
        state = 'q'
        i = 0
        symbol = self.tokens[i]
        while stack.top() != '#' and valid:
            if stack.top() == 'S': #Terminal Variable
                if symbol == 1:
                    stack.move([1, 'A'])
                elif symbol == 6:
                    stack.move([6, 'S', 7, 'S'])
                elif symbol == 2:
                    stack.move([2, 'S'])
                elif symbol == 9:
                    stack.move([9, 'S', 10, 'A'])
                else:
                    valid = False
            elif stack.top() == 'A': #Terminal Variable
                if symbol == 3:
                    stack.move([3, 'S'])
                elif symbol == 4:
                    stack.move([4, 'S'])
                elif symbol == 5:
                    stack.move([5, 'S'])
                elif symbol == 8:
                    stack.move([8, 'S'])
                elif symbol in [7, 10, '$']: #Empty
                    stack.pop()
                else:
                    valid = False
            elif stack.top() in range(1, 11): #Non Terminal Variable
                if symbol == stack.top():
                    stack.pop()
                    i += 1
                    if i == len(self.tokens):
                        symbol = '$'
                    else:
                        symbol = self.tokens[i]
                else:
                    valid = False

        stack.pop()
        state = 'f'

        return valid

test = Proposition(input())
print(test.tokens)
print(test.valid)