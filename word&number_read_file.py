import random
class Employee:
    def __init__(self,name, hours,hourly_rate):
        self.name = name
        self.hours = hours
        self.hourly_rate = hourly_rate

    def pay(self):
        if self.hours > 40:
            return (self.hours - 40)* 1.5*self.hourly_rate + 40.0 * self.hourly_rate
        else:
            return self.hourly_rate * self.hours
    def __str__(self):
        return f"name:{self.name}\tPay:{self.pay()}"

def get_filename(prompt):
    return input(prompt)

def write_to_file(filename,emp):
    outfile = open(filename,"a")
    outfile.write(emp.name+","+str(emp.hours)+","+str(emp.hourly_rate)+'\n')
    outfile.close()

def read_from_file(filename,emp_list):
    with open(filename,'r') as infile:
        for line in infile:
            emp = line.strip().split(',')
            emp_list.append(Employee(emp[0],int(emp[1]),float(emp[2])))

def write_number_file(filename):
    with open(filename, "w") as file:
        for _ in range(20):
            file.write(str(random.randint(1, 50))+ " ")

def read_number_file(filename):
    try:
        with open(filename, "r") as file:
            num_str = file.read()
            num_lst = [float(num) for num in num_str.strip().split()]
            for num in num_lst:
                print(num, end = " ")
        
    except FileNotFoundError:
        print("The file does not exist.")

def main():
    emp1 = Employee("J Smith",50,20.5)
    emp2 = Employee("M Jones",35,30.0)
    emp3 = Employee("R Martin",40,25.0)
    employees =[emp1,emp2,emp3]
    filename1 = get_filename("Enter the word filename: ")
    filename2 = get_filename("Enter the number filename: ")
    for emp in employees:
        write_to_file(filename1,emp)
    new_employees = []
    read_from_file(filename1,new_employees)
    print("\nPrint final emp objects after reading from file")
    for emp in new_employees:
        print(emp)
    write_number_file(filename2)
    read_number_file(filename2)
    
if __name__ == "__main__":
    main()




    

    