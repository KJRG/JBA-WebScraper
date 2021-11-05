import string

# put your code here
username = input()
msg_template = string.Template(
    "Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!")
print(msg_template.substitute(username=username))
