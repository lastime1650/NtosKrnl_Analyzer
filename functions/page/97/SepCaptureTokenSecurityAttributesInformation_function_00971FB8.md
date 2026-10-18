# SepCaptureTokenSecurityAttributesInformation

- RVA: `0x00971FB8`–`0x00972583` (길이 `1,483` bytes)
- VA: `0x0000000140971FB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000960F4`
- 디코드: `362`개 명령, `1,483/1,483` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00972016` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009720FE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0097214F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00972196` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009721F1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009722C0` → [SepCaptureInt64Array](SepCaptureInt64Array_function_00972B84.md) (function, `0x00972B84`)
- `0x009722FD` → [SepCaptureUnicodeStringArray](SepCaptureUnicodeStringArray_function_00972F70.md) (function, `0x00972F70`)
- `0x0097232E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00972356` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00972367` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00972376` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009723B9` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009723FA` → [SepCaptureOctetStringArray](../79/SepCaptureOctetStringArray_function_0079FF6C.md) (function, `0x0079FF6C`)
- `0x00972411` → [SepCaptureFqbnArray](../79/SepCaptureFqbnArray_function_0079FD38.md) (function, `0x0079FD38`)
- `0x009724FE` → [RtlCompareUnicodeStrings](RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)

### Direct callers
- [SepCaptureTokenSecurityAttributesAndOperationsInformation](SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) at `0x00971F1B`
- [NtCreateTokenEx](../9C/NtCreateTokenEx_function_009C7C80.md) at `0x009C82FD`
- [NtCreateTokenEx](../9C/NtCreateTokenEx_function_009C7C80.md) at `0x009C833D`

### Static image references
- `0x00972456` → RVA `0x00B4CA80` (`SepValidAttributesTypes`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00972016` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009720FE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0097214F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00972196` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009721F1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00972356` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00972367` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00972565` → [sub_00B29176 + 0x45](../B2/Unknown_function_00B29176.md) (`tail-transfer`)
  - `0x0097256F` → [sub_00B29176 + 0x19](../B2/Unknown_function_00B29176.md) (`tail-transfer`)
  - `0x0097257E` → [sub_00B29176](../B2/Unknown_function_00B29176.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00971FB8  48 8B C4                        mov rax, rsp
00971FBB  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
00971FBF  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00971FC3  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00971FC7  53                              push rbx
00971FC8  56                              push rsi
00971FC9  57                              push rdi
00971FCA  41 54                           push r12
00971FCC  41 55                           push r13
00971FCE  41 56                           push r14
00971FD0  41 57                           push r15
00971FD2  48 81 EC 80 00 00 00            sub rsp, 0x80
00971FD9  4C 8B F9                        mov r15, rcx
00971FDC  33 DB                           xor ebx, ebx
00971FDE  8B F3                           mov esi, ebx
00971FE0  48 89 58 A8                     mov qword ptr [rax - 0x58], rbx
00971FE4  89 58 90                        mov dword ptr [rax - 0x70], ebx
00971FE7  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
00971FEB  8B FB                           mov edi, ebx
00971FED  44 8B E3                        mov r12d, ebx
00971FF0  48 89 58 98                     mov qword ptr [rax - 0x68], rbx
00971FF4  44 8B EB                        mov r13d, ebx
00971FF7  44 89 68 84                     mov dword ptr [rax - 0x7c], r13d
00971FFB  48 89 58 88                     mov qword ptr [rax - 0x78], rbx
00971FFF  45 84 C9                        test r9b, r9b
00972002  0F 84 46 05 00 00               je 0x14097254e
00972008  8D 53 10                        lea edx, [rbx + 0x10]
0097200B  B9 00 01 00 00                  mov ecx, 0x100
00972010  41 B8 53 65 41 74               mov r8d, 0x74416553
00972016  E8 D5 00 21 00                  call 0x140b820f0
0097201B  4C 8B F0                        mov r14, rax
0097201E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00972023  48 85 C0                        test rax, rax
00972026  0F 84 2C 05 00 00               je 0x140972558
0097202C  0F 57 C0                        xorps xmm0, xmm0
0097202F  0F 11 00                        movups xmmword ptr [rax], xmm0
00972032  80 BC 24 D8 00 00 00 01         cmp byte ptr [rsp + 0xd8], 1
0097203A  0F 85 58 04 00 00               jne 0x140972498
00972040  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00972048  48 85 C0                        test rax, rax
0097204B  0F 84 D3 02 00 00               je 0x140972324
00972051  83 BC 24 D0 00 00 00 01         cmp dword ptr [rsp + 0xd0], 1
00972059  0F 82 C5 02 00 00               jb 0x140972324
0097205F  83 38 01                        cmp dword ptr [rax], 1
00972062  0F 84 BC 02 00 00               je 0x140972324
00972068  41 F6 C7 03                     test r15b, 3
0097206C  0F 85 BC 02 00 00               jne 0x14097232e
00972072  49 8D 47 10                     lea rax, [r15 + 0x10]
00972076  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00972080  48 3B C1                        cmp rax, rcx
00972083  0F 87 AA 02 00 00               ja 0x140972333
00972089  49 3B C7                        cmp rax, r15
0097208C  0F 82 A1 02 00 00               jb 0x140972333
00972092  41 0F B7 07                     movzx eax, word ptr [r15]
00972096  66 41 89 06                     mov word ptr [r14], ax
0097209A  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
0097209F  66 41 89 46 02                  mov word ptr [r14 + 2], ax
009720A4  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
009720A8  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
009720AC  85 C9                           test ecx, ecx
009720AE  0F 84 8B 02 00 00               je 0x14097233f
009720B4  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
009720B8  49 89 46 08                     mov qword ptr [r14 + 8], rax
009720BC  48 8D 0C 89                     lea rcx, [rcx + rcx*4]
009720C0  48 C1 E1 03                     shl rcx, 3
009720C4  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009720C9  B8 FF FF FF FF                  mov eax, 0xffffffff
009720CE  44 8B E0                        mov r12d, eax
009720D1  48 3B C8                        cmp rcx, rax
009720D4  44 0F 46 E1                     cmovbe r12d, ecx
009720D8  48 3B C1                        cmp rax, rcx
009720DB  1B FF                           sbb edi, edi
009720DD  81 E7 95 00 00 C0               and edi, 0xc0000095
009720E3  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
009720E7  0F 8C 64 02 00 00               jl 0x140972351
009720ED  45 8B FC                        mov r15d, r12d
009720F0  41 B8 53 65 41 74               mov r8d, 0x74416553
009720F6  41 8B D4                        mov edx, r12d
009720F9  B9 00 01 00 00                  mov ecx, 0x100
009720FE  E8 ED FF 20 00                  call 0x140b820f0
00972103  48 8B F0                        mov rsi, rax
00972106  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0097210B  48 85 C0                        test rax, rax
0097210E  0F 84 4E 02 00 00               je 0x140972362
00972114  45 85 E4                        test r12d, r12d
00972117  74 2C                           je 0x140972145
00972119  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0097211D  A8 03                           test al, 3
0097211F  0F 85 51 02 00 00               jne 0x140972376
00972125  4A 8D 0C 20                     lea rcx, [rax + r12]
00972129  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00972133  48 3B CA                        cmp rcx, rdx
00972136  0F 87 3F 02 00 00               ja 0x14097237b
0097213C  48 3B C8                        cmp rcx, rax
0097213F  0F 82 36 02 00 00               jb 0x14097237b
00972145  4D 8B C7                        mov r8, r15
00972148  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0097214C  48 8B CE                        mov rcx, rsi
0097214F  E8 EC 46 D5 FF                  call 0x1406c6840
00972154  44 8B FB                        mov r15d, ebx
00972157  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
0097215B  4C 8B E3                        mov r12, rbx
0097215E  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00972163  45 3B 7E 04                     cmp r15d, dword ptr [r14 + 4]
00972167  0F 83 A8 00 00 00               jae 0x140972215
0097216D  41 8B C7                        mov eax, r15d
00972170  48 8D 0C 80                     lea rcx, [rax + rax*4]
00972174  48 8D 04 CE                     lea rax, [rsi + rcx*8]
00972178  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097217D  0F B7 08                        movzx ecx, word ptr [rax]
00972180  66 85 C9                        test cx, cx
00972183  0F 84 07 02 00 00               je 0x140972390
00972189  8B D1                           mov edx, ecx
0097218B  B9 00 01 00 00                  mov ecx, 0x100
00972190  41 B8 53 65 41 74               mov r8d, 0x74416553
00972196  E8 55 FF 20 00                  call 0x140b820f0
0097219B  4C 8B E0                        mov r12, rax
0097219E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009721A3  48 85 C0                        test rax, rax
009721A6  0F 84 FC 01 00 00               je 0x1409723a8
009721AC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009721B1  0F B7 01                        movzx eax, word ptr [rcx]
009721B4  66 85 C0                        test ax, ax
009721B7  74 2D                           je 0x1409721e6
009721B9  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
009721BD  F6 C2 01                        test dl, 1
009721C0  0F 85 F3 01 00 00               jne 0x1409723b9
009721C6  4C 8D 04 02                     lea r8, [rdx + rax]
009721CA  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009721D4  4C 3B C0                        cmp r8, rax
009721D7  0F 87 E1 01 00 00               ja 0x1409723be
009721DD  4C 3B C2                        cmp r8, rdx
009721E0  0F 82 D8 01 00 00               jb 0x1409723be
009721E6  44 0F B7 01                     movzx r8d, word ptr [rcx]
009721EA  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
009721EE  49 8B CC                        mov rcx, r12
009721F1  E8 4A 46 D5 FF                  call 0x1406c6840
009721F6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009721FB  4C 89 60 08                     mov qword ptr [rax + 8], r12
009721FF  FF 44 24 48                     inc dword ptr [rsp + 0x48]
00972203  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00972208  41 FF C7                        inc r15d
0097220B  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00972210  E9 46 FF FF FF                  jmp 0x14097215b
00972215  8B D3                           mov edx, ebx
00972217  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
0097221B  41 3B 56 04                     cmp edx, dword ptr [r14 + 4]
0097221F  73 32                           jae 0x140972253
00972221  8B C2                           mov eax, edx
00972223  4C 8D 3C 80                     lea r15, [rax + rax*4]
00972227  46 8B 54 FE 18                  mov r10d, dword ptr [rsi + r15*8 + 0x18]
0097222C  45 85 D2                        test r10d, r10d
0097222F  75 56                           jne 0x140972287
00972231  38 9C 24 E0 00 00 00            cmp byte ptr [rsp + 0xe0], bl
00972238  0F 84 9F 01 00 00               je 0x1409723dd
0097223E  4A 89 5C FE 20                  mov qword ptr [rsi + r15*8 + 0x20], rbx
00972243  41 FF C5                        inc r13d
00972246  44 89 6C 24 3C                  mov dword ptr [rsp + 0x3c], r13d
0097224B  FF C2                           inc edx
0097224D  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00972251  EB C8                           jmp 0x14097221b
00972253  85 FF                           test edi, edi
00972255  0F 88 56 01 00 00               js 0x1409723b1
0097225B  49 89 76 08                     mov qword ptr [r14 + 8], rsi
0097225F  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
00972263  0F 85 48 01 00 00               jne 0x1409723b1
00972269  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0097226F  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
00972276  41 3B 4E 04                     cmp ecx, dword ptr [r14 + 4]
0097227A  41 0F 45 FF                     cmovne edi, r15d
0097227E  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00972282  E9 94 01 00 00                  jmp 0x14097241b
00972287  42 0F B7 4C FE 10               movzx ecx, word ptr [rsi + r15*8 + 0x10]
0097228D  83 E9 01                        sub ecx, 1
00972290  74 21                           je 0x1409722b3
00972292  83 E9 01                        sub ecx, 1
00972295  74 1C                           je 0x1409722b3
00972297  83 E9 01                        sub ecx, 1
0097229A  74 51                           je 0x1409722ed
0097229C  83 E9 01                        sub ecx, 1
0097229F  0F 84 5F 01 00 00               je 0x140972404
009722A5  83 E9 01                        sub ecx, 1
009722A8  0F 84 3F 01 00 00               je 0x1409723ed
009722AE  83 E9 01                        sub ecx, 1
009722B1  75 5D                           jne 0x140972310
009722B3  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
009722B8  41 8B D2                        mov edx, r10d
009722BB  4A 8B 4C FE 20                  mov rcx, qword ptr [rsi + r15*8 + 0x20]
009722C0  E8 BF 08 00 00                  call 0x140972b84
009722C5  85 C0                           test eax, eax
009722C7  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009722CB  8B F8                           mov edi, eax
009722CD  79 35                           jns 0x140972304
009722CF  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
009722D3  85 FF                           test edi, edi
009722D5  0F 88 D6 00 00 00               js 0x1409723b1
009722DB  41 FF C5                        inc r13d
009722DE  44 89 6C 24 3C                  mov dword ptr [rsp + 0x3c], r13d
009722E3  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
009722E8  E9 5E FF FF FF                  jmp 0x14097224b
009722ED  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
009722F2  41 B0 01                        mov r8b, 1
009722F5  41 8B D2                        mov edx, r10d
009722F8  4A 8B 4C FE 20                  mov rcx, qword ptr [rsi + r15*8 + 0x20]
009722FD  E8 6E 0C 00 00                  call 0x140972f70
00972302  EB C1                           jmp 0x1409722c5
00972304  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00972309  4A 89 44 FE 20                  mov qword ptr [rsi + r15*8 + 0x20], rax
0097230E  EB BF                           jmp 0x1409722cf
00972310  83 F9 0A                        cmp ecx, 0xa
00972313  0F 84 D4 00 00 00               je 0x1409723ed
00972319  BF BB 00 00 C0                  mov edi, 0xc00000bb
0097231E  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00972322  EB AF                           jmp 0x1409722d3
00972324  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00972329  E9 3A FD FF FF                  jmp 0x140972068
0097232E  E8 9D 7C F2 FF                  call 0x140899fd0
00972333  8A 01                           mov al, byte ptr [rcx]
00972335  44 8B 6C 24 3C                  mov r13d, dword ptr [rsp + 0x3c]
0097233A  E9 53 FD FF FF                  jmp 0x140972092
0097233F  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00972347  4C 89 30                        mov qword ptr [rax], r14
0097234A  33 C0                           xor eax, eax
0097234C  E9 5C 01 00 00                  jmp 0x1409724ad
00972351  33 D2                           xor edx, edx
00972353  49 8B CE                        mov rcx, r14
00972356  E8 15 05 21 00                  call 0x140b82870
0097235B  8B C7                           mov eax, edi
0097235D  E9 4B 01 00 00                  jmp 0x1409724ad
00972362  33 D2                           xor edx, edx
00972364  49 8B CE                        mov rcx, r14
00972367  E8 04 05 21 00                  call 0x140b82870
0097236C  B8 9A 00 00 C0                  mov eax, 0xc000009a
00972371  E9 37 01 00 00                  jmp 0x1409724ad
00972376  E8 55 7C F2 FF                  call 0x140899fd0
0097237B  8A 02                           mov al, byte ptr [rdx]
0097237D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00972382  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
00972386  44 8B 6C 24 3C                  mov r13d, dword ptr [rsp + 0x3c]
0097238B  E9 B5 FD FF FF                  jmp 0x140972145
00972390  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
00972396  41 8B FF                        mov edi, r15d
00972399  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
0097239E  4C 8B E3                        mov r12, rbx
009723A1  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
009723A6  EB 73                           jmp 0x14097241b
009723A8  BF 9A 00 00 C0                  mov edi, 0xc000009a
009723AD  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
009723B1  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009723B7  EB 62                           jmp 0x14097241b
009723B9  E8 12 7C F2 FF                  call 0x140899fd0
009723BE  8A 00                           mov al, byte ptr [rax]
009723C0  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
009723C5  8B 7C 24 38                     mov edi, dword ptr [rsp + 0x38]
009723C9  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
009723CE  44 8B 6C 24 3C                  mov r13d, dword ptr [rsp + 0x3c]
009723D3  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
009723D8  E9 09 FE FF FF                  jmp 0x1409721e6
009723DD  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009723E3  41 8B FF                        mov edi, r15d
009723E6  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
009723EB  EB 2E                           jmp 0x14097241b
009723ED  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
009723F2  41 8B D2                        mov edx, r10d
009723F5  4A 8B 4C FE 20                  mov rcx, qword ptr [rsi + r15*8 + 0x20]
009723FA  E8 6D DB E2 FF                  call 0x14079ff6c
009723FF  E9 C1 FE FF FF                  jmp 0x1409722c5
00972404  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00972409  41 8B D2                        mov edx, r10d
0097240C  4A 8B 4C FE 20                  mov rcx, qword ptr [rsi + r15*8 + 0x20]
00972411  E8 22 D9 E2 FF                  call 0x14079fd38
00972416  E9 AA FE FF FF                  jmp 0x1409722c5
0097241B  EB 22                           jmp 0x14097243f
0097241D  8B F8                           mov edi, eax
0097241F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00972423  33 DB                           xor ebx, ebx
00972425  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0097242B  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00972430  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00972435  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0097243A  44 8B 6C 24 3C                  mov r13d, dword ptr [rsp + 0x3c]
0097243F  85 FF                           test edi, edi
00972441  0F 88 1B 01 00 00               js 0x140972562
00972447  8B CB                           mov ecx, ebx
00972449  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
00972450  41 39 5E 04                     cmp dword ptr [r14 + 4], ebx
00972454  76 42                           jbe 0x140972498
00972456  4C 8D 15 23 A6 1D 00            lea r10, [rip + 0x1da623]
0097245D  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
00972465  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
00972469  75 56                           jne 0x1409724c1
0097246B  8B C1                           mov eax, ecx
0097246D  41 8B 4C 85 00                  mov ecx, dword ptr [r13 + rax*4]
00972472  83 C1 FE                        add ecx, -2
00972475  F7 C1 FD FF FF FF               test ecx, 0xfffffffd
0097247B  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
00972482  74 3D                           je 0x1409724c1
00972484  FF C1                           inc ecx
00972486  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
0097248D  41 3B 4E 04                     cmp ecx, dword ptr [r14 + 4]
00972491  72 D2                           jb 0x140972465
00972493  44 8B 6C 24 3C                  mov r13d, dword ptr [rsp + 0x3c]
00972498  85 FF                           test edi, edi
0097249A  0F 88 C2 00 00 00               js 0x140972562
009724A0  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
009724A8  4C 89 30                        mov qword ptr [rax], r14
009724AB  8B C7                           mov eax, edi
009724AD  48 81 C4 80 00 00 00            add rsp, 0x80
009724B4  41 5F                           pop r15
009724B6  41 5E                           pop r14
009724B8  41 5D                           pop r13
009724BA  41 5C                           pop r12
009724BC  5F                              pop rdi
009724BD  5E                              pop rsi
009724BE  5B                              pop rbx
009724BF  C3                              ret
009724C0  CC                              int3
009724C1  8B C3                           mov eax, ebx
009724C3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009724C7  83 F8 04                        cmp eax, 4
009724CA  73 B8                           jae 0x140972484
009724CC  4C 8D 04 40                     lea r8, [rax + rax*2]
009724D0  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
009724D5  8B C1                           mov eax, ecx
009724D7  48 8D 04 80                     lea rax, [rax + rax*4]
009724DB  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009724E0  47 0F B7 0C C2                  movzx r9d, word ptr [r10 + r8*8]
009724E5  49 D1 E9                        shr r9, 1
009724E8  0F B7 14 C6                     movzx edx, word ptr [rsi + rax*8]
009724EC  48 D1 EA                        shr rdx, 1
009724EF  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
009724F4  4F 8B 44 C2 08                  mov r8, qword ptr [r10 + r8*8 + 8]
009724F9  48 8B 4C C6 08                  mov rcx, qword ptr [rsi + rax*8 + 8]
009724FE  E8 DD 02 00 00                  call 0x1409727e0
00972503  4C 8D 15 76 A5 1D 00            lea r10, [rip + 0x1da576]
0097250A  85 C0                           test eax, eax
0097250C  74 0F                           je 0x14097251d
0097250E  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00972512  FF C0                           inc eax
00972514  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
0097251B  EB A6                           jmp 0x1409724c3
0097251D  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00972522  0F B7 44 D6 10                  movzx eax, word ptr [rsi + rdx*8 + 0x10]
00972527  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0097252C  41 3B 44 CA 10                  cmp eax, dword ptr [r10 + rcx*8 + 0x10]
00972531  41 0F 45 FF                     cmovne edi, r15d
00972535  41 8B 44 CA 14                  mov eax, dword ptr [r10 + rcx*8 + 0x14]
0097253A  39 44 D6 18                     cmp dword ptr [rsi + rdx*8 + 0x18], eax
0097253E  41 0F 42 FF                     cmovb edi, r15d
00972542  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
00972549  E9 36 FF FF FF                  jmp 0x140972484
0097254E  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00972553  E9 55 FF FF FF                  jmp 0x1409724ad
00972558  B8 9A 00 00 C0                  mov eax, 0xc000009a
0097255D  E9 4B FF FF FF                  jmp 0x1409724ad
00972562  48 85 F6                        test rsi, rsi
00972565  0F 84 50 6C 1B 00               je 0x140b291bb
0097256B  39 5C 24 48                     cmp dword ptr [rsp + 0x48], ebx
0097256F  0F 86 1A 6C 1B 00               jbe 0x140b2918f
00972575  4C 8D 7E 08                     lea r15, [rsi + 8]
00972579  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
0097257E  E9 F3 6B 1B 00                  jmp 0x140b29176
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepCaptureTokenSecurityAttributesInformation(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p48;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_pD8;

    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (128);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned int *)(v_rsp - 112) = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned int *)(v_rsp - 124) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    if (a4 == 0) goto loc_0097254E;
    result = ExAllocatePool2(256, v_rbx + 16, (unsigned int)(0x74416553ULL), a4);
    v_stack_m50 = result;
    if (result == 0) goto loc_00972558;
    *(unsigned __int64 *)(result) = v_xmm0;
    if (v_stack_p20 != 1) goto loc_00972498;
    if (v_stack_p10 == 0) goto loc_00972324;
    if (v_stack_p18 < 1) goto loc_00972324;
    if ((*(unsigned int *)(v_stack_p10)) == 1) goto loc_00972324;
loc_00972068:
    if ((((unsigned __int8)(a1)) & (3)) != 0) goto loc_0097232E;
    if ((a1 + 16) > 256) goto loc_00972333;
    if ((a1 + 16) < a1) goto loc_00972333;
loc_00972092:
    *(unsigned __int16 *)(result) = (unsigned __int16)(*(unsigned __int16 *)(a1));
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 2));
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) == 0) goto loc_0097233F;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 8);
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 4)) + (unsigned int)(*(unsigned int *)(a1 + 4)) * 4) << (3);
    v_stack_m48 = a1;
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (a1 <= ((unsigned int)(0xFFFFFFFFULL))) { v_r12 = (unsigned int)(a1); }
    v_rdi = (unsigned int)((0) & (0xC0000095ULL));
    v_stack_m80 = (unsigned int)(v_rdi);
    if (condition_is_less) goto loc_00972351;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x74416553ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00972362;
    if ((unsigned int)(v_r12) == 0) goto loc_00972145;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 8))) & (3)) != 0) goto loc_00972376;
    if ((*(unsigned __int64 *)(result + 8) + v_r12 * 1) > ((unsigned int)((unsigned int)(v_r12)))) goto loc_0097237B;
    if ((*(unsigned __int64 *)(result + 8) + v_r12 * 1) < (*(unsigned __int64 *)(result + 8))) goto loc_0097237B;
loc_00972145:
    result = memcpy(result, *(unsigned __int64 *)(result + 8), (unsigned int)((unsigned int)(v_r12)), a4);
    v_stack_m84 = 0;
loc_0097215B:
    v_stack_m68 = 0;
    if (0 >= (*(unsigned int *)(result + 4))) goto loc_00972215;
    v_stack_m60 = result + 0 + 0 * 4 * 8;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 0 + 0 * 4 * 8)) == 0) goto loc_00972390;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 0 + 0 * 4 * 8))), (unsigned int)(0x74416553ULL), a4);
    v_stack_m68 = result;
    if (result == 0) goto loc_009723A8;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m60)) == 0) goto loc_009721E6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m60 + 8))) & (1)) != 0) goto loc_009723B9;
    if ((*(unsigned __int64 *)(v_stack_m60 + 8) + *(unsigned __int16 *)(v_stack_m60) * 1) > (*(unsigned __int16 *)(v_stack_m60))) goto loc_009723BE;
    if ((*(unsigned __int64 *)(v_stack_m60 + 8) + *(unsigned __int16 *)(v_stack_m60) * 1) < (*(unsigned __int64 *)(v_stack_m60 + 8))) goto loc_009723BE;
loc_009721E6:
    result = memcpy(result, *(unsigned __int64 *)(v_stack_m60 + 8), *(unsigned __int16 *)(v_stack_m60), a4);
    *(unsigned __int64 *)(v_stack_m60 + 8) = result;
    v_stack_m68 = 0;
    v_r15 = (unsigned int)((0) + 1);
    v_stack_m84 = (unsigned int)(v_r15);
    goto loc_0097215B;
loc_00972215:
    v_stack_m84 = 0;
loc_0097221B:
    if (0 >= (*(unsigned int *)(result + 4))) goto loc_00972253;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24))) != 0) goto loc_00972287;
    if (a5 == 0) goto loc_009723DD;
    *(unsigned __int64 *)(result + 0 + 0 * 4 * 8 + 32) = 0;
    v_r13 = (unsigned int)((0) + 1);
    v_stack_m7C = (unsigned int)(v_r13);
loc_0097224B:
    a2 = (unsigned int)((0) + 1);
    v_stack_m84 = (unsigned int)(a2);
    goto loc_0097221B;
loc_00972253:
    if (sign_flag) goto loc_009723B1;
    *(unsigned __int64 *)(result + 8) = result;
    if (v_stack_m88 != 0) goto loc_009723B1;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != (*(unsigned int *)(result + 4))) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_0097241B;
loc_00972287:
    a1 = (unsigned int)((*(unsigned __int16 *)(result + (unsigned int)(0xC000000DULL) * 8 + 16)) - (1));
    if (condition_is_equal) goto loc_009722B3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009722B3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009722ED;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00972404;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009723ED;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00972310;
loc_009722B3:
    result = SepCaptureInt64Array(*(unsigned __int64 *)(result + (unsigned int)(0xC000000DULL) * 8 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24)))), *(unsigned __int16 *)(v_stack_m60), v_stack_m78);
loc_009722C5:
    v_stack_m80 = (unsigned int)(result);
    if (!sign_flag) goto loc_00972304;
loc_009722CF:
loc_009722D3:
    if (sign_flag) goto loc_009723B1;
    v_r13 = (unsigned int)((v_r13) + 1);
    v_stack_m7C = (unsigned int)(v_r13);
    v_stack_m78 = 0;
    goto loc_0097224B;
loc_009722ED:
    result = SepCaptureUnicodeStringArray(*(unsigned __int64 *)(result + (unsigned int)(0xC000000DULL) * 8 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_00972304:
    *(unsigned __int64 *)(result + (unsigned int)(0xC000000DULL) * 8 + 32) = v_stack_m78;
    goto loc_009722CF;
loc_00972310:
    if (((unsigned int)(*(unsigned __int64 *)(result + (unsigned int)(0xC000000DULL) * 8 + 32))) == 10) goto loc_009723ED;
    v_stack_m80 = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_009722D3;
loc_00972324:
    v_stack_m88 = 1;
    goto loc_00972068;
loc_0097232E:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(result + (unsigned int)(0xC000000DULL) * 8 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24)))), 1, v_stack_m78);
loc_00972333:
    goto loc_00972092;
loc_0097233F:
    *(unsigned __int64 *)(a6) = result;
    result = 0;
    goto loc_009724AD;
loc_00972351:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, 1, v_stack_m78);
    goto loc_009724AD;
loc_00972362:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 1, v_stack_m78);
    goto loc_009724AD;
loc_00972376:
    result = ExRaiseDatatypeMisalignment(result, a2, 1, v_stack_m78);
loc_0097237B:
    goto loc_00972145;
loc_00972390:
    v_stack_m80 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_m68 = 0;
    goto loc_0097241B;
loc_009723A8:
    v_stack_m80 = (unsigned int)((unsigned int)(0xC000009AULL));
loc_009723B1:
    goto loc_0097241B;
loc_009723B9:
    result = ExRaiseDatatypeMisalignment(result, a2, 1, v_stack_m78);
loc_009723BE:
    goto loc_009721E6;
loc_009723DD:
    v_stack_m80 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0097241B;
loc_009723ED:
    result = SepCaptureOctetStringArray(*(unsigned __int64 *)(v_stack_m58 + (unsigned int)(0xC000000DULL) * 8 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_00972404:
    result = SepCaptureFqbnArray(*(unsigned __int64 *)(v_stack_m58 + (unsigned int)(0xC000000DULL) * 8 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 8 + 24)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_0097241B:
    goto loc_0097243F;
loc_0097243F:
    if (sign_flag) goto loc_00972562;
    v_stack_p20 = 0;
    if ((*(unsigned int *)(result + 4)) <= 0) goto loc_00972498;
loc_00972465:
    if (v_stack_m88 != 0) goto loc_009724C1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 0 * 4))) + (-2));
    if ((((unsigned int)(a1)) & (0xFFFFFFFDULL)) == 0) goto loc_009724C1;
loc_00972484:
    a1 = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_stack_p20 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < (*(unsigned int *)(result + 4))) goto loc_00972465;
loc_00972498:
    if (sign_flag) goto loc_00972562;
    *(unsigned __int64 *)(a6) = result;
loc_009724AD:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)))));
loc_009724C1:
loc_009724C3:
    v_stack_p58 = 0;
    if (0 >= 4) goto loc_00972484;
    v_stack_p70 = 0 + 0 * 2;
    v_stack_p78 = (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 4;
    a4 = (*(unsigned __int16 *)(v_rip + 1943075 + 0 + 0 * 2 * 8)) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_m58 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 4 * 8)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_m58 + (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 4 * 8 + 8), a2, *(unsigned __int64 *)(v_rip + 1943075 + 0 + 0 * 2 * 8 + 8), a4);
    if ((unsigned int)(result) == 0) goto loc_0097251D;
    result = (unsigned int)(((unsigned int)(v_stack_p58)) + 1);
    goto loc_009724C3;
loc_0097251D:
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m58 + v_stack_p78 * 8 + 16))) != (*(unsigned int *)(v_rip + 1942902 + v_stack_p70 * 8 + 16))) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    if ((*(unsigned int *)(v_stack_m58 + v_stack_p78 * 8 + 24)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1942902 + v_stack_p70 * 8 + 20))))) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    goto loc_00972484;
loc_0097254E:
    goto loc_009724AD;
loc_00972558:
    goto loc_009724AD;
loc_00972562:
}
```

## 5. (Beta) C Style

```c
int64_t SepCaptureTokenSecurityAttributesInformation(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint32_t v_stack_p48;
    uint32_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_pD8;

    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (128);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x70) = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint32_t *)(local_rsp - 0x7C) = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    if (Arg4 == 0) goto loc_0097254E;
    result = ExAllocatePool2(256, local_rbx + 16, (uint32_t)(0x74416553ULL), Arg4);
    v_stack_m50 = result;
    if (result == 0) goto loc_00972558;
    *(uint64_t *)(result) = v_xmm0;
    if (v_stack_p20 != 1) goto loc_00972498;
    if (v_stack_p10 == 0) goto loc_00972324;
    if (v_stack_p18 < 1) goto loc_00972324;
    if ((*(uint32_t *)(v_stack_p10)) == 1) goto loc_00972324;
loc_00972068:
    if ((((uint8_t)(Arg1)) & (3)) != 0) goto loc_0097232E;
    if ((Arg1 + 16) > 256) goto loc_00972333;
    if ((Arg1 + 16) < Arg1) goto loc_00972333;
loc_00972092:
    *(uint16_t *)(result) = (uint16_t)(*(uint16_t *)(Arg1));
    *(uint16_t *)(result + 0x2) = (uint16_t)(*(uint16_t *)(Arg1 + 0x2));
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4))) == 0) goto loc_0097233F;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(Arg1 + 0x8);
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg1 + 0x4)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x4)) * 4) << (3);
    v_stack_m48 = Arg1;
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (Arg1 <= ((uint32_t)(0xFFFFFFFFULL))) { local_r12 = (uint32_t)(Arg1); }
    local_rdi = (uint32_t)((0) & (0xC0000095ULL));
    v_stack_m80 = (uint32_t)(local_rdi);
    if (condition_is_less) goto loc_00972351;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x74416553ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00972362;
    if ((uint32_t)(local_r12) == 0) goto loc_00972145;
    if ((((uint8_t)(*(uint64_t *)(result + 0x8))) & (3)) != 0) goto loc_00972376;
    if ((*(uint64_t *)(result + 0x8) + local_r12 * 1) > ((uint32_t)((uint32_t)(local_r12)))) goto loc_0097237B;
    if ((*(uint64_t *)(result + 0x8) + local_r12 * 1) < (*(uint64_t *)(result + 0x8))) goto loc_0097237B;
loc_00972145:
    result = memcpy(result, *(uint64_t *)(result + 0x8), (uint32_t)((uint32_t)(local_r12)), Arg4);
    v_stack_m84 = 0;
loc_0097215B:
    v_stack_m68 = 0;
    if (0 >= (*(uint32_t *)(result + 0x4))) goto loc_00972215;
    v_stack_m60 = result + 0 + 0 * 4 * 8;
    if ((uint16_t)(*(uint16_t *)(result + 0x0 + 0x0 * 4 * 8)) == 0) goto loc_00972390;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x0 + 0x0 * 4 * 8))), (uint32_t)(0x74416553ULL), Arg4);
    v_stack_m68 = result;
    if (result == 0) goto loc_009723A8;
    if ((uint16_t)(*(uint16_t *)(v_stack_m60)) == 0) goto loc_009721E6;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m60 + 0x8))) & (1)) != 0) goto loc_009723B9;
    if ((*(uint64_t *)(v_stack_m60 + 0x8) + *(uint16_t *)(v_stack_m60) * 1) > (*(uint16_t *)(v_stack_m60))) goto loc_009723BE;
    if ((*(uint64_t *)(v_stack_m60 + 0x8) + *(uint16_t *)(v_stack_m60) * 1) < (*(uint64_t *)(v_stack_m60 + 0x8))) goto loc_009723BE;
loc_009721E6:
    result = memcpy(result, *(uint64_t *)(v_stack_m60 + 0x8), *(uint16_t *)(v_stack_m60), Arg4);
    *(uint64_t *)(v_stack_m60 + 0x8) = result;
    v_stack_m68 = 0;
    local_r15 = (uint32_t)((0) + 1);
    v_stack_m84 = (uint32_t)(local_r15);
    goto loc_0097215B;
loc_00972215:
    v_stack_m84 = 0;
loc_0097221B:
    if (0 >= (*(uint32_t *)(result + 0x4))) goto loc_00972253;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18))) != 0) goto loc_00972287;
    if (Arg5 == 0) goto loc_009723DD;
    *(uint64_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x20) = 0;
    local_r13 = (uint32_t)((0) + 1);
    v_stack_m7C = (uint32_t)(local_r13);
loc_0097224B:
    Arg2 = (uint32_t)((0) + 1);
    v_stack_m84 = (uint32_t)(Arg2);
    goto loc_0097221B;
loc_00972253:
    if (sign_flag) goto loc_009723B1;
    *(uint64_t *)(result + 0x8) = result;
    if (v_stack_m88 != 0) goto loc_009723B1;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != (*(uint32_t *)(result + 0x4))) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_0097241B;
loc_00972287:
    Arg1 = (uint32_t)((*(uint16_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x10)) - (1));
    if (condition_is_equal) goto loc_009722B3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009722B3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009722ED;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00972404;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009723ED;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00972310;
loc_009722B3:
    result = SepCaptureInt64Array(*(uint64_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18)))), *(uint16_t *)(v_stack_m60), v_stack_m78);
loc_009722C5:
    v_stack_m80 = (uint32_t)(result);
    if (!sign_flag) goto loc_00972304;
loc_009722CF:
loc_009722D3:
    if (sign_flag) goto loc_009723B1;
    local_r13 = (uint32_t)((local_r13) + 1);
    v_stack_m7C = (uint32_t)(local_r13);
    v_stack_m78 = 0;
    goto loc_0097224B;
loc_009722ED:
    result = SepCaptureUnicodeStringArray(*(uint64_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_00972304:
    *(uint64_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x20) = v_stack_m78;
    goto loc_009722CF;
loc_00972310:
    if (((uint32_t)(*(uint64_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x20))) == 10) goto loc_009723ED;
    v_stack_m80 = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_009722D3;
loc_00972324:
    v_stack_m88 = 1;
    goto loc_00972068;
loc_0097232E:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(result + (uint32_t)(0xC000000DULL) * 8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18)))), 1, v_stack_m78);
loc_00972333:
    goto loc_00972092;
loc_0097233F:
    *(uint64_t *)(arg6) = result;
    result = 0;
    goto loc_009724AD;
loc_00972351:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, 1, v_stack_m78);
    goto loc_009724AD;
loc_00972362:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 1, v_stack_m78);
    goto loc_009724AD;
loc_00972376:
    result = ExRaiseDatatypeMisalignment(result, Arg2, 1, v_stack_m78);
loc_0097237B:
    goto loc_00972145;
loc_00972390:
    v_stack_m80 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_m68 = 0;
    goto loc_0097241B;
loc_009723A8:
    v_stack_m80 = (uint32_t)((uint32_t)(0xC000009AULL));
loc_009723B1:
    goto loc_0097241B;
loc_009723B9:
    result = ExRaiseDatatypeMisalignment(result, Arg2, 1, v_stack_m78);
loc_009723BE:
    goto loc_009721E6;
loc_009723DD:
    v_stack_m80 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0097241B;
loc_009723ED:
    result = SepCaptureOctetStringArray(*(uint64_t *)(v_stack_m58 + (uint32_t)(0xC000000DULL) * 8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_00972404:
    result = SepCaptureFqbnArray(*(uint64_t *)(v_stack_m58 + (uint32_t)(0xC000000DULL) * 8 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 8 + 0x18)))), 1, v_stack_m78);
    goto loc_009722C5;
loc_0097241B:
    goto loc_0097243F;
loc_0097243F:
    if (sign_flag) goto loc_00972562;
    v_stack_p20 = 0;
    if ((*(uint32_t *)(result + 0x4)) <= 0) goto loc_00972498;
loc_00972465:
    if (v_stack_m88 != 0) goto loc_009724C1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x0 * 4))) + (-2));
    if ((((uint32_t)(Arg1)) & (0xFFFFFFFDULL)) == 0) goto loc_009724C1;
loc_00972484:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    v_stack_p20 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(result + 0x4))) goto loc_00972465;
loc_00972498:
    if (sign_flag) goto loc_00972562;
    *(uint64_t *)(arg6) = result;
loc_009724AD:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
loc_009724C1:
loc_009724C3:
    v_stack_p58 = 0;
    if (0 >= 4) goto loc_00972484;
    v_stack_p70 = 0 + 0 * 2;
    v_stack_p78 = (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 4;
    Arg4 = (*(uint16_t *)(v_rip + 0x1DA623 + 0x0 + 0x0 * 2 * 8)) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_m58 + (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 4 * 8)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_m58 + (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 4 * 8 + 0x8), Arg2, *(uint64_t *)(v_rip + 0x1DA623 + 0x0 + 0x0 * 2 * 8 + 0x8), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0097251D;
    result = (uint32_t)(((uint32_t)(v_stack_p58)) + 1);
    goto loc_009724C3;
loc_0097251D:
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if (((uint32_t)(*(uint16_t *)(v_stack_m58 + v_stack_p78 * 8 + 0x10))) != (*(uint32_t *)(v_rip + 0x1DA576 + v_stack_p70 * 8 + 0x10))) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    if ((*(uint32_t *)(v_stack_m58 + v_stack_p78 * 8 + 0x18)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1DA576 + v_stack_p70 * 8 + 0x14))))) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    goto loc_00972484;
loc_0097254E:
    goto loc_009724AD;
loc_00972558:
    goto loc_009724AD;
loc_00972562:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00971FB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
