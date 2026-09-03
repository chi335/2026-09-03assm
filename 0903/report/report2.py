def hex_to_integer(hex_str):
    total = 0
    for char in hex_str:
        # 문자를 직접 0~15의 숫자로 변환 (내장 함수 회피)
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        else:
            digit = 0
            
        total = total * 16 + digit
        
    return total

# 사용 예시
result = hex_to_integer("0000000A")  # 결과: 10
print("변환된 십진수 값:", result)