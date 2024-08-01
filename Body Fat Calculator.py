def calculate_body_fat(gender, waist, neck, height, measurement_system):
    if measurement_system == "metric":                                          
        if gender.lower() == 'male':
            body_fat_percentage = 86.010 * (waist - neck) / height - 70.041 * (height / 100) + 36.76
        else:
            body_fat_percentage = 163.205 * (waist + neck) / height - 97.684 * (height / 100) - 78.387
    else:
        waist = waist * 2.54  
        neck = neck * 2.54    
        height = height * 2.54
        if gender.lower() == 'male':
            body_fat_percentage = 86.010 * (waist - neck) / height - 70.041 * (height / 100) + 36.76
        else:
            body_fat_percentage = 163.205 * (waist + neck) / height - 97.684 * (height / 100) - 78.387
            
    return body_fat_percentage

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Enhanced Body Fat Calculator!")
    
    measurement_system = input("Would you like to use metric (cm) or imperial (in) measurements? (type 'metric' or 'imperial'): ").strip().lower()
    
    if measurement_system not in ["metric", "imperial"]:
        print("Invalid measurement system chosen. Exiting program.")
        return
    
    gender = input("Enter your gender (male/female): ").strip().lower()
    while gender not in ["male", "female"]:
        print("Invalid gender. Please enter 'male' or 'female'.")
        gender = input("Enter your gender (male/female): ").strip().lower()
    
    waist = get_float_input("Enter your waist measurement: ")
    neck = get_float_input("Enter your neck measurement: ")
    height = get_float_input("Enter your height measurement: ")
    
    body_fat = calculate_body_fat(gender, waist, neck, height, measurement_system)
    
    print(f"Your estimated body fat percentage is: {body_fat:.2f}%")
    
    with open("body_fat_results.txt", "a") as file:
        file.write(f"Gender: {gender}, Waist: {waist}, Neck: {neck}, Height: {height}, Body Fat Percentage: {body_fat:.2f}%\n")
    
    print("Your results have been saved to 'body_fat_results.txt'.")

if __name__ == "__main__":
    main()