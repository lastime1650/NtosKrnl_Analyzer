# KeReleaseMutantEx

- RVA: `0x00396850`–`0x00396E27` (길이 `1,495` bytes)
- VA: `0x0000000140396850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081268`
- 디코드: `359`개 명령, `1,495/1,495` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00396A51` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00396A6C` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00396B27` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x00396B2F` → [KiEnterDeferredReadyState](KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x00396B80` → [KiWaitSatisfyMutant](../3C/KiWaitSatisfyMutant_function_003C6490.md) (function, `0x003C6490`)
- `0x00396BAF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00396BCC` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00396C41` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00396C51` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00396C69` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00396C78` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00396C90` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00396C9F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00396CC2` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00396D3D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00396D65` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00396D80` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00396DC8` → [KiAcquireReleaseObjectRundownLockExclusive](../35/KiAcquireReleaseObjectRundownLockExclusive_function_00351A0C.md) (function, `0x00351A0C`)
- `0x00396E07` → [KeAbPreWakeupThread](../35/KeAbPreWakeupThread_function_0035034C.md) (function, `0x0035034C`)
- `0x00396E1D` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [sub_002F8BF2](../2F/Unknown_function_002F8BF2.md) at `0x002F8C18`
- [sub_002F8BF2](../2F/Unknown_function_002F8BF2.md) at `0x002F8C87`
- [WmipFindRegEntryByProviderId](../38/WmipFindRegEntryByProviderId_function_00386908.md) at `0x0038698A`
- [KeReleaseMutant](KeReleaseMutant_function_003967D0.md) at `0x003967F6`
- [KeReleaseMutex](KeReleaseMutex_function_00396810.md) at `0x00396835`
- [NtSignalAndWaitForSingleObject](../3A/NtSignalAndWaitForSingleObject_function_003A11D0.md) at `0x003A156E`
- [LdrUnloadAlternateResourceModuleEx](../45/LdrUnloadAlternateResourceModuleEx_function_00454AE4.md) at `0x00454C71`
- [LdrpGetAlternateResourceModuleHandleEx](../45/LdrpGetAlternateResourceModuleHandleEx_function_00455334.md) at `0x004554B3`
- [LdrpGetFromMUIMemCache](../45/LdrpGetFromMUIMemCache_function_00455948.md) at `0x00455B07`
- [LdrpSetAlternateResourceModuleHandle](../45/LdrpSetAlternateResourceModuleHandle_function_00455EBC.md) at `0x004562BA`
- [WmipFindRegEntryByDevice](../46/WmipFindRegEntryByDevice_function_0046C22C.md) at `0x0046C296`
- [WmipDeregisterRegEntry](../47/WmipDeregisterRegEntry_function_0047B568.md) at `0x0047B600`
- [WmipDeregisterRegEntry](../47/WmipDeregisterRegEntry_function_0047B568.md) at `0x0047B692`
- [WmipBuildTraceDeviceList](../49/WmipBuildTraceDeviceList_function_00494050.md) at `0x0049412F`
- [WmiQueryTraceProviderCount](../4A/WmiQueryTraceProviderCount_function_004A24C8.md) at `0x004A2554`
- [WmipAllocRegEntry](../4B/WmipAllocRegEntry_function_004B6D24.md) at `0x004B6E00`
- [NtReleaseMutant](../../page/9A/NtReleaseMutant_function_009A2780.md) at `0x009A2805`

### Static image references
- `0x003968A2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0039696B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00396C33` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00396E14` → [sub_006E59F0](../6E/Unknown_function_006E59F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00396850  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00396855  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00396859  55                              push rbp
0039685A  56                              push rsi
0039685B  57                              push rdi
0039685C  41 54                           push r12
0039685E  41 55                           push r13
00396860  41 56                           push r14
00396862  41 57                           push r15
00396864  48 81 EC 90 00 00 00            sub rsp, 0x90
0039686B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00396874  45 33 E4                        xor r12d, r12d
00396877  45 33 ED                        xor r13d, r13d
0039687A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0039687F  40 32 F6                        xor sil, sil
00396882  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00396887  4D 8B F9                        mov r15, r9
0039688A  41 8B E8                        mov ebp, r8d
0039688D  48 8B F9                        mov rdi, rcx
00396890  45 0F 20 C6                     mov r14, cr8
00396894  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
00396899  B8 02 00 00 00                  mov eax, 2
0039689E  44 0F 22 C0                     mov cr8, rax
003968A2  44 39 25 77 04 C3 00            cmp dword ptr [rip + 0xc30477], r12d
003968A9  0F 85 F9 02 00 00               jne 0x140396ba8
003968AF  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
003968B8  33 DB                           xor ebx, ebx
003968BA  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
003968BF  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
003968C4  0F 82 26 03 00 00               jb 0x140396bf0
003968CA  8B 5F 04                        mov ebx, dword ptr [rdi + 4]
003968CD  89 9C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ebx
003968D4  40 F6 C5 01                     test bpl, 1
003968D8  0F 85 C2 04 00 00               jne 0x140396da0
003968DE  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
003968E3  48 39 47 28                     cmp qword ptr [rdi + 0x28], rax
003968E7  0F 85 31 04 00 00               jne 0x140396d1e
003968ED  41 0F B6 80 BA 38 00 00         movzx eax, byte ptr [r8 + 0x38ba]
003968F5  38 47 02                        cmp byte ptr [rdi + 2], al
003968F8  0F 85 20 04 00 00               jne 0x140396d1e
003968FE  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00396901  4C 8D 77 28                     lea r14, [rdi + 0x28]
00396905  40 88 B4 24 E0 00 00 00         mov byte ptr [rsp + 0xe0], sil
0039690D  8D 41 01                        lea eax, [rcx + 1]
00396910  89 47 04                        mov dword ptr [rdi + 4], eax
00396913  85 C9                           test ecx, ecx
00396915  0F 85 BE 00 00 00               jne 0x1403969d9
0039691B  85 DB                           test ebx, ebx
0039691D  0F 8F B6 00 00 00               jg 0x1403969d9
00396923  33 C0                           xor eax, eax
00396925  0F 57 C0                        xorps xmm0, xmm0
00396928  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00396930  33 DB                           xor ebx, ebx
00396932  8B 07                           mov eax, dword ptr [rdi]
00396934  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00396939  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0039693D  40 88 74 24 72                  mov byte ptr [rsp + 0x72], sil
00396942  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00396946  89 07                           mov dword ptr [rdi], eax
00396948  0F B6 47 31                     movzx eax, byte ptr [rdi + 0x31]
0039694C  4D 8B 2E                        mov r13, qword ptr [r14]
0039694F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00396953  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00396958  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00396960  F0 49 0F BA 6D 40 00            lock bts qword ptr [r13 + 0x40], 0
00396967  73 1B                           jae 0x140396984
00396969  FF C3                           inc ebx
0039696B  85 1D 3B E9 C2 00               test dword ptr [rip + 0xc2e93b], ebx
00396971  0F 84 E4 02 00 00               je 0x140396c5b
00396977  F3 90                           pause
00396979  49 8B 45 40                     mov rax, qword ptr [r13 + 0x40]
0039697D  48 85 C0                        test rax, rax
00396980  74 DE                           je 0x140396960
00396982  EB E5                           jmp 0x140396969
00396984  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00396988  48 8D 47 18                     lea rax, [rdi + 0x18]
0039698C  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00396990  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00396994  75 3C                           jne 0x1403969d2
00396996  48 39 01                        cmp qword ptr [rcx], rax
00396999  75 37                           jne 0x1403969d2
0039699B  48 89 11                        mov qword ptr [rcx], rdx
0039699E  48 8D 47 08                     lea rax, [rdi + 8]
003969A2  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003969A6  4D 89 65 40                     mov qword ptr [r13 + 0x40], r12
003969AA  4D 89 26                        mov qword ptr [r14], r12
003969AD  4C 8B 20                        mov r12, qword ptr [rax]
003969B0  4C 3B E0                        cmp r12, rax
003969B3  74 37                           je 0x1403969ec
003969B5  49 8B 04 24                     mov rax, qword ptr [r12]
003969B9  49 8B F4                        mov rsi, r12
003969BC  4C 8B E0                        mov r12, rax
003969BF  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
003969C3  48 39 70 08                     cmp qword ptr [rax + 8], rsi
003969C7  75 09                           jne 0x1403969d2
003969C9  48 39 31                        cmp qword ptr [rcx], rsi
003969CC  0F 84 C5 00 00 00               je 0x140396a97
003969D2  B9 03 00 00 00                  mov ecx, 3
003969D7  CD 29                           int 0x29
003969D9  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
003969E0  EB 47                           jmp 0x140396a29
003969E2  83 6F 04 01                     sub dword ptr [rdi + 4], 1
003969E6  0F 85 D0 03 00 00               jne 0x140396dbc
003969EC  0F B6 5F 30                     movzx ebx, byte ptr [rdi + 0x30]
003969F0  80 E3 02                        and bl, 2
003969F3  41 0F 95 C6                     setne r14b
003969F7  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
003969FE  80 BC 24 E0 00 00 00 00         cmp byte ptr [rsp + 0xe0], 0
00396A06  0F 85 B9 03 00 00               jne 0x140396dc5
00396A0C  41 0F B6 F6                     movzx esi, r14b
00396A10  84 DB                           test bl, bl
00396A12  0F 85 BA 03 00 00               jne 0x140396dd2
00396A18  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00396A1D  8B 9C 24 D0 00 00 00            mov ebx, dword ptr [rsp + 0xd0]
00396A24  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
00396A29  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00396A2E  40 80 E5 02                     and bpl, 2
00396A32  44 8B 8C 24 D8 00 00 00         mov r9d, dword ptr [rsp + 0xd8]
00396A3A  40 F6 DD                        neg bpl
00396A3D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00396A42  41 B8 01 00 00 00               mov r8d, 1
00396A48  1B D2                           sbb edx, edx
00396A4A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00396A4E  83 E2 03                        and edx, 3
00396A51  E8 9A B2 EB FF                  call 0x140251cf0
00396A56  40 84 F6                        test sil, sil
00396A59  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00396A5E  0F 85 AD 03 00 00               jne 0x140396e11
00396A64  45 85 E4                        test r12d, r12d
00396A67  74 08                           je 0x140396a71
00396A69  48 8B CE                        mov rcx, rsi
00396A6C  E8 9F 85 EC FF                  call 0x14025f010
00396A71  4D 85 FF                        test r15, r15
00396A74  74 03                           je 0x140396a79
00396A76  41 89 1F                        mov dword ptr [r15], ebx
00396A79  33 C0                           xor eax, eax
00396A7B  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00396A83  48 81 C4 90 00 00 00            add rsp, 0x90
00396A8A  41 5F                           pop r15
00396A8C  41 5E                           pop r14
00396A8E  41 5D                           pop r13
00396A90  41 5C                           pop r12
00396A92  5F                              pop rdi
00396A93  5E                              pop rsi
00396A94  5D                              pop rbp
00396A95  C3                              ret
00396A96  CC                              int3
00396A97  48 89 01                        mov qword ptr [rcx], rax
00396A9A  48 89 48 08                     mov qword ptr [rax + 8], rcx
00396A9E  0F B6 46 10                     movzx eax, byte ptr [rsi + 0x10]
00396AA2  3C 01                           cmp al, 1
00396AA4  0F 85 0F 01 00 00               jne 0x140396bb9
00396AAA  0F B7 56 12                     movzx edx, word ptr [rsi + 0x12]
00396AAE  45 32 ED                        xor r13b, r13b
00396AB1  48 8B 5E 18                     mov rbx, qword ptr [rsi + 0x18]
00396AB5  45 33 F6                        xor r14d, r14d
00396AB8  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00396ABD  0F 1F 00                        nop dword ptr [rax]
00396AC0  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00396AC7  73 1D                           jae 0x140396ae6
00396AC9  41 FF C6                        inc r14d
00396ACC  44 85 35 D9 E7 C2 00            test dword ptr [rip + 0xc2e7d9], r14d
00396AD3  0F 84 5A 01 00 00               je 0x140396c33
00396AD9  F3 90                           pause
00396ADB  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00396ADF  48 85 C0                        test rax, rax
00396AE2  74 DC                           je 0x140396ac0
00396AE4  EB E3                           jmp 0x140396ac9
00396AE6  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00396AED  3C 05                           cmp al, 5
00396AEF  0F 85 90 00 00 00               jne 0x140396b85
00396AF5  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
00396AF9  8B C1                           mov eax, ecx
00396AFB  83 E0 07                        and eax, 7
00396AFE  83 F8 01                        cmp eax, 1
00396B01  0F 85 C9 01 00 00               jne 0x140396cd0
00396B07  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00396B0E  48 85 D2                        test rdx, rdx
00396B11  74 11                           je 0x140396b24
00396B13  0F B6 02                        movzx eax, byte ptr [rdx]
00396B16  24 7F                           and al, 0x7f
00396B18  3C 15                           cmp al, 0x15
00396B1A  0F 84 F7 00 00 00               je 0x140396c17
00396B20  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00396B24  48 8B CB                        mov rcx, rbx
00396B27  E8 A4 97 EB FF                  call 0x1402502d0
00396B2C  48 8B CB                        mov rcx, rbx
00396B2F  E8 EC 08 00 00                  call 0x140397420
00396B34  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00396B39  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00396B40  49 8B 80 08 2D 00 00            mov rax, qword ptr [r8 + 0x2d08]
00396B47  48 89 01                        mov qword ptr [rcx], rax
00396B4A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00396B4F  49 89 88 08 2D 00 00            mov qword ptr [r8 + 0x2d08], rcx
00396B56  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00396B5D  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
00396B68  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00396B6C  41 B5 01                        mov r13b, 1
00396B6F  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00396B74  0F B6 01                        movzx eax, byte ptr [rcx]
00396B77  24 7F                           and al, 0x7f
00396B79  3C 02                           cmp al, 2
00396B7B  75 08                           jne 0x140396b85
00396B7D  48 8B D3                        mov rdx, rbx
00396B80  E8 0B F9 02 00                  call 0x1403c6490
00396B85  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
00396B8D  0F B6 46 11                     movzx eax, byte ptr [rsi + 0x11]
00396B91  FE C0                           inc al
00396B93  88 46 11                        mov byte ptr [rsi + 0x11], al
00396B96  48 8D 47 08                     lea rax, [rdi + 8]
00396B9A  45 84 ED                        test r13b, r13b
00396B9D  0F 84 0D FE FF FF               je 0x1403969b0
00396BA3  E9 3A FE FF FF                  jmp 0x1403969e2
00396BA8  0F B6 D0                        movzx edx, al
00396BAB  41 0F B6 CE                     movzx ecx, r14b
00396BAF  E8 48 EB 15 00                  call 0x1404f56fc
00396BB4  E9 F6 FC FF FF                  jmp 0x1403968af
00396BB9  3C 02                           cmp al, 2
00396BBB  0F 85 E8 00 00 00               jne 0x140396ca9
00396BC1  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
00396BC5  48 8B D6                        mov rdx, rsi
00396BC8  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00396BCC  E8 5F 2F E8 FF                  call 0x140219b30
00396BD1  83 6F 04 01                     sub dword ptr [rdi + 4], 1
00396BD5  0F 84 11 FE FF FF               je 0x1403969ec
00396BDB  48 8D 47 08                     lea rax, [rdi + 8]
00396BDF  E9 CC FD FF FF                  jmp 0x1403969b0
00396BE4  0F 1F 40 00                     nop dword ptr [rax]
00396BE8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00396BF0  FF C3                           inc ebx
00396BF2  85 1D B4 E6 C2 00               test dword ptr [rip + 0xc2e6b4], ebx
00396BF8  0F 84 84 00 00 00               je 0x140396c82
00396BFE  F3 90                           pause
00396C00  8B 07                           mov eax, dword ptr [rdi]
00396C02  84 C0                           test al, al
00396C04  78 EA                           js 0x140396bf0
00396C06  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00396C0B  72 E3                           jb 0x140396bf0
00396C0D  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00396C12  E9 B3 FC FF FF                  jmp 0x1403968ca
00396C17  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
00396C1D  0F B6 C0                        movzx eax, al
00396C20  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
00396C26  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
00396C2E  E9 F1 FE FF FF                  jmp 0x140396b24
00396C33  8B 05 7F FE C2 00               mov eax, dword ptr [rip + 0xc2fe7f]
00396C39  A8 40                           test al, 0x40
00396C3B  0F 84 98 FE FF FF               je 0x140396ad9
00396C41  E8 4A 88 F7 FF                  call 0x14030f490
00396C46  84 C0                           test al, al
00396C48  0F 84 8B FE FF FF               je 0x140396ad9
00396C4E  41 8B CE                        mov ecx, r14d
00396C51  E8 0A 88 F7 FF                  call 0x14030f460
00396C56  E9 80 FE FF FF                  jmp 0x140396adb
00396C5B  8B 05 57 FE C2 00               mov eax, dword ptr [rip + 0xc2fe57]
00396C61  A8 40                           test al, 0x40
00396C63  0F 84 0E FD FF FF               je 0x140396977
00396C69  E8 22 88 F7 FF                  call 0x14030f490
00396C6E  84 C0                           test al, al
00396C70  0F 84 01 FD FF FF               je 0x140396977
00396C76  8B CB                           mov ecx, ebx
00396C78  E8 E3 87 F7 FF                  call 0x14030f460
00396C7D  E9 F7 FC FF FF                  jmp 0x140396979
00396C82  8B 05 30 FE C2 00               mov eax, dword ptr [rip + 0xc2fe30]
00396C88  A8 40                           test al, 0x40
00396C8A  0F 84 6E FF FF FF               je 0x140396bfe
00396C90  E8 FB 87 F7 FF                  call 0x14030f490
00396C95  84 C0                           test al, al
00396C97  0F 84 61 FF FF FF               je 0x140396bfe
00396C9D  8B CB                           mov ecx, ebx
00396C9F  E8 BC 87 F7 FF                  call 0x14030f460
00396CA4  E9 57 FF FF FF                  jmp 0x140396c00
00396CA9  3C 04                           cmp al, 4
00396CAB  0F 84 BA 00 00 00               je 0x140396d6b
00396CB1  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00396CB6  45 33 C9                        xor r9d, r9d
00396CB9  41 B8 00 01 00 00               mov r8d, 0x100
00396CBF  48 8B D6                        mov rdx, rsi
00396CC2  E8 09 9A FB FF                  call 0x1403506d0
00396CC7  48 8D 47 08                     lea rax, [rdi + 8]
00396CCB  E9 E0 FC FF FF                  jmp 0x1403969b0
00396CD0  83 F8 04                        cmp eax, 4
00396CD3  0F 84 2E FE FF FF               je 0x140396b07
00396CD9  85 C0                           test eax, eax
00396CDB  75 2E                           jne 0x140396d0b
00396CDD  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00396CE2  80 E1 FA                        and cl, 0xfa
00396CE5  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00396CEA  80 C9 02                        or cl, 2
00396CED  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00396CF0  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00396CF7  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
00396D02  44 88 6E 11                     mov byte ptr [rsi + 0x11], r13b
00396D06  E9 5D FE FF FF                  jmp 0x140396b68
00396D0B  83 F8 05                        cmp eax, 5
00396D0E  75 7E                           jne 0x140396d8e
00396D10  80 E1 FE                        and cl, 0xfe
00396D13  80 C9 06                        or cl, 6
00396D16  88 4B 70                        mov byte ptr [rbx + 0x70], cl
00396D19  E9 67 FE FF FF                  jmp 0x140396b85
00396D1E  0F B6 5F 30                     movzx ebx, byte ptr [rdi + 0x30]
00396D22  80 E3 01                        and bl, 1
00396D25  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00396D2C  44 39 25 ED FF C2 00            cmp dword ptr [rip + 0xc2ffed], r12d
00396D33  74 0D                           je 0x140396d42
00396D35  44 0F 20 C1                     mov rcx, cr8
00396D39  41 0F B6 D6                     movzx edx, r14b
00396D3D  E8 56 E9 15 00                  call 0x1404f5698
00396D42  41 0F B6 C6                     movzx eax, r14b
00396D46  44 0F 22 C0                     mov cr8, rax
00396D4A  84 DB                           test bl, bl
00396D4C  B8 80 00 00 00                  mov eax, 0x80
00396D51  B9 46 00 00 C0                  mov ecx, 0xc0000046
00396D56  0F 44 C1                        cmove eax, ecx
00396D59  40 F6 C5 04                     test bpl, 4
00396D5D  0F 84 18 FD FF FF               je 0x140396a7b
00396D63  8B C8                           mov ecx, eax
00396D65  E8 E6 FC F5 FF                  call 0x1402f6a50
00396D6A  CC                              int3
00396D6B  C6 46 11 05                     mov byte ptr [rsi + 0x11], 5
00396D6F  4C 8B C6                        mov r8, rsi
00396D72  C7 47 04 00 00 00 00            mov dword ptr [rdi + 4], 0
00396D79  48 8B D7                        mov rdx, rdi
00396D7C  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00396D80  E8 CB 0E E7 FF                  call 0x140207c50
00396D85  48 8D 47 08                     lea rax, [rdi + 8]
00396D89  E9 22 FC FF FF                  jmp 0x1403969b0
00396D8E  83 F8 03                        cmp eax, 3
00396D91  0F 85 EE FD FF FF               jne 0x140396b85
00396D97  C6 46 11 02                     mov byte ptr [rsi + 0x11], 2
00396D9B  E9 E5 FD FF FF                  jmp 0x140396b85
00396DA0  80 4F 30 01                     or byte ptr [rdi + 0x30], 1
00396DA4  4C 8D 77 28                     lea r14, [rdi + 0x28]
00396DA8  C6 84 24 E0 00 00 00 01         mov byte ptr [rsp + 0xe0], 1
00396DB0  C7 47 04 01 00 00 00            mov dword ptr [rdi + 4], 1
00396DB7  E9 5F FB FF FF                  jmp 0x14039691b
00396DBC  48 8D 47 08                     lea rax, [rdi + 8]
00396DC0  E9 EB FB FF FF                  jmp 0x1403969b0
00396DC5  48 8B CF                        mov rcx, rdi
00396DC8  E8 3F AC FB FF                  call 0x140351a0c
00396DCD  E9 3A FC FF FF                  jmp 0x140396a0c
00396DD2  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00396DD7  48 85 C9                        test rcx, rcx
00396DDA  0F 84 38 FC FF FF               je 0x140396a18
00396DE0  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00396DE5  48 8B 80 08 2D 00 00            mov rax, qword ptr [rax + 0x2d08]
00396DEC  48 85 C0                        test rax, rax
00396DEF  0F 84 23 FC FF FF               je 0x140396a18
00396DF5  48 05 28 FF FF FF               add rax, -0xd8
00396DFB  48 3B C8                        cmp rcx, rax
00396DFE  0F 85 14 FC FF FF               jne 0x140396a18
00396E04  48 8B D7                        mov rdx, rdi
00396E07  E8 40 95 FB FF                  call 0x14035034c
00396E0C  E9 07 FC FF FF                  jmp 0x140396a18
00396E11  4C 3B EE                        cmp r13, rsi
00396E14  0F 85 D6 EB 34 00               jne 0x1406e59f0
00396E1A  48 8B CF                        mov rcx, rdi
00396E1D  E8 DE A7 F4 FF                  call 0x1402e1600
00396E22  E9 3D FC FF FF                  jmp 0x140396a64
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReleaseMutantEx(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m56;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pE0;

    v_stack_p20 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (144);
    v_r12 = 0;
    v_r13 = 0;
    v_stack_m80 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m60 = v_cr8;
    if ((*(unsigned int *)(v_rip + 12780663)) != 0) goto loc_00396BA8;
loc_003968AF:
    v_rbx = 0;
    v_stack_m90 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (condition_is_below) goto loc_00396BF0;
loc_003968CA:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) != 0) goto loc_00396DA0;
    if ((*(unsigned __int64 *)(a1 + 40)) != v_stack_m80) goto loc_00396D1E;
    if ((*(unsigned __int8 *)(a1 + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14522)))) goto loc_00396D1E;
    v_stack_p18 = 0;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) goto loc_003969D9;
loc_0039691B:
    if (condition_is_greater) goto loc_003969D9;
    result = 0;
    v_stack_m48 = 0;
    v_rbx = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m56 = 0;
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(v_stack_m58));
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(a1 + 49));
    v_stack_m88 = *(unsigned __int64 *)(a1 + 40);
loc_00396960:
    if (condition_is_above_or_equal) goto loc_00396984;
loc_00396969:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 12773691)) & ((unsigned int)(v_rbx))) == 0) goto loc_00396C5B;
loc_00396977:
loc_00396979:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 64) == 0) goto loc_00396960;
    goto loc_00396969;
loc_00396984:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8)) != (a1 + 24)) goto loc_003969D2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) != (a1 + 24)) goto loc_003969D2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8)) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8) = *(unsigned __int64 *)(a1 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 64) = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
loc_003969B0:
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_003969EC;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_003969D2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 8))) goto loc_00396A97;
loc_003969D2:
loc_003969D9:
    goto loc_00396A29;
loc_003969E2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) != (*(unsigned __int64 *)(a1 + 8))) goto loc_00396DBC;
loc_003969EC:
    v_rbx = (unsigned __int8)((*(unsigned __int8 *)(a1 + 48)) & (2));
    v_r14 = (condition_is_not_equal) ? 1 : 0;
    if (v_stack_p18 != 0) goto loc_00396DC5;
loc_00396A0C:
    if ((unsigned __int8)(v_rbx) != 0) goto loc_00396DD2;
loc_00396A18:
loc_00396A29:
    v_rbp = (unsigned __int8)(((unsigned int)(a3)) & (2));
    v_rbp = (unsigned __int8)(-(v_rbp));
    v_stack_mA8 = (unsigned __int8)(v_stack_m60);
    a2 = (unsigned int)((*(unsigned __int64 *)(a1 + 24)) & (3));
    result = KiExitDispatcher(v_stack_m90, a2, 1, (unsigned int)(v_stack_p10));
    if ((unsigned __int8)((unsigned __int8)(v_r14)) != 0) goto loc_00396E11;
loc_00396A64:
    if ((unsigned int)((unsigned int)(v_stack_m98)) != 0) {
        a1 = v_stack_m80;
        result = KiLeaveCriticalRegionUnsafe(a1, a2, 1, (unsigned int)(v_stack_p10));
    }
    if (a4 != 0) {
        *(unsigned int *)(a4) = (unsigned int)((unsigned int)(v_stack_p8));
    }
    result = 0;
loc_00396A7B:
    v_rsp = (v_rsp) + (144);
    return result;
loc_00396A97:
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(result + 8) = a1;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m80 + 16))) != 1) goto loc_00396BB9;
    v_r13 = 0;
    v_r14 = 0;
    v_stack_p50 = *(unsigned __int16 *)(v_stack_m80 + 18);
loc_00396AC0:
    if (condition_is_above_or_equal) goto loc_00396AE6;
loc_00396AC9:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 12773337)) & ((unsigned int)(v_r14))) == 0) goto loc_00396C33;
loc_00396AD9:
loc_00396ADB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 64) == 0) goto loc_00396AC0;
    goto loc_00396AC9;
loc_00396AE6:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 388))) != 5) goto loc_00396B85;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_00396CD0;
loc_00396B07:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 232) == 0) goto loc_00396B24;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00396C17;
loc_00396B24:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(v_stack_m80 + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 232), 1, (unsigned int)(v_stack_p10));
    result = KiEnterDeferredReadyState(*(unsigned __int64 *)(v_stack_m80 + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 232), 1, (unsigned int)(v_stack_p10));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 216) = *(unsigned __int64 *)(v_stack_p38 + 11528);
    *(unsigned __int64 *)(v_stack_p38 + 11528) = *(unsigned __int64 *)(v_stack_m80 + 24) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 200) = v_stack_p50;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 976) = 0;
loc_00396B68:
    v_stack_p58 = *(unsigned __int64 *)(v_stack_m80 + 24);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m80 + 32))) & (127));
    if (((unsigned __int8)(result)) == 2) {
        a2 = *(unsigned __int64 *)(v_stack_m80 + 24);
        result = KiWaitSatisfyMutant(*(unsigned __int64 *)(v_stack_m80 + 32), a2, v_stack_p38, (unsigned int)(v_stack_p10));
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 24) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m80 + 17)) + 1);
    *(unsigned __int8 *)(v_stack_m80 + 17) = (unsigned __int8)(result);
    if (1 == 0) goto loc_003969B0;
    goto loc_003969E2;
loc_00396BA8:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r14), (unsigned __int8)(a1 + 8), v_stack_p38, (unsigned int)(v_stack_p10));
    goto loc_003968AF;
loc_00396BB9:
    if (((unsigned __int8)(result)) != 2) goto loc_00396CA9;
    *(unsigned __int8 *)(v_stack_m80 + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(v_stack_m80 + 24), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    if (((unsigned __int8)(result)) == 2) goto loc_003969EC;
    goto loc_003969B0;
loc_00396BF0:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_stack_m80 + 24)) + 1);
    if (((*(unsigned int *)(v_rip + 12773044)) & ((unsigned int)(v_rbx))) == 0) goto loc_00396C82;
loc_00396BFE:
loc_00396C00:
    if (sign_flag) goto loc_00396BF0;
    if (condition_is_below) goto loc_00396BF0;
    goto loc_003968CA;
loc_00396C17:
    *(unsigned int *)(v_rbx + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 540))));
    goto loc_00396B24;
loc_00396C33:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12779135)))) & (64)) == 0) goto loc_00396AD9;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_stack_m80 + 24), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    if ((unsigned __int8)(result) == 0) goto loc_00396AD9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    goto loc_00396ADB;
loc_00396C5B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12779095)))) & (64)) == 0) goto loc_00396977;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    if ((unsigned __int8)(result) == 0) goto loc_00396977;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    goto loc_00396979;
loc_00396C82:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12779056)))) & (64)) == 0) goto loc_00396BFE;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    if ((unsigned __int8)(result) == 0) goto loc_00396BFE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_m80, v_stack_p38, (unsigned int)(v_stack_p10));
    goto loc_00396C00;
loc_00396CA9:
    if (((unsigned __int8)(result)) == 4) goto loc_00396D6B;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_p38, v_stack_m80, 256, a4);
    goto loc_003969B0;
loc_00396CD0:
    if (((unsigned int)(a1 + 8)) == 4) goto loc_00396B07;
    if ((unsigned int)(a1 + 8) != 0) goto loc_00396D0B;
    a1 = (unsigned __int8)((v_stack_p38) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_rbx + 112) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_rbx + 200) = v_stack_p50;
    *(unsigned __int64 *)(v_rbx + 976) = 0;
    *(unsigned __int8 *)(v_stack_m80 + 17) = 1;
    goto loc_00396B68;
loc_00396D0B:
    if (((unsigned int)(v_stack_p50)) != 5) goto loc_00396D8E;
    a1 = (unsigned __int8)((a1) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_rbx + 112) = (unsigned __int8)(a1);
    goto loc_00396B85;
loc_00396D1E:
    v_rbx = (unsigned __int8)((*(unsigned __int8 *)(a1 + 48)) & (1));
    result = v_stack_p50;
    if ((*(unsigned int *)(v_rip + 12779501)) != ((unsigned int)((unsigned int)(v_stack_m98)))) {
        a1 = 2;
        a2 = (unsigned __int8)(v_r14);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p38, a4);
    }
    result = 128;
    if ((unsigned __int8)(v_rbx) == 0) { result = (unsigned int)((unsigned int)(0xC0000046ULL)); }
    if ((((unsigned __int8)(v_rbp)) & (4)) == 0) goto loc_00396A7B;
    result = RtlRaiseStatus((unsigned int)((unsigned int)(result)), a2, v_stack_p38, a4);
loc_00396D6B:
    *(unsigned __int8 *)(v_stack_m80 + 17) = 5;
    *(unsigned int *)(a1 + 4) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(v_stack_m80 + 24), a1, v_stack_m80, a4);
    goto loc_003969B0;
loc_00396D8E:
    if (((unsigned int)(a1 + 8)) != 3) goto loc_00396B85;
    *(unsigned __int8 *)(v_stack_m80 + 17) = 2;
    goto loc_00396B85;
loc_00396DA0:
    v_stack_pE0 = 1;
    *(unsigned int *)(a1 + 4) = 1;
    goto loc_0039691B;
loc_00396DBC:
    goto loc_003969B0;
loc_00396DC5:
    result = KiAcquireReleaseObjectRundownLockExclusive(a1, a1, v_stack_m80, a4);
    goto loc_00396A0C;
loc_00396DD2:
    if (v_stack_p58 == 0) goto loc_00396A18;
    if (*(unsigned __int64 *)(v_stack_p38 + 11528) == 0) goto loc_00396A18;
    result = (*(unsigned __int64 *)(v_stack_p38 + 11528)) + (-216);
    if (v_stack_p58 != result) goto loc_00396A18;
    result = KeAbPreWakeupThread(v_stack_p58, a1, v_stack_m80, a4);
    goto loc_00396A18;
loc_00396E11:
    result = KeAbPostRelease(a1, a1, v_stack_m80, a4);
    goto loc_00396A64;
}
```

## 5. (Beta) C Style

```c
int64_t KeReleaseMutantEx(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint8_t v_stack_m56;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint8_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p8;
    uint8_t v_stack_pE0;

    v_stack_p20 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (144);
    local_r12 = 0;
    local_r13 = 0;
    v_stack_m80 = *(uint64_t *)(gs_base + (0 + 0x188));
    local_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m60 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC30477)) != 0) goto loc_00396BA8;
loc_003968AF:
    local_rbx = 0;
    v_stack_m90 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (condition_is_below) goto loc_00396BF0;
loc_003968CA:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) != 0) goto loc_00396DA0;
    if ((*(uint64_t *)(arg1 + 0x28)) != v_stack_m80) goto loc_00396D1E;
    if ((*(uint8_t *)(arg1 + 0x2)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BA)))) goto loc_00396D1E;
    v_stack_p18 = 0;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) goto loc_003969D9;
loc_0039691B:
    if (condition_is_greater) goto loc_003969D9;
    result = 0;
    v_stack_m48 = 0;
    local_rbx = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m56 = 0;
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(v_stack_m58));
    v_stack_m98 = (uint32_t)(*(uint8_t *)(arg1 + 0x31));
    v_stack_m88 = *(uint64_t *)(arg1 + 0x28);
loc_00396960:
    if (condition_is_above_or_equal) goto loc_00396984;
loc_00396969:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2E93B)) & ((uint32_t)(local_rbx))) == 0) goto loc_00396C5B;
loc_00396977:
loc_00396979:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x40) == 0) goto loc_00396960;
    goto loc_00396969;
loc_00396984:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)) != (Arg1 + 24)) goto loc_003969D2;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) != (Arg1 + 24)) goto loc_003969D2;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8)) = *(uint64_t *)(arg1 + 0x18);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8) = *(uint64_t *)(arg1 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x40) = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
loc_003969B0:
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_003969EC;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_003969D2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x8))) goto loc_00396A97;
loc_003969D2:
loc_003969D9:
    goto loc_00396A29;
loc_003969E2:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) != (*(uint64_t *)(arg1 + 0x8))) goto loc_00396DBC;
loc_003969EC:
    local_rbx = (uint8_t)((*(uint8_t *)(arg1 + 0x30)) & (2));
    local_r14 = (condition_is_not_equal) ? 1 : 0;
    if (v_stack_p18 != 0) goto loc_00396DC5;
loc_00396A0C:
    if ((uint8_t)(local_rbx) != 0) goto loc_00396DD2;
loc_00396A18:
loc_00396A29:
    local_rbp = (uint8_t)(((uint32_t)(Arg3)) & (2));
    local_rbp = (uint8_t)(-(local_rbp));
    v_stack_mA8 = (uint8_t)(v_stack_m60);
    Arg2 = (uint32_t)((*(uint64_t *)(arg1 + 0x18)) & (3));
    result = KiExitDispatcher(v_stack_m90, Arg2, 1, (uint32_t)(v_stack_p10));
    if ((uint8_t)((uint8_t)(local_r14)) != 0) goto loc_00396E11;
loc_00396A64:
    if ((uint32_t)((uint32_t)(v_stack_m98)) != 0) {
        Arg1 = v_stack_m80;
        result = KiLeaveCriticalRegionUnsafe(Arg1, Arg2, 1, (uint32_t)(v_stack_p10));
    }
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = (uint32_t)((uint32_t)(v_stack_p8));
    }
    result = 0;
loc_00396A7B:
    local_rsp = (local_rsp) + (144);
    return result;
loc_00396A97:
    *(uint64_t *)(arg1) = 0;
    *(void **)(result + 0x8) = Arg1;
    if (((uint8_t)(*(uint8_t *)(v_stack_m80 + 0x10))) != 1) goto loc_00396BB9;
    local_r13 = 0;
    local_r14 = 0;
    v_stack_p50 = *(uint16_t *)(v_stack_m80 + 0x12);
loc_00396AC0:
    if (condition_is_above_or_equal) goto loc_00396AE6;
loc_00396AC9:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2E7D9)) & ((uint32_t)(local_r14))) == 0) goto loc_00396C33;
loc_00396AD9:
loc_00396ADB:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0x40) == 0) goto loc_00396AC0;
    goto loc_00396AC9;
loc_00396AE6:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0x184))) != 5) goto loc_00396B85;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_00396CD0;
loc_00396B07:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xE8) == 0) goto loc_00396B24;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00396C17;
loc_00396B24:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(v_stack_m80 + 0x18), *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xE8), 1, (uint32_t)(v_stack_p10));
    result = KiEnterDeferredReadyState(*(uint64_t *)(v_stack_m80 + 0x18), *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xE8), 1, (uint32_t)(v_stack_p10));
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xD8) = *(uint64_t *)(v_stack_p38 + 0x2D08);
    *(uint64_t *)(v_stack_p38 + 0x2D08) = *(uint64_t *)(v_stack_m80 + 0x18) + 216;
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0xC8) = v_stack_p50;
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0x3D0) = 0;
loc_00396B68:
    v_stack_p58 = *(uint64_t *)(v_stack_m80 + 0x18);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m80 + 0x20))) & (127));
    if (((uint8_t)(result)) == 2) {
        Arg2 = *(uint64_t *)(v_stack_m80 + 0x18);
        result = KiWaitSatisfyMutant(*(uint64_t *)(v_stack_m80 + 0x20), Arg2, v_stack_p38, (uint32_t)(v_stack_p10));
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x18) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_m80 + 0x11)) + 1);
    *(uint8_t *)(v_stack_m80 + 0x11) = (uint8_t)(result);
    if (1 == 0) goto loc_003969B0;
    goto loc_003969E2;
loc_00396BA8:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r14), (uint8_t)(Arg1 + 8), v_stack_p38, (uint32_t)(v_stack_p10));
    goto loc_003968AF;
loc_00396BB9:
    if (((uint8_t)(result)) != 2) goto loc_00396CA9;
    *(uint8_t *)(v_stack_m80 + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(v_stack_m80 + 0x18), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    if (((uint8_t)(result)) == 2) goto loc_003969EC;
    goto loc_003969B0;
loc_00396BF0:
    local_rbx = (uint32_t)((*(uint64_t *)(v_stack_m80 + 0x18)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2E6B4)) & ((uint32_t)(local_rbx))) == 0) goto loc_00396C82;
loc_00396BFE:
loc_00396C00:
    if (sign_flag) goto loc_00396BF0;
    if (condition_is_below) goto loc_00396BF0;
    goto loc_003968CA;
loc_00396C17:
    *(uint32_t *)(local_rbx + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x21C))));
    goto loc_00396B24;
loc_00396C33:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2FE7F)))) & (64)) == 0) goto loc_00396AD9;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_stack_m80 + 0x18), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    if ((uint8_t)(result) == 0) goto loc_00396AD9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    goto loc_00396ADB;
loc_00396C5B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2FE57)))) & (64)) == 0) goto loc_00396977;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    if ((uint8_t)(result) == 0) goto loc_00396977;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    goto loc_00396979;
loc_00396C82:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2FE30)))) & (64)) == 0) goto loc_00396BFE;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    if ((uint8_t)(result) == 0) goto loc_00396BFE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_m80, v_stack_p38, (uint32_t)(v_stack_p10));
    goto loc_00396C00;
loc_00396CA9:
    if (((uint8_t)(result)) == 4) goto loc_00396D6B;
    Arg4 = 0;
    result = KiTryUnwaitThread(v_stack_p38, v_stack_m80, 256, Arg4);
    goto loc_003969B0;
loc_00396CD0:
    if (((uint32_t)(Arg1 + 8)) == 4) goto loc_00396B07;
    if ((uint32_t)(Arg1 + 8) != 0) goto loc_00396D0B;
    Arg1 = (uint8_t)((v_stack_p38) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(local_rbx + 0x70) = (uint8_t)(Arg1);
    *(uint64_t *)(local_rbx + 0xC8) = v_stack_p50;
    *(uint64_t *)(local_rbx + 0x3D0) = 0;
    *(uint8_t *)(v_stack_m80 + 0x11) = 1;
    goto loc_00396B68;
loc_00396D0B:
    if (((uint32_t)(v_stack_p50)) != 5) goto loc_00396D8E;
    Arg1 = (uint8_t)((Arg1) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(local_rbx + 0x70) = (uint8_t)(Arg1);
    goto loc_00396B85;
loc_00396D1E:
    local_rbx = (uint8_t)((*(uint8_t *)(arg1 + 0x30)) & (1));
    result = v_stack_p50;
    if ((*(uint32_t *)(v_rip + 0xC2FFED)) != ((uint32_t)((uint32_t)(v_stack_m98)))) {
        Arg1 = 2;
        Arg2 = (uint8_t)(local_r14);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p38, Arg4);
    }
    result = 128;
    if ((uint8_t)(local_rbx) == 0) { result = (uint32_t)((uint32_t)(0xC0000046ULL)); }
    if ((((uint8_t)(local_rbp)) & (4)) == 0) goto loc_00396A7B;
    result = RtlRaiseStatus((uint32_t)((uint32_t)(result)), Arg2, v_stack_p38, Arg4);
loc_00396D6B:
    *(uint8_t *)(v_stack_m80 + 0x11) = 5;
    *(uint32_t *)(arg1 + 0x4) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(v_stack_m80 + 0x18), Arg1, v_stack_m80, Arg4);
    goto loc_003969B0;
loc_00396D8E:
    if (((uint32_t)(Arg1 + 8)) != 3) goto loc_00396B85;
    *(uint8_t *)(v_stack_m80 + 0x11) = 2;
    goto loc_00396B85;
loc_00396DA0:
    v_stack_pE0 = 1;
    *(uint32_t *)(arg1 + 0x4) = 1;
    goto loc_0039691B;
loc_00396DBC:
    goto loc_003969B0;
loc_00396DC5:
    result = KiAcquireReleaseObjectRundownLockExclusive(Arg1, Arg1, v_stack_m80, Arg4);
    goto loc_00396A0C;
loc_00396DD2:
    if (v_stack_p58 == 0) goto loc_00396A18;
    if (*(uint64_t *)(v_stack_p38 + 0x2D08) == 0) goto loc_00396A18;
    result = (*(uint64_t *)(v_stack_p38 + 0x2D08)) + (-216);
    if (v_stack_p58 != result) goto loc_00396A18;
    result = KeAbPreWakeupThread(v_stack_p58, Arg1, v_stack_m80, Arg4);
    goto loc_00396A18;
loc_00396E11:
    result = KeAbPostRelease(Arg1, Arg1, v_stack_m80, Arg4);
    goto loc_00396A64;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `8` | `R` |
| `Arg1` | `+ 0x30` | `8` | `R/W` |
| `Arg1` | `+ 0x31` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00396850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
