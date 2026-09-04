import requests

# download a web page
response = requests.get('https://api.github.com')  
print(response.status_code)  # print the status code of the response
print("-" * 40)
print("Hello, World!\n")


string = """
am the one who is going to be the best AI engineer in the world.\n I will learn and practice every day to achieve my goal. I will not give up, no matter how hard it gets.\n I will keep pushing forward and never stop learning. I will be the best AI engineer in the world.
the ai engineer is the one who is going to change the world with his knowledge and skills.\n He will create amazing AI applications that will make people's lives easier and better.\n He will be a role model for future AI engineers and inspire them to achieve their dreams.
"""
print(string)
print("-" * 40)
print("\nByye, World!")

temprature = 25

if temprature > 30:
    print("It's a hot day.")
    
# list advanced
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1  

# dict addvanced
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}       

# access dictionary values
print(person["name"])  # Output: John

# tuple advanced
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1

# set advanced
my_set = {90, 90, 3, 4, 5}
print(my_set)  # Output: {90, 3, 4, 5}

