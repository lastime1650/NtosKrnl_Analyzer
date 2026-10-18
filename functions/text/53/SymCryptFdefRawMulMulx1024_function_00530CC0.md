# SymCryptFdefRawMulMulx1024

- RVA: `0x00530CC0`–`0x0053234F` (길이 `5,775` bytes)
- VA: `0x0000000140530CC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3530`
- 디코드: `1,028`개 명령, `5,775/5,775` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefModMulMontgomeryMulx1024](SymCryptFdefModMulMontgomeryMulx1024_function_00534F20.md) at `0x00534F45`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00530CC0  48 56                           push rsi
00530CC2  57                              push rdi
00530CC3  55                              push rbp
00530CC4  53                              push rbx
00530CC5  41 54                           push r12
00530CC7  41 55                           push r13
00530CC9  41 56                           push r14
00530CCB  4C 8B D2                        mov r10, rdx
00530CCE  0F 57 C0                        xorps xmm0, xmm0
00530CD1  41 0F 29 01                     movaps xmmword ptr [r9], xmm0
00530CD5  41 0F 29 41 10                  movaps xmmword ptr [r9 + 0x10], xmm0
00530CDA  41 0F 29 41 20                  movaps xmmword ptr [r9 + 0x20], xmm0
00530CDF  41 0F 29 41 30                  movaps xmmword ptr [r9 + 0x30], xmm0
00530CE4  41 0F 29 41 40                  movaps xmmword ptr [r9 + 0x40], xmm0
00530CE9  41 0F 29 41 50                  movaps xmmword ptr [r9 + 0x50], xmm0
00530CEE  41 0F 29 41 60                  movaps xmmword ptr [r9 + 0x60], xmm0
00530CF3  41 0F 29 41 70                  movaps xmmword ptr [r9 + 0x70], xmm0
00530CF8  4D 33 DB                        xor r11, r11
00530CFB  48 33 F6                        xor rsi, rsi
00530CFE  48 33 FF                        xor rdi, rdi
00530D01  48 33 ED                        xor rbp, rbp
00530D04  48 33 DB                        xor rbx, rbx
00530D07  4D 33 E4                        xor r12, r12
00530D0A  4D 33 ED                        xor r13, r13
00530D0D  4D 33 F6                        xor r14, r14
00530D10  48 33 C0                        xor rax, rax
00530D13  49 8B 12                        mov rdx, qword ptr [r10]
00530D16  F3 4D 0F 38 F6 19               adox r11, qword ptr [r9]
00530D1C  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00530D21  66 4C 0F 38 F6 D8               adcx r11, rax
00530D27  F3 49 0F 38 F6 F0               adox rsi, r8
00530D2D  4D 89 19                        mov qword ptr [r9], r11
00530D30  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00530D36  66 48 0F 38 F6 F0               adcx rsi, rax
00530D3C  F3 49 0F 38 F6 F8               adox rdi, r8
00530D42  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00530D48  66 48 0F 38 F6 F8               adcx rdi, rax
00530D4E  F3 49 0F 38 F6 E8               adox rbp, r8
00530D54  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00530D5A  66 48 0F 38 F6 E8               adcx rbp, rax
00530D60  F3 49 0F 38 F6 D8               adox rbx, r8
00530D66  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00530D6C  66 48 0F 38 F6 D8               adcx rbx, rax
00530D72  F3 4D 0F 38 F6 E0               adox r12, r8
00530D78  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00530D7E  66 4C 0F 38 F6 E0               adcx r12, rax
00530D84  F3 4D 0F 38 F6 E8               adox r13, r8
00530D8A  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00530D90  66 4C 0F 38 F6 E8               adcx r13, rax
00530D96  F3 4D 0F 38 F6 F0               adox r14, r8
00530D9C  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00530DA2  66 4C 0F 38 F6 F0               adcx r14, rax
00530DA8  49 C7 C3 00 00 00 00            mov r11, 0
00530DAF  F3 4D 0F 38 F6 DB               adox r11, r11
00530DB5  66 4D 0F 38 F6 D8               adcx r11, r8
00530DBB  48 33 C0                        xor rax, rax
00530DBE  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
00530DC2  F3 49 0F 38 F6 71 08            adox rsi, qword ptr [r9 + 8]
00530DC9  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00530DCE  66 48 0F 38 F6 F0               adcx rsi, rax
00530DD4  F3 49 0F 38 F6 F8               adox rdi, r8
00530DDA  49 89 71 08                     mov qword ptr [r9 + 8], rsi
00530DDE  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00530DE4  66 48 0F 38 F6 F8               adcx rdi, rax
00530DEA  F3 49 0F 38 F6 E8               adox rbp, r8
00530DF0  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00530DF6  66 48 0F 38 F6 E8               adcx rbp, rax
00530DFC  F3 49 0F 38 F6 D8               adox rbx, r8
00530E02  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00530E08  66 48 0F 38 F6 D8               adcx rbx, rax
00530E0E  F3 4D 0F 38 F6 E0               adox r12, r8
00530E14  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00530E1A  66 4C 0F 38 F6 E0               adcx r12, rax
00530E20  F3 4D 0F 38 F6 E8               adox r13, r8
00530E26  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00530E2C  66 4C 0F 38 F6 E8               adcx r13, rax
00530E32  F3 4D 0F 38 F6 F0               adox r14, r8
00530E38  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00530E3E  66 4C 0F 38 F6 F0               adcx r14, rax
00530E44  F3 4D 0F 38 F6 D8               adox r11, r8
00530E4A  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00530E50  66 4C 0F 38 F6 D8               adcx r11, rax
00530E56  48 C7 C6 00 00 00 00            mov rsi, 0
00530E5D  F3 48 0F 38 F6 F6               adox rsi, rsi
00530E63  66 49 0F 38 F6 F0               adcx rsi, r8
00530E69  48 33 C0                        xor rax, rax
00530E6C  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
00530E70  F3 49 0F 38 F6 79 10            adox rdi, qword ptr [r9 + 0x10]
00530E77  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00530E7C  66 48 0F 38 F6 F8               adcx rdi, rax
00530E82  F3 49 0F 38 F6 E8               adox rbp, r8
00530E88  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
00530E8C  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00530E92  66 48 0F 38 F6 E8               adcx rbp, rax
00530E98  F3 49 0F 38 F6 D8               adox rbx, r8
00530E9E  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00530EA4  66 48 0F 38 F6 D8               adcx rbx, rax
00530EAA  F3 4D 0F 38 F6 E0               adox r12, r8
00530EB0  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00530EB6  66 4C 0F 38 F6 E0               adcx r12, rax
00530EBC  F3 4D 0F 38 F6 E8               adox r13, r8
00530EC2  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00530EC8  66 4C 0F 38 F6 E8               adcx r13, rax
00530ECE  F3 4D 0F 38 F6 F0               adox r14, r8
00530ED4  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00530EDA  66 4C 0F 38 F6 F0               adcx r14, rax
00530EE0  F3 4D 0F 38 F6 D8               adox r11, r8
00530EE6  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00530EEC  66 4C 0F 38 F6 D8               adcx r11, rax
00530EF2  F3 49 0F 38 F6 F0               adox rsi, r8
00530EF8  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00530EFE  66 48 0F 38 F6 F0               adcx rsi, rax
00530F04  48 C7 C7 00 00 00 00            mov rdi, 0
00530F0B  F3 48 0F 38 F6 FF               adox rdi, rdi
00530F11  66 49 0F 38 F6 F8               adcx rdi, r8
00530F17  48 33 C0                        xor rax, rax
00530F1A  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
00530F1E  F3 49 0F 38 F6 69 18            adox rbp, qword ptr [r9 + 0x18]
00530F25  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00530F2A  66 48 0F 38 F6 E8               adcx rbp, rax
00530F30  F3 49 0F 38 F6 D8               adox rbx, r8
00530F36  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
00530F3A  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00530F40  66 48 0F 38 F6 D8               adcx rbx, rax
00530F46  F3 4D 0F 38 F6 E0               adox r12, r8
00530F4C  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00530F52  66 4C 0F 38 F6 E0               adcx r12, rax
00530F58  F3 4D 0F 38 F6 E8               adox r13, r8
00530F5E  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00530F64  66 4C 0F 38 F6 E8               adcx r13, rax
00530F6A  F3 4D 0F 38 F6 F0               adox r14, r8
00530F70  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00530F76  66 4C 0F 38 F6 F0               adcx r14, rax
00530F7C  F3 4D 0F 38 F6 D8               adox r11, r8
00530F82  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00530F88  66 4C 0F 38 F6 D8               adcx r11, rax
00530F8E  F3 49 0F 38 F6 F0               adox rsi, r8
00530F94  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00530F9A  66 48 0F 38 F6 F0               adcx rsi, rax
00530FA0  F3 49 0F 38 F6 F8               adox rdi, r8
00530FA6  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00530FAC  66 48 0F 38 F6 F8               adcx rdi, rax
00530FB2  48 C7 C5 00 00 00 00            mov rbp, 0
00530FB9  F3 48 0F 38 F6 ED               adox rbp, rbp
00530FBF  66 49 0F 38 F6 E8               adcx rbp, r8
00530FC5  48 33 C0                        xor rax, rax
00530FC8  49 8B 52 20                     mov rdx, qword ptr [r10 + 0x20]
00530FCC  F3 49 0F 38 F6 59 20            adox rbx, qword ptr [r9 + 0x20]
00530FD3  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00530FD8  66 48 0F 38 F6 D8               adcx rbx, rax
00530FDE  F3 4D 0F 38 F6 E0               adox r12, r8
00530FE4  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
00530FE8  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00530FEE  66 4C 0F 38 F6 E0               adcx r12, rax
00530FF4  F3 4D 0F 38 F6 E8               adox r13, r8
00530FFA  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531000  66 4C 0F 38 F6 E8               adcx r13, rax
00531006  F3 4D 0F 38 F6 F0               adox r14, r8
0053100C  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531012  66 4C 0F 38 F6 F0               adcx r14, rax
00531018  F3 4D 0F 38 F6 D8               adox r11, r8
0053101E  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531024  66 4C 0F 38 F6 D8               adcx r11, rax
0053102A  F3 49 0F 38 F6 F0               adox rsi, r8
00531030  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531036  66 48 0F 38 F6 F0               adcx rsi, rax
0053103C  F3 49 0F 38 F6 F8               adox rdi, r8
00531042  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531048  66 48 0F 38 F6 F8               adcx rdi, rax
0053104E  F3 49 0F 38 F6 E8               adox rbp, r8
00531054  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
0053105A  66 48 0F 38 F6 E8               adcx rbp, rax
00531060  48 C7 C3 00 00 00 00            mov rbx, 0
00531067  F3 48 0F 38 F6 DB               adox rbx, rbx
0053106D  66 49 0F 38 F6 D8               adcx rbx, r8
00531073  48 33 C0                        xor rax, rax
00531076  49 8B 52 28                     mov rdx, qword ptr [r10 + 0x28]
0053107A  F3 4D 0F 38 F6 61 28            adox r12, qword ptr [r9 + 0x28]
00531081  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531086  66 4C 0F 38 F6 E0               adcx r12, rax
0053108C  F3 4D 0F 38 F6 E8               adox r13, r8
00531092  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
00531096  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
0053109C  66 4C 0F 38 F6 E8               adcx r13, rax
005310A2  F3 4D 0F 38 F6 F0               adox r14, r8
005310A8  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005310AE  66 4C 0F 38 F6 F0               adcx r14, rax
005310B4  F3 4D 0F 38 F6 D8               adox r11, r8
005310BA  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005310C0  66 4C 0F 38 F6 D8               adcx r11, rax
005310C6  F3 49 0F 38 F6 F0               adox rsi, r8
005310CC  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005310D2  66 48 0F 38 F6 F0               adcx rsi, rax
005310D8  F3 49 0F 38 F6 F8               adox rdi, r8
005310DE  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005310E4  66 48 0F 38 F6 F8               adcx rdi, rax
005310EA  F3 49 0F 38 F6 E8               adox rbp, r8
005310F0  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005310F6  66 48 0F 38 F6 E8               adcx rbp, rax
005310FC  F3 49 0F 38 F6 D8               adox rbx, r8
00531102  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531108  66 48 0F 38 F6 D8               adcx rbx, rax
0053110E  49 C7 C4 00 00 00 00            mov r12, 0
00531115  F3 4D 0F 38 F6 E4               adox r12, r12
0053111B  66 4D 0F 38 F6 E0               adcx r12, r8
00531121  48 33 C0                        xor rax, rax
00531124  49 8B 52 30                     mov rdx, qword ptr [r10 + 0x30]
00531128  F3 4D 0F 38 F6 69 30            adox r13, qword ptr [r9 + 0x30]
0053112F  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531134  66 4C 0F 38 F6 E8               adcx r13, rax
0053113A  F3 4D 0F 38 F6 F0               adox r14, r8
00531140  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
00531144  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
0053114A  66 4C 0F 38 F6 F0               adcx r14, rax
00531150  F3 4D 0F 38 F6 D8               adox r11, r8
00531156  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
0053115C  66 4C 0F 38 F6 D8               adcx r11, rax
00531162  F3 49 0F 38 F6 F0               adox rsi, r8
00531168  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
0053116E  66 48 0F 38 F6 F0               adcx rsi, rax
00531174  F3 49 0F 38 F6 F8               adox rdi, r8
0053117A  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531180  66 48 0F 38 F6 F8               adcx rdi, rax
00531186  F3 49 0F 38 F6 E8               adox rbp, r8
0053118C  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531192  66 48 0F 38 F6 E8               adcx rbp, rax
00531198  F3 49 0F 38 F6 D8               adox rbx, r8
0053119E  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005311A4  66 48 0F 38 F6 D8               adcx rbx, rax
005311AA  F3 4D 0F 38 F6 E0               adox r12, r8
005311B0  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005311B6  66 4C 0F 38 F6 E0               adcx r12, rax
005311BC  49 C7 C5 00 00 00 00            mov r13, 0
005311C3  F3 4D 0F 38 F6 ED               adox r13, r13
005311C9  66 4D 0F 38 F6 E8               adcx r13, r8
005311CF  48 33 C0                        xor rax, rax
005311D2  49 8B 52 38                     mov rdx, qword ptr [r10 + 0x38]
005311D6  F3 4D 0F 38 F6 71 38            adox r14, qword ptr [r9 + 0x38]
005311DD  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005311E2  66 4C 0F 38 F6 F0               adcx r14, rax
005311E8  F3 4D 0F 38 F6 D8               adox r11, r8
005311EE  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
005311F2  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005311F8  66 4C 0F 38 F6 D8               adcx r11, rax
005311FE  F3 49 0F 38 F6 F0               adox rsi, r8
00531204  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
0053120A  66 48 0F 38 F6 F0               adcx rsi, rax
00531210  F3 49 0F 38 F6 F8               adox rdi, r8
00531216  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
0053121C  66 48 0F 38 F6 F8               adcx rdi, rax
00531222  F3 49 0F 38 F6 E8               adox rbp, r8
00531228  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
0053122E  66 48 0F 38 F6 E8               adcx rbp, rax
00531234  F3 49 0F 38 F6 D8               adox rbx, r8
0053123A  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531240  66 48 0F 38 F6 D8               adcx rbx, rax
00531246  F3 4D 0F 38 F6 E0               adox r12, r8
0053124C  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531252  66 4C 0F 38 F6 E0               adcx r12, rax
00531258  F3 4D 0F 38 F6 E8               adox r13, r8
0053125E  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531264  66 4C 0F 38 F6 E8               adcx r13, rax
0053126A  49 C7 C6 00 00 00 00            mov r14, 0
00531271  F3 4D 0F 38 F6 F6               adox r14, r14
00531277  66 4D 0F 38 F6 F0               adcx r14, r8
0053127D  49 83 C2 40                     add r10, 0x40
00531281  49 83 C1 40                     add r9, 0x40
00531285  48 33 C0                        xor rax, rax
00531288  48 33 C0                        xor rax, rax
0053128B  49 8B 12                        mov rdx, qword ptr [r10]
0053128E  F3 4D 0F 38 F6 19               adox r11, qword ptr [r9]
00531294  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531299  66 4C 0F 38 F6 D8               adcx r11, rax
0053129F  F3 49 0F 38 F6 F0               adox rsi, r8
005312A5  4D 89 19                        mov qword ptr [r9], r11
005312A8  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005312AE  66 48 0F 38 F6 F0               adcx rsi, rax
005312B4  F3 49 0F 38 F6 F8               adox rdi, r8
005312BA  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005312C0  66 48 0F 38 F6 F8               adcx rdi, rax
005312C6  F3 49 0F 38 F6 E8               adox rbp, r8
005312CC  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005312D2  66 48 0F 38 F6 E8               adcx rbp, rax
005312D8  F3 49 0F 38 F6 D8               adox rbx, r8
005312DE  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005312E4  66 48 0F 38 F6 D8               adcx rbx, rax
005312EA  F3 4D 0F 38 F6 E0               adox r12, r8
005312F0  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005312F6  66 4C 0F 38 F6 E0               adcx r12, rax
005312FC  F3 4D 0F 38 F6 E8               adox r13, r8
00531302  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531308  66 4C 0F 38 F6 E8               adcx r13, rax
0053130E  F3 4D 0F 38 F6 F0               adox r14, r8
00531314  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
0053131A  66 4C 0F 38 F6 F0               adcx r14, rax
00531320  49 C7 C3 00 00 00 00            mov r11, 0
00531327  F3 4D 0F 38 F6 DB               adox r11, r11
0053132D  66 4D 0F 38 F6 D8               adcx r11, r8
00531333  48 33 C0                        xor rax, rax
00531336  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
0053133A  F3 49 0F 38 F6 71 08            adox rsi, qword ptr [r9 + 8]
00531341  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531346  66 48 0F 38 F6 F0               adcx rsi, rax
0053134C  F3 49 0F 38 F6 F8               adox rdi, r8
00531352  49 89 71 08                     mov qword ptr [r9 + 8], rsi
00531356  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
0053135C  66 48 0F 38 F6 F8               adcx rdi, rax
00531362  F3 49 0F 38 F6 E8               adox rbp, r8
00531368  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
0053136E  66 48 0F 38 F6 E8               adcx rbp, rax
00531374  F3 49 0F 38 F6 D8               adox rbx, r8
0053137A  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531380  66 48 0F 38 F6 D8               adcx rbx, rax
00531386  F3 4D 0F 38 F6 E0               adox r12, r8
0053138C  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531392  66 4C 0F 38 F6 E0               adcx r12, rax
00531398  F3 4D 0F 38 F6 E8               adox r13, r8
0053139E  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005313A4  66 4C 0F 38 F6 E8               adcx r13, rax
005313AA  F3 4D 0F 38 F6 F0               adox r14, r8
005313B0  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005313B6  66 4C 0F 38 F6 F0               adcx r14, rax
005313BC  F3 4D 0F 38 F6 D8               adox r11, r8
005313C2  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005313C8  66 4C 0F 38 F6 D8               adcx r11, rax
005313CE  48 C7 C6 00 00 00 00            mov rsi, 0
005313D5  F3 48 0F 38 F6 F6               adox rsi, rsi
005313DB  66 49 0F 38 F6 F0               adcx rsi, r8
005313E1  48 33 C0                        xor rax, rax
005313E4  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
005313E8  F3 49 0F 38 F6 79 10            adox rdi, qword ptr [r9 + 0x10]
005313EF  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005313F4  66 48 0F 38 F6 F8               adcx rdi, rax
005313FA  F3 49 0F 38 F6 E8               adox rbp, r8
00531400  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
00531404  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
0053140A  66 48 0F 38 F6 E8               adcx rbp, rax
00531410  F3 49 0F 38 F6 D8               adox rbx, r8
00531416  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
0053141C  66 48 0F 38 F6 D8               adcx rbx, rax
00531422  F3 4D 0F 38 F6 E0               adox r12, r8
00531428  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
0053142E  66 4C 0F 38 F6 E0               adcx r12, rax
00531434  F3 4D 0F 38 F6 E8               adox r13, r8
0053143A  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531440  66 4C 0F 38 F6 E8               adcx r13, rax
00531446  F3 4D 0F 38 F6 F0               adox r14, r8
0053144C  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531452  66 4C 0F 38 F6 F0               adcx r14, rax
00531458  F3 4D 0F 38 F6 D8               adox r11, r8
0053145E  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531464  66 4C 0F 38 F6 D8               adcx r11, rax
0053146A  F3 49 0F 38 F6 F0               adox rsi, r8
00531470  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531476  66 48 0F 38 F6 F0               adcx rsi, rax
0053147C  48 C7 C7 00 00 00 00            mov rdi, 0
00531483  F3 48 0F 38 F6 FF               adox rdi, rdi
00531489  66 49 0F 38 F6 F8               adcx rdi, r8
0053148F  48 33 C0                        xor rax, rax
00531492  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
00531496  F3 49 0F 38 F6 69 18            adox rbp, qword ptr [r9 + 0x18]
0053149D  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005314A2  66 48 0F 38 F6 E8               adcx rbp, rax
005314A8  F3 49 0F 38 F6 D8               adox rbx, r8
005314AE  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
005314B2  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005314B8  66 48 0F 38 F6 D8               adcx rbx, rax
005314BE  F3 4D 0F 38 F6 E0               adox r12, r8
005314C4  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005314CA  66 4C 0F 38 F6 E0               adcx r12, rax
005314D0  F3 4D 0F 38 F6 E8               adox r13, r8
005314D6  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005314DC  66 4C 0F 38 F6 E8               adcx r13, rax
005314E2  F3 4D 0F 38 F6 F0               adox r14, r8
005314E8  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005314EE  66 4C 0F 38 F6 F0               adcx r14, rax
005314F4  F3 4D 0F 38 F6 D8               adox r11, r8
005314FA  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531500  66 4C 0F 38 F6 D8               adcx r11, rax
00531506  F3 49 0F 38 F6 F0               adox rsi, r8
0053150C  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531512  66 48 0F 38 F6 F0               adcx rsi, rax
00531518  F3 49 0F 38 F6 F8               adox rdi, r8
0053151E  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531524  66 48 0F 38 F6 F8               adcx rdi, rax
0053152A  48 C7 C5 00 00 00 00            mov rbp, 0
00531531  F3 48 0F 38 F6 ED               adox rbp, rbp
00531537  66 49 0F 38 F6 E8               adcx rbp, r8
0053153D  48 33 C0                        xor rax, rax
00531540  49 8B 52 20                     mov rdx, qword ptr [r10 + 0x20]
00531544  F3 49 0F 38 F6 59 20            adox rbx, qword ptr [r9 + 0x20]
0053154B  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531550  66 48 0F 38 F6 D8               adcx rbx, rax
00531556  F3 4D 0F 38 F6 E0               adox r12, r8
0053155C  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
00531560  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531566  66 4C 0F 38 F6 E0               adcx r12, rax
0053156C  F3 4D 0F 38 F6 E8               adox r13, r8
00531572  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531578  66 4C 0F 38 F6 E8               adcx r13, rax
0053157E  F3 4D 0F 38 F6 F0               adox r14, r8
00531584  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
0053158A  66 4C 0F 38 F6 F0               adcx r14, rax
00531590  F3 4D 0F 38 F6 D8               adox r11, r8
00531596  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
0053159C  66 4C 0F 38 F6 D8               adcx r11, rax
005315A2  F3 49 0F 38 F6 F0               adox rsi, r8
005315A8  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005315AE  66 48 0F 38 F6 F0               adcx rsi, rax
005315B4  F3 49 0F 38 F6 F8               adox rdi, r8
005315BA  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005315C0  66 48 0F 38 F6 F8               adcx rdi, rax
005315C6  F3 49 0F 38 F6 E8               adox rbp, r8
005315CC  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005315D2  66 48 0F 38 F6 E8               adcx rbp, rax
005315D8  48 C7 C3 00 00 00 00            mov rbx, 0
005315DF  F3 48 0F 38 F6 DB               adox rbx, rbx
005315E5  66 49 0F 38 F6 D8               adcx rbx, r8
005315EB  48 33 C0                        xor rax, rax
005315EE  49 8B 52 28                     mov rdx, qword ptr [r10 + 0x28]
005315F2  F3 4D 0F 38 F6 61 28            adox r12, qword ptr [r9 + 0x28]
005315F9  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005315FE  66 4C 0F 38 F6 E0               adcx r12, rax
00531604  F3 4D 0F 38 F6 E8               adox r13, r8
0053160A  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
0053160E  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531614  66 4C 0F 38 F6 E8               adcx r13, rax
0053161A  F3 4D 0F 38 F6 F0               adox r14, r8
00531620  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531626  66 4C 0F 38 F6 F0               adcx r14, rax
0053162C  F3 4D 0F 38 F6 D8               adox r11, r8
00531632  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531638  66 4C 0F 38 F6 D8               adcx r11, rax
0053163E  F3 49 0F 38 F6 F0               adox rsi, r8
00531644  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
0053164A  66 48 0F 38 F6 F0               adcx rsi, rax
00531650  F3 49 0F 38 F6 F8               adox rdi, r8
00531656  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
0053165C  66 48 0F 38 F6 F8               adcx rdi, rax
00531662  F3 49 0F 38 F6 E8               adox rbp, r8
00531668  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
0053166E  66 48 0F 38 F6 E8               adcx rbp, rax
00531674  F3 49 0F 38 F6 D8               adox rbx, r8
0053167A  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531680  66 48 0F 38 F6 D8               adcx rbx, rax
00531686  49 C7 C4 00 00 00 00            mov r12, 0
0053168D  F3 4D 0F 38 F6 E4               adox r12, r12
00531693  66 4D 0F 38 F6 E0               adcx r12, r8
00531699  48 33 C0                        xor rax, rax
0053169C  49 8B 52 30                     mov rdx, qword ptr [r10 + 0x30]
005316A0  F3 4D 0F 38 F6 69 30            adox r13, qword ptr [r9 + 0x30]
005316A7  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005316AC  66 4C 0F 38 F6 E8               adcx r13, rax
005316B2  F3 4D 0F 38 F6 F0               adox r14, r8
005316B8  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
005316BC  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005316C2  66 4C 0F 38 F6 F0               adcx r14, rax
005316C8  F3 4D 0F 38 F6 D8               adox r11, r8
005316CE  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005316D4  66 4C 0F 38 F6 D8               adcx r11, rax
005316DA  F3 49 0F 38 F6 F0               adox rsi, r8
005316E0  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005316E6  66 48 0F 38 F6 F0               adcx rsi, rax
005316EC  F3 49 0F 38 F6 F8               adox rdi, r8
005316F2  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005316F8  66 48 0F 38 F6 F8               adcx rdi, rax
005316FE  F3 49 0F 38 F6 E8               adox rbp, r8
00531704  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
0053170A  66 48 0F 38 F6 E8               adcx rbp, rax
00531710  F3 49 0F 38 F6 D8               adox rbx, r8
00531716  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
0053171C  66 48 0F 38 F6 D8               adcx rbx, rax
00531722  F3 4D 0F 38 F6 E0               adox r12, r8
00531728  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
0053172E  66 4C 0F 38 F6 E0               adcx r12, rax
00531734  49 C7 C5 00 00 00 00            mov r13, 0
0053173B  F3 4D 0F 38 F6 ED               adox r13, r13
00531741  66 4D 0F 38 F6 E8               adcx r13, r8
00531747  48 33 C0                        xor rax, rax
0053174A  49 8B 52 38                     mov rdx, qword ptr [r10 + 0x38]
0053174E  F3 4D 0F 38 F6 71 38            adox r14, qword ptr [r9 + 0x38]
00531755  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
0053175A  66 4C 0F 38 F6 F0               adcx r14, rax
00531760  F3 4D 0F 38 F6 D8               adox r11, r8
00531766  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
0053176A  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531770  66 4C 0F 38 F6 D8               adcx r11, rax
00531776  F3 49 0F 38 F6 F0               adox rsi, r8
0053177C  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531782  66 48 0F 38 F6 F0               adcx rsi, rax
00531788  F3 49 0F 38 F6 F8               adox rdi, r8
0053178E  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531794  66 48 0F 38 F6 F8               adcx rdi, rax
0053179A  F3 49 0F 38 F6 E8               adox rbp, r8
005317A0  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005317A6  66 48 0F 38 F6 E8               adcx rbp, rax
005317AC  F3 49 0F 38 F6 D8               adox rbx, r8
005317B2  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005317B8  66 48 0F 38 F6 D8               adcx rbx, rax
005317BE  F3 4D 0F 38 F6 E0               adox r12, r8
005317C4  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005317CA  66 4C 0F 38 F6 E0               adcx r12, rax
005317D0  F3 4D 0F 38 F6 E8               adox r13, r8
005317D6  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005317DC  66 4C 0F 38 F6 E8               adcx r13, rax
005317E2  49 C7 C6 00 00 00 00            mov r14, 0
005317E9  F3 4D 0F 38 F6 F6               adox r14, r14
005317EF  66 4D 0F 38 F6 F0               adcx r14, r8
005317F5  49 83 C1 40                     add r9, 0x40
005317F9  4D 89 19                        mov qword ptr [r9], r11
005317FC  49 89 71 08                     mov qword ptr [r9 + 8], rsi
00531800  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
00531804  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
00531808  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
0053180C  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
00531810  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
00531814  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
00531818  49 83 E9 40                     sub r9, 0x40
0053181C  49 83 EA 40                     sub r10, 0x40
00531820  48 83 C1 40                     add rcx, 0x40
00531824  4D 33 DB                        xor r11, r11
00531827  48 33 F6                        xor rsi, rsi
0053182A  48 33 FF                        xor rdi, rdi
0053182D  48 33 ED                        xor rbp, rbp
00531830  48 33 DB                        xor rbx, rbx
00531833  4D 33 E4                        xor r12, r12
00531836  4D 33 ED                        xor r13, r13
00531839  4D 33 F6                        xor r14, r14
0053183C  48 33 C0                        xor rax, rax
0053183F  49 8B 12                        mov rdx, qword ptr [r10]
00531842  F3 4D 0F 38 F6 19               adox r11, qword ptr [r9]
00531848  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
0053184D  66 4C 0F 38 F6 D8               adcx r11, rax
00531853  F3 49 0F 38 F6 F0               adox rsi, r8
00531859  4D 89 19                        mov qword ptr [r9], r11
0053185C  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531862  66 48 0F 38 F6 F0               adcx rsi, rax
00531868  F3 49 0F 38 F6 F8               adox rdi, r8
0053186E  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531874  66 48 0F 38 F6 F8               adcx rdi, rax
0053187A  F3 49 0F 38 F6 E8               adox rbp, r8
00531880  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531886  66 48 0F 38 F6 E8               adcx rbp, rax
0053188C  F3 49 0F 38 F6 D8               adox rbx, r8
00531892  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531898  66 48 0F 38 F6 D8               adcx rbx, rax
0053189E  F3 4D 0F 38 F6 E0               adox r12, r8
005318A4  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005318AA  66 4C 0F 38 F6 E0               adcx r12, rax
005318B0  F3 4D 0F 38 F6 E8               adox r13, r8
005318B6  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005318BC  66 4C 0F 38 F6 E8               adcx r13, rax
005318C2  F3 4D 0F 38 F6 F0               adox r14, r8
005318C8  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005318CE  66 4C 0F 38 F6 F0               adcx r14, rax
005318D4  49 C7 C3 00 00 00 00            mov r11, 0
005318DB  F3 4D 0F 38 F6 DB               adox r11, r11
005318E1  66 4D 0F 38 F6 D8               adcx r11, r8
005318E7  48 33 C0                        xor rax, rax
005318EA  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
005318EE  F3 49 0F 38 F6 71 08            adox rsi, qword ptr [r9 + 8]
005318F5  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005318FA  66 48 0F 38 F6 F0               adcx rsi, rax
00531900  F3 49 0F 38 F6 F8               adox rdi, r8
00531906  49 89 71 08                     mov qword ptr [r9 + 8], rsi
0053190A  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531910  66 48 0F 38 F6 F8               adcx rdi, rax
00531916  F3 49 0F 38 F6 E8               adox rbp, r8
0053191C  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531922  66 48 0F 38 F6 E8               adcx rbp, rax
00531928  F3 49 0F 38 F6 D8               adox rbx, r8
0053192E  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531934  66 48 0F 38 F6 D8               adcx rbx, rax
0053193A  F3 4D 0F 38 F6 E0               adox r12, r8
00531940  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531946  66 4C 0F 38 F6 E0               adcx r12, rax
0053194C  F3 4D 0F 38 F6 E8               adox r13, r8
00531952  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531958  66 4C 0F 38 F6 E8               adcx r13, rax
0053195E  F3 4D 0F 38 F6 F0               adox r14, r8
00531964  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
0053196A  66 4C 0F 38 F6 F0               adcx r14, rax
00531970  F3 4D 0F 38 F6 D8               adox r11, r8
00531976  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
0053197C  66 4C 0F 38 F6 D8               adcx r11, rax
00531982  48 C7 C6 00 00 00 00            mov rsi, 0
00531989  F3 48 0F 38 F6 F6               adox rsi, rsi
0053198F  66 49 0F 38 F6 F0               adcx rsi, r8
00531995  48 33 C0                        xor rax, rax
00531998  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
0053199C  F3 49 0F 38 F6 79 10            adox rdi, qword ptr [r9 + 0x10]
005319A3  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005319A8  66 48 0F 38 F6 F8               adcx rdi, rax
005319AE  F3 49 0F 38 F6 E8               adox rbp, r8
005319B4  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
005319B8  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005319BE  66 48 0F 38 F6 E8               adcx rbp, rax
005319C4  F3 49 0F 38 F6 D8               adox rbx, r8
005319CA  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005319D0  66 48 0F 38 F6 D8               adcx rbx, rax
005319D6  F3 4D 0F 38 F6 E0               adox r12, r8
005319DC  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005319E2  66 4C 0F 38 F6 E0               adcx r12, rax
005319E8  F3 4D 0F 38 F6 E8               adox r13, r8
005319EE  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005319F4  66 4C 0F 38 F6 E8               adcx r13, rax
005319FA  F3 4D 0F 38 F6 F0               adox r14, r8
00531A00  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531A06  66 4C 0F 38 F6 F0               adcx r14, rax
00531A0C  F3 4D 0F 38 F6 D8               adox r11, r8
00531A12  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531A18  66 4C 0F 38 F6 D8               adcx r11, rax
00531A1E  F3 49 0F 38 F6 F0               adox rsi, r8
00531A24  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531A2A  66 48 0F 38 F6 F0               adcx rsi, rax
00531A30  48 C7 C7 00 00 00 00            mov rdi, 0
00531A37  F3 48 0F 38 F6 FF               adox rdi, rdi
00531A3D  66 49 0F 38 F6 F8               adcx rdi, r8
00531A43  48 33 C0                        xor rax, rax
00531A46  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
00531A4A  F3 49 0F 38 F6 69 18            adox rbp, qword ptr [r9 + 0x18]
00531A51  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531A56  66 48 0F 38 F6 E8               adcx rbp, rax
00531A5C  F3 49 0F 38 F6 D8               adox rbx, r8
00531A62  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
00531A66  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531A6C  66 48 0F 38 F6 D8               adcx rbx, rax
00531A72  F3 4D 0F 38 F6 E0               adox r12, r8
00531A78  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531A7E  66 4C 0F 38 F6 E0               adcx r12, rax
00531A84  F3 4D 0F 38 F6 E8               adox r13, r8
00531A8A  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531A90  66 4C 0F 38 F6 E8               adcx r13, rax
00531A96  F3 4D 0F 38 F6 F0               adox r14, r8
00531A9C  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531AA2  66 4C 0F 38 F6 F0               adcx r14, rax
00531AA8  F3 4D 0F 38 F6 D8               adox r11, r8
00531AAE  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531AB4  66 4C 0F 38 F6 D8               adcx r11, rax
00531ABA  F3 49 0F 38 F6 F0               adox rsi, r8
00531AC0  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531AC6  66 48 0F 38 F6 F0               adcx rsi, rax
00531ACC  F3 49 0F 38 F6 F8               adox rdi, r8
00531AD2  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531AD8  66 48 0F 38 F6 F8               adcx rdi, rax
00531ADE  48 C7 C5 00 00 00 00            mov rbp, 0
00531AE5  F3 48 0F 38 F6 ED               adox rbp, rbp
00531AEB  66 49 0F 38 F6 E8               adcx rbp, r8
00531AF1  48 33 C0                        xor rax, rax
00531AF4  49 8B 52 20                     mov rdx, qword ptr [r10 + 0x20]
00531AF8  F3 49 0F 38 F6 59 20            adox rbx, qword ptr [r9 + 0x20]
00531AFF  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531B04  66 48 0F 38 F6 D8               adcx rbx, rax
00531B0A  F3 4D 0F 38 F6 E0               adox r12, r8
00531B10  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
00531B14  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531B1A  66 4C 0F 38 F6 E0               adcx r12, rax
00531B20  F3 4D 0F 38 F6 E8               adox r13, r8
00531B26  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531B2C  66 4C 0F 38 F6 E8               adcx r13, rax
00531B32  F3 4D 0F 38 F6 F0               adox r14, r8
00531B38  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531B3E  66 4C 0F 38 F6 F0               adcx r14, rax
00531B44  F3 4D 0F 38 F6 D8               adox r11, r8
00531B4A  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531B50  66 4C 0F 38 F6 D8               adcx r11, rax
00531B56  F3 49 0F 38 F6 F0               adox rsi, r8
00531B5C  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531B62  66 48 0F 38 F6 F0               adcx rsi, rax
00531B68  F3 49 0F 38 F6 F8               adox rdi, r8
00531B6E  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531B74  66 48 0F 38 F6 F8               adcx rdi, rax
00531B7A  F3 49 0F 38 F6 E8               adox rbp, r8
00531B80  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531B86  66 48 0F 38 F6 E8               adcx rbp, rax
00531B8C  48 C7 C3 00 00 00 00            mov rbx, 0
00531B93  F3 48 0F 38 F6 DB               adox rbx, rbx
00531B99  66 49 0F 38 F6 D8               adcx rbx, r8
00531B9F  48 33 C0                        xor rax, rax
00531BA2  49 8B 52 28                     mov rdx, qword ptr [r10 + 0x28]
00531BA6  F3 4D 0F 38 F6 61 28            adox r12, qword ptr [r9 + 0x28]
00531BAD  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531BB2  66 4C 0F 38 F6 E0               adcx r12, rax
00531BB8  F3 4D 0F 38 F6 E8               adox r13, r8
00531BBE  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
00531BC2  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531BC8  66 4C 0F 38 F6 E8               adcx r13, rax
00531BCE  F3 4D 0F 38 F6 F0               adox r14, r8
00531BD4  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531BDA  66 4C 0F 38 F6 F0               adcx r14, rax
00531BE0  F3 4D 0F 38 F6 D8               adox r11, r8
00531BE6  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531BEC  66 4C 0F 38 F6 D8               adcx r11, rax
00531BF2  F3 49 0F 38 F6 F0               adox rsi, r8
00531BF8  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531BFE  66 48 0F 38 F6 F0               adcx rsi, rax
00531C04  F3 49 0F 38 F6 F8               adox rdi, r8
00531C0A  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531C10  66 48 0F 38 F6 F8               adcx rdi, rax
00531C16  F3 49 0F 38 F6 E8               adox rbp, r8
00531C1C  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531C22  66 48 0F 38 F6 E8               adcx rbp, rax
00531C28  F3 49 0F 38 F6 D8               adox rbx, r8
00531C2E  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531C34  66 48 0F 38 F6 D8               adcx rbx, rax
00531C3A  49 C7 C4 00 00 00 00            mov r12, 0
00531C41  F3 4D 0F 38 F6 E4               adox r12, r12
00531C47  66 4D 0F 38 F6 E0               adcx r12, r8
00531C4D  48 33 C0                        xor rax, rax
00531C50  49 8B 52 30                     mov rdx, qword ptr [r10 + 0x30]
00531C54  F3 4D 0F 38 F6 69 30            adox r13, qword ptr [r9 + 0x30]
00531C5B  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531C60  66 4C 0F 38 F6 E8               adcx r13, rax
00531C66  F3 4D 0F 38 F6 F0               adox r14, r8
00531C6C  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
00531C70  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531C76  66 4C 0F 38 F6 F0               adcx r14, rax
00531C7C  F3 4D 0F 38 F6 D8               adox r11, r8
00531C82  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531C88  66 4C 0F 38 F6 D8               adcx r11, rax
00531C8E  F3 49 0F 38 F6 F0               adox rsi, r8
00531C94  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531C9A  66 48 0F 38 F6 F0               adcx rsi, rax
00531CA0  F3 49 0F 38 F6 F8               adox rdi, r8
00531CA6  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531CAC  66 48 0F 38 F6 F8               adcx rdi, rax
00531CB2  F3 49 0F 38 F6 E8               adox rbp, r8
00531CB8  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531CBE  66 48 0F 38 F6 E8               adcx rbp, rax
00531CC4  F3 49 0F 38 F6 D8               adox rbx, r8
00531CCA  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531CD0  66 48 0F 38 F6 D8               adcx rbx, rax
00531CD6  F3 4D 0F 38 F6 E0               adox r12, r8
00531CDC  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531CE2  66 4C 0F 38 F6 E0               adcx r12, rax
00531CE8  49 C7 C5 00 00 00 00            mov r13, 0
00531CEF  F3 4D 0F 38 F6 ED               adox r13, r13
00531CF5  66 4D 0F 38 F6 E8               adcx r13, r8
00531CFB  48 33 C0                        xor rax, rax
00531CFE  49 8B 52 38                     mov rdx, qword ptr [r10 + 0x38]
00531D02  F3 4D 0F 38 F6 71 38            adox r14, qword ptr [r9 + 0x38]
00531D09  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531D0E  66 4C 0F 38 F6 F0               adcx r14, rax
00531D14  F3 4D 0F 38 F6 D8               adox r11, r8
00531D1A  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
00531D1E  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531D24  66 4C 0F 38 F6 D8               adcx r11, rax
00531D2A  F3 49 0F 38 F6 F0               adox rsi, r8
00531D30  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531D36  66 48 0F 38 F6 F0               adcx rsi, rax
00531D3C  F3 49 0F 38 F6 F8               adox rdi, r8
00531D42  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531D48  66 48 0F 38 F6 F8               adcx rdi, rax
00531D4E  F3 49 0F 38 F6 E8               adox rbp, r8
00531D54  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531D5A  66 48 0F 38 F6 E8               adcx rbp, rax
00531D60  F3 49 0F 38 F6 D8               adox rbx, r8
00531D66  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531D6C  66 48 0F 38 F6 D8               adcx rbx, rax
00531D72  F3 4D 0F 38 F6 E0               adox r12, r8
00531D78  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531D7E  66 4C 0F 38 F6 E0               adcx r12, rax
00531D84  F3 4D 0F 38 F6 E8               adox r13, r8
00531D8A  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531D90  66 4C 0F 38 F6 E8               adcx r13, rax
00531D96  49 C7 C6 00 00 00 00            mov r14, 0
00531D9D  F3 4D 0F 38 F6 F6               adox r14, r14
00531DA3  66 4D 0F 38 F6 F0               adcx r14, r8
00531DA9  49 83 C2 40                     add r10, 0x40
00531DAD  49 83 C1 40                     add r9, 0x40
00531DB1  48 33 C0                        xor rax, rax
00531DB4  48 33 C0                        xor rax, rax
00531DB7  49 8B 12                        mov rdx, qword ptr [r10]
00531DBA  F3 4D 0F 38 F6 19               adox r11, qword ptr [r9]
00531DC0  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531DC5  66 4C 0F 38 F6 D8               adcx r11, rax
00531DCB  F3 49 0F 38 F6 F0               adox rsi, r8
00531DD1  4D 89 19                        mov qword ptr [r9], r11
00531DD4  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531DDA  66 48 0F 38 F6 F0               adcx rsi, rax
00531DE0  F3 49 0F 38 F6 F8               adox rdi, r8
00531DE6  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531DEC  66 48 0F 38 F6 F8               adcx rdi, rax
00531DF2  F3 49 0F 38 F6 E8               adox rbp, r8
00531DF8  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531DFE  66 48 0F 38 F6 E8               adcx rbp, rax
00531E04  F3 49 0F 38 F6 D8               adox rbx, r8
00531E0A  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531E10  66 48 0F 38 F6 D8               adcx rbx, rax
00531E16  F3 4D 0F 38 F6 E0               adox r12, r8
00531E1C  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531E22  66 4C 0F 38 F6 E0               adcx r12, rax
00531E28  F3 4D 0F 38 F6 E8               adox r13, r8
00531E2E  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531E34  66 4C 0F 38 F6 E8               adcx r13, rax
00531E3A  F3 4D 0F 38 F6 F0               adox r14, r8
00531E40  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531E46  66 4C 0F 38 F6 F0               adcx r14, rax
00531E4C  49 C7 C3 00 00 00 00            mov r11, 0
00531E53  F3 4D 0F 38 F6 DB               adox r11, r11
00531E59  66 4D 0F 38 F6 D8               adcx r11, r8
00531E5F  48 33 C0                        xor rax, rax
00531E62  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
00531E66  F3 49 0F 38 F6 71 08            adox rsi, qword ptr [r9 + 8]
00531E6D  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531E72  66 48 0F 38 F6 F0               adcx rsi, rax
00531E78  F3 49 0F 38 F6 F8               adox rdi, r8
00531E7E  49 89 71 08                     mov qword ptr [r9 + 8], rsi
00531E82  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531E88  66 48 0F 38 F6 F8               adcx rdi, rax
00531E8E  F3 49 0F 38 F6 E8               adox rbp, r8
00531E94  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531E9A  66 48 0F 38 F6 E8               adcx rbp, rax
00531EA0  F3 49 0F 38 F6 D8               adox rbx, r8
00531EA6  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531EAC  66 48 0F 38 F6 D8               adcx rbx, rax
00531EB2  F3 4D 0F 38 F6 E0               adox r12, r8
00531EB8  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531EBE  66 4C 0F 38 F6 E0               adcx r12, rax
00531EC4  F3 4D 0F 38 F6 E8               adox r13, r8
00531ECA  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531ED0  66 4C 0F 38 F6 E8               adcx r13, rax
00531ED6  F3 4D 0F 38 F6 F0               adox r14, r8
00531EDC  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531EE2  66 4C 0F 38 F6 F0               adcx r14, rax
00531EE8  F3 4D 0F 38 F6 D8               adox r11, r8
00531EEE  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531EF4  66 4C 0F 38 F6 D8               adcx r11, rax
00531EFA  48 C7 C6 00 00 00 00            mov rsi, 0
00531F01  F3 48 0F 38 F6 F6               adox rsi, rsi
00531F07  66 49 0F 38 F6 F0               adcx rsi, r8
00531F0D  48 33 C0                        xor rax, rax
00531F10  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
00531F14  F3 49 0F 38 F6 79 10            adox rdi, qword ptr [r9 + 0x10]
00531F1B  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531F20  66 48 0F 38 F6 F8               adcx rdi, rax
00531F26  F3 49 0F 38 F6 E8               adox rbp, r8
00531F2C  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
00531F30  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531F36  66 48 0F 38 F6 E8               adcx rbp, rax
00531F3C  F3 49 0F 38 F6 D8               adox rbx, r8
00531F42  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531F48  66 48 0F 38 F6 D8               adcx rbx, rax
00531F4E  F3 4D 0F 38 F6 E0               adox r12, r8
00531F54  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00531F5A  66 4C 0F 38 F6 E0               adcx r12, rax
00531F60  F3 4D 0F 38 F6 E8               adox r13, r8
00531F66  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00531F6C  66 4C 0F 38 F6 E8               adcx r13, rax
00531F72  F3 4D 0F 38 F6 F0               adox r14, r8
00531F78  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00531F7E  66 4C 0F 38 F6 F0               adcx r14, rax
00531F84  F3 4D 0F 38 F6 D8               adox r11, r8
00531F8A  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00531F90  66 4C 0F 38 F6 D8               adcx r11, rax
00531F96  F3 49 0F 38 F6 F0               adox rsi, r8
00531F9C  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00531FA2  66 48 0F 38 F6 F0               adcx rsi, rax
00531FA8  48 C7 C7 00 00 00 00            mov rdi, 0
00531FAF  F3 48 0F 38 F6 FF               adox rdi, rdi
00531FB5  66 49 0F 38 F6 F8               adcx rdi, r8
00531FBB  48 33 C0                        xor rax, rax
00531FBE  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
00531FC2  F3 49 0F 38 F6 69 18            adox rbp, qword ptr [r9 + 0x18]
00531FC9  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00531FCE  66 48 0F 38 F6 E8               adcx rbp, rax
00531FD4  F3 49 0F 38 F6 D8               adox rbx, r8
00531FDA  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
00531FDE  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00531FE4  66 48 0F 38 F6 D8               adcx rbx, rax
00531FEA  F3 4D 0F 38 F6 E0               adox r12, r8
00531FF0  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00531FF6  66 4C 0F 38 F6 E0               adcx r12, rax
00531FFC  F3 4D 0F 38 F6 E8               adox r13, r8
00532002  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00532008  66 4C 0F 38 F6 E8               adcx r13, rax
0053200E  F3 4D 0F 38 F6 F0               adox r14, r8
00532014  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
0053201A  66 4C 0F 38 F6 F0               adcx r14, rax
00532020  F3 4D 0F 38 F6 D8               adox r11, r8
00532026  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
0053202C  66 4C 0F 38 F6 D8               adcx r11, rax
00532032  F3 49 0F 38 F6 F0               adox rsi, r8
00532038  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
0053203E  66 48 0F 38 F6 F0               adcx rsi, rax
00532044  F3 49 0F 38 F6 F8               adox rdi, r8
0053204A  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00532050  66 48 0F 38 F6 F8               adcx rdi, rax
00532056  48 C7 C5 00 00 00 00            mov rbp, 0
0053205D  F3 48 0F 38 F6 ED               adox rbp, rbp
00532063  66 49 0F 38 F6 E8               adcx rbp, r8
00532069  48 33 C0                        xor rax, rax
0053206C  49 8B 52 20                     mov rdx, qword ptr [r10 + 0x20]
00532070  F3 49 0F 38 F6 59 20            adox rbx, qword ptr [r9 + 0x20]
00532077  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
0053207C  66 48 0F 38 F6 D8               adcx rbx, rax
00532082  F3 4D 0F 38 F6 E0               adox r12, r8
00532088  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
0053208C  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00532092  66 4C 0F 38 F6 E0               adcx r12, rax
00532098  F3 4D 0F 38 F6 E8               adox r13, r8
0053209E  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005320A4  66 4C 0F 38 F6 E8               adcx r13, rax
005320AA  F3 4D 0F 38 F6 F0               adox r14, r8
005320B0  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005320B6  66 4C 0F 38 F6 F0               adcx r14, rax
005320BC  F3 4D 0F 38 F6 D8               adox r11, r8
005320C2  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005320C8  66 4C 0F 38 F6 D8               adcx r11, rax
005320CE  F3 49 0F 38 F6 F0               adox rsi, r8
005320D4  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005320DA  66 48 0F 38 F6 F0               adcx rsi, rax
005320E0  F3 49 0F 38 F6 F8               adox rdi, r8
005320E6  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005320EC  66 48 0F 38 F6 F8               adcx rdi, rax
005320F2  F3 49 0F 38 F6 E8               adox rbp, r8
005320F8  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005320FE  66 48 0F 38 F6 E8               adcx rbp, rax
00532104  48 C7 C3 00 00 00 00            mov rbx, 0
0053210B  F3 48 0F 38 F6 DB               adox rbx, rbx
00532111  66 49 0F 38 F6 D8               adcx rbx, r8
00532117  48 33 C0                        xor rax, rax
0053211A  49 8B 52 28                     mov rdx, qword ptr [r10 + 0x28]
0053211E  F3 4D 0F 38 F6 61 28            adox r12, qword ptr [r9 + 0x28]
00532125  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
0053212A  66 4C 0F 38 F6 E0               adcx r12, rax
00532130  F3 4D 0F 38 F6 E8               adox r13, r8
00532136  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
0053213A  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
00532140  66 4C 0F 38 F6 E8               adcx r13, rax
00532146  F3 4D 0F 38 F6 F0               adox r14, r8
0053214C  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00532152  66 4C 0F 38 F6 F0               adcx r14, rax
00532158  F3 4D 0F 38 F6 D8               adox r11, r8
0053215E  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00532164  66 4C 0F 38 F6 D8               adcx r11, rax
0053216A  F3 49 0F 38 F6 F0               adox rsi, r8
00532170  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00532176  66 48 0F 38 F6 F0               adcx rsi, rax
0053217C  F3 49 0F 38 F6 F8               adox rdi, r8
00532182  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00532188  66 48 0F 38 F6 F8               adcx rdi, rax
0053218E  F3 49 0F 38 F6 E8               adox rbp, r8
00532194  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
0053219A  66 48 0F 38 F6 E8               adcx rbp, rax
005321A0  F3 49 0F 38 F6 D8               adox rbx, r8
005321A6  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
005321AC  66 48 0F 38 F6 D8               adcx rbx, rax
005321B2  49 C7 C4 00 00 00 00            mov r12, 0
005321B9  F3 4D 0F 38 F6 E4               adox r12, r12
005321BF  66 4D 0F 38 F6 E0               adcx r12, r8
005321C5  48 33 C0                        xor rax, rax
005321C8  49 8B 52 30                     mov rdx, qword ptr [r10 + 0x30]
005321CC  F3 4D 0F 38 F6 69 30            adox r13, qword ptr [r9 + 0x30]
005321D3  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
005321D8  66 4C 0F 38 F6 E8               adcx r13, rax
005321DE  F3 4D 0F 38 F6 F0               adox r14, r8
005321E4  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
005321E8  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
005321EE  66 4C 0F 38 F6 F0               adcx r14, rax
005321F4  F3 4D 0F 38 F6 D8               adox r11, r8
005321FA  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
00532200  66 4C 0F 38 F6 D8               adcx r11, rax
00532206  F3 49 0F 38 F6 F0               adox rsi, r8
0053220C  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
00532212  66 48 0F 38 F6 F0               adcx rsi, rax
00532218  F3 49 0F 38 F6 F8               adox rdi, r8
0053221E  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
00532224  66 48 0F 38 F6 F8               adcx rdi, rax
0053222A  F3 49 0F 38 F6 E8               adox rbp, r8
00532230  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
00532236  66 48 0F 38 F6 E8               adcx rbp, rax
0053223C  F3 49 0F 38 F6 D8               adox rbx, r8
00532242  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
00532248  66 48 0F 38 F6 D8               adcx rbx, rax
0053224E  F3 4D 0F 38 F6 E0               adox r12, r8
00532254  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
0053225A  66 4C 0F 38 F6 E0               adcx r12, rax
00532260  49 C7 C5 00 00 00 00            mov r13, 0
00532267  F3 4D 0F 38 F6 ED               adox r13, r13
0053226D  66 4D 0F 38 F6 E8               adcx r13, r8
00532273  48 33 C0                        xor rax, rax
00532276  49 8B 52 38                     mov rdx, qword ptr [r10 + 0x38]
0053227A  F3 4D 0F 38 F6 71 38            adox r14, qword ptr [r9 + 0x38]
00532281  C4 62 FB F6 01                  mulx r8, rax, qword ptr [rcx]
00532286  66 4C 0F 38 F6 F0               adcx r14, rax
0053228C  F3 4D 0F 38 F6 D8               adox r11, r8
00532292  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
00532296  C4 62 FB F6 41 08               mulx r8, rax, qword ptr [rcx + 8]
0053229C  66 4C 0F 38 F6 D8               adcx r11, rax
005322A2  F3 49 0F 38 F6 F0               adox rsi, r8
005322A8  C4 62 FB F6 41 10               mulx r8, rax, qword ptr [rcx + 0x10]
005322AE  66 48 0F 38 F6 F0               adcx rsi, rax
005322B4  F3 49 0F 38 F6 F8               adox rdi, r8
005322BA  C4 62 FB F6 41 18               mulx r8, rax, qword ptr [rcx + 0x18]
005322C0  66 48 0F 38 F6 F8               adcx rdi, rax
005322C6  F3 49 0F 38 F6 E8               adox rbp, r8
005322CC  C4 62 FB F6 41 20               mulx r8, rax, qword ptr [rcx + 0x20]
005322D2  66 48 0F 38 F6 E8               adcx rbp, rax
005322D8  F3 49 0F 38 F6 D8               adox rbx, r8
005322DE  C4 62 FB F6 41 28               mulx r8, rax, qword ptr [rcx + 0x28]
005322E4  66 48 0F 38 F6 D8               adcx rbx, rax
005322EA  F3 4D 0F 38 F6 E0               adox r12, r8
005322F0  C4 62 FB F6 41 30               mulx r8, rax, qword ptr [rcx + 0x30]
005322F6  66 4C 0F 38 F6 E0               adcx r12, rax
005322FC  F3 4D 0F 38 F6 E8               adox r13, r8
00532302  C4 62 FB F6 41 38               mulx r8, rax, qword ptr [rcx + 0x38]
00532308  66 4C 0F 38 F6 E8               adcx r13, rax
0053230E  49 C7 C6 00 00 00 00            mov r14, 0
00532315  F3 4D 0F 38 F6 F6               adox r14, r14
0053231B  66 4D 0F 38 F6 F0               adcx r14, r8
00532321  49 83 C1 40                     add r9, 0x40
00532325  4D 89 19                        mov qword ptr [r9], r11
00532328  49 89 71 08                     mov qword ptr [r9 + 8], rsi
0053232C  49 89 79 10                     mov qword ptr [r9 + 0x10], rdi
00532330  49 89 69 18                     mov qword ptr [r9 + 0x18], rbp
00532334  49 89 59 20                     mov qword ptr [r9 + 0x20], rbx
00532338  4D 89 61 28                     mov qword ptr [r9 + 0x28], r12
0053233C  4D 89 69 30                     mov qword ptr [r9 + 0x30], r13
00532340  4D 89 71 38                     mov qword ptr [r9 + 0x38], r14
00532344  41 5E                           pop r14
00532346  41 5D                           pop r13
00532348  41 5C                           pop r12
0053234A  5B                              pop rbx
0053234B  5D                              pop rbp
0053234C  5F                              pop rdi
0053234D  5E                              pop rsi
0053234E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefRawMulMulx1024(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;

    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm0;
    *(unsigned __int64 *)(a4 + 32) = v_xmm0;
    *(unsigned __int64 *)(a4 + 48) = v_xmm0;
    *(unsigned __int64 *)(a4 + 64) = v_xmm0;
    *(unsigned __int64 *)(a4 + 80) = v_xmm0;
    *(unsigned __int64 *)(a4 + 96) = v_xmm0;
    *(unsigned __int64 *)(a4 + 112) = v_xmm0;
    v_r11 = 0;
    v_rsi = 0;
    v_rdi = 0;
    v_rbp = 0;
    v_rbx = 0;
    v_r12 = 0;
    v_r13 = 0;
    v_r14 = 0;
    result = 0;
    *(unsigned __int64 *)(a4) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    v_r10 = (a2) + (64);
    a4 = (a4) + (64);
    result = 0;
    result = 0;
    *(unsigned __int64 *)(a4) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    a4 = (a4) + (64);
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    a4 = (a4) - (64);
    v_r10 = (v_r10) - (64);
    a1 = (a1) + (64);
    v_r11 = 0;
    v_rsi = 0;
    v_rdi = 0;
    v_rbp = 0;
    v_rbx = 0;
    v_r12 = 0;
    v_r13 = 0;
    v_r14 = 0;
    result = 0;
    *(unsigned __int64 *)(a4) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    v_r10 = (v_r10) + (64);
    a4 = (a4) + (64);
    result = 0;
    result = 0;
    *(unsigned __int64 *)(a4) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    result = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    a4 = (a4) + (64);
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned __int64 *)(a4 + 8) = 0;
    *(unsigned __int64 *)(a4 + 16) = 0;
    *(unsigned __int64 *)(a4 + 24) = 0;
    *(unsigned __int64 *)(a4 + 32) = 0;
    *(unsigned __int64 *)(a4 + 40) = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    *(unsigned __int64 *)(a4 + 56) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefRawMulMulx1024(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;

    *(uint64_t *)(arg4) = v_xmm0;
    *(uint64_t *)(arg4 + 0x10) = v_xmm0;
    *(uint64_t *)(arg4 + 0x20) = v_xmm0;
    *(uint64_t *)(arg4 + 0x30) = v_xmm0;
    *(uint64_t *)(arg4 + 0x40) = v_xmm0;
    *(uint64_t *)(arg4 + 0x50) = v_xmm0;
    *(uint64_t *)(arg4 + 0x60) = v_xmm0;
    *(uint64_t *)(arg4 + 0x70) = v_xmm0;
    local_r11 = 0;
    local_rsi = 0;
    local_rdi = 0;
    local_rbp = 0;
    local_rbx = 0;
    local_r12 = 0;
    local_r13 = 0;
    local_r14 = 0;
    result = 0;
    *(uint64_t *)(arg4) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    local_r10 = (Arg2) + (64);
    Arg4 = (Arg4) + (64);
    result = 0;
    result = 0;
    *(uint64_t *)(arg4) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    Arg4 = (Arg4) + (64);
    *(uint64_t *)(arg4) = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    Arg4 = (Arg4) - (64);
    local_r10 = (local_r10) - (64);
    Arg1 = (Arg1) + (64);
    local_r11 = 0;
    local_rsi = 0;
    local_rdi = 0;
    local_rbp = 0;
    local_rbx = 0;
    local_r12 = 0;
    local_r13 = 0;
    local_r14 = 0;
    result = 0;
    *(uint64_t *)(arg4) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    local_r10 = (local_r10) + (64);
    Arg4 = (Arg4) + (64);
    result = 0;
    result = 0;
    *(uint64_t *)(arg4) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    result = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    Arg4 = (Arg4) + (64);
    *(uint64_t *)(arg4) = 0;
    *(uint64_t *)(arg4 + 0x8) = 0;
    *(uint64_t *)(arg4 + 0x10) = 0;
    *(uint64_t *)(arg4 + 0x18) = 0;
    *(uint64_t *)(arg4 + 0x20) = 0;
    *(uint64_t *)(arg4 + 0x28) = 0;
    *(uint64_t *)(arg4 + 0x30) = 0;
    *(uint64_t *)(arg4 + 0x38) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `128` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x10` | `128` | `W` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x18` | `64` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x20` | `64` | `W` |
| `Arg4` | `+ 0x20` | `128` | `W` |
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x28` | `64` | `W` |
| `Arg4` | `+ 0x30` | `64` | `R` |

추가 오프셋 8개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00530CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00530CC0[BB_00530CC0]
```
