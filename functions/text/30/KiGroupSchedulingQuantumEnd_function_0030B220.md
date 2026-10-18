# KiGroupSchedulingQuantumEnd

- RVA: `0x0030B220`–`0x0030B744` (길이 `1,316` bytes)
- VA: `0x000000014030B220`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00073C8C`
- 디코드: `334`개 명령, `1,316/1,316` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0030B272` → [KiAcquirePrcbLocksForIsolationUnit](KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0030B36C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030B37F` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030B3B3` → [KiCommitRescheduleContext](KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x0030B3C2` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0030B3CB` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0030B3F6` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0030B424` → [KiInsertDeferredPreemptionApc](KiInsertDeferredPreemptionApc_function_0030A8E8.md) (function, `0x0030A8E8`)
- `0x0030B434` → [KiAcquirePrcbLocksForIsolationUnit](KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0030B444` → [KiGroupSchedulingGenerationEnd](KiGroupSchedulingGenerationEnd_function_0030A9B4.md) (function, `0x0030A9B4`)
- `0x0030B464` → [KiComputeGroupSchedulingRank](../21/KiComputeGroupSchedulingRank_function_0021EB84.md) (function, `0x0021EB84`)
- `0x0030B530` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0030B539` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0030B545` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0030B558` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030B5CE` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030B5DE` → [KiCheckMaxOverQuotaTransition](../35/KiCheckMaxOverQuotaTransition_function_00354884.md) (function, `0x00354884`)
- `0x0030B623` → [KiRemoveSchedulingGroupQueue](../20/KiRemoveSchedulingGroupQueue_function_00202638.md) (function, `0x00202638`)
- `0x0030B636` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030B69D` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x0030B6BE` → [KiRecomputeGroupSchedulingRank](../45/KiRecomputeGroupSchedulingRank_function_00452FC8.md) (function, `0x00452FC8`)
- `0x0030B728` → [KiProcessScbTracingList](../45/KiProcessScbTracingList_function_0045A500.md) (function, `0x0045A500`)
- `0x0030B73A` → [KiReadyDeferredReadyList](KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)

### Direct callers
- [sub_0021C0DA](../21/Unknown_function_0021C0DA.md) at `0x0021C1BE`

### Static image references
- `0x0030B312` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0030B6F4` → [sub_006E0C4E](../6E/Unknown_function_006E0C4E.md) (`tail-transfer`)
  - `0x0030B706` → [sub_006E0C4E](../6E/Unknown_function_006E0C4E.md) (`tail-transfer`)
  - `0x0030B711` → [sub_006E0C4E + 0x4E](../6E/Unknown_function_006E0C4E.md) (`tail-transfer`)
  - `0x0030B71B` → [sub_006E0C4E + 0x1E](../6E/Unknown_function_006E0C4E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030B220  48 8B C4                        mov rax, rsp
0030B223  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
0030B227  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0030B22B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0030B22F  53                              push rbx
0030B230  55                              push rbp
0030B231  56                              push rsi
0030B232  57                              push rdi
0030B233  41 54                           push r12
0030B235  41 55                           push r13
0030B237  41 56                           push r14
0030B239  41 57                           push r15
0030B23B  48 83 EC 48                     sub rsp, 0x48
0030B23F  48 BB 20 03 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000320
0030B249  48 8B E9                        mov rbp, rcx
0030B24C  33 C9                           xor ecx, ecx
0030B24E  4D 8B E8                        mov r13, r8
0030B251  48 8B FA                        mov rdi, rdx
0030B254  88 8C 24 90 00 00 00            mov byte ptr [rsp + 0x90], cl
0030B25B  44 8A F9                        mov r15b, cl
0030B25E  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
0030B262  48 8B 1B                        mov rbx, qword ptr [rbx]
0030B265  48 89 48 A0                     mov qword ptr [rax - 0x60], rcx
0030B269  4C 8B C2                        mov r8, rdx
0030B26C  8D 51 01                        lea edx, [rcx + 1]
0030B26F  48 8B CD                        mov rcx, rbp
0030B272  E8 E9 3A 00 00                  call 0x14030ed60
0030B277  48 3B 9D D8 8B 00 00            cmp rbx, qword ptr [rbp + 0x8bd8]
0030B27E  0F 87 B7 01 00 00               ja 0x14030b43b
0030B284  49 8B 75 68                     mov rsi, qword ptr [r13 + 0x68]
0030B288  45 33 D2                        xor r10d, r10d
0030B28B  48 85 F6                        test rsi, rsi
0030B28E  0F 84 B5 01 00 00               je 0x14030b449
0030B294  8B BD D8 00 00 00               mov edi, dword ptr [rbp + 0xd8]
0030B29A  48 03 FE                        add rdi, rsi
0030B29D  0F 84 A6 01 00 00               je 0x14030b449
0030B2A3  4C 8B 65 10                     mov r12, qword ptr [rbp + 0x10]
0030B2A7  45 8B F2                        mov r14d, r10d
0030B2AA  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0030B2AF  4D 85 E4                        test r12, r12
0030B2B2  74 14                           je 0x14030b2c8
0030B2B4  49 8B 44 24 68                  mov rax, qword ptr [r12 + 0x68]
0030B2B9  48 85 C0                        test rax, rax
0030B2BC  74 0A                           je 0x14030b2c8
0030B2BE  44 8B B5 D8 00 00 00            mov r14d, dword ptr [rbp + 0xd8]
0030B2C5  4C 03 F0                        add r14, rax
0030B2C8  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
0030B2CD  41 BD 01 00 00 00               mov r13d, 1
0030B2D3  44 8A A4 24 A8 00 00 00         mov r12b, byte ptr [rsp + 0xa8]
0030B2DB  0F B7 47 70                     movzx eax, word ptr [rdi + 0x70]
0030B2DF  44 8B 4F 7C                     mov r9d, dword ptr [rdi + 0x7c]
0030B2E3  44 0F B7 C0                     movzx r8d, ax
0030B2E7  66 41 83 E0 02                  and r8w, 2
0030B2EC  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
0030B2F1  66 44 89 44 24 22               mov word ptr [rsp + 0x22], r8w
0030B2F7  A8 04                           test al, 4
0030B2F9  0F 84 5C 01 00 00               je 0x14030b45b
0030B2FF  A8 02                           test al, 2
0030B301  0F 84 D1 02 00 00               je 0x14030b5d8
0030B307  44 88 AC 24 90 00 00 00         mov byte ptr [rsp + 0x90], r13b
0030B30F  45 8A FD                        mov r15b, r13b
0030B312  F7 05 F8 B7 CB 00 00 40 00 00   test dword ptr [rip + 0xcbb7f8], 0x4000
0030B31C  0F 85 C3 01 00 00               jne 0x14030b4e5
0030B322  48 8B BF A0 01 00 00            mov rdi, qword ptr [rdi + 0x1a0]
0030B329  48 85 FF                        test rdi, rdi
0030B32C  0F 85 89 01 00 00               jne 0x14030b4bb
0030B332  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
0030B33A  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0030B33F  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
0030B343  48 85 C0                        test rax, rax
0030B346  0F 84 80 01 00 00               je 0x14030b4cc
0030B34C  8B 9D D8 00 00 00               mov ebx, dword ptr [rbp + 0xd8]
0030B352  48 03 D8                        add rbx, rax
0030B355  48 8B B5 E8 37 00 00            mov rsi, qword ptr [rbp + 0x37e8]
0030B35C  33 D2                           xor edx, edx
0030B35E  48 8B CE                        mov rcx, rsi
0030B361  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0030B366  41 B8 F0 00 00 00               mov r8d, 0xf0
0030B36C  E8 CF B8 3B 00                  call 0x1406c6c40
0030B371  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0030B379  45 33 C0                        xor r8d, r8d
0030B37C  48 8B CE                        mov rcx, rsi
0030B37F  E8 2C 13 00 00                  call 0x14030c6b0
0030B384  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
0030B389  45 84 FF                        test r15b, r15b
0030B38C  0F 85 92 01 00 00               jne 0x14030b524
0030B392  40 38 BC 24 90 00 00 00         cmp byte ptr [rsp + 0x90], dil
0030B39A  0F 85 06 02 00 00               jne 0x14030b5a6
0030B3A0  BB 01 00 00 00                  mov ebx, 1
0030B3A5  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
0030B3AA  45 33 C0                        xor r8d, r8d
0030B3AD  48 8B D5                        mov rdx, rbp
0030B3B0  48 8B CE                        mov rcx, rsi
0030B3B3  E8 68 1B 00 00                  call 0x14030cf20
0030B3B8  49 8B CD                        mov rcx, r13
0030B3BB  44 0F B6 F7                     movzx r14d, dil
0030B3BF  44 8A F8                        mov r15b, al
0030B3C2  E8 39 FE FF FF                  call 0x14030b200
0030B3C7  84 C0                           test al, al
0030B3C9  74 0D                           je 0x14030b3d8
0030B3CB  E8 40 AF 04 00                  call 0x140356310
0030B3D0  84 C0                           test al, al
0030B3D2  0F 85 FC 00 00 00               jne 0x14030b4d4
0030B3D8  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
0030B3DD  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
0030B3E2  45 84 FF                        test r15b, r15b
0030B3E5  0F 84 B4 00 00 00               je 0x14030b49f
0030B3EB  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
0030B3F3  49 8B CC                        mov rcx, r12
0030B3F6  E8 55 E8 08 00                  call 0x140399c50
0030B3FB  45 84 FF                        test r15b, r15b
0030B3FE  0F 85 07 03 00 00               jne 0x14030b70b
0030B404  48 85 DB                        test rbx, rbx
0030B407  0F 85 13 03 00 00               jne 0x14030b720
0030B40D  48 85 FF                        test rdi, rdi
0030B410  0F 85 1C 03 00 00               jne 0x14030b732
0030B416  45 84 F6                        test r14b, r14b
0030B419  74 0E                           je 0x14030b429
0030B41B  45 33 C0                        xor r8d, r8d
0030B41E  49 8B D5                        mov rdx, r13
0030B421  48 8B CD                        mov rcx, rbp
0030B424  E8 BF F4 FF FF                  call 0x14030a8e8
0030B429  4D 8B C4                        mov r8, r12
0030B42C  BA 01 00 00 00                  mov edx, 1
0030B431  48 8B CD                        mov rcx, rbp
0030B434  E8 27 39 00 00                  call 0x14030ed60
0030B439  EB 0E                           jmp 0x14030b449
0030B43B  4C 8B C3                        mov r8, rbx
0030B43E  48 8B D7                        mov rdx, rdi
0030B441  48 8B CD                        mov rcx, rbp
0030B444  E8 6B F5 FF FF                  call 0x14030a9b4
0030B449  48 83 C4 48                     add rsp, 0x48
0030B44D  41 5F                           pop r15
0030B44F  41 5E                           pop r14
0030B451  41 5D                           pop r13
0030B453  41 5C                           pop r12
0030B455  5F                              pop rdi
0030B456  5E                              pop rsi
0030B457  5D                              pop rbp
0030B458  5B                              pop rbx
0030B459  C3                              ret
0030B45A  CC                              int3
0030B45B  4C 8B CF                        mov r9, rdi
0030B45E  48 8B D5                        mov rdx, rbp
0030B461  48 8B CE                        mov rcx, rsi
0030B464  E8 1B 37 F1 FF                  call 0x14021eb84
0030B469  44 0F B7 44 24 22               movzx r8d, word ptr [rsp + 0x22]
0030B46F  45 33 D2                        xor r10d, r10d
0030B472  F6 47 70 04                     test byte ptr [rdi + 0x70], 4
0030B476  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0030B47B  0F 84 91 FE FF FF               je 0x14030b312
0030B481  44 88 AC 24 90 00 00 00         mov byte ptr [rsp + 0x90], r13b
0030B489  45 8A FD                        mov r15b, r13b
0030B48C  4C 3B F7                        cmp r14, rdi
0030B48F  0F 85 7D FE FF FF               jne 0x14030b312
0030B495  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
0030B49A  E9 73 FE FF FF                  jmp 0x14030b312
0030B49F  48 85 FF                        test rdi, rdi
0030B4A2  0F 85 43 FF FF FF               jne 0x14030b3eb
0030B4A8  45 84 F6                        test r14b, r14b
0030B4AB  0F 85 3A FF FF FF               jne 0x14030b3eb
0030B4B1  48 85 DB                        test rbx, rbx
0030B4B4  74 93                           je 0x14030b449
0030B4B6  E9 30 FF FF FF                  jmp 0x14030b3eb
0030B4BB  8B 85 D8 00 00 00               mov eax, dword ptr [rbp + 0xd8]
0030B4C1  48 8B F7                        mov rsi, rdi
0030B4C4  48 2B F0                        sub rsi, rax
0030B4C7  E9 0F FE FF FF                  jmp 0x14030b2db
0030B4CC  48 8B DF                        mov rbx, rdi
0030B4CF  E9 81 FE FF FF                  jmp 0x14030b355
0030B4D4  41 F7 45 78 00 0C 00 00         test dword ptr [r13 + 0x78], 0xc00
0030B4DC  44 0F 44 F3                     cmove r14d, ebx
0030B4E0  E9 F3 FE FF FF                  jmp 0x14030b3d8
0030B4E5  0F B7 57 70                     movzx edx, word ptr [rdi + 0x70]
0030B4E9  41 8B C2                        mov eax, r10d
0030B4EC  0F B7 CA                        movzx ecx, dx
0030B4EF  66 D1 E9                        shr cx, 1
0030B4F2  66 41 23 CD                     and cx, r13w
0030B4F6  66 45 85 C0                     test r8w, r8w
0030B4FA  0F 95 C0                        setne al
0030B4FD  66 3B C8                        cmp cx, ax
0030B500  0F 84 DC 01 00 00               je 0x14030b6e2
0030B506  B8 00 01 00 00                  mov eax, 0x100
0030B50B  66 0B D0                        or dx, ax
0030B50E  48 8D 87 B0 01 00 00            lea rax, [rdi + 0x1b0]
0030B515  66 89 57 70                     mov word ptr [rdi + 0x70], dx
0030B519  48 89 18                        mov qword ptr [rax], rbx
0030B51C  48 8B D8                        mov rbx, rax
0030B51F  E9 FE FD FF FF                  jmp 0x14030b322
0030B524  4D 85 E4                        test r12, r12
0030B527  0F 85 65 FE FF FF               jne 0x14030b392
0030B52D  49 8B CD                        mov rcx, r13
0030B530  E8 CB FC FF FF                  call 0x14030b200
0030B535  84 C0                           test al, al
0030B537  74 19                           je 0x14030b552
0030B539  E8 D2 AD 04 00                  call 0x140356310
0030B53E  84 C0                           test al, al
0030B540  75 10                           jne 0x14030b552
0030B542  48 8B CB                        mov rcx, rbx
0030B545  E8 56 72 EF FF                  call 0x1402027a0
0030B54A  84 C0                           test al, al
0030B54C  0F 85 DE 00 00 00               jne 0x14030b630
0030B552  48 8B D5                        mov rdx, rbp
0030B555  48 8B CE                        mov rcx, rsi
0030B558  E8 03 7B 04 00                  call 0x140353060
0030B55D  4C 8B C0                        mov r8, rax
0030B560  BB 01 00 00 00                  mov ebx, 1
0030B565  8A 50 20                        mov dl, byte ptr [rax + 0x20]
0030B568  80 48 22 02                     or byte ptr [rax + 0x22], 2
0030B56C  8A CA                           mov cl, dl
0030B56E  80 C9 08                        or cl, 8
0030B571  88 48 20                        mov byte ptr [rax + 0x20], cl
0030B574  F6 C2 02                        test dl, 2
0030B577  74 4D                           je 0x14030b5c6
0030B579  8B D7                           mov edx, edi
0030B57B  40 38 3E                        cmp byte ptr [rsi], dil
0030B57E  76 46                           jbe 0x14030b5c6
0030B580  8B C2                           mov eax, edx
0030B582  48 8D 04 80                     lea rax, [rax + rax*4]
0030B586  48 8D 40 02                     lea rax, [rax + 2]
0030B58A  48 8D 04 C6                     lea rax, [rsi + rax*8]
0030B58E  49 3B C0                        cmp rax, r8
0030B591  74 08                           je 0x14030b59b
0030B593  80 48 20 08                     or byte ptr [rax + 0x20], 8
0030B597  80 48 22 02                     or byte ptr [rax + 0x22], 2
0030B59B  0F B6 06                        movzx eax, byte ptr [rsi]
0030B59E  03 D3                           add edx, ebx
0030B5A0  3B D0                           cmp edx, eax
0030B5A2  72 DC                           jb 0x14030b580
0030B5A4  EB 20                           jmp 0x14030b5c6
0030B5A6  4D 85 E4                        test r12, r12
0030B5A9  0F 84 F1 FD FF FF               je 0x14030b3a0
0030B5AF  4D 85 F6                        test r14, r14
0030B5B2  0F 84 E8 FD FF FF               je 0x14030b3a0
0030B5B8  4C 3B F3                        cmp r14, rbx
0030B5BB  0F 85 30 01 00 00               jne 0x14030b6f1
0030B5C1  BB 01 00 00 00                  mov ebx, 1
0030B5C6  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0030B5CB  48 8B CE                        mov rcx, rsi
0030B5CE  E8 4D D0 F4 FF                  call 0x140258620
0030B5D3  E9 CD FD FF FF                  jmp 0x14030b3a5
0030B5D8  48 8B D6                        mov rdx, rsi
0030B5DB  48 8B CF                        mov rcx, rdi
0030B5DE  E8 A1 92 04 00                  call 0x140354884
0030B5E3  45 33 D2                        xor r10d, r10d
0030B5E6  84 C0                           test al, al
0030B5E8  75 26                           jne 0x14030b610
0030B5EA  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0030B5EE  48 39 07                        cmp qword ptr [rdi], rax
0030B5F1  0F 83 BE 00 00 00               jae 0x14030b6b5
0030B5F7  44 0F B7 44 24 22               movzx r8d, word ptr [rsp + 0x22]
0030B5FD  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0030B602  45 84 E4                        test r12b, r12b
0030B605  0F 85 04 FD FF FF               jne 0x14030b30f
0030B60B  E9 02 FD FF FF                  jmp 0x14030b312
0030B610  44 84 6F 70                     test byte ptr [rdi + 0x70], r13b
0030B614  0F 84 B1 00 00 00               je 0x14030b6cb
0030B61A  45 8A C5                        mov r8b, r13b
0030B61D  48 8B D7                        mov rdx, rdi
0030B620  48 8B CD                        mov rcx, rbp
0030B623  E8 10 70 EF FF                  call 0x140202638
0030B628  45 33 D2                        xor r10d, r10d
0030B62B  E9 9B 00 00 00                  jmp 0x14030b6cb
0030B630  48 8B D5                        mov rdx, rbp
0030B633  48 8B CE                        mov rcx, rsi
0030B636  E8 25 7A 04 00                  call 0x140353060
0030B63B  4C 8B D8                        mov r11, rax
0030B63E  BB 01 00 00 00                  mov ebx, 1
0030B643  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
0030B647  44 8A 40 20                     mov r8b, byte ptr [rax + 0x20]
0030B64B  48 8B 10                        mov rdx, qword ptr [rax]
0030B64E  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
0030B652  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
0030B656  41 8A C8                        mov cl, r8b
0030B659  80 E1 C5                        and cl, 0xc5
0030B65C  80 C9 05                        or cl, 5
0030B65F  88 48 20                        mov byte ptr [rax + 0x20], cl
0030B662  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
0030B666  80 60 21 FE                     and byte ptr [rax + 0x21], 0xfe
0030B66A  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0030B66E  41 F6 C0 02                     test r8b, 2
0030B672  0F 84 4E FF FF FF               je 0x14030b5c6
0030B678  44 8B D7                        mov r10d, edi
0030B67B  40 38 3E                        cmp byte ptr [rsi], dil
0030B67E  76 2D                           jbe 0x14030b6ad
0030B680  41 8B C2                        mov eax, r10d
0030B683  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0030B68B  48 03 C8                        add rcx, rax
0030B68E  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
0030B692  49 3B CB                        cmp rcx, r11
0030B695  74 0B                           je 0x14030b6a2
0030B697  45 33 C9                        xor r9d, r9d
0030B69A  45 33 C0                        xor r8d, r8d
0030B69D  E8 9E 6C 04 00                  call 0x140352340
0030B6A2  0F B6 06                        movzx eax, byte ptr [rsi]
0030B6A5  44 03 D3                        add r10d, ebx
0030B6A8  44 3B D0                        cmp r10d, eax
0030B6AB  72 D3                           jb 0x14030b680
0030B6AD  89 7E 04                        mov dword ptr [rsi + 4], edi
0030B6B0  E9 11 FF FF FF                  jmp 0x14030b5c6
0030B6B5  4C 8B C5                        mov r8, rbp
0030B6B8  48 8B D7                        mov rdx, rdi
0030B6BB  48 8B CE                        mov rcx, rsi
0030B6BE  E8 05 79 14 00                  call 0x140452fc8
0030B6C3  45 33 D2                        xor r10d, r10d
0030B6C6  4C 3B F7                        cmp r14, rdi
0030B6C9  74 10                           je 0x14030b6db
0030B6CB  44 0F B7 44 24 22               movzx r8d, word ptr [rsp + 0x22]
0030B6D1  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
0030B6D6  E9 2C FC FF FF                  jmp 0x14030b307
0030B6DB  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
0030B6E0  EB E9                           jmp 0x14030b6cb
0030B6E2  44 39 4F 7C                     cmp dword ptr [rdi + 0x7c], r9d
0030B6E6  0F 84 36 FC FF FF               je 0x14030b322
0030B6EC  E9 15 FE FF FF                  jmp 0x14030b506
0030B6F1  4D 85 F6                        test r14, r14
0030B6F4  0F 84 54 55 3D 00               je 0x1406e0c4e
0030B6FA  4D 8B B6 A0 01 00 00            mov r14, qword ptr [r14 + 0x1a0]
0030B701  4C 3B F3                        cmp r14, rbx
0030B704  75 EB                           jne 0x14030b6f1
0030B706  E9 43 55 3D 00                  jmp 0x1406e0c4e
0030B70B  45 33 FF                        xor r15d, r15d
0030B70E  44 38 3E                        cmp byte ptr [rsi], r15b
0030B711  0F 86 85 55 3D 00               jbe 0x1406e0c9c
0030B717  45 8D 6F 01                     lea r13d, [r15 + 1]
0030B71B  E9 4C 55 3D 00                  jmp 0x1406e0c6c
0030B720  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
0030B725  48 8B CD                        mov rcx, rbp
0030B728  E8 D3 ED 14 00                  call 0x14045a500
0030B72D  E9 DB FC FF FF                  jmp 0x14030b40d
0030B732  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0030B737  48 8B CD                        mov rcx, rbp
0030B73A  E8 41 26 00 00                  call 0x14030dd80
0030B73F  E9 D2 FC FF FF                  jmp 0x14030b416
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiGroupSchedulingQuantumEnd(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m66;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int16 v_stack_p22;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_p90;

    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (72);
    a1 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, a1 + 1, a2, a4);
    if ((*(unsigned __int64 *)(v_rbx)) > (*(unsigned __int64 *)(a1 + 35800))) goto loc_0030B43B;
    v_r10 = 0;
    if (*(unsigned __int64 *)(a3 + 104) == 0) goto loc_0030B449;
    v_rdi = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a3 + 104));
    if (condition_is_equal) goto loc_0030B449;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 16);
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0030B2C8;
    v_r14 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104) != 0) {
        v_r14 = *(unsigned int *)(a1 + 216);
        v_r14 = (v_r14) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104));
    }
loc_0030B2DB:
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 112))) & (2));
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 124)));
    v_stack_m66 = (unsigned __int16)(a3);
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rdi + 112))) & (4)) == 0) goto loc_0030B45B;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rdi + 112))) & (2)) == 0) goto loc_0030B5D8;
loc_0030B307:
    v_stack_p8 = 1;
loc_0030B30F:
loc_0030B312:
    if (((*(unsigned int *)(v_rip + 13350904)) & (0x4000ULL)) != 0) goto loc_0030B4E5;
loc_0030B322:
    if (*(unsigned __int64 *)(v_rdi + 416) != 0) goto loc_0030B4BB;
    v_stack_m60 = v_stack_m60;
    if (*(unsigned __int64 *)(v_stack_p18 + 104) == 0) goto loc_0030B4CC;
    v_rbx = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(v_stack_p18 + 104));
loc_0030B355:
    a2 = 0;
    v_stack_m58 = *(unsigned __int64 *)(v_rdi + 416);
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, (unsigned int)(*(unsigned int *)(v_rdi + 124)));
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_p10, a3, (unsigned int)(*(unsigned int *)(v_rdi + 124)));
    if (1 != 0) goto loc_0030B524;
loc_0030B392:
    if (v_stack_p8 != ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 416)))) goto loc_0030B5A6;
loc_0030B3A0:
loc_0030B3A5:
    a3 = 0;
    result = KiCommitRescheduleContext(*(unsigned __int64 *)(a1 + 14312), 0, a3, v_stack_m58);
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, 0, a3, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_0030B3D8;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, 0, a3, v_stack_m58);
    if ((unsigned __int8)(result) != 0) goto loc_0030B4D4;
loc_0030B3D8:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0030B49F;
loc_0030B3EB:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, 0, a3, v_stack_m58);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0030B70B;
    if (v_stack_m60 != 0) goto loc_0030B720;
loc_0030B40D:
    if (v_stack_m58 != 0) goto loc_0030B732;
loc_0030B416:
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 416))) != 0) {
        a3 = 0;
        a2 = v_stack_p18;
        a1 = 0;
        result = KiInsertDeferredPreemptionApc(a1, a2, a3, v_stack_m58);
    }
    result = KiAcquirePrcbLocksForIsolationUnit(a1, 1, v_stack_p10, v_stack_m58);
    goto loc_0030B449;
loc_0030B43B:
    result = KiGroupSchedulingGenerationEnd(a1, v_stack_m58, v_stack_m60, v_stack_m58);
loc_0030B449:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0030B45B:
    result = KiComputeGroupSchedulingRank(*(unsigned __int64 *)(a1 + 14312), a1, v_stack_m60, v_stack_m58);
    v_r10 = 0;
    if (((*(unsigned __int8 *)(v_stack_m58 + 112)) & (4)) == 0) goto loc_0030B312;
    v_stack_p90 = (unsigned __int8)(v_stack_p18);
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 416))) != v_stack_m58) goto loc_0030B312;
    v_stack_p20 = (unsigned __int8)(v_stack_p18);
    goto loc_0030B312;
loc_0030B49F:
    if (v_stack_m58 != 0) goto loc_0030B3EB;
    if ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 416))) != 0) goto loc_0030B3EB;
    if (v_stack_m60 == 0) goto loc_0030B449;
    goto loc_0030B3EB;
loc_0030B4BB:
    v_rsi = (v_stack_m58) - ((unsigned int)(*(unsigned int *)(a1 + 216)));
    goto loc_0030B2DB;
loc_0030B4CC:
    goto loc_0030B355;
loc_0030B4D4:
    v_r14 = (unsigned __int8)(*(unsigned __int64 *)(v_rdi + 416));
    if (((*(unsigned int *)(v_stack_p18 + 120)) & (0xC00ULL)) == 0) { v_r14 = (unsigned int)(v_stack_m58); }
    goto loc_0030B3D8;
loc_0030B4E5:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + 112))) >> (1));
    a1 = (unsigned __int16)((a1) & ((unsigned __int16)(v_stack_p18)));
    result = ((unsigned __int16)(v_stack_p22) != 0) ? 1 : 0;
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(result))) goto loc_0030B6E2;
loc_0030B506:
    a2 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m58 + 112)) | (256));
    *(unsigned __int16 *)(v_stack_m58 + 112) = (unsigned __int16)(a2);
    *(unsigned __int64 *)(v_stack_m58 + 432) = v_stack_m58;
    goto loc_0030B322;
loc_0030B524:
    if (v_stack_p10 != 0) goto loc_0030B392;
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, a2, v_stack_p22, (unsigned int)(v_stack_p28));
    if ((unsigned __int8)(result) == 0) goto loc_0030B552;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, a2, v_stack_p22, (unsigned int)(v_stack_p28));
    if ((unsigned __int8)(result) != 0) goto loc_0030B552;
    result = KiCheckForMaxOverQuotaScb(v_stack_m58 + 432, a2, v_stack_p22, (unsigned int)(v_stack_p28));
    if ((unsigned __int8)(result) != 0) goto loc_0030B630;
loc_0030B552:
    result = KiFindRescheduleContextEntryForPrcb(v_rsi, a1, v_stack_p22, (unsigned int)(v_stack_p28));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) | (8));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) == 0) goto loc_0030B5C6;
    if ((*(unsigned __int8 *)(v_rsi)) <= ((unsigned __int8)(v_stack_m58))) goto loc_0030B5C6;
loc_0030B580:
    if ((v_rsi + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) * 4 + 2 * 8) != result) {
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m58))) + (1));
    if (((unsigned int)(a2)) < ((unsigned int)(*(unsigned __int8 *)(v_rsi)))) goto loc_0030B580;
    goto loc_0030B5C6;
loc_0030B5A6:
    if (v_stack_p10 == 0) goto loc_0030B3A0;
    if (v_r14 == 0) goto loc_0030B3A0;
    if (v_r14 != 1) goto loc_0030B6F1;
loc_0030B5C6:
    result = KiSearchForNewThreadsForRescheduleContext(v_rsi, v_stack_p30, result, (unsigned int)(v_stack_p28));
    goto loc_0030B3A5;
loc_0030B5D8:
    result = KiCheckMaxOverQuotaTransition(v_stack_m58, v_rsi, result, (unsigned int)(v_stack_p28));
    v_r10 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0030B610;
    if ((*(unsigned __int64 *)(v_stack_m58)) >= (*(unsigned __int64 *)(v_stack_m58 + 24))) goto loc_0030B6B5;
    if ((unsigned __int8)(v_stack_p10) != 0) goto loc_0030B30F;
    goto loc_0030B312;
loc_0030B610:
    if (((*(unsigned __int8 *)(v_stack_m58 + 112)) & ((unsigned __int8)(v_stack_p18))) == 0) goto loc_0030B6CB;
    result = KiRemoveSchedulingGroupQueue(a1, v_stack_m58, (unsigned __int8)(v_stack_p18), (unsigned int)(v_stack_p28));
    v_r10 = 0;
    goto loc_0030B6CB;
loc_0030B630:
    result = KiFindRescheduleContextEntryForPrcb(v_rsi, a1, (unsigned __int8)(v_stack_p18), (unsigned int)(v_stack_p28));
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (197));
    a1 = (unsigned __int8)((a1) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) == 0) goto loc_0030B5C6;
    if ((*(unsigned __int8 *)(v_rsi)) <= ((unsigned __int8)(v_stack_m58))) goto loc_0030B6AD;
loc_0030B680:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))));
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58))));
    if ((v_rsi + a1 * 8) != result) {
        a4 = 0;
        a3 = 0;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(v_rsi + a1 * 8, *(unsigned __int64 *)(result), a3, a4);
    }
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m58))) + (1));
    if (((unsigned int)(v_r10)) < ((unsigned int)(*(unsigned __int8 *)(v_rsi)))) goto loc_0030B680;
loc_0030B6AD:
    *(unsigned int *)(v_rsi + 4) = (unsigned int)(v_stack_m58);
    goto loc_0030B5C6;
loc_0030B6B5:
    result = KiRecomputeGroupSchedulingRank(v_rsi, v_stack_m58, a1, a4);
    v_r10 = 0;
    if (v_r14 == v_stack_m58) goto loc_0030B6DB;
loc_0030B6CB:
    goto loc_0030B307;
loc_0030B6DB:
    v_stack_p20 = (unsigned __int8)(v_stack_p18);
    goto loc_0030B6CB;
loc_0030B6E2:
    if ((*(unsigned int *)(v_stack_m58 + 124)) == ((unsigned int)((unsigned int)(v_stack_p28)))) goto loc_0030B322;
    goto loc_0030B506;
loc_0030B6F1:
    if ((*(unsigned __int64 *)(v_r14 + 416)) != 1) goto loc_0030B6F1;
loc_0030B70B:
    v_r15 = 0;
loc_0030B720:
    result = KiProcessScbTracingList(a1, v_stack_p28, v_stack_p22, (unsigned int)(v_stack_p28));
    goto loc_0030B40D;
loc_0030B732:
    result = KiReadyDeferredReadyList(a1, v_stack_p30, v_stack_p22, (unsigned int)(v_stack_p28));
    goto loc_0030B416;
}
```

## 5. (Beta) C Style

```c
int64_t KiGroupSchedulingQuantumEnd(void *Arg1, int64_t Arg2, void *Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint16_t v_stack_m66;
    uint8_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint16_t v_stack_p22;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p8;
    uint8_t v_stack_p90;

    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (72);
    Arg1 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, Arg1 + 1, Arg2, Arg4);
    if ((*(uint64_t *)(local_rbx)) > (*(uint64_t *)(arg1 + 0x8BD8))) goto loc_0030B43B;
    local_r10 = 0;
    if (*(uint64_t *)(arg3 + 0x68) == 0) goto loc_0030B449;
    local_rdi = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg3 + 0x68));
    if (condition_is_equal) goto loc_0030B449;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x10);
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0030B2C8;
    local_r14 = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68) != 0) {
        local_r14 = *(uint32_t *)(arg1 + 0xD8);
        local_r14 = (local_r14) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68));
    }
loc_0030B2DB:
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rdi + 0x70))) & (2));
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x7C)));
    v_stack_m66 = (uint16_t)(Arg3);
    if ((((uint8_t)(*(uint16_t *)(local_rdi + 0x70))) & (4)) == 0) goto loc_0030B45B;
    if ((((uint8_t)(*(uint16_t *)(local_rdi + 0x70))) & (2)) == 0) goto loc_0030B5D8;
loc_0030B307:
    v_stack_p8 = 1;
loc_0030B30F:
loc_0030B312:
    if (((*(uint32_t *)(v_rip + 0xCBB7F8)) & (0x4000ULL)) != 0) goto loc_0030B4E5;
loc_0030B322:
    if (*(uint64_t *)(local_rdi + 0x1A0) != 0) goto loc_0030B4BB;
    v_stack_m60 = v_stack_m60;
    if (*(uint64_t *)(v_stack_p18 + 0x68) == 0) goto loc_0030B4CC;
    local_rbx = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(v_stack_p18 + 0x68));
loc_0030B355:
    Arg2 = 0;
    v_stack_m58 = *(uint64_t *)(local_rdi + 0x1A0);
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, (uint32_t)(*(uint32_t *)(local_rdi + 0x7C)));
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_p10, Arg3, (uint32_t)(*(uint32_t *)(local_rdi + 0x7C)));
    if (1 != 0) goto loc_0030B524;
loc_0030B392:
    if (v_stack_p8 != ((uint8_t)(*(uint64_t *)(local_rdi + 0x1A0)))) goto loc_0030B5A6;
loc_0030B3A0:
loc_0030B3A5:
    Arg3 = 0;
    result = KiCommitRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), 0, Arg3, v_stack_m58);
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, 0, Arg3, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_0030B3D8;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, 0, Arg3, v_stack_m58);
    if ((uint8_t)(result) != 0) goto loc_0030B4D4;
loc_0030B3D8:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0030B49F;
loc_0030B3EB:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, 0, Arg3, v_stack_m58);
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0030B70B;
    if (v_stack_m60 != 0) goto loc_0030B720;
loc_0030B40D:
    if (v_stack_m58 != 0) goto loc_0030B732;
loc_0030B416:
    if ((uint8_t)((uint8_t)(*(uint64_t *)(local_rdi + 0x1A0))) != 0) {
        Arg3 = 0;
        Arg2 = v_stack_p18;
        Arg1 = 0;
        result = KiInsertDeferredPreemptionApc(Arg1, Arg2, Arg3, v_stack_m58);
    }
    result = KiAcquirePrcbLocksForIsolationUnit(Arg1, 1, v_stack_p10, v_stack_m58);
    goto loc_0030B449;
loc_0030B43B:
    result = KiGroupSchedulingGenerationEnd(Arg1, v_stack_m58, v_stack_m60, v_stack_m58);
loc_0030B449:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0030B45B:
    result = KiComputeGroupSchedulingRank(*(uint64_t *)(arg1 + 0x37E8), Arg1, v_stack_m60, v_stack_m58);
    local_r10 = 0;
    if (((*(uint8_t *)(v_stack_m58 + 0x70)) & (4)) == 0) goto loc_0030B312;
    v_stack_p90 = (uint8_t)(v_stack_p18);
    if (((uint8_t)(*(uint64_t *)(local_rdi + 0x1A0))) != v_stack_m58) goto loc_0030B312;
    v_stack_p20 = (uint8_t)(v_stack_p18);
    goto loc_0030B312;
loc_0030B49F:
    if (v_stack_m58 != 0) goto loc_0030B3EB;
    if ((uint8_t)((uint8_t)(*(uint64_t *)(local_rdi + 0x1A0))) != 0) goto loc_0030B3EB;
    if (v_stack_m60 == 0) goto loc_0030B449;
    goto loc_0030B3EB;
loc_0030B4BB:
    local_rsi = (v_stack_m58) - ((uint32_t)(*(uint32_t *)(arg1 + 0xD8)));
    goto loc_0030B2DB;
loc_0030B4CC:
    goto loc_0030B355;
loc_0030B4D4:
    local_r14 = (uint8_t)(*(uint64_t *)(local_rdi + 0x1A0));
    if (((*(uint32_t *)(v_stack_p18 + 0x78)) & (0xC00ULL)) == 0) { local_r14 = (uint32_t)(v_stack_m58); }
    goto loc_0030B3D8;
loc_0030B4E5:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m58 + 0x70))) >> (1));
    Arg1 = (uint16_t)((Arg1) & ((uint16_t)(v_stack_p18)));
    result = ((uint16_t)(v_stack_p22) != 0) ? 1 : 0;
    if (((uint16_t)(Arg1)) == ((uint16_t)(result))) goto loc_0030B6E2;
loc_0030B506:
    Arg2 = (uint16_t)((*(uint16_t *)(v_stack_m58 + 0x70)) | (256));
    *(uint16_t *)(v_stack_m58 + 0x70) = (uint16_t)(Arg2);
    *(uint64_t *)(v_stack_m58 + 0x1B0) = v_stack_m58;
    goto loc_0030B322;
loc_0030B524:
    if (v_stack_p10 != 0) goto loc_0030B392;
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, Arg2, v_stack_p22, (uint32_t)(v_stack_p28));
    if ((uint8_t)(result) == 0) goto loc_0030B552;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, Arg2, v_stack_p22, (uint32_t)(v_stack_p28));
    if ((uint8_t)(result) != 0) goto loc_0030B552;
    result = KiCheckForMaxOverQuotaScb(v_stack_m58 + 432, Arg2, v_stack_p22, (uint32_t)(v_stack_p28));
    if ((uint8_t)(result) != 0) goto loc_0030B630;
loc_0030B552:
    result = KiFindRescheduleContextEntryForPrcb(local_rsi, Arg1, v_stack_p22, (uint32_t)(v_stack_p28));
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) | (8));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) == 0) goto loc_0030B5C6;
    if ((*(uint8_t *)(local_rsi)) <= ((uint8_t)(v_stack_m58))) goto loc_0030B5C6;
loc_0030B580:
    if ((local_rsi + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) * 4 + 2 * 8) != result) {
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m58))) + (1));
    if (((uint32_t)(Arg2)) < ((uint32_t)(*(uint8_t *)(local_rsi)))) goto loc_0030B580;
    goto loc_0030B5C6;
loc_0030B5A6:
    if (v_stack_p10 == 0) goto loc_0030B3A0;
    if (local_r14 == 0) goto loc_0030B3A0;
    if (local_r14 != 1) goto loc_0030B6F1;
loc_0030B5C6:
    result = KiSearchForNewThreadsForRescheduleContext(local_rsi, v_stack_p30, result, (uint32_t)(v_stack_p28));
    goto loc_0030B3A5;
loc_0030B5D8:
    result = KiCheckMaxOverQuotaTransition(v_stack_m58, local_rsi, result, (uint32_t)(v_stack_p28));
    local_r10 = 0;
    if ((uint8_t)(result) != 0) goto loc_0030B610;
    if ((*(uint64_t *)(v_stack_m58)) >= (*(uint64_t *)(v_stack_m58 + 0x18))) goto loc_0030B6B5;
    if ((uint8_t)(v_stack_p10) != 0) goto loc_0030B30F;
    goto loc_0030B312;
loc_0030B610:
    if (((*(uint8_t *)(v_stack_m58 + 0x70)) & ((uint8_t)(v_stack_p18))) == 0) goto loc_0030B6CB;
    result = KiRemoveSchedulingGroupQueue(Arg1, v_stack_m58, (uint8_t)(v_stack_p18), (uint32_t)(v_stack_p28));
    local_r10 = 0;
    goto loc_0030B6CB;
loc_0030B630:
    result = KiFindRescheduleContextEntryForPrcb(local_rsi, Arg1, (uint8_t)(v_stack_p18), (uint32_t)(v_stack_p28));
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) & (197));
    Arg1 = (uint8_t)((Arg1) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) == 0) goto loc_0030B5C6;
    if ((*(uint8_t *)(local_rsi)) <= ((uint8_t)(v_stack_m58))) goto loc_0030B6AD;
loc_0030B680:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))));
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58))));
    if ((local_rsi + Arg1 * 8) != result) {
        Arg4 = 0;
        Arg3 = 0;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(local_rsi + Arg1 * 8, *(uint64_t *)(result), Arg3, Arg4);
    }
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m58))) + (1));
    if (((uint32_t)(local_r10)) < ((uint32_t)(*(uint8_t *)(local_rsi)))) goto loc_0030B680;
loc_0030B6AD:
    *(uint32_t *)(local_rsi + 0x4) = (uint32_t)(v_stack_m58);
    goto loc_0030B5C6;
loc_0030B6B5:
    result = KiRecomputeGroupSchedulingRank(local_rsi, v_stack_m58, Arg1, Arg4);
    local_r10 = 0;
    if (local_r14 == v_stack_m58) goto loc_0030B6DB;
loc_0030B6CB:
    goto loc_0030B307;
loc_0030B6DB:
    v_stack_p20 = (uint8_t)(v_stack_p18);
    goto loc_0030B6CB;
loc_0030B6E2:
    if ((*(uint32_t *)(v_stack_m58 + 0x7C)) == ((uint32_t)((uint32_t)(v_stack_p28)))) goto loc_0030B322;
    goto loc_0030B506;
loc_0030B6F1:
    if ((*(uint64_t *)(local_r14 + 0x1A0)) != 1) goto loc_0030B6F1;
loc_0030B70B:
    local_r15 = 0;
loc_0030B720:
    result = KiProcessScbTracingList(Arg1, v_stack_p28, v_stack_p22, (uint32_t)(v_stack_p28));
    goto loc_0030B40D;
loc_0030B732:
    result = KiReadyDeferredReadyList(Arg1, v_stack_p30, v_stack_p22, (uint32_t)(v_stack_p28));
    goto loc_0030B416;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg1` | `+ 0x8BD8` | `64` | `R` |
| `Arg3` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030B220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
