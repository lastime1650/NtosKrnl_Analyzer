# AlpcpQueueIoCompletion

- RVA: `0x00397480`–`0x00397900` (길이 `1,152` bytes)
- VA: `0x0000000140397480`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081384`
- 디코드: `265`개 명령, `1,152/1,152` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00397576` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0039761B` → [KiRemovePrcbWaitEntry](../25/KiRemovePrcbWaitEntry_function_002502D0.md) (function, `0x002502D0`)
- `0x003976CE` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (function, `0x009DA2E0`)
- `0x0039776D` → [KiWakeOtherQueueWaiters](KiWakeOtherQueueWaiters_function_003964D0.md) (function, `0x003964D0`)
- `0x003977B5` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00397806` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039782E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039783D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0039784A` → [KeIsThreadRunning](KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x00397859` → [EtwTraceEnqueueWork](EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)
- `0x0039789F` → [KiCompleteDirectSwitchThread](../3F/KiCompleteDirectSwitchThread_function_003FFE1C.md) (function, `0x003FFE1C`)

### Direct callers
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F9A6B`
- [AlpcpSignal](AlpcpSignal_function_003955E0.md) at `0x00396011`
- [AlpcpQueueIoCompletionPort](../3F/AlpcpQueueIoCompletionPort_function_003FF760.md) at `0x003FFA7B`
- [AlpcpLookasidePacketCallbackRoutine](../41/AlpcpLookasidePacketCallbackRoutine_function_00419D50.md) at `0x00419F6B`

### Static image references
- `0x00397502` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00397518` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0039770F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00397820` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003976CE` → [IopAllocateMiniCompletionPacket](../../page/9D/IopAllocateMiniCompletionPacket_function_009DA2E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00397480  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00397485  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0039748A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0039748F  57                              push rdi
00397490  41 54                           push r12
00397492  41 55                           push r13
00397494  41 56                           push r14
00397496  41 57                           push r15
00397498  48 83 EC 40                     sub rsp, 0x40
0039749C  45 33 F6                        xor r14d, r14d
0039749F  4D 8B E1                        mov r12, r9
003974A2  41 8B C6                        mov eax, r14d
003974A5  49 8B D8                        mov rbx, r8
003974A8  38 84 24 90 00 00 00            cmp byte ptr [rsp + 0x90], al
003974AF  48 8B FA                        mov rdi, rdx
003974B2  4C 8B F9                        mov r15, rcx
003974B5  0F 95 C0                        setne al
003974B8  8B F0                           mov esi, eax
003974BA  83 CE 04                        or esi, 4
003974BD  44 39 B4 24 98 00 00 00         cmp dword ptr [rsp + 0x98], r14d
003974C5  0F 44 F0                        cmove esi, eax
003974C8  89 B4 24 90 00 00 00            mov dword ptr [rsp + 0x90], esi
003974CF  4D 85 C9                        test r9, r9
003974D2  0F 84 F2 01 00 00               je 0x1403976ca
003974D8  49 89 7C 24 18                  mov qword ptr [r12 + 0x18], rdi
003974DD  49 8D 6F 08                     lea rbp, [r15 + 8]
003974E1  49 89 5C 24 20                  mov qword ptr [r12 + 0x20], rbx
003974E6  45 89 74 24 28                  mov dword ptr [r12 + 0x28], r14d
003974EB  4D 89 74 24 30                  mov qword ptr [r12 + 0x30], r14
003974F0  44 0F 20 C0                     mov rax, cr8
003974F4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003974F9  B9 02 00 00 00                  mov ecx, 2
003974FE  44 0F 22 C1                     mov cr8, rcx
00397502  44 39 35 17 F8 C2 00            cmp dword ptr [rip + 0xc2f817], r14d
00397509  0F 85 F1 02 00 00               jne 0x140397800
0039750F  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00397518  8B 05 E6 F5 C2 00               mov eax, dword ptr [rip + 0xc2f5e6]
0039751E  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
00397526  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
0039752A  0F BA E0 18                     bt eax, 0x18
0039752E  0F 82 13 03 00 00               jb 0x140397847
00397534  41 0F B6 47 01                  movzx eax, byte ptr [r15 + 1]
00397539  F6 D0                           not al
0039753B  D1 E8                           shr eax, 1
0039753D  83 E0 01                        and eax, 1
00397540  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
00397547  48 8B 83 50 06 00 00            mov rax, qword ptr [rbx + 0x650]
0039754E  48 85 C0                        test rax, rax
00397551  48 0F 44 C3                     cmove rax, rbx
00397555  85 F6                           test esi, esi
00397557  74 17                           je 0x140397570
00397559  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
00397560  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
00397566  0F BA E0 0D                     bt eax, 0xd
0039756A  0F 82 18 03 00 00               jb 0x140397888
00397570  40 32 FF                        xor dil, dil
00397573  49 8B CF                        mov rcx, r15
00397576  E8 15 A7 EB FF                  call 0x140251c90
0039757B  48 39 6D 00                     cmp qword ptr [rbp], rbp
0039757F  0F 84 AC 01 00 00               je 0x140397731
00397585  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00397589  41 3B 47 2C                     cmp eax, dword ptr [r15 + 0x2c]
0039758D  0F 83 95 01 00 00               jae 0x140397728
00397593  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
0039759A  49 3B C7                        cmp rax, r15
0039759D  0F 84 D3 02 00 00               je 0x140397876
003975A3  48 8B 75 00                     mov rsi, qword ptr [rbp]
003975A7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003975B0  48 8B FE                        mov rdi, rsi
003975B3  48 8B 36                        mov rsi, qword ptr [rsi]
003975B6  80 7F 10 03                     cmp byte ptr [rdi + 0x10], 3
003975BA  0F 85 F0 00 00 00               jne 0x1403976b0
003975C0  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003975C4  48 39 7E 08                     cmp qword ptr [rsi + 8], rdi
003975C8  75 09                           jne 0x1403975d3
003975CA  48 39 38                        cmp qword ptr [rax], rdi
003975CD  0F 84 11 01 00 00               je 0x1403976e4
003975D3  B9 03 00 00 00                  mov ecx, 3
003975D8  CD 29                           int 0x29
003975DA  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
003975E1  3C 05                           cmp al, 5
003975E3  0F 85 A4 00 00 00               jne 0x14039768d
003975E9  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
003975ED  8B C1                           mov eax, ecx
003975EF  83 E0 07                        and eax, 7
003975F2  83 F8 01                        cmp eax, 1
003975F5  0F 85 B3 02 00 00               jne 0x1403978ae
003975FB  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
00397602  48 85 D2                        test rdx, rdx
00397605  74 11                           je 0x140397618
00397607  0F B6 02                        movzx eax, byte ptr [rdx]
0039760A  24 7F                           and al, 0x7f
0039760C  3C 15                           cmp al, 0x15
0039760E  0F 84 D0 01 00 00               je 0x1403977e4
00397614  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00397618  48 8B CB                        mov rcx, rbx
0039761B  E8 B0 8C EB FF                  call 0x1402502d0
00397620  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
00397627  3C 01                           cmp al, 1
00397629  0F 84 3E 02 00 00               je 0x14039786d
0039762F  3C 05                           cmp al, 5
00397631  75 22                           jne 0x140397655
00397633  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0039763D  8B 08                           mov ecx, dword ptr [rax]
0039763F  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
00397645  44 38 AB 87 01 00 00            cmp byte ptr [rbx + 0x187], r13b
0039764C  74 73                           je 0x1403976c1
0039764E  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
00397655  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0039765D  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00397664  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
0039766B  48 8B 82 08 2D 00 00            mov rax, qword ptr [rdx + 0x2d08]
00397672  48 89 01                        mov qword ptr [rcx], rax
00397675  48 89 8A 08 2D 00 00            mov qword ptr [rdx + 0x2d08], rcx
0039767C  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
00397683  4C 89 B3 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r14
0039768A  41 B5 01                        mov r13b, 1
0039768D  4C 89 73 40                     mov qword ptr [rbx + 0x40], r14
00397691  0F B6 47 11                     movzx eax, byte ptr [rdi + 0x11]
00397695  FE C0                           inc al
00397697  88 47 11                        mov byte ptr [rdi + 0x11], al
0039769A  45 84 ED                        test r13b, r13b
0039769D  0F 85 6D 01 00 00               jne 0x140397810
003976A3  49 8D 6F 08                     lea rbp, [r15 + 8]
003976A7  48 3B F5                        cmp rsi, rbp
003976AA  0F 85 00 FF FF FF               jne 0x1403975b0
003976B0  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003976B7  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
003976BF  EB 70                           jmp 0x140397731
003976C1  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
003976C8  EB 8B                           jmp 0x140397655
003976CA  33 D2                           xor edx, edx
003976CC  B1 01                           mov cl, 1
003976CE  E8 0D 2C 64 00                  call 0x1409da2e0
003976D3  4C 8B E0                        mov r12, rax
003976D6  48 85 C0                        test rax, rax
003976D9  0F 85 F9 FD FF FF               jne 0x1403974d8
003976DF  E9 DC 00 00 00                  jmp 0x1403977c0
003976E4  48 89 30                        mov qword ptr [rax], rsi
003976E7  45 32 ED                        xor r13b, r13b
003976EA  48 89 46 08                     mov qword ptr [rsi + 8], rax
003976EE  41 8B EE                        mov ebp, r14d
003976F1  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
003976F5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00397700  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
00397707  0F 83 CD FE FF FF               jae 0x1403975da
0039770D  FF C5                           inc ebp
0039770F  85 2D 97 DB C2 00               test dword ptr [rip + 0xc2db97], ebp
00397715  0F 84 05 01 00 00               je 0x140397820
0039771B  F3 90                           pause
0039771D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00397721  48 85 C0                        test rax, rax
00397724  74 DA                           je 0x140397700
00397726  EB E5                           jmp 0x14039770d
00397728  40 84 FF                        test dil, dil
0039772B  0F 85 62 FE FF FF               jne 0x140397593
00397731  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
00397735  8D 41 01                        lea eax, [rcx + 1]
00397738  41 89 47 04                     mov dword ptr [r15 + 4], eax
0039773C  49 8D 47 18                     lea rax, [r15 + 0x18]
00397740  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00397744  48 39 02                        cmp qword ptr [rdx], rax
00397747  0F 85 86 FE FF FF               jne 0x1403975d3
0039774D  49 89 04 24                     mov qword ptr [r12], rax
00397751  49 89 54 24 08                  mov qword ptr [r12 + 8], rdx
00397756  4C 89 22                        mov qword ptr [rdx], r12
00397759  4C 89 60 08                     mov qword ptr [rax + 8], r12
0039775D  85 C9                           test ecx, ecx
0039775F  75 11                           jne 0x140397772
00397761  48 39 6D 00                     cmp qword ptr [rbp], rbp
00397765  74 0B                           je 0x140397772
00397767  49 8B D7                        mov rdx, r15
0039776A  49 8B CD                        mov rcx, r13
0039776D  E8 5E ED FF FF                  call 0x1403964d0
00397772  F0 41 81 27 7F FF FF FF         lock and dword ptr [r15], 0xffffff7f
0039777A  40 F6 C6 01                     test sil, 1
0039777E  0F 85 DF 00 00 00               jne 0x140397863
00397784  41 8B CE                        mov ecx, r14d
00397787  40 F6 C6 04                     test sil, 4
0039778B  0F 85 FF 00 00 00               jne 0x140397890
00397791  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00397799  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0039779E  8B D1                           mov edx, ecx
003977A0  44 8B 8C 24 98 00 00 00         mov r9d, dword ptr [rsp + 0x98]
003977A8  48 8B CB                        mov rcx, rbx
003977AB  41 B8 01 00 00 00               mov r8d, 1
003977B1  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003977B5  E8 36 A5 EB FF                  call 0x140251cf0
003977BA  41 BE 01 00 00 00               mov r14d, 1
003977C0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
003977C5  41 8B C6                        mov eax, r14d
003977C8  48 8B 6C 24 78                  mov rbp, qword ptr [rsp + 0x78]
003977CD  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
003977D5  48 83 C4 40                     add rsp, 0x40
003977D9  41 5F                           pop r15
003977DB  41 5E                           pop r14
003977DD  41 5D                           pop r13
003977DF  41 5C                           pop r12
003977E1  5F                              pop rdi
003977E2  C3                              ret
003977E3  CC                              int3
003977E4  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
003977EA  0F B6 C0                        movzx eax, al
003977ED  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
003977F3  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
003977FB  E9 18 FE FF FF                  jmp 0x140397618
00397800  0F B6 D1                        movzx edx, cl
00397803  0F B6 C8                        movzx ecx, al
00397806  E8 F1 DE 15 00                  call 0x1404f56fc
0039780B  E9 FF FC FF FF                  jmp 0x14039750f
00397810  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
00397817  4D 89 34 24                     mov qword ptr [r12], r14
0039781B  E9 52 FF FF FF                  jmp 0x140397772
00397820  8B 05 92 F2 C2 00               mov eax, dword ptr [rip + 0xc2f292]
00397826  A8 40                           test al, 0x40
00397828  0F 84 ED FE FF FF               je 0x14039771b
0039782E  E8 5D 7C F7 FF                  call 0x14030f490
00397833  84 C0                           test al, al
00397835  0F 84 E0 FE FF FF               je 0x14039771b
0039783B  8B CD                           mov ecx, ebp
0039783D  E8 1E 7C F7 FF                  call 0x14030f460
00397842  E9 D6 FE FF FF                  jmp 0x14039771d
00397847  48 8B CB                        mov rcx, rbx
0039784A  E8 D1 EE FF FF                  call 0x140396720
0039784F  44 0F B6 C0                     movzx r8d, al
00397853  48 8B CB                        mov rcx, rbx
00397856  49 8B D4                        mov rdx, r12
00397859  E8 EE EE FF FF                  call 0x14039674c
0039785E  E9 D1 FC FF FF                  jmp 0x140397534
00397863  B9 03 00 00 00                  mov ecx, 3
00397868  E9 24 FF FF FF                  jmp 0x140397791
0039786D  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
00397871  E9 DF FD FF FF                  jmp 0x140397655
00397876  80 BB 83 02 00 00 0F            cmp byte ptr [rbx + 0x283], 0xf
0039787D  0F 85 20 FD FF FF               jne 0x1403975a3
00397883  E9 A9 FE FF FF                  jmp 0x140397731
00397888  40 B7 01                        mov dil, 1
0039788B  E9 E3 FC FF FF                  jmp 0x140397573
00397890  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00397898  48 8B CB                        mov rcx, rbx
0039789B  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0039789F  E8 78 85 06 00                  call 0x1403ffe1c
003978A4  B9 06 00 00 00                  mov ecx, 6
003978A9  E9 EB FE FF FF                  jmp 0x140397799
003978AE  83 F8 04                        cmp eax, 4
003978B1  0F 84 44 FD FF FF               je 0x1403975fb
003978B7  85 C0                           test eax, eax
003978B9  75 20                           jne 0x1403978db
003978BB  80 E1 FA                        and cl, 0xfa
003978BE  80 C9 02                        or cl, 2
003978C1  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003978C4  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
003978CB  4C 89 B3 D0 03 00 00            mov qword ptr [rbx + 0x3d0], r14
003978D2  44 88 77 11                     mov byte ptr [rdi + 0x11], r14b
003978D6  E9 AF FD FF FF                  jmp 0x14039768a
003978DB  83 F8 05                        cmp eax, 5
003978DE  75 0E                           jne 0x1403978ee
003978E0  80 E1 FE                        and cl, 0xfe
003978E3  80 C9 06                        or cl, 6
003978E6  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003978E9  E9 9F FD FF FF                  jmp 0x14039768d
003978EE  83 F8 03                        cmp eax, 3
003978F1  0F 85 96 FD FF FF               jne 0x14039768d
003978F7  C6 47 11 02                     mov byte ptr [rdi + 0x11], 2
003978FB  E9 8D FD FF FF                  jmp 0x14039768d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpQueueIoCompletion(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_r14 = 0;
    result = (a5 != 0) ? 1 : 0;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) | (4));
    if (a6 == 0) { v_rsi = (unsigned int)(result); }
    v_stack_p28 = (unsigned int)(v_rsi);
    if (a4 == 0) goto loc_003976CA;
loc_003974D8:
    *(unsigned __int64 *)(a4 + 24) = a2;
    *(unsigned __int64 *)(a4 + 32) = a3;
    *(unsigned int *)(a4 + 40) = 0;
    *(unsigned __int64 *)(a4 + 48) = 0;
    v_stack_m38 = v_cr8;
    if ((*(unsigned int *)(v_rip + 12777495)) != 0) goto loc_00397800;
loc_0039750F:
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned int *)(v_rip + 12777495)) < 0) goto loc_00397847;
loc_00397534:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(a1 + 1)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) & (1));
    v_stack_p30 = (unsigned int)(result);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 1616) == 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8); }
    if ((unsigned int)(v_rsi) == 0) goto loc_00397570;
    if (condition_is_below) goto loc_00397888;
loc_00397570:
    v_rdi = 0;
loc_00397573:
    result = KiAcquireKobjectLockSafe(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 8)) == (a1 + 8)) goto loc_00397731;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) >= (*(unsigned int *)(a1 + 44))) goto loc_00397728;
loc_00397593:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232)) == a1) goto loc_00397876;
loc_003975A3:
loc_003975B0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16)) != 3) goto loc_003976B0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 8)) != (*(unsigned __int64 *)(a1 + 8))) goto loc_003975D3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 8))) goto loc_003976E4;
loc_003975D3:
loc_003975DA:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_0039768D;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_003978AE;
loc_003975FB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232) == 0) goto loc_00397618;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_003977E4;
loc_00397618:
    result = KiRemovePrcbWaitEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 232), a3, a4);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) == 1) goto loc_0039786D;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388))) != 5) goto loc_00397655;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 391)) == ((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))))) goto loc_003976C1;
loc_00397655:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216) = *(unsigned __int64 *)(v_stack_p20 + 11528);
    *(unsigned __int64 *)(v_stack_p20 + 11528) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 200) = a4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 976) = 0;
loc_0039768A:
loc_0039768D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 64) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 17) = (unsigned __int8)(result);
    if (1 != 0) goto loc_00397810;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != (a1 + 8)) goto loc_003975B0;
loc_003976B0:
    goto loc_00397731;
loc_003976C1:
    goto loc_00397655;
loc_003976CA:
    a2 = 0;
    result = IopAllocateMiniCompletionPacket(1, a2, a3, a4);
    if (result != 0) goto loc_003974D8;
    goto loc_003977C0;
loc_003976E4:
    *(unsigned __int64 *)(result) = (unsigned int)(a5);
    v_r13 = 0;
    *(unsigned __int64 *)((unsigned int)(a5) + 8) = result;
loc_00397700:
    if (condition_is_above_or_equal) goto loc_003975DA;
loc_0039770D:
    v_rbp = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12770199)) & ((unsigned int)(v_rbp))) == 0) goto loc_00397820;
loc_0039771B:
loc_0039771D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24) + 64) == 0) goto loc_00397700;
    goto loc_0039770D;
loc_00397728:
    if ((unsigned __int8)(*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_00397593;
loc_00397731:
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) != (a1 + 24)) goto loc_003975D3;
    *(unsigned __int64 *)(result) = a1 + 24;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8)) = result;
    *(unsigned __int64 *)(a1 + 24 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) goto loc_00397772;
    result = a1 + 24;
    if ((*(unsigned __int64 *)(v_rbp)) != v_rbp) {
        a2 = a1;
        a1 = 0;
        result = KiWakeOtherQueueWaiters(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(a5))) & (1)) != 0) goto loc_00397863;
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) != 0) goto loc_00397890;
loc_00397791:
loc_00397799:
    v_stack_m48 = (unsigned __int8)(v_stack_m38);
    result = KiExitDispatcher(v_stack_p20, 0, 1, (unsigned int)(a6));
loc_003977C0:
    v_rsp = (v_rsp) + (64);
    return 1;
loc_003977E4:
    *(unsigned int *)(v_stack_p8 + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540))));
    goto loc_00397618;
loc_00397800:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540)))), (unsigned __int8)(v_stack_p20), 1, (unsigned int)(a6));
    goto loc_0039750F;
loc_00397810:
    *(unsigned __int64 *)(result) = 1;
    goto loc_00397772;
loc_00397820:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12776082)))) & (64)) == 0) goto loc_0039771B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540)))), (unsigned __int8)(v_stack_p20), 1, (unsigned int)(a6));
    if ((unsigned __int8)(result) == 0) goto loc_0039771B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p10)), (unsigned __int8)(v_stack_p20), 1, (unsigned int)(a6));
    goto loc_0039771D;
loc_00397847:
    result = KeIsThreadRunning(v_stack_p8, (unsigned __int8)(v_stack_p20), 1, (unsigned int)(a6));
    result = EtwTraceEnqueueWork(v_stack_p8, result, (unsigned __int8)(result), (unsigned int)(a6));
    goto loc_00397534;
loc_00397863:
    goto loc_00397791;
loc_0039786D:
    goto loc_00397655;
loc_00397876:
    if ((*(unsigned __int8 *)(v_stack_p8 + 643)) != 15) goto loc_003975A3;
    goto loc_00397731;
loc_00397888:
    goto loc_00397573;
loc_00397890:
    result = KiCompleteDirectSwitchThread(v_stack_p88, *(unsigned __int64 *)(v_stack_p88 + 8), (unsigned __int8)(result), (unsigned int)(a6));
    goto loc_00397799;
loc_003978AE:
    if (((unsigned int)(result)) == 4) goto loc_003975FB;
    if ((unsigned int)(result) != 0) goto loc_003978DB;
    a1 = (unsigned __int8)((6) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p88 + 112) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_stack_p88 + 200) = result;
    *(unsigned __int64 *)(v_stack_p88 + 976) = 1;
    *(unsigned __int8 *)(1 + 17) = 1;
    goto loc_0039768A;
loc_003978DB:
    if (((unsigned int)(result)) != 5) goto loc_003978EE;
    a1 = (unsigned __int8)((a1) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_p88 + 112) = (unsigned __int8)(a1);
    goto loc_0039768D;
loc_003978EE:
    if (((unsigned int)(result)) != 3) goto loc_0039768D;
    *(unsigned __int8 *)(1 + 17) = 2;
    goto loc_0039768D;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpQueueIoCompletion(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint8_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_r14 = 0;
    result = (Arg5 != 0) ? 1 : 0;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) | (4));
    if (Arg6 == 0) { local_rsi = (uint32_t)(result); }
    v_stack_p28 = (uint32_t)(local_rsi);
    if (Arg4 == 0) goto loc_003976CA;
loc_003974D8:
    *(uint64_t *)(Arg4 + 0x18) = Arg2;
    *(uint64_t *)(Arg4 + 0x20) = Arg3;
    *(uint32_t *)(Arg4 + 0x28) = 0;
    *(uint64_t *)(Arg4 + 0x30) = 0;
    v_stack_m38 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC2F817)) != 0) goto loc_00397800;
loc_0039750F:
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint32_t *)(v_rip + 0xC2F817)) < 0) goto loc_00397847;
loc_00397534:
    result = (uint8_t)(~(*(uint8_t *)(arg1 + 0x1)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) & (1));
    v_stack_p30 = (uint32_t)(result);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x650) == 0) { result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8); }
    if ((uint32_t)(local_rsi) == 0) goto loc_00397570;
    if (condition_is_below) goto loc_00397888;
loc_00397570:
    local_rdi = 0;
loc_00397573:
    result = KiAcquireKobjectLockSafe(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x8)) == (Arg1 + 8)) goto loc_00397731;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) >= (*(uint32_t *)(arg1 + 0x2C))) goto loc_00397728;
loc_00397593:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8)) == Arg1) goto loc_00397876;
loc_003975A3:
loc_003975B0:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) != 3) goto loc_003976B0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x8))) goto loc_003975D3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x8))) goto loc_003976E4;
loc_003975D3:
loc_003975DA:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_0039768D;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_003978AE;
loc_003975FB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8) == 0) goto loc_00397618;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_003977E4;
loc_00397618:
    result = KiRemovePrcbWaitEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xE8), Arg3, Arg4);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) == 1) goto loc_0039786D;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184))) != 5) goto loc_00397655;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x187)) == ((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))))) goto loc_003976C1;
loc_00397655:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xD8) = *(uint64_t *)(v_stack_p20 + 0x2D08);
    *(uint64_t *)(v_stack_p20 + 0x2D08) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 216;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0xC8) = Arg4;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x3D0) = 0;
loc_0039768A:
loc_0039768D:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x40) = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11)) + 1);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x11) = (uint8_t)(result);
    if (1 != 0) goto loc_00397810;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != (Arg1 + 8)) goto loc_003975B0;
loc_003976B0:
    goto loc_00397731;
loc_003976C1:
    goto loc_00397655;
loc_003976CA:
    Arg2 = 0;
    result = IopAllocateMiniCompletionPacket(1, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_003974D8;
    goto loc_003977C0;
loc_003976E4:
    *(uint64_t *)(result) = (uint32_t)(Arg5);
    local_r13 = 0;
    *(uint64_t *)((uint32_t)(Arg5) + 0x8) = result;
loc_00397700:
    if (condition_is_above_or_equal) goto loc_003975DA;
loc_0039770D:
    local_rbp = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2DB97)) & ((uint32_t)(local_rbp))) == 0) goto loc_00397820;
loc_0039771B:
loc_0039771D:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) + 0x40) == 0) goto loc_00397700;
    goto loc_0039770D;
loc_00397728:
    if ((uint8_t)(*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_00397593;
loc_00397731:
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) != (Arg1 + 24)) goto loc_003975D3;
    *(void **)(result) = Arg1 + 24;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x18 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) goto loc_00397772;
    result = Arg1 + 24;
    if ((*(uint64_t *)(local_rbp)) != local_rbp) {
        Arg2 = Arg1;
        Arg1 = 0;
        result = KiWakeOtherQueueWaiters(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)(Arg5))) & (1)) != 0) goto loc_00397863;
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) != 0) goto loc_00397890;
loc_00397791:
loc_00397799:
    v_stack_m48 = (uint8_t)(v_stack_m38);
    result = KiExitDispatcher(v_stack_p20, 0, 1, (uint32_t)(Arg6));
loc_003977C0:
    local_rsp = (local_rsp) + (64);
    return 1;
loc_003977E4:
    *(uint32_t *)(v_stack_p8 + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C))));
    goto loc_00397618;
loc_00397800:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C)))), (uint8_t)(v_stack_p20), 1, (uint32_t)(Arg6));
    goto loc_0039750F;
loc_00397810:
    *(uint64_t *)(result) = 1;
    goto loc_00397772;
loc_00397820:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2F292)))) & (64)) == 0) goto loc_0039771B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C)))), (uint8_t)(v_stack_p20), 1, (uint32_t)(Arg6));
    if ((uint8_t)(result) == 0) goto loc_0039771B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p10)), (uint8_t)(v_stack_p20), 1, (uint32_t)(Arg6));
    goto loc_0039771D;
loc_00397847:
    result = KeIsThreadRunning(v_stack_p8, (uint8_t)(v_stack_p20), 1, (uint32_t)(Arg6));
    result = EtwTraceEnqueueWork(v_stack_p8, result, (uint8_t)(result), (uint32_t)(Arg6));
    goto loc_00397534;
loc_00397863:
    goto loc_00397791;
loc_0039786D:
    goto loc_00397655;
loc_00397876:
    if ((*(uint8_t *)(v_stack_p8 + 0x283)) != 15) goto loc_003975A3;
    goto loc_00397731;
loc_00397888:
    goto loc_00397573;
loc_00397890:
    result = KiCompleteDirectSwitchThread(v_stack_p88, *(uint64_t *)(v_stack_p88 + 0x8), (uint8_t)(result), (uint32_t)(Arg6));
    goto loc_00397799;
loc_003978AE:
    if (((uint32_t)(result)) == 4) goto loc_003975FB;
    if ((uint32_t)(result) != 0) goto loc_003978DB;
    Arg1 = (uint8_t)((6) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p88 + 0x70) = (uint8_t)(Arg1);
    *(uint64_t *)(v_stack_p88 + 0xC8) = result;
    *(uint64_t *)(v_stack_p88 + 0x3D0) = 1;
    *(uint8_t *)(1 + 0x11) = 1;
    goto loc_0039768A;
loc_003978DB:
    if (((uint32_t)(result)) != 5) goto loc_003978EE;
    Arg1 = (uint8_t)((Arg1) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_p88 + 0x70) = (uint8_t)(Arg1);
    goto loc_0039768D;
loc_003978EE:
    if (((uint32_t)(result)) != 3) goto loc_0039768D;
    *(uint8_t *)(1 + 0x11) = 2;
    goto loc_0039768D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00397480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
