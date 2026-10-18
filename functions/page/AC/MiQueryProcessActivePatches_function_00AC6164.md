# MiQueryProcessActivePatches

- RVA: `0x00AC6164`–`0x00AC68A4` (길이 `1,856` bytes)
- VA: `0x0000000140AC6164`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000966BC`
- 디코드: `494`개 명령, `1,856/1,856` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00AC6202` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (function, `0x004DC2A0`)
- `0x00AC62B3` → [MiIsActiveSystemHotPatch](../80/MiIsActiveSystemHotPatch_function_008045D8.md) (function, `0x008045D8`)
- `0x00AC6313` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AC632E` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AC6352` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00AC6373` → [VslQueryActiveSecurePatches](../../text/58/VslQueryActiveSecurePatches_function_0058ED14.md) (function, `0x0058ED14`)
- `0x00AC63E3` → [MiGetProcessHotPatchContext](../80/MiGetProcessHotPatchContext_function_00803948.md) (function, `0x00803948`)
- `0x00AC641C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00AC643B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00AC64E0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00AC65F3` → [MiFillActivePatchesQueryBuffer](../80/MiFillActivePatchesQueryBuffer_function_008034D4.md) (function, `0x008034D4`)
- `0x00AC666A` → [MiFillActivePatchesQueryBuffer](../80/MiFillActivePatchesQueryBuffer_function_008034D4.md) (function, `0x008034D4`)
- `0x00AC66C7` → [MiIsActiveSystemHotPatch](../80/MiIsActiveSystemHotPatch_function_008045D8.md) (function, `0x008045D8`)
- `0x00AC66D3` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00AC6737` → [MiFillActivePatchesQueryBuffer](../80/MiFillActivePatchesQueryBuffer_function_008034D4.md) (function, `0x008034D4`)
- `0x00AC679E` → [MiFillActivePatchesQueryBuffer](../80/MiFillActivePatchesQueryBuffer_function_008034D4.md) (function, `0x008034D4`)
- `0x00AC67E1` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)
- `0x00AC6805` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00AC680D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00AC682A` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00AC683F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AC6850` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AC6862` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AC6875` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AC6883` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtManageHotPatch](../AF/NtManageHotPatch_function_00AF8660.md) at `0x00AF8980`

### Static image references
- `0x00AC6180` → RVA `0x00E0A740` (`.data`; read)
- `0x00AC6207` → RVA `0x00E37588` (`.data`; read)
- `0x00AC6299` → RVA `0x00EF54C0` (`.data`; read)
- `0x00AC62E1` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00AC6202` → [MmAcquireLoadLock](../../text/4D/MmAcquireLoadLock_function_004DC2A0.md) (`PAGE` → `.text`)
  - `0x00AC632E` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AC6352` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00AC6373` → [VslQueryActiveSecurePatches](../../text/58/VslQueryActiveSecurePatches_function_0058ED14.md) (`PAGE` → `.text`)
  - `0x00AC641C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00AC643B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00AC64E0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00AC66D3` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00AC67E1` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`PAGE` → `.text`)
  - `0x00AC6805` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00AC680D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00AC682A` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00AC683F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AC6850` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AC6862` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AC6875` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AC6883` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC6164  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AC6169  55                              push rbp
00AC616A  56                              push rsi
00AC616B  57                              push rdi
00AC616C  41 54                           push r12
00AC616E  41 55                           push r13
00AC6170  41 56                           push r14
00AC6172  41 57                           push r15
00AC6174  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00AC6179  48 81 EC 20 01 00 00            sub rsp, 0x120
00AC6180  48 8B 05 B9 45 34 00            mov rax, qword ptr [rip + 0x3445b9]
00AC6187  48 33 C4                        xor rax, rsp
00AC618A  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00AC618E  8B B5 90 00 00 00               mov esi, dword ptr [rbp + 0x90]
00AC6194  33 FF                           xor edi, edi
00AC6196  0F 57 C0                        xorps xmm0, xmm0
00AC6199  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00AC619D  48 8B C1                        mov rax, rcx
00AC61A0  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
00AC61A4  83 FE 02                        cmp esi, 2
00AC61A7  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
00AC61AB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00AC61AF  44 8D 6F 28                     lea r13d, [rdi + 0x28]
00AC61B3  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00AC61B7  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00AC61BB  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AC61C0  44 8B FF                        mov r15d, edi
00AC61C3  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00AC61C7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AC61D0  44 8B F7                        mov r14d, edi
00AC61D3  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00AC61D7  44 8B E7                        mov r12d, edi
00AC61DA  8D 4F 30                        lea ecx, [rdi + 0x30]
00AC61DD  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00AC61E2  44 0F 45 E9                     cmovne r13d, ecx
00AC61E6  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00AC61EA  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
00AC61EE  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00AC61F2  48 85 C0                        test rax, rax
00AC61F5  0F 85 E6 00 00 00               jne 0x140ac62e1
00AC61FB  8D 58 08                        lea ebx, [rax + 8]
00AC61FE  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00AC6202  E8 99 60 A1 FF                  call 0x1404dc2a0
00AC6207  48 8B 0D 7A 13 37 00            mov rcx, qword ptr [rip + 0x37137a]
00AC620E  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00AC6212  EB 06                           jmp 0x140ac621a
00AC6214  4C 8B F1                        mov r14, rcx
00AC6217  48 8B 09                        mov rcx, qword ptr [rcx]
00AC621A  48 85 C9                        test rcx, rcx
00AC621D  75 F5                           jne 0x140ac6214
00AC621F  45 33 D2                        xor r10d, r10d
00AC6222  49 8B CE                        mov rcx, r14
00AC6225  4D 8B FD                        mov r15, r13
00AC6228  BF 01 00 00 00                  mov edi, 1
00AC622D  4D 85 F6                        test r14, r14
00AC6230  74 67                           je 0x140ac6299
00AC6232  49 8B D5                        mov rdx, r13
00AC6235  44 8D 4F 17                     lea r9d, [rdi + 0x17]
00AC6239  44 0F B7 79 30                  movzx r15d, word ptr [rcx + 0x30]
00AC623E  44 03 E7                        add r12d, edi
00AC6241  83 FE 02                        cmp esi, 2
00AC6244  B8 1C 00 00 00                  mov eax, 0x1c
00AC6249  49 0F 44 C1                     cmove rax, r9
00AC624D  48 03 C2                        add rax, rdx
00AC6250  48 8B D1                        mov rdx, rcx
00AC6253  4C 03 F8                        add r15, rax
00AC6256  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00AC625A  48 85 C0                        test rax, rax
00AC625D  74 23                           je 0x140ac6282
00AC625F  48 8B 10                        mov rdx, qword ptr [rax]
00AC6262  48 8B C8                        mov rcx, rax
00AC6265  48 85 D2                        test rdx, rdx
00AC6268  74 22                           je 0x140ac628c
00AC626A  48 8B 02                        mov rax, qword ptr [rdx]
00AC626D  48 8B CA                        mov rcx, rdx
00AC6270  48 8B D0                        mov rdx, rax
00AC6273  48 85 C0                        test rax, rax
00AC6276  75 F2                           jne 0x140ac626a
00AC6278  EB 12                           jmp 0x140ac628c
00AC627A  48 39 11                        cmp qword ptr [rcx], rdx
00AC627D  74 0D                           je 0x140ac628c
00AC627F  48 8B D1                        mov rdx, rcx
00AC6282  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00AC6286  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00AC628A  75 EE                           jne 0x140ac627a
00AC628C  49 8B D7                        mov rdx, r15
00AC628F  48 85 C9                        test rcx, rcx
00AC6292  75 A5                           jne 0x140ac6239
00AC6294  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00AC6299  4C 8B 0D 20 F2 42 00            mov r9, qword ptr [rip + 0x42f220]
00AC62A0  4C 8D 1D 19 F2 42 00            lea r11, [rip + 0x42f219]
00AC62A7  4D 3B CB                        cmp r9, r11
00AC62AA  0F 84 EF 01 00 00               je 0x140ac649f
00AC62B0  49 8B C9                        mov rcx, r9
00AC62B3  E8 20 E3 D3 FF                  call 0x1408045d8
00AC62B8  85 C0                           test eax, eax
00AC62BA  74 18                           je 0x140ac62d4
00AC62BC  41 0F B7 41 48                  movzx eax, word ptr [r9 + 0x48]
00AC62C1  49 83 C7 18                     add r15, 0x18
00AC62C5  4C 03 F8                        add r15, rax
00AC62C8  44 03 E7                        add r12d, edi
00AC62CB  83 FE 02                        cmp esi, 2
00AC62CE  74 04                           je 0x140ac62d4
00AC62D0  49 83 C7 04                     add r15, 4
00AC62D4  4D 8B 09                        mov r9, qword ptr [r9]
00AC62D7  4D 3B CB                        cmp r9, r11
00AC62DA  75 D4                           jne 0x140ac62b0
00AC62DC  E9 B9 01 00 00                  jmp 0x140ac649a
00AC62E1  4C 8B 05 B0 07 50 00            mov r8, qword ptr [rip + 0x5007b0]
00AC62E8  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AC62ED  44 8A 8D 88 00 00 00            mov r9b, byte ptr [rbp + 0x88]
00AC62F4  BA 00 10 00 00                  mov edx, 0x1000
00AC62F9  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AC62FE  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AC6303  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AC6308  48 8B C8                        mov rcx, rax
00AC630B  C7 44 24 20 4D 6D 48 70         mov dword ptr [rsp + 0x20], 0x70486d4d
00AC6313  E8 38 33 DA FF                  call 0x140869650
00AC6318  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00AC631D  8B F8                           mov edi, eax
00AC631F  85 C0                           test eax, eax
00AC6321  0F 88 2E 05 00 00               js 0x140ac6855
00AC6327  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
00AC632E  E8 ED 02 75 FF                  call 0x140216620
00AC6333  BF 01 00 00 00                  mov edi, 1
00AC6338  23 C7                           and eax, edi
00AC633A  8D 1C 00                        lea ebx, [rax + rax]
00AC633D  75 0A                           jne 0x140ac6349
00AC633F  BF 0A 01 00 C0                  mov edi, 0xc000010a
00AC6344  E9 8C 04 00 00                  jmp 0x140ac67d5
00AC6349  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00AC634D  33 D2                           xor edx, edx
00AC634F  48 8B CE                        mov rcx, rsi
00AC6352  E8 C9 04 75 FF                  call 0x140216820
00AC6357  48 8B 8E 70 01 00 00            mov rcx, qword ptr [rsi + 0x170]
00AC635E  83 CB 04                        or ebx, 4
00AC6361  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00AC6365  40 84 CF                        test dil, cl
00AC6368  74 74                           je 0x140ac63de
00AC636A  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AC636F  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00AC6373  E8 9C 89 AC FF                  call 0x14058ed14
00AC6378  45 33 D2                        xor r10d, r10d
00AC637B  8B F8                           mov edi, eax
00AC637D  85 C0                           test eax, eax
00AC637F  0F 88 50 04 00 00               js 0x140ac67d5
00AC6385  44 8B 64 24 60                  mov r12d, dword ptr [rsp + 0x60]
00AC638A  4D 8B FD                        mov r15, r13
00AC638D  45 85 E4                        test r12d, r12d
00AC6390  0F 84 0E 01 00 00               je 0x140ac64a4
00AC6396  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00AC639A  41 8D 7A 01                     lea edi, [r10 + 1]
00AC639E  45 8D 4A 18                     lea r9d, [r10 + 0x18]
00AC63A2  4D 8B C5                        mov r8, r13
00AC63A5  44 8B 95 90 00 00 00            mov r10d, dword ptr [rbp + 0x90]
00AC63AC  41 8B D4                        mov edx, r12d
00AC63AF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AC63B3  44 0F B7 39                     movzx r15d, word ptr [rcx]
00AC63B7  41 83 FA 02                     cmp r10d, 2
00AC63BB  B8 1C 00 00 00                  mov eax, 0x1c
00AC63C0  48 8D 49 10                     lea rcx, [rcx + 0x10]
00AC63C4  49 0F 44 C1                     cmove rax, r9
00AC63C8  49 03 C0                        add rax, r8
00AC63CB  4C 03 F8                        add r15, rax
00AC63CE  4D 8B C7                        mov r8, r15
00AC63D1  48 2B D7                        sub rdx, rdi
00AC63D4  75 DD                           jne 0x140ac63b3
00AC63D6  45 33 D2                        xor r10d, r10d
00AC63D9  E9 C6 00 00 00                  jmp 0x140ac64a4
00AC63DE  33 D2                           xor edx, edx
00AC63E0  48 8B CE                        mov rcx, rsi
00AC63E3  E8 60 D5 D3 FF                  call 0x140803948
00AC63E8  45 33 D2                        xor r10d, r10d
00AC63EB  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00AC63EF  4C 8B C0                        mov r8, rax
00AC63F2  4D 8B FD                        mov r15, r13
00AC63F5  48 85 C0                        test rax, rax
00AC63F8  0F 84 A6 00 00 00               je 0x140ac64a4
00AC63FE  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00AC6402  0B DF                           or ebx, edi
00AC6404  49 8D 78 10                     lea rdi, [r8 + 0x10]
00AC6408  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00AC640C  45 33 C0                        xor r8d, r8d
00AC640F  33 D2                           xor edx, edx
00AC6411  48 8B CF                        mov rcx, rdi
00AC6414  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
00AC641B  90                              nop
00AC641C  E8 0F 9E 74 FF                  call 0x140210230
00AC6421  48 8B F0                        mov rsi, rax
00AC6424  33 C0                           xor eax, eax
00AC6426  8D 48 11                        lea ecx, [rax + 0x11]
00AC6429  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00AC642E  74 10                           je 0x140ac6440
00AC6430  4C 8B CF                        mov r9, rdi
00AC6433  4C 8B C6                        mov r8, rsi
00AC6436  33 D2                           xor edx, edx
00AC6438  48 8B CF                        mov rcx, rdi
00AC643B  E8 0C A0 74 FF                  call 0x14021044c
00AC6440  45 33 D2                        xor r10d, r10d
00AC6443  41 8D 7A 01                     lea edi, [r10 + 1]
00AC6447  48 85 F6                        test rsi, rsi
00AC644A  74 04                           je 0x140ac6450
00AC644C  40 88 7E 0A                     mov byte ptr [rsi + 0xa], dil
00AC6450  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
00AC6454  44 8B 64 24 60                  mov r12d, dword ptr [rsp + 0x60]
00AC6459  49 8B 08                        mov rcx, qword ptr [r8]
00AC645C  49 3B C8                        cmp rcx, r8
00AC645F  74 3E                           je 0x140ac649f
00AC6461  44 8B 95 90 00 00 00            mov r10d, dword ptr [rbp + 0x90]
00AC6468  49 8B D5                        mov rdx, r13
00AC646B  41 B9 18 00 00 00               mov r9d, 0x18
00AC6471  44 0F B7 79 28                  movzx r15d, word ptr [rcx + 0x28]
00AC6476  44 03 E7                        add r12d, edi
00AC6479  48 8B 09                        mov rcx, qword ptr [rcx]
00AC647C  41 83 FA 02                     cmp r10d, 2
00AC6480  B8 1C 00 00 00                  mov eax, 0x1c
00AC6485  49 0F 44 C1                     cmove rax, r9
00AC6489  48 03 C2                        add rax, rdx
00AC648C  4C 03 F8                        add r15, rax
00AC648F  49 8B D7                        mov rdx, r15
00AC6492  49 3B C8                        cmp rcx, r8
00AC6495  75 DA                           jne 0x140ac6471
00AC6497  45 33 D2                        xor r10d, r10d
00AC649A  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00AC649F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00AC64A4  8B 85 80 00 00 00               mov eax, dword ptr [rbp + 0x80]
00AC64AA  49 3B C7                        cmp rax, r15
00AC64AD  73 23                           jae 0x140ac64d2
00AC64AF  B8 FF FF FF FF                  mov eax, 0xffffffff
00AC64B4  4C 3B F8                        cmp r15, rax
00AC64B7  76 0A                           jbe 0x140ac64c3
00AC64B9  BF 95 00 00 C0                  mov edi, 0xc0000095
00AC64BE  E9 0E 03 00 00                  jmp 0x140ac67d1
00AC64C3  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00AC64C7  41 8B FA                        mov edi, r10d
00AC64CA  4C 89 10                        mov qword ptr [rax], r10
00AC64CD  E9 F8 02 00 00                  jmp 0x140ac67ca
00AC64D2  41 8B D7                        mov edx, r15d
00AC64D5  B9 00 01 00 00                  mov ecx, 0x100
00AC64DA  41 B8 4D 6D 48 71               mov r8d, 0x71486d4d
00AC64E0  E8 5B 50 89 FF                  call 0x14035b540
00AC64E5  45 33 DB                        xor r11d, r11d
00AC64E8  48 8B F8                        mov rdi, rax
00AC64EB  48 85 C0                        test rax, rax
00AC64EE  75 0A                           jne 0x140ac64fa
00AC64F0  BF 9A 00 00 C0                  mov edi, 0xc000009a
00AC64F5  E9 D7 02 00 00                  jmp 0x140ac67d1
00AC64FA  4C 8B 55 B8                     mov r10, qword ptr [rbp - 0x48]
00AC64FE  44 8B 8D 90 00 00 00            mov r9d, dword ptr [rbp + 0x90]
00AC6505  4C 89 50 08                     mov qword ptr [rax + 8], r10
00AC6509  44 89 08                        mov dword ptr [rax], r9d
00AC650C  45 85 E4                        test r12d, r12d
00AC650F  0F 84 AB 02 00 00               je 0x140ac67c0
00AC6515  4A 8D 14 28                     lea rdx, [rax + r13]
00AC6519  41 8B CC                        mov ecx, r12d
00AC651C  45 8B C4                        mov r8d, r12d
00AC651F  49 C1 E0 04                     shl r8, 4
00AC6523  4C 03 C2                        add r8, rdx
00AC6526  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
00AC652A  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00AC652E  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
00AC6532  49 8D 04 C8                     lea rax, [r8 + rcx*8]
00AC6536  41 83 F9 02                     cmp r9d, 2
00AC653A  75 08                           jne 0x140ac6544
00AC653C  48 8B C8                        mov rcx, rax
00AC653F  49 8B C3                        mov rax, r11
00AC6542  EB 04                           jmp 0x140ac6548
00AC6544  48 8D 0C 88                     lea rcx, [rax + rcx*4]
00AC6548  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00AC654C  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00AC6550  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
00AC6554  4C 89 47 20                     mov qword ptr [rdi + 0x20], r8
00AC6558  48 85 C0                        test rax, rax
00AC655B  74 04                           je 0x140ac6561
00AC655D  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00AC6561  4C 8B EF                        mov r13, rdi
00AC6564  4C 2B 6D D0                     sub r13, qword ptr [rbp - 0x30]
00AC6568  4D 85 D2                        test r10, r10
00AC656B  0F 84 3A 01 00 00               je 0x140ac66ab
00AC6571  F6 86 70 01 00 00 01            test byte ptr [rsi + 0x170], 1
00AC6578  0F 84 CF 01 00 00               je 0x140ac674d
00AC657E  45 85 E4                        test r12d, r12d
00AC6581  0F 84 27 02 00 00               je 0x140ac67ae
00AC6587  4C 8B 75 B0                     mov r14, qword ptr [rbp - 0x50]
00AC658B  49 8B DB                        mov rbx, r11
00AC658E  48 8B 75 B8                     mov rsi, qword ptr [rbp - 0x48]
00AC6592  4D 8B E3                        mov r12, r11
00AC6595  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
00AC6599  4D 8B CD                        mov r9, r13
00AC659C  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00AC65A0  48 03 CB                        add rcx, rbx
00AC65A3  41 8B 04 14                     mov eax, dword ptr [r12 + rdx]
00AC65A7  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AC65AB  41 8B 44 14 04                  mov eax, dword ptr [r12 + rdx + 4]
00AC65B0  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00AC65B4  41 8B 44 14 18                  mov eax, dword ptr [r12 + rdx + 0x18]
00AC65B9  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AC65BD  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AC65C2  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00AC65C7  48 8B CF                        mov rcx, rdi
00AC65CA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AC65CF  48 8D 45 88                     lea rax, [rbp - 0x78]
00AC65D3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AC65D8  48 8D 45 90                     lea rax, [rbp - 0x70]
00AC65DC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AC65E1  48 8D 45 98                     lea rax, [rbp - 0x68]
00AC65E5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC65EA  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AC65EE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AC65F3  E8 DC CE D3 FF                  call 0x1408034d4
00AC65F8  48 83 C3 10                     add rbx, 0x10
00AC65FC  4D 8D 64 24 1C                  lea r12, [r12 + 0x1c]
00AC6601  48 83 EE 01                     sub rsi, 1
00AC6605  75 8E                           jne 0x140ac6595
00AC6607  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
00AC660B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00AC6610  E9 96 01 00 00                  jmp 0x140ac67ab
00AC6615  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
00AC6619  49 8D 4E 30                     lea rcx, [r14 + 0x30]
00AC661D  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AC6621  4D 8B CD                        mov r9, r13
00AC6624  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
00AC6628  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00AC662C  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00AC6630  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AC6634  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AC6639  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00AC663E  48 8B CF                        mov rcx, rdi
00AC6641  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AC6646  48 8D 45 88                     lea rax, [rbp - 0x78]
00AC664A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AC664F  48 8D 45 90                     lea rax, [rbp - 0x70]
00AC6653  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AC6658  48 8D 45 98                     lea rax, [rbp - 0x68]
00AC665C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC6661  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AC6665  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AC666A  E8 65 CE D3 FF                  call 0x1408034d4
00AC666F  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00AC6673  45 33 DB                        xor r11d, r11d
00AC6676  49 8B CE                        mov rcx, r14
00AC6679  48 85 C0                        test rax, rax
00AC667C  74 23                           je 0x140ac66a1
00AC667E  48 8B 08                        mov rcx, qword ptr [rax]
00AC6681  4C 8B F0                        mov r14, rax
00AC6684  48 85 C9                        test rcx, rcx
00AC6687  74 22                           je 0x140ac66ab
00AC6689  48 8B 01                        mov rax, qword ptr [rcx]
00AC668C  4C 8B F1                        mov r14, rcx
00AC668F  48 8B C8                        mov rcx, rax
00AC6692  48 85 C0                        test rax, rax
00AC6695  75 F2                           jne 0x140ac6689
00AC6697  EB 12                           jmp 0x140ac66ab
00AC6699  49 39 0E                        cmp qword ptr [r14], rcx
00AC669C  74 0D                           je 0x140ac66ab
00AC669E  49 8B CE                        mov rcx, r14
00AC66A1  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
00AC66A5  49 83 E6 FC                     and r14, 0xfffffffffffffffc
00AC66A9  75 EE                           jne 0x140ac6699
00AC66AB  4D 85 F6                        test r14, r14
00AC66AE  0F 85 61 FF FF FF               jne 0x140ac6615
00AC66B4  4C 8B 35 05 EE 42 00            mov r14, qword ptr [rip + 0x42ee05]
00AC66BB  4C 8D 25 FE ED 42 00            lea r12, [rip + 0x42edfe]
00AC66C2  EB 7E                           jmp 0x140ac6742
00AC66C4  49 8B CE                        mov rcx, r14
00AC66C7  E8 0C DF D3 FF                  call 0x1408045d8
00AC66CC  85 C0                           test eax, eax
00AC66CE  74 6F                           je 0x140ac673f
00AC66D0  49 8B CE                        mov rcx, r14
00AC66D3  E8 5C 36 A1 FF                  call 0x1404d9d34
00AC66D8  4D 8B CD                        mov r9, r13
00AC66DB  48 8B 90 F8 00 00 00            mov rdx, qword ptr [rax + 0xf8]
00AC66E2  8B 80 10 01 00 00               mov eax, dword ptr [rax + 0x110]
00AC66E8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AC66EC  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AC66F1  8B 4A 78                        mov ecx, dword ptr [rdx + 0x78]
00AC66F4  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
00AC66F8  8B 8A 9C 00 00 00               mov ecx, dword ptr [rdx + 0x9c]
00AC66FE  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
00AC6702  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00AC6706  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00AC670B  48 8B CF                        mov rcx, rdi
00AC670E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AC6713  48 8D 45 88                     lea rax, [rbp - 0x78]
00AC6717  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AC671C  48 8D 45 90                     lea rax, [rbp - 0x70]
00AC6720  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AC6725  48 8D 45 98                     lea rax, [rbp - 0x68]
00AC6729  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC672E  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AC6732  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AC6737  E8 98 CD D3 FF                  call 0x1408034d4
00AC673C  45 33 DB                        xor r11d, r11d
00AC673F  4D 8B 36                        mov r14, qword ptr [r14]
00AC6742  4D 3B F4                        cmp r14, r12
00AC6745  0F 85 79 FF FF FF               jne 0x140ac66c4
00AC674B  EB 61                           jmp 0x140ac67ae
00AC674D  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
00AC6751  4D 8B 34 24                     mov r14, qword ptr [r12]
00AC6755  4D 3B F4                        cmp r14, r12
00AC6758  74 54                           je 0x140ac67ae
00AC675A  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
00AC675E  49 8D 4E 28                     lea rcx, [r14 + 0x28]
00AC6762  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AC6766  49 8D 56 20                     lea rdx, [r14 + 0x20]
00AC676A  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00AC676F  48 8D 45 88                     lea rax, [rbp - 0x78]
00AC6773  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00AC6778  4D 8B CD                        mov r9, r13
00AC677B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AC6780  48 8B CF                        mov rcx, rdi
00AC6783  48 8D 45 90                     lea rax, [rbp - 0x70]
00AC6787  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AC678C  48 8D 45 98                     lea rax, [rbp - 0x68]
00AC6790  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC6795  48 8D 45 A0                     lea rax, [rbp - 0x60]
00AC6799  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AC679E  E8 31 CD D3 FF                  call 0x1408034d4
00AC67A3  4D 8B 36                        mov r14, qword ptr [r14]
00AC67A6  4D 3B F4                        cmp r14, r12
00AC67A9  75 AF                           jne 0x140ac675a
00AC67AB  45 33 DB                        xor r11d, r11d
00AC67AE  4C 29 6F 20                     sub qword ptr [rdi + 0x20], r13
00AC67B2  4C 29 6F 18                     sub qword ptr [rdi + 0x18], r13
00AC67B6  4C 39 5D 88                     cmp qword ptr [rbp - 0x78], r11
00AC67BA  74 04                           je 0x140ac67c0
00AC67BC  4C 29 6F 28                     sub qword ptr [rdi + 0x28], r13
00AC67C0  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00AC67C4  48 89 38                        mov qword ptr [rax], rdi
00AC67C7  41 8B FB                        mov edi, r11d
00AC67CA  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00AC67CE  44 89 38                        mov dword ptr [rax], r15d
00AC67D1  4C 8B 7D 80                     mov r15, qword ptr [rbp - 0x80]
00AC67D5  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
00AC67D9  83 FB 08                        cmp ebx, 8
00AC67DC  72 08                           jb 0x140ac67e6
00AC67DE  49 8B CD                        mov rcx, r13
00AC67E1  E8 EA CE A0 FF                  call 0x1404d36d0
00AC67E6  41 BE 01 00 00 00               mov r14d, 1
00AC67EC  41 84 DE                        test r14b, bl
00AC67EF  74 43                           je 0x140ac6834
00AC67F1  49 8D 77 10                     lea rsi, [r15 + 0x10]
00AC67F5  33 C9                           xor ecx, ecx
00AC67F7  41 8D 46 10                     lea eax, [r14 + 0x10]
00AC67FB  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
00AC6800  74 08                           je 0x140ac680a
00AC6802  48 8B CE                        mov rcx, rsi
00AC6805  E8 36 CC 79 FF                  call 0x140263440
00AC680A  48 8B CE                        mov rcx, rsi
00AC680D  E8 EE AD 81 FF                  call 0x1402e1600
00AC6812  90                              nop
00AC6813  66 45 01 B5 E6 01 00 00         add word ptr [r13 + 0x1e6], r14w
00AC681B  75 12                           jne 0x140ac682f
00AC681D  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
00AC6824  90                              nop
00AC6825  48 39 00                        cmp qword ptr [rax], rax
00AC6828  74 05                           je 0x140ac682f
00AC682A  E8 51 C4 81 FF                  call 0x1402e2c80
00AC682F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00AC6834  F6 C3 04                        test bl, 4
00AC6837  74 0B                           je 0x140ac6844
00AC6839  33 D2                           xor edx, edx
00AC683B  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00AC683F  E8 EC 14 75 FF                  call 0x140217d30
00AC6844  F6 C3 02                        test bl, 2
00AC6847  74 0C                           je 0x140ac6855
00AC6849  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
00AC6850  E8 2B 36 88 FF                  call 0x140349e80
00AC6855  48 85 F6                        test rsi, rsi
00AC6858  74 0D                           je 0x140ac6867
00AC685A  BA 4D 6D 48 70                  mov edx, 0x70486d4d
00AC685F  48 8B CE                        mov rcx, rsi
00AC6862  E8 79 10 83 FF                  call 0x1402f78e0
00AC6867  4C 8B 75 B0                     mov r14, qword ptr [rbp - 0x50]
00AC686B  4D 85 F6                        test r14, r14
00AC686E  74 0A                           je 0x140ac687a
00AC6870  33 D2                           xor edx, edx
00AC6872  49 8B CE                        mov rcx, r14
00AC6875  E8 F6 BF 0B 00                  call 0x140b82870
00AC687A  8B C7                           mov eax, edi
00AC687C  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AC6880  48 33 CC                        xor rcx, rsp
00AC6883  E8 B8 5D BE FF                  call 0x1406ac640
00AC6888  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
00AC6890  48 81 C4 20 01 00 00            add rsp, 0x120
00AC6897  41 5F                           pop r15
00AC6899  41 5E                           pop r14
00AC689B  41 5D                           pop r13
00AC689D  41 5C                           pop r12
00AC689F  5F                              pop rdi
00AC68A0  5E                              pop rsi
00AC68A1  5D                              pop rbp
00AC68A2  C3                              ret
00AC68A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiQueryProcessActivePatches(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned __int8 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 3425721)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_mA0 = a1;
    v_stack_m88 = a4;
    v_stack_m90 = a3;
    v_stack_m78 = v_xmm0;
    v_stack_m98 = a2;
    v_stack_m68 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_mB0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mF0 = 0;
    v_r13 = v_rdi + 40;
    if (((unsigned int)((unsigned int)(a7))) != 2) { v_r13 = (unsigned int)(v_rdi + 48); }
    v_stack_mA8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = 0;
    if (a1 != 0) goto loc_00AC62E1;
    v_stack_mE0 = (unsigned int)(a1 + 8);
    result = MmAcquireLoadLock(v_rdi + 48, a2, a3, a4);
    v_stack_mB0 = result;
    goto loc_00AC621A;
loc_00AC6214:
loc_00AC621A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466)) != 0) goto loc_00AC6214;
    v_r10 = 0;
    if (*(unsigned __int64 *)(v_rip + 3609466) == 0) goto loc_00AC6299;
loc_00AC6239:
    v_r12 = (unsigned int)((0) + (1));
    result = 28;
    if (((unsigned int)((unsigned int)(a7))) == 2) { result = 1 + 23; }
    result = (result) + (v_r13);
    v_r15 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3609466) + 48)) + (result);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8) == 0) goto loc_00AC6282;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8)) == 0) goto loc_00AC628C;
loc_00AC626A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8))) != 0) goto loc_00AC626A;
    goto loc_00AC628C;
loc_00AC627A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8))))) goto loc_00AC628C;
loc_00AC6282:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3609466) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00AC627A;
loc_00AC628C:
    if (a1 != 0) goto loc_00AC6239;
    v_stack_mF8 = (unsigned int)(v_r12);
loc_00AC6299:
    if ((*(unsigned __int64 *)(v_rip + 4387360)) == (v_rip + 4387353)) goto loc_00AC649F;
loc_00AC62B0:
    result = MiIsActiveSystemHotPatch(*(unsigned __int64 *)(v_rip + 4387360), v_r15, a3, *(unsigned __int64 *)(v_rip + 4387360));
    if ((unsigned int)(result) == 0) goto loc_00AC62D4;
    v_r15 = (v_r15) + (24);
    v_r15 = (v_r15) + (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4387360) + 72));
    v_r12 = (unsigned int)((v_r12) + (1));
    if (((unsigned int)((unsigned int)(a7))) != 2) {
        v_r15 = (v_r15) + (4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4387360))) != (v_rip + 4387353)) goto loc_00AC62B0;
    goto loc_00AC649A;
loc_00AC62E1:
    v_stack_m120 = 1;
    v_stack_m128 = 1;
    v_stack_m130 = v_stack_mF0;
    v_stack_m138 = 0x70486D4DULL;
    result = ObpReferenceObjectByHandleWithTag(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4387360) + 72), (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5244848), a6);
    if (sign_flag) goto loc_00AC6855;
    result = ExAcquireRundownProtection(v_stack_mF0 + 488, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5244848), a6);
    result = (unsigned int)((result) & (1));
    if (condition_is_not_equal) goto loc_00AC6349;
    goto loc_00AC67D5;
loc_00AC6349:
    a2 = 0;
    result = KiStackAttachProcess(v_stack_mF0, a2, v_stack_m78, a6);
    v_rbx = (unsigned int)((result + result * 1) | (4));
    v_stack_mE0 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)((unsigned int)(0xC000010AULL))) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_mF0 + 368)))) == 0) goto loc_00AC63DE;
    result = VslQueryActiveSecurePatches(*(unsigned __int64 *)(v_stack_mF0 + 368), v_stack_mA8, v_stack_mF8, a6);
    v_r10 = 0;
    if (sign_flag) goto loc_00AC67D5;
    if ((unsigned int)((unsigned int)(v_stack_mF8)) == 0) goto loc_00AC64A4;
loc_00AC63B3:
    result = 28;
    if (((unsigned int)((unsigned int)(a7))) == 2) { result = v_r10 + 24; }
    result = (result) + (v_r13);
    v_r15 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mA8 + 8))) + (result);
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mF8)))) - (v_r10 + 1);
    if (condition_is_not_equal) goto loc_00AC63B3;
    v_r10 = 0;
    goto loc_00AC64A4;
loc_00AC63DE:
    a2 = 0;
    result = MiGetProcessHotPatchContext(v_stack_mF0, a2, v_r15, v_r10 + 24);
    v_r10 = 0;
    v_stack_mD8 = result;
    if (result == 0) goto loc_00AC64A4;
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(v_r10 + 1)));
    v_stack_mE0 = (unsigned int)(v_rbx);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, v_r10 + 24);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 16;
        a3 = 0;
        a2 = 0;
        a1 = result + 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    v_r10 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r10 + 1);
    }
    if ((*(unsigned __int64 *)(v_stack_mD8)) == v_stack_mD8) goto loc_00AC649F;
loc_00AC6471:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_mF8)) + ((unsigned int)(v_r10 + 1)));
    result = 28;
    if (((unsigned int)((unsigned int)(a7))) == 2) { result = 24; }
    result = (result) + (v_r13);
    v_r15 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mD8) + 40)) + (result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8))) != v_stack_mD8) goto loc_00AC6471;
    v_r10 = 0;
loc_00AC649A:
    v_stack_mF8 = (unsigned int)(v_r12);
loc_00AC649F:
loc_00AC64A4:
    if (((unsigned int)(a5)) >= v_r15) goto loc_00AC64D2;
    if (v_r15 <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00AC64C3;
    goto loc_00AC67D1;
loc_00AC64C3:
    *(unsigned __int64 *)(v_stack_m98) = 0;
    goto loc_00AC67CA;
loc_00AC64D2:
    result = MiAllocatePool(256, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x71486D4DULL), 24);
    v_r11 = 0;
    if (result != 0) goto loc_00AC64FA;
    goto loc_00AC67D1;
loc_00AC64FA:
    *(unsigned __int64 *)(result + 8) = v_stack_mA0;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(a7));
    if ((unsigned int)(v_r12) == 0) goto loc_00AC67C0;
    a3 = ((unsigned int)((unsigned int)(v_r12))) << (4);
    a3 = (a3) + (result + v_r13 * 1);
    v_stack_mC0 = result + v_r13 * 1;
    v_stack_mA0 = (unsigned int)((unsigned int)(v_r12));
    v_stack_mB8 = a3;
    if (((unsigned int)((unsigned int)(a7))) != 2) goto loc_00AC6544;
    goto loc_00AC6548;
loc_00AC6544:
loc_00AC6548:
    v_stack_mD0 = 0;
    v_stack_mC8 = 0 + a3 + (unsigned int)((unsigned int)(v_r12)) * 8 * 4;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 24) = result + v_r13 * 1;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 32) = a3;
    if (0 != 0) {
        *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 40) = 0;
    }
    v_r13 = ((unsigned int)(0xC000009AULL)) - (v_stack_m88);
    if (v_stack_mA0 == 0) goto loc_00AC66AB;
    if (((*(unsigned __int8 *)(v_stack_mF0 + 368)) & (1)) == 0) goto loc_00AC674D;
    if ((unsigned int)(v_r12) == 0) goto loc_00AC67AE;
loc_00AC6595:
    a1 = (*(unsigned __int64 *)(v_stack_mA8 + 8)) + (0);
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_mA8 + 16) * 1)));
    v_stack_mE4 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_mA8 + 16) * 1 + 4)));
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_stack_mA8 + 16) * 1 + 24)));
    v_stack_m110 = a1;
    v_stack_m118 = v_stack_mE8;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((unsigned int)(0xC000009AULL), *(unsigned __int64 *)(v_stack_mA8 + 16), a3, v_r13);
    v_rbx = (0) + (16);
    v_rsi = (v_stack_mA0) - (1);
    if (condition_is_not_equal) goto loc_00AC6595;
    goto loc_00AC67AB;
loc_00AC6615:
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + 24)));
    v_stack_mE4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + 28)));
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + 40)));
    v_stack_m110 = v_stack_mA8 + 48;
    v_stack_m118 = v_stack_mE8;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((unsigned int)(0xC000009AULL), *(unsigned __int64 *)(v_stack_mA8 + 16), a3, v_r13);
    v_r11 = 0;
    if (*(unsigned __int64 *)(v_stack_mA8 + 8) == 0) goto loc_00AC66A1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + 8)) == 0) goto loc_00AC66AB;
loc_00AC6689:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + 8))) != 0) goto loc_00AC6689;
    goto loc_00AC66AB;
loc_00AC6699:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + 8))))) goto loc_00AC66AB;
loc_00AC66A1:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00AC6699;
loc_00AC66AB:
    if (v_r14 != 0) goto loc_00AC6615;
    goto loc_00AC6742;
loc_00AC66C4:
    result = MiIsActiveSystemHotPatch(*(unsigned __int64 *)(v_rip + 4386309), *(unsigned __int64 *)(v_stack_mA8 + 16), a3, v_r13);
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 4386309);
        result = MiGetBaseLoaderPortion(a1, *(unsigned __int64 *)(v_stack_mA8 + 16), a3, v_r13);
        a4 = v_r13;
        a2 = *(unsigned __int64 *)(result + 248);
        result = *(unsigned int *)(result + 272);
        v_stack_m108 = (unsigned int)(result);
        result = v_stack_mE8;
        a1 = *(unsigned int *)(a2 + 120);
        v_stack_mE8 = (unsigned int)(a1);
        a1 = *(unsigned int *)(a2 + 156);
        v_stack_mE4 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 4386309) + 72;
        v_stack_m110 = a1;
        a1 = (unsigned int)(0xC000009AULL);
        v_stack_m118 = result;
        result = v_stack_mD0;
        v_stack_m120 = result;
        result = v_stack_mC8;
        v_stack_m128 = result;
        result = v_stack_mC0;
        v_stack_m130 = result;
        result = v_stack_mB8;
        v_stack_m138 = result;
        result = MiFillActivePatchesQueryBuffer(a1, a2, a3, a4);
        v_r11 = 0;
    }
loc_00AC6742:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4386309))) != (v_rip + 4386302)) goto loc_00AC66C4;
    goto loc_00AC67AE;
loc_00AC674D:
    if ((*(unsigned __int64 *)(v_stack_mD8)) == v_stack_mD8) goto loc_00AC67AE;
loc_00AC675A:
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mD8) + 64)));
    v_stack_m110 = *(unsigned __int64 *)(v_stack_mD8) + 40;
    v_stack_m118 = *(unsigned __int64 *)(v_stack_mD8) + 32;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((unsigned int)(0xC000009AULL), *(unsigned __int64 *)(v_stack_mD8) + 32, a3, v_r13);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8))) != v_stack_mD8) goto loc_00AC675A;
loc_00AC67AB:
    v_r11 = 0;
loc_00AC67AE:
    if (v_stack_mD0 != 0) {
    }
    *(unsigned __int64 *)(v_stack_m98) = (unsigned int)(0xC000009AULL);
loc_00AC67CA:
    *(unsigned int *)(v_stack_m90) = (unsigned int)(v_r15);
loc_00AC67D1:
loc_00AC67D5:
    result = v_stack_m90;
    if (((unsigned int)((unsigned int)(v_stack_mE0))) >= 8) {
        a1 = v_stack_mB0;
        result = MmReleaseLoadLock(a1, *(unsigned __int64 *)(v_stack_mD8) + 32, a3, v_r13);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_mE0)))) == 0) goto loc_00AC6834;
    a1 = 0;
    result = 1 + 16;
    if (!(condition_is_equal)) {
        a1 = v_stack_mD8 + 16;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(v_stack_mD8) + 32, a3, v_r13);
    }
    result = KeAbPostRelease(v_stack_mD8 + 16, *(unsigned __int64 *)(v_stack_mD8) + 32, a3, v_r13);
    if (condition_is_not_equal) goto loc_00AC682F;
    result = v_stack_mB0 + 152;
    if ((*(unsigned __int64 *)(v_stack_mB0 + 152)) != (v_stack_mB0 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mD8 + 16, *(unsigned __int64 *)(v_stack_mD8) + 32, a3, v_r13);
    }
loc_00AC6834:
    if ((((unsigned __int8)((unsigned int)(v_stack_mE0))) & (4)) != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = KiUnstackDetachProcess(a1, a2, a3, v_r13);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_mE0))) & (2)) != 0) {
        a1 = v_stack_mF0 + 488;
        result = ExReleaseRundownProtection(a1, a2, a3, v_r13);
    }
    if (v_stack_mF0 != 0) {
        a2 = 0x70486D4DULL;
        a1 = v_stack_mF0;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, v_r13);
    }
    if (v_stack_mA8 != 0) {
        a2 = 0;
        a1 = v_stack_mA8;
        result = ExFreePoolWithTag(a1, a2, a3, v_r13);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_r13);
    v_rsp = (v_rsp) + (288);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiQueryProcessActivePatches(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint8_t Arg6, uint32_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x3445B9)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_mA0 = Arg1;
    v_stack_m88 = Arg4;
    v_stack_m90 = Arg3;
    v_stack_m78 = v_xmm0;
    v_stack_m98 = Arg2;
    v_stack_m68 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_mB0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mF0 = 0;
    local_r13 = local_rdi + 40;
    if (((uint32_t)((uint32_t)(Arg7))) != 2) { local_r13 = (uint32_t)(local_rdi + 48); }
    v_stack_mA8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = 0;
    if (Arg1 != 0) goto loc_00AC62E1;
    v_stack_mE0 = (uint32_t)(Arg1 + 8);
    result = MmAcquireLoadLock(local_rdi + 48, Arg2, Arg3, Arg4);
    v_stack_mB0 = result;
    goto loc_00AC621A;
loc_00AC6214:
loc_00AC621A:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A)) != 0) goto loc_00AC6214;
    local_r10 = 0;
    if (*(uint64_t *)(v_rip + 0x37137A) == 0) goto loc_00AC6299;
loc_00AC6239:
    local_r12 = (uint32_t)((0) + (1));
    result = 28;
    if (((uint32_t)((uint32_t)(Arg7))) == 2) { result = 1 + 23; }
    result = (result) + (local_r13);
    local_r15 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x30)) + (result);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8) == 0) goto loc_00AC6282;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8)) == 0) goto loc_00AC628C;
loc_00AC626A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8))) != 0) goto loc_00AC626A;
    goto loc_00AC628C;
loc_00AC627A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8))))) goto loc_00AC628C;
loc_00AC6282:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37137A) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00AC627A;
loc_00AC628C:
    if (Arg1 != 0) goto loc_00AC6239;
    v_stack_mF8 = (uint32_t)(local_r12);
loc_00AC6299:
    if ((*(uint64_t *)(v_rip + 0x42F220)) == (v_rip + 4387353)) goto loc_00AC649F;
loc_00AC62B0:
    result = MiIsActiveSystemHotPatch(*(uint64_t *)(v_rip + 0x42F220), local_r15, Arg3, *(uint64_t *)(v_rip + 0x42F220));
    if ((uint32_t)(result) == 0) goto loc_00AC62D4;
    local_r15 = (local_r15) + (24);
    local_r15 = (local_r15) + (*(uint16_t *)(*(uint64_t *)(v_rip + 0x42F220) + 0x48));
    local_r12 = (uint32_t)((local_r12) + (1));
    if (((uint32_t)((uint32_t)(Arg7))) != 2) {
        local_r15 = (local_r15) + (4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42F220))) != (v_rip + 4387353)) goto loc_00AC62B0;
    goto loc_00AC649A;
loc_00AC62E1:
    v_stack_m120 = 1;
    v_stack_m128 = 1;
    v_stack_m130 = v_stack_mF0;
    v_stack_m138 = 0x70486D4DULL;
    result = ObpReferenceObjectByHandleWithTag(*(uint16_t *)(*(uint64_t *)(v_rip + 0x42F220) + 0x48), (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x5007B0), Arg6);
    if (sign_flag) goto loc_00AC6855;
    result = ExAcquireRundownProtection(v_stack_mF0 + 488, (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x5007B0), Arg6);
    result = (uint32_t)((result) & (1));
    if (condition_is_not_equal) goto loc_00AC6349;
    goto loc_00AC67D5;
loc_00AC6349:
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_mF0, Arg2, v_stack_m78, Arg6);
    local_rbx = (uint32_t)((result + result * 1) | (4));
    v_stack_mE0 = (uint32_t)(local_rbx);
    if ((((uint8_t)((uint32_t)(0xC000010AULL))) & ((uint8_t)(*(uint64_t *)(v_stack_mF0 + 0x170)))) == 0) goto loc_00AC63DE;
    result = VslQueryActiveSecurePatches(*(uint64_t *)(v_stack_mF0 + 0x170), v_stack_mA8, v_stack_mF8, Arg6);
    local_r10 = 0;
    if (sign_flag) goto loc_00AC67D5;
    if ((uint32_t)((uint32_t)(v_stack_mF8)) == 0) goto loc_00AC64A4;
loc_00AC63B3:
    result = 28;
    if (((uint32_t)((uint32_t)(Arg7))) == 2) { result = local_r10 + 24; }
    result = (result) + (local_r13);
    local_r15 = (*(uint16_t *)(*(uint64_t *)(v_stack_mA8 + 0x8))) + (result);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mF8)))) - (local_r10 + 1);
    if (condition_is_not_equal) goto loc_00AC63B3;
    local_r10 = 0;
    goto loc_00AC64A4;
loc_00AC63DE:
    Arg2 = 0;
    result = MiGetProcessHotPatchContext(v_stack_mF0, Arg2, local_r15, local_r10 + 24);
    local_r10 = 0;
    v_stack_mD8 = result;
    if (result == 0) goto loc_00AC64A4;
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(local_r10 + 1)));
    v_stack_mE0 = (uint32_t)(local_rbx);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, Arg3, local_r10 + 24);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = result + 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_r10 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r10 + 1);
    }
    if ((*(uint64_t *)(v_stack_mD8)) == v_stack_mD8) goto loc_00AC649F;
loc_00AC6471:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_mF8)) + ((uint32_t)(local_r10 + 1)));
    result = 28;
    if (((uint32_t)((uint32_t)(Arg7))) == 2) { result = 24; }
    result = (result) + (local_r13);
    local_r15 = (*(uint16_t *)(*(uint64_t *)(v_stack_mD8) + 0x28)) + (result);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD8))) != v_stack_mD8) goto loc_00AC6471;
    local_r10 = 0;
loc_00AC649A:
    v_stack_mF8 = (uint32_t)(local_r12);
loc_00AC649F:
loc_00AC64A4:
    if (((uint32_t)(Arg5)) >= local_r15) goto loc_00AC64D2;
    if (local_r15 <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00AC64C3;
    goto loc_00AC67D1;
loc_00AC64C3:
    *(uint64_t *)(v_stack_m98) = 0;
    goto loc_00AC67CA;
loc_00AC64D2:
    result = MiAllocatePool(256, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x71486D4DULL), 24);
    local_r11 = 0;
    if (result != 0) goto loc_00AC64FA;
    goto loc_00AC67D1;
loc_00AC64FA:
    *(uint64_t *)(result + 0x8) = v_stack_mA0;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(Arg7));
    if ((uint32_t)(local_r12) == 0) goto loc_00AC67C0;
    Arg3 = ((uint32_t)((uint32_t)(local_r12))) << (4);
    Arg3 = (Arg3) + (result + local_r13 * 1);
    v_stack_mC0 = result + local_r13 * 1;
    v_stack_mA0 = (uint32_t)((uint32_t)(local_r12));
    v_stack_mB8 = Arg3;
    if (((uint32_t)((uint32_t)(Arg7))) != 2) goto loc_00AC6544;
    goto loc_00AC6548;
loc_00AC6544:
loc_00AC6548:
    v_stack_mD0 = 0;
    v_stack_mC8 = 0 + Arg3 + (uint32_t)((uint32_t)(local_r12)) * 8 * 4;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x18) = result + local_r13 * 1;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x20) = Arg3;
    if (0 != 0) {
        *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x28) = 0;
    }
    local_r13 = ((uint32_t)(0xC000009AULL)) - (v_stack_m88);
    if (v_stack_mA0 == 0) goto loc_00AC66AB;
    if (((*(uint8_t *)(v_stack_mF0 + 0x170)) & (1)) == 0) goto loc_00AC674D;
    if ((uint32_t)(local_r12) == 0) goto loc_00AC67AE;
loc_00AC6595:
    Arg1 = (*(uint64_t *)(v_stack_mA8 + 0x8)) + (0);
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_stack_mA8 + 0x10) * 1)));
    v_stack_mE4 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_stack_mA8 + 0x10) * 1 + 0x4)));
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_stack_mA8 + 0x10) * 1 + 0x18)));
    v_stack_m110 = Arg1;
    v_stack_m118 = v_stack_mE8;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((uint32_t)(0xC000009AULL), *(uint64_t *)(v_stack_mA8 + 0x10), Arg3, local_r13);
    local_rbx = (0) + (16);
    local_rsi = (v_stack_mA0) - (1);
    if (condition_is_not_equal) goto loc_00AC6595;
    goto loc_00AC67AB;
loc_00AC6615:
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0x18)));
    v_stack_mE4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0x1C)));
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0x28)));
    v_stack_m110 = v_stack_mA8 + 48;
    v_stack_m118 = v_stack_mE8;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((uint32_t)(0xC000009AULL), *(uint64_t *)(v_stack_mA8 + 0x10), Arg3, local_r13);
    local_r11 = 0;
    if (*(uint64_t *)(v_stack_mA8 + 0x8) == 0) goto loc_00AC66A1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + 0x8)) == 0) goto loc_00AC66AB;
loc_00AC6689:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + 0x8))) != 0) goto loc_00AC6689;
    goto loc_00AC66AB;
loc_00AC6699:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + 0x8))))) goto loc_00AC66AB;
loc_00AC66A1:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00AC6699;
loc_00AC66AB:
    if (local_r14 != 0) goto loc_00AC6615;
    goto loc_00AC6742;
loc_00AC66C4:
    result = MiIsActiveSystemHotPatch(*(uint64_t *)(v_rip + 0x42EE05), *(uint64_t *)(v_stack_mA8 + 0x10), Arg3, local_r13);
    if ((uint32_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x42EE05);
        result = MiGetBaseLoaderPortion(Arg1, *(uint64_t *)(v_stack_mA8 + 0x10), Arg3, local_r13);
        Arg4 = local_r13;
        Arg2 = *(uint64_t *)(result + 0xF8);
        result = *(uint32_t *)(result + 0x110);
        v_stack_m108 = (uint32_t)(result);
        result = v_stack_mE8;
        Arg1 = *(uint32_t *)(Arg2 + 0x78);
        v_stack_mE8 = (uint32_t)(Arg1);
        Arg1 = *(uint32_t *)(Arg2 + 0x9C);
        v_stack_mE4 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x42EE05) + 72;
        v_stack_m110 = Arg1;
        Arg1 = (uint32_t)(0xC000009AULL);
        v_stack_m118 = result;
        result = v_stack_mD0;
        v_stack_m120 = result;
        result = v_stack_mC8;
        v_stack_m128 = result;
        result = v_stack_mC0;
        v_stack_m130 = result;
        result = v_stack_mB8;
        v_stack_m138 = result;
        result = MiFillActivePatchesQueryBuffer(Arg1, Arg2, Arg3, Arg4);
        local_r11 = 0;
    }
loc_00AC6742:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42EE05))) != (v_rip + 4386302)) goto loc_00AC66C4;
    goto loc_00AC67AE;
loc_00AC674D:
    if ((*(uint64_t *)(v_stack_mD8)) == v_stack_mD8) goto loc_00AC67AE;
loc_00AC675A:
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mD8) + 0x40)));
    v_stack_m110 = *(uint64_t *)(v_stack_mD8) + 40;
    v_stack_m118 = *(uint64_t *)(v_stack_mD8) + 32;
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mC8;
    v_stack_m130 = v_stack_mC0;
    v_stack_m138 = v_stack_mB8;
    result = MiFillActivePatchesQueryBuffer((uint32_t)(0xC000009AULL), *(uint64_t *)(v_stack_mD8) + 32, Arg3, local_r13);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD8))) != v_stack_mD8) goto loc_00AC675A;
loc_00AC67AB:
    local_r11 = 0;
loc_00AC67AE:
    if (v_stack_mD0 != 0) {
    }
    *(uint64_t *)(v_stack_m98) = (uint32_t)(0xC000009AULL);
loc_00AC67CA:
    *(uint32_t *)(v_stack_m90) = (uint32_t)(local_r15);
loc_00AC67D1:
loc_00AC67D5:
    result = v_stack_m90;
    if (((uint32_t)((uint32_t)(v_stack_mE0))) >= 8) {
        Arg1 = v_stack_mB0;
        result = MmReleaseLoadLock(Arg1, *(uint64_t *)(v_stack_mD8) + 32, Arg3, local_r13);
    }
    if (((1) & ((uint8_t)((uint32_t)(v_stack_mE0)))) == 0) goto loc_00AC6834;
    Arg1 = 0;
    result = 1 + 16;
    if (!(condition_is_equal)) {
        Arg1 = v_stack_mD8 + 16;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(v_stack_mD8) + 32, Arg3, local_r13);
    }
    result = KeAbPostRelease(v_stack_mD8 + 16, *(uint64_t *)(v_stack_mD8) + 32, Arg3, local_r13);
    if (condition_is_not_equal) goto loc_00AC682F;
    result = v_stack_mB0 + 152;
    if ((*(uint64_t *)(v_stack_mB0 + 0x98)) != (v_stack_mB0 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mD8 + 16, *(uint64_t *)(v_stack_mD8) + 32, Arg3, local_r13);
    }
loc_00AC6834:
    if ((((uint8_t)((uint32_t)(v_stack_mE0))) & (4)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, local_r13);
    }
    if ((((uint8_t)((uint32_t)(v_stack_mE0))) & (2)) != 0) {
        Arg1 = v_stack_mF0 + 488;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, local_r13);
    }
    if (v_stack_mF0 != 0) {
        Arg2 = 0x70486D4DULL;
        Arg1 = v_stack_mF0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, local_r13);
    }
    if (v_stack_mA8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mA8;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, local_r13);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, local_r13);
    local_rsp = (local_rsp) + (288);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC6164&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
