from studentDAO import studentDAO  

# Create a new student and get the latest ID
latestid = studentDAO.create(('Mark', 45))  

# Check if creation was successful
if latestid is None:
    print("Error: Failed to create student!")
    exit()

# Find by ID
result = studentDAO.findByID(latestid)
print("Student Retrieved:", result)

# Update student information
studentDAO.update(('Fred', 21, latestid))
result = studentDAO.findByID(latestid)
print("Updated Student:", result)

# Get all students
print("\nAll Students in Database:")
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

# Delete the student
studentDAO.delete(latestid)
print(f"Student with ID {latestid} deleted.")
