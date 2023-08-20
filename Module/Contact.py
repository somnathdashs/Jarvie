
Mother="8917617552"
sonu="9337557605"
Friend="LCis5nPhWOqAnh18Ji07bL"


def Get_Mob_or_GID(Person):
    country_code="+91"
    Mob_or_GID=""
    Person=str(Person).lower()
    if "me" in Person:
        Mob_or_GID=country_code+Mother
    elif "sonu" in Person:
        Mob_or_GID=country_code+sonu
        
    elif "friend" in Person:
        Mob_or_GID=Friend
    else :
        Mob_or_GID="Person or Group not found in the contact. Please add it."

    return Mob_or_GID

def IsGroup(Person):
    M_or_ID=str(Get_Mob_or_GID(Person))
    if M_or_ID.isdigit():
        return False
    else:
        return True



def IsinContact(Person):
    if Get_Mob_or_GID(Person).startswith("Person"):
        return False
    else:
        return True



### EMAIL ADD ###

sonu="pinudash104@gmail.com"


def Get_Email_add(statment):
    EmailAdd=""
    statment=str(statment).lower()
    if "subham" in statment:
        EmailAdd=sonu
    else :
        EmailAdd="Email address not found in the Email contact. Please add it."

    return EmailAdd


def Is_In_Email_Contact(statment):
    if Get_Email_add(statment).startswith("Email"):
        return False
    else:
        return True