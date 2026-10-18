# MiReacquireHigherPageTableLock

- RVA: `0x00239650`–`0x00239D0E` (길이 `1,726` bytes)
- VA: `0x0000000140239650`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BF4`
- 디코드: `414`개 명령, `1,726/1,726` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002397F8` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00239818` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x002398B1` → [KxTryToAcquireQueuedSpinLock](../27/KxTryToAcquireQueuedSpinLock_function_00277388.md) (function, `0x00277388`)
- `0x00239A62` → [MiAgeTrimListsTail](MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x00239B59` → [MiAgeTrimListsTail](MiAgeTrimListsTail_function_00239E90.md) (function, `0x00239E90`)
- `0x00239B9E` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00239BE6` → [MiReleaseWalkLocks](MiReleaseWalkLocks_function_00239FD0.md) (function, `0x00239FD0`)
- `0x00239C72` → [MiDeleteVaTail](../47/MiDeleteVaTail_function_00473EF0.md) (function, `0x00473EF0`)
- `0x00239C82` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00239C9E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00239CB2` → [ExTryAcquireSpinLockExclusiveAtDpcLevel](../2B/ExTryAcquireSpinLockExclusiveAtDpcLevel_function_002BB800.md) (function, `0x002BB800`)
- `0x00239CDB` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00239CF8` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00239D02` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B4F3`

### Static image references
- `0x002396C1` → RVA `0x00E2CB40` (`.data`; read)
- `0x0023978F` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0023994E` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00239A2B` → RVA `0x00428D10` (`MiAgeWorkingSetTail`; read)
- `0x00239A4C` → RVA `0x0048DE00` (`MiAgeWorkingSetVpabCallback`; read)
- `0x00239B29` → RVA `0x00428C00` (`MiUpdateOldWorkingSetPagesTail`; read)
- `0x00239B40` → RVA `0x0049CF50` (`MiUpdateOldPagesVpabCallback`; read)
- `0x00239B88` → RVA `0x00F0DE58` (`.data`; read)
- `0x00239C39` → RVA `0x004ACD40` (`MiSimpleAgePte`; read)
- `0x00239C5F` → RVA `0x00473EF0` (`MiDeleteVaTail`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00239650  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00239655  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0023965A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0023965F  57                              push rdi
00239660  41 54                           push r12
00239662  41 55                           push r13
00239664  41 56                           push r14
00239666  41 57                           push r15
00239668  48 83 EC 30                     sub rsp, 0x30
0023966C  4C 8B 71 20                     mov r14, qword ptr [rcx + 0x20]
00239670  48 8B DA                        mov rbx, rdx
00239673  48 C1 EB 09                     shr rbx, 9
00239677  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00239681  48 23 D8                        and rbx, rax
00239684  45 8B E8                        mov r13d, r8d
00239687  48 8B F2                        mov rsi, rdx
0023968A  48 8B F9                        mov rdi, rcx
0023968D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00239697  48 03 D8                        add rbx, rax
0023969A  48 BA 00 D0 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed000
002396A4  41 BC 02 00 00 00               mov r12d, 2
002396AA  49 B8 FF DF BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbedfff
002396B4  45 33 FF                        xor r15d, r15d
002396B7  48 BD 68 DF BE 7D FB F6 FF FF   movabs rbp, 0xfffff6fb7dbedf68
002396C1  4C 8D 0D 78 34 BF 00            lea r9, [rip + 0xbf3478]
002396C8  48 8B C5                        mov rax, rbp
002396CB  F7 01 00 10 00 00               test dword ptr [rcx], 0x1000
002396D1  0F 84 9A 01 00 00               je 0x140239871
002396D7  48 3B D8                        cmp rbx, rax
002396DA  0F 85 E1 01 00 00               jne 0x1402398c1
002396E0  48 8B C5                        mov rax, rbp
002396E3  48 3B F0                        cmp rsi, rax
002396E6  0F 84 B8 00 00 00               je 0x1402397a4
002396EC  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002396F3  A8 0F                           test al, 0xf
002396F5  74 41                           je 0x140239738
002396F7  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002396FE  A8 0F                           test al, 0xf
00239700  0F 85 1C 01 00 00               jne 0x140239822
00239706  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
00239710  F0 48 21 06                     lock and qword ptr [rsi], rax
00239714  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
00239718  33 C0                           xor eax, eax
0023971A  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0023971F  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00239724  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00239729  48 83 C4 30                     add rsp, 0x30
0023972D  41 5F                           pop r15
0023972F  41 5E                           pop r14
00239731  41 5D                           pop r13
00239733  41 5C                           pop r12
00239735  5F                              pop rdi
00239736  C3                              ret
00239737  CC                              int3
00239738  48 8B C2                        mov rax, rdx
0023973B  48 3B F0                        cmp rsi, rax
0023973E  72 B7                           jb 0x1402396f7
00239740  49 8B C0                        mov rax, r8
00239743  48 3B F0                        cmp rsi, rax
00239746  77 AF                           ja 0x1402396f7
00239748  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00239751  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00239758  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0023975F  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00239766  48 85 C9                        test rcx, rcx
00239769  74 8C                           je 0x1402396f7
0023976B  48 C1 EE 03                     shr rsi, 3
0023976F  81 E6 FF 01 00 00               and esi, 0x1ff
00239775  8B 04 B1                        mov eax, dword ptr [rcx + rsi*4]
00239778  48 8D 0C B1                     lea rcx, [rcx + rsi*4]
0023977C  A9 FF FF FF 3F                  test eax, 0x3fffffff
00239781  0F 85 21 04 00 00               jne 0x140239ba8
00239787  85 C0                           test eax, eax
00239789  0F 89 FA 04 00 00               jns 0x140239c89
0023978F  F6 05 70 D3 D8 00 01            test byte ptr [rip + 0xd8d370], 1
00239796  0F 85 2C 05 00 00               jne 0x140239cc8
0023979C  44 89 39                        mov dword ptr [rcx], r15d
0023979F  E9 70 FF FF FF                  jmp 0x140239714
002397A4  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002397AD  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002397B4  24 0F                           and al, 0xf
002397B6  0F 85 08 04 00 00               jne 0x140239bc4
002397BC  B9 30 00 00 00                  mov ecx, 0x30
002397C1  48 8D B2 40 9C 00 00            lea rsi, [rdx + 0x9c40]
002397C8  48 03 F1                        add rsi, rcx
002397CB  F6 05 34 D3 D8 00 01            test byte ptr [rip + 0xd8d334], 1
002397D2  0F 85 B0 03 00 00               jne 0x140239b88
002397D8  0F 0D 0E                        prefetchw byte ptr [rsi]
002397DB  48 8B 06                        mov rax, qword ptr [rsi]
002397DE  48 85 C0                        test rax, rax
002397E1  75 1A                           jne 0x1402397fd
002397E3  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
002397E7  48 8B C6                        mov rax, rsi
002397EA  F0 4C 0F B1 39                  lock cmpxchg qword ptr [rcx], r15
002397EF  0F 84 1F FF FF FF               je 0x140239714
002397F5  48 8B CE                        mov rcx, rsi
002397F8  E8 A3 E2 FD FF                  call 0x140217aa0
002397FD  48 8D 48 08                     lea rcx, [rax + 8]
00239801  4C 89 3E                        mov qword ptr [rsi], r15
00239804  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00239808  48 8B C2                        mov rax, rdx
0023980B  48 87 01                        xchg qword ptr [rcx], rax
0023980E  32 C2                           xor al, dl
00239810  A8 04                           test al, 4
00239812  0F 84 FC FE FF FF               je 0x140239714
00239818  E8 03 E4 FD FF                  call 0x140217c20
0023981D  E9 F2 FE FF FF                  jmp 0x140239714
00239822  48 8B C2                        mov rax, rdx
00239825  48 3B F0                        cmp rsi, rax
00239828  0F 82 D8 FE FF FF               jb 0x140239706
0023982E  49 8B C0                        mov rax, r8
00239831  48 3B F0                        cmp rsi, rax
00239834  0F 87 CC FE FF FF               ja 0x140239706
0023983A  48 8B C2                        mov rax, rdx
0023983D  48 2B F0                        sub rsi, rax
00239840  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00239847  48 C1 FE 03                     sar rsi, 3
0023984B  8D 14 36                        lea edx, [rsi + rsi]
0023984E  8B CA                           mov ecx, edx
00239850  8B C2                           mov eax, edx
00239852  83 E1 1F                        and ecx, 0x1f
00239855  41 D3 E4                        shl r12d, cl
00239858  41 F7 D4                        not r12d
0023985B  41 0F B3 CC                     btr r12d, ecx
0023985F  48 C1 E8 05                     shr rax, 5
00239863  F0 45 21 A4 81 6C 26 00 00      lock and dword ptr [r9 + rax*4 + 0x266c], r12d
0023986C  E9 A3 FE FF FF                  jmp 0x140239714
00239871  48 3B D8                        cmp rbx, rax
00239874  75 4B                           jne 0x1402398c1
00239876  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0023987F  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00239886  24 0F                           and al, 0xf
00239888  0F 85 D5 02 00 00               jne 0x140239b63
0023988E  41 8B CC                        mov ecx, r12d
00239891  49 8D 96 B0 00 00 00            lea rdx, [r14 + 0xb0]
00239898  8B C1                           mov eax, ecx
0023989A  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
002398A1  48 8D 0C 48                     lea rcx, [rax + rcx*2]
002398A5  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
002398A9  48 89 51 08                     mov qword ptr [rcx + 8], rdx
002398AD  4C 89 39                        mov qword ptr [rcx], r15
002398B0  90                              nop
002398B1  E8 D2 DA 03 00                  call 0x140277388
002398B6  41 B9 01 00 00 00               mov r9d, 1
002398BC  E9 34 01 00 00                  jmp 0x1402399f5
002398C1  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002398C8  A8 0F                           test al, 0xf
002398CA  75 37                           jne 0x140239903
002398CC  48 8B C2                        mov rax, rdx
002398CF  48 3B D8                        cmp rbx, rax
002398D2  72 2F                           jb 0x140239903
002398D4  49 8B C0                        mov rax, r8
002398D7  48 3B D8                        cmp rbx, rax
002398DA  77 27                           ja 0x140239903
002398DC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002398E5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002398EC  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
002398F3  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
002398FA  48 85 C9                        test rcx, rcx
002398FD  0F 85 A1 03 00 00               jne 0x140239ca4
00239903  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0023990A  A8 0F                           test al, 0xf
0023990C  74 14                           je 0x140239922
0023990E  48 8B C2                        mov rax, rdx
00239911  48 3B D8                        cmp rbx, rax
00239914  72 0C                           jb 0x140239922
00239916  49 8B C0                        mov rax, r8
00239919  48 3B D8                        cmp rbx, rax
0023991C  0F 86 80 01 00 00               jbe 0x140239aa2
00239922  48 8B 03                        mov rax, qword ptr [rbx]
00239925  48 8B CA                        mov rcx, rdx
00239928  48 3B D9                        cmp rbx, rcx
0023992B  72 7B                           jb 0x1402399a8
0023992D  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00239937  48 3B D9                        cmp rbx, rcx
0023993A  77 6C                           ja 0x1402399a8
0023993C  A8 01                           test al, 1
0023993E  74 68                           je 0x1402399a8
00239940  A8 42                           test al, 0x42
00239942  0F 95 C2                        setne dl
00239945  A8 20                           test al, 0x20
00239947  0F 95 C1                        setne cl
0023994A  84 D1                           test cl, dl
0023994C  75 5A                           jne 0x1402399a8
0023994E  48 F7 05 2F D1 D8 00 00 00 60 00  test qword ptr [rip + 0xd8d12f], 0x600000
00239959  74 4D                           je 0x1402399a8
0023995B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00239964  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0023996B  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00239972  74 34                           je 0x1402399a8
00239974  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
0023997B  4D 85 C0                        test r8, r8
0023997E  74 28                           je 0x1402399a8
00239980  48 8B CB                        mov rcx, rbx
00239983  48 C1 E9 03                     shr rcx, 3
00239987  81 E1 FF 01 00 00               and ecx, 0x1ff
0023998D  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
00239991  F6 C1 20                        test cl, 0x20
00239994  74 04                           je 0x14023999a
00239996  48 83 C8 20                     or rax, 0x20
0023999A  48 8B D0                        mov rdx, rax
0023999D  48 83 C8 42                     or rax, 0x42
002399A1  F6 C1 42                        test cl, 0x42
002399A4  48 0F 44 C2                     cmove rax, rdx
002399A8  41 B9 01 00 00 00               mov r9d, 1
002399AE  41 84 C1                        test r9b, al
002399B1  74 3F                           je 0x1402399f2
002399B3  48 0F BA E0 3C                  bt rax, 0x3c
002399B8  72 38                           jb 0x1402399f2
002399BA  48 BA FF FF FF FF FF FF FF DF   movabs rdx, 0xdfffffffffffffff
002399C4  48 8B C8                        mov rcx, rax
002399C7  48 23 CA                        and rcx, rdx
002399CA  48 BA 20 00 00 00 00 00 00 10   movabs rdx, 0x1000000000000020
002399D4  48 0B CA                        or rcx, rdx
002399D7  48 F7 05 A6 D0 D8 00 00 00 00 02  test qword ptr [rip + 0xd8d0a6], 0x2000000
002399E2  74 03                           je 0x1402399e7
002399E4  0F AE E8                        lfence
002399E7  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
002399EC  0F 84 A8 00 00 00               je 0x140239a9a
002399F2  41 8B C7                        mov eax, r15d
002399F5  85 C0                           test eax, eax
002399F7  0F 85 0C 01 00 00               jne 0x140239b09
002399FD  48 8D 5F 04                     lea rbx, [rdi + 4]
00239A01  45 85 ED                        test r13d, r13d
00239A04  74 16                           je 0x140239a1c
00239A06  8B 03                           mov eax, dword ptr [rbx]
00239A08  41 0F B6 CD                     movzx ecx, r13b
00239A0C  C1 E1 02                        shl ecx, 2
00239A0F  33 C8                           xor ecx, eax
00239A11  48 89 77 48                     mov qword ptr [rdi + 0x48], rsi
00239A15  83 E1 1C                        and ecx, 0x1c
00239A18  33 C8                           xor ecx, eax
00239A1A  89 0B                           mov dword ptr [rbx], ecx
00239A1C  48 8B 87 B0 00 00 00            mov rax, qword ptr [rdi + 0xb0]
00239A23  83 0B 20                        or dword ptr [rbx], 0x20
00239A26  48 85 C0                        test rax, rax
00239A29  74 4A                           je 0x140239a75
00239A2B  48 8D 0D DE F2 1E 00            lea rcx, [rip + 0x1ef2de]
00239A32  48 3B C1                        cmp rax, rcx
00239A35  0F 85 EE 00 00 00               jne 0x140239b29
00239A3B  48 8B B7 B8 00 00 00            mov rsi, qword ptr [rdi + 0xb8]
00239A42  8B 06                           mov eax, dword ptr [rsi]
00239A44  A8 03                           test al, 3
00239A46  0F 84 ED 01 00 00               je 0x140239c39
00239A4C  48 8D 05 AD 43 25 00            lea rax, [rip + 0x2543ad]
00239A53  45 33 C0                        xor r8d, r8d
00239A56  48 8D 56 38                     lea rdx, [rsi + 0x38]
00239A5A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00239A5F  48 8B CF                        mov rcx, rdi
00239A62  E8 29 04 00 00                  call 0x140239e90
00239A67  8B 03                           mov eax, dword ptr [rbx]
00239A69  A8 20                           test al, 0x20
00239A6B  74 04                           je 0x140239a71
00239A6D  C6 46 06 01                     mov byte ptr [rsi + 6], 1
00239A71  48 8D 5F 04                     lea rbx, [rdi + 4]
00239A75  41 8B F7                        mov esi, r15d
00239A78  8B 03                           mov eax, dword ptr [rbx]
00239A7A  83 E0 DF                        and eax, 0xffffffdf
00239A7D  89 03                           mov dword ptr [rbx], eax
00239A7F  A8 01                           test al, 1
00239A81  75 09                           jne 0x140239a8c
00239A83  83 FE 04                        cmp esi, 4
00239A86  0F 8C 50 01 00 00               jl 0x140239bdc
00239A8C  83 FE 05                        cmp esi, 5
00239A8F  8B C6                           mov eax, esi
00239A91  41 0F 45 C4                     cmovne eax, r12d
00239A95  E9 80 FC FF FF                  jmp 0x14023971a
00239A9A  41 8B C1                        mov eax, r9d
00239A9D  E9 53 FF FF FF                  jmp 0x1402399f5
00239AA2  48 8B C2                        mov rax, rdx
00239AA5  48 8B CB                        mov rcx, rbx
00239AA8  48 2B C8                        sub rcx, rax
00239AAB  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00239AB2  48 C1 F9 03                     sar rcx, 3
00239AB6  03 C9                           add ecx, ecx
00239AB8  8B C1                           mov eax, ecx
00239ABA  8B D1                           mov edx, ecx
00239ABC  48 C1 E8 05                     shr rax, 5
00239AC0  83 E2 1F                        and edx, 0x1f
00239AC3  8B CA                           mov ecx, edx
00239AC5  4D 8D 14 81                     lea r10, [r9 + rax*4]
00239AC9  41 B9 01 00 00 00               mov r9d, 1
00239ACF  45 8B 9A 6C 26 00 00            mov r11d, dword ptr [r10 + 0x266c]
00239AD6  41 8B C3                        mov eax, r11d
00239AD9  D3 E8                           shr eax, cl
00239ADB  41 84 C1                        test r9b, al
00239ADE  0F 85 19 FF FF FF               jne 0x1402399fd
00239AE4  45 8B C1                        mov r8d, r9d
00239AE7  41 8B D4                        mov edx, r12d
00239AEA  41 D3 E0                        shl r8d, cl
00239AED  41 8B C3                        mov eax, r11d
00239AF0  D3 E2                           shl edx, cl
00239AF2  45 0B C3                        or r8d, r11d
00239AF5  F7 D2                           not edx
00239AF7  44 23 C2                        and r8d, edx
00239AFA  F0 45 0F B1 82 6C 26 00 00      lock cmpxchg dword ptr [r10 + 0x266c], r8d
00239B03  0F 85 F4 FE FF FF               jne 0x1402399fd
00239B09  48 BA 00 D0 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed000
00239B13  4C 8D 0D 26 30 BF 00            lea r9, [rip + 0xbf3026]
00239B1A  49 B8 FF DF BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbedfff
00239B24  E9 B7 FB FF FF                  jmp 0x1402396e0
00239B29  48 8D 0D D0 F0 1E 00            lea rcx, [rip + 0x1ef0d0]
00239B30  48 3B C1                        cmp rax, rcx
00239B33  0F 85 26 01 00 00               jne 0x140239c5f
00239B39  48 8B 97 B8 00 00 00            mov rdx, qword ptr [rdi + 0xb8]
00239B40  48 8D 05 09 34 26 00            lea rax, [rip + 0x263409]
00239B47  48 83 C2 30                     add rdx, 0x30
00239B4B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00239B50  45 33 C9                        xor r9d, r9d
00239B53  45 33 C0                        xor r8d, r8d
00239B56  48 8B CF                        mov rcx, rdi
00239B59  E8 32 03 00 00                  call 0x140239e90
00239B5E  E9 12 FF FF FF                  jmp 0x140239a75
00239B63  3C 07                           cmp al, 7
00239B65  0F 84 8E 00 00 00               je 0x140239bf9
00239B6B  3C 05                           cmp al, 5
00239B6D  B9 03 00 00 00                  mov ecx, 3
00239B72  41 0F 44 CF                     cmove ecx, r15d
00239B76  8B D1                           mov edx, ecx
00239B78  48 81 C2 50 06 00 00            add rdx, 0x650
00239B7F  49 8D 14 D1                     lea rdx, [r9 + rdx*8]
00239B83  E9 10 FD FF FF                  jmp 0x140239898
00239B88  8B 05 CA 42 CD 00               mov eax, dword ptr [rip + 0xcd42ca]
00239B8E  85 C0                           test eax, eax
00239B90  0F 85 42 FC FF FF               jne 0x1402397d8
00239B96  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00239B9B  48 8B CE                        mov rcx, rsi
00239B9E  E8 4D DE FD FF                  call 0x1402179f0
00239BA3  E9 6C FB FF FF                  jmp 0x140239714
00239BA8  F6 05 57 CF D8 00 01            test byte ptr [rip + 0xd8cf57], 1
00239BAF  0F 85 30 01 00 00               jne 0x140239ce5
00239BB5  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
00239BBC  F0 FF 09                        lock dec dword ptr [rcx]
00239BBF  E9 50 FB FF FF                  jmp 0x140239714
00239BC4  3C 07                           cmp al, 7
00239BC6  0F 84 89 00 00 00               je 0x140239c55
00239BCC  3C 05                           cmp al, 5
00239BCE  B9 48 00 00 00                  mov ecx, 0x48
00239BD3  49 0F 44 CF                     cmove rcx, r15
00239BD7  E9 E5 FB FF FF                  jmp 0x1402397c1
00239BDC  8B 0F                           mov ecx, dword ptr [rdi]
00239BDE  F6 C1 02                        test cl, 2
00239BE1  74 2D                           je 0x140239c10
00239BE3  48 8B CF                        mov rcx, rdi
00239BE6  E8 E5 03 00 00                  call 0x140239fd0
00239BEB  83 FE 05                        cmp esi, 5
00239BEE  8B C6                           mov eax, esi
00239BF0  41 0F 45 C4                     cmovne eax, r12d
00239BF4  E9 21 FB FF FF                  jmp 0x14023971a
00239BF9  B9 01 00 00 00                  mov ecx, 1
00239BFE  8B D1                           mov edx, ecx
00239C00  48 81 C2 50 06 00 00            add rdx, 0x650
00239C07  49 8D 14 D1                     lea rdx, [r9 + rdx*8]
00239C0B  E9 88 FC FF FF                  jmp 0x140239898
00239C10  48 8B 57 38                     mov rdx, qword ptr [rdi + 0x38]
00239C14  48 85 D2                        test rdx, rdx
00239C17  0F 84 6F FE FF FF               je 0x140239a8c
00239C1D  83 C8 02                        or eax, 2
00239C20  89 03                           mov dword ptr [rbx], eax
00239C22  0F BA E1 0C                     bt ecx, 0xc
00239C26  73 56                           jae 0x140239c7e
00239C28  48 8B C5                        mov rax, rbp
00239C2B  48 3B D0                        cmp rdx, rax
00239C2E  75 4E                           jne 0x140239c7e
00239C30  4C 89 7F 38                     mov qword ptr [rdi + 0x38], r15
00239C34  E9 53 FE FF FF                  jmp 0x140239a8c
00239C39  48 8D 05 00 31 27 00            lea rax, [rip + 0x273100]
00239C40  48 39 87 A8 00 00 00            cmp qword ptr [rdi + 0xa8], rax
00239C47  0F 84 FF FD FF FF               je 0x140239a4c
00239C4D  45 8B CF                        mov r9d, r15d
00239C50  E9 F7 FD FF FF                  jmp 0x140239a4c
00239C55  B9 18 00 00 00                  mov ecx, 0x18
00239C5A  E9 62 FB FF FF                  jmp 0x1402397c1
00239C5F  48 8D 0D 8A A2 23 00            lea rcx, [rip + 0x23a28a]
00239C66  48 3B C1                        cmp rax, rcx
00239C69  48 8B CF                        mov rcx, rdi
00239C6C  0F 85 90 00 00 00               jne 0x140239d02
00239C72  E8 79 A2 23 00                  call 0x140473ef0
00239C77  8B F0                           mov esi, eax
00239C79  E9 FA FD FF FF                  jmp 0x140239a78
00239C7E  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00239C82  E8 39 D2 FD FF                  call 0x140216ec0
00239C87  EB A7                           jmp 0x140239c30
00239C89  45 33 C9                        xor r9d, r9d
00239C8C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00239C91  48 8B D1                        mov rdx, rcx
00239C94  41 B8 00 01 00 00               mov r8d, 0x100
00239C9A  41 8D 49 10                     lea ecx, [r9 + 0x10]
00239C9E  E8 BD 39 2C 00                  call 0x1404fd660
00239CA3  CC                              int3
00239CA4  8B C3                           mov eax, ebx
00239CA6  C1 E8 03                        shr eax, 3
00239CA9  25 FF 01 00 00                  and eax, 0x1ff
00239CAE  48 8D 0C 81                     lea rcx, [rcx + rax*4]
00239CB2  E8 49 1B 08 00                  call 0x1402bb800
00239CB7  85 C0                           test eax, eax
00239CB9  0F 85 4A FE FF FF               jne 0x140239b09
00239CBF  44 8D 48 01                     lea r9d, [rax + 1]
00239CC3  E9 35 FD FF FF                  jmp 0x1402399fd
00239CC8  8B 05 8A 41 CD 00               mov eax, dword ptr [rip + 0xcd418a]
00239CCE  85 C0                           test eax, eax
00239CD0  0F 85 C6 FA FF FF               jne 0x14023979c
00239CD6  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00239CDB  E8 64 72 08 00                  call 0x1402c0f44
00239CE0  E9 2F FA FF FF                  jmp 0x140239714
00239CE5  8B 05 6D 41 CD 00               mov eax, dword ptr [rip + 0xcd416d]
00239CEB  85 C0                           test eax, eax
00239CED  0F 85 C2 FE FF FF               jne 0x140239bb5
00239CF3  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00239CF8  E8 4B 72 0B 00                  call 0x1402f0f48
00239CFD  E9 12 FA FF FF                  jmp 0x140239714
00239D02  E8 C9 0D 48 00                  call 0x1406baad0
00239D07  8B F0                           mov esi, eax
00239D09  E9 6A FD FF FF                  jmp 0x140239a78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReacquireHigherPageTableLock(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p58;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rbx = (a2) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (result);
    v_r15 = 0;
    if (((*(unsigned int *)(a1)) & (0x1000ULL)) == 0) goto loc_00239871;
    if (v_rbx != v_rbp) goto loc_002398C1;
loc_002396E0:
    if (a2 == v_rbp) goto loc_002397A4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) == 0) goto loc_00239738;
loc_002396F7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) != 0) goto loc_00239822;
loc_00239706:
loc_00239714:
    *(unsigned __int64 *)(a1 + 56) = v_rbx;
    result = 0;
loc_0023971A:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00239738:
    if (v_stack_p20 < a2) goto loc_002396F7;
    if (v_stack_p20 > a3) goto loc_002396F7;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_002396F7;
    v_rsi = (v_stack_p20) >> (3);
    v_rsi = (unsigned int)((v_rsi) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_rsi * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_00239BA8;
    if (!sign_flag) goto loc_00239C89;
    if (((*(unsigned __int8 *)(v_rip + 14209904)) & (1)) != 0) goto loc_00239CC8;
loc_0023979C:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_rsi * 4) = 0;
    goto loc_00239714;
loc_002397A4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (condition_is_not_equal) goto loc_00239BC4;
loc_002397C1:
    v_rsi = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 14209844)) & (1)) != 0) goto loc_00239B88;
loc_002397D8:
    if (*(unsigned __int64 *)(v_rsi) != 0) goto loc_002397FD;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00239714;
    result = KxWaitForLockChainValid(v_rsi, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, v_rip + 12530808);
loc_002397FD:
    *(unsigned __int64 *)(v_rsi) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rsi + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00239714;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rsi + 8), a3, v_rip + 12530808);
    goto loc_00239714;
loc_00239822:
    if (v_rsi < (*(unsigned __int64 *)(v_rsi + 8))) goto loc_00239706;
    if (v_rsi > a3) goto loc_00239706;
    v_rsi = (v_rsi) - (*(unsigned __int64 *)(v_rsi + 8));
    v_rsi = (v_rsi) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) & (31));
    v_r12 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    v_r12 = (unsigned int)(~(v_r12));
    result = ((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) >> (5);
    goto loc_00239714;
loc_00239871:
    if (v_stack_p10 != result) goto loc_002398C1;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (condition_is_not_equal) goto loc_00239B63;
loc_00239898:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + 2500 * 2 * 8 + 8) = *(unsigned __int64 *)(a1 + 32) + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + 2500 * 2 * 8) = 0;
    result = KxTryToAcquireQueuedSpinLock(*(unsigned __int64 *)(gs_base + (0 + 32)) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + 2500 * 2 * 8, *(unsigned __int64 *)(a1 + 32) + 176, *(unsigned __int64 *)(gs_base + (0 + 32)), v_rip + 12530808);
    goto loc_002399F5;
loc_002398C1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) != 0) goto loc_00239903;
    if (v_stack_p10 < (*(unsigned __int64 *)(a1 + 32) + 176)) goto loc_00239903;
    if (v_stack_p10 > (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00239903;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_00239CA4;
loc_00239903:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184)))) & (15)) == 0) goto loc_00239922;
    if (v_stack_p10 < (*(unsigned __int64 *)(a1 + 32) + 176)) goto loc_00239922;
    if (v_stack_p10 <= (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00239AA2;
loc_00239922:
    if (v_stack_p10 < (*(unsigned __int64 *)(a1 + 32) + 176)) goto loc_002399A8;
    if (v_stack_p10 > (*(unsigned __int64 *)(a1 + 32) + 176)) goto loc_002399A8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (1)) == 0) goto loc_002399A8;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) != 0) goto loc_002399A8;
    if (((*(unsigned __int64 *)(v_rip + 14209327)) & (0x600000ULL)) == 0) goto loc_002399A8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002399A8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002399A8;
    a1 = (v_stack_p10) >> (3);
    a1 = (unsigned int)((a1) & (511));
    result = *(unsigned __int64 *)(v_stack_p10);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (*(unsigned __int64 *)(v_stack_p10)) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
loc_002399A8:
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_002399F2;
    if (condition_is_below) goto loc_002399F2;
    a1 = (result) & (result);
    a1 = (a1) | (result);
    if (((*(unsigned __int64 *)(v_rip + 14209190)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14209190)) & (0x2000000ULL)) == 0) goto loc_00239A9A;
loc_002399F2:
loc_002399F5:
    if (0 != 0) goto loc_00239B09;
loc_002399FD:
    result = 0;
    if ((unsigned int)((unsigned int)(a3)) != 0) {
        result = *(unsigned int *)(a1 + 4);
        a1 = (unsigned __int8)((unsigned int)(a3));
        a1 = (unsigned int)((a1) << (2));
        a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
        *(unsigned __int64 *)(a1 + 72) = v_rsi;
        a1 = (unsigned int)((a1) & (28));
        a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
        *(unsigned int *)(a1 + 4) = (unsigned int)(a1);
    }
    if (*(unsigned __int64 *)(a1 + 176) == 0) goto loc_00239A75;
    if ((*(unsigned __int64 *)(a1 + 176)) != (v_rip + 2028254)) goto loc_00239B29;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184))))) & (3)) == 0) goto loc_00239C39;
loc_00239A4C:
    a3 = 0;
    v_stack_p20 = v_rip + 2442157;
    result = MiAgeTrimListsTail(a1, *(unsigned __int64 *)(a1 + 184) + 56, a3, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 184) + 6) = 1;
    }
loc_00239A75:
loc_00239A78:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (0xFFFFFFDFULL));
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00239A8C;
    if (0 < 4) goto loc_00239BDC;
loc_00239A8C:
    result = 0;
    if (0 != 5) { result = (unsigned int)(v_r12); }
    goto loc_0023971A;
loc_00239A9A:
    goto loc_002399F5;
loc_00239AA2:
    a1 = (a1 + 4) - (*(unsigned __int64 *)(a1 + 184) + 56);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    result = ((unsigned int)((unsigned int)(a1))) >> (5);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1 + result * 4 + 9836))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_002399FD;
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    a3 = (unsigned int)((a3) | ((unsigned int)((unsigned int)(*(unsigned int *)(1 + result * 4 + 9836)))));
    a2 = (unsigned int)(~(a2));
    a3 = (unsigned int)((a3) & ((unsigned int)(a2)));
    if (condition_is_not_equal) goto loc_002399FD;
loc_00239B09:
    goto loc_002396E0;
loc_00239B29:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1 + result * 4 + 9836))))) != (v_rip + 2027728)) goto loc_00239C5F;
    a2 = (*(unsigned __int64 *)(a1 + 184)) + (48);
    v_stack_p20 = v_rip + 2503689;
    a4 = 0;
    a3 = 0;
    result = MiAgeTrimListsTail(a1, a2, a3, a4);
    goto loc_00239A75;
loc_00239B63:
    if (((unsigned __int8)(result)) == 7) goto loc_00239BF9;
    a1 = 3;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    a2 = ((unsigned int)((unsigned int)(a1))) + (0x650ULL);
    goto loc_00239898;
loc_00239B88:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13451978))) != 0) goto loc_002397D8;
    result = KiReleaseQueuedSpinLockInstrumented(0, v_stack_p58, a3, a4);
    goto loc_00239714;
loc_00239BA8:
    if (((*(unsigned __int8 *)(v_rip + 14208855)) & (1)) != 0) goto loc_00239CE5;
loc_00239BB5:
    goto loc_00239714;
loc_00239BC4:
    if (((unsigned __int8)(result)) == 7) goto loc_00239C55;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    goto loc_002397C1;
loc_00239BDC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_00239C10;
    result = MiReleaseWalkLocks(a1, v_stack_p58, a3, a4);
    result = 0;
    if (0 != 5) { result = (unsigned int)(v_r12); }
    goto loc_0023971A;
loc_00239BF9:
    a2 = (1) + (0x650ULL);
    goto loc_00239898;
loc_00239C10:
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_00239A8C;
    result = (unsigned int)((result) | (2));
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_00239C7E;
    if ((*(unsigned __int64 *)(a1 + 56)) != v_stack_p18) goto loc_00239C7E;
loc_00239C30:
    *(unsigned __int64 *)(a1 + 56) = 0;
    goto loc_00239A8C;
loc_00239C39:
    if ((*(unsigned __int64 *)(a1 + 168)) == (v_rip + 2568448)) goto loc_00239A4C;
    goto loc_00239A4C;
loc_00239C55:
    goto loc_002397C1;
loc_00239C5F:
    if ((v_rip + 2568448) != (v_rip + 2335370)) goto loc_00239D02;
    result = MiDeleteVaTail(a1, *(unsigned __int64 *)(a1 + 56), a3, 0);
    goto loc_00239A78;
loc_00239C7E:
    result = MiUnlockPageTable(*(unsigned __int64 *)(a1 + 32), *(unsigned __int64 *)(a1 + 56), a3, 0);
    goto loc_00239C30;
loc_00239C89:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 16, *(unsigned __int64 *)(a1 + 32), 256, a4);
loc_00239CA4:
    result = (unsigned int)(((unsigned int)((unsigned int)(a1 + 4))) >> (3));
    result = (unsigned int)((result) & (511));
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(a4 + 16 + result * 4, *(unsigned __int64 *)(a1 + 32), 256, a4);
    if ((unsigned int)(result) != 0) goto loc_00239B09;
    goto loc_002399FD;
loc_00239CC8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13451658))) != 0) goto loc_0023979C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239714;
loc_00239CE5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13451629))) != 0) goto loc_00239BB5;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239714;
loc_00239D02:
    result = guard_dispatch_icall(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239A78;
}
```

## 5. (Beta) C Style

```c
int64_t MiReacquireHigherPageTableLock(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p58;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rbx = (Arg2) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (result);
    local_r15 = 0;
    if (((*(uint32_t *)(arg1)) & (0x1000ULL)) == 0) goto loc_00239871;
    if (local_rbx != local_rbp) goto loc_002398C1;
loc_002396E0:
    if (Arg2 == local_rbp) goto loc_002397A4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) == 0) goto loc_00239738;
loc_002396F7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00239822;
loc_00239706:
loc_00239714:
    *(uint64_t *)(arg1 + 0x38) = local_rbx;
    result = 0;
loc_0023971A:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00239738:
    if (v_stack_p20 < Arg2) goto loc_002396F7;
    if (v_stack_p20 > Arg3) goto loc_002396F7;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_002396F7;
    local_rsi = (v_stack_p20) >> (3);
    local_rsi = (uint32_t)((local_rsi) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_rsi * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_00239BA8;
    if (!sign_flag) goto loc_00239C89;
    if (((*(uint8_t *)(v_rip + 0xD8D370)) & (1)) != 0) goto loc_00239CC8;
loc_0023979C:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_rsi * 4) = 0;
    goto loc_00239714;
loc_002397A4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00239BC4;
loc_002397C1:
    local_rsi = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD8D334)) & (1)) != 0) goto loc_00239B88;
loc_002397D8:
    if (*(uint64_t *)(local_rsi) != 0) goto loc_002397FD;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00239714;
    result = KxWaitForLockChainValid(local_rsi, *(uint64_t *)(gs_base + (0 + 0x20)), Arg3, v_rip + 12530808);
loc_002397FD:
    *(uint64_t *)(local_rsi) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rsi + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rsi + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00239714;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rsi + 0x8), Arg3, v_rip + 12530808);
    goto loc_00239714;
loc_00239822:
    if (local_rsi < (*(uint64_t *)(local_rsi + 0x8))) goto loc_00239706;
    if (local_rsi > Arg3) goto loc_00239706;
    local_rsi = (local_rsi) - (*(uint64_t *)(local_rsi + 0x8));
    local_rsi = (local_rsi) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) & (31));
    local_r12 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    local_r12 = (uint32_t)(~(local_r12));
    result = ((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) >> (5);
    goto loc_00239714;
loc_00239871:
    if (v_stack_p10 != result) goto loc_002398C1;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00239B63;
loc_00239898:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + 0x9C4 * 2 * 8 + 0x8) = *(uint64_t *)(arg1 + 0x20) + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + 0x9C4 * 2 * 8) = 0;
    result = KxTryToAcquireQueuedSpinLock(*(uint64_t *)(gs_base + (0 + 0x20)) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + 2500 * 2 * 8, *(uint64_t *)(arg1 + 0x20) + 176, *(uint64_t *)(gs_base + (0 + 0x20)), v_rip + 12530808);
    goto loc_002399F5;
loc_002398C1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) != 0) goto loc_00239903;
    if (v_stack_p10 < (*(uint64_t *)(arg1 + 0x20) + 176)) goto loc_00239903;
    if (v_stack_p10 > (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00239903;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_00239CA4;
loc_00239903:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8)))) & (15)) == 0) goto loc_00239922;
    if (v_stack_p10 < (*(uint64_t *)(arg1 + 0x20) + 176)) goto loc_00239922;
    if (v_stack_p10 <= (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00239AA2;
loc_00239922:
    if (v_stack_p10 < (*(uint64_t *)(arg1 + 0x20) + 176)) goto loc_002399A8;
    if (v_stack_p10 > (*(uint64_t *)(arg1 + 0x20) + 176)) goto loc_002399A8;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (1)) == 0) goto loc_002399A8;
    Arg2 = ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_p10))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) != 0) goto loc_002399A8;
    if (((*(uint64_t *)(v_rip + 0xD8D12F)) & (0x600000ULL)) == 0) goto loc_002399A8;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002399A8;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002399A8;
    Arg1 = (v_stack_p10) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    result = *(uint64_t *)(v_stack_p10);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (*(uint64_t *)(v_stack_p10)) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { result = result; }
loc_002399A8:
    if (((1) & ((uint8_t)(result))) == 0) goto loc_002399F2;
    if (condition_is_below) goto loc_002399F2;
    Arg1 = (result) & (result);
    Arg1 = (Arg1) | (result);
    if (((*(uint64_t *)(v_rip + 0xD8D0A6)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD8D0A6)) & (0x2000000ULL)) == 0) goto loc_00239A9A;
loc_002399F2:
loc_002399F5:
    if (0 != 0) goto loc_00239B09;
loc_002399FD:
    result = 0;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) {
        result = *(uint32_t *)(arg1 + 0x4);
        Arg1 = (uint8_t)((uint32_t)(Arg3));
        Arg1 = (uint32_t)((Arg1) << (2));
        Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
        *(uint64_t *)(arg1 + 0x48) = local_rsi;
        Arg1 = (uint32_t)((Arg1) & (28));
        Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
        *(uint32_t *)(arg1 + 0x4) = (uint32_t)(Arg1);
    }
    if (*(uint64_t *)(arg1 + 0xB0) == 0) goto loc_00239A75;
    if ((*(uint64_t *)(arg1 + 0xB0)) != (v_rip + 2028254)) goto loc_00239B29;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8))))) & (3)) == 0) goto loc_00239C39;
loc_00239A4C:
    Arg3 = 0;
    v_stack_p20 = v_rip + 2442157;
    result = MiAgeTrimListsTail(Arg1, *(uint64_t *)(arg1 + 0xB8) + 56, Arg3, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (32)) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x6) = 1;
    }
loc_00239A75:
loc_00239A78:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (0xFFFFFFDFULL));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00239A8C;
    if (0 < 4) goto loc_00239BDC;
loc_00239A8C:
    result = 0;
    if (0 != 5) { result = (uint32_t)(local_r12); }
    goto loc_0023971A;
loc_00239A9A:
    goto loc_002399F5;
loc_00239AA2:
    Arg1 = (Arg1 + 4) - (*(uint64_t *)(arg1 + 0xB8) + 56);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    result = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1 + result * 4 + 0x266C))))) >> ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    if (((1) & ((uint8_t)(result))) != 0) goto loc_002399FD;
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)((uint32_t)(*(uint32_t *)(1 + result * 4 + 0x266C)))));
    Arg2 = (uint32_t)(~(Arg2));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)(Arg2)));
    if (condition_is_not_equal) goto loc_002399FD;
loc_00239B09:
    goto loc_002396E0;
loc_00239B29:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1 + result * 4 + 0x266C))))) != (v_rip + 2027728)) goto loc_00239C5F;
    Arg2 = (*(uint64_t *)(arg1 + 0xB8)) + (48);
    v_stack_p20 = v_rip + 2503689;
    a4 = 0;
    Arg3 = 0;
    result = MiAgeTrimListsTail(Arg1, Arg2, Arg3, a4);
    goto loc_00239A75;
loc_00239B63:
    if (((uint8_t)(result)) == 7) goto loc_00239BF9;
    Arg1 = 3;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (0x650ULL);
    goto loc_00239898;
loc_00239B88:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD42CA))) != 0) goto loc_002397D8;
    result = KiReleaseQueuedSpinLockInstrumented(0, v_stack_p58, Arg3, a4);
    goto loc_00239714;
loc_00239BA8:
    if (((*(uint8_t *)(v_rip + 0xD8CF57)) & (1)) != 0) goto loc_00239CE5;
loc_00239BB5:
    goto loc_00239714;
loc_00239BC4:
    if (((uint8_t)(result)) == 7) goto loc_00239C55;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    goto loc_002397C1;
loc_00239BDC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_00239C10;
    result = MiReleaseWalkLocks(Arg1, v_stack_p58, Arg3, a4);
    result = 0;
    if (0 != 5) { result = (uint32_t)(local_r12); }
    goto loc_0023971A;
loc_00239BF9:
    Arg2 = (1) + (0x650ULL);
    goto loc_00239898;
loc_00239C10:
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_00239A8C;
    result = (uint32_t)((result) | (2));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_00239C7E;
    if ((*(uint64_t *)(arg1 + 0x38)) != v_stack_p18) goto loc_00239C7E;
loc_00239C30:
    *(uint64_t *)(arg1 + 0x38) = 0;
    goto loc_00239A8C;
loc_00239C39:
    if ((*(uint64_t *)(arg1 + 0xA8)) == (v_rip + 2568448)) goto loc_00239A4C;
    goto loc_00239A4C;
loc_00239C55:
    goto loc_002397C1;
loc_00239C5F:
    if ((v_rip + 2568448) != (v_rip + 2335370)) goto loc_00239D02;
    result = MiDeleteVaTail(Arg1, *(uint64_t *)(arg1 + 0x38), Arg3, 0);
    goto loc_00239A78;
loc_00239C7E:
    result = MiUnlockPageTable(*(uint64_t *)(arg1 + 0x20), *(uint64_t *)(arg1 + 0x38), Arg3, 0);
    goto loc_00239C30;
loc_00239C89:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 16, *(uint64_t *)(arg1 + 0x20), 256, a4);
loc_00239CA4:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1 + 4))) >> (3));
    result = (uint32_t)((result) & (511));
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(a4 + 16 + result * 4, *(uint64_t *)(arg1 + 0x20), 256, a4);
    if ((uint32_t)(result) != 0) goto loc_00239B09;
    goto loc_002399FD;
loc_00239CC8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD418A))) != 0) goto loc_0023979C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239714;
loc_00239CE5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD416D))) != 0) goto loc_00239BB5;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239714;
loc_00239D02:
    result = guard_dispatch_icall(a4 + 16 + result * 4, v_stack_p58, 256, result + 1);
    goto loc_00239A78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00239650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
