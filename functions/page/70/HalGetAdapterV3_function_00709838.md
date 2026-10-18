# HalGetAdapterV3

- RVA: `0x00709838`–`0x00709DD0` (길이 `1,432` bytes)
- VA: `0x0000000140709838`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C441C`
- 디코드: `388`개 명령, `1,432/1,432` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00709901` → [HalpFindDmaControllerByRequestLine](../../text/55/HalpFindDmaControllerByRequestLine_function_00554514.md) (function, `0x00554514`)
- `0x0070991B` → [HalpFindAdapterByRequestLine](../../text/55/HalpFindAdapterByRequestLine_function_00554460.md) (function, `0x00554460`)
- `0x00709931` → [HalpDmaControllerValidateRequestLineBinding](../../text/55/HalpDmaControllerValidateRequestLineBinding_function_00554274.md) (function, `0x00554274`)
- `0x007099C5` → [HalpGetCacheCoherency](HalpGetCacheCoherency_function_00706FA0.md) (function, `0x00706FA0`)
- `0x00709A9E` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x00709AE3` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x00709B04` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00709B19` → [HalpFindAdapterByRequestLine](../../text/55/HalpFindAdapterByRequestLine_function_00554460.md) (function, `0x00554460`)
- `0x00709B54` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x00709B62` → [HalpDmaFindAdapterByDeviceObject](../../text/53/HalpDmaFindAdapterByDeviceObject_function_0053FC8C.md) (function, `0x0053FC8C`)
- `0x00709B72` → [HalpDmaGetAdapterVersion](../../text/3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (function, `0x003DEC8C`)
- `0x00709B83` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00709BF5` → [HalpDmaAllocateChildAdapterV3](HalpDmaAllocateChildAdapterV3_function_007066A0.md) (function, `0x007066A0`)
- `0x00709C23` → [HalpAddAdapterToList](../../text/53/HalpAddAdapterToList_function_0053FBD0.md) (function, `0x0053FBD0`)
- `0x00709C90` → [HalpDmaIsAutomaticDomain](../../text/55/HalpDmaIsAutomaticDomain_function_0055253C.md) (function, `0x0055253C`)
- `0x00709CB2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00709CC3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00709CD4` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00709CF6` → [HalpAddAdapterToSystemList](../../text/55/HalpAddAdapterToSystemList_function_00553FE0.md) (function, `0x00553FE0`)
- `0x00709D31` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x00709D71` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [HalpGetAdapter](HalpGetAdapter_function_00706EBC.md) at `0x00706F3C`

### Static image references
- `0x00709860` → RVA `0x00FC18A0` (`.data`; read)
- `0x007099E4` → RVA `0x00FC3C08` (`.data`; read)
- `0x00709A5E` → RVA `0x00FC3DE8` (`.data`; read)
- `0x00709A6A` → RVA `0x00FC3CE8` (`.data`; read)
- `0x00709AD9` → RVA `0x00FC6D38` (`ALMOSTRO`; read)
- `0x00709AF3` → RVA `0x00FC1760` (`.data`; read)
- `0x00709B9B` → RVA `0x00FC18A4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00709901` → [HalpFindDmaControllerByRequestLine](../../text/55/HalpFindDmaControllerByRequestLine_function_00554514.md) (`PAGE` → `.text`)
  - `0x0070991B` → [HalpFindAdapterByRequestLine](../../text/55/HalpFindAdapterByRequestLine_function_00554460.md) (`PAGE` → `.text`)
  - `0x00709931` → [HalpDmaControllerValidateRequestLineBinding](../../text/55/HalpDmaControllerValidateRequestLineBinding_function_00554274.md) (`PAGE` → `.text`)
  - `0x00709A9E` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x00709AE3` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x00709B04` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00709B19` → [HalpFindAdapterByRequestLine](../../text/55/HalpFindAdapterByRequestLine_function_00554460.md) (`PAGE` → `.text`)
  - `0x00709B54` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x00709B62` → [HalpDmaFindAdapterByDeviceObject](../../text/53/HalpDmaFindAdapterByDeviceObject_function_0053FC8C.md) (`PAGE` → `.text`)
  - `0x00709B72` → [HalpDmaGetAdapterVersion](../../text/3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (`PAGE` → `.text`)
  - `0x00709B83` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00709C23` → [HalpAddAdapterToList](../../text/53/HalpAddAdapterToList_function_0053FBD0.md) (`PAGE` → `.text`)
  - `0x00709C90` → [HalpDmaIsAutomaticDomain](../../text/55/HalpDmaIsAutomaticDomain_function_0055253C.md) (`PAGE` → `.text`)
  - `0x00709CB2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00709CC3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00709CD4` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00709CF6` → [HalpAddAdapterToSystemList](../../text/55/HalpAddAdapterToSystemList_function_00553FE0.md) (`PAGE` → `.text`)
  - `0x00709D31` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x00709D71` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00709838  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0070983D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00709842  55                              push rbp
00709843  53                              push rbx
00709844  56                              push rsi
00709845  57                              push rdi
00709846  41 54                           push r12
00709848  41 55                           push r13
0070984A  41 56                           push r14
0070984C  41 57                           push r15
0070984E  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00709853  48 81 EC A8 00 00 00            sub rsp, 0xa8
0070985A  45 33 D2                        xor r10d, r10d
0070985D  4C 8B CA                        mov r9, rdx
00709860  44 38 15 39 80 8B 00            cmp byte ptr [rip + 0x8b8039], r10b
00709867  4C 8B F1                        mov r14, rcx
0070986A  44 88 55 E7                     mov byte ptr [rbp - 0x19], r10b
0070986E  45 0F 45 C2                     cmovne r8d, r10d
00709872  4C 89 55 07                     mov qword ptr [rbp + 7], r10
00709876  83 39 03                        cmp dword ptr [rcx], 3
00709879  41 8D 72 40                     lea esi, [r10 + 0x40]
0070987D  44 89 45 77                     mov dword ptr [rbp + 0x77], r8d
00709881  44 88 55 E9                     mov byte ptr [rbp - 0x17], r10b
00709885  75 08                           jne 0x14070988f
00709887  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0070988A  89 45 EB                        mov dword ptr [rbp - 0x15], eax
0070988D  EB 3E                           jmp 0x1407098cd
0070988F  0F 83 44 04 00 00               jae 0x140709cd9
00709895  45 85 C0                        test r8d, r8d
00709898  0F 84 3B 04 00 00               je 0x140709cd9
0070989E  44 38 51 04                     cmp byte ptr [rcx + 4], r10b
007098A2  0F 84 31 04 00 00               je 0x140709cd9
007098A8  44 38 51 0B                     cmp byte ptr [rcx + 0xb], r10b
007098AC  74 05                           je 0x1407098b3
007098AE  89 75 EB                        mov dword ptr [rbp - 0x15], esi
007098B1  EB 1A                           jmp 0x1407098cd
007098B3  44 38 51 08                     cmp byte ptr [rcx + 8], r10b
007098B7  75 0D                           jne 0x1407098c6
007098B9  C7 45 EB 18 00 00 00            mov dword ptr [rbp - 0x15], 0x18
007098C0  44 38 51 05                     cmp byte ptr [rcx + 5], r10b
007098C4  74 07                           je 0x1407098cd
007098C6  C7 45 EB 20 00 00 00            mov dword ptr [rbp - 0x15], 0x20
007098CD  41 BC 04 00 00 00               mov r12d, 4
007098D3  4D 8B FE                        mov r15, r14
007098D6  48 85 D2                        test rdx, rdx
007098D9  0F 84 FA 03 00 00               je 0x140709cd9
007098DF  49 8B DA                        mov rbx, r10
007098E2  44 89 55 F3                     mov dword ptr [rbp - 0xd], r10d
007098E6  49 8B FA                        mov rdi, r10
007098E9  47 38 14 26                     cmp byte ptr [r14 + r12], r10b
007098ED  0F 85 82 00 00 00               jne 0x140709975
007098F3  48 8B 59 38                     mov rbx, qword ptr [rcx + 0x38]
007098F7  8B 49 30                        mov ecx, dword ptr [rcx + 0x30]
007098FA  89 4D F3                        mov dword ptr [rbp - 0xd], ecx
007098FD  C6 45 EA 01                     mov byte ptr [rbp - 0x16], 1
00709901  E8 0E AC E4 FF                  call 0x140554514
00709906  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0070990A  4C 8B E8                        mov r13, rax
0070990D  48 85 C0                        test rax, rax
00709910  0F 84 C3 03 00 00               je 0x140709cd9
00709916  8B D1                           mov edx, ecx
00709918  48 8B C8                        mov rcx, rax
0070991B  E8 40 AB E4 FF                  call 0x140554460
00709920  45 33 D2                        xor r10d, r10d
00709923  48 8B F8                        mov rdi, rax
00709926  48 85 C0                        test rax, rax
00709929  75 16                           jne 0x140709941
0070992B  49 8B D6                        mov rdx, r14
0070992E  49 8B CD                        mov rcx, r13
00709931  E8 3E A9 E4 FF                  call 0x140554274
00709936  45 33 D2                        xor r10d, r10d
00709939  84 C0                           test al, al
0070993B  0F 84 98 03 00 00               je 0x140709cd9
00709941  4C 8B 4D 6F                     mov r9, qword ptr [rbp + 0x6f]
00709945  45 8B 7E 20                     mov r15d, dword ptr [r14 + 0x20]
00709949  43 8A 04 26                     mov al, byte ptr [r14 + r12]
0070994D  41 0F BA F7 1F                  btr r15d, 0x1f
00709952  41 81 C7 FF 0F 00 00            add r15d, 0xfff
00709959  41 81 E7 00 F0 FF FF            and r15d, 0xfffff000
00709960  84 C0                           test al, al
00709962  74 1E                           je 0x140709982
00709964  45 8A 46 05                     mov r8b, byte ptr [r14 + 5]
00709968  8B 4D EB                        mov ecx, dword ptr [rbp - 0x15]
0070996B  44 88 45 67                     mov byte ptr [rbp + 0x67], r8b
0070996F  44 89 55 F7                     mov dword ptr [rbp - 9], r10d
00709973  EB 29                           jmp 0x14070999e
00709975  44 88 55 EA                     mov byte ptr [rbp - 0x16], r10b
00709979  4D 8B EA                        mov r13, r10
0070997C  4C 89 55 FF                     mov qword ptr [rbp - 1], r10
00709980  EB C3                           jmp 0x140709945
00709982  41 8B 55 30                     mov edx, dword ptr [r13 + 0x30]
00709986  B9 08 00 00 00                  mov ecx, 8
0070998B  3B D1                           cmp edx, ecx
0070998D  C6 45 67 01                     mov byte ptr [rbp + 0x67], 1
00709991  0F 47 D1                        cmova edx, ecx
00709994  41 8B 4D 4C                     mov ecx, dword ptr [r13 + 0x4c]
00709998  89 55 F7                        mov dword ptr [rbp - 9], edx
0070999B  89 4D EB                        mov dword ptr [rbp - 0x15], ecx
0070999E  83 F9 20                        cmp ecx, 0x20
007099A1  72 08                           jb 0x1407099ab
007099A3  41 BD 01 00 00 00               mov r13d, 1
007099A9  EB 0B                           jmp 0x1407099b6
007099AB  44 88 55 E8                     mov byte ptr [rbp - 0x18], r10b
007099AF  45 8B EA                        mov r13d, r10d
007099B2  84 C0                           test al, al
007099B4  74 04                           je 0x1407099ba
007099B6  C6 45 E8 01                     mov byte ptr [rbp - 0x18], 1
007099BA  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
007099BE  4C 8D 45 E7                     lea r8, [rbp - 0x19]
007099C2  49 8B D1                        mov rdx, r9
007099C5  E8 D6 D5 FF FF                  call 0x140706fa0
007099CA  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
007099CD  3B C6                           cmp eax, esi
007099CF  72 06                           jb 0x1407099d7
007099D1  48 83 C8 FF                     or rax, 0xffffffffffffffff
007099D5  EB 0D                           jmp 0x1407099e4
007099D7  8B C8                           mov ecx, eax
007099D9  B8 01 00 00 00                  mov eax, 1
007099DE  48 D3 E0                        shl rax, cl
007099E1  48 FF C8                        dec rax
007099E4  48 3B 05 1D A2 8B 00            cmp rax, qword ptr [rip + 0x8ba21d]
007099EB  44 8A 4D E7                     mov r9b, byte ptr [rbp - 0x19]
007099EF  0F 93 C0                        setae al
007099F2  80 3D A7 7E 8B 00 00            cmp byte ptr [rip + 0x8b7ea7], 0
007099F9  74 10                           je 0x140709a0b
007099FB  32 C9                           xor cl, cl
007099FD  8A 55 67                        mov dl, byte ptr [rbp + 0x67]
00709A00  45 85 ED                        test r13d, r13d
00709A03  75 2D                           jne 0x140709a32
00709A05  41 8D 75 10                     lea esi, [r13 + 0x10]
00709A09  EB 39                           jmp 0x140709a44
00709A0B  8A C8                           mov cl, al
00709A0D  84 C0                           test al, al
00709A0F  74 EC                           je 0x1407099fd
00709A11  45 84 C9                        test r9b, r9b
00709A14  74 E7                           je 0x1407099fd
00709A16  8A 55 67                        mov dl, byte ptr [rbp + 0x67]
00709A19  84 D2                           test dl, dl
00709A1B  74 E3                           je 0x140709a00
00709A1D  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00709A20  85 D2                           test edx, edx
00709A22  74 05                           je 0x140709a29
00709A24  83 FA 02                        cmp edx, 2
00709A27  75 D4                           jne 0x1407099fd
00709A29  33 C9                           xor ecx, ecx
00709A2B  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
00709A2E  33 C0                           xor eax, eax
00709A30  EB 54                           jmp 0x140709a86
00709A32  84 D2                           test dl, dl
00709A34  74 0E                           je 0x140709a44
00709A36  45 84 C9                        test r9b, r9b
00709A39  75 04                           jne 0x140709a3f
00709A3B  84 C9                           test cl, cl
00709A3D  75 05                           jne 0x140709a44
00709A3F  BE 00 02 00 00                  mov esi, 0x200
00709A44  41 8B CF                        mov ecx, r15d
00709A47  C1 E9 0C                        shr ecx, 0xc
00709A4A  FF C1                           inc ecx
00709A4C  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
00709A4F  44 8B C1                        mov r8d, ecx
00709A52  3B CE                           cmp ecx, esi
00709A54  76 08                           jbe 0x140709a5e
00709A56  8B CE                           mov ecx, esi
00709A58  44 8B C6                        mov r8d, esi
00709A5B  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
00709A5E  8B 15 84 A3 8B 00               mov edx, dword ptr [rip + 0x8ba384]
00709A64  45 85 ED                        test r13d, r13d
00709A67  41 8B C0                        mov eax, r8d
00709A6A  0F 44 15 77 A2 8B 00            cmove edx, dword ptr [rip + 0x8ba277]
00709A71  80 7D E8 00                     cmp byte ptr [rbp - 0x18], 0
00709A75  75 0F                           jne 0x140709a86
00709A77  C1 EA 0D                        shr edx, 0xd
00709A7A  44 3B C2                        cmp r8d, edx
00709A7D  76 07                           jbe 0x140709a86
00709A7F  8B CA                           mov ecx, edx
00709A81  89 55 EF                        mov dword ptr [rbp - 0x11], edx
00709A84  8B C2                           mov eax, edx
00709A86  45 84 C9                        test r9b, r9b
00709A89  75 28                           jne 0x140709ab3
00709A8B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00709A91  45 33 C9                        xor r9d, r9d
00709A94  C1 E0 0C                        shl eax, 0xc
00709A97  45 33 C0                        xor r8d, r8d
00709A9A  8B D0                           mov edx, eax
00709A9C  33 C9                           xor ecx, ecx
00709A9E  E8 4D 51 B9 FF                  call 0x14029ebf0
00709AA3  48 89 45 07                     mov qword ptr [rbp + 7], rax
00709AA7  48 85 C0                        test rax, rax
00709AAA  0F 84 29 02 00 00               je 0x140709cd9
00709AB0  8B 4D EF                        mov ecx, dword ptr [rbp - 0x11]
00709AB3  48 85 FF                        test rdi, rdi
00709AB6  74 35                           je 0x140709aed
00709AB8  3B 8F E8 00 00 00               cmp ecx, dword ptr [rdi + 0xe8]
00709ABE  76 06                           jbe 0x140709ac6
00709AC0  89 8F E8 00 00 00               mov dword ptr [rdi + 0xe8], ecx
00709AC6  49 8B 46 38                     mov rax, qword ptr [r14 + 0x38]
00709ACA  45 33 C9                        xor r9d, r9d
00709ACD  48 89 87 C8 01 00 00            mov qword ptr [rdi + 0x1c8], rax
00709AD4  BA 00 00 02 00                  mov edx, 0x20000
00709AD9  4C 8B 05 58 D2 8B 00            mov r8, qword ptr [rip + 0x8bd258]
00709AE0  48 8B CF                        mov rcx, rdi
00709AE3  E8 18 F2 D2 FF                  call 0x140438d00
00709AE8  E9 89 02 00 00                  jmp 0x140709d76
00709AED  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00709AF3  48 8D 0D 66 7C 8B 00            lea rcx, [rip + 0x8b7c66]
00709AFA  45 33 C9                        xor r9d, r9d
00709AFD  45 33 C0                        xor r8d, r8d
00709B00  41 8D 51 07                     lea edx, [r9 + 7]
00709B04  E8 A7 4B B0 FF                  call 0x14020e6b0
00709B09  80 7D EA 00                     cmp byte ptr [rbp - 0x16], 0
00709B0D  4C 8B 6D FF                     mov r13, qword ptr [rbp - 1]
00709B11  74 4B                           je 0x140709b5e
00709B13  8B 55 F3                        mov edx, dword ptr [rbp - 0xd]
00709B16  49 8B CD                        mov rcx, r13
00709B19  E8 42 A9 E4 FF                  call 0x140554460
00709B1E  48 8B F8                        mov rdi, rax
00709B21  48 85 C0                        test rax, rax
00709B24  74 38                           je 0x140709b5e
00709B26  8B 45 EF                        mov eax, dword ptr [rbp - 0x11]
00709B29  3B 87 E8 00 00 00               cmp eax, dword ptr [rdi + 0xe8]
00709B2F  76 06                           jbe 0x140709b37
00709B31  89 87 E8 00 00 00               mov dword ptr [rdi + 0xe8], eax
00709B37  49 8B 46 38                     mov rax, qword ptr [r14 + 0x38]
00709B3B  45 33 C9                        xor r9d, r9d
00709B3E  48 89 87 C8 01 00 00            mov qword ptr [rdi + 0x1c8], rax
00709B45  BA 00 00 02 00                  mov edx, 0x20000
00709B4A  4C 8B 05 E7 D1 8B 00            mov r8, qword ptr [rip + 0x8bd1e7]
00709B51  48 8B CF                        mov rcx, rdi
00709B54  E8 A7 F1 D2 FF                  call 0x140438d00
00709B59  E9 07 02 00 00                  jmp 0x140709d65
00709B5E  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00709B62  E8 25 61 E3 FF                  call 0x14053fc8c
00709B67  48 8B F0                        mov rsi, rax
00709B6A  48 85 C0                        test rax, rax
00709B6D  74 1D                           je 0x140709b8c
00709B6F  48 8B C8                        mov rcx, rax
00709B72  E8 15 51 CD FF                  call 0x1403dec8c
00709B77  83 F8 03                        cmp eax, 3
00709B7A  0F 84 AD 00 00 00               je 0x140709c2d
00709B80  48 8B CE                        mov rcx, rsi
00709B83  E8 C8 F7 BE FF                  call 0x1402f9350
00709B88  C6 45 E9 01                     mov byte ptr [rbp - 0x17], 1
00709B8C  8B 7D EB                        mov edi, dword ptr [rbp - 0x15]
00709B8F  80 3D 0A 7D 8B 00 00            cmp byte ptr [rip + 0x8b7d0a], 0
00709B96  8B 4D EF                        mov ecx, dword ptr [rbp - 0x11]
00709B99  74 0F                           je 0x140709baa
00709B9B  8B 05 03 7D 8B 00               mov eax, dword ptr [rip + 0x8b7d03]
00709BA1  3B C8                           cmp ecx, eax
00709BA3  73 05                           jae 0x140709baa
00709BA5  8B C8                           mov ecx, eax
00709BA7  89 45 EF                        mov dword ptr [rbp - 0x11], eax
00709BAA  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
00709BAE  48 8D 45 EF                     lea rax, [rbp - 0x11]
00709BB2  44 8A 4D 67                     mov r9b, byte ptr [rbp + 0x67]
00709BB6  44 8B C7                        mov r8d, edi
00709BB9  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00709BBE  41 8B D7                        mov edx, r15d
00709BC1  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
00709BC7  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00709BCA  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00709BCF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00709BD3  8B 45 F7                        mov eax, dword ptr [rbp - 9]
00709BD6  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00709BDB  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00709BDF  8A 45 E7                        mov al, byte ptr [rbp - 0x19]
00709BE2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00709BE6  8A 45 E8                        mov al, byte ptr [rbp - 0x18]
00709BE9  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00709BED  43 8A 04 26                     mov al, byte ptr [r14 + r12]
00709BF1  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00709BF5  E8 A6 CA FF FF                  call 0x1407066a0
00709BFA  48 8B F8                        mov rdi, rax
00709BFD  48 85 C0                        test rax, rax
00709C00  0F 84 C2 00 00 00               je 0x140709cc8
00709C06  80 7D EA 00                     cmp byte ptr [rbp - 0x16], 0
00709C0A  8A 45 E9                        mov al, byte ptr [rbp - 0x17]
00709C0D  88 87 0C 02 00 00               mov byte ptr [rdi + 0x20c], al
00709C13  0F 85 D7 00 00 00               jne 0x140709cf0
00709C19  48 8B CF                        mov rcx, rdi
00709C1C  48 89 B7 10 02 00 00            mov qword ptr [rdi + 0x210], rsi
00709C23  E8 A8 5F E3 FF                  call 0x14053fbd0
00709C28  E9 09 01 00 00                  jmp 0x140709d36
00709C2D  43 80 3C 26 00                  cmp byte ptr [r14 + r12], 0
00709C32  8B 7D EB                        mov edi, dword ptr [rbp - 0x15]
00709C35  74 52                           je 0x140709c89
00709C37  8A 86 BA 01 00 00               mov al, byte ptr [rsi + 0x1ba]
00709C3D  41 38 46 05                     cmp byte ptr [r14 + 5], al
00709C41  75 46                           jne 0x140709c89
00709C43  8A 86 BC 01 00 00               mov al, byte ptr [rsi + 0x1bc]
00709C49  41 38 46 09                     cmp byte ptr [r14 + 9], al
00709C4D  75 3A                           jne 0x140709c89
00709C4F  3B BE C0 01 00 00               cmp edi, dword ptr [rsi + 0x1c0]
00709C55  75 32                           jne 0x140709c89
00709C57  80 BE B8 01 00 00 00            cmp byte ptr [rsi + 0x1b8], 0
00709C5E  48 8B FE                        mov rdi, rsi
00709C61  0F 85 FE 00 00 00               jne 0x140709d65
00709C67  41 8B C7                        mov eax, r15d
00709C6A  C1 E8 0C                        shr eax, 0xc
00709C6D  FF C0                           inc eax
00709C6F  89 45 EF                        mov dword ptr [rbp - 0x11], eax
00709C72  3B 86 E8 00 00 00               cmp eax, dword ptr [rsi + 0xe8]
00709C78  0F 86 E7 00 00 00               jbe 0x140709d65
00709C7E  89 86 E8 00 00 00               mov dword ptr [rsi + 0xe8], eax
00709C84  E9 DC 00 00 00                  jmp 0x140709d65
00709C89  48 8B 8E 00 02 00 00            mov rcx, qword ptr [rsi + 0x200]
00709C90  E8 A7 88 E4 FF                  call 0x14055253c
00709C95  84 C0                           test al, al
00709C97  74 27                           je 0x140709cc0
00709C99  83 BE 08 02 00 00 03            cmp dword ptr [rsi + 0x208], 3
00709CA0  74 1E                           je 0x140709cc0
00709CA2  83 7D 77 03                     cmp dword ptr [rbp + 0x77], 3
00709CA6  74 18                           je 0x140709cc0
00709CA8  48 8B CE                        mov rcx, rsi
00709CAB  C6 86 0C 02 00 00 01            mov byte ptr [rsi + 0x20c], 1
00709CB2  E8 99 F6 BE FF                  call 0x1402f9350
00709CB7  C6 45 E9 01                     mov byte ptr [rbp - 0x17], 1
00709CBB  E9 CF FE FF FF                  jmp 0x140709b8f
00709CC0  48 8B CE                        mov rcx, rsi
00709CC3  E8 88 F6 BE FF                  call 0x1402f9350
00709CC8  45 33 C0                        xor r8d, r8d
00709CCB  48 8D 0D 8E 7A 8B 00            lea rcx, [rip + 0x8b7a8e]
00709CD2  33 D2                           xor edx, edx
00709CD4  E8 37 56 C3 FF                  call 0x14033f310
00709CD9  33 C0                           xor eax, eax
00709CDB  48 81 C4 A8 00 00 00            add rsp, 0xa8
00709CE2  41 5F                           pop r15
00709CE4  41 5E                           pop r14
00709CE6  41 5D                           pop r13
00709CE8  41 5C                           pop r12
00709CEA  5F                              pop rdi
00709CEB  5E                              pop rsi
00709CEC  5B                              pop rbx
00709CED  5D                              pop rbp
00709CEE  C3                              ret
00709CEF  CC                              int3
00709CF0  48 8B D7                        mov rdx, rdi
00709CF3  49 8B CD                        mov rcx, r13
00709CF6  E8 E5 A2 E4 FF                  call 0x140553fe0
00709CFB  8B 45 F3                        mov eax, dword ptr [rbp - 0xd]
00709CFE  45 33 C9                        xor r9d, r9d
00709D01  89 87 80 01 00 00               mov dword ptr [rdi + 0x180], eax
00709D07  BA 00 00 02 00                  mov edx, 0x20000
00709D0C  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00709D10  48 8B CF                        mov rcx, rdi
00709D13  89 87 7C 01 00 00               mov dword ptr [rdi + 0x17c], eax
00709D19  4C 89 AF 70 01 00 00            mov qword ptr [rdi + 0x170], r13
00709D20  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
00709D24  89 87 C4 01 00 00               mov dword ptr [rdi + 0x1c4], eax
00709D2A  4C 8B 05 07 D0 8B 00            mov r8, qword ptr [rip + 0x8bd007]
00709D31  E8 CA EF D2 FF                  call 0x140438d00
00709D36  8B 45 EF                        mov eax, dword ptr [rbp - 0x11]
00709D39  85 C0                           test eax, eax
00709D3B  74 0A                           je 0x140709d47
00709D3D  89 87 E8 00 00 00               mov dword ptr [rdi + 0xe8], eax
00709D43  B0 01                           mov al, 1
00709D45  EB 10                           jmp 0x140709d57
00709D47  41 8B C7                        mov eax, r15d
00709D4A  C1 E8 0C                        shr eax, 0xc
00709D4D  FF C0                           inc eax
00709D4F  89 87 E8 00 00 00               mov dword ptr [rdi + 0xe8], eax
00709D55  32 C0                           xor al, al
00709D57  88 87 B8 01 00 00               mov byte ptr [rdi + 0x1b8], al
00709D5D  48 83 A7 38 01 00 00 00         and qword ptr [rdi + 0x138], 0
00709D65  45 33 C0                        xor r8d, r8d
00709D68  48 8D 0D F1 79 8B 00            lea rcx, [rip + 0x8b79f1]
00709D6F  33 D2                           xor edx, edx
00709D71  E8 9A 55 C3 FF                  call 0x14033f310
00709D76  41 8A 46 07                     mov al, byte ptr [r14 + 7]
00709D7A  88 87 BB 01 00 00               mov byte ptr [rdi + 0x1bb], al
00709D80  C6 87 BC 01 00 00 00            mov byte ptr [rdi + 0x1bc], 0
00709D87  41 83 3E 01                     cmp dword ptr [r14], 1
00709D8B  72 0A                           jb 0x140709d97
00709D8D  41 8A 46 09                     mov al, byte ptr [r14 + 9]
00709D91  88 87 BC 01 00 00               mov byte ptr [rdi + 0x1bc], al
00709D97  83 7D 77 02                     cmp dword ptr [rbp + 0x77], 2
00709D9B  75 12                           jne 0x140709daf
00709D9D  80 BF B8 01 00 00 00            cmp byte ptr [rdi + 0x1b8], 0
00709DA4  75 09                           jne 0x140709daf
00709DA6  41 C1 EF 0C                     shr r15d, 0xc
00709DAA  41 FF C7                        inc r15d
00709DAD  EB 07                           jmp 0x140709db6
00709DAF  44 8B BF E8 00 00 00            mov r15d, dword ptr [rdi + 0xe8]
00709DB6  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00709DBA  44 89 38                        mov dword ptr [rax], r15d
00709DBD  48 8B 45 07                     mov rax, qword ptr [rbp + 7]
00709DC1  48 89 87 30 01 00 00            mov qword ptr [rdi + 0x130], rax
00709DC8  48 8B C7                        mov rax, rdi
00709DCB  E9 0B FF FF FF                  jmp 0x140709cdb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalGetAdapterV3(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m75;
    unsigned __int8 v_stack_m76;
    unsigned __int8 v_stack_m77;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int8 v_stack_mB8;
    unsigned __int8 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (168);
    v_r10 = 0;
    v_stack_m78 = 0;
    if ((*(unsigned __int8 *)(v_rip + 9142329)) != 0) { a3 = 0; }
    v_stack_m58 = 0;
    v_stack_p18 = (unsigned int)(a3);
    v_stack_m76 = 0;
    if ((*(unsigned int *)(a1)) != 3) goto loc_0070988F;
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    goto loc_007098CD;
loc_0070988F:
    if ((*(unsigned int *)(a1)) >= 3) goto loc_00709CD9;
    if ((unsigned int)(a3) == 0) goto loc_00709CD9;
    if ((*(unsigned __int8 *)(a1 + 4)) == 0) goto loc_00709CD9;
    if ((*(unsigned __int8 *)(a1 + 11)) == 0) goto loc_007098B3;
    v_stack_m74 = (unsigned int)(v_r10 + 64);
    goto loc_007098CD;
loc_007098B3:
    if ((*(unsigned __int8 *)(a1 + 8)) != 0) goto loc_007098C6;
    v_stack_m74 = 24;
    if ((*(unsigned __int8 *)(a1 + 5)) != 0) {
        v_stack_m74 = 32;
    }
    if (a2 == 0) goto loc_00709CD9;
    v_stack_m6C = 0;
    if ((*(unsigned __int8 *)(a1 + 4 * 1)) != 0) goto loc_00709975;
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    v_stack_m75 = 1;
    result = HalpFindDmaControllerByRequestLine((unsigned int)(*(unsigned int *)(a1 + 48)), a2, a3, a2);
    v_stack_m60 = result;
    if (result == 0) goto loc_00709CD9;
    result = HalpFindAdapterByRequestLine(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))), a3, a2);
    v_r10 = 0;
    if (result != 0) goto loc_00709941;
    result = HalpDmaControllerValidateRequestLineBinding(result, a1, a3, a2);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00709CD9;
loc_00709941:
loc_00709945:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) + (0xFFFULL));
    v_r15 = (unsigned int)((v_r15) & (0xFFFFF000ULL));
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4 * 1)) == 0) goto loc_00709982;
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 5));
    v_stack_m68 = 0;
    goto loc_0070999E;
loc_00709975:
    v_stack_m75 = 0;
    v_stack_m60 = 0;
    goto loc_00709945;
loc_00709982:
    v_stack_p8 = 1;
    a2 = (unsigned int)(*(unsigned int *)(0 + 48));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 48)))) > 8) { a2 = 8; }
    v_stack_m68 = (unsigned int)(a2);
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 76)));
loc_0070999E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 76)))) < 32) goto loc_007099AB;
    goto loc_007099B6;
loc_007099AB:
    v_stack_m77 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4 * 1)) != 0) {
        v_stack_m77 = 1;
    }
    result = HalpGetCacheCoherency(v_stack_m60, v_stack_p10, v_stack_m78, v_stack_p10);
    if (((unsigned int)((unsigned int)(v_stack_m74))) < ((unsigned int)(v_r10 + 64))) goto loc_007099D7;
    result = ((unsigned int)(v_stack_m74)) | (-1);
    goto loc_007099E4;
loc_007099D7:
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(result))));
    result = (result) - 1;
loc_007099E4:
    result = (result >= (*(unsigned __int64 *)(v_rip + 9151005))) ? 1 : 0;
    if ((*(unsigned __int8 *)(v_rip + 9141927)) == 0) goto loc_00709A0B;
    a1 = 0;
loc_007099FD:
loc_00709A00:
    if (0 != 0) goto loc_00709A32;
    goto loc_00709A44;
loc_00709A0B:
    if ((unsigned __int8)(result) == 0) goto loc_007099FD;
    if ((unsigned __int8)(v_stack_m78) == 0) goto loc_007099FD;
    if ((unsigned __int8)(v_stack_p8) == 0) goto loc_00709A00;
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_00709A29;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 2) goto loc_007099FD;
loc_00709A29:
    a1 = 0;
    v_stack_m70 = 0;
    result = 0;
    goto loc_00709A86;
loc_00709A32:
    if ((unsigned __int8)((unsigned int)(v_stack_p18)) == 0) goto loc_00709A44;
    if ((unsigned __int8)(v_stack_m78) != 0) goto loc_00709A3F;
    v_rsi = 0 + 16;
    if (0 == 0) {
        v_rsi = 512;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (12));
    a1 = (unsigned int)((a1) + 1);
    v_stack_m70 = (unsigned int)(a1);
    if (((unsigned int)(a1)) >= = ((unsigned int)(v_rsi))) {
        a1 = (unsigned int)(v_rsi);
        a3 = (unsigned int)(v_rsi);
        v_stack_m70 = (unsigned int)(a1);
    }
    a2 = (unsigned int)(*(unsigned int *)(v_rip + 9151364));
    if (0 == 0) { a2 = *(unsigned int *)(v_rip + 9151095); }
    if (v_stack_m77 != 0) goto loc_00709A86;
    a2 = (unsigned int)((a2) >> (13));
    result = (unsigned int)((unsigned int)(a3));
    if (((unsigned int)(a3)) >= = ((unsigned int)(a2))) {
        a1 = (unsigned int)(a2);
        v_stack_m70 = (unsigned int)(a2);
        result = (unsigned int)(a2);
    }
    if ((unsigned __int8)(v_stack_m78) != 0) goto loc_00709AB3;
    a4 = 0;
    result = (unsigned int)((result) << (12));
    a3 = 0;
    a1 = 0;
    result = IoAllocateMdl(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00709CD9;
loc_00709AB3:
    if (result == 0) goto loc_00709AED;
    if (((unsigned int)((unsigned int)(v_stack_m70))) >= = (*(unsigned int *)(result + 232))) {
        *(unsigned int *)(result + 232) = (unsigned int)((unsigned int)(v_stack_m70));
    }
    a4 = 0;
    *(unsigned __int64 *)(result + 456) = *(unsigned __int64 *)(a1 + 56);
    result = ObReferenceObjectByPointer(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9163352), a4);
    goto loc_00709D76;
loc_00709AED:
    a4 = 0;
    a3 = 0;
    result = KeWaitForSingleObject(v_rip + 9141350, a4 + 7, a3, a4);
    if (v_stack_m75 == 0) goto loc_00709B5E;
    result = HalpFindAdapterByRequestLine(v_stack_m60, (unsigned int)(v_stack_m6C), a3, a4);
    if (result == 0) goto loc_00709B5E;
    if (((unsigned int)((unsigned int)(v_stack_m70))) >= = (*(unsigned int *)(result + 232))) {
        *(unsigned int *)(result + 232) = (unsigned int)((unsigned int)(v_stack_m70));
    }
    a4 = 0;
    *(unsigned __int64 *)(result + 456) = *(unsigned __int64 *)(a1 + 56);
    result = ObReferenceObjectByPointer(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9163239), a4);
    goto loc_00709D65;
loc_00709B5E:
    result = HalpDmaFindAdapterByDeviceObject(v_stack_p10, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9163239), a4);
    if (result == 0) goto loc_00709B8C;
    result = HalpDmaGetAdapterVersion(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9163239), a4);
    if (((unsigned int)(result)) == 3) goto loc_00709C2D;
    result = ObfDereferenceObject(result, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9163239), a4);
    v_stack_m76 = 1;
loc_00709B8C:
loc_00709B8F:
    if ((*(unsigned __int8 *)(v_rip + 9141514)) == 0) goto loc_00709BAA;
    if (((unsigned int)((unsigned int)(v_stack_m70))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141507))))) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141507)));
        v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141507)));
    }
    v_stack_m88 = v_stack_m70;
    v_stack_m98 = v_stack_p10;
    v_stack_mA0 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 56);
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_m68));
    v_stack_mB8 = (unsigned __int8)(v_stack_m78);
    v_stack_mC0 = (unsigned __int8)(v_stack_m77);
    v_stack_mC8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 4 * 1));
    result = HalpDmaAllocateChildAdapterV3(a1, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_p8);
    if (result == 0) goto loc_00709CC8;
    *(unsigned __int8 *)(result + 524) = (unsigned __int8)(v_stack_m76);
    if (v_stack_m75 != 0) goto loc_00709CF0;
    *(unsigned __int64 *)(result + 528) = v_stack_p10;
    result = HalpAddAdapterToList(result, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_p8);
    goto loc_00709D36;
loc_00709C2D:
    if ((*(unsigned __int8 *)(a1 + 4 * 1)) == 0) goto loc_00709C89;
    if ((*(unsigned __int8 *)(a1 + 5)) != ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 442)))) goto loc_00709C89;
    if ((*(unsigned __int8 *)(a1 + 9)) != ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 + 444)))) goto loc_00709C89;
    if (((unsigned int)((unsigned int)(v_stack_m74))) != (*(unsigned int *)(v_stack_p10 + 448))) goto loc_00709C89;
    if ((*(unsigned __int8 *)(v_stack_p10 + 440)) != 0) goto loc_00709D65;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (12));
    result = (unsigned int)((result) + 1);
    v_stack_m70 = (unsigned int)(result);
    if (((unsigned int)(result)) <= (*(unsigned int *)(v_stack_p10 + 232))) goto loc_00709D65;
    *(unsigned int *)(v_stack_p10 + 232) = (unsigned int)(result);
    goto loc_00709D65;
loc_00709C89:
    result = HalpDmaIsAutomaticDomain(*(unsigned __int64 *)(v_stack_p10 + 512), (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_p8);
    if ((unsigned __int8)(result) == 0) goto loc_00709CC0;
    if ((*(unsigned int *)(v_stack_p10 + 520)) == 3) goto loc_00709CC0;
    if (v_stack_p18 == 3) goto loc_00709CC0;
    *(unsigned __int8 *)(v_stack_p10 + 524) = 1;
    result = ObfDereferenceObject(v_stack_p10, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_p8);
    v_stack_m76 = 1;
    goto loc_00709B8F;
loc_00709CC0:
    result = ObfDereferenceObject(v_stack_p10, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), v_stack_p8);
loc_00709CC8:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 9140878, a2, a3, v_stack_p8);
loc_00709CD9:
    result = 0;
loc_00709CDB:
    v_rsp = (v_rsp) + (168);
    return result;
loc_00709CF0:
    result = HalpAddAdapterToSystemList(v_stack_m60, v_stack_p10, a3, v_stack_p8);
    a4 = 0;
    *(unsigned int *)(v_stack_p10 + 384) = (unsigned int)((unsigned int)(v_stack_m6C));
    *(unsigned int *)(v_stack_p10 + 380) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(v_stack_p10 + 368) = v_stack_m60;
    *(unsigned int *)(v_stack_p10 + 452) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    result = ObReferenceObjectByPointer(v_stack_p10, (unsigned int)(0x20000ULL), *(unsigned __int64 *)(v_rip + 9162759), a4);
loc_00709D36:
    if ((unsigned int)((unsigned int)(v_stack_m70)) == 0) goto loc_00709D47;
    *(unsigned int *)(v_stack_p10 + 232) = (unsigned int)((unsigned int)(v_stack_m70));
    goto loc_00709D57;
loc_00709D47:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (12));
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(v_stack_p10 + 232) = (unsigned int)(result);
    result = 0;
loc_00709D57:
    *(unsigned __int8 *)(v_stack_p10 + 440) = 0;
loc_00709D65:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 9140721, a2, a3, a4);
loc_00709D76:
    *(unsigned __int8 *)(v_stack_p10 + 443) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
    *(unsigned __int8 *)(v_stack_p10 + 444) = 0;
    result = *(unsigned __int8 *)(a1 + 7);
    if ((*(unsigned int *)(a1)) >= 1) {
        result = *(unsigned __int8 *)(a1 + 9);
        *(unsigned __int8 *)(v_stack_p10 + 444) = (unsigned __int8)(result);
    }
    if (v_stack_p18 != 2) goto loc_00709DAF;
    if ((*(unsigned __int8 *)(v_stack_p10 + 440)) != 0) goto loc_00709DAF;
    v_r15 = (unsigned int)((v_r15) >> (12));
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_00709DB6;
loc_00709DAF:
loc_00709DB6:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 232)));
    *(unsigned __int64 *)(v_stack_p10 + 304) = v_stack_m58;
    goto loc_00709CDB;
}
```

## 5. (Beta) C Style

```c
int64_t HalGetAdapterV3(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m75;
    uint8_t v_stack_m76;
    uint8_t v_stack_m77;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint8_t v_stack_mB8;
    uint8_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (168);
    local_r10 = 0;
    v_stack_m78 = 0;
    if ((*(uint8_t *)(v_rip + 0x8B8039)) != 0) { Arg3 = 0; }
    v_stack_m58 = 0;
    v_stack_p18 = (uint32_t)(Arg3);
    v_stack_m76 = 0;
    if ((*(uint32_t *)(arg1)) != 3) goto loc_0070988F;
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    goto loc_007098CD;
loc_0070988F:
    if ((*(uint32_t *)(arg1)) >= 3) goto loc_00709CD9;
    if ((uint32_t)(Arg3) == 0) goto loc_00709CD9;
    if ((*(uint8_t *)(arg1 + 0x4)) == 0) goto loc_00709CD9;
    if ((*(uint8_t *)(arg1 + 0xB)) == 0) goto loc_007098B3;
    v_stack_m74 = (uint32_t)(local_r10 + 64);
    goto loc_007098CD;
loc_007098B3:
    if ((*(uint8_t *)(arg1 + 0x8)) != 0) goto loc_007098C6;
    v_stack_m74 = 24;
    if ((*(uint8_t *)(arg1 + 0x5)) != 0) {
        v_stack_m74 = 32;
    }
    if (Arg2 == 0) goto loc_00709CD9;
    v_stack_m6C = 0;
    if ((*(uint8_t *)(arg1 + 0x4 * 1)) != 0) goto loc_00709975;
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    v_stack_m75 = 1;
    result = HalpFindDmaControllerByRequestLine((uint32_t)(*(uint32_t *)(arg1 + 0x30)), Arg2, Arg3, Arg2);
    v_stack_m60 = result;
    if (result == 0) goto loc_00709CD9;
    result = HalpFindAdapterByRequestLine(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))), Arg3, Arg2);
    local_r10 = 0;
    if (result != 0) goto loc_00709941;
    result = HalpDmaControllerValidateRequestLineBinding(result, Arg1, Arg3, Arg2);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00709CD9;
loc_00709941:
loc_00709945:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) + (0xFFFULL));
    local_r15 = (uint32_t)((local_r15) & (0xFFFFF000ULL));
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x4 * 1)) == 0) goto loc_00709982;
    v_stack_p8 = (uint8_t)(*(uint8_t *)(arg1 + 0x5));
    v_stack_m68 = 0;
    goto loc_0070999E;
loc_00709975:
    v_stack_m75 = 0;
    v_stack_m60 = 0;
    goto loc_00709945;
loc_00709982:
    v_stack_p8 = 1;
    Arg2 = (uint32_t)(*(uint32_t *)(0 + 0x30));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x30)))) > 8) { Arg2 = 8; }
    v_stack_m68 = (uint32_t)(Arg2);
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4C)));
loc_0070999E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4C)))) < 32) goto loc_007099AB;
    goto loc_007099B6;
loc_007099AB:
    v_stack_m77 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x4 * 1)) != 0) {
        v_stack_m77 = 1;
    }
    result = HalpGetCacheCoherency(v_stack_m60, v_stack_p10, v_stack_m78, v_stack_p10);
    if (((uint32_t)((uint32_t)(v_stack_m74))) < ((uint32_t)(local_r10 + 64))) goto loc_007099D7;
    result = ((uint32_t)(v_stack_m74)) | (-1);
    goto loc_007099E4;
loc_007099D7:
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)(result))));
    result = (result) - 1;
loc_007099E4:
    result = (result >= (*(uint64_t *)(v_rip + 0x8BA21D))) ? 1 : 0;
    if ((*(uint8_t *)(v_rip + 0x8B7EA7)) == 0) goto loc_00709A0B;
    Arg1 = 0;
loc_007099FD:
loc_00709A00:
    if (0 != 0) goto loc_00709A32;
    goto loc_00709A44;
loc_00709A0B:
    if ((uint8_t)(result) == 0) goto loc_007099FD;
    if ((uint8_t)(v_stack_m78) == 0) goto loc_007099FD;
    if ((uint8_t)(v_stack_p8) == 0) goto loc_00709A00;
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_00709A29;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 2) goto loc_007099FD;
loc_00709A29:
    Arg1 = 0;
    v_stack_m70 = 0;
    result = 0;
    goto loc_00709A86;
loc_00709A32:
    if ((uint8_t)((uint32_t)(v_stack_p18)) == 0) goto loc_00709A44;
    if ((uint8_t)(v_stack_m78) != 0) goto loc_00709A3F;
    local_rsi = 0 + 16;
    if (0 == 0) {
        local_rsi = 512;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (12));
    Arg1 = (uint32_t)((Arg1) + 1);
    v_stack_m70 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) >= = ((uint32_t)(local_rsi))) {
        Arg1 = (uint32_t)(local_rsi);
        Arg3 = (uint32_t)(local_rsi);
        v_stack_m70 = (uint32_t)(Arg1);
    }
    Arg2 = (uint32_t)(*(uint32_t *)(v_rip + 0x8BA384));
    if (0 == 0) { Arg2 = *(uint32_t *)(v_rip + 0x8BA277); }
    if (v_stack_m77 != 0) goto loc_00709A86;
    Arg2 = (uint32_t)((Arg2) >> (13));
    result = (uint32_t)((uint32_t)(Arg3));
    if (((uint32_t)(Arg3)) >= = ((uint32_t)(Arg2))) {
        Arg1 = (uint32_t)(Arg2);
        v_stack_m70 = (uint32_t)(Arg2);
        result = (uint32_t)(Arg2);
    }
    if ((uint8_t)(v_stack_m78) != 0) goto loc_00709AB3;
    Arg4 = 0;
    result = (uint32_t)((result) << (12));
    Arg3 = 0;
    Arg1 = 0;
    result = IoAllocateMdl(Arg1, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00709CD9;
loc_00709AB3:
    if (result == 0) goto loc_00709AED;
    if (((uint32_t)((uint32_t)(v_stack_m70))) >= = (*(uint32_t *)(result + 0xE8))) {
        *(uint32_t *)(result + 0xE8) = (uint32_t)((uint32_t)(v_stack_m70));
    }
    Arg4 = 0;
    *(uint64_t *)(result + 0x1C8) = *(uint64_t *)(arg1 + 0x38);
    result = ObReferenceObjectByPointer(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD258), Arg4);
    goto loc_00709D76;
loc_00709AED:
    Arg4 = 0;
    Arg3 = 0;
    result = KeWaitForSingleObject(v_rip + 9141350, Arg4 + 7, Arg3, Arg4);
    if (v_stack_m75 == 0) goto loc_00709B5E;
    result = HalpFindAdapterByRequestLine(v_stack_m60, (uint32_t)(v_stack_m6C), Arg3, Arg4);
    if (result == 0) goto loc_00709B5E;
    if (((uint32_t)((uint32_t)(v_stack_m70))) >= = (*(uint32_t *)(result + 0xE8))) {
        *(uint32_t *)(result + 0xE8) = (uint32_t)((uint32_t)(v_stack_m70));
    }
    Arg4 = 0;
    *(uint64_t *)(result + 0x1C8) = *(uint64_t *)(arg1 + 0x38);
    result = ObReferenceObjectByPointer(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD1E7), Arg4);
    goto loc_00709D65;
loc_00709B5E:
    result = HalpDmaFindAdapterByDeviceObject(v_stack_p10, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD1E7), Arg4);
    if (result == 0) goto loc_00709B8C;
    result = HalpDmaGetAdapterVersion(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD1E7), Arg4);
    if (((uint32_t)(result)) == 3) goto loc_00709C2D;
    result = ObfDereferenceObject(result, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD1E7), Arg4);
    v_stack_m76 = 1;
loc_00709B8C:
loc_00709B8F:
    if ((*(uint8_t *)(v_rip + 0x8B7D0A)) == 0) goto loc_00709BAA;
    if (((uint32_t)((uint32_t)(v_stack_m70))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D03))))) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D03)));
        v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D03)));
    }
    v_stack_m88 = v_stack_m70;
    v_stack_m98 = v_stack_p10;
    v_stack_mA0 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x38);
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_m68));
    v_stack_mB8 = (uint8_t)(v_stack_m78);
    v_stack_mC0 = (uint8_t)(v_stack_m77);
    v_stack_mC8 = (uint8_t)(*(uint8_t *)(arg1 + 0x4 * 1));
    result = HalpDmaAllocateChildAdapterV3(Arg1, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_p8);
    if (result == 0) goto loc_00709CC8;
    *(uint8_t *)(result + 0x20C) = (uint8_t)(v_stack_m76);
    if (v_stack_m75 != 0) goto loc_00709CF0;
    *(uint64_t *)(result + 0x210) = v_stack_p10;
    result = HalpAddAdapterToList(result, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_p8);
    goto loc_00709D36;
loc_00709C2D:
    if ((*(uint8_t *)(arg1 + 0x4 * 1)) == 0) goto loc_00709C89;
    if ((*(uint8_t *)(arg1 + 0x5)) != ((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x1BA)))) goto loc_00709C89;
    if ((*(uint8_t *)(arg1 + 0x9)) != ((uint8_t)(*(uint8_t *)(v_stack_p10 + 0x1BC)))) goto loc_00709C89;
    if (((uint32_t)((uint32_t)(v_stack_m74))) != (*(uint32_t *)(v_stack_p10 + 0x1C0))) goto loc_00709C89;
    if ((*(uint8_t *)(v_stack_p10 + 0x1B8)) != 0) goto loc_00709D65;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (12));
    result = (uint32_t)((result) + 1);
    v_stack_m70 = (uint32_t)(result);
    if (((uint32_t)(result)) <= (*(uint32_t *)(v_stack_p10 + 0xE8))) goto loc_00709D65;
    *(uint32_t *)(v_stack_p10 + 0xE8) = (uint32_t)(result);
    goto loc_00709D65;
loc_00709C89:
    result = HalpDmaIsAutomaticDomain(*(uint64_t *)(v_stack_p10 + 0x200), (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_p8);
    if ((uint8_t)(result) == 0) goto loc_00709CC0;
    if ((*(uint32_t *)(v_stack_p10 + 0x208)) == 3) goto loc_00709CC0;
    if (v_stack_p18 == 3) goto loc_00709CC0;
    *(uint8_t *)(v_stack_p10 + 0x20C) = 1;
    result = ObfDereferenceObject(v_stack_p10, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_p8);
    v_stack_m76 = 1;
    goto loc_00709B8F;
loc_00709CC0:
    result = ObfDereferenceObject(v_stack_p10, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), v_stack_p8);
loc_00709CC8:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 9140878, Arg2, Arg3, v_stack_p8);
loc_00709CD9:
    result = 0;
loc_00709CDB:
    local_rsp = (local_rsp) + (168);
    return result;
loc_00709CF0:
    result = HalpAddAdapterToSystemList(v_stack_m60, v_stack_p10, Arg3, v_stack_p8);
    Arg4 = 0;
    *(uint32_t *)(v_stack_p10 + 0x180) = (uint32_t)((uint32_t)(v_stack_m6C));
    *(uint32_t *)(v_stack_p10 + 0x17C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(v_stack_p10 + 0x170) = v_stack_m60;
    *(uint32_t *)(v_stack_p10 + 0x1C4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    result = ObReferenceObjectByPointer(v_stack_p10, (uint32_t)(0x20000ULL), *(uint64_t *)(v_rip + 0x8BD007), Arg4);
loc_00709D36:
    if ((uint32_t)((uint32_t)(v_stack_m70)) == 0) goto loc_00709D47;
    *(uint32_t *)(v_stack_p10 + 0xE8) = (uint32_t)((uint32_t)(v_stack_m70));
    goto loc_00709D57;
loc_00709D47:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (12));
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(v_stack_p10 + 0xE8) = (uint32_t)(result);
    result = 0;
loc_00709D57:
    *(uint8_t *)(v_stack_p10 + 0x1B8) = 0;
loc_00709D65:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 9140721, Arg2, Arg3, Arg4);
loc_00709D76:
    *(uint8_t *)(v_stack_p10 + 0x1BB) = (uint8_t)(*(uint8_t *)(arg1 + 0x7));
    *(uint8_t *)(v_stack_p10 + 0x1BC) = 0;
    result = *(uint8_t *)(arg1 + 0x7);
    if ((*(uint32_t *)(arg1)) >= 1) {
        result = *(uint8_t *)(arg1 + 0x9);
        *(uint8_t *)(v_stack_p10 + 0x1BC) = (uint8_t)(result);
    }
    if (v_stack_p18 != 2) goto loc_00709DAF;
    if ((*(uint8_t *)(v_stack_p10 + 0x1B8)) != 0) goto loc_00709DAF;
    local_r15 = (uint32_t)((local_r15) >> (12));
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_00709DB6;
loc_00709DAF:
loc_00709DB6:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xE8)));
    *(uint64_t *)(v_stack_p10 + 0x130) = v_stack_m58;
    goto loc_00709CDB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0 + r12*1` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |
| `Arg1` | `+ 0x7` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00709838&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
