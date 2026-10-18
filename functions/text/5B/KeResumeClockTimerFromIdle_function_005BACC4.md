# KeResumeClockTimerFromIdle

- RVA: `0x005BACC4`–`0x005BB32B` (길이 `1,639` bytes)
- VA: `0x00000001405BACC4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA124`
- 디코드: `386`개 명령, `1,639/1,639` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **43**

### Outgoing calls
- `0x005BAD77` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x005BAD8A` → [KiUpdateTimeAssist](../39/KiUpdateTimeAssist_function_0039E230.md) (function, `0x0039E230`)
- `0x005BAE0E` → [KiOnlyClockInterruptPending](KiOnlyClockInterruptPending_function_005BB880.md) (function, `0x005BB880`)
- `0x005BAE6D` → [KiGetPastDueIRTimerInfo](../5C/KiGetPastDueIRTimerInfo_function_005C64F8.md) (function, `0x005C64F8`)
- `0x005BAE82` → [KiOnlyClockInterruptPending](KiOnlyClockInterruptPending_function_005BB880.md) (function, `0x005BB880`)
- `0x005BAF01` → [KiAdjustTimersAfterDripsExit](KiAdjustTimersAfterDripsExit_function_005BB490.md) (function, `0x005BB490`)
- `0x005BAF10` → [KiGetNextClockOwner](KiGetNextClockOwner_function_005BB5D4.md) (function, `0x005BB5D4`)
- `0x005BAF3F` → [KiEventClockStateChange](../46/KiEventClockStateChange_function_0046279C.md) (function, `0x0046279C`)
- `0x005BAF53` → [KiSendClockInterruptToTargetProcessor](../23/KiSendClockInterruptToTargetProcessor_function_00234700.md) (function, `0x00234700`)
- `0x005BAFA2` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x005BAFF8` → [KiOnlyClockInterruptPending](KiOnlyClockInterruptPending_function_005BB880.md) (function, `0x005BB880`)
- `0x005BB037` → [KiGetPendingTick](KiGetPendingTick_function_005BB84C.md) (function, `0x005BB84C`)
- `0x005BB047` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005BB07A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005BB0A8` → [KiSetClockTimer](../39/KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x005BB0B6` → [KiSetClockTimerKTimerDeadlines](../23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) (function, `0x0023671C`)
- `0x005BB0CB` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x005BB0E6` → [KiRestoreClockTickRate](../4D/KiRestoreClockTickRate_function_004D2780.md) (function, `0x004D2780`)
- `0x005BB11C` → [KiEventClockStateChange](../46/KiEventClockStateChange_function_0046279C.md) (function, `0x0046279C`)
- `0x005BB12B` → [KiResetForceIdle](../3A/KiResetForceIdle_function_003A4160.md) (function, `0x003A4160`)
- `0x005BB143` → [KiSetVpThreadHrTimerActive](../46/KiSetVpThreadHrTimerActive_function_00463394.md) (function, `0x00463394`)
- `0x005BB148` → [KiGetPendingTick](KiGetPendingTick_function_005BB84C.md) (function, `0x005BB84C`)
- `0x005BB16B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005BB1D8` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005BB1EE` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x005BB215` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005BB243` → [KiSetClockTimer](../39/KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x005BB260` → [KiSetClockTimerKTimerDeadlines](../23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) (function, `0x0023671C`)
- `0x005BB270` → [KiRestoreClockTickRate](../4D/KiRestoreClockTickRate_function_004D2780.md) (function, `0x004D2780`)
- `0x005BB285` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x005BB2C9` → [KiEventClockStateChange](../46/KiEventClockStateChange_function_0046279C.md) (function, `0x0046279C`)
- `0x005BB2EA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005BB2F1` → [KiSetPendingTick](../44/KiSetPendingTick_function_004400F4.md) (function, `0x004400F4`)
- `0x005BB304` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006DCEEE](../6D/Unknown_function_006DCEEE.md) at `0x006DD31D`

### Static image references
- `0x005BACE7` → RVA `0x00E0A740` (`.data`; read)
- `0x005BACFB` → RVA `0x00FC5364` (`ALMOSTRO`; read)
- `0x005BAD47` → RVA `0x00FCF000` (`CACHEALI`; read)
- `0x005BAD4D` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x005BAD93` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x005BAD9B` → RVA `0x00F21F80` (`.data`; write)
- `0x005BADA2` → RVA `0x00E668B0` (`.data`; read)
- `0x005BADAA` → RVA `0x00FC6BEC` (`ALMOSTRO`; read)
- `0x005BADB8` → RVA `0x00E668B0` (`.data`; write)
- `0x005BADBF` → RVA `0x00E668A8` (`.data`; read)
- `0x005BADC5` → RVA `0x00FC6BB8` (`ALMOSTRO`; read)
- `0x005BADDD` → RVA `0x00E668A8` (`.data`; write)
- `0x005BADE4` → RVA `0x00F21FAD` (`.data`; read)
- `0x005BADF5` → RVA `0x00F21FB0` (`.data`; read)
- `0x005BADFD` → RVA `0x00F21F88` (`.data`; read)
- `0x005BAE21` → RVA `0x00F21FAD` (`.data`; write)
- `0x005BAE2B` → RVA `0x00F21FB8` (`.data`; read)
- `0x005BAE32` → RVA `0x00F21F48` (`.data`; read)
- `0x005BAE3B` → RVA `0x00F21F48` (`.data`; write)
- `0x005BAE42` → RVA `0x00F21F40` (`.data`; read)
- `0x005BAE4B` → RVA `0x00F21F40` (`.data`; write)
- `0x005BAE52` → RVA `0x00F22260` (`.data`; read)
- `0x005BAE8B` → RVA `0x00EFAB80` (`.data`; read)
- `0x005BAED8` → RVA `0x00E093D0` (`.data`; read)
- `0x005BAF06` → RVA `0x00F22260` (`.data`; write)
- `0x005BAF26` → RVA `0x00F21F38` (`.data`; read/write)
- `0x005BAF4C` → RVA `0x00F21FB0` (`.data`; write)
- `0x005BAF58` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x005BAFA7` → RVA `0x00FCF000` (`CACHEALI`; read/write)
- `0x005BAFDC` → RVA `0x00F21FAC` (`.data`; read)
- `0x005BAFED` → RVA `0x00F21FAC` (`.data`; write)
- `0x005BB00E` → RVA `0x00F21FC0` (`.data`; read)
- `0x005BB024` → RVA `0x00FC6ABF` (`ALMOSTRO`; read)
- `0x005BB040` → RVA `0x00E00AE0` (`.data`; read)
- `0x005BB056` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x005BB06C` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x005BB07F` → RVA `0x00FC6D5C` (`ALMOSTRO`; read)
- `0x005BB0FD` → RVA `0x00FC6B7C` (`ALMOSTRO`; read)
- `0x005BB10A` → RVA `0x00F21F88` (`.data`; write)
- `0x005BB17D` → RVA `0x00E070D8` (`.data`; read)
- `0x005BB18C` → RVA `0x00048490` (`.rdata`; read)
- `0x005BB251` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x005BB2E3` → RVA `0x00E00AE8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BACC4  48 8B C4                        mov rax, rsp
005BACC7  48 89 58 08                     mov qword ptr [rax + 8], rbx
005BACCB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005BACCF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
005BACD3  55                              push rbp
005BACD4  41 54                           push r12
005BACD6  41 55                           push r13
005BACD8  41 56                           push r14
005BACDA  41 57                           push r15
005BACDC  48 8D 68 A1                     lea rbp, [rax - 0x5f]
005BACE0  48 81 EC E0 00 00 00            sub rsp, 0xe0
005BACE7  48 8B 05 52 FA 84 00            mov rax, qword ptr [rip + 0x84fa52]
005BACEE  48 33 C4                        xor rax, rsp
005BACF1  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005BACF5  45 33 ED                        xor r13d, r13d
005BACF8  49 8B F0                        mov rsi, r8
005BACFB  44 38 2D 62 A6 A0 00            cmp byte ptr [rip + 0xa0a662], r13b
005BAD02  44 8A F2                        mov r14b, dl
005BAD05  44 8A E1                        mov r12b, cl
005BAD08  4C 89 6D AF                     mov qword ptr [rbp - 0x51], r13
005BAD0C  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
005BAD10  4C 89 6D A7                     mov qword ptr [rbp - 0x59], r13
005BAD14  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
005BAD18  44 88 6D 97                     mov byte ptr [rbp - 0x69], r13b
005BAD1C  44 88 6D 9A                     mov byte ptr [rbp - 0x66], r13b
005BAD20  44 89 6D B7                     mov dword ptr [rbp - 0x49], r13d
005BAD24  0F 85 D3 05 00 00               jne 0x1405bb2fd
005BAD2A  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
005BAD33  45 8A FD                        mov r15b, r13b
005BAD36  44 88 6D 99                     mov byte ptr [rbp - 0x67], r13b
005BAD3A  44 88 6D 98                     mov byte ptr [rbp - 0x68], r13b
005BAD3E  4D 85 C0                        test r8, r8
005BAD41  74 04                           je 0x1405bad47
005BAD43  41 83 08 FF                     or dword ptr [r8], 0xffffffff
005BAD47  8B 05 B3 42 A1 00               mov eax, dword ptr [rip + 0xa142b3]
005BAD4D  48 8D 3D AC 52 A4 FF            lea rdi, [rip - 0x5bad54]
005BAD54  41 B8 03 00 00 00               mov r8d, 3
005BAD5A  83 F8 01                        cmp eax, 1
005BAD5D  75 0B                           jne 0x1405bad6a
005BAD5F  F0 44 0F B1 05 98 42 A1 00      lock cmpxchg dword ptr [rip + 0xa14298], r8d
005BAD68  74 14                           je 0x1405bad7e
005BAD6A  41 3B C0                        cmp eax, r8d
005BAD6D  0F 85 41 02 00 00               jne 0x1405bafb4
005BAD73  48 8D 4D B7                     lea rcx, [rbp - 0x49]
005BAD77  E8 84 0F E4 FF                  call 0x1403fbd00
005BAD7C  EB C9                           jmp 0x1405bad47
005BAD7E  4C 8D 4D BF                     lea r9, [rbp - 0x41]
005BAD82  B2 01                           mov dl, 1
005BAD84  4C 8D 45 9F                     lea r8, [rbp - 0x61]
005BAD88  33 C9                           xor ecx, ecx
005BAD8A  E8 A1 34 DE FF                  call 0x14039e230
005BAD8F  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
005BAD93  8B 05 A3 BD A0 00               mov eax, dword ptr [rip + 0xa0bda3]
005BAD99  FF C8                           dec eax
005BAD9B  48 89 0D DE 71 96 00            mov qword ptr [rip + 0x9671de], rcx
005BADA2  2B 0D 08 BB 8A 00               sub ecx, dword ptr [rip + 0x8abb08]
005BADA8  03 C8                           add ecx, eax
005BADAA  8B 05 3C BE A0 00               mov eax, dword ptr [rip + 0xa0be3c]
005BADB0  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
005BADB4  3B C8                           cmp ecx, eax
005BADB6  72 07                           jb 0x1405badbf
005BADB8  48 89 15 F1 BA 8A 00            mov qword ptr [rip + 0x8abaf1], rdx
005BADBF  2B 15 E3 BA 8A 00               sub edx, dword ptr [rip + 0x8abae3]
005BADC5  8B 05 ED BD A0 00               mov eax, dword ptr [rip + 0xa0bded]
005BADCB  8B 0D 6B BD A0 00               mov ecx, dword ptr [rip + 0xa0bd6b]
005BADD1  48 8B 7D 9F                     mov rdi, qword ptr [rbp - 0x61]
005BADD5  FF C9                           dec ecx
005BADD7  03 CA                           add ecx, edx
005BADD9  3B C8                           cmp ecx, eax
005BADDB  72 07                           jb 0x1405bade4
005BADDD  48 89 3D C4 BA 8A 00            mov qword ptr [rip + 0x8abac4], rdi
005BADE4  44 38 2D C2 71 96 00            cmp byte ptr [rip + 0x9671c2], r13b
005BADEB  74 3B                           je 0x1405bae28
005BADED  48 85 F6                        test rsi, rsi
005BADF0  74 2F                           je 0x1405bae21
005BADF2  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
005BADF5  39 05 B5 71 96 00               cmp dword ptr [rip + 0x9671b5], eax
005BADFB  75 24                           jne 0x1405bae21
005BADFD  48 3B 3D 84 71 96 00            cmp rdi, qword ptr [rip + 0x967184]
005BAE04  72 1B                           jb 0x1405bae21
005BAE06  48 8D 55 98                     lea rdx, [rbp - 0x68]
005BAE0A  48 8D 4D 99                     lea rcx, [rbp - 0x67]
005BAE0E  E8 6D 0A 00 00                  call 0x1405bb880
005BAE13  84 C0                           test al, al
005BAE15  74 0A                           je 0x1405bae21
005BAE17  8B C7                           mov eax, edi
005BAE19  2B 05 69 71 96 00               sub eax, dword ptr [rip + 0x967169]
005BAE1F  89 06                           mov dword ptr [rsi], eax
005BAE21  44 88 2D 85 71 96 00            mov byte ptr [rip + 0x967185], r13b
005BAE28  48 8B C7                        mov rax, rdi
005BAE2B  48 2B 05 86 71 96 00            sub rax, qword ptr [rip + 0x967186]
005BAE32  48 3B 05 0F 71 96 00            cmp rax, qword ptr [rip + 0x96710f]
005BAE39  73 07                           jae 0x1405bae42
005BAE3B  48 89 05 06 71 96 00            mov qword ptr [rip + 0x967106], rax
005BAE42  48 3B 05 F7 70 96 00            cmp rax, qword ptr [rip + 0x9670f7]
005BAE49  76 07                           jbe 0x1405bae52
005BAE4B  48 89 05 EE 70 96 00            mov qword ptr [rip + 0x9670ee], rax
005BAE52  44 38 2D 07 74 96 00            cmp byte ptr [rip + 0x967407], r13b
005BAE59  0F 84 AE 00 00 00               je 0x1405baf0d
005BAE5F  4C 8D 4D 9A                     lea r9, [rbp - 0x66]
005BAE63  41 8A D6                        mov dl, r14b
005BAE66  4C 8D 45 97                     lea r8, [rbp - 0x69]
005BAE6A  48 8B CF                        mov rcx, rdi
005BAE6D  E8 86 B6 00 00                  call 0x1405c64f8
005BAE72  85 C0                           test eax, eax
005BAE74  0F 84 81 00 00 00               je 0x1405baefb
005BAE7A  48 8D 55 98                     lea rdx, [rbp - 0x68]
005BAE7E  48 8D 4D 99                     lea rcx, [rbp - 0x67]
005BAE82  E8 F9 09 00 00                  call 0x1405bb880
005BAE87  84 C0                           test al, al
005BAE89  74 70                           je 0x1405baefb
005BAE8B  48 8B 15 EE FC 93 00            mov rdx, qword ptr [rip + 0x93fcee]
005BAE92  44 8A 45 9A                     mov r8b, byte ptr [rbp - 0x66]
005BAE96  44 8A 4D 97                     mov r9b, byte ptr [rbp - 0x69]
005BAE9A  48 85 D2                        test rdx, rdx
005BAE9D  74 58                           je 0x1405baef7
005BAE9F  80 7D 97 14                     cmp byte ptr [rbp - 0x69], 0x14
005BAEA3  72 06                           jb 0x1405baeab
005BAEA5  45 8A CD                        mov r9b, r13b
005BAEA8  45 8A C5                        mov r8b, r13b
005BAEAB  41 0F B6 C1                     movzx eax, r9b
005BAEAF  48 8D 0C 40                     lea rcx, [rax + rax*2]
005BAEB3  48 8D 05 46 51 A4 FF            lea rax, [rip - 0x5baeba]
005BAEBA  8A 84 C8 D0 93 E0 00            mov al, byte ptr [rax + rcx*8 + 0xe093d0]
005BAEC1  44 3A C0                        cmp r8b, al
005BAEC4  45 1A D2                        sbb r10b, r10b
005BAEC7  44 3A C0                        cmp r8b, al
005BAECA  1A C0                           sbb al, al
005BAECC  41 22 C0                        and al, r8b
005BAECF  44 0F B6 C0                     movzx r8d, al
005BAED3  45 22 D1                        and r10b, r9b
005BAED6  74 1B                           je 0x1405baef3
005BAED8  48 8D 0D F1 E4 84 00            lea rcx, [rip + 0x84e4f1]
005BAEDF  45 0F B6 CA                     movzx r9d, r10b
005BAEE3  0F B6 01                        movzx eax, byte ptr [rcx]
005BAEE6  48 8D 49 18                     lea rcx, [rcx + 0x18]
005BAEEA  44 03 C0                        add r8d, eax
005BAEED  49 83 E9 01                     sub r9, 1
005BAEF1  75 F0                           jne 0x1405baee3
005BAEF3  42 FF 04 82                     inc dword ptr [rdx + r8*4]
005BAEF7  48 8B 7D 9F                     mov rdi, qword ptr [rbp - 0x61]
005BAEFB  48 8B D7                        mov rdx, rdi
005BAEFE  48 8B CB                        mov rcx, rbx
005BAF01  E8 8A 05 00 00                  call 0x1405bb490
005BAF06  44 88 2D 53 73 96 00            mov byte ptr [rip + 0x967353], r13b
005BAF0D  48 8B CB                        mov rcx, rbx
005BAF10  E8 BF 06 00 00                  call 0x1405bb5d4
005BAF15  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
005BAF18  44 8B F0                        mov r14d, eax
005BAF1B  3B C8                           cmp ecx, eax
005BAF1D  0F 84 EB 00 00 00               je 0x1405bb00e
005BAF23  41 B7 01                        mov r15b, 1
005BAF26  48 FF 05 0B 70 96 00            inc qword ptr [rip + 0x96700b]
005BAF2D  B8 02 00 00 00                  mov eax, 2
005BAF32  45 33 C9                        xor r9d, r9d
005BAF35  45 33 C0                        xor r8d, r8d
005BAF38  8B C8                           mov ecx, eax
005BAF3A  8B F0                           mov esi, eax
005BAF3C  8D 50 FF                        lea edx, [rax - 1]
005BAF3F  E8 58 78 EA FF                  call 0x14046279c
005BAF44  45 84 FF                        test r15b, r15b
005BAF47  74 0F                           je 0x1405baf58
005BAF49  41 8B CE                        mov ecx, r14d
005BAF4C  44 89 35 5D 70 96 00            mov dword ptr [rip + 0x96705d], r14d
005BAF53  E8 A8 97 C7 FF                  call 0x140234700
005BAF58  F7 05 A6 BB A0 00 00 00 10 00   test dword ptr [rip + 0xa0bba6], 0x100000
005BAF62  8B 0D 48 70 96 00               mov ecx, dword ptr [rip + 0x967048]
005BAF68  44 89 6D D3                     mov dword ptr [rbp - 0x2d], r13d
005BAF6C  74 39                           je 0x1405bafa7
005BAF6E  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
005BAF71  48 8D 45 C7                     lea rax, [rbp - 0x39]
005BAF75  48 8D 4D D7                     lea rcx, [rbp - 0x29]
005BAF79  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
005BAF7D  41 B9 58 0F 00 00               mov r9d, 0xf58
005BAF83  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
005BAF87  BA 01 00 00 00                  mov edx, 1
005BAF8C  48 C7 45 DF 10 00 00 00         mov qword ptr [rbp - 0x21], 0x10
005BAF94  41 B8 00 00 10 40               mov r8d, 0x40100000
005BAF9A  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
005BAFA2  E8 A9 A3 C7 FF                  call 0x140235350
005BAFA7  87 35 53 40 A1 00               xchg dword ptr [rip + 0xa14053], esi
005BAFAD  48 8D 3D 4C 50 A4 FF            lea rdi, [rip - 0x5bafb4]
005BAFB4  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
005BAFB7  39 05 F3 6F 96 00               cmp dword ptr [rip + 0x966ff3], eax
005BAFBD  75 0A                           jne 0x1405bafc9
005BAFBF  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BAFC3  75 0E                           jne 0x1405bafd3
005BAFC5  C6 43 21 01                     mov byte ptr [rbx + 0x21], 1
005BAFC9  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BAFCD  0F 84 63 01 00 00               je 0x1405bb136
005BAFD3  45 84 E4                        test r12b, r12b
005BAFD6  0F 85 54 01 00 00               jne 0x1405bb130
005BAFDC  44 38 2D C9 6F 96 00            cmp byte ptr [rip + 0x966fc9], r13b
005BAFE3  0F 84 47 01 00 00               je 0x1405bb130
005BAFE9  48 8D 55 98                     lea rdx, [rbp - 0x68]
005BAFED  44 88 2D B8 6F 96 00            mov byte ptr [rip + 0x966fb8], r13b
005BAFF4  48 8D 4D 99                     lea rcx, [rbp - 0x67]
005BAFF8  E8 83 08 00 00                  call 0x1405bb880
005BAFFD  33 D2                           xor edx, edx
005BAFFF  84 C0                           test al, al
005BB001  0F 84 1F 01 00 00               je 0x1405bb126
005BB007  33 C9                           xor ecx, ecx
005BB009  E9 1D 01 00 00                  jmp 0x1405bb12b
005BB00E  8B 05 AC 6F 96 00               mov eax, dword ptr [rip + 0x966fac]
005BB014  48 03 C7                        add rax, rdi
005BB017  48 3B 05 6A 6F 96 00            cmp rax, qword ptr [rip + 0x966f6a]
005BB01E  0F 87 02 FF FF FF               ja 0x1405baf26
005BB024  44 38 2D 94 BA A0 00            cmp byte ptr [rip + 0xa0ba94], r13b
005BB02B  74 1F                           je 0x1405bb04c
005BB02D  C6 43 21 01                     mov byte ptr [rbx + 0x21], 1
005BB031  89 0D 79 6F 96 00               mov dword ptr [rip + 0x966f79], ecx
005BB037  E8 10 08 00 00                  call 0x1405bb84c
005BB03C  84 C0                           test al, al
005BB03E  75 0C                           jne 0x1405bb04c
005BB040  48 8B 05 99 5A 84 00            mov rax, qword ptr [rip + 0x845a99]
005BB047  E8 84 FA 0F 00                  call 0x1406baad0
005BB04C  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BB050  0F 84 82 00 00 00               je 0x1405bb0d8
005BB056  44 38 2D 28 BA A0 00            cmp byte ptr [rip + 0xa0ba28], r13b
005BB05D  74 79                           je 0x1405bb0d8
005BB05F  44 0F 20 C6                     mov rsi, cr8
005BB063  B8 0F 00 00 00                  mov eax, 0xf
005BB068  44 0F 22 C0                     mov cr8, rax
005BB06C  44 39 2D AD BC A0 00            cmp dword ptr [rip + 0xa0bcad], r13d
005BB073  74 0A                           je 0x1405bb07f
005BB075  8A D0                           mov dl, al
005BB077  40 8A CE                        mov cl, sil
005BB07A  E8 7D A6 F3 FF                  call 0x1404f56fc
005BB07F  44 8B 05 D6 BC A0 00            mov r8d, dword ptr [rip + 0xa0bcd6]
005BB086  48 8B D7                        mov rdx, rdi
005BB089  44 8B 0D AC BA A0 00            mov r9d, dword ptr [rip + 0xa0baac]
005BB090  49 F7 D8                        neg r8
005BB093  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
005BB098  48 8B CB                        mov rcx, rbx
005BB09B  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
005BB0A0  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
005BB0A8  E8 7F 2A DE FF                  call 0x14039db2c
005BB0AD  41 B0 01                        mov r8b, 1
005BB0B0  48 8B D7                        mov rdx, rdi
005BB0B3  48 8B CB                        mov rcx, rbx
005BB0B6  E8 61 B6 C7 FF                  call 0x14023671c
005BB0BB  44 39 2D 5E BC A0 00            cmp dword ptr [rip + 0xa0bc5e], r13d
005BB0C2  74 0C                           je 0x1405bb0d0
005BB0C4  44 0F 20 C1                     mov rcx, cr8
005BB0C8  40 8A D6                        mov dl, sil
005BB0CB  E8 C8 A5 F3 FF                  call 0x1404f5698
005BB0D0  40 0F B6 C6                     movzx eax, sil
005BB0D4  44 0F 22 C0                     mov cr8, rax
005BB0D8  4C 8D 45 AF                     lea r8, [rbp - 0x51]
005BB0DC  48 8B CF                        mov rcx, rdi
005BB0DF  48 8D 55 A7                     lea rdx, [rbp - 0x59]
005BB0E3  41 8B F5                        mov esi, r13d
005BB0E6  E8 95 76 F1 FF                  call 0x1404d2780
005BB0EB  44 38 2D 93 B9 A0 00            cmp byte ptr [rip + 0xa0b993], r13b
005BB0F2  74 09                           je 0x1405bb0fd
005BB0F4  48 8B 83 80 95 00 00            mov rax, qword ptr [rbx + 0x9580]
005BB0FB  EB 09                           jmp 0x1405bb106
005BB0FD  8B 05 79 BA A0 00               mov eax, dword ptr [rip + 0xa0ba79]
005BB103  48 03 C7                        add rax, rdi
005BB106  4C 8D 4D A7                     lea r9, [rbp - 0x59]
005BB10A  48 89 05 77 6E 96 00            mov qword ptr [rip + 0x966e77], rax
005BB111  4C 8D 45 AF                     lea r8, [rbp - 0x51]
005BB115  BA 01 00 00 00                  mov edx, 1
005BB11A  33 C9                           xor ecx, ecx
005BB11C  E8 7B 76 EA FF                  call 0x14046279c
005BB121  E9 32 FE FF FF                  jmp 0x1405baf58
005BB126  B9 01 00 00 00                  mov ecx, 1
005BB12B  E8 30 90 DE FF                  call 0x1403a4160
005BB130  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BB134  75 12                           jne 0x1405bb148
005BB136  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
005BB139  33 D2                           xor edx, edx
005BB13B  48 8B 8C CF 40 8C FC 00         mov rcx, qword ptr [rdi + rcx*8 + 0xfc8c40]
005BB143  E8 4C 82 EA FF                  call 0x140463394
005BB148  E8 FF 06 00 00                  call 0x1405bb84c
005BB14D  84 C0                           test al, al
005BB14F  75 1F                           jne 0x1405bb170
005BB151  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BB155  75 0D                           jne 0x1405bb164
005BB157  44 38 2D 27 B9 A0 00            cmp byte ptr [rip + 0xa0b927], r13b
005BB15E  0F 84 6A 01 00 00               je 0x1405bb2ce
005BB164  48 8B 05 75 59 84 00            mov rax, qword ptr [rip + 0x845975]
005BB16B  E8 60 F9 0F 00                  call 0x1406baad0
005BB170  44 38 2D 0E B9 A0 00            cmp byte ptr [rip + 0xa0b90e], r13b
005BB177  0F 84 51 01 00 00               je 0x1405bb2ce
005BB17D  83 3D 54 BF 84 00 05            cmp dword ptr [rip + 0x84bf54], 5
005BB184  76 57                           jbe 0x1405bb1dd
005BB186  8A 83 09 96 00 00               mov al, byte ptr [rbx + 0x9609]
005BB18C  48 8D 15 FD D2 A8 FF            lea rdx, [rip - 0x572d03]
005BB193  88 45 9B                        mov byte ptr [rbp - 0x65], al
005BB196  48 8D 0D 3B BF 84 00            lea rcx, [rip + 0x84bf3b]
005BB19D  48 8D 45 9B                     lea rax, [rbp - 0x65]
005BB1A1  48 C7 45 0F 01 00 00 00         mov qword ptr [rbp + 0xf], 1
005BB1A9  48 89 45 07                     mov qword ptr [rbp + 7], rax
005BB1AD  45 33 C9                        xor r9d, r9d
005BB1B0  48 8D 45 9C                     lea rax, [rbp - 0x64]
005BB1B4  44 88 65 9C                     mov byte ptr [rbp - 0x64], r12b
005BB1B8  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005BB1BC  45 33 C0                        xor r8d, r8d
005BB1BF  48 8D 45 E7                     lea rax, [rbp - 0x19]
005BB1C3  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
005BB1CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005BB1D0  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
005BB1D8  E8 03 AF E6 FF                  call 0x1404260e0
005BB1DD  44 38 AB 09 96 00 00            cmp byte ptr [rbx + 0x9609], r13b
005BB1E4  0F 84 E4 00 00 00               je 0x1405bb2ce
005BB1EA  48 8D 4D BF                     lea rcx, [rbp - 0x41]
005BB1EE  E8 CD F2 C4 FF                  call 0x14020a4c0
005BB1F3  48 8B F8                        mov rdi, rax
005BB1F6  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
005BB1FA  44 0F 20 C6                     mov rsi, cr8
005BB1FE  B8 0F 00 00 00                  mov eax, 0xf
005BB203  44 0F 22 C0                     mov cr8, rax
005BB207  44 39 2D 12 BB A0 00            cmp dword ptr [rip + 0xa0bb12], r13d
005BB20E  74 0A                           je 0x1405bb21a
005BB210  8A D0                           mov dl, al
005BB212  40 8A CE                        mov cl, sil
005BB215  E8 E2 A4 F3 FF                  call 0x1404f56fc
005BB21A  44 8B 05 3B BB A0 00            mov r8d, dword ptr [rip + 0xa0bb3b]
005BB221  48 8B D7                        mov rdx, rdi
005BB224  44 8B 0D 11 B9 A0 00            mov r9d, dword ptr [rip + 0xa0b911]
005BB22B  49 F7 D8                        neg r8
005BB22E  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
005BB233  48 8B CB                        mov rcx, rbx
005BB236  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
005BB23B  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
005BB243  E8 E4 28 DE FF                  call 0x14039db2c
005BB248  44 8A 43 21                     mov r8b, byte ptr [rbx + 0x21]
005BB24C  45 84 C0                        test r8b, r8b
005BB24F  75 09                           jne 0x1405bb25a
005BB251  44 39 2D D8 9D A0 00            cmp dword ptr [rip + 0xa09dd8], r13d
005BB258  75 0B                           jne 0x1405bb265
005BB25A  48 8B D7                        mov rdx, rdi
005BB25D  48 8B CB                        mov rcx, rbx
005BB260  E8 B7 B4 C7 FF                  call 0x14023671c
005BB265  4C 8D 45 AF                     lea r8, [rbp - 0x51]
005BB269  48 8B CF                        mov rcx, rdi
005BB26C  48 8D 55 A7                     lea rdx, [rbp - 0x59]
005BB270  E8 0B 75 F1 FF                  call 0x1404d2780
005BB275  44 39 2D A4 BA A0 00            cmp dword ptr [rip + 0xa0baa4], r13d
005BB27C  74 0C                           je 0x1405bb28a
005BB27E  44 0F 20 C1                     mov rcx, cr8
005BB282  40 8A D6                        mov dl, sil
005BB285  E8 0E A4 F3 FF                  call 0x1404f5698
005BB28A  40 0F B6 C6                     movzx eax, sil
005BB28E  44 0F 22 C0                     mov cr8, rax
005BB292  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BB296  74 3C                           je 0x1405bb2d4
005BB298  48 8B 83 80 95 00 00            mov rax, qword ptr [rbx + 0x9580]
005BB29F  48 89 05 E2 6C 96 00            mov qword ptr [rip + 0x966ce2], rax
005BB2A6  8B 05 54 3D A1 00               mov eax, dword ptr [rip + 0xa13d54]
005BB2AC  83 F8 02                        cmp eax, 2
005BB2AF  75 1D                           jne 0x1405bb2ce
005BB2B1  41 8B C5                        mov eax, r13d
005BB2B4  4C 8D 4D A7                     lea r9, [rbp - 0x59]
005BB2B8  87 05 42 3D A1 00               xchg dword ptr [rip + 0xa13d42], eax
005BB2BE  4C 8D 45 AF                     lea r8, [rbp - 0x51]
005BB2C2  BA 02 00 00 00                  mov edx, 2
005BB2C7  33 C9                           xor ecx, ecx
005BB2C9  E8 CE 74 EA FF                  call 0x14046279c
005BB2CE  44 38 6B 21                     cmp byte ptr [rbx + 0x21], r13b
005BB2D2  75 29                           jne 0x1405bb2fd
005BB2D4  F6 43 22 01                     test byte ptr [rbx + 0x22], 1
005BB2D8  74 23                           je 0x1405bb2fd
005BB2DA  44 38 2D A4 B7 A0 00            cmp byte ptr [rip + 0xa0b7a4], r13b
005BB2E1  75 1A                           jne 0x1405bb2fd
005BB2E3  48 8B 05 FE 57 84 00            mov rax, qword ptr [rip + 0x8457fe]
005BB2EA  E8 E1 F7 0F 00                  call 0x1406baad0
005BB2EF  33 C9                           xor ecx, ecx
005BB2F1  E8 FE 4D E8 FF                  call 0x1404400f4
005BB2F6  44 88 AB 08 96 00 00            mov byte ptr [rbx + 0x9608], r13b
005BB2FD  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
005BB301  48 33 CC                        xor rcx, rsp
005BB304  E8 37 13 0F 00                  call 0x1406ac640
005BB309  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
005BB311  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005BB315  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
005BB319  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
005BB31D  49 8B E3                        mov rsp, r11
005BB320  41 5F                           pop r15
005BB322  41 5E                           pop r14
005BB324  41 5D                           pop r13
005BB326  41 5C                           pop r12
005BB328  5D                              pop rbp
005BB329  C3                              ret
005BB32A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeResumeClockTimerFromIdle(unsigned __int8 a1, unsigned __int8 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_mD8;
    unsigned __int8 v_stack_mE0;
    unsigned int v_stack_mE8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 8714834)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 105) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 102) = 0;
    *(unsigned int *)(v_rsp - 95 - 73) = 0;
    if ((*(unsigned __int8 *)(v_rip + 10528354)) != 0) goto loc_005BB2FD;
    *(unsigned __int8 *)(v_rsp - 95 - 103) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 104) = 0;
    if (a3 != 0) {
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568371)))) != 1) goto loc_005BAD6A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568371)))) == 1) goto loc_005BAD7E;
loc_005BAD6A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568371)))) != 3) goto loc_005BAFB4;
    result = KeYieldProcessorEx(v_rsp - 95 - 73, a2, 3, a4);
    goto loc_005BAD47;
loc_005BAD7E:
    a1 = 0;
    result = KiUpdateTimeAssist(a1, 1, v_rsp - 95 - 97, v_rsp - 95 - 65);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10534307))) - 1);
    *(unsigned __int64 *)(v_rip + 9859550) = *(unsigned __int64 *)(v_rsp - 95 - 97);
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 97)) - (*(unsigned int *)(v_rip + 9091848)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (a1 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10534460))))) {
        *(unsigned __int64 *)(v_rip + 9091825) = *(unsigned __int64 *)(v_rsp - 95 - 97);
    }
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 97)) - (*(unsigned int *)(v_rip + 9091811)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10534251))) - 1);
    a1 = (unsigned int)((a1) + (a2));
    if (a1 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10534381))))) {
        *(unsigned __int64 *)(v_rip + 9091780) = *(unsigned __int64 *)(v_rsp - 95 - 97);
    }
    if ((*(unsigned __int8 *)(v_rip + 9859522)) == 0) goto loc_005BAE28;
    if (a3 == 0) goto loc_005BAE21;
    if ((*(unsigned int *)(v_rip + 9859509)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))))) goto loc_005BAE21;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 97)) < (*(unsigned __int64 *)(v_rip + 9859460))) goto loc_005BAE21;
    result = KiOnlyClockInterruptPending(v_rsp - 95 - 103, v_rsp - 95 - 104, v_rsp - 95 - 97, v_rsp - 95 - 65);
    if ((unsigned __int8)(result) != 0) {
        result = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 97));
        result = (unsigned int)((result) - (*(unsigned int *)(v_rip + 9859433)));
        *(unsigned int *)(a3) = (unsigned int)(result);
    }
    *(unsigned __int8 *)(v_rip + 9859461) = 0;
loc_005BAE28:
    result = (*(unsigned __int64 *)(v_rsp - 95 - 97)) - (*(unsigned __int64 *)(v_rip + 9859462));
    if (result < (*(unsigned __int64 *)(v_rip + 9859343))) {
        *(unsigned __int64 *)(v_rip + 9859334) = result;
    }
    if (result >= = (*(unsigned __int64 *)(v_rip + 9859319))) {
        *(unsigned __int64 *)(v_rip + 9859310) = result;
    }
    if ((*(unsigned __int8 *)(v_rip + 9860103)) == 0) goto loc_005BAF0D;
    result = KiGetPastDueIRTimerInfo(*(unsigned __int64 *)(v_rsp - 95 - 97), a2, v_rsp - 95 - 105, v_rsp - 95 - 102);
    if ((unsigned int)(result) == 0) goto loc_005BAEFB;
    result = KiOnlyClockInterruptPending(v_rsp - 95 - 103, v_rsp - 95 - 104, v_rsp - 95 - 105, v_rsp - 95 - 102);
    if ((unsigned __int8)(result) == 0) goto loc_005BAEFB;
    if (*(unsigned __int64 *)(v_rip + 9698542) == 0) goto loc_005BAEF7;
    if ((*(unsigned __int8 *)(v_rsp - 95 - 105)) >= 20) {
        a4 = 0;
        a3 = 0;
    }
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 6008506 + (unsigned __int8)(a4) + (unsigned __int8)(a4) * 2 * 8 + 14717904)) & ((unsigned __int8)(a3)));
    v_r10 = (unsigned __int8)((v_r10) & ((unsigned __int8)(a4)));
    if (condition_is_equal) goto loc_005BAEF3;
loc_005BAEE3:
    a3 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)(*(unsigned __int8 *)(v_rip + 8709361))));
    a4 = ((unsigned __int8)(v_r10)) - (1);
    if (condition_is_not_equal) goto loc_005BAEE3;
loc_005BAEF3:
loc_005BAEF7:
loc_005BAEFB:
    result = KiAdjustTimersAfterDripsExit(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_rsp - 95 - 97), a3, a4);
    *(unsigned __int8 *)(v_rip + 9859923) = 0;
loc_005BAF0D:
    result = KiGetNextClockOwner(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_rsp - 95 - 97), a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)))) == ((unsigned int)(result))) goto loc_005BB00E;
loc_005BAF26:
    a4 = 0;
    a3 = 0;
    result = KiEventClockStateChange(2, 2 - 1, a3, a4);
    if (1 != 0) {
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned int *)(v_rip + 9859165) = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = KiSendClockInterruptToTargetProcessor(a1, 2 - 1, a3, a4);
    }
    *(unsigned int *)(v_rsp - 95 - 45) = 0;
    if (((*(unsigned int *)(v_rip + 10533798)) & (0x100000ULL)) != 0) {
        *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9859144)));
        result = v_rsp - 95 - 57;
        a1 = v_rsp - 95 - 41;
        *(unsigned __int64 *)(v_rsp - 95 - 41) = result;
        a4 = 0xF58ULL;
        *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_rsp - 95 - 97);
        a2 = 1;
        *(unsigned __int64 *)(v_rsp - 95 - 33) = 16;
        a3 = 0x40100000ULL;
        v_stack_mE8 = 0x602ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
loc_005BAFB4:
    if ((*(unsigned int *)(v_rip + 9859059)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))))) goto loc_005BAFC9;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) != 0) goto loc_005BAFD3;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33) = 1;
loc_005BAFC9:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) goto loc_005BB136;
loc_005BAFD3:
    if (a1 != 0) goto loc_005BB130;
    if ((*(unsigned __int8 *)(v_rip + 9859017)) == 0) goto loc_005BB130;
    *(unsigned __int8 *)(v_rip + 9859000) = 0;
    result = KiOnlyClockInterruptPending(v_rsp - 95 - 103, v_rsp - 95 - 104, a3, a4);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_005BB126;
    a1 = 0;
    goto loc_005BB12B;
loc_005BB00E:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 9858988))) + (v_rip - 6008756);
    if (result > (*(unsigned __int64 *)(v_rip + 9858922))) goto loc_005BAF26;
    if ((*(unsigned __int8 *)(v_rip + 10533524)) == 0) goto loc_005BB04C;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33) = 1;
    *(unsigned int *)(v_rip + 9858937) = 0;
    result = KiGetPendingTick(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned __int64 *)(v_rip + 8673945);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) goto loc_005BB0D8;
    if ((*(unsigned __int8 *)(v_rip + 10533416)) == 0) goto loc_005BB0D8;
    result = 15;
    if ((*(unsigned int *)(v_rip + 10534061)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    a3 = -((unsigned int)(*(unsigned int *)(v_rip + 10534102)));
    v_stack_mD8 = 0;
    v_stack_mE0 = 1;
    v_stack_mE8 = 3;
    result = KiSetClockTimer(*(unsigned __int64 *)(gs_base + (0 + 32)), v_rip - 6008756, a3, (unsigned int)(*(unsigned int *)(v_rip + 10533548)));
    result = KiSetClockTimerKTimerDeadlines(*(unsigned __int64 *)(gs_base + (0 + 32)), v_rip - 6008756, 1, (unsigned int)(*(unsigned int *)(v_rip + 10533548)));
    if ((*(unsigned int *)(v_rip + 10533982)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_rip + 10533548)));
    }
loc_005BB0D8:
    result = KiRestoreClockTickRate(v_rip - 6008756, v_rsp - 95 - 89, v_rsp - 95 - 81, (unsigned int)(*(unsigned int *)(v_rip + 10533548)));
    if ((*(unsigned __int8 *)(v_rip + 10533267)) == 0) goto loc_005BB0FD;
    goto loc_005BB106;
loc_005BB0FD:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 10533497))) + (v_rip - 6008756);
loc_005BB106:
    *(unsigned __int64 *)(v_rip + 9858679) = result;
    a1 = 0;
    result = KiEventClockStateChange(a1, 1, v_rsp - 95 - 81, v_rsp - 95 - 89);
    goto loc_005BAF58;
loc_005BB126:
loc_005BB12B:
    result = KiResetForceIdle(1, 1, v_rsp - 95 - 81, v_rsp - 95 - 89);
loc_005BB130:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rip - 6008756 + a1 * 8 + 16550976);
        result = KiSetVpThreadHrTimerActive(a1, a2, v_rsp - 95 - 81, v_rsp - 95 - 89);
    }
    result = KiGetPendingTick(a1, a2, v_rsp - 95 - 81, v_rsp - 95 - 89);
    if ((unsigned __int8)(result) != 0) goto loc_005BB170;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) != 0) goto loc_005BB164;
    if ((*(unsigned __int8 *)(v_rip + 10533159)) == 0) goto loc_005BB2CE;
loc_005BB164:
    result = guard_dispatch_icall(a1, a2, v_rsp - 95 - 81, v_rsp - 95 - 89);
loc_005BB170:
    if ((*(unsigned __int8 *)(v_rip + 10533134)) == 0) goto loc_005BB2CE;
    if ((*(unsigned int *)(v_rip + 8699732)) >= = 5) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38409);
        a2 = v_rip - 5713155;
        *(unsigned __int8 *)(v_rsp - 95 - 101) = (unsigned __int8)(result);
        a1 = v_rip + 8699707;
        result = v_rsp - 95 - 101;
        *(unsigned __int64 *)(v_rsp - 95 + 15) = 1;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        a4 = 0;
        result = v_rsp - 95 - 100;
        *(unsigned __int8 *)(v_rsp - 95 - 100) = a1;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        a3 = 0;
        result = v_rsp - 95 - 25;
        *(unsigned __int64 *)(v_rsp - 95 + 31) = 1;
        v_stack_mE0 = result;
        v_stack_mE8 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38409)) == 0) goto loc_005BB2CE;
    result = RtlGetInterruptTimePrecise(v_rsp - 95 - 65, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 95 - 97) = result;
    result = 15;
    if ((*(unsigned int *)(v_rip + 10533650)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    a3 = -((unsigned int)(*(unsigned int *)(v_rip + 10533691)));
    v_stack_mD8 = 0;
    v_stack_mE0 = 1;
    v_stack_mE8 = 3;
    result = KiSetClockTimer(*(unsigned __int64 *)(gs_base + (0 + 32)), result, a3, (unsigned int)(*(unsigned int *)(v_rip + 10533137)));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) != 0) goto loc_005BB25A;
    if ((*(unsigned int *)(v_rip + 10526168)) == 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiSetClockTimerKTimerDeadlines(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33), (unsigned int)(*(unsigned int *)(v_rip + 10533137)));
    }
    result = KiRestoreClockTickRate(result, v_rsp - 95 - 89, v_rsp - 95 - 81, (unsigned int)(*(unsigned int *)(v_rip + 10533137)));
    if ((*(unsigned int *)(v_rip + 10533540)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rsp - 95 - 81, (unsigned int)(*(unsigned int *)(v_rip + 10533137)));
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) goto loc_005BB2D4;
    *(unsigned __int64 *)(v_rip + 9858274) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272);
    result = (unsigned int)(*(unsigned int *)(v_rip + 10566996));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10566996)))) == 2) {
        result = 0;
        a4 = v_rsp - 95 - 89;
        a3 = v_rsp - 95 - 81;
        a2 = 2;
        a1 = 0;
        result = KiEventClockStateChange(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) != 0) goto loc_005BB2FD;
loc_005BB2D4:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34)) & (1)) == 0) goto loc_005BB2FD;
    if ((*(unsigned __int8 *)(v_rip + 10532772)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 8673278);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = 0;
        result = KiSetPendingTick(a1, a2, a3, a4);
        *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38408) = 0;
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeResumeClockTimerFromIdle(uint8_t Arg1, uint8_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_mD8;
    uint8_t v_stack_mE0;
    uint32_t v_stack_mE8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x84FA52)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x69) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x66) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = 0;
    if ((*(uint8_t *)(v_rip + 0xA0A662)) != 0) goto loc_005BB2FD;
    *(uint8_t *)(local_rsp - 0x5F - 0x67) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x68) = 0;
    if (Arg3 != 0) {
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA142B3)))) != 1) goto loc_005BAD6A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA142B3)))) == 1) goto loc_005BAD7E;
loc_005BAD6A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA142B3)))) != 3) goto loc_005BAFB4;
    result = KeYieldProcessorEx(local_rsp - 95 - 73, Arg2, 3, a4);
    goto loc_005BAD47;
loc_005BAD7E:
    Arg1 = 0;
    result = KiUpdateTimeAssist(Arg1, 1, local_rsp - 95 - 97, local_rsp - 95 - 65);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA0BDA3))) - 1);
    *(uint64_t *)(v_rip + 0x9671DE) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    Arg1 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x61)) - (*(uint32_t *)(v_rip + 0x8ABB08)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (Arg1 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0BE3C))))) {
        *(uint64_t *)(v_rip + 0x8ABAF1) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    }
    Arg2 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x61)) - (*(uint32_t *)(v_rip + 0x8ABAE3)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA0BD6B))) - 1);
    Arg1 = (uint32_t)((Arg1) + (Arg2));
    if (Arg1 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0BDED))))) {
        *(uint64_t *)(v_rip + 0x8ABAC4) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    }
    if ((*(uint8_t *)(v_rip + 0x9671C2)) == 0) goto loc_005BAE28;
    if (Arg3 == 0) goto loc_005BAE21;
    if ((*(uint32_t *)(v_rip + 0x9671B5)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))))) goto loc_005BAE21;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x61)) < (*(uint64_t *)(v_rip + 0x967184))) goto loc_005BAE21;
    result = KiOnlyClockInterruptPending(local_rsp - 95 - 103, local_rsp - 95 - 104, local_rsp - 95 - 97, local_rsp - 95 - 65);
    if ((uint8_t)(result) != 0) {
        result = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x61));
        result = (uint32_t)((result) - (*(uint32_t *)(v_rip + 0x967169)));
        *(uint32_t *)(Arg3) = (uint32_t)(result);
    }
    *(uint8_t *)(v_rip + 0x967185) = 0;
loc_005BAE28:
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x61)) - (*(uint64_t *)(v_rip + 0x967186));
    if (result < (*(uint64_t *)(v_rip + 0x96710F))) {
        *(uint64_t *)(v_rip + 0x967106) = result;
    }
    if (result >= = (*(uint64_t *)(v_rip + 0x9670F7))) {
        *(uint64_t *)(v_rip + 0x9670EE) = result;
    }
    if ((*(uint8_t *)(v_rip + 0x967407)) == 0) goto loc_005BAF0D;
    result = KiGetPastDueIRTimerInfo(*(uint64_t *)(local_rsp - 0x5F - 0x61), Arg2, local_rsp - 95 - 105, local_rsp - 95 - 102);
    if ((uint32_t)(result) == 0) goto loc_005BAEFB;
    result = KiOnlyClockInterruptPending(local_rsp - 95 - 103, local_rsp - 95 - 104, local_rsp - 95 - 105, local_rsp - 95 - 102);
    if ((uint8_t)(result) == 0) goto loc_005BAEFB;
    if (*(uint64_t *)(v_rip + 0x93FCEE) == 0) goto loc_005BAEF7;
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x69)) >= 20) {
        a4 = 0;
        Arg3 = 0;
    }
    result = (uint8_t)((*(uint8_t *)(v_rip - 0x5BAEBA + (uint8_t)(a4) + (uint8_t)(a4) * 2 * 8 + 0xE093D0)) & ((uint8_t)(Arg3)));
    local_r10 = (uint8_t)((local_r10) & ((uint8_t)(a4)));
    if (condition_is_equal) goto loc_005BAEF3;
loc_005BAEE3:
    Arg3 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)(*(uint8_t *)(v_rip + 0x84E4F1))));
    a4 = ((uint8_t)(local_r10)) - (1);
    if (condition_is_not_equal) goto loc_005BAEE3;
loc_005BAEF3:
loc_005BAEF7:
loc_005BAEFB:
    result = KiAdjustTimersAfterDripsExit(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(local_rsp - 0x5F - 0x61), Arg3, a4);
    *(uint8_t *)(v_rip + 0x967353) = 0;
loc_005BAF0D:
    result = KiGetNextClockOwner(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(local_rsp - 0x5F - 0x61), Arg3, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)))) == ((uint32_t)(result))) goto loc_005BB00E;
loc_005BAF26:
    a4 = 0;
    Arg3 = 0;
    result = KiEventClockStateChange(2, 2 - 1, Arg3, a4);
    if (1 != 0) {
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint32_t *)(v_rip + 0x96705D) = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = KiSendClockInterruptToTargetProcessor(Arg1, 2 - 1, Arg3, a4);
    }
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = 0;
    if (((*(uint32_t *)(v_rip + 0xA0BBA6)) & (0x100000ULL)) != 0) {
        *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x967048)));
        result = local_rsp - 95 - 57;
        Arg1 = local_rsp - 95 - 41;
        *(uint64_t *)(local_rsp - 0x5F - 0x29) = result;
        a4 = 0xF58ULL;
        *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
        Arg2 = 1;
        *(uint64_t *)(local_rsp - 0x5F - 0x21) = 16;
        Arg3 = 0x40100000ULL;
        v_stack_mE8 = 0x602ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, a4);
    }
loc_005BAFB4:
    if ((*(uint32_t *)(v_rip + 0x966FF3)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))))) goto loc_005BAFC9;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) != 0) goto loc_005BAFD3;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21) = 1;
loc_005BAFC9:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) goto loc_005BB136;
loc_005BAFD3:
    if (Arg1 != 0) goto loc_005BB130;
    if ((*(uint8_t *)(v_rip + 0x966FC9)) == 0) goto loc_005BB130;
    *(uint8_t *)(v_rip + 0x966FB8) = 0;
    result = KiOnlyClockInterruptPending(local_rsp - 95 - 103, local_rsp - 95 - 104, Arg3, a4);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_005BB126;
    Arg1 = 0;
    goto loc_005BB12B;
loc_005BB00E:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x966FAC))) + (v_rip - 6008756);
    if (result > (*(uint64_t *)(v_rip + 0x966F6A))) goto loc_005BAF26;
    if ((*(uint8_t *)(v_rip + 0xA0BA94)) == 0) goto loc_005BB04C;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21) = 1;
    *(uint32_t *)(v_rip + 0x966F79) = 0;
    result = KiGetPendingTick(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) {
        result = *(uint64_t *)(v_rip + 0x845A99);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) goto loc_005BB0D8;
    if ((*(uint8_t *)(v_rip + 0xA0BA28)) == 0) goto loc_005BB0D8;
    result = 15;
    if ((*(uint32_t *)(v_rip + 0xA0BCAD)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    Arg3 = -((uint32_t)(*(uint32_t *)(v_rip + 0xA0BCD6)));
    v_stack_mD8 = 0;
    v_stack_mE0 = 1;
    v_stack_mE8 = 3;
    result = KiSetClockTimer(*(uint64_t *)(gs_base + (0 + 0x20)), v_rip - 6008756, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xA0BAAC)));
    result = KiSetClockTimerKTimerDeadlines(*(uint64_t *)(gs_base + (0 + 0x20)), v_rip - 6008756, 1, (uint32_t)(*(uint32_t *)(v_rip + 0xA0BAAC)));
    if ((*(uint32_t *)(v_rip + 0xA0BC5E)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_rip + 0xA0BAAC)));
    }
loc_005BB0D8:
    result = KiRestoreClockTickRate(v_rip - 6008756, local_rsp - 95 - 89, local_rsp - 95 - 81, (uint32_t)(*(uint32_t *)(v_rip + 0xA0BAAC)));
    if ((*(uint8_t *)(v_rip + 0xA0B993)) == 0) goto loc_005BB0FD;
    goto loc_005BB106;
loc_005BB0FD:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0xA0BA79))) + (v_rip - 6008756);
loc_005BB106:
    *(uint64_t *)(v_rip + 0x966E77) = result;
    Arg1 = 0;
    result = KiEventClockStateChange(Arg1, 1, local_rsp - 95 - 81, local_rsp - 95 - 89);
    goto loc_005BAF58;
loc_005BB126:
loc_005BB12B:
    result = KiResetForceIdle(1, 1, local_rsp - 95 - 81, local_rsp - 95 - 89);
loc_005BB130:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_rip - 0x5BAFB4 + Arg1 * 8 + 0xFC8C40);
        result = KiSetVpThreadHrTimerActive(Arg1, Arg2, local_rsp - 95 - 81, local_rsp - 95 - 89);
    }
    result = KiGetPendingTick(Arg1, Arg2, local_rsp - 95 - 81, local_rsp - 95 - 89);
    if ((uint8_t)(result) != 0) goto loc_005BB170;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) != 0) goto loc_005BB164;
    if ((*(uint8_t *)(v_rip + 0xA0B927)) == 0) goto loc_005BB2CE;
loc_005BB164:
    result = guard_dispatch_icall(Arg1, Arg2, local_rsp - 95 - 81, local_rsp - 95 - 89);
loc_005BB170:
    if ((*(uint8_t *)(v_rip + 0xA0B90E)) == 0) goto loc_005BB2CE;
    if ((*(uint32_t *)(v_rip + 0x84BF54)) >= = 5) {
        result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9609);
        Arg2 = v_rip - 5713155;
        *(uint8_t *)(local_rsp - 0x5F - 0x65) = (uint8_t)(result);
        Arg1 = v_rip + 8699707;
        result = local_rsp - 95 - 101;
        *(uint64_t *)(local_rsp - 0x5F + 0xF) = 1;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        a4 = 0;
        result = local_rsp - 95 - 100;
        *(uint8_t *)(local_rsp - 0x5F - 0x64) = Arg1;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        Arg3 = 0;
        result = local_rsp - 95 - 25;
        *(uint64_t *)(local_rsp - 0x5F + 0x1F) = 1;
        v_stack_mE0 = result;
        v_stack_mE8 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9609)) == 0) goto loc_005BB2CE;
    result = RtlGetInterruptTimePrecise(local_rsp - 95 - 65, Arg2, Arg3, a4);
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = result;
    result = 15;
    if ((*(uint32_t *)(v_rip + 0xA0BB12)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    Arg3 = -((uint32_t)(*(uint32_t *)(v_rip + 0xA0BB3B)));
    v_stack_mD8 = 0;
    v_stack_mE0 = 1;
    v_stack_mE8 = 3;
    result = KiSetClockTimer(*(uint64_t *)(gs_base + (0 + 0x20)), result, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xA0B911)));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) != 0) goto loc_005BB25A;
    if ((*(uint32_t *)(v_rip + 0xA09DD8)) == 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiSetClockTimerKTimerDeadlines(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21), (uint32_t)(*(uint32_t *)(v_rip + 0xA0B911)));
    }
    result = KiRestoreClockTickRate(result, local_rsp - 95 - 89, local_rsp - 95 - 81, (uint32_t)(*(uint32_t *)(v_rip + 0xA0B911)));
    if ((*(uint32_t *)(v_rip + 0xA0BAA4)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_rsp - 95 - 81, (uint32_t)(*(uint32_t *)(v_rip + 0xA0B911)));
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) goto loc_005BB2D4;
    *(uint64_t *)(v_rip + 0x966CE2) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA13D54));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA13D54)))) == 2) {
        result = 0;
        a4 = local_rsp - 95 - 89;
        Arg3 = local_rsp - 95 - 81;
        Arg2 = 2;
        Arg1 = 0;
        result = KiEventClockStateChange(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) != 0) goto loc_005BB2FD;
loc_005BB2D4:
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x22)) & (1)) == 0) goto loc_005BB2FD;
    if ((*(uint8_t *)(v_rip + 0xA0B7A4)) == 0) {
        result = *(uint64_t *)(v_rip + 0x8457FE);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
        Arg1 = 0;
        result = KiSetPendingTick(Arg1, Arg2, Arg3, a4);
        *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9608) = 0;
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BACC4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
