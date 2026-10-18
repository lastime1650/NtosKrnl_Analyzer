# KiEndThreadCycleAccumulation

- RVA: `0x0037BFF0`–`0x0037CB85` (길이 `2,965` bytes)
- VA: `0x000000014037BFF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B1E0`
- 디코드: `697`개 명령, `2,965/2,965` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x0037C3B9` → [KiUpdateThreadHgsFeedback](KiUpdateThreadHgsFeedback_function_0037D790.md) (function, `0x0037D790`)
- `0x0037C443` → [KiEndCounterAccumulation](KiEndCounterAccumulation_function_0037EEAC.md) (function, `0x0037EEAC`)
- `0x0037C6A2` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037C767` → [HalpTimerScaleCounter](HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0037C798` → [HalpTimerScaleCounter](HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0037C7C1` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037C7D6` → [HalpHpetQueryCounter](HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0037C90E` → [HvlpGetRegister64](HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0037C95E` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037C973` → [HalpHpetQueryCounter](HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0037CA3E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037CA87` → [HvlpGetRegister64](HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0037CAA7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037CB43` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037CB54` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037CB6A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [KiStartInterruptCycleAccumulation](KiStartInterruptCycleAccumulation_function_0037B410.md) at `0x0037B431`
- [PpmCheckCustomRun](../3B/PpmCheckCustomRun_function_003BEC2C.md) at `0x003BEC6E`
- [KeUpdateThreadTag](../47/KeUpdateThreadTag_function_00475770.md) at `0x00475817`

### Static image references
- `0x0037C031` → RVA `0x00FC3FD0` (`.data`; read)
- `0x0037C04C` → RVA `0x00FC40E0` (`.data`; read)
- `0x0037C075` → RVA `0x0041FD10` (`HalpTscQueryCounterOrdered`; read)
- `0x0037C0B8` → RVA `0x00FC3FC8` (`.data`; read)
- `0x0037C0F8` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x0037C153` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x0037C167` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x0037C2EB` → RVA `0x00F10A44` (`.data`; read)
- `0x0037C311` → RVA `0x00FC6D60` (`ALMOSTRO`; read)
- `0x0037C3A2` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x0037C3BE` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x0037C4CB` → RVA `0x00378F50` (`HalpHvCounterQueryCounter`; read)
- `0x0037C4DB` → RVA `0x00E11760` (`.data`; read)
- `0x0037C4EB` → RVA `0x002DDBC0` (`HvlGetReferenceTimeUsingTscPage`; read)
- `0x0037C50D` → RVA `0x00FC6D88` (`ALMOSTRO`; read)
- `0x0037C7B0` → RVA `0x00379660` (`HalpHpetQueryCounter`; read)
- `0x0037CADC` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0037CAEA` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0037BFF0  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0037BFF5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0037BFFA  55                              push rbp
0037BFFB  53                              push rbx
0037BFFC  56                              push rsi
0037BFFD  57                              push rdi
0037BFFE  41 54                           push r12
0037C000  41 55                           push r13
0037C002  41 56                           push r14
0037C004  41 57                           push r15
0037C006  48 8B EC                        mov rbp, rsp
0037C009  48 83 EC 68                     sub rsp, 0x68
0037C00D  45 33 E4                        xor r12d, r12d
0037C010  C6 41 20 01                     mov byte ptr [rcx + 0x20], 1
0037C014  90                              nop
0037C015  4C 8B F2                        mov r14, rdx
0037C018  48 8B F1                        mov rsi, rcx
0037C01B  45 8B DC                        mov r11d, r12d
0037C01E  45 8B FC                        mov r15d, r12d
0037C021  41 8B FC                        mov edi, r12d
0037C024  44 38 A1 DC 86 00 00            cmp byte ptr [rcx + 0x86dc], r12b
0037C02B  0F 84 66 01 00 00               je 0x14037c197
0037C031  4C 8B 3D 98 7F C4 00            mov r15, qword ptr [rip + 0xc47f98]
0037C038  41 B9 80 96 98 00               mov r9d, 0x989680
0037C03E  41 83 BF E4 00 00 00 05         cmp dword ptr [r15 + 0xe4], 5
0037C046  0F 85 51 04 00 00               jne 0x14037c49d
0037C04C  4C 39 25 8D 80 C4 00            cmp qword ptr [rip + 0xc4808d], r12
0037C053  41 8B D9                        mov ebx, r9d
0037C056  0F 84 35 06 00 00               je 0x14037c691
0037C05C  41 F7 87 E0 00 00 00 00 00 01 00  test dword ptr [r15 + 0xe0], 0x10000
0037C067  0F 85 D9 07 00 00               jne 0x14037c846
0037C06D  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
0037C071  49 8B 47 70                     mov rax, qword ptr [r15 + 0x70]
0037C075  48 8D 15 94 3C 0A 00            lea rdx, [rip + 0xa3c94]
0037C07C  48 3B C2                        cmp rax, rdx
0037C07F  0F 85 CF 0A 00 00               jne 0x14037cb54
0037C085  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
0037C089  0F 01 F9                        rdtscp
0037C08C  4C 8D 45 50                     lea r8, [rbp + 0x50]
0037C090  48 C1 E2 20                     shl rdx, 0x20
0037C094  41 89 08                        mov dword ptr [r8], ecx
0037C097  48 0B D0                        or rdx, rax
0037C09A  48 8B 05 3F 80 C4 00            mov rax, qword ptr [rip + 0xc4803f]
0037C0A1  48 B9 B8 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff780000003b8
0037C0AB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0037C0AF  4C 8B 19                        mov r11, qword ptr [rcx]
0037C0B2  48 F7 E2                        mul rdx
0037C0B5  4C 03 DA                        add r11, rdx
0037C0B8  48 8B 05 09 7F C4 00            mov rax, qword ptr [rip + 0xc47f09]
0037C0BF  4C 3B F8                        cmp r15, rax
0037C0C2  0F 85 AF 06 00 00               jne 0x14037c777
0037C0C8  0F B6 8E AC 00 00 00            movzx ecx, byte ptr [rsi + 0xac]
0037C0CF  49 8B D3                        mov rdx, r11
0037C0D2  48 8B 86 B0 00 00 00            mov rax, qword ptr [rsi + 0xb0]
0037C0D9  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
0037C0DD  84 C9                           test cl, cl
0037C0DF  74 03                           je 0x14037c0e4
0037C0E1  48 D3 E2                        shl rdx, cl
0037C0E4  48 F7 E2                        mul rdx
0037C0E7  48 8B FA                        mov rdi, rdx
0037C0EA  48 89 55 E8                     mov qword ptr [rbp - 0x18], rdx
0037C0EE  48 2B BE 80 86 00 00            sub rdi, qword ptr [rsi + 0x8680]
0037C0F5  4C 8B FA                        mov r15, rdx
0037C0F8  44 38 25 96 A9 C4 00            cmp byte ptr [rip + 0xc4a996], r12b
0037C0FF  0F 84 92 00 00 00               je 0x14037c197
0037C105  48 8B 96 F8 86 00 00            mov rdx, qword ptr [rsi + 0x86f8]
0037C10C  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0037C116  4C 39 20                        cmp qword ptr [rax], r12
0037C119  74 7C                           je 0x14037c197
0037C11B  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0037C124  49 B9 60 03 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000360
0037C12E  0F B6 C8                        movzx ecx, al
0037C131  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0037C135  84 C0                           test al, al
0037C137  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0037C13B  4D 8B C3                        mov r8, r11
0037C13E  4D 8B 09                        mov r9, qword ptr [r9]
0037C141  49 8B C1                        mov rax, r9
0037C144  0F 84 3F 05 00 00               je 0x14037c689
0037C14A  48 D3 E2                        shl rdx, cl
0037C14D  48 F7 E2                        mul rdx
0037C150  49 D3 E0                        shl r8, cl
0037C153  0F BE 0D 6C AA C4 00            movsx ecx, byte ptr [rip + 0xc4aa6c]
0037C15A  4C 8B D2                        mov r10, rdx
0037C15D  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
0037C161  49 8B C1                        mov rax, r9
0037C164  49 F7 E0                        mul r8
0037C167  48 8B 05 AA B1 C4 00            mov rax, qword ptr [rip + 0xc4b1aa]
0037C16E  4C 8B CA                        mov r9, rdx
0037C171  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
0037C175  49 F7 E2                        mul r10
0037C178  48 8B 05 99 B1 C4 00            mov rax, qword ptr [rip + 0xc4b199]
0037C17F  4C 8B D2                        mov r10, rdx
0037C182  49 F7 E1                        mul r9
0037C185  49 D3 EA                        shr r10, cl
0037C188  4C 8B C2                        mov r8, rdx
0037C18B  49 D3 E8                        shr r8, cl
0037C18E  45 2B C2                        sub r8d, r10d
0037C191  0F 85 EB 03 00 00               jne 0x14037c582
0037C197  4C 89 9E F8 86 00 00            mov qword ptr [rsi + 0x86f8], r11
0037C19E  4C 89 BE 80 86 00 00            mov qword ptr [rsi + 0x8680], r15
0037C1A5  4D 8B 6E 48                     mov r13, qword ptr [r14 + 0x48]
0037C1A9  4C 03 EF                        add r13, rdi
0037C1AC  4D 89 6E 48                     mov qword ptr [r14 + 0x48], r13
0037C1B0  4C 3B 76 18                     cmp r14, qword ptr [rsi + 0x18]
0037C1B4  74 25                           je 0x14037c1db
0037C1B6  8B 86 B8 86 00 00               mov eax, dword ptr [rsi + 0x86b8]
0037C1BC  41 8B 4E 50                     mov ecx, dword ptr [r14 + 0x50]
0037C1C0  48 0F AF C7                     imul rax, rdi
0037C1C4  48 C1 E8 10                     shr rax, 0x10
0037C1C8  48 03 C8                        add rcx, rax
0037C1CB  B8 FF FF FF FF                  mov eax, 0xffffffff
0037C1D0  48 3B C8                        cmp rcx, rax
0037C1D3  48 0F 47 C8                     cmova rcx, rax
0037C1D7  41 89 4E 50                     mov dword ptr [r14 + 0x50], ecx
0037C1DB  41 0F B6 5E 02                  movzx ebx, byte ptr [r14 + 2]
0037C1E0  F6 C3 BE                        test bl, 0xbe
0037C1E3  0F 84 F7 01 00 00               je 0x14037c3e0
0037C1E9  41 BB 01 00 00 00               mov r11d, 1
0037C1EF  84 DB                           test bl, bl
0037C1F1  79 52                           jns 0x14037c245
0037C1F3  49 8B 86 20 02 00 00            mov rax, qword ptr [r14 + 0x220]
0037C1FA  41 8B D3                        mov edx, r11d
0037C1FD  4C 8B 86 B0 8B 00 00            mov r8, qword ptr [rsi + 0x8bb0]
0037C204  44 8B 88 90 01 00 00            mov r9d, dword ptr [rax + 0x190]
0037C20B  41 8B C1                        mov eax, r9d
0037C20E  C1 E8 0D                        shr eax, 0xd
0037C211  25 FF FF 03 00                  and eax, 0x3ffff
0037C216  49 C1 E9 04                     shr r9, 4
0037C21A  0F BD C8                        bsr ecx, eax
0037C21D  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0037C224  D3 E2                           shl edx, cl
0037C226  83 C1 FE                        add ecx, -2
0037C229  33 D0                           xor edx, eax
0037C22B  89 4D BC                        mov dword ptr [rbp - 0x44], ecx
0037C22E  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0037C232  48 8B 54 D1 08                  mov rdx, qword ptr [rcx + rdx*8 + 8]
0037C237  4A 8B 04 CA                     mov rax, qword ptr [rdx + r9*8]
0037C23B  48 03 C7                        add rax, rdi
0037C23E  4A 89 04 CA                     mov qword ptr [rdx + r9*8], rax
0037C242  80 E3 7F                        and bl, 0x7f
0037C245  F6 C3 10                        test bl, 0x10
0037C248  0F 85 14 02 00 00               jne 0x14037c462
0037C24E  F6 C3 20                        test bl, 0x20
0037C251  0F 84 42 01 00 00               je 0x14037c399
0037C257  4D 8B 86 88 06 00 00            mov r8, qword ptr [r14 + 0x688]
0037C25E  4D 85 C0                        test r8, r8
0037C261  0F 84 2F 01 00 00               je 0x14037c396
0037C267  48 8B 86 B0 89 00 00            mov rax, qword ptr [rsi + 0x89b0]
0037C26E  48 8B 96 B8 89 00 00            mov rdx, qword ptr [rsi + 0x89b8]
0037C275  48 85 C0                        test rax, rax
0037C278  0F 84 FD 08 00 00               je 0x14037cb7b
0037C27E  48 85 D2                        test rdx, rdx
0037C281  0F 84 F4 08 00 00               je 0x14037cb7b
0037C287  44 38 62 70                     cmp byte ptr [rdx + 0x70], r12b
0037C28B  75 11                           jne 0x14037c29e
0037C28D  8B 52 50                        mov edx, dword ptr [rdx + 0x50]
0037C290  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
0037C296  3B D1                           cmp edx, ecx
0037C298  72 0A                           jb 0x14037c2a4
0037C29A  8B D1                           mov edx, ecx
0037C29C  EB 06                           jmp 0x14037c2a4
0037C29E  8B 92 84 00 00 00               mov edx, dword ptr [rdx + 0x84]
0037C2A4  45 8B CC                        mov r9d, r12d
0037C2A7  48 8D 8E 6A 8A 00 00            lea rcx, [rsi + 0x8a6a]
0037C2AE  0F B7 01                        movzx eax, word ptr [rcx]
0037C2B1  3B D0                           cmp edx, eax
0037C2B3  76 0D                           jbe 0x14037c2c2
0037C2B5  41 FF C1                        inc r9d
0037C2B8  48 83 C1 02                     add rcx, 2
0037C2BC  41 83 F9 03                     cmp r9d, 3
0037C2C0  72 EC                           jb 0x14037c2ae
0037C2C2  44 0F B6 96 08 8A 00 00         movzx r10d, byte ptr [rsi + 0x8a08]
0037C2CA  41 0F B6 C2                     movzx eax, r10b
0037C2CE  41 8B C9                        mov ecx, r9d
0037C2D1  48 03 C9                        add rcx, rcx
0037C2D4  F6 D8                           neg al
0037C2D6  48 1B D2                        sbb rdx, rdx
0037C2D9  49 8D 04 C8                     lea rax, [r8 + rcx*8]
0037C2DD  83 E2 08                        and edx, 8
0037C2E0  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0037C2E4  48 03 CF                        add rcx, rdi
0037C2E7  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0037C2EB  8B 05 53 47 B9 00               mov eax, dword ptr [rip + 0xb94753]
0037C2F1  41 8B 88 C0 00 00 00            mov ecx, dword ptr [r8 + 0xc0]
0037C2F8  3B C1                           cmp eax, ecx
0037C2FA  0F 87 56 03 00 00               ja 0x14037c656
0037C300  2B C8                           sub ecx, eax
0037C302  83 F9 20                        cmp ecx, 0x20
0037C305  73 0A                           jae 0x14037c311
0037C307  41 D3 E3                        shl r11d, cl
0037C30A  45 09 98 C4 00 00 00            or dword ptr [r8 + 0xc4], r11d
0037C311  44 39 25 48 AA C4 00            cmp dword ptr [rip + 0xc4aa48], r12d
0037C318  75 1F                           jne 0x14037c339
0037C31A  41 0F B6 8E 04 02 00 00         movzx ecx, byte ptr [r14 + 0x204]
0037C322  8D 41 FE                        lea eax, [rcx - 2]
0037C325  A9 FB FF FF FF                  test eax, 0xfffffffb
0037C32A  0F 84 1A 01 00 00               je 0x14037c44a
0037C330  80 F9 05                        cmp cl, 5
0037C333  0F 84 11 01 00 00               je 0x14037c44a
0037C339  4D 39 A6 50 06 00 00            cmp qword ptr [r14 + 0x650], r12
0037C340  74 54                           je 0x14037c396
0037C342  41 0F B6 C2                     movzx eax, r10b
0037C346  41 8B C9                        mov ecx, r9d
0037C349  48 83 C1 08                     add rcx, 8
0037C34D  48 03 C9                        add rcx, rcx
0037C350  F6 D8                           neg al
0037C352  48 1B D2                        sbb rdx, rdx
0037C355  83 E2 08                        and edx, 8
0037C358  49 8D 04 C8                     lea rax, [r8 + rcx*8]
0037C35C  41 B8 48 00 00 00               mov r8d, 0x48
0037C362  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0037C366  48 03 CF                        add rcx, rdi
0037C369  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0037C36D  BA 40 00 00 00                  mov edx, 0x40
0037C372  49 8B 86 50 06 00 00            mov rax, qword ptr [r14 + 0x650]
0037C379  48 8B 88 88 06 00 00            mov rcx, qword ptr [rax + 0x688]
0037C380  41 8B C1                        mov eax, r9d
0037C383  48 C1 E0 04                     shl rax, 4
0037C387  45 84 D2                        test r10b, r10b
0037C38A  41 0F 45 D0                     cmovne edx, r8d
0037C38E  48 03 C1                        add rax, rcx
0037C391  F0 48 01 3C 02                  lock add qword ptr [rdx + rax], rdi
0037C396  80 E3 DF                        and bl, 0xdf
0037C399  F6 C3 40                        test bl, 0x40
0037C39C  0F 85 E2 00 00 00               jne 0x14037c484
0037C3A2  44 38 25 35 A7 C4 00            cmp byte ptr [rip + 0xc4a735], r12b
0037C3A9  74 13                           je 0x14037c3be
0037C3AB  44 0F B6 4D 60                  movzx r9d, byte ptr [rbp + 0x60]
0037C3B0  4C 8B C7                        mov r8, rdi
0037C3B3  49 8B D6                        mov rdx, r14
0037C3B6  48 8B CE                        mov rcx, rsi
0037C3B9  E8 D2 13 00 00                  call 0x14037d790
0037C3BE  4C 8D 05 3B 3B C5 00            lea r8, [rip + 0xc53b3b]
0037C3C5  4C 39 A6 B0 86 00 00            cmp qword ptr [rsi + 0x86b0], r12
0037C3CC  74 0D                           je 0x14037c3db
0037C3CE  4D 39 86 20 02 00 00            cmp qword ptr [r14 + 0x220], r8
0037C3D5  0F 85 D9 06 00 00               jne 0x14037cab4
0037C3DB  F6 C3 BE                        test bl, 0xbe
0037C3DE  75 21                           jne 0x14037c401
0037C3E0  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0037C3E4  48 85 C0                        test rax, rax
0037C3E7  74 03                           je 0x14037c3ec
0037C3E9  4C 89 38                        mov qword ptr [rax], r15
0037C3EC  49 8B C5                        mov rax, r13
0037C3EF  48 83 C4 68                     add rsp, 0x68
0037C3F3  41 5F                           pop r15
0037C3F5  41 5E                           pop r14
0037C3F7  41 5D                           pop r13
0037C3F9  41 5C                           pop r12
0037C3FB  5F                              pop rdi
0037C3FC  5E                              pop rsi
0037C3FD  5B                              pop rbx
0037C3FE  5D                              pop rbp
0037C3FF  C3                              ret
0037C400  CC                              int3
0037C401  49 8B 4E 68                     mov rcx, qword ptr [r14 + 0x68]
0037C405  48 85 C9                        test rcx, rcx
0037C408  74 18                           je 0x14037c422
0037C40A  8B 86 D8 00 00 00               mov eax, dword ptr [rsi + 0xd8]
0037C410  48 03 C1                        add rax, rcx
0037C413  48 01 38                        add qword ptr [rax], rdi
0037C416  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
0037C41D  48 85 C0                        test rax, rax
0037C420  75 F1                           jne 0x14037c413
0037C422  41 F6 46 02 08                  test byte ptr [r14 + 2], 8
0037C427  74 0D                           je 0x14037c436
0037C429  4D 39 86 20 02 00 00            cmp qword ptr [r14 + 0x220], r8
0037C430  0F 85 CD 06 00 00               jne 0x14037cb03
0037C436  49 83 BE 68 01 00 00 00         cmp qword ptr [r14 + 0x168], 0
0037C43E  74 A0                           je 0x14037c3e0
0037C440  49 8B CE                        mov rcx, r14
0037C443  E8 64 2A 00 00                  call 0x14037eeac
0037C448  EB 96                           jmp 0x14037c3e0
0037C44A  41 8B D1                        mov edx, r9d
0037C44D  48 03 D2                        add rdx, rdx
0037C450  49 8B 4C D0 08                  mov rcx, qword ptr [r8 + rdx*8 + 8]
0037C455  48 03 CF                        add rcx, rdi
0037C458  49 89 4C D0 08                  mov qword ptr [r8 + rdx*8 + 8], rcx
0037C45D  E9 D7 FE FF FF                  jmp 0x14037c339
0037C462  41 0F B6 46 7C                  movzx eax, byte ptr [r14 + 0x7c]
0037C467  48 8D 14 C6                     lea rdx, [rsi + rax*8]
0037C46B  48 8B 8A 88 86 00 00            mov rcx, qword ptr [rdx + 0x8688]
0037C472  48 03 CF                        add rcx, rdi
0037C475  48 89 8A 88 86 00 00            mov qword ptr [rdx + 0x8688], rcx
0037C47C  80 E3 EF                        and bl, 0xef
0037C47F  E9 CA FD FF FF                  jmp 0x14037c24e
0037C484  49 8B 86 C8 03 00 00            mov rax, qword ptr [r14 + 0x3c8]
0037C48B  48 85 C0                        test rax, rax
0037C48E  0F 84 0E FF FF FF               je 0x14037c3a2
0037C494  44 88 60 40                     mov byte ptr [rax + 0x40], r12b
0037C498  E9 05 FF FF FF                  jmp 0x14037c3a2
0037C49D  41 83 BF DC 00 00 00 40         cmp dword ptr [r15 + 0xdc], 0x40
0037C4A5  49 8B 9F C0 00 00 00            mov rbx, qword ptr [r15 + 0xc0]
0037C4AC  0F 85 F3 02 00 00               jne 0x14037c7a5
0037C4B2  41 F7 87 E0 00 00 00 00 00 01 00  test dword ptr [r15 + 0xe0], 0x10000
0037C4BD  0F 85 0E 04 00 00               jne 0x14037c8d1
0037C4C3  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
0037C4C7  49 8B 57 70                     mov rdx, qword ptr [r15 + 0x70]
0037C4CB  48 8D 05 7E CA FF FF            lea rax, [rip - 0x3582]
0037C4D2  48 3B D0                        cmp rdx, rax
0037C4D5  0F 85 60 05 00 00               jne 0x14037ca3b
0037C4DB  48 8B 05 7E 52 A9 00            mov rax, qword ptr [rip + 0xa9527e]
0037C4E2  48 85 C0                        test rax, rax
0037C4E5  0F 84 44 04 00 00               je 0x14037c92f
0037C4EB  48 8D 0D CE 16 F6 FF            lea rcx, [rip - 0x9e932]
0037C4F2  48 3B C1                        cmp rax, rcx
0037C4F5  0F 85 79 06 00 00               jne 0x14037cb74
0037C4FB  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
0037C4FF  49 BA 94 02 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000294
0037C509  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
0037C50D  48 8B 05 74 A8 C4 00            mov rax, qword ptr [rip + 0xc4a874]
0037C514  44 8B 08                        mov r9d, dword ptr [rax]
0037C517  45 85 C9                        test r9d, r9d
0037C51A  0F 84 E5 03 00 00               je 0x14037c905
0037C520  41 38 3A                        cmp byte ptr [r10], dil
0037C523  0F 84 C0 03 00 00               je 0x14037c8e9
0037C529  0F 01 F9                        rdtscp
0037C52C  4C 8D 45 B8                     lea r8, [rbp - 0x48]
0037C530  41 89 08                        mov dword ptr [r8], ecx
0037C533  48 C1 E2 20                     shl rdx, 0x20
0037C537  48 0B D0                        or rdx, rax
0037C53A  48 8B 05 47 A8 C4 00            mov rax, qword ptr [rip + 0xc4a847]
0037C541  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0037C545  48 8B 0D 3C A8 C4 00            mov rcx, qword ptr [rip + 0xc4a83c]
0037C54C  48 F7 E2                        mul rdx
0037C54F  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0037C553  48 8B 05 2E A8 C4 00            mov rax, qword ptr [rip + 0xc4a82e]
0037C55A  49 03 D0                        add rdx, r8
0037C55D  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0037C561  8B 08                           mov ecx, dword ptr [rax]
0037C563  41 3B C9                        cmp ecx, r9d
0037C566  75 A5                           jne 0x14037c50d
0037C568  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0037C56C  4D 8B AF D0 00 00 00            mov r13, qword ptr [r15 + 0xd0]
0037C573  41 B9 80 96 98 00               mov r9d, 0x989680
0037C579  4E 8D 1C 2A                     lea r11, [rdx + r13]
0037C57D  E9 36 FB FF FF                  jmp 0x14037c0b8
0037C582  41 F7 46 74 00 04 00 00         test dword ptr [r14 + 0x74], 0x400
0037C58A  75 1E                           jne 0x14037c5aa
0037C58C  41 8B 86 4C 04 00 00            mov eax, dword ptr [r14 + 0x44c]
0037C593  F3 48 0F B8 D0                  popcnt rdx, rax
0037C598  49 8B C3                        mov rax, r11
0037C59B  48 C1 E8 04                     shr rax, 4
0037C59F  83 E0 1F                        and eax, 0x1f
0037C5A2  3B C2                           cmp eax, edx
0037C5A4  0F 82 99 00 00 00               jb 0x14037c643
0037C5AA  44 01 86 44 86 00 00            add dword ptr [rsi + 0x8644], r8d
0037C5B1  45 01 86 8C 02 00 00            add dword ptr [r14 + 0x28c], r8d
0037C5B8  4C 3B 76 18                     cmp r14, qword ptr [rsi + 0x18]
0037C5BC  0F 84 D5 FB FF FF               je 0x14037c197
0037C5C2  49 8D 96 C3 00 00 00            lea rdx, [r14 + 0xc3]
0037C5C9  80 3A 10                        cmp byte ptr [rdx], 0x10
0037C5CC  7D 60                           jge 0x14037c62e
0037C5CE  49 8B 46 68                     mov rax, qword ptr [r14 + 0x68]
0037C5D2  48 85 C0                        test rax, rax
0037C5D5  74 57                           je 0x14037c62e
0037C5D7  49 8B 46 68                     mov rax, qword ptr [r14 + 0x68]
0037C5DB  48 85 C0                        test rax, rax
0037C5DE  74 4E                           je 0x14037c62e
0037C5E0  8B 8E D8 00 00 00               mov ecx, dword ptr [rsi + 0xd8]
0037C5E6  45 8B CC                        mov r9d, r12d
0037C5E9  48 03 C8                        add rcx, rax
0037C5EC  80 3A 10                        cmp byte ptr [rdx], 0x10
0037C5EF  7D 36                           jge 0x14037c627
0037C5F1  41 F7 46 78 00 02 00 00         test dword ptr [r14 + 0x78], 0x200
0037C5F9  75 2C                           jne 0x14037c627
0037C5FB  48 8B D1                        mov rdx, rcx
0037C5FE  F6 42 70 02                     test byte ptr [rdx + 0x70], 2
0037C602  75 33                           jne 0x14037c637
0037C604  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0037C60B  48 85 D2                        test rdx, rdx
0037C60E  75 EE                           jne 0x14037c5fe
0037C610  44 03 49 7C                     add r9d, dword ptr [rcx + 0x7c]
0037C614  75 0C                           jne 0x14037c622
0037C616  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0037C61D  48 85 C9                        test rcx, rcx
0037C620  75 EE                           jne 0x14037c610
0037C622  45 85 C9                        test r9d, r9d
0037C625  75 10                           jne 0x14037c637
0037C627  49 8D 96 C3 00 00 00            lea rdx, [r14 + 0xc3]
0037C62E  80 3A 08                        cmp byte ptr [rdx], 8
0037C631  0F 8D 60 FB FF FF               jge 0x14037c197
0037C637  44 01 86 6C 86 00 00            add dword ptr [rsi + 0x866c], r8d
0037C63E  E9 54 FB FF FF                  jmp 0x14037c197
0037C643  44 01 86 48 86 00 00            add dword ptr [rsi + 0x8648], r8d
0037C64A  45 01 86 DC 02 00 00            add dword ptr [r14 + 0x2dc], r8d
0037C651  E9 62 FF FF FF                  jmp 0x14037c5b8
0037C656  8B D0                           mov edx, eax
0037C658  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0037C65B  2B D1                           sub edx, ecx
0037C65D  83 FA 20                        cmp edx, 0x20
0037C660  73 21                           jae 0x14037c683
0037C662  41 8B 80 C4 00 00 00            mov eax, dword ptr [r8 + 0xc4]
0037C669  8B CA                           mov ecx, edx
0037C66B  D3 E0                           shl eax, cl
0037C66D  83 C8 01                        or eax, 1
0037C670  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
0037C673  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0037C677  49 89 80 C0 00 00 00            mov qword ptr [r8 + 0xc0], rax
0037C67E  E9 8E FC FF FF                  jmp 0x14037c311
0037C683  44 89 5D D4                     mov dword ptr [rbp - 0x2c], r11d
0037C687  EB EA                           jmp 0x14037c673
0037C689  48 F7 E2                        mul rdx
0037C68C  E9 C2 FA FF FF                  jmp 0x14037c153
0037C691  41 83 BF DC 00 00 00 40         cmp dword ptr [r15 + 0xdc], 0x40
0037C699  0F 85 A3 02 00 00               jne 0x14037c942
0037C69F  49 8B CF                        mov rcx, r15
0037C6A2  E8 59 CE E8 FF                  call 0x140209500
0037C6A7  49 8B 57 70                     mov rdx, qword ptr [r15 + 0x70]
0037C6AB  48 8B C8                        mov rcx, rax
0037C6AE  48 8D 05 9B C8 FF FF            lea rax, [rip - 0x3765]
0037C6B5  48 3B D0                        cmp rdx, rax
0037C6B8  0F 85 E6 03 00 00               jne 0x14037caa4
0037C6BE  48 8B 05 9B 50 A9 00            mov rax, qword ptr [rip + 0xa9509b]
0037C6C5  48 85 C0                        test rax, rax
0037C6C8  0F 84 C3 03 00 00               je 0x14037ca91
0037C6CE  48 8D 0D EB 14 F6 FF            lea rcx, [rip - 0x9eb15]
0037C6D5  48 3B C1                        cmp rax, rcx
0037C6D8  0F 85 6F 04 00 00               jne 0x14037cb4d
0037C6DE  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
0037C6E2  49 BA 94 02 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000294
0037C6EC  44 89 65 48                     mov dword ptr [rbp + 0x48], r12d
0037C6F0  48 8B 05 91 A6 C4 00            mov rax, qword ptr [rip + 0xc4a691]
0037C6F7  44 8B 08                        mov r9d, dword ptr [rax]
0037C6FA  45 85 C9                        test r9d, r9d
0037C6FD  0F 84 7B 03 00 00               je 0x14037ca7e
0037C703  41 38 3A                        cmp byte ptr [r10], dil
0037C706  0F 84 3F 03 00 00               je 0x14037ca4b
0037C70C  0F 01 F9                        rdtscp
0037C70F  4C 8D 45 48                     lea r8, [rbp + 0x48]
0037C713  41 89 08                        mov dword ptr [r8], ecx
0037C716  48 C1 E2 20                     shl rdx, 0x20
0037C71A  48 0B D0                        or rdx, rax
0037C71D  48 8B 05 64 A6 C4 00            mov rax, qword ptr [rip + 0xc4a664]
0037C724  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0037C728  48 8B 05 59 A6 C4 00            mov rax, qword ptr [rip + 0xc4a659]
0037C72F  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
0037C733  48 8B C1                        mov rax, rcx
0037C736  48 F7 E2                        mul rdx
0037C739  48 8B 05 48 A6 C4 00            mov rax, qword ptr [rip + 0xc4a648]
0037C740  49 03 D0                        add rdx, r8
0037C743  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
0037C747  8B 08                           mov ecx, dword ptr [rax]
0037C749  41 3B C9                        cmp ecx, r9d
0037C74C  75 A2                           jne 0x14037c6f0
0037C74E  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0037C752  4D 8B AF D0 00 00 00            mov r13, qword ptr [r15 + 0xd0]
0037C759  4A 8D 0C 2A                     lea rcx, [rdx + r13]
0037C75D  4C 8B C3                        mov r8, rbx
0037C760  49 8B 97 C0 00 00 00            mov rdx, qword ptr [r15 + 0xc0]
0037C767  E8 E8 EB FF FF                  call 0x14037b354
0037C76C  4C 8B D8                        mov r11, rax
0037C76F  4C 8B CB                        mov r9, rbx
0037C772  E9 41 F9 FF FF                  jmp 0x14037c0b8
0037C777  48 85 C0                        test rax, rax
0037C77A  0F 84 48 F9 FF FF               je 0x14037c0c8
0037C780  83 B8 E4 00 00 00 05            cmp dword ptr [rax + 0xe4], 5
0037C787  48 8B D3                        mov rdx, rbx
0037C78A  4C 8B 80 C0 00 00 00            mov r8, qword ptr [rax + 0xc0]
0037C791  49 8B CB                        mov rcx, r11
0037C794  4D 0F 44 C1                     cmove r8, r9
0037C798  E8 B7 EB FF FF                  call 0x14037b354
0037C79D  4C 8B D8                        mov r11, rax
0037C7A0  E9 23 F9 FF FF                  jmp 0x14037c0c8
0037C7A5  4D 8B AF D0 00 00 00            mov r13, qword ptr [r15 + 0xd0]
0037C7AC  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
0037C7B0  4C 8D 2D A9 CE FF FF            lea r13, [rip - 0x3157]
0037C7B7  49 8B BF C8 00 00 00            mov rdi, qword ptr [r15 + 0xc8]
0037C7BE  49 8B CF                        mov rcx, r15
0037C7C1  E8 3A CD E8 FF                  call 0x140209500
0037C7C6  49 8B 57 70                     mov rdx, qword ptr [r15 + 0x70]
0037C7CA  48 8B C8                        mov rcx, rax
0037C7CD  49 3B D5                        cmp rdx, r13
0037C7D0  0F 85 91 03 00 00               jne 0x14037cb67
0037C7D6  E8 85 CE FF FF                  call 0x140379660
0037C7DB  4C 8B D0                        mov r10, rax
0037C7DE  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
0037C7E3  49 8B 87 C8 00 00 00            mov rax, qword ptr [r15 + 0xc8]
0037C7EA  48 3B F8                        cmp rdi, rax
0037C7ED  75 C8                           jne 0x14037c7b7
0037C7EF  49 8B 8F D0 00 00 00            mov rcx, qword ptr [r15 + 0xd0]
0037C7F6  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
0037C7FA  4C 3B E9                        cmp r13, rcx
0037C7FD  75 A6                           jne 0x14037c7a5
0037C7FF  45 8B 8F DC 00 00 00            mov r9d, dword ptr [r15 + 0xdc]
0037C806  BA 01 00 00 00                  mov edx, 1
0037C80B  41 8D 49 FF                     lea ecx, [r9 - 1]
0037C80F  48 D3 E2                        shl rdx, cl
0037C812  49 8B CA                        mov rcx, r10
0037C815  48 33 CF                        xor rcx, rdi
0037C818  48 85 CA                        test rdx, rcx
0037C81B  75 41                           jne 0x14037c85e
0037C81D  41 83 F9 40                     cmp r9d, 0x40
0037C821  0F 85 86 00 00 00               jne 0x14037c8ad
0037C827  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0037C82E  48 F7 D2                        not rdx
0037C831  41 B9 80 96 98 00               mov r9d, 0x989680
0037C837  48 23 D7                        and rdx, rdi
0037C83A  49 0B D2                        or rdx, r10
0037C83D  4E 8D 1C 2A                     lea r11, [rdx + r13]
0037C841  E9 72 F8 FF FF                  jmp 0x14037c0b8
0037C846  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0037C84E  41 0F AF 47 50                  imul eax, dword ptr [r15 + 0x50]
0037C853  8B C8                           mov ecx, eax
0037C855  49 03 4F 48                     add rcx, qword ptr [r15 + 0x48]
0037C859  E9 13 F8 FF FF                  jmp 0x14037c071
0037C85E  41 83 F9 40                     cmp r9d, 0x40
0037C862  75 5C                           jne 0x14037c8c0
0037C864  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0037C86B  41 8B C9                        mov ecx, r9d
0037C86E  BA 01 00 00 00                  mov edx, 1
0037C873  48 D3 E2                        shl rdx, cl
0037C876  49 8B CC                        mov rcx, r12
0037C879  41 83 F9 40                     cmp r9d, 0x40
0037C87D  48 0F 45 CA                     cmovne rcx, rdx
0037C881  4C 23 C7                        and r8, rdi
0037C884  49 8B D0                        mov rdx, r8
0037C887  48 33 D7                        xor rdx, rdi
0037C88A  49 0B D2                        or rdx, r10
0037C88D  4D 3B D0                        cmp r10, r8
0037C890  73 03                           jae 0x14037c895
0037C892  48 03 D1                        add rdx, rcx
0037C895  F0 49 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [r15 + 0xc8], rdx
0037C89E  4E 8D 1C 2A                     lea r11, [rdx + r13]
0037C8A2  41 B9 80 96 98 00               mov r9d, 0x989680
0037C8A8  E9 0B F8 FF FF                  jmp 0x14037c0b8
0037C8AD  41 8B C9                        mov ecx, r9d
0037C8B0  BA 01 00 00 00                  mov edx, 1
0037C8B5  48 D3 E2                        shl rdx, cl
0037C8B8  48 FF CA                        dec rdx
0037C8BB  E9 6E FF FF FF                  jmp 0x14037c82e
0037C8C0  41 8B C9                        mov ecx, r9d
0037C8C3  41 B8 01 00 00 00               mov r8d, 1
0037C8C9  49 D3 E0                        shl r8, cl
0037C8CC  49 FF C8                        dec r8
0037C8CF  EB 9A                           jmp 0x14037c86b
0037C8D1  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0037C8D9  41 0F AF 47 50                  imul eax, dword ptr [r15 + 0x50]
0037C8DE  8B C8                           mov ecx, eax
0037C8E0  49 03 4F 48                     add rcx, qword ptr [r15 + 0x48]
0037C8E4  E9 DE FB FF FF                  jmp 0x14037c4c7
0037C8E9  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037C8F2  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0037C8F9  75 1D                           jne 0x14037c918
0037C8FB  0F AE E8                        lfence
0037C8FE  0F 31                           rdtsc
0037C900  E9 2E FC FF FF                  jmp 0x14037c533
0037C905  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0037C909  B9 04 00 09 00                  mov ecx, 0x90004
0037C90E  E8 3D C7 FF FF                  call 0x140379050
0037C913  E9 50 FC FF FF                  jmp 0x14037c568
0037C918  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037C921  80 B8 8D 00 00 00 01            cmp byte ptr [rax + 0x8d], 1
0037C928  75 D4                           jne 0x14037c8fe
0037C92A  0F AE F0                        mfence
0037C92D  EB CF                           jmp 0x14037c8fe
0037C92F  B9 20 00 00 40                  mov ecx, 0x40000020
0037C934  0F 32                           rdmsr
0037C936  48 C1 E2 20                     shl rdx, 0x20
0037C93A  48 0B D0                        or rdx, rax
0037C93D  E9 2A FC FF FF                  jmp 0x14037c56c
0037C942  4D 8B AF D0 00 00 00            mov r13, qword ptr [r15 + 0xd0]
0037C949  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
0037C94D  4C 8D 2D 0C CD FF FF            lea r13, [rip - 0x32f4]
0037C954  49 8B BF C8 00 00 00            mov rdi, qword ptr [r15 + 0xc8]
0037C95B  49 8B CF                        mov rcx, r15
0037C95E  E8 9D CB E8 FF                  call 0x140209500
0037C963  49 8B 57 70                     mov rdx, qword ptr [r15 + 0x70]
0037C967  48 8B C8                        mov rcx, rax
0037C96A  49 3B D5                        cmp rdx, r13
0037C96D  0F 85 CD 01 00 00               jne 0x14037cb40
0037C973  E8 E8 CC FF FF                  call 0x140379660
0037C978  4C 8B D0                        mov r10, rax
0037C97B  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
0037C980  49 8B 87 C8 00 00 00            mov rax, qword ptr [r15 + 0xc8]
0037C987  48 3B F8                        cmp rdi, rax
0037C98A  75 C8                           jne 0x14037c954
0037C98C  49 8B 8F D0 00 00 00            mov rcx, qword ptr [r15 + 0xd0]
0037C993  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
0037C997  4C 3B E9                        cmp r13, rcx
0037C99A  75 A6                           jne 0x14037c942
0037C99C  45 8B 8F DC 00 00 00            mov r9d, dword ptr [r15 + 0xdc]
0037C9A3  BA 01 00 00 00                  mov edx, 1
0037C9A8  41 8D 49 FF                     lea ecx, [r9 - 1]
0037C9AC  48 D3 E2                        shl rdx, cl
0037C9AF  49 8B CA                        mov rcx, r10
0037C9B2  48 33 CF                        xor rcx, rdi
0037C9B5  48 85 CA                        test rdx, rcx
0037C9B8  75 1B                           jne 0x14037c9d5
0037C9BA  41 83 F9 40                     cmp r9d, 0x40
0037C9BE  75 5A                           jne 0x14037ca1a
0037C9C0  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0037C9C7  48 F7 D2                        not rdx
0037C9CA  48 23 D7                        and rdx, rdi
0037C9CD  49 0B D2                        or rdx, r10
0037C9D0  E9 84 FD FF FF                  jmp 0x14037c759
0037C9D5  41 83 F9 40                     cmp r9d, 0x40
0037C9D9  75 4F                           jne 0x14037ca2a
0037C9DB  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0037C9E2  41 8B C9                        mov ecx, r9d
0037C9E5  BA 01 00 00 00                  mov edx, 1
0037C9EA  48 D3 E2                        shl rdx, cl
0037C9ED  49 8B CC                        mov rcx, r12
0037C9F0  41 83 F9 40                     cmp r9d, 0x40
0037C9F4  48 0F 45 CA                     cmovne rcx, rdx
0037C9F8  4C 23 C7                        and r8, rdi
0037C9FB  49 8B D0                        mov rdx, r8
0037C9FE  48 33 D7                        xor rdx, rdi
0037CA01  49 0B D2                        or rdx, r10
0037CA04  4D 3B D0                        cmp r10, r8
0037CA07  73 03                           jae 0x14037ca0c
0037CA09  48 03 D1                        add rdx, rcx
0037CA0C  F0 49 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [r15 + 0xc8], rdx
0037CA15  E9 3F FD FF FF                  jmp 0x14037c759
0037CA1A  41 8B C9                        mov ecx, r9d
0037CA1D  BA 01 00 00 00                  mov edx, 1
0037CA22  48 D3 E2                        shl rdx, cl
0037CA25  48 FF CA                        dec rdx
0037CA28  EB 9D                           jmp 0x14037c9c7
0037CA2A  41 8B C9                        mov ecx, r9d
0037CA2D  41 B8 01 00 00 00               mov r8d, 1
0037CA33  49 D3 E0                        shl r8, cl
0037CA36  49 FF C8                        dec r8
0037CA39  EB A7                           jmp 0x14037c9e2
0037CA3B  48 8B C2                        mov rax, rdx
0037CA3E  E8 8D E0 33 00                  call 0x1406baad0
0037CA43  48 8B D0                        mov rdx, rax
0037CA46  E9 21 FB FF FF                  jmp 0x14037c56c
0037CA4B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037CA54  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0037CA5B  75 0A                           jne 0x14037ca67
0037CA5D  0F AE E8                        lfence
0037CA60  0F 31                           rdtsc
0037CA62  E9 AF FC FF FF                  jmp 0x14037c716
0037CA67  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037CA70  80 B8 8D 00 00 00 01            cmp byte ptr [rax + 0x8d], 1
0037CA77  75 E7                           jne 0x14037ca60
0037CA79  0F AE F0                        mfence
0037CA7C  EB E2                           jmp 0x14037ca60
0037CA7E  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0037CA82  B9 04 00 09 00                  mov ecx, 0x90004
0037CA87  E8 C4 C5 FF FF                  call 0x140379050
0037CA8C  E9 BD FC FF FF                  jmp 0x14037c74e
0037CA91  B9 20 00 00 40                  mov ecx, 0x40000020
0037CA96  0F 32                           rdmsr
0037CA98  48 C1 E2 20                     shl rdx, 0x20
0037CA9C  48 0B D0                        or rdx, rax
0037CA9F  E9 AE FC FF FF                  jmp 0x14037c752
0037CAA4  48 8B C2                        mov rax, rdx
0037CAA7  E8 24 E0 33 00                  call 0x1406baad0
0037CAAC  48 8B D0                        mov rdx, rax
0037CAAF  E9 9E FC FF FF                  jmp 0x14037c752
0037CAB4  41 0F B6 86 04 02 00 00         movzx eax, byte ptr [r14 + 0x204]
0037CABC  8B D0                           mov edx, eax
0037CABE  83 F8 07                        cmp eax, 7
0037CAC1  0F 83 14 F9 FF FF               jae 0x14037c3db
0037CAC7  41 8B 46 54                     mov eax, dword ptr [r14 + 0x54]
0037CACB  41 8B 4E 50                     mov ecx, dword ptr [r14 + 0x50]
0037CACF  3B C8                           cmp ecx, eax
0037CAD1  0F 46 C8                        cmovbe ecx, eax
0037CAD4  41 0F B6 86 05 02 00 00         movzx eax, byte ptr [r14 + 0x205]
0037CADC  3B 0D 9A 88 C4 00               cmp ecx, dword ptr [rip + 0xc4889a]
0037CAE2  41 0F 93 C4                     setae r12b
0037CAE6  41 8D 0C 54                     lea ecx, [r12 + rdx*2]
0037CAEA  0F AF 0D EF 88 C4 00            imul ecx, dword ptr [rip + 0xc488ef]
0037CAF1  03 C8                           add ecx, eax
0037CAF3  48 8B 86 B0 86 00 00            mov rax, qword ptr [rsi + 0x86b0]
0037CAFA  48 01 3C C8                     add qword ptr [rax + rcx*8], rdi
0037CAFE  E9 D8 F8 FF FF                  jmp 0x14037c3db
0037CB03  4C 8B 86 C0 00 00 00            mov r8, qword ptr [rsi + 0xc0]
0037CB0A  49 8B 86 40 02 00 00            mov rax, qword ptr [r14 + 0x240]
0037CB11  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
0037CB19  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0037CB1E  49 8B 88 80 00 00 00            mov rcx, qword ptr [r8 + 0x80]
0037CB25  48 8B C1                        mov rax, rcx
0037CB28  48 23 C2                        and rax, rdx
0037CB2B  48 3B C1                        cmp rax, rcx
0037CB2E  0F 84 02 F9 FF FF               je 0x14037c436
0037CB34  48 01 BE A8 86 00 00            add qword ptr [rsi + 0x86a8], rdi
0037CB3B  E9 F6 F8 FF FF                  jmp 0x14037c436
0037CB40  48 8B C2                        mov rax, rdx
0037CB43  E8 88 DF 33 00                  call 0x1406baad0
0037CB48  E9 2B FE FF FF                  jmp 0x14037c978
0037CB4D  33 C9                           xor ecx, ecx
0037CB4F  E9 53 FF FF FF                  jmp 0x14037caa7
0037CB54  E8 77 DF 33 00                  call 0x1406baad0
0037CB59  48 8B D0                        mov rdx, rax
0037CB5C  41 B9 80 96 98 00               mov r9d, 0x989680
0037CB62  E9 33 F5 FF FF                  jmp 0x14037c09a
0037CB67  48 8B C2                        mov rax, rdx
0037CB6A  E8 61 DF 33 00                  call 0x1406baad0
0037CB6F  E9 67 FC FF FF                  jmp 0x14037c7db
0037CB74  33 C9                           xor ecx, ecx
0037CB76  E9 C3 FE FF FF                  jmp 0x14037ca3e
0037CB7B  BA 64 00 00 00                  mov edx, 0x64
0037CB80  E9 1F F7 FF FF                  jmp 0x14037c2a4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiEndThreadCycleAccumulation(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (104);
    v_r12 = 0;
    *(unsigned __int8 *)(a1 + 32) = 1;
    if ((*(unsigned __int8 *)(a1 + 34524)) == 0) goto loc_0037C197;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12877720) + 228)) != 5) goto loc_0037C49D;
    if ((*(unsigned __int64 *)(v_rip + 12877965)) == 0) goto loc_0037C691;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12877720) + 224)) & (0x10000ULL)) != 0) goto loc_0037C846;
loc_0037C071:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12877720) + 112)) != (v_rip + 670868)) goto loc_0037CB54;
    v_stack_p10 = 0;
    a2 = (v_rip + 670868) << (32);
    *(unsigned int *)(v_stack_p10) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12877720) + 72));
    a2 = (a2) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12877720) + 112));
loc_0037C09A:
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12877720) + 72))) + (a2);
loc_0037C0B8:
    if ((*(unsigned __int64 *)(v_rip + 12877720)) != (*(unsigned __int64 *)(v_rip + 12877577))) goto loc_0037C777;
loc_0037C0C8:
    v_stack_m58 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)) != 0) {
        a2 = (v_r11) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 172)));
    }
    v_stack_m58 = a2;
    v_rdi = (a2) - (*(unsigned __int64 *)(a1 + 34432));
    if ((*(unsigned __int8 *)(v_rip + 12888470)) == 0) goto loc_0037C197;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 176))) == 0) goto loc_0037C197;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_0037C689;
    a2 = (*(unsigned __int64 *)(a1 + 34552)) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
    a3 = (v_r11) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(a1 + 176))));
loc_0037C153:
    v_stack_m68 = a2;
    v_stack_m60 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12888684))));
    a3 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12888684))));
    a3 = (unsigned int)((a3) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_0037C582;
loc_0037C197:
    *(unsigned __int64 *)(a1 + 34552) = v_r11;
    *(unsigned __int64 *)(a1 + 34432) = a2;
    v_r13 = (*(unsigned __int64 *)(a2 + 72)) + (v_rdi);
    *(unsigned __int64 *)(a2 + 72) = v_r13;
    result = *(unsigned __int64 *)(v_rip + 12890521);
    if (a2 != (*(unsigned __int64 *)(a1 + 24))) {
        result = *(unsigned int *)(a1 + 34488);
        a1 = *(unsigned int *)(a2 + 80);
        result = (result) * (v_rdi);
        result = (result) >> (16);
        a1 = (a1) + (result);
        result = 0xFFFFFFFFULL;
        if (a1 > result) { a1 = result; }
        *(unsigned int *)(a2 + 80) = (unsigned int)(a1);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (190)) == 0) goto loc_0037C3E0;
    v_rbx = *(unsigned __int8 *)(a2 + 2);
    if (sign_flag) {
        result = *(unsigned __int64 *)(a2 + 544);
        a2 = 1;
        a3 = *(unsigned __int64 *)(a1 + 35760);
        a4 = *(unsigned int *)(result + 400);
        result = a4;
        result = (unsigned int)((result) >> (13));
        result = (unsigned int)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (unsigned int)((a4) & (511));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a1 = (unsigned int)((a1) + (-2));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        v_stack_m84 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(a3 + a1 * 8);
        a2 = *(unsigned __int64 *)(a1 + a2 * 8 + 8);
        result = *(unsigned __int64 *)(a2 + a4 * 8);
        result = (result) + (v_rdi);
        *(unsigned __int64 *)(a2 + a4 * 8) = result;
        v_rbx = (unsigned __int8)((*(unsigned __int8 *)(a2 + 2)) & (127));
    }
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_0037C462;
loc_0037C24E:
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) goto loc_0037C399;
    if (*(unsigned __int64 *)(a2 + 1672) == 0) goto loc_0037C396;
    if (*(unsigned __int64 *)(a1 + 35248) == 0) goto loc_0037CB7B;
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_0037CB7B;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112)) != 0) goto loc_0037C29E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528))))) goto loc_0037C2A4;
    goto loc_0037C2A4;
loc_0037C29E:
loc_0037C2A4:
loc_0037C2AE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)))) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(a1 + 35434)))) goto loc_0037C2C2;
    a4 = (unsigned int)((0) + 1);
    a1 = (a1 + 35434) + (2);
    if (a4 < 3) goto loc_0037C2AE;
loc_0037C2C2:
    a1 = ((unsigned int)(a4)) + ((unsigned int)(a4));
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 528)))) + 132))) & (8));
    a1 = (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(a2 + 1672) + a1 * 8 * 1)) + (v_rdi);
    *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(a2 + 1672) + a1 * 8 * 1) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12142419)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1672) + 192))))) goto loc_0037C656;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1672) + 192))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12142419)))));
    v_r11 = 1;
    if (((unsigned int)(a1)) < 32) {
        v_r11 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    }
    if ((*(unsigned int *)(v_rip + 12888648)) != 0) goto loc_0037C339;
    if ((((unsigned int)(*(unsigned __int8 *)(a2 + 516) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037C44A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 516))) == 5) goto loc_0037C44A;
loc_0037C339:
    result = *(unsigned __int8 *)(a2 + 516) - 2;
    if ((*(unsigned __int64 *)(a2 + 1616)) != 0) {
        result = (unsigned __int8)(*(unsigned __int8 *)(a1 + 35336));
        a1 = a4;
        a1 = (a1) + (8);
        a1 = (a1) + (a1);
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (8));
        result = *(unsigned __int64 *)(a2 + 1672) + a1 * 8;
        a3 = 72;
        a1 = *(unsigned __int64 *)(a2 + result * 1);
        a1 = (a1) + (v_rdi);
        *(unsigned __int64 *)(a2 + result * 1) = a1;
        a2 = 64;
        result = *(unsigned __int64 *)(a2 + 1616);
        a1 = *(unsigned __int64 *)(result + 1672);
        result = a4;
        result = (result) << (4);
        if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 35336)) != 0) { a2 = (unsigned int)(a3); }
        result = (result) + (a1);
    }
    v_rbx = (unsigned __int8)((v_rbx) & (223));
loc_0037C399:
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_0037C484;
loc_0037C3A2:
    if ((*(unsigned __int8 *)(v_rip + 12887861)) != 0) {
        a4 = v_stack_p20;
        a3 = v_rdi;
        a2 = a2;
        a1 = a1;
        result = KiUpdateThreadHgsFeedback(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 34480)) == 0) goto loc_0037C3DB;
    if ((*(unsigned __int64 *)(a2 + 544)) != (v_rip + 12925755)) goto loc_0037CAB4;
loc_0037C3DB:
    if ((((unsigned __int8)(v_rbx)) & (190)) != 0) goto loc_0037C401;
loc_0037C3E0:
    if (v_stack_p18 != 0) {
        *(unsigned __int64 *)(v_stack_p18) = a2;
    }
    v_rsp = (v_rsp) + (104);
    return v_r13;
loc_0037C401:
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037C422;
    result = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a2 + 104));
loc_0037C413:
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_0037C413;
loc_0037C422:
    if (((*(unsigned __int8 *)(a2 + 2)) & (8)) == 0) goto loc_0037C436;
    if ((*(unsigned __int64 *)(a2 + 544)) != (v_rip + 12925755)) goto loc_0037CB03;
loc_0037C436:
    if ((*(unsigned __int64 *)(a2 + 360)) == 0) goto loc_0037C3E0;
    result = KiEndCounterAccumulation(a2, a2, v_rip + 12925755, a4);
    goto loc_0037C3E0;
loc_0037C44A:
    a2 = ((unsigned int)(a4)) + ((unsigned int)(a4));
    a1 = (*(unsigned __int64 *)(v_rip + 12925755 + a2 * 8 + 8)) + (v_rdi);
    *(unsigned __int64 *)(v_rip + 12925755 + a2 * 8 + 8) = a1;
    goto loc_0037C339;
loc_0037C462:
    a1 = (*(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a2 + 124) * 8 + 34440)) + (v_rdi);
    *(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a2 + 124) * 8 + 34440) = a1;
    v_rbx = (unsigned __int8)((v_rbx) & (239));
    goto loc_0037C24E;
loc_0037C484:
    if (*(unsigned __int64 *)(a2 + 968) == 0) goto loc_0037C3A2;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 968) + 64) = 0;
    goto loc_0037C3A2;
loc_0037C49D:
    if ((*(unsigned int *)(a2 + 220)) != 64) goto loc_0037C7A5;
    if (((*(unsigned int *)(a2 + 224)) & (0x10000ULL)) != 0) goto loc_0037C8D1;
loc_0037C4C7:
    if ((*(unsigned __int64 *)(a2 + 112)) != (v_rip - 13698)) goto loc_0037CA3B;
    if (*(unsigned __int64 *)(v_rip + 11096702) == 0) goto loc_0037C92F;
    if ((*(unsigned __int64 *)(v_rip + 11096702)) != (v_rip - 649522)) goto loc_0037CB74;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
loc_0037C50D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12888180)))) == 0) goto loc_0037C905;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(a1 + 35336))) == ((unsigned __int8)(v_rdi))) goto loc_0037C8E9;
    *(unsigned int *)(v_stack_m88) = (unsigned int)(v_rip - 649522);
loc_0037C533:
    a2 = (*(unsigned __int64 *)(a2 + 112)) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(v_rip + 12888180));
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12888124) + 16));
    v_stack_m78 = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12888110))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12888180)))))) goto loc_0037C50D;
loc_0037C568:
loc_0037C56C:
    goto loc_0037C0B8;
loc_0037C582:
    if (((*(unsigned int *)(a2 + 116)) & (0x400ULL)) != 0) goto loc_0037C5AA;
    result = (v_stack_m78 + *(unsigned __int64 *)(a2 + 208) * 1) >> (4);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) < ((unsigned int)(v_stack_m78))) goto loc_0037C643;
loc_0037C5AA:
loc_0037C5B8:
    if (a2 == (*(unsigned __int64 *)(a1 + 24))) goto loc_0037C197;
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_0037C62E;
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037C62E;
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_0037C62E;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a2 + 104));
    if ((*(unsigned __int8 *)(a2 + 195)) >= 16) goto loc_0037C627;
    if (((*(unsigned int *)(a2 + 120)) & (512)) != 0) goto loc_0037C627;
loc_0037C5FE:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_0037C637;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037C5FE;
loc_0037C610:
    a4 = (unsigned int)((0) + (*(unsigned int *)(a1 + 124)));
    if (condition_is_not_equal) goto loc_0037C622;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037C610;
loc_0037C622:
    if (a4 != 0) goto loc_0037C637;
loc_0037C627:
loc_0037C62E:
    if ((*(unsigned __int8 *)(a2 + 195)) >= 8) goto loc_0037C197;
loc_0037C637:
    goto loc_0037C197;
loc_0037C643:
    goto loc_0037C5B8;
loc_0037C656:
    v_stack_m70 = (unsigned int)(*(unsigned __int64 *)(a2 + 104));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2 + 104)))) - ((unsigned int)(*(unsigned __int64 *)(a1 + 416))));
    if (((unsigned int)(a2)) >= 32) goto loc_0037C683;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12888124) + 16) + 196))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) | (1));
    v_stack_m6C = (unsigned int)(result);
loc_0037C673:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12888124) + 16) + 192) = v_stack_m70;
    goto loc_0037C311;
loc_0037C683:
    v_stack_m6C = (unsigned int)(v_stack_m78 + *(unsigned __int64 *)(a2 + 208) * 1);
    goto loc_0037C673;
loc_0037C689:
    goto loc_0037C153;
loc_0037C691:
    if ((*(unsigned int *)(a2 + 220)) != 64) goto loc_0037C942;
    result = HalpTimerGetInternalData(a2, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12888124) + 16), a4);
    if ((*(unsigned __int64 *)(a2 + 112)) != (v_rip - 14181)) goto loc_0037CAA4;
    if (*(unsigned __int64 *)(v_rip + 11096219) == 0) goto loc_0037CA91;
    if ((*(unsigned __int64 *)(v_rip + 11096219)) != (v_rip - 650005)) goto loc_0037CB4D;
    v_stack_m80 = 0;
    v_stack_p8 = 0;
loc_0037C6F0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12887697)))) == 0) goto loc_0037CA7E;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(a1 + 35336))) == ((unsigned __int8)(v_rdi))) goto loc_0037CA4B;
    *(unsigned int *)(v_stack_p8) = (unsigned int)(v_rip - 650005);
loc_0037C716:
    a2 = (*(unsigned __int64 *)(a2 + 112)) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(v_rip + 12887697));
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12887641) + 16));
    v_stack_m80 = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12887624))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12887697)))))) goto loc_0037C6F0;
loc_0037C74E:
loc_0037C752:
loc_0037C759:
    result = HalpTimerScaleCounter(v_stack_m80 + *(unsigned __int64 *)(a2 + 208) * 1, *(unsigned __int64 *)(a2 + 192), *(unsigned __int64 *)(a2 + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12887697))));
    goto loc_0037C0B8;
loc_0037C777:
    if (result == 0) goto loc_0037C0C8;
    a3 = *(unsigned __int64 *)(result + 192);
    if ((*(unsigned int *)(result + 228)) == 5) { a3 = *(unsigned __int64 *)(a2 + 192); }
    result = HalpTimerScaleCounter(result, *(unsigned __int64 *)(a2 + 192), a3, *(unsigned __int64 *)(a2 + 192));
    goto loc_0037C0C8;
loc_0037C7A5:
    v_stack_m70 = *(unsigned __int64 *)(a2 + 208);
loc_0037C7B7:
    result = HalpTimerGetInternalData(a2, *(unsigned __int64 *)(a2 + 192), a3, *(unsigned __int64 *)(a2 + 192));
    if ((*(unsigned __int64 *)(a2 + 112)) != (v_rip - 12631)) goto loc_0037CB67;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(a2 + 112), a3, *(unsigned __int64 *)(a2 + 192));
loc_0037C7DB:
    if ((*(unsigned __int64 *)(a2 + 200)) != (*(unsigned __int64 *)(a2 + 200))) goto loc_0037C7B7;
    if (v_stack_m70 != (*(unsigned __int64 *)(a2 + 208))) goto loc_0037C7A5;
    a2 = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 220)) - 1));
    a1 = (result) ^ (*(unsigned __int64 *)(a2 + 200));
    if (((a2) & (a1)) != 0) goto loc_0037C85E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)))) != 64) goto loc_0037C8AD;
loc_0037C82E:
    a2 = ~(-1);
    a2 = (a2) & (*(unsigned __int64 *)(a2 + 200));
    a2 = (a2) | (result);
    goto loc_0037C0B8;
loc_0037C846:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * (*(unsigned int *)(a2 + 80)));
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a2 + 72));
    goto loc_0037C071;
loc_0037C85E:
    if (((unsigned int)((unsigned int)(0x989680ULL))) != 64) goto loc_0037C8C0;
loc_0037C86B:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0x989680ULL)))));
    a1 = 0;
    if (((unsigned int)((unsigned int)(0x989680ULL))) != 64) { a1 = a2; }
    a3 = (-1) & (*(unsigned __int64 *)(a2 + 200));
    a2 = (a3) ^ (*(unsigned __int64 *)(a2 + 200));
    a2 = (a2) | (result);
    if (result < a3) {
        a2 = (a2) + (a1);
    }
    goto loc_0037C0B8;
loc_0037C8AD:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0x989680ULL)))));
    a2 = (a2) - 1;
    goto loc_0037C82E;
loc_0037C8C0:
    a3 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0x989680ULL)))));
    a3 = (a3) - 1;
    goto loc_0037C86B;
loc_0037C8D1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * (*(unsigned int *)(a2 + 80)));
    a1 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a2 + 72));
    goto loc_0037C4C7;
loc_0037C8E9:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 2) goto loc_0037C918;
loc_0037C8FE:
    goto loc_0037C533;
loc_0037C905:
    result = HvlpGetRegister64((unsigned int)(0x90004ULL), v_stack_m78, a3, (unsigned int)(0x989680ULL));
    goto loc_0037C568;
loc_0037C918:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 1) goto loc_0037C8FE;
    goto loc_0037C8FE;
loc_0037C92F:
    a2 = (v_stack_m78) << (32);
    a2 = (a2) | (*(unsigned __int64 *)(gs_base + (0 + 32)));
    goto loc_0037C56C;
loc_0037C942:
    v_stack_m70 = *(unsigned __int64 *)(a2 + 208);
loc_0037C954:
    result = HalpTimerGetInternalData(a2, a2, a3, (unsigned int)(0x989680ULL));
    if ((*(unsigned __int64 *)(a2 + 112)) != (v_rip - 13044)) goto loc_0037CB40;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(a2 + 112), a3, (unsigned int)(0x989680ULL));
loc_0037C978:
    if ((*(unsigned __int64 *)(a2 + 200)) != (*(unsigned __int64 *)(a2 + 200))) goto loc_0037C954;
    if (v_stack_m70 != (*(unsigned __int64 *)(a2 + 208))) goto loc_0037C942;
    a2 = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 220)) - 1));
    a1 = (result) ^ (*(unsigned __int64 *)(a2 + 200));
    if (((a2) & (a1)) != 0) goto loc_0037C9D5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)))) != 64) goto loc_0037CA1A;
loc_0037C9C7:
    a2 = ~(-1);
    a2 = (a2) & (*(unsigned __int64 *)(a2 + 200));
    a2 = (a2) | (result);
    goto loc_0037C759;
loc_0037C9D5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)))) != 64) goto loc_0037CA2A;
loc_0037C9E2:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220))))));
    a1 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)))) != 64) { a1 = a2; }
    a3 = (-1) & (*(unsigned __int64 *)(a2 + 200));
    a2 = (a3) ^ (*(unsigned __int64 *)(a2 + 200));
    a2 = (a2) | (result);
    if (result < a3) {
        a2 = (a2) + (a1);
    }
    goto loc_0037C759;
loc_0037CA1A:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220))))));
    a2 = (a2) - 1;
    goto loc_0037C9C7;
loc_0037CA2A:
    a3 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220))))));
    a3 = (a3) - 1;
    goto loc_0037C9E2;
loc_0037CA3B:
loc_0037CA3E:
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)))), a2, a3, (unsigned int)(*(unsigned int *)(a2 + 220)));
    goto loc_0037C56C;
loc_0037CA4B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 2) goto loc_0037CA67;
loc_0037CA60:
    goto loc_0037C716;
loc_0037CA67:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) != 1) goto loc_0037CA60;
    goto loc_0037CA60;
loc_0037CA7E:
    result = HvlpGetRegister64((unsigned int)(0x90004ULL), v_stack_m80, a3, (unsigned int)(*(unsigned int *)(a2 + 220)));
    goto loc_0037C74E;
loc_0037CA91:
    a2 = (v_stack_m80) << (32);
    a2 = (a2) | (result);
    goto loc_0037C752;
loc_0037CAA4:
loc_0037CAA7:
    result = guard_dispatch_icall((unsigned int)(0x40000020ULL), a2, a3, (unsigned int)(*(unsigned int *)(a2 + 220)));
    goto loc_0037C752;
loc_0037CAB4:
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 516))) >= 7) goto loc_0037C3DB;
    a1 = (unsigned int)(*(unsigned int *)(a2 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84))); }
    v_r12 = (((unsigned int)(a1)) >= (*(unsigned int *)(v_rip + 12880026))) ? 1 : 0;
    a1 = (unsigned int)((v_r12 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a2 + 516))) * 2) * (*(unsigned int *)(v_rip + 12880111)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(a2 + 517))));
    goto loc_0037C3DB;
loc_0037CB03:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 128)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 136) * 8 + 8));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 128))) goto loc_0037C436;
    goto loc_0037C436;
loc_0037CB40:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 128), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 136) * 8 + 8), *(unsigned __int64 *)(a1 + 192), (unsigned int)(*(unsigned int *)(a2 + 220)));
    goto loc_0037C978;
loc_0037CB4D:
    a1 = 0;
    goto loc_0037CAA7;
loc_0037CB54:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 136) * 8 + 8), *(unsigned __int64 *)(a1 + 192), (unsigned int)(*(unsigned int *)(a2 + 220)));
    goto loc_0037C09A;
loc_0037CB67:
    result = guard_dispatch_icall(a1, result, *(unsigned __int64 *)(a1 + 192), (unsigned int)(0x989680ULL));
    goto loc_0037C7DB;
loc_0037CB74:
    a1 = 0;
    goto loc_0037CA3E;
loc_0037CB7B:
    goto loc_0037C2A4;
}
```

## 5. (Beta) C Style

```c
int64_t KiEndThreadCycleAccumulation(void *Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (104);
    local_r12 = 0;
    *(uint8_t *)(arg1 + 0x20) = 1;
    if ((*(uint8_t *)(arg1 + 0x86DC)) == 0) goto loc_0037C197;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0xE4)) != 5) goto loc_0037C49D;
    if ((*(uint64_t *)(v_rip + 0xC4808D)) == 0) goto loc_0037C691;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0xE0)) & (0x10000ULL)) != 0) goto loc_0037C846;
loc_0037C071:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0x70)) != (v_rip + 670868)) goto loc_0037CB54;
    v_stack_p10 = 0;
    Arg2 = (v_rip + 670868) << (32);
    *(uint32_t *)(v_stack_p10) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0x48));
    Arg2 = (Arg2) | (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0x70));
loc_0037C09A:
    local_r11 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC47F98) + 0x48))) + (Arg2);
loc_0037C0B8:
    if ((*(uint64_t *)(v_rip + 0xC47F98)) != (*(uint64_t *)(v_rip + 0xC47F09))) goto loc_0037C777;
loc_0037C0C8:
    v_stack_m58 = 0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)) != 0) {
        Arg2 = (local_r11) << ((uint8_t)(*(uint8_t *)(arg1 + 0xAC)));
    }
    v_stack_m58 = Arg2;
    local_rdi = (Arg2) - (*(uint64_t *)(arg1 + 0x8680));
    if ((*(uint8_t *)(v_rip + 0xC4A996)) == 0) goto loc_0037C197;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xB0))) == 0) goto loc_0037C197;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if ((uint8_t)(*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_0037C689;
    Arg2 = (*(uint64_t *)(arg1 + 0x86F8)) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
    Arg3 = (local_r11) << ((uint8_t)((uint8_t)(*(uint64_t *)(arg1 + 0xB0))));
loc_0037C153:
    v_stack_m68 = Arg2;
    v_stack_m60 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC4AA6C))));
    Arg3 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC4AA6C))));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_0037C582;
loc_0037C197:
    *(uint64_t *)(arg1 + 0x86F8) = local_r11;
    *(void **)(arg1 + 0x8680) = Arg2;
    local_r13 = (*(uint64_t *)(arg2 + 0x48)) + (local_rdi);
    *(uint64_t *)(arg2 + 0x48) = local_r13;
    result = *(uint64_t *)(v_rip + 0xC4B199);
    if (Arg2 != (*(uint64_t *)(arg1 + 0x18))) {
        result = *(uint32_t *)(arg1 + 0x86B8);
        Arg1 = *(uint32_t *)(arg2 + 0x50);
        result = (result) * (local_rdi);
        result = (result) >> (16);
        Arg1 = (Arg1) + (result);
        result = 0xFFFFFFFFULL;
        if (Arg1 > result) { Arg1 = result; }
        *(uint32_t *)(arg2 + 0x50) = (uint32_t)(Arg1);
    }
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x2))) & (190)) == 0) goto loc_0037C3E0;
    local_rbx = *(uint8_t *)(arg2 + 0x2);
    if (sign_flag) {
        result = *(uint64_t *)(arg2 + 0x220);
        Arg2 = 1;
        Arg3 = *(uint64_t *)(arg1 + 0x8BB0);
        Arg4 = *(uint32_t *)(result + 0x190);
        result = Arg4;
        result = (uint32_t)((result) >> (13));
        result = (uint32_t)((result) & (0x3FFFFULL));
        Arg4 = (Arg4) >> (4);
        Arg4 = (uint32_t)((Arg4) & (511));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)((Arg1) + (-2));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        v_stack_m84 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(Arg3 + arg1 * 8);
        Arg2 = *(uint64_t *)(arg1 + arg2 * 8 + 0x8);
        result = *(uint64_t *)(arg2 + Arg4 * 8);
        result = (result) + (local_rdi);
        *(uint64_t *)(arg2 + Arg4 * 8) = result;
        local_rbx = (uint8_t)((*(uint8_t *)(arg2 + 0x2)) & (127));
    }
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_0037C462;
loc_0037C24E:
    if ((((uint8_t)(local_rbx)) & (32)) == 0) goto loc_0037C399;
    if (*(uint64_t *)(arg2 + 0x688) == 0) goto loc_0037C396;
    if (*(uint64_t *)(arg1 + 0x89B0) == 0) goto loc_0037CB7B;
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_0037CB7B;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70)) != 0) goto loc_0037C29E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210))))) goto loc_0037C2A4;
    goto loc_0037C2A4;
loc_0037C29E:
loc_0037C2A4:
loc_0037C2AE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)))) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(arg1 + 0x8A6A)))) goto loc_0037C2C2;
    Arg4 = (uint32_t)((0) + 1);
    Arg1 = (Arg1 + 35434) + (2);
    if (Arg4 < 3) goto loc_0037C2AE;
loc_0037C2C2:
    Arg1 = ((uint32_t)(Arg4)) + ((uint32_t)(Arg4));
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg1 + 0x8A08))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x210)))) + 0x84))) & (8));
    Arg1 = (*(uint64_t *)(arg2 + *(uint64_t *)(arg2 + 0x688) + arg1 * 8 * 1)) + (local_rdi);
    *(void **)(arg2 + *(uint64_t *)(arg2 + 0x688) + arg1 * 8 * 1) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB94753)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x688) + 0xC0))))) goto loc_0037C656;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x688) + 0xC0))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB94753)))));
    local_r11 = 1;
    if (((uint32_t)(Arg1)) < 32) {
        local_r11 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    }
    if ((*(uint32_t *)(v_rip + 0xC4AA48)) != 0) goto loc_0037C339;
    if ((((uint32_t)(*(uint8_t *)(arg2 + 0x204) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037C44A;
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x204))) == 5) goto loc_0037C44A;
loc_0037C339:
    result = *(uint8_t *)(arg2 + 0x204) - 2;
    if ((*(uint64_t *)(arg2 + 0x650)) != 0) {
        result = (uint8_t)(*(uint8_t *)(arg1 + 0x8A08));
        Arg1 = Arg4;
        Arg1 = (Arg1) + (8);
        Arg1 = (Arg1) + (Arg1);
        result = (uint8_t)(-(result));
        Arg2 = (uint32_t)((Arg2) & (8));
        result = *(uint64_t *)(arg2 + 0x688) + Arg1 * 8;
        Arg3 = 72;
        Arg1 = *(uint64_t *)(arg2 + result * 1);
        Arg1 = (Arg1) + (local_rdi);
        *(void **)(arg2 + result * 1) = Arg1;
        Arg2 = 64;
        result = *(uint64_t *)(arg2 + 0x650);
        Arg1 = *(uint64_t *)(result + 0x688);
        result = Arg4;
        result = (result) << (4);
        if ((uint8_t)(*(uint8_t *)(arg1 + 0x8A08)) != 0) { Arg2 = (uint32_t)(Arg3); }
        result = (result) + (Arg1);
    }
    local_rbx = (uint8_t)((local_rbx) & (223));
loc_0037C399:
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_0037C484;
loc_0037C3A2:
    if ((*(uint8_t *)(v_rip + 0xC4A735)) != 0) {
        Arg4 = v_stack_p20;
        Arg3 = local_rdi;
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = KiUpdateThreadHgsFeedback(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(arg1 + 0x86B0)) == 0) goto loc_0037C3DB;
    if ((*(uint64_t *)(arg2 + 0x220)) != (v_rip + 12925755)) goto loc_0037CAB4;
loc_0037C3DB:
    if ((((uint8_t)(local_rbx)) & (190)) != 0) goto loc_0037C401;
loc_0037C3E0:
    if (v_stack_p18 != 0) {
        *(void **)(v_stack_p18) = Arg2;
    }
    local_rsp = (local_rsp) + (104);
    return local_r13;
loc_0037C401:
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037C422;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg2 + 0x68));
loc_0037C413:
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_0037C413;
loc_0037C422:
    if (((*(uint8_t *)(arg2 + 0x2)) & (8)) == 0) goto loc_0037C436;
    if ((*(uint64_t *)(arg2 + 0x220)) != (v_rip + 12925755)) goto loc_0037CB03;
loc_0037C436:
    if ((*(uint64_t *)(arg2 + 0x168)) == 0) goto loc_0037C3E0;
    result = KiEndCounterAccumulation(Arg2, Arg2, v_rip + 12925755, Arg4);
    goto loc_0037C3E0;
loc_0037C44A:
    Arg2 = ((uint32_t)(Arg4)) + ((uint32_t)(Arg4));
    Arg1 = (*(uint64_t *)(v_rip + 0xC53B3B + arg2 * 8 + 0x8)) + (local_rdi);
    *(void **)(v_rip + 0xC53B3B + arg2 * 8 + 0x8) = Arg1;
    goto loc_0037C339;
loc_0037C462:
    Arg1 = (*(uint64_t *)(arg1 + *(uint8_t *)(arg2 + 0x7C) * 8 + 0x8688)) + (local_rdi);
    *(void **)(arg1 + *(uint8_t *)(arg2 + 0x7C) * 8 + 0x8688) = Arg1;
    local_rbx = (uint8_t)((local_rbx) & (239));
    goto loc_0037C24E;
loc_0037C484:
    if (*(uint64_t *)(arg2 + 0x3C8) == 0) goto loc_0037C3A2;
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x3C8) + 0x40) = 0;
    goto loc_0037C3A2;
loc_0037C49D:
    if ((*(uint32_t *)(arg2 + 0xDC)) != 64) goto loc_0037C7A5;
    if (((*(uint32_t *)(arg2 + 0xE0)) & (0x10000ULL)) != 0) goto loc_0037C8D1;
loc_0037C4C7:
    if ((*(uint64_t *)(arg2 + 0x70)) != (v_rip - 13698)) goto loc_0037CA3B;
    if (*(uint64_t *)(v_rip + 0xA9527E) == 0) goto loc_0037C92F;
    if ((*(uint64_t *)(v_rip + 0xA9527E)) != (v_rip - 649522)) goto loc_0037CB74;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
loc_0037C50D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A874)))) == 0) goto loc_0037C905;
    if ((*(uint8_t *)(*(uint8_t *)(arg1 + 0x8A08))) == ((uint8_t)(local_rdi))) goto loc_0037C8E9;
    *(uint32_t *)(v_stack_m88) = (uint32_t)(v_rip - 649522);
loc_0037C533:
    Arg2 = (*(uint64_t *)(arg2 + 0x70)) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(v_rip + 0xC4A874));
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC4A83C) + 0x10));
    v_stack_m78 = Arg2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A82E))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A874)))))) goto loc_0037C50D;
loc_0037C568:
loc_0037C56C:
    goto loc_0037C0B8;
loc_0037C582:
    if (((*(uint32_t *)(arg2 + 0x74)) & (0x400ULL)) != 0) goto loc_0037C5AA;
    result = (v_stack_m78 + *(uint64_t *)(arg2 + 0xD0) * 1) >> (4);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) < ((uint32_t)(v_stack_m78))) goto loc_0037C643;
loc_0037C5AA:
loc_0037C5B8:
    if (Arg2 == (*(uint64_t *)(arg1 + 0x18))) goto loc_0037C197;
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 16) goto loc_0037C62E;
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037C62E;
    if (*(uint64_t *)(arg2 + 0x68) == 0) goto loc_0037C62E;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg2 + 0x68));
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 16) goto loc_0037C627;
    if (((*(uint32_t *)(arg2 + 0x78)) & (512)) != 0) goto loc_0037C627;
loc_0037C5FE:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) != 0) goto loc_0037C637;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0037C5FE;
loc_0037C610:
    Arg4 = (uint32_t)((0) + (*(uint32_t *)(arg1 + 0x7C)));
    if (condition_is_not_equal) goto loc_0037C622;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_0037C610;
loc_0037C622:
    if (Arg4 != 0) goto loc_0037C637;
loc_0037C627:
loc_0037C62E:
    if ((*(uint8_t *)(arg2 + 0xC3)) >= 8) goto loc_0037C197;
loc_0037C637:
    goto loc_0037C197;
loc_0037C643:
    goto loc_0037C5B8;
loc_0037C656:
    v_stack_m70 = (uint32_t)(*(uint64_t *)(arg2 + 0x68));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg2 + 0x68)))) - ((uint32_t)(*(uint64_t *)(arg1 + 0x1A0))));
    if (((uint32_t)(Arg2)) >= 32) goto loc_0037C683;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC4A83C) + 0x10) + 0xC4))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) | (1));
    v_stack_m6C = (uint32_t)(result);
loc_0037C673:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC4A83C) + 0x10) + 0xC0) = v_stack_m70;
    goto loc_0037C311;
loc_0037C683:
    v_stack_m6C = (uint32_t)(v_stack_m78 + *(uint64_t *)(arg2 + 0xD0) * 1);
    goto loc_0037C673;
loc_0037C689:
    goto loc_0037C153;
loc_0037C691:
    if ((*(uint32_t *)(arg2 + 0xDC)) != 64) goto loc_0037C942;
    result = HalpTimerGetInternalData(Arg2, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC4A83C) + 0x10), Arg4);
    if ((*(uint64_t *)(arg2 + 0x70)) != (v_rip - 14181)) goto loc_0037CAA4;
    if (*(uint64_t *)(v_rip + 0xA9509B) == 0) goto loc_0037CA91;
    if ((*(uint64_t *)(v_rip + 0xA9509B)) != (v_rip - 650005)) goto loc_0037CB4D;
    v_stack_m80 = 0;
    v_stack_p8 = 0;
loc_0037C6F0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A691)))) == 0) goto loc_0037CA7E;
    if ((*(uint8_t *)(*(uint8_t *)(arg1 + 0x8A08))) == ((uint8_t)(local_rdi))) goto loc_0037CA4B;
    *(uint32_t *)(v_stack_p8) = (uint32_t)(v_rip - 650005);
loc_0037C716:
    Arg2 = (*(uint64_t *)(arg2 + 0x70)) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(v_rip + 0xC4A691));
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC4A659) + 0x10));
    v_stack_m80 = Arg2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A648))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A691)))))) goto loc_0037C6F0;
loc_0037C74E:
loc_0037C752:
loc_0037C759:
    result = HalpTimerScaleCounter(v_stack_m80 + *(uint64_t *)(arg2 + 0xD0) * 1, *(uint64_t *)(arg2 + 0xC0), *(uint64_t *)(arg2 + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4A691))));
    goto loc_0037C0B8;
loc_0037C777:
    if (result == 0) goto loc_0037C0C8;
    Arg3 = *(uint64_t *)(result + 0xC0);
    if ((*(uint32_t *)(result + 0xE4)) == 5) { Arg3 = *(uint64_t *)(arg2 + 0xC0); }
    result = HalpTimerScaleCounter(result, *(uint64_t *)(arg2 + 0xC0), Arg3, *(uint64_t *)(arg2 + 0xC0));
    goto loc_0037C0C8;
loc_0037C7A5:
    v_stack_m70 = *(uint64_t *)(arg2 + 0xD0);
loc_0037C7B7:
    result = HalpTimerGetInternalData(Arg2, *(uint64_t *)(arg2 + 0xC0), Arg3, *(uint64_t *)(arg2 + 0xC0));
    if ((*(uint64_t *)(arg2 + 0x70)) != (v_rip - 12631)) goto loc_0037CB67;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(arg2 + 0x70), Arg3, *(uint64_t *)(arg2 + 0xC0));
loc_0037C7DB:
    if ((*(uint64_t *)(arg2 + 0xC8)) != (*(uint64_t *)(arg2 + 0xC8))) goto loc_0037C7B7;
    if (v_stack_m70 != (*(uint64_t *)(arg2 + 0xD0))) goto loc_0037C7A5;
    Arg2 = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)) - 1));
    Arg1 = (result) ^ (*(uint64_t *)(arg2 + 0xC8));
    if (((Arg2) & (Arg1)) != 0) goto loc_0037C85E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)))) != 64) goto loc_0037C8AD;
loc_0037C82E:
    Arg2 = ~(-1);
    Arg2 = (Arg2) & (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_0037C0B8;
loc_0037C846:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * (*(uint32_t *)(arg2 + 0x50)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg2 + 0x48));
    goto loc_0037C071;
loc_0037C85E:
    if (((uint32_t)((uint32_t)(0x989680ULL))) != 64) goto loc_0037C8C0;
loc_0037C86B:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0x989680ULL)))));
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(0x989680ULL))) != 64) { Arg1 = Arg2; }
    Arg3 = (-1) & (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg3) ^ (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg2) | (result);
    if (result < Arg3) {
        Arg2 = (Arg2) + (Arg1);
    }
    goto loc_0037C0B8;
loc_0037C8AD:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0x989680ULL)))));
    Arg2 = (Arg2) - 1;
    goto loc_0037C82E;
loc_0037C8C0:
    Arg3 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0x989680ULL)))));
    Arg3 = (Arg3) - 1;
    goto loc_0037C86B;
loc_0037C8D1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * (*(uint32_t *)(arg2 + 0x50)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg2 + 0x48));
    goto loc_0037C4C7;
loc_0037C8E9:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 2) goto loc_0037C918;
loc_0037C8FE:
    goto loc_0037C533;
loc_0037C905:
    result = HvlpGetRegister64((uint32_t)(0x90004ULL), v_stack_m78, Arg3, (uint32_t)(0x989680ULL));
    goto loc_0037C568;
loc_0037C918:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 1) goto loc_0037C8FE;
    goto loc_0037C8FE;
loc_0037C92F:
    Arg2 = (v_stack_m78) << (32);
    Arg2 = (Arg2) | (*(uint64_t *)(gs_base + (0 + 0x20)));
    goto loc_0037C56C;
loc_0037C942:
    v_stack_m70 = *(uint64_t *)(arg2 + 0xD0);
loc_0037C954:
    result = HalpTimerGetInternalData(Arg2, Arg2, Arg3, (uint32_t)(0x989680ULL));
    if ((*(uint64_t *)(arg2 + 0x70)) != (v_rip - 13044)) goto loc_0037CB40;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(arg2 + 0x70), Arg3, (uint32_t)(0x989680ULL));
loc_0037C978:
    if ((*(uint64_t *)(arg2 + 0xC8)) != (*(uint64_t *)(arg2 + 0xC8))) goto loc_0037C954;
    if (v_stack_m70 != (*(uint64_t *)(arg2 + 0xD0))) goto loc_0037C942;
    Arg2 = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)) - 1));
    Arg1 = (result) ^ (*(uint64_t *)(arg2 + 0xC8));
    if (((Arg2) & (Arg1)) != 0) goto loc_0037C9D5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)))) != 64) goto loc_0037CA1A;
loc_0037C9C7:
    Arg2 = ~(-1);
    Arg2 = (Arg2) & (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_0037C759;
loc_0037C9D5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)))) != 64) goto loc_0037CA2A;
loc_0037C9E2:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC))))));
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)))) != 64) { Arg1 = Arg2; }
    Arg3 = (-1) & (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg3) ^ (*(uint64_t *)(arg2 + 0xC8));
    Arg2 = (Arg2) | (result);
    if (result < Arg3) {
        Arg2 = (Arg2) + (Arg1);
    }
    goto loc_0037C759;
loc_0037CA1A:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC))))));
    Arg2 = (Arg2) - 1;
    goto loc_0037C9C7;
loc_0037CA2A:
    Arg3 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC))))));
    Arg3 = (Arg3) - 1;
    goto loc_0037C9E2;
loc_0037CA3B:
loc_0037CA3E:
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)))), Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    goto loc_0037C56C;
loc_0037CA4B:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 2) goto loc_0037CA67;
loc_0037CA60:
    goto loc_0037C716;
loc_0037CA67:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) != 1) goto loc_0037CA60;
    goto loc_0037CA60;
loc_0037CA7E:
    result = HvlpGetRegister64((uint32_t)(0x90004ULL), v_stack_m80, Arg3, (uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    goto loc_0037C74E;
loc_0037CA91:
    Arg2 = (v_stack_m80) << (32);
    Arg2 = (Arg2) | (result);
    goto loc_0037C752;
loc_0037CAA4:
loc_0037CAA7:
    result = guard_dispatch_icall((uint32_t)(0x40000020ULL), Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    goto loc_0037C752;
loc_0037CAB4:
    if (((uint32_t)(*(uint8_t *)(arg2 + 0x204))) >= 7) goto loc_0037C3DB;
    Arg1 = (uint32_t)(*(uint32_t *)(arg2 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54))); }
    local_r12 = (((uint32_t)(Arg1)) >= (*(uint32_t *)(v_rip + 0xC4889A))) ? 1 : 0;
    Arg1 = (uint32_t)((local_r12 + (uint32_t)((uint32_t)(*(uint8_t *)(arg2 + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xC488EF)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint8_t *)(arg2 + 0x205))));
    goto loc_0037C3DB;
loc_0037CB03:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x80)) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0x240) + *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x88) * 8 + 0x8));
    if (result == (*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x80))) goto loc_0037C436;
    goto loc_0037C436;
loc_0037CB40:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x80), *(uint64_t *)(*(uint64_t *)(arg2 + 0x240) + *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x88) * 8 + 0x8), *(uint64_t *)(arg1 + 0xC0), (uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    goto loc_0037C978;
loc_0037CB4D:
    Arg1 = 0;
    goto loc_0037CAA7;
loc_0037CB54:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x240) + *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x88) * 8 + 0x8), *(uint64_t *)(arg1 + 0xC0), (uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    goto loc_0037C09A;
loc_0037CB67:
    result = guard_dispatch_icall(Arg1, result, *(uint64_t *)(arg1 + 0xC0), (uint32_t)(0x989680ULL));
    goto loc_0037C7DB;
loc_0037CB74:
    Arg1 = 0;
    goto loc_0037CA3E;
loc_0037CB7B:
    goto loc_0037C2A4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `W` |
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x8644` | `32` | `R/W` |
| `Arg1` | `+ 0x8648` | `32` | `R/W` |
| `Arg1` | `+ 0x866C` | `32` | `R/W` |
| `Arg1` | `+ 0x8680` | `64` | `R` |
| `Arg1` | `+ 0x8680` | `64` | `W` |
| `Arg1` | `+ 0x8688` | `64` | `R` |
| `Arg1` | `+ 0x8688` | `64` | `W` |
| `Arg1` | `+ 0x86A8` | `64` | `R/W` |
| `Arg1` | `+ 0x86B0` | `64` | `R` |
| `Arg1` | `+ 0x86B8` | `32` | `R` |
| `Arg1` | `+ 0x86DC` | `8` | `R` |
| `Arg1` | `+ 0x86F8` | `64` | `R` |
| `Arg1` | `+ 0x86F8` | `64` | `W` |
| `Arg1` | `+ 0x89B0` | `64` | `R` |
| `Arg1` | `+ 0x89B8` | `64` | `R` |
| `Arg1` | `+ 0x8A08` | `8` | `R` |
| `Arg1` | `+ 0x8A6A` | `64` | `R` |
| `Arg1` | `+ 0x8BB0` | `64` | `R` |
| `Arg2` | `+ 0x74` | `32` | `R` |
| `Arg2` | `+ 0x28C` | `32` | `R/W` |
| `Arg2` | `+ 0x2DC` | `32` | `R/W` |
| `Arg2` | `+ 0x44C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037BFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
