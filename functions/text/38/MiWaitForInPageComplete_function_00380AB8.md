# MiWaitForInPageComplete

- RVA: `0x00380AB8`–`0x003810B8` (길이 `1,536` bytes)
- VA: `0x0000000140380AB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007B908`
- 디코드: `368`개 명령, `1,536/1,536` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00380B7D` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00380C14` → [MiStoreFaultComplete](MiStoreFaultComplete_function_00381240.md) (function, `0x00381240`)
- `0x00380C97` → [PfHardFaultLog](PfHardFaultLog_function_003810C0.md) (function, `0x003810C0`)
- `0x00380CAE` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x00380D4C` → [MiValidatePagefilePageHash](MiValidatePagefilePageHash_function_003815F0.md) (function, `0x003815F0`)
- `0x00380D5C` → [MiFlowThroughRemoveNode](MiFlowThroughRemoveNode_function_00381BB0.md) (function, `0x00381BB0`)
- `0x00380D6D` → [MiValidateInPage](MiValidateInPage_function_00382E0C.md) (function, `0x00382E0C`)
- `0x00380DA0` → [MiDeleteControlArea](../36/MiDeleteControlArea_function_003691F4.md) (function, `0x003691F4`)
- `0x00380DBC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00380DC5` → [MiRetardMdl](../40/MiRetardMdl_function_0040494C.md) (function, `0x0040494C`)
- `0x00380E2E` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00380E45` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00380E56` → [MiUnmapPageInHyperSpaceWorker](../43/MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)
- `0x00380E90` → [MiPrefetchRestOfCluster](../36/MiPrefetchRestOfCluster_function_0036B590.md) (function, `0x0036B590`)
- `0x00380F0D` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x00380F4B` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00380F65` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00380F90` → [MiIsRetryIoStatus](../40/MiIsRetryIoStatus_function_00408640.md) (function, `0x00408640`)
- `0x00380FE0` → [MiCopyPage](../2B/MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x00381005` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x00381021` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00381033` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0038106B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00381085` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiPfCompleteInPageSupport](../36/MiPfCompleteInPageSupport_function_0036D738.md) at `0x0036D7C3`
- [MiIssueHardFault](MiIssueHardFault_function_00380074.md) at `0x00380327`

### Static image references
- `0x00380F2F` → RVA `0x00E38860` (`.data`; read)
- `0x00380FF7` → RVA `0x00010880` (`.rdata`; read)
- `0x0038108B` → RVA `0x00E37398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00380D3A` → [sub_006E4582 + 0xD5](../6E/Unknown_function_006E4582.md) (`tail-transfer`)
  - `0x00380F73` → [sub_006E4582](../6E/Unknown_function_006E4582.md) (`tail-transfer`)
  - `0x0038109B` → [sub_006E4582 + 0xC6](../6E/Unknown_function_006E4582.md) (`tail-transfer`)
  - `0x003810AB` → [sub_006E4582 + 0xC6](../6E/Unknown_function_006E4582.md) (`tail-transfer`)
  - `0x003810B3` → [sub_006E4582 + 0xD5](../6E/Unknown_function_006E4582.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00380AB8  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00380ABD  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00380AC2  55                              push rbp
00380AC3  53                              push rbx
00380AC4  56                              push rsi
00380AC5  57                              push rdi
00380AC6  41 54                           push r12
00380AC8  41 55                           push r13
00380ACA  41 56                           push r14
00380ACC  41 57                           push r15
00380ACE  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00380AD3  48 81 EC B8 00 00 00            sub rsp, 0xb8
00380ADA  48 8B 82 E8 00 00 00            mov rax, qword ptr [rdx + 0xe8]
00380AE1  4C 8D AA 10 01 00 00            lea r13, [rdx + 0x110]
00380AE8  4C 8B 8A F8 00 00 00            mov r9, qword ptr [rdx + 0xf8]
00380AEF  33 F6                           xor esi, esi
00380AF1  4C 8B 61 38                     mov r12, qword ptr [rcx + 0x38]
00380AF5  4C 8B F2                        mov r14, rdx
00380AF8  48 89 45 07                     mov qword ptr [rbp + 7], rax
00380AFC  4C 8B C1                        mov r8, rcx
00380AFF  48 8B 82 E0 00 00 00            mov rax, qword ptr [rdx + 0xe0]
00380B06  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
00380B10  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00380B14  8B 82 C0 00 00 00               mov eax, dword ptr [rdx + 0xc0]
00380B1A  48 8B 82 00 01 00 00            mov rax, qword ptr [rdx + 0x100]
00380B21  48 85 C0                        test rax, rax
00380B24  40 88 75 6F                     mov byte ptr [rbp + 0x6f], sil
00380B28  89 75 7F                        mov dword ptr [rbp + 0x7f], esi
00380B2B  4C 0F 45 E8                     cmovne r13, rax
00380B2F  4C 89 4D FF                     mov qword ptr [rbp - 1], r9
00380B33  48 83 CF FF                     or rdi, 0xffffffffffffffff
00380B37  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
00380B41  48 89 7D EF                     mov qword ptr [rbp - 0x11], rdi
00380B45  49 8B 41 28                     mov rax, qword ptr [r9 + 0x28]
00380B49  48 0F BA E0 28                  bt rax, 0x28
00380B4E  72 0D                           jb 0x140380b5d
00380B50  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00380B54  48 85 C0                        test rax, rax
00380B57  0F 89 F8 03 00 00               jns 0x140380f55
00380B5D  49 8B 50 10                     mov rdx, qword ptr [r8 + 0x10]
00380B61  F6 C2 01                        test dl, 1
00380B64  0F 85 0A 03 00 00               jne 0x140380e74
00380B6A  45 33 C9                        xor r9d, r9d
00380B6D  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00380B72  49 8D 4E 20                     lea rcx, [r14 + 0x20]
00380B76  45 33 C0                        xor r8d, r8d
00380B79  41 8D 51 09                     lea edx, [r9 + 9]
00380B7D  E8 2E DB E8 FF                  call 0x14020e6b0
00380B82  4D 8B 8E 08 01 00 00            mov r9, qword ptr [r14 + 0x108]
00380B89  4D 85 C9                        test r9, r9
00380B8C  0F 85 18 02 00 00               jne 0x140380daa
00380B92  4D 85 E4                        test r12, r12
00380B95  74 15                           je 0x140380bac
00380B97  41 8B 84 24 B8 00 00 00         mov eax, dword ptr [r12 + 0xb8]
00380B9F  C1 E8 18                        shr eax, 0x18
00380BA2  24 30                           and al, 0x30
00380BA4  3C 30                           cmp al, 0x30
00380BA6  0F 84 77 03 00 00               je 0x140380f23
00380BAC  66 41 0F BA 65 0A 09            bt word ptr [r13 + 0xa], 9
00380BB3  0F 82 09 02 00 00               jb 0x140380dc2
00380BB9  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
00380BC0  A8 40                           test al, 0x40
00380BC2  0F 85 91 01 00 00               jne 0x140380d59
00380BC8  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00380BCF  41 8B 4D 2C                     mov ecx, dword ptr [r13 + 0x2c]
00380BD3  41 03 4D 20                     add ecx, dword ptr [r13 + 0x20]
00380BD7  89 45 D7                        mov dword ptr [rbp - 0x29], eax
00380BDA  81 E1 FF 0F 00 00               and ecx, 0xfff
00380BE0  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
00380BE4  48 05 FF 0F 00 00               add rax, 0xfff
00380BEA  89 75 67                        mov dword ptr [rbp + 0x67], esi
00380BED  48 03 C8                        add rcx, rax
00380BF0  49 8D 45 28                     lea rax, [r13 + 0x28]
00380BF4  48 C1 E9 0C                     shr rcx, 0xc
00380BF8  48 8D 04 C8                     lea rax, [rax + rcx*8]
00380BFC  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00380C00  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
00380C07  0F BA E0 0A                     bt eax, 0xa
00380C0B  73 0C                           jae 0x140380c19
00380C0D  48 8D 55 7F                     lea rdx, [rbp + 0x7f]
00380C11  49 8B CE                        mov rcx, r14
00380C14  E8 27 06 00 00                  call 0x140381240
00380C19  49 8D 5E 50                     lea rbx, [r14 + 0x50]
00380C1D  4C 8B FB                        mov r15, rbx
00380C20  49 39 B6 D0 00 00 00            cmp qword ptr [r14 + 0xd0], rsi
00380C27  0F 85 39 01 00 00               jne 0x140380d66
00380C2D  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
00380C34  39 33                           cmp dword ptr [rbx], esi
00380C36  0F 8D 03 01 00 00               jge 0x140380d3f
00380C3C  F6 45 7F 01                     test byte ptr [rbp + 0x7f], 1
00380C40  45 8B 3F                        mov r15d, dword ptr [r15]
00380C43  75 3B                           jne 0x140380c80
00380C45  65 FF 04 25 A4 2E 00 00         inc dword ptr gs:[0x2ea4]
00380C4D  8B CE                           mov ecx, esi
00380C4F  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
00380C52  A9 FF 0F 00 00                  test eax, 0xfff
00380C57  0F 95 C1                        setne cl
00380C5A  C1 E8 0C                        shr eax, 0xc
00380C5D  03 C8                           add ecx, eax
00380C5F  65 01 0C 25 A0 2E 00 00         add dword ptr gs:[0x2ea0], ecx
00380C67  4D 85 E4                        test r12, r12
00380C6A  74 14                           je 0x140380c80
00380C6C  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
00380C73  A8 20                           test al, 0x20
00380C75  75 09                           jne 0x140380c80
00380C77  F0 41 FF 84 24 A8 00 00 00      lock inc dword ptr [r12 + 0xa8]
00380C80  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
00380C84  8B 5D 7F                        mov ebx, dword ptr [rbp + 0x7f]
00380C87  83 E3 01                        and ebx, 1
00380C8A  03 DB                           add ebx, ebx
00380C8C  49 8B 0C 24                     mov rcx, qword ptr [r12]
00380C90  48 85 C9                        test rcx, rcx
00380C93  74 07                           je 0x140380c9c
00380C95  8B D3                           mov edx, ebx
00380C97  E8 24 04 00 00                  call 0x1403810c0
00380C9C  41 F6 45 0A 01                  test byte ptr [r13 + 0xa], 1
00380CA1  41 89 1C 24                     mov dword ptr [r12], ebx
00380CA5  74 0C                           je 0x140380cb3
00380CA7  49 8B 4D 18                     mov rcx, qword ptr [r13 + 0x18]
00380CAB  49 8B D5                        mov rdx, r13
00380CAE  E8 AD 61 EC FF                  call 0x140246e60
00380CB3  41 83 8E BC 00 00 00 FF         or dword ptr [r14 + 0xbc], 0xffffffff
00380CBB  41 BC 17 00 00 C0               mov r12d, 0xc0000017
00380CC1  41 8B 9E C0 00 00 00            mov ebx, dword ptr [r14 + 0xc0]
00380CC8  89 75 DF                        mov dword ptr [rbp - 0x21], esi
00380CCB  45 85 FF                        test r15d, r15d
00380CCE  79 4E                           jns 0x140380d1e
00380CD0  49 C7 C0 11 00 00 C0            mov r8, 0xffffffffc0000011
00380CD7  45 3B F8                        cmp r15d, r8d
00380CDA  0F 84 EC 01 00 00               je 0x140380ecc
00380CE0  41 81 FF 16 00 00 80            cmp r15d, 0x80000016
00380CE7  0F 85 9C 02 00 00               jne 0x140380f89
00380CED  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00380CF1  48 3B CF                        cmp rcx, rdi
00380CF4  0F 85 B7 02 00 00               jne 0x140380fb1
00380CFA  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00380CFD  41 89 46 70                     mov dword ptr [r14 + 0x70], eax
00380D01  49 89 76 68                     mov qword ptr [r14 + 0x68], rsi
00380D05  45 89 7E 50                     mov dword ptr [r14 + 0x50], r15d
00380D09  48 81 C4 B8 00 00 00            add rsp, 0xb8
00380D10  41 5F                           pop r15
00380D12  41 5E                           pop r14
00380D14  41 5D                           pop r13
00380D16  41 5C                           pop r12
00380D18  5F                              pop rdi
00380D19  5E                              pop rsi
00380D1A  5B                              pop rbx
00380D1B  5D                              pop rbp
00380D1C  C3                              ret
00380D1D  CC                              int3
00380D1E  49 8B 56 58                     mov rdx, qword ptr [r14 + 0x58]
00380D22  44 8B 45 D7                     mov r8d, dword ptr [rbp - 0x29]
00380D26  49 3B D0                        cmp rdx, r8
00380D29  0F 85 AC 00 00 00               jne 0x140380ddb
00380D2F  8B 5D 67                        mov ebx, dword ptr [rbp + 0x67]
00380D32  81 FB 3F 00 00 C0               cmp ebx, 0xc000003f
00380D38  75 B3                           jne 0x140380ced
00380D3A  E9 18 39 36 00                  jmp 0x1406e4657
00380D3F  0F BA E0 17                     bt eax, 0x17
00380D43  0F 83 F3 FE FF FF               jae 0x140380c3c
00380D49  49 8B CE                        mov rcx, r14
00380D4C  E8 9F 08 00 00                  call 0x1403815f0
00380D51  89 45 67                        mov dword ptr [rbp + 0x67], eax
00380D54  E9 E3 FE FF FF                  jmp 0x140380c3c
00380D59  49 8B CE                        mov rcx, r14
00380D5C  E8 4F 0E 00 00                  call 0x140381bb0
00380D61  E9 62 FE FF FF                  jmp 0x140380bc8
00380D66  39 33                           cmp dword ptr [rbx], esi
00380D68  7C 16                           jl 0x140380d80
00380D6A  49 8B CE                        mov rcx, r14
00380D6D  E8 9A 20 00 00                  call 0x140382e0c
00380D72  89 45 67                        mov dword ptr [rbp + 0x67], eax
00380D75  3D 34 04 00 C0                  cmp eax, 0xc0000434
00380D7A  0F 84 1A 01 00 00               je 0x140380e9a
00380D80  49 8B 8E D0 00 00 00            mov rcx, qword ptr [r14 + 0xd0]
00380D87  48 8B C7                        mov rax, rdi
00380D8A  48 8B 09                        mov rcx, qword ptr [rcx]
00380D8D  F0 48 0F C1 41 70               lock xadd qword ptr [rcx + 0x70], rax
00380D93  48 03 C7                        add rax, rdi
00380D96  74 08                           je 0x140380da0
00380D98  4C 8B FB                        mov r15, rbx
00380D9B  E9 9C FE FF FF                  jmp 0x140380c3c
00380DA0  E8 4F 84 FE FF                  call 0x1403691f4
00380DA5  49 8B DF                        mov rbx, r15
00380DA8  EB EE                           jmp 0x140380d98
00380DAA  4D 8B C6                        mov r8, r14
00380DAD  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00380DB2  BA 47 19 06 00                  mov edx, 0x61947
00380DB7  B9 1A 00 00 00                  mov ecx, 0x1a
00380DBC  E8 9F C8 17 00                  call 0x1404fd660
00380DC1  CC                              int3
00380DC2  49 8B CD                        mov rcx, r13
00380DC5  E8 82 3B 08 00                  call 0x14040494c
00380DCA  41 C7 46 50 9A 00 00 C0         mov dword ptr [r14 + 0x50], 0xc000009a
00380DD2  49 89 76 58                     mov qword ptr [r14 + 0x58], rsi
00380DD6  E9 DE FD FF FF                  jmp 0x140380bb9
00380DDB  48 85 D2                        test rdx, rdx
00380DDE  0F 84 94 01 00 00               je 0x140380f78
00380DE4  0F BA E3 16                     bt ebx, 0x16
00380DE8  0F 82 5C 02 00 00               jb 0x14038104a
00380DEE  45 8B 65 2C                     mov r12d, dword ptr [r13 + 0x2c]
00380DF2  41 B9 FF 0F 00 00               mov r9d, 0xfff
00380DF8  45 03 65 20                     add r12d, dword ptr [r13 + 0x20]
00380DFC  45 2B 45 28                     sub r8d, dword ptr [r13 + 0x28]
00380E00  4D 23 E1                        and r12, r9
00380E03  41 8B 5E 58                     mov ebx, dword ptr [r14 + 0x58]
00380E07  41 8B C0                        mov eax, r8d
00380E0A  4C 2B E0                        sub r12, rax
00380E0D  4D 03 E1                        add r12, r9
00380E10  4C 03 E2                        add r12, rdx
00380E13  49 C1 EC 0C                     shr r12, 0xc
00380E17  41 23 D9                        and ebx, r9d
00380E1A  89 5D D7                        mov dword ptr [rbp - 0x29], ebx
00380E1D  74 3C                           je 0x140380e5b
00380E1F  4B 8B 4C E5 28                  mov rcx, qword ptr [r13 + r12*8 + 0x28]
00380E24  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00380E28  41 B8 00 00 00 80               mov r8d, 0x80000000
00380E2E  E8 DD 1C FB FF                  call 0x140332b10
00380E33  48 03 D8                        add rbx, rax
00380E36  41 B8 00 10 00 00               mov r8d, 0x1000
00380E3C  44 2B 45 D7                     sub r8d, dword ptr [rbp - 0x29]
00380E40  48 8B CB                        mov rcx, rbx
00380E43  33 D2                           xor edx, edx
00380E45  E8 F6 5D 34 00                  call 0x1406c6c40
00380E4A  8A 55 6F                        mov dl, byte ptr [rbp + 0x6f]
00380E4D  41 B8 00 00 00 80               mov r8d, 0x80000000
00380E53  48 8B CB                        mov rcx, rbx
00380E56  E8 A5 19 0B 00                  call 0x140432800
00380E5B  49 8D 45 30                     lea rax, [r13 + 0x30]
00380E5F  4A 8D 04 E0                     lea rax, [rax + r12*8]
00380E63  48 3B 45 F7                     cmp rax, qword ptr [rbp - 9]
00380E67  76 4C                           jbe 0x140380eb5
00380E69  41 BC 17 00 00 C0               mov r12d, 0xc0000017
00380E6F  E9 BB FE FF FF                  jmp 0x140380d2f
00380E74  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
00380E78  80 3A 02                        cmp byte ptr [rdx], 2
00380E7B  0F 85 E9 FC FF FF               jne 0x140380b6a
00380E81  4D 85 E4                        test r12, r12
00380E84  0F 84 E0 FC FF FF               je 0x140380b6a
00380E8A  4D 8B C4                        mov r8, r12
00380E8D  49 8B CE                        mov rcx, r14
00380E90  E8 FB A6 FE FF                  call 0x14036b590
00380E95  E9 D0 FC FF FF                  jmp 0x140380b6a
00380E9A  41 8B 8E C0 00 00 00            mov ecx, dword ptr [r14 + 0xc0]
00380EA1  4D 8D 7E 50                     lea r15, [r14 + 0x50]
00380EA5  0F BA E9 15                     bts ecx, 0x15
00380EA9  41 89 8E C0 00 00 00            mov dword ptr [r14 + 0xc0], ecx
00380EB0  E9 CB FE FF FF                  jmp 0x140380d80
00380EB5  4A 8D 04 E5 F8 FF FF FF         lea rax, [r12*8 - 8]
00380EBD  48 C1 F8 03                     sar rax, 3
00380EC1  FF C0                           inc eax
00380EC3  41 89 86 BC 00 00 00            mov dword ptr [r14 + 0xbc], eax
00380ECA  EB 9D                           jmp 0x140380e69
00380ECC  0F BA E3 16                     bt ebx, 0x16
00380ED0  0F 82 9B 01 00 00               jb 0x140381071
00380ED6  49 8D 5D 30                     lea rbx, [r13 + 0x30]
00380EDA  4C 8B 6D F7                     mov r13, qword ptr [rbp - 9]
00380EDE  EB 36                           jmp 0x140380f16
00380EE0  48 8B 03                        mov rax, qword ptr [rbx]
00380EE3  48 8D 04 40                     lea rax, [rax + rax*2]
00380EE7  48 03 C0                        add rax, rax
00380EEA  48 B9 20 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000020
00380EF4  8B 04 C1                        mov eax, dword ptr [rcx + rax*8]
00380EF7  41 B8 01 00 00 00               mov r8d, 1
00380EFD  48 8B 13                        mov rdx, qword ptr [rbx]
00380F00  33 C9                           xor ecx, ecx
00380F02  C1 E8 10                        shr eax, 0x10
00380F05  44 0F B6 C8                     movzx r9d, al
00380F09  41 C1 E9 06                     shr r9d, 6
00380F0D  E8 7E 16 FB FF                  call 0x140332590
00380F12  48 83 C3 08                     add rbx, 8
00380F16  49 3B DD                        cmp rbx, r13
00380F19  76 C5                           jbe 0x140380ee0
00380F1B  44 8B FE                        mov r15d, esi
00380F1E  E9 CA FD FF FF                  jmp 0x140380ced
00380F23  41 8B 84 24 B8 00 00 00         mov eax, dword ptr [r12 + 0xb8]
00380F2B  24 0F                           and al, 0xf
00380F2D  3C 01                           cmp al, 1
00380F2F  48 8D 05 2A 79 AB 00            lea rax, [rip + 0xab792a]
00380F36  0F 85 01 01 00 00               jne 0x14038103d
00380F3C  48 39 30                        cmp qword ptr [rax], rsi
00380F3F  0F 85 67 FC FF FF               jne 0x140380bac
00380F45  49 8D 4E 68                     lea rcx, [r14 + 0x68]
00380F49  33 D2                           xor edx, edx
00380F4B  E8 E0 6D E9 FF                  call 0x140217d30
00380F50  E9 57 FC FF FF                  jmp 0x140380bac
00380F55  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00380F59  48 85 C0                        test rax, rax
00380F5C  0F 84 FB FB FF FF               je 0x140380b5d
00380F62  49 8B C9                        mov rcx, r9
00380F65  E8 66 D3 F0 FF                  call 0x14028e2d0
00380F6A  83 F8 09                        cmp eax, 9
00380F6D  0F 85 EA FB FF FF               jne 0x140380b5d
00380F73  E9 0A 36 36 00                  jmp 0x1406e4582
00380F78  F6 C3 20                        test bl, 0x20
00380F7B  0F 84 63 FE FF FF               je 0x140380de4
00380F81  45 8B FC                        mov r15d, r12d
00380F84  E9 A6 FD FF FF                  jmp 0x140380d2f
00380F89  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00380F8D  41 8B CF                        mov ecx, r15d
00380F90  E8 AB 76 08 00                  call 0x140408640
00380F95  89 45 DF                        mov dword ptr [rbp - 0x21], eax
00380F98  85 C0                           test eax, eax
00380F9A  0F 85 EB 00 00 00               jne 0x14038108b
00380FA0  F6 C3 20                        test bl, 0x20
00380FA3  0F 84 07 01 00 00               je 0x1403810b0
00380FA9  45 8B FC                        mov r15d, r12d
00380FAC  E9 3C FD FF FF                  jmp 0x140380ced
00380FB1  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
00380FBB  48 8B C7                        mov rax, rdi
00380FBE  48 8B 5D FF                     mov rbx, qword ptr [rbp - 1]
00380FC2  41 B8 01 00 00 00               mov r8d, 1
00380FC8  48 8B D3                        mov rdx, rbx
00380FCB  48 2B D0                        sub rdx, rax
00380FCE  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00380FD8  48 C1 FA 04                     sar rdx, 4
00380FDC  48 0F AF D0                     imul rdx, rax
00380FE0  E8 4B 0B F3 FF                  call 0x1402b1b30
00380FE5  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00380FE9  48 8D 34 40                     lea rsi, [rax + rax*2]
00380FED  48 C1 E6 04                     shl rsi, 4
00380FF1  48 8B C7                        mov rax, rdi
00380FF4  48 03 F0                        add rsi, rax
00380FF7  48 8B 05 82 F8 C8 FF            mov rax, qword ptr [rip - 0x37077e]
00380FFE  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00381002  48 89 01                        mov qword ptr [rcx], rax
00381005  E8 92 99 F0 FF                  call 0x14028a99c
0038100A  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0038100E  48 C1 E9 3C                     shr rcx, 0x3c
00381012  80 E1 07                        and cl, 7
00381015  80 F9 03                        cmp cl, 3
00381018  0F 85 DC FC FF FF               jne 0x140380cfa
0038101E  48 8B CE                        mov rcx, rsi
00381021  E8 1A 93 F9 FF                  call 0x14031a340
00381026  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0038102A  8A D0                           mov dl, al
0038102C  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
00381030  48 8B CE                        mov rcx, rsi
00381033  E8 A8 93 F9 FF                  call 0x14031a3e0
00381038  E9 BD FC FF FF                  jmp 0x140380cfa
0038103D  49 8D 84 24 E0 00 00 00         lea rax, [r12 + 0xe0]
00381045  E9 F2 FE FF FF                  jmp 0x140380f3c
0038104A  F6 45 7F 01                     test byte ptr [rbp + 0x7f], 1
0038104E  0F 85 9A FD FF FF               jne 0x140380dee
00381054  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00381058  4C 8B C2                        mov r8, rdx
0038105B  BA 04 00 00 00                  mov edx, 4
00381060  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00381065  4D 8B CE                        mov r9, r14
00381068  8D 4A 76                        lea ecx, [rdx + 0x76]
0038106B  E8 F0 C5 17 00                  call 0x1404fd660
00381070  CC                              int3
00381071  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00381075  BA 03 00 00 00                  mov edx, 3
0038107A  4D 8B CE                        mov r9, r14
0038107D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00381082  8D 4A 77                        lea ecx, [rdx + 0x77]
00381085  E8 D6 C5 17 00                  call 0x1404fd660
0038108A  CC                              int3
0038108B  39 35 07 63 AB 00               cmp dword ptr [rip + 0xab6307], esi
00381091  0F 85 09 FF FF FF               jne 0x140380fa0
00381097  F6 45 7F 01                     test byte ptr [rbp + 0x7f], 1
0038109B  0F 84 A7 35 36 00               je 0x1406e4648
003810A1  F6 45 7F 02                     test byte ptr [rbp + 0x7f], 2
003810A5  0F 84 F5 FE FF FF               je 0x140380fa0
003810AB  E9 98 35 36 00                  jmp 0x1406e4648
003810B0  8B 5D 67                        mov ebx, dword ptr [rbp + 0x67]
003810B3  E9 9F 35 36 00                  jmp 0x1406e4657
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWaitForInPageComplete(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (184);
    v_rsi = 0;
    v_stack_m58 = *(unsigned __int64 *)(a2 + 232);
    v_stack_m78 = *(unsigned __int64 *)(a2 + 224);
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    v_r13 = a2 + 272;
    if (*(unsigned __int64 *)(a2 + 256) != 0) { v_r13 = *(unsigned __int64 *)(a2 + 256); }
    v_stack_m60 = *(unsigned __int64 *)(a2 + 248);
    v_rdi = (v_rdi) | (-1);
    v_stack_m70 = v_rdi;
    if (condition_is_below) goto loc_00380B5D;
    if (!sign_flag) goto loc_00380F55;
loc_00380B5D:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_00380E74;
loc_00380B6A:
    a4 = 0;
    v_stack_mD8 = 0;
    a3 = 0;
    result = KeWaitForSingleObject(a2 + 32, a4 + 9, a3, a4);
    if (*(unsigned __int64 *)(a2 + 264) != 0) goto loc_00380DAA;
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_00380BAC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184))) >> (24));
    result = (unsigned __int8)((result) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_00380F23;
loc_00380BAC:
    if (((unsigned __int8)(result)) < 48) goto loc_00380DC2;
loc_00380BB9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 192)))) & (64)) != 0) goto loc_00380D59;
loc_00380BC8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 44))) + (*(unsigned int *)(v_r13 + 32)));
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 184)));
    a1 = (unsigned int)((a1) & (0xFFFULL));
    result = ((unsigned int)(*(unsigned int *)(v_r13 + 40))) + (0xFFFULL);
    v_stack_p8 = 0;
    a1 = (a1) + (result);
    a1 = (a1) >> (12);
    v_stack_m68 = v_r13 + 40 + a1 * 8;
    result = (unsigned int)(*(unsigned int *)(a2 + 192));
    if (!(condition_is_above_or_equal)) {
        a2 = v_stack_p20;
        a1 = a2;
        result = MiStoreFaultComplete(a1, a2, a3, *(unsigned __int64 *)(a2 + 264));
    }
    if ((*(unsigned __int64 *)(a2 + 208)) != 0) goto loc_00380D66;
    if ((*(unsigned int *)(a2 + 80)) >= 0) goto loc_00380D3F;
loc_00380C3C:
    if (((v_stack_p20) & (1)) != 0) goto loc_00380C80;
    a1 = ((((unsigned int)((unsigned int)(v_stack_m88))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)(v_stack_m88)) >> (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_00380C80;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 192)))) & (32)) == 0) {
    }
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p20)) & (1));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_rbx)));
    result = (unsigned int)(*(unsigned int *)(a2 + 192));
    if (*(unsigned __int64 *)(v_stack_p18) != 0) {
        a2 = (unsigned int)(v_rbx);
        result = PfHardFaultLog(*(unsigned __int64 *)(v_stack_p18), a2, a3, *(unsigned __int64 *)(a2 + 264));
    }
    *(unsigned int *)(v_stack_p18) = (unsigned int)(v_rbx);
    if (((*(unsigned __int8 *)(v_r13 + 10)) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(v_r13 + 24);
        a2 = v_r13;
        result = MmUnmapLockedPages(a1, a2, a3, *(unsigned __int64 *)(a2 + 264));
    }
    v_stack_m80 = 0;
    if (!sign_flag) goto loc_00380D1E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)))) == ((unsigned int)(0xFFFFFFFFC0000011ULL))) goto loc_00380ECC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)))) != 0x80000016ULL) goto loc_00380F89;
loc_00380CED:
    if (v_stack_m70 != v_rdi) goto loc_00380FB1;
loc_00380CFA:
    *(unsigned int *)(a2 + 112) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(a2 + 104) = 0;
    *(unsigned int *)(a2 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)));
    v_rsp = (v_rsp) + (184);
    return (unsigned int)(v_stack_p20);
loc_00380D1E:
    if ((*(unsigned __int64 *)(a2 + 88)) != ((unsigned int)(v_stack_m88))) goto loc_00380DDB;
loc_00380D2F:
    if (((unsigned int)((unsigned int)(v_stack_p8))) != 0xC000003FULL) goto loc_00380CED;
loc_00380D3F:
    if (((unsigned int)((unsigned int)(v_stack_p8))) >= 0xC000003FULL) goto loc_00380C3C;
    result = MiValidatePagefilePageHash(a2, *(unsigned __int64 *)(a2 + 88), (unsigned int)(v_stack_m88), *(unsigned __int64 *)(a2 + 264));
    v_stack_p8 = (unsigned int)(result);
    goto loc_00380C3C;
loc_00380D59:
    result = MiFlowThroughRemoveNode(a2, *(unsigned __int64 *)(a2 + 88), (unsigned int)(v_stack_m88), *(unsigned __int64 *)(a2 + 264));
    goto loc_00380BC8;
loc_00380D66:
    if ((*(unsigned int *)((unsigned int)(v_stack_p8))) < 0) goto loc_00380D80;
    result = MiValidateInPage(a2, *(unsigned __int64 *)(a2 + 88), (unsigned int)(v_stack_m88), *(unsigned __int64 *)(a2 + 264));
    v_stack_p8 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC0000434ULL) goto loc_00380E9A;
loc_00380D80:
    result = (v_rdi) + (v_rdi);
    if (condition_is_equal) goto loc_00380DA0;
loc_00380D98:
    goto loc_00380C3C;
loc_00380DA0:
    result = MiDeleteControlArea(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 208)), *(unsigned __int64 *)(a2 + 88), (unsigned int)(v_stack_m88), *(unsigned __int64 *)(a2 + 264));
    goto loc_00380D98;
loc_00380DAA:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x61947ULL), a2, *(unsigned __int64 *)(a2 + 264));
loc_00380DC2:
    result = MiRetardMdl(v_r13, (unsigned int)(0x61947ULL), a2, *(unsigned __int64 *)(a2 + 264));
    *(unsigned int *)(a2 + 80) = 0xC000009AULL;
    *(unsigned __int64 *)(a2 + 88) = 0;
    goto loc_00380BB9;
loc_00380DDB:
    if ((unsigned int)(0x61947ULL) == 0) goto loc_00380F78;
loc_00380DE4:
    if (condition_is_below) goto loc_0038104A;
loc_00380DEE:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 44))) + (*(unsigned int *)(v_r13 + 32)));
    a3 = (unsigned int)((a2) - (*(unsigned int *)(v_r13 + 40)));
    v_r12 = (v_r12) & ((unsigned int)(0xFFFULL));
    v_r12 = (v_r12) - ((unsigned int)((unsigned int)(a3)));
    v_r12 = (v_r12) + ((unsigned int)(0xFFFULL));
    v_r12 = (v_r12) + ((unsigned int)(0x61947ULL));
    v_r12 = (v_r12) >> (12);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 88))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    v_stack_m88 = (unsigned int)(v_rbx);
    result = (unsigned int)((unsigned int)(a3));
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(v_r13 + v_r12 * 8 + 40);
        a2 = v_stack_p10;
        a3 = 0x80000000ULL;
        result = MiMapPageInHyperSpaceWorker(a1, a2, a3, (unsigned int)(0xFFFULL));
        v_rbx = (v_rbx) + (result);
        a3 = 0x1000ULL;
        a3 = (unsigned int)((a3) - (v_stack_m88));
        a1 = v_rbx;
        a2 = 0;
        result = memset(a1, a2, a3, (unsigned int)(0xFFFULL));
        a2 = v_stack_p10;
        a3 = 0x80000000ULL;
        a1 = v_rbx;
        result = MiUnmapPageInHyperSpaceWorker(a1, a2, a3, (unsigned int)(0xFFFULL));
    }
    if ((v_r13 + 48 + v_r12 * 8) <= v_stack_m68) goto loc_00380EB5;
loc_00380E69:
    goto loc_00380D2F;
loc_00380E74:
    a2 = (a2) & (-2);
    if ((*(unsigned __int8 *)(a2)) != 2) goto loc_00380B6A;
    if ((unsigned int)(0xC0000017ULL) == 0) goto loc_00380B6A;
    result = MiPrefetchRestOfCluster(a2, a2, (unsigned int)(0xC0000017ULL), (unsigned int)(0xFFFULL));
    goto loc_00380B6A;
loc_00380E9A:
    *(unsigned int *)(a2 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 192)));
    goto loc_00380D80;
loc_00380EB5:
    result = ((unsigned int)(0xC0000017ULL) * 8 - 8) >> (3);
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(a2 + 188) = (unsigned int)(result);
    goto loc_00380E69;
loc_00380ECC:
    if (condition_is_below) goto loc_00381071;
    goto loc_00380F16;
loc_00380EE0:
    result = (*(unsigned __int64 *)(v_r13 + 48) + *(unsigned __int64 *)(v_r13 + 48) * 2) + (*(unsigned __int64 *)(v_r13 + 48) + *(unsigned __int64 *)(v_r13 + 48) * 2);
    a1 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a2 + 192)) + result * 8))) >> (16));
    a4 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiZeroPhysicalPage(a1, *(unsigned __int64 *)(v_r13 + 48), 1, a4);
    v_rbx = (v_r13 + 48) + (8);
loc_00380F16:
    if (v_rbx <= v_stack_m68) goto loc_00380EE0;
    goto loc_00380CED;
loc_00380F23:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000017ULL) + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0038103D;
loc_00380F3C:
    if ((*(unsigned __int64 *)(v_rip + 11237674)) != 0) goto loc_00380BAC;
    a2 = 0;
    result = KiUnstackDetachProcess(a2 + 104, a2, 1, a4);
    goto loc_00380BAC;
loc_00380F55:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00380B5D;
    result = MiGetPfnSlabType(a4, a2, 1, a4);
    if (((unsigned int)(result)) != 9) goto loc_00380B5D;
loc_00380F78:
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) goto loc_00380DE4;
    goto loc_00380D2F;
loc_00380F89:
    result = MiIsRetryIoStatus((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))))), (unsigned int)(*(unsigned int *)(v_stack_m68 + 40)), 1, a4);
    v_stack_m80 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_0038108B;
loc_00380FA0:
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) goto loc_003810B0;
    goto loc_00380CED;
loc_00380FB1:
    a2 = (v_stack_m60) - (v_rdi);
    a2 = (a2) >> (4);
    a2 = (a2) * (v_rdi);
    result = MiCopyPage((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))))), a2, 1, a4);
    v_rsi = (v_stack_m70 + v_stack_m70 * 2) << (4);
    v_rsi = (v_rsi) + (v_rdi);
    *(unsigned __int64 *)(v_rsi + 16) = *(unsigned __int64 *)(v_rip - 3606398);
    result = MiSetOriginalPtePfnFromFreeList(v_rsi + 16, a2, 1, a4);
    a1 = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    a1 = (unsigned __int8)((a1) & (7));
    if (((unsigned __int8)(a1)) != 3) goto loc_00380CFA;
    result = MiLockPageInline(v_rsi, a2, 1, a4);
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(v_stack_m60 + 8);
    result = MiUnlockPage(v_rsi, (unsigned __int8)(result), 1, a4);
    goto loc_00380CFA;
loc_0038103D:
    goto loc_00380F3C;
loc_0038104A:
    if (((v_stack_p20) & (1)) != 0) goto loc_00380DEE;
    v_stack_p20 = v_stack_m78;
    result = KeBugCheckEx(4 + 118, 4, (unsigned __int8)(result), a2);
loc_00381071:
    v_stack_p20 = v_stack_m78;
    result = KeBugCheckEx(3 + 119, 3, (unsigned __int8)(result), a2);
loc_0038108B:
    if ((*(unsigned int *)(v_rip + 11232007)) != ((unsigned int)(v_rsi))) goto loc_00380FA0;
    if (((v_stack_p20) & (2)) == 0) goto loc_00380FA0;
loc_003810B0:
}
```

## 5. (Beta) C Style

```c
int64_t MiWaitForInPageComplete(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_mD8;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (184);
    local_rsi = 0;
    v_stack_m58 = *(uint64_t *)(arg2 + 0xE8);
    v_stack_m78 = *(uint64_t *)(arg2 + 0xE0);
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    local_r13 = Arg2 + 272;
    if (*(uint64_t *)(arg2 + 0x100) != 0) { local_r13 = *(uint64_t *)(arg2 + 0x100); }
    v_stack_m60 = *(uint64_t *)(arg2 + 0xF8);
    local_rdi = (local_rdi) | (-1);
    v_stack_m70 = local_rdi;
    if (condition_is_below) goto loc_00380B5D;
    if (!sign_flag) goto loc_00380F55;
loc_00380B5D:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_00380E74;
loc_00380B6A:
    a4 = 0;
    v_stack_mD8 = 0;
    Arg3 = 0;
    result = KeWaitForSingleObject(Arg2 + 32, a4 + 9, Arg3, a4);
    if (*(uint64_t *)(arg2 + 0x108) != 0) goto loc_00380DAA;
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_00380BAC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8))) >> (24));
    result = (uint8_t)((result) & (48));
    if (((uint8_t)(result)) == 48) goto loc_00380F23;
loc_00380BAC:
    if (((uint8_t)(result)) < 48) goto loc_00380DC2;
loc_00380BB9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))) & (64)) != 0) goto loc_00380D59;
loc_00380BC8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x2C))) + (*(uint32_t *)(local_r13 + 0x20)));
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB8)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    result = ((uint32_t)(*(uint32_t *)(local_r13 + 0x28))) + (0xFFFULL);
    v_stack_p8 = 0;
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) >> (12);
    v_stack_m68 = local_r13 + 40 + Arg1 * 8;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0xC0));
    if (!(condition_is_above_or_equal)) {
        Arg2 = v_stack_p20;
        Arg1 = Arg2;
        result = MiStoreFaultComplete(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x108));
    }
    if ((*(uint64_t *)(arg2 + 0xD0)) != 0) goto loc_00380D66;
    if ((*(uint32_t *)(arg2 + 0x50)) >= 0) goto loc_00380D3F;
loc_00380C3C:
    if (((v_stack_p20) & (1)) != 0) goto loc_00380C80;
    Arg1 = ((((uint32_t)((uint32_t)(v_stack_m88))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)(v_stack_m88)) >> (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_00380C80;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))) & (32)) == 0) {
    }
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p20)) & (1));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_rbx)));
    result = (uint32_t)(*(uint32_t *)(arg2 + 0xC0));
    if (*(uint64_t *)(v_stack_p18) != 0) {
        Arg2 = (uint32_t)(local_rbx);
        result = PfHardFaultLog(*(uint64_t *)(v_stack_p18), Arg2, Arg3, *(uint64_t *)(arg2 + 0x108));
    }
    *(uint32_t *)(v_stack_p18) = (uint32_t)(local_rbx);
    if (((*(uint8_t *)(local_r13 + 0xA)) & (1)) != 0) {
        Arg1 = *(uint64_t *)(local_r13 + 0x18);
        Arg2 = local_r13;
        result = MmUnmapLockedPages(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x108));
    }
    v_stack_m80 = 0;
    if (!sign_flag) goto loc_00380D1E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)))) == ((uint32_t)(0xFFFFFFFFC0000011ULL))) goto loc_00380ECC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)))) != 0x80000016ULL) goto loc_00380F89;
loc_00380CED:
    if (v_stack_m70 != local_rdi) goto loc_00380FB1;
loc_00380CFA:
    *(uint32_t *)(arg2 + 0x70) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint64_t *)(arg2 + 0x68) = 0;
    *(uint32_t *)(arg2 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)));
    local_rsp = (local_rsp) + (184);
    return (uint32_t)(v_stack_p20);
loc_00380D1E:
    if ((*(uint64_t *)(arg2 + 0x58)) != ((uint32_t)(v_stack_m88))) goto loc_00380DDB;
loc_00380D2F:
    if (((uint32_t)((uint32_t)(v_stack_p8))) != 0xC000003FULL) goto loc_00380CED;
loc_00380D3F:
    if (((uint32_t)((uint32_t)(v_stack_p8))) >= 0xC000003FULL) goto loc_00380C3C;
    result = MiValidatePagefilePageHash(Arg2, *(uint64_t *)(arg2 + 0x58), (uint32_t)(v_stack_m88), *(uint64_t *)(arg2 + 0x108));
    v_stack_p8 = (uint32_t)(result);
    goto loc_00380C3C;
loc_00380D59:
    result = MiFlowThroughRemoveNode(Arg2, *(uint64_t *)(arg2 + 0x58), (uint32_t)(v_stack_m88), *(uint64_t *)(arg2 + 0x108));
    goto loc_00380BC8;
loc_00380D66:
    if ((*(uint32_t *)((uint32_t)(v_stack_p8))) < 0) goto loc_00380D80;
    result = MiValidateInPage(Arg2, *(uint64_t *)(arg2 + 0x58), (uint32_t)(v_stack_m88), *(uint64_t *)(arg2 + 0x108));
    v_stack_p8 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC0000434ULL) goto loc_00380E9A;
loc_00380D80:
    result = (local_rdi) + (local_rdi);
    if (condition_is_equal) goto loc_00380DA0;
loc_00380D98:
    goto loc_00380C3C;
loc_00380DA0:
    result = MiDeleteControlArea(*(uint64_t *)(*(uint64_t *)(arg2 + 0xD0)), *(uint64_t *)(arg2 + 0x58), (uint32_t)(v_stack_m88), *(uint64_t *)(arg2 + 0x108));
    goto loc_00380D98;
loc_00380DAA:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x61947ULL), Arg2, *(uint64_t *)(arg2 + 0x108));
loc_00380DC2:
    result = MiRetardMdl(local_r13, (uint32_t)(0x61947ULL), Arg2, *(uint64_t *)(arg2 + 0x108));
    *(uint32_t *)(arg2 + 0x50) = 0xC000009AULL;
    *(uint64_t *)(arg2 + 0x58) = 0;
    goto loc_00380BB9;
loc_00380DDB:
    if ((uint32_t)(0x61947ULL) == 0) goto loc_00380F78;
loc_00380DE4:
    if (condition_is_below) goto loc_0038104A;
loc_00380DEE:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x2C))) + (*(uint32_t *)(local_r13 + 0x20)));
    Arg3 = (uint32_t)((Arg2) - (*(uint32_t *)(local_r13 + 0x28)));
    local_r12 = (local_r12) & ((uint32_t)(0xFFFULL));
    local_r12 = (local_r12) - ((uint32_t)((uint32_t)(Arg3)));
    local_r12 = (local_r12) + ((uint32_t)(0xFFFULL));
    local_r12 = (local_r12) + ((uint32_t)(0x61947ULL));
    local_r12 = (local_r12) >> (12);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x58))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    v_stack_m88 = (uint32_t)(local_rbx);
    result = (uint32_t)((uint32_t)(Arg3));
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(local_r13 + local_r12 * 8 + 0x28);
        Arg2 = v_stack_p10;
        Arg3 = 0x80000000ULL;
        result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, (uint32_t)(0xFFFULL));
        local_rbx = (local_rbx) + (result);
        Arg3 = 0x1000ULL;
        Arg3 = (uint32_t)((Arg3) - (v_stack_m88));
        Arg1 = local_rbx;
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, (uint32_t)(0xFFFULL));
        Arg2 = v_stack_p10;
        Arg3 = 0x80000000ULL;
        Arg1 = local_rbx;
        result = MiUnmapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, (uint32_t)(0xFFFULL));
    }
    if ((local_r13 + 48 + local_r12 * 8) <= v_stack_m68) goto loc_00380EB5;
loc_00380E69:
    goto loc_00380D2F;
loc_00380E74:
    Arg2 = (Arg2) & (-2);
    if ((*(uint8_t *)(arg2)) != 2) goto loc_00380B6A;
    if ((uint32_t)(0xC0000017ULL) == 0) goto loc_00380B6A;
    result = MiPrefetchRestOfCluster(Arg2, Arg2, (uint32_t)(0xC0000017ULL), (uint32_t)(0xFFFULL));
    goto loc_00380B6A;
loc_00380E9A:
    *(uint32_t *)(arg2 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)));
    goto loc_00380D80;
loc_00380EB5:
    result = ((uint32_t)(0xC0000017ULL) * 8 - 8) >> (3);
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(arg2 + 0xBC) = (uint32_t)(result);
    goto loc_00380E69;
loc_00380ECC:
    if (condition_is_below) goto loc_00381071;
    goto loc_00380F16;
loc_00380EE0:
    result = (*(uint64_t *)(local_r13 + 0x30) + *(uint64_t *)(local_r13 + 0x30) * 2) + (*(uint64_t *)(local_r13 + 0x30) + *(uint64_t *)(local_r13 + 0x30) * 2);
    Arg1 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)) + result * 8))) >> (16));
    a4 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiZeroPhysicalPage(Arg1, *(uint64_t *)(local_r13 + 0x30), 1, a4);
    local_rbx = (local_r13 + 48) + (8);
loc_00380F16:
    if (local_rbx <= v_stack_m68) goto loc_00380EE0;
    goto loc_00380CED;
loc_00380F23:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000017ULL) + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0038103D;
loc_00380F3C:
    if ((*(uint64_t *)(v_rip + 0xAB792A)) != 0) goto loc_00380BAC;
    Arg2 = 0;
    result = KiUnstackDetachProcess(Arg2 + 104, Arg2, 1, a4);
    goto loc_00380BAC;
loc_00380F55:
    if (*(uint64_t *)(a4 + 0x8) == 0) goto loc_00380B5D;
    result = MiGetPfnSlabType(a4, Arg2, 1, a4);
    if (((uint32_t)(result)) != 9) goto loc_00380B5D;
loc_00380F78:
    if ((((uint8_t)(local_rbx)) & (32)) == 0) goto loc_00380DE4;
    goto loc_00380D2F;
loc_00380F89:
    result = MiIsRetryIoStatus((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))))), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x28)), 1, a4);
    v_stack_m80 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_0038108B;
loc_00380FA0:
    if ((((uint8_t)(local_rbx)) & (32)) == 0) goto loc_003810B0;
    goto loc_00380CED;
loc_00380FB1:
    Arg2 = (v_stack_m60) - (local_rdi);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (local_rdi);
    result = MiCopyPage((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))))), Arg2, 1, a4);
    local_rsi = (v_stack_m70 + v_stack_m70 * 2) << (4);
    local_rsi = (local_rsi) + (local_rdi);
    *(uint64_t *)(local_rsi + 0x10) = *(uint64_t *)(v_rip - 0x37077E);
    result = MiSetOriginalPtePfnFromFreeList(local_rsi + 16, Arg2, 1, a4);
    Arg1 = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    Arg1 = (uint8_t)((Arg1) & (7));
    if (((uint8_t)(Arg1)) != 3) goto loc_00380CFA;
    result = MiLockPageInline(local_rsi, Arg2, 1, a4);
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(v_stack_m60 + 0x8);
    result = MiUnlockPage(local_rsi, (uint8_t)(result), 1, a4);
    goto loc_00380CFA;
loc_0038103D:
    goto loc_00380F3C;
loc_0038104A:
    if (((v_stack_p20) & (1)) != 0) goto loc_00380DEE;
    v_stack_p20 = v_stack_m78;
    result = KeBugCheckEx(4 + 118, 4, (uint8_t)(result), Arg2);
loc_00381071:
    v_stack_p20 = v_stack_m78;
    result = KeBugCheckEx(3 + 119, 3, (uint8_t)(result), Arg2);
loc_0038108B:
    if ((*(uint32_t *)(v_rip + 0xAB6307)) != ((uint32_t)(local_rsi))) goto loc_00380FA0;
    if (((v_stack_p20) & (2)) == 0) goto loc_00380FA0;
loc_003810B0:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x50` | `32` | `W` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x58` | `32` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `W` |
| `Arg2` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0x68` | `64` | `W` |
| `Arg2` | `+ 0x70` | `32` | `W` |
| `Arg2` | `+ 0xB8` | `32` | `R` |
| `Arg2` | `+ 0xBC` | `32` | `R/W` |
| `Arg2` | `+ 0xBC` | `32` | `W` |
| `Arg2` | `+ 0xC0` | `32` | `R` |
| `Arg2` | `+ 0xC0` | `32` | `W` |
| `Arg2` | `+ 0xD0` | `64` | `R` |
| `Arg2` | `+ 0xE0` | `64` | `R` |
| `Arg2` | `+ 0xE8` | `64` | `R` |
| `Arg2` | `+ 0xF8` | `64` | `R` |
| `Arg2` | `+ 0x100` | `64` | `R` |
| `Arg2` | `+ 0x108` | `64` | `R` |
| `Arg2` | `+ 0x110` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00380AB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
