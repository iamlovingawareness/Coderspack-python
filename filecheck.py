# Coderspack-python
"""for python programs for mycaptain work"""
filename=str(input("Enter the file name"))
a=filename.split(".")

if (a[1]=="py"):
    print("The name of the extension is python")
elif (a[1]=="exe"):
    print("the name of the extension is executable file.")

elif a[1]=="docx":
    print("The name of the extension is word document")

elif a[1]=="dwg":
    print("The name of the extension is drawing file")

elif a[1]=="jpg":
    print("The name of the extension is JPEG image file")

else:
    print("Sorry the file extension doesnt exist in our database.")
          
