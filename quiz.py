def quiz_game():
 quiz=input("your welome to quiz game!!!! \nEnter go to start the Game:")
 if quiz=="go":
   print("Now the game is start \n\nRead the given instruction \n*total qestion 10.\n*Each correct question you have 1 mark.\n*Each wrong question you have negative mark(-0.5)")
   start=input("Enter 'Start' to join the game:")
 if start=="start":
    print("\nNow the question are given below...\n***Question***:")
    mark=0
    c_question=0
    w_question=0
    first_ques=input("1. Which of the following is not a major data analysis approaches?\n\nA. Data Mining\nB. Predictive Intelligence\nC. Business Intelligence\nD. Text Analytics \nSelect your option:")
    if first_ques=="b":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:Predictive Intelligence")
            
    second_ques=input("2. How many main statistical methodologies are used in data analysis?\n\nA. 2\nB. 3\nC. 4\nD. 5 \nSelect your option:")
    if second_ques=="a":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark is:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:2")
           
    third_ques=input("3. Data Analysis is defined by the statistician?\n\nA. William S.\nB. Hans Peter Luhn\nC. Gregory Piatetsky-Shapiro\nD. John Tukey \nSelect your option:")
    if third_ques=="d":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:John tukey")
            
    four_ques=input("4. Find the median of the given set of number 2,6,6,8,4,2,7,9?\n\nA.6\nB.8\nC.4\nD.5 \nSelect your option:")
    if four_ques=="a":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark is:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:6")
            
    fifth_ques=input("5. The following set of data is categorical or numerical data?\nred, red, blue, green, red, green, red, red, blue, blue \n\nA.Categorical data\nB.Numerical data \nSelect your option:")
    if fifth_ques=="a":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:Categorical data")
            
    sixth_ques=input("6. Text Analytics, also referred to as Text Mining?\n\nA. TRUE\nB. FALSE\nC. Can be true or false\nD. Can not say \nSelect your option:")
    if sixth_ques=="a":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark is:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:True")
            
    sevth_ques=input("7. ———- data that depends on data model and resides in a fixed field within a record.\n\nA. Un-Structured data\nB. Structured data\nC. Semi-Structured data\nD. Scattere \nSelect your option:")
    if sevth_ques=="b":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:Structural data")
            
    eight_ques=input("8. —————– is an example of human generated unstructured data.\n\nA. Satellite data\nB. Sensor data\nC. YouTube data\nD. Seismic imagery data \nSelect your option:")
    if eight_ques=="c":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark is:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:Youtube data")
            
    ninth_ques=input("9. ———- plot displays information as series of data points connected bystraight lines.\n\nA. Bar\nB. Line\nC. Scatter\nD. Histogram \nSelect your option:")
    if ninth_ques=="b":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:Line")
           
    tenth_ques=input("10. The ——– function creates a 2-D array with all values 1.\n\nA. numpy.Ones()\nB. numpy.zeros()\nC. numpy.eye()\nD. numpy.empty() \nSelect your option:")
    if tenth_ques=="a":
        print("your correct")
        mark=mark+1
        c_question=c_question+1
        print("your mark is:",mark)
    else:
        print("sorry!! Your answer is wrong")
        mark=mark-0.5
        w_question=w_question+1
        print("now your mark is:",mark)
        correct=input("Are you want to know the correct(yes/no):")
        if correct=="yes":
            print("Answer is:numpy.ones()")
            
        
 print("Your total mark is:",mark)
 print("Total Number of Correct Answer is ",c_question)
 print("Total Number of Wrong Answer is ",w_question)

 if mark==10:
   print("your grade is 'S'\nyour did wonderul!!!")
 elif mark>8.5 and mark<9.5:
   print(" your grade is 'A'\nyou did super!!!")
 elif mark>7.5 and mark<8:
    print("your grade is 'B'\nyou did good!!!")
 elif mark>6.5 and mark<7:
    print("your grade is 'C'\nyou did better")
 elif mark>4.5 and mark<6:
    print("your grade is 'D'\nyou did average")
 elif mark<=4:
    print("your grade is 'E'\nbetter luck next time!!!sorry ")
    
 print("\nGrade certeria:\n 10 is 'S'\n 9.5 to 8.5 is 'A'\n 8 to 7.5 is 'B'\n 7 to 6.5 is 'C'\n 6 to 4.5\n below 4.5 is 'E' ")    
 print("\n\n     -----Now your game is over!!-----")
        
        
        
        
        

    