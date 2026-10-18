# KiIpiSendRequest

- RVA: `0x003113C0`–`0x00311A5D` (길이 `1,693` bytes)
- VA: `0x00000001403113C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074158`
- 디코드: `406`개 명령, `1,693/1,693` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00311451` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0031146A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00311733` → [KiIpiEnlightenedGuestPriorityKick](../45/KiIpiEnlightenedGuestPriorityKick_function_004536B0.md) (function, `0x004536B0`)
- `0x0031183D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00311857` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x00311874` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00311918` → [KiIpiEnlightenedGuestPriorityKick](../45/KiIpiEnlightenedGuestPriorityKick_function_004536B0.md) (function, `0x004536B0`)
- `0x00311926` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x00311947` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0031196E` → [KiSubtractAffinityEx](../2D/KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)
- `0x003119D6` → [EtwGetKernelTraceTimestamp](../39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x00311A0D` → [PerfInfoLogIpiSend](../4B/PerfInfoLogIpiSend_function_004B7AD0.md) (function, `0x004B7AD0`)
- `0x00311A57` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KeFlushProcessWriteBuffers](../2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) at `0x002CE5FE`
- [KeInvalidateRangeAllCaches](../30/KeInvalidateRangeAllCaches_function_00308880.md) at `0x003088E5`
- [KeInvalidateAllCaches](../30/KeInvalidateAllCaches_function_00308CC0.md) at `0x00308D1A`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x0030912B`
- [KxFlushEntireTb](../30/KxFlushEntireTb_function_00309094.md) at `0x0030923D`
- [KiIpiSendRequestEx](KiIpiSendRequestEx_function_003112D0.md) at `0x003112FF`
- [sub_003127BF](Unknown_function_003127BF.md) at `0x003127FB`
- [sub_003127BF](Unknown_function_003127BF.md) at `0x003129D8`
- [KxFlushNonGlobalTb](KxFlushNonGlobalTb_function_00314E50.md) at `0x00314F5A`
- [KxFlushNonGlobalTb](KxFlushNonGlobalTb_function_00314E50.md) at `0x00314F91`
- [KeQueryTotalCycleTimeThread](../37/KeQueryTotalCycleTimeThread_function_0037EF20.md) at `0x0037F98E`
- [sub_003E67E6](../3E/Unknown_function_003E67E6.md) at `0x003E689F`
- [KiIpiSendPacket](../47/KiIpiSendPacket_function_004711DC.md) at `0x00471221`
- [KeIpiGenericCall](../47/KeIpiGenericCall_function_00471720.md) at `0x004717C4`
- [KeUpdateThreadTag](../47/KeUpdateThreadTag_function_00475770.md) at `0x00475B95`

### Static image references
- `0x003113DC` → RVA `0x00E0A740` (`.data`; read)
- `0x003113F6` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x003114E2` → RVA `0x00F21AC8` (`.data`; read)
- `0x00311511` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00311518` → RVA `0x00F21AD0` (`.data`; read)
- `0x003115C0` → RVA `0x00F231B8` (`.data`; read)
- `0x0031164B` → RVA `0x00F231B0` (`.data`; read)
- `0x0031176C` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x003117F5` → RVA `0x00F10F20` (`.data`; read)
- `0x00311824` → RVA `0x00E101F0` (`.data`; read)
- `0x00311992` → RVA `0x00FC7128` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003113C0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003113C5  55                              push rbp
003113C6  56                              push rsi
003113C7  57                              push rdi
003113C8  41 54                           push r12
003113CA  41 55                           push r13
003113CC  41 56                           push r14
003113CE  41 57                           push r15
003113D0  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
003113D5  48 81 EC E0 00 00 00            sub rsp, 0xe0
003113DC  48 8B 05 5D 93 AF 00            mov rax, qword ptr [rip + 0xaf935d]
003113E3  48 33 C4                        xor rax, rsp
003113E6  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
003113EA  33 C0                           xor eax, eax
003113EC  4C 89 4D BF                     mov qword ptr [rbp - 0x41], r9
003113F0  33 FF                           xor edi, edi
003113F2  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
003113F6  F7 05 08 57 CB 00 00 00 40 00   test dword ptr [rip + 0xcb5708], 0x400000
00311400  0F 57 C9                        xorps xmm1, xmm1
00311403  0F 57 C0                        xorps xmm0, xmm0
00311406  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0031140A  49 8B F0                        mov rsi, r8
0031140D  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
00311411  44 8B E2                        mov r12d, edx
00311414  4C 8B F9                        mov r15, rcx
00311417  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
0031141B  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
0031141F  0F 11 4D EF                     movups xmmword ptr [rbp - 0x11], xmm1
00311423  0F 85 9F 05 00 00               jne 0x1403119c8
00311429  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0031142D  49 8D 9F C8 2F 00 00            lea rbx, [r15 + 0x2fc8]
00311434  33 D2                           xor edx, edx
00311436  4C 8D 73 08                     lea r14, [rbx + 8]
0031143A  48 C7 03 01 00 20 00            mov qword ptr [rbx], 0x200001
00311441  49 8B CE                        mov rcx, r14
00311444  4D 8D AF D0 30 00 00            lea r13, [r15 + 0x30d0]
0031144B  41 B8 00 01 00 00               mov r8d, 0x100
00311451  E8 EA 57 3B 00                  call 0x1406c6c40
00311456  49 8D 4D 08                     lea rcx, [r13 + 8]
0031145A  49 C7 45 00 01 00 20 00         mov qword ptr [r13], 0x200001
00311462  33 D2                           xor edx, edx
00311464  41 B8 00 01 00 00               mov r8d, 0x100
0031146A  E8 D1 57 3B 00                  call 0x1406c6c40
0031146F  0F B7 4B 02                     movzx ecx, word ptr [rbx + 2]
00311473  0F B7 D1                        movzx edx, cx
00311476  45 85 E4                        test r12d, r12d
00311479  0F 85 ED 02 00 00               jne 0x14031176c
0031147F  0F B7 06                        movzx eax, word ptr [rsi]
00311482  66 3B C1                        cmp ax, cx
00311485  66 89 4B 02                     mov word ptr [rbx + 2], cx
00311489  89 7B 04                        mov dword ptr [rbx + 4], edi
0031148C  0F B7 CF                        movzx ecx, di
0031148F  66 0F 46 D0                     cmovbe dx, ax
00311493  66 89 13                        mov word ptr [rbx], dx
00311496  66 3B FA                        cmp di, dx
00311499  0F 82 4A 04 00 00               jb 0x1403118e9
0031149F  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
003114A3  73 11                           jae 0x1403114b6
003114A5  0F B7 C1                        movzx eax, cx
003114A8  66 FF C1                        inc cx
003114AB  48 89 7C C3 08                  mov qword ptr [rbx + rax*8 + 8], rdi
003114B0  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
003114B4  72 EF                           jb 0x1403114a5
003114B6  4C 8B 65 7F                     mov r12, qword ptr [rbp + 0x7f]
003114BA  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
003114BE  49 8B C4                        mov rax, r12
003114C1  83 E0 0F                        and eax, 0xf
003114C4  48 C1 E1 07                     shl rcx, 7
003114C8  48 0B C8                        or rcx, rax
003114CB  41 C7 87 80 2D 00 00 01 00 00 00  mov dword ptr [r15 + 0x2d80], 1
003114D6  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
003114DA  8B D7                           mov edx, edi
003114DC  89 45 83                        mov dword ptr [rbp - 0x7d], eax
003114DF  0F 57 C0                        xorps xmm0, xmm0
003114E2  0F B7 05 DF 05 C1 00            movzx eax, word ptr [rip + 0xc105df]
003114E9  44 8B C7                        mov r8d, edi
003114EC  41 89 87 84 2D 00 00            mov dword ptr [r15 + 0x2d84], eax
003114F3  44 8B CF                        mov r9d, edi
003114F6  89 54 24 3C                     mov dword ptr [rsp + 0x3c], edx
003114FA  44 8B DF                        mov r11d, edi
003114FD  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00311501  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00311505  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00311509  85 C0                           test eax, eax
0031150B  0F 84 F8 01 00 00               je 0x140311709
00311511  4C 8D 15 28 77 CB 00            lea r10, [rip + 0xcb7728]
00311518  48 8B 05 B1 05 C1 00            mov rax, qword ptr [rip + 0xc105b1]
0031151F  41 8B D3                        mov edx, r11d
00311522  4C 8B 04 D0                     mov r8, qword ptr [rax + rdx*8]
00311526  4D 85 C0                        test r8, r8
00311529  0F 84 56 04 00 00               je 0x140311985
0031152F  49 8B 90 80 00 00 00            mov rdx, qword ptr [r8 + 0x80]
00311536  33 C0                           xor eax, eax
00311538  45 0F B7 80 88 00 00 00         movzx r8d, word ptr [r8 + 0x88]
00311540  0F 57 C0                        xorps xmm0, xmm0
00311543  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00311547  66 44 89 45 D7                  mov word ptr [rbp - 0x29], r8w
0031154C  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00311550  89 45 D9                        mov dword ptr [rbp - 0x27], eax
00311553  66 89 45 DD                     mov word ptr [rbp - 0x23], ax
00311557  66 44 39 03                     cmp word ptr [rbx], r8w
0031155B  0F 86 77 01 00 00               jbe 0x1403116d8
00311561  4A 23 54 C3 08                  and rdx, qword ptr [rbx + r8*8 + 8]
00311566  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
0031156A  0F 84 6C 01 00 00               je 0x1403116dc
00311570  48 8B F7                        mov rsi, rdi
00311573  66 44 89 45 B7                  mov word ptr [rbp - 0x49], r8w
00311578  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
0031157C  45 8B F0                        mov r14d, r8d
0031157F  48 89 7D A7                     mov qword ptr [rbp - 0x59], rdi
00311583  0F 1F 40 00                     nop dword ptr [rax]
00311587  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00311590  89 7D 9F                        mov dword ptr [rbp - 0x61], edi
00311593  45 8D 46 01                     lea r8d, [r14 + 1]
00311597  48 85 D2                        test rdx, rdx
0031159A  0F 84 0E 01 00 00               je 0x1403116ae
003115A0  4C 0F BC C2                     bsf r8, rdx
003115A4  41 0F B6 C0                     movzx eax, r8b
003115A8  48 0F B3 C2                     btr rdx, rax
003115AC  44 89 45 9F                     mov dword ptr [rbp - 0x61], r8d
003115B0  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
003115B4  41 8B D6                        mov edx, r14d
003115B7  C1 E2 06                        shl edx, 6
003115BA  41 0F B6 C0                     movzx eax, r8b
003115BE  03 D0                           add edx, eax
003115C0  48 8B 05 F1 1B C1 00            mov rax, qword ptr [rip + 0xc11bf1]
003115C7  8B 14 90                        mov edx, dword ptr [rax + rdx*4]
003115CA  44 8B CA                        mov r9d, edx
003115CD  4D 8B 14 D2                     mov r10, qword ptr [r10 + rdx*8]
003115D1  41 0F 0D 8A C0 9A 00 00         prefetchw byte ptr [r10 + 0x9ac0]
003115D9  8B 55 83                        mov edx, dword ptr [rbp - 0x7d]
003115DC  48 81 C2 3B 03 00 00            add rdx, 0x33b
003115E3  48 C1 E2 06                     shl rdx, 6
003115E7  49 03 D2                        add rdx, r10
003115EA  0F 0D 0A                        prefetchw byte ptr [rdx]
003115ED  48 85 F6                        test rsi, rsi
003115F0  75 0C                           jne 0x1403115fe
003115F2  F3 48 0F B8 45 CF               popcnt rax, qword ptr [rbp - 0x31]
003115F8  48 8D 72 38                     lea rsi, [rdx + 0x38]
003115FC  89 06                           mov dword ptr [rsi], eax
003115FE  48 89 72 30                     mov qword ptr [rdx + 0x30], rsi
00311602  49 83 FC 05                     cmp r12, 5
00311606  75 1B                           jne 0x140311623
00311608  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0031160C  0F 10 00                        movups xmm0, xmmword ptr [rax]
0031160F  0F 11 42 10                     movups xmmword ptr [rdx + 0x10], xmm0
00311613  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00311617  0F 11 4A 20                     movups xmmword ptr [rdx + 0x20], xmm1
0031161B  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0031161F  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00311623  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00311627  49 8B 82 C0 9A 00 00            mov rax, qword ptr [r10 + 0x9ac0]
0031162E  4C 8B C0                        mov r8, rax
00311631  48 89 02                        mov qword ptr [rdx], rax
00311634  F0 49 0F B1 92 C0 9A 00 00      lock cmpxchg qword ptr [r10 + 0x9ac0], rdx
0031163D  49 3B C0                        cmp rax, r8
00311640  75 EC                           jne 0x14031162e
00311642  48 85 C0                        test rax, rax
00311645  0F 85 2D 03 00 00               jne 0x140311978
0031164B  48 8B 05 5E 1B C1 00            mov rax, qword ptr [rip + 0xc11b5e]
00311652  C7 44 24 3C 01 00 00 00         mov dword ptr [rsp + 0x3c], 1
0031165A  46 8B 0C 88                     mov r9d, dword ptr [rax + r9*4]
0031165E  41 8B D1                        mov edx, r9d
00311661  41 0F B7 45 00                  movzx eax, word ptr [r13]
00311666  41 83 E1 3F                     and r9d, 0x3f
0031166A  C1 EA 06                        shr edx, 6
0031166D  3B C2                           cmp eax, edx
0031166F  0F 86 6B 03 00 00               jbe 0x1403119e0
00311675  4C 8D 04 D5 00 00 00 00         lea r8, [rdx*8]
0031167D  41 8B C1                        mov eax, r9d
00311680  4B 8B 54 28 08                  mov rdx, qword ptr [r8 + r13 + 8]
00311685  48 0F AB C2                     bts rdx, rax
00311689  4B 89 54 28 08                  mov qword ptr [r8 + r13 + 8], rdx
0031168E  49 8B 82 B8 8E 00 00            mov rax, qword ptr [r10 + 0x8eb8]
00311695  4C 8D 15 A4 75 CB 00            lea r10, [rip + 0xcb75a4]
0031169C  48 85 C0                        test rax, rax
0031169F  0F 85 72 03 00 00               jne 0x140311a17
003116A5  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
003116A9  E9 E2 FE FF FF                  jmp 0x140311590
003116AE  0F B7 45 B7                     movzx eax, word ptr [rbp - 0x49]
003116B2  66 FF C0                        inc ax
003116B5  44 0F B7 F0                     movzx r14d, ax
003116B9  66 44 89 75 B7                  mov word ptr [rbp - 0x49], r14w
003116BE  45 3B F0                        cmp r14d, r8d
003116C1  0F 83 F7 02 00 00               jae 0x1403119be
003116C7  4A 8B 14 F5 08 00 00 00         mov rdx, qword ptr [r14*8 + 8]
003116CF  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
003116D3  E9 BF FE FF FF                  jmp 0x140311597
003116D8  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
003116DC  41 FF C1                        inc r9d
003116DF  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
003116E4  0F B7 05 DD 03 C1 00            movzx eax, word ptr [rip + 0xc103dd]
003116EB  41 FF C3                        inc r11d
003116EE  44 3B D8                        cmp r11d, eax
003116F1  0F 82 21 FE FF FF               jb 0x140311518
003116F7  45 85 C9                        test r9d, r9d
003116FA  0F 85 A1 01 00 00               jne 0x1403118a1
00311700  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
00311705  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
00311709  49 83 FC 05                     cmp r12, 5
0031170D  74 09                           je 0x140311718
0031170F  45 85 C0                        test r8d, r8d
00311712  0F 85 F2 01 00 00               jne 0x14031190a
00311718  48 63 74 24 34                  movsxd rsi, dword ptr [rsp + 0x34]
0031171D  8D 46 FF                        lea eax, [rsi - 1]
00311720  83 F8 01                        cmp eax, 1
00311723  0F 86 6C 01 00 00               jbe 0x140311895
00311729  41 FF 87 D0 8E 00 00            inc dword ptr [r15 + 0x8ed0]
00311730  48 8B CB                        mov rcx, rbx
00311733  E8 78 1F 14 00                  call 0x1404536b0
00311738  33 C0                           xor eax, eax
0031173A  0F 57 C0                        xorps xmm0, xmm0
0031173D  89 45 97                        mov dword ptr [rbp - 0x69], eax
00311740  0F 11 45 87                     movups xmmword ptr [rbp - 0x79], xmm0
00311744  85 F6                           test esi, esi
00311746  0F 85 76 01 00 00               jne 0x1403118c2
0031174C  0F B7 0B                        movzx ecx, word ptr [rbx]
0031174F  66 3B F9                        cmp di, cx
00311752  0F 83 C7 00 00 00               jae 0x14031181f
00311758  0F B7 C7                        movzx eax, di
0031175B  48 83 7C C3 08 00               cmp qword ptr [rbx + rax*8 + 8], 0
00311761  0F 85 DC 00 00 00               jne 0x140311843
00311767  66 FF C7                        inc di
0031176A  EB E3                           jmp 0x14031174f
0031176C  66 39 0D AD 59 CB 00            cmp word ptr [rip + 0xcb59ad], cx
00311773  66 0F 46 15 A5 59 CB 00         cmovbe dx, word ptr [rip + 0xcb59a5]
0031177B  66 89 4B 02                     mov word ptr [rbx + 2], cx
0031177F  0F B7 CF                        movzx ecx, di
00311782  66 89 13                        mov word ptr [rbx], dx
00311785  89 7B 04                        mov dword ptr [rbx + 4], edi
00311788  66 3B FA                        cmp di, dx
0031178B  0F 82 01 02 00 00               jb 0x140311992
00311791  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
00311795  73 11                           jae 0x1403117a8
00311797  0F B7 C1                        movzx eax, cx
0031179A  66 FF C1                        inc cx
0031179D  48 89 7C C3 08                  mov qword ptr [rbx + rax*8 + 8], rdi
003117A2  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
003117A6  72 EF                           jb 0x140311797
003117A8  41 83 FC 01                     cmp r12d, 1
003117AC  75 33                           jne 0x1403117e1
003117AE  41 8B 4F 24                     mov ecx, dword ptr [r15 + 0x24]
003117B2  48 8B 05 F7 19 C1 00            mov rax, qword ptr [rip + 0xc119f7]
003117B9  44 8B 04 88                     mov r8d, dword ptr [rax + rcx*4]
003117BD  41 8B C8                        mov ecx, r8d
003117C0  0F B7 03                        movzx eax, word ptr [rbx]
003117C3  41 83 E0 3F                     and r8d, 0x3f
003117C7  C1 E9 06                        shr ecx, 6
003117CA  3B C1                           cmp eax, ecx
003117CC  76 13                           jbe 0x1403117e1
003117CE  48 8D 14 CB                     lea rdx, [rbx + rcx*8]
003117D2  41 8B C0                        mov eax, r8d
003117D5  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
003117D9  48 0F B3 C1                     btr rcx, rax
003117DD  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003117E1  4C 8B 65 7F                     mov r12, qword ptr [rbp + 0x7f]
003117E5  49 0F BA E4 1F                  bt r12, 0x1f
003117EA  0F 83 CA FC FF FF               jae 0x1403114ba
003117F0  41 0F BA F4 1F                  btr r12d, 0x1f
003117F5  48 8D 15 24 F7 BF 00            lea rdx, [rip + 0xbff724]
003117FC  0F B7 CF                        movzx ecx, di
003117FF  66 3B 0D 1A F7 BF 00            cmp cx, word ptr [rip + 0xbff71a]
00311806  0F 83 AE FC FF FF               jae 0x1403114ba
0031180C  0F B7 C1                        movzx eax, cx
0031180F  48 39 7C C2 08                  cmp qword ptr [rdx + rax*8 + 8], rdi
00311814  0F 85 45 01 00 00               jne 0x14031195f
0031181A  66 FF C1                        inc cx
0031181D  EB E0                           jmp 0x1403117ff
0031181F  B9 0D 00 00 C0                  mov ecx, 0xc000000d
00311824  4C 8B 05 C5 E9 AF 00            mov r8, qword ptr [rip + 0xafe9c5]
0031182B  BA 01 02 00 00                  mov edx, 0x201
00311830  4C 63 C9                        movsxd r9, ecx
00311833  B9 5C 00 00 00                  mov ecx, 0x5c
00311838  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0031183D  E8 1E BE 1E 00                  call 0x1404fd660
00311842  CC                              int3
00311843  C7 45 87 02 00 00 00            mov dword ptr [rbp - 0x79], 2
0031184A  48 89 5D 8F                     mov qword ptr [rbp - 0x71], rbx
0031184E  BA E1 00 00 00                  mov edx, 0xe1
00311853  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00311857  E8 B4 0A F4 FF                  call 0x140252310
0031185C  8B C8                           mov ecx, eax
0031185E  85 C0                           test eax, eax
00311860  78 C2                           js 0x140311824
00311862  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00311867  0F 85 8D 01 00 00               jne 0x1403119fa
0031186D  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
00311871  48 33 CC                        xor rcx, rsp
00311874  E8 C7 AD 39 00                  call 0x1406ac640
00311879  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
00311881  48 81 C4 E0 00 00 00            add rsp, 0xe0
00311888  41 5F                           pop r15
0031188A  41 5E                           pop r14
0031188C  41 5D                           pop r13
0031188E  41 5C                           pop r12
00311890  5F                              pop rdi
00311891  5E                              pop rsi
00311892  5D                              pop rbp
00311893  C3                              ret
00311894  CC                              int3
00311895  41 FF 87 CC 8E 00 00            inc dword ptr [r15 + 0x8ecc]
0031189C  E9 8F FE FF FF                  jmp 0x140311730
003118A1  41 F7 D9                        neg r9d
003118A4  41 8B C1                        mov eax, r9d
003118A7  F0 41 0F C1 87 84 2D 00 00      lock xadd dword ptr [r15 + 0x2d84], eax
003118B0  41 03 C1                        add eax, r9d
003118B3  0F 85 47 FE FF FF               jne 0x140311700
003118B9  41 89 BF 80 2D 00 00            mov dword ptr [r15 + 0x2d80], edi
003118C0  EB AB                           jmp 0x14031186d
003118C2  8B CE                           mov ecx, esi
003118C4  83 E9 01                        sub ecx, 1
003118C7  74 09                           je 0x1403118d2
003118C9  83 F9 01                        cmp ecx, 1
003118CC  0F 85 4D FF FF FF               jne 0x14031181f
003118D2  8B CE                           mov ecx, esi
003118D4  83 E9 01                        sub ecx, 1
003118D7  0F 85 47 01 00 00               jne 0x140311a24
003118DD  C7 45 87 04 00 00 00            mov dword ptr [rbp - 0x79], 4
003118E4  E9 65 FF FF FF                  jmp 0x14031184e
003118E9  48 2B F3                        sub rsi, rbx
003118EC  44 0F B7 C2                     movzx r8d, dx
003118F0  0F B7 CA                        movzx ecx, dx
003118F3  4A 8B 04 36                     mov rax, qword ptr [rsi + r14]
003118F7  49 89 06                        mov qword ptr [r14], rax
003118FA  4D 8D 76 08                     lea r14, [r14 + 8]
003118FE  49 83 E8 01                     sub r8, 1
00311902  0F 84 97 FB FF FF               je 0x14031149f
00311908  EB E9                           jmp 0x1403118f3
0031190A  85 D2                           test edx, edx
0031190C  74 48                           je 0x140311956
0031190E  41 FF 87 D0 8E 00 00            inc dword ptr [r15 + 0x8ed0]
00311915  49 8B CD                        mov rcx, r13
00311918  E8 93 1D 14 00                  call 0x1404536b0
0031191D  49 8B CD                        mov rcx, r13
00311920  89 7D 8B                        mov dword ptr [rbp - 0x75], edi
00311923  89 7D 97                        mov dword ptr [rbp - 0x69], edi
00311926  E8 55 FC FB FF                  call 0x1402d1580
0031192B  85 C0                           test eax, eax
0031192D  0F 85 06 01 00 00               jne 0x140311a39
00311933  BA E1 00 00 00                  mov edx, 0xe1
00311938  C7 45 87 02 00 00 00            mov dword ptr [rbp - 0x79], 2
0031193F  48 8D 4D 87                     lea rcx, [rbp - 0x79]
00311943  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
00311947  E8 C4 09 F4 FF                  call 0x140252310
0031194C  8B C8                           mov ecx, eax
0031194E  85 C0                           test eax, eax
00311950  0F 88 E8 00 00 00               js 0x140311a3e
00311956  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
0031195A  E9 03 FF FF FF                  jmp 0x140311862
0031195F  44 0F B7 4B 02                  movzx r9d, word ptr [rbx + 2]
00311964  4C 8B C3                        mov r8, rbx
00311967  48 8B CB                        mov rcx, rbx
0031196A  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
0031196E  E8 75 48 FC FF                  call 0x1402d61e8
00311973  E9 42 FB FF FF                  jmp 0x1403114ba
00311978  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00311980  E9 09 FD FF FF                  jmp 0x14031168e
00311985  41 FF C1                        inc r9d
00311988  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0031198D  E9 52 FD FF FF                  jmp 0x1403116e4
00311992  4C 8D 05 8F 57 CB 00            lea r8, [rip + 0xcb578f]
00311999  44 0F B7 CA                     movzx r9d, dx
0031199D  4C 8B D3                        mov r10, rbx
003119A0  0F B7 CA                        movzx ecx, dx
003119A3  4D 2B D0                        sub r10, r8
003119A6  49 8B 00                        mov rax, qword ptr [r8]
003119A9  4B 89 44 02 08                  mov qword ptr [r10 + r8 + 8], rax
003119AE  4D 8D 40 08                     lea r8, [r8 + 8]
003119B2  49 83 E9 01                     sub r9, 1
003119B6  0F 84 D5 FD FF FF               je 0x140311791
003119BC  EB E8                           jmp 0x1403119a6
003119BE  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
003119C3  E9 1C FD FF FF                  jmp 0x1403116e4
003119C8  BA 00 00 40 40                  mov edx, 0x40400000
003119CD  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
003119D2  48 8D 4D DF                     lea rcx, [rbp - 0x21]
003119D6  E8 75 E2 08 00                  call 0x14039fc50
003119DB  E9 4D FA FF FF                  jmp 0x14031142d
003119E0  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
003119E5  3B C2                           cmp eax, edx
003119E7  0F 86 A1 FC FF FF               jbe 0x14031168e
003119ED  8D 42 01                        lea eax, [rdx + 1]
003119F0  66 41 89 45 00                  mov word ptr [r13], ax
003119F5  E9 7B FC FF FF                  jmp 0x140311675
003119FA  4C 8B 45 C7                     mov r8, qword ptr [rbp - 0x39]
003119FE  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00311A02  44 8B CE                        mov r9d, esi
00311A05  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00311A0A  41 8B D4                        mov edx, r12d
00311A0D  E8 BE 60 1A 00                  call 0x1404b7ad0
00311A12  E9 56 FE FF FF                  jmp 0x14031186d
00311A17  F0 FF 40 20                     lock inc dword ptr [rax + 0x20]
00311A1B  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00311A1F  E9 6C FB FF FF                  jmp 0x140311590
00311A24  83 F9 01                        cmp ecx, 1
00311A27  0F 85 21 FE FF FF               jne 0x14031184e
00311A2D  C7 45 87 03 00 00 00            mov dword ptr [rbp - 0x79], 3
00311A34  E9 15 FE FF FF                  jmp 0x14031184e
00311A39  B9 0D 00 00 C0                  mov ecx, 0xc000000d
00311A3E  4C 8B 05 AB E7 AF 00            mov r8, qword ptr [rip + 0xafe7ab]
00311A45  BA 01 02 00 00                  mov edx, 0x201
00311A4A  4C 63 C9                        movsxd r9, ecx
00311A4D  B9 5C 00 00 00                  mov ecx, 0x5c
00311A52  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00311A57  E8 04 BC 1E 00                  call 0x1404fd660
00311A5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIpiSendRequest(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int16 v_stack_m7A;
    unsigned int v_stack_m7E;
    unsigned __int16 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 11506525)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m98 = a4;
    v_rdi = 0;
    v_stack_mE4 = a2;
    v_stack_mA0 = 0;
    v_stack_m90 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm1;
    if (((*(unsigned int *)(v_rip + 13326088)) & (0x400000ULL)) != 0) goto loc_003119C8;
    v_stack_mE8 = 0;
loc_0031142D:
    a2 = 0;
    *(unsigned __int64 *)(a1 + 12232) = 0x200001ULL;
    result = memset(a1 + 12232 + 8, a2, 256, a4);
    *(unsigned __int64 *)(a1 + 12496) = 0x200001ULL;
    a2 = 0;
    result = memset(a1 + 12496 + 8, a2, 256, a4);
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_0031176C;
    *(unsigned __int16 *)(a1 + 12232 + 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 12232 + 2));
    *(unsigned int *)(a1 + 12232 + 4) = 0;
    a2 = (unsigned __int16)(*(unsigned __int16 *)(a1 + 12232 + 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(a3))) <= ((unsigned __int16)(*(unsigned __int16 *)(a1 + 12232 + 2)))) { a2 = (unsigned __int16)(*(unsigned __int16 *)(a3)); }
    *(unsigned __int16 *)(a1 + 12232) = (unsigned __int16)(a2);
    if (0 < ((unsigned __int16)(a2))) goto loc_003118E9;
loc_0031149F:
    if (0 >= (*(unsigned __int16 *)(a1 + 12232 + 2))) goto loc_003114B6;
loc_003114A5:
    a1 = (unsigned __int16)((0) + 1);
    *(unsigned __int64 *)(a1 + 12232 + 0 * 8 + 8) = 0;
    if (((unsigned __int16)(a1)) < (*(unsigned __int16 *)(a1 + 12232 + 2))) goto loc_003114A5;
loc_003114B6:
loc_003114BA:
    result = (unsigned int)((a5) & (15));
    a1 = (v_stack_m98) << (7);
    a1 = (a1) | (result);
    *(unsigned int *)(a1 + 11648) = 1;
    v_stack_mD4 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    *(unsigned int *)(a1 + 11652) = (unsigned int)(*(unsigned __int16 *)(v_rip + 12649951));
    v_stack_mDC = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_m88 = v_xmm0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 12649951)) == 0) goto loc_00311709;
loc_00311518:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) == 0) goto loc_00311985;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m80 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136));
    v_stack_m58 = v_xmm0;
    v_stack_m7E = 0;
    v_stack_m7A = 0;
    if ((*(unsigned __int16 *)(a1 + 12232)) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136)))) goto loc_003116D8;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 128)) & (*(unsigned __int64 *)(a1 + 12232 + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136) * 8 + 8));
    v_stack_m88 = a2;
    if (condition_is_equal) goto loc_003116DC;
    v_stack_mA0 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136));
    v_stack_mA8 = a2;
    v_stack_mB0 = 0;
loc_00311590:
    v_stack_mB8 = 0;
loc_00311597:
    if (a2 == 0) goto loc_003116AE;
    v_stack_mB8 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136))) + 1);
    v_stack_mA8 = a2;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136)))))) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12649905) + 0 * 8) + 136))) + 1))));
    a2 = ((unsigned int)(v_stack_mD4)) + (827);
    a2 = (a2) << (6);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8));
    v_rsi = 0;
    if (0 == 0) {
        v_rsi = a2 + 56;
        *(unsigned int *)(v_rsi) = (unsigned int)(*(unsigned __int64 *)(v_rip + 12655601));
    }
    *(unsigned __int64 *)(a2 + 48) = v_rsi;
    result = *(unsigned __int64 *)(v_rip + 12655601);
    if (a5 == 5) {
        result = v_stack_m98;
        *(unsigned __int64 *)(a2 + 16) = v_xmm0;
        *(unsigned __int64 *)(a2 + 32) = v_xmm1;
        result = *(unsigned __int64 *)(a2 + 40);
        v_stack_m90 = result;
    }
    *(unsigned __int64 *)(a2 + 8) = a1;
loc_0031162E:
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8) + 39616);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8) + 39616)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8) + 39616))) goto loc_0031162E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8) + 39616) != 0) goto loc_00311978;
    v_stack_mDC = 1;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655454) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)))) * 4))) & (63));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655454) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)))) * 4))))) >> (6));
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 12496))) <= a2) goto loc_003119E0;
loc_00311675:
    *(unsigned __int64 *)(a2 * 8 + a1 + 12496 * 1 + 8) = *(unsigned __int64 *)(a2 * 8 + a1 + 12496 * 1 + 8);
loc_0031168E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13334312 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655601) + a2 * 4)) * 8) + 36536) != 0) goto loc_00311A17;
    goto loc_00311590;
loc_003116AE:
    result = (unsigned __int16)((v_stack_mA0) + 1);
    v_stack_mA0 = (unsigned __int16)((unsigned __int16)(result));
    if (((unsigned int)((unsigned __int16)(result))) >= ((unsigned int)(a2 * 8))) goto loc_003119BE;
    v_stack_mA8 = *(unsigned __int64 *)((unsigned __int16)(result) * 8 + 8);
    goto loc_00311597;
loc_003116D8:
    v_stack_m88 = 0;
loc_003116DC:
    a4 = (unsigned int)((a4) + 1);
    v_stack_mE0 = (unsigned int)(a4);
loc_003116E4:
    v_r11 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 12649437)))) goto loc_00311518;
    if ((unsigned int)(a4) != 0) goto loc_003118A1;
loc_00311700:
loc_00311709:
    if (a5 == 5) goto loc_00311718;
    if ((unsigned int)((unsigned int)(v_stack_mD8)) != 0) goto loc_0031190A;
loc_00311718:
    if (((unsigned int)((int)(v_stack_mE4) - 1)) <= 1) goto loc_00311895;
loc_00311730:
    result = KiIpiEnlightenedGuestPriorityKick(a1 + 12232, (unsigned int)(v_stack_mDC), (unsigned int)(v_stack_mD8), a4);
    result = 0;
    v_stack_mC0 = 0;
    v_stack_mD0 = v_xmm0;
    if ((unsigned int)((int)(v_stack_mE4)) != 0) goto loc_003118C2;
loc_0031174F:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(a1 + 12232)))) goto loc_0031181F;
    if ((*(unsigned __int64 *)(a1 + 12232 + 0 * 8 + 8)) != 0) goto loc_00311843;
    v_rdi = (unsigned __int16)((v_rdi) + 1);
    goto loc_0031174F;
loc_0031176C:
    a2 = (unsigned int)(v_stack_mDC);
    if ((*(unsigned __int16 *)(v_rip + 13326765)) <= ((unsigned __int16)(*(unsigned __int16 *)(a1 + 12232)))) { a2 = *(unsigned __int16 *)(v_rip + 13326757); }
    *(unsigned __int16 *)(a1 + 12232 + 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 12232));
    *(unsigned __int16 *)(a1 + 12232) = (unsigned __int16)(a2);
    *(unsigned int *)(a1 + 12232 + 4) = (unsigned int)(v_rdi);
    if (((unsigned __int16)(v_rdi)) < ((unsigned __int16)(a2))) goto loc_00311992;
loc_00311791:
    if (((unsigned __int16)((unsigned __int16)(v_rdi))) >= (*(unsigned __int16 *)(a1 + 12232 + 2))) goto loc_003117A8;
loc_00311797:
    a1 = (unsigned __int16)(((unsigned __int16)(v_rdi)) + 1);
    *(unsigned __int64 *)(a1 + 12232 + (unsigned __int16)((unsigned __int16)(v_rdi)) * 8 + 8) = v_rdi;
    if (((unsigned __int16)(a1)) < (*(unsigned __int16 *)(a1 + 12232 + 2))) goto loc_00311797;
loc_003117A8:
    if (((unsigned int)(a5)) != 1) goto loc_003117E1;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655095) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12655095) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 4))))) >> (6));
    result = *(unsigned __int16 *)(a1 + 12232);
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 12232))) >= = ((unsigned int)(a1))) {
        a2 = a1 + 12232 + a1 * 8;
        result = (unsigned int)(a3);
        a1 = *(unsigned __int64 *)(a2 + 8);
        *(unsigned __int64 *)(a2 + 8) = a1;
    }
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 12232))) >= ((unsigned int)(a1))) goto loc_003114BA;
loc_003117FF:
    if (((unsigned __int16)((unsigned __int16)(v_rdi))) >= (*(unsigned __int16 *)(v_rip + 12580634))) goto loc_003114BA;
    if ((*(unsigned __int64 *)(v_rip + 12580644 + (unsigned __int16)((unsigned __int16)(v_rdi)) * 8 + 8)) != v_rdi) goto loc_0031195F;
    a1 = (unsigned __int16)(((unsigned __int16)(v_rdi)) + 1);
    goto loc_003117FF;
loc_0031181F:
loc_00311824:
    v_stack_mF8 = (int)(v_stack_mE4);
    result = KeBugCheckEx(92, 513, *(unsigned __int64 *)(v_rip + 11528645), (int)((unsigned int)((unsigned int)(0xC000000DULL))));
loc_00311843:
    v_stack_mD0 = 2;
    v_stack_mC8 = a1 + 12232;
loc_0031184E:
    result = HalpInterruptSendIpi(v_stack_mD0, 225, *(unsigned __int64 *)(v_rip + 11528645), (int)((unsigned int)((unsigned int)(0xC000000DULL))));
    if (sign_flag) goto loc_00311824;
loc_00311862:
    if (v_stack_mE8 != 0) goto loc_003119FA;
loc_0031186D:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, 225, *(unsigned __int64 *)(v_rip + 11528645), (int)((unsigned int)((unsigned int)(0xC000000DULL))));
    v_rsp = (v_rsp) + (224);
    return result;
loc_00311895:
    goto loc_00311730;
loc_003118A1:
    a4 = (unsigned int)(-((int)((unsigned int)((unsigned int)(0xC000000DULL)))));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00311700;
    *(unsigned int *)(a1 + 11648) = (unsigned int)(v_rdi);
    goto loc_0031186D;
loc_003118C2:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((int)(v_stack_mE4)))) - (1));
    if (condition_is_equal) goto loc_003118D2;
    if (((unsigned int)(a1)) != 1) goto loc_0031181F;
loc_003118D2:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((int)(v_stack_mE4)))) - (1));
    if (condition_is_not_equal) goto loc_00311A24;
    v_stack_mD0 = 4;
    goto loc_0031184E;
loc_003118E9:
    v_rsi = ((int)(v_stack_mE4)) - (v_stack_p18);
loc_003118F3:
    *(unsigned __int64 *)((unsigned __int16)(result)) = *(unsigned __int64 *)(v_rsi + (unsigned __int16)(result) * 1);
    a3 = (225) - (1);
    if (condition_is_equal) goto loc_0031149F;
    goto loc_003118F3;
loc_0031190A:
    if (225 == 0) goto loc_00311956;
    result = KiIpiEnlightenedGuestPriorityKick(a1 + 12496, 225, a3, a4);
    v_stack_mCC = (unsigned int)(v_rdi);
    v_stack_mC0 = (unsigned int)(v_rdi);
    result = KeIsEmptyAffinityEx(a1 + 12496, 225, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00311A39;
    v_stack_mD0 = 2;
    v_stack_mC8 = a1 + 12496;
    result = HalpInterruptSendIpi(v_stack_mD0, 225, a3, a4);
    if (sign_flag) goto loc_00311A3E;
loc_00311956:
    goto loc_00311862;
loc_0031195F:
    v_stack_p34 = (unsigned int)(v_rdi);
    result = KiSubtractAffinityEx(v_stack_p18, 225, v_stack_p18, *(unsigned __int16 *)(v_stack_p18 + 2));
    goto loc_003114BA;
loc_00311978:
    v_stack_p40 = 1;
    goto loc_0031168E;
loc_00311985:
    a4 = (unsigned int)((*(unsigned __int16 *)(v_stack_p18 + 2)) + 1);
    v_stack_p38 = (unsigned int)(a4);
    goto loc_003116E4;
loc_00311992:
    v_r10 = (v_stack_p18) - (v_rip + 13326223);
loc_003119A6:
    *(unsigned __int64 *)(v_r10 + v_rip + 13326223 * 1 + 8) = *(unsigned __int64 *)(v_rip + 13326223);
    a4 = (225) - (1);
    if (condition_is_equal) goto loc_00311791;
    goto loc_003119A6;
loc_003119BE:
    goto loc_003116E4;
loc_003119C8:
    v_stack_p30 = 1;
    result = EtwGetKernelTraceTimestamp(v_stack_m78, (unsigned int)(0x40400000ULL), v_rip + 13326223 + 8, (unsigned int)(v_stack_p38));
    goto loc_0031142D;
loc_003119E0:
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 12496 + 2))) <= ((unsigned int)((unsigned int)(0x40400000ULL)))) goto loc_0031168E;
    *(unsigned __int16 *)(a1 + 12496) = (unsigned __int16)((unsigned int)(0x40400000ULL) + 1);
    goto loc_00311675;
loc_003119FA:
    v_stack_p20 = v_stack_p18;
    result = PerfInfoLogIpiSend(v_stack_m78, (unsigned int)((unsigned int)(a5)), v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(v_stack_p34))));
    goto loc_0031186D;
loc_00311A17:
    goto loc_00311590;
loc_00311A24:
    if (((unsigned int)(v_stack_m78)) != 1) goto loc_0031184E;
    v_stack_mD0 = 3;
    goto loc_0031184E;
loc_00311A39:
loc_00311A3E:
    v_stack_p20 = v_rdi;
    result = KeBugCheckEx(92, 513, *(unsigned __int64 *)(v_rip + 11528107), (int)((unsigned int)((unsigned int)(0xC000000DULL))));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiIpiSendRequest(void *Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint16_t v_stack_m7A;
    uint32_t v_stack_m7E;
    uint16_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0xAF935D)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m98 = Arg4;
    local_rdi = 0;
    v_stack_mE4 = Arg2;
    v_stack_mA0 = 0;
    v_stack_m90 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm1;
    if (((*(uint32_t *)(v_rip + 0xCB5708)) & (0x400000ULL)) != 0) goto loc_003119C8;
    v_stack_mE8 = 0;
loc_0031142D:
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x2FC8) = 0x200001ULL;
    result = memset(Arg1 + 12232 + 8, Arg2, 256, Arg4);
    *(uint64_t *)(arg1 + 0x30D0) = 0x200001ULL;
    Arg2 = 0;
    result = memset(Arg1 + 12496 + 8, Arg2, 256, Arg4);
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_0031176C;
    *(uint16_t *)(arg1 + 0x2FC8 + 0x2) = (uint16_t)(*(uint16_t *)(arg1 + 0x2FC8 + 0x2));
    *(uint32_t *)(arg1 + 0x2FC8 + 0x4) = 0;
    Arg2 = (uint16_t)(*(uint16_t *)(arg1 + 0x2FC8 + 0x2));
    if (((uint16_t)(*(uint16_t *)(arg3))) <= ((uint16_t)(*(uint16_t *)(arg1 + 0x2FC8 + 0x2)))) { Arg2 = (uint16_t)(*(uint16_t *)(arg3)); }
    *(uint16_t *)(arg1 + 0x2FC8) = (uint16_t)(Arg2);
    if (0 < ((uint16_t)(Arg2))) goto loc_003118E9;
loc_0031149F:
    if (0 >= (*(uint16_t *)(arg1 + 0x2FC8 + 0x2))) goto loc_003114B6;
loc_003114A5:
    Arg1 = (uint16_t)((0) + 1);
    *(uint64_t *)(arg1 + 0x2FC8 + 0x0 * 8 + 0x8) = 0;
    if (((uint16_t)(Arg1)) < (*(uint16_t *)(arg1 + 0x2FC8 + 0x2))) goto loc_003114A5;
loc_003114B6:
loc_003114BA:
    result = (uint32_t)((Arg5) & (15));
    Arg1 = (v_stack_m98) << (7);
    Arg1 = (Arg1) | (result);
    *(uint32_t *)(arg1 + 0x2D80) = 1;
    v_stack_mD4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    *(uint32_t *)(arg1 + 0x2D84) = (uint32_t)(*(uint16_t *)(v_rip + 0xC105DF));
    v_stack_mDC = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_m88 = v_xmm0;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0xC105DF)) == 0) goto loc_00311709;
loc_00311518:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) == 0) goto loc_00311985;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m80 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88));
    v_stack_m58 = v_xmm0;
    v_stack_m7E = 0;
    v_stack_m7A = 0;
    if ((*(uint16_t *)(arg1 + 0x2FC8)) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88)))) goto loc_003116D8;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x80)) & (*(uint64_t *)(arg1 + 0x2FC8 + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88) * 8 + 0x8));
    v_stack_m88 = Arg2;
    if (condition_is_equal) goto loc_003116DC;
    v_stack_mA0 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88));
    v_stack_mA8 = Arg2;
    v_stack_mB0 = 0;
loc_00311590:
    v_stack_mB8 = 0;
loc_00311597:
    if (Arg2 == 0) goto loc_003116AE;
    v_stack_mB8 = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88))) + 1);
    v_stack_mA8 = Arg2;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88)))))) << (6));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint8_t)((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC105B1) + 0x0 * 8) + 0x88))) + 1))));
    Arg2 = ((uint32_t)(v_stack_mD4)) + (827);
    Arg2 = (Arg2) << (6);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8));
    local_rsi = 0;
    if (0 == 0) {
        local_rsi = Arg2 + 56;
        *(uint32_t *)(local_rsi) = (uint32_t)(*(uint64_t *)(v_rip + 0xC11BF1));
    }
    *(uint64_t *)(Arg2 + 0x30) = local_rsi;
    result = *(uint64_t *)(v_rip + 0xC11BF1);
    if (Arg5 == 5) {
        result = v_stack_m98;
        *(uint64_t *)(Arg2 + 0x10) = v_xmm0;
        *(uint64_t *)(Arg2 + 0x20) = v_xmm1;
        result = *(uint64_t *)(Arg2 + 0x28);
        v_stack_m90 = result;
    }
    *(void **)(Arg2 + 0x8) = Arg1;
loc_0031162E:
    *(uint64_t *)(Arg2) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8) + 0x9AC0);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8) + 0x9AC0)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8) + 0x9AC0))) goto loc_0031162E;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8) + 0x9AC0) != 0) goto loc_00311978;
    v_stack_mDC = 1;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11B5E) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)))) * 4))) & (63));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11B5E) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)))) * 4))))) >> (6));
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x30D0))) <= Arg2) goto loc_003119E0;
loc_00311675:
    *(uint64_t *)(Arg2 * 8 + arg1 + 0x30D0 * 1 + 0x8) = *(uint64_t *)(Arg2 * 8 + arg1 + 0x30D0 * 1 + 0x8);
loc_0031168E:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCB7728 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC11BF1) + Arg2 * 4)) * 8) + 0x8EB8) != 0) goto loc_00311A17;
    goto loc_00311590;
loc_003116AE:
    result = (uint16_t)((v_stack_mA0) + 1);
    v_stack_mA0 = (uint16_t)((uint16_t)(result));
    if (((uint32_t)((uint16_t)(result))) >= ((uint32_t)(Arg2 * 8))) goto loc_003119BE;
    v_stack_mA8 = *(uint64_t *)((uint16_t)(result) * 8 + 0x8);
    goto loc_00311597;
loc_003116D8:
    v_stack_m88 = 0;
loc_003116DC:
    Arg4 = (uint32_t)((Arg4) + 1);
    v_stack_mE0 = (uint32_t)(Arg4);
loc_003116E4:
    local_r11 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint16_t *)(v_rip + 0xC103DD)))) goto loc_00311518;
    if ((uint32_t)(Arg4) != 0) goto loc_003118A1;
loc_00311700:
loc_00311709:
    if (Arg5 == 5) goto loc_00311718;
    if ((uint32_t)((uint32_t)(v_stack_mD8)) != 0) goto loc_0031190A;
loc_00311718:
    if (((uint32_t)((int32_t)(v_stack_mE4) - 1)) <= 1) goto loc_00311895;
loc_00311730:
    result = KiIpiEnlightenedGuestPriorityKick(Arg1 + 12232, (uint32_t)(v_stack_mDC), (uint32_t)(v_stack_mD8), Arg4);
    result = 0;
    v_stack_mC0 = 0;
    v_stack_mD0 = v_xmm0;
    if ((uint32_t)((int32_t)(v_stack_mE4)) != 0) goto loc_003118C2;
loc_0031174F:
    if (0 >= ((uint16_t)(*(uint16_t *)(arg1 + 0x2FC8)))) goto loc_0031181F;
    if ((*(uint64_t *)(arg1 + 0x2FC8 + 0x0 * 8 + 0x8)) != 0) goto loc_00311843;
    local_rdi = (uint16_t)((local_rdi) + 1);
    goto loc_0031174F;
loc_0031176C:
    Arg2 = (uint32_t)(v_stack_mDC);
    if ((*(uint16_t *)(v_rip + 0xCB59AD)) <= ((uint16_t)(*(uint16_t *)(arg1 + 0x2FC8)))) { Arg2 = *(uint16_t *)(v_rip + 0xCB59A5); }
    *(uint16_t *)(arg1 + 0x2FC8 + 0x2) = (uint16_t)(*(uint16_t *)(arg1 + 0x2FC8));
    *(uint16_t *)(arg1 + 0x2FC8) = (uint16_t)(Arg2);
    *(uint32_t *)(arg1 + 0x2FC8 + 0x4) = (uint32_t)(local_rdi);
    if (((uint16_t)(local_rdi)) < ((uint16_t)(Arg2))) goto loc_00311992;
loc_00311791:
    if (((uint16_t)((uint16_t)(local_rdi))) >= (*(uint16_t *)(arg1 + 0x2FC8 + 0x2))) goto loc_003117A8;
loc_00311797:
    Arg1 = (uint16_t)(((uint16_t)(local_rdi)) + 1);
    *(uint64_t *)(arg1 + 0x2FC8 + (uint16_t)((uint16_t)(local_rdi)) * 8 + 0x8) = local_rdi;
    if (((uint16_t)(Arg1)) < (*(uint16_t *)(arg1 + 0x2FC8 + 0x2))) goto loc_00311797;
loc_003117A8:
    if (((uint32_t)(Arg5)) != 1) goto loc_003117E1;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC119F7) + (uint32_t)(*(uint32_t *)(arg1 + 0x24)) * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC119F7) + (uint32_t)(*(uint32_t *)(arg1 + 0x24)) * 4))))) >> (6));
    result = *(uint16_t *)(arg1 + 0x2FC8);
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2FC8))) >= = ((uint32_t)(Arg1))) {
        Arg2 = Arg1 + 12232 + Arg1 * 8;
        result = (uint32_t)(Arg3);
        Arg1 = *(uint64_t *)(Arg2 + 0x8);
        *(void **)(Arg2 + 0x8) = Arg1;
    }
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2FC8))) >= ((uint32_t)(Arg1))) goto loc_003114BA;
loc_003117FF:
    if (((uint16_t)((uint16_t)(local_rdi))) >= (*(uint16_t *)(v_rip + 0xBFF71A))) goto loc_003114BA;
    if ((*(uint64_t *)(v_rip + 0xBFF724 + (uint16_t)((uint16_t)(local_rdi)) * 8 + 0x8)) != local_rdi) goto loc_0031195F;
    Arg1 = (uint16_t)(((uint16_t)(local_rdi)) + 1);
    goto loc_003117FF;
loc_0031181F:
loc_00311824:
    v_stack_mF8 = (int32_t)(v_stack_mE4);
    result = KeBugCheckEx(92, 513, *(uint64_t *)(v_rip + 0xAFE9C5), (int32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
loc_00311843:
    v_stack_mD0 = 2;
    v_stack_mC8 = Arg1 + 12232;
loc_0031184E:
    result = HalpInterruptSendIpi(v_stack_mD0, 225, *(uint64_t *)(v_rip + 0xAFE9C5), (int32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    if (sign_flag) goto loc_00311824;
loc_00311862:
    if (v_stack_mE8 != 0) goto loc_003119FA;
loc_0031186D:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 225, *(uint64_t *)(v_rip + 0xAFE9C5), (int32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    local_rsp = (local_rsp) + (224);
    return result;
loc_00311895:
    goto loc_00311730;
loc_003118A1:
    Arg4 = (uint32_t)(-((int32_t)((uint32_t)((uint32_t)(0xC000000DULL)))));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) + ((uint32_t)(Arg4)));
    if (condition_is_not_equal) goto loc_00311700;
    *(uint32_t *)(arg1 + 0x2D80) = (uint32_t)(local_rdi);
    goto loc_0031186D;
loc_003118C2:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((int32_t)(v_stack_mE4)))) - (1));
    if (condition_is_equal) goto loc_003118D2;
    if (((uint32_t)(Arg1)) != 1) goto loc_0031181F;
loc_003118D2:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((int32_t)(v_stack_mE4)))) - (1));
    if (condition_is_not_equal) goto loc_00311A24;
    v_stack_mD0 = 4;
    goto loc_0031184E;
loc_003118E9:
    local_rsi = ((int32_t)(v_stack_mE4)) - (v_stack_p18);
loc_003118F3:
    *(uint64_t *)((uint16_t)(result)) = *(uint64_t *)(local_rsi + (uint16_t)(result) * 1);
    Arg3 = (225) - (1);
    if (condition_is_equal) goto loc_0031149F;
    goto loc_003118F3;
loc_0031190A:
    if (225 == 0) goto loc_00311956;
    result = KiIpiEnlightenedGuestPriorityKick(Arg1 + 12496, 225, Arg3, Arg4);
    v_stack_mCC = (uint32_t)(local_rdi);
    v_stack_mC0 = (uint32_t)(local_rdi);
    result = KeIsEmptyAffinityEx(Arg1 + 12496, 225, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00311A39;
    v_stack_mD0 = 2;
    v_stack_mC8 = Arg1 + 12496;
    result = HalpInterruptSendIpi(v_stack_mD0, 225, Arg3, Arg4);
    if (sign_flag) goto loc_00311A3E;
loc_00311956:
    goto loc_00311862;
loc_0031195F:
    v_stack_p34 = (uint32_t)(local_rdi);
    result = KiSubtractAffinityEx(v_stack_p18, 225, v_stack_p18, *(uint16_t *)(v_stack_p18 + 0x2));
    goto loc_003114BA;
loc_00311978:
    v_stack_p40 = 1;
    goto loc_0031168E;
loc_00311985:
    Arg4 = (uint32_t)((*(uint16_t *)(v_stack_p18 + 0x2)) + 1);
    v_stack_p38 = (uint32_t)(Arg4);
    goto loc_003116E4;
loc_00311992:
    local_r10 = (v_stack_p18) - (v_rip + 13326223);
loc_003119A6:
    *(uint64_t *)(local_r10 + v_rip + 0xCB578F * 1 + 0x8) = *(uint64_t *)(v_rip + 0xCB578F);
    Arg4 = (225) - (1);
    if (condition_is_equal) goto loc_00311791;
    goto loc_003119A6;
loc_003119BE:
    goto loc_003116E4;
loc_003119C8:
    v_stack_p30 = 1;
    result = EtwGetKernelTraceTimestamp(v_stack_m78, (uint32_t)(0x40400000ULL), v_rip + 13326223 + 8, (uint32_t)(v_stack_p38));
    goto loc_0031142D;
loc_003119E0:
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x30D0 + 0x2))) <= ((uint32_t)((uint32_t)(0x40400000ULL)))) goto loc_0031168E;
    *(uint16_t *)(arg1 + 0x30D0) = (uint16_t)((uint32_t)(0x40400000ULL) + 1);
    goto loc_00311675;
loc_003119FA:
    v_stack_p20 = v_stack_p18;
    result = PerfInfoLogIpiSend(v_stack_m78, (uint32_t)((uint32_t)(Arg5)), v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(v_stack_p34))));
    goto loc_0031186D;
loc_00311A17:
    goto loc_00311590;
loc_00311A24:
    if (((uint32_t)(v_stack_m78)) != 1) goto loc_0031184E;
    v_stack_mD0 = 3;
    goto loc_0031184E;
loc_00311A39:
loc_00311A3E:
    v_stack_p20 = local_rdi;
    result = KeBugCheckEx(92, 513, *(uint64_t *)(v_rip + 0xAFE7AB), (int32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x8 + r8*1` | `64` | `W` |
| `Arg1` | `+ 0x8 + r8*8` | `64` | `R` |
| `Arg1` | `+ 0x8 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x8 + rax*8` | `64` | `W` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x2D80` | `32` | `W` |
| `Arg1` | `+ 0x2D84` | `32` | `R/W` |
| `Arg1` | `+ 0x2D84` | `32` | `W` |
| `Arg1` | `+ 0x2FC8` | `64` | `R` |
| `Arg1` | `+ 0x30D0` | `64` | `R` |
| `Arg1` | `+ 0x8ECC` | `32` | `R/W` |
| `Arg1` | `+ 0x8ED0` | `32` | `R/W` |
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x0 + r14*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003113C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
