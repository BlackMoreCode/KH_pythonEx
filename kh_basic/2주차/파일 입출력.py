# 파일 입/출력: 파일을 읽고 쓰는 동작
# 파일 객체, 파일명, "w" => "wt", 한글깨짐 방지 (utf-8)

# score_file = open("score.txt", "w", encoding="utf-8")
# # score_file = open("score.txt", "a", encoding="utf8") # append
# print("수학 : 55", file=score_file) # print() 함수를 사용해 파이렝 쓰기
# print("영어 : 75", file=score_file)
# score_file.write("국어 : 90" + "\n") # 줄바꿈 포함 (\n)
# score_file.write("코딩 : 100" + "\n")
# score_file.close() #오픈한 파일은 반드시 닫아야 한다!

# # 파일 읽기
# # read() 함수: 파일 내의 모든 내용을 읽어서 하나의 문자열로 반환
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()


# # readline() 함수: 해당 파일의 내용을 한 라인씩 읽어들임.
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line, end="")
# score_file.close()


# # readlines() 함수: 해당 파일의 모든 내용을 읽어서 리스트로 반환
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()


# # with 키워드: close() 메서드를 불러주지 않아도 자동으로 닫아주는 기능
# with open('score.txt', 'r', encoding="utf-8") as score_file:
#     lines = score_file.readlines()
#     for line in lines:
#         print(line, end="")

# # 위 구문과 동일한 내용
# file = open('textfile.txt', 'r')
# contents = file.read()
# file.close()

# pickle => 파이썬 객체를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 모듈
import pickle

# # 객체를 직렬화하여 파일에 저장하기
# data = {'name': 'Alice', 'age': 30, 'addr': 'New York'}
# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file) #dump => 직렬화를 해주는 문법. 해당 객체를 파일에 직렬화해서 쓰기

# 파일에서 객체를 역직렬화하여 복원하기
with open('data.pickle', 'rb') as file:
    restored_data = pickle.load(file)

print(restored_data)  # {'name': 'Alice', 'age': 30, 'addr': 'New York'}