import email
from tkinter import Label
from wsgiref.validate import validator
from click import password_option
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

app = Flask(__name__)

class RegistrationForm(FlaskForm):
    username = StringField(lable = "Enter Username", validator = [DataRequired(), Length(min = 2, max = 15)])
    email = StringField(lable = "Enter Email", validator = [DataRequired(), Length(min = 2, max = 15)])
    password = PasswordField(lable = "Enter Password", validator = [DataRequired(), Length(min = 5, max = 15)])
    confirm_password = PasswordField(lable = "Confirm Password", validator = [DataRequired(), EqualTo('password')])
    submit = SubmitField(Label = "Click to Register")


class LoginForm(FlaskForm):
    username = StringField(lable = "Enter Username", validator = [DataRequired(), Length(min = 2, max = 15)])
    password = PasswordField(lable = "Enter Password", validator = [DataRequired(), Length(min = 5, max = 15)])
    submit = SubmitField(Label = "Click to Login")


if __name__ == '__main__':
    app.run(debug=True)
