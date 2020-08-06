#%%
# q1) A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는
#     다음과 같다. A 학급의 평균을 구하시오
#     70,60,55,75,95,90,80,85,100
#     [조건] 중간고사 점수를 리스트로 생성하고 평균 구하기
score = [70,60,55,75,95,90,80,85,100]
sum = 0
for i in score:
    sum += i
print("평균 : %d" % (sum // len(score)))

#%%
# q2) 아래 문자열의 길이를 구하시오.
#  str1 = "dk2jd23iljdk2jd93fdkedieliddkfiejfied"
str1 = "dk2jd23iljdk2jd93fdkedieliddkfiejfied"
print(len(str1))

#%%
# q3) 화면에 * 기호 100개를 표시하기
print("*" * 100)

#%%
# q4) 문자열 30을 각각 정수형, 실수형, 문자형으로 변경해서 출력하기
str2 = "30"
print(type(int(str2)))
print(int(str2))
print(type(float(str2)))
print(float(str2))
print(type(str2))
print(str2)

#%%
# q5) 문자열 Niceman 에서 man 문자열만 출력하기
str3 = "Niceman"
print(str3[4:])

#%%
# q6) 문자열 http://www.daum.net 에서 http:// 제거하고 출력하기
str4 = "http://www.daum.net "
str4.replace("http://", "")
print(str4)

#%%
# q7) 문자열 abcdefghijklmn 에서 슬라이싱을 이용해 "cde" 만 출력하기
str5 = "abcdefghijklmn"
print(str5[2:5])

#%%
# q8) 다음 리스트에서 "Apple" 항목만 삭제하고 출력하기
#     ["Banana","Apple","Orange","Grape"]
list2 = ["Banana","Apple","Orange","Grape"]
list2.remove("Apple")
print(list2)

#%%
# q9) 다음 리스트에서 '정' 글자만 제외하고 출력하기
#     ["갑","을","병","정","경"]
list3 = ["갑","을","병","정","경"]
list3.remove("정")
print(list3)

#%%
# q10) 다음 리스트에서 5글자 이상의 단어만 출력하기
#      ["nice","study","python","anaconda","!"]
list4 = ["nice","study","python","anaconda","!"]
for s in list4:
    if len(s) >= 5:
        print(s)

#%%
# q11) 아래 리스트에서 소문자만 출력하기
#      ["A","b","c","D","e","F","G","h"]
list5 = ["A","b","c","D","e","F","G","h"]
for s in list5:
    if str(s).islower():
        print(s)

#%%
# q12) 아래 리스트에서 소문자는 대문자로 대문자는 소문자로 출력하기
#      ["A","b","c","D","e","F","G","h"]
list6 = ["A","b","c","D","e","F","G","h"]
for i in range(0, len(list6)-1):
    list6[i] = str(list6[i]).swapcase()
print(list6)

# %%
# q13) 주차장 프로그램 작성하기
park = []
cars = []
num = 0
while num != 3:
    num = int(input("[1] 자동차 넣기  |  [2] 자동차 빼기  |  [3] 종료 : "))
    if num == 1:
        park.append(chr(65 + len(park)))
        print("%s 자동차 들어감. 주차장 상태 ==> " % (chr(64 + len(park))), end="")
        print(park)
    if num == 2:
        if park == []:
            print("빠져나갈 자동차가 없음")
        else:
            print("%s 자동차 나감. 주차장 상태 ==> " % park[-1], end="") 
            park.pop()
            print(park)


# %%
list11 = []
list11.append('A')
print(list11)



# %%
print(ord('A'))
print(chr(65))