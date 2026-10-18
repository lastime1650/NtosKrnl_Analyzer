# PnpFilterResourceRequirementsList

- RVA: `0x00AD0D7C`–`0x00AD14D6` (길이 `1,882` bytes)
- VA: `0x0000000140AD0D7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE97C`
- 디코드: `559`개 명령, `1,882/1,882` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AD0DDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD0E00` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD1067` → [RtlCmDecodeMemIoResource](../../text/4A/RtlCmDecodeMemIoResource_function_004A0120.md) (function, `0x004A0120`)
- `0x00AD108F` → [RtlIoDecodeMemIoResource](../../text/5E/RtlIoDecodeMemIoResource_function_005E7D80.md) (function, `0x005E7D80`)
- `0x00AD135E` → [PnpCmResourcesToIoResources](../73/PnpCmResourcesToIoResources_function_0073D584.md) (function, `0x0073D584`)
- `0x00AD1390` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD13A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD149C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD14B7` → [PnpCmResourcesToIoResources](../73/PnpCmResourcesToIoResources_function_0073D584.md) (function, `0x0073D584`)

### Direct callers
- [IopQueryDeviceResources](../8F/IopQueryDeviceResources_function_008FC344.md) at `0x008FC5B3`
- [PnpGetResourceRequirementsForAssignTable](../A2/PnpGetResourceRequirementsForAssignTable_function_00A2ADBC.md) at `0x00A2AF62`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AD0DDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD0E00` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD1067` → [RtlCmDecodeMemIoResource](../../text/4A/RtlCmDecodeMemIoResource_function_004A0120.md) (`PAGE` → `.text`)
  - `0x00AD108F` → [RtlIoDecodeMemIoResource](../../text/5E/RtlIoDecodeMemIoResource_function_005E7D80.md) (`PAGE` → `.text`)
  - `0x00AD1390` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD13A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD149C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD0D7C  48 8B C4                        mov rax, rsp
00AD0D7F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AD0D83  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AD0D87  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AD0D8B  55                              push rbp
00AD0D8C  53                              push rbx
00AD0D8D  56                              push rsi
00AD0D8E  57                              push rdi
00AD0D8F  41 54                           push r12
00AD0D91  41 55                           push r13
00AD0D93  41 56                           push r14
00AD0D95  41 57                           push r15
00AD0D97  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00AD0D9B  48 81 EC B8 00 00 00            sub rsp, 0xb8
00AD0DA2  33 DB                           xor ebx, ebx
00AD0DA4  4D 8B F0                        mov r14, r8
00AD0DA7  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
00AD0DAB  4C 8B E2                        mov r12, rdx
00AD0DAE  89 5D 87                        mov dword ptr [rbp - 0x79], ebx
00AD0DB1  48 8B F9                        mov rdi, rcx
00AD0DB4  49 89 18                        mov qword ptr [r8], rbx
00AD0DB7  44 8B FB                        mov r15d, ebx
00AD0DBA  41 89 19                        mov dword ptr [r9], ebx
00AD0DBD  48 85 C9                        test rcx, rcx
00AD0DC0  0F 84 E2 06 00 00               je 0x140ad14a8
00AD0DC6  39 59 1C                        cmp dword ptr [rcx + 0x1c], ebx
00AD0DC9  0F 84 D9 06 00 00               je 0x140ad14a8
00AD0DCF  8B 11                           mov edx, dword ptr [rcx]
00AD0DD1  41 B8 50 6E 70 36               mov r8d, 0x36706e50
00AD0DD7  B9 00 01 00 00                  mov ecx, 0x100
00AD0DDC  E8 0F 13 0B 00                  call 0x140b820f0
00AD0DE1  48 89 45 07                     mov qword ptr [rbp + 7], rax
00AD0DE5  4C 8B E8                        mov r13, rax
00AD0DE8  48 85 C0                        test rax, rax
00AD0DEB  75 0A                           jne 0x140ad0df7
00AD0DED  B8 9A 00 00 C0                  mov eax, 0xc000009a
00AD0DF2  E9 CA 06 00 00                  jmp 0x140ad14c1
00AD0DF7  44 8B 07                        mov r8d, dword ptr [rdi]
00AD0DFA  48 8B D7                        mov rdx, rdi
00AD0DFD  49 8B CD                        mov rcx, r13
00AD0E00  E8 3B 5A BF FF                  call 0x1406c6840
00AD0E05  4D 85 E4                        test r12, r12
00AD0E08  0F 84 95 06 00 00               je 0x140ad14a3
00AD0E0E  41 8B 04 24                     mov eax, dword ptr [r12]
00AD0E12  85 C0                           test eax, eax
00AD0E14  0F 84 89 06 00 00               je 0x140ad14a3
00AD0E1A  49 8D 7C 24 04                  lea rdi, [r12 + 4]
00AD0E1F  44 8B D8                        mov r11d, eax
00AD0E22  48 8B CF                        mov rcx, rdi
00AD0E25  BE 01 00 00 00                  mov esi, 1
00AD0E2A  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00AD0E2D  48 83 C1 10                     add rcx, 0x10
00AD0E31  44 03 F8                        add r15d, eax
00AD0E34  85 C0                           test eax, eax
00AD0E36  74 3C                           je 0x140ad0e74
00AD0E38  44 8B D0                        mov r10d, eax
00AD0E3B  44 0F B6 01                     movzx r8d, byte ptr [rcx]
00AD0E3F  44 8B CB                        mov r9d, ebx
00AD0E42  41 8B D0                        mov edx, r8d
00AD0E45  83 EA 05                        sub edx, 5
00AD0E48  74 14                           je 0x140ad0e5e
00AD0E4A  83 EA 7B                        sub edx, 0x7b
00AD0E4D  74 13                           je 0x140ad0e62
00AD0E4F  3B D6                           cmp edx, esi
00AD0E51  74 0F                           je 0x140ad0e62
00AD0E53  44 2A C6                        sub r8b, sil
00AD0E56  41 80 F8 06                     cmp r8b, 6
00AD0E5A  77 06                           ja 0x140ad0e62
00AD0E5C  EB 07                           jmp 0x140ad0e65
00AD0E5E  44 8B 49 04                     mov r9d, dword ptr [rcx + 4]
00AD0E62  41 FF CF                        dec r15d
00AD0E65  48 83 C1 14                     add rcx, 0x14
00AD0E69  41 8B C1                        mov eax, r9d
00AD0E6C  48 03 C8                        add rcx, rax
00AD0E6F  4C 2B D6                        sub r10, rsi
00AD0E72  75 C7                           jne 0x140ad0e3b
00AD0E74  4C 2B DE                        sub r11, rsi
00AD0E77  75 B1                           jne 0x140ad0e2a
00AD0E79  45 85 FF                        test r15d, r15d
00AD0E7C  0F 84 21 06 00 00               je 0x140ad14a3
00AD0E82  45 8B 4D 1C                     mov r9d, dword ptr [r13 + 0x1c]
00AD0E86  4D 8D 75 20                     lea r14, [r13 + 0x20]
00AD0E8A  44 2B CE                        sub r9d, esi
00AD0E8D  89 5D B7                        mov dword ptr [rbp - 0x49], ebx
00AD0E90  44 8B D3                        mov r10d, ebx
00AD0E93  49 8B D6                        mov rdx, r14
00AD0E96  78 35                           js 0x140ad0ecd
00AD0E98  4C 8D 42 08                     lea r8, [rdx + 8]
00AD0E9C  8B 52 04                        mov edx, dword ptr [rdx + 4]
00AD0E9F  48 C1 E2 05                     shl rdx, 5
00AD0EA3  49 03 D0                        add rdx, r8
00AD0EA6  EB 17                           jmp 0x140ad0ebf
00AD0EA8  41 38 58 01                     cmp byte ptr [r8 + 1], bl
00AD0EAC  41 8D 4A 01                     lea ecx, [r10 + 1]
00AD0EB0  41 88 58 03                     mov byte ptr [r8 + 3], bl
00AD0EB4  41 0F 45 CA                     cmovne ecx, r10d
00AD0EB8  49 83 C0 20                     add r8, 0x20
00AD0EBC  44 8B D1                        mov r10d, ecx
00AD0EBF  4C 3B C2                        cmp r8, rdx
00AD0EC2  72 E4                           jb 0x140ad0ea8
00AD0EC4  44 2B CE                        sub r9d, esi
00AD0EC7  79 CF                           jns 0x140ad0e98
00AD0EC9  44 89 55 B7                     mov dword ptr [rbp - 0x49], r10d
00AD0ECD  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
00AD0ED1  B9 FF FF 00 00                  mov ecx, 0xffff
00AD0ED6  89 45 CF                        mov dword ptr [rbp - 0x31], eax
00AD0ED9  8D 50 FF                        lea edx, [rax - 1]
00AD0EDC  89 55 B3                        mov dword ptr [rbp - 0x4d], edx
00AD0EDF  85 D2                           test edx, edx
00AD0EE1  0F 88 69 04 00 00               js 0x140ad1350
00AD0EE7  41 0F B7 06                     movzx eax, word ptr [r14]
00AD0EEB  89 45 A3                        mov dword ptr [rbp - 0x5d], eax
00AD0EEE  66 3B C1                        cmp ax, cx
00AD0EF1  75 03                           jne 0x140ad0ef6
00AD0EF3  89 75 A3                        mov dword ptr [rbp - 0x5d], esi
00AD0EF6  45 8B 5E 04                     mov r11d, dword ptr [r14 + 4]
00AD0EFA  4D 8D 4E 08                     lea r9, [r14 + 8]
00AD0EFE  45 8B C3                        mov r8d, r11d
00AD0F01  66 41 89 1E                     mov word ptr [r14], bx
00AD0F05  49 C1 E0 05                     shl r8, 5
00AD0F09  4D 03 C1                        add r8, r9
00AD0F0C  4C 89 5D 0F                     mov qword ptr [rbp + 0xf], r11
00AD0F10  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
00AD0F14  4D 3B C8                        cmp r9, r8
00AD0F17  75 0D                           jne 0x140ad0f26
00AD0F19  66 41 89 0E                     mov word ptr [r14], cx
00AD0F1D  41 FF 4D 1C                     dec dword ptr [r13 + 0x1c]
00AD0F21  E9 1B 04 00 00                  jmp 0x140ad1341
00AD0F26  48 8B C7                        mov rax, rdi
00AD0F29  44 8B D6                        mov r10d, esi
00AD0F2C  8B CB                           mov ecx, ebx
00AD0F2E  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
00AD0F32  89 75 8B                        mov dword ptr [rbp - 0x75], esi
00AD0F35  89 5D AF                        mov dword ptr [rbp - 0x51], ebx
00AD0F38  41 39 1C 24                     cmp dword ptr [r12], ebx
00AD0F3C  0F 86 F9 02 00 00               jbe 0x140ad123b
00AD0F42  44 89 7D CB                     mov dword ptr [rbp - 0x35], r15d
00AD0F46  4C 8D 58 10                     lea r11, [rax + 0x10]
00AD0F4A  44 8B FB                        mov r15d, ebx
00AD0F4D  4C 89 5D 97                     mov qword ptr [rbp - 0x69], r11
00AD0F51  39 58 0C                        cmp dword ptr [rax + 0xc], ebx
00AD0F54  0F 86 B7 02 00 00               jbe 0x140ad1211
00AD0F5A  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00AD0F5E  41 0F B6 0B                     movzx ecx, byte ptr [r11]
00AD0F62  8B D1                           mov edx, ecx
00AD0F64  83 EA 05                        sub edx, 5
00AD0F67  0F 84 91 03 00 00               je 0x140ad12fe
00AD0F6D  83 FA 7C                        cmp edx, 0x7c
00AD0F70  0F 84 72 02 00 00               je 0x140ad11e8
00AD0F76  40 2A CE                        sub cl, sil
00AD0F79  80 F9 06                        cmp cl, 6
00AD0F7C  0F 87 66 02 00 00               ja 0x140ad11e8
00AD0F82  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
00AD0F85  49 8B F9                        mov rdi, r9
00AD0F88  49 3B F8                        cmp rdi, r8
00AD0F8B  0F 83 3E 02 00 00               jae 0x140ad11cf
00AD0F91  41 8A 03                        mov al, byte ptr [r11]
00AD0F94  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00AD0F97  38 47 01                        cmp byte ptr [rdi + 1], al
00AD0F9A  0F 85 7F 01 00 00               jne 0x140ad111f
00AD0FA0  38 5F 03                        cmp byte ptr [rdi + 3], bl
00AD0FA3  0F 85 76 01 00 00               jne 0x140ad111f
00AD0FA9  41 0F B6 43 01                  movzx eax, byte ptr [r11 + 1]
00AD0FAE  4C 8B E3                        mov r12, rbx
00AD0FB1  0F B6 57 02                     movzx edx, byte ptr [rdi + 2]
00AD0FB5  8A C8                           mov cl, al
00AD0FB7  40 2A CE                        sub cl, sil
00AD0FBA  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
00AD0FBE  80 F9 02                        cmp cl, 2
00AD0FC1  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
00AD0FC5  8A CA                           mov cl, dl
00AD0FC7  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00AD0FCB  44 8B D8                        mov r11d, eax
00AD0FCE  48 89 75 8F                     mov qword ptr [rbp - 0x71], rsi
00AD0FD2  44 0F 47 DA                     cmova r11d, edx
00AD0FD6  48 89 75 EF                     mov qword ptr [rbp - 0x11], rsi
00AD0FDA  40 2A CE                        sub cl, sil
00AD0FDD  41 0F B6 C3                     movzx eax, r11b
00AD0FE1  80 F9 02                        cmp cl, 2
00AD0FE4  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
00AD0FE8  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
00AD0FEC  4C 8B CB                        mov r9, rbx
00AD0FEF  0F 47 D0                        cmova edx, eax
00AD0FF2  4C 8B C3                        mov r8, rbx
00AD0FF5  89 55 A7                        mov dword ptr [rbp - 0x59], edx
00AD0FF8  4C 8B D6                        mov r10, rsi
00AD0FFB  2B CE                           sub ecx, esi
00AD0FFD  74 60                           je 0x140ad105f
00AD0FFF  2B CE                           sub ecx, esi
00AD1001  74 43                           je 0x140ad1046
00AD1003  2B CE                           sub ecx, esi
00AD1005  74 58                           je 0x140ad105f
00AD1007  2B CE                           sub ecx, esi
00AD1009  74 2F                           je 0x140ad103a
00AD100B  83 E9 02                        sub ecx, 2
00AD100E  74 09                           je 0x140ad1019
00AD1010  3B CE                           cmp ecx, esi
00AD1012  74 4B                           je 0x140ad105f
00AD1014  48 8B D3                        mov rdx, rbx
00AD1017  EB 40                           jmp 0x140ad1059
00AD1019  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00AD101D  44 8B 4F 0C                     mov r9d, dword ptr [rdi + 0xc]
00AD1021  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
00AD1025  8B 47 08                        mov eax, dword ptr [rdi + 8]
00AD1028  44 8B 61 04                     mov r12d, dword ptr [rcx + 4]
00AD102C  44 8B 51 08                     mov r10d, dword ptr [rcx + 8]
00AD1030  41 8D 54 24 FF                  lea edx, [r12 - 1]
00AD1035  41 03 D2                        add edx, r10d
00AD1038  EB 6E                           jmp 0x140ad10a8
00AD103A  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00AD103E  8B 51 04                        mov edx, dword ptr [rcx + 4]
00AD1041  44 8B E2                        mov r12d, edx
00AD1044  EB 0B                           jmp 0x140ad1051
00AD1046  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00AD104A  44 8B 61 08                     mov r12d, dword ptr [rcx + 8]
00AD104E  41 8B D4                        mov edx, r12d
00AD1051  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
00AD1055  44 8B 47 0C                     mov r8d, dword ptr [rdi + 0xc]
00AD1059  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00AD105D  EB 4D                           jmp 0x140ad10ac
00AD105F  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00AD1063  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00AD1067  E8 B4 F0 9C FF                  call 0x1404a0120
00AD106C  4C 8B 65 BF                     mov r12, qword ptr [rbp - 0x41]
00AD1070  4C 8D 4D E7                     lea r9, [rbp - 0x19]
00AD1074  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00AD1078  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00AD107C  48 8D 55 EF                     lea rdx, [rbp - 0x11]
00AD1080  49 8D 4C 24 FF                  lea rcx, [r12 - 1]
00AD1085  48 03 C8                        add rcx, rax
00AD1088  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
00AD108C  48 8B CF                        mov rcx, rdi
00AD108F  E8 EC 6C B1 FF                  call 0x1405e7d80
00AD1094  4C 8B 4D DF                     mov r9, qword ptr [rbp - 0x21]
00AD1098  4C 8B 45 E7                     mov r8, qword ptr [rbp - 0x19]
00AD109C  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
00AD10A0  4C 8B 55 FF                     mov r10, qword ptr [rbp - 1]
00AD10A4  44 8B 5D C7                     mov r11d, dword ptr [rbp - 0x39]
00AD10A8  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
00AD10AC  39 5D 9F                        cmp dword ptr [rbp - 0x61], ebx
00AD10AF  75 42                           jne 0x140ad10f3
00AD10B1  44 3A 5D A7                     cmp r11b, byte ptr [rbp - 0x59]
00AD10B5  75 60                           jne 0x140ad1117
00AD10B7  4D 3B CC                        cmp r9, r12
00AD10BA  75 5B                           jne 0x140ad1117
00AD10BC  4C 3B C2                        cmp r8, rdx
00AD10BF  72 56                           jb 0x140ad1117
00AD10C1  49 3B C2                        cmp rax, r10
00AD10C4  72 51                           jb 0x140ad1117
00AD10C6  44 8B 55 8B                     mov r10d, dword ptr [rbp - 0x75]
00AD10CA  4C 3B C2                        cmp r8, rdx
00AD10CD  44 0F 45 D3                     cmovne r10d, ebx
00AD10D1  66 41 01 36                     add word ptr [r14], si
00AD10D5  F6 07 08                        test byte ptr [rdi], 8
00AD10D8  44 89 55 8B                     mov dword ptr [rbp - 0x75], r10d
00AD10DC  C6 47 03 80                     mov byte ptr [rdi + 3], 0x80
00AD10E0  0F 84 A3 01 00 00               je 0x140ad1289
00AD10E6  48 8D 47 E0                     lea rax, [rdi - 0x20]
00AD10EA  49 8D 4E 08                     lea rcx, [r14 + 8]
00AD10EE  E9 91 01 00 00                  jmp 0x140ad1284
00AD10F3  89 5D 8B                        mov dword ptr [rbp - 0x75], ebx
00AD10F6  44 3A 5D A7                     cmp r11b, byte ptr [rbp - 0x59]
00AD10FA  75 1B                           jne 0x140ad1117
00AD10FC  4D 3B CC                        cmp r9, r12
00AD10FF  77 16                           ja 0x140ad1117
00AD1101  4C 3B C2                        cmp r8, rdx
00AD1104  72 11                           jb 0x140ad1117
00AD1106  49 3B C2                        cmp rax, r10
00AD1109  72 0C                           jb 0x140ad1117
00AD110B  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00AD110F  48 FF C8                        dec rax
00AD1112  49 85 C4                        test r12, rax
00AD1115  74 15                           je 0x140ad112c
00AD1117  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
00AD111B  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00AD111F  B8 20 00 00 00                  mov eax, 0x20
00AD1124  48 03 F8                        add rdi, rax
00AD1127  E9 5C FE FF FF                  jmp 0x140ad0f88
00AD112C  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
00AD1130  2B CE                           sub ecx, esi
00AD1132  74 15                           je 0x140ad1149
00AD1134  2B CE                           sub ecx, esi
00AD1136  74 59                           je 0x140ad1191
00AD1138  2B CE                           sub ecx, esi
00AD113A  74 0D                           je 0x140ad1149
00AD113C  2B CE                           sub ecx, esi
00AD113E  74 51                           je 0x140ad1191
00AD1140  83 E9 02                        sub ecx, 2
00AD1143  74 3A                           je 0x140ad117f
00AD1145  3B CE                           cmp ecx, esi
00AD1147  75 12                           jne 0x140ad115b
00AD1149  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00AD114D  48 FF C8                        dec rax
00AD1150  4C 89 67 10                     mov qword ptr [rdi + 0x10], r12
00AD1154  49 03 C4                        add rax, r12
00AD1157  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00AD115B  66 41 01 36                     add word ptr [r14], si
00AD115F  4D 8D 4E 08                     lea r9, [r14 + 8]
00AD1163  F6 07 08                        test byte ptr [rdi], 8
00AD1166  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
00AD116A  C6 47 03 80                     mov byte ptr [rdi + 3], 0x80
00AD116E  41 0F B7 43 02                  movzx eax, word ptr [r11 + 2]
00AD1173  66 89 47 04                     mov word ptr [rdi + 4], ax
00AD1177  74 36                           je 0x140ad11af
00AD1179  48 8D 47 E0                     lea rax, [rdi - 0x20]
00AD117D  EB 2B                           jmp 0x140ad11aa
00AD117F  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00AD1183  FF C8                           dec eax
00AD1185  44 89 67 0C                     mov dword ptr [rdi + 0xc], r12d
00AD1189  41 03 C4                        add eax, r12d
00AD118C  89 47 10                        mov dword ptr [rdi + 0x10], eax
00AD118F  EB CA                           jmp 0x140ad115b
00AD1191  44 89 67 08                     mov dword ptr [rdi + 8], r12d
00AD1195  89 57 0C                        mov dword ptr [rdi + 0xc], edx
00AD1198  EB C1                           jmp 0x140ad115b
00AD119A  88 58 01                        mov byte ptr [rax + 1], bl
00AD119D  41 FF 4E 04                     dec dword ptr [r14 + 4]
00AD11A1  80 38 08                        cmp byte ptr [rax], 8
00AD11A4  75 09                           jne 0x140ad11af
00AD11A6  48 83 E8 20                     sub rax, 0x20
00AD11AA  49 3B C1                        cmp rax, r9
00AD11AD  73 EB                           jae 0x140ad119a
00AD11AF  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00AD11B3  40 88 37                        mov byte ptr [rdi], sil
00AD11B6  EB 0C                           jmp 0x140ad11c4
00AD11B8  F6 07 08                        test byte ptr [rdi], 8
00AD11BB  74 16                           je 0x140ad11d3
00AD11BD  88 5F 01                        mov byte ptr [rdi + 1], bl
00AD11C0  41 FF 4E 04                     dec dword ptr [r14 + 4]
00AD11C4  48 83 C7 20                     add rdi, 0x20
00AD11C8  49 3B F8                        cmp rdi, r8
00AD11CB  72 EB                           jb 0x140ad11b8
00AD11CD  EB 04                           jmp 0x140ad11d3
00AD11CF  4D 8D 4E 08                     lea r9, [r14 + 8]
00AD11D3  8B 45 9F                        mov eax, dword ptr [rbp - 0x61]
00AD11D6  03 C6                           add eax, esi
00AD11D8  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00AD11DB  83 F8 02                        cmp eax, 2
00AD11DE  0F 82 A1 FD FF FF               jb 0x140ad0f85
00AD11E4  44 8B 55 8B                     mov r10d, dword ptr [rbp - 0x75]
00AD11E8  8B C3                           mov eax, ebx
00AD11EA  49 83 C3 14                     add r11, 0x14
00AD11EE  4D 8D 4E 08                     lea r9, [r14 + 8]
00AD11F2  4C 03 D8                        add r11, rax
00AD11F5  44 03 FE                        add r15d, esi
00AD11F8  4C 89 5D 97                     mov qword ptr [rbp - 0x69], r11
00AD11FC  45 3B 7D 0C                     cmp r15d, dword ptr [r13 + 0xc]
00AD1200  0F 82 58 FD FF FF               jb 0x140ad0f5e
00AD1206  4C 8B 65 6F                     mov r12, qword ptr [rbp + 0x6f]
00AD120A  4D 8D 4E 08                     lea r9, [r14 + 8]
00AD120E  8B 4D AF                        mov ecx, dword ptr [rbp - 0x51]
00AD1211  03 CE                           add ecx, esi
00AD1213  49 8B C3                        mov rax, r11
00AD1216  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
00AD121A  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
00AD121D  41 3B 0C 24                     cmp ecx, dword ptr [r12]
00AD1221  0F 82 1F FD FF FF               jb 0x140ad0f46
00AD1227  44 8B 7D CB                     mov r15d, dword ptr [rbp - 0x35]
00AD122B  49 8D 7C 24 04                  lea rdi, [r12 + 4]
00AD1230  4C 8B 6D 07                     mov r13, qword ptr [rbp + 7]
00AD1234  8B 55 B3                        mov edx, dword ptr [rbp - 0x4d]
00AD1237  4C 8B 5D 0F                     mov r11, qword ptr [rbp + 0xf]
00AD123B  66 45 39 3E                     cmp word ptr [r14], r15w
00AD123F  0F 85 C8 00 00 00               jne 0x140ad130d
00AD1245  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD1249  41 3B CF                        cmp ecx, r15d
00AD124C  0F 84 B5 00 00 00               je 0x140ad1307
00AD1252  41 8D 47 01                     lea eax, [r15 + 1]
00AD1256  3B C8                           cmp ecx, eax
00AD1258  75 0B                           jne 0x140ad1265
00AD125A  41 80 7E 09 80                  cmp byte ptr [r14 + 9], 0x80
00AD125F  0F 84 A2 00 00 00               je 0x140ad1307
00AD1265  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00AD1268  01 4D 87                        add dword ptr [rbp - 0x79], ecx
00AD126B  66 41 89 06                     mov word ptr [r14], ax
00AD126F  E9 C1 00 00 00                  jmp 0x140ad1335
00AD1274  88 58 01                        mov byte ptr [rax + 1], bl
00AD1277  41 FF 4E 04                     dec dword ptr [r14 + 4]
00AD127B  80 38 08                        cmp byte ptr [rax], 8
00AD127E  75 09                           jne 0x140ad1289
00AD1280  48 83 E8 20                     sub rax, 0x20
00AD1284  48 3B C1                        cmp rax, rcx
00AD1287  73 EB                           jae 0x140ad1274
00AD1289  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
00AD128D  8A 4F 01                        mov cl, byte ptr [rdi + 1]
00AD1290  40 88 37                        mov byte ptr [rdi], sil
00AD1293  41 0F B7 43 02                  movzx eax, word ptr [r11 + 2]
00AD1298  66 89 47 04                     mov word ptr [rdi + 4], ax
00AD129C  8A C1                           mov al, cl
00AD129E  40 2A C6                        sub al, sil
00AD12A1  A8 F9                           test al, 0xf9
00AD12A3  75 1C                           jne 0x140ad12c1
00AD12A5  80 F9 05                        cmp cl, 5
00AD12A8  74 17                           je 0x140ad12c1
00AD12AA  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00AD12AE  48 FF C8                        dec rax
00AD12B1  4C 89 67 10                     mov qword ptr [rdi + 0x10], r12
00AD12B5  49 03 C4                        add rax, r12
00AD12B8  89 77 0C                        mov dword ptr [rdi + 0xc], esi
00AD12BB  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00AD12BF  EB 15                           jmp 0x140ad12d6
00AD12C1  80 F9 06                        cmp cl, 6
00AD12C4  75 10                           jne 0x140ad12d6
00AD12C6  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00AD12CA  FF C8                           dec eax
00AD12CC  44 89 67 0C                     mov dword ptr [rdi + 0xc], r12d
00AD12D0  41 03 C4                        add eax, r12d
00AD12D3  89 47 10                        mov dword ptr [rdi + 0x10], eax
00AD12D6  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00AD12DA  48 83 C7 20                     add rdi, 0x20
00AD12DE  EB 14                           jmp 0x140ad12f4
00AD12E0  F6 07 08                        test byte ptr [rdi], 8
00AD12E3  0F 84 FF FE FF FF               je 0x140ad11e8
00AD12E9  88 5F 01                        mov byte ptr [rdi + 1], bl
00AD12EC  48 83 C7 20                     add rdi, 0x20
00AD12F0  41 FF 4E 04                     dec dword ptr [r14 + 4]
00AD12F4  49 3B F8                        cmp rdi, r8
00AD12F7  72 E7                           jb 0x140ad12e0
00AD12F9  E9 EA FE FF FF                  jmp 0x140ad11e8
00AD12FE  41 8B 43 04                     mov eax, dword ptr [r11 + 4]
00AD1302  E9 E3 FE FF FF                  jmp 0x140ad11ea
00AD1307  48 39 5D F7                     cmp qword ptr [rbp - 9], rbx
00AD130B  74 0F                           je 0x140ad131c
00AD130D  B9 FF FF 00 00                  mov ecx, 0xffff
00AD1312  66 41 89 0E                     mov word ptr [r14], cx
00AD1316  41 FF 4D 1C                     dec dword ptr [r13 + 0x1c]
00AD131A  EB 1E                           jmp 0x140ad133a
00AD131C  01 4D 87                        add dword ptr [rbp - 0x79], ecx
00AD131F  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00AD1322  4C 89 75 F7                     mov qword ptr [rbp - 9], r14
00AD1326  66 41 89 06                     mov word ptr [r14], ax
00AD132A  45 85 D2                        test r10d, r10d
00AD132D  74 06                           je 0x140ad1335
00AD132F  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AD1333  89 30                           mov dword ptr [rax], esi
00AD1335  B9 FF FF 00 00                  mov ecx, 0xffff
00AD133A  45 89 5E 04                     mov dword ptr [r14 + 4], r11d
00AD133E  4D 8B F0                        mov r14, r8
00AD1341  2B D6                           sub edx, esi
00AD1343  89 55 B3                        mov dword ptr [rbp - 0x4d], edx
00AD1346  0F 89 9B FB FF FF               jns 0x140ad0ee7
00AD134C  44 8B 55 B7                     mov r10d, dword ptr [rbp - 0x49]
00AD1350  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
00AD1354  85 C0                           test eax, eax
00AD1356  75 14                           jne 0x140ad136c
00AD1358  44 8B C6                        mov r8d, esi
00AD135B  49 8B D4                        mov rdx, r12
00AD135E  E8 21 C2 C6 FF                  call 0x14073d584
00AD1363  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00AD1367  48 89 01                        mov qword ptr [rcx], rax
00AD136A  EB 36                           jmp 0x140ad13a2
00AD136C  8B 4D 87                        mov ecx, dword ptr [rbp - 0x79]
00AD136F  41 B8 50 6E 70 36               mov r8d, 0x36706e50
00AD1375  41 2B CA                        sub ecx, r10d
00AD1378  C1 E1 05                        shl ecx, 5
00AD137B  FF C8                           dec eax
00AD137D  8D 14 85 09 00 00 00            lea edx, [rax*4 + 9]
00AD1384  03 D0                           add edx, eax
00AD1386  8D 3C D1                        lea edi, [rcx + rdx*8]
00AD1389  B9 00 01 00 00                  mov ecx, 0x100
00AD138E  8B D7                           mov edx, edi
00AD1390  E8 5B 0D 0B 00                  call 0x140b820f0
00AD1395  48 8B D0                        mov rdx, rax
00AD1398  48 85 C0                        test rax, rax
00AD139B  75 16                           jne 0x140ad13b3
00AD139D  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AD13A2  33 D2                           xor edx, edx
00AD13A4  49 8B CD                        mov rcx, r13
00AD13A7  E8 C4 14 0B 00                  call 0x140b82870
00AD13AC  8B C3                           mov eax, ebx
00AD13AE  E9 0E 01 00 00                  jmp 0x140ad14c1
00AD13B3  89 38                           mov dword ptr [rax], edi
00AD13B5  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00AD13BA  89 42 04                        mov dword ptr [rdx + 4], eax
00AD13BD  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00AD13C2  89 42 08                        mov dword ptr [rdx + 8], eax
00AD13C5  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
00AD13C9  89 42 0C                        mov dword ptr [rdx + 0xc], eax
00AD13CC  41 8B 45 1C                     mov eax, dword ptr [r13 + 0x1c]
00AD13D0  3B C6                           cmp eax, esi
00AD13D2  76 06                           jbe 0x140ad13da
00AD13D4  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00AD13D8  89 19                           mov dword ptr [rcx], ebx
00AD13DA  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
00AD13DD  4D 8D 55 20                     lea r10, [r13 + 0x20]
00AD13E1  2B FE                           sub edi, esi
00AD13E3  89 42 1C                        mov dword ptr [rdx + 0x1c], eax
00AD13E6  4C 8D 5A 20                     lea r11, [rdx + 0x20]
00AD13EA  0F 88 A0 00 00 00               js 0x140ad1490
00AD13F0  41 BE FF FF 00 00               mov r14d, 0xffff
00AD13F6  45 8B 4A 04                     mov r9d, dword ptr [r10 + 4]
00AD13FA  4D 8D 42 08                     lea r8, [r10 + 8]
00AD13FE  41 0F B7 02                     movzx eax, word ptr [r10]
00AD1402  49 C1 E1 05                     shl r9, 5
00AD1406  4D 03 C8                        add r9, r8
00AD1409  66 41 3B C6                     cmp ax, r14w
00AD140D  74 76                           je 0x140ad1485
00AD140F  66 41 89 03                     mov word ptr [r11], ax
00AD1413  49 8D 4B 08                     lea rcx, [r11 + 8]
00AD1417  41 0F B7 42 02                  movzx eax, word ptr [r10 + 2]
00AD141C  66 41 89 43 02                  mov word ptr [r11 + 2], ax
00AD1421  41 80 7A 09 80                  cmp byte ptr [r10 + 9], 0x80
00AD1426  4C 8B D1                        mov r10, rcx
00AD1429  74 19                           je 0x140ad1444
00AD142B  66 C7 01 01 80                  mov word ptr [rcx], 0x8001
00AD1430  C7 41 02 03 00 00 00            mov dword ptr [rcx + 2], 3
00AD1437  66 89 59 06                     mov word ptr [rcx + 6], bx
00AD143B  89 71 08                        mov dword ptr [rcx + 8], esi
00AD143E  48 83 C1 20                     add rcx, 0x20
00AD1442  EB 23                           jmp 0x140ad1467
00AD1444  83 02 E0                        add dword ptr [rdx], -0x20
00AD1447  EB 1E                           jmp 0x140ad1467
00AD1449  41 38 58 01                     cmp byte ptr [r8 + 1], bl
00AD144D  74 14                           je 0x140ad1463
00AD144F  41 0F 10 00                     movups xmm0, xmmword ptr [r8]
00AD1453  0F 11 01                        movups xmmword ptr [rcx], xmm0
00AD1456  41 0F 10 48 10                  movups xmm1, xmmword ptr [r8 + 0x10]
00AD145B  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00AD145F  48 83 C1 20                     add rcx, 0x20
00AD1463  49 83 C0 20                     add r8, 0x20
00AD1467  4D 3B C1                        cmp r8, r9
00AD146A  72 DD                           jb 0x140ad1449
00AD146C  48 8B C1                        mov rax, rcx
00AD146F  49 2B C3                        sub rax, r11
00AD1472  48 83 E8 08                     sub rax, 8
00AD1476  48 C1 F8 05                     sar rax, 5
00AD147A  41 89 43 04                     mov dword ptr [r11 + 4], eax
00AD147E  4C 8B D9                        mov r11, rcx
00AD1481  41 89 72 08                     mov dword ptr [r10 + 8], esi
00AD1485  2B FE                           sub edi, esi
00AD1487  4D 8B D1                        mov r10, r9
00AD148A  0F 89 66 FF FF FF               jns 0x140ad13f6
00AD1490  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00AD1494  48 89 11                        mov qword ptr [rcx], rdx
00AD1497  33 D2                           xor edx, edx
00AD1499  49 8B CD                        mov rcx, r13
00AD149C  E8 CF 13 0B 00                  call 0x140b82870
00AD14A1  EB 1C                           jmp 0x140ad14bf
00AD14A3  4D 89 2E                        mov qword ptr [r14], r13
00AD14A6  EB 17                           jmp 0x140ad14bf
00AD14A8  4D 85 E4                        test r12, r12
00AD14AB  74 12                           je 0x140ad14bf
00AD14AD  39 1A                           cmp dword ptr [rdx], ebx
00AD14AF  74 0E                           je 0x140ad14bf
00AD14B1  41 B8 01 00 00 00               mov r8d, 1
00AD14B7  E8 C8 C0 C6 FF                  call 0x14073d584
00AD14BC  49 89 06                        mov qword ptr [r14], rax
00AD14BF  33 C0                           xor eax, eax
00AD14C1  48 81 C4 B8 00 00 00            add rsp, 0xb8
00AD14C8  41 5F                           pop r15
00AD14CA  41 5E                           pop r14
00AD14CC  41 5D                           pop r13
00AD14CE  41 5C                           pop r12
00AD14D0  5F                              pop rdi
00AD14D1  5E                              pop rsi
00AD14D2  5B                              pop rbx
00AD14D3  5D                              pop rbp
00AD14D4  C3                              ret
00AD14D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpFilterResourceRequirementsList(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (184);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
    *(unsigned int *)(v_rsp - 95 - 121) = 0;
    *(unsigned __int64 *)(a3) = 0;
    *(unsigned int *)(a4) = 0;
    if (a1 == 0) goto loc_00AD14A8;
    if ((*(unsigned int *)(a1 + 28)) == 0) goto loc_00AD14A8;
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(a1)), (unsigned int)(0x36706E50ULL), a4);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
    if (result != 0) goto loc_00AD0DF7;
    goto loc_00AD14C1;
loc_00AD0DF7:
    result = memcpy(result, a1, (unsigned int)(*(unsigned int *)(a1)), a4);
    if (a2 == 0) goto loc_00AD14A3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_00AD14A3;
loc_00AD0E2A:
    a1 = (a2 + 4) + (16);
    v_r15 = (unsigned int)((0) + ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4 + 12)))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4 + 12))) == 0) goto loc_00AD0E74;
loc_00AD0E3B:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1)))) - (5));
    if (condition_is_equal) goto loc_00AD0E5E;
    a2 = (unsigned int)((a2) - (123));
    if (condition_is_equal) goto loc_00AD0E62;
    if (((unsigned int)(a2)) == 1) goto loc_00AD0E62;
    a3 = (unsigned __int8)((*(unsigned __int8 *)(a1)) - (1));
    if (((unsigned __int8)(a3)) > 6) goto loc_00AD0E62;
    goto loc_00AD0E65;
loc_00AD0E5E:
loc_00AD0E62:
    v_r15 = (unsigned int)((v_r15) - 1);
loc_00AD0E65:
    a1 = (a1) + (20);
    a1 = (a1) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4 + 12))))) - (1);
    if (condition_is_not_equal) goto loc_00AD0E3B;
loc_00AD0E74:
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) - (1);
    if (condition_is_not_equal) goto loc_00AD0E2A;
    if ((unsigned int)(v_r15) == 0) goto loc_00AD14A3;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 28))) - (1));
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    if (sign_flag) goto loc_00AD0ECD;
loc_00AD0E98:
    a2 = ((unsigned int)(*(unsigned int *)(result + 32 + 4))) << (5);
    a2 = (a2) + (result + 32 + 8);
    goto loc_00AD0EBF;
loc_00AD0EA8:
    *(unsigned __int8 *)(result + 32 + 8 + 3) = 0;
    a1 = 0 + 1;
    if ((*(unsigned __int8 *)(result + 32 + 8 + 1)) != 0) { a1 = 0; }
    a3 = (result + 32 + 8) + (32);
loc_00AD0EBF:
    if (a3 < a2) goto loc_00AD0EA8;
    a4 = (unsigned int)((a4) - (1));
    if (!sign_flag) goto loc_00AD0E98;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_00AD0ECD:
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 28)));
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 28)) - 1);
    if (sign_flag) goto loc_00AD1350;
loc_00AD0EE7:
    *(unsigned int *)(v_rsp - 95 - 93) = (unsigned int)(*(unsigned __int16 *)(result + 32));
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 32))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        *(unsigned int *)(v_rsp - 95 - 93) = 1;
    }
    *(unsigned __int16 *)(result + 32) = 0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 4))))) << (5);
    a3 = (a3) + (result + 32 + 8);
    *(unsigned __int64 *)(v_rsp - 95 + 15) = (unsigned int)(*(unsigned int *)(result + 32 + 4));
    *(unsigned __int64 *)(v_rsp - 95 - 41) = a3;
    if ((result + 32 + 8) != a3) goto loc_00AD0F26;
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)((unsigned int)(0xFFFFULL));
    goto loc_00AD1341;
loc_00AD0F26:
    *(unsigned __int64 *)(v_rsp - 95 + 103) = a2 + 4;
    *(unsigned int *)(v_rsp - 95 - 117) = 1;
    *(unsigned int *)(v_rsp - 95 - 81) = 0;
    if ((*(unsigned int *)(a2)) <= 0) goto loc_00AD123B;
    *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(v_r15);
loc_00AD0F46:
    *(unsigned __int64 *)(v_rsp - 95 - 105) = a2 + 4 + 16;
    if ((*(unsigned int *)(a2 + 4 + 12)) <= 0) goto loc_00AD1211;
loc_00AD0F5E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a2 + 4 + 16)))) - (5));
    if (condition_is_equal) goto loc_00AD12FE;
    if (((unsigned int)(a2)) == 124) goto loc_00AD11E8;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a2 + 4 + 16)) - (1));
    if (((unsigned __int8)(a1)) > 6) goto loc_00AD11E8;
    *(unsigned int *)(v_rsp - 95 - 97) = 0;
loc_00AD0F85:
loc_00AD0F88:
    if ((result + 32 + 8) >= a3) goto loc_00AD11CF;
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(*(unsigned __int8 *)(a2 + 4 + 16));
    if ((*(unsigned __int8 *)(result + 32 + 8 + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 4 + 16)))) goto loc_00AD111F;
    if ((*(unsigned __int8 *)(result + 32 + 8 + 3)) != 0) goto loc_00AD111F;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 4 + 16 + 1))) - (1));
    *(unsigned __int64 *)(v_rsp - 95 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 113) = 1;
    v_r11 = (unsigned int)((unsigned int)(*(unsigned __int8 *)(a2 + 4 + 16 + 1)));
    if (((unsigned __int8)(a1)) > 2) { v_r11 = (unsigned int)(*(unsigned __int8 *)(result + 32 + 8 + 2)); }
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 1;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32 + 8 + 2))) - (1));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(v_r11);
    a2 = *(unsigned __int8 *)(result + 32 + 8 + 2);
    if (((unsigned __int8)(a1)) > 2) { a2 = (unsigned int)((unsigned __int8)(v_r11)); }
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)(a2);
    a1 = (unsigned int)((*(unsigned __int8 *)(v_rsp - 95 - 85)) - (1));
    if (condition_is_equal) goto loc_00AD105F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD1046;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD105F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD103A;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AD1019;
    if (((unsigned int)(a1)) == 1) goto loc_00AD105F;
    goto loc_00AD1059;
loc_00AD1019:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 105) + 4)) - 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 105) + 8)))));
    goto loc_00AD10A8;
loc_00AD103A:
    goto loc_00AD1051;
loc_00AD1046:
loc_00AD1051:
loc_00AD1059:
    goto loc_00AD10AC;
loc_00AD105F:
    result = RtlCmDecodeMemIoResource(*(unsigned __int64 *)(v_rsp - 95 - 105), v_rsp - 95 - 65, (unsigned int)(*(unsigned int *)(result + 32 + 8 + 12)), (unsigned int)(*(unsigned int *)(result + 32 + 8 + 8)));
    *(unsigned __int64 *)(v_rsp - 95 - 1) = result;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 65) - 1) + (result);
    *(unsigned __int64 *)(v_rsp - 95 - 65) = a1;
    result = RtlIoDecodeMemIoResource(result + 32 + 8, v_rsp - 95 - 17, v_rsp - 95 - 33, v_rsp - 95 - 25);
loc_00AD10A8:
    *(unsigned __int64 *)(v_rsp - 95 - 113) = result;
loc_00AD10AC:
    if ((*(unsigned int *)(v_rsp - 95 - 97)) != 0) goto loc_00AD10F3;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))) != (*(unsigned __int8 *)(v_rsp - 95 - 89))) goto loc_00AD1117;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 33)) != (*(unsigned __int64 *)(v_rsp - 95 - 65))) goto loc_00AD1117;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25)) < (*(unsigned __int64 *)(v_rsp - 95 - 65))) goto loc_00AD1117;
    if (result < (*(unsigned __int64 *)(v_rsp - 95 - 1))) goto loc_00AD1117;
    v_r10 = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 117));
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25)) != (*(unsigned __int64 *)(v_rsp - 95 - 65))) { v_r10 = 0; }
    *(unsigned int *)(v_rsp - 95 - 117) = (unsigned int)(v_r10);
    *(unsigned __int8 *)(result + 32 + 8 + 3) = 128;
    if (((*(unsigned __int8 *)(result + 32 + 8)) & (8)) == 0) goto loc_00AD1289;
    goto loc_00AD1284;
loc_00AD10F3:
    *(unsigned int *)(v_rsp - 95 - 117) = 0;
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))) != (*(unsigned __int8 *)(v_rsp - 95 - 89))) goto loc_00AD1117;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 33)) > (*(unsigned __int64 *)(v_rsp - 95 - 65))) goto loc_00AD1117;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25)) < (*(unsigned __int64 *)(v_rsp - 95 - 65))) goto loc_00AD1117;
    if ((result + 32 + 8 - 32) < v_r10) goto loc_00AD1117;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 17)) - 1;
    if (((*(unsigned __int64 *)(v_rsp - 95 - 65)) & (result)) == 0) goto loc_00AD112C;
loc_00AD1117:
loc_00AD111F:
    v_rdi = (result + 32 + 8) + (32);
    goto loc_00AD0F88;
loc_00AD112C:
    a1 = (unsigned int)((*(unsigned __int8 *)(v_rsp - 95 - 85)) - (1));
    if (condition_is_equal) goto loc_00AD1149;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD1191;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD1149;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD1191;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AD117F;
    result = 32;
    if (((unsigned int)(a1)) == 1) {
        result = *(unsigned __int64 *)(v_rsp - 95 - 113);
        result = (result) - 1;
        *(unsigned __int64 *)(v_rdi + 16) = *(unsigned __int64 *)(v_rsp - 95 - 65);
        result = (result) + (*(unsigned __int64 *)(v_rsp - 95 - 65));
        *(unsigned __int64 *)(v_rdi + 24) = result;
    }
    *(unsigned __int8 *)(v_rdi + 3) = 128;
    *(unsigned __int16 *)(v_rdi + 4) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 105) + 2));
    if (((*(unsigned __int8 *)(v_rdi)) & (8)) == 0) goto loc_00AD11AF;
    goto loc_00AD11AA;
loc_00AD117F:
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 113)) - 1);
    *(unsigned int *)(v_rdi + 12) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 65));
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 65))));
    *(unsigned int *)(v_rdi + 16) = (unsigned int)(result);
    goto loc_00AD115B;
loc_00AD1191:
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 65));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 65));
    goto loc_00AD115B;
loc_00AD119A:
    *(unsigned __int8 *)(result + 1) = 0;
    if ((*(unsigned __int8 *)(result)) != 8) goto loc_00AD11AF;
    result = (result) - (32);
loc_00AD11AA:
    if (result >= (result + 32 + 8)) goto loc_00AD119A;
loc_00AD11AF:
    *(unsigned __int8 *)(v_rdi) = 1;
    goto loc_00AD11C4;
loc_00AD11B8:
    if (((*(unsigned __int8 *)(v_rdi)) & (8)) == 0) goto loc_00AD11D3;
    *(unsigned __int8 *)(v_rdi + 1) = 0;
loc_00AD11C4:
    v_rdi = (v_rdi) + (32);
    if (v_rdi < (*(unsigned __int64 *)(v_rsp - 95 - 41))) goto loc_00AD11B8;
    goto loc_00AD11D3;
loc_00AD11CF:
loc_00AD11D3:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97))) + (1));
    *(unsigned int *)(v_rsp - 95 - 97) = (unsigned int)(result);
    if (((unsigned int)(result)) < 2) goto loc_00AD0F85;
loc_00AD11E8:
loc_00AD11EA:
    v_r11 = (*(unsigned __int64 *)(v_rsp - 95 - 105)) + (20);
    v_r11 = (v_r11) + (0);
    v_r15 = (unsigned int)((0) + (1));
    *(unsigned __int64 *)(v_rsp - 95 - 105) = v_r11;
    if (((unsigned int)(v_r15)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 12))) goto loc_00AD0F5E;
loc_00AD1211:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 81))) + (1));
    *(unsigned __int64 *)(v_rsp - 95 + 103) = v_r11;
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)(a1);
    if (((unsigned int)(a1)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111)))) goto loc_00AD0F46;
loc_00AD123B:
    if ((*(unsigned __int16 *)(result + 32)) != ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53))))) goto loc_00AD130D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53))))) goto loc_00AD1307;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 4)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 53)) + 1))) goto loc_00AD1265;
    if ((*(unsigned __int8 *)(result + 32 + 9)) == 128) goto loc_00AD1307;
loc_00AD1265:
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)));
    goto loc_00AD1335;
loc_00AD1274:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)) + 1) = 0;
    if ((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)))) != 8) goto loc_00AD1289;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93))) - (32);
loc_00AD1284:
    if (result >= ((unsigned int)(*(unsigned int *)(result + 32 + 4)))) goto loc_00AD1274;
loc_00AD1289:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4) = 1;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 4) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 105) + 2));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 1))) - (1));
    if ((((unsigned __int8)(result)) & (249)) != 0) goto loc_00AD12C1;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 1))) == 5) goto loc_00AD12C1;
    result = (*(unsigned __int64 *)(v_rsp - 95 - 113)) - 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 16) = *(unsigned __int64 *)(v_rsp - 95 + 111);
    result = (result) + (*(unsigned __int64 *)(v_rsp - 95 + 111));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 12) = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 24) = result;
    goto loc_00AD12D6;
loc_00AD12C1:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 1))) == 6) {
        result = *(unsigned __int64 *)(v_rsp - 95 - 113);
        result = (unsigned int)((result) - 1);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 12) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 111));
        result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 111))));
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4 + 16) = (unsigned int)(result);
    }
    v_rdi = (*(unsigned __int64 *)(v_rsp - 95 + 111) + 4) + (32);
    goto loc_00AD12F4;
loc_00AD12E0:
    if (((*(unsigned __int8 *)(v_rdi)) & (8)) == 0) goto loc_00AD11E8;
    *(unsigned __int8 *)(v_rdi + 1) = 0;
    v_rdi = (v_rdi) + (32);
loc_00AD12F4:
    if (v_rdi < (*(unsigned __int64 *)(v_rsp - 95 - 41))) goto loc_00AD12E0;
    goto loc_00AD11E8;
loc_00AD12FE:
    goto loc_00AD11EA;
loc_00AD1307:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 9)) == 0) goto loc_00AD131C;
loc_00AD130D:
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)((unsigned int)(0xFFFFULL));
    goto loc_00AD133A;
loc_00AD131C:
    *(unsigned __int64 *)(v_rsp - 95 - 9) = result + 32;
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 93)));
    result = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 93));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 117))) != 0) {
        result = *(unsigned __int64 *)(v_rsp - 95 + 127);
        *(unsigned int *)(result) = 1;
    }
loc_00AD133A:
    *(unsigned int *)(result + 32 + 4) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 105));
loc_00AD1341:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 77))) - (1));
    *(unsigned int *)(v_rsp - 95 - 77) = (unsigned int)(a2);
    if (!sign_flag) goto loc_00AD0EE7;
loc_00AD1350:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 28))) != 0) goto loc_00AD136C;
    result = PnpCmResourcesToIoResources((unsigned int)(0xFFFFULL), *(unsigned __int64 *)(v_rsp - 95 + 111), 1, result + 32 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 119)) = result;
    goto loc_00AD13A2;
loc_00AD136C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 121))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))));
    a1 = (unsigned int)((a1) << (5));
    result = (unsigned int)((result) - 1);
    a2 = (unsigned int)((result * 4 + 9) + ((unsigned int)(result)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 + a2 * 8)), (unsigned int)(0x36706E50ULL), result + 32 + 8);
    if (result != 0) goto loc_00AD13B3;
loc_00AD13A2:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 + 7), a2, (unsigned int)(0x36706E50ULL), result + 32 + 8);
    goto loc_00AD14C1;
loc_00AD13B3:
    *(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) = (unsigned int)(a1 + a2 * 8);
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 4)));
    *(unsigned int *)(a2 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 8)));
    *(unsigned int *)(a2 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 12)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 28)))) >= = 1) {
        a1 = *(unsigned __int64 *)(v_rsp - 95 + 127);
        *(unsigned int *)(a1) = (unsigned int)((unsigned int)(0xC000009AULL));
    }
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49))) - (1));
    *(unsigned int *)(a2 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 28)));
    if (sign_flag) goto loc_00AD1490;
loc_00AD13F6:
    a4 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 4))) << (5);
    a4 = (a4) + (*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 8);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_00AD1485;
    *(unsigned __int16 *)(a2 + 32) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32));
    *(unsigned __int16 *)(a2 + 32 + 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 2));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 9)) == 128) goto loc_00AD1444;
    *(unsigned __int16 *)(a2 + 32 + 8) = 0x8001ULL;
    *(unsigned int *)(a2 + 32 + 8 + 2) = 3;
    *(unsigned __int16 *)(a2 + 32 + 8 + 6) = (unsigned __int16)((unsigned int)(0xC000009AULL));
    *(unsigned int *)(a2 + 32 + 8 + 8) = 1;
    a1 = (a2 + 32 + 8) + (32);
    goto loc_00AD1467;
loc_00AD1444:
    goto loc_00AD1467;
loc_00AD1449:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 8 + 1)) != ((unsigned __int8)((unsigned int)(0xC000009AULL)))) {
        *(unsigned __int64 *)(a1) = v_xmm0;
        *(unsigned __int64 *)(a1 + 16) = v_xmm1;
        a1 = (a1) + (32);
    }
    a3 = (*(unsigned __int64 *)(v_rsp - 95 + 7) + 32 + 8) + (32);
loc_00AD1467:
    if (a3 < a4) goto loc_00AD1449;
    result = (a1) - (a2 + 32);
    result = (result) - (8);
    result = (result) >> (5);
    *(unsigned int *)(a2 + 32 + 4) = (unsigned int)(result);
    *(unsigned int *)(a2 + 32 + 8 + 8) = 1;
loc_00AD1485:
    v_rdi = (unsigned int)((v_rdi) - (1));
    if (!sign_flag) goto loc_00AD13F6;
loc_00AD1490:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 119)) = 0;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 + 7), a2, a3, a4);
    goto loc_00AD14BF;
loc_00AD14A3:
    *(unsigned __int64 *)((unsigned int)(0xFFFFULL)) = *(unsigned __int64 *)(v_rsp - 95 + 7);
    goto loc_00AD14BF;
loc_00AD14A8:
    if (*(unsigned __int64 *)(v_rsp - 95 + 111) == 0) goto loc_00AD14BF;
    if ((*(unsigned int *)(a2)) != ((unsigned int)((unsigned int)(0xC000009AULL)))) {
        a3 = 1;
        result = PnpCmResourcesToIoResources(*(unsigned __int64 *)(v_rsp - 95 + 7), a2, a3, a4);
        *(unsigned __int64 *)((unsigned int)(0xFFFFULL)) = result;
    }
    result = 0;
loc_00AD14C1:
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpFilterResourceRequirementsList(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (184);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x79) = 0;
    *(uint64_t *)(arg3) = 0;
    *(uint32_t *)(arg4) = 0;
    if (Arg1 == NULL) goto loc_00AD14A8;
    if ((*(uint32_t *)(arg1 + 0x1C)) == 0) goto loc_00AD14A8;
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(arg1)), (uint32_t)(0x36706E50ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
    if (result != 0) goto loc_00AD0DF7;
    goto loc_00AD14C1;
loc_00AD0DF7:
    result = memcpy(result, Arg1, (uint32_t)(*(uint32_t *)(arg1)), Arg4);
    if (Arg2 == NULL) goto loc_00AD14A3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))) == 0) goto loc_00AD14A3;
loc_00AD0E2A:
    Arg1 = (Arg2 + 4) + (16);
    local_r15 = (uint32_t)((0) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4 + 0xC)))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4 + 0xC))) == 0) goto loc_00AD0E74;
loc_00AD0E3B:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1)))) - (5));
    if (condition_is_equal) goto loc_00AD0E5E;
    Arg2 = (uint32_t)((Arg2) - (123));
    if (condition_is_equal) goto loc_00AD0E62;
    if (((uint32_t)(Arg2)) == 1) goto loc_00AD0E62;
    Arg3 = (uint8_t)((*(uint8_t *)(arg1)) - (1));
    if (((uint8_t)(Arg3)) > 6) goto loc_00AD0E62;
    goto loc_00AD0E65;
loc_00AD0E5E:
loc_00AD0E62:
    local_r15 = (uint32_t)((local_r15) - 1);
loc_00AD0E65:
    Arg1 = (Arg1) + (20);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4 + 0xC))))) - (1);
    if (condition_is_not_equal) goto loc_00AD0E3B;
loc_00AD0E74:
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) - (1);
    if (condition_is_not_equal) goto loc_00AD0E2A;
    if ((uint32_t)(local_r15) == 0) goto loc_00AD14A3;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x1C))) - (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    if (sign_flag) goto loc_00AD0ECD;
loc_00AD0E98:
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4))) << (5);
    Arg2 = (Arg2) + (result + 32 + 8);
    goto loc_00AD0EBF;
loc_00AD0EA8:
    *(uint8_t *)(result + 0x20 + 0x8 + 0x3) = 0;
    Arg1 = 0 + 1;
    if ((*(uint8_t *)(result + 0x20 + 0x8 + 0x1)) != 0) { Arg1 = 0; }
    Arg3 = (result + 32 + 8) + (32);
loc_00AD0EBF:
    if (Arg3 < Arg2) goto loc_00AD0EA8;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (!sign_flag) goto loc_00AD0E98;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_00AD0ECD:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)));
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)) - 1);
    if (sign_flag) goto loc_00AD1350;
loc_00AD0EE7:
    *(uint32_t *)(local_rsp - 0x5F - 0x5D) = (uint32_t)(*(uint16_t *)(result + 0x20));
    if (((uint16_t)(*(uint16_t *)(result + 0x20))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        *(uint32_t *)(local_rsp - 0x5F - 0x5D) = 1;
    }
    *(uint16_t *)(result + 0x20) = 0;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4))))) << (5);
    Arg3 = (Arg3) + (result + 32 + 8);
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)(*(uint32_t *)(result + 0x20 + 0x4));
    *(void **)(local_rsp - 0x5F - 0x29) = Arg3;
    if ((result + 32 + 8) != Arg3) goto loc_00AD0F26;
    *(uint16_t *)(result + 0x20) = (uint16_t)((uint32_t)(0xFFFFULL));
    goto loc_00AD1341;
loc_00AD0F26:
    *(void **)(local_rsp - 0x5F + 0x67) = Arg2 + 4;
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 1;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 0;
    if ((*(uint32_t *)(arg2)) <= 0) goto loc_00AD123B;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(local_r15);
loc_00AD0F46:
    *(void **)(local_rsp - 0x5F - 0x69) = Arg2 + 4 + 16;
    if ((*(uint32_t *)(arg2 + 0x4 + 0xC)) <= 0) goto loc_00AD1211;
loc_00AD0F5E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg2 + 0x4 + 0x10)))) - (5));
    if (condition_is_equal) goto loc_00AD12FE;
    if (((uint32_t)(Arg2)) == 124) goto loc_00AD11E8;
    Arg1 = (uint8_t)((*(uint8_t *)(arg2 + 0x4 + 0x10)) - (1));
    if (((uint8_t)(Arg1)) > 6) goto loc_00AD11E8;
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = 0;
loc_00AD0F85:
loc_00AD0F88:
    if ((result + 32 + 8) >= Arg3) goto loc_00AD11CF;
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(*(uint8_t *)(arg2 + 0x4 + 0x10));
    if ((*(uint8_t *)(result + 0x20 + 0x8 + 0x1)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x4 + 0x10)))) goto loc_00AD111F;
    if ((*(uint8_t *)(result + 0x20 + 0x8 + 0x3)) != 0) goto loc_00AD111F;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x4 + 0x10 + 0x1))) - (1));
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = 1;
    local_r11 = (uint32_t)((uint32_t)(*(uint8_t *)(arg2 + 0x4 + 0x10 + 0x1)));
    if (((uint8_t)(Arg1)) > 2) { local_r11 = (uint32_t)(*(uint8_t *)(result + 0x20 + 0x8 + 0x2)); }
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 1;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20 + 0x8 + 0x2))) - (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(local_r11);
    Arg2 = *(uint8_t *)(result + 0x20 + 0x8 + 0x2);
    if (((uint8_t)(Arg1)) > 2) { Arg2 = (uint32_t)((uint8_t)(local_r11)); }
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)(Arg2);
    Arg1 = (uint32_t)((*(uint8_t *)(local_rsp - 0x5F - 0x55)) - (1));
    if (condition_is_equal) goto loc_00AD105F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD1046;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD105F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD103A;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AD1019;
    if (((uint32_t)(Arg1)) == 1) goto loc_00AD105F;
    goto loc_00AD1059;
loc_00AD1019:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x69) + 0x4)) - 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x69) + 0x8)))));
    goto loc_00AD10A8;
loc_00AD103A:
    goto loc_00AD1051;
loc_00AD1046:
loc_00AD1051:
loc_00AD1059:
    goto loc_00AD10AC;
loc_00AD105F:
    result = RtlCmDecodeMemIoResource(*(uint64_t *)(local_rsp - 0x5F - 0x69), local_rsp - 95 - 65, (uint32_t)(*(uint32_t *)(result + 0x20 + 0x8 + 0xC)), (uint32_t)(*(uint32_t *)(result + 0x20 + 0x8 + 0x8)));
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = result;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F - 0x41) - 1) + (result);
    *(void **)(local_rsp - 0x5F - 0x41) = Arg1;
    result = RtlIoDecodeMemIoResource(result + 32 + 8, local_rsp - 95 - 17, local_rsp - 95 - 33, local_rsp - 95 - 25);
loc_00AD10A8:
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = result;
loc_00AD10AC:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x61)) != 0) goto loc_00AD10F3;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))) != (*(uint8_t *)(local_rsp - 0x5F - 0x59))) goto loc_00AD1117;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x21)) != (*(uint64_t *)(local_rsp - 0x5F - 0x41))) goto loc_00AD1117;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19)) < (*(uint64_t *)(local_rsp - 0x5F - 0x41))) goto loc_00AD1117;
    if (result < (*(uint64_t *)(local_rsp - 0x5F - 0x1))) goto loc_00AD1117;
    local_r10 = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75));
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19)) != (*(uint64_t *)(local_rsp - 0x5F - 0x41))) { local_r10 = 0; }
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = (uint32_t)(local_r10);
    *(uint8_t *)(result + 0x20 + 0x8 + 0x3) = 128;
    if (((*(uint8_t *)(result + 0x20 + 0x8)) & (8)) == 0) goto loc_00AD1289;
    goto loc_00AD1284;
loc_00AD10F3:
    *(uint32_t *)(local_rsp - 0x5F - 0x75) = 0;
    if (((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))) != (*(uint8_t *)(local_rsp - 0x5F - 0x59))) goto loc_00AD1117;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x21)) > (*(uint64_t *)(local_rsp - 0x5F - 0x41))) goto loc_00AD1117;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19)) < (*(uint64_t *)(local_rsp - 0x5F - 0x41))) goto loc_00AD1117;
    if ((result + 32 + 8 - 32) < local_r10) goto loc_00AD1117;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x11)) - 1;
    if (((*(uint64_t *)(local_rsp - 0x5F - 0x41)) & (result)) == 0) goto loc_00AD112C;
loc_00AD1117:
loc_00AD111F:
    local_rdi = (result + 32 + 8) + (32);
    goto loc_00AD0F88;
loc_00AD112C:
    Arg1 = (uint32_t)((*(uint8_t *)(local_rsp - 0x5F - 0x55)) - (1));
    if (condition_is_equal) goto loc_00AD1149;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD1191;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD1149;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD1191;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AD117F;
    result = 32;
    if (((uint32_t)(Arg1)) == 1) {
        result = *(uint64_t *)(local_rsp - 0x5F - 0x71);
        result = (result) - 1;
        *(uint64_t *)(local_rdi + 0x10) = *(uint64_t *)(local_rsp - 0x5F - 0x41);
        result = (result) + (*(uint64_t *)(local_rsp - 0x5F - 0x41));
        *(uint64_t *)(local_rdi + 0x18) = result;
    }
    *(uint8_t *)(local_rdi + 0x3) = 128;
    *(uint16_t *)(local_rdi + 0x4) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x69) + 0x2));
    if (((*(uint8_t *)(local_rdi)) & (8)) == 0) goto loc_00AD11AF;
    goto loc_00AD11AA;
loc_00AD117F:
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x71)) - 1);
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x41));
    result = (uint32_t)((result) + ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x41))));
    *(uint32_t *)(local_rdi + 0x10) = (uint32_t)(result);
    goto loc_00AD115B;
loc_00AD1191:
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x41));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x41));
    goto loc_00AD115B;
loc_00AD119A:
    *(uint8_t *)(result + 0x1) = 0;
    if ((*(uint8_t *)(result)) != 8) goto loc_00AD11AF;
    result = (result) - (32);
loc_00AD11AA:
    if (result >= (result + 32 + 8)) goto loc_00AD119A;
loc_00AD11AF:
    *(uint8_t *)(local_rdi) = 1;
    goto loc_00AD11C4;
loc_00AD11B8:
    if (((*(uint8_t *)(local_rdi)) & (8)) == 0) goto loc_00AD11D3;
    *(uint8_t *)(local_rdi + 0x1) = 0;
loc_00AD11C4:
    local_rdi = (local_rdi) + (32);
    if (local_rdi < (*(uint64_t *)(local_rsp - 0x5F - 0x29))) goto loc_00AD11B8;
    goto loc_00AD11D3;
loc_00AD11CF:
loc_00AD11D3:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61))) + (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = (uint32_t)(result);
    if (((uint32_t)(result)) < 2) goto loc_00AD0F85;
loc_00AD11E8:
loc_00AD11EA:
    local_r11 = (*(uint64_t *)(local_rsp - 0x5F - 0x69)) + (20);
    local_r11 = (local_r11) + (0);
    local_r15 = (uint32_t)((0) + (1));
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = local_r11;
    if (((uint32_t)(local_r15)) < (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0xC))) goto loc_00AD0F5E;
loc_00AD1211:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x51))) + (1));
    *(uint64_t *)(local_rsp - 0x5F + 0x67) = local_r11;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F)))) goto loc_00AD0F46;
loc_00AD123B:
    if ((*(uint16_t *)(result + 0x20)) != ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35))))) goto loc_00AD130D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35))))) goto loc_00AD1307;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x35)) + 1))) goto loc_00AD1265;
    if ((*(uint8_t *)(result + 0x20 + 0x9)) == 128) goto loc_00AD1307;
loc_00AD1265:
    *(uint16_t *)(result + 0x20) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)));
    goto loc_00AD1335;
loc_00AD1274:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)) + 0x1) = 0;
    if ((*(uint8_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)))) != 8) goto loc_00AD1289;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D))) - (32);
loc_00AD1284:
    if (result >= ((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4)))) goto loc_00AD1274;
loc_00AD1289:
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4) = 1;
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x4) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x69) + 0x2));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x1))) - (1));
    if ((((uint8_t)(result)) & (249)) != 0) goto loc_00AD12C1;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x1))) == 5) goto loc_00AD12C1;
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x71)) - 1;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x10) = *(uint64_t *)(local_rsp - 0x5F + 0x6F);
    result = (result) + (*(uint64_t *)(local_rsp - 0x5F + 0x6F));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0xC) = 1;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x18) = result;
    goto loc_00AD12D6;
loc_00AD12C1:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x1))) == 6) {
        result = *(uint64_t *)(local_rsp - 0x5F - 0x71);
        result = (uint32_t)((result) - 1);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0xC) = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x6F));
        result = (uint32_t)((result) + ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x6F))));
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4 + 0x10) = (uint32_t)(result);
    }
    local_rdi = (*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 4) + (32);
    goto loc_00AD12F4;
loc_00AD12E0:
    if (((*(uint8_t *)(local_rdi)) & (8)) == 0) goto loc_00AD11E8;
    *(uint8_t *)(local_rdi + 0x1) = 0;
    local_rdi = (local_rdi) + (32);
loc_00AD12F4:
    if (local_rdi < (*(uint64_t *)(local_rsp - 0x5F - 0x29))) goto loc_00AD12E0;
    goto loc_00AD11E8;
loc_00AD12FE:
    goto loc_00AD11EA;
loc_00AD1307:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x9)) == 0) goto loc_00AD131C;
loc_00AD130D:
    *(uint16_t *)(result + 0x20) = (uint16_t)((uint32_t)(0xFFFFULL));
    goto loc_00AD133A;
loc_00AD131C:
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = result + 32;
    *(uint16_t *)(result + 0x20) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D)));
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x5D));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x75))) != 0) {
        result = *(uint64_t *)(local_rsp - 0x5F + 0x7F);
        *(uint32_t *)(result) = 1;
    }
loc_00AD133A:
    *(uint32_t *)(result + 0x20 + 0x4) = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x69));
loc_00AD1341:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x4D))) - (1));
    *(uint32_t *)(local_rsp - 0x5F - 0x4D) = (uint32_t)(Arg2);
    if (!sign_flag) goto loc_00AD0EE7;
loc_00AD1350:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x1C))) != 0) goto loc_00AD136C;
    result = PnpCmResourcesToIoResources((uint32_t)(0xFFFFULL), *(uint64_t *)(local_rsp - 0x5F + 0x6F), 1, result + 32 + 8);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)) = result;
    goto loc_00AD13A2;
loc_00AD136C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x79))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))));
    Arg1 = (uint32_t)((Arg1) << (5));
    result = (uint32_t)((result) - 1);
    Arg2 = (uint32_t)((result * 4 + 9) + ((uint32_t)(result)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 + Arg2 * 8)), (uint32_t)(0x36706E50ULL), result + 32 + 8);
    if (result != 0) goto loc_00AD13B3;
loc_00AD13A2:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F + 0x7), Arg2, (uint32_t)(0x36706E50ULL), result + 32 + 8);
    goto loc_00AD14C1;
loc_00AD13B3:
    *(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) = (uint32_t)(Arg1 + Arg2 * 8);
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x4)));
    *(uint32_t *)(arg2 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x8)));
    *(uint32_t *)(arg2 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0xC)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x1C)))) >= = 1) {
        Arg1 = *(uint64_t *)(local_rsp - 0x5F + 0x7F);
        *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(0xC000009AULL));
    }
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31))) - (1));
    *(uint32_t *)(arg2 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x1C)));
    if (sign_flag) goto loc_00AD1490;
loc_00AD13F6:
    Arg4 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20 + 0x4))) << (5);
    Arg4 = (Arg4) + (*(uint64_t *)(local_rsp - 0x5F + 0x7) + 32 + 8);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_00AD1485;
    *(uint16_t *)(arg2 + 0x20) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20));
    *(uint16_t *)(arg2 + 0x20 + 0x2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20 + 0x2));
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20 + 0x9)) == 128) goto loc_00AD1444;
    *(uint16_t *)(arg2 + 0x20 + 0x8) = 0x8001ULL;
    *(uint32_t *)(arg2 + 0x20 + 0x8 + 0x2) = 3;
    *(uint16_t *)(arg2 + 0x20 + 0x8 + 0x6) = (uint16_t)((uint32_t)(0xC000009AULL));
    *(uint32_t *)(arg2 + 0x20 + 0x8 + 0x8) = 1;
    Arg1 = (Arg2 + 32 + 8) + (32);
    goto loc_00AD1467;
loc_00AD1444:
    goto loc_00AD1467;
loc_00AD1449:
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7) + 0x20 + 0x8 + 0x1)) != ((uint8_t)((uint32_t)(0xC000009AULL)))) {
        *(uint64_t *)(arg1) = v_xmm0;
        *(uint64_t *)(arg1 + 0x10) = v_xmm1;
        Arg1 = (Arg1) + (32);
    }
    Arg3 = (*(uint64_t *)(local_rsp - 0x5F + 0x7) + 32 + 8) + (32);
loc_00AD1467:
    if (Arg3 < Arg4) goto loc_00AD1449;
    result = (Arg1) - (Arg2 + 32);
    result = (result) - (8);
    result = (result) >> (5);
    *(uint32_t *)(arg2 + 0x20 + 0x4) = (uint32_t)(result);
    *(uint32_t *)(arg2 + 0x20 + 0x8 + 0x8) = 1;
loc_00AD1485:
    local_rdi = (uint32_t)((local_rdi) - (1));
    if (!sign_flag) goto loc_00AD13F6;
loc_00AD1490:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)) = 0;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F + 0x7), Arg2, Arg3, Arg4);
    goto loc_00AD14BF;
loc_00AD14A3:
    *(uint64_t *)((uint32_t)(0xFFFFULL)) = *(uint64_t *)(local_rsp - 0x5F + 0x7);
    goto loc_00AD14BF;
loc_00AD14A8:
    if (*(uint64_t *)(local_rsp - 0x5F + 0x6F) == 0) goto loc_00AD14BF;
    if ((*(uint32_t *)(arg2)) != ((uint32_t)((uint32_t)(0xC000009AULL)))) {
        Arg3 = 1;
        result = PnpCmResourcesToIoResources(*(uint64_t *)(local_rsp - 0x5F + 0x7), Arg2, Arg3, Arg4);
        *(uint64_t *)((uint32_t)(0xFFFFULL)) = result;
    }
    result = 0;
loc_00AD14C1:
    local_rsp = (local_rsp) + (184);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD0D7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
