
def validate_email(email):

    email_character_list = list(email)
    print(email_character_list)

    if not '@' in email_character_list:
        raise ValueError(f'You entered an in valid email: {email}')

    return email


value = validate_email('victoregbejunior@gmail.com')
print(value)
