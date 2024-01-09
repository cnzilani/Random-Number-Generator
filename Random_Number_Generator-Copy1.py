#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install requests')


# In[5]:


import requests

def fetch_true_random_number():#This function is responsible for fetching a true random number from the random.org API.
    #It sends a GET request to the API's endpoint, asking for one integer (num=1) in the range of 1 to 100,000 (min=1, max=100000).
    #The API response is received as plain text format (format=plain)
    #The function then extracts and returns the fetched random number as an integer
    try:
        response = requests.get("https://www.random.org/integers/?num=1&min=1&max=100000&col=1&base=10&format=plain&rnd=new")
        if response.status_code == 200:
            return int(response.text.strip())
        else:
            raise Exception("Failed to fetch true random number.")
    except Exception as e:
        raise Exception("An error occurred while fetching the true random number: " + str(e))

def calculate_randomness(numbers):
    #Calculates the randomness of a list of numbers based on the number of unique values observed in the list
    #It takes a list of integers (numbers) as input.
    #The function finds the maximum and minimum values in the list to determine the range of numbers present.
    #The randomness is then computed as the ratio of the number of unique numbers to the total range of numbers.
    max_number = max(numbers)
    min_number = min(numbers)
    range_of_numbers = max_number - min_number + 1
    unique_numbers = len(set(numbers))
    randomness = unique_numbers / range_of_numbers
    return randomness

if __name__ == "__main__":#checks if the script is being run as the main program.
    #Anything inside this block will only execute if the script is directly run, not if it's imported as a module.
    num_iterations = 100 #determines the number of random numbers to fetch and calculate randomness for. Here, we choose 100 iterations.
    random_numbers = [] #stores the true random numbers fetched from random.org

    for _ in range(num_iterations): #The loop fetches a true random number from the API in each iteration and appends it to the random_numbers list.
        random_number = fetch_true_random_number() #fetches a true random number by calling the fetch_true_random_number() function.
        random_numbers.append(random_number) #adds the fetched random number to the random_numbers list.

    overall_randomness = calculate_randomness(random_numbers)

    print("True random numbers:") # prints a message indicating that the following lines will display the true random numbers.
    print(random_numbers)
    print("Randomness over", num_iterations, "iterations:", overall_randomness)#This line prints the calculated randomness value over the specified number of iterations (100 in this case).


# In[ ]:


#the system may take sometime while generating the numbers

