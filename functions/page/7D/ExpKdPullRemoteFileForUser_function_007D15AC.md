# ExpKdPullRemoteFileForUser

- RVA: `0x007D15AC`–`0x007D1AB2` (길이 `1,286` bytes)
- VA: `0x00000001407D15AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D58A0`
- 디코드: `333`개 명령, `1,286/1,286` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x007D1610` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007D1675` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D16A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007D16B4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D16EF` → [RtlDowncaseUnicodeString](../9C/RtlDowncaseUnicodeString_function_009C4190.md) (function, `0x009C4190`)
- `0x007D1706` → [KeComputeSha256](../../text/4A/KeComputeSha256_function_004A7370.md) (function, `0x004A7370`)
- `0x007D1712` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D1749` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007D176C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007D17B1` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007D17EE` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007D17F6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007D17FB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007D1812` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D1838` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007D1852` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007D189E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D18DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007D18ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D192D` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007D1969` → [KdPullRemoteFile](../../pagekd/B8/KdPullRemoteFile_function_00B86618.md) (function, `0x00B86618`)
- `0x007D1989` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x007D19EF` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007D1A25` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007D1A54` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007D1A5C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007D1A61` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007D1A74` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D1A8F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00B3F842](../B3/Unknown_function_00B3F842.md) at `0x00B3FAFF`

### Static image references
- `0x007D15C6` → RVA `0x00E0A740` (`.data`; read)
- `0x007D171B` → RVA `0x00EFED78` (`.data`; read)
- `0x007D1722` → RVA `0x00EFED98` (`.data`; read)
- `0x007D18F2` → RVA `0x00EFED98` (`.data`; write)
- `0x007D197C` → RVA `0x00B08B40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D198E` → RVA `0x00EFA270` (`.data`; read)
- `0x007D1A40` → RVA `0x00EFED78` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x007D1675` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D16A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007D16B4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D1706` → [KeComputeSha256](../../text/4A/KeComputeSha256_function_004A7370.md) (`PAGE` → `.text`)
  - `0x007D1712` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D1749` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007D176C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007D17B1` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007D17EE` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007D17F6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007D17FB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007D1812` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D1838` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007D1852` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007D189E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D18DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007D18ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D192D` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007D1969` → [KdPullRemoteFile](../../pagekd/B8/KdPullRemoteFile_function_00B86618.md) (`PAGE` → `PAGEKD`)
  - `0x007D1989` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
  - `0x007D19EF` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007D1A25` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007D1A54` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007D1A5C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007D1A61` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007D1A74` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D1A8F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D15AC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
007D15B1  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
007D15B6  57                              push rdi
007D15B7  41 54                           push r12
007D15B9  41 55                           push r13
007D15BB  41 56                           push r14
007D15BD  41 57                           push r15
007D15BF  48 81 EC B0 00 00 00            sub rsp, 0xb0
007D15C6  48 8B 05 73 91 63 00            mov rax, qword ptr [rip + 0x639173]
007D15CD  48 33 C4                        xor rax, rsp
007D15D0  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
007D15D8  45 33 FF                        xor r15d, r15d
007D15DB  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
007D15E0  44 89 7C 24 5C                  mov dword ptr [rsp + 0x5c], r15d
007D15E5  0F 57 C0                        xorps xmm0, xmm0
007D15E8  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
007D15ED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D15F6  8A 90 32 02 00 00               mov dl, byte ptr [rax + 0x232]
007D15FC  0F 10 01                        movups xmm0, xmmword ptr [rcx]
007D15FF  F3 0F 7F 44 24 48               movdqu xmmword ptr [rsp + 0x48], xmm0
007D1605  80 FA 01                        cmp dl, 1
007D1608  75 2A                           jne 0x1407d1634
007D160A  84 54 24 50                     test byte ptr [rsp + 0x50], dl
007D160E  74 05                           je 0x1407d1615
007D1610  E8 BB 89 0C 00                  call 0x140899fd0
007D1615  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
007D161A  48 8D 48 02                     lea rcx, [rax + 2]
007D161E  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
007D1628  48 3B CA                        cmp rcx, rdx
007D162B  77 05                           ja 0x1407d1632
007D162D  48 3B C8                        cmp rcx, rax
007D1630  73 02                           jae 0x1407d1634
007D1632  8A 02                           mov al, byte ptr [rdx]
007D1634  0F B7 5C 24 48                  movzx ebx, word ptr [rsp + 0x48]
007D1639  66 85 DB                        test bx, bx
007D163C  0F 84 3B 04 00 00               je 0x1407d1a7d
007D1642  F6 C3 01                        test bl, 1
007D1645  0F 85 32 04 00 00               jne 0x1407d1a7d
007D164B  F6 44 24 4A 01                  test byte ptr [rsp + 0x4a], 1
007D1650  0F 85 27 04 00 00               jne 0x1407d1a7d
007D1656  66 39 5C 24 4A                  cmp word ptr [rsp + 0x4a], bx
007D165B  0F 82 1C 04 00 00               jb 0x1407d1a7d
007D1661  BE 55 4B 64 46                  mov esi, 0x46644b55
007D1666  44 8B C6                        mov r8d, esi
007D1669  48 8B D3                        mov rdx, rbx
007D166C  41 BE 40 00 00 00               mov r14d, 0x40
007D1672  41 8B CE                        mov ecx, r14d
007D1675  E8 76 0A 3B 00                  call 0x140b820f0
007D167A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007D167F  48 85 C0                        test rax, rax
007D1682  75 0A                           jne 0x1407d168e
007D1684  B8 9A 00 00 C0                  mov eax, 0xc000009a
007D1689  E9 F6 03 00 00                  jmp 0x1407d1a84
007D168E  66 89 5C 24 38                  mov word ptr [rsp + 0x38], bx
007D1693  66 89 5C 24 3A                  mov word ptr [rsp + 0x3a], bx
007D1698  4C 8B C3                        mov r8, rbx
007D169B  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
007D16A0  48 8B C8                        mov rcx, rax
007D16A3  E8 98 51 EF FF                  call 0x1406c6840
007D16A8  90                              nop
007D16A9  0F B7 54 24 38                  movzx edx, word ptr [rsp + 0x38]
007D16AE  44 8B C6                        mov r8d, esi
007D16B1  49 8B CE                        mov rcx, r14
007D16B4  E8 37 0A 3B 00                  call 0x140b820f0
007D16B9  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007D16BE  48 85 C0                        test rax, rax
007D16C1  75 0B                           jne 0x1407d16ce
007D16C3  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
007D16C9  E9 3D 01 00 00                  jmp 0x1407d180b
007D16CE  0F B7 44 24 38                  movzx eax, word ptr [rsp + 0x38]
007D16D3  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
007D16D8  0F B7 44 24 3A                  movzx eax, word ptr [rsp + 0x3a]
007D16DD  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
007D16E2  45 33 C0                        xor r8d, r8d
007D16E5  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007D16EA  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007D16EF  E8 9C 2A 1F 00                  call 0x1409c4190
007D16F4  0F B7 54 24 58                  movzx edx, word ptr [rsp + 0x58]
007D16F9  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
007D1701  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D1706  E8 65 5C CD FF                  call 0x1404a7370
007D170B  33 D2                           xor edx, edx
007D170D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D1712  E8 59 11 3B 00                  call 0x140b82870
007D1717  48 83 CB FF                     or rbx, 0xffffffffffffffff
007D171B  4C 8D 25 56 D6 72 00            lea r12, [rip + 0x72d656]
007D1722  48 83 3D 6E D6 72 00 00         cmp qword ptr [rip + 0x72d66e], 0
007D172A  0F 84 EF 00 00 00               je 0x1407d181f
007D1730  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D1739  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007D1740  90                              nop
007D1741  45 33 C0                        xor r8d, r8d
007D1744  33 D2                           xor edx, edx
007D1746  49 8B CC                        mov rcx, r12
007D1749  E8 E2 EA A3 FF                  call 0x140210230
007D174E  48 8B F8                        mov rdi, rax
007D1751  8D 4B 12                        lea ecx, [rbx + 0x12]
007D1754  33 C0                           xor eax, eax
007D1756  F0 48 0F B1 0D 19 D6 72 00      lock cmpxchg qword ptr [rip + 0x72d619], rcx
007D175F  74 10                           je 0x1407d1771
007D1761  4D 8B CC                        mov r9, r12
007D1764  4C 8B C7                        mov r8, rdi
007D1767  33 D2                           xor edx, edx
007D1769  49 8B CC                        mov rcx, r12
007D176C  E8 DB EC A3 FF                  call 0x14021044c
007D1771  48 85 FF                        test rdi, rdi
007D1774  74 04                           je 0x1407d177a
007D1776  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
007D177A  45 8B EF                        mov r13d, r15d
007D177D  4C 8B 35 14 D6 72 00            mov r14, qword ptr [rip + 0x72d614]
007D1784  4D 85 F6                        test r14, r14
007D1787  74 52                           je 0x1407d17db
007D1789  41 8B 3E                        mov edi, dword ptr [r14]
007D178C  FF CF                           dec edi
007D178E  41 3B FF                        cmp edi, r15d
007D1791  7C 45                           jl 0x1407d17d8
007D1793  41 8D 34 3F                     lea esi, [r15 + rdi]
007D1797  D1 FE                           sar esi, 1
007D1799  48 63 C6                        movsxd rax, esi
007D179C  48 FF C0                        inc rax
007D179F  49 8D 14 C6                     lea rdx, [r14 + rax*8]
007D17A3  41 B8 08 00 00 00               mov r8d, 8
007D17A9  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007D17B1  E8 5A 53 EF FF                  call 0x1406c6b10
007D17B6  85 C0                           test eax, eax
007D17B8  79 09                           jns 0x1407d17c3
007D17BA  85 F6                           test esi, esi
007D17BC  74 1A                           je 0x1407d17d8
007D17BE  8D 7E FF                        lea edi, [rsi - 1]
007D17C1  EB CB                           jmp 0x1407d178e
007D17C3  45 33 FF                        xor r15d, r15d
007D17C6  85 C0                           test eax, eax
007D17C8  7E 06                           jle 0x1407d17d0
007D17CA  44 8D 7E 01                     lea r15d, [rsi + 1]
007D17CE  EB BE                           jmp 0x1407d178e
007D17D0  41 BD 01 00 00 00               mov r13d, 1
007D17D6  EB 03                           jmp 0x1407d17db
007D17D8  45 33 FF                        xor r15d, r15d
007D17DB  B8 11 00 00 00                  mov eax, 0x11
007D17E0  F0 4C 0F B1 3D 8F D5 72 00      lock cmpxchg qword ptr [rip + 0x72d58f], r15
007D17E9  74 08                           je 0x1407d17f3
007D17EB  49 8B CC                        mov rcx, r12
007D17EE  E8 4D 1C A9 FF                  call 0x140263440
007D17F3  49 8B CC                        mov rcx, r12
007D17F6  E8 05 FE B0 FF                  call 0x1402e1600
007D17FB  E8 B0 C0 A8 FF                  call 0x14025d8b0
007D1800  45 85 ED                        test r13d, r13d
007D1803  74 1A                           je 0x1407d181f
007D1805  41 BE FF 00 00 00               mov r14d, 0xff
007D180B  33 D2                           xor edx, edx
007D180D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007D1812  E8 59 10 3B 00                  call 0x140b82870
007D1817  41 8B C6                        mov eax, r14d
007D181A  E9 65 02 00 00                  jmp 0x1407d1a84
007D181F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D1828  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007D182F  90                              nop
007D1830  45 33 C0                        xor r8d, r8d
007D1833  33 D2                           xor edx, edx
007D1835  49 8B CC                        mov rcx, r12
007D1838  E8 F3 E9 A3 FF                  call 0x140210230
007D183D  48 8B F8                        mov rdi, rax
007D1840  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
007D1847  73 0E                           jae 0x1407d1857
007D1849  4D 8B C4                        mov r8, r12
007D184C  48 8B D0                        mov rdx, rax
007D184F  49 8B CC                        mov rcx, r12
007D1852  E8 39 E4 A3 FF                  call 0x14020fc90
007D1857  48 85 FF                        test rdi, rdi
007D185A  74 04                           je 0x1407d1860
007D185C  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
007D1860  48 8B F3                        mov rsi, rbx
007D1863  48 8B 05 2E D5 72 00            mov rax, qword ptr [rip + 0x72d52e]
007D186A  48 85 C0                        test rax, rax
007D186D  75 07                           jne 0x1407d1876
007D186F  BA 10 40 00 00                  mov edx, 0x4010
007D1874  EB 1D                           jmp 0x1407d1893
007D1876  8B 08                           mov ecx, dword ptr [rax]
007D1878  81 F9 FF FF FF 1F               cmp ecx, 0x1fffffff
007D187E  0F 8D B6 01 00 00               jge 0x1407d1a3a
007D1884  48 63 50 04                     movsxd rdx, dword ptr [rax + 4]
007D1888  3B CA                           cmp ecx, edx
007D188A  75 1A                           jne 0x1407d18a6
007D188C  48 FF C2                        inc rdx
007D188F  48 C1 E2 04                     shl rdx, 4
007D1893  41 B8 55 4B 64 66               mov r8d, 0x66644b55
007D1899  B9 00 01 00 00                  mov ecx, 0x100
007D189E  E8 4D 08 3B 00                  call 0x140b820f0
007D18A3  48 8B F0                        mov rsi, rax
007D18A6  48 85 F6                        test rsi, rsi
007D18A9  0F 84 8B 01 00 00               je 0x1407d1a3a
007D18AF  48 3B F3                        cmp rsi, rbx
007D18B2  74 47                           je 0x1407d18fb
007D18B4  44 89 3E                        mov dword ptr [rsi], r15d
007D18B7  C7 46 04 00 08 00 00            mov dword ptr [rsi + 4], 0x800
007D18BE  48 8B 3D D3 D4 72 00            mov rdi, qword ptr [rip + 0x72d4d3]
007D18C5  48 85 FF                        test rdi, rdi
007D18C8  74 28                           je 0x1407d18f2
007D18CA  4C 63 07                        movsxd r8, dword ptr [rdi]
007D18CD  4E 8D 04 C5 10 00 00 00         lea r8, [r8*8 + 0x10]
007D18D5  48 8B D7                        mov rdx, rdi
007D18D8  48 8B CE                        mov rcx, rsi
007D18DB  E8 60 4F EF FF                  call 0x1406c6840
007D18E0  8B 47 04                        mov eax, dword ptr [rdi + 4]
007D18E3  03 C0                           add eax, eax
007D18E5  89 46 04                        mov dword ptr [rsi + 4], eax
007D18E8  33 D2                           xor edx, edx
007D18EA  48 8B CF                        mov rcx, rdi
007D18ED  E8 7E 0F 3B 00                  call 0x140b82870
007D18F2  48 89 35 9F D4 72 00            mov qword ptr [rip + 0x72d49f], rsi
007D18F9  EB 07                           jmp 0x1407d1902
007D18FB  48 8B 35 96 D4 72 00            mov rsi, qword ptr [rip + 0x72d496]
007D1902  45 8B EF                        mov r13d, r15d
007D1905  8B 3E                           mov edi, dword ptr [rsi]
007D1907  FF CF                           dec edi
007D1909  41 3B FD                        cmp edi, r13d
007D190C  7C 41                           jl 0x1407d194f
007D190E  46 8D 34 2F                     lea r14d, [rdi + r13]
007D1912  41 D1 FE                        sar r14d, 1
007D1915  49 63 C6                        movsxd rax, r14d
007D1918  48 FF C0                        inc rax
007D191B  48 8D 14 C6                     lea rdx, [rsi + rax*8]
007D191F  41 B8 08 00 00 00               mov r8d, 8
007D1925  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007D192D  E8 DE 51 EF FF                  call 0x1406c6b10
007D1932  85 C0                           test eax, eax
007D1934  79 0B                           jns 0x1407d1941
007D1936  45 85 F6                        test r14d, r14d
007D1939  74 14                           je 0x1407d194f
007D193B  41 8D 7E FF                     lea edi, [r14 - 1]
007D193F  EB C8                           jmp 0x1407d1909
007D1941  7E 06                           jle 0x1407d1949
007D1943  45 8D 6E 01                     lea r13d, [r14 + 1]
007D1947  EB C0                           jmp 0x1407d1909
007D1949  41 BF 01 00 00 00               mov r15d, 1
007D194F  45 85 FF                        test r15d, r15d
007D1952  74 0B                           je 0x1407d195f
007D1954  41 BE FF 00 00 00               mov r14d, 0xff
007D195A  E9 E1 00 00 00                  jmp 0x1407d1a40
007D195F  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007D1964  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
007D1969  E8 AA 4C 3B 00                  call 0x140b86618
007D196E  44 8B F0                        mov r14d, eax
007D1971  33 C9                           xor ecx, ecx
007D1973  85 C0                           test eax, eax
007D1975  78 27                           js 0x1407d199e
007D1977  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007D197C  4C 8D 05 BD 71 33 00            lea r8, [rip + 0x3371bd]
007D1983  8D 51 02                        lea edx, [rcx + 2]
007D1986  8D 4A 64                        lea ecx, [rdx + 0x64]
007D1989  E8 02 79 B8 FF                  call 0x140359290
007D198E  8B 0D DC 88 72 00               mov ecx, dword ptr [rip + 0x7288dc]
007D1994  85 C9                           test ecx, ecx
007D1996  0F 84 A4 00 00 00               je 0x1407d1a40
007D199C  33 C9                           xor ecx, ecx
007D199E  41 3B FD                        cmp edi, r13d
007D19A1  7D 21                           jge 0x1407d19c4
007D19A3  44 8B E9                        mov r13d, ecx
007D19A6  8B 06                           mov eax, dword ptr [rsi]
007D19A8  8D 78 FF                        lea edi, [rax - 1]
007D19AB  85 C0                           test eax, eax
007D19AD  75 15                           jne 0x1407d19c4
007D19AF  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007D19B7  48 89 46 08                     mov qword ptr [rsi + 8], rax
007D19BB  C7 06 01 00 00 00               mov dword ptr [rsi], 1
007D19C1  48 8B F1                        mov rsi, rcx
007D19C4  48 85 F6                        test rsi, rsi
007D19C7  74 77                           je 0x1407d1a40
007D19C9  44 8B F9                        mov r15d, ecx
007D19CC  45 85 ED                        test r13d, r13d
007D19CF  45 0F 49 FD                     cmovns r15d, r13d
007D19D3  FF C7                           inc edi
007D19D5  EB 24                           jmp 0x1407d19fb
007D19D7  49 63 C7                        movsxd rax, r15d
007D19DA  48 FF C0                        inc rax
007D19DD  48 8D 14 C6                     lea rdx, [rsi + rax*8]
007D19E1  41 B8 08 00 00 00               mov r8d, 8
007D19E7  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007D19EF  E8 1C 51 EF FF                  call 0x1406c6b10
007D19F4  85 C0                           test eax, eax
007D19F6  78 08                           js 0x1407d1a00
007D19F8  41 FF C7                        inc r15d
007D19FB  44 3B FF                        cmp r15d, edi
007D19FE  7C D7                           jl 0x1407d19d7
007D1A00  49 63 C7                        movsxd rax, r15d
007D1A03  48 8D 3C C6                     lea rdi, [rsi + rax*8]
007D1A07  8B 06                           mov eax, dword ptr [rsi]
007D1A09  41 2B C7                        sub eax, r15d
007D1A0C  4C 63 C0                        movsxd r8, eax
007D1A0F  49 C1 E0 03                     shl r8, 3
007D1A13  41 8D 47 01                     lea eax, [r15 + 1]
007D1A17  48 63 C8                        movsxd rcx, eax
007D1A1A  48 FF C1                        inc rcx
007D1A1D  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
007D1A21  48 8D 57 08                     lea rdx, [rdi + 8]
007D1A25  E8 16 4E EF FF                  call 0x1406c6840
007D1A2A  FF 06                           inc dword ptr [rsi]
007D1A2C  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007D1A34  48 89 47 08                     mov qword ptr [rdi + 8], rax
007D1A38  EB 06                           jmp 0x1407d1a40
007D1A3A  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
007D1A40  F0 48 0F C1 1D 2F D3 72 00      lock xadd qword ptr [rip + 0x72d32f], rbx
007D1A49  80 E3 06                        and bl, 6
007D1A4C  80 FB 02                        cmp bl, 2
007D1A4F  75 08                           jne 0x1407d1a59
007D1A51  49 8B CC                        mov rcx, r12
007D1A54  E8 77 43 A9 FF                  call 0x140265dd0
007D1A59  49 8B CC                        mov rcx, r12
007D1A5C  E8 9F FB B0 FF                  call 0x1402e1600
007D1A61  E8 4A BE A8 FF                  call 0x14025d8b0
007D1A66  E9 A0 FD FF FF                  jmp 0x1407d180b
007D1A6B  8B D8                           mov ebx, eax
007D1A6D  33 D2                           xor edx, edx
007D1A6F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007D1A74  E8 F7 0D 3B 00                  call 0x140b82870
007D1A79  8B C3                           mov eax, ebx
007D1A7B  EB 07                           jmp 0x1407d1a84
007D1A7D  B8 0D 00 00 C0                  mov eax, 0xc000000d
007D1A82  EB 00                           jmp 0x1407d1a84
007D1A84  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
007D1A8C  48 33 CC                        xor rcx, rsp
007D1A8F  E8 AC AB ED FF                  call 0x1406ac640
007D1A94  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
007D1A9C  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007D1AA0  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007D1AA4  49 8B E3                        mov rsp, r11
007D1AA7  41 5F                           pop r15
007D1AA9  41 5E                           pop r14
007D1AAB  41 5D                           pop r13
007D1AAD  41 5C                           pop r12
007D1AAF  5F                              pop rdi
007D1AB0  C3                              ret
007D1AB1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpKdPullRemoteFileForUser(__int64 a1)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int16 v_stack_m7E;
    unsigned __int16 v_stack_m80;
    unsigned __int8 v_stack_m88;
    unsigned __int8 v_stack_m8E;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int16 v_stack_m9E;
    unsigned __int16 v_stack_mA0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 6525299)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r15 = 0;
    v_stack_m9C = 0;
    v_stack_m7C = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m90 = v_xmm0;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_007D1634;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (((v_stack_m88) & ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a3, a4);
    }
    if ((v_stack_m88 + 2) > (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) goto loc_007D1632;
    result = v_stack_m88;
    if ((v_stack_m88 + 2) < v_stack_m88) {
        result = *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    if ((unsigned __int16)(v_stack_m90) == 0) goto loc_007D1A7D;
    if ((((unsigned __int8)(v_stack_m90)) & (1)) != 0) goto loc_007D1A7D;
    if (((v_stack_m8E) & (1)) != 0) goto loc_007D1A7D;
    if (v_stack_m8E < ((unsigned __int16)(v_stack_m90))) goto loc_007D1A7D;
    result = ExAllocatePool2(64, v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(0x46644B55ULL))), a4);
    v_stack_m98 = result;
    if (result != 0) goto loc_007D168E;
    goto loc_007D1A84;
loc_007D168E:
    v_stack_mA0 = (unsigned __int16)(v_stack_m90);
    v_stack_m9E = (unsigned __int16)(v_stack_m90);
    result = memcpy((unsigned int)(0xC000009AULL), v_stack_m88, v_stack_m90, a4);
    result = ExAllocatePool2(64, v_stack_mA0, (unsigned int)((unsigned int)((unsigned int)(0x46644B55ULL))), a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007D16CE;
    goto loc_007D180B;
loc_007D16CE:
    v_stack_m80 = (unsigned __int16)(v_stack_mA0);
    v_stack_m7E = (unsigned __int16)(v_stack_m9E);
    a3 = 0;
    result = RtlDowncaseUnicodeString(v_stack_m80, v_stack_mA0, a3, a4);
    result = KeComputeSha256(v_stack_m78, v_stack_m80, v_stack_m58, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, a2, v_stack_m58, a4);
    v_rbx = (v_stack_m90) | (-1);
    if ((*(unsigned __int64 *)(v_rip + 7525998)) == 0) goto loc_007D181F;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7525974, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 7525974;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 7525974;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rip + 7525908) == 0) goto loc_007D17DB;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525908)))) - 1);
loc_007D178E:
    if (((unsigned int)(v_rdi)) < 0) goto loc_007D17D8;
    v_rsi = (unsigned int)((v_r15 + v_rdi * 1) >> (1));
    result = ((int)((unsigned int)(v_rsi))) + 1;
    result = memcmp(v_stack_m58, *(unsigned __int64 *)(v_rip + 7525908) + result * 8, 8, a4);
    if (!sign_flag) goto loc_007D17C3;
    if ((unsigned int)(v_rsi) == 0) goto loc_007D17D8;
    goto loc_007D178E;
loc_007D17C3:
    v_r15 = 0;
    if (condition_is_less_or_equal) goto loc_007D17D0;
    goto loc_007D178E;
loc_007D17D0:
    goto loc_007D17DB;
loc_007D17D8:
    v_r15 = 0;
loc_007D17DB:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rip + 7525974;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(v_rip + 7525908) + result * 8, 8, a4);
    }
    result = KeAbPostRelease(v_rip + 7525974, *(unsigned __int64 *)(v_rip + 7525908) + result * 8, 8, a4);
    result = KeLeaveCriticalRegion(v_rip + 7525974, *(unsigned __int64 *)(v_rip + 7525908) + result * 8, 8, a4);
    if (1 == 0) goto loc_007D181F;
loc_007D180B:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m98, a2, 8, a4);
    goto loc_007D1A84;
loc_007D181F:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7525974, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7525974;
        a2 = result;
        a1 = v_rip + 7525974;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rip + 7525678) != 0) goto loc_007D1876;
    goto loc_007D1893;
loc_007D1876:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525678))))) >= 0x1FFFFFFFULL) goto loc_007D1A3A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525678))))) != ((unsigned int)((int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525678) + 4))))) goto loc_007D18A6;
    a2 = ((int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525678) + 4))) + 1;
    a2 = (a2) << (4);
loc_007D1893:
    result = ExAllocatePool2(256, a2, (unsigned int)(0x66644B55ULL), a4);
loc_007D18A6:
    if (result == 0) goto loc_007D1A3A;
    if (result == v_rbx) goto loc_007D18FB;
    *(unsigned int *)(result) = 0;
    *(unsigned int *)(result + 4) = 0x800ULL;
    if (*(unsigned __int64 *)(v_rip + 7525587) != 0) {
        a3 = (int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525587)));
        a3 = a3 * 8 + 16;
        a2 = *(unsigned __int64 *)(v_rip + 7525587);
        a1 = result;
        result = memcpy(a1, a2, a3, a4);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525587) + 4);
        result = (unsigned int)((result) + ((unsigned int)(result)));
        *(unsigned int *)(result + 4) = (unsigned int)(result);
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 7525587);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 7525535) = result;
    goto loc_007D1902;
loc_007D18FB:
loc_007D1902:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525526)))) - 1);
loc_007D1909:
    if (((unsigned int)(v_rdi)) < 0) goto loc_007D194F;
    v_r14 = (unsigned int)((v_rdi + 0 * 1) >> (1));
    result = ((int)((unsigned int)(v_r14))) + 1;
    result = memcmp(v_stack_m58, *(unsigned __int64 *)(v_rip + 7525526) + result * 8, 8, a4);
    if (!sign_flag) goto loc_007D1941;
    if ((unsigned int)(v_r14) == 0) goto loc_007D194F;
    goto loc_007D1909;
loc_007D1941:
    if (condition_is_less_or_equal) goto loc_007D1949;
    goto loc_007D1909;
loc_007D1949:
loc_007D194F:
    if (1 == 0) goto loc_007D195F;
    goto loc_007D1A40;
loc_007D195F:
    result = KdPullRemoteFile(v_stack_mA0, v_stack_mA0, 8, a4);
    a1 = 0;
    if (sign_flag) goto loc_007D199E;
    result = DbgPrintEx(a1 + 2 + 100, a1 + 2, v_rip + 3371453, v_stack_mA0);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7506140))) == 0) goto loc_007D1A40;
    a1 = 0;
loc_007D199E:
    if (((unsigned int)(v_r14 - 1)) >= ((unsigned int)(v_r14 + 1))) goto loc_007D19C4;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525526)));
    v_rsi = *(unsigned __int64 *)(v_rip + 7525526);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525526)))) == 0) {
        result = v_stack_m58;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7525526) + 8) = result;
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525526)) = 1;
        v_rsi = 0;
    }
    if (v_rsi == 0) goto loc_007D1A40;
    v_r15 = 0;
    if (!sign_flag) { v_r15 = 0; }
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525526))) - 1) + 1);
    goto loc_007D19FB;
loc_007D19D7:
    result = ((int)((unsigned int)(v_r15))) + 1;
    result = memcmp(v_stack_m58, v_rsi + result * 8, 8, v_stack_mA0);
    if (sign_flag) goto loc_007D1A00;
    v_r15 = (unsigned int)((v_r15) + 1);
loc_007D19FB:
    if (((unsigned int)(v_r15)) < ((unsigned int)(v_rdi))) goto loc_007D19D7;
loc_007D1A00:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) - ((unsigned int)(v_r15)));
    a3 = ((int)((unsigned int)(result))) << (3);
    a1 = ((int)((unsigned int)(v_r15 + 1))) + 1;
    result = memcpy(v_rsi + a1 * 8, v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8, a3, v_stack_mA0);
    *(unsigned __int64 *)(v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8) = v_stack_m58;
    goto loc_007D1A40;
loc_007D1A3A:
loc_007D1A40:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = v_stack_m58;
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 7525974;
        result = ExfTryToWakePushLock(a1, v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8, a3, v_stack_mA0);
    }
    result = KeAbPostRelease(v_rip + 7525974, v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8, a3, v_stack_mA0);
    result = KeLeaveCriticalRegion(v_rip + 7525974, v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8, a3, v_stack_mA0);
    goto loc_007D180B;
loc_007D1A7D:
    goto loc_007D1A84;
loc_007D1A84:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rsi + (int)((unsigned int)(v_r15)) * 8 + 8, a3, v_stack_mA0);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpKdPullRemoteFileForUser(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint16_t v_stack_m7E;
    uint16_t v_stack_m80;
    uint8_t v_stack_m88;
    uint8_t v_stack_m8E;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint16_t v_stack_m9E;
    uint16_t v_stack_mA0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x639173)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r15 = 0;
    v_stack_m9C = 0;
    v_stack_m7C = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m90 = v_xmm0;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_007D1634;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (((v_stack_m88) & ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), a3, a4);
    }
    if ((v_stack_m88 + 2) > (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) goto loc_007D1632;
    result = v_stack_m88;
    if ((v_stack_m88 + 2) < v_stack_m88) {
        result = *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    if ((uint16_t)(v_stack_m90) == 0) goto loc_007D1A7D;
    if ((((uint8_t)(v_stack_m90)) & (1)) != 0) goto loc_007D1A7D;
    if (((v_stack_m8E) & (1)) != 0) goto loc_007D1A7D;
    if (v_stack_m8E < ((uint16_t)(v_stack_m90))) goto loc_007D1A7D;
    result = ExAllocatePool2(64, v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(0x46644B55ULL))), a4);
    v_stack_m98 = result;
    if (result != 0) goto loc_007D168E;
    goto loc_007D1A84;
loc_007D168E:
    v_stack_mA0 = (uint16_t)(v_stack_m90);
    v_stack_m9E = (uint16_t)(v_stack_m90);
    result = memcpy((uint32_t)(0xC000009AULL), v_stack_m88, v_stack_m90, a4);
    result = ExAllocatePool2(64, v_stack_mA0, (uint32_t)((uint32_t)((uint32_t)(0x46644B55ULL))), a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007D16CE;
    goto loc_007D180B;
loc_007D16CE:
    v_stack_m80 = (uint16_t)(v_stack_mA0);
    v_stack_m7E = (uint16_t)(v_stack_m9E);
    a3 = 0;
    result = RtlDowncaseUnicodeString(v_stack_m80, v_stack_mA0, a3, a4);
    result = KeComputeSha256(v_stack_m78, v_stack_m80, v_stack_m58, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m78, a2, v_stack_m58, a4);
    local_rbx = (v_stack_m90) | (-1);
    if ((*(uint64_t *)(v_rip + 0x72D66E)) == 0) goto loc_007D181F;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7525974, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 7525974;
        a3 = 0;
        a2 = 0;
        Arg1 = v_rip + 7525974;
        result = ExfAcquirePushLockSharedEx(Arg1, a2, a3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(v_rip + 0x72D614) == 0) goto loc_007D17DB;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D614)))) - 1);
loc_007D178E:
    if (((uint32_t)(local_rdi)) < 0) goto loc_007D17D8;
    local_rsi = (uint32_t)((local_r15 + local_rdi * 1) >> (1));
    result = ((int32_t)((uint32_t)(local_rsi))) + 1;
    result = memcmp(v_stack_m58, *(uint64_t *)(v_rip + 0x72D614) + result * 8, 8, a4);
    if (!sign_flag) goto loc_007D17C3;
    if ((uint32_t)(local_rsi) == 0) goto loc_007D17D8;
    goto loc_007D178E;
loc_007D17C3:
    local_r15 = 0;
    if (condition_is_less_or_equal) goto loc_007D17D0;
    goto loc_007D178E;
loc_007D17D0:
    goto loc_007D17DB;
loc_007D17D8:
    local_r15 = 0;
loc_007D17DB:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_rip + 7525974;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(v_rip + 0x72D614) + result * 8, 8, a4);
    }
    result = KeAbPostRelease(v_rip + 7525974, *(uint64_t *)(v_rip + 0x72D614) + result * 8, 8, a4);
    result = KeLeaveCriticalRegion(v_rip + 7525974, *(uint64_t *)(v_rip + 0x72D614) + result * 8, 8, a4);
    if (1 == 0) goto loc_007D181F;
loc_007D180B:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m98, a2, 8, a4);
    goto loc_007D1A84;
loc_007D181F:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7525974, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7525974;
        a2 = result;
        Arg1 = v_rip + 7525974;
        result = ExfAcquirePushLockExclusiveEx(Arg1, a2, a3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(v_rip + 0x72D52E) != 0) goto loc_007D1876;
    goto loc_007D1893;
loc_007D1876:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D52E))))) >= 0x1FFFFFFFULL) goto loc_007D1A3A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D52E))))) != ((uint32_t)((int32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D52E) + 0x4))))) goto loc_007D18A6;
    a2 = ((int32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D52E) + 0x4))) + 1;
    a2 = (a2) << (4);
loc_007D1893:
    result = ExAllocatePool2(256, a2, (uint32_t)(0x66644B55ULL), a4);
loc_007D18A6:
    if (result == 0) goto loc_007D1A3A;
    if (result == local_rbx) goto loc_007D18FB;
    *(uint32_t *)(result) = 0;
    *(uint32_t *)(result + 0x4) = 0x800ULL;
    if (*(uint64_t *)(v_rip + 0x72D4D3) != 0) {
        a3 = (int32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D4D3)));
        a3 = a3 * 8 + 16;
        a2 = *(uint64_t *)(v_rip + 0x72D4D3);
        Arg1 = result;
        result = memcpy(Arg1, a2, a3, a4);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x72D4D3) + 0x4);
        result = (uint32_t)((result) + ((uint32_t)(result)));
        *(uint32_t *)(result + 0x4) = (uint32_t)(result);
        a2 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x72D4D3);
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    *(uint64_t *)(v_rip + 0x72D49F) = result;
    goto loc_007D1902;
loc_007D18FB:
loc_007D1902:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D496)))) - 1);
loc_007D1909:
    if (((uint32_t)(local_rdi)) < 0) goto loc_007D194F;
    local_r14 = (uint32_t)((local_rdi + 0 * 1) >> (1));
    result = ((int32_t)((uint32_t)(local_r14))) + 1;
    result = memcmp(v_stack_m58, *(uint64_t *)(v_rip + 0x72D496) + result * 8, 8, a4);
    if (!sign_flag) goto loc_007D1941;
    if ((uint32_t)(local_r14) == 0) goto loc_007D194F;
    goto loc_007D1909;
loc_007D1941:
    if (condition_is_less_or_equal) goto loc_007D1949;
    goto loc_007D1909;
loc_007D1949:
loc_007D194F:
    if (1 == 0) goto loc_007D195F;
    goto loc_007D1A40;
loc_007D195F:
    result = KdPullRemoteFile(v_stack_mA0, v_stack_mA0, 8, a4);
    Arg1 = 0;
    if (sign_flag) goto loc_007D199E;
    result = DbgPrintEx(Arg1 + 2 + 100, Arg1 + 2, v_rip + 3371453, v_stack_mA0);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7288DC))) == 0) goto loc_007D1A40;
    Arg1 = 0;
loc_007D199E:
    if (((uint32_t)(local_r14 - 1)) >= ((uint32_t)(local_r14 + 1))) goto loc_007D19C4;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D496)));
    local_rsi = *(uint64_t *)(v_rip + 0x72D496);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D496)))) == 0) {
        result = v_stack_m58;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x72D496) + 0x8) = result;
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x72D496)) = 1;
        local_rsi = 0;
    }
    if (local_rsi == 0) goto loc_007D1A40;
    local_r15 = 0;
    if (!sign_flag) { local_r15 = 0; }
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D496))) - 1) + 1);
    goto loc_007D19FB;
loc_007D19D7:
    result = ((int32_t)((uint32_t)(local_r15))) + 1;
    result = memcmp(v_stack_m58, local_rsi + result * 8, 8, v_stack_mA0);
    if (sign_flag) goto loc_007D1A00;
    local_r15 = (uint32_t)((local_r15) + 1);
loc_007D19FB:
    if (((uint32_t)(local_r15)) < ((uint32_t)(local_rdi))) goto loc_007D19D7;
loc_007D1A00:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) - ((uint32_t)(local_r15)));
    a3 = ((int32_t)((uint32_t)(result))) << (3);
    Arg1 = ((int32_t)((uint32_t)(local_r15 + 1))) + 1;
    result = memcpy(local_rsi + Arg1 * 8, local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 8, a3, v_stack_mA0);
    *(uint64_t *)(local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 0x8) = v_stack_m58;
    goto loc_007D1A40;
loc_007D1A3A:
loc_007D1A40:
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = v_stack_m58;
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 7525974;
        result = ExfTryToWakePushLock(Arg1, local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 8, a3, v_stack_mA0);
    }
    result = KeAbPostRelease(v_rip + 7525974, local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 8, a3, v_stack_mA0);
    result = KeLeaveCriticalRegion(v_rip + 7525974, local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 8, a3, v_stack_mA0);
    goto loc_007D180B;
loc_007D1A7D:
    goto loc_007D1A84;
loc_007D1A84:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rsi + (int32_t)((uint32_t)(local_r15)) * 8 + 8, a3, v_stack_mA0);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D15AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
