def feedback(performance_vector:list)->list[str]: # Rules
    hours_worked = ''
    feedback_ = []
    if performance_vector[0]>=17: #Work hours
        feedback_.append(r"Well done employee, you have worked for more than 85% of the time")
    else:
        feedback_.append("Dear employee, you should work more!")
    if performance_vector[1]>=18: #Timely submissions
        feedback_.append("You have great discipline and complete the assingned work on time, we encourage you to continue to do so!")
    elif performance_vector[1] >=16: 
        feedback_.append("You have done timely submissions in most of the cases, well done!")
    else:
        feedback_.append("You really must, increase your work rate!")
    
    if performance_vector[2]<=6: # leaves
        feedback_.append("Wow!, you are working really hard")
    elif performance_vector[2]<=12:
        feedback_.append("You took some well deserved rest")
    elif performance_vector[2]<=20:
        feedback_.append("You don't shy away from talking holidays")
    else:
        feedback_.append("You have taken more holidays, than granted...action will be taken.")
    
    if performance_vector[3]>15: # Extra curricular activities
        feedback_.append("You are an all-rounder!")
    else:
        feedback_.append("Don't worry, we all have our own skills!")
    
    if performance_vector[4]>=5: #Error rate
        feedback_.append("You should work really carefully")
    else:
        feedback_.append("You make mistakes, but who doesn't")
    
    return  feedback_



def Employee_performance(performance_parameters:list[int]):

    work_rate = performance_parameters[0]*20//2100
    timely_submissions = performance_parameters[1]*20/35
    leaves = (10-performance_parameters[2])*2
    extra_curr  = performance_parameters[3]*2
    error_rate = performance_parameters[4]*2
    rating = work_rate+timely_submissions+leaves+extra_curr+(20-error_rate)
    performance_vector = [work_rate,timely_submissions,leaves,extra_curr,error_rate]
    print(performance_vector)
    feedback_= feedback(performance_vector)
    print("Based on the work that you have done following is your assessment :  ")
    for f in feedback_:
        print(f)
    print(f"Your performance rating is : {rating}")


Employee_performance([2050,32,4,8,2])


    

