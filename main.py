student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dic = {row.letter: row.code for (idx, row) in df.iterrows()}
# print(nato_alphabet_dic)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# 인풋을 받는다.
# 대문자화 한다.
# 한개의 단어를 한 글자 마다 nato의 밸류값으로 리스트에 저장하여 담는다.
# 조건을 단다. 가지고있는 값이 있는지 없는지

user_input = input("이름을 입력하세요").upper()
user_input_lst = [nato_alphabet_dic[alphabet] for alphabet in user_input]

# print(user_input_lst)

# user_nato = {key: value for (key, value) in nato_alphabet_dic if key in user_input_lst}
# print(user_nato)

