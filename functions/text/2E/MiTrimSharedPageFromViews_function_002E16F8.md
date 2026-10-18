# MiTrimSharedPageFromViews

- RVA: `0x002E16F8`–`0x002E22BB` (길이 `3,011` bytes)
- VA: `0x00000001402E16F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070D04`
- 디코드: `746`개 명령, `3,011/3,011` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **63**; 고유 호출 대상: **46**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002E1763` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002E1813` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002E1825` → [MiPrepareAttachThread](../2B/MiPrepareAttachThread_function_002B4650.md) (function, `0x002B4650`)
- `0x002E1839` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002E1853` → [KeForceAttachProcess](../21/KeForceAttachProcess_function_00216650.md) (function, `0x00216650`)
- `0x002E1890` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002E18BC` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x002E1924` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x002E1930` → [KeAbPostRelease](KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002E1953` → [KiCheckForKernelApcDelivery](KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002E19C0` → [Feature_Servicing_Mm_TrimSharedPageFix__private_IsEnabledDeviceUsageNoInline](../67/Feature_Servicing_Mm_TrimSharedPageFix__private_IsEnabledDeviceUsageNoInline_function_0067F190.md) (function, `0x0067F190`)
- `0x002E1A50` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002E1A7D` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002E1A91` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002E1AA6` → [MiUnlockSystemVa](../34/MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x002E1AB8` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002E1AC4` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002E1AF5` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x002E1AFF` → [MiSystemVaTypeHasWsles](../34/MiSystemVaTypeHasWsles_function_0034B2C4.md) (function, `0x0034B2C4`)
- `0x002E1B0F` → [MiSystemVaTypeToVm](../28/MiSystemVaTypeToVm_function_0028EB50.md) (function, `0x0028EB50`)
- `0x002E1B32` → [MiSynchronizeSystemVa](../28/MiSynchronizeSystemVa_function_0028ECB8.md) (function, `0x0028ECB8`)
- `0x002E1B5C` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002E1B80` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x002E1BB8` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x002E1BC9` → [MiGetSystemCacheReverseMap](../29/MiGetSystemCacheReverseMap_function_00294BF0.md) (function, `0x00294BF0`)
- `0x002E1BDD` → [MiGetMultiplexedVm](../34/MiGetMultiplexedVm_function_003479B0.md) (function, `0x003479B0`)
- `0x002E1C5B` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002E1C7C` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002E1CA0` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x002E1CAA` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x002E1CB2` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x002E1D74` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x002E1D96` → [MiStartingOffset](../34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x002E1DAC` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x002E1E1F` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x002E1F01` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x002E1F32` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x002E1F50` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002E1F64` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x002E1F82` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x002E1FB2` → [MiVmAccessLoggingEnabled](../36/MiVmAccessLoggingEnabled_function_003629D4.md) (function, `0x003629D4`)
- `0x002E1FC1` → [MI_WSLE_LOG_ACCESS](../29/MI_WSLE_LOG_ACCESS_function_00294400.md) (function, `0x00294400`)
- `0x002E1FE0` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002E200F` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x002E2020` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x002E2049` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002E20B0` → [MiReplaceLockedPage](../38/MiReplaceLockedPage_function_0038351C.md) (function, `0x0038351C`)
- `0x002E20F0` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x002E2125` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002E2152` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002E2166` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002E217E` → [MiUnlockSystemVa](../34/MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x002E2195` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002E21A1` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002E21E1` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x002E21ED` → [KeAbPostRelease](KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002E220E` → [KiCheckForKernelApcDelivery](KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002E2222` → [KeForceDetachProcess](../3C/KeForceDetachProcess_function_003C7770.md) (function, `0x003C7770`)
- `0x002E222E` → [MiAttachThreadDone](../28/MiAttachThreadDone_function_0028F3E0.md) (function, `0x0028F3E0`)
- `0x002E2240` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x002E224B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002E2284` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002E22B2` → [MiDeleteTrimViewInfoList](../../page/A6/MiDeleteTrimViewInfoList_function_00A610A4.md) (function, `0x00A610A4`)

### Direct callers
- [sub_002E087E](Unknown_function_002E087E.md) at `0x002E0AE7`

### Static image references
- `0x002E1717` → RVA `0x00E0A740` (`.data`; read)
- `0x002E180C` → RVA `0x00E374C0` (`.data`; read)
- `0x002E1883` → RVA `0x00E36040` (`.data`; read)
- `0x002E18D7` → RVA `0x00E36048` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002E224B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002E22B2` → [MiDeleteTrimViewInfoList](../../page/A6/MiDeleteTrimViewInfoList_function_00A610A4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E16F8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002E16FD  55                              push rbp
002E16FE  56                              push rsi
002E16FF  57                              push rdi
002E1700  41 54                           push r12
002E1702  41 55                           push r13
002E1704  41 56                           push r14
002E1706  41 57                           push r15
002E1708  48 8D AC 24 60 FF FF FF         lea rbp, [rsp - 0xa0]
002E1710  48 81 EC A0 01 00 00            sub rsp, 0x1a0
002E1717  48 8B 05 22 90 B2 00            mov rax, qword ptr [rip + 0xb29022]
002E171E  48 33 C4                        xor rax, rsp
002E1721  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
002E1728  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
002E172F  0F 57 C0                        xorps xmm0, xmm0
002E1732  41 8B F8                        mov edi, r8d
002E1735  44 89 45 AC                     mov dword ptr [rbp - 0x54], r8d
002E1739  89 55 88                        mov dword ptr [rbp - 0x78], edx
002E173C  48 8B D9                        mov rbx, rcx
002E173F  33 D2                           xor edx, edx
002E1741  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002E1745  41 B8 80 00 00 00               mov r8d, 0x80
002E174B  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
002E1750  48 8D 4D E0                     lea rcx, [rbp - 0x20]
002E1754  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
002E1758  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
002E175C  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
002E1763  E8 D8 54 3E 00                  call 0x1406c6c40
002E1768  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
002E1771  45 33 C9                        xor r9d, r9d
002E1774  C6 44 24 30 11                  mov byte ptr [rsp + 0x30], 0x11
002E1779  41 8B C1                        mov eax, r9d
002E177C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002E1780  45 8B E9                        mov r13d, r9d
002E1783  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
002E1788  45 8B E1                        mov r12d, r9d
002E178B  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
002E1790  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
002E1795  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
002E1799  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
002E179E  48 85 DB                        test rbx, rbx
002E17A1  0F 84 D3 0A 00 00               je 0x1402e227a
002E17A7  45 8D 59 01                     lea r11d, [r9 + 1]
002E17AB  4C 8B C3                        mov r8, rbx
002E17AE  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
002E17B2  48 8B 1B                        mov rbx, qword ptr [rbx]
002E17B5  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
002E17B9  44 89 4D 84                     mov dword ptr [rbp - 0x7c], r9d
002E17BD  49 8B 48 18                     mov rcx, qword ptr [r8 + 0x18]
002E17C1  49 8B 58 08                     mov rbx, qword ptr [r8 + 8]
002E17C5  4C 8B F1                        mov r14, rcx
002E17C8  4D 8B 78 10                     mov r15, qword ptr [r8 + 0x10]
002E17CC  49 8B 50 20                     mov rdx, qword ptr [r8 + 0x20]
002E17D0  49 8B C7                        mov rax, r15
002E17D3  48 C1 E8 0C                     shr rax, 0xc
002E17D7  49 C1 EE 0C                     shr r14, 0xc
002E17DB  4C 2B F0                        sub r14, rax
002E17DE  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
002E17E3  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
002E17E7  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002E17EC  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
002E17F1  44 89 4D 80                     mov dword ptr [rbp - 0x80], r9d
002E17F5  48 85 DB                        test rbx, rbx
002E17F8  74 63                           je 0x1402e185d
002E17FA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002E1803  48 3B 98 B8 00 00 00            cmp rbx, qword ptr [rax + 0xb8]
002E180A  74 51                           je 0x1402e185d
002E180C  48 8D 0D AD 5C B5 00            lea rcx, [rip + 0xb55cad]
002E1813  E8 78 6E F6 FF                  call 0x140248690
002E1818  48 8D 93 00 04 00 00            lea rdx, [rbx + 0x400]
002E181F  48 8B CB                        mov rcx, rbx
002E1822  44 8A C8                        mov r9b, al
002E1825  E8 26 2E FD FF                  call 0x1402b4650
002E182A  41 8A D1                        mov dl, r9b
002E182D  89 45 84                        mov dword ptr [rbp - 0x7c], eax
002E1830  48 8D 0D 89 5C B5 00            lea rcx, [rip + 0xb55c89]
002E1837  8B F0                           mov esi, eax
002E1839  E8 82 6A F6 FF                  call 0x1402482c0
002E183E  45 33 C9                        xor r9d, r9d
002E1841  85 F6                           test esi, esi
002E1843  0F 84 B4 08 00 00               je 0x1402e20fd
002E1849  45 33 C0                        xor r8d, r8d
002E184C  48 8D 55 60                     lea rdx, [rbp + 0x60]
002E1850  48 8B CB                        mov rcx, rbx
002E1853  E8 F8 4D F3 FF                  call 0x140216650
002E1858  E9 3C 01 00 00                  jmp 0x1402e1999
002E185D  41 8B 40 28                     mov eax, dword ptr [r8 + 0x28]
002E1861  A9 FC FF FF FF                  test eax, 0xfffffffc
002E1866  75 09                           jne 0x1402e1871
002E1868  83 F8 02                        cmp eax, 2
002E186B  0F 85 2D 01 00 00               jne 0x1402e199e
002E1871  40 F6 C7 06                     test dil, 6
002E1875  0F 85 82 08 00 00               jne 0x1402e20fd
002E187B  66 44 29 9E E6 01 00 00         sub word ptr [rsi + 0x1e6], r11w
002E1883  48 8D 0D B6 47 B5 00            lea rcx, [rip + 0xb547b6]
002E188A  45 33 C0                        xor r8d, r8d
002E188D  33 D2                           xor edx, edx
002E188F  90                              nop
002E1890  E8 9B E9 F2 FF                  call 0x140210230
002E1895  48 8B D8                        mov rbx, rax
002E1898  33 C0                           xor eax, eax
002E189A  44 8D 50 11                     lea r10d, [rax + 0x11]
002E189E  F0 4C 0F B1 15 99 47 B5 00      lock cmpxchg qword ptr [rip + 0xb54799], r10
002E18A7  74 1E                           je 0x1402e18c7
002E18A9  4C 8D 0D 90 47 B5 00            lea r9, [rip + 0xb54790]
002E18B0  4C 8B C3                        mov r8, rbx
002E18B3  33 D2                           xor edx, edx
002E18B5  48 8D 0D 84 47 B5 00            lea rcx, [rip + 0xb54784]
002E18BC  E8 8B EB F2 FF                  call 0x14021044c
002E18C1  41 BA 11 00 00 00               mov r10d, 0x11
002E18C7  45 33 C9                        xor r9d, r9d
002E18CA  45 8D 59 01                     lea r11d, [r9 + 1]
002E18CE  48 85 DB                        test rbx, rbx
002E18D1  74 04                           je 0x1402e18d7
002E18D3  44 88 5B 0A                     mov byte ptr [rbx + 0xa], r11b
002E18D7  48 8B 15 6A 47 B5 00            mov rdx, qword ptr [rip + 0xb5476a]
002E18DE  EB 25                           jmp 0x1402e1905
002E18E0  4C 8B 42 58                     mov r8, qword ptr [rdx + 0x58]
002E18E4  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
002E18E8  49 81 E0 00 F0 FF FF            and r8, 0xfffffffffffff000
002E18EF  49 03 C8                        add rcx, r8
002E18F2  4C 3B F9                        cmp r15, rcx
002E18F5  72 06                           jb 0x1402e18fd
002E18F7  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
002E18FB  EB 08                           jmp 0x1402e1905
002E18FD  4D 3B F8                        cmp r15, r8
002E1900  73 08                           jae 0x1402e190a
002E1902  48 8B 12                        mov rdx, qword ptr [rdx]
002E1905  48 85 D2                        test rdx, rdx
002E1908  75 D6                           jne 0x1402e18e0
002E190A  48 85 D2                        test rdx, rdx
002E190D  75 51                           jne 0x1402e1960
002E190F  49 8B C2                        mov rax, r10
002E1912  F0 4C 0F B1 0D 25 47 B5 00      lock cmpxchg qword ptr [rip + 0xb54725], r9
002E191B  74 0C                           je 0x1402e1929
002E191D  48 8D 0D 1C 47 B5 00            lea rcx, [rip + 0xb5471c]
002E1924  E8 17 1B F8 FF                  call 0x140263440
002E1929  48 8D 0D 10 47 B5 00            lea rcx, [rip + 0xb54710]
002E1930  E8 CB FC FF FF                  call 0x1402e1600
002E1935  41 BE 01 00 00 00               mov r14d, 1
002E193B  90                              nop
002E193C  66 44 01 B6 E6 01 00 00         add word ptr [rsi + 0x1e6], r14w
002E1944  75 12                           jne 0x1402e1958
002E1946  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
002E194D  90                              nop
002E194E  48 39 00                        cmp qword ptr [rax], rax
002E1951  74 05                           je 0x1402e1958
002E1953  E8 28 13 00 00                  call 0x1402e2c80
002E1958  45 33 C9                        xor r9d, r9d
002E195B  E9 A3 07 00 00                  jmp 0x1402e2103
002E1960  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
002E1964  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002E1969  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002E196D  48 39 08                        cmp qword ptr [rax], rcx
002E1970  75 9D                           jne 0x1402e190f
002E1972  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
002E1976  48 8B 42 58                     mov rax, qword ptr [rdx + 0x58]
002E197A  48 C1 E1 0C                     shl rcx, 0xc
002E197E  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
002E1984  48 2B 4C 24 48                  sub rcx, qword ptr [rsp + 0x48]
002E1989  49 03 CF                        add rcx, r15
002E198C  48 3B C8                        cmp rcx, rax
002E198F  0F 85 7A FF FF FF               jne 0x1402e190f
002E1995  44 89 5D 80                     mov dword ptr [rbp - 0x80], r11d
002E1999  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E199E  48 81 EA 00 10 00 00            sub rdx, 0x1000
002E19A5  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
002E19AA  49 81 EF 00 10 00 00            sub r15, 0x1000
002E19B1  EB 0A                           jmp 0x1402e19bd
002E19B3  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E19B8  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
002E19BD  48 8B F2                        mov rsi, rdx
002E19C0  E8 CB D7 39 00                  call 0x14067f190
002E19C5  45 33 C9                        xor r9d, r9d
002E19C8  85 C0                           test eax, eax
002E19CA  75 13                           jne 0x1402e19df
002E19CC  49 81 C7 00 10 00 00            add r15, 0x1000
002E19D3  4C 3B 7D C8                     cmp r15, qword ptr [rbp - 0x38]
002E19D7  0F 83 20 07 00 00               jae 0x1402e20fd
002E19DD  EB 18                           jmp 0x1402e19f7
002E19DF  4D 85 F6                        test r14, r14
002E19E2  0F 84 15 07 00 00               je 0x1402e20fd
002E19E8  49 FF CE                        dec r14
002E19EB  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002E19F0  49 81 C7 00 10 00 00            add r15, 0x1000
002E19F7  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
002E19FC  48 81 C3 00 10 00 00            add rbx, 0x1000
002E1A03  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
002E1A08  4D 85 ED                        test r13, r13
002E1A0B  0F 84 C3 00 00 00               je 0x1402e1ad4
002E1A11  49 8B CF                        mov rcx, r15
002E1A14  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
002E1A1E  48 C1 E9 12                     shr rcx, 0x12
002E1A22  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
002E1A28  48 8B C0                        mov rax, rax
002E1A2B  48 03 C8                        add rcx, rax
002E1A2E  49 3B CC                        cmp rcx, r12
002E1A31  0F 84 9D 00 00 00               je 0x1402e1ad4
002E1A37  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002E1A3C  48 85 C0                        test rax, rax
002E1A3F  74 2F                           je 0x1402e1a70
002E1A41  44 39 48 1C                     cmp dword ptr [rax + 0x1c], r9d
002E1A45  74 24                           je 0x1402e1a6b
002E1A47  45 33 C0                        xor r8d, r8d
002E1A4A  48 8B D0                        mov rdx, rax
002E1A4D  49 8B CD                        mov rcx, r13
002E1A50  E8 13 F7 F5 FF                  call 0x140241168
002E1A55  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
002E1A59  45 33 C9                        xor r9d, r9d
002E1A5C  48 85 C0                        test rax, rax
002E1A5F  B8 15 01 00 00                  mov eax, 0x115
002E1A64  0F 45 C8                        cmovne ecx, eax
002E1A67  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
002E1A6B  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
002E1A70  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002E1A75  48 85 C0                        test rax, rax
002E1A78  74 10                           je 0x1402e1a8a
002E1A7A  48 8B C8                        mov rcx, rax
002E1A7D  E8 3E 05 03 00                  call 0x140311fc0
002E1A82  45 33 C9                        xor r9d, r9d
002E1A85  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
002E1A8A  4C 39 4C 24 58                  cmp qword ptr [rsp + 0x58], r9
002E1A8F  74 0A                           je 0x1402e1a9b
002E1A91  E8 DA 21 03 00                  call 0x140313c70
002E1A96  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
002E1A9B  4C 39 4C 24 78                  cmp qword ptr [rsp + 0x78], r9
002E1AA0  75 0B                           jne 0x1402e1aad
002E1AA2  48 8D 4D E0                     lea rcx, [rbp - 0x20]
002E1AA6  E8 55 9D 06 00                  call 0x14034b800
002E1AAB  EB 1C                           jmp 0x1402e1ac9
002E1AAD  4D 85 E4                        test r12, r12
002E1AB0  74 0B                           je 0x1402e1abd
002E1AB2  49 8B D4                        mov rdx, r12
002E1AB5  49 8B CD                        mov rcx, r13
002E1AB8  E8 03 54 F3 FF                  call 0x140216ec0
002E1ABD  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
002E1AC1  49 8B CD                        mov rcx, r13
002E1AC4  E8 C7 BB F9 FF                  call 0x14027d690
002E1AC9  45 33 C9                        xor r9d, r9d
002E1ACC  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
002E1AD1  45 8B E9                        mov r13d, r9d
002E1AD4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
002E1AD9  48 85 C0                        test rax, rax
002E1ADC  0F 85 67 01 00 00               jne 0x1402e1c49
002E1AE2  44 8D 70 01                     lea r14d, [rax + 1]
002E1AE6  45 8B E6                        mov r12d, r14d
002E1AE9  4D 85 ED                        test r13, r13
002E1AEC  0F 85 B5 00 00 00               jne 0x1402e1ba7
002E1AF2  49 8B CF                        mov rcx, r15
002E1AF5  E8 86 D1 FA FF                  call 0x14028ec80
002E1AFA  8B C8                           mov ecx, eax
002E1AFC  44 8B D0                        mov r10d, eax
002E1AFF  E8 C0 97 06 00                  call 0x14034b2c4
002E1B04  45 33 C9                        xor r9d, r9d
002E1B07  85 C0                           test eax, eax
002E1B09  0F 84 A7 06 00 00               je 0x1402e21b6
002E1B0F  E8 3C D0 FA FF                  call 0x14028eb50
002E1B14  4C 8B E8                        mov r13, rax
002E1B17  48 85 C0                        test rax, rax
002E1B1A  0F 84 96 06 00 00               je 0x1402e21b6
002E1B20  48 8D 45 E0                     lea rax, [rbp - 0x20]
002E1B24  45 8B C2                        mov r8d, r10d
002E1B27  49 8B D7                        mov rdx, r15
002E1B2A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002E1B2F  49 8B CD                        mov rcx, r13
002E1B32  E8 81 D1 FA FF                  call 0x14028ecb8
002E1B37  45 33 C9                        xor r9d, r9d
002E1B3A  85 C0                           test eax, eax
002E1B3C  0F 84 CA 05 00 00               je 0x1402e210c
002E1B42  4C 8B 6D F8                     mov r13, qword ptr [rbp - 8]
002E1B46  41 84 FE                        test r14b, dil
002E1B49  74 3A                           je 0x1402e1b85
002E1B4B  4C 39 4C 24 60                  cmp qword ptr [rsp + 0x60], r9
002E1B50  75 33                           jne 0x1402e1b85
002E1B52  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002E1B57  48 85 C0                        test rax, rax
002E1B5A  75 0A                           jne 0x1402e1b66
002E1B5C  E8 2F 11 F6 FF                  call 0x140242c90
002E1B61  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002E1B66  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
002E1B6A  45 33 C9                        xor r9d, r9d
002E1B6D  49 8B D5                        mov rdx, r13
002E1B70  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002E1B75  48 8B C8                        mov rcx, rax
002E1B78  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
002E1B80  E8 7B 33 FB FF                  call 0x140294f00
002E1B85  49 8B CF                        mov rcx, r15
002E1B88  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
002E1B92  48 C1 E9 12                     shr rcx, 0x12
002E1B96  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
002E1B9C  48 8B C0                        mov rax, rax
002E1B9F  48 03 C8                        add rcx, rax
002E1BA2  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002E1BA7  4C 8B 55 98                     mov r10, qword ptr [rbp - 0x68]
002E1BAB  45 39 4A 28                     cmp dword ptr [r10 + 0x28], r9d
002E1BAF  0F 85 5C 03 00 00               jne 0x1402e1f11
002E1BB5  49 8B CF                        mov rcx, r15
002E1BB8  E8 C3 D0 FA FF                  call 0x14028ec80
002E1BBD  83 F8 07                        cmp eax, 7
002E1BC0  0F 85 92 FD FF FF               jne 0x1402e1958
002E1BC6  49 8B CF                        mov rcx, r15
002E1BC9  E8 22 30 FB FF                  call 0x140294bf0
002E1BCE  4C 8B C8                        mov r9, rax
002E1BD1  48 85 C0                        test rax, rax
002E1BD4  0F 84 7E FD FF FF               je 0x1402e1958
002E1BDA  49 8B D7                        mov rdx, r15
002E1BDD  E8 CE 5D 06 00                  call 0x1403479b0
002E1BE2  4C 3B E8                        cmp r13, rax
002E1BE5  0F 85 6D FD FF FF               jne 0x1402e1958
002E1BEB  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
002E1BEF  48 C1 E8 3E                     shr rax, 0x3e
002E1BF3  3C 03                           cmp al, 3
002E1BF5  0F 85 5D FD FF FF               jne 0x1402e1958
002E1BFB  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
002E1BFF  4D 8B DC                        mov r11, r12
002E1C02  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002E1C06  41 84 C3                        test r11b, al
002E1C09  74 08                           je 0x1402e1c13
002E1C0B  48 83 E0 FE                     and rax, 0xfffffffffffffffe
002E1C0F  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002E1C13  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
002E1C18  4C 39 00                        cmp qword ptr [rax], r8
002E1C1B  0F 85 37 FD FF FF               jne 0x1402e1958
002E1C21  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
002E1C25  49 8B CF                        mov rcx, r15
002E1C28  48 25 00 00 FF FF               and rax, 0xffffffffffff0000
002E1C2E  81 E1 FF FF 03 00               and ecx, 0x3ffff
002E1C34  48 8B D3                        mov rdx, rbx
002E1C37  48 8D 0C 81                     lea rcx, [rcx + rax*4]
002E1C3B  48 3B CB                        cmp rcx, rbx
002E1C3E  0F 85 14 FD FF FF               jne 0x1402e1958
002E1C44  E9 F9 01 00 00                  jmp 0x1402e1e42
002E1C49  45 8B E1                        mov r12d, r9d
002E1C4C  4D 85 ED                        test r13, r13
002E1C4F  75 54                           jne 0x1402e1ca5
002E1C51  4C 8D A8 00 04 00 00            lea r13, [rax + 0x400]
002E1C58  49 8B CD                        mov rcx, r13
002E1C5B  E8 90 AF F9 FF                  call 0x14027cbf0
002E1C60  88 44 24 30                     mov byte ptr [rsp + 0x30], al
002E1C64  40 F6 C7 01                     test dil, 1
002E1C68  74 3B                           je 0x1402e1ca5
002E1C6A  48 83 7C 24 60 00               cmp qword ptr [rsp + 0x60], 0
002E1C70  75 33                           jne 0x1402e1ca5
002E1C72  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002E1C77  48 85 C0                        test rax, rax
002E1C7A  75 0A                           jne 0x1402e1c86
002E1C7C  E8 0F 10 F6 FF                  call 0x140242c90
002E1C81  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002E1C86  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
002E1C8A  45 33 C9                        xor r9d, r9d
002E1C8D  49 8B D5                        mov rdx, r13
002E1C90  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002E1C95  48 8B C8                        mov rcx, rax
002E1C98  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
002E1CA0  E8 5B 32 FB FF                  call 0x140294f00
002E1CA5  B9 01 00 00 00                  mov ecx, 1
002E1CAA  E8 41 A4 F9 FF                  call 0x14027c0f0
002E1CAF  49 8B CF                        mov rcx, r15
002E1CB2  E8 19 4C 03 00                  call 0x1403168d0
002E1CB7  48 8B C8                        mov rcx, rax
002E1CBA  48 85 C0                        test rax, rax
002E1CBD  0F 84 21 04 00 00               je 0x1402e20e4
002E1CC3  8B 40 30                        mov eax, dword ptr [rax + 0x30]
002E1CC6  0F BA E0 15                     bt eax, 0x15
002E1CCA  0F 82 14 04 00 00               jb 0x1402e20e4
002E1CD0  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
002E1CD5  41 8B 50 38                     mov edx, dword ptr [r8 + 0x38]
002E1CD9  83 E2 20                        and edx, 0x20
002E1CDC  75 08                           jne 0x1402e1ce6
002E1CDE  A8 70                           test al, 0x70
002E1CE0  0F 85 FE 03 00 00               jne 0x1402e20e4
002E1CE6  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
002E1CEA  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002E1CEE  4C 39 00                        cmp qword ptr [rax], r8
002E1CF1  0F 85 ED 03 00 00               jne 0x1402e20e4
002E1CF7  85 D2                           test edx, edx
002E1CF9  74 68                           je 0x1402e1d63
002E1CFB  4C 8B 41 50                     mov r8, qword ptr [rcx + 0x50]
002E1CFF  4C 8B 55 B8                     mov r10, qword ptr [rbp - 0x48]
002E1D03  4D 3B D0                        cmp r10, r8
002E1D06  0F 82 D8 03 00 00               jb 0x1402e20e4
002E1D0C  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
002E1D0F  0F B6 51 21                     movzx edx, byte ptr [rcx + 0x21]
002E1D13  44 0F B6 79 20                  movzx r15d, byte ptr [rcx + 0x20]
002E1D18  44 8B 49 18                     mov r9d, dword ptr [rcx + 0x18]
002E1D1C  48 C1 E2 20                     shl rdx, 0x20
002E1D20  48 0B D0                        or rdx, rax
002E1D23  41 8B C7                        mov eax, r15d
002E1D26  48 C1 E0 20                     shl rax, 0x20
002E1D2A  49 0B C1                        or rax, r9
002E1D2D  48 6B C0 F8                     imul rax, rax, -8
002E1D31  48 83 C0 08                     add rax, 8
002E1D35  49 03 C0                        add rax, r8
002E1D38  48 8D 04 D0                     lea rax, [rax + rdx*8]
002E1D3C  4C 3B D0                        cmp r10, rax
002E1D3F  0F 83 9F 03 00 00               jae 0x1402e20e4
002E1D45  49 C1 E7 20                     shl r15, 0x20
002E1D49  49 8B C2                        mov rax, r10
002E1D4C  49 2B C0                        sub rax, r8
002E1D4F  4D 0B F9                        or r15, r9
002E1D52  48 C1 F8 03                     sar rax, 3
002E1D56  48 C1 E0 0C                     shl rax, 0xc
002E1D5A  49 C1 E7 0C                     shl r15, 0xc
002E1D5E  4C 03 F8                        add r15, rax
002E1D61  EB 41                           jmp 0x1402e1da4
002E1D63  49 8B D7                        mov rdx, r15
002E1D66  4C 8D 4D 90                     lea r9, [rbp - 0x70]
002E1D6A  48 C1 EA 0C                     shr rdx, 0xc
002E1D6E  41 B8 08 00 00 00               mov r8d, 8
002E1D74  E8 F7 CB 04 00                  call 0x14032e970
002E1D79  48 85 C0                        test rax, rax
002E1D7C  0F 84 62 03 00 00               je 0x1402e20e4
002E1D82  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002E1D86  48 85 C9                        test rcx, rcx
002E1D89  0F 84 55 03 00 00               je 0x1402e20e4
002E1D8F  41 83 C8 FF                     or r8d, 0xffffffff
002E1D93  48 8B D0                        mov rdx, rax
002E1D96  E8 45 65 06 00                  call 0x1403482e0
002E1D9B  48 3B D8                        cmp rbx, rax
002E1D9E  0F 85 40 03 00 00               jne 0x1402e20e4
002E1DA4  BA 11 00 00 00                  mov edx, 0x11
002E1DA9  8D 4A F0                        lea ecx, [rdx - 0x10]
002E1DAC  E8 6F 52 FB FF                  call 0x140297020
002E1DB1  49 8B D7                        mov rdx, r15
002E1DB4  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
002E1DBE  48 C1 EA 09                     shr rdx, 9
002E1DC2  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
002E1DCC  49 23 D1                        and rdx, r9
002E1DCF  49 8B C0                        mov rax, r8
002E1DD2  48 03 D0                        add rdx, rax
002E1DD5  48 8B DA                        mov rbx, rdx
002E1DD8  48 C1 EB 09                     shr rbx, 9
002E1DDC  49 23 D9                        and rbx, r9
002E1DDF  49 8B C0                        mov rax, r8
002E1DE2  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002E1DE7  48 03 D8                        add rbx, rax
002E1DEA  48 3B CB                        cmp rcx, rbx
002E1DED  74 43                           je 0x1402e1e32
002E1DEF  48 85 C9                        test rcx, rcx
002E1DF2  74 21                           je 0x1402e1e15
002E1DF4  49 81 EF 00 10 00 00            sub r15, 0x1000
002E1DFB  48 8B D6                        mov rdx, rsi
002E1DFE  49 FF C6                        inc r14
002E1E01  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
002E1E06  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002E1E0B  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E1E10  E9 A8 FB FF FF                  jmp 0x1402e19bd
002E1E15  45 33 C9                        xor r9d, r9d
002E1E18  4C 8D 45 D0                     lea r8, [rbp - 0x30]
002E1E1C  49 8B CD                        mov rcx, r13
002E1E1F  E8 EC EE F9 FF                  call 0x140280d10
002E1E24  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002E1E29  48 3B C3                        cmp rax, rbx
002E1E2C  0F 85 C8 02 00 00               jne 0x1402e20fa
002E1E32  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
002E1E37  41 BB 01 00 00 00               mov r11d, 1
002E1E3D  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E1E42  4C 8B 55 98                     mov r10, qword ptr [rbp - 0x68]
002E1E46  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002E1E50  4D 8B F7                        mov r14, r15
002E1E53  49 C1 EE 09                     shr r14, 9
002E1E57  4C 23 F0                        and r14, rax
002E1E5A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002E1E64  48 8B C0                        mov rax, rax
002E1E67  4C 03 F0                        add r14, rax
002E1E6A  49 8B 1E                        mov rbx, qword ptr [r14]
002E1E6D  41 84 DB                        test r11b, bl
002E1E70  0F 84 3D FB FF FF               je 0x1402e19b3
002E1E76  48 8B C3                        mov rax, rbx
002E1E79  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002E1E83  48 C1 E8 0C                     shr rax, 0xc
002E1E87  48 23 C1                        and rax, rcx
002E1E8A  48 8D 34 40                     lea rsi, [rax + rax*2]
002E1E8E  48 C1 E6 04                     shl rsi, 4
002E1E92  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002E1E9C  48 03 F0                        add rsi, rax
002E1E9F  40 F6 C7 08                     test dil, 8
002E1EA3  74 13                           je 0x1402e1eb8
002E1EA5  F6 C3 42                        test bl, 0x42
002E1EA8  0F 85 05 FB FF FF               jne 0x1402e19b3
002E1EAE  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
002E1EB2  0F 85 FB FA FF FF               jne 0x1402e19b3
002E1EB8  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002E1EBC  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
002E1EC0  48 85 C0                        test rax, rax
002E1EC3  0F 89 EA FA FF FF               jns 0x1402e19b3
002E1EC9  81 E1 00 04 00 00               and ecx, 0x400
002E1ECF  41 84 FB                        test r11b, dil
002E1ED2  0F 84 96 00 00 00               je 0x1402e1f6e
002E1ED8  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E1EDD  48 85 C9                        test rcx, rcx
002E1EE0  0F 84 D2 FA FF FF               je 0x1402e19b8
002E1EE6  F6 C3 42                        test bl, 0x42
002E1EE9  0F 84 C9 FA FF FF               je 0x1402e19b8
002E1EEF  33 FF                           xor edi, edi
002E1EF1  89 7D A8                        mov dword ptr [rbp - 0x58], edi
002E1EF4  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
002E1EFB  73 24                           jae 0x1402e1f21
002E1EFD  48 8D 4D A8                     lea rcx, [rbp - 0x58]
002E1F01  E8 FA 9D 11 00                  call 0x1403fbd00
002E1F06  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002E1F0A  48 85 C0                        test rax, rax
002E1F0D  78 EE                           js 0x1402e1efd
002E1F0F  EB E3                           jmp 0x1402e1ef4
002E1F11  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
002E1F16  48 8B D3                        mov rdx, rbx
002E1F19  4D 8B DC                        mov r11, r12
002E1F1C  E9 25 FF FF FF                  jmp 0x1402e1e46
002E1F21  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
002E1F25  8B 7D AC                        mov edi, dword ptr [rbp - 0x54]
002E1F28  75 0D                           jne 0x1402e1f37
002E1F2A  BA 01 00 00 00                  mov edx, 1
002E1F2F  48 8B CE                        mov rcx, rsi
002E1F32  E8 29 0A 08 00                  call 0x140362960
002E1F37  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002E1F41  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002E1F46  48 83 E3 BD                     and rbx, 0xffffffffffffffbd
002E1F4A  49 8B CE                        mov rcx, r14
002E1F4D  48 8B D3                        mov rdx, rbx
002E1F50  E8 BB F8 F9 FF                  call 0x140281810
002E1F55  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002E1F5A  45 33 C9                        xor r9d, r9d
002E1F5D  49 8B D7                        mov rdx, r15
002E1F60  45 8D 41 01                     lea r8d, [r9 + 1]
002E1F64  E8 07 17 FB FF                  call 0x140293670
002E1F69  E9 67 01 00 00                  jmp 0x1402e20d5
002E1F6E  48 85 C9                        test rcx, rcx
002E1F71  75 0C                           jne 0x1402e1f7f
002E1F73  41 8B 40 38                     mov eax, dword ptr [r8 + 0x38]
002E1F77  84 C0                           test al, al
002E1F79  0F 88 34 FA FF FF               js 0x1402e19b3
002E1F7F  49 8B D7                        mov rdx, r15
002E1F82  E8 B9 45 03 00                  call 0x140316540
002E1F87  24 0F                           and al, 0xf
002E1F89  41 83 7A 28 03                  cmp dword ptr [r10 + 0x28], 3
002E1F8E  75 0D                           jne 0x1402e1f9d
002E1F90  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E1F95  3C 09                           cmp al, 9
002E1F97  0F 84 16 FA FF FF               je 0x1402e19b3
002E1F9D  3C 08                           cmp al, 8
002E1F9F  0F 84 CD 00 00 00               je 0x1402e2072
002E1FA5  40 F6 C7 10                     test dil, 0x10
002E1FA9  0F 85 C3 00 00 00               jne 0x1402e2072
002E1FAF  49 8B CD                        mov rcx, r13
002E1FB2  E8 1D 0A 08 00                  call 0x1403629d4
002E1FB7  85 C0                           test eax, eax
002E1FB9  74 11                           je 0x1402e1fcc
002E1FBB  49 8B D6                        mov rdx, r14
002E1FBE  49 8B CD                        mov rcx, r13
002E1FC1  E8 3A 24 FB FF                  call 0x140294400
002E1FC6  41 BB 01 00 00 00               mov r11d, 1
002E1FCC  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
002E1FD1  48 85 DB                        test rbx, rbx
002E1FD4  75 3E                           jne 0x1402e2014
002E1FD6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002E1FDB  48 85 C0                        test rax, rax
002E1FDE  75 0E                           jne 0x1402e1fee
002E1FE0  E8 AB 0C F6 FF                  call 0x140242c90
002E1FE5  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002E1FEA  44 8D 5B 01                     lea r11d, [rbx + 1]
002E1FEE  48 8D 98 28 10 00 00            lea rbx, [rax + 0x1028]
002E1FF5  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
002E1FFA  44 8B 43 0C                     mov r8d, dword ptr [rbx + 0xc]
002E1FFE  48 8B CB                        mov rcx, rbx
002E2001  41 B9 02 00 00 00               mov r9d, 2
002E2007  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
002E200C  49 8B D5                        mov rdx, r13
002E200F  E8 EC 2E FB FF                  call 0x140294f00
002E2014  45 33 C9                        xor r9d, r9d
002E2017  4D 8B C3                        mov r8, r11
002E201A  49 8B D7                        mov rdx, r15
002E201D  48 8B CB                        mov rcx, rbx
002E2020  E8 4B 16 FB FF                  call 0x140293670
002E2025  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
002E2028  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E202D  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
002E2032  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E2037  39 43 1C                        cmp dword ptr [rbx + 0x1c], eax
002E203A  0F 85 7D F9 FF FF               jne 0x1402e19bd
002E2040  45 33 C0                        xor r8d, r8d
002E2043  48 8B D3                        mov rdx, rbx
002E2046  49 8B CD                        mov rcx, r13
002E2049  E8 1A F1 F5 FF                  call 0x140241168
002E204E  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
002E2052  48 85 C0                        test rax, rax
002E2055  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E205A  B8 15 01 00 00                  mov eax, 0x115
002E205F  0F 45 D8                        cmovne ebx, eax
002E2062  33 C0                           xor eax, eax
002E2064  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002E2069  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
002E206D  E9 99 FD FF FF                  jmp 0x1402e1e0b
002E2072  8B CF                           mov ecx, edi
002E2074  83 E1 40                        and ecx, 0x40
002E2077  C1 E1 09                        shl ecx, 9
002E207A  41 0B CB                        or ecx, r11d
002E207D  44 8B C1                        mov r8d, ecx
002E2080  41 0F BA E8 0B                  bts r8d, 0xb
002E2085  40 F6 C7 80                     test dil, 0x80
002E2089  44 0F 44 C1                     cmove r8d, ecx
002E208D  40 F6 C7 08                     test dil, 8
002E2091  75 39                           jne 0x1402e20cc
002E2093  83 7D 88 00                     cmp dword ptr [rbp - 0x78], 0
002E2097  74 33                           je 0x1402e20cc
002E2099  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
002E20A0  24 0F                           and al, 0xf
002E20A2  41 3A C3                        cmp al, r11b
002E20A5  74 25                           je 0x1402e20cc
002E20A7  45 8B CC                        mov r9d, r12d
002E20AA  49 8B D7                        mov rdx, r15
002E20AD  48 8B CE                        mov rcx, rsi
002E20B0  E8 67 14 0A 00                  call 0x14038351c
002E20B5  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E20BA  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
002E20BF  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E20C4  85 C0                           test eax, eax
002E20C6  0F 85 F1 F8 FF FF               jne 0x1402e19bd
002E20CC  B8 15 01 00 00                  mov eax, 0x115
002E20D1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002E20D5  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E20DA  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
002E20DF  E9 27 FD FF FF                  jmp 0x1402e1e0b
002E20E4  BA 11 00 00 00                  mov edx, 0x11
002E20E9  44 8D 72 F0                     lea r14d, [rdx - 0x10]
002E20ED  41 8B CE                        mov ecx, r14d
002E20F0  E8 2B 4F FB FF                  call 0x140297020
002E20F5  E9 5E F8 FF FF                  jmp 0x1402e1958
002E20FA  45 33 C9                        xor r9d, r9d
002E20FD  41 BE 01 00 00 00               mov r14d, 1
002E2103  4D 85 ED                        test r13, r13
002E2106  0F 84 AA 00 00 00               je 0x1402e21b6
002E210C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002E2111  48 85 C0                        test rax, rax
002E2114  74 2F                           je 0x1402e2145
002E2116  44 39 48 1C                     cmp dword ptr [rax + 0x1c], r9d
002E211A  74 24                           je 0x1402e2140
002E211C  45 33 C0                        xor r8d, r8d
002E211F  48 8B D0                        mov rdx, rax
002E2122  49 8B CD                        mov rcx, r13
002E2125  E8 3E F0 F5 FF                  call 0x140241168
002E212A  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
002E212E  45 33 C9                        xor r9d, r9d
002E2131  48 85 C0                        test rax, rax
002E2134  B8 15 01 00 00                  mov eax, 0x115
002E2139  0F 45 C8                        cmovne ecx, eax
002E213C  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
002E2140  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
002E2145  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002E214A  48 85 C0                        test rax, rax
002E214D  74 10                           je 0x1402e215f
002E214F  48 8B C8                        mov rcx, rax
002E2152  E8 69 FE 02 00                  call 0x140311fc0
002E2157  45 33 C9                        xor r9d, r9d
002E215A  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
002E215F  4C 39 4C 24 58                  cmp qword ptr [rsp + 0x58], r9
002E2164  74 0A                           je 0x1402e2170
002E2166  E8 05 1B 03 00                  call 0x140313c70
002E216B  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
002E2170  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
002E2175  48 85 DB                        test rbx, rbx
002E2178  75 0B                           jne 0x1402e2185
002E217A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
002E217E  E8 7D 96 06 00                  call 0x14034b800
002E2183  EB 21                           jmp 0x1402e21a6
002E2185  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002E218A  48 85 C0                        test rax, rax
002E218D  74 0B                           je 0x1402e219a
002E218F  48 8B D0                        mov rdx, rax
002E2192  49 8B CD                        mov rcx, r13
002E2195  E8 26 4D F3 FF                  call 0x140216ec0
002E219A  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
002E219E  49 8B CD                        mov rcx, r13
002E21A1  E8 EA B4 F9 FF                  call 0x14027d690
002E21A6  45 33 C9                        xor r9d, r9d
002E21A9  45 8B E1                        mov r12d, r9d
002E21AC  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
002E21B1  45 8B E9                        mov r13d, r9d
002E21B4  EB 0A                           jmp 0x1402e21c0
002E21B6  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
002E21BB  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
002E21C0  44 39 4D 80                     cmp dword ptr [rbp - 0x80], r9d
002E21C4  0F 84 DB 00 00 00               je 0x1402e22a5
002E21CA  B8 11 00 00 00                  mov eax, 0x11
002E21CF  F0 4C 0F B1 0D 68 3E B5 00      lock cmpxchg qword ptr [rip + 0xb53e68], r9
002E21D8  74 0C                           je 0x1402e21e6
002E21DA  48 8D 0D 5F 3E B5 00            lea rcx, [rip + 0xb53e5f]
002E21E1  E8 5A 12 F8 FF                  call 0x140263440
002E21E6  48 8D 0D 53 3E B5 00            lea rcx, [rip + 0xb53e53]
002E21ED  E8 0E F4 FF FF                  call 0x1402e1600
002E21F2  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
002E21F6  90                              nop
002E21F7  66 44 01 B6 E6 01 00 00         add word ptr [rsi + 0x1e6], r14w
002E21FF  75 12                           jne 0x1402e2213
002E2201  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
002E2208  90                              nop
002E2209  48 39 00                        cmp qword ptr [rax], rax
002E220C  74 05                           je 0x1402e2213
002E220E  E8 6D 0A 00 00                  call 0x1402e2c80
002E2213  45 33 C9                        xor r9d, r9d
002E2216  44 39 4D 84                     cmp dword ptr [rbp - 0x7c], r9d
002E221A  74 17                           je 0x1402e2233
002E221C  33 D2                           xor edx, edx
002E221E  48 8D 4D 60                     lea rcx, [rbp + 0x60]
002E2222  E8 49 55 0E 00                  call 0x1403c7770
002E2227  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
002E222E  E8 AD D1 FA FF                  call 0x14028f3e0
002E2233  48 85 DB                        test rbx, rbx
002E2236  74 0D                           je 0x1402e2245
002E2238  BA 4D 6D 56 77                  mov edx, 0x77566d4d
002E223D  48 8B CB                        mov rcx, rbx
002E2240  E8 5B 1C F8 FF                  call 0x140263ea0
002E2245  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002E2249  33 D2                           xor edx, edx
002E224B  E8 20 06 8A 00                  call 0x140b82870
002E2250  45 33 C9                        xor r9d, r9d
002E2253  45 8D 59 01                     lea r11d, [r9 + 1]
002E2257  44 39 4D 88                     cmp dword ptr [rbp - 0x78], r9d
002E225B  74 0C                           je 0x1402e2269
002E225D  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
002E2261  48 8B 00                        mov rax, qword ptr [rax]
002E2264  41 84 C3                        test r11b, al
002E2267  74 45                           je 0x1402e22ae
002E2269  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
002E226D  48 85 DB                        test rbx, rbx
002E2270  0F 85 35 F5 FF FF               jne 0x1402e17ab
002E2276  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002E227A  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
002E2281  48 33 CC                        xor rcx, rsp
002E2284  E8 B7 A3 3C 00                  call 0x1406ac640
002E2289  48 8B 9C 24 E8 01 00 00         mov rbx, qword ptr [rsp + 0x1e8]
002E2291  48 81 C4 A0 01 00 00            add rsp, 0x1a0
002E2298  41 5F                           pop r15
002E229A  41 5E                           pop r14
002E229C  41 5D                           pop r13
002E229E  41 5C                           pop r12
002E22A0  5F                              pop rdi
002E22A1  5E                              pop rsi
002E22A2  5D                              pop rbp
002E22A3  C3                              ret
002E22A4  CC                              int3
002E22A5  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
002E22A9  E9 68 FF FF FF                  jmp 0x1402e2216
002E22AE  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
002E22B2  E8 ED ED 77 00                  call 0x140a610a4
002E22B7  33 C0                           xor eax, eax
002E22B9  EB BF                           jmp 0x1402e227a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiTrimSharedPageFromViews(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int8 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (416);
    result = (*(unsigned __int64 *)(v_rip + 11702306)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m12C = a3;
    v_stack_m150 = a2;
    a2 = 0;
    v_stack_m120 = a5;
    v_stack_m168 = a4;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = memset(v_stack_mF8, a2, 128, a4);
    a4 = 0;
    v_stack_m1A8 = 17;
    v_stack_m198 = 0;
    v_stack_m180 = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    v_stack_m128 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1A0 = 0;
    if (a1 == 0) goto loc_002E227A;
loc_002E17AB:
    v_stack_m140 = a1;
    v_stack_m118 = *(unsigned __int64 *)(a1);
    v_stack_m154 = 0;
    result = (*(unsigned __int64 *)(a1 + 16)) >> (12);
    v_r14 = (*(unsigned __int64 *)(a1 + 24)) >> (12);
    v_r14 = (v_r14) - (result);
    v_stack_m160 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m110 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m188 = v_r14;
    v_stack_m190 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m158 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_002E185D;
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_002E185D;
    result = ExAcquireSpinLockExclusive(v_rip + 11885741, *(unsigned __int64 *)(a1 + 32), a1, a4);
    result = MiPrepareAttachThread(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 8) + 1024, a1, (unsigned __int8)(result));
    v_stack_m154 = (unsigned int)(result);
    result = MiReleaseSpinLockExclusive(v_rip + 11885705, (unsigned __int8)((unsigned __int8)(result)), a1, (unsigned __int8)(result));
    a4 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_002E20FD;
    a3 = 0;
    result = KeForceAttachProcess(*(unsigned __int64 *)(a1 + 8), v_stack_m78, a3, a4);
    goto loc_002E1999;
loc_002E185D:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40)))) & (0xFFFFFFFCULL)) != 0) goto loc_002E1871;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40)))) != 2) goto loc_002E199E;
loc_002E1871:
    if ((((unsigned __int8)((unsigned int)(a3))) & (6)) != 0) goto loc_002E20FD;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 11880374, a2, a3, a4);
    result = 0;
    v_r10 = result + 17;
    if (!(condition_is_equal)) {
        a4 = v_rip + 11880336;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 11880324;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        v_r10 = 17;
    }
    a4 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(a4 + 1);
    }
    goto loc_002E1905;
loc_002E18E0:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 88)) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 32)) + (a3);
    if ((*(unsigned __int64 *)(a1 + 16)) < a1) goto loc_002E18FD;
    goto loc_002E1905;
loc_002E18FD:
    if ((*(unsigned __int64 *)(a1 + 16)) >= a3) goto loc_002E190A;
loc_002E1905:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) != 0) goto loc_002E18E0;
loc_002E190A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) != 0) goto loc_002E1960;
loc_002E190F:
    result = v_r10;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) != 0) {
        a1 = v_rip + 11880220;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)), a3, a4);
    }
    result = KeAbPostRelease(v_rip + 11880208, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)), a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) != 0) goto loc_002E1958;
    result = (unsigned int)((unsigned int)(result)) + 152;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 152)) != ((unsigned int)((unsigned int)(result)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 11880208, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)), a3, a4);
    }
    a4 = 0;
    goto loc_002E2103;
loc_002E1960:
    v_stack_m148 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) + 48);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) + 48))) != v_stack_m168) goto loc_002E190F;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) + 24)) << (12);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11880298) + 8)) + 88)) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) - (v_stack_m190);
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 16));
    if (a1 != result) goto loc_002E190F;
    v_stack_m158 = (unsigned int)(a4 + 1);
loc_002E1999:
loc_002E199E:
    a2 = (v_stack_m190) - (0x1000ULL);
    v_stack_m190 = a2;
    v_r15 = (*(unsigned __int64 *)(a1 + 16)) - (0x1000ULL);
    goto loc_002E19BD;
loc_002E19B3:
loc_002E19B8:
loc_002E19BD:
    result = Feature_Servicing_Mm_TrimSharedPageFix__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_002E19DF;
    v_r15 = (v_r15) + (0x1000ULL);
    if (v_r15 >= v_stack_m110) goto loc_002E20FD;
    goto loc_002E19F7;
loc_002E19DF:
    if (v_stack_m188 == 0) goto loc_002E20FD;
    v_r14 = (v_stack_m188) - 1;
    v_stack_m188 = v_r14;
    v_r15 = (v_r15) + (0x1000ULL);
loc_002E19F7:
    v_rbx = (v_stack_m190) + (0x1000ULL);
    v_stack_m190 = v_rbx;
    if (0 == 0) goto loc_002E1AD4;
    a1 = (v_r15) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + (result);
    if (a1 == v_stack_m1A0) goto loc_002E1AD4;
    if (v_stack_m170 == 0) goto loc_002E1A70;
    result = v_stack_m170;
    if ((*(unsigned int *)(v_stack_m170 + 28)) != 0) {
        a3 = 0;
        a2 = v_stack_m170;
        a1 = 0;
        result = MiFreeWsleList(a1, a2, a3, a4);
        a1 = v_stack_m198;
        a4 = 0;
        result = 277;
        if (result != 0) { a1 = (unsigned int)(result); }
        v_stack_m198 = (unsigned int)(a1);
    }
    v_stack_m170 = 0;
loc_002E1A70:
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        a1 = v_stack_m178;
        result = MiFlushTbList(a1, a2, a3, a4);
        a4 = 0;
        v_stack_m178 = 0;
    }
    if (v_stack_m180 != 0) {
        result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
        v_stack_m180 = 0;
    }
    if (v_stack_m160 != 0) goto loc_002E1AAD;
    result = MiUnlockSystemVa(v_stack_mF8, a2, a3, a4);
    goto loc_002E1AC9;
loc_002E1AAD:
    if (v_stack_m1A0 != 0) {
        a2 = v_stack_m1A0;
        a1 = 0;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(0, v_stack_m1A8, a3, a4);
loc_002E1AC9:
    a4 = 0;
    v_stack_m1A0 = 0;
loc_002E1AD4:
    if (v_stack_m160 != 0) goto loc_002E1C49;
    if (0 != 0) goto loc_002E1BA7;
    result = MiGetSystemRegionType(v_r15, v_stack_m1A8, a3, a4);
    result = MiSystemVaTypeHasWsles((unsigned int)((unsigned int)(result)), v_stack_m1A8, a3, a4);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_002E21B6;
    result = MiSystemVaTypeToVm((unsigned int)((unsigned int)(result)), v_stack_m1A8, a3, a4);
    if (result == 0) goto loc_002E21B6;
    v_stack_m1B8 = v_stack_mF8;
    result = MiSynchronizeSystemVa(result, v_r15, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_002E210C;
    if ((((unsigned __int8)(v_stack_m160 + 1)) & ((unsigned __int8)((unsigned int)(a3)))) == 0) goto loc_002E1B85;
    if (v_stack_m178 != 0) goto loc_002E1B85;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(result, v_r15, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
        v_stack_m180 = result;
    }
    a4 = 0;
    v_stack_m178 = result;
    v_stack_m1B8 = 10;
    result = MiInitializeTbFlushList(result, v_stack_mE0, (unsigned int)(*(unsigned int *)(result + 12)), a4);
loc_002E1B85:
    a1 = (v_r15) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + (result);
    v_stack_m1A0 = a1;
loc_002E1BA7:
    if ((*(unsigned int *)(v_stack_m140 + 40)) != 0) goto loc_002E1F11;
    result = MiGetSystemRegionType(v_r15, v_stack_mE0, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    if (((unsigned int)(result)) != 7) goto loc_002E1958;
    result = MiGetSystemCacheReverseMap(v_r15, v_stack_mE0, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    if (result == 0) goto loc_002E1958;
    result = MiGetMultiplexedVm(v_r15, v_r15, (unsigned int)(*(unsigned int *)(result + 12)), result);
    if (v_stack_mE0 != result) goto loc_002E1958;
    result = (*(unsigned __int64 *)(result + 32)) >> (62);
    if (((unsigned __int8)(result)) != 3) goto loc_002E1958;
    v_stack_m148 = *(unsigned __int64 *)(result + 24);
    result = *(unsigned __int64 *)(result + 24);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_stack_m160 + 1)))) & ((unsigned __int8)(*(unsigned __int64 *)(result + 24)))) != 0) {
        result = (*(unsigned __int64 *)(result + 24)) & (-2);
        v_stack_m148 = result;
    }
    if ((*(unsigned __int64 *)(result)) != v_stack_m168) goto loc_002E1958;
    result = (*(unsigned __int64 *)(result + 32)) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (unsigned int)((v_r15) & (0x3FFFFULL));
    if ((a1 + result * 4) != v_rbx) goto loc_002E1958;
    goto loc_002E1E42;
loc_002E1C49:
    if (v_stack_mE0 != 0) goto loc_002E1CA5;
    result = MiLockWorkingSetShared(result + 1024, v_rbx, v_stack_m168, result);
    v_stack_m1A8 = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) == 0) goto loc_002E1CA5;
    if (v_stack_m178 != 0) goto loc_002E1CA5;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(result + 1024, v_rbx, v_stack_m168, result);
        v_stack_m180 = result;
    }
    a4 = 0;
    v_stack_m178 = result;
    v_stack_m1B8 = 10;
    result = MiInitializeTbFlushList(result, result + 1024, (unsigned int)(*(unsigned int *)(result + 12)), a4);
loc_002E1CA5:
    result = MiLockVadTree(1, result + 1024, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    result = MiLocateAddress(v_r15, result + 1024, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    if (result == 0) goto loc_002E20E4;
    if (condition_is_below) goto loc_002E20E4;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m168 + 56))) & (32));
    if (condition_is_not_equal) goto loc_002E1CE6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (112)) != 0) goto loc_002E20E4;
loc_002E1CE6:
    v_stack_m148 = *(unsigned __int64 *)(result + 72);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72))) != v_stack_m168) goto loc_002E20E4;
    if (a2 == 0) goto loc_002E1D63;
    if (v_stack_m120 < (*(unsigned __int64 *)(result + 80))) goto loc_002E20E4;
    a2 = (*(unsigned __int8 *)(result + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 28)));
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 32)))) << (32);
    result = (result) | ((unsigned int)(*(unsigned int *)(result + 24)));
    result = (result) * (result);
    result = (result) + (8);
    result = (result) + (*(unsigned __int64 *)(result + 80));
    if (v_stack_m120 >= (result + a2 * 8)) goto loc_002E20E4;
    v_r15 = (*(unsigned __int8 *)(result + 32)) << (32);
    result = (v_stack_m120) - (*(unsigned __int64 *)(result + 80));
    v_r15 = (v_r15) | ((unsigned int)(*(unsigned int *)(result + 24)));
    result = (result) >> (3);
    result = (result) << (12);
    v_r15 = (v_r15) << (12);
    v_r15 = (v_r15) + (result);
    goto loc_002E1DA4;
loc_002E1D63:
    a2 = (v_r15) >> (12);
    result = MiGetProtoPteAddress(result, a2, 8, v_stack_m148);
    if (result == 0) goto loc_002E20E4;
    if (v_stack_m148 == 0) goto loc_002E20E4;
    a3 = (unsigned int)((8) | (0xFFFFFFFFULL));
    result = MiStartingOffset(v_stack_m148, result, a3, v_stack_m148);
    if (v_rbx != result) goto loc_002E20E4;
loc_002E1DA4:
    result = MiUnlockVadTree(17 - 16, 17, a3, v_stack_m148);
    a2 = (v_r15) >> (9);
    a2 = (a2) & (v_stack_m148);
    a2 = (a2) + (a3);
    v_rbx = (a2) >> (9);
    v_rbx = (v_rbx) & (v_stack_m148);
    v_rbx = (v_rbx) + (a3);
    if (v_stack_m1A0 == v_rbx) goto loc_002E1E32;
    if (v_stack_m1A0 == 0) goto loc_002E1E15;
    v_r15 = (v_r15) - (0x1000ULL);
    v_r14 = (v_stack_m160 + 1) + 1;
    v_stack_m190 = a2;
    v_stack_m188 = v_r14;
loc_002E1E0B:
    goto loc_002E19BD;
loc_002E1E15:
    a4 = 0;
    result = MiLockLowestValidPageTableEx(result + 1024, a2, v_stack_m108, a4);
    v_stack_m1A0 = result;
    if (result != v_rbx) goto loc_002E20FA;
loc_002E1E32:
loc_002E1E42:
loc_002E1E46:
    v_r14 = (v_r15) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (result);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) == 0) goto loc_002E19B3;
    result = (*(unsigned __int64 *)(v_r14)) >> (12);
    result = (result) & (result + 1024);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    if ((((unsigned __int8)((unsigned int)(a3))) & (8)) == 0) goto loc_002E1EB8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) != 0) goto loc_002E19B3;
    if (((*(unsigned __int8 *)(v_rsi + 34)) & (16)) != 0) goto loc_002E19B3;
loc_002E1EB8:
    if (!sign_flag) goto loc_002E19B3;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rsi + 16)) & (0x400ULL));
    if (((1) & ((unsigned __int8)((unsigned int)(a3)))) == 0) goto loc_002E1F6E;
    if (a1 == 0) goto loc_002E19B8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) == 0) goto loc_002E19B8;
    v_rdi = 0;
    v_stack_m130 = 0;
loc_002E1EF4:
    if (condition_is_above_or_equal) goto loc_002E1F21;
loc_002E1EFD:
    result = KeYieldProcessorEx(v_stack_m130, v_stack_m190, v_stack_m168, a4);
    if (sign_flag) goto loc_002E1EFD;
    goto loc_002E1EF4;
loc_002E1F11:
    goto loc_002E1E46;
loc_002E1F21:
    result = *(unsigned __int64 *)(v_rsi + 24);
    if (((*(unsigned __int8 *)(v_rsi + 34)) & (16)) == 0) {
        a2 = 1;
        a1 = v_rsi;
        result = MiSetPfnModified(a1, a2, v_stack_m168, a4);
    }
    v_rbx = (*(unsigned __int64 *)(v_r14)) & (-67);
    result = MiWriteValidPteNewProtection(v_r14, v_rbx, v_stack_m168, a4);
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m178, v_r15, a4 + 1, a4);
    goto loc_002E20D5;
loc_002E1F6E:
    if (v_stack_m178 != 0) goto loc_002E1F7F;
    if (sign_flag) goto loc_002E19B3;
loc_002E1F7F:
    result = MiGetWsleContents(v_stack_m178, v_r15, a4 + 1, a4);
    result = (unsigned __int8)((result) & (15));
    if ((*(unsigned int *)(v_stack_m140 + 40)) != 3) goto loc_002E1F9D;
    if (((unsigned __int8)(result)) == 9) goto loc_002E19B3;
loc_002E1F9D:
    if (((unsigned __int8)(result)) == 8) goto loc_002E2072;
    if ((((unsigned __int8)((unsigned int)(v_stack_m12C))) & (16)) != 0) goto loc_002E2072;
    result = MiVmAccessLoggingEnabled(result + 1024, v_stack_m190, a4 + 1, a4);
    v_r11 = v_stack_m1A0;
    if ((unsigned int)(result) != 0) {
        a2 = v_r14;
        a1 = result + 1024;
        result = MI_WSLE_LOG_ACCESS(a1, a2, a4 + 1, a4);
        v_r11 = 1;
    }
    if (v_stack_m170 != 0) goto loc_002E2014;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(a1, a2, a4 + 1, a4);
        v_stack_m180 = result;
        v_r11 = v_stack_m170 + 1;
    }
    v_stack_m1B8 = (unsigned int)(v_r11);
    v_stack_m170 = result + 4136;
    result = MiInitializeTbFlushList(result + 4136, result + 1024, (unsigned int)(*(unsigned int *)(result + 4136 + 12)), 2);
loc_002E2014:
    a4 = 0;
    result = MiInsertTbFlushEntry(result + 4136, v_r15, v_r11, a4);
    if ((*(unsigned int *)(result + 4136 + 28)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4136 + 12))))) goto loc_002E19BD;
    a3 = 0;
    result = MiFreeWsleList(result + 1024, result + 4136, a3, a4);
    v_rbx = (unsigned int)(v_stack_m198);
    if (result != 0) { v_rbx = 277; }
    result = 0;
    v_stack_m170 = 0;
    v_stack_m198 = (unsigned int)(v_rbx);
    goto loc_002E1E0B;
loc_002E2072:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m12C)))) & (64));
    a1 = (unsigned int)((a1) << (9));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_r11)));
    a3 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)((unsigned int)(v_stack_m12C))) & (128)) == 0) { a3 = (unsigned int)(a1); }
    if ((((unsigned __int8)((unsigned int)(v_stack_m12C))) & (8)) != 0) goto loc_002E20CC;
    if (v_stack_m150 == 0) goto loc_002E20CC;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 1024 + 184))) & (15));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(v_r11))) goto loc_002E20CC;
    result = MiReplaceLockedPage(v_rsi, v_r15, a3, (unsigned int)((unsigned int)(v_stack_m1A0)));
    if ((unsigned int)(result) != 0) goto loc_002E19BD;
loc_002E20CC:
    v_stack_m198 = 277;
loc_002E20D5:
    goto loc_002E1E0B;
loc_002E20E4:
    result = MiUnlockVadTree((unsigned int)((unsigned int)(17 - 16)), 17, a3, (unsigned int)((unsigned int)(v_stack_m1A0)));
    goto loc_002E1958;
loc_002E20FA:
    a4 = 0;
loc_002E20FD:
loc_002E2103:
    if (result + 1024 == 0) goto loc_002E21B6;
loc_002E210C:
    if (v_stack_m170 == 0) goto loc_002E2145;
    result = v_stack_m170;
    if ((*(unsigned int *)(v_stack_m170 + 28)) != 0) {
        a3 = 0;
        a2 = v_stack_m170;
        a1 = result + 1024;
        result = MiFreeWsleList(a1, a2, a3, a4);
        a1 = v_stack_m198;
        a4 = 0;
        result = 277;
        if (result != 0) { a1 = (unsigned int)(result); }
        v_stack_m198 = (unsigned int)(a1);
    }
    v_stack_m170 = 0;
loc_002E2145:
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        a1 = v_stack_m178;
        result = MiFlushTbList(a1, a2, a3, a4);
        a4 = 0;
        v_stack_m178 = 0;
    }
    if (v_stack_m180 != 0) {
        result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
        v_stack_m180 = 0;
    }
    if (v_stack_m160 != 0) goto loc_002E2185;
    result = MiUnlockSystemVa(v_stack_mF8, a2, a3, a4);
    goto loc_002E21A6;
loc_002E2185:
    result = v_stack_m1A0;
    if (v_stack_m1A0 != 0) {
        a2 = v_stack_m1A0;
        a1 = result + 1024;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(result + 1024, v_stack_m1A8, a3, a4);
loc_002E21A6:
    a4 = 0;
    v_stack_m1A0 = 0;
    goto loc_002E21C0;
loc_002E21B6:
loc_002E21C0:
    if (v_stack_m158 == 0) goto loc_002E22A5;
    result = 17;
    if (v_stack_m158 != 0) {
        a1 = v_rip + 11877983;
        result = ExfReleasePushLockShared(a1, v_stack_m1A8, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 11877971, v_stack_m1A8, a3, a4);
    if (v_stack_m158 != 0) goto loc_002E2213;
    result = v_stack_m128 + 152;
    if ((*(unsigned __int64 *)(v_stack_m128 + 152)) != (v_stack_m128 + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 11877971, v_stack_m1A8, a3, a4);
    }
    a4 = 0;
loc_002E2216:
    if (v_stack_m154 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = KeForceDetachProcess(a1, a2, a3, a4);
        a1 = v_stack_m160 + 1024;
        result = MiAttachThreadDone(a1, a2, a3, a4);
    }
    if (v_stack_m160 != 0) {
        a2 = 0x77566D4DULL;
        a1 = v_stack_m160;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m140, a2, a3, a4);
    a4 = 0;
    if (v_stack_m150 == 0) goto loc_002E2269;
    if ((((unsigned __int8)(a4 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m120)))) == 0) goto loc_002E22AE;
loc_002E2269:
    if (v_stack_m118 != 0) goto loc_002E17AB;
loc_002E227A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (416);
    return result;
loc_002E22A5:
    goto loc_002E2216;
loc_002E22AE:
    result = MiDeleteTrimViewInfoList(v_stack_m118, a2, a3, a4);
    result = 0;
    goto loc_002E227A;
}
```

## 5. (Beta) C Style

```c
int64_t MiTrimSharedPageFromViews(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint8_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (416);
    result = (*(uint64_t *)(v_rip + 0xB29022)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m12C = Arg3;
    v_stack_m150 = Arg2;
    Arg2 = 0;
    v_stack_m120 = Arg5;
    v_stack_m168 = Arg4;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = memset(v_stack_mF8, Arg2, 128, Arg4);
    Arg4 = 0;
    v_stack_m1A8 = 17;
    v_stack_m198 = 0;
    v_stack_m180 = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    v_stack_m128 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1A0 = 0;
    if (Arg1 == 0) goto loc_002E227A;
loc_002E17AB:
    v_stack_m140 = Arg1;
    v_stack_m118 = *(uint64_t *)(Arg1);
    v_stack_m154 = 0;
    result = (*(uint64_t *)(Arg1 + 0x10)) >> (12);
    local_r14 = (*(uint64_t *)(Arg1 + 0x18)) >> (12);
    local_r14 = (local_r14) - (result);
    v_stack_m160 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m110 = *(uint64_t *)(Arg1 + 0x18);
    v_stack_m188 = local_r14;
    v_stack_m190 = *(uint64_t *)(Arg1 + 0x20);
    v_stack_m158 = 0;
    if (*(uint64_t *)(Arg1 + 0x8) == 0) goto loc_002E185D;
    if ((*(uint64_t *)(Arg1 + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_002E185D;
    result = ExAcquireSpinLockExclusive(v_rip + 11885741, *(uint64_t *)(Arg1 + 0x20), Arg1, Arg4);
    result = MiPrepareAttachThread(*(uint64_t *)(Arg1 + 0x8), *(uint64_t *)(Arg1 + 0x8) + 1024, Arg1, (uint8_t)(result));
    v_stack_m154 = (uint32_t)(result);
    result = MiReleaseSpinLockExclusive(v_rip + 11885705, (uint8_t)((uint8_t)(result)), Arg1, (uint8_t)(result));
    Arg4 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_002E20FD;
    Arg3 = 0;
    result = KeForceAttachProcess(*(uint64_t *)(Arg1 + 0x8), v_stack_m78, Arg3, Arg4);
    goto loc_002E1999;
loc_002E185D:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x28)))) & (0xFFFFFFFCULL)) != 0) goto loc_002E1871;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x28)))) != 2) goto loc_002E199E;
loc_002E1871:
    if ((((uint8_t)((uint32_t)(Arg3))) & (6)) != 0) goto loc_002E20FD;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 11880374, Arg2, Arg3, Arg4);
    result = 0;
    local_r10 = result + 17;
    if (!(condition_is_equal)) {
        Arg4 = v_rip + 11880336;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 11880324;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 17;
    }
    Arg4 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(Arg4 + 1);
    }
    goto loc_002E1905;
loc_002E18E0:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x58)) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x20)) + (Arg3);
    if ((*(uint64_t *)(Arg1 + 0x10)) < Arg1) goto loc_002E18FD;
    goto loc_002E1905;
loc_002E18FD:
    if ((*(uint64_t *)(Arg1 + 0x10)) >= Arg3) goto loc_002E190A;
loc_002E1905:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) != 0) goto loc_002E18E0;
loc_002E190A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) != 0) goto loc_002E1960;
loc_002E190F:
    result = local_r10;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) != 0) {
        Arg1 = v_rip + 11880220;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)), Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 11880208, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)), Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) != 0) goto loc_002E1958;
    result = (uint32_t)((uint32_t)(result)) + 152;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x98)) != ((uint32_t)((uint32_t)(result)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 11880208, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)), Arg3, Arg4);
    }
    Arg4 = 0;
    goto loc_002E2103;
loc_002E1960:
    v_stack_m148 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) + 0x30);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) + 0x30))) != v_stack_m168) goto loc_002E190F;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) + 0x18)) << (12);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5476A) + 0x8)) + 0x58)) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) - (v_stack_m190);
    Arg1 = (Arg1) + (*(uint64_t *)(Arg1 + 0x10));
    if (Arg1 != result) goto loc_002E190F;
    v_stack_m158 = (uint32_t)(Arg4 + 1);
loc_002E1999:
loc_002E199E:
    Arg2 = (v_stack_m190) - (0x1000ULL);
    v_stack_m190 = Arg2;
    local_r15 = (*(uint64_t *)(Arg1 + 0x10)) - (0x1000ULL);
    goto loc_002E19BD;
loc_002E19B3:
loc_002E19B8:
loc_002E19BD:
    result = Feature_Servicing_Mm_TrimSharedPageFix__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_002E19DF;
    local_r15 = (local_r15) + (0x1000ULL);
    if (local_r15 >= v_stack_m110) goto loc_002E20FD;
    goto loc_002E19F7;
loc_002E19DF:
    if (v_stack_m188 == 0) goto loc_002E20FD;
    local_r14 = (v_stack_m188) - 1;
    v_stack_m188 = local_r14;
    local_r15 = (local_r15) + (0x1000ULL);
loc_002E19F7:
    local_rbx = (v_stack_m190) + (0x1000ULL);
    v_stack_m190 = local_rbx;
    if (0 == 0) goto loc_002E1AD4;
    Arg1 = (local_r15) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + (result);
    if (Arg1 == v_stack_m1A0) goto loc_002E1AD4;
    if (v_stack_m170 == 0) goto loc_002E1A70;
    result = v_stack_m170;
    if ((*(uint32_t *)(v_stack_m170 + 0x1C)) != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m170;
        Arg1 = 0;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m198;
        Arg4 = 0;
        result = 277;
        if (result != 0) { Arg1 = (uint32_t)(result); }
        v_stack_m198 = (uint32_t)(Arg1);
    }
    v_stack_m170 = 0;
loc_002E1A70:
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        Arg1 = v_stack_m178;
        result = MiFlushTbList(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
        v_stack_m178 = 0;
    }
    if (v_stack_m180 != 0) {
        result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, Arg4);
        v_stack_m180 = 0;
    }
    if (v_stack_m160 != 0) goto loc_002E1AAD;
    result = MiUnlockSystemVa(v_stack_mF8, Arg2, Arg3, Arg4);
    goto loc_002E1AC9;
loc_002E1AAD:
    if (v_stack_m1A0 != 0) {
        Arg2 = v_stack_m1A0;
        Arg1 = 0;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(0, v_stack_m1A8, Arg3, Arg4);
loc_002E1AC9:
    Arg4 = 0;
    v_stack_m1A0 = 0;
loc_002E1AD4:
    if (v_stack_m160 != 0) goto loc_002E1C49;
    if (0 != 0) goto loc_002E1BA7;
    result = MiGetSystemRegionType(local_r15, v_stack_m1A8, Arg3, Arg4);
    result = MiSystemVaTypeHasWsles((uint32_t)((uint32_t)(result)), v_stack_m1A8, Arg3, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_002E21B6;
    result = MiSystemVaTypeToVm((uint32_t)((uint32_t)(result)), v_stack_m1A8, Arg3, Arg4);
    if (result == 0) goto loc_002E21B6;
    v_stack_m1B8 = v_stack_mF8;
    result = MiSynchronizeSystemVa(result, local_r15, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_002E210C;
    if ((((uint8_t)(v_stack_m160 + 1)) & ((uint8_t)((uint32_t)(Arg3)))) == 0) goto loc_002E1B85;
    if (v_stack_m178 != 0) goto loc_002E1B85;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(result, local_r15, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
        v_stack_m180 = result;
    }
    Arg4 = 0;
    v_stack_m178 = result;
    v_stack_m1B8 = 10;
    result = MiInitializeTbFlushList(result, v_stack_mE0, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
loc_002E1B85:
    Arg1 = (local_r15) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + (result);
    v_stack_m1A0 = Arg1;
loc_002E1BA7:
    if ((*(uint32_t *)(v_stack_m140 + 0x28)) != 0) goto loc_002E1F11;
    result = MiGetSystemRegionType(local_r15, v_stack_mE0, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    if (((uint32_t)(result)) != 7) goto loc_002E1958;
    result = MiGetSystemCacheReverseMap(local_r15, v_stack_mE0, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    if (result == 0) goto loc_002E1958;
    result = MiGetMultiplexedVm(local_r15, local_r15, (uint32_t)(*(uint32_t *)(result + 0xC)), result);
    if (v_stack_mE0 != result) goto loc_002E1958;
    result = (*(uint64_t *)(result + 0x20)) >> (62);
    if (((uint8_t)(result)) != 3) goto loc_002E1958;
    v_stack_m148 = *(uint64_t *)(result + 0x18);
    result = *(uint64_t *)(result + 0x18);
    if ((((uint8_t)((uint32_t)((uint32_t)(v_stack_m160 + 1)))) & ((uint8_t)(*(uint64_t *)(result + 0x18)))) != 0) {
        result = (*(uint64_t *)(result + 0x18)) & (-2);
        v_stack_m148 = result;
    }
    if ((*(uint64_t *)(result)) != v_stack_m168) goto loc_002E1958;
    result = (*(uint64_t *)(result + 0x20)) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (uint32_t)((local_r15) & (0x3FFFFULL));
    if ((Arg1 + result * 4) != local_rbx) goto loc_002E1958;
    goto loc_002E1E42;
loc_002E1C49:
    if (v_stack_mE0 != 0) goto loc_002E1CA5;
    result = MiLockWorkingSetShared(result + 1024, local_rbx, v_stack_m168, result);
    v_stack_m1A8 = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) == 0) goto loc_002E1CA5;
    if (v_stack_m178 != 0) goto loc_002E1CA5;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(result + 1024, local_rbx, v_stack_m168, result);
        v_stack_m180 = result;
    }
    Arg4 = 0;
    v_stack_m178 = result;
    v_stack_m1B8 = 10;
    result = MiInitializeTbFlushList(result, result + 1024, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
loc_002E1CA5:
    result = MiLockVadTree(1, result + 1024, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    result = MiLocateAddress(local_r15, result + 1024, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    if (result == 0) goto loc_002E20E4;
    if (condition_is_below) goto loc_002E20E4;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x38))) & (32));
    if (condition_is_not_equal) goto loc_002E1CE6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (112)) != 0) goto loc_002E20E4;
loc_002E1CE6:
    v_stack_m148 = *(uint64_t *)(result + 0x48);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x48))) != v_stack_m168) goto loc_002E20E4;
    if (Arg2 == 0) goto loc_002E1D63;
    if (v_stack_m120 < (*(uint64_t *)(result + 0x50))) goto loc_002E20E4;
    Arg2 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    result = ((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x20)))) << (32);
    result = (result) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    result = (result) * (result);
    result = (result) + (8);
    result = (result) + (*(uint64_t *)(result + 0x50));
    if (v_stack_m120 >= (result + Arg2 * 8)) goto loc_002E20E4;
    local_r15 = (*(uint8_t *)(result + 0x20)) << (32);
    result = (v_stack_m120) - (*(uint64_t *)(result + 0x50));
    local_r15 = (local_r15) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    result = (result) >> (3);
    result = (result) << (12);
    local_r15 = (local_r15) << (12);
    local_r15 = (local_r15) + (result);
    goto loc_002E1DA4;
loc_002E1D63:
    Arg2 = (local_r15) >> (12);
    result = MiGetProtoPteAddress(result, Arg2, 8, v_stack_m148);
    if (result == 0) goto loc_002E20E4;
    if (v_stack_m148 == 0) goto loc_002E20E4;
    Arg3 = (uint32_t)((8) | (0xFFFFFFFFULL));
    result = MiStartingOffset(v_stack_m148, result, Arg3, v_stack_m148);
    if (local_rbx != result) goto loc_002E20E4;
loc_002E1DA4:
    result = MiUnlockVadTree(17 - 16, 17, Arg3, v_stack_m148);
    Arg2 = (local_r15) >> (9);
    Arg2 = (Arg2) & (v_stack_m148);
    Arg2 = (Arg2) + (Arg3);
    local_rbx = (Arg2) >> (9);
    local_rbx = (local_rbx) & (v_stack_m148);
    local_rbx = (local_rbx) + (Arg3);
    if (v_stack_m1A0 == local_rbx) goto loc_002E1E32;
    if (v_stack_m1A0 == 0) goto loc_002E1E15;
    local_r15 = (local_r15) - (0x1000ULL);
    local_r14 = (v_stack_m160 + 1) + 1;
    v_stack_m190 = Arg2;
    v_stack_m188 = local_r14;
loc_002E1E0B:
    goto loc_002E19BD;
loc_002E1E15:
    Arg4 = 0;
    result = MiLockLowestValidPageTableEx(result + 1024, Arg2, v_stack_m108, Arg4);
    v_stack_m1A0 = result;
    if (result != local_rbx) goto loc_002E20FA;
loc_002E1E32:
loc_002E1E42:
loc_002E1E46:
    local_r14 = (local_r15) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (result);
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) == 0) goto loc_002E19B3;
    result = (*(uint64_t *)(local_r14)) >> (12);
    result = (result) & (result + 1024);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    if ((((uint8_t)((uint32_t)(Arg3))) & (8)) == 0) goto loc_002E1EB8;
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) != 0) goto loc_002E19B3;
    if (((*(uint8_t *)(local_rsi + 0x22)) & (16)) != 0) goto loc_002E19B3;
loc_002E1EB8:
    if (!sign_flag) goto loc_002E19B3;
    Arg1 = (uint32_t)((*(uint64_t *)(local_rsi + 0x10)) & (0x400ULL));
    if (((1) & ((uint8_t)((uint32_t)(Arg3)))) == 0) goto loc_002E1F6E;
    if (Arg1 == 0) goto loc_002E19B8;
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) == 0) goto loc_002E19B8;
    local_rdi = 0;
    v_stack_m130 = 0;
loc_002E1EF4:
    if (condition_is_above_or_equal) goto loc_002E1F21;
loc_002E1EFD:
    result = KeYieldProcessorEx(v_stack_m130, v_stack_m190, v_stack_m168, Arg4);
    if (sign_flag) goto loc_002E1EFD;
    goto loc_002E1EF4;
loc_002E1F11:
    goto loc_002E1E46;
loc_002E1F21:
    result = *(uint64_t *)(local_rsi + 0x18);
    if (((*(uint8_t *)(local_rsi + 0x22)) & (16)) == 0) {
        Arg2 = 1;
        Arg1 = local_rsi;
        result = MiSetPfnModified(Arg1, Arg2, v_stack_m168, Arg4);
    }
    local_rbx = (*(uint64_t *)(local_r14)) & (-67);
    result = MiWriteValidPteNewProtection(local_r14, local_rbx, v_stack_m168, Arg4);
    Arg4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m178, local_r15, Arg4 + 1, Arg4);
    goto loc_002E20D5;
loc_002E1F6E:
    if (v_stack_m178 != 0) goto loc_002E1F7F;
    if (sign_flag) goto loc_002E19B3;
loc_002E1F7F:
    result = MiGetWsleContents(v_stack_m178, local_r15, Arg4 + 1, Arg4);
    result = (uint8_t)((result) & (15));
    if ((*(uint32_t *)(v_stack_m140 + 0x28)) != 3) goto loc_002E1F9D;
    if (((uint8_t)(result)) == 9) goto loc_002E19B3;
loc_002E1F9D:
    if (((uint8_t)(result)) == 8) goto loc_002E2072;
    if ((((uint8_t)((uint32_t)(v_stack_m12C))) & (16)) != 0) goto loc_002E2072;
    result = MiVmAccessLoggingEnabled(result + 1024, v_stack_m190, Arg4 + 1, Arg4);
    local_r11 = v_stack_m1A0;
    if ((uint32_t)(result) != 0) {
        Arg2 = local_r14;
        Arg1 = result + 1024;
        result = MI_WSLE_LOG_ACCESS(Arg1, Arg2, Arg4 + 1, Arg4);
        local_r11 = 1;
    }
    if (v_stack_m170 != 0) goto loc_002E2014;
    result = v_stack_m180;
    if (v_stack_m180 == 0) {
        result = MiGetProcessorFlushList(Arg1, Arg2, Arg4 + 1, Arg4);
        v_stack_m180 = result;
        local_r11 = v_stack_m170 + 1;
    }
    v_stack_m1B8 = (uint32_t)(local_r11);
    v_stack_m170 = result + 4136;
    result = MiInitializeTbFlushList(result + 4136, result + 1024, (uint32_t)(*(uint32_t *)(result + 0x1028 + 0xC)), 2);
loc_002E2014:
    Arg4 = 0;
    result = MiInsertTbFlushEntry(result + 4136, local_r15, local_r11, Arg4);
    if ((*(uint32_t *)(result + 0x1028 + 0x1C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0xC))))) goto loc_002E19BD;
    Arg3 = 0;
    result = MiFreeWsleList(result + 1024, result + 4136, Arg3, Arg4);
    local_rbx = (uint32_t)(v_stack_m198);
    if (result != 0) { local_rbx = 277; }
    result = 0;
    v_stack_m170 = 0;
    v_stack_m198 = (uint32_t)(local_rbx);
    goto loc_002E1E0B;
loc_002E2072:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m12C)))) & (64));
    Arg1 = (uint32_t)((Arg1) << (9));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_r11)));
    Arg3 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)((uint32_t)(v_stack_m12C))) & (128)) == 0) { Arg3 = (uint32_t)(Arg1); }
    if ((((uint8_t)((uint32_t)(v_stack_m12C))) & (8)) != 0) goto loc_002E20CC;
    if (v_stack_m150 == 0) goto loc_002E20CC;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x400 + 0xB8))) & (15));
    if (((uint8_t)(result)) == ((uint8_t)(local_r11))) goto loc_002E20CC;
    result = MiReplaceLockedPage(local_rsi, local_r15, Arg3, (uint32_t)((uint32_t)(v_stack_m1A0)));
    if ((uint32_t)(result) != 0) goto loc_002E19BD;
loc_002E20CC:
    v_stack_m198 = 277;
loc_002E20D5:
    goto loc_002E1E0B;
loc_002E20E4:
    result = MiUnlockVadTree((uint32_t)((uint32_t)(17 - 16)), 17, Arg3, (uint32_t)((uint32_t)(v_stack_m1A0)));
    goto loc_002E1958;
loc_002E20FA:
    Arg4 = 0;
loc_002E20FD:
loc_002E2103:
    if (result + 1024 == 0) goto loc_002E21B6;
loc_002E210C:
    if (v_stack_m170 == 0) goto loc_002E2145;
    result = v_stack_m170;
    if ((*(uint32_t *)(v_stack_m170 + 0x1C)) != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m170;
        Arg1 = result + 1024;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m198;
        Arg4 = 0;
        result = 277;
        if (result != 0) { Arg1 = (uint32_t)(result); }
        v_stack_m198 = (uint32_t)(Arg1);
    }
    v_stack_m170 = 0;
loc_002E2145:
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        Arg1 = v_stack_m178;
        result = MiFlushTbList(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
        v_stack_m178 = 0;
    }
    if (v_stack_m180 != 0) {
        result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, Arg4);
        v_stack_m180 = 0;
    }
    if (v_stack_m160 != 0) goto loc_002E2185;
    result = MiUnlockSystemVa(v_stack_mF8, Arg2, Arg3, Arg4);
    goto loc_002E21A6;
loc_002E2185:
    result = v_stack_m1A0;
    if (v_stack_m1A0 != 0) {
        Arg2 = v_stack_m1A0;
        Arg1 = result + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(result + 1024, v_stack_m1A8, Arg3, Arg4);
loc_002E21A6:
    Arg4 = 0;
    v_stack_m1A0 = 0;
    goto loc_002E21C0;
loc_002E21B6:
loc_002E21C0:
    if (v_stack_m158 == 0) goto loc_002E22A5;
    result = 17;
    if (v_stack_m158 != 0) {
        Arg1 = v_rip + 11877983;
        result = ExfReleasePushLockShared(Arg1, v_stack_m1A8, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 11877971, v_stack_m1A8, Arg3, Arg4);
    if (v_stack_m158 != 0) goto loc_002E2213;
    result = v_stack_m128 + 152;
    if ((*(uint64_t *)(v_stack_m128 + 0x98)) != (v_stack_m128 + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 11877971, v_stack_m1A8, Arg3, Arg4);
    }
    Arg4 = 0;
loc_002E2216:
    if (v_stack_m154 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KeForceDetachProcess(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m160 + 1024;
        result = MiAttachThreadDone(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m160 != 0) {
        Arg2 = 0x77566D4DULL;
        Arg1 = v_stack_m160;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m140, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if (v_stack_m150 == 0) goto loc_002E2269;
    if ((((uint8_t)(Arg4 + 1)) & ((uint8_t)(*(uint64_t *)(v_stack_m120)))) == 0) goto loc_002E22AE;
loc_002E2269:
    if (v_stack_m118 != 0) goto loc_002E17AB;
loc_002E227A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (416);
    return result;
loc_002E22A5:
    goto loc_002E2216;
loc_002E22AE:
    result = MiDeleteTrimViewInfoList(v_stack_m118, Arg2, Arg3, Arg4);
    result = 0;
    goto loc_002E227A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E16F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
