# KiSetSystemAffinityThread

- RVA: `0x003993E0`–`0x00399B14` (길이 `1,844` bytes)
- VA: `0x00000001403993E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000817C8`
- 디코드: `449`개 명령, `1,844/1,844` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00399438` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003994FD` → [KiUpdateNodeAffinitizedFlag](KiUpdateNodeAffinitizedFlag_function_00399B1C.md) (function, `0x00399B1C`)
- `0x0039958E` → [KiReleasePrcbLocksForIsolationUnit](KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00399602` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039960E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00399707` → [KiComputeThreadAffinity](KiComputeThreadAffinity_function_00399DE0.md) (function, `0x00399DE0`)
- `0x00399748` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00399757` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x00399762` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x003997A6` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x003997B8` → [KiCommitRescheduleContext](../30/KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x003998DF` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x00399912` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00399928` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x003999BB` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x003999E1` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x00399A07` → [EtwTraceIdealProcessor](../3C/EtwTraceIdealProcessor_function_003C0808.md) (function, `0x003C0808`)
- `0x00399A52` → [EtwTraceThreadAffinity](../3C/EtwTraceThreadAffinity_function_003C29A0.md) (function, `0x003C29A0`)

### Direct callers
- [sub_002092A9](../20/Unknown_function_002092A9.md) at `0x00209331`
- [KeRevertToUserGroupAffinityThread](KeRevertToUserGroupAffinityThread_function_00398EC0.md) at `0x00398FA7`
- [sub_0039915F](Unknown_function_0039915F.md) at `0x0039923E`
- [KeSetSystemMultipleGroupAffinityThread](../4D/KeSetSystemMultipleGroupAffinityThread_function_004D0C88.md) at `0x004D0EA7`
- [KeRevertToUserMultipleGroupAffinityThread](../4D/KeRevertToUserMultipleGroupAffinityThread_function_004D8A90.md) at `0x004D8C51`

### Static image references
- `0x00399469` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003995A2` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003995B2` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x003995DE` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003995F8` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00399688` → RVA `0x00F231B8` (`.data`; read)
- `0x00399975` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x003999A9` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003993E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003993E5  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003993EA  55                              push rbp
003993EB  56                              push rsi
003993EC  57                              push rdi
003993ED  41 54                           push r12
003993EF  41 55                           push r13
003993F1  41 56                           push r14
003993F3  41 57                           push r15
003993F5  48 8B EC                        mov rbp, rsp
003993F8  48 83 EC 50                     sub rsp, 0x50
003993FC  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
00399400  45 33 E4                        xor r12d, r12d
00399403  45 8B F9                        mov r15d, r9d
00399406  4D 8B F0                        mov r14, r8
00399409  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
0039940D  48 8B F1                        mov rsi, rcx
00399410  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
00399414  48 8B 9F 40 02 00 00            mov rbx, qword ptr [rdi + 0x240]
0039941B  45 8D 54 24 01                  lea r10d, [r12 + 1]
00399420  45 8A EA                        mov r13b, r10b
00399423  48 85 D2                        test rdx, rdx
00399426  0F 85 82 02 00 00               jne 0x1403996ae
0039942C  44 0F B7 03                     movzx r8d, word ptr [rbx]
00399430  48 8D 4B 08                     lea rcx, [rbx + 8]
00399434  49 C1 E0 03                     shl r8, 3
00399438  E8 03 D8 32 00                  call 0x1406c6c40
0039943D  45 8D 54 24 01                  lea r10d, [r12 + 1]
00399442  66 44 89 13                     mov word ptr [rbx], r10w
00399446  48 8B 8F 40 02 00 00            mov rcx, qword ptr [rdi + 0x240]
0039944D  41 0F B7 56 08                  movzx edx, word ptr [r14 + 8]
00399452  4D 8B 06                        mov r8, qword ptr [r14]
00399455  66 39 11                        cmp word ptr [rcx], dx
00399458  0F 86 B3 05 00 00               jbe 0x140399a11
0039945E  4C 09 44 D1 08                  or qword ptr [rcx + rdx*8 + 8], r8
00399463  8B 87 4C 02 00 00               mov eax, dword ptr [rdi + 0x24c]
00399469  4C 8D 1D 90 6B C6 FF            lea r11, [rip - 0x399470]
00399470  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00399473  41 81 FF 00 08 00 00            cmp r15d, 0x800
0039947A  0F 83 95 01 00 00               jae 0x140399615
00399480  0F AE E8                        lfence
00399483  44 89 BF 4C 02 00 00            mov dword ptr [rdi + 0x24c], r15d
0039948A  4B 8B 9C FB 40 8C FC 00         mov rbx, qword ptr [r11 + r15*8 + 0xfc8c40]
00399492  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
00399499  66 89 87 48 02 00 00            mov word ptr [rdi + 0x248], ax
003994A0  8B 47 74                        mov eax, dword ptr [rdi + 0x74]
003994A3  A8 08                           test al, 8
003994A5  0F 84 59 02 00 00               je 0x140399704
003994AB  4C 8B 83 40 8E 00 00            mov r8, qword ptr [rbx + 0x8e40]
003994B2  41 8B D4                        mov edx, r12d
003994B5  4D 85 C0                        test r8, r8
003994B8  74 25                           je 0x1403994df
003994BA  48 8B 8F 40 02 00 00            mov rcx, qword ptr [rdi + 0x240]
003994C1  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
003994C8  66 3B 01                        cmp ax, word ptr [rcx]
003994CB  0F 83 8B 05 00 00               jae 0x140399a5c
003994D1  48 8B 4C C1 08                  mov rcx, qword ptr [rcx + rax*8 + 8]
003994D6  49 23 C8                        and rcx, r8
003994D9  49 3B C8                        cmp rcx, r8
003994DC  0F 94 C2                        sete dl
003994DF  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
003994E2  41 BE 01 00 00 00               mov r14d, 1
003994E8  C1 E8 0D                        shr eax, 0xd
003994EB  41 23 C6                        and eax, r14d
003994EE  3B D0                           cmp edx, eax
003994F0  74 08                           je 0x1403994fa
003994F2  F0 81 77 78 00 20 00 00         lock xor dword ptr [rdi + 0x78], 0x2000
003994FA  48 8B CF                        mov rcx, rdi
003994FD  E8 1A 06 00 00                  call 0x140399b1c
00399502  48 8B 97 40 02 00 00            mov rdx, qword ptr [rdi + 0x240]
00399509  0F B6 86 D0 00 00 00            movzx eax, byte ptr [rsi + 0xd0]
00399510  66 3B 02                        cmp ax, word ptr [rdx]
00399513  73 13                           jae 0x140399528
00399515  8A 8E D1 00 00 00               mov cl, byte ptr [rsi + 0xd1]
0039951B  48 8B 54 C2 08                  mov rdx, qword ptr [rdx + rax*8 + 8]
00399520  48 D3 EA                        shr rdx, cl
00399523  41 84 D6                        test r14b, dl
00399526  75 70                           jne 0x140399598
00399528  F0 0F BA 6F 78 0C               lock bts dword ptr [rdi + 0x78], 0xc
0039952E  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00399532  48 85 C0                        test rax, rax
00399535  75 61                           jne 0x140399598
00399537  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
0039953E  48 8B DE                        mov rbx, rsi
00399541  49 0B DE                        or rbx, r14
00399544  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00399548  0F B6 08                        movzx ecx, byte ptr [rax]
0039954B  4C 8D 78 08                     lea r15, [rax + 8]
0039954F  84 C9                           test cl, cl
00399551  74 28                           je 0x14039957b
00399553  44 8B E1                        mov r12d, ecx
00399556  BF 01 00 00 00                  mov edi, 1
0039955B  49 8B 1F                        mov rbx, qword ptr [r15]
0039955E  45 33 F6                        xor r14d, r14d
00399561  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
00399568  72 71                           jb 0x1403995db
0039956A  49 83 C7 08                     add r15, 8
0039956E  4C 2B E7                        sub r12, rdi
00399571  75 E8                           jne 0x14039955b
00399573  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00399577  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
0039957B  4C 39 66 10                     cmp qword ptr [rsi + 0x10], r12
0039957F  0F 84 B1 01 00 00               je 0x140399736
00399585  48 85 DB                        test rbx, rbx
00399588  74 09                           je 0x140399593
0039958A  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0039958E  E8 BD 06 00 00                  call 0x140399c50
00399593  45 84 ED                        test r13b, r13b
00399596  74 04                           je 0x14039959c
00399598  4C 89 67 40                     mov qword ptr [rdi + 0x40], r12
0039959C  41 BA 01 00 00 00               mov r10d, 1
003995A2  F7 05 58 D5 C2 00 00 10 00 00   test dword ptr [rip + 0xc2d558], 0x1000
003995AC  0F 85 75 04 00 00               jne 0x140399a27
003995B2  F7 05 54 D5 C2 00 00 00 00 08   test dword ptr [rip + 0xc2d554], 0x8000000
003995BC  0F 85 35 04 00 00               jne 0x1403999f7
003995C2  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
003995CA  48 83 C4 50                     add rsp, 0x50
003995CE  41 5F                           pop r15
003995D0  41 5E                           pop r14
003995D2  41 5D                           pop r13
003995D4  41 5C                           pop r12
003995D6  5F                              pop rdi
003995D7  5E                              pop rsi
003995D8  5D                              pop rbp
003995D9  C3                              ret
003995DA  CC                              int3
003995DB  44 03 F7                        add r14d, edi
003995DE  44 85 35 C7 BC C2 00            test dword ptr [rip + 0xc2bcc7], r14d
003995E5  74 11                           je 0x1403995f8
003995E7  F3 90                           pause
003995E9  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
003995ED  48 85 C0                        test rax, rax
003995F0  0F 84 6B FF FF FF               je 0x140399561
003995F6  EB E3                           jmp 0x1403995db
003995F8  8B 05 BA D4 C2 00               mov eax, dword ptr [rip + 0xc2d4ba]
003995FE  A8 40                           test al, 0x40
00399600  74 E5                           je 0x1403995e7
00399602  E8 89 5E F7 FF                  call 0x14030f490
00399607  84 C0                           test al, al
00399609  74 DC                           je 0x1403995e7
0039960B  41 8B CE                        mov ecx, r14d
0039960E  E8 4D 5E F7 FF                  call 0x14030f460
00399613  EB D4                           jmp 0x1403995e9
00399615  49 8B 9C C3 40 8C FC 00         mov rbx, qword ptr [r11 + rax*8 + 0xfc8c40]
0039961D  4C 8B 8F 40 02 00 00            mov r9, qword ptr [rdi + 0x240]
00399624  89 45 58                        mov dword ptr [rbp + 0x58], eax
00399627  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
0039962E  45 0F B7 01                     movzx r8d, word ptr [r9]
00399632  66 41 3B C0                     cmp ax, r8w
00399636  73 17                           jae 0x14039964f
00399638  8A 8B D1 00 00 00               mov cl, byte ptr [rbx + 0xd1]
0039963E  49 8B 54 C1 08                  mov rdx, qword ptr [r9 + rax*8 + 8]
00399643  48 D3 EA                        shr rdx, cl
00399646  41 84 D2                        test r10b, dl
00399649  0F 85 43 FE FF FF               jne 0x140399492
0039964F  4C 8B 93 C0 00 00 00            mov r10, qword ptr [rbx + 0xc0]
00399656  41 0F B7 92 88 00 00 00         movzx edx, word ptr [r10 + 0x88]
0039965E  66 41 3B D0                     cmp dx, r8w
00399662  0F 83 1D 04 00 00               jae 0x140399a85
00399668  49 8B 4C D1 08                  mov rcx, qword ptr [r9 + rdx*8 + 8]
0039966D  49 23 8A 80 00 00 00            and rcx, qword ptr [r10 + 0x80]
00399674  0F 84 EA 03 00 00               je 0x140399a64
0039967A  8B C2                           mov eax, edx
0039967C  48 0F BD C9                     bsr rcx, rcx
00399680  C1 E0 06                        shl eax, 6
00399683  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
00399686  03 C8                           add ecx, eax
00399688  48 8B 05 29 9B B8 00            mov rax, qword ptr [rip + 0xb89b29]
0039968F  44 8B 3C 88                     mov r15d, dword ptr [rax + rcx*4]
00399693  41 8B C7                        mov eax, r15d
00399696  44 89 BF 4C 02 00 00            mov dword ptr [rdi + 0x24c], r15d
0039969D  44 89 7D 58                     mov dword ptr [rbp + 0x58], r15d
003996A1  49 8B 9C C3 40 8C FC 00         mov rbx, qword ptr [r11 + rax*8 + 0xfc8c40]
003996A9  E9 E4 FD FF FF                  jmp 0x140399492
003996AE  0F B7 02                        movzx eax, word ptr [rdx]
003996B1  0F B7 4B 02                     movzx ecx, word ptr [rbx + 2]
003996B5  66 3B C1                        cmp ax, cx
003996B8  66 89 4B 02                     mov word ptr [rbx + 2], cx
003996BC  44 0F B7 C1                     movzx r8d, cx
003996C0  44 89 63 04                     mov dword ptr [rbx + 4], r12d
003996C4  66 44 0F 46 C0                  cmovbe r8w, ax
003996C9  41 0F B7 CC                     movzx ecx, r12w
003996CD  66 44 89 03                     mov word ptr [rbx], r8w
003996D1  66 45 3B E0                     cmp r12w, r8w
003996D5  73 54                           jae 0x14039972b
003996D7  4C 8D 4B 08                     lea r9, [rbx + 8]
003996DB  45 0F B7 D0                     movzx r10d, r8w
003996DF  48 2B D3                        sub rdx, rbx
003996E2  41 0F B7 C8                     movzx ecx, r8w
003996E6  41 BE 01 00 00 00               mov r14d, 1
003996EC  4A 8B 04 0A                     mov rax, qword ptr [rdx + r9]
003996F0  49 89 01                        mov qword ptr [r9], rax
003996F3  4D 8D 49 08                     lea r9, [r9 + 8]
003996F7  4D 2B D6                        sub r10, r14
003996FA  75 F0                           jne 0x1403996ec
003996FC  41 BA 01 00 00 00               mov r10d, 1
00399702  EB 27                           jmp 0x14039972b
00399704  48 8B CF                        mov rcx, rdi
00399707  E8 D4 06 00 00                  call 0x140399de0
0039970C  85 C0                           test eax, eax
0039970E  0F 84 97 FD FF FF               je 0x1403994ab
00399714  41 BE 01 00 00 00               mov r14d, 1
0039971A  E9 E3 FD FF FF                  jmp 0x140399502
0039971F  0F B7 C1                        movzx eax, cx
00399722  66 41 03 CA                     add cx, r10w
00399726  4C 89 64 C3 08                  mov qword ptr [rbx + rax*8 + 8], r12
0039972B  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
0039972F  72 EE                           jb 0x14039971f
00399731  E9 2D FD FF FF                  jmp 0x140399463
00399736  4C 8B B6 E8 37 00 00            mov r14, qword ptr [rsi + 0x37e8]
0039973D  33 D2                           xor edx, edx
0039973F  49 8B CE                        mov rcx, r14
00399742  41 B8 F0 00 00 00               mov r8d, 0xf0
00399748  E8 F3 D4 32 00                  call 0x1406c6c40
0039974D  4C 8B C7                        mov r8, rdi
00399750  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00399754  49 8B CE                        mov rcx, r14
00399757  E8 54 2F F7 FF                  call 0x14030c6b0
0039975C  48 8B D6                        mov rdx, rsi
0039975F  49 8B CE                        mov rcx, r14
00399762  E8 F9 98 FB FF                  call 0x140353060
00399767  4C 8B C8                        mov r9, rax
0039976A  8A 50 20                        mov dl, byte ptr [rax + 0x20]
0039976D  41 80 49 22 02                  or byte ptr [r9 + 0x22], 2
00399772  48 8B 00                        mov rax, qword ptr [rax]
00399775  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00399779  49 89 49 10                     mov qword ptr [r9 + 0x10], rcx
0039977D  8A CA                           mov cl, dl
0039977F  80 E1 C5                        and cl, 0xc5
00399782  80 C9 05                        or cl, 5
00399785  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
00399789  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0039978D  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
00399792  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00399796  F6 C2 02                        test dl, 2
00399799  0F 85 F7 02 00 00               jne 0x140399a96
0039979F  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
003997A3  49 8B CE                        mov rcx, r14
003997A6  E8 75 EE EB FF                  call 0x140258620
003997AB  4C 8B 4D 60                     mov r9, qword ptr [rbp + 0x60]
003997AF  45 33 C0                        xor r8d, r8d
003997B2  48 8B D6                        mov rdx, rsi
003997B5  49 8B CE                        mov rcx, r14
003997B8  E8 63 37 F7 FF                  call 0x14030cf20
003997BD  44 8A C8                        mov r9b, al
003997C0  41 BA 01 00 00 00               mov r10d, 1
003997C6  48 8B C3                        mov rax, rbx
003997C9  4D 8B C4                        mov r8, r12
003997CC  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003997D0  41 8B D4                        mov edx, r12d
003997D3  48 89 45 F8                     mov qword ptr [rbp - 8], rax
003997D7  41 23 DA                        and ebx, r10d
003997DA  0F 84 0B 02 00 00               je 0x1403999eb
003997E0  41 3B DA                        cmp ebx, r10d
003997E3  75 15                           jne 0x1403997fa
003997E5  4C 8B 80 58 8E 00 00            mov r8, qword ptr [rax + 0x8e58]
003997EC  48 8B 80 58 8E 00 00            mov rax, qword ptr [rax + 0x8e58]
003997F3  49 83 C0 08                     add r8, 8
003997F7  0F B6 10                        movzx edx, byte ptr [rax]
003997FA  85 D2                           test edx, edx
003997FC  74 12                           je 0x140399810
003997FE  8D 42 FF                        lea eax, [rdx - 1]
00399801  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00399805  8B D0                           mov edx, eax
00399807  F0 4C 21 61 30                  lock and qword ptr [rcx + 0x30], r12
0039980C  85 C0                           test eax, eax
0039980E  75 EE                           jne 0x1403997fe
00399810  44 88 65 40                     mov byte ptr [rbp + 0x40], r12b
00399814  49 8B DC                        mov rbx, r12
00399817  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
0039981B  4C 89 67 40                     mov qword ptr [rdi + 0x40], r12
0039981F  45 84 C9                        test r9b, r9b
00399822  0F 84 7A FD FF FF               je 0x1403995a2
00399828  45 8B EC                        mov r13d, r12d
0039982B  45 38 26                        cmp byte ptr [r14], r12b
0039982E  0F 86 A4 00 00 00               jbe 0x1403998d8
00399834  48 8D 3D C5 67 C6 FF            lea rdi, [rip - 0x39983b]
0039983B  41 8B C5                        mov eax, r13d
0039983E  4C 8D 24 80                     lea r12, [rax + rax*4]
00399842  43 8A 44 E6 33                  mov al, byte ptr [r14 + r12*8 + 0x33]
00399847  4B 8B 5C E6 10                  mov rbx, qword ptr [r14 + r12*8 + 0x10]
0039984C  A8 10                           test al, 0x10
0039984E  75 0B                           jne 0x14039985b
00399850  A8 08                           test al, 8
00399852  74 25                           je 0x140399879
00399854  90                              nop
00399855  80 7B 07 00                     cmp byte ptr [rbx + 7], 0
00399859  74 1E                           je 0x140399879
0039985B  8A 86 D9 35 00 00               mov al, byte ptr [rsi + 0x35d9]
00399861  84 C0                           test al, al
00399863  0F 85 84 00 00 00               jne 0x1403998ed
00399869  44 88 96 D9 35 00 00            mov byte ptr [rsi + 0x35d9], r10b
00399870  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00399873  89 86 DC 35 00 00               mov dword ptr [rsi + 0x35dc], eax
00399879  43 F6 44 E6 33 02               test byte ptr [r14 + r12*8 + 0x33], 2
0039987F  0F 85 51 01 00 00               jne 0x1403999d6
00399885  43 F6 44 E6 33 04               test byte ptr [r14 + r12*8 + 0x33], 4
0039988B  74 16                           je 0x1403998a3
0039988D  48 8B 83 B8 8E 00 00            mov rax, qword ptr [rbx + 0x8eb8]
00399894  47 0F BE 4C E6 34               movsx r9d, byte ptr [r14 + r12*8 + 0x34]
0039989A  48 85 C0                        test rax, rax
0039989D  0F 85 98 00 00 00               jne 0x14039993b
003998A3  41 BA 01 00 00 00               mov r10d, 1
003998A9  47 84 54 E6 33                  test byte ptr [r14 + r12*8 + 0x33], r10b
003998AE  74 0D                           je 0x1403998bd
003998B0  4B 8B 44 E6 28                  mov rax, qword ptr [r14 + r12*8 + 0x28]
003998B5  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
003998BD  41 0F B6 06                     movzx eax, byte ptr [r14]
003998C1  45 03 EA                        add r13d, r10d
003998C4  44 3B E8                        cmp r13d, eax
003998C7  0F 82 6E FF FF FF               jb 0x14039983b
003998CD  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
003998D1  45 33 E4                        xor r12d, r12d
003998D4  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
003998D8  48 8D 8E D8 35 00 00            lea rcx, [rsi + 0x35d8]
003998DF  E8 1C 89 EB FF                  call 0x140252200
003998E4  44 8A 6D 40                     mov r13b, byte ptr [rbp + 0x40]
003998E8  E9 98 FC FF FF                  jmp 0x140399585
003998ED  41 3A C2                        cmp al, r10b
003998F0  75 40                           jne 0x140399932
003998F2  8B 96 DC 35 00 00               mov edx, dword ptr [rsi + 0x35dc]
003998F8  3B 53 24                        cmp edx, dword ptr [rbx + 0x24]
003998FB  0F 84 78 FF FF FF               je 0x140399879
00399901  4C 8D BE E0 35 00 00            lea r15, [rsi + 0x35e0]
00399908  C6 86 D9 35 00 00 02            mov byte ptr [rsi + 0x35d9], 2
0039990F  49 8B CF                        mov rcx, r15
00399912  E8 D9 1D EC FF                  call 0x14025b6f0
00399917  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
0039991E  49 8B CF                        mov rcx, r15
00399921  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
00399928  E8 93 1D EC FF                  call 0x14025b6c0
0039992D  E9 47 FF FF FF                  jmp 0x140399879
00399932  4C 8D BE E0 35 00 00            lea r15, [rsi + 0x35e0]
00399939  EB DC                           jmp 0x140399917
0039993B  48 8D 8E B8 8E 00 00            lea rcx, [rsi + 0x8eb8]
00399942  48 83 39 00                     cmp qword ptr [rcx], 0
00399946  0F 84 57 FF FF FF               je 0x1403998a3
0039994C  48 3B F3                        cmp rsi, rbx
0039994F  0F 84 4E FF FF FF               je 0x1403998a3
00399955  8B 00                           mov eax, dword ptr [rax]
00399957  4C 8B C1                        mov r8, rcx
0039995A  8B D0                           mov edx, eax
0039995C  81 E2 00 00 04 00               and edx, 0x40000
00399962  74 07                           je 0x14039996b
00399964  4C 8D 86 B8 8E 00 00            lea r8, [rsi + 0x8eb8]
0039996B  0F BA E0 14                     bt eax, 0x14
0039996F  0F 83 83 01 00 00               jae 0x140399af8
00399975  80 3D 8B B6 C2 00 00            cmp byte ptr [rip + 0xc2b68b], 0
0039997C  48 8B 11                        mov rdx, qword ptr [rcx]
0039997F  C7 42 0C 02 00 00 00            mov dword ptr [rdx + 0xc], 2
00399986  44 8B 7B 24                     mov r15d, dword ptr [rbx + 0x24]
0039998A  75 19                           jne 0x1403999a5
0039998C  42 0F B6 84 7F 61 D2 FC 00      movzx eax, byte ptr [rdi + r15*2 + 0xfcd261]
00399995  46 0F B6 BC 7F 60 D2 FC 00      movzx r15d, byte ptr [rdi + r15*2 + 0xfcd260]
0039999E  41 C1 E7 06                     shl r15d, 6
003999A2  44 0B F8                        or r15d, eax
003999A5  44 89 7A 08                     mov dword ptr [rdx + 8], r15d
003999A9  8B 05 65 D1 C2 00               mov eax, dword ptr [rip + 0xc2d165]
003999AF  A8 20                           test al, 0x20
003999B1  74 0D                           je 0x1403999c0
003999B3  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
003999B6  BA 02 00 00 00                  mov edx, 2
003999BB  E8 00 19 16 00                  call 0x1404fb2c0
003999C0  41 8B D7                        mov edx, r15d
003999C3  B9 C2 00 00 40                  mov ecx, 0x400000c2
003999C8  48 C1 EA 20                     shr rdx, 0x20
003999CC  41 8B C7                        mov eax, r15d
003999CF  0F 30                           wrmsr
003999D1  E9 CD FE FF FF                  jmp 0x1403998a3
003999D6  4B 8B 4C E6 28                  mov rcx, qword ptr [r14 + r12*8 + 0x28]
003999DB  45 33 C0                        xor r8d, r8d
003999DE  48 8B D3                        mov rdx, rbx
003999E1  E8 66 1D F7 FF                  call 0x14030b74c
003999E6  E9 9A FE FF FF                  jmp 0x140399885
003999EB  4C 8D 45 F8                     lea r8, [rbp - 8]
003999EF  41 8B D2                        mov edx, r10d
003999F2  E9 07 FE FF FF                  jmp 0x1403997fe
003999F7  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
003999FB  BA 46 05 00 00                  mov edx, 0x546
00399A00  44 8B 45 E0                     mov r8d, dword ptr [rbp - 0x20]
00399A04  48 8B CF                        mov rcx, rdi
00399A07  E8 FC 6D 02 00                  call 0x1403c0808
00399A0C  E9 B1 FB FF FF                  jmp 0x1403995c2
00399A11  66 39 51 02                     cmp word ptr [rcx + 2], dx
00399A15  0F 86 48 FA FF FF               jbe 0x140399463
00399A1B  41 8D 04 12                     lea eax, [r10 + rdx]
00399A1F  66 89 01                        mov word ptr [rcx], ax
00399A22  E9 37 FA FF FF                  jmp 0x14039945e
00399A27  44 8B 47 74                     mov r8d, dword ptr [rdi + 0x74]
00399A2B  45 33 C9                        xor r9d, r9d
00399A2E  48 8B 87 40 02 00 00            mov rax, qword ptr [rdi + 0x240]
00399A35  48 8B CF                        mov rcx, rdi
00399A38  0F B7 97 48 02 00 00            movzx edx, word ptr [rdi + 0x248]
00399A3F  41 C1 E8 03                     shr r8d, 3
00399A43  45 22 C2                        and r8b, r10b
00399A46  66 C7 44 24 28 36 05            mov word ptr [rsp + 0x28], 0x536
00399A4D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00399A52  E8 49 8F 02 00                  call 0x1403c29a0
00399A57  E9 56 FB FF FF                  jmp 0x1403995b2
00399A5C  49 8B CC                        mov rcx, r12
00399A5F  E9 72 FA FF FF                  jmp 0x1403994d6
00399A64  66 41 FF C8                     dec r8w
00399A68  66 45 85 C0                     test r8w, r8w
00399A6C  78 1F                           js 0x140399a8d
00399A6E  49 0F BF C0                     movsx rax, r8w
00399A72  49 8B 4C C1 08                  mov rcx, qword ptr [r9 + rax*8 + 8]
00399A77  48 85 C9                        test rcx, rcx
00399A7A  74 E8                           je 0x140399a64
00399A7C  41 0F BF C0                     movsx eax, r8w
00399A80  E9 F7 FB FF FF                  jmp 0x14039967c
00399A85  49 8B CC                        mov rcx, r12
00399A88  E9 E0 FB FF FF                  jmp 0x14039966d
00399A8D  41 83 CF FF                     or r15d, 0xffffffff
00399A91  E9 FD FB FF FF                  jmp 0x140399693
00399A96  45 8B C4                        mov r8d, r12d
00399A99  45 38 26                        cmp byte ptr [r14], r12b
00399A9C  76 51                           jbe 0x140399aef
00399A9E  BF 01 00 00 00                  mov edi, 1
00399AA3  41 8B C0                        mov eax, r8d
00399AA6  48 8D 14 85 02 00 00 00         lea rdx, [rax*4 + 2]
00399AAE  48 03 D0                        add rdx, rax
00399AB1  49 8D 14 D6                     lea rdx, [r14 + rdx*8]
00399AB5  49 3B D1                        cmp rdx, r9
00399AB8  74 25                           je 0x140399adf
00399ABA  80 4A 22 02                     or byte ptr [rdx + 0x22], 2
00399ABE  48 8B 0A                        mov rcx, qword ptr [rdx]
00399AC1  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00399AC5  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
00399AC9  8A 42 20                        mov al, byte ptr [rdx + 0x20]
00399ACC  24 C5                           and al, 0xc5
00399ACE  0C 05                           or al, 5
00399AD0  88 42 20                        mov byte ptr [rdx + 0x20], al
00399AD3  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00399AD7  80 62 21 FE                     and byte ptr [rdx + 0x21], 0xfe
00399ADB  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
00399ADF  41 0F B6 06                     movzx eax, byte ptr [r14]
00399AE3  44 03 C7                        add r8d, edi
00399AE6  44 3B C0                        cmp r8d, eax
00399AE9  72 B8                           jb 0x140399aa3
00399AEB  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00399AEF  45 89 66 04                     mov dword ptr [r14 + 4], r12d
00399AF3  E9 A7 FC FF FF                  jmp 0x14039979f
00399AF8  85 D2                           test edx, edx
00399AFA  0F 84 A3 FD FF FF               je 0x1403998a3
00399B00  0F B6 C0                        movzx eax, al
00399B03  49 8B C8                        mov rcx, r8
00399B06  41 3B C1                        cmp eax, r9d
00399B09  0F 8D 94 FD FF FF               jge 0x1403998a3
00399B0F  E9 61 FE FF FF                  jmp 0x140399975
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetSystemAffinityThread(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p28;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (80);
    v_r12 = 0;
    v_stack_m50 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a1 + 8);
    if (a2 != 0) goto loc_003996AE;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576))) << (3);
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576) + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576)) = (unsigned __int16)(v_r12 + 1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576))) <= ((unsigned __int16)(*(unsigned __int16 *)(a3 + 8)))) goto loc_00399A11;
loc_0039945E:
loc_00399463:
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 588)));
    if (((unsigned int)((unsigned int)(a4))) >= 0x800ULL) goto loc_00399615;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 588) = (unsigned int)((unsigned int)(a4));
loc_00399492:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 584) = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 208));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 116)))) & (8)) == 0) goto loc_00399704;
loc_003994AB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416) == 0) goto loc_003994DF;
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576)))) goto loc_00399A5C;
loc_003994D6:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576) + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 208) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416));
    a2 = (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416))) ? 1 : 0;
loc_003994DF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120))) >> (13));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(a2)) != ((unsigned int)(result))) {
    }
    result = KiUpdateNodeAffinitizedFlag(*(unsigned __int64 *)(a1 + 8), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416), a4);
loc_00399502:
    if (((unsigned __int16)(*(unsigned __int8 *)(a1 + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576)))) goto loc_00399528;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 576) + *(unsigned __int8 *)(a1 + 208) * 8 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(a1 + 209)));
    if (((1) & ((unsigned __int8)(a2))) != 0) goto loc_00399598;
loc_00399528:
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_00399598;
    v_rbx = (a1) | (1);
    v_stack_m50 = v_rbx;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 36440))) == 0) goto loc_0039957B;
loc_0039955B:
    v_r14 = 0;
loc_00399561:
    if (condition_is_below) goto loc_003995DB;
    v_r15 = (*(unsigned __int64 *)(a1 + 36440) + 8) + (8);
    v_r12 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_0039955B;
loc_0039957B:
    if ((*(unsigned __int64 *)(a1 + 16)) == v_r12) goto loc_00399736;
loc_00399585:
    result = *(unsigned __int64 *)(a1 + 36440);
    if (v_stack_m50 != 0) {
        a1 = v_stack_m50;
        result = KiReleasePrcbLocksForIsolationUnit(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416), a4);
    }
    if ((unsigned __int8)((unsigned __int8)(v_r12 + 1)) != 0) {
        *(unsigned __int64 *)(v_stack_m48 + 64) = v_r12;
    }
loc_003995A2:
    if (((*(unsigned int *)(v_rip + 12768600)) & (0x1000ULL)) != 0) goto loc_00399A27;
loc_003995B2:
    if (((*(unsigned int *)(v_rip + 12768596)) & (0x8000000ULL)) != 0) goto loc_003999F7;
loc_003995C2:
    v_rsp = (v_rsp) + (80);
    return result;
loc_003995DB:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_stack_m48)));
    if (((*(unsigned int *)(v_rip + 12762311)) & ((unsigned int)(v_r14))) == 0) goto loc_003995F8;
loc_003995E7:
loc_003995E9:
    if (*(unsigned __int64 *)(v_stack_p18 + 48) == 0) goto loc_00399561;
    goto loc_003995DB;
loc_003995F8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12768442)))) & (64)) == 0) goto loc_003995E7;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003995E7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)(a4) * 8 + 16550976) + 36416), a4);
    goto loc_003995E9;
loc_00399615:
    v_stack_p20 = (unsigned int)(result);
    if (((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 208))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m48 + 576))))) goto loc_0039964F;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48 + 576) + *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 208) * 8 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 209)));
    if (((1) & ((unsigned __int8)(a2))) != 0) goto loc_00399492;
loc_0039964F:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m48 + 576))))) goto loc_00399A85;
loc_0039966D:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m48 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 128));
    if (condition_is_equal) goto loc_00399A64;
loc_0039967C:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136)))) << (6));
    v_stack_p10 = (unsigned int)(a1);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
loc_00399693:
    *(unsigned int *)(v_stack_m48 + 588) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)));
    goto loc_00399492;
loc_003996AE:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 2));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 4) = (unsigned int)(v_r12);
    a3 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136)))) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 2)))) { a3 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136))); }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976)) = (unsigned __int16)(a3);
    if (((unsigned __int16)(v_r12)) >= ((unsigned __int16)(a3))) goto loc_0039972B;
    a2 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + result * 8 + 16550976) + 192) + 136)) - (*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976));
loc_003996EC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8) = *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8 * 1);
    v_r10 = ((unsigned __int16)(a3)) - (1);
    if (condition_is_not_equal) goto loc_003996EC;
    goto loc_0039972B;
loc_00399704:
    result = KiComputeThreadAffinity(v_stack_m48, a2, a3, *(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8 + 8);
    if ((unsigned int)(result) == 0) goto loc_003994AB;
    goto loc_00399502;
loc_0039971F:
    a1 = (unsigned __int16)((v_stack_m48) + (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + (unsigned __int16)(v_stack_m48) * 8 + 8) = v_r12;
loc_0039972B:
    if (((unsigned __int16)(a1)) < (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 2))) goto loc_0039971F;
    goto loc_00399463;
loc_00399736:
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, *(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8 + 8);
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_m50, v_stack_m48, *(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8 + 8);
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a1 + 14312), a1, v_stack_m48, *(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976) + 8 + 8);
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (197));
    a1 = (unsigned __int8)((a1) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) != 0) goto loc_00399A96;
loc_0039979F:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(a1 + 14312), a5, v_stack_m48, result);
    a3 = 0;
    result = KiCommitRescheduleContext(*(unsigned __int64 *)(a1 + 14312), a1, a3, a5);
    result = (*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976)) & (-2);
    v_stack_m40 = result;
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rip - 3773552 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12098345) + a1 * 4)))) * 8 + 16550976)) & (1));
    if (condition_is_equal) goto loc_003999EB;
    if (((unsigned int)(v_rbx)) == 1) {
        a3 = *(unsigned __int64 *)(result + 36440);
        result = *(unsigned __int64 *)(result + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00399810;
loc_003997FE:
    if ((unsigned int)(a2 - 1) != 0) goto loc_003997FE;
loc_00399810:
    v_stack_p8 = (unsigned __int8)(v_r12);
    v_stack_m50 = v_r12;
    *(unsigned __int64 *)(v_stack_m48 + 64) = v_r12;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_003995A2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= ((unsigned __int8)(v_r12))) goto loc_003998D8;
loc_0039983B:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 51))) & (16)) != 0) goto loc_0039985B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 51))) & (8)) == 0) goto loc_00399879;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 16) + 7)) == 0) goto loc_00399879;
loc_0039985B:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_003998ED;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 16) + 36)));
loc_00399879:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 51)) & (2)) != 0) goto loc_003999D6;
loc_00399885:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 51)) & (4)) == 0) goto loc_003998A3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 16) + 36536) != 0) goto loc_0039993B;
loc_003998A3:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 16) + 36536);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 40);
    }
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + (1));
    if (((unsigned int)(v_r13)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0039983B;
    v_r12 = 0;
loc_003998D8:
    result = KiFlushSoftwareInterruptBatch(a1 + 13784, (unsigned int)((unsigned int)(a2 - 1)), a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 52)));
    goto loc_00399585;
loc_003998ED:
    if (((unsigned __int8)(result)) != 1) goto loc_00399932;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(v_stack_m50 + 36))) goto loc_00399879;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 52)));
loc_00399917:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(v_stack_m50 + 208), *(unsigned __int64 *)(v_stack_m50 + 200), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 52)));
    goto loc_00399879;
loc_00399932:
    goto loc_00399917;
loc_0039993B:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_003998A3;
    if (a1 == v_stack_m50) goto loc_003998A3;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    if (!(condition_is_equal)) {
        a3 = a1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00399AF8;
loc_00399975:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 12) = 2;
    result = (unsigned int)(*(unsigned int *)(result));
    v_r15 = (unsigned int)(*(unsigned int *)(v_stack_m50 + 36));
    if ((*(unsigned __int8 *)(v_rip + 12760715)) == 0) {
        result = *(unsigned __int8 *)(v_stack_m48 + (unsigned int)(*(unsigned int *)(v_stack_m50 + 36)) * 2 + 16568929);
        v_r15 = *(unsigned __int8 *)(v_stack_m48 + (unsigned int)(*(unsigned int *)(v_stack_m50 + 36)) * 2 + 16568928);
        v_r15 = (unsigned int)((v_r15) << (6));
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 8) = (unsigned int)(v_r15);
    result = (unsigned int)(*(unsigned int *)(v_rip + 12767589));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12767589)))) & (32)) != 0) {
        a1 = *(unsigned int *)(v_stack_m50 + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 52)));
    }
    a2 = ((unsigned int)((unsigned int)(v_r15))) >> (32);
    goto loc_003998A3;
loc_003999D6:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 * 8 + 40), v_stack_m50, a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4 * 8 + 52)));
    goto loc_00399885;
loc_003999EB:
    goto loc_003997FE;
loc_003999F7:
    result = EtwTraceIdealProcessor(v_stack_m48, (unsigned int)(0x546ULL), (unsigned int)(v_stack_m58), (unsigned int)(v_stack_p20));
    goto loc_003995C2;
loc_00399A11:
    if ((*(unsigned __int16 *)(v_stack_m48 + 2)) <= ((unsigned __int16)((unsigned int)(0x546ULL)))) goto loc_00399463;
    *(unsigned __int16 *)(v_stack_m48) = (unsigned __int16)(1 + (unsigned int)(0x546ULL) * 1);
    goto loc_0039945E;
loc_00399A27:
    a4 = 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 116))) >> (3));
    a3 = (unsigned __int8)((a3) & (1));
    v_stack_p28 = 0x536ULL;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_m48 + 576);
    result = EtwTraceThreadAffinity(v_stack_m48, *(unsigned __int16 *)(v_stack_m48 + 584), a3, a4);
    goto loc_003995B2;
loc_00399A5C:
    goto loc_003994D6;
loc_00399A64:
    a3 = (unsigned __int16)((a3) - 1);
    if (sign_flag) goto loc_00399A8D;
    if (*(unsigned __int64 *)(a4 + (__int16)((unsigned __int16)(a3)) * 8 + 8) == 0) goto loc_00399A64;
    goto loc_0039967C;
loc_00399A85:
    goto loc_0039966D;
loc_00399A8D:
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    goto loc_00399693;
loc_00399A96:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_00399AEF;
loc_00399AA3:
    a2 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 14312) + a2 * 8) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8 + 16) = result;
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8 + 32);
        result = (unsigned __int8)((result) & (197));
        result = (unsigned __int8)((result) | (5));
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8 + 32) = (unsigned __int8)(result);
        result = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8 + 24) = result;
    }
    a3 = (unsigned int)((0) + (1));
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00399AA3;
loc_00399AEF:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = 0;
    goto loc_0039979F;
loc_00399AF8:
    if ((unsigned int)(*(unsigned __int64 *)(a1 + 14312) + a2 * 8) == 0) goto loc_003998A3;
    if (((unsigned int)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) >= 0) goto loc_003998A3;
    goto loc_00399975;
}
```

## 5. (Beta) C Style

```c
int64_t KiSetSystemAffinityThread(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint16_t v_stack_p28;
    uint8_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (80);
    local_r12 = 0;
    v_stack_m50 = 0;
    v_stack_m48 = *(uint64_t *)(arg1 + 0x8);
    if (Arg2 != 0) goto loc_003996AE;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240))) << (3);
    result = memset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240) + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240)) = (uint16_t)(local_r12 + 1);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240))) <= ((uint16_t)(*(uint16_t *)(arg3 + 0x8)))) goto loc_00399A11;
loc_0039945E:
loc_00399463:
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x24C)));
    if (((uint32_t)((uint32_t)(Arg4))) >= 0x800ULL) goto loc_00399615;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x24C) = (uint32_t)((uint32_t)(Arg4));
loc_00399492:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x248) = (uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0xD0));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x74)))) & (8)) == 0) goto loc_00399704;
loc_003994AB:
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40) == 0) goto loc_003994DF;
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240)))) goto loc_00399A5C;
loc_003994D6:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240) + *(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0xD0) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40));
    Arg2 = (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40))) ? 1 : 0;
loc_003994DF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78))) >> (13));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(Arg2)) != ((uint32_t)(result))) {
    }
    result = KiUpdateNodeAffinitizedFlag(*(uint64_t *)(arg1 + 0x8), Arg2, *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40), Arg4);
loc_00399502:
    if (((uint16_t)(*(uint8_t *)(arg1 + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240)))) goto loc_00399528;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x240) + *(uint8_t *)(arg1 + 0xD0) * 8 + 0x8)) >> ((uint8_t)(*(uint8_t *)(arg1 + 0xD1)));
    if (((1) & ((uint8_t)(Arg2))) != 0) goto loc_00399598;
loc_00399528:
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_00399598;
    local_rbx = (Arg1) | (1);
    v_stack_m50 = local_rbx;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8E58))) == 0) goto loc_0039957B;
loc_0039955B:
    local_r14 = 0;
loc_00399561:
    if (condition_is_below) goto loc_003995DB;
    local_r15 = (*(uint64_t *)(arg1 + 0x8E58) + 8) + (8);
    local_r12 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_0039955B;
loc_0039957B:
    if ((*(uint64_t *)(arg1 + 0x10)) == local_r12) goto loc_00399736;
loc_00399585:
    result = *(uint64_t *)(arg1 + 0x8E58);
    if (v_stack_m50 != 0) {
        Arg1 = v_stack_m50;
        result = KiReleasePrcbLocksForIsolationUnit(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40), Arg4);
    }
    if ((uint8_t)((uint8_t)(local_r12 + 1)) != 0) {
        *(uint64_t *)(v_stack_m48 + 0x40) = local_r12;
    }
loc_003995A2:
    if (((*(uint32_t *)(v_rip + 0xC2D558)) & (0x1000ULL)) != 0) goto loc_00399A27;
loc_003995B2:
    if (((*(uint32_t *)(v_rip + 0xC2D554)) & (0x8000000ULL)) != 0) goto loc_003999F7;
loc_003995C2:
    local_rsp = (local_rsp) + (80);
    return result;
loc_003995DB:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(v_stack_m48)));
    if (((*(uint32_t *)(v_rip + 0xC2BCC7)) & ((uint32_t)(local_r14))) == 0) goto loc_003995F8;
loc_003995E7:
loc_003995E9:
    if (*(uint64_t *)(v_stack_p18 + 0x30) == 0) goto loc_00399561;
    goto loc_003995DB;
loc_003995F8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2D4BA)))) & (64)) == 0) goto loc_003995E7;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003995E7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)(Arg4) * 8 + 0xFC8C40) + 0x8E40), Arg4);
    goto loc_003995E9;
loc_00399615:
    v_stack_p20 = (uint32_t)(result);
    if (((uint16_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xD0))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m48 + 0x240))))) goto loc_0039964F;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m48 + 0x240) + *(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xD0) * 8 + 0x8)) >> ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xD1)));
    if (((1) & ((uint8_t)(Arg2))) != 0) goto loc_00399492;
loc_0039964F:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m48 + 0x240))))) goto loc_00399A85;
loc_0039966D:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m48 + 0x240) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x80));
    if (condition_is_equal) goto loc_00399A64;
loc_0039967C:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88)))) << (6));
    v_stack_p10 = (uint32_t)(Arg1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
loc_00399693:
    *(uint32_t *)(v_stack_m48 + 0x24C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)));
    goto loc_00399492;
loc_003996AE:
    *(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x2));
    *(uint32_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x4) = (uint32_t)(local_r12);
    Arg3 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x2));
    if (((uint16_t)(*(uint16_t *)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88)))) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x2)))) { Arg3 = (uint16_t)(*(uint16_t *)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88))); }
    *(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40)) = (uint16_t)(Arg3);
    if (((uint16_t)(local_r12)) >= ((uint16_t)(Arg3))) goto loc_0039972B;
    Arg2 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + result * 8 + 0xFC8C40) + 0xC0) + 0x88)) - (*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40));
loc_003996EC:
    *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x8) = *(uint64_t *)(Arg2 + *(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x8 * 1);
    local_r10 = ((uint16_t)(Arg3)) - (1);
    if (condition_is_not_equal) goto loc_003996EC;
    goto loc_0039972B;
loc_00399704:
    result = KiComputeThreadAffinity(v_stack_m48, Arg2, Arg3, *(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 8 + 8);
    if ((uint32_t)(result) == 0) goto loc_003994AB;
    goto loc_00399502;
loc_0039971F:
    Arg1 = (uint16_t)((v_stack_m48) + (1));
    *(uint64_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + (uint16_t)(v_stack_m48) * 8 + 0x8) = local_r12;
loc_0039972B:
    if (((uint16_t)(Arg1)) < (*(uint16_t *)(*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 0x2))) goto loc_0039971F;
    goto loc_00399463;
loc_00399736:
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, *(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 8 + 8);
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_m50, v_stack_m48, *(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 8 + 8);
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg1 + 0x37E8), Arg1, v_stack_m48, *(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40) + 8 + 8);
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) & (197));
    Arg1 = (uint8_t)((Arg1) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) != 0) goto loc_00399A96;
loc_0039979F:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), Arg5, v_stack_m48, result);
    Arg3 = 0;
    result = KiCommitRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), Arg1, Arg3, Arg5);
    result = (*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40)) & (-2);
    v_stack_m40 = result;
    local_rbx = (uint32_t)((*(uint64_t *)(v_rip - 0x399470 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB89B29) + arg1 * 4)))) * 8 + 0xFC8C40)) & (1));
    if (condition_is_equal) goto loc_003999EB;
    if (((uint32_t)(local_rbx)) == 1) {
        Arg3 = *(uint64_t *)(result + 0x8E58);
        result = *(uint64_t *)(result + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00399810;
loc_003997FE:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_003997FE;
loc_00399810:
    v_stack_p8 = (uint8_t)(local_r12);
    v_stack_m50 = local_r12;
    *(uint64_t *)(v_stack_m48 + 0x40) = local_r12;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_003995A2;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= ((uint8_t)(local_r12))) goto loc_003998D8;
loc_0039983B:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x33))) & (16)) != 0) goto loc_0039985B;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x33))) & (8)) == 0) goto loc_00399879;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_00399879;
loc_0039985B:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_003998ED;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x10) + 0x24)));
loc_00399879:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x33)) & (2)) != 0) goto loc_003999D6;
loc_00399885:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x33)) & (4)) == 0) goto loc_003998A3;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_0039993B;
loc_003998A3:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x10) + 0x8EB8);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x28);
    }
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + (1));
    if (((uint32_t)(local_r13)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0039983B;
    local_r12 = 0;
loc_003998D8:
    result = KiFlushSoftwareInterruptBatch(Arg1 + 13784, (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x34)));
    goto loc_00399585;
loc_003998ED:
    if (((uint8_t)(result)) != 1) goto loc_00399932;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(v_stack_m50 + 0x24))) goto loc_00399879;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), Arg3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x34)));
loc_00399917:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(v_stack_m50 + 0xD0), *(uint64_t *)(v_stack_m50 + 0xC8), (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x34)));
    goto loc_00399879;
loc_00399932:
    goto loc_00399917;
loc_0039993B:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_003998A3;
    if (Arg1 == v_stack_m50) goto loc_003998A3;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    if (!(condition_is_equal)) {
        Arg3 = Arg1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00399AF8;
loc_00399975:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0xC) = 2;
    result = (uint32_t)(*(uint32_t *)(result));
    local_r15 = (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24));
    if ((*(uint8_t *)(v_rip + 0xC2B68B)) == 0) {
        result = *(uint8_t *)(v_stack_m48 + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)) * 2 + 0xFCD261);
        local_r15 = *(uint8_t *)(v_stack_m48 + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)) * 2 + 0xFCD260);
        local_r15 = (uint32_t)((local_r15) << (6));
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0x8) = (uint32_t)(local_r15);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC2D165));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2D165)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m50 + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, Arg3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x34)));
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) >> (32);
    goto loc_003998A3;
loc_003999D6:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 * 8 + 0x28), v_stack_m50, Arg3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4 * 8 + 0x34)));
    goto loc_00399885;
loc_003999EB:
    goto loc_003997FE;
loc_003999F7:
    result = EtwTraceIdealProcessor(v_stack_m48, (uint32_t)(0x546ULL), (uint32_t)(v_stack_m58), (uint32_t)(v_stack_p20));
    goto loc_003995C2;
loc_00399A11:
    if ((*(uint16_t *)(v_stack_m48 + 0x2)) <= ((uint16_t)((uint32_t)(0x546ULL)))) goto loc_00399463;
    *(uint16_t *)(v_stack_m48) = (uint16_t)(1 + (uint32_t)(0x546ULL) * 1);
    goto loc_0039945E;
loc_00399A27:
    Arg4 = 0;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x74))) >> (3));
    Arg3 = (uint8_t)((Arg3) & (1));
    v_stack_p28 = 0x536ULL;
    v_stack_p20 = *(uint64_t *)(v_stack_m48 + 0x240);
    result = EtwTraceThreadAffinity(v_stack_m48, *(uint16_t *)(v_stack_m48 + 0x248), Arg3, Arg4);
    goto loc_003995B2;
loc_00399A5C:
    goto loc_003994D6;
loc_00399A64:
    Arg3 = (uint16_t)((Arg3) - 1);
    if (sign_flag) goto loc_00399A8D;
    if (*(uint64_t *)(Arg4 + (int16_t)((uint16_t)(arg3)) * 8 + 0x8) == 0) goto loc_00399A64;
    goto loc_0039967C;
loc_00399A85:
    goto loc_0039966D;
loc_00399A8D:
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    goto loc_00399693;
loc_00399A96:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_00399AEF;
loc_00399AA3:
    Arg2 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8);
        result = *(uint64_t *)(arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8 + 0x10) = result;
        result = *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8 + 0x20);
        result = (uint8_t)((result) & (197));
        result = (uint8_t)((result) | (5));
        *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8 + 0x20) = (uint8_t)(result);
        result = *(uint64_t *)(arg1 + 0x18);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8 + 0x18) = result;
    }
    Arg3 = (uint32_t)((0) + (1));
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00399AA3;
loc_00399AEF:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = 0;
    goto loc_0039979F;
loc_00399AF8:
    if ((uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + Arg2 * 8) == 0) goto loc_003998A3;
    if (((uint32_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) >= 0) goto loc_003998A3;
    goto loc_00399975;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `8` | `R` |
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg1` | `+ 0x8E58` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003993E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
