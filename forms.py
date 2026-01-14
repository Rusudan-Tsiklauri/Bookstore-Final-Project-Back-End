from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired
from wtforms import StringField, PasswordField,FloatField, DateField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, length, equal_to

from choices import countries, genres, genders



class SignupForm(FlaskForm):
    username = StringField("შექმენი იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("შექმენი პაროლი", validators=[DataRequired(), length(min=8, max=64,
                                                                                  message="პაროლის სიგრძე უნდა იყოს 8დან 64 სიმბოლომდე")])
    repeat_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("password",
                                                                                            message="პაროლები უნდა ემთხვეოდეს ერთმანეთს")])
    gender = SelectField("აირჩიე სქესი", choices=genders)
    email = StringField("შეიყვანე ემაილი", validators=[DataRequired()])
    birthday = DateField("აირჩიე დაბადების თარიღი")
    country = SelectField("აირჩიე ქვეყანა", choices=countries)

    submit = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    username = StringField("შეიყვანე  იუზერნეიმი")
    password = PasswordField("შეიყვანე პაროლი")

    login = SubmitField("შესვლა")


class ProductForm(FlaskForm):
        image = FileField("აირჩიე წიგნის ფოტო", validators=[FileRequired(), FileAllowed(["png", "jpg", "jpeg"])])
        name = StringField("შეიყვანე წიგნის სახელი", validators=[DataRequired()])
        price = FloatField("შეიყვანე წიგნის ფასი", validators=[DataRequired()])
        author = StringField("შეიყვანე წიგნის ავტორი", validators=[DataRequired()])
        genre = SelectField("აირჩიე წიგნის ჟანრი", choices=genres)
        description = StringField("შეიყვანეთ წიგნის აღწერა", validators=[DataRequired()])
        submit = SubmitField("დამატება")


class OrderForm(FlaskForm):
    name  = StringField("შეიყვანეთ თქვენი სახელი", validators=[DataRequired()])
    address = StringField("შეიყვანე თქვენი მისამართი", validators=[DataRequired()])
    phone = StringField("შეიყვანე თქვენი მობილურის ნომერი", validators=[DataRequired()])


class AuthorForm(FlaskForm):
    name = StringField("ავტორის სახელი", validators=[DataRequired()])
    bio = StringField("ბიოგრაფია", validators=[DataRequired()])
    image = FileField("ავტორის სურათი", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("შენახვა")


class ChangePasswordForm(FlaskForm):
        old_password = PasswordField("ძველი პაროლი", validators=[DataRequired()])
        new_password = PasswordField("ახალი პაროლი", validators=[ DataRequired()])
        repeat_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("new_password",
                                                                                                message="პაროლები უნდა ემთხვეოდეს ერთმანეთს")])
        submit = SubmitField("პაროლის შეცვლა")



