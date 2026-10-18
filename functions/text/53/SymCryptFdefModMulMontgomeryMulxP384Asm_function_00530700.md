# SymCryptFdefModMulMontgomeryMulxP384Asm

- RVA: `0x00530700`–`0x00530C71` (길이 `1,393` bytes)
- VA: `0x0000000140530700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C34F8`
- 디코드: `294`개 명령, `1,393/1,393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefModSetPostMontgomeryMulxP384](SymCryptFdefModSetPostMontgomeryMulxP384_function_00535160.md) at `0x0053516E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00530700  48 56                           push rsi
00530702  57                              push rdi
00530703  55                              push rbp
00530704  53                              push rbx
00530705  41 54                           push r12
00530707  41 55                           push r13
00530709  41 56                           push r14
0053070B  41 57                           push r15
0053070D  4C 8B D2                        mov r10, rdx
00530710  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00530715  4D 33 FF                        xor r15, r15
00530718  49 8B 12                        mov rdx, qword ptr [r10]
0053071B  C4 C2 CB F6 38                  mulx rdi, rsi, qword ptr [r8]
00530720  C4 C2 FB F6 68 08               mulx rbp, rax, qword ptr [r8 + 8]
00530726  48 13 F8                        adc rdi, rax
00530729  C4 C2 FB F6 58 10               mulx rbx, rax, qword ptr [r8 + 0x10]
0053072F  48 13 E8                        adc rbp, rax
00530732  C4 42 FB F6 60 18               mulx r12, rax, qword ptr [r8 + 0x18]
00530738  48 13 D8                        adc rbx, rax
0053073B  C4 42 FB F6 68 20               mulx r13, rax, qword ptr [r8 + 0x20]
00530741  4C 13 E0                        adc r12, rax
00530744  C4 42 FB F6 70 28               mulx r14, rax, qword ptr [r8 + 0x28]
0053074A  4C 13 E8                        adc r13, rax
0053074D  4D 13 F7                        adc r14, r15
00530750  48 81 C1 80 00 00 00            add rcx, 0x80
00530757  4D 33 C9                        xor r9, r9
0053075A  48 8B D6                        mov rdx, rsi
0053075D  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
00530762  49 83 C1 FF                     add r9, -1
00530766  48 1B DA                        sbb rbx, rdx
00530769  4D 1B C9                        sbb r9, r9
0053076C  48 33 C0                        xor rax, rax
0053076F  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
00530774  66 48 0F 38 F6 F0               adcx rsi, rax
0053077A  F3 49 0F 38 F6 FB               adox rdi, r11
00530780  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530786  66 48 0F 38 F6 F8               adcx rdi, rax
0053078C  F3 49 0F 38 F6 EB               adox rbp, r11
00530792  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
00530798  66 48 0F 38 F6 E8               adcx rbp, rax
0053079E  F3 49 0F 38 F6 DB               adox rbx, r11
005307A4  66 48 0F 38 F6 DE               adcx rbx, rsi
005307AA  F3 4C 0F 38 F6 CE               adox r9, rsi
005307B0  4C 13 CE                        adc r9, rsi
005307B3  4C 03 F2                        add r14, rdx
005307B6  4C 13 FE                        adc r15, rsi
005307B9  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
005307BD  48 33 F6                        xor rsi, rsi
005307C0  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
005307C5  66 48 0F 38 F6 F8               adcx rdi, rax
005307CB  F3 49 0F 38 F6 EB               adox rbp, r11
005307D1  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
005307D7  66 48 0F 38 F6 E8               adcx rbp, rax
005307DD  F3 49 0F 38 F6 DB               adox rbx, r11
005307E3  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
005307E9  66 48 0F 38 F6 D8               adcx rbx, rax
005307EF  F3 4D 0F 38 F6 E3               adox r12, r11
005307F5  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
005307FB  66 4C 0F 38 F6 E0               adcx r12, rax
00530801  F3 4D 0F 38 F6 EB               adox r13, r11
00530807  C4 42 FB F6 58 20               mulx r11, rax, qword ptr [r8 + 0x20]
0053080D  66 4C 0F 38 F6 E8               adcx r13, rax
00530813  F3 4D 0F 38 F6 F3               adox r14, r11
00530819  C4 42 FB F6 58 28               mulx r11, rax, qword ptr [r8 + 0x28]
0053081F  66 4C 0F 38 F6 F0               adcx r14, rax
00530825  F3 4C 0F 38 F6 FE               adox r15, rsi
0053082B  4D 13 FB                        adc r15, r11
0053082E  48 13 F6                        adc rsi, rsi
00530831  48 8B D7                        mov rdx, rdi
00530834  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
00530839  49 83 C1 FF                     add r9, -1
0053083D  4C 1B E2                        sbb r12, rdx
00530840  4D 1B C9                        sbb r9, r9
00530843  48 33 C0                        xor rax, rax
00530846  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
0053084B  66 48 0F 38 F6 F8               adcx rdi, rax
00530851  F3 49 0F 38 F6 EB               adox rbp, r11
00530857  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
0053085D  66 48 0F 38 F6 E8               adcx rbp, rax
00530863  F3 49 0F 38 F6 DB               adox rbx, r11
00530869  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
0053086F  66 48 0F 38 F6 D8               adcx rbx, rax
00530875  F3 4D 0F 38 F6 E3               adox r12, r11
0053087B  66 4C 0F 38 F6 E7               adcx r12, rdi
00530881  F3 4C 0F 38 F6 CF               adox r9, rdi
00530887  4C 13 CF                        adc r9, rdi
0053088A  4C 03 FA                        add r15, rdx
0053088D  48 13 F7                        adc rsi, rdi
00530890  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
00530894  48 33 FF                        xor rdi, rdi
00530897  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
0053089C  66 48 0F 38 F6 E8               adcx rbp, rax
005308A2  F3 49 0F 38 F6 DB               adox rbx, r11
005308A8  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
005308AE  66 48 0F 38 F6 D8               adcx rbx, rax
005308B4  F3 4D 0F 38 F6 E3               adox r12, r11
005308BA  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
005308C0  66 4C 0F 38 F6 E0               adcx r12, rax
005308C6  F3 4D 0F 38 F6 EB               adox r13, r11
005308CC  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
005308D2  66 4C 0F 38 F6 E8               adcx r13, rax
005308D8  F3 4D 0F 38 F6 F3               adox r14, r11
005308DE  C4 42 FB F6 58 20               mulx r11, rax, qword ptr [r8 + 0x20]
005308E4  66 4C 0F 38 F6 F0               adcx r14, rax
005308EA  F3 4D 0F 38 F6 FB               adox r15, r11
005308F0  C4 42 FB F6 58 28               mulx r11, rax, qword ptr [r8 + 0x28]
005308F6  66 4C 0F 38 F6 F8               adcx r15, rax
005308FC  F3 48 0F 38 F6 F7               adox rsi, rdi
00530902  49 13 F3                        adc rsi, r11
00530905  48 13 FF                        adc rdi, rdi
00530908  48 8B D5                        mov rdx, rbp
0053090B  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
00530910  49 83 C1 FF                     add r9, -1
00530914  4C 1B EA                        sbb r13, rdx
00530917  4D 1B C9                        sbb r9, r9
0053091A  48 33 C0                        xor rax, rax
0053091D  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
00530922  66 48 0F 38 F6 E8               adcx rbp, rax
00530928  F3 49 0F 38 F6 DB               adox rbx, r11
0053092E  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530934  66 48 0F 38 F6 D8               adcx rbx, rax
0053093A  F3 4D 0F 38 F6 E3               adox r12, r11
00530940  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
00530946  66 4C 0F 38 F6 E0               adcx r12, rax
0053094C  F3 4D 0F 38 F6 EB               adox r13, r11
00530952  66 4C 0F 38 F6 ED               adcx r13, rbp
00530958  F3 4C 0F 38 F6 CD               adox r9, rbp
0053095E  4C 13 CD                        adc r9, rbp
00530961  48 03 F2                        add rsi, rdx
00530964  48 13 FD                        adc rdi, rbp
00530967  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
0053096B  48 33 ED                        xor rbp, rbp
0053096E  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
00530973  66 48 0F 38 F6 D8               adcx rbx, rax
00530979  F3 4D 0F 38 F6 E3               adox r12, r11
0053097F  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
00530985  66 4C 0F 38 F6 E0               adcx r12, rax
0053098B  F3 4D 0F 38 F6 EB               adox r13, r11
00530991  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
00530997  66 4C 0F 38 F6 E8               adcx r13, rax
0053099D  F3 4D 0F 38 F6 F3               adox r14, r11
005309A3  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
005309A9  66 4C 0F 38 F6 F0               adcx r14, rax
005309AF  F3 4D 0F 38 F6 FB               adox r15, r11
005309B5  C4 42 FB F6 58 20               mulx r11, rax, qword ptr [r8 + 0x20]
005309BB  66 4C 0F 38 F6 F8               adcx r15, rax
005309C1  F3 49 0F 38 F6 F3               adox rsi, r11
005309C7  C4 42 FB F6 58 28               mulx r11, rax, qword ptr [r8 + 0x28]
005309CD  66 48 0F 38 F6 F0               adcx rsi, rax
005309D3  F3 48 0F 38 F6 FD               adox rdi, rbp
005309D9  49 13 FB                        adc rdi, r11
005309DC  48 13 ED                        adc rbp, rbp
005309DF  48 8B D3                        mov rdx, rbx
005309E2  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
005309E7  49 83 C1 FF                     add r9, -1
005309EB  4C 1B F2                        sbb r14, rdx
005309EE  4D 1B C9                        sbb r9, r9
005309F1  48 33 C0                        xor rax, rax
005309F4  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
005309F9  66 48 0F 38 F6 D8               adcx rbx, rax
005309FF  F3 4D 0F 38 F6 E3               adox r12, r11
00530A05  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530A0B  66 4C 0F 38 F6 E0               adcx r12, rax
00530A11  F3 4D 0F 38 F6 EB               adox r13, r11
00530A17  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
00530A1D  66 4C 0F 38 F6 E8               adcx r13, rax
00530A23  F3 4D 0F 38 F6 F3               adox r14, r11
00530A29  66 4C 0F 38 F6 F3               adcx r14, rbx
00530A2F  F3 4C 0F 38 F6 CB               adox r9, rbx
00530A35  4C 13 CB                        adc r9, rbx
00530A38  48 03 FA                        add rdi, rdx
00530A3B  48 13 EB                        adc rbp, rbx
00530A3E  49 8B 52 20                     mov rdx, qword ptr [r10 + 0x20]
00530A42  48 33 DB                        xor rbx, rbx
00530A45  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
00530A4A  66 4C 0F 38 F6 E0               adcx r12, rax
00530A50  F3 4D 0F 38 F6 EB               adox r13, r11
00530A56  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
00530A5C  66 4C 0F 38 F6 E8               adcx r13, rax
00530A62  F3 4D 0F 38 F6 F3               adox r14, r11
00530A68  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
00530A6E  66 4C 0F 38 F6 F0               adcx r14, rax
00530A74  F3 4D 0F 38 F6 FB               adox r15, r11
00530A7A  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
00530A80  66 4C 0F 38 F6 F8               adcx r15, rax
00530A86  F3 49 0F 38 F6 F3               adox rsi, r11
00530A8C  C4 42 FB F6 58 20               mulx r11, rax, qword ptr [r8 + 0x20]
00530A92  66 48 0F 38 F6 F0               adcx rsi, rax
00530A98  F3 49 0F 38 F6 FB               adox rdi, r11
00530A9E  C4 42 FB F6 58 28               mulx r11, rax, qword ptr [r8 + 0x28]
00530AA4  66 48 0F 38 F6 F8               adcx rdi, rax
00530AAA  F3 48 0F 38 F6 EB               adox rbp, rbx
00530AB0  49 13 EB                        adc rbp, r11
00530AB3  48 13 DB                        adc rbx, rbx
00530AB6  49 8B D4                        mov rdx, r12
00530AB9  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
00530ABE  49 83 C1 FF                     add r9, -1
00530AC2  4C 1B FA                        sbb r15, rdx
00530AC5  4D 1B C9                        sbb r9, r9
00530AC8  48 33 C0                        xor rax, rax
00530ACB  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
00530AD0  66 4C 0F 38 F6 E0               adcx r12, rax
00530AD6  F3 4D 0F 38 F6 EB               adox r13, r11
00530ADC  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530AE2  66 4C 0F 38 F6 E8               adcx r13, rax
00530AE8  F3 4D 0F 38 F6 F3               adox r14, r11
00530AEE  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
00530AF4  66 4C 0F 38 F6 F0               adcx r14, rax
00530AFA  F3 4D 0F 38 F6 FB               adox r15, r11
00530B00  66 4D 0F 38 F6 FC               adcx r15, r12
00530B06  F3 4D 0F 38 F6 CC               adox r9, r12
00530B0C  4D 13 CC                        adc r9, r12
00530B0F  48 03 EA                        add rbp, rdx
00530B12  49 13 DC                        adc rbx, r12
00530B15  49 8B 52 28                     mov rdx, qword ptr [r10 + 0x28]
00530B19  4D 33 E4                        xor r12, r12
00530B1C  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
00530B21  66 4C 0F 38 F6 E8               adcx r13, rax
00530B27  F3 4D 0F 38 F6 F3               adox r14, r11
00530B2D  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
00530B33  66 4C 0F 38 F6 F0               adcx r14, rax
00530B39  F3 4D 0F 38 F6 FB               adox r15, r11
00530B3F  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
00530B45  66 4C 0F 38 F6 F8               adcx r15, rax
00530B4B  F3 49 0F 38 F6 F3               adox rsi, r11
00530B51  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
00530B57  66 48 0F 38 F6 F0               adcx rsi, rax
00530B5D  F3 49 0F 38 F6 FB               adox rdi, r11
00530B63  C4 42 FB F6 58 20               mulx r11, rax, qword ptr [r8 + 0x20]
00530B69  66 48 0F 38 F6 F8               adcx rdi, rax
00530B6F  F3 49 0F 38 F6 EB               adox rbp, r11
00530B75  C4 42 FB F6 58 28               mulx r11, rax, qword ptr [r8 + 0x28]
00530B7B  66 48 0F 38 F6 E8               adcx rbp, rax
00530B81  F3 49 0F 38 F6 DC               adox rbx, r12
00530B87  49 13 DB                        adc rbx, r11
00530B8A  4D 13 E4                        adc r12, r12
00530B8D  49 8B D5                        mov rdx, r13
00530B90  48 0F AF 51 98                  imul rdx, qword ptr [rcx - 0x68]
00530B95  49 83 C1 FF                     add r9, -1
00530B99  48 1B F2                        sbb rsi, rdx
00530B9C  4D 1B C9                        sbb r9, r9
00530B9F  48 33 C0                        xor rax, rax
00530BA2  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
00530BA7  66 4C 0F 38 F6 E8               adcx r13, rax
00530BAD  F3 4D 0F 38 F6 F3               adox r14, r11
00530BB3  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530BB9  66 4C 0F 38 F6 F0               adcx r14, rax
00530BBF  F3 4D 0F 38 F6 FB               adox r15, r11
00530BC5  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
00530BCB  66 4C 0F 38 F6 F8               adcx r15, rax
00530BD1  F3 49 0F 38 F6 F3               adox rsi, r11
00530BD7  66 49 0F 38 F6 F5               adcx rsi, r13
00530BDD  F3 4D 0F 38 F6 CD               adox r9, r13
00530BE3  4D 13 CD                        adc r9, r13
00530BE6  48 03 DA                        add rbx, rdx
00530BE9  4D 13 E5                        adc r12, r13
00530BEC  48 33 C0                        xor rax, rax
00530BEF  F3 49 0F 38 F6 F9               adox rdi, r9
00530BF5  F3 49 0F 38 F6 E9               adox rbp, r9
00530BFB  F3 49 0F 38 F6 D9               adox rbx, r9
00530C01  F3 4D 0F 38 F6 E1               adox r12, r9
00530C07  4C 8B 91 80 00 00 00            mov r10, qword ptr [rcx + 0x80]
00530C0E  4D 03 D6                        add r10, r14
00530C11  4C 8B 01                        mov r8, qword ptr [rcx]
00530C14  4D 13 C7                        adc r8, r15
00530C17  49 C7 C3 01 00 00 00            mov r11, 1
00530C1E  4C 13 DE                        adc r11, rsi
00530C21  48 8B C8                        mov rcx, rax
00530C24  48 13 C7                        adc rax, rdi
00530C27  48 13 CD                        adc rcx, rbp
00530C2A  4C 13 EB                        adc r13, rbx
00530C2D  4D 13 E4                        adc r12, r12
00530C30  4D 0F 45 F2                     cmovne r14, r10
00530C34  4D 0F 45 F8                     cmovne r15, r8
00530C38  49 0F 45 F3                     cmovne rsi, r11
00530C3C  48 0F 45 F8                     cmovne rdi, rax
00530C40  48 0F 45 E9                     cmovne rbp, rcx
00530C44  49 0F 45 DD                     cmovne rbx, r13
00530C48  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00530C4D  4D 89 31                        mov qword ptr [r9], r14
00530C50  4D 89 79 08                     mov qword ptr [r9 + 8], r15
00530C54  49 89 71 10                     mov qword ptr [r9 + 0x10], rsi
00530C58  49 89 79 18                     mov qword ptr [r9 + 0x18], rdi
00530C5C  49 89 69 20                     mov qword ptr [r9 + 0x20], rbp
00530C60  49 89 59 28                     mov qword ptr [r9 + 0x28], rbx
00530C64  41 5F                           pop r15
00530C66  41 5E                           pop r14
00530C68  41 5D                           pop r13
00530C6A  41 5C                           pop r12
00530C6C  5B                              pop rbx
00530C6D  5D                              pop rbp
00530C6E  5F                              pop rdi
00530C6F  5E                              pop rsi
00530C70  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModMulMontgomeryMulxP384Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a4;
    v_r15 = 0;
    a1 = (a1) + (128);
    a4 = 0;
    a2 = (v_rsi) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_r14 = (v_r14) + (a2);
    v_rsi = 0;
    a2 = (v_rdi) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_r15 = (v_r15) + (a2);
    v_rdi = 0;
    a2 = (v_rbp) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_rsi = (v_rsi) + (a2);
    v_rbp = 0;
    a2 = (v_rbx) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_rdi = (v_rdi) + (a2);
    v_rbx = 0;
    a2 = (v_r12) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_rbp = (v_rbp) + (a2);
    v_r12 = 0;
    a2 = (v_r13) * (*(unsigned __int64 *)(a1 - 104));
    a4 = (a4) + (-1);
    result = 0;
    v_rbx = (v_rbx) + (a2);
    result = 0;
    v_r10 = (*(unsigned __int64 *)(a1 + 128)) + (v_r14);
    if (condition_is_not_equal) {
        v_r14 = v_r10;
        v_r15 = *(unsigned __int64 *)(a1);
        v_rsi = 1;
        v_rdi = 0;
        v_rbp = 0;
        v_rbx = v_r13;
    }
    *(unsigned __int64 *)(v_stack_p8) = v_r14;
    *(unsigned __int64 *)(v_stack_p8 + 8) = v_r15;
    *(unsigned __int64 *)(v_stack_p8 + 16) = v_rsi;
    *(unsigned __int64 *)(v_stack_p8 + 24) = v_rdi;
    *(unsigned __int64 *)(v_stack_p8 + 32) = v_rbp;
    *(unsigned __int64 *)(v_stack_p8 + 40) = v_rbx;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModMulMontgomeryMulxP384Asm(void *Arg1, void *Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg4;
    local_r15 = 0;
    Arg1 = (Arg1) + (128);
    Arg4 = 0;
    Arg2 = (local_rsi) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_r14 = (local_r14) + (Arg2);
    local_rsi = 0;
    Arg2 = (local_rdi) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_r15 = (local_r15) + (Arg2);
    local_rdi = 0;
    Arg2 = (local_rbp) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_rsi = (local_rsi) + (Arg2);
    local_rbp = 0;
    Arg2 = (local_rbx) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_rdi = (local_rdi) + (Arg2);
    local_rbx = 0;
    Arg2 = (local_r12) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_rbp = (local_rbp) + (Arg2);
    local_r12 = 0;
    Arg2 = (local_r13) * (*(uint64_t *)(arg1 - 0x68));
    Arg4 = (Arg4) + (-1);
    result = 0;
    local_rbx = (local_rbx) + (Arg2);
    result = 0;
    local_r10 = (*(uint64_t *)(arg1 + 0x80)) + (local_r14);
    if (condition_is_not_equal) {
        local_r14 = local_r10;
        local_r15 = *(uint64_t *)(arg1);
        local_rsi = 1;
        local_rdi = 0;
        local_rbp = 0;
        local_rbx = local_r13;
    }
    *(uint64_t *)(v_stack_p8) = local_r14;
    *(uint64_t *)(v_stack_p8 + 0x8) = local_r15;
    *(uint64_t *)(v_stack_p8 + 0x10) = local_rsi;
    *(uint64_t *)(v_stack_p8 + 0x18) = local_rdi;
    *(uint64_t *)(v_stack_p8 + 0x20) = local_rbp;
    *(uint64_t *)(v_stack_p8 + 0x28) = local_rbx;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x68` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00530700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00530700[BB_00530700]
```
