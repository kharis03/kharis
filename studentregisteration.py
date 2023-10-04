def student_registration():
    name = (input("Enter your name"))
    phone_number = (input("Enter your phone number"))
    email_address = (input("Enter your email_address"))
    age = int(input("Enter student age"))
    gender = (input("Enter your gender"))


    # student_file = {
    #     'name' :name,
    #     'gender': gender,
    #     'age' : age,
    #     'phone_number' : phone_number,
    #     'email_address':email_address
    # }

    return name, gender, age, phone_number, email_address


    # print(f'Student Name: {name}')
    # print(f'Student Gender: {gender}')
    # print(f'Student Age: {age}')
    # print(f'Student Email_Address: {email_address}')
    # print(f'Student Phone Number: {phone_number}')