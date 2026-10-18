# KiRescheduleThreadAfterAffinityChange

- RVA: `0x0030C9E8`–`0x0030CF17` (길이 `1,327` bytes)
- VA: `0x000000014030C9E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073E4C`
- 디코드: `340`개 명령, `1,327/1,327` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0030CAB3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030CAC6` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030CB32` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030CB74` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030CC4A` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0030CC68` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0030CCC1` → [KeCheckProcessorAffinityEx](KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x0030CD76` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0030CDA0` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0030CDB6` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0030CE35` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0030CE5B` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0030CE78` → [KiRemoveThreadFromAnyReadyQueue](../20/KiRemoveThreadFromAnyReadyQueue_function_002015E4.md) (function, `0x002015E4`)
- `0x0030CE8A` → [KiPrepareReadyThreadForRescheduling](../39/KiPrepareReadyThreadForRescheduling_function_00397F2C.md) (function, `0x00397F2C`)

### Direct callers
- [KiSetAffinityThread](../2C/KiSetAffinityThread_function_002CE010.md) at `0x002CE1C3`
- [KiUpdateThreadCpuSets](KiUpdateThreadCpuSets_function_0030313C.md) at `0x003031E1`

### Static image references
- `0x0030CA53` → RVA `0x00F231B0` (`.data`; read)
- `0x0030CB37` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0030CC1E` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0030CCD9` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x0030CDFE` → RVA `0x00FC5007` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030C9E8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0030C9ED  55                              push rbp
0030C9EE  56                              push rsi
0030C9EF  57                              push rdi
0030C9F0  41 54                           push r12
0030C9F2  41 55                           push r13
0030C9F4  41 56                           push r14
0030C9F6  41 57                           push r15
0030C9F8  48 83 EC 20                     sub rsp, 0x20
0030C9FC  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0030CA05  45 33 F6                        xor r14d, r14d
0030CA08  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
0030CA10  4C 8B D2                        mov r10, rdx
0030CA13  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
0030CA1B  48 8B E9                        mov rbp, rcx
0030CA1E  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
0030CA26  41 8B FE                        mov edi, r14d
0030CA29  45 0F B6 C1                     movzx r8d, r9b
0030CA2D  41 8D 5E 02                     lea ebx, [r14 + 2]
0030CA31  44 88 74 24 78                  mov byte ptr [rsp + 0x78], r14b
0030CA36  41 83 E8 01                     sub r8d, 1
0030CA3A  0F 84 25 04 00 00               je 0x14030ce65
0030CA40  41 83 E8 01                     sub r8d, 1
0030CA44  0F 85 5D 02 00 00               jne 0x14030cca7
0030CA4A  48 85 D2                        test rdx, rdx
0030CA4D  0F 84 63 01 00 00               je 0x14030cbb6
0030CA53  48 8B 05 56 67 C1 00            mov rax, qword ptr [rip + 0xc16756]
0030CA5A  41 8B 4F 24                     mov ecx, dword ptr [r15 + 0x24]
0030CA5E  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
0030CA61  8B D1                           mov edx, ecx
0030CA63  41 0F B7 02                     movzx eax, word ptr [r10]
0030CA67  C1 EA 06                        shr edx, 6
0030CA6A  3B D0                           cmp edx, eax
0030CA6C  73 15                           jae 0x14030ca83
0030CA6E  49 8B 54 D2 08                  mov rdx, qword ptr [r10 + rdx*8 + 8]
0030CA73  83 E1 3F                        and ecx, 0x3f
0030CA76  48 D3 EA                        shr rdx, cl
0030CA79  0F BA E2 00                     bt edx, 0
0030CA7D  0F 82 33 01 00 00               jb 0x14030cbb6
0030CA83  8A 85 84 01 00 00               mov al, byte ptr [rbp + 0x184]
0030CA89  3A C3                           cmp al, bl
0030CA8B  0F 85 7D 04 00 00               jne 0x14030cf0e
0030CA91  F0 0F BA 6D 78 0C               lock bts dword ptr [rbp + 0x78], 0xc
0030CA97  4D 39 77 10                     cmp qword ptr [r15 + 0x10], r14
0030CA9B  0F 85 15 01 00 00               jne 0x14030cbb6
0030CAA1  48 8B BE E8 37 00 00            mov rdi, qword ptr [rsi + 0x37e8]
0030CAA8  33 D2                           xor edx, edx
0030CAAA  48 8B CF                        mov rcx, rdi
0030CAAD  41 B8 F0 00 00 00               mov r8d, 0xf0
0030CAB3  E8 88 A1 3B 00                  call 0x1406c6c40
0030CAB8  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0030CAC0  4C 8B C5                        mov r8, rbp
0030CAC3  48 8B CF                        mov rcx, rdi
0030CAC6  E8 E5 FB FF FF                  call 0x14030c6b0
0030CACB  44 0F B6 07                     movzx r8d, byte ptr [rdi]
0030CACF  4D 8B CE                        mov r9, r14
0030CAD2  41 8B D6                        mov edx, r14d
0030CAD5  41 3B D0                        cmp edx, r8d
0030CAD8  73 18                           jae 0x14030caf2
0030CADA  8B C2                           mov eax, edx
0030CADC  48 8D 0C 80                     lea rcx, [rax + rax*4]
0030CAE0  48 8D 04 CF                     lea rax, [rdi + rcx*8]
0030CAE4  4C 39 78 10                     cmp qword ptr [rax + 0x10], r15
0030CAE8  74 04                           je 0x14030caee
0030CAEA  FF C2                           inc edx
0030CAEC  EB E7                           jmp 0x14030cad5
0030CAEE  4C 8D 48 10                     lea r9, [rax + 0x10]
0030CAF2  41 08 59 22                     or byte ptr [r9 + 0x22], bl
0030CAF6  45 0F B6 51 20                  movzx r10d, byte ptr [r9 + 0x20]
0030CAFB  49 8B 09                        mov rcx, qword ptr [r9]
0030CAFE  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0030CB02  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
0030CB06  41 8A C2                        mov al, r10b
0030CB09  24 C5                           and al, 0xc5
0030CB0B  0C 05                           or al, 5
0030CB0D  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0030CB11  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0030CB15  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
0030CB1A  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
0030CB1E  44 84 D3                        test bl, r10b
0030CB21  0F 85 6D 03 00 00               jne 0x14030ce94
0030CB27  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
0030CB2F  48 8B CF                        mov rcx, rdi
0030CB32  E8 E9 BA F4 FF                  call 0x140258620
0030CB37  F7 05 D3 9F CB 00 00 04 00 00   test dword ptr [rip + 0xcb9fd3], 0x400
0030CB41  44 88 74 24 78                  mov byte ptr [rsp + 0x78], r14b
0030CB46  44 0F 45 F3                     cmovne r14d, ebx
0030CB4A  33 C0                           xor eax, eax
0030CB4C  8B D8                           mov ebx, eax
0030CB4E  38 07                           cmp byte ptr [rdi], al
0030CB50  76 40                           jbe 0x14030cb92
0030CB52  44 8A E0                        mov r12b, al
0030CB55  4C 8B 8C 24 A0 00 00 00         mov r9, qword ptr [rsp + 0xa0]
0030CB5D  45 8B C6                        mov r8d, r14d
0030CB60  8B C3                           mov eax, ebx
0030CB62  48 8B D6                        mov rdx, rsi
0030CB65  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0030CB6D  48 03 C8                        add rcx, rax
0030CB70  48 8D 0C CF                     lea rcx, [rdi + rcx*8]
0030CB74  E8 57 04 00 00                  call 0x14030cfd0
0030CB79  44 0A E0                        or r12b, al
0030CB7C  FF C3                           inc ebx
0030CB7E  0F B6 07                        movzx eax, byte ptr [rdi]
0030CB81  3B D8                           cmp ebx, eax
0030CB83  72 D0                           jb 0x14030cb55
0030CB85  44 88 64 24 78                  mov byte ptr [rsp + 0x78], r12b
0030CB8A  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
0030CB92  45 33 F6                        xor r14d, r14d
0030CB95  83 7F 08 01                     cmp dword ptr [rdi + 8], 1
0030CB99  75 1B                           jne 0x14030cbb6
0030CB9B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0030CB9F  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030CBA6  8A 41 01                        mov al, byte ptr [rcx + 1]
0030CBA9  FE C0                           inc al
0030CBAB  88 41 01                        mov byte ptr [rcx + 1], al
0030CBAE  3A 01                           cmp al, byte ptr [rcx]
0030CBB0  72 04                           jb 0x14030cbb6
0030CBB2  44 88 71 01                     mov byte ptr [rcx + 1], r14b
0030CBB6  4D 85 FF                        test r15, r15
0030CBB9  74 5E                           je 0x14030cc19
0030CBBB  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
0030CBC3  4D 8B C6                        mov r8, r14
0030CBC6  41 8B D6                        mov edx, r14d
0030CBC9  4D 8B 0A                        mov r9, qword ptr [r10]
0030CBCC  41 8B 0A                        mov ecx, dword ptr [r10]
0030CBCF  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0030CBD3  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
0030CBDB  83 E1 01                        and ecx, 1
0030CBDE  0F 84 B1 00 00 00               je 0x14030cc95
0030CBE4  83 F9 01                        cmp ecx, 1
0030CBE7  75 15                           jne 0x14030cbfe
0030CBE9  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0030CBF0  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0030CBF7  49 83 C0 08                     add r8, 8
0030CBFB  0F B6 10                        movzx edx, byte ptr [rax]
0030CBFE  85 D2                           test edx, edx
0030CC00  74 12                           je 0x14030cc14
0030CC02  8D 42 FF                        lea eax, [rdx - 1]
0030CC05  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030CC09  8B D0                           mov edx, eax
0030CC0B  F0 4C 21 71 30                  lock and qword ptr [rcx + 0x30], r14
0030CC10  85 C0                           test eax, eax
0030CC12  75 EE                           jne 0x14030cc02
0030CC14  33 C0                           xor eax, eax
0030CC16  49 89 02                        mov qword ptr [r10], rax
0030CC19  4D 85 ED                        test r13, r13
0030CC1C  74 4F                           je 0x14030cc6d
0030CC1E  F7 05 10 9F CB 00 00 00 20 00   test dword ptr [rip + 0xcb9f10], 0x200000
0030CC28  74 64                           je 0x14030cc8e
0030CC2A  41 0F 0D 0C 24                  prefetchw byte ptr [r12]
0030CC2F  49 8B 04 24                     mov rax, qword ptr [r12]
0030CC33  48 85 C0                        test rax, rax
0030CC36  75 17                           jne 0x14030cc4f
0030CC38  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0030CC3D  49 8B C4                        mov rax, r12
0030CC40  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
0030CC45  74 26                           je 0x14030cc6d
0030CC47  49 8B CC                        mov rcx, r12
0030CC4A  E8 51 AE F0 FF                  call 0x140217aa0
0030CC4F  48 8D 48 08                     lea rcx, [rax + 8]
0030CC53  4D 89 34 24                     mov qword ptr [r12], r14
0030CC57  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
0030CC5C  48 8B C2                        mov rax, rdx
0030CC5F  48 87 01                        xchg qword ptr [rcx], rax
0030CC62  32 C2                           xor al, dl
0030CC64  A8 04                           test al, 4
0030CC66  74 05                           je 0x14030cc6d
0030CC68  E8 B3 AF F0 FF                  call 0x140217c20
0030CC6D  4C 89 75 40                     mov qword ptr [rbp + 0x40], r14
0030CC71  44 38 74 24 78                  cmp byte ptr [rsp + 0x78], r14b
0030CC76  75 55                           jne 0x14030cccd
0030CC78  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0030CC7D  48 83 C4 20                     add rsp, 0x20
0030CC81  41 5F                           pop r15
0030CC83  41 5E                           pop r14
0030CC85  41 5D                           pop r13
0030CC87  41 5C                           pop r12
0030CC89  5F                              pop rdi
0030CC8A  5E                              pop rsi
0030CC8B  5D                              pop rbp
0030CC8C  C3                              ret
0030CC8D  CC                              int3
0030CC8E  F0 4D 21 75 00                  lock and qword ptr [r13], r14
0030CC93  EB D8                           jmp 0x14030cc6d
0030CC95  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0030CC9D  BA 01 00 00 00                  mov edx, 1
0030CCA2  E9 5B FF FF FF                  jmp 0x14030cc02
0030CCA7  41 83 F8 01                     cmp r8d, 1
0030CCAB  0F 85 05 FF FF FF               jne 0x14030cbb6
0030CCB1  4D 85 D2                        test r10, r10
0030CCB4  0F 84 FC FE FF FF               je 0x14030cbb6
0030CCBA  41 8B 57 24                     mov edx, dword ptr [r15 + 0x24]
0030CCBE  49 8B CA                        mov rcx, r10
0030CCC1  E8 8A 84 FF FF                  call 0x140305150
0030CCC6  85 C0                           test eax, eax
0030CCC8  E9 CE FD FF FF                  jmp 0x14030ca9b
0030CCCD  45 8B FE                        mov r15d, r14d
0030CCD0  44 38 37                        cmp byte ptr [rdi], r14b
0030CCD3  0F 86 96 00 00 00               jbe 0x14030cd6f
0030CCD9  4C 8D 2D 80 05 CC 00            lea r13, [rip + 0xcc0580]
0030CCE0  41 BC 02 00 00 00               mov r12d, 2
0030CCE6  41 8B C7                        mov eax, r15d
0030CCE9  48 8D 2C 80                     lea rbp, [rax + rax*4]
0030CCED  8A 44 EF 33                     mov al, byte ptr [rdi + rbp*8 + 0x33]
0030CCF1  48 8B 5C EF 10                  mov rbx, qword ptr [rdi + rbp*8 + 0x10]
0030CCF6  A8 10                           test al, 0x10
0030CCF8  75 0B                           jne 0x14030cd05
0030CCFA  A8 08                           test al, 8
0030CCFC  74 21                           je 0x14030cd1f
0030CCFE  90                              nop
0030CCFF  44 38 73 07                     cmp byte ptr [rbx + 7], r14b
0030CD03  74 1A                           je 0x14030cd1f
0030CD05  8A 86 D9 35 00 00               mov al, byte ptr [rsi + 0x35d9]
0030CD0B  84 C0                           test al, al
0030CD0D  75 71                           jne 0x14030cd80
0030CD0F  C6 86 D9 35 00 00 01            mov byte ptr [rsi + 0x35d9], 1
0030CD16  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0030CD19  89 86 DC 35 00 00               mov dword ptr [rsi + 0x35dc], eax
0030CD1F  44 84 64 EF 33                  test byte ptr [rdi + rbp*8 + 0x33], r12b
0030CD24  0F 85 26 01 00 00               jne 0x14030ce50
0030CD2A  F6 44 EF 33 04                  test byte ptr [rdi + rbp*8 + 0x33], 4
0030CD2F  74 15                           je 0x14030cd46
0030CD31  48 8B 8B B8 8E 00 00            mov rcx, qword ptr [rbx + 0x8eb8]
0030CD38  0F BE 54 EF 34                  movsx edx, byte ptr [rdi + rbp*8 + 0x34]
0030CD3D  48 85 C9                        test rcx, rcx
0030CD40  0F 85 86 00 00 00               jne 0x14030cdcc
0030CD46  F6 44 EF 33 01                  test byte ptr [rdi + rbp*8 + 0x33], 1
0030CD4B  74 0D                           je 0x14030cd5a
0030CD4D  48 8B 44 EF 28                  mov rax, qword ptr [rdi + rbp*8 + 0x28]
0030CD52  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
0030CD5A  0F B6 07                        movzx eax, byte ptr [rdi]
0030CD5D  41 FF C7                        inc r15d
0030CD60  41 BE 00 00 00 00               mov r14d, 0
0030CD66  44 3B F8                        cmp r15d, eax
0030CD69  0F 82 77 FF FF FF               jb 0x14030cce6
0030CD6F  48 8D 8E D8 35 00 00            lea rcx, [rsi + 0x35d8]
0030CD76  E8 85 54 F4 FF                  call 0x140252200
0030CD7B  E9 F8 FE FF FF                  jmp 0x14030cc78
0030CD80  3C 01                           cmp al, 1
0030CD82  75 3F                           jne 0x14030cdc3
0030CD84  8B 96 DC 35 00 00               mov edx, dword ptr [rsi + 0x35dc]
0030CD8A  3B 53 24                        cmp edx, dword ptr [rbx + 0x24]
0030CD8D  74 90                           je 0x14030cd1f
0030CD8F  4C 8D B6 E0 35 00 00            lea r14, [rsi + 0x35e0]
0030CD96  44 88 A6 D9 35 00 00            mov byte ptr [rsi + 0x35d9], r12b
0030CD9D  49 8B CE                        mov rcx, r14
0030CDA0  E8 4B E9 F4 FF                  call 0x14025b6f0
0030CDA5  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
0030CDAC  49 8B CE                        mov rcx, r14
0030CDAF  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
0030CDB6  E8 05 E9 F4 FF                  call 0x14025b6c0
0030CDBB  45 33 F6                        xor r14d, r14d
0030CDBE  E9 5C FF FF FF                  jmp 0x14030cd1f
0030CDC3  4C 8D B6 E0 35 00 00            lea r14, [rsi + 0x35e0]
0030CDCA  EB D9                           jmp 0x14030cda5
0030CDCC  4C 39 B6 B8 8E 00 00            cmp qword ptr [rsi + 0x8eb8], r14
0030CDD3  0F 84 6D FF FF FF               je 0x14030cd46
0030CDD9  48 3B F3                        cmp rsi, rbx
0030CDDC  0F 84 64 FF FF FF               je 0x14030cd46
0030CDE2  8B 09                           mov ecx, dword ptr [rcx]
0030CDE4  8B C1                           mov eax, ecx
0030CDE6  25 00 00 04 00                  and eax, 0x40000
0030CDEB  0F BA E1 14                     bt ecx, 0x14
0030CDEF  0F 83 01 01 00 00               jae 0x14030cef6
0030CDF5  48 8B 8E B8 8E 00 00            mov rcx, qword ptr [rsi + 0x8eb8]
0030CDFC  33 C0                           xor eax, eax
0030CDFE  38 05 03 82 CB 00               cmp byte ptr [rip + 0xcb8203], al
0030CE04  44 89 61 0C                     mov dword ptr [rcx + 0xc], r12d
0030CE08  44 8B 73 24                     mov r14d, dword ptr [rbx + 0x24]
0030CE0C  75 13                           jne 0x14030ce21
0030CE0E  43 0F B6 44 75 01               movzx eax, byte ptr [r13 + r14*2 + 1]
0030CE14  47 0F B6 74 75 00               movzx r14d, byte ptr [r13 + r14*2]
0030CE1A  41 C1 E6 06                     shl r14d, 6
0030CE1E  44 0B F0                        or r14d, eax
0030CE21  44 89 71 08                     mov dword ptr [rcx + 8], r14d
0030CE25  8B 05 E9 9C CB 00               mov eax, dword ptr [rip + 0xcb9ce9]
0030CE2B  A8 20                           test al, 0x20
0030CE2D  74 0B                           je 0x14030ce3a
0030CE2F  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
0030CE32  41 8B D4                        mov edx, r12d
0030CE35  E8 86 E4 1E 00                  call 0x1404fb2c0
0030CE3A  41 8B D6                        mov edx, r14d
0030CE3D  B9 C2 00 00 40                  mov ecx, 0x400000c2
0030CE42  48 C1 EA 20                     shr rdx, 0x20
0030CE46  41 8B C6                        mov eax, r14d
0030CE49  0F 30                           wrmsr
0030CE4B  E9 F6 FE FF FF                  jmp 0x14030cd46
0030CE50  48 8B 4C EF 28                  mov rcx, qword ptr [rdi + rbp*8 + 0x28]
0030CE55  45 33 C0                        xor r8d, r8d
0030CE58  48 8B D3                        mov rdx, rbx
0030CE5B  E8 EC E8 FF FF                  call 0x14030b74c
0030CE60  E9 C5 FE FF FF                  jmp 0x14030cd2a
0030CE65  0F BE 99 C3 00 00 00            movsx ebx, byte ptr [rcx + 0xc3]
0030CE6C  4C 8B C5                        mov r8, rbp
0030CE6F  44 8B CB                        mov r9d, ebx
0030CE72  49 8B D5                        mov rdx, r13
0030CE75  49 8B CF                        mov rcx, r15
0030CE78  E8 67 47 EF FF                  call 0x1402015e4
0030CE7D  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
0030CE85  8B D3                           mov edx, ebx
0030CE87  48 8B CD                        mov rcx, rbp
0030CE8A  E8 9D B0 08 00                  call 0x140397f2c
0030CE8F  E9 22 FD FF FF                  jmp 0x14030cbb6
0030CE94  45 8B C6                        mov r8d, r14d
0030CE97  44 38 37                        cmp byte ptr [rdi], r14b
0030CE9A  77 12                           ja 0x14030ceae
0030CE9C  44 84 D3                        test bl, r10b
0030CE9F  0F 84 82 FC FF FF               je 0x14030cb27
0030CEA5  44 89 77 04                     mov dword ptr [rdi + 4], r14d
0030CEA9  E9 79 FC FF FF                  jmp 0x14030cb27
0030CEAE  41 8B C0                        mov eax, r8d
0030CEB1  48 8D 14 85 02 00 00 00         lea rdx, [rax*4 + 2]
0030CEB9  48 03 D0                        add rdx, rax
0030CEBC  48 8D 14 D7                     lea rdx, [rdi + rdx*8]
0030CEC0  49 3B D1                        cmp rdx, r9
0030CEC3  74 24                           je 0x14030cee9
0030CEC5  08 5A 22                        or byte ptr [rdx + 0x22], bl
0030CEC8  48 8B 0A                        mov rcx, qword ptr [rdx]
0030CECB  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0030CECF  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
0030CED3  8A 42 20                        mov al, byte ptr [rdx + 0x20]
0030CED6  24 C5                           and al, 0xc5
0030CED8  0C 05                           or al, 5
0030CEDA  88 42 20                        mov byte ptr [rdx + 0x20], al
0030CEDD  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0030CEE1  80 62 21 FE                     and byte ptr [rdx + 0x21], 0xfe
0030CEE5  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
0030CEE9  0F B6 07                        movzx eax, byte ptr [rdi]
0030CEEC  41 FF C0                        inc r8d
0030CEEF  44 3B C0                        cmp r8d, eax
0030CEF2  72 BA                           jb 0x14030ceae
0030CEF4  EB A6                           jmp 0x14030ce9c
0030CEF6  85 C0                           test eax, eax
0030CEF8  0F 84 48 FE FF FF               je 0x14030cd46
0030CEFE  0F B6 C1                        movzx eax, cl
0030CF01  3B C2                           cmp eax, edx
0030CF03  0F 8D 3D FE FF FF               jge 0x14030cd46
0030CF09  E9 E7 FE FF FF                  jmp 0x14030cdf5
0030CF0E  80 4D 70 08                     or byte ptr [rbp + 0x70], 8
0030CF12  E9 9F FC FF FF                  jmp 0x14030cbb6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiRescheduleThreadAfterAffinityChange(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_r14 = 0;
    v_stack_p20 = 0;
    a3 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_0030CE65;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_not_equal) goto loc_0030CCA7;
    if (a2 == 0) goto loc_0030CBB6;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12674902) + (unsigned int)(*(unsigned int *)(a5 + 36)) * 4))))) >> (6));
    if (((unsigned int)(a2)) >= ((unsigned int)(*(unsigned __int16 *)(a2)))) goto loc_0030CA83;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12674902) + (unsigned int)(*(unsigned int *)(a5 + 36)) * 4))) & (63));
    a2 = (*(unsigned __int64 *)(a2 + a2 * 8 + 8)) >> ((unsigned __int8)(a1));
    if (condition_is_below) goto loc_0030CBB6;
loc_0030CA83:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != ((unsigned __int8)(v_r14 + 2))) goto loc_0030CF0E;
loc_0030CA9B:
    if ((*(unsigned __int64 *)(a5 + 16)) != 0) goto loc_0030CBB6;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), a2, 240, a4);
    result = KiStartRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), a6, a1, a4);
loc_0030CAD5:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))))) goto loc_0030CAF2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16)) == a5) goto loc_0030CAEE;
    a2 = (unsigned int)((0) + 1);
    goto loc_0030CAD5;
loc_0030CAEE:
loc_0030CAF2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16 + 32))) & (197));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16 + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 24);
    if ((((unsigned __int8)(v_r14 + 2)) & ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16 + 32)))) != 0) goto loc_0030CE94;
loc_0030CB27:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312), a9, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16);
    v_stack_p20 = 0;
    if (((*(unsigned int *)(v_rip + 13344723)) & (0x400ULL)) != 0) { v_r14 = (unsigned int)(v_r14 + 2); }
    result = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))) <= 0) goto loc_0030CB92;
loc_0030CB55:
    a1 = (0 * 4 + 2) + (0);
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a1 * 8, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)(v_r14)), a9);
    v_r12 = (unsigned __int8)((0) | ((unsigned __int8)(result)));
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))))) goto loc_0030CB55;
    v_stack_p20 = (unsigned __int8)(v_r12);
loc_0030CB92:
    v_r14 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 8)) != 1) goto loc_0030CBB6;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 16) + 36440) + 1) = 0;
    }
    if (a5 == 0) goto loc_0030CC19;
    a4 = (*(unsigned __int64 *)(a6)) & (-2);
    v_stack_p38 = a4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a6))) & (1));
    if (condition_is_equal) goto loc_0030CC95;
    if (((unsigned int)(a1)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0030CC14;
loc_0030CC02:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030CC02;
loc_0030CC14:
    result = 0;
    *(unsigned __int64 *)(a6) = 0;
loc_0030CC19:
    if (a7 == 0) goto loc_0030CC6D;
    if (((*(unsigned int *)(v_rip + 13344528)) & (0x200000ULL)) == 0) goto loc_0030CC8E;
    if (*(unsigned __int64 *)(a8) != 0) goto loc_0030CC4F;
    if (*(unsigned __int64 *)(a8) == 0) goto loc_0030CC6D;
    result = KxWaitForLockChainValid(a8, (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
loc_0030CC4F:
    *(unsigned __int64 *)(a8) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(a8 + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(a8 + 8))));
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(a8 + 8), a3, a4);
    }
    *(unsigned __int64 *)(a1 + 64) = 0;
    if (v_stack_p20 != 0) goto loc_0030CCCD;
loc_0030CC78:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0030CC8E:
    goto loc_0030CC6D;
loc_0030CC95:
    goto loc_0030CC02;
loc_0030CCA7:
    if (((unsigned int)(a7)) != 1) goto loc_0030CBB6;
    if (a6 == 0) goto loc_0030CBB6;
    result = KeCheckProcessorAffinityEx(a6, (unsigned int)(*(unsigned int *)(a5 + 36)), a7, a4);
    goto loc_0030CA9B;
loc_0030CCCD:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))) <= 0) goto loc_0030CD6F;
loc_0030CCE6:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 51))) & (16)) != 0) goto loc_0030CD05;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 51))) & (8)) == 0) goto loc_0030CD1F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 7)) == 0) goto loc_0030CD1F;
loc_0030CD05:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13785)) != 0) goto loc_0030CD80;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13785) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36)));
loc_0030CD1F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 51)) & (2)) != 0) goto loc_0030CE50;
loc_0030CD2A:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 51)) & (4)) == 0) goto loc_0030CD46;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36536) != 0) goto loc_0030CDCC;
loc_0030CD46:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40);
    }
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))))) goto loc_0030CCE6;
loc_0030CD6F:
    result = KiFlushSoftwareInterruptBatch(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13784, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 52)), a7, a4);
    goto loc_0030CC78;
loc_0030CD80:
    if (((unsigned __int8)(result)) != 1) goto loc_0030CDC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36))) goto loc_0030CD1F;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13785) = 2;
    result = KeAddProcessorAffinityEx(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13792, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13788)), a7, a4);
loc_0030CDA5:
    result = KeAddGroupAffinityEx(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 200), a4);
    v_r14 = 0;
    goto loc_0030CD1F;
loc_0030CDC3:
    goto loc_0030CDA5;
loc_0030CDCC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) == (*(unsigned __int64 *)(gs_base + (0 + 32)) + 13792)) goto loc_0030CD46;
    if ((*(unsigned __int64 *)(gs_base + (0 + 32))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16))) goto loc_0030CD46;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 13792))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030CEF6;
loc_0030CDF5:
    result = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) + 12) = 2;
    v_r14 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 13337091)) == 0) {
        result = *(unsigned __int8 *)(v_rip + 13370752 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36)) * 2 + 1);
        v_r14 = *(unsigned __int8 *)(v_rip + 13370752 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36)) * 2);
        v_r14 = (unsigned int)((v_r14) << (6));
        v_r14 = (unsigned int)((v_r14) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) + 8) = (unsigned int)(v_r14);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13343977));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13343977)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16) + 200), a4);
    }
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> (32);
    goto loc_0030CD46;
loc_0030CE50:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 16), a3, a4);
    goto loc_0030CD2A;
loc_0030CE65:
    result = KiRemoveThreadFromAnyReadyQueue(v_r15, v_rip + 13370752, 0 + 0 * 4, (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40) + 195)))));
    result = KiPrepareReadyThreadForRescheduling(0 + 0 * 4, (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40) + 195)))), a9, (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40) + 195)))));
    goto loc_0030CBB6;
loc_0030CE94:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))) > ((unsigned __int8)(v_r14))) goto loc_0030CEAE;
loc_0030CE9C:
    if ((((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40) + 195)))) & ((unsigned __int8)(a6))) == 0) goto loc_0030CB27;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 4) = (unsigned int)(v_r14);
    goto loc_0030CB27;
loc_0030CEAE:
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14)))));
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8) != ((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + 0 + 0 * 4 * 8 + 40) + 195)))))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8 + 16) = result;
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8 + 32);
        result = (unsigned __int8)((result) & (197));
        result = (unsigned __int8)((result) | (5));
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8 + 32) = (unsigned __int8)(result);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8 + 24) = result;
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) + 1);
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))))) goto loc_0030CEAE;
    goto loc_0030CE9C;
loc_0030CEF6:
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312))) == 0) goto loc_0030CD46;
    if (((unsigned int)((unsigned __int8)(a1))) >= ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14312) + a2 * 8))) goto loc_0030CD46;
    goto loc_0030CDF5;
loc_0030CF0E:
    goto loc_0030CBB6;
}
```

## 5. (Beta) C Style

```c
int64_t KiRescheduleThreadAfterAffinityChange(void *Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4, void *Arg5, void *Arg6, int64_t Arg7, void *Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint8_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_r14 = 0;
    v_stack_p20 = 0;
    Arg3 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_0030CE65;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_not_equal) goto loc_0030CCA7;
    if (Arg2 == NULL) goto loc_0030CBB6;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC16756) + (uint32_t)(*(uint32_t *)(arg5 + 0x24)) * 4))))) >> (6));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(*(uint16_t *)(arg2)))) goto loc_0030CA83;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC16756) + (uint32_t)(*(uint32_t *)(arg5 + 0x24)) * 4))) & (63));
    Arg2 = (*(uint64_t *)(arg2 + arg2 * 8 + 0x8)) >> ((uint8_t)(Arg1));
    if (condition_is_below) goto loc_0030CBB6;
loc_0030CA83:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != ((uint8_t)(local_r14 + 2))) goto loc_0030CF0E;
loc_0030CA9B:
    if ((*(uint64_t *)(arg5 + 0x10)) != 0) goto loc_0030CBB6;
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), Arg2, 240, Arg4);
    result = KiStartRescheduleContext(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), Arg6, Arg1, Arg4);
loc_0030CAD5:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))))) goto loc_0030CAF2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10)) == Arg5) goto loc_0030CAEE;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0030CAD5;
loc_0030CAEE:
loc_0030CAF2:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20))) & (197));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20) = (uint8_t)(result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x18);
    if ((((uint8_t)(local_r14 + 2)) & ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10 + 0x20)))) != 0) goto loc_0030CE94;
loc_0030CB27:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8), Arg9, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0 + 0 * 4 * 8 + 16);
    v_stack_p20 = 0;
    if (((*(uint32_t *)(v_rip + 0xCB9FD3)) & (0x400ULL)) != 0) { local_r14 = (uint32_t)(local_r14 + 2); }
    result = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))) <= 0) goto loc_0030CB92;
loc_0030CB55:
    Arg1 = (0 * 4 + 2) + (0);
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + Arg1 * 8, *(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)(local_r14)), Arg9);
    local_r12 = (uint8_t)((0) | ((uint8_t)(result)));
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))))) goto loc_0030CB55;
    v_stack_p20 = (uint8_t)(local_r12);
loc_0030CB92:
    local_r14 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x8)) != 1) goto loc_0030CBB6;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    if (Arg5 == NULL) goto loc_0030CC19;
    Arg4 = (*(uint64_t *)(arg6)) & (-2);
    v_stack_p38 = Arg4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg6))) & (1));
    if (condition_is_equal) goto loc_0030CC95;
    if (((uint32_t)(Arg1)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030CC14;
loc_0030CC02:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030CC02;
loc_0030CC14:
    result = 0;
    *(uint64_t *)(arg6) = 0;
loc_0030CC19:
    if (Arg7 == 0) goto loc_0030CC6D;
    if (((*(uint32_t *)(v_rip + 0xCB9F10)) & (0x200000ULL)) == 0) goto loc_0030CC8E;
    if (*(uint64_t *)(arg8) != 0) goto loc_0030CC4F;
    if (*(uint64_t *)(arg8) == 0) goto loc_0030CC6D;
    result = KxWaitForLockChainValid(Arg8, (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
loc_0030CC4F:
    *(uint64_t *)(arg8) = 0;
    result = (uint8_t)((*(uint64_t *)(arg8 + 0x8)) ^ ((uint8_t)(*(uint64_t *)(arg8 + 0x8))));
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(uint64_t *)(arg8 + 0x8), Arg3, Arg4);
    }
    *(uint64_t *)(arg1 + 0x40) = 0;
    if (v_stack_p20 != 0) goto loc_0030CCCD;
loc_0030CC78:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0030CC8E:
    goto loc_0030CC6D;
loc_0030CC95:
    goto loc_0030CC02;
loc_0030CCA7:
    if (((uint32_t)(Arg7)) != 1) goto loc_0030CBB6;
    if (Arg6 == NULL) goto loc_0030CBB6;
    result = KeCheckProcessorAffinityEx(Arg6, (uint32_t)(*(uint32_t *)(arg5 + 0x24)), Arg7, Arg4);
    goto loc_0030CA9B;
loc_0030CCCD:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))) <= 0) goto loc_0030CD6F;
loc_0030CCE6:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (16)) != 0) goto loc_0030CD05;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (8)) == 0) goto loc_0030CD1F;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_0030CD1F;
loc_0030CD05:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35D9)) != 0) goto loc_0030CD80;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35D9) = 1;
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)));
loc_0030CD1F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (2)) != 0) goto loc_0030CE50;
loc_0030CD2A:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (4)) == 0) goto loc_0030CD46;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_0030CDCC;
loc_0030CD46:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28);
    }
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))))) goto loc_0030CCE6;
loc_0030CD6F:
    result = KiFlushSoftwareInterruptBatch(*(uint64_t *)(gs_base + (0 + 0x20)) + 13784, (int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)), Arg7, Arg4);
    goto loc_0030CC78;
loc_0030CD80:
    if (((uint8_t)(result)) != 1) goto loc_0030CDC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24))) goto loc_0030CD1F;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(*(uint64_t *)(gs_base + (0 + 0x20)) + 13792, (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35DC)), Arg7, Arg4);
loc_0030CDA5:
    result = KeAddGroupAffinityEx(*(uint64_t *)(gs_base + (0 + 0x20)) + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xC8), Arg4);
    local_r14 = 0;
    goto loc_0030CD1F;
loc_0030CDC3:
    goto loc_0030CDA5;
loc_0030CDCC:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) == (*(uint64_t *)(gs_base + (0 + 0x20)) + 13792)) goto loc_0030CD46;
    if ((*(uint64_t *)(gs_base + (0 + 0x20))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))) goto loc_0030CD46;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x35E0))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030CEF6;
loc_0030CDF5:
    result = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) + 0xC) = 2;
    local_r14 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xCB8203)) == 0) {
        result = *(uint8_t *)(v_rip + 0xCC0580 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)) * 2 + 0x1);
        local_r14 = *(uint8_t *)(v_rip + 0xCC0580 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)) * 2);
        local_r14 = (uint32_t)((local_r14) << (6));
        local_r14 = (uint32_t)((local_r14) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) + 0x8) = (uint32_t)(local_r14);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCB9CE9));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB9CE9)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xC8), Arg4);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> (32);
    goto loc_0030CD46;
loc_0030CE50:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), Arg3, Arg4);
    goto loc_0030CD2A;
loc_0030CE65:
    result = KiRemoveThreadFromAnyReadyQueue(local_r15, v_rip + 13370752, 0 + 0 * 4, (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) + 0xC3)))));
    result = KiPrepareReadyThreadForRescheduling(0 + 0 * 4, (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) + 0xC3)))), Arg9, (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) + 0xC3)))));
    goto loc_0030CBB6;
loc_0030CE94:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))) > ((uint8_t)(local_r14))) goto loc_0030CEAE;
loc_0030CE9C:
    if ((((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) + 0xC3)))) & ((uint8_t)(Arg6))) == 0) goto loc_0030CB27;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x4) = (uint32_t)(local_r14);
    goto loc_0030CB27;
loc_0030CEAE:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14)))));
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + Arg2 * 8) != ((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28) + 0xC3)))))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + arg2 * 8);
        result = *(uint64_t *)(arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + arg2 * 8 + 0x10) = result;
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + arg2 * 8 + 0x20);
        result = (uint8_t)((result) & (197));
        result = (uint8_t)((result) | (5));
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + arg2 * 8 + 0x20) = (uint8_t)(result);
        result = *(uint64_t *)(arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + arg2 * 8 + 0x18) = result;
    }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) + 1);
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))))) goto loc_0030CEAE;
    goto loc_0030CE9C;
loc_0030CEF6:
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8))) == 0) goto loc_0030CD46;
    if (((uint32_t)((uint8_t)(Arg1))) >= ((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x37E8) + Arg2 * 8))) goto loc_0030CD46;
    goto loc_0030CDF5;
loc_0030CF0E:
    goto loc_0030CBB6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x70` | `8` | `R/W` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg1` | `+ 0xC3` | `8` | `R` |
| `Arg1` | `+ 0x184` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x8 + rdx*8` | `64` | `R` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x24` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `8` | `R` |
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030C9E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
