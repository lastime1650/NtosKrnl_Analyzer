# KiSendHeteroRescheduleIntRequestHelper

- RVA: `0x0035420C`–`0x0035487E` (길이 `1,650` bytes)
- VA: `0x000000014035420C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000791AC`
- 디코드: `425`개 명령, `1,650/1,650` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00354306` → [KiCheckPreferredHeteroProcessor](../39/KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x0035438C` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x003543D2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003543E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00354474` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x003544AF` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x003544D0` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00354519` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x00354560` → [Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline](Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline_function_00355C60.md) (function, `0x00355C60`)
- `0x0035459D` → [KiCheckPreferredHeteroProcessor](../39/KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x003545F3` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x0035466E` → [KiCheckPreferredHeteroProcessor](../39/KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x003546B4` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x00354725` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0035473B` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x00354755` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00354764` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00354814` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00354835` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0035486D` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)

### Direct callers
- [KiSendHeteroRescheduleIntRequest](KiSendHeteroRescheduleIntRequest_function_00354120.md) at `0x003541B1`
- [KiSendHeteroRescheduleIntRequest](KiSendHeteroRescheduleIntRequest_function_00354120.md) at `0x003541DA`
- [KiSendHeteroRescheduleIntRequest](KiSendHeteroRescheduleIntRequest_function_00354120.md) at `0x003541F7`

### Static image references
- `0x00354231` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00354283` → RVA `0x00F231B8` (`.data`; read)
- `0x003542AA` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003542F5` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x003543C4` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00354789` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0035485B` → [sub_006E2730](../6E/Unknown_function_006E2730.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035420C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00354211  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00354216  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0035421B  55                              push rbp
0035421C  56                              push rsi
0035421D  57                              push rdi
0035421E  41 54                           push r12
00354220  41 55                           push r13
00354222  41 56                           push r14
00354224  41 57                           push r15
00354226  48 8B EC                        mov rbp, rsp
00354229  48 83 EC 70                     sub rsp, 0x70
0035422D  83 4D C4 FF                     or dword ptr [rbp - 0x3c], 0xffffffff
00354231  48 8D 3D 08 4A C7 00            lea rdi, [rip + 0xc74a08]
00354238  33 F6                           xor esi, esi
0035423A  0F 57 C0                        xorps xmm0, xmm0
0035423D  89 75 C8                        mov dword ptr [rbp - 0x38], esi
00354240  4D 8B F9                        mov r15, r9
00354243  49 8B D8                        mov rbx, r8
00354246  4C 8B F2                        mov r14, rdx
00354249  4C 8B D1                        mov r10, rcx
0035424C  44 8B EE                        mov r13d, esi
0035424F  44 8A E6                        mov r12b, sil
00354252  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00354256  48 85 C9                        test rcx, rcx
00354259  0F 84 26 01 00 00               je 0x140354385
0035425F  49 0F BC CA                     bsf rcx, r10
00354263  41 BE 01 00 00 00               mov r14d, 1
00354269  8B C1                           mov eax, ecx
0035426B  49 0F BB C2                     btc r10, rax
0035426F  89 4D C0                        mov dword ptr [rbp - 0x40], ecx
00354272  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
0035427A  C1 E0 06                        shl eax, 6
0035427D  03 C8                           add ecx, eax
0035427F  4C 89 55 40                     mov qword ptr [rbp + 0x40], r10
00354283  48 8B 05 2E EF BC 00            mov rax, qword ptr [rip + 0xbcef2e]
0035428A  8B 34 88                        mov esi, dword ptr [rax + rcx*4]
0035428D  48 8B 3C F7                     mov rdi, qword ptr [rdi + rsi*8]
00354291  48 8B C7                        mov rax, rdi
00354294  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00354298  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0035429C  33 DB                           xor ebx, ebx
0035429E  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
003542A5  73 1C                           jae 0x1403542c3
003542A7  41 03 DE                        add ebx, r14d
003542AA  85 1D FC 0F C7 00               test dword ptr [rip + 0xc70ffc], ebx
003542B0  0F 84 0E 01 00 00               je 0x1403543c4
003542B6  F3 90                           pause
003542B8  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
003542BC  48 85 C0                        test rax, rax
003542BF  74 DD                           je 0x14035429e
003542C1  EB E4                           jmp 0x1403542a7
003542C3  44 84 77 23                     test byte ptr [rdi + 0x23], r14b
003542C7  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
003542CB  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
003542CF  0F 84 16 01 00 00               je 0x1403543eb
003542D5  48 83 7F 10 00                  cmp qword ptr [rdi + 0x10], 0
003542DA  0F 85 0B 01 00 00               jne 0x1403543eb
003542E0  8A 87 B9 38 00 00               mov al, byte ptr [rdi + 0x38b9]
003542E6  84 C0                           test al, al
003542E8  75 29                           jne 0x140354313
003542EA  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
003542ED  8B 43 54                        mov eax, dword ptr [rbx + 0x54]
003542F0  3B C8                           cmp ecx, eax
003542F2  0F 46 C8                        cmovbe ecx, eax
003542F5  3B 0D 81 10 C7 00               cmp ecx, dword ptr [rip + 0xc71081]
003542FB  72 16                           jb 0x140354313
003542FD  45 33 C0                        xor r8d, r8d
00354300  48 8B D7                        mov rdx, rdi
00354303  48 8B CB                        mov rcx, rbx
00354306  E8 21 94 04 00                  call 0x14039d72c
0035430B  85 C0                           test eax, eax
0035430D  0F 85 45 01 00 00               jne 0x140354458
00354313  33 F6                           xor esi, esi
00354315  41 BA 01 00 00 00               mov r10d, 1
0035431B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0035431F  48 85 C0                        test rax, rax
00354322  74 49                           je 0x14035436d
00354324  4C 8B C0                        mov r8, rax
00354327  4C 8B CE                        mov r9, rsi
0035432A  49 83 E0 FE                     and r8, 0xfffffffffffffffe
0035432E  8B D6                           mov edx, esi
00354330  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
00354334  41 23 C2                        and eax, r10d
00354337  0F 84 06 01 00 00               je 0x140354443
0035433D  83 F8 01                        cmp eax, 1
00354340  75 15                           jne 0x140354357
00354342  49 8B 80 58 8E 00 00            mov rax, qword ptr [r8 + 0x8e58]
00354349  4D 8B 88 58 8E 00 00            mov r9, qword ptr [r8 + 0x8e58]
00354350  49 83 C1 08                     add r9, 8
00354354  0F B6 10                        movzx edx, byte ptr [rax]
00354357  85 D2                           test edx, edx
00354359  74 12                           je 0x14035436d
0035435B  8D 42 FF                        lea eax, [rdx - 1]
0035435E  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
00354362  8B D0                           mov edx, eax
00354364  F0 48 21 71 30                  lock and qword ptr [rcx + 0x30], rsi
00354369  85 C0                           test eax, eax
0035436B  75 EE                           jne 0x14035435b
0035436D  4C 8B 55 40                     mov r10, qword ptr [rbp + 0x40]
00354371  48 8D 3D C8 48 C7 00            lea rdi, [rip + 0xc748c8]
00354378  4D 85 D2                        test r10, r10
0035437B  0F 85 DE FE FF FF               jne 0x14035425f
00354381  48 8B 5D 50                     mov rbx, qword ptr [rbp + 0x50]
00354385  49 8D 8F D8 35 00 00            lea rcx, [r15 + 0x35d8]
0035438C  E8 6F DE EF FF                  call 0x140252200
00354391  4D 85 F6                        test r14, r14
00354394  74 03                           je 0x140354399
00354396  4D 89 2E                        mov qword ptr [r14], r13
00354399  48 85 DB                        test rbx, rbx
0035439C  74 0A                           je 0x1403543a8
0035439E  8B 4D C8                        mov ecx, dword ptr [rbp - 0x38]
003543A1  48 8B 0C CF                     mov rcx, qword ptr [rdi + rcx*8]
003543A5  48 89 0B                        mov qword ptr [rbx], rcx
003543A8  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
003543B0  41 8A C4                        mov al, r12b
003543B3  48 83 C4 70                     add rsp, 0x70
003543B7  41 5F                           pop r15
003543B9  41 5E                           pop r14
003543BB  41 5D                           pop r13
003543BD  41 5C                           pop r12
003543BF  5F                              pop rdi
003543C0  5E                              pop rsi
003543C1  5D                              pop rbp
003543C2  C3                              ret
003543C3  CC                              int3
003543C4  8B 05 EE 26 C7 00               mov eax, dword ptr [rip + 0xc726ee]
003543CA  A8 40                           test al, 0x40
003543CC  0F 84 E4 FE FF FF               je 0x1403542b6
003543D2  E8 B9 B0 FB FF                  call 0x14030f490
003543D7  84 C0                           test al, al
003543D9  0F 84 D7 FE FF FF               je 0x1403542b6
003543DF  8B CB                           mov ecx, ebx
003543E1  E8 7A B0 FB FF                  call 0x14030f460
003543E6  E9 CD FE FF FF                  jmp 0x1403542b8
003543EB  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
003543EF  33 F6                           xor esi, esi
003543F1  4C 8B C0                        mov r8, rax
003543F4  44 8B CE                        mov r9d, esi
003543F7  49 83 E0 FE                     and r8, 0xfffffffffffffffe
003543FB  8B D6                           mov edx, esi
003543FD  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00354401  44 8D 56 01                     lea r10d, [rsi + 1]
00354405  41 23 C2                        and eax, r10d
00354408  74 45                           je 0x14035444f
0035440A  41 3B C2                        cmp eax, r10d
0035440D  75 15                           jne 0x140354424
0035440F  49 8B 80 58 8E 00 00            mov rax, qword ptr [r8 + 0x8e58]
00354416  4D 8B 88 58 8E 00 00            mov r9, qword ptr [r8 + 0x8e58]
0035441D  49 83 C1 08                     add r9, 8
00354421  0F B6 10                        movzx edx, byte ptr [rax]
00354424  85 D2                           test edx, edx
00354426  0F 84 41 FF FF FF               je 0x14035436d
0035442C  8D 42 FF                        lea eax, [rdx - 1]
0035442F  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
00354433  8B D0                           mov edx, eax
00354435  F0 48 21 71 30                  lock and qword ptr [rcx + 0x30], rsi
0035443A  85 C0                           test eax, eax
0035443C  75 EE                           jne 0x14035442c
0035443E  E9 2A FF FF FF                  jmp 0x14035436d
00354443  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00354447  41 8B D2                        mov edx, r10d
0035444A  E9 0C FF FF FF                  jmp 0x14035435b
0035444F  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00354453  41 8B D2                        mov edx, r10d
00354456  EB D4                           jmp 0x14035442c
00354458  4D 85 F6                        test r14, r14
0035445B  0F 85 A4 01 00 00               jne 0x140354605
00354461  41 BE 01 00 00 00               mov r14d, 1
00354467  66 F0 44 01 B3 64 03 00 00      lock add word ptr [rbx + 0x364], r14w
00354470  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00354474  E8 D7 57 04 00                  call 0x140399c50
00354479  33 F6                           xor esi, esi
0035447B  8B FE                           mov edi, esi
0035447D  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00354484  73 51                           jae 0x1403544d7
00354486  41 03 FE                        add edi, r14d
00354489  85 3D 1D 0E C7 00               test dword ptr [rip + 0xc70e1d], edi
0035448F  0F 84 B2 02 00 00               je 0x140354747
00354495  F3 90                           pause
00354497  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0035449B  48 85 C0                        test rax, rax
0035449E  74 DD                           je 0x14035447d
003544A0  EB E4                           jmp 0x140354486
003544A2  48 8B 3C F1                     mov rdi, qword ptr [rcx + rsi*8]
003544A6  4C 8D 45 D0                     lea r8, [rbp - 0x30]
003544AA  48 8B CF                        mov rcx, rdi
003544AD  33 D2                           xor edx, edx
003544AF  E8 AC A8 FB FF                  call 0x14030ed60
003544B4  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
003544BA  3C 01                           cmp al, 1
003544BC  75 0E                           jne 0x1403544cc
003544BE  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
003544C4  3B C6                           cmp eax, esi
003544C6  0F 84 AB 03 00 00               je 0x140354877
003544CC  48 8D 4D D0                     lea rcx, [rbp - 0x30]
003544D0  E8 7B 57 04 00                  call 0x140399c50
003544D5  33 F6                           xor esi, esi
003544D7  0F B6 8B 84 01 00 00            movzx ecx, byte ptr [rbx + 0x184]
003544DE  48 8B FE                        mov rdi, rsi
003544E1  4C 8B F6                        mov r14, rsi
003544E4  83 E9 01                        sub ecx, 1
003544E7  0F 84 81 02 00 00               je 0x14035476e
003544ED  83 E9 01                        sub ecx, 1
003544F0  0F 84 9C 01 00 00               je 0x140354692
003544F6  83 E9 01                        sub ecx, 1
003544F9  75 48                           jne 0x140354543
003544FB  8B B3 18 02 00 00               mov esi, dword ptr [rbx + 0x218]
00354501  85 F6                           test esi, esi
00354503  78 D0                           js 0x1403544d5
00354505  48 8D 0D 34 47 C7 00            lea rcx, [rip + 0xc74734]
0035450C  33 D2                           xor edx, edx
0035450E  48 8B 3C F1                     mov rdi, qword ptr [rcx + rsi*8]
00354512  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00354516  48 8B CF                        mov rcx, rdi
00354519  E8 42 A8 FB FF                  call 0x14030ed60
0035451E  48 3B 5F 10                     cmp rbx, qword ptr [rdi + 0x10]
00354522  0F 84 4F 03 00 00               je 0x140354877
00354528  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
0035452E  3C 03                           cmp al, 3
00354530  75 9A                           jne 0x1403544cc
00354532  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
00354538  3B C6                           cmp eax, esi
0035453A  75 90                           jne 0x1403544cc
0035453C  B9 1E 00 00 00                  mov ecx, 0x1e
00354541  CD 29                           int 0x29
00354543  83 F9 02                        cmp ecx, 2
00354546  75 0D                           jne 0x140354555
00354548  8A 43 70                        mov al, byte ptr [rbx + 0x70]
0035454B  24 07                           and al, 7
0035454D  3C 01                           cmp al, 1
0035454F  0F 85 33 01 00 00               jne 0x140354688
00354555  83 C8 FF                        or eax, 0xffffffff
00354558  66 F0 01 83 64 03 00 00         lock add word ptr [rbx + 0x364], ax
00354560  E8 FB 16 00 00                  call 0x140355c60
00354565  85 C0                           test eax, eax
00354567  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
0035456D  0F 85 CD 00 00 00               jne 0x140354640
00354573  3C 02                           cmp al, 2
00354575  75 69                           jne 0x1403545e0
00354577  8A 87 B9 38 00 00               mov al, byte ptr [rdi + 0x38b9]
0035457D  84 C0                           test al, al
0035457F  75 5F                           jne 0x1403545e0
00354581  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
00354584  8B 43 54                        mov eax, dword ptr [rbx + 0x54]
00354587  3B C8                           cmp ecx, eax
00354589  0F 46 C8                        cmovbe ecx, eax
0035458C  3B 0D EA 0D C7 00               cmp ecx, dword ptr [rip + 0xc70dea]
00354592  72 4C                           jb 0x1403545e0
00354594  45 33 C0                        xor r8d, r8d
00354597  48 8B D7                        mov rdx, rdi
0035459A  48 8B CB                        mov rcx, rbx
0035459D  E8 8A 91 04 00                  call 0x14039d72c
003545A2  85 C0                           test eax, eax
003545A4  74 3A                           je 0x1403545e0
003545A6  F0 0F BA 6B 78 0C               lock bts dword ptr [rbx + 0x78], 0xc
003545AC  0F 92 C0                        setb al
003545AF  84 C0                           test al, al
003545B1  75 2D                           jne 0x1403545e0
003545B3  41 BC 01 00 00 00               mov r12d, 1
003545B9  44 88 A7 B9 38 00 00            mov byte ptr [rdi + 0x38b9], r12b
003545C0  41 8A 87 D9 35 00 00            mov al, byte ptr [r15 + 0x35d9]
003545C7  84 C0                           test al, al
003545C9  0F 85 2B 01 00 00               jne 0x1403546fa
003545CF  45 88 A7 D9 35 00 00            mov byte ptr [r15 + 0x35d9], r12b
003545D6  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
003545D9  41 89 87 DC 35 00 00            mov dword ptr [r15 + 0x35dc], eax
003545E0  48 8D 45 E8                     lea rax, [rbp - 0x18]
003545E4  4D 8B CE                        mov r9, r14
003545E7  4C 8D 45 D0                     lea r8, [rbp - 0x30]
003545EB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003545F0  48 8B D7                        mov rdx, rdi
003545F3  E8 18 33 EC FF                  call 0x140217910
003545F8  4C 8B 75 48                     mov r14, qword ptr [rbp + 0x48]
003545FC  48 89 73 40                     mov qword ptr [rbx + 0x40], rsi
00354600  E9 10 FD FF FF                  jmp 0x140354315
00354605  F7 43 78 00 10 00 00            test dword ptr [rbx + 0x78], 0x1000
0035460C  75 72                           jne 0x140354680
0035460E  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
00354611  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00354614  49 0F AB C5                     bts r13, rax
00354618  83 C8 FF                        or eax, 0xffffffff
0035461B  3B D0                           cmp edx, eax
0035461D  0F 85 C3 00 00 00               jne 0x1403546e6
00354623  0F BE 83 C3 00 00 00            movsx eax, byte ptr [rbx + 0xc3]
0035462A  41 BA 01 00 00 00               mov r10d, 1
00354630  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
00354633  45 8A E2                        mov r12b, r10b
00354636  89 75 C8                        mov dword ptr [rbp - 0x38], esi
00354639  33 F6                           xor esi, esi
0035463B  E9 DB FC FF FF                  jmp 0x14035431b
00354640  3C 02                           cmp al, 2
00354642  75 9C                           jne 0x1403545e0
00354644  8A 87 B9 38 00 00               mov al, byte ptr [rdi + 0x38b9]
0035464A  84 C0                           test al, al
0035464C  75 92                           jne 0x1403545e0
0035464E  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
00354651  8B 43 54                        mov eax, dword ptr [rbx + 0x54]
00354654  3B C8                           cmp ecx, eax
00354656  0F 46 C8                        cmovbe ecx, eax
00354659  3B 0D 1D 0D C7 00               cmp ecx, dword ptr [rip + 0xc70d1d]
0035465F  0F 82 7B FF FF FF               jb 0x1403545e0
00354665  45 33 C0                        xor r8d, r8d
00354668  48 8B D7                        mov rdx, rdi
0035466B  48 8B CB                        mov rcx, rbx
0035466E  E8 B9 90 04 00                  call 0x14039d72c
00354673  85 C0                           test eax, eax
00354675  0F 84 65 FF FF FF               je 0x1403545e0
0035467B  E9 33 FF FF FF                  jmp 0x1403545b3
00354680  41 BA 01 00 00 00               mov r10d, 1
00354686  EB B1                           jmp 0x140354639
00354688  2C 03                           sub al, 3
0035468A  3C 03                           cmp al, 3
0035468C  0F 86 C3 FE FF FF               jbe 0x140354555
00354692  8B B3 18 02 00 00               mov esi, dword ptr [rbx + 0x218]
00354698  85 F6                           test esi, esi
0035469A  0F 88 35 FE FF FF               js 0x1403544d5
003546A0  48 8D 0D 99 45 C7 00            lea rcx, [rip + 0xc74599]
003546A7  33 D2                           xor edx, edx
003546A9  48 8B 3C F1                     mov rdi, qword ptr [rcx + rsi*8]
003546AD  4C 8D 45 D0                     lea r8, [rbp - 0x30]
003546B1  48 8B CF                        mov rcx, rdi
003546B4  E8 A7 A6 FB FF                  call 0x14030ed60
003546B9  48 3B 5F 08                     cmp rbx, qword ptr [rdi + 8]
003546BD  0F 84 B4 01 00 00               je 0x140354877
003546C3  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
003546C9  3C 02                           cmp al, 2
003546CB  0F 85 FB FD FF FF               jne 0x1403544cc
003546D1  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
003546D7  3B C6                           cmp eax, esi
003546D9  0F 85 ED FD FF FF               jne 0x1403544cc
003546DF  B9 4A 00 00 00                  mov ecx, 0x4a
003546E4  CD 29                           int 0x29
003546E6  0F BE 83 C3 00 00 00            movsx eax, byte ptr [rbx + 0xc3]
003546ED  3B C2                           cmp eax, edx
003546EF  0F 8E 1E FC FF FF               jle 0x140354313
003546F5  E9 29 FF FF FF                  jmp 0x140354623
003546FA  41 3A C4                        cmp al, r12b
003546FD  0F 85 3C 01 00 00               jne 0x14035483f
00354703  41 8B 97 DC 35 00 00            mov edx, dword ptr [r15 + 0x35dc]
0035470A  3B 57 24                        cmp edx, dword ptr [rdi + 0x24]
0035470D  0F 84 CD FE FF FF               je 0x1403545e0
00354713  49 8D B7 E0 35 00 00            lea rsi, [r15 + 0x35e0]
0035471A  41 C6 87 D9 35 00 00 02         mov byte ptr [r15 + 0x35d9], 2
00354722  48 8B CE                        mov rcx, rsi
00354725  E8 C6 6F F0 FF                  call 0x14025b6f0
0035472A  4C 8B 87 C8 00 00 00            mov r8, qword ptr [rdi + 0xc8]
00354731  48 8B CE                        mov rcx, rsi
00354734  0F B6 97 D0 00 00 00            movzx edx, byte ptr [rdi + 0xd0]
0035473B  E8 80 6F F0 FF                  call 0x14025b6c0
00354740  33 F6                           xor esi, esi
00354742  E9 99 FE FF FF                  jmp 0x1403545e0
00354747  8B 05 6B 23 C7 00               mov eax, dword ptr [rip + 0xc7236b]
0035474D  A8 40                           test al, 0x40
0035474F  0F 84 40 FD FF FF               je 0x140354495
00354755  E8 36 AD FB FF                  call 0x14030f490
0035475A  84 C0                           test al, al
0035475C  0F 84 33 FD FF FF               je 0x140354495
00354762  8B CF                           mov ecx, edi
00354764  E8 F7 AC FB FF                  call 0x14030f460
00354769  E9 29 FD FF FF                  jmp 0x140354497
0035476E  8B B3 18 02 00 00               mov esi, dword ptr [rbx + 0x218]
00354774  48 8D 0D C5 44 C7 00            lea rcx, [rip + 0xc744c5]
0035477B  85 F6                           test esi, esi
0035477D  0F 89 1F FD FF FF               jns 0x1403544a2
00354783  8B C6                           mov eax, esi
00354785  0F BA F0 1F                     btr eax, 0x1f
00354789  F7 05 A5 23 C7 00 00 00 20 00   test dword ptr [rip + 0xc723a5], 0x200000
00354793  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00354797  4C 8B B0 48 8E 00 00            mov r14, qword ptr [rax + 0x8e48]
0035479E  0F 84 A7 00 00 00               je 0x14035484b
003547A4  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
003547A9  48 8D 55 E8                     lea rdx, [rbp - 0x18]
003547AD  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
003547B1  90                              nop
003547B2  49 87 16                        xchg qword ptr [r14], rdx
003547B5  48 85 D2                        test rdx, rdx
003547B8  0F 85 AB 00 00 00               jne 0x140354869
003547BE  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
003547C4  3C 01                           cmp al, 1
003547C6  75 13                           jne 0x1403547db
003547C8  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
003547CE  3B C6                           cmp eax, esi
003547D0  75 09                           jne 0x1403547db
003547D2  33 F6                           xor esi, esi
003547D4  8B FE                           mov edi, esi
003547D6  E9 7A FD FF FF                  jmp 0x140354555
003547DB  33 F6                           xor esi, esi
003547DD  F7 05 51 23 C7 00 00 00 20 00   test dword ptr [rip + 0xc72351], 0x200000
003547E7  74 77                           je 0x140354860
003547E9  0F 0D 4D E8                     prefetchw byte ptr [rbp - 0x18]
003547ED  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
003547F1  48 85 C0                        test rax, rax
003547F4  75 23                           jne 0x140354819
003547F6  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
003547FA  48 8D 45 E8                     lea rax, [rbp - 0x18]
003547FE  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
00354803  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00354807  48 3B C1                        cmp rax, rcx
0035480A  0F 84 C7 FC FF FF               je 0x1403544d7
00354810  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00354814  E8 87 32 EC FF                  call 0x140217aa0
00354819  48 8D 48 08                     lea rcx, [rax + 8]
0035481D  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
00354821  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00354825  48 8B C2                        mov rax, rdx
00354828  48 87 01                        xchg qword ptr [rcx], rax
0035482B  32 C2                           xor al, dl
0035482D  A8 04                           test al, 4
0035482F  0F 84 A2 FC FF FF               je 0x1403544d7
00354835  E8 E6 33 EC FF                  call 0x140217c20
0035483A  E9 98 FC FF FF                  jmp 0x1403544d7
0035483F  49 8D B7 E0 35 00 00            lea rsi, [r15 + 0x35e0]
00354846  E9 DF FE FF FF                  jmp 0x14035472a
0035484B  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
0035484F  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00354855  0F 83 63 FF FF FF               jae 0x1403547be
0035485B  E9 D0 DE 38 00                  jmp 0x1406e2730
00354860  F0 49 21 36                     lock and qword ptr [r14], rsi
00354864  E9 6E FC FF FF                  jmp 0x1403544d7
00354869  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0035486D  E8 3E 36 F0 FF                  call 0x140257eb0
00354872  E9 47 FF FF FF                  jmp 0x1403547be
00354877  33 F6                           xor esi, esi
00354879  E9 D7 FC FF FF                  jmp 0x140354555
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSendHeteroRescheduleIntRequestHelper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (112);
    v_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m50 = v_xmm0;
    if (a1 == 0) goto loc_00354385;
loc_0035425F:
    v_stack_m78 = (unsigned int)(a1);
    result = (unsigned int)((*(unsigned __int8 *)(a4 + 208)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    v_stack_p8 = a1;
    result = (*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8)) & (-2);
    v_stack_m68 = result;
    v_rbx = 0;
loc_0035429E:
    if (condition_is_above_or_equal) goto loc_003542C3;
loc_003542A7:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((*(unsigned int *)(v_rip + 13045756)) & ((unsigned int)(v_rbx))) == 0) goto loc_003543C4;
loc_003542B6:
loc_003542B8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 48) == 0) goto loc_0035429E;
    goto loc_003542A7;
loc_003542C3:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 35)) & (1)) == 0) goto loc_003543EB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 16)) != 0) goto loc_003543EB;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 14521)) != 0) goto loc_00354313;
    a1 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 8) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 8) + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 8) + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 8) + 84))); }
    if (((unsigned int)(a1)) < (*(unsigned int *)(v_rip + 13045889))) goto loc_00354313;
    a3 = 0;
    result = KiCheckPreferredHeteroProcessor(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8) + 8), *(unsigned __int64 *)(v_rip + 13060616 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12381998) + a1 * 4)) * 8), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00354458;
loc_00354313:
    v_rsi = 0;
loc_00354315:
loc_0035431B:
    if (v_stack_m68 == 0) goto loc_0035436D;
    a3 = (v_stack_m68) & (-2);
    v_stack_m60 = a3;
    result = (unsigned int)((v_stack_m68) & (1));
    if (condition_is_equal) goto loc_00354443;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a3 + 36440);
        a4 = *(unsigned __int64 *)(a3 + 36440);
        a4 = (a4) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0035436D;
loc_0035435B:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0035435B;
loc_0035436D:
    if (v_stack_p8 != 0) goto loc_0035425F;
loc_00354385:
    result = KiFlushSoftwareInterruptBatch(a4 + 13784, (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    if (v_stack_p10 != 0) {
        *(unsigned __int64 *)(v_stack_p10) = 0;
    }
    if (v_stack_p18 != 0) {
        a1 = v_stack_m70;
        a1 = *(unsigned __int64 *)(v_rip + 13060296 + a1 * 8);
        *(unsigned __int64 *)(v_stack_p18) = a1;
    }
    v_rsp = (v_rsp) + (112);
    return 0;
loc_003543C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13051630)))) & (64)) == 0) goto loc_003542B6;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003542B6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p20)), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    goto loc_003542B8;
loc_003543EB:
    v_rsi = 0;
    a3 = (v_stack_m68) & (-2);
    v_stack_m58 = a3;
    result = (unsigned int)((v_stack_m68) & ((unsigned int)(v_rsi + 1)));
    if (condition_is_equal) goto loc_0035444F;
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi + 1))) {
        result = *(unsigned __int64 *)(a3 + 36440);
        a4 = *(unsigned __int64 *)(a3 + 36440);
        a4 = (a4) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0035436D;
loc_0035442C:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0035442C;
    goto loc_0035436D;
loc_00354443:
    goto loc_0035435B;
loc_0035444F:
    goto loc_0035442C;
loc_00354458:
    if (v_stack_p10 != 0) goto loc_00354605;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, (unsigned int)((unsigned int)(v_rsi + 1)), a3, v_stack_m58);
    v_rsi = 0;
loc_0035447D:
    if (condition_is_above_or_equal) goto loc_003544D7;
loc_00354486:
    v_rdi = (unsigned int)((0) + (1));
    if (((*(unsigned int *)(v_rip + 13045277)) & ((unsigned int)(v_rdi))) == 0) goto loc_00354747;
loc_00354495:
loc_00354497:
    if (*(unsigned __int64 *)(v_stack_p20 + 64) == 0) goto loc_0035447D;
    goto loc_00354486;
loc_003544A2:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_stack_m68 + v_rsi * 8), a2, v_stack_m68, v_stack_m58);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 388))) != 1) goto loc_003544CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)))) == 0) goto loc_00354877;
loc_003544CC:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, a2, v_stack_m68, v_stack_m58);
loc_003544D5:
    v_rsi = 0;
loc_003544D7:
    a1 = (unsigned int)((*(unsigned __int8 *)(v_stack_p20 + 388)) - (1));
    if (condition_is_equal) goto loc_0035476E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00354692;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00354543;
    if (sign_flag) goto loc_003544D5;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8), a2, v_stack_m68, v_stack_m58);
    if (v_stack_p20 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 16))) goto loc_00354877;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 388))) != 3) goto loc_003544CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536))))) goto loc_003544CC;
loc_00354543:
    if (30 != 2) goto loc_00354555;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p20 + 112)) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_00354688;
loc_00354555:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline(30, a2, v_stack_m68, v_stack_m58);
    if ((unsigned int)(result) != 0) goto loc_00354640;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 388))) != 2) goto loc_003545E0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 14521)) != 0) goto loc_003545E0;
    a1 = (unsigned int)(*(unsigned int *)(v_stack_p20 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 84))); }
    if (((unsigned int)(a1)) < (*(unsigned int *)(v_rip + 13045226))) goto loc_003545E0;
    a3 = 0;
    result = KiCheckPreferredHeteroProcessor(v_stack_p20, *(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8), a3, v_stack_m58);
    if ((unsigned int)(result) == 0) goto loc_003545E0;
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_003545E0;
loc_003545B3:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 14521) = 1;
    if ((unsigned __int8)(*(unsigned __int8 *)(a4 + 13785)) != 0) goto loc_003546FA;
    *(unsigned __int8 *)(a4 + 13785) = 1;
    *(unsigned int *)(a4 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 36)));
loc_003545E0:
    v_stack_p20 = v_stack_m50;
    result = KiReleaseThreadStateLock(v_stack_p20, *(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8), v_stack_m68, 0);
    *(unsigned __int64 *)(v_stack_p20 + 64) = (unsigned int)(*(unsigned int *)(v_stack_p20 + 536));
    goto loc_00354315;
loc_00354605:
    if (((*(unsigned int *)(v_stack_p20 + 120)) & (0x1000ULL)) != 0) goto loc_00354680;
    result = (unsigned int)(((unsigned int)(v_stack_m78)) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_m74))) != ((unsigned int)(result))) goto loc_003546E6;
loc_00354623:
    v_stack_m74 = (unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p20 + 195)));
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)));
loc_00354639:
    v_rsi = 0;
    goto loc_0035431B;
loc_00354640:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_stack_p20 + 195)))) != 2) goto loc_003545E0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 14521)) != 0) goto loc_003545E0;
    a1 = (unsigned int)(*(unsigned int *)(v_stack_p20 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 84))); }
    if (((unsigned int)(a1)) < (*(unsigned int *)(v_rip + 13045021))) goto loc_003545E0;
    a3 = 0;
    result = KiCheckPreferredHeteroProcessor(v_stack_p20, *(unsigned __int64 *)(v_rip + 13059892 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8), a3, 0);
    if ((unsigned int)(result) == 0) goto loc_003545E0;
    goto loc_003545B3;
loc_00354680:
    goto loc_00354639;
loc_00354688:
    result = (unsigned __int8)((result) - (3));
    if (((unsigned __int8)(result)) <= 3) goto loc_00354555;
loc_00354692:
    if (sign_flag) goto loc_003544D5;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8), a2, v_stack_m68, 0);
    if (v_stack_p20 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 8))) goto loc_00354877;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 388))) != 2) goto loc_003544CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536))))) goto loc_003544CC;
loc_003546E6:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p20 + 195)))) <= 0) goto loc_00354313;
    goto loc_00354623;
loc_003546FA:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_stack_p20 + 195)))) != 1) goto loc_0035483F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 36))) goto loc_003545E0;
    *(unsigned __int8 *)(a4 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a4 + 13792, (unsigned int)(*(unsigned int *)(a4 + 13788)), v_stack_m68, 0);
loc_0035472A:
    result = KeAddGroupAffinityEx(a4 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
    v_rsi = 0;
    goto loc_003545E0;
loc_00354747:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13050731)))) & (64)) == 0) goto loc_00354495;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
    if ((unsigned __int8)(result) == 0) goto loc_00354495;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8))), *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
    goto loc_00354497;
loc_0035476E:
    if (!sign_flag) goto loc_003544A2;
    if (((*(unsigned int *)(v_rip + 13050789)) & (0x200000ULL)) == 0) goto loc_0035484B;
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059269 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)))) * 8) + 36424);
    if (v_stack_m50 != 0) goto loc_00354869;
loc_003547BE:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 388))) != 1) goto loc_003547DB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 536))))) goto loc_003547DB;
    v_rsi = 0;
    goto loc_00354555;
loc_003547DB:
    v_rsi = 0;
    if (((*(unsigned int *)(v_rip + 13050705)) & (0x200000ULL)) == 0) goto loc_00354860;
    if (v_stack_m50 != 0) goto loc_00354819;
    if (v_stack_m50 == v_stack_m50) goto loc_003544D7;
    result = KxWaitForLockChainValid(v_stack_m50, v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
loc_00354819:
    v_stack_m50 = 0;
    result = (unsigned __int8)((v_stack_m48) ^ ((unsigned __int8)(v_stack_m48)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_003544D7;
    result = KeWakeAddressAll(result + 8, v_stack_m48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
    goto loc_003544D7;
loc_0035483F:
    goto loc_0035472A;
loc_0035484B:
    if (condition_is_above_or_equal) goto loc_003547BE;
loc_00354860:
    goto loc_003544D7;
loc_00354869:
    result = KxWaitForLockOwnerShip(v_stack_m50, v_stack_m48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13059481 + (unsigned int)(*(unsigned int *)(v_stack_p20 + 536)) * 8) + 200), 0);
    goto loc_003547BE;
loc_00354877:
    v_rsi = 0;
    goto loc_00354555;
}
```

## 5. (Beta) C Style

```c
int64_t KiSendHeteroRescheduleIntRequestHelper(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (112);
    local_rsi = 0;
    v_stack_m70 = 0;
    v_stack_m50 = v_xmm0;
    if (Arg1 == 0) goto loc_00354385;
loc_0035425F:
    v_stack_m78 = (uint32_t)(Arg1);
    result = (uint32_t)((*(uint8_t *)(arg4 + 0xD0)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    v_stack_p8 = Arg1;
    result = (*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8)) & (-2);
    v_stack_m68 = result;
    local_rbx = 0;
loc_0035429E:
    if (condition_is_above_or_equal) goto loc_003542C3;
loc_003542A7:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((*(uint32_t *)(v_rip + 0xC70FFC)) & ((uint32_t)(local_rbx))) == 0) goto loc_003543C4;
loc_003542B6:
loc_003542B8:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x30) == 0) goto loc_0035429E;
    goto loc_003542A7;
loc_003542C3:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x23)) & (1)) == 0) goto loc_003543EB;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x10)) != 0) goto loc_003543EB;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x38B9)) != 0) goto loc_00354313;
    Arg1 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x8) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x8) + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x8) + 0x54))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x8) + 0x54))); }
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(v_rip + 0xC71081))) goto loc_00354313;
    Arg3 = 0;
    result = KiCheckPreferredHeteroProcessor(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8) + 0x8), *(uint64_t *)(v_rip + 0xC74A08 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBCEF2E) + Arg1 * 4)) * 8), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00354458;
loc_00354313:
    local_rsi = 0;
loc_00354315:
loc_0035431B:
    if (v_stack_m68 == 0) goto loc_0035436D;
    Arg3 = (v_stack_m68) & (-2);
    v_stack_m60 = Arg3;
    result = (uint32_t)((v_stack_m68) & (1));
    if (condition_is_equal) goto loc_00354443;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg3 + 0x8E58);
        Arg4 = *(uint64_t *)(Arg3 + 0x8E58);
        Arg4 = (Arg4) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0035436D;
loc_0035435B:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0035435B;
loc_0035436D:
    if (v_stack_p8 != 0) goto loc_0035425F;
loc_00354385:
    result = KiFlushSoftwareInterruptBatch(Arg4 + 13784, (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
    if (v_stack_p10 != 0) {
        *(uint64_t *)(v_stack_p10) = 0;
    }
    if (v_stack_p18 != 0) {
        Arg1 = v_stack_m70;
        Arg1 = *(uint64_t *)(v_rip + 0xC748C8 + Arg1 * 8);
        *(uint64_t *)(v_stack_p18) = Arg1;
    }
    local_rsp = (local_rsp) + (112);
    return 0;
loc_003543C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC726EE)))) & (64)) == 0) goto loc_003542B6;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003542B6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p20)), (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
    goto loc_003542B8;
loc_003543EB:
    local_rsi = 0;
    Arg3 = (v_stack_m68) & (-2);
    v_stack_m58 = Arg3;
    result = (uint32_t)((v_stack_m68) & ((uint32_t)(local_rsi + 1)));
    if (condition_is_equal) goto loc_0035444F;
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi + 1))) {
        result = *(uint64_t *)(Arg3 + 0x8E58);
        Arg4 = *(uint64_t *)(Arg3 + 0x8E58);
        Arg4 = (Arg4) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0035436D;
loc_0035442C:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0035442C;
    goto loc_0035436D;
loc_00354443:
    goto loc_0035435B;
loc_0035444F:
    goto loc_0035442C;
loc_00354458:
    if (v_stack_p10 != 0) goto loc_00354605;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, (uint32_t)((uint32_t)(local_rsi + 1)), Arg3, v_stack_m58);
    local_rsi = 0;
loc_0035447D:
    if (condition_is_above_or_equal) goto loc_003544D7;
loc_00354486:
    local_rdi = (uint32_t)((0) + (1));
    if (((*(uint32_t *)(v_rip + 0xC70E1D)) & ((uint32_t)(local_rdi))) == 0) goto loc_00354747;
loc_00354495:
loc_00354497:
    if (*(uint64_t *)(v_stack_p20 + 0x40) == 0) goto loc_0035447D;
    goto loc_00354486;
loc_003544A2:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_stack_m68 + local_rsi * 8), Arg2, v_stack_m68, v_stack_m58);
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x184))) != 1) goto loc_003544CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)))) == 0) goto loc_00354877;
loc_003544CC:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m68, Arg2, v_stack_m68, v_stack_m58);
loc_003544D5:
    local_rsi = 0;
loc_003544D7:
    Arg1 = (uint32_t)((*(uint8_t *)(v_stack_p20 + 0x184)) - (1));
    if (condition_is_equal) goto loc_0035476E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00354692;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00354543;
    if (sign_flag) goto loc_003544D5;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8), Arg2, v_stack_m68, v_stack_m58);
    if (v_stack_p20 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x10))) goto loc_00354877;
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x184))) != 3) goto loc_003544CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218))))) goto loc_003544CC;
loc_00354543:
    if (30 != 2) goto loc_00354555;
    result = (uint8_t)((*(uint8_t *)(v_stack_p20 + 0x70)) & (7));
    if (((uint8_t)(result)) != 1) goto loc_00354688;
loc_00354555:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline(30, Arg2, v_stack_m68, v_stack_m58);
    if ((uint32_t)(result) != 0) goto loc_00354640;
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x184))) != 2) goto loc_003545E0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x38B9)) != 0) goto loc_003545E0;
    Arg1 = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x54))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x54))); }
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(v_rip + 0xC70DEA))) goto loc_003545E0;
    Arg3 = 0;
    result = KiCheckPreferredHeteroProcessor(v_stack_p20, *(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8), Arg3, v_stack_m58);
    if ((uint32_t)(result) == 0) goto loc_003545E0;
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_003545E0;
loc_003545B3:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x38B9) = 1;
    if ((uint8_t)(*(uint8_t *)(arg4 + 0x35D9)) != 0) goto loc_003546FA;
    *(uint8_t *)(arg4 + 0x35D9) = 1;
    *(uint32_t *)(arg4 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x24)));
loc_003545E0:
    v_stack_p20 = v_stack_m50;
    result = KiReleaseThreadStateLock(v_stack_p20, *(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8), v_stack_m68, 0);
    *(uint64_t *)(v_stack_p20 + 0x40) = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218));
    goto loc_00354315;
loc_00354605:
    if (((*(uint32_t *)(v_stack_p20 + 0x78)) & (0x1000ULL)) != 0) goto loc_00354680;
    result = (uint32_t)(((uint32_t)(v_stack_m78)) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_m74))) != ((uint32_t)(result))) goto loc_003546E6;
loc_00354623:
    v_stack_m74 = (uint32_t)((int8_t)(*(uint8_t *)(v_stack_p20 + 0xC3)));
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)));
loc_00354639:
    local_rsi = 0;
    goto loc_0035431B;
loc_00354640:
    if (((uint8_t)((int8_t)(*(uint8_t *)(v_stack_p20 + 0xC3)))) != 2) goto loc_003545E0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x38B9)) != 0) goto loc_003545E0;
    Arg1 = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x54))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x54))); }
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(v_rip + 0xC70D1D))) goto loc_003545E0;
    Arg3 = 0;
    result = KiCheckPreferredHeteroProcessor(v_stack_p20, *(uint64_t *)(v_rip + 0xC74734 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8), Arg3, 0);
    if ((uint32_t)(result) == 0) goto loc_003545E0;
    goto loc_003545B3;
loc_00354680:
    goto loc_00354639;
loc_00354688:
    result = (uint8_t)((result) - (3));
    if (((uint8_t)(result)) <= 3) goto loc_00354555;
loc_00354692:
    if (sign_flag) goto loc_003544D5;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8), Arg2, v_stack_m68, 0);
    if (v_stack_p20 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x8))) goto loc_00354877;
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x184))) != 2) goto loc_003544CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218))))) goto loc_003544CC;
loc_003546E6:
    if (((uint32_t)((int8_t)(*(uint8_t *)(v_stack_p20 + 0xC3)))) <= 0) goto loc_00354313;
    goto loc_00354623;
loc_003546FA:
    if (((uint8_t)((int8_t)(*(uint8_t *)(v_stack_p20 + 0xC3)))) != 1) goto loc_0035483F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0x24))) goto loc_003545E0;
    *(uint8_t *)(arg4 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg4 + 13792, (uint32_t)(*(uint32_t *)(arg4 + 0x35DC)), v_stack_m68, 0);
loc_0035472A:
    result = KeAddGroupAffinityEx(Arg4 + 13792, *(uint8_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xD0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
    local_rsi = 0;
    goto loc_003545E0;
loc_00354747:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7236B)))) & (64)) == 0) goto loc_00354495;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4 + 13792, *(uint8_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xD0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
    if ((uint8_t)(result) == 0) goto loc_00354495;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8))), *(uint8_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xD0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
    goto loc_00354497;
loc_0035476E:
    if (!sign_flag) goto loc_003544A2;
    if (((*(uint32_t *)(v_rip + 0xC723A5)) & (0x200000ULL)) == 0) goto loc_0035484B;
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC744C5 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)))) * 8) + 0x8E48);
    if (v_stack_m50 != 0) goto loc_00354869;
loc_003547BE:
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x184))) != 1) goto loc_003547DB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218))))) goto loc_003547DB;
    local_rsi = 0;
    goto loc_00354555;
loc_003547DB:
    local_rsi = 0;
    if (((*(uint32_t *)(v_rip + 0xC72351)) & (0x200000ULL)) == 0) goto loc_00354860;
    if (v_stack_m50 != 0) goto loc_00354819;
    if (v_stack_m50 == v_stack_m50) goto loc_003544D7;
    result = KxWaitForLockChainValid(v_stack_m50, v_stack_m50, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
loc_00354819:
    v_stack_m50 = 0;
    result = (uint8_t)((v_stack_m48) ^ ((uint8_t)(v_stack_m48)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_003544D7;
    result = KeWakeAddressAll(result + 8, v_stack_m48, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
    goto loc_003544D7;
loc_0035483F:
    goto loc_0035472A;
loc_0035484B:
    if (condition_is_above_or_equal) goto loc_003547BE;
loc_00354860:
    goto loc_003544D7;
loc_00354869:
    result = KxWaitForLockOwnerShip(v_stack_m50, v_stack_m48, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC74599 + (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x218)) * 8) + 0xC8), 0);
    goto loc_003547BE;
loc_00354877:
    local_rsi = 0;
    goto loc_00354555;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0xD0` | `8` | `R` |
| `Arg4` | `+ 0x35D8` | `64` | `R` |
| `Arg4` | `+ 0x35D9` | `8` | `R` |
| `Arg4` | `+ 0x35D9` | `8` | `W` |
| `Arg4` | `+ 0x35DC` | `32` | `R` |
| `Arg4` | `+ 0x35DC` | `32` | `W` |
| `Arg4` | `+ 0x35E0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035420C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
