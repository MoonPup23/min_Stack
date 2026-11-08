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


class Metro:
    def __init__(self) -> None:
        self.people: dict = {}
        self.metro_data: dict = {}

    def check_in(self, passenger_id: int, station: str, time: int) -> None:
        if passenger_id in self.people:
            raise ValueError(f"passenger: {passenger_id} in metro")
        self.people[passenger_id] = (station, time)

    def check_out(self, passenger_id, out_station, out_time):

        if passenger_id not in self.people:
            raise ValueError(f"passenger: {passenger_id} not exit")
        else:
            in_station, in_time = self.people[passenger_id]
            time_trip = out_time - in_time

        stat = (in_station, out_station)
        if stat not in self.metro_data:
            self.metro_data[stat] = [time_trip, 1]
        else:
            self.metro_data[stat][0] += time_trip
            self.metro_data[stat][1] += 1
            del self.people[passenger_id]

    def get_average_time(self, start_station: str, end_station: str) -> float:
        final_trip = (start_station, end_station)
        if final_trip not in self.metro_data:
            raise ValueError(f" trip: {final_trip} is not trip")
        else:
            return self.metro_data[final_trip][0] / self.metro_data[final_trip][1]


m = Metro()
m.check_in(1, "A", 10)
m.check_out(1, "B", 20)

m.check_in(2, "A", 15)
m.check_out(2, "B", 35)

m.check_in(3, "A", 40)
m.check_out(3, "B", 50)

#m.check_in(1, "A", 10)
# повторный вход

#m.check_out(67, "B", 52)
# выход без входа

#print(m.get_average_time("A", "b")
# проверка на маршрут корректный

print(m.get_average_time("A", "b"))
