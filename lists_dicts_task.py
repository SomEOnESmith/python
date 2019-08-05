
# ====================== FUNCTION =======================
def append_to_skills():
	for skill in skills:
		print(str(skills.index(skill)+1) + "-",skill )

	skill_number = input("Choose a skill to add to the list (numbers only): ")
	if skill_number.isdigit():
		skill_number
		if int(skill_number) <=len(skills) and int(skill_number) >= 1:
			cv['skills'].append(skills[int(skill_number)-1])
			print("\nSkill been added.\n\n")
		else:
			print("\nWrong number, try again. \n\n")
			append_to_skills()
	else:
		print("\nYou didn't Enter a number, try again.\n\n")
		append_to_skills()
	

def check_skills():
	if 'git' in cv['skills']:
		print ("\n=====> You have been accepted, {} <=====".format(cv['name']))
	else:
		print ('\n\nSorry, "git" must be in the skill list. ')


# declaration of skills and cv dictionary
skills = ['python','c++','c#', 'javaScript', 'crossfit', 'git', 'playing video games']
cv = {}


# ================ Main body ====================

cv['name'] = (input("Enter your name:  ")).capitalize()
cv['age'] = input("Enter your age:  ")
cv['experience'] = input("Enter your years of experience:  ")
cv['skills'] = []

if int(cv['age']) > 18 and int(cv['age']) < 40:
	if int(cv['experience']) > 2:
		append_to_skills()
		append_to_skills()
		check_skills()

	else:
		print ("\n\nSorry, applicant must have more than 2 years of experience.\n")
else:
	print("\n\nSorry, applicant must be between 18 and 40 years old. \n")



