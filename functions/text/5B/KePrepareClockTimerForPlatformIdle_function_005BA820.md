# KePrepareClockTimerForPlatformIdle

- RVA: `0x005BA820`–`0x005BACBC` (길이 `1,180` bytes)
- VA: `0x00000001405BA820`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA150`
- 디코드: `274`개 명령, `1,180/1,180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **35**

### Outgoing calls
- `0x005BA8EC` → [PoAllProcessorsDeepIdle](../5C/PoAllProcessorsDeepIdle_function_005CF1C4.md) (function, `0x005CF1C4`)
- `0x005BA904` → [KeIsForceIdleEngaged](../3A/KeIsForceIdleEngaged_function_003A38D0.md) (function, `0x003A38D0`)
- `0x005BA959` → [KiGetNextTimerExpirationDueTime](KiGetNextTimerExpirationDueTime_function_005BCF60.md) (function, `0x005BCF60`)
- `0x005BA9E4` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x005BAA0E` → [KePrepareClockTimerForIdle](KePrepareClockTimerForIdle_function_005BA49C.md) (function, `0x005BA49C`)
- `0x005BAA76` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x005BAA82` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x005BAAAD` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x005BAB39` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005BAB51` → [KiLogClockIncrementUpdate](../46/KiLogClockIncrementUpdate_function_00466C98.md) (function, `0x00466C98`)
- `0x005BAB58` → [KiSetPendingTick](../44/KiSetPendingTick_function_004400F4.md) (function, `0x004400F4`)
- `0x005BAB76` → [KiEventClockStateChange](../46/KiEventClockStateChange_function_0046279C.md) (function, `0x0046279C`)
- `0x005BABF0` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005BAC01` → [KeIsForceIdleEngaged](../3A/KeIsForceIdleEngaged_function_003A38D0.md) (function, `0x003A38D0`)
- `0x005BAC21` → [KiCancelClockTimerKTimerDeadlines](KiCancelClockTimerKTimerDeadlines_function_005BB5A0.md) (function, `0x005BB5A0`)
- `0x005BAC8C` → [KiSetVpThreadHrTimerActive](../46/KiSetVpThreadHrTimerActive_function_00463394.md) (function, `0x00463394`)

### Direct callers
- [sub_006DCEEE](../6D/Unknown_function_006DCEEE.md) at `0x006DD120`

### Static image references
- `0x005BA843` → RVA `0x00E0A740` (`.data`; read)
- `0x005BA87E` → RVA `0x00FC6BC4` (`ALMOSTRO`; read)
- `0x005BA8A8` → RVA `0x00FC5364` (`ALMOSTRO`; read)
- `0x005BA8B5` → RVA `0x00F21FC0` (`.data`; read)
- `0x005BA8CA` → RVA `0x00FC5128` (`ALMOSTRO`; read)
- `0x005BA8D6` → RVA `0x00F21F28` (`.data`; read/write)
- `0x005BA8E5` → RVA `0x00FCF000` (`CACHEALI`; read/write)
- `0x005BA984` → RVA `0x00FC6BA7` (`ALMOSTRO`; read)
- `0x005BA98D` → RVA `0x00F21FB8` (`.data`; read)
- `0x005BA999` → RVA `0x00F21F80` (`.data`; read)
- `0x005BA9AB` → RVA `0x00F21FC4` (`.data`; read/write)
- `0x005BA9B1` → RVA `0x00F21FB8` (`.data`; read/write)
- `0x005BA9BF` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x005BA9CA` → RVA `0x00F21FC4` (`.data`; read)
- `0x005BAA03` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x005BAA1C` → RVA `0x00F21F88` (`.data`; read)
- `0x005BAA37` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x005BAAB5` → RVA `0x00FC50EC` (`ALMOSTRO`; read)
- `0x005BAB00` → RVA `0x00FC549C` (`ALMOSTRO`; read)
- `0x005BAB25` → RVA `0x00E00AF0` (`.data`; read)
- `0x005BAB62` → RVA `0x00F21FB8` (`.data`; write)
- `0x005BAB7B` → RVA `0x00E070D8` (`.data`; read)
- `0x005BAB91` → RVA `0x000484E4` (`.rdata`; read)
- `0x005BABFA` → RVA `0x00F21FAD` (`.data`; write)
- `0x005BAC0A` → RVA `0x00F21FAC` (`.data`; write)
- `0x005BAC26` → RVA `0x00F21F30` (`.data`; read/write)
- `0x005BAC33` → RVA `0x00F21F68` (`.data`; read)
- `0x005BAC47` → RVA `0x00F21F68` (`.data`; write)
- `0x005BAC4E` → RVA `0x00F21F60` (`.data`; read)
- `0x005BAC57` → RVA `0x00F21F60` (`.data`; write)
- `0x005BAC63` → RVA `0x00F22260` (`.data`; write)
- `0x005BAC6A` → RVA `0x00F232F8` (`.data`; read)
- `0x005BAC72` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x005BAC7F` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x005BACA2` → RVA `0x00F21F88` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BA820  48 8B C4                        mov rax, rsp
005BA823  48 89 58 08                     mov qword ptr [rax + 8], rbx
005BA827  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005BA82B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
005BA82F  55                              push rbp
005BA830  41 54                           push r12
005BA832  41 55                           push r13
005BA834  41 56                           push r14
005BA836  41 57                           push r15
005BA838  48 8D 68 C8                     lea rbp, [rax - 0x38]
005BA83C  48 81 EC 10 01 00 00            sub rsp, 0x110
005BA843  48 8B 05 F6 FE 84 00            mov rax, qword ptr [rip + 0x84fef6]
005BA84A  48 33 C4                        xor rax, rsp
005BA84D  48 89 45 00                     mov qword ptr [rbp], rax
005BA851  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
005BA855  33 FF                           xor edi, edi
005BA857  48 83 64 24 60 00               and qword ptr [rsp + 0x60], 0
005BA85D  4D 8B F9                        mov r15, r9
005BA860  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
005BA869  41 8A F0                        mov sil, r8b
005BA86C  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
005BA872  44 8A E1                        mov r12b, cl
005BA875  48 83 65 88 00                  and qword ptr [rbp - 0x78], 0
005BA87A  44 8D 77 04                     lea r14d, [rdi + 4]
005BA87E  40 38 3D 3F C3 A0 00            cmp byte ptr [rip + 0xa0c33f], dil
005BA885  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
005BA889  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
005BA88D  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
005BA891  88 54 24 51                     mov byte ptr [rsp + 0x51], dl
005BA895  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
005BA899  C7 44 24 54 0D 00 00 00         mov dword ptr [rsp + 0x54], 0xd
005BA8A1  0F 84 5C 01 00 00               je 0x1405baa03
005BA8A7  90                              nop
005BA8A8  40 38 3D B5 AA A0 00            cmp byte ptr [rip + 0xa0aab5], dil
005BA8AF  0F 85 4E 01 00 00               jne 0x1405baa03
005BA8B5  8B 05 05 77 96 00               mov eax, dword ptr [rip + 0x967705]
005BA8BB  4C 3B C8                        cmp r9, rax
005BA8BE  77 0A                           ja 0x1405ba8ca
005BA8C0  BF 02 00 00 00                  mov edi, 2
005BA8C5  E9 39 01 00 00                  jmp 0x1405baa03
005BA8CA  48 8B 05 57 A8 A0 00            mov rax, qword ptr [rip + 0xa0a857]
005BA8D1  4C 3B C8                        cmp r9, rax
005BA8D4  76 09                           jbe 0x1405ba8df
005BA8D6  FF 05 4C 76 96 00               inc dword ptr [rip + 0x96764c]
005BA8DC  4C 8B F8                        mov r15, rax
005BA8DF  41 BE 03 00 00 00               mov r14d, 3
005BA8E5  44 87 35 14 47 A1 00            xchg dword ptr [rip + 0xa14714], r14d
005BA8EC  E8 D3 48 01 00                  call 0x1405cf1c4
005BA8F1  84 C0                           test al, al
005BA8F3  75 0A                           jne 0x1405ba8ff
005BA8F5  BF 01 00 00 00                  mov edi, 1
005BA8FA  E9 04 01 00 00                  jmp 0x1405baa03
005BA8FF  45 84 E4                        test r12b, r12b
005BA902  75 13                           jne 0x1405ba917
005BA904  E8 C7 8F DE FF                  call 0x1403a38d0
005BA909  84 C0                           test al, al
005BA90B  74 0A                           je 0x1405ba917
005BA90D  BF 06 00 00 00                  mov edi, 6
005BA912  E9 EC 00 00 00                  jmp 0x1405baa03
005BA917  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
005BA91B  48 BB 08 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000008
005BA925  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005BA92A  45 8A CC                        mov r9b, r12b
005BA92D  48 8D 44 24 54                  lea rax, [rsp + 0x54]
005BA932  B2 01                           mov dl, 1
005BA934  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005BA939  49 8B CD                        mov rcx, r13
005BA93C  48 8B 1B                        mov rbx, qword ptr [rbx]
005BA93F  48 8D 44 24 58                  lea rax, [rsp + 0x58]
005BA944  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005BA949  4C 8B C3                        mov r8, rbx
005BA94C  8A 44 24 51                     mov al, byte ptr [rsp + 0x51]
005BA950  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
005BA955  88 44 24 20                     mov byte ptr [rsp + 0x20], al
005BA959  E8 02 26 00 00                  call 0x1405bcf60
005BA95E  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
005BA963  40 38 7D 60                     cmp byte ptr [rbp + 0x60], dil
005BA967  0F 85 3C 01 00 00               jne 0x1405baaa9
005BA96D  8B 05 4D 76 96 00               mov eax, dword ptr [rip + 0x96764d]
005BA973  48 03 C3                        add rax, rbx
005BA976  48 3B F0                        cmp rsi, rax
005BA979  0F 86 41 FF FF FF               jbe 0x1405ba8c0
005BA97F  45 84 E4                        test r12b, r12b
005BA982  75 5C                           jne 0x1405ba9e0
005BA984  40 38 3D 1C C2 A0 00            cmp byte ptr [rip + 0xa0c21c], dil
005BA98B  74 53                           je 0x1405ba9e0
005BA98D  48 8B 0D 24 76 96 00            mov rcx, qword ptr [rip + 0x967624]
005BA994  48 85 C9                        test rcx, rcx
005BA997  74 1F                           je 0x1405ba9b8
005BA999  48 8B 05 E0 75 96 00            mov rax, qword ptr [rip + 0x9675e0]
005BA9A0  48 2B C1                        sub rax, rcx
005BA9A3  48 3D 10 27 00 00               cmp rax, 0x2710
005BA9A9  73 06                           jae 0x1405ba9b1
005BA9AB  FF 05 13 76 96 00               inc dword ptr [rip + 0x967613]
005BA9B1  48 21 3D 00 76 96 00            and qword ptr [rip + 0x967600], rdi
005BA9B8  48 2B 1D C1 75 96 00            sub rbx, qword ptr [rip + 0x9675c1]
005BA9BF  8B 05 DB C0 A0 00               mov eax, dword ptr [rip + 0xa0c0db]
005BA9C5  48 3B D8                        cmp rbx, rax
005BA9C8  73 10                           jae 0x1405ba9da
005BA9CA  83 3D F3 75 96 00 03            cmp dword ptr [rip + 0x9675f3], 3
005BA9D1  76 0D                           jbe 0x1405ba9e0
005BA9D3  BF 03 00 00 00                  mov edi, 3
005BA9D8  EB 29                           jmp 0x1405baa03
005BA9DA  21 3D E4 75 96 00               and dword ptr [rip + 0x9675e4], edi
005BA9E0  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005BA9E4  E8 D7 FA C4 FF                  call 0x14020a4c0
005BA9E9  8B 0D D1 75 96 00               mov ecx, dword ptr [rip + 0x9675d1]
005BA9EF  4C 8B E0                        mov r12, rax
005BA9F2  48 03 C8                        add rcx, rax
005BA9F5  48 3B F1                        cmp rsi, rcx
005BA9F8  0F 87 B7 00 00 00               ja 0x1405baab5
005BA9FE  BF 04 00 00 00                  mov edi, 4
005BAA03  80 3D 7B C0 A0 00 00            cmp byte ptr [rip + 0xa0c07b], 0
005BAA0A  74 07                           je 0x1405baa13
005BAA0C  33 C9                           xor ecx, ecx
005BAA0E  E8 89 FA FF FF                  call 0x1405ba49c
005BAA13  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
005BAA17  48 85 C9                        test rcx, rcx
005BAA1A  74 0A                           je 0x1405baa26
005BAA1C  48 8B 05 65 75 96 00            mov rax, qword ptr [rip + 0x967565]
005BAA23  48 89 01                        mov qword ptr [rcx], rax
005BAA26  41 83 FE 04                     cmp r14d, 4
005BAA2A  74 07                           je 0x1405baa33
005BAA2C  44 87 35 CD 45 A1 00            xchg dword ptr [rip + 0xa145cd], r14d
005BAA33  85 FF                           test edi, edi
005BAA35  74 44                           je 0x1405baa7b
005BAA37  F7 05 C7 C0 A0 00 00 00 10 00   test dword ptr [rip + 0xa0c0c7], 0x100000
005BAA41  89 7D 80                        mov dword ptr [rbp - 0x80], edi
005BAA44  74 35                           je 0x1405baa7b
005BAA46  83 65 AC 00                     and dword ptr [rbp - 0x54], 0
005BAA4A  48 8D 45 80                     lea rax, [rbp - 0x80]
005BAA4E  41 B9 59 0F 00 00               mov r9d, 0xf59
005BAA54  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
005BAA58  BA 01 00 00 00                  mov edx, 1
005BAA5D  C7 45 A8 01 00 00 00            mov dword ptr [rbp - 0x58], 1
005BAA64  41 B8 00 00 10 40               mov r8d, 0x40100000
005BAA6A  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
005BAA72  48 8D 4D A0                     lea rcx, [rbp - 0x60]
005BAA76  E8 D5 A8 C7 FF                  call 0x140235350
005BAA7B  48 8B 4D 00                     mov rcx, qword ptr [rbp]
005BAA7F  48 33 CC                        xor rcx, rsp
005BAA82  E8 B9 1B 0F 00                  call 0x1406ac640
005BAA87  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
005BAA8F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005BAA93  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
005BAA97  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
005BAA9B  49 8B E3                        mov rsp, r11
005BAA9E  41 5F                           pop r15
005BAAA0  41 5E                           pop r14
005BAAA2  41 5D                           pop r13
005BAAA4  41 5C                           pop r12
005BAAA6  5D                              pop rbp
005BAAA7  C3                              ret
005BAAA8  CC                              int3
005BAAA9  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005BAAAD  E8 0E FA C4 FF                  call 0x14020a4c0
005BAAB2  4C 8B E0                        mov r12, rax
005BAAB5  8B 05 31 A6 A0 00               mov eax, dword ptr [rip + 0xa0a631]
005BAABB  49 03 C4                        add rax, r12
005BAABE  48 3B F0                        cmp rsi, rax
005BAAC1  0F 86 37 FF FF FF               jbe 0x1405ba9fe
005BAAC7  48 8B DE                        mov rbx, rsi
005BAACA  49 2B DC                        sub rbx, r12
005BAACD  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
005BAAD2  49 3B DF                        cmp rbx, r15
005BAAD5  76 16                           jbe 0x1405baaed
005BAAD7  49 2B DF                        sub rbx, r15
005BAADA  48 8B C3                        mov rax, rbx
005BAADD  49 8B DF                        mov rbx, r15
005BAAE0  48 2B F0                        sub rsi, rax
005BAAE3  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
005BAAE8  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
005BAAED  44 8A 7D 60                     mov r15b, byte ptr [rbp + 0x60]
005BAAF1  40 8A 74 24 50                  mov sil, byte ptr [rsp + 0x50]
005BAAF6  45 84 FF                        test r15b, r15b
005BAAF9  74 2A                           je 0x1405bab25
005BAAFB  40 84 F6                        test sil, sil
005BAAFE  75 25                           jne 0x1405bab25
005BAB00  8B 05 96 A9 A0 00               mov eax, dword ptr [rip + 0xa0a996]
005BAB06  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
005BAB0B  8B C8                           mov ecx, eax
005BAB0D  48 3B D8                        cmp rbx, rax
005BAB10  76 13                           jbe 0x1405bab25
005BAB12  48 8B C3                        mov rax, rbx
005BAB15  48 2B C1                        sub rax, rcx
005BAB18  48 2B D8                        sub rbx, rax
005BAB1B  48 29 44 24 58                  sub qword ptr [rsp + 0x58], rax
005BAB20  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
005BAB25  48 8B 05 C4 5F 84 00            mov rax, qword ptr [rip + 0x845fc4]
005BAB2C  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
005BAB31  48 8B D3                        mov rdx, rbx
005BAB34  B9 01 00 00 00                  mov ecx, 1
005BAB39  E8 92 FF 0F 00                  call 0x1406baad0
005BAB3E  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
005BAB43  44 8B C3                        mov r8d, ebx
005BAB46  49 8B D4                        mov rdx, r12
005BAB49  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
005BAB4E  49 8B CD                        mov rcx, r13
005BAB51  E8 42 C1 EA FF                  call 0x140466c98
005BAB56  B1 01                           mov cl, 1
005BAB58  E8 97 55 E8 FF                  call 0x1404400f4
005BAB5D  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
005BAB62  4C 89 25 4F 74 96 00            mov qword ptr [rip + 0x96744f], r12
005BAB69  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
005BAB6E  41 8B D6                        mov edx, r14d
005BAB71  B9 01 00 00 00                  mov ecx, 1
005BAB76  E8 21 7C EA FF                  call 0x14046279c
005BAB7B  83 3D 56 C5 84 00 05            cmp dword ptr [rip + 0x84c556], 5
005BAB82  76 71                           jbe 0x1405babf5
005BAB84  48 8D 44 24 70                  lea rax, [rsp + 0x70]
005BAB89  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
005BAB8D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005BAB91  48 8D 15 4C D9 A8 FF            lea rdx, [rip - 0x5726b4]
005BAB98  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
005BAB9C  48 8D 0D 35 C5 84 00            lea rcx, [rip + 0x84c535]
005BABA3  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
005BABA7  45 33 C9                        xor r9d, r9d
005BABAA  48 8D 44 24 74                  lea rax, [rsp + 0x74]
005BABAF  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
005BABB7  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005BABBB  45 33 C0                        xor r8d, r8d
005BABBE  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
005BABC2  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005BABC6  48 8D 44 24 78                  lea rax, [rsp + 0x78]
005BABCB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005BABCF  48 8D 45 B0                     lea rax, [rbp - 0x50]
005BABD3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005BABD8  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
005BABE0  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
005BABE8  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
005BABF0  E8 EB B4 E6 FF                  call 0x1404260e0
005BABF5  45 84 FF                        test r15b, r15b
005BABF8  74 07                           je 0x1405bac01
005BABFA  C6 05 AC 73 96 00 01            mov byte ptr [rip + 0x9673ac], 1
005BAC01  E8 CA 8C DE FF                  call 0x1403a38d0
005BAC06  84 C0                           test al, al
005BAC08  74 07                           je 0x1405bac11
005BAC0A  C6 05 9B 73 96 00 01            mov byte ptr [rip + 0x96739b], 1
005BAC11  40 38 3D 6D BE A0 00            cmp byte ptr [rip + 0xa0be6d], dil
005BAC18  41 88 7D 21                     mov byte ptr [r13 + 0x21], dil
005BAC1C  74 08                           je 0x1405bac26
005BAC1E  49 8B CD                        mov rcx, r13
005BAC21  E8 7A 09 00 00                  call 0x1405bb5a0
005BAC26  48 FF 05 03 73 96 00            inc qword ptr [rip + 0x967303]
005BAC2D  41 BE 01 00 00 00               mov r14d, 1
005BAC33  48 3B 1D 2E 73 96 00            cmp rbx, qword ptr [rip + 0x96732e]
005BAC3A  41 C7 85 90 95 00 00 01 00 00 00  mov dword ptr [r13 + 0x9590], 1
005BAC45  73 07                           jae 0x1405bac4e
005BAC47  48 89 1D 1A 73 96 00            mov qword ptr [rip + 0x96731a], rbx
005BAC4E  48 3B 1D 0B 73 96 00            cmp rbx, qword ptr [rip + 0x96730b]
005BAC55  76 07                           jbe 0x1405bac5e
005BAC57  48 89 1D 02 73 96 00            mov qword ptr [rip + 0x967302], rbx
005BAC5E  40 84 F6                        test sil, sil
005BAC61  74 07                           je 0x1405bac6a
005BAC63  44 88 35 F6 75 96 00            mov byte ptr [rip + 0x9675f6], r14b
005BAC6A  8B 05 88 86 96 00               mov eax, dword ptr [rip + 0x968688]
005BAC70  85 C0                           test eax, eax
005BAC72  8B 05 08 BE A0 00               mov eax, dword ptr [rip + 0xa0be08]
005BAC78  0F 9F C2                        setg dl
005BAC7B  85 C0                           test eax, eax
005BAC7D  74 1B                           je 0x1405bac9a
005BAC7F  4C 8D 15 BA DF A0 00            lea r10, [rip + 0xa0dfba]
005BAC86  44 8B D8                        mov r11d, eax
005BAC89  49 8B 0A                        mov rcx, qword ptr [r10]
005BAC8C  E8 03 87 EA FF                  call 0x140463394
005BAC91  4D 8D 52 08                     lea r10, [r10 + 8]
005BAC95  4D 2B DE                        sub r11, r14
005BAC98  75 EF                           jne 0x1405bac89
005BAC9A  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
005BAC9F  49 03 CC                        add rcx, r12
005BACA2  48 89 0D DF 72 96 00            mov qword ptr [rip + 0x9672df], rcx
005BACA9  49 89 8D 80 95 00 00            mov qword ptr [r13 + 0x9580], rcx
005BACB0  45 88 B5 09 96 00 00            mov byte ptr [r13 + 0x9609], r14b
005BACB7  E9 57 FD FF FF                  jmp 0x1405baa13
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KePrepareClockTimerForPlatformIdle(unsigned __int8 a1, unsigned __int8 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int8 v_stack_m110;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int8 v_stack_mC0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int8 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 8716022)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 56) = result;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = *(unsigned __int64 *)(v_rsp - 56 + 104);
    *(unsigned __int64 *)(v_rsp - 56 - 104) = *(unsigned __int64 *)(v_rsp - 56 + 112);
    v_stack_mE7 = a2;
    v_stack_mE8 = a1;
    v_stack_mE4 = 13;
    if ((*(unsigned __int8 *)(v_rip + 10535743)) == 0) goto loc_005BAA03;
    if ((*(unsigned __int8 *)(v_rip + 10529461)) != 0) goto loc_005BAA03;
    if (a4 > ((unsigned int)(*(unsigned int *)(v_rip + 9860869)))) goto loc_005BA8CA;
loc_005BA8C0:
    goto loc_005BAA03;
loc_005BA8CA:
    v_r15 = a4;
    if (a4 >= = (*(unsigned __int64 *)(v_rip + 10528855))) {
        v_r15 = *(unsigned __int64 *)(v_rip + 10528855);
    }
    result = PoAllProcessorsDeepIdle(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_005BA8FF;
    goto loc_005BAA03;
loc_005BA8FF:
    if (a1 != 0) goto loc_005BA917;
    result = KeIsForceIdleEngaged(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005BA917;
    goto loc_005BAA03;
loc_005BA917:
    v_stack_mF8 = *(unsigned __int64 *)(v_rsp - 56 - 112);
    v_stack_m100 = v_stack_mE4;
    v_stack_m108 = v_stack_mE0;
    v_stack_m110 = a3;
    v_stack_m118 = (unsigned __int8)(v_stack_mE7);
    result = KiGetNextTimerExpirationDueTime(*(unsigned __int64 *)(gs_base + (0 + 32)), 1, *(unsigned __int64 *)(v_rbx), a1);
    if ((*(unsigned __int8 *)(v_rsp - 56 + 96)) != 6) goto loc_005BAAA9;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 9860685))) + (*(unsigned __int64 *)(v_rbx));
    if (v_stack_mE0 <= result) goto loc_005BA8C0;
    if (a1 != 0) goto loc_005BA9E0;
    if ((*(unsigned __int8 *)(v_rip + 10535452)) == 6) goto loc_005BA9E0;
    if (*(unsigned __int64 *)(v_rip + 9860644) == 0) goto loc_005BA9B8;
    result = (*(unsigned __int64 *)(v_rip + 9860576)) - (*(unsigned __int64 *)(v_rip + 9860644));
    if (result < 0x2710ULL) {
    }
loc_005BA9B8:
    v_rbx = (*(unsigned __int64 *)(v_rbx)) - (*(unsigned __int64 *)(v_rip + 9860545));
    if (v_rbx >= ((unsigned int)(*(unsigned int *)(v_rip + 10535131)))) goto loc_005BA9DA;
    if ((*(unsigned int *)(v_rip + 9860595)) <= 3) goto loc_005BA9E0;
    goto loc_005BAA03;
loc_005BA9DA:
loc_005BA9E0:
    result = RtlGetInterruptTimePrecise(v_rsp - 56 - 120, 1, *(unsigned __int64 *)(v_rbx), a1);
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 9860561))) + (result);
    if (v_stack_mE0 > a1) goto loc_005BAAB5;
loc_005BA9FE:
loc_005BAA03:
    if ((*(unsigned __int8 *)(v_rip + 10535035)) != 0) {
        a1 = 0;
        result = KePrepareClockTimerForIdle(a1, 1, *(unsigned __int64 *)(v_rbx), a1);
    }
    if (*(unsigned __int64 *)(v_rsp - 56 - 104) != 0) {
        result = *(unsigned __int64 *)(v_rip + 9860453);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 56 - 104)) = result;
    }
    if (3 != 4) {
    }
    if (4 == 0) goto loc_005BAA7B;
    *(unsigned int *)(v_rsp - 56 - 128) = 4;
    if (((*(unsigned int *)(v_rip + 10535111)) & (0x100000ULL)) != 0) {
        result = v_rsp - 56 - 128;
        a4 = 0xF59ULL;
        *(unsigned __int64 *)(v_rsp - 56 - 96) = result;
        a2 = 1;
        *(unsigned int *)(v_rsp - 56 - 88) = 1;
        a3 = 0x40100000ULL;
        v_stack_m118 = 0x602ULL;
        a1 = v_rsp - 56 - 96;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 56)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_005BAAA9:
    result = RtlGetInterruptTimePrecise(v_rsp - 56 - 120, a2, a3, a4);
loc_005BAAB5:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 10528305))) + (result);
    if ((*(unsigned __int64 *)(v_stack_m28 + 56)) <= result) goto loc_005BA9FE;
    v_rbx = (*(unsigned __int64 *)(v_stack_m28 + 56)) - (result);
    v_stack_mA8 = v_rbx;
    v_rsi = *(unsigned __int64 *)(v_stack_m28 + 56);
    if (v_rbx >= = v_r15) {
        v_rbx = (v_rbx) - (v_r15);
        result = v_rbx;
        v_rbx = v_r15;
        v_rsi = (*(unsigned __int64 *)(v_stack_m28 + 56)) - (result);
        v_stack_mA8 = v_rbx;
        v_stack_mB8 = v_rsi;
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 56 + 96)) == 0) goto loc_005BAB25;
    if ((unsigned __int8)(v_stack_mC0) != 0) goto loc_005BAB25;
    result = (unsigned int)(*(unsigned int *)(v_rip + 10529174));
    v_rbx = v_stack_mA8;
    if (v_stack_mA8 >= = ((unsigned int)(*(unsigned int *)(v_rip + 10529174)))) {
        result = v_stack_mA8;
        result = (result) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10529174)))));
        v_rbx = (v_stack_mA8) - (result);
        v_stack_mA8 = v_rbx;
    }
    result = guard_dispatch_icall(1, v_rbx, v_stack_mB0, a4);
    v_stack_mF0 = 1;
    result = KiLogClockIncrementUpdate(*(unsigned __int64 *)(gs_base + (0 + 32)), result, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_mB0));
    result = KiSetPendingTick(1, result, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_mB0));
    *(unsigned __int64 *)(v_rip + 9860175) = result;
    result = KiEventClockStateChange(1, 3, v_stack_mB0, v_stack_mA8);
    if ((*(unsigned int *)(v_rip + 8701270)) >= = 5) {
        result = v_stack_mA0;
        v_stack_mA0 = (unsigned int)(v_rbx);
        *(unsigned __int64 *)(v_rsp - 56 - 48) = result;
        a2 = v_rip - 5711540;
        result = v_stack_mB0;
        a1 = v_rip + 8701237;
        v_stack_m9C = (unsigned int)(result);
        a4 = 0;
        result = v_stack_m9C;
        *(unsigned __int64 *)(v_rsp - 56 - 40) = 4;
        *(unsigned __int64 *)(v_rsp - 56 - 32) = result;
        a3 = 0;
        result = v_stack_mBC;
        v_stack_m98 = (unsigned int)(result);
        result = v_stack_m98;
        *(unsigned __int64 *)(v_rsp - 56 - 16) = result;
        result = v_rsp - 56 - 80;
        v_stack_mE8 = result;
        v_stack_mF0 = 5;
        *(unsigned __int64 *)(v_rsp - 56 - 24) = 4;
        *(unsigned __int64 *)(v_rsp - 56 - 8) = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 56 + 96)) != 0) {
        *(unsigned __int8 *)(v_rip + 9860012) = 1;
    }
    result = KeIsForceIdleEngaged(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 9859995) = 1;
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33) = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if ((*(unsigned __int8 *)(v_rip + 10534509)) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)))) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiCancelClockTimerKTimerDeadlines(a1, a2, a3, a4);
    }
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38288) = 1;
    if (v_rbx < (*(unsigned __int64 *)(v_rip + 9859886))) {
        *(unsigned __int64 *)(v_rip + 9859866) = v_rbx;
    }
    if (v_rbx >= = (*(unsigned __int64 *)(v_rip + 9859851))) {
        *(unsigned __int64 *)(v_rip + 9859842) = v_rbx;
    }
    if ((unsigned __int8)(v_stack_mC0) != 0) {
        *(unsigned __int8 *)(v_rip + 9860598) = 1;
    }
    a2 = (condition_is_greater) ? 1 : 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10534408))) == 0) goto loc_005BAC9A;
loc_005BAC89:
    result = KiSetVpThreadHrTimerActive(*(unsigned __int64 *)(v_rip + 10543034), a2, a3, a4);
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10534408))))) - (1);
    if (condition_is_not_equal) goto loc_005BAC89;
loc_005BAC9A:
    a1 = (v_stack_mB0) + (result);
    *(unsigned __int64 *)(v_rip + 9859807) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272) = a1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38409) = 1;
    goto loc_005BAA13;
}
```

## 5. (Beta) C Style

```c
int64_t KePrepareClockTimerForPlatformIdle(uint8_t Arg1, uint8_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint8_t v_stack_m110;
    uint8_t v_stack_m118;
    uint64_t v_stack_m28;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint8_t v_stack_mC0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint8_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x84FEF6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x38) = result;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = *(uint64_t *)(local_rsp - 0x38 + 0x68);
    *(uint64_t *)(local_rsp - 0x38 - 0x68) = *(uint64_t *)(local_rsp - 0x38 + 0x70);
    v_stack_mE7 = Arg2;
    v_stack_mE8 = Arg1;
    v_stack_mE4 = 13;
    if ((*(uint8_t *)(v_rip + 0xA0C33F)) == 0) goto loc_005BAA03;
    if ((*(uint8_t *)(v_rip + 0xA0AAB5)) != 0) goto loc_005BAA03;
    if (Arg4 > ((uint32_t)(*(uint32_t *)(v_rip + 0x967705)))) goto loc_005BA8CA;
loc_005BA8C0:
    goto loc_005BAA03;
loc_005BA8CA:
    local_r15 = Arg4;
    if (Arg4 >= = (*(uint64_t *)(v_rip + 0xA0A857))) {
        local_r15 = *(uint64_t *)(v_rip + 0xA0A857);
    }
    result = PoAllProcessorsDeepIdle(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_005BA8FF;
    goto loc_005BAA03;
loc_005BA8FF:
    if (Arg1 != 0) goto loc_005BA917;
    result = KeIsForceIdleEngaged(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_005BA917;
    goto loc_005BAA03;
loc_005BA917:
    v_stack_mF8 = *(uint64_t *)(local_rsp - 0x38 - 0x70);
    v_stack_m100 = v_stack_mE4;
    v_stack_m108 = v_stack_mE0;
    v_stack_m110 = Arg3;
    v_stack_m118 = (uint8_t)(v_stack_mE7);
    result = KiGetNextTimerExpirationDueTime(*(uint64_t *)(gs_base + (0 + 0x20)), 1, *(uint64_t *)(local_rbx), Arg1);
    if ((*(uint8_t *)(local_rsp - 0x38 + 0x60)) != 6) goto loc_005BAAA9;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x96764D))) + (*(uint64_t *)(local_rbx));
    if (v_stack_mE0 <= result) goto loc_005BA8C0;
    if (Arg1 != 0) goto loc_005BA9E0;
    if ((*(uint8_t *)(v_rip + 0xA0C21C)) == 6) goto loc_005BA9E0;
    if (*(uint64_t *)(v_rip + 0x967624) == 0) goto loc_005BA9B8;
    result = (*(uint64_t *)(v_rip + 0x9675E0)) - (*(uint64_t *)(v_rip + 0x967624));
    if (result < 0x2710ULL) {
    }
loc_005BA9B8:
    local_rbx = (*(uint64_t *)(local_rbx)) - (*(uint64_t *)(v_rip + 0x9675C1));
    if (local_rbx >= ((uint32_t)(*(uint32_t *)(v_rip + 0xA0C0DB)))) goto loc_005BA9DA;
    if ((*(uint32_t *)(v_rip + 0x9675F3)) <= 3) goto loc_005BA9E0;
    goto loc_005BAA03;
loc_005BA9DA:
loc_005BA9E0:
    result = RtlGetInterruptTimePrecise(local_rsp - 56 - 120, 1, *(uint64_t *)(local_rbx), Arg1);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0x9675D1))) + (result);
    if (v_stack_mE0 > Arg1) goto loc_005BAAB5;
loc_005BA9FE:
loc_005BAA03:
    if ((*(uint8_t *)(v_rip + 0xA0C07B)) != 0) {
        Arg1 = 0;
        result = KePrepareClockTimerForIdle(Arg1, 1, *(uint64_t *)(local_rbx), Arg1);
    }
    if (*(uint64_t *)(local_rsp - 0x38 - 0x68) != 0) {
        result = *(uint64_t *)(v_rip + 0x967565);
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x38 - 0x68)) = result;
    }
    if (3 != 4) {
    }
    if (4 == 0) goto loc_005BAA7B;
    *(uint32_t *)(local_rsp - 0x38 - 0x80) = 4;
    if (((*(uint32_t *)(v_rip + 0xA0C0C7)) & (0x100000ULL)) != 0) {
        result = local_rsp - 56 - 128;
        Arg4 = 0xF59ULL;
        *(uint64_t *)(local_rsp - 0x38 - 0x60) = result;
        Arg2 = 1;
        *(uint32_t *)(local_rsp - 0x38 - 0x58) = 1;
        Arg3 = 0x40100000ULL;
        v_stack_m118 = 0x602ULL;
        Arg1 = local_rsp - 56 - 96;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x38)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
loc_005BAAA9:
    result = RtlGetInterruptTimePrecise(local_rsp - 56 - 120, Arg2, Arg3, Arg4);
loc_005BAAB5:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0xA0A631))) + (result);
    if ((*(uint64_t *)(v_stack_m28 + 0x38)) <= result) goto loc_005BA9FE;
    local_rbx = (*(uint64_t *)(v_stack_m28 + 0x38)) - (result);
    v_stack_mA8 = local_rbx;
    local_rsi = *(uint64_t *)(v_stack_m28 + 0x38);
    if (local_rbx >= = local_r15) {
        local_rbx = (local_rbx) - (local_r15);
        result = local_rbx;
        local_rbx = local_r15;
        local_rsi = (*(uint64_t *)(v_stack_m28 + 0x38)) - (result);
        v_stack_mA8 = local_rbx;
        v_stack_mB8 = local_rsi;
    }
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x38 + 0x60)) == 0) goto loc_005BAB25;
    if ((uint8_t)(v_stack_mC0) != 0) goto loc_005BAB25;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA0A996));
    local_rbx = v_stack_mA8;
    if (v_stack_mA8 >= = ((uint32_t)(*(uint32_t *)(v_rip + 0xA0A996)))) {
        result = v_stack_mA8;
        result = (result) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0A996)))));
        local_rbx = (v_stack_mA8) - (result);
        v_stack_mA8 = local_rbx;
    }
    result = guard_dispatch_icall(1, local_rbx, v_stack_mB0, Arg4);
    v_stack_mF0 = 1;
    result = KiLogClockIncrementUpdate(*(uint64_t *)(gs_base + (0 + 0x20)), result, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_mB0));
    result = KiSetPendingTick(1, result, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_mB0));
    *(uint64_t *)(v_rip + 0x96744F) = result;
    result = KiEventClockStateChange(1, 3, v_stack_mB0, v_stack_mA8);
    if ((*(uint32_t *)(v_rip + 0x84C556)) >= = 5) {
        result = v_stack_mA0;
        v_stack_mA0 = (uint32_t)(local_rbx);
        *(uint64_t *)(local_rsp - 0x38 - 0x30) = result;
        Arg2 = v_rip - 5711540;
        result = v_stack_mB0;
        Arg1 = v_rip + 8701237;
        v_stack_m9C = (uint32_t)(result);
        Arg4 = 0;
        result = v_stack_m9C;
        *(uint64_t *)(local_rsp - 0x38 - 0x28) = 4;
        *(uint64_t *)(local_rsp - 0x38 - 0x20) = result;
        Arg3 = 0;
        result = v_stack_mBC;
        v_stack_m98 = (uint32_t)(result);
        result = v_stack_m98;
        *(uint64_t *)(local_rsp - 0x38 - 0x10) = result;
        result = local_rsp - 56 - 80;
        v_stack_mE8 = result;
        v_stack_mF0 = 5;
        *(uint64_t *)(local_rsp - 0x38 - 0x18) = 4;
        *(uint64_t *)(local_rsp - 0x38 - 0x8) = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x38 + 0x60)) != 0) {
        *(uint8_t *)(v_rip + 0x9673AC) = 1;
    }
    result = KeIsForceIdleEngaged(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x96739B) = 1;
    }
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21) = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    if ((*(uint8_t *)(v_rip + 0xA0BE6D)) != ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiCancelClockTimerKTimerDeadlines(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9590) = 1;
    if (local_rbx < (*(uint64_t *)(v_rip + 0x96732E))) {
        *(uint64_t *)(v_rip + 0x96731A) = local_rbx;
    }
    if (local_rbx >= = (*(uint64_t *)(v_rip + 0x96730B))) {
        *(uint64_t *)(v_rip + 0x967302) = local_rbx;
    }
    if ((uint8_t)(v_stack_mC0) != 0) {
        *(uint8_t *)(v_rip + 0x9675F6) = 1;
    }
    Arg2 = (condition_is_greater) ? 1 : 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0BE08))) == 0) goto loc_005BAC9A;
loc_005BAC89:
    result = KiSetVpThreadHrTimerActive(*(uint64_t *)(v_rip + 0xA0DFBA), Arg2, Arg3, Arg4);
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0BE08))))) - (1);
    if (condition_is_not_equal) goto loc_005BAC89;
loc_005BAC9A:
    Arg1 = (v_stack_mB0) + (result);
    *(uint64_t *)(v_rip + 0x9672DF) = Arg1;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580) = Arg1;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9609) = 1;
    goto loc_005BAA13;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BA820&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
