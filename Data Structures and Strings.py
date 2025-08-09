name=str(input("Enter the student's name: "))
dictionary={"Alice":85,"Jam55es":70,"Noah":68,"jack":50,"bob":45}
if name in dictionary:
    print(name,"marks: ",dictionary.get(name))
else:
    print("Student not found.")
