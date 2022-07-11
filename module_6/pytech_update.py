db.student.findOne({"new_student_id_1": 1007})
db.student.updateOne({"new_student_id_1": 1007}, {"$set": {"last_name": "Smith"}})
