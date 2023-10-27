class Stack:
    class_level_num = 777
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        try:
            val = self.__stack_list[-1]
            del self.__stack_list[-1]
            return val
        except IndexError:
            print("Empty")

    def getList(self):
        return self.__stack_list

my_stack = Stack()
print(type(my_stack))
my_stack.push(2)
my_stack.push(3)
my_stack.push(55)
my_stack.push(1)

print(my_stack.getList())

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

print(my_stack.class_level_num)
print(my_stack.pop())