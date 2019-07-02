'''
ord(x): 문자 x를 (ascii)숫자로 변환합니다.
chr(x): (ascii)숫자 x를 문자로 변환합니다.
'''

print(ord('가'))
print(ord('힣'))

korean = [chr(x) for x in range(ord('가'), ord('힣'))]
print(korean)
