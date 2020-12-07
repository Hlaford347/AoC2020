with open('day5.txt', 'r') as f:
    passes = f.read().splitlines()

# first 7 must be F or B; these specify one of the 128 rows (0-127); rows
# last 3 must be R or L; these specify one of the 8 seats (0-7); columns or seats
# Seat ID: Row * 8 + column


def getSeatId(row, column):
    return row * 8 + column


seat_Ids = []

rows = list(range(128))
columns = list(range(8))


def getRow(b_pass: str, row_list: list):
    global current_letter_index
    global rowNum

    if len(row_list) != 1:
        current_letter = b_pass[current_letter_index]
        if current_letter == 'F':
            row_list = row_list[:int(len(row_list)/2)]
        elif current_letter == 'B':
            row_list = row_list[int(len(row_list)/2):]

        current_letter_index += 1
        getRow(b_pass, row_list)
    else:
        rowNum = row_list[0]


def getColumn(b_pass: str, seat_list: list):
    global current_letter_index
    global seatNum

    if len(seat_list) == 1:
        seatNum = seat_list[0]
    else:
        current_letter = b_pass[current_letter_index]
        if current_letter == 'L':
            seat_list = seat_list[:int(len(seat_list)/2)]
        elif current_letter == 'R':
            seat_list = seat_list[int(len(seat_list)/2):]

        current_letter_index += 1
        getColumn(b_pass, seat_list)


for b_pass in passes:
    global current_letter_index
    global rowNum
    global seatNum
    current_letter_index = 0
    getRow(b_pass, rows.copy())
    getColumn(b_pass, columns.copy())
    seat_Ids.append(getSeatId(rowNum, seatNum))

seat_Ids = sorted(seat_Ids)

for n in range(seat_Ids[0], seat_Ids[-1]):
    if n not in seat_Ids:
        print(n)


# order seat ID lowest to highest/highest to lowest
# print(listID[-1])
