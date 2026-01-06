days = 5
present = 0
i = 1

while i <= days:
    status = input("Present or Absent (P/A): ")

    if status == "P":
        present += 1

    i += 1

print("Total Present Days:", present)
