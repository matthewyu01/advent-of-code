def find_seat(code):
    #FBFBBFFRLR #binary
    row = 0
    column = 0
    for i,char in enumerate(code):
        if char == 'B': #first 7 chars
            row += 2**(6-i) #64 32 16 8 4 2 1    
        elif char == 'R': #8-10 chars - (i-7)
            column += 2**(2-(i-7)) # 4 2 1
    seat = 8 * row + column
    return seat 


def main():
    with open('input.txt','r') as f:
        lines = f.readlines()
    max_seat = 0
    seats = []
    for seat_code in lines:
        #part 1
        seat = find_seat(seat_code)
        if seat > max_seat:
            max_seat = seat

        seats.append(seat) #part 2
    
    print(max_seat) # part 1

    #part 2 -
    seats.sort() # sort seats to find missing seat in middle of plane
    for i in range(1, len(seats)):
        if seats[i] - 1 != seats[i-1]:
            print(seats[i] - 1) #your seat
            break


if __name__ == "__main__":
    main()