#To enter the extension of the filename 
file_name = input("Enter the filename : ")
file_ext = file_name.split(".")
print("The extension of the file is : " + repr(file_ext[-1]))
