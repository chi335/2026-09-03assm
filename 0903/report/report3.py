def integer_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = []
    while n > 0:
        remainder = n % 2
        # 숫자를 문자로 변환 (내장 bin() 함수 회피)
        binary_digits.append('1' if remainder == 1 else '0')
        n = n // 2
        
    # 역순으로 수집된 비트를 바로 정렬
    binary_digits.reverse()
    return "".join(binary_digits)

# 사용 예시
result = integer_to_binary(10)  # 결과: "1010"
print("변환된 이진수 문자열:", result)