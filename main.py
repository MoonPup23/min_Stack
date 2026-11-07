class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.min_list: list[int] = []

    def push(self, new_data: int) -> None:
        self.data.append(new_data)
        if not self.min_list:
            self.min_list.append(new_data)
        else:
            last_data = self.min_list[-1]
            self.min_list.append(min(last_data, new_data))

    def pop(self) -> None:
        self.data.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.data[-1]

    def get_min(self) -> int:
        return self.min_list[-1]


stack = Stack()
stack.push(67)
stack.push(52)
stack.push(665)
print(stack.top())
print(stack.get_min())
stack.pop()
print(stack.top())
stack.push(42)
print(stack.get_min())
