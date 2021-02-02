# Type in the filename of the Fails to Deliver Data
fname = input("Enter the name of the file:")

try:
    fhandle = open(fname)

except Exception:
    print("File not found, please try again")
    quit()

# Type in the stock ticker to find it
search = (input("Enter stock ticker name you wish to search:")).upper()

content = []
for line in fhandle:
    line.rstrip()
    newline = line.split("|")
    try:
        if newline[2] == search:
            content.append(line)
    except Exception:
        print("")

for item in content:
    print(item)

if len(content) < 1:
    print("Selected ticker not found in list, please try again")
