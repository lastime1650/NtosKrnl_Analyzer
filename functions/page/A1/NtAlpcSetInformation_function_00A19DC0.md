# NtAlpcSetInformation

- RVA: `0x00A19DC0`–`0x00A1A285` (길이 `1,221` bytes)
- VA: `0x0000000140A19DC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AA3F4`
- 디코드: `296`개 명령, `1,221/1,221` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A19E03` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A19E8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A19EC8` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A19EFB` → [AlpcpAssociateIoCompletionPort](AlpcpAssociateIoCompletionPort_function_00A1A28C.md) (function, `0x00A1A28C`)
- `0x00A19F07` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A19F0C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A19F1E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A19F87` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A19FA7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00A19FCE` → [AlpcpAdjustCompletionListConcurrencyCount](AlpcpAdjustCompletionListConcurrencyCount_function_00A1A62C.md) (function, `0x00A1A62C`)
- `0x00A19FE2` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00A1A04A` → [AlpcpInitializeCompletionList](AlpcpInitializeCompletionList_function_00A1A6D0.md) (function, `0x00A1A6D0`)
- `0x00A1A090` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A1A0A9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A1A0E7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A1A105` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A1A11E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A1A13B` → [AlpcpFreeCompletionList](AlpcpFreeCompletionList_function_00A1AD08.md) (function, `0x00A1AD08`)
- `0x00A1A150` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A1A173` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A1A180` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A1A1AA` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A1A1C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A1A1E0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A19DD3` → RVA `0x00E0A740` (`.data`; read)
- `0x00A19EA0` → RVA `0x00FC6C18` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00A19E03` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A19E8A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A19F07` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A19F0C` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A19F1E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A19F87` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A19FA7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00A19FE2` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00A1A090` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A1A0A9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A1A0E7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A1A105` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A1A11E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A1A150` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A1A173` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A1A180` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A1A1AA` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A1A1C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A1A1E0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00A1A1D1` → [sub_00B372D4](../B3/Unknown_function_00B372D4.md) (`tail-transfer`)
  - `0x00A1A1E6` → [sub_00B372D4](../B3/Unknown_function_00B372D4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A19DC0  40 53                           push rbx
00A19DC2  56                              push rsi
00A19DC3  57                              push rdi
00A19DC4  41 54                           push r12
00A19DC6  41 55                           push r13
00A19DC8  41 56                           push r14
00A19DCA  41 57                           push r15
00A19DCC  48 81 EC C0 00 00 00            sub rsp, 0xc0
00A19DD3  48 8B 05 66 09 3F 00            mov rax, qword ptr [rip + 0x3f0966]
00A19DDA  48 33 C4                        xor rax, rsp
00A19DDD  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00A19DE5  45 8B F9                        mov r15d, r9d
00A19DE8  44 8B F2                        mov r14d, edx
00A19DEB  48 8B F9                        mov rdi, rcx
00A19DEE  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00A19DF3  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00A19DF8  33 D2                           xor edx, edx
00A19DFA  44 8D 42 48                     lea r8d, [rdx + 0x48]
00A19DFE  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00A19E03  E8 38 CE CA FF                  call 0x1406c6c40
00A19E08  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A19E11  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A19E15  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
00A19E1C  90                              nop
00A19E1D  33 F6                           xor esi, esi
00A19E1F  48 85 FF                        test rdi, rdi
00A19E22  0F 84 DB 01 00 00               je 0x140a1a003
00A19E28  48 39 74 24 40                  cmp qword ptr [rsp + 0x40], rsi
00A19E2D  0F 84 BC 01 00 00               je 0x140a19fef
00A19E33  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A19E3C  40 8A B8 32 02 00 00            mov dil, byte ptr [rax + 0x232]
00A19E43  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00A19E48  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00A19E4D  4D 8B E5                        mov r12, r13
00A19E50  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00A19E55  45 85 FF                        test r15d, r15d
00A19E58  74 46                           je 0x140a19ea0
00A19E5A  40 84 FF                        test dil, dil
00A19E5D  74 41                           je 0x140a19ea0
00A19E5F  41 83 FF 48                     cmp r15d, 0x48
00A19E63  0F 87 1E 03 00 00               ja 0x140a1a187
00A19E69  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00A19E73  4C 3B E8                        cmp r13, rax
00A19E76  4C 0F 43 E8                     cmovae r13, rax
00A19E7A  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00A19E7F  4D 8B C7                        mov r8, r15
00A19E82  49 8B D5                        mov rdx, r13
00A19E85  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00A19E8A  E8 B1 C9 CA FF                  call 0x1406c6840
00A19E8F  90                              nop
00A19E90  4C 8D 64 24 60                  lea r12, [rsp + 0x60]
00A19E95  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00A19E9A  EB 04                           jmp 0x140a19ea0
00A19E9C  8B F8                           mov edi, eax
00A19E9E  EB 6C                           jmp 0x140a19f0c
00A19EA0  4C 8B 05 71 CD 5A 00            mov r8, qword ptr [rip + 0x5acd71]
00A19EA7  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A19EAC  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A19EB1  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00A19EB6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A19EBB  44 8A CF                        mov r9b, dil
00A19EBE  BA 01 00 00 00                  mov edx, 1
00A19EC3  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A19EC8  E8 E3 EE E4 FF                  call 0x140868db0
00A19ECD  8B F8                           mov edi, eax
00A19ECF  85 C0                           test eax, eax
00A19ED1  78 39                           js 0x140a19f0c
00A19ED3  41 83 EE 01                     sub r14d, 1
00A19ED7  0F 84 6A 03 00 00               je 0x140a1a247
00A19EDD  41 83 EE 01                     sub r14d, 1
00A19EE1  75 54                           jne 0x140a19f37
00A19EE3  41 83 FF 10                     cmp r15d, 0x10
00A19EE7  0F 85 79 02 00 00               jne 0x140a1a166
00A19EED  4D 8B 04 24                     mov r8, qword ptr [r12]
00A19EF1  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00A19EF6  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A19EFB  E8 8C 03 00 00                  call 0x140a1a28c
00A19F00  8B F8                           mov edi, eax
00A19F02  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A19F07  E8 44 F4 8D FF                  call 0x1402f9350
00A19F0C  E8 9F 39 84 FF                  call 0x14025d8b0
00A19F11  8B C7                           mov eax, edi
00A19F13  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00A19F1B  48 33 CC                        xor rcx, rsp
00A19F1E  E8 1D 27 C9 FF                  call 0x1406ac640
00A19F23  48 81 C4 C0 00 00 00            add rsp, 0xc0
00A19F2A  41 5F                           pop r15
00A19F2C  41 5E                           pop r14
00A19F2E  41 5D                           pop r13
00A19F30  41 5C                           pop r12
00A19F32  5F                              pop rdi
00A19F33  5E                              pop rsi
00A19F34  5B                              pop rbx
00A19F35  C3                              ret
00A19F36  CC                              int3
00A19F37  41 83 EE 03                     sub r14d, 3
00A19F3B  0F 84 F1 02 00 00               je 0x140a1a232
00A19F41  41 83 EE 01                     sub r14d, 1
00A19F45  0F 84 C2 00 00 00               je 0x140a1a00d
00A19F4B  41 83 EE 01                     sub r14d, 1
00A19F4F  0F 84 FF 00 00 00               je 0x140a1a054
00A19F55  41 83 EE 01                     sub r14d, 1
00A19F59  0F 85 08 01 00 00               jne 0x140a1a067
00A19F5F  41 83 FF 04                     cmp r15d, 4
00A19F63  0F 85 F4 00 00 00               jne 0x140a1a05d
00A19F69  41 39 34 24                     cmp dword ptr [r12], esi
00A19F6D  0F 84 EA 00 00 00               je 0x140a1a05d
00A19F73  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00A19F78  48 81 C3 60 01 00 00            add rbx, 0x160
00A19F7F  45 33 C0                        xor r8d, r8d
00A19F82  33 D2                           xor edx, edx
00A19F84  48 8B CB                        mov rcx, rbx
00A19F87  E8 A4 62 7F FF                  call 0x140210230
00A19F8C  48 8B F8                        mov rdi, rax
00A19F8F  33 C0                           xor eax, eax
00A19F91  45 8D 77 0D                     lea r14d, [r15 + 0xd]
00A19F95  F0 4C 0F B1 33                  lock cmpxchg qword ptr [rbx], r14
00A19F9A  74 10                           je 0x140a19fac
00A19F9C  4C 8B CB                        mov r9, rbx
00A19F9F  4C 8B C7                        mov r8, rdi
00A19FA2  33 D2                           xor edx, edx
00A19FA4  48 8B CB                        mov rcx, rbx
00A19FA7  E8 A0 64 7F FF                  call 0x14021044c
00A19FAC  48 85 FF                        test rdi, rdi
00A19FAF  74 04                           je 0x140a19fb5
00A19FB1  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00A19FB5  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A19FBA  48 39 B1 68 01 00 00            cmp qword ptr [rcx + 0x168], rsi
00A19FC1  0F 84 95 01 00 00               je 0x140a1a15c
00A19FC7  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00A19FCC  8B 12                           mov edx, dword ptr [rdx]
00A19FCE  E8 59 06 00 00                  call 0x140a1a62c
00A19FD3  8B FE                           mov edi, esi
00A19FD5  49 8B C6                        mov rax, r14
00A19FD8  F0 48 0F B1 33                  lock cmpxchg qword ptr [rbx], rsi
00A19FDD  74 08                           je 0x140a19fe7
00A19FDF  48 8B CB                        mov rcx, rbx
00A19FE2  E8 59 94 84 FF                  call 0x140263440
00A19FE7  48 8B CB                        mov rcx, rbx
00A19FEA  E9 F8 00 00 00                  jmp 0x140a1a0e7
00A19FEF  41 83 FE 07                     cmp r14d, 7
00A19FF3  0F 84 3A FE FF FF               je 0x140a19e33
00A19FF9  41 83 FE 0A                     cmp r14d, 0xa
00A19FFD  0F 84 30 FE FF FF               je 0x140a19e33
00A1A003  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1A008  E9 FF FE FF FF                  jmp 0x140a19f0c
00A1A00D  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00A1A012  8B 88 A0 01 00 00               mov ecx, dword ptr [rax + 0x1a0]
00A1A018  80 E1 06                        and cl, 6
00A1A01B  80 F9 02                        cmp cl, 2
00A1A01E  75 3D                           jne 0x140a1a05d
00A1A020  41 83 FF 18                     cmp r15d, 0x18
00A1A024  0F 85 C1 01 00 00               jne 0x140a1a1eb
00A1A02A  49 8B 14 24                     mov rdx, qword ptr [r12]
00A1A02E  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00A1A032  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00A1A037  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A1A03B  45 8B 4C 24 0C                  mov r9d, dword ptr [r12 + 0xc]
00A1A040  45 8B 44 24 08                  mov r8d, dword ptr [r12 + 8]
00A1A045  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A1A04A  E8 81 06 00 00                  call 0x140a1a6d0
00A1A04F  E9 AC FE FF FF                  jmp 0x140a19f00
00A1A054  45 85 FF                        test r15d, r15d
00A1A057  0F 84 94 00 00 00               je 0x140a1a0f1
00A1A05D  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1A062  E9 9B FE FF FF                  jmp 0x140a19f02
00A1A067  41 83 EE 01                     sub r14d, 1
00A1A06B  0F 84 2A 01 00 00               je 0x140a1a19b
00A1A071  41 83 FE 01                     cmp r14d, 1
00A1A075  75 E6                           jne 0x140a1a05d
00A1A077  45 85 FF                        test r15d, r15d
00A1A07A  75 E1                           jne 0x140a1a05d
00A1A07C  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00A1A081  49 81 C6 60 01 00 00            add r14, 0x160
00A1A088  45 33 C0                        xor r8d, r8d
00A1A08B  33 D2                           xor edx, edx
00A1A08D  49 8B CE                        mov rcx, r14
00A1A090  E8 9B 61 7F FF                  call 0x140210230
00A1A095  48 8B F8                        mov rdi, rax
00A1A098  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00A1A09E  73 0E                           jae 0x140a1a0ae
00A1A0A0  4D 8B C6                        mov r8, r14
00A1A0A3  48 8B D0                        mov rdx, rax
00A1A0A6  49 8B CE                        mov rcx, r14
00A1A0A9  E8 E2 5B 7F FF                  call 0x14020fc90
00A1A0AE  48 85 FF                        test rdi, rdi
00A1A0B1  74 04                           je 0x140a1a0b7
00A1A0B3  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00A1A0B7  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00A1A0BC  48 39 B0 68 01 00 00            cmp qword ptr [rax + 0x168], rsi
00A1A0C3  0F 84 C8 00 00 00               je 0x140a1a191
00A1A0C9  0F BA B0 A0 01 00 00 10         btr dword ptr [rax + 0x1a0], 0x10
00A1A0D1  8B FE                           mov edi, esi
00A1A0D3  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
00A1A0D8  80 E3 06                        and bl, 6
00A1A0DB  80 FB 02                        cmp bl, 2
00A1A0DE  0F 84 8C 00 00 00               je 0x140a1a170
00A1A0E4  49 8B CE                        mov rcx, r14
00A1A0E7  E8 14 75 8C FF                  call 0x1402e1600
00A1A0EC  E9 11 FE FF FF                  jmp 0x140a19f02
00A1A0F1  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00A1A0F6  48 81 C7 60 01 00 00            add rdi, 0x160
00A1A0FD  45 33 C0                        xor r8d, r8d
00A1A100  33 D2                           xor edx, edx
00A1A102  48 8B CF                        mov rcx, rdi
00A1A105  E8 26 61 7F FF                  call 0x140210230
00A1A10A  4C 8B F0                        mov r14, rax
00A1A10D  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00A1A113  73 0E                           jae 0x140a1a123
00A1A115  4C 8B C7                        mov r8, rdi
00A1A118  48 8B D0                        mov rdx, rax
00A1A11B  48 8B CF                        mov rcx, rdi
00A1A11E  E8 6D 5B 7F FF                  call 0x14020fc90
00A1A123  4D 85 F6                        test r14, r14
00A1A126  74 05                           je 0x140a1a12d
00A1A128  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
00A1A12D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00A1A132  48 39 B1 68 01 00 00            cmp qword ptr [rcx + 0x168], rsi
00A1A139  74 05                           je 0x140a1a140
00A1A13B  E8 C8 0B 00 00                  call 0x140a1ad08
00A1A140  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00A1A145  80 E3 06                        and bl, 6
00A1A148  80 FB 02                        cmp bl, 2
00A1A14B  74 30                           je 0x140a1a17d
00A1A14D  48 8B CF                        mov rcx, rdi
00A1A150  E8 AB 74 8C FF                  call 0x1402e1600
00A1A155  8B FE                           mov edi, esi
00A1A157  E9 A6 FD FF FF                  jmp 0x140a19f02
00A1A15C  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1A161  E9 6F FE FF FF                  jmp 0x140a19fd5
00A1A166  BF 04 00 00 C0                  mov edi, 0xc0000004
00A1A16B  E9 92 FD FF FF                  jmp 0x140a19f02
00A1A170  49 8B CE                        mov rcx, r14
00A1A173  E8 58 BC 84 FF                  call 0x140265dd0
00A1A178  E9 67 FF FF FF                  jmp 0x140a1a0e4
00A1A17D  48 8B CF                        mov rcx, rdi
00A1A180  E8 4B BC 84 FF                  call 0x140265dd0
00A1A185  EB C6                           jmp 0x140a1a14d
00A1A187  BF 04 00 00 C0                  mov edi, 0xc0000004
00A1A18C  E9 7B FD FF FF                  jmp 0x140a19f0c
00A1A191  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1A196  E9 38 FF FF FF                  jmp 0x140a1a0d3
00A1A19B  40 38 74 24 30                  cmp byte ptr [rsp + 0x30], sil
00A1A1A0  0F 85 B7 FE FF FF               jne 0x140a1a05d
00A1A1A6  49 8B 4D 00                     mov rcx, qword ptr [r13]
00A1A1AA  E8 71 58 7F FF                  call 0x14020fa20
00A1A1AF  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00A1A1B4  48 81 C7 60 01 00 00            add rdi, 0x160
00A1A1BB  45 33 C0                        xor r8d, r8d
00A1A1BE  33 D2                           xor edx, edx
00A1A1C0  48 8B CF                        mov rcx, rdi
00A1A1C3  E8 68 60 7F FF                  call 0x140210230
00A1A1C8  4C 8B F0                        mov r14, rax
00A1A1CB  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00A1A1D1  0F 83 FD D0 11 00               jae 0x140b372d4
00A1A1D7  4C 8B C7                        mov r8, rdi
00A1A1DA  48 8B D0                        mov rdx, rax
00A1A1DD  48 8B CF                        mov rcx, rdi
00A1A1E0  E8 AB 5A 7F FF                  call 0x14020fc90
00A1A1E5  90                              nop
00A1A1E6  E9 E9 D0 11 00                  jmp 0x140b372d4
00A1A1EB  41 83 FF 10                     cmp r15d, 0x10
00A1A1EF  0F 85 68 FE FF FF               jne 0x140a1a05d
00A1A1F5  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00A1A1FA  4C 8D 64 24 60                  lea r12, [rsp + 0x60]
00A1A1FF  66 48 0F 7E C0                  movq rax, xmm0
00A1A204  8B D0                           mov edx, eax
00A1A206  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00A1A20B  48 C1 E8 20                     shr rax, 0x20
00A1A20F  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A1A213  66 0F 73 D8 08                  psrldq xmm0, 8
00A1A218  66 48 0F 7E C0                  movq rax, xmm0
00A1A21D  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00A1A221  48 C1 E8 20                     shr rax, 0x20
00A1A225  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00A1A229  41 8D 77 F1                     lea esi, [r15 - 0xf]
00A1A22D  E9 FC FD FF FF                  jmp 0x140a1a02e
00A1A232  41 83 EF 10                     sub r15d, 0x10
00A1A236  41 F7 DF                        neg r15d
00A1A239  1B C0                           sbb eax, eax
00A1A23B  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1A240  23 F8                           and edi, eax
00A1A242  E9 BB FC FF FF                  jmp 0x140a19f02
00A1A247  41 83 FF 48                     cmp r15d, 0x48
00A1A24B  0F 85 15 FF FF FF               jne 0x140a1a166
00A1A251  45 8B 04 24                     mov r8d, dword ptr [r12]
00A1A255  41 F7 C0 FF FF 00 FC            test r8d, 0xfc00ffff
00A1A25C  0F 85 FB FD FF FF               jne 0x140a1a05d
00A1A262  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00A1A267  8B 82 00 01 00 00               mov eax, dword ptr [rdx + 0x100]
00A1A26D  8B C8                           mov ecx, eax
00A1A26F  41 33 C8                        xor ecx, r8d
00A1A272  81 E1 00 00 02 00               and ecx, 0x20000
00A1A278  33 C8                           xor ecx, eax
00A1A27A  89 8A 00 01 00 00               mov dword ptr [rdx + 0x100], ecx
00A1A280  E9 7D FC FF FF                  jmp 0x140a19f02
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtAlpcSetInformation(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 4131174)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mB0 = a1;
    v_stack_mB8 = a3;
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 72, a4);
    v_rbx = (v_rbx) | (-1);
    v_rsi = 0;
    if (a1 == 0) goto loc_00A1A003;
    if (v_stack_mB8 == 0) goto loc_00A19FEF;
loc_00A19E33:
    v_stack_mC8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mA8 = v_stack_mB8;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00A19EA0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00A19EA0;
    if (((unsigned int)((unsigned int)(a4))) > 72) goto loc_00A1A187;
    v_r13 = v_stack_mB8;
    if (v_stack_mB8 >= (*(unsigned __int64 *)(gs_base + (0 + 392)))) { v_r13 = *(unsigned __int64 *)(gs_base + (0 + 392)); }
    v_stack_mB8 = v_r13;
    result = memcpy(v_stack_m98, v_r13, (unsigned int)(a4), a4);
    v_stack_mA8 = v_stack_m98;
    goto loc_00A19EA0;
loc_00A19EA0:
    v_stack_mC0 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = v_stack_mC0;
    result = ObReferenceObjectByHandle(v_stack_mB0, 1, *(unsigned __int64 *)(v_rip + 5950833), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00A19F0C;
    v_r14 = (unsigned int)(((unsigned int)(a2)) - (1));
    if (condition_is_equal) goto loc_00A1A247;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_not_equal) goto loc_00A19F37;
    if (((unsigned int)((unsigned int)(a4))) != 16) goto loc_00A1A166;
    result = AlpcpAssociateIoCompletionPort(v_stack_mC0, *(unsigned __int64 *)(v_stack_m98 + 8), *(unsigned __int64 *)(v_stack_m98), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_00A19F00:
loc_00A19F02:
    result = ObfDereferenceObject(v_stack_mC0, *(unsigned __int64 *)(v_stack_m98 + 8), *(unsigned __int64 *)(v_stack_m98), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_00A19F0C:
    result = KeLeaveCriticalRegion(v_stack_mC0, *(unsigned __int64 *)(v_stack_m98 + 8), *(unsigned __int64 *)(v_stack_m98), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_stack_m98 + 8), *(unsigned __int64 *)(v_stack_m98), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_rsp = (v_rsp) + (192);
    return result;
loc_00A19F37:
    v_r14 = (unsigned int)((v_r14) - (3));
    if (condition_is_equal) goto loc_00A1A232;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00A1A00D;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_equal) goto loc_00A1A054;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (condition_is_not_equal) goto loc_00A1A067;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00A1A05D;
    if ((*(unsigned int *)(v_stack_m98)) == 0) goto loc_00A1A05D;
    v_rbx = (v_stack_p38) + (352);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_stack_p38 + 360)) == 0) goto loc_00A1A15C;
    result = AlpcpAdjustCompletionListConcurrencyCount(v_stack_p38, (unsigned int)(*(unsigned int *)(v_stack_p50)), a3, a4);
loc_00A19FD5:
    result = (unsigned int)(a4) + 13;
    if ((*(unsigned __int64 *)(v_stack_p38 + 360)) != 0) {
        a1 = v_rbx;
        result = ExfReleasePushLockShared(a1, (unsigned int)(*(unsigned int *)(v_stack_p50)), a3, a4);
    }
    goto loc_00A1A0E7;
loc_00A19FEF:
    if (((unsigned int)((unsigned int)(a4) + 13)) == 7) goto loc_00A19E33;
    if (((unsigned int)((unsigned int)(a4) + 13)) == 10) goto loc_00A19E33;
loc_00A1A003:
    goto loc_00A19F0C;
loc_00A1A00D:
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p38 + 416))) & (6));
    if (((unsigned __int8)(a1)) != 2) goto loc_00A1A05D;
    if (((unsigned int)((unsigned int)(a4))) != 24) goto loc_00A1A1EB;
loc_00A1A02E:
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + 16)));
    result = AlpcpInitializeCompletionList(v_stack_p38, *(unsigned __int64 *)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m98 + 8)), (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    goto loc_00A19F00;
loc_00A1A054:
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00A1A0F1;
loc_00A1A05D:
    goto loc_00A19F02;
loc_00A1A067:
    v_r14 = (unsigned int)(((unsigned int)(a4) + 13) - (1));
    if (condition_is_equal) goto loc_00A1A19B;
    if (((unsigned int)(v_r14)) != 1) goto loc_00A1A05D;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_00A1A05D;
    v_r14 = (v_stack_p38) + (352);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r14, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r14;
        a2 = result;
        a1 = v_r14;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_stack_p38 + 360)) == 0) goto loc_00A1A191;
loc_00A1A0D3:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00A1A170;
loc_00A1A0E4:
loc_00A1A0E7:
    result = KeAbPostRelease(v_r14, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    goto loc_00A19F02;
loc_00A1A0F1:
    v_rdi = (v_stack_p38) + (352);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_stack_p38 + 360)) != 0) {
        result = AlpcpFreeCompletionList(v_stack_p38, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    }
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00A1A17D;
loc_00A1A14D:
    result = KeAbPostRelease(v_rdi, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    goto loc_00A19F02;
loc_00A1A15C:
    goto loc_00A19FD5;
loc_00A1A166:
    goto loc_00A19F02;
loc_00A1A170:
    result = ExfTryToWakePushLock(result, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    goto loc_00A1A0E4;
loc_00A1A17D:
    result = ExfTryToWakePushLock((unsigned int)(0xC0000004ULL), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    goto loc_00A1A14D;
loc_00A1A187:
    goto loc_00A19F0C;
loc_00A1A191:
    goto loc_00A1A0D3;
loc_00A1A19B:
    if (v_stack_p30 != 0) goto loc_00A1A05D;
    result = ObfReferenceObject(*(unsigned __int64 *)(v_r13), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    v_rdi = (v_stack_p38) + (352);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
    result = ExfAcquirePushLockExclusiveEx(v_rdi, result, v_rdi, (unsigned int)(*(unsigned int *)(v_stack_m98 + 12)));
loc_00A1A1EB:
    if (((unsigned int)((unsigned int)(a4))) != 16) goto loc_00A1A05D;
    v_stack_p60 = (unsigned int)((unsigned int)(result));
    result = (result) >> (32);
    v_stack_p68 = (unsigned int)(result);
    v_stack_p6C = (unsigned int)(result);
    result = (result) >> (32);
    v_stack_p70 = (unsigned int)(result);
    goto loc_00A1A02E;
loc_00A1A232:
    v_r15 = (unsigned int)(((unsigned int)(a4)) - (16));
    v_r15 = (unsigned int)(-(v_r15));
    v_rdi = (unsigned int)(((unsigned int)(0xC000000DULL)) & ((unsigned int)(result)));
    goto loc_00A19F02;
loc_00A1A247:
    if (((unsigned int)(v_r15)) != 72) goto loc_00A1A166;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60)))) & (0xFC00FFFFULL)) != 0) goto loc_00A1A05D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p38 + 256))))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60)))));
    a1 = (unsigned int)((a1) & (0x20000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p38 + 256)))));
    *(unsigned int *)(v_stack_p38 + 256) = (unsigned int)(a1);
    goto loc_00A19F02;
}
```

## 5. (Beta) C Style

```c
int64_t NtAlpcSetInformation(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x3F0966)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mB0 = Arg1;
    v_stack_mB8 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 72, Arg4);
    local_rbx = (local_rbx) | (-1);
    local_rsi = 0;
    if (Arg1 == 0) goto loc_00A1A003;
    if (v_stack_mB8 == 0) goto loc_00A19FEF;
loc_00A19E33:
    v_stack_mC8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mA8 = v_stack_mB8;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00A19EA0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00A19EA0;
    if (((uint32_t)((uint32_t)(Arg4))) > 72) goto loc_00A1A187;
    local_r13 = v_stack_mB8;
    if (v_stack_mB8 >= (*(uint64_t *)(gs_base + (0 + 0x188)))) { local_r13 = *(uint64_t *)(gs_base + (0 + 0x188)); }
    v_stack_mB8 = local_r13;
    result = memcpy(v_stack_m98, local_r13, (uint32_t)(Arg4), Arg4);
    v_stack_mA8 = v_stack_m98;
    goto loc_00A19EA0;
loc_00A19EA0:
    v_stack_mC0 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = v_stack_mC0;
    result = ObReferenceObjectByHandle(v_stack_mB0, 1, *(uint64_t *)(v_rip + 0x5ACD71), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00A19F0C;
    local_r14 = (uint32_t)(((uint32_t)(Arg2)) - (1));
    if (condition_is_equal) goto loc_00A1A247;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_not_equal) goto loc_00A19F37;
    if (((uint32_t)((uint32_t)(Arg4))) != 16) goto loc_00A1A166;
    result = AlpcpAssociateIoCompletionPort(v_stack_mC0, *(uint64_t *)(v_stack_m98 + 0x8), *(uint64_t *)(v_stack_m98), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_00A19F00:
loc_00A19F02:
    result = ObfDereferenceObject(v_stack_mC0, *(uint64_t *)(v_stack_m98 + 0x8), *(uint64_t *)(v_stack_m98), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_00A19F0C:
    result = KeLeaveCriticalRegion(v_stack_mC0, *(uint64_t *)(v_stack_m98 + 0x8), *(uint64_t *)(v_stack_m98), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_stack_m98 + 0x8), *(uint64_t *)(v_stack_m98), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_rsp = (local_rsp) + (192);
    return result;
loc_00A19F37:
    local_r14 = (uint32_t)((local_r14) - (3));
    if (condition_is_equal) goto loc_00A1A232;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00A1A00D;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_equal) goto loc_00A1A054;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (condition_is_not_equal) goto loc_00A1A067;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00A1A05D;
    if ((*(uint32_t *)(v_stack_m98)) == 0) goto loc_00A1A05D;
    local_rbx = (v_stack_p38) + (352);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rbx;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_stack_p38 + 0x168)) == 0) goto loc_00A1A15C;
    result = AlpcpAdjustCompletionListConcurrencyCount(v_stack_p38, (uint32_t)(*(uint32_t *)(v_stack_p50)), Arg3, Arg4);
loc_00A19FD5:
    result = (uint32_t)(Arg4) + 13;
    if ((*(uint64_t *)(v_stack_p38 + 0x168)) != 0) {
        Arg1 = local_rbx;
        result = ExfReleasePushLockShared(Arg1, (uint32_t)(*(uint32_t *)(v_stack_p50)), Arg3, Arg4);
    }
    goto loc_00A1A0E7;
loc_00A19FEF:
    if (((uint32_t)((uint32_t)(Arg4) + 13)) == 7) goto loc_00A19E33;
    if (((uint32_t)((uint32_t)(Arg4) + 13)) == 10) goto loc_00A19E33;
loc_00A1A003:
    goto loc_00A19F0C;
loc_00A1A00D:
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + 0x1A0))) & (6));
    if (((uint8_t)(Arg1)) != 2) goto loc_00A1A05D;
    if (((uint32_t)((uint32_t)(Arg4))) != 24) goto loc_00A1A1EB;
loc_00A1A02E:
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x10)));
    result = AlpcpInitializeCompletionList(v_stack_p38, *(uint64_t *)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m98 + 0x8)), (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    goto loc_00A19F00;
loc_00A1A054:
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00A1A0F1;
loc_00A1A05D:
    goto loc_00A19F02;
loc_00A1A067:
    local_r14 = (uint32_t)(((uint32_t)(Arg4) + 13) - (1));
    if (condition_is_equal) goto loc_00A1A19B;
    if (((uint32_t)(local_r14)) != 1) goto loc_00A1A05D;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_00A1A05D;
    local_r14 = (v_stack_p38) + (352);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r14, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r14;
        Arg2 = result;
        Arg1 = local_r14;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_stack_p38 + 0x168)) == 0) goto loc_00A1A191;
loc_00A1A0D3:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00A1A170;
loc_00A1A0E4:
loc_00A1A0E7:
    result = KeAbPostRelease(local_r14, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    goto loc_00A19F02;
loc_00A1A0F1:
    local_rdi = (v_stack_p38) + (352);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_stack_p38 + 0x168)) != 0) {
        result = AlpcpFreeCompletionList(v_stack_p38, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    }
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00A1A17D;
loc_00A1A14D:
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    goto loc_00A19F02;
loc_00A1A15C:
    goto loc_00A19FD5;
loc_00A1A166:
    goto loc_00A19F02;
loc_00A1A170:
    result = ExfTryToWakePushLock(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    goto loc_00A1A0E4;
loc_00A1A17D:
    result = ExfTryToWakePushLock((uint32_t)(0xC0000004ULL), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    goto loc_00A1A14D;
loc_00A1A187:
    goto loc_00A19F0C;
loc_00A1A191:
    goto loc_00A1A0D3;
loc_00A1A19B:
    if (v_stack_p30 != 0) goto loc_00A1A05D;
    result = ObfReferenceObject(*(uint64_t *)(local_r13), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    local_rdi = (v_stack_p38) + (352);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
    result = ExfAcquirePushLockExclusiveEx(local_rdi, result, local_rdi, (uint32_t)(*(uint32_t *)(v_stack_m98 + 0xC)));
loc_00A1A1EB:
    if (((uint32_t)((uint32_t)(Arg4))) != 16) goto loc_00A1A05D;
    v_stack_p60 = (uint32_t)((uint32_t)(result));
    result = (result) >> (32);
    v_stack_p68 = (uint32_t)(result);
    v_stack_p6C = (uint32_t)(result);
    result = (result) >> (32);
    v_stack_p70 = (uint32_t)(result);
    goto loc_00A1A02E;
loc_00A1A232:
    local_r15 = (uint32_t)(((uint32_t)(Arg4)) - (16));
    local_r15 = (uint32_t)(-(local_r15));
    local_rdi = (uint32_t)(((uint32_t)(0xC000000DULL)) & ((uint32_t)(result)));
    goto loc_00A19F02;
loc_00A1A247:
    if (((uint32_t)(local_r15)) != 72) goto loc_00A1A166;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60)))) & (0xFC00FFFFULL)) != 0) goto loc_00A1A05D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0x100))))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60)))));
    Arg1 = (uint32_t)((Arg1) & (0x20000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0x100)))));
    *(uint32_t *)(v_stack_p38 + 0x100) = (uint32_t)(Arg1);
    goto loc_00A19F02;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A19DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
