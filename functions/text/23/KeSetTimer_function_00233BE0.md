# KeSetTimer

- RVA: `0x00233BE0`–`0x002341F0` (길이 `1,552` bytes)
- VA: `0x0000000140233BE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060534`
- 디코드: `363`개 명령, `1,552/1,552` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00233DF1` → [KiComputeDueTime](KiComputeDueTime_function_002332E8.md) (function, `0x002332E8`)
- `0x00233E1A` → [KiInsertTimerTable](KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x00233E4A` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00233E5E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00233E88` → [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x00233EAE` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00234036` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00234046` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002340D8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002340E3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002340F8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00234108` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00234120` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023412F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00234147` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00234156` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0023416E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0023417E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002341C4` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002341D7` → [KiTraceSetTimer](../22/KiTraceSetTimer_function_0022FB08.md) (function, `0x0022FB08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00233BF7` → RVA `0x00E0A740` (`.data`; read)
- `0x00233C09` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x00233C13` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x00233C4D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00233C6E` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00233CD3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00233D86` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x00233D9B` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x00233F34` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x00234028` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00233BE0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00233BE5  55                              push rbp
00233BE6  56                              push rsi
00233BE7  57                              push rdi
00233BE8  41 54                           push r12
00233BEA  41 55                           push r13
00233BEC  41 56                           push r14
00233BEE  41 57                           push r15
00233BF0  48 81 EC 90 00 00 00            sub rsp, 0x90
00233BF7  48 8B 05 42 6B BD 00            mov rax, qword ptr [rip + 0xbd6b42]
00233BFE  48 33 C4                        xor rax, rsp
00233C01  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00233C09  48 8B 05 68 33 D9 00            mov rax, qword ptr [rip + 0xd93368]
00233C10  49 8B E8                        mov rbp, r8
00233C13  48 33 2D 36 36 D9 00            xor rbp, qword ptr [rip + 0xd93636]
00233C1A  48 8B F9                        mov rdi, rcx
00233C1D  48 0F CD                        bswap rbp
00233C20  48 33 E9                        xor rbp, rcx
00233C23  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
00233C28  8B C8                           mov ecx, eax
00233C2A  C7 44 24 30 00 00 00 00         mov dword ptr [rsp + 0x30], 0
00233C32  48 D3 CD                        ror rbp, cl
00233C35  48 8B DA                        mov rbx, rdx
00233C38  48 33 E8                        xor rbp, rax
00233C3B  45 0F 20 C5                     mov r13, cr8
00233C3F  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00233C44  B8 02 00 00 00                  mov eax, 2
00233C49  44 0F 22 C0                     mov cr8, rax
00233C4D  83 3D CC 30 D9 00 00            cmp dword ptr [rip + 0xd930cc], 0
00233C54  0F 85 4D 02 00 00               jne 0x140233ea7
00233C5A  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00233C63  45 33 F6                        xor r14d, r14d
00233C66  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00233C6B  45 32 E4                        xor r12b, r12b
00233C6E  48 8D 15 8B C3 DC FF            lea rdx, [rip - 0x233c75]
00233C75  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00233C7A  41 8B F6                        mov esi, r14d
00233C7D  0F 82 ED 02 00 00               jb 0x140233f70
00233C83  F6 47 03 C0                     test byte ptr [rdi + 3], 0xc0
00233C87  0F 84 F9 00 00 00               je 0x140233d86
00233C8D  0F B6 4F 02                     movzx ecx, byte ptr [rdi + 2]
00233C91  0F B7 47 38                     movzx eax, word ptr [rdi + 0x38]
00233C95  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00233C99  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00233C9E  48 8D 71 10                     lea rsi, [rcx + 0x10]
00233CA2  4C 8B 8C C2 40 8C FC 00         mov r9, qword ptr [rdx + rax*8 + 0xfc8c40]
00233CAA  0F B7 47 3A                     movzx eax, word ptr [rdi + 0x3a]
00233CAE  48 C1 E0 08                     shl rax, 8
00233CB2  48 03 F0                        add rsi, rax
00233CB5  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00233CBA  48 C1 E6 05                     shl rsi, 5
00233CBE  4D 8D 91 00 41 00 00            lea r10, [r9 + 0x4100]
00233CC5  49 03 F2                        add rsi, r10
00233CC8  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00233CCE  73 1C                           jae 0x140233cec
00233CD0  41 FF C6                        inc r14d
00233CD3  44 85 35 D2 15 D9 00            test dword ptr [rip + 0xd915d2], r14d
00233CDA  0F 84 48 03 00 00               je 0x140234028
00233CE0  F3 90                           pause
00233CE2  48 8B 06                        mov rax, qword ptr [rsi]
00233CE5  48 85 C0                        test rax, rax
00233CE8  74 DE                           je 0x140233cc8
00233CEA  EB E4                           jmp 0x140233cd0
00233CEC  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00233CF0  84 C0                           test al, al
00233CF2  0F 88 77 03 00 00               js 0x14023406f
00233CF8  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
00233CFD  48 8D 57 20                     lea rdx, [rdi + 0x20]
00233D01  44 0F B7 47 3A                  movzx r8d, word ptr [rdi + 0x3a]
00233D06  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00233D0B  41 8B C0                        mov eax, r8d
00233D0E  48 8B 0A                        mov rcx, qword ptr [rdx]
00233D11  48 C1 E0 08                     shl rax, 8
00233D15  4D 8D 6B 10                     lea r13, [r11 + 0x10]
00233D19  4C 03 E8                        add r13, rax
00233D1C  4D 8D 4B 10                     lea r9, [r11 + 0x10]
00233D20  49 C1 E5 05                     shl r13, 5
00233D24  4D 8D 94 24 00 41 00 00         lea r10, [r12 + 0x4100]
00233D2C  41 8B C0                        mov eax, r8d
00233D2F  4D 03 EA                        add r13, r10
00233D32  48 83 F0 01                     xor rax, 1
00233D36  48 C1 E0 08                     shl rax, 8
00233D3A  4C 03 C8                        add r9, rax
00233D3D  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00233D41  49 C1 E1 05                     shl r9, 5
00233D45  4D 03 CA                        add r9, r10
00233D48  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00233D4D  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
00233D51  75 05                           jne 0x140233d58
00233D53  48 39 10                        cmp qword ptr [rax], rdx
00233D56  74 07                           je 0x140233d5f
00233D58  B9 03 00 00 00                  mov ecx, 3
00233D5D  CD 29                           int 0x29
00233D5F  48 89 08                        mov qword ptr [rax], rcx
00233D62  48 89 41 08                     mov qword ptr [rcx + 8], rax
00233D66  48 3B C1                        cmp rax, rcx
00233D69  0F 84 49 01 00 00               je 0x140233eb8
00233D6F  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00233D74  F0 81 27 FF FF FF BF            lock and dword ptr [rdi], 0xbfffffff
00233D7B  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00233D80  41 B4 01                        mov r12b, 1
00233D83  45 33 F6                        xor r14d, r14d
00233D86  F7 05 78 2D D9 00 00 00 02 00   test dword ptr [rip + 0xd92d78], 0x20000
00233D90  BE 01 00 00 00                  mov esi, 1
00233D95  0F 85 ED 03 00 00               jne 0x140234188
00233D9B  83 3D A6 2E D9 00 00            cmp dword ptr [rip + 0xd92ea6], 0
00233DA2  0F 85 F7 00 00 00               jne 0x140233e9f
00233DA8  41 80 7F 20 00                  cmp byte ptr [r15 + 0x20], 0
00233DAD  75 20                           jne 0x140233dcf
00233DAF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00233DB8  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00233DBF  F7 81 F4 01 00 00 00 10 00 00   test dword ptr [rcx + 0x1f4], 0x1000
00233DC9  0F 85 C0 00 00 00               jne 0x140233e8f
00233DCF  0F B7 D6                        movzx edx, si
00233DD2  B8 3A 00 00 00                  mov eax, 0x3a
00233DD7  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00233DDC  48 8B CF                        mov rcx, rdi
00233DDF  45 33 C0                        xor r8d, r8d
00233DE2  66 89 14 01                     mov word ptr [rcx + rax], dx
00233DE6  48 8B D3                        mov rdx, rbx
00233DE9  48 89 6F 30                     mov qword ptr [rdi + 0x30], rbp
00233DED  44 89 77 3C                     mov dword ptr [rdi + 0x3c], r14d
00233DF1  E8 F2 F4 FF FF                  call 0x1402332e8
00233DF6  85 C0                           test eax, eax
00233DF8  0F 84 81 00 00 00               je 0x140233e7f
00233DFE  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00233E03  48 8B D7                        mov rdx, rdi
00233E06  44 89 77 04                     mov dword ptr [rdi + 4], r14d
00233E0A  49 8B CF                        mov rcx, r15
00233E0D  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00233E12  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00233E17  4D 8B C6                        mov r8, r14
00233E1A  E8 E1 F5 FF FF                  call 0x140233400
00233E1F  84 C0                           test al, al
00233E21  74 5C                           je 0x140233e7f
00233E23  F7 05 DB 2C D9 00 00 00 02 00   test dword ptr [rip + 0xd92cdb], 0x20000
00233E2D  0F 85 9B 03 00 00               jne 0x1402341ce
00233E33  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
00233E3A  45 33 C9                        xor r9d, r9d
00233E3D  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
00233E42  44 8B C6                        mov r8d, esi
00233E45  33 D2                           xor edx, edx
00233E47  49 8B CF                        mov rcx, r15
00233E4A  E8 A1 DE 01 00                  call 0x140251cf0
00233E4F  41 0F B6 C4                     movzx eax, r12b
00233E53  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00233E5B  48 33 CC                        xor rcx, rsp
00233E5E  E8 DD 87 47 00                  call 0x1406ac640
00233E63  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00233E6B  48 81 C4 90 00 00 00            add rsp, 0x90
00233E72  41 5F                           pop r15
00233E74  41 5E                           pop r14
00233E76  41 5D                           pop r13
00233E78  41 5C                           pop r12
00233E7A  5F                              pop rdi
00233E7B  5E                              pop rsi
00233E7C  5D                              pop rbp
00233E7D  C3                              ret
00233E7E  CC                              int3
00233E7F  45 33 C0                        xor r8d, r8d
00233E82  48 8B D7                        mov rdx, rdi
00233E85  49 8B CF                        mov rcx, r15
00233E88  E8 43 F9 FF FF                  call 0x1402337d0
00233E8D  EB AB                           jmp 0x140233e3a
00233E8F  F7 81 FC 05 00 00 00 00 00 04   test dword ptr [rcx + 0x5fc], 0x4000000
00233E99  0F 85 30 FF FF FF               jne 0x140233dcf
00233E9F  41 8B D6                        mov edx, r14d
00233EA2  E9 2B FF FF FF                  jmp 0x140233dd2
00233EA7  0F B6 D0                        movzx edx, al
00233EAA  41 0F B6 CD                     movzx ecx, r13b
00233EAE  E8 49 18 2C 00                  call 0x1404f56fc
00233EB3  E9 A2 FD FF FF                  jmp 0x140233c5a
00233EB8  41 C7 45 1C FF FF FF FF         mov dword ptr [r13 + 0x1c], 0xffffffff
00233EC0  66 45 85 C0                     test r8w, r8w
00233EC4  0F 85 CF 00 00 00               jne 0x140233f99
00233ECA  4D 8D B3 10 01 00 00            lea r14, [r11 + 0x110]
00233ED1  49 C1 E6 05                     shl r14, 5
00233ED5  4D 03 F2                        add r14, r10
00233ED8  45 33 E4                        xor r12d, r12d
00233EDB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00233EE0  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00233EE6  73 1C                           jae 0x140233f04
00233EE8  41 FF C4                        inc r12d
00233EEB  44 85 25 BA 13 D9 00            test dword ptr [rip + 0xd913ba], r12d
00233EF2  0F 84 F2 01 00 00               je 0x1402340ea
00233EF8  F3 90                           pause
00233EFA  49 8B 06                        mov rax, qword ptr [r14]
00233EFD  48 85 C0                        test rax, rax
00233F00  74 DE                           je 0x140233ee0
00233F02  EB E4                           jmp 0x140233ee8
00233F04  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00233F09  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
00233F0E  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00233F13  41 83 7D 1C FF                  cmp dword ptr [r13 + 0x1c], -1
00233F18  75 44                           jne 0x140233f5e
00233F1A  41 83 79 1C FF                  cmp dword ptr [r9 + 0x1c], -1
00233F1F  75 3D                           jne 0x140233f5e
00233F21  41 0F B6 84 24 D0 00 00 00      movzx eax, byte ptr [r12 + 0xd0]
00233F2A  48 8D 0D CF C0 DC FF            lea rcx, [rip - 0x233f31]
00233F31  48 03 C0                        add rax, rax
00233F34  83 3D F5 10 D9 00 00            cmp dword ptr [rip + 0xd910f5], 0
00233F3B  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
00233F43  0F 84 07 01 00 00               je 0x140234050
00233F49  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00233F4D  49 C1 EB 06                     shr r11, 6
00233F51  83 E0 3F                        and eax, 0x3f
00233F54  F0 4A 0F B3 04 D9               lock btr qword ptr [rcx + r11*8], rax
00233F5A  4A 8D 0C D9                     lea rcx, [rcx + r11*8]
00233F5E  F0 49 83 26 00                  lock and qword ptr [r14], 0
00233F63  E9 07 FE FF FF                  jmp 0x140233d6f
00233F68  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00233F70  FF C6                           inc esi
00233F72  85 35 34 13 D9 00               test dword ptr [rip + 0xd91334], esi
00233F78  0F 84 94 01 00 00               je 0x140234112
00233F7E  F3 90                           pause
00233F80  8B 07                           mov eax, dword ptr [rdi]
00233F82  84 C0                           test al, al
00233F84  78 EA                           js 0x140233f70
00233F86  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00233F8B  72 E3                           jb 0x140233f70
00233F8D  48 8D 15 6C C0 DC FF            lea rdx, [rip - 0x233f94]
00233F94  E9 EA FC FF FF                  jmp 0x140233c83
00233F99  4D 8D 73 10                     lea r14, [r11 + 0x10]
00233F9D  49 C1 E6 05                     shl r14, 5
00233FA1  4D 03 F2                        add r14, r10
00233FA4  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00233FAA  73 04                           jae 0x140233fb0
00233FAC  F3 90                           pause
00233FAE  EB 09                           jmp 0x140233fb9
00233FB0  4D 85 F6                        test r14, r14
00233FB3  0F 85 5A FF FF FF               jne 0x140233f13
00233FB9  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00233FBE  33 F6                           xor esi, esi
00233FC0  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00233FC6  73 1A                           jae 0x140233fe2
00233FC8  FF C6                           inc esi
00233FCA  85 35 DC 12 D9 00               test dword ptr [rip + 0xd912dc], esi
00233FD0  0F 84 63 01 00 00               je 0x140234139
00233FD6  F3 90                           pause
00233FD8  49 8B 06                        mov rax, qword ptr [r14]
00233FDB  48 85 C0                        test rax, rax
00233FDE  74 E0                           je 0x140233fc0
00233FE0  EB E6                           jmp 0x140233fc8
00233FE2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00233FE7  49 8D 94 24 00 41 00 00         lea rdx, [r12 + 0x4100]
00233FEF  48 81 C6 10 01 00 00            add rsi, 0x110
00233FF6  48 C1 E6 05                     shl rsi, 5
00233FFA  48 03 F2                        add rsi, rdx
00233FFD  45 33 E4                        xor r12d, r12d
00234000  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00234006  0F 83 F8 FE FF FF               jae 0x140233f04
0023400C  41 FF C4                        inc r12d
0023400F  44 85 25 96 12 D9 00            test dword ptr [rip + 0xd91296], r12d
00234016  0F 84 44 01 00 00               je 0x140234160
0023401C  F3 90                           pause
0023401E  48 8B 06                        mov rax, qword ptr [rsi]
00234021  48 85 C0                        test rax, rax
00234024  74 DA                           je 0x140234000
00234026  EB E4                           jmp 0x14023400c
00234028  8B 05 8A 2A D9 00               mov eax, dword ptr [rip + 0xd92a8a]
0023402E  A8 40                           test al, 0x40
00234030  0F 84 AA FC FF FF               je 0x140233ce0
00234036  E8 55 B4 0D 00                  call 0x14030f490
0023403B  84 C0                           test al, al
0023403D  0F 84 9D FC FF FF               je 0x140233ce0
00234043  41 8B CE                        mov ecx, r14d
00234046  E8 15 B4 0D 00                  call 0x14030f460
0023404B  E9 92 FC FF FF                  jmp 0x140233ce2
00234050  41 0F B6 84 24 D1 00 00 00      movzx eax, byte ptr [r12 + 0xd1]
00234059  49 C1 E3 06                     shl r11, 6
0023405D  49 03 CB                        add rcx, r11
00234060  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
00234065  F0 49 83 26 00                  lock and qword ptr [r14], 0
0023406A  E9 00 FD FF FF                  jmp 0x140233d6f
0023406F  F0 48 83 26 00                  lock and qword ptr [rsi], 0
00234074  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00234078  45 33 F6                        xor r14d, r14d
0023407B  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00234080  83 E0 3F                        and eax, 0x3f
00234083  41 8B CE                        mov ecx, r14d
00234086  49 87 8C C0 00 41 00 00         xchg qword ptr [r8 + rax*8 + 0x4100], rcx
0023408E  48 85 C9                        test rcx, rcx
00234091  0F 85 4A 01 00 00               jne 0x1402341e1
00234097  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
0023409E  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
002340A2  48 8D 15 57 BF DC FF            lea rdx, [rip - 0x2340a9]
002340A9  41 8B F6                        mov esi, r14d
002340AC  84 C0                           test al, al
002340AE  0F 89 C1 FB FF FF               jns 0x140233c75
002340B4  FF C6                           inc esi
002340B6  85 35 F0 11 D9 00               test dword ptr [rip + 0xd911f0], esi
002340BC  74 10                           je 0x1402340ce
002340BE  F3 90                           pause
002340C0  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
002340C4  84 C0                           test al, al
002340C6  0F 89 A2 FB FF FF               jns 0x140233c6e
002340CC  EB E6                           jmp 0x1402340b4
002340CE  8B 05 E4 29 D9 00               mov eax, dword ptr [rip + 0xd929e4]
002340D4  A8 40                           test al, 0x40
002340D6  74 E6                           je 0x1402340be
002340D8  E8 B3 B3 0D 00                  call 0x14030f490
002340DD  84 C0                           test al, al
002340DF  74 DD                           je 0x1402340be
002340E1  8B CE                           mov ecx, esi
002340E3  E8 78 B3 0D 00                  call 0x14030f460
002340E8  EB D6                           jmp 0x1402340c0
002340EA  8B 05 C8 29 D9 00               mov eax, dword ptr [rip + 0xd929c8]
002340F0  A8 40                           test al, 0x40
002340F2  0F 84 00 FE FF FF               je 0x140233ef8
002340F8  E8 93 B3 0D 00                  call 0x14030f490
002340FD  84 C0                           test al, al
002340FF  0F 84 F3 FD FF FF               je 0x140233ef8
00234105  41 8B CC                        mov ecx, r12d
00234108  E8 53 B3 0D 00                  call 0x14030f460
0023410D  E9 E8 FD FF FF                  jmp 0x140233efa
00234112  8B 05 A0 29 D9 00               mov eax, dword ptr [rip + 0xd929a0]
00234118  A8 40                           test al, 0x40
0023411A  0F 84 5E FE FF FF               je 0x140233f7e
00234120  E8 6B B3 0D 00                  call 0x14030f490
00234125  84 C0                           test al, al
00234127  0F 84 51 FE FF FF               je 0x140233f7e
0023412D  8B CE                           mov ecx, esi
0023412F  E8 2C B3 0D 00                  call 0x14030f460
00234134  E9 47 FE FF FF                  jmp 0x140233f80
00234139  8B 05 79 29 D9 00               mov eax, dword ptr [rip + 0xd92979]
0023413F  A8 40                           test al, 0x40
00234141  0F 84 8F FE FF FF               je 0x140233fd6
00234147  E8 44 B3 0D 00                  call 0x14030f490
0023414C  84 C0                           test al, al
0023414E  0F 84 82 FE FF FF               je 0x140233fd6
00234154  8B CE                           mov ecx, esi
00234156  E8 05 B3 0D 00                  call 0x14030f460
0023415B  E9 78 FE FF FF                  jmp 0x140233fd8
00234160  8B 05 52 29 D9 00               mov eax, dword ptr [rip + 0xd92952]
00234166  A8 40                           test al, 0x40
00234168  0F 84 AE FE FF FF               je 0x14023401c
0023416E  E8 1D B3 0D 00                  call 0x14030f490
00234173  84 C0                           test al, al
00234175  0F 84 A1 FE FF FF               je 0x14023401c
0023417B  41 8B CC                        mov ecx, r12d
0023417E  E8 DD B2 0D 00                  call 0x14030f460
00234183  E9 96 FE FF FF                  jmp 0x14023401e
00234188  45 84 E4                        test r12b, r12b
0023418B  0F 84 0A FC FF FF               je 0x140233d9b
00234191  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00234196  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0023419B  41 B9 55 0F 00 00               mov r9d, 0xf55
002341A1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002341A6  41 B8 00 00 02 40               mov r8d, 0x40020000
002341AC  48 C7 44 24 78 08 00 00 00      mov qword ptr [rsp + 0x78], 8
002341B5  8B D6                           mov edx, esi
002341B7  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002341BF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
002341C4  E8 87 11 00 00                  call 0x140235350
002341C9  E9 CD FB FF FF                  jmp 0x140233d9b
002341CE  45 33 C0                        xor r8d, r8d
002341D1  49 8B D6                        mov rdx, r14
002341D4  48 8B CF                        mov rcx, rdi
002341D7  E8 2C B9 FF FF                  call 0x14022fb08
002341DC  E9 59 FC FF FF                  jmp 0x140233e3a
002341E1  F0 81 27 FF FF FF 00            lock and dword ptr [rdi], 0xffffff
002341E8  41 B4 01                        mov r12b, 1
002341EB  E9 96 FB FF FF                  jmp 0x140233d86
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSetTimer(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 12413762)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rbp = (a3) ^ (*(unsigned __int64 *)(v_rip + 14235190));
    v_rbp = (v_rbp) ^ (a1);
    v_stack_m60 = a3;
    v_stack_m98 = 0;
    v_rbp = (v_rbp) ^ (*(unsigned __int64 *)(v_rip + 14234472));
    v_stack_m58 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14233804)) != 0) goto loc_00233EA7;
loc_00233C5A:
    v_r14 = 0;
    v_stack_m70 = 0;
    v_r12 = 0;
loc_00233C6E:
loc_00233C75:
    if (condition_is_below) goto loc_00233F70;
loc_00233C83:
    if (((*(unsigned __int8 *)(a1 + 3)) & (192)) == 0) goto loc_00233D86;
    v_stack_m80 = (unsigned int)(*(unsigned __int8 *)(a1 + 2));
    v_stack_m90 = *(unsigned __int8 *)(a1 + 2);
    result = (*(unsigned __int16 *)(a1 + 58)) << (8);
    v_rsi = (*(unsigned __int8 *)(a1 + 2) + 16) + (result);
    v_stack_m88 = *(unsigned __int64 *)(v_rip - 2309237 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip - 2309237 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976) + 16640);
loc_00233CC8:
    if (condition_is_above_or_equal) goto loc_00233CEC;
loc_00233CD0:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14226898)) & ((unsigned int)(v_r14))) == 0) goto loc_00234028;
loc_00233CE0:
loc_00233CE2:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00233CC8;
    goto loc_00233CD0;
loc_00233CEC:
    if (sign_flag) goto loc_0023406F;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) << (8);
    v_r13 = (v_stack_m90 + 16) + (result);
    v_r13 = (v_r13) << (5);
    v_r13 = (v_r13) + (v_stack_m88 + 16640);
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) ^ (1);
    result = (result) << (8);
    a4 = (v_stack_m90 + 16) + (result);
    a4 = (a4) << (5);
    a4 = (a4) + (v_stack_m88 + 16640);
    v_stack_m78 = a4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (a1 + 32)) goto loc_00233D58;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8))) != (a1 + 32)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a1 + 32 + 8);
    if ((*(unsigned __int64 *)(a1 + 32 + 8)) == a1) goto loc_00233EB8;
loc_00233D6F:
    v_r14 = 0;
loc_00233D86:
    if (((*(unsigned int *)(v_rip + 14232952)) & (0x20000ULL)) != 0) goto loc_00234188;
loc_00233D9B:
    if ((*(unsigned int *)(v_rip + 14233254)) != 0) goto loc_00233E9F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_00233DCF;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)) & (0x1000ULL)) != 0) goto loc_00233E8F;
loc_00233DCF:
loc_00233DD2:
    a3 = 0;
    *(unsigned __int16 *)(a1 + 58 * 1) = 1;
    *(unsigned __int64 *)(a1 + 48) = v_rbp;
    *(unsigned int *)(a1 + 60) = 0;
    result = KiComputeDueTime(a1, a2, a3, v_stack_m98);
    if ((unsigned int)(result) == 0) goto loc_00233E7F;
    *(unsigned int *)(a1 + 4) = 0;
    v_stack_mA8 = 0;
    result = KiInsertTimerTable(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, v_stack_m60, (unsigned int)(v_stack_m98));
    if ((unsigned __int8)(result) == 0) goto loc_00233E7F;
    if (((*(unsigned int *)(v_rip + 14232795)) & (0x20000ULL)) != 0) goto loc_002341CE;
loc_00233E3A:
    a4 = 0;
    v_stack_mA8 = (unsigned __int8)(v_stack_m58);
    a2 = 0;
    result = KiExitDispatcher(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, 1, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (144);
    return result;
loc_00233E7F:
    a3 = 0;
    result = KiTimerWaitTest(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, a3, a4);
    goto loc_00233E3A;
loc_00233E8F:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1532)) & (0x4000000ULL)) != 0) goto loc_00233DCF;
loc_00233E9F:
    goto loc_00233DD2;
loc_00233EA7:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m58), (unsigned __int8)(result), a3, a4);
    goto loc_00233C5A;
loc_00233EB8:
    *(unsigned int *)(v_stack_m58 + 28) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00233F99;
    v_r14 = (v_stack_m90 + 272) << (5);
    v_r14 = (v_r14) + (v_stack_m88 + 16640);
    v_r12 = 0;
loc_00233EE0:
    if (condition_is_above_or_equal) goto loc_00233F04;
loc_00233EE8:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14226362)) & ((unsigned int)(v_r12))) == 0) goto loc_002340EA;
loc_00233EF8:
loc_00233EFA:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_00233EE0;
    goto loc_00233EE8;
loc_00233F04:
loc_00233F13:
    if ((*(unsigned int *)(v_stack_m58 + 28)) != -1) goto loc_00233F5E;
    if ((*(unsigned int *)(v_stack_p50 + 28)) != -1) goto loc_00233F5E;
    result = (*(unsigned __int8 *)(v_stack_p40 + 208)) + (*(unsigned __int8 *)(v_stack_p40 + 208));
    if ((*(unsigned int *)(v_rip + 14225653)) == 0) goto loc_00234050;
    v_r11 = (v_stack_p38) >> (6);
    result = (unsigned int)(((unsigned int)(v_stack_p48)) & (63));
loc_00233F5E:
    goto loc_00233D6F;
loc_00233F70:
    v_rsi = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 14226228)) & ((unsigned int)(v_rsi))) == 0) goto loc_00234112;
loc_00233F7E:
loc_00233F80:
    if (sign_flag) goto loc_00233F70;
    if (condition_is_below) goto loc_00233F70;
    goto loc_00233C83;
loc_00233F99:
    v_r14 = (v_r11 + 16) << (5);
    v_r14 = (v_r14) + (v_stack_m88 + 16640);
    if (condition_is_above_or_equal) goto loc_00233FB0;
    goto loc_00233FB9;
loc_00233FB0:
    if (v_r14 != 0) goto loc_00233F13;
loc_00233FB9:
    v_rsi = 0;
loc_00233FC0:
    if (condition_is_above_or_equal) goto loc_00233FE2;
loc_00233FC8:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 14226140)) & ((unsigned int)(v_rsi))) == 0) goto loc_00234139;
loc_00233FD6:
loc_00233FD8:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_00233FC0;
    goto loc_00233FC8;
loc_00233FE2:
    v_rsi = (v_stack_p38) + (272);
    v_rsi = (v_rsi) << (5);
    v_rsi = (v_rsi) + (v_stack_p40 + 16640);
    v_r12 = 0;
loc_00234000:
    if (condition_is_above_or_equal) goto loc_00233F04;
loc_0023400C:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 14226070)) & ((unsigned int)(v_r12))) == 0) goto loc_00234160;
loc_0023401C:
loc_0023401E:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_00234000;
    goto loc_0023400C;
loc_00234028:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14232202)))) & (64)) == 0) goto loc_00233CE0;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rip - 2309937 + result * 8 + 16549160) + v_r11 * 8, v_stack_p40 + 16640, a3, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00233CE0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_p40 + 16640, a3, v_stack_p50);
    goto loc_00233CE2;
loc_00234050:
    v_r11 = (v_r11) << (6);
    a1 = ((unsigned int)((unsigned int)(v_r14))) + (v_r11);
    goto loc_00233D6F;
loc_0023406F:
    v_r14 = 0;
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 3)) & (63));
    if (0 != 0) goto loc_002341E1;
    if (!sign_flag) goto loc_00233C75;
loc_002340B4:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14225904)) & ((unsigned int)(v_rsi))) == 0) goto loc_002340CE;
loc_002340BE:
loc_002340C0:
    if (!sign_flag) goto loc_00233C6E;
    goto loc_002340B4;
loc_002340CE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14232036)))) & (64)) == 0) goto loc_002340BE;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_002340BE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_002340C0;
loc_002340EA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14232008)))) & (64)) == 0) goto loc_00233EF8;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00233EF8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233EFA;
loc_00234112:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14231968)))) & (64)) == 0) goto loc_00233F7E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00233F7E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233F80;
loc_00234139:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14231929)))) & (64)) == 0) goto loc_00233FD6;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_00233FD6;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233FD8;
loc_00234160:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14231890)))) & (64)) == 0) goto loc_0023401C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((unsigned __int8)(result) == 0) goto loc_0023401C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_0023401E;
loc_00234188:
    if ((unsigned __int8)(v_r12) == 0) goto loc_00233D9B;
    v_stack_p58 = a1;
    v_stack_p70 = v_stack_p58;
    v_stack_p78 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p70, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    goto loc_00233D9B;
loc_002341CE:
    a3 = 0;
    result = KiTraceSetTimer(a1, 0, a3, (unsigned int)(0xF55ULL));
    goto loc_00233E3A;
loc_002341E1:
    goto loc_00233D86;
}
```

## 5. (Beta) C Style

```c
int64_t KeSetTimer(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0xBD6B42)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rbp = (Arg3) ^ (*(uint64_t *)(v_rip + 0xD93636));
    local_rbp = (local_rbp) ^ (Arg1);
    v_stack_m60 = Arg3;
    v_stack_m98 = 0;
    local_rbp = (local_rbp) ^ (*(uint64_t *)(v_rip + 0xD93368));
    v_stack_m58 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD930CC)) != 0) goto loc_00233EA7;
loc_00233C5A:
    local_r14 = 0;
    v_stack_m70 = 0;
    local_r12 = 0;
loc_00233C6E:
loc_00233C75:
    if (condition_is_below) goto loc_00233F70;
loc_00233C83:
    if (((*(uint8_t *)(arg1 + 0x3)) & (192)) == 0) goto loc_00233D86;
    v_stack_m80 = (uint32_t)(*(uint8_t *)(arg1 + 0x2));
    v_stack_m90 = *(uint8_t *)(arg1 + 0x2);
    result = (*(uint16_t *)(arg1 + 0x3A)) << (8);
    local_rsi = (*(uint8_t *)(arg1 + 0x2) + 16) + (result);
    v_stack_m88 = *(uint64_t *)(v_rip - 0x233C75 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip - 0x233C75 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40) + 16640);
loc_00233CC8:
    if (condition_is_above_or_equal) goto loc_00233CEC;
loc_00233CD0:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD915D2)) & ((uint32_t)(local_r14))) == 0) goto loc_00234028;
loc_00233CE0:
loc_00233CE2:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00233CC8;
    goto loc_00233CD0;
loc_00233CEC:
    if (sign_flag) goto loc_0023406F;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) << (8);
    local_r13 = (v_stack_m90 + 16) + (result);
    local_r13 = (local_r13) << (5);
    local_r13 = (local_r13) + (v_stack_m88 + 16640);
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) ^ (1);
    result = (result) << (8);
    a4 = (v_stack_m90 + 16) + (result);
    a4 = (a4) << (5);
    a4 = (a4) + (v_stack_m88 + 16640);
    v_stack_m78 = a4;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (Arg1 + 32)) goto loc_00233D58;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8))) != (Arg1 + 32)) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(arg1 + 0x20 + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg1 + 0x20 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x20 + 0x8)) == Arg1) goto loc_00233EB8;
loc_00233D6F:
    local_r14 = 0;
loc_00233D86:
    if (((*(uint32_t *)(v_rip + 0xD92D78)) & (0x20000ULL)) != 0) goto loc_00234188;
loc_00233D9B:
    if ((*(uint32_t *)(v_rip + 0xD92EA6)) != 0) goto loc_00233E9F;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_00233DCF;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)) & (0x1000ULL)) != 0) goto loc_00233E8F;
loc_00233DCF:
loc_00233DD2:
    Arg3 = 0;
    *(uint16_t *)(arg1 + 0x3A * 1) = 1;
    *(uint64_t *)(arg1 + 0x30) = local_rbp;
    *(uint32_t *)(arg1 + 0x3C) = 0;
    result = KiComputeDueTime(Arg1, Arg2, Arg3, v_stack_m98);
    if ((uint32_t)(result) == 0) goto loc_00233E7F;
    *(uint32_t *)(arg1 + 0x4) = 0;
    v_stack_mA8 = 0;
    result = KiInsertTimerTable(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, v_stack_m60, (uint32_t)(v_stack_m98));
    if ((uint8_t)(result) == 0) goto loc_00233E7F;
    if (((*(uint32_t *)(v_rip + 0xD92CDB)) & (0x20000ULL)) != 0) goto loc_002341CE;
loc_00233E3A:
    a4 = 0;
    v_stack_mA8 = (uint8_t)(v_stack_m58);
    Arg2 = 0;
    result = KiExitDispatcher(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, 1, a4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, a4);
    local_rsp = (local_rsp) + (144);
    return result;
loc_00233E7F:
    Arg3 = 0;
    result = KiTimerWaitTest(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, Arg3, a4);
    goto loc_00233E3A;
loc_00233E8F:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x5FC)) & (0x4000000ULL)) != 0) goto loc_00233DCF;
loc_00233E9F:
    goto loc_00233DD2;
loc_00233EA7:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m58), (uint8_t)(result), Arg3, a4);
    goto loc_00233C5A;
loc_00233EB8:
    *(uint32_t *)(v_stack_m58 + 0x1C) = 0xFFFFFFFFULL;
    if (0 != 0) goto loc_00233F99;
    local_r14 = (v_stack_m90 + 272) << (5);
    local_r14 = (local_r14) + (v_stack_m88 + 16640);
    local_r12 = 0;
loc_00233EE0:
    if (condition_is_above_or_equal) goto loc_00233F04;
loc_00233EE8:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD913BA)) & ((uint32_t)(local_r12))) == 0) goto loc_002340EA;
loc_00233EF8:
loc_00233EFA:
    if (*(uint64_t *)(local_r14) == 0) goto loc_00233EE0;
    goto loc_00233EE8;
loc_00233F04:
loc_00233F13:
    if ((*(uint32_t *)(v_stack_m58 + 0x1C)) != -1) goto loc_00233F5E;
    if ((*(uint32_t *)(v_stack_p50 + 0x1C)) != -1) goto loc_00233F5E;
    result = (*(uint8_t *)(v_stack_p40 + 0xD0)) + (*(uint8_t *)(v_stack_p40 + 0xD0));
    if ((*(uint32_t *)(v_rip + 0xD910F5)) == 0) goto loc_00234050;
    local_r11 = (v_stack_p38) >> (6);
    result = (uint32_t)(((uint32_t)(v_stack_p48)) & (63));
loc_00233F5E:
    goto loc_00233D6F;
loc_00233F70:
    local_rsi = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xD91334)) & ((uint32_t)(local_rsi))) == 0) goto loc_00234112;
loc_00233F7E:
loc_00233F80:
    if (sign_flag) goto loc_00233F70;
    if (condition_is_below) goto loc_00233F70;
    goto loc_00233C83;
loc_00233F99:
    local_r14 = (local_r11 + 16) << (5);
    local_r14 = (local_r14) + (v_stack_m88 + 16640);
    if (condition_is_above_or_equal) goto loc_00233FB0;
    goto loc_00233FB9;
loc_00233FB0:
    if (local_r14 != 0) goto loc_00233F13;
loc_00233FB9:
    local_rsi = 0;
loc_00233FC0:
    if (condition_is_above_or_equal) goto loc_00233FE2;
loc_00233FC8:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD912DC)) & ((uint32_t)(local_rsi))) == 0) goto loc_00234139;
loc_00233FD6:
loc_00233FD8:
    if (*(uint64_t *)(local_r14) == 0) goto loc_00233FC0;
    goto loc_00233FC8;
loc_00233FE2:
    local_rsi = (v_stack_p38) + (272);
    local_rsi = (local_rsi) << (5);
    local_rsi = (local_rsi) + (v_stack_p40 + 16640);
    local_r12 = 0;
loc_00234000:
    if (condition_is_above_or_equal) goto loc_00233F04;
loc_0023400C:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD91296)) & ((uint32_t)(local_r12))) == 0) goto loc_00234160;
loc_0023401C:
loc_0023401E:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_00234000;
    goto loc_0023400C;
loc_00234028:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD92A8A)))) & (64)) == 0) goto loc_00233CE0;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_rip - 0x233F31 + result * 8 + 0xFC8528) + local_r11 * 8, v_stack_p40 + 16640, Arg3, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00233CE0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_p40 + 16640, Arg3, v_stack_p50);
    goto loc_00233CE2;
loc_00234050:
    local_r11 = (local_r11) << (6);
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) + (local_r11);
    goto loc_00233D6F;
loc_0023406F:
    local_r14 = 0;
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x3)) & (63));
    if (0 != 0) goto loc_002341E1;
    if (!sign_flag) goto loc_00233C75;
loc_002340B4:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD911F0)) & ((uint32_t)(local_rsi))) == 0) goto loc_002340CE;
loc_002340BE:
loc_002340C0:
    if (!sign_flag) goto loc_00233C6E;
    goto loc_002340B4;
loc_002340CE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD929E4)))) & (64)) == 0) goto loc_002340BE;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_002340BE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_002340C0;
loc_002340EA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD929C8)))) & (64)) == 0) goto loc_00233EF8;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00233EF8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233EFA;
loc_00234112:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD929A0)))) & (64)) == 0) goto loc_00233F7E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00233F7E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233F80;
loc_00234139:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD92979)))) & (64)) == 0) goto loc_00233FD6;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_00233FD6;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_00233FD8;
loc_00234160:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD92952)))) & (64)) == 0) goto loc_0023401C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    if ((uint8_t)(result) == 0) goto loc_0023401C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), v_rip - 2310313, v_stack_p40, v_stack_p50);
    goto loc_0023401E;
loc_00234188:
    if ((uint8_t)(local_r12) == 0) goto loc_00233D9B;
    v_stack_p58 = Arg1;
    v_stack_p70 = v_stack_p58;
    v_stack_p78 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p70, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    goto loc_00233D9B;
loc_002341CE:
    Arg3 = 0;
    result = KiTraceSetTimer(Arg1, 0, Arg3, (uint32_t)(0xF55ULL));
    goto loc_00233E3A;
loc_002341E1:
    goto loc_00233D86;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `16` | `W` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `16` | `R` |
| `Arg1` | `+ 0x3A` | `16` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00233BE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
