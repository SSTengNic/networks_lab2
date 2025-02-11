#!/bin/bash

BASE_URL="http://127.0.0.1:8000"  # Change this if your API runs on a different host


curl -X 'POST' 'http://127.0.0.1:8000/students/upload' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'name=John Doe' \
-F 'student_id=1003416' \
-F 'gpa=3.8' \
-F 'file=@../Nicholas_Teng_Resume.pdf'


# echo "[TEST 1] Testing GET all students..."
# echo "GET http://127.0.0.1:8000/students"

# curl -i -X GET "$BASE_URL/students"
# echo -e "\n-----------------------------\n"

# echo "[TEST 2] Testing GET students with sortBy query parameter..."
# echo "GET http://127.0.0.1:8000/students?sortBy=gpa"
# curl -i -X GET "$BASE_URL/students?sortBy=gpa"
# echo -e "\n-----------------------------\n"

# echo "[TEST 3] Testing GET students with count query parameter..."
# echo "GET http://127.0.0.1:8000/students?count=2"
# curl -i -X GET "$BASE_URL/students?count=2"
# echo -e "\n-----------------------------\n"

# echo "[TEST 4] Testing GET students with sortBy and count query parameter..."
# echo "GET http://127.0.0.1:8000/students?sortBy=gpa&count=2"
# curl -i -X GET "$BASE_URL/students?sortBy=gpa&count=2"
# echo -e "\n-----------------------------\n"


# echo "[TEST 5] Testing POST create student..."
# curl -i -X POST "$BASE_URL/students" -H "Content-Type: application/json" -d '{
#   "name": "John Doe",
#   "student_id": "123456",
#   "gpa": 3.8
# }'
# echo -e "\n-----------------------------\n"

# echo "[TEST 6] Testing GET specific student to show that resource has indeen been created..."
# curl -i -X GET "$BASE_URL/students/123456"
# echo -e "\n-----------------------------\n"


# echo "[TEST 7] Testing POST invalid data, missing name (Returns 400)..."
# curl -i -X POST "$BASE_URL/students" -H "Content-Type: application/json" -d '{
#   "name": "",
#   "student_id": "1122334",
#   "gpa": 3.8
# }'
# echo -e "\n-----------------------------\n"

# echo "[TEST 8] Testing DELETE student..."
# curl -i -X DELETE "$BASE_URL/students/123456"
# echo -e "\n-----------------------------\n"

# echo "[TEST 9] Testing DELETE of a nonexistent user (Returns 404)..."
# curl -i -X DELETE "$BASE_URL/students/123456"
# echo -e "\n-----------------------------\n"


# echo "[TEST 10]Testing GET deleted student (Returns 404)..."
# curl -i -X GET "$BASE_URL/students/123456"
# echo -e "\n-----------------------------\n"
