# KiAttemptToStealStandbyThread

- RVA: `0x0030D790`–`0x0030DD6E` (길이 `1,502` bytes)
- VA: `0x000000014030D790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00073EB4`
- 디코드: `399`개 명령, `1,502/1,502` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0030D7DC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030D838` → [KiAcquireMultiplePrcbLockArrays](KiAcquireMultiplePrcbLockArrays_function_0030D4D0.md) (function, `0x0030D4D0`)
- `0x0030D8EF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0030D915` → [KiIsIsolationUnitIdleByHandle](../25/KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x0030D929` → [KiFindStandbyThreadForSteal](KiFindStandbyThreadForSteal_function_0030D640.md) (function, `0x0030D640`)
- `0x0030D950` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030D960` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030D983` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030D994` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030D9A9` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030D9FF` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030DA42` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030DB02` → [KiScheduleThreadToRescheduleContext](KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x0030DB14` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030DB5A` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030DC73` → [KiAcquirePrcbLocksForIsolationUnit](KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0030DC8F` → [KiReadyDeferredReadyList](KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x0030DCC2` → [KiCompleteRescheduleContextEntry](../35/KiCompleteRescheduleContextEntry_function_00356330.md) (function, `0x00356330`)
- `0x0030DCE4` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)

### Direct callers
- [KiSearchForNewThreadsOnTarget](KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x0030FA4D`

### Static image references
- `0x0030D7AC` → RVA `0x00E0A740` (`.data`; read)
- `0x0030DA04` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0030DD69` → [sub_006E0E76](../6E/Unknown_function_006E0E76.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030D790  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0030D795  55                              push rbp
0030D796  56                              push rsi
0030D797  57                              push rdi
0030D798  41 54                           push r12
0030D79A  41 55                           push r13
0030D79C  41 56                           push r14
0030D79E  41 57                           push r15
0030D7A0  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
0030D7A5  48 81 EC 80 01 00 00            sub rsp, 0x180
0030D7AC  48 8B 05 8D CF AF 00            mov rax, qword ptr [rip + 0xafcf8d]
0030D7B3  48 33 C4                        xor rax, rsp
0030D7B6  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0030D7BA  4D 8B E0                        mov r12, r8
0030D7BD  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
0030D7C2  4C 8B EA                        mov r13, rdx
0030D7C5  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0030D7CA  4C 8B F1                        mov r14, rcx
0030D7CD  41 BF F0 00 00 00               mov r15d, 0xf0
0030D7D3  45 8B C7                        mov r8d, r15d
0030D7D6  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0030D7DA  33 D2                           xor edx, edx
0030D7DC  E8 5F 94 3B 00                  call 0x1406c6c40
0030D7E1  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
0030D7E7  33 FF                           xor edi, edi
0030D7E9  48 21 7C 24 38                  and qword ptr [rsp + 0x38], rdi
0030D7EE  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0030D7F3  49 8B 8D 58 8E 00 00            mov rcx, qword ptr [r13 + 0x8e58]
0030D7FA  8D 77 01                        lea esi, [rdi + 1]
0030D7FD  4D 8B 84 24 58 8E 00 00         mov r8, qword ptr [r12 + 0x8e58]
0030D805  49 3B C8                        cmp rcx, r8
0030D808  0F 84 5B 04 00 00               je 0x14030dc69
0030D80E  45 0F B6 08                     movzx r9d, byte ptr [r8]
0030D812  49 8B FD                        mov rdi, r13
0030D815  0F B6 11                        movzx edx, byte ptr [rcx]
0030D818  48 0B FE                        or rdi, rsi
0030D81B  49 8B DC                        mov rbx, r12
0030D81E  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0030D823  48 0B DE                        or rbx, rsi
0030D826  49 83 C0 08                     add r8, 8
0030D82A  48 83 C1 08                     add rcx, 8
0030D82E  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0030D833  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0030D838  E8 93 FC FF FF                  call 0x14030d4d0
0030D83D  41 84 74 24 23                  test byte ptr [r12 + 0x23], sil
0030D842  0F 84 C8 00 00 00               je 0x14030d910
0030D848  45 32 D2                        xor r10b, r10b
0030D84B  48 85 FF                        test rdi, rdi
0030D84E  74 48                           je 0x14030d898
0030D850  48 8B CF                        mov rcx, rdi
0030D853  45 33 C0                        xor r8d, r8d
0030D856  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030D85A  33 D2                           xor edx, edx
0030D85C  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0030D861  23 FE                           and edi, esi
0030D863  0F 84 BD 03 00 00               je 0x14030dc26
0030D869  83 FF 01                        cmp edi, 1
0030D86C  75 0E                           jne 0x14030d87c
0030D86E  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030D875  0F B6 10                        movzx edx, byte ptr [rax]
0030D878  4C 8D 40 08                     lea r8, [rax + 8]
0030D87C  85 D2                           test edx, edx
0030D87E  74 18                           je 0x14030d898
0030D880  8D 42 FF                        lea eax, [rdx - 1]
0030D883  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030D887  8B D0                           mov edx, eax
0030D889  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030D88F  85 C0                           test eax, eax
0030D891  75 ED                           jne 0x14030d880
0030D893  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0030D898  48 85 DB                        test rbx, rbx
0030D89B  74 48                           je 0x14030d8e5
0030D89D  48 8B CB                        mov rcx, rbx
0030D8A0  45 33 C9                        xor r9d, r9d
0030D8A3  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030D8A7  45 33 C0                        xor r8d, r8d
0030D8AA  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0030D8AF  23 DE                           and ebx, esi
0030D8B1  0F 84 7B 03 00 00               je 0x14030dc32
0030D8B7  83 FB 01                        cmp ebx, 1
0030D8BA  75 0F                           jne 0x14030d8cb
0030D8BC  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030D8C3  44 0F B6 00                     movzx r8d, byte ptr [rax]
0030D8C7  4C 8D 48 08                     lea r9, [rax + 8]
0030D8CB  45 85 C0                        test r8d, r8d
0030D8CE  74 15                           je 0x14030d8e5
0030D8D0  41 8D 48 FF                     lea ecx, [r8 - 1]
0030D8D4  49 8B 14 C9                     mov rdx, qword ptr [r9 + rcx*8]
0030D8D8  44 8B C1                        mov r8d, ecx
0030D8DB  F0 48 83 62 30 00               lock and qword ptr [rdx + 0x30], 0
0030D8E1  85 C9                           test ecx, ecx
0030D8E3  75 EB                           jne 0x14030d8d0
0030D8E5  41 8A C2                        mov al, r10b
0030D8E8  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0030D8EC  48 33 CC                        xor rcx, rsp
0030D8EF  E8 4C ED 39 00                  call 0x1406ac640
0030D8F4  48 8B 9C 24 D8 01 00 00         mov rbx, qword ptr [rsp + 0x1d8]
0030D8FC  48 81 C4 80 01 00 00            add rsp, 0x180
0030D903  41 5F                           pop r15
0030D905  41 5E                           pop r14
0030D907  41 5D                           pop r13
0030D909  41 5C                           pop r12
0030D90B  5F                              pop rdi
0030D90C  5E                              pop rsi
0030D90D  5D                              pop rbp
0030D90E  C3                              ret
0030D90F  CC                              int3
0030D910  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0030D915  E8 56 93 F4 FF                  call 0x140256c70
0030D91A  45 33 C0                        xor r8d, r8d
0030D91D  49 8B D5                        mov rdx, r13
0030D920  85 C0                           test eax, eax
0030D922  49 8B CC                        mov rcx, r12
0030D925  41 0F 95 C0                     setne r8b
0030D929  E8 12 FD FF FF                  call 0x14030d640
0030D92E  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0030D933  48 85 C0                        test rax, rax
0030D936  0F 84 0C FF FF FF               je 0x14030d848
0030D93C  4D 8B B6 E8 37 00 00            mov r14, qword ptr [r14 + 0x37e8]
0030D943  4D 8B C7                        mov r8, r15
0030D946  49 8B CE                        mov rcx, r14
0030D949  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
0030D94E  33 D2                           xor edx, edx
0030D950  E8 EB 92 3B 00                  call 0x1406c6c40
0030D955  45 33 C0                        xor r8d, r8d
0030D958  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0030D95D  49 8B CE                        mov rcx, r14
0030D960  E8 4B ED FF FF                  call 0x14030c6b0
0030D965  48 85 FF                        test rdi, rdi
0030D968  0F 84 D1 02 00 00               je 0x14030dc3f
0030D96E  4C 8D 7D 80                     lea r15, [rbp - 0x80]
0030D972  33 D2                           xor edx, edx
0030D974  41 B8 F0 00 00 00               mov r8d, 0xf0
0030D97A  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
0030D97F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0030D983  E8 B8 92 3B 00                  call 0x1406c6c40
0030D988  45 33 C0                        xor r8d, r8d
0030D98B  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0030D990  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0030D994  E8 17 ED FF FF                  call 0x14030c6b0
0030D999  49 8B D5                        mov rdx, r13
0030D99C  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0030D9A1  49 8B CF                        mov rcx, r15
0030D9A4  C6 44 24 31 00                  mov byte ptr [rsp + 0x31], 0
0030D9A9  E8 B2 56 04 00                  call 0x140353060
0030D9AE  4C 8B C8                        mov r9, rax
0030D9B1  44 0F B6 40 20                  movzx r8d, byte ptr [rax + 0x20]
0030D9B6  4C 8B 10                        mov r10, qword ptr [rax]
0030D9B9  41 F6 C0 20                     test r8b, 0x20
0030D9BD  75 04                           jne 0x14030d9c3
0030D9BF  40 08 70 22                     or byte ptr [rax + 0x22], sil
0030D9C3  80 48 22 02                     or byte ptr [rax + 0x22], 2
0030D9C7  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
0030D9CB  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
0030D9CF  41 8A C0                        mov al, r8b
0030D9D2  24 C5                           and al, 0xc5
0030D9D4  0C 05                           or al, 5
0030D9D6  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0030D9DA  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
0030D9DE  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
0030D9E3  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
0030D9E7  41 F6 C0 02                     test r8b, 2
0030D9EB  0F 85 FD 02 00 00               jne 0x14030dcee
0030D9F1  4D 3B FE                        cmp r15, r14
0030D9F4  0F 84 67 02 00 00               je 0x14030dc61
0030D9FA  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0030D9FF  E8 1C AC F4 FF                  call 0x140258620
0030DA04  44 8B 25 09 91 CB 00            mov r12d, dword ptr [rip + 0xcb9109]
0030DA0B  45 33 ED                        xor r13d, r13d
0030DA0E  41 C1 EC 09                     shr r12d, 9
0030DA12  41 83 E4 02                     and r12d, 2
0030DA16  C6 44 24 31 00                  mov byte ptr [rsp + 0x31], 0
0030DA1B  45 38 2F                        cmp byte ptr [r15], r13b
0030DA1E  76 45                           jbe 0x14030da65
0030DA20  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0030DA25  45 8A F5                        mov r14b, r13b
0030DA28  41 8B CD                        mov ecx, r13d
0030DA2B  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
0030DA30  48 83 C1 02                     add rcx, 2
0030DA34  45 8B C4                        mov r8d, r12d
0030DA37  48 8B D3                        mov rdx, rbx
0030DA3A  4A 8D 0C A9                     lea rcx, [rcx + r13*4]
0030DA3E  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0030DA42  E8 89 F5 FF FF                  call 0x14030cfd0
0030DA47  44 0A F0                        or r14b, al
0030DA4A  44 03 EE                        add r13d, esi
0030DA4D  41 0F B6 07                     movzx eax, byte ptr [r15]
0030DA51  44 3B E8                        cmp r13d, eax
0030DA54  72 D2                           jb 0x14030da28
0030DA56  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0030DA5B  44 88 74 24 31                  mov byte ptr [rsp + 0x31], r14b
0030DA60  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0030DA65  41 39 77 08                     cmp dword ptr [r15 + 8], esi
0030DA69  75 1C                           jne 0x14030da87
0030DA6B  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0030DA6F  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030DA76  8A 41 01                        mov al, byte ptr [rcx + 1]
0030DA79  40 02 C6                        add al, sil
0030DA7C  88 41 01                        mov byte ptr [rcx + 1], al
0030DA7F  3A 01                           cmp al, byte ptr [rcx]
0030DA81  72 04                           jb 0x14030da87
0030DA83  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0030DA87  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0030DA8C  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
0030DA91  48 85 FF                        test rdi, rdi
0030DA94  74 54                           je 0x14030daea
0030DA96  48 8B CF                        mov rcx, rdi
0030DA99  45 33 C0                        xor r8d, r8d
0030DA9C  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030DAA0  33 D2                           xor edx, edx
0030DAA2  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0030DAA7  23 FE                           and edi, esi
0030DAA9  0F 84 A6 01 00 00               je 0x14030dc55
0030DAAF  83 FF 01                        cmp edi, 1
0030DAB2  75 0E                           jne 0x14030dac2
0030DAB4  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030DABB  0F B6 10                        movzx edx, byte ptr [rax]
0030DABE  4C 8D 40 08                     lea r8, [rax + 8]
0030DAC2  85 D2                           test edx, edx
0030DAC4  74 1D                           je 0x14030dae3
0030DAC6  8D 42 FF                        lea eax, [rdx - 1]
0030DAC9  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030DACD  8B D0                           mov edx, eax
0030DACF  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030DAD5  85 C0                           test eax, eax
0030DAD7  75 ED                           jne 0x14030dac6
0030DAD9  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0030DADE  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0030DAE3  33 FF                           xor edi, edi
0030DAE5  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0030DAEA  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0030DAEF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0030DAF4  45 33 C9                        xor r9d, r9d
0030DAF7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0030DAFC  4D 8B C4                        mov r8, r12
0030DAFF  49 8B CE                        mov rcx, r14
0030DB02  E8 99 E7 FF FF                  call 0x14030c2a0
0030DB07  41 0A C5                        or al, r13b
0030DB0A  74 0D                           je 0x14030db19
0030DB0C  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0030DB11  49 8B CE                        mov rcx, r14
0030DB14  E8 07 AB F4 FF                  call 0x140258620
0030DB19  44 8B 25 F4 8F CB 00            mov r12d, dword ptr [rip + 0xcb8ff4]
0030DB20  45 32 C9                        xor r9b, r9b
0030DB23  41 C1 EC 09                     shr r12d, 9
0030DB27  45 33 ED                        xor r13d, r13d
0030DB2A  41 83 E4 02                     and r12d, 2
0030DB2E  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
0030DB33  45 38 0E                        cmp byte ptr [r14], r9b
0030DB36  76 4A                           jbe 0x14030db82
0030DB38  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0030DB3D  45 8A F9                        mov r15b, r9b
0030DB40  41 8B CD                        mov ecx, r13d
0030DB43  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
0030DB48  48 83 C1 02                     add rcx, 2
0030DB4C  45 8B C4                        mov r8d, r12d
0030DB4F  48 8B D3                        mov rdx, rbx
0030DB52  4A 8D 0C A9                     lea rcx, [rcx + r13*4]
0030DB56  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0030DB5A  E8 71 F4 FF FF                  call 0x14030cfd0
0030DB5F  44 0A F8                        or r15b, al
0030DB62  44 03 EE                        add r13d, esi
0030DB65  41 0F B6 06                     movzx eax, byte ptr [r14]
0030DB69  44 3B E8                        cmp r13d, eax
0030DB6C  72 D2                           jb 0x14030db40
0030DB6E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0030DB73  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0030DB78  44 8A 4C 24 30                  mov r9b, byte ptr [rsp + 0x30]
0030DB7D  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0030DB82  41 39 76 08                     cmp dword ptr [r14 + 8], esi
0030DB86  75 1C                           jne 0x14030dba4
0030DB88  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0030DB8C  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030DB93  8A 41 01                        mov al, byte ptr [rcx + 1]
0030DB96  40 02 C6                        add al, sil
0030DB99  88 41 01                        mov byte ptr [rcx + 1], al
0030DB9C  3A 01                           cmp al, byte ptr [rcx]
0030DB9E  72 04                           jb 0x14030dba4
0030DBA0  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0030DBA4  48 85 DB                        test rbx, rbx
0030DBA7  74 54                           je 0x14030dbfd
0030DBA9  48 8B CB                        mov rcx, rbx
0030DBAC  45 33 C0                        xor r8d, r8d
0030DBAF  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030DBB3  33 D2                           xor edx, edx
0030DBB5  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0030DBBA  23 DE                           and ebx, esi
0030DBBC  0F 84 8A 00 00 00               je 0x14030dc4c
0030DBC2  83 FB 01                        cmp ebx, 1
0030DBC5  75 0E                           jne 0x14030dbd5
0030DBC7  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030DBCE  0F B6 10                        movzx edx, byte ptr [rax]
0030DBD1  4C 8D 40 08                     lea r8, [rax + 8]
0030DBD5  85 D2                           test edx, edx
0030DBD7  74 18                           je 0x14030dbf1
0030DBD9  8D 42 FF                        lea eax, [rdx - 1]
0030DBDC  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030DBE0  8B D0                           mov edx, eax
0030DBE2  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030DBE8  85 C0                           test eax, eax
0030DBEA  75 ED                           jne 0x14030dbd9
0030DBEC  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0030DBF1  33 DB                           xor ebx, ebx
0030DBF3  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0030DBF8  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0030DBFD  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
0030DC02  0F 85 50 01 00 00               jne 0x14030dd58
0030DC08  45 84 C9                        test r9b, r9b
0030DC0B  0F 85 8C 00 00 00               jne 0x14030dc9d
0030DC11  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0030DC16  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
0030DC1C  75 69                           jne 0x14030dc87
0030DC1E  44 8A D6                        mov r10b, sil
0030DC21  E9 25 FC FF FF                  jmp 0x14030d84b
0030DC26  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
0030DC2B  8B D6                           mov edx, esi
0030DC2D  E9 4E FC FF FF                  jmp 0x14030d880
0030DC32  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
0030DC37  44 8B C6                        mov r8d, esi
0030DC3A  E9 91 FC FF FF                  jmp 0x14030d8d0
0030DC3F  4D 8B FE                        mov r15, r14
0030DC42  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
0030DC47  E9 4D FD FF FF                  jmp 0x14030d999
0030DC4C  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
0030DC51  8B D6                           mov edx, esi
0030DC53  EB 84                           jmp 0x14030dbd9
0030DC55  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0030DC5A  8B D6                           mov edx, esi
0030DC5C  E9 65 FE FF FF                  jmp 0x14030dac6
0030DC61  44 8A EE                        mov r13b, sil
0030DC64  E9 28 FE FF FF                  jmp 0x14030da91
0030DC69  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0030DC6E  8B D6                           mov edx, esi
0030DC70  49 8B CC                        mov rcx, r12
0030DC73  E8 E8 10 00 00                  call 0x14030ed60
0030DC78  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0030DC7D  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0030DC82  E9 B6 FB FF FF                  jmp 0x14030d83d
0030DC87  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0030DC8C  49 8B CE                        mov rcx, r14
0030DC8F  E8 EC 00 00 00                  call 0x14030dd80
0030DC94  EB 88                           jmp 0x14030dc1e
0030DC96  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
0030DC9B  74 3B                           je 0x14030dcd8
0030DC9D  45 33 FF                        xor r15d, r15d
0030DCA0  45 38 3E                        cmp byte ptr [r14], r15b
0030DCA3  76 33                           jbe 0x14030dcd8
0030DCA5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0030DCAA  41 8B CF                        mov ecx, r15d
0030DCAD  45 33 C9                        xor r9d, r9d
0030DCB0  48 83 C1 02                     add rcx, 2
0030DCB4  45 33 C0                        xor r8d, r8d
0030DCB7  48 8B D3                        mov rdx, rbx
0030DCBA  4A 8D 0C B9                     lea rcx, [rcx + r15*4]
0030DCBE  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0030DCC2  E8 69 86 04 00                  call 0x140356330
0030DCC7  41 0F B6 06                     movzx eax, byte ptr [r14]
0030DCCB  44 03 FE                        add r15d, esi
0030DCCE  44 3B F8                        cmp r15d, eax
0030DCD1  72 D7                           jb 0x14030dcaa
0030DCD3  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0030DCD8  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
0030DCDD  49 8D 8E D8 35 00 00            lea rcx, [r14 + 0x35d8]
0030DCE4  E8 17 45 F4 FF                  call 0x140252200
0030DCE9  E9 28 FF FF FF                  jmp 0x14030dc16
0030DCEE  45 33 C0                        xor r8d, r8d
0030DCF1  45 38 07                        cmp byte ptr [r15], r8b
0030DCF4  76 58                           jbe 0x14030dd4e
0030DCF6  41 8B C0                        mov eax, r8d
0030DCF9  4A 8D 14 85 02 00 00 00         lea rdx, [r8*4 + 2]
0030DD01  48 03 D0                        add rdx, rax
0030DD04  49 8D 14 D7                     lea rdx, [r15 + rdx*8]
0030DD08  49 3B D1                        cmp rdx, r9
0030DD0B  74 35                           je 0x14030dd42
0030DD0D  44 8A 52 20                     mov r10b, byte ptr [rdx + 0x20]
0030DD11  4C 8B 1A                        mov r11, qword ptr [rdx]
0030DD14  41 F6 C2 20                     test r10b, 0x20
0030DD18  75 04                           jne 0x14030dd1e
0030DD1A  40 08 72 22                     or byte ptr [rdx + 0x22], sil
0030DD1E  80 4A 22 02                     or byte ptr [rdx + 0x22], 2
0030DD22  41 80 E2 C5                     and r10b, 0xc5
0030DD26  49 8B 43 18                     mov rax, qword ptr [r11 + 0x18]
0030DD2A  41 80 CA 05                     or r10b, 5
0030DD2E  44 88 52 20                     mov byte ptr [rdx + 0x20], r10b
0030DD32  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
0030DD36  49 8B 43 18                     mov rax, qword ptr [r11 + 0x18]
0030DD3A  80 62 21 FE                     and byte ptr [rdx + 0x21], 0xfe
0030DD3E  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
0030DD42  41 0F B6 07                     movzx eax, byte ptr [r15]
0030DD46  44 03 C6                        add r8d, esi
0030DD49  44 3B C0                        cmp r8d, eax
0030DD4C  72 A8                           jb 0x14030dcf6
0030DD4E  41 83 67 04 00                  and dword ptr [r15 + 4], 0
0030DD53  E9 99 FC FF FF                  jmp 0x14030d9f1
0030DD58  45 33 E4                        xor r12d, r12d
0030DD5B  45 38 27                        cmp byte ptr [r15], r12b
0030DD5E  0F 86 32 FF FF FF               jbe 0x14030dc96
0030DD64  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0030DD69  E9 08 31 3D 00                  jmp 0x1406e0e76
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAttemptToStealStandbyThread(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 11521933)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m148 = a3;
    v_stack_m168 = a1;
    a2 = 0;
    result = memset(v_stack_m138, a2, 240, a4);
    v_rdi = 0;
    v_stack_m160 = 0;
    if ((*(unsigned __int64 *)(a2 + 36440)) == (*(unsigned __int64 *)(a3 + 36440))) goto loc_0030DC69;
    v_rdi = (0) | (v_rdi + 1);
    v_stack_m160 = v_rdi;
    v_rbx = (a3) | (v_rdi + 1);
    a3 = (*(unsigned __int64 *)(a3 + 36440)) + (8);
    a1 = (*(unsigned __int64 *)(a2 + 36440)) + (8);
    v_stack_m178 = v_rbx;
    v_stack_m180 = v_rbx;
    result = KiAcquireMultiplePrcbLockArrays(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440)), a3, *(unsigned __int8 *)(*(unsigned __int64 *)(a3 + 36440)));
loc_0030D83D:
    if (((*(unsigned __int8 *)(a3 + 35)) & ((unsigned __int8)(v_rdi + 1))) == 0) goto loc_0030D910;
loc_0030D848:
    v_r10 = 0;
loc_0030D84B:
    if (v_rdi == 0) goto loc_0030D898;
    a3 = 0;
    a1 = (v_rdi) & (-2);
    a2 = 0;
    v_stack_m150 = a1;
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC26;
    if (((unsigned int)(v_rdi)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a2 = *(unsigned __int8 *)(result);
        a3 = result + 8;
    }
    if ((unsigned int)(a2) == 0) goto loc_0030D898;
loc_0030D880:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030D880;
loc_0030D898:
    if (v_stack_m180 == 0) goto loc_0030D8E5;
    a4 = 0;
    a1 = (v_stack_m180) & (-2);
    a3 = 0;
    v_stack_m158 = a1;
    v_rbx = (unsigned int)((v_stack_m180) & ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC32;
    result = a2 - 1;
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a3 = *(unsigned __int8 *)(result);
        a4 = result + 8;
    }
    if ((unsigned int)(a3) == 0) goto loc_0030D8E5;
loc_0030D8D0:
    if ((unsigned int)(a3 - 1) != 0) goto loc_0030D8D0;
loc_0030D8E5:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a4 + a3 - 1 * 8), (unsigned int)((unsigned int)(a3 - 1)), a4);
    v_rsp = (v_rsp) + (384);
    return result;
loc_0030D910:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p38, *(unsigned __int64 *)(a4 + a3 - 1 * 8), (unsigned int)((unsigned int)(a3 - 1)), a4);
    a3 = 0;
    a3 = ((unsigned int)(result) != 0) ? 1 : 0;
    result = KiFindStandbyThreadForSteal(0, a2, a3, a4);
    v_stack_p78 = result;
    if (result == 0) goto loc_0030D848;
    v_stack_p68 = *(unsigned __int64 *)(a1 + 14312);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_p38, a3, a4);
    if (v_rdi == 0) goto loc_0030DC3F;
    a2 = 0;
    v_stack_p60 = v_stack_m138;
    result = memset(v_stack_m138, a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(v_stack_m138, v_stack_p58, a3, a4);
loc_0030D999:
    v_stack_p30 = 0;
    v_stack_p31 = 0;
    result = KiFindRescheduleContextEntryForPrcb(v_stack_m138, 0, a3, a4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (197));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) != 0) goto loc_0030DCEE;
loc_0030D9F1:
    if (v_stack_m138 == (*(unsigned __int64 *)(a1 + 14312))) goto loc_0030DC61;
    result = KiSearchForNewThreadsForRescheduleContext(v_stack_m138, v_stack_p48, *(unsigned __int8 *)(result + 32), result);
    v_r13 = 0;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13340937))) >> (9));
    v_r12 = (unsigned int)((v_r12) & (2));
    v_stack_p31 = 0;
    if ((*(unsigned __int8 *)(v_stack_m138)) <= 0) goto loc_0030DA65;
loc_0030DA28:
    a1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(v_stack_m138 + a1 + v_r13 * 4 * 8, v_stack_p50, (unsigned int)((unsigned int)(v_r12)), v_stack_p48);
    v_r14 = (unsigned __int8)((0) | ((unsigned __int8)(result)));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(v_r13)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m138)))) goto loc_0030DA28;
    v_stack_p31 = (unsigned __int8)(v_r14);
loc_0030DA65:
    if ((*(unsigned int *)(v_stack_m138 + 8)) != ((unsigned int)(v_rdi + 1))) goto loc_0030DA87;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 16) + 36440) + 1)) + ((unsigned __int8)(v_rdi + 1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 16) + 36440) + 1) = 0;
    }
loc_0030DA91:
    if (v_rdi == 0) goto loc_0030DAEA;
    a3 = 0;
    a1 = (v_rdi) & (-2);
    a2 = 0;
    v_stack_p70 = a1;
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC55;
    if (((unsigned int)(v_rdi)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a2 = *(unsigned __int8 *)(result);
        a3 = result + 8;
    }
    if ((unsigned int)(a2) == 0) goto loc_0030DAE3;
loc_0030DAC6:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030DAC6;
    v_stack_p40 = v_stack_p38;
loc_0030DAE3:
    v_rdi = 0;
    v_stack_p58 = 0;
loc_0030DAEA:
    a4 = 0;
    v_stack_p20 = v_stack_p48;
    result = KiScheduleThreadToRescheduleContext(v_stack_p68, v_stack_p78, v_stack_p70, a4);
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_stack_p30)));
    if (!(condition_is_equal)) {
        a2 = v_stack_p48;
        a1 = v_stack_p68;
        result = KiSearchForNewThreadsForRescheduleContext(a1, a2, v_stack_p70, a4);
    }
    a4 = 0;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13340660))) >> (9));
    v_r13 = 0;
    v_r12 = (unsigned int)((v_r12) & (2));
    v_stack_p30 = 0;
    if ((*(unsigned __int8 *)(v_stack_p68)) <= 0) goto loc_0030DB82;
loc_0030DB40:
    a1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(v_stack_p68 + a1 + v_r13 * 4 * 8, v_stack_p50, (unsigned int)((unsigned int)(v_r12)), v_stack_p48);
    v_r15 = (unsigned __int8)((0) | ((unsigned __int8)(result)));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(v_r13)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p68)))) goto loc_0030DB40;
    v_stack_p30 = (unsigned __int8)(v_r15);
loc_0030DB82:
    if ((*(unsigned int *)(v_stack_p68 + 8)) != ((unsigned int)(v_rdi + 1))) goto loc_0030DBA4;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 16) + 36440) + 1)) + ((unsigned __int8)(v_rdi + 1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68 + 16) + 36440) + 1) = 0;
    }
    if (v_stack_p40 == 0) goto loc_0030DBFD;
    a3 = 0;
    a1 = (v_stack_p40) & (-2);
    a2 = 0;
    v_stack_p78 = a1;
    v_rbx = (unsigned int)((v_stack_p40) & ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC4C;
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a2 = *(unsigned __int8 *)(result);
        a3 = result + 8;
    }
    if ((unsigned int)(a2) == 0) goto loc_0030DBF1;
loc_0030DBD9:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030DBD9;
loc_0030DBF1:
    v_rbx = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
loc_0030DBFD:
    if (v_stack_p31 != 0) goto loc_0030DD58;
    if ((unsigned __int8)(v_stack_p30) != 0) goto loc_0030DC9D;
loc_0030DC16:
    if (v_stack_p48 != 0) goto loc_0030DC87;
loc_0030DC1E:
    goto loc_0030D84B;
loc_0030DC26:
    goto loc_0030D880;
loc_0030DC32:
    goto loc_0030D8D0;
loc_0030DC3F:
    v_stack_p60 = v_stack_p50;
    goto loc_0030D999;
loc_0030DC4C:
    goto loc_0030DBD9;
loc_0030DC55:
    goto loc_0030DAC6;
loc_0030DC61:
    goto loc_0030DA91;
loc_0030DC69:
    result = KiAcquirePrcbLocksForIsolationUnit(v_r12, (unsigned int)((unsigned int)(v_rdi + 1)), v_stack_p38, v_stack_p60);
    v_stack_p40 = v_stack_p38;
    goto loc_0030D83D;
loc_0030DC87:
    result = KiReadyDeferredReadyList(v_stack_p50, v_stack_p48, v_stack_p38, v_stack_p60);
    goto loc_0030DC1E;
loc_0030DC96:
    if (v_stack_p30 == 0) goto loc_0030DCD8;
loc_0030DC9D:
    v_r15 = 0;
    if ((*(unsigned __int8 *)(v_stack_p50)) <= 0) goto loc_0030DCD8;
loc_0030DCAA:
    a4 = 0;
    a1 = (0) + (2);
    a3 = 0;
    result = KiCompleteRescheduleContextEntry(v_stack_p50 + a1 + v_r15 * 4 * 8, v_stack_p50, a3, a4);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p50)))) goto loc_0030DCAA;
loc_0030DCD8:
    result = KiFlushSoftwareInterruptBatch(v_stack_p50 + 13784, v_stack_p50, a3, a4);
    goto loc_0030DC16;
loc_0030DCEE:
    a3 = 0;
    if ((*(unsigned __int8 *)(v_r15)) <= 0) goto loc_0030DD4E;
loc_0030DCF6:
    a2 = (a3 * 4 + 2) + (0);
    if ((v_r15 + a2 * 8) == 0) goto loc_0030DD42;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r15 + a2 * 8 + 32))) & (32)) == 0) {
    }
    v_r10 = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + a2 * 8 + 32)) & (197));
    v_r10 = (unsigned __int8)((v_r10) | (5));
    *(unsigned __int8 *)(v_r15 + a2 * 8 + 32) = (unsigned __int8)(v_r10);
    *(unsigned __int64 *)(v_r15 + a2 * 8 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + a2 * 8) + 24);
    *(unsigned __int64 *)(v_r15 + a2 * 8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + a2 * 8) + 24);
loc_0030DD42:
    a3 = (unsigned int)((a3) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int8 *)(v_r15)))) goto loc_0030DCF6;
loc_0030DD4E:
    goto loc_0030D9F1;
loc_0030DD58:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(v_r15)) <= 0) goto loc_0030DC96;
}
```

## 5. (Beta) C Style

```c
int64_t KiAttemptToStealStandbyThread(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m48;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0xAFCF8D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m148 = Arg3;
    v_stack_m168 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 240, a4);
    local_rdi = 0;
    v_stack_m160 = 0;
    if ((*(uint64_t *)(arg2 + 0x8E58)) == (*(uint64_t *)(arg3 + 0x8E58))) goto loc_0030DC69;
    local_rdi = (0) | (local_rdi + 1);
    v_stack_m160 = local_rdi;
    local_rbx = (Arg3) | (local_rdi + 1);
    Arg3 = (*(uint64_t *)(arg3 + 0x8E58)) + (8);
    Arg1 = (*(uint64_t *)(arg2 + 0x8E58)) + (8);
    v_stack_m178 = local_rbx;
    v_stack_m180 = local_rbx;
    result = KiAcquireMultiplePrcbLockArrays(Arg1, *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58)), Arg3, *(uint8_t *)(*(uint64_t *)(arg3 + 0x8E58)));
loc_0030D83D:
    if (((*(uint8_t *)(arg3 + 0x23)) & ((uint8_t)(local_rdi + 1))) == 0) goto loc_0030D910;
loc_0030D848:
    local_r10 = 0;
loc_0030D84B:
    if (local_rdi == 0) goto loc_0030D898;
    Arg3 = 0;
    Arg1 = (local_rdi) & (-2);
    Arg2 = 0;
    v_stack_m150 = Arg1;
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC26;
    if (((uint32_t)(local_rdi)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
        Arg3 = result + 8;
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030D898;
loc_0030D880:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030D880;
loc_0030D898:
    if (v_stack_m180 == 0) goto loc_0030D8E5;
    a4 = 0;
    Arg1 = (v_stack_m180) & (-2);
    Arg3 = 0;
    v_stack_m158 = Arg1;
    local_rbx = (uint32_t)((v_stack_m180) & ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC32;
    result = Arg2 - 1;
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = *(uint8_t *)(result);
        a4 = result + 8;
    }
    if ((uint32_t)(Arg3) == 0) goto loc_0030D8E5;
loc_0030D8D0:
    if ((uint32_t)(Arg3 - 1) != 0) goto loc_0030D8D0;
loc_0030D8E5:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(a4 + arg3 - 0x1 * 8), (uint32_t)((uint32_t)(Arg3 - 1)), a4);
    local_rsp = (local_rsp) + (384);
    return result;
loc_0030D910:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p38, *(uint64_t *)(a4 + arg3 - 0x1 * 8), (uint32_t)((uint32_t)(Arg3 - 1)), a4);
    Arg3 = 0;
    Arg3 = ((uint32_t)(result) != 0) ? 1 : 0;
    result = KiFindStandbyThreadForSteal(0, Arg2, Arg3, a4);
    v_stack_p78 = result;
    if (result == 0) goto loc_0030D848;
    v_stack_p68 = *(uint64_t *)(arg1 + 0x37E8);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, a4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_p38, Arg3, a4);
    if (local_rdi == 0) goto loc_0030DC3F;
    Arg2 = 0;
    v_stack_p60 = v_stack_m138;
    result = memset(v_stack_m138, Arg2, 240, a4);
    Arg3 = 0;
    result = KiStartRescheduleContext(v_stack_m138, v_stack_p58, Arg3, a4);
loc_0030D999:
    v_stack_p30 = 0;
    v_stack_p31 = 0;
    result = KiFindRescheduleContextEntryForPrcb(v_stack_m138, 0, Arg3, a4);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) & (197));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) != 0) goto loc_0030DCEE;
loc_0030D9F1:
    if (v_stack_m138 == (*(uint64_t *)(arg1 + 0x37E8))) goto loc_0030DC61;
    result = KiSearchForNewThreadsForRescheduleContext(v_stack_m138, v_stack_p48, *(uint8_t *)(result + 0x20), result);
    local_r13 = 0;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCB9109))) >> (9));
    local_r12 = (uint32_t)((local_r12) & (2));
    v_stack_p31 = 0;
    if ((*(uint8_t *)(v_stack_m138)) <= 0) goto loc_0030DA65;
loc_0030DA28:
    Arg1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(v_stack_m138 + Arg1 + local_r13 * 4 * 8, v_stack_p50, (uint32_t)((uint32_t)(local_r12)), v_stack_p48);
    local_r14 = (uint8_t)((0) | ((uint8_t)(result)));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(local_r13)) < ((uint32_t)(*(uint8_t *)(v_stack_m138)))) goto loc_0030DA28;
    v_stack_p31 = (uint8_t)(local_r14);
loc_0030DA65:
    if ((*(uint32_t *)(v_stack_m138 + 0x8)) != ((uint32_t)(local_rdi + 1))) goto loc_0030DA87;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x10) + 0x8E58) + 0x1)) + ((uint8_t)(local_rdi + 1)));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x10) + 0x8E58) + 0x1) = 0;
    }
loc_0030DA91:
    if (local_rdi == 0) goto loc_0030DAEA;
    Arg3 = 0;
    Arg1 = (local_rdi) & (-2);
    Arg2 = 0;
    v_stack_p70 = Arg1;
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC55;
    if (((uint32_t)(local_rdi)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
        Arg3 = result + 8;
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030DAE3;
loc_0030DAC6:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030DAC6;
    v_stack_p40 = v_stack_p38;
loc_0030DAE3:
    local_rdi = 0;
    v_stack_p58 = 0;
loc_0030DAEA:
    a4 = 0;
    v_stack_p20 = v_stack_p48;
    result = KiScheduleThreadToRescheduleContext(v_stack_p68, v_stack_p78, v_stack_p70, a4);
    result = (uint8_t)((result) | ((uint8_t)(v_stack_p30)));
    if (!(condition_is_equal)) {
        Arg2 = v_stack_p48;
        Arg1 = v_stack_p68;
        result = KiSearchForNewThreadsForRescheduleContext(Arg1, Arg2, v_stack_p70, a4);
    }
    a4 = 0;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCB8FF4))) >> (9));
    local_r13 = 0;
    local_r12 = (uint32_t)((local_r12) & (2));
    v_stack_p30 = 0;
    if ((*(uint8_t *)(v_stack_p68)) <= 0) goto loc_0030DB82;
loc_0030DB40:
    Arg1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(v_stack_p68 + Arg1 + local_r13 * 4 * 8, v_stack_p50, (uint32_t)((uint32_t)(local_r12)), v_stack_p48);
    local_r15 = (uint8_t)((0) | ((uint8_t)(result)));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(local_r13)) < ((uint32_t)(*(uint8_t *)(v_stack_p68)))) goto loc_0030DB40;
    v_stack_p30 = (uint8_t)(local_r15);
loc_0030DB82:
    if ((*(uint32_t *)(v_stack_p68 + 0x8)) != ((uint32_t)(local_rdi + 1))) goto loc_0030DBA4;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x10) + 0x8E58) + 0x1)) + ((uint8_t)(local_rdi + 1)));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p68 + 0x10) + 0x8E58) + 0x1) = 0;
    }
    if (v_stack_p40 == 0) goto loc_0030DBFD;
    Arg3 = 0;
    Arg1 = (v_stack_p40) & (-2);
    Arg2 = 0;
    v_stack_p78 = Arg1;
    local_rbx = (uint32_t)((v_stack_p40) & ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_0030DC4C;
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
        Arg3 = result + 8;
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030DBF1;
loc_0030DBD9:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030DBD9;
loc_0030DBF1:
    local_rbx = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
loc_0030DBFD:
    if (v_stack_p31 != 0) goto loc_0030DD58;
    if ((uint8_t)(v_stack_p30) != 0) goto loc_0030DC9D;
loc_0030DC16:
    if (v_stack_p48 != 0) goto loc_0030DC87;
loc_0030DC1E:
    goto loc_0030D84B;
loc_0030DC26:
    goto loc_0030D880;
loc_0030DC32:
    goto loc_0030D8D0;
loc_0030DC3F:
    v_stack_p60 = v_stack_p50;
    goto loc_0030D999;
loc_0030DC4C:
    goto loc_0030DBD9;
loc_0030DC55:
    goto loc_0030DAC6;
loc_0030DC61:
    goto loc_0030DA91;
loc_0030DC69:
    result = KiAcquirePrcbLocksForIsolationUnit(local_r12, (uint32_t)((uint32_t)(local_rdi + 1)), v_stack_p38, v_stack_p60);
    v_stack_p40 = v_stack_p38;
    goto loc_0030D83D;
loc_0030DC87:
    result = KiReadyDeferredReadyList(v_stack_p50, v_stack_p48, v_stack_p38, v_stack_p60);
    goto loc_0030DC1E;
loc_0030DC96:
    if (v_stack_p30 == 0) goto loc_0030DCD8;
loc_0030DC9D:
    local_r15 = 0;
    if ((*(uint8_t *)(v_stack_p50)) <= 0) goto loc_0030DCD8;
loc_0030DCAA:
    a4 = 0;
    Arg1 = (0) + (2);
    Arg3 = 0;
    result = KiCompleteRescheduleContextEntry(v_stack_p50 + Arg1 + local_r15 * 4 * 8, v_stack_p50, Arg3, a4);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(v_stack_p50)))) goto loc_0030DCAA;
loc_0030DCD8:
    result = KiFlushSoftwareInterruptBatch(v_stack_p50 + 13784, v_stack_p50, Arg3, a4);
    goto loc_0030DC16;
loc_0030DCEE:
    Arg3 = 0;
    if ((*(uint8_t *)(local_r15)) <= 0) goto loc_0030DD4E;
loc_0030DCF6:
    Arg2 = (Arg3 * 4 + 2) + (0);
    if ((local_r15 + Arg2 * 8) == 0) goto loc_0030DD42;
    if ((((uint8_t)(*(uint8_t *)(local_r15 + arg2 * 8 + 0x20))) & (32)) == 0) {
    }
    local_r10 = (uint8_t)((*(uint8_t *)(local_r15 + arg2 * 8 + 0x20)) & (197));
    local_r10 = (uint8_t)((local_r10) | (5));
    *(uint8_t *)(local_r15 + arg2 * 8 + 0x20) = (uint8_t)(local_r10);
    *(uint64_t *)(local_r15 + arg2 * 8 + 0x10) = *(uint64_t *)(*(uint64_t *)(local_r15 + arg2 * 8) + 0x18);
    *(uint64_t *)(local_r15 + arg2 * 8 + 0x18) = *(uint64_t *)(*(uint64_t *)(local_r15 + arg2 * 8) + 0x18);
loc_0030DD42:
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint8_t *)(local_r15)))) goto loc_0030DCF6;
loc_0030DD4E:
    goto loc_0030D9F1;
loc_0030DD58:
    local_r12 = 0;
    if ((*(uint8_t *)(local_r15)) <= 0) goto loc_0030DC96;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg2` | `+ 0x8E58` | `64` | `R` |
| `Arg3` | `+ 0x23` | `8` | `R` |
| `Arg3` | `+ 0x8E58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030D790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
