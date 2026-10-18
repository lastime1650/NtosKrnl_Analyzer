# EtwpCovSampContextPruneModules

- RVA: `0x008DA03C`–`0x008DA5B1` (길이 `1,397` bytes)
- VA: `0x00000001408DA03C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00085724`
- 디코드: `351`개 명령, `1,397/1,397` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008DA093` → [PsGetCurrentThreadId](../../text/43/PsGetCurrentThreadId_function_00439680.md) (function, `0x00439680`)
- `0x008DA0ED` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008DA10D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008DA1A5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008DA20F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008DA228` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008DA4B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008DA4BC` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008DA510` → [EtwpCovSampModuleCleanup](../97/EtwpCovSampModuleCleanup_function_0097D91C.md) (function, `0x0097D91C`)
- `0x008DA51D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DA547` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008DA59B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)

### Direct callers
- [EtwpCovSampContextGetModule](EtwpCovSampContextGetModule_function_008D7FEC.md) at `0x008D8DF7`
- [EtwpCoverageSamplerQuery](../95/EtwpCoverageSamplerQuery_function_0095C4A0.md) at `0x0095D0BE`

### Static image references
- `0x008DA05F` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x008DA093` → [PsGetCurrentThreadId](../../text/43/PsGetCurrentThreadId_function_00439680.md) (`PAGE` → `.text`)
  - `0x008DA0ED` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008DA10D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008DA1A5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008DA20F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008DA228` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008DA4B7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008DA4BC` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008DA51D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DA547` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008DA59B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008DA592` → [sub_00B1C3CE](../B1/Unknown_function_00B1C3CE.md) (`tail-transfer`)
  - `0x008DA5A1` → [sub_00B1C3CE](../B1/Unknown_function_00B1C3CE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DA03C  48 8B C4                        mov rax, rsp
008DA03F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
008DA043  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
008DA047  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
008DA04B  55                              push rbp
008DA04C  41 54                           push r12
008DA04E  41 55                           push r13
008DA050  41 56                           push r14
008DA052  41 57                           push r15
008DA054  48 8D 68 A1                     lea rbp, [rax - 0x5f]
008DA058  48 81 EC F0 00 00 00            sub rsp, 0xf0
008DA05F  48 8B 05 DA 06 53 00            mov rax, qword ptr [rip + 0x5306da]
008DA066  48 33 C4                        xor rax, rsp
008DA069  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
008DA06D  48 8B F9                        mov rdi, rcx
008DA070  0F 57 C0                        xorps xmm0, xmm0
008DA073  8B 49 10                        mov ecx, dword ptr [rcx + 0x10]
008DA076  0F 57 C9                        xorps xmm1, xmm1
008DA079  D1 E9                           shr ecx, 1
008DA07B  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
008DA080  8B 87 DC 04 00 00               mov eax, dword ptr [rdi + 0x4dc]
008DA086  0F 11 4C 24 28                  movups xmmword ptr [rsp + 0x28], xmm1
008DA08B  3B C1                           cmp eax, ecx
008DA08D  0F 86 FF 00 00 00               jbe 0x1408da192
008DA093  E8 E8 F5 B5 FF                  call 0x140439680
008DA098  48 8B C8                        mov rcx, rax
008DA09B  33 C0                           xor eax, eax
008DA09D  F0 0F B1 8F 68 06 00 00         lock cmpxchg dword ptr [rdi + 0x668], ecx
008DA0A5  0F 85 F3 00 00 00               jne 0x1408da19e
008DA0AB  41 BF 08 00 00 00               mov r15d, 8
008DA0B1  48 8D 45 A7                     lea rax, [rbp - 0x59]
008DA0B5  41 8B CF                        mov ecx, r15d
008DA0B8  48 89 40 08                     mov qword ptr [rax + 8], rax
008DA0BC  48 89 00                        mov qword ptr [rax], rax
008DA0BF  48 83 C0 10                     add rax, 0x10
008DA0C3  48 83 E9 01                     sub rcx, 1
008DA0C7  75 EF                           jne 0x1408da0b8
008DA0C9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008DA0D2  4C 8D B7 98 04 00 00            lea r14, [rdi + 0x498]
008DA0D9  48 83 CB FF                     or rbx, 0xffffffffffffffff
008DA0DD  45 33 C0                        xor r8d, r8d
008DA0E0  33 D2                           xor edx, edx
008DA0E2  49 8B CE                        mov rcx, r14
008DA0E5  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
008DA0EC  90                              nop
008DA0ED  E8 3E 61 93 FF                  call 0x140210230
008DA0F2  4C 8B E8                        mov r13, rax
008DA0F5  44 8D 63 12                     lea r12d, [rbx + 0x12]
008DA0F9  33 C0                           xor eax, eax
008DA0FB  F0 4D 0F B1 26                  lock cmpxchg qword ptr [r14], r12
008DA100  74 10                           je 0x1408da112
008DA102  4D 8B CE                        mov r9, r14
008DA105  4D 8B C5                        mov r8, r13
008DA108  33 D2                           xor edx, edx
008DA10A  49 8B CE                        mov rcx, r14
008DA10D  E8 3A 63 93 FF                  call 0x14021044c
008DA112  33 F6                           xor esi, esi
008DA114  4D 85 ED                        test r13, r13
008DA117  74 05                           je 0x1408da11e
008DA119  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
008DA11E  4C 8D 8F C8 04 00 00            lea r9, [rdi + 0x4c8]
008DA125  49 8B 09                        mov rcx, qword ptr [r9]
008DA128  49 3B C9                        cmp rcx, r9
008DA12B  0F 84 59 04 00 00               je 0x1408da58a
008DA131  48 83 79 F8 01                  cmp qword ptr [rcx - 8], 1
008DA136  74 05                           je 0x1408da13d
008DA138  48 8B 09                        mov rcx, qword ptr [rcx]
008DA13B  EB EB                           jmp 0x1408da128
008DA13D  39 71 3C                        cmp dword ptr [rcx + 0x3c], esi
008DA140  75 F6                           jne 0x1408da138
008DA142  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
008DA14C  8B 00                           mov eax, dword ptr [rax]
008DA14E  2B 41 40                        sub eax, dword ptr [rcx + 0x40]
008DA151  3D 00 01 00 00                  cmp eax, 0x100
008DA156  73 2D                           jae 0x1408da185
008DA158  C1 E8 06                        shr eax, 6
008DA15B  41 3B C7                        cmp eax, r15d
008DA15E  4C 8D 45 A7                     lea r8, [rbp - 0x59]
008DA162  BA 07 00 00 00                  mov edx, 7
008DA167  0F 43 C2                        cmovae eax, edx
008DA16A  48 8D 51 10                     lea rdx, [rcx + 0x10]
008DA16E  48 C1 E0 04                     shl rax, 4
008DA172  4C 03 C0                        add r8, rax
008DA175  4D 8B 50 08                     mov r10, qword ptr [r8 + 8]
008DA179  4D 39 02                        cmp qword ptr [r10], r8
008DA17C  74 4E                           je 0x1408da1cc
008DA17E  B9 03 00 00 00                  mov ecx, 3
008DA183  CD 29                           int 0x29
008DA185  05 00 FF FF FF                  add eax, 0xffffff00
008DA18A  C1 E8 08                        shr eax, 8
008DA18D  83 C0 04                        add eax, 4
008DA190  EB C9                           jmp 0x1408da15b
008DA192  39 8F 64 06 00 00               cmp dword ptr [rdi + 0x664], ecx
008DA198  0F 8F F5 FE FF FF               jg 0x1408da093
008DA19E  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
008DA1A2  48 33 CC                        xor rcx, rsp
008DA1A5  E8 96 24 DD FF                  call 0x1406ac640
008DA1AA  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
008DA1B2  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008DA1B6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
008DA1BA  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008DA1BE  49 8B E3                        mov rsp, r11
008DA1C1  41 5F                           pop r15
008DA1C3  41 5E                           pop r14
008DA1C5  41 5D                           pop r13
008DA1C7  41 5C                           pop r12
008DA1C9  5D                              pop rbp
008DA1CA  C3                              ret
008DA1CB  CC                              int3
008DA1CC  4C 89 02                        mov qword ptr [rdx], r8
008DA1CF  4C 89 52 08                     mov qword ptr [rdx + 8], r10
008DA1D3  49 89 12                        mov qword ptr [r10], rdx
008DA1D6  49 89 50 08                     mov qword ptr [r8 + 8], rdx
008DA1DA  E9 59 FF FF FF                  jmp 0x1408da138
008DA1DF  48 8D 44 24 28                  lea rax, [rsp + 0x28]
008DA1E4  45 33 C0                        xor r8d, r8d
008DA1E7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008DA1EC  33 D2                           xor edx, edx
008DA1EE  48 8D 44 24 28                  lea rax, [rsp + 0x28]
008DA1F3  49 8B CE                        mov rcx, r14
008DA1F6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DA1FB  4C 8B EE                        mov r13, rsi
008DA1FE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008DA207  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
008DA20E  90                              nop
008DA20F  E8 1C 60 93 FF                  call 0x140210230
008DA214  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
008DA21A  4C 8B F8                        mov r15, rax
008DA21D  73 0E                           jae 0x1408da22d
008DA21F  4D 8B C6                        mov r8, r14
008DA222  48 8B D0                        mov rdx, rax
008DA225  49 8B CE                        mov rcx, r14
008DA228  E8 63 5A 93 FF                  call 0x14020fc90
008DA22D  4D 85 FF                        test r15, r15
008DA230  74 05                           je 0x1408da237
008DA232  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008DA237  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008DA240  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
008DA245  48 89 87 A0 04 00 00            mov qword ptr [rdi + 0x4a0], rax
008DA24C  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008DA251  4C 3B D8                        cmp r11, rax
008DA254  0F 84 36 02 00 00               je 0x1408da490
008DA25A  49 8B C3                        mov rax, r11
008DA25D  4D 8D 53 A8                     lea r10, [r11 - 0x58]
008DA261  4D 8B 1B                        mov r11, qword ptr [r11]
008DA264  48 89 40 08                     mov qword ptr [rax + 8], rax
008DA268  48 89 00                        mov qword ptr [rax], rax
008DA26B  49 83 7A 40 01                  cmp qword ptr [r10 + 0x40], 1
008DA270  75 DA                           jne 0x1408da24c
008DA272  41 39 B2 84 00 00 00            cmp dword ptr [r10 + 0x84], esi
008DA279  75 D1                           jne 0x1408da24c
008DA27B  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008DA27E  49 FF C5                        inc r13
008DA281  4C 3B E8                        cmp r13, rax
008DA284  76 C6                           jbe 0x1408da24c
008DA286  41 F7 42 78 00 00 04 00         test dword ptr [r10 + 0x78], 0x40000
008DA28E  0F 85 CC 00 00 00               jne 0x1408da360
008DA294  44 8B 8F AC 04 00 00            mov r9d, dword ptr [rdi + 0x4ac]
008DA29B  48 8B C3                        mov rax, rbx
008DA29E  41 8B C9                        mov ecx, r9d
008DA2A1  41 C1 E9 05                     shr r9d, 5
008DA2A5  83 E1 1F                        and ecx, 0x1f
008DA2A8  48 D3 E0                        shl rax, cl
008DA2AB  49 23 42 08                     and rax, qword ptr [r10 + 8]
008DA2AF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DA2B4  0F B6 C0                        movzx eax, al
008DA2B7  48 05 CB 5D B1 00               add rax, 0xb15dcb
008DA2BD  48 6B C8 25                     imul rcx, rax, 0x25
008DA2C1  0F B6 44 24 21                  movzx eax, byte ptr [rsp + 0x21]
008DA2C6  48 03 C8                        add rcx, rax
008DA2C9  0F B6 44 24 22                  movzx eax, byte ptr [rsp + 0x22]
008DA2CE  48 6B D1 25                     imul rdx, rcx, 0x25
008DA2D2  48 03 D0                        add rdx, rax
008DA2D5  0F B6 44 24 23                  movzx eax, byte ptr [rsp + 0x23]
008DA2DA  48 6B CA 25                     imul rcx, rdx, 0x25
008DA2DE  48 03 C8                        add rcx, rax
008DA2E1  0F B6 44 24 24                  movzx eax, byte ptr [rsp + 0x24]
008DA2E6  48 6B D1 25                     imul rdx, rcx, 0x25
008DA2EA  48 03 D0                        add rdx, rax
008DA2ED  0F B6 44 24 25                  movzx eax, byte ptr [rsp + 0x25]
008DA2F2  48 6B CA 25                     imul rcx, rdx, 0x25
008DA2F6  48 03 C8                        add rcx, rax
008DA2F9  0F B6 44 24 26                  movzx eax, byte ptr [rsp + 0x26]
008DA2FE  48 6B D1 25                     imul rdx, rcx, 0x25
008DA302  41 8D 49 FF                     lea ecx, [r9 - 1]
008DA306  48 03 D0                        add rdx, rax
008DA309  0F B6 44 24 27                  movzx eax, byte ptr [rsp + 0x27]
008DA30E  4C 6B C2 25                     imul r8, rdx, 0x25
008DA312  49 03 C0                        add rax, r8
008DA315  8B C0                           mov eax, eax
008DA317  48 23 C8                        and rcx, rax
008DA31A  48 8B 87 B0 04 00 00            mov rax, qword ptr [rdi + 0x4b0]
008DA321  48 8D 14 C8                     lea rdx, [rax + rcx*8]
008DA325  49 8B 02                        mov rax, qword ptr [r10]
008DA328  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
008DA332  48 23 C1                        and rax, rcx
008DA335  48 3B C1                        cmp rax, rcx
008DA338  75 03                           jne 0x1408da33d
008DA33A  48 8B 06                        mov rax, qword ptr [rsi]
008DA33D  48 8B 02                        mov rax, qword ptr [rdx]
008DA340  A8 01                           test al, 1
008DA342  0F 85 DC 01 00 00               jne 0x1408da524
008DA348  49 3B C2                        cmp rax, r10
008DA34B  0F 85 DB 01 00 00               jne 0x1408da52c
008DA351  49 8B 02                        mov rax, qword ptr [r10]
008DA354  48 89 02                        mov qword ptr [rdx], rax
008DA357  FF 8F A8 04 00 00               dec dword ptr [rdi + 0x4a8]
008DA35D  49 89 32                        mov qword ptr [r10], rsi
008DA360  4D 8D 7A 10                     lea r15, [r10 + 0x10]
008DA364  4D 8B 27                        mov r12, qword ptr [r15]
008DA367  4D 85 E4                        test r12, r12
008DA36A  0F 84 C9 00 00 00               je 0x1408da439
008DA370  44 8B 8F BC 04 00 00            mov r9d, dword ptr [rdi + 0x4bc]
008DA377  48 8B C3                        mov rax, rbx
008DA37A  41 8B C9                        mov ecx, r9d
008DA37D  41 C1 E9 05                     shr r9d, 5
008DA381  83 E1 1F                        and ecx, 0x1f
008DA384  48 D3 E0                        shl rax, cl
008DA387  49 23 47 08                     and rax, qword ptr [r15 + 8]
008DA38B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DA390  0F B6 C0                        movzx eax, al
008DA393  48 05 CB 5D B1 00               add rax, 0xb15dcb
008DA399  48 6B C8 25                     imul rcx, rax, 0x25
008DA39D  0F B6 44 24 21                  movzx eax, byte ptr [rsp + 0x21]
008DA3A2  48 03 C8                        add rcx, rax
008DA3A5  0F B6 44 24 22                  movzx eax, byte ptr [rsp + 0x22]
008DA3AA  48 6B D1 25                     imul rdx, rcx, 0x25
008DA3AE  48 03 D0                        add rdx, rax
008DA3B1  0F B6 44 24 23                  movzx eax, byte ptr [rsp + 0x23]
008DA3B6  48 6B CA 25                     imul rcx, rdx, 0x25
008DA3BA  48 03 C8                        add rcx, rax
008DA3BD  0F B6 44 24 24                  movzx eax, byte ptr [rsp + 0x24]
008DA3C2  48 6B D1 25                     imul rdx, rcx, 0x25
008DA3C6  48 03 D0                        add rdx, rax
008DA3C9  0F B6 44 24 25                  movzx eax, byte ptr [rsp + 0x25]
008DA3CE  48 6B CA 25                     imul rcx, rdx, 0x25
008DA3D2  48 03 C8                        add rcx, rax
008DA3D5  0F B6 44 24 26                  movzx eax, byte ptr [rsp + 0x26]
008DA3DA  48 6B D1 25                     imul rdx, rcx, 0x25
008DA3DE  41 8D 49 FF                     lea ecx, [r9 - 1]
008DA3E2  48 03 D0                        add rdx, rax
008DA3E5  0F B6 44 24 27                  movzx eax, byte ptr [rsp + 0x27]
008DA3EA  4C 6B C2 25                     imul r8, rdx, 0x25
008DA3EE  49 03 C0                        add rax, r8
008DA3F1  8B C0                           mov eax, eax
008DA3F3  48 23 C8                        and rcx, rax
008DA3F6  48 8B 87 C0 04 00 00            mov rax, qword ptr [rdi + 0x4c0]
008DA3FD  48 8D 14 C8                     lea rdx, [rax + rcx*8]
008DA401  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
008DA40B  4C 23 E1                        and r12, rcx
008DA40E  4C 3B E1                        cmp r12, rcx
008DA411  75 03                           jne 0x1408da416
008DA413  48 8B 06                        mov rax, qword ptr [rsi]
008DA416  48 8B 02                        mov rax, qword ptr [rdx]
008DA419  A8 01                           test al, 1
008DA41B  0F 85 1B 01 00 00               jne 0x1408da53c
008DA421  49 3B C7                        cmp rax, r15
008DA424  0F 85 0A 01 00 00               jne 0x1408da534
008DA42A  49 8B 07                        mov rax, qword ptr [r15]
008DA42D  48 89 02                        mov qword ptr [rdx], rax
008DA430  FF 8F B8 04 00 00               dec dword ptr [rdi + 0x4b8]
008DA436  49 89 37                        mov qword ptr [r15], rsi
008DA439  49 8D 42 48                     lea rax, [r10 + 0x48]
008DA43D  48 8B 10                        mov rdx, qword ptr [rax]
008DA440  48 39 42 08                     cmp qword ptr [rdx + 8], rax
008DA444  0F 85 34 FD FF FF               jne 0x1408da17e
008DA44A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008DA44E  48 39 01                        cmp qword ptr [rcx], rax
008DA451  0F 85 27 FD FF FF               jne 0x1408da17e
008DA457  48 89 11                        mov qword ptr [rcx], rdx
008DA45A  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
008DA45E  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
008DA463  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
008DA468  FF 8F D8 04 00 00               dec dword ptr [rdi + 0x4d8]
008DA46E  48 39 11                        cmp qword ptr [rcx], rdx
008DA471  0F 85 07 FD FF FF               jne 0x1408da17e
008DA477  48 89 48 08                     mov qword ptr [rax + 8], rcx
008DA47B  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
008DA480  48 89 10                        mov qword ptr [rax], rdx
008DA483  48 89 01                        mov qword ptr [rcx], rax
008DA486  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008DA48B  E9 BC FD FF FF                  jmp 0x1408da24c
008DA490  89 B7 DC 04 00 00               mov dword ptr [rdi + 0x4dc], esi
008DA496  89 B7 64 06 00 00               mov dword ptr [rdi + 0x664], esi
008DA49C  48 89 B7 A0 04 00 00            mov qword ptr [rdi + 0x4a0], rsi
008DA4A3  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
008DA4A8  80 E3 06                        and bl, 6
008DA4AB  80 FB 02                        cmp bl, 2
008DA4AE  0F 84 90 00 00 00               je 0x1408da544
008DA4B4  49 8B CE                        mov rcx, r14
008DA4B7  E8 44 71 A0 FF                  call 0x1402e1600
008DA4BC  E8 EF 33 98 FF                  call 0x14025d8b0
008DA4C1  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
008DA4C6  48 8D 4C 24 28                  lea rcx, [rsp + 0x28]
008DA4CB  48 3B C1                        cmp rax, rcx
008DA4CE  0F 84 D2 00 00 00               je 0x1408da5a6
008DA4D4  48 8D 4C 24 28                  lea rcx, [rsp + 0x28]
008DA4D9  48 39 48 08                     cmp qword ptr [rax + 8], rcx
008DA4DD  0F 85 9B FC FF FF               jne 0x1408da17e
008DA4E3  48 8B 08                        mov rcx, qword ptr [rax]
008DA4E6  48 39 41 08                     cmp qword ptr [rcx + 8], rax
008DA4EA  0F 85 8E FC FF FF               jne 0x1408da17e
008DA4F0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008DA4F5  48 8D 58 B8                     lea rbx, [rax - 0x48]
008DA4F9  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
008DA4FE  48 89 51 08                     mov qword ptr [rcx + 8], rdx
008DA502  48 8B CB                        mov rcx, rbx
008DA505  48 89 73 40                     mov qword ptr [rbx + 0x40], rsi
008DA509  48 89 40 08                     mov qword ptr [rax + 8], rax
008DA50D  48 89 00                        mov qword ptr [rax], rax
008DA510  E8 07 34 0A 00                  call 0x14097d91c
008DA515  BA 45 74 77 56                  mov edx, 0x56777445
008DA51A  48 8B CB                        mov rcx, rbx
008DA51D  E8 4E 83 2A 00                  call 0x140b82870
008DA522  EB 9D                           jmp 0x1408da4c1
008DA524  48 8B 06                        mov rax, qword ptr [rsi]
008DA527  E9 31 FE FF FF                  jmp 0x1408da35d
008DA52C  48 8B D0                        mov rdx, rax
008DA52F  E9 09 FE FF FF                  jmp 0x1408da33d
008DA534  48 8B D0                        mov rdx, rax
008DA537  E9 DA FE FF FF                  jmp 0x1408da416
008DA53C  48 8B 06                        mov rax, qword ptr [rsi]
008DA53F  E9 F2 FE FF FF                  jmp 0x1408da436
008DA544  49 8B CE                        mov rcx, r14
008DA547  E8 84 B8 98 FF                  call 0x140265dd0
008DA54C  E9 63 FF FF FF                  jmp 0x1408da4b4
008DA551  48 8B 0A                        mov rcx, qword ptr [rdx]
008DA554  48 3B CA                        cmp rcx, rdx
008DA557  74 22                           je 0x1408da57b
008DA559  48 89 08                        mov qword ptr [rax], rcx
008DA55C  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
008DA560  48 8B 0A                        mov rcx, qword ptr [rdx]
008DA563  48 89 41 08                     mov qword ptr [rcx + 8], rax
008DA567  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
008DA56C  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
008DA570  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
008DA574  48 89 08                        mov qword ptr [rax], rcx
008DA577  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
008DA57B  48 83 C2 10                     add rdx, 0x10
008DA57F  49 83 EF 01                     sub r15, 1
008DA583  75 CC                           jne 0x1408da551
008DA585  E9 55 FC FF FF                  jmp 0x1408da1df
008DA58A  49 8B C4                        mov rax, r12
008DA58D  F0 49 0F B1 36                  lock cmpxchg qword ptr [r14], rsi
008DA592  0F 84 36 1E 24 00               je 0x140b1c3ce
008DA598  49 8B CE                        mov rcx, r14
008DA59B  E8 A0 8E 98 FF                  call 0x140263440
008DA5A0  90                              nop
008DA5A1  E9 28 1E 24 00                  jmp 0x140b1c3ce
008DA5A6  87 B7 68 06 00 00               xchg dword ptr [rdi + 0x668], esi
008DA5AC  E9 ED FB FF FF                  jmp 0x1408da19e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCovSampContextPruneModules(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_mC9;
    unsigned __int8 v_stack_mCA;
    unsigned __int8 v_stack_mCB;
    unsigned __int8 v_stack_mCC;
    unsigned __int8 v_stack_mCD;
    unsigned __int8 v_stack_mCE;
    unsigned __int8 v_stack_mCF;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 5441242)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) >> (1));
    v_stack_mE0 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1244)))) <= ((unsigned int)(a1))) goto loc_008DA192;
loc_008DA093:
    result = PsGetCurrentThreadId(a1, a2, a3, a4);
    result = 0;
    if (condition_is_not_equal) goto loc_008DA19E;
loc_008DA0B8:
    *(unsigned __int64 *)(v_rsp - 95 - 89 + 8) = v_rsp - 95 - 89;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = v_rsp - 95 - 89;
    result = (v_rsp - 95 - 89) + (16);
    a1 = (8) - (1);
    if (condition_is_not_equal) goto loc_008DA0B8;
    v_rbx = (v_rbx) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1176, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 1176;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 1176;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_008DA128:
    if ((*(unsigned __int64 *)(a1 + 1224)) == (a1 + 1224)) goto loc_008DA58A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224) - 8)) == 1) goto loc_008DA13D;
loc_008DA138:
    goto loc_008DA128;
loc_008DA13D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 60)) != 0) goto loc_008DA138;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 64)));
    if (((unsigned int)(result)) >= 256) goto loc_008DA185;
    result = (unsigned int)((result) >> (6));
loc_008DA15B:
    if (((unsigned int)(result)) >= 8) { result = 7; }
    result = (result) << (4);
    a3 = (v_rsp - 95 - 89) + (result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8))) == a3) goto loc_008DA1CC;
loc_008DA17E:
loc_008DA185:
    result = (unsigned int)((result) + (0xFFFFFF00ULL));
    result = (unsigned int)((result) >> (8));
    result = (unsigned int)((result) + (4));
    goto loc_008DA15B;
loc_008DA192:
    if ((*(unsigned int *)(a1 + 1636)) > 3) goto loc_008DA093;
loc_008DA19E:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16, a3, a1 + 1224);
    return result;
loc_008DA1CC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16) = a3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16 + 8) = *(unsigned __int64 *)(a3 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16;
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16;
    goto loc_008DA138;
loc_008DA58A:
    result = ExfReleasePushLockShared(a1 + 1176, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224)) + 16, a3, a1 + 1224);
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCovSampContextPruneModules(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_mC9;
    uint8_t v_stack_mCA;
    uint8_t v_stack_mCB;
    uint8_t v_stack_mCC;
    uint8_t v_stack_mCD;
    uint8_t v_stack_mCE;
    uint8_t v_stack_mCF;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x5306DA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) >> (1));
    v_stack_mE0 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4DC)))) <= ((uint32_t)(Arg1))) goto loc_008DA192;
loc_008DA093:
    result = PsGetCurrentThreadId(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (condition_is_not_equal) goto loc_008DA19E;
loc_008DA0B8:
    *(uint64_t *)(local_rsp - 0x5F - 0x59 + 0x8) = local_rsp - 95 - 89;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = local_rsp - 95 - 89;
    result = (local_rsp - 95 - 89) + (16);
    Arg1 = (8) - (1);
    if (condition_is_not_equal) goto loc_008DA0B8;
    local_rbx = (local_rbx) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1176, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 1176;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 1176;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    local_rsi = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_008DA128:
    if ((*(uint64_t *)(arg1 + 0x4C8)) == (Arg1 + 1224)) goto loc_008DA58A;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8) - 0x8)) == 1) goto loc_008DA13D;
loc_008DA138:
    goto loc_008DA128;
loc_008DA13D:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 0x3C)) != 0) goto loc_008DA138;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 0x40)));
    if (((uint32_t)(result)) >= 256) goto loc_008DA185;
    result = (uint32_t)((result) >> (6));
loc_008DA15B:
    if (((uint32_t)(result)) >= 8) { result = 7; }
    result = (result) << (4);
    Arg3 = (local_rsp - 95 - 89) + (result);
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0x8))) == Arg3) goto loc_008DA1CC;
loc_008DA17E:
loc_008DA185:
    result = (uint32_t)((result) + (0xFFFFFF00ULL));
    result = (uint32_t)((result) >> (8));
    result = (uint32_t)((result) + (4));
    goto loc_008DA15B;
loc_008DA192:
    if ((*(uint32_t *)(arg1 + 0x664)) > 3) goto loc_008DA093;
loc_008DA19E:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 16, Arg3, Arg1 + 1224);
    return result;
loc_008DA1CC:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 0x10) = Arg3;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 0x10 + 0x8) = *(uint64_t *)(Arg3 + 0x8);
    *(uint64_t *)(*(uint64_t *)(Arg3 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 16;
    *(uint64_t *)(Arg3 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 16;
    goto loc_008DA138;
loc_008DA58A:
    result = ExfReleasePushLockShared(Arg1 + 1176, *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8)) + 16, Arg3, Arg1 + 1224);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R` |
| `Arg1` | `+ 0x4C8` | `64` | `R` |
| `Arg1` | `+ 0x4DC` | `32` | `R` |
| `Arg1` | `+ 0x664` | `32` | `R` |
| `Arg1` | `+ 0x668` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DA03C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
