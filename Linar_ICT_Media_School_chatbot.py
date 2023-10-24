#importing the 'datetime' and 'time' module 
import datetime
import time
#Printing out the current time and date
current_date=datetime.datetime.now()
print("Date: ",current_date.strftime("%Y-%m-%d"))
print("Time: ",datetime.datetime.now().strftime("%H:%M %p\n"))
#creating a function to introduce the school chatbot and also welcome the user
def introduction():
    print("        LINAR          \nSCHOOL OF MEDIA AND ICT\nComputer training school")
    print("We take you from being a novice to an expert level with our hands-on practical training\n")
    time.sleep(3)
    global name
    name= input("Chatbot: Hello welcome :)....Enter your name?\nYou: ")
    print("Chatbot: Nice to meet you",name,"!\n")
    print("Chatbot: I'm the school chatbot,I'm here to help with any questions....just ask ;)...\n")
    time.sleep(1)
introduction()
#Creating a function to print out lists of inquiry 
def school_chatbot():
    print("\nSchool Chatbot: What would you like to make an inquiry on?\nChoose between 1-20 or enter 'exit' to end the conversation\n")
    time.sleep(2)
    print("1. About the school")
    time.sleep(1)
    print("2. Courses offered")
    time.sleep(1)
    print("3. List of ICT courses offered")
    time.sleep(1)
    print("4. Prices and duration of each ICT course")
    time.sleep(1)
    print("5. List of Media courses offered")
    time.sleep(1)
    print("6. Prices and duration of each media course")
    time.sleep(1)
    print("7. Vocational skills")
    time.sleep(1)
    print("8. School opening and closing hours/days")
    time.sleep(1)
    print("9. School location")
    time.sleep(1)
    print("10. School email and contact")
    time.sleep(1)
    print("11. School aim")
    time.sleep(1)
    print("12. School mission and vision")
    time.sleep(1)
    print("13. Learning benefits")
    time.sleep(1)
    print("14. Linar School of ICT/Media training")
    time.sleep(1)
    print("15. Linar School of ICT/Media after training")
    time.sleep(1)
    print("16. Payment details")
    time.sleep(1)
    print("17. Register for a course")
    time.sleep(1)
    print("18. More inquiries about a course")
    time.sleep(1)
    print("19. Talk to the manager\n")
    time.sleep(1)
#creating different functions to print the response to every inquries
def About_school():
    print("\nSchool Chatbot: Linar is an IT/Media company that focuses on IT/Media,trainings and services for businesses\nLinar a nascent IT/Media company started operations in the year 2018,\nwith well-trained staffs and proactive skills.")
    print("We have consulted for various reputable organizations within and outside our locality;\npresently we have been able to gain the trust of our clients for overwhelming performance and excellent reliability.\nWe provide media services such as Digital marketing, social media management and trainings.\nWe also provide IT support and services such as app development and lots more using cutting edge technology.")

def Courses_offered():
    print("\nSchool Chatbot: The school offers just two variety of course, including:\n-->Ict courses\n-->Media courses.")

def Ict_courses():
    print("\nSchool Chatbot: We offer 15 Ict courses")
    print("1. Python\n2. Web design\n3. Digital marketing\n4. Ict fundamentals\n5. Graphic design\n6. (UI/UX) Design\n7. Data Analytics\n8. Cloud engineering")
    print("9. Web application development\n10. Web application security\n11. Computer networking\n12. Game Development\n13. Computer Hardware engineering\n14. Web design using wordpress\n15. office productivity. ")

def Ict_courses_prices_duration():
    print()

def Media_courses():
    print("\nSchool Chatbot: We offer 6 Media courses")
    print("1. Filmmaking\n2. Photography\n3. Videography\n4. 3D Animation & Visual Effects\n5. Drawing\n6. Arts")

def Media_courses_prices_duration():
    print()
def Vocational_skills():
    print("\nSchool Chatbot: We also train on skills like:\n-> Catering\n-> Makeup/Gele\n-> Fashion designing\n-> Woodwork\n-> Interior design\n-> Solar design/installation, and more.")

def School_opening_closing_hours():
    print("\nSchool Chatbot: The school is open from 9:00 am to 5:00 pm, Monday to Friday and Saturday 11:00 am to 5:00pm")

def School_location():
    print("\nSchool Chatbot: The School is located at: Linar Library/Workspace\nAddress: O'mark Bustop, KM 9 Isheri Lasu Rd, Igando 102213, Lagos")

def School_contact():
    print("\nSchool Chatbot:You can reach the via calls, message or WhatsApp : +2348132590905.\nYou can also message the school on email:\nadmin@linar.ng")

def School_aim():
    print("\nSchool Chatbot: Our aim is to offer the most cost-effective and reliable IT/media solutions and our services match international standards.")

def School_mission_vision():
    print("\nSchool Chatbot: Our school's mission is to collaborate with ICT experts and institutions globally to enhance people's creative minds equipping them with ICT knowledge and tools to produce international certified professionals")
    print("\nOur school vision is leveraging Media and ICT to foster people's creative minds towards problem solving innovations..")

def Learning_benefits():
    print("\nSchool Chatbot: Learning at our school provides numerous benefits, including:\n->Realistic and 100% practical trainings\n->Single-handedly carrying out a project related to what was learnt\n->Certificate of Completion")
    print("->Access to systems(computers)\n->Access to the training facility during and after classes\n->Reading and self-development space")
    
def Training():
    print("\nSchool Chatbot: Our Training is designed for prospective students who are ready to learn and build a career in different Media and ICT fields")
    print("our training is designed to eliminate the problems students have with learning by going strictly on practical and working with projects.")
    print("Aside from understanding the fundamentals of our courses, we expose our students to the practical area.")
def After_training():
    print("\nSchool Chatbot: We train our students to excel in any skill learnt, We train them to be able to compete globally by teaching the rudiments of each course,")
    print("We also give our students a platform to practice in the industry through Internships(within or outside) our organization")

def Course_payment():
    print("\nSchool Chatbot: Payment details:\nPay only to the registered company account\nAccount No- 0427119078\nAccount Name- LINAR LIMITED Bank- GTBank")

def Registration():
    print("\nSchool Chatbot: To register for a course, please visit our School website or contact the school's admissions department via phone contact:  +2348132590905 .")

def More_inquiry():
    print("\nSchool Chatbot: For more inquiry pls visit the School 'Linar School of Media& ICT'\nAddress:Km 9, Isheri-LASU Expressway, Igando, Lagos\nCall number: 08132590905")
        
def Manager():
    print("\nSchool Chatbot: The manager is available to speak with you from 9:00 am to 5:00 pm, Monday to Friday via calls, message or\n WhatsApp : +2348132590905.:.")
def Electives():
    print("\nSchool Chatbot: We offer a variety of electives, such as:\n->Coding\n->Logo making\n->Drawing\n->Photography.")
# Main loop to keep the conversation with the chatbot
while True:
    school_chatbot() # Present the menu of inquiries
    choice = input("You: ")  # Get the user's choice
    #check the user's choice and call the corresponding function
    if choice == '1':
        About_school()
    elif choice == '2':
        Courses_offered()
    elif choice == '3':
        Ict_courses() 
    elif choice == '4':
        Ict_courses_prices_duration()
    elif choice == '5':
        Media_courses()
    elif choice == '6':
        Media_courses_prices_duration()
    elif choice == '7':
        Vocational_skills()
    elif choice == '8':
        School_opening_closing_hours()
    elif choice == '9':
        School_location()
    elif choice == '10':
        School_contact()
    elif choice == '11':
        School_aim()
    elif choice == '12':
        School_mission_vision()
    elif choice == '13':
        Learning_benefits()
    elif choice == '14':
        Training()
    elif choice == '15':
        After_training()
    elif choice == '16':
        Course_payment()
    elif choice == '17':
        Registration()
    elif choice == '18':
        More_inquiry()
    elif choice == '19':
        Manager()
    elif choice == '20':
        Electives()
        # Ask if the user wants to make another inquiry or exit the conversation
    choice = input("\nSchool Chatbot: Do you want to make another inquiry (yes/no)\You: ").lower()
    if choice == 'no':
        break
    elif choice != 'yes':
        print("\nSchool Chatbot: Invalid choice. Please enter either 'yes' or 'no'")
    elif choice.lower() == 'exit':
        break
    else:
            print("\nSchool Chatbot: Invalid choice. Please enter a number between 1 and 20.")
