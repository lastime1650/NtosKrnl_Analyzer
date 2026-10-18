# SPCallServerHandleQueryPolicy

- RVA: `0x0096AF24`–`0x0096BCB9` (길이 `3,477` bytes)
- VA: `0x000000014096AF24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00095250`
- 디코드: `898`개 명령, `3,477/3,477` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x0096AFD6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0096B0FB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096B115` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096B157` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096B16E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0096B201` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0096B239` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096B27C` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096B363` → [KeQueryTimeIncrement](../../text/44/KeQueryTimeIncrement_function_0044B4C0.md) (function, `0x0044B4C0`)
- `0x0096B3B1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0096B3E6` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096B483` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0096B4EC` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x0096B516` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0096B77E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0096B931` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096B9BA` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x0096BA27` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0096BA4C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x0096BA8B` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096BAFC` → [sub_0096BFF0](Unknown_function_0096BFF0.md) (function, `0x0096BFF0`)
- `0x0096BB6F` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x0096BBDD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096BC11` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096BC28` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096BC5D` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0096BC77` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0096BC81` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0096BC9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [sub_00968AF6](Unknown_function_00968AF6.md) at `0x00969744`

### Static image references
- `0x0096AF47` → RVA `0x00E0A740` (`.data`; read)
- `0x0096B206` → RVA `0x0096BFF0` (`PAGE`; read)
- `0x0096B24E` → RVA `0x00FD8448` (`PAGEDATA`; read)
- `0x0096B398` → RVA `0x00B57960` (` ?? ::LBKOJDO::`string'`; read)
- `0x0096B40D` → RVA `0x00FD8178` (`PAGEDATA`; read)
- `0x0096B420` → RVA `0x00FD81B8` (`PAGEDATA`; read)
- `0x0096B432` → RVA `0x00012CD8` (`.rdata`; read)
- `0x0096B478` → RVA `0x00EF0DE0` (`.data`; read)
- `0x0096B4BB` → RVA `0x00FD8180` (`PAGEDATA`; read)
- `0x0096B4CC` → RVA `0x00FD8118` (`PAGEDATA`; read)
- `0x0096B4D3` → RVA `0x00FD8180` (`PAGEDATA`; write)
- `0x0096B980` → RVA `0x00FD8174` (`PAGEDATA`; read)
- `0x0096B998` → RVA `0x00012CE0` (`.rdata`; read)
- `0x0096B9B0` → RVA `0x00FD8174` (`PAGEDATA`; write)
- `0x0096BA01` → RVA `0x00FD8184` (`PAGEDATA`; read)
- `0x0096BA1C` → RVA `0x00EF0DC0` (`.data`; read)
- `0x0096BA34` → RVA `0x00FD8860` (`PAGEDATA`; read)
- `0x0096BA7F` → RVA `0x00FD86D0` (`PAGEDATA`; read)
- `0x0096BAF0` → RVA `0x00FD86E0` (`PAGEDATA`; read)
- `0x0096BB47` → RVA `0x00FD8058` (`PAGEDATA`; read)
- `0x0096BB57` → RVA `0x00FD8058` (`PAGEDATA`; write)
- `0x0096BC3A` → RVA `0x00FD81B8` (`PAGEDATA`; write)
- `0x0096BC41` → RVA `0x00FD8178` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x0096AFD6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0096B0FB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096B115` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096B157` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096B16E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0096B201` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0096B239` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096B363` → [KeQueryTimeIncrement](../../text/44/KeQueryTimeIncrement_function_0044B4C0.md) (`PAGE` → `.text`)
  - `0x0096B3B1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0096B483` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0096B4EC` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x0096B516` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0096B77E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0096B9BA` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x0096BA27` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x0096BA4C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x0096BB6F` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x0096BBDD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096BC11` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096BC28` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096BC5D` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x0096BC77` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0096BC81` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0096BC9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0096BBEA` → [sub_00B28806](../B2/Unknown_function_00B28806.md) (`tail-transfer`)
  - `0x0096BC50` → [sub_00B28806 + 0x8](../B2/Unknown_function_00B28806.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0096AF24  48 8B C4                        mov rax, rsp
0096AF27  48 89 58 08                     mov qword ptr [rax + 8], rbx
0096AF2B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0096AF2F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0096AF33  55                              push rbp
0096AF34  41 54                           push r12
0096AF36  41 55                           push r13
0096AF38  41 56                           push r14
0096AF3A  41 57                           push r15
0096AF3C  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0096AF40  48 81 EC C0 00 00 00            sub rsp, 0xc0
0096AF47  48 8B 05 F2 F7 49 00            mov rax, qword ptr [rip + 0x49f7f2]
0096AF4E  48 33 C4                        xor rax, rsp
0096AF51  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0096AF55  33 F6                           xor esi, esi
0096AF57  44 89 45 CB                     mov dword ptr [rbp - 0x35], r8d
0096AF5B  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
0096AF5F  0F 57 C0                        xorps xmm0, xmm0
0096AF62  89 75 D3                        mov dword ptr [rbp - 0x2d], esi
0096AF65  4D 8B F1                        mov r14, r9
0096AF68  89 75 C3                        mov dword ptr [rbp - 0x3d], esi
0096AF6B  48 8B C2                        mov rax, rdx
0096AF6E  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
0096AF72  48 8B D9                        mov rbx, rcx
0096AF75  48 89 75 FF                     mov qword ptr [rbp - 1], rsi
0096AF79  8B FE                           mov edi, esi
0096AF7B  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0096AF7F  48 85 C9                        test rcx, rcx
0096AF82  0F 84 EE 09 00 00               je 0x14096b976
0096AF88  48 85 C0                        test rax, rax
0096AF8B  0F 84 E5 09 00 00               je 0x14096b976
0096AF91  4D 85 C9                        test r9, r9
0096AF94  0F 84 DC 09 00 00               je 0x14096b976
0096AF9A  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0096AF9E  48 85 C9                        test rcx, rcx
0096AFA1  0F 84 CF 09 00 00               je 0x14096b976
0096AFA7  83 3B 03                        cmp dword ptr [rbx], 3
0096AFAA  0F 86 C6 09 00 00               jbe 0x14096b976
0096AFB0  48 8B C1                        mov rax, rcx
0096AFB3  44 8B C6                        mov r8d, esi
0096AFB6  44 8B 08                        mov r9d, dword ptr [rax]
0096AFB9  48 8D 50 04                     lea rdx, [rax + 4]
0096AFBD  41 83 F8 03                     cmp r8d, 3
0096AFC1  73 48                           jae 0x14096b00b
0096AFC3  48 3B D0                        cmp rdx, rax
0096AFC6  73 35                           jae 0x14096affd
0096AFC8  BB 95 00 00 C0                  mov ebx, 0xc0000095
0096AFCD  8B C3                           mov eax, ebx
0096AFCF  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
0096AFD3  48 33 CC                        xor rcx, rsp
0096AFD6  E8 65 16 D4 FF                  call 0x1406ac640
0096AFDB  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
0096AFE3  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0096AFE7  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0096AFEB  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0096AFEF  49 8B E3                        mov rsp, r11
0096AFF2  41 5F                           pop r15
0096AFF4  41 5E                           pop r14
0096AFF6  41 5D                           pop r13
0096AFF8  41 5C                           pop r12
0096AFFA  5D                              pop rbp
0096AFFB  C3                              ret
0096AFFC  CC                              int3
0096AFFD  4A 8D 04 0A                     lea rax, [rdx + r9]
0096B001  48 3B C2                        cmp rax, rdx
0096B004  72 C2                           jb 0x14096afc8
0096B006  41 FF C0                        inc r8d
0096B009  EB AB                           jmp 0x14096afb6
0096B00B  48 3B D0                        cmp rdx, rax
0096B00E  72 B8                           jb 0x14096afc8
0096B010  45 85 C9                        test r9d, r9d
0096B013  4C 8B E6                        mov r12, rsi
0096B016  4C 0F 45 E2                     cmovne r12, rdx
0096B01A  41 83 F9 08                     cmp r9d, 8
0096B01E  0F 85 73 0B 00 00               jne 0x14096bb97
0096B024  83 3B 04                        cmp dword ptr [rbx], 4
0096B027  4D 8B 24 24                     mov r12, qword ptr [r12]
0096B02B  0F 86 45 09 00 00               jbe 0x14096b976
0096B031  44 8B CE                        mov r9d, esi
0096B034  44 8B 01                        mov r8d, dword ptr [rcx]
0096B037  48 8D 51 04                     lea rdx, [rcx + 4]
0096B03B  41 83 F9 04                     cmp r9d, 4
0096B03F  73 17                           jae 0x14096b058
0096B041  48 3B D1                        cmp rdx, rcx
0096B044  72 82                           jb 0x14096afc8
0096B046  4A 8D 0C 02                     lea rcx, [rdx + r8]
0096B04A  48 3B CA                        cmp rcx, rdx
0096B04D  0F 82 75 FF FF FF               jb 0x14096afc8
0096B053  41 FF C1                        inc r9d
0096B056  EB DC                           jmp 0x14096b034
0096B058  48 3B D1                        cmp rdx, rcx
0096B05B  0F 82 67 FF FF FF               jb 0x14096afc8
0096B061  45 85 C0                        test r8d, r8d
0096B064  48 8B CE                        mov rcx, rsi
0096B067  48 0F 45 CA                     cmovne rcx, rdx
0096B06B  0F 84 53 09 00 00               je 0x14096b9c4
0096B071  41 F6 C0 01                     test r8b, 1
0096B075  0F 85 49 09 00 00               jne 0x14096b9c4
0096B07B  49 8B C0                        mov rax, r8
0096B07E  48 D1 E8                        shr rax, 1
0096B081  66 3B 74 41 FE                  cmp si, word ptr [rcx + rax*2 - 2]
0096B086  0F 85 38 09 00 00               jne 0x14096b9c4
0096B08C  48 85 C9                        test rcx, rcx
0096B08F  0F 84 2F 09 00 00               je 0x14096b9c4
0096B095  48 8B D0                        mov rdx, rax
0096B098  4C 8B E9                        mov r13, rcx
0096B09B  48 85 C0                        test rax, rax
0096B09E  0F 84 24 0B 00 00               je 0x14096bbc8
0096B0A4  66 39 31                        cmp word ptr [rcx], si
0096B0A7  74 0A                           je 0x14096b0b3
0096B0A9  48 83 C1 02                     add rcx, 2
0096B0AD  48 83 E8 01                     sub rax, 1
0096B0B1  75 F1                           jne 0x14096b0a4
0096B0B3  48 85 C0                        test rax, rax
0096B0B6  0F 84 0C 0B 00 00               je 0x14096bbc8
0096B0BC  48 2B D0                        sub rdx, rax
0096B0BF  48 85 C0                        test rax, rax
0096B0C2  0F 84 FC 08 00 00               je 0x14096b9c4
0096B0C8  48 8D 0C 12                     lea rcx, [rdx + rdx]
0096B0CC  48 8D 41 02                     lea rax, [rcx + 2]
0096B0D0  49 3B C0                        cmp rax, r8
0096B0D3  0F 85 EB 08 00 00               jne 0x14096b9c4
0096B0D9  48 D1 E9                        shr rcx, 1
0096B0DC  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
0096B0E3  85 C9                           test ecx, ecx
0096B0E5  0F 84 D9 08 00 00               je 0x14096b9c4
0096B0EB  44 8B F9                        mov r15d, ecx
0096B0EE  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096B0F4  8B D1                           mov edx, ecx
0096B0F6  B9 00 01 00 00                  mov ecx, 0x100
0096B0FB  E8 F0 6F 21 00                  call 0x140b820f0
0096B100  48 8B F0                        mov rsi, rax
0096B103  48 85 C0                        test rax, rax
0096B106  0F 84 1B 05 00 00               je 0x14096b627
0096B10C  45 8B C7                        mov r8d, r15d
0096B10F  49 8B D5                        mov rdx, r13
0096B112  48 8B C8                        mov rcx, rax
0096B115  E8 26 B7 D5 FF                  call 0x1406c6840
0096B11A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0096B11E  48 85 C9                        test rcx, rcx
0096B121  0F 84 66 06 00 00               je 0x14096b78d
0096B127  83 3B 05                        cmp dword ptr [rbx], 5
0096B12A  0F 86 5D 06 00 00               jbe 0x14096b78d
0096B130  48 8B C1                        mov rax, rcx
0096B133  45 33 C0                        xor r8d, r8d
0096B136  44 8B 10                        mov r10d, dword ptr [rax]
0096B139  48 8D 50 04                     lea rdx, [rax + 4]
0096B13D  41 83 F8 05                     cmp r8d, 5
0096B141  73 43                           jae 0x14096b186
0096B143  48 3B D0                        cmp rdx, rax
0096B146  73 30                           jae 0x14096b178
0096B148  BB 95 00 00 C0                  mov ebx, 0xc0000095
0096B14D  48 85 F6                        test rsi, rsi
0096B150  74 0A                           je 0x14096b15c
0096B152  33 D2                           xor edx, edx
0096B154  48 8B CE                        mov rcx, rsi
0096B157  E8 14 77 21 00                  call 0x140b82870
0096B15C  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0096B160  48 85 C0                        test rax, rax
0096B163  0F 84 64 FE FF FF               je 0x14096afcd
0096B169  33 D2                           xor edx, edx
0096B16B  48 8B C8                        mov rcx, rax
0096B16E  E8 FD 76 21 00                  call 0x140b82870
0096B173  E9 55 FE FF FF                  jmp 0x14096afcd
0096B178  4A 8D 04 12                     lea rax, [rdx + r10]
0096B17C  48 3B C2                        cmp rax, rdx
0096B17F  72 C7                           jb 0x14096b148
0096B181  41 FF C0                        inc r8d
0096B184  EB B0                           jmp 0x14096b136
0096B186  48 3B D0                        cmp rdx, rax
0096B189  72 BD                           jb 0x14096b148
0096B18B  33 C0                           xor eax, eax
0096B18D  45 85 D2                        test r10d, r10d
0096B190  48 0F 45 C2                     cmovne rax, rdx
0096B194  41 83 FA 04                     cmp r10d, 4
0096B198  0F 85 56 07 00 00               jne 0x14096b8f4
0096B19E  83 3B 06                        cmp dword ptr [rbx], 6
0096B1A1  44 8B 10                        mov r10d, dword ptr [rax]
0096B1A4  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0096B1A8  0F 86 DF 05 00 00               jbe 0x14096b78d
0096B1AE  45 33 C0                        xor r8d, r8d
0096B1B1  8B 01                           mov eax, dword ptr [rcx]
0096B1B3  48 8D 51 04                     lea rdx, [rcx + 4]
0096B1B7  41 83 F8 06                     cmp r8d, 6
0096B1BB  73 1B                           jae 0x14096b1d8
0096B1BD  48 3B D1                        cmp rdx, rcx
0096B1C0  72 86                           jb 0x14096b148
0096B1C2  48 8D 0C 02                     lea rcx, [rdx + rax]
0096B1C6  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0096B1CA  48 3B CA                        cmp rcx, rdx
0096B1CD  0F 82 75 FF FF FF               jb 0x14096b148
0096B1D3  41 FF C0                        inc r8d
0096B1D6  EB D9                           jmp 0x14096b1b1
0096B1D8  48 3B D1                        cmp rdx, rcx
0096B1DB  0F 82 67 FF FF FF               jb 0x14096b148
0096B1E1  33 DB                           xor ebx, ebx
0096B1E3  85 C0                           test eax, eax
0096B1E5  48 0F 45 DA                     cmovne rbx, rdx
0096B1E9  83 F8 04                        cmp eax, 4
0096B1EC  0F 85 02 07 00 00               jne 0x14096b8f4
0096B1F2  8B 1B                           mov ebx, dword ptr [rbx]
0096B1F4  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0096B1F8  48 8B D6                        mov rdx, rsi
0096B1FB  89 5D B7                        mov dword ptr [rbp - 0x49], ebx
0096B1FE  44 8B FB                        mov r15d, ebx
0096B201  E8 7A F5 AB FF                  call 0x14042a780
0096B206  48 8D 0D E3 0D 00 00            lea rcx, [rip + 0xde3]
0096B20D  85 DB                           test ebx, ebx
0096B20F  0F 84 E9 06 00 00               je 0x14096b8fe
0096B215  41 BD 01 00 00 00               mov r13d, 1
0096B21B  81 FB 00 00 10 00               cmp ebx, 0x100000
0096B221  0F 87 DA 06 00 00               ja 0x14096b901
0096B227  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
0096B22B  B9 00 01 00 00                  mov ecx, 0x100
0096B230  41 8B D5                        mov edx, r13d
0096B233  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096B239  E8 B2 6E 21 00                  call 0x140b820f0
0096B23E  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0096B242  4C 8B D0                        mov r10, rax
0096B245  48 85 C0                        test rax, rax
0096B248  0F 84 AC 09 00 00               je 0x14096bbfa
0096B24E  48 8B 05 F3 D1 66 00            mov rax, qword ptr [rip + 0x66d1f3]
0096B255  48 8D 0D 94 0D 00 00            lea rcx, [rip + 0xd94]
0096B25C  48 8D 55 D3                     lea rdx, [rbp - 0x2d]
0096B260  45 8B CD                        mov r9d, r13d
0096B263  4D 8B C2                        mov r8, r10
0096B266  48 3B C1                        cmp rax, rcx
0096B269  0F 85 95 09 00 00               jne 0x14096bc04
0096B26F  48 8D 45 C3                     lea rax, [rbp - 0x3d]
0096B273  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0096B277  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096B27C  E8 6F 0D 00 00                  call 0x14096bff0
0096B281  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0096B284  44 8B C8                        mov r9d, eax
0096B287  3D 23 00 00 C0                  cmp eax, 0xc0000023
0096B28C  0F 85 AA 03 00 00               jne 0x14096b63c
0096B292  44 3B 6D C3                     cmp r13d, dword ptr [rbp - 0x3d]
0096B296  72 08                           jb 0x14096b2a0
0096B298  44 8B 6D C3                     mov r13d, dword ptr [rbp - 0x3d]
0096B29C  44 89 6D B7                     mov dword ptr [rbp - 0x49], r13d
0096B2A0  41 8D 45 04                     lea eax, [r13 + 4]
0096B2A4  83 F8 04                        cmp eax, 4
0096B2A7  0F 82 9B FE FF FF               jb 0x14096b148
0096B2AD  8D 48 1C                        lea ecx, [rax + 0x1c]
0096B2B0  83 F9 1C                        cmp ecx, 0x1c
0096B2B3  0F 82 8F FE FF FF               jb 0x14096b148
0096B2B9  8D 41 08                        lea eax, [rcx + 8]
0096B2BC  3B C1                           cmp eax, ecx
0096B2BE  0F 82 84 FE FF FF               jb 0x14096b148
0096B2C4  8D 50 08                        lea edx, [rax + 8]
0096B2C7  3B D0                           cmp edx, eax
0096B2C9  0F 82 79 FE FF FF               jb 0x14096b148
0096B2CF  8D 42 08                        lea eax, [rdx + 8]
0096B2D2  83 F8 08                        cmp eax, 8
0096B2D5  0F 82 6D FE FF FF               jb 0x14096b148
0096B2DB  48 8D 48 07                     lea rcx, [rax + 7]
0096B2DF  83 E1 F8                        and ecx, 0xfffffff8
0096B2E2  3B C8                           cmp ecx, eax
0096B2E4  0F 82 5E FE FF FF               jb 0x14096b148
0096B2EA  8D 41 08                        lea eax, [rcx + 8]
0096B2ED  3B C1                           cmp eax, ecx
0096B2EF  0F 82 53 FE FF FF               jb 0x14096b148
0096B2F5  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
0096B2F9  8D 48 04                        lea ecx, [rax + 4]
0096B2FC  45 8B 50 20                     mov r10d, dword ptr [r8 + 0x20]
0096B300  45 8B 40 10                     mov r8d, dword ptr [r8 + 0x10]
0096B304  83 F9 04                        cmp ecx, 4
0096B307  0F 82 3B FE FF FF               jb 0x14096b148
0096B30D  8D 41 04                        lea eax, [rcx + 4]
0096B310  3B C1                           cmp eax, ecx
0096B312  0F 82 30 FE FF FF               jb 0x14096b148
0096B318  41 8D 0C 00                     lea ecx, [r8 + rax]
0096B31C  3B C8                           cmp ecx, eax
0096B31E  0F 82 24 FE FF FF               jb 0x14096b148
0096B324  8D 41 04                        lea eax, [rcx + 4]
0096B327  3B C1                           cmp eax, ecx
0096B329  0F 82 19 FE FF FF               jb 0x14096b148
0096B32F  41 8D 0C 02                     lea ecx, [r10 + rax]
0096B333  3B C8                           cmp ecx, eax
0096B335  0F 82 0D FE FF FF               jb 0x14096b148
0096B33B  8B DA                           mov ebx, edx
0096B33D  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
0096B341  4D 8B FC                        mov r15, r12
0096B344  39 4D CB                        cmp dword ptr [rbp - 0x35], ecx
0096B347  0F 82 B0 01 00 00               jb 0x14096b4fd
0096B34D  45 85 C9                        test r9d, r9d
0096B350  0F 88 A7 01 00 00               js 0x14096b4fd
0096B356  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0096B360  48 8B 18                        mov rbx, qword ptr [rax]
0096B363  E8 58 01 AE FF                  call 0x14044b4c0
0096B368  8B C8                           mov ecx, eax
0096B36A  33 F6                           xor esi, esi
0096B36C  48 0F AF CB                     imul rcx, rbx
0096B370  0F 57 C0                        xorps xmm0, xmm0
0096B373  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0096B377  89 75 BB                        mov dword ptr [rbp - 0x45], esi
0096B37A  44 8D 6E 01                     lea r13d, [rsi + 1]
0096B37E  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
0096B388  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0096B38B  48 F7 E9                        imul rcx
0096B38E  48 8D 4D 07                     lea rcx, [rbp + 7]
0096B392  89 75 CB                        mov dword ptr [rbp - 0x35], esi
0096B395  48 8B DA                        mov rbx, rdx
0096B398  48 8D 15 C1 C5 1E 00            lea rdx, [rip + 0x1ec5c1]
0096B39F  48 C1 FB 0B                     sar rbx, 0xb
0096B3A3  48 8B C3                        mov rax, rbx
0096B3A6  48 C1 E8 3F                     shr rax, 0x3f
0096B3AA  48 03 D8                        add rbx, rax
0096B3AD  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
0096B3B1  E8 CA F3 AB FF                  call 0x14042a780
0096B3B6  48 8B 05 8B D0 66 00            mov rax, qword ptr [rip + 0x66d08b]
0096B3BD  48 8D 0D 2C 0C 00 00            lea rcx, [rip + 0xc2c]
0096B3C4  44 8D 4E 04                     lea r9d, [rsi + 4]
0096B3C8  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0096B3CC  48 8D 55 BB                     lea rdx, [rbp - 0x45]
0096B3D0  48 3B C1                        cmp rax, rcx
0096B3D3  0F 85 42 08 00 00               jne 0x14096bc1b
0096B3D9  48 8D 45 CB                     lea rax, [rbp - 0x35]
0096B3DD  48 8D 4D 07                     lea rcx, [rbp + 7]
0096B3E1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096B3E6  E8 05 0C 00 00                  call 0x14096bff0
0096B3EB  3D 34 00 00 C0                  cmp eax, 0xc0000034
0096B3F0  0F 84 3C 08 00 00               je 0x14096bc32
0096B3F6  85 C0                           test eax, eax
0096B3F8  78 13                           js 0x14096b40d
0096B3FA  83 7D BB 04                     cmp dword ptr [rbp - 0x45], 4
0096B3FE  0F 85 2E 08 00 00               jne 0x14096bc32
0096B404  39 75 BF                        cmp dword ptr [rbp - 0x41], esi
0096B407  0F 84 25 08 00 00               je 0x14096bc32
0096B40D  44 39 2D 64 CD 66 00            cmp dword ptr [rip + 0x66cd64], r13d
0096B414  0F 85 20 08 00 00               jne 0x14096bc3a
0096B41A  48 8B CB                        mov rcx, rbx
0096B41D  0F 57 C0                        xorps xmm0, xmm0
0096B420  48 2B 0D 91 CD 66 00            sub rcx, qword ptr [rip + 0x66cd91]
0096B427  0F 88 81 07 00 00               js 0x14096bbae
0096B42D  F2 48 0F 2A C1                  cvtsi2sd xmm0, rcx
0096B432  66 0F 2F 05 9E 78 6A FF         comisd xmm0, xmmword ptr [rip - 0x958762]
0096B43A  8B C6                           mov eax, esi
0096B43C  0F 93 C0                        setae al
0096B43F  45 85 ED                        test r13d, r13d
0096B442  0F 84 38 05 00 00               je 0x14096b980
0096B448  8B 5D B7                        mov ebx, dword ptr [rbp - 0x49]
0096B44B  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0096B44F  83 C3 30                        add ebx, 0x30
0096B452  48 2B 05 5F CD 66 00            sub rax, qword ptr [rip + 0x66cd5f]
0096B459  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
0096B45D  48 3D FB CB A4 00               cmp rax, 0xa4cbfb
0096B463  0F 82 CA 01 00 00               jb 0x14096b633
0096B469  45 33 C9                        xor r9d, r9d
0096B46C  48 8D 45 FF                     lea rax, [rbp - 1]
0096B470  41 B0 01                        mov r8b, 1
0096B473  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096B478  48 8D 0D 61 59 58 00            lea rcx, [rip + 0x585961]
0096B47F  41 8D 51 06                     lea edx, [r9 + 6]
0096B483  E8 28 32 8A FF                  call 0x14020e6b0
0096B488  44 8B C0                        mov r8d, eax
0096B48B  48 8B CE                        mov rcx, rsi
0096B48E  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
0096B491  83 C0 30                        add eax, 0x30
0096B494  8B D8                           mov ebx, eax
0096B496  45 85 C0                        test r8d, r8d
0096B499  0F 88 94 01 00 00               js 0x14096b633
0096B49F  41 81 F8 C0 00 00 00            cmp r8d, 0xc0
0096B4A6  0F 84 87 01 00 00               je 0x14096b633
0096B4AC  41 81 F8 02 01 00 00            cmp r8d, 0x102
0096B4B3  0F 84 7A 01 00 00               je 0x14096b633
0096B4B9  33 F6                           xor esi, esi
0096B4BB  44 39 2D BE CC 66 00            cmp dword ptr [rip + 0x66ccbe], r13d
0096B4C2  0F 85 85 07 00 00               jne 0x14096bc4d
0096B4C8  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0096B4CC  48 2B 05 45 CC 66 00            sub rax, qword ptr [rip + 0x66cc45]
0096B4D3  44 89 2D A6 CC 66 00            mov dword ptr [rip + 0x66cca6], r13d
0096B4DA  45 85 ED                        test r13d, r13d
0096B4DD  0F 84 1E 05 00 00               je 0x14096ba01
0096B4E3  33 D2                           xor edx, edx
0096B4E5  48 8D 0D F4 58 58 00            lea rcx, [rip + 0x5858f4]
0096B4EC  E8 1F B3 A2 FF                  call 0x140396810
0096B4F1  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
0096B4F5  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
0096B4F9  41 8D 5D 30                     lea ebx, [r13 + 0x30]
0096B4FD  41 89 5E 04                     mov dword ptr [r14 + 4], ebx
0096B501  85 DB                           test ebx, ebx
0096B503  0F 84 9C 07 00 00               je 0x14096bca5
0096B509  8B D3                           mov edx, ebx
0096B50B  B9 00 01 00 00                  mov ecx, 0x100
0096B510  41 B8 53 4C 53 20               mov r8d, 0x20534c53
0096B516  E8 D5 6B 21 00                  call 0x140b820f0
0096B51B  48 85 C0                        test rax, rax
0096B51E  0F 84 8B 07 00 00               je 0x14096bcaf
0096B524  49 89 46 08                     mov qword ptr [r14 + 8], rax
0096B528  41 83 26 00                     and dword ptr [r14], 0
0096B52C  4C 8B CE                        mov r9, rsi
0096B52F  4D 8B C7                        mov r8, r15
0096B532  EB 0E                           jmp 0x14096b542
0096B534  4C 8B CE                        mov r9, rsi
0096B537  4D 8B C7                        mov r8, r15
0096B53A  85 DB                           test ebx, ebx
0096B53C  0F 88 0B FC FF FF               js 0x14096b14d
0096B542  44 8B 55 CF                     mov r10d, dword ptr [rbp - 0x31]
0096B546  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B54A  41 0F BA EA 1C                  bts r10d, 0x1c
0096B54F  48 85 D2                        test rdx, rdx
0096B552  0F 84 5D 03 00 00               je 0x14096b8b5
0096B558  45 8B 0E                        mov r9d, dword ptr [r14]
0096B55B  33 C9                           xor ecx, ecx
0096B55D  44 8D 61 04                     lea r12d, [rcx + 4]
0096B561  4D 8B C7                        mov r8, r15
0096B564  41 3B C9                        cmp ecx, r9d
0096B567  73 24                           jae 0x14096b58d
0096B569  8B 02                           mov eax, dword ptr [rdx]
0096B56B  41 03 C4                        add eax, r12d
0096B56E  41 3B C4                        cmp eax, r12d
0096B571  0F 82 D1 FB FF FF               jb 0x14096b148
0096B577  44 8B C0                        mov r8d, eax
0096B57A  4C 03 C2                        add r8, rdx
0096B57D  4C 3B C2                        cmp r8, rdx
0096B580  0F 82 C2 FB FF FF               jb 0x14096b148
0096B586  49 8B D0                        mov rdx, r8
0096B589  FF C1                           inc ecx
0096B58B  EB D4                           jmp 0x14096b561
0096B58D  4C 8D 4A 04                     lea r9, [rdx + 4]
0096B591  4C 3B CA                        cmp r9, rdx
0096B594  0F 82 AE FB FF FF               jb 0x14096b148
0096B59A  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B59E  48 8D 42 08                     lea rax, [rdx + 8]
0096B5A2  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B5A6  48 3B C1                        cmp rax, rcx
0096B5A9  0F 87 45 03 00 00               ja 0x14096b8f4
0096B5AF  44 89 22                        mov dword ptr [rdx], r12d
0096B5B2  45 89 11                        mov dword ptr [r9], r10d
0096B5B5  41 FF 06                        inc dword ptr [r14]
0096B5B8  41 83 CF FF                     or r15d, 0xffffffff
0096B5BC  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B5C0  48 85 D2                        test rdx, rdx
0096B5C3  0F 84 84 00 00 00               je 0x14096b64d
0096B5C9  45 8B 16                        mov r10d, dword ptr [r14]
0096B5CC  33 C9                           xor ecx, ecx
0096B5CE  41 3B CA                        cmp ecx, r10d
0096B5D1  73 24                           jae 0x14096b5f7
0096B5D3  8B 02                           mov eax, dword ptr [rdx]
0096B5D5  83 C0 04                        add eax, 4
0096B5D8  41 3B C4                        cmp eax, r12d
0096B5DB  0F 82 67 FB FF FF               jb 0x14096b148
0096B5E1  44 8B C8                        mov r9d, eax
0096B5E4  4C 03 CA                        add r9, rdx
0096B5E7  4C 3B CA                        cmp r9, rdx
0096B5EA  0F 82 58 FB FF FF               jb 0x14096b148
0096B5F0  49 8B D1                        mov rdx, r9
0096B5F3  FF C1                           inc ecx
0096B5F5  EB D7                           jmp 0x14096b5ce
0096B5F7  4C 8D 4A 04                     lea r9, [rdx + 4]
0096B5FB  4C 3B CA                        cmp r9, rdx
0096B5FE  0F 82 44 FB FF FF               jb 0x14096b148
0096B604  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B608  48 8D 42 0C                     lea rax, [rdx + 0xc]
0096B60C  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B610  48 3B C1                        cmp rax, rcx
0096B613  0F 87 DB 02 00 00               ja 0x14096b8f4
0096B619  C7 02 08 00 00 00               mov dword ptr [rdx], 8
0096B61F  4D 89 01                        mov qword ptr [r9], r8
0096B622  41 FF 06                        inc dword ptr [r14]
0096B625  EB 4D                           jmp 0x14096b674
0096B627  BB 17 00 00 C0                  mov ebx, 0xc0000017
0096B62C  E9 9C F9 FF FF                  jmp 0x14096afcd
0096B631  8B F8                           mov edi, eax
0096B633  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
0096B637  E9 C1 FE FF FF                  jmp 0x14096b4fd
0096B63C  41 8B D9                        mov ebx, r9d
0096B63F  45 85 C9                        test r9d, r9d
0096B642  0F 89 4A FC FF FF               jns 0x14096b292
0096B648  E9 00 FB FF FF                  jmp 0x14096b14d
0096B64D  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
0096B651  41 8B C7                        mov eax, r15d
0096B654  8D 4A 0C                        lea ecx, [rdx + 0xc]
0096B657  3B CA                           cmp ecx, edx
0096B659  0F 43 C1                        cmovae eax, ecx
0096B65C  1B DB                           sbb ebx, ebx
0096B65E  81 E3 95 00 00 C0               and ebx, 0xc0000095
0096B664  41 89 46 04                     mov dword ptr [r14 + 4], eax
0096B668  3B CA                           cmp ecx, edx
0096B66A  73 B6                           jae 0x14096b622
0096B66C  85 DB                           test ebx, ebx
0096B66E  0F 88 D9 FA FF FF               js 0x14096b14d
0096B674  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B678  44 8B 55 D3                     mov r10d, dword ptr [rbp - 0x2d]
0096B67C  48 85 D2                        test rdx, rdx
0096B67F  74 5B                           je 0x14096b6dc
0096B681  45 8B 0E                        mov r9d, dword ptr [r14]
0096B684  33 C9                           xor ecx, ecx
0096B686  41 3B C9                        cmp ecx, r9d
0096B689  73 24                           jae 0x14096b6af
0096B68B  8B 02                           mov eax, dword ptr [rdx]
0096B68D  83 C0 04                        add eax, 4
0096B690  41 3B C4                        cmp eax, r12d
0096B693  0F 82 AF FA FF FF               jb 0x14096b148
0096B699  44 8B C0                        mov r8d, eax
0096B69C  4C 03 C2                        add r8, rdx
0096B69F  4C 3B C2                        cmp r8, rdx
0096B6A2  0F 82 A0 FA FF FF               jb 0x14096b148
0096B6A8  49 8B D0                        mov rdx, r8
0096B6AB  FF C1                           inc ecx
0096B6AD  EB D7                           jmp 0x14096b686
0096B6AF  4C 8D 42 04                     lea r8, [rdx + 4]
0096B6B3  4C 3B C2                        cmp r8, rdx
0096B6B6  0F 82 8C FA FF FF               jb 0x14096b148
0096B6BC  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B6C0  48 8D 42 08                     lea rax, [rdx + 8]
0096B6C4  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B6C8  48 3B C1                        cmp rax, rcx
0096B6CB  0F 87 23 02 00 00               ja 0x14096b8f4
0096B6D1  44 89 22                        mov dword ptr [rdx], r12d
0096B6D4  45 89 10                        mov dword ptr [r8], r10d
0096B6D7  41 FF 06                        inc dword ptr [r14]
0096B6DA  EB 27                           jmp 0x14096b703
0096B6DC  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
0096B6E0  41 8B C7                        mov eax, r15d
0096B6E3  8D 4A 08                        lea ecx, [rdx + 8]
0096B6E6  3B CA                           cmp ecx, edx
0096B6E8  0F 43 C1                        cmovae eax, ecx
0096B6EB  1B DB                           sbb ebx, ebx
0096B6ED  81 E3 95 00 00 C0               and ebx, 0xc0000095
0096B6F3  41 89 46 04                     mov dword ptr [r14 + 4], eax
0096B6F7  3B CA                           cmp ecx, edx
0096B6F9  73 DC                           jae 0x14096b6d7
0096B6FB  85 DB                           test ebx, ebx
0096B6FD  0F 88 4A FA FF FF               js 0x14096b14d
0096B703  4C 8B 55 E7                     mov r10, qword ptr [rbp - 0x19]
0096B707  4D 85 D2                        test r10, r10
0096B70A  75 7C                           jne 0x14096b788
0096B70C  45 85 ED                        test r13d, r13d
0096B70F  75 7C                           jne 0x14096b78d
0096B711  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B715  48 85 D2                        test rdx, rdx
0096B718  74 7D                           je 0x14096b797
0096B71A  45 8B 0E                        mov r9d, dword ptr [r14]
0096B71D  33 C9                           xor ecx, ecx
0096B71F  41 3B C9                        cmp ecx, r9d
0096B722  73 24                           jae 0x14096b748
0096B724  8B 02                           mov eax, dword ptr [rdx]
0096B726  83 C0 04                        add eax, 4
0096B729  41 3B C4                        cmp eax, r12d
0096B72C  0F 82 16 FA FF FF               jb 0x14096b148
0096B732  44 8B C0                        mov r8d, eax
0096B735  4C 03 C2                        add r8, rdx
0096B738  4C 3B C2                        cmp r8, rdx
0096B73B  0F 82 07 FA FF FF               jb 0x14096b148
0096B741  49 8B D0                        mov rdx, r8
0096B744  FF C1                           inc ecx
0096B746  EB D7                           jmp 0x14096b71f
0096B748  4C 8D 4A 04                     lea r9, [rdx + 4]
0096B74C  4C 3B CA                        cmp r9, rdx
0096B74F  0F 82 F3 F9 FF FF               jb 0x14096b148
0096B755  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B759  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B75D  45 8B C5                        mov r8d, r13d
0096B760  49 8D 40 04                     lea rax, [r8 + 4]
0096B764  48 03 C2                        add rax, rdx
0096B767  48 3B C1                        cmp rax, rcx
0096B76A  0F 87 84 01 00 00               ja 0x14096b8f4
0096B770  44 89 2A                        mov dword ptr [rdx], r13d
0096B773  4D 85 D2                        test r10, r10
0096B776  74 0B                           je 0x14096b783
0096B778  49 8B D2                        mov rdx, r10
0096B77B  49 8B C9                        mov rcx, r9
0096B77E  E8 BD B0 D5 FF                  call 0x1406c6840
0096B783  41 FF 06                        inc dword ptr [r14]
0096B786  EB 39                           jmp 0x14096b7c1
0096B788  45 85 ED                        test r13d, r13d
0096B78B  75 84                           jne 0x14096b711
0096B78D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0096B792  E9 B6 F9 FF FF                  jmp 0x14096b14d
0096B797  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
0096B79B  41 8D 4D 04                     lea ecx, [r13 + 4]
0096B79F  03 CA                           add ecx, edx
0096B7A1  41 8B C7                        mov eax, r15d
0096B7A4  3B CA                           cmp ecx, edx
0096B7A6  0F 43 C1                        cmovae eax, ecx
0096B7A9  1B DB                           sbb ebx, ebx
0096B7AB  81 E3 95 00 00 C0               and ebx, 0xc0000095
0096B7B1  41 89 46 04                     mov dword ptr [r14 + 4], eax
0096B7B5  3B CA                           cmp ecx, edx
0096B7B7  73 CA                           jae 0x14096b783
0096B7B9  85 DB                           test ebx, ebx
0096B7BB  0F 88 8C F9 FF FF               js 0x14096b14d
0096B7C1  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B7C5  44 8B 55 C3                     mov r10d, dword ptr [rbp - 0x3d]
0096B7C9  48 85 D2                        test rdx, rdx
0096B7CC  74 5B                           je 0x14096b829
0096B7CE  45 8B 0E                        mov r9d, dword ptr [r14]
0096B7D1  33 C9                           xor ecx, ecx
0096B7D3  41 3B C9                        cmp ecx, r9d
0096B7D6  73 24                           jae 0x14096b7fc
0096B7D8  8B 02                           mov eax, dword ptr [rdx]
0096B7DA  83 C0 04                        add eax, 4
0096B7DD  41 3B C4                        cmp eax, r12d
0096B7E0  0F 82 62 F9 FF FF               jb 0x14096b148
0096B7E6  44 8B C0                        mov r8d, eax
0096B7E9  4C 03 C2                        add r8, rdx
0096B7EC  4C 3B C2                        cmp r8, rdx
0096B7EF  0F 82 53 F9 FF FF               jb 0x14096b148
0096B7F5  49 8B D0                        mov rdx, r8
0096B7F8  FF C1                           inc ecx
0096B7FA  EB D7                           jmp 0x14096b7d3
0096B7FC  4C 8D 42 04                     lea r8, [rdx + 4]
0096B800  4C 3B C2                        cmp r8, rdx
0096B803  0F 82 3F F9 FF FF               jb 0x14096b148
0096B809  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B80D  48 8D 42 08                     lea rax, [rdx + 8]
0096B811  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B815  48 3B C1                        cmp rax, rcx
0096B818  0F 87 D6 00 00 00               ja 0x14096b8f4
0096B81E  44 89 22                        mov dword ptr [rdx], r12d
0096B821  45 89 10                        mov dword ptr [r8], r10d
0096B824  41 FF 06                        inc dword ptr [r14]
0096B827  EB 27                           jmp 0x14096b850
0096B829  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
0096B82D  41 8B C7                        mov eax, r15d
0096B830  8D 4A 08                        lea ecx, [rdx + 8]
0096B833  3B CA                           cmp ecx, edx
0096B835  0F 43 C1                        cmovae eax, ecx
0096B838  1B DB                           sbb ebx, ebx
0096B83A  81 E3 95 00 00 C0               and ebx, 0xc0000095
0096B840  41 89 46 04                     mov dword ptr [r14 + 4], eax
0096B844  3B CA                           cmp ecx, edx
0096B846  73 DC                           jae 0x14096b824
0096B848  85 DB                           test ebx, ebx
0096B84A  0F 88 FD F8 FF FF               js 0x14096b14d
0096B850  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0096B854  48 85 D2                        test rdx, rdx
0096B857  74 75                           je 0x14096b8ce
0096B859  45 8B 0E                        mov r9d, dword ptr [r14]
0096B85C  33 C9                           xor ecx, ecx
0096B85E  41 3B C9                        cmp ecx, r9d
0096B861  73 24                           jae 0x14096b887
0096B863  8B 02                           mov eax, dword ptr [rdx]
0096B865  83 C0 04                        add eax, 4
0096B868  41 3B C4                        cmp eax, r12d
0096B86B  0F 82 D7 F8 FF FF               jb 0x14096b148
0096B871  44 8B C0                        mov r8d, eax
0096B874  4C 03 C2                        add r8, rdx
0096B877  4C 3B C2                        cmp r8, rdx
0096B87A  0F 82 C8 F8 FF FF               jb 0x14096b148
0096B880  49 8B D0                        mov rdx, r8
0096B883  FF C1                           inc ecx
0096B885  EB D7                           jmp 0x14096b85e
0096B887  4C 8D 42 04                     lea r8, [rdx + 4]
0096B88B  4C 3B C2                        cmp r8, rdx
0096B88E  0F 82 B4 F8 FF FF               jb 0x14096b148
0096B894  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B898  48 8D 42 08                     lea rax, [rdx + 8]
0096B89C  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
0096B8A0  48 3B C1                        cmp rax, rcx
0096B8A3  77 4F                           ja 0x14096b8f4
0096B8A5  44 89 22                        mov dword ptr [rdx], r12d
0096B8A8  41 89 38                        mov dword ptr [r8], edi
0096B8AB  41 FF 06                        inc dword ptr [r14]
0096B8AE  33 DB                           xor ebx, ebx
0096B8B0  E9 98 F8 FF FF                  jmp 0x14096b14d
0096B8B5  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0096B8B9  8D 48 08                        lea ecx, [rax + 8]
0096B8BC  3B C8                           cmp ecx, eax
0096B8BE  0F 83 0A 01 00 00               jae 0x14096b9ce
0096B8C4  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
0096B8C9  E9 7A F8 FF FF                  jmp 0x14096b148
0096B8CE  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
0096B8D2  8D 41 08                        lea eax, [rcx + 8]
0096B8D5  3B C1                           cmp eax, ecx
0096B8D7  44 0F 43 F8                     cmovae r15d, eax
0096B8DB  1B DB                           sbb ebx, ebx
0096B8DD  81 E3 95 00 00 C0               and ebx, 0xc0000095
0096B8E3  45 89 7E 04                     mov dword ptr [r14 + 4], r15d
0096B8E7  3B C1                           cmp eax, ecx
0096B8E9  73 C0                           jae 0x14096b8ab
0096B8EB  85 DB                           test ebx, ebx
0096B8ED  79 BF                           jns 0x14096b8ae
0096B8EF  E9 59 F8 FF FF                  jmp 0x14096b14d
0096B8F4  BB 23 00 00 C0                  mov ebx, 0xc0000023
0096B8F9  E9 4F F8 FF FF                  jmp 0x14096b14d
0096B8FE  45 33 ED                        xor r13d, r13d
0096B901  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
0096B904  48 8D 55 D3                     lea rdx, [rbp - 0x2d]
0096B908  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0096B90B  45 33 C9                        xor r9d, r9d
0096B90E  48 8B 05 33 CB 66 00            mov rax, qword ptr [rip + 0x66cb33]
0096B915  45 33 C0                        xor r8d, r8d
0096B918  89 5D B7                        mov dword ptr [rbp - 0x49], ebx
0096B91B  48 3B C1                        cmp rax, rcx
0096B91E  0F 85 AC 02 00 00               jne 0x14096bbd0
0096B924  48 8D 45 C3                     lea rax, [rbp - 0x3d]
0096B928  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0096B92C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096B931  E8 BA 06 00 00                  call 0x14096bff0
0096B936  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0096B939  44 8B C8                        mov r9d, eax
0096B93C  3D 23 00 00 C0                  cmp eax, 0xc0000023
0096B941  0F 85 5A 02 00 00               jne 0x14096bba1
0096B947  44 3B 7D C3                     cmp r15d, dword ptr [rbp - 0x3d]
0096B94B  0F 82 8F 00 00 00               jb 0x14096b9e0
0096B951  8B 45 C3                        mov eax, dword ptr [rbp - 0x3d]
0096B954  45 33 C9                        xor r9d, r9d
0096B957  89 45 B7                        mov dword ptr [rbp - 0x49], eax
0096B95A  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
0096B95D  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0096B960  44 89 4D CF                     mov dword ptr [rbp - 0x31], r9d
0096B964  45 85 ED                        test r13d, r13d
0096B967  0F 85 BA F8 FF FF               jne 0x14096b227
0096B96D  44 8B 6D B7                     mov r13d, dword ptr [rbp - 0x49]
0096B971  E9 2A F9 FF FF                  jmp 0x14096b2a0
0096B976  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0096B97B  E9 4D F6 FF FF                  jmp 0x14096afcd
0096B980  39 35 EE C7 66 00               cmp dword ptr [rip + 0x66c7ee], esi
0096B986  0F 85 BC FA FF FF               jne 0x14096b448
0096B98C  85 C0                           test eax, eax
0096B98E  0F 84 B4 FA FF FF               je 0x14096b448
0096B994  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0096B998  48 8D 0D 41 73 6A FF            lea rcx, [rip - 0x958cbf]
0096B99F  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0096B9A3  45 33 C9                        xor r9d, r9d
0096B9A6  45 33 C0                        xor r8d, r8d
0096B9A9  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0096B9AE  33 D2                           xor edx, edx
0096B9B0  C7 05 BA C7 66 00 01 00 00 00   mov dword ptr [rip + 0x66c7ba], 1
0096B9BA  E8 51 53 D4 FF                  call 0x1406b0d10
0096B9BF  E9 84 FA FF FF                  jmp 0x14096b448
0096B9C4  BB 3E 00 00 C0                  mov ebx, 0xc000003e
0096B9C9  E9 FF F5 FF FF                  jmp 0x14096afcd
0096B9CE  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
0096B9D2  49 8B F1                        mov rsi, r9
0096B9D5  41 BC 04 00 00 00               mov r12d, 4
0096B9DB  E9 D5 FB FF FF                  jmp 0x14096b5b5
0096B9E0  44 8B EB                        mov r13d, ebx
0096B9E3  45 85 FF                        test r15d, r15d
0096B9E6  0F 85 B4 F8 FF FF               jne 0x14096b2a0
0096B9EC  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
0096B9EF  45 33 C9                        xor r9d, r9d
0096B9F2  44 89 4D CF                     mov dword ptr [rbp - 0x31], r9d
0096B9F6  89 5D B7                        mov dword ptr [rbp - 0x49], ebx
0096B9F9  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0096B9FC  E9 9F F8 FF FF                  jmp 0x14096b2a0
0096BA01  39 35 7D C7 66 00               cmp dword ptr [rip + 0x66c77d], esi
0096BA07  0F 84 D6 FA FF FF               je 0x14096b4e3
0096BA0D  48 3D FC F4 AD 00               cmp rax, 0xadf4fc
0096BA13  0F 82 CA FA FF FF               jb 0x14096b4e3
0096BA19  45 33 C0                        xor r8d, r8d
0096BA1C  48 8D 0D 9D 53 58 00            lea rcx, [rip + 0x58539d]
0096BA23  41 8D 50 01                     lea edx, [r8 + 1]
0096BA27  E8 E4 38 9D FF                  call 0x14033f310
0096BA2C  BB 04 00 00 00                  mov ebx, 4
0096BA31  89 75 BB                        mov dword ptr [rbp - 0x45], esi
0096BA34  4C 8D 05 25 CE 66 00            lea r8, [rip + 0x66ce25]
0096BA3B  89 5D BF                        mov dword ptr [rbp - 0x41], ebx
0096BA3E  48 8D 4D DF                     lea rcx, [rbp - 0x21]
0096BA42  89 75 CB                        mov dword ptr [rbp - 0x35], esi
0096BA45  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
0096BA49  8D 53 FD                        lea edx, [rbx - 3]
0096BA4C  E8 BF 18 D4 FF                  call 0x1406ad310
0096BA51  4C 8D 3D 98 05 00 00            lea r15, [rip + 0x598]
0096BA58  85 C0                           test eax, eax
0096BA5A  0F 89 28 01 00 00               jns 0x14096bb88
0096BA60  48 8B 05 E1 C9 66 00            mov rax, qword ptr [rip + 0x66c9e1]
0096BA67  4C 8D 45 BB                     lea r8, [rbp - 0x45]
0096BA6B  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096BA6F  44 8B CB                        mov r9d, ebx
0096BA72  49 3B C7                        cmp rax, r15
0096BA75  0F 85 EC 01 00 00               jne 0x14096bc67
0096BA7B  48 8D 45 CB                     lea rax, [rbp - 0x35]
0096BA7F  48 8D 0D 4A CC 66 00            lea rcx, [rip + 0x66cc4a]
0096BA86  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096BA8B  E8 60 05 00 00                  call 0x14096bff0
0096BA90  85 C0                           test eax, eax
0096BA92  0F 88 E1 00 00 00               js 0x14096bb79
0096BA98  44 8B 6D BB                     mov r13d, dword ptr [rbp - 0x45]
0096BA9C  39 5D BF                        cmp dword ptr [rbp - 0x41], ebx
0096BA9F  0F 85 D4 00 00 00               jne 0x14096bb79
0096BAA5  41 8D 45 FF                     lea eax, [r13 - 1]
0096BAA9  83 F8 02                        cmp eax, 2
0096BAAC  0F 87 C7 00 00 00               ja 0x14096bb79
0096BAB2  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
0096BAB6  48 85 C9                        test rcx, rcx
0096BAB9  0F 85 C2 01 00 00               jne 0x14096bc81
0096BABF  33 C0                           xor eax, eax
0096BAC1  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0096BAC4  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0096BAC8  4C 8D 45 17                     lea r8, [rbp + 0x17]
0096BACC  89 45 1F                        mov dword ptr [rbp + 0x1f], eax
0096BACF  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0096BAD3  48 8B 05 6E C9 66 00            mov rax, qword ptr [rip + 0x66c96e]
0096BADA  41 B9 0C 00 00 00               mov r9d, 0xc
0096BAE0  89 75 BB                        mov dword ptr [rbp - 0x45], esi
0096BAE3  49 3B C7                        cmp rax, r15
0096BAE6  0F 85 9F 01 00 00               jne 0x14096bc8b
0096BAEC  48 8D 45 BB                     lea rax, [rbp - 0x45]
0096BAF0  48 8D 0D E9 CB 66 00            lea rcx, [rip + 0x66cbe9]
0096BAF7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0096BAFC  E8 EF 04 00 00                  call 0x14096bff0
0096BB01  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0096BB05  44 8B C8                        mov r9d, eax
0096BB08  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
0096BB0B  4D 8B FC                        mov r15, r12
0096BB0E  44 8B 55 C7                     mov r10d, dword ptr [rbp - 0x39]
0096BB12  83 C0 30                        add eax, 0x30
0096BB15  8B D8                           mov ebx, eax
0096BB17  45 8B C2                        mov r8d, r10d
0096BB1A  48 8B F1                        mov rsi, rcx
0096BB1D  45 85 C9                        test r9d, r9d
0096BB20  78 25                           js 0x14096bb47
0096BB22  83 7D BF 03                     cmp dword ptr [rbp - 0x41], 3
0096BB26  75 1F                           jne 0x14096bb47
0096BB28  83 7D BB 0C                     cmp dword ptr [rbp - 0x45], 0xc
0096BB2C  75 19                           jne 0x14096bb47
0096BB2E  33 D2                           xor edx, edx
0096BB30  83 FA 03                        cmp edx, 3
0096BB33  73 12                           jae 0x14096bb47
0096BB35  8B 44 95 17                     mov eax, dword ptr [rbp + rdx*4 + 0x17]
0096BB39  8B C8                           mov ecx, eax
0096BB3B  83 E1 0F                        and ecx, 0xf
0096BB3E  41 3B CD                        cmp ecx, r13d
0096BB41  74 14                           je 0x14096bb57
0096BB43  FF C2                           inc edx
0096BB45  EB E9                           jmp 0x14096bb30
0096BB47  8B 05 0B C5 66 00               mov eax, dword ptr [rip + 0x66c50b]
0096BB4D  25 11 32 FF FF                  and eax, 0xffff3211
0096BB52  0D 11 32 00 00                  or eax, 0x3211
0096BB57  89 05 FB C4 66 00               mov dword ptr [rip + 0x66c4fb], eax
0096BB5D  45 85 C0                        test r8d, r8d
0096BB60  0F 85 CB FA FF FF               jne 0x14096b631
0096BB66  33 D2                           xor edx, edx
0096BB68  48 8D 0D 71 52 58 00            lea rcx, [rip + 0x585271]
0096BB6F  E8 9C AC A2 FF                  call 0x140396810
0096BB74  E9 BA FA FF FF                  jmp 0x14096b633
0096BB79  41 BD 01 00 00 00               mov r13d, 1
0096BB7F  44 89 6D BB                     mov dword ptr [rbp - 0x45], r13d
0096BB83  E9 2A FF FF FF                  jmp 0x14096bab2
0096BB88  41 BD 03 00 00 00               mov r13d, 3
0096BB8E  44 89 6D BB                     mov dword ptr [rbp - 0x45], r13d
0096BB92  E9 05 FF FF FF                  jmp 0x14096ba9c
0096BB97  BB 23 00 00 C0                  mov ebx, 0xc0000023
0096BB9C  E9 2C F4 FF FF                  jmp 0x14096afcd
0096BBA1  45 85 C9                        test r9d, r9d
0096BBA4  79 41                           jns 0x14096bbe7
0096BBA6  41 8B D9                        mov ebx, r9d
0096BBA9  E9 9F F5 FF FF                  jmp 0x14096b14d
0096BBAE  48 8B C1                        mov rax, rcx
0096BBB1  83 E1 01                        and ecx, 1
0096BBB4  48 D1 E8                        shr rax, 1
0096BBB7  48 0B C1                        or rax, rcx
0096BBBA  F2 48 0F 2A C0                  cvtsi2sd xmm0, rax
0096BBBF  F2 0F 58 C0                     addsd xmm0, xmm0
0096BBC3  E9 6A F8 FF FF                  jmp 0x14096b432
0096BBC8  48 8B D6                        mov rdx, rsi
0096BBCB  E9 EF F4 FF FF                  jmp 0x14096b0bf
0096BBD0  48 8D 4D C3                     lea rcx, [rbp - 0x3d]
0096BBD4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096BBD9  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0096BBDD  E8 EE EE D4 FF                  call 0x1406baad0
0096BBE2  E9 4F FD FF FF                  jmp 0x14096b936
0096BBE7  39 7D C3                        cmp dword ptr [rbp - 0x3d], edi
0096BBEA  0F 84 16 CC 1B 00               je 0x140b28806
0096BBF0  BB FF FF 00 80                  mov ebx, 0x8000ffff
0096BBF5  E9 53 F5 FF FF                  jmp 0x14096b14d
0096BBFA  BB 17 00 00 C0                  mov ebx, 0xc0000017
0096BBFF  E9 49 F5 FF FF                  jmp 0x14096b14d
0096BC04  48 8D 4D C3                     lea rcx, [rbp - 0x3d]
0096BC08  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096BC0D  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0096BC11  E8 BA EE D4 FF                  call 0x1406baad0
0096BC16  E9 66 F6 FF FF                  jmp 0x14096b281
0096BC1B  48 8D 4D CB                     lea rcx, [rbp - 0x35]
0096BC1F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096BC24  48 8D 4D 07                     lea rcx, [rbp + 7]
0096BC28  E8 A3 EE D4 FF                  call 0x1406baad0
0096BC2D  E9 B9 F7 FF FF                  jmp 0x14096b3eb
0096BC32  44 8B EE                        mov r13d, esi
0096BC35  E9 D3 F7 FF FF                  jmp 0x14096b40d
0096BC3A  48 89 1D 77 C5 66 00            mov qword ptr [rip + 0x66c577], rbx
0096BC41  44 89 2D 30 C5 66 00            mov dword ptr [rip + 0x66c530], r13d
0096BC48  E9 CD F7 FF FF                  jmp 0x14096b41a
0096BC4D  45 85 ED                        test r13d, r13d
0096BC50  0F 84 B8 CB 1B 00               je 0x140b2880e
0096BC56  48 8D 0D 63 51 58 00            lea rcx, [rip + 0x585163]
0096BC5D  E8 EE C6 8D FF                  call 0x140248350
0096BC62  E9 61 F8 FF FF                  jmp 0x14096b4c8
0096BC67  48 8D 4D CB                     lea rcx, [rbp - 0x35]
0096BC6B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096BC70  48 8D 0D 59 CA 66 00            lea rcx, [rip + 0x66ca59]
0096BC77  E8 54 EE D4 FF                  call 0x1406baad0
0096BC7C  E9 0F FE FF FF                  jmp 0x14096ba90
0096BC81  E8 2A 16 D4 FF                  call 0x1406ad2b0
0096BC86  E9 34 FE FF FF                  jmp 0x14096babf
0096BC8B  48 8D 4D BB                     lea rcx, [rbp - 0x45]
0096BC8F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0096BC94  48 8D 0D 45 CA 66 00            lea rcx, [rip + 0x66ca45]
0096BC9B  E8 30 EE D4 FF                  call 0x1406baad0
0096BCA0  E9 5C FE FF FF                  jmp 0x14096bb01
0096BCA5  BB 3E 00 00 C0                  mov ebx, 0xc000003e
0096BCAA  E9 85 F8 FF FF                  jmp 0x14096b534
0096BCAF  BB 17 00 00 C0                  mov ebx, 0xc0000017
0096BCB4  E9 7B F8 FF FF                  jmp 0x14096b534
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SPCallServerHandleQueryPolicy(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 4847602)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    v_rsi = 0;
    *(unsigned int *)(v_rsp - 95 - 53) = a3;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = a2;
    *(unsigned int *)(v_rsp - 95 - 45) = 0;
    *(unsigned int *)(v_rsp - 95 - 61) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_xmm0;
    if (a1 == 0) goto loc_0096B976;
    if (a2 == 0) goto loc_0096B976;
    if (a4 == 0) goto loc_0096B976;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0096B976;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_0096B976;
loc_0096AFB6:
    if (0 >= 3) goto loc_0096B00B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_0096AFFD;
loc_0096AFC8:
loc_0096AFCD:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 8) + 4, 0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    return result;
loc_0096AFFD:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_0096AFC8;
    a3 = (unsigned int)((0) + 1);
    goto loc_0096AFB6;
loc_0096B00B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_0096AFC8;
    v_r12 = *(unsigned __int64 *)(v_stack_m28 + 56);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r12 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_0096BB97;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48))) <= 4) goto loc_0096B976;
loc_0096B034:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))))) >= 4) goto loc_0096B058;
    if ((a1 + 4) < a1) goto loc_0096AFC8;
    if ((a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1) < (a1 + 4)) goto loc_0096AFC8;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) + 1);
    goto loc_0096B034;
loc_0096B058:
    if ((a1 + 4) < (a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1)) goto loc_0096AFC8;
    a1 = *(unsigned __int64 *)(v_stack_m28 + 56);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) != 0) { a1 = a1 + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_0096B9C4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) != 0) goto loc_0096B9C4;
    result = ((unsigned int)(*(unsigned int *)(a1))) >> (1);
    if (((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56))) != (*(unsigned __int16 *)(a1 + result * 2 - 2))) goto loc_0096B9C4;
    if (a1 == 0) goto loc_0096B9C4;
    if (result == 0) goto loc_0096BBC8;
loc_0096B0A4:
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_0096B0B3;
    a1 = (a1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0096B0A4;
loc_0096B0B3:
    if (result == 0) goto loc_0096BBC8;
    a2 = (result) - (result);
loc_0096B0BF:
    if (result == 0) goto loc_0096B9C4;
    if ((a2 + a2 * 1 + 2) != ((unsigned int)(*(unsigned int *)(a1)))) goto loc_0096B9C4;
    a1 = (a2 + a2 * 1) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_0096B9C4;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_0096B627;
    result = memcpy(result, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 * 2 + 2)))), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8) == 0) goto loc_0096B78D;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48))) <= 5) goto loc_0096B78D;
    a3 = 0;
loc_0096B136:
    if (0 >= 5) goto loc_0096B186;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8) + 4) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8))) goto loc_0096B178;
loc_0096B148:
loc_0096B14D:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 25) == 0) goto loc_0096AFCD;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 25), a2, a3, a4);
    goto loc_0096AFCD;
loc_0096B178:
    if ((a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8))) * 1) < 0) goto loc_0096B148;
    a3 = (unsigned int)((a3) + 1);
    goto loc_0096B136;
loc_0096B186:
    if (0 < (a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8))) * 1)) goto loc_0096B148;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8)))) != 0) { result = 0; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8))))) != 4) goto loc_0096B8F4;
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned int *)((unsigned int)(0xC0000095ULL))) <= 6) goto loc_0096B78D;
    a3 = 0;
loc_0096B1B1:
    if (0 >= 6) goto loc_0096B1D8;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25) + 4) < (*(unsigned __int64 *)(v_rsp - 95 - 25))) goto loc_0096B148;
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 25))) * 1) < (*(unsigned __int64 *)(v_rsp - 95 - 25) + 4)) goto loc_0096B148;
    a3 = (unsigned int)((a3) + 1);
    goto loc_0096B1B1;
loc_0096B1D8:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 25) + 4) < (*(unsigned __int64 *)(v_rsp - 95 - 25) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 25))) * 1)) goto loc_0096B148;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 25)))) != 0) { v_rbx = *(unsigned __int64 *)(v_rsp - 95 - 25) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 25))))) != 4) goto loc_0096B8F4;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)));
    result = RtlInitUnicodeString(v_rsp - 95 - 17, result, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))) == 0) goto loc_0096B8FE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) > 0x100000ULL) goto loc_0096B901;
loc_0096B227:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))), (unsigned int)(0x20534C53ULL), a4);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = result;
    if (result == 0) goto loc_0096BBFA;
    if ((*(unsigned __int64 *)(v_rip + 6738419)) != (v_rip + 3476)) goto loc_0096BC04;
    v_stack_mA0 = v_rsp - 95 - 61;
    result = sub_0096BFF0(v_rsp - 95 - 17, v_rsp - 95 - 45, result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))));
loc_0096B281:
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0096B63C;
loc_0096B292:
    v_r13 = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 73));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) >= (*(unsigned int *)(v_rsp - 95 - 61))) {
        v_r13 = *(unsigned int *)(v_rsp - 95 - 61);
        *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)(v_r13);
    }
    if (((unsigned int)(v_r13 + 4)) < 4) goto loc_0096B148;
    if (((unsigned int)(v_r13 + 4 + 28)) < 28) goto loc_0096B148;
    if (((unsigned int)(v_r13 + 4 + 28 + 8)) < ((unsigned int)(v_r13 + 4 + 28))) goto loc_0096B148;
    if (((unsigned int)(v_r13 + 4 + 28 + 8 + 8)) < ((unsigned int)(v_r13 + 4 + 28 + 8))) goto loc_0096B148;
    if (((unsigned int)(v_r13 + 4 + 28 + 8 + 8 + 8)) < 8) goto loc_0096B148;
    a1 = (unsigned int)((v_r13 + 4 + 28 + 8 + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a1)) < ((unsigned int)(v_r13 + 4 + 28 + 8 + 8 + 8))) goto loc_0096B148;
    if (((unsigned int)(a1 + 8)) < ((unsigned int)(a1))) goto loc_0096B148;
    if (((unsigned int)(a1 + 8 + 4)) < 4) goto loc_0096B148;
    if (((unsigned int)(a1 + 8 + 4 + 4)) < ((unsigned int)(a1 + 8 + 4))) goto loc_0096B148;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1)) < ((unsigned int)(a1 + 8 + 4 + 4))) goto loc_0096B148;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1))) goto loc_0096B148;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 32)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4 * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4))) goto loc_0096B148;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = result;
    if ((*(unsigned int *)(v_rsp - 95 - 53)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 32)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4 * 1))) goto loc_0096B4FD;
    if (sign_flag) goto loc_0096B4FD;
    result = KeQueryTimeIncrement((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 32)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4 * 1, v_r13 + 4 + 28 + 8 + 8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)), (unsigned int)((unsigned int)(result)));
    v_rsi = 0;
    a1 = ((unsigned int)((unsigned int)(result))) * (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)) + a1 + 8 + 4 + 4 * 1 + 4));
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 - 69) = 0;
    *(unsigned int *)(v_rsp - 95 - 65) = 0;
    *(unsigned int *)(v_rsp - 95 - 53) = 0;
    v_rbx = (v_r13 + 4 + 28 + 8 + 8) >> (11);
    result = (v_rbx) >> (63);
    v_rbx = (v_rbx) + (result);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_rbx;
    result = RtlInitUnicodeString(v_rsp - 95 + 7, v_rip + 2016705, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 16)), (unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(v_rip + 6738059)) != (v_rip + 3116)) goto loc_0096BC1B;
    v_stack_mA0 = v_rsp - 95 - 53;
    result = sub_0096BFF0(v_rsp - 95 + 7, v_rsp - 95 - 69, v_rsp - 95 - 65, v_rsi + 4);
loc_0096B3EB:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_0096BC32;
    if (sign_flag) goto loc_0096B40D;
    if ((*(unsigned int *)(v_rsp - 95 - 69)) != 4) goto loc_0096BC32;
    if ((*(unsigned int *)(v_rsp - 95 - 65)) == 0) goto loc_0096BC32;
loc_0096B40D:
    if ((*(unsigned int *)(v_rip + 6737252)) != ((unsigned int)(v_rsi + 1))) goto loc_0096BC3A;
loc_0096B41A:
    a1 = (v_rbx) - (*(unsigned __int64 *)(v_rip + 6737297));
    if (sign_flag) goto loc_0096BBAE;
loc_0096B432:
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((unsigned int)(v_rsi + 1) == 0) goto loc_0096B980;
loc_0096B448:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) + (48));
    result = (*(unsigned __int64 *)(v_rsp - 95 - 33)) - (*(unsigned __int64 *)(v_rip + 6737247));
    if (result < 0xA4CBFBULL) goto loc_0096B633;
    a4 = 0;
    v_stack_mA0 = v_rsp - 95 - 1;
    result = KeWaitForSingleObject(v_rip + 5790049, a4 + 6, 1, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) + (48));
    if (sign_flag) goto loc_0096B633;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 192) goto loc_0096B633;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 258) goto loc_0096B633;
    v_rsi = 0;
    if ((*(unsigned int *)(v_rip + 6737086)) != ((unsigned int)(v_rsi + 1))) goto loc_0096BC4D;
loc_0096B4C8:
    result = (*(unsigned __int64 *)(v_rsp - 95 - 33)) - (*(unsigned __int64 *)(v_rip + 6736965));
    *(unsigned int *)(v_rip + 6737062) = (unsigned int)(v_rsi + 1);
    if ((unsigned int)(v_rsi + 1) == 0) goto loc_0096BA01;
loc_0096B4E3:
    a2 = 0;
    result = KeReleaseMutex(v_rip + 5789940, a2, (unsigned int)((unsigned int)(result)), a4);
loc_0096B4FD:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + 48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + 48) == 0) goto loc_0096BCA5;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + 48)), (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_0096BCAF;
    *(unsigned __int64 *)(a4 + 8) = result;
    goto loc_0096B542;
loc_0096B534:
    if (sign_flag) goto loc_0096B14D;
loc_0096B542:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B8B5;
    a1 = 0;
loc_0096B561:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B58D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + ((unsigned int)(a1 + 4)));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B561;
loc_0096B58D:
    if ((a3 + 4) < a3) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_0096B8F4;
    *(unsigned int *)(a3) = (unsigned int)(a1 + 4);
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49)));
loc_0096B5B5:
    v_r15 = (unsigned int)((*(unsigned __int64 *)(v_r12)) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B64D;
    a1 = 0;
loc_0096B5CE:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B5F7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B5CE;
loc_0096B5F7:
    if ((a4 + 4) < a4) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 12) > a1) goto loc_0096B8F4;
    *(unsigned int *)(a4) = 8;
    *(unsigned __int64 *)(a4 + 4) = a3;
loc_0096B622:
    goto loc_0096B674;
loc_0096B627:
    goto loc_0096AFCD;
loc_0096B631:
loc_0096B633:
    goto loc_0096B4FD;
loc_0096B63C:
    if (!sign_flag) goto loc_0096B292;
    goto loc_0096B14D;
loc_0096B64D:
    result = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a4 + 4))) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B622;
    if (sign_flag) goto loc_0096B14D;
loc_0096B674:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B6DC;
    a1 = 0;
loc_0096B686:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B6AF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B686;
loc_0096B6AF:
    if ((a3 + 4) < a3) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_0096B8F4;
    *(unsigned int *)(a3) = (unsigned int)(a1 + 4);
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45)));
loc_0096B6D7:
    goto loc_0096B703;
loc_0096B6DC:
    result = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8); }
    v_rbx = (unsigned int)((v_rbx) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B6D7;
    if (sign_flag) goto loc_0096B14D;
loc_0096B703:
    if (*(unsigned __int64 *)(v_rsp - 95 - 25) != 0) goto loc_0096B788;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) != 0) goto loc_0096B78D;
loc_0096B711:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B797;
    a1 = 0;
loc_0096B71F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B748;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B71F;
loc_0096B748:
    if ((a3 + 4) < a3) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))) + 4) + (a3);
    if (result > a1) goto loc_0096B8F4;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)));
    if (*(unsigned __int64 *)(v_rsp - 95 - 25) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 25);
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)))), a3 + 4);
    }
    goto loc_0096B7C1;
loc_0096B788:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) != 0) goto loc_0096B711;
loc_0096B78D:
    goto loc_0096B14D;
loc_0096B797:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73)) + 4) + ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))));
    result = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)(a1); }
    v_rbx = (unsigned int)(((unsigned int)(0xC000000DULL)) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B783;
    if (sign_flag) goto loc_0096B14D;
loc_0096B7C1:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B829;
    a1 = 0;
loc_0096B7D3:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B7FC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B7D3;
loc_0096B7FC:
    if ((a3 + 4) < a3) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_0096B8F4;
    *(unsigned int *)(a3) = (unsigned int)(a1 + 4);
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 61)));
loc_0096B824:
    goto loc_0096B850;
loc_0096B829:
    result = (unsigned int)((unsigned int)(v_r15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8); }
    v_rbx = (unsigned int)((v_rbx) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B824;
    if (sign_flag) goto loc_0096B14D;
loc_0096B850:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0096B8CE;
    a1 = 0;
loc_0096B85E:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0096B887;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < ((unsigned int)(a1 + 4))) goto loc_0096B148;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_0096B148;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0096B85E;
loc_0096B887:
    if ((a3 + 4) < a3) goto loc_0096B148;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_0096B8F4;
    *(unsigned int *)(a3) = (unsigned int)(a1 + 4);
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)(a4 + 12)));
loc_0096B8AB:
loc_0096B8AE:
    v_rbx = 0;
    goto loc_0096B14D;
loc_0096B8B5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B9CE;
    goto loc_0096B148;
loc_0096B8CE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8); }
    v_rbx = (unsigned int)((v_rbx) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(v_r15);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0096B8AB;
    if (!sign_flag) goto loc_0096B8AE;
    goto loc_0096B14D;
loc_0096B8F4:
    goto loc_0096B14D;
loc_0096B8FE:
    v_r13 = 0;
loc_0096B901:
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
    a4 = 0;
    a3 = 0;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)(0xC0000023ULL));
    if ((*(unsigned __int64 *)(v_rip + 6736691)) != ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_0096BBD0;
    v_stack_mA0 = v_rsp - 95 - 61;
    result = sub_0096BFF0(v_rsp - 95 - 17, v_rsp - 95 - 45, a3, a4);
loc_0096B936:
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0096BBA1;
    if (((unsigned int)(v_r15)) < (*(unsigned int *)(v_rsp - 95 - 61))) goto loc_0096B9E0;
    a4 = 0;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 61)));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
    *(unsigned int *)(v_rsp - 95 - 49) = 0;
    if (0 != 0) goto loc_0096B227;
    goto loc_0096B2A0;
loc_0096B976:
    goto loc_0096AFCD;
loc_0096B980:
    if ((*(unsigned int *)(v_rip + 6735854)) != ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 41)))) goto loc_0096B448;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) == 0) goto loc_0096B448;
    v_stack_m90 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 41));
    v_stack_m98 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 41));
    a4 = 0;
    a3 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(v_rsp - 95 - 41);
    a2 = 0;
    *(unsigned int *)(v_rip + 6735802) = 1;
    result = ZwUpdateWnfStateData(v_rip - 9800895, a2, a3, a4);
    goto loc_0096B448;
loc_0096B9C4:
    goto loc_0096AFCD;
loc_0096B9CE:
    *(unsigned int *)(a4 + 4) = (unsigned int)(v_rip - 9800895);
    goto loc_0096B5B5;
loc_0096B9E0:
    if ((unsigned int)(v_r15) != 0) goto loc_0096B2A0;
    a4 = 0;
    *(unsigned int *)(v_rsp - 95 - 49) = 0;
    *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)((unsigned int)(0xC000003EULL));
    *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)));
    goto loc_0096B2A0;
loc_0096BA01:
    if ((*(unsigned int *)(v_rip + 6735741)) == 0) goto loc_0096B4E3;
    if (((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))) < 0xADF4FCULL) goto loc_0096B4E3;
    a3 = 0;
    result = KeSetEvent(v_rip + 5788573, a3 + 1, a3, a4);
    *(unsigned int *)(v_rsp - 95 - 69) = 0;
    *(unsigned int *)(v_rsp - 95 - 65) = 4;
    *(unsigned int *)(v_rsp - 95 - 53) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    result = ZwOpenKey(v_rsp - 95 - 33, 4 - 3, v_rip + 6737445, a4);
    if (!sign_flag) goto loc_0096BB88;
    if ((*(unsigned __int64 *)(v_rip + 6736353)) != (v_rip + 1432)) goto loc_0096BC67;
    v_stack_mA0 = v_rsp - 95 - 53;
    result = sub_0096BFF0(v_rip + 6736970, v_rsp - 95 - 65, v_rsp - 95 - 69, 4);
loc_0096BA90:
    if (sign_flag) goto loc_0096BB79;
loc_0096BA9C:
    if ((*(unsigned int *)(v_rsp - 95 - 65)) != 4) goto loc_0096BB79;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69)) - 1)) > 2) goto loc_0096BB79;
loc_0096BAB2:
    if (*(unsigned __int64 *)(v_rsp - 95 - 33) != 0) goto loc_0096BC81;
loc_0096BABF:
    result = 0;
    *(unsigned int *)(v_rsp - 95 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = 0;
    *(unsigned int *)(v_rsp - 95 + 31) = 0;
    *(unsigned int *)(v_rsp - 95 - 69) = 0;
    if ((*(unsigned __int64 *)(v_rip + 6736238)) != (v_rip + 1432)) goto loc_0096BC8B;
    v_stack_mA0 = v_rsp - 95 - 69;
    result = sub_0096BFF0(v_rip + 6736873, v_rsp - 95 - 65, v_rsp - 95 + 23, 12);
loc_0096BB01:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 73))) + (48));
    if (sign_flag) goto loc_0096BB47;
    if ((*(unsigned int *)(v_rsp - 95 - 65)) != 3) goto loc_0096BB47;
    if ((*(unsigned int *)(v_rsp - 95 - 69)) != 12) goto loc_0096BB47;
    a2 = 0;
loc_0096BB30:
    if (0 >= 3) goto loc_0096BB47;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + a2 * 4 + 23))))) & (15));
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 69))))) goto loc_0096BB57;
    a2 = (unsigned int)((a2) + 1);
    goto loc_0096BB30;
loc_0096BB47:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 6735115))) & (0xFFFF3211ULL));
    result = (unsigned int)((result) | (0x3211ULL));
loc_0096BB57:
    *(unsigned int *)(v_rip + 6735099) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57))))) != 0) goto loc_0096B631;
    a2 = 0;
    result = KeReleaseMutex(v_rip + 5788273, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096B633;
loc_0096BB79:
    *(unsigned int *)(v_rsp - 95 - 69) = 1;
    goto loc_0096BAB2;
loc_0096BB88:
    *(unsigned int *)(v_rsp - 95 - 69) = 3;
    goto loc_0096BA9C;
loc_0096BB97:
    goto loc_0096AFCD;
loc_0096BBA1:
    if (!sign_flag) goto loc_0096BBE7;
    goto loc_0096B14D;
loc_0096BBAE:
    a1 = (unsigned int)((v_rip + 5788273) & (1));
    result = (v_rip + 5788273) >> (1);
    result = (result) | (a1);
    goto loc_0096B432;
loc_0096BBC8:
    goto loc_0096B0BF;
loc_0096BBD0:
    v_stack_mA0 = v_rsp - 95 - 61;
    result = guard_dispatch_icall(v_rsp - 95 - 17, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096B936;
loc_0096BBE7:
    goto loc_0096B14D;
loc_0096BBFA:
    goto loc_0096B14D;
loc_0096BC04:
    v_stack_mA0 = v_rsp - 95 - 61;
    result = guard_dispatch_icall(v_rsp - 95 - 17, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096B281;
loc_0096BC1B:
    v_stack_mA0 = v_rsp - 95 - 53;
    result = guard_dispatch_icall(v_rsp - 95 + 7, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096B3EB;
loc_0096BC32:
    goto loc_0096B40D;
loc_0096BC3A:
    *(unsigned __int64 *)(v_rip + 6735223) = (unsigned int)(0xC0000017ULL);
    *(unsigned int *)(v_rip + 6735152) = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 41))));
    goto loc_0096B41A;
loc_0096BC4D:
    result = KeResetEvent(v_rip + 5788003, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096B4C8;
loc_0096BC67:
    v_stack_mA0 = v_rsp - 95 - 53;
    result = guard_dispatch_icall(v_rip + 6736473, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096BA90;
loc_0096BC81:
    result = ZwClose(v_rip + 6736473, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096BABF;
loc_0096BC8B:
    v_stack_mA0 = v_rsp - 95 - 69;
    result = guard_dispatch_icall(v_rip + 6736453, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 57)))), (unsigned int)((unsigned int)(result)));
    goto loc_0096BB01;
loc_0096BCA5:
    goto loc_0096B534;
loc_0096BCAF:
    goto loc_0096B534;
}
```

## 5. (Beta) C Style

```c
int64_t SPCallServerHandleQueryPolicy(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x49F7F2)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    local_rsi = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = Arg3;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = Arg2;
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x3D) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = v_xmm0;
    if (Arg1 == NULL) goto loc_0096B976;
    if (Arg2 == 0) goto loc_0096B976;
    if (Arg4 == NULL) goto loc_0096B976;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_0096B976;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_0096B976;
loc_0096AFB6:
    if (0 >= 3) goto loc_0096B00B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_0096AFFD;
loc_0096AFC8:
loc_0096AFCD:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x8) + 4, 0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    return result;
loc_0096AFFD:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_0096AFC8;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_0096AFB6;
loc_0096B00B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_0096AFC8;
    local_r12 = *(uint64_t *)(v_stack_m28 + 0x38);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r12 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_0096BB97;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30))) <= 4) goto loc_0096B976;
loc_0096B034:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))))) >= 4) goto loc_0096B058;
    if ((Arg1 + 4) < Arg1) goto loc_0096AFC8;
    if ((Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1) < (Arg1 + 4)) goto loc_0096AFC8;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) + 1);
    goto loc_0096B034;
loc_0096B058:
    if ((Arg1 + 4) < (Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1)) goto loc_0096AFC8;
    Arg1 = *(uint64_t *)(v_stack_m28 + 0x38);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) != 0) { Arg1 = Arg1 + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_0096B9C4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) != 0) goto loc_0096B9C4;
    result = ((uint32_t)(*(uint32_t *)(arg1))) >> (1);
    if (((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38))) != (*(uint16_t *)(arg1 + result * 2 - 0x2))) goto loc_0096B9C4;
    if (Arg1 == NULL) goto loc_0096B9C4;
    if (result == 0) goto loc_0096BBC8;
loc_0096B0A4:
    if ((*(uint16_t *)(arg1)) == ((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_0096B0B3;
    Arg1 = (Arg1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0096B0A4;
loc_0096B0B3:
    if (result == 0) goto loc_0096BBC8;
    Arg2 = (result) - (result);
loc_0096B0BF:
    if (result == 0) goto loc_0096B9C4;
    if ((Arg2 + Arg2 * 1 + 2) != ((uint32_t)(*(uint32_t *)(arg1)))) goto loc_0096B9C4;
    Arg1 = (Arg2 + Arg2 * 1) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_0096B9C4;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_0096B627;
    result = memcpy(result, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 * 2 + 2)))), Arg4);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8) == 0) goto loc_0096B78D;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30))) <= 5) goto loc_0096B78D;
    Arg3 = 0;
loc_0096B136:
    if (0 >= 5) goto loc_0096B186;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8) + 4) >= (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8))) goto loc_0096B178;
loc_0096B148:
loc_0096B14D:
    result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x19) == 0) goto loc_0096AFCD;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x19), Arg2, Arg3, Arg4);
    goto loc_0096AFCD;
loc_0096B178:
    if ((Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8))) * 1) < 0) goto loc_0096B148;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_0096B136;
loc_0096B186:
    if (0 < (Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8))) * 1)) goto loc_0096B148;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8)))) != 0) { result = 0; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8))))) != 4) goto loc_0096B8F4;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint32_t *)((uint32_t)(0xC0000095ULL))) <= 6) goto loc_0096B78D;
    Arg3 = 0;
loc_0096B1B1:
    if (0 >= 6) goto loc_0096B1D8;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19) + 4) < (*(uint64_t *)(local_rsp - 0x5F - 0x19))) goto loc_0096B148;
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19))) * 1) < (*(uint64_t *)(local_rsp - 0x5F - 0x19) + 4)) goto loc_0096B148;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_0096B1B1;
loc_0096B1D8:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x19) + 4) < (*(uint64_t *)(local_rsp - 0x5F - 0x19) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19))) * 1)) goto loc_0096B148;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19)))) != 0) { local_rbx = *(uint64_t *)(local_rsp - 0x5F - 0x19) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19))))) != 4) goto loc_0096B8F4;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)));
    result = RtlInitUnicodeString(local_rsp - 95 - 17, result, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))) == 0) goto loc_0096B8FE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) > 0x100000ULL) goto loc_0096B901;
loc_0096B227:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))), (uint32_t)(0x20534C53ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = result;
    if (result == 0) goto loc_0096BBFA;
    if ((*(uint64_t *)(v_rip + 0x66D1F3)) != (v_rip + 3476)) goto loc_0096BC04;
    v_stack_mA0 = local_rsp - 95 - 61;
    result = sub_0096BFF0(local_rsp - 95 - 17, local_rsp - 95 - 45, result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))));
loc_0096B281:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0096B63C;
loc_0096B292:
    local_r13 = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) >= (*(uint32_t *)(local_rsp - 0x5F - 0x3D))) {
        local_r13 = *(uint32_t *)(local_rsp - 0x5F - 0x3D);
        *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)(local_r13);
    }
    if (((uint32_t)(local_r13 + 4)) < 4) goto loc_0096B148;
    if (((uint32_t)(local_r13 + 4 + 28)) < 28) goto loc_0096B148;
    if (((uint32_t)(local_r13 + 4 + 28 + 8)) < ((uint32_t)(local_r13 + 4 + 28))) goto loc_0096B148;
    if (((uint32_t)(local_r13 + 4 + 28 + 8 + 8)) < ((uint32_t)(local_r13 + 4 + 28 + 8))) goto loc_0096B148;
    if (((uint32_t)(local_r13 + 4 + 28 + 8 + 8 + 8)) < 8) goto loc_0096B148;
    Arg1 = (uint32_t)((local_r13 + 4 + 28 + 8 + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg1)) < ((uint32_t)(local_r13 + 4 + 28 + 8 + 8 + 8))) goto loc_0096B148;
    if (((uint32_t)(Arg1 + 8)) < ((uint32_t)(Arg1))) goto loc_0096B148;
    if (((uint32_t)(Arg1 + 8 + 4)) < 4) goto loc_0096B148;
    if (((uint32_t)(Arg1 + 8 + 4 + 4)) < ((uint32_t)(Arg1 + 8 + 4))) goto loc_0096B148;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1)) < ((uint32_t)(Arg1 + 8 + 4 + 4))) goto loc_0096B148;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1 + 4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1))) goto loc_0096B148;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x20)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1 + 4 * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1 + 4))) goto loc_0096B148;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = result;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x35)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x20)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1 + 4 * 1))) goto loc_0096B4FD;
    if (sign_flag) goto loc_0096B4FD;
    result = KeQueryTimeIncrement((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x20)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + Arg1 + 8 + 4 + 4 * 1 + 4 * 1, local_r13 + 4 + 28 + 8 + 8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)), (uint32_t)((uint32_t)(result)));
    local_rsi = 0;
    Arg1 = ((uint32_t)((uint32_t)(result))) * (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)) + arg1 + 0x8 + 0x4 + 0x4 * 1 + 0x4));
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = 0;
    local_rbx = (local_r13 + 4 + 28 + 8 + 8) >> (11);
    result = (local_rbx) >> (63);
    local_rbx = (local_rbx) + (result);
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = local_rbx;
    result = RtlInitUnicodeString(local_rsp - 95 + 7, v_rip + 2016705, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x10)), (uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(v_rip + 0x66D08B)) != (v_rip + 3116)) goto loc_0096BC1B;
    v_stack_mA0 = local_rsp - 95 - 53;
    result = sub_0096BFF0(local_rsp - 95 + 7, local_rsp - 95 - 69, local_rsp - 95 - 65, local_rsi + 4);
loc_0096B3EB:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_0096BC32;
    if (sign_flag) goto loc_0096B40D;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x45)) != 4) goto loc_0096BC32;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x41)) == 0) goto loc_0096BC32;
loc_0096B40D:
    if ((*(uint32_t *)(v_rip + 0x66CD64)) != ((uint32_t)(local_rsi + 1))) goto loc_0096BC3A;
loc_0096B41A:
    Arg1 = (local_rbx) - (*(uint64_t *)(v_rip + 0x66CD91));
    if (sign_flag) goto loc_0096BBAE;
loc_0096B432:
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((uint32_t)(local_rsi + 1) == 0) goto loc_0096B980;
loc_0096B448:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) + (48));
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x21)) - (*(uint64_t *)(v_rip + 0x66CD5F));
    if (result < 0xA4CBFBULL) goto loc_0096B633;
    Arg4 = 0;
    v_stack_mA0 = local_rsp - 95 - 1;
    result = KeWaitForSingleObject(v_rip + 5790049, Arg4 + 6, 1, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) + (48));
    if (sign_flag) goto loc_0096B633;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 192) goto loc_0096B633;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 258) goto loc_0096B633;
    local_rsi = 0;
    if ((*(uint32_t *)(v_rip + 0x66CCBE)) != ((uint32_t)(local_rsi + 1))) goto loc_0096BC4D;
loc_0096B4C8:
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x21)) - (*(uint64_t *)(v_rip + 0x66CC45));
    *(uint32_t *)(v_rip + 0x66CCA6) = (uint32_t)(local_rsi + 1);
    if ((uint32_t)(local_rsi + 1) == 0) goto loc_0096BA01;
loc_0096B4E3:
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 5789940, Arg2, (uint32_t)((uint32_t)(result)), Arg4);
loc_0096B4FD:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + 48);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + 48) == 0) goto loc_0096BCA5;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + 48)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_0096BCAF;
    *(uint64_t *)(arg4 + 0x8) = result;
    goto loc_0096B542;
loc_0096B534:
    if (sign_flag) goto loc_0096B14D;
loc_0096B542:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B8B5;
    Arg1 = 0;
loc_0096B561:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B58D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + ((uint32_t)(Arg1 + 4)));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B561;
loc_0096B58D:
    if ((Arg3 + 4) < Arg3) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(Arg3) = (uint32_t)(Arg1 + 4);
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31)));
loc_0096B5B5:
    local_r15 = (uint32_t)((*(uint64_t *)(local_r12)) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B64D;
    Arg1 = 0;
loc_0096B5CE:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B5F7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B5CE;
loc_0096B5F7:
    if ((Arg4 + 4) < Arg4) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg4 + 12) > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(arg4) = 8;
    *(uint64_t *)(arg4 + 0x4) = Arg3;
loc_0096B622:
    goto loc_0096B674;
loc_0096B627:
    goto loc_0096AFCD;
loc_0096B631:
loc_0096B633:
    goto loc_0096B4FD;
loc_0096B63C:
    if (!sign_flag) goto loc_0096B292;
    goto loc_0096B14D;
loc_0096B64D:
    result = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg4 + 4))) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B622;
    if (sign_flag) goto loc_0096B14D;
loc_0096B674:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B6DC;
    Arg1 = 0;
loc_0096B686:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B6AF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B686;
loc_0096B6AF:
    if ((Arg3 + 4) < Arg3) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(Arg3) = (uint32_t)(Arg1 + 4);
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D)));
loc_0096B6D7:
    goto loc_0096B703;
loc_0096B6DC:
    result = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8); }
    local_rbx = (uint32_t)((local_rbx) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B6D7;
    if (sign_flag) goto loc_0096B14D;
loc_0096B703:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x19) != 0) goto loc_0096B788;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) != 0) goto loc_0096B78D;
loc_0096B711:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B797;
    Arg1 = 0;
loc_0096B71F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B748;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B71F;
loc_0096B748:
    if ((Arg3 + 4) < Arg3) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))) + 4) + (Arg3);
    if (result > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(Arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)));
    if (*(uint64_t *)(local_rsp - 0x5F - 0x19) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x19);
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)))), Arg3 + 4);
    }
    goto loc_0096B7C1;
loc_0096B788:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) != 0) goto loc_0096B711;
loc_0096B78D:
    goto loc_0096B14D;
loc_0096B797:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49)) + 4) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)))));
    result = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)(Arg1); }
    local_rbx = (uint32_t)(((uint32_t)(0xC000000DULL)) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B783;
    if (sign_flag) goto loc_0096B14D;
loc_0096B7C1:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B829;
    Arg1 = 0;
loc_0096B7D3:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B7FC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B7D3;
loc_0096B7FC:
    if ((Arg3 + 4) < Arg3) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(Arg3) = (uint32_t)(Arg1 + 4);
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x3D)));
loc_0096B824:
    goto loc_0096B850;
loc_0096B829:
    result = (uint32_t)((uint32_t)(local_r15));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8); }
    local_rbx = (uint32_t)((local_rbx) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B824;
    if (sign_flag) goto loc_0096B14D;
loc_0096B850:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_0096B8CE;
    Arg1 = 0;
loc_0096B85E:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_0096B887;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1 + 4))) goto loc_0096B148;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_0096B148;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0096B85E;
loc_0096B887:
    if ((Arg3 + 4) < Arg3) goto loc_0096B148;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_0096B8F4;
    *(uint32_t *)(Arg3) = (uint32_t)(Arg1 + 4);
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(Arg4 + 12)));
loc_0096B8AB:
loc_0096B8AE:
    local_rbx = 0;
    goto loc_0096B14D;
loc_0096B8B5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B9CE;
    goto loc_0096B148;
loc_0096B8CE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8); }
    local_rbx = (uint32_t)((local_rbx) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(local_r15);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_0096B8AB;
    if (!sign_flag) goto loc_0096B8AE;
    goto loc_0096B14D;
loc_0096B8F4:
    goto loc_0096B14D;
loc_0096B8FE:
    local_r13 = 0;
loc_0096B901:
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
    Arg4 = 0;
    Arg3 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)(0xC0000023ULL));
    if ((*(uint64_t *)(v_rip + 0x66CB33)) != ((uint32_t)(*(uint32_t *)(arg4 + 0x4)))) goto loc_0096BBD0;
    v_stack_mA0 = local_rsp - 95 - 61;
    result = sub_0096BFF0(local_rsp - 95 - 17, local_rsp - 95 - 45, Arg3, Arg4);
loc_0096B936:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0096BBA1;
    if (((uint32_t)(local_r15)) < (*(uint32_t *)(local_rsp - 0x5F - 0x3D))) goto loc_0096B9E0;
    Arg4 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x3D)));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0;
    if (0 != 0) goto loc_0096B227;
    goto loc_0096B2A0;
loc_0096B976:
    goto loc_0096AFCD;
loc_0096B980:
    if ((*(uint32_t *)(v_rip + 0x66C7EE)) != ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x29)))) goto loc_0096B448;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) == 0) goto loc_0096B448;
    v_stack_m90 = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x29));
    v_stack_m98 = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x29));
    Arg4 = 0;
    Arg3 = 0;
    v_stack_mA0 = *(uint64_t *)(local_rsp - 0x5F - 0x29);
    Arg2 = 0;
    *(uint32_t *)(v_rip + 0x66C7BA) = 1;
    result = ZwUpdateWnfStateData(v_rip - 9800895, Arg2, Arg3, Arg4);
    goto loc_0096B448;
loc_0096B9C4:
    goto loc_0096AFCD;
loc_0096B9CE:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(v_rip - 9800895);
    goto loc_0096B5B5;
loc_0096B9E0:
    if ((uint32_t)(local_r15) != 0) goto loc_0096B2A0;
    Arg4 = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)((uint32_t)(0xC000003EULL));
    *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)));
    goto loc_0096B2A0;
loc_0096BA01:
    if ((*(uint32_t *)(v_rip + 0x66C77D)) == 0) goto loc_0096B4E3;
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))) < 0xADF4FCULL) goto loc_0096B4E3;
    Arg3 = 0;
    result = KeSetEvent(v_rip + 5788573, Arg3 + 1, Arg3, Arg4);
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = 4;
    *(uint32_t *)(local_rsp - 0x5F - 0x35) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    result = ZwOpenKey(local_rsp - 95 - 33, 4 - 3, v_rip + 6737445, Arg4);
    if (!sign_flag) goto loc_0096BB88;
    if ((*(uint64_t *)(v_rip + 0x66C9E1)) != (v_rip + 1432)) goto loc_0096BC67;
    v_stack_mA0 = local_rsp - 95 - 53;
    result = sub_0096BFF0(v_rip + 6736970, local_rsp - 95 - 65, local_rsp - 95 - 69, 4);
loc_0096BA90:
    if (sign_flag) goto loc_0096BB79;
loc_0096BA9C:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x41)) != 4) goto loc_0096BB79;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45)) - 1)) > 2) goto loc_0096BB79;
loc_0096BAB2:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x21) != 0) goto loc_0096BC81;
loc_0096BABF:
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 0;
    if ((*(uint64_t *)(v_rip + 0x66C96E)) != (v_rip + 1432)) goto loc_0096BC8B;
    v_stack_mA0 = local_rsp - 95 - 69;
    result = sub_0096BFF0(v_rip + 6736873, local_rsp - 95 - 65, local_rsp - 95 + 23, 12);
loc_0096BB01:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x49))) + (48));
    if (sign_flag) goto loc_0096BB47;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x41)) != 3) goto loc_0096BB47;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x45)) != 12) goto loc_0096BB47;
    Arg2 = 0;
loc_0096BB30:
    if (0 >= 3) goto loc_0096BB47;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + Arg2 * 4 + 0x17))))) & (15));
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x45))))) goto loc_0096BB57;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0096BB30;
loc_0096BB47:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x66C50B))) & (0xFFFF3211ULL));
    result = (uint32_t)((result) | (0x3211ULL));
loc_0096BB57:
    *(uint32_t *)(v_rip + 0x66C4FB) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39))))) != 0) goto loc_0096B631;
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 5788273, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096B633;
loc_0096BB79:
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 1;
    goto loc_0096BAB2;
loc_0096BB88:
    *(uint32_t *)(local_rsp - 0x5F - 0x45) = 3;
    goto loc_0096BA9C;
loc_0096BB97:
    goto loc_0096AFCD;
loc_0096BBA1:
    if (!sign_flag) goto loc_0096BBE7;
    goto loc_0096B14D;
loc_0096BBAE:
    Arg1 = (uint32_t)((v_rip + 5788273) & (1));
    result = (v_rip + 5788273) >> (1);
    result = (result) | (Arg1);
    goto loc_0096B432;
loc_0096BBC8:
    goto loc_0096B0BF;
loc_0096BBD0:
    v_stack_mA0 = local_rsp - 95 - 61;
    result = guard_dispatch_icall(local_rsp - 95 - 17, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096B936;
loc_0096BBE7:
    goto loc_0096B14D;
loc_0096BBFA:
    goto loc_0096B14D;
loc_0096BC04:
    v_stack_mA0 = local_rsp - 95 - 61;
    result = guard_dispatch_icall(local_rsp - 95 - 17, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096B281;
loc_0096BC1B:
    v_stack_mA0 = local_rsp - 95 - 53;
    result = guard_dispatch_icall(local_rsp - 95 + 7, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096B3EB;
loc_0096BC32:
    goto loc_0096B40D;
loc_0096BC3A:
    *(uint64_t *)(v_rip + 0x66C577) = (uint32_t)(0xC0000017ULL);
    *(uint32_t *)(v_rip + 0x66C530) = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x29))));
    goto loc_0096B41A;
loc_0096BC4D:
    result = KeResetEvent(v_rip + 5788003, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096B4C8;
loc_0096BC67:
    v_stack_mA0 = local_rsp - 95 - 53;
    result = guard_dispatch_icall(v_rip + 6736473, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096BA90;
loc_0096BC81:
    result = ZwClose(v_rip + 6736473, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096BABF;
loc_0096BC8B:
    v_stack_mA0 = local_rsp - 95 - 69;
    result = guard_dispatch_icall(v_rip + 6736453, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x39)))), (uint32_t)((uint32_t)(result)));
    goto loc_0096BB01;
loc_0096BCA5:
    goto loc_0096B534;
loc_0096BCAF:
    goto loc_0096B534;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096AF24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
