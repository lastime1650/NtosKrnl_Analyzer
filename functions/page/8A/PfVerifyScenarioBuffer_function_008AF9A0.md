# PfVerifyScenarioBuffer

- RVA: `0x008AF9A0`–`0x008B0459` (길이 `2,745` bytes)
- VA: `0x00000001408AF9A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FAF4`
- 디코드: `622`개 명령, `2,745/2,745` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008AFA9D` → [PfVerifyScenarioId](../8B/PfVerifyScenarioId_function_008B0460.md) (function, `0x008B0460`)
- `0x008AFD73` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008AFF42` → [StringCchPrintfW](../../text/47/StringCchPrintfW_function_0047BAD0.md) (function, `0x0047BAD0`)
- `0x008B013B` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)

### Direct callers
- [PfSnGetPrefetchInstructions](PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AEE59`

### Static image references
- `0x008AF9B7` → RVA `0x00E0A740` (`.data`; read)
- `0x008AFF1F` → RVA `0x00B01590` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008AFD73` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008AFF42` → [StringCchPrintfW](../../text/47/StringCchPrintfW_function_0047BAD0.md) (`PAGE` → `.text`)
  - `0x008B013B` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AF9A0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008AF9A5  55                              push rbp
008AF9A6  56                              push rsi
008AF9A7  57                              push rdi
008AF9A8  41 54                           push r12
008AF9AA  41 55                           push r13
008AF9AC  41 56                           push r14
008AF9AE  41 57                           push r15
008AF9B0  48 81 EC 10 01 00 00            sub rsp, 0x110
008AF9B7  48 8B 05 82 AD 55 00            mov rax, qword ptr [rip + 0x55ad82]
008AF9BE  48 33 C4                        xor rax, rsp
008AF9C1  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
008AF9C9  45 33 FF                        xor r15d, r15d
008AF9CC  8B DA                           mov ebx, edx
008AF9CE  45 32 E4                        xor r12b, r12b
008AF9D1  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008AF9D5  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
008AF9DA  4D 8B E8                        mov r13, r8
008AF9DD  4C 8B D9                        mov r11, rcx
008AF9E0  81 FA 28 01 00 00               cmp edx, 0x128
008AF9E6  0F 82 6B 07 00 00               jb 0x1408b0157
008AF9EC  41 F6 C3 07                     test r11b, 7
008AF9F0  0F 85 03 08 00 00               jne 0x1408b01f9
008AF9F6  83 39 1F                        cmp dword ptr [rcx], 0x1f
008AF9F9  0F 85 63 07 00 00               jne 0x1408b0162
008AF9FF  81 79 04 53 43 43 41            cmp dword ptr [rcx + 4], 0x41434353
008AFA06  0F 85 56 07 00 00               jne 0x1408b0162
008AFA0C  81 FB 00 00 00 10               cmp ebx, 0x10000000
008AFA12  0F 87 EC 07 00 00               ja 0x1408b0204
008AFA18  3B 59 0C                        cmp ebx, dword ptr [rcx + 0xc]
008AFA1B  0F 85 EE 07 00 00               jne 0x1408b020f
008AFA21  83 79 50 01                     cmp dword ptr [rcx + 0x50], 1
008AFA25  0F 87 4D 07 00 00               ja 0x1408b0178
008AFA2B  8B 79 58                        mov edi, dword ptr [rcx + 0x58]
008AFA2E  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
008AFA32  81 FF 00 40 00 00               cmp edi, 0x4000
008AFA38  0F 87 08 0A 00 00               ja 0x1408b0446
008AFA3E  44 8B 51 70                     mov r10d, dword ptr [rcx + 0x70]
008AFA42  41 81 FA 00 40 00 00            cmp r10d, 0x4000
008AFA49  0F 87 F7 09 00 00               ja 0x1408b0446
008AFA4F  8B 71 60                        mov esi, dword ptr [rcx + 0x60]
008AFA52  81 FE 00 00 10 00               cmp esi, 0x100000
008AFA58  0F 87 E8 09 00 00               ja 0x1408b0446
008AFA5E  44 8B 49 68                     mov r9d, dword ptr [rcx + 0x68]
008AFA62  41 81 F9 00 00 40 00            cmp r9d, 0x400000
008AFA69  0F 87 D7 09 00 00               ja 0x1408b0446
008AFA6F  85 FF                           test edi, edi
008AFA71  0F 84 C4 09 00 00               je 0x1408b043b
008AFA77  85 F6                           test esi, esi
008AFA79  0F 84 BC 09 00 00               je 0x1408b043b
008AFA7F  45 85 C9                        test r9d, r9d
008AFA82  0F 84 B3 09 00 00               je 0x1408b043b
008AFA88  8B 81 CC 00 00 00               mov eax, dword ptr [rcx + 0xcc]
008AFA8E  FF C8                           dec eax
008AFA90  83 F8 07                        cmp eax, 7
008AFA93  0F 87 34 07 00 00               ja 0x1408b01cd
008AFA99  48 83 C1 10                     add rcx, 0x10
008AFA9D  E8 BE 09 00 00                  call 0x1408b0460
008AFAA2  84 C0                           test al, al
008AFAA4  0F 84 70 07 00 00               je 0x1408b021a
008AFAAA  41 8B 53 54                     mov edx, dword ptr [r11 + 0x54]
008AFAAE  49 03 D3                        add rdx, r11
008AFAB1  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
008AFAB9  F6 C2 03                        test dl, 3
008AFABC  0F 85 63 07 00 00               jne 0x1408b0225
008AFAC2  49 3B D3                        cmp rdx, r11
008AFAC5  0F 82 65 09 00 00               jb 0x1408b0430
008AFACB  49 03 DB                        add rbx, r11
008AFACE  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008AFAD3  48 3B D3                        cmp rdx, rbx
008AFAD6  0F 83 54 09 00 00               jae 0x1408b0430
008AFADC  8B CF                           mov ecx, edi
008AFADE  48 C1 E1 05                     shl rcx, 5
008AFAE2  48 FF C9                        dec rcx
008AFAE5  48 03 CA                        add rcx, rdx
008AFAE8  48 3B CB                        cmp rcx, rbx
008AFAEB  0F 83 34 09 00 00               jae 0x1408b0425
008AFAF1  49 3B CB                        cmp rcx, r11
008AFAF4  0F 82 2B 09 00 00               jb 0x1408b0425
008AFAFA  41 8B 4B 5C                     mov ecx, dword ptr [r11 + 0x5c]
008AFAFE  49 03 CB                        add rcx, r11
008AFB01  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
008AFB06  F6 C1 03                        test cl, 3
008AFB09  0F 85 21 07 00 00               jne 0x1408b0230
008AFB0F  48 3B CB                        cmp rcx, rbx
008AFB12  0F 83 02 09 00 00               jae 0x1408b041a
008AFB18  49 3B CB                        cmp rcx, r11
008AFB1B  0F 82 F9 08 00 00               jb 0x1408b041a
008AFB21  48 8D 0C F1                     lea rcx, [rcx + rsi*8]
008AFB25  48 FF C9                        dec rcx
008AFB28  48 3B CB                        cmp rcx, rbx
008AFB2B  0F 83 DE 08 00 00               jae 0x1408b040f
008AFB31  49 3B CB                        cmp rcx, r11
008AFB34  0F 82 D5 08 00 00               jb 0x1408b040f
008AFB3A  45 8B 43 64                     mov r8d, dword ptr [r11 + 0x64]
008AFB3E  4D 03 C3                        add r8, r11
008AFB41  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
008AFB46  41 F6 C0 01                     test r8b, 1
008AFB4A  0F 85 EB 06 00 00               jne 0x1408b023b
008AFB50  4C 3B C3                        cmp r8, rbx
008AFB53  0F 83 7F 06 00 00               jae 0x1408b01d8
008AFB59  4D 3B C3                        cmp r8, r11
008AFB5C  0F 82 76 06 00 00               jb 0x1408b01d8
008AFB62  49 8D 49 FF                     lea rcx, [r9 - 1]
008AFB66  49 03 C8                        add rcx, r8
008AFB69  48 3B CB                        cmp rcx, rbx
008AFB6C  0F 83 92 08 00 00               jae 0x1408b0404
008AFB72  49 3B CB                        cmp rcx, r11
008AFB75  0F 82 89 08 00 00               jb 0x1408b0404
008AFB7B  45 8B 4B 6C                     mov r9d, dword ptr [r11 + 0x6c]
008AFB7F  4D 03 CB                        add r9, r11
008AFB82  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
008AFB87  41 F6 C1 07                     test r9b, 7
008AFB8B  0F 85 B5 06 00 00               jne 0x1408b0246
008AFB91  4C 3B CB                        cmp r9, rbx
008AFB94  0F 83 5F 08 00 00               jae 0x1408b03f9
008AFB9A  4D 3B CB                        cmp r9, r11
008AFB9D  0F 82 56 08 00 00               jb 0x1408b03f9
008AFBA3  41 8B 4B 74                     mov ecx, dword ptr [r11 + 0x74]
008AFBA7  48 FF C9                        dec rcx
008AFBAA  49 03 C9                        add rcx, r9
008AFBAD  48 3B CB                        cmp rcx, rbx
008AFBB0  0F 83 38 08 00 00               jae 0x1408b03ee
008AFBB6  49 3B CB                        cmp rcx, r11
008AFBB9  0F 82 2F 08 00 00               jb 0x1408b03ee
008AFBBF  4B 8D 04 52                     lea rax, [r10 + r10*2]
008AFBC3  48 C1 E0 05                     shl rax, 5
008AFBC7  48 FF C8                        dec rax
008AFBCA  49 03 C1                        add rax, r9
008AFBCD  48 3B C3                        cmp rax, rbx
008AFBD0  0F 83 0D 08 00 00               jae 0x1408b03e3
008AFBD6  49 3B C3                        cmp rax, r11
008AFBD9  0F 82 04 08 00 00               jb 0x1408b03e3
008AFBDF  41 8B 43 7C                     mov eax, dword ptr [r11 + 0x7c]
008AFBE3  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AFBE7  83 F8 07                        cmp eax, 7
008AFBEA  0F 87 61 06 00 00               ja 0x1408b0251
008AFBF0  44 8B D6                        mov r10d, esi
008AFBF3  41 8B EF                        mov ebp, r15d
008AFBF6  41 8B C7                        mov eax, r15d
008AFBF9  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
008AFBFD  B9 00 04 00 00                  mov ecx, 0x400
008AFC02  3B C7                           cmp eax, edi
008AFC04  0F 83 70 02 00 00               jae 0x1408afe7a
008AFC0A  44 8B C8                        mov r9d, eax
008AFC0D  49 C1 E1 05                     shl r9, 5
008AFC11  4C 03 CA                        add r9, rdx
008AFC14  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
008AFC19  41 8B 51 0C                     mov edx, dword ptr [r9 + 0xc]
008AFC1D  49 03 D0                        add rdx, r8
008AFC20  F6 C2 01                        test dl, 1
008AFC23  0F 85 BA 05 00 00               jne 0x1408b01e3
008AFC29  48 3B D3                        cmp rdx, rbx
008AFC2C  0F 83 BF 06 00 00               jae 0x1408b02f1
008AFC32  49 3B D3                        cmp rdx, r11
008AFC35  0F 82 B6 06 00 00               jb 0x1408b02f1
008AFC3B  45 8B 41 10                     mov r8d, dword ptr [r9 + 0x10]
008AFC3F  45 85 C0                        test r8d, r8d
008AFC42  0F 84 9E 06 00 00               je 0x1408b02e6
008AFC48  44 3B C1                        cmp r8d, ecx
008AFC4B  0F 87 8A 06 00 00               ja 0x1408b02db
008AFC51  42 8D 04 45 02 00 00 00         lea eax, [r8*2 + 2]
008AFC59  48 FF C8                        dec rax
008AFC5C  48 03 C2                        add rax, rdx
008AFC5F  48 3B C3                        cmp rax, rbx
008AFC62  0F 83 68 06 00 00               jae 0x1408b02d0
008AFC68  49 3B C3                        cmp rax, r11
008AFC6B  0F 82 5F 06 00 00               jb 0x1408b02d0
008AFC71  66 46 39 3C 42                  cmp word ptr [rdx + r8*2], r15w
008AFC76  0F 85 49 06 00 00               jne 0x1408b02c5
008AFC7C  41 8B 51 04                     mov edx, dword ptr [r9 + 4]
008AFC80  81 FA 00 80 00 00               cmp edx, 0x8000
008AFC86  0F 87 36 05 00 00               ja 0x1408b01c2
008AFC8C  41 3B D2                        cmp edx, r10d
008AFC8F  0F 87 25 06 00 00               ja 0x1408b02ba
008AFC95  49 63 19                        movsxd rbx, dword ptr [r9]
008AFC98  44 2B D2                        sub r10d, edx
008AFC9B  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
008AFCA0  83 FB FF                        cmp ebx, -1
008AFCA3  0F 84 B3 05 00 00               je 0x1408b025c
008AFCA9  3B DD                           cmp ebx, ebp
008AFCAB  0F 85 BE 05 00 00               jne 0x1408b026f
008AFCB1  45 8B 41 14                     mov r8d, dword ptr [r9 + 0x14]
008AFCB5  03 EA                           add ebp, edx
008AFCB7  41 F7 C0 00 7F 00 00            test r8d, 0x7f00
008AFCBE  89 6C 24 4C                     mov dword ptr [rsp + 0x4c], ebp
008AFCC2  0F 94 C1                        sete cl
008AFCC5  41 F6 C0 01                     test r8b, 1
008AFCC9  0F 94 C0                        sete al
008AFCCC  84 C8                           test al, cl
008AFCCE  0F 85 91 01 00 00               jne 0x1408afe65
008AFCD4  41 F6 C0 01                     test r8b, 1
008AFCD8  0F 84 1D 01 00 00               je 0x1408afdfb
008AFCDE  8D 04 13                        lea eax, [rbx + rdx]
008AFCE1  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
008AFCE6  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008AFCEB  4C 8B D3                        mov r10, rbx
008AFCEE  48 83 C2 04                     add rdx, 4
008AFCF2  48 63 F8                        movsxd rdi, eax
008AFCF5  41 8B EF                        mov ebp, r15d
008AFCF8  45 8B F7                        mov r14d, r15d
008AFCFB  4C 8B DB                        mov r11, rbx
008AFCFE  48 8D 14 DA                     lea rdx, [rdx + rbx*8]
008AFD02  4C 3B DF                        cmp r11, rdi
008AFD05  0F 8D 89 00 00 00               jge 0x1408afd94
008AFD0B  4D 85 DB                        test r11, r11
008AFD0E  0F 88 85 05 00 00               js 0x1408b0299
008AFD14  44 3B D6                        cmp r10d, esi
008AFD17  0F 83 7C 05 00 00               jae 0x1408b0299
008AFD1D  44 3B D3                        cmp r10d, ebx
008AFD20  74 0C                           je 0x1408afd2e
008AFD22  8B 42 F4                        mov eax, dword ptr [rdx - 0xc]
008AFD25  39 42 FC                        cmp dword ptr [rdx - 4], eax
008AFD28  0F 86 55 05 00 00               jbe 0x1408b0283
008AFD2E  44 8B 02                        mov r8d, dword ptr [rdx]
008AFD31  45 8B C8                        mov r9d, r8d
008AFD34  41 C1 E9 04                     shr r9d, 4
008AFD38  41 8B C0                        mov eax, r8d
008AFD3B  83 E0 01                        and eax, 1
008AFD3E  75 10                           jne 0x1408afd50
008AFD40  41 8B C9                        mov ecx, r9d
008AFD43  83 E1 07                        and ecx, 7
008AFD46  3B 4C 24 40                     cmp ecx, dword ptr [rsp + 0x40]
008AFD4A  0F 87 3E 05 00 00               ja 0x1408b028e
008AFD50  41 F6 C0 0E                     test r8b, 0xe
008AFD54  0F 85 B6 00 00 00               jne 0x1408afe10
008AFD5A  41 BF AD 00 00 00               mov r15d, 0xad
008AFD60  45 89 7D 00                     mov dword ptr [r13], r15d
008AFD64  41 0F B6 C4                     movzx eax, r12b
008AFD68  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
008AFD70  48 33 CC                        xor rcx, rsp
008AFD73  E8 C8 C8 DF FF                  call 0x1406ac640
008AFD78  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
008AFD80  48 81 C4 10 01 00 00            add rsp, 0x110
008AFD87  41 5F                           pop r15
008AFD89  41 5E                           pop r14
008AFD8B  41 5D                           pop r13
008AFD8D  41 5C                           pop r12
008AFD8F  5F                              pop rdi
008AFD90  5E                              pop rsi
008AFD91  5D                              pop rbp
008AFD92  C3                              ret
008AFD93  CC                              int3
008AFD94  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
008AFD99  41 3B 69 08                     cmp ebp, dword ptr [r9 + 8]
008AFD9D  0F 85 0C 05 00 00               jne 0x1408b02af
008AFDA3  41 8B 49 14                     mov ecx, dword ptr [r9 + 0x14]
008AFDA7  F6 C1 01                        test cl, 1
008AFDAA  75 20                           jne 0x1408afdcc
008AFDAC  8B C1                           mov eax, ecx
008AFDAE  D1 E8                           shr eax, 1
008AFDB0  83 E0 7F                        and eax, 0x7f
008AFDB3  39 44 24 30                     cmp dword ptr [rsp + 0x30], eax
008AFDB7  0F 85 E7 04 00 00               jne 0x1408b02a4
008AFDBD  C1 E9 08                        shr ecx, 8
008AFDC0  83 E1 7F                        and ecx, 0x7f
008AFDC3  44 3B F1                        cmp r14d, ecx
008AFDC6  0F 85 D8 04 00 00               jne 0x1408b02a4
008AFDCC  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
008AFDD0  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
008AFDD5  FF C0                           inc eax
008AFDD7  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
008AFDDC  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
008AFDE1  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
008AFDE6  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
008AFDEE  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
008AFDF2  8B 6C 24 4C                     mov ebp, dword ptr [rsp + 0x4c]
008AFDF6  E9 FE FD FF FF                  jmp 0x1408afbf9
008AFDFB  45 39 79 08                     cmp dword ptr [r9 + 8], r15d
008AFDFF  0F 85 D9 FE FF FF               jne 0x1408afcde
008AFE05  41 BF 9D 00 00 00               mov r15d, 0x9d
008AFE0B  E9 50 FF FF FF                  jmp 0x1408afd60
008AFE10  85 C0                           test eax, eax
008AFE12  75 40                           jne 0x1408afe54
008AFE14  FF C5                           inc ebp
008AFE16  41 F6 C0 04                     test r8b, 4
008AFE1A  74 11                           je 0x1408afe2d
008AFE1C  41 8B C9                        mov ecx, r9d
008AFE1F  B8 01 00 00 00                  mov eax, 1
008AFE24  83 E1 07                        and ecx, 7
008AFE27  D3 E0                           shl eax, cl
008AFE29  09 44 24 30                     or dword ptr [rsp + 0x30], eax
008AFE2D  41 F6 C0 02                     test r8b, 2
008AFE31  74 12                           je 0x1408afe45
008AFE33  41 83 E1 07                     and r9d, 7
008AFE37  B8 01 00 00 00                  mov eax, 1
008AFE3C  41 0F B6 C9                     movzx ecx, r9b
008AFE40  D3 E0                           shl eax, cl
008AFE42  44 0B F0                        or r14d, eax
008AFE45  41 FF C2                        inc r10d
008AFE48  49 FF C3                        inc r11
008AFE4B  48 83 C2 08                     add rdx, 8
008AFE4F  E9 AE FE FF FF                  jmp 0x1408afd02
008AFE54  41 F6 C0 08                     test r8b, 8
008AFE58  74 EB                           je 0x1408afe45
008AFE5A  41 BF AF 00 00 00               mov r15d, 0xaf
008AFE60  E9 FB FE FF FF                  jmp 0x1408afd60
008AFE65  41 F6 C0 FE                     test r8b, 0xfe
008AFE69  0F 85 65 FE FF FF               jne 0x1408afcd4
008AFE6F  41 BF 9B 00 00 00               mov r15d, 0x9b
008AFE75  E9 E6 FE FF FF                  jmp 0x1408afd60
008AFE7A  45 85 D2                        test r10d, r10d
008AFE7D  0F 85 79 04 00 00               jne 0x1408b02fc
008AFE83  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
008AFE87  45 8B F7                        mov r14d, r15d
008AFE8A  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
008AFE8F  49 03 F3                        add rsi, r11
008AFE92  41 8B EF                        mov ebp, r15d
008AFE95  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
008AFEA0  41 8B 53 70                     mov edx, dword ptr [r11 + 0x70]
008AFEA4  3B EA                           cmp ebp, edx
008AFEA6  0F 83 49 02 00 00               jae 0x1408b00f5
008AFEAC  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
008AFEB1  44 8D 45 01                     lea r8d, [rbp + 1]
008AFEB5  8B C5                           mov eax, ebp
008AFEB7  48 8D 3C 40                     lea rdi, [rax + rax*2]
008AFEBB  48 C1 E7 05                     shl rdi, 5
008AFEBF  49 03 F9                        add rdi, r9
008AFEC2  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008AFEC6  44 8B 4F 10                     mov r9d, dword ptr [rdi + 0x10]
008AFECA  44 3B C2                        cmp r8d, edx
008AFECD  0F 82 C6 02 00 00               jb 0x1408b0199
008AFED3  8B 1F                           mov ebx, dword ptr [rdi]
008AFED5  48 03 5C 24 38                  add rbx, qword ptr [rsp + 0x38]
008AFEDA  F6 C3 01                        test bl, 1
008AFEDD  0F 85 0B 03 00 00               jne 0x1408b01ee
008AFEE3  48 3B DE                        cmp rbx, rsi
008AFEE6  0F 83 D6 04 00 00               jae 0x1408b03c2
008AFEEC  49 3B DB                        cmp rbx, r11
008AFEEF  0F 82 CD 04 00 00               jb 0x1408b03c2
008AFEF5  8B 47 04                        mov eax, dword ptr [rdi + 4]
008AFEF8  48 8D 0C 43                     lea rcx, [rbx + rax*2]
008AFEFC  48 8D 41 01                     lea rax, [rcx + 1]
008AFF00  48 3B C6                        cmp rax, rsi
008AFF03  0F 83 AE 04 00 00               jae 0x1408b03b7
008AFF09  49 3B C3                        cmp rax, r11
008AFF0C  0F 82 A5 04 00 00               jb 0x1408b03b7
008AFF12  66 44 39 39                     cmp word ptr [rcx], r15w
008AFF16  0F 85 90 04 00 00               jne 0x1408b03ac
008AFF1C  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
008AFF1F  4C 8D 05 6A 16 25 00            lea r8, [rip + 0x25166a]
008AFF26  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008AFF29  BA 23 00 00 00                  mov edx, 0x23
008AFF2E  44 8B 4F 0C                     mov r9d, dword ptr [rdi + 0xc]
008AFF32  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008AFF36  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
008AFF3A  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
008AFF42  E8 89 BB BC FF                  call 0x14047bad0
008AFF47  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
008AFF4F  48 2B D3                        sub rdx, rbx
008AFF52  0F B7 0B                        movzx ecx, word ptr [rbx]
008AFF55  0F B7 04 13                     movzx eax, word ptr [rbx + rdx]
008AFF59  2B C8                           sub ecx, eax
008AFF5B  75 08                           jne 0x1408aff65
008AFF5D  48 83 C3 02                     add rbx, 2
008AFF61  85 C0                           test eax, eax
008AFF63  75 ED                           jne 0x1408aff52
008AFF65  85 C9                           test ecx, ecx
008AFF67  0F 85 21 02 00 00               jne 0x1408b018e
008AFF6D  8B 4F 14                        mov ecx, dword ptr [rdi + 0x14]
008AFF70  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
008AFF75  49 03 C9                        add rcx, r9
008AFF78  F6 C1 07                        test cl, 7
008AFF7B  0F 85 20 04 00 00               jne 0x1408b03a1
008AFF81  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
008AFF86  48 3B CE                        cmp rcx, rsi
008AFF89  0F 83 07 04 00 00               jae 0x1408b0396
008AFF8F  49 3B CB                        cmp rcx, r11
008AFF92  0F 82 FE 03 00 00               jb 0x1408b0396
008AFF98  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008AFF9B  83 F8 18                        cmp eax, 0x18
008AFF9E  0F 82 E7 03 00 00               jb 0x1408b038b
008AFFA4  48 8D 50 FF                     lea rdx, [rax - 1]
008AFFA8  48 03 D1                        add rdx, rcx
008AFFAB  48 3B D6                        cmp rdx, rsi
008AFFAE  0F 83 CC 03 00 00               jae 0x1408b0380
008AFFB4  49 3B D3                        cmp rdx, r11
008AFFB7  0F 82 C3 03 00 00               jb 0x1408b0380
008AFFBD  83 39 03                        cmp dword ptr [rcx], 3
008AFFC0  0F 85 AF 03 00 00               jne 0x1408b0375
008AFFC6  81 79 04 00 40 08 00            cmp dword ptr [rcx + 4], 0x84000
008AFFCD  0F 87 97 03 00 00               ja 0x1408b036a
008AFFD3  41 8B 43 7C                     mov eax, dword ptr [r11 + 0x7c]
008AFFD7  41 8B D7                        mov edx, r15d
008AFFDA  85 C0                           test eax, eax
008AFFDC  0F 85 D6 00 00 00               jne 0x1408b00b8
008AFFE2  8B 41 04                        mov eax, dword ptr [rcx + 4]
008AFFE5  3B D0                           cmp edx, eax
008AFFE7  0F 85 96 01 00 00               jne 0x1408b0183
008AFFED  B9 18 00 00 00                  mov ecx, 0x18
008AFFF2  85 C0                           test eax, eax
008AFFF4  74 07                           je 0x1408afffd
008AFFF6  8D 0C C5 10 00 00 00            lea ecx, [rax*8 + 0x10]
008AFFFD  3B 4F 18                        cmp ecx, dword ptr [rdi + 0x18]
008B0000  0F 85 59 03 00 00               jne 0x1408b035f
008B0006  81 7F 20 00 00 08 00            cmp dword ptr [rdi + 0x20], 0x80000
008B000D  0F 87 41 03 00 00               ja 0x1408b0354
008B0013  41 8B 4B 7C                     mov ecx, dword ptr [r11 + 0x7c]
008B0017  41 8B C7                        mov eax, r15d
008B001A  85 C9                           test ecx, ecx
008B001C  0F 85 BA 00 00 00               jne 0x1408b00dc
008B0022  44 8B 47 20                     mov r8d, dword ptr [rdi + 0x20]
008B0026  41 3B C0                        cmp eax, r8d
008B0029  0F 85 1A 03 00 00               jne 0x1408b0349
008B002F  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
008B0032  44 03 F0                        add r14d, eax
008B0035  49 03 C9                        add rcx, r9
008B0038  F6 C1 01                        test cl, 1
008B003B  0F 85 FD 02 00 00               jne 0x1408b033e
008B0041  41 8B D7                        mov edx, r15d
008B0044  41 3B D0                        cmp edx, r8d
008B0047  73 68                           jae 0x1408b00b1
008B0049  48 3B CE                        cmp rcx, rsi
008B004C  0F 83 E1 02 00 00               jae 0x1408b0333
008B0052  49 3B CB                        cmp rcx, r11
008B0055  0F 82 D8 02 00 00               jb 0x1408b0333
008B005B  48 8D 41 03                     lea rax, [rcx + 3]
008B005F  48 3B C6                        cmp rax, rsi
008B0062  0F 83 C0 02 00 00               jae 0x1408b0328
008B0068  49 3B C3                        cmp rax, r11
008B006B  0F 82 B7 02 00 00               jb 0x1408b0328
008B0071  0F B7 01                        movzx eax, word ptr [rcx]
008B0074  41 BA 00 04 00 00               mov r10d, 0x400
008B007A  66 41 3B C2                     cmp ax, r10w
008B007E  0F 83 99 02 00 00               jae 0x1408b031d
008B0084  48 8D 0C 41                     lea rcx, [rcx + rax*2]
008B0088  48 8D 41 03                     lea rax, [rcx + 3]
008B008C  48 3B C6                        cmp rax, rsi
008B008F  0F 83 7D 02 00 00               jae 0x1408b0312
008B0095  49 3B C3                        cmp rax, r11
008B0098  0F 82 74 02 00 00               jb 0x1408b0312
008B009E  66 44 39 79 02                  cmp word ptr [rcx + 2], r15w
008B00A3  0F 85 5E 02 00 00               jne 0x1408b0307
008B00A9  FF C2                           inc edx
008B00AB  48 83 C1 04                     add rcx, 4
008B00AF  EB 93                           jmp 0x1408b0044
008B00B1  FF C5                           inc ebp
008B00B3  E9 E8 FD FF FF                  jmp 0x1408afea0
008B00B8  4C 8D 47 24                     lea r8, [rdi + 0x24]
008B00BC  4C 8B C8                        mov r9, rax
008B00BF  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
008B00C3  41 03 00                        add eax, dword ptr [r8]
008B00C6  4D 8D 40 04                     lea r8, [r8 + 4]
008B00CA  03 D0                           add edx, eax
008B00CC  49 83 E9 01                     sub r9, 1
008B00D0  75 ED                           jne 0x1408b00bf
008B00D2  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
008B00D7  E9 06 FF FF FF                  jmp 0x1408affe2
008B00DC  48 8D 57 40                     lea rdx, [rdi + 0x40]
008B00E0  4C 8B C1                        mov r8, rcx
008B00E3  03 02                           add eax, dword ptr [rdx]
008B00E5  48 8D 52 04                     lea rdx, [rdx + 4]
008B00E9  49 83 E8 01                     sub r8, 1
008B00ED  0F 84 2F FF FF FF               je 0x1408b0022
008B00F3  EB EE                           jmp 0x1408b00e3
008B00F5  45 3B 73 78                     cmp r14d, dword ptr [r11 + 0x78]
008B00F9  0F 85 CE 02 00 00               jne 0x1408b03cd
008B00FF  41 81 FE 00 00 08 00            cmp r14d, 0x80000
008B0106  0F 87 CC 02 00 00               ja 0x1408b03d8
008B010C  41 8B 93 D8 00 00 00            mov edx, dword ptr [r11 + 0xd8]
008B0113  41 8B CF                        mov ecx, r15d
008B0116  45 8B 83 D4 00 00 00            mov r8d, dword ptr [r11 + 0xd4]
008B011D  85 D2                           test edx, edx
008B011F  41 8B C7                        mov eax, r15d
008B0122  0F 94 C1                        sete cl
008B0125  45 85 C0                        test r8d, r8d
008B0128  0F 94 C0                        sete al
008B012B  3B C1                           cmp eax, ecx
008B012D  75 3E                           jne 0x1408b016d
008B012F  45 85 C0                        test r8d, r8d
008B0132  74 10                           je 0x1408b0144
008B0134  4B 8D 0C 03                     lea rcx, [r11 + r8]
008B0138  45 33 C0                        xor r8d, r8d
008B013B  E8 20 8A BA FF                  call 0x140458b60
008B0140  85 C0                           test eax, eax
008B0142  78 08                           js 0x1408b014c
008B0144  41 B4 01                        mov r12b, 1
008B0147  E9 14 FC FF FF                  jmp 0x1408afd60
008B014C  41 BF 68 01 00 00               mov r15d, 0x168
008B0152  E9 09 FC FF FF                  jmp 0x1408afd60
008B0157  41 BF 0A 00 00 00               mov r15d, 0xa
008B015D  E9 FE FB FF FF                  jmp 0x1408afd60
008B0162  41 BF 14 00 00 00               mov r15d, 0x14
008B0168  E9 F3 FB FF FF                  jmp 0x1408afd60
008B016D  41 BF 5E 01 00 00               mov r15d, 0x15e
008B0173  E9 E8 FB FF FF                  jmp 0x1408afd60
008B0178  41 BF 1B 00 00 00               mov r15d, 0x1b
008B017E  E9 DD FB FF FF                  jmp 0x1408afd60
008B0183  41 BF 09 01 00 00               mov r15d, 0x109
008B0189  E9 D2 FB FF FF                  jmp 0x1408afd60
008B018E  41 BF DE 00 00 00               mov r15d, 0xde
008B0194  E9 C7 FB FF FF                  jmp 0x1408afd60
008B0199  4F 8D 14 40                     lea r10, [r8 + r8*2]
008B019D  49 C1 E2 05                     shl r10, 5
008B01A1  49 39 44 1A 08                  cmp qword ptr [r10 + rbx + 8], rax
008B01A6  0F 85 A5 02 00 00               jne 0x1408b0451
008B01AC  45 39 4C 1A 10                  cmp dword ptr [r10 + rbx + 0x10], r9d
008B01B1  0F 85 9A 02 00 00               jne 0x1408b0451
008B01B7  41 BF C0 00 00 00               mov r15d, 0xc0
008B01BD  E9 9E FB FF FF                  jmp 0x1408afd60
008B01C2  41 BF 8C 00 00 00               mov r15d, 0x8c
008B01C8  E9 93 FB FF FF                  jmp 0x1408afd60
008B01CD  41 BF 23 00 00 00               mov r15d, 0x23
008B01D3  E9 88 FB FF FF                  jmp 0x1408afd60
008B01D8  41 BF 3C 00 00 00               mov r15d, 0x3c
008B01DE  E9 7D FB FF FF                  jmp 0x1408afd60
008B01E3  41 BF 4D 00 00 00               mov r15d, 0x4d
008B01E9  E9 72 FB FF FF                  jmp 0x1408afd60
008B01EE  41 BF C3 00 00 00               mov r15d, 0xc3
008B01F4  E9 67 FB FF FF                  jmp 0x1408afd60
008B01F9  41 BF 0F 00 00 00               mov r15d, 0xf
008B01FF  E9 5C FB FF FF                  jmp 0x1408afd60
008B0204  41 BF 19 00 00 00               mov r15d, 0x19
008B020A  E9 51 FB FF FF                  jmp 0x1408afd60
008B020F  41 BF 1A 00 00 00               mov r15d, 0x1a
008B0215  E9 46 FB FF FF                  jmp 0x1408afd60
008B021A  41 BF 25 00 00 00               mov r15d, 0x25
008B0220  E9 3B FB FF FF                  jmp 0x1408afd60
008B0225  41 BF 26 00 00 00               mov r15d, 0x26
008B022B  E9 30 FB FF FF                  jmp 0x1408afd60
008B0230  41 BF 2F 00 00 00               mov r15d, 0x2f
008B0236  E9 25 FB FF FF                  jmp 0x1408afd60
008B023B  41 BF 39 00 00 00               mov r15d, 0x39
008B0241  E9 1A FB FF FF                  jmp 0x1408afd60
008B0246  41 BF 48 00 00 00               mov r15d, 0x48
008B024C  E9 0F FB FF FF                  jmp 0x1408afd60
008B0251  41 BF 4C 00 00 00               mov r15d, 0x4c
008B0257  E9 04 FB FF FF                  jmp 0x1408afd60
008B025C  85 D2                           test edx, edx
008B025E  0F 84 45 FA FF FF               je 0x1408afca9
008B0264  41 BF 98 00 00 00               mov r15d, 0x98
008B026A  E9 F1 FA FF FF                  jmp 0x1408afd60
008B026F  83 FB FF                        cmp ebx, -1
008B0272  0F 84 39 FA FF FF               je 0x1408afcb1
008B0278  41 BF 99 00 00 00               mov r15d, 0x99
008B027E  E9 DD FA FF FF                  jmp 0x1408afd60
008B0283  41 BF A5 00 00 00               mov r15d, 0xa5
008B0289  E9 D2 FA FF FF                  jmp 0x1408afd60
008B028E  41 BF A7 00 00 00               mov r15d, 0xa7
008B0294  E9 C7 FA FF FF                  jmp 0x1408afd60
008B0299  41 BF A0 00 00 00               mov r15d, 0xa0
008B029F  E9 BC FA FF FF                  jmp 0x1408afd60
008B02A4  41 BF BB 00 00 00               mov r15d, 0xbb
008B02AA  E9 B1 FA FF FF                  jmp 0x1408afd60
008B02AF  41 BF B9 00 00 00               mov r15d, 0xb9
008B02B5  E9 A6 FA FF FF                  jmp 0x1408afd60
008B02BA  41 BF 96 00 00 00               mov r15d, 0x96
008B02C0  E9 9B FA FF FF                  jmp 0x1408afd60
008B02C5  41 BF 78 00 00 00               mov r15d, 0x78
008B02CB  E9 90 FA FF FF                  jmp 0x1408afd60
008B02D0  41 BF 6E 00 00 00               mov r15d, 0x6e
008B02D6  E9 85 FA FF FF                  jmp 0x1408afd60
008B02DB  41 BF 64 00 00 00               mov r15d, 0x64
008B02E1  E9 7A FA FF FF                  jmp 0x1408afd60
008B02E6  41 BF 5A 00 00 00               mov r15d, 0x5a
008B02EC  E9 6F FA FF FF                  jmp 0x1408afd60
008B02F1  41 BF 50 00 00 00               mov r15d, 0x50
008B02F7  E9 64 FA FF FF                  jmp 0x1408afd60
008B02FC  41 BF BE 00 00 00               mov r15d, 0xbe
008B0302  E9 59 FA FF FF                  jmp 0x1408afd60
008B0307  41 BF 40 01 00 00               mov r15d, 0x140
008B030D  E9 4E FA FF FF                  jmp 0x1408afd60
008B0312  41 BF 36 01 00 00               mov r15d, 0x136
008B0318  E9 43 FA FF FF                  jmp 0x1408afd60
008B031D  41 BF 2C 01 00 00               mov r15d, 0x12c
008B0323  E9 38 FA FF FF                  jmp 0x1408afd60
008B0328  41 BF 22 01 00 00               mov r15d, 0x122
008B032E  E9 2D FA FF FF                  jmp 0x1408afd60
008B0333  41 BF 1D 01 00 00               mov r15d, 0x11d
008B0339  E9 22 FA FF FF                  jmp 0x1408afd60
008B033E  41 BF 1B 01 00 00               mov r15d, 0x11b
008B0344  E9 17 FA FF FF                  jmp 0x1408afd60
008B0349  41 BF 19 01 00 00               mov r15d, 0x119
008B034F  E9 0C FA FF FF                  jmp 0x1408afd60
008B0354  41 BF 18 01 00 00               mov r15d, 0x118
008B035A  E9 01 FA FF FF                  jmp 0x1408afd60
008B035F  41 BF 0E 01 00 00               mov r15d, 0x10e
008B0365  E9 F6 F9 FF FF                  jmp 0x1408afd60
008B036A  41 BF 04 01 00 00               mov r15d, 0x104
008B0370  E9 EB F9 FF FF                  jmp 0x1408afd60
008B0375  41 BF FA 00 00 00               mov r15d, 0xfa
008B037B  E9 E0 F9 FF FF                  jmp 0x1408afd60
008B0380  41 BF F5 00 00 00               mov r15d, 0xf5
008B0386  E9 D5 F9 FF FF                  jmp 0x1408afd60
008B038B  41 BF F0 00 00 00               mov r15d, 0xf0
008B0391  E9 CA F9 FF FF                  jmp 0x1408afd60
008B0396  41 BF E6 00 00 00               mov r15d, 0xe6
008B039C  E9 BF F9 FF FF                  jmp 0x1408afd60
008B03A1  41 BF E1 00 00 00               mov r15d, 0xe1
008B03A7  E9 B4 F9 FF FF                  jmp 0x1408afd60
008B03AC  41 BF DC 00 00 00               mov r15d, 0xdc
008B03B2  E9 A9 F9 FF FF                  jmp 0x1408afd60
008B03B7  41 BF D2 00 00 00               mov r15d, 0xd2
008B03BD  E9 9E F9 FF FF                  jmp 0x1408afd60
008B03C2  41 BF C8 00 00 00               mov r15d, 0xc8
008B03C8  E9 93 F9 FF FF                  jmp 0x1408afd60
008B03CD  41 BF 4A 01 00 00               mov r15d, 0x14a
008B03D3  E9 88 F9 FF FF                  jmp 0x1408afd60
008B03D8  41 BF 54 01 00 00               mov r15d, 0x154
008B03DE  E9 7D F9 FF FF                  jmp 0x1408afd60
008B03E3  41 BF 4B 00 00 00               mov r15d, 0x4b
008B03E9  E9 72 F9 FF FF                  jmp 0x1408afd60
008B03EE  41 BF 4A 00 00 00               mov r15d, 0x4a
008B03F4  E9 67 F9 FF FF                  jmp 0x1408afd60
008B03F9  41 BF 49 00 00 00               mov r15d, 0x49
008B03FF  E9 5C F9 FF FF                  jmp 0x1408afd60
008B0404  41 BF 46 00 00 00               mov r15d, 0x46
008B040A  E9 51 F9 FF FF                  jmp 0x1408afd60
008B040F  41 BF 37 00 00 00               mov r15d, 0x37
008B0415  E9 46 F9 FF FF                  jmp 0x1408afd60
008B041A  41 BF 32 00 00 00               mov r15d, 0x32
008B0420  E9 3B F9 FF FF                  jmp 0x1408afd60
008B0425  41 BF 2D 00 00 00               mov r15d, 0x2d
008B042B  E9 30 F9 FF FF                  jmp 0x1408afd60
008B0430  41 BF 28 00 00 00               mov r15d, 0x28
008B0436  E9 25 F9 FF FF                  jmp 0x1408afd60
008B043B  41 BF 21 00 00 00               mov r15d, 0x21
008B0441  E9 1A F9 FF FF                  jmp 0x1408afd60
008B0446  41 BF 1E 00 00 00               mov r15d, 0x1e
008B044C  E9 0F F9 FF FF                  jmp 0x1408afd60
008B0451  41 FF C0                        inc r8d
008B0454  E9 71 FA FF FF                  jmp 0x1408afeca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfVerifyScenarioBuffer(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pB0;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 5614978)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_r12 = 0;
    v_stack_mF8 = (unsigned int)((unsigned int)(a2));
    v_stack_mF0 = a1;
    if (a2 < 296) goto loc_008B0157;
    if ((((unsigned __int8)(a1)) & (7)) != 0) goto loc_008B01F9;
    if ((*(unsigned int *)(a1)) != 31) goto loc_008B0162;
    if ((*(unsigned int *)(a1 + 4)) != 0x41434353ULL) goto loc_008B0162;
    if (((unsigned int)((unsigned int)(a2))) > 0x10000000ULL) goto loc_008B0204;
    if (((unsigned int)((unsigned int)(a2))) != (*(unsigned int *)(a1 + 12))) goto loc_008B020F;
    if ((*(unsigned int *)(a1 + 80)) > 1) goto loc_008B0178;
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)))) > 0x4000ULL) goto loc_008B0446;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112)))) > 0x4000ULL) goto loc_008B0446;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)))) > 0x100000ULL) goto loc_008B0446;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 104)))) > 0x400000ULL) goto loc_008B0446;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88))) == 0) goto loc_008B043B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96))) == 0) goto loc_008B043B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 104))) == 0) goto loc_008B043B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 204))) - 1);
    if (((unsigned int)(result)) > 7) goto loc_008B01CD;
    a1 = (a1) + (16);
    result = PfVerifyScenarioId(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 104)));
    if ((unsigned __int8)(result) == 0) goto loc_008B021A;
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 84))) + (a1);
    v_stack_mC8 = a2;
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_008B0225;
    if (a2 < a1) goto loc_008B0430;
    v_rbx = ((unsigned int)(a2)) + (a1);
    v_stack_mD8 = v_rbx;
    if (a2 >= v_rbx) goto loc_008B0430;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88))))) << (5);
    a1 = (a1) - 1;
    a1 = (a1) + (a2);
    if (a1 >= v_rbx) goto loc_008B0425;
    if (a1 < a1) goto loc_008B0425;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 92))) + (a1);
    v_stack_mE8 = a1;
    if ((((unsigned __int8)(a1)) & (3)) != 0) goto loc_008B0230;
    if (a1 >= v_rbx) goto loc_008B041A;
    if (a1 < a1) goto loc_008B041A;
    a1 = (a1 + (unsigned int)(*(unsigned int *)(a1 + 96)) * 8) - 1;
    if (a1 >= v_rbx) goto loc_008B040F;
    if (a1 < a1) goto loc_008B040F;
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 100))) + (a1);
    v_stack_mD0 = a3;
    if ((((unsigned __int8)(a3)) & (1)) != 0) goto loc_008B023B;
    if (a3 >= v_rbx) goto loc_008B01D8;
    if (a3 < a1) goto loc_008B01D8;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 104)) - 1) + (a3);
    if (a1 >= v_rbx) goto loc_008B0404;
    if (a1 < a1) goto loc_008B0404;
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 108))) + (a1);
    v_stack_m110 = a4;
    if ((((unsigned __int8)(a4)) & (7)) != 0) goto loc_008B0246;
    if (a4 >= v_rbx) goto loc_008B03F9;
    if (a4 < a1) goto loc_008B03F9;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 116))) - 1;
    a1 = (a1) + (a4);
    if (a1 >= v_rbx) goto loc_008B03EE;
    if (a1 < a1) goto loc_008B03EE;
    result = ((unsigned int)(*(unsigned int *)(a1 + 112)) + (unsigned int)(*(unsigned int *)(a1 + 112)) * 2) << (5);
    result = (result) - 1;
    result = (result) + (a4);
    if (result >= v_rbx) goto loc_008B03E3;
    if (result < a1) goto loc_008B03E3;
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)))) > 7) goto loc_008B0251;
loc_008AFBF9:
    v_stack_m114 = 0;
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88))))) goto loc_008AFE7A;
    a4 = (0) << (5);
    a4 = (a4) + (a2);
    v_stack_mE0 = a4;
    a2 = ((unsigned int)(*(unsigned int *)(a4 + 12))) + (a3);
    if ((((unsigned __int8)(a2)) & (1)) != 0) goto loc_008B01E3;
    if (a2 >= v_rbx) goto loc_008B02F1;
    if (a2 < a1) goto loc_008B02F1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))) == 0) goto loc_008B02E6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) > ((unsigned int)((unsigned int)(0x400ULL)))) goto loc_008B02DB;
    result = ((unsigned int)(*(unsigned int *)(a4 + 16)) * 2 + 2) - 1;
    result = (result) + (a2);
    if (result >= v_rbx) goto loc_008B02D0;
    if (result < a1) goto loc_008B02D0;
    if ((*(unsigned __int16 *)(a2 + (unsigned int)(*(unsigned int *)(a4 + 16)) * 2)) != 0) goto loc_008B02C5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))) > 0x8000ULL) goto loc_008B01C2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))) > ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96))))))) goto loc_008B02BA;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))));
    v_stack_m104 = (unsigned int)(v_r10);
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) == -1) goto loc_008B025C;
loc_008AFCA9:
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) != 0) goto loc_008B026F;
loc_008AFCB1:
    v_rbp = (unsigned int)((0) + ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))));
    v_stack_mFC = (unsigned int)(v_rbp);
    a1 = ((((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20)))) & (0x7F00ULL)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 20)))) & (1)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_008AFE65;
loc_008AFCD4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 20)))) & (1)) == 0) goto loc_008AFDFB;
loc_008AFCDE:
    v_stack_m118 = 0;
    a2 = (v_stack_mE8) + (4);
loc_008AFD02:
    if (((int)(*(unsigned int *)(a4))) >= ((int)((unsigned int)((int)(*(unsigned int *)(a4)) + (unsigned int)(*(unsigned int *)(a4 + 4)) * 1)))) goto loc_008AFD94;
    if (sign_flag) goto loc_008B0299;
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96))))) goto loc_008B0299;
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) == ((unsigned int)((int)(*(unsigned int *)(a4))))) goto loc_008AFD2E;
    if ((*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8 - 4)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8 - 12))))) goto loc_008B0283;
loc_008AFD2E:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8))))) >> (4));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8))))) & (1));
    if (condition_is_not_equal) goto loc_008AFD50;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (7));
    if (((unsigned int)(a1)) > v_stack_m108) goto loc_008B028E;
loc_008AFD50:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8)))) & (14)) != 0) goto loc_008AFE10;
loc_008AFD60:
    *(unsigned int *)(a3) = 173;
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2 + (int)(*(unsigned int *)(a4)) * 8, (unsigned int)(*(unsigned int *)(a2 + (int)(*(unsigned int *)(a4)) * 8)), a4);
    v_rsp = (v_rsp) + (272);
    return result;
loc_008AFD94:
    if (0 != (*(unsigned int *)(v_stack_p68 + 8))) goto loc_008B02AF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p68 + 20)))) & (1)) != 0) goto loc_008AFDCC;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 20))))) >> (1));
    result = (unsigned int)((result) & (127));
    if (v_stack_p30 != ((unsigned int)(result))) goto loc_008B02A4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 20))) >> (8));
    a1 = (unsigned int)((a1) & (127));
    if (0 != ((unsigned int)(a1))) goto loc_008B02A4;
loc_008AFDCC:
    result = (unsigned int)(((unsigned int)(v_stack_p34)) + 1);
    goto loc_008AFBF9;
loc_008AFDFB:
    if ((*(unsigned int *)(v_stack_p68 + 8)) != 173) goto loc_008AFCDE;
    goto loc_008AFD60;
loc_008AFE10:
    if ((unsigned int)(result) != 0) goto loc_008AFE54;
    v_rbp = (unsigned int)(((unsigned int)(v_stack_p4C)) + 1);
    if ((((unsigned __int8)(v_stack_p78)) & (4)) != 0) {
        a1 = (unsigned int)(v_stack_p68);
        result = 1;
        a1 = (unsigned int)((a1) & (7));
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    }
    v_r14 = 0;
    if ((((unsigned __int8)(v_stack_p78)) & (2)) != 0) {
        a4 = (unsigned int)((v_stack_p68) & (7));
        result = 1;
        a1 = (unsigned __int8)(a4);
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        v_r14 = (unsigned int)((0) | ((unsigned int)(result)));
    }
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p44)) + 1);
    v_r11 = (v_stack_p58) + 1;
    a2 = (v_stack_p80) + (8);
    goto loc_008AFD02;
loc_008AFE54:
    if ((((unsigned __int8)(v_stack_p78)) & (8)) == 0) goto loc_008AFE45;
    goto loc_008AFD60;
loc_008AFE65:
    if ((((unsigned __int8)(v_stack_p78)) & (254)) != 0) goto loc_008AFCD4;
    goto loc_008AFD60;
loc_008AFE7A:
    if ((unsigned int)(v_r10) != 0) goto loc_008B02FC;
    v_rsi = ((unsigned int)(v_stack_p50)) + (v_r11);
loc_008AFEA0:
    if (155 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 112))))) goto loc_008B00F5;
    v_rdi = (155 + 155 * 2) << (5);
    v_rdi = (v_rdi) + (v_stack_p38);
loc_008AFECA:
    if (((unsigned int)(155 + 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 112))))) goto loc_008B0199;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rdi))) + (v_stack_p38);
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_008B01EE;
    if (v_rbx >= v_rsi) goto loc_008B03C2;
    if (v_rbx < v_r11) goto loc_008B03C2;
    if ((v_rbx + (unsigned int)(*(unsigned int *)(v_rdi + 4)) * 2 + 1) >= v_rsi) goto loc_008B03B7;
    if ((v_rbx + (unsigned int)(*(unsigned int *)(v_rdi + 4)) * 2 + 1) < v_r11) goto loc_008B03B7;
    if ((*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rdi + 4)) * 2)) != 155) goto loc_008B03AC;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)));
    result = StringCchPrintfW(v_stack_pB0, 35, v_rip + 2430570, (unsigned int)(*(unsigned int *)(v_rdi + 12)));
    a2 = (v_stack_pB0) - (v_rbx);
loc_008AFF52:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbx)) - ((unsigned int)(*(unsigned __int16 *)(v_rbx + a2 * 1))));
    if (condition_is_not_equal) goto loc_008AFF65;
    v_rbx = (v_rbx) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(v_rbx + a2 * 1)) != 0) goto loc_008AFF52;
loc_008AFF65:
    if ((unsigned int)(a1) != 0) goto loc_008B018E;
    a1 = ((unsigned int)(*(unsigned int *)(v_rdi + 20))) + (v_stack_p38);
    if ((((unsigned __int8)(a1)) & (7)) != 0) goto loc_008B03A1;
    if (a1 >= v_rsi) goto loc_008B0396;
    if (a1 < v_stack_p58) goto loc_008B0396;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24)))) < 24) goto loc_008B038B;
    a2 = ((unsigned int)(*(unsigned int *)(v_rdi + 24)) - 1) + (a1);
    if (a2 >= v_rsi) goto loc_008B0380;
    if (a2 < v_stack_p58) goto loc_008B0380;
    if ((*(unsigned int *)(a1)) != 3) goto loc_008B0375;
    if ((*(unsigned int *)(a1 + 4)) > 0x84000ULL) goto loc_008B036A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 124))) != 0) goto loc_008B00B8;
loc_008AFFE2:
    if (155 != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_008B0183;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) {
        a1 = (unsigned int)(*(unsigned int *)(a1 + 4)) * 8 + 16;
    }
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rdi + 24))) goto loc_008B035F;
    if ((*(unsigned int *)(v_rdi + 32)) > 0x80000ULL) goto loc_008B0354;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 124))) != 0) goto loc_008B00DC;
loc_008B0022:
    if (155 != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32))))) goto loc_008B0349;
    v_r14 = (unsigned int)((155) + (155));
    a1 = ((unsigned int)(*(unsigned int *)(v_rdi + 28))) + (v_stack_p38);
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_008B033E;
loc_008B0044:
    if (155 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32))))) goto loc_008B00B1;
    if (a1 >= v_rsi) goto loc_008B0333;
    if (a1 < v_stack_p58) goto loc_008B0333;
    if ((a1 + 3) >= v_rsi) goto loc_008B0328;
    if ((a1 + 3) < v_stack_p58) goto loc_008B0328;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) >= ((unsigned __int16)((unsigned int)(0x400ULL)))) goto loc_008B031D;
    if ((a1 + *(unsigned __int16 *)(a1) * 2 + 3) >= v_rsi) goto loc_008B0312;
    if ((a1 + *(unsigned __int16 *)(a1) * 2 + 3) < v_stack_p58) goto loc_008B0312;
    if ((*(unsigned __int16 *)(a1 + *(unsigned __int16 *)(a1) * 2 + 2)) != 155) goto loc_008B0307;
    a2 = (unsigned int)((155) + 1);
    a1 = (a1 + *(unsigned __int16 *)(a1) * 2) + (4);
    goto loc_008B0044;
loc_008B00B1:
    v_rbp = (unsigned int)((155) + 1);
    goto loc_008AFEA0;
loc_008B00B8:
loc_008B00BF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 36 + 28))) + (*(unsigned int *)(v_rdi + 36)));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    a4 = (a1 + *(unsigned __int16 *)(a1) * 2 + 3) - (1);
    if (condition_is_not_equal) goto loc_008B00BF;
    goto loc_008AFFE2;
loc_008B00DC:
loc_008B00E3:
    result = (unsigned int)((result) + (*(unsigned int *)(v_rdi + 64)));
    a3 = (a1) - (1);
    if (condition_is_equal) goto loc_008B0022;
    goto loc_008B00E3;
loc_008B00F5:
    if (((unsigned int)(v_r14)) != (*(unsigned int *)(v_stack_p58 + 120))) goto loc_008B03CD;
    if (((unsigned int)(v_r14)) > 0x80000ULL) goto loc_008B03D8;
    a1 = ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 216))) == 0) ? 1 : 0;
    result = ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 212))) == 0) ? 1 : 0;
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_008B016D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 212))) == 0) goto loc_008B0144;
    a3 = 0;
    result = StringCbLengthW(v_stack_p58 + (unsigned int)(*(unsigned int *)(v_stack_p58 + 212)) * 1, (unsigned int)(*(unsigned int *)(v_stack_p58 + 216)), a3, v_stack_p38);
    if (sign_flag) goto loc_008B014C;
loc_008B0144:
    goto loc_008AFD60;
loc_008B014C:
    goto loc_008AFD60;
loc_008B0157:
    goto loc_008AFD60;
loc_008B0162:
    goto loc_008AFD60;
loc_008B016D:
    goto loc_008AFD60;
loc_008B0178:
    goto loc_008AFD60;
loc_008B0183:
    goto loc_008AFD60;
loc_008B018E:
    goto loc_008AFD60;
loc_008B0199:
    v_r10 = (a3 + a3 * 2) << (5);
    if ((*(unsigned __int64 *)(v_r10 + v_rbx * 1 + 8)) != result) goto loc_008B0451;
    if ((*(unsigned int *)(v_r10 + v_rbx * 1 + 16)) != ((unsigned int)(v_stack_p38))) goto loc_008B0451;
    goto loc_008AFD60;
loc_008B01C2:
    goto loc_008AFD60;
loc_008B01CD:
    goto loc_008AFD60;
loc_008B01D8:
    goto loc_008AFD60;
loc_008B01E3:
    goto loc_008AFD60;
loc_008B01EE:
    goto loc_008AFD60;
loc_008B01F9:
    goto loc_008AFD60;
loc_008B0204:
    goto loc_008AFD60;
loc_008B020F:
    goto loc_008AFD60;
loc_008B021A:
    goto loc_008AFD60;
loc_008B0225:
    goto loc_008AFD60;
loc_008B0230:
    goto loc_008AFD60;
loc_008B023B:
    goto loc_008AFD60;
loc_008B0246:
    goto loc_008AFD60;
loc_008B0251:
    goto loc_008AFD60;
loc_008B025C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 216))) == 0) goto loc_008AFCA9;
    goto loc_008AFD60;
loc_008B026F:
    if (((unsigned int)(v_rbx)) == -1) goto loc_008AFCB1;
    goto loc_008AFD60;
loc_008B0283:
    goto loc_008AFD60;
loc_008B028E:
    goto loc_008AFD60;
loc_008B0299:
    goto loc_008AFD60;
loc_008B02A4:
    goto loc_008AFD60;
loc_008B02AF:
    goto loc_008AFD60;
loc_008B02BA:
    goto loc_008AFD60;
loc_008B02C5:
    goto loc_008AFD60;
loc_008B02D0:
    goto loc_008AFD60;
loc_008B02DB:
    goto loc_008AFD60;
loc_008B02E6:
    goto loc_008AFD60;
loc_008B02F1:
    goto loc_008AFD60;
loc_008B02FC:
    goto loc_008AFD60;
loc_008B0307:
    goto loc_008AFD60;
loc_008B0312:
    goto loc_008AFD60;
loc_008B031D:
    goto loc_008AFD60;
loc_008B0328:
    goto loc_008AFD60;
loc_008B0333:
    goto loc_008AFD60;
loc_008B033E:
    goto loc_008AFD60;
loc_008B0349:
    goto loc_008AFD60;
loc_008B0354:
    goto loc_008AFD60;
loc_008B035F:
    goto loc_008AFD60;
loc_008B036A:
    goto loc_008AFD60;
loc_008B0375:
    goto loc_008AFD60;
loc_008B0380:
    goto loc_008AFD60;
loc_008B038B:
    goto loc_008AFD60;
loc_008B0396:
    goto loc_008AFD60;
loc_008B03A1:
    goto loc_008AFD60;
loc_008B03AC:
    goto loc_008AFD60;
loc_008B03B7:
    goto loc_008AFD60;
loc_008B03C2:
    goto loc_008AFD60;
loc_008B03CD:
    goto loc_008AFD60;
loc_008B03D8:
    goto loc_008AFD60;
loc_008B03E3:
    goto loc_008AFD60;
loc_008B03EE:
    goto loc_008AFD60;
loc_008B03F9:
    goto loc_008AFD60;
loc_008B0404:
    goto loc_008AFD60;
loc_008B040F:
    goto loc_008AFD60;
loc_008B041A:
    goto loc_008AFD60;
loc_008B0425:
    goto loc_008AFD60;
loc_008B0430:
    goto loc_008AFD60;
loc_008B043B:
    goto loc_008AFD60;
loc_008B0446:
    goto loc_008AFD60;
loc_008B0451:
    a3 = (unsigned int)((a3) + 1);
    goto loc_008AFECA;
}
```

## 5. (Beta) C Style

```c
int64_t PfVerifyScenarioBuffer(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_pB0;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x55AD82)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    local_r12 = 0;
    v_stack_mF8 = (uint32_t)((uint32_t)(Arg2));
    v_stack_mF0 = Arg1;
    if (Arg2 < 296) goto loc_008B0157;
    if ((((uint8_t)(Arg1)) & (7)) != 0) goto loc_008B01F9;
    if ((*(uint32_t *)(arg1)) != 31) goto loc_008B0162;
    if ((*(uint32_t *)(arg1 + 0x4)) != 0x41434353ULL) goto loc_008B0162;
    if (((uint32_t)((uint32_t)(Arg2))) > 0x10000000ULL) goto loc_008B0204;
    if (((uint32_t)((uint32_t)(Arg2))) != (*(uint32_t *)(arg1 + 0xC))) goto loc_008B020F;
    if ((*(uint32_t *)(arg1 + 0x50)) > 1) goto loc_008B0178;
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)))) > 0x4000ULL) goto loc_008B0446;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) > 0x4000ULL) goto loc_008B0446;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)))) > 0x100000ULL) goto loc_008B0446;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)))) > 0x400000ULL) goto loc_008B0446;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58))) == 0) goto loc_008B043B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60))) == 0) goto loc_008B043B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68))) == 0) goto loc_008B043B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xCC))) - 1);
    if (((uint32_t)(result)) > 7) goto loc_008B01CD;
    Arg1 = (Arg1) + (16);
    result = PfVerifyScenarioId(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x68)));
    if ((uint8_t)(result) == 0) goto loc_008B021A;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x54))) + (Arg1);
    v_stack_mC8 = Arg2;
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_008B0225;
    if (Arg2 < Arg1) goto loc_008B0430;
    local_rbx = ((uint32_t)(Arg2)) + (Arg1);
    v_stack_mD8 = local_rbx;
    if (Arg2 >= local_rbx) goto loc_008B0430;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58))))) << (5);
    Arg1 = (Arg1) - 1;
    Arg1 = (Arg1) + (Arg2);
    if (Arg1 >= local_rbx) goto loc_008B0425;
    if (Arg1 < Arg1) goto loc_008B0425;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x5C))) + (Arg1);
    v_stack_mE8 = Arg1;
    if ((((uint8_t)(Arg1)) & (3)) != 0) goto loc_008B0230;
    if (Arg1 >= local_rbx) goto loc_008B041A;
    if (Arg1 < Arg1) goto loc_008B041A;
    Arg1 = (Arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x60)) * 8) - 1;
    if (Arg1 >= local_rbx) goto loc_008B040F;
    if (Arg1 < Arg1) goto loc_008B040F;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x64))) + (Arg1);
    v_stack_mD0 = Arg3;
    if ((((uint8_t)(Arg3)) & (1)) != 0) goto loc_008B023B;
    if (Arg3 >= local_rbx) goto loc_008B01D8;
    if (Arg3 < Arg1) goto loc_008B01D8;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x68)) - 1) + (Arg3);
    if (Arg1 >= local_rbx) goto loc_008B0404;
    if (Arg1 < Arg1) goto loc_008B0404;
    a4 = ((uint32_t)(*(uint32_t *)(arg1 + 0x6C))) + (Arg1);
    v_stack_m110 = a4;
    if ((((uint8_t)(a4)) & (7)) != 0) goto loc_008B0246;
    if (a4 >= local_rbx) goto loc_008B03F9;
    if (a4 < Arg1) goto loc_008B03F9;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x74))) - 1;
    Arg1 = (Arg1) + (a4);
    if (Arg1 >= local_rbx) goto loc_008B03EE;
    if (Arg1 < Arg1) goto loc_008B03EE;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x70)) + (uint32_t)(*(uint32_t *)(arg1 + 0x70)) * 2) << (5);
    result = (result) - 1;
    result = (result) + (a4);
    if (result >= local_rbx) goto loc_008B03E3;
    if (result < Arg1) goto loc_008B03E3;
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)))) > 7) goto loc_008B0251;
loc_008AFBF9:
    v_stack_m114 = 0;
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58))))) goto loc_008AFE7A;
    a4 = (0) << (5);
    a4 = (a4) + (Arg2);
    v_stack_mE0 = a4;
    Arg2 = ((uint32_t)(*(uint32_t *)(a4 + 0xC))) + (Arg3);
    if ((((uint8_t)(Arg2)) & (1)) != 0) goto loc_008B01E3;
    if (Arg2 >= local_rbx) goto loc_008B02F1;
    if (Arg2 < Arg1) goto loc_008B02F1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x10))) == 0) goto loc_008B02E6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x10)))) > ((uint32_t)((uint32_t)(0x400ULL)))) goto loc_008B02DB;
    result = ((uint32_t)(*(uint32_t *)(a4 + 0x10)) * 2 + 2) - 1;
    result = (result) + (Arg2);
    if (result >= local_rbx) goto loc_008B02D0;
    if (result < Arg1) goto loc_008B02D0;
    if ((*(uint16_t *)(Arg2 + (uint32_t)(*(uint32_t *)(a4 + 0x10)) * 2)) != 0) goto loc_008B02C5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))) > 0x8000ULL) goto loc_008B01C2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))) > ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60))))))) goto loc_008B02BA;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))));
    v_stack_m104 = (uint32_t)(local_r10);
    if (((uint32_t)((int32_t)(*(uint32_t *)(a4)))) == -1) goto loc_008B025C;
loc_008AFCA9:
    if (((uint32_t)((int32_t)(*(uint32_t *)(a4)))) != 0) goto loc_008B026F;
loc_008AFCB1:
    local_rbp = (uint32_t)((0) + ((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x4)))));
    v_stack_mFC = (uint32_t)(local_rbp);
    Arg1 = ((((uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x14)))) & (0x7F00ULL)) == 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(a4 + 0x14)))) & (1)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_008AFE65;
loc_008AFCD4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(a4 + 0x14)))) & (1)) == 0) goto loc_008AFDFB;
loc_008AFCDE:
    v_stack_m118 = 0;
    Arg2 = (v_stack_mE8) + (4);
loc_008AFD02:
    if (((int32_t)(*(uint32_t *)(a4))) >= ((int32_t)((uint32_t)((int32_t)(*(uint32_t *)(a4)) + (uint32_t)(*(uint32_t *)(a4 + 0x4)) * 1)))) goto loc_008AFD94;
    if (sign_flag) goto loc_008B0299;
    if (((uint32_t)((int32_t)(*(uint32_t *)(a4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60))))) goto loc_008B0299;
    if (((uint32_t)((int32_t)(*(uint32_t *)(a4)))) == ((uint32_t)((int32_t)(*(uint32_t *)(a4))))) goto loc_008AFD2E;
    if ((*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8 - 0x4)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8 - 0xC))))) goto loc_008B0283;
loc_008AFD2E:
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8))))) >> (4));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8))))) & (1));
    if (condition_is_not_equal) goto loc_008AFD50;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a4))) & (7));
    if (((uint32_t)(Arg1)) > v_stack_m108) goto loc_008B028E;
loc_008AFD50:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8)))) & (14)) != 0) goto loc_008AFE10;
loc_008AFD60:
    *(uint32_t *)(arg3) = 173;
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8, (uint32_t)(*(uint32_t *)(Arg2 + (int32_t)(*(uint32_t *)(a4)) * 8)), a4);
    local_rsp = (local_rsp) + (272);
    return result;
loc_008AFD94:
    if (0 != (*(uint32_t *)(v_stack_p68 + 0x8))) goto loc_008B02AF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x14)))) & (1)) != 0) goto loc_008AFDCC;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x14))))) >> (1));
    result = (uint32_t)((result) & (127));
    if (v_stack_p30 != ((uint32_t)(result))) goto loc_008B02A4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x14))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (127));
    if (0 != ((uint32_t)(Arg1))) goto loc_008B02A4;
loc_008AFDCC:
    result = (uint32_t)(((uint32_t)(v_stack_p34)) + 1);
    goto loc_008AFBF9;
loc_008AFDFB:
    if ((*(uint32_t *)(v_stack_p68 + 0x8)) != 173) goto loc_008AFCDE;
    goto loc_008AFD60;
loc_008AFE10:
    if ((uint32_t)(result) != 0) goto loc_008AFE54;
    local_rbp = (uint32_t)(((uint32_t)(v_stack_p4C)) + 1);
    if ((((uint8_t)(v_stack_p78)) & (4)) != 0) {
        Arg1 = (uint32_t)(v_stack_p68);
        result = 1;
        Arg1 = (uint32_t)((Arg1) & (7));
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    }
    local_r14 = 0;
    if ((((uint8_t)(v_stack_p78)) & (2)) != 0) {
        a4 = (uint32_t)((v_stack_p68) & (7));
        result = 1;
        Arg1 = (uint8_t)(a4);
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        local_r14 = (uint32_t)((0) | ((uint32_t)(result)));
    }
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p44)) + 1);
    local_r11 = (v_stack_p58) + 1;
    Arg2 = (v_stack_p80) + (8);
    goto loc_008AFD02;
loc_008AFE54:
    if ((((uint8_t)(v_stack_p78)) & (8)) == 0) goto loc_008AFE45;
    goto loc_008AFD60;
loc_008AFE65:
    if ((((uint8_t)(v_stack_p78)) & (254)) != 0) goto loc_008AFCD4;
    goto loc_008AFD60;
loc_008AFE7A:
    if ((uint32_t)(local_r10) != 0) goto loc_008B02FC;
    local_rsi = ((uint32_t)(v_stack_p50)) + (local_r11);
loc_008AFEA0:
    if (155 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x70))))) goto loc_008B00F5;
    local_rdi = (155 + 155 * 2) << (5);
    local_rdi = (local_rdi) + (v_stack_p38);
loc_008AFECA:
    if (((uint32_t)(155 + 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x70))))) goto loc_008B0199;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rdi))) + (v_stack_p38);
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_008B01EE;
    if (local_rbx >= local_rsi) goto loc_008B03C2;
    if (local_rbx < local_r11) goto loc_008B03C2;
    if ((local_rbx + (uint32_t)(*(uint32_t *)(local_rdi + 0x4)) * 2 + 1) >= local_rsi) goto loc_008B03B7;
    if ((local_rbx + (uint32_t)(*(uint32_t *)(local_rdi + 0x4)) * 2 + 1) < local_r11) goto loc_008B03B7;
    if ((*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(local_rdi + 0x4)) * 2)) != 155) goto loc_008B03AC;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)));
    result = StringCchPrintfW(v_stack_pB0, 35, v_rip + 2430570, (uint32_t)(*(uint32_t *)(local_rdi + 0xC)));
    Arg2 = (v_stack_pB0) - (local_rbx);
loc_008AFF52:
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbx)) - ((uint32_t)(*(uint16_t *)(local_rbx + Arg2 * 1))));
    if (condition_is_not_equal) goto loc_008AFF65;
    local_rbx = (local_rbx) + (2);
    if ((uint32_t)(*(uint16_t *)(local_rbx + Arg2 * 1)) != 0) goto loc_008AFF52;
loc_008AFF65:
    if ((uint32_t)(Arg1) != 0) goto loc_008B018E;
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x14))) + (v_stack_p38);
    if ((((uint8_t)(Arg1)) & (7)) != 0) goto loc_008B03A1;
    if (Arg1 >= local_rsi) goto loc_008B0396;
    if (Arg1 < v_stack_p58) goto loc_008B0396;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)))) < 24) goto loc_008B038B;
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x18)) - 1) + (Arg1);
    if (Arg2 >= local_rsi) goto loc_008B0380;
    if (Arg2 < v_stack_p58) goto loc_008B0380;
    if ((*(uint32_t *)(arg1)) != 3) goto loc_008B0375;
    if ((*(uint32_t *)(arg1 + 0x4)) > 0x84000ULL) goto loc_008B036A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x7C))) != 0) goto loc_008B00B8;
loc_008AFFE2:
    if (155 != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_008B0183;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) {
        Arg1 = (uint32_t)(*(uint32_t *)(arg1 + 0x4)) * 8 + 16;
    }
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(local_rdi + 0x18))) goto loc_008B035F;
    if ((*(uint32_t *)(local_rdi + 0x20)) > 0x80000ULL) goto loc_008B0354;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x7C))) != 0) goto loc_008B00DC;
loc_008B0022:
    if (155 != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20))))) goto loc_008B0349;
    local_r14 = (uint32_t)((155) + (155));
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x1C))) + (v_stack_p38);
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_008B033E;
loc_008B0044:
    if (155 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20))))) goto loc_008B00B1;
    if (Arg1 >= local_rsi) goto loc_008B0333;
    if (Arg1 < v_stack_p58) goto loc_008B0333;
    if ((Arg1 + 3) >= local_rsi) goto loc_008B0328;
    if ((Arg1 + 3) < v_stack_p58) goto loc_008B0328;
    if (((uint16_t)(*(uint16_t *)(arg1))) >= ((uint16_t)((uint32_t)(0x400ULL)))) goto loc_008B031D;
    if ((Arg1 + *(uint16_t *)(arg1) * 2 + 3) >= local_rsi) goto loc_008B0312;
    if ((Arg1 + *(uint16_t *)(arg1) * 2 + 3) < v_stack_p58) goto loc_008B0312;
    if ((*(uint16_t *)(arg1 + *(uint16_t *)(arg1) * 2 + 0x2)) != 155) goto loc_008B0307;
    Arg2 = (uint32_t)((155) + 1);
    Arg1 = (Arg1 + *(uint16_t *)(arg1) * 2) + (4);
    goto loc_008B0044;
loc_008B00B1:
    local_rbp = (uint32_t)((155) + 1);
    goto loc_008AFEA0;
loc_008B00B8:
loc_008B00BF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x24 + 0x1C))) + (*(uint32_t *)(local_rdi + 0x24)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    a4 = (Arg1 + *(uint16_t *)(arg1) * 2 + 3) - (1);
    if (condition_is_not_equal) goto loc_008B00BF;
    goto loc_008AFFE2;
loc_008B00DC:
loc_008B00E3:
    result = (uint32_t)((result) + (*(uint32_t *)(local_rdi + 0x40)));
    Arg3 = (Arg1) - (1);
    if (condition_is_equal) goto loc_008B0022;
    goto loc_008B00E3;
loc_008B00F5:
    if (((uint32_t)(local_r14)) != (*(uint32_t *)(v_stack_p58 + 0x78))) goto loc_008B03CD;
    if (((uint32_t)(local_r14)) > 0x80000ULL) goto loc_008B03D8;
    Arg1 = ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD8))) == 0) ? 1 : 0;
    result = ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD4))) == 0) ? 1 : 0;
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_008B016D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD4))) == 0) goto loc_008B0144;
    Arg3 = 0;
    result = StringCbLengthW(v_stack_p58 + (uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD4)) * 1, (uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD8)), Arg3, v_stack_p38);
    if (sign_flag) goto loc_008B014C;
loc_008B0144:
    goto loc_008AFD60;
loc_008B014C:
    goto loc_008AFD60;
loc_008B0157:
    goto loc_008AFD60;
loc_008B0162:
    goto loc_008AFD60;
loc_008B016D:
    goto loc_008AFD60;
loc_008B0178:
    goto loc_008AFD60;
loc_008B0183:
    goto loc_008AFD60;
loc_008B018E:
    goto loc_008AFD60;
loc_008B0199:
    local_r10 = (Arg3 + Arg3 * 2) << (5);
    if ((*(uint64_t *)(local_r10 + local_rbx * 1 + 0x8)) != result) goto loc_008B0451;
    if ((*(uint32_t *)(local_r10 + local_rbx * 1 + 0x10)) != ((uint32_t)(v_stack_p38))) goto loc_008B0451;
    goto loc_008AFD60;
loc_008B01C2:
    goto loc_008AFD60;
loc_008B01CD:
    goto loc_008AFD60;
loc_008B01D8:
    goto loc_008AFD60;
loc_008B01E3:
    goto loc_008AFD60;
loc_008B01EE:
    goto loc_008AFD60;
loc_008B01F9:
    goto loc_008AFD60;
loc_008B0204:
    goto loc_008AFD60;
loc_008B020F:
    goto loc_008AFD60;
loc_008B021A:
    goto loc_008AFD60;
loc_008B0225:
    goto loc_008AFD60;
loc_008B0230:
    goto loc_008AFD60;
loc_008B023B:
    goto loc_008AFD60;
loc_008B0246:
    goto loc_008AFD60;
loc_008B0251:
    goto loc_008AFD60;
loc_008B025C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD8))) == 0) goto loc_008AFCA9;
    goto loc_008AFD60;
loc_008B026F:
    if (((uint32_t)(local_rbx)) == -1) goto loc_008AFCB1;
    goto loc_008AFD60;
loc_008B0283:
    goto loc_008AFD60;
loc_008B028E:
    goto loc_008AFD60;
loc_008B0299:
    goto loc_008AFD60;
loc_008B02A4:
    goto loc_008AFD60;
loc_008B02AF:
    goto loc_008AFD60;
loc_008B02BA:
    goto loc_008AFD60;
loc_008B02C5:
    goto loc_008AFD60;
loc_008B02D0:
    goto loc_008AFD60;
loc_008B02DB:
    goto loc_008AFD60;
loc_008B02E6:
    goto loc_008AFD60;
loc_008B02F1:
    goto loc_008AFD60;
loc_008B02FC:
    goto loc_008AFD60;
loc_008B0307:
    goto loc_008AFD60;
loc_008B0312:
    goto loc_008AFD60;
loc_008B031D:
    goto loc_008AFD60;
loc_008B0328:
    goto loc_008AFD60;
loc_008B0333:
    goto loc_008AFD60;
loc_008B033E:
    goto loc_008AFD60;
loc_008B0349:
    goto loc_008AFD60;
loc_008B0354:
    goto loc_008AFD60;
loc_008B035F:
    goto loc_008AFD60;
loc_008B036A:
    goto loc_008AFD60;
loc_008B0375:
    goto loc_008AFD60;
loc_008B0380:
    goto loc_008AFD60;
loc_008B038B:
    goto loc_008AFD60;
loc_008B0396:
    goto loc_008AFD60;
loc_008B03A1:
    goto loc_008AFD60;
loc_008B03AC:
    goto loc_008AFD60;
loc_008B03B7:
    goto loc_008AFD60;
loc_008B03C2:
    goto loc_008AFD60;
loc_008B03CD:
    goto loc_008AFD60;
loc_008B03D8:
    goto loc_008AFD60;
loc_008B03E3:
    goto loc_008AFD60;
loc_008B03EE:
    goto loc_008AFD60;
loc_008B03F9:
    goto loc_008AFD60;
loc_008B0404:
    goto loc_008AFD60;
loc_008B040F:
    goto loc_008AFD60;
loc_008B041A:
    goto loc_008AFD60;
loc_008B0425:
    goto loc_008AFD60;
loc_008B0430:
    goto loc_008AFD60;
loc_008B043B:
    goto loc_008AFD60;
loc_008B0446:
    goto loc_008AFD60;
loc_008B0451:
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_008AFECA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0xCC` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AF9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
