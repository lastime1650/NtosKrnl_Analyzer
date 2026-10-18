# FsRtlAcquireFileForModWriteEx

- RVA: `0x00299E5C`–`0x0029A291` (길이 `1,077` bytes)
- VA: `0x0000000140299E5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00067C9C`
- 디코드: `280`개 명령, `1,077/1,077` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00299EA6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00299EC6` → [IoGetRelatedDeviceObject](IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00299ED1` → [IoGetBaseFileSystemDeviceObject](IoGetBaseFileSystemDeviceObject_function_0029A2A0.md) (function, `0x0029A2A0`)
- `0x00299F7A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00299FA7` → [FsFilterPerformCallbacks](FsFilterPerformCallbacks_function_00299590.md) (function, `0x00299590`)
- `0x0029A000` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0029A03A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0029A092` → [FsFilterPerformCompletionCallbacks](FsFilterPerformCompletionCallbacks_function_00299000.md) (function, `0x00299000`)
- `0x0029A09C` → [FsFilterCtrlFree](FsFilterCtrlFree_function_0029908C.md) (function, `0x0029908C`)
- `0x0029A0B0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0029A11C` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x0029A174` → [ExConvertExclusiveToSharedLite](../34/ExConvertExclusiveToSharedLite_function_0034F700.md) (function, `0x0034F700`)
- `0x0029A18A` → [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) (function, `0x003D43F0`)
- `0x0029A199` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0029A1FA` → [IoGetDeviceAttachmentBaseRefWithTag](../27/IoGetDeviceAttachmentBaseRefWithTag_function_00272788.md) (function, `0x00272788`)
- `0x0029A227` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029A265` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0029A27B` → [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) (function, `0x003D43F0`)

### Direct callers
- [MiGatherMappedPages](../40/MiGatherMappedPages_function_00404E80.md) at `0x004050D4`

### Static image references
- `0x00299E7B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0029A0B0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0029A282` → [sub_006DA8C0](../6D/Unknown_function_006DA8C0.md) (`tail-transfer`)
  - `0x0029A28C` → [sub_006DA8C0](../6D/Unknown_function_006DA8C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00299E5C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00299E61  55                              push rbp
00299E62  56                              push rsi
00299E63  57                              push rdi
00299E64  41 54                           push r12
00299E66  41 55                           push r13
00299E68  41 56                           push r14
00299E6A  41 57                           push r15
00299E6C  48 8D AC 24 60 FE FF FF         lea rbp, [rsp - 0x1a0]
00299E74  48 81 EC A0 02 00 00            sub rsp, 0x2a0
00299E7B  48 8B 05 BE 08 B7 00            mov rax, qword ptr [rip + 0xb708be]
00299E82  48 33 C4                        xor rax, rsp
00299E85  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
00299E8C  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00299E91  4C 8B E9                        mov r13, rcx
00299E94  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00299E99  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00299E9E  33 D2                           xor edx, edx
00299EA0  41 B8 38 02 00 00               mov r8d, 0x238
00299EA6  E8 95 CD 42 00                  call 0x1406c6c40
00299EAB  33 C9                           xor ecx, ecx
00299EAD  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00299EB2  8B D9                           mov ebx, ecx
00299EB4  88 4C 24 31                     mov byte ptr [rsp + 0x31], cl
00299EB8  8B F1                           mov esi, ecx
00299EBA  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00299EBE  49 8B CD                        mov rcx, r13
00299EC1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00299EC6  E8 55 12 00 00                  call 0x14029b120
00299ECB  49 8B CD                        mov rcx, r13
00299ECE  4C 8B E0                        mov r12, rax
00299ED1  E8 CA 03 00 00                  call 0x14029a2a0
00299ED6  4C 8B F8                        mov r15, rax
00299ED9  45 33 C0                        xor r8d, r8d
00299EDC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00299EE0  4C 8B 70 50                     mov r14, qword ptr [rax + 0x50]
00299EE4  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
00299EE8  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
00299EEC  48 85 FF                        test rdi, rdi
00299EEF  74 20                           je 0x140299f11
00299EF1  8B 07                           mov eax, dword ptr [rdi]
00299EF3  83 F8 50                        cmp eax, 0x50
00299EF6  72 0A                           jb 0x140299f02
00299EF8  4C 39 47 48                     cmp qword ptr [rdi + 0x48], r8
00299EFC  0F 85 BF 02 00 00               jne 0x14029a1c1
00299F02  83 F8 58                        cmp eax, 0x58
00299F05  72 0A                           jb 0x140299f11
00299F07  4C 39 47 50                     cmp qword ptr [rdi + 0x50], r8
00299F0B  0F 85 B0 02 00 00               jne 0x14029a1c1
00299F11  8A C3                           mov al, bl
00299F13  4D 3B E7                        cmp r12, r15
00299F16  0F 84 8E 02 00 00               je 0x14029a1aa
00299F1C  33 C0                           xor eax, eax
00299F1E  44 89 45 90                     mov dword ptr [rbp - 0x70], r8d
00299F22  B9 40 00 00 00                  mov ecx, 0x40
00299F27  C6 44 24 54 FD                  mov byte ptr [rsp + 0x54], 0xfd
00299F2C  0F 57 C0                        xorps xmm0, xmm0
00299F2F  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00299F33  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00299F38  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00299F3D  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00299F42  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00299F46  8D 59 CF                        lea ebx, [rcx - 0x31]
00299F49  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00299F4E  41 0F BE 44 24 4C               movsx eax, byte ptr [r12 + 0x4c]
00299F54  66 89 45 98                     mov word ptr [rbp - 0x68], ax
00299F58  66 44 89 45 9A                  mov word ptr [rbp - 0x66], r8w
00299F5D  66 3B C3                        cmp ax, bx
00299F60  0F 87 3D 01 00 00               ja 0x14029a0a3
00299F66  48 8D 45 A8                     lea rax, [rbp - 0x58]
00299F6A  33 D2                           xor edx, edx
00299F6C  41 B8 E0 01 00 00               mov r8d, 0x1e0
00299F72  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00299F76  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00299F7A  E8 C1 CC 42 00                  call 0x1406c6c40
00299F7F  66 89 5D 98                     mov word ptr [rbp - 0x68], bx
00299F83  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00299F88  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00299F8D  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00299F92  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00299F97  41 B0 01                        mov r8b, 1
00299F9A  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00299F9F  41 8A D0                        mov dl, r8b
00299FA2  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00299FA7  E8 E4 F5 FF FF                  call 0x140299590
00299FAC  45 33 C0                        xor r8d, r8d
00299FAF  8B D8                           mov ebx, eax
00299FB1  85 C0                           test eax, eax
00299FB3  0F 89 19 02 00 00               jns 0x14029a1d2
00299FB9  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
00299FBD  EB 59                           jmp 0x14029a018
00299FBF  F6 45 90 04                     test byte ptr [rbp - 0x70], 4
00299FC3  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00299FC8  0F 85 22 02 00 00               jne 0x14029a1f0
00299FCE  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
00299FD2  48 85 FF                        test rdi, rdi
00299FD5  0F 85 87 00 00 00               jne 0x14029a062
00299FDB  4D 85 F6                        test r14, r14
00299FDE  74 7B                           je 0x14029a05b
00299FE0  41 81 3E 80 00 00 00            cmp dword ptr [r14], 0x80
00299FE7  72 72                           jb 0x14029a05b
00299FE9  49 8B 46 78                     mov rax, qword ptr [r14 + 0x78]
00299FED  48 85 C0                        test rax, rax
00299FF0  74 69                           je 0x14029a05b
00299FF2  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00299FF7  4D 8B CF                        mov r9, r15
00299FFA  4D 8B C4                        mov r8, r12
00299FFD  49 8B CD                        mov rcx, r13
0029A000  E8 CB 0A 42 00                  call 0x1406baad0
0029A005  8B D8                           mov ebx, eax
0029A007  45 33 C0                        xor r8d, r8d
0029A00A  83 CE 01                        or esi, 1
0029A00D  44 38 44 24 31                  cmp byte ptr [rsp + 0x31], r8b
0029A012  0F 85 07 02 00 00               jne 0x14029a21f
0029A018  81 FB 10 00 00 C0               cmp ebx, 0xc0000010
0029A01E  0F 84 A7 00 00 00               je 0x14029a0cb
0029A024  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0029A029  48 85 C0                        test rax, rax
0029A02C  75 56                           jne 0x14029a084
0029A02E  8B C3                           mov eax, ebx
0029A030  48 8B 8D 90 01 00 00            mov rcx, qword ptr [rbp + 0x190]
0029A037  48 33 CC                        xor rcx, rsp
0029A03A  E8 01 26 41 00                  call 0x1406ac640
0029A03F  48 8B 9C 24 F8 02 00 00         mov rbx, qword ptr [rsp + 0x2f8]
0029A047  48 81 C4 A0 02 00 00            add rsp, 0x2a0
0029A04E  41 5F                           pop r15
0029A050  41 5E                           pop r14
0029A052  41 5D                           pop r13
0029A054  41 5C                           pop r12
0029A056  5F                              pop rdi
0029A057  5E                              pop rsi
0029A058  5D                              pop rbp
0029A059  C3                              ret
0029A05A  CC                              int3
0029A05B  BB 10 00 00 C0                  mov ebx, 0xc0000010
0029A060  EB A8                           jmp 0x14029a00a
0029A062  8B 07                           mov eax, dword ptr [rdi]
0029A064  83 F8 50                        cmp eax, 0x50
0029A067  72 06                           jb 0x14029a06f
0029A069  4C 39 47 48                     cmp qword ptr [rdi + 0x48], r8
0029A06D  75 9E                           jne 0x14029a00d
0029A06F  83 F8 58                        cmp eax, 0x58
0029A072  0F 82 63 FF FF FF               jb 0x140299fdb
0029A078  4C 39 47 50                     cmp qword ptr [rdi + 0x50], r8
0029A07C  0F 84 59 FF FF FF               je 0x140299fdb
0029A082  EB 89                           jmp 0x14029a00d
0029A084  66 44 39 40 4A                  cmp word ptr [rax + 0x4a], r8w
0029A089  76 0C                           jbe 0x14029a097
0029A08B  8B D3                           mov edx, ebx
0029A08D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0029A092  E8 69 EF FF FF                  call 0x140299000
0029A097  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0029A09C  E8 EB EF FF FF                  call 0x14029908c
0029A0A1  EB 8B                           jmp 0x14029a02e
0029A0A3  0F B7 D0                        movzx edx, ax
0029A0A6  41 B8 46 53 6D 67               mov r8d, 0x676d5346
0029A0AC  48 C1 E2 05                     shl rdx, 5
0029A0B0  E8 3B 80 8E 00                  call 0x140b820f0
0029A0B5  48 85 C0                        test rax, rax
0029A0B8  0F 84 0A 01 00 00               je 0x14029a1c8
0029A0BE  83 4D 90 01                     or dword ptr [rbp - 0x70], 1
0029A0C2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0029A0C6  E9 B8 FE FF FF                  jmp 0x140299f83
0029A0CB  40 F6 C6 01                     test sil, 1
0029A0CF  0F 84 4F FF FF FF               je 0x14029a024
0029A0D5  49 8B 7D 18                     mov rdi, qword ptr [r13 + 0x18]
0029A0D9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0029A0DD  48 85 C0                        test rax, rax
0029A0E0  0F 84 4E 01 00 00               je 0x14029a234
0029A0E6  8A 57 04                        mov dl, byte ptr [rdi + 4]
0029A0E9  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0029A0EE  F6 C2 08                        test dl, 8
0029A0F1  0F 85 50 01 00 00               jne 0x14029a247
0029A0F7  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0029A0FB  49 39 0E                        cmp qword ptr [r14], rcx
0029A0FE  0F 8F 39 01 00 00               jg 0x14029a23d
0029A104  F6 C2 10                        test dl, 0x10
0029A107  74 29                           je 0x14029a132
0029A109  41 8A F0                        mov sil, r8b
0029A10C  48 8B C8                        mov rcx, rax
0029A10F  48 8B D9                        mov rbx, rcx
0029A112  40 84 F6                        test sil, sil
0029A115  74 71                           je 0x14029a188
0029A117  33 D2                           xor edx, edx
0029A119  48 8B CB                        mov rcx, rbx
0029A11C  E8 FF AC F7 FF                  call 0x140214e20
0029A121  45 33 C0                        xor r8d, r8d
0029A124  84 C0                           test al, al
0029A126  75 18                           jne 0x14029a140
0029A128  BB D8 00 00 C0                  mov ebx, 0xc00000d8
0029A12D  E9 F2 FE FF FF                  jmp 0x14029a024
0029A132  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0029A136  48 85 C9                        test rcx, rcx
0029A139  74 CE                           je 0x14029a109
0029A13B  41 8A F0                        mov sil, r8b
0029A13E  EB CF                           jmp 0x14029a10f
0029A140  8A 4F 04                        mov cl, byte ptr [rdi + 4]
0029A143  F6 C1 08                        test cl, 8
0029A146  75 49                           jne 0x14029a191
0029A148  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0029A14C  49 39 06                        cmp qword ptr [r14], rax
0029A14F  7F 40                           jg 0x14029a191
0029A151  F6 C1 10                        test cl, 0x10
0029A154  0F 85 F5 00 00 00               jne 0x14029a24f
0029A15A  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0029A15E  48 85 C9                        test rcx, rcx
0029A161  74 09                           je 0x14029a16c
0029A163  48 3B D9                        cmp rbx, rcx
0029A166  0F 85 0A 01 00 00               jne 0x14029a276
0029A16C  40 84 F6                        test sil, sil
0029A16F  74 0B                           je 0x14029a17c
0029A171  48 8B CB                        mov rcx, rbx
0029A174  E8 87 55 0B 00                  call 0x14034f700
0029A179  45 33 C0                        xor r8d, r8d
0029A17C  49 89 1C 24                     mov qword ptr [r12], rbx
0029A180  41 8B D8                        mov ebx, r8d
0029A183  E9 9C FE FF FF                  jmp 0x14029a024
0029A188  33 D2                           xor edx, edx
0029A18A  E8 61 A2 13 00                  call 0x1403d43f0
0029A18F  EB 90                           jmp 0x14029a121
0029A191  40 84 F6                        test sil, sil
0029A194  75 E6                           jne 0x14029a17c
0029A196  48 8B CB                        mov rcx, rbx
0029A199  E8 72 58 FC FF                  call 0x14025fa10
0029A19E  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
0029A1A2  40 B6 01                        mov sil, 1
0029A1A5  E9 6D FF FF FF                  jmp 0x14029a117
0029A1AA  84 C0                           test al, al
0029A1AC  0F 85 6A FD FF FF               jne 0x140299f1c
0029A1B2  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0029A1B7  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0029A1BC  E9 11 FE FF FF                  jmp 0x140299fd2
0029A1C1  B0 01                           mov al, 1
0029A1C3  E9 4B FD FF FF                  jmp 0x140299f13
0029A1C8  B8 9A 00 00 C0                  mov eax, 0xc000009a
0029A1CD  E9 5E FE FF FF                  jmp 0x14029a030
0029A1D2  0F 84 E7 FD FF FF               je 0x140299fbf
0029A1D8  3D 26 01 00 00                  cmp eax, 0x126
0029A1DD  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0029A1E2  0F 85 9C FE FF FF               jne 0x14029a084
0029A1E8  41 8B D8                        mov ebx, r8d
0029A1EB  E9 94 FE FF FF                  jmp 0x14029a084
0029A1F0  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0029A1F5  BA 44 66 6C 74                  mov edx, 0x746c6644
0029A1FA  E8 89 85 FD FF                  call 0x140272788
0029A1FF  4C 8B F8                        mov r15, rax
0029A202  C6 44 24 31 01                  mov byte ptr [rsp + 0x31], 1
0029A207  45 33 C0                        xor r8d, r8d
0029A20A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0029A20E  4C 8B 70 50                     mov r14, qword ptr [rax + 0x50]
0029A212  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
0029A216  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
0029A21A  E9 AF FD FF FF                  jmp 0x140299fce
0029A21F  BA 44 66 6C 74                  mov edx, 0x746c6644
0029A224  49 8B CF                        mov rcx, r15
0029A227  E8 B4 D6 05 00                  call 0x1402f78e0
0029A22C  45 33 C0                        xor r8d, r8d
0029A22F  E9 E4 FD FF FF                  jmp 0x14029a018
0029A234  4D 89 04 24                     mov qword ptr [r12], r8
0029A238  E9 43 FF FF FF                  jmp 0x14029a180
0029A23D  48 3B 4F 20                     cmp rcx, qword ptr [rdi + 0x20]
0029A241  0F 84 BD FE FF FF               je 0x14029a104
0029A247  40 B6 01                        mov sil, 1
0029A24A  E9 BD FE FF FF                  jmp 0x14029a10c
0029A24F  40 84 F6                        test sil, sil
0029A252  0F 85 19 FF FF FF               jne 0x14029a171
0029A258  48 3B 5F 08                     cmp rbx, qword ptr [rdi + 8]
0029A25C  0F 84 1A FF FF FF               je 0x14029a17c
0029A262  48 8B CB                        mov rcx, rbx
0029A265  E8 A6 57 FC FF                  call 0x14025fa10
0029A26A  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
0029A26E  40 B6 01                        mov sil, 1
0029A271  E9 A1 FE FF FF                  jmp 0x14029a117
0029A276  33 D2                           xor edx, edx
0029A278  49 8B D8                        mov rbx, r8
0029A27B  E8 70 A1 13 00                  call 0x1403d43f0
0029A280  84 C0                           test al, al
0029A282  0F 84 38 06 44 00               je 0x1406da8c0
0029A288  48 8B 5F 10                     mov rbx, qword ptr [rdi + 0x10]
0029A28C  E9 2F 06 44 00                  jmp 0x1406da8c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlAcquireFileForModWriteEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int16 v_stack_m23E;
    unsigned __int16 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m284;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned __int8 v_stack_m2A7;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (672);
    result = (*(unsigned __int64 *)(v_rip + 11995326)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m298 = a3;
    v_stack_m2A0 = a2;
    a2 = 0;
    result = memset(v_stack_m288, a2, 568, a4);
    a1 = 0;
    v_stack_m2A7 = 0;
    v_stack_m2A4 = 0;
    v_stack_m290 = v_stack_m288;
    result = IoGetRelatedDeviceObject(0, a2, 568, a4);
    result = IoGetBaseFileSystemDeviceObject(0, a2, 568, a4);
    a3 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) == 0) goto loc_00299F11;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48))))) < 80) goto loc_00299F02;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 72)) != 0) goto loc_0029A1C1;
loc_00299F02:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48))))) < 88) goto loc_00299F11;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 80)) != 0) goto loc_0029A1C1;
loc_00299F11:
loc_00299F13:
    if (result == result) goto loc_0029A1AA;
loc_00299F1C:
    result = 0;
    v_stack_m248 = 0;
    v_stack_m284 = 253;
    v_stack_m288 = 64;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m270 = v_xmm0;
    v_stack_m250 = 0;
    v_stack_m260 = v_xmm0;
    v_stack_m240 = (unsigned __int16)((__int8)(*(unsigned __int8 *)(result + 76)));
    v_stack_m23E = 0;
    if (((unsigned __int16)((__int8)(*(unsigned __int8 *)(result + 76)))) > ((unsigned __int16)(64 - 49))) goto loc_0029A0A3;
    a2 = 0;
    v_stack_m238 = v_stack_m230;
    result = memset(v_stack_m230, a2, 480, a4);
    v_stack_m240 = (unsigned __int16)(64 - 49);
loc_00299F83:
    v_stack_m270 = v_stack_m2A0;
    v_stack_m268 = v_stack_m298;
    result = FsFilterPerformCallbacks(v_stack_m288, 1, 1, v_stack_m2A4);
    a3 = 0;
    if (!sign_flag) goto loc_0029A1D2;
    goto loc_0029A018;
loc_00299FBF:
    if (((v_stack_m248) & (4)) != 0) goto loc_0029A1F0;
loc_00299FCE:
loc_00299FD2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) != 0) goto loc_0029A062;
loc_00299FDB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) == 0) goto loc_0029A05B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80))) < 128) goto loc_0029A05B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 120) == 0) goto loc_0029A05B;
    result = guard_dispatch_icall(v_stack_m278, v_stack_m2A0, v_stack_m298, result);
    a3 = 0;
loc_0029A00A:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m2A4)) | (1));
loc_0029A00D:
    if (v_stack_m2A7 != 0) goto loc_0029A21F;
loc_0029A018:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000010ULL) goto loc_0029A0CB;
loc_0029A024:
    if (v_stack_m290 != 0) goto loc_0029A084;
loc_0029A02E:
loc_0029A030:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m2A0, a3, result);
    v_rsp = (v_rsp) + (672);
    return result;
loc_0029A05B:
    goto loc_0029A00A;
loc_0029A062:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48))))) < 80) goto loc_0029A06F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 72)) != 0) goto loc_0029A00D;
loc_0029A06F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48))))) < 88) goto loc_00299FDB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 80)) == 0) goto loc_00299FDB;
    goto loc_0029A00D;
loc_0029A084:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48)));
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48))) + 74)) >= = 0) {
        a2 = (unsigned int)((unsigned int)(0xC0000010ULL));
        a1 = v_stack_p50;
        result = FsFilterPerformCompletionCallbacks(a1, a2, a3, result);
    }
    result = FsFilterCtrlFree(v_stack_p50, a2, a3, result);
    goto loc_0029A02E;
loc_0029A0A3:
    a2 = ((unsigned __int16)(result)) << (5);
    result = ExAllocatePool2(v_stack_p50, a2, (unsigned int)(0x676D5346ULL), result);
    if (result == 0) goto loc_0029A1C8;
    v_stack_m238 = result;
    goto loc_00299F83;
loc_0029A0CB:
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_0029A024;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 8) == 0) goto loc_0029A234;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 4))) & (8)) != 0) goto loc_0029A247;
    if ((*(unsigned __int64 *)(v_stack_p38)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 40))) goto loc_0029A23D;
loc_0029A104:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 4))) & (16)) == 0) goto loc_0029A132;
loc_0029A109:
loc_0029A10C:
loc_0029A10F:
    if ((unsigned __int8)((unsigned __int8)((unsigned int)(0x676D5346ULL))) == 0) goto loc_0029A188;
loc_0029A117:
    a2 = 0;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 8), a2, (unsigned int)(0x676D5346ULL), result);
loc_0029A121:
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0029A140;
    goto loc_0029A024;
loc_0029A132:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 16) == 0) goto loc_0029A109;
    goto loc_0029A10F;
loc_0029A140:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 4))) & (8)) != 0) goto loc_0029A191;
    if ((*(unsigned __int64 *)(v_stack_p38)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 40))) goto loc_0029A191;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 4))) & (16)) != 0) goto loc_0029A24F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 16) == 0) goto loc_0029A16C;
    if (((unsigned int)(0xC00000D8ULL)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 16))) goto loc_0029A276;
loc_0029A16C:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m278 + 24) + 40);
    if (0 != 0) {
        a1 = (unsigned int)(0xC00000D8ULL);
        result = ExConvertExclusiveToSharedLite(a1, a2, a3, result);
        a3 = 0;
    }
    *(unsigned __int64 *)(v_stack_m298) = (unsigned int)(0xC00000D8ULL);
loc_0029A180:
    goto loc_0029A024;
loc_0029A188:
    a2 = 0;
    result = ExAcquireSharedWaitForExclusive(a1, a2, a3, result);
    goto loc_0029A121;
loc_0029A191:
    if (0 != 0) goto loc_0029A17C;
    result = ExReleaseResourceLite(0, a2, a3, result);
    goto loc_0029A117;
loc_0029A1AA:
    if ((unsigned __int8)(result) != 0) goto loc_00299F1C;
    v_stack_p48 = 0;
    goto loc_00299FD2;
loc_0029A1C1:
    goto loc_00299F13;
loc_0029A1C8:
    goto loc_0029A030;
loc_0029A1D2:
    if ((unsigned __int8)(result) == 0) goto loc_00299FBF;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) != 294) goto loc_0029A084;
    goto loc_0029A084;
loc_0029A1F0:
    result = IoGetDeviceAttachmentBaseRefWithTag(v_stack_p58, (unsigned int)(0x746C6644ULL), a3, result);
    v_stack_p31 = 1;
    a3 = 0;
    goto loc_00299FCE;
loc_0029A21F:
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x746C6644ULL), a3, result);
    a3 = 0;
    goto loc_0029A018;
loc_0029A234:
    *(unsigned __int64 *)(v_stack_p40) = 0;
    goto loc_0029A180;
loc_0029A23D:
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 32))) goto loc_0029A104;
loc_0029A247:
    goto loc_0029A10C;
loc_0029A24F:
    if (1 != 0) goto loc_0029A171;
    if (0 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 48) + 48) + 8))) goto loc_0029A17C;
    result = ExReleaseResourceLite(0, (unsigned int)(0x746C6644ULL), a3, result);
    goto loc_0029A117;
loc_0029A276:
    a2 = 0;
    result = ExAcquireSharedWaitForExclusive(0, a2, a3, result);
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlAcquireFileForModWriteEx(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint16_t v_stack_m23E;
    uint16_t v_stack_m240;
    uint32_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint8_t v_stack_m284;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint8_t v_stack_m2A7;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;
    uint8_t v_stack_p31;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (672);
    result = (*(uint64_t *)(v_rip + 0xB708BE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m298 = Arg3;
    v_stack_m2A0 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m288, Arg2, 568, a4);
    Arg1 = 0;
    v_stack_m2A7 = 0;
    v_stack_m2A4 = 0;
    v_stack_m290 = v_stack_m288;
    result = IoGetRelatedDeviceObject(0, Arg2, 568, a4);
    result = IoGetBaseFileSystemDeviceObject(0, Arg2, 568, a4);
    Arg3 = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) == 0) goto loc_00299F11;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30))))) < 80) goto loc_00299F02;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x48)) != 0) goto loc_0029A1C1;
loc_00299F02:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30))))) < 88) goto loc_00299F11;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x50)) != 0) goto loc_0029A1C1;
loc_00299F11:
loc_00299F13:
    if (result == result) goto loc_0029A1AA;
loc_00299F1C:
    result = 0;
    v_stack_m248 = 0;
    v_stack_m284 = 253;
    v_stack_m288 = 64;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m270 = v_xmm0;
    v_stack_m250 = 0;
    v_stack_m260 = v_xmm0;
    v_stack_m240 = (uint16_t)((int8_t)(*(uint8_t *)(result + 0x4C)));
    v_stack_m23E = 0;
    if (((uint16_t)((int8_t)(*(uint8_t *)(result + 0x4C)))) > ((uint16_t)(64 - 49))) goto loc_0029A0A3;
    Arg2 = 0;
    v_stack_m238 = v_stack_m230;
    result = memset(v_stack_m230, Arg2, 480, a4);
    v_stack_m240 = (uint16_t)(64 - 49);
loc_00299F83:
    v_stack_m270 = v_stack_m2A0;
    v_stack_m268 = v_stack_m298;
    result = FsFilterPerformCallbacks(v_stack_m288, 1, 1, v_stack_m2A4);
    Arg3 = 0;
    if (!sign_flag) goto loc_0029A1D2;
    goto loc_0029A018;
loc_00299FBF:
    if (((v_stack_m248) & (4)) != 0) goto loc_0029A1F0;
loc_00299FCE:
loc_00299FD2:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) != 0) goto loc_0029A062;
loc_00299FDB:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) == 0) goto loc_0029A05B;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50))) < 128) goto loc_0029A05B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x78) == 0) goto loc_0029A05B;
    result = guard_dispatch_icall(v_stack_m278, v_stack_m2A0, v_stack_m298, result);
    Arg3 = 0;
loc_0029A00A:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m2A4)) | (1));
loc_0029A00D:
    if (v_stack_m2A7 != 0) goto loc_0029A21F;
loc_0029A018:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000010ULL) goto loc_0029A0CB;
loc_0029A024:
    if (v_stack_m290 != 0) goto loc_0029A084;
loc_0029A02E:
loc_0029A030:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m2A0, Arg3, result);
    local_rsp = (local_rsp) + (672);
    return result;
loc_0029A05B:
    goto loc_0029A00A;
loc_0029A062:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30))))) < 80) goto loc_0029A06F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x48)) != 0) goto loc_0029A00D;
loc_0029A06F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30))))) < 88) goto loc_00299FDB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x50)) == 0) goto loc_00299FDB;
    goto loc_0029A00D;
loc_0029A084:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30)));
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30))) + 0x4A)) >= = 0) {
        Arg2 = (uint32_t)((uint32_t)(0xC0000010ULL));
        Arg1 = v_stack_p50;
        result = FsFilterPerformCompletionCallbacks(Arg1, Arg2, Arg3, result);
    }
    result = FsFilterCtrlFree(v_stack_p50, Arg2, Arg3, result);
    goto loc_0029A02E;
loc_0029A0A3:
    Arg2 = ((uint16_t)(result)) << (5);
    result = ExAllocatePool2(v_stack_p50, Arg2, (uint32_t)(0x676D5346ULL), result);
    if (result == 0) goto loc_0029A1C8;
    v_stack_m238 = result;
    goto loc_00299F83;
loc_0029A0CB:
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_0029A024;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x8) == 0) goto loc_0029A234;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x4))) & (8)) != 0) goto loc_0029A247;
    if ((*(uint64_t *)(v_stack_p38)) > (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x28))) goto loc_0029A23D;
loc_0029A104:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x4))) & (16)) == 0) goto loc_0029A132;
loc_0029A109:
loc_0029A10C:
loc_0029A10F:
    if ((uint8_t)((uint8_t)((uint32_t)(0x676D5346ULL))) == 0) goto loc_0029A188;
loc_0029A117:
    Arg2 = 0;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x8), Arg2, (uint32_t)(0x676D5346ULL), result);
loc_0029A121:
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_0029A140;
    goto loc_0029A024;
loc_0029A132:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x10) == 0) goto loc_0029A109;
    goto loc_0029A10F;
loc_0029A140:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x4))) & (8)) != 0) goto loc_0029A191;
    if ((*(uint64_t *)(v_stack_p38)) > (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x28))) goto loc_0029A191;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x4))) & (16)) != 0) goto loc_0029A24F;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x10) == 0) goto loc_0029A16C;
    if (((uint32_t)(0xC00000D8ULL)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x10))) goto loc_0029A276;
loc_0029A16C:
    result = *(uint64_t *)(*(uint64_t *)(v_stack_m278 + 0x18) + 0x28);
    if (0 != 0) {
        Arg1 = (uint32_t)(0xC00000D8ULL);
        result = ExConvertExclusiveToSharedLite(Arg1, Arg2, Arg3, result);
        Arg3 = 0;
    }
    *(uint64_t *)(v_stack_m298) = (uint32_t)(0xC00000D8ULL);
loc_0029A180:
    goto loc_0029A024;
loc_0029A188:
    Arg2 = 0;
    result = ExAcquireSharedWaitForExclusive(Arg1, Arg2, Arg3, result);
    goto loc_0029A121;
loc_0029A191:
    if (0 != 0) goto loc_0029A17C;
    result = ExReleaseResourceLite(0, Arg2, Arg3, result);
    goto loc_0029A117;
loc_0029A1AA:
    if ((uint8_t)(result) != 0) goto loc_00299F1C;
    v_stack_p48 = 0;
    goto loc_00299FD2;
loc_0029A1C1:
    goto loc_00299F13;
loc_0029A1C8:
    goto loc_0029A030;
loc_0029A1D2:
    if ((uint8_t)(result) == 0) goto loc_00299FBF;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) != 294) goto loc_0029A084;
    goto loc_0029A084;
loc_0029A1F0:
    result = IoGetDeviceAttachmentBaseRefWithTag(v_stack_p58, (uint32_t)(0x746C6644ULL), Arg3, result);
    v_stack_p31 = 1;
    Arg3 = 0;
    goto loc_00299FCE;
loc_0029A21F:
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x746C6644ULL), Arg3, result);
    Arg3 = 0;
    goto loc_0029A018;
loc_0029A234:
    *(uint64_t *)(v_stack_p40) = 0;
    goto loc_0029A180;
loc_0029A23D:
    if (result == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x20))) goto loc_0029A104;
loc_0029A247:
    goto loc_0029A10C;
loc_0029A24F:
    if (1 != 0) goto loc_0029A171;
    if (0 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x30) + 0x30) + 0x8))) goto loc_0029A17C;
    result = ExReleaseResourceLite(0, (uint32_t)(0x746C6644ULL), Arg3, result);
    goto loc_0029A117;
loc_0029A276:
    Arg2 = 0;
    result = ExAcquireSharedWaitForExclusive(0, Arg2, Arg3, result);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00299E5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
