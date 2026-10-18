# EtwQueryPerformanceTraceInformation

- RVA: `0x00AF28A4`–`0x00AF2FE6` (길이 `1,858` bytes)
- VA: `0x0000000140AF28A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D353C`
- 디코드: `442`개 명령, `1,858/1,858` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00AF28E4` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00AF29D3` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00AF29E7` → [EtwpReferenceLoggerSecurityDescriptor](../8C/EtwpReferenceLoggerSecurityDescriptor_function_008C0810.md) (function, `0x008C0810`)
- `0x00AF2A15` → [SeQuerySecurityDescriptorInfo](../87/SeQuerySecurityDescriptorInfo_function_00872820.md) (function, `0x00872820`)
- `0x00AF2A30` → [EtwpDereferenceLoggerSecurityDescriptor](../A3/EtwpDereferenceLoggerSecurityDescriptor_function_00A34D94.md) (function, `0x00A34D94`)
- `0x00AF2A79` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00AF2ADE` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00AF2B27` → [EtwpMapEnableFlags](../A4/EtwpMapEnableFlags_function_00A46450.md) (function, `0x00A46450`)
- `0x00AF2B42` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00AF2B47` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF2BC8` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00AF2BE6` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00AF2BF6` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00AF2BFB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF2C18` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x00AF2C5F` → [RtlFindSetBits](../../text/3F/RtlFindSetBits_function_003F0610.md) (function, `0x003F0610`)
- `0x00AF2D14` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00AF2D38` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF2D4F` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)
- `0x00AF2D5F` → [EtwpGetPmcProfileSource](../AD/EtwpGetPmcProfileSource_function_00ADC6EC.md) (function, `0x00ADC6EC`)
- `0x00AF2D7C` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF2DBC` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00AF2DE9` → [EtwpCheckSystemTraceAccess](../A8/EtwpCheckSystemTraceAccess_function_00A8DE44.md) (function, `0x00A8DE44`)
- `0x00AF2E38` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF2E51` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00AF2E72` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF2E8F` → [PsGetNextProcess](../91/PsGetNextProcess_function_0091C900.md) (function, `0x0091C900`)
- `0x00AF2EB5` → [EtwpUMGLEnabled](../7B/EtwpUMGLEnabled_function_007B8E44.md) (function, `0x007B8E44`)
- `0x00AF2EC1` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x00AF2EE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF2F49` → [EtwpGetSoftRestartInformation](../7B/EtwpGetSoftRestartInformation_function_007BEC70.md) (function, `0x007BEC70`)
- `0x00AF2F89` → [RtlWriteULongToUser](../70/RtlWriteULongToUser_function_00705E8C.md) (function, `0x00705E8C`)
- `0x00AF2FAB` → [RtlWriteULongToUser](../70/RtlWriteULongToUser_function_00705E8C.md) (function, `0x00705E8C`)
- `0x00AF2FBF` → [EtwpQueryCoverageSamplerInformation](../95/EtwpQueryCoverageSamplerInformation_function_0095D2D8.md) (function, `0x0095D2D8`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A583FD`

### Static image references
- `0x00AF2954` → RVA `0x00FC5150` (`ALMOSTRO`; read)
- `0x00AF295D` → RVA `0x00FC5154` (`ALMOSTRO`; read)
- `0x00AF2966` → RVA `0x00FC5158` (`ALMOSTRO`; read)
- `0x00AF2975` → RVA `0x00FC50D4` (`ALMOSTRO`; read)
- `0x00AF2A55` → RVA `0x00E0EB28` (`.data`; read)
- `0x00AF2D21` → RVA `0x00E00638` (`.data`; read)
- `0x00AF2E07` → RVA `0x00EFF940` (`.data`; read)
- `0x00AF2F1E` → RVA `0x00E0EB10` (`.data`; read)
- `0x00AF2F27` → RVA `0x00E0EB18` (`.data`; read)
- `0x00AF2F30` → RVA `0x00E0EB14` (`.data`; read)
- `0x00AF2F78` → RVA `0x00FC6DA0` (`ALMOSTRO`; read)
- `0x00AF2F9A` → RVA `0x00FC6D40` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00AF28E4` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00AF2A79` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00AF2B47` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF2BFB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF2C18` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x00AF2C5F` → [RtlFindSetBits](../../text/3F/RtlFindSetBits_function_003F0610.md) (`PAGE` → `.text`)
  - `0x00AF2D38` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF2D4F` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
  - `0x00AF2D7C` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF2E38` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF2E72` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF2EC1` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x00AF2EE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF28A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AF28A9  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AF28AE  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
00AF28B3  57                              push rdi
00AF28B4  41 54                           push r12
00AF28B6  41 55                           push r13
00AF28B8  41 56                           push r14
00AF28BA  41 57                           push r15
00AF28BC  48 83 EC 60                     sub rsp, 0x60
00AF28C0  4D 8B E1                        mov r12, r9
00AF28C3  44 8B F2                        mov r14d, edx
00AF28C6  48 8B F1                        mov rsi, rcx
00AF28C9  45 33 FF                        xor r15d, r15d
00AF28CC  41 8B FF                        mov edi, r15d
00AF28CF  83 FA 04                        cmp edx, 4
00AF28D2  73 0A                           jae 0x140af28de
00AF28D4  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AF28D9  E9 ED 06 00 00                  jmp 0x140af2fcb
00AF28DE  8B 19                           mov ebx, dword ptr [rcx]
00AF28E0  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00AF28E4  E8 07 B9 80 FF                  call 0x1402fe1f0
00AF28E9  4C 8B A8 40 03 00 00            mov r13, qword ptr [rax + 0x340]
00AF28F0  83 FB 12                        cmp ebx, 0x12
00AF28F3  0F 8F 57 06 00 00               jg 0x140af2f50
00AF28F9  0F 84 44 06 00 00               je 0x140af2f43
00AF28FF  83 FB 06                        cmp ebx, 6
00AF2902  0F 8F 9B 03 00 00               jg 0x140af2ca3
00AF2908  0F 84 6A 02 00 00               je 0x140af2b78
00AF290E  85 DB                           test ebx, ebx
00AF2910  0F 84 40 02 00 00               je 0x140af2b56
00AF2916  83 EB 01                        sub ebx, 1
00AF2919  0F 84 7B 01 00 00               je 0x140af2a9a
00AF291F  83 EB 01                        sub ebx, 1
00AF2922  0F 84 40 01 00 00               je 0x140af2a68
00AF2928  83 EB 01                        sub ebx, 1
00AF292B  0F 84 13 01 00 00               je 0x140af2a44
00AF2931  83 EB 01                        sub ebx, 1
00AF2934  74 52                           je 0x140af2988
00AF2936  83 FB 01                        cmp ebx, 1
00AF2939  0F 85 1B 06 00 00               jne 0x140af2f5a
00AF293F  41 C7 01 14 00 00 00            mov dword ptr [r9], 0x14
00AF2946  8D 42 F0                        lea eax, [rdx - 0x10]
00AF2949  A9 FB FF FF FF                  test eax, 0xfffffffb
00AF294E  0F 85 1D 06 00 00               jne 0x140af2f71
00AF2954  8B 05 F6 27 4D 00               mov eax, dword ptr [rip + 0x4d27f6]
00AF295A  89 46 04                        mov dword ptr [rsi + 4], eax
00AF295D  8B 05 F1 27 4D 00               mov eax, dword ptr [rip + 0x4d27f1]
00AF2963  89 46 08                        mov dword ptr [rsi + 8], eax
00AF2966  8B 05 EC 27 4D 00               mov eax, dword ptr [rip + 0x4d27ec]
00AF296C  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00AF296F  41 83 FE 14                     cmp r14d, 0x14
00AF2973  75 09                           jne 0x140af297e
00AF2975  8B 05 59 27 4D 00               mov eax, dword ptr [rip + 0x4d2759]
00AF297B  89 46 10                        mov dword ptr [rsi + 0x10], eax
00AF297E  E9 7D 02 00 00                  jmp 0x140af2c00
00AF2983  E9 43 06 00 00                  jmp 0x140af2fcb
00AF2988  41 C7 01 18 00 00 00            mov dword ptr [r9], 0x18
00AF298F  41 83 FE 18                     cmp r14d, 0x18
00AF2993  0F 82 D8 05 00 00               jb 0x140af2f71
00AF2999  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00AF299D  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00AF29A2  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AF29A5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AF29A9  0F B7 D1                        movzx edx, cx
00AF29AC  81 FA FF FF 00 00               cmp edx, 0xffff
00AF29B2  75 08                           jne 0x140af29bc
00AF29B4  41 0F B6 95 98 11 00 00         movzx edx, byte ptr [r13 + 0x1198]
00AF29BC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF29C5  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF29CC  90                              nop
00AF29CD  45 33 C0                        xor r8d, r8d
00AF29D0  49 8B CD                        mov rcx, r13
00AF29D3  E8 48 FF E3 FF                  call 0x140932920
00AF29D8  4C 8B E8                        mov r13, rax
00AF29DB  48 85 C0                        test rax, rax
00AF29DE  0F 84 EA 03 00 00               je 0x140af2dce
00AF29E4  48 8B C8                        mov rcx, rax
00AF29E7  E8 24 DE DC FF                  call 0x1408c0810
00AF29EC  48 8B D8                        mov rbx, rax
00AF29EF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF29F4  41 8D 46 F0                     lea eax, [r14 - 0x10]
00AF29F8  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
00AF29FF  48 8D 56 10                     lea rdx, [rsi + 0x10]
00AF2A03  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00AF2A08  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
00AF2A10  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00AF2A15  E8 06 FE D7 FF                  call 0x140872820
00AF2A1A  8B F8                           mov edi, eax
00AF2A1C  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
00AF2A23  83 C0 10                        add eax, 0x10
00AF2A26  41 89 04 24                     mov dword ptr [r12], eax
00AF2A2A  48 8B D3                        mov rdx, rbx
00AF2A2D  49 8B CD                        mov rcx, r13
00AF2A30  E8 5F 23 F4 FF                  call 0x140a34d94
00AF2A35  33 D2                           xor edx, edx
00AF2A37  49 8B CD                        mov rcx, r13
00AF2A3A  E9 B7 01 00 00                  jmp 0x140af2bf6
00AF2A3F  E9 87 05 00 00                  jmp 0x140af2fcb
00AF2A44  41 C7 01 08 00 00 00            mov dword ptr [r9], 8
00AF2A4B  41 83 FE 08                     cmp r14d, 8
00AF2A4F  0F 85 1C 05 00 00               jne 0x140af2f71
00AF2A55  8B 05 CD C0 31 00               mov eax, dword ptr [rip + 0x31c0cd]
00AF2A5B  89 46 04                        mov dword ptr [rsi + 4], eax
00AF2A5E  E9 9D 01 00 00                  jmp 0x140af2c00
00AF2A63  E9 63 05 00 00                  jmp 0x140af2fcb
00AF2A68  41 C7 01 10 00 00 00            mov dword ptr [r9], 0x10
00AF2A6F  41 83 FE 10                     cmp r14d, 0x10
00AF2A73  0F 85 F8 04 00 00               jne 0x140af2f71
00AF2A79  E8 72 B7 80 FF                  call 0x1402fe1f0
00AF2A7E  48 8B 80 40 03 00 00            mov rax, qword ptr [rax + 0x340]
00AF2A85  48 8B 80 38 11 00 00            mov rax, qword ptr [rax + 0x1138]
00AF2A8C  48 89 46 08                     mov qword ptr [rsi + 8], rax
00AF2A90  E9 6B 01 00 00                  jmp 0x140af2c00
00AF2A95  E9 31 05 00 00                  jmp 0x140af2fcb
00AF2A9A  41 C7 01 30 00 00 00            mov dword ptr [r9], 0x30
00AF2AA1  41 83 FE 30                     cmp r14d, 0x30
00AF2AA5  0F 85 C6 04 00 00               jne 0x140af2f71
00AF2AAB  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00AF2AAF  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AF2AB4  0F B7 D0                        movzx edx, ax
00AF2AB7  81 FA FF FF 00 00               cmp edx, 0xffff
00AF2ABD  75 08                           jne 0x140af2ac7
00AF2ABF  41 0F B6 95 98 11 00 00         movzx edx, byte ptr [r13 + 0x1198]
00AF2AC7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF2AD0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF2AD7  90                              nop
00AF2AD8  41 B0 01                        mov r8b, 1
00AF2ADB  49 8B CD                        mov rcx, r13
00AF2ADE  E8 3D FE E3 FF                  call 0x140932920
00AF2AE3  48 8B D8                        mov rbx, rax
00AF2AE6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF2AEB  48 85 C0                        test rax, rax
00AF2AEE  0F 84 DA 02 00 00               je 0x140af2dce
00AF2AF4  F7 40 0C 00 00 00 02            test dword ptr [rax + 0xc], 0x2000000
00AF2AFB  74 40                           je 0x140af2b3d
00AF2AFD  0F B6 80 32 03 00 00            movzx eax, byte ptr [rax + 0x332]
00AF2B04  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00AF2B08  48 C1 E0 05                     shl rax, 5
00AF2B0C  42 0F 10 84 28 CC 11 00 00      movups xmm0, xmmword ptr [rax + r13 + 0x11cc]
00AF2B15  0F 11 01                        movups xmmword ptr [rcx], xmm0
00AF2B18  42 0F 10 8C 28 DC 11 00 00      movups xmm1, xmmword ptr [rax + r13 + 0x11dc]
00AF2B21  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00AF2B25  33 D2                           xor edx, edx
00AF2B27  E8 24 39 F5 FF                  call 0x140a46450
00AF2B2C  E9 C3 02 00 00                  jmp 0x140af2df4
00AF2B31  8B F8                           mov edi, eax
00AF2B33  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00AF2B38  E9 B7 02 00 00                  jmp 0x140af2df4
00AF2B3D  B2 01                           mov dl, 1
00AF2B3F  48 8B C8                        mov rcx, rax
00AF2B42  E8 19 16 F1 FF                  call 0x140a04160
00AF2B47  E8 64 AD 76 FF                  call 0x14025d8b0
00AF2B4C  E9 83 FD FF FF                  jmp 0x140af28d4
00AF2B51  E9 75 04 00 00                  jmp 0x140af2fcb
00AF2B56  41 C7 01 08 00 00 00            mov dword ptr [r9], 8
00AF2B5D  41 83 FE 08                     cmp r14d, 8
00AF2B61  0F 85 0A 04 00 00               jne 0x140af2f71
00AF2B67  C7 46 04 55 00 00 00            mov dword ptr [rsi + 4], 0x55
00AF2B6E  E9 8D 00 00 00                  jmp 0x140af2c00
00AF2B73  E9 53 04 00 00                  jmp 0x140af2fcb
00AF2B78  41 8B DF                        mov ebx, r15d
00AF2B7B  89 9C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ebx
00AF2B82  48 8D 46 10                     lea rax, [rsi + 0x10]
00AF2B86  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF2B8B  41 83 FE 10                     cmp r14d, 0x10
00AF2B8F  0F 82 DC 03 00 00               jb 0x140af2f71
00AF2B95  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00AF2B99  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AF2B9E  0F B7 D0                        movzx edx, ax
00AF2BA1  81 FA FF FF 00 00               cmp edx, 0xffff
00AF2BA7  75 08                           jne 0x140af2bb1
00AF2BA9  41 0F B6 95 98 11 00 00         movzx edx, byte ptr [r13 + 0x1198]
00AF2BB1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF2BBA  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF2BC1  90                              nop
00AF2BC2  41 B0 01                        mov r8b, 1
00AF2BC5  49 8B CD                        mov rcx, r13
00AF2BC8  E8 53 FD E3 FF                  call 0x140932920
00AF2BCD  48 8B F0                        mov rsi, rax
00AF2BD0  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AF2BD5  48 85 C0                        test rax, rax
00AF2BD8  0F 84 F0 01 00 00               je 0x140af2dce
00AF2BDE  48 8B D0                        mov rdx, rax
00AF2BE1  B9 01 00 00 00                  mov ecx, 1
00AF2BE6  E8 F5 DE DC FF                  call 0x1408c0ae0
00AF2BEB  8B F8                           mov edi, eax
00AF2BED  85 C0                           test eax, eax
00AF2BEF  79 16                           jns 0x140af2c07
00AF2BF1  48 8B CE                        mov rcx, rsi
00AF2BF4  B2 01                           mov dl, 1
00AF2BF6  E8 65 15 F1 FF                  call 0x140a04160
00AF2BFB  E8 B0 AC 76 FF                  call 0x14025d8b0
00AF2C00  8B C7                           mov eax, edi
00AF2C02  E9 C4 03 00 00                  jmp 0x140af2fcb
00AF2C07  8B 86 30 03 00 00               mov eax, dword ptr [rsi + 0x330]
00AF2C0D  84 C0                           test al, al
00AF2C0F  79 15                           jns 0x140af2c26
00AF2C11  48 8D 8E 10 04 00 00            lea rcx, [rsi + 0x410]
00AF2C18  E8 53 13 94 FF                  call 0x140433f70
00AF2C1D  8B D8                           mov ebx, eax
00AF2C1F  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
00AF2C26  8D 04 9D 10 00 00 00            lea eax, [rbx*4 + 0x10]
00AF2C2D  41 89 04 24                     mov dword ptr [r12], eax
00AF2C31  41 3B C6                        cmp eax, r14d
00AF2C34  77 5E                           ja 0x140af2c94
00AF2C36  41 8B DF                        mov ebx, r15d
00AF2C39  44 8B B4 24 98 00 00 00         mov r14d, dword ptr [rsp + 0x98]
00AF2C41  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00AF2C46  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00AF2C4A  41 3B DE                        cmp ebx, r14d
00AF2C4D  73 A2                           jae 0x140af2bf1
00AF2C4F  45 8D 47 01                     lea r8d, [r15 + 1]
00AF2C53  48 8D 8E 10 04 00 00            lea rcx, [rsi + 0x410]
00AF2C5A  BA 01 00 00 00                  mov edx, 1
00AF2C5F  E8 AC D9 8F FF                  call 0x1403f0610
00AF2C64  44 8B F8                        mov r15d, eax
00AF2C67  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AF2C6B  8B CB                           mov ecx, ebx
00AF2C6D  41 89 04 8C                     mov dword ptr [r12 + rcx*4], eax
00AF2C71  EB 1D                           jmp 0x140af2c90
00AF2C73  8B F8                           mov edi, eax
00AF2C75  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
00AF2C7A  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00AF2C7E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF2C83  44 8B B4 24 98 00 00 00         mov r14d, dword ptr [rsp + 0x98]
00AF2C8B  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00AF2C90  FF C3                           inc ebx
00AF2C92  EB B2                           jmp 0x140af2c46
00AF2C94  BF 23 00 00 C0                  mov edi, 0xc0000023
00AF2C99  E9 53 FF FF FF                  jmp 0x140af2bf1
00AF2C9E  E9 28 03 00 00                  jmp 0x140af2fcb
00AF2CA3  8B CB                           mov ecx, ebx
00AF2CA5  83 E9 07                        sub ecx, 7
00AF2CA8  0F 84 63 02 00 00               je 0x140af2f11
00AF2CAE  83 E9 01                        sub ecx, 1
00AF2CB1  0F 84 AE 01 00 00               je 0x140af2e65
00AF2CB7  83 E9 01                        sub ecx, 1
00AF2CBA  0F 84 A5 01 00 00               je 0x140af2e65
00AF2CC0  83 E9 01                        sub ecx, 1
00AF2CC3  0F 84 A0 00 00 00               je 0x140af2d69
00AF2CC9  83 E9 02                        sub ecx, 2
00AF2CCC  0F 84 87 00 00 00               je 0x140af2d59
00AF2CD2  83 F9 01                        cmp ecx, 1
00AF2CD5  0F 85 7F 02 00 00               jne 0x140af2f5a
00AF2CDB  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00AF2CE0  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00AF2CE5  41 83 FE 28                     cmp r14d, 0x28
00AF2CE9  0F 82 82 02 00 00               jb 0x140af2f71
00AF2CEF  41 83 C6 F8                     add r14d, -8
00AF2CF3  48 8D 4E 08                     lea rcx, [rsi + 8]
00AF2CF7  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AF2CFC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF2D01  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00AF2D06  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF2D0B  41 B9 01 00 00 00               mov r9d, 1
00AF2D11  41 8B D6                        mov edx, r14d
00AF2D14  E8 9F 06 E6 FF                  call 0x1409533b8
00AF2D19  85 C0                           test eax, eax
00AF2D1B  0F 88 AA 02 00 00               js 0x140af2fcb
00AF2D21  48 8B 05 10 D9 30 00            mov rax, qword ptr [rip + 0x30d910]
00AF2D28  4D 8B CC                        mov r9, r12
00AF2D2B  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00AF2D30  41 8B D6                        mov edx, r14d
00AF2D33  B9 14 00 00 00                  mov ecx, 0x14
00AF2D38  E8 93 7D BC FF                  call 0x1406baad0
00AF2D3D  8B F8                           mov edi, eax
00AF2D3F  4C 39 7C 24 38                  cmp qword ptr [rsp + 0x38], r15
00AF2D44  0F 84 B6 FE FF FF               je 0x140af2c00
00AF2D4A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AF2D4F  E8 04 C5 7A FF                  call 0x14029f258
00AF2D54  E9 A7 FE FF FF                  jmp 0x140af2c00
00AF2D59  4D 8B C4                        mov r8, r12
00AF2D5C  48 8B CE                        mov rcx, rsi
00AF2D5F  E8 88 99 FE FF                  call 0x140adc6ec
00AF2D64  E9 5B 02 00 00                  jmp 0x140af2fc4
00AF2D69  48 8D 46 10                     lea rax, [rsi + 0x10]
00AF2D6D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AF2D72  41 83 FE 10                     cmp r14d, 0x10
00AF2D76  0F 82 F5 01 00 00               jb 0x140af2f71
00AF2D7C  E8 5F 35 94 FF                  call 0x1404362e0
00AF2D81  84 C0                           test al, al
00AF2D83  0F 85 F2 00 00 00               jne 0x140af2e7b
00AF2D89  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00AF2D8D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF2D92  0F B7 D0                        movzx edx, ax
00AF2D95  81 FA FF FF 00 00               cmp edx, 0xffff
00AF2D9B  75 08                           jne 0x140af2da5
00AF2D9D  41 0F B6 95 98 11 00 00         movzx edx, byte ptr [r13 + 0x1198]
00AF2DA5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF2DAE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF2DB5  90                              nop
00AF2DB6  41 B0 01                        mov r8b, 1
00AF2DB9  49 8B CD                        mov rcx, r13
00AF2DBC  E8 5F FB E3 FF                  call 0x140932920
00AF2DC1  48 8B D8                        mov rbx, rax
00AF2DC4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF2DC9  48 85 C0                        test rax, rax
00AF2DCC  75 0A                           jne 0x140af2dd8
00AF2DCE  BF 96 02 00 C0                  mov edi, 0xc0000296
00AF2DD3  E9 23 FE FF FF                  jmp 0x140af2bfb
00AF2DD8  48 8B CB                        mov rcx, rbx
00AF2DDB  F7 40 0C 00 00 00 02            test dword ptr [rax + 0xc], 0x2000000
00AF2DE2  74 6B                           je 0x140af2e4f
00AF2DE4  BA 01 00 00 00                  mov edx, 1
00AF2DE9  E8 56 B0 F9 FF                  call 0x140a8de44
00AF2DEE  8B F8                           mov edi, eax
00AF2DF0  85 C0                           test eax, eax
00AF2DF2  79 08                           jns 0x140af2dfc
00AF2DF4  48 8B CB                        mov rcx, rbx
00AF2DF7  E9 F8 FD FF FF                  jmp 0x140af2bf4
00AF2DFC  0F B6 83 32 03 00 00            movzx eax, byte ptr [rbx + 0x332]
00AF2E03  48 8D 14 80                     lea rdx, [rax + rax*4]
00AF2E07  48 8D 0D 32 CB 40 00            lea rcx, [rip + 0x40cb32]
00AF2E0E  0F B7 04 91                     movzx eax, word ptr [rcx + rdx*4]
00AF2E12  8D 04 85 10 00 00 00            lea eax, [rax*4 + 0x10]
00AF2E19  41 89 04 24                     mov dword ptr [r12], eax
00AF2E1D  41 3B C6                        cmp eax, r14d
00AF2E20  77 26                           ja 0x140af2e48
00AF2E22  44 0F B7 04 91                  movzx r8d, word ptr [rcx + rdx*4]
00AF2E27  49 C1 E0 02                     shl r8, 2
00AF2E2B  48 83 C1 04                     add rcx, 4
00AF2E2F  48 8D 14 91                     lea rdx, [rcx + rdx*4]
00AF2E33  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF2E38  E8 03 3A BD FF                  call 0x1406c6840
00AF2E3D  EB B5                           jmp 0x140af2df4
00AF2E3F  8B F8                           mov edi, eax
00AF2E41  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00AF2E46  EB AC                           jmp 0x140af2df4
00AF2E48  BF 23 00 00 C0                  mov edi, 0xc0000023
00AF2E4D  EB A5                           jmp 0x140af2df4
00AF2E4F  B2 01                           mov dl, 1
00AF2E51  E8 0A 13 F1 FF                  call 0x140a04160
00AF2E56  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AF2E5B  E9 9B FD FF FF                  jmp 0x140af2bfb
00AF2E60  E9 66 01 00 00                  jmp 0x140af2fcb
00AF2E65  45 8B EF                        mov r13d, r15d
00AF2E68  41 83 FE 08                     cmp r14d, 8
00AF2E6C  0F 82 FF 00 00 00               jb 0x140af2f71
00AF2E72  E8 69 34 94 FF                  call 0x1404362e0
00AF2E77  84 C0                           test al, al
00AF2E79  74 0A                           je 0x140af2e85
00AF2E7B  B8 22 00 00 C0                  mov eax, 0xc0000022
00AF2E80  E9 46 01 00 00                  jmp 0x140af2fcb
00AF2E85  41 83 C6 FC                     add r14d, -4
00AF2E89  41 C1 EE 02                     shr r14d, 2
00AF2E8D  33 C9                           xor ecx, ecx
00AF2E8F  E8 6C 9A E2 FF                  call 0x14091c900
00AF2E94  48 8B F8                        mov rdi, rax
00AF2E97  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF2E9C  48 85 C0                        test rax, rax
00AF2E9F  74 53                           je 0x140af2ef4
00AF2EA1  F7 80 FC 05 00 00 00 10 00 00   test dword ptr [rax + 0x5fc], 0x1000
00AF2EAB  75 42                           jne 0x140af2eef
00AF2EAD  83 FB 09                        cmp ebx, 9
00AF2EB0  74 0C                           je 0x140af2ebe
00AF2EB2  48 8B C8                        mov rcx, rax
00AF2EB5  E8 8A 5F CC FF                  call 0x1407b8e44
00AF2EBA  84 C0                           test al, al
00AF2EBC  74 31                           je 0x140af2eef
00AF2EBE  48 8B CF                        mov rcx, rdi
00AF2EC1  E8 4A AA 94 FF                  call 0x14043d910
00AF2EC6  45 3B EE                        cmp r13d, r14d
00AF2EC9  73 21                           jae 0x140af2eec
00AF2ECB  41 8B CD                        mov ecx, r13d
00AF2ECE  89 44 8E 04                     mov dword ptr [rsi + rcx*4 + 4], eax
00AF2ED2  EB 18                           jmp 0x140af2eec
00AF2ED4  8B D8                           mov ebx, eax
00AF2ED6  BA 50 73 45 6E                  mov edx, 0x6e457350
00AF2EDB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AF2EE0  E8 FB 49 80 FF                  call 0x1402f78e0
00AF2EE5  8B C3                           mov eax, ebx
00AF2EE7  E9 DF 00 00 00                  jmp 0x140af2fcb
00AF2EEC  41 FF C5                        inc r13d
00AF2EEF  48 8B CF                        mov rcx, rdi
00AF2EF2  EB 9B                           jmp 0x140af2e8f
00AF2EF4  42 8D 04 AD 04 00 00 00         lea eax, [r13*4 + 4]
00AF2EFC  41 89 04 24                     mov dword ptr [r12], eax
00AF2F00  45 3B F5                        cmp r14d, r13d
00AF2F03  1B C0                           sbb eax, eax
00AF2F05  BF 23 00 00 C0                  mov edi, 0xc0000023
00AF2F0A  23 F8                           and edi, eax
00AF2F0C  E9 EF FC FF FF                  jmp 0x140af2c00
00AF2F11  41 C7 01 10 00 00 00            mov dword ptr [r9], 0x10
00AF2F18  41 83 FE 10                     cmp r14d, 0x10
00AF2F1C  75 53                           jne 0x140af2f71
00AF2F1E  8B 05 EC BB 31 00               mov eax, dword ptr [rip + 0x31bbec]
00AF2F24  89 46 04                        mov dword ptr [rsi + 4], eax
00AF2F27  8B 05 EB BB 31 00               mov eax, dword ptr [rip + 0x31bbeb]
00AF2F2D  89 46 08                        mov dword ptr [rsi + 8], eax
00AF2F30  8B 05 DE BB 31 00               mov eax, dword ptr [rip + 0x31bbde]
00AF2F36  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00AF2F39  E9 C2 FC FF FF                  jmp 0x140af2c00
00AF2F3E  E9 88 00 00 00                  jmp 0x140af2fcb
00AF2F43  4D 8B C4                        mov r8, r12
00AF2F46  48 8B CE                        mov rcx, rsi
00AF2F49  E8 22 BD CC FF                  call 0x1407bec70
00AF2F4E  EB 74                           jmp 0x140af2fc4
00AF2F50  83 FB 19                        cmp ebx, 0x19
00AF2F53  74 67                           je 0x140af2fbc
00AF2F55  83 FB 1C                        cmp ebx, 0x1c
00AF2F58  74 0A                           je 0x140af2f64
00AF2F5A  BF 02 00 00 C0                  mov edi, 0xc0000002
00AF2F5F  E9 9C FC FF FF                  jmp 0x140af2c00
00AF2F64  41 C7 01 0C 00 00 00            mov dword ptr [r9], 0xc
00AF2F6B  41 83 FE 0C                     cmp r14d, 0xc
00AF2F6F  74 07                           je 0x140af2f78
00AF2F71  B8 04 00 00 C0                  mov eax, 0xc0000004
00AF2F76  EB 53                           jmp 0x140af2fcb
00AF2F78  8B 05 22 3E 4D 00               mov eax, dword ptr [rip + 0x4d3e22]
00AF2F7E  48 8D 4E 04                     lea rcx, [rsi + 4]
00AF2F82  45 84 C0                        test r8b, r8b
00AF2F85  74 11                           je 0x140af2f98
00AF2F87  8B D0                           mov edx, eax
00AF2F89  E8 FE 2E C1 FF                  call 0x140705e8c
00AF2F8E  44 8A 84 24 A0 00 00 00         mov r8b, byte ptr [rsp + 0xa0]
00AF2F96  EB 02                           jmp 0x140af2f9a
00AF2F98  89 01                           mov dword ptr [rcx], eax
00AF2F9A  8B 05 A0 3D 4D 00               mov eax, dword ptr [rip + 0x4d3da0]
00AF2FA0  45 84 C0                        test r8b, r8b
00AF2FA3  74 0D                           je 0x140af2fb2
00AF2FA5  8B D0                           mov edx, eax
00AF2FA7  48 8D 4E 08                     lea rcx, [rsi + 8]
00AF2FAB  E8 DC 2E C1 FF                  call 0x140705e8c
00AF2FB0  EB 03                           jmp 0x140af2fb5
00AF2FB2  89 46 08                        mov dword ptr [rsi + 8], eax
00AF2FB5  E9 46 FC FF FF                  jmp 0x140af2c00
00AF2FBA  EB 0F                           jmp 0x140af2fcb
00AF2FBC  48 8B CE                        mov rcx, rsi
00AF2FBF  E8 14 A3 E6 FF                  call 0x14095d2d8
00AF2FC4  8B F8                           mov edi, eax
00AF2FC6  E9 35 FC FF FF                  jmp 0x140af2c00
00AF2FCB  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00AF2FD0  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00AF2FD4  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00AF2FD8  49 8B E3                        mov rsp, r11
00AF2FDB  41 5F                           pop r15
00AF2FDD  41 5E                           pop r14
00AF2FDF  41 5D                           pop r13
00AF2FE1  41 5C                           pop r12
00AF2FE3  5F                              pop rdi
00AF2FE4  C3                              ret
00AF2FE5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwQueryPerformanceTraceInformation(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = (unsigned __int8)(a3);
    v_rsp = (v_rsp) - (96);
    v_r15 = 0;
    if (((unsigned int)(a2)) >= 4) goto loc_00AF28DE;
loc_00AF28D4:
    goto loc_00AF2FCB;
loc_00AF28DE:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > 18) goto loc_00AF2F50;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == 18) goto loc_00AF2F43;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > 6) goto loc_00AF2CA3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == 6) goto loc_00AF2B78;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_00AF2B56;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (1));
    if (condition_is_equal) goto loc_00AF2A9A;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2A68;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2A44;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2988;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF2F5A;
    *(unsigned int *)(a4) = 20;
    if ((((unsigned int)(a2 - 16)) & (0xFFFFFFFBULL)) != 0) goto loc_00AF2F71;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5056502)));
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5056497)));
    *(unsigned int *)(a1 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5056492)));
    result = (unsigned int)(*(unsigned int *)(v_rip + 5056492));
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 20) {
        result = *(unsigned int *)(v_rip + 5056345);
        *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    }
    goto loc_00AF2C00;
loc_00AF2988:
    *(unsigned int *)(a4) = 24;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 24) goto loc_00AF2F71;
    v_stack_m38 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(a1 + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)(*(unsigned __int64 *)(result + 832) + 4504);
    }
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(result + 832), a2, a3, a4);
    if (result == 0) goto loc_00AF2DCE;
    result = EtwpReferenceLoggerSecurityDescriptor(result, a2, a3, a4);
    v_stack_m40 = result;
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)(a2)) - 16);
    result = SeQuerySecurityDescriptorInfo(v_stack_m58, a1 + 16, v_stack_p10, v_stack_m40);
    result = (unsigned int)(((unsigned int)(v_stack_p10)) + (16));
    *(unsigned int *)(a4) = (unsigned int)(result);
    result = EtwpDereferenceLoggerSecurityDescriptor(result, result, v_stack_p10, v_stack_m40);
    a2 = 0;
    goto loc_00AF2BF6;
loc_00AF2A44:
    *(unsigned int *)(v_stack_m40) = 8;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 8) goto loc_00AF2F71;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3260621)));
    goto loc_00AF2C00;
loc_00AF2A68:
    *(unsigned int *)(v_stack_m40) = 16;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 16) goto loc_00AF2F71;
    result = PsGetCurrentServerSiloGlobals(result, a2, v_stack_p10, v_stack_m40);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 4408);
    goto loc_00AF2C00;
loc_00AF2A9A:
    *(unsigned int *)(v_stack_m40) = 48;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 48) goto loc_00AF2F71;
    v_stack_m38 = *(unsigned __int64 *)(a1 + 8);
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(a1 + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)(result + 4504);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, a2, 1, v_stack_m40);
    v_stack_m40 = result;
    if (result == 0) goto loc_00AF2DCE;
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) == 0) goto loc_00AF2B3D;
    result = (*(unsigned __int8 *)(result + 818)) << (5);
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16 + 16) = v_xmm1;
    a2 = 0;
    result = EtwpMapEnableFlags(a1 + 16, a2, 1, v_stack_m40);
    goto loc_00AF2DF4;
loc_00AF2B3D:
    result = EtwpReleaseLoggerContext(result, 1, 1, v_stack_m40);
    result = KeLeaveCriticalRegion(result, 1, 1, v_stack_m40);
    goto loc_00AF28D4;
loc_00AF2B56:
    *(unsigned int *)(v_stack_m40) = 8;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 8) goto loc_00AF2F71;
    *(unsigned int *)(a1 + 4) = 85;
    goto loc_00AF2C00;
loc_00AF2B78:
    v_stack_p10 = 0;
    v_stack_m40 = a1 + 16;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 16) goto loc_00AF2F71;
    v_stack_m38 = *(unsigned __int64 *)(a1 + 8);
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(a1 + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)(result + 4504);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, a2, 1, v_stack_m40);
    v_stack_m38 = result;
    if (result == 0) goto loc_00AF2DCE;
    result = EtwpCheckLoggerControlAccess(1, result, 1, v_stack_m40);
    if (!sign_flag) goto loc_00AF2C07;
loc_00AF2BF1:
loc_00AF2BF4:
loc_00AF2BF6:
    result = EtwpReleaseLoggerContext(result, 1, 1, v_stack_m40);
loc_00AF2BFB:
    result = KeLeaveCriticalRegion(result, 1, 1, v_stack_m40);
loc_00AF2C00:
    goto loc_00AF2FCB;
loc_00AF2C07:
    result = (unsigned int)(*(unsigned int *)(result + 816));
    v_rbx = 0;
    if (sign_flag) {
        a1 = result + 1040;
        result = RtlNumberOfSetBits(a1, 1, 1, v_stack_m40);
        v_rbx = (unsigned int)(result);
        v_stack_p10 = (unsigned int)(result);
    }
    *(unsigned int *)(a4) = (unsigned int)(v_rbx * 4 + 16);
    if (((unsigned int)(v_rbx * 4 + 16)) > ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00AF2C94;
loc_00AF2C46:
    v_stack_m58 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00AF2BF1;
    result = RtlFindSetBits(result + 1040, 1, v_r15 + 1, v_stack_m40);
    v_stack_m50 = (unsigned int)(result);
    *(unsigned int *)(v_stack_m40 + 0 * 4) = (unsigned int)(result);
    goto loc_00AF2C90;
loc_00AF2C90:
    v_rbx = (unsigned int)((0) + 1);
    goto loc_00AF2C46;
loc_00AF2C94:
    goto loc_00AF2BF1;
loc_00AF2CA3:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (7));
    if (condition_is_equal) goto loc_00AF2F11;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF2E65;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF2E65;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF2D69;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF2D59;
    if (((unsigned int)(a1)) != 1) goto loc_00AF2F5A;
    v_stack_m40 = (unsigned int)((unsigned int)(result));
    v_stack_m50 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(v_stack_p10))) < 40) goto loc_00AF2F71;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p10)) + (-8));
    v_stack_m60 = v_stack_m40;
    v_stack_m68 = v_stack_m50;
    result = ExLockUserBuffer(result + 8, (unsigned int)((unsigned int)(v_r14)), v_r15 + 1, 1);
    if (sign_flag) goto loc_00AF2FCB;
    result = guard_dispatch_icall(20, (unsigned int)((unsigned int)(v_r14)), v_stack_m50, v_stack_m40);
    if (v_stack_m50 == ((unsigned int)((unsigned int)(result)))) goto loc_00AF2C00;
    result = ExUnlockUserBuffer(v_stack_m40, (unsigned int)((unsigned int)(v_r14)), v_stack_m50, v_stack_m40);
    goto loc_00AF2C00;
loc_00AF2D59:
    result = EtwpGetPmcProfileSource(result, (unsigned int)((unsigned int)(v_r14)), v_stack_m40, v_stack_m40);
    goto loc_00AF2FC4;
loc_00AF2D69:
    v_stack_m38 = result + 16;
    if (((unsigned int)(v_r14)) < 16) goto loc_00AF2F71;
    result = PsIsCurrentThreadInServerSilo(result, (unsigned int)((unsigned int)(v_r14)), v_stack_m40, v_stack_m40);
    if ((unsigned __int8)(result) != 0) goto loc_00AF2E7B;
    v_stack_m40 = *(unsigned __int64 *)(result + 8);
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)(result + 4504);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, a2, 1, v_stack_m40);
    v_stack_m40 = result;
    if (result != 0) goto loc_00AF2DD8;
loc_00AF2DCE:
    goto loc_00AF2BFB;
loc_00AF2DD8:
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) == 0) goto loc_00AF2E4F;
    result = EtwpCheckSystemTraceAccess(result, 1, 1, v_stack_m40);
    if (!sign_flag) goto loc_00AF2DFC;
loc_00AF2DF4:
    goto loc_00AF2BF4;
loc_00AF2DFC:
    *(unsigned int *)(v_stack_m40) = (unsigned int)(*(unsigned __int16 *)(v_rip + 4246322 + *(unsigned __int8 *)(result + 818) + *(unsigned __int8 *)(result + 818) * 4 * 4) * 4 + 16);
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 4246322 + *(unsigned __int8 *)(result + 818) + *(unsigned __int8 *)(result + 818) * 4 * 4) * 4 + 16)) > ((unsigned int)(v_r14))) goto loc_00AF2E48;
    a3 = (*(unsigned __int16 *)(v_rip + 4246322 + *(unsigned __int8 *)(result + 818) + *(unsigned __int8 *)(result + 818) * 4 * 4)) << (2);
    a1 = (v_rip + 4246322) + (4);
    result = memcpy(v_stack_m38, a1 + *(unsigned __int8 *)(result + 818) + *(unsigned __int8 *)(result + 818) * 4 * 4, a3, v_stack_m40);
    goto loc_00AF2DF4;
loc_00AF2E48:
    goto loc_00AF2DF4;
loc_00AF2E4F:
    result = EtwpReleaseLoggerContext(v_stack_m38, 1, a3, v_stack_m40);
    goto loc_00AF2BFB;
loc_00AF2E65:
    if (((unsigned int)(v_r14)) < 8) goto loc_00AF2F71;
    result = PsIsCurrentThreadInServerSilo(v_stack_m38, 1, a3, v_stack_m40);
    if ((unsigned __int8)(result) == 0) goto loc_00AF2E85;
loc_00AF2E7B:
    goto loc_00AF2FCB;
loc_00AF2E85:
    v_r14 = (unsigned int)((v_r14) + (-4));
    v_r14 = (unsigned int)((v_r14) >> (2));
    a1 = 0;
loc_00AF2E8F:
    result = PsGetNextProcess(a1, 1, a3, v_stack_m40);
    v_stack_m40 = result;
    if (result == 0) goto loc_00AF2EF4;
    if (((*(unsigned int *)(result + 1532)) & (0x1000ULL)) != 0) goto loc_00AF2EEF;
    if (((unsigned int)(result)) == 9) goto loc_00AF2EBE;
    result = EtwpUMGLEnabled(result, 1, a3, v_stack_m40);
    if ((unsigned __int8)(result) == 0) goto loc_00AF2EEF;
loc_00AF2EBE:
    result = PsGetProcessId(result, 1, a3, v_stack_m40);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) >= ((unsigned int)(v_r14))) goto loc_00AF2EEC;
    *(unsigned int *)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) * 4 + 4) = (unsigned int)(result);
    goto loc_00AF2EEC;
loc_00AF2EEC:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) + 1);
loc_00AF2EEF:
    goto loc_00AF2E8F;
loc_00AF2EF4:
    *(unsigned int *)(v_stack_m40) = (unsigned int)(v_r13 * 4 + 4);
    v_rdi = (unsigned int)(((unsigned int)(0xC0000023ULL)) & ((unsigned int)(v_r13 * 4 + 4)));
    goto loc_00AF2C00;
loc_00AF2F11:
    *(unsigned int *)(v_stack_m40) = 16;
    if (((unsigned int)(v_r14)) != 16) goto loc_00AF2F71;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3259372)));
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3259371)));
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3259358)));
    goto loc_00AF2C00;
loc_00AF2F43:
    result = EtwpGetSoftRestartInformation(result, 1, v_stack_m40, v_stack_m40);
    goto loc_00AF2FC4;
loc_00AF2F50:
    if (((unsigned int)(result)) == 25) goto loc_00AF2FBC;
    if (((unsigned int)(result)) == 28) goto loc_00AF2F64;
loc_00AF2F5A:
    goto loc_00AF2C00;
loc_00AF2F64:
    *(unsigned int *)(v_stack_m40) = 12;
    if (((unsigned int)(v_r14)) == 12) goto loc_00AF2F78;
loc_00AF2F71:
    goto loc_00AF2FCB;
loc_00AF2F78:
    if ((unsigned __int8)(v_stack_m40) == 0) goto loc_00AF2F98;
    result = RtlWriteULongToUser(result + 4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5062178)))), v_stack_m40, v_stack_m40);
    goto loc_00AF2F9A;
loc_00AF2F98:
    *(unsigned int *)(result + 4) = (unsigned int)(result);
loc_00AF2F9A:
    if ((unsigned __int8)(v_stack_p18) == 0) goto loc_00AF2FB2;
    result = RtlWriteULongToUser(result + 8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5062048)))), v_stack_p18, v_stack_m40);
    goto loc_00AF2FB5;
loc_00AF2FB2:
    *(unsigned int *)(result + 8) = (unsigned int)(result);
loc_00AF2FB5:
    goto loc_00AF2C00;
loc_00AF2FBC:
    result = EtwpQueryCoverageSamplerInformation(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5062048)))), v_stack_p18, v_stack_m40);
loc_00AF2FC4:
    goto loc_00AF2C00;
loc_00AF2FCB:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwQueryPerformanceTraceInformation(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = (uint8_t)(Arg3);
    local_rsp = (local_rsp) - (96);
    local_r15 = 0;
    if (((uint32_t)(Arg2)) >= 4) goto loc_00AF28DE;
loc_00AF28D4:
    goto loc_00AF2FCB;
loc_00AF28DE:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > 18) goto loc_00AF2F50;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == 18) goto loc_00AF2F43;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > 6) goto loc_00AF2CA3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == 6) goto loc_00AF2B78;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_00AF2B56;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (1));
    if (condition_is_equal) goto loc_00AF2A9A;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2A68;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2A44;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF2988;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF2F5A;
    *(uint32_t *)(arg4) = 20;
    if ((((uint32_t)(Arg2 - 16)) & (0xFFFFFFFBULL)) != 0) goto loc_00AF2F71;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D27F6)));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D27F1)));
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D27EC)));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x4D27EC));
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 20) {
        result = *(uint32_t *)(v_rip + 0x4D2759);
        *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    }
    goto loc_00AF2C00;
loc_00AF2988:
    *(uint32_t *)(arg4) = 24;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 24) goto loc_00AF2F71;
    v_stack_m38 = *(uint64_t *)(arg1 + 0x8);
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    if (((uint32_t)((uint16_t)(*(uint64_t *)(arg1 + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)(*(uint64_t *)(result + 0x340) + 0x1198);
    }
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(result + 0x340), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00AF2DCE;
    result = EtwpReferenceLoggerSecurityDescriptor(result, Arg2, Arg3, Arg4);
    v_stack_m40 = result;
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)(Arg2)) - 16);
    result = SeQuerySecurityDescriptorInfo(v_stack_m58, Arg1 + 16, v_stack_p10, v_stack_m40);
    result = (uint32_t)(((uint32_t)(v_stack_p10)) + (16));
    *(uint32_t *)(arg4) = (uint32_t)(result);
    result = EtwpDereferenceLoggerSecurityDescriptor(result, result, v_stack_p10, v_stack_m40);
    Arg2 = 0;
    goto loc_00AF2BF6;
loc_00AF2A44:
    *(uint32_t *)(v_stack_m40) = 8;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 8) goto loc_00AF2F71;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x31C0CD)));
    goto loc_00AF2C00;
loc_00AF2A68:
    *(uint32_t *)(v_stack_m40) = 16;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 16) goto loc_00AF2F71;
    result = PsGetCurrentServerSiloGlobals(result, Arg2, v_stack_p10, v_stack_m40);
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x1138);
    goto loc_00AF2C00;
loc_00AF2A9A:
    *(uint32_t *)(v_stack_m40) = 48;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 48) goto loc_00AF2F71;
    v_stack_m38 = *(uint64_t *)(arg1 + 0x8);
    if (((uint32_t)((uint16_t)(*(uint64_t *)(arg1 + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)(result + 0x1198);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, Arg2, 1, v_stack_m40);
    v_stack_m40 = result;
    if (result == 0) goto loc_00AF2DCE;
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) == 0) goto loc_00AF2B3D;
    result = (*(uint8_t *)(result + 0x332)) << (5);
    *(uint64_t *)(arg1 + 0x10) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10 + 0x10) = v_xmm1;
    Arg2 = 0;
    result = EtwpMapEnableFlags(Arg1 + 16, Arg2, 1, v_stack_m40);
    goto loc_00AF2DF4;
loc_00AF2B3D:
    result = EtwpReleaseLoggerContext(result, 1, 1, v_stack_m40);
    result = KeLeaveCriticalRegion(result, 1, 1, v_stack_m40);
    goto loc_00AF28D4;
loc_00AF2B56:
    *(uint32_t *)(v_stack_m40) = 8;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 8) goto loc_00AF2F71;
    *(uint32_t *)(arg1 + 0x4) = 85;
    goto loc_00AF2C00;
loc_00AF2B78:
    v_stack_p10 = 0;
    v_stack_m40 = Arg1 + 16;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 16) goto loc_00AF2F71;
    v_stack_m38 = *(uint64_t *)(arg1 + 0x8);
    if (((uint32_t)((uint16_t)(*(uint64_t *)(arg1 + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)(result + 0x1198);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, Arg2, 1, v_stack_m40);
    v_stack_m38 = result;
    if (result == 0) goto loc_00AF2DCE;
    result = EtwpCheckLoggerControlAccess(1, result, 1, v_stack_m40);
    if (!sign_flag) goto loc_00AF2C07;
loc_00AF2BF1:
loc_00AF2BF4:
loc_00AF2BF6:
    result = EtwpReleaseLoggerContext(result, 1, 1, v_stack_m40);
loc_00AF2BFB:
    result = KeLeaveCriticalRegion(result, 1, 1, v_stack_m40);
loc_00AF2C00:
    goto loc_00AF2FCB;
loc_00AF2C07:
    result = (uint32_t)(*(uint32_t *)(result + 0x330));
    local_rbx = 0;
    if (sign_flag) {
        Arg1 = result + 1040;
        result = RtlNumberOfSetBits(Arg1, 1, 1, v_stack_m40);
        local_rbx = (uint32_t)(result);
        v_stack_p10 = (uint32_t)(result);
    }
    *(uint32_t *)(arg4) = (uint32_t)(local_rbx * 4 + 16);
    if (((uint32_t)(local_rbx * 4 + 16)) > ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00AF2C94;
loc_00AF2C46:
    v_stack_m58 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00AF2BF1;
    result = RtlFindSetBits(result + 1040, 1, local_r15 + 1, v_stack_m40);
    v_stack_m50 = (uint32_t)(result);
    *(uint32_t *)(v_stack_m40 + 0x0 * 4) = (uint32_t)(result);
    goto loc_00AF2C90;
loc_00AF2C90:
    local_rbx = (uint32_t)((0) + 1);
    goto loc_00AF2C46;
loc_00AF2C94:
    goto loc_00AF2BF1;
loc_00AF2CA3:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (7));
    if (condition_is_equal) goto loc_00AF2F11;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF2E65;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF2E65;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF2D69;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF2D59;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AF2F5A;
    v_stack_m40 = (uint32_t)((uint32_t)(result));
    v_stack_m50 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(v_stack_p10))) < 40) goto loc_00AF2F71;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p10)) + (-8));
    v_stack_m60 = v_stack_m40;
    v_stack_m68 = v_stack_m50;
    result = ExLockUserBuffer(result + 8, (uint32_t)((uint32_t)(local_r14)), local_r15 + 1, 1);
    if (sign_flag) goto loc_00AF2FCB;
    result = guard_dispatch_icall(20, (uint32_t)((uint32_t)(local_r14)), v_stack_m50, v_stack_m40);
    if (v_stack_m50 == ((uint32_t)((uint32_t)(result)))) goto loc_00AF2C00;
    result = ExUnlockUserBuffer(v_stack_m40, (uint32_t)((uint32_t)(local_r14)), v_stack_m50, v_stack_m40);
    goto loc_00AF2C00;
loc_00AF2D59:
    result = EtwpGetPmcProfileSource(result, (uint32_t)((uint32_t)(local_r14)), v_stack_m40, v_stack_m40);
    goto loc_00AF2FC4;
loc_00AF2D69:
    v_stack_m38 = result + 16;
    if (((uint32_t)(local_r14)) < 16) goto loc_00AF2F71;
    result = PsIsCurrentThreadInServerSilo(result, (uint32_t)((uint32_t)(local_r14)), v_stack_m40, v_stack_m40);
    if ((uint8_t)(result) != 0) goto loc_00AF2E7B;
    v_stack_m40 = *(uint64_t *)(result + 0x8);
    if (((uint32_t)((uint16_t)(*(uint64_t *)(result + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)(result + 0x1198);
    }
    result = EtwpAcquireLoggerContextByLoggerId(result, Arg2, 1, v_stack_m40);
    v_stack_m40 = result;
    if (result != 0) goto loc_00AF2DD8;
loc_00AF2DCE:
    goto loc_00AF2BFB;
loc_00AF2DD8:
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) == 0) goto loc_00AF2E4F;
    result = EtwpCheckSystemTraceAccess(result, 1, 1, v_stack_m40);
    if (!sign_flag) goto loc_00AF2DFC;
loc_00AF2DF4:
    goto loc_00AF2BF4;
loc_00AF2DFC:
    *(uint32_t *)(v_stack_m40) = (uint32_t)(*(uint16_t *)(v_rip + 0x40CB32 + *(uint8_t *)(result + 0x332) + *(uint8_t *)(result + 0x332) * 4 * 4) * 4 + 16);
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x40CB32 + *(uint8_t *)(result + 0x332) + *(uint8_t *)(result + 0x332) * 4 * 4) * 4 + 16)) > ((uint32_t)(local_r14))) goto loc_00AF2E48;
    Arg3 = (*(uint16_t *)(v_rip + 0x40CB32 + *(uint8_t *)(result + 0x332) + *(uint8_t *)(result + 0x332) * 4 * 4)) << (2);
    Arg1 = (v_rip + 4246322) + (4);
    result = memcpy(v_stack_m38, Arg1 + *(uint8_t *)(result + 0x332) + *(uint8_t *)(result + 0x332) * 4 * 4, Arg3, v_stack_m40);
    goto loc_00AF2DF4;
loc_00AF2E48:
    goto loc_00AF2DF4;
loc_00AF2E4F:
    result = EtwpReleaseLoggerContext(v_stack_m38, 1, Arg3, v_stack_m40);
    goto loc_00AF2BFB;
loc_00AF2E65:
    if (((uint32_t)(local_r14)) < 8) goto loc_00AF2F71;
    result = PsIsCurrentThreadInServerSilo(v_stack_m38, 1, Arg3, v_stack_m40);
    if ((uint8_t)(result) == 0) goto loc_00AF2E85;
loc_00AF2E7B:
    goto loc_00AF2FCB;
loc_00AF2E85:
    local_r14 = (uint32_t)((local_r14) + (-4));
    local_r14 = (uint32_t)((local_r14) >> (2));
    Arg1 = 0;
loc_00AF2E8F:
    result = PsGetNextProcess(Arg1, 1, Arg3, v_stack_m40);
    v_stack_m40 = result;
    if (result == 0) goto loc_00AF2EF4;
    if (((*(uint32_t *)(result + 0x5FC)) & (0x1000ULL)) != 0) goto loc_00AF2EEF;
    if (((uint32_t)(result)) == 9) goto loc_00AF2EBE;
    result = EtwpUMGLEnabled(result, 1, Arg3, v_stack_m40);
    if ((uint8_t)(result) == 0) goto loc_00AF2EEF;
loc_00AF2EBE:
    result = PsGetProcessId(result, 1, Arg3, v_stack_m40);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) >= ((uint32_t)(local_r14))) goto loc_00AF2EEC;
    *(uint32_t *)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) * 4 + 0x4) = (uint32_t)(result);
    goto loc_00AF2EEC;
loc_00AF2EEC:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) + 1);
loc_00AF2EEF:
    goto loc_00AF2E8F;
loc_00AF2EF4:
    *(uint32_t *)(v_stack_m40) = (uint32_t)(local_r13 * 4 + 4);
    local_rdi = (uint32_t)(((uint32_t)(0xC0000023ULL)) & ((uint32_t)(local_r13 * 4 + 4)));
    goto loc_00AF2C00;
loc_00AF2F11:
    *(uint32_t *)(v_stack_m40) = 16;
    if (((uint32_t)(local_r14)) != 16) goto loc_00AF2F71;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x31BBEC)));
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x31BBEB)));
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x31BBDE)));
    goto loc_00AF2C00;
loc_00AF2F43:
    result = EtwpGetSoftRestartInformation(result, 1, v_stack_m40, v_stack_m40);
    goto loc_00AF2FC4;
loc_00AF2F50:
    if (((uint32_t)(result)) == 25) goto loc_00AF2FBC;
    if (((uint32_t)(result)) == 28) goto loc_00AF2F64;
loc_00AF2F5A:
    goto loc_00AF2C00;
loc_00AF2F64:
    *(uint32_t *)(v_stack_m40) = 12;
    if (((uint32_t)(local_r14)) == 12) goto loc_00AF2F78;
loc_00AF2F71:
    goto loc_00AF2FCB;
loc_00AF2F78:
    if ((uint8_t)(v_stack_m40) == 0) goto loc_00AF2F98;
    result = RtlWriteULongToUser(result + 4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D3E22)))), v_stack_m40, v_stack_m40);
    goto loc_00AF2F9A;
loc_00AF2F98:
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
loc_00AF2F9A:
    if ((uint8_t)(v_stack_p18) == 0) goto loc_00AF2FB2;
    result = RtlWriteULongToUser(result + 8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D3DA0)))), v_stack_p18, v_stack_m40);
    goto loc_00AF2FB5;
loc_00AF2FB2:
    *(uint32_t *)(result + 0x8) = (uint32_t)(result);
loc_00AF2FB5:
    goto loc_00AF2C00;
loc_00AF2FBC:
    result = EtwpQueryCoverageSamplerInformation(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D3DA0)))), v_stack_p18, v_stack_m40);
loc_00AF2FC4:
    goto loc_00AF2C00;
loc_00AF2FCB:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x4 + rcx*4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF28A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
