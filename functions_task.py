import datetime

def check_birthdate(year, month, day):
	if datetime.date(year, month, day) >= datetime.date.today():
		return False
	else:
		return True


def calculate_age(year, month, day):
	user_age = datetime.date.today() - datetime.date(year, month, day)
	user_age_days = ""
	for x in str(user_age):
		if x.isdigit():
			user_age_days = user_age_days + str(x)
		else:
			break

	age_year = int(user_age_days) / 365
	remaining_days = ((int(user_age_days) - (int(age_year)*365)) - (int(age_year)/4))
	age_month = remaining_days / 30
	age_days = remaining_days % 30
	print("User's age is {} years and {} months and {} days".format(int(age_year),int(age_month),int(age_days)))


user_year = input ("Enter your birthday year:  ")
user_month = input ("Enter your birthday month:  ")
user_day = input ("Enter your birthday day: ")

if check_birthdate(int(user_year),int(user_month),int(user_day)):
	calculate_age(int(user_year),int(user_month),int(user_day))
else:
	print ("Your birthdate is invalid. ")


