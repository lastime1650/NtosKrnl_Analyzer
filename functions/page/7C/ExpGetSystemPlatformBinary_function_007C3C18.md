# ExpGetSystemPlatformBinary

- RVA: `0x007C3C18`–`0x007C40C7` (길이 `1,199` bytes)
- VA: `0x00000001407C3C18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4148`
- 디코드: `278`개 명령, `1,199/1,199` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x007C3CD7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C3D02` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007C3D4A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007C3D56` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C3D64` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x007C3DB5` → [ExpGetSystemFirmwareTableInformation](../A3/ExpGetSystemFirmwareTableInformation_function_00A38A2C.md) (function, `0x00A38A2C`)
- `0x007C3DE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007C3E29` → [ExpGetSystemFirmwareTableInformation](../A3/ExpGetSystemFirmwareTableInformation_function_00A38A2C.md) (function, `0x00A38A2C`)
- `0x007C3E55` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C3E7A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007C3EE6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007C3EF2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C3F00` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x007C3F6C` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (function, `0x00327830`)
- `0x007C3FA9` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x007C3FBA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007C3FD8` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x007C3FEB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007C4051` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007C405D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C406B` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x007C407F` → [MmUnmapIoSpace](../../text/3F/MmUnmapIoSpace_function_003F78F0.md) (function, `0x003F78F0`)
- `0x007C4091` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007C40A3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A59CE5`

### Static image references
- `0x007C3C34` → RVA `0x00E0A740` (`.data`; read)
- `0x007C3CD0` → RVA `0x00FD80B8` (`PAGEDATA`; read)
- `0x007C3D16` → RVA `0x00FD80E0` (`PAGEDATA`; read)
- `0x007C3E5D` → RVA `0x00FD80B8` (`PAGEDATA`; read/write)
- `0x007C3E94` → RVA `0x00FD80E0` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x007C3CD7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C3D02` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007C3D4A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007C3D56` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C3D64` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x007C3DE5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007C3E55` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C3E7A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007C3EE6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007C3EF2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C3F00` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x007C3F6C` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (`PAGE` → `.text`)
  - `0x007C3FBA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007C3FEB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007C4051` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007C405D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C406B` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x007C407F` → [MmUnmapIoSpace](../../text/3F/MmUnmapIoSpace_function_003F78F0.md) (`PAGE` → `.text`)
  - `0x007C4091` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007C40A3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C3C18  4C 8B DC                        mov r11, rsp
007C3C1B  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
007C3C1F  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
007C3C23  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
007C3C27  41 54                           push r12
007C3C29  41 55                           push r13
007C3C2B  41 57                           push r15
007C3C2D  48 81 EC A0 00 00 00            sub rsp, 0xa0
007C3C34  48 8B 05 05 6B 64 00            mov rax, qword ptr [rip + 0x646b05]
007C3C3B  48 33 C4                        xor rax, rsp
007C3C3E  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
007C3C46  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
007C3C4B  4C 8B E9                        mov r13, rcx
007C3C4E  33 F6                           xor esi, esi
007C3C50  49 89 73 90                     mov qword ptr [r11 - 0x70], rsi
007C3C54  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
007C3C58  0F 57 C0                        xorps xmm0, xmm0
007C3C5B  33 C0                           xor eax, eax
007C3C5D  41 0F 11 43 C8                  movups xmmword ptr [r11 - 0x38], xmm0
007C3C62  41 89 43 D8                     mov dword ptr [r11 - 0x28], eax
007C3C66  89 74 24 2C                     mov dword ptr [rsp + 0x2c], esi
007C3C6A  49 89 73 88                     mov qword ptr [r11 - 0x78], rsi
007C3C6E  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
007C3C72  44 8B FE                        mov r15d, esi
007C3C75  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007C3C7A  44 8A E6                        mov r12b, sil
007C3C7D  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
007C3C82  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007C3C87  83 FA 20                        cmp edx, 0x20
007C3C8A  73 0A                           jae 0x1407c3c96
007C3C8C  BF 0D 00 00 C0                  mov edi, 0xc000000d
007C3C91  E9 9F 03 00 00                  jmp 0x1407c4035
007C3C96  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
007C3C99  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007C3C9D  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
007C3CA0  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007C3CA4  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
007C3CA8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007C3CAD  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
007C3CB1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007C3CB6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007C3CBF  48 83 CB FF                     or rbx, 0xffffffffffffffff
007C3CC3  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007C3CCA  90                              nop
007C3CCB  45 33 C0                        xor r8d, r8d
007C3CCE  33 D2                           xor edx, edx
007C3CD0  48 8D 0D E1 43 81 00            lea rcx, [rip + 0x8143e1]
007C3CD7  E8 54 C5 A4 FF                  call 0x140210230
007C3CDC  48 8B F8                        mov rdi, rax
007C3CDF  8D 4B 12                        lea ecx, [rbx + 0x12]
007C3CE2  33 C0                           xor eax, eax
007C3CE4  F0 48 0F B1 0D CB 43 81 00      lock cmpxchg qword ptr [rip + 0x8143cb], rcx
007C3CED  74 1B                           je 0x1407c3d0a
007C3CEF  4C 8D 0D C2 43 81 00            lea r9, [rip + 0x8143c2]
007C3CF6  4C 8B C7                        mov r8, rdi
007C3CF9  33 D2                           xor edx, edx
007C3CFB  48 8D 0D B6 43 81 00            lea rcx, [rip + 0x8143b6]
007C3D02  E8 45 C7 A4 FF                  call 0x14021044c
007C3D07  8D 4B 12                        lea ecx, [rbx + 0x12]
007C3D0A  48 85 FF                        test rdi, rdi
007C3D0D  74 04                           je 0x1407c3d13
007C3D0F  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
007C3D13  41 B4 01                        mov r12b, 1
007C3D16  48 8B 05 C3 43 81 00            mov rax, qword ptr [rip + 0x8143c3]
007C3D1D  48 3B C3                        cmp rax, rbx
007C3D20  75 0A                           jne 0x1407c3d2c
007C3D22  BF BB 00 00 C0                  mov edi, 0xc00000bb
007C3D27  E9 09 03 00 00                  jmp 0x1407c4035
007C3D2C  48 85 C0                        test rax, rax
007C3D2F  0F 85 7F 01 00 00               jne 0x1407c3eb4
007C3D35  48 8B C1                        mov rax, rcx
007C3D38  F0 48 0F B1 35 77 43 81 00      lock cmpxchg qword ptr [rip + 0x814377], rsi
007C3D41  74 0C                           je 0x1407c3d4f
007C3D43  48 8D 0D 6E 43 81 00            lea rcx, [rip + 0x81436e]
007C3D4A  E8 F1 F6 A9 FF                  call 0x140263440
007C3D4F  48 8D 0D 62 43 81 00            lea rcx, [rip + 0x814362]
007C3D56  E8 A5 D8 B1 FF                  call 0x1402e1600
007C3D5B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007C3D64  E8 A7 B2 A9 FF                  call 0x14025f010
007C3D69  44 8A E6                        mov r12b, sil
007C3D6C  39 74 24 28                     cmp dword ptr [rsp + 0x28], esi
007C3D70  0F 85 16 FF FF FF               jne 0x1407c3c8c
007C3D76  39 74 24 30                     cmp dword ptr [rsp + 0x30], esi
007C3D7A  0F 85 0C FF FF FF               jne 0x1407c3c8c
007C3D80  C7 84 24 80 00 00 00 49 50 43 41  mov dword ptr [rsp + 0x80], 0x41435049
007C3D8B  C7 84 24 84 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x84], 1
007C3D96  48 C7 84 24 88 00 00 00 57 50 42 54  mov qword ptr [rsp + 0x88], 0x54425057
007C3DA2  4C 8D 4C 24 2C                  lea r9, [rsp + 0x2c]
007C3DA7  33 D2                           xor edx, edx
007C3DA9  44 8D 42 14                     lea r8d, [rdx + 0x14]
007C3DAD  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007C3DB5  E8 72 4C 27 00                  call 0x140a38a2c
007C3DBA  8B F8                           mov edi, eax
007C3DBC  3D 23 00 00 C0                  cmp eax, 0xc0000023
007C3DC1  74 11                           je 0x1407c3dd4
007C3DC3  C1 FF 1F                        sar edi, 0x1f
007C3DC6  83 E7 40                        and edi, 0x40
007C3DC9  81 EF 85 FF FF 3F               sub edi, 0x3fffff85
007C3DCF  E9 61 02 00 00                  jmp 0x1407c4035
007C3DD4  8B 7C 24 2C                     mov edi, dword ptr [rsp + 0x2c]
007C3DD8  8B D7                           mov edx, edi
007C3DDA  B9 40 00 00 00                  mov ecx, 0x40
007C3DDF  41 B8 57 50 42 54               mov r8d, 0x54425057
007C3DE5  E8 06 E3 3B 00                  call 0x140b820f0
007C3DEA  4C 8B F8                        mov r15, rax
007C3DED  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007C3DF2  48 85 C0                        test rax, rax
007C3DF5  75 0A                           jne 0x1407c3e01
007C3DF7  BF 9A 00 00 C0                  mov edi, 0xc000009a
007C3DFC  E9 34 02 00 00                  jmp 0x1407c4035
007C3E01  C7 00 49 50 43 41               mov dword ptr [rax], 0x41435049
007C3E07  C7 40 04 01 00 00 00            mov dword ptr [rax + 4], 1
007C3E0E  C7 40 08 57 50 42 54            mov dword ptr [rax + 8], 0x54425057
007C3E15  8D 47 F0                        lea eax, [rdi - 0x10]
007C3E18  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
007C3E1C  4C 8D 4C 24 2C                  lea r9, [rsp + 0x2c]
007C3E21  44 8B C7                        mov r8d, edi
007C3E24  33 D2                           xor edx, edx
007C3E26  49 8B CF                        mov rcx, r15
007C3E29  E8 FE 4B 27 00                  call 0x140a38a2c
007C3E2E  8B F8                           mov edi, eax
007C3E30  85 C0                           test eax, eax
007C3E32  0F 88 FD 01 00 00               js 0x1407c4035
007C3E38  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007C3E41  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007C3E48  90                              nop
007C3E49  45 33 C0                        xor r8d, r8d
007C3E4C  33 D2                           xor edx, edx
007C3E4E  48 8D 0D 63 42 81 00            lea rcx, [rip + 0x814263]
007C3E55  E8 D6 C3 A4 FF                  call 0x140210230
007C3E5A  48 8B F8                        mov rdi, rax
007C3E5D  F0 48 0F BA 2D 51 42 81 00 00   lock bts qword ptr [rip + 0x814251], 0
007C3E67  73 16                           jae 0x1407c3e7f
007C3E69  4C 8D 05 48 42 81 00            lea r8, [rip + 0x814248]
007C3E70  48 8B D0                        mov rdx, rax
007C3E73  48 8D 0D 3E 42 81 00            lea rcx, [rip + 0x81423e]
007C3E7A  E8 11 BE A4 FF                  call 0x14020fc90
007C3E7F  48 85 FF                        test rdi, rdi
007C3E82  74 04                           je 0x1407c3e88
007C3E84  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
007C3E88  48 8B 05 51 42 81 00            mov rax, qword ptr [rip + 0x814251]
007C3E8F  48 85 C0                        test rax, rax
007C3E92  75 35                           jne 0x1407c3ec9
007C3E94  4C 89 3D 45 42 81 00            mov qword ptr [rip + 0x814245], r15
007C3E9B  4C 8B FE                        mov r15, rsi
007C3E9E  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007C3EA3  B8 01 00 00 00                  mov eax, 1
007C3EA8  8D 48 10                        lea ecx, [rax + 0x10]
007C3EAB  F0 48 0F B1 0D 04 42 81 00      lock cmpxchg qword ptr [rip + 0x814204], rcx
007C3EB4  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
007C3EB9  41 F6 C4 01                     test r12b, 1
007C3EBD  74 4B                           je 0x1407c3f0a
007C3EBF  BF 0D 00 00 C0                  mov edi, 0xc000000d
007C3EC4  E9 71 01 00 00                  jmp 0x1407c403a
007C3EC9  48 3B C3                        cmp rax, rbx
007C3ECC  75 D5                           jne 0x1407c3ea3
007C3ECE  F0 48 0F C1 1D E1 41 81 00      lock xadd qword ptr [rip + 0x8141e1], rbx
007C3ED7  80 E3 06                        and bl, 6
007C3EDA  80 FB 02                        cmp bl, 2
007C3EDD  75 0C                           jne 0x1407c3eeb
007C3EDF  48 8D 0D D2 41 81 00            lea rcx, [rip + 0x8141d2]
007C3EE6  E8 E5 1E AA FF                  call 0x140265dd0
007C3EEB  48 8D 0D C6 41 81 00            lea rcx, [rip + 0x8141c6]
007C3EF2  E8 09 D7 B1 FF                  call 0x1402e1600
007C3EF7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007C3F00  E8 0B B1 A9 FF                  call 0x14025f010
007C3F05  E9 18 FE FF FF                  jmp 0x1407c3d22
007C3F0A  48 8B 1D CF 41 81 00            mov rbx, qword ptr [rip + 0x8141cf]
007C3F11  80 7B 40 01                     cmp byte ptr [rbx + 0x40], 1
007C3F15  0F 85 09 01 00 00               jne 0x1407c4024
007C3F1B  80 7B 41 01                     cmp byte ptr [rbx + 0x41], 1
007C3F1F  0F 85 FF 00 00 00               jne 0x1407c4024
007C3F25  44 0F B7 43 42                  movzx r8d, word ptr [rbx + 0x42]
007C3F2A  41 F6 C0 01                     test r8b, 1
007C3F2E  0F 85 F0 00 00 00               jne 0x1407c4024
007C3F34  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
007C3F38  48 85 C9                        test rcx, rcx
007C3F3B  0F 84 E3 00 00 00               je 0x1407c4024
007C3F41  83 7B 28 01                     cmp dword ptr [rbx + 0x28], 1
007C3F45  0F 85 D9 00 00 00               jne 0x1407c4024
007C3F4B  8B 53 34                        mov edx, dword ptr [rbx + 0x34]
007C3F4E  3B 54 24 28                     cmp edx, dword ptr [rsp + 0x28]
007C3F52  0F 87 AE 00 00 00               ja 0x1407c4006
007C3F58  45 3B C4                        cmp r8d, r12d
007C3F5B  0F 87 A5 00 00 00               ja 0x1407c4006
007C3F61  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
007C3F66  41 B8 02 00 00 00               mov r8d, 2
007C3F6C  E8 BF 38 B6 FF                  call 0x140327830
007C3F71  48 8B F8                        mov rdi, rax
007C3F74  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007C3F79  48 85 C0                        test rax, rax
007C3F7C  75 0A                           jne 0x1407c3f88
007C3F7E  BF 9A 00 00 C0                  mov edi, 0xc000009a
007C3F83  E9 B2 00 00 00                  jmp 0x1407c403a
007C3F88  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
007C3F8C  49 89 45 00                     mov qword ptr [r13], rax
007C3F90  44 8A 6C 24 20                  mov r13b, byte ptr [rsp + 0x20]
007C3F95  45 84 ED                        test r13b, r13b
007C3F98  74 14                           je 0x1407c3fae
007C3F9A  8B 54 24 28                     mov edx, dword ptr [rsp + 0x28]
007C3F9E  41 B8 04 00 00 00               mov r8d, 4
007C3FA4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007C3FA9  E8 12 52 12 00                  call 0x1408e91c0
007C3FAE  44 8B 43 34                     mov r8d, dword ptr [rbx + 0x34]
007C3FB2  48 8B D7                        mov rdx, rdi
007C3FB5  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007C3FBA  E8 81 28 F0 FF                  call 0x1406c6840
007C3FBF  66 39 73 42                     cmp word ptr [rbx + 0x42], si
007C3FC3  76 2C                           jbe 0x1407c3ff1
007C3FC5  45 84 ED                        test r13b, r13b
007C3FC8  74 13                           je 0x1407c3fdd
007C3FCA  49 8B D4                        mov rdx, r12
007C3FCD  41 B8 02 00 00 00               mov r8d, 2
007C3FD3  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007C3FD8  E8 E3 51 12 00                  call 0x1408e91c0
007C3FDD  44 0F B7 43 42                  movzx r8d, word ptr [rbx + 0x42]
007C3FE2  48 8D 53 44                     lea rdx, [rbx + 0x44]
007C3FE6  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007C3FEB  E8 50 28 F0 FF                  call 0x1406c6840
007C3FF0  90                              nop
007C3FF1  8B FE                           mov edi, esi
007C3FF3  41 B4 01                        mov r12b, 1
007C3FF6  EB 3D                           jmp 0x1407c4035
007C3FF8  8B F8                           mov edi, eax
007C3FFA  41 B4 01                        mov r12b, 1
007C3FFD  33 F6                           xor esi, esi
007C3FFF  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
007C4004  EB 2F                           jmp 0x1407c4035
007C4006  BF 23 00 00 C0                  mov edi, 0xc0000023
007C400B  41 89 55 18                     mov dword ptr [r13 + 0x18], edx
007C400F  0F B7 43 42                     movzx eax, word ptr [rbx + 0x42]
007C4013  41 89 45 1C                     mov dword ptr [r13 + 0x1c], eax
007C4017  EB 21                           jmp 0x1407c403a
007C4019  8B F8                           mov edi, eax
007C401B  33 F6                           xor esi, esi
007C401D  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
007C4022  EB 16                           jmp 0x1407c403a
007C4024  BF 7B 00 00 C0                  mov edi, 0xc000007b
007C4029  EB 0F                           jmp 0x1407c403a
007C402B  8B F8                           mov edi, eax
007C402D  33 F6                           xor esi, esi
007C402F  44 8B FE                        mov r15d, esi
007C4032  44 8A E6                        mov r12b, sil
007C4035  45 84 E4                        test r12b, r12b
007C4038  74 36                           je 0x1407c4070
007C403A  B8 11 00 00 00                  mov eax, 0x11
007C403F  F0 48 0F B1 35 70 40 81 00      lock cmpxchg qword ptr [rip + 0x814070], rsi
007C4048  74 0C                           je 0x1407c4056
007C404A  48 8D 0D 67 40 81 00            lea rcx, [rip + 0x814067]
007C4051  E8 EA F3 A9 FF                  call 0x140263440
007C4056  48 8D 0D 5B 40 81 00            lea rcx, [rip + 0x81405b]
007C405D  E8 9E D5 B1 FF                  call 0x1402e1600
007C4062  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007C406B  E8 A0 AF A9 FF                  call 0x14025f010
007C4070  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007C4075  48 85 C9                        test rcx, rcx
007C4078  74 0A                           je 0x1407c4084
007C407A  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007C407F  E8 6C 38 C3 FF                  call 0x1403f78f0
007C4084  4D 85 FF                        test r15, r15
007C4087  74 0D                           je 0x1407c4096
007C4089  BA 57 50 42 54                  mov edx, 0x54425057
007C408E  49 8B CF                        mov rcx, r15
007C4091  E8 DA E7 3B 00                  call 0x140b82870
007C4096  8B C7                           mov eax, edi
007C4098  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
007C40A0  48 33 CC                        xor rcx, rsp
007C40A3  E8 98 85 EE FF                  call 0x1406ac640
007C40A8  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
007C40B0  49 8B 5B 28                     mov rbx, qword ptr [r11 + 0x28]
007C40B4  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
007C40B8  49 8B 7B 38                     mov rdi, qword ptr [r11 + 0x38]
007C40BC  49 8B E3                        mov rsp, r11
007C40BF  41 5F                           pop r15
007C40C1  41 5D                           pop r13
007C40C3  41 5C                           pop r12
007C40C5  C3                              ret
007C40C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpGetSystemPlatformBinary(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int8 v_stack_m98;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6580997)) ^ (v_rsp);
    v_stack_m20 = result;
    v_stack_m98 = (unsigned __int8)(a3);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_m88 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned int *)(v_rsp - 40) = 0;
    v_stack_m8C = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (a2 >= 32) goto loc_007C3C96;
loc_007C3C8C:
    goto loc_007C4035;
loc_007C3C96:
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_stack_m78 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 16);
    v_rbx = (v_rbx) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8471521, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8471490;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 8471478;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_rbx + 18;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_rip + 8471491)) != v_rbx) goto loc_007C3D2C;
loc_007C3D22:
    goto loc_007C4035;
loc_007C3D2C:
    if (*(unsigned __int64 *)(v_rip + 8471491) != 0) goto loc_007C3EB4;
    result = a1;
    if (*(unsigned __int64 *)(v_rip + 8471491) != 0) {
        a1 = v_rip + 8471406;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8471394, a2, a3, a4);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (v_stack_m90 != 0) goto loc_007C3C8C;
    if (v_stack_m88 != 0) goto loc_007C3C8C;
    v_stack_m38 = 0x41435049ULL;
    v_stack_m34 = 1;
    v_stack_m30 = 0x54425057ULL;
    a2 = 0;
    result = ExpGetSystemFirmwareTableInformation(v_stack_m38, a2, a2 + 20, v_stack_m8C);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_007C3DD4;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    v_rdi = (unsigned int)((v_rdi) & (64));
    v_rdi = (unsigned int)((v_rdi) - (0x3FFFFF85ULL));
    goto loc_007C4035;
loc_007C3DD4:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_m8C))), (unsigned int)(0x54425057ULL), v_stack_m8C);
    v_stack_m80 = result;
    if (result != 0) goto loc_007C3E01;
    goto loc_007C4035;
loc_007C3E01:
    *(unsigned int *)(result) = 0x41435049ULL;
    *(unsigned int *)(result + 4) = 1;
    *(unsigned int *)(result + 8) = 0x54425057ULL;
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(0xC000009AULL) - 16);
    a2 = 0;
    result = ExpGetSystemFirmwareTableInformation(result, a2, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), v_stack_m8C);
    if (sign_flag) goto loc_007C4035;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8471139, a2, a3, v_stack_m8C);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 8471112;
        a2 = result;
        a1 = v_rip + 8471102;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m8C);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rip + 8471121) != 0) goto loc_007C3EC9;
    *(unsigned __int64 *)(v_rip + 8471109) = result;
    v_stack_m80 = 0;
loc_007C3EA3:
loc_007C3EB4:
    if ((((unsigned __int8)((unsigned int)(v_stack_m88))) & (1)) == 0) goto loc_007C3F0A;
    goto loc_007C403A;
loc_007C3EC9:
    if (1 != v_rbx) goto loc_007C3EA3;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = 1;
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 8470994;
        result = ExfTryToWakePushLock(a1, a2, a3, v_stack_m8C);
    }
    result = KeAbPostRelease(v_rip + 8470982, a2, a3, v_stack_m8C);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, v_stack_m8C);
    goto loc_007C3D22;
loc_007C3F0A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8470991) + 64)) != 1) goto loc_007C4024;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8470991) + 65)) != 1) goto loc_007C4024;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66))) & (1)) != 0) goto loc_007C4024;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8470991) + 56) == 0) goto loc_007C4024;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8470991) + 40)) != 1) goto loc_007C4024;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8470991) + 52)))) > v_stack_m90) goto loc_007C4006;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66))) > ((unsigned int)((unsigned int)(v_stack_m88)))) goto loc_007C4006;
    v_stack_m60 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8470991) + 52));
    result = MmMapIoSpaceEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8470991) + 56), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8470991) + 52)), 2, v_stack_m8C);
    v_stack_m68 = result;
    if (result != 0) goto loc_007C3F88;
    goto loc_007C403A;
loc_007C3F88:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8470991) + 56);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8470991) + 56);
    if ((unsigned __int8)(v_stack_m98) != 0) {
        a2 = v_stack_m90;
        a3 = 4;
        a1 = v_stack_m78;
        result = ProbeForWrite(a1, a2, a3, v_stack_m8C);
    }
    result = memcpy(v_stack_m78, (unsigned int)(0xC000009AULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8470991) + 52)), v_stack_m8C);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66)) <= 0) goto loc_007C3FF1;
    if ((unsigned __int8)(v_stack_m98) != 0) {
        a2 = (unsigned int)(v_stack_m88);
        a3 = 2;
        a1 = v_stack_m70;
        result = ProbeForWrite(a1, a2, a3, v_stack_m8C);
    }
    result = memcpy(v_stack_m70, *(unsigned __int64 *)(v_rip + 8470991) + 68, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
loc_007C3FF1:
    goto loc_007C4035;
loc_007C4006:
    *(unsigned int *)(v_stack_m98 + 24) = (unsigned int)(*(unsigned __int64 *)(v_rip + 8470991) + 68);
    *(unsigned int *)(v_stack_m98 + 28) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66));
    goto loc_007C403A;
loc_007C4024:
    goto loc_007C403A;
loc_007C4035:
    if (1 == 0) goto loc_007C4070;
loc_007C403A:
    result = 17;
    if (1 != 0) {
        a1 = v_rip + 8470631;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(v_rip + 8470991) + 68, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
    }
    result = KeAbPostRelease(v_rip + 8470619, *(unsigned __int64 *)(v_rip + 8470991) + 68, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rip + 8470991) + 68, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
loc_007C4070:
    if (v_stack_m68 != 0) {
        a2 = v_stack_m60;
        result = MmUnmapIoSpace(v_stack_m68, a2, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
    }
    if (0 != 0) {
        a2 = 0x54425057ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
    }
    a1 = (v_stack_m20) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8470991) + 66), v_stack_m8C);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpGetSystemPlatformBinary(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint8_t v_stack_m98;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x646B05)) ^ (local_rsp);
    v_stack_m20 = result;
    v_stack_m98 = (uint8_t)(Arg3);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_m88 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x28) = 0;
    v_stack_m8C = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (Arg2 >= 32) goto loc_007C3C96;
loc_007C3C8C:
    goto loc_007C4035;
loc_007C3C96:
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    v_stack_m78 = *(uint64_t *)(arg1 + 0x8);
    v_stack_m70 = *(uint64_t *)(arg1 + 0x10);
    local_rbx = (local_rbx) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8471521, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8471490;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 8471478;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        Arg1 = local_rbx + 18;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_rip + 0x8143C3)) != local_rbx) goto loc_007C3D2C;
loc_007C3D22:
    goto loc_007C4035;
loc_007C3D2C:
    if (*(uint64_t *)(v_rip + 0x8143C3) != 0) goto loc_007C3EB4;
    result = Arg1;
    if (*(uint64_t *)(v_rip + 0x8143C3) != 0) {
        Arg1 = v_rip + 8471406;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(v_rip + 8471394, Arg2, Arg3, a4);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    if (v_stack_m90 != 0) goto loc_007C3C8C;
    if (v_stack_m88 != 0) goto loc_007C3C8C;
    v_stack_m38 = 0x41435049ULL;
    v_stack_m34 = 1;
    v_stack_m30 = 0x54425057ULL;
    Arg2 = 0;
    result = ExpGetSystemFirmwareTableInformation(v_stack_m38, Arg2, Arg2 + 20, v_stack_m8C);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_007C3DD4;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    local_rdi = (uint32_t)((local_rdi) & (64));
    local_rdi = (uint32_t)((local_rdi) - (0x3FFFFF85ULL));
    goto loc_007C4035;
loc_007C3DD4:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_m8C))), (uint32_t)(0x54425057ULL), v_stack_m8C);
    v_stack_m80 = result;
    if (result != 0) goto loc_007C3E01;
    goto loc_007C4035;
loc_007C3E01:
    *(uint32_t *)(result) = 0x41435049ULL;
    *(uint32_t *)(result + 0x4) = 1;
    *(uint32_t *)(result + 0x8) = 0x54425057ULL;
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(0xC000009AULL) - 16);
    Arg2 = 0;
    result = ExpGetSystemFirmwareTableInformation(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), v_stack_m8C);
    if (sign_flag) goto loc_007C4035;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8471139, Arg2, Arg3, v_stack_m8C);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 8471112;
        Arg2 = result;
        Arg1 = v_rip + 8471102;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m8C);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(v_rip + 0x814251) != 0) goto loc_007C3EC9;
    *(uint64_t *)(v_rip + 0x814245) = result;
    v_stack_m80 = 0;
loc_007C3EA3:
loc_007C3EB4:
    if ((((uint8_t)((uint32_t)(v_stack_m88))) & (1)) == 0) goto loc_007C3F0A;
    goto loc_007C403A;
loc_007C3EC9:
    if (1 != local_rbx) goto loc_007C3EA3;
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = 1;
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 8470994;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, v_stack_m8C);
    }
    result = KeAbPostRelease(v_rip + 8470982, Arg2, Arg3, v_stack_m8C);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, v_stack_m8C);
    goto loc_007C3D22;
loc_007C3F0A:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x40)) != 1) goto loc_007C4024;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x41)) != 1) goto loc_007C4024;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42))) & (1)) != 0) goto loc_007C4024;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x38) == 0) goto loc_007C4024;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x28)) != 1) goto loc_007C4024;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x34)))) > v_stack_m90) goto loc_007C4006;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42))) > ((uint32_t)((uint32_t)(v_stack_m88)))) goto loc_007C4006;
    v_stack_m60 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x34));
    result = MmMapIoSpaceEx(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x38), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x34)), 2, v_stack_m8C);
    v_stack_m68 = result;
    if (result != 0) goto loc_007C3F88;
    goto loc_007C403A;
loc_007C3F88:
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x38);
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x38);
    if ((uint8_t)(v_stack_m98) != 0) {
        Arg2 = v_stack_m90;
        Arg3 = 4;
        Arg1 = v_stack_m78;
        result = ProbeForWrite(Arg1, Arg2, Arg3, v_stack_m8C);
    }
    result = memcpy(v_stack_m78, (uint32_t)(0xC000009AULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x34)), v_stack_m8C);
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42)) <= 0) goto loc_007C3FF1;
    if ((uint8_t)(v_stack_m98) != 0) {
        Arg2 = (uint32_t)(v_stack_m88);
        Arg3 = 2;
        Arg1 = v_stack_m70;
        result = ProbeForWrite(Arg1, Arg2, Arg3, v_stack_m8C);
    }
    result = memcpy(v_stack_m70, *(uint64_t *)(v_rip + 0x8141CF) + 68, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
loc_007C3FF1:
    goto loc_007C4035;
loc_007C4006:
    *(uint32_t *)(v_stack_m98 + 0x18) = (uint32_t)(*(uint64_t *)(v_rip + 0x8141CF) + 68);
    *(uint32_t *)(v_stack_m98 + 0x1C) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42));
    goto loc_007C403A;
loc_007C4024:
    goto loc_007C403A;
loc_007C4035:
    if (1 == 0) goto loc_007C4070;
loc_007C403A:
    result = 17;
    if (1 != 0) {
        Arg1 = v_rip + 8470631;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(v_rip + 0x8141CF) + 68, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
    }
    result = KeAbPostRelease(v_rip + 8470619, *(uint64_t *)(v_rip + 0x8141CF) + 68, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_rip + 0x8141CF) + 68, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
loc_007C4070:
    if (v_stack_m68 != 0) {
        Arg2 = v_stack_m60;
        result = MmUnmapIoSpace(v_stack_m68, Arg2, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
    }
    if (0 != 0) {
        Arg2 = 0x54425057ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
    }
    Arg1 = (v_stack_m20) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8141CF) + 0x42), v_stack_m8C);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C3C18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
