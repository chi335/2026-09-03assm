def multiply_hex_digit_by_string(single_hex, hex_str):
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

    multiplier = char_to_val(single_hex)
    if multiplier == 0 or hex_str == "0":
        return "0"

    carry = 0
    result = []
    
    # 가장 오른쪽 자릿수부터 시작하여 왼쪽으로 이동
    for i in range(len(hex_str) - 1, -1, -1):
        val = char_to_val(hex_str[i])
        total = val * multiplier + carry
        carry = total // 16
        digit = total % 16
        result.append(val_to_char(digit))

    # 연산이 끝난 후 남은 올림수 처리
    while carry > 0:
        digit = carry % 16
        result.append(val_to_char(digit))
        carry = carry // 16

    # 역순으로 수집된 결과를 올바른 순서로 뒤집음
    return "".join(reversed(result))

# 사용 예시 (예: 0x1F * 0xA = 31 * 10 = 310 -> 0x136)
result = multiply_hex_digit_by_string("A", "1F")
print("16진수 단일 자릿수 곱셈 결과:", result)