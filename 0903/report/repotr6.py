def add_hex_strings(hex1, hex2):
    def char_to_val(c):
        if '0' <= c <= '9':
            return ord(c) - ord('0')
        elif 'A' <= c <= 'F':
            return ord(c) - ord('A') + 10
        elif 'a' <= c <= 'f':
            return ord(c) - ord('a') + 10
        return 0

    def val_to_char(v):
        if 0 <= v <= 9:
            return chr(ord('0') + v)
        else:
            return chr(ord('A') + v - 10)

    i = len(hex1) - 1
    j = len(hex2) - 1
    carry = 0
    result = []

    # 두 문자열의 끝에서부터 시작하여 올림수가 없을 때까지 반복
    while i >= 0 or j >= 0 or carry > 0:
        v1 = char_to_val(hex1[i]) if i >= 0 else 0
        v2 = char_to_val(hex2[j]) if j >= 0 else 0

        total = v1 + v2 + carry
        carry = total // 16
        digit = total % 16

        result.append(val_to_char(digit))

        i -= 1
        j -= 1

    # 역순으로 수집된 결과를 올바른 순서로 뒤집음
    return "".join(reversed(result))

# 사용 예시
result = add_hex_strings("1A3F", "2B")  # 1A3F + 2B = 1A6A
print("16진수 덧셈 결과:", result)