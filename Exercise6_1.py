<<<<<<< HEAD
# while True:
#     try:
#         a = input("입력하세요: ")
#         if a == 'stop':
#             break
#         elif int(a) == 1001:
#             break
#         else:
#             pass
#     except :
#         pass
# print("bye")

# while True:
#     try:
#         a = input("입력하세요: ")
#         if a == 'stop':
#             break
#         elif int(a) == 1001:
#             break
#         else:
#             continue
#     except :
#         continue
# print("bye")

####pass와 continue 차이점###

# pass

# for i in range(1, 5):
#     if i == 2:
#         print("ready")
#         pass
#         print("go")
#     print(i)
# 1
# ready
# go
# 2
# 3
# 4

#continue

# for i in range(1, 5):
#     if i == 2:
#         print("ready")
#         continue
#         print("go")
#     print(i)
# 1
# ready
# 3
# 4

while True:
    user_input = input("입력값을 입력하세요: ")
    try:
        if user_input == "stop":
            break
        elif int(user_input) == 1001:
            break
    except :
=======
# while True:
#     try:
#         a = input("입력하세요: ")
#         if a == 'stop':
#             break
#         elif int(a) == 1001:
#             break
#         else:
#             pass
#     except :
#         pass
# print("bye")

# while True:
#     try:
#         a = input("입력하세요: ")
#         if a == 'stop':
#             break
#         elif int(a) == 1001:
#             break
#         else:
#             continue
#     except :
#         continue
# print("bye")

####pass와 continue 차이점###

# pass

# for i in range(1, 5):
#     if i == 2:
#         print("ready")
#         pass
#         print("go")
#     print(i)
# 1
# ready
# go
# 2
# 3
# 4

#continue

# for i in range(1, 5):
#     if i == 2:
#         print("ready")
#         continue
#         print("go")
#     print(i)
# 1
# ready
# 3
# 4

while True:
    user_input = input("입력값을 입력하세요: ")
    try:
        if user_input == "stop":
            break
        elif int(user_input) == 1001:
            break
    except :
>>>>>>> d97a1b790e93937e3c55395fc1d79efe1b78ab1a
        continue