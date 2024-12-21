import sys
import statistics

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_arguments():
    if len(sys.argv) < 2:
        print("No temperatures provided. Please provide temperature values as arguments.")
        return []
    
    fahrenheit_temperatures = []
    for temp in sys.argv[1:]:
        try:
            celsius_value = float(temp[:-1])
            fahrenheit_temperatures.append(celsius_to_fahrenheit(celsius_value))
        except ValueError:
            # Handle any invalid temperature format
            print(f"Invalid temperature format: {temp}")
            return []
    
    return fahrenheit_temperatures

def display(fahrenheit_temperatures):
    if not fahrenheit_temperatures:
        return
    
    max_temp = max(fahrenheit_temperatures)
    min_temp = min(fahrenheit_temperatures)
    mean_temp = statistics.mean(fahrenheit_temperatures)

    print(f"Maximum Temperature: {max_temp:.2f}F")
    print(f"Minimum Temperature: {min_temp:.2f}F")
    print(f"Mean Temperature: {mean_temp:.2f}F")

def main():
    fahrenheit_temperatures = process_arguments()
    display(fahrenheit_temperatures)

if __name__ == "__main__":
    main()
