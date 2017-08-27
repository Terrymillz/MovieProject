from __future__ import unicode_literals
from django.db import models


# Create your models here.
# =================================================================
# Model Functions
# =================================================================
class UserManager(models.Manager):
    def register(self, data):
        errors = []
        try: #check to see if the email is already in use
            User.objects.get(email=data['email'])
            print 'email is already registered'
            errors.append('This email is already registered')
        except:
            pass
            #first name validations
        if data['first_name'] == '':
            errors.append('The First name cannot be blank')
        elif data['first_name'].isdigit():
            errors.append('The First Name can only be characters!')
        #Last Name Validations
        if data['first_name'] == '':
            errors.append('The First name cannot be blank')
        elif data['first_name'].isdigit():
            errors.append('The First Name can only be characters!')
        #email Validations

        if data['email'] == '':
            errors.append('The Email Field cannot be blank')
        # ----------------------
        # MUST ADD EMAIL REGEX INTO VALIDATIONS
        # ---------------------
        # Password validation
        if len(data['password']) < 1 :
            errors.append('The password cannot be blank')
# ****************************************************************
# ****************************************************************
# BCRIPT NEEDS TO BE ADDED BEFORE DEPLOYMENT
# ****************************************************************
# ****************************************************************



        if len(errors) == 0: #if there are no errors in the validations
            user = User.objects.create( # create the new user
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
            )
            print 'User was added'
            return {'user': user, 'errors': None}
        else:
            print 'User was NOT added'
            return {'user': None, 'errors': errors}



    def login(self, data): #the function for validating a log in
        errors = []
        try:
            foundUser = User.objects.get(email=data['email'])
            print "User is found"
            if foundUser.password == data['password']:
                return {'user': foundUser, 'errors': None}
            else:
                errors.append('Email or password is incorrect')
                return {'user': None, 'errors': errors }

        except:
            print "there is no user with that name"
            errors.append('Email or password is incorrect')
            return {'user': None, 'errors': errors }




# =================================================================
# Models
# =================================================================
#this is the Model for our users ==================
class User(models.Model):
#Users
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# this is the model for the profile thats attached to a user =======
class Profile(models.Model):
    email = models.CharField(max_length=100, default='null')
    birthday = models.DateField()
    hometown = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, related_name='users')

#this is the Model for our movies ==================
class Movie(models.Model):
    api_Movie_code = models.CharField(max_length=100)
