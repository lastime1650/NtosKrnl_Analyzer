# AlpcpCreateClientPort

- RVA: `0x009270AC`–`0x009275DB` (길이 `1,327` bytes)
- VA: `0x00000001409270AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008D5B0`
- 디코드: `336`개 명령, `1,327/1,327` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0092712A` → [ObReferenceObjectByName](../8C/ObReferenceObjectByName_function_008C4A00.md) (function, `0x008C4A00`)
- `0x0092717F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009271A0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009271CC` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x009271E0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009271E8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00927206` → [AlpcpCheckConnectionSecurity](../A2/AlpcpCheckConnectionSecurity_function_00A227A0.md) (function, `0x00A227A0`)
- `0x00927215` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0092725A` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x00927275` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092729F` → [AlpcpInitializePort](AlpcpInitializePort_function_00925DC4.md) (function, `0x00925DC4`)
- `0x009272C7` → [AlpcpAllocateBlob](../89/AlpcpAllocateBlob_function_008925B0.md) (function, `0x008925B0`)
- `0x009272F9` → [AlpcpLockBlobExclusive](AlpcpLockBlobExclusive_function_009253A4.md) (function, `0x009253A4`)
- `0x0092730D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00927327` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00927378` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00927381` → [AlpcpUnlockBlobUncachedExclusive](AlpcpUnlockBlobUncachedExclusive_function_0092536C.md) (function, `0x0092536C`)
- `0x0092738B` → [AlpcInitializeHandleTable](AlpcInitializeHandleTable_function_00925D70.md) (function, `0x00925D70`)
- `0x009273CD` → [AlpcpValidateAndSetPortAttributes](../9E/AlpcpValidateAndSetPortAttributes_function_009E73BC.md) (function, `0x009E73BC`)
- `0x009273E5` → [AlpcpAllocateMessage](../89/AlpcpAllocateMessage_function_008926C0.md) (function, `0x008926C0`)
- `0x0092740B` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0092744C` → [AlpcpSetOwnerProcessPort](../9E/AlpcpSetOwnerProcessPort_function_009E761C.md) (function, `0x009E761C`)
- `0x00927465` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0092748B` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x009274EA` → [ObReferenceObjectByNameEx](../8B/ObReferenceObjectByNameEx_function_008BD524.md) (function, `0x008BD524`)
- `0x0092751D` → [SeCreateClientSecurity](../89/SeCreateClientSecurity_function_008911B0.md) (function, `0x008911B0`)
- `0x00927548` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00927565` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00927578` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00927587` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0092758F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009275A2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [NtSecureConnectPort](NtSecureConnectPort_function_00922F20.md) at `0x00923225`
- [AlpcpConnectPort](AlpcpConnectPort_function_00926C8C.md) at `0x00926EDA`

### Static image references
- `0x0092710E` → RVA `0x00FC6C18` (`ALMOSTRO`; read)
- `0x009272BB` → RVA `0x000020A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x0092717F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009271A0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009271CC` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x009271E0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009271E8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00927215` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00927275` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092730D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00927327` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00927378` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00927465` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00927548` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00927565` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00927578` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00927587` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0092758F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009275A2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00927556` → [sub_00B22BF8](../B2/Unknown_function_00B22BF8.md) (`tail-transfer`)
  - `0x0092756B` → [sub_00B22BF8](../B2/Unknown_function_00B22BF8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009270AC  4C 8B DC                        mov r11, rsp
009270AF  49 89 5B 20                     mov qword ptr [r11 + 0x20], rbx
009270B3  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
009270B7  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
009270BB  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
009270BF  55                              push rbp
009270C0  56                              push rsi
009270C1  57                              push rdi
009270C2  41 54                           push r12
009270C4  41 55                           push r13
009270C6  41 56                           push r14
009270C8  41 57                           push r15
009270CA  48 8B EC                        mov rbp, rsp
009270CD  48 83 EC 70                     sub rsp, 0x70
009270D1  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
009270D5  33 F6                           xor esi, esi
009270D7  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
009270DB  4D 8B D1                        mov r10, r9
009270DE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009270E7  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
009270EB  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
009270EF  44 8D 7E 01                     lea r15d, [rsi + 1]
009270F3  44 8A A0 32 02 00 00            mov r12b, byte ptr [rax + 0x232]
009270FA  48 8D 45 E0                     lea rax, [rbp - 0x20]
009270FE  48 85 C9                        test rcx, rcx
00927101  0F 85 C8 03 00 00               jne 0x1409274cf
00927107  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
0092710B  45 8B CF                        mov r9d, r15d
0092710E  48 8B 05 03 FB 69 00            mov rax, qword ptr [rip + 0x69fb03]
00927115  45 33 C0                        xor r8d, r8d
00927118  49 89 73 88                     mov qword ptr [r11 - 0x78], rsi
0092711C  33 D2                           xor edx, edx
0092711E  45 88 63 80                     mov byte ptr [r11 - 0x80], r12b
00927122  49 8B CA                        mov rcx, r10
00927125  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092712A  E8 D1 D8 F9 FF                  call 0x1408c4a00
0092712F  85 C0                           test eax, eax
00927131  0F 88 7F 03 00 00               js 0x1409274b6
00927137  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
0092713B  41 8B 8E A0 01 00 00            mov ecx, dword ptr [r14 + 0x1a0]
00927142  8B C1                           mov eax, ecx
00927144  24 06                           and al, 6
00927146  3C 02                           cmp al, 2
00927148  0F 85 22 04 00 00               jne 0x140927570
0092714E  48 83 CB FF                     or rbx, 0xffffffffffffffff
00927152  40 38 B5 90 00 00 00            cmp byte ptr [rbp + 0x90], sil
00927159  0F 84 D0 03 00 00               je 0x14092752f
0092715F  4C 8B 6D 78                     mov r13, qword ptr [rbp + 0x78]
00927163  48 39 B5 80 00 00 00            cmp qword ptr [rbp + 0x80], rsi
0092716A  0F 84 84 03 00 00               je 0x1409274f4
00927170  49 81 C6 60 01 00 00            add r14, 0x160
00927177  45 33 C0                        xor r8d, r8d
0092717A  49 8B CE                        mov rcx, r14
0092717D  33 D2                           xor edx, edx
0092717F  E8 AC 90 8E FF                  call 0x140210230
00927184  48 8B F8                        mov rdi, rax
00927187  B9 11 00 00 00                  mov ecx, 0x11
0092718C  33 C0                           xor eax, eax
0092718E  F0 49 0F B1 0E                  lock cmpxchg qword ptr [r14], rcx
00927193  74 10                           je 0x1409271a5
00927195  4D 8B CE                        mov r9, r14
00927198  4C 8B C7                        mov r8, rdi
0092719B  33 D2                           xor edx, edx
0092719D  49 8B CE                        mov rcx, r14
009271A0  E8 A7 92 8E FF                  call 0x14021044c
009271A5  48 85 FF                        test rdi, rdi
009271A8  74 04                           je 0x1409271ae
009271AA  44 88 7F 0A                     mov byte ptr [rdi + 0xa], r15b
009271AE  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
009271B2  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
009271B6  41 84 CF                        test r15b, cl
009271B9  48 0F 44 F1                     cmove rsi, rcx
009271BD  33 FF                           xor edi, edi
009271BF  48 85 F6                        test rsi, rsi
009271C2  74 0D                           je 0x1409271d1
009271C4  BA 41 6C 70 63                  mov edx, 0x63706c41
009271C9  48 8B CE                        mov rcx, rsi
009271CC  E8 3F 95 8E FF                  call 0x140210710
009271D1  B8 11 00 00 00                  mov eax, 0x11
009271D6  F0 49 0F B1 3E                  lock cmpxchg qword ptr [r14], rdi
009271DB  74 08                           je 0x1409271e5
009271DD  49 8B CE                        mov rcx, r14
009271E0  E8 5B C2 93 FF                  call 0x140263440
009271E5  49 8B CE                        mov rcx, r14
009271E8  E8 13 A4 9B FF                  call 0x1402e1600
009271ED  48 85 F6                        test rsi, rsi
009271F0  0F 84 B6 03 00 00               je 0x1409275ac
009271F6  4C 8B 85 80 00 00 00            mov r8, qword ptr [rbp + 0x80]
009271FD  4D 8B CD                        mov r9, r13
00927200  41 8A D4                        mov dl, r12b
00927203  48 8B CE                        mov rcx, rsi
00927206  E8 95 B5 0F 00                  call 0x140a227a0
0092720B  BA 41 6C 70 63                  mov edx, 0x63706c41
00927210  48 8B CE                        mov rcx, rsi
00927213  8B F8                           mov edi, eax
00927215  E8 C6 06 9D FF                  call 0x1402f78e0
0092721A  33 F6                           xor esi, esi
0092721C  85 FF                           test edi, edi
0092721E  0F 88 8D 03 00 00               js 0x1409275b1
00927224  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
00927228  48 8B 15 E9 F9 69 00            mov rdx, qword ptr [rip + 0x69f9e9]
0092722F  48 8D 45 E8                     lea rax, [rbp - 0x18]
00927233  4C 8B 45 68                     mov r8, qword ptr [rbp + 0x68]
00927237  41 BD D8 01 00 00               mov r13d, 0x1d8
0092723D  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00927242  45 8A CC                        mov r9b, r12b
00927245  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092724A  41 8A CC                        mov cl, r12b
0092724D  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00927251  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00927255  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
0092725A  E8 81 3F F7 FF                  call 0x14089b1e0
0092725F  8B F8                           mov edi, eax
00927261  85 C0                           test eax, eax
00927263  0F 88 0C 03 00 00               js 0x140927575
00927269  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
0092726D  45 8B C5                        mov r8d, r13d
00927270  48 8B CF                        mov rcx, rdi
00927273  33 D2                           xor edx, edx
00927275  E8 C6 F9 D9 FF                  call 0x1406c6c40
0092727A  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0092727E  48 85 C0                        test rax, rax
00927281  74 0B                           je 0x14092728e
00927283  F7 00 00 00 04 00               test dword ptr [rax], 0x40000
00927289  41 8A C7                        mov al, r15b
0092728C  75 03                           jne 0x140927291
0092728E  40 8A C6                        mov al, sil
00927291  44 8A C0                        mov r8b, al
00927294  88 45 60                        mov byte ptr [rbp + 0x60], al
00927297  BA 02 00 00 00                  mov edx, 2
0092729C  48 8B CF                        mov rcx, rdi
0092729F  E8 20 EB FF FF                  call 0x140925dc4
009272A4  8B F0                           mov esi, eax
009272A6  85 C0                           test eax, eax
009272A8  0F 88 D6 02 00 00               js 0x140927584
009272AE  48 8D B7 A0 01 00 00            lea rsi, [rdi + 0x1a0]
009272B5  45 8B C7                        mov r8d, r15d
009272B8  83 0E 08                        or dword ptr [rsi], 8
009272BB  48 8D 0D E6 AD 6D FF            lea rcx, [rip - 0x92521a]
009272C2  BA 50 00 00 00                  mov edx, 0x50
009272C7  E8 E4 B2 F6 FF                  call 0x1408925b0
009272CC  4C 8B E0                        mov r12, rax
009272CF  33 C0                           xor eax, eax
009272D1  4D 85 E4                        test r12, r12
009272D4  0F 84 DD 02 00 00               je 0x1409275b7
009272DA  4C 89 67 10                     mov qword ptr [rdi + 0x10], r12
009272DE  4D 8D 6C 24 48                  lea r13, [r12 + 0x48]
009272E3  49 89 45 00                     mov qword ptr [r13], rax
009272E7  4D 89 34 24                     mov qword ptr [r12], r14
009272EB  49 89 7C 24 10                  mov qword ptr [r12 + 0x10], rdi
009272F0  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
009272F5  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
009272F9  E8 A6 E0 FF FF                  call 0x1409253a4
009272FE  49 8D BE 60 01 00 00            lea rdi, [r14 + 0x160]
00927305  45 33 C0                        xor r8d, r8d
00927308  48 8B CF                        mov rcx, rdi
0092730B  33 D2                           xor edx, edx
0092730D  E8 1E 8F 8E FF                  call 0x140210230
00927312  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00927318  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0092731C  73 12                           jae 0x140927330
0092731E  4C 8B C7                        mov r8, rdi
00927321  48 8B D0                        mov rdx, rax
00927324  48 8B CF                        mov rcx, rdi
00927327  E8 64 89 8E FF                  call 0x14020fc90
0092732C  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00927330  48 85 C0                        test rax, rax
00927333  74 04                           je 0x140927339
00927335  44 88 78 0A                     mov byte ptr [rax + 0xa], r15b
00927339  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0092733D  49 8D 4C 24 18                  lea rcx, [r12 + 0x18]
00927342  48 83 C0 18                     add rax, 0x18
00927346  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0092734A  48 39 02                        cmp qword ptr [rdx], rax
0092734D  74 07                           je 0x140927356
0092734F  B9 03 00 00 00                  mov ecx, 3
00927354  CD 29                           int 0x29
00927356  48 89 01                        mov qword ptr [rcx], rax
00927359  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0092735D  48 89 0A                        mov qword ptr [rdx], rcx
00927360  48 89 48 08                     mov qword ptr [rax + 8], rcx
00927364  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00927369  80 E3 06                        and bl, 6
0092736C  80 FB 02                        cmp bl, 2
0092736F  0F 84 2A 02 00 00               je 0x14092759f
00927375  48 8B CF                        mov rcx, rdi
00927378  E8 83 A2 9B FF                  call 0x1402e1600
0092737D  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00927381  E8 E6 DF FF FF                  call 0x14092536c
00927386  49 8D 4C 24 28                  lea rcx, [r12 + 0x28]
0092738B  E8 E0 E9 FF FF                  call 0x140925d70
00927390  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
00927394  33 C9                           xor ecx, ecx
00927396  85 C0                           test eax, eax
00927398  0F 88 FD 01 00 00               js 0x14092759b
0092739E  8A 45 60                        mov al, byte ptr [rbp + 0x60]
009273A1  44 8A A5 90 00 00 00            mov r12b, byte ptr [rbp + 0x90]
009273A8  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
009273AC  4C 8B 75 70                     mov r14, qword ptr [rbp + 0x70]
009273B0  4C 8B C3                        mov r8, rbx
009273B3  4C 8B 8D 88 00 00 00            mov r9, qword ptr [rbp + 0x88]
009273BA  49 8B D6                        mov rdx, r14
009273BD  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
009273C2  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009273C6  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009273CA  48 8B CF                        mov rcx, rdi
009273CD  E8 EA FF 0B 00                  call 0x1409e73bc
009273D2  85 C0                           test eax, eax
009273D4  0F 88 C1 01 00 00               js 0x14092759b
009273DA  45 8B C7                        mov r8d, r15d
009273DD  BA 30 00 00 00                  mov edx, 0x30
009273E2  49 8B CD                        mov rcx, r13
009273E5  E8 D6 B2 F6 FF                  call 0x1408926c0
009273EA  85 C0                           test eax, eax
009273EC  0F 88 A9 01 00 00               js 0x14092759b
009273F2  49 8B 45 00                     mov rax, qword ptr [r13]
009273F6  66 44 01 78 E2                  add word ptr [rax - 0x1e], r15w
009273FB  49 8B 45 00                     mov rax, qword ptr [r13]
009273FF  0F BA A8 08 01 00 00 1F         bts dword ptr [rax + 0x108], 0x1f
00927407  49 8B 4D 00                     mov rcx, qword ptr [r13]
0092740B  E8 D0 06 F7 FF                  call 0x140897ae0
00927410  45 33 ED                        xor r13d, r13d
00927413  45 84 E4                        test r12b, r12b
00927416  74 04                           je 0x14092741c
00927418  0F BA 2E 0C                     bts dword ptr [rsi], 0xc
0092741C  F7 45 50 00 00 08 00            test dword ptr [rbp + 0x50], 0x80000
00927423  74 0C                           je 0x140927431
00927425  8B 06                           mov eax, dword ptr [rsi]
00927427  0F BA E8 08                     bts eax, 8
0092742B  89 87 A0 01 00 00               mov dword ptr [rdi + 0x1a0], eax
00927431  44 38 BF 0C 01 00 00            cmp byte ptr [rdi + 0x10c], r15b
00927438  0F 85 C4 00 00 00               jne 0x140927502
0092743E  0F BA AF A0 01 00 00 0A         bts dword ptr [rdi + 0x1a0], 0xa
00927446  49 8B D6                        mov rdx, r14
00927449  48 8B CF                        mov rcx, rdi
0092744C  E8 CB 01 0C 00                  call 0x1409e761c
00927451  B9 00 00 00 01                  mov ecx, 0x1000000
00927456  85 8B 00 01 00 00               test dword ptr [rbx + 0x100], ecx
0092745C  0F 85 5C 01 00 00               jne 0x1409275be
00927462  48 8B CF                        mov rcx, rdi
00927465  E8 B6 85 8E FF                  call 0x14020fa20
0092746A  48 8D 45 F0                     lea rax, [rbp - 0x10]
0092746E  45 33 C9                        xor r9d, r9d
00927471  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00927476  33 D2                           xor edx, edx
00927478  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0092747D  41 B8 01 00 1F 00               mov r8d, 0x1f0001
00927483  48 8B CF                        mov rcx, rdi
00927486  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
0092748B  E8 10 23 F9 FF                  call 0x1408b97a0
00927490  8B C8                           mov ecx, eax
00927492  85 C0                           test eax, eax
00927494  0F 88 3D 01 00 00               js 0x1409275d7
0092749A  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092749E  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
009274A2  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
009274A6  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
009274AA  48 89 02                        mov qword ptr [rdx], rax
009274AD  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
009274B1  48 89 38                        mov qword ptr [rax], rdi
009274B4  8B C1                           mov eax, ecx
009274B6  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
009274BE  48 83 C4 70                     add rsp, 0x70
009274C2  41 5F                           pop r15
009274C4  41 5E                           pop r14
009274C6  41 5D                           pop r13
009274C8  41 5C                           pop r12
009274CA  5F                              pop rdi
009274CB  5E                              pop rsi
009274CC  5D                              pop rbp
009274CD  C3                              ret
009274CE  CC                              int3
009274CF  4C 8B 0D 42 F7 69 00            mov r9, qword ptr [rip + 0x69f742]
009274D6  45 8B C7                        mov r8d, r15d
009274D9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009274DE  33 D2                           xor edx, edx
009274E0  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
009274E5  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
009274EA  E8 35 60 F9 FF                  call 0x1408bd524
009274EF  E9 3B FC FF FF                  jmp 0x14092712f
009274F4  4D 85 ED                        test r13, r13
009274F7  0F 84 2B FD FF FF               je 0x140927228
009274FD  E9 6E FC FF FF                  jmp 0x140927170
00927502  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0092750B  45 33 C0                        xor r8d, r8d
0092750E  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
00927512  4C 8D 4F 40                     lea r9, [rdi + 0x40]
00927516  48 8D 97 04 01 00 00            lea rdx, [rdi + 0x104]
0092751D  E8 8E 9C F6 FF                  call 0x1408911b0
00927522  85 C0                           test eax, eax
00927524  78 75                           js 0x14092759b
00927526  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
0092752A  E9 17 FF FF FF                  jmp 0x140927446
0092752F  0F BA E1 0C                     bt ecx, 0xc
00927533  0F 83 26 FC FF FF               jae 0x14092715f
00927539  49 8D BE 60 01 00 00            lea rdi, [r14 + 0x160]
00927540  45 33 C0                        xor r8d, r8d
00927543  48 8B CF                        mov rcx, rdi
00927546  33 D2                           xor edx, edx
00927548  E8 E3 8C 8E FF                  call 0x140210230
0092754D  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00927553  48 8B F0                        mov rsi, rax
00927556  0F 83 9C B6 1F 00               jae 0x140b22bf8
0092755C  4C 8B C7                        mov r8, rdi
0092755F  48 8B D0                        mov rdx, rax
00927562  48 8B CF                        mov rcx, rdi
00927565  E8 26 87 8E FF                  call 0x14020fc90
0092756A  90                              nop
0092756B  E9 88 B6 1F 00                  jmp 0x140b22bf8
00927570  BF 42 00 00 C0                  mov edi, 0xc0000042
00927575  49 8B CE                        mov rcx, r14
00927578  E8 D3 1D 9D FF                  call 0x1402f9350
0092757D  8B C7                           mov eax, edi
0092757F  E9 32 FF FF FF                  jmp 0x1409274b6
00927584  49 8B CE                        mov rcx, r14
00927587  E8 C4 1D 9D FF                  call 0x1402f9350
0092758C  48 8B CF                        mov rcx, rdi
0092758F  E8 BC 1D 9D FF                  call 0x1402f9350
00927594  8B C6                           mov eax, esi
00927596  E9 1B FF FF FF                  jmp 0x1409274b6
0092759B  8B F0                           mov esi, eax
0092759D  EB ED                           jmp 0x14092758c
0092759F  48 8B CF                        mov rcx, rdi
009275A2  E8 29 E8 93 FF                  call 0x140265dd0
009275A7  E9 C9 FD FF FF                  jmp 0x140927375
009275AC  BF A0 02 00 C0                  mov edi, 0xc00002a0
009275B1  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
009275B5  EB BE                           jmp 0x140927575
009275B7  BE 17 00 00 C0                  mov esi, 0xc0000017
009275BC  EB C6                           jmp 0x140927584
009275BE  09 8F 00 01 00 00               or dword ptr [rdi + 0x100], ecx
009275C4  48 8B 83 10 01 00 00            mov rax, qword ptr [rbx + 0x110]
009275CB  48 89 87 10 01 00 00            mov qword ptr [rdi + 0x110], rax
009275D2  E9 8B FE FF FF                  jmp 0x140927462
009275D7  8B F1                           mov esi, ecx
009275D9  EB B1                           jmp 0x14092758c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpCreateClientPort(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, unsigned __int8 a11)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    v_rsi = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    if (a5 != 0) goto loc_009274CF;
    *(unsigned __int64 *)(v_rsp - 112) = v_stack_m58;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    a2 = 0;
    *(unsigned __int8 *)(v_rsp - 128) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m88 = *(unsigned __int64 *)(v_rip + 6945539);
    result = ObReferenceObjectByName(a4, a2, a3, (unsigned int)((unsigned int)(v_rsi + 1)));
loc_0092712F:
    if (sign_flag) goto loc_009274B6;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 416))))) & (6));
    if (((unsigned __int8)(result)) != 2) goto loc_00927570;
    v_rbx = (v_rbx) | (-1);
    if (a11 == 0) goto loc_0092752F;
loc_0092715F:
    if (a9 == 0) goto loc_009274F4;
loc_00927170:
    v_r14 = (v_stack_m58) + (352);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r14, a2, a3, (unsigned int)((unsigned int)(v_rsi + 1)));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r14;
        a3 = 0;
        a2 = 0;
        a1 = v_r14;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rsi + 1);
    }
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m58 + 24)))) == 0) { v_rsi = *(unsigned __int64 *)(v_stack_m58 + 24); }
    v_rdi = 0;
    result = v_stack_m58;
    if (v_rsi != 0) {
        a2 = 0x63706C41ULL;
        a1 = v_rsi;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = 17;
    if (v_rsi != 0) {
        a1 = v_r14;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_r14, a2, a3, a4);
    if (v_rsi == 0) goto loc_009275AC;
    result = AlpcpCheckConnectionSecurity(v_rsi, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a9, a8);
    result = ObfDereferenceObjectWithTag(v_rsi, (unsigned int)(0x63706C41ULL), a9, a8);
    v_rsi = 0;
    if (sign_flag) goto loc_009275B1;
loc_00927228:
    v_stack_m60 = 0;
    v_stack_m68 = v_stack_m50;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 472;
    result = ObCreateObjectEx((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 6945257), a6, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00927575;
    a2 = 0;
    result = memset(v_stack_m50, a2, 472, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (a7 == 0) goto loc_0092728E;
    result = (unsigned __int8)(v_rsi + 1);
    if (((*(unsigned int *)(a7)) & (0x40000ULL)) == 0) {
        result = 0;
    }
    v_stack_p28 = (unsigned __int8)(result);
    result = AlpcpInitializePort(v_stack_m50, 2, (unsigned __int8)(result), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00927584;
    result = AlpcpAllocateBlob(v_rip - 9589274, 80, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = 0;
    if (0 == 0) goto loc_009275B7;
    *(unsigned __int64 *)(v_stack_m50 + 16) = 0;
    *(unsigned __int64 *)(result + 72) = 0;
    *(unsigned __int64 *)(result) = v_stack_m58;
    *(unsigned __int64 *)(result + 16) = v_stack_m50;
    *(unsigned __int64 *)(result + 8) = 0;
    result = AlpcpLockBlobExclusive(*(unsigned __int64 *)(v_stack_m58 + 16), 80, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m58 + 352, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m40 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_m58 + 352;
        a2 = result;
        a1 = v_stack_m58 + 352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
        result = v_stack_m40;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rsi + 1);
    }
    result = (*(unsigned __int64 *)(v_stack_m58 + 16)) + (24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = a1;
    *(unsigned __int64 *)(result + 8) = a1;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0092759F;
loc_00927375:
    result = KeAbPostRelease(v_stack_m58 + 352, *(unsigned __int64 *)(result + 8), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = AlpcpUnlockBlobUncachedExclusive(*(unsigned __int64 *)(v_stack_m58 + 16), *(unsigned __int64 *)(result + 8), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = AlpcInitializeHandleTable(result + 40, *(unsigned __int64 *)(result + 8), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    a1 = 0;
    if (sign_flag) goto loc_0092759B;
    v_stack_m78 = a11;
    v_stack_m80 = a5;
    v_stack_m88 = 0;
    result = AlpcpValidateAndSetPortAttributes(v_stack_m50, a7, v_stack_m58, a10);
    if (sign_flag) goto loc_0092759B;
    result = AlpcpAllocateMessage(result + 72, 48, (unsigned int)((unsigned int)(v_rsi + 1)), a10);
    if (sign_flag) goto loc_0092759B;
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(result + 72), 48, (unsigned int)((unsigned int)(v_rsi + 1)), a10);
    v_r13 = 0;
    if (a11 != 0) {
    }
    if (((v_stack_p18) & (0x80000ULL)) != 0) {
        result = *(unsigned int *)(v_stack_m50 + 416);
        *(unsigned int *)(v_stack_m50 + 416) = (unsigned int)(result);
    }
    if ((*(unsigned __int8 *)(v_stack_m50 + 268)) != ((unsigned __int8)(v_rsi + 1))) goto loc_00927502;
loc_00927446:
    result = AlpcpSetOwnerProcessPort(v_stack_m50, a7, (unsigned int)((unsigned int)(v_rsi + 1)), a10);
    if (((*(unsigned int *)(v_stack_m58 + 256)) & ((unsigned int)((unsigned int)(0x1000000ULL)))) != 0) goto loc_009275BE;
loc_00927462:
    result = ObfReferenceObject(v_stack_m50, a7, (unsigned int)((unsigned int)(v_rsi + 1)), a10);
    a4 = 0;
    v_stack_m78 = v_stack_m48;
    a2 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = 0;
    result = ObInsertObjectEx(v_stack_m50, a2, (unsigned int)(0x1F0001ULL), a4);
    if (sign_flag) goto loc_009275D7;
    *(unsigned __int64 *)(v_stack_m50 + 56) = v_stack_m48;
    *(unsigned __int64 *)(v_stack_p8) = v_stack_m48;
    *(unsigned __int64 *)(v_stack_p10) = v_stack_m50;
loc_009274B6:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009274CF:
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    a2 = 0;
    v_stack_p28 = v_stack_m50 + 416;
    v_stack_p20 = a11;
    result = ObReferenceObjectByNameEx((unsigned int)((unsigned int)(result)), a2, (unsigned int)((unsigned int)(v_rsi + 1)), *(unsigned __int64 *)(v_rip + 6944578));
    goto loc_0092712F;
loc_009274F4:
    if (0 == 0) goto loc_00927228;
    goto loc_00927170;
loc_00927502:
    a3 = 0;
    result = SeCreateClientSecurity(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m50 + 260, a3, v_stack_m50 + 64);
    if (sign_flag) goto loc_0092759B;
    goto loc_00927446;
loc_0092752F:
    if (condition_is_above_or_equal) goto loc_0092715F;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a7 + 352, a2, a3, v_stack_m50 + 64);
    result = ExfAcquirePushLockExclusiveEx(a7 + 352, result, a7 + 352, v_stack_m50 + 64);
loc_00927570:
loc_00927575:
    result = ObfDereferenceObject(a7, result, a7 + 352, v_stack_m50 + 64);
    goto loc_009274B6;
loc_00927584:
    result = ObfDereferenceObject(a7, result, a7 + 352, v_stack_m50 + 64);
loc_0092758C:
    result = ObfDereferenceObject((unsigned int)(0xC0000042ULL), result, a7 + 352, v_stack_m50 + 64);
    goto loc_009274B6;
loc_0092759B:
    goto loc_0092758C;
loc_0092759F:
    result = ExfTryToWakePushLock((unsigned int)(0xC0000042ULL), result, a7 + 352, v_stack_m50 + 64);
    goto loc_00927375;
loc_009275AC:
loc_009275B1:
    goto loc_00927575;
loc_009275B7:
    goto loc_00927584;
loc_009275BE:
    *(unsigned __int64 *)((unsigned int)(0xC00002A0ULL) + 272) = *(unsigned __int64 *)(v_stack_m58 + 272);
    goto loc_00927462;
loc_009275D7:
    goto loc_0092758C;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpCreateClientPort(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, uint8_t Arg11)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    local_rsi = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    if (Arg5 != 0) goto loc_009274CF;
    *(uint64_t *)(local_rsp - 0x70) = v_stack_m58;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    Arg2 = 0;
    *(uint8_t *)(local_rsp - 0x80) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m88 = *(uint64_t *)(v_rip + 0x69FB03);
    result = ObReferenceObjectByName(Arg4, Arg2, Arg3, (uint32_t)((uint32_t)(local_rsi + 1)));
loc_0092712F:
    if (sign_flag) goto loc_009274B6;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x1A0))))) & (6));
    if (((uint8_t)(result)) != 2) goto loc_00927570;
    local_rbx = (local_rbx) | (-1);
    if (Arg11 == 0) goto loc_0092752F;
loc_0092715F:
    if (Arg9 == 0) goto loc_009274F4;
loc_00927170:
    local_r14 = (v_stack_m58) + (352);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r14, Arg2, Arg3, (uint32_t)((uint32_t)(local_rsi + 1)));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_r14;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r14;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rsi + 1);
    }
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)(*(uint64_t *)(v_stack_m58 + 0x18)))) == 0) { local_rsi = *(uint64_t *)(v_stack_m58 + 0x18); }
    local_rdi = 0;
    result = v_stack_m58;
    if (local_rsi != 0) {
        Arg2 = 0x63706C41ULL;
        Arg1 = local_rsi;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = 17;
    if (local_rsi != 0) {
        Arg1 = local_r14;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(local_r14, Arg2, Arg3, Arg4);
    if (local_rsi == 0) goto loc_009275AC;
    result = AlpcpCheckConnectionSecurity(local_rsi, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg9, Arg8);
    result = ObfDereferenceObjectWithTag(local_rsi, (uint32_t)(0x63706C41ULL), Arg9, Arg8);
    local_rsi = 0;
    if (sign_flag) goto loc_009275B1;
loc_00927228:
    v_stack_m60 = 0;
    v_stack_m68 = v_stack_m50;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 472;
    result = ObCreateObjectEx((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x69F9E9), Arg6, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00927575;
    Arg2 = 0;
    result = memset(v_stack_m50, Arg2, 472, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (Arg7 == 0) goto loc_0092728E;
    result = (uint8_t)(local_rsi + 1);
    if (((*(uint32_t *)(Arg7)) & (0x40000ULL)) == 0) {
        result = 0;
    }
    v_stack_p28 = (uint8_t)(result);
    result = AlpcpInitializePort(v_stack_m50, 2, (uint8_t)(result), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00927584;
    result = AlpcpAllocateBlob(v_rip - 9589274, 80, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = 0;
    if (0 == 0) goto loc_009275B7;
    *(uint64_t *)(v_stack_m50 + 0x10) = 0;
    *(uint64_t *)(result + 0x48) = 0;
    *(uint64_t *)(result) = v_stack_m58;
    *(uint64_t *)(result + 0x10) = v_stack_m50;
    *(uint64_t *)(result + 0x8) = 0;
    result = AlpcpLockBlobExclusive(*(uint64_t *)(v_stack_m58 + 0x10), 80, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m58 + 352, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m40 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_m58 + 352;
        Arg2 = result;
        Arg1 = v_stack_m58 + 352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
        result = v_stack_m40;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rsi + 1);
    }
    result = (*(uint64_t *)(v_stack_m58 + 0x10)) + (24);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) {
        Arg1 = 3;
    }
    *(uint64_t *)(Arg1) = result;
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = Arg1;
    *(uint64_t *)(result + 0x8) = Arg1;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0092759F;
loc_00927375:
    result = KeAbPostRelease(v_stack_m58 + 352, *(uint64_t *)(result + 0x8), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = AlpcpUnlockBlobUncachedExclusive(*(uint64_t *)(v_stack_m58 + 0x10), *(uint64_t *)(result + 0x8), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = AlpcInitializeHandleTable(result + 40, *(uint64_t *)(result + 0x8), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    Arg1 = 0;
    if (sign_flag) goto loc_0092759B;
    v_stack_m78 = Arg11;
    v_stack_m80 = Arg5;
    v_stack_m88 = 0;
    result = AlpcpValidateAndSetPortAttributes(v_stack_m50, Arg7, v_stack_m58, Arg10);
    if (sign_flag) goto loc_0092759B;
    result = AlpcpAllocateMessage(result + 72, 48, (uint32_t)((uint32_t)(local_rsi + 1)), Arg10);
    if (sign_flag) goto loc_0092759B;
    result = AlpcpUnlockMessage(*(uint64_t *)(result + 0x48), 48, (uint32_t)((uint32_t)(local_rsi + 1)), Arg10);
    local_r13 = 0;
    if (Arg11 != 0) {
    }
    if (((v_stack_p18) & (0x80000ULL)) != 0) {
        result = *(uint32_t *)(v_stack_m50 + 0x1A0);
        *(uint32_t *)(v_stack_m50 + 0x1A0) = (uint32_t)(result);
    }
    if ((*(uint8_t *)(v_stack_m50 + 0x10C)) != ((uint8_t)(local_rsi + 1))) goto loc_00927502;
loc_00927446:
    result = AlpcpSetOwnerProcessPort(v_stack_m50, Arg7, (uint32_t)((uint32_t)(local_rsi + 1)), Arg10);
    if (((*(uint32_t *)(v_stack_m58 + 0x100)) & ((uint32_t)((uint32_t)(0x1000000ULL)))) != 0) goto loc_009275BE;
loc_00927462:
    result = ObfReferenceObject(v_stack_m50, Arg7, (uint32_t)((uint32_t)(local_rsi + 1)), Arg10);
    Arg4 = 0;
    v_stack_m78 = v_stack_m48;
    Arg2 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = 0;
    result = ObInsertObjectEx(v_stack_m50, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    if (sign_flag) goto loc_009275D7;
    *(uint64_t *)(v_stack_m50 + 0x38) = v_stack_m48;
    *(uint64_t *)(v_stack_p8) = v_stack_m48;
    *(uint64_t *)(v_stack_p10) = v_stack_m50;
loc_009274B6:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009274CF:
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    Arg2 = 0;
    v_stack_p28 = v_stack_m50 + 416;
    v_stack_p20 = Arg11;
    result = ObReferenceObjectByNameEx((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)((uint32_t)(local_rsi + 1)), *(uint64_t *)(v_rip + 0x69F742));
    goto loc_0092712F;
loc_009274F4:
    if (0 == 0) goto loc_00927228;
    goto loc_00927170;
loc_00927502:
    Arg3 = 0;
    result = SeCreateClientSecurity(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m50 + 260, Arg3, v_stack_m50 + 64);
    if (sign_flag) goto loc_0092759B;
    goto loc_00927446;
loc_0092752F:
    if (condition_is_above_or_equal) goto loc_0092715F;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg7 + 352, Arg2, Arg3, v_stack_m50 + 64);
    result = ExfAcquirePushLockExclusiveEx(Arg7 + 352, result, Arg7 + 352, v_stack_m50 + 64);
loc_00927570:
loc_00927575:
    result = ObfDereferenceObject(Arg7, result, Arg7 + 352, v_stack_m50 + 64);
    goto loc_009274B6;
loc_00927584:
    result = ObfDereferenceObject(Arg7, result, Arg7 + 352, v_stack_m50 + 64);
loc_0092758C:
    result = ObfDereferenceObject((uint32_t)(0xC0000042ULL), result, Arg7 + 352, v_stack_m50 + 64);
    goto loc_009274B6;
loc_0092759B:
    goto loc_0092758C;
loc_0092759F:
    result = ExfTryToWakePushLock((uint32_t)(0xC0000042ULL), result, Arg7 + 352, v_stack_m50 + 64);
    goto loc_00927375;
loc_009275AC:
loc_009275B1:
    goto loc_00927575;
loc_009275B7:
    goto loc_00927584;
loc_009275BE:
    *(uint64_t *)((uint32_t)(0xC00002A0ULL) + 0x110) = *(uint64_t *)(v_stack_m58 + 0x110);
    goto loc_00927462;
loc_009275D7:
    goto loc_0092758C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009270AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
