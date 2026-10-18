# NtQueryValueKey

- RVA: `0x008B2A00`–`0x008B31F4` (길이 `2,036` bytes)
- VA: `0x00000001408B2A00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000826BC`
- 디코드: `421`개 명령, `2,036/2,036` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x008B2A77` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B2AEB` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008B2B03` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B2B30` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x008B2B3D` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x008B2B86` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x008B2C1C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B2C6C` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x008B2D25` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008B2D2E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008B2DD0` → [CmKeyBodyRemapToVirtualForEnum](CmKeyBodyRemapToVirtualForEnum_function_008B46C0.md) (function, `0x008B46C0`)
- `0x008B2DF8` → [CmpBounceContextStart](CmpBounceContextStart_function_008B27F0.md) (function, `0x008B27F0`)
- `0x008B2E8D` → [KeExpandKernelStackAndCallout](../../text/46/KeExpandKernelStackAndCallout_function_004675F0.md) (function, `0x004675F0`)
- `0x008B2EE0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B2F26` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B2F35` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B2F85` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x008B2F92` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x008B2FA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B2FCA` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B3069` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B308F` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (function, `0x0038ACC0`)
- `0x008B30A6` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x008B30D0` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B3142` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B316D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B319E` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B31C7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B31EA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x006FFE63`
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x006FFEA8`
- [sub_00B2CB5C](../B2/Unknown_function_00B2CB5C.md) at `0x00B2CBAC`
- [InitSafeBoot](../../init/C1/InitSafeBoot_function_00C1BFE0.md) at `0x00C1C0AE`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B16F`
- [IopProtectSystemPartition](../../init/C2/IopProtectSystemPartition_function_00C2E5EC.md) at `0x00C2E6AC`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C522DF`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C52350`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C52506`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C52569`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C525DC`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C529F8`

### Static image references
- `0x008B2A13` → RVA `0x00E0A740` (`.data`; read)
- `0x008B2AC3` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x008B2BD4` → RVA `0x00EF7208` (`.data`; read)
- `0x008B2DAD` → RVA `0x00EEFB88` (`.data`; read)
- `0x008B2E86` → RVA `0x00A19D70` (`CmQueryValueKeyCallout`; read)
- `0x008B3088` → RVA `0x00E2CA40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x008B2A77` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B2AEB` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008B2B03` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B2B30` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x008B2B3D` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x008B2B86` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x008B2C1C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B2C6C` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x008B2E8D` → [KeExpandKernelStackAndCallout](../../text/46/KeExpandKernelStackAndCallout_function_004675F0.md) (`PAGE` → `.text`)
  - `0x008B2EE0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B2F26` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B2F35` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B2F85` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x008B2F92` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x008B2FA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B2FCA` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B308F` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (`PAGE` → `.text`)
  - `0x008B30A6` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x008B30D0` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B316D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B319E` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B31C7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B31EA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008B2B55` → [sub_00B1A740](../B1/Unknown_function_00B1A740.md) (`tail-transfer`)
  - `0x008B2E65` → [sub_00B1A740 + 0x5F](../B1/Unknown_function_00B1A740.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008B2A00  40 53                           push rbx
008B2A02  56                              push rsi
008B2A03  57                              push rdi
008B2A04  41 54                           push r12
008B2A06  41 55                           push r13
008B2A08  41 56                           push r14
008B2A0A  41 57                           push r15
008B2A0C  48 81 EC 80 02 00 00            sub rsp, 0x280
008B2A13  48 8B 05 26 7D 55 00            mov rax, qword ptr [rip + 0x557d26]
008B2A1A  48 33 C4                        xor rax, rsp
008B2A1D  48 89 84 24 70 02 00 00         mov qword ptr [rsp + 0x270], rax
008B2A25  4D 8B F9                        mov r15, r9
008B2A28  45 8B E8                        mov r13d, r8d
008B2A2B  48 8B F2                        mov rsi, rdx
008B2A2E  48 8B F9                        mov rdi, rcx
008B2A31  48 8B 94 24 E8 02 00 00         mov rdx, qword ptr [rsp + 0x2e8]
008B2A39  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
008B2A3E  44 89 84 24 88 00 00 00         mov dword ptr [rsp + 0x88], r8d
008B2A46  0F 57 C0                        xorps xmm0, xmm0
008B2A49  33 C0                           xor eax, eax
008B2A4B  0F 11 84 24 48 01 00 00         movups xmmword ptr [rsp + 0x148], xmm0
008B2A53  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
008B2A5B  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
008B2A60  33 DB                           xor ebx, ebx
008B2A62  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
008B2A69  33 D2                           xor edx, edx
008B2A6B  44 8D 40 58                     lea r8d, [rax + 0x58]
008B2A6F  48 8D 8C 24 D0 01 00 00         lea rcx, [rsp + 0x1d0]
008B2A77  E8 C4 41 E1 FF                  call 0x1406c6c40
008B2A7C  33 C0                           xor eax, eax
008B2A7E  0F 57 C0                        xorps xmm0, xmm0
008B2A81  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
008B2A89  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008B2A91  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008B2A99  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
008B2AA1  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
008B2AA8  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
008B2AB0  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
008B2AB8  44 8B E3                        mov r12d, ebx
008B2ABB  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
008B2AC3  48 39 05 3E 55 72 00            cmp qword ptr [rip + 0x72553e], rax
008B2ACA  0F 85 C9 05 00 00               jne 0x1408b3099
008B2AD0  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
008B2AD4  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
008B2AD8  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
008B2ADD  89 9C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ebx
008B2AE4  33 D2                           xor edx, edx
008B2AE6  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
008B2AEB  E8 90 7C B7 FF                  call 0x14042a780
008B2AF0  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008B2AF5  33 D2                           xor edx, edx
008B2AF7  44 8D 42 48                     lea r8d, [rdx + 0x48]
008B2AFB  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
008B2B03  E8 38 41 E1 FF                  call 0x1406c6c40
008B2B08  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008B2B10  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008B2B18  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008B2B20  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
008B2B28  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
008B2B30  E8 3B 93 B4 FF                  call 0x1403fbe70
008B2B35  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008B2B3D  E8 BE 68 31 00                  call 0x140bc9400
008B2B42  44 8A F0                        mov r14b, al
008B2B45  88 44 24 40                     mov byte ptr [rsp + 0x40], al
008B2B49  84 C0                           test al, al
008B2B4B  0F 84 80 06 00 00               je 0x1408b31d1
008B2B51  41 83 FD 04                     cmp r13d, 4
008B2B55  0F 87 E5 7B 26 00               ja 0x140b1a740
008B2B5B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B2B64  44 0F BE B0 32 02 00 00         movsx r14d, byte ptr [rax + 0x232]
008B2B6C  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
008B2B71  48 8D 44 24 68                  lea rax, [rsp + 0x68]
008B2B76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B2B7B  45 8A CE                        mov r9b, r14b
008B2B7E  BA 01 00 00 00                  mov edx, 1
008B2B83  48 8B CF                        mov rcx, rdi
008B2B86  E8 C5 67 31 00                  call 0x140bc9350
008B2B8B  8B F8                           mov edi, eax
008B2B8D  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008B2B91  85 C0                           test eax, eax
008B2B93  0F 88 2D 05 00 00               js 0x1408b30c6
008B2B99  48 39 1D 68 54 72 00            cmp qword ptr [rip + 0x725468], rbx
008B2BA0  0F 85 D1 05 00 00               jne 0x1408b3177
008B2BA6  41 80 FE 01                     cmp r14b, 1
008B2BAA  0F 84 D6 00 00 00               je 0x1408b2c86
008B2BB0  0F 10 06                        movups xmm0, xmmword ptr [rsi]
008B2BB3  F3 0F 7F 44 24 50               movdqu xmmword ptr [rsp + 0x50], xmm0
008B2BB9  8B B4 24 E0 02 00 00            mov esi, dword ptr [rsp + 0x2e0]
008B2BC0  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008B2BC5  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008B2BCA  66 89 54 24 52                  mov word ptr [rsp + 0x52], dx
008B2BCF  45 84 F6                        test r14b, r14b
008B2BD2  75 1B                           jne 0x1408b2bef
008B2BD4  48 83 3D 2C 46 64 00 00         cmp qword ptr [rip + 0x64462c], 0
008B2BDC  74 52                           je 0x1408b2c30
008B2BDE  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
008B2BE8  48 39 44 24 58                  cmp qword ptr [rsp + 0x58], rax
008B2BED  77 41                           ja 0x1408b2c30
008B2BEF  66 85 D2                        test dx, dx
008B2BF2  74 6B                           je 0x1408b2c5f
008B2BF4  83 FA 40                        cmp edx, 0x40
008B2BF7  77 6D                           ja 0x1408b2c66
008B2BF9  48 8D 84 24 30 02 00 00         lea rax, [rsp + 0x230]
008B2C01  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B2C06  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B2C0B  48 85 C0                        test rax, rax
008B2C0E  74 16                           je 0x1408b2c26
008B2C10  44 0F B7 C2                     movzx r8d, dx
008B2C14  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008B2C19  48 8B C8                        mov rcx, rax
008B2C1C  E8 1F 3C E1 FF                  call 0x1406c6840
008B2C21  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008B2C26  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B2C2B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008B2C30  F6 C2 01                        test dl, 1
008B2C33  0F 85 0D 01 00 00               jne 0x1408b2d46
008B2C39  66 85 D2                        test dx, dx
008B2C3C  0F 84 25 01 00 00               je 0x1408b2d67
008B2C42  0F B7 D2                        movzx edx, dx
008B2C45  8B CA                           mov ecx, edx
008B2C47  48 D1 E9                        shr rcx, 1
008B2C4A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008B2C4F  66 39 5C 48 FE                  cmp word ptr [rax + rcx*2 - 2], bx
008B2C54  0F 84 FF 00 00 00               je 0x1408b2d59
008B2C5A  E9 08 01 00 00                  jmp 0x1408b2d67
008B2C5F  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008B2C64  EB C0                           jmp 0x1408b2c26
008B2C66  41 B8 43 4D 76 6E               mov r8d, 0x6e764d43
008B2C6C  E8 1F E5 BA FF                  call 0x140461190
008B2C71  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B2C76  48 85 C0                        test rax, rax
008B2C79  0F 84 B4 00 00 00               je 0x1408b2d33
008B2C7F  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008B2C84  EB 80                           jmp 0x1408b2c06
008B2C86  0F 57 C0                        xorps xmm0, xmm0
008B2C89  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
008B2C91  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008B2C9B  48 8B CA                        mov rcx, rdx
008B2C9E  48 3B F2                        cmp rsi, rdx
008B2CA1  48 0F 42 CE                     cmovb rcx, rsi
008B2CA5  90                              nop
008B2CA6  8B 01                           mov eax, dword ptr [rcx]
008B2CA8  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
008B2CAF  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
008B2CB3  4C 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], r8
008B2CBB  0F 28 84 24 00 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x100]
008B2CC3  66 0F 7F 44 24 50               movdqa xmmword ptr [rsp + 0x50], xmm0
008B2CC9  66 0F 7E C0                     movd eax, xmm0
008B2CCD  66 85 C0                        test ax, ax
008B2CD0  74 1B                           je 0x1408b2ced
008B2CD2  41 F6 C0 01                     test r8b, 1
008B2CD6  75 4D                           jne 0x1408b2d25
008B2CD8  0F B7 C0                        movzx eax, ax
008B2CDB  4E 8D 0C 00                     lea r9, [rax + r8]
008B2CDF  4A 8D 0C 00                     lea rcx, [rax + r8]
008B2CE3  48 3B CA                        cmp rcx, rdx
008B2CE6  77 42                           ja 0x1408b2d2a
008B2CE8  4D 3B C8                        cmp r9, r8
008B2CEB  72 3D                           jb 0x1408b2d2a
008B2CED  8B B4 24 E0 02 00 00            mov esi, dword ptr [rsp + 0x2e0]
008B2CF4  85 F6                           test esi, esi
008B2CF6  75 15                           jne 0x1408b2d0d
008B2CF8  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008B2CFD  48 3B FA                        cmp rdi, rdx
008B2D00  48 0F 42 D7                     cmovb rdx, rdi
008B2D04  8B 02                           mov eax, dword ptr [rdx]
008B2D06  89 02                           mov dword ptr [rdx], eax
008B2D08  E9 B8 FE FF FF                  jmp 0x1408b2bc5
008B2D0D  41 F6 C7 03                     test r15b, 3
008B2D11  75 1B                           jne 0x1408b2d2e
008B2D13  49 8D 0C 37                     lea rcx, [r15 + rsi]
008B2D17  48 3B CA                        cmp rcx, rdx
008B2D1A  77 05                           ja 0x1408b2d21
008B2D1C  49 3B CF                        cmp rcx, r15
008B2D1F  73 D7                           jae 0x1408b2cf8
008B2D21  8A 02                           mov al, byte ptr [rdx]
008B2D23  EB D3                           jmp 0x1408b2cf8
008B2D25  E8 A6 72 FE FF                  call 0x140899fd0
008B2D2A  8A 02                           mov al, byte ptr [rdx]
008B2D2C  EB BF                           jmp 0x1408b2ced
008B2D2E  E8 9D 72 FE FF                  call 0x140899fd0
008B2D33  BF 9A 00 00 C0                  mov edi, 0xc000009a
008B2D38  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
008B2D3C  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B2D41  E9 BF 01 00 00                  jmp 0x1408b2f05
008B2D46  BF 0D 00 00 C0                  mov edi, 0xc000000d
008B2D4B  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
008B2D4F  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B2D54  E9 AC 01 00 00                  jmp 0x1408b2f05
008B2D59  66 83 EA 02                     sub dx, 2
008B2D5D  66 89 54 24 50                  mov word ptr [rsp + 0x50], dx
008B2D62  E9 D2 FE FF FF                  jmp 0x1408b2c39
008B2D67  EB 2E                           jmp 0x1408b2d97
008B2D69  8B F8                           mov edi, eax
008B2D6B  33 C0                           xor eax, eax
008B2D6D  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
008B2D72  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
008B2D77  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
008B2D7B  33 DB                           xor ebx, ebx
008B2D7D  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
008B2D85  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
008B2D8D  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B2D92  E9 6E 01 00 00                  jmp 0x1408b2f05
008B2D97  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B2DA0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B2DA7  90                              nop
008B2DA8  C6 44 24 42 01                  mov byte ptr [rsp + 0x42], 1
008B2DAD  83 3D D4 CD 63 00 00            cmp dword ptr [rip + 0x63cdd4], 0
008B2DB4  0F 85 16 03 00 00               jne 0x1408b30d0
008B2DBA  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
008B2DC2  41 B8 01 00 00 00               mov r8d, 1
008B2DC8  41 8A D6                        mov dl, r14b
008B2DCB  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
008B2DD0  E8 EB 18 00 00                  call 0x1408b46c0
008B2DD5  8B F8                           mov edi, eax
008B2DD7  85 C0                           test eax, eax
008B2DD9  0F 88 E7 02 00 00               js 0x1408b30c6
008B2DDF  45 8B CE                        mov r9d, r14d
008B2DE2  44 8B C6                        mov r8d, esi
008B2DE5  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
008B2DED  49 8B D7                        mov rdx, r15
008B2DF0  48 8D 8C 24 D0 01 00 00         lea rcx, [rsp + 0x1d0]
008B2DF8  E8 F3 F9 FF FF                  call 0x1408b27f0
008B2DFD  8B F8                           mov edi, eax
008B2DFF  85 C0                           test eax, eax
008B2E01  0F 88 BF 02 00 00               js 0x1408b30c6
008B2E07  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
008B2E0F  89 9C 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], ebx
008B2E16  89 9C 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], ebx
008B2E1D  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
008B2E22  F3 0F 7F 84 24 C0 00 00 00      movdqu xmmword ptr [rsp + 0xc0], xmm0
008B2E2B  44 89 AC 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r13d
008B2E33  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
008B2E3B  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
008B2E43  89 B4 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], esi
008B2E4A  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B2E52  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
008B2E5A  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008B2E62  48 85 C9                        test rcx, rcx
008B2E65  0F 85 34 79 26 00               jne 0x140b1a79f
008B2E6B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008B2E70  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008B2E78  41 B8 00 48 00 00               mov r8d, 0x4800
008B2E7E  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
008B2E86  48 8D 0D E3 6E 16 00            lea rcx, [rip + 0x166ee3]
008B2E8D  E8 5E 47 BB FF                  call 0x1404675f0
008B2E92  8B F8                           mov edi, eax
008B2E94  85 C0                           test eax, eax
008B2E96  0F 88 2A 02 00 00               js 0x1408b30c6
008B2E9C  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
008B2EA3  8B F8                           mov edi, eax
008B2EA5  85 C0                           test eax, eax
008B2EA7  0F 88 03 02 00 00               js 0x1408b30b0
008B2EAD  90                              nop
008B2EAE  8B 8C 24 80 00 00 00            mov ecx, dword ptr [rsp + 0x80]
008B2EB5  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008B2EBA  89 0A                           mov dword ptr [rdx], ecx
008B2EBC  3D 23 00 00 C0                  cmp eax, 0xc0000023
008B2EC1  74 22                           je 0x1408b2ee5
008B2EC3  3B CE                           cmp ecx, esi
008B2EC5  0F 42 F1                        cmovb esi, ecx
008B2EC8  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
008B2ED0  48 8B 94 24 D8 01 00 00         mov rdx, qword ptr [rsp + 0x1d8]
008B2ED8  48 3B CA                        cmp rcx, rdx
008B2EDB  74 08                           je 0x1408b2ee5
008B2EDD  44 8B C6                        mov r8d, esi
008B2EE0  E8 5B 39 E1 FF                  call 0x1406c6840
008B2EE5  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B2EEA  EB 19                           jmp 0x1408b2f05
008B2EEC  8B F8                           mov edi, eax
008B2EEE  33 DB                           xor ebx, ebx
008B2EF0  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
008B2EF8  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
008B2F00  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B2F05  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008B2F0D  48 85 C9                        test rcx, rcx
008B2F10  0F 85 D4 02 00 00               jne 0x1408b31ea
008B2F16  38 5C 24 41                     cmp byte ptr [rsp + 0x41], bl
008B2F1A  0F 85 9D 00 00 00               jne 0x1408b2fbd
008B2F20  38 5C 24 42                     cmp byte ptr [rsp + 0x42], bl
008B2F24  74 05                           je 0x1408b2f2b
008B2F26  E8 85 A9 9A FF                  call 0x14025d8b0
008B2F2B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B2F30  48 85 C9                        test rcx, rcx
008B2F33  74 05                           je 0x1408b2f3a
008B2F35  E8 16 64 A4 FF                  call 0x1402f9350
008B2F3A  48 8B 94 24 D8 01 00 00         mov rdx, qword ptr [rsp + 0x1d8]
008B2F42  48 85 D2                        test rdx, rdx
008B2F45  74 1B                           je 0x1408b2f62
008B2F47  48 3B 94 24 D0 01 00 00         cmp rdx, qword ptr [rsp + 0x1d0]
008B2F4F  74 11                           je 0x1408b2f62
008B2F51  48 8D 84 24 E1 01 00 00         lea rax, [rsp + 0x1e1]
008B2F59  48 3B D0                        cmp rdx, rax
008B2F5C  0F 85 18 01 00 00               jne 0x1408b307a
008B2F62  48 8B 05 9F 50 72 00            mov rax, qword ptr [rip + 0x72509f]
008B2F69  48 85 C0                        test rax, rax
008B2F6C  0F 85 36 02 00 00               jne 0x1408b31a8
008B2F72  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008B2F77  48 85 C0                        test rax, rax
008B2F7A  0F 85 D9 01 00 00               jne 0x1408b3159
008B2F80  45 84 F6                        test r14b, r14b
008B2F83  74 05                           je 0x1408b2f8a
008B2F85  E8 F6 68 31 00                  call 0x140bc9880
008B2F8A  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
008B2F92  E8 B9 CD B6 FF                  call 0x14041fd50
008B2F97  8B C7                           mov eax, edi
008B2F99  48 8B 8C 24 70 02 00 00         mov rcx, qword ptr [rsp + 0x270]
008B2FA1  48 33 CC                        xor rcx, rsp
008B2FA4  E8 97 96 DF FF                  call 0x1406ac640
008B2FA9  48 81 C4 80 02 00 00            add rsp, 0x280
008B2FB0  41 5F                           pop r15
008B2FB2  41 5E                           pop r14
008B2FB4  41 5D                           pop r13
008B2FB6  41 5C                           pop r12
008B2FB8  5F                              pop rdi
008B2FB9  5E                              pop rsi
008B2FBA  5B                              pop rbx
008B2FBB  C3                              ret
008B2FBC  CC                              int3
008B2FBD  83 3D C4 CB 63 00 00            cmp dword ptr [rip + 0x63cbc4], 0
008B2FC4  0F 84 56 FF FF FF               je 0x1408b2f20
008B2FCA  E8 AD 3A BA FF                  call 0x140456a7c
008B2FCF  85 C0                           test eax, eax
008B2FD1  0F 85 49 FF FF FF               jne 0x1408b2f20
008B2FD7  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008B2FDF  48 39 84 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rax
008B2FE7  0F 84 33 FF FF FF               je 0x1408b2f20
008B2FED  0F 57 C0                        xorps xmm0, xmm0
008B2FF0  33 C0                           xor eax, eax
008B2FF2  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
008B2FFA  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
008B3002  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
008B300A  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
008B3012  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B3017  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
008B301F  89 BC 24 18 01 00 00            mov dword ptr [rsp + 0x118], edi
008B3026  89 BC 24 28 01 00 00            mov dword ptr [rsp + 0x128], edi
008B302D  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
008B3035  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
008B303D  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008B3045  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B304A  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B304F  C7 44 24 20 17 00 00 00         mov dword ptr [rsp + 0x20], 0x17
008B3057  45 33 C9                        xor r9d, r9d
008B305A  45 33 C0                        xor r8d, r8d
008B305D  48 8D 94 24 10 01 00 00         lea rdx, [rsp + 0x110]
008B3065  41 8D 49 17                     lea ecx, [r9 + 0x17]
008B3069  E8 D2 2E FB FF                  call 0x140865f40
008B306E  8B BC 24 28 01 00 00            mov edi, dword ptr [rsp + 0x128]
008B3075  E9 A6 FE FF FF                  jmp 0x1408b2f20
008B307A  F6 84 24 E0 01 00 00 01         test byte ptr [rsp + 0x1e0], 1
008B3082  0F 84 0E 01 00 00               je 0x1408b3196
008B3088  48 8D 0D B1 99 57 00            lea rcx, [rip + 0x5799b1]
008B308F  E8 2C 7C AD FF                  call 0x14038acc0
008B3094  E9 C9 FE FF FF                  jmp 0x1408b2f62
008B3099  BA 00 00 02 00                  mov edx, 0x20000
008B309E  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008B30A6  E8 A5 CB AE FF                  call 0x14039fc50
008B30AB  E9 20 FA FF FF                  jmp 0x1408b2ad0
008B30B0  3D 05 00 00 80                  cmp eax, 0x80000005
008B30B5  0F 84 F2 FD FF FF               je 0x1408b2ead
008B30BB  3D 23 00 00 C0                  cmp eax, 0xc0000023
008B30C0  0F 84 E7 FD FF FF               je 0x1408b2ead
008B30C6  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
008B30CB  E9 35 FE FF FF                  jmp 0x1408b2f05
008B30D0  E8 A7 39 BA FF                  call 0x140456a7c
008B30D5  85 C0                           test eax, eax
008B30D7  0F 85 DD FC FF FF               jne 0x1408b2dba
008B30DD  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B30E2  48 89 8C 24 60 01 00 00         mov qword ptr [rsp + 0x160], rcx
008B30EA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008B30EF  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
008B30F7  44 89 AC 24 70 01 00 00         mov dword ptr [rsp + 0x170], r13d
008B30FF  4C 89 BC 24 78 01 00 00         mov qword ptr [rsp + 0x178], r15
008B3107  89 B4 24 80 01 00 00            mov dword ptr [rsp + 0x180], esi
008B310E  48 89 BC 24 88 01 00 00         mov qword ptr [rsp + 0x188], rdi
008B3116  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008B311E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B3123  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B3128  C7 44 24 20 17 00 00 00         mov dword ptr [rsp + 0x20], 0x17
008B3130  41 B1 01                        mov r9b, 1
008B3133  45 33 C0                        xor r8d, r8d
008B3136  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
008B313E  41 8D 48 08                     lea ecx, [r8 + 8]
008B3142  E8 F9 2D FB FF                  call 0x140865f40
008B3147  85 C0                           test eax, eax
008B3149  0F 88 8C 00 00 00               js 0x1408b31db
008B314F  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008B3154  E9 61 FC FF FF                  jmp 0x1408b2dba
008B3159  48 8D 8C 24 30 02 00 00         lea rcx, [rsp + 0x230]
008B3161  48 3B C1                        cmp rax, rcx
008B3164  0F 84 16 FE FF FF               je 0x1408b2f80
008B316A  48 8B C8                        mov rcx, rax
008B316D  E8 0E 2C BC FF                  call 0x140475d80
008B3172  E9 09 FE FF FF                  jmp 0x1408b2f80
008B3177  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008B317C  48 85 C0                        test rax, rax
008B317F  0F 84 21 FA FF FF               je 0x1408b2ba6
008B3185  4C 8B 60 08                     mov r12, qword ptr [rax + 8]
008B3189  4C 89 A4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r12
008B3191  E9 10 FA FF FF                  jmp 0x1408b2ba6
008B3196  48 8B 8C 24 D8 01 00 00         mov rcx, qword ptr [rsp + 0x1d8]
008B319E  E8 DD 2B BC FF                  call 0x140475d80
008B31A3  E9 BA FD FF FF                  jmp 0x1408b2f62
008B31A8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
008B31AD  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B31B2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008B31B7  45 8B CD                        mov r9d, r13d
008B31BA  44 8B C7                        mov r8d, edi
008B31BD  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
008B31C5  B1 10                           mov cl, 0x10
008B31C7  E8 04 79 E0 FF                  call 0x1406baad0
008B31CC  E9 A1 FD FF FF                  jmp 0x1408b2f72
008B31D1  BF 89 01 00 C0                  mov edi, 0xc0000189
008B31D6  E9 2A FD FF FF                  jmp 0x1408b2f05
008B31DB  8B FB                           mov edi, ebx
008B31DD  3D 03 05 00 C0                  cmp eax, 0xc0000503
008B31E2  0F 45 F8                        cmovne edi, eax
008B31E5  E9 DC FE FF FF                  jmp 0x1408b30c6
008B31EA  E8 61 61 A4 FF                  call 0x1402f9350
008B31EF  E9 22 FD FF FF                  jmp 0x1408b2f16
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryValueKey(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int16 v_stack_m266;
    unsigned __int64 v_stack_m268;
    unsigned __int8 v_stack_m276;
    unsigned __int8 v_stack_m277;
    unsigned __int8 v_stack_m278;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mD7;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p110;
    unsigned int v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned int v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned int v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned int v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1D8;
    unsigned __int8 v_stack_p1E0;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p230;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;

    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 5602598)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m240 = a6;
    v_stack_m230 = a3;
    result = 0;
    v_stack_m170 = v_xmm0;
    v_stack_m160 = 0;
    v_stack_m268 = v_xmm0;
    v_rbx = 0;
    v_stack_m1C8 = 0;
    a2 = 0;
    result = memset(v_stack_mE8, a2, result + 88, a4);
    result = 0;
    v_stack_m208 = v_xmm0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm0;
    v_stack_m228 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7492926)) != 0) goto loc_008B3099;
loc_008B2AD0:
    v_stack_m277 = 0;
    v_stack_m276 = 0;
    v_stack_m250 = 0;
    v_stack_m238 = 0;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m268, a2, result + 88, a4);
    v_stack_m248 = 0;
    a2 = 0;
    result = memset(v_stack_m158, a2, a2 + 72, a4);
    v_stack_m210 = v_stack_m218;
    v_stack_m218 = v_stack_m218;
    result = CmpInitializeThreadInfo(v_stack_m170, a2, a2 + 72, a4);
    v_stack_m220 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m170, a2, a2 + 72, a4);
    v_stack_m278 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_008B31D1;
    v_stack_m290 = 0;
    v_stack_m298 = v_stack_m250;
    result = CmObReferenceObjectByHandle(a1, 1, a2 + 72, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    v_stack_m258 = (unsigned int)(result);
    if (sign_flag) goto loc_008B30C6;
    if ((*(unsigned __int64 *)(v_rip + 7492712)) != 0) goto loc_008B3177;
loc_008B2BA6:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) == 1) goto loc_008B2C86;
    v_stack_m268 = v_xmm0;
loc_008B2BC5:
    v_stack_m266 = (unsigned __int16)(v_stack_m268);
    if ((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 0) goto loc_008B2BEF;
    if ((*(unsigned __int64 *)(v_rip + 6571564)) == 0) goto loc_008B2C30;
    if (v_stack_m260 > result) goto loc_008B2C30;
loc_008B2BEF:
    if ((unsigned __int16)(v_stack_m268) == 0) goto loc_008B2C5F;
    if (((unsigned int)(v_stack_m268)) > 64) goto loc_008B2C66;
    v_stack_m248 = v_stack_m88;
loc_008B2C06:
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        a3 = (unsigned __int16)(v_stack_m268);
        a2 = v_stack_m260;
        a1 = v_stack_m248;
        result = memcpy(a1, a2, a3, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
        a2 = v_stack_m268;
    }
    v_stack_m260 = v_stack_m248;
loc_008B2C30:
    if ((((unsigned __int8)(a2)) & (1)) != 0) goto loc_008B2D46;
loc_008B2C39:
    if ((unsigned __int16)(a2) == 0) goto loc_008B2D67;
    a1 = ((unsigned int)((unsigned int)((unsigned __int16)(a2)))) >> (1);
    if ((*(unsigned __int16 *)(v_stack_m260 + a1 * 2 - 2)) == 0) goto loc_008B2D59;
    goto loc_008B2D67;
loc_008B2C5F:
    v_stack_m248 = 0;
    goto loc_008B2C26;
loc_008B2C66:
    result = CmpAllocateTransientPoolWithQuota(a1, (unsigned __int16)(a2), (unsigned int)(0x6E764D43ULL), (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    v_stack_m248 = result;
    if (result == 0) goto loc_008B2D33;
    goto loc_008B2C06;
loc_008B2C86:
    v_stack_m1B8 = v_xmm0;
    a1 = v_stack_m268;
    if (((unsigned int)(a5)) < v_stack_m268) { a1 = (unsigned int)(a5); }
    v_stack_m1B8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m1B0 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m268 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_008B2CED;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (1)) != 0) goto loc_008B2D25;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) > v_stack_m268) goto loc_008B2D2A;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) < (*(unsigned __int64 *)(a1 + 8))) goto loc_008B2D2A;
loc_008B2CED:
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_008B2D0D;
loc_008B2CF8:
    a2 = v_stack_m268;
    if (v_stack_m240 < v_stack_m268) { a2 = v_stack_m240; }
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    goto loc_008B2BC5;
loc_008B2D0D:
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_008B2D2E;
    if ((a4 + (unsigned int)(a5) * 1) > a2) goto loc_008B2D21;
    if ((a4 + (unsigned int)(a5) * 1) >= a4) goto loc_008B2CF8;
loc_008B2D21:
    goto loc_008B2CF8;
loc_008B2D25:
    result = ExRaiseDatatypeMisalignment(a4 + (unsigned int)(a5) * 1, a2, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
loc_008B2D2A:
    goto loc_008B2CED;
loc_008B2D2E:
    result = ExRaiseDatatypeMisalignment(a4 + (unsigned int)(a5) * 1, a2, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
loc_008B2D33:
    v_stack_m258 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_008B2F05;
loc_008B2D46:
    v_stack_m258 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008B2F05;
loc_008B2D59:
    a2 = (unsigned __int16)((a2) - (2));
    v_stack_m268 = (unsigned __int16)(a2);
    goto loc_008B2C39;
loc_008B2D67:
    goto loc_008B2D97;
loc_008B2D97:
    v_stack_m276 = 1;
    if ((*(unsigned int *)(v_rip + 6540756)) != 0) goto loc_008B30D0;
loc_008B2DBA:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m250, (unsigned __int8)(v_stack_m278), 1, v_stack_m220);
    if (sign_flag) goto loc_008B30C6;
    v_stack_m298 = 3;
    result = CmpBounceContextStart(v_stack_mE8, a4, (unsigned int)((unsigned int)((unsigned int)(a5))), (unsigned int)((unsigned int)(v_stack_m278)));
    if (sign_flag) goto loc_008B30C6;
    v_stack_m208 = 0;
    v_stack_m1E4 = 0;
    v_stack_m1D4 = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = (unsigned int)((unsigned int)(a3));
    v_stack_m1E0 = v_stack_mE0;
    v_stack_m1D8 = (unsigned int)((unsigned int)(a5));
    v_stack_m1D0 = v_stack_m238;
    v_stack_m200 = v_stack_m250;
    result = KeExpandKernelStackAndCallout(v_rip + 1470179, v_stack_m208, (unsigned int)(0x4800ULL), (unsigned int)((unsigned int)(v_stack_m278)));
    if (sign_flag) goto loc_008B30C6;
    if (sign_flag) goto loc_008B30B0;
loc_008B2EAD:
    *(unsigned int *)(v_stack_m240) = (unsigned int)((unsigned int)(v_stack_m238));
    if (((unsigned int)((unsigned int)(v_stack_m208))) == 0xC0000023ULL) goto loc_008B2EE5;
    v_rsi = (unsigned int)(a5);
    if (((unsigned int)((unsigned int)(v_stack_m238))) < ((unsigned int)((unsigned int)(a5)))) { v_rsi = (unsigned int)((unsigned int)(v_stack_m238)); }
    result = (unsigned int)(v_stack_m208);
    if (v_stack_mE8 != v_stack_mE0) {
        a3 = (unsigned int)(v_rsi);
        result = memcpy(v_stack_mE8, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    }
    goto loc_008B2F05;
loc_008B2F05:
    if (v_stack_m220 != 0) goto loc_008B31EA;
loc_008B2F16:
    if (v_stack_m277 != 0) goto loc_008B2FBD;
loc_008B2F20:
    if (v_stack_m276 != 0) {
        result = KeLeaveCriticalRegion(v_stack_m220, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    }
    if (v_stack_m250 != 0) {
        result = ObfDereferenceObject(v_stack_m250, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    }
    if (v_stack_mE0 == 0) goto loc_008B2F62;
    if (v_stack_mE0 == v_stack_mE8) goto loc_008B2F62;
    if (v_stack_mE0 != v_stack_mD7) goto loc_008B307A;
loc_008B2F62:
    if (*(unsigned __int64 *)(v_rip + 7491743) != 0) goto loc_008B31A8;
loc_008B2F72:
    if (v_stack_m248 != 0) goto loc_008B3159;
loc_008B2F80:
    result = v_stack_m248;
    if ((unsigned __int8)(v_stack_m278) != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m250, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    }
    result = CmCleanupThreadInfo(v_stack_m170, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    v_rsp = (v_rsp) + (640);
    return result;
loc_008B2FBD:
    if ((*(unsigned int *)(v_rip + 6540228)) == 0) goto loc_008B2F20;
    result = CmpIsRegistryLockAcquired(a1, v_stack_mE0, a3, (unsigned int)((unsigned int)(v_stack_m278)));
    if ((unsigned int)(result) != 0) goto loc_008B2F20;
    if (v_stack_pA0 == v_stack_pA0) goto loc_008B2F20;
    result = 0;
    v_stack_p110 = v_xmm0;
    v_stack_p120 = v_xmm0;
    v_stack_p130 = v_xmm0;
    v_stack_p140 = 0;
    v_stack_p110 = v_stack_p68;
    v_stack_p118 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m208))));
    v_stack_p128 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m208))));
    v_stack_p120 = v_stack_p160;
    v_stack_p30 = v_stack_pA0;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 23;
    a4 = 0;
    a3 = 0;
    result = CmpCallCallBacksEx(a4 + 23, v_stack_p110, a3, a4);
    goto loc_008B2F20;
loc_008B307A:
    if (((v_stack_p1E0) & (1)) == 0) goto loc_008B3196;
    result = ExFreeToLookasideListEx(v_rip + 5740977, v_stack_p110, a3, a4);
    goto loc_008B2F62;
loc_008B3099:
    result = EtwGetKernelTraceTimestamp(v_stack_p1B0, (unsigned int)(0x20000ULL), a3, a4);
    goto loc_008B2AD0;
loc_008B30B0:
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_008B2EAD;
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008B2EAD;
loc_008B30C6:
    goto loc_008B2F05;
loc_008B30D0:
    result = CmpIsRegistryLockAcquired(v_stack_p1B0, (unsigned int)(0x20000ULL), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_008B2DBA;
    v_stack_p160 = v_stack_p68;
    v_stack_p168 = v_stack_p50;
    v_stack_p170 = (unsigned int)((unsigned int)(a3));
    v_stack_p178 = 0;
    v_stack_p180 = (unsigned int)(v_rsi);
    v_stack_p188 = (unsigned int)(v_stack_p128);
    v_stack_p30 = v_stack_pA0;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 23;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 8, v_stack_p160, a3, 1);
    if (sign_flag) goto loc_008B31DB;
    v_stack_p41 = 1;
    goto loc_008B2DBA;
loc_008B3159:
    if (result == v_stack_p230) goto loc_008B2F80;
    result = CmSiFreeMemory(result, v_stack_p160, a3, 1);
    goto loc_008B2F80;
loc_008B3177:
    if (v_stack_p68 == 0) goto loc_008B2BA6;
    v_stack_p90 = *(unsigned __int64 *)(v_stack_p68 + 8);
    goto loc_008B2BA6;
loc_008B3196:
    result = CmSiFreeMemory(v_stack_p1D8, v_stack_p160, a3, 1);
    goto loc_008B2F62;
loc_008B31A8:
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p68 + 8);
    result = guard_dispatch_icall(16, v_stack_p1B0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p128))), (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_008B2F72;
loc_008B31D1:
    goto loc_008B2F05;
loc_008B31DB:
    v_rdi = 0;
    if (((unsigned int)(result)) != 0xC0000503ULL) { v_rdi = (unsigned int)(result); }
    goto loc_008B30C6;
loc_008B31EA:
    result = ObfDereferenceObject(16, v_stack_p1B0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p128))), (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_008B2F16;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryValueKey(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m170;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m260;
    uint16_t v_stack_m266;
    uint64_t v_stack_m268;
    uint8_t v_stack_m276;
    uint8_t v_stack_m277;
    uint8_t v_stack_m278;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m48;
    uint64_t v_stack_m88;
    uint64_t v_stack_mD7;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p110;
    uint32_t v_stack_p118;
    uint64_t v_stack_p120;
    uint32_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p140;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint32_t v_stack_p170;
    uint64_t v_stack_p178;
    uint32_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1D8;
    uint8_t v_stack_p1E0;
    uint32_t v_stack_p20;
    uint64_t v_stack_p230;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint64_t v_stack_p50;
    uint64_t v_stack_p68;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;

    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x557D26)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m240 = Arg6;
    v_stack_m230 = Arg3;
    result = 0;
    v_stack_m170 = v_xmm0;
    v_stack_m160 = 0;
    v_stack_m268 = v_xmm0;
    local_rbx = 0;
    v_stack_m1C8 = 0;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, result + 88, Arg4);
    result = 0;
    v_stack_m208 = v_xmm0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm0;
    v_stack_m228 = 0;
    if ((*(uint64_t *)(v_rip + 0x72553E)) != 0) goto loc_008B3099;
loc_008B2AD0:
    v_stack_m277 = 0;
    v_stack_m276 = 0;
    v_stack_m250 = 0;
    v_stack_m238 = 0;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m268, Arg2, result + 88, Arg4);
    v_stack_m248 = 0;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, Arg2 + 72, Arg4);
    v_stack_m210 = v_stack_m218;
    v_stack_m218 = v_stack_m218;
    result = CmpInitializeThreadInfo(v_stack_m170, Arg2, Arg2 + 72, Arg4);
    v_stack_m220 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m170, Arg2, Arg2 + 72, Arg4);
    v_stack_m278 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_008B31D1;
    v_stack_m290 = 0;
    v_stack_m298 = v_stack_m250;
    result = CmObReferenceObjectByHandle(Arg1, 1, Arg2 + 72, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    v_stack_m258 = (uint32_t)(result);
    if (sign_flag) goto loc_008B30C6;
    if ((*(uint64_t *)(v_rip + 0x725468)) != 0) goto loc_008B3177;
loc_008B2BA6:
    if (((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) == 1) goto loc_008B2C86;
    v_stack_m268 = v_xmm0;
loc_008B2BC5:
    v_stack_m266 = (uint16_t)(v_stack_m268);
    if ((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 0) goto loc_008B2BEF;
    if ((*(uint64_t *)(v_rip + 0x64462C)) == 0) goto loc_008B2C30;
    if (v_stack_m260 > result) goto loc_008B2C30;
loc_008B2BEF:
    if ((uint16_t)(v_stack_m268) == 0) goto loc_008B2C5F;
    if (((uint32_t)(v_stack_m268)) > 64) goto loc_008B2C66;
    v_stack_m248 = v_stack_m88;
loc_008B2C06:
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        Arg3 = (uint16_t)(v_stack_m268);
        Arg2 = v_stack_m260;
        Arg1 = v_stack_m248;
        result = memcpy(Arg1, Arg2, Arg3, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
        Arg2 = v_stack_m268;
    }
    v_stack_m260 = v_stack_m248;
loc_008B2C30:
    if ((((uint8_t)(Arg2)) & (1)) != 0) goto loc_008B2D46;
loc_008B2C39:
    if ((uint16_t)(Arg2) == 0) goto loc_008B2D67;
    Arg1 = ((uint32_t)((uint32_t)((uint16_t)(Arg2)))) >> (1);
    if ((*(uint16_t *)(v_stack_m260 + Arg1 * 2 - 0x2)) == 0) goto loc_008B2D59;
    goto loc_008B2D67;
loc_008B2C5F:
    v_stack_m248 = 0;
    goto loc_008B2C26;
loc_008B2C66:
    result = CmpAllocateTransientPoolWithQuota(Arg1, (uint16_t)(Arg2), (uint32_t)(0x6E764D43ULL), (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    v_stack_m248 = result;
    if (result == 0) goto loc_008B2D33;
    goto loc_008B2C06;
loc_008B2C86:
    v_stack_m1B8 = v_xmm0;
    Arg1 = v_stack_m268;
    if (((uint32_t)(Arg5)) < v_stack_m268) { Arg1 = (uint32_t)(Arg5); }
    v_stack_m1B8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_m1B0 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m268 = v_xmm0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_008B2CED;
    if ((((uint8_t)(*(uint64_t *)(Arg1 + 0x8))) & (1)) != 0) goto loc_008B2D25;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) > v_stack_m268) goto loc_008B2D2A;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_008B2D2A;
loc_008B2CED:
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_008B2D0D;
loc_008B2CF8:
    Arg2 = v_stack_m268;
    if (v_stack_m240 < v_stack_m268) { Arg2 = v_stack_m240; }
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    goto loc_008B2BC5;
loc_008B2D0D:
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_008B2D2E;
    if ((Arg4 + (uint32_t)(Arg5) * 1) > Arg2) goto loc_008B2D21;
    if ((Arg4 + (uint32_t)(Arg5) * 1) >= Arg4) goto loc_008B2CF8;
loc_008B2D21:
    goto loc_008B2CF8;
loc_008B2D25:
    result = ExRaiseDatatypeMisalignment(Arg4 + (uint32_t)(Arg5) * 1, Arg2, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
loc_008B2D2A:
    goto loc_008B2CED;
loc_008B2D2E:
    result = ExRaiseDatatypeMisalignment(Arg4 + (uint32_t)(Arg5) * 1, Arg2, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
loc_008B2D33:
    v_stack_m258 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_008B2F05;
loc_008B2D46:
    v_stack_m258 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008B2F05;
loc_008B2D59:
    Arg2 = (uint16_t)((Arg2) - (2));
    v_stack_m268 = (uint16_t)(Arg2);
    goto loc_008B2C39;
loc_008B2D67:
    goto loc_008B2D97;
loc_008B2D97:
    v_stack_m276 = 1;
    if ((*(uint32_t *)(v_rip + 0x63CDD4)) != 0) goto loc_008B30D0;
loc_008B2DBA:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m250, (uint8_t)(v_stack_m278), 1, v_stack_m220);
    if (sign_flag) goto loc_008B30C6;
    v_stack_m298 = 3;
    result = CmpBounceContextStart(v_stack_mE8, Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), (uint32_t)((uint32_t)(v_stack_m278)));
    if (sign_flag) goto loc_008B30C6;
    v_stack_m208 = 0;
    v_stack_m1E4 = 0;
    v_stack_m1D4 = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m1E0 = v_stack_mE0;
    v_stack_m1D8 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m1D0 = v_stack_m238;
    v_stack_m200 = v_stack_m250;
    result = KeExpandKernelStackAndCallout(v_rip + 1470179, v_stack_m208, (uint32_t)(0x4800ULL), (uint32_t)((uint32_t)(v_stack_m278)));
    if (sign_flag) goto loc_008B30C6;
    if (sign_flag) goto loc_008B30B0;
loc_008B2EAD:
    *(uint32_t *)(v_stack_m240) = (uint32_t)((uint32_t)(v_stack_m238));
    if (((uint32_t)((uint32_t)(v_stack_m208))) == 0xC0000023ULL) goto loc_008B2EE5;
    local_rsi = (uint32_t)(Arg5);
    if (((uint32_t)((uint32_t)(v_stack_m238))) < ((uint32_t)((uint32_t)(Arg5)))) { local_rsi = (uint32_t)((uint32_t)(v_stack_m238)); }
    result = (uint32_t)(v_stack_m208);
    if (v_stack_mE8 != v_stack_mE0) {
        Arg3 = (uint32_t)(local_rsi);
        result = memcpy(v_stack_mE8, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    }
    goto loc_008B2F05;
loc_008B2F05:
    if (v_stack_m220 != 0) goto loc_008B31EA;
loc_008B2F16:
    if (v_stack_m277 != 0) goto loc_008B2FBD;
loc_008B2F20:
    if (v_stack_m276 != 0) {
        result = KeLeaveCriticalRegion(v_stack_m220, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    }
    if (v_stack_m250 != 0) {
        result = ObfDereferenceObject(v_stack_m250, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    }
    if (v_stack_mE0 == 0) goto loc_008B2F62;
    if (v_stack_mE0 == v_stack_mE8) goto loc_008B2F62;
    if (v_stack_mE0 != v_stack_mD7) goto loc_008B307A;
loc_008B2F62:
    if (*(uint64_t *)(v_rip + 0x72509F) != 0) goto loc_008B31A8;
loc_008B2F72:
    if (v_stack_m248 != 0) goto loc_008B3159;
loc_008B2F80:
    result = v_stack_m248;
    if ((uint8_t)(v_stack_m278) != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m250, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    }
    result = CmCleanupThreadInfo(v_stack_m170, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    local_rsp = (local_rsp) + (640);
    return result;
loc_008B2FBD:
    if ((*(uint32_t *)(v_rip + 0x63CBC4)) == 0) goto loc_008B2F20;
    result = CmpIsRegistryLockAcquired(Arg1, v_stack_mE0, Arg3, (uint32_t)((uint32_t)(v_stack_m278)));
    if ((uint32_t)(result) != 0) goto loc_008B2F20;
    if (v_stack_pA0 == v_stack_pA0) goto loc_008B2F20;
    result = 0;
    v_stack_p110 = v_xmm0;
    v_stack_p120 = v_xmm0;
    v_stack_p130 = v_xmm0;
    v_stack_p140 = 0;
    v_stack_p110 = v_stack_p68;
    v_stack_p118 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m208))));
    v_stack_p128 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m208))));
    v_stack_p120 = v_stack_p160;
    v_stack_p30 = v_stack_pA0;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 23;
    Arg4 = 0;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg4 + 23, v_stack_p110, Arg3, Arg4);
    goto loc_008B2F20;
loc_008B307A:
    if (((v_stack_p1E0) & (1)) == 0) goto loc_008B3196;
    result = ExFreeToLookasideListEx(v_rip + 5740977, v_stack_p110, Arg3, Arg4);
    goto loc_008B2F62;
loc_008B3099:
    result = EtwGetKernelTraceTimestamp(v_stack_p1B0, (uint32_t)(0x20000ULL), Arg3, Arg4);
    goto loc_008B2AD0;
loc_008B30B0:
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_008B2EAD;
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008B2EAD;
loc_008B30C6:
    goto loc_008B2F05;
loc_008B30D0:
    result = CmpIsRegistryLockAcquired(v_stack_p1B0, (uint32_t)(0x20000ULL), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_008B2DBA;
    v_stack_p160 = v_stack_p68;
    v_stack_p168 = v_stack_p50;
    v_stack_p170 = (uint32_t)((uint32_t)(Arg3));
    v_stack_p178 = 0;
    v_stack_p180 = (uint32_t)(local_rsi);
    v_stack_p188 = (uint32_t)(v_stack_p128);
    v_stack_p30 = v_stack_pA0;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = 23;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 8, v_stack_p160, Arg3, 1);
    if (sign_flag) goto loc_008B31DB;
    v_stack_p41 = 1;
    goto loc_008B2DBA;
loc_008B3159:
    if (result == v_stack_p230) goto loc_008B2F80;
    result = CmSiFreeMemory(result, v_stack_p160, Arg3, 1);
    goto loc_008B2F80;
loc_008B3177:
    if (v_stack_p68 == 0) goto loc_008B2BA6;
    v_stack_p90 = *(uint64_t *)(v_stack_p68 + 0x8);
    goto loc_008B2BA6;
loc_008B3196:
    result = CmSiFreeMemory(v_stack_p1D8, v_stack_p160, Arg3, 1);
    goto loc_008B2F62;
loc_008B31A8:
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = *(uint64_t *)(v_stack_p68 + 0x8);
    result = guard_dispatch_icall(16, v_stack_p1B0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p128))), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_008B2F72;
loc_008B31D1:
    goto loc_008B2F05;
loc_008B31DB:
    local_rdi = 0;
    if (((uint32_t)(result)) != 0xC0000503ULL) { local_rdi = (uint32_t)(result); }
    goto loc_008B30C6;
loc_008B31EA:
    result = ObfDereferenceObject(16, v_stack_p1B0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p128))), (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_008B2F16;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B2A00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
