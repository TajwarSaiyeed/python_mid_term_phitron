class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, id, seats):
        if id not in self.__seats:
            print(f"Show ID : {id} does not exist.")
            return

        for seat in seats:
            row, col = seat
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                print(f"Seat ({row}, {col}) is invalid!!!")
                continue
            elif self.__seats[id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked!!")
                continue
            else:
                self.__seats[id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        print("----------------Show List------------------------")
        for show in self.__show_list:
            print(f"[Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}]")
        print("-------------------------------------------------")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"Show ID : {id} does not exist.")
            return

        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[id][row][col] == 0:
                    print(0, end=" ")
                else:
                    print(1, end=" ")
            print()



hall1 = Hall(5, 5, "Hall 1")
hall1.entry_show(111, "Avengers", "12:00")
hall1.entry_show(222, "Spiderman", "3:00")
hall1.entry_show(333, "Ironman", "6:00")


while True:
    print("Star Cinema")
    print("1. View Show List")
    print("2. Book Seats")
    print("3. View Available Seats")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        hall1.view_show_list()
    elif choice == 2:
        show_id = int(input("Enter show ID: "))
        how_many = int(input("How many seats do you want to book? "))
        seats = []
        for i in range(how_many):
            row, col = map(int, input("Enter row and col: ").split())
            seats.append((row, col))
        hall1.book_seats(show_id, seats)
        print("Updated Seats:")
        hall1.view_available_seats(show_id)
    elif choice == 3:
        show_id = int(input("Enter show ID: "))
        hall1.view_available_seats(show_id)
    elif choice == 4:
        break      
