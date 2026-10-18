# KiSoftParkElectionUnparkProcessor

- RVA: `0x0030B818`–`0x0030BD29` (길이 `1,297` bytes)
- VA: `0x000000014030B818`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073CCC`
- 디코드: `314`개 명령, `1,297/1,297` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0030B8EC` → [KiCheckVpBackingLongSpinWaitHypercall](KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0030B8F8` → [HvlNotifyLongSpinWait](HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0030B90E` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x0030B93F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030B94F` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030B95A` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030B996` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030BB36` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0030BB4C` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0030BBD3` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0030BBFF` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0030BC3B` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0030BC51` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0030BC91` → [KiAdjustReadyQueueScanOwnerOnParkingChange](KiAdjustReadyQueueScanOwnerOnParkingChange_function_0030BD30.md) (function, `0x0030BD30`)
- `0x0030BD08` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0030BD16` → [EtwTraceParkTransition](../64/EtwTraceParkTransition_function_0064FE38.md) (function, `0x0064FE38`)
- `0x0030BD1F` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- [KiSoftParkElectionDpcRoutine](../45/KiSoftParkElectionDpcRoutine_function_004508F0.md) at `0x00450A4E`

### Static image references
- `0x0030B8CC` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0030B8E2` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0030B913` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x0030B95F` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0030BA37` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x0030BB8F` → RVA `0x00FC5007` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030B818  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0030B81D  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0030B822  53                              push rbx
0030B823  55                              push rbp
0030B824  56                              push rsi
0030B825  57                              push rdi
0030B826  41 54                           push r12
0030B828  41 55                           push r13
0030B82A  41 56                           push r14
0030B82C  41 57                           push r15
0030B82E  48 83 EC 58                     sub rsp, 0x58
0030B832  48 8B A9 E8 37 00 00            mov rbp, qword ptr [rcx + 0x37e8]
0030B839  45 32 E4                        xor r12b, r12b
0030B83C  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
0030B841  4D 8B E9                        mov r13, r9
0030B844  44 88 A4 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r12b
0030B84C  4D 8B F0                        mov r14, r8
0030B84F  44 88 A4 24 A8 00 00 00         mov byte ptr [rsp + 0xa8], r12b
0030B857  48 8B F2                        mov rsi, rdx
0030B85A  48 8B D9                        mov rbx, rcx
0030B85D  48 8B C2                        mov rax, rdx
0030B860  48 83 C8 01                     or rax, 1
0030B864  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0030B869  48 8B 82 58 8E 00 00            mov rax, qword ptr [rdx + 0x8e58]
0030B870  0F B6 08                        movzx ecx, byte ptr [rax]
0030B873  4C 8D 78 08                     lea r15, [rax + 8]
0030B877  84 C9                           test cl, cl
0030B879  74 36                           je 0x14030b8b1
0030B87B  44 8B E1                        mov r12d, ecx
0030B87E  41 BD 01 00 00 00               mov r13d, 1
0030B884  49 8B 3F                        mov rdi, qword ptr [r15]
0030B887  45 33 F6                        xor r14d, r14d
0030B88A  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
0030B891  72 36                           jb 0x14030b8c9
0030B893  49 83 C7 08                     add r15, 8
0030B897  4D 2B E5                        sub r12, r13
0030B89A  75 E8                           jne 0x14030b884
0030B89C  4C 8B AC 24 B8 00 00 00         mov r13, qword ptr [rsp + 0xb8]
0030B8A4  44 8A 64 24 30                  mov r12b, byte ptr [rsp + 0x30]
0030B8A9  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
0030B8B1  8A 46 23                        mov al, byte ptr [rsi + 0x23]
0030B8B4  24 14                           and al, 0x14
0030B8B6  3C 14                           cmp al, 0x14
0030B8B8  0F 84 BE 03 00 00               je 0x14030bc7c
0030B8BE  41 BE 01 00 00 00               mov r14d, 1
0030B8C4  E9 09 01 00 00                  jmp 0x14030b9d2
0030B8C9  45 03 F5                        add r14d, r13d
0030B8CC  44 85 35 D9 99 CB 00            test dword ptr [rip + 0xcb99d9], r14d
0030B8D3  74 0D                           je 0x14030b8e2
0030B8D5  F3 90                           pause
0030B8D7  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0030B8DB  48 85 C0                        test rax, rax
0030B8DE  74 AA                           je 0x14030b88a
0030B8E0  EB E7                           jmp 0x14030b8c9
0030B8E2  8B 05 D0 B1 CB 00               mov eax, dword ptr [rip + 0xcbb1d0]
0030B8E8  A8 40                           test al, 0x40
0030B8EA  74 E9                           je 0x14030b8d5
0030B8EC  E8 9F 3B 00 00                  call 0x14030f490
0030B8F1  84 C0                           test al, al
0030B8F3  74 E0                           je 0x14030b8d5
0030B8F5  41 8B CE                        mov ecx, r14d
0030B8F8  E8 63 3B 00 00                  call 0x14030f460
0030B8FD  EB D8                           jmp 0x14030b8d7
0030B8FF  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
0030B903  45 33 C9                        xor r9d, r9d
0030B906  48 8B CE                        mov rcx, rsi
0030B909  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
0030B90E  E8 FD BE F4 FF                  call 0x140257810
0030B913  48 8B 05 EE 96 CB 00            mov rax, qword ptr [rip + 0xcb96ee]
0030B91A  66 F0 44 01 B0 6A 03 00 00      lock add word ptr [rax + 0x36a], r14w
0030B923  44 88 B4 24 A8 00 00 00         mov byte ptr [rsp + 0xa8], r14b
0030B92B  40 84 FF                        test dil, dil
0030B92E  0F 84 9E 00 00 00               je 0x14030b9d2
0030B934  33 D2                           xor edx, edx
0030B936  41 B8 F0 00 00 00               mov r8d, 0xf0
0030B93C  48 8B CD                        mov rcx, rbp
0030B93F  E8 FC B2 3B 00                  call 0x1406c6c40
0030B944  45 33 C0                        xor r8d, r8d
0030B947  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0030B94C  48 8B CD                        mov rcx, rbp
0030B94F  E8 5C 0D 00 00                  call 0x14030c6b0
0030B954  49 8B D5                        mov rdx, r13
0030B957  48 8B CD                        mov rcx, rbp
0030B95A  E8 C1 CC F4 FF                  call 0x140258620
0030B95F  8B 3D AF B1 CB 00               mov edi, dword ptr [rip + 0xcbb1af]
0030B965  45 32 E4                        xor r12b, r12b
0030B968  C1 EF 09                        shr edi, 9
0030B96B  45 33 F6                        xor r14d, r14d
0030B96E  83 E7 02                        and edi, 2
0030B971  44 38 65 00                     cmp byte ptr [rbp], r12b
0030B975  76 33                           jbe 0x14030b9aa
0030B977  41 8B CE                        mov ecx, r14d
0030B97A  4D 8B CD                        mov r9, r13
0030B97D  48 83 C1 02                     add rcx, 2
0030B981  44 8B C7                        mov r8d, edi
0030B984  48 8B D3                        mov rdx, rbx
0030B987  4A 8D 0C B1                     lea rcx, [rcx + r14*4]
0030B98B  48 8D 0C CD 00 00 00 00         lea rcx, [rcx*8]
0030B993  48 03 CD                        add rcx, rbp
0030B996  E8 35 16 00 00                  call 0x14030cfd0
0030B99B  44 0A E0                        or r12b, al
0030B99E  45 03 F7                        add r14d, r15d
0030B9A1  0F B6 45 00                     movzx eax, byte ptr [rbp]
0030B9A5  44 3B F0                        cmp r14d, eax
0030B9A8  72 CD                           jb 0x14030b977
0030B9AA  41 BE 01 00 00 00               mov r14d, 1
0030B9B0  44 39 75 08                     cmp dword ptr [rbp + 8], r14d
0030B9B4  75 1C                           jne 0x14030b9d2
0030B9B6  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0030B9BA  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030B9C1  8A 41 01                        mov al, byte ptr [rcx + 1]
0030B9C4  41 02 C6                        add al, r14b
0030B9C7  88 41 01                        mov byte ptr [rcx + 1], al
0030B9CA  3A 01                           cmp al, byte ptr [rcx]
0030B9CC  72 04                           jb 0x14030b9d2
0030B9CE  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0030B9D2  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0030B9D7  45 33 C9                        xor r9d, r9d
0030B9DA  4C 8B C0                        mov r8, rax
0030B9DD  33 D2                           xor edx, edx
0030B9DF  49 83 E0 FE                     and r8, 0xfffffffffffffffe
0030B9E3  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0030B9E8  41 23 C6                        and eax, r14d
0030B9EB  0F 84 18 02 00 00               je 0x14030bc09
0030B9F1  83 F8 01                        cmp eax, 1
0030B9F4  75 0E                           jne 0x14030ba04
0030B9F6  49 8B 80 58 8E 00 00            mov rax, qword ptr [r8 + 0x8e58]
0030B9FD  0F B6 10                        movzx edx, byte ptr [rax]
0030BA00  4C 8D 48 08                     lea r9, [rax + 8]
0030BA04  85 D2                           test edx, edx
0030BA06  74 13                           je 0x14030ba1b
0030BA08  8D 42 FF                        lea eax, [rdx - 1]
0030BA0B  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
0030BA0F  8B D0                           mov edx, eax
0030BA11  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0030BA17  85 C0                           test eax, eax
0030BA19  75 ED                           jne 0x14030ba08
0030BA1B  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
0030BA21  45 84 E4                        test r12b, r12b
0030BA24  0F 84 9D 00 00 00               je 0x14030bac7
0030BA2A  45 33 E4                        xor r12d, r12d
0030BA2D  44 38 65 00                     cmp byte ptr [rbp], r12b
0030BA31  0F 86 90 00 00 00               jbe 0x14030bac7
0030BA37  4C 8D 2D 22 18 CC 00            lea r13, [rip + 0xcc1822]
0030BA3E  4F 8D 3C A4                     lea r15, [r12 + r12*4]
0030BA42  42 8A 44 FD 33                  mov al, byte ptr [rbp + r15*8 + 0x33]
0030BA47  4A 8B 7C FD 10                  mov rdi, qword ptr [rbp + r15*8 + 0x10]
0030BA4C  A8 10                           test al, 0x10
0030BA4E  75 0B                           jne 0x14030ba5b
0030BA50  A8 08                           test al, 8
0030BA52  74 25                           je 0x14030ba79
0030BA54  90                              nop
0030BA55  80 7F 07 00                     cmp byte ptr [rdi + 7], 0
0030BA59  74 1E                           je 0x14030ba79
0030BA5B  8A 83 D9 35 00 00               mov al, byte ptr [rbx + 0x35d9]
0030BA61  84 C0                           test al, al
0030BA63  0F 85 A8 00 00 00               jne 0x14030bb11
0030BA69  44 88 B3 D9 35 00 00            mov byte ptr [rbx + 0x35d9], r14b
0030BA70  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
0030BA73  89 83 DC 35 00 00               mov dword ptr [rbx + 0x35dc], eax
0030BA79  42 F6 44 FD 33 02               test byte ptr [rbp + r15*8 + 0x33], 2
0030BA7F  0F 85 6F 01 00 00               jne 0x14030bbf4
0030BA85  42 F6 44 FD 33 04               test byte ptr [rbp + r15*8 + 0x33], 4
0030BA8B  74 16                           je 0x14030baa3
0030BA8D  48 8B 8F B8 8E 00 00            mov rcx, qword ptr [rdi + 0x8eb8]
0030BA94  42 0F BE 54 FD 34               movsx edx, byte ptr [rbp + r15*8 + 0x34]
0030BA9A  48 85 C9                        test rcx, rcx
0030BA9D  0F 85 C2 00 00 00               jne 0x14030bb65
0030BAA3  46 84 74 FD 33                  test byte ptr [rbp + r15*8 + 0x33], r14b
0030BAA8  74 0D                           je 0x14030bab7
0030BAAA  4A 8B 44 FD 28                  mov rax, qword ptr [rbp + r15*8 + 0x28]
0030BAAF  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
0030BAB7  0F B6 45 00                     movzx eax, byte ptr [rbp]
0030BABB  45 03 E6                        add r12d, r14d
0030BABE  44 3B E0                        cmp r12d, eax
0030BAC1  0F 82 77 FF FF FF               jb 0x14030ba3e
0030BAC7  80 BC 24 A0 00 00 00 00         cmp byte ptr [rsp + 0xa0], 0
0030BACF  74 1E                           je 0x14030baef
0030BAD1  8A 83 D9 35 00 00               mov al, byte ptr [rbx + 0x35d9]
0030BAD7  84 C0                           test al, al
0030BAD9  0F 85 37 01 00 00               jne 0x14030bc16
0030BADF  44 88 B3 D9 35 00 00            mov byte ptr [rbx + 0x35d9], r14b
0030BAE6  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0030BAE9  89 83 DC 35 00 00               mov dword ptr [rbx + 0x35dc], eax
0030BAEF  F7 05 1B B0 CB 00 00 20 00 00   test dword ptr [rip + 0xcbb01b], 0x2000
0030BAF9  0F 85 EF 01 00 00               jne 0x14030bcee
0030BAFF  48 83 C4 58                     add rsp, 0x58
0030BB03  41 5F                           pop r15
0030BB05  41 5E                           pop r14
0030BB07  41 5D                           pop r13
0030BB09  41 5C                           pop r12
0030BB0B  5F                              pop rdi
0030BB0C  5E                              pop rsi
0030BB0D  5D                              pop rbp
0030BB0E  5B                              pop rbx
0030BB0F  C3                              ret
0030BB10  CC                              int3
0030BB11  41 3A C6                        cmp al, r14b
0030BB14  75 46                           jne 0x14030bb5c
0030BB16  8B 93 DC 35 00 00               mov edx, dword ptr [rbx + 0x35dc]
0030BB1C  3B 57 24                        cmp edx, dword ptr [rdi + 0x24]
0030BB1F  0F 84 54 FF FF FF               je 0x14030ba79
0030BB25  4C 8D B3 E0 35 00 00            lea r14, [rbx + 0x35e0]
0030BB2C  C6 83 D9 35 00 00 02            mov byte ptr [rbx + 0x35d9], 2
0030BB33  49 8B CE                        mov rcx, r14
0030BB36  E8 B5 FB F4 FF                  call 0x14025b6f0
0030BB3B  4C 8B 87 C8 00 00 00            mov r8, qword ptr [rdi + 0xc8]
0030BB42  49 8B CE                        mov rcx, r14
0030BB45  0F B6 97 D0 00 00 00            movzx edx, byte ptr [rdi + 0xd0]
0030BB4C  E8 6F FB F4 FF                  call 0x14025b6c0
0030BB51  41 BE 01 00 00 00               mov r14d, 1
0030BB57  E9 1D FF FF FF                  jmp 0x14030ba79
0030BB5C  4C 8D B3 E0 35 00 00            lea r14, [rbx + 0x35e0]
0030BB63  EB D6                           jmp 0x14030bb3b
0030BB65  48 83 BB B8 8E 00 00 00         cmp qword ptr [rbx + 0x8eb8], 0
0030BB6D  0F 84 30 FF FF FF               je 0x14030baa3
0030BB73  48 3B DF                        cmp rbx, rdi
0030BB76  0F 84 27 FF FF FF               je 0x14030baa3
0030BB7C  8B 09                           mov ecx, dword ptr [rcx]
0030BB7E  8B C1                           mov eax, ecx
0030BB80  25 00 00 04 00                  and eax, 0x40000
0030BB85  0F BA E1 14                     bt ecx, 0x14
0030BB89  0F 83 D5 00 00 00               jae 0x14030bc64
0030BB8F  80 3D 71 94 CB 00 00            cmp byte ptr [rip + 0xcb9471], 0
0030BB96  48 8B 8B B8 8E 00 00            mov rcx, qword ptr [rbx + 0x8eb8]
0030BB9D  C7 41 0C 02 00 00 00            mov dword ptr [rcx + 0xc], 2
0030BBA4  44 8B 77 24                     mov r14d, dword ptr [rdi + 0x24]
0030BBA8  75 13                           jne 0x14030bbbd
0030BBAA  43 0F B6 44 75 01               movzx eax, byte ptr [r13 + r14*2 + 1]
0030BBB0  47 0F B6 74 75 00               movzx r14d, byte ptr [r13 + r14*2]
0030BBB6  41 C1 E6 06                     shl r14d, 6
0030BBBA  44 0B F0                        or r14d, eax
0030BBBD  44 89 71 08                     mov dword ptr [rcx + 8], r14d
0030BBC1  8B 05 4D AF CB 00               mov eax, dword ptr [rip + 0xcbaf4d]
0030BBC7  A8 20                           test al, 0x20
0030BBC9  74 0D                           je 0x14030bbd8
0030BBCB  8B 4F 24                        mov ecx, dword ptr [rdi + 0x24]
0030BBCE  BA 02 00 00 00                  mov edx, 2
0030BBD3  E8 E8 F6 1E 00                  call 0x1404fb2c0
0030BBD8  41 8B D6                        mov edx, r14d
0030BBDB  B9 C2 00 00 40                  mov ecx, 0x400000c2
0030BBE0  48 C1 EA 20                     shr rdx, 0x20
0030BBE4  41 8B C6                        mov eax, r14d
0030BBE7  0F 30                           wrmsr
0030BBE9  41 BE 01 00 00 00               mov r14d, 1
0030BBEF  E9 AF FE FF FF                  jmp 0x14030baa3
0030BBF4  4A 8B 4C FD 28                  mov rcx, qword ptr [rbp + r15*8 + 0x28]
0030BBF9  45 33 C0                        xor r8d, r8d
0030BBFC  48 8B D7                        mov rdx, rdi
0030BBFF  E8 48 FB FF FF                  call 0x14030b74c
0030BC04  E9 7C FE FF FF                  jmp 0x14030ba85
0030BC09  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
0030BC0E  41 8B D6                        mov edx, r14d
0030BC11  E9 F2 FD FF FF                  jmp 0x14030ba08
0030BC16  41 3A C6                        cmp al, r14b
0030BC19  75 40                           jne 0x14030bc5b
0030BC1B  8B 93 DC 35 00 00               mov edx, dword ptr [rbx + 0x35dc]
0030BC21  3B 56 24                        cmp edx, dword ptr [rsi + 0x24]
0030BC24  0F 84 C5 FE FF FF               je 0x14030baef
0030BC2A  C6 83 D9 35 00 00 02            mov byte ptr [rbx + 0x35d9], 2
0030BC31  48 81 C3 E0 35 00 00            add rbx, 0x35e0
0030BC38  48 8B CB                        mov rcx, rbx
0030BC3B  E8 B0 FA F4 FF                  call 0x14025b6f0
0030BC40  0F B6 96 D0 00 00 00            movzx edx, byte ptr [rsi + 0xd0]
0030BC47  48 8B CB                        mov rcx, rbx
0030BC4A  4C 8B 86 C8 00 00 00            mov r8, qword ptr [rsi + 0xc8]
0030BC51  E8 6A FA F4 FF                  call 0x14025b6c0
0030BC56  E9 94 FE FF FF                  jmp 0x14030baef
0030BC5B  48 81 C3 E0 35 00 00            add rbx, 0x35e0
0030BC62  EB DC                           jmp 0x14030bc40
0030BC64  85 C0                           test eax, eax
0030BC66  0F 84 37 FE FF FF               je 0x14030baa3
0030BC6C  0F B6 C1                        movzx eax, cl
0030BC6F  3B C2                           cmp eax, edx
0030BC71  0F 8D 2C FE FF FF               jge 0x14030baa3
0030BC77  E9 13 FF FF FF                  jmp 0x14030bb8f
0030BC7C  48 8B BE C8 00 00 00            mov rdi, qword ptr [rsi + 0xc8]
0030BC83  F0 49 31 7E 50                  lock xor qword ptr [r14 + 0x50], rdi
0030BC88  45 33 C0                        xor r8d, r8d
0030BC8B  49 8B D6                        mov rdx, r14
0030BC8E  48 8B CE                        mov rcx, rsi
0030BC91  E8 9A 00 00 00                  call 0x14030bd30
0030BC96  8A 56 23                        mov dl, byte ptr [rsi + 0x23]
0030BC99  45 8D 78 01                     lea r15d, [r8 + 1]
0030BC9D  80 E2 CF                        and dl, 0xcf
0030BCA0  41 84 D7                        test r15b, dl
0030BCA3  75 33                           jne 0x14030bcd8
0030BCA5  F0 49 09 7E 08                  lock or qword ptr [r14 + 8], rdi
0030BCAA  88 56 23                        mov byte ptr [rsi + 0x23], dl
0030BCAD  45 8B F7                        mov r14d, r15d
0030BCB0  44 88 B6 BB 38 00 00            mov byte ptr [rsi + 0x38bb], r14b
0030BCB7  41 8A FE                        mov dil, r14b
0030BCBA  44 88 84 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r8b
0030BCC2  48 3B F3                        cmp rsi, rbx
0030BCC5  0F 84 34 FC FF FF               je 0x14030b8ff
0030BCCB  44 88 B4 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r14b
0030BCD3  E9 27 FC FF FF                  jmp 0x14030b8ff
0030BCD8  40 32 FF                        xor dil, dil
0030BCDB  88 56 23                        mov byte ptr [rsi + 0x23], dl
0030BCDE  40 88 BC 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], dil
0030BCE6  4D 8B F7                        mov r14, r15
0030BCE9  E9 11 FC FF FF                  jmp 0x14030b8ff
0030BCEE  80 BC 24 A8 00 00 00 00         cmp byte ptr [rsp + 0xa8], 0
0030BCF6  0F 84 03 FE FF FF               je 0x14030baff
0030BCFC  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0030BD04  48 8D 4B 78                     lea rcx, [rbx + 0x78]
0030BD08  E8 D3 DA F3 FF                  call 0x1402497e0
0030BD0D  33 D2                           xor edx, edx
0030BD0F  48 8B CE                        mov rcx, rsi
0030BD12  44 8D 42 02                     lea r8d, [rdx + 2]
0030BD16  E8 1D 41 34 00                  call 0x14064fe38
0030BD1B  48 8D 4B 78                     lea rcx, [rbx + 0x78]
0030BD1F  E8 5C D1 F3 FF                  call 0x140248e80
0030BD24  E9 D6 FD FF FF                  jmp 0x14030baff
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSoftParkElectionUnparkProcessor(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int8 v_stack_m78;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_pA0;
    unsigned __int8 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (88);
    v_r12 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    result = (a2) | (1);
    v_stack_m60 = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))) == 0) goto loc_0030B8B1;
loc_0030B884:
    v_r14 = 0;
loc_0030B88A:
    if (condition_is_below) goto loc_0030B8C9;
    v_r15 = (*(unsigned __int64 *)(a2 + 36440) + 8) + (8);
    v_r12 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0030B884;
loc_0030B8B1:
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 35)) & (20));
    if (((unsigned __int8)(result)) == 20) goto loc_0030BC7C;
    goto loc_0030B9D2;
loc_0030B8C9:
    v_r14 = (unsigned int)((1) + ((unsigned int)(v_stack_p20)));
    if (((*(unsigned int *)(v_rip + 13343193)) & ((unsigned int)(v_r14))) == 0) goto loc_0030B8E2;
loc_0030B8D5:
loc_0030B8D7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 36440) + 8) + 48) == 0) goto loc_0030B88A;
    goto loc_0030B8C9;
loc_0030B8E2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13349328)))) & (64)) == 0) goto loc_0030B8D5;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030B8D5;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, a3, a4);
    goto loc_0030B8D7;
loc_0030B8FF:
    a4 = 0;
    v_stack_m78 = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 36440) + 8));
    result = KiUpdateThreadPriority(a2, a2, *(unsigned __int64 *)(a2 + 24), a4);
    v_stack_p10 = (unsigned __int8)(v_r14);
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 36440) + 8)) == 0) goto loc_0030B9D2;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_m60, a3, a4);
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_p20, a3, a4);
    v_r12 = 0;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13349295))) >> (9));
    v_r14 = 0;
    v_rdi = (unsigned int)((v_rdi) & (2));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030B9AA;
loc_0030B977:
    a1 = (0) + (2);
    a1 = (a1 + v_r14 * 4 * 8) + (*(unsigned __int64 *)(a1 + 14312));
    result = KiCommitRescheduleContextEntry(a1, a1, (unsigned int)((unsigned int)(v_rdi)), v_stack_p20);
    v_r12 = (unsigned __int8)((v_r12) | ((unsigned __int8)(result)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r15)));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030B977;
loc_0030B9AA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_0030B9D2;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    a4 = 0;
    a2 = 0;
    a3 = (v_stack_m60) & (-2);
    v_stack_m58 = a3;
    result = (unsigned int)((v_stack_m60) & (1));
    if (condition_is_equal) goto loc_0030BC09;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a3 + 36440);
        a2 = *(unsigned __int8 *)(result);
        a4 = result + 8;
    }
    if ((unsigned int)(a2) == 0) goto loc_0030BA1B;
loc_0030BA08:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030BA08;
loc_0030BA1B:
    if ((unsigned __int8)(v_r12) == 0) goto loc_0030BAC7;
    v_r12 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030BAC7;
loc_0030BA3E:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51))) & (16)) != 0) goto loc_0030BA5B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51))) & (8)) == 0) goto loc_0030BA79;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 7)) == 0) goto loc_0030BA79;
loc_0030BA5B:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_0030BB11;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36)));
loc_0030BA79:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (2)) != 0) goto loc_0030BBF4;
loc_0030BA85:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (4)) == 0) goto loc_0030BAA3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36536) != 0) goto loc_0030BB65;
loc_0030BAA3:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 40);
    }
    v_r12 = (unsigned int)((v_r12) + (1));
    if (((unsigned int)(v_r12)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030BA3E;
loc_0030BAC7:
    if (v_stack_p8 == 0) goto loc_0030BAEF;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_0030BC16;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36)));
loc_0030BAEF:
    if (((*(unsigned int *)(v_rip + 13348891)) & (0x2000ULL)) != 0) goto loc_0030BCEE;
loc_0030BAFF:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)(*(unsigned int *)(a2 + 36));
loc_0030BB11:
    if (((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 36)))) != 1) goto loc_0030BB5C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36))) goto loc_0030BA79;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), a3, a4);
loc_0030BB3B:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 200), a4);
    goto loc_0030BA79;
loc_0030BB5C:
    goto loc_0030BB3B;
loc_0030BB65:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_0030BAA3;
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16))) goto loc_0030BAA3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13792))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030BC64;
loc_0030BB8F:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 12) = 2;
    v_r14 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 13341809)) == 0) {
        result = *(unsigned __int8 *)(v_rip + 13375522 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36)) * 2 + 1);
        v_r14 = *(unsigned __int8 *)(v_rip + 13375522 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36)) * 2);
        v_r14 = (unsigned int)((v_r14) << (6));
        v_r14 = (unsigned int)((v_r14) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 8) = (unsigned int)(v_r14);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13348685));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13348685)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 200), a4);
    }
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> (32);
    goto loc_0030BAA3;
loc_0030BBF4:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16), a3, a4);
    goto loc_0030BA85;
loc_0030BC09:
    goto loc_0030BA08;
loc_0030BC16:
    if (((unsigned __int8)(result)) != 1) goto loc_0030BC5B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(a2 + 36))) goto loc_0030BAEF;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    v_rbx = (a1) + (0x35E0ULL);
    result = KeAddProcessorAffinityEx(v_rbx, (unsigned int)(*(unsigned int *)(a1 + 13788)), a3, v_stack_p40);
loc_0030BC40:
    result = KeAddGroupAffinityEx(v_rbx, *(unsigned __int8 *)(a2 + 208), *(unsigned __int64 *)(a2 + 200), v_stack_p40);
    goto loc_0030BAEF;
loc_0030BC5B:
    v_rbx = (v_rbx) + (0x35E0ULL);
    goto loc_0030BC40;
loc_0030BC64:
    if ((unsigned int)(result) == 0) goto loc_0030BAA3;
    if (((unsigned int)((unsigned __int8)(v_rbx))) >= ((unsigned int)(*(unsigned __int8 *)(a2 + 208)))) goto loc_0030BAA3;
    goto loc_0030BB8F;
loc_0030BC7C:
    a3 = 0;
    result = KiAdjustReadyQueueScanOwnerOnParkingChange(a2, 1, a3, v_stack_p40);
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a2 + 35)) & (207));
    if ((((unsigned __int8)(a3 + 1)) & ((unsigned __int8)(a2))) != 0) goto loc_0030BCD8;
    *(unsigned __int8 *)(a2 + 35) = (unsigned __int8)(a2);
    *(unsigned __int8 *)(a2 + 14523) = (unsigned __int8)((unsigned int)((unsigned int)(a3 + 1)));
    v_stack_pA0 = 0;
    if (a2 == v_rbx) goto loc_0030B8FF;
    v_stack_pA0 = (unsigned __int8)((unsigned int)((unsigned int)(a3 + 1)));
    goto loc_0030B8FF;
loc_0030BCD8:
    v_rdi = 0;
    *(unsigned __int8 *)(a2 + 35) = (unsigned __int8)(a2);
    v_stack_pA0 = 0;
    goto loc_0030B8FF;
loc_0030BCEE:
    if (v_stack_pA8 == 0) goto loc_0030BAFF;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_pB0 + 120, a2, a3, v_stack_p40);
    a2 = 0;
    result = EtwTraceParkTransition(0, a2, a2 + 2, v_stack_p40);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pB0 + 120, a2, a2 + 2, v_stack_p40);
    goto loc_0030BAFF;
}
```

## 5. (Beta) C Style

```c
int64_t KiSoftParkElectionUnparkProcessor(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint8_t v_stack_m78;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;
    uint8_t v_stack_p8;
    uint8_t v_stack_pA0;
    uint8_t v_stack_pA8;
    uint64_t v_stack_pB0;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (88);
    local_r12 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    result = (Arg2) | (1);
    v_stack_m60 = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))) == 0) goto loc_0030B8B1;
loc_0030B884:
    local_r14 = 0;
loc_0030B88A:
    if (condition_is_below) goto loc_0030B8C9;
    local_r15 = (*(uint64_t *)(arg2 + 0x8E58) + 8) + (8);
    local_r12 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0030B884;
loc_0030B8B1:
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x23)) & (20));
    if (((uint8_t)(result)) == 20) goto loc_0030BC7C;
    goto loc_0030B9D2;
loc_0030B8C9:
    local_r14 = (uint32_t)((1) + ((uint32_t)(v_stack_p20)));
    if (((*(uint32_t *)(v_rip + 0xCB99D9)) & ((uint32_t)(local_r14))) == 0) goto loc_0030B8E2;
loc_0030B8D5:
loc_0030B8D7:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8E58) + 0x8) + 0x30) == 0) goto loc_0030B88A;
    goto loc_0030B8C9;
loc_0030B8E2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBB1D0)))) & (64)) == 0) goto loc_0030B8D5;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030B8D5;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, Arg3, Arg4);
    goto loc_0030B8D7;
loc_0030B8FF:
    Arg4 = 0;
    v_stack_m78 = (uint8_t)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8E58) + 0x8));
    result = KiUpdateThreadPriority(Arg2, Arg2, *(uint64_t *)(arg2 + 0x18), Arg4);
    v_stack_p10 = (uint8_t)(local_r14);
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8E58) + 0x8)) == 0) goto loc_0030B9D2;
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_m60, Arg3, Arg4);
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_p20, Arg3, Arg4);
    local_r12 = 0;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCBB1AF))) >> (9));
    local_r14 = 0;
    local_rdi = (uint32_t)((local_rdi) & (2));
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030B9AA;
loc_0030B977:
    Arg1 = (0) + (2);
    Arg1 = (Arg1 + local_r14 * 4 * 8) + (*(uint64_t *)(arg1 + 0x37E8));
    result = KiCommitRescheduleContextEntry(Arg1, Arg1, (uint32_t)((uint32_t)(local_rdi)), v_stack_p20);
    local_r12 = (uint8_t)((local_r12) | ((uint8_t)(result)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r15)));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030B977;
loc_0030B9AA:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_0030B9D2;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + (1));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    Arg4 = 0;
    Arg2 = 0;
    Arg3 = (v_stack_m60) & (-2);
    v_stack_m58 = Arg3;
    result = (uint32_t)((v_stack_m60) & (1));
    if (condition_is_equal) goto loc_0030BC09;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg3 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
        Arg4 = result + 8;
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030BA1B;
loc_0030BA08:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030BA08;
loc_0030BA1B:
    if ((uint8_t)(local_r12) == 0) goto loc_0030BAC7;
    local_r12 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030BAC7;
loc_0030BA3E:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33))) & (16)) != 0) goto loc_0030BA5B;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33))) & (8)) == 0) goto loc_0030BA79;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_0030BA79;
loc_0030BA5B:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_0030BB11;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24)));
loc_0030BA79:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (2)) != 0) goto loc_0030BBF4;
loc_0030BA85:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (4)) == 0) goto loc_0030BAA3;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_0030BB65;
loc_0030BAA3:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x28);
    }
    local_r12 = (uint32_t)((local_r12) + (1));
    if (((uint32_t)(local_r12)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030BA3E;
loc_0030BAC7:
    if (v_stack_p8 == 0) goto loc_0030BAEF;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_0030BC16;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24)));
loc_0030BAEF:
    if (((*(uint32_t *)(v_rip + 0xCBB01B)) & (0x2000ULL)) != 0) goto loc_0030BCEE;
loc_0030BAFF:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)(*(uint32_t *)(arg2 + 0x24));
loc_0030BB11:
    if (((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24)))) != 1) goto loc_0030BB5C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24))) goto loc_0030BA79;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), Arg3, Arg4);
loc_0030BB3B:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0xC8), Arg4);
    goto loc_0030BA79;
loc_0030BB5C:
    goto loc_0030BB3B;
loc_0030BB65:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_0030BAA3;
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10))) goto loc_0030BAA3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35E0))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030BC64;
loc_0030BB8F:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0xC) = 2;
    local_r14 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xCB9471)) == 0) {
        result = *(uint8_t *)(v_rip + 0xCC1822 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24)) * 2 + 0x1);
        local_r14 = *(uint8_t *)(v_rip + 0xCC1822 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24)) * 2);
        local_r14 = (uint32_t)((local_r14) << (6));
        local_r14 = (uint32_t)((local_r14) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0x8) = (uint32_t)(local_r14);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCBAF4D));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBAF4D)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0xC8), Arg4);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> (32);
    goto loc_0030BAA3;
loc_0030BBF4:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x28), *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10), Arg3, Arg4);
    goto loc_0030BA85;
loc_0030BC09:
    goto loc_0030BA08;
loc_0030BC16:
    if (((uint8_t)(result)) != 1) goto loc_0030BC5B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(arg2 + 0x24))) goto loc_0030BAEF;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    local_rbx = (Arg1) + (0x35E0ULL);
    result = KeAddProcessorAffinityEx(local_rbx, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), Arg3, v_stack_p40);
loc_0030BC40:
    result = KeAddGroupAffinityEx(local_rbx, *(uint8_t *)(arg2 + 0xD0), *(uint64_t *)(arg2 + 0xC8), v_stack_p40);
    goto loc_0030BAEF;
loc_0030BC5B:
    local_rbx = (local_rbx) + (0x35E0ULL);
    goto loc_0030BC40;
loc_0030BC64:
    if ((uint32_t)(result) == 0) goto loc_0030BAA3;
    if (((uint32_t)((uint8_t)(local_rbx))) >= ((uint32_t)(*(uint8_t *)(arg2 + 0xD0)))) goto loc_0030BAA3;
    goto loc_0030BB8F;
loc_0030BC7C:
    Arg3 = 0;
    result = KiAdjustReadyQueueScanOwnerOnParkingChange(Arg2, 1, Arg3, v_stack_p40);
    Arg2 = (uint8_t)((*(uint8_t *)(arg2 + 0x23)) & (207));
    if ((((uint8_t)(Arg3 + 1)) & ((uint8_t)(Arg2))) != 0) goto loc_0030BCD8;
    *(uint8_t *)(arg2 + 0x23) = (uint8_t)(Arg2);
    *(uint8_t *)(arg2 + 0x38BB) = (uint8_t)((uint32_t)((uint32_t)(Arg3 + 1)));
    v_stack_pA0 = 0;
    if (Arg2 == local_rbx) goto loc_0030B8FF;
    v_stack_pA0 = (uint8_t)((uint32_t)((uint32_t)(Arg3 + 1)));
    goto loc_0030B8FF;
loc_0030BCD8:
    local_rdi = 0;
    *(uint8_t *)(arg2 + 0x23) = (uint8_t)(Arg2);
    v_stack_pA0 = 0;
    goto loc_0030B8FF;
loc_0030BCEE:
    if (v_stack_pA8 == 0) goto loc_0030BAFF;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_pB0 + 120, Arg2, Arg3, v_stack_p40);
    Arg2 = 0;
    result = EtwTraceParkTransition(0, Arg2, Arg2 + 2, v_stack_p40);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pB0 + 120, Arg2, Arg2 + 2, v_stack_p40);
    goto loc_0030BAFF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg2` | `+ 0x23` | `8` | `R` |
| `Arg2` | `+ 0x23` | `8` | `W` |
| `Arg2` | `+ 0xC8` | `64` | `R` |
| `Arg2` | `+ 0x38BB` | `8` | `W` |
| `Arg2` | `+ 0x8E58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030B818&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
