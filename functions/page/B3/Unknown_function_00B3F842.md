# sub_00B3F842

- RVA: `0x00B3F842`–`0x00B3FE64` (길이 `1,570` bytes)
- VA: `0x0000000140B3F842`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B4BDC`
- 디코드: `389`개 명령, `1,570/1,570` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00B3F842` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3F865` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00B3F8A2` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00B3F953` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (function, `0x004FE4E0`)
- `0x00B3FA79` → [KdSetDbgPrintBufferSize](../../text/5B/KdSetDbgPrintBufferSize_function_005B0F54.md) (function, `0x005B0F54`)
- `0x00B3FAEE` → [KdDisableDebugger](../../text/5B/KdDisableDebugger_function_005B0900.md) (function, `0x005B0900`)
- `0x00B3FAF5` → [KdEnableDebugger](../../text/5B/KdEnableDebugger_function_005B0A40.md) (function, `0x005B0A40`)
- `0x00B3FAFF` → [ExpKdPullRemoteFileForUser](../7D/ExpKdPullRemoteFileForUser_function_007D15AC.md) (function, `0x007D15AC`)
- `0x00B3FBD2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B3FC12` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00B3FC26` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B3FC4D` → [DbgkCaptureLiveDump](../71/DbgkCaptureLiveDump_function_0071113C.md) (function, `0x0071113C`)
- `0x00B3FC74` → [EtwTiLogSyscallUsage](../90/EtwTiLogSyscallUsage_function_00903890.md) (function, `0x00903890`)
- `0x00B3FC85` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3FC9C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B3FCA6` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)
- `0x00B3FD57` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3FD74` → [DbgkCaptureLiveKernelDump](../../text/58/DbgkCaptureLiveKernelDump_function_00580288.md) (function, `0x00580288`)
- `0x00B3FD86` → [EtwTiLogSyscallUsage](../90/EtwTiLogSyscallUsage_function_00903890.md) (function, `0x00903890`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B3F947` → RVA `0x00F475F8` (`.data`; read)
- `0x00B3FA0E` → RVA `0x00F55CA0` (`.data`; write)
- `0x00B3FA2E` → RVA `0x00F55CA0` (`.data`; read)
- `0x00B3FA8C` → RVA `0x00E0AA54` (`.data`; read)
- `0x00B3FAB4` → RVA `0x00F55CA1` (`.data`; write)
- `0x00B3FAD4` → RVA `0x00F55CA1` (`.data`; read)
- `0x00B3FD1D` → RVA `0x00F49B5C` (`.data`; write)
- `0x00B3FD99` → RVA `0x00F49B54` (`.data`; read)
- `0x00B3FDB3` → RVA `0x00F49B60` (`.data`; read)
- `0x00B3FDC1` → RVA `0x00F49B54` (`.data`; write)
- `0x00B3FDD5` → RVA `0x00F49B58` (`.data`; read)
- `0x00B3FDEB` → RVA `0x00F49B50` (`.data`; read)
- `0x00B3FDF9` → RVA `0x00F49B58` (`.data`; write)
- `0x00B3FE11` → RVA `0x00F55CB2` (`.data`; write)
- `0x00B3FE26` → RVA `0x00F55CB2` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00B3F842` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3F953` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (`PAGE` → `.text`)
  - `0x00B3FA79` → [KdSetDbgPrintBufferSize](../../text/5B/KdSetDbgPrintBufferSize_function_005B0F54.md) (`PAGE` → `.text`)
  - `0x00B3FAEE` → [KdDisableDebugger](../../text/5B/KdDisableDebugger_function_005B0900.md) (`PAGE` → `.text`)
  - `0x00B3FAF5` → [KdEnableDebugger](../../text/5B/KdEnableDebugger_function_005B0A40.md) (`PAGE` → `.text`)
  - `0x00B3FBD2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B3FC26` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B3FC85` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B3FC9C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B3FCA6` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
  - `0x00B3FD57` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B3FD74` → [DbgkCaptureLiveKernelDump](../../text/58/DbgkCaptureLiveKernelDump_function_00580288.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00B3F902` → [NtSystemDebugControl + 0x9A](../A6/NtSystemDebugControl_function_00A6E760.md) (`tail-transfer`)
  - `0x00B3F9A8` → [NtSystemDebugControl + 0x9A](../A6/NtSystemDebugControl_function_00A6E760.md) (`tail-transfer`)
  - `0x00B3FCB5` → [NtSystemDebugControl + 0x9A](../A6/NtSystemDebugControl_function_00A6E760.md) (`tail-transfer`)
  - `0x00B3FE3F` → [NtSystemDebugControl + 0x9A](../A6/NtSystemDebugControl_function_00A6E760.md) (`tail-transfer`)
  - `0x00B3FE5F` → [NtSystemDebugControl + 0x9A](../A6/NtSystemDebugControl_function_00A6E760.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3F842  E8 99 6A 8F FF                  call 0x1404362e0
00B3F847  84 C0                           test al, al
00B3F849  0F 85 AE 00 00 00               jne 0x140b3f8fd
00B3F84F  33 FF                           xor edi, edi
00B3F851  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00B3F855  45 84 ED                        test r13b, r13b
00B3F858  74 6E                           je 0x140b3f8c8
00B3F85A  45 85 FF                        test r15d, r15d
00B3F85D  74 29                           je 0x140b3f888
00B3F85F  41 F6 C6 03                     test r14b, 3
00B3F863  74 05                           je 0x140b3f86a
00B3F865  E8 66 A7 D5 FF                  call 0x140899fd0
00B3F86A  4B 8D 0C 3E                     lea rcx, [r14 + r15]
00B3F86E  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00B3F878  49 3B CD                        cmp rcx, r13
00B3F87B  77 05                           ja 0x140b3f882
00B3F87D  49 3B CE                        cmp rcx, r14
00B3F880  73 10                           jae 0x140b3f892
00B3F882  41 8A 45 00                     mov al, byte ptr [r13]
00B3F886  EB 0A                           jmp 0x140b3f892
00B3F888  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00B3F892  85 F6                           test esi, esi
00B3F894  74 11                           je 0x140b3f8a7
00B3F896  48 8B D6                        mov rdx, rsi
00B3F899  41 B8 04 00 00 00               mov r8d, 4
00B3F89F  49 8B CC                        mov rcx, r12
00B3F8A2  E8 19 99 DA FF                  call 0x1408e91c0
00B3F8A7  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
00B3F8AF  48 85 C9                        test rcx, rcx
00B3F8B2  74 0F                           je 0x140b3f8c3
00B3F8B4  49 3B CD                        cmp rcx, r13
00B3F8B7  4C 0F 42 E9                     cmovb r13, rcx
00B3F8BB  41 8B 45 00                     mov eax, dword ptr [r13]
00B3F8BF  41 89 45 00                     mov dword ptr [r13], eax
00B3F8C3  44 8A 6C 24 34                  mov r13b, byte ptr [rsp + 0x34]
00B3F8C8  EB 3D                           jmp 0x140b3f907
00B3F8CA  8B F8                           mov edi, eax
00B3F8CC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3F8D0  8B B4 24 40 01 00 00            mov esi, dword ptr [rsp + 0x140]
00B3F8D7  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
00B3F8DF  44 8B BC 24 30 01 00 00         mov r15d, dword ptr [rsp + 0x130]
00B3F8E7  4C 8B B4 24 28 01 00 00         mov r14, qword ptr [rsp + 0x128]
00B3F8EF  8B 9C 24 20 01 00 00            mov ebx, dword ptr [rsp + 0x120]
00B3F8F6  44 8A 6C 24 35                  mov r13b, byte ptr [rsp + 0x35]
00B3F8FB  EB 0A                           jmp 0x140b3f907
00B3F8FD  B8 22 00 00 C0                  mov eax, 0xc0000022
00B3F902  E9 F3 EE F2 FF                  jmp 0x140a6e7fa
00B3F907  85 FF                           test edi, edi
00B3F909  0F 85 4E 05 00 00               jne 0x140b3fe5d
00B3F90F  83 FB 13                        cmp ebx, 0x13
00B3F912  0F 8F 95 00 00 00               jg 0x140b3f9ad
00B3F918  0F 84 85 00 00 00               je 0x140b3f9a3
00B3F91E  83 FB 09                        cmp ebx, 9
00B3F921  7F 4F                           jg 0x140b3f972
00B3F923  74 7E                           je 0x140b3f9a3
00B3F925  85 DB                           test ebx, ebx
00B3F927  74 7A                           je 0x140b3f9a3
00B3F929  83 EB 01                        sub ebx, 1
00B3F92C  74 75                           je 0x140b3f9a3
00B3F92E  83 EB 01                        sub ebx, 1
00B3F931  74 70                           je 0x140b3f9a3
00B3F933  83 EB 01                        sub ebx, 1
00B3F936  74 6B                           je 0x140b3f9a3
00B3F938  83 EB 01                        sub ebx, 1
00B3F93B  74 66                           je 0x140b3f9a3
00B3F93D  83 EB 01                        sub ebx, 1
00B3F940  74 61                           je 0x140b3f9a3
00B3F942  83 EB 01                        sub ebx, 1
00B3F945  75 4E                           jne 0x140b3f995
00B3F947  80 3D AA 7C 40 00 01            cmp byte ptr [rip + 0x407caa], 1
00B3F94E  75 18                           jne 0x140b3f968
00B3F950  8D 4F 06                        lea ecx, [rdi + 6]
00B3F953  E8 88 EB 9B FF                  call 0x1404fe4e0
00B3F958  E9 E7 04 00 00                  jmp 0x140b3fe44
00B3F95D  8B F8                           mov edi, eax
00B3F95F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3F963  E9 DC 04 00 00                  jmp 0x140b3fe44
00B3F968  BF 01 00 00 C0                  mov edi, 0xc0000001
00B3F96D  E9 B7 03 00 00                  jmp 0x140b3fd29
00B3F972  83 EB 0A                        sub ebx, 0xa
00B3F975  74 2C                           je 0x140b3f9a3
00B3F977  83 EB 01                        sub ebx, 1
00B3F97A  74 27                           je 0x140b3f9a3
00B3F97C  83 EB 01                        sub ebx, 1
00B3F97F  74 22                           je 0x140b3f9a3
00B3F981  83 EB 01                        sub ebx, 1
00B3F984  74 1D                           je 0x140b3f9a3
00B3F986  83 EB 01                        sub ebx, 1
00B3F989  74 18                           je 0x140b3f9a3
00B3F98B  83 EB 01                        sub ebx, 1
00B3F98E  74 13                           je 0x140b3f9a3
00B3F990  83 EB 01                        sub ebx, 1
00B3F993  74 0E                           je 0x140b3f9a3
00B3F995  83 EB 01                        sub ebx, 1
00B3F998  74 09                           je 0x140b3f9a3
00B3F99A  83 FB 01                        cmp ebx, 1
00B3F99D  0F 85 73 03 00 00               jne 0x140b3fd16
00B3F9A3  B8 02 00 00 C0                  mov eax, 0xc0000002
00B3F9A8  E9 4D EE F2 FF                  jmp 0x140a6e7fa
00B3F9AD  83 FB 1D                        cmp ebx, 0x1d
00B3F9B0  0F 8F 04 03 00 00               jg 0x140b3fcba
00B3F9B6  0F 84 53 01 00 00               je 0x140b3fb0f
00B3F9BC  83 EB 14                        sub ebx, 0x14
00B3F9BF  74 E2                           je 0x140b3f9a3
00B3F9C1  83 EB 01                        sub ebx, 1
00B3F9C4  0F 84 2B 01 00 00               je 0x140b3faf5
00B3F9CA  83 EB 01                        sub ebx, 1
00B3F9CD  0F 84 1B 01 00 00               je 0x140b3faee
00B3F9D3  83 EB 01                        sub ebx, 1
00B3F9D6  0F 84 EF 00 00 00               je 0x140b3facb
00B3F9DC  83 EB 01                        sub ebx, 1
00B3F9DF  0F 84 C1 00 00 00               je 0x140b3faa6
00B3F9E5  83 EB 01                        sub ebx, 1
00B3F9E8  0F 84 95 00 00 00               je 0x140b3fa83
00B3F9EE  83 EB 01                        sub ebx, 1
00B3F9F1  74 59                           je 0x140b3fa4c
00B3F9F3  83 EB 01                        sub ebx, 1
00B3F9F6  74 2D                           je 0x140b3fa25
00B3F9F8  83 FB 01                        cmp ebx, 1
00B3F9FB  0F 85 15 03 00 00               jne 0x140b3fd16
00B3FA01  44 3B FB                        cmp r15d, ebx
00B3FA04  0F 85 30 04 00 00               jne 0x140b3fe3a
00B3FA0A  41 80 3E 00                     cmp byte ptr [r14], 0
00B3FA0E  0F 94 05 8B 62 41 00            sete byte ptr [rip + 0x41628b]
00B3FA15  E9 2A 04 00 00                  jmp 0x140b3fe44
00B3FA1A  8B F8                           mov edi, eax
00B3FA1C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FA20  E9 1F 04 00 00                  jmp 0x140b3fe44
00B3FA25  83 FE 01                        cmp esi, 1
00B3FA28  0F 85 0C 04 00 00               jne 0x140b3fe3a
00B3FA2E  80 3D 6B 62 41 00 00            cmp byte ptr [rip + 0x41626b], 0
00B3FA35  0F 94 C0                        sete al
00B3FA38  41 88 04 24                     mov byte ptr [r12], al
00B3FA3C  E9 03 04 00 00                  jmp 0x140b3fe44
00B3FA41  8B F8                           mov edi, eax
00B3FA43  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FA47  E9 F8 03 00 00                  jmp 0x140b3fe44
00B3FA4C  41 83 FF 04                     cmp r15d, 4
00B3FA50  0F 85 E4 03 00 00               jne 0x140b3fe3a
00B3FA56  C7 44 24 3C 00 00 00 00         mov dword ptr [rsp + 0x3c], 0
00B3FA5E  41 8B 0E                        mov ecx, dword ptr [r14]
00B3FA61  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
00B3FA65  EB 0A                           jmp 0x140b3fa71
00B3FA67  8B F8                           mov edi, eax
00B3FA69  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FA6D  8B 4C 24 3C                     mov ecx, dword ptr [rsp + 0x3c]
00B3FA71  85 FF                           test edi, edi
00B3FA73  0F 85 CB 03 00 00               jne 0x140b3fe44
00B3FA79  E8 D6 14 A7 FF                  call 0x1405b0f54
00B3FA7E  E9 81 00 00 00                  jmp 0x140b3fb04
00B3FA83  83 FE 04                        cmp esi, 4
00B3FA86  0F 85 AE 03 00 00               jne 0x140b3fe3a
00B3FA8C  8B 05 C2 AF 2C 00               mov eax, dword ptr [rip + 0x2cafc2]
00B3FA92  41 89 04 24                     mov dword ptr [r12], eax
00B3FA96  E9 A9 03 00 00                  jmp 0x140b3fe44
00B3FA9B  8B F8                           mov edi, eax
00B3FA9D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FAA1  E9 9E 03 00 00                  jmp 0x140b3fe44
00B3FAA6  41 83 FF 01                     cmp r15d, 1
00B3FAAA  0F 85 8A 03 00 00               jne 0x140b3fe3a
00B3FAB0  41 80 3E 00                     cmp byte ptr [r14], 0
00B3FAB4  0F 95 05 E6 61 41 00            setne byte ptr [rip + 0x4161e6]
00B3FABB  E9 84 03 00 00                  jmp 0x140b3fe44
00B3FAC0  8B F8                           mov edi, eax
00B3FAC2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FAC6  E9 79 03 00 00                  jmp 0x140b3fe44
00B3FACB  83 FE 01                        cmp esi, 1
00B3FACE  0F 85 66 03 00 00               jne 0x140b3fe3a
00B3FAD4  8A 05 C7 61 41 00               mov al, byte ptr [rip + 0x4161c7]
00B3FADA  41 88 04 24                     mov byte ptr [r12], al
00B3FADE  E9 61 03 00 00                  jmp 0x140b3fe44
00B3FAE3  8B F8                           mov edi, eax
00B3FAE5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FAE9  E9 56 03 00 00                  jmp 0x140b3fe44
00B3FAEE  E8 0D 0E A7 FF                  call 0x1405b0900
00B3FAF3  EB 0F                           jmp 0x140b3fb04
00B3FAF5  E8 46 0F A7 FF                  call 0x1405b0a40
00B3FAFA  EB 08                           jmp 0x140b3fb04
00B3FAFC  49 8B CE                        mov rcx, r14
00B3FAFF  E8 A8 1A C9 FF                  call 0x1407d15ac
00B3FB04  8B F8                           mov edi, eax
00B3FB06  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FB0A  E9 35 03 00 00                  jmp 0x140b3fe44
00B3FB0F  41 83 FF 38                     cmp r15d, 0x38
00B3FB13  0F 85 21 03 00 00               jne 0x140b3fe3a
00B3FB19  81 FE 00 00 04 00               cmp esi, 0x40000
00B3FB1F  0F 82 15 03 00 00               jb 0x140b3fe3a
00B3FB25  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00B3FB29  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00B3FB2E  41 0F 10 4E 10                  movups xmm1, xmmword ptr [r14 + 0x10]
00B3FB33  0F 11 4C 24 68                  movups xmmword ptr [rsp + 0x68], xmm1
00B3FB38  41 0F 10 46 20                  movups xmm0, xmmword ptr [r14 + 0x20]
00B3FB3D  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B3FB42  F2 41 0F 10 4E 30               movsd xmm1, qword ptr [r14 + 0x30]
00B3FB48  F2 0F 11 8C 24 88 00 00 00      movsd qword ptr [rsp + 0x88], xmm1
00B3FB51  EB 1A                           jmp 0x140b3fb6d
00B3FB53  8B F8                           mov edi, eax
00B3FB55  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FB59  8B B4 24 40 01 00 00            mov esi, dword ptr [rsp + 0x140]
00B3FB60  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
00B3FB68  44 8A 6C 24 35                  mov r13b, byte ptr [rsp + 0x35]
00B3FB6D  85 FF                           test edi, edi
00B3FB6F  0F 85 CF 02 00 00               jne 0x140b3fe44
00B3FB75  39 BC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], edi
00B3FB7C  0F 85 2E 01 00 00               jne 0x140b3fcb0
00B3FB82  8B 84 24 84 00 00 00            mov eax, dword ptr [rsp + 0x84]
00B3FB89  85 C0                           test eax, eax
00B3FB8B  0F 84 1F 01 00 00               je 0x140b3fcb0
00B3FB91  F7 44 24 58 FE FF FF FF         test dword ptr [rsp + 0x58], 0xfffffffe
00B3FB99  0F 85 11 01 00 00               jne 0x140b3fcb0
00B3FB9F  48 C1 E0 03                     shl rax, 3
00B3FBA3  B9 FF FF FF FF                  mov ecx, 0xffffffff
00B3FBA8  8B F9                           mov edi, ecx
00B3FBAA  48 3B C1                        cmp rax, rcx
00B3FBAD  0F 46 F8                        cmovbe edi, eax
00B3FBB0  0F 87 FA 00 00 00               ja 0x140b3fcb0
00B3FBB6  B8 00 00 10 00                  mov eax, 0x100000
00B3FBBB  3B F0                           cmp esi, eax
00B3FBBD  0F 46 44 24 40                  cmovbe eax, dword ptr [rsp + 0x40]
00B3FBC2  44 8B F0                        mov r14d, eax
00B3FBC5  8B D0                           mov edx, eax
00B3FBC7  B9 40 00 00 00                  mov ecx, 0x40
00B3FBCC  41 B8 4B 53 4E 70               mov r8d, 0x704e534b
00B3FBD2  E8 19 25 04 00                  call 0x140b820f0
00B3FBD7  48 8B D8                        mov rbx, rax
00B3FBDA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B3FBDF  48 85 C0                        test rax, rax
00B3FBE2  75 0A                           jne 0x140b3fbee
00B3FBE4  BF 17 00 00 C0                  mov edi, 0xc0000017
00B3FBE9  E9 3B 01 00 00                  jmp 0x140b3fd29
00B3FBEE  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00B3FBF3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3FBF8  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00B3FBFD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3FC02  45 33 C9                        xor r9d, r9d
00B3FC05  45 8A C5                        mov r8b, r13b
00B3FC08  8B D7                           mov edx, edi
00B3FC0A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00B3FC12  E8 A1 37 E1 FF                  call 0x1409533b8
00B3FC17  8B F8                           mov edi, eax
00B3FC19  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FC1D  85 C0                           test eax, eax
00B3FC1F  79 0F                           jns 0x140b3fc30
00B3FC21  33 D2                           xor edx, edx
00B3FC23  48 8B CB                        mov rcx, rbx
00B3FC26  E8 45 2C 04 00                  call 0x140b82870
00B3FC2B  E9 14 02 00 00                  jmp 0x140b3fe44
00B3FC30  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00B3FC35  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00B3FC3D  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00B3FC42  45 8B C6                        mov r8d, r14d
00B3FC45  48 8B D3                        mov rdx, rbx
00B3FC48  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00B3FC4D  E8 EA 14 BD FF                  call 0x14071113c
00B3FC52  8B F8                           mov edi, eax
00B3FC54  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FC58  85 C0                           test eax, eax
00B3FC5A  78 3B                           js 0x140b3fc97
00B3FC5C  39 74 24 38                     cmp dword ptr [rsp + 0x38], esi
00B3FC60  76 0B                           jbe 0x140b3fc6d
00B3FC62  BF 01 00 00 C0                  mov edi, 0xc0000001
00B3FC67  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00B3FC6B  EB 2A                           jmp 0x140b3fc97
00B3FC6D  BA 19 00 00 00                  mov edx, 0x19
00B3FC72  8B C8                           mov ecx, eax
00B3FC74  E8 17 3C DC FF                  call 0x140903890
00B3FC79  90                              nop
00B3FC7A  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
00B3FC7F  48 8B D3                        mov rdx, rbx
00B3FC82  49 8B CC                        mov rcx, r12
00B3FC85  E8 B6 6B B8 FF                  call 0x1406c6840
00B3FC8A  EB 0B                           jmp 0x140b3fc97
00B3FC8C  8B F8                           mov edi, eax
00B3FC8E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FC92  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00B3FC97  33 D2                           xor edx, edx
00B3FC99  48 8B CB                        mov rcx, rbx
00B3FC9C  E8 CF 2B 04 00                  call 0x140b82870
00B3FCA1  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00B3FCA6  E8 AD F5 75 FF                  call 0x14029f258
00B3FCAB  E9 94 01 00 00                  jmp 0x140b3fe44
00B3FCB0  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3FCB5  E9 40 EB F2 FF                  jmp 0x140a6e7fa
00B3FCBA  83 EB 1E                        sub ebx, 0x1e
00B3FCBD  0F 84 5E 01 00 00               je 0x140b3fe21
00B3FCC3  83 EB 01                        sub ebx, 1
00B3FCC6  0F 84 3C 01 00 00               je 0x140b3fe08
00B3FCCC  83 EB 01                        sub ebx, 1
00B3FCCF  74 4C                           je 0x140b3fd1d
00B3FCD1  83 EB 01                        sub ebx, 1
00B3FCD4  0F 84 F6 00 00 00               je 0x140b3fdd0
00B3FCDA  83 EB 01                        sub ebx, 1
00B3FCDD  0F 84 16 01 00 00               je 0x140b3fdf9
00B3FCE3  83 EB 01                        sub ebx, 1
00B3FCE6  0F 84 A4 00 00 00               je 0x140b3fd90
00B3FCEC  83 EB 01                        sub ebx, 1
00B3FCEF  0F 84 CC 00 00 00               je 0x140b3fdc1
00B3FCF5  83 EB 01                        sub ebx, 1
00B3FCF8  74 38                           je 0x140b3fd32
00B3FCFA  83 FB 01                        cmp ebx, 1
00B3FCFD  75 17                           jne 0x140b3fd16
00B3FCFF  41 83 FF 10                     cmp r15d, 0x10
00B3FD03  0F 85 31 01 00 00               jne 0x140b3fe3a
00B3FD09  85 F6                           test esi, esi
00B3FD0B  0F 85 29 01 00 00               jne 0x140b3fe3a
00B3FD11  E9 E6 FD FF FF                  jmp 0x140b3fafc
00B3FD16  BF 03 00 00 C0                  mov edi, 0xc0000003
00B3FD1B  EB 0C                           jmp 0x140b3fd29
00B3FD1D  C7 05 35 9E 40 00 BB BB 1D DB   mov dword ptr [rip + 0x409e35], 0xdb1dbbbb
00B3FD27  33 FF                           xor edi, edi
00B3FD29  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00B3FD2D  E9 12 01 00 00                  jmp 0x140b3fe44
00B3FD32  85 F6                           test esi, esi
00B3FD34  0F 85 00 01 00 00               jne 0x140b3fe3a
00B3FD3A  41 8D 47 C0                     lea eax, [r15 - 0x40]
00B3FD3E  A9 F7 FF FF FF                  test eax, 0xfffffff7
00B3FD43  0F 85 F1 00 00 00               jne 0x140b3fe3a
00B3FD49  45 8B C7                        mov r8d, r15d
00B3FD4C  49 8B D6                        mov rdx, r14
00B3FD4F  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00B3FD57  E8 E4 6A B8 FF                  call 0x1406c6840
00B3FD5C  EB 06                           jmp 0x140b3fd64
00B3FD5E  8B F8                           mov edi, eax
00B3FD60  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FD64  85 FF                           test edi, edi
00B3FD66  0F 85 D8 00 00 00               jne 0x140b3fe44
00B3FD6C  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00B3FD74  E8 0F 05 A4 FF                  call 0x140580288
00B3FD79  8B F8                           mov edi, eax
00B3FD7B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FD7F  BA 1A 00 00 00                  mov edx, 0x1a
00B3FD84  8B C8                           mov ecx, eax
00B3FD86  E8 05 3B DC FF                  call 0x140903890
00B3FD8B  E9 B4 00 00 00                  jmp 0x140b3fe44
00B3FD90  83 FE 04                        cmp esi, 4
00B3FD93  0F 85 A1 00 00 00               jne 0x140b3fe3a
00B3FD99  8B 05 B5 9D 40 00               mov eax, dword ptr [rip + 0x409db5]
00B3FD9F  41 89 04 24                     mov dword ptr [r12], eax
00B3FDA3  EB 06                           jmp 0x140b3fdab
00B3FDA5  8B F8                           mov edi, eax
00B3FDA7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FDAB  85 FF                           test edi, edi
00B3FDAD  0F 88 91 00 00 00               js 0x140b3fe44
00B3FDB3  8A 05 A7 9D 40 00               mov al, byte ptr [rip + 0x409da7]
00B3FDB9  84 C0                           test al, al
00B3FDBB  0F 84 66 FF FF FF               je 0x140b3fd27
00B3FDC1  C7 05 89 9D 40 00 00 00 00 00   mov dword ptr [rip + 0x409d89], 0
00B3FDCB  E9 57 FF FF FF                  jmp 0x140b3fd27
00B3FDD0  83 FE 04                        cmp esi, 4
00B3FDD3  75 65                           jne 0x140b3fe3a
00B3FDD5  8B 05 7D 9D 40 00               mov eax, dword ptr [rip + 0x409d7d]
00B3FDDB  41 89 04 24                     mov dword ptr [r12], eax
00B3FDDF  EB 06                           jmp 0x140b3fde7
00B3FDE1  8B F8                           mov edi, eax
00B3FDE3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FDE7  85 FF                           test edi, edi
00B3FDE9  78 59                           js 0x140b3fe44
00B3FDEB  8A 05 5F 9D 40 00               mov al, byte ptr [rip + 0x409d5f]
00B3FDF1  84 C0                           test al, al
00B3FDF3  0F 84 2E FF FF FF               je 0x140b3fd27
00B3FDF9  C7 05 55 9D 40 00 00 00 00 00   mov dword ptr [rip + 0x409d55], 0
00B3FE03  E9 1F FF FF FF                  jmp 0x140b3fd27
00B3FE08  41 83 FF 01                     cmp r15d, 1
00B3FE0C  75 2C                           jne 0x140b3fe3a
00B3FE0E  41 8A 06                        mov al, byte ptr [r14]
00B3FE11  88 05 9B 5E 41 00               mov byte ptr [rip + 0x415e9b], al
00B3FE17  EB 2B                           jmp 0x140b3fe44
00B3FE19  8B F8                           mov edi, eax
00B3FE1B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FE1F  EB 23                           jmp 0x140b3fe44
00B3FE21  83 FE 01                        cmp esi, 1
00B3FE24  75 14                           jne 0x140b3fe3a
00B3FE26  8A 05 86 5E 41 00               mov al, byte ptr [rip + 0x415e86]
00B3FE2C  41 88 04 24                     mov byte ptr [r12], al
00B3FE30  EB 12                           jmp 0x140b3fe44
00B3FE32  8B F8                           mov edi, eax
00B3FE34  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3FE38  EB 0A                           jmp 0x140b3fe44
00B3FE3A  B8 04 00 00 C0                  mov eax, 0xc0000004
00B3FE3F  E9 B6 E9 F2 FF                  jmp 0x140a6e7fa
00B3FE44  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
00B3FE4C  48 85 C9                        test rcx, rcx
00B3FE4F  74 0C                           je 0x140b3fe5d
00B3FE51  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00B3FE55  89 01                           mov dword ptr [rcx], eax
00B3FE57  EB 04                           jmp 0x140b3fe5d
00B3FE59  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00B3FE5D  8B C7                           mov eax, edi
00B3FE5F  E9 96 E9 F2 FF                  jmp 0x140a6e7fa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B3F842(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10, unsigned int a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, unsigned int a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    unsigned int v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned int v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned int v_stack_p140;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p34;
    unsigned __int8 v_stack_p35;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p84;
    unsigned __int64 v_stack_p88;

    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B3F8FD;
    v_rdi = 0;
    v_stack_p30 = 0;
    if ((unsigned __int8)(v_r13) == 0) goto loc_00B3F8C8;
    if ((unsigned int)(v_r15) == 0) goto loc_00B3F888;
    if ((((unsigned __int8)(v_r14)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    if ((v_r14 + v_r15 * 1) > v_r13) goto loc_00B3F882;
    if ((v_r14 + v_r15 * 1) >= v_r14) goto loc_00B3F892;
loc_00B3F882:
    goto loc_00B3F892;
loc_00B3F888:
loc_00B3F892:
    result = *(unsigned __int8 *)(v_r13);
    if ((unsigned int)(v_rsi) != 0) {
        a2 = v_rsi;
        a3 = 4;
        a1 = v_r12;
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    if (a41 != 0) {
        if (a41 < v_r13) { v_r13 = a41; }
        result = *(unsigned int *)(v_r13);
        *(unsigned int *)(v_r13) = (unsigned int)(result);
    }
loc_00B3F8C8:
    goto loc_00B3F907;
loc_00B3F8FD:
loc_00B3F907:
    if (0 != 0) goto loc_00B3FE5D;
    if (((unsigned int)(v_rbx)) > 19) goto loc_00B3F9AD;
    if (((unsigned int)(v_rbx)) == 19) goto loc_00B3F9A3;
    if (((unsigned int)(v_rbx)) > 9) goto loc_00B3F972;
    if (((unsigned int)(v_rbx)) == 9) goto loc_00B3F9A3;
    if ((unsigned int)(v_rbx) == 0) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_00B3F995;
    if ((*(unsigned __int8 *)(v_rip + 4226218)) != 1) goto loc_00B3F968;
    result = DbgBreakPointWithStatus(v_rdi + 6, a2, a3, a4);
    goto loc_00B3FE44;
loc_00B3F968:
    goto loc_00B3FD29;
loc_00B3F972:
    v_rbx = (unsigned int)((v_rbx) - (10));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
loc_00B3F995:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00B3FD16;
loc_00B3F9A3:
loc_00B3F9AD:
    if (((unsigned int)(v_rbx)) > 29) goto loc_00B3FCBA;
    if (((unsigned int)(v_rbx)) == 29) goto loc_00B3FB0F;
    v_rbx = (unsigned int)((v_rbx) - (20));
    if (condition_is_equal) goto loc_00B3F9A3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAF5;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAEE;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FACB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAA6;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA83;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA4C;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA25;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00B3FD16;
    if (((unsigned int)(v_r15)) != ((unsigned int)(v_rbx))) goto loc_00B3FE3A;
    goto loc_00B3FE44;
loc_00B3FA25:
    if (((unsigned int)(v_rsi)) != 1) goto loc_00B3FE3A;
    result = ((*(unsigned __int8 *)(v_rip + 4285035)) == 0) ? 1 : 0;
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)(result);
    goto loc_00B3FE44;
loc_00B3FA4C:
    if (((unsigned int)(v_r15)) != 4) goto loc_00B3FE3A;
    v_stack_p3C = 0;
    v_stack_p3C = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
    goto loc_00B3FA71;
loc_00B3FA71:
    if ((unsigned int)((unsigned int)(0xC0000001ULL)) != 0) goto loc_00B3FE44;
    result = KdSetDbgPrintBufferSize((unsigned int)(*(unsigned int *)(v_r14)), a2, a3, a4);
    goto loc_00B3FB04;
loc_00B3FA83:
    if (((unsigned int)(v_rsi)) != 4) goto loc_00B3FE3A;
    *(unsigned int *)(v_r12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2928578)));
    goto loc_00B3FE44;
loc_00B3FAA6:
    if (((unsigned int)(v_r15)) != 1) goto loc_00B3FE3A;
    goto loc_00B3FE44;
loc_00B3FACB:
    if (((unsigned int)(v_rsi)) != 1) goto loc_00B3FE3A;
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4284871));
    goto loc_00B3FE44;
loc_00B3FAEE:
    result = KdDisableDebugger((unsigned int)(*(unsigned int *)(v_r14)), a2, a3, a4);
    goto loc_00B3FB04;
loc_00B3FAF5:
    result = KdEnableDebugger((unsigned int)(*(unsigned int *)(v_r14)), a2, a3, a4);
    goto loc_00B3FB04;
loc_00B3FAFC:
    result = ExpKdPullRemoteFileForUser(v_r14, a2, a3, a4);
loc_00B3FB04:
    v_stack_p30 = (unsigned int)(result);
    goto loc_00B3FE44;
loc_00B3FB0F:
    if (((unsigned int)(v_r15)) != 56) goto loc_00B3FE3A;
    if (((unsigned int)(v_rsi)) < 0x40000ULL) goto loc_00B3FE3A;
    a11 = v_xmm0;
    a13 = v_xmm1;
    a15 = v_xmm0;
    v_stack_p88 = v_xmm1;
    goto loc_00B3FB6D;
loc_00B3FB6D:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00B3FE44;
    if (a16 != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00B3FCB0;
    if ((unsigned int)((unsigned int)(v_stack_p84)) == 0) goto loc_00B3FCB0;
    if (((a11) & (0xFFFFFFFEULL)) != 0) goto loc_00B3FCB0;
    result = ((unsigned int)(v_stack_p84)) << (3);
    v_rdi = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) { v_rdi = (unsigned int)(result); }
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00B3FCB0;
    result = (unsigned int)(0x100000ULL);
    if (((unsigned int)(v_rsi)) <= ((unsigned int)((unsigned int)(0x100000ULL)))) { result = a8; }
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)(0x704E534BULL), a4);
    v_stack_p40 = result;
    if (result != 0) goto loc_00B3FBEE;
    goto loc_00B3FD29;
loc_00B3FBEE:
    v_stack_p28 = a10;
    v_stack_p20 = a9;
    a4 = 0;
    result = ExLockUserBuffer(a17, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), (unsigned __int8)(v_stack_p34), a4);
    v_stack_p30 = (unsigned int)(result);
    if (!sign_flag) goto loc_00B3FC30;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned __int8)(v_stack_p34), a4);
    goto loc_00B3FE44;
loc_00B3FC30:
    v_stack_p88 = a9;
    result = DbgkCaptureLiveDump(a11, result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a7);
    v_stack_p30 = (unsigned int)(result);
    if (sign_flag) goto loc_00B3FC97;
    if (a7 <= ((unsigned int)(v_rsi))) goto loc_00B3FC6D;
    v_stack_p30 = (unsigned int)((unsigned int)(0xC0000001ULL));
    goto loc_00B3FC97;
loc_00B3FC6D:
    result = EtwTiLogSyscallUsage((unsigned int)((unsigned int)(result)), 25, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a7);
    result = memcpy(v_r12, result, (unsigned int)(a7), a7);
    goto loc_00B3FC97;
loc_00B3FC97:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(a7), a7);
    result = ExUnlockUserBuffer(a10, a2, (unsigned int)(a7), a7);
    goto loc_00B3FE44;
loc_00B3FCB0:
loc_00B3FCBA:
    v_rbx = (unsigned int)((result) - (30));
    if (condition_is_equal) goto loc_00B3FE21;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FE08;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD1D;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDD0;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDF9;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD90;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDC1;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD32;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00B3FD16;
    if (((unsigned int)(v_r15)) != 16) goto loc_00B3FE3A;
    if ((unsigned int)(v_rsi) != 0) goto loc_00B3FE3A;
    goto loc_00B3FAFC;
loc_00B3FD16:
    goto loc_00B3FD29;
loc_00B3FD1D:
    *(unsigned int *)(v_rip + 4234805) = 0xDB1DBBBBULL;
loc_00B3FD27:
    v_rdi = 0;
loc_00B3FD29:
    v_stack_p30 = 0;
    goto loc_00B3FE44;
loc_00B3FD32:
    if ((unsigned int)(v_rsi) != 0) goto loc_00B3FE3A;
    if ((((unsigned int)(v_r15 - 64)) & (0xFFFFFFF7ULL)) != 0) goto loc_00B3FE3A;
    result = memcpy(a18, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r15)), a7);
    goto loc_00B3FD64;
loc_00B3FD64:
    if (0 != 0) goto loc_00B3FE44;
    result = DbgkCaptureLiveKernelDump(a18, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r15)), a7);
    v_stack_p30 = (unsigned int)(result);
    result = EtwTiLogSyscallUsage((unsigned int)((unsigned int)(result)), 26, (unsigned int)((unsigned int)(v_r15)), a7);
    goto loc_00B3FE44;
loc_00B3FD90:
    if (((unsigned int)(v_rsi)) != 4) goto loc_00B3FE3A;
    *(unsigned int *)(v_r12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4234677)));
    goto loc_00B3FDAB;
loc_00B3FDAB:
    if (sign_flag) goto loc_00B3FE44;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4234663)) == 0) goto loc_00B3FD27;
loc_00B3FDC1:
    *(unsigned int *)(v_rip + 4234633) = 0;
    goto loc_00B3FD27;
loc_00B3FDD0:
    if (((unsigned int)(v_rsi)) != 4) goto loc_00B3FE3A;
    *(unsigned int *)(v_r12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4234621)));
    goto loc_00B3FDE7;
loc_00B3FDE7:
    if (sign_flag) goto loc_00B3FE44;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4234591)) == 0) goto loc_00B3FD27;
loc_00B3FDF9:
    *(unsigned int *)(v_rip + 4234581) = 0;
    goto loc_00B3FD27;
loc_00B3FE08:
    if (((unsigned int)(v_r15)) != 1) goto loc_00B3FE3A;
    *(unsigned __int8 *)(v_rip + 4284059) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(result))));
    goto loc_00B3FE44;
loc_00B3FE21:
    if (((unsigned int)(v_rsi)) != 1) goto loc_00B3FE3A;
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4284038));
    goto loc_00B3FE44;
loc_00B3FE3A:
loc_00B3FE44:
    if (a41 == 0) goto loc_00B3FE5D;
    *(unsigned int *)(a41) = (unsigned int)((unsigned int)(a7));
    goto loc_00B3FE5D;
loc_00B3FE5D:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B3F842(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10, uint32_t Arg11, uint64_t Arg12, int64_t Arg13, uint64_t Arg14, int64_t Arg15, uint32_t Arg16, int64_t Arg17, int64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, int64_t Arg41)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    uint32_t v_stack_p120;
    uint64_t v_stack_p128;
    uint32_t v_stack_p130;
    uint64_t v_stack_p138;
    uint32_t v_stack_p140;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p34;
    uint8_t v_stack_p35;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;
    uint32_t v_stack_p84;
    uint64_t v_stack_p88;

    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B3F8FD;
    local_rdi = 0;
    v_stack_p30 = 0;
    if ((uint8_t)(local_r13) == 0) goto loc_00B3F8C8;
    if ((uint32_t)(local_r15) == 0) goto loc_00B3F888;
    if ((((uint8_t)(local_r14)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    if ((local_r14 + local_r15 * 1) > local_r13) goto loc_00B3F882;
    if ((local_r14 + local_r15 * 1) >= local_r14) goto loc_00B3F892;
loc_00B3F882:
    goto loc_00B3F892;
loc_00B3F888:
loc_00B3F892:
    result = *(uint8_t *)(local_r13);
    if ((uint32_t)(local_rsi) != 0) {
        Arg2 = local_rsi;
        Arg3 = 4;
        Arg1 = local_r12;
        result = ProbeForWrite(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg41 != 0) {
        if (Arg41 < local_r13) { local_r13 = Arg41; }
        result = *(uint32_t *)(local_r13);
        *(uint32_t *)(local_r13) = (uint32_t)(result);
    }
loc_00B3F8C8:
    goto loc_00B3F907;
loc_00B3F8FD:
loc_00B3F907:
    if (0 != 0) goto loc_00B3FE5D;
    if (((uint32_t)(local_rbx)) > 19) goto loc_00B3F9AD;
    if (((uint32_t)(local_rbx)) == 19) goto loc_00B3F9A3;
    if (((uint32_t)(local_rbx)) > 9) goto loc_00B3F972;
    if (((uint32_t)(local_rbx)) == 9) goto loc_00B3F9A3;
    if ((uint32_t)(local_rbx) == 0) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_00B3F995;
    if ((*(uint8_t *)(v_rip + 0x407CAA)) != 1) goto loc_00B3F968;
    result = DbgBreakPointWithStatus(local_rdi + 6, Arg2, Arg3, Arg4);
    goto loc_00B3FE44;
loc_00B3F968:
    goto loc_00B3FD29;
loc_00B3F972:
    local_rbx = (uint32_t)((local_rbx) - (10));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
loc_00B3F995:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3F9A3;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00B3FD16;
loc_00B3F9A3:
loc_00B3F9AD:
    if (((uint32_t)(local_rbx)) > 29) goto loc_00B3FCBA;
    if (((uint32_t)(local_rbx)) == 29) goto loc_00B3FB0F;
    local_rbx = (uint32_t)((local_rbx) - (20));
    if (condition_is_equal) goto loc_00B3F9A3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAF5;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAEE;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FACB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FAA6;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA83;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA4C;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FA25;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00B3FD16;
    if (((uint32_t)(local_r15)) != ((uint32_t)(local_rbx))) goto loc_00B3FE3A;
    goto loc_00B3FE44;
loc_00B3FA25:
    if (((uint32_t)(local_rsi)) != 1) goto loc_00B3FE3A;
    result = ((*(uint8_t *)(v_rip + 0x41626B)) == 0) ? 1 : 0;
    *(uint8_t *)(local_r12) = (uint8_t)(result);
    goto loc_00B3FE44;
loc_00B3FA4C:
    if (((uint32_t)(local_r15)) != 4) goto loc_00B3FE3A;
    v_stack_p3C = 0;
    v_stack_p3C = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
    goto loc_00B3FA71;
loc_00B3FA71:
    if ((uint32_t)((uint32_t)(0xC0000001ULL)) != 0) goto loc_00B3FE44;
    result = KdSetDbgPrintBufferSize((uint32_t)(*(uint32_t *)(local_r14)), Arg2, Arg3, Arg4);
    goto loc_00B3FB04;
loc_00B3FA83:
    if (((uint32_t)(local_rsi)) != 4) goto loc_00B3FE3A;
    *(uint32_t *)(local_r12) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2CAFC2)));
    goto loc_00B3FE44;
loc_00B3FAA6:
    if (((uint32_t)(local_r15)) != 1) goto loc_00B3FE3A;
    goto loc_00B3FE44;
loc_00B3FACB:
    if (((uint32_t)(local_rsi)) != 1) goto loc_00B3FE3A;
    *(uint8_t *)(local_r12) = (uint8_t)(*(uint8_t *)(v_rip + 0x4161C7));
    goto loc_00B3FE44;
loc_00B3FAEE:
    result = KdDisableDebugger((uint32_t)(*(uint32_t *)(local_r14)), Arg2, Arg3, Arg4);
    goto loc_00B3FB04;
loc_00B3FAF5:
    result = KdEnableDebugger((uint32_t)(*(uint32_t *)(local_r14)), Arg2, Arg3, Arg4);
    goto loc_00B3FB04;
loc_00B3FAFC:
    result = ExpKdPullRemoteFileForUser(local_r14, Arg2, Arg3, Arg4);
loc_00B3FB04:
    v_stack_p30 = (uint32_t)(result);
    goto loc_00B3FE44;
loc_00B3FB0F:
    if (((uint32_t)(local_r15)) != 56) goto loc_00B3FE3A;
    if (((uint32_t)(local_rsi)) < 0x40000ULL) goto loc_00B3FE3A;
    Arg11 = v_xmm0;
    Arg13 = v_xmm1;
    Arg15 = v_xmm0;
    v_stack_p88 = v_xmm1;
    goto loc_00B3FB6D;
loc_00B3FB6D:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00B3FE44;
    if (Arg16 != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00B3FCB0;
    if ((uint32_t)((uint32_t)(v_stack_p84)) == 0) goto loc_00B3FCB0;
    if (((Arg11) & (0xFFFFFFFEULL)) != 0) goto loc_00B3FCB0;
    result = ((uint32_t)(v_stack_p84)) << (3);
    local_rdi = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) { local_rdi = (uint32_t)(result); }
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00B3FCB0;
    result = (uint32_t)(0x100000ULL);
    if (((uint32_t)(local_rsi)) <= ((uint32_t)((uint32_t)(0x100000ULL)))) { result = Arg8; }
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)(0x704E534BULL), Arg4);
    v_stack_p40 = result;
    if (result != 0) goto loc_00B3FBEE;
    goto loc_00B3FD29;
loc_00B3FBEE:
    v_stack_p28 = Arg10;
    v_stack_p20 = Arg9;
    Arg4 = 0;
    result = ExLockUserBuffer(Arg17, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), (uint8_t)(v_stack_p34), Arg4);
    v_stack_p30 = (uint32_t)(result);
    if (!sign_flag) goto loc_00B3FC30;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint8_t)(v_stack_p34), Arg4);
    goto loc_00B3FE44;
loc_00B3FC30:
    v_stack_p88 = Arg9;
    result = DbgkCaptureLiveDump(Arg11, result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg7);
    v_stack_p30 = (uint32_t)(result);
    if (sign_flag) goto loc_00B3FC97;
    if (Arg7 <= ((uint32_t)(local_rsi))) goto loc_00B3FC6D;
    v_stack_p30 = (uint32_t)((uint32_t)(0xC0000001ULL));
    goto loc_00B3FC97;
loc_00B3FC6D:
    result = EtwTiLogSyscallUsage((uint32_t)((uint32_t)(result)), 25, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg7);
    result = memcpy(local_r12, result, (uint32_t)(Arg7), Arg7);
    goto loc_00B3FC97;
loc_00B3FC97:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(Arg7), Arg7);
    result = ExUnlockUserBuffer(Arg10, Arg2, (uint32_t)(Arg7), Arg7);
    goto loc_00B3FE44;
loc_00B3FCB0:
loc_00B3FCBA:
    local_rbx = (uint32_t)((result) - (30));
    if (condition_is_equal) goto loc_00B3FE21;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FE08;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD1D;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDD0;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDF9;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD90;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FDC1;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00B3FD32;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00B3FD16;
    if (((uint32_t)(local_r15)) != 16) goto loc_00B3FE3A;
    if ((uint32_t)(local_rsi) != 0) goto loc_00B3FE3A;
    goto loc_00B3FAFC;
loc_00B3FD16:
    goto loc_00B3FD29;
loc_00B3FD1D:
    *(uint32_t *)(v_rip + 0x409E35) = 0xDB1DBBBBULL;
loc_00B3FD27:
    local_rdi = 0;
loc_00B3FD29:
    v_stack_p30 = 0;
    goto loc_00B3FE44;
loc_00B3FD32:
    if ((uint32_t)(local_rsi) != 0) goto loc_00B3FE3A;
    if ((((uint32_t)(local_r15 - 64)) & (0xFFFFFFF7ULL)) != 0) goto loc_00B3FE3A;
    result = memcpy(Arg18, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r15)), Arg7);
    goto loc_00B3FD64;
loc_00B3FD64:
    if (0 != 0) goto loc_00B3FE44;
    result = DbgkCaptureLiveKernelDump(Arg18, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r15)), Arg7);
    v_stack_p30 = (uint32_t)(result);
    result = EtwTiLogSyscallUsage((uint32_t)((uint32_t)(result)), 26, (uint32_t)((uint32_t)(local_r15)), Arg7);
    goto loc_00B3FE44;
loc_00B3FD90:
    if (((uint32_t)(local_rsi)) != 4) goto loc_00B3FE3A;
    *(uint32_t *)(local_r12) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x409DB5)));
    goto loc_00B3FDAB;
loc_00B3FDAB:
    if (sign_flag) goto loc_00B3FE44;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x409DA7)) == 0) goto loc_00B3FD27;
loc_00B3FDC1:
    *(uint32_t *)(v_rip + 0x409D89) = 0;
    goto loc_00B3FD27;
loc_00B3FDD0:
    if (((uint32_t)(local_rsi)) != 4) goto loc_00B3FE3A;
    *(uint32_t *)(local_r12) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x409D7D)));
    goto loc_00B3FDE7;
loc_00B3FDE7:
    if (sign_flag) goto loc_00B3FE44;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x409D5F)) == 0) goto loc_00B3FD27;
loc_00B3FDF9:
    *(uint32_t *)(v_rip + 0x409D55) = 0;
    goto loc_00B3FD27;
loc_00B3FE08:
    if (((uint32_t)(local_r15)) != 1) goto loc_00B3FE3A;
    *(uint8_t *)(v_rip + 0x415E9B) = (uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(result))));
    goto loc_00B3FE44;
loc_00B3FE21:
    if (((uint32_t)(local_rsi)) != 1) goto loc_00B3FE3A;
    *(uint8_t *)(local_r12) = (uint8_t)(*(uint8_t *)(v_rip + 0x415E86));
    goto loc_00B3FE44;
loc_00B3FE3A:
loc_00B3FE44:
    if (Arg41 == 0) goto loc_00B3FE5D;
    *(uint32_t *)(Arg41) = (uint32_t)((uint32_t)(Arg7));
    goto loc_00B3FE5D;
loc_00B3FE5D:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3F842&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
