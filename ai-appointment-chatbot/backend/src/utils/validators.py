def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone_number(phone_number):
    import re
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(phone_regex, phone_number) is not None

def validate_appointment_date(date):
    from datetime import datetime
    try:
        datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def validate_user_input(data):
    if not isinstance(data, dict):
        return False
    required_fields = ['email', 'phone_number', 'appointment_date']
    for field in required_fields:
        if field not in data:
            return False
    return (validate_email(data['email']) and
            validate_phone_number(data['phone_number']) and
            validate_appointment_date(data['appointment_date']))