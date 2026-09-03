### 문제 및 답

**1. In an 8-bit binary number, which is the most significant bit (MSB)?**
*(8비트 이진수에서 최상위 비트(MSB)는 어느 것인가요?)*
- **정답:** 8비트 이진수에서 가장 왼쪽에 위치한 비트(가장 높은 자릿수인 $b_7$)가 최상위 비트(MSB, Most Significant Bit)입니다.

**2. What is the decimal representation of each of the following unsigned binary integers?**
*(다음 각 부호 없는 이진수의 십진수 표현은 무엇인가요?)*

* **a. 00110101**
  - **계산식:** $(0 \times 128) + (0 \times 64) + (1 \times 32) + (1 \times 16) + (0 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$
  - **연산:** $32 + 16 + 4 + 1$
  - **정답:** $53$

* **b. 10010110**
  - **계산식:** $(1 \times 128) + (0 \times 64) + (0 \times 32) + (1 \times 16) + (0 \times 8) + (1 \times 4) + (1 \times 2) + (0 \times 1)$
  - **연산:** $128 + 16 + 4 + 2$
  - **정답:** $150$

* **c. 11001100**
  - **계산식:** $(1 \times 128) + (1 \times 64) + (0 \times 32) + (0 \times 16) + (1 \times 8) + (1 \times 4) + (0 \times 2) + (0 \times 1)$
  - **연산:** $128 + 64 + 8 + 4$
  - **정답:** $204$


**3. What is the sum of each pair of binary integers?**
*(각 이진수 쌍의 합은 얼마인가요?)*

* **a. $10101111 + 11011011$**
  - **이진수 덧셈 과정:**
    $$\begin{array}{r@{\quad}l}
      10101111 \\
    + 11011011 \\
    \hline
      110001010
    \end{array}$$
  - **검증 (십진수):** $175 + 219 = 394$
  - **정답:** $110001010_2$ (십진수 394)

* **b. $10010111 + 11111111$**
  - **이진수 덧셈 과정:**
    $$\begin{array}{r@{\quad}l}
      10010111 \\
    + 11111111 \\
    \hline
      110010110
    \end{array}$$
  - **검증 (십진수):** $151 + 255 = 406$
  - **정답:** $110010110_2$ (십진수 406)

* **c. $01110101 + 10101100$**
  - **이진수 덧셈 과정:**
    $$\begin{array}{r@{\quad}l}
      01110101 \\
    + 10101100 \\
    \hline
      100100001
    \end{array}$$
  - **검증 (십진수):** $117 + 172 = 289$
  - **정답:** $100100001_2$ (십진수 289)
 
  - ---

 
**4. Calculate binary 00001101 minus 00000111.**
*(이진수 $00001101$에서 $00000111$을 빼시오.)*

* **십진수 변환을 통한 검증:**
  - $00001101_2 = 8 + 4 + 1 = 13_{10}$
  - $00000111_2 = 4 + 2 + 1 = 7_{10}$
  - $13 - 7 = 6_{10}$

* **이진수 직접 뺄셈 과정 (받아내림):**
  $$\begin{array}{r@{\quad}l}
    00001101 \\
  - 00000111 \\
  \hline
    00000110
  \end{array}$$

* **정답:** $00000110_2$ (십진수 6)

* ---


**5. How many bits are used by each of the following data types?**
*(다음 각 데이터 타입은 몇 비트를 사용하나요?)*

* **a. word:** 16비트 (2바이트)
* **b. doubleword:** 32비트 (4바이트)
* **c. quadword:** 64비트 (8바이트)
* **d. double quadword:** 128비트 (16바이트)

* ---


**6. What is the minimum number of binary bits needed to represent each of the following unsigned decimal integers?**
*(다음 각 부호 없는 십진수를 표현하는 데 필요한 최소한의 이진수 비트 수는 얼마인가요?)*

* **a. 4095**
  - **설명:** $2^{12} - 1 = 4095$이므로 12비트가 필요합니다. ($111111111111_2$)
  - **정답:** 12비트

* **b. 65534**
  - **설명:** 16비트로 표현할 수 있는 최댓값은 $65535$($2^{16}-1$)이며, $65534$는 이 범위($2^{15} \le 65534 < 2^{16}$)에 포함됩니다.
  - **정답:** 16비트

* **c. 42319**
  - **설명:** $32768(2^{15}) \le 42319 < 65536(2^{16})$ 이므로 16비트가 필요합니다.
  - **정답:** 16비트
 
  - ---


**7. What is the hexadecimal representation of each of the following binary numbers?**
*(다음 각 이진수의 십육진수 표현은 무엇인가요?)*

* **a. 0011 0101 1101 1010**
  - **4비트씩 변환:** $0011_2 = 3$, $0101_2 = 5$, $1101_2 = D$, $1010_2 = A$
  - **정답:** $35DA$ (또는 $0\text{x}35DA$)

* **b. 1100 1110 1010 0011**
  - **4비트씩 변환:** $1100_2 = C$, $1110_2 = E$, $1010_2 = A$, $0011_2 = 3$
  - **정답:** $CEA3$ (또는 $0\text{x}CEA3$)

* **c. 1111 1110 1101 1011**
  - **4비트씩 변환:** $1111_2 = F$, $1110_2 = E$, $1101_2 = D$, $1011_2 = B$
  - **정답:** $FEDB$ (또는 $0\text{xFEDB}$)
 
  - ---


**What is the binary representation of the following hexadecimal numbers?**
*(다음 각 십육진수의 이진수 표현은 무엇인가요?)*

* **a. 0126F9D4**
  - **각 자리 변환:** $0 \rightarrow 0000$, $1 \rightarrow 0001$, $2 \rightarrow 0010$, $6 \rightarrow 0110$, $F \rightarrow 1111$, $9 \rightarrow 1001$, $D \rightarrow 1101$, $4 \rightarrow 0100$
  - **정답:** `0000 0001 0010 0110 1111 1001 1101 0100`

* **b. 6ACDFA95**
  - **각 자리 변환:** $6 \rightarrow 0110$, $A \rightarrow 1010$, $C \rightarrow 1100$, $D \rightarrow 1101$, $F \rightarrow 1111$, $A \rightarrow 1010$, $9 \rightarrow 1001$, $5 \rightarrow 0101$
  - **정답:** `0110 1010 1100 1101 1111 1010 1001 0101`

* **c. F69BDC2A**
  - **각 자리 변환:** $F \rightarrow 1111$, $6 \rightarrow 0110$, $9 \rightarrow 1001$, $B \rightarrow 1011$, $D \rightarrow 1101$, $C \rightarrow 1100$, $2 \rightarrow 0010$, $A \rightarrow 1010$
  - **정답:** `1111 0110 1001 1011 1101 1100 0010 1010`
 
  - ---


**9. What is the unsigned decimal representation of each of the following hexadecimal integers?**
*(다음 각 십육진수의 부호 없는 십진수 표현은 무엇인가요?)*

* **a. 3A**
  - **계산식:** $(3 \times 16^1) + (10 \times 16^0) = 48 + 10$
  - **정답:** $58$

* **b. 1BF**
  - **계산식:** $(1 \times 16^2) + (11 \times 16^1) + (15 \times 16^0) = 256 + 176 + 15$
  - **정답:** $447$

* **c. 1001**
  - **계산식:** $(1 \times 16^3) + (0 \times 16^2) + (0 \times 16^1) + (1 \times 16^0) = 4096 + 0 + 0 + 1$
  - **정답:** $4097$
 
  - ---


**10. What is the unsigned decimal representation of each of the following hexadecimal integers?**
*(다음 각 십육진수의 부호 없는 십진수 표현은 무엇인가요?)*

* **a. 62**
  - **계산식:** $(6 \times 16^1) + (2 \times 16^0) = 96 + 2$
  - **정답:** $98$

* **b. 4B3**
  - **계산식:** $(4 \times 16^2) + (11 \times 16^1) + (3 \times 16^0) = 1024 + 176 + 3$
  - **정답:** $1203$

* **c. 29F**
  - **계산식:** $(2 \times 16^2) + (9 \times 16^1) + (15 \times 16^0) = 512 + 144 + 15$
  - **정답:** $671$
 
  - ---


**11. What is the 16-bit hexadecimal representation of each of the following signed decimal integers?**
*(다음 각 부호 있는 십진수의 16비트 십육진수 표현은 무엇인가요?)*

* **a. -24**
  - **과정:** 양수 24의 이진수($0000\ 0000\ 0001\ 1000$)의 2의 보수($1111\ 1111\ 1110\ 1000$)를 구한 뒤 십육진수로 변환합니다.
  - **정답:** `FFE8`

* **b. -331**
  - **과정:** 양수 331의 이진수($0000\ 0001\ 0100\ 1011$)의 2의 보수($1111\ 1110\ 1011\ 0101$)를 구한 뒤 십육진수로 변환합니다.
  - **정답:** `FEB5`
 
  - ---


**12. What is the 16-bit hexadecimal representation of each of the following signed decimal integers?**
*(다음 각 부호 있는 십진수의 16비트 십육진수 표현은 무엇인가요?)*

* **a. -21**
  - **과정:** 양수 21의 이진수($0000\ 0000\ 0001\ 0101$)의 2의 보수($1111\ 1111\ 1110\ 1011$)를 구한 뒤 십육진수로 변환합니다.
  - **정답:** `FFEB`

* **b. -45**
  - **과정:** 양수 45의 이진수($0000\ 0000\ 0010\ 1101$)의 2의 보수($1111\ 1111\ 1101\ 0011$)를 구한 뒤 십육진수로 변환합니다.
  - **정답:** `FFD3`
 
---
**13. The following 16-bit hexadecimal numbers represent signed integers. Convert each to decimal.**
*(다음 16비트 십육진수는 부호 있는 정수를 나타냅니다. 각각 십진수로 변환하세요.)*

* **a. 6BF9**
  - **부호 및 계산:** MSB가 0이므로 양수입니다. $(6 \times 16^3) + (11 \times 16^2) + (15 \times 16^1) + (9 \times 16^0) = 24576 + 2816 + 240 + 9$
  - **정답:** $27641$

* **b. C123**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 부호 없는 값($49443$)에서 $65536$을 빼서 구합니다. ($49443 - 65536$)
  - **정답:** $-16093$
 
 ---
 
**14. The following 16-bit hexadecimal numbers represent signed integers. Convert each to decimal.**
*(다음 16비트 십육진수는 부호 있는 정수를 나타냅니다. 각각 십진수로 변환하세요.)*

* **a. 4CD2**
  - **부호 및 계산:** MSB가 0이므로 양수입니다. $(4 \times 16^3) + (12 \times 16^2) + (13 \times 16^1) + (2 \times 16^0) = 16384 + 3072 + 208 + 2$
  - **정답:** $19666$

* **b. 8230**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 부호 없는 값($33328$)에서 $65536$을 빼서 구합니다. ($33328 - 65536$)
  - **정답:** $-32208$
 
  - ---


**15. What is the decimal representation of each of the following signed binary numbers?**
*(다음 각 부호 있는 이진수의 십진수 표현은 무엇인가요?)*

* **a. 10110101**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 2의 보수를 취해 절댓값을 구하면 $75$가 됩니다.
  - **정답:** $-75$

* **b. 00101010**
  - **부호 및 계산:** MSB가 0이므로 양수입니다. $32 + 8 + 2 = 42$
  - **정답:** $42$

* **c. 11110000**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 2의 보수를 취해 절댓값을 구하면 $16$이 됩니다.
  - **정답:** $-16$

  ---


**16. What is the decimal representation of each of the following signed binary numbers?**
*(다음 각 부호 있는 이진수의 십진수 표현은 무엇인가요?)*

* **a. 10000000**
  - **부호 및 계산:** MSB가 1이며 8비트 2의 보수 체계에서 가장 작은 값($-2^7$)을 나타냅니다.
  - **정답:** $-128$

* **b. 11001100**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 2의 보수를 취해 절댓값을 구하면 $52$가 됩니다.
  - **정답:** $-52$

* **c. 10110111**
  - **부호 및 계산:** MSB가 1이므로 음수입니다. 2의 보수를 취해 절댓값을 구하면 $73$이 됩니다.
  - **정답:** $-73$
 
  - ---

**17. What is the 8-bit binary (two’s-complement) representation of each of the following signed decimal integers?**
*(다음 각 부호 있는 십진수의 8비트 2의 보수 이진수 표현은 무엇인가요?)*

* **a. -5**
  - **과정:** 양수 5의 이진수($0000\ 0101$)의 2의 보수를 구합니다.
  - **정답:** `11111011`

* **b. -42**
  - **과정:** 양수 42의 이진수($0010\ 1010$)의 2의 보수를 구합니다.
  - **정답:** `11010110`

* **c. -26**
  - **과정:** 양수 26의 이진수($0001\ 1010$)의 2의 보수를 구합니다.
  - **정답:** `11100110`
 
  - ---


**18. What is the 8-bit binary (two’s-complement) representation of each of the following signed decimal integers?**
*(다음 각 부호 있는 십진수의 8비트 2의 보수 이진수 표현은 무엇인가요?)*

* **a. -72**
  - **과정:** 양수 72의 이진수($0100\ 1000$)의 2의 보수를 구합니다.
  - **정답:** `10111000`

* **b. -98**
  - **과정:** 양수 98의 이진수($0110\ 0010$)의 2의 보수를 구합니다.
  - **정답:** `10011110`

* **c. -26**
  - **과정:** 양수 26의 이진수($0001\ 1010$)의 2의 보수를 구합니다.
  - **정답:** `11100110`
 
  - ---


**19. What is the sum of each pair of hexadecimal integers?**
*(다음 각 십육진수 쌍의 합은 무엇인가요?)*

* **a. 6B4 + 3FE**
  - **과정:** 각 자리의 십육진수 값을 더하고 16이 넘어가면 자리올림을 처리합니다.
  - **정답:** `AB2`

* **b. A49 + 6BD**
  - **과정:** 각 자리의 십육진수 값을 더하고 16이 넘어가면 자리올림을 처리합니다.
  - **정답:** `1106`
 
  - ---

  ### 1.7 Review Questions and Exercises
#### 1.7.1 Short Answer

**20. What is the sum of each pair of hexadecimal integers?**
*(다음 각 십육진수 쌍의 합은 무엇인가요?)*

* **a. 7C4 + 3BE**
  - **과정:** 각 자리의 십육진수 값을 더하고 16이 넘어가면 16을 빼준 뒤 윗자리로 캐리를 보냅니다.
  - **정답:** `B82`

* **b. B69 + 7AD**
  - **과정:** 각 자리의 십육진수 값을 더하고 16이 넘어가면 16을 빼준 뒤 윗자리로 캐리를 보냅니다.
  - **정답:** `1316`
 
  - ---


**21. What are the hexadecimal and decimal representations of the ASCII character capital B?**
*(ASCII 문자 대문자 B의 십육진수 및 십진수 표현은 무엇인가요?)*
* **정답:** 십진수 $66$, 십육진수 `42`

**22. What are the hexadecimal and decimal representations of the ASCII character capital G?**
*(ASCII 문자 대문자 G의 십육진수 및 십진수 표현은 무엇인가요?)*
* **정답:** 십진수 $71$, 십육진수 `47`

**23. Challenge: What is the largest decimal value you can represent, using a 129-bit unsigned integer?**
*(도전 과제: 129비트 부호 없는 정수를 사용하여 표현할 수 있는 가장 큰 십진수 값은 무엇인가요?)*
* **정답:** $2^{129} - 1$

**24. Challenge: What is the largest decimal value you can represent, using a 86-bit signed integer?**
*(도전 과제: 86비트 부호 있는 정수를 사용하여 표현할 수 있는 가장 큰 십진수 값은 무엇인가요?)*
* **정답:** $2^{85} - 1$

* ---


**25. Create a truth table to show all possible inputs and outputs for the boolean function described by ¬(AvB).**
*(부울 함수 $\neg(A \lor B)$에 대한 모든 가능한 입력과 출력을 보여주는 진리표를 작성하세요.)*

| $A$ | $B$ | $A \lor B$ | $\neg(A \lor B)$ |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | **1** |
| 0 | 1 | 1 | **0** |
| 1 | 0 | 1 | **0** |
| 1 | 1 | 1 | **0** |

---


**26. Create a truth table to show all possible inputs and outputs for the boolean function described by ($\neg A \land \neg B$). How would you describe the rightmost column of this table in relation to the table from question number 25? Have you heard of De Morgan’s Theorem?**
*(부울 함수 $(\neg A \land \neg B)$에 대한 가능한 모든 입력과 출력을 보여주는 진리표를 만드세요. 이 진리표의 가장 오른쪽 열을 25번 문제의 진리표와 비교하여 어떻게 설명하시겠습니까? 드 모르간의 법칙에 대해 들어본 적이 있나요?)*

| $A$ | $B$ | $\neg A$ | $\neg B$ | $\neg A \land \neg B$ |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 1 | 1 | **1** |
| 0 | 1 | 1 | 0 | **0** |
| 1 | 0 | 0 | 1 | **0** |
| 1 | 1 | 0 | 0 | **0** |

* **관계:** 25번 문제의 결과($\neg(A \lor B)$)와 **완전히 동일**합니다.
* **드 모르간의 법칙 (De Morgan’s Theorem):** $\neg(A \lor B) \equiv \neg A \land \neg B$ 관계를 증명합니다.

---


**27. If a boolean function has four inputs, how many rows are required for its truth table?**
*(부울 함수에 4개의 입력이 있는 경우, 진리표에 몇 개의 행이 필요합니까?)*
* **정답:** 16개 ($2^4 = 16$)

**28. How many selector bits are required for a four-input multiplexer?**
*(4개의 입력을 받는 멀티플렉서에는 몇 개의 선택 비트가 필요합니까?)*
* **정답:** 2개 ($2^2 = 4$)

* ---

> **9. Devise a way of subtracting unsigned binary integers. Test your technique by subtracting binary 00000101 from binary 10001000, producing 10000011. Test your technique with at least two other sets of integers, in which a smaller value is always subtracted from a larger one.**
>
> *(9. 부호 없는 이진 정수의 뺄셈 방법을 고안하시오. 이진수 10001000에서 00000101을 빼서 10000011이 산출되는지 당신의 기법을 검증하시오. 항상 작은 값이 큰 값에서 빼지는 조건으로 최소 두 가지 다른 정수 세트를 사용하여 당신의 기법을 테스트하시오.)*

---

## 1. 이진수 뺄셈 기법 (Subtraction Technique)

**받아내림(Borrow) 세로셈 연산 기법**
- 자릿수(오른쪽 LSB부터 왼쪽 MSB까지)를 맞춰 정렬한 후, 오른쪽에서 왼쪽 방향으로 각 비트별 뺄셈을 진행합니다.
- 기본 연산 규칙:
  - $0 - 0 = 0$
  - $1 - 0 = 1$
  - $1 - 1 = 0$
  - $0 - 1$ 연산 시: 상위 비트(왼쪽에서 가장 가까운 `1`)로부터 $2(10_2)$를 받아내림(Borrow)해옵니다. 이때 빌려준 비트는 `0`이 되고, 그 사이 위치한 `0` 비트들은 모두 `1`로 전환됩니다.

---

## 2. 기본 예시 검증 (Test Case 1)

**연산식:** $10001000_2 - 00000101_2 = 10000011_2$

### 1) 이진수 세로셈 연산 과정
```text
  1000 1000
- 0000 0101
-----------
  1000 0011
```

### 2) 십진수 변환을 통한 검증
- **피감수(빼지는 수):** $10001000_2 = 128 + 8 = 136_{10}$
- **감수(빼는 수):** $00000101_2 = 4 + 1 = 5_{10}$
- **십진수 계산:** $136 - 5 = 131_{10}$
- **이진수 결과 변환:** $10000011_2 = 128 + 2 + 1 = 131_{10}$ **(일치)**

---

## 3. 추가 테스트 케이스 1 (Test Case 2)

**연산식:** $11001100_2 - 00110011_2 = 10011001_2$

### 1) 이진수 세로셈 연산 과정
```text
  1100 1100
- 0011 0011
-----------
  1001 1001
```

### 2) 십진수 변환을 통한 검증
- **피감수(큰 수):** $11001100_2 = 128 + 64 + 8 + 4 = 204_{10}$
- **감수(작은 수):** $00110011_2 = 32 + 16 + 2 + 1 = 51_{10}$
- **십진수 계산:** $204 - 51 = 153_{10}$
- **이진수 결과 변환:** $10011001_2 = 128 + 16 + 8 + 1 = 153_{10}$ **(일치)**

---

## 4. 추가 테스트 케이스 2 (Test Case 3)

**연산식:** $10101010_2 - 00001111_2 = 10011011_2$

### 1) 이진수 세로셈 연산 과정
```text
  1010 1010
- 0000 1111
-----------
  1001 1011
```

### 2) 십진수 변환을 통한 검증
- **피감수(큰 수):** $10101010_2 = 128 + 32 + 8 + 2 = 170_{10}$
- **감수(작은 수):** $00001111_2 = 8 + 4 + 2 + 1 = 15_{10}$
- **십진수 계산:** $170 - 15 = 155_{10}$
- **이진수 결과 변환:** $10011011_2 = 128 + 16 + 8 + 2 + 1 = 155_{10}$ **(일치)**

---

## 5. 최종 결과 요약 표

| 구분 | 피감수 (이진수 / 십진수) | 감수 (이진수 / 십진수) | 연산 결과 (이진수 / 십진수) | 검증 |
| :--- | :--- | :--- | :--- | :---: |
| **기본 문제** | $10001000_2$ ($136$) | $00000101_2$ ($5$) | $10000011_2$ ($131$) | 성공 |
| **추가 테스트 1** | $11001100_2$ ($204$) | $00110011_2$ ($51$) | $10011001_2$ ($153$) | 성공 |
| **추가 테스트 2** | $10101010_2$ ($170$) | $00001111_2$ ($15$) | $10011011_2$ ($155$) | 성공 |
