# CmpSecurityMethod

- RVA: `0x00870CC0`–`0x008714E6` (길이 `2,086` bytes)
- VA: `0x0000000140870CC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006C37C`
- 디코드: `526`개 명령, `2,086/2,086` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00870D49` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x00870D52` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00870DD8` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00870DEC` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00870E80` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00870E97` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x00870F56` → [SeQuerySecurityDescriptorInfo](SeQuerySecurityDescriptorInfo_function_00872820.md) (function, `0x00872820`)
- `0x00870F94` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00870FC3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00870FCC` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00870FD6` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00870FFD` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00871058` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00871069` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00871072` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00871090` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008710AA` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008710F9` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x0087113C` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x00871183` → [EtwpTraceRegistry](../86/EtwpTraceRegistry_function_00862980.md) (function, `0x00862980`)
- `0x008711FC` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x0087125B` → [CmpSetKeySecurity](../94/CmpSetKeySecurity_function_0094A124.md) (function, `0x0094A124`)
- `0x008712D0` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00871320` → [CmpTransReferenceTransaction](CmpTransReferenceTransaction_function_00873434.md) (function, `0x00873434`)
- `0x00871349` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00871368` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x008713BE` → [CmpTransSearchAddTrans](CmpTransSearchAddTrans_function_008743FC.md) (function, `0x008743FC`)
- `0x00871446` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x008714A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008714DC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) at `0x0086C53E`
- [ObpGrantAccess](../86/ObpGrantAccess_function_0086F250.md) at `0x0086F6CD`
- [ObpGetObjectSecurity](ObpGetObjectSecurity_function_008717E0.md) at `0x0087193B`
- [ObCheckObjectAccess](ObCheckObjectAccess_function_00872260.md) at `0x008725A2`
- [NtQuerySecurityObject](NtQuerySecurityObject_function_008737B0.md) at `0x008739CC`
- [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) at `0x008B6526`
- [ObGetObjectSecurity](../9D/ObGetObjectSecurity_function_009D45F0.md) at `0x009D473F`

### Static image references
- `0x00870CD9` → RVA `0x00E0A740` (`.data`; read)
- `0x00870CF0` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x00870D9D` → RVA `0x00EEFB88` (`.data`; read)
- `0x0087115A` → RVA `0x00862980` (`EtwpTraceRegistry`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00870D49` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x00870D52` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00870DD8` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00870DEC` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x00870E80` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00870E97` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x00870F94` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00870FC3` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00870FCC` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00870FD6` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00870FFD` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00871069` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00871072` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00871090` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008710AA` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008711FC` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008712D0` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00871349` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00871368` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x008714A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008714DC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00871485` → [sub_00B176D6](../B1/Unknown_function_00B176D6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00870CC0  40 55                           push rbp
00870CC2  53                              push rbx
00870CC3  56                              push rsi
00870CC4  57                              push rdi
00870CC5  41 54                           push r12
00870CC7  41 55                           push r13
00870CC9  41 56                           push r14
00870CCB  41 57                           push r15
00870CCD  48 8D 6C 24 88                  lea rbp, [rsp - 0x78]
00870CD2  48 81 EC 78 01 00 00            sub rsp, 0x178
00870CD9  48 8B 05 60 9A 59 00            mov rax, qword ptr [rip + 0x599a60]
00870CE0  48 33 C4                        xor rax, rsp
00870CE3  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00870CE7  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
00870CEE  33 C0                           xor eax, eax
00870CF0  48 39 05 11 73 76 00            cmp qword ptr [rip + 0x767311], rax
00870CF7  0F 57 C9                        xorps xmm1, xmm1
00870CFA  48 8B 9D E8 00 00 00            mov rbx, qword ptr [rbp + 0xe8]
00870D01  0F 57 C0                        xorps xmm0, xmm0
00870D04  48 8B BD F8 00 00 00            mov rdi, qword ptr [rbp + 0xf8]
00870D0B  4D 8B E0                        mov r12, r8
00870D0E  4C 63 FA                        movsxd r15, edx
00870D11  4C 8B E9                        mov r13, rcx
00870D14  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00870D19  4C 89 45 E8                     mov qword ptr [rbp - 0x18], r8
00870D1D  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00870D22  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00870D26  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00870D2A  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00870D2E  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00870D32  0F 11 4D 40                     movups xmmword ptr [rbp + 0x40], xmm1
00870D36  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00870D3A  0F 11 4D 50                     movups xmmword ptr [rbp + 0x50], xmm1
00870D3E  74 0E                           je 0x140870d4e
00870D40  BA 00 00 02 00                  mov edx, 0x20000
00870D45  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00870D49  E8 02 EF B2 FF                  call 0x14039fc50
00870D4E  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00870D52  E8 19 B1 B8 FF                  call 0x1403fbe70
00870D57  0F 57 C0                        xorps xmm0, xmm0
00870D5A  48 8D 45 80                     lea rax, [rbp - 0x80]
00870D5E  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00870D62  45 32 F6                        xor r14b, r14b
00870D65  48 8D 45 80                     lea rax, [rbp - 0x80]
00870D69  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00870D6D  33 C0                           xor eax, eax
00870D6F  48 39 05 92 72 76 00            cmp qword ptr [rip + 0x767292], rax
00870D76  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00870D7A  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00870D7E  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00870D82  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00870D86  0F 85 13 04 00 00               jne 0x14087119f
00870D8C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00870D95  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00870D9C  90                              nop
00870D9D  83 3D E4 ED 67 00 00            cmp dword ptr [rip + 0x67ede4], 0
00870DA4  0F 85 00 03 00 00               jne 0x1408710aa
00870DAA  41 0F B6 F6                     movzx esi, r14b
00870DAE  41 83 FF 01                     cmp r15d, 1
00870DB2  0F 85 52 03 00 00               jne 0x14087110a
00870DB8  33 C0                           xor eax, eax
00870DBA  0F 57 C0                        xorps xmm0, xmm0
00870DBD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00870DC2  32 DB                           xor bl, bl
00870DC4  B8 FF FF FF FF                  mov eax, 0xffffffff
00870DC9  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00870DCE  66 89 44 24 62                  mov word ptr [rsp + 0x62], ax
00870DD3  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00870DD8  E8 23 86 35 00                  call 0x140bc9400
00870DDD  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00870DE1  0F B6 F8                        movzx edi, al
00870DE4  84 C0                           test al, al
00870DE6  0F 84 BA 06 00 00               je 0x1408714a6
00870DEC  E8 43 8D 35 00                  call 0x140bc9b34
00870DF1  49 8B 7D 08                     mov rdi, qword ptr [r13 + 8]
00870DF5  45 33 C0                        xor r8d, r8d
00870DF8  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
00870DFD  45 8B E0                        mov r12d, r8d
00870E00  0F BF 5F 42                     movsx ebx, word ptr [rdi + 0x42]
00870E04  83 FB 02                        cmp ebx, 2
00870E07  7C 0B                           jl 0x140870e14
00870E09  8B C3                           mov eax, ebx
00870E0B  41 2B C7                        sub eax, r15d
00870E0E  0F 85 AB 04 00 00               jne 0x1408712bf
00870E14  4C 0F BF 77 42                  movsx r14, word ptr [rdi + 0x42]
00870E19  44 0F B6 FE                     movzx r15d, sil
00870E1D  66 89 5C 24 60                  mov word ptr [rsp + 0x60], bx
00870E22  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00870E27  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00870E2C  66 44 89 74 24 62               mov word ptr [rsp + 0x62], r14w
00870E32  66 45 85 F6                     test r14w, r14w
00870E36  0F 85 33 04 00 00               jne 0x14087126f
00870E3C  4A 89 7C F4 68                  mov qword ptr [rsp + r14*8 + 0x68], rdi
00870E41  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00870E46  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00870E4B  44 0F B7 74 24 62               movzx r14d, word ptr [rsp + 0x62]
00870E51  41 0F B7 D8                     movzx ebx, r8w
00870E55  66 45 3B C6                     cmp r8w, r14w
00870E59  7F 37                           jg 0x140870e92
00870E5B  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00870E60  49 8B F4                        mov rsi, r12
00870E63  48 2B F1                        sub rsi, rcx
00870E66  48 8D 7C 24 68                  lea rdi, [rsp + 0x68]
00870E6B  48 83 C6 F0                     add rsi, -0x10
00870E6F  90                              nop
00870E70  66 83 FB 02                     cmp bx, 2
00870E74  0F 8D 1C 03 00 00               jge 0x140871196
00870E7A  48 8B CF                        mov rcx, rdi
00870E7D  48 8B 09                        mov rcx, qword ptr [rcx]
00870E80  E8 97 8B 35 00                  call 0x140bc9a1c
00870E85  66 FF C3                        inc bx
00870E88  48 83 C7 08                     add rdi, 8
00870E8C  66 41 3B DE                     cmp bx, r14w
00870E90  7E DE                           jle 0x140870e70
00870E92  33 D2                           xor edx, edx
00870E94  49 8B CD                        mov rcx, r13
00870E97  E8 34 89 35 00                  call 0x140bc97d0
00870E9C  8B F0                           mov esi, eax
00870E9E  85 C0                           test eax, eax
00870EA0  0F 88 BF 00 00 00               js 0x140870f65
00870EA6  49 8B 5D 38                     mov rbx, qword ptr [r13 + 0x38]
00870EAA  48 85 DB                        test rbx, rbx
00870EAD  0F 85 36 04 00 00               jne 0x1408712e9
00870EB3  49 39 5D 40                     cmp qword ptr [r13 + 0x40], rbx
00870EB7  0F 85 2C 04 00 00               jne 0x1408712e9
00870EBD  33 C9                           xor ecx, ecx
00870EBF  41 0F B7 C6                     movzx eax, r14w
00870EC3  44 8B F9                        mov r15d, ecx
00870EC6  66 45 85 F6                     test r14w, r14w
00870ECA  78 5F                           js 0x140870f2b
00870ECC  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00870ED1  44 8D 69 FF                     lea r13d, [rcx - 1]
00870ED5  0F B7 F8                        movzx edi, ax
00870ED8  83 FF 02                        cmp edi, 2
00870EDB  0F 83 DD 02 00 00               jae 0x1408711be
00870EE1  48 8B 5C FC 68                  mov rbx, qword ptr [rsp + rdi*8 + 0x68]
00870EE6  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
00870EEB  74 06                           je 0x140870ef3
00870EED  80 7B 41 01                     cmp byte ptr [rbx + 0x41], 1
00870EF1  74 32                           je 0x140870f25
00870EF3  83 7B 28 FF                     cmp dword ptr [rbx + 0x28], -1
00870EF7  0F 84 4C 02 00 00               je 0x140871149
00870EFD  48 8B 93 F0 00 00 00            mov rdx, qword ptr [rbx + 0xf0]
00870F04  48 85 D2                        test rdx, rdx
00870F07  0F 85 2C 02 00 00               jne 0x140871139
00870F0D  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
00870F12  4C 8B FB                        mov r15, rbx
00870F15  74 06                           je 0x140870f1d
00870F17  80 7B 41 00                     cmp byte ptr [rbx + 0x41], 0
00870F1B  75 08                           jne 0x140870f25
00870F1D  41 8B C5                        mov eax, r13d
00870F20  66 03 C7                        add ax, di
00870F23  79 B0                           jns 0x140870ed5
00870F25  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
00870F29  33 C9                           xor ecx, ecx
00870F2B  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00870F30  49 8B 5F 58                     mov rbx, qword ptr [r15 + 0x58]
00870F34  4D 85 C0                        test r8, r8
00870F37  0F 85 A6 04 00 00               jne 0x1408713e3
00870F3D  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
00870F41  48 8D 43 20                     lea rax, [rbx + 0x20]
00870F45  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00870F4A  4C 8D 4D A0                     lea r9, [rbp - 0x60]
00870F4E  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00870F52  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00870F56  E8 C5 18 00 00                  call 0x140872820
00870F5B  8B F0                           mov esi, eax
00870F5D  85 C0                           test eax, eax
00870F5F  0F 89 50 02 00 00               jns 0x1408711b5
00870F65  33 C0                           xor eax, eax
00870F67  0F B7 D8                        movzx ebx, ax
00870F6A  66 41 3B C6                     cmp ax, r14w
00870F6E  7F 36                           jg 0x140870fa6
00870F70  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00870F75  4D 8B FC                        mov r15, r12
00870F78  4C 2B F9                        sub r15, rcx
00870F7B  48 8D 7C 24 68                  lea rdi, [rsp + 0x68]
00870F80  49 83 C7 F0                     add r15, -0x10
00870F84  66 83 FB 02                     cmp bx, 2
00870F88  0F 8D FF 01 00 00               jge 0x14087118d
00870F8E  48 8B CF                        mov rcx, rdi
00870F91  48 8B 09                        mov rcx, qword ptr [rcx]
00870F94  E8 27 83 35 00                  call 0x140bc92c0
00870F99  66 FF C3                        inc bx
00870F9C  48 83 C7 08                     add rdi, 8
00870FA0  66 41 3B DE                     cmp bx, r14w
00870FA4  7E DE                           jle 0x140870f84
00870FA6  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00870FAB  44 0F B6 74 24 40               movzx r14d, byte ptr [rsp + 0x40]
00870FB1  0F B6 5C 24 41                  movzx ebx, byte ptr [rsp + 0x41]
00870FB6  0F B6 7C 24 42                  movzx edi, byte ptr [rsp + 0x42]
00870FBB  4D 85 E4                        test r12, r12
00870FBE  74 08                           je 0x140870fc8
00870FC0  49 8B CC                        mov rcx, r12
00870FC3  E8 B8 4D C0 FF                  call 0x140475d80
00870FC8  84 DB                           test bl, bl
00870FCA  74 05                           je 0x140870fd1
00870FCC  E8 B3 8A 35 00                  call 0x140bc9a84
00870FD1  40 84 FF                        test dil, dil
00870FD4  74 05                           je 0x140870fdb
00870FD6  E8 A5 88 35 00                  call 0x140bc9880
00870FDB  85 F6                           test esi, esi
00870FDD  0F 89 3C 01 00 00               jns 0x14087111f
00870FE3  33 DB                           xor ebx, ebx
00870FE5  45 84 F6                        test r14b, r14b
00870FE8  74 76                           je 0x140871060
00870FEA  41 83 FF 01                     cmp r15d, 1
00870FEE  0F 85 F2 01 00 00               jne 0x1408711e6
00870FF4  83 3D 8D EB 67 00 00            cmp dword ptr [rip + 0x67eb8d], 0
00870FFB  74 63                           je 0x140871060
00870FFD  E8 7A 5A BE FF                  call 0x140456a7c
00871002  85 C0                           test eax, eax
00871004  75 5A                           jne 0x140871060
00871006  48 8D 45 80                     lea rax, [rbp - 0x80]
0087100A  48 39 45 80                     cmp qword ptr [rbp - 0x80], rax
0087100E  74 50                           je 0x140871060
00871010  48 8D 45 F0                     lea rax, [rbp - 0x10]
00871014  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00871018  41 8D 4F 24                     lea ecx, [r15 + 0x24]
0087101C  48 8D 45 80                     lea rax, [rbp - 0x80]
00871020  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00871025  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0087102A  C7 44 24 20 25 00 00 00         mov dword ptr [rsp + 0x20], 0x25
00871032  0F 57 C0                        xorps xmm0, xmm0
00871035  89 5D B4                        mov dword ptr [rbp - 0x4c], ebx
00871038  45 33 C9                        xor r9d, r9d
0087103B  48 89 5D D4                     mov qword ptr [rbp - 0x2c], rbx
0087103F  45 33 C0                        xor r8d, r8d
00871042  89 5D DC                        mov dword ptr [rbp - 0x24], ebx
00871045  48 8D 55 A8                     lea rdx, [rbp - 0x58]
00871049  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
0087104D  F3 0F 7F 45 C4                  movdqu xmmword ptr [rbp - 0x3c], xmm0
00871052  89 75 B0                        mov dword ptr [rbp - 0x50], esi
00871055  89 75 C0                        mov dword ptr [rbp - 0x40], esi
00871058  E8 E3 4E FF FF                  call 0x140865f40
0087105D  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
00871060  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00871069  E8 82 DF 9E FF                  call 0x14025eff0
0087106E  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00871072  E8 D9 EC BA FF                  call 0x14041fd50
00871077  48 8B 05 8A 6F 76 00            mov rax, qword ptr [rip + 0x766f8a]
0087107E  48 85 C0                        test rax, rax
00871081  0F 85 CB 00 00 00               jne 0x140871152
00871087  8B C6                           mov eax, esi
00871089  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
0087108D  48 33 CC                        xor rcx, rsp
00871090  E8 AB B5 E3 FF                  call 0x1406ac640
00871095  48 81 C4 78 01 00 00            add rsp, 0x178
0087109C  41 5F                           pop r15
0087109E  41 5E                           pop r14
008710A0  41 5D                           pop r13
008710A2  41 5C                           pop r12
008710A4  5F                              pop rdi
008710A5  5E                              pop rsi
008710A6  5B                              pop rbx
008710A7  5D                              pop rbp
008710A8  C3                              ret
008710A9  CC                              int3
008710AA  E8 CD 59 BE FF                  call 0x140456a7c
008710AF  85 C0                           test eax, eax
008710B1  0F 85 F3 FC FF FF               jne 0x140870daa
008710B7  41 83 FF 01                     cmp r15d, 1
008710BB  0F 85 07 01 00 00               jne 0x1408711c8
008710C1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008710C6  41 8D 4F 23                     lea ecx, [r15 + 0x23]
008710CA  48 89 45 00                     mov qword ptr [rbp], rax
008710CE  8D 41 01                        lea eax, [rcx + 1]
008710D1  48 89 75 08                     mov qword ptr [rbp + 8], rsi
008710D5  48 8D 55 80                     lea rdx, [rbp - 0x80]
008710D9  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
008710DD  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
008710E2  41 B1 01                        mov r9b, 1
008710E5  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008710EA  48 8D 55 F0                     lea rdx, [rbp - 0x10]
008710EE  45 33 C0                        xor r8d, r8d
008710F1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008710F5  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
008710F9  E8 42 4E FF FF                  call 0x140865f40
008710FE  85 C0                           test eax, eax
00871100  78 26                           js 0x140871128
00871102  41 B6 01                        mov r14b, 1
00871105  E9 A0 FC FF FF                  jmp 0x140870daa
0087110A  41 8B CF                        mov ecx, r15d
0087110D  45 85 FF                        test r15d, r15d
00871110  0F 84 28 01 00 00               je 0x14087123e
00871116  83 E9 02                        sub ecx, 2
00871119  0F 85 63 03 00 00               jne 0x140871482
0087111F  33 DB                           xor ebx, ebx
00871121  8B F3                           mov esi, ebx
00871123  E9 BD FE FF FF                  jmp 0x140870fe5
00871128  33 DB                           xor ebx, ebx
0087112A  3D 03 05 00 C0                  cmp eax, 0xc0000503
0087112F  8B F3                           mov esi, ebx
00871131  0F 45 F0                        cmovne esi, eax
00871134  E9 27 FF FF FF                  jmp 0x140871060
00871139  48 8B CE                        mov rcx, rsi
0087113C  E8 1F AE FD FF                  call 0x14084bf60
00871141  84 C0                           test al, al
00871143  0F 85 C4 FD FF FF               jne 0x140870f0d
00871149  41 0F B7 C5                     movzx eax, r13w
0087114D  E9 CE FD FF FF                  jmp 0x140870f20
00871152  45 85 FF                        test r15d, r15d
00871155  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0087115A  48 8D 15 1F 18 FF FF            lea rdx, [rip - 0xe7e1]
00871161  44 8B C6                        mov r8d, esi
00871164  0F 95 C1                        setne cl
00871167  45 33 C9                        xor r9d, r9d
0087116A  80 C1 1C                        add cl, 0x1c
0087116D  48 3B C2                        cmp rax, rdx
00871170  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00871174  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00871179  48 8D 55 40                     lea rdx, [rbp + 0x40]
0087117D  0F 85 59 03 00 00               jne 0x1408714dc
00871183  E8 F8 17 FF FF                  call 0x140862980
00871188  E9 FA FE FF FF                  jmp 0x140871087
0087118D  4A 8D 0C 3F                     lea rcx, [rdi + r15]
00871191  E9 FB FD FF FF                  jmp 0x140870f91
00871196  48 8D 0C 3E                     lea rcx, [rsi + rdi]
0087119A  E9 DE FC FF FF                  jmp 0x140870e7d
0087119F  4D 85 ED                        test r13, r13
008711A2  0F 84 E4 FB FF FF               je 0x140870d8c
008711A8  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
008711AC  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
008711B0  E9 D7 FB FF FF                  jmp 0x140870d8c
008711B5  33 C0                           xor eax, eax
008711B7  8B F0                           mov esi, eax
008711B9  E9 A9 FD FF FF                  jmp 0x140870f67
008711BE  49 8B 5C FC F0                  mov rbx, qword ptr [r12 + rdi*8 - 0x10]
008711C3  E9 1E FD FF FF                  jmp 0x140870ee6
008711C8  45 85 FF                        test r15d, r15d
008711CB  0F 85 39 FF FF FF               jne 0x14087110a
008711D1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008711D6  41 8D 4F 26                     lea ecx, [r15 + 0x26]
008711DA  48 89 45 00                     mov qword ptr [rbp], rax
008711DE  8D 41 01                        lea eax, [rcx + 1]
008711E1  E9 EF FE FF FF                  jmp 0x1408710d5
008711E6  45 85 FF                        test r15d, r15d
008711E9  0F 85 71 FE FF FF               jne 0x140871060
008711EF  44 39 3D 92 E9 67 00            cmp dword ptr [rip + 0x67e992], r15d
008711F6  0F 84 64 FE FF FF               je 0x140871060
008711FC  E8 7B 58 BE FF                  call 0x140456a7c
00871201  85 C0                           test eax, eax
00871203  0F 85 57 FE FF FF               jne 0x140871060
00871209  48 8D 45 80                     lea rax, [rbp - 0x80]
0087120D  48 39 45 80                     cmp qword ptr [rbp - 0x80], rax
00871211  0F 84 49 FE FF FF               je 0x140871060
00871217  48 8D 45 F0                     lea rax, [rbp - 0x10]
0087121B  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0087121F  41 8D 4F 27                     lea ecx, [r15 + 0x27]
00871223  48 8D 45 80                     lea rax, [rbp - 0x80]
00871227  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0087122C  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00871231  C7 44 24 20 27 00 00 00         mov dword ptr [rsp + 0x20], 0x27
00871239  E9 F4 FD FF FF                  jmp 0x140871032
0087123E  8B 85 F0 00 00 00               mov eax, dword ptr [rbp + 0xf0]
00871244  4C 8B CB                        mov r9, rbx
00871247  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0087124C  49 8B D4                        mov rdx, r12
0087124F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00871254  49 8B CD                        mov rcx, r13
00871257  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087125B  E8 C4 8E 0D 00                  call 0x14094a124
00871260  8B F0                           mov esi, eax
00871262  85 C0                           test eax, eax
00871264  0F 88 79 FD FF FF               js 0x140870fe3
0087126A  E9 B0 FE FF FF                  jmp 0x14087111f
0087126F  48 8B 87 C0 00 00 00            mov rax, qword ptr [rdi + 0xc0]
00871276  48 85 C0                        test rax, rax
00871279  0F 84 D2 FB FF FF               je 0x140870e51
0087127F  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00871284  0F 1F 40 00                     nop dword ptr [rax]
00871288  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00871290  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
00871294  49 0F BF D6                     movsx rdx, r14w
00871298  66 41 83 FE 02                  cmp r14w, 2
0087129D  0F 8D D5 01 00 00               jge 0x140871478
008712A3  48 89 4C D4 68                  mov qword ptr [rsp + rdx*8 + 0x68], rcx
008712A8  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
008712AD  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
008712B1  66 41 FF CE                     dec r14w
008712B5  48 85 C0                        test rax, rax
008712B8  75 D6                           jne 0x140871290
008712BA  E9 8C FB FF FF                  jmp 0x140870e4b
008712BF  8B D0                           mov edx, eax
008712C1  B9 00 01 00 00                  mov ecx, 0x100
008712C6  48 C1 E2 03                     shl rdx, 3
008712CA  41 B8 43 4D 36 35               mov r8d, 0x35364d43
008712D0  E8 2F C2 B5 FF                  call 0x1403cd504
008712D5  4C 8B E0                        mov r12, rax
008712D8  48 85 C0                        test rax, rax
008712DB  0F 84 D4 01 00 00               je 0x1408714b5
008712E1  45 33 C0                        xor r8d, r8d
008712E4  E9 2B FB FF FF                  jmp 0x140870e14
008712E9  33 FF                           xor edi, edi
008712EB  8B C7                           mov eax, edi
008712ED  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008712F2  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008712F6  48 85 DB                        test rbx, rbx
008712F9  0F 84 57 01 00 00               je 0x140871456
008712FF  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00871303  48 8B D1                        mov rdx, rcx
00871306  48 83 F2 01                     xor rdx, 1
0087130A  F6 C1 01                        test cl, 1
0087130D  48 0F 44 D1                     cmove rdx, rcx
00871311  F6 C3 01                        test bl, 1
00871314  74 6B                           je 0x140871381
00871316  48 8B FB                        mov rdi, rbx
00871319  48 8B CB                        mov rcx, rbx
0087131C  48 83 E7 FE                     and rdi, 0xfffffffffffffffe
00871320  E8 0F 21 00 00                  call 0x140873434
00871325  8B F0                           mov esi, eax
00871327  85 C0                           test eax, eax
00871329  78 2E                           js 0x140871359
0087132B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0087132F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00871334  48 85 C0                        test rax, rax
00871337  0F 84 93 00 00 00               je 0x1408713d0
0087133D  33 C0                           xor eax, eax
0087133F  8B F0                           mov esi, eax
00871341  48 85 DB                        test rbx, rbx
00871344  74 08                           je 0x14087134e
00871346  48 8B CF                        mov rcx, rdi
00871349  E8 02 80 A8 FF                  call 0x1402f9350
0087134E  44 0F B7 74 24 62               movzx r14d, word ptr [rsp + 0x62]
00871354  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00871359  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0087135E  85 F6                           test esi, esi
00871360  78 3E                           js 0x1408713a0
00871362  48 8B D0                        mov rdx, rax
00871365  49 8B CD                        mov rcx, r13
00871368  E8 63 84 35 00                  call 0x140bc97d0
0087136D  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
00871372  8B F0                           mov esi, eax
00871374  85 C0                           test eax, eax
00871376  0F 88 E9 FB FF FF               js 0x140870f65
0087137C  E9 3C FB FF FF                  jmp 0x140870ebd
00871381  4C 8B 4A 20                     mov r9, qword ptr [rdx + 0x20]
00871385  4D 8B 81 38 10 00 00            mov r8, qword ptr [r9 + 0x1038]
0087138C  4D 85 C0                        test r8, r8
0087138F  75 19                           jne 0x1408713aa
00871391  BE 05 00 19 C0                  mov esi, 0xc0190005
00871396  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0087139B  E9 C7 FB FF FF                  jmp 0x140870f67
008713A0  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
008713A5  E9 BB FB FF FF                  jmp 0x140870f65
008713AA  49 8B 55 40                     mov rdx, qword ptr [r13 + 0x40]
008713AE  48 8D 45 90                     lea rax, [rbp - 0x70]
008713B2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008713B7  48 8B CB                        mov rcx, rbx
008713BA  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
008713BE  E8 39 30 00 00                  call 0x1408743fc
008713C3  8B F0                           mov esi, eax
008713C5  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
008713C9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008713CE  EB 8E                           jmp 0x14087135e
008713D0  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
008713D4  BE 02 00 19 C0                  mov esi, 0xc0190002
008713D9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008713DE  E9 5E FF FF FF                  jmp 0x140871341
008713E3  49 81 C7 D0 00 00 00            add r15, 0xd0
008713EA  49 8B 77 08                     mov rsi, qword ptr [r15 + 8]
008713EE  4C 3B FE                        cmp r15, rsi
008713F1  75 2E                           jne 0x140871421
008713F3  48 8B F9                        mov rdi, rcx
008713F6  48 85 FF                        test rdi, rdi
008713F9  0F 84 3E FB FF FF               je 0x140870f3d
008713FF  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
00871403  48 85 C9                        test rcx, rcx
00871406  74 0B                           je 0x140871413
00871408  49 3B C8                        cmp rcx, r8
0087140B  75 24                           jne 0x140871431
0087140D  83 7F 44 09                     cmp dword ptr [rdi + 0x44], 9
00871411  74 5C                           je 0x14087146f
00871413  48 85 F6                        test rsi, rsi
00871416  75 04                           jne 0x14087141c
00871418  49 8B 77 08                     mov rsi, qword ptr [r15 + 8]
0087141C  4C 3B FE                        cmp r15, rsi
0087141F  74 0A                           je 0x14087142b
00871421  48 8D 7E E0                     lea rdi, [rsi - 0x20]
00871425  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00871429  EB CB                           jmp 0x1408713f6
0087142B  33 C0                           xor eax, eax
0087142D  8B F8                           mov edi, eax
0087142F  EB C5                           jmp 0x1408713f6
00871431  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
00871435  48 85 D2                        test rdx, rdx
00871438  0F 85 86 00 00 00               jne 0x1408714c4
0087143E  49 8D 50 58                     lea rdx, [r8 + 0x58]
00871442  48 83 C1 58                     add rcx, 0x58
00871446  E8 81 35 E9 FF                  call 0x1407049cc
0087144B  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00871450  84 C0                           test al, al
00871452  74 BF                           je 0x140871413
00871454  EB B7                           jmp 0x14087140d
00871456  49 39 45 40                     cmp qword ptr [r13 + 0x40], rax
0087145A  0F 85 9F FE FF FF               jne 0x1408712ff
00871460  BE 02 00 19 C0                  mov esi, 0xc0190002
00871465  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0087146A  E9 F8 FA FF FF                  jmp 0x140870f67
0087146F  48 8B 5F 58                     mov rbx, qword ptr [rdi + 0x58]
00871473  E9 C5 FA FF FF                  jmp 0x140870f3d
00871478  49 89 4C D4 F0                  mov qword ptr [r12 + rdx*8 - 0x10], rcx
0087147D  E9 2B FE FF FF                  jmp 0x1408712ad
00871482  83 F9 01                        cmp ecx, 1
00871485  0F 84 4B 62 2A 00               je 0x140b176d6
0087148B  4D 8B 4D 08                     mov r9, qword ptr [r13 + 8]
0087148F  BA 05 00 00 00                  mov edx, 5
00871494  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00871499  8D 4A 4C                        lea ecx, [rdx + 0x4c]
0087149C  44 8D 42 FC                     lea r8d, [rdx - 4]
008714A0  E8 BB C1 C8 FF                  call 0x1404fd660
008714A5  CC                              int3
008714A6  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
008714AB  BE 89 01 00 C0                  mov esi, 0xc0000189
008714B0  E9 06 FB FF FF                  jmp 0x140870fbb
008714B5  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
008714BA  BE 9A 00 00 C0                  mov esi, 0xc000009a
008714BF  E9 ED FA FF FF                  jmp 0x140870fb1
008714C4  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
008714C8  48 85 C0                        test rax, rax
008714CB  0F 84 6D FF FF FF               je 0x14087143e
008714D1  48 3B D0                        cmp rdx, rax
008714D4  0F 94 C0                        sete al
008714D7  E9 74 FF FF FF                  jmp 0x140871450
008714DC  E8 EF 95 E4 FF                  call 0x1406baad0
008714E1  E9 A1 FB FF FF                  jmp 0x140871087
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSecurityMethod(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int16 v_stack_m156;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m176;
    unsigned __int8 v_stack_m177;
    unsigned __int8 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE4;
    unsigned __int64 v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int16 v_stack_p62;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (376);
    result = (*(unsigned __int64 *)(v_rip + 5872224)) ^ (v_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m160 = a4;
    v_stack_mD0 = a3;
    v_stack_m168 = (unsigned int)((int)(a2));
    v_stack_m118 = a1;
    v_stack_mD8 = a5;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm1;
    v_stack_m120 = 0;
    v_stack_m68 = v_xmm1;
    if ((*(unsigned __int64 *)(v_rip + 7762705)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_stack_m78;
        result = EtwGetKernelTraceTimestamp(a1, a2, a3, a4);
    }
    result = CmpInitializeThreadInfo(v_stack_m90, a2, a3, a4);
    v_stack_m130 = v_stack_m138;
    v_r14 = 0;
    v_stack_m138 = v_stack_m138;
    result = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    if ((*(unsigned __int64 *)(v_rip + 7762578)) != 0) goto loc_0087119F;
loc_00870D8C:
    if ((*(unsigned int *)(v_rip + 6811108)) != 0) goto loc_008710AA;
loc_00870DAA:
    if (((unsigned int)((int)(a2))) != 1) goto loc_0087110A;
    result = 0;
    v_stack_m170 = 0;
    v_rbx = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m156 = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m148 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m90, a2, a3, a4);
    v_stack_m176 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_008714A6;
    result = CmpLockRegistry(v_stack_m90, a2, a3, a4);
    a3 = 0;
    v_stack_m177 = (unsigned __int8)((int)(a2));
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)))) < 2) goto loc_00870E14;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))))) - ((unsigned int)((int)(a2))));
    if (condition_is_not_equal) goto loc_008712BF;
loc_00870E14:
    v_stack_m158 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    v_stack_m140 = 0;
    v_stack_m178 = 0;
    v_stack_m156 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) != 0) goto loc_0087126F;
    *(unsigned __int64 *)(v_rsp + (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) * 8 + 104) = *(unsigned __int64 *)(a1 + 8);
    v_stack_m178 = 0;
loc_00870E4B:
loc_00870E51:
    if (0 > ((unsigned __int16)(v_stack_m156))) goto loc_00870E92;
    v_rsi = (v_stack_m140) - (v_stack_m150);
    v_rsi = (v_rsi) + (-16);
loc_00870E70:
    if (0 >= 2) goto loc_00871196;
loc_00870E7D:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m150), a2, a3, a4);
    v_rbx = (unsigned __int16)((0) + 1);
    v_rdi = (v_stack_m150) + (8);
    if (((unsigned __int16)(v_rbx)) <= ((unsigned __int16)(v_stack_m156))) goto loc_00870E70;
loc_00870E92:
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, a3, a4);
    if (sign_flag) goto loc_00870F65;
    if (*(unsigned __int64 *)(a1 + 56) != 0) goto loc_008712E9;
    if ((*(unsigned __int64 *)(a1 + 64)) != (*(unsigned __int64 *)(a1 + 56))) goto loc_008712E9;
loc_00870EBD:
    a1 = 0;
    if (sign_flag) goto loc_00870F2B;
loc_00870ED5:
    if (((unsigned int)((unsigned __int16)((unsigned __int16)(v_stack_m156)))) >= 2) goto loc_008711BE;
loc_00870EE6:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 66)) == 0) goto loc_00870EF3;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 65)) == 1) goto loc_00870F25;
loc_00870EF3:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 40)) == -1) goto loc_00871149;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 240) != 0) goto loc_00871139;
loc_00870F0D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 66)) == 0) goto loc_00870F1D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 65)) != 0) goto loc_00870F25;
loc_00870F1D:
loc_00870F20:
    result = (unsigned __int16)(((unsigned int)((unsigned int)(a1 - 1))) + ((unsigned __int16)((unsigned __int16)((unsigned __int16)(v_stack_m156)))));
    if (!sign_flag) goto loc_00870ED5;
loc_00870F25:
    a1 = 0;
loc_00870F2B:
    if (v_stack_m170 != 0) goto loc_008713E3;
loc_00870F3D:
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_stack_m156)) * 8 + 104) + 88) + 32;
    result = SeQuerySecurityDescriptorInfo(v_stack_mD0, v_stack_m160, v_stack_mD8, v_stack_m118);
    if (!sign_flag) goto loc_008711B5;
loc_00870F65:
    result = 0;
loc_00870F67:
    if (0 > ((unsigned __int16)(v_stack_m156))) goto loc_00870FA6;
    v_r15 = (v_stack_m140) - (v_stack_m150);
    v_r15 = (v_r15) + (-16);
loc_00870F84:
    if (0 >= 2) goto loc_0087118D;
loc_00870F91:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m150), v_stack_m160, v_stack_mD8, v_stack_m118);
    v_rbx = (unsigned __int16)((0) + 1);
    v_rdi = (v_stack_m150) + (8);
    if (((unsigned __int16)(v_rbx)) <= ((unsigned __int16)(v_stack_m156))) goto loc_00870F84;
loc_00870FA6:
loc_00870FB1:
loc_00870FBB:
    if (v_stack_m140 != 0) {
        a1 = v_stack_m140;
        result = CmSiFreeMemory(a1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if ((unsigned __int8)(v_stack_m177) != 0) {
        result = CmpUnlockRegistry(a1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if ((unsigned __int8)(v_stack_m176) != 0) {
        result = CmpReleaseShutdownRundown(a1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if (!sign_flag) goto loc_0087111F;
loc_00870FE3:
    v_rbx = 0;
loc_00870FE5:
    if ((unsigned __int8)(v_stack_m178) == 0) goto loc_00871060;
    if (((unsigned int)((unsigned int)(v_stack_m168))) != 1) goto loc_008711E6;
    if ((*(unsigned int *)(v_rip + 6810509)) == 0) goto loc_00871060;
    result = CmpIsRegistryLockAcquired(a1, v_stack_m160, v_stack_mD8, v_stack_m118);
    if ((unsigned int)(result) != 0) goto loc_00871060;
    if (v_stack_m138 == v_stack_m138) goto loc_00871060;
    v_stack_m100 = v_stack_mC8;
    v_stack_m188 = v_stack_m138;
    v_stack_m190 = v_stack_m118;
    v_stack_m198 = 37;
loc_00871032:
    v_stack_m104 = 0;
    a4 = 0;
    v_stack_mE4 = 0;
    a3 = 0;
    v_stack_mDC = 0;
    v_stack_m110 = v_stack_m118;
    v_stack_mF4 = v_xmm0;
    v_stack_m108 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = CmpCallCallBacksEx((unsigned int)(v_stack_m168) + 36, v_stack_m110, a3, a4);
loc_00871060:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m110, a3, a4);
    result = CmCleanupThreadInfo(v_stack_m90, v_stack_m110, a3, a4);
    if (*(unsigned __int64 *)(v_rip + 7761802) != 0) goto loc_00871152;
loc_00871087:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m110, a3, a4);
    v_rsp = (v_rsp) + (376);
    return result;
loc_008710AA:
    result = CmpIsRegistryLockAcquired(a1, v_stack_m110, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00870DAA;
    if (((unsigned int)((unsigned int)(v_stack_m168))) != 1) goto loc_008711C8;
    v_stack_mB8 = v_stack_p58;
    v_stack_mB0 = (unsigned int)(v_stack_mF8);
loc_008710D5:
    v_stack_mC0 = v_stack_m140;
    v_stack_p30 = v_stack_m138;
    v_stack_p28 = v_stack_m118;
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m168) + 35 + 1);
    v_stack_mC8 = v_stack_m118;
    result = CmpCallCallBacksEx((unsigned int)(v_stack_m168) + 35, v_stack_mC8, a3, 1);
    if (sign_flag) goto loc_00871128;
    goto loc_00870DAA;
loc_0087110A:
    if ((unsigned int)((unsigned int)(v_stack_m168)) == 0) goto loc_0087123E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m168)))) - (2));
    if (condition_is_not_equal) goto loc_00871482;
loc_0087111F:
    v_rbx = 0;
    goto loc_00870FE5;
loc_00871128:
    v_rbx = 0;
    v_rsi = 0;
    if (((unsigned int)(result)) != 0xC0000503ULL) { v_rsi = (unsigned int)(result); }
    goto loc_00871060;
loc_00871139:
    result = CmEqualTrans(v_rsi, v_stack_mC8, a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00870F0D;
loc_00871149:
    goto loc_00870F20;
loc_00871152:
    v_stack_p28 = 0;
    a1 = ((unsigned int)((unsigned int)(v_stack_m168)) != 0) ? 1 : 0;
    a4 = 0;
    a1 = (unsigned __int8)((a1) + (28));
    v_stack_p20 = v_stack_m120;
    if (((unsigned __int16)(v_stack_m118)) != (v_rip - 59361)) goto loc_008714DC;
    result = EtwpTraceRegistry(a1, v_stack_m78, (unsigned int)((unsigned int)(v_rsi)), a4);
    goto loc_00871087;
loc_0087118D:
    goto loc_00870F91;
loc_00871196:
    goto loc_00870E7D;
loc_0087119F:
    if (v_stack_m118 == 0) goto loc_00870D8C;
    v_stack_m120 = *(unsigned __int64 *)(v_stack_m118 + 8);
    goto loc_00870D8C;
loc_008711B5:
    result = 0;
    goto loc_00870F67;
loc_008711BE:
    goto loc_00870EE6;
loc_008711C8:
    if ((unsigned int)((unsigned int)(v_stack_m168)) != 0) goto loc_0087110A;
    v_stack_mB8 = v_stack_p58;
    goto loc_008710D5;
loc_008711E6:
    if ((unsigned int)((unsigned int)(v_stack_m168)) != 0) goto loc_00871060;
    if ((*(unsigned int *)(v_rip + 6810002)) == ((unsigned int)((unsigned int)(v_stack_m168)))) goto loc_00871060;
    result = CmpIsRegistryLockAcquired((unsigned int)(v_stack_m168) + 38, v_stack_m78, (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned int)(result) != 0) goto loc_00871060;
    if (v_stack_m138 == v_stack_m138) goto loc_00871060;
    v_stack_m100 = v_stack_mC8;
    v_stack_p30 = v_stack_m138;
    v_stack_p28 = v_stack_m118;
    v_stack_p20 = 39;
    goto loc_00871032;
loc_0087123E:
    v_stack_p28 = v_stack_m176;
    v_stack_p20 = (unsigned int)((unsigned int)(a7));
    result = CmpSetKeySecurity(v_stack_m118, v_stack_m140, v_stack_p58, *(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16));
    if (sign_flag) goto loc_00870FE3;
    goto loc_0087111F;
loc_0087126F:
    if (*(unsigned __int64 *)(v_stack_m176 + 192) == 0) goto loc_00870E51;
    v_stack_p40 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
loc_00871290:
    if (1 >= 2) goto loc_00871478;
    *(unsigned __int64 *)(v_rsp + (__int16)(1) * 8 + 104) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m176 + 192) + 16);
loc_008712AD:
    v_r14 = (unsigned __int16)((1) - 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m176 + 192) + 24) != 0) goto loc_00871290;
    goto loc_00870E4B;
loc_008712BF:
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m176 + 192) + 24)))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), *(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16));
    if (result == 0) goto loc_008714B5;
    a3 = 0;
    goto loc_00870E14;
loc_008712E9:
    v_rdi = 0;
    v_stack_p48 = 0;
    v_stack_m128 = 0;
    if (*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) == 0) goto loc_00871456;
loc_008712FF:
    a2 = (*(unsigned __int64 *)(v_stack_m118 + 8)) ^ (1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m118 + 8))) & (1)) == 0) { a2 = *(unsigned __int64 *)(v_stack_m118 + 8); }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16))) & (1)) == 0) goto loc_00871381;
    v_rdi = (*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16)) & (-2);
    result = CmpTransReferenceTransaction(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16), a2, a3, *(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16));
    if (sign_flag) goto loc_00871359;
    v_stack_p48 = *(unsigned __int64 *)(v_rdi + 16);
    if (*(unsigned __int64 *)(v_rdi + 16) == 0) goto loc_008713D0;
    result = 0;
loc_00871341:
    if (*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) != 0) {
        a1 = v_rdi;
        result = ObfDereferenceObject(a1, a2, a3, *(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16));
    }
loc_00871359:
loc_0087135E:
    if (sign_flag) goto loc_008713A0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_m118, v_stack_p48, a3, *(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16));
    v_stack_p40 = (unsigned __int8)((unsigned int)(v_stack_m168));
    if (sign_flag) goto loc_00870F65;
    goto loc_00870EBD;
loc_00871381:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152) != 0) goto loc_008713AA;
    v_stack_p40 = (unsigned __int8)((unsigned int)(v_stack_m168));
    goto loc_00870F67;
loc_008713A0:
    v_stack_p40 = (unsigned __int8)((unsigned int)(v_stack_m168));
    goto loc_00870F65;
loc_008713AA:
    v_stack_p28 = v_stack_m128;
    v_stack_p20 = (unsigned int)(v_rdi);
    result = CmpTransSearchAddTrans(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16), *(unsigned __int64 *)(v_stack_m118 + 64), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152), *(unsigned __int64 *)(v_stack_p48 + 32));
    v_stack_p48 = v_stack_m128;
    goto loc_0087135E;
loc_008713D0:
    v_stack_p48 = v_stack_m128;
    goto loc_00871341;
loc_008713E3:
    v_r15 = ((unsigned int)(v_stack_m168)) + (208);
    if (v_r15 != (*(unsigned __int64 *)(v_r15 + 8))) goto loc_00871421;
loc_008713F6:
    if (*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) == 0) goto loc_00870F3D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) + 56) == 0) goto loc_00871413;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) + 56)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152))) goto loc_00871431;
loc_0087140D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) + 68)) == 9) goto loc_0087146F;
loc_00871413:
    v_rsi = *(unsigned __int64 *)(v_r15 + 8);
    if (*(unsigned __int64 *)(v_r15 + 8) == 0) {
        v_rsi = *(unsigned __int64 *)(v_r15 + 8);
    }
    if (v_r15 == v_rsi) goto loc_0087142B;
loc_00871421:
    goto loc_008713F6;
loc_0087142B:
    result = 0;
    goto loc_008713F6;
loc_00871431:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) + 56) + 56) != 0) goto loc_008714C4;
loc_0087143E:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m140 + v_stack_m176 * 8 - 16) + 56)) + (88);
    result = CmpTransUowIsEqual(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152) + 88, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152), *(unsigned __int64 *)(v_stack_p48 + 32));
loc_00871450:
    if ((unsigned __int8)(result) == 0) goto loc_00871413;
    goto loc_0087140D;
loc_00871456:
    if ((*(unsigned __int64 *)(v_stack_m118 + 64)) != result) goto loc_008712FF;
    v_stack_p40 = (unsigned __int8)(v_r15);
    goto loc_00870F67;
loc_0087146F:
    goto loc_00870F3D;
loc_00871478:
    *(unsigned __int64 *)(v_stack_p78 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48 + 32) + 4152) + 88 * 8 - 16) = a1;
    goto loc_008712AD;
loc_00871482:
    v_stack_p20 = v_r15;
    result = KeBugCheckEx(5 + 76, 5, 5 - 4, *(unsigned __int64 *)(v_stack_m118 + 8));
loc_008714A6:
    goto loc_00870FBB;
loc_008714B5:
    goto loc_00870FB1;
loc_008714C4:
    if (*(unsigned __int64 *)(5 - 4 + 56) == 0) goto loc_0087143E;
    result = (5 == (*(unsigned __int64 *)(5 - 4 + 56))) ? 1 : 0;
    goto loc_00871450;
loc_008714DC:
    result = guard_dispatch_icall(5 + 76, 5, 5 - 4, *(unsigned __int64 *)(v_stack_m118 + 8));
    goto loc_00871087;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSecurityMethod(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint16_t v_stack_m156;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m176;
    uint8_t v_stack_m177;
    uint8_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE4;
    uint64_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint16_t v_stack_p62;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (376);
    result = (*(uint64_t *)(v_rip + 0x599A60)) ^ (local_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m160 = Arg4;
    v_stack_mD0 = Arg3;
    v_stack_m168 = (uint32_t)((int32_t)(Arg2));
    v_stack_m118 = Arg1;
    v_stack_mD8 = Arg5;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm1;
    v_stack_m120 = 0;
    v_stack_m68 = v_xmm1;
    if ((*(uint64_t *)(v_rip + 0x767311)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = v_stack_m78;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpInitializeThreadInfo(v_stack_m90, Arg2, Arg3, Arg4);
    v_stack_m130 = v_stack_m138;
    local_r14 = 0;
    v_stack_m138 = v_stack_m138;
    result = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    if ((*(uint64_t *)(v_rip + 0x767292)) != 0) goto loc_0087119F;
loc_00870D8C:
    if ((*(uint32_t *)(v_rip + 0x67EDE4)) != 0) goto loc_008710AA;
loc_00870DAA:
    if (((uint32_t)((int32_t)(Arg2))) != 1) goto loc_0087110A;
    result = 0;
    v_stack_m170 = 0;
    local_rbx = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m156 = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m148 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m90, Arg2, Arg3, Arg4);
    v_stack_m176 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_008714A6;
    result = CmpLockRegistry(v_stack_m90, Arg2, Arg3, Arg4);
    Arg3 = 0;
    v_stack_m177 = (uint8_t)((int32_t)(Arg2));
    if (((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)))) < 2) goto loc_00870E14;
    result = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))))) - ((uint32_t)((int32_t)(Arg2))));
    if (condition_is_not_equal) goto loc_008712BF;
loc_00870E14:
    v_stack_m158 = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)));
    v_stack_m140 = 0;
    v_stack_m178 = 0;
    v_stack_m156 = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42))) != 0) goto loc_0087126F;
    *(uint64_t *)(local_rsp + (int16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8) + 0x42)) * 8 + 0x68) = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m178 = 0;
loc_00870E4B:
loc_00870E51:
    if (0 > ((uint16_t)(v_stack_m156))) goto loc_00870E92;
    local_rsi = (v_stack_m140) - (v_stack_m150);
    local_rsi = (local_rsi) + (-16);
loc_00870E70:
    if (0 >= 2) goto loc_00871196;
loc_00870E7D:
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m150), Arg2, Arg3, Arg4);
    local_rbx = (uint16_t)((0) + 1);
    local_rdi = (v_stack_m150) + (8);
    if (((uint16_t)(local_rbx)) <= ((uint16_t)(v_stack_m156))) goto loc_00870E70;
loc_00870E92:
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00870F65;
    if (*(uint64_t *)(Arg1 + 0x38) != 0) goto loc_008712E9;
    if ((*(uint64_t *)(Arg1 + 0x40)) != (*(uint64_t *)(Arg1 + 0x38))) goto loc_008712E9;
loc_00870EBD:
    Arg1 = 0;
    if (sign_flag) goto loc_00870F2B;
loc_00870ED5:
    if (((uint32_t)((uint16_t)((uint16_t)(v_stack_m156)))) >= 2) goto loc_008711BE;
loc_00870EE6:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x42)) == 0) goto loc_00870EF3;
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x41)) == 1) goto loc_00870F25;
loc_00870EF3:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x28)) == -1) goto loc_00871149;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0xF0) != 0) goto loc_00871139;
loc_00870F0D:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x42)) == 0) goto loc_00870F1D;
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x41)) != 0) goto loc_00870F25;
loc_00870F1D:
loc_00870F20:
    result = (uint16_t)(((uint32_t)((uint32_t)(Arg1 - 1))) + ((uint16_t)((uint16_t)((uint16_t)(v_stack_m156)))));
    if (!sign_flag) goto loc_00870ED5;
loc_00870F25:
    Arg1 = 0;
loc_00870F2B:
    if (v_stack_m170 != 0) goto loc_008713E3;
loc_00870F3D:
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(v_stack_m156)) * 8 + 0x68) + 0x58) + 32;
    result = SeQuerySecurityDescriptorInfo(v_stack_mD0, v_stack_m160, v_stack_mD8, v_stack_m118);
    if (!sign_flag) goto loc_008711B5;
loc_00870F65:
    result = 0;
loc_00870F67:
    if (0 > ((uint16_t)(v_stack_m156))) goto loc_00870FA6;
    local_r15 = (v_stack_m140) - (v_stack_m150);
    local_r15 = (local_r15) + (-16);
loc_00870F84:
    if (0 >= 2) goto loc_0087118D;
loc_00870F91:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m150), v_stack_m160, v_stack_mD8, v_stack_m118);
    local_rbx = (uint16_t)((0) + 1);
    local_rdi = (v_stack_m150) + (8);
    if (((uint16_t)(local_rbx)) <= ((uint16_t)(v_stack_m156))) goto loc_00870F84;
loc_00870FA6:
loc_00870FB1:
loc_00870FBB:
    if (v_stack_m140 != 0) {
        Arg1 = v_stack_m140;
        result = CmSiFreeMemory(Arg1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if ((uint8_t)(v_stack_m177) != 0) {
        result = CmpUnlockRegistry(Arg1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if ((uint8_t)(v_stack_m176) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, v_stack_m160, v_stack_mD8, v_stack_m118);
    }
    if (!sign_flag) goto loc_0087111F;
loc_00870FE3:
    local_rbx = 0;
loc_00870FE5:
    if ((uint8_t)(v_stack_m178) == 0) goto loc_00871060;
    if (((uint32_t)((uint32_t)(v_stack_m168))) != 1) goto loc_008711E6;
    if ((*(uint32_t *)(v_rip + 0x67EB8D)) == 0) goto loc_00871060;
    result = CmpIsRegistryLockAcquired(Arg1, v_stack_m160, v_stack_mD8, v_stack_m118);
    if ((uint32_t)(result) != 0) goto loc_00871060;
    if (v_stack_m138 == v_stack_m138) goto loc_00871060;
    v_stack_m100 = v_stack_mC8;
    v_stack_m188 = v_stack_m138;
    v_stack_m190 = v_stack_m118;
    v_stack_m198 = 37;
loc_00871032:
    v_stack_m104 = 0;
    Arg4 = 0;
    v_stack_mE4 = 0;
    Arg3 = 0;
    v_stack_mDC = 0;
    v_stack_m110 = v_stack_m118;
    v_stack_mF4 = v_xmm0;
    v_stack_m108 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = CmpCallCallBacksEx((uint32_t)(v_stack_m168) + 36, v_stack_m110, Arg3, Arg4);
loc_00871060:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m110, Arg3, Arg4);
    result = CmCleanupThreadInfo(v_stack_m90, v_stack_m110, Arg3, Arg4);
    if (*(uint64_t *)(v_rip + 0x766F8A) != 0) goto loc_00871152;
loc_00871087:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m110, Arg3, Arg4);
    local_rsp = (local_rsp) + (376);
    return result;
loc_008710AA:
    result = CmpIsRegistryLockAcquired(Arg1, v_stack_m110, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00870DAA;
    if (((uint32_t)((uint32_t)(v_stack_m168))) != 1) goto loc_008711C8;
    v_stack_mB8 = v_stack_p58;
    v_stack_mB0 = (uint32_t)(v_stack_mF8);
loc_008710D5:
    v_stack_mC0 = v_stack_m140;
    v_stack_p30 = v_stack_m138;
    v_stack_p28 = v_stack_m118;
    Arg3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m168) + 35 + 1);
    v_stack_mC8 = v_stack_m118;
    result = CmpCallCallBacksEx((uint32_t)(v_stack_m168) + 35, v_stack_mC8, Arg3, 1);
    if (sign_flag) goto loc_00871128;
    goto loc_00870DAA;
loc_0087110A:
    if ((uint32_t)((uint32_t)(v_stack_m168)) == 0) goto loc_0087123E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m168)))) - (2));
    if (condition_is_not_equal) goto loc_00871482;
loc_0087111F:
    local_rbx = 0;
    goto loc_00870FE5;
loc_00871128:
    local_rbx = 0;
    local_rsi = 0;
    if (((uint32_t)(result)) != 0xC0000503ULL) { local_rsi = (uint32_t)(result); }
    goto loc_00871060;
loc_00871139:
    result = CmEqualTrans(local_rsi, v_stack_mC8, Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_00870F0D;
loc_00871149:
    goto loc_00870F20;
loc_00871152:
    v_stack_p28 = 0;
    Arg1 = ((uint32_t)((uint32_t)(v_stack_m168)) != 0) ? 1 : 0;
    Arg4 = 0;
    Arg1 = (uint8_t)((Arg1) + (28));
    v_stack_p20 = v_stack_m120;
    if (((uint16_t)(v_stack_m118)) != (v_rip - 59361)) goto loc_008714DC;
    result = EtwpTraceRegistry(Arg1, v_stack_m78, (uint32_t)((uint32_t)(local_rsi)), Arg4);
    goto loc_00871087;
loc_0087118D:
    goto loc_00870F91;
loc_00871196:
    goto loc_00870E7D;
loc_0087119F:
    if (v_stack_m118 == 0) goto loc_00870D8C;
    v_stack_m120 = *(uint64_t *)(v_stack_m118 + 0x8);
    goto loc_00870D8C;
loc_008711B5:
    result = 0;
    goto loc_00870F67;
loc_008711BE:
    goto loc_00870EE6;
loc_008711C8:
    if ((uint32_t)((uint32_t)(v_stack_m168)) != 0) goto loc_0087110A;
    v_stack_mB8 = v_stack_p58;
    goto loc_008710D5;
loc_008711E6:
    if ((uint32_t)((uint32_t)(v_stack_m168)) != 0) goto loc_00871060;
    if ((*(uint32_t *)(v_rip + 0x67E992)) == ((uint32_t)((uint32_t)(v_stack_m168)))) goto loc_00871060;
    result = CmpIsRegistryLockAcquired((uint32_t)(v_stack_m168) + 38, v_stack_m78, (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00871060;
    if (v_stack_m138 == v_stack_m138) goto loc_00871060;
    v_stack_m100 = v_stack_mC8;
    v_stack_p30 = v_stack_m138;
    v_stack_p28 = v_stack_m118;
    v_stack_p20 = 39;
    goto loc_00871032;
loc_0087123E:
    v_stack_p28 = v_stack_m176;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg7));
    result = CmpSetKeySecurity(v_stack_m118, v_stack_m140, v_stack_p58, *(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10));
    if (sign_flag) goto loc_00870FE3;
    goto loc_0087111F;
loc_0087126F:
    if (*(uint64_t *)(v_stack_m176 + 0xC0) == 0) goto loc_00870E51;
    v_stack_p40 = (uint8_t)((uint32_t)((uint32_t)(result)));
loc_00871290:
    if (1 >= 2) goto loc_00871478;
    *(uint64_t *)(local_rsp + (int16_t)(1) * 8 + 0x68) = *(uint64_t *)(*(uint64_t *)(v_stack_m176 + 0xC0) + 0x10);
loc_008712AD:
    local_r14 = (uint16_t)((1) - 1);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m176 + 0xC0) + 0x18) != 0) goto loc_00871290;
    goto loc_00870E4B;
loc_008712BF:
    Arg2 = ((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m176 + 0xC0) + 0x18)))) << (3);
    result = CmpAllocatePool(256, Arg2, (uint32_t)(0x35364D43ULL), *(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10));
    if (result == 0) goto loc_008714B5;
    Arg3 = 0;
    goto loc_00870E14;
loc_008712E9:
    local_rdi = 0;
    v_stack_p48 = 0;
    v_stack_m128 = 0;
    if (*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) == 0) goto loc_00871456;
loc_008712FF:
    Arg2 = (*(uint64_t *)(v_stack_m118 + 0x8)) ^ (1);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m118 + 0x8))) & (1)) == 0) { Arg2 = *(uint64_t *)(v_stack_m118 + 0x8); }
    if ((((uint8_t)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10))) & (1)) == 0) goto loc_00871381;
    local_rdi = (*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10)) & (-2);
    result = CmpTransReferenceTransaction(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10), Arg2, Arg3, *(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10));
    if (sign_flag) goto loc_00871359;
    v_stack_p48 = *(uint64_t *)(local_rdi + 0x10);
    if (*(uint64_t *)(local_rdi + 0x10) == 0) goto loc_008713D0;
    result = 0;
loc_00871341:
    if (*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) != 0) {
        Arg1 = local_rdi;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10));
    }
loc_00871359:
loc_0087135E:
    if (sign_flag) goto loc_008713A0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_m118, v_stack_p48, Arg3, *(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10));
    v_stack_p40 = (uint8_t)((uint32_t)(v_stack_m168));
    if (sign_flag) goto loc_00870F65;
    goto loc_00870EBD;
loc_00871381:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038) != 0) goto loc_008713AA;
    v_stack_p40 = (uint8_t)((uint32_t)(v_stack_m168));
    goto loc_00870F67;
loc_008713A0:
    v_stack_p40 = (uint8_t)((uint32_t)(v_stack_m168));
    goto loc_00870F65;
loc_008713AA:
    v_stack_p28 = v_stack_m128;
    v_stack_p20 = (uint32_t)(local_rdi);
    result = CmpTransSearchAddTrans(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10), *(uint64_t *)(v_stack_m118 + 0x40), *(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038), *(uint64_t *)(v_stack_p48 + 0x20));
    v_stack_p48 = v_stack_m128;
    goto loc_0087135E;
loc_008713D0:
    v_stack_p48 = v_stack_m128;
    goto loc_00871341;
loc_008713E3:
    local_r15 = ((uint32_t)(v_stack_m168)) + (208);
    if (local_r15 != (*(uint64_t *)(local_r15 + 0x8))) goto loc_00871421;
loc_008713F6:
    if (*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) == 0) goto loc_00870F3D;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) + 0x38) == 0) goto loc_00871413;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) + 0x38)) != (*(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038))) goto loc_00871431;
loc_0087140D:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) + 0x44)) == 9) goto loc_0087146F;
loc_00871413:
    local_rsi = *(uint64_t *)(local_r15 + 0x8);
    if (*(uint64_t *)(local_r15 + 0x8) == 0) {
        local_rsi = *(uint64_t *)(local_r15 + 0x8);
    }
    if (local_r15 == local_rsi) goto loc_0087142B;
loc_00871421:
    goto loc_008713F6;
loc_0087142B:
    result = 0;
    goto loc_008713F6;
loc_00871431:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) + 0x38) + 0x38) != 0) goto loc_008714C4;
loc_0087143E:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m140 + v_stack_m176 * 8 - 0x10) + 0x38)) + (88);
    result = CmpTransUowIsEqual(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038) + 88, *(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038), *(uint64_t *)(v_stack_p48 + 0x20));
loc_00871450:
    if ((uint8_t)(result) == 0) goto loc_00871413;
    goto loc_0087140D;
loc_00871456:
    if ((*(uint64_t *)(v_stack_m118 + 0x40)) != result) goto loc_008712FF;
    v_stack_p40 = (uint8_t)(local_r15);
    goto loc_00870F67;
loc_0087146F:
    goto loc_00870F3D;
loc_00871478:
    *(uint64_t *)(v_stack_p78 + *(uint64_t *)(*(uint64_t *)(v_stack_p48 + 0x20) + 0x1038) + 0x58 * 8 - 0x10) = Arg1;
    goto loc_008712AD;
loc_00871482:
    v_stack_p20 = local_r15;
    result = KeBugCheckEx(5 + 76, 5, 5 - 4, *(uint64_t *)(v_stack_m118 + 0x8));
loc_008714A6:
    goto loc_00870FBB;
loc_008714B5:
    goto loc_00870FB1;
loc_008714C4:
    if (*(uint64_t *)(5 - 0x4 + 0x38) == 0) goto loc_0087143E;
    result = (5 == (*(uint64_t *)(5 - 0x4 + 0x38))) ? 1 : 0;
    goto loc_00871450;
loc_008714DC:
    result = guard_dispatch_icall(5 + 76, 5, 5 - 4, *(uint64_t *)(v_stack_m118 + 0x8));
    goto loc_00871087;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00870CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
