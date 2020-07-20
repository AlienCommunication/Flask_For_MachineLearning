#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:16:06 2020

@author: kris
"""


from flask import Flask

""" NOW I will create that Flask app using that flask object

It is just variable name provides functionality of the main function. As it is

inbuilt  variable in python

"""

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def  hello():
    return  "Hello world"

""" Flask is just work frame work hence will create website 
TO create a url in flask  , @app.route() is a python decorater that 
      
FLask provides to assign URL in our app to function easily. SO

Decorater is telling @app that whenever a user visit our app domain
at the given .route() execute the home() function """
    

if __name__ == '__main__':
    app.run(debug= True)
    


""" Apart from this @app.route() we can go with other approach also which is add_url_rule() function, This function

is useful when there is no view point ANd we need to connect a view function to the end point exeternally


Let's understand the parameter it accepts 

URl rule - It is the url rule provided as a string

End point - IN GENERAL Term, End point is any device which is at the end of any network or end point of a 

Communication channel- IN FLask term, IT is just name of the view function but However you can change it later. 
It acts as reverse look up

View function -

"""


def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
    
""" Now Let's understand  url_for() function. It is used to build a URL to the specific function dynamically 

This function is useful in case we want to avoid hardcoding urls into the templates

The FIRst arguement in this function  is the name of specified function then can put any number of arguements"""


@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
if __name__ =='__main__':  
    app.run(debug = True)  
    


""" NOw I Will move to HTTP methods in Flask 

1. POST Method : To handle POST Requests at the server. We use POST REquests to access the data form at the client side

2. GET Method : It does same as POST but only difference is that POST Does not show the data which is to access

3. Head() : It is similar to the GET but used without  response body.

4. PUT() : IT is used to replace all the current representation of the target resource.

5. DELETE() : IT is used to delete all the current representation"""


@app.route('/login',methods = ['POST'])  """ Rest everything is same before """

@app.route('/login',methods = ['GET'])   """ Same as above"""


""" Flask Session() 
    FLask session is very similar to Coockies, SEssion can be defined as the duration for which a user logs into
    
    the server and logs out. DAta is stored on the server to track the logs of the user"""
    
""" WHAT IS WTF In FLASK?

WTF stands for WT Forms which is intended to provide the interface for the user"""



rom flask_wtf import Form  
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  
  
class ContactForm(Form):  
   name = TextField("Candidate Name ",[validators.Required("Please enter your name.")])  
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])  
   Address = TextAreaField("Address")  
     
   email = TextField("Email",[validators.Required("Please enter your email address."),  
   validators.Email("Please enter your email address.")])  
     
   Age = IntegerField("Age")  
   language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')])  
  
   submit = SubmitField("Submit") 
   
   
   



