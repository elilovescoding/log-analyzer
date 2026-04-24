# open the log file
file = open("sample.log", "r")

# read all lines from the file
lines = file.readlines()

# counters
failed_logins = 0
errors = 0

# go through each line
for line in lines:
    line = line.lower()

    if ("failed login" in line) or ("login failed" in line):
        failed_logins += 1

    if "error" in line:
        errors += 1

# print results
print("Failed logins:", failed_logins)
print("Errors:", errors)

# close file
file.close()