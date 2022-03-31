import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

###########################################
#	Phone Class that's just for a field
###########################################
#	regVal = Validator ensuring only numbers, 9 - 15 characters in length
#	phoneNumber = the actual number, having been validated
class PhoneNumber(models.Model):
    regVal = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter as '+##########'")
    phoneNumber = models.CharField(max_length=15, validators=[regVal], null=True, blank=True)

###########################################
#	CreditCard Number
###########################################
#	regVal = Validator ensuring only Visa, Mastercard, AmericanExpress
#	creditCardNumber = the actual number, having been validated
class CreditCardNumber(models.Model):
    regVal = RegexValidator(regex=r'^(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13})$', message="Please enter with no spaces")
    creditCardNumber = models.CharField(max_length=16, validators=[regVal], null=True, blank=True)

###########################################
#	CreditCard Security PIN
###########################################
#	regVal = Validator ensuring only numbers, 3 max length
#	creditCardSecurity = the actual number, having been validated
class CreditCardSecurity(models.Model):
    regVal = RegexValidator(regex=r'^(?:\d{3})$', message="CVV 3 digit code")
    creditCardSecurity = models.CharField(max_length=3, validators=[regVal], null=True, blank=True)

###########################################
#	CreditCardExpire
###########################################
#	regVal = Validator, mm/yy
#	creditCardExpire = the actual number, having been validated
class CreditCardExpire(models.Model):
    regVal = RegexValidator(regex=r'^(?:\d{2}\/\d{2})$', message="Please enter mm/yy")
    creditCardExpire = models.CharField(max_length=15, validators=[regVal], null=True, blank=True)


##########################################
#	Email Class that's just for a field
##########################################
#	regVal = Validator ensuring valid email
#	email = the actual email
class Email(models.Model):
    regVal = RegexValidator(regex=r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', message="Emails are case-insensitive")
    email = models.CharField(max_length=50, validators=[regVal], null=True, blank=True)

##########################################
#   PRODUCT CLASS/MODEL
##########################################
#	name = the name
class Product(models.Model):
    name = models.CharField(max_length=200)
    description_text = models.CharField(max_length=500)
    cost = models.IntegerField(default=0)

    # STR FUNCTION ::: for returning info
    def __str__(self):
        return self.name

##########################################
#   PERSON CLASS/MODEL
##########################################
#	username = login/username of Person, up to 20 characters
#	password = login password, up to 20 characters
class Person(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phoneNumber = models.ForeignKey(PhoneNumber, null=True, blank=True,on_delete=models.CASCADE)
    email = models.ForeignKey(Email, null=True, blank=True,on_delete=models.CASCADE)

    # STR FUNCTION ::: for returning firstname
    def __str__(self):
        return self.userName

##########################################
#   COMPANY CLASS/MODEL
##########################################
#	name = name of the company
class Company(models.Model):
	name = models.CharField(max_length = 200)

	# STR FUNCTION ::: for returning companyname
	def __str__(self):
		return self.name

##########################################
#   ADMINISTRATOR CLASS/MODEL
##########################################
#	adminList = contains the list of admins for a Company
class Administrator(Person):
    # many admins to one Company
    adminList = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,

    )

##########################################
#   CUSTOMER CLASS/MODEL
##########################################
class Customer(Person):
    creditCardNumber = models.ForeignKey(CreditCardNumber, null=True, blank=True,on_delete=models.CASCADE)
    creditCardExpireDate = models.ForeignKey(CreditCardExpire, null=True, blank=True,on_delete=models.CASCADE)
    creditCardSecurity = models.ForeignKey(CreditCardSecurity, null=True, blank=True,on_delete=models.CASCADE)