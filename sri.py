from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, event
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

uri = "mongodb+srv://yasiru11:yasiru11@cluster1.otlcmjt.mongodb.net/"

client = MongoClient(uri, server_api=ServerApi("1"))
DB = client["ssh"]
collection = DB["ysk"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    first_name, set_first_name = use_state("")
    Last_name,set_Last_name=use_state("")
    Username,set_Username=use_state("")
    gender, set_gender = use_state("")  
    phone, set_phone = use_state("")
    Email,set_Email=use_state("")
    password, set_password = use_state(0)
    
    def mysubmit(MyCrud):
        newtodo = {"first_name": first_name,"Last_name":Last_name,"Username":Username,"gender": gender,  
            "phone": phone,"Email":Email,"password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data

    # looping data from alltodo to show on web


        user_data = {
            "first_name": first_name,
            "last_name": Last_name,
            "username": Username,
            "email": Email,
            "password": password,
            "gender": gender,
        }
        # Insert user data into MongoDB
        result = collection.insert_one(user_data)
        print("result")
    
    return html.div(
                 
      {"style": 
         {"display": "flex",
                "justify-content": "center",  # Centering horizontally
                "align-items": "center",      # Centering vertically
                "background-image": "url(https://c1.wallpaperflare.com/preview/934/689/246/sri-lanka-flag.jpg)", 
                "background-size": "cover",
                "height": "100vh",  # Adjust as needed
                "width": "100vw",   # Adjust as needed
                "margin": "15px",
                "padding": "15px",}
           },
        

        ## creating form for submission
        html.form(
        # Heading
               {"on submit": mysubmit}, 
         html.img(
        {
         "src": "https://c4.wallpaperflare.com/wallpaper/634/90/518/artistic-cultural-devil-mask-wallpaper-preview.jpg",
         "class_name": "img-fluid",
         "style": {"width": "100px","height":"100px",
         "justify_content": "center","margin_right":"0px",
         "margin_left":"10px","margin_top":"5px","margin_bottom":"8px"},
         "alt": "picture",}),
         
                html.b(html.h1(
                    {"style": {"font-family": "Arial", "font-size": "26px", "justify_content": "center","color":"blue"}}
                    ," WELCOME TO FREE PARADAISE",)),
                
                    html.b(html.h2(
                    {"style": {"font-family": "Arial", "font-size": "20px","color":"green"}}
                    ,'Sign-Up With Us')),

                html.label(
                    {"style": {"font-family": "Arial",  "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box","font-size": "14px","color": "#b0e0e6"}}
                    ,"First name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "First name",
                        "on_change": lambda event: set_first_name(event["target"]["value"]),
                    }
                    ),
                html.br(),

                html.label(
                    {"style": {"font-family": "Arial", "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box", "font-size": "14px","color": "#b0e0e6"}}
                    ,"Last name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Last name",
                        "on_change": lambda event: set_Last_name(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box", "font-size": "14px","color": "#b0e0e6"}}
                    ,"Username"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Username",
                        "on_change": lambda event: set_Username(event["target"]["value"]),
                    }
                    ),
                html.br(),
                html.p(""),
                 # Adding gender radio buttons
            html.label(
                {
                    "style": {
                        "font-family": "Arial",
                        "font-size": "14px","border-radius": "4px",
                        "box-sizing": "border-box",
                        "color": "#b0e0e6",
                    }
                },
                "Gender:",
            ),
            html.br(),
            html.input(
                {
                    "type": "radio",
                    "name": "gender",
                    "value": "Male",
                    "on_change": lambda event: set_gender(event["target"]["value"]),
                },
            ),
            "Male",
            html.input(
                {
                    "type": "radio",
                    "name": "gender",
                    "value": "Female",
                    "on_change": lambda event: set_gender(event["target"]["value"]),
                },
            ),
            "Female",
            html.input(
                {
                    "type": "radio",
                    "name": "gender",
                    "value": "Other",
                    "on_change": lambda event: set_gender(event["target"]["value"]),
                },
            ),
            "Other",
            html.br(),
             html.label(
                {
                    "style": {
                        "font-family": "Arial",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",
                        "font-size": "14px",
                        "color": "#b0e0e6",
                    }
                },
                "Phone Number",
            ),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "Phone Number",
                    "on_change": lambda event: set_phone(event["target"]["value"]),
                }
            ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial",  "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box","font-size": "14px","color": "#b0e0e6"}}
                    ,"Gmail"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Email",
                        "on_change": lambda event: set_Email(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "border-radius": "4px",
                        "box-sizing": "border-box","font-size": "14px","color": "#b0e0e6"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                    }
                ),
                
                html.br(),
                html.p(""),
                # creating submit button on form
                html.button(
                    {
                        "type": "sign_up",
                        "on_click":event(lambda event:mysubmit(event)),
                    },
                    "sign_up",
                ),
    # add a button
                html.button(
                {
                    "type": "Reset",
                    "on_click":lambda event: set_first_name("") and set_Last_name("") and set_Username("")and set_gender("") and set_phone("") and set_Email("") and set_password(0)
                },
                "Reset",
                ),
                ),
       
    )
    

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI



def login(
    login_data: dict,
): 
    first_name= login_data["first_name"]
    Last_name=login_data["Last_name"]
    Username=login_data["Username"]
    gender = login_data["gender"]  
    phone = login_data["phone"]
    Email=login_data["Email"]
    password = login_data["password"]

    # Create a document to insert into the collection
    document = {"first_name": first_name,"Last_name":Last_name,"Username":Username,"gender": gender,
        "phone": phone,"Email":Email,"password": password}
    #logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}

configure(app, MyCrud)