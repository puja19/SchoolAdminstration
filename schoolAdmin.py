#Project 1: Basic School adminstrative Program
import csv

def write_into_csv(info_list):
    #a file named student_info.csv is created with every new information getting appended
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact no.","E-mail ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    
    print("\nWelcome to School Administration Program\n")

    #Some initial conditions for internal loops
    condition=True
    student_num=1

    #Input student information
    while (condition):
        student_info=input("Enter the student information for student no. {} in following format: Name, Age, contact no., e-mail-ID: ".format(student_num))
        
        #Split
        student_info_list=student_info.split(' ')
        print("\nThe entered information is-\nName: {}\nAge: {}\nContact number is: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        t1=1 #temporory variable
        while t1==1:
            choice_check=input("Is entered information correct (yes/no): ")
            choice_check.lower()

            if choice_check=="yes":
                write_into_csv(student_info_list)
                t=1#temporory variable
                while (t):
                    condition_check=input("Do you want to enter another student information? (yes/no)")
                    condition_check.lower()
                    if condition_check=="no":
                        condition=False
                        t=0
                    elif condition_check=="yes":
                        condition=True
                        student_num=student_num+1
                        t=0
                    else:
                        #If user gives input other than yes/no
                        print("Wrong input please type again yes/no")
                        continue
                t1=0
            elif choice_check=="no":
                print("Please enter the values again\n")
                t1=0
            else:
                If user gives input other than yes/no
                print("wrong input please type again yes/no")
                continue
            
        
        

