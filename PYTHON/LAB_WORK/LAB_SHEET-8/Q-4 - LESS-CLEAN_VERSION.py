def celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius
    """
    return (fahrenheit - 32) * 5 / 9

def fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit
    """
    return celsius * 9 / 5 + 32

def print_conversion_tables():
    """
    Print conversion tables for Celsius to Fahrenheit (0-100°C)
    and Fahrenheit to Celsius (32-212°F) in a tabular format
    """
    print("TEMPERATURE CONVERSION CHARTS")
    print("\n1. Celsius to Fahrenheit (0-100°C)")
    print("-" * 50)
    print(f"{'°C':^10}{'°F':^10}{'°C':^10}{'°F':^10}{'°C':^10}{'°F':^10}")
    print("-" * 50)
    
    # Print Celsius to Fahrenheit in 3 columns to minimize output lines
    for i in range(0, 34):  # Will cover 0-99°C in 34 rows (34*3 = 102)
        c1 = i
        c2 = i + 34
        c3 = i + 68
        
        # Prepare row data
        row = f"{c1:^10}{fahrenheit(c1):^10.1f}"
        
        # Add second column if within range
        if c2 <= 100:
            row += f"{c2:^10}{fahrenheit(c2):^10.1f}"
        else:
            row += " " * 20  # Fill with spaces if out of range
            
        # Add third column if within range
        if c3 <= 100:
            row += f"{c3:^10}{fahrenheit(c3):^10.1f}"
        
        print(row)
    
    print("\n2. Fahrenheit to Celsius (32-212°F)")
    print("-" * 50)
    print(f"{'°F':^10}{'°C':^10}{'°F':^10}{'°C':^10}{'°F':^10}{'°C':^10}")
    print("-" * 50)
    
    # Print Fahrenheit to Celsius in 3 columns to minimize output lines
    range_size = 212 - 32 + 1  # 181 values
    column_size = range_size // 3 + (1 if range_size % 3 > 0 else 0)  # ~61 rows
    
    for i in range(0, column_size):
        f1 = 32 + i
        f2 = 32 + i + column_size
        f3 = 32 + i + 2 * column_size
        
        # Prepare row data
        row = f"{f1:^10}{celsius(f1):^10.1f}"
        
        # Add second column if within range
        if f2 <= 212:
            row += f"{f2:^10}{celsius(f2):^10.1f}"
        else:
            row += " " * 20  # Fill with spaces if out of range
            
        # Add third column if within range
        if f3 <= 212:
            row += f"{f3:^10}{celsius(f3):^10.1f}"
        
        print(row)

if __name__ == "__main__":
    print_conversion_tables()