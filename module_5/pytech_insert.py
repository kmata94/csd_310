
new_student_id_1=1007
new_student_id_2=1008
new_student_id_3=1009

db.student.insertOne({new_student_id_1}).inserted_id
db.student.insertOne({new_student_id_2}).inserted_id
db.student.insertOne({new_student_id_3}).inserted_id

db.student.findOne({"new_student_id_1": "1007"})
db.student.findOne({"new_student_id_2": "1008"})
db.student.findOne({"new_student_id_3": "1009"})
