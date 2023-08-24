class FlightTable:
    def __init__(self):
        self.data = [
            {'Match Location': 'Mumbai', 'Team 01': 'India', 'Team 02': 'Sri Lanka', 'Timing': 'DAY'},
            {'Match Location': 'Delhi', 'Team 01': 'England', 'Team 02': 'Australia', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Chennai', 'Team 01': 'India', 'Team 02': 'South Africa', 'Timing': 'DAY'},
            {'Match Location': 'Indore', 'Team 01': 'England', 'Team 02': 'Sri Lanka', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Mohali', 'Team 01': 'Australia', 'Team 02': 'South Africa', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Delhi', 'Team 01': 'India', 'Team 02': 'Australia', 'Timing': 'DAY'}
        ]

    def search(self, search_param, value):
        if search_param == 1:
            return [row for row in self.data if row['Team 01'] == value or row['Team 02'] == value]
        elif search_param == 2:
            return [row for row in self.data if row['Match Location'] == value]
        elif search_param == 3:
            return [row for row in self.data if row['Timing'] == value]
        else:
            return []

    def print_result(self, result):
        for row in result:
            print(f"Match Location: {row['Match Location']}, Team 01: {row['Team 01']}, Team 02: {row['Team 02']}, Timing: {row['Timing']}")

if __name__ == '__main__':
    ft = FlightTable()
    print("Choose the search parameter:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    search_param = int(input())
    print("Enter the value:")
    value = input()
    result = ft.search(search_param, value)
    ft.print_result(result)
    #hey 