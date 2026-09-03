def binary_to_integer(binary_str):
    total = 0
    for char in binary_str:
        # 문자를 직접 숫자로 변환 (내장 함수 회피)
        bit = 1 if char == '1' else 0
        total = total * 2 + bit
    return total

result = binary_to_integer("0000000000001010")  
print("변환된 십진수 값:", result)
# 사용 예시
# result = binary_to_integer("0000000000001010")  # 결과: 10