# LocalGetConditionForString

- RVA: `0x00A01C20`–`0x00A02427` (길이 `2,055` bytes)
- VA: `0x0000000140A01C20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7E98`
- 디코드: `511`개 명령, `2,055/2,055` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A01D29` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A01D48` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A01D75` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00A01D96` → [GetConditionToken](GetConditionToken_function_00A02430.md) (function, `0x00A02430`)
- `0x00A01EA5` → [GetOperandValue](GetOperandValue_function_00A024C0.md) (function, `0x00A024C0`)
- `0x00A01EDB` → [AppendCondition](AppendCondition_function_00A026B4.md) (function, `0x00A026B4`)
- `0x00A01EF3` → [IsValueSizeFixed](IsValueSizeFixed_function_00A02664.md) (function, `0x00A02664`)
- `0x00A01F13` → [AppendCondition](AppendCondition_function_00A026B4.md) (function, `0x00A026B4`)
- `0x00A01F42` → [AppendCondition](AppendCondition_function_00A026B4.md) (function, `0x00A026B4`)
- `0x00A01F59` → [FreeOperandValue](FreeOperandValue_function_00A0262C.md) (function, `0x00A0262C`)
- `0x00A01FC2` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A02039` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A0204E` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A020A3` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A0218A` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A021DE` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A02218` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A02233` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A02240` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A022B2` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A022D2` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A022F1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A022FE` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A02384` → [IsArrayType](../7A/IsArrayType_function_007A58FC.md) (function, `0x007A58FC`)
- `0x00A023F5` → [AppendCondition](AppendCondition_function_00A026B4.md) (function, `0x00A026B4`)
- `0x00A02409` → [FreeOperandValue](FreeOperandValue_function_00A0262C.md) (function, `0x00A0262C`)

### Direct callers
- [LocalGetAclForString](../92/LocalGetAclForString_function_00927F30.md) at `0x00928ACC`

### Static image references
- `0x00A01C3C` → RVA `0x00E0A740` (`.data`; read)
- `0x00A01FCA` → RVA `0x00002BB0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00A01D29` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A01D75` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00A02233` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A022F1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x00A02207` → [sub_00B32FA8 + 0x20](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A02340` → [sub_00B32FA8](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A0234B` → [sub_00B32FA8](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A02357` → [sub_00B32FA8](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A02363` → [sub_00B32FA8](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A023D7` → [sub_00B32FA8 + 0x16](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)
  - `0x00A02418` → [sub_00B32FA8 + 0x20](../B3/Unknown_function_00B32FA8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A01C20  40 55                           push rbp
00A01C22  53                              push rbx
00A01C23  56                              push rsi
00A01C24  57                              push rdi
00A01C25  41 54                           push r12
00A01C27  41 55                           push r13
00A01C29  41 56                           push r14
00A01C2B  41 57                           push r15
00A01C2D  48 8D AC 24 68 FF FF FF         lea rbp, [rsp - 0x98]
00A01C35  48 81 EC 98 01 00 00            sub rsp, 0x198
00A01C3C  48 8B 05 FD 8A 40 00            mov rax, qword ptr [rip + 0x408afd]
00A01C43  48 33 C4                        xor rax, rsp
00A01C46  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00A01C4D  4C 8B E1                        mov r12, rcx
00A01C50  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00A01C55  33 C9                           xor ecx, ecx
00A01C57  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00A01C5C  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00A01C61  4D 8B F1                        mov r14, r9
00A01C64  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
00A01C68  4D 8B F8                        mov r15, r8
00A01C6B  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
00A01C6F  48 8B C2                        mov rax, rdx
00A01C72  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00A01C77  8B F1                           mov esi, ecx
00A01C79  88 4C 24 51                     mov byte ptr [rsp + 0x51], cl
00A01C7D  8B D9                           mov ebx, ecx
00A01C7F  88 4C 24 52                     mov byte ptr [rsp + 0x52], cl
00A01C83  8B F9                           mov edi, ecx
00A01C85  44 8B E9                        mov r13d, ecx
00A01C88  4D 85 E4                        test r12, r12
00A01C8B  0F 84 8C 07 00 00               je 0x140a0241d
00A01C91  48 85 C0                        test rax, rax
00A01C94  0F 84 83 07 00 00               je 0x140a0241d
00A01C9A  4D 85 C0                        test r8, r8
00A01C9D  0F 84 7A 07 00 00               je 0x140a0241d
00A01CA3  4D 85 C9                        test r9, r9
00A01CA6  0F 84 71 07 00 00               je 0x140a0241d
00A01CAC  49 89 08                        mov qword ptr [r8], rcx
00A01CAF  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A01CB3  41 89 09                        mov dword ptr [r9], ecx
00A01CB6  48 FF C0                        inc rax
00A01CB9  66 41 39 0C 44                  cmp word ptr [r12 + rax*2], cx
00A01CBE  75 F6                           jne 0x140a01cb6
00A01CC0  83 F8 03                        cmp eax, 3
00A01CC3  0F 82 39 05 00 00               jb 0x140a02202
00A01CC9  66 41 83 3C 24 28               cmp word ptr [r12], 0x28
00A01CCF  0F 85 2D 05 00 00               jne 0x140a02202
00A01CD5  FF C0                           inc eax
00A01CD7  BA FF FF FF FF                  mov edx, 0xffffffff
00A01CDC  83 F8 01                        cmp eax, 1
00A01CDF  8B CA                           mov ecx, edx
00A01CE1  0F 43 C8                        cmovae ecx, eax
00A01CE4  41 89 09                        mov dword ptr [r9], ecx
00A01CE7  72 0D                           jb 0x140a01cf6
00A01CE9  8B C1                           mov eax, ecx
00A01CEB  48 03 C0                        add rax, rax
00A01CEE  48 3B C2                        cmp rax, rdx
00A01CF1  76 50                           jbe 0x140a01d43
00A01CF3  41 89 11                        mov dword ptr [r9], edx
00A01CF6  BB 16 02 00 00                  mov ebx, 0x216
00A01CFB  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A01D00  33 F6                           xor esi, esi
00A01D02  48 85 C9                        test rcx, rcx
00A01D05  0F 85 FE 06 00 00               jne 0x140a02409
00A01D0B  41 83 3E 04                     cmp dword ptr [r14], 4
00A01D0F  0F 84 FE 06 00 00               je 0x140a02413
00A01D15  85 DB                           test ebx, ebx
00A01D17  0F 85 F6 06 00 00               jne 0x140a02413
00A01D1D  8B C3                           mov eax, ebx
00A01D1F  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00A01D26  48 33 CC                        xor rcx, rsp
00A01D29  E8 12 A9 CA FF                  call 0x1406ac640
00A01D2E  48 81 C4 98 01 00 00            add rsp, 0x198
00A01D35  41 5F                           pop r15
00A01D37  41 5E                           pop r14
00A01D39  41 5D                           pop r13
00A01D3B  41 5C                           pop r12
00A01D3D  5F                              pop rdi
00A01D3E  5E                              pop rsi
00A01D3F  5B                              pop rbx
00A01D40  5D                              pop rbp
00A01D41  C3                              ret
00A01D42  CC                              int3
00A01D43  8B C8                           mov ecx, eax
00A01D45  41 89 09                        mov dword ptr [r9], ecx
00A01D48  E8 3B 42 F2 FF                  call 0x140925f88
00A01D4D  49 89 07                        mov qword ptr [r15], rax
00A01D50  48 85 C0                        test rax, rax
00A01D53  0F 84 B3 04 00 00               je 0x140a0220c
00A01D59  C7 00 61 72 74 78               mov dword ptr [rax], 0x78747261
00A01D5F  C7 44 24 54 04 00 00 00         mov dword ptr [rsp + 0x54], 4
00A01D67  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00A01D6C  66 85 C9                        test cx, cx
00A01D6F  0F 84 2A 02 00 00               je 0x140a01f9f
00A01D75  E8 86 EA AF FF                  call 0x140500800
00A01D7A  85 C0                           test eax, eax
00A01D7C  0F 85 F2 02 00 00               jne 0x140a02074
00A01D82  81 FE FF 00 00 00               cmp esi, 0xff
00A01D88  0F 84 32 06 00 00               je 0x140a023c0
00A01D8E  48 8D 54 24 64                  lea rdx, [rsp + 0x64]
00A01D93  49 8B CC                        mov rcx, r12
00A01D96  E8 95 06 00 00                  call 0x140a02430
00A01D9B  33 C9                           xor ecx, ecx
00A01D9D  44 8A E0                        mov r12b, al
00A01DA0  84 C0                           test al, al
00A01DA2  0F 84 94 00 00 00               je 0x140a01e3c
00A01DA8  3C FE                           cmp al, 0xfe
00A01DAA  0F 84 5E 03 00 00               je 0x140a0210e
00A01DB0  4C 63 FE                        movsxd r15, esi
00A01DB3  3C FF                           cmp al, 0xff
00A01DB5  0F 85 04 02 00 00               jne 0x140a01fbf
00A01DBB  85 F6                           test esi, esi
00A01DBD  0F 84 7D 03 00 00               je 0x140a02140
00A01DC3  83 FF 03                        cmp edi, 3
00A01DC6  0F 84 74 03 00 00               je 0x140a02140
00A01DCC  83 FF 01                        cmp edi, 1
00A01DCF  0F 84 6B 03 00 00               je 0x140a02140
00A01DD5  46 8A 64 3C 7F                  mov r12b, byte ptr [rsp + r15 + 0x7f]
00A01DDA  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00A01DDE  41 80 FC FE                     cmp r12b, 0xfe
00A01DE2  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00A01DE7  0F 94 44 24 51                  sete byte ptr [rsp + 0x51]
00A01DEC  4D 85 FF                        test r15, r15
00A01DEF  0F 84 86 01 00 00               je 0x140a01f7b
00A01DF5  46 8A 54 3C 7F                  mov r10b, byte ptr [rsp + r15 + 0x7f]
00A01DFA  49 FF CF                        dec r15
00A01DFD  FF CE                           dec esi
00A01DFF  44 88 54 24 50                  mov byte ptr [rsp + 0x50], r10b
00A01E04  41 80 FA FE                     cmp r10b, 0xfe
00A01E08  0F 84 77 01 00 00               je 0x140a01f85
00A01E0E  8D 58 01                        lea ebx, [rax + 1]
00A01E11  3B D8                           cmp ebx, eax
00A01E13  0F 82 DD FE FF FF               jb 0x140a01cf6
00A01E19  41 3B 1E                        cmp ebx, dword ptr [r14]
00A01E1C  0F 87 F4 03 00 00               ja 0x140a02216
00A01E22  8B C8                           mov ecx, eax
00A01E24  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A01E29  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
00A01E2D  48 8B 00                        mov rax, qword ptr [rax]
00A01E30  44 88 14 01                     mov byte ptr [rcx + rax], r10b
00A01E34  8B C3                           mov eax, ebx
00A01E36  33 C9                           xor ecx, ecx
00A01E38  8B D9                           mov ebx, ecx
00A01E3A  EB B0                           jmp 0x140a01dec
00A01E3C  F7 C7 FC FF FF FF               test edi, 0xfffffffc
00A01E42  0F 85 F8 02 00 00               jne 0x140a02140
00A01E48  41 83 FD 03                     cmp r13d, 3
00A01E4C  0F 84 EE 02 00 00               je 0x140a02140
00A01E52  83 FF 02                        cmp edi, 2
00A01E55  0F 84 E5 02 00 00               je 0x140a02140
00A01E5B  45 85 ED                        test r13d, r13d
00A01E5E  0F 84 19 02 00 00               je 0x140a0207d
00A01E64  41 8B FD                        mov edi, r13d
00A01E67  41 83 FD 03                     cmp r13d, 3
00A01E6B  0F 84 04 05 00 00               je 0x140a02375
00A01E71  44 8A C1                        mov r8b, cl
00A01E74  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00A01E79  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00A01E7E  88 4C 24 40                     mov byte ptr [rsp + 0x40], cl
00A01E82  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00A01E87  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A01E8C  41 83 FD 04                     cmp r13d, 4
00A01E90  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A01E95  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A01E9A  0F 94 C2                        sete dl
00A01E9D  49 8B CC                        mov rcx, r12
00A01EA0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A01EA5  E8 16 06 00 00                  call 0x140a024c0
00A01EAA  33 C9                           xor ecx, ecx
00A01EAC  8B D8                           mov ebx, eax
00A01EAE  85 C0                           test eax, eax
00A01EB0  0F 85 45 FE FF FF               jne 0x140a01cfb
00A01EB6  38 4C 24 52                     cmp byte ptr [rsp + 0x52], cl
00A01EBA  0F 85 DB 04 00 00               jne 0x140a0239b
00A01EC0  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00A01EC5  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00A01ECA  49 FF C1                        inc r9
00A01ECD  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A01ED5  49 8B D6                        mov rdx, r14
00A01ED8  49 8B CF                        mov rcx, r15
00A01EDB  E8 D4 07 00 00                  call 0x140a026b4
00A01EE0  8B D8                           mov ebx, eax
00A01EE2  85 C0                           test eax, eax
00A01EE4  0F 85 11 FE FF FF               jne 0x140a01cfb
00A01EEA  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00A01EEF  41 8A 49 01                     mov cl, byte ptr [r9 + 1]
00A01EF3  E8 6C 07 00 00                  call 0x140a02664
00A01EF8  84 C0                           test al, al
00A01EFA  75 2B                           jne 0x140a01f27
00A01EFC  49 83 C1 04                     add r9, 4
00A01F00  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00A01F08  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00A01F0D  49 8B D6                        mov rdx, r14
00A01F10  49 8B CF                        mov rcx, r15
00A01F13  E8 9C 07 00 00                  call 0x140a026b4
00A01F18  8B D8                           mov ebx, eax
00A01F1A  85 C0                           test eax, eax
00A01F1C  0F 85 D9 FD FF FF               jne 0x140a01cfb
00A01F22  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00A01F27  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00A01F2B  85 C0                           test eax, eax
00A01F2D  74 27                           je 0x140a01f56
00A01F2F  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
00A01F33  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00A01F38  49 8B D6                        mov rdx, r14
00A01F3B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A01F3F  49 8B CF                        mov rcx, r15
00A01F42  E8 6D 07 00 00                  call 0x140a026b4
00A01F47  8B D8                           mov ebx, eax
00A01F49  85 C0                           test eax, eax
00A01F4B  0F 85 AA FD FF FF               jne 0x140a01cfb
00A01F51  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00A01F56  49 8B C9                        mov rcx, r9
00A01F59  E8 CE 06 00 00                  call 0x140a0262c
00A01F5E  33 D2                           xor edx, edx
00A01F60  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00A01F65  44 8D 6A 03                     lea r13d, [rdx + 3]
00A01F69  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00A01F6D  4D 8D 24 44                     lea r12, [r12 + rax*2]
00A01F71  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00A01F76  E9 EC FD FF FF                  jmp 0x140a01d67
00A01F7B  41 80 FA FE                     cmp r10b, 0xfe
00A01F7F  0F 85 BB 01 00 00               jne 0x140a02140
00A01F85  85 F6                           test esi, esi
00A01F87  0F 85 4A 02 00 00               jne 0x140a021d7
00A01F8D  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00A01F91  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00A01F96  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A01F9B  4D 8D 24 44                     lea r12, [r12 + rax*2]
00A01F9F  48 63 FE                        movsxd rdi, esi
00A01FA2  48 85 FF                        test rdi, rdi
00A01FA5  0F 85 1F 04 00 00               jne 0x140a023ca
00A01FAB  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00A01FAF  41 89 06                        mov dword ptr [r14], eax
00A01FB2  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A01FB7  4C 89 20                        mov qword ptr [rax], r12
00A01FBA  E9 3C FD FF FF                  jmp 0x140a01cfb
00A01FBF  41 8A CC                        mov cl, r12b
00A01FC2  E8 E5 FB FF FF                  call 0x140a01bac
00A01FC7  48 63 C8                        movsxd rcx, eax
00A01FCA  4C 8D 15 DF 0B 60 FF            lea r10, [rip - 0x9ff421]
00A01FD1  4C 8D 04 49                     lea r8, [rcx + rcx*2]
00A01FD5  33 C9                           xor ecx, ecx
00A01FD7  47 8B 4C C2 0C                  mov r9d, dword ptr [r10 + r8*8 + 0xc]
00A01FDC  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
00A01FE1  83 FF 04                        cmp edi, 4
00A01FE4  0F 85 42 01 00 00               jne 0x140a0212c
00A01FEA  47 8A 5C C2 10                  mov r11b, byte ptr [r10 + r8*8 + 0x10]
00A01FEF  45 84 DB                        test r11b, r11b
00A01FF2  0F 85 A3 02 00 00               jne 0x140a0229b
00A01FF8  47 8A 54 C2 13                  mov r10b, byte ptr [r10 + r8*8 + 0x13]
00A01FFD  45 84 D2                        test r10b, r10b
00A02000  0F 84 67 01 00 00               je 0x140a0216d
00A02006  41 8D 45 FC                     lea eax, [r13 - 4]
00A0200A  83 F8 01                        cmp eax, 1
00A0200D  0F 86 2D 01 00 00               jbe 0x140a02140
00A02013  85 F6                           test esi, esi
00A02015  0F 84 B9 00 00 00               je 0x140a020d4
00A0201B  45 84 D2                        test r10b, r10b
00A0201E  0F 84 B0 00 00 00               je 0x140a020d4
00A02024  44 8D 4E FF                     lea r9d, [rsi - 1]
00A02028  4D 63 C1                        movsxd r8, r9d
00A0202B  4D 85 C0                        test r8, r8
00A0202E  0F 88 9B 00 00 00               js 0x140a020cf
00A02034  42 8A 4C 05 80                  mov cl, byte ptr [rbp + r8 - 0x80]
00A02039  E8 6E FB FF FF                  call 0x140a01bac
00A0203E  83 F8 FF                        cmp eax, -1
00A02041  0F 84 BA 00 00 00               je 0x140a02101
00A02047  49 63 C9                        movsxd rcx, r9d
00A0204A  8A 4C 0D 80                     mov cl, byte ptr [rbp + rcx - 0x80]
00A0204E  E8 59 FB FF FF                  call 0x140a01bac
00A02053  48 63 C8                        movsxd rcx, eax
00A02056  48 8D 3D 53 0B 60 FF            lea rdi, [rip - 0x9ff4ad]
00A0205D  48 8D 04 49                     lea rax, [rcx + rcx*2]
00A02061  33 C9                           xor ecx, ecx
00A02063  38 4C C7 13                     cmp byte ptr [rdi + rax*8 + 0x13], cl
00A02067  0F 85 85 01 00 00               jne 0x140a021f2
00A0206D  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00A02072  EB 67                           jmp 0x140a020db
00A02074  49 83 C4 02                     add r12, 2
00A02078  E9 F4 FE FF FF                  jmp 0x140a01f71
00A0207D  41 BA 05 00 00 00               mov r10d, 5
00A02083  45 8B EA                        mov r13d, r10d
00A02086  85 F6                           test esi, esi
00A02088  0F 84 DA 02 00 00               je 0x140a02368
00A0208E  44 8D 4E FF                     lea r9d, [rsi - 1]
00A02092  4D 63 C1                        movsxd r8, r9d
00A02095  4D 85 C0                        test r8, r8
00A02098  78 21                           js 0x140a020bb
00A0209A  42 8A 4C 05 80                  mov cl, byte ptr [rbp + r8 - 0x80]
00A0209F  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
00A020A3  E8 04 FB FF FF                  call 0x140a01bac
00A020A8  83 F8 FF                        cmp eax, -1
00A020AB  0F 85 78 02 00 00               jne 0x140a02329
00A020B1  41 FF C9                        dec r9d
00A020B4  49 FF C8                        dec r8
00A020B7  33 C9                           xor ecx, ecx
00A020B9  EB DA                           jmp 0x140a02095
00A020BB  45 85 C9                        test r9d, r9d
00A020BE  0F 89 A0 FD FF FF               jns 0x140a01e64
00A020C4  41 BD 04 00 00 00               mov r13d, 4
00A020CA  E9 95 FD FF FF                  jmp 0x140a01e64
00A020CF  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00A020D4  48 8D 3D D5 0A 60 FF            lea rdi, [rip - 0x9ff52b]
00A020DB  45 84 DB                        test r11b, r11b
00A020DE  74 6A                           je 0x140a0214a
00A020E0  44 8B E9                        mov r13d, ecx
00A020E3  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00A020E8  4D 85 FF                        test r15, r15
00A020EB  75 6A                           jne 0x140a02157
00A020ED  BF 03 00 00 00                  mov edi, 3
00A020F2  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A020F7  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00A020FC  E9 68 FE FF FF                  jmp 0x140a01f69
00A02101  41 FF C9                        dec r9d
00A02104  49 FF C8                        dec r8
00A02107  33 C9                           xor ecx, ecx
00A02109  E9 1D FF FF FF                  jmp 0x140a0202b
00A0210E  F7 C7 FC FF FF FF               test edi, 0xfffffffc
00A02114  75 2A                           jne 0x140a02140
00A02116  83 FF 02                        cmp edi, 2
00A02119  74 25                           je 0x140a02140
00A0211B  48 63 C6                        movsxd rax, esi
00A0211E  BF 01 00 00 00                  mov edi, 1
00A02123  FF C6                           inc esi
00A02125  C6 44 05 80 FE                  mov byte ptr [rbp + rax - 0x80], 0xfe
00A0212A  EB CB                           jmp 0x140a020f7
00A0212C  43 38 4C C2 12                  cmp byte ptr [r10 + r8*8 + 0x12], cl
00A02131  0F 84 B3 FE FF FF               je 0x140a01fea
00A02137  83 FF 02                        cmp edi, 2
00A0213A  0F 84 4C 01 00 00               je 0x140a0228c
00A02140  BB 38 05 00 00                  mov ebx, 0x538
00A02145  E9 B1 FB FF FF                  jmp 0x140a01cfb
00A0214A  41 BD 05 00 00 00               mov r13d, 5
00A02150  45 84 D2                        test r10b, r10b
00A02153  75 8E                           jne 0x140a020e3
00A02155  EB 89                           jmp 0x140a020e0
00A02157  42 8A 4C 3C 7F                  mov cl, byte ptr [rsp + r15 + 0x7f]
00A0215C  80 F9 FE                        cmp cl, 0xfe
00A0215F  75 22                           jne 0x140a02183
00A02161  48 63 C6                        movsxd rax, esi
00A02164  FF C6                           inc esi
00A02166  44 88 64 05 80                  mov byte ptr [rbp + rax - 0x80], r12b
00A0216B  EB 80                           jmp 0x140a020ed
00A0216D  F7 C7 FC FF FF FF               test edi, 0xfffffffc
00A02173  0F 85 8D FE FF FF               jne 0x140a02006
00A02179  83 FF 02                        cmp edi, 2
00A0217C  75 C2                           jne 0x140a02140
00A0217E  E9 83 FE FF FF                  jmp 0x140a02006
00A02183  44 8A D1                        mov r10b, cl
00A02186  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
00A0218A  E8 1D FA FF FF                  call 0x140a01bac
00A0218F  48 63 C8                        movsxd rcx, eax
00A02192  48 8D 04 49                     lea rax, [rcx + rcx*2]
00A02196  44 3B 4C C7 0C                  cmp r9d, dword ptr [rdi + rax*8 + 0xc]
00A0219B  7F C4                           jg 0x140a02161
00A0219D  FF CE                           dec esi
00A0219F  41 8D 58 01                     lea ebx, [r8 + 1]
00A021A3  49 FF CF                        dec r15
00A021A6  41 3B D8                        cmp ebx, r8d
00A021A9  0F 82 47 FB FF FF               jb 0x140a01cf6
00A021AF  41 3B 1E                        cmp ebx, dword ptr [r14]
00A021B2  0F 87 18 01 00 00               ja 0x140a022d0
00A021B8  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A021BD  48 8B 00                        mov rax, qword ptr [rax]
00A021C0  41 8B C8                        mov ecx, r8d
00A021C3  44 8B C3                        mov r8d, ebx
00A021C6  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
00A021CA  44 88 14 01                     mov byte ptr [rcx + rax], r10b
00A021CE  33 C9                           xor ecx, ecx
00A021D0  8B D9                           mov ebx, ecx
00A021D2  E9 11 FF FF FF                  jmp 0x140a020e8
00A021D7  48 63 CE                        movsxd rcx, esi
00A021DA  8A 4C 0C 7F                     mov cl, byte ptr [rsp + rcx + 0x7f]
00A021DE  E8 C9 F9 FF FF                  call 0x140a01bac
00A021E3  83 F8 FF                        cmp eax, -1
00A021E6  75 76                           jne 0x140a0225e
00A021E8  BF 02 00 00 00                  mov edi, 2
00A021ED  E9 00 FF FF FF                  jmp 0x140a020f2
00A021F2  80 7C C7 08 A2                  cmp byte ptr [rdi + rax*8 + 8], 0xa2
00A021F7  0F 84 70 FE FF FF               je 0x140a0206d
00A021FD  E9 3E FF FF FF                  jmp 0x140a02140
00A02202  BB 38 05 00 00                  mov ebx, 0x538
00A02207  E9 BC 0D 13 00                  jmp 0x140b32fc8
00A0220C  BB 08 00 00 00                  mov ebx, 8
00A02211  E9 E5 FA FF FF                  jmp 0x140a01cfb
00A02216  8B CB                           mov ecx, ebx
00A02218  E8 6B 3D F2 FF                  call 0x140925f88
00A0221D  48 8B F8                        mov rdi, rax
00A02220  48 85 C0                        test rax, rax
00A02223  74 E7                           je 0x140a0220c
00A02225  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00A0222A  48 8B C8                        mov rcx, rax
00A0222D  45 8B 06                        mov r8d, dword ptr [r14]
00A02230  48 8B 12                        mov rdx, qword ptr [rdx]
00A02233  E8 08 46 CC FF                  call 0x1406c6840
00A02238  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A0223D  48 8B 08                        mov rcx, qword ptr [rax]
00A02240  E8 BF 01 ED FF                  call 0x1408d2404
00A02245  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A0224A  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00A0224F  48 89 38                        mov qword ptr [rax], rdi
00A02252  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00A02256  41 89 1E                        mov dword ptr [r14], ebx
00A02259  E9 C4 FB FF FF                  jmp 0x140a01e22
00A0225E  41 80 FC FE                     cmp r12b, 0xfe
00A02262  74 84                           je 0x140a021e8
00A02264  48 98                           cdqe
00A02266  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A0226A  48 8D 05 3F 09 60 FF            lea rax, [rip - 0x9ff6c1]
00A02271  80 7C C8 13 00                  cmp byte ptr [rax + rcx*8 + 0x13], 0
00A02276  0F 84 6C FF FF FF               je 0x140a021e8
00A0227C  80 7C C8 08 A2                  cmp byte ptr [rax + rcx*8 + 8], 0xa2
00A02281  0F 85 B9 FE FF FF               jne 0x140a02140
00A02287  E9 5C FF FF FF                  jmp 0x140a021e8
00A0228C  38 4C 24 51                     cmp byte ptr [rsp + 0x51], cl
00A02290  0F 84 AA FE FF FF               je 0x140a02140
00A02296  E9 4F FD FF FF                  jmp 0x140a01fea
00A0229B  83 FF 01                        cmp edi, 1
00A0229E  0F 86 54 FD FF FF               jbe 0x140a01ff8
00A022A4  83 FF 03                        cmp edi, 3
00A022A7  0F 85 93 FE FF FF               jne 0x140a02140
00A022AD  42 8A 4C 3C 7F                  mov cl, byte ptr [rsp + r15 + 0x7f]
00A022B2  E8 F5 F8 FF FF                  call 0x140a01bac
00A022B7  48 63 C8                        movsxd rcx, eax
00A022BA  48 8D 04 49                     lea rax, [rcx + rcx*2]
00A022BE  33 C9                           xor ecx, ecx
00A022C0  41 38 4C C2 13                  cmp byte ptr [r10 + rax*8 + 0x13], cl
00A022C5  0F 85 75 FE FF FF               jne 0x140a02140
00A022CB  E9 28 FD FF FF                  jmp 0x140a01ff8
00A022D0  8B CB                           mov ecx, ebx
00A022D2  E8 B1 3C F2 FF                  call 0x140925f88
00A022D7  48 8B F8                        mov rdi, rax
00A022DA  48 85 C0                        test rax, rax
00A022DD  0F 84 29 FF FF FF               je 0x140a0220c
00A022E3  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A022E8  48 8B CF                        mov rcx, rdi
00A022EB  45 8B 06                        mov r8d, dword ptr [r14]
00A022EE  48 8B 10                        mov rdx, qword ptr [rax]
00A022F1  E8 4A 45 CC FF                  call 0x1406c6840
00A022F6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A022FB  48 8B 08                        mov rcx, qword ptr [rax]
00A022FE  E8 01 01 ED FF                  call 0x1408d2404
00A02303  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A02308  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00A0230D  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00A02312  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00A02317  48 89 38                        mov qword ptr [rax], rdi
00A0231A  48 8D 3D 8F 08 60 FF            lea rdi, [rip - 0x9ff771]
00A02321  41 89 1E                        mov dword ptr [r14], ebx
00A02324  E9 94 FE FF FF                  jmp 0x140a021bd
00A02329  48 98                           cdqe
00A0232B  4C 8D 05 7E 08 60 FF            lea r8, [rip - 0x9ff782]
00A02332  48 8D 14 40                     lea rdx, [rax + rax*2]
00A02336  41 8A 4C D0 08                  mov cl, byte ptr [r8 + rdx*8 + 8]
00A0233B  8D 41 77                        lea eax, [rcx + 0x77]
00A0233E  3C 03                           cmp al, 3
00A02340  0F 86 62 0C 13 00               jbe 0x140b32fa8
00A02346  8D 41 70                        lea eax, [rcx + 0x70]
00A02349  3C 03                           cmp al, 3
00A0234B  0F 86 57 0C 13 00               jbe 0x140b32fa8
00A02351  41 80 7C D0 11 00               cmp byte ptr [r8 + rdx*8 + 0x11], 0
00A02357  0F 84 4B 0C 13 00               je 0x140b32fa8
00A0235D  41 BD 04 00 00 00               mov r13d, 4
00A02363  E9 40 0C 13 00                  jmp 0x140b32fa8
00A02368  BF 04 00 00 00                  mov edi, 4
00A0236D  44 8B EF                        mov r13d, edi
00A02370  E9 FC FA FF FF                  jmp 0x140a01e71
00A02375  85 F6                           test esi, esi
00A02377  0F 84 F4 FA FF FF               je 0x140a01e71
00A0237D  48 63 CE                        movsxd rcx, esi
00A02380  8A 4C 0C 7F                     mov cl, byte ptr [rsp + rcx + 0x7f]
00A02384  E8 73 35 DA FF                  call 0x1407a58fc
00A02389  33 C9                           xor ecx, ecx
00A0238B  41 B0 01                        mov r8b, 1
00A0238E  84 C0                           test al, al
00A02390  0F 85 DE FA FF FF               jne 0x140a01e74
00A02396  E9 D6 FA FF FF                  jmp 0x140a01e71
00A0239B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A023A0  88 4C 24 52                     mov byte ptr [rsp + 0x52], cl
00A023A4  8A 48 01                        mov cl, byte ptr [rax + 1]
00A023A7  8D 41 07                        lea eax, [rcx + 7]
00A023AA  A8 FC                           test al, 0xfc
00A023AC  0F 85 0E FB FF FF               jne 0x140a01ec0
00A023B2  80 F9 FA                        cmp cl, 0xfa
00A023B5  0F 85 85 FD FF FF               jne 0x140a02140
00A023BB  E9 00 FB FF FF                  jmp 0x140a01ec0
00A023C0  BB E9 03 00 00                  mov ebx, 0x3e9
00A023C5  E9 31 F9 FF FF                  jmp 0x140a01cfb
00A023CA  8A 44 3C 7F                     mov al, byte ptr [rsp + rdi + 0x7f]
00A023CE  48 FF CF                        dec rdi
00A023D1  88 44 24 51                     mov byte ptr [rsp + 0x51], al
00A023D5  3C FE                           cmp al, 0xfe
00A023D7  0F 84 E1 0B 13 00               je 0x140b32fbe
00A023DD  4C 8D 4C 24 51                  lea r9, [rsp + 0x51]
00A023E2  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A023EA  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00A023EF  49 8B D6                        mov rdx, r14
00A023F2  49 8B CF                        mov rcx, r15
00A023F5  E8 BA 02 00 00                  call 0x140a026b4
00A023FA  8B D8                           mov ebx, eax
00A023FC  85 C0                           test eax, eax
00A023FE  0F 84 9E FB FF FF               je 0x140a01fa2
00A02404  E9 F2 F8 FF FF                  jmp 0x140a01cfb
00A02409  E8 1E 02 00 00                  call 0x140a0262c
00A0240E  E9 F8 F8 FF FF                  jmp 0x140a01d0b
00A02413  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A02418  E9 AB 0B 13 00                  jmp 0x140b32fc8
00A0241D  B8 57 00 00 00                  mov eax, 0x57
00A02422  E9 F8 F8 FF FF                  jmp 0x140a01d1f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalGetConditionForString(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m174;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m186;
    unsigned __int8 v_stack_m187;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (408);
    result = (*(unsigned __int64 *)(v_rip + 4229885)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m168 = a1;
    a1 = 0;
    v_stack_m180 = a3;
    v_stack_m160 = a2;
    v_stack_m188 = 0;
    v_stack_m174 = 0;
    v_stack_m170 = 0;
    v_stack_m187 = 0;
    v_stack_m186 = 0;
    if (0 == 0) goto loc_00A0241D;
    if (a2 == 0) goto loc_00A0241D;
    if (a3 == 0) goto loc_00A0241D;
    if (a4 == 0) goto loc_00A0241D;
    *(unsigned __int64 *)(a3) = 0;
    result = (a2) | (-1);
    *(unsigned int *)(a4) = 0;
loc_00A01CB6:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(a1 + result * 2)) != 0) goto loc_00A01CB6;
    if (((unsigned int)(result)) < 3) goto loc_00A02202;
    if ((*(unsigned __int16 *)(a1)) != 40) goto loc_00A02202;
    result = (unsigned int)((result) + 1);
    a1 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned int)(result)) >= 1) { a1 = (unsigned int)(result); }
    *(unsigned int *)(a4) = (unsigned int)(a1);
    if (((unsigned int)(result)) < 1) goto loc_00A01CF6;
    result = ((unsigned int)((unsigned int)(a1))) + ((unsigned int)((unsigned int)(a1)));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A01D43;
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
loc_00A01CF6:
loc_00A01CFB:
    v_rsi = 0;
    if (v_stack_m170 != 0) goto loc_00A02409;
loc_00A01D0B:
    if ((*(unsigned int *)(a4)) == 4) goto loc_00A02413;
    if (534 != 0) goto loc_00A02413;
loc_00A01D1F:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0xFFFFFFFFULL), a3, a4);
    v_rsp = (v_rsp) + (408);
    return result;
loc_00A01D43:
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = SddlpAlloc((unsigned int)((unsigned int)(result)), (unsigned int)(0xFFFFFFFFULL), a3, a4);
    *(unsigned __int64 *)(a3) = result;
    if (result == 0) goto loc_00A0220C;
    *(unsigned int *)(result) = 0x78747261ULL;
    v_stack_p54 = 4;
loc_00A01D67:
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_00A01F9F;
    result = iswspace(*(unsigned __int16 *)(a1), (unsigned int)(0xFFFFFFFFULL), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00A02074;
    if (0 == 255) goto loc_00A023C0;
    result = GetConditionToken(a1, v_stack_p64, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A01E3C;
    if (((unsigned __int8)(result)) == 254) goto loc_00A0210E;
    if (((unsigned __int8)(result)) != 255) goto loc_00A01FBF;
    if (0 == 0) goto loc_00A02140;
    if (0 == 3) goto loc_00A02140;
    if (0 == 1) goto loc_00A02140;
loc_00A01DEC:
    if ((int)(0) == 0) goto loc_00A01F7B;
    v_r15 = ((int)(0)) - 1;
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_stack_p50 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp + (int)(0) * 1 + 127));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp + (int)(0) * 1 + 127))) == 254) goto loc_00A01F85;
    if (((unsigned int)((unsigned int)(v_stack_p54) + 1)) < ((unsigned int)((unsigned int)(v_stack_p54)))) goto loc_00A01CF6;
    if (((unsigned int)((unsigned int)(v_stack_p54) + 1)) > (*(unsigned int *)(a4))) goto loc_00A02216;
loc_00A01E22:
    v_stack_p54 = (unsigned int)((unsigned int)(v_stack_p54) + 1);
    *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p54))) + *(unsigned __int64 *)(v_stack_p58) * 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp + (int)(0) * 1 + 127));
    a1 = 0;
    goto loc_00A01DEC;
loc_00A01E3C:
    if (((0) & (0xFFFFFFFCULL)) != 0) goto loc_00A02140;
    if (0 == 3) goto loc_00A02140;
    if (0 == 2) goto loc_00A02140;
    if (0 == 0) goto loc_00A0207D;
loc_00A01E64:
    if (0 == 3) goto loc_00A02375;
loc_00A01E71:
loc_00A01E74:
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    a2 = (0 == 4) ? 1 : 0;
    v_stack_p20 = v_stack_p64;
    result = GetOperandValue(v_stack_p70, a2, 0, v_stack_p68);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_00A01CFB;
    if (v_stack_p52 != 0) goto loc_00A0239B;
loc_00A01EC0:
    a4 = (v_stack_p68) + 1;
    v_stack_p20 = 1;
    result = AppendCondition(v_r15, a4, v_stack_p54, a4);
    if ((unsigned int)(result) != 0) goto loc_00A01CFB;
    result = IsValueSizeFixed(*(unsigned __int8 *)(v_stack_p68 + 1), a4, v_stack_p54, v_stack_p68);
    if ((unsigned __int8)(result) != 0) goto loc_00A01F27;
    a4 = (v_stack_p68) + (4);
    v_stack_p20 = 4;
    result = AppendCondition(v_r15, a4, v_stack_p54, a4);
    if ((unsigned int)(result) != 0) goto loc_00A01CFB;
loc_00A01F27:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 4))) == 0) goto loc_00A01F56;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p68 + 4)));
    result = AppendCondition(v_r15, a4, v_stack_p54, *(unsigned __int64 *)(v_stack_p68 + 8));
    if ((unsigned int)(result) != 0) goto loc_00A01CFB;
loc_00A01F56:
    result = FreeOperandValue(v_stack_p68, a4, v_stack_p54, v_stack_p68);
    a2 = 0;
    v_stack_p68 = 0;
loc_00A01F69:
loc_00A01F71:
    v_stack_p70 = v_stack_p70 + (unsigned int)(v_stack_p64) * 2;
    goto loc_00A01D67;
loc_00A01F7B:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp + (int)(0) * 1 + 127))) != 254) goto loc_00A02140;
loc_00A01F85:
    if ((unsigned int)(v_rsi) != 0) goto loc_00A021D7;
loc_00A01F9F:
loc_00A01FA2:
    if ((int)((unsigned int)(v_rsi)) != 0) goto loc_00A023CA;
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(v_stack_p54));
    *(unsigned __int64 *)(v_stack_p78) = v_stack_p70 + (unsigned int)(v_stack_p64) * 2;
    goto loc_00A01CFB;
loc_00A01FBF:
    result = GetOperatorIndexByToken((unsigned __int8)(v_stack_p70 + (unsigned int)(v_stack_p64) * 2), a2, v_stack_p54, v_stack_p68);
    a1 = 0;
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10482721 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 12)));
    if (((unsigned int)((int)((unsigned int)(v_rsi)))) != 4) goto loc_00A0212C;
loc_00A01FEA:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip - 10482721 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 16)) != 0) goto loc_00A0229B;
loc_00A01FF8:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip - 10482721 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 19)) == 0) goto loc_00A0216D;
loc_00A02006:
    if (((unsigned int)(a2 + 3 - 4)) <= 1) goto loc_00A02140;
    if ((unsigned int)(v_rsi) == 0) goto loc_00A020D4;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip - 10482721 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 19)) == 0) goto loc_00A020D4;
loc_00A0202B:
    if (sign_flag) goto loc_00A020CF;
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi - 1)) * 1 - 128), a2, (int)((unsigned int)(v_rsi - 1)), v_rsi - 1);
    if (((unsigned int)(result)) == -1) goto loc_00A02101;
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi - 1)) * 1 - 128), a2, (int)((unsigned int)(v_rsi - 1)), v_rsi - 1);
    a1 = 0;
    if ((*(unsigned __int8 *)(v_rip - 10482861 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 19)) != 0) goto loc_00A021F2;
loc_00A0206D:
    goto loc_00A020DB;
loc_00A02074:
    v_r12 = (v_stack_p70 + (unsigned int)(v_stack_p64) * 2) + (2);
    goto loc_00A01F71;
loc_00A0207D:
    if ((unsigned int)(v_rsi) == 0) goto loc_00A02368;
loc_00A02095:
    if (sign_flag) goto loc_00A020BB;
    v_stack_p50 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi - 1)) * 1 - 128));
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi - 1)) * 1 - 128), a2, (int)((unsigned int)(v_rsi - 1)), v_rsi - 1);
    if (((unsigned int)(result)) != -1) goto loc_00A02329;
    a4 = (unsigned int)((v_rsi - 1) - 1);
    a3 = ((int)((unsigned int)(v_rsi - 1))) - 1;
    a1 = 0;
    goto loc_00A02095;
loc_00A020BB:
    if (!sign_flag) goto loc_00A01E64;
    goto loc_00A01E64;
loc_00A020CF:
loc_00A020D4:
loc_00A020DB:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip - 10482721 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 16)) == 0) goto loc_00A0214A;
loc_00A020E0:
loc_00A020E3:
loc_00A020E8:
    if (v_stack_p58 != 0) goto loc_00A02157;
loc_00A020ED:
loc_00A020F2:
loc_00A020F7:
    goto loc_00A01F69;
loc_00A02101:
    a4 = (unsigned int)(((unsigned int)(v_stack_p60)) - 1);
    a3 = ((unsigned int)(v_stack_p54)) - 1;
    a1 = 0;
    goto loc_00A0202B;
loc_00A0210E:
    if (((3) & (0xFFFFFFFCULL)) != 0) goto loc_00A02140;
    if (3 == 2) goto loc_00A02140;
    v_rsi = (unsigned int)((v_rsi) + 1);
    *(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi)) * 1 - 128) = 254;
    goto loc_00A020F7;
loc_00A0212C:
    if ((*(unsigned __int8 *)(5 + a3 * 8 + 18)) == 0) goto loc_00A01FEA;
    if (1 == 2) goto loc_00A0228C;
loc_00A02140:
    goto loc_00A01CFB;
loc_00A0214A:
    if (5 != 0) goto loc_00A020E3;
    goto loc_00A020E0;
loc_00A02157:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp + v_stack_p58 * 1 + 127))) != 254) goto loc_00A02183;
loc_00A02161:
    v_rsi = (unsigned int)((v_rsi) + 1);
    *(unsigned __int8 *)(v_stack_mD8 + (int)((unsigned int)(v_rsi)) * 1 - 128) = (unsigned __int8)(v_stack_p70);
    goto loc_00A020ED;
loc_00A0216D:
    if (((1) & (0xFFFFFFFCULL)) != 0) goto loc_00A02006;
    if (1 != 2) goto loc_00A02140;
    goto loc_00A02006;
loc_00A02183:
    v_stack_p50 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp + v_stack_p58 * 1 + 127));
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_rsp + v_stack_p58 * 1 + 127), a2, a3, a4);
    if (((unsigned int)(a4)) > (*(unsigned int *)(1 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 12))) goto loc_00A02161;
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_r15 = (v_stack_p58) - 1;
    if (((unsigned int)(a3 + 1)) < ((unsigned int)(a3))) goto loc_00A01CF6;
    if (((unsigned int)(a3 + 1)) > (*(unsigned int *)(a4))) goto loc_00A022D0;
loc_00A021BD:
    v_stack_p54 = (unsigned int)(a3 + 1);
    *(unsigned __int8 *)((unsigned int)((unsigned int)(a3)) + *(unsigned __int64 *)(v_stack_p58) * 1) = (unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(v_rsp + v_stack_p58 * 1 + 127)));
    a1 = 0;
    goto loc_00A020E8;
loc_00A021D7:
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_rsp + (int)((unsigned int)(v_rsi)) * 1 + 127), a2, (unsigned int)((unsigned int)(a3 + 1)), a4);
    if (((unsigned int)(result)) != -1) goto loc_00A0225E;
loc_00A021E8:
    goto loc_00A020F2;
loc_00A021F2:
    if ((*(unsigned __int8 *)(2 + result * 8 + 8)) == 162) goto loc_00A0206D;
    goto loc_00A02140;
loc_00A02202:
loc_00A0220C:
    goto loc_00A01CFB;
loc_00A02216:
    result = SddlpAlloc(8, a2, (unsigned int)((unsigned int)(a3 + 1)), a4);
    if (result == 0) goto loc_00A0220C;
    result = memcpy(result, *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_stack_p58), *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    *(unsigned __int64 *)(v_stack_p58) = result;
    *(unsigned int *)(a4) = 8;
    goto loc_00A01E22;
loc_00A0225E:
    if (((unsigned __int8)(v_stack_p70)) == 254) goto loc_00A021E8;
    if ((*(unsigned __int8 *)(v_rip - 10483393 + (unsigned int)(v_stack_p54) + (unsigned int)(v_stack_p54) * 2 * 8 + 19)) == 0) goto loc_00A021E8;
    if ((*(unsigned __int8 *)(v_rip - 10483393 + (unsigned int)(v_stack_p54) + (unsigned int)(v_stack_p54) * 2 * 8 + 8)) != 162) goto loc_00A02140;
    goto loc_00A021E8;
loc_00A0228C:
    if (v_stack_p51 == ((unsigned __int8)((unsigned int)(v_stack_p54) + (unsigned int)(v_stack_p54) * 2))) goto loc_00A02140;
    goto loc_00A01FEA;
loc_00A0229B:
    if (((unsigned int)(result)) <= 1) goto loc_00A01FF8;
    if (((unsigned int)(result)) != 3) goto loc_00A02140;
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_rsp + v_r15 * 1 + 127), *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    a1 = 0;
    if ((*(unsigned __int8 *)(v_stack_p50 + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 19)) != 0) goto loc_00A02140;
    goto loc_00A01FF8;
loc_00A022D0:
    result = SddlpAlloc(8, *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    if (result == 0) goto loc_00A0220C;
    result = memcpy(result, *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_stack_p58), *(unsigned __int64 *)(v_stack_p58), (unsigned int)(*(unsigned int *)(a4)), a4);
    *(unsigned __int64 *)(v_stack_p58) = result;
    *(unsigned int *)(a4) = 8;
    goto loc_00A021BD;
loc_00A02329:
loc_00A02368:
    goto loc_00A01E71;
loc_00A02375:
    if ((unsigned int)(v_rsi) == 0) goto loc_00A01E71;
    result = IsArrayType(*(unsigned __int8 *)(v_rsp + (int)((unsigned int)(v_rsi)) * 1 + 127), v_stack_p58 + v_stack_p58 * 2, v_rip - 10483586, (unsigned int)(v_stack_p60));
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A01E74;
    goto loc_00A01E71;
loc_00A0239B:
    v_stack_p52 = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p68 + 1) + 7)) & (252)) != 0) goto loc_00A01EC0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p68 + 1))) != 250) goto loc_00A02140;
    goto loc_00A01EC0;
loc_00A023C0:
    goto loc_00A01CFB;
loc_00A023CA:
    v_rdi = (4) - 1;
    v_stack_p51 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp + 4 * 1 + 127));
    v_stack_p20 = 1;
    result = AppendCondition(v_r15, a4, v_stack_p54, v_stack_p51);
    if ((unsigned int)(result) == 0) goto loc_00A01FA2;
    goto loc_00A01CFB;
loc_00A02409:
    result = FreeOperandValue(v_r15, a4, v_stack_p54, v_stack_p51);
    goto loc_00A01D0B;
loc_00A02413:
loc_00A0241D:
    goto loc_00A01D1F;
}
```

## 5. (Beta) C Style

```c
int64_t LocalGetConditionForString(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m174;
    uint64_t v_stack_m180;
    uint8_t v_stack_m186;
    uint8_t v_stack_m187;
    uint8_t v_stack_m188;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (408);
    result = (*(uint64_t *)(v_rip + 0x408AFD)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m168 = Arg1;
    Arg1 = 0;
    v_stack_m180 = Arg3;
    v_stack_m160 = Arg2;
    v_stack_m188 = 0;
    v_stack_m174 = 0;
    v_stack_m170 = 0;
    v_stack_m187 = 0;
    v_stack_m186 = 0;
    if (0 == 0) goto loc_00A0241D;
    if (Arg2 == 0) goto loc_00A0241D;
    if (Arg3 == NULL) goto loc_00A0241D;
    if (Arg4 == NULL) goto loc_00A0241D;
    *(uint64_t *)(arg3) = 0;
    result = (Arg2) | (-1);
    *(uint32_t *)(arg4) = 0;
loc_00A01CB6:
    result = (result) + 1;
    if ((*(uint16_t *)(Arg1 + result * 2)) != 0) goto loc_00A01CB6;
    if (((uint32_t)(result)) < 3) goto loc_00A02202;
    if ((*(uint16_t *)(Arg1)) != 40) goto loc_00A02202;
    result = (uint32_t)((result) + 1);
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint32_t)(result)) >= 1) { Arg1 = (uint32_t)(result); }
    *(uint32_t *)(arg4) = (uint32_t)(Arg1);
    if (((uint32_t)(result)) < 1) goto loc_00A01CF6;
    result = ((uint32_t)((uint32_t)(Arg1))) + ((uint32_t)((uint32_t)(Arg1)));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A01D43;
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
loc_00A01CF6:
loc_00A01CFB:
    local_rsi = 0;
    if (v_stack_m170 != 0) goto loc_00A02409;
loc_00A01D0B:
    if ((*(uint32_t *)(arg4)) == 4) goto loc_00A02413;
    if (534 != 0) goto loc_00A02413;
loc_00A01D1F:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0xFFFFFFFFULL), Arg3, Arg4);
    local_rsp = (local_rsp) + (408);
    return result;
loc_00A01D43:
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = SddlpAlloc((uint32_t)((uint32_t)(result)), (uint32_t)(0xFFFFFFFFULL), Arg3, Arg4);
    *(uint64_t *)(arg3) = result;
    if (result == 0) goto loc_00A0220C;
    *(uint32_t *)(result) = 0x78747261ULL;
    v_stack_p54 = 4;
loc_00A01D67:
    if ((uint16_t)(*(uint16_t *)(Arg1)) == 0) goto loc_00A01F9F;
    result = iswspace(*(uint16_t *)(Arg1), (uint32_t)(0xFFFFFFFFULL), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A02074;
    if (0 == 255) goto loc_00A023C0;
    result = GetConditionToken(Arg1, v_stack_p64, Arg3, Arg4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A01E3C;
    if (((uint8_t)(result)) == 254) goto loc_00A0210E;
    if (((uint8_t)(result)) != 255) goto loc_00A01FBF;
    if (0 == 0) goto loc_00A02140;
    if (0 == 3) goto loc_00A02140;
    if (0 == 1) goto loc_00A02140;
loc_00A01DEC:
    if ((int32_t)(0) == 0) goto loc_00A01F7B;
    local_r15 = ((int32_t)(0)) - 1;
    local_rsi = (uint32_t)((local_rsi) - 1);
    v_stack_p50 = (uint8_t)(*(uint8_t *)(local_rsp + (int32_t)(0) * 1 + 0x7F));
    if (((uint8_t)(*(uint8_t *)(local_rsp + (int32_t)(0) * 1 + 0x7F))) == 254) goto loc_00A01F85;
    if (((uint32_t)((uint32_t)(v_stack_p54) + 1)) < ((uint32_t)((uint32_t)(v_stack_p54)))) goto loc_00A01CF6;
    if (((uint32_t)((uint32_t)(v_stack_p54) + 1)) > (*(uint32_t *)(arg4))) goto loc_00A02216;
loc_00A01E22:
    v_stack_p54 = (uint32_t)((uint32_t)(v_stack_p54) + 1);
    *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p54))) + *(uint64_t *)(v_stack_p58) * 1) = (uint8_t)(*(uint8_t *)(local_rsp + (int32_t)(0) * 1 + 0x7F));
    Arg1 = 0;
    goto loc_00A01DEC;
loc_00A01E3C:
    if (((0) & (0xFFFFFFFCULL)) != 0) goto loc_00A02140;
    if (0 == 3) goto loc_00A02140;
    if (0 == 2) goto loc_00A02140;
    if (0 == 0) goto loc_00A0207D;
loc_00A01E64:
    if (0 == 3) goto loc_00A02375;
loc_00A01E71:
loc_00A01E74:
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    Arg2 = (0 == 4) ? 1 : 0;
    v_stack_p20 = v_stack_p64;
    result = GetOperandValue(v_stack_p70, Arg2, 0, v_stack_p68);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_00A01CFB;
    if (v_stack_p52 != 0) goto loc_00A0239B;
loc_00A01EC0:
    Arg4 = (v_stack_p68) + 1;
    v_stack_p20 = 1;
    result = AppendCondition(local_r15, Arg4, v_stack_p54, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A01CFB;
    result = IsValueSizeFixed(*(uint8_t *)(v_stack_p68 + 0x1), Arg4, v_stack_p54, v_stack_p68);
    if ((uint8_t)(result) != 0) goto loc_00A01F27;
    Arg4 = (v_stack_p68) + (4);
    v_stack_p20 = 4;
    result = AppendCondition(local_r15, Arg4, v_stack_p54, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A01CFB;
loc_00A01F27:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x4))) == 0) goto loc_00A01F56;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x4)));
    result = AppendCondition(local_r15, Arg4, v_stack_p54, *(uint64_t *)(v_stack_p68 + 0x8));
    if ((uint32_t)(result) != 0) goto loc_00A01CFB;
loc_00A01F56:
    result = FreeOperandValue(v_stack_p68, Arg4, v_stack_p54, v_stack_p68);
    Arg2 = 0;
    v_stack_p68 = 0;
loc_00A01F69:
loc_00A01F71:
    v_stack_p70 = v_stack_p70 + (uint32_t)(v_stack_p64) * 2;
    goto loc_00A01D67;
loc_00A01F7B:
    if (((uint8_t)(*(uint8_t *)(local_rsp + (int32_t)(0) * 1 + 0x7F))) != 254) goto loc_00A02140;
loc_00A01F85:
    if ((uint32_t)(local_rsi) != 0) goto loc_00A021D7;
loc_00A01F9F:
loc_00A01FA2:
    if ((int32_t)((uint32_t)(local_rsi)) != 0) goto loc_00A023CA;
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(v_stack_p54));
    *(uint64_t *)(v_stack_p78) = v_stack_p70 + (uint32_t)(v_stack_p64) * 2;
    goto loc_00A01CFB;
loc_00A01FBF:
    result = GetOperatorIndexByToken((uint8_t)(v_stack_p70 + (uint32_t)(v_stack_p64) * 2), Arg2, v_stack_p54, v_stack_p68);
    Arg1 = 0;
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9FF421 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0xC)));
    if (((uint32_t)((int32_t)((uint32_t)(local_rsi)))) != 4) goto loc_00A0212C;
loc_00A01FEA:
    if ((uint8_t)(*(uint8_t *)(v_rip - 0x9FF421 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) != 0) goto loc_00A0229B;
loc_00A01FF8:
    if ((uint8_t)(*(uint8_t *)(v_rip - 0x9FF421 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x13)) == 0) goto loc_00A0216D;
loc_00A02006:
    if (((uint32_t)(Arg2 + 3 - 4)) <= 1) goto loc_00A02140;
    if ((uint32_t)(local_rsi) == 0) goto loc_00A020D4;
    if ((uint8_t)(*(uint8_t *)(v_rip - 0x9FF421 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x13)) == 0) goto loc_00A020D4;
loc_00A0202B:
    if (sign_flag) goto loc_00A020CF;
    result = GetOperatorIndexByToken(*(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi - 0x1)) * 1 - 0x80), Arg2, (int32_t)((uint32_t)(local_rsi - 1)), local_rsi - 1);
    if (((uint32_t)(result)) == -1) goto loc_00A02101;
    result = GetOperatorIndexByToken(*(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi - 0x1)) * 1 - 0x80), Arg2, (int32_t)((uint32_t)(local_rsi - 1)), local_rsi - 1);
    Arg1 = 0;
    if ((*(uint8_t *)(v_rip - 0x9FF4AD + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x13)) != 0) goto loc_00A021F2;
loc_00A0206D:
    goto loc_00A020DB;
loc_00A02074:
    local_r12 = (v_stack_p70 + (uint32_t)(v_stack_p64) * 2) + (2);
    goto loc_00A01F71;
loc_00A0207D:
    if ((uint32_t)(local_rsi) == 0) goto loc_00A02368;
loc_00A02095:
    if (sign_flag) goto loc_00A020BB;
    v_stack_p50 = (uint8_t)(*(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi - 0x1)) * 1 - 0x80));
    result = GetOperatorIndexByToken(*(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi - 0x1)) * 1 - 0x80), Arg2, (int32_t)((uint32_t)(local_rsi - 1)), local_rsi - 1);
    if (((uint32_t)(result)) != -1) goto loc_00A02329;
    Arg4 = (uint32_t)((local_rsi - 1) - 1);
    Arg3 = ((int32_t)((uint32_t)(local_rsi - 1))) - 1;
    Arg1 = 0;
    goto loc_00A02095;
loc_00A020BB:
    if (!sign_flag) goto loc_00A01E64;
    goto loc_00A01E64;
loc_00A020CF:
loc_00A020D4:
loc_00A020DB:
    if ((uint8_t)(*(uint8_t *)(v_rip - 0x9FF421 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x10)) == 0) goto loc_00A0214A;
loc_00A020E0:
loc_00A020E3:
loc_00A020E8:
    if (v_stack_p58 != 0) goto loc_00A02157;
loc_00A020ED:
loc_00A020F2:
loc_00A020F7:
    goto loc_00A01F69;
loc_00A02101:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p60)) - 1);
    Arg3 = ((uint32_t)(v_stack_p54)) - 1;
    Arg1 = 0;
    goto loc_00A0202B;
loc_00A0210E:
    if (((3) & (0xFFFFFFFCULL)) != 0) goto loc_00A02140;
    if (3 == 2) goto loc_00A02140;
    local_rsi = (uint32_t)((local_rsi) + 1);
    *(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi)) * 1 - 0x80) = 254;
    goto loc_00A020F7;
loc_00A0212C:
    if ((*(uint8_t *)(5 + arg3 * 8 + 0x12)) == 0) goto loc_00A01FEA;
    if (1 == 2) goto loc_00A0228C;
loc_00A02140:
    goto loc_00A01CFB;
loc_00A0214A:
    if (5 != 0) goto loc_00A020E3;
    goto loc_00A020E0;
loc_00A02157:
    if (((uint8_t)(*(uint8_t *)(local_rsp + v_stack_p58 * 1 + 0x7F))) != 254) goto loc_00A02183;
loc_00A02161:
    local_rsi = (uint32_t)((local_rsi) + 1);
    *(uint8_t *)(v_stack_mD8 + (int32_t)((uint32_t)(local_rsi)) * 1 - 0x80) = (uint8_t)(v_stack_p70);
    goto loc_00A020ED;
loc_00A0216D:
    if (((1) & (0xFFFFFFFCULL)) != 0) goto loc_00A02006;
    if (1 != 2) goto loc_00A02140;
    goto loc_00A02006;
loc_00A02183:
    v_stack_p50 = (uint8_t)(*(uint8_t *)(local_rsp + v_stack_p58 * 1 + 0x7F));
    result = GetOperatorIndexByToken(*(uint8_t *)(local_rsp + v_stack_p58 * 1 + 0x7F), Arg2, Arg3, Arg4);
    if (((uint32_t)(Arg4)) > (*(uint32_t *)(1 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0xC))) goto loc_00A02161;
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_r15 = (v_stack_p58) - 1;
    if (((uint32_t)(Arg3 + 1)) < ((uint32_t)(Arg3))) goto loc_00A01CF6;
    if (((uint32_t)(Arg3 + 1)) > (*(uint32_t *)(arg4))) goto loc_00A022D0;
loc_00A021BD:
    v_stack_p54 = (uint32_t)(Arg3 + 1);
    *(uint8_t *)((uint32_t)((uint32_t)(arg3)) + *(uint64_t *)(v_stack_p58) * 1) = (uint8_t)((uint8_t)(*(uint8_t *)(local_rsp + v_stack_p58 * 1 + 0x7F)));
    Arg1 = 0;
    goto loc_00A020E8;
loc_00A021D7:
    result = GetOperatorIndexByToken(*(uint8_t *)(local_rsp + (int32_t)((uint32_t)(local_rsi)) * 1 + 0x7F), Arg2, (uint32_t)((uint32_t)(Arg3 + 1)), Arg4);
    if (((uint32_t)(result)) != -1) goto loc_00A0225E;
loc_00A021E8:
    goto loc_00A020F2;
loc_00A021F2:
    if ((*(uint8_t *)(2 + result * 8 + 0x8)) == 162) goto loc_00A0206D;
    goto loc_00A02140;
loc_00A02202:
loc_00A0220C:
    goto loc_00A01CFB;
loc_00A02216:
    result = SddlpAlloc(8, Arg2, (uint32_t)((uint32_t)(Arg3 + 1)), Arg4);
    if (result == 0) goto loc_00A0220C;
    result = memcpy(result, *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    result = PdcCloseEvent(*(uint64_t *)(v_stack_p58), *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    *(uint64_t *)(v_stack_p58) = result;
    *(uint32_t *)(arg4) = 8;
    goto loc_00A01E22;
loc_00A0225E:
    if (((uint8_t)(v_stack_p70)) == 254) goto loc_00A021E8;
    if ((*(uint8_t *)(v_rip - 0x9FF6C1 + (uint32_t)(v_stack_p54) + (uint32_t)(v_stack_p54) * 2 * 8 + 0x13)) == 0) goto loc_00A021E8;
    if ((*(uint8_t *)(v_rip - 0x9FF6C1 + (uint32_t)(v_stack_p54) + (uint32_t)(v_stack_p54) * 2 * 8 + 0x8)) != 162) goto loc_00A02140;
    goto loc_00A021E8;
loc_00A0228C:
    if (v_stack_p51 == ((uint8_t)((uint32_t)(v_stack_p54) + (uint32_t)(v_stack_p54) * 2))) goto loc_00A02140;
    goto loc_00A01FEA;
loc_00A0229B:
    if (((uint32_t)(result)) <= 1) goto loc_00A01FF8;
    if (((uint32_t)(result)) != 3) goto loc_00A02140;
    result = GetOperatorIndexByToken(*(uint8_t *)(local_rsp + local_r15 * 1 + 0x7F), *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    Arg1 = 0;
    if ((*(uint8_t *)(v_stack_p50 + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x13)) != 0) goto loc_00A02140;
    goto loc_00A01FF8;
loc_00A022D0:
    result = SddlpAlloc(8, *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    if (result == 0) goto loc_00A0220C;
    result = memcpy(result, *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    result = PdcCloseEvent(*(uint64_t *)(v_stack_p58), *(uint64_t *)(v_stack_p58), (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    *(uint64_t *)(v_stack_p58) = result;
    *(uint32_t *)(arg4) = 8;
    goto loc_00A021BD;
loc_00A02329:
loc_00A02368:
    goto loc_00A01E71;
loc_00A02375:
    if ((uint32_t)(local_rsi) == 0) goto loc_00A01E71;
    result = IsArrayType(*(uint8_t *)(local_rsp + (int32_t)((uint32_t)(local_rsi)) * 1 + 0x7F), v_stack_p58 + v_stack_p58 * 2, v_rip - 10483586, (uint32_t)(v_stack_p60));
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_00A01E74;
    goto loc_00A01E71;
loc_00A0239B:
    v_stack_p52 = 0;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p68 + 0x1) + 7)) & (252)) != 0) goto loc_00A01EC0;
    if (((uint8_t)(*(uint8_t *)(v_stack_p68 + 0x1))) != 250) goto loc_00A02140;
    goto loc_00A01EC0;
loc_00A023C0:
    goto loc_00A01CFB;
loc_00A023CA:
    local_rdi = (4) - 1;
    v_stack_p51 = (uint8_t)(*(uint8_t *)(local_rsp + 0x4 * 1 + 0x7F));
    v_stack_p20 = 1;
    result = AppendCondition(local_r15, Arg4, v_stack_p54, v_stack_p51);
    if ((uint32_t)(result) == 0) goto loc_00A01FA2;
    goto loc_00A01CFB;
loc_00A02409:
    result = FreeOperandValue(local_r15, Arg4, v_stack_p54, v_stack_p51);
    goto loc_00A01D0B;
loc_00A02413:
loc_00A0241D:
    goto loc_00A01D1F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A01C20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
