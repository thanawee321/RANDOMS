import string
import random
import os

list_random = []
list_name = []
english_letters = list(string.ascii_letters)
thai_letters = [chr(i) for i in range(3585, 3631)] + [chr(i) for i in range(3632, 3648)]
non_vowel_thai_letters = [letter for letter in thai_letters if not ('\u0E30' <= letter <= '\u0E3A') and letter not in ['฽', '฾', '฼']]
numbers = list(string.digits)
excluded_specials = ['~', '"', '^', "'","`"]
special_char = [char for char in string.punctuation if char not in excluded_specials]
combined_array = english_letters + non_vowel_thai_letters + numbers + special_char


while True:
    num_char = input("กรุณาใส่ตัวอักษรที่ต้องการสุ่ม : ")
    
    # ตรวจสอบให้แน่ใจว่า num_char เป็นตัวเลข
    if num_char.isdigit():
        num_char = int(num_char)
        if num_char == 0:
            print("กรุณาใส่จำนวนที่ถูกต้องอีกครั้ง")
            continue
    else:
        print("กรุณาใส่ตัวเลขที่ถูกต้อง")
        continue

    # ถ้าใส่ 00 ให้หยุดการทำงาน
    if num_char == 00 or num_char == "00":
        print("จบการทำงาน")
        break
    

    list_name = []  # ล้างรายชื่อก่อน

    while True:
        name = input("รายการพระ : ")
        if name != '0':
            list_name.append(str(name))
        else:
            break

    list_random.clear()  # เคลียร์ข้อมูลจากลิสต์ก่อนเขียนข้อมูลใหม่
    for i in list_name:
        rand_char = ''.join(random.choices(combined_array, k=num_char))  # สร้างตัวอักษรสุ่ม 10 ตัวสำหรับแต่ละชื่อ
        print(f"{i} : {str(rand_char)}")
        list_random.append((i, rand_char))
    
    # บันทึกลงไฟล์แบบไม่ลบข้อมูลเก่า
    with open('random.txt', 'a', encoding='utf-8') as file:
        for name, char_rand in list_random:
            text = f"{name} : {char_rand}"
            file.write(str(text) + '\n')
        file.write(str("-" * 60) + '\n')
