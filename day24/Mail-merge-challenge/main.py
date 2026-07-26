with open("./day24/Mail-merge-challenge/Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()

invited_guests = []
names = open("./day24/Mail-merge-challenge/Input/Names/invited_names.txt", "r")

for name in names.readlines():
    invited_guests.append(name)

for invitee in invited_guests:
    invitation = letter_content.replace("[name]", invitee.strip('\n'))
    
    with open(f"./day24/Mail-merge-challenge/Output/ReadyToSend/letter_for_{invitee}.docx", "w") as invitation_to_send:
        invitation_to_send.write(invitation)

names.close()
    