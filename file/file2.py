# 파일 읽기
#%%
f = open("../resource/test1.txt", "r", encoding="utf-8")
print(f.read())
f.close()


#%%
with open("../resource/test1.txt", "r", encoding="utf-8") as f:
    print(f.read())

#%%
with open("../resource/review.txt","r",encoding="utf-8") as f:
    print(f.read())

# %%
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    for c in f:
        print(c.strip())    # strip() 은 공백 제거

# %% readline() : 줄단위로 읽어오기
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    #print(f.readline())
    line = f.readline()
    while line:
        print(line, end = "")
        line = f.readline()
# %%
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    print(f.readlines())


#%% readlines() : 리스트 구조로 반환
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    for c in content:
        print(c, end="")

#%% score.txt 읽어와서 평균을 구한 후 화면에 출력
with open("../resource/score.txt", "r", encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))

print("평균 :", sum(score) / len(score))
print("평균 : %.2f" % (sum(score) / len(score)))


# %% score.txt 를 읽어와서 평균을 구한 후 화면에 출력
with open("../resource/score.txt", "r", encoding="utf-8") as f:
    scores = f.readlines()
    sum = 0
    for c in scores:
        sum += float(c)
    print("%.2f" % float(sum / len(scores)))

# %% socre.txt 읽어와서 총합과 평균을 구한 후 구한 결과 값을
# result.txt에 쓰기
# 예)
# 총합 : 790
# 평균 : 97.66 

with open("../resource/score.txt", "r", encoding="utf-8") as f:
    scores = f.readlines()
    sum = 0
    for c in scores:
        sum += float(c)
with open("../resource/result.txt", "w", encoding="utf-8") as f:
    f.write("총합 : %d\n" % sum)
    f.write("평균 : %.2f" % float(sum / len(scores)))

# %% 특정 경로의 파일을 읽어 사용자가 지정하는 폴더로 복사하기
import os   # 운영체제와 관련되 기능을 가진 모듈(폴더생성, 폴더목록보기 등)
content = ""
# 사용자에게 읽을 파일을 입력받고 저장할 폴더와 이름도 입력받기
fName = input("읽을 파일 경로 및 파일명 : ")
writePathName = input("저장할 위치 및 저장할 파일명 입력 : ")
# 파일이 존재하면 읽은 후 사용자가 입력한 저장 폴더에 읽은 파일을 저장하기
# os.path.exists("D:/temp/test.txt")
if os.path.exists(fName):
    with open(fName, 'r', encoding="utf-8") as f:
        content = f.read()
    with open(writePathName, 'w', encoding="utf-8") as f:
        f.write(content)
else:
    print("%s 파일이 없습니다." % fName)


# %%
os.path.exists("d:/*.rar") # true false 리턴

# %% info.txt 파일을 읽어 BMI지수를 계산한 후 화면에 출력하기
# BMI 지수 계산 = 체중 / (키 / 180) * 2
# BMI 지수가 25 이상이면 과체중
#           18.5 이상이면 정상체중
#                이하이면 저체중
# 출력 결과 예시
# 이름 : 가나
# 몸무게 : 44
# 키 : 150
# BMI : 12.1354213
# 판정결과 : 저체중
with open("../resource/info.txt", 'r', encoding="utf-8") as info:
    for f in info:
        user = info.readline()
        name = user[:2]
        height = float(user[4:7])
        weight = float(user[9:])
        bmi = weight / ((height / 100) ** 2)
        # print("이름 : %s" % name)
        # print("체중 : %.2f" % weight)
        # print("신장 : %.2f" % height)
        # print("BMI : %.2f" % bmi)
        # 한 줄로 줄이기
        print("\n".join(["이름 : {}", "체중 : {}kg", "신장 : {}cm", "BMI : {:.2f}"]).format(name, weight, height, bmi))

        if bmi >= 25:
            print("BMI : 과체중")
        elif bmi < 25 and bmi >= 18.5:
            print("BMI : 정상체중")
        else:
            print("BMI : 저체중")
        print()


# %% 이진파일

data = ""
try:
    with open('c:/windows/notepad.exe', 'rb') as f1:
        data = f1.read()
    with open('c:/temp/notepad.exe', 'wb') as f2:
        f2.write(data)
except:
    print("복사 실패")


# %%
