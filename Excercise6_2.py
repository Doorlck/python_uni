# freq =0
# while True:
#     try:
#         a = input("입력하세요: ")
#         if a == 'stop':
#             break
#         elif int(a) == 1001:
#             break
#         elif int(a) == 4 :
#             freq +=1
#             continue
#         else:
#             continue
#     except :
#         continue
# print("bye",freq)


freq=0
while True:
    try:
        a = input("입력하세요: ")
        if int(a) == 1001 :
            break
        elif int(a) == 4 :
            freq+=1
            break
    except :
        if a=='stop' :
            continue
print("bye",freq)
