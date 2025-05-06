def get_user_input():
    user_input = input("Enter temperatures separated by spaces: ")
    temp_strings = user_input.split()
    temperatures = [float(temp) for temp in temp_strings]
    return temperatures

def calc_average(temperatures):
    return sum(temperatures) / len(temperatures)

def find_min(temperatures):
    return min(temperatures)

def find_max(temperatures):
    return max(temperatures)

def calc_median(temperatures):
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    mid = n // 2

    if n % 2 == 0:
        # Even number of elements
        return (sorted_temps[mid - 1] + sorted_temps[mid]) / 2
    else:
        # Odd number of elements
        return sorted_temps[mid]

def main():
    temperatures = get_user_input()
    
    print("\nYou entered:", temperatures)
    print("Sorted temperatures:", sorted(temperatures))
    print("Average temperature:", round(calc_average(temperatures), 2))
    print("Minimum temperature:", find_min(temperatures))
    print("Maximum temperature:", find_max(temperatures))
    print("Median temperature:", calc_median(temperatures))

if __name__ == "__main__":
    main()