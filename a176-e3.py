import re
email = "admin@gmail.com"
print("the email is  Valid" if re.match(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$", email)
      else "Invalid email")
