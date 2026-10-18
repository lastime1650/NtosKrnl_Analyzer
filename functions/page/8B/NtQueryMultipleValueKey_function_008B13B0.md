# NtQueryMultipleValueKey

- RVA: `0x008B13B0`–`0x008B1A39` (길이 `1,673` bytes)
- VA: `0x00000001408B13B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082510`
- 디코드: `344`개 명령, `1,673/1,673` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008B1451` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B149E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B14CB` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x008B14EE` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x008B152B` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x008B1583` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008B15A7` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008B15BD` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x008B160D` → [CmpCaptureKeyValueArray](CmpCaptureKeyValueArray_function_008B1074.md) (function, `0x008B1074`)
- `0x008B163F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B16BC` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B16E1` → [CmKeyBodyRemapToVirtualForEnum](CmKeyBodyRemapToVirtualForEnum_function_008B46C0.md) (function, `0x008B46C0`)
- `0x008B170D` → [CmpBounceContextStart](CmpBounceContextStart_function_008B27F0.md) (function, `0x008B27F0`)
- `0x008B1724` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008B175C` → [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) (function, `0x00846EC0`)
- `0x008B176B` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x008B17AA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B17F3` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B1892` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B18B1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B18C0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B18CD` → [CmpBounceContextCleanup](CmpBounceContextCleanup_function_008B2520.md) (function, `0x008B2520`)
- `0x008B18E9` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x008B18F8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B190A` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B191C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B1929` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x008B193B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B19D2` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x008B1A02` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B1A2F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008B13C2` → RVA `0x00E0A740` (`.data`; read)
- `0x008B1472` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x008B1632` → RVA `0x00EEFB88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x008B1451` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B149E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B14CB` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x008B14EE` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x008B152B` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x008B15BD` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x008B163F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B1724` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B176B` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x008B17AA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B17F3` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B18B1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B18C0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B18E9` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x008B18F8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B190A` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B191C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B1929` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x008B193B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B19D2` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x008B1A02` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B1A2F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B13B0  40 56                           push rsi
008B13B2  57                              push rdi
008B13B3  41 54                           push r12
008B13B5  41 55                           push r13
008B13B7  41 56                           push r14
008B13B9  41 57                           push r15
008B13BB  48 81 EC 28 02 00 00            sub rsp, 0x228
008B13C2  48 8B 05 77 93 55 00            mov rax, qword ptr [rip + 0x559377]
008B13C9  48 33 C4                        xor rax, rsp
008B13CC  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
008B13D4  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
008B13D9  45 8B F0                        mov r14d, r8d
008B13DC  4C 8B EA                        mov r13, rdx
008B13DF  48 8B F9                        mov rdi, rcx
008B13E2  48 8B B4 24 88 02 00 00         mov rsi, qword ptr [rsp + 0x288]
008B13EA  4C 8B A4 24 80 02 00 00         mov r12, qword ptr [rsp + 0x280]
008B13F2  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
008B13FA  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
008B13FF  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
008B1407  0F 57 C0                        xorps xmm0, xmm0
008B140A  33 C0                           xor eax, eax
008B140C  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
008B1414  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
008B141C  21 44 24 44                     and dword ptr [rsp + 0x44], eax
008B1420  21 44 24 68                     and dword ptr [rsp + 0x68], eax
008B1424  21 84 24 B8 00 00 00            and dword ptr [rsp + 0xb8], eax
008B142B  0F 11 84 24 80 01 00 00         movups xmmword ptr [rsp + 0x180], xmm0
008B1433  0F 11 84 24 90 01 00 00         movups xmmword ptr [rsp + 0x190], xmm0
008B143B  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
008B1443  33 D2                           xor edx, edx
008B1445  44 8D 40 58                     lea r8d, [rax + 0x58]
008B1449  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008B1451  E8 EA 57 E1 FF                  call 0x1406c6c40
008B1456  0F 57 C0                        xorps xmm0, xmm0
008B1459  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
008B1461  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
008B1469  48 83 A4 24 A0 00 00 00 00      and qword ptr [rsp + 0xa0], 0
008B1472  48 83 3D 8E 6B 72 00 00         cmp qword ptr [rip + 0x726b8e], 0
008B147A  0F 85 45 05 00 00               jne 0x1408b19c5
008B1480  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008B1485  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
008B148A  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
008B1490  33 D2                           xor edx, edx
008B1492  44 8D 42 48                     lea r8d, [rdx + 0x48]
008B1496  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
008B149E  E8 9D 57 E1 FF                  call 0x1406c6c40
008B14A3  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B14AB  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
008B14B3  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B14BB  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008B14C3  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
008B14CB  E8 A0 A9 B4 FF                  call 0x1403fbe70
008B14D0  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
008B14D6  48 83 64 24 60 00               and qword ptr [rsp + 0x60], 0
008B14DC  48 83 A4 24 A8 00 00 00 00      and qword ptr [rsp + 0xa8], 0
008B14E5  48 83 A4 24 B0 00 00 00 00      and qword ptr [rsp + 0xb0], 0
008B14EE  E8 0D 7F 31 00                  call 0x140bc9400
008B14F3  88 44 24 48                     mov byte ptr [rsp + 0x48], al
008B14F7  84 C0                           test al, al
008B14F9  0F 84 DD 04 00 00               je 0x1408b19dc
008B14FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B1508  44 0F BE B8 32 02 00 00         movsx r15d, byte ptr [rax + 0x232]
008B1510  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
008B1516  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008B151B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B1520  45 8A CF                        mov r9b, r15b
008B1523  BA 01 00 00 00                  mov edx, 1
008B1528  48 8B CF                        mov rcx, rdi
008B152B  E8 20 7E 31 00                  call 0x140bc9350
008B1530  8B F8                           mov edi, eax
008B1532  85 C0                           test eax, eax
008B1534  0F 88 81 04 00 00               js 0x1408b19bb
008B153A  48 83 3D C6 6A 72 00 00         cmp qword ptr [rip + 0x726ac6], 0
008B1542  0F 85 9B 04 00 00               jne 0x1408b19e3
008B1548  41 80 FF 01                     cmp r15b, 1
008B154C  75 60                           jne 0x1408b15ae
008B154E  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
008B1558  48 8B C7                        mov rax, rdi
008B155B  4C 3B E7                        cmp r12, rdi
008B155E  49 0F 42 C4                     cmovb rax, r12
008B1562  90                              nop
008B1563  8B 00                           mov eax, dword ptr [rax]
008B1565  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008B1569  41 81 FE 00 00 01 00            cmp r14d, 0x10000
008B1570  77 46                           ja 0x1408b15b8
008B1572  4B 8D 14 76                     lea rdx, [r14 + r14*2]
008B1576  48 C1 E2 03                     shl rdx, 3
008B157A  41 B8 04 00 00 00               mov r8d, 4
008B1580  49 8B CD                        mov rcx, r13
008B1583  E8 38 7C 03 00                  call 0x1408e91c0
008B1588  48 85 F6                        test rsi, rsi
008B158B  74 0B                           je 0x1408b1598
008B158D  48 3B F7                        cmp rsi, rdi
008B1590  48 0F 42 FE                     cmovb rdi, rsi
008B1594  8B 07                           mov eax, dword ptr [rdi]
008B1596  89 07                           mov dword ptr [rdi], eax
008B1598  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
008B159C  41 B8 04 00 00 00               mov r8d, 4
008B15A2  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008B15A7  E8 14 7C 03 00                  call 0x1408e91c0
008B15AC  EB 14                           jmp 0x1408b15c2
008B15AE  41 8B 04 24                     mov eax, dword ptr [r12]
008B15B2  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008B15B6  EB 0A                           jmp 0x1408b15c2
008B15B8  B9 9A 00 00 C0                  mov ecx, 0xc000009a
008B15BD  E8 8E 54 A4 FF                  call 0x1402f6a50
008B15C2  EB 21                           jmp 0x1408b15e5
008B15C4  8B F8                           mov edi, eax
008B15C6  BE 00 00 00 80                  mov esi, 0x80000000
008B15CB  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008B15D3  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
008B15D8  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
008B15E0  E9 E8 01 00 00                  jmp 0x1408b17cd
008B15E5  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B15ED  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B15F2  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
008B15FA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B15FF  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
008B1604  45 8A C7                        mov r8b, r15b
008B1607  41 8B D6                        mov edx, r14d
008B160A  49 8B CD                        mov rcx, r13
008B160D  E8 62 FA FF FF                  call 0x1408b1074
008B1612  8B F8                           mov edi, eax
008B1614  85 C0                           test eax, eax
008B1616  0F 88 9F 03 00 00               js 0x1408b19bb
008B161C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B1625  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B162C  90                              nop
008B162D  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008B1632  83 3D 4F E5 63 00 00            cmp dword ptr [rip + 0x63e54f], 0
008B1639  0F 84 8F 00 00 00               je 0x1408b16ce
008B163F  E8 38 54 BA FF                  call 0x140456a7c
008B1644  85 C0                           test eax, eax
008B1646  0F 85 82 00 00 00               jne 0x1408b16ce
008B164C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B1651  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
008B1659  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008B165E  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
008B1666  44 89 B4 24 20 01 00 00         mov dword ptr [rsp + 0x120], r14d
008B166E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B1673  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008B167B  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008B1680  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
008B1688  48 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], rsi
008B1690  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B1698  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B169D  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B16A2  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
008B16AA  41 B1 01                        mov r9b, 1
008B16AD  45 33 C0                        xor r8d, r8d
008B16B0  48 8D 94 24 10 01 00 00         lea rdx, [rsp + 0x110]
008B16B8  41 8D 48 09                     lea ecx, [r8 + 9]
008B16BC  E8 7F 48 FB FF                  call 0x140865f40
008B16C1  85 C0                           test eax, eax
008B16C3  0F 88 E8 02 00 00               js 0x1408b19b1
008B16C9  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008B16CE  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
008B16D3  41 B8 01 00 00 00               mov r8d, 1
008B16D9  41 8A D7                        mov dl, r15b
008B16DC  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
008B16E1  E8 DA 2F 00 00                  call 0x1408b46c0
008B16E6  8B F8                           mov edi, eax
008B16E8  85 C0                           test eax, eax
008B16EA  0F 88 CB 02 00 00               js 0x1408b19bb
008B16F0  45 8B CF                        mov r9d, r15d
008B16F3  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
008B16F8  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
008B1700  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008B1705  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008B170D  E8 DE 10 00 00                  call 0x1408b27f0
008B1712  8B F8                           mov edi, eax
008B1714  85 C0                           test eax, eax
008B1716  0F 88 9F 02 00 00               js 0x1408b19bb
008B171C  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
008B1724  E8 B7 81 31 00                  call 0x140bc98e0
008B1729  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008B172E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B1733  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008B1738  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B173D  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
008B1745  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B174A  45 8B CE                        mov r9d, r14d
008B174D  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
008B1752  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008B1757  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B175C  E8 5F 57 F9 FF                  call 0x140846ec0
008B1761  8B F8                           mov edi, eax
008B1763  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
008B176B  E8 B0 81 31 00                  call 0x140bc9920
008B1770  90                              nop
008B1771  48 85 F6                        test rsi, rsi
008B1774  74 06                           je 0x1408b177c
008B1776  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008B177A  89 06                           mov dword ptr [rsi], eax
008B177C  BE 00 00 00 80                  mov esi, 0x80000000
008B1781  8D 04 37                        lea eax, [rdi + rsi]
008B1784  85 C6                           test esi, eax
008B1786  75 08                           jne 0x1408b1790
008B1788  81 FF 05 00 00 80               cmp edi, 0x80000005
008B178E  75 1F                           jne 0x1408b17af
008B1790  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
008B1795  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
008B179D  48 8B 94 24 B8 01 00 00         mov rdx, qword ptr [rsp + 0x1b8]
008B17A5  48 3B CA                        cmp rcx, rdx
008B17A8  74 05                           je 0x1408b17af
008B17AA  E8 91 50 E1 FF                  call 0x1406c6840
008B17AF  EB 1C                           jmp 0x1408b17cd
008B17B1  8B F8                           mov edi, eax
008B17B3  BE 00 00 00 80                  mov esi, 0x80000000
008B17B8  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008B17C0  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
008B17C5  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
008B17CD  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008B17D2  48 85 C9                        test rcx, rcx
008B17D5  0F 85 27 02 00 00               jne 0x1408b1a02
008B17DB  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008B17E0  0F 84 B8 00 00 00               je 0x1408b189e
008B17E6  83 3D 9B E3 63 00 00            cmp dword ptr [rip + 0x63e39b], 0
008B17ED  0F 84 AB 00 00 00               je 0x1408b189e
008B17F3  E8 84 52 BA FF                  call 0x140456a7c
008B17F8  85 C0                           test eax, eax
008B17FA  0F 85 9E 00 00 00               jne 0x1408b189e
008B1800  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B1808  48 39 84 24 80 00 00 00         cmp qword ptr [rsp + 0x80], rax
008B1810  0F 84 88 00 00 00               je 0x1408b189e
008B1816  0F 57 C0                        xorps xmm0, xmm0
008B1819  33 C0                           xor eax, eax
008B181B  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008B1823  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008B182B  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
008B1833  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008B183B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B1840  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
008B1848  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
008B184F  89 BC 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edi
008B1856  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
008B185E  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008B1866  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B186E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B1873  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B1878  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
008B1880  45 33 C9                        xor r9d, r9d
008B1883  45 33 C0                        xor r8d, r8d
008B1886  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
008B188E  41 8D 49 18                     lea ecx, [r9 + 0x18]
008B1892  E8 A9 46 FB FF                  call 0x140865f40
008B1897  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
008B189E  48 83 7C 24 60 00               cmp qword ptr [rsp + 0x60], 0
008B18A4  0F 85 A9 00 00 00               jne 0x1408b1953
008B18AA  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
008B18AF  74 05                           je 0x1408b18b6
008B18B1  E8 FA BF 9A FF                  call 0x14025d8b0
008B18B6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B18BB  48 85 C9                        test rcx, rcx
008B18BE  74 05                           je 0x1408b18c5
008B18C0  E8 8B 7A A4 FF                  call 0x1402f9350
008B18C5  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008B18CD  E8 4E 0C 00 00                  call 0x1408b2520
008B18D2  48 8B 05 2F 67 72 00            mov rax, qword ptr [rip + 0x72672f]
008B18D9  48 85 C0                        test rax, rax
008B18DC  0F 85 2A 01 00 00               jne 0x1408b1a0c
008B18E2  80 7C 24 48 00                  cmp byte ptr [rsp + 0x48], 0
008B18E7  74 05                           je 0x1408b18ee
008B18E9  E8 92 7F 31 00                  call 0x140bc9880
008B18EE  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008B18F3  48 85 C9                        test rcx, rcx
008B18F6  74 05                           je 0x1408b18fd
008B18F8  E8 83 44 BC FF                  call 0x140475d80
008B18FD  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008B1905  48 85 C9                        test rcx, rcx
008B1908  74 05                           je 0x1408b190f
008B190A  E8 71 44 BC FF                  call 0x140475d80
008B190F  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008B1917  48 85 C9                        test rcx, rcx
008B191A  74 05                           je 0x1408b1921
008B191C  E8 5F 44 BC FF                  call 0x140475d80
008B1921  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
008B1929  E8 22 E4 B6 FF                  call 0x14041fd50
008B192E  8B C7                           mov eax, edi
008B1930  48 8B 8C 24 10 02 00 00         mov rcx, qword ptr [rsp + 0x210]
008B1938  48 33 CC                        xor rcx, rsp
008B193B  E8 00 AD DF FF                  call 0x1406ac640
008B1940  48 81 C4 28 02 00 00            add rsp, 0x228
008B1947  41 5F                           pop r15
008B1949  41 5E                           pop r14
008B194B  41 5D                           pop r13
008B194D  41 5C                           pop r12
008B194F  5F                              pop rdi
008B1950  5E                              pop rsi
008B1951  C3                              ret
008B1952  CC                              int3
008B1953  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
008B1957  41 89 04 24                     mov dword ptr [r12], eax
008B195B  8D 04 37                        lea eax, [rdi + rsi]
008B195E  85 C6                           test esi, eax
008B1960  74 36                           je 0x1408b1998
008B1962  45 33 C0                        xor r8d, r8d
008B1965  44 89 44 24 6C                  mov dword ptr [rsp + 0x6c], r8d
008B196A  45 3B C6                        cmp r8d, r14d
008B196D  73 31                           jae 0x1408b19a0
008B196F  4B 8D 14 40                     lea rdx, [r8 + r8*2]
008B1973  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008B1978  8B 44 D1 08                     mov eax, dword ptr [rcx + rdx*8 + 8]
008B197C  41 89 44 D5 08                  mov dword ptr [r13 + rdx*8 + 8], eax
008B1981  8B 44 D1 0C                     mov eax, dword ptr [rcx + rdx*8 + 0xc]
008B1985  41 89 44 D5 0C                  mov dword ptr [r13 + rdx*8 + 0xc], eax
008B198A  8B 44 D1 10                     mov eax, dword ptr [rcx + rdx*8 + 0x10]
008B198E  41 89 44 D5 10                  mov dword ptr [r13 + rdx*8 + 0x10], eax
008B1993  41 FF C0                        inc r8d
008B1996  EB CD                           jmp 0x1408b1965
008B1998  81 FF 05 00 00 80               cmp edi, 0x80000005
008B199E  74 C2                           je 0x1408b1962
008B19A0  E9 05 FF FF FF                  jmp 0x1408b18aa
008B19A5  8B F8                           mov edi, eax
008B19A7  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
008B19AC  E9 F9 FE FF FF                  jmp 0x1408b18aa
008B19B1  33 FF                           xor edi, edi
008B19B3  3D 03 05 00 C0                  cmp eax, 0xc0000503
008B19B8  0F 45 F8                        cmovne edi, eax
008B19BB  BE 00 00 00 80                  mov esi, 0x80000000
008B19C0  E9 08 FE FF FF                  jmp 0x1408b17cd
008B19C5  BA 00 00 02 00                  mov edx, 0x20000
008B19CA  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
008B19D2  E8 79 E2 AE FF                  call 0x14039fc50
008B19D7  E9 A4 FA FF FF                  jmp 0x1408b1480
008B19DC  BF 89 01 00 C0                  mov edi, 0xc0000189
008B19E1  EB D8                           jmp 0x1408b19bb
008B19E3  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B19E8  48 85 C9                        test rcx, rcx
008B19EB  0F 84 57 FB FF FF               je 0x1408b1548
008B19F1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008B19F5  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
008B19FD  E9 46 FB FF FF                  jmp 0x1408b1548
008B1A02  E8 49 79 A4 FF                  call 0x1402f9350
008B1A07  E9 CF FD FF FF                  jmp 0x1408b17db
008B1A0C  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
008B1A12  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
008B1A1A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008B1A1F  45 8B CE                        mov r9d, r14d
008B1A22  44 8B C7                        mov r8d, edi
008B1A25  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
008B1A2D  B1 13                           mov cl, 0x13
008B1A2F  E8 9C 90 E0 FF                  call 0x1406baad0
008B1A34  E9 A9 FE FF FF                  jmp 0x1408b18e2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryMultipleValueKey(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int8 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned __int8 v_stack_m217;
    unsigned __int8 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p44;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_pA0;

    v_rsp = (v_rsp) - (552);
    result = (*(unsigned __int64 *)(v_rip + 5608311)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1E8 = a4;
    v_stack_m1C8 = a2;
    v_stack_m208 = (unsigned int)((unsigned int)(a3));
    v_stack_m1C0 = a5;
    result = 0;
    v_stack_m160 = v_xmm0;
    v_stack_m150 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_mA8, a2, result + 88, a4);
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    if ((*(unsigned __int64 *)(v_rip + 7498638)) != 0) goto loc_008B19C5;
loc_008B1480:
    v_stack_m218 = 0;
    v_stack_m217 = 0;
    a2 = 0;
    result = memset(v_stack_m148, a2, a2 + 72, a4);
    v_stack_m1D0 = v_stack_m1D8;
    v_stack_m1D8 = v_stack_m1D8;
    result = CmpInitializeThreadInfo(v_stack_m160, a2, a2 + 72, a4);
    result = CmpAcquireShutdownRundown(v_stack_m160, a2, a2 + 72, a4);
    v_stack_m210 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_008B19DC;
    v_stack_m238 = v_stack_m200;
    result = CmObReferenceObjectByHandle(a1, 1, a2 + 72, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if (sign_flag) goto loc_008B19BB;
    if ((*(unsigned __int64 *)(v_rip + 7498438)) != 0) goto loc_008B19E3;
loc_008B1548:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) != 1) goto loc_008B15AE;
    result = (unsigned int)((unsigned int)(result));
    if (a5 < ((unsigned int)((unsigned int)(result)))) { result = a5; }
    v_stack_m214 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((unsigned int)((unsigned int)(a3))) > 0x10000ULL) goto loc_008B15B8;
    a2 = ((unsigned int)(a3) + (unsigned int)(a3) * 2) << (3);
    result = ProbeForWrite(a2, a2, 4, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    v_rdi = (unsigned int)((unsigned int)(result));
    if (a6 != 0) {
        v_rdi = (unsigned int)((unsigned int)(result));
        if (a6 < ((unsigned int)((unsigned int)(result)))) { v_rdi = a6; }
        result = *(unsigned int *)(v_rdi);
        *(unsigned int *)(v_rdi) = (unsigned int)(result);
    }
    result = ProbeForWrite(v_stack_m1E8, (unsigned int)(v_stack_m214), 4, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    goto loc_008B15C2;
loc_008B15AE:
    v_stack_m214 = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    goto loc_008B15C2;
loc_008B15B8:
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), (unsigned int)(v_stack_m214), 4, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
loc_008B15C2:
    goto loc_008B15E5;
loc_008B15E5:
    v_stack_m230 = v_stack_m1A8;
    v_stack_m238 = v_stack_m1B0;
    result = CmpCaptureKeyValueArray(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), v_stack_m1F8);
    if (sign_flag) goto loc_008B19BB;
    v_stack_m217 = 1;
    if ((*(unsigned int *)(v_rip + 6546767)) == 0) goto loc_008B16CE;
    result = CmpIsRegistryLockAcquired(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), v_stack_m1F8);
    if ((unsigned int)(result) != 0) goto loc_008B16CE;
    v_stack_m148 = v_stack_m200;
    v_stack_m140 = v_stack_m1F8;
    v_stack_m138 = (unsigned int)((unsigned int)(a3));
    v_stack_m130 = v_stack_m1E8;
    v_stack_m128 = v_stack_m214;
    v_stack_m120 = a6;
    v_stack_m228 = v_stack_m1D8;
    v_stack_m230 = v_stack_m200;
    v_stack_m238 = 24;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 9, v_stack_m148, a3, 1);
    if (sign_flag) goto loc_008B19B1;
    v_stack_m218 = 1;
loc_008B16CE:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m200, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), 1, v_stack_m1E0);
    if (sign_flag) goto loc_008B19BB;
    v_stack_m238 = 4;
    result = CmpBounceContextStart(v_stack_mA8, v_stack_m1E8, (unsigned int)(v_stack_m214), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))));
    if (sign_flag) goto loc_008B19BB;
    result = CmpAttachToRegistryProcess(v_stack_mD8, v_stack_m1E8, (unsigned int)(v_stack_m214), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))));
    v_stack_m228 = v_stack_m1F0;
    v_stack_m230 = v_stack_m214;
    v_stack_m238 = v_stack_mA0;
    result = CmQueryMultipleValueKey(v_stack_m200, v_stack_m1E0, v_stack_m1F8, (unsigned int)((unsigned int)((unsigned int)(a3))));
    result = CmpDetachFromRegistryProcess(v_stack_mD8, v_stack_m1E0, v_stack_m1F8, (unsigned int)((unsigned int)((unsigned int)(a3))));
    if (a6 != 0) {
        result = v_stack_m1F0;
        *(unsigned int *)(a6) = (unsigned int)(result);
    }
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_008B1790;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0x80000005ULL) goto loc_008B17AF;
loc_008B1790:
    result = (unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1;
    if (v_stack_mA8 != v_stack_mA0) {
        result = memcpy(v_stack_mA8, v_stack_mA0, (unsigned int)(v_stack_m214), (unsigned int)((unsigned int)((unsigned int)(a3))));
    }
    goto loc_008B17CD;
loc_008B17CD:
    if (v_stack_m1E0 != 0) goto loc_008B1A02;
loc_008B17DB:
    if (v_stack_m218 == 0) goto loc_008B189E;
    if ((*(unsigned int *)(v_rip + 6546331)) == 0) goto loc_008B189E;
    result = CmpIsRegistryLockAcquired(v_stack_m1E0, v_stack_mA0, (unsigned int)(v_stack_m214), (unsigned int)((unsigned int)((unsigned int)(a3))));
    if ((unsigned int)(result) != 0) goto loc_008B189E;
    result = v_stack_m1D8;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (v_stack_m1D8 != v_stack_m1D8) {
        result = 0;
        v_stack_m198 = v_xmm0;
        v_stack_m188 = v_xmm0;
        v_stack_m178 = v_xmm0;
        v_stack_m168 = 0;
        a1 = v_stack_m200;
        v_stack_m198 = a1;
        v_stack_m190 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m180 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = v_stack_m148;
        v_stack_m188 = result;
        result = v_stack_m1D8;
        v_stack_m228 = result;
        v_stack_m230 = a1;
        v_stack_m238 = 24;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m198;
        a1 = a4 + 24;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rdi = v_stack_m180;
    }
    if (v_stack_m1F8 != 0) goto loc_008B1953;
loc_008B18AA:
    if (v_stack_m217 != 0) {
        result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    }
    if (v_stack_m200 != 0) {
        result = ObfDereferenceObject(v_stack_m200, a2, a3, a4);
    }
    result = CmpBounceContextCleanup(v_stack_mA8, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rip + 7497519) != 0) goto loc_008B1A0C;
loc_008B18E2:
    result = *(unsigned __int64 *)(v_rip + 7497519);
    if (v_stack_m210 != 0) {
        result = CmpReleaseShutdownRundown(v_stack_mA8, a2, a3, a4);
    }
    if (v_stack_m1F8 != 0) {
        result = CmSiFreeMemory(v_stack_m1F8, a2, a3, a4);
    }
    if (v_stack_m1B0 != 0) {
        result = CmSiFreeMemory(v_stack_m1B0, a2, a3, a4);
    }
    if (v_stack_m1A8 != 0) {
        result = CmSiFreeMemory(v_stack_m1A8, a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m160, a2, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (552);
    return result;
loc_008B1953:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_p44));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(v_rdi + (unsigned int)(0x80000000ULL) * 1))) == 0) goto loc_008B1998;
loc_008B1962:
    a3 = 0;
loc_008B1965:
    v_stack_p6C = 0;
    if (0 >= ((unsigned int)((unsigned int)(a3)))) goto loc_008B19A0;
    *(unsigned int *)(a2 + a3 + a3 * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + a3 + a3 * 2 * 8 + 8)));
    *(unsigned int *)(a2 + a3 + a3 * 2 * 8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + a3 + a3 * 2 * 8 + 12)));
    *(unsigned int *)(a2 + a3 + a3 * 2 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + a3 + a3 * 2 * 8 + 16)));
    a3 = (unsigned int)((a3) + 1);
    goto loc_008B1965;
loc_008B1998:
    if (((unsigned int)(v_rdi)) == 0x80000005ULL) goto loc_008B1962;
loc_008B19A0:
    goto loc_008B18AA;
loc_008B19B1:
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + a3 + a3 * 2 * 8 + 16)))) != 0xC0000503ULL) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + a3 + a3 * 2 * 8 + 16))); }
loc_008B19BB:
    goto loc_008B17CD;
loc_008B19C5:
    result = EtwGetKernelTraceTimestamp(v_stack_p160, (unsigned int)(0x20000ULL), a3, a4);
    goto loc_008B1480;
loc_008B19DC:
    goto loc_008B19BB;
loc_008B19E3:
    if (v_stack_p58 == 0) goto loc_008B1548;
    v_stack_pA0 = *(unsigned __int64 *)(v_stack_p58 + 8);
    goto loc_008B1548;
loc_008B1A02:
    result = ObfDereferenceObject(v_stack_p58, (unsigned int)(0x20000ULL), a3, a4);
    goto loc_008B17DB;
loc_008B1A0C:
    v_stack_p20 = v_stack_pA0;
    result = guard_dispatch_icall(19, v_stack_p160, (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_008B18E2;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryMultipleValueKey(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint8_t v_stack_m210;
    uint32_t v_stack_m214;
    uint8_t v_stack_m217;
    uint8_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p160;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p44;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p6C;
    uint64_t v_stack_pA0;

    local_rsp = (local_rsp) - (552);
    result = (*(uint64_t *)(v_rip + 0x559377)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1E8 = Arg4;
    v_stack_m1C8 = Arg2;
    v_stack_m208 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m1C0 = Arg5;
    result = 0;
    v_stack_m160 = v_xmm0;
    v_stack_m150 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, result + 88, Arg4);
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    if ((*(uint64_t *)(v_rip + 0x726B8E)) != 0) goto loc_008B19C5;
loc_008B1480:
    v_stack_m218 = 0;
    v_stack_m217 = 0;
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, Arg2 + 72, Arg4);
    v_stack_m1D0 = v_stack_m1D8;
    v_stack_m1D8 = v_stack_m1D8;
    result = CmpInitializeThreadInfo(v_stack_m160, Arg2, Arg2 + 72, Arg4);
    result = CmpAcquireShutdownRundown(v_stack_m160, Arg2, Arg2 + 72, Arg4);
    v_stack_m210 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_008B19DC;
    v_stack_m238 = v_stack_m200;
    result = CmObReferenceObjectByHandle(Arg1, 1, Arg2 + 72, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if (sign_flag) goto loc_008B19BB;
    if ((*(uint64_t *)(v_rip + 0x726AC6)) != 0) goto loc_008B19E3;
loc_008B1548:
    if (((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) != 1) goto loc_008B15AE;
    result = (uint32_t)((uint32_t)(result));
    if (Arg5 < ((uint32_t)((uint32_t)(result)))) { result = Arg5; }
    v_stack_m214 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((uint32_t)((uint32_t)(Arg3))) > 0x10000ULL) goto loc_008B15B8;
    Arg2 = ((uint32_t)(Arg3) + (uint32_t)(Arg3) * 2) << (3);
    result = ProbeForWrite(Arg2, Arg2, 4, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    local_rdi = (uint32_t)((uint32_t)(result));
    if (Arg6 != 0) {
        local_rdi = (uint32_t)((uint32_t)(result));
        if (Arg6 < ((uint32_t)((uint32_t)(result)))) { local_rdi = Arg6; }
        result = *(uint32_t *)(local_rdi);
        *(uint32_t *)(local_rdi) = (uint32_t)(result);
    }
    result = ProbeForWrite(v_stack_m1E8, (uint32_t)(v_stack_m214), 4, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    goto loc_008B15C2;
loc_008B15AE:
    v_stack_m214 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    goto loc_008B15C2;
loc_008B15B8:
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), (uint32_t)(v_stack_m214), 4, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
loc_008B15C2:
    goto loc_008B15E5;
loc_008B15E5:
    v_stack_m230 = v_stack_m1A8;
    v_stack_m238 = v_stack_m1B0;
    result = CmpCaptureKeyValueArray(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), v_stack_m1F8);
    if (sign_flag) goto loc_008B19BB;
    v_stack_m217 = 1;
    if ((*(uint32_t *)(v_rip + 0x63E54F)) == 0) goto loc_008B16CE;
    result = CmpIsRegistryLockAcquired(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), v_stack_m1F8);
    if ((uint32_t)(result) != 0) goto loc_008B16CE;
    v_stack_m148 = v_stack_m200;
    v_stack_m140 = v_stack_m1F8;
    v_stack_m138 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m130 = v_stack_m1E8;
    v_stack_m128 = v_stack_m214;
    v_stack_m120 = Arg6;
    v_stack_m228 = v_stack_m1D8;
    v_stack_m230 = v_stack_m200;
    v_stack_m238 = 24;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 9, v_stack_m148, Arg3, 1);
    if (sign_flag) goto loc_008B19B1;
    v_stack_m218 = 1;
loc_008B16CE:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m200, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), 1, v_stack_m1E0);
    if (sign_flag) goto loc_008B19BB;
    v_stack_m238 = 4;
    result = CmpBounceContextStart(v_stack_mA8, v_stack_m1E8, (uint32_t)(v_stack_m214), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))));
    if (sign_flag) goto loc_008B19BB;
    result = CmpAttachToRegistryProcess(v_stack_mD8, v_stack_m1E8, (uint32_t)(v_stack_m214), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))));
    v_stack_m228 = v_stack_m1F0;
    v_stack_m230 = v_stack_m214;
    v_stack_m238 = v_stack_mA0;
    result = CmQueryMultipleValueKey(v_stack_m200, v_stack_m1E0, v_stack_m1F8, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    result = CmpDetachFromRegistryProcess(v_stack_mD8, v_stack_m1E0, v_stack_m1F8, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if (Arg6 != 0) {
        result = v_stack_m1F0;
        *(uint32_t *)(Arg6) = (uint32_t)(result);
    }
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_008B1790;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0x80000005ULL) goto loc_008B17AF;
loc_008B1790:
    result = (uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1;
    if (v_stack_mA8 != v_stack_mA0) {
        result = memcpy(v_stack_mA8, v_stack_mA0, (uint32_t)(v_stack_m214), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    }
    goto loc_008B17CD;
loc_008B17CD:
    if (v_stack_m1E0 != 0) goto loc_008B1A02;
loc_008B17DB:
    if (v_stack_m218 == 0) goto loc_008B189E;
    if ((*(uint32_t *)(v_rip + 0x63E39B)) == 0) goto loc_008B189E;
    result = CmpIsRegistryLockAcquired(v_stack_m1E0, v_stack_mA0, (uint32_t)(v_stack_m214), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if ((uint32_t)(result) != 0) goto loc_008B189E;
    result = v_stack_m1D8;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (v_stack_m1D8 != v_stack_m1D8) {
        result = 0;
        v_stack_m198 = v_xmm0;
        v_stack_m188 = v_xmm0;
        v_stack_m178 = v_xmm0;
        v_stack_m168 = 0;
        Arg1 = v_stack_m200;
        v_stack_m198 = Arg1;
        v_stack_m190 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m180 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_m148;
        v_stack_m188 = result;
        result = v_stack_m1D8;
        v_stack_m228 = result;
        v_stack_m230 = Arg1;
        v_stack_m238 = 24;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m198;
        Arg1 = Arg4 + 24;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m180;
    }
    if (v_stack_m1F8 != 0) goto loc_008B1953;
loc_008B18AA:
    if (v_stack_m217 != 0) {
        result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m200 != 0) {
        result = ObfDereferenceObject(v_stack_m200, Arg2, Arg3, Arg4);
    }
    result = CmpBounceContextCleanup(v_stack_mA8, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(v_rip + 0x72672F) != 0) goto loc_008B1A0C;
loc_008B18E2:
    result = *(uint64_t *)(v_rip + 0x72672F);
    if (v_stack_m210 != 0) {
        result = CmpReleaseShutdownRundown(v_stack_mA8, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1F8 != 0) {
        result = CmSiFreeMemory(v_stack_m1F8, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1B0 != 0) {
        result = CmSiFreeMemory(v_stack_m1B0, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1A8 != 0) {
        result = CmSiFreeMemory(v_stack_m1A8, Arg2, Arg3, Arg4);
    }
    result = CmCleanupThreadInfo(v_stack_m160, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (552);
    return result;
loc_008B1953:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(v_stack_p44));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(local_rdi + (uint32_t)(0x80000000ULL) * 1))) == 0) goto loc_008B1998;
loc_008B1962:
    Arg3 = 0;
loc_008B1965:
    v_stack_p6C = 0;
    if (0 >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_008B19A0;
    *(uint32_t *)(arg2 + Arg3 + Arg3 * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + Arg3 + Arg3 * 2 * 8 + 0x8)));
    *(uint32_t *)(arg2 + Arg3 + Arg3 * 2 * 8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + Arg3 + Arg3 * 2 * 8 + 0xC)));
    *(uint32_t *)(arg2 + Arg3 + Arg3 * 2 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + Arg3 + Arg3 * 2 * 8 + 0x10)));
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_008B1965;
loc_008B1998:
    if (((uint32_t)(local_rdi)) == 0x80000005ULL) goto loc_008B1962;
loc_008B19A0:
    goto loc_008B18AA;
loc_008B19B1:
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + Arg3 + Arg3 * 2 * 8 + 0x10)))) != 0xC0000503ULL) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + Arg3 + Arg3 * 2 * 8 + 0x10))); }
loc_008B19BB:
    goto loc_008B17CD;
loc_008B19C5:
    result = EtwGetKernelTraceTimestamp(v_stack_p160, (uint32_t)(0x20000ULL), Arg3, Arg4);
    goto loc_008B1480;
loc_008B19DC:
    goto loc_008B19BB;
loc_008B19E3:
    if (v_stack_p58 == 0) goto loc_008B1548;
    v_stack_pA0 = *(uint64_t *)(v_stack_p58 + 0x8);
    goto loc_008B1548;
loc_008B1A02:
    result = ObfDereferenceObject(v_stack_p58, (uint32_t)(0x20000ULL), Arg3, Arg4);
    goto loc_008B17DB;
loc_008B1A0C:
    v_stack_p20 = v_stack_pA0;
    result = guard_dispatch_icall(19, v_stack_p160, (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_008B18E2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8 + rdx*8` | `32` | `W` |
| `Arg2` | `+ 0xC + rdx*8` | `32` | `W` |
| `Arg2` | `+ 0x10 + rdx*8` | `32` | `W` |
| `Arg5` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B13B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
