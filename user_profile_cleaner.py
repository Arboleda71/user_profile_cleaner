name=input("Enter your full name:")
name=name.strip().lower().title()

email=input("Enter your full Email:")
email=email.strip().lower()

city=input("Enter your City:")
city=city.strip().lower().title()

comment=input("Write a short comment about yourself:")
comment=comment.strip().replace("  "," ")

print(f"\nUser profile Summary")
print(f"Name:{name}")
print(f"Email:{email}")
print(f"City:{city}")
print(f"Comment:{comment}")