# HalGetAdapterV2

- RVA: `0x00709DD8`–`0x0070A1FA` (길이 `1,058` bytes)
- VA: `0x0000000140709DD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD64C`
- 디코드: `284`개 명령, `1,058/1,058` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00709E40` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00709EAC` → [HalpGetCacheCoherency](HalpGetCacheCoherency_function_00706FA0.md) (function, `0x00706FA0`)
- `0x00709F8D` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x00709FD9` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x00709FFA` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0070A034` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0070A04E` → [HalpDmaFindAdapterByDeviceObject](../../text/53/HalpDmaFindAdapterByDeviceObject_function_0053FC8C.md) (function, `0x0053FC8C`)
- `0x0070A05E` → [HalpDmaGetAdapterVersion](../../text/3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (function, `0x003DEC8C`)
- `0x0070A06C` → [HalpDmaIsAutomaticDomain](../../text/55/HalpDmaIsAutomaticDomain_function_0055253C.md) (function, `0x0055253C`)
- `0x0070A077` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0070A0C0` → [HalpDmaAllocateChildAdapterV2](HalpDmaAllocateChildAdapterV2_function_0070A200.md) (function, `0x0070A200`)
- `0x0070A0F6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0070A11D` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0070A175` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0070A1C2` → [HalpAddAdapterToList](../../text/53/HalpAddAdapterToList_function_0053FBD0.md) (function, `0x0053FBD0`)
- `0x0070A1E1` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [HalpGetAdapter](HalpGetAdapter_function_00706EBC.md) at `0x00706F1D`

### Static image references
- `0x00709E2A` → RVA `0x00FC3E58` (`.data`; read)
- `0x00709EDD` → RVA `0x00FC3C08` (`.data`; read)
- `0x00709F4E` → RVA `0x00FC3BE8` (`.data`; read)
- `0x00709F58` → RVA `0x00FC3AE8` (`.data`; read)
- `0x00709FA9` → RVA `0x00E103F0` (`.data`; read)
- `0x00709FC7` → RVA `0x00FC6D38` (`ALMOSTRO`; read)
- `0x00709FE9` → RVA `0x00FC1760` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00709E40` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00709F8D` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x00709FD9` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x00709FFA` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0070A034` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0070A04E` → [HalpDmaFindAdapterByDeviceObject](../../text/53/HalpDmaFindAdapterByDeviceObject_function_0053FC8C.md) (`PAGE` → `.text`)
  - `0x0070A05E` → [HalpDmaGetAdapterVersion](../../text/3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (`PAGE` → `.text`)
  - `0x0070A06C` → [HalpDmaIsAutomaticDomain](../../text/55/HalpDmaIsAutomaticDomain_function_0055253C.md) (`PAGE` → `.text`)
  - `0x0070A077` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0070A0F6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0070A11D` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0070A175` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x0070A1C2` → [HalpAddAdapterToList](../../text/53/HalpAddAdapterToList_function_0053FBD0.md) (`PAGE` → `.text`)
  - `0x0070A1E1` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00709DD8  48 8B C4                        mov rax, rsp
00709DDB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00709DDF  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00709DE3  53                              push rbx
00709DE4  55                              push rbp
00709DE5  56                              push rsi
00709DE6  57                              push rdi
00709DE7  41 54                           push r12
00709DE9  41 55                           push r13
00709DEB  41 56                           push r14
00709DED  41 57                           push r15
00709DEF  48 83 EC 58                     sub rsp, 0x58
00709DF3  45 33 E4                        xor r12d, r12d
00709DF6  48 8B F9                        mov rdi, rcx
00709DF9  83 39 02                        cmp dword ptr [rcx], 2
00709DFC  44 88 60 20                     mov byte ptr [rax + 0x20], r12b
00709E00  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00709E05  0F 87 DB 03 00 00               ja 0x14070a1e6
00709E0B  44 38 61 04                     cmp byte ptr [rcx + 4], r12b
00709E0F  74 19                           je 0x140709e2a
00709E11  83 79 14 01                     cmp dword ptr [rcx + 0x14], 1
00709E15  75 06                           jne 0x140709e1d
00709E17  83 79 10 07                     cmp dword ptr [rcx + 0x10], 7
00709E1B  76 0D                           jbe 0x140709e2a
00709E1D  45 8A FC                        mov r15b, r12b
00709E20  44 88 A4 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r12b
00709E28  EB 2B                           jmp 0x140709e55
00709E2A  48 8B 05 27 A0 8B 00            mov rax, qword ptr [rip + 0x8ba027]
00709E31  41 B7 01                        mov r15b, 1
00709E34  44 88 BC 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r15b
00709E3C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00709E40  E8 8B 0C FB FF                  call 0x1406baad0
00709E45  84 C0                           test al, al
00709E47  0F 84 99 03 00 00               je 0x14070a1e6
00709E4D  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00709E55  44 8B 6F 20                     mov r13d, dword ptr [rdi + 0x20]
00709E59  8A 47 04                        mov al, byte ptr [rdi + 4]
00709E5C  41 0F BA F5 1F                  btr r13d, 0x1f
00709E61  84 C0                           test al, al
00709E63  74 0A                           je 0x140709e6f
00709E65  44 38 67 05                     cmp byte ptr [rdi + 5], r12b
00709E69  74 04                           je 0x140709e6f
00709E6B  C6 47 08 01                     mov byte ptr [rdi + 8], 1
00709E6F  44 38 67 0B                     cmp byte ptr [rdi + 0xb], r12b
00709E73  74 04                           je 0x140709e79
00709E75  C6 47 08 01                     mov byte ptr [rdi + 8], 1
00709E79  44 38 67 08                     cmp byte ptr [rdi + 8], r12b
00709E7D  74 07                           je 0x140709e86
00709E7F  BB 01 00 00 00                  mov ebx, 1
00709E84  EB 0A                           jmp 0x140709e90
00709E86  41 8B DC                        mov ebx, r12d
00709E89  41 8A EC                        mov bpl, r12b
00709E8C  84 C0                           test al, al
00709E8E  74 03                           je 0x140709e93
00709E90  40 B5 01                        mov bpl, 1
00709E93  40 88 6C 24 40                  mov byte ptr [rsp + 0x40], bpl
00709E98  45 84 FF                        test r15b, r15b
00709E9B  75 27                           jne 0x140709ec4
00709E9D  48 85 D2                        test rdx, rdx
00709EA0  74 22                           je 0x140709ec4
00709EA2  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
00709EAA  33 C9                           xor ecx, ecx
00709EAC  E8 EF D0 FF FF                  call 0x140706fa0
00709EB1  44 8A B4 24 B8 00 00 00         mov r14b, byte ptr [rsp + 0xb8]
00709EB9  45 84 F6                        test r14b, r14b
00709EBC  0F 84 24 03 00 00               je 0x14070a1e6
00709EC2  EB 03                           jmp 0x140709ec7
00709EC4  41 B6 01                        mov r14b, 1
00709EC7  8A 47 05                        mov al, byte ptr [rdi + 5]
00709ECA  84 C0                           test al, al
00709ECC  74 2E                           je 0x140709efc
00709ECE  45 84 F6                        test r14b, r14b
00709ED1  74 29                           je 0x140709efc
00709ED3  48 B9 00 00 00 00 01 00 00 00   movabs rcx, 0x100000000
00709EDD  48 39 0D 24 9D 8B 00            cmp qword ptr [rip + 0x8b9d24], rcx
00709EE4  72 06                           jb 0x140709eec
00709EE6  44 38 67 0B                     cmp byte ptr [rdi + 0xb], r12b
00709EEA  74 10                           je 0x140709efc
00709EEC  41 8B F4                        mov esi, r12d
00709EEF  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
00709EF7  41 8B CC                        mov ecx, r12d
00709EFA  EB 7A                           jmp 0x140709f76
00709EFC  85 DB                           test ebx, ebx
00709EFE  75 05                           jne 0x140709f05
00709F00  8D 53 10                        lea edx, [rbx + 0x10]
00709F03  EB 18                           jmp 0x140709f1d
00709F05  BA 40 00 00 00                  mov edx, 0x40
00709F0A  84 C0                           test al, al
00709F0C  74 0F                           je 0x140709f1d
00709F0E  41 8A C6                        mov al, r14b
00709F11  F6 D8                           neg al
00709F13  1B C9                           sbb ecx, ecx
00709F15  81 E1 C0 01 00 00               and ecx, 0x1c0
00709F1B  03 D1                           add edx, ecx
00709F1D  41 8B C5                        mov eax, r13d
00709F20  25 FF 0F 00 00                  and eax, 0xfff
00709F25  F7 D8                           neg eax
00709F27  41 8B C5                        mov eax, r13d
00709F2A  1B C9                           sbb ecx, ecx
00709F2C  C1 E8 0C                        shr eax, 0xc
00709F2F  F7 D9                           neg ecx
00709F31  8D 71 01                        lea esi, [rcx + 1]
00709F34  03 F0                           add esi, eax
00709F36  89 B4 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], esi
00709F3D  8B CE                           mov ecx, esi
00709F3F  3B F2                           cmp esi, edx
00709F41  76 0B                           jbe 0x140709f4e
00709F43  8B F2                           mov esi, edx
00709F45  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
00709F4C  8B CA                           mov ecx, edx
00709F4E  8B 15 94 9C 8B 00               mov edx, dword ptr [rip + 0x8b9c94]
00709F54  85 DB                           test ebx, ebx
00709F56  8B C1                           mov eax, ecx
00709F58  0F 44 15 89 9B 8B 00            cmove edx, dword ptr [rip + 0x8b9b89]
00709F5F  40 84 ED                        test bpl, bpl
00709F62  75 12                           jne 0x140709f76
00709F64  C1 EA 0D                        shr edx, 0xd
00709F67  3B C2                           cmp eax, edx
00709F69  76 0B                           jbe 0x140709f76
00709F6B  8B F2                           mov esi, edx
00709F6D  89 94 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edx
00709F74  8B CA                           mov ecx, edx
00709F76  45 84 F6                        test r14b, r14b
00709F79  75 25                           jne 0x140709fa0
00709F7B  C1 E1 0C                        shl ecx, 0xc
00709F7E  45 33 C9                        xor r9d, r9d
00709F81  8B D1                           mov edx, ecx
00709F83  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00709F88  33 C9                           xor ecx, ecx
00709F8A  45 33 C0                        xor r8d, r8d
00709F8D  E8 5E 4C B9 FF                  call 0x14029ebf0
00709F92  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00709F97  48 85 C0                        test rax, rax
00709F9A  0F 84 46 02 00 00               je 0x14070a1e6
00709FA0  44 8B 67 10                     mov r12d, dword ptr [rdi + 0x10]
00709FA4  45 84 FF                        test r15b, r15b
00709FA7  74 3A                           je 0x140709fe3
00709FA9  48 8B 0D 40 64 70 00            mov rcx, qword ptr [rip + 0x706440]
00709FB0  4A 8B 1C E1                     mov rbx, qword ptr [rcx + r12*8]
00709FB4  48 85 DB                        test rbx, rbx
00709FB7  74 2A                           je 0x140709fe3
00709FB9  3B B3 E8 00 00 00               cmp esi, dword ptr [rbx + 0xe8]
00709FBF  76 06                           jbe 0x140709fc7
00709FC1  89 B3 E8 00 00 00               mov dword ptr [rbx + 0xe8], esi
00709FC7  4C 8B 05 6A CD 8B 00            mov r8, qword ptr [rip + 0x8bcd6a]
00709FCE  45 33 C9                        xor r9d, r9d
00709FD1  BA 00 00 02 00                  mov edx, 0x20000
00709FD6  48 8B CB                        mov rcx, rbx
00709FD9  E8 22 ED D2 FF                  call 0x140438d00
00709FDE  E9 97 01 00 00                  jmp 0x14070a17a
00709FE3  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00709FE9  48 8D 0D 70 77 8B 00            lea rcx, [rip + 0x8b7770]
00709FF0  45 33 C9                        xor r9d, r9d
00709FF3  45 33 C0                        xor r8d, r8d
00709FF6  41 8D 51 07                     lea edx, [r9 + 7]
00709FFA  E8 B1 46 B0 FF                  call 0x14020e6b0
00709FFF  45 84 FF                        test r15b, r15b
0070A002  74 3A                           je 0x14070a03e
0070A004  48 8B 05 E5 63 70 00            mov rax, qword ptr [rip + 0x7063e5]
0070A00B  4A 8B 1C E0                     mov rbx, qword ptr [rax + r12*8]
0070A00F  48 85 DB                        test rbx, rbx
0070A012  74 2A                           je 0x14070a03e
0070A014  3B B3 E8 00 00 00               cmp esi, dword ptr [rbx + 0xe8]
0070A01A  76 06                           jbe 0x14070a022
0070A01C  89 B3 E8 00 00 00               mov dword ptr [rbx + 0xe8], esi
0070A022  4C 8B 05 0F CD 8B 00            mov r8, qword ptr [rip + 0x8bcd0f]
0070A029  45 33 C9                        xor r9d, r9d
0070A02C  BA 00 00 02 00                  mov edx, 0x20000
0070A031  48 8B CB                        mov rcx, rbx
0070A034  E8 C7 EC D2 FF                  call 0x140438d00
0070A039  E9 2B 01 00 00                  jmp 0x14070a169
0070A03E  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0070A046  48 85 C0                        test rax, rax
0070A049  74 47                           je 0x14070a092
0070A04B  48 8B C8                        mov rcx, rax
0070A04E  E8 39 5C E3 FF                  call 0x14053fc8c
0070A053  48 8B E8                        mov rbp, rax
0070A056  48 85 C0                        test rax, rax
0070A059  74 37                           je 0x14070a092
0070A05B  48 8B C8                        mov rcx, rax
0070A05E  E8 29 4C CD FF                  call 0x1403dec8c
0070A063  48 8B 8D 00 02 00 00            mov rcx, qword ptr [rbp + 0x200]
0070A06A  8B D8                           mov ebx, eax
0070A06C  E8 CB 84 E4 FF                  call 0x14055253c
0070A071  48 8B CD                        mov rcx, rbp
0070A074  44 8A F8                        mov r15b, al
0070A077  E8 D4 F2 BE FF                  call 0x1402f9350
0070A07C  83 FB 02                        cmp ebx, 2
0070A07F  74 09                           je 0x14070a08a
0070A081  45 84 FF                        test r15b, r15b
0070A084  0F 84 4B 01 00 00               je 0x14070a1d5
0070A08A  44 8A BC 24 A0 00 00 00         mov r15b, byte ptr [rsp + 0xa0]
0070A092  44 8A 4F 05                     mov r9b, byte ptr [rdi + 5]
0070A096  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
0070A09E  44 8A 47 0B                     mov r8b, byte ptr [rdi + 0xb]
0070A0A2  8B CE                           mov ecx, esi
0070A0A4  8A 57 08                        mov dl, byte ptr [rdi + 8]
0070A0A7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0070A0AC  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
0070A0B0  44 88 74 24 30                  mov byte ptr [rsp + 0x30], r14b
0070A0B5  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0070A0B9  8A 47 04                        mov al, byte ptr [rdi + 4]
0070A0BC  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0070A0C0  E8 3B 01 00 00                  call 0x14070a200
0070A0C5  48 8B D8                        mov rbx, rax
0070A0C8  48 85 C0                        test rax, rax
0070A0CB  0F 84 04 01 00 00               je 0x14070a1d5
0070A0D1  C6 80 0C 02 00 00 01            mov byte ptr [rax + 0x20c], 1
0070A0D8  45 84 FF                        test r15b, r15b
0070A0DB  74 45                           je 0x14070a122
0070A0DD  48 8B 05 0C 63 70 00            mov rax, qword ptr [rip + 0x70630c]
0070A0E4  48 8B CF                        mov rcx, rdi
0070A0E7  4A 89 1C E0                     mov qword ptr [rax + r12*8], rbx
0070A0EB  48 8B 05 66 9D 8B 00            mov rax, qword ptr [rip + 0x8b9d66]
0070A0F2  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0070A0F6  E8 D5 09 FB FF                  call 0x1406baad0
0070A0FB  48 85 C0                        test rax, rax
0070A0FE  0F 84 D1 00 00 00               je 0x14070a1d5
0070A104  48 89 83 B0 01 00 00            mov qword ptr [rbx + 0x1b0], rax
0070A10B  45 33 C9                        xor r9d, r9d
0070A10E  4C 8B 05 23 CC 8B 00            mov r8, qword ptr [rip + 0x8bcc23]
0070A115  BA 00 00 02 00                  mov edx, 0x20000
0070A11A  48 8B CB                        mov rcx, rbx
0070A11D  E8 DE EB D2 FF                  call 0x140438d00
0070A122  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
0070A129  85 C0                           test eax, eax
0070A12B  74 0A                           je 0x14070a137
0070A12D  89 83 E8 00 00 00               mov dword ptr [rbx + 0xe8], eax
0070A133  B1 01                           mov cl, 1
0070A135  EB 1F                           jmp 0x14070a156
0070A137  41 8B C5                        mov eax, r13d
0070A13A  25 FF 0F 00 00                  and eax, 0xfff
0070A13F  F7 D8                           neg eax
0070A141  1B D2                           sbb edx, edx
0070A143  41 C1 ED 0C                     shr r13d, 0xc
0070A147  F7 DA                           neg edx
0070A149  FF C2                           inc edx
0070A14B  41 03 D5                        add edx, r13d
0070A14E  89 93 E8 00 00 00               mov dword ptr [rbx + 0xe8], edx
0070A154  32 C9                           xor cl, cl
0070A156  B8 B8 01 00 00                  mov eax, 0x1b8
0070A15B  48 8B D3                        mov rdx, rbx
0070A15E  88 0C 18                        mov byte ptr [rax + rbx], cl
0070A161  48 83 A3 38 01 00 00 00         and qword ptr [rbx + 0x138], 0
0070A169  45 33 C0                        xor r8d, r8d
0070A16C  48 8D 0D ED 75 8B 00            lea rcx, [rip + 0x8b75ed]
0070A173  33 D2                           xor edx, edx
0070A175  E8 96 51 C3 FF                  call 0x14033f310
0070A17A  C6 83 BC 01 00 00 00            mov byte ptr [rbx + 0x1bc], 0
0070A181  83 3F 01                        cmp dword ptr [rdi], 1
0070A184  72 09                           jb 0x14070a18f
0070A186  8A 47 09                        mov al, byte ptr [rdi + 9]
0070A189  88 83 BC 01 00 00               mov byte ptr [rbx + 0x1bc], al
0070A18F  8B 83 E8 00 00 00               mov eax, dword ptr [rbx + 0xe8]
0070A195  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0070A19D  89 01                           mov dword ptr [rcx], eax
0070A19F  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0070A1A4  48 89 83 30 01 00 00            mov qword ptr [rbx + 0x130], rax
0070A1AB  45 84 FF                        test r15b, r15b
0070A1AE  75 19                           jne 0x14070a1c9
0070A1B0  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0070A1B8  48 8B CB                        mov rcx, rbx
0070A1BB  48 89 83 10 02 00 00            mov qword ptr [rbx + 0x210], rax
0070A1C2  E8 09 5A E3 FF                  call 0x14053fbd0
0070A1C7  EB 07                           jmp 0x14070a1d0
0070A1C9  44 89 A3 7C 01 00 00            mov dword ptr [rbx + 0x17c], r12d
0070A1D0  48 8B C3                        mov rax, rbx
0070A1D3  EB 13                           jmp 0x14070a1e8
0070A1D5  45 33 C0                        xor r8d, r8d
0070A1D8  48 8D 0D 81 75 8B 00            lea rcx, [rip + 0x8b7581]
0070A1DF  33 D2                           xor edx, edx
0070A1E1  E8 2A 51 C3 FF                  call 0x14033f310
0070A1E6  33 C0                           xor eax, eax
0070A1E8  48 83 C4 58                     add rsp, 0x58
0070A1EC  41 5F                           pop r15
0070A1EE  41 5E                           pop r14
0070A1F0  41 5D                           pop r13
0070A1F2  41 5C                           pop r12
0070A1F4  5F                              pop rdi
0070A1F5  5E                              pop rsi
0070A1F6  5D                              pop rbp
0070A1F7  5B                              pop rbx
0070A1F8  C3                              ret
0070A1F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalGetAdapterV2(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (88);
    v_r12 = 0;
    *(unsigned __int8 *)(v_rsp + 32) = 0;
    v_stack_m50 = 0;
    if ((*(unsigned int *)(a1)) > 2) goto loc_0070A1E6;
    if ((*(unsigned __int8 *)(a1 + 4)) == 0) goto loc_00709E2A;
    if ((*(unsigned int *)(a1 + 20)) != 1) goto loc_00709E1D;
    if ((*(unsigned int *)(a1 + 16)) <= 7) goto loc_00709E2A;
loc_00709E1D:
    v_stack_p8 = 0;
    goto loc_00709E55;
loc_00709E2A:
    v_stack_p8 = 1;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0070A1E6;
loc_00709E55:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4)) == 0) goto loc_00709E6F;
    if ((*(unsigned __int8 *)(a1 + 5)) != 0) {
        *(unsigned __int8 *)(a1 + 8) = 1;
    }
    if ((*(unsigned __int8 *)(a1 + 11)) != 0) {
        *(unsigned __int8 *)(a1 + 8) = 1;
    }
    if ((*(unsigned __int8 *)(a1 + 8)) == 0) goto loc_00709E86;
    goto loc_00709E90;
loc_00709E86:
    v_rbp = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4)) != 0) {
        v_rbp = 1;
    }
    v_stack_m58 = (unsigned __int8)(v_rbp);
    if (1 != 0) goto loc_00709EC4;
    if (v_stack_p10 == 0) goto loc_00709EC4;
    a1 = 0;
    result = HalpGetCacheCoherency(a1, v_stack_p10, v_stack_p20, a4);
    if ((unsigned __int8)(v_stack_p20) == 0) goto loc_0070A1E6;
    goto loc_00709EC7;
loc_00709EC4:
loc_00709EC7:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 5)) == 0) goto loc_00709EFC;
    if (1 == 0) goto loc_00709EFC;
    if ((*(unsigned __int64 *)(v_rip + 9149732)) < 0) goto loc_00709EEC;
    if ((*(unsigned __int8 *)(a1 + 11)) == 0) goto loc_00709EFC;
loc_00709EEC:
    v_stack_p20 = 0;
    goto loc_00709F76;
loc_00709EFC:
    if (0 != 0) goto loc_00709F05;
    goto loc_00709F1D;
loc_00709F05:
    result = *(unsigned __int8 *)(a1 + 5);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 5)) != 0) {
        result = 1;
        result = (unsigned __int8)(-(result));
        a1 = (unsigned int)((0) & (448));
        a2 = (unsigned int)((64) + ((unsigned int)(a1)));
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (0xFFFULL));
    result = (unsigned int)(-(result));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) >> (12));
    a1 = (unsigned int)(-(a1));
    v_rsi = (unsigned int)((a1 + 1) + ((unsigned int)(result)));
    v_stack_p20 = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) >= = ((unsigned int)(a2))) {
        v_rsi = (unsigned int)(a2);
        v_stack_p20 = (unsigned int)(a2);
        a1 = (unsigned int)(a2);
    }
    a2 = (unsigned int)(*(unsigned int *)(v_rip + 9149588));
    if (0 == 0) { a2 = *(unsigned int *)(v_rip + 9149321); }
    if ((unsigned __int8)(v_rbp) != 0) goto loc_00709F76;
    a2 = (unsigned int)((a2) >> (13));
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) >= = ((unsigned int)(a2))) {
        v_rsi = (unsigned int)(a2);
        v_stack_p20 = (unsigned int)(a2);
        a1 = (unsigned int)(a2);
    }
    if (1 != 0) goto loc_00709FA0;
    a1 = (unsigned int)((a1) << (12));
    a4 = 0;
    v_stack_m78 = 0;
    a1 = 0;
    a3 = 0;
    result = IoAllocateMdl(a1, (unsigned int)((unsigned int)(a1)), a3, a4);
    v_stack_m50 = result;
    if (result == 0) goto loc_0070A1E6;
loc_00709FA0:
    if (1 == 0) goto loc_00709FE3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365696) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) == 0) goto loc_00709FE3;
    if (((unsigned int)(v_rsi)) >= = (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365696) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) + 232))) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365696) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) + 232) = (unsigned int)(v_rsi);
    }
    a4 = 0;
    result = ObReferenceObjectByPointer(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365696) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8), (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9162090), a4);
    goto loc_0070A17A;
loc_00709FE3:
    a4 = 0;
    a3 = 0;
    result = KeWaitForSingleObject(v_rip + 9140080, a4 + 7, a3, a4);
    if (1 == 0) goto loc_0070A03E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365605) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) == 0) goto loc_0070A03E;
    if (((unsigned int)(v_rsi)) >= = (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365605) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) + 232))) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365605) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) + 232) = (unsigned int)(v_rsi);
    }
    a4 = 0;
    result = ObReferenceObjectByPointer(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365605) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8), (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161999), a4);
    goto loc_0070A169;
loc_0070A03E:
    if (v_stack_p10 == 0) goto loc_0070A092;
    result = HalpDmaFindAdapterByDeviceObject(v_stack_p10, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161999), a4);
    if (result == 0) goto loc_0070A092;
    result = HalpDmaGetAdapterVersion(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161999), a4);
    result = HalpDmaIsAutomaticDomain(*(unsigned __int64 *)(result + 512), (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161999), a4);
    result = ObfDereferenceObject(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161999), a4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 2) goto loc_0070A08A;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0070A1D5;
loc_0070A08A:
loc_0070A092:
    v_stack_m60 = v_stack_p20;
    v_stack_m68 = 1;
    v_stack_m70 = (unsigned __int8)(v_stack_m58);
    v_stack_m78 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 4));
    result = HalpDmaAllocateChildAdapterV2((unsigned int)((unsigned int)(v_rsi)), *(unsigned __int8 *)(a1 + 8), *(unsigned __int8 *)(a1 + 11), *(unsigned __int8 *)(a1 + 5));
    if (result == 0) goto loc_0070A1D5;
    *(unsigned __int8 *)(result + 524) = 1;
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_0070A122;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7365388) + (unsigned int)(*(unsigned int *)(a1 + 16)) * 8) = result;
    result = guard_dispatch_icall(0, *(unsigned __int8 *)(a1 + 8), *(unsigned __int8 *)(a1 + 11), *(unsigned __int8 *)(a1 + 5));
    if (result == 0) goto loc_0070A1D5;
    *(unsigned __int64 *)(result + 432) = result;
    a4 = 0;
    result = ObReferenceObjectByPointer(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9161763), a4);
loc_0070A122:
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_0070A137;
    *(unsigned int *)(result + 232) = (unsigned int)((unsigned int)(v_stack_p20));
    goto loc_0070A156;
loc_0070A137:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (0xFFFULL));
    result = (unsigned int)(-(result));
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (12));
    a2 = (unsigned int)(-((unsigned int)(0x20000ULL)));
    a2 = (unsigned int)((a2) + 1);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13)));
    *(unsigned int *)(result + 232) = (unsigned int)(a2);
    a1 = 0;
loc_0070A156:
    *(unsigned __int8 *)(440 + result * 1) = 0;
loc_0070A169:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 9139693, a2, a3, a4);
loc_0070A17A:
    *(unsigned __int8 *)(result + 444) = 0;
    if ((*(unsigned int *)(a1)) >= 1) {
        result = *(unsigned __int8 *)(a1 + 9);
        *(unsigned __int8 *)(result + 444) = (unsigned __int8)(result);
    }
    *(unsigned int *)(v_stack_p18) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 232)));
    *(unsigned __int64 *)(result + 304) = v_stack_m50;
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_0070A1C9;
    *(unsigned __int64 *)(result + 528) = v_stack_p10;
    result = HalpAddAdapterToList(result, a2, a3, a4);
    goto loc_0070A1D0;
loc_0070A1C9:
    *(unsigned int *)(result + 380) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
loc_0070A1D0:
    goto loc_0070A1E8;
loc_0070A1D5:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 9139585, a2, a3, a4);
loc_0070A1E6:
    result = 0;
loc_0070A1E8:
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalGetAdapterV2(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint8_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint8_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (88);
    local_r12 = 0;
    *(uint8_t *)(local_rsp + 0x20) = 0;
    v_stack_m50 = 0;
    if ((*(uint32_t *)(arg1)) > 2) goto loc_0070A1E6;
    if ((*(uint8_t *)(arg1 + 0x4)) == 0) goto loc_00709E2A;
    if ((*(uint32_t *)(arg1 + 0x14)) != 1) goto loc_00709E1D;
    if ((*(uint32_t *)(arg1 + 0x10)) <= 7) goto loc_00709E2A;
loc_00709E1D:
    v_stack_p8 = 0;
    goto loc_00709E55;
loc_00709E2A:
    v_stack_p8 = 1;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0070A1E6;
loc_00709E55:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x4)) == 0) goto loc_00709E6F;
    if ((*(uint8_t *)(arg1 + 0x5)) != 0) {
        *(uint8_t *)(arg1 + 0x8) = 1;
    }
    if ((*(uint8_t *)(arg1 + 0xB)) != 0) {
        *(uint8_t *)(arg1 + 0x8) = 1;
    }
    if ((*(uint8_t *)(arg1 + 0x8)) == 0) goto loc_00709E86;
    goto loc_00709E90;
loc_00709E86:
    local_rbp = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x4)) != 0) {
        local_rbp = 1;
    }
    v_stack_m58 = (uint8_t)(local_rbp);
    if (1 != 0) goto loc_00709EC4;
    if (v_stack_p10 == 0) goto loc_00709EC4;
    Arg1 = 0;
    result = HalpGetCacheCoherency(Arg1, v_stack_p10, v_stack_p20, Arg4);
    if ((uint8_t)(v_stack_p20) == 0) goto loc_0070A1E6;
    goto loc_00709EC7;
loc_00709EC4:
loc_00709EC7:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x5)) == 0) goto loc_00709EFC;
    if (1 == 0) goto loc_00709EFC;
    if ((*(uint64_t *)(v_rip + 0x8B9D24)) < 0) goto loc_00709EEC;
    if ((*(uint8_t *)(arg1 + 0xB)) == 0) goto loc_00709EFC;
loc_00709EEC:
    v_stack_p20 = 0;
    goto loc_00709F76;
loc_00709EFC:
    if (0 != 0) goto loc_00709F05;
    goto loc_00709F1D;
loc_00709F05:
    result = *(uint8_t *)(arg1 + 0x5);
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x5)) != 0) {
        result = 1;
        result = (uint8_t)(-(result));
        Arg1 = (uint32_t)((0) & (448));
        Arg2 = (uint32_t)((64) + ((uint32_t)(Arg1)));
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (0xFFFULL));
    result = (uint32_t)(-(result));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) >> (12));
    Arg1 = (uint32_t)(-(Arg1));
    local_rsi = (uint32_t)((Arg1 + 1) + ((uint32_t)(result)));
    v_stack_p20 = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) >= = ((uint32_t)(Arg2))) {
        local_rsi = (uint32_t)(Arg2);
        v_stack_p20 = (uint32_t)(Arg2);
        Arg1 = (uint32_t)(Arg2);
    }
    Arg2 = (uint32_t)(*(uint32_t *)(v_rip + 0x8B9C94));
    if (0 == 0) { Arg2 = *(uint32_t *)(v_rip + 0x8B9B89); }
    if ((uint8_t)(local_rbp) != 0) goto loc_00709F76;
    Arg2 = (uint32_t)((Arg2) >> (13));
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) >= = ((uint32_t)(Arg2))) {
        local_rsi = (uint32_t)(Arg2);
        v_stack_p20 = (uint32_t)(Arg2);
        Arg1 = (uint32_t)(Arg2);
    }
    if (1 != 0) goto loc_00709FA0;
    Arg1 = (uint32_t)((Arg1) << (12));
    Arg4 = 0;
    v_stack_m78 = 0;
    Arg1 = 0;
    Arg3 = 0;
    result = IoAllocateMdl(Arg1, (uint32_t)((uint32_t)(Arg1)), Arg3, Arg4);
    v_stack_m50 = result;
    if (result == 0) goto loc_0070A1E6;
loc_00709FA0:
    if (1 == 0) goto loc_00709FE3;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x706440) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) == 0) goto loc_00709FE3;
    if (((uint32_t)(local_rsi)) >= = (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x706440) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) + 0xE8))) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x706440) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) + 0xE8) = (uint32_t)(local_rsi);
    }
    Arg4 = 0;
    result = ObReferenceObjectByPointer(*(uint64_t *)(*(uint64_t *)(v_rip + 0x706440) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8), (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD6A), Arg4);
    goto loc_0070A17A;
loc_00709FE3:
    Arg4 = 0;
    Arg3 = 0;
    result = KeWaitForSingleObject(v_rip + 9140080, Arg4 + 7, Arg3, Arg4);
    if (1 == 0) goto loc_0070A03E;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7063E5) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) == 0) goto loc_0070A03E;
    if (((uint32_t)(local_rsi)) >= = (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7063E5) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) + 0xE8))) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7063E5) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) + 0xE8) = (uint32_t)(local_rsi);
    }
    Arg4 = 0;
    result = ObReferenceObjectByPointer(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7063E5) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8), (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD0F), Arg4);
    goto loc_0070A169;
loc_0070A03E:
    if (v_stack_p10 == 0) goto loc_0070A092;
    result = HalpDmaFindAdapterByDeviceObject(v_stack_p10, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD0F), Arg4);
    if (result == 0) goto loc_0070A092;
    result = HalpDmaGetAdapterVersion(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD0F), Arg4);
    result = HalpDmaIsAutomaticDomain(*(uint64_t *)(result + 0x200), (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD0F), Arg4);
    result = ObfDereferenceObject(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCD0F), Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 2) goto loc_0070A08A;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0070A1D5;
loc_0070A08A:
loc_0070A092:
    v_stack_m60 = v_stack_p20;
    v_stack_m68 = 1;
    v_stack_m70 = (uint8_t)(v_stack_m58);
    v_stack_m78 = (uint8_t)(*(uint8_t *)(arg1 + 0x4));
    result = HalpDmaAllocateChildAdapterV2((uint32_t)((uint32_t)(local_rsi)), *(uint8_t *)(arg1 + 0x8), *(uint8_t *)(arg1 + 0xB), *(uint8_t *)(arg1 + 0x5));
    if (result == 0) goto loc_0070A1D5;
    *(uint8_t *)(result + 0x20C) = 1;
    if ((uint8_t)(v_stack_p8) == 0) goto loc_0070A122;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x70630C) + (uint32_t)(*(uint32_t *)(arg1 + 0x10)) * 8) = result;
    result = guard_dispatch_icall(0, *(uint8_t *)(arg1 + 0x8), *(uint8_t *)(arg1 + 0xB), *(uint8_t *)(arg1 + 0x5));
    if (result == 0) goto loc_0070A1D5;
    *(uint64_t *)(result + 0x1B0) = result;
    Arg4 = 0;
    result = ObReferenceObjectByPointer(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BCC23), Arg4);
loc_0070A122:
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_0070A137;
    *(uint32_t *)(result + 0xE8) = (uint32_t)((uint32_t)(v_stack_p20));
    goto loc_0070A156;
loc_0070A137:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (0xFFFULL));
    result = (uint32_t)(-(result));
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (12));
    Arg2 = (uint32_t)(-((uint32_t)(0x20000ULL)));
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r13)));
    *(uint32_t *)(result + 0xE8) = (uint32_t)(Arg2);
    Arg1 = 0;
loc_0070A156:
    *(uint8_t *)(440 + result * 1) = 0;
loc_0070A169:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 9139693, Arg2, Arg3, Arg4);
loc_0070A17A:
    *(uint8_t *)(result + 0x1BC) = 0;
    if ((*(uint32_t *)(arg1)) >= 1) {
        result = *(uint8_t *)(arg1 + 0x9);
        *(uint8_t *)(result + 0x1BC) = (uint8_t)(result);
    }
    *(uint32_t *)(v_stack_p18) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xE8)));
    *(uint64_t *)(result + 0x130) = v_stack_m50;
    if ((uint8_t)(v_stack_p8) != 0) goto loc_0070A1C9;
    *(uint64_t *)(result + 0x210) = v_stack_p10;
    result = HalpAddAdapterToList(result, Arg2, Arg3, Arg4);
    goto loc_0070A1D0;
loc_0070A1C9:
    *(uint32_t *)(result + 0x17C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
loc_0070A1D0:
    goto loc_0070A1E8;
loc_0070A1D5:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 9139585, Arg2, Arg3, Arg4);
loc_0070A1E6:
    result = 0;
loc_0070A1E8:
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `W` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00709DD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
