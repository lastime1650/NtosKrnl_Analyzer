# EtwpDisableKernelTrace

- RVA: `0x00A4F7D8`–`0x00A4FBC3` (길이 `1,003` bytes)
- VA: `0x0000000140A4F7D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B094C`
- 디코드: `216`개 명령, `1,003/1,003` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x00A4FA36` → [AlpcUnregisterLogRoutine](../74/AlpcUnregisterLogRoutine_function_0074CF84.md) (function, `0x0074CF84`)
- `0x00A4FAA6` → [WmiSetNetworkNotify](../7B/WmiSetNetworkNotify_function_007B3EE4.md) (function, `0x007B3EE4`)
- `0x00A4FAB5` → [IoPerfReset](../../text/59/IoPerfReset_function_0059863C.md) (function, `0x0059863C`)
- `0x00A4FB31` → [DbgSetDebugPrintCallback](../../text/4F/DbgSetDebugPrintCallback_function_004FC110.md) (function, `0x004FC110`)
- `0x00A4FB42` → [KeStopProfile](../../text/5C/KeStopProfile_function_005C0640.md) (function, `0x005C0640`)
- `0x00A4FB6A` → [ObDisableEtwReferenceTrace](../74/ObDisableEtwReferenceTrace_function_0074F394.md) (function, `0x0074F394`)
- `0x00A4FB90` → [WmiTraceRundownNotify](../9E/WmiTraceRundownNotify_function_009E46E0.md) (function, `0x009E46E0`)
- `0x00A4FB97` → [EtwpUpdateFileInfoDriverRegistration](../7B/EtwpUpdateFileInfoDriverRegistration_function_007B8B1C.md) (function, `0x007B8B1C`)
- `0x00A4FBA8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A4FBB2` → [ZwUnloadDriver](../../text/6B/ZwUnloadDriver_function_006B0C10.md) (function, `0x006B0C10`)

### Direct callers
- [EtwpUpdateGlobalGroupMasks](EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) at `0x00A4F6F4`
- [EtwpEnableKernelTrace](EtwpEnableKernelTrace_function_00A4FBCC.md) at `0x00A4FF0B`

### Static image references
- `0x00A4F883` → RVA `0x00E684B0` (`.data`; write)
- `0x00A4F9FC` → RVA `0x00E68488` (`.data`; read)
- `0x00A4FA23` → RVA `0x00FD8008` (`PAGEDATA`; write)
- `0x00A4FA2A` → RVA `0x00FD81D0` (`PAGEDATA`; write)
- `0x00A4FA40` → RVA `0x00E036A0` (`.data`; write)
- `0x00A4FA4C` → RVA `0x00E03698` (`.data`; write)
- `0x00A4FA58` → RVA `0x00E03690` (`.data`; write)
- `0x00A4FA64` → RVA `0x00E684A8` (`.data`; write)
- `0x00A4FA6B` → RVA `0x00E036D0` (`.data`; write)
- `0x00A4FA77` → RVA `0x00E684B8` (`.data`; write)
- `0x00A4FA8C` → RVA `0x00E684C0` (`.data`; write)
- `0x00A4FA98` → RVA `0x00E68498` (`.data`; write)
- `0x00A4FABF` → RVA `0x00E036B0` (`.data`; write)
- `0x00A4FAD4` → RVA `0x00E036B8` (`.data`; write)
- `0x00A4FAE4` → RVA `0x00E036C0` (`.data`; write)
- `0x00A4FAF4` → RVA `0x00E036C8` (`.data`; write)
- `0x00A4FB04` → RVA `0x00E0EB40` (`.data`; write)
- `0x00A4FB10` → RVA `0x00E0EB48` (`.data`; write)
- `0x00A4FB1C` → RVA `0x00E0EB50` (`.data`; write)
- `0x00A4FB2A` → RVA `0x00650CA0` (`EtwpTraceDebugPrint`; read)
- `0x00A4FB3B` → RVA `0x00EFF520` (`.data`; read)
- `0x00A4FB55` → RVA `0x00EFF290` (`.data`; read)
- `0x00A4FB9C` → RVA `0x00B07530` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A4FBB7` → RVA `0x00E68488` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00A4FAB5` → [IoPerfReset](../../text/59/IoPerfReset_function_0059863C.md) (`PAGE` → `.text`)
  - `0x00A4FB31` → [DbgSetDebugPrintCallback](../../text/4F/DbgSetDebugPrintCallback_function_004FC110.md) (`PAGE` → `.text`)
  - `0x00A4FB42` → [KeStopProfile](../../text/5C/KeStopProfile_function_005C0640.md) (`PAGE` → `.text`)
  - `0x00A4FBA8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A4FBB2` → [ZwUnloadDriver](../../text/6B/ZwUnloadDriver_function_006B0C10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00A4FB65` → [sub_00B3C582](../B3/Unknown_function_00B3C582.md) (`tail-transfer`)
  - `0x00A4FB77` → [sub_00B3C582 + 0x24](../B3/Unknown_function_00B3C582.md) (`tail-transfer`)
  - `0x00A4FB86` → [sub_00B3C582 + 0x24](../B3/Unknown_function_00B3C582.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A4F7D8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A4F7DD  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A4F7E2  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A4F7E7  57                              push rdi
00A4F7E8  41 56                           push r14
00A4F7EA  41 57                           push r15
00A4F7EC  48 83 EC 30                     sub rsp, 0x30
00A4F7F0  45 33 FF                        xor r15d, r15d
00A4F7F3  41 8B E9                        mov ebp, r9d
00A4F7F6  4D 8B F0                        mov r14, r8
00A4F7F9  48 8B DA                        mov rbx, rdx
00A4F7FC  48 8B F1                        mov rsi, rcx
00A4F7FF  48 85 D2                        test rdx, rdx
00A4F802  0F 84 7B 02 00 00               je 0x140a4fa83
00A4F808  F7 02 00 00 02 00               test dword ptr [rdx], 0x20000
00A4F80E  0F 85 0F 02 00 00               jne 0x140a4fa23
00A4F814  0F BA 22 14                     bt dword ptr [rdx], 0x14
00A4F818  0F 82 18 02 00 00               jb 0x140a4fa36
00A4F81E  48 85 DB                        test rbx, rbx
00A4F821  0F 84 5C 02 00 00               je 0x140a4fa83
00A4F827  F7 03 00 00 00 02               test dword ptr [rbx], 0x2000000
00A4F82D  0F 85 0D 02 00 00               jne 0x140a4fa40
00A4F833  48 85 DB                        test rbx, rbx
00A4F836  0F 84 47 02 00 00               je 0x140a4fa83
00A4F83C  F7 03 00 00 00 04               test dword ptr [rbx], 0x4000000
00A4F842  0F 85 04 02 00 00               jne 0x140a4fa4c
00A4F848  48 85 DB                        test rbx, rbx
00A4F84B  0F 84 32 02 00 00               je 0x140a4fa83
00A4F851  F7 03 00 02 00 00               test dword ptr [rbx], 0x200
00A4F857  0F 85 FB 01 00 00               jne 0x140a4fa58
00A4F85D  48 85 DB                        test rbx, rbx
00A4F860  0F 84 1D 02 00 00               je 0x140a4fa83
00A4F866  F7 03 00 01 00 00               test dword ptr [rbx], 0x100
00A4F86C  0F 85 F2 01 00 00               jne 0x140a4fa64
00A4F872  48 85 DB                        test rbx, rbx
00A4F875  0F 84 08 02 00 00               je 0x140a4fa83
00A4F87B  F7 03 00 04 00 00               test dword ptr [rbx], 0x400
00A4F881  74 09                           je 0x140a4f88c
00A4F883  4C 89 3D 26 8C 41 00            mov qword ptr [rip + 0x418c26], r15
00A4F88A  EB 09                           jmp 0x140a4f895
00A4F88C  48 85 DB                        test rbx, rbx
00A4F88F  0F 84 EE 01 00 00               je 0x140a4fa83
00A4F895  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A4F899  8B 01                           mov eax, dword ptr [rcx]
00A4F89B  A8 01                           test al, 1
00A4F89D  0F 85 D4 01 00 00               jne 0x140a4fa77
00A4F8A3  48 85 DB                        test rbx, rbx
00A4F8A6  0F 84 1F 02 00 00               je 0x140a4facb
00A4F8AC  8B 01                           mov eax, dword ptr [rcx]
00A4F8AE  A8 02                           test al, 2
00A4F8B0  0F 85 D6 01 00 00               jne 0x140a4fa8c
00A4F8B6  48 85 DB                        test rbx, rbx
00A4F8B9  0F 84 0C 02 00 00               je 0x140a4facb
00A4F8BF  F7 03 00 00 20 00               test dword ptr [rbx], 0x200000
00A4F8C5  0F 85 CD 01 00 00               jne 0x140a4fa98
00A4F8CB  48 85 DB                        test rbx, rbx
00A4F8CE  0F 84 F7 01 00 00               je 0x140a4facb
00A4F8D4  F7 03 00 00 01 00               test dword ptr [rbx], 0x10000
00A4F8DA  0F 85 C4 01 00 00               jne 0x140a4faa4
00A4F8E0  48 85 DB                        test rbx, rbx
00A4F8E3  0F 84 E2 01 00 00               je 0x140a4facb
00A4F8E9  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A4F8EC  A8 10                           test al, 0x10
00A4F8EE  0F 85 BC 01 00 00               jne 0x140a4fab0
00A4F8F4  48 85 DB                        test rbx, rbx
00A4F8F7  0F 84 CE 01 00 00               je 0x140a4facb
00A4F8FD  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A4F901  F7 01 00 00 40 00               test dword ptr [rcx], 0x400000
00A4F907  0F 85 B2 01 00 00               jne 0x140a4fabf
00A4F90D  48 85 DB                        test rbx, rbx
00A4F910  74 0C                           je 0x140a4f91e
00A4F912  F7 01 00 00 08 00               test dword ptr [rcx], 0x80000
00A4F918  0F 85 B6 01 00 00               jne 0x140a4fad4
00A4F91E  48 8B D1                        mov rdx, rcx
00A4F921  48 85 DB                        test rbx, rbx
00A4F924  74 0A                           je 0x140a4f930
00A4F926  0F BA 21 14                     bt dword ptr [rcx], 0x14
00A4F92A  0F 82 B4 01 00 00               jb 0x140a4fae4
00A4F930  48 8B CA                        mov rcx, rdx
00A4F933  48 85 DB                        test rbx, rbx
00A4F936  74 0C                           je 0x140a4f944
00A4F938  F7 02 00 00 20 00               test dword ptr [rdx], 0x200000
00A4F93E  0F 85 B0 01 00 00               jne 0x140a4faf4
00A4F944  48 8B D1                        mov rdx, rcx
00A4F947  48 85 DB                        test rbx, rbx
00A4F94A  0F 84 FC 01 00 00               je 0x140a4fb4c
00A4F950  F7 01 00 00 00 01               test dword ptr [rcx], 0x1000000
00A4F956  0F 85 A8 01 00 00               jne 0x140a4fb04
00A4F95C  48 85 DB                        test rbx, rbx
00A4F95F  0F 84 E7 01 00 00               je 0x140a4fb4c
00A4F965  F7 02 00 00 00 02               test dword ptr [rdx], 0x2000000
00A4F96B  0F 85 9F 01 00 00               jne 0x140a4fb10
00A4F971  48 85 DB                        test rbx, rbx
00A4F974  0F 84 D2 01 00 00               je 0x140a4fb4c
00A4F97A  F7 43 08 00 00 00 08            test dword ptr [rbx + 8], 0x8000000
00A4F981  0F 85 95 01 00 00               jne 0x140a4fb1c
00A4F987  48 85 DB                        test rbx, rbx
00A4F98A  0F 84 BC 01 00 00               je 0x140a4fb4c
00A4F990  F7 03 00 00 04 00               test dword ptr [rbx], 0x40000
00A4F996  0F 85 8C 01 00 00               jne 0x140a4fb28
00A4F99C  48 85 DB                        test rbx, rbx
00A4F99F  0F 84 A7 01 00 00               je 0x140a4fb4c
00A4F9A5  48 8D 7B 04                     lea rdi, [rbx + 4]
00A4F9A9  8B 07                           mov eax, dword ptr [rdi]
00A4F9AB  A8 02                           test al, 2
00A4F9AD  0F 85 88 01 00 00               jne 0x140a4fb3b
00A4F9B3  48 85 DB                        test rbx, rbx
00A4F9B6  74 2F                           je 0x140a4f9e7
00A4F9B8  F7 07 00 04 00 00               test dword ptr [rdi], 0x400
00A4F9BE  0F 85 91 01 00 00               jne 0x140a4fb55
00A4F9C4  48 85 DB                        test rbx, rbx
00A4F9C7  74 1E                           je 0x140a4f9e7
00A4F9C9  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A4F9CC  84 C0                           test al, al
00A4F9CE  0F 88 96 01 00 00               js 0x140a4fb6a
00A4F9D4  48 85 DB                        test rbx, rbx
00A4F9D7  74 0E                           je 0x140a4f9e7
00A4F9D9  B9 00 00 88 00                  mov ecx, 0x880000
00A4F9DE  85 4B 04                        test dword ptr [rbx + 4], ecx
00A4F9E1  0F 85 8D 01 00 00               jne 0x140a4fb74
00A4F9E7  0F 57 C0                        xorps xmm0, xmm0
00A4F9EA  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00A4F9EF  48 85 F6                        test rsi, rsi
00A4F9F2  74 08                           je 0x140a4f9fc
00A4F9F4  F7 06 00 02 00 06               test dword ptr [rsi], 0x6000200
00A4F9FA  75 0D                           jne 0x140a4fa09
00A4F9FC  44 39 3D 85 8A 41 00            cmp dword ptr [rip + 0x418a85], r15d
00A4FA03  0F 85 82 01 00 00               jne 0x140a4fb8b
00A4FA09  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A4FA0E  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00A4FA13  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00A4FA18  48 83 C4 30                     add rsp, 0x30
00A4FA1C  41 5F                           pop r15
00A4FA1E  41 5E                           pop r14
00A4FA20  5F                              pop rdi
00A4FA21  C3                              ret
00A4FA22  CC                              int3
00A4FA23  4C 89 3D DE 85 58 00            mov qword ptr [rip + 0x5885de], r15
00A4FA2A  4C 89 3D 9F 87 58 00            mov qword ptr [rip + 0x58879f], r15
00A4FA31  E9 DE FD FF FF                  jmp 0x140a4f814
00A4FA36  E8 49 D5 CF FF                  call 0x14074cf84
00A4FA3B  E9 E7 FD FF FF                  jmp 0x140a4f827
00A4FA40  4C 89 3D 59 3C 3B 00            mov qword ptr [rip + 0x3b3c59], r15
00A4FA47  E9 F0 FD FF FF                  jmp 0x140a4f83c
00A4FA4C  4C 89 3D 45 3C 3B 00            mov qword ptr [rip + 0x3b3c45], r15
00A4FA53  E9 F9 FD FF FF                  jmp 0x140a4f851
00A4FA58  4C 89 3D 31 3C 3B 00            mov qword ptr [rip + 0x3b3c31], r15
00A4FA5F  E9 02 FE FF FF                  jmp 0x140a4f866
00A4FA64  4C 89 3D 3D 8A 41 00            mov qword ptr [rip + 0x418a3d], r15
00A4FA6B  4C 89 3D 5E 3C 3B 00            mov qword ptr [rip + 0x3b3c5e], r15
00A4FA72  E9 04 FE FF FF                  jmp 0x140a4f87b
00A4FA77  4C 89 3D 3A 8A 41 00            mov qword ptr [rip + 0x418a3a], r15
00A4FA7E  E9 29 FE FF FF                  jmp 0x140a4f8ac
00A4FA83  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A4FA87  E9 17 FE FF FF                  jmp 0x140a4f8a3
00A4FA8C  4C 89 3D 2D 8A 41 00            mov qword ptr [rip + 0x418a2d], r15
00A4FA93  E9 27 FE FF FF                  jmp 0x140a4f8bf
00A4FA98  4C 89 3D F9 89 41 00            mov qword ptr [rip + 0x4189f9], r15
00A4FA9F  E9 30 FE FF FF                  jmp 0x140a4f8d4
00A4FAA4  33 C9                           xor ecx, ecx
00A4FAA6  E8 39 44 D6 FF                  call 0x1407b3ee4
00A4FAAB  E9 39 FE FF FF                  jmp 0x140a4f8e9
00A4FAB0  B9 01 00 00 00                  mov ecx, 1
00A4FAB5  E8 82 8B B4 FF                  call 0x14059863c
00A4FABA  E9 3E FE FF FF                  jmp 0x140a4f8fd
00A4FABF  4C 89 3D EA 3B 3B 00            mov qword ptr [rip + 0x3b3bea], r15
00A4FAC6  E9 47 FE FF FF                  jmp 0x140a4f912
00A4FACB  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A4FACF  E9 39 FE FF FF                  jmp 0x140a4f90d
00A4FAD4  4C 89 3D DD 3B 3B 00            mov qword ptr [rip + 0x3b3bdd], r15
00A4FADB  48 8D 53 10                     lea rdx, [rbx + 0x10]
00A4FADF  E9 42 FE FF FF                  jmp 0x140a4f926
00A4FAE4  4C 89 3D D5 3B 3B 00            mov qword ptr [rip + 0x3b3bd5], r15
00A4FAEB  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A4FAEF  E9 44 FE FF FF                  jmp 0x140a4f938
00A4FAF4  4C 89 3D CD 3B 3B 00            mov qword ptr [rip + 0x3b3bcd], r15
00A4FAFB  48 8D 53 10                     lea rdx, [rbx + 0x10]
00A4FAFF  E9 4C FE FF FF                  jmp 0x140a4f950
00A4FB04  4C 89 3D 35 F0 3B 00            mov qword ptr [rip + 0x3bf035], r15
00A4FB0B  E9 55 FE FF FF                  jmp 0x140a4f965
00A4FB10  4C 89 3D 31 F0 3B 00            mov qword ptr [rip + 0x3bf031], r15
00A4FB17  E9 5E FE FF FF                  jmp 0x140a4f97a
00A4FB1C  4C 89 3D 2D F0 3B 00            mov qword ptr [rip + 0x3bf02d], r15
00A4FB23  E9 68 FE FF FF                  jmp 0x140a4f990
00A4FB28  33 D2                           xor edx, edx
00A4FB2A  48 8D 0D 6F 11 C0 FF            lea rcx, [rip - 0x3fee91]
00A4FB31  E8 DA C5 AA FF                  call 0x1404fc110
00A4FB36  E9 6A FE FF FF                  jmp 0x140a4f9a5
00A4FB3B  48 8D 0D DE F9 4A 00            lea rcx, [rip + 0x4af9de]
00A4FB42  E8 F9 0A B7 FF                  call 0x1405c0640
00A4FB47  E9 6C FE FF FF                  jmp 0x140a4f9b8
00A4FB4C  48 8D 7B 04                     lea rdi, [rbx + 4]
00A4FB50  E9 5E FE FF FF                  jmp 0x140a4f9b3
00A4FB55  44 39 3D 34 F7 4A 00            cmp dword ptr [rip + 0x4af734], r15d
00A4FB5C  41 8B FF                        mov edi, r15d
00A4FB5F  0F 86 64 FE FF FF               jbe 0x140a4f9c9
00A4FB65  E9 18 CA 0E 00                  jmp 0x140b3c582
00A4FB6A  E8 25 F8 CF FF                  call 0x14074f394
00A4FB6F  E9 65 FE FF FF                  jmp 0x140a4f9d9
00A4FB74  48 85 F6                        test rsi, rsi
00A4FB77  0F 84 29 CA 0E 00               je 0x140b3c5a6
00A4FB7D  85 4E 04                        test dword ptr [rsi + 4], ecx
00A4FB80  0F 85 61 FE FF FF               jne 0x140a4f9e7
00A4FB86  E9 1B CA 0E 00                  jmp 0x140b3c5a6
00A4FB8B  49 8B 0E                        mov rcx, qword ptr [r14]
00A4FB8E  8B D5                           mov edx, ebp
00A4FB90  E8 4B 4B F9 FF                  call 0x1409e46e0
00A4FB95  33 C9                           xor ecx, ecx
00A4FB97  E8 80 8F D6 FF                  call 0x1407b8b1c
00A4FB9C  48 8D 15 8D 79 0B 00            lea rdx, [rip + 0xb798d]
00A4FBA3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A4FBA8  E8 D3 AB 9D FF                  call 0x14042a780
00A4FBAD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A4FBB2  E8 59 10 C6 FF                  call 0x1406b0c10
00A4FBB7  44 89 3D CA 88 41 00            mov dword ptr [rip + 0x4188ca], r15d
00A4FBBE  E9 46 FE FF FF                  jmp 0x140a4fa09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpDisableKernelTrace(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_r15 = 0;
    if (a2 == 0) goto loc_00A4FA83;
    if (((*(unsigned int *)(a2)) & (0x20000ULL)) != 0) goto loc_00A4FA23;
loc_00A4F814:
    if (condition_is_below) goto loc_00A4FA36;
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F827:
    if (((*(unsigned int *)(a2)) & (0x2000000ULL)) != 0) goto loc_00A4FA40;
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F83C:
    if (((*(unsigned int *)(a2)) & (0x4000000ULL)) != 0) goto loc_00A4FA4C;
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F851:
    if (((*(unsigned int *)(a2)) & (512)) != 0) goto loc_00A4FA58;
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F866:
    if (((*(unsigned int *)(a2)) & (256)) != 0) goto loc_00A4FA64;
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F87B:
    if (((*(unsigned int *)(a2)) & (0x400ULL)) == 0) goto loc_00A4F88C;
    *(unsigned __int64 *)(v_rip + 4295718) = 0;
    goto loc_00A4F895;
loc_00A4F88C:
    if (a2 == 0) goto loc_00A4FA83;
loc_00A4F895:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (1)) != 0) goto loc_00A4FA77;
loc_00A4F8A3:
    if (a2 == 0) goto loc_00A4FACB;
loc_00A4F8AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (2)) != 0) goto loc_00A4FA8C;
    if (a2 == 0) goto loc_00A4FACB;
loc_00A4F8BF:
    if (((*(unsigned int *)(a2)) & (0x200000ULL)) != 0) goto loc_00A4FA98;
    if (a2 == 0) goto loc_00A4FACB;
loc_00A4F8D4:
    if (((*(unsigned int *)(a2)) & (0x10000ULL)) != 0) goto loc_00A4FAA4;
    if (a2 == 0) goto loc_00A4FACB;
loc_00A4F8E9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (16)) != 0) goto loc_00A4FAB0;
    if (a2 == 0) goto loc_00A4FACB;
loc_00A4F8FD:
    if (((*(unsigned int *)(a2 + 16)) & (0x400000ULL)) != 0) goto loc_00A4FABF;
loc_00A4F90D:
    if (a2 == 0) goto loc_00A4F91E;
loc_00A4F912:
    if (((*(unsigned int *)(a2 + 16)) & (0x80000ULL)) != 0) goto loc_00A4FAD4;
loc_00A4F91E:
    if (a2 == 0) goto loc_00A4F930;
loc_00A4F926:
    if (condition_is_below) goto loc_00A4FAE4;
loc_00A4F930:
    if (a2 == 0) goto loc_00A4F944;
loc_00A4F938:
    if (((*(unsigned int *)(a2 + 16)) & (0x200000ULL)) != 0) goto loc_00A4FAF4;
loc_00A4F944:
    if (a2 == 0) goto loc_00A4FB4C;
loc_00A4F950:
    if (((*(unsigned int *)(a2 + 16)) & (0x1000000ULL)) != 0) goto loc_00A4FB04;
    if (a2 == 0) goto loc_00A4FB4C;
loc_00A4F965:
    if (((*(unsigned int *)(a2 + 16)) & (0x2000000ULL)) != 0) goto loc_00A4FB10;
    if (a2 == 0) goto loc_00A4FB4C;
loc_00A4F97A:
    if (((*(unsigned int *)(a2 + 8)) & (0x8000000ULL)) != 0) goto loc_00A4FB1C;
    if (a2 == 0) goto loc_00A4FB4C;
loc_00A4F990:
    if (((*(unsigned int *)(a2)) & (0x40000ULL)) != 0) goto loc_00A4FB28;
    if (a2 == 0) goto loc_00A4FB4C;
loc_00A4F9A5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 4)))) & (2)) != 0) goto loc_00A4FB3B;
loc_00A4F9B3:
    if (a2 == 0) goto loc_00A4F9E7;
loc_00A4F9B8:
    if (((*(unsigned int *)(a2 + 4)) & (0x400ULL)) != 0) goto loc_00A4FB55;
    if (a2 == 0) goto loc_00A4F9E7;
loc_00A4F9C9:
    if (sign_flag) goto loc_00A4FB6A;
    if (a2 == 0) goto loc_00A4F9E7;
loc_00A4F9D9:
    if (((*(unsigned int *)(a2 + 4)) & ((unsigned int)((unsigned int)(0x880000ULL)))) != 0) goto loc_00A4FB74;
loc_00A4F9E7:
    v_stack_m28 = v_xmm0;
    if (a1 == 0) goto loc_00A4F9FC;
    if (((*(unsigned int *)(a1)) & (0x6000200ULL)) != 0) goto loc_00A4FA09;
loc_00A4F9FC:
    if ((*(unsigned int *)(v_rip + 4295301)) != 0) goto loc_00A4FB8B;
loc_00A4FA09:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(a2 + 16));
loc_00A4FA23:
    *(unsigned __int64 *)(v_rip + 5801438) = 0;
    *(unsigned __int64 *)(v_rip + 5801887) = 0;
    goto loc_00A4F814;
loc_00A4FA36:
    result = AlpcUnregisterLogRoutine((unsigned int)(0x880000ULL), a2 + 16, a3, a4);
    goto loc_00A4F827;
loc_00A4FA40:
    *(unsigned __int64 *)(v_rip + 3882073) = 0;
    goto loc_00A4F83C;
loc_00A4FA4C:
    *(unsigned __int64 *)(v_rip + 3882053) = 0;
    goto loc_00A4F851;
loc_00A4FA58:
    *(unsigned __int64 *)(v_rip + 3882033) = 0;
    goto loc_00A4F866;
loc_00A4FA64:
    *(unsigned __int64 *)(v_rip + 4295229) = 0;
    *(unsigned __int64 *)(v_rip + 3882078) = 0;
    goto loc_00A4F87B;
loc_00A4FA77:
    *(unsigned __int64 *)(v_rip + 4295226) = 0;
    goto loc_00A4F8AC;
loc_00A4FA83:
    goto loc_00A4F8A3;
loc_00A4FA8C:
    *(unsigned __int64 *)(v_rip + 4295213) = 0;
    goto loc_00A4F8BF;
loc_00A4FA98:
    *(unsigned __int64 *)(v_rip + 4295161) = 0;
    goto loc_00A4F8D4;
loc_00A4FAA4:
    a1 = 0;
    result = WmiSetNetworkNotify(a1, a2 + 16, a3, a4);
    goto loc_00A4F8E9;
loc_00A4FAB0:
    result = IoPerfReset(1, a2 + 16, a3, a4);
    goto loc_00A4F8FD;
loc_00A4FABF:
    *(unsigned __int64 *)(v_rip + 3881962) = 0;
    goto loc_00A4F912;
loc_00A4FACB:
    goto loc_00A4F90D;
loc_00A4FAD4:
    *(unsigned __int64 *)(v_rip + 3881949) = 0;
    goto loc_00A4F926;
loc_00A4FAE4:
    *(unsigned __int64 *)(v_rip + 3881941) = 0;
    goto loc_00A4F938;
loc_00A4FAF4:
    *(unsigned __int64 *)(v_rip + 3881933) = 0;
    goto loc_00A4F950;
loc_00A4FB04:
    *(unsigned __int64 *)(v_rip + 3928117) = 0;
    goto loc_00A4F965;
loc_00A4FB10:
    *(unsigned __int64 *)(v_rip + 3928113) = 0;
    goto loc_00A4F97A;
loc_00A4FB1C:
    *(unsigned __int64 *)(v_rip + 3928109) = 0;
    goto loc_00A4F990;
loc_00A4FB28:
    a2 = 0;
    result = DbgSetDebugPrintCallback(v_rip - 4189841, a2, a3, a4);
    goto loc_00A4F9A5;
loc_00A4FB3B:
    result = KeStopProfile(v_rip + 4913630, a2, a3, a4);
    goto loc_00A4F9B8;
loc_00A4FB4C:
    goto loc_00A4F9B3;
loc_00A4FB55:
    if ((*(unsigned int *)(v_rip + 4912948)) <= 0) goto loc_00A4F9C9;
loc_00A4FB6A:
    result = ObDisableEtwReferenceTrace(v_rip + 4913630, a2, a3, a4);
    goto loc_00A4F9D9;
loc_00A4FB74:
    if (((*(unsigned int *)(v_stack_p18 + 4)) & ((unsigned int)(v_rip + 4913630))) != 0) goto loc_00A4F9E7;
loc_00A4FB8B:
    result = WmiTraceRundownNotify(*(unsigned __int64 *)(a3), (unsigned int)((unsigned int)(v_stack_p10)), a3, a4);
    a1 = 0;
    result = EtwpUpdateFileInfoDriverRegistration(a1, (unsigned int)((unsigned int)(v_stack_p10)), a3, a4);
    result = RtlInitUnicodeString(v_stack_p20, v_rip + 752013, a3, a4);
    result = ZwUnloadDriver(v_stack_p20, v_rip + 752013, a3, a4);
    *(unsigned int *)(v_rip + 4294858) = 0;
    goto loc_00A4FA09;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpDisableKernelTrace(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_r15 = 0;
    if (Arg2 == 0) goto loc_00A4FA83;
    if (((*(uint32_t *)(Arg2)) & (0x20000ULL)) != 0) goto loc_00A4FA23;
loc_00A4F814:
    if (condition_is_below) goto loc_00A4FA36;
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F827:
    if (((*(uint32_t *)(Arg2)) & (0x2000000ULL)) != 0) goto loc_00A4FA40;
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F83C:
    if (((*(uint32_t *)(Arg2)) & (0x4000000ULL)) != 0) goto loc_00A4FA4C;
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F851:
    if (((*(uint32_t *)(Arg2)) & (512)) != 0) goto loc_00A4FA58;
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F866:
    if (((*(uint32_t *)(Arg2)) & (256)) != 0) goto loc_00A4FA64;
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F87B:
    if (((*(uint32_t *)(Arg2)) & (0x400ULL)) == 0) goto loc_00A4F88C;
    *(uint64_t *)(v_rip + 0x418C26) = 0;
    goto loc_00A4F895;
loc_00A4F88C:
    if (Arg2 == 0) goto loc_00A4FA83;
loc_00A4F895:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) & (1)) != 0) goto loc_00A4FA77;
loc_00A4F8A3:
    if (Arg2 == 0) goto loc_00A4FACB;
loc_00A4F8AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) & (2)) != 0) goto loc_00A4FA8C;
    if (Arg2 == 0) goto loc_00A4FACB;
loc_00A4F8BF:
    if (((*(uint32_t *)(Arg2)) & (0x200000ULL)) != 0) goto loc_00A4FA98;
    if (Arg2 == 0) goto loc_00A4FACB;
loc_00A4F8D4:
    if (((*(uint32_t *)(Arg2)) & (0x10000ULL)) != 0) goto loc_00A4FAA4;
    if (Arg2 == 0) goto loc_00A4FACB;
loc_00A4F8E9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)))) & (16)) != 0) goto loc_00A4FAB0;
    if (Arg2 == 0) goto loc_00A4FACB;
loc_00A4F8FD:
    if (((*(uint32_t *)(Arg2 + 0x10)) & (0x400000ULL)) != 0) goto loc_00A4FABF;
loc_00A4F90D:
    if (Arg2 == 0) goto loc_00A4F91E;
loc_00A4F912:
    if (((*(uint32_t *)(Arg2 + 0x10)) & (0x80000ULL)) != 0) goto loc_00A4FAD4;
loc_00A4F91E:
    if (Arg2 == 0) goto loc_00A4F930;
loc_00A4F926:
    if (condition_is_below) goto loc_00A4FAE4;
loc_00A4F930:
    if (Arg2 == 0) goto loc_00A4F944;
loc_00A4F938:
    if (((*(uint32_t *)(Arg2 + 0x10)) & (0x200000ULL)) != 0) goto loc_00A4FAF4;
loc_00A4F944:
    if (Arg2 == 0) goto loc_00A4FB4C;
loc_00A4F950:
    if (((*(uint32_t *)(Arg2 + 0x10)) & (0x1000000ULL)) != 0) goto loc_00A4FB04;
    if (Arg2 == 0) goto loc_00A4FB4C;
loc_00A4F965:
    if (((*(uint32_t *)(Arg2 + 0x10)) & (0x2000000ULL)) != 0) goto loc_00A4FB10;
    if (Arg2 == 0) goto loc_00A4FB4C;
loc_00A4F97A:
    if (((*(uint32_t *)(Arg2 + 0x8)) & (0x8000000ULL)) != 0) goto loc_00A4FB1C;
    if (Arg2 == 0) goto loc_00A4FB4C;
loc_00A4F990:
    if (((*(uint32_t *)(Arg2)) & (0x40000ULL)) != 0) goto loc_00A4FB28;
    if (Arg2 == 0) goto loc_00A4FB4C;
loc_00A4F9A5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)))) & (2)) != 0) goto loc_00A4FB3B;
loc_00A4F9B3:
    if (Arg2 == 0) goto loc_00A4F9E7;
loc_00A4F9B8:
    if (((*(uint32_t *)(Arg2 + 0x4)) & (0x400ULL)) != 0) goto loc_00A4FB55;
    if (Arg2 == 0) goto loc_00A4F9E7;
loc_00A4F9C9:
    if (sign_flag) goto loc_00A4FB6A;
    if (Arg2 == 0) goto loc_00A4F9E7;
loc_00A4F9D9:
    if (((*(uint32_t *)(Arg2 + 0x4)) & ((uint32_t)((uint32_t)(0x880000ULL)))) != 0) goto loc_00A4FB74;
loc_00A4F9E7:
    v_stack_m28 = v_xmm0;
    if (Arg1 == 0) goto loc_00A4F9FC;
    if (((*(uint32_t *)(Arg1)) & (0x6000200ULL)) != 0) goto loc_00A4FA09;
loc_00A4F9FC:
    if ((*(uint32_t *)(v_rip + 0x418A85)) != 0) goto loc_00A4FB8B;
loc_00A4FA09:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(Arg2 + 0x10));
loc_00A4FA23:
    *(uint64_t *)(v_rip + 0x5885DE) = 0;
    *(uint64_t *)(v_rip + 0x58879F) = 0;
    goto loc_00A4F814;
loc_00A4FA36:
    result = AlpcUnregisterLogRoutine((uint32_t)(0x880000ULL), Arg2 + 16, Arg3, Arg4);
    goto loc_00A4F827;
loc_00A4FA40:
    *(uint64_t *)(v_rip + 0x3B3C59) = 0;
    goto loc_00A4F83C;
loc_00A4FA4C:
    *(uint64_t *)(v_rip + 0x3B3C45) = 0;
    goto loc_00A4F851;
loc_00A4FA58:
    *(uint64_t *)(v_rip + 0x3B3C31) = 0;
    goto loc_00A4F866;
loc_00A4FA64:
    *(uint64_t *)(v_rip + 0x418A3D) = 0;
    *(uint64_t *)(v_rip + 0x3B3C5E) = 0;
    goto loc_00A4F87B;
loc_00A4FA77:
    *(uint64_t *)(v_rip + 0x418A3A) = 0;
    goto loc_00A4F8AC;
loc_00A4FA83:
    goto loc_00A4F8A3;
loc_00A4FA8C:
    *(uint64_t *)(v_rip + 0x418A2D) = 0;
    goto loc_00A4F8BF;
loc_00A4FA98:
    *(uint64_t *)(v_rip + 0x4189F9) = 0;
    goto loc_00A4F8D4;
loc_00A4FAA4:
    Arg1 = 0;
    result = WmiSetNetworkNotify(Arg1, Arg2 + 16, Arg3, Arg4);
    goto loc_00A4F8E9;
loc_00A4FAB0:
    result = IoPerfReset(1, Arg2 + 16, Arg3, Arg4);
    goto loc_00A4F8FD;
loc_00A4FABF:
    *(uint64_t *)(v_rip + 0x3B3BEA) = 0;
    goto loc_00A4F912;
loc_00A4FACB:
    goto loc_00A4F90D;
loc_00A4FAD4:
    *(uint64_t *)(v_rip + 0x3B3BDD) = 0;
    goto loc_00A4F926;
loc_00A4FAE4:
    *(uint64_t *)(v_rip + 0x3B3BD5) = 0;
    goto loc_00A4F938;
loc_00A4FAF4:
    *(uint64_t *)(v_rip + 0x3B3BCD) = 0;
    goto loc_00A4F950;
loc_00A4FB04:
    *(uint64_t *)(v_rip + 0x3BF035) = 0;
    goto loc_00A4F965;
loc_00A4FB10:
    *(uint64_t *)(v_rip + 0x3BF031) = 0;
    goto loc_00A4F97A;
loc_00A4FB1C:
    *(uint64_t *)(v_rip + 0x3BF02D) = 0;
    goto loc_00A4F990;
loc_00A4FB28:
    Arg2 = 0;
    result = DbgSetDebugPrintCallback(v_rip - 4189841, Arg2, Arg3, Arg4);
    goto loc_00A4F9A5;
loc_00A4FB3B:
    result = KeStopProfile(v_rip + 4913630, Arg2, Arg3, Arg4);
    goto loc_00A4F9B8;
loc_00A4FB4C:
    goto loc_00A4F9B3;
loc_00A4FB55:
    if ((*(uint32_t *)(v_rip + 0x4AF734)) <= 0) goto loc_00A4F9C9;
loc_00A4FB6A:
    result = ObDisableEtwReferenceTrace(v_rip + 4913630, Arg2, Arg3, Arg4);
    goto loc_00A4F9D9;
loc_00A4FB74:
    if (((*(uint32_t *)(v_stack_p18 + 0x4)) & ((uint32_t)(v_rip + 4913630))) != 0) goto loc_00A4F9E7;
loc_00A4FB8B:
    result = WmiTraceRundownNotify(*(uint64_t *)(arg3), (uint32_t)((uint32_t)(v_stack_p10)), Arg3, Arg4);
    Arg1 = 0;
    result = EtwpUpdateFileInfoDriverRegistration(Arg1, (uint32_t)((uint32_t)(v_stack_p10)), Arg3, Arg4);
    result = RtlInitUnicodeString(v_stack_p20, v_rip + 752013, Arg3, Arg4);
    result = ZwUnloadDriver(v_stack_p20, v_rip + 752013, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x4188CA) = 0;
    goto loc_00A4FA09;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4F7D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
