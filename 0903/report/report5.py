def add_base_strings(str1, str2, base):
    # 문자를 숫자로 변환하는 헬퍼 함수
    def char_to_val(c):
        if '0' <= c <= '9':
            return ord(c) - ord('0')
        elif 'A' <= c <= 'Z':
            return ord(c) - ord('A') + 10
        elif 'a' <= c <= 'z':
            return ord(c) - ord('a') + 10
        return 0

    # 숫자를 문자로 변환하는 헬퍼 함수
    def val_to_char(v):
        if 0 <= v <= 9:
            return chr(ord('0') + v)
        else:
            return chr(ord('A') + v - 10)

    i = len(str1) - 1
    j = len(str2) - 1
    carry = 0
    result = []

    # 두 문자열 중 하나라도 남았거나 올림수(carry)가 남아있는 동안 반복
    while i >= 0 or j >= 0 or carry > 0:
        val1 = char_to_val(str1[i]) if i >= 0 else 0
        val2 = char_to_val(str2[j]) if j >= 0 else 0

        total = val1 + val2 + carry
        carry = total // base
        digit = total % base

        result.append(val_to_char(digit))

        i -= 1
        j -= 1

    # 역순으로 수집된 결과를 올바른 순서로 뒤집음
    return "".join(reversed(result))

# 사용 예시 (예: 2진수 덧셈)
result_bin = add_base_strings("1011", "1101", 2)  # 11 + 13 = 24 ("11000")
print("진법 덧셈 결과 (Binary):", result_bin)

# 사용 예시 (예: 16진수 덧셈)
result_hex = add_base_strings("1A", "F", 16)      # 26 + 15 = 41 ("29")
print("진법 덧셈 결과 (Hex):", result_hex)