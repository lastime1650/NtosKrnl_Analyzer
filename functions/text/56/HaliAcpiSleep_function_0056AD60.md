# HaliAcpiSleep

- RVA: `0x0056AD60`–`0x0056B30B` (길이 `1,451` bytes)
- VA: `0x000000014056AD60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3904`
- 디코드: `392`개 명령, `1,451/1,451` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **27**

### Outgoing calls
- `0x0056ADAB` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)
- `0x0056ADE3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056AE04` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056AE09` → [HalpTimerSaveProcessorCounter](../4D/HalpTimerSaveProcessorCounter_function_004DCF88.md) (function, `0x004DCF88`)
- `0x0056AE52` → [HalpAcpiPreSleep](../../pagelk/B7/HalpAcpiPreSleep_function_00B7BFD4.md) (function, `0x00B7BFD4`)
- `0x0056AE74` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056AE96` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056AEB5` → [HalpSetupRealModeResume](../6A/HalpSetupRealModeResume_function_006ACC60.md) (function, `0x006ACC60`)
- `0x0056AEEF` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056AF0D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056AF49` → [HalpReenableAcpi](../../pagelk/B7/HalpReenableAcpi_function_00B7AE78.md) (function, `0x00B7AE78`)
- `0x0056AF7F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056AF9A` → [HalpCheckWakeupTimeAndAdjust](../55/HalpCheckWakeupTimeAndAdjust_function_0055BB14.md) (function, `0x0055BB14`)
- `0x0056AFA1` → [HalpCheckLowMemoryPreSleep](../../pagelk/B5/HalpCheckLowMemoryPreSleep_function_00B5EB88.md) (function, `0x00B5EB88`)
- `0x0056AFCD` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056AFEC` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056B01B` → [HalSetEnvironmentVariableEx](../44/HalSetEnvironmentVariableEx_function_00448EB0.md) (function, `0x00448EB0`)
- `0x0056B035` → [KeWriteProtectPAT](../../pagelk/B6/KeWriteProtectPAT_function_00B6ABD0.md) (function, `0x00B6ABD0`)
- `0x0056B061` → [HalpHvEnterSleepState](../54/HalpHvEnterSleepState_function_0054CDEC.md) (function, `0x0054CDEC`)
- `0x0056B07E` → [HalReturnToFirmware](../54/HalReturnToFirmware_function_00546550.md) (function, `0x00546550`)
- `0x0056B0A0` → [VslTerminateSecureServices](../58/VslTerminateSecureServices_function_0058F83C.md) (function, `0x0058F83C`)
- `0x0056B0C5` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056B0F9` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056B118` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056B14E` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056B184` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056B1A7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056B1C3` → [HalpAcpiPmRegisterRead](../41/HalpAcpiPmRegisterRead_function_0041DB30.md) (function, `0x0041DB30`)
- `0x0056B1F0` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056B212` → [HalpAcpiPmRegisterWrite](../41/HalpAcpiPmRegisterWrite_function_0041C760.md) (function, `0x0041C760`)
- `0x0056B241` → [HalSetEnvironmentVariableEx](../44/HalSetEnvironmentVariableEx_function_00448EB0.md) (function, `0x00448EB0`)
- `0x0056B256` → [HalpAcpiPostSleep](../../pagelk/B7/HalpAcpiPostSleep_function_00B79990.md) (function, `0x00B79990`)
- `0x0056B28F` → [HaliSaveProcessorContextAndSleep](../6A/HaliSaveProcessorContextAndSleep_function_006ACE10.md) (function, `0x006ACE10`)
- `0x0056B2BA` → [KeWriteProtectPAT](../../pagelk/B6/KeWriteProtectPAT_function_00B6ABD0.md) (function, `0x00B6ABD0`)
- `0x0056B2C4` → [HalpPostSleepMP](../../pagelk/B5/HalpPostSleepMP_function_00B5ECC4.md) (function, `0x00B5ECC4`)
- `0x0056B2DC` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0056ADCD` → RVA `0x00FC1C7C` (`.data`; reference)
- `0x0056ADD5` → RVA `0x00FC1C80` (`.data`; read)
- `0x0056ADF4` → RVA `0x00E03B20` (`.data`; read)
- `0x0056AE10` → RVA `0x00FC3F98` (`.data`; write)
- `0x0056AE23` → RVA `0x00FC4040` (`.data`; read)
- `0x0056AE2D` → RVA `0x00FC4048` (`.data`; write)
- `0x0056AE43` → RVA `0x00FC1AB2` (`.data`; write)
- `0x0056AE4C` → RVA `0x00F8F9A8` (`.data`; write)
- `0x0056AE57` → RVA `0x00F8FE90` (`.data`; read)
- `0x0056AE79` → RVA `0x00F8FF20` (`.data`; read)
- `0x0056AEA8` → RVA `0x00FC1AA8` (`.data`; read)
- `0x0056AEAF` → RVA `0x00FC1AA0` (`.data`; read)
- `0x0056AEC2` → RVA `0x00FC3E19` (`.data`; write)
- `0x0056AEC9` → RVA `0x00F8F9AC` (`.data`; read/write)
- `0x0056AEF8` → RVA `0x00F8F9AC` (`.data`; read)
- `0x0056AF12` → RVA `0x00E0A808` (`.data`; read)
- `0x0056AF5B` → RVA `0x00F8F9B0` (`.data`; read/write)
- `0x0056AF88` → RVA `0x00F8F9B0` (`.data`; read)
- `0x0056AFA6` → RVA `0x00F8FE60` (`.data`; read)
- `0x0056AFD2` → RVA `0x00F8FEF0` (`.data`; read)
- `0x0056B00D` → RVA `0x000260A8` (`.rdata`; read)
- `0x0056B014` → RVA `0x00026078` (`.rdata`; read)
- `0x0056B03C` → RVA `0x00FC1C42` (`.data`; read)
- `0x0056B246` → RVA `0x00F8F9AC` (`.data`; write)
- `0x0056B24F` → RVA `0x00F8F9B0` (`.data`; write)
- `0x0056B272` → RVA `0x00FC1A90` (`.data`; read)
- `0x0056B2C9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0056AE52` → [HalpAcpiPreSleep](../../pagelk/B7/HalpAcpiPreSleep_function_00B7BFD4.md) (`.text` → `PAGELK`)
  - `0x0056AF49` → [HalpReenableAcpi](../../pagelk/B7/HalpReenableAcpi_function_00B7AE78.md) (`.text` → `PAGELK`)
  - `0x0056AFA1` → [HalpCheckLowMemoryPreSleep](../../pagelk/B5/HalpCheckLowMemoryPreSleep_function_00B5EB88.md) (`.text` → `PAGELK`)
  - `0x0056B035` → [KeWriteProtectPAT](../../pagelk/B6/KeWriteProtectPAT_function_00B6ABD0.md) (`.text` → `PAGELK`)
  - `0x0056B256` → [HalpAcpiPostSleep](../../pagelk/B7/HalpAcpiPostSleep_function_00B79990.md) (`.text` → `PAGELK`)
  - `0x0056B2BA` → [KeWriteProtectPAT](../../pagelk/B6/KeWriteProtectPAT_function_00B6ABD0.md) (`.text` → `PAGELK`)
  - `0x0056B2C4` → [HalpPostSleepMP](../../pagelk/B5/HalpPostSleepMP_function_00B5ECC4.md) (`.text` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056AD60  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0056AD65  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0056AD6A  55                              push rbp
0056AD6B  56                              push rsi
0056AD6C  57                              push rdi
0056AD6D  41 54                           push r12
0056AD6F  41 55                           push r13
0056AD71  41 56                           push r14
0056AD73  41 57                           push r15
0056AD75  48 8B EC                        mov rbp, rsp
0056AD78  48 83 EC 60                     sub rsp, 0x60
0056AD7C  4C 8B F2                        mov r14, rdx
0056AD7F  45 8B E1                        mov r12d, r9d
0056AD82  33 D2                           xor edx, edx
0056AD84  4D 8B E8                        mov r13, r8
0056AD87  88 55 40                        mov byte ptr [rbp + 0x40], dl
0056AD8A  48 8B F9                        mov rdi, rcx
0056AD8D  66 89 55 D4                     mov word ptr [rbp - 0x2c], dx
0056AD91  66 89 55 DC                     mov word ptr [rbp - 0x24], dx
0056AD95  66 89 55 D0                     mov word ptr [rbp - 0x30], dx
0056AD99  88 55 D9                        mov byte ptr [rbp - 0x27], dl
0056AD9C  66 89 55 E0                     mov word ptr [rbp - 0x20], dx
0056ADA0  44 0F 20 C0                     mov rax, cr8
0056ADA4  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0056ADA8  44 8B FA                        mov r15d, edx
0056ADAB  E8 F0 73 CE FF                  call 0x1402521a0
0056ADB0  48 8B 75 60                     mov rsi, qword ptr [rbp + 0x60]
0056ADB4  8B DA                           mov ebx, edx
0056ADB6  88 45 DA                        mov byte ptr [rbp - 0x26], al
0056ADB9  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0056ADC2  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0056ADC6  F0 FF 0E                        lock dec dword ptr [rsi]
0056ADC9  EB 23                           jmp 0x14056adee
0056ADCB  FF C3                           inc ebx
0056ADCD  85 1D A9 6E A5 00               test dword ptr [rip + 0xa56ea9], ebx
0056ADD3  75 17                           jne 0x14056adec
0056ADD5  48 8B 05 A4 6E A5 00            mov rax, qword ptr [rip + 0xa56ea4]
0056ADDC  48 85 C0                        test rax, rax
0056ADDF  74 0B                           je 0x14056adec
0056ADE1  8B CB                           mov ecx, ebx
0056ADE3  E8 E8 FC 14 00                  call 0x1406baad0
0056ADE8  33 D2                           xor edx, edx
0056ADEA  EB 02                           jmp 0x14056adee
0056ADEC  F3 90                           pause
0056ADEE  8B 06                           mov eax, dword ptr [rsi]
0056ADF0  85 C0                           test eax, eax
0056ADF2  75 D7                           jne 0x14056adcb
0056ADF4  48 8B 05 25 8D 89 00            mov rax, qword ptr [rip + 0x898d25]
0056ADFB  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
0056ADFF  48 85 C0                        test rax, rax
0056AE02  74 05                           je 0x14056ae09
0056AE04  E8 C7 FC 14 00                  call 0x1406baad0
0056AE09  E8 7A 21 F7 FF                  call 0x1404dcf88
0056AE0E  33 F6                           xor esi, esi
0056AE10  48 89 35 81 91 A5 00            mov qword ptr [rip + 0xa59181], rsi
0056AE17  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0056AE1F  85 C0                           test eax, eax
0056AE21  75 11                           jne 0x14056ae34
0056AE23  48 8B 05 16 92 A5 00            mov rax, qword ptr [rip + 0xa59216]
0056AE2A  48 8B 08                        mov rcx, qword ptr [rax]
0056AE2D  48 89 0D 14 92 A5 00            mov qword ptr [rip + 0xa59214], rcx
0056AE34  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
0056AE38  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0056AE3B  85 C0                           test eax, eax
0056AE3D  0F 85 22 04 00 00               jne 0x14056b265
0056AE43  40 88 35 68 6C A5 00            mov byte ptr [rip + 0xa56c68], sil
0056AE4A  8B CF                           mov ecx, edi
0056AE4C  89 35 56 4B A2 00               mov dword ptr [rip + 0xa24b56], esi
0056AE52  E8 7D 11 61 00                  call 0x140b7bfd4
0056AE57  40 38 35 32 50 A2 00            cmp byte ptr [rip + 0xa25032], sil
0056AE5E  74 19                           je 0x14056ae79
0056AE60  33 D2                           xor edx, edx
0056AE62  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0056AE67  41 B9 02 00 00 00               mov r9d, 2
0056AE6D  4C 8D 45 DC                     lea r8, [rbp - 0x24]
0056AE71  8D 4A 01                        lea ecx, [rdx + 1]
0056AE74  E8 B7 2C EB FF                  call 0x14041db30
0056AE79  40 38 35 A0 50 A2 00            cmp byte ptr [rip + 0xa250a0], sil
0056AE80  74 19                           je 0x14056ae9b
0056AE82  33 D2                           xor edx, edx
0056AE84  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0056AE89  41 B9 02 00 00 00               mov r9d, 2
0056AE8F  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0056AE93  8D 4A 04                        lea ecx, [rdx + 4]
0056AE96  E8 95 2C EB FF                  call 0x14041db30
0056AE9B  44 8B E7                        mov r12d, edi
0056AE9E  41 C1 EC 0C                     shr r12d, 0xc
0056AEA2  41 F6 C4 02                     test r12b, 2
0056AEA6  74 1A                           je 0x14056aec2
0056AEA8  48 8B 0D F9 6B A5 00            mov rcx, qword ptr [rip + 0xa56bf9]
0056AEAF  8B 15 EB 6B A5 00               mov edx, dword ptr [rip + 0xa56beb]
0056AEB5  E8 A6 1D 14 00                  call 0x1406acc60
0056AEBA  84 C0                           test al, al
0056AEBC  0F 85 0E 03 00 00               jne 0x14056b1d0
0056AEC2  C6 05 50 8F A5 00 01            mov byte ptr [rip + 0xa58f50], 1
0056AEC9  F0 FF 05 DC 4A A2 00            lock inc dword ptr [rip + 0xa24adc]
0056AED0  8B DE                           mov ebx, esi
0056AED2  8B 75 58                        mov esi, dword ptr [rbp + 0x58]
0056AED5  EB 21                           jmp 0x14056aef8
0056AED7  FF C3                           inc ebx
0056AED9  85 1D 9D 6D A5 00               test dword ptr [rip + 0xa56d9d], ebx
0056AEDF  75 15                           jne 0x14056aef6
0056AEE1  48 8B 05 98 6D A5 00            mov rax, qword ptr [rip + 0xa56d98]
0056AEE8  48 85 C0                        test rax, rax
0056AEEB  74 09                           je 0x14056aef6
0056AEED  8B CB                           mov ecx, ebx
0056AEEF  E8 DC FB 14 00                  call 0x1406baad0
0056AEF4  EB 02                           jmp 0x14056aef8
0056AEF6  F3 90                           pause
0056AEF8  8B 05 AE 4A A2 00               mov eax, dword ptr [rip + 0xa24aae]
0056AEFE  3B C6                           cmp eax, esi
0056AF00  75 D5                           jne 0x14056aed7
0056AF02  4D 85 F6                        test r14, r14
0056AF05  74 4C                           je 0x14056af53
0056AF07  49 8B CD                        mov rcx, r13
0056AF0A  49 8B C6                        mov rax, r14
0056AF0D  E8 BE FB 14 00                  call 0x1406baad0
0056AF12  8B 0D F0 F8 89 00               mov ecx, dword ptr [rip + 0x89f8f0]
0056AF18  44 8B F8                        mov r15d, eax
0056AF1B  F6 C1 01                        test cl, 1
0056AF1E  75 0F                           jne 0x14056af2f
0056AF20  3D C0 00 00 C0                  cmp eax, 0xc00000c0
0056AF25  75 08                           jne 0x14056af2f
0056AF27  41 B6 01                        mov r14b, 1
0056AF2A  45 33 ED                        xor r13d, r13d
0056AF2D  EB 2C                           jmp 0x14056af5b
0056AF2F  45 33 ED                        xor r13d, r13d
0056AF32  85 C0                           test eax, eax
0056AF34  74 22                           je 0x14056af58
0056AF36  3D 94 02 00 40                  cmp eax, 0x40000294
0056AF3B  75 0C                           jne 0x14056af49
0056AF3D  C6 05 6E 6B A5 00 01            mov byte ptr [rip + 0xa56b6e], 1
0056AF44  E9 8A 02 00 00                  jmp 0x14056b1d3
0056AF49  E8 2A FF 60 00                  call 0x140b7ae78
0056AF4E  E9 80 02 00 00                  jmp 0x14056b1d3
0056AF53  45 8A F7                        mov r14b, r15b
0056AF56  EB D2                           jmp 0x14056af2a
0056AF58  45 8A F5                        mov r14b, r13b
0056AF5B  F0 FF 05 4E 4A A2 00            lock inc dword ptr [rip + 0xa24a4e]
0056AF62  41 8B DD                        mov ebx, r13d
0056AF65  EB 21                           jmp 0x14056af88
0056AF67  FF C3                           inc ebx
0056AF69  85 1D 0D 6D A5 00               test dword ptr [rip + 0xa56d0d], ebx
0056AF6F  75 15                           jne 0x14056af86
0056AF71  48 8B 05 08 6D A5 00            mov rax, qword ptr [rip + 0xa56d08]
0056AF78  48 85 C0                        test rax, rax
0056AF7B  74 09                           je 0x14056af86
0056AF7D  8B CB                           mov ecx, ebx
0056AF7F  E8 4C FB 14 00                  call 0x1406baad0
0056AF84  EB 02                           jmp 0x14056af88
0056AF86  F3 90                           pause
0056AF88  8B 05 22 4A A2 00               mov eax, dword ptr [rip + 0xa24a22]
0056AF8E  3B C6                           cmp eax, esi
0056AF90  75 D5                           jne 0x14056af67
0056AF92  F0 44 09 2D 16 4A A2 00         lock or dword ptr [rip + 0xa24a16], r13d
0056AF9A  E8 75 0B FF FF                  call 0x14055bb14
0056AF9F  8B CF                           mov ecx, edi
0056AFA1  E8 E2 3B 5F 00                  call 0x140b5eb88
0056AFA6  44 38 2D B3 4E A2 00            cmp byte ptr [rip + 0xa24eb3], r13b
0056AFAD  BE 00 80 00 00                  mov esi, 0x8000
0056AFB2  66 89 75 D0                     mov word ptr [rbp - 0x30], si
0056AFB6  BB 02 00 00 00                  mov ebx, 2
0056AFBB  74 15                           je 0x14056afd2
0056AFBD  44 8B CB                        mov r9d, ebx
0056AFC0  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056AFC5  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0056AFC9  33 D2                           xor edx, edx
0056AFCB  33 C9                           xor ecx, ecx
0056AFCD  E8 8E 17 EB FF                  call 0x14041c760
0056AFD2  44 38 2D 17 4F A2 00            cmp byte ptr [rip + 0xa24f17], r13b
0056AFD9  74 16                           je 0x14056aff1
0056AFDB  33 D2                           xor edx, edx
0056AFDD  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056AFE2  44 8B CB                        mov r9d, ebx
0056AFE5  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0056AFE9  8D 4A 03                        lea ecx, [rdx + 3]
0056AFEC  E8 6F 17 EB FF                  call 0x14041c760
0056AFF1  C6 45 40 90                     mov byte ptr [rbp + 0x40], 0x90
0056AFF5  41 F6 C4 40                     test r12b, 0x40
0056AFF9  74 25                           je 0x14056b020
0056AFFB  41 B9 01 00 00 00               mov r9d, 1
0056B001  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0056B009  4C 8D 45 40                     lea r8, [rbp + 0x40]
0056B00D  48 8D 15 94 B0 AB FF            lea rdx, [rip - 0x544f6c]
0056B014  48 8D 0D 5D B0 AB FF            lea rcx, [rip - 0x544fa3]
0056B01B  E8 90 DE ED FF                  call 0x140448eb0
0056B020  41 F6 C4 01                     test r12b, 1
0056B024  74 16                           je 0x14056b03c
0056B026  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0056B02A  80 B8 8D 00 00 00 01            cmp byte ptr [rax + 0x8d], 1
0056B031  75 07                           jne 0x14056b03a
0056B033  B1 01                           mov cl, 1
0056B035  E8 96 FB 5F 00                  call 0x140b6abd0
0056B03A  0F 09                           wbinvd
0056B03C  44 38 2D FF 6B A5 00            cmp byte ptr [rip + 0xa56bff], r13b
0056B043  74 29                           je 0x14056b06e
0056B045  8B CF                           mov ecx, edi
0056B047  C1 E9 08                        shr ecx, 8
0056B04A  83 E1 0F                        and ecx, 0xf
0056B04D  83 F9 01                        cmp ecx, 1
0056B050  74 0F                           je 0x14056b061
0056B052  8D 41 FE                        lea eax, [rcx - 2]
0056B055  A9 FC FF FF FF                  test eax, 0xfffffffc
0056B05A  75 12                           jne 0x14056b06e
0056B05C  83 F9 04                        cmp ecx, 4
0056B05F  74 0D                           je 0x14056b06e
0056B061  E8 86 1D FE FF                  call 0x14054cdec
0056B066  44 8B F8                        mov r15d, eax
0056B069  E9 A9 01 00 00                  jmp 0x14056b217
0056B06E  8B 05 94 F7 89 00               mov eax, dword ptr [rip + 0x89f794]
0056B074  A8 01                           test al, 1
0056B076  75 0D                           jne 0x14056b085
0056B078  41 0F B6 CE                     movzx ecx, r14b
0056B07C  FF C1                           inc ecx
0056B07E  E8 CD B4 FD FF                  call 0x140546550
0056B083  EB 20                           jmp 0x14056b0a5
0056B085  8B C7                           mov eax, edi
0056B087  B9 00 0F 00 00                  mov ecx, 0xf00
0056B08C  23 C1                           and eax, ecx
0056B08E  3D 00 04 00 00                  cmp eax, 0x400
0056B093  74 0B                           je 0x14056b0a0
0056B095  8B C7                           mov eax, edi
0056B097  23 C1                           and eax, ecx
0056B099  3D 00 05 00 00                  cmp eax, 0x500
0056B09E  75 05                           jne 0x14056b0a5
0056B0A0  E8 97 47 02 00                  call 0x14058f83c
0056B0A5  44 38 2D E4 4D A2 00            cmp byte ptr [rip + 0xa24de4], r13b
0056B0AC  41 BE 03 02 00 00               mov r14d, 0x203
0056B0B2  74 4A                           je 0x14056b0fe
0056B0B4  33 D2                           xor edx, edx
0056B0B6  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B0BB  44 8B CB                        mov r9d, ebx
0056B0BE  4C 8D 45 D4                     lea r8, [rbp - 0x2c]
0056B0C2  8D 4A 01                        lea ecx, [rdx + 1]
0056B0C5  E8 66 2A EB FF                  call 0x14041db30
0056B0CA  0F B7 45 D4                     movzx eax, word ptr [rbp - 0x2c]
0056B0CE  4C 8D 45 D4                     lea r8, [rbp - 0x2c]
0056B0D2  0F B7 CF                        movzx ecx, di
0056B0D5  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B0DA  66 83 E1 07                     and cx, 7
0056B0DE  66 41 23 C6                     and ax, r14w
0056B0E2  66 83 C9 08                     or cx, 8
0056B0E6  33 D2                           xor edx, edx
0056B0E8  66 C1 E1 0A                     shl cx, 0xa
0056B0EC  44 8B CB                        mov r9d, ebx
0056B0EF  66 0B C8                        or cx, ax
0056B0F2  66 89 4D D4                     mov word ptr [rbp - 0x2c], cx
0056B0F6  8D 4A 01                        lea ecx, [rdx + 1]
0056B0F9  E8 62 16 EB FF                  call 0x14041c760
0056B0FE  44 38 2D 1B 4E A2 00            cmp byte ptr [rip + 0xa24e1b], r13b
0056B105  74 4C                           je 0x14056b153
0056B107  33 D2                           xor edx, edx
0056B109  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B10E  44 8B CB                        mov r9d, ebx
0056B111  4C 8D 45 D4                     lea r8, [rbp - 0x2c]
0056B115  8D 4A 04                        lea ecx, [rdx + 4]
0056B118  E8 13 2A EB FF                  call 0x14041db30
0056B11D  0F B7 45 D4                     movzx eax, word ptr [rbp - 0x2c]
0056B121  4C 8D 45 D4                     lea r8, [rbp - 0x2c]
0056B125  8B CF                           mov ecx, edi
0056B127  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B12C  C1 E9 04                        shr ecx, 4
0056B12F  66 41 23 C6                     and ax, r14w
0056B133  66 83 E1 07                     and cx, 7
0056B137  33 D2                           xor edx, edx
0056B139  66 83 C9 08                     or cx, 8
0056B13D  44 8B CB                        mov r9d, ebx
0056B140  66 C1 E1 0A                     shl cx, 0xa
0056B144  66 0B C8                        or cx, ax
0056B147  66 89 4D D4                     mov word ptr [rbp - 0x2c], cx
0056B14B  8D 4A 04                        lea ecx, [rdx + 4]
0056B14E  E8 0D 16 EB FF                  call 0x14041c760
0056B153  44 38 2D 06 4D A2 00            cmp byte ptr [rip + 0xa24d06], r13b
0056B15A  41 8B DD                        mov ebx, r13d
0056B15D  74 74                           je 0x14056b1d3
0056B15F  8A 05 8B 4D A2 00               mov al, byte ptr [rip + 0xa24d8b]
0056B165  F6 D8                           neg al
0056B167  45 1B F6                        sbb r14d, r14d
0056B16A  41 83 E6 03                     and r14d, 3
0056B16E  EB 40                           jmp 0x14056b1b0
0056B170  41 B9 02 00 00 00               mov r9d, 2
0056B176  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B17B  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0056B17F  33 D2                           xor edx, edx
0056B181  41 8B CE                        mov ecx, r14d
0056B184  E8 A7 29 EB FF                  call 0x14041db30
0056B189  66 85 75 D0                     test word ptr [rbp - 0x30], si
0056B18D  75 44                           jne 0x14056b1d3
0056B18F  FF C3                           inc ebx
0056B191  85 1D E5 6A A5 00               test dword ptr [rip + 0xa56ae5], ebx
0056B197  75 15                           jne 0x14056b1ae
0056B199  48 8B 05 E0 6A A5 00            mov rax, qword ptr [rip + 0xa56ae0]
0056B1A0  48 85 C0                        test rax, rax
0056B1A3  74 09                           je 0x14056b1ae
0056B1A5  8B CB                           mov ecx, ebx
0056B1A7  E8 24 F9 14 00                  call 0x1406baad0
0056B1AC  EB 02                           jmp 0x14056b1b0
0056B1AE  F3 90                           pause
0056B1B0  41 B9 02 00 00 00               mov r9d, 2
0056B1B6  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B1BB  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0056B1BF  33 D2                           xor edx, edx
0056B1C1  33 C9                           xor ecx, ecx
0056B1C3  E8 68 29 EB FF                  call 0x14041db30
0056B1C8  66 85 75 D0                     test word ptr [rbp - 0x30], si
0056B1CC  74 A2                           je 0x14056b170
0056B1CE  EB 03                           jmp 0x14056b1d3
0056B1D0  45 33 ED                        xor r13d, r13d
0056B1D3  44 38 2D B6 4C A2 00            cmp byte ptr [rip + 0xa24cb6], r13b
0056B1DA  74 19                           je 0x14056b1f5
0056B1DC  33 D2                           xor edx, edx
0056B1DE  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B1E3  41 B9 02 00 00 00               mov r9d, 2
0056B1E9  4C 8D 45 DC                     lea r8, [rbp - 0x24]
0056B1ED  8D 4A 01                        lea ecx, [rdx + 1]
0056B1F0  E8 6B 15 EB FF                  call 0x14041c760
0056B1F5  44 38 2D 24 4D A2 00            cmp byte ptr [rip + 0xa24d24], r13b
0056B1FC  74 19                           je 0x14056b217
0056B1FE  33 D2                           xor edx, edx
0056B200  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0056B205  41 B9 02 00 00 00               mov r9d, 2
0056B20B  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0056B20F  8D 4A 04                        lea ecx, [rdx + 4]
0056B212  E8 49 15 EB FF                  call 0x14041c760
0056B217  C6 45 40 9F                     mov byte ptr [rbp + 0x40], 0x9f
0056B21B  41 F6 C4 40                     test r12b, 0x40
0056B21F  74 25                           je 0x14056b246
0056B221  41 B9 01 00 00 00               mov r9d, 1
0056B227  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0056B22F  4C 8D 45 40                     lea r8, [rbp + 0x40]
0056B233  48 8D 15 6E AE AB FF            lea rdx, [rip - 0x545192]
0056B23A  48 8D 0D 37 AE AB FF            lea rcx, [rip - 0x5451c9]
0056B241  E8 6A DC ED FF                  call 0x140448eb0
0056B246  44 89 2D 5F 47 A2 00            mov dword ptr [rip + 0xa2475f], r13d
0056B24D  8B CF                           mov ecx, edi
0056B24F  44 89 2D 5A 47 A2 00            mov dword ptr [rip + 0xa2475a], r13d
0056B256  E8 35 E7 60 00                  call 0x140b79990
0056B25B  44 8B 65 58                     mov r12d, dword ptr [rbp + 0x58]
0056B25F  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
0056B263  EB 35                           jmp 0x14056b29a
0056B265  0F BA E7 0F                     bt edi, 0xf
0056B269  72 10                           jb 0x14056b27b
0056B26B  48 69 C8 C0 05 00 00            imul rcx, rax, 0x5c0
0056B272  48 03 0D 17 68 A5 00            add rcx, qword ptr [rip + 0xa56817]
0056B279  EB 02                           jmp 0x14056b27d
0056B27B  33 C9                           xor ecx, ecx
0056B27D  48 8D 45 D9                     lea rax, [rbp - 0x27]
0056B281  45 8B CC                        mov r9d, r12d
0056B284  4D 8B C5                        mov r8, r13
0056B287  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0056B28C  49 8B D6                        mov rdx, r14
0056B28F  E8 7C 1B 14 00                  call 0x1406ace10
0056B294  44 8B F8                        mov r15d, eax
0056B297  45 33 ED                        xor r13d, r13d
0056B29A  8B C7                           mov eax, edi
0056B29C  C1 E8 0C                        shr eax, 0xc
0056B29F  A8 10                           test al, 0x10
0056B2A1  0F 94 C1                        sete cl
0056B2A4  0F BA E7 0C                     bt edi, 0xc
0056B2A8  0F 92 C0                        setb al
0056B2AB  84 C8                           test al, cl
0056B2AD  74 12                           je 0x14056b2c1
0056B2AF  80 BB 8D 00 00 00 01            cmp byte ptr [rbx + 0x8d], 1
0056B2B6  75 09                           jne 0x14056b2c1
0056B2B8  33 C9                           xor ecx, ecx
0056B2BA  E8 11 F9 5F 00                  call 0x140b6abd0
0056B2BF  0F 09                           wbinvd
0056B2C1  41 8B CC                        mov ecx, r12d
0056B2C4  E8 FB 39 5F 00                  call 0x140b5ecc4
0056B2C9  44 39 2D 50 BA A5 00            cmp dword ptr [rip + 0xa5ba50], r13d
0056B2D0  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
0056B2D4  74 0B                           je 0x14056b2e1
0056B2D6  44 0F 20 C1                     mov rcx, cr8
0056B2DA  8A D3                           mov dl, bl
0056B2DC  E8 B7 A3 F8 FF                  call 0x1404f5698
0056B2E1  0F B6 C3                        movzx eax, bl
0056B2E4  44 0F 22 C0                     mov cr8, rax
0056B2E8  44 38 6D DA                     cmp byte ptr [rbp - 0x26], r13b
0056B2EC  74 01                           je 0x14056b2ef
0056B2EE  FB                              sti
0056B2EF  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0056B2F7  41 8B C7                        mov eax, r15d
0056B2FA  48 83 C4 60                     add rsp, 0x60
0056B2FE  41 5F                           pop r15
0056B300  41 5E                           pop r14
0056B302  41 5D                           pop r13
0056B304  41 5C                           pop r12
0056B306  5F                              pop rdi
0056B307  5E                              pop rsi
0056B308  5D                              pop rbp
0056B309  C3                              ret
0056B30A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HaliAcpiSleep(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int16 v_stack_m58;
    unsigned __int16 v_stack_m5C;
    unsigned __int8 v_stack_m5E;
    unsigned __int8 v_stack_m5F;
    unsigned __int16 v_stack_m64;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (96);
    a2 = 0;
    v_stack_p8 = 0;
    v_stack_m64 = 0;
    v_stack_m5C = 0;
    v_stack_m68 = 0;
    v_stack_m5F = 0;
    v_stack_m58 = 0;
    v_stack_m48 = v_cr8;
    result = HalpDisableInterrupts(a1, a2, a3, a4);
    v_stack_m5E = (unsigned __int8)(result);
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 32));
    goto loc_0056ADEE;
loc_0056ADCB:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 10841769)) & ((unsigned int)(v_rbx))) != 0) goto loc_0056ADEC;
    if (*(unsigned __int64 *)(v_rip + 10841764) == 0) goto loc_0056ADEC;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    a2 = 0;
    goto loc_0056ADEE;
loc_0056ADEC:
loc_0056ADEE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5))) != 0) goto loc_0056ADCB;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9014565) + 48);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9014565) + 48) != 0) {
        result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    }
    result = HalpTimerSaveProcessorCounter((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rip + 10850689) = 0;
    result = (unsigned int)(*(unsigned int *)(gs_base + (0 + 420)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) == 0) {
        result = *(unsigned __int64 *)(v_rip + 10850838);
        a1 = *(unsigned __int64 *)(result);
        *(unsigned __int64 *)(v_rip + 10850836) = a1;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 36))) != 0) goto loc_0056B265;
    *(unsigned __int8 *)(v_rip + 10841192) = 0;
    *(unsigned int *)(v_rip + 10636118) = 0;
    result = HalpAcpiPreSleep((unsigned int)((unsigned int)(a1)), a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 10637362)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m5C;
        a1 = a2 + 1;
        result = HalpAcpiPmRegisterRead(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10637472)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m58;
        a1 = a2 + 4;
        result = HalpAcpiPmRegisterRead(a1, a2, a3, a4);
    }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(a1))) >> (12));
    if ((((unsigned __int8)(v_r12)) & (2)) == 0) goto loc_0056AEC2;
    result = HalpSetupRealModeResume(*(unsigned __int64 *)(v_rip + 10841081), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0056B1D0;
loc_0056AEC2:
    *(unsigned __int8 *)(v_rip + 10850128) = 1;
    goto loc_0056AEF8;
loc_0056AED7:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 10841501)) & ((unsigned int)(v_rbx))) != 0) goto loc_0056AEF6;
    if (*(unsigned __int64 *)(v_rip + 10841496) == 0) goto loc_0056AEF6;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    goto loc_0056AEF8;
loc_0056AEF6:
loc_0056AEF8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10635950)))) != ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_0056AED7;
    if (0 == 0) goto loc_0056AF53;
    result = guard_dispatch_icall(a3, (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9042160)))) & (1)) != 0) goto loc_0056AF2F;
    if (((unsigned int)(result)) != 0xC00000C0ULL) goto loc_0056AF2F;
loc_0056AF2A:
    v_r13 = 0;
    goto loc_0056AF5B;
loc_0056AF2F:
    v_r13 = 0;
    if ((unsigned int)(result) == 0) goto loc_0056AF58;
    if (((unsigned int)(result)) != 0x40000294ULL) goto loc_0056AF49;
    *(unsigned __int8 *)(v_rip + 10840942) = 1;
    goto loc_0056B1D3;
loc_0056AF49:
    result = HalpReenableAcpi((unsigned int)(*(unsigned int *)(v_rip + 9042160)), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    goto loc_0056B1D3;
loc_0056AF53:
    goto loc_0056AF2A;
loc_0056AF58:
loc_0056AF5B:
    goto loc_0056AF88;
loc_0056AF67:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 10841357)) & ((unsigned int)(v_rbx))) != 0) goto loc_0056AF86;
    if (*(unsigned __int64 *)(v_rip + 10841352) == 0) goto loc_0056AF86;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    goto loc_0056AF88;
loc_0056AF86:
loc_0056AF88:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10635810)))) != ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_0056AF67;
    result = HalpCheckWakeupTimeAndAdjust((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    result = HalpCheckLowMemoryPreSleep((unsigned int)((unsigned int)(a1)), (unsigned int)(*(unsigned int *)(v_rip + 10841067)), a3, a4);
    v_stack_m68 = (unsigned __int16)((unsigned int)(0x8000ULL));
    if ((*(unsigned __int8 *)(v_rip + 10636979)) != 0) {
        a4 = 2;
        v_stack_m78 = 0;
        a3 = v_stack_m68;
        a2 = 0;
        a1 = 0;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10637079)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m68;
        a1 = a2 + 3;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    v_stack_p8 = 144;
    if ((((unsigned __int8)(v_r12)) & (64)) != 0) {
        a4 = 1;
        v_stack_m78 = 1;
        a3 = v_stack_p8;
        a2 = v_rip - 5525356;
        a1 = v_rip - 5525411;
        result = HalSetEnvironmentVariableEx(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_r12)) & (1)) == 0) goto loc_0056B03C;
    result = v_stack_m50;
    if ((*(unsigned __int8 *)(v_stack_m50 + 141)) == 1) {
        a1 = 1;
        result = KeWriteProtectPAT(a1, a2, a3, a4);
    }
loc_0056B03C:
    if ((*(unsigned __int8 *)(v_rip + 10841087)) == 0) goto loc_0056B06E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a1))) >> (8));
    a1 = (unsigned int)((a1) & (15));
    if (((unsigned int)(a1)) == 1) goto loc_0056B061;
    if ((((unsigned int)(a1 - 2)) & (0xFFFFFFFCULL)) != 0) goto loc_0056B06E;
    if (((unsigned int)(a1)) == 4) goto loc_0056B06E;
loc_0056B061:
    result = HalpHvEnterSleepState(a1, a2, a3, a4);
    goto loc_0056B217;
loc_0056B06E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9041812)))) & (1)) != 0) goto loc_0056B085;
    a1 = (unsigned int)((0) + 1);
    result = HalReturnToFirmware(a1, a2, a3, a4);
    goto loc_0056B0A5;
loc_0056B085:
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & ((unsigned int)((unsigned int)(0xF00ULL))));
    if (((unsigned int)(result)) == 0x400ULL) goto loc_0056B0A0;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & ((unsigned int)((unsigned int)(0xF00ULL))));
    if (((unsigned int)(result)) == 0x500ULL) {
        result = VslTerminateSecureServices((unsigned int)(0xF00ULL), a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10636772)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m64;
        a1 = a2 + 1;
        result = HalpAcpiPmRegisterRead(a1, a2, a3, a4);
        result = v_stack_m64;
        a3 = v_stack_m64;
        a1 = (unsigned __int16)(a1);
        v_stack_m78 = 0;
        a1 = (unsigned __int16)((a1) & (7));
        result = (unsigned __int16)((result) & (515));
        a1 = (unsigned __int16)((a1) | (8));
        a2 = 0;
        a1 = (unsigned __int16)((a1) << (10));
        a4 = 2;
        a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
        v_stack_m64 = (unsigned __int16)(a1);
        a1 = a2 + 1;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10636827)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m64;
        a1 = a2 + 4;
        result = HalpAcpiPmRegisterRead(a1, a2, a3, a4);
        result = v_stack_m64;
        a3 = v_stack_m64;
        a1 = (unsigned int)(a1);
        v_stack_m78 = 0;
        a1 = (unsigned int)((a1) >> (4));
        result = (unsigned __int16)((result) & (515));
        a1 = (unsigned __int16)((a1) & (7));
        a2 = 0;
        a1 = (unsigned __int16)((a1) | (8));
        a4 = 2;
        a1 = (unsigned __int16)((a1) << (10));
        a1 = (unsigned __int16)((a1) | ((unsigned __int16)(result)));
        v_stack_m64 = (unsigned __int16)(a1);
        a1 = a2 + 4;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10636550)) == 0) goto loc_0056B1D3;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 10636683)));
    v_r14 = (unsigned int)((515) & (3));
    goto loc_0056B1B0;
loc_0056B170:
    v_stack_m78 = 0;
    a2 = 0;
    result = HalpAcpiPmRegisterRead((unsigned int)((unsigned int)(v_r14)), a2, v_stack_m68, 2);
    if (((v_stack_m68) & ((unsigned __int16)((unsigned int)(0x8000ULL)))) != 0) goto loc_0056B1D3;
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 10840805)) & ((unsigned int)(v_rbx))) != 0) goto loc_0056B1AE;
    if (*(unsigned __int64 *)(v_rip + 10840800) == 0) goto loc_0056B1AE;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), a2, v_stack_m68, 2);
    goto loc_0056B1B0;
loc_0056B1AE:
loc_0056B1B0:
    v_stack_m78 = 0;
    a2 = 0;
    a1 = 0;
    result = HalpAcpiPmRegisterRead(a1, a2, v_stack_m68, 2);
    if (((v_stack_m68) & ((unsigned __int16)((unsigned int)(0x8000ULL)))) == 0) goto loc_0056B170;
    goto loc_0056B1D3;
loc_0056B1D0:
    v_r13 = 0;
loc_0056B1D3:
    if ((*(unsigned __int8 *)(v_rip + 10636470)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m5C;
        a1 = a2 + 1;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10636580)) != 0) {
        a2 = 0;
        v_stack_m78 = 0;
        a4 = 2;
        a3 = v_stack_m58;
        a1 = a2 + 4;
        result = HalpAcpiPmRegisterWrite(a1, a2, a3, a4);
    }
    v_stack_p8 = 159;
    if ((((unsigned __int8)(v_r12)) & (64)) != 0) {
        a4 = 1;
        v_stack_m78 = 1;
        a3 = v_stack_p8;
        a2 = v_rip - 5525906;
        a1 = v_rip - 5525961;
        result = HalSetEnvironmentVariableEx(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rip + 10635103) = 0;
    *(unsigned int *)(v_rip + 10635098) = 0;
    result = HalpAcpiPostSleep((unsigned int)((unsigned int)(a1)), a2, a3, a4);
    goto loc_0056B29A;
loc_0056B265:
    if (condition_is_below) goto loc_0056B27B;
    a1 = ((unsigned int)((unsigned int)(a1))) * (result);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10840087));
    goto loc_0056B27D;
loc_0056B27B:
    a1 = 0;
loc_0056B27D:
    v_stack_m78 = v_stack_m5F;
    result = HaliSaveProcessorContextAndSleep(a1, v_r14, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    v_r13 = 0;
loc_0056B29A:
    result = (unsigned int)((0) >> (12));
    a1 = ((((unsigned __int8)(result)) & (16)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0056B2C1;
    if ((*(unsigned __int8 *)(v_stack_m50 + 141)) == 1) {
        a1 = 0;
        result = KeWriteProtectPAT(a1, v_r14, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    }
    result = HalpPostSleepMP((unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_r14, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    if ((*(unsigned int *)(v_rip + 10861136)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_m48);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    }
    if (v_stack_m5E != 0) {
    }
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HaliAcpiSleep(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint16_t v_stack_m58;
    uint16_t v_stack_m5C;
    uint8_t v_stack_m5E;
    uint8_t v_stack_m5F;
    uint16_t v_stack_m64;
    uint16_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (96);
    Arg2 = 0;
    v_stack_p8 = 0;
    v_stack_m64 = 0;
    v_stack_m5C = 0;
    v_stack_m68 = 0;
    v_stack_m5F = 0;
    v_stack_m58 = 0;
    v_stack_m48 = v_cr8;
    result = HalpDisableInterrupts(Arg1, Arg2, Arg3, Arg4);
    v_stack_m5E = (uint8_t)(result);
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x20));
    goto loc_0056ADEE;
loc_0056ADCB:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xA56EA9)) & ((uint32_t)(local_rbx))) != 0) goto loc_0056ADEC;
    if (*(uint64_t *)(v_rip + 0xA56EA4) == 0) goto loc_0056ADEC;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    Arg2 = 0;
    goto loc_0056ADEE;
loc_0056ADEC:
loc_0056ADEE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg5))) != 0) goto loc_0056ADCB;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x898D25) + 0x30);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x898D25) + 0x30) != 0) {
        result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    }
    result = HalpTimerSaveProcessorCounter((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    local_rsi = 0;
    *(uint64_t *)(v_rip + 0xA59181) = 0;
    result = (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) == 0) {
        result = *(uint64_t *)(v_rip + 0xA59216);
        Arg1 = *(uint64_t *)(result);
        *(uint64_t *)(v_rip + 0xA59214) = Arg1;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24))) != 0) goto loc_0056B265;
    *(uint8_t *)(v_rip + 0xA56C68) = 0;
    *(uint32_t *)(v_rip + 0xA24B56) = 0;
    result = HalpAcpiPreSleep((uint32_t)((uint32_t)(Arg1)), Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0xA25032)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m5C;
        Arg1 = Arg2 + 1;
        result = HalpAcpiPmRegisterRead(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA250A0)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m58;
        Arg1 = Arg2 + 4;
        result = HalpAcpiPmRegisterRead(Arg1, Arg2, Arg3, Arg4);
    }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) >> (12));
    if ((((uint8_t)(local_r12)) & (2)) == 0) goto loc_0056AEC2;
    result = HalpSetupRealModeResume(*(uint64_t *)(v_rip + 0xA56BF9), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0056B1D0;
loc_0056AEC2:
    *(uint8_t *)(v_rip + 0xA58F50) = 1;
    goto loc_0056AEF8;
loc_0056AED7:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xA56D9D)) & ((uint32_t)(local_rbx))) != 0) goto loc_0056AEF6;
    if (*(uint64_t *)(v_rip + 0xA56D98) == 0) goto loc_0056AEF6;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    goto loc_0056AEF8;
loc_0056AEF6:
loc_0056AEF8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA24AAE)))) != ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_0056AED7;
    if (0 == 0) goto loc_0056AF53;
    result = guard_dispatch_icall(Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x89F8F0)))) & (1)) != 0) goto loc_0056AF2F;
    if (((uint32_t)(result)) != 0xC00000C0ULL) goto loc_0056AF2F;
loc_0056AF2A:
    local_r13 = 0;
    goto loc_0056AF5B;
loc_0056AF2F:
    local_r13 = 0;
    if ((uint32_t)(result) == 0) goto loc_0056AF58;
    if (((uint32_t)(result)) != 0x40000294ULL) goto loc_0056AF49;
    *(uint8_t *)(v_rip + 0xA56B6E) = 1;
    goto loc_0056B1D3;
loc_0056AF49:
    result = HalpReenableAcpi((uint32_t)(*(uint32_t *)(v_rip + 0x89F8F0)), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    goto loc_0056B1D3;
loc_0056AF53:
    goto loc_0056AF2A;
loc_0056AF58:
loc_0056AF5B:
    goto loc_0056AF88;
loc_0056AF67:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xA56D0D)) & ((uint32_t)(local_rbx))) != 0) goto loc_0056AF86;
    if (*(uint64_t *)(v_rip + 0xA56D08) == 0) goto loc_0056AF86;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    goto loc_0056AF88;
loc_0056AF86:
loc_0056AF88:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA24A22)))) != ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_0056AF67;
    result = HalpCheckWakeupTimeAndAdjust((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    result = HalpCheckLowMemoryPreSleep((uint32_t)((uint32_t)(Arg1)), (uint32_t)(*(uint32_t *)(v_rip + 0xA56BEB)), Arg3, Arg4);
    v_stack_m68 = (uint16_t)((uint32_t)(0x8000ULL));
    if ((*(uint8_t *)(v_rip + 0xA24EB3)) != 0) {
        Arg4 = 2;
        v_stack_m78 = 0;
        Arg3 = v_stack_m68;
        Arg2 = 0;
        Arg1 = 0;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA24F17)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m68;
        Arg1 = Arg2 + 3;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p8 = 144;
    if ((((uint8_t)(local_r12)) & (64)) != 0) {
        Arg4 = 1;
        v_stack_m78 = 1;
        Arg3 = v_stack_p8;
        Arg2 = v_rip - 5525356;
        Arg1 = v_rip - 5525411;
        result = HalSetEnvironmentVariableEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(local_r12)) & (1)) == 0) goto loc_0056B03C;
    result = v_stack_m50;
    if ((*(uint8_t *)(v_stack_m50 + 0x8D)) == 1) {
        Arg1 = 1;
        result = KeWriteProtectPAT(Arg1, Arg2, Arg3, Arg4);
    }
loc_0056B03C:
    if ((*(uint8_t *)(v_rip + 0xA56BFF)) == 0) goto loc_0056B06E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (15));
    if (((uint32_t)(Arg1)) == 1) goto loc_0056B061;
    if ((((uint32_t)(Arg1 - 2)) & (0xFFFFFFFCULL)) != 0) goto loc_0056B06E;
    if (((uint32_t)(Arg1)) == 4) goto loc_0056B06E;
loc_0056B061:
    result = HalpHvEnterSleepState(Arg1, Arg2, Arg3, Arg4);
    goto loc_0056B217;
loc_0056B06E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x89F794)))) & (1)) != 0) goto loc_0056B085;
    Arg1 = (uint32_t)((0) + 1);
    result = HalReturnToFirmware(Arg1, Arg2, Arg3, Arg4);
    goto loc_0056B0A5;
loc_0056B085:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & ((uint32_t)((uint32_t)(0xF00ULL))));
    if (((uint32_t)(result)) == 0x400ULL) goto loc_0056B0A0;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & ((uint32_t)((uint32_t)(0xF00ULL))));
    if (((uint32_t)(result)) == 0x500ULL) {
        result = VslTerminateSecureServices((uint32_t)(0xF00ULL), Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA24DE4)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m64;
        Arg1 = Arg2 + 1;
        result = HalpAcpiPmRegisterRead(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m64;
        Arg3 = v_stack_m64;
        Arg1 = (uint16_t)(Arg1);
        v_stack_m78 = 0;
        Arg1 = (uint16_t)((Arg1) & (7));
        result = (uint16_t)((result) & (515));
        Arg1 = (uint16_t)((Arg1) | (8));
        Arg2 = 0;
        Arg1 = (uint16_t)((Arg1) << (10));
        Arg4 = 2;
        Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
        v_stack_m64 = (uint16_t)(Arg1);
        Arg1 = Arg2 + 1;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA24E1B)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m64;
        Arg1 = Arg2 + 4;
        result = HalpAcpiPmRegisterRead(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m64;
        Arg3 = v_stack_m64;
        Arg1 = (uint32_t)(Arg1);
        v_stack_m78 = 0;
        Arg1 = (uint32_t)((Arg1) >> (4));
        result = (uint16_t)((result) & (515));
        Arg1 = (uint16_t)((Arg1) & (7));
        Arg2 = 0;
        Arg1 = (uint16_t)((Arg1) | (8));
        Arg4 = 2;
        Arg1 = (uint16_t)((Arg1) << (10));
        Arg1 = (uint16_t)((Arg1) | ((uint16_t)(result)));
        v_stack_m64 = (uint16_t)(Arg1);
        Arg1 = Arg2 + 4;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA24D06)) == 0) goto loc_0056B1D3;
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0xA24D8B)));
    local_r14 = (uint32_t)((515) & (3));
    goto loc_0056B1B0;
loc_0056B170:
    v_stack_m78 = 0;
    Arg2 = 0;
    result = HalpAcpiPmRegisterRead((uint32_t)((uint32_t)(local_r14)), Arg2, v_stack_m68, 2);
    if (((v_stack_m68) & ((uint16_t)((uint32_t)(0x8000ULL)))) != 0) goto loc_0056B1D3;
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xA56AE5)) & ((uint32_t)(local_rbx))) != 0) goto loc_0056B1AE;
    if (*(uint64_t *)(v_rip + 0xA56AE0) == 0) goto loc_0056B1AE;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), Arg2, v_stack_m68, 2);
    goto loc_0056B1B0;
loc_0056B1AE:
loc_0056B1B0:
    v_stack_m78 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = HalpAcpiPmRegisterRead(Arg1, Arg2, v_stack_m68, 2);
    if (((v_stack_m68) & ((uint16_t)((uint32_t)(0x8000ULL)))) == 0) goto loc_0056B170;
    goto loc_0056B1D3;
loc_0056B1D0:
    local_r13 = 0;
loc_0056B1D3:
    if ((*(uint8_t *)(v_rip + 0xA24CB6)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m5C;
        Arg1 = Arg2 + 1;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xA24D24)) != 0) {
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg4 = 2;
        Arg3 = v_stack_m58;
        Arg1 = Arg2 + 4;
        result = HalpAcpiPmRegisterWrite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p8 = 159;
    if ((((uint8_t)(local_r12)) & (64)) != 0) {
        Arg4 = 1;
        v_stack_m78 = 1;
        Arg3 = v_stack_p8;
        Arg2 = v_rip - 5525906;
        Arg1 = v_rip - 5525961;
        result = HalSetEnvironmentVariableEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(v_rip + 0xA2475F) = 0;
    *(uint32_t *)(v_rip + 0xA2475A) = 0;
    result = HalpAcpiPostSleep((uint32_t)((uint32_t)(Arg1)), Arg2, Arg3, Arg4);
    goto loc_0056B29A;
loc_0056B265:
    if (condition_is_below) goto loc_0056B27B;
    Arg1 = ((uint32_t)((uint32_t)(Arg1))) * (result);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA56817));
    goto loc_0056B27D;
loc_0056B27B:
    Arg1 = 0;
loc_0056B27D:
    v_stack_m78 = v_stack_m5F;
    result = HaliSaveProcessorContextAndSleep(Arg1, local_r14, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    local_r13 = 0;
loc_0056B29A:
    result = (uint32_t)((0) >> (12));
    Arg1 = ((((uint8_t)(result)) & (16)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0056B2C1;
    if ((*(uint8_t *)(v_stack_m50 + 0x8D)) == 1) {
        Arg1 = 0;
        result = KeWriteProtectPAT(Arg1, local_r14, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    }
    result = HalpPostSleepMP((uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), local_r14, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    if ((*(uint32_t *)(v_rip + 0xA5BA50)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_m48);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    }
    if (v_stack_m5E != 0) {
    }
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056AD60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
