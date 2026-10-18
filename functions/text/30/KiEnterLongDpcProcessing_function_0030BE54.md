# KiEnterLongDpcProcessing

- RVA: `0x0030BE54`–`0x0030C28C` (길이 `1,080` bytes)
- VA: `0x000000014030BE54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00073CF8`
- 디코드: `293`개 명령, `1,080/1,080` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0030BF9E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030BFAD` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030BFCB` → [KiScheduleThreadToRescheduleContext](KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x0030C021` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030C0D1` → [KiReadyDeferredReadyList](KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x0030C188` → [KiCheckVpBackingLongSpinWaitHypercall](KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0030C194` → [HvlNotifyLongSpinWait](HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0030C1D7` → [KiAffinityContainsProcessorsOtherThanSelf](KiAffinityContainsProcessorsOtherThanSelf_function_0030B1B0.md) (function, `0x0030B1B0`)
- `0x0030C210` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0030C223` → [KiAcquirePrcbLocksForPreemptionAttemptSlowPath](../43/KiAcquirePrcbLocksForPreemptionAttemptSlowPath_function_00434910.md) (function, `0x00434910`)
- `0x0030C238` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030C282` → [EtwTraceLongDpcMitigationEvent](../64/EtwTraceLongDpcMitigationEvent_function_0064FCE4.md) (function, `0x0064FCE4`)

### Direct callers
- [KiExecuteAllDpcs](../25/KiExecuteAllDpcs_function_0025B740.md) at `0x0025C77D`

### Static image references
- `0x0030BFF0` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0030C136` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0030C164` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0030C17E` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0030C248` → [sub_006E0CAE](../6E/Unknown_function_006E0CAE.md) (`tail-transfer`)
  - `0x0030C24E` → [sub_006E0CAE + 0x29](../6E/Unknown_function_006E0CAE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030BE54  40 55                           push rbp
0030BE56  53                              push rbx
0030BE57  56                              push rsi
0030BE58  57                              push rdi
0030BE59  41 54                           push r12
0030BE5B  41 55                           push r13
0030BE5D  41 56                           push r14
0030BE5F  41 57                           push r15
0030BE61  48 8B EC                        mov rbp, rsp
0030BE64  48 83 EC 58                     sub rsp, 0x58
0030BE68  4C 8B EA                        mov r13, rdx
0030BE6B  48 8B F1                        mov rsi, rcx
0030BE6E  C6 45 48 00                     mov byte ptr [rbp + 0x48], 0
0030BE72  48 3B 91 38 38 00 00            cmp rdx, qword ptr [rcx + 0x3838]
0030BE79  0F 84 6C 03 00 00               je 0x14030c1eb
0030BE7F  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0030BE88  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0030BE8F  4D 85 C0                        test r8, r8
0030BE92  0F 85 5A 03 00 00               jne 0x14030c1f2
0030BE98  FB                              sti
0030BE99  48 8B 7E 38                     mov rdi, qword ptr [rsi + 0x38]
0030BE9D  33 C9                           xor ecx, ecx
0030BE9F  48 8B DE                        mov rbx, rsi
0030BEA2  0F B6 3F                        movzx edi, byte ptr [rdi]
0030BEA5  8B C7                           mov eax, edi
0030BEA7  48 89 75 D8                     mov qword ptr [rbp - 0x28], rsi
0030BEAB  C1 E8 07                        shr eax, 7
0030BEAE  85 C0                           test eax, eax
0030BEB0  0F 45 C8                        cmovne ecx, eax
0030BEB3  48 83 E3 FE                     and rbx, 0xfffffffffffffffe
0030BEB7  8B C1                           mov eax, ecx
0030BEB9  48 0B D8                        or rbx, rax
0030BEBC  48 89 5D 58                     mov qword ptr [rbp + 0x58], rbx
0030BEC0  85 C9                           test ecx, ecx
0030BEC2  0F 84 DB 02 00 00               je 0x14030c1a3
0030BEC8  83 F9 01                        cmp ecx, 1
0030BECB  75 36                           jne 0x14030bf03
0030BECD  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
0030BED4  0F B6 08                        movzx ecx, byte ptr [rax]
0030BED7  4C 8D 70 08                     lea r14, [rax + 8]
0030BEDB  85 C9                           test ecx, ecx
0030BEDD  74 24                           je 0x14030bf03
0030BEDF  44 8B E1                        mov r12d, ecx
0030BEE2  49 8B 1E                        mov rbx, qword ptr [r14]
0030BEE5  45 33 FF                        xor r15d, r15d
0030BEE8  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
0030BEEF  0F 82 6C 02 00 00               jb 0x14030c161
0030BEF5  49 83 C6 08                     add r14, 8
0030BEF9  49 83 EC 01                     sub r12, 1
0030BEFD  75 E3                           jne 0x14030bee2
0030BEFF  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
0030BF03  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
0030BF07  40 32 38                        xor dil, byte ptr [rax]
0030BF0A  0F 88 0A 03 00 00               js 0x14030c21a
0030BF10  8B 86 EC 00 00 00               mov eax, dword ptr [rsi + 0xec]
0030BF16  B9 00 08 00 00                  mov ecx, 0x800
0030BF1B  85 C1                           test ecx, eax
0030BF1D  75 08                           jne 0x14030bf27
0030BF1F  0B C1                           or eax, ecx
0030BF21  89 86 EC 00 00 00               mov dword ptr [rsi + 0xec], eax
0030BF27  4C 3B 6E 18                     cmp r13, qword ptr [rsi + 0x18]
0030BF2B  74 1F                           je 0x14030bf4c
0030BF2D  48 8B 86 38 38 00 00            mov rax, qword ptr [rsi + 0x3838]
0030BF34  48 85 C0                        test rax, rax
0030BF37  74 13                           je 0x14030bf4c
0030BF39  4C 3B E8                        cmp r13, rax
0030BF3C  74 0E                           je 0x14030bf4c
0030BF3E  41 80 BD C3 00 00 00 10         cmp byte ptr [r13 + 0xc3], 0x10
0030BF46  0F 8D 81 02 00 00               jge 0x14030c1cd
0030BF4C  32 C0                           xor al, al
0030BF4E  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
0030BF52  44 0F B6 F8                     movzx r15d, al
0030BF56  48 8B 86 38 38 00 00            mov rax, qword ptr [rsi + 0x3838]
0030BF5D  45 03 FF                        add r15d, r15d
0030BF60  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
0030BF64  41 8B FF                        mov edi, r15d
0030BF67  48 85 C0                        test rax, rax
0030BF6A  0F 84 66 01 00 00               je 0x14030c0d6
0030BF70  48 3B C8                        cmp rcx, rax
0030BF73  0F 84 5D 01 00 00               je 0x14030c0d6
0030BF79  48 85 C9                        test rcx, rcx
0030BF7C  74 09                           je 0x14030bf87
0030BF7E  8A 81 C3 00 00 00               mov al, byte ptr [rcx + 0xc3]
0030BF84  88 45 48                        mov byte ptr [rbp + 0x48], al
0030BF87  4C 8B B6 E8 37 00 00            mov r14, qword ptr [rsi + 0x37e8]
0030BF8E  33 D2                           xor edx, edx
0030BF90  48 83 65 60 00                  and qword ptr [rbp + 0x60], 0
0030BF95  49 8B CE                        mov rcx, r14
0030BF98  41 B8 F0 00 00 00               mov r8d, 0xf0
0030BF9E  E8 9D AC 3B 00                  call 0x1406c6c40
0030BFA3  45 33 C0                        xor r8d, r8d
0030BFA6  48 8D 55 58                     lea rdx, [rbp + 0x58]
0030BFAA  49 8B CE                        mov rcx, r14
0030BFAD  E8 FE 06 00 00                  call 0x14030c6b0
0030BFB2  48 8B 96 38 38 00 00            mov rdx, qword ptr [rsi + 0x3838]
0030BFB9  48 8D 45 60                     lea rax, [rbp + 0x60]
0030BFBD  45 33 C9                        xor r9d, r9d
0030BFC0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0030BFC5  4C 8B C6                        mov r8, rsi
0030BFC8  49 8B CE                        mov rcx, r14
0030BFCB  E8 D0 02 00 00                  call 0x14030c2a0
0030BFD0  83 E0 01                        and eax, 1
0030BFD3  8D 0C 85 00 00 00 00            lea ecx, [rax*4]
0030BFDA  41 0B CF                        or ecx, r15d
0030BFDD  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
0030BFE0  85 C0                           test eax, eax
0030BFE2  0F 85 49 02 00 00               jne 0x14030c231
0030BFE8  BF 00 00 00 00                  mov edi, 0
0030BFED  45 32 E4                        xor r12b, r12b
0030BFF0  F7 05 1A AB CB 00 00 04 00 00   test dword ptr [rip + 0xcbab1a], 0x400
0030BFFA  8D 47 02                        lea eax, [rdi + 2]
0030BFFD  0F 45 F8                        cmovne edi, eax
0030C000  45 33 FF                        xor r15d, r15d
0030C003  45 38 26                        cmp byte ptr [r14], r12b
0030C006  76 2D                           jbe 0x14030c035
0030C008  41 8B CF                        mov ecx, r15d
0030C00B  4C 8D 4D 60                     lea r9, [rbp + 0x60]
0030C00F  48 83 C1 02                     add rcx, 2
0030C013  44 8B C7                        mov r8d, edi
0030C016  48 8B D6                        mov rdx, rsi
0030C019  4A 8D 0C B9                     lea rcx, [rcx + r15*4]
0030C01D  49 8D 0C CE                     lea rcx, [r14 + rcx*8]
0030C021  E8 AA 0F 00 00                  call 0x14030cfd0
0030C026  44 0A E0                        or r12b, al
0030C029  41 FF C7                        inc r15d
0030C02C  41 0F B6 06                     movzx eax, byte ptr [r14]
0030C030  44 3B F8                        cmp r15d, eax
0030C033  72 D3                           jb 0x14030c008
0030C035  41 83 7E 08 01                  cmp dword ptr [r14 + 8], 1
0030C03A  75 1B                           jne 0x14030c057
0030C03C  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0030C040  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030C047  8A 41 01                        mov al, byte ptr [rcx + 1]
0030C04A  FE C0                           inc al
0030C04C  88 41 01                        mov byte ptr [rcx + 1], al
0030C04F  3A 01                           cmp al, byte ptr [rcx]
0030C051  72 04                           jb 0x14030c057
0030C053  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0030C057  48 8B CB                        mov rcx, rbx
0030C05A  41 0F B6 FC                     movzx edi, r12b
0030C05E  83 E7 01                        and edi, 1
0030C061  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030C065  C1 E7 03                        shl edi, 3
0030C068  45 33 C0                        xor r8d, r8d
0030C06B  0B 7D 50                        or edi, dword ptr [rbp + 0x50]
0030C06E  33 D2                           xor edx, edx
0030C070  83 CF 01                        or edi, 1
0030C073  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
0030C077  83 E3 01                        and ebx, 1
0030C07A  0F 84 3F 01 00 00               je 0x14030c1bf
0030C080  83 FB 01                        cmp ebx, 1
0030C083  75 15                           jne 0x14030c09a
0030C085  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030C08C  4C 8B 81 58 8E 00 00            mov r8, qword ptr [rcx + 0x8e58]
0030C093  49 83 C0 08                     add r8, 8
0030C097  0F B6 10                        movzx edx, byte ptr [rax]
0030C09A  85 D2                           test edx, edx
0030C09C  74 13                           je 0x14030c0b1
0030C09E  8D 42 FF                        lea eax, [rdx - 1]
0030C0A1  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030C0A5  8B D0                           mov edx, eax
0030C0A7  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030C0AD  85 C0                           test eax, eax
0030C0AF  75 ED                           jne 0x14030c09e
0030C0B1  33 DB                           xor ebx, ebx
0030C0B3  48 89 5D 58                     mov qword ptr [rbp + 0x58], rbx
0030C0B7  83 FF 08                        cmp edi, 8
0030C0BA  0F 83 82 01 00 00               jae 0x14030c242
0030C0C0  48 39 5D 60                     cmp qword ptr [rbp + 0x60], rbx
0030C0C4  0F 84 D1 00 00 00               je 0x14030c19b
0030C0CA  48 8D 55 60                     lea rdx, [rbp + 0x60]
0030C0CE  48 8B CE                        mov rcx, rsi
0030C0D1  E8 AA 1C 00 00                  call 0x14030dd80
0030C0D6  44 8A 4D 48                     mov r9b, byte ptr [rbp + 0x48]
0030C0DA  8B F7                           mov esi, edi
0030C0DC  48 85 DB                        test rbx, rbx
0030C0DF  0F 84 B6 00 00 00               je 0x14030c19b
0030C0E5  48 8B CB                        mov rcx, rbx
0030C0E8  45 33 C0                        xor r8d, r8d
0030C0EB  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030C0EF  33 D2                           xor edx, edx
0030C0F1  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
0030C0F5  83 E3 01                        and ebx, 1
0030C0F8  0F 84 B3 00 00 00               je 0x14030c1b1
0030C0FE  83 FB 01                        cmp ebx, 1
0030C101  75 15                           jne 0x14030c118
0030C103  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030C10A  4C 8B 81 58 8E 00 00            mov r8, qword ptr [rcx + 0x8e58]
0030C111  49 83 C0 08                     add r8, 8
0030C115  0F B6 10                        movzx edx, byte ptr [rax]
0030C118  45 8A D1                        mov r10b, r9b
0030C11B  85 D2                           test edx, edx
0030C11D  74 16                           je 0x14030c135
0030C11F  45 8A D1                        mov r10b, r9b
0030C122  8D 42 FF                        lea eax, [rdx - 1]
0030C125  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030C129  8B D0                           mov edx, eax
0030C12B  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030C131  85 C0                           test eax, eax
0030C133  75 ED                           jne 0x14030c122
0030C135  FA                              cli
0030C136  F7 05 C4 A9 CB 00 00 00 04 00   test dword ptr [rip + 0xcba9c4], 0x40000
0030C140  0F 85 0D 01 00 00               jne 0x14030c253
0030C146  D1 EE                           shr esi, 1
0030C148  40 80 E6 01                     and sil, 1
0030C14C  40 8A C6                        mov al, sil
0030C14F  48 83 C4 58                     add rsp, 0x58
0030C153  41 5F                           pop r15
0030C155  41 5E                           pop r14
0030C157  41 5D                           pop r13
0030C159  41 5C                           pop r12
0030C15B  5F                              pop rdi
0030C15C  5E                              pop rsi
0030C15D  5B                              pop rbx
0030C15E  5D                              pop rbp
0030C15F  C3                              ret
0030C160  CC                              int3
0030C161  41 FF C7                        inc r15d
0030C164  44 85 3D 41 91 CB 00            test dword ptr [rip + 0xcb9141], r15d
0030C16B  74 11                           je 0x14030c17e
0030C16D  F3 90                           pause
0030C16F  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0030C173  48 85 C0                        test rax, rax
0030C176  0F 84 6C FD FF FF               je 0x14030bee8
0030C17C  EB E3                           jmp 0x14030c161
0030C17E  8B 05 34 A9 CB 00               mov eax, dword ptr [rip + 0xcba934]
0030C184  A8 40                           test al, 0x40
0030C186  74 E5                           je 0x14030c16d
0030C188  E8 03 33 00 00                  call 0x14030f490
0030C18D  84 C0                           test al, al
0030C18F  74 DC                           je 0x14030c16d
0030C191  41 8B CF                        mov ecx, r15d
0030C194  E8 C7 32 00 00                  call 0x14030f460
0030C199  EB D4                           jmp 0x14030c16f
0030C19B  44 8A 55 48                     mov r10b, byte ptr [rbp + 0x48]
0030C19F  8B F7                           mov esi, edi
0030C1A1  EB 92                           jmp 0x14030c135
0030C1A3  4C 8D 75 D8                     lea r14, [rbp - 0x28]
0030C1A7  B9 01 00 00 00                  mov ecx, 1
0030C1AC  E9 2E FD FF FF                  jmp 0x14030bedf
0030C1B1  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0030C1B5  BA 01 00 00 00                  mov edx, 1
0030C1BA  E9 60 FF FF FF                  jmp 0x14030c11f
0030C1BF  4C 8D 45 50                     lea r8, [rbp + 0x50]
0030C1C3  BA 01 00 00 00                  mov edx, 1
0030C1C8  E9 D1 FE FF FF                  jmp 0x14030c09e
0030C1CD  49 8B 95 40 02 00 00            mov rdx, qword ptr [r13 + 0x240]
0030C1D4  48 8B CE                        mov rcx, rsi
0030C1D7  E8 D4 EF FF FF                  call 0x14030b1b0
0030C1DC  85 C0                           test eax, eax
0030C1DE  0F 84 68 FD FF FF               je 0x14030bf4c
0030C1E4  B0 01                           mov al, 1
0030C1E6  E9 63 FD FF FF                  jmp 0x14030bf4e
0030C1EB  32 C0                           xor al, al
0030C1ED  E9 5D FF FF FF                  jmp 0x14030c14f
0030C1F2  41 0F 0D 08                     prefetchw byte ptr [r8]
0030C1F6  41 8B 00                        mov eax, dword ptr [r8]
0030C1F9  8B D0                           mov edx, eax
0030C1FB  0F BA F2 15                     btr edx, 0x15
0030C1FF  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0030C204  75 F3                           jne 0x14030c1f9
0030C206  0F BA E0 15                     bt eax, 0x15
0030C20A  0F 83 88 FC FF FF               jae 0x14030be98
0030C210  E8 BB 6F F5 FF                  call 0x1402631d0
0030C215  E9 7E FC FF FF                  jmp 0x14030be98
0030C21A  4C 8D 45 58                     lea r8, [rbp + 0x58]
0030C21E  33 D2                           xor edx, edx
0030C220  48 8B CE                        mov rcx, rsi
0030C223  E8 E8 86 12 00                  call 0x140434910
0030C228  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
0030C22C  E9 DF FC FF FF                  jmp 0x14030bf10
0030C231  48 8D 55 60                     lea rdx, [rbp + 0x60]
0030C235  49 8B CE                        mov rcx, r14
0030C238  E8 E3 C3 F4 FF                  call 0x140258620
0030C23D  E9 A6 FD FF FF                  jmp 0x14030bfe8
0030C242  45 33 FF                        xor r15d, r15d
0030C245  41 38 1E                        cmp byte ptr [r14], bl
0030C248  0F 87 60 4A 3D 00               ja 0x1406e0cae
0030C24E  E9 84 4A 3D 00                  jmp 0x1406e0cd7
0030C253  40 F6 C7 03                     test dil, 3
0030C257  0F 84 E9 FE FF FF               je 0x14030c146
0030C25D  45 8A 85 C3 00 00 00            mov r8b, byte ptr [r13 + 0xc3]
0030C264  8B CE                           mov ecx, esi
0030C266  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
0030C26A  40 80 E7 01                     and dil, 1
0030C26E  D1 E9                           shr ecx, 1
0030C270  45 8A CA                        mov r9b, r10b
0030C273  80 E1 01                        and cl, 1
0030C276  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
0030C27A  49 8B CD                        mov rcx, r13
0030C27D  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
0030C282  E8 5D 3A 34 00                  call 0x14064fce4
0030C287  E9 BA FE FF FF                  jmp 0x14030c146
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiEnterLongDpcProcessing(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (88);
    v_stack_p8 = 0;
    if (a2 == (*(unsigned __int64 *)(a1 + 14392))) goto loc_0030C1EB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0030C1F2;
loc_0030BE98:
    a1 = 0;
    v_stack_m68 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56))))) >> (7));
    if ((unsigned int)(result) != 0) { a1 = (unsigned int)(result); }
    v_rbx = (0) & (-2);
    v_rbx = (v_rbx) | ((unsigned int)((unsigned int)(a1)));
    v_stack_p18 = v_rbx;
    if ((unsigned int)(a1) == 0) goto loc_0030C1A3;
    if (((unsigned int)(a1)) != 1) goto loc_0030BF03;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 36440))) == 0) goto loc_0030BF03;
loc_0030BEDF:
loc_0030BEE2:
    v_r15 = 0;
loc_0030BEE8:
    if (condition_is_below) goto loc_0030C161;
    v_r14 = (*(unsigned __int64 *)(a1 + 36440) + 8) + (8);
    v_r12 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0030BEE2;
loc_0030BF03:
    v_rdi = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56))));
    if (sign_flag) goto loc_0030C21A;
loc_0030BF10:
    result = (unsigned int)(*(unsigned int *)(a1 + 236));
    if ((((unsigned int)((unsigned int)(0x800ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 236))))) == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 236))) | ((unsigned int)((unsigned int)(0x800ULL))));
        *(unsigned int *)(a1 + 236) = (unsigned int)(result);
    }
    if (a2 == (*(unsigned __int64 *)(a1 + 24))) goto loc_0030BF4C;
    if (*(unsigned __int64 *)(a1 + 14392) == 0) goto loc_0030BF4C;
    if (a2 == (*(unsigned __int64 *)(a1 + 14392))) goto loc_0030BF4C;
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_0030C1CD;
loc_0030BF4C:
    result = 0;
loc_0030BF4E:
    v_r15 = (unsigned int)((0) + (0));
    v_stack_m58 = *(unsigned __int64 *)(a1 + 16);
    if (*(unsigned __int64 *)(a1 + 14392) == 0) goto loc_0030C0D6;
    if ((*(unsigned __int64 *)(a1 + 16)) == (*(unsigned __int64 *)(a1 + 14392))) goto loc_0030C0D6;
    result = *(unsigned __int64 *)(a1 + 14392);
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 195);
        v_stack_p8 = (unsigned __int8)(result);
    }
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_p18, a3, a4);
    a4 = 0;
    v_stack_m78 = v_stack_p20;
    result = KiScheduleThreadToRescheduleContext(*(unsigned __int64 *)(a1 + 14312), *(unsigned __int64 *)(a1 + 14392), a1, a4);
    result = (unsigned int)((result) & (1));
    a1 = (unsigned int)((result * 4) | ((unsigned int)(v_r15)));
    v_stack_p10 = (unsigned int)(a1);
    if ((unsigned int)(result) != 0) goto loc_0030C231;
loc_0030BFE8:
    v_r12 = 0;
    v_rdi = 0;
    if (((*(unsigned int *)(v_rip + 13347610)) & (0x400ULL)) != 0) { v_rdi = (unsigned int)(0 + 2); }
    v_r15 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030C035;
loc_0030C008:
    a1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 + v_r15 * 4 * 8, a1, (unsigned int)((unsigned int)(v_rdi)), v_stack_p20);
    v_r12 = (unsigned __int8)((v_r12) | ((unsigned __int8)(result)));
    v_r15 = (unsigned int)((v_r15) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030C008;
loc_0030C035:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_0030C057;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    v_rdi = (unsigned int)(((unsigned __int8)(v_r12)) & (1));
    a1 = (v_stack_p18) & (-2);
    v_rdi = (unsigned int)((v_rdi) << (3));
    a3 = 0;
    v_rdi = (unsigned int)((v_rdi) | (v_stack_p10));
    a2 = 0;
    v_rdi = (unsigned int)((v_rdi) | (1));
    v_stack_p10 = a1;
    v_rbx = (unsigned int)((v_stack_p18) & (1));
    if (condition_is_equal) goto loc_0030C1BF;
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a3 = *(unsigned __int64 *)(a1 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0030C0B1;
loc_0030C09E:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030C09E;
loc_0030C0B1:
    v_rbx = 0;
    v_stack_p18 = 0;
    if (((unsigned int)(v_rdi)) >= 8) goto loc_0030C242;
    if (v_stack_p20 == 0) goto loc_0030C19B;
    result = KiReadyDeferredReadyList(a1, v_stack_p20, a3, v_stack_p20);
loc_0030C0D6:
    if (0 == 0) goto loc_0030C19B;
    a3 = 0;
    a1 = (0) & (-2);
    a2 = 0;
    v_stack_m60 = a1;
    v_rbx = (unsigned int)((v_rbx) & (1));
    if (condition_is_equal) goto loc_0030C1B1;
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a3 = *(unsigned __int64 *)(a1 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0030C135;
loc_0030C11F:
loc_0030C122:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030C122;
loc_0030C135:
    if (((*(unsigned int *)(v_rip + 13347268)) & (0x40000ULL)) != 0) goto loc_0030C253;
loc_0030C146:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) >> (1));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
loc_0030C14F:
    v_rsp = (v_rsp) + (88);
    return (unsigned __int8)(v_rsi);
loc_0030C161:
    v_r15 = (unsigned int)((v_r15) + 1);
    if (((*(unsigned int *)(v_rip + 13340993)) & ((unsigned int)(v_r15))) == 0) goto loc_0030C17E;
loc_0030C16D:
loc_0030C16F:
    if (*(unsigned __int64 *)(v_rbx + 48) == 0) goto loc_0030BEE8;
    goto loc_0030C161;
loc_0030C17E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13347124)))) & (64)) == 0) goto loc_0030C16D;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a3 + a2 - 1 * 8), (unsigned int)((unsigned int)(a2 - 1)), a3, v_stack_p8);
    if ((unsigned __int8)(result) == 0) goto loc_0030C16D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(a2 - 1)), a3, v_stack_p8);
    goto loc_0030C16F;
loc_0030C19B:
    goto loc_0030C135;
loc_0030C1A3:
    goto loc_0030BEDF;
loc_0030C1B1:
    goto loc_0030C11F;
loc_0030C1BF:
    goto loc_0030C09E;
loc_0030C1CD:
    result = KiAffinityContainsProcessorsOtherThanSelf((unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(a2 + 576), v_stack_p10, v_stack_p8);
    if ((unsigned int)(result) == 0) goto loc_0030BF4C;
    goto loc_0030BF4E;
loc_0030C1EB:
    result = 0;
    goto loc_0030C14F;
loc_0030C1F2:
loc_0030C1F9:
    if (condition_is_not_equal) goto loc_0030C1F9;
    if (condition_is_above_or_equal) goto loc_0030BE98;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10)))), v_stack_p10, v_stack_p8);
    goto loc_0030BE98;
loc_0030C21A:
    a2 = 0;
    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath((unsigned int)((unsigned int)(v_rdi)), a2, v_stack_p18, v_stack_p8);
    goto loc_0030BF10;
loc_0030C231:
    result = KiSearchForNewThreadsForRescheduleContext(v_stack_m68, v_stack_p20, v_stack_p18, v_stack_p8);
    goto loc_0030BFE8;
loc_0030C242:
    v_r15 = 0;
loc_0030C253:
    if ((((unsigned __int8)(v_rdi)) & (3)) == 0) goto loc_0030C146;
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi))))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_p28 = (unsigned __int8)(a1);
    v_stack_p20 = (unsigned __int8)(v_rdi);
    result = EtwTraceLongDpcMitigationEvent(0, v_stack_m58, *(unsigned __int8 *)(a2 + 195), (unsigned __int8)(v_stack_p8));
    goto loc_0030C146;
}
```

## 5. (Beta) C Style

```c
int64_t KiEnterLongDpcProcessing(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (88);
    v_stack_p8 = 0;
    if (Arg2 == (*(uint64_t *)(arg1 + 0x3838))) goto loc_0030C1EB;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0030C1F2;
loc_0030BE98:
    Arg1 = 0;
    v_stack_m68 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x38))))) >> (7));
    if ((uint32_t)(result) != 0) { Arg1 = (uint32_t)(result); }
    local_rbx = (0) & (-2);
    local_rbx = (local_rbx) | ((uint32_t)((uint32_t)(Arg1)));
    v_stack_p18 = local_rbx;
    if ((uint32_t)(Arg1) == 0) goto loc_0030C1A3;
    if (((uint32_t)(Arg1)) != 1) goto loc_0030BF03;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8E58))) == 0) goto loc_0030BF03;
loc_0030BEDF:
loc_0030BEE2:
    local_r15 = 0;
loc_0030BEE8:
    if (condition_is_below) goto loc_0030C161;
    local_r14 = (*(uint64_t *)(arg1 + 0x8E58) + 8) + (8);
    local_r12 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0030BEE2;
loc_0030BF03:
    local_rdi = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x38))) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x38))));
    if (sign_flag) goto loc_0030C21A;
loc_0030BF10:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0xEC));
    if ((((uint32_t)((uint32_t)(0x800ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xEC))))) == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xEC))) | ((uint32_t)((uint32_t)(0x800ULL))));
        *(uint32_t *)(arg1 + 0xEC) = (uint32_t)(result);
    }
    if (Arg2 == (*(uint64_t *)(arg1 + 0x18))) goto loc_0030BF4C;
    if (*(uint64_t *)(arg1 + 0x3838) == 0) goto loc_0030BF4C;
    if (Arg2 == (*(uint64_t *)(arg1 + 0x3838))) goto loc_0030BF4C;
    if ((*(uint8_t *)(Arg2 + 0xC3)) >= 16) goto loc_0030C1CD;
loc_0030BF4C:
    result = 0;
loc_0030BF4E:
    local_r15 = (uint32_t)((0) + (0));
    v_stack_m58 = *(uint64_t *)(arg1 + 0x10);
    if (*(uint64_t *)(arg1 + 0x3838) == 0) goto loc_0030C0D6;
    if ((*(uint64_t *)(arg1 + 0x10)) == (*(uint64_t *)(arg1 + 0x3838))) goto loc_0030C0D6;
    result = *(uint64_t *)(arg1 + 0x3838);
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0xC3);
        v_stack_p8 = (uint8_t)(result);
    }
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_p18, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m78 = v_stack_p20;
    result = KiScheduleThreadToRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), *(uint64_t *)(arg1 + 0x3838), Arg1, Arg4);
    result = (uint32_t)((result) & (1));
    Arg1 = (uint32_t)((result * 4) | ((uint32_t)(local_r15)));
    v_stack_p10 = (uint32_t)(Arg1);
    if ((uint32_t)(result) != 0) goto loc_0030C231;
loc_0030BFE8:
    local_r12 = 0;
    local_rdi = 0;
    if (((*(uint32_t *)(v_rip + 0xCBAB1A)) & (0x400ULL)) != 0) { local_rdi = (uint32_t)(0 + 2); }
    local_r15 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030C035;
loc_0030C008:
    Arg1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 + local_r15 * 4 * 8, Arg1, (uint32_t)((uint32_t)(local_rdi)), v_stack_p20);
    local_r12 = (uint8_t)((local_r12) | ((uint8_t)(result)));
    local_r15 = (uint32_t)((local_r15) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030C008;
loc_0030C035:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_0030C057;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    local_rdi = (uint32_t)(((uint8_t)(local_r12)) & (1));
    Arg1 = (v_stack_p18) & (-2);
    local_rdi = (uint32_t)((local_rdi) << (3));
    Arg3 = 0;
    local_rdi = (uint32_t)((local_rdi) | (v_stack_p10));
    Arg2 = 0;
    local_rdi = (uint32_t)((local_rdi) | (1));
    v_stack_p10 = Arg1;
    local_rbx = (uint32_t)((v_stack_p18) & (1));
    if (condition_is_equal) goto loc_0030C1BF;
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030C0B1;
loc_0030C09E:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030C09E;
loc_0030C0B1:
    local_rbx = 0;
    v_stack_p18 = 0;
    if (((uint32_t)(local_rdi)) >= 8) goto loc_0030C242;
    if (v_stack_p20 == 0) goto loc_0030C19B;
    result = KiReadyDeferredReadyList(Arg1, v_stack_p20, Arg3, v_stack_p20);
loc_0030C0D6:
    if (0 == 0) goto loc_0030C19B;
    Arg3 = 0;
    Arg1 = (0) & (-2);
    Arg2 = 0;
    v_stack_m60 = Arg1;
    local_rbx = (uint32_t)((local_rbx) & (1));
    if (condition_is_equal) goto loc_0030C1B1;
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030C135;
loc_0030C11F:
loc_0030C122:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030C122;
loc_0030C135:
    if (((*(uint32_t *)(v_rip + 0xCBA9C4)) & (0x40000ULL)) != 0) goto loc_0030C253;
loc_0030C146:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) >> (1));
    local_rsi = (uint8_t)((local_rsi) & (1));
loc_0030C14F:
    local_rsp = (local_rsp) + (88);
    return (uint8_t)(local_rsi);
loc_0030C161:
    local_r15 = (uint32_t)((local_r15) + 1);
    if (((*(uint32_t *)(v_rip + 0xCB9141)) & ((uint32_t)(local_r15))) == 0) goto loc_0030C17E;
loc_0030C16D:
loc_0030C16F:
    if (*(uint64_t *)(local_rbx + 0x30) == 0) goto loc_0030BEE8;
    goto loc_0030C161;
loc_0030C17E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBA934)))) & (64)) == 0) goto loc_0030C16D;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(Arg3 + Arg2 - 0x1 * 8), (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, v_stack_p8);
    if ((uint8_t)(result) == 0) goto loc_0030C16D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, v_stack_p8);
    goto loc_0030C16F;
loc_0030C19B:
    goto loc_0030C135;
loc_0030C1A3:
    goto loc_0030BEDF;
loc_0030C1B1:
    goto loc_0030C11F;
loc_0030C1BF:
    goto loc_0030C09E;
loc_0030C1CD:
    result = KiAffinityContainsProcessorsOtherThanSelf((uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(Arg2 + 0x240), v_stack_p10, v_stack_p8);
    if ((uint32_t)(result) == 0) goto loc_0030BF4C;
    goto loc_0030BF4E;
loc_0030C1EB:
    result = 0;
    goto loc_0030C14F;
loc_0030C1F2:
loc_0030C1F9:
    if (condition_is_not_equal) goto loc_0030C1F9;
    if (condition_is_above_or_equal) goto loc_0030BE98;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10)))), v_stack_p10, v_stack_p8);
    goto loc_0030BE98;
loc_0030C21A:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath((uint32_t)((uint32_t)(local_rdi)), Arg2, v_stack_p18, v_stack_p8);
    goto loc_0030BF10;
loc_0030C231:
    result = KiSearchForNewThreadsForRescheduleContext(v_stack_m68, v_stack_p20, v_stack_p18, v_stack_p8);
    goto loc_0030BFE8;
loc_0030C242:
    local_r15 = 0;
loc_0030C253:
    if ((((uint8_t)(local_rdi)) & (3)) == 0) goto loc_0030C146;
    local_rdi = (uint8_t)((local_rdi) & (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi))))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_p28 = (uint8_t)(Arg1);
    v_stack_p20 = (uint8_t)(local_rdi);
    result = EtwTraceLongDpcMitigationEvent(0, v_stack_m58, *(uint8_t *)(Arg2 + 0xC3), (uint8_t)(v_stack_p8));
    goto loc_0030C146;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0xEC` | `32` | `R` |
| `Arg1` | `+ 0xEC` | `32` | `W` |
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg1` | `+ 0x3838` | `64` | `R` |
| `Arg1` | `+ 0x8E58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030BE54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
