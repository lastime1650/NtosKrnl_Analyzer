# CcLazyWriteScanVolume

- RVA: `0x00388DC0`–`0x00389586` (길이 `1,990` bytes)
- VA: `0x0000000140388DC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007FE9C`
- 디코드: `448`개 명령, `1,990/1,990` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00388E40` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00388E52` → [CcSetLazyWriteScanQueuedInternal](../3C/CcSetLazyWriteScanQueuedInternal_function_003C9F60.md) (function, `0x003C9F60`)
- `0x00388F17` → [CcCalculatePagesToWriteForVolume](../47/CcCalculatePagesToWriteForVolume_function_0047CEF4.md) (function, `0x0047CEF4`)
- `0x00388F24` → [CcAdjustThrottleForVolume](../4B/CcAdjustThrottleForVolume_function_004BD5D0.md) (function, `0x004BD5D0`)
- `0x00388FBC` → [CcIsCacheMapACursorInPrivateVCM](CcIsCacheMapACursorInPrivateVCM_function_0038958C.md) (function, `0x0038958C`)
- `0x00388FE4` → [CcShouldLazyWriteCacheMap](CcShouldLazyWriteCacheMap_function_003897A0.md) (function, `0x003897A0`)
- `0x0038903E` → [CcGetNodeForLazyWrite](../40/CcGetNodeForLazyWrite_function_004031AC.md) (function, `0x004031AC`)
- `0x0038908C` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0038909E` → [CcAllocateWorkQueueEntry](../35/CcAllocateWorkQueueEntry_function_0035710C.md) (function, `0x0035710C`)
- `0x003890C8` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0038911B` → [CcPostWorkQueue](../35/CcPostWorkQueue_function_00356808.md) (function, `0x00356808`)
- `0x00389176` → [CcPostWorkQueueAsyncLazywrite](../4B/CcPostWorkQueueAsyncLazywrite_function_004BA17C.md) (function, `0x004BA17C`)
- `0x003891D5` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00389204` → [CcRescheduleLazyWriteScanOnVolume](../22/CcRescheduleLazyWriteScanOnVolume_function_0022FE00.md) (function, `0x0022FE00`)
- `0x0038920D` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00389218` → [CcPostDeferredWrites](../35/CcPostDeferredWrites_function_003590FC.md) (function, `0x003590FC`)
- `0x003892C8` → [CcScanLogHandleList](CcScanLogHandleList_function_0038A26C.md) (function, `0x0038A26C`)
- `0x00389337` → [CcIsDirtyCachemapListEmptyForVolume](../3C/CcIsDirtyCachemapListEmptyForVolume_function_003CF2EC.md) (function, `0x003CF2EC`)
- `0x0038936A` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0038941C` → [CcIncrementWriteBehindPriority](../57/CcIncrementWriteBehindPriority_function_0057B8AC.md) (function, `0x0057B8AC`)
- `0x0038943F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00389452` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003894AC` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00389505` → [CcPostWorkQueue](../35/CcPostWorkQueue_function_00356808.md) (function, `0x00356808`)
- `0x00389536` → [CcComputeNextScanTime](../4A/CcComputeNextScanTime_function_004A2574.md) (function, `0x004A2574`)
- `0x00389547` → [CcRescheduleLazyWriteScanOnVolume](../22/CcRescheduleLazyWriteScanOnVolume_function_0022FE00.md) (function, `0x0022FE00`)
- `0x00389568` → [CcUpdateTimeOnLogHandles](../4C/CcUpdateTimeOnLogHandles_function_004C6D0C.md) (function, `0x004C6D0C`)
- `0x0038957C` → [CcPerfLogLoggedStreamsStats](../4B/CcPerfLogLoggedStreamsStats_function_004B2400.md) (function, `0x004B2400`)

### Direct callers
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F370`
- [CcQuickLazyWriteScanForVolume](../4B/CcQuickLazyWriteScanForVolume_function_004BFEE0.md) at `0x004BFF2A`

### Static image references
- `0x00388E07` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)
- `0x00388F64` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x003891A1` → RVA `0x00FC521C` (`ALMOSTRO`; read)
- `0x003893F6` → RVA `0x00E65B14` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00388F6E` → [sub_006E4FBA](../6E/Unknown_function_006E4FBA.md) (`tail-transfer`)
  - `0x003893CB` → [sub_006E4FBA + 0x84](../6E/Unknown_function_006E4FBA.md) (`tail-transfer`)
  - `0x003893DF` → [sub_006E4FBA + 0x84](../6E/Unknown_function_006E4FBA.md) (`tail-transfer`)
  - `0x003894FB` → [sub_006E4FBA + 0x92](../6E/Unknown_function_006E4FBA.md) (`tail-transfer`)
  - `0x0038950B` → [sub_006E4FBA + 0x9E](../6E/Unknown_function_006E4FBA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00388DC0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00388DC5  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00388DCA  55                              push rbp
00388DCB  56                              push rsi
00388DCC  57                              push rdi
00388DCD  41 54                           push r12
00388DCF  41 55                           push r13
00388DD1  41 56                           push r14
00388DD3  41 57                           push r15
00388DD5  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00388DDA  48 81 EC C0 00 00 00            sub rsp, 0xc0
00388DE1  4C 8B 79 20                     mov r15, qword ptr [rcx + 0x20]
00388DE5  33 DB                           xor ebx, ebx
00388DE7  33 C0                           xor eax, eax
00388DE9  88 5D C7                        mov byte ptr [rbp - 0x39], bl
00388DEC  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00388DF0  0F 57 C0                        xorps xmm0, xmm0
00388DF3  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00388DFD  88 5D 67                        mov byte ptr [rbp + 0x67], bl
00388E00  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00388E04  45 8B E1                        mov r12d, r9d
00388E07  48 8B 05 92 E0 C3 00            mov rax, qword ptr [rip + 0xc3e092]
00388E0E  4D 8B F0                        mov r14, r8
00388E11  48 8B F2                        mov rsi, rdx
00388E14  89 5D CB                        mov dword ptr [rbp - 0x35], ebx
00388E17  48 8B F9                        mov rdi, rcx
00388E1A  88 5D C9                        mov byte ptr [rbp - 0x37], bl
00388E1D  44 8B EB                        mov r13d, ebx
00388E20  88 5D C8                        mov byte ptr [rbp - 0x38], bl
00388E23  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
00388E27  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00388E2B  4C 3B 78 08                     cmp r15, qword ptr [rax + 8]
00388E2F  0F 84 85 04 00 00               je 0x1403892ba
00388E35  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
00388E3C  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00388E40  E8 5B C9 EE FF                  call 0x1402757a0
00388E45  48 8D 8F 98 03 00 00            lea rcx, [rdi + 0x398]
00388E4C  45 33 C0                        xor r8d, r8d
00388E4F  41 8B D4                        mov edx, r12d
00388E52  E8 09 11 04 00                  call 0x1403c9f60
00388E57  44 8B 8F 28 04 00 00            mov r9d, dword ptr [rdi + 0x428]
00388E5E  33 D2                           xor edx, edx
00388E60  48 8B 87 18 04 00 00            mov rax, qword ptr [rdi + 0x418]
00388E67  49 F7 F1                        div r9
00388E6A  33 D2                           xor edx, edx
00388E6C  48 89 87 38 04 00 00            mov qword ptr [rdi + 0x438], rax
00388E73  4C 8B D0                        mov r10, rax
00388E76  48 8B 87 20 04 00 00            mov rax, qword ptr [rdi + 0x420]
00388E7D  49 F7 F1                        div r9
00388E80  48 89 87 40 04 00 00            mov qword ptr [rdi + 0x440], rax
00388E87  4C 8B D8                        mov r11, rax
00388E8A  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00388E8E  B8 01 00 00 00                  mov eax, 1
00388E93  4C 8B 01                        mov r8, qword ptr [rcx]
00388E96  44 3B C8                        cmp r9d, eax
00388E99  0F 86 C8 03 00 00               jbe 0x140389267
00388E9F  41 8D 49 FF                     lea ecx, [r9 - 1]
00388EA3  8B C1                           mov eax, ecx
00388EA5  49 0F AF C2                     imul rax, r10
00388EA9  8B D1                           mov edx, ecx
00388EAB  49 03 80 00 49 00 00            add rax, qword ptr [r8 + 0x4900]
00388EB2  48 8B 8F E0 03 00 00            mov rcx, qword ptr [rdi + 0x3e0]
00388EB9  49 0F AF D3                     imul rdx, r11
00388EBD  48 03 D1                        add rdx, rcx
00388EC0  48 89 87 18 04 00 00            mov qword ptr [rdi + 0x418], rax
00388EC7  48 89 97 20 04 00 00            mov qword ptr [rdi + 0x420], rdx
00388ECE  48 85 C9                        test rcx, rcx
00388ED1  0F 84 5D 04 00 00               je 0x140389334
00388ED7  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
00388EE1  48 8D 8F 10 03 00 00            lea rcx, [rdi + 0x310]
00388EE8  48 89 87 40 06 00 00            mov qword ptr [rdi + 0x640], rax
00388EEF  48 8D 45 CF                     lea rax, [rbp - 0x31]
00388EF3  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00388EF7  48 8D 45 CF                     lea rax, [rbp - 0x31]
00388EFB  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00388EFF  48 8B 01                        mov rax, qword ptr [rcx]
00388F02  48 3B C1                        cmp rax, rcx
00388F05  0F 85 2E 03 00 00               jne 0x140389239
00388F0B  41 8B D4                        mov edx, r12d
00388F0E  88 9F DA 03 00 00               mov byte ptr [rdi + 0x3da], bl
00388F14  48 8B CF                        mov rcx, rdi
00388F17  E8 D8 3F 0F 00                  call 0x14047cef4
00388F1C  48 8B CF                        mov rcx, rdi
00388F1F  89 45 CB                        mov dword ptr [rbp - 0x35], eax
00388F22  8B D8                           mov ebx, eax
00388F24  E8 A7 46 13 00                  call 0x1404bd5d0
00388F29  48 8B 8F E0 03 00 00            mov rcx, qword ptr [rdi + 0x3e0]
00388F30  48 89 8F E8 03 00 00            mov qword ptr [rdi + 0x3e8], rcx
00388F37  48 8B 8F 30 04 00 00            mov rcx, qword ptr [rdi + 0x430]
00388F3E  89 9F F0 03 00 00               mov dword ptr [rdi + 0x3f0], ebx
00388F44  89 9F 90 03 00 00               mov dword ptr [rdi + 0x390], ebx
00388F4A  8B 96 98 00 00 00               mov edx, dword ptr [rsi + 0x98]
00388F50  89 1C D1                        mov dword ptr [rcx + rdx*8], ebx
00388F53  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
00388F5D  48 89 86 D8 00 00 00            mov qword ptr [rsi + 0xd8], rax
00388F64  F7 05 A2 DB C3 00 00 00 02 00   test dword ptr [rip + 0xc3dba2], 0x20000
00388F6E  0F 85 46 C0 35 00               jne 0x1406e4fba
00388F74  44 8B 65 CB                     mov r12d, dword ptr [rbp - 0x35]
00388F78  4C 8D B7 98 02 00 00            lea r14, [rdi + 0x298]
00388F7F  49 8B 1E                        mov rbx, qword ptr [r14]
00388F82  48 81 EB 38 02 00 00            sub rbx, 0x238
00388F89  33 C9                           xor ecx, ecx
00388F8B  48 3B D9                        cmp rbx, rcx
00388F8E  0F 84 E9 01 00 00               je 0x14038917d
00388F94  48 8D B3 38 02 00 00            lea rsi, [rbx + 0x238]
00388F9B  48 89 75 17                     mov qword ptr [rbp + 0x17], rsi
00388F9F  49 3B F6                        cmp rsi, r14
00388FA2  0F 84 D5 01 00 00               je 0x14038917d
00388FA8  48 85 C9                        test rcx, rcx
00388FAB  48 8B C3                        mov rax, rbx
00388FAE  48 8B D3                        mov rdx, rbx
00388FB1  48 0F 45 C1                     cmovne rax, rcx
00388FB5  48 8B CF                        mov rcx, rdi
00388FB8  48 89 45 07                     mov qword ptr [rbp + 7], rax
00388FBC  E8 CB 05 00 00                  call 0x14038958c
00388FC1  84 C0                           test al, al
00388FC3  75 54                           jne 0x140389019
00388FC5  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
00388FC9  4C 8B C7                        mov r8, rdi
00388FCC  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00388FCF  48 83 E0 F0                     and rax, 0xfffffffffffffff0
00388FD3  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00388FD7  33 D2                           xor edx, edx
00388FD9  45 8B CC                        mov r9d, r12d
00388FDC  48 8B CB                        mov rcx, rbx
00388FDF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00388FE4  E8 B7 07 00 00                  call 0x1403897a0
00388FE9  84 C0                           test al, al
00388FEB  75 49                           jne 0x140389036
00388FED  8B 8B 98 00 00 00               mov ecx, dword ptr [rbx + 0x98]
00388FF3  41 B8 20 00 01 00               mov r8d, 0x10020
00388FF9  8B C1                           mov eax, ecx
00388FFB  41 23 C0                        and eax, r8d
00388FFE  41 3B C0                        cmp eax, r8d
00389001  0F 84 12 04 00 00               je 0x140389419
00389007  BA 01 00 00 00                  mov edx, 1
0038900C  44 03 EA                        add r13d, edx
0038900F  41 83 FD 14                     cmp r13d, 0x14
00389013  0F 83 0D 04 00 00               jae 0x140389426
00389019  48 8B 1E                        mov rbx, qword ptr [rsi]
0038901C  48 81 EB 38 02 00 00            sub rbx, 0x238
00389023  80 7D 67 00                     cmp byte ptr [rbp + 0x67], 0
00389027  0F 85 39 04 00 00               jne 0x140389466
0038902D  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
00389031  E9 55 FF FF FF                  jmp 0x140388f8b
00389036  48 83 65 FF 00                  and qword ptr [rbp - 1], 0
0038903B  48 8B CB                        mov rcx, rbx
0038903E  E8 69 A1 07 00                  call 0x1404031ac
00389043  0F BA A3 98 00 00 00 18         bt dword ptr [rbx + 0x98], 0x18
0038904B  4C 8B E8                        mov r13, rax
0038904E  41 BA 01 00 00 00               mov r10d, 1
00389054  0F 82 23 02 00 00               jb 0x14038927d
0038905A  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
00389060  8B 53 70                        mov edx, dword ptr [rbx + 0x70]
00389063  89 93 C8 00 00 00               mov dword ptr [rbx + 0xc8], edx
00389069  0F BA E0 09                     bt eax, 9
0038906D  0F 82 4B 03 00 00               jb 0x1403893be
00389073  80 7D C7 00                     cmp byte ptr [rbp - 0x39], 0
00389077  0F 84 C4 00 00 00               je 0x140389141
0038907D  83 8B 98 00 00 00 20            or dword ptr [rbx + 0x98], 0x20
00389084  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00389088  44 01 53 70                     add dword ptr [rbx + 0x70], r10d
0038908C  E8 4F 9C FB FF                  call 0x140342ce0
00389091  4C 8D 4D FF                     lea r9, [rbp - 1]
00389095  4D 8B C5                        mov r8, r13
00389098  48 8B D7                        mov rdx, rdi
0038909B  49 8B CF                        mov rcx, r15
0038909E  E8 69 E0 FC FF                  call 0x14035710c
003890A3  48 8D 55 E7                     lea rdx, [rbp - 0x19]
003890A7  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003890AE  85 C0                           test eax, eax
003890B0  0F 88 F6 03 00 00               js 0x1403894ac
003890B6  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
003890BA  C7 86 80 00 00 00 02 00 00 00   mov dword ptr [rsi + 0x80], 2
003890C4  48 89 5E 10                     mov qword ptr [rsi + 0x10], rbx
003890C8  E8 D3 C6 EE FF                  call 0x1402757a0
003890CD  8B 4B 70                        mov ecx, dword ptr [rbx + 0x70]
003890D0  FF C9                           dec ecx
003890D2  F7 83 98 00 00 00 00 00 01 00   test dword ptr [rbx + 0x98], 0x10000
003890DC  89 4B 70                        mov dword ptr [rbx + 0x70], ecx
003890DF  75 25                           jne 0x140389106
003890E1  83 7B 04 00                     cmp dword ptr [rbx + 4], 0
003890E5  74 49                           je 0x140389130
003890E7  48 89 B3 F8 01 00 00            mov qword ptr [rbx + 0x1f8], rsi
003890EE  BA 01 00 00 00                  mov edx, 1
003890F3  8B 87 50 06 00 00               mov eax, dword ptr [rdi + 0x650]
003890F9  48 8B CE                        mov rcx, rsi
003890FC  84 C2                           test dl, al
003890FE  75 5C                           jne 0x14038915c
00389100  49 8D 55 68                     lea rdx, [r13 + 0x68]
00389104  EB 15                           jmp 0x14038911b
00389106  48 8B C6                        mov rax, rsi
00389109  49 8D 55 48                     lea rdx, [r13 + 0x48]
0038910D  48 83 C8 01                     or rax, 1
00389111  48 89 83 F8 01 00 00            mov qword ptr [rbx + 0x1f8], rax
00389118  48 8B CE                        mov rcx, rsi
0038911B  E8 E8 D6 FC FF                  call 0x140356808
00389120  48 8B 75 17                     mov rsi, qword ptr [rbp + 0x17]
00389124  45 33 ED                        xor r13d, r13d
00389127  C6 45 C8 01                     mov byte ptr [rbp - 0x38], 1
0038912B  E9 E9 FE FF FF                  jmp 0x140389019
00389130  85 C9                           test ecx, ecx
00389132  75 B3                           jne 0x1403890e7
00389134  48 89 B3 F8 01 00 00            mov qword ptr [rbx + 0x1f8], rsi
0038913B  49 8D 55 78                     lea rdx, [r13 + 0x78]
0038913F  EB D7                           jmp 0x140389118
00389141  8B 83 C8 00 00 00               mov eax, dword ptr [rbx + 0xc8]
00389147  41 3B C4                        cmp eax, r12d
0038914A  0F 83 82 01 00 00               jae 0x1403892d2
00389150  44 2B E0                        sub r12d, eax
00389153  44 89 65 CB                     mov dword ptr [rbp - 0x35], r12d
00389157  E9 21 FF FF FF                  jmp 0x14038907d
0038915C  C7 86 80 00 00 00 07 00 00 00   mov dword ptr [rsi + 0x80], 7
00389166  49 8D 95 38 01 00 00            lea rdx, [r13 + 0x138]
0038916D  48 89 5E 18                     mov qword ptr [rsi + 0x18], rbx
00389171  48 83 66 10 00                  and qword ptr [rsi + 0x10], 0
00389176  E8 01 10 13 00                  call 0x1404ba17c
0038917B  EB A3                           jmp 0x140389120
0038917D  BA 01 00 00 00                  mov edx, 1
00389182  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00389186  48 8D 45 CF                     lea rax, [rbp - 0x31]
0038918A  0F B6 5D C8                     movzx ebx, byte ptr [rbp - 0x38]
0038918E  48 3B C8                        cmp rcx, rax
00389191  0F 45 DA                        cmovne ebx, edx
00389194  48 8D 45 CF                     lea rax, [rbp - 0x31]
00389198  48 3B C8                        cmp rcx, rax
0038919B  0F 85 24 03 00 00               jne 0x1403894c5
003891A1  80 3D 74 C0 C3 00 00            cmp byte ptr [rip + 0xc3c074], 0
003891A8  0F 84 62 03 00 00               je 0x140389510
003891AE  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003891B8  48 39 45 DF                     cmp qword ptr [rbp - 0x21], rax
003891BC  0F 85 7E 03 00 00               jne 0x140389540
003891C2  C6 87 C4 02 00 00 01            mov byte ptr [rdi + 0x2c4], 1
003891C9  41 C6 87 19 04 00 00 00         mov byte ptr [r15 + 0x419], 0
003891D1  48 8D 4D E7                     lea rcx, [rbp - 0x19]
003891D5  E8 06 9B FB FF                  call 0x140342ce0
003891DA  80 7D C9 00                     cmp byte ptr [rbp - 0x37], 0
003891DE  0F 85 81 03 00 00               jne 0x140389565
003891E4  F7 05 22 D9 C3 00 00 00 02 00   test dword ptr [rip + 0xc3d922], 0x20000
003891EE  0F 85 7E 03 00 00               jne 0x140389572
003891F4  48 8D 87 50 04 00 00            lea rax, [rdi + 0x450]
003891FB  48 39 00                        cmp qword ptr [rax], rax
003891FE  75 12                           jne 0x140389212
00389200  EB 1B                           jmp 0x14038921d
00389202  33 D2                           xor edx, edx
00389204  E8 F7 6B EA FF                  call 0x14022fe00
00389209  48 8D 4D E7                     lea rcx, [rbp - 0x19]
0038920D  E8 CE 9A FB FF                  call 0x140342ce0
00389212  48 8B D7                        mov rdx, rdi
00389215  49 8B CF                        mov rcx, r15
00389218  E8 DF FE FC FF                  call 0x1403590fc
0038921D  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
00389225  48 81 C4 C0 00 00 00            add rsp, 0xc0
0038922C  41 5F                           pop r15
0038922E  41 5E                           pop r14
00389230  41 5D                           pop r13
00389232  41 5C                           pop r12
00389234  5F                              pop rdi
00389235  5E                              pop rsi
00389236  5D                              pop rbp
00389237  C3                              ret
00389238  CC                              int3
00389239  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0038923D  75 21                           jne 0x140389260
0038923F  48 8B 10                        mov rdx, qword ptr [rax]
00389242  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00389246  75 18                           jne 0x140389260
00389248  48 89 11                        mov qword ptr [rcx], rdx
0038924B  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0038924F  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00389253  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
00389257  4C 39 02                        cmp qword ptr [rdx], r8
0038925A  0F 84 14 01 00 00               je 0x140389374
00389260  B9 03 00 00 00                  mov ecx, 3
00389265  CD 29                           int 0x29
00389267  48 8B 97 E0 03 00 00            mov rdx, qword ptr [rdi + 0x3e0]
0038926E  49 8B 80 00 49 00 00            mov rax, qword ptr [r8 + 0x4900]
00389275  48 8B CA                        mov rcx, rdx
00389278  E9 43 FC FF FF                  jmp 0x140388ec0
0038927D  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
00389287  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
0038928E  44 88 55 C9                     mov byte ptr [rbp - 0x37], r10b
00389292  44 09 91 90 00 00 00            or dword ptr [rcx + 0x90], r10d
00389299  48 8B 8B 08 01 00 00            mov rcx, qword ptr [rbx + 0x108]
003892A0  48 8B 93 F8 00 00 00            mov rdx, qword ptr [rbx + 0xf8]
003892A7  48 3B 4A 70                     cmp rcx, qword ptr [rdx + 0x70]
003892AB  0F 8F DA 00 00 00               jg 0x14038938b
003892B1  44 8B 65 CB                     mov r12d, dword ptr [rbp - 0x35]
003892B5  E9 A0 FD FF FF                  jmp 0x14038905a
003892BA  4C 8D 4D 0F                     lea r9, [rbp + 0xf]
003892BE  45 8B C4                        mov r8d, r12d
003892C1  48 8D 55 CB                     lea rdx, [rbp - 0x35]
003892C5  49 8B CF                        mov rcx, r15
003892C8  E8 9F 0F 00 00                  call 0x14038a26c
003892CD  E9 63 FB FF FF                  jmp 0x140388e35
003892D2  F7 83 98 00 00 00 00 02 00 00   test dword ptr [rbx + 0x98], 0x200
003892DC  0F 85 2E 01 00 00               jne 0x140389410
003892E2  48 39 5D 07                     cmp qword ptr [rbp + 7], rbx
003892E6  0F 84 16 01 00 00               je 0x140389402
003892EC  49 8B 0E                        mov rcx, qword ptr [r14]
003892EF  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
003892F3  0F 85 67 FF FF FF               jne 0x140389260
003892F9  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
003892FD  4C 39 30                        cmp qword ptr [rax], r14
00389300  0F 85 5A FF FF FF               jne 0x140389260
00389306  48 89 08                        mov qword ptr [rax], rcx
00389309  48 89 41 08                     mov qword ptr [rcx + 8], rax
0038930D  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00389311  48 39 30                        cmp qword ptr [rax], rsi
00389314  0F 85 46 FF FF FF               jne 0x140389260
0038931A  49 89 36                        mov qword ptr [r14], rsi
0038931D  49 89 46 08                     mov qword ptr [r14 + 8], rax
00389321  4C 89 30                        mov qword ptr [rax], r14
00389324  4C 89 76 08                     mov qword ptr [rsi + 8], r14
00389328  45 33 E4                        xor r12d, r12d
0038932B  44 88 55 C7                     mov byte ptr [rbp - 0x39], r10b
0038932F  E9 1F FE FF FF                  jmp 0x140389153
00389334  48 8B CF                        mov rcx, rdi
00389337  E8 B0 5F 04 00                  call 0x1403cf2ec
0038933C  84 C0                           test al, al
0038933E  0F 84 93 FB FF FF               je 0x140388ed7
00389344  38 9F DA 03 00 00               cmp byte ptr [rdi + 0x3da], bl
0038934A  0F 85 87 FB FF FF               jne 0x140388ed7
00389350  48 8D 87 50 04 00 00            lea rax, [rdi + 0x450]
00389357  48 39 00                        cmp qword ptr [rax], rax
0038935A  0F 85 A2 FE FF FF               jne 0x140389202
00389360  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00389364  88 9F D9 03 00 00               mov byte ptr [rdi + 0x3d9], bl
0038936A  E8 71 99 FB FF                  call 0x140342ce0
0038936F  E9 A9 FE FF FF                  jmp 0x14038921d
00389374  48 89 50 08                     mov qword ptr [rax + 8], rdx
00389378  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0038937C  4C 89 00                        mov qword ptr [rax], r8
0038937F  48 89 02                        mov qword ptr [rdx], rax
00389382  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00389386  E9 74 FB FF FF                  jmp 0x140388eff
0038938B  48 89 4A 70                     mov qword ptr [rdx + 0x70], rcx
0038938F  F7 05 77 D7 C3 00 00 00 02 00   test dword ptr [rip + 0xc3d777], 0x20000
00389399  0F 84 12 FF FF FF               je 0x1403892b1
0038939F  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
003893A3  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
003893AA  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003893AE  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
003893B2  48 89 81 80 00 00 00            mov qword ptr [rcx + 0x80], rax
003893B9  E9 F3 FE FF FF                  jmp 0x1403892b1
003893BE  83 FA 40                        cmp edx, 0x40
003893C1  0F 82 AC FC FF FF               jb 0x140389073
003893C7  0F BA E0 18                     bt eax, 0x18
003893CB  0F 83 6D BC 35 00               jae 0x1406e503e
003893D1  4C 8B 8B F8 00 00 00            mov r9, qword ptr [rbx + 0xf8]
003893D8  45 8B 41 68                     mov r8d, dword ptr [r9 + 0x68]
003893DC  45 85 C0                        test r8d, r8d
003893DF  0F 84 59 BC 35 00               je 0x1406e503e
003893E5  33 C0                           xor eax, eax
003893E7  41 8B C8                        mov ecx, r8d
003893EA  2B CA                           sub ecx, edx
003893EC  41 3B D0                        cmp edx, r8d
003893EF  0F 46 C1                        cmovbe eax, ecx
003893F2  41 89 41 68                     mov dword ptr [r9 + 0x68], eax
003893F6  44 01 15 17 C7 AD 00            add dword ptr [rip + 0xadc717], r10d
003893FD  E9 71 FC FF FF                  jmp 0x140389073
00389402  8B 83 14 01 00 00               mov eax, dword ptr [rbx + 0x114]
00389408  A8 0F                           test al, 0xf
0038940A  0F 85 DC FE FF FF               jne 0x1403892ec
00389410  44 88 55 67                     mov byte ptr [rbp + 0x67], r10b
00389414  E9 0F FF FF FF                  jmp 0x140389328
00389419  48 8B CB                        mov rcx, rbx
0038941C  E8 8B 24 1F 00                  call 0x14057b8ac
00389421  E9 F3 FB FF FF                  jmp 0x140389019
00389426  F6 C1 20                        test cl, 0x20
00389429  0F 85 EA FB FF FF               jne 0x140389019
0038942F  01 53 70                        add dword ptr [rbx + 0x70], edx
00389432  83 C9 20                        or ecx, 0x20
00389435  89 8B 98 00 00 00               mov dword ptr [rbx + 0x98], ecx
0038943B  48 8D 4D E7                     lea rcx, [rbp - 0x19]
0038943F  E8 9C 98 FB FF                  call 0x140342ce0
00389444  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00389448  45 33 ED                        xor r13d, r13d
0038944B  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
00389452  E8 49 C3 EE FF                  call 0x1402757a0
00389457  83 A3 98 00 00 00 DF            and dword ptr [rbx + 0x98], 0xffffffdf
0038945E  FF 4B 70                        dec dword ptr [rbx + 0x70]
00389461  E9 B3 FB FF FF                  jmp 0x140389019
00389466  49 8B 06                        mov rax, qword ptr [r14]
00389469  4C 39 70 08                     cmp qword ptr [rax + 8], r14
0038946D  0F 85 ED FD FF FF               jne 0x140389260
00389473  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00389477  4C 39 31                        cmp qword ptr [rcx], r14
0038947A  0F 85 E0 FD FF FF               jne 0x140389260
00389480  48 89 01                        mov qword ptr [rcx], rax
00389483  48 89 48 08                     mov qword ptr [rax + 8], rcx
00389487  48 8B 06                        mov rax, qword ptr [rsi]
0038948A  48 39 70 08                     cmp qword ptr [rax + 8], rsi
0038948E  0F 85 CC FD FF FF               jne 0x140389260
00389494  49 89 06                        mov qword ptr [r14], rax
00389497  49 89 76 08                     mov qword ptr [r14 + 8], rsi
0038949B  4C 89 70 08                     mov qword ptr [rax + 8], r14
0038949F  32 C0                           xor al, al
003894A1  88 45 67                        mov byte ptr [rbp + 0x67], al
003894A4  4C 89 36                        mov qword ptr [rsi], r14
003894A7  E9 81 FB FF FF                  jmp 0x14038902d
003894AC  E8 EF C2 EE FF                  call 0x1402757a0
003894B1  83 A3 98 00 00 00 DF            and dword ptr [rbx + 0x98], 0xffffffdf
003894B8  BA 01 00 00 00                  mov edx, 1
003894BD  29 53 70                        sub dword ptr [rbx + 0x70], edx
003894C0  E9 BD FC FF FF                  jmp 0x140389182
003894C5  48 8D 45 CF                     lea rax, [rbp - 0x31]
003894C9  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003894CD  0F 85 8D FD FF FF               jne 0x140389260
003894D3  48 8B 01                        mov rax, qword ptr [rcx]
003894D6  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003894DA  0F 85 80 FD FF FF               jne 0x140389260
003894E0  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
003894E4  48 8D 55 CF                     lea rdx, [rbp - 0x31]
003894E8  48 89 50 08                     mov qword ptr [rax + 8], rdx
003894EC  8B 87 50 06 00 00               mov eax, dword ptr [rdi + 0x650]
003894F2  48 8B 91 98 00 00 00            mov rdx, qword ptr [rcx + 0x98]
003894F9  A8 02                           test al, 2
003894FB  0F 85 4B BB 35 00               jne 0x1406e504c
00389501  48 83 C2 68                     add rdx, 0x68
00389505  E8 FE D2 FC FF                  call 0x140356808
0038950A  90                              nop
0038950B  E9 48 BB 35 00                  jmp 0x1406e5058
00389510  84 DB                           test bl, bl
00389512  0F 85 96 FC FF FF               jne 0x1403891ae
00389518  48 8D 87 50 04 00 00            lea rax, [rdi + 0x450]
0038951F  48 39 00                        cmp qword ptr [rax], rax
00389522  0F 85 86 FC FF FF               jne 0x1403891ae
00389528  4C 8D 4D DF                     lea r9, [rbp - 0x21]
0038952C  48 8B D7                        mov rdx, rdi
0038952F  4C 8D 45 0F                     lea r8, [rbp + 0xf]
00389533  49 8B CF                        mov rcx, r15
00389536  E8 39 90 11 00                  call 0x1404a2574
0038953B  E9 6E FC FF FF                  jmp 0x1403891ae
00389540  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00389544  48 8B CF                        mov rcx, rdi
00389547  E8 B4 68 EA FF                  call 0x14022fe00
0038954C  80 BF C4 02 00 00 00            cmp byte ptr [rdi + 0x2c4], 0
00389553  0F 84 78 FC FF FF               je 0x1403891d1
00389559  C6 87 C4 02 00 00 00            mov byte ptr [rdi + 0x2c4], 0
00389560  E9 6C FC FF FF                  jmp 0x1403891d1
00389565  49 8B CF                        mov rcx, r15
00389568  E8 9F D7 13 00                  call 0x1404c6d0c
0038956D  E9 72 FC FF FF                  jmp 0x1403891e4
00389572  41 8B 97 D0 03 00 00            mov edx, dword ptr [r15 + 0x3d0]
00389579  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
0038957C  E8 7F 8E 12 00                  call 0x1404b2400
00389581  E9 6E FC FF FF                  jmp 0x1403891f4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcLazyWriteScanVolume(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m96;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (192);
    v_rbx = 0;
    result = 0;
    v_stack_m98 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_m50 = 0;
    v_stack_m94 = 0;
    v_stack_m96 = 0;
    v_stack_m97 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 32)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12837010) + 8))) goto loc_003892BA;
loc_00388E35:
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 32) + 768, v_stack_m78, a3, a4);
    a3 = 0;
    result = CcSetLazyWriteScanQueuedInternal(a1 + 920, (unsigned int)((unsigned int)((unsigned int)(a4))), a3, a4);
    a2 = 0;
    a2 = 0;
    *(unsigned __int64 *)(a1 + 1080) = *(unsigned __int64 *)(a1 + 1048);
    *(unsigned __int64 *)(a1 + 1088) = *(unsigned __int64 *)(a1 + 1056);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1064)))) <= 1) goto loc_00389267;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1064)) - 1))) * (*(unsigned __int64 *)(a1 + 1048));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) + 18688));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1064)) - 1))) * (*(unsigned __int64 *)(a1 + 1056));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 992));
loc_00388EC0:
    *(unsigned __int64 *)(a1 + 1048) = result;
    *(unsigned __int64 *)(a1 + 1056) = a2;
    if (*(unsigned __int64 *)(a1 + 992) == 0) goto loc_00389334;
loc_00388ED7:
    *(unsigned __int64 *)(a1 + 1600) = result;
    v_stack_m88 = v_stack_m90;
    v_stack_m90 = v_stack_m90;
loc_00388EFF:
    if ((*(unsigned __int64 *)(a1 + 784)) != (a1 + 784)) goto loc_00389239;
    *(unsigned __int8 *)(a1 + 986) = 0;
    result = CcCalculatePagesToWriteForVolume(a1, (unsigned int)((unsigned int)((unsigned int)(a4))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)), (unsigned int)(*(unsigned int *)(a1 + 1064)));
    v_stack_m94 = (unsigned int)(result);
    result = CcAdjustThrottleForVolume(a1, (unsigned int)((unsigned int)((unsigned int)(a4))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)), (unsigned int)(*(unsigned int *)(a1 + 1064)));
    *(unsigned __int64 *)(a1 + 1000) = *(unsigned __int64 *)(a1 + 992);
    *(unsigned int *)(a1 + 1008) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(a1 + 912) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1072) + (unsigned int)(*(unsigned int *)(a2 + 152)) * 8) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a2 + 216) = result;
    v_rbx = (*(unsigned __int64 *)(a1 + 664)) - (568);
    a1 = 0;
loc_00388F8B:
    if (v_rbx == 0) goto loc_0038917D;
    v_stack_m48 = v_rbx + 568;
    if ((v_rbx + 568) == (a1 + 664)) goto loc_0038917D;
    result = v_rbx;
    if (0 != 0) { result = 0; }
    v_stack_m58 = result;
    result = CcIsCacheMapACursorInPrivateVCM(0, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)), (unsigned int)(*(unsigned int *)(a1 + 1064)));
    if ((unsigned __int8)(result) != 0) goto loc_00389019;
    result = (*(unsigned __int64 *)(v_rbx + 96)) & (-16);
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_p20));
    a2 = 0;
    v_stack_mD8 = result;
    result = CcShouldLazyWriteCacheMap(v_rbx, a2, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))));
    if ((unsigned __int8)(result) != 0) goto loc_00389036;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 152))))) & ((unsigned int)((unsigned int)(0x10020ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x10020ULL)))) goto loc_00389419;
    v_r13 = (unsigned int)((0) + (1));
    if (((unsigned int)(v_r13)) >= 20) goto loc_00389426;
loc_00389019:
    v_rbx = (*(unsigned __int64 *)(v_rbx + 568)) - (568);
    if (v_stack_p8 != 0) goto loc_00389466;
loc_0038902D:
    goto loc_00388F8B;
loc_00389036:
    result = CcGetNodeForLazyWrite(v_rbx, 1, (unsigned int)(0x10020ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))));
    if (v_stack_p8 < 0) goto loc_0038927D;
loc_0038905A:
    *(unsigned int *)(v_rbx + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)));
    if (v_stack_p8 < 0) goto loc_003893BE;
loc_00389073:
    if (v_stack_m98 == 0) goto loc_00389141;
loc_0038907D:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, (unsigned int)(*(unsigned int *)(v_rbx + 112)), (unsigned int)(0x10020ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))));
    result = CcAllocateWorkQueueEntry(*(unsigned __int64 *)(a1 + 32), 0, result, v_stack_m60);
    if (sign_flag) goto loc_003894AC;
    *(unsigned int *)(v_stack_m60 + 128) = 2;
    *(unsigned __int64 *)(v_stack_m60 + 16) = v_rbx;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 32) + 768, v_stack_m78, result, v_stack_m60);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 112))) - 1);
    *(unsigned int *)(v_rbx + 112) = (unsigned int)(a1);
    if (((*(unsigned int *)(v_rbx + 152)) & (0x10000ULL)) != 0) goto loc_00389106;
    if ((*(unsigned int *)(v_rbx + 4)) == 0) goto loc_00389130;
loc_003890E7:
    *(unsigned __int64 *)(v_rbx + 504) = v_stack_m60;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1616))))) != 0) goto loc_0038915C;
    goto loc_0038911B;
loc_00389106:
    result = (v_stack_m60) | (1);
    *(unsigned __int64 *)(v_rbx + 504) = result;
loc_00389118:
loc_0038911B:
    result = CcPostWorkQueue(v_stack_m60, result + 72, result, v_stack_m60);
loc_00389120:
    v_r13 = 0;
    v_stack_m97 = 1;
    goto loc_00389019;
loc_00389130:
    if ((unsigned int)(v_stack_m60) != 0) goto loc_003890E7;
    *(unsigned __int64 *)(v_rbx + 504) = v_stack_m48;
    goto loc_00389118;
loc_00389141:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 200)))) >= ((unsigned int)((unsigned int)(v_stack_m94)))) goto loc_003892D2;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m94)) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 200)))));
loc_00389153:
    v_stack_m94 = (unsigned int)(v_r12);
    goto loc_0038907D;
loc_0038915C:
    *(unsigned int *)(v_stack_m48 + 128) = 7;
    *(unsigned __int64 *)(v_stack_m48 + 24) = v_rbx;
    result = CcPostWorkQueueAsyncLazywrite(v_stack_m60, v_r13 + 312, result, v_stack_m60);
    goto loc_00389120;
loc_0038917D:
loc_00389182:
    v_rbx = v_stack_m97;
    if (v_stack_m90 != v_stack_m90) { v_rbx = 1; }
    if (v_stack_m90 != v_stack_m90) goto loc_003894C5;
    if ((*(unsigned __int8 *)(v_rip + 12828788)) == 0) goto loc_00389510;
loc_003891AE:
    if (v_stack_m80 != v_stack_m90) goto loc_00389540;
    *(unsigned __int8 *)(a1 + 708) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 1049) = 0;
loc_003891D1:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, 1, result, v_stack_m60);
    if (v_stack_m96 != 0) goto loc_00389565;
loc_003891E4:
    if (((*(unsigned int *)(v_rip + 12835106)) & (0x20000ULL)) != 0) goto loc_00389572;
loc_003891F4:
    if ((*(unsigned __int64 *)(a1 + 1104)) != (a1 + 1104)) goto loc_00389212;
    goto loc_0038921D;
loc_00389202:
    a2 = 0;
    result = CcRescheduleLazyWriteScanOnVolume(v_stack_m78, a2, result, v_stack_m60);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, a2, result, v_stack_m60);
loc_00389212:
    result = CcPostDeferredWrites(*(unsigned __int64 *)(a1 + 32), a1, result, v_stack_m60);
loc_0038921D:
    v_rsp = (v_rsp) + (192);
    return result;
loc_00389239:
    if ((*(unsigned __int64 *)(result + 8)) != (*(unsigned __int64 *)(a1 + 32))) goto loc_00389260;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_00389260;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(a1 + 32);
    if ((*(unsigned __int64 *)(v_stack_m88)) == v_stack_m90) goto loc_00389374;
loc_00389260:
loc_00389267:
    goto loc_00388EC0;
loc_0038927D:
    v_stack_m96 = 1;
    if ((*(unsigned __int64 *)(v_stack_p10 + 264)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 112))) goto loc_0038938B;
loc_003892B1:
    goto loc_0038905A;
loc_003892BA:
    result = CcScanLogHandleList(*(unsigned __int64 *)(a1 + 32), v_stack_m94, (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))), v_stack_m50);
    goto loc_00388E35;
loc_003892D2:
    if (((*(unsigned int *)(v_stack_p10 + 152)) & (512)) != 0) goto loc_00389410;
    if (v_stack_m58 == v_stack_p10) goto loc_00389402;
loc_003892EC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664) + 8)) != (a1 + 664)) goto loc_00389260;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8))) != (a1 + 664)) goto loc_00389260;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8)) = *(unsigned __int64 *)(a1 + 664);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664) + 8) = *(unsigned __int64 *)(a1 + 664 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48 + 8))) != v_stack_m48) goto loc_00389260;
    *(unsigned __int64 *)(a1 + 664) = v_stack_m48;
    *(unsigned __int64 *)(a1 + 664 + 8) = *(unsigned __int64 *)(v_stack_m48 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48 + 8)) = a1 + 664;
    *(unsigned __int64 *)(v_stack_m48 + 8) = a1 + 664;
loc_00389328:
    v_r12 = 0;
    v_stack_m98 = 1;
    goto loc_00389153;
loc_00389334:
    result = CcIsDirtyCachemapListEmptyForVolume(a1, v_stack_m94, (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))), v_stack_m50);
    if ((unsigned __int8)(result) == 0) goto loc_00388ED7;
    if ((*(unsigned __int8 *)(a1 + 986)) != ((unsigned __int8)(v_stack_p10))) goto loc_00388ED7;
    if ((*(unsigned __int64 *)(a1 + 1104)) != (a1 + 1104)) goto loc_00389202;
    *(unsigned __int8 *)(a1 + 985) = (unsigned __int8)(v_stack_p10);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, v_stack_m94, (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))), v_stack_m50);
    goto loc_0038921D;
loc_00389374:
    *(unsigned __int64 *)(result + 8) = v_stack_m94;
    *(unsigned __int64 *)(result) = v_stack_m90;
    *(unsigned __int64 *)(v_stack_m94) = result;
    v_stack_m88 = result;
    goto loc_00388EFF;
loc_0038938B:
    *(unsigned __int64 *)(v_stack_m94 + 112) = v_stack_m78;
    if (((*(unsigned int *)(v_rip + 12834679)) & (0x20000ULL)) == 0) goto loc_003892B1;
    result = (*(unsigned __int64 *)(v_stack_p10 + 96)) & (-16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 128) = *(unsigned __int64 *)(result + 24);
    goto loc_003892B1;
loc_003893BE:
    if (((unsigned int)(v_stack_m94)) < 64) goto loc_00389073;
    result = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104))))) - ((unsigned int)(v_stack_m94)));
    if (((unsigned int)(v_stack_m94)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104))))) { result = (unsigned int)(a1); }
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104) = (unsigned int)(result);
    goto loc_00389073;
loc_00389402:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 276)))) & (15)) != 0) goto loc_003892EC;
loc_00389410:
    v_stack_p8 = 1;
    goto loc_00389328;
loc_00389419:
    result = CcIncrementWriteBehindPriority(v_stack_p10, v_stack_m94, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104)), *(unsigned __int64 *)(v_stack_p10 + 248));
    goto loc_00389019;
loc_00389426:
    if ((((unsigned __int8)(v_stack_p10)) & (32)) != 0) goto loc_00389019;
    a1 = (unsigned int)((v_stack_p10) | (32));
    *(unsigned int *)(v_stack_p10 + 152) = (unsigned int)(a1);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, v_stack_m94, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104)), *(unsigned __int64 *)(v_stack_p10 + 248));
    v_r13 = 0;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 32) + 768, v_stack_m78, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104)), *(unsigned __int64 *)(v_stack_p10 + 248));
    goto loc_00389019;
loc_00389466:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664) + 8)) != (a1 + 664)) goto loc_00389260;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8))) != (a1 + 664)) goto loc_00389260;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8)) = *(unsigned __int64 *)(a1 + 664);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664) + 8) = *(unsigned __int64 *)(a1 + 664 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48) + 8)) != v_stack_m48) goto loc_00389260;
    *(unsigned __int64 *)(a1 + 664) = *(unsigned __int64 *)(v_stack_m48);
    *(unsigned __int64 *)(a1 + 664 + 8) = v_stack_m48;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48) + 8) = a1 + 664;
    result = 0;
    v_stack_p8 = 0;
    *(unsigned __int64 *)(v_stack_m48) = a1 + 664;
    goto loc_0038902D;
loc_003894AC:
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 664 + 8), v_stack_m78, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104)), *(unsigned __int64 *)(v_stack_p10 + 248));
    goto loc_00389182;
loc_003894C5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8) + 8)) != v_stack_m90) goto loc_00389260;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 664 + 8))) goto loc_00389260;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8)) + 8) = v_stack_m90;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 664 + 8) + 152)) + (104);
    result = CcPostWorkQueue(*(unsigned __int64 *)(a1 + 664 + 8), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 248) + 104)), *(unsigned __int64 *)(v_stack_p10 + 248));
loc_00389510:
    if ((unsigned __int8)(v_stack_p10) != 0) goto loc_003891AE;
    if ((*(unsigned __int64 *)(a1 + 1104)) != (a1 + 1104)) goto loc_003891AE;
    result = CcComputeNextScanTime(*(unsigned __int64 *)(a1 + 32), a1, v_stack_m50, v_stack_m80);
    goto loc_003891AE;
loc_00389540:
    result = CcRescheduleLazyWriteScanOnVolume(a1, v_stack_m80, v_stack_m50, v_stack_m80);
    if ((*(unsigned __int8 *)(a1 + 708)) == 0) goto loc_003891D1;
    *(unsigned __int8 *)(a1 + 708) = 0;
    goto loc_003891D1;
loc_00389565:
    result = CcUpdateTimeOnLogHandles(*(unsigned __int64 *)(a1 + 32), v_stack_m80, v_stack_m50, v_stack_m80);
    goto loc_003891E4;
loc_00389572:
    result = CcPerfLogLoggedStreamsStats((unsigned int)(v_stack_p20), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 976)), v_stack_m50, v_stack_m80);
    goto loc_003891F4;
}
```

## 5. (Beta) C Style

```c
int64_t CcLazyWriteScanVolume(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m96;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (192);
    local_rbx = 0;
    result = 0;
    v_stack_m98 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_m50 = 0;
    v_stack_m94 = 0;
    v_stack_m96 = 0;
    v_stack_m97 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x20)) == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3E092) + 0x8))) goto loc_003892BA;
loc_00388E35:
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x20) + 768, v_stack_m78, Arg3, Arg4);
    Arg3 = 0;
    result = CcSetLazyWriteScanQueuedInternal(Arg1 + 920, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg3, Arg4);
    Arg2 = 0;
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x438) = *(uint64_t *)(arg1 + 0x418);
    *(uint64_t *)(arg1 + 0x440) = *(uint64_t *)(arg1 + 0x420);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x428)))) <= 1) goto loc_00389267;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x428)) - 1))) * (*(uint64_t *)(arg1 + 0x418));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) + 0x4900));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x428)) - 1))) * (*(uint64_t *)(arg1 + 0x420));
    Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0x3E0));
loc_00388EC0:
    *(uint64_t *)(arg1 + 0x418) = result;
    *(uint64_t *)(arg1 + 0x420) = Arg2;
    if (*(uint64_t *)(arg1 + 0x3E0) == 0) goto loc_00389334;
loc_00388ED7:
    *(uint64_t *)(arg1 + 0x640) = result;
    v_stack_m88 = v_stack_m90;
    v_stack_m90 = v_stack_m90;
loc_00388EFF:
    if ((*(uint64_t *)(arg1 + 0x310)) != (Arg1 + 784)) goto loc_00389239;
    *(uint8_t *)(arg1 + 0x3DA) = 0;
    result = CcCalculatePagesToWriteForVolume(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg4))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x428)));
    v_stack_m94 = (uint32_t)(result);
    result = CcAdjustThrottleForVolume(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg4))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x428)));
    *(uint64_t *)(arg1 + 0x3E8) = *(uint64_t *)(arg1 + 0x3E0);
    *(uint32_t *)(arg1 + 0x3F0) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0x390) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x430) + (uint32_t)(*(uint32_t *)(Arg2 + 0x98)) * 8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(Arg2 + 0xD8) = result;
    local_rbx = (*(uint64_t *)(arg1 + 0x298)) - (568);
    Arg1 = 0;
loc_00388F8B:
    if (local_rbx == 0) goto loc_0038917D;
    v_stack_m48 = local_rbx + 568;
    if ((local_rbx + 568) == (Arg1 + 664)) goto loc_0038917D;
    result = local_rbx;
    if (0 != 0) { result = 0; }
    v_stack_m58 = result;
    result = CcIsCacheMapACursorInPrivateVCM(0, local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x428)));
    if ((uint8_t)(result) != 0) goto loc_00389019;
    result = (*(uint64_t *)(local_rbx + 0x60)) & (-16);
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_p20));
    Arg2 = 0;
    v_stack_mD8 = result;
    result = CcShouldLazyWriteCacheMap(local_rbx, Arg2, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))));
    if ((uint8_t)(result) != 0) goto loc_00389036;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x98))))) & ((uint32_t)((uint32_t)(0x10020ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x10020ULL)))) goto loc_00389419;
    local_r13 = (uint32_t)((0) + (1));
    if (((uint32_t)(local_r13)) >= 20) goto loc_00389426;
loc_00389019:
    local_rbx = (*(uint64_t *)(local_rbx + 0x238)) - (568);
    if (v_stack_p8 != 0) goto loc_00389466;
loc_0038902D:
    goto loc_00388F8B;
loc_00389036:
    result = CcGetNodeForLazyWrite(local_rbx, 1, (uint32_t)(0x10020ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))));
    if (v_stack_p8 < 0) goto loc_0038927D;
loc_0038905A:
    *(uint32_t *)(local_rbx + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)));
    if (v_stack_p8 < 0) goto loc_003893BE;
loc_00389073:
    if (v_stack_m98 == 0) goto loc_00389141;
loc_0038907D:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, (uint32_t)(*(uint32_t *)(local_rbx + 0x70)), (uint32_t)(0x10020ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))));
    result = CcAllocateWorkQueueEntry(*(uint64_t *)(arg1 + 0x20), 0, result, v_stack_m60);
    if (sign_flag) goto loc_003894AC;
    *(uint32_t *)(v_stack_m60 + 0x80) = 2;
    *(uint64_t *)(v_stack_m60 + 0x10) = local_rbx;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x20) + 768, v_stack_m78, result, v_stack_m60);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x70))) - 1);
    *(uint32_t *)(local_rbx + 0x70) = (uint32_t)(Arg1);
    if (((*(uint32_t *)(local_rbx + 0x98)) & (0x10000ULL)) != 0) goto loc_00389106;
    if ((*(uint32_t *)(local_rbx + 0x4)) == 0) goto loc_00389130;
loc_003890E7:
    *(uint64_t *)(local_rbx + 0x1F8) = v_stack_m60;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x650))))) != 0) goto loc_0038915C;
    goto loc_0038911B;
loc_00389106:
    result = (v_stack_m60) | (1);
    *(uint64_t *)(local_rbx + 0x1F8) = result;
loc_00389118:
loc_0038911B:
    result = CcPostWorkQueue(v_stack_m60, result + 72, result, v_stack_m60);
loc_00389120:
    local_r13 = 0;
    v_stack_m97 = 1;
    goto loc_00389019;
loc_00389130:
    if ((uint32_t)(v_stack_m60) != 0) goto loc_003890E7;
    *(uint64_t *)(local_rbx + 0x1F8) = v_stack_m48;
    goto loc_00389118;
loc_00389141:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC8)))) >= ((uint32_t)((uint32_t)(v_stack_m94)))) goto loc_003892D2;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m94)) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC8)))));
loc_00389153:
    v_stack_m94 = (uint32_t)(local_r12);
    goto loc_0038907D;
loc_0038915C:
    *(uint32_t *)(v_stack_m48 + 0x80) = 7;
    *(uint64_t *)(v_stack_m48 + 0x18) = local_rbx;
    result = CcPostWorkQueueAsyncLazywrite(v_stack_m60, local_r13 + 312, result, v_stack_m60);
    goto loc_00389120;
loc_0038917D:
loc_00389182:
    local_rbx = v_stack_m97;
    if (v_stack_m90 != v_stack_m90) { local_rbx = 1; }
    if (v_stack_m90 != v_stack_m90) goto loc_003894C5;
    if ((*(uint8_t *)(v_rip + 0xC3C074)) == 0) goto loc_00389510;
loc_003891AE:
    if (v_stack_m80 != v_stack_m90) goto loc_00389540;
    *(uint8_t *)(arg1 + 0x2C4) = 1;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x419) = 0;
loc_003891D1:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, 1, result, v_stack_m60);
    if (v_stack_m96 != 0) goto loc_00389565;
loc_003891E4:
    if (((*(uint32_t *)(v_rip + 0xC3D922)) & (0x20000ULL)) != 0) goto loc_00389572;
loc_003891F4:
    if ((*(uint64_t *)(arg1 + 0x450)) != (Arg1 + 1104)) goto loc_00389212;
    goto loc_0038921D;
loc_00389202:
    Arg2 = 0;
    result = CcRescheduleLazyWriteScanOnVolume(v_stack_m78, Arg2, result, v_stack_m60);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, Arg2, result, v_stack_m60);
loc_00389212:
    result = CcPostDeferredWrites(*(uint64_t *)(arg1 + 0x20), Arg1, result, v_stack_m60);
loc_0038921D:
    local_rsp = (local_rsp) + (192);
    return result;
loc_00389239:
    if ((*(uint64_t *)(result + 0x8)) != (*(uint64_t *)(arg1 + 0x20))) goto loc_00389260;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_00389260;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(arg1 + 0x20);
    if ((*(uint64_t *)(v_stack_m88)) == v_stack_m90) goto loc_00389374;
loc_00389260:
loc_00389267:
    goto loc_00388EC0;
loc_0038927D:
    v_stack_m96 = 1;
    if ((*(uint64_t *)(v_stack_p10 + 0x108)) > (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x70))) goto loc_0038938B;
loc_003892B1:
    goto loc_0038905A;
loc_003892BA:
    result = CcScanLogHandleList(*(uint64_t *)(arg1 + 0x20), v_stack_m94, (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))), v_stack_m50);
    goto loc_00388E35;
loc_003892D2:
    if (((*(uint32_t *)(v_stack_p10 + 0x98)) & (512)) != 0) goto loc_00389410;
    if (v_stack_m58 == v_stack_p10) goto loc_00389402;
loc_003892EC:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x298) + 0x8)) != (Arg1 + 664)) goto loc_00389260;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8))) != (Arg1 + 664)) goto loc_00389260;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8)) = *(uint64_t *)(arg1 + 0x298);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x298) + 0x8) = *(uint64_t *)(arg1 + 0x298 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m48 + 0x8))) != v_stack_m48) goto loc_00389260;
    *(uint64_t *)(arg1 + 0x298) = v_stack_m48;
    *(uint64_t *)(arg1 + 0x298 + 0x8) = *(uint64_t *)(v_stack_m48 + 0x8);
    *(void **)(*(uint64_t *)(v_stack_m48 + 0x8)) = Arg1 + 664;
    *(void **)(v_stack_m48 + 0x8) = Arg1 + 664;
loc_00389328:
    local_r12 = 0;
    v_stack_m98 = 1;
    goto loc_00389153;
loc_00389334:
    result = CcIsDirtyCachemapListEmptyForVolume(Arg1, v_stack_m94, (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))), v_stack_m50);
    if ((uint8_t)(result) == 0) goto loc_00388ED7;
    if ((*(uint8_t *)(arg1 + 0x3DA)) != ((uint8_t)(v_stack_p10))) goto loc_00388ED7;
    if ((*(uint64_t *)(arg1 + 0x450)) != (Arg1 + 1104)) goto loc_00389202;
    *(uint8_t *)(arg1 + 0x3D9) = (uint8_t)(v_stack_p10);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, v_stack_m94, (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))), v_stack_m50);
    goto loc_0038921D;
loc_00389374:
    *(uint64_t *)(result + 0x8) = v_stack_m94;
    *(uint64_t *)(result) = v_stack_m90;
    *(uint64_t *)(v_stack_m94) = result;
    v_stack_m88 = result;
    goto loc_00388EFF;
loc_0038938B:
    *(uint64_t *)(v_stack_m94 + 0x70) = v_stack_m78;
    if (((*(uint32_t *)(v_rip + 0xC3D777)) & (0x20000ULL)) == 0) goto loc_003892B1;
    result = (*(uint64_t *)(v_stack_p10 + 0x60)) & (-16);
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x80) = *(uint64_t *)(result + 0x18);
    goto loc_003892B1;
loc_003893BE:
    if (((uint32_t)(v_stack_m94)) < 64) goto loc_00389073;
    result = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68))))) - ((uint32_t)(v_stack_m94)));
    if (((uint32_t)(v_stack_m94)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68))))) { result = (uint32_t)(Arg1); }
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68) = (uint32_t)(result);
    goto loc_00389073;
loc_00389402:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x114)))) & (15)) != 0) goto loc_003892EC;
loc_00389410:
    v_stack_p8 = 1;
    goto loc_00389328;
loc_00389419:
    result = CcIncrementWriteBehindPriority(v_stack_p10, v_stack_m94, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68)), *(uint64_t *)(v_stack_p10 + 0xF8));
    goto loc_00389019;
loc_00389426:
    if ((((uint8_t)(v_stack_p10)) & (32)) != 0) goto loc_00389019;
    Arg1 = (uint32_t)((v_stack_p10) | (32));
    *(uint32_t *)(v_stack_p10 + 0x98) = (uint32_t)(Arg1);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m78, v_stack_m94, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68)), *(uint64_t *)(v_stack_p10 + 0xF8));
    local_r13 = 0;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x20) + 768, v_stack_m78, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68)), *(uint64_t *)(v_stack_p10 + 0xF8));
    goto loc_00389019;
loc_00389466:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x298) + 0x8)) != (Arg1 + 664)) goto loc_00389260;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8))) != (Arg1 + 664)) goto loc_00389260;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8)) = *(uint64_t *)(arg1 + 0x298);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x298) + 0x8) = *(uint64_t *)(arg1 + 0x298 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m48) + 0x8)) != v_stack_m48) goto loc_00389260;
    *(uint64_t *)(arg1 + 0x298) = *(uint64_t *)(v_stack_m48);
    *(uint64_t *)(arg1 + 0x298 + 0x8) = v_stack_m48;
    *(void **)(*(uint64_t *)(v_stack_m48) + 0x8) = Arg1 + 664;
    result = 0;
    v_stack_p8 = 0;
    *(void **)(v_stack_m48) = Arg1 + 664;
    goto loc_0038902D;
loc_003894AC:
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x298 + 0x8), v_stack_m78, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68)), *(uint64_t *)(v_stack_p10 + 0xF8));
    goto loc_00389182;
loc_003894C5:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8) + 0x8)) != v_stack_m90) goto loc_00389260;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x298 + 0x8))) goto loc_00389260;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8)) + 0x8) = v_stack_m90;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x298 + 0x8) + 0x98)) + (104);
    result = CcPostWorkQueue(*(uint64_t *)(arg1 + 0x298 + 0x8), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0xF8) + 0x68)), *(uint64_t *)(v_stack_p10 + 0xF8));
loc_00389510:
    if ((uint8_t)(v_stack_p10) != 0) goto loc_003891AE;
    if ((*(uint64_t *)(arg1 + 0x450)) != (Arg1 + 1104)) goto loc_003891AE;
    result = CcComputeNextScanTime(*(uint64_t *)(arg1 + 0x20), Arg1, v_stack_m50, v_stack_m80);
    goto loc_003891AE;
loc_00389540:
    result = CcRescheduleLazyWriteScanOnVolume(Arg1, v_stack_m80, v_stack_m50, v_stack_m80);
    if ((*(uint8_t *)(arg1 + 0x2C4)) == 0) goto loc_003891D1;
    *(uint8_t *)(arg1 + 0x2C4) = 0;
    goto loc_003891D1;
loc_00389565:
    result = CcUpdateTimeOnLogHandles(*(uint64_t *)(arg1 + 0x20), v_stack_m80, v_stack_m50, v_stack_m80);
    goto loc_003891E4;
loc_00389572:
    result = CcPerfLogLoggedStreamsStats((uint32_t)(v_stack_p20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x3D0)), v_stack_m50, v_stack_m80);
    goto loc_003891F4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x298` | `64` | `R` |
| `Arg1` | `+ 0x2C4` | `8` | `R` |
| `Arg1` | `+ 0x2C4` | `8` | `W` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg1` | `+ 0x390` | `32` | `W` |
| `Arg1` | `+ 0x398` | `64` | `R` |
| `Arg1` | `+ 0x3D9` | `8` | `W` |
| `Arg1` | `+ 0x3DA` | `8` | `R` |
| `Arg1` | `+ 0x3DA` | `8` | `W` |
| `Arg1` | `+ 0x3E0` | `64` | `R` |
| `Arg1` | `+ 0x3E8` | `64` | `W` |
| `Arg1` | `+ 0x3F0` | `32` | `W` |
| `Arg1` | `+ 0x418` | `64` | `R` |
| `Arg1` | `+ 0x418` | `64` | `W` |
| `Arg1` | `+ 0x420` | `64` | `R` |
| `Arg1` | `+ 0x420` | `64` | `W` |
| `Arg1` | `+ 0x428` | `32` | `R` |
| `Arg1` | `+ 0x430` | `64` | `R` |
| `Arg1` | `+ 0x438` | `64` | `W` |
| `Arg1` | `+ 0x440` | `64` | `W` |
| `Arg1` | `+ 0x450` | `64` | `R` |
| `Arg1` | `+ 0x640` | `64` | `W` |
| `Arg1` | `+ 0x650` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00388DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
