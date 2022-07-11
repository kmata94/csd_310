student_id=1010

db.student.insertOne({student_id}).inserted_id

db.student.findOne({"student_id": 1010})

db.student.deleteOne({"student_id": 1010})
