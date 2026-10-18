# EtwpEnableKernelTrace

- RVA: `0x00A4FBCC`–`0x00A501B3` (길이 `1,511` bytes)
- VA: `0x0000000140A4FBCC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B0978`
- 디코드: `351`개 명령, `1,511/1,511` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **42**

### Outgoing calls
- `0x00A4FC79` → [EtwpUpdateFileInfoDriverState](../A5/EtwpUpdateFileInfoDriverState_function_00A501BC.md) (function, `0x00A501BC`)
- `0x00A4FE98` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A4FEBE` → [IoPerfInit](../../text/4D/IoPerfInit_function_004DC338.md) (function, `0x004DC338`)
- `0x00A4FF0B` → [EtwpDisableKernelTrace](EtwpDisableKernelTrace_function_00A4F7D8.md) (function, `0x00A4F7D8`)
- `0x00A4FF1E` → [DbgSetDebugPrintCallback](../../text/4F/DbgSetDebugPrintCallback_function_004FC110.md) (function, `0x004FC110`)
- `0x00A4FF35` → [EtwpTimeProfileStart](../6F/EtwpTimeProfileStart_function_006FF5E0.md) (function, `0x006FF5E0`)
- `0x00A4FFCA` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x00A5013A` → [AlpcRegisterLogRoutine](../74/AlpcRegisterLogRoutine_function_0074CE5C.md) (function, `0x0074CE5C`)
- `0x00A50163` → [WmiSetNetworkNotify](../7B/WmiSetNetworkNotify_function_007B3EE4.md) (function, `0x007B3EE4`)
- `0x00A50194` → [ObEnableEtwReferenceTrace](../74/ObEnableEtwReferenceTrace_function_0074F434.md) (function, `0x0074F434`)

### Direct callers
- [EtwpUpdateGlobalGroupMasks](EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) at `0x00A4F707`
- [EtwpFixBootLoggers](../../init/C4/EtwpFixBootLoggers_function_00C4F09C.md) at `0x00C4F1E7`

### Static image references
- `0x00A4FBE8` → RVA `0x00E0A740` (`.data`; read)
- `0x00A4FBFC` → RVA `0x00EFF284` (`.data`; read)
- `0x00A4FCAC` → RVA `0x00223BB0` (`EtwpTraceFileIo`; read)
- `0x00A4FD59` → RVA `0x00650D50` (`EtwpTraceFltIo`; read)
- `0x00A4FD89` → RVA `0x00650DB0` (`EtwpTraceFltTimedIo`; read)
- `0x00A4FDBB` → RVA `0x004A5BB0` (`EtwpTraceWdf`; read)
- `0x00A4FF17` → RVA `0x00650CA0` (`EtwpTraceDebugPrint`; read)
- `0x00A4FF4D` → RVA `0x00862980` (`EtwpTraceRegistry`; read)
- `0x00A4FF56` → RVA `0x00FD8008` (`PAGEDATA`; write)
- `0x00A4FF60` → RVA `0x00AC1DB0` (`EtwpTraceRegistryTransaction`; read)
- `0x00A4FF6A` → RVA `0x00FD81D0` (`PAGEDATA`; write)
- `0x00A4FF76` → RVA `0x00FC7538` (`ALMOSTRO`; read)
- `0x00A4FFA3` → RVA `0x00E0EB2C` (`.data`; read)
- `0x00A4FFB1` → RVA `0x00EFF3C0` (`.data`; read)
- `0x00A4FFDF` → RVA `0x00E036A0` (`.data`; write)
- `0x00A4FFF0` → RVA `0x00E03698` (`.data`; write)
- `0x00A4FFFF` → RVA `0x002251F0` (`EtwpTraceFileName`; read)
- `0x00A50008` → RVA `0x00E03690` (`.data`; write)
- `0x00A50017` → RVA `0x00224400` (`EtwpTraceIo`; read)
- `0x00A50020` → RVA `0x00E684A8` (`.data`; write)
- `0x00A50027` → RVA `0x00651190` (`EtwpTraceRedirectedIo`; read)
- `0x00A5002E` → RVA `0x00E036D0` (`.data`; write)
- `0x00A5003D` → RVA `0x002241C0` (`EtwpTraceIoInit`; read)
- `0x00A50047` → RVA `0x00E684B0` (`.data`; write)
- `0x00A5005A` → RVA `0x00650DF0` (`EtwpTraceOpticalIo`; read)
- `0x00A50065` → RVA `0x00E684B8` (`.data`; write)
- `0x00A50075` → RVA `0x006510A0` (`EtwpTraceOpticalIoInit`; read)
- `0x00A50080` → RVA `0x00E684C0` (`.data`; write)
- `0x00A50090` → RVA `0x00651230` (`EtwpTraceSplitIo`; read)
- `0x00A5009A` → RVA `0x00E68498` (`.data`; write)
- `0x00A500AC` → RVA `0x00E036B0` (`.data`; write)
- `0x00A500BF` → RVA `0x00E036B8` (`.data`; write)
- `0x00A500D2` → RVA `0x00E036C0` (`.data`; write)
- `0x00A500E5` → RVA `0x00E036C8` (`.data`; write)
- `0x00A500F8` → RVA `0x00E0EB40` (`.data`; write)
- `0x00A5010B` → RVA `0x00E0EB48` (`.data`; write)
- `0x00A5011E` → RVA `0x00650B40` (`EtwpSystemTraceWdf`; read)
- `0x00A50125` → RVA `0x00E0EB50` (`.data`; write)
- `0x00A50155` → RVA `0x002356F0` (`EtwpTraceNetwork`; read)
- `0x00A5015C` → RVA `0x00E684C8` (`.data`; write)
- `0x00A50183` → RVA `0x00EFF290` (`.data`; read)
- `0x00A501A7` → RVA `0x00E68468` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00A4FE98` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A4FEBE` → [IoPerfInit](../../text/4D/IoPerfInit_function_004DC338.md) (`PAGE` → `.text`)
  - `0x00A4FF1E` → [DbgSetDebugPrintCallback](../../text/4F/DbgSetDebugPrintCallback_function_004FC110.md) (`PAGE` → `.text`)
  - `0x00A4FFCA` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00A4FF86` → [sub_00B3C5BA](../B3/Unknown_function_00B3C5BA.md) (`tail-transfer`)
  - `0x00A50189` → [sub_00B3C5BA + 0x16](../B3/Unknown_function_00B3C5BA.md) (`tail-transfer`)
  - `0x00A5018F` → [sub_00B3C5BA + 0x35](../B3/Unknown_function_00B3C5BA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A4FBCC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A4FBD1  55                              push rbp
00A4FBD2  56                              push rsi
00A4FBD3  57                              push rdi
00A4FBD4  41 54                           push r12
00A4FBD6  41 55                           push r13
00A4FBD8  41 56                           push r14
00A4FBDA  41 57                           push r15
00A4FBDC  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00A4FBE1  48 81 EC 90 00 00 00            sub rsp, 0x90
00A4FBE8  48 8B 05 51 AB 3B 00            mov rax, qword ptr [rip + 0x3bab51]
00A4FBEF  48 33 C4                        xor rax, rsp
00A4FBF2  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00A4FBF6  33 F6                           xor esi, esi
00A4FBF8  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
00A4FBFC  40 38 35 81 F6 4A 00            cmp byte ptr [rip + 0x4af681], sil
00A4FC03  0F 57 C0                        xorps xmm0, xmm0
00A4FC06  45 8B D1                        mov r10d, r9d
00A4FC09  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
00A4FC0D  4D 8B C8                        mov r9, r8
00A4FC10  48 8B DA                        mov rbx, rdx
00A4FC13  44 8D 6E 08                     lea r13d, [rsi + 8]
00A4FC17  4C 8B E1                        mov r12, rcx
00A4FC1A  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00A4FC1E  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00A4FC22  0F 84 4E 03 00 00               je 0x140a4ff76
00A4FC28  44 8B 7D E3                     mov r15d, dword ptr [rbp - 0x1d]
00A4FC2C  B9 00 00 08 00                  mov ecx, 0x80000
00A4FC31  48 85 DB                        test rbx, rbx
00A4FC34  74 29                           je 0x140a4fc5f
00A4FC36  85 4B 04                        test dword ptr [rbx + 4], ecx
00A4FC39  0F 85 4C 03 00 00               jne 0x140a4ff8b
00A4FC3F  B9 00 00 80 00                  mov ecx, 0x800000
00A4FC44  85 4B 04                        test dword ptr [rbx + 4], ecx
00A4FC47  0F 85 4A 03 00 00               jne 0x140a4ff97
00A4FC4D  48 85 DB                        test rbx, rbx
00A4FC50  74 0D                           je 0x140a4fc5f
00A4FC52  F7 43 04 00 00 88 00            test dword ptr [rbx + 4], 0x880000
00A4FC59  0F 85 44 03 00 00               jne 0x140a4ffa3
00A4FC5F  80 3D 1E F6 4A 00 03            cmp byte ptr [rip + 0x4af61e], 3
00A4FC66  76 20                           jbe 0x140a4fc88
00A4FC68  41 B8 01 00 00 00               mov r8d, 1
00A4FC6E  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
00A4FC73  48 8B D3                        mov rdx, rbx
00A4FC76  49 8B CC                        mov rcx, r12
00A4FC79  E8 3E 05 00 00                  call 0x140a501bc
00A4FC7E  8B F0                           mov esi, eax
00A4FC80  85 C0                           test eax, eax
00A4FC82  0F 85 03 02 00 00               jne 0x140a4fe8b
00A4FC88  8B 7D DF                        mov edi, dword ptr [rbp - 0x21]
00A4FC8B  41 BB 00 00 02 00               mov r11d, 0x20000
00A4FC91  41 BA 00 00 10 00               mov r10d, 0x100000
00A4FC97  41 B8 00 04 00 00               mov r8d, 0x400
00A4FC9D  48 85 DB                        test rbx, rbx
00A4FCA0  0F 84 8B 04 00 00               je 0x140a50131
00A4FCA6  41 B9 00 00 00 02               mov r9d, 0x2000000
00A4FCAC  48 8D 15 FD 3E 7D FF            lea rdx, [rip - 0x82c103]
00A4FCB3  44 85 0B                        test dword ptr [rbx], r9d
00A4FCB6  0F 85 20 03 00 00               jne 0x140a4ffdc
00A4FCBC  B9 00 00 00 04                  mov ecx, 0x4000000
00A4FCC1  85 0B                           test dword ptr [rbx], ecx
00A4FCC3  0F 85 25 03 00 00               jne 0x140a4ffee
00A4FCC9  48 85 DB                        test rbx, rbx
00A4FCCC  0F 84 5F 04 00 00               je 0x140a50131
00A4FCD2  B9 00 02 00 00                  mov ecx, 0x200
00A4FCD7  85 0B                           test dword ptr [rbx], ecx
00A4FCD9  0F 85 20 03 00 00               jne 0x140a4ffff
00A4FCDF  48 85 DB                        test rbx, rbx
00A4FCE2  0F 84 49 04 00 00               je 0x140a50131
00A4FCE8  B9 00 01 00 00                  mov ecx, 0x100
00A4FCED  85 0B                           test dword ptr [rbx], ecx
00A4FCEF  0F 85 22 03 00 00               jne 0x140a50017
00A4FCF5  48 85 DB                        test rbx, rbx
00A4FCF8  0F 84 33 04 00 00               je 0x140a50131
00A4FCFE  44 85 03                        test dword ptr [rbx], r8d
00A4FD01  0F 85 36 03 00 00               jne 0x140a5003d
00A4FD07  48 85 DB                        test rbx, rbx
00A4FD0A  0F 84 21 04 00 00               je 0x140a50131
00A4FD10  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A4FD13  A8 01                           test al, 1
00A4FD15  0F 85 3B 03 00 00               jne 0x140a50056
00A4FD1B  48 85 DB                        test rbx, rbx
00A4FD1E  0F 84 0D 04 00 00               je 0x140a50131
00A4FD24  44 8B 75 EF                     mov r14d, dword ptr [rbp - 0x11]
00A4FD28  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A4FD2B  A8 02                           test al, 2
00A4FD2D  0F 85 42 03 00 00               jne 0x140a50075
00A4FD33  48 85 DB                        test rbx, rbx
00A4FD36  0F 84 4F 01 00 00               je 0x140a4fe8b
00A4FD3C  41 B8 00 00 20 00               mov r8d, 0x200000
00A4FD42  44 85 03                        test dword ptr [rbx], r8d
00A4FD45  0F 85 45 03 00 00               jne 0x140a50090
00A4FD4B  48 85 DB                        test rbx, rbx
00A4FD4E  0F 84 37 01 00 00               je 0x140a4fe8b
00A4FD54  B9 00 00 40 00                  mov ecx, 0x400000
00A4FD59  48 8D 15 F0 0F C0 FF            lea rdx, [rip - 0x3ff010]
00A4FD60  85 4B 10                        test dword ptr [rbx + 0x10], ecx
00A4FD63  0F 85 40 03 00 00               jne 0x140a500a9
00A4FD69  48 85 DB                        test rbx, rbx
00A4FD6C  0F 84 19 01 00 00               je 0x140a4fe8b
00A4FD72  B9 00 00 08 00                  mov ecx, 0x80000
00A4FD77  85 4B 10                        test dword ptr [rbx + 0x10], ecx
00A4FD7A  0F 85 3C 03 00 00               jne 0x140a500bc
00A4FD80  48 85 DB                        test rbx, rbx
00A4FD83  0F 84 02 01 00 00               je 0x140a4fe8b
00A4FD89  48 8D 0D 20 10 C0 FF            lea rcx, [rip - 0x3fefe0]
00A4FD90  44 85 53 10                     test dword ptr [rbx + 0x10], r10d
00A4FD94  0F 85 35 03 00 00               jne 0x140a500cf
00A4FD9A  48 85 DB                        test rbx, rbx
00A4FD9D  0F 84 E8 00 00 00               je 0x140a4fe8b
00A4FDA3  44 85 43 10                     test dword ptr [rbx + 0x10], r8d
00A4FDA7  0F 85 35 03 00 00               jne 0x140a500e2
00A4FDAD  48 85 DB                        test rbx, rbx
00A4FDB0  0F 84 D5 00 00 00               je 0x140a4fe8b
00A4FDB6  B9 00 00 00 01                  mov ecx, 0x1000000
00A4FDBB  48 8D 15 EE 5D A5 FF            lea rdx, [rip - 0x5aa212]
00A4FDC2  85 4B 10                        test dword ptr [rbx + 0x10], ecx
00A4FDC5  0F 85 2A 03 00 00               jne 0x140a500f5
00A4FDCB  48 85 DB                        test rbx, rbx
00A4FDCE  0F 84 B7 00 00 00               je 0x140a4fe8b
00A4FDD4  44 85 4B 10                     test dword ptr [rbx + 0x10], r9d
00A4FDD8  0F 85 2A 03 00 00               jne 0x140a50108
00A4FDDE  48 85 DB                        test rbx, rbx
00A4FDE1  0F 84 A4 00 00 00               je 0x140a4fe8b
00A4FDE7  B9 00 00 00 08                  mov ecx, 0x8000000
00A4FDEC  85 4B 08                        test dword ptr [rbx + 8], ecx
00A4FDEF  0F 85 26 03 00 00               jne 0x140a5011b
00A4FDF5  48 85 DB                        test rbx, rbx
00A4FDF8  0F 84 8D 00 00 00               je 0x140a4fe8b
00A4FDFE  44 85 1B                        test dword ptr [rbx], r11d
00A4FE01  0F 85 46 01 00 00               jne 0x140a4ff4d
00A4FE07  48 85 DB                        test rbx, rbx
00A4FE0A  74 7F                           je 0x140a4fe8b
00A4FE0C  44 85 13                        test dword ptr [rbx], r10d
00A4FE0F  0F 85 25 03 00 00               jne 0x140a5013a
00A4FE15  48 85 DB                        test rbx, rbx
00A4FE18  74 71                           je 0x140a4fe8b
00A4FE1A  F7 03 00 00 01 00               test dword ptr [rbx], 0x10000
00A4FE20  0F 85 2F 03 00 00               jne 0x140a50155
00A4FE26  48 85 DB                        test rbx, rbx
00A4FE29  74 60                           je 0x140a4fe8b
00A4FE2B  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A4FE2E  A8 10                           test al, 0x10
00A4FE30  0F 85 83 00 00 00               jne 0x140a4feb9
00A4FE36  48 85 DB                        test rbx, rbx
00A4FE39  74 50                           je 0x140a4fe8b
00A4FE3B  F7 03 00 00 04 00               test dword ptr [rbx], 0x40000
00A4FE41  0F 85 CE 00 00 00               jne 0x140a4ff15
00A4FE47  48 85 DB                        test rbx, rbx
00A4FE4A  74 3F                           je 0x140a4fe8b
00A4FE4C  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A4FE4F  A8 02                           test al, 2
00A4FE51  0F 85 DE 00 00 00               jne 0x140a4ff35
00A4FE57  48 85 DB                        test rbx, rbx
00A4FE5A  74 2F                           je 0x140a4fe8b
00A4FE5C  F7 43 04 00 04 00 00            test dword ptr [rbx + 4], 0x400
00A4FE63  0F 85 18 03 00 00               jne 0x140a50181
00A4FE69  48 85 DB                        test rbx, rbx
00A4FE6C  74 1D                           je 0x140a4fe8b
00A4FE6E  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A4FE71  84 C0                           test al, al
00A4FE73  0F 88 1B 03 00 00               js 0x140a50194
00A4FE79  48 85 DB                        test rbx, rbx
00A4FE7C  74 0D                           je 0x140a4fe8b
00A4FE7E  F7 43 04 00 00 02 00            test dword ptr [rbx + 4], 0x20000
00A4FE85  0F 85 1C 03 00 00               jne 0x140a501a7
00A4FE8B  85 F6                           test esi, esi
00A4FE8D  78 3E                           js 0x140a4fecd
00A4FE8F  8B C6                           mov eax, esi
00A4FE91  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00A4FE95  48 33 CC                        xor rcx, rsp
00A4FE98  E8 A3 C7 C5 FF                  call 0x1406ac640
00A4FE9D  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A4FEA5  48 81 C4 90 00 00 00            add rsp, 0x90
00A4FEAC  41 5F                           pop r15
00A4FEAE  41 5E                           pop r14
00A4FEB0  41 5D                           pop r13
00A4FEB2  41 5C                           pop r12
00A4FEB4  5F                              pop rdi
00A4FEB5  5E                              pop rsi
00A4FEB6  5D                              pop rbp
00A4FEB7  C3                              ret
00A4FEB8  CC                              int3
00A4FEB9  B9 01 00 00 00                  mov ecx, 1
00A4FEBE  E8 75 C4 A8 FF                  call 0x1404dc338
00A4FEC3  8B F0                           mov esi, eax
00A4FEC5  85 C0                           test eax, eax
00A4FEC7  0F 89 A7 02 00 00               jns 0x140a50174
00A4FECD  0F 57 C0                        xorps xmm0, xmm0
00A4FED0  48 8D 4D FF                     lea rcx, [rbp - 1]
00A4FED4  49 2B DC                        sub rbx, r12
00A4FED7  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A4FEDB  49 2B CC                        sub rcx, r12
00A4FEDE  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
00A4FEE2  42 8B 04 23                     mov eax, dword ptr [rbx + r12]
00A4FEE6  F7 D0                           not eax
00A4FEE8  41 23 04 24                     and eax, dword ptr [r12]
00A4FEEC  42 89 04 21                     mov dword ptr [rcx + r12], eax
00A4FEF0  4D 8D 64 24 04                  lea r12, [r12 + 4]
00A4FEF5  49 83 ED 01                     sub r13, 1
00A4FEF9  75 E7                           jne 0x140a4fee2
00A4FEFB  44 8B 4D C7                     mov r9d, dword ptr [rbp - 0x39]
00A4FEFF  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00A4FF03  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00A4FF07  48 8D 4D FF                     lea rcx, [rbp - 1]
00A4FF0B  E8 C8 F8 FF FF                  call 0x140a4f7d8
00A4FF10  E9 7A FF FF FF                  jmp 0x140a4fe8f
00A4FF15  B2 01                           mov dl, 1
00A4FF17  48 8D 0D 82 0D C0 FF            lea rcx, [rip - 0x3ff27e]
00A4FF1E  E8 ED C1 AA FF                  call 0x1404fc110
00A4FF23  8B F0                           mov esi, eax
00A4FF25  85 C0                           test eax, eax
00A4FF27  78 A4                           js 0x140a4fecd
00A4FF29  0F BA EF 12                     bts edi, 0x12
00A4FF2D  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A4FF30  E9 17 FF FF FF                  jmp 0x140a4fe4c
00A4FF35  E8 A6 F6 CA FF                  call 0x1406ff5e0
00A4FF3A  8B F0                           mov esi, eax
00A4FF3C  85 C0                           test eax, eax
00A4FF3E  78 8D                           js 0x140a4fecd
00A4FF40  41 83 CF 02                     or r15d, 2
00A4FF44  44 89 7D E3                     mov dword ptr [rbp - 0x1d], r15d
00A4FF48  E9 0F FF FF FF                  jmp 0x140a4fe5c
00A4FF4D  48 8D 05 2C 2A E1 FF            lea rax, [rip - 0x1ed5d4]
00A4FF54  33 F6                           xor esi, esi
00A4FF56  48 89 05 AB 80 58 00            mov qword ptr [rip + 0x5880ab], rax
00A4FF5D  41 0B FB                        or edi, r11d
00A4FF60  48 8D 05 49 1E 07 00            lea rax, [rip + 0x71e49]
00A4FF67  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A4FF6A  48 89 05 5F 82 58 00            mov qword ptr [rip + 0x58825f], rax
00A4FF71  E9 96 FE FF FF                  jmp 0x140a4fe0c
00A4FF76  48 8D 15 BB 75 57 00            lea rdx, [rip + 0x5775bb]
00A4FF7D  48 8B CB                        mov rcx, rbx
00A4FF80  48 2B D3                        sub rdx, rbx
00A4FF83  4D 8B C5                        mov r8, r13
00A4FF86  E9 2F C6 0E 00                  jmp 0x140b3c5ba
00A4FF8B  44 0B F9                        or r15d, ecx
00A4FF8E  44 89 7D E3                     mov dword ptr [rbp - 0x1d], r15d
00A4FF92  E9 A8 FC FF FF                  jmp 0x140a4fc3f
00A4FF97  44 0B F9                        or r15d, ecx
00A4FF9A  44 89 7D E3                     mov dword ptr [rbp - 0x1d], r15d
00A4FF9E  E9 AF FC FF FF                  jmp 0x140a4fc52
00A4FFA3  8B 05 83 EB 3B 00               mov eax, dword ptr [rip + 0x3beb83]
00A4FFA9  4C 8D 4D FF                     lea r9, [rbp - 1]
00A4FFAD  48 21 75 FF                     and qword ptr [rbp - 1], rsi
00A4FFB1  48 8D 0D 08 F4 4A 00            lea rcx, [rip + 0x4af408]
00A4FFB8  48 83 4D 07 FF                  or qword ptr [rbp + 7], 0xffffffffffffffff
00A4FFBD  4C 69 C0 10 27 00 00            imul r8, rax, 0x2710
00A4FFC4  49 8B D0                        mov rdx, r8
00A4FFC7  48 F7 DA                        neg rdx
00A4FFCA  E8 11 09 95 FF                  call 0x1403a08e0
00A4FFCF  4C 8B 4D CF                     mov r9, qword ptr [rbp - 0x31]
00A4FFD3  44 8B 55 C7                     mov r10d, dword ptr [rbp - 0x39]
00A4FFD7  E9 83 FC FF FF                  jmp 0x140a4fc5f
00A4FFDC  41 0B F9                        or edi, r9d
00A4FFDF  48 89 15 BA 36 3B 00            mov qword ptr [rip + 0x3b36ba], rdx
00A4FFE6  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A4FFE9  E9 CE FC FF FF                  jmp 0x140a4fcbc
00A4FFEE  0B F9                           or edi, ecx
00A4FFF0  48 89 15 A1 36 3B 00            mov qword ptr [rip + 0x3b36a1], rdx
00A4FFF7  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A4FFFA  E9 D3 FC FF FF                  jmp 0x140a4fcd2
00A4FFFF  48 8D 05 EA 51 7D FF            lea rax, [rip - 0x82ae16]
00A50006  0B F9                           or edi, ecx
00A50008  48 89 05 81 36 3B 00            mov qword ptr [rip + 0x3b3681], rax
00A5000F  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A50012  E9 D1 FC FF FF                  jmp 0x140a4fce8
00A50017  48 8D 05 E2 43 7D FF            lea rax, [rip - 0x82bc1e]
00A5001E  0B F9                           or edi, ecx
00A50020  48 89 05 81 84 41 00            mov qword ptr [rip + 0x418481], rax
00A50027  48 8D 05 62 11 C0 FF            lea rax, [rip - 0x3fee9e]
00A5002E  48 89 05 9B 36 3B 00            mov qword ptr [rip + 0x3b369b], rax
00A50035  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A50038  E9 C1 FC FF FF                  jmp 0x140a4fcfe
00A5003D  48 8D 05 7C 41 7D FF            lea rax, [rip - 0x82be84]
00A50044  41 0B F8                        or edi, r8d
00A50047  48 89 05 62 84 41 00            mov qword ptr [rip + 0x418462], rax
00A5004E  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A50051  E9 BA FC FF FF                  jmp 0x140a4fd10
00A50056  44 8B 75 EF                     mov r14d, dword ptr [rbp - 0x11]
00A5005A  48 8D 05 8F 0D C0 FF            lea rax, [rip - 0x3ff271]
00A50061  41 83 CE 01                     or r14d, 1
00A50065  48 89 05 4C 84 41 00            mov qword ptr [rip + 0x41844c], rax
00A5006C  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A50070  E9 B3 FC FF FF                  jmp 0x140a4fd28
00A50075  48 8D 05 24 10 C0 FF            lea rax, [rip - 0x3fefdc]
00A5007C  41 83 CE 02                     or r14d, 2
00A50080  48 89 05 39 84 41 00            mov qword ptr [rip + 0x418439], rax
00A50087  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A5008B  E9 AC FC FF FF                  jmp 0x140a4fd3c
00A50090  48 8D 05 99 11 C0 FF            lea rax, [rip - 0x3fee67]
00A50097  41 0B F8                        or edi, r8d
00A5009A  48 89 05 F7 83 41 00            mov qword ptr [rip + 0x4183f7], rax
00A500A1  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A500A4  E9 AB FC FF FF                  jmp 0x140a4fd54
00A500A9  44 0B F1                        or r14d, ecx
00A500AC  48 89 15 FD 35 3B 00            mov qword ptr [rip + 0x3b35fd], rdx
00A500B3  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A500B7  E9 B6 FC FF FF                  jmp 0x140a4fd72
00A500BC  44 0B F1                        or r14d, ecx
00A500BF  48 89 15 F2 35 3B 00            mov qword ptr [rip + 0x3b35f2], rdx
00A500C6  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A500CA  E9 BA FC FF FF                  jmp 0x140a4fd89
00A500CF  45 0B F2                        or r14d, r10d
00A500D2  48 89 0D E7 35 3B 00            mov qword ptr [rip + 0x3b35e7], rcx
00A500D9  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A500DD  E9 C1 FC FF FF                  jmp 0x140a4fda3
00A500E2  45 0B F0                        or r14d, r8d
00A500E5  48 89 0D DC 35 3B 00            mov qword ptr [rip + 0x3b35dc], rcx
00A500EC  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A500F0  E9 C1 FC FF FF                  jmp 0x140a4fdb6
00A500F5  44 0B F1                        or r14d, ecx
00A500F8  48 89 15 41 EA 3B 00            mov qword ptr [rip + 0x3bea41], rdx
00A500FF  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A50103  E9 CC FC FF FF                  jmp 0x140a4fdd4
00A50108  45 0B F1                        or r14d, r9d
00A5010B  48 89 15 36 EA 3B 00            mov qword ptr [rip + 0x3bea36], rdx
00A50112  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A50116  E9 CC FC FF FF                  jmp 0x140a4fde7
00A5011B  09 4D E7                        or dword ptr [rbp - 0x19], ecx
00A5011E  48 8D 05 1B 0A C0 FF            lea rax, [rip - 0x3ff5e5]
00A50125  48 89 05 24 EA 3B 00            mov qword ptr [rip + 0x3bea24], rax
00A5012C  E9 CD FC FF FF                  jmp 0x140a4fdfe
00A50131  44 8B 75 EF                     mov r14d, dword ptr [rbp - 0x11]
00A50135  E9 CD FC FF FF                  jmp 0x140a4fe07
00A5013A  E8 1D CD CF FF                  call 0x14074ce5c
00A5013F  8B F0                           mov esi, eax
00A50141  85 C0                           test eax, eax
00A50143  0F 88 84 FD FF FF               js 0x140a4fecd
00A50149  0F BA EF 14                     bts edi, 0x14
00A5014D  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A50150  E9 C5 FC FF FF                  jmp 0x140a4fe1a
00A50155  48 8D 0D 94 55 7E FF            lea rcx, [rip - 0x81aa6c]
00A5015C  48 89 0D 65 83 41 00            mov qword ptr [rip + 0x418365], rcx
00A50163  E8 7C 3D D6 FF                  call 0x1407b3ee4
00A50168  0F BA EF 10                     bts edi, 0x10
00A5016C  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00A5016F  E9 B7 FC FF FF                  jmp 0x140a4fe2b
00A50174  41 83 CF 10                     or r15d, 0x10
00A50178  44 89 7D E3                     mov dword ptr [rbp - 0x1d], r15d
00A5017C  E9 BA FC FF FF                  jmp 0x140a4fe3b
00A50181  33 FF                           xor edi, edi
00A50183  39 3D 07 F1 4A 00               cmp dword ptr [rip + 0x4af107], edi
00A50189  0F 87 41 C4 0E 00               ja 0x140b3c5d0
00A5018F  E9 5B C4 0E 00                  jmp 0x140b3c5ef
00A50194  E8 9B F2 CF FF                  call 0x14074f434
00A50199  41 0F BA EE 07                  bts r14d, 7
00A5019E  44 89 75 EF                     mov dword ptr [rbp - 0x11], r14d
00A501A2  E9 D7 FC FF FF                  jmp 0x140a4fe7e
00A501A7  F0 FF 05 BA 82 41 00            lock inc dword ptr [rip + 0x4182ba]
00A501AE  E9 D8 FC FF FF                  jmp 0x140a4fe8b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEnableKernelTrace(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 3910481)) ^ (v_rsp);
    v_stack_m40 = result;
    v_rsi = 0;
    v_stack_m98 = a4;
    v_stack_m90 = a3;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 4912769)) == 0) goto loc_00A4FF76;
    if (a2 == 0) goto loc_00A4FC5F;
    if (((*(unsigned int *)(a2 + 4)) & ((unsigned int)((unsigned int)(0x80000ULL)))) != 0) goto loc_00A4FF8B;
loc_00A4FC3F:
    if (((*(unsigned int *)(a2 + 4)) & ((unsigned int)((unsigned int)(0x800000ULL)))) != 0) goto loc_00A4FF97;
    if (a2 == 0) goto loc_00A4FC5F;
loc_00A4FC52:
    if (((*(unsigned int *)(a2 + 4)) & (0x880000ULL)) != 0) goto loc_00A4FFA3;
loc_00A4FC5F:
    if ((*(unsigned __int8 *)(v_rip + 4912670)) <= 3) goto loc_00A4FC88;
    v_stack_mA8 = (unsigned int)((unsigned int)(a4));
    result = EtwpUpdateFileInfoDriverState(a1, a2, 1, a3);
    if ((unsigned int)(result) != 0) goto loc_00A4FE8B;
loc_00A4FC88:
    if (a2 == 0) goto loc_00A50131;
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x2000000ULL)))) != 0) goto loc_00A4FFDC;
loc_00A4FCBC:
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x4000000ULL)))) != 0) goto loc_00A4FFEE;
    if (a2 == 0) goto loc_00A50131;
loc_00A4FCD2:
    if (((*(unsigned int *)(a2)) & (512)) != 0) goto loc_00A4FFFF;
    if (a2 == 0) goto loc_00A50131;
loc_00A4FCE8:
    if (((*(unsigned int *)(a2)) & (256)) != 0) goto loc_00A50017;
    if (a2 == 0) goto loc_00A50131;
loc_00A4FCFE:
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x400ULL)))) != 0) goto loc_00A5003D;
    if (a2 == 0) goto loc_00A50131;
loc_00A4FD10:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (1)) != 0) goto loc_00A50056;
    if (a2 == 0) goto loc_00A50131;
loc_00A4FD28:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (2)) != 0) goto loc_00A50075;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FD3C:
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x200000ULL)))) != 0) goto loc_00A50090;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FD54:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x400000ULL)))) != 0) goto loc_00A500A9;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FD72:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x80000ULL)))) != 0) goto loc_00A500BC;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FD89:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x100000ULL)))) != 0) goto loc_00A500CF;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FDA3:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x200000ULL)))) != 0) goto loc_00A500E2;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FDB6:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x1000000ULL)))) != 0) goto loc_00A500F5;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FDD4:
    if (((*(unsigned int *)(a2 + 16)) & ((unsigned int)((unsigned int)(0x2000000ULL)))) != 0) goto loc_00A50108;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FDE7:
    if (((*(unsigned int *)(a2 + 8)) & ((unsigned int)((unsigned int)(0x8000000ULL)))) != 0) goto loc_00A5011B;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FDFE:
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x20000ULL)))) != 0) goto loc_00A4FF4D;
loc_00A4FE07:
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE0C:
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0x100000ULL)))) != 0) goto loc_00A5013A;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE1A:
    if (((*(unsigned int *)(a2)) & (0x10000ULL)) != 0) goto loc_00A50155;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE2B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (16)) != 0) goto loc_00A4FEB9;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE3B:
    if (((*(unsigned int *)(a2)) & (0x40000ULL)) != 0) goto loc_00A4FF15;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE4C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (2)) != 0) goto loc_00A4FF35;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE5C:
    if (((*(unsigned int *)(a2 + 4)) & (0x400ULL)) != 0) goto loc_00A50181;
    if (a2 == 0) goto loc_00A4FE8B;
    if (sign_flag) goto loc_00A50194;
    if (a2 == 0) goto loc_00A4FE8B;
loc_00A4FE7E:
    if (((*(unsigned int *)(a2 + 4)) & (0x20000ULL)) != 0) goto loc_00A501A7;
loc_00A4FE8B:
    if (sign_flag) goto loc_00A4FECD;
loc_00A4FE8F:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 5939730, (unsigned int)(0x200000ULL), (unsigned int)(0x2000000ULL));
    v_rsp = (v_rsp) + (144);
    return result;
loc_00A4FEB9:
    result = IoPerfInit(1, v_rip - 5939730, (unsigned int)(0x200000ULL), (unsigned int)(0x2000000ULL));
    if (!sign_flag) goto loc_00A50174;
loc_00A4FECD:
    v_rbx = (v_stack_p8) - (a1);
    v_stack_m60 = v_xmm0;
    a1 = (v_stack_m60) - (a1);
    v_stack_m50 = v_xmm0;
loc_00A4FEE2:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_rbx + a1 * 1))));
    result = (unsigned int)((result) & (*(unsigned int *)(a1)));
    *(unsigned int *)(a1 + a1 * 1) = (unsigned int)(result);
    v_r13 = (v_rsi + 8) - (1);
    if (condition_is_not_equal) goto loc_00A4FEE2;
    result = EtwpDisableKernelTrace(v_stack_m60, v_stack_m80, v_stack_m90, (unsigned int)(v_stack_m98));
    goto loc_00A4FE8F;
loc_00A4FF15:
    result = DbgSetDebugPrintCallback(v_rip - 4190846, 1, v_stack_m90, (unsigned int)(v_stack_m98));
    if (sign_flag) goto loc_00A4FECD;
    v_stack_m80 = (unsigned int)((unsigned int)(v_stack_m80));
    goto loc_00A4FE4C;
loc_00A4FF35:
    result = EtwpTimeProfileStart(v_rip - 4190846, 1, v_stack_m90, (unsigned int)(v_stack_m98));
    if (sign_flag) goto loc_00A4FECD;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m7C)) | (2));
    v_stack_m7C = (unsigned int)(v_r15);
    goto loc_00A4FE5C;
loc_00A4FF4D:
    v_rsi = 0;
    *(unsigned __int64 *)(v_rip + 5800107) = v_rip - 2020820;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m80)) | ((unsigned int)((unsigned int)(0x20000ULL))));
    v_stack_m80 = (unsigned int)(v_rdi);
    *(unsigned __int64 *)(v_rip + 5800543) = v_rip + 466505;
    goto loc_00A4FE0C;
loc_00A4FF76:
    a2 = (v_rip + 5731771) - (v_rbx);
loc_00A4FF8B:
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(v_rbx)));
    v_stack_m7C = (unsigned int)(v_r15);
    goto loc_00A4FC3F;
loc_00A4FF97:
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(v_rbx)));
    v_stack_m7C = (unsigned int)(v_r15);
    goto loc_00A4FC52;
loc_00A4FFA3:
    a3 = (v_r13) * ((unsigned int)(*(unsigned int *)(v_rip + 3926915)));
    a2 = -(a3);
    result = KeSetTimer2(v_rip + 4912136, a2, a3, v_stack_m60);
    goto loc_00A4FC5F;
loc_00A4FFDC:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_stack_m90)));
    *(unsigned __int64 *)(v_rip + 3880634) = a2;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FCBC;
loc_00A4FFEE:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 3880609) = a2;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FCD2;
loc_00A4FFFF:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 3880577) = v_rip - 8564246;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FCE8;
loc_00A50017:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 4293761) = v_rip - 8567838;
    *(unsigned __int64 *)(v_rip + 3880603) = v_rip - 4189854;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FCFE;
loc_00A5003D:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a3)));
    *(unsigned __int64 *)(v_rip + 4293730) = v_rip - 8568452;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FD10;
loc_00A50056:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m70)) | (1));
    *(unsigned __int64 *)(v_rip + 4293708) = v_rip - 4190833;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FD28;
loc_00A50075:
    v_r14 = (unsigned int)((v_r14) | (2));
    *(unsigned __int64 *)(v_rip + 4293689) = v_rip - 4190172;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FD3C;
loc_00A50090:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a3)));
    *(unsigned __int64 *)(v_rip + 4293623) = v_rip - 4189799;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FD54;
loc_00A500A9:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 3880445) = a2;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FD72;
loc_00A500BC:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 3880434) = a2;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FD89;
loc_00A500CF:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)((unsigned int)(v_stack_m98))));
    *(unsigned __int64 *)(v_rip + 3880423) = v_rip + 4912136;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FDA3;
loc_00A500E2:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(a3)));
    *(unsigned __int64 *)(v_rip + 3880412) = v_rip + 4912136;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FDB6;
loc_00A500F5:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(v_rip + 4912136)));
    *(unsigned __int64 *)(v_rip + 3926593) = a2;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FDD4;
loc_00A50108:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(v_stack_m90)));
    *(unsigned __int64 *)(v_rip + 3926582) = a2;
    v_stack_m70 = (unsigned int)(v_r14);
    goto loc_00A4FDE7;
loc_00A5011B:
    *(unsigned __int64 *)(v_rip + 3926564) = v_rip - 4191717;
    goto loc_00A4FDFE;
loc_00A50131:
    goto loc_00A4FE07;
loc_00A5013A:
    result = AlpcRegisterLogRoutine(v_rip + 4912136, a2, a3, v_stack_m90);
    if (sign_flag) goto loc_00A4FECD;
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FE1A;
loc_00A50155:
    *(unsigned __int64 *)(v_rip + 4293477) = v_rip - 8497772;
    result = WmiSetNetworkNotify(v_rip - 8497772, a2, a3, v_stack_m90);
    v_stack_m80 = (unsigned int)(v_rdi);
    goto loc_00A4FE2B;
loc_00A50174:
    v_r15 = (unsigned int)((v_r15) | (16));
    v_stack_m7C = (unsigned int)(v_r15);
    goto loc_00A4FE3B;
loc_00A50181:
    v_rdi = 0;
loc_00A50194:
    result = ObEnableEtwReferenceTrace(v_rip - 8497772, a2, a3, v_stack_m90);
    v_stack_m70 = (unsigned int)((unsigned int)(v_stack_m70));
    goto loc_00A4FE7E;
loc_00A501A7:
    goto loc_00A4FE8B;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEnableKernelTrace(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x3BAB51)) ^ (local_rsp);
    v_stack_m40 = result;
    local_rsi = 0;
    v_stack_m98 = Arg4;
    v_stack_m90 = Arg3;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0x4AF681)) == 0) goto loc_00A4FF76;
    if (Arg2 == 0) goto loc_00A4FC5F;
    if (((*(uint32_t *)(Arg2 + 0x4)) & ((uint32_t)((uint32_t)(0x80000ULL)))) != 0) goto loc_00A4FF8B;
loc_00A4FC3F:
    if (((*(uint32_t *)(Arg2 + 0x4)) & ((uint32_t)((uint32_t)(0x800000ULL)))) != 0) goto loc_00A4FF97;
    if (Arg2 == 0) goto loc_00A4FC5F;
loc_00A4FC52:
    if (((*(uint32_t *)(Arg2 + 0x4)) & (0x880000ULL)) != 0) goto loc_00A4FFA3;
loc_00A4FC5F:
    if ((*(uint8_t *)(v_rip + 0x4AF61E)) <= 3) goto loc_00A4FC88;
    v_stack_mA8 = (uint32_t)((uint32_t)(Arg4));
    result = EtwpUpdateFileInfoDriverState(Arg1, Arg2, 1, Arg3);
    if ((uint32_t)(result) != 0) goto loc_00A4FE8B;
loc_00A4FC88:
    if (Arg2 == 0) goto loc_00A50131;
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x2000000ULL)))) != 0) goto loc_00A4FFDC;
loc_00A4FCBC:
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x4000000ULL)))) != 0) goto loc_00A4FFEE;
    if (Arg2 == 0) goto loc_00A50131;
loc_00A4FCD2:
    if (((*(uint32_t *)(Arg2)) & (512)) != 0) goto loc_00A4FFFF;
    if (Arg2 == 0) goto loc_00A50131;
loc_00A4FCE8:
    if (((*(uint32_t *)(Arg2)) & (256)) != 0) goto loc_00A50017;
    if (Arg2 == 0) goto loc_00A50131;
loc_00A4FCFE:
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x400ULL)))) != 0) goto loc_00A5003D;
    if (Arg2 == 0) goto loc_00A50131;
loc_00A4FD10:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) & (1)) != 0) goto loc_00A50056;
    if (Arg2 == 0) goto loc_00A50131;
loc_00A4FD28:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) & (2)) != 0) goto loc_00A50075;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FD3C:
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x200000ULL)))) != 0) goto loc_00A50090;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FD54:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x400000ULL)))) != 0) goto loc_00A500A9;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FD72:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x80000ULL)))) != 0) goto loc_00A500BC;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FD89:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x100000ULL)))) != 0) goto loc_00A500CF;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FDA3:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x200000ULL)))) != 0) goto loc_00A500E2;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FDB6:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x1000000ULL)))) != 0) goto loc_00A500F5;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FDD4:
    if (((*(uint32_t *)(Arg2 + 0x10)) & ((uint32_t)((uint32_t)(0x2000000ULL)))) != 0) goto loc_00A50108;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FDE7:
    if (((*(uint32_t *)(Arg2 + 0x8)) & ((uint32_t)((uint32_t)(0x8000000ULL)))) != 0) goto loc_00A5011B;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FDFE:
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x20000ULL)))) != 0) goto loc_00A4FF4D;
loc_00A4FE07:
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE0C:
    if (((*(uint32_t *)(Arg2)) & ((uint32_t)((uint32_t)(0x100000ULL)))) != 0) goto loc_00A5013A;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE1A:
    if (((*(uint32_t *)(Arg2)) & (0x10000ULL)) != 0) goto loc_00A50155;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE2B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)))) & (16)) != 0) goto loc_00A4FEB9;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE3B:
    if (((*(uint32_t *)(Arg2)) & (0x40000ULL)) != 0) goto loc_00A4FF15;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE4C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)))) & (2)) != 0) goto loc_00A4FF35;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE5C:
    if (((*(uint32_t *)(Arg2 + 0x4)) & (0x400ULL)) != 0) goto loc_00A50181;
    if (Arg2 == 0) goto loc_00A4FE8B;
    if (sign_flag) goto loc_00A50194;
    if (Arg2 == 0) goto loc_00A4FE8B;
loc_00A4FE7E:
    if (((*(uint32_t *)(Arg2 + 0x4)) & (0x20000ULL)) != 0) goto loc_00A501A7;
loc_00A4FE8B:
    if (sign_flag) goto loc_00A4FECD;
loc_00A4FE8F:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 5939730, (uint32_t)(0x200000ULL), (uint32_t)(0x2000000ULL));
    local_rsp = (local_rsp) + (144);
    return result;
loc_00A4FEB9:
    result = IoPerfInit(1, v_rip - 5939730, (uint32_t)(0x200000ULL), (uint32_t)(0x2000000ULL));
    if (!sign_flag) goto loc_00A50174;
loc_00A4FECD:
    local_rbx = (v_stack_p8) - (Arg1);
    v_stack_m60 = v_xmm0;
    Arg1 = (v_stack_m60) - (Arg1);
    v_stack_m50 = v_xmm0;
loc_00A4FEE2:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(local_rbx + arg1 * 1))));
    result = (uint32_t)((result) & (*(uint32_t *)(arg1)));
    *(uint32_t *)(arg1 + arg1 * 1) = (uint32_t)(result);
    local_r13 = (local_rsi + 8) - (1);
    if (condition_is_not_equal) goto loc_00A4FEE2;
    result = EtwpDisableKernelTrace(v_stack_m60, v_stack_m80, v_stack_m90, (uint32_t)(v_stack_m98));
    goto loc_00A4FE8F;
loc_00A4FF15:
    result = DbgSetDebugPrintCallback(v_rip - 4190846, 1, v_stack_m90, (uint32_t)(v_stack_m98));
    if (sign_flag) goto loc_00A4FECD;
    v_stack_m80 = (uint32_t)((uint32_t)(v_stack_m80));
    goto loc_00A4FE4C;
loc_00A4FF35:
    result = EtwpTimeProfileStart(v_rip - 4190846, 1, v_stack_m90, (uint32_t)(v_stack_m98));
    if (sign_flag) goto loc_00A4FECD;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m7C)) | (2));
    v_stack_m7C = (uint32_t)(local_r15);
    goto loc_00A4FE5C;
loc_00A4FF4D:
    local_rsi = 0;
    *(uint64_t *)(v_rip + 0x5880AB) = v_rip - 2020820;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m80)) | ((uint32_t)((uint32_t)(0x20000ULL))));
    v_stack_m80 = (uint32_t)(local_rdi);
    *(uint64_t *)(v_rip + 0x58825F) = v_rip + 466505;
    goto loc_00A4FE0C;
loc_00A4FF76:
    Arg2 = (v_rip + 5731771) - (local_rbx);
loc_00A4FF8B:
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(local_rbx)));
    v_stack_m7C = (uint32_t)(local_r15);
    goto loc_00A4FC3F;
loc_00A4FF97:
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(local_rbx)));
    v_stack_m7C = (uint32_t)(local_r15);
    goto loc_00A4FC52;
loc_00A4FFA3:
    Arg3 = (local_r13) * ((uint32_t)(*(uint32_t *)(v_rip + 0x3BEB83)));
    Arg2 = -(Arg3);
    result = KeSetTimer2(v_rip + 4912136, Arg2, Arg3, v_stack_m60);
    goto loc_00A4FC5F;
loc_00A4FFDC:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_stack_m90)));
    *(uint64_t *)(v_rip + 0x3B36BA) = Arg2;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FCBC;
loc_00A4FFEE:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x3B36A1) = Arg2;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FCD2;
loc_00A4FFFF:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x3B3681) = v_rip - 8564246;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FCE8;
loc_00A50017:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x418481) = v_rip - 8567838;
    *(uint64_t *)(v_rip + 0x3B369B) = v_rip - 4189854;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FCFE;
loc_00A5003D:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg3)));
    *(uint64_t *)(v_rip + 0x418462) = v_rip - 8568452;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FD10;
loc_00A50056:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m70)) | (1));
    *(uint64_t *)(v_rip + 0x41844C) = v_rip - 4190833;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FD28;
loc_00A50075:
    local_r14 = (uint32_t)((local_r14) | (2));
    *(uint64_t *)(v_rip + 0x418439) = v_rip - 4190172;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FD3C;
loc_00A50090:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg3)));
    *(uint64_t *)(v_rip + 0x4183F7) = v_rip - 4189799;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FD54;
loc_00A500A9:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x3B35FD) = Arg2;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FD72;
loc_00A500BC:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x3B35F2) = Arg2;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FD89;
loc_00A500CF:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)((uint32_t)(v_stack_m98))));
    *(uint64_t *)(v_rip + 0x3B35E7) = v_rip + 4912136;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FDA3;
loc_00A500E2:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(Arg3)));
    *(uint64_t *)(v_rip + 0x3B35DC) = v_rip + 4912136;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FDB6;
loc_00A500F5:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(v_rip + 4912136)));
    *(uint64_t *)(v_rip + 0x3BEA41) = Arg2;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FDD4;
loc_00A50108:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(v_stack_m90)));
    *(uint64_t *)(v_rip + 0x3BEA36) = Arg2;
    v_stack_m70 = (uint32_t)(local_r14);
    goto loc_00A4FDE7;
loc_00A5011B:
    *(uint64_t *)(v_rip + 0x3BEA24) = v_rip - 4191717;
    goto loc_00A4FDFE;
loc_00A50131:
    goto loc_00A4FE07;
loc_00A5013A:
    result = AlpcRegisterLogRoutine(v_rip + 4912136, Arg2, Arg3, v_stack_m90);
    if (sign_flag) goto loc_00A4FECD;
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FE1A;
loc_00A50155:
    *(uint64_t *)(v_rip + 0x418365) = v_rip - 8497772;
    result = WmiSetNetworkNotify(v_rip - 8497772, Arg2, Arg3, v_stack_m90);
    v_stack_m80 = (uint32_t)(local_rdi);
    goto loc_00A4FE2B;
loc_00A50174:
    local_r15 = (uint32_t)((local_r15) | (16));
    v_stack_m7C = (uint32_t)(local_r15);
    goto loc_00A4FE3B;
loc_00A50181:
    local_rdi = 0;
loc_00A50194:
    result = ObEnableEtwReferenceTrace(v_rip - 8497772, Arg2, Arg3, v_stack_m90);
    v_stack_m70 = (uint32_t)((uint32_t)(v_stack_m70));
    goto loc_00A4FE7E;
loc_00A501A7:
    goto loc_00A4FE8B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4FBCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
