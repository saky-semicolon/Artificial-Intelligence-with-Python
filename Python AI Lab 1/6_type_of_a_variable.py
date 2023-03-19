
#Everything is an object in python.
#when you use the type() function to print the type of the value stored in a variable to the console, it returns the class type of the object.

topic ="My-CV"

fullName = "S M ASIFUL ISLAM SAKY"

phoneNumber = 35894587

address =  ["Mymensingh", "Bangladesh"]
currentAddress = ["AIU", "Kedah, MY"]

personalDetails = {
    "firstName": "S M ASIFUL ISLAM",
    "lastName": "SAKY",
    "age": 19
}

languageProficiency = ("Bangla", "English", "Hindi")

experiences = {"HTML", "CSS", "JavaScript", "C"}


# As I have written about myself in this file, I will then print the types to the console by wrapping print() around some strings and the type() function.
#By doing so I will be able to find out my givevn data types.


print("The variable, Topic is of type:", type(topic))
print("The variable, Full name is of type:", type(fullName))
print("The variable, Phone Number is of type:", type(phoneNumber))
print("The variable, Current Address is of type:", type(currentAddress))
print("The variable, Personal Details is of type:", type(personalDetails))
print("The variable, Language proficiency is of type:", type(languageProficiency))
print("The variable, Experiences is of type:", type(experiences))