import random as r
import os
from datetime import datetime

class calculator:
    ''' Taking user input and greet the user '''
    def __init__(self,user_name):
        self.user_name=user_name
        print("Hello %s , This is the program where you can practise the differnt kind of math operations."%user_name)
        

    ''' Function for Adding two numbers and returning result'''
    def add(self,num1,num2):
        result = num1 + num2
        return result

    ''' Function for Subtraction two numbers and returning result'''
    def subtraction(self,num1,num2):
        if num1 < num2:
            num1,num2 = num2,num1
        result = num1 - num2
        return result

    ''' Function for Multiply two numbers and returning result'''
    def multiply(self,num1,num2):
        result = num1 * num2
        return result
        
    ''' Function for Division two numbers and returning result'''
    def division(self,num1,num2):
        if num1 < num2:
            num1,num2 = num2,num1
        try:
            result = int(num1 / num2)
            return result
        except ZeroDivisionError:
            print("Can not divide the number with zero")
        
        
    ''' Function for Generating two random numbers single digit and double digit and returning result'''
    def generate_random_num(self,user_input):
        num1, num2 = -1,-1
        try:
            if user_input == 1:
                num1 = r.randint(0,9)
                num2 = r.randint(0,9)
            elif user_input == 2:
                num1 = r.randint(10,99)
                num2 = r.randint(10,99)
        except:
            print("You have not entered correct option")
        return num1, num2
        
    ''' Function for presenting menu and returning math operation value'''
    def menu(self):
        print(" These are the opearations which you can practise :")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Write a report")
        print("6. View a report")
        print("7. Exit")
        operation = input("Please select one of the option from above operations :")
        return operation
        
    ''' Function for positive and supportive reinforces returning related message'''
    def reinforces(self,operation,count,no_of_tries,no_of_correct_res,result):
        try:
            res = int(input("Please provide the answer for above operation :"))
        except ValueError:
            print("You have provided invalid option")
        positive = ["Excellent","Very Good","Well Done","Awesome","Correct","Good Job"]
        supportive = ["Try Again","OOPS","Not Quite","Look at it again","Sorry"]
        if res == int(result):
            flag=True
            no_of_correct_res+=1
            results = r.choice(positive)
        else:
            flag=False
            count +=1
            no_of_tries+=1
            results = r.choice(supportive)
        return results, count, no_of_tries,no_of_correct_res, flag
        
    ''' Function for performing math operations and returning result'''
    def operations(self,status,operation,no_of_tries,no_of_correct_res,file_name,choices,num1=None,num2=None,result=None):
        if operation == "1":
            result = self.add(num1,num2)
        elif operation == "2":
            result = self.subtraction(num1,num2)
        elif operation == "3":
            result = self.multiply(num1,num2)
        elif operation == "4":
            result = self.division(num1,num2)
        response = self.status_of_operations(operation,status,choices[operation],no_of_tries,no_of_correct_res,result)
        if operation == "5":
            self.write_a_report(response,file_name)
        elif operation == "6":
            self.view_a_report(response,file_name)
        if operation != '5' and operation != '6':
            return result,response
        return

    '''writing data records into the file'''
    def writing_into_fun(self,file_name,file,response,option=None):
        if option == None:
            opt = 'x'
        elif option == 2:
            opt = 'a'
        elif option == 1:
            opt='x'
            file_name+=1
            file='{}{}_data.txt'.format(user_name,file_name)
        else:
            print("Please enter the correct response")
        with open(file,opt) as fp:
            if opt == 'a':
                file_name-=1
                fp.write('\n')
            result={}
            f1="The opeartion performed is: "
            f2="The total number of incorrect tries are :"
            f3="The total number of correct responses are :"
            f4='The result of the operation is :'
            choices = {f1:"choice",f2:"no_of_tries",f3:"no_of_correct_res",f4:'result'}
            choice=list(choices)
            index=0
            flag=True
            for details in response:
                for detail in details:
                    result[choice[index]]=detail
                    index+=1
                index=0
                for res in result:
                    fp.write('{} {}{}'.format(datetime.now(),res,result[res]))
                    fp.write('\n')
                fp.write('='*50)
                fp.write('\n')
            file_name+=1
        print("Your operations has been recorded in report")
        

    '''This function is to write a report'''
    def write_a_report(self,response,file_name): 
        file='{}{}_data.txt'.format(user_name,file_name)
        if os.path.exists(file) == False:
            self.writing_into_fun(file_name,file,response,option=None)
        else:
            try:
                option = int(input("Your File is already present if you want to create a new file press 1 or if you want to append press 2:"))
            except ValueError:
                print("You have provided invalid option")
            self.writing_into_fun(file_name,file,response,option)
          

    '''This function is to view a report'''
    def view_a_report(self,response,file_name):
        if not os.path.exists("{}{}_data.txt".format(user_name,file_name)):
            print("You have not performed any operations yet")
            return
        with open('{}{}_data.txt'.format(user_name,file_name),'r') as fp:
            data=fp.read()
            print(data)
            

    ''' This function will track the status of operations and it's result '''
    def status_of_operations(self,operation,status,choice,no_of_tries,no_of_correct_res,result):
        if operation == '5' or operation == '6':
            return status
        res=[]
        res.append(choice)
        res.append(no_of_tries)
        res.append(no_of_correct_res)
        res.append(result)
        status.append(res)
        return status
        
    '''This is the main function where all the operations and functions has been called from here'''
    def main_fun(self,choices,count, no_of_tries, no_of_correct_res,file_name,flag,status):
        while True:
            operation = self.menu()        # Displaying menu
            if operation == "7":
                if not flag:
                    in_put=input("No records will be maintained please type 'yes' if you want to record your data otherwise 'no' : ")
                    if in_put == "yes":
                        response = self.status_of_operations(operation,status,choices[operation],no_of_tries,no_of_correct_res,result=None)
                        self.write_a_report(response,file_name)
                print("Thank You")
                break
            if operation == '5' or operation == '6':
                self.operations(status,operation,no_of_tries,no_of_correct_res,file_name,choices,num1=None,num2=None,result=None)
                input("Press the Enter key to continue: ")
            elif operation >= '1' and operation <= '7':
                '''To do valid operations below'''
                try:
                    user_input = int(input("If you want to do operations with single digit number press 1 or else press 2 for double digit numbers : "))
                    no_of_times = int(input("How many times do you want to do this operation :"))
                except:
                    print("You have entered incorrect option")
                ind = 0
                while ind < no_of_times:
                    num1, num2 = self.generate_random_num(user_input)
                    result,response = self.operations(status,operation,no_of_tries,no_of_correct_res,file_name,choices,num1,num2,result=0)
                    print("These are the two numbers are ready to perform operations %s %s"%(num1,num2))
                    results,count,no_of_tries,no_of_correct_res,flag = self.reinforces(operation,count,no_of_tries,no_of_correct_res,result)
                    print(results)
                    count=1
                    while not flag:
                        results,count,no_of_tries,no_of_correct_res,flag = self.reinforces(operation,count,no_of_tries,no_of_correct_res,result)
                        print(results)
                        if count > 1:
                            print("The result of the operation which you have performed is : %s"%result)
                            break
                    ind+=1
                input("Press the Enter key to continue: ")
            else:                                       # If wrong input from user if block will execute
                print("You have Entered incorrect option please select the valid option")


if __name__ == '__main__':
    user_name = input("Please Enter your name: ")
    cal_obj = calculator(user_name)
    choices = {'1':'Addition','2':'Subtraction','3':'Multiplication','4':'Division','5':'write_a_report','6':'view_a_report','7':'Exit'}
    count, no_of_tries, no_of_correct_res,file_name,flag = 1,0,0,1,False
    status=[]
    cal_obj.main_fun(choices,count, no_of_tries, no_of_correct_res,file_name,flag,status)
