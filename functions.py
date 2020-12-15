"""A collection of function for doing my project."""

def get_info():
    """
    Gets info such as sex, age, height, and donation history.
    
    Returns
    -------
    info_dict : a dictionary 5 keys long
         The value is the user's input
    """
    
    #a semi filled dictionary
    info_dict = {'sex': '1' , 'age' : 2 , 'weight' : 3, 'height' : 4 , 'last donation' : 5}
    
   #greet user 
    print('Hello! Please enter some basic information to recieve what blood donation services you may be eligible for.')
    print()
    #getting user input (making sure they enter correctly)
    try:
        sex = input('Please specify your sex: male or female ')
    except ValueError:
        print('Please enter "male" or "female" in lowercase letters please :)')
        sex = input('Please specify your sex: male or female ')
    try:
        age = int(input('What is your age? '))
    except ValueError:
        print('Please enter a number ')
        age = int(input('What is your age? '))   
    try:
        weight = int(input('What is your weight? '))
    except ValueError:
        print('Please enter a number ')
        weight = int(input('What is your weight? '))
    try:
        height = float(input("What is your height? For example 5'5 = 5.5 "))
    except ValueError:
        print('Please enter a number in this format 0.0  ')
        height = float(input("What is your height? For example 5'5 = 5.5 "))
    try:
        last_donation = int(input('When was your last donation? Please enter # of days, if new donor enter 0. '))
    except ValueError:
        print('Please enter a number ')
        last_donation = int(input('When was your last donation? Please enter # of days, if new donor enter 0. '))
    
    #assigning user input to correct keys
    info_dict['sex'] = sex
    info_dict['age'] = age
    info_dict['weight'] = weight
    info_dict['height'] = height
    info_dict['last donation'] = last_donation 
    
    #returning the filled dictionary 
    return info_dict

def check_whole(info_dict):
    """
    Checks eligibility for Whole Blood donation. 
    
    Parameters 
    ----------
    info_dict: dictionary 
    
    Returns
    -------
    True : if all conditions for whole blood are met
    
    False : if any condition is not met
    """
    
    #assigning variables to input dictionary values
    age = info_dict['age'] 
    weight = info_dict['weight']
    last = info_dict['last donation']
    
    #conditions to meet 
    if age >= 16 and weight >= 110 and (last >= 56 or last == 0):
        return True
    else:
        return False


def check_powerMale(info_dict):
    """
    Checks eligibility for male Power Red donation.
    
    Parameters 
    ----------
    info_dict: dictionary
        dictionary from get_info()
    
    Returns
    -------
    True : if all conditions for male power red are met
    
    False : if any condition is not met
    """
    
    
    #assigning variables to input dictionary values
    sex = info_dict['sex']
    age = info_dict['age']
    weight = info_dict['weight']
    height = info_dict['height']
    last_donation = info_dict['last donation']
    
    #conditions to meet
    if sex == 'male' and age >= 17 and weight >= 130 and height >= 5.1 and (last_donation >= 112 or last_donation == 0):
        return True
    else:
        return False

def check_powerFemale(info_dict):
    """
    Checks eligibility for female Power Red donation.
    
    Parameters 
    ----------
    info_dict: dictionary
        dictionary from get_info()
    
    Returns
    -------
    True : if all conditions for female power red are met
    
    False : if any condition is not met
    """
    
    #assigning variables to input dictionary values
    sex = info_dict['sex']
    age = info_dict['age']
    weight = info_dict['weight']
    height = info_dict['height']
    last_donation = info_dict['last donation']
    
    #conditions to meet
    if sex == 'female' and age >= 19 and weight >= 150 and height >= 5.5 and (last_donation >= 112 or last_donation == 0):
        return True
    else:
        return False
    
def advise_user(info_dict):
    """
    Gives statement on blood services user is eligible for. 
    
    Parameters
    ----------
    info_dict : dictionary
        dictionary from get_info()
        
    Returns
    -------
    "You're (eligible or uneligible) to donate (blood donation or blood)!"
    """
    
    #using previous functions and assigning them a variable
    eligible_w = check_whole(info_dict)
    eligible_m = check_powerMale(info_dict)
    eligible_f = check_powerFemale(info_dict)
    
    #empty str 
    blood_donation = ''
    eligible = ''
    
    #conditions to meet
    
    #if user is eligible for both Whole and Power Red donations
    if eligible_w == True and eligible_m == True or eligible_f == True:
        blood_donation = 'Whole Blood and Power Red!'
        eligible = 'eligible'
    #if user is only eligible for one donation service
    elif eligible_w == True: 
        blood_donation = 'Whole Blood!'
        eligible = 'eligible'  
    elif eligible_m == True or eligible_f == True :
        blood_donation = 'Power Red!'
        eligible = 'eligible'
    else: 
        eligible = 'uneligible'
        blood_donation = 'blood :('
    
    return "You're " + eligible + ' to donate ' + blood_donation 
        

