# KiHeteroSelectProcessorToPreempt

- RVA: `0x002560D0`–`0x002566D1` (길이 `1,537` bytes)
- VA: `0x00000001402560D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063814`
- 디코드: `380`개 명령, `1,537/1,537` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00256204` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002563B3` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x002563DA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00256409` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00256418` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00256580` → [KiSelectCandidateProcessor](../43/KiSelectCandidateProcessor_function_00434690.md) (function, `0x00434690`)
- `0x0025658A` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x002565FC` → [KiAcquirePrcbLocksForPreemptionAttemptSlowPath](../43/KiAcquirePrcbLocksForPreemptionAttemptSlowPath_function_00434910.md) (function, `0x00434910`)

### Direct callers
- [sub_0025308F](Unknown_function_0025308F.md) at `0x00253DA8`

### Static image references
- `0x002560E7` → RVA `0x00E0A740` (`.data`; read)
- `0x002561C2` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00256212` → RVA `0x00FC6D14` (`ALMOSTRO`; read)
- `0x00256241` → RVA `0x00FC6C6C` (`ALMOSTRO`; read)
- `0x00256273` → RVA `0x00F231B8` (`.data`; read)
- `0x00256341` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002563FB` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0025662A` → RVA `0x00FC6D10` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002560D0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002560D5  55                              push rbp
002560D6  56                              push rsi
002560D7  57                              push rdi
002560D8  41 54                           push r12
002560DA  41 55                           push r13
002560DC  41 56                           push r14
002560DE  41 57                           push r15
002560E0  48 81 EC C0 00 00 00            sub rsp, 0xc0
002560E7  48 8B 05 52 46 BB 00            mov rax, qword ptr [rip + 0xbb4652]
002560EE  48 33 C4                        xor rax, rsp
002560F1  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
002560F9  4C 8B 92 C0 00 00 00            mov r10, qword ptr [rdx + 0xc0]
00256100  45 33 FF                        xor r15d, r15d
00256103  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
0025610B  49 8B F1                        mov rsi, r9
0025610E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00256113  4C 8B E2                        mov r12, rdx
00256116  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0025611B  41 0F B7 82 88 00 00 00         movzx eax, word ptr [r10 + 0x88]
00256123  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00256128  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0025612D  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
00256132  66 41 3B 00                     cmp ax, word ptr [r8]
00256136  0F 83 CF 04 00 00               jae 0x14025660b
0025613C  4D 8B 4C C0 08                  mov r9, qword ptr [r8 + rax*8 + 8]
00256141  8B 46 04                        mov eax, dword ptr [rsi + 4]
00256144  4D 8B F1                        mov r14, r9
00256147  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
0025614A  49 8B F9                        mov rdi, r9
0025614D  0F B6 56 10                     movzx edx, byte ptr [rsi + 0x10]
00256151  44 8D 04 41                     lea r8d, [rcx + rax*2]
00256155  41 0F B6 82 B9 00 00 00         movzx eax, byte ptr [r10 + 0xb9]
0025615D  44 0F AF C0                     imul r8d, eax
00256161  49 8B 82 C0 00 00 00            mov rax, qword ptr [r10 + 0xc0]
00256168  44 03 C2                        add r8d, edx
0025616B  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0025616F  48 8B 54 C8 10                  mov rdx, qword ptr [rax + rcx*8 + 0x10]
00256174  48 8D 04 C8                     lea rax, [rax + rcx*8]
00256178  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0025617C  48 8B 00                        mov rax, qword ptr [rax]
0025617F  4C 23 F1                        and r14, rcx
00256182  4C 23 F2                        and r14, rdx
00256185  48 23 FA                        and rdi, rdx
00256188  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0025618D  48 8B C7                        mov rax, rdi
00256190  74 16                           je 0x1402561a8
00256192  4D 85 F6                        test r14, r14
00256195  74 20                           je 0x1402561b7
00256197  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0025619C  4C 3B F0                        cmp r14, rax
0025619F  74 16                           je 0x1402561b7
002561A1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002561A6  EB 12                           jmp 0x1402561ba
002561A8  49 8B BA 80 00 00 00            mov rdi, qword ptr [r10 + 0x80]
002561AF  49 23 F9                        and rdi, r9
002561B2  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
002561B7  4D 8B F7                        mov r14, r15
002561BA  49 8B AC 24 40 8E 00 00         mov rbp, qword ptr [r12 + 0x8e40]
002561C2  4C 8D 05 77 2A D7 00            lea r8, [rip + 0xd72a77]
002561C9  48 23 EF                        and rbp, rdi
002561CC  48 8D 45 FF                     lea rax, [rbp - 1]
002561D0  48 85 C5                        test rbp, rax
002561D3  0F 84 BD 00 00 00               je 0x140256296
002561D9  49 8B 94 24 48 8E 00 00         mov rdx, qword ptr [r12 + 0x8e48]
002561E1  48 8D 74 24 70                  lea rsi, [rsp + 0x70]
002561E6  0F B6 BA C1 02 00 00            movzx edi, byte ptr [rdx + 0x2c1]
002561ED  0F B6 9A C0 02 00 00            movzx ebx, byte ptr [rdx + 0x2c0]
002561F4  48 03 F7                        add rsi, rdi
002561F7  48 8B CE                        mov rcx, rsi
002561FA  44 8B C3                        mov r8d, ebx
002561FD  48 81 C2 40 02 00 00            add rdx, 0x240
00256204  E8 37 06 47 00                  call 0x1406c6840
00256209  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0025620E  44 8D 1C 1F                     lea r11d, [rdi + rbx]
00256212  8B 05 FC 0A D7 00               mov eax, dword ptr [rip + 0xd70afc]
00256218  41 BA FF FF FF FF               mov r10d, 0xffffffff
0025621E  44 0F B6 81 C3 00 00 00         movzx r8d, byte ptr [rcx + 0xc3]
00256226  A8 02                           test al, 2
00256228  0F 85 FC 03 00 00               jne 0x14025662a
0025622E  0F B6 89 04 02 00 00            movzx ecx, byte ptr [rcx + 0x204]
00256235  8D 41 FB                        lea eax, [rcx - 5]
00256238  83 F8 01                        cmp eax, 1
0025623B  0F 87 D2 03 00 00               ja 0x140256613
00256241  44 39 3D 24 0A D7 00            cmp dword ptr [rip + 0xd70a24], r15d
00256248  0F 85 40 02 00 00               jne 0x14025648e
0025624E  4D 85 F6                        test r14, r14
00256251  0F 85 4C 03 00 00               jne 0x1402565a3
00256257  45 85 D2                        test r10d, r10d
0025625A  0F 88 DD 03 00 00               js 0x14025663d
00256260  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00256265  4C 8D 05 D4 29 D7 00            lea r8, [rip + 0xd729d4]
0025626C  0F B6 88 D0 00 00 00            movzx ecx, byte ptr [rax + 0xd0]
00256273  48 8B 05 3E CF CC 00            mov rax, qword ptr [rip + 0xcccf3e]
0025627A  C1 E1 06                        shl ecx, 6
0025627D  41 03 CA                        add ecx, r10d
00256280  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
00256283  4D 8B 24 C8                     mov r12, qword ptr [r8 + rcx*8]
00256287  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0025628C  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00256291  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00256296  49 85 BC 24 C8 00 00 00         test qword ptr [r12 + 0xc8], rdi
0025629E  75 38                           jne 0x1402562d8
002562A0  41 0F B6 8C 24 D1 00 00 00      movzx ecx, byte ptr [r12 + 0xd1]
002562A9  48 8B C7                        mov rax, rdi
002562AC  41 0F B6 94 24 D0 00 00 00      movzx edx, byte ptr [r12 + 0xd0]
002562B5  48 D3 C8                        ror rax, cl
002562B8  48 0F BC C0                     bsf rax, rax
002562BC  C1 E2 06                        shl edx, 6
002562BF  03 C8                           add ecx, eax
002562C1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002562C5  48 8B 05 EC CE CC 00            mov rax, qword ptr [rip + 0xccceec]
002562CC  83 E1 3F                        and ecx, 0x3f
002562CF  03 D1                           add edx, ecx
002562D1  8B 0C 90                        mov ecx, dword ptr [rax + rdx*4]
002562D4  4D 8B 24 C8                     mov r12, qword ptr [r8 + rcx*8]
002562D8  44 8B 6E 14                     mov r13d, dword ptr [rsi + 0x14]
002562DC  41 8B D5                        mov edx, r13d
002562DF  49 8B 5C 24 38                  mov rbx, qword ptr [r12 + 0x38]
002562E4  0F B6 1B                        movzx ebx, byte ptr [rbx]
002562E7  8B C3                           mov eax, ebx
002562E9  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
002562EE  C1 E8 07                        shr eax, 7
002562F1  44 3B E8                        cmp r13d, eax
002562F4  0F 4C D0                        cmovl edx, eax
002562F7  48 63 C2                        movsxd rax, edx
002562FA  48 8B C8                        mov rcx, rax
002562FD  49 33 CC                        xor rcx, r12
00256300  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00256304  48 33 C8                        xor rcx, rax
00256307  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0025630C  85 D2                           test edx, edx
0025630E  0F 84 0E 01 00 00               je 0x140256422
00256314  83 FA 01                        cmp edx, 1
00256317  75 5A                           jne 0x140256373
00256319  49 8B 84 24 58 8E 00 00         mov rax, qword ptr [r12 + 0x8e58]
00256321  0F B6 08                        movzx ecx, byte ptr [rax]
00256324  4C 8D 70 08                     lea r14, [rax + 8]
00256328  85 C9                           test ecx, ecx
0025632A  74 47                           je 0x140256373
0025632C  8B E9                           mov ebp, ecx
0025632E  66 90                           nop
00256330  49 8B 3E                        mov rdi, qword ptr [r14]
00256333  41 8B F7                        mov esi, r15d
00256336  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
0025633D  73 1B                           jae 0x14025635a
0025633F  FF C6                           inc esi
00256341  85 35 65 EF D6 00               test dword ptr [rip + 0xd6ef65], esi
00256347  0F 84 AE 00 00 00               je 0x1402563fb
0025634D  F3 90                           pause
0025634F  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00256353  48 85 C0                        test rax, rax
00256356  74 DE                           je 0x140256336
00256358  EB E5                           jmp 0x14025633f
0025635A  49 83 C6 08                     add r14, 8
0025635E  48 83 ED 01                     sub rbp, 1
00256362  75 CC                           jne 0x140256330
00256364  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00256369  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0025636E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00256373  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
00256378  32 18                           xor bl, byte ptr [rax]
0025637A  0F 88 71 02 00 00               js 0x1402565f1
00256380  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
00256384  48 63 46 14                     movsxd rax, dword ptr [rsi + 0x14]
00256388  48 23 D7                        and rdx, rdi
0025638B  49 8B 4C C2 10                  mov rcx, qword ptr [r10 + rax*8 + 0x10]
00256390  48 85 CA                        test rdx, rcx
00256393  0F 85 98 00 00 00               jne 0x140256431
00256399  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0025639E  44 89 7B 08                     mov dword ptr [rbx + 8], r15d
002563A2  41 F6 44 24 23 10               test byte ptr [r12 + 0x23], 0x10
002563A8  0F 85 63 01 00 00               jne 0x140256511
002563AE  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002563B3  E8 B8 08 00 00                  call 0x140256c70
002563B8  85 C0                           test eax, eax
002563BA  0F 85 FB 02 00 00               jne 0x1402566bb
002563C0  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002563C5  48 89 0B                        mov qword ptr [rbx], rcx
002563C8  44 89 7B 0C                     mov dword ptr [rbx + 0xc], r15d
002563CC  41 8B C7                        mov eax, r15d
002563CF  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
002563D7  48 33 CC                        xor rcx, rsp
002563DA  E8 61 62 45 00                  call 0x1406ac640
002563DF  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
002563E7  48 81 C4 C0 00 00 00            add rsp, 0xc0
002563EE  41 5F                           pop r15
002563F0  41 5E                           pop r14
002563F2  41 5D                           pop r13
002563F4  41 5C                           pop r12
002563F6  5F                              pop rdi
002563F7  5E                              pop rsi
002563F8  5D                              pop rbp
002563F9  C3                              ret
002563FA  CC                              int3
002563FB  8B 05 B7 06 D7 00               mov eax, dword ptr [rip + 0xd706b7]
00256401  A8 40                           test al, 0x40
00256403  0F 84 44 FF FF FF               je 0x14025634d
00256409  E8 82 90 0B 00                  call 0x14030f490
0025640E  84 C0                           test al, al
00256410  0F 84 37 FF FF FF               je 0x14025634d
00256416  8B CE                           mov ecx, esi
00256418  E8 43 90 0B 00                  call 0x14030f460
0025641D  E9 2D FF FF FF                  jmp 0x14025634f
00256422  4C 8D 74 24 68                  lea r14, [rsp + 0x68]
00256427  B9 01 00 00 00                  mov ecx, 1
0025642C  E9 FB FE FF FF                  jmp 0x14025632c
00256431  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00256436  41 8B D7                        mov edx, r15d
00256439  4C 8B C0                        mov r8, rax
0025643C  49 83 E0 FE                     and r8, 0xfffffffffffffffe
00256440  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00256445  83 E0 01                        and eax, 1
00256448  0F 84 B4 00 00 00               je 0x140256502
0025644E  83 F8 01                        cmp eax, 1
00256451  75 15                           jne 0x140256468
00256453  49 8B 80 58 8E 00 00            mov rax, qword ptr [r8 + 0x8e58]
0025645A  4D 8B B8 58 8E 00 00            mov r15, qword ptr [r8 + 0x8e58]
00256461  49 83 C7 08                     add r15, 8
00256465  0F B6 10                        movzx edx, byte ptr [rax]
00256468  85 D2                           test edx, edx
0025646A  74 17                           je 0x140256483
0025646C  0F 1F 40 00                     nop dword ptr [rax]
00256470  8D 42 FF                        lea eax, [rdx - 1]
00256473  49 8B 0C C7                     mov rcx, qword ptr [r15 + rax*8]
00256477  8B D0                           mov edx, eax
00256479  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0025647F  85 C0                           test eax, eax
00256481  75 ED                           jne 0x140256470
00256483  41 BF 2D 02 00 C0               mov r15d, 0xc000022d
00256489  E9 3E FF FF FF                  jmp 0x1402563cc
0025648E  49 8B 84 24 C0 00 00 00         mov rax, qword ptr [r12 + 0xc0]
00256496  4C 8B A0 48 01 00 00            mov r12, qword ptr [rax + 0x148]
0025649D  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
002564A2  4C 85 E5                        test rbp, r12
002564A5  0F 84 A3 FD FF FF               je 0x14025624e
002564AB  44 8B CF                        mov r9d, edi
002564AE  41 3B FB                        cmp edi, r11d
002564B1  0F 83 97 FD FF FF               jae 0x14025624e
002564B7  48 8B CF                        mov rcx, rdi
002564BA  BA 01 00 00 00                  mov edx, 1
002564BF  48 D3 C2                        rol rdx, cl
002564C2  48 8B DE                        mov rbx, rsi
002564C5  48 8B C2                        mov rax, rdx
002564C8  49 23 C4                        and rax, r12
002564CB  48 85 C5                        test rbp, rax
002564CE  74 1F                           je 0x1402564ef
002564D0  44 0F B6 23                     movzx r12d, byte ptr [rbx]
002564D4  41 8B CC                        mov ecx, r12d
002564D7  83 E1 7F                        and ecx, 0x7f
002564DA  41 3A C8                        cmp cl, r8b
002564DD  7D 0B                           jge 0x1402564ea
002564DF  45 0F B6 C4                     movzx r8d, r12b
002564E3  45 8B D1                        mov r10d, r9d
002564E6  41 80 E0 7F                     and r8b, 0x7f
002564EA  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
002564EF  41 FF C1                        inc r9d
002564F2  48 D1 C2                        rol rdx, 1
002564F5  48 FF C3                        inc rbx
002564F8  45 3B CB                        cmp r9d, r11d
002564FB  72 C8                           jb 0x1402564c5
002564FD  E9 4C FD FF FF                  jmp 0x14025624e
00256502  4C 8D 7C 24 58                  lea r15, [rsp + 0x58]
00256507  BA 01 00 00 00                  mov edx, 1
0025650C  E9 5F FF FF FF                  jmp 0x140256470
00256511  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00256516  4D 8B C7                        mov r8, r15
00256519  4C 8B C8                        mov r9, rax
0025651C  41 8B D7                        mov edx, r15d
0025651F  49 83 E1 FE                     and r9, 0xfffffffffffffffe
00256523  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
00256528  83 E0 01                        and eax, 1
0025652B  0F 84 B1 00 00 00               je 0x1402565e2
00256531  83 F8 01                        cmp eax, 1
00256534  75 15                           jne 0x14025654b
00256536  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0025653D  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
00256544  49 83 C0 08                     add r8, 8
00256548  0F B6 10                        movzx edx, byte ptr [rax]
0025654B  85 D2                           test edx, edx
0025654D  74 13                           je 0x140256562
0025654F  90                              nop
00256550  8D 42 FF                        lea eax, [rdx - 1]
00256553  4D 8B 0C C0                     mov r9, qword ptr [r8 + rax*8]
00256557  8B D0                           mov edx, eax
00256559  F0 4D 21 79 30                  lock and qword ptr [r9 + 0x30], r15
0025655E  85 C0                           test eax, eax
00256560  75 EE                           jne 0x140256550
00256562  44 8B 4E 14                     mov r9d, dword ptr [rsi + 0x14]
00256566  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0025656B  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00256570  4C 8B C7                        mov r8, rdi
00256573  49 8B CC                        mov rcx, r12
00256576  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025657B  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00256580  E8 0B E1 1D 00                  call 0x140434690
00256585  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0025658A  E8 E1 06 00 00                  call 0x140256c70
0025658F  85 C0                           test eax, eax
00256591  0F 84 29 FE FF FF               je 0x1402563c0
00256597  C7 43 08 01 00 00 00            mov dword ptr [rbx + 8], 1
0025659E  E9 1D FE FF FF                  jmp 0x1402563c0
002565A3  45 85 D2                        test r10d, r10d
002565A6  0F 89 B4 FC FF FF               jns 0x140256260
002565AC  44 8B CF                        mov r9d, edi
002565AF  41 3B FB                        cmp edi, r11d
002565B2  0F 83 CF 00 00 00               jae 0x140256687
002565B8  48 8B CF                        mov rcx, rdi
002565BB  BA 01 00 00 00                  mov edx, 1
002565C0  48 D3 C2                        rol rdx, cl
002565C3  48 8B DE                        mov rbx, rsi
002565C6  49 85 D6                        test r14, rdx
002565C9  0F 85 C9 00 00 00               jne 0x140256698
002565CF  41 FF C1                        inc r9d
002565D2  48 D1 C2                        rol rdx, 1
002565D5  48 FF C3                        inc rbx
002565D8  45 3B CB                        cmp r9d, r11d
002565DB  72 E9                           jb 0x1402565c6
002565DD  E9 75 FC FF FF                  jmp 0x140256257
002565E2  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
002565E7  BA 01 00 00 00                  mov edx, 1
002565EC  E9 5F FF FF FF                  jmp 0x140256550
002565F1  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
002565F6  41 8B D5                        mov edx, r13d
002565F9  49 8B CC                        mov rcx, r12
002565FC  E8 0F E3 1D 00                  call 0x140434910
00256601  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00256606  E9 75 FD FF FF                  jmp 0x140256380
0025660B  4D 8B CF                        mov r9, r15
0025660E  E9 2E FB FF FF                  jmp 0x140256141
00256613  83 F9 02                        cmp ecx, 2
00256616  0F 84 25 FC FF FF               je 0x140256241
0025661C  80 F9 01                        cmp cl, 1
0025661F  0F 85 29 FC FF FF               jne 0x14025624e
00256625  E9 17 FC FF FF                  jmp 0x140256241
0025662A  8B 05 E0 06 D7 00               mov eax, dword ptr [rip + 0xd706e0]
00256630  A8 02                           test al, 2
00256632  0F 84 16 FC FF FF               je 0x14025624e
00256638  E9 F1 FB FF FF                  jmp 0x14025622e
0025663D  41 3B FB                        cmp edi, r11d
00256640  73 45                           jae 0x140256687
00256642  48 8B CF                        mov rcx, rdi
00256645  BA 01 00 00 00                  mov edx, 1
0025664A  48 D3 C2                        rol rdx, cl
0025664D  0F 1F 00                        nop dword ptr [rax]
00256650  48 85 D5                        test rbp, rdx
00256653  74 1A                           je 0x14025666f
00256655  44 0F B6 0E                     movzx r9d, byte ptr [rsi]
00256659  41 8B C9                        mov ecx, r9d
0025665C  83 E1 7F                        and ecx, 0x7f
0025665F  41 3A C8                        cmp cl, r8b
00256662  7D 0B                           jge 0x14025666f
00256664  45 0F B6 C1                     movzx r8d, r9b
00256668  44 8B D7                        mov r10d, edi
0025666B  41 80 E0 7F                     and r8b, 0x7f
0025666F  FF C7                           inc edi
00256671  48 D1 C2                        rol rdx, 1
00256674  48 FF C6                        inc rsi
00256677  41 8B C2                        mov eax, r10d
0025667A  41 3B FB                        cmp edi, r11d
0025667D  72 D1                           jb 0x140256650
0025667F  85 C0                           test eax, eax
00256681  0F 89 D9 FB FF FF               jns 0x140256260
00256687  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
0025668C  4C 8D 05 AD 25 D7 00            lea r8, [rip + 0xd725ad]
00256693  E9 EF FB FF FF                  jmp 0x140256287
00256698  44 0F B6 23                     movzx r12d, byte ptr [rbx]
0025669C  41 8B CC                        mov ecx, r12d
0025669F  83 E1 7F                        and ecx, 0x7f
002566A2  41 3A C8                        cmp cl, r8b
002566A5  0F 8D 24 FF FF FF               jge 0x1402565cf
002566AB  45 0F B6 C4                     movzx r8d, r12b
002566AF  45 8B D1                        mov r10d, r9d
002566B2  41 80 E0 7F                     and r8b, 0x7f
002566B6  E9 14 FF FF FF                  jmp 0x1402565cf
002566BB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
002566C0  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002566C5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002566CA  B9 21 00 00 00                  mov ecx, 0x21
002566CF  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiHeteroSelectProcessorToPreempt(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 12273234)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_stack_m98 = a5;
    v_stack_mB8 = a4;
    v_stack_mB0 = a2;
    v_stack_mA0 = a1;
    v_stack_mA8 = *(unsigned __int64 *)(a2 + 192);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136))) >= (*(unsigned __int16 *)(a3))) goto loc_0025660B;
loc_00256141:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 8)) + (unsigned int)(*(unsigned int *)(a4 + 4)) * 2) * ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 192) + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(a4 + 16))));
    v_r14 = (*(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 192) + 192) + a3 + a3 * 2 * 8 + 8));
    v_r14 = (v_r14) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 192) + 192) + a3 + a3 * 2 * 8 + 16));
    v_rdi = (*(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 192) + 192) + a3 + a3 * 2 * 8 + 16));
    v_stack_mC0 = v_rdi;
    if (condition_is_equal) goto loc_002561A8;
    if (v_r14 == 0) goto loc_002561B7;
    v_stack_mC0 = v_rdi;
    if (v_r14 == v_rdi) goto loc_002561B7;
    v_stack_mC0 = v_rdi;
    goto loc_002561BA;
loc_002561A8:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 192) + 128)) & (*(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    v_stack_mC0 = v_rdi;
loc_002561B7:
loc_002561BA:
    v_rbp = (*(unsigned __int64 *)(a2 + 36416)) & (v_rdi);
    if (((v_rbp) & (v_rbp - 1)) == 0) goto loc_00256296;
    v_rsi = (v_stack_m88) + (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705));
    a2 = (*(unsigned __int64 *)(a2 + 36424)) + (576);
    result = memcpy(v_rsi, a2, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704))), *(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14093052)))) & (2)) != 0) goto loc_0025662A;
loc_0025622E:
    if (((unsigned int)(*(unsigned __int8 *)(v_stack_mA0 + 516) - 5)) > 1) goto loc_00256613;
loc_00256241:
    if ((*(unsigned int *)(v_rip + 14092836)) != 0) goto loc_0025648E;
loc_0025624E:
    if (0 != 0) goto loc_002565A3;
loc_00256257:
    if (sign_flag) goto loc_0025663D;
loc_00256260:
    a1 = (unsigned int)((*(unsigned __int8 *)(v_stack_mB0 + 208)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(0xFFFFFFFFULL))));
loc_00256287:
loc_00256296:
    result = *(unsigned __int64 *)(v_rip + 13422398);
    v_r12 = *(unsigned __int64 *)(v_rip + 14100948 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13422398) + a1 * 4)) * 8);
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14100948 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13422398) + a1 * 4)) * 8) + 200)) & (v_stack_mC0)) == 0) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14100948 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13422398) + a1 * 4)) * 8) + 209);
        result = v_stack_mC0;
        a2 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14100948 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13422398) + a1 * 4)) * 8) + 208);
        a2 = (unsigned int)((a2) << (6));
        a1 = (unsigned int)((a1) + ((unsigned int)(result)));
        v_stack_mB0 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 13422316);
        a1 = (unsigned int)((a1) & (63));
        a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
        a1 = *(unsigned int *)(result + a2 * 4);
        v_r12 = *(unsigned __int64 *)(v_rip + 14100948 + a1 * 8);
    }
    v_stack_m90 = v_r12;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + 56))))) >> (7));
    a2 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 20))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 20)))) < ((unsigned int)(result))) { a2 = (unsigned int)(result); }
    a1 = ((int)((unsigned int)(a2))) ^ (v_r12);
    a1 = (a1) & (-2);
    a1 = (a1) ^ ((int)((unsigned int)(a2)));
    v_stack_mC8 = a1;
    if ((unsigned int)(a2) == 0) goto loc_00256422;
    if (((unsigned int)(a2)) != 1) goto loc_00256373;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + 36440))) == 0) goto loc_00256373;
loc_0025632C:
loc_00256330:
loc_00256336:
    if (condition_is_above_or_equal) goto loc_0025635A;
loc_0025633F:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14085989)) & ((unsigned int)(v_rsi))) == 0) goto loc_002563FB;
loc_0025634D:
loc_0025634F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 36440) + 8) + 48) == 0) goto loc_00256336;
    goto loc_0025633F;
loc_0025635A:
    v_r14 = (*(unsigned __int64 *)(v_r12 + 36440) + 8) + (8);
    v_rbp = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_00256330;
loc_00256373:
    v_rbx = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + 56))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + 56))));
    if (sign_flag) goto loc_002565F1;
loc_00256380:
    a2 = (*(unsigned __int64 *)(v_stack_mA8 + 8)) & (v_stack_mC0);
    if (((a2) & (*(unsigned __int64 *)(v_stack_mA8 + (int)(*(unsigned int *)(v_stack_mB8 + 20)) * 8 + 16))) != 0) goto loc_00256431;
    *(unsigned int *)(v_stack_m98 + 8) = 0;
    if (((*(unsigned __int8 *)(v_r12 + 35)) & (16)) != 0) goto loc_00256511;
    result = KiIsIsolationUnitIdleByHandle(v_stack_mC8, a2, v_rip + 14100948, *(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    if ((unsigned int)(result) != 0) goto loc_002566BB;
loc_002563C0:
    *(unsigned __int64 *)(v_stack_m98) = v_stack_mC8;
    *(unsigned int *)(v_stack_m98 + 12) = 0;
loc_002563CC:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 14100948, *(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    v_rsp = (v_rsp) + (192);
    return result;
loc_002563FB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14091959)))) & (64)) == 0) goto loc_0025634D;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, v_rip + 14100948, *(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    if ((unsigned __int8)(result) == 0) goto loc_0025634D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_mB8)), a2, v_rip + 14100948, *(unsigned __int64 *)(a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 192) + 136) * 8 + 8));
    goto loc_0025634F;
loc_00256422:
    goto loc_0025632C;
loc_00256431:
    a3 = (v_stack_p30) & (-2);
    v_stack_p58 = a3;
    result = (unsigned int)((v_stack_p30) & (1));
    if (condition_is_equal) goto loc_00256502;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a3 + 36440);
        v_r15 = *(unsigned __int64 *)(a3 + 36440);
        v_r15 = (v_r15) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00256483;
loc_00256470:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00256470;
loc_00256483:
    goto loc_002563CC;
loc_0025648E:
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 192) + 328);
    if (((v_rbp) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 192) + 328))) == 0) goto loc_0025624E;
    if (((unsigned int)(v_stack_mC0)) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_0025624E;
loc_002564C5:
    result = (1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + 192) + 328));
    if (((v_rbp) & (result)) == 0) goto loc_002564EF;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_mB8)))) & (127));
    v_r10 = v_stack_mA8;
    if (((unsigned __int8)(a1)) < ((unsigned __int8)(a3))) {
        a3 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mB8));
        v_r10 = (unsigned int)((unsigned int)((unsigned int)(v_stack_mC0)));
        a3 = (unsigned __int8)((a3) & (127));
    }
loc_002564EF:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mC0))) + 1);
    v_rbx = (v_stack_mB8) + 1;
    if (((unsigned int)(a4)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_002564C5;
    goto loc_0025624E;
loc_00256502:
    goto loc_00256470;
loc_00256511:
    a4 = (v_stack_p30) & (-2);
    v_stack_p60 = a4;
    result = (unsigned int)((v_stack_p30) & (1));
    if (condition_is_equal) goto loc_002565E2;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00256562;
loc_00256550:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00256550;
loc_00256562:
    v_stack_p20 = v_stack_p30;
    v_stack_p30 = v_stack_p58;
    result = KiSelectCandidateProcessor(v_stack_p30, v_stack_p58, v_stack_mC0, (unsigned int)(*(unsigned int *)(v_stack_mB8 + 20)));
    result = KiIsIsolationUnitIdleByHandle(v_stack_p30, v_stack_p58, v_stack_mC0, (unsigned int)(*(unsigned int *)(v_stack_mB8 + 20)));
    if ((unsigned int)(result) == 0) goto loc_002563C0;
    *(unsigned int *)(v_rbx + 8) = 1;
    goto loc_002563C0;
loc_002565A3:
    if (!sign_flag) goto loc_00256260;
    if (((unsigned int)(v_stack_mC0)) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_00256687;
loc_002565C6:
    if (((v_stack_p68) & (1)) != 0) goto loc_00256698;
loc_002565CF:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mC0))) + 1);
    v_rbx = (v_stack_mB8) + 1;
    if (((unsigned int)(a4)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_002565C6;
    goto loc_00256257;
loc_002565E2:
    goto loc_00256550;
loc_002565F1:
    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath(v_stack_p30, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 20)))), v_stack_p30, a4);
    goto loc_00256380;
loc_0025660B:
    goto loc_00256141;
loc_00256613:
    if (((unsigned int)(v_stack_p30)) == 2) goto loc_00256241;
    if (((unsigned __int8)(v_stack_p30)) != 1) goto loc_0025624E;
    goto loc_00256241;
loc_0025662A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14092000)))) & (2)) == 0) goto loc_0025624E;
    goto loc_0025622E;
loc_0025663D:
    if (((unsigned int)(v_stack_mC0)) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_00256687;
loc_00256650:
    if (((v_rbp) & (1)) == 0) goto loc_0025666F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_mB8)))) & (127));
    v_r10 = v_stack_p50;
    if (((unsigned __int8)(a1)) < ((unsigned __int8)(v_stack_p30))) {
        a3 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mB8));
        v_r10 = (unsigned int)(v_stack_mC0);
        a3 = (unsigned __int8)((a3) & (127));
    }
    v_rdi = (unsigned int)((v_stack_mC0) + 1);
    v_rsi = (v_stack_mB8) + 1;
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 705) + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36424) + 704) * 1))) goto loc_00256650;
    if (!sign_flag) goto loc_00256260;
loc_00256687:
    goto loc_00256287;
loc_00256698:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx)))) & (127));
    if (((unsigned __int8)(a1)) >= ((unsigned __int8)(v_rip + 14099885))) goto loc_002565CF;
    a3 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) & (127));
    goto loc_002565CF;
loc_002566BB:
    v_stack_p40 = v_rdi;
    v_stack_p60 = v_stack_p40;
    return v_stack_p40;
}
```

## 5. (Beta) C Style

```c
int64_t KiHeteroSelectProcessorToPreempt(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0xBB4652)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    v_stack_m98 = Arg5;
    v_stack_mB8 = Arg4;
    v_stack_mB0 = Arg2;
    v_stack_mA0 = Arg1;
    v_stack_mA8 = *(uint64_t *)(arg2 + 0xC0);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88))) >= (*(uint16_t *)(arg3))) goto loc_0025660B;
loc_00256141:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + (uint32_t)(*(uint32_t *)(arg4 + 0x4)) * 2) * ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xC0) + 0xB9))));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(arg4 + 0x10))));
    local_r14 = (*(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xC0) + 0xC0) + arg3 + arg3 * 2 * 8 + 0x8));
    local_r14 = (local_r14) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xC0) + 0xC0) + arg3 + arg3 * 2 * 8 + 0x10));
    local_rdi = (*(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xC0) + 0xC0) + arg3 + arg3 * 2 * 8 + 0x10));
    v_stack_mC0 = local_rdi;
    if (condition_is_equal) goto loc_002561A8;
    if (local_r14 == 0) goto loc_002561B7;
    v_stack_mC0 = local_rdi;
    if (local_r14 == local_rdi) goto loc_002561B7;
    v_stack_mC0 = local_rdi;
    goto loc_002561BA;
loc_002561A8:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x80)) & (*(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    v_stack_mC0 = local_rdi;
loc_002561B7:
loc_002561BA:
    local_rbp = (*(uint64_t *)(arg2 + 0x8E40)) & (local_rdi);
    if (((local_rbp) & (local_rbp - 1)) == 0) goto loc_00256296;
    local_rsi = (v_stack_m88) + (*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1));
    Arg2 = (*(uint64_t *)(arg2 + 0x8E48)) + (576);
    result = memcpy(local_rsi, Arg2, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0))), *(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD70AFC)))) & (2)) != 0) goto loc_0025662A;
loc_0025622E:
    if (((uint32_t)(*(uint8_t *)(v_stack_mA0 + 0x204) - 5)) > 1) goto loc_00256613;
loc_00256241:
    if ((*(uint32_t *)(v_rip + 0xD70A24)) != 0) goto loc_0025648E;
loc_0025624E:
    if (0 != 0) goto loc_002565A3;
loc_00256257:
    if (sign_flag) goto loc_0025663D;
loc_00256260:
    Arg1 = (uint32_t)((*(uint8_t *)(v_stack_mB0 + 0xD0)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(0xFFFFFFFFULL))));
loc_00256287:
loc_00256296:
    result = *(uint64_t *)(v_rip + 0xCCCF3E);
    local_r12 = *(uint64_t *)(v_rip + 0xD729D4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCCF3E) + Arg1 * 4)) * 8);
    if (((*(uint64_t *)(*(uint64_t *)(v_rip + 0xD729D4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCCF3E) + Arg1 * 4)) * 8) + 0xC8)) & (v_stack_mC0)) == 0) {
        Arg1 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD729D4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCCF3E) + Arg1 * 4)) * 8) + 0xD1);
        result = v_stack_mC0;
        Arg2 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD729D4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCCF3E) + Arg1 * 4)) * 8) + 0xD0);
        Arg2 = (uint32_t)((Arg2) << (6));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
        v_stack_mB0 = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0xCCCEEC);
        Arg1 = (uint32_t)((Arg1) & (63));
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
        Arg1 = *(uint32_t *)(result + arg2 * 4);
        local_r12 = *(uint64_t *)(v_rip + 0xD729D4 + Arg1 * 8);
    }
    v_stack_m90 = local_r12;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 + 0x38))))) >> (7));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x14))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x14)))) < ((uint32_t)(result))) { Arg2 = (uint32_t)(result); }
    Arg1 = ((int32_t)((uint32_t)(Arg2))) ^ (local_r12);
    Arg1 = (Arg1) & (-2);
    Arg1 = (Arg1) ^ ((int32_t)((uint32_t)(Arg2)));
    v_stack_mC8 = Arg1;
    if ((uint32_t)(Arg2) == 0) goto loc_00256422;
    if (((uint32_t)(Arg2)) != 1) goto loc_00256373;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 + 0x8E58))) == 0) goto loc_00256373;
loc_0025632C:
loc_00256330:
loc_00256336:
    if (condition_is_above_or_equal) goto loc_0025635A;
loc_0025633F:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD6EF65)) & ((uint32_t)(local_rsi))) == 0) goto loc_002563FB;
loc_0025634D:
loc_0025634F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12 + 0x8E58) + 0x8) + 0x30) == 0) goto loc_00256336;
    goto loc_0025633F;
loc_0025635A:
    local_r14 = (*(uint64_t *)(local_r12 + 0x8E58) + 8) + (8);
    local_rbp = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_00256330;
loc_00256373:
    local_rbx = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r12 + 0x38))) ^ (*(uint8_t *)(*(uint64_t *)(local_r12 + 0x38))));
    if (sign_flag) goto loc_002565F1;
loc_00256380:
    Arg2 = (*(uint64_t *)(v_stack_mA8 + 0x8)) & (v_stack_mC0);
    if (((Arg2) & (*(uint64_t *)(v_stack_mA8 + (int32_t)(*(uint32_t *)(v_stack_mB8 + 0x14)) * 8 + 0x10))) != 0) goto loc_00256431;
    *(uint32_t *)(v_stack_m98 + 0x8) = 0;
    if (((*(uint8_t *)(local_r12 + 0x23)) & (16)) != 0) goto loc_00256511;
    result = KiIsIsolationUnitIdleByHandle(v_stack_mC8, Arg2, v_rip + 14100948, *(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    if ((uint32_t)(result) != 0) goto loc_002566BB;
loc_002563C0:
    *(uint64_t *)(v_stack_m98) = v_stack_mC8;
    *(uint32_t *)(v_stack_m98 + 0xC) = 0;
loc_002563CC:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 14100948, *(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    local_rsp = (local_rsp) + (192);
    return result;
loc_002563FB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD706B7)))) & (64)) == 0) goto loc_0025634D;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, v_rip + 14100948, *(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    if ((uint8_t)(result) == 0) goto loc_0025634D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_mB8)), Arg2, v_rip + 14100948, *(uint64_t *)(arg3 + *(uint16_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x88) * 8 + 0x8));
    goto loc_0025634F;
loc_00256422:
    goto loc_0025632C;
loc_00256431:
    Arg3 = (v_stack_p30) & (-2);
    v_stack_p58 = Arg3;
    result = (uint32_t)((v_stack_p30) & (1));
    if (condition_is_equal) goto loc_00256502;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(arg3 + 0x8E58);
        local_r15 = *(uint64_t *)(arg3 + 0x8E58);
        local_r15 = (local_r15) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00256483;
loc_00256470:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00256470;
loc_00256483:
    goto loc_002563CC;
loc_0025648E:
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(local_r12 + 0xC0) + 0x148);
    if (((local_rbp) & (*(uint64_t *)(*(uint64_t *)(local_r12 + 0xC0) + 0x148))) == 0) goto loc_0025624E;
    if (((uint32_t)(v_stack_mC0)) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_0025624E;
loc_002564C5:
    result = (1) & (*(uint64_t *)(*(uint64_t *)(local_r12 + 0xC0) + 0x148));
    if (((local_rbp) & (result)) == 0) goto loc_002564EF;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_mB8)))) & (127));
    local_r10 = v_stack_mA8;
    if (((uint8_t)(Arg1)) < ((uint8_t)(Arg3))) {
        Arg3 = (uint8_t)(*(uint8_t *)(v_stack_mB8));
        local_r10 = (uint32_t)((uint32_t)((uint32_t)(v_stack_mC0)));
        Arg3 = (uint8_t)((Arg3) & (127));
    }
loc_002564EF:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mC0))) + 1);
    local_rbx = (v_stack_mB8) + 1;
    if (((uint32_t)(Arg4)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_002564C5;
    goto loc_0025624E;
loc_00256502:
    goto loc_00256470;
loc_00256511:
    Arg4 = (v_stack_p30) & (-2);
    v_stack_p60 = Arg4;
    result = (uint32_t)((v_stack_p30) & (1));
    if (condition_is_equal) goto loc_002565E2;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00256562;
loc_00256550:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00256550;
loc_00256562:
    v_stack_p20 = v_stack_p30;
    v_stack_p30 = v_stack_p58;
    result = KiSelectCandidateProcessor(v_stack_p30, v_stack_p58, v_stack_mC0, (uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x14)));
    result = KiIsIsolationUnitIdleByHandle(v_stack_p30, v_stack_p58, v_stack_mC0, (uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x14)));
    if ((uint32_t)(result) == 0) goto loc_002563C0;
    *(uint32_t *)(local_rbx + 0x8) = 1;
    goto loc_002563C0;
loc_002565A3:
    if (!sign_flag) goto loc_00256260;
    if (((uint32_t)(v_stack_mC0)) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_00256687;
loc_002565C6:
    if (((v_stack_p68) & (1)) != 0) goto loc_00256698;
loc_002565CF:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mC0))) + 1);
    local_rbx = (v_stack_mB8) + 1;
    if (((uint32_t)(Arg4)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_002565C6;
    goto loc_00256257;
loc_002565E2:
    goto loc_00256550;
loc_002565F1:
    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath(v_stack_p30, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x14)))), v_stack_p30, Arg4);
    goto loc_00256380;
loc_0025660B:
    goto loc_00256141;
loc_00256613:
    if (((uint32_t)(v_stack_p30)) == 2) goto loc_00256241;
    if (((uint8_t)(v_stack_p30)) != 1) goto loc_0025624E;
    goto loc_00256241;
loc_0025662A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD706E0)))) & (2)) == 0) goto loc_0025624E;
    goto loc_0025622E;
loc_0025663D:
    if (((uint32_t)(v_stack_mC0)) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_00256687;
loc_00256650:
    if (((local_rbp) & (1)) == 0) goto loc_0025666F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_mB8)))) & (127));
    local_r10 = v_stack_p50;
    if (((uint8_t)(Arg1)) < ((uint8_t)(v_stack_p30))) {
        Arg3 = (uint8_t)(*(uint8_t *)(v_stack_mB8));
        local_r10 = (uint32_t)(v_stack_mC0);
        Arg3 = (uint8_t)((Arg3) & (127));
    }
    local_rdi = (uint32_t)((v_stack_mC0) + 1);
    local_rsi = (v_stack_mB8) + 1;
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C1) + *(uint8_t *)(*(uint64_t *)(arg2 + 0x8E48) + 0x2C0) * 1))) goto loc_00256650;
    if (!sign_flag) goto loc_00256260;
loc_00256687:
    goto loc_00256287;
loc_00256698:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx)))) & (127));
    if (((uint8_t)(Arg1)) >= ((uint8_t)(v_rip + 14099885))) goto loc_002565CF;
    Arg3 = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rbx))) & (127));
    goto loc_002565CF;
loc_002566BB:
    v_stack_p40 = local_rdi;
    v_stack_p60 = v_stack_p40;
    return v_stack_p40;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0x8E40` | `64` | `R` |
| `Arg2` | `+ 0x8E48` | `64` | `R` |
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x8 + rax*8` | `64` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002560D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
