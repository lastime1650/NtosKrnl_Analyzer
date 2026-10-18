# KiInsertTimerTable

- RVA: `0x00233400`–`0x002337CA` (길이 `970` bytes)
- VA: `0x0000000140233400`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000604F8`
- 디코드: `236`개 명령, `970/970` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002335C9` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002335D9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00233717` → [KiSendClockInterruptToTargetProcessor](KiSendClockInterruptToTargetProcessor_function_00234700.md) (function, `0x00234700`)
- `0x002337B3` → [KiRemoveEntryTimer](../40/KiRemoveEntryTimer_function_00401740.md) (function, `0x00401740`)

### Direct callers
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x0020396C`
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E1D2`
- [ExpSetTimerObject](ExpSetTimerObject_function_00231730.md) at `0x00231C93`
- [KiSetTimerEx](KiSetTimerEx_function_00232CB0.md) at `0x00232F08`
- [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) at `0x00233997`
- [KeSetTimer](KeSetTimer_function_00233BE0.md) at `0x00233E1A`
- [KiAdjustTimerDueTimes](../4E/KiAdjustTimerDueTimes_function_004E8CD4.md) at `0x004E8F21`

### Static image references
- `0x00233433` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x00233445` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0023349D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002334EA` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00233573` → RVA `0x00F231B8` (`.data`; read)
- `0x002335BB` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002336D9` → RVA `0x00FC6A85` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00233400  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00233405  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0023340A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0023340F  55                              push rbp
00233410  56                              push rsi
00233411  57                              push rdi
00233412  41 54                           push r12
00233414  41 55                           push r13
00233416  41 56                           push r14
00233418  41 57                           push r15
0023341A  48 83 EC 40                     sub rsp, 0x40
0023341E  33 ED                           xor ebp, ebp
00233420  45 8B D1                        mov r10d, r9d
00233423  4C 8B F2                        mov r14, rdx
00233426  4C 8B D9                        mov r11, rcx
00233429  8B DD                           mov ebx, ebp
0023342B  39 6A 3C                        cmp dword ptr [rdx + 0x3c], ebp
0023342E  75 03                           jne 0x140233433
00233430  89 6A 04                        mov dword ptr [rdx + 4], ebp
00233433  39 2D F7 1B D9 00               cmp dword ptr [rip + 0xd91bf7], ebp
00233439  8B D5                           mov edx, ebp
0023343B  0F 84 DF 00 00 00               je 0x140233520
00233441  4D 8B 6E 18                     mov r13, qword ptr [r14 + 0x18]
00233445  4C 8D 0D B4 CB DC FF            lea r9, [rip - 0x23344c]
0023344C  8B C2                           mov eax, edx
0023344E  49 8D 7A 10                     lea rdi, [r10 + 0x10]
00233452  66 41 89 56 38                  mov word ptr [r14 + 0x38], dx
00233457  44 8B FD                        mov r15d, ebp
0023345A  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0023345F  4D 8B 9C C1 40 8C FC 00         mov r11, qword ptr [r9 + rax*8 + 0xfc8c40]
00233467  41 0F B7 46 3A                  movzx eax, word ptr [r14 + 0x3a]
0023346C  48 C1 E0 08                     shl rax, 8
00233470  48 03 F8                        add rdi, rax
00233473  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00233478  49 8D 93 00 41 00 00            lea rdx, [r11 + 0x4100]
0023347F  48 C1 E7 05                     shl rdi, 5
00233483  48 03 FA                        add rdi, rdx
00233486  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0023348B  4C 8D 67 08                     lea r12, [rdi + 8]
0023348F  49 8B F4                        mov rsi, r12
00233492  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00233498  73 1C                           jae 0x1402334b6
0023349A  41 FF C7                        inc r15d
0023349D  44 85 3D 08 1E D9 00            test dword ptr [rip + 0xd91e08], r15d
002334A4  0F 84 11 01 00 00               je 0x1402335bb
002334AA  F3 90                           pause
002334AC  48 8B 07                        mov rax, qword ptr [rdi]
002334AF  48 85 C0                        test rax, rax
002334B2  74 DE                           je 0x140233492
002334B4  EB E4                           jmp 0x14023349a
002334B6  49 8B 14 24                     mov rdx, qword ptr [r12]
002334BA  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
002334BF  49 3B D4                        cmp rdx, r12
002334C2  74 55                           je 0x140233519
002334C4  4C 8B 42 F8                     mov r8, qword ptr [rdx - 8]
002334C8  4D 3B E8                        cmp r13, r8
002334CB  77 1D                           ja 0x1402334ea
002334CD  1B DB                           sbb ebx, ebx
002334CF  83 E3 02                        and ebx, 2
002334D2  48 8B 16                        mov rdx, qword ptr [rsi]
002334D5  49 8D 46 20                     lea rax, [r14 + 0x20]
002334D9  48 39 72 08                     cmp qword ptr [rdx + 8], rsi
002334DD  0F 84 00 01 00 00               je 0x1402335e3
002334E3  B9 03 00 00 00                  mov ecx, 3
002334E8  CD 29                           int 0x29
002334EA  8B 0D B0 35 D9 00               mov ecx, dword ptr [rip + 0xd935b0]
002334F0  49 8B C5                        mov rax, r13
002334F3  48 C1 E9 02                     shr rcx, 2
002334F7  49 2B C0                        sub rax, r8
002334FA  48 3B C1                        cmp rax, rcx
002334FD  0F 86 84 00 00 00               jbe 0x140233587
00233503  49 8B 74 24 08                  mov rsi, qword ptr [r12 + 8]
00233508  4C 3B 6E F8                     cmp r13, qword ptr [rsi - 8]
0023350C  73 C4                           jae 0x1402334d2
0023350E  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00233512  49 3B F4                        cmp rsi, r12
00233515  75 F1                           jne 0x140233508
00233517  EB B9                           jmp 0x1402334d2
00233519  BB 06 00 00 00                  mov ebx, 6
0023351E  EB B5                           jmp 0x1402334d5
00233520  4D 85 C0                        test r8, r8
00233523  0F 85 23 02 00 00               jne 0x14023374c
00233529  41 F6 43 23 10                  test byte ptr [r11 + 0x23], 0x10
0023352E  41 8B 53 24                     mov edx, dword ptr [r11 + 0x24]
00233532  0F 84 09 FF FF FF               je 0x140233441
00233538  49 8B 83 C0 00 00 00            mov rax, qword ptr [r11 + 0xc0]
0023353F  4C 8B 80 80 00 00 00            mov r8, qword ptr [rax + 0x80]
00233546  4C 23 40 50                     and r8, qword ptr [rax + 0x50]
0023354A  0F 84 F1 FE FF FF               je 0x140233441
00233550  41 0F B6 8B D1 00 00 00         movzx ecx, byte ptr [r11 + 0xd1]
00233558  41 0F B6 93 D0 00 00 00         movzx edx, byte ptr [r11 + 0xd0]
00233560  49 D3 C8                        ror r8, cl
00233563  49 0F BC C0                     bsf rax, r8
00233567  C1 E2 06                        shl edx, 6
0023356A  03 C8                           add ecx, eax
0023356C  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
00233573  48 8B 05 3E FC CE 00            mov rax, qword ptr [rip + 0xcefc3e]
0023357A  83 E1 3F                        and ecx, 0x3f
0023357D  03 D1                           add edx, ecx
0023357F  8B 14 90                        mov edx, dword ptr [rax + rdx*4]
00233582  E9 BA FE FF FF                  jmp 0x140233441
00233587  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0023358C  48 8B F2                        mov rsi, rdx
0023358F  48 3B D1                        cmp rdx, rcx
00233592  0F 84 3A FF FF FF               je 0x1402334d2
00233598  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002335A0  48 8B 06                        mov rax, qword ptr [rsi]
002335A3  4C 3B 68 F8                     cmp r13, qword ptr [rax - 8]
002335A7  0F 86 25 FF FF FF               jbe 0x1402334d2
002335AD  48 8B F0                        mov rsi, rax
002335B0  48 3B C1                        cmp rax, rcx
002335B3  0F 84 19 FF FF FF               je 0x1402334d2
002335B9  EB E5                           jmp 0x1402335a0
002335BB  8B 05 F7 34 D9 00               mov eax, dword ptr [rip + 0xd934f7]
002335C1  A8 40                           test al, 0x40
002335C3  0F 84 E1 FE FF FF               je 0x1402334aa
002335C9  E8 C2 BE 0D 00                  call 0x14030f490
002335CE  84 C0                           test al, al
002335D0  0F 84 D4 FE FF FF               je 0x1402334aa
002335D6  41 8B CF                        mov ecx, r15d
002335D9  E8 82 BE 0D 00                  call 0x14030f460
002335DE  E9 C9 FE FF FF                  jmp 0x1402334ac
002335E3  4C 8B 5C 24 20                  mov r11, qword ptr [rsp + 0x20]
002335E8  48 89 70 08                     mov qword ptr [rax + 8], rsi
002335EC  48 89 10                        mov qword ptr [rax], rdx
002335EF  48 89 42 08                     mov qword ptr [rdx + 8], rax
002335F3  48 89 06                        mov qword ptr [rsi], rax
002335F6  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
002335FE  F6 C3 02                        test bl, 2
00233601  75 40                           jne 0x140233643
00233603  40 32 FF                        xor dil, dil
00233606  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
0023360B  F0 48 83 20 00                  lock and qword ptr [rax], 0
00233610  83 FB 08                        cmp ebx, 8
00233613  0F 83 FA 00 00 00               jae 0x140233713
00233619  48 85 F6                        test rsi, rsi
0023361C  0F 85 71 01 00 00               jne 0x140233793
00233622  F6 D3                           not bl
00233624  80 E3 01                        and bl, 1
00233627  0F B6 C3                        movzx eax, bl
0023362A  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00233632  48 83 C4 40                     add rsp, 0x40
00233636  41 5F                           pop r15
00233638  41 5E                           pop r14
0023363A  41 5D                           pop r13
0023363C  41 5C                           pop r12
0023363E  5F                              pop rdi
0023363F  5E                              pop rsi
00233640  5D                              pop rbp
00233641  C3                              ret
00233642  CC                              int3
00233643  4C 89 6F 18                     mov qword ptr [rdi + 0x18], r13
00233647  F0 09 2C 24                     lock or dword ptr [rsp], ebp
0023364B  83 FB 04                        cmp ebx, 4
0023364E  0F 82 CD 00 00 00               jb 0x140233721
00233654  41 0F B6 83 D0 00 00 00         movzx eax, byte ptr [r11 + 0xd0]
0023365C  48 8D 0D 9D C9 DC FF            lea rcx, [rip - 0x233663]
00233663  48 03 C0                        add rax, rax
00233666  39 2D C4 19 D9 00               cmp dword ptr [rip + 0xd919c4], ebp
0023366C  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
00233674  0F 85 B4 00 00 00               jne 0x14023372e
0023367A  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0023367F  41 0F B6 83 D1 00 00 00         movzx eax, byte ptr [r11 + 0xd1]
00233687  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
0023368F  48 C1 E2 06                     shl rdx, 6
00233693  48 03 CA                        add rcx, rdx
00233696  F0 48 0F AB 01                  lock bts qword ptr [rcx], rax
0023369B  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
002336A5  48 8B 00                        mov rax, qword ptr [rax]
002336A8  4C 3B E8                        cmp r13, rax
002336AB  0F 86 EA 00 00 00               jbe 0x14023379b
002336B1  40 32 FF                        xor dil, dil
002336B4  8B CB                           mov ecx, ebx
002336B6  F6 C3 01                        test bl, 1
002336B9  0F 85 47 FF FF FF               jne 0x140233606
002336BF  39 2D 6B 19 D9 00               cmp dword ptr [rip + 0xd9196b], ebp
002336C5  0F 85 3B FF FF FF               jne 0x140233606
002336CB  4C 3B 9C 24 80 00 00 00         cmp r11, qword ptr [rsp + 0x80]
002336D3  0F 84 2D FF FF FF               je 0x140233606
002336D9  40 38 2D A5 33 D9 00            cmp byte ptr [rip + 0xd933a5], bpl
002336E0  0F 84 20 FF FF FF               je 0x140233606
002336E6  41 0F B6 83 09 96 00 00         movzx eax, byte ptr [r11 + 0x9609]
002336EE  41 0F B6 53 07                  movzx edx, byte ptr [r11 + 7]
002336F3  84 C0                           test al, al
002336F5  75 71                           jne 0x140233768
002336F7  8B C5                           mov eax, ebp
002336F9  84 D2                           test dl, dl
002336FB  BD 01 00 00 00                  mov ebp, 1
00233700  0F 45 C5                        cmovne eax, ebp
00233703  8B E8                           mov ebp, eax
00233705  8D 1C ED 00 00 00 00            lea ebx, [rbp*8]
0023370C  0B D9                           or ebx, ecx
0023370E  E9 F3 FE FF FF                  jmp 0x140233606
00233713  41 8B 4B 24                     mov ecx, dword ptr [r11 + 0x24]
00233717  E8 E4 0F 00 00                  call 0x140234700
0023371C  E9 F8 FE FF FF                  jmp 0x140233619
00233721  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
00233729  E9 6D FF FF FF                  jmp 0x14023369b
0023372E  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
00233736  41 8B C2                        mov eax, r10d
00233739  41 8B D2                        mov edx, r10d
0023373C  83 E0 3F                        and eax, 0x3f
0023373F  48 C1 EA 06                     shr rdx, 6
00233743  48 8D 0C D1                     lea rcx, [rcx + rdx*8]
00233747  E9 4A FF FF FF                  jmp 0x140233696
0023374C  41 0F B7 40 02                  movzx eax, word ptr [r8 + 2]
00233751  B9 00 08 00 00                  mov ecx, 0x800
00233756  66 3B C1                        cmp ax, cx
00233759  0F 82 CA FD FF FF               jb 0x140233529
0023375F  8B D0                           mov edx, eax
00233761  2B D1                           sub edx, ecx
00233763  E9 D9 FC FF FF                  jmp 0x140233441
00233768  41 0F B6 83 08 96 00 00         movzx eax, byte ptr [r11 + 0x9608]
00233770  49 8B 93 80 95 00 00            mov rdx, qword ptr [r11 + 0x9580]
00233777  84 C0                           test al, al
00233779  74 05                           je 0x140233780
0023377B  49 3B D5                        cmp rdx, r13
0023377E  76 85                           jbe 0x140233705
00233780  BD 01 00 00 00                  mov ebp, 1
00233785  8D 1C ED 00 00 00 00            lea ebx, [rbp*8]
0023378C  0B D9                           or ebx, ecx
0023378E  E9 73 FE FF FF                  jmp 0x140233606
00233793  40 88 3E                        mov byte ptr [rsi], dil
00233796  E9 87 FE FF FF                  jmp 0x140233622
0023379B  48 85 F6                        test rsi, rsi
0023379E  75 22                           jne 0x1402337c2
002337A0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002337A5  4C 8D 4C 24 28                  lea r9, [rsp + 0x28]
002337AA  83 CB 01                        or ebx, 1
002337AD  45 8B C2                        mov r8d, r10d
002337B0  49 8B D6                        mov rdx, r14
002337B3  E8 88 DF 1C 00                  call 0x140401740
002337B8  4C 8B 5C 24 20                  mov r11, qword ptr [rsp + 0x20]
002337BD  E9 EF FE FF FF                  jmp 0x1402336b1
002337C2  40 B7 01                        mov dil, 1
002337C5  E9 EA FE FF FF                  jmp 0x1402336b4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInsertTimerTable(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p98;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_rbp = 0;
    if ((*(unsigned int *)(a2 + 60)) == 0) {
        *(unsigned int *)(a2 + 4) = 0;
    }
    if ((*(unsigned int *)(v_rip + 14228471)) == 0) goto loc_00233520;
loc_00233441:
    *(unsigned __int16 *)(a2 + 56) = 0;
    v_stack_m48 = (unsigned int)(a4);
    result = (*(unsigned __int16 *)(a2 + 58)) << (8);
    v_rdi = ((unsigned int)(a4) + 16) + (result);
    v_stack_m58 = *(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976);
    v_rdi = (v_rdi) << (5);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 16640);
    v_stack_m40 = *(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 16640;
loc_00233492:
    if (condition_is_above_or_equal) goto loc_002334B6;
loc_0023349A:
    v_r15 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14229000)) & ((unsigned int)(v_r15))) == 0) goto loc_002335BB;
loc_002334AA:
loc_002334AC:
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_00233492;
    goto loc_0023349A;
loc_002334B6:
    v_stack_m50 = v_rdi;
    if ((*(unsigned __int64 *)(v_rdi + 8)) == (v_rdi + 8)) goto loc_00233519;
    if ((*(unsigned __int64 *)(a2 + 24)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) - 8))) goto loc_002334EA;
    v_rbx = (unsigned int)((0) & (2));
loc_002334D2:
loc_002334D5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) + 8)) == (v_rdi + 8)) goto loc_002335E3;
loc_002334EA:
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 14235056))) >> (2);
    result = (*(unsigned __int64 *)(a2 + 24)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) - 8));
    if (result <= a1) goto loc_00233587;
loc_00233508:
    if ((*(unsigned __int64 *)(a2 + 24)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8 + 8) - 8))) goto loc_002334D2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8 + 8) + 8)) != (v_rdi + 8)) goto loc_00233508;
    goto loc_002334D2;
loc_00233519:
    goto loc_002334D5;
loc_00233520:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) - 8) != 0) goto loc_0023374C;
loc_00233529:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 35)) & (16)) == 0) goto loc_00233441;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 192) + 128)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 192) + 80));
    if (condition_is_equal) goto loc_00233441;
    a2 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 208)) << (6));
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 209)) + ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 192))));
    v_stack_p10 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2307148 + 0 * 8 + 16550976) + 192));
    a1 = (unsigned int)((a1) & (63));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    goto loc_00233441;
loc_00233587:
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4))) == (*(unsigned __int64 *)(v_rdi + 8 + 8))) goto loc_002334D2;
loc_002335A0:
    if ((*(unsigned __int64 *)(a2 + 24)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4))) - 8))) goto loc_002334D2;
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)))) == (*(unsigned __int64 *)(v_rdi + 8 + 8))) goto loc_002334D2;
    goto loc_002335A0;
loc_002335BB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14234871)))) & (64)) == 0) goto loc_002334AA;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rdi + 8 + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)), a3, v_rip - 2307148);
    if ((unsigned __int8)(result) == 0) goto loc_002334AA;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)), a3, v_rip - 2307148);
    goto loc_002334AC;
loc_002335E3:
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)));
    *(unsigned __int64 *)(result) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)) + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13564990) + a2 * 4)))) = result;
    if (((6) & (2)) != 0) goto loc_00233643;
    v_rdi = 0;
loc_00233606:
    if (6 >= 8) goto loc_00233713;
loc_00233619:
    if (a5 != 0) goto loc_00233793;
loc_00233622:
    v_rbx = (unsigned __int8)(~(6));
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    v_rsp = (v_rsp) + (64);
    return (unsigned __int8)(v_rbx);
loc_00233643:
    *(unsigned __int64 *)(v_rdi + 24) = *(unsigned __int64 *)(a2 + 24);
    if (((unsigned int)(v_stack_p18)) < 4) goto loc_00233721;
    result = (*(unsigned __int8 *)(v_stack_m58 + 208)) + (*(unsigned __int8 *)(v_stack_m58 + 208));
    if ((*(unsigned int *)(v_rip + 14227908)) != 0) goto loc_0023372E;
    a2 = (v_stack_p30) << (6);
    a1 = (*(unsigned __int64 *)(v_rip - 2307683 + result * 8 + 16549160)) + (a2);
loc_00233696:
loc_0023369B:
    if ((*(unsigned __int64 *)(a2 + 24)) <= (*(unsigned __int64 *)(*(unsigned __int8 *)(v_stack_m58 + 209)))) goto loc_0023379B;
loc_002336B1:
    v_rdi = 0;
loc_002336B4:
    if ((((unsigned __int8)(v_stack_p18)) & (1)) != 0) goto loc_00233606;
    if ((*(unsigned int *)(v_rip + 14227819)) != 0) goto loc_00233606;
    if (v_stack_m58 == v_stack_p80) goto loc_00233606;
    if ((*(unsigned __int8 *)(v_rip + 14234533)) == 0) goto loc_00233606;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + 38409)) != 0) goto loc_00233768;
    result = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + 7)) != 0) { result = 1; }
loc_00233705:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result)) * 8) | ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))));
    goto loc_00233606;
loc_00233713:
    result = KiSendClockInterruptToTargetProcessor((unsigned int)(*(unsigned int *)(v_stack_m58 + 36)), *(unsigned __int8 *)(v_stack_m58 + 7), a3, v_rip - 2307148);
    goto loc_00233619;
loc_00233721:
    goto loc_0023369B;
loc_0023372E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p98)))) & (63));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p98)))) >> (6);
    goto loc_00233696;
loc_0023374C:
    if (((unsigned __int16)(*(unsigned __int16 *)(a3 + 2))) < ((unsigned __int16)((unsigned int)(0x800ULL)))) goto loc_00233529;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a3 + 2)))) - ((unsigned int)((unsigned int)(0x800ULL))));
    goto loc_00233441;
loc_00233768:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + 38408)) == 0) goto loc_00233780;
    if ((*(unsigned __int64 *)(v_stack_m58 + 38272)) <= (*(unsigned __int64 *)(a2 + 24))) goto loc_00233705;
loc_00233780:
    v_rbx = (unsigned int)((1 * 8) | ((unsigned int)((unsigned int)(0x800ULL))));
    goto loc_00233606;
loc_00233793:
    *(unsigned __int8 *)(a5) = 0;
    goto loc_00233622;
loc_0023379B:
    if (a5 != 0) goto loc_002337C2;
    v_rbx = (unsigned int)((v_rbx) | (1));
    result = KiRemoveEntryTimer(v_stack_p38, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p98))), v_stack_p28);
    goto loc_002336B1;
loc_002337C2:
    goto loc_002336B4;
}
```

## 5. (Beta) C Style

```c
int64_t KiInsertTimerTable(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p98;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    local_rbp = 0;
    if ((*(uint32_t *)(arg2 + 0x3C)) == 0) {
        *(uint32_t *)(arg2 + 0x4) = 0;
    }
    if ((*(uint32_t *)(v_rip + 0xD91BF7)) == 0) goto loc_00233520;
loc_00233441:
    *(uint16_t *)(arg2 + 0x38) = 0;
    v_stack_m48 = (uint32_t)(Arg4);
    result = (*(uint16_t *)(arg2 + 0x3A)) << (8);
    local_rdi = ((uint32_t)(Arg4) + 16) + (result);
    v_stack_m58 = *(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40);
    local_rdi = (local_rdi) << (5);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 16640);
    v_stack_m40 = *(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 16640;
loc_00233492:
    if (condition_is_above_or_equal) goto loc_002334B6;
loc_0023349A:
    local_r15 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD91E08)) & ((uint32_t)(local_r15))) == 0) goto loc_002335BB;
loc_002334AA:
loc_002334AC:
    if (*(uint64_t *)(local_rdi) == 0) goto loc_00233492;
    goto loc_0023349A;
loc_002334B6:
    v_stack_m50 = local_rdi;
    if ((*(uint64_t *)(local_rdi + 0x8)) == (local_rdi + 8)) goto loc_00233519;
    if ((*(uint64_t *)(arg2 + 0x18)) > (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) - 0x8))) goto loc_002334EA;
    local_rbx = (uint32_t)((0) & (2));
loc_002334D2:
loc_002334D5:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8)) == (local_rdi + 8)) goto loc_002335E3;
loc_002334EA:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0xD935B0))) >> (2);
    result = (*(uint64_t *)(arg2 + 0x18)) - (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) - 0x8));
    if (result <= Arg1) goto loc_00233587;
loc_00233508:
    if ((*(uint64_t *)(arg2 + 0x18)) >= (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8 + 0x8) - 0x8))) goto loc_002334D2;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8 + 0x8) + 0x8)) != (local_rdi + 8)) goto loc_00233508;
    goto loc_002334D2;
loc_00233519:
    goto loc_002334D5;
loc_00233520:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) - 0x8) != 0) goto loc_0023374C;
loc_00233529:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0x23)) & (16)) == 0) goto loc_00233441;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xC0) + 0x80)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xC0) + 0x50));
    if (condition_is_equal) goto loc_00233441;
    Arg2 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xD0)) << (6));
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xD1)) + ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xC0))));
    v_stack_p10 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x23344C + 0x0 * 8 + 0xFC8C40) + 0xC0));
    Arg1 = (uint32_t)((Arg1) & (63));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    goto loc_00233441;
loc_00233587:
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4))) == (*(uint64_t *)(local_rdi + 0x8 + 0x8))) goto loc_002334D2;
loc_002335A0:
    if ((*(uint64_t *)(arg2 + 0x18)) <= (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4))) - 0x8))) goto loc_002334D2;
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)))) == (*(uint64_t *)(local_rdi + 0x8 + 0x8))) goto loc_002334D2;
    goto loc_002335A0;
loc_002335BB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD934F7)))) & (64)) == 0) goto loc_002334AA;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(local_rdi + 0x8 + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)), Arg3, v_rip - 2307148);
    if ((uint8_t)(result) == 0) goto loc_002334AA;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)), Arg3, v_rip - 2307148);
    goto loc_002334AC;
loc_002335E3:
    *(uint64_t *)(result + 0x8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)));
    *(uint64_t *)(result) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)) + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCEFC3E) + arg2 * 4)))) = result;
    if (((6) & (2)) != 0) goto loc_00233643;
    local_rdi = 0;
loc_00233606:
    if (6 >= 8) goto loc_00233713;
loc_00233619:
    if (Arg5 != 0) goto loc_00233793;
loc_00233622:
    local_rbx = (uint8_t)(~(6));
    local_rbx = (uint8_t)((local_rbx) & (1));
    local_rsp = (local_rsp) + (64);
    return (uint8_t)(local_rbx);
loc_00233643:
    *(uint64_t *)(local_rdi + 0x18) = *(uint64_t *)(arg2 + 0x18);
    if (((uint32_t)(v_stack_p18)) < 4) goto loc_00233721;
    result = (*(uint8_t *)(v_stack_m58 + 0xD0)) + (*(uint8_t *)(v_stack_m58 + 0xD0));
    if ((*(uint32_t *)(v_rip + 0xD919C4)) != 0) goto loc_0023372E;
    Arg2 = (v_stack_p30) << (6);
    Arg1 = (*(uint64_t *)(v_rip - 0x233663 + result * 8 + 0xFC8528)) + (Arg2);
loc_00233696:
loc_0023369B:
    if ((*(uint64_t *)(arg2 + 0x18)) <= (*(uint64_t *)(*(uint8_t *)(v_stack_m58 + 0xD1)))) goto loc_0023379B;
loc_002336B1:
    local_rdi = 0;
loc_002336B4:
    if ((((uint8_t)(v_stack_p18)) & (1)) != 0) goto loc_00233606;
    if ((*(uint32_t *)(v_rip + 0xD9196B)) != 0) goto loc_00233606;
    if (v_stack_m58 == v_stack_p80) goto loc_00233606;
    if ((*(uint8_t *)(v_rip + 0xD933A5)) == 0) goto loc_00233606;
    if ((uint8_t)(*(uint8_t *)(v_stack_m58 + 0x9609)) != 0) goto loc_00233768;
    result = 0;
    if ((uint8_t)(*(uint8_t *)(v_stack_m58 + 0x7)) != 0) { result = 1; }
loc_00233705:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result)) * 8) | ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))));
    goto loc_00233606;
loc_00233713:
    result = KiSendClockInterruptToTargetProcessor((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24)), *(uint8_t *)(v_stack_m58 + 0x7), Arg3, v_rip - 2307148);
    goto loc_00233619;
loc_00233721:
    goto loc_0023369B;
loc_0023372E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p98)))) & (63));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p98)))) >> (6);
    goto loc_00233696;
loc_0023374C:
    if (((uint16_t)(*(uint16_t *)(Arg3 + 0x2))) < ((uint16_t)((uint32_t)(0x800ULL)))) goto loc_00233529;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(Arg3 + 0x2)))) - ((uint32_t)((uint32_t)(0x800ULL))));
    goto loc_00233441;
loc_00233768:
    if ((uint8_t)(*(uint8_t *)(v_stack_m58 + 0x9608)) == 0) goto loc_00233780;
    if ((*(uint64_t *)(v_stack_m58 + 0x9580)) <= (*(uint64_t *)(arg2 + 0x18))) goto loc_00233705;
loc_00233780:
    local_rbx = (uint32_t)((1 * 8) | ((uint32_t)((uint32_t)(0x800ULL))));
    goto loc_00233606;
loc_00233793:
    *(uint8_t *)(Arg5) = 0;
    goto loc_00233622;
loc_0023379B:
    if (Arg5 != 0) goto loc_002337C2;
    local_rbx = (uint32_t)((local_rbx) | (1));
    result = KiRemoveEntryTimer(v_stack_p38, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p98))), v_stack_p28);
    goto loc_002336B1;
loc_002337C2:
    goto loc_002336B4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x23` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `8` | `R` |
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x38` | `16` | `W` |
| `Arg2` | `+ 0x3A` | `16` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00233400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
