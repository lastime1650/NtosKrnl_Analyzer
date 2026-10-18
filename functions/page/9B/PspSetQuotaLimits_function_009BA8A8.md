# PspSetQuotaLimits

- RVA: `0x009BA8A8`–`0x009BADC5` (길이 `1,309` bytes)
- VA: `0x00000001409BA8A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009EB84`
- 디코드: `284`개 명령, `1,309/1,309` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x009BA8F7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009BAA90` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009BAAFB` → [PspSinglePrivCheck](PspSinglePrivCheck_function_009BADCC.md) (function, `0x009BADCC`)
- `0x009BAB35` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009BAB59` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009BAB78` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009BAB9D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009BABAF` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009BABD9` → [MmAdjustWorkingSetSizeEx](../../text/47/MmAdjustWorkingSetSizeEx_function_0047D8D4.md) (function, `0x0047D8D4`)
- `0x009BAC0C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009BAC29` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x009BAC38` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009BAC82` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009BAC91` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009BACA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009BAD10` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009BAD36` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009BAD82` → [MmEnforceWorkingSetLimit](../../text/48/MmEnforceWorkingSetLimit_function_004881E0.md) (function, `0x004881E0`)
- `0x009BADBB` → [SePrivilegedServiceAuditAlarm](../87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) (function, `0x00871CB0`)

### Direct callers
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5EAB`

### Static image references
- `0x009BA8C2` → RVA `0x00E0A740` (`.data`; read)
- `0x009BAA62` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x009BAAA9` → RVA `0x00E27F80` (`.data`; read)
- `0x009BAB71` → RVA `0x00FC70B0` (`ALMOSTRO`; read)
- `0x009BAB80` → RVA `0x00FC70B0` (`ALMOSTRO`; read/write)
- `0x009BADB4` → RVA `0x00B4BE88` (`PspWorkingSetAdjustService`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x009BA8F7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009BAB35` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009BAB59` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009BAB78` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009BAB9D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009BABAF` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009BABD9` → [MmAdjustWorkingSetSizeEx](../../text/47/MmAdjustWorkingSetSizeEx_function_0047D8D4.md) (`PAGE` → `.text`)
  - `0x009BAC0C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009BAC29` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x009BAC38` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009BAC91` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009BACA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009BAD10` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009BAD36` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009BAD82` → [MmEnforceWorkingSetLimit](../../text/48/MmEnforceWorkingSetLimit_function_004881E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009BAD00` → [sub_00B2E606](../B2/Unknown_function_00B2E606.md) (`tail-transfer`)
  - `0x009BAD20` → [sub_00B2E606](../B2/Unknown_function_00B2E606.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009BA8A8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
009BA8AD  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009BA8B2  57                              push rdi
009BA8B3  41 54                           push r12
009BA8B5  41 55                           push r13
009BA8B7  41 56                           push r14
009BA8B9  41 57                           push r15
009BA8BB  48 81 EC 30 01 00 00            sub rsp, 0x130
009BA8C2  48 8B 05 77 FE 44 00            mov rax, qword ptr [rip + 0x44fe77]
009BA8C9  48 33 C4                        xor rax, rsp
009BA8CC  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
009BA8D4  41 8A F1                        mov sil, r9b
009BA8D7  41 8B F8                        mov edi, r8d
009BA8DA  48 8B DA                        mov rbx, rdx
009BA8DD  4C 8B F1                        mov r14, rcx
009BA8E0  45 33 E4                        xor r12d, r12d
009BA8E3  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
009BA8E8  45 8D 7C 24 58                  lea r15d, [r12 + 0x58]
009BA8ED  45 8B C7                        mov r8d, r15d
009BA8F0  33 D2                           xor edx, edx
009BA8F2  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009BA8F7  E8 44 C3 D0 FF                  call 0x1406c6c40
009BA8FC  0F 57 C0                        xorps xmm0, xmm0
009BA8FF  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
009BA907  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
009BA90F  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
009BA917  44 88 64 24 43                  mov byte ptr [rsp + 0x43], r12b
009BA91C  0F 57 C9                        xorps xmm1, xmm1
009BA91F  33 C0                           xor eax, eax
009BA921  0F 11 8C 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm1
009BA929  0F 11 8C 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm1
009BA931  0F 11 8C 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm1
009BA939  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
009BA941  83 FF 30                        cmp edi, 0x30
009BA944  75 41                           jne 0x1409ba987
009BA946  0F 10 03                        movups xmm0, xmmword ptr [rbx]
009BA949  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
009BA94E  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
009BA952  0F 29 4C 24 70                  movaps xmmword ptr [rsp + 0x70], xmm1
009BA957  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
009BA95B  0F 29 84 24 80 00 00 00         movaps xmmword ptr [rsp + 0x80], xmm0
009BA963  0F 57 C9                        xorps xmm1, xmm1
009BA966  0F 11 8C 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm1
009BA96E  0F 11 8C 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm1
009BA976  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
009BA97E  8D 58 01                        lea ebx, [rax + 1]
009BA981  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
009BA985  EB 63                           jmp 0x1409ba9ea
009BA987  41 3B FF                        cmp edi, r15d
009BA98A  75 4F                           jne 0x1409ba9db
009BA98C  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
009BA991  0F 10 03                        movups xmm0, xmmword ptr [rbx]
009BA994  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
009BA999  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
009BA99D  0F 29 4C 24 70                  movaps xmmword ptr [rsp + 0x70], xmm1
009BA9A2  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
009BA9A6  0F 29 84 24 80 00 00 00         movaps xmmword ptr [rsp + 0x80], xmm0
009BA9AE  0F 10 4B 30                     movups xmm1, xmmword ptr [rbx + 0x30]
009BA9B2  0F 29 8C 24 90 00 00 00         movaps xmmword ptr [rsp + 0x90], xmm1
009BA9BA  0F 10 43 40                     movups xmm0, xmmword ptr [rbx + 0x40]
009BA9BE  0F 29 84 24 A0 00 00 00         movaps xmmword ptr [rsp + 0xa0], xmm0
009BA9C6  F2 0F 10 4B 50                  movsd xmm1, qword ptr [rbx + 0x50]
009BA9CB  F2 0F 11 8C 24 B0 00 00 00      movsd qword ptr [rsp + 0xb0], xmm1
009BA9D4  BB 01 00 00 00                  mov ebx, 1
009BA9D9  EB AA                           jmp 0x1409ba985
009BA9DB  B8 04 00 00 C0                  mov eax, 0xc0000004
009BA9E0  E9 B4 02 00 00                  jmp 0x1409bac99
009BA9E5  E9 AF 02 00 00                  jmp 0x1409bac99
009BA9EA  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
009BA9F1  F7 C1 E0 FF FF FF               test ecx, 0xffffffe0
009BA9F7  0F 85 E6 02 00 00               jne 0x1409bace3
009BA9FD  8B C1                           mov eax, ecx
009BA9FF  83 E0 03                        and eax, 3
009BAA02  3C 03                           cmp al, 3
009BAA04  0F 84 D9 02 00 00               je 0x1409bace3
009BAA0A  8B C1                           mov eax, ecx
009BAA0C  83 E0 0C                        and eax, 0xc
009BAA0F  3C 0C                           cmp al, 0xc
009BAA11  0F 84 CC 02 00 00               je 0x1409bace3
009BAA17  B8 08 00 00 00                  mov eax, 8
009BAA1C  84 CB                           test bl, cl
009BAA1E  0F 85 01 03 00 00               jne 0x1409bad25
009BAA24  F6 C1 02                        test cl, 2
009BAA27  41 8B FC                        mov edi, r12d
009BAA2A  0F 45 F8                        cmovne edi, eax
009BAA2D  F6 C1 04                        test cl, 4
009BAA30  0F 85 E1 00 00 00               jne 0x1409bab17
009BAA36  84 C8                           test al, cl
009BAA38  74 03                           je 0x1409baa3d
009BAA3A  83 CF 02                        or edi, 2
009BAA3D  8B 84 24 B4 00 00 00            mov eax, dword ptr [rsp + 0xb4]
009BAA44  48 0B 84 24 A8 00 00 00         or rax, qword ptr [rsp + 0xa8]
009BAA4C  48 0B 84 24 A0 00 00 00         or rax, qword ptr [rsp + 0xa0]
009BAA54  48 0B 84 24 98 00 00 00         or rax, qword ptr [rsp + 0x98]
009BAA5C  0F 85 81 02 00 00               jne 0x1409bace3
009BAA62  4C 8B 05 2F C0 60 00            mov r8, qword ptr [rip + 0x60c02f]
009BAA69  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
009BAA6E  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
009BAA73  48 8D 44 24 48                  lea rax, [rsp + 0x48]
009BAA78  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009BAA7D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009BAA85  44 8A CE                        mov r9b, sil
009BAA88  BA 00 01 00 00                  mov edx, 0x100
009BAA8D  49 8B CE                        mov rcx, r14
009BAA90  E8 BB EB EA FF                  call 0x140869650
009BAA95  85 C0                           test eax, eax
009BAA97  0F 88 FC 01 00 00               js 0x1409bac99
009BAA9D  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
009BAAA6  45 8B F4                        mov r14d, r12d
009BAAA9  48 8D 0D D0 D4 46 00            lea rcx, [rip + 0x46d4d0]
009BAAB0  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
009BAAB5  48 39 88 F8 02 00 00            cmp qword ptr [rax + 0x2f8], rcx
009BAABC  0F 84 28 02 00 00               je 0x1409bacea
009BAAC2  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009BAAC7  48 85 C0                        test rax, rax
009BAACA  0F 84 B7 01 00 00               je 0x1409bac87
009BAAD0  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009BAAD5  48 85 C9                        test rcx, rcx
009BAAD8  0F 84 A9 01 00 00               je 0x1409bac87
009BAADE  48 83 CA FF                     or rdx, 0xffffffffffffffff
009BAAE2  48 3B C2                        cmp rax, rdx
009BAAE5  0F 84 DC 01 00 00               je 0x1409bacc7
009BAAEB  44 88 64 24 41                  mov byte ptr [rsp + 0x41], r12b
009BAAF0  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
009BAAF8  44 8A C6                        mov r8b, sil
009BAAFB  E8 CC 02 00 00                  call 0x1409badcc
009BAB00  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009BAB04  88 5C 24 44                     mov byte ptr [rsp + 0x44], bl
009BAB08  45 8A FC                        mov r15b, r12b
009BAB0B  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
009BAB10  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
009BAB15  EB 0A                           jmp 0x1409bab21
009BAB17  0B FB                           or edi, ebx
009BAB19  E9 1F FF FF FF                  jmp 0x1409baa3d
009BAB1E  45 33 E4                        xor r12d, r12d
009BAB21  44 88 64 24 42                  mov byte ptr [rsp + 0x42], r12b
009BAB26  4C 8D 84 24 F8 00 00 00         lea r8, [rsp + 0xf8]
009BAB2E  33 D2                           xor edx, edx
009BAB30  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BAB35  E8 E6 BC 85 FF                  call 0x140216820
009BAB3A  48 83 C8 FF                     or rax, 0xffffffffffffffff
009BAB3E  66 41 01 85 E6 01 00 00         add word ptr [r13 + 0x1e6], ax
009BAB46  90                              nop
009BAB47  48 8B B6 A0 02 00 00            mov rsi, qword ptr [rsi + 0x2a0]
009BAB4E  48 85 F6                        test rsi, rsi
009BAB51  74 66                           je 0x1409babb9
009BAB53  8A D3                           mov dl, bl
009BAB55  48 8D 4E 38                     lea rcx, [rsi + 0x38]
009BAB59  E8 C2 A2 85 FF                  call 0x140214e20
009BAB5E  8B 86 20 04 00 00               mov eax, dword ptr [rsi + 0x420]
009BAB64  84 C3                           test bl, al
009BAB66  0F 85 D4 01 00 00               jne 0x1409bad40
009BAB6C  45 33 C0                        xor r8d, r8d
009BAB6F  33 D2                           xor edx, edx
009BAB71  48 8D 0D 38 C5 60 00            lea rcx, [rip + 0x60c538]
009BAB78  E8 B3 56 85 FF                  call 0x140210230
009BAB7D  4C 8B F0                        mov r14, rax
009BAB80  F0 48 0F BA 2D 26 C5 60 00 00   lock bts qword ptr [rip + 0x60c526], 0
009BAB8A  73 16                           jae 0x1409baba2
009BAB8C  4C 8D 05 1D C5 60 00            lea r8, [rip + 0x60c51d]
009BAB93  48 8B D0                        mov rdx, rax
009BAB96  48 8D 0D 13 C5 60 00            lea rcx, [rip + 0x60c513]
009BAB9D  E8 EE 50 85 FF                  call 0x14020fc90
009BABA2  4D 85 F6                        test r14, r14
009BABA5  74 04                           je 0x1409babab
009BABA7  41 88 5E 0A                     mov byte ptr [r14 + 0xa], bl
009BABAB  48 8D 4E 38                     lea rcx, [rsi + 0x38]
009BABAF  E8 5C 4E 8A FF                  call 0x14025fa10
009BABB4  44 8A 64 24 42                  mov r12b, byte ptr [rsp + 0x42]
009BABB9  48 8D 44 24 43                  lea rax, [rsp + 0x43]
009BABBE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009BABC3  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
009BABC7  44 8A 4C 24 50                  mov r9b, byte ptr [rsp + 0x50]
009BABCC  45 33 C0                        xor r8d, r8d
009BABCF  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
009BABD4  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009BABD9  E8 F6 2C AC FF                  call 0x14047d8d4
009BABDE  44 8B F0                        mov r14d, eax
009BABE1  85 C0                           test eax, eax
009BABE3  0F 88 89 01 00 00               js 0x1409bad72
009BABE9  48 85 F6                        test rsi, rsi
009BABEC  74 23                           je 0x1409bac11
009BABEE  48 83 C8 FF                     or rax, 0xffffffffffffffff
009BABF2  F0 48 0F C1 05 B5 C4 60 00      lock xadd qword ptr [rip + 0x60c4b5], rax
009BABFB  24 06                           and al, 6
009BABFD  3C 02                           cmp al, 2
009BABFF  0F 84 2A 01 00 00               je 0x1409bad2f
009BAC05  48 8D 0D A4 C4 60 00            lea rcx, [rip + 0x60c4a4]
009BAC0C  E8 EF 69 92 FF                  call 0x1402e1600
009BAC11  90                              nop
009BAC12  66 41 01 9D E6 01 00 00         add word ptr [r13 + 0x1e6], bx
009BAC1A  75 12                           jne 0x1409bac2e
009BAC1C  90                              nop
009BAC1D  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
009BAC24  48 39 00                        cmp qword ptr [rax], rax
009BAC27  74 05                           je 0x1409bac2e
009BAC29  E8 52 80 92 FF                  call 0x1402e2c80
009BAC2E  33 D2                           xor edx, edx
009BAC30  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
009BAC38  E8 F3 D0 85 FF                  call 0x140217d30
009BAC3D  38 5C 24 43                     cmp byte ptr [rsp + 0x43], bl
009BAC41  0F 84 45 01 00 00               je 0x1409bad8c
009BAC47  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009BAC4C  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
009BAC53  48 3B C6                        cmp rax, rsi
009BAC56  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
009BAC5B  0F 85 BD FE FF FF               jne 0x1409bab1e
009BAC61  38 5C 24 44                     cmp byte ptr [rsp + 0x44], bl
009BAC65  75 20                           jne 0x1409bac87
009BAC67  80 BC 24 F4 00 00 00 00         cmp byte ptr [rsp + 0xf4], 0
009BAC6F  74 16                           je 0x1409bac87
009BAC71  44 3A FB                        cmp r15b, bl
009BAC74  0F 84 22 01 00 00               je 0x1409bad9c
009BAC7A  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
009BAC82  E8 89 0A EB FF                  call 0x14086b710
009BAC87  BA 50 73 51 79                  mov edx, 0x79517350
009BAC8C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BAC91  E8 4A CC 93 FF                  call 0x1402f78e0
009BAC96  41 8B C6                        mov eax, r14d
009BAC99  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
009BACA1  48 33 CC                        xor rcx, rsp
009BACA4  E8 97 19 CF FF                  call 0x1406ac640
009BACA9  4C 8D 9C 24 30 01 00 00         lea r11, [rsp + 0x130]
009BACB1  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
009BACB5  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009BACB9  49 8B E3                        mov rsp, r11
009BACBC  41 5F                           pop r15
009BACBE  41 5E                           pop r14
009BACC0  41 5D                           pop r13
009BACC2  41 5C                           pop r12
009BACC4  5F                              pop rdi
009BACC5  C3                              ret
009BACC6  CC                              int3
009BACC7  48 3B CA                        cmp rcx, rdx
009BACCA  0F 85 1B FE FF FF               jne 0x1409baaeb
009BACD0  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
009BACD4  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
009BACD9  44 88 64 24 44                  mov byte ptr [rsp + 0x44], r12b
009BACDE  E9 25 FE FF FF                  jmp 0x1409bab08
009BACE3  B8 0D 00 00 C0                  mov eax, 0xc000000d
009BACE8  EB AF                           jmp 0x1409bac99
009BACEA  4C 39 64 24 70                  cmp qword ptr [rsp + 0x70], r12
009BACEF  74 0B                           je 0x1409bacfc
009BACF1  4C 39 64 24 78                  cmp qword ptr [rsp + 0x78], r12
009BACF6  0F 85 C6 FD FF FF               jne 0x1409baac2
009BACFC  38 5C 24 40                     cmp byte ptr [rsp + 0x40], bl
009BAD00  0F 85 00 39 17 00               jne 0x140b2e606
009BAD06  4D 8B C7                        mov r8, r15
009BAD09  33 D2                           xor edx, edx
009BAD0B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009BAD10  E8 2B BF D0 FF                  call 0x1406c6c40
009BAD15  C7 84 24 B0 00 00 00 10 00 00 00  mov dword ptr [rsp + 0xb0], 0x10
009BAD20  E9 E1 38 17 00                  jmp 0x140b2e606
009BAD25  BF 04 00 00 00                  mov edi, 4
009BAD2A  E9 FE FC FF FF                  jmp 0x1409baa2d
009BAD2F  48 8D 0D 7A C3 60 00            lea rcx, [rip + 0x60c37a]
009BAD36  E8 95 B0 8A FF                  call 0x140265dd0
009BAD3B  E9 C5 FE FF FF                  jmp 0x1409bac05
009BAD40  8B FB                           mov edi, ebx
009BAD42  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
009BAD46  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
009BAD4A  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
009BAD4F  0F 85 17 FE FF FF               jne 0x1409bab6c
009BAD55  48 8B 86 E8 03 00 00            mov rax, qword ptr [rsi + 0x3e8]
009BAD5C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009BAD61  48 8B 86 F0 03 00 00            mov rax, qword ptr [rsi + 0x3f0]
009BAD68  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009BAD6D  E9 FA FD FF FF                  jmp 0x1409bab6c
009BAD72  44 3A E3                        cmp r12b, bl
009BAD75  0F 85 6E FE FF FF               jne 0x1409babe9
009BAD7B  8B D7                           mov edx, edi
009BAD7D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BAD82  E8 59 D4 AC FF                  call 0x1404881e0
009BAD87  E9 5D FE FF FF                  jmp 0x1409babe9
009BAD8C  45 0F B6 FF                     movzx r15d, r15b
009BAD90  45 84 E4                        test r12b, r12b
009BAD93  44 0F 44 FB                     cmove r15d, ebx
009BAD97  E9 AB FE FF FF                  jmp 0x1409bac47
009BAD9C  44 8A 8C 24 F5 00 00 00         mov r9b, byte ptr [rsp + 0xf5]
009BADA4  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
009BADAC  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
009BADB4  48 8D 0D CD 10 19 00            lea rcx, [rip + 0x1910cd]
009BADBB  E8 F0 6E EB FF                  call 0x140871cb0
009BADC0  E9 B5 FE FF FF                  jmp 0x1409bac7a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspSetQuotaLimits(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int8 v_stack_m114;
    unsigned __int8 v_stack_m115;
    unsigned __int8 v_stack_m116;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int8 v_stack_m3B;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mEC;
    unsigned __int8 v_stack_mEE;
    unsigned __int8 v_stack_mEF;
    unsigned __int8 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 4521591)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r12 = 0;
    v_stack_m110 = 0;
    a2 = 0;
    result = memset(v_stack_mF8, a2, (unsigned int)((unsigned int)(v_r12 + 88)), a4);
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    v_stack_m115 = 0;
    result = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = 0;
    if (((unsigned int)((unsigned int)(a3))) != 48) goto loc_009BA987;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = 0;
    v_stack_m118 = (unsigned __int8)(result + 1);
loc_009BA985:
    goto loc_009BA9EA;
loc_009BA987:
    if (((unsigned int)((unsigned int)(a3))) != ((unsigned int)(v_r12 + 88))) goto loc_009BA9DB;
    v_stack_m118 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    goto loc_009BA985;
loc_009BA9DB:
    goto loc_009BAC99;
loc_009BA9EA:
    if ((((unsigned int)((unsigned int)(v_stack_mA8))) & (0xFFFFFFE0ULL)) != 0) goto loc_009BACE3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mA8)))) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_009BACE3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mA8)))) & (12));
    if (((unsigned __int8)(result)) == 12) goto loc_009BACE3;
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_mA8)))) != 0) goto loc_009BAD25;
    v_rdi = 0;
    if ((((unsigned __int8)((unsigned int)(v_stack_mA8))) & (2)) != 0) { v_rdi = 8; }
loc_009BAA2D:
    if ((((unsigned __int8)((unsigned int)(v_stack_mA8))) & (4)) != 0) goto loc_009BAB17;
    if (((8) & ((unsigned __int8)((unsigned int)(v_stack_mA8)))) != 0) {
        v_rdi = (unsigned int)((v_rdi) | (2));
    }
    result = ((unsigned int)(v_stack_mA4)) | (v_stack_mB0);
    result = (result) | (v_stack_mB8);
    result = (result) | (v_stack_mC0);
    if (condition_is_not_equal) goto loc_009BACE3;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_m110;
    v_stack_m138 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, 256, *(unsigned __int64 *)(v_rip + 6340655), a4);
    if (sign_flag) goto loc_009BAC99;
    if ((*(unsigned __int64 *)(v_stack_m110 + 760)) == (v_rip + 4642000)) goto loc_009BACEA;
loc_009BAAC2:
    if (v_stack_mE8 == 0) goto loc_009BAC87;
    if (v_stack_mE0 == 0) goto loc_009BAC87;
    a2 = (256) | (-1);
    if (v_stack_mE8 == a2) goto loc_009BACC7;
loc_009BAAEB:
    v_stack_m117 = 0;
    result = PspSinglePrivCheck(v_stack_mE0, a2, a4, v_stack_m98);
    v_stack_m108 = (unsigned int)(result);
    v_stack_m114 = 1;
loc_009BAB08:
    v_stack_m100 = v_stack_m110;
    goto loc_009BAB21;
loc_009BAB17:
    v_rdi = (unsigned int)((v_rdi) | (1));
    goto loc_009BAA3D;
loc_009BAB1E:
    v_r12 = 0;
loc_009BAB21:
    v_stack_m116 = 0;
    a2 = 0;
    result = KiStackAttachProcess(v_stack_m110, a2, v_stack_m60, v_stack_m98);
    result = (result) | (-1);
    if (*(unsigned __int64 *)(v_stack_m110 + 672) == 0) goto loc_009BABB9;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m110 + 672) + 56, 1, v_stack_m60, v_stack_m98);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110 + 672) + 1056))))) != 0) goto loc_009BAD40;
loc_009BAB6C:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6341944, a2, a3, v_stack_m98);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6341917;
        a2 = result;
        a1 = v_rip + 6341907;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m98);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m110 + 672) + 56, a2, a3, v_stack_m98);
loc_009BABB9:
    v_stack_m130 = v_stack_m115;
    v_stack_m138 = (unsigned int)(v_rdi);
    a3 = 0;
    result = MmAdjustWorkingSetSizeEx(v_stack_mE8, v_stack_mE0, a3, v_stack_m108);
    if (sign_flag) goto loc_009BAD72;
loc_009BABE9:
    if (*(unsigned __int64 *)(v_stack_m110 + 672) == 0) goto loc_009BAC11;
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009BAD2F;
loc_009BAC05:
    result = KeAbPostRelease(v_rip + 6341796, v_stack_mE0, a3, v_stack_m108);
loc_009BAC11:
    if (((unsigned __int8)(result)) != 2) goto loc_009BAC2E;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 6341796, v_stack_mE0, a3, v_stack_m108);
    }
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m60, a2, a3, v_stack_m108);
    if (v_stack_m115 == 1) goto loc_009BAD8C;
loc_009BAC47:
    if ((*(unsigned __int64 *)(v_stack_m100 + 672)) != (*(unsigned __int64 *)(v_stack_m110 + 672))) goto loc_009BAB1E;
    if (v_stack_m114 != 1) goto loc_009BAC87;
    if (v_stack_m64 == 0) goto loc_009BAC87;
    if (0 == 1) goto loc_009BAD9C;
loc_009BAC7A:
    result = SeReleaseSubjectContext(v_stack_m98, a2, a3, v_stack_m108);
loc_009BAC87:
    result = ObfDereferenceObjectWithTag(v_stack_m110, (unsigned int)(0x79517350ULL), a3, v_stack_m108);
loc_009BAC99:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x79517350ULL), a3, v_stack_m108);
    return result;
loc_009BACC7:
    if (a1 != ((unsigned int)(0x79517350ULL))) goto loc_009BAAEB;
    v_stack_mEF = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    v_stack_mE0 = (unsigned __int8)(v_stack_m116);
    v_stack_mEC = (unsigned __int8)(v_stack_m116);
    goto loc_009BAB08;
loc_009BACE3:
    goto loc_009BAC99;
loc_009BACEA:
    if (v_stack_mC0 == v_stack_m116) goto loc_009BACFC;
    if (v_stack_mB8 != v_stack_m116) goto loc_009BAAC2;
loc_009BACFC:
    a2 = 0;
    result = memset(v_stack_mD0, a2, 0, v_stack_m108);
    v_stack_m80 = 16;
loc_009BAD25:
    goto loc_009BAA2D;
loc_009BAD2F:
    result = ExfTryToWakePushLock(v_rip + 6341498, a2, 0, v_stack_m108);
    goto loc_009BAC05;
loc_009BAD40:
    v_stack_mE0 = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    v_stack_mEE = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if (v_stack_mEF != 0) goto loc_009BAB6C;
    v_stack_mC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1000);
    v_stack_mB8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1008);
    goto loc_009BAB6C;
loc_009BAD72:
    if (((unsigned __int8)(v_stack_m116)) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_009BABE9;
    result = MmEnforceWorkingSetLimit(v_stack_mE8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))))), 0, v_stack_m108);
    goto loc_009BABE9;
loc_009BAD8C:
    v_r15 = 0;
    if ((unsigned __int8)(v_stack_m116) == 0) { v_r15 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)); }
    goto loc_009BAC47;
loc_009BAD9C:
    result = SePrivilegedServiceAuditAlarm(v_rip + 1642701, v_stack_m70, v_stack_m50, v_stack_m3B);
    goto loc_009BAC7A;
}
```

## 5. (Beta) C Style

```c
int64_t PspSetQuotaLimits(int64_t Arg1, void *Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint8_t v_stack_m114;
    uint8_t v_stack_m115;
    uint8_t v_stack_m116;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint8_t v_stack_m3B;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint8_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mEC;
    uint8_t v_stack_mEE;
    uint8_t v_stack_mEF;
    uint8_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x44FE77)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r12 = 0;
    v_stack_m110 = 0;
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, (uint32_t)((uint32_t)(local_r12 + 88)), Arg4);
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    v_stack_m115 = 0;
    result = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) != 48) goto loc_009BA987;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = 0;
    v_stack_m118 = (uint8_t)(result + 1);
loc_009BA985:
    goto loc_009BA9EA;
loc_009BA987:
    if (((uint32_t)((uint32_t)(Arg3))) != ((uint32_t)(local_r12 + 88))) goto loc_009BA9DB;
    v_stack_m118 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    goto loc_009BA985;
loc_009BA9DB:
    goto loc_009BAC99;
loc_009BA9EA:
    if ((((uint32_t)((uint32_t)(v_stack_mA8))) & (0xFFFFFFE0ULL)) != 0) goto loc_009BACE3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mA8)))) & (3));
    if (((uint8_t)(result)) == 3) goto loc_009BACE3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mA8)))) & (12));
    if (((uint8_t)(result)) == 12) goto loc_009BACE3;
    if (((1) & ((uint8_t)((uint32_t)(v_stack_mA8)))) != 0) goto loc_009BAD25;
    local_rdi = 0;
    if ((((uint8_t)((uint32_t)(v_stack_mA8))) & (2)) != 0) { local_rdi = 8; }
loc_009BAA2D:
    if ((((uint8_t)((uint32_t)(v_stack_mA8))) & (4)) != 0) goto loc_009BAB17;
    if (((8) & ((uint8_t)((uint32_t)(v_stack_mA8)))) != 0) {
        local_rdi = (uint32_t)((local_rdi) | (2));
    }
    result = ((uint32_t)(v_stack_mA4)) | (v_stack_mB0);
    result = (result) | (v_stack_mB8);
    result = (result) | (v_stack_mC0);
    if (condition_is_not_equal) goto loc_009BACE3;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_m110;
    v_stack_m138 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, 256, *(uint64_t *)(v_rip + 0x60C02F), Arg4);
    if (sign_flag) goto loc_009BAC99;
    if ((*(uint64_t *)(v_stack_m110 + 0x2F8)) == (v_rip + 4642000)) goto loc_009BACEA;
loc_009BAAC2:
    if (v_stack_mE8 == 0) goto loc_009BAC87;
    if (v_stack_mE0 == 0) goto loc_009BAC87;
    Arg2 = (256) | (-1);
    if (v_stack_mE8 == Arg2) goto loc_009BACC7;
loc_009BAAEB:
    v_stack_m117 = 0;
    result = PspSinglePrivCheck(v_stack_mE0, Arg2, Arg4, v_stack_m98);
    v_stack_m108 = (uint32_t)(result);
    v_stack_m114 = 1;
loc_009BAB08:
    v_stack_m100 = v_stack_m110;
    goto loc_009BAB21;
loc_009BAB17:
    local_rdi = (uint32_t)((local_rdi) | (1));
    goto loc_009BAA3D;
loc_009BAB1E:
    local_r12 = 0;
loc_009BAB21:
    v_stack_m116 = 0;
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_m110, Arg2, v_stack_m60, v_stack_m98);
    result = (result) | (-1);
    if (*(uint64_t *)(v_stack_m110 + 0x2A0) == 0) goto loc_009BABB9;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m110 + 0x2A0) + 56, 1, v_stack_m60, v_stack_m98);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110 + 0x2A0) + 0x420))))) != 0) goto loc_009BAD40;
loc_009BAB6C:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6341944, Arg2, Arg3, v_stack_m98);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6341917;
        Arg2 = result;
        Arg1 = v_rip + 6341907;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m98);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m110 + 0x2A0) + 56, Arg2, Arg3, v_stack_m98);
loc_009BABB9:
    v_stack_m130 = v_stack_m115;
    v_stack_m138 = (uint32_t)(local_rdi);
    Arg3 = 0;
    result = MmAdjustWorkingSetSizeEx(v_stack_mE8, v_stack_mE0, Arg3, v_stack_m108);
    if (sign_flag) goto loc_009BAD72;
loc_009BABE9:
    if (*(uint64_t *)(v_stack_m110 + 0x2A0) == 0) goto loc_009BAC11;
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009BAD2F;
loc_009BAC05:
    result = KeAbPostRelease(v_rip + 6341796, v_stack_mE0, Arg3, v_stack_m108);
loc_009BAC11:
    if (((uint8_t)(result)) != 2) goto loc_009BAC2E;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 6341796, v_stack_mE0, Arg3, v_stack_m108);
    }
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m60, Arg2, Arg3, v_stack_m108);
    if (v_stack_m115 == 1) goto loc_009BAD8C;
loc_009BAC47:
    if ((*(uint64_t *)(v_stack_m100 + 0x2A0)) != (*(uint64_t *)(v_stack_m110 + 0x2A0))) goto loc_009BAB1E;
    if (v_stack_m114 != 1) goto loc_009BAC87;
    if (v_stack_m64 == 0) goto loc_009BAC87;
    if (0 == 1) goto loc_009BAD9C;
loc_009BAC7A:
    result = SeReleaseSubjectContext(v_stack_m98, Arg2, Arg3, v_stack_m108);
loc_009BAC87:
    result = ObfDereferenceObjectWithTag(v_stack_m110, (uint32_t)(0x79517350ULL), Arg3, v_stack_m108);
loc_009BAC99:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x79517350ULL), Arg3, v_stack_m108);
    return result;
loc_009BACC7:
    if (Arg1 != ((uint32_t)(0x79517350ULL))) goto loc_009BAAEB;
    v_stack_mEF = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    v_stack_mE0 = (uint8_t)(v_stack_m116);
    v_stack_mEC = (uint8_t)(v_stack_m116);
    goto loc_009BAB08;
loc_009BACE3:
    goto loc_009BAC99;
loc_009BACEA:
    if (v_stack_mC0 == v_stack_m116) goto loc_009BACFC;
    if (v_stack_mB8 != v_stack_m116) goto loc_009BAAC2;
loc_009BACFC:
    Arg2 = 0;
    result = memset(v_stack_mD0, Arg2, 0, v_stack_m108);
    v_stack_m80 = 16;
loc_009BAD25:
    goto loc_009BAA2D;
loc_009BAD2F:
    result = ExfTryToWakePushLock(v_rip + 6341498, Arg2, 0, v_stack_m108);
    goto loc_009BAC05;
loc_009BAD40:
    v_stack_mE0 = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    v_stack_mEE = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    if (v_stack_mEF != 0) goto loc_009BAB6C;
    v_stack_mC0 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x3E8);
    v_stack_mB8 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x3F0);
    goto loc_009BAB6C;
loc_009BAD72:
    if (((uint8_t)(v_stack_m116)) != ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_009BABE9;
    result = MmEnforceWorkingSetLimit(v_stack_mE8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))))), 0, v_stack_m108);
    goto loc_009BABE9;
loc_009BAD8C:
    local_r15 = 0;
    if ((uint8_t)(v_stack_m116) == 0) { local_r15 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)); }
    goto loc_009BAC47;
loc_009BAD9C:
    result = SePrivilegedServiceAuditAlarm(v_rip + 1642701, v_stack_m70, v_stack_m50, v_stack_m3B);
    goto loc_009BAC7A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x20` | `128` | `R` |
| `Arg2` | `+ 0x30` | `128` | `R` |
| `Arg2` | `+ 0x40` | `128` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BA8A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
