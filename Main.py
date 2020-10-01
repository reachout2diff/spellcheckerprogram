import language_check

tool = language_check.LanguageTool('en-US')
i = 0

# Path of file which needs to be checked
with open(r"MyText.txt", 'r') as x:

    for line in x:
        matches = tool.check(line
                             )
        i = i + len(matches)
        pass

# prints total mistakes which are found
# from the document
print("No. of mistakes found in document is ", i)
print()

# prints mistake one by one
for mistake in matches:
    print(mistake)
    print()