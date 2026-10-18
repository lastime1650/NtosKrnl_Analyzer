# SymCryptFdefRawSquareMulx1024

- RVA: `0x00532360`–`0x005331F1` (길이 `3,729` bytes)
- VA: `0x0000000140532360`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3530`
- 디코드: `683`개 명령, `3,729/3,729` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefModSquareMontgomeryMulx1024](SymCryptFdefModSquareMontgomeryMulx1024_function_00535400.md) at `0x00535424`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00532360  48 56                           push rsi
00532362  57                              push rdi
00532363  55                              push rbp
00532364  53                              push rbx
00532365  41 54                           push r12
00532367  41 55                           push r13
00532369  41 56                           push r14
0053236B  4C 8B D2                        mov r10, rdx
0053236E  0F 57 C0                        xorps xmm0, xmm0
00532371  41 0F 29 00                     movaps xmmword ptr [r8], xmm0
00532375  41 0F 29 40 10                  movaps xmmword ptr [r8 + 0x10], xmm0
0053237A  41 0F 29 40 20                  movaps xmmword ptr [r8 + 0x20], xmm0
0053237F  41 0F 29 40 30                  movaps xmmword ptr [r8 + 0x30], xmm0
00532384  41 0F 29 40 40                  movaps xmmword ptr [r8 + 0x40], xmm0
00532389  41 0F 29 40 50                  movaps xmmword ptr [r8 + 0x50], xmm0
0053238E  41 0F 29 40 60                  movaps xmmword ptr [r8 + 0x60], xmm0
00532393  41 0F 29 40 70                  movaps xmmword ptr [r8 + 0x70], xmm0
00532398  48 33 C0                        xor rax, rax
0053239B  48 8B 11                        mov rdx, qword ptr [rcx]
0053239E  49 8B 70 08                     mov rsi, qword ptr [r8 + 8]
005323A2  49 8B 78 10                     mov rdi, qword ptr [r8 + 0x10]
005323A6  49 8B 68 18                     mov rbp, qword ptr [r8 + 0x18]
005323AA  49 8B 58 20                     mov rbx, qword ptr [r8 + 0x20]
005323AE  4D 8B 60 28                     mov r12, qword ptr [r8 + 0x28]
005323B2  4D 8B 68 30                     mov r13, qword ptr [r8 + 0x30]
005323B6  4D 8B 70 38                     mov r14, qword ptr [r8 + 0x38]
005323BA  4D 33 DB                        xor r11, r11
005323BD  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
005323C3  66 48 0F 38 F6 F0               adcx rsi, rax
005323C9  F3 49 0F 38 F6 FA               adox rdi, r10
005323CF  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
005323D5  66 48 0F 38 F6 F8               adcx rdi, rax
005323DB  F3 49 0F 38 F6 EA               adox rbp, r10
005323E1  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
005323E7  66 48 0F 38 F6 E8               adcx rbp, rax
005323ED  F3 49 0F 38 F6 DA               adox rbx, r10
005323F3  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
005323F9  66 48 0F 38 F6 D8               adcx rbx, rax
005323FF  F3 4D 0F 38 F6 E2               adox r12, r10
00532405  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
0053240B  66 4C 0F 38 F6 E0               adcx r12, rax
00532411  F3 4D 0F 38 F6 EA               adox r13, r10
00532417  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053241D  66 4C 0F 38 F6 E8               adcx r13, rax
00532423  F3 4D 0F 38 F6 F2               adox r14, r10
00532429  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
0053242F  66 4C 0F 38 F6 F0               adcx r14, rax
00532435  49 89 70 08                     mov qword ptr [r8 + 8], rsi
00532439  F3 4D 0F 38 F6 DB               adox r11, r11
0053243F  66 4D 0F 38 F6 DA               adcx r11, r10
00532445  49 89 78 10                     mov qword ptr [r8 + 0x10], rdi
00532449  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0053244D  48 33 C0                        xor rax, rax
00532450  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532456  66 48 0F 38 F6 E8               adcx rbp, rax
0053245C  F3 49 0F 38 F6 DA               adox rbx, r10
00532462  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532468  66 48 0F 38 F6 D8               adcx rbx, rax
0053246E  F3 4D 0F 38 F6 E2               adox r12, r10
00532474  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
0053247A  66 4C 0F 38 F6 E0               adcx r12, rax
00532480  F3 4D 0F 38 F6 EA               adox r13, r10
00532486  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
0053248C  66 4C 0F 38 F6 E8               adcx r13, rax
00532492  F3 4D 0F 38 F6 F2               adox r14, r10
00532498  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053249E  66 4C 0F 38 F6 F0               adcx r14, rax
005324A4  F3 4D 0F 38 F6 DA               adox r11, r10
005324AA  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
005324AE  48 C7 C6 00 00 00 00            mov rsi, 0
005324B5  48 C7 C7 00 00 00 00            mov rdi, 0
005324BC  49 89 68 18                     mov qword ptr [r8 + 0x18], rbp
005324C0  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
005324C6  66 4C 0F 38 F6 D8               adcx r11, rax
005324CC  F3 49 0F 38 F6 F2               adox rsi, r10
005324D2  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
005324D8  66 48 0F 38 F6 F0               adcx rsi, rax
005324DE  49 89 58 20                     mov qword ptr [r8 + 0x20], rbx
005324E2  66 49 0F 38 F6 FA               adcx rdi, r10
005324E8  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
005324EC  48 33 C0                        xor rax, rax
005324EF  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
005324F5  66 4C 0F 38 F6 E0               adcx r12, rax
005324FB  F3 4D 0F 38 F6 EA               adox r13, r10
00532501  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532507  66 4C 0F 38 F6 E8               adcx r13, rax
0053250D  F3 4D 0F 38 F6 F2               adox r14, r10
00532513  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532519  66 4C 0F 38 F6 F0               adcx r14, rax
0053251F  F3 4D 0F 38 F6 DA               adox r11, r10
00532525  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053252B  66 4C 0F 38 F6 D8               adcx r11, rax
00532531  F3 49 0F 38 F6 F2               adox rsi, r10
00532537  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
0053253B  48 C7 C5 00 00 00 00            mov rbp, 0
00532542  48 C7 C3 00 00 00 00            mov rbx, 0
00532549  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
0053254F  66 48 0F 38 F6 F0               adcx rsi, rax
00532555  F3 49 0F 38 F6 FA               adox rdi, r10
0053255B  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
00532561  66 48 0F 38 F6 F8               adcx rdi, rax
00532567  F3 49 0F 38 F6 EA               adox rbp, r10
0053256D  48 8B 51 28                     mov rdx, qword ptr [rcx + 0x28]
00532571  4D 89 60 28                     mov qword ptr [r8 + 0x28], r12
00532575  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053257B  66 48 0F 38 F6 E8               adcx rbp, rax
00532581  66 49 0F 38 F6 DA               adcx rbx, r10
00532587  48 8B 51 18                     mov rdx, qword ptr [rcx + 0x18]
0053258B  4D 89 68 30                     mov qword ptr [r8 + 0x30], r13
0053258F  48 33 C0                        xor rax, rax
00532592  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532598  66 4C 0F 38 F6 F0               adcx r14, rax
0053259E  F3 4D 0F 38 F6 DA               adox r11, r10
005325A4  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
005325AA  66 4C 0F 38 F6 D8               adcx r11, rax
005325B0  F3 49 0F 38 F6 F2               adox rsi, r10
005325B6  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
005325BC  66 48 0F 38 F6 F0               adcx rsi, rax
005325C2  F3 49 0F 38 F6 FA               adox rdi, r10
005325C8  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
005325CE  66 48 0F 38 F6 F8               adcx rdi, rax
005325D4  F3 49 0F 38 F6 EA               adox rbp, r10
005325DA  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
005325DE  49 C7 C4 00 00 00 00            mov r12, 0
005325E5  49 C7 C5 00 00 00 00            mov r13, 0
005325EC  4D 89 70 38                     mov qword ptr [r8 + 0x38], r14
005325F0  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
005325F6  66 48 0F 38 F6 E8               adcx rbp, rax
005325FC  F3 49 0F 38 F6 DA               adox rbx, r10
00532602  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532608  66 48 0F 38 F6 D8               adcx rbx, rax
0053260E  F3 4D 0F 38 F6 E2               adox r12, r10
00532614  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053261A  66 4C 0F 38 F6 E0               adcx r12, rax
00532620  66 4D 0F 38 F6 EA               adcx r13, r10
00532626  4D 33 F6                        xor r14, r14
00532629  4C 8D 49 40                     lea r9, [rcx + 0x40]
0053262D  4D 8D 40 40                     lea r8, [r8 + 0x40]
00532631  48 33 C0                        xor rax, rax
00532634  49 8B 11                        mov rdx, qword ptr [r9]
00532637  F3 4D 0F 38 F6 18               adox r11, qword ptr [r8]
0053263D  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
00532642  66 4C 0F 38 F6 D8               adcx r11, rax
00532648  F3 49 0F 38 F6 F2               adox rsi, r10
0053264E  4D 89 18                        mov qword ptr [r8], r11
00532651  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
00532657  66 48 0F 38 F6 F0               adcx rsi, rax
0053265D  F3 49 0F 38 F6 FA               adox rdi, r10
00532663  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532669  66 48 0F 38 F6 F8               adcx rdi, rax
0053266F  F3 49 0F 38 F6 EA               adox rbp, r10
00532675  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
0053267B  66 48 0F 38 F6 E8               adcx rbp, rax
00532681  F3 49 0F 38 F6 DA               adox rbx, r10
00532687  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
0053268D  66 48 0F 38 F6 D8               adcx rbx, rax
00532693  F3 4D 0F 38 F6 E2               adox r12, r10
00532699  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
0053269F  66 4C 0F 38 F6 E0               adcx r12, rax
005326A5  F3 4D 0F 38 F6 EA               adox r13, r10
005326AB  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
005326B1  66 4C 0F 38 F6 E8               adcx r13, rax
005326B7  F3 4D 0F 38 F6 F2               adox r14, r10
005326BD  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
005326C3  66 4C 0F 38 F6 F0               adcx r14, rax
005326C9  49 C7 C3 00 00 00 00            mov r11, 0
005326D0  F3 4D 0F 38 F6 DB               adox r11, r11
005326D6  66 4D 0F 38 F6 DA               adcx r11, r10
005326DC  48 33 C0                        xor rax, rax
005326DF  49 8B 51 08                     mov rdx, qword ptr [r9 + 8]
005326E3  F3 49 0F 38 F6 70 08            adox rsi, qword ptr [r8 + 8]
005326EA  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
005326EF  66 48 0F 38 F6 F0               adcx rsi, rax
005326F5  F3 49 0F 38 F6 FA               adox rdi, r10
005326FB  49 89 70 08                     mov qword ptr [r8 + 8], rsi
005326FF  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
00532705  66 48 0F 38 F6 F8               adcx rdi, rax
0053270B  F3 49 0F 38 F6 EA               adox rbp, r10
00532711  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532717  66 48 0F 38 F6 E8               adcx rbp, rax
0053271D  F3 49 0F 38 F6 DA               adox rbx, r10
00532723  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532729  66 48 0F 38 F6 D8               adcx rbx, rax
0053272F  F3 4D 0F 38 F6 E2               adox r12, r10
00532735  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
0053273B  66 4C 0F 38 F6 E0               adcx r12, rax
00532741  F3 4D 0F 38 F6 EA               adox r13, r10
00532747  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
0053274D  66 4C 0F 38 F6 E8               adcx r13, rax
00532753  F3 4D 0F 38 F6 F2               adox r14, r10
00532759  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053275F  66 4C 0F 38 F6 F0               adcx r14, rax
00532765  F3 4D 0F 38 F6 DA               adox r11, r10
0053276B  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
00532771  66 4C 0F 38 F6 D8               adcx r11, rax
00532777  48 C7 C6 00 00 00 00            mov rsi, 0
0053277E  F3 48 0F 38 F6 F6               adox rsi, rsi
00532784  66 49 0F 38 F6 F2               adcx rsi, r10
0053278A  48 33 C0                        xor rax, rax
0053278D  49 8B 51 10                     mov rdx, qword ptr [r9 + 0x10]
00532791  F3 49 0F 38 F6 78 10            adox rdi, qword ptr [r8 + 0x10]
00532798  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
0053279D  66 48 0F 38 F6 F8               adcx rdi, rax
005327A3  F3 49 0F 38 F6 EA               adox rbp, r10
005327A9  49 89 78 10                     mov qword ptr [r8 + 0x10], rdi
005327AD  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
005327B3  66 48 0F 38 F6 E8               adcx rbp, rax
005327B9  F3 49 0F 38 F6 DA               adox rbx, r10
005327BF  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
005327C5  66 48 0F 38 F6 D8               adcx rbx, rax
005327CB  F3 4D 0F 38 F6 E2               adox r12, r10
005327D1  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
005327D7  66 4C 0F 38 F6 E0               adcx r12, rax
005327DD  F3 4D 0F 38 F6 EA               adox r13, r10
005327E3  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
005327E9  66 4C 0F 38 F6 E8               adcx r13, rax
005327EF  F3 4D 0F 38 F6 F2               adox r14, r10
005327F5  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
005327FB  66 4C 0F 38 F6 F0               adcx r14, rax
00532801  F3 4D 0F 38 F6 DA               adox r11, r10
00532807  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
0053280D  66 4C 0F 38 F6 D8               adcx r11, rax
00532813  F3 49 0F 38 F6 F2               adox rsi, r10
00532819  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
0053281F  66 48 0F 38 F6 F0               adcx rsi, rax
00532825  48 C7 C7 00 00 00 00            mov rdi, 0
0053282C  F3 48 0F 38 F6 FF               adox rdi, rdi
00532832  66 49 0F 38 F6 FA               adcx rdi, r10
00532838  48 33 C0                        xor rax, rax
0053283B  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
0053283F  F3 49 0F 38 F6 68 18            adox rbp, qword ptr [r8 + 0x18]
00532846  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
0053284B  66 48 0F 38 F6 E8               adcx rbp, rax
00532851  F3 49 0F 38 F6 DA               adox rbx, r10
00532857  49 89 68 18                     mov qword ptr [r8 + 0x18], rbp
0053285B  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
00532861  66 48 0F 38 F6 D8               adcx rbx, rax
00532867  F3 4D 0F 38 F6 E2               adox r12, r10
0053286D  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532873  66 4C 0F 38 F6 E0               adcx r12, rax
00532879  F3 4D 0F 38 F6 EA               adox r13, r10
0053287F  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532885  66 4C 0F 38 F6 E8               adcx r13, rax
0053288B  F3 4D 0F 38 F6 F2               adox r14, r10
00532891  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532897  66 4C 0F 38 F6 F0               adcx r14, rax
0053289D  F3 4D 0F 38 F6 DA               adox r11, r10
005328A3  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
005328A9  66 4C 0F 38 F6 D8               adcx r11, rax
005328AF  F3 49 0F 38 F6 F2               adox rsi, r10
005328B5  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
005328BB  66 48 0F 38 F6 F0               adcx rsi, rax
005328C1  F3 49 0F 38 F6 FA               adox rdi, r10
005328C7  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
005328CD  66 48 0F 38 F6 F8               adcx rdi, rax
005328D3  48 C7 C5 00 00 00 00            mov rbp, 0
005328DA  F3 48 0F 38 F6 ED               adox rbp, rbp
005328E0  66 49 0F 38 F6 EA               adcx rbp, r10
005328E6  48 33 C0                        xor rax, rax
005328E9  49 8B 51 20                     mov rdx, qword ptr [r9 + 0x20]
005328ED  F3 49 0F 38 F6 58 20            adox rbx, qword ptr [r8 + 0x20]
005328F4  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
005328F9  66 48 0F 38 F6 D8               adcx rbx, rax
005328FF  F3 4D 0F 38 F6 E2               adox r12, r10
00532905  49 89 58 20                     mov qword ptr [r8 + 0x20], rbx
00532909  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
0053290F  66 4C 0F 38 F6 E0               adcx r12, rax
00532915  F3 4D 0F 38 F6 EA               adox r13, r10
0053291B  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532921  66 4C 0F 38 F6 E8               adcx r13, rax
00532927  F3 4D 0F 38 F6 F2               adox r14, r10
0053292D  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532933  66 4C 0F 38 F6 F0               adcx r14, rax
00532939  F3 4D 0F 38 F6 DA               adox r11, r10
0053293F  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532945  66 4C 0F 38 F6 D8               adcx r11, rax
0053294B  F3 49 0F 38 F6 F2               adox rsi, r10
00532951  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532957  66 48 0F 38 F6 F0               adcx rsi, rax
0053295D  F3 49 0F 38 F6 FA               adox rdi, r10
00532963  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
00532969  66 48 0F 38 F6 F8               adcx rdi, rax
0053296F  F3 49 0F 38 F6 EA               adox rbp, r10
00532975  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
0053297B  66 48 0F 38 F6 E8               adcx rbp, rax
00532981  48 C7 C3 00 00 00 00            mov rbx, 0
00532988  F3 48 0F 38 F6 DB               adox rbx, rbx
0053298E  66 49 0F 38 F6 DA               adcx rbx, r10
00532994  48 33 C0                        xor rax, rax
00532997  49 8B 51 28                     mov rdx, qword ptr [r9 + 0x28]
0053299B  F3 4D 0F 38 F6 60 28            adox r12, qword ptr [r8 + 0x28]
005329A2  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
005329A7  66 4C 0F 38 F6 E0               adcx r12, rax
005329AD  F3 4D 0F 38 F6 EA               adox r13, r10
005329B3  4D 89 60 28                     mov qword ptr [r8 + 0x28], r12
005329B7  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
005329BD  66 4C 0F 38 F6 E8               adcx r13, rax
005329C3  F3 4D 0F 38 F6 F2               adox r14, r10
005329C9  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
005329CF  66 4C 0F 38 F6 F0               adcx r14, rax
005329D5  F3 4D 0F 38 F6 DA               adox r11, r10
005329DB  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
005329E1  66 4C 0F 38 F6 D8               adcx r11, rax
005329E7  F3 49 0F 38 F6 F2               adox rsi, r10
005329ED  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
005329F3  66 48 0F 38 F6 F0               adcx rsi, rax
005329F9  F3 49 0F 38 F6 FA               adox rdi, r10
005329FF  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532A05  66 48 0F 38 F6 F8               adcx rdi, rax
00532A0B  F3 49 0F 38 F6 EA               adox rbp, r10
00532A11  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
00532A17  66 48 0F 38 F6 E8               adcx rbp, rax
00532A1D  F3 49 0F 38 F6 DA               adox rbx, r10
00532A23  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
00532A29  66 48 0F 38 F6 D8               adcx rbx, rax
00532A2F  49 C7 C4 00 00 00 00            mov r12, 0
00532A36  F3 4D 0F 38 F6 E4               adox r12, r12
00532A3C  66 4D 0F 38 F6 E2               adcx r12, r10
00532A42  48 33 C0                        xor rax, rax
00532A45  49 8B 51 30                     mov rdx, qword ptr [r9 + 0x30]
00532A49  F3 4D 0F 38 F6 68 30            adox r13, qword ptr [r8 + 0x30]
00532A50  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
00532A55  66 4C 0F 38 F6 E8               adcx r13, rax
00532A5B  F3 4D 0F 38 F6 F2               adox r14, r10
00532A61  4D 89 68 30                     mov qword ptr [r8 + 0x30], r13
00532A65  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
00532A6B  66 4C 0F 38 F6 F0               adcx r14, rax
00532A71  F3 4D 0F 38 F6 DA               adox r11, r10
00532A77  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532A7D  66 4C 0F 38 F6 D8               adcx r11, rax
00532A83  F3 49 0F 38 F6 F2               adox rsi, r10
00532A89  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532A8F  66 48 0F 38 F6 F0               adcx rsi, rax
00532A95  F3 49 0F 38 F6 FA               adox rdi, r10
00532A9B  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532AA1  66 48 0F 38 F6 F8               adcx rdi, rax
00532AA7  F3 49 0F 38 F6 EA               adox rbp, r10
00532AAD  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532AB3  66 48 0F 38 F6 E8               adcx rbp, rax
00532AB9  F3 49 0F 38 F6 DA               adox rbx, r10
00532ABF  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
00532AC5  66 48 0F 38 F6 D8               adcx rbx, rax
00532ACB  F3 4D 0F 38 F6 E2               adox r12, r10
00532AD1  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
00532AD7  66 4C 0F 38 F6 E0               adcx r12, rax
00532ADD  49 C7 C5 00 00 00 00            mov r13, 0
00532AE4  F3 4D 0F 38 F6 ED               adox r13, r13
00532AEA  66 4D 0F 38 F6 EA               adcx r13, r10
00532AF0  48 33 C0                        xor rax, rax
00532AF3  49 8B 51 38                     mov rdx, qword ptr [r9 + 0x38]
00532AF7  F3 4D 0F 38 F6 70 38            adox r14, qword ptr [r8 + 0x38]
00532AFE  C4 62 FB F6 11                  mulx r10, rax, qword ptr [rcx]
00532B03  66 4C 0F 38 F6 F0               adcx r14, rax
00532B09  F3 4D 0F 38 F6 DA               adox r11, r10
00532B0F  4D 89 70 38                     mov qword ptr [r8 + 0x38], r14
00532B13  C4 62 FB F6 51 08               mulx r10, rax, qword ptr [rcx + 8]
00532B19  66 4C 0F 38 F6 D8               adcx r11, rax
00532B1F  F3 49 0F 38 F6 F2               adox rsi, r10
00532B25  C4 62 FB F6 51 10               mulx r10, rax, qword ptr [rcx + 0x10]
00532B2B  66 48 0F 38 F6 F0               adcx rsi, rax
00532B31  F3 49 0F 38 F6 FA               adox rdi, r10
00532B37  C4 62 FB F6 51 18               mulx r10, rax, qword ptr [rcx + 0x18]
00532B3D  66 48 0F 38 F6 F8               adcx rdi, rax
00532B43  F3 49 0F 38 F6 EA               adox rbp, r10
00532B49  C4 62 FB F6 51 20               mulx r10, rax, qword ptr [rcx + 0x20]
00532B4F  66 48 0F 38 F6 E8               adcx rbp, rax
00532B55  F3 49 0F 38 F6 DA               adox rbx, r10
00532B5B  C4 62 FB F6 51 28               mulx r10, rax, qword ptr [rcx + 0x28]
00532B61  66 48 0F 38 F6 D8               adcx rbx, rax
00532B67  F3 4D 0F 38 F6 E2               adox r12, r10
00532B6D  C4 62 FB F6 51 30               mulx r10, rax, qword ptr [rcx + 0x30]
00532B73  66 4C 0F 38 F6 E0               adcx r12, rax
00532B79  F3 4D 0F 38 F6 EA               adox r13, r10
00532B7F  C4 62 FB F6 51 38               mulx r10, rax, qword ptr [rcx + 0x38]
00532B85  66 4C 0F 38 F6 E8               adcx r13, rax
00532B8B  49 C7 C6 00 00 00 00            mov r14, 0
00532B92  F3 4D 0F 38 F6 F6               adox r14, r14
00532B98  66 4D 0F 38 F6 F2               adcx r14, r10
00532B9E  49 83 C0 40                     add r8, 0x40
00532BA2  4D 89 18                        mov qword ptr [r8], r11
00532BA5  49 89 70 08                     mov qword ptr [r8 + 8], rsi
00532BA9  49 89 78 10                     mov qword ptr [r8 + 0x10], rdi
00532BAD  49 89 68 18                     mov qword ptr [r8 + 0x18], rbp
00532BB1  49 89 58 20                     mov qword ptr [r8 + 0x20], rbx
00532BB5  4D 89 60 28                     mov qword ptr [r8 + 0x28], r12
00532BB9  4D 89 68 30                     mov qword ptr [r8 + 0x30], r13
00532BBD  4D 89 70 38                     mov qword ptr [r8 + 0x38], r14
00532BC1  48 33 C0                        xor rax, rax
00532BC4  49 8B 11                        mov rdx, qword ptr [r9]
00532BC7  49 8B 70 08                     mov rsi, qword ptr [r8 + 8]
00532BCB  49 8B 78 10                     mov rdi, qword ptr [r8 + 0x10]
00532BCF  49 8B 68 18                     mov rbp, qword ptr [r8 + 0x18]
00532BD3  49 8B 58 20                     mov rbx, qword ptr [r8 + 0x20]
00532BD7  4D 8B 60 28                     mov r12, qword ptr [r8 + 0x28]
00532BDB  4D 8B 68 30                     mov r13, qword ptr [r8 + 0x30]
00532BDF  4D 8B 70 38                     mov r14, qword ptr [r8 + 0x38]
00532BE3  4D 33 DB                        xor r11, r11
00532BE6  C4 42 FB F6 51 08               mulx r10, rax, qword ptr [r9 + 8]
00532BEC  66 48 0F 38 F6 F0               adcx rsi, rax
00532BF2  F3 49 0F 38 F6 FA               adox rdi, r10
00532BF8  C4 42 FB F6 51 10               mulx r10, rax, qword ptr [r9 + 0x10]
00532BFE  66 48 0F 38 F6 F8               adcx rdi, rax
00532C04  F3 49 0F 38 F6 EA               adox rbp, r10
00532C0A  C4 42 FB F6 51 18               mulx r10, rax, qword ptr [r9 + 0x18]
00532C10  66 48 0F 38 F6 E8               adcx rbp, rax
00532C16  F3 49 0F 38 F6 DA               adox rbx, r10
00532C1C  C4 42 FB F6 51 20               mulx r10, rax, qword ptr [r9 + 0x20]
00532C22  66 48 0F 38 F6 D8               adcx rbx, rax
00532C28  F3 4D 0F 38 F6 E2               adox r12, r10
00532C2E  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532C34  66 4C 0F 38 F6 E0               adcx r12, rax
00532C3A  F3 4D 0F 38 F6 EA               adox r13, r10
00532C40  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532C46  66 4C 0F 38 F6 E8               adcx r13, rax
00532C4C  F3 4D 0F 38 F6 F2               adox r14, r10
00532C52  C4 42 FB F6 51 38               mulx r10, rax, qword ptr [r9 + 0x38]
00532C58  66 4C 0F 38 F6 F0               adcx r14, rax
00532C5E  49 89 70 08                     mov qword ptr [r8 + 8], rsi
00532C62  F3 4D 0F 38 F6 DB               adox r11, r11
00532C68  66 4D 0F 38 F6 DA               adcx r11, r10
00532C6E  49 89 78 10                     mov qword ptr [r8 + 0x10], rdi
00532C72  49 8B 51 08                     mov rdx, qword ptr [r9 + 8]
00532C76  48 33 C0                        xor rax, rax
00532C79  C4 42 FB F6 51 10               mulx r10, rax, qword ptr [r9 + 0x10]
00532C7F  66 48 0F 38 F6 E8               adcx rbp, rax
00532C85  F3 49 0F 38 F6 DA               adox rbx, r10
00532C8B  C4 42 FB F6 51 18               mulx r10, rax, qword ptr [r9 + 0x18]
00532C91  66 48 0F 38 F6 D8               adcx rbx, rax
00532C97  F3 4D 0F 38 F6 E2               adox r12, r10
00532C9D  C4 42 FB F6 51 20               mulx r10, rax, qword ptr [r9 + 0x20]
00532CA3  66 4C 0F 38 F6 E0               adcx r12, rax
00532CA9  F3 4D 0F 38 F6 EA               adox r13, r10
00532CAF  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532CB5  66 4C 0F 38 F6 E8               adcx r13, rax
00532CBB  F3 4D 0F 38 F6 F2               adox r14, r10
00532CC1  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532CC7  66 4C 0F 38 F6 F0               adcx r14, rax
00532CCD  F3 4D 0F 38 F6 DA               adox r11, r10
00532CD3  49 8B 51 38                     mov rdx, qword ptr [r9 + 0x38]
00532CD7  48 C7 C6 00 00 00 00            mov rsi, 0
00532CDE  48 C7 C7 00 00 00 00            mov rdi, 0
00532CE5  49 89 68 18                     mov qword ptr [r8 + 0x18], rbp
00532CE9  C4 42 FB F6 51 08               mulx r10, rax, qword ptr [r9 + 8]
00532CEF  66 4C 0F 38 F6 D8               adcx r11, rax
00532CF5  F3 49 0F 38 F6 F2               adox rsi, r10
00532CFB  C4 42 FB F6 51 10               mulx r10, rax, qword ptr [r9 + 0x10]
00532D01  66 48 0F 38 F6 F0               adcx rsi, rax
00532D07  49 89 58 20                     mov qword ptr [r8 + 0x20], rbx
00532D0B  66 49 0F 38 F6 FA               adcx rdi, r10
00532D11  49 8B 51 10                     mov rdx, qword ptr [r9 + 0x10]
00532D15  48 33 C0                        xor rax, rax
00532D18  C4 42 FB F6 51 18               mulx r10, rax, qword ptr [r9 + 0x18]
00532D1E  66 4C 0F 38 F6 E0               adcx r12, rax
00532D24  F3 4D 0F 38 F6 EA               adox r13, r10
00532D2A  C4 42 FB F6 51 20               mulx r10, rax, qword ptr [r9 + 0x20]
00532D30  66 4C 0F 38 F6 E8               adcx r13, rax
00532D36  F3 4D 0F 38 F6 F2               adox r14, r10
00532D3C  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532D42  66 4C 0F 38 F6 F0               adcx r14, rax
00532D48  F3 4D 0F 38 F6 DA               adox r11, r10
00532D4E  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532D54  66 4C 0F 38 F6 D8               adcx r11, rax
00532D5A  F3 49 0F 38 F6 F2               adox rsi, r10
00532D60  49 8B 51 20                     mov rdx, qword ptr [r9 + 0x20]
00532D64  48 C7 C5 00 00 00 00            mov rbp, 0
00532D6B  48 C7 C3 00 00 00 00            mov rbx, 0
00532D72  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532D78  66 48 0F 38 F6 F0               adcx rsi, rax
00532D7E  F3 49 0F 38 F6 FA               adox rdi, r10
00532D84  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532D8A  66 48 0F 38 F6 F8               adcx rdi, rax
00532D90  F3 49 0F 38 F6 EA               adox rbp, r10
00532D96  49 8B 51 28                     mov rdx, qword ptr [r9 + 0x28]
00532D9A  4D 89 60 28                     mov qword ptr [r8 + 0x28], r12
00532D9E  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532DA4  66 48 0F 38 F6 E8               adcx rbp, rax
00532DAA  66 49 0F 38 F6 DA               adcx rbx, r10
00532DB0  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
00532DB4  4D 89 68 30                     mov qword ptr [r8 + 0x30], r13
00532DB8  48 33 C0                        xor rax, rax
00532DBB  C4 42 FB F6 51 20               mulx r10, rax, qword ptr [r9 + 0x20]
00532DC1  66 4C 0F 38 F6 F0               adcx r14, rax
00532DC7  F3 4D 0F 38 F6 DA               adox r11, r10
00532DCD  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532DD3  66 4C 0F 38 F6 D8               adcx r11, rax
00532DD9  F3 49 0F 38 F6 F2               adox rsi, r10
00532DDF  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532DE5  66 48 0F 38 F6 F0               adcx rsi, rax
00532DEB  F3 49 0F 38 F6 FA               adox rdi, r10
00532DF1  C4 42 FB F6 51 38               mulx r10, rax, qword ptr [r9 + 0x38]
00532DF7  66 48 0F 38 F6 F8               adcx rdi, rax
00532DFD  F3 49 0F 38 F6 EA               adox rbp, r10
00532E03  49 8B 51 38                     mov rdx, qword ptr [r9 + 0x38]
00532E07  49 C7 C4 00 00 00 00            mov r12, 0
00532E0E  49 C7 C5 00 00 00 00            mov r13, 0
00532E15  4D 89 70 38                     mov qword ptr [r8 + 0x38], r14
00532E19  C4 42 FB F6 51 20               mulx r10, rax, qword ptr [r9 + 0x20]
00532E1F  66 48 0F 38 F6 E8               adcx rbp, rax
00532E25  F3 49 0F 38 F6 DA               adox rbx, r10
00532E2B  C4 42 FB F6 51 28               mulx r10, rax, qword ptr [r9 + 0x28]
00532E31  66 48 0F 38 F6 D8               adcx rbx, rax
00532E37  F3 4D 0F 38 F6 E2               adox r12, r10
00532E3D  C4 42 FB F6 51 30               mulx r10, rax, qword ptr [r9 + 0x30]
00532E43  66 4C 0F 38 F6 E0               adcx r12, rax
00532E49  66 4D 0F 38 F6 EA               adcx r13, r10
00532E4F  4D 33 F6                        xor r14, r14
00532E52  4D 89 58 40                     mov qword ptr [r8 + 0x40], r11
00532E56  49 89 70 48                     mov qword ptr [r8 + 0x48], rsi
00532E5A  49 89 78 50                     mov qword ptr [r8 + 0x50], rdi
00532E5E  49 89 68 58                     mov qword ptr [r8 + 0x58], rbp
00532E62  49 89 58 60                     mov qword ptr [r8 + 0x60], rbx
00532E66  4D 89 60 68                     mov qword ptr [r8 + 0x68], r12
00532E6A  4D 89 68 70                     mov qword ptr [r8 + 0x70], r13
00532E6E  4D 89 70 78                     mov qword ptr [r8 + 0x78], r14
00532E72  49 81 E8 80 00 00 00            sub r8, 0x80
00532E79  48 8B 11                        mov rdx, qword ptr [rcx]
00532E7C  49 8B 00                        mov rax, qword ptr [r8]
00532E7F  4D 8B 50 08                     mov r10, qword ptr [r8 + 8]
00532E83  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532E88  66 4C 0F 38 F6 C8               adcx r9, rax
00532E8E  F3 4C 0F 38 F6 C8               adox r9, rax
00532E94  66 4D 0F 38 F6 DA               adcx r11, r10
00532E9A  F3 4D 0F 38 F6 DA               adox r11, r10
00532EA0  4D 89 08                        mov qword ptr [r8], r9
00532EA3  4D 89 58 08                     mov qword ptr [r8 + 8], r11
00532EA7  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00532EAB  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00532EAF  4D 8B 50 18                     mov r10, qword ptr [r8 + 0x18]
00532EB3  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532EB8  66 4C 0F 38 F6 C8               adcx r9, rax
00532EBE  F3 4C 0F 38 F6 C8               adox r9, rax
00532EC4  66 4D 0F 38 F6 DA               adcx r11, r10
00532ECA  F3 4D 0F 38 F6 DA               adox r11, r10
00532ED0  4D 89 48 10                     mov qword ptr [r8 + 0x10], r9
00532ED4  4D 89 58 18                     mov qword ptr [r8 + 0x18], r11
00532ED8  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00532EDC  49 8B 40 20                     mov rax, qword ptr [r8 + 0x20]
00532EE0  4D 8B 50 28                     mov r10, qword ptr [r8 + 0x28]
00532EE4  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532EE9  66 4C 0F 38 F6 C8               adcx r9, rax
00532EEF  F3 4C 0F 38 F6 C8               adox r9, rax
00532EF5  66 4D 0F 38 F6 DA               adcx r11, r10
00532EFB  F3 4D 0F 38 F6 DA               adox r11, r10
00532F01  4D 89 48 20                     mov qword ptr [r8 + 0x20], r9
00532F05  4D 89 58 28                     mov qword ptr [r8 + 0x28], r11
00532F09  48 8B 51 18                     mov rdx, qword ptr [rcx + 0x18]
00532F0D  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00532F11  4D 8B 50 38                     mov r10, qword ptr [r8 + 0x38]
00532F15  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532F1A  66 4C 0F 38 F6 C8               adcx r9, rax
00532F20  F3 4C 0F 38 F6 C8               adox r9, rax
00532F26  66 4D 0F 38 F6 DA               adcx r11, r10
00532F2C  F3 4D 0F 38 F6 DA               adox r11, r10
00532F32  4D 89 48 30                     mov qword ptr [r8 + 0x30], r9
00532F36  4D 89 58 38                     mov qword ptr [r8 + 0x38], r11
00532F3A  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
00532F3E  49 8B 40 40                     mov rax, qword ptr [r8 + 0x40]
00532F42  4D 8B 50 48                     mov r10, qword ptr [r8 + 0x48]
00532F46  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532F4B  66 4C 0F 38 F6 C8               adcx r9, rax
00532F51  F3 4C 0F 38 F6 C8               adox r9, rax
00532F57  66 4D 0F 38 F6 DA               adcx r11, r10
00532F5D  F3 4D 0F 38 F6 DA               adox r11, r10
00532F63  4D 89 48 40                     mov qword ptr [r8 + 0x40], r9
00532F67  4D 89 58 48                     mov qword ptr [r8 + 0x48], r11
00532F6B  48 8B 51 28                     mov rdx, qword ptr [rcx + 0x28]
00532F6F  49 8B 40 50                     mov rax, qword ptr [r8 + 0x50]
00532F73  4D 8B 50 58                     mov r10, qword ptr [r8 + 0x58]
00532F77  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532F7C  66 4C 0F 38 F6 C8               adcx r9, rax
00532F82  F3 4C 0F 38 F6 C8               adox r9, rax
00532F88  66 4D 0F 38 F6 DA               adcx r11, r10
00532F8E  F3 4D 0F 38 F6 DA               adox r11, r10
00532F94  4D 89 48 50                     mov qword ptr [r8 + 0x50], r9
00532F98  4D 89 58 58                     mov qword ptr [r8 + 0x58], r11
00532F9C  48 8B 51 30                     mov rdx, qword ptr [rcx + 0x30]
00532FA0  49 8B 40 60                     mov rax, qword ptr [r8 + 0x60]
00532FA4  4D 8B 50 68                     mov r10, qword ptr [r8 + 0x68]
00532FA8  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532FAD  66 4C 0F 38 F6 C8               adcx r9, rax
00532FB3  F3 4C 0F 38 F6 C8               adox r9, rax
00532FB9  66 4D 0F 38 F6 DA               adcx r11, r10
00532FBF  F3 4D 0F 38 F6 DA               adox r11, r10
00532FC5  4D 89 48 60                     mov qword ptr [r8 + 0x60], r9
00532FC9  4D 89 58 68                     mov qword ptr [r8 + 0x68], r11
00532FCD  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
00532FD1  49 8B 40 70                     mov rax, qword ptr [r8 + 0x70]
00532FD5  4D 8B 50 78                     mov r10, qword ptr [r8 + 0x78]
00532FD9  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00532FDE  66 4C 0F 38 F6 C8               adcx r9, rax
00532FE4  F3 4C 0F 38 F6 C8               adox r9, rax
00532FEA  66 4D 0F 38 F6 DA               adcx r11, r10
00532FF0  F3 4D 0F 38 F6 DA               adox r11, r10
00532FF6  4D 89 48 70                     mov qword ptr [r8 + 0x70], r9
00532FFA  4D 89 58 78                     mov qword ptr [r8 + 0x78], r11
00532FFE  48 8B 51 40                     mov rdx, qword ptr [rcx + 0x40]
00533002  49 8B 80 80 00 00 00            mov rax, qword ptr [r8 + 0x80]
00533009  4D 8B 90 88 00 00 00            mov r10, qword ptr [r8 + 0x88]
00533010  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00533015  66 4C 0F 38 F6 C8               adcx r9, rax
0053301B  F3 4C 0F 38 F6 C8               adox r9, rax
00533021  66 4D 0F 38 F6 DA               adcx r11, r10
00533027  F3 4D 0F 38 F6 DA               adox r11, r10
0053302D  4D 89 88 80 00 00 00            mov qword ptr [r8 + 0x80], r9
00533034  4D 89 98 88 00 00 00            mov qword ptr [r8 + 0x88], r11
0053303B  48 8B 51 48                     mov rdx, qword ptr [rcx + 0x48]
0053303F  49 8B 80 90 00 00 00            mov rax, qword ptr [r8 + 0x90]
00533046  4D 8B 90 98 00 00 00            mov r10, qword ptr [r8 + 0x98]
0053304D  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00533052  66 4C 0F 38 F6 C8               adcx r9, rax
00533058  F3 4C 0F 38 F6 C8               adox r9, rax
0053305E  66 4D 0F 38 F6 DA               adcx r11, r10
00533064  F3 4D 0F 38 F6 DA               adox r11, r10
0053306A  4D 89 88 90 00 00 00            mov qword ptr [r8 + 0x90], r9
00533071  4D 89 98 98 00 00 00            mov qword ptr [r8 + 0x98], r11
00533078  48 8B 51 50                     mov rdx, qword ptr [rcx + 0x50]
0053307C  49 8B 80 A0 00 00 00            mov rax, qword ptr [r8 + 0xa0]
00533083  4D 8B 90 A8 00 00 00            mov r10, qword ptr [r8 + 0xa8]
0053308A  C4 62 B3 F6 DA                  mulx r11, r9, rdx
0053308F  66 4C 0F 38 F6 C8               adcx r9, rax
00533095  F3 4C 0F 38 F6 C8               adox r9, rax
0053309B  66 4D 0F 38 F6 DA               adcx r11, r10
005330A1  F3 4D 0F 38 F6 DA               adox r11, r10
005330A7  4D 89 88 A0 00 00 00            mov qword ptr [r8 + 0xa0], r9
005330AE  4D 89 98 A8 00 00 00            mov qword ptr [r8 + 0xa8], r11
005330B5  48 8B 51 58                     mov rdx, qword ptr [rcx + 0x58]
005330B9  49 8B 80 B0 00 00 00            mov rax, qword ptr [r8 + 0xb0]
005330C0  4D 8B 90 B8 00 00 00            mov r10, qword ptr [r8 + 0xb8]
005330C7  C4 62 B3 F6 DA                  mulx r11, r9, rdx
005330CC  66 4C 0F 38 F6 C8               adcx r9, rax
005330D2  F3 4C 0F 38 F6 C8               adox r9, rax
005330D8  66 4D 0F 38 F6 DA               adcx r11, r10
005330DE  F3 4D 0F 38 F6 DA               adox r11, r10
005330E4  4D 89 88 B0 00 00 00            mov qword ptr [r8 + 0xb0], r9
005330EB  4D 89 98 B8 00 00 00            mov qword ptr [r8 + 0xb8], r11
005330F2  48 8B 51 60                     mov rdx, qword ptr [rcx + 0x60]
005330F6  49 8B 80 C0 00 00 00            mov rax, qword ptr [r8 + 0xc0]
005330FD  4D 8B 90 C8 00 00 00            mov r10, qword ptr [r8 + 0xc8]
00533104  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00533109  66 4C 0F 38 F6 C8               adcx r9, rax
0053310F  F3 4C 0F 38 F6 C8               adox r9, rax
00533115  66 4D 0F 38 F6 DA               adcx r11, r10
0053311B  F3 4D 0F 38 F6 DA               adox r11, r10
00533121  4D 89 88 C0 00 00 00            mov qword ptr [r8 + 0xc0], r9
00533128  4D 89 98 C8 00 00 00            mov qword ptr [r8 + 0xc8], r11
0053312F  48 8B 51 68                     mov rdx, qword ptr [rcx + 0x68]
00533133  49 8B 80 D0 00 00 00            mov rax, qword ptr [r8 + 0xd0]
0053313A  4D 8B 90 D8 00 00 00            mov r10, qword ptr [r8 + 0xd8]
00533141  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00533146  66 4C 0F 38 F6 C8               adcx r9, rax
0053314C  F3 4C 0F 38 F6 C8               adox r9, rax
00533152  66 4D 0F 38 F6 DA               adcx r11, r10
00533158  F3 4D 0F 38 F6 DA               adox r11, r10
0053315E  4D 89 88 D0 00 00 00            mov qword ptr [r8 + 0xd0], r9
00533165  4D 89 98 D8 00 00 00            mov qword ptr [r8 + 0xd8], r11
0053316C  48 8B 51 70                     mov rdx, qword ptr [rcx + 0x70]
00533170  49 8B 80 E0 00 00 00            mov rax, qword ptr [r8 + 0xe0]
00533177  4D 8B 90 E8 00 00 00            mov r10, qword ptr [r8 + 0xe8]
0053317E  C4 62 B3 F6 DA                  mulx r11, r9, rdx
00533183  66 4C 0F 38 F6 C8               adcx r9, rax
00533189  F3 4C 0F 38 F6 C8               adox r9, rax
0053318F  66 4D 0F 38 F6 DA               adcx r11, r10
00533195  F3 4D 0F 38 F6 DA               adox r11, r10
0053319B  4D 89 88 E0 00 00 00            mov qword ptr [r8 + 0xe0], r9
005331A2  4D 89 98 E8 00 00 00            mov qword ptr [r8 + 0xe8], r11
005331A9  48 8B 51 78                     mov rdx, qword ptr [rcx + 0x78]
005331AD  49 8B 80 F0 00 00 00            mov rax, qword ptr [r8 + 0xf0]
005331B4  4D 8B 90 F8 00 00 00            mov r10, qword ptr [r8 + 0xf8]
005331BB  C4 62 B3 F6 DA                  mulx r11, r9, rdx
005331C0  66 4C 0F 38 F6 C8               adcx r9, rax
005331C6  F3 4C 0F 38 F6 C8               adox r9, rax
005331CC  66 4D 0F 38 F6 DA               adcx r11, r10
005331D2  F3 4D 0F 38 F6 DA               adox r11, r10
005331D8  4D 89 88 F0 00 00 00            mov qword ptr [r8 + 0xf0], r9
005331DF  4D 89 98 F8 00 00 00            mov qword ptr [r8 + 0xf8], r11
005331E6  41 5E                           pop r14
005331E8  41 5D                           pop r13
005331EA  41 5C                           pop r12
005331EC  5B                              pop rbx
005331ED  5D                              pop rbp
005331EE  5F                              pop rdi
005331EF  5E                              pop rsi
005331F0  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefRawSquareMulx1024(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;

    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm0;
    *(unsigned __int64 *)(a3 + 32) = v_xmm0;
    *(unsigned __int64 *)(a3 + 48) = v_xmm0;
    *(unsigned __int64 *)(a3 + 64) = v_xmm0;
    *(unsigned __int64 *)(a3 + 80) = v_xmm0;
    *(unsigned __int64 *)(a3 + 96) = v_xmm0;
    *(unsigned __int64 *)(a3 + 112) = v_xmm0;
    result = 0;
    v_r11 = 0;
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(a3 + 8);
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(a3 + 16);
    result = 0;
    *(unsigned __int64 *)(a3 + 24) = *(unsigned __int64 *)(a3 + 24);
    *(unsigned __int64 *)(a3 + 32) = *(unsigned __int64 *)(a3 + 32);
    result = 0;
    *(unsigned __int64 *)(a3 + 40) = *(unsigned __int64 *)(a3 + 40);
    *(unsigned __int64 *)(a3 + 48) = *(unsigned __int64 *)(a3 + 48);
    result = 0;
    *(unsigned __int64 *)(a3 + 56) = *(unsigned __int64 *)(a3 + 56);
    v_r14 = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 16) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 24) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 32) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 40) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 48) = 0;
    result = 0;
    *(unsigned __int64 *)(a3 + 64 + 56) = 0;
    a3 = (a3 + 64) + (64);
    *(unsigned __int64 *)(a3) = 0;
    *(unsigned __int64 *)(a3 + 8) = 0;
    *(unsigned __int64 *)(a3 + 16) = 0;
    *(unsigned __int64 *)(a3 + 24) = 0;
    *(unsigned __int64 *)(a3 + 32) = 0;
    *(unsigned __int64 *)(a3 + 40) = 0;
    *(unsigned __int64 *)(a3 + 48) = 0;
    *(unsigned __int64 *)(a3 + 56) = 0;
    result = 0;
    v_r11 = 0;
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(a3 + 8);
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(a3 + 16);
    result = 0;
    *(unsigned __int64 *)(a3 + 24) = *(unsigned __int64 *)(a3 + 24);
    *(unsigned __int64 *)(a3 + 32) = *(unsigned __int64 *)(a3 + 32);
    result = 0;
    *(unsigned __int64 *)(a3 + 40) = *(unsigned __int64 *)(a3 + 40);
    *(unsigned __int64 *)(a3 + 48) = *(unsigned __int64 *)(a3 + 48);
    result = 0;
    *(unsigned __int64 *)(a3 + 56) = *(unsigned __int64 *)(a3 + 56);
    v_r14 = 0;
    *(unsigned __int64 *)(a3 + 64) = 0;
    *(unsigned __int64 *)(a3 + 72) = 0;
    *(unsigned __int64 *)(a3 + 80) = 0;
    *(unsigned __int64 *)(a3 + 88) = 0;
    *(unsigned __int64 *)(a3 + 96) = 0;
    *(unsigned __int64 *)(a3 + 104) = 0;
    *(unsigned __int64 *)(a3 + 112) = 0;
    *(unsigned __int64 *)(a3 + 120) = 0;
    a3 = (a3) - (128);
    *(unsigned __int64 *)(a3) = a1 + 64;
    *(unsigned __int64 *)(a3 + 8) = 0;
    *(unsigned __int64 *)(a3 + 16) = a1 + 64;
    *(unsigned __int64 *)(a3 + 24) = 0;
    *(unsigned __int64 *)(a3 + 32) = a1 + 64;
    *(unsigned __int64 *)(a3 + 40) = 0;
    *(unsigned __int64 *)(a3 + 48) = a1 + 64;
    *(unsigned __int64 *)(a3 + 56) = 0;
    *(unsigned __int64 *)(a3 + 64) = a1 + 64;
    *(unsigned __int64 *)(a3 + 72) = 0;
    *(unsigned __int64 *)(a3 + 80) = a1 + 64;
    *(unsigned __int64 *)(a3 + 88) = 0;
    *(unsigned __int64 *)(a3 + 96) = a1 + 64;
    *(unsigned __int64 *)(a3 + 104) = 0;
    *(unsigned __int64 *)(a3 + 112) = a1 + 64;
    *(unsigned __int64 *)(a3 + 120) = 0;
    *(unsigned __int64 *)(a3 + 128) = a1 + 64;
    *(unsigned __int64 *)(a3 + 136) = 0;
    *(unsigned __int64 *)(a3 + 144) = a1 + 64;
    *(unsigned __int64 *)(a3 + 152) = 0;
    *(unsigned __int64 *)(a3 + 160) = a1 + 64;
    *(unsigned __int64 *)(a3 + 168) = 0;
    *(unsigned __int64 *)(a3 + 176) = a1 + 64;
    *(unsigned __int64 *)(a3 + 184) = 0;
    *(unsigned __int64 *)(a3 + 192) = a1 + 64;
    *(unsigned __int64 *)(a3 + 200) = 0;
    *(unsigned __int64 *)(a3 + 208) = a1 + 64;
    *(unsigned __int64 *)(a3 + 216) = 0;
    *(unsigned __int64 *)(a3 + 224) = a1 + 64;
    *(unsigned __int64 *)(a3 + 232) = 0;
    *(unsigned __int64 *)(a3 + 240) = a1 + 64;
    *(unsigned __int64 *)(a3 + 248) = 0;
    return *(unsigned __int64 *)(a3 + 240);
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefRawSquareMulx1024(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_r14;

    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = v_xmm0;
    *(uint64_t *)(arg3 + 0x20) = v_xmm0;
    *(uint64_t *)(arg3 + 0x30) = v_xmm0;
    *(uint64_t *)(arg3 + 0x40) = v_xmm0;
    *(uint64_t *)(arg3 + 0x50) = v_xmm0;
    *(uint64_t *)(arg3 + 0x60) = v_xmm0;
    *(uint64_t *)(arg3 + 0x70) = v_xmm0;
    result = 0;
    local_r11 = 0;
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(arg3 + 0x8);
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(arg3 + 0x10);
    result = 0;
    *(uint64_t *)(arg3 + 0x18) = *(uint64_t *)(arg3 + 0x18);
    *(uint64_t *)(arg3 + 0x20) = *(uint64_t *)(arg3 + 0x20);
    result = 0;
    *(uint64_t *)(arg3 + 0x28) = *(uint64_t *)(arg3 + 0x28);
    *(uint64_t *)(arg3 + 0x30) = *(uint64_t *)(arg3 + 0x30);
    result = 0;
    *(uint64_t *)(arg3 + 0x38) = *(uint64_t *)(arg3 + 0x38);
    local_r14 = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x8) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x10) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x18) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x20) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x28) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x30) = 0;
    result = 0;
    *(uint64_t *)(arg3 + 0x40 + 0x38) = 0;
    Arg3 = (Arg3 + 64) + (64);
    *(uint64_t *)(arg3) = 0;
    *(uint64_t *)(arg3 + 0x8) = 0;
    *(uint64_t *)(arg3 + 0x10) = 0;
    *(uint64_t *)(arg3 + 0x18) = 0;
    *(uint64_t *)(arg3 + 0x20) = 0;
    *(uint64_t *)(arg3 + 0x28) = 0;
    *(uint64_t *)(arg3 + 0x30) = 0;
    *(uint64_t *)(arg3 + 0x38) = 0;
    result = 0;
    local_r11 = 0;
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(arg3 + 0x8);
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(arg3 + 0x10);
    result = 0;
    *(uint64_t *)(arg3 + 0x18) = *(uint64_t *)(arg3 + 0x18);
    *(uint64_t *)(arg3 + 0x20) = *(uint64_t *)(arg3 + 0x20);
    result = 0;
    *(uint64_t *)(arg3 + 0x28) = *(uint64_t *)(arg3 + 0x28);
    *(uint64_t *)(arg3 + 0x30) = *(uint64_t *)(arg3 + 0x30);
    result = 0;
    *(uint64_t *)(arg3 + 0x38) = *(uint64_t *)(arg3 + 0x38);
    local_r14 = 0;
    *(uint64_t *)(arg3 + 0x40) = 0;
    *(uint64_t *)(arg3 + 0x48) = 0;
    *(uint64_t *)(arg3 + 0x50) = 0;
    *(uint64_t *)(arg3 + 0x58) = 0;
    *(uint64_t *)(arg3 + 0x60) = 0;
    *(uint64_t *)(arg3 + 0x68) = 0;
    *(uint64_t *)(arg3 + 0x70) = 0;
    *(uint64_t *)(arg3 + 0x78) = 0;
    Arg3 = (Arg3) - (128);
    *(void **)(arg3) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x8) = 0;
    *(void **)(arg3 + 0x10) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x18) = 0;
    *(void **)(arg3 + 0x20) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x28) = 0;
    *(void **)(arg3 + 0x30) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x38) = 0;
    *(void **)(arg3 + 0x40) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x48) = 0;
    *(void **)(arg3 + 0x50) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x58) = 0;
    *(void **)(arg3 + 0x60) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x68) = 0;
    *(void **)(arg3 + 0x70) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x78) = 0;
    *(void **)(arg3 + 0x80) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x88) = 0;
    *(void **)(arg3 + 0x90) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0x98) = 0;
    *(void **)(arg3 + 0xA0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xA8) = 0;
    *(void **)(arg3 + 0xB0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xB8) = 0;
    *(void **)(arg3 + 0xC0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xC8) = 0;
    *(void **)(arg3 + 0xD0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xD8) = 0;
    *(void **)(arg3 + 0xE0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xE8) = 0;
    *(void **)(arg3 + 0xF0) = Arg1 + 64;
    *(uint64_t *)(arg3 + 0xF8) = 0;
    return *(uint64_t *)(arg3 + 0xF0);
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
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `128` | `W` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x10` | `128` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x20` | `128` | `W` |
| `Arg3` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `W` |
| `Arg3` | `+ 0x30` | `64` | `R` |

추가 오프셋 56개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00532360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00532360[BB_00532360]
```
