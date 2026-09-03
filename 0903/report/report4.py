def integer_to_hex(n):
    if n == 0:
        return "0"
    
    # 0~15에 대응하는 16진수 문자 테이블 (내장 함수 회피)
    hex_chars = "0123456789ABCDEF"
    hex_digits = []
    
    while n > 0:
        remainder = n % 16
        hex_digits.append(hex_chars[remainder])
        n = n // 16
        
    # 역순으로 수집된 자릿수를 바로 정렬
    hex_digits.reverse()
    return "".join(hex_digits)

# 사용 예시
result = integer_to_hex(255)  # 결과: "FF"
print("변환된 16진수 문자열:", result)