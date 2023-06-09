import mysql.connector # import mysql connector to connect to the database
import cv2 # import cv2 library to read the image path

# Establish a database connection
db = mysql.connector.connect(
    host="localhost", # host name of your database
    user="root", # username of your database
    password="", # password of your database
    database="pic_db" # database name
)

# Function to fetch and display the image based on user input
def fetch_image(description):
    cursor = db.cursor()
    # Make a querry to database
    query = "SELECT image_path, name,position,description FROM pic_tb WHERE description = %s OR name = %s OR position = %s OR country = %s"

    # execute the querry and get the result
    cursor.execute(query, (description, description, description, description))
    result = cursor.fetchone()

    # Check if the querry contains the result data 
    if result:

        # get the image path from the result
        image_path = result[0] 

        # read the image path using cv2 library
        image = cv2.imread(image_path)
    
        # print the result of the user search
        print("User Search result : ", result)


        # if cv2 libabry can read the image path and continue to show the image 
        if image is not None:
            cv2.imshow("Image", image) # show the image
            cv2.waitKey(0) # wait for the user input
            cv2.destroyAllWindows() # close the image window

        else:
            # if cv2 libary can't read the image path  the error message
            print("Failed to load image.") 
            
    else:
        print("No image found for the given description.")

# Use speech recognition to get user input
def recognize_speech():

    # import speech recognition library
    import speech_recognition as sr 

    # initialize the speech recognition library
    r = sr.Recognizer() 

    # use the imported library to listen the user voice
    with sr.Microphone() as source:

        # print the message to the user listen to the user voice
        print("Listening...")

        # audio to listen to voice input of user 
        audio = r.listen(source)


    # make a try catch of the audio input by the user 
    try:
        description = r.recognize_google(audio)
        print("Description:", description)
        fetch_image(description)

   
     # if the audio input is not recognize by the system print the error 
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")

        # and ask the user to enter the text description
        fallback_text = input("Please enter the text description: ")

        # call the function to fetch the image based on the user input
        fetch_image(fallback_text)

    # If the speech recoginition libabry is not working or not internet  print the error
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# call the function to start the program
recognize_speech()

# Close the database connection
db.close()








































# import speech_recognition as sr
# import mysql.connector
# import cv2

# # Set up the speech recognition system
# r = sr.Recognizer()

# # Establish a database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="pic_db"
# )

# # Function to fetch and display the image based on user input
# def fetch_image(description):
#     cursor = db.cursor()
#     query = "SELECT image_path FROM pic_tb WHERE description = %s"
#     cursor.execute(query, (description))
#     result = cursor.fetchone()

#     if result:
#         image_path = result[0]
#         image = cv2.imread(image_path)

#         if image is not None:
#             cv2.imshow("Image", image)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#         else:
#             print("Failed to load image.")
#     else:
#         print("No image found for the given description.")
#         fallback_text = input("Please enter the text description: ")
#         fetch_image(fallback_text)
        

# # Use speech recognition to get user input
# def recognize_speech():
#     import speech_recognition as sr
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)

#     try:
#         description = r.recognize_google(audio)
#         print("Description:", description)
#         fetch_image(description)

#     except sr.UnknownValueError:
#         print("Speech recognition could not understand audio.")
#         # fallback_text = input("Please enter the text description: ")
#         # fetch_image(fallback_text)

#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Example usage
# recognize_speech()

    

# # Close the database connection
# db.close()





# # # Use speech recognition to get user input
# # with sr.Microphone() as source:
# #     print("Listening...")
# #     audio = r.listen(source)

# # try:
# #     # Recognize speech using Google Speech Recognition
# #     print("Recognizing...")
# #     description = r.recognize_google(audio)
# #     print("Description:", description)

# #     # Fetch and display the image based on the description
# #     fetch_image(description)

# # except sr.UnknownValueError:
# #     print("Speech recognition could not understand audio.")
# # except sr.RequestError as e:
# #     print("Could not request results from Google Speech Recognition service; {0}".format(e))