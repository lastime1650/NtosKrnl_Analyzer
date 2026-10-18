# KiSetFeatureBits

- RVA: `0x00B6A03C`–`0x00B6A937` (길이 `2,299` bytes)
- VA: `0x0000000140B6A03C`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9F88`
- 디코드: `617`개 명령, `2,299/2,299` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x00B6A1F5` → [KiGetProcessorSignature](../../text/5C/KiGetProcessorSignature_function_005C48A8.md) (function, `0x005C48A8`)
- `0x00B6A1FF` → [KiSetProcessorSignature](../../text/5C/KiSetProcessorSignature_function_005C48C0.md) (function, `0x005C48C0`)
- `0x00B6A373` → [KiDetectKvaLeakage](../../text/5C/KiDetectKvaLeakage_function_005C4CD0.md) (function, `0x005C4CD0`)
- `0x00B6A486` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x00B6A4D3` → [KiComputeTopologyConstants](../../text/5C/KiComputeTopologyConstants_function_005C9CB8.md) (function, `0x005C9CB8`)
- `0x00B6A521` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x00B6A585` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x00B6A5CB` → [HalIsHyperThreadingEnabled](../../text/54/HalIsHyperThreadingEnabled_function_00543D60.md) (function, `0x00543D60`)
- `0x00B6A78B` → [HvlSetHardwareMbecAvailable](../../text/58/HvlSetHardwareMbecAvailable_function_0058445C.md) (function, `0x0058445C`)
- `0x00B6A795` → [HvlSetApicVirtualizationAvailable](../../text/58/HvlSetApicVirtualizationAvailable_function_0058444C.md) (function, `0x0058444C`)
- `0x00B6A800` → [HvlSetHardwareMbecAvailable](../../text/58/HvlSetHardwareMbecAvailable_function_0058445C.md) (function, `0x0058445C`)
- `0x00B6A80B` → [HvlSetApicVirtualizationAvailable](../../text/58/HvlSetApicVirtualizationAvailable_function_0058444C.md) (function, `0x0058444C`)
- `0x00B6A89F` → [KiApplyProcessorErrata](../../text/5C/KiApplyProcessorErrata_function_005C1704.md) (function, `0x005C1704`)
- `0x00B6A8A7` → [KiInitializeHresetSupport](KiInitializeHresetSupport_function_00B68A18.md) (function, `0x00B68A18`)
- `0x00B6A8DD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B6A913` → [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) (function, `0x00B85E30`)
- `0x00B6A931` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KiInitializeBootStructures](KiInitializeBootStructures_function_00B68530.md) at `0x00B688B2`

### Static image references
- `0x00B6A05F` → RVA `0x00E0A740` (`.data`; read)
- `0x00B6A0CE` → RVA `0x00FC6E60` (`ALMOSTRO`; write)
- `0x00B6A0D8` → RVA `0x00FC6E64` (`ALMOSTRO`; write)
- `0x00B6A13B` → RVA `0x00FC6CFC` (`ALMOSTRO`; write)
- `0x00B6A145` → RVA `0x00FC6D58` (`ALMOSTRO`; write)
- `0x00B6A14F` → RVA `0x00FC6CFC` (`ALMOSTRO`; read)
- `0x00B6A15C` → RVA `0x00FC6FCC` (`ALMOSTRO`; write)
- `0x00B6A2D7` → RVA `0x00FC6D28` (`ALMOSTRO`; read/write)
- `0x00B6A322` → RVA `0x00E66930` (`.data`; write)
- `0x00B6A3E9` → RVA `0x00F10A3C` (`.data`; read)
- `0x00B6A59A` → RVA `0x00FC7268` (`ALMOSTRO`; read/write)
- `0x00B6A602` → RVA `0x00E0B0F0` (`.data`; write)
- `0x00B6A616` → RVA `0x00E0B0F0` (`.data`; read)
- `0x00B6A62B` → RVA `0x00E0B0F8` (`.data`; write)
- `0x00B6A632` → RVA `0x00E0B0E8` (`.data`; write)
- `0x00B6A65D` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x00B6A66B` → RVA `0x00FC6B60` (`ALMOSTRO`; read)
- `0x00B6A6B0` → RVA `0x00FC6A87` (`ALMOSTRO`; read)
- `0x00B6A7BE` → RVA `0x00E66920` (`.data`; read/write)
- `0x00B6A86C` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00B6A8B3` → RVA `0x00FC7458` (`ALMOSTRO`; read)
- `0x00B6A8BD` → RVA `0x00FC7560` (`ALMOSTRO`; write)
- `0x00B6A8CB` → RVA `0x00FC7558` (`ALMOSTRO`; write)
- `0x00B6A90A` → RVA `0x00FC6B20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00B6A1F5` → [KiGetProcessorSignature](../../text/5C/KiGetProcessorSignature_function_005C48A8.md) (`PAGELK` → `.text`)
  - `0x00B6A1FF` → [KiSetProcessorSignature](../../text/5C/KiSetProcessorSignature_function_005C48C0.md) (`PAGELK` → `.text`)
  - `0x00B6A373` → [KiDetectKvaLeakage](../../text/5C/KiDetectKvaLeakage_function_005C4CD0.md) (`PAGELK` → `.text`)
  - `0x00B6A486` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (`PAGELK` → `.text`)
  - `0x00B6A4D3` → [KiComputeTopologyConstants](../../text/5C/KiComputeTopologyConstants_function_005C9CB8.md) (`PAGELK` → `.text`)
  - `0x00B6A521` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (`PAGELK` → `.text`)
  - `0x00B6A585` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../../text/4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (`PAGELK` → `.text`)
  - `0x00B6A5CB` → [HalIsHyperThreadingEnabled](../../text/54/HalIsHyperThreadingEnabled_function_00543D60.md) (`PAGELK` → `.text`)
  - `0x00B6A78B` → [HvlSetHardwareMbecAvailable](../../text/58/HvlSetHardwareMbecAvailable_function_0058445C.md) (`PAGELK` → `.text`)
  - `0x00B6A795` → [HvlSetApicVirtualizationAvailable](../../text/58/HvlSetApicVirtualizationAvailable_function_0058444C.md) (`PAGELK` → `.text`)
  - `0x00B6A800` → [HvlSetHardwareMbecAvailable](../../text/58/HvlSetHardwareMbecAvailable_function_0058445C.md) (`PAGELK` → `.text`)
  - `0x00B6A80B` → [HvlSetApicVirtualizationAvailable](../../text/58/HvlSetApicVirtualizationAvailable_function_0058444C.md) (`PAGELK` → `.text`)
  - `0x00B6A89F` → [KiApplyProcessorErrata](../../text/5C/KiApplyProcessorErrata_function_005C1704.md) (`PAGELK` → `.text`)
  - `0x00B6A8DD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B6A913` → [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) (`PAGELK` → `PAGEKD`)
  - `0x00B6A931` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B6A03C  48 8B C4                        mov rax, rsp
00B6A03F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00B6A043  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00B6A047  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00B6A04B  55                              push rbp
00B6A04C  41 54                           push r12
00B6A04E  41 55                           push r13
00B6A050  41 56                           push r14
00B6A052  41 57                           push r15
00B6A054  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00B6A058  48 81 EC C0 00 00 00            sub rsp, 0xc0
00B6A05F  48 8B 05 DA 06 2A 00            mov rax, qword ptr [rip + 0x2a06da]
00B6A066  48 33 C4                        xor rax, rsp
00B6A069  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00B6A06D  8A 59 40                        mov bl, byte ptr [rcx + 0x40]
00B6A070  45 33 D2                        xor r10d, r10d
00B6A073  48 8B F9                        mov rdi, rcx
00B6A076  45 0F B6 C2                     movzx r8d, r10b
00B6A07A  0F B6 49 43                     movzx ecx, byte ptr [rcx + 0x43]
00B6A07E  0F 57 C9                        xorps xmm1, xmm1
00B6A081  0F 57 C0                        xorps xmm0, xmm0
00B6A084  45 8D 4A 01                     lea r9d, [r10 + 1]
00B6A088  8A 97 8D 00 00 00               mov dl, byte ptr [rdi + 0x8d]
00B6A08E  8A C2                           mov al, dl
00B6A090  41 2A C1                        sub al, r9b
00B6A093  41 3A C1                        cmp al, r9b
00B6A096  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00B6A09A  45 0F 46 C1                     cmovbe r8d, r9d
00B6A09E  44 89 45 AF                     mov dword ptr [rbp - 0x51], r8d
00B6A0A2  0F 11 4D 07                     movups xmmword ptr [rbp + 7], xmm1
00B6A0A6  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
00B6A0AA  0F 11 4D B7                     movups xmmword ptr [rbp - 0x49], xmm1
00B6A0AE  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
00B6A0B2  44 39 57 24                     cmp dword ptr [rdi + 0x24], r10d
00B6A0B6  0F 85 2F 01 00 00               jne 0x140b6a1eb
00B6A0BC  80 FA 02                        cmp dl, 2
00B6A0BF  0F 85 F7 00 00 00               jne 0x140b6a1bc
00B6A0C5  80 FB 06                        cmp bl, 6
00B6A0C8  0F 85 3F 01 00 00               jne 0x140b6a20d
00B6A0CE  C7 05 88 CD 45 00 DD 01 00 00   mov dword ptr [rip + 0x45cd88], 0x1dd
00B6A0D8  C7 05 82 CD 45 00 DE 01 00 00   mov dword ptr [rip + 0x45cd82], 0x1de
00B6A0E2  83 F9 2D                        cmp ecx, 0x2d
00B6A0E5  0F 87 80 00 00 00               ja 0x140b6a16b
00B6A0EB  74 4E                           je 0x140b6a13b
00B6A0ED  83 F9 1F                        cmp ecx, 0x1f
00B6A0F0  77 30                           ja 0x140b6a122
00B6A0F2  74 47                           je 0x140b6a13b
00B6A0F4  83 E9 0F                        sub ecx, 0xf
00B6A0F7  0F 84 A9 00 00 00               je 0x140b6a1a6
00B6A0FD  83 E9 08                        sub ecx, 8
00B6A100  0F 84 A0 00 00 00               je 0x140b6a1a6
00B6A106  83 E9 03                        sub ecx, 3
00B6A109  74 30                           je 0x140b6a13b
00B6A10B  83 E9 02                        sub ecx, 2
00B6A10E  0F 84 92 00 00 00               je 0x140b6a1a6
00B6A114  41 2B C9                        sub ecx, r9d
00B6A117  0F 84 89 00 00 00               je 0x140b6a1a6
00B6A11D  41 3B C9                        cmp ecx, r9d
00B6A120  EB 17                           jmp 0x140b6a139
00B6A122  83 E9 25                        sub ecx, 0x25
00B6A125  74 14                           je 0x140b6a13b
00B6A127  41 2B C9                        sub ecx, r9d
00B6A12A  74 7A                           je 0x140b6a1a6
00B6A12C  41 2B C9                        sub ecx, r9d
00B6A12F  74 75                           je 0x140b6a1a6
00B6A131  83 E9 03                        sub ecx, 3
00B6A134  74 05                           je 0x140b6a13b
00B6A136  83 F9 02                        cmp ecx, 2
00B6A139  75 14                           jne 0x140b6a14f
00B6A13B  C7 05 B7 CB 45 00 80 06 00 00   mov dword ptr [rip + 0x45cbb7], 0x680
00B6A145  C7 05 09 CC 45 00 C0 06 00 00   mov dword ptr [rip + 0x45cc09], 0x6c0
00B6A14F  44 39 15 A6 CB 45 00            cmp dword ptr [rip + 0x45cba6], r10d
00B6A156  0F 84 B1 00 00 00               je 0x140b6a20d
00B6A15C  C7 05 66 CE 45 00 C9 01 00 00   mov dword ptr [rip + 0x45ce66], 0x1c9
00B6A166  E9 A2 00 00 00                  jmp 0x140b6a20d
00B6A16B  83 F9 3A                        cmp ecx, 0x3a
00B6A16E  77 1D                           ja 0x140b6a18d
00B6A170  74 C9                           je 0x140b6a13b
00B6A172  83 E9 2E                        sub ecx, 0x2e
00B6A175  74 C4                           je 0x140b6a13b
00B6A177  41 2B C9                        sub ecx, r9d
00B6A17A  74 BF                           je 0x140b6a13b
00B6A17C  83 E9 06                        sub ecx, 6
00B6A17F  74 25                           je 0x140b6a1a6
00B6A181  41 2B C9                        sub ecx, r9d
00B6A184  74 20                           je 0x140b6a1a6
00B6A186  41 3B C9                        cmp ecx, r9d
00B6A189  74 1B                           je 0x140b6a1a6
00B6A18B  EB C2                           jmp 0x140b6a14f
00B6A18D  83 E9 3C                        sub ecx, 0x3c
00B6A190  74 A9                           je 0x140b6a13b
00B6A192  83 E9 03                        sub ecx, 3
00B6A195  74 A4                           je 0x140b6a13b
00B6A197  83 E9 06                        sub ecx, 6
00B6A19A  74 9F                           je 0x140b6a13b
00B6A19C  41 2B C9                        sub ecx, r9d
00B6A19F  74 9A                           je 0x140b6a13b
00B6A1A1  83 F9 07                        cmp ecx, 7
00B6A1A4  75 A9                           jne 0x140b6a14f
00B6A1A6  C7 05 4C CB 45 00 40 00 00 00   mov dword ptr [rip + 0x45cb4c], 0x40
00B6A1B0  C7 05 9E CB 45 00 60 00 00 00   mov dword ptr [rip + 0x45cb9e], 0x60
00B6A1BA  EB A0                           jmp 0x140b6a15c
00B6A1BC  41 3A D1                        cmp dl, r9b
00B6A1BF  75 4C                           jne 0x140b6a20d
00B6A1C1  C7 05 31 CB 45 00 DB 01 00 00   mov dword ptr [rip + 0x45cb31], 0x1db
00B6A1CB  C7 05 83 CB 45 00 DC 01 00 00   mov dword ptr [rip + 0x45cb83], 0x1dc
00B6A1D5  C7 05 81 CC 45 00 DD 01 00 00   mov dword ptr [rip + 0x45cc81], 0x1dd
00B6A1DF  C7 05 7B CC 45 00 DE 01 00 00   mov dword ptr [rip + 0x45cc7b], 0x1de
00B6A1E9  EB 22                           jmp 0x140b6a20d
00B6A1EB  45 33 C9                        xor r9d, r9d
00B6A1EE  45 33 C0                        xor r8d, r8d
00B6A1F1  33 D2                           xor edx, edx
00B6A1F3  33 C9                           xor ecx, ecx
00B6A1F5  E8 AE A6 A5 FF                  call 0x1405c48a8
00B6A1FA  8B D0                           mov edx, eax
00B6A1FC  48 8B CF                        mov rcx, rdi
00B6A1FF  E8 BC A6 A5 FF                  call 0x1405c48c0
00B6A204  41 B9 01 00 00 00               mov r9d, 1
00B6A20A  45 33 D2                        xor r10d, r10d
00B6A20D  44 8A 87 8D 00 00 00            mov r8b, byte ptr [rdi + 0x8d]
00B6A214  33 C0                           xor eax, eax
00B6A216  33 C9                           xor ecx, ecx
00B6A218  0F A2                           cpuid
00B6A21A  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00B6A21D  89 45 F7                        mov dword ptr [rbp - 9], eax
00B6A220  89 5D FB                        mov dword ptr [rbp - 5], ebx
00B6A223  89 4D FF                        mov dword ptr [rbp - 1], ecx
00B6A226  89 55 03                        mov dword ptr [rbp + 3], edx
00B6A229  41 80 F8 02                     cmp r8b, 2
00B6A22D  75 20                           jne 0x140b6a24f
00B6A22F  33 C0                           xor eax, eax
00B6A231  B9 8B 00 00 00                  mov ecx, 0x8b
00B6A236  33 D2                           xor edx, edx
00B6A238  0F 30                           wrmsr
00B6A23A  41 8B C1                        mov eax, r9d
00B6A23D  33 C9                           xor ecx, ecx
00B6A23F  0F A2                           cpuid
00B6A241  89 45 F7                        mov dword ptr [rbp - 9], eax
00B6A244  89 5D FB                        mov dword ptr [rbp - 5], ebx
00B6A247  89 4D FF                        mov dword ptr [rbp - 1], ecx
00B6A24A  89 55 03                        mov dword ptr [rbp + 3], edx
00B6A24D  EB 05                           jmp 0x140b6a254
00B6A24F  45 3A C1                        cmp r8b, r9b
00B6A252  75 15                           jne 0x140b6a269
00B6A254  B9 8B 00 00 00                  mov ecx, 0x8b
00B6A259  0F 32                           rdmsr
00B6A25B  48 C1 E2 20                     shl rdx, 0x20
00B6A25F  48 0B C2                        or rax, rdx
00B6A262  48 89 87 A8 8F 00 00            mov qword ptr [rdi + 0x8fa8], rax
00B6A269  33 C9                           xor ecx, ecx
00B6A26B  41 8B C1                        mov eax, r9d
00B6A26E  0F A2                           cpuid
00B6A270  44 8B E9                        mov r13d, ecx
00B6A273  89 45 17                        mov dword ptr [rbp + 0x17], eax
00B6A276  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
00B6A279  8B F3                           mov esi, ebx
00B6A27B  33 C9                           xor ecx, ecx
00B6A27D  44 8B E2                        mov r12d, edx
00B6A280  89 5D 1B                        mov dword ptr [rbp + 0x1b], ebx
00B6A283  B8 00 00 00 80                  mov eax, 0x80000000
00B6A288  0F A2                           cpuid
00B6A28A  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00B6A28D  33 C9                           xor ecx, ecx
00B6A28F  B8 01 00 00 80                  mov eax, 0x80000001
00B6A294  44 89 65 23                     mov dword ptr [rbp + 0x23], r12d
00B6A298  0F A2                           cpuid
00B6A29A  44 8B F2                        mov r14d, edx
00B6A29D  44 8B F9                        mov r15d, ecx
00B6A2A0  44 89 7D 0F                     mov dword ptr [rbp + 0xf], r15d
00B6A2A4  89 45 07                        mov dword ptr [rbp + 7], eax
00B6A2A7  89 5D 0B                        mov dword ptr [rbp + 0xb], ebx
00B6A2AA  89 55 13                        mov dword ptr [rbp + 0x13], edx
00B6A2AD  44 39 57 24                     cmp dword ptr [rdi + 0x24], r10d
00B6A2B1  0F 85 B9 00 00 00               jne 0x140b6a370
00B6A2B7  45 3A C1                        cmp r8b, r9b
00B6A2BA  75 4F                           jne 0x140b6a30b
00B6A2BC  8A 57 40                        mov dl, byte ptr [rdi + 0x40]
00B6A2BF  8A 47 43                        mov al, byte ptr [rdi + 0x43]
00B6A2C2  8A 4F 42                        mov cl, byte ptr [rdi + 0x42]
00B6A2C5  80 FA 0F                        cmp dl, 0xf
00B6A2C8  75 16                           jne 0x140b6a2e0
00B6A2CA  3C 6B                           cmp al, 0x6b
00B6A2CC  74 04                           je 0x140b6a2d2
00B6A2CE  3C 68                           cmp al, 0x68
00B6A2D0  75 39                           jne 0x140b6a30b
00B6A2D2  41 3A C9                        cmp cl, r9b
00B6A2D5  75 34                           jne 0x140b6a30b
00B6A2D7  4C 09 0D 4A CA 45 00            or qword ptr [rip + 0x45ca4a], r9
00B6A2DE  EB 2B                           jmp 0x140b6a30b
00B6A2E0  80 FA 10                        cmp dl, 0x10
00B6A2E3  75 26                           jne 0x140b6a30b
00B6A2E5  84 C0                           test al, al
00B6A2E7  75 05                           jne 0x140b6a2ee
00B6A2E9  80 F9 02                        cmp cl, 2
00B6A2EC  76 15                           jbe 0x140b6a303
00B6A2EE  3C 02                           cmp al, 2
00B6A2F0  75 09                           jne 0x140b6a2fb
00B6A2F2  3A C8                           cmp cl, al
00B6A2F4  76 0D                           jbe 0x140b6a303
00B6A2F6  80 F9 0A                        cmp cl, 0xa
00B6A2F9  74 08                           je 0x140b6a303
00B6A2FB  3C 04                           cmp al, 4
00B6A2FD  75 0C                           jne 0x140b6a30b
00B6A2FF  84 C9                           test cl, cl
00B6A301  75 08                           jne 0x140b6a30b
00B6A303  48 83 0D 1D CA 45 00 02         or qword ptr [rip + 0x45ca1d], 2
00B6A30B  44 39 57 24                     cmp dword ptr [rdi + 0x24], r10d
00B6A30F  75 5F                           jne 0x140b6a370
00B6A311  8A 87 8D 00 00 00               mov al, byte ptr [rdi + 0x8d]
00B6A317  41 3A C1                        cmp al, r9b
00B6A31A  75 0F                           jne 0x140b6a32b
00B6A31C  80 7F 40 17                     cmp byte ptr [rdi + 0x40], 0x17
00B6A320  75 4E                           jne 0x140b6a370
00B6A322  44 89 0D 07 C6 2F 00            mov dword ptr [rip + 0x2fc607], r9d
00B6A329  EB 45                           jmp 0x140b6a370
00B6A32B  3C 02                           cmp al, 2
00B6A32D  75 41                           jne 0x140b6a370
00B6A32F  80 7F 40 06                     cmp byte ptr [rdi + 0x40], 6
00B6A333  75 3B                           jne 0x140b6a370
00B6A335  0F B6 4F 43                     movzx ecx, byte ptr [rdi + 0x43]
00B6A339  80 F9 36                        cmp cl, 0x36
00B6A33C  77 10                           ja 0x140b6a34e
00B6A33E  48 BA 00 00 00 10 C0 00 60 00   movabs rdx, 0x6000c010000000
00B6A348  48 0F A3 CA                     bt rdx, rcx
00B6A34C  72 18                           jb 0x140b6a366
00B6A34E  80 E9 37                        sub cl, 0x37
00B6A351  80 F9 16                        cmp cl, 0x16
00B6A354  77 1A                           ja 0x140b6a370
00B6A356  B8 01 00 48 00                  mov eax, 0x480001
00B6A35B  0F A3 C8                        bt eax, ecx
00B6A35E  73 10                           jae 0x140b6a370
00B6A360  80 7F 42 07                     cmp byte ptr [rdi + 0x42], 7
00B6A364  77 0A                           ja 0x140b6a370
00B6A366  C7 05 C0 C5 2F 00 02 00 00 00   mov dword ptr [rip + 0x2fc5c0], 2
00B6A370  48 8B CF                        mov rcx, rdi
00B6A373  E8 58 A9 A5 FF                  call 0x1405c4cd0
00B6A378  0F 0D 0F                        prefetchw byte ptr [rdi]
00B6A37B  80 BF 8D 00 00 00 01            cmp byte ptr [rdi + 0x8d], 1
00B6A382  75 09                           jne 0x140b6a38d
00B6A384  41 0F BA EE 14                  bts r14d, 0x14
00B6A389  44 89 75 13                     mov dword ptr [rbp + 0x13], r14d
00B6A38D  8B C6                           mov eax, esi
00B6A38F  B9 FD F3 89 07                  mov ecx, 0x789f3fd
00B6A394  C1 E8 18                        shr eax, 0x18
00B6A397  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
00B6A39D  41 8B C4                        mov eax, r12d
00B6A3A0  C1 EE 05                        shr esi, 5
00B6A3A3  23 C1                           and eax, ecx
00B6A3A5  81 E6 F8 07 00 00               and esi, 0x7f8
00B6A3AB  89 B7 E8 00 00 00               mov dword ptr [rdi + 0xe8], esi
00B6A3B1  3B C1                           cmp eax, ecx
00B6A3B3  0F 85 4B 05 00 00               jne 0x140b6a904
00B6A3B9  41 0F BA E6 0B                  bt r14d, 0xb
00B6A3BE  0F 83 40 05 00 00               jae 0x140b6a904
00B6A3C4  41 0F BA E6 14                  bt r14d, 0x14
00B6A3C9  0F 83 35 05 00 00               jae 0x140b6a904
00B6A3CF  41 0F BA E5 0D                  bt r13d, 0xd
00B6A3D4  0F 83 2A 05 00 00               jae 0x140b6a904
00B6A3DA  41 BD 01 00 00 00               mov r13d, 1
00B6A3E0  45 84 FD                        test r13b, r15b
00B6A3E3  0F 84 1B 05 00 00               je 0x140b6a904
00B6A3E9  83 3D 4C 66 3A 00 00            cmp dword ptr [rip + 0x3a664c], 0
00B6A3F0  0F 85 0E 05 00 00               jne 0x140b6a904
00B6A3F6  48 8B B7 A0 8F 00 00            mov rsi, qword ptr [rdi + 0x8fa0]
00B6A3FD  48 81 CE FE 3D 11 20            or rsi, 0x20113dfe
00B6A404  48 0F BA E6 22                  bt rsi, 0x22
00B6A409  73 23                           jae 0x140b6a42e
00B6A40B  0F B6 87 D1 00 00 00            movzx eax, byte ptr [rdi + 0xd1]
00B6A412  B9 03 01 00 C0                  mov ecx, 0xc0000103
00B6A417  0F B6 97 D0 00 00 00            movzx edx, byte ptr [rdi + 0xd0]
00B6A41E  48 C1 E2 08                     shl rdx, 8
00B6A422  48 0B D0                        or rdx, rax
00B6A425  48 8B C2                        mov rax, rdx
00B6A428  48 C1 EA 20                     shr rdx, 0x20
00B6A42C  0F 30                           wrmsr
00B6A42E  33 C0                           xor eax, eax
00B6A430  B9 74 01 00 00                  mov ecx, 0x174
00B6A435  33 D2                           xor edx, edx
00B6A437  0F 30                           wrmsr
00B6A439  B9 76 01 00 00                  mov ecx, 0x176
00B6A43E  0F 30                           wrmsr
00B6A440  B9 75 01 00 00                  mov ecx, 0x175
00B6A445  0F 30                           wrmsr
00B6A447  41 0F BA E6 19                  bt r14d, 0x19
00B6A44C  73 1C                           jae 0x140b6a46a
00B6A44E  B9 80 00 00 C0                  mov ecx, 0xc0000080
00B6A453  0F 32                           rdmsr
00B6A455  48 C1 E2 20                     shl rdx, 0x20
00B6A459  48 0B C2                        or rax, rdx
00B6A45C  48 0F BA E8 0E                  bts rax, 0xe
00B6A461  48 8B D0                        mov rdx, rax
00B6A464  48 C1 EA 20                     shr rdx, 0x20
00B6A468  0F 30                           wrmsr
00B6A46A  44 89 AF A0 00 00 00            mov dword ptr [rdi + 0xa0], r13d
00B6A471  44 89 AF A4 00 00 00            mov dword ptr [rdi + 0xa4], r13d
00B6A478  44 89 AF C8 9E 00 00            mov dword ptr [rdi + 0x9ec8], r13d
00B6A47F  44 89 AF CC 9E 00 00            mov dword ptr [rdi + 0x9ecc], r13d
00B6A486  E8 55 9C 98 FF                  call 0x1404f40e0
00B6A48B  85 C0                           test eax, eax
00B6A48D  74 07                           je 0x140b6a496
00B6A48F  44 89 AF 48 BB 00 00            mov dword ptr [rdi + 0xbb48], r13d
00B6A496  0F 28 45 17                     movaps xmm0, xmmword ptr [rbp + 0x17]
00B6A49A  48 8D 45 B7                     lea rax, [rbp - 0x49]
00B6A49E  0F 28 4D 07                     movaps xmm1, xmmword ptr [rbp + 7]
00B6A4A2  4C 8D 4D E7                     lea r9, [rbp - 0x19]
00B6A4A6  44 8B 65 A7                     mov r12d, dword ptr [rbp - 0x59]
00B6A4AA  45 8B C4                        mov r8d, r12d
00B6A4AD  44 8B 7D AB                     mov r15d, dword ptr [rbp - 0x55]
00B6A4B1  41 8B D7                        mov edx, r15d
00B6A4B4  0F B6 8F 8D 00 00 00            movzx ecx, byte ptr [rdi + 0x8d]
00B6A4BB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B6A4C0  48 8D 45 D7                     lea rax, [rbp - 0x29]
00B6A4C4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B6A4C9  66 0F 7F 45 D7                  movdqa xmmword ptr [rbp - 0x29], xmm0
00B6A4CE  66 0F 7F 4D E7                  movdqa xmmword ptr [rbp - 0x19], xmm1
00B6A4D3  E8 E0 F7 A5 FF                  call 0x1405c9cb8
00B6A4D8  8B 5D B7                        mov ebx, dword ptr [rbp - 0x49]
00B6A4DB  F6 C3 10                        test bl, 0x10
00B6A4DE  74 09                           je 0x140b6a4e9
00B6A4E0  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
00B6A4E3  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
00B6A4E9  41 84 DD                        test r13b, bl
00B6A4EC  74 09                           je 0x140b6a4f7
00B6A4EE  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
00B6A4F1  89 87 A4 00 00 00               mov dword ptr [rdi + 0xa4], eax
00B6A4F7  F6 C3 08                        test bl, 8
00B6A4FA  74 09                           je 0x140b6a505
00B6A4FC  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
00B6A4FF  89 87 CC 9E 00 00               mov dword ptr [rdi + 0x9ecc], eax
00B6A505  F6 C3 02                        test bl, 2
00B6A508  74 09                           je 0x140b6a513
00B6A50A  8B 45 C3                        mov eax, dword ptr [rbp - 0x3d]
00B6A50D  89 87 A0 00 00 00               mov dword ptr [rdi + 0xa0], eax
00B6A513  F6 C3 04                        test bl, 4
00B6A516  74 09                           je 0x140b6a521
00B6A518  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00B6A51B  89 87 C8 9E 00 00               mov dword ptr [rdi + 0x9ec8], eax
00B6A521  E8 BA 9B 98 FF                  call 0x1404f40e0
00B6A526  85 C0                           test eax, eax
00B6A528  74 0E                           je 0x140b6a538
00B6A52A  F6 C3 20                        test bl, 0x20
00B6A52D  74 09                           je 0x140b6a538
00B6A52F  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
00B6A532  89 87 48 BB 00 00               mov dword ptr [rdi + 0xbb48], eax
00B6A538  8A 87 A4 00 00 00               mov al, byte ptr [rdi + 0xa4]
00B6A53E  44 8B 75 BB                     mov r14d, dword ptr [rbp - 0x45]
00B6A542  88 87 8F 00 00 00               mov byte ptr [rdi + 0x8f], al
00B6A548  8A 87 A0 00 00 00               mov al, byte ptr [rdi + 0xa0]
00B6A54E  88 87 8E 00 00 00               mov byte ptr [rdi + 0x8e], al
00B6A554  41 8B C6                        mov eax, r14d
00B6A557  41 23 C5                        and eax, r13d
00B6A55A  8D 0C 45 01 00 00 00            lea ecx, [rax*2 + 1]
00B6A561  8B D1                           mov edx, ecx
00B6A563  83 CA 04                        or edx, 4
00B6A566  41 F6 C6 08                     test r14b, 8
00B6A56A  0F 44 D1                        cmove edx, ecx
00B6A56D  8B CA                           mov ecx, edx
00B6A56F  83 C9 08                        or ecx, 8
00B6A572  41 F6 C6 04                     test r14b, 4
00B6A576  0F 44 CA                        cmove ecx, edx
00B6A579  8B D9                           mov ebx, ecx
00B6A57B  83 CB 10                        or ebx, 0x10
00B6A57E  41 F6 C6 02                     test r14b, 2
00B6A582  0F 44 D9                        cmove ebx, ecx
00B6A585  E8 56 9B 98 FF                  call 0x1404f40e0
00B6A58A  45 33 D2                        xor r10d, r10d
00B6A58D  85 C0                           test eax, eax
00B6A58F  74 09                           je 0x140b6a59a
00B6A591  41 F6 C6 20                     test r14b, 0x20
00B6A595  74 03                           je 0x140b6a59a
00B6A597  83 CB 20                        or ebx, 0x20
00B6A59A  F0 09 1D C7 CC 45 00            lock or dword ptr [rip + 0x45ccc7], ebx
00B6A5A1  44 8A B7 8D 00 00 00            mov r14b, byte ptr [rdi + 0x8d]
00B6A5A8  45 3A F5                        cmp r14b, r13b
00B6A5AB  75 07                           jne 0x140b6a5b4
00B6A5AD  48 0F BA EE 15                  bts rsi, 0x15
00B6A5B2  EB 0B                           jmp 0x140b6a5bf
00B6A5B4  41 80 FE 02                     cmp r14b, 2
00B6A5B8  75 05                           jne 0x140b6a5bf
00B6A5BA  48 0F BA EE 18                  bts rsi, 0x18
00B6A5BF  8B 9F A4 00 00 00               mov ebx, dword ptr [rdi + 0xa4]
00B6A5C5  44 39 57 24                     cmp dword ptr [rdi + 0x24], r10d
00B6A5C9  74 13                           je 0x140b6a5de
00B6A5CB  E8 90 97 9D FF                  call 0x140543d60
00B6A5D0  45 33 D2                        xor r10d, r10d
00B6A5D3  84 C0                           test al, al
00B6A5D5  75 07                           jne 0x140b6a5de
00B6A5D7  0F AF 9F A0 00 00 00            imul ebx, dword ptr [rdi + 0xa0]
00B6A5DE  F7 DB                           neg ebx
00B6A5E0  41 8A C6                        mov al, r14b
00B6A5E3  41 2A C5                        sub al, r13b
00B6A5E6  89 9F DC 00 00 00               mov dword ptr [rdi + 0xdc], ebx
00B6A5EC  3C 02                           cmp al, 2
00B6A5EE  77 26                           ja 0x140b6a616
00B6A5F0  41 81 FC 08 00 00 80            cmp r12d, 0x80000008
00B6A5F7  72 11                           jb 0x140b6a60a
00B6A5F9  B8 08 00 00 80                  mov eax, 0x80000008
00B6A5FE  33 C9                           xor ecx, ecx
00B6A600  0F A2                           cpuid
00B6A602  88 05 E8 0A 2A 00               mov byte ptr [rip + 0x2a0ae8], al
00B6A608  EB 0C                           jmp 0x140b6a616
00B6A60A  45 3A F5                        cmp r14b, r13b
00B6A60D  75 07                           jne 0x140b6a616
00B6A60F  C6 05 DA 0A 2A 00 28            mov byte ptr [rip + 0x2a0ada], 0x28
00B6A616  8A 0D D4 0A 2A 00               mov cl, byte ptr [rip + 0x2a0ad4]
00B6A61C  49 8B C5                        mov rax, r13
00B6A61F  48 D3 E0                        shl rax, cl
00B6A622  49 2B C5                        sub rax, r13
00B6A625  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00B6A62B  48 89 05 C6 0A 2A 00            mov qword ptr [rip + 0x2a0ac6], rax
00B6A632  48 89 05 AF 0A 2A 00            mov qword ptr [rip + 0x2a0aaf], rax
00B6A639  0F 20 E1                        mov rcx, cr4
00B6A63C  41 84 F5                        test r13b, sil
00B6A63F  74 05                           je 0x140b6a646
00B6A641  48 0F BA E9 14                  bts rcx, 0x14
00B6A646  48 8B C6                        mov rax, rsi
00B6A649  48 8B D9                        mov rbx, rcx
00B6A64C  48 0F BA EB 10                  bts rbx, 0x10
00B6A651  25 00 00 00 10                  and eax, 0x10000000
00B6A656  48 85 C0                        test rax, rax
00B6A659  48 0F 44 D9                     cmove rbx, rcx
00B6A65D  44 39 15 8C C5 45 00            cmp dword ptr [rip + 0x45c58c], r10d
00B6A664  74 05                           je 0x140b6a66b
00B6A666  48 0F BA EB 15                  bts rbx, 0x15
00B6A66B  48 8B 15 EE C4 45 00            mov rdx, qword ptr [rip + 0x45c4ee]
00B6A672  48 8B CB                        mov rcx, rbx
00B6A675  48 0F BA E9 0B                  bts rcx, 0xb
00B6A67A  41 BE 00 00 00 08               mov r14d, 0x8000000
00B6A680  F6 C2 04                        test dl, 4
00B6A683  41 BB 00 00 02 00               mov r11d, 0x20000
00B6A689  48 0F 44 CB                     cmove rcx, rbx
00B6A68D  81 E2 00 40 00 00               and edx, 0x4000
00B6A693  48 8B D9                        mov rbx, rcx
00B6A696  49 0B DE                        or rbx, r14
00B6A699  48 85 D2                        test rdx, rdx
00B6A69C  48 0F 44 D9                     cmove rbx, rcx
00B6A6A0  48 8B C3                        mov rax, rbx
00B6A6A3  44 39 57 24                     cmp dword ptr [rdi + 0x24], r10d
00B6A6A7  74 13                           je 0x140b6a6bc
00B6A6A9  48 0F BA E6 2A                  bt rsi, 0x2a
00B6A6AE  73 0C                           jae 0x140b6a6bc
00B6A6B0  44 38 15 D0 C3 45 00            cmp byte ptr [rip + 0x45c3d0], r10b
00B6A6B7  74 03                           je 0x140b6a6bc
00B6A6B9  49 0B C3                        or rax, r11
00B6A6BC  0F 22 E0                        mov cr4, rax
00B6A6BF  44 39 15 2A C5 45 00            cmp dword ptr [rip + 0x45c52a], r10d
00B6A6C6  74 03                           je 0x140b6a6cb
00B6A6C8  0F 01 CB                        stac
00B6A6CB  49 85 C3                        test r11, rax
00B6A6CE  74 0A                           je 0x140b6a6da
00B6A6D0  0F 20 D8                        mov rax, cr3
00B6A6D3  48 83 C8 02                     or rax, 2
00B6A6D7  0F 22 D8                        mov cr3, rax
00B6A6DA  44 8A 8F 8D 00 00 00            mov r9b, byte ptr [rdi + 0x8d]
00B6A6E1  41 80 F9 02                     cmp r9b, 2
00B6A6E5  75 30                           jne 0x140b6a717
00B6A6E7  41 83 FF 07                     cmp r15d, 7
00B6A6EB  72 2A                           jb 0x140b6a717
00B6A6ED  33 C9                           xor ecx, ecx
00B6A6EF  B8 07 00 00 00                  mov eax, 7
00B6A6F4  0F A2                           cpuid
00B6A6F6  0F BA E3 0F                     bt ebx, 0xf
00B6A6FA  73 1B                           jae 0x140b6a717
00B6A6FC  33 C9                           xor ecx, ecx
00B6A6FE  B8 10 00 00 00                  mov eax, 0x10
00B6A703  0F A2                           cpuid
00B6A705  41 84 D9                        test r9b, bl
00B6A708  74 0D                           je 0x140b6a717
00B6A70A  48 B8 00 00 00 00 00 10 00 00   movabs rax, 0x100000000000
00B6A714  48 0B F0                        or rsi, rax
00B6A717  4C 8B C6                        mov r8, rsi
00B6A71A  4D 0B C3                        or r8, r11
00B6A71D  44 38 55 AF                     cmp byte ptr [rbp - 0x51], r10b
00B6A721  49 BA 00 00 00 00 00 01 00 00   movabs r10, 0x10000000000
00B6A72B  4C 0F 44 C6                     cmove r8, rsi
00B6A72F  49 8B F0                        mov rsi, r8
00B6A732  41 80 F9 02                     cmp r9b, 2
00B6A736  0F 85 97 00 00 00               jne 0x140b6a7d3
00B6A73C  33 C9                           xor ecx, ecx
00B6A73E  41 8B C5                        mov eax, r13d
00B6A741  0F A2                           cpuid
00B6A743  F6 C1 20                        test cl, 0x20
00B6A746  0F 84 E0 00 00 00               je 0x140b6a82c
00B6A74C  B9 82 04 00 00                  mov ecx, 0x482
00B6A751  0F 32                           rdmsr
00B6A753  48 C1 E2 20                     shl rdx, 0x20
00B6A757  49 8B D8                        mov rbx, r8
00B6A75A  48 0B C2                        or rax, rdx
00B6A75D  7D 3B                           jge 0x140b6a79a
00B6A75F  B9 8B 04 00 00                  mov ecx, 0x48b
00B6A764  0F 32                           rdmsr
00B6A766  48 C1 E2 20                     shl rdx, 0x20
00B6A76A  48 0B D0                        or rdx, rax
00B6A76D  48 0F BA E2 21                  bt rdx, 0x21
00B6A772  73 05                           jae 0x140b6a779
00B6A774  48 0F BA EB 1A                  bts rbx, 0x1a
00B6A779  48 0F BA E2 36                  bt rdx, 0x36
00B6A77E  0F 92 C1                        setb cl
00B6A781  41 84 DD                        test r13b, bl
00B6A784  0F 95 C0                        setne al
00B6A787  84 C8                           test al, cl
00B6A789  74 05                           je 0x140b6a790
00B6A78B  E8 CC 9C A1 FF                  call 0x14058445c
00B6A790  49 85 D2                        test r10, rdx
00B6A793  74 05                           je 0x140b6a79a
00B6A795  E8 B2 9C A1 FF                  call 0x14058444c
00B6A79A  B9 3A 00 00 00                  mov ecx, 0x3a
00B6A79F  0F 32                           rdmsr
00B6A7A1  48 C1 E2 20                     shl rdx, 0x20
00B6A7A5  48 8B F3                        mov rsi, rbx
00B6A7A8  48 0B C2                        or rax, rdx
00B6A7AB  49 0B F6                        or rsi, r14
00B6A7AE  48 8B C8                        mov rcx, rax
00B6A7B1  24 05                           and al, 5
00B6A7B3  3C 05                           cmp al, 5
00B6A7B5  48 0F 45 F3                     cmovne rsi, rbx
00B6A7B9  F6 C1 04                        test cl, 4
00B6A7BC  74 07                           je 0x140b6a7c5
00B6A7BE  44 08 2D 5B C1 2F 00            or byte ptr [rip + 0x2fc15b], r13b
00B6A7C5  41 84 CD                        test r13b, cl
00B6A7C8  74 62                           je 0x140b6a82c
00B6A7CA  80 0D 4F C1 2F 00 02            or byte ptr [rip + 0x2fc14f], 2
00B6A7D1  EB 59                           jmp 0x140b6a82c
00B6A7D3  45 3A CD                        cmp r9b, r13b
00B6A7D6  75 54                           jne 0x140b6a82c
00B6A7D8  33 C9                           xor ecx, ecx
00B6A7DA  B8 00 00 00 80                  mov eax, 0x80000000
00B6A7DF  0F A2                           cpuid
00B6A7E1  3D 0A 00 00 80                  cmp eax, 0x8000000a
00B6A7E6  72 28                           jb 0x140b6a810
00B6A7E8  33 C9                           xor ecx, ecx
00B6A7EA  B8 0A 00 00 80                  mov eax, 0x8000000a
00B6A7EF  0F A2                           cpuid
00B6A7F1  41 84 D5                        test r13b, dl
00B6A7F4  74 05                           je 0x140b6a7fb
00B6A7F6  48 0F BA EE 1A                  bts rsi, 0x1a
00B6A7FB  41 85 D3                        test r11d, edx
00B6A7FE  74 05                           je 0x140b6a805
00B6A800  E8 57 9C A1 FF                  call 0x14058445c
00B6A805  0F BA E2 0D                     bt edx, 0xd
00B6A809  73 05                           jae 0x140b6a810
00B6A80B  E8 3C 9C A1 FF                  call 0x14058444c
00B6A810  B9 14 01 01 C0                  mov ecx, 0xc0010114
00B6A815  0F 32                           rdmsr
00B6A817  48 C1 E2 20                     shl rdx, 0x20
00B6A81B  48 0B C2                        or rax, rdx
00B6A81E  A8 10                           test al, 0x10
00B6A820  75 0A                           jne 0x140b6a82c
00B6A822  49 0B F6                        or rsi, r14
00B6A825  44 08 2D F4 C0 2F 00            or byte ptr [rip + 0x2fc0f4], r13b
00B6A82C  80 BF 8D 00 00 00 02            cmp byte ptr [rdi + 0x8d], 2
00B6A833  75 67                           jne 0x140b6a89c
00B6A835  33 C9                           xor ecx, ecx
00B6A837  B8 07 00 00 00                  mov eax, 7
00B6A83C  0F A2                           cpuid
00B6A83E  F6 C3 04                        test bl, 4
00B6A841  74 59                           je 0x140b6a89c
00B6A843  B9 3A 00 00 00                  mov ecx, 0x3a
00B6A848  0F 32                           rdmsr
00B6A84A  48 C1 E2 20                     shl rdx, 0x20
00B6A84E  B9 01 00 04 00                  mov ecx, 0x40001
00B6A853  48 0B C2                        or rax, rdx
00B6A856  48 23 C1                        and rax, rcx
00B6A859  48 3B C1                        cmp rax, rcx
00B6A85C  75 3E                           jne 0x140b6a89c
00B6A85E  33 C9                           xor ecx, ecx
00B6A860  B8 12 00 00 00                  mov eax, 0x12
00B6A865  0F A2                           cpuid
00B6A867  41 84 C5                        test r13b, al
00B6A86A  74 30                           je 0x140b6a89c
00B6A86C  48 8B 0D 95 A7 45 00            mov rcx, qword ptr [rip + 0x45a795]
00B6A873  49 0B F2                        or rsi, r10
00B6A876  83 89 6C 03 00 00 02            or dword ptr [rcx + 0x36c], 2
00B6A87D  A8 02                           test al, 2
00B6A87F  74 1B                           je 0x140b6a89c
00B6A881  48 B8 00 00 00 00 00 08 00 00   movabs rax, 0x80000000000
00B6A88B  48 0B F0                        or rsi, rax
00B6A88E  48 8B 05 73 A7 45 00            mov rax, qword ptr [rip + 0x45a773]
00B6A895  83 88 6C 03 00 00 04            or dword ptr [rax + 0x36c], 4
00B6A89C  48 8B CF                        mov rcx, rdi
00B6A89F  E8 60 6E A5 FF                  call 0x1405c1704
00B6A8A4  48 8B CF                        mov rcx, rdi
00B6A8A7  E8 6C E1 FF FF                  call 0x140b68a18
00B6A8AC  48 89 B7 A0 8F 00 00            mov qword ptr [rdi + 0x8fa0], rsi
00B6A8B3  48 8D 05 9E CB 45 00            lea rax, [rip + 0x45cb9e]
00B6A8BA  0F 57 C0                        xorps xmm0, xmm0
00B6A8BD  48 89 05 9C CC 45 00            mov qword ptr [rip + 0x45cc9c], rax
00B6A8C4  0F 11 05 8D CB 45 00            movups xmmword ptr [rip + 0x45cb8d], xmm0
00B6A8CB  48 C7 05 82 CC 45 00 80 00 00 00  mov qword ptr [rip + 0x45cc82], 0x80
00B6A8D6  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
00B6A8DA  48 33 CC                        xor rcx, rsp
00B6A8DD  E8 5E 1D B4 FF                  call 0x1406ac640
00B6A8E2  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
00B6A8EA  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00B6A8EE  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00B6A8F2  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00B6A8F6  49 8B E3                        mov rsp, r11
00B6A8F9  41 5F                           pop r15
00B6A8FB  41 5E                           pop r14
00B6A8FD  41 5D                           pop r13
00B6A8FF  41 5C                           pop r12
00B6A901  5D                              pop rbp
00B6A902  C3                              ret
00B6A903  CC                              int3
00B6A904  83 7F 24 00                     cmp dword ptr [rdi + 0x24], 0
00B6A908  75 0E                           jne 0x140b6a918
00B6A90A  48 8B 15 0F C2 45 00            mov rdx, qword ptr [rip + 0x45c20f]
00B6A911  33 C9                           xor ecx, ecx
00B6A913  E8 18 B5 01 00                  call 0x140b85e30
00B6A918  8B 05 1E 61 3A 00               mov eax, dword ptr [rip + 0x3a611e]
00B6A91E  4D 8B CF                        mov r9, r15
00B6A921  45 8B C6                        mov r8d, r14d
00B6A924  49 8B D4                        mov rdx, r12
00B6A927  B9 5D 00 00 00                  mov ecx, 0x5d
00B6A92C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B6A931  E8 2A 2D 99 FF                  call 0x1404fd660
00B6A936  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetFeatureBits(__int64 a1)
{
    __int64 result;
    __int64 v_cr3;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 2754266)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    v_r10 = 0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) - ((unsigned __int8)(v_r10 + 1)));
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    a3 = 0;
    if (((unsigned __int8)(result)) <= ((unsigned __int8)(v_r10 + 1))) { a3 = (unsigned int)(v_r10 + 1); }
    *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)(a3);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = v_xmm1;
    if ((*(unsigned int *)(a1 + 36)) != 0) goto loc_00B6A1EB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_00B6A1BC;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) != 6) goto loc_00B6A20D;
    *(unsigned int *)(v_rip + 4574600) = 477;
    *(unsigned int *)(v_rip + 4574594) = 478;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 67))) > 45) goto loc_00B6A16B;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 67))) == 45) goto loc_00B6A13B;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 67))) > 31) goto loc_00B6A122;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 67))) == 31) goto loc_00B6A13B;
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 67)) - (15));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - (8));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    goto loc_00B6A139;
loc_00B6A122:
    a1 = (unsigned int)((a1) - (37));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
loc_00B6A139:
    if (((unsigned int)(a1)) == 2) {
        *(unsigned int *)(v_rip + 4574135) = 0x680ULL;
        *(unsigned int *)(v_rip + 4574217) = 0x6C0ULL;
    }
    if ((*(unsigned int *)(v_rip + 4574118)) == 0) goto loc_00B6A20D;
loc_00B6A15C:
    *(unsigned int *)(v_rip + 4574822) = 457;
    goto loc_00B6A20D;
loc_00B6A16B:
    if (((unsigned int)(a1)) > 58) goto loc_00B6A18D;
    if (((unsigned int)(a1)) == 58) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - (46));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B6A1A6;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    if (((unsigned int)(a1)) == ((unsigned int)(v_r10 + 1))) goto loc_00B6A1A6;
    goto loc_00B6A14F;
loc_00B6A18D:
    a1 = (unsigned int)((a1) - (60));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B6A13B;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A13B;
    if (((unsigned int)(a1)) != 7) goto loc_00B6A14F;
loc_00B6A1A6:
    *(unsigned int *)(v_rip + 4574028) = 64;
    *(unsigned int *)(v_rip + 4574110) = 96;
    goto loc_00B6A15C;
loc_00B6A1BC:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != ((unsigned __int8)(v_r10 + 1))) goto loc_00B6A20D;
    *(unsigned int *)(v_rip + 4574001) = 475;
    *(unsigned int *)(v_rip + 4574083) = 476;
    *(unsigned int *)(v_rip + 4574337) = 477;
    *(unsigned int *)(v_rip + 4574331) = 478;
    goto loc_00B6A20D;
loc_00B6A1EB:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiGetProcessorSignature(a1, a2, a3, a4);
    result = KiSetProcessorSignature(0, (unsigned int)((unsigned int)(result)), a3, a4);
    v_r10 = 0;
loc_00B6A20D:
    result = 0;
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 - 85) = 0;
    *(unsigned int *)(v_rsp - 95 - 9) = 0;
    *(unsigned int *)(v_rsp - 95 - 5) = (unsigned int)(*(unsigned __int8 *)(a1 + 64));
    *(unsigned int *)(v_rsp - 95 - 1) = 0;
    *(unsigned int *)(v_rsp - 95 + 3) = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_00B6A24F;
    result = 0;
    a2 = 0;
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 - 9) = 1;
    *(unsigned int *)(v_rsp - 95 - 5) = (unsigned int)(*(unsigned __int8 *)(a1 + 64));
    *(unsigned int *)(v_rsp - 95 - 1) = 0;
    *(unsigned int *)(v_rsp - 95 + 3) = 0;
    goto loc_00B6A254;
loc_00B6A24F:
    result = 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) == 1) {
        a1 = 139;
        a2 = (a2) << (32);
        result = (1) | (a2);
        *(unsigned __int64 *)(a1 + 36776) = result;
    }
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 + 23) = 1;
    *(unsigned int *)(v_rsp - 95 + 31) = 0;
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 + 27) = (unsigned int)(*(unsigned __int8 *)(a1 + 64));
    *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)((unsigned int)(0x80000000ULL));
    a1 = 0;
    *(unsigned int *)(v_rsp - 95 + 35) = (unsigned int)((unsigned int)((unsigned int)(a2)));
    *(unsigned int *)(v_rsp - 95 + 15) = 0;
    *(unsigned int *)(v_rsp - 95 + 7) = (unsigned int)((unsigned int)(0x80000001ULL));
    *(unsigned int *)(v_rsp - 95 + 11) = (unsigned int)(*(unsigned __int8 *)(a1 + 64));
    *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)(a2);
    if ((*(unsigned int *)(a1 + 36)) != 0) goto loc_00B6A370;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 1) goto loc_00B6A30B;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) != 15) goto loc_00B6A2E0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) == 107) goto loc_00B6A2D2;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) != 104) goto loc_00B6A30B;
loc_00B6A2D2:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) != 1) goto loc_00B6A30B;
    goto loc_00B6A30B;
loc_00B6A2E0:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) != 16) goto loc_00B6A30B;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 67)) != 0) goto loc_00B6A2EE;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) <= 2) goto loc_00B6A303;
loc_00B6A2EE:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) != 2) goto loc_00B6A2FB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) <= ((unsigned __int8)(*(unsigned __int8 *)(a1 + 67)))) goto loc_00B6A303;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) == 10) goto loc_00B6A303;
loc_00B6A2FB:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) != 4) goto loc_00B6A30B;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 66)) == 0) {
    }
    if ((*(unsigned int *)(a1 + 36)) != 0) goto loc_00B6A370;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 1) goto loc_00B6A32B;
    if ((*(unsigned __int8 *)(a1 + 64)) != 23) goto loc_00B6A370;
    *(unsigned int *)(v_rip + 3130887) = 1;
    goto loc_00B6A370;
loc_00B6A32B:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_00B6A370;
    if ((*(unsigned __int8 *)(a1 + 64)) != 6) goto loc_00B6A370;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) > 54) goto loc_00B6A34E;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) < 54) goto loc_00B6A366;
loc_00B6A34E:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 67)) - (55));
    if (((unsigned __int8)(a1)) > 22) goto loc_00B6A370;
    if (((unsigned __int8)(a1)) >= 22) goto loc_00B6A370;
    if ((*(unsigned __int8 *)(a1 + 66)) <= 7) {
        *(unsigned int *)(v_rip + 3130816) = 2;
    }
    result = KiDetectKvaLeakage(a1, *(unsigned __int8 *)(a1 + 64), *(unsigned __int8 *)(a1 + 141), 1);
    if ((*(unsigned __int8 *)(a1 + 141)) == 1) {
        *(unsigned int *)(v_rsp - 95 + 19) = (unsigned int)((unsigned int)((unsigned int)(a2)));
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 64)))))) >> (24));
    *(unsigned int *)(a1 + 212) = (unsigned int)(result);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 64)))) >> (5));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) & ((unsigned int)((unsigned int)(0x789F3FDULL))));
    v_rsi = (unsigned int)((v_rsi) & (0x7F8ULL));
    *(unsigned int *)(a1 + 232) = (unsigned int)(v_rsi);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((1) & (0)) == 0) goto loc_00B6A904;
    if ((*(unsigned int *)(v_rip + 3827276)) != 0) goto loc_00B6A904;
    v_rsi = (*(unsigned __int64 *)(a1 + 36768)) | (0x20113DFEULL);
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int8 *)(a1 + 209);
        a1 = 0xC0000103ULL;
        a2 = *(unsigned __int8 *)(a1 + 208);
        a2 = (a2) << (8);
        a2 = (a2) | (result);
        result = a2;
        a2 = (a2) >> (32);
    }
    result = 0;
    a2 = 0;
    if (!(condition_is_above_or_equal)) {
        a1 = 0xC0000080ULL;
        a2 = (a2) << (32);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    *(unsigned int *)(a1 + 160) = 1;
    *(unsigned int *)(a1 + 164) = 1;
    *(unsigned int *)(a1 + 40648) = 1;
    *(unsigned int *)(a1 + 40652) = 1;
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(a1, a2, *(unsigned __int8 *)(a1 + 141), 1);
    if ((unsigned int)(result) != 0) {
        *(unsigned int *)(a1 + 47944) = 1;
    }
    v_stack_mC0 = v_rsp - 95 - 73;
    v_stack_mC8 = v_rsp - 95 - 41;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm1;
    result = KiComputeTopologyConstants(*(unsigned __int8 *)(a1 + 141), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), v_rsp - 95 - 25);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) & (16)) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 49);
        *(unsigned int *)(a1 + 212) = (unsigned int)(result);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))))) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 65);
        *(unsigned int *)(a1 + 164) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) & (8)) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 53);
        *(unsigned int *)(a1 + 40652) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) & (2)) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 61);
        *(unsigned int *)(a1 + 160) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) & (4)) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 57);
        *(unsigned int *)(a1 + 40648) = (unsigned int)(result);
    }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(*(unsigned __int8 *)(a1 + 141), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), v_rsp - 95 - 25);
    if ((unsigned int)(result) == 0) goto loc_00B6A538;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) & (32)) != 0) {
        result = *(unsigned int *)(v_rsp - 95 - 45);
        *(unsigned int *)(a1 + 47944) = (unsigned int)(result);
    }
    *(unsigned __int8 *)(a1 + 143) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 164));
    *(unsigned __int8 *)(a1 + 142) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 160));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) & (1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result * 2 + 1))) | (4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) & (8)) == 0) { a2 = (unsigned int)(result * 2 + 1); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (8));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) & (4)) == 0) { a1 = (unsigned int)(a2); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) & (2)) == 0) { v_rbx = (unsigned int)(a1); }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), v_rsp - 95 - 25);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_00B6A59A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)))) & (32)) != 0) {
        v_rbx = (unsigned int)((v_rbx) | (32));
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 1) goto loc_00B6A5B4;
    goto loc_00B6A5BF;
loc_00B6A5B4:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) == 2) {
    }
    if ((*(unsigned int *)(a1 + 36)) == 0) goto loc_00B6A5DE;
    result = HalIsHyperThreadingEnabled(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), v_rsp - 95 - 25);
    v_r10 = 0;
    v_rbx = (unsigned int)(*(unsigned int *)(a1 + 164));
    if ((unsigned __int8)(result) == 0) {
        v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 164))) * (*(unsigned int *)(a1 + 160)));
    }
    v_rbx = (unsigned int)(-(v_rbx));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) - (1));
    *(unsigned int *)(a1 + 220) = (unsigned int)(v_rbx);
    if (((unsigned __int8)(result)) > 2) goto loc_00B6A616;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))) < 0x80000008ULL) goto loc_00B6A60A;
    a1 = 0;
    *(unsigned __int8 *)(v_rip + 2755304) = (unsigned __int8)((unsigned int)(0x80000008ULL));
    goto loc_00B6A616;
loc_00B6A60A:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) == 1) {
        *(unsigned __int8 *)(v_rip + 2755290) = 40;
    }
    result = (1) << ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 2755284)));
    result = (result) - (1);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(v_rip + 2755270) = result;
    *(unsigned __int64 *)(v_rip + 2755247) = result;
    if (((1) & ((unsigned __int8)(v_rsi))) != 0) {
    }
    result = (unsigned int)((v_rsi) & (0x10000000ULL));
    v_rbx = v_cr4;
    if (result == 0) { v_rbx = v_cr4; }
    if ((*(unsigned int *)(v_rip + 4572556)) != 0) {
    }
    a1 = v_rbx;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 4572398))) & (4)) == 0) { a1 = v_rbx; }
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rip + 4572398)) & (0x4000ULL));
    v_rbx = (a1) | ((unsigned int)(0x8000000ULL));
    if (a2 == 0) { v_rbx = a1; }
    if ((*(unsigned int *)(a1 + 36)) == 0) goto loc_00B6A6BC;
    if ((*(unsigned int *)(a1 + 36)) >= 0) goto loc_00B6A6BC;
    result = v_rbx;
    if ((*(unsigned __int8 *)(v_rip + 4572112)) != 0) {
        result = (v_rbx) | ((unsigned int)(0x20000ULL));
    }
    if ((*(unsigned int *)(v_rip + 4572458)) != 0) {
    }
    if ((((unsigned int)(0x20000ULL)) & (result)) != 0) {
        result = v_cr3;
        result = (result) | (2);
        v_cr3 = result;
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_00B6A717;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)))) < 7) goto loc_00B6A717;
    a1 = 0;
    if (condition_is_above_or_equal) goto loc_00B6A717;
    a1 = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) & ((unsigned __int8)(v_rbx))) != 0) {
        v_rsi = (v_rsi) | (16);
    }
    a3 = (v_rsi) | ((unsigned int)(0x20000ULL));
    if ((*(unsigned __int8 *)(v_rsp - 95 - 81)) == 0) { a3 = v_rsi; }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_00B6A7D3;
    a1 = 0;
    if (((0) & (32)) == 0) goto loc_00B6A82C;
    a2 = (a2) << (32);
    result = (1) | (a2);
    if (condition_is_greater_or_equal) goto loc_00B6A79A;
    a2 = (a2) << (32);
    a2 = (a2) | (result);
    if (!(condition_is_above_or_equal)) {
    }
    a1 = (condition_is_below) ? 1 : 0;
    result = (((1) & ((unsigned __int8)(a3))) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        result = HvlSetHardwareMbecAvailable(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    }
    if (((0) & (a2)) != 0) {
        result = HvlSetApicVirtualizationAvailable(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_rsi = (a3) | ((unsigned int)(0x8000000ULL));
    result = (unsigned __int8)((result) & (5));
    if (((unsigned __int8)(result)) != 5) { v_rsi = a3; }
    if ((((unsigned __int8)(result)) & (4)) != 0) {
    }
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_00B6A82C;
    goto loc_00B6A82C;
loc_00B6A7D3:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 1) goto loc_00B6A82C;
    a1 = 0;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) < 0x8000000AULL) goto loc_00B6A810;
    a1 = 0;
    if (((1) & ((unsigned __int8)(a2))) != 0) {
    }
    result = (unsigned int)(0x8000000AULL);
    if ((((unsigned int)((unsigned int)(0x20000ULL))) & ((unsigned int)(a2))) != 0) {
        result = HvlSetHardwareMbecAvailable(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    }
    if (!(condition_is_above_or_equal)) {
        result = HvlSetApicVirtualizationAvailable(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    if ((((unsigned __int8)(result)) & (16)) == 0) {
        v_rsi = (v_rsi) | ((unsigned int)(0x8000000ULL));
    }
    if ((*(unsigned __int8 *)(a1 + 141)) != 2) goto loc_00B6A89C;
    a1 = 0;
    if ((((unsigned __int8)(a3)) & (4)) == 0) goto loc_00B6A89C;
    a2 = (a2) << (32);
    result = (7) | (a2);
    result = (result) & ((unsigned int)(0x40001ULL));
    if (result != ((unsigned int)(0x40001ULL))) goto loc_00B6A89C;
    a1 = 0;
    if (((1) & (18)) == 0) goto loc_00B6A89C;
    v_rsi = (v_rsi) | (0);
    result = 18;
    if (((18) & (2)) != 0) {
        v_rsi = (v_rsi) | (18);
        result = *(unsigned __int64 *)(v_rip + 4564851);
    }
    result = KiApplyProcessorErrata(0, a2, a3, *(unsigned __int8 *)(a1 + 141));
    result = KiInitializeHresetSupport(0, a2, a3, *(unsigned __int8 *)(a1 + 141));
    *(unsigned __int64 *)(a1 + 36768) = v_rsi;
    *(unsigned __int64 *)(v_rip + 4574364) = v_rip + 4574110;
    *(unsigned __int64 *)(v_rip + 4574093) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4574338) = 128;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    return result;
loc_00B6A904:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 36)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 4571663);
        a1 = 0;
        result = KdInitSystem(a1, a2, a3, *(unsigned __int8 *)(a1 + 141));
    }
    v_stack_mA0 = (unsigned int)(*(unsigned int *)(v_rip + 3825950));
    result = KeBugCheckEx(93, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)), (unsigned int)((unsigned int)((unsigned int)(0x8000000ULL))), (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiSetFeatureBits(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t v_cr3;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x2A06DA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    local_r10 = 0;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) - ((uint8_t)(local_r10 + 1)));
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    a3 = 0;
    if (((uint8_t)(result)) <= ((uint8_t)(local_r10 + 1))) { a3 = (uint32_t)(local_r10 + 1); }
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)(a3);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = v_xmm1;
    if ((*(uint32_t *)(arg1 + 0x24)) != 0) goto loc_00B6A1EB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_00B6A1BC;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) != 6) goto loc_00B6A20D;
    *(uint32_t *)(v_rip + 0x45CD88) = 477;
    *(uint32_t *)(v_rip + 0x45CD82) = 478;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x43))) > 45) goto loc_00B6A16B;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x43))) == 45) goto loc_00B6A13B;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x43))) > 31) goto loc_00B6A122;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x43))) == 31) goto loc_00B6A13B;
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0x43)) - (15));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - (8));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    goto loc_00B6A139;
loc_00B6A122:
    Arg1 = (uint32_t)((Arg1) - (37));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
loc_00B6A139:
    if (((uint32_t)(Arg1)) == 2) {
        *(uint32_t *)(v_rip + 0x45CBB7) = 0x680ULL;
        *(uint32_t *)(v_rip + 0x45CC09) = 0x6C0ULL;
    }
    if ((*(uint32_t *)(v_rip + 0x45CBA6)) == 0) goto loc_00B6A20D;
loc_00B6A15C:
    *(uint32_t *)(v_rip + 0x45CE66) = 457;
    goto loc_00B6A20D;
loc_00B6A16B:
    if (((uint32_t)(Arg1)) > 58) goto loc_00B6A18D;
    if (((uint32_t)(Arg1)) == 58) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - (46));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B6A1A6;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A1A6;
    if (((uint32_t)(Arg1)) == ((uint32_t)(local_r10 + 1))) goto loc_00B6A1A6;
    goto loc_00B6A14F;
loc_00B6A18D:
    Arg1 = (uint32_t)((Arg1) - (60));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B6A13B;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10 + 1)));
    if (condition_is_equal) goto loc_00B6A13B;
    if (((uint32_t)(Arg1)) != 7) goto loc_00B6A14F;
loc_00B6A1A6:
    *(uint32_t *)(v_rip + 0x45CB4C) = 64;
    *(uint32_t *)(v_rip + 0x45CB9E) = 96;
    goto loc_00B6A15C;
loc_00B6A1BC:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != ((uint8_t)(local_r10 + 1))) goto loc_00B6A20D;
    *(uint32_t *)(v_rip + 0x45CB31) = 475;
    *(uint32_t *)(v_rip + 0x45CB83) = 476;
    *(uint32_t *)(v_rip + 0x45CC81) = 477;
    *(uint32_t *)(v_rip + 0x45CC7B) = 478;
    goto loc_00B6A20D;
loc_00B6A1EB:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    Arg1 = 0;
    result = KiGetProcessorSignature(Arg1, a2, a3, a4);
    result = KiSetProcessorSignature(0, (uint32_t)((uint32_t)(result)), a3, a4);
    local_r10 = 0;
loc_00B6A20D:
    result = 0;
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x5) = (uint32_t)(*(uint8_t *)(arg1 + 0x40));
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x3) = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_00B6A24F;
    result = 0;
    a2 = 0;
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 1;
    *(uint32_t *)(local_rsp - 0x5F - 0x5) = (uint32_t)(*(uint8_t *)(arg1 + 0x40));
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x3) = 0;
    goto loc_00B6A254;
loc_00B6A24F:
    result = 1;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) == 1) {
        Arg1 = 139;
        a2 = (a2) << (32);
        result = (1) | (a2);
        *(uint64_t *)(arg1 + 0x8FA8) = result;
    }
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = 1;
    *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 0;
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x1B) = (uint32_t)(*(uint8_t *)(arg1 + 0x40));
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)((uint32_t)(0x80000000ULL));
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x23) = (uint32_t)((uint32_t)((uint32_t)(a2)));
    *(uint32_t *)(local_rsp - 0x5F + 0xF) = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x7) = (uint32_t)((uint32_t)(0x80000001ULL));
    *(uint32_t *)(local_rsp - 0x5F + 0xB) = (uint32_t)(*(uint8_t *)(arg1 + 0x40));
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)(a2);
    if ((*(uint32_t *)(arg1 + 0x24)) != 0) goto loc_00B6A370;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 1) goto loc_00B6A30B;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) != 15) goto loc_00B6A2E0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) == 107) goto loc_00B6A2D2;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) != 104) goto loc_00B6A30B;
loc_00B6A2D2:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) != 1) goto loc_00B6A30B;
    goto loc_00B6A30B;
loc_00B6A2E0:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) != 16) goto loc_00B6A30B;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x43)) != 0) goto loc_00B6A2EE;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) <= 2) goto loc_00B6A303;
loc_00B6A2EE:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) != 2) goto loc_00B6A2FB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) <= ((uint8_t)(*(uint8_t *)(arg1 + 0x43)))) goto loc_00B6A303;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) == 10) goto loc_00B6A303;
loc_00B6A2FB:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) != 4) goto loc_00B6A30B;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x42)) == 0) {
    }
    if ((*(uint32_t *)(arg1 + 0x24)) != 0) goto loc_00B6A370;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 1) goto loc_00B6A32B;
    if ((*(uint8_t *)(arg1 + 0x40)) != 23) goto loc_00B6A370;
    *(uint32_t *)(v_rip + 0x2FC607) = 1;
    goto loc_00B6A370;
loc_00B6A32B:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_00B6A370;
    if ((*(uint8_t *)(arg1 + 0x40)) != 6) goto loc_00B6A370;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) > 54) goto loc_00B6A34E;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) < 54) goto loc_00B6A366;
loc_00B6A34E:
    Arg1 = (uint8_t)((*(uint8_t *)(arg1 + 0x43)) - (55));
    if (((uint8_t)(Arg1)) > 22) goto loc_00B6A370;
    if (((uint8_t)(Arg1)) >= 22) goto loc_00B6A370;
    if ((*(uint8_t *)(arg1 + 0x42)) <= 7) {
        *(uint32_t *)(v_rip + 0x2FC5C0) = 2;
    }
    result = KiDetectKvaLeakage(Arg1, *(uint8_t *)(arg1 + 0x40), *(uint8_t *)(arg1 + 0x8D), 1);
    if ((*(uint8_t *)(arg1 + 0x8D)) == 1) {
        *(uint32_t *)(local_rsp - 0x5F + 0x13) = (uint32_t)((uint32_t)((uint32_t)(a2)));
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x40)))))) >> (24));
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)(result);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x40)))) >> (5));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(a2))))) & ((uint32_t)((uint32_t)(0x789F3FDULL))));
    local_rsi = (uint32_t)((local_rsi) & (0x7F8ULL));
    *(uint32_t *)(arg1 + 0xE8) = (uint32_t)(local_rsi);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x789F3FDULL)))) goto loc_00B6A904;
    if (((1) & (0)) == 0) goto loc_00B6A904;
    if ((*(uint32_t *)(v_rip + 0x3A664C)) != 0) goto loc_00B6A904;
    local_rsi = (*(uint64_t *)(arg1 + 0x8FA0)) | (0x20113DFEULL);
    if (!(condition_is_above_or_equal)) {
        result = *(uint8_t *)(arg1 + 0xD1);
        Arg1 = 0xC0000103ULL;
        a2 = *(uint8_t *)(arg1 + 0xD0);
        a2 = (a2) << (8);
        a2 = (a2) | (result);
        result = a2;
        a2 = (a2) >> (32);
    }
    result = 0;
    a2 = 0;
    if (!(condition_is_above_or_equal)) {
        Arg1 = 0xC0000080ULL;
        a2 = (a2) << (32);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    *(uint32_t *)(arg1 + 0xA0) = 1;
    *(uint32_t *)(arg1 + 0xA4) = 1;
    *(uint32_t *)(arg1 + 0x9EC8) = 1;
    *(uint32_t *)(arg1 + 0x9ECC) = 1;
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(Arg1, a2, *(uint8_t *)(arg1 + 0x8D), 1);
    if ((uint32_t)(result) != 0) {
        *(uint32_t *)(arg1 + 0xBB48) = 1;
    }
    v_stack_mC0 = local_rsp - 95 - 73;
    v_stack_mC8 = local_rsp - 95 - 41;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm1;
    result = KiComputeTopologyConstants(*(uint8_t *)(arg1 + 0x8D), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), local_rsp - 95 - 25);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) & (16)) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x31);
        *(uint32_t *)(arg1 + 0xD4) = (uint32_t)(result);
    }
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))))) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x41);
        *(uint32_t *)(arg1 + 0xA4) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) & (8)) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x35);
        *(uint32_t *)(arg1 + 0x9ECC) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) & (2)) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x3D);
        *(uint32_t *)(arg1 + 0xA0) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) & (4)) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x39);
        *(uint32_t *)(arg1 + 0x9EC8) = (uint32_t)(result);
    }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(*(uint8_t *)(arg1 + 0x8D), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), local_rsp - 95 - 25);
    if ((uint32_t)(result) == 0) goto loc_00B6A538;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) & (32)) != 0) {
        result = *(uint32_t *)(local_rsp - 0x5F - 0x2D);
        *(uint32_t *)(arg1 + 0xBB48) = (uint32_t)(result);
    }
    *(uint8_t *)(arg1 + 0x8F) = (uint8_t)(*(uint8_t *)(arg1 + 0xA4));
    *(uint8_t *)(arg1 + 0x8E) = (uint8_t)(*(uint8_t *)(arg1 + 0xA0));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) & (1));
    a2 = (uint32_t)(((uint32_t)((uint32_t)(result * 2 + 1))) | (4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) & (8)) == 0) { a2 = (uint32_t)(result * 2 + 1); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a2))) | (8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) & (4)) == 0) { Arg1 = (uint32_t)(a2); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (16));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) & (2)) == 0) { local_rbx = (uint32_t)(Arg1); }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), local_rsp - 95 - 25);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_00B6A59A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)))) & (32)) != 0) {
        local_rbx = (uint32_t)((local_rbx) | (32));
    }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 1) goto loc_00B6A5B4;
    goto loc_00B6A5BF;
loc_00B6A5B4:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) == 2) {
    }
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) goto loc_00B6A5DE;
    result = HalIsHyperThreadingEnabled(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), local_rsp - 95 - 25);
    local_r10 = 0;
    local_rbx = (uint32_t)(*(uint32_t *)(arg1 + 0xA4));
    if ((uint8_t)(result) == 0) {
        local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA4))) * (*(uint32_t *)(arg1 + 0xA0)));
    }
    local_rbx = (uint32_t)(-(local_rbx));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) - (1));
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)(local_rbx);
    if (((uint8_t)(result)) > 2) goto loc_00B6A616;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))) < 0x80000008ULL) goto loc_00B6A60A;
    Arg1 = 0;
    *(uint8_t *)(v_rip + 0x2A0AE8) = (uint8_t)((uint32_t)(0x80000008ULL));
    goto loc_00B6A616;
loc_00B6A60A:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) == 1) {
        *(uint8_t *)(v_rip + 0x2A0ADA) = 40;
    }
    result = (1) << ((uint8_t)(*(uint8_t *)(v_rip + 0x2A0AD4)));
    result = (result) - (1);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(v_rip + 0x2A0AC6) = result;
    *(uint64_t *)(v_rip + 0x2A0AAF) = result;
    if (((1) & ((uint8_t)(local_rsi))) != 0) {
    }
    result = (uint32_t)((local_rsi) & (0x10000000ULL));
    local_rbx = v_cr4;
    if (result == 0) { local_rbx = v_cr4; }
    if ((*(uint32_t *)(v_rip + 0x45C58C)) != 0) {
    }
    Arg1 = local_rbx;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x45C4EE))) & (4)) == 0) { Arg1 = local_rbx; }
    a2 = (uint32_t)((*(uint64_t *)(v_rip + 0x45C4EE)) & (0x4000ULL));
    local_rbx = (Arg1) | ((uint32_t)(0x8000000ULL));
    if (a2 == 0) { local_rbx = Arg1; }
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) goto loc_00B6A6BC;
    if ((*(uint32_t *)(arg1 + 0x24)) >= 0) goto loc_00B6A6BC;
    result = local_rbx;
    if ((*(uint8_t *)(v_rip + 0x45C3D0)) != 0) {
        result = (local_rbx) | ((uint32_t)(0x20000ULL));
    }
    if ((*(uint32_t *)(v_rip + 0x45C52A)) != 0) {
    }
    if ((((uint32_t)(0x20000ULL)) & (result)) != 0) {
        result = v_cr3;
        result = (result) | (2);
        v_cr3 = result;
    }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_00B6A717;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)))) < 7) goto loc_00B6A717;
    Arg1 = 0;
    if (condition_is_above_or_equal) goto loc_00B6A717;
    Arg1 = 0;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) & ((uint8_t)(local_rbx))) != 0) {
        local_rsi = (local_rsi) | (16);
    }
    a3 = (local_rsi) | ((uint32_t)(0x20000ULL));
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x51)) == 0) { a3 = local_rsi; }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_00B6A7D3;
    Arg1 = 0;
    if (((0) & (32)) == 0) goto loc_00B6A82C;
    a2 = (a2) << (32);
    result = (1) | (a2);
    if (condition_is_greater_or_equal) goto loc_00B6A79A;
    a2 = (a2) << (32);
    a2 = (a2) | (result);
    if (!(condition_is_above_or_equal)) {
    }
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (((1) & ((uint8_t)(a3))) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        result = HvlSetHardwareMbecAvailable(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    }
    if (((0) & (a2)) != 0) {
        result = HvlSetApicVirtualizationAvailable(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    local_rsi = (a3) | ((uint32_t)(0x8000000ULL));
    result = (uint8_t)((result) & (5));
    if (((uint8_t)(result)) != 5) { local_rsi = a3; }
    if ((((uint8_t)(result)) & (4)) != 0) {
    }
    if (((1) & ((uint8_t)(result))) == 0) goto loc_00B6A82C;
    goto loc_00B6A82C;
loc_00B6A7D3:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 1) goto loc_00B6A82C;
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) < 0x8000000AULL) goto loc_00B6A810;
    Arg1 = 0;
    if (((1) & ((uint8_t)(a2))) != 0) {
    }
    result = (uint32_t)(0x8000000AULL);
    if ((((uint32_t)((uint32_t)(0x20000ULL))) & ((uint32_t)(a2))) != 0) {
        result = HvlSetHardwareMbecAvailable(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    }
    if (!(condition_is_above_or_equal)) {
        result = HvlSetApicVirtualizationAvailable(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    if ((((uint8_t)(result)) & (16)) == 0) {
        local_rsi = (local_rsi) | ((uint32_t)(0x8000000ULL));
    }
    if ((*(uint8_t *)(arg1 + 0x8D)) != 2) goto loc_00B6A89C;
    Arg1 = 0;
    if ((((uint8_t)(a3)) & (4)) == 0) goto loc_00B6A89C;
    a2 = (a2) << (32);
    result = (7) | (a2);
    result = (result) & ((uint32_t)(0x40001ULL));
    if (result != ((uint32_t)(0x40001ULL))) goto loc_00B6A89C;
    Arg1 = 0;
    if (((1) & (18)) == 0) goto loc_00B6A89C;
    local_rsi = (local_rsi) | (0);
    result = 18;
    if (((18) & (2)) != 0) {
        local_rsi = (local_rsi) | (18);
        result = *(uint64_t *)(v_rip + 0x45A773);
    }
    result = KiApplyProcessorErrata(0, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    result = KiInitializeHresetSupport(0, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    *(uint64_t *)(arg1 + 0x8FA0) = local_rsi;
    *(uint64_t *)(v_rip + 0x45CC9C) = v_rip + 4574110;
    *(uint64_t *)(v_rip + 0x45CB8D) = v_xmm0;
    *(uint64_t *)(v_rip + 0x45CC82) = 128;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    return result;
loc_00B6A904:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x24)) == 0) {
        a2 = *(uint64_t *)(v_rip + 0x45C20F);
        Arg1 = 0;
        result = KdInitSystem(Arg1, a2, a3, *(uint8_t *)(arg1 + 0x8D));
    }
    v_stack_mA0 = (uint32_t)(*(uint32_t *)(v_rip + 0x3A611E));
    result = KeBugCheckEx(93, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)), (uint32_t)((uint32_t)((uint32_t)(0x8000000ULL))), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg1` | `+ 0x42` | `8` | `R` |
| `Arg1` | `+ 0x43` | `8` | `R` |
| `Arg1` | `+ 0x8D` | `8` | `R` |
| `Arg1` | `+ 0x8E` | `8` | `W` |
| `Arg1` | `+ 0x8F` | `8` | `W` |
| `Arg1` | `+ 0xA0` | `8` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `W` |
| `Arg1` | `+ 0xA4` | `8` | `R` |
| `Arg1` | `+ 0xA4` | `32` | `R` |
| `Arg1` | `+ 0xA4` | `32` | `W` |
| `Arg1` | `+ 0xD0` | `8` | `R` |
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `W` |
| `Arg1` | `+ 0xDC` | `32` | `W` |
| `Arg1` | `+ 0xE8` | `32` | `W` |
| `Arg1` | `+ 0x8FA0` | `64` | `R` |
| `Arg1` | `+ 0x8FA0` | `64` | `W` |
| `Arg1` | `+ 0x8FA8` | `64` | `W` |
| `Arg1` | `+ 0x9EC8` | `32` | `W` |
| `Arg1` | `+ 0x9ECC` | `32` | `W` |
| `Arg1` | `+ 0xBB48` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B6A03C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
