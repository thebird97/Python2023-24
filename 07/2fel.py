class Stack:
    class_level_num = 777

    def __init__(self):
        self._stack_list = []  # Made protected

    def push(self, val):
        self._stack_list.append(val)

    def pop(self):
        try:
            val = self._stack_list[-1]
            del self._stack_list[-1]
            return val
        except IndexError:
            print("Empty")

    def getList(self):
        return self._stack_list


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        super().push(val)  # Use super() for clarity

    def pop(self):
        val = super().pop()
        if val is not None:
            self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum


my_stack = AddingStack()

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

print(my_stack.get_sum())
