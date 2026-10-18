# PoBroadcastSystemState

- RVA: `0x00B761B0`–`0x00B76772` (길이 `1,474` bytes)
- VA: `0x0000000140B761B0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A10B8`
- 디코드: `338`개 명령, `1,474/1,474` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x00B762E8` → [PopFxActivateDevicesForSx](../../text/4A/PopFxActivateDevicesForSx_function_004A0CAC.md) (function, `0x004A0CAC`)
- `0x00B762F6` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (function, `0x004982F8`)
- `0x00B762FD` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B76332` → [PopDiagTraceDevicesLevel](PopDiagTraceDevicesLevel_function_00B76778.md) (function, `0x00B76778`)
- `0x00B7634F` → [PopDiagTraceDevicesLevel](PopDiagTraceDevicesLevel_function_00B76778.md) (function, `0x00B76778`)
- `0x00B763B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B763EB` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B76404` → [BgDisplayFade](../../pagebgfx/BC/BgDisplayFade_function_00BC36A4.md) (function, `0x00BC36A4`)
- `0x00B76450` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00B76481` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (function, `0x009C5874`)
- `0x00B7648F` → [PopSetupSleepNotifies](PopSetupSleepNotifies_function_00B76850.md) (function, `0x00B76850`)
- `0x00B764B2` → [PopDiagTraceDevicesSuspend](../../page/AA/PopDiagTraceDevicesSuspend_function_00AA4950.md) (function, `0x00AA4950`)
- `0x00B764C6` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B76512` → [PopDiagTraceDevicesLevel](PopDiagTraceDevicesLevel_function_00B76778.md) (function, `0x00B76778`)
- `0x00B76529` → [PopDiagTraceDevicesLevel](PopDiagTraceDevicesLevel_function_00B76778.md) (function, `0x00B76778`)
- `0x00B76564` → [PopSleepDeviceList](../../text/43/PopSleepDeviceList_function_00430460.md) (function, `0x00430460`)
- `0x00B76586` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (function, `0x004982F8`)
- `0x00B76596` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B765CB` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x00B765F9` → [PopFxActivateDevicesForSx](../../text/4A/PopFxActivateDevicesForSx_function_004A0CAC.md) (function, `0x004A0CAC`)
- `0x00B7668A` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00B766D9` → [PopFxNotifySxTransitionState](../../page/75/PopFxNotifySxTransitionState_function_007593B0.md) (function, `0x007593B0`)
- `0x00B76722` → [WmiAcquireSmbiosLockExclusive](../../page/7B/WmiAcquireSmbiosLockExclusive_function_007B27E4.md) (function, `0x007B27E4`)
- `0x00B76736` → [PopFxIdleDevicesFromSx](../../text/4B/PopFxIdleDevicesFromSx_function_004B2FB4.md) (function, `0x004B2FB4`)
- `0x00B76752` → [PopWakeDeviceList](../../text/43/PopWakeDeviceList_function_00430238.md) (function, `0x00430238`)
- `0x00B76768` → [PopFxNotifySxTransitionState](../../page/75/PopFxNotifySxTransitionState_function_007593B0.md) (function, `0x007593B0`)

### Direct callers
- [PopDirectedDripsSuspendDevices](../../page/A4/PopDirectedDripsSuspendDevices_function_00A4D474.md) at `0x00A4D5B5`
- [PopDirectedDripsResumeDevices](../../page/A4/PopDirectedDripsResumeDevices_function_00A4DB10.md) at `0x00A4DBEB`
- [sub_00B3BDB8](../../page/B3/Unknown_function_00B3BDB8.md) at `0x00B3BDC6`
- [PnprQuiesceDevices](../B6/PnprQuiesceDevices_function_00B649E4.md) at `0x00B64AD5`
- [PnprQuiesceDevices](../B6/PnprQuiesceDevices_function_00B649E4.md) at `0x00B64AE1`
- [PnprWakeDevices](../B6/PnprWakeDevices_function_00B65614.md) at `0x00B6563D`
- [PopSetDevicesSystemState](PopSetDevicesSystemState_function_00B76110.md) at `0x00B76192`

### Static image references
- `0x00B761CF` → RVA `0x00E0A740` (`.data`; read)
- `0x00B761EB` → RVA `0x00F0BCD0` (`.data`; read)
- `0x00B76229` → RVA `0x00F0BCC4` (`.data`; write)
- `0x00B76257` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x00B76269` → RVA `0x00F0BCC0` (`.data`; write)
- `0x00B76270` → RVA `0x00F0BCC8` (`.data`; write)
- `0x00B762AB` → RVA `0x00F0BCC4` (`.data`; read/write)
- `0x00B762EF` → RVA `0x00014018` (`.rdata`; read)
- `0x00B76302` → RVA `0x00F0C338` (`.data`; write)
- `0x00B7631A` → RVA `0x00F0C680` (`.data`; read)
- `0x00B763E0` → RVA `0x00F0BF60` (`.data`; read)
- `0x00B763F0` → RVA `0x00F0C520` (`.data`; write)
- `0x00B763F7` → RVA `0x00E65EB9` (`.data`; read)
- `0x00B76409` → RVA `0x00E65EB8` (`.data`; write)
- `0x00B76410` → RVA `0x00E65E81` (`.data`; write)
- `0x00B76494` → RVA `0x00F0BCC4` (`.data`; read)
- `0x00B7657F` → RVA `0x00014028` (`.rdata`; read)
- `0x00B765AA` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00B765C4` → RVA `0x00B7FF10` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B7662E` → RVA `0x00F0B6D8` (`.data`; read)
- `0x00B766E3` → RVA `0x00F0C2E4` (`.data`; read)
- `0x00B766F0` → RVA `0x00F0BD80` (`.data`; read)
- `0x00B76715` → RVA `0x00F0BD74` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00B762E8` → [PopFxActivateDevicesForSx](../../text/4A/PopFxActivateDevicesForSx_function_004A0CAC.md) (`PAGELK` → `.text`)
  - `0x00B762F6` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (`PAGELK` → `.text`)
  - `0x00B762FD` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B763B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B763EB` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B76404` → [BgDisplayFade](../../pagebgfx/BC/BgDisplayFade_function_00BC36A4.md) (`PAGELK` → `PAGEBGFX`)
  - `0x00B76450` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGELK` → `.text`)
  - `0x00B76481` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (`PAGELK` → `PAGE`)
  - `0x00B764B2` → [PopDiagTraceDevicesSuspend](../../page/AA/PopDiagTraceDevicesSuspend_function_00AA4950.md) (`PAGELK` → `PAGE`)
  - `0x00B76564` → [PopSleepDeviceList](../../text/43/PopSleepDeviceList_function_00430460.md) (`PAGELK` → `.text`)
  - `0x00B76586` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (`PAGELK` → `.text`)
  - `0x00B765CB` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGELK` → `.text`)
  - `0x00B765F9` → [PopFxActivateDevicesForSx](../../text/4A/PopFxActivateDevicesForSx_function_004A0CAC.md) (`PAGELK` → `.text`)
  - `0x00B7668A` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGELK` → `.text`)
  - `0x00B766D9` → [PopFxNotifySxTransitionState](../../page/75/PopFxNotifySxTransitionState_function_007593B0.md) (`PAGELK` → `PAGE`)
  - `0x00B76722` → [WmiAcquireSmbiosLockExclusive](../../page/7B/WmiAcquireSmbiosLockExclusive_function_007B27E4.md) (`PAGELK` → `PAGE`)
  - `0x00B76736` → [PopFxIdleDevicesFromSx](../../text/4B/PopFxIdleDevicesFromSx_function_004B2FB4.md) (`PAGELK` → `.text`)
  - `0x00B76752` → [PopWakeDeviceList](../../text/43/PopWakeDeviceList_function_00430238.md) (`PAGELK` → `.text`)
  - `0x00B76768` → [PopFxNotifySxTransitionState](../../page/75/PopFxNotifySxTransitionState_function_007593B0.md) (`PAGELK` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00B7636A` → [sub_00B80364 + 0x179](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B76474` → [sub_00B80364 + 0xE1](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B76487` → [sub_00B80364 + 0xE1](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B76535` → [sub_00B80364 + 0x6F](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B766EA` → [sub_00B80364](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B766FD` → [sub_00B80364](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B7671C` → [sub_00B80364 + 0xB](../B8/Unknown_function_00B80364.md) (`tail-transfer`)
  - `0x00B76728` → [sub_00B80364 + 0xB](../B8/Unknown_function_00B80364.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B761B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00B761B5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00B761BA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B761BF  55                              push rbp
00B761C0  41 54                           push r12
00B761C2  41 55                           push r13
00B761C4  41 56                           push r14
00B761C6  41 57                           push r15
00B761C8  48 8B EC                        mov rbp, rsp
00B761CB  48 83 EC 60                     sub rsp, 0x60
00B761CF  48 8B 05 6A 45 29 00            mov rax, qword ptr [rip + 0x29456a]
00B761D6  48 33 C4                        xor rax, rsp
00B761D9  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B761DD  44 8A 71 19                     mov r14b, byte ptr [rcx + 0x19]
00B761E1  48 8D 71 10                     lea rsi, [rcx + 0x10]
00B761E5  8A 41 1A                        mov al, byte ptr [rcx + 0x1a]
00B761E8  45 33 FF                        xor r15d, r15d
00B761EB  48 8B 1D DE 5A 39 00            mov rbx, qword ptr [rip + 0x395ade]
00B761F2  48 8B F9                        mov rdi, rcx
00B761F5  44 88 75 D0                     mov byte ptr [rbp - 0x30], r14b
00B761F9  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00B761FD  88 03                           mov byte ptr [rbx], al
00B761FF  8B 41 04                        mov eax, dword ptr [rcx + 4]
00B76202  89 43 04                        mov dword ptr [rbx + 4], eax
00B76205  44 89 BB C0 01 00 00            mov dword ptr [rbx + 0x1c0], r15d
00B7620C  4C 89 BB C8 01 00 00            mov qword ptr [rbx + 0x1c8], r15
00B76213  66 44 89 BB D1 01 00 00         mov word ptr [rbx + 0x1d1], r15w
00B7621B  44 88 BB D3 01 00 00            mov byte ptr [rbx + 0x1d3], r15b
00B76222  44 88 B3 D0 01 00 00            mov byte ptr [rbx + 0x1d0], r14b
00B76229  44 89 3D 94 5A 39 00            mov dword ptr [rip + 0x395a94], r15d
00B76230  8B 11                           mov edx, dword ptr [rcx]
00B76232  83 E2 0F                        and edx, 0xf
00B76235  C1 E2 10                        shl edx, 0x10
00B76238  89 15 86 5A 39 00               mov dword ptr [rip + 0x395a86], edx
00B7623E  45 84 F6                        test r14b, r14b
00B76241  0F 84 BC 03 00 00               je 0x140b76603
00B76247  81 CA 00 11 00 00               or edx, 0x1100
00B7624D  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00B76251  89 15 6D 5A 39 00               mov dword ptr [rip + 0x395a6d], edx
00B76257  F7 05 AF 08 45 00 00 80 00 00   test dword ptr [rip + 0x4508af], 0x8000
00B76261  41 BC 01 00 00 00               mov r12d, 1
00B76267  8B 06                           mov eax, dword ptr [rsi]
00B76269  44 88 25 50 5A 39 00            mov byte ptr [rip + 0x395a50], r12b
00B76270  89 05 52 5A 39 00               mov dword ptr [rip + 0x395a52], eax
00B76276  0F 85 C9 03 00 00               jne 0x140b76645
00B7627C  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B76280  B9 00 00 00 04                  mov ecx, 0x4000000
00B76285  0F 84 09 04 00 00               je 0x140b76694
00B7628B  44 38 7F 18                     cmp byte ptr [rdi + 0x18], r15b
00B7628F  0F 85 14 04 00 00               jne 0x140b766a9
00B76295  F7 47 14 00 00 00 08            test dword ptr [rdi + 0x14], 0x8000000
00B7629C  0F 85 1D 04 00 00               jne 0x140b766bf
00B762A2  44 8B 6F 14                     mov r13d, dword ptr [rdi + 0x14]
00B762A6  44 23 E9                        and r13d, ecx
00B762A9  74 08                           je 0x140b762b3
00B762AB  0F BA 2D 11 5A 39 00 17         bts dword ptr [rip + 0x395a11], 0x17
00B762B3  45 84 F6                        test r14b, r14b
00B762B6  0F 84 10 04 00 00               je 0x140b766cc
00B762BC  44 88 B3 D0 01 00 00            mov byte ptr [rbx + 0x1d0], r14b
00B762C3  45 84 F6                        test r14b, r14b
00B762C6  0F 84 B3 00 00 00               je 0x140b7637f
00B762CC  44 88 A3 D2 01 00 00            mov byte ptr [rbx + 0x1d2], r12b
00B762D3  C6 03 02                        mov byte ptr [rbx], 2
00B762D6  44 89 63 04                     mov dword ptr [rbx + 4], r12d
00B762DA  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B762DE  74 0F                           je 0x140b762ef
00B762E0  45 85 ED                        test r13d, r13d
00B762E3  74 29                           je 0x140b7630e
00B762E5  41 8B CC                        mov ecx, r12d
00B762E8  E8 BF A9 92 FF                  call 0x1404a0cac
00B762ED  EB 1F                           jmp 0x140b7630e
00B762EF  48 8D 0D 22 DD 49 FF            lea rcx, [rip - 0xb622de]
00B762F6  E8 FD 1F 92 FF                  call 0x1404982f8
00B762FB  33 C9                           xor ecx, ecx
00B762FD  E8 DE 84 80 FF                  call 0x14037e7e0
00B76302  48 89 05 2F 60 39 00            mov qword ptr [rip + 0x39602f], rax
00B76309  80 3B 02                        cmp byte ptr [rbx], 2
00B7630C  74 D2                           je 0x140b762e0
00B7630E  41 8B F7                        mov esi, r15d
00B76311  4C 8D 73 40                     lea r14, [rbx + 0x40]
00B76315  83 FE 04                        cmp esi, 4
00B76318  7F 4C                           jg 0x140b76366
00B7631A  44 38 3D 5F 63 39 00            cmp byte ptr [rip + 0x39635f], r15b
00B76321  0F 85 B1 00 00 00               jne 0x140b763d8
00B76327  44 8A 03                        mov r8b, byte ptr [rbx]
00B7632A  45 8A CC                        mov r9b, r12b
00B7632D  41 8B D4                        mov edx, r12d
00B76330  8B CE                           mov ecx, esi
00B76332  E8 41 04 00 00                  call 0x140b76778
00B76337  41 8B 06                        mov eax, dword ptr [r14]
00B7633A  41 39 46 04                     cmp dword ptr [r14 + 4], eax
00B7633E  0F 82 FC 03 00 00               jb 0x140b76740
00B76344  44 8A 03                        mov r8b, byte ptr [rbx]
00B76347  45 33 C9                        xor r9d, r9d
00B7634A  41 8B D4                        mov edx, r12d
00B7634D  8B CE                           mov ecx, esi
00B7634F  E8 24 04 00 00                  call 0x140b76778
00B76354  41 3B F4                        cmp esi, r12d
00B76357  0F 84 FD 00 00 00               je 0x140b7645a
00B7635D  41 03 F4                        add esi, r12d
00B76360  49 83 C6 48                     add r14, 0x48
00B76364  EB AF                           jmp 0x140b76315
00B76366  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B7636A  0F 84 6D A1 00 00               je 0x140b804dd
00B76370  8A 47 1A                        mov al, byte ptr [rdi + 0x1a]
00B76373  44 8A 75 D0                     mov r14b, byte ptr [rbp - 0x30]
00B76377  88 03                           mov byte ptr [rbx], al
00B76379  8B 47 04                        mov eax, dword ptr [rdi + 4]
00B7637C  89 43 04                        mov dword ptr [rbx + 4], eax
00B7637F  F7 05 87 07 45 00 00 80 00 00   test dword ptr [rip + 0x450787], 0x8000
00B76389  0F 85 8D 00 00 00               jne 0x140b7641c
00B7638F  45 84 F6                        test r14b, r14b
00B76392  0F 85 C4 03 00 00               jne 0x140b7675c
00B76398  0F BA 35 24 59 39 00 17         btr dword ptr [rip + 0x395924], 0x17
00B763A0  44 88 3D 19 59 39 00            mov byte ptr [rip + 0x395919], r15b
00B763A7  8B 83 C0 01 00 00               mov eax, dword ptr [rbx + 0x1c0]
00B763AD  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00B763B1  48 33 CC                        xor rcx, rsp
00B763B4  E8 87 62 B3 FF                  call 0x1406ac640
00B763B9  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00B763BE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00B763C2  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B763C6  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00B763CA  49 8B E3                        mov rsp, r11
00B763CD  41 5F                           pop r15
00B763CF  41 5E                           pop r14
00B763D1  41 5D                           pop r13
00B763D3  41 5C                           pop r12
00B763D5  5D                              pop rbp
00B763D6  C3                              ret
00B763D7  CC                              int3
00B763D8  85 F6                           test esi, esi
00B763DA  0F 85 47 FF FF FF               jne 0x140b76327
00B763E0  44 38 3D 79 5B 39 00            cmp byte ptr [rip + 0x395b79], r15b
00B763E7  74 0E                           je 0x140b763f7
00B763E9  33 C9                           xor ecx, ecx
00B763EB  E8 F0 83 80 FF                  call 0x14037e7e0
00B763F0  48 89 05 29 61 39 00            mov qword ptr [rip + 0x396129], rax
00B763F7  44 38 3D BB FA 2E 00            cmp byte ptr [rip + 0x2efabb], r15b
00B763FE  0F 84 23 FF FF FF               je 0x140b76327
00B76404  E8 9B D2 04 00                  call 0x140bc36a4
00B76409  44 88 3D A8 FA 2E 00            mov byte ptr [rip + 0x2efaa8], r15b
00B76410  44 88 3D 6A FA 2E 00            mov byte ptr [rip + 0x2efa6a], r15b
00B76417  E9 0B FF FF FF                  jmp 0x140b76327
00B7641C  8B 83 C0 01 00 00               mov eax, dword ptr [rbx + 0x1c0]
00B76422  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00B76426  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00B76429  41 B9 25 12 00 00               mov r9d, 0x1225
00B7642F  48 8D 45 D8                     lea rax, [rbp - 0x28]
00B76433  48 C7 45 F0 04 00 00 00         mov qword ptr [rbp - 0x10], 4
00B7643B  41 B8 00 80 00 80               mov r8d, 0x80008000
00B76441  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00B76445  41 8B D4                        mov edx, r12d
00B76448  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
00B76450  E8 FB EE 6B FF                  call 0x140235350
00B76455  E9 35 FF FF FF                  jmp 0x140b7638f
00B7645A  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B7645E  0F 85 F9 FE FF FF               jne 0x140b7635d
00B76464  45 85 ED                        test r13d, r13d
00B76467  0F 85 F0 FE FF FF               jne 0x140b7635d
00B7646D  44 38 BB D4 01 00 00            cmp byte ptr [rbx + 0x1d4], r15b
00B76474  0F 84 CB 9F 00 00               je 0x140b80445
00B7647A  44 88 BB D4 01 00 00            mov byte ptr [rbx + 0x1d4], r15b
00B76481  E8 EE F3 E4 FF                  call 0x1409c5874
00B76486  90                              nop
00B76487  E9 B9 9F 00 00                  jmp 0x140b80445
00B7648C  48 8B CB                        mov rcx, rbx
00B7648F  E8 BC 03 00 00                  call 0x140b76850
00B76494  8B 15 2A 58 39 00               mov edx, dword ptr [rip + 0x39582a]
00B7649A  44 8B C2                        mov r8d, edx
00B7649D  41 C1 E8 0C                     shr r8d, 0xc
00B764A1  C1 EA 08                        shr edx, 8
00B764A4  41 83 E0 0F                     and r8d, 0xf
00B764A8  83 E2 0F                        and edx, 0xf
00B764AB  80 7F 1A 03                     cmp byte ptr [rdi + 0x1a], 3
00B764AF  0F 94 C1                        sete cl
00B764B2  E8 99 E4 F2 FF                  call 0x140aa4950
00B764B7  80 7F 1A 03                     cmp byte ptr [rdi + 0x1a], 3
00B764BB  B9 0B 00 00 00                  mov ecx, 0xb
00B764C0  8D 41 03                        lea eax, [rcx + 3]
00B764C3  0F 45 C8                        cmovne ecx, eax
00B764C6  E8 C5 17 00 00                  call 0x140b77c90
00B764CB  8B 06                           mov eax, dword ptr [rsi]
00B764CD  83 F8 04                        cmp eax, 4
00B764D0  0F 84 0D 02 00 00               je 0x140b766e3
00B764D6  83 F8 02                        cmp eax, 2
00B764D9  0F 84 0B 01 00 00               je 0x140b765ea
00B764DF  4D 8B F7                        mov r14, r15
00B764E2  83 F8 03                        cmp eax, 3
00B764E5  0F 84 FF 00 00 00               je 0x140b765ea
00B764EB  BE 04 00 00 00                  mov esi, 4
00B764F0  4C 8D A3 60 01 00 00            lea r12, [rbx + 0x160]
00B764F7  44 8B FE                        mov r15d, esi
00B764FA  4D 3B FE                        cmp r15, r14
00B764FD  7C 6C                           jl 0x140b7656b
00B764FF  83 FE 01                        cmp esi, 1
00B76502  0F 84 FA 01 00 00               je 0x140b76702
00B76508  44 8A 03                        mov r8b, byte ptr [rbx]
00B7650B  41 B1 01                        mov r9b, 1
00B7650E  33 D2                           xor edx, edx
00B76510  8B CE                           mov ecx, esi
00B76512  E8 61 02 00 00                  call 0x140b76778
00B76517  33 C9                           xor ecx, ecx
00B76519  41 39 0C 24                     cmp dword ptr [r12], ecx
00B7651D  77 27                           ja 0x140b76546
00B7651F  44 8A 03                        mov r8b, byte ptr [rbx]
00B76522  45 33 C9                        xor r9d, r9d
00B76525  33 D2                           xor edx, edx
00B76527  8B CE                           mov ecx, esi
00B76529  E8 4A 02 00 00                  call 0x140b76778
00B7652E  83 BB C0 01 00 00 00            cmp dword ptr [rbx + 0x1c0], 0
00B76535  0F 8C 98 9E 00 00               jl 0x140b803d3
00B7653B  FF CE                           dec esi
00B7653D  49 FF CF                        dec r15
00B76540  49 83 EC 48                     sub r12, 0x48
00B76544  EB B4                           jmp 0x140b764fa
00B76546  39 4F 14                        cmp dword ptr [rdi + 0x14], ecx
00B76549  7D 07                           jge 0x140b76552
00B7654B  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
00B7654F  48 89 08                        mov qword ptr [rax], rcx
00B76552  48 63 C6                        movsxd rax, esi
00B76555  48 8D 48 01                     lea rcx, [rax + 1]
00B76559  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00B7655D  48 8D 14 CB                     lea rdx, [rbx + rcx*8]
00B76561  48 8B CB                        mov rcx, rbx
00B76564  E8 F7 9E 8B FF                  call 0x140430460
00B76569  EB B4                           jmp 0x140b7651f
00B7656B  44 8A 75 D0                     mov r14b, byte ptr [rbp - 0x30]
00B7656F  45 33 FF                        xor r15d, r15d
00B76572  45 8D 67 01                     lea r12d, [r15 + 1]
00B76576  80 3B 02                        cmp byte ptr [rbx], 2
00B76579  0F 84 AE 01 00 00               je 0x140b7672d
00B7657F  48 8D 0D A2 DA 49 FF            lea rcx, [rip - 0xb6255e]
00B76586  E8 6D 1D 92 FF                  call 0x1404982f8
00B7658B  80 7F 1A 03                     cmp byte ptr [rdi + 0x1a], 3
00B7658F  75 19                           jne 0x140b765aa
00B76591  B9 0C 00 00 00                  mov ecx, 0xc
00B76596  E8 F5 16 00 00                  call 0x140b77c90
00B7659B  EB 0D                           jmp 0x140b765aa
00B7659D  44 39 BB C0 01 00 00            cmp dword ptr [rbx + 0x1c0], r15d
00B765A4  0F 8D E2 FE FF FF               jge 0x140b7648c
00B765AA  F7 05 58 69 39 00 00 00 02 00   test dword ptr [rip + 0x396958], 0x20000
00B765B4  0F 84 02 FD FF FF               je 0x140b762bc
00B765BA  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B765BE  0F 85 F8 FC FF FF               jne 0x140b762bc
00B765C4  48 8D 0D 45 99 00 00            lea rcx, [rip + 0x9945]
00B765CB  E8 E0 26 7E FF                  call 0x140358cb0
00B765D0  44 88 65 D0                     mov byte ptr [rbp - 0x30], r12b
00B765D4  C7 83 C0 01 00 00 01 00 00 C0   mov dword ptr [rbx + 0x1c0], 0xc0000001
00B765DE  44 88 A3 D0 01 00 00            mov byte ptr [rbx + 0x1d0], r12b
00B765E5  E9 E2 FC FF FF                  jmp 0x140b762cc
00B765EA  80 3B 02                        cmp byte ptr [rbx], 2
00B765ED  4D 8B F7                        mov r14, r15
00B765F0  0F 85 F5 FE FF FF               jne 0x140b764eb
00B765F6  41 8B CC                        mov ecx, r12d
00B765F9  E8 AE A6 92 FF                  call 0x1404a0cac
00B765FE  E9 E8 FE FF FF                  jmp 0x140b764eb
00B76603  8B 41 08                        mov eax, dword ptr [rcx + 8]
00B76606  83 E0 0F                        and eax, 0xf
00B76609  C1 E0 08                        shl eax, 8
00B7660C  0B C2                           or eax, edx
00B7660E  89 05 B0 56 39 00               mov dword ptr [rip + 0x3956b0], eax
00B76614  8B 51 04                        mov edx, dword ptr [rcx + 4]
00B76617  83 E2 0F                        and edx, 0xf
00B7661A  C1 E2 0C                        shl edx, 0xc
00B7661D  0B D0                           or edx, eax
00B7661F  89 15 9F 56 39 00               mov dword ptr [rip + 0x39569f], edx
00B76625  83 3E 05                        cmp dword ptr [rsi], 5
00B76628  0F 85 29 FC FF FF               jne 0x140b76257
00B7662E  8A 05 A4 50 39 00               mov al, byte ptr [rip + 0x3950a4]
00B76634  F6 D8                           neg al
00B76636  1B C9                           sbb ecx, ecx
00B76638  81 E1 00 00 40 00               and ecx, 0x400000
00B7663E  0B D1                           or edx, ecx
00B76640  E9 0C FC FF FF                  jmp 0x140b76251
00B76645  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B76648  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00B7664C  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00B76650  41 B9 24 12 00 00               mov r9d, 0x1224
00B76656  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00B76659  41 B8 00 80 00 80               mov r8d, 0x80008000
00B7665F  8A 47 1A                        mov al, byte ptr [rdi + 0x1a]
00B76662  41 8B D4                        mov edx, r12d
00B76665  88 45 DE                        mov byte ptr [rbp - 0x22], al
00B76668  8A 47 18                        mov al, byte ptr [rdi + 0x18]
00B7666B  88 45 DD                        mov byte ptr [rbp - 0x23], al
00B7666E  48 8D 45 D8                     lea rax, [rbp - 0x28]
00B76672  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00B76676  44 88 75 DC                     mov byte ptr [rbp - 0x24], r14b
00B7667A  48 C7 45 F0 08 00 00 00         mov qword ptr [rbp - 0x10], 8
00B76682  C7 44 24 20 02 18 50 00         mov dword ptr [rsp + 0x20], 0x501802
00B7668A  E8 C1 EC 6B FF                  call 0x140235350
00B7668F  E9 E8 FB FF FF                  jmp 0x140b7627c
00B76694  85 4F 14                        test dword ptr [rdi + 0x14], ecx
00B76697  0F 85 EE FB FF FF               jne 0x140b7628b
00B7669D  44 88 A3 D2 01 00 00            mov byte ptr [rbx + 0x1d2], r12b
00B766A4  E9 E2 FB FF FF                  jmp 0x140b7628b
00B766A9  80 7F 1A 03                     cmp byte ptr [rdi + 0x1a], 3
00B766AD  0F 85 E2 FB FF FF               jne 0x140b76295
00B766B3  44 88 A3 D3 01 00 00            mov byte ptr [rbx + 0x1d3], r12b
00B766BA  E9 D6 FB FF FF                  jmp 0x140b76295
00B766BF  0F BA 2D FD 55 39 00 15         bts dword ptr [rip + 0x3955fd], 0x15
00B766C7  E9 D6 FB FF FF                  jmp 0x140b762a2
00B766CC  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B766D0  0F 85 C7 FE FF FF               jne 0x140b7659d
00B766D6  41 8A CC                        mov cl, r12b
00B766D9  E8 D2 2C BE FF                  call 0x1407593b0
00B766DE  E9 BA FE FF FF                  jmp 0x140b7659d
00B766E3  44 38 3D FA 5B 39 00            cmp byte ptr [rip + 0x395bfa], r15b
00B766EA  0F 85 74 9C 00 00               jne 0x140b80364
00B766F0  4C 39 3D 89 56 39 00            cmp qword ptr [rip + 0x395689], r15
00B766F7  0F 84 E2 FD FF FF               je 0x140b764df
00B766FD  E9 62 9C 00 00                  jmp 0x140b80364
00B76702  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B76706  0F 85 FC FD FF FF               jne 0x140b76508
00B7670C  45 85 ED                        test r13d, r13d
00B7670F  0F 85 F3 FD FF FF               jne 0x140b76508
00B76715  83 3D 58 56 39 00 05            cmp dword ptr [rip + 0x395658], 5
00B7671C  0F 85 4D 9C 00 00               jne 0x140b8036f
00B76722  E8 BD C0 C3 FF                  call 0x1407b27e4
00B76727  90                              nop
00B76728  E9 42 9C 00 00                  jmp 0x140b8036f
00B7672D  45 85 ED                        test r13d, r13d
00B76730  0F 84 49 FE FF FF               je 0x140b7657f
00B76736  E8 79 C8 93 FF                  call 0x1404b2fb4
00B7673B  E9 3F FE FF FF                  jmp 0x140b7657f
00B76740  48 63 C6                        movsxd rax, esi
00B76743  48 8D 48 01                     lea rcx, [rax + 1]
00B76747  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00B7674B  48 8D 14 CB                     lea rdx, [rbx + rcx*8]
00B7674F  48 8B CB                        mov rcx, rbx
00B76752  E8 E1 9A 8B FF                  call 0x140430238
00B76757  E9 E8 FB FF FF                  jmp 0x140b76344
00B7675C  80 7F 1A 02                     cmp byte ptr [rdi + 0x1a], 2
00B76760  0F 85 32 FC FF FF               jne 0x140b76398
00B76766  33 C9                           xor ecx, ecx
00B76768  E8 43 2C BE FF                  call 0x1407593b0
00B7676D  E9 26 FC FF FF                  jmp 0x140b76398
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoBroadcastSystemState(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m4A;
    unsigned __int8 v_stack_m4B;
    unsigned __int8 v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 2704746)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r15 = 0;
    v_stack_m58 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 25));
    v_stack_m48 = a1 + 16;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 26));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 448) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3758814) + 456) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3758814) + 465) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814) + 467) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814) + 464) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 25));
    *(unsigned int *)(v_rip + 3758740) = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (15));
    a2 = (unsigned int)((a2) << (16));
    *(unsigned int *)(v_rip + 3758726) = (unsigned int)(a2);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 25)) == 0) goto loc_00B76603;
    a2 = (unsigned int)((a2) | (0x1100ULL));
    v_stack_m48 = a1 + 16;
loc_00B76251:
    *(unsigned int *)(v_rip + 3758701) = (unsigned int)(a2);
loc_00B76257:
    *(unsigned __int8 *)(v_rip + 3758672) = 1;
    *(unsigned int *)(v_rip + 3758674) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    if (((*(unsigned int *)(v_rip + 4524207)) & (0x8000ULL)) != 0) goto loc_00B76645;
loc_00B7627C:
    if ((*(unsigned __int8 *)(a1 + 26)) == 2) goto loc_00B76694;
loc_00B7628B:
    if ((*(unsigned __int8 *)(a1 + 24)) != 0) goto loc_00B766A9;
loc_00B76295:
    if (((*(unsigned int *)(a1 + 20)) & (0x8000000ULL)) != 0) goto loc_00B766BF;
loc_00B762A2:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 20))) & ((unsigned int)((unsigned int)(0x4000000ULL))));
    if (!(condition_is_equal)) {
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 25)) == 0) goto loc_00B766CC;
loc_00B762BC:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814) + 464) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 25));
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 25)) == 0) goto loc_00B7637F;
loc_00B762CC:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814) + 466) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)) = 2;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 4) = 1;
    if ((*(unsigned __int8 *)(a1 + 26)) == 2) goto loc_00B762EF;
loc_00B762E0:
    if ((unsigned int)(v_r13) == 0) goto loc_00B7630E;
    result = PopFxActivateDevicesForSx(1, a2, a3, a4);
    goto loc_00B7630E;
loc_00B762EF:
    result = PopDiagTraceEventNoPayload(v_rip - 11936478, a2, a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3760175) = result;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814))) == 2) goto loc_00B762E0;
loc_00B7630E:
loc_00B76315:
    if (0 > 4) goto loc_00B76366;
    if ((*(unsigned __int8 *)(v_rip + 3760991)) != 0) goto loc_00B763D8;
loc_00B76327:
    result = PopDiagTraceDevicesLevel(0, 1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)), 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 64 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 64))))) goto loc_00B76740;
loc_00B76344:
    a4 = 0;
    result = PopDiagTraceDevicesLevel(0, 1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)), a4);
    if (0 == 1) goto loc_00B7645A;
loc_00B7635D:
    v_rsi = (unsigned int)((0) + (1));
    v_r14 = (*(unsigned __int64 *)(v_rip + 3758814) + 64) + (72);
    goto loc_00B76315;
loc_00B76366:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 26));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3758814) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
loc_00B7637F:
    if (((*(unsigned int *)(v_rip + 4523911)) & (0x8000ULL)) != 0) goto loc_00B7641C;
loc_00B7638F:
    if ((unsigned __int8)(v_stack_m58) != 0) goto loc_00B7675C;
loc_00B76398:
    *(unsigned __int8 *)(v_rip + 3758361) = 0;
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)), a4);
    return result;
loc_00B763D8:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_00B76327;
    if ((*(unsigned __int8 *)(v_rip + 3758969)) != 0) {
        a1 = 0;
        result = KeQueryPerformanceCounter(a1, 1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)), a4);
        *(unsigned __int64 *)(v_rip + 3760425) = result;
    }
    if ((*(unsigned __int8 *)(v_rip + 3078843)) == 0) goto loc_00B76327;
    result = BgDisplayFade(a1, 1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3758814)), a4);
    *(unsigned __int8 *)(v_rip + 3078824) = 0;
    *(unsigned __int8 *)(v_rip + 3078762) = 0;
    goto loc_00B76327;
loc_00B7641C:
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 448)));
    v_stack_m38 = 4;
    v_stack_m40 = v_stack_m50;
    v_stack_m40 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m40, 1, (unsigned int)(0x80008000ULL), (unsigned int)(0x1225ULL));
    goto loc_00B7638F;
loc_00B7645A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 2) goto loc_00B7635D;
    if ((unsigned int)(v_r13) != 0) goto loc_00B7635D;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 468) = 0;
    result = ExReleaseTimeRefreshLockExclusive(v_stack_m40, 1, (unsigned int)(0x80008000ULL), (unsigned int)(0x1225ULL));
loc_00B7648C:
    result = PopSetupSleepNotifies(*(unsigned __int64 *)(v_stack_m28 + 56), 1, (unsigned int)(0x80008000ULL), (unsigned int)(0x1225ULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3758122))))) >> (12));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3758122))) >> (8));
    a3 = (unsigned int)((a3) & (15));
    a2 = (unsigned int)((a2) & (15));
    a1 = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) == 3) ? 1 : 0;
    result = PopDiagTraceDevicesSuspend(a1, a2, a3, (unsigned int)(0x1225ULL));
    a1 = 11;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 3) { a1 = (unsigned int)(11 + 3); }
    result = PopCheckpointSystemSleep(a1, a2, a3, (unsigned int)(0x1225ULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) == 4) goto loc_00B766E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) == 2) goto loc_00B765EA;
loc_00B764DF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) == 3) goto loc_00B765EA;
loc_00B764EB:
loc_00B764FA:
    if (4 < 0) goto loc_00B7656B;
    if (4 == 1) goto loc_00B76702;
loc_00B76508:
    a2 = 0;
    result = PopDiagTraceDevicesLevel(4, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), 1);
    a1 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 352)) > 0) goto loc_00B76546;
loc_00B7651F:
    a4 = 0;
    a2 = 0;
    result = PopDiagTraceDevicesLevel(4, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    v_rsi = (unsigned int)((4) - 1);
    v_r15 = (4) - 1;
    v_r12 = (*(unsigned __int64 *)(v_stack_m28 + 56) + 352) - (72);
    goto loc_00B764FA;
loc_00B76546:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 20)) < 4) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56);
        *(unsigned __int64 *)(result) = 4;
    }
    result = PopSleepDeviceList(*(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    goto loc_00B7651F;
loc_00B7656B:
    v_r15 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) == 2) goto loc_00B7672D;
loc_00B7657F:
    result = PopDiagTraceEventNoPayload(v_rip - 11937118, *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 3) goto loc_00B765AA;
    result = PopCheckpointSystemSleep(12, *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    goto loc_00B765AA;
loc_00B7659D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 448)) >= 0) goto loc_00B7648C;
loc_00B765AA:
    if (((*(unsigned int *)(v_rip + 3762520)) & (0x20000ULL)) == 0) goto loc_00B762BC;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 2) goto loc_00B762BC;
    result = DbgPrint(v_rip + 39237, *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    v_stack_m58 = (unsigned __int8)(v_r15 + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 448) = 0xC0000001ULL;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 464) = (unsigned __int8)(v_r15 + 1);
    goto loc_00B762CC;
loc_00B765EA:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) != 2) goto loc_00B764EB;
    result = PopFxActivateDevicesForSx((unsigned int)((unsigned int)(v_r15 + 1)), *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)), a4);
    goto loc_00B764EB;
loc_00B76603:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15 + 1)) + 8))) & (15));
    result = (unsigned int)((result) << (8));
    result = (unsigned int)((result) | ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8)));
    *(unsigned int *)(v_rip + 3757744) = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r15 + 1)) + 4))) & (15));
    a2 = (unsigned int)((a2) << (12));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    *(unsigned int *)(v_rip + 3757727) = (unsigned int)(a2);
    if ((*(unsigned int *)(v_rsi)) != 5) goto loc_00B76257;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 3756196)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + 1))) & (0x400000ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    goto loc_00B76251;
loc_00B76645:
    v_stack_m50 = 0;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 4)));
    v_stack_m4A = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26));
    v_stack_m4B = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24));
    v_stack_m40 = v_stack_m50;
    v_stack_m4C = 0;
    v_stack_m38 = 8;
    v_stack_m40 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m40, (unsigned int)((unsigned int)(v_r15 + 1)), (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
    goto loc_00B7627C;
loc_00B76694:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 20)) & ((unsigned int)(v_stack_m40))) != 0) goto loc_00B7628B;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 466) = (unsigned __int8)(v_r15 + 1);
    goto loc_00B7628B;
loc_00B766A9:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 3) goto loc_00B76295;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 467) = (unsigned __int8)(v_r15 + 1);
    goto loc_00B76295;
loc_00B766BF:
    goto loc_00B762A2;
loc_00B766CC:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 2) goto loc_00B7659D;
    result = PopFxNotifySxTransitionState((unsigned __int8)(v_r15 + 1), (unsigned int)((unsigned int)(v_r15 + 1)), (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
    goto loc_00B7659D;
loc_00B766E3:
    if ((*(unsigned __int64 *)(v_rip + 3757705)) == 0) goto loc_00B764DF;
loc_00B76702:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 2) goto loc_00B76508;
    if ((unsigned int)(v_r13) != 0) goto loc_00B76508;
    result = WmiAcquireSmbiosLockExclusive((unsigned __int8)(v_r15 + 1), (unsigned int)((unsigned int)(v_r15 + 1)), (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
loc_00B7672D:
    if ((unsigned int)(v_r13) == 0) goto loc_00B7657F;
    result = PopFxIdleDevicesFromSx((unsigned __int8)(v_r15 + 1), (unsigned int)((unsigned int)(v_r15 + 1)), (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
    goto loc_00B7657F;
loc_00B76740:
    result = PopWakeDeviceList(*(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
    goto loc_00B76344;
loc_00B7675C:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 26)) != 2) goto loc_00B76398;
    a1 = 0;
    result = PopFxNotifySxTransitionState(a1, *(unsigned __int64 *)(v_stack_m28 + 56) + (int)((unsigned int)(v_rsi)) + (int)((unsigned int)(v_rsi)) + 1 * 8 * 8, (unsigned int)(0x80008000ULL), (unsigned int)(0x1224ULL));
    goto loc_00B76398;
}
```

## 5. (Beta) C Style

```c
int64_t PoBroadcastSystemState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m4A;
    uint8_t v_stack_m4B;
    uint8_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint8_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x29456A)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r15 = 0;
    v_stack_m58 = (uint8_t)(*(uint8_t *)(arg1 + 0x19));
    v_stack_m48 = Arg1 + 16;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)) = (uint8_t)(*(uint8_t *)(arg1 + 0x1A));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1C0) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1C8) = 0;
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1D1) = 0;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1D3) = 0;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1D0) = (uint8_t)(*(uint8_t *)(arg1 + 0x19));
    *(uint32_t *)(v_rip + 0x395A94) = 0;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (15));
    a2 = (uint32_t)((a2) << (16));
    *(uint32_t *)(v_rip + 0x395A86) = (uint32_t)(a2);
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x19)) == 0) goto loc_00B76603;
    a2 = (uint32_t)((a2) | (0x1100ULL));
    v_stack_m48 = Arg1 + 16;
loc_00B76251:
    *(uint32_t *)(v_rip + 0x395A6D) = (uint32_t)(a2);
loc_00B76257:
    *(uint8_t *)(v_rip + 0x395A50) = 1;
    *(uint32_t *)(v_rip + 0x395A52) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if (((*(uint32_t *)(v_rip + 0x4508AF)) & (0x8000ULL)) != 0) goto loc_00B76645;
loc_00B7627C:
    if ((*(uint8_t *)(arg1 + 0x1A)) == 2) goto loc_00B76694;
loc_00B7628B:
    if ((*(uint8_t *)(arg1 + 0x18)) != 0) goto loc_00B766A9;
loc_00B76295:
    if (((*(uint32_t *)(arg1 + 0x14)) & (0x8000000ULL)) != 0) goto loc_00B766BF;
loc_00B762A2:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x14))) & ((uint32_t)((uint32_t)(0x4000000ULL))));
    if (!(condition_is_equal)) {
    }
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x19)) == 0) goto loc_00B766CC;
loc_00B762BC:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1D0) = (uint8_t)(*(uint8_t *)(arg1 + 0x19));
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x19)) == 0) goto loc_00B7637F;
loc_00B762CC:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x1D2) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)) = 2;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x4) = 1;
    if ((*(uint8_t *)(arg1 + 0x1A)) == 2) goto loc_00B762EF;
loc_00B762E0:
    if ((uint32_t)(local_r13) == 0) goto loc_00B7630E;
    result = PopFxActivateDevicesForSx(1, a2, a3, a4);
    goto loc_00B7630E;
loc_00B762EF:
    result = PopDiagTraceEventNoPayload(v_rip - 11936478, a2, a3, a4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, a2, a3, a4);
    *(uint64_t *)(v_rip + 0x39602F) = result;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE))) == 2) goto loc_00B762E0;
loc_00B7630E:
loc_00B76315:
    if (0 > 4) goto loc_00B76366;
    if ((*(uint8_t *)(v_rip + 0x39635F)) != 0) goto loc_00B763D8;
loc_00B76327:
    result = PopDiagTraceDevicesLevel(0, 1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)), 1);
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x40 + 0x4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x40))))) goto loc_00B76740;
loc_00B76344:
    a4 = 0;
    result = PopDiagTraceDevicesLevel(0, 1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)), a4);
    if (0 == 1) goto loc_00B7645A;
loc_00B7635D:
    local_rsi = (uint32_t)((0) + (1));
    local_r14 = (*(uint64_t *)(v_rip + 0x395ADE) + 64) + (72);
    goto loc_00B76315;
loc_00B76366:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)) = (uint8_t)(*(uint8_t *)(arg1 + 0x1A));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x395ADE) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
loc_00B7637F:
    if (((*(uint32_t *)(v_rip + 0x450787)) & (0x8000ULL)) != 0) goto loc_00B7641C;
loc_00B7638F:
    if ((uint8_t)(v_stack_m58) != 0) goto loc_00B7675C;
loc_00B76398:
    *(uint8_t *)(v_rip + 0x395919) = 0;
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)), a4);
    return result;
loc_00B763D8:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_00B76327;
    if ((*(uint8_t *)(v_rip + 0x395B79)) != 0) {
        Arg1 = 0;
        result = KeQueryPerformanceCounter(Arg1, 1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)), a4);
        *(uint64_t *)(v_rip + 0x396129) = result;
    }
    if ((*(uint8_t *)(v_rip + 0x2EFABB)) == 0) goto loc_00B76327;
    result = BgDisplayFade(Arg1, 1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x395ADE)), a4);
    *(uint8_t *)(v_rip + 0x2EFAA8) = 0;
    *(uint8_t *)(v_rip + 0x2EFA6A) = 0;
    goto loc_00B76327;
loc_00B7641C:
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1C0)));
    v_stack_m38 = 4;
    v_stack_m40 = v_stack_m50;
    v_stack_m40 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m40, 1, (uint32_t)(0x80008000ULL), (uint32_t)(0x1225ULL));
    goto loc_00B7638F;
loc_00B7645A:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 2) goto loc_00B7635D;
    if ((uint32_t)(local_r13) != 0) goto loc_00B7635D;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1D4) = 0;
    result = ExReleaseTimeRefreshLockExclusive(v_stack_m40, 1, (uint32_t)(0x80008000ULL), (uint32_t)(0x1225ULL));
loc_00B7648C:
    result = PopSetupSleepNotifies(*(uint64_t *)(v_stack_m28 + 0x38), 1, (uint32_t)(0x80008000ULL), (uint32_t)(0x1225ULL));
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x39582A))))) >> (12));
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x39582A))) >> (8));
    a3 = (uint32_t)((a3) & (15));
    a2 = (uint32_t)((a2) & (15));
    Arg1 = ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) == 3) ? 1 : 0;
    result = PopDiagTraceDevicesSuspend(Arg1, a2, a3, (uint32_t)(0x1225ULL));
    Arg1 = 11;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 3) { Arg1 = (uint32_t)(11 + 3); }
    result = PopCheckpointSystemSleep(Arg1, a2, a3, (uint32_t)(0x1225ULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) == 4) goto loc_00B766E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) == 2) goto loc_00B765EA;
loc_00B764DF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) == 3) goto loc_00B765EA;
loc_00B764EB:
loc_00B764FA:
    if (4 < 0) goto loc_00B7656B;
    if (4 == 1) goto loc_00B76702;
loc_00B76508:
    a2 = 0;
    result = PopDiagTraceDevicesLevel(4, a2, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), 1);
    Arg1 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x160)) > 0) goto loc_00B76546;
loc_00B7651F:
    a4 = 0;
    a2 = 0;
    result = PopDiagTraceDevicesLevel(4, a2, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    local_rsi = (uint32_t)((4) - 1);
    local_r15 = (4) - 1;
    local_r12 = (*(uint64_t *)(v_stack_m28 + 0x38) + 352) - (72);
    goto loc_00B764FA;
loc_00B76546:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x14)) < 4) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38);
        *(uint64_t *)(result) = 4;
    }
    result = PopSleepDeviceList(*(uint64_t *)(v_stack_m28 + 0x38), *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    goto loc_00B7651F;
loc_00B7656B:
    local_r15 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) == 2) goto loc_00B7672D;
loc_00B7657F:
    result = PopDiagTraceEventNoPayload(v_rip - 11937118, *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 3) goto loc_00B765AA;
    result = PopCheckpointSystemSleep(12, *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    goto loc_00B765AA;
loc_00B7659D:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1C0)) >= 0) goto loc_00B7648C;
loc_00B765AA:
    if (((*(uint32_t *)(v_rip + 0x396958)) & (0x20000ULL)) == 0) goto loc_00B762BC;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 2) goto loc_00B762BC;
    result = DbgPrint(v_rip + 39237, *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    v_stack_m58 = (uint8_t)(local_r15 + 1);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1C0) = 0xC0000001ULL;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1D0) = (uint8_t)(local_r15 + 1);
    goto loc_00B762CC;
loc_00B765EA:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) != 2) goto loc_00B764EB;
    result = PopFxActivateDevicesForSx((uint32_t)((uint32_t)(local_r15 + 1)), *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)), a4);
    goto loc_00B764EB;
loc_00B76603:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15 + 0x1)) + 0x8))) & (15));
    result = (uint32_t)((result) << (8));
    result = (uint32_t)((result) | ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8)));
    *(uint32_t *)(v_rip + 0x3956B0) = (uint32_t)(result);
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r15 + 0x1)) + 0x4))) & (15));
    a2 = (uint32_t)((a2) << (12));
    a2 = (uint32_t)((a2) | ((uint32_t)(result)));
    *(uint32_t *)(v_rip + 0x39569F) = (uint32_t)(a2);
    if ((*(uint32_t *)(local_rsi)) != 5) goto loc_00B76257;
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0x3950A4)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + 1))) & (0x400000ULL));
    a2 = (uint32_t)((a2) | ((uint32_t)(Arg1)));
    goto loc_00B76251;
loc_00B76645:
    v_stack_m50 = 0;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4)));
    v_stack_m4A = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A));
    v_stack_m4B = (uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18));
    v_stack_m40 = v_stack_m50;
    v_stack_m4C = 0;
    v_stack_m38 = 8;
    v_stack_m40 = 0x501802ULL;
    result = EtwTraceKernelEvent(v_stack_m40, (uint32_t)((uint32_t)(local_r15 + 1)), (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
    goto loc_00B7627C;
loc_00B76694:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x14)) & ((uint32_t)(v_stack_m40))) != 0) goto loc_00B7628B;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1D2) = (uint8_t)(local_r15 + 1);
    goto loc_00B7628B;
loc_00B766A9:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 3) goto loc_00B76295;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x1D3) = (uint8_t)(local_r15 + 1);
    goto loc_00B76295;
loc_00B766BF:
    goto loc_00B762A2;
loc_00B766CC:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 2) goto loc_00B7659D;
    result = PopFxNotifySxTransitionState((uint8_t)(local_r15 + 1), (uint32_t)((uint32_t)(local_r15 + 1)), (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
    goto loc_00B7659D;
loc_00B766E3:
    if ((*(uint64_t *)(v_rip + 0x395689)) == 0) goto loc_00B764DF;
loc_00B76702:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 2) goto loc_00B76508;
    if ((uint32_t)(local_r13) != 0) goto loc_00B76508;
    result = WmiAcquireSmbiosLockExclusive((uint8_t)(local_r15 + 1), (uint32_t)((uint32_t)(local_r15 + 1)), (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
loc_00B7672D:
    if ((uint32_t)(local_r13) == 0) goto loc_00B7657F;
    result = PopFxIdleDevicesFromSx((uint8_t)(local_r15 + 1), (uint32_t)((uint32_t)(local_r15 + 1)), (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
    goto loc_00B7657F;
loc_00B76740:
    result = PopWakeDeviceList(*(uint64_t *)(v_stack_m28 + 0x38), *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
    goto loc_00B76344;
loc_00B7675C:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1A)) != 2) goto loc_00B76398;
    Arg1 = 0;
    result = PopFxNotifySxTransitionState(Arg1, *(uint64_t *)(v_stack_m28 + 0x38) + (int32_t)((uint32_t)(local_rsi)) + (int32_t)((uint32_t)(local_rsi)) + 1 * 8 * 8, (uint32_t)(0x80008000ULL), (uint32_t)(0x1224ULL));
    goto loc_00B76398;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x19` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B761B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
