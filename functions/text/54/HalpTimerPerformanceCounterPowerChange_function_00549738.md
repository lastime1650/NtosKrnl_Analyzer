# HalpTimerPerformanceCounterPowerChange

- RVA: `0x00549738`–`0x00549DE9` (길이 `1,713` bytes)
- VA: `0x0000000140549738`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3E18`
- 디코드: `426`개 명령, `1,713/1,713` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0054977A` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549786` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005497A6` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x005497FD` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0054980E` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x00549818` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005498C3` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x005498DB` → [HalpHvCounterQueryCounter](../37/HalpHvCounterQueryCounter_function_00378F50.md) (function, `0x00378F50`)
- `0x005498E5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549914` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x00549927` → [HalpTimerCalibratePerformanceCounter](../4A/HalpTimerCalibratePerformanceCounter_function_004AB874.md) (function, `0x004AB874`)
- `0x00549948` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x005499A5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x005499E0` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x005499F1` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x005499FB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549A9F` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549AB0` → [HalpHvCounterQueryCounter](../37/HalpHvCounterQueryCounter_function_00378F50.md) (function, `0x00378F50`)
- `0x00549ABA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549B09` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549B1A` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x00549B24` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549BC6` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549BD7` → [HalpHvCounterQueryCounter](../37/HalpHvCounterQueryCounter_function_00378F50.md) (function, `0x00378F50`)
- `0x00549BE1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549C10` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x00549C60` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549C71` → [HalpHpetQueryCounter](../37/HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x00549C7B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549D1A` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x00549D2B` → [HalpHvCounterQueryCounter](../37/HalpHvCounterQueryCounter_function_00378F50.md) (function, `0x00378F50`)
- `0x00549D35` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00549D64` → [HalpTimerScaleCounter](../37/HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x00549D6F` → [HalpTimerCalibratePerformanceCounter](../4A/HalpTimerCalibratePerformanceCounter_function_004AB874.md) (function, `0x004AB874`)
- `0x00549D94` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalpTimerPowerChange](HalpTimerPowerChange_function_00549DF0.md) at `0x00549E5B`

### Static image references
- `0x0054974E` → RVA `0x00FC3FB8` (`.data`; read)
- `0x005497AC` → RVA `0x00E10348` (`.data`; read)
- `0x005497BF` → RVA `0x00FC3FD0` (`.data`; read)
- `0x005497CA` → RVA `0x00E10348` (`.data`; write)
- `0x005497E5` → RVA `0x00379660` (`HalpHpetQueryCounter`; read)
- `0x005498CC` → RVA `0x00378F50` (`HalpHvCounterQueryCounter`; read)
- `0x0054994E` → RVA `0x00FC3FD0` (`.data`; write)
- `0x00549955` → RVA `0x00FC3FB8` (`.data`; write)
- `0x00549979` → RVA `0x00FC4140` (`.data`; read)
- `0x00549C28` → RVA `0x00FC40D0` (`.data`; read)
- `0x00549C35` → RVA `0x00E10350` (`.data`; read/write)
- `0x00549DAA` → RVA `0x00548F20` (`HalpTimerDelayedQueryCounter`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00549738  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0054973D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00549742  56                              push rsi
00549743  57                              push rdi
00549744  41 54                           push r12
00549746  41 55                           push r13
00549748  41 56                           push r14
0054974A  48 83 EC 30                     sub rsp, 0x30
0054974E  48 8B 2D 63 A8 A7 00            mov rbp, qword ptr [rip + 0xa7a863]
00549755  45 33 ED                        xor r13d, r13d
00549758  48 89 6C 24 70                  mov qword ptr [rsp + 0x70], rbp
0054975D  48 85 ED                        test rbp, rbp
00549760  0F 84 FB 01 00 00               je 0x140549961
00549766  48 3B CD                        cmp rcx, rbp
00549769  0F 85 62 06 00 00               jne 0x140549dd1
0054976F  84 D2                           test dl, dl
00549771  0F 84 5A 06 00 00               je 0x140549dd1
00549777  48 8B CD                        mov rcx, rbp
0054977A  E8 81 FD CB FF                  call 0x140209500
0054977F  48 8B C8                        mov rcx, rax
00549782  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00549786  E8 45 13 17 00                  call 0x1406baad0
0054978B  85 C0                           test eax, eax
0054978D  79 1D                           jns 0x1405497ac
0054978F  48 98                           cdqe
00549791  41 8D 4D 5C                     lea ecx, [r13 + 0x5c]
00549795  4C 8B CD                        mov r9, rbp
00549798  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0054979D  BA 13 01 00 00                  mov edx, 0x113
005497A2  45 8D 45 0F                     lea r8d, [r13 + 0xf]
005497A6  E8 B5 3E FB FF                  call 0x1404fd660
005497AB  CC                              int3
005497AC  48 8B 05 95 6B 8C 00            mov rax, qword ptr [rip + 0x8c6b95]
005497B3  48 85 C0                        test rax, rax
005497B6  74 19                           je 0x1405497d1
005497B8  48 8B 0D 89 6B 8C 00            mov rcx, qword ptr [rip + 0x8c6b89]
005497BF  48 8B 05 0A A8 A7 00            mov rax, qword ptr [rip + 0xa7a80a]
005497C6  48 89 48 70                     mov qword ptr [rax + 0x70], rcx
005497CA  4C 89 2D 77 6B 8C 00            mov qword ptr [rip + 0x8c6b77], r13
005497D1  48 8B 3D F8 A7 A7 00            mov rdi, qword ptr [rip + 0xa7a7f8]
005497D8  83 BF DC 00 00 00 40            cmp dword ptr [rdi + 0xdc], 0x40
005497DF  0F 84 DB 00 00 00               je 0x1405498c0
005497E5  48 8D 2D 74 FE E2 FF            lea rbp, [rip - 0x1d018c]
005497EC  4C 8B A7 D0 00 00 00            mov r12, qword ptr [rdi + 0xd0]
005497F3  48 8B 9F C8 00 00 00            mov rbx, qword ptr [rdi + 0xc8]
005497FA  48 8B CF                        mov rcx, rdi
005497FD  E8 FE FC CB FF                  call 0x140209500
00549802  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549806  48 8B C8                        mov rcx, rax
00549809  48 3B D5                        cmp rdx, rbp
0054980C  75 07                           jne 0x140549815
0054980E  E8 4D FE E2 FF                  call 0x140379660
00549813  EB 08                           jmp 0x14054981d
00549815  48 8B C2                        mov rax, rdx
00549818  E8 B3 12 17 00                  call 0x1406baad0
0054981D  4C 8B C8                        mov r9, rax
00549820  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00549825  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
0054982C  48 3B D8                        cmp rbx, rax
0054982F  75 C2                           jne 0x1405497f3
00549831  48 8B 8F D0 00 00 00            mov rcx, qword ptr [rdi + 0xd0]
00549838  4C 3B E1                        cmp r12, rcx
0054983B  75 AF                           jne 0x1405497ec
0054983D  44 8B 87 DC 00 00 00            mov r8d, dword ptr [rdi + 0xdc]
00549844  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00549849  41 8D 48 FF                     lea ecx, [r8 - 1]
0054984D  0F B6 D1                        movzx edx, cl
00549850  49 8B C9                        mov rcx, r9
00549853  48 33 CB                        xor rcx, rbx
00549856  48 0F A3 D1                     bt rcx, rdx
0054985A  73 3D                           jae 0x140549899
0054985C  49 83 CE FF                     or r14, 0xffffffffffffffff
00549860  41 8B C8                        mov ecx, r8d
00549863  BE 01 00 00 00                  mov esi, 1
00549868  48 D3 E6                        shl rsi, cl
0054986B  41 83 F8 40                     cmp r8d, 0x40
0054986F  48 8D 4E FF                     lea rcx, [rsi - 1]
00549873  4C 0F 45 F1                     cmovne r14, rcx
00549877  4C 23 F3                        and r14, rbx
0054987A  49 8B CE                        mov rcx, r14
0054987D  48 33 CB                        xor rcx, rbx
00549880  49 0B C9                        or rcx, r9
00549883  4D 3B CE                        cmp r9, r14
00549886  48 8D 14 31                     lea rdx, [rcx + rsi]
0054988A  48 0F 43 D1                     cmovae rdx, rcx
0054988E  F0 48 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [rdi + 0xc8], rdx
00549897  EB 5B                           jmp 0x1405498f4
00549899  41 83 F8 40                     cmp r8d, 0x40
0054989D  75 06                           jne 0x1405498a5
0054989F  48 83 CA FF                     or rdx, 0xffffffffffffffff
005498A3  EB 10                           jmp 0x1405498b5
005498A5  BE 01 00 00 00                  mov esi, 1
005498AA  41 8B C8                        mov ecx, r8d
005498AD  8B D6                           mov edx, esi
005498AF  48 D3 E2                        shl rdx, cl
005498B2  48 2B D6                        sub rdx, rsi
005498B5  48 F7 D2                        not rdx
005498B8  48 23 D3                        and rdx, rbx
005498BB  49 0B D1                        or rdx, r9
005498BE  EB 34                           jmp 0x1405498f4
005498C0  48 8B CF                        mov rcx, rdi
005498C3  E8 38 FC CB FF                  call 0x140209500
005498C8  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
005498CC  4C 8D 25 7D F6 E2 FF            lea r12, [rip - 0x1d0983]
005498D3  48 8B C8                        mov rcx, rax
005498D6  49 3B D4                        cmp rdx, r12
005498D9  75 07                           jne 0x1405498e2
005498DB  E8 70 F6 E2 FF                  call 0x140378f50
005498E0  EB 08                           jmp 0x1405498ea
005498E2  48 8B C2                        mov rax, rdx
005498E5  E8 E6 11 17 00                  call 0x1406baad0
005498EA  4C 8B A7 D0 00 00 00            mov r12, qword ptr [rdi + 0xd0]
005498F1  48 8B D0                        mov rdx, rax
005498F4  4C 8B 1D BD A6 A7 00            mov r11, qword ptr [rip + 0xa7a6bd]
005498FB  49 8D 0C 14                     lea rcx, [r12 + rdx]
005498FF  48 8B 15 CA A6 A7 00            mov rdx, qword ptr [rip + 0xa7a6ca]
00549906  4D 8B 83 C0 00 00 00            mov r8, qword ptr [r11 + 0xc0]
0054990D  48 8B 92 C0 00 00 00            mov rdx, qword ptr [rdx + 0xc0]
00549914  E8 3B 1A E3 FF                  call 0x14037b354
00549919  49 8B 53 10                     mov rdx, qword ptr [r11 + 0x10]
0054991D  48 8B CD                        mov rcx, rbp
00549920  48 3B C2                        cmp rax, rdx
00549923  48 0F 43 D0                     cmovae rdx, rax
00549927  E8 48 1F F6 FF                  call 0x1404ab874
0054992C  85 C0                           test eax, eax
0054992E  79 1E                           jns 0x14054994e
00549930  B9 5C 00 00 00                  mov ecx, 0x5c
00549935  48 98                           cdqe
00549937  4C 8B CD                        mov r9, rbp
0054993A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0054993F  BA 13 01 00 00                  mov edx, 0x113
00549944  44 8D 41 CA                     lea r8d, [rcx - 0x36]
00549948  E8 13 3D FB FF                  call 0x1404fd660
0054994D  CC                              int3
0054994E  48 89 2D 7B A6 A7 00            mov qword ptr [rip + 0xa7a67b], rbp
00549955  4C 89 2D 5C A6 A7 00            mov qword ptr [rip + 0xa7a65c], r13
0054995C  E9 70 04 00 00                  jmp 0x140549dd1
00549961  48 8B 3D 68 A6 A7 00            mov rdi, qword ptr [rip + 0xa7a668]
00549968  48 3B CF                        cmp rcx, rdi
0054996B  0F 85 60 04 00 00               jne 0x140549dd1
00549971  84 D2                           test dl, dl
00549973  0F 85 58 04 00 00               jne 0x140549dd1
00549979  48 8B 05 C0 A7 A7 00            mov rax, qword ptr [rip + 0xa7a7c0]
00549980  48 89 3D 31 A6 A7 00            mov qword ptr [rip + 0xa7a631], rdi
00549987  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0054998C  48 85 C0                        test rax, rax
0054998F  75 1A                           jne 0x1405499ab
00549991  4C 8B C9                        mov r9, rcx
00549994  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00549999  8D 48 5C                        lea ecx, [rax + 0x5c]
0054999C  BA 13 01 00 00                  mov edx, 0x113
005499A1  44 8D 40 22                     lea r8d, [rax + 0x22]
005499A5  E8 B6 3C FB FF                  call 0x1404fd660
005499AA  CC                              int3
005499AB  49 83 CE FF                     or r14, 0xffffffffffffffff
005499AF  4C 8D 25 9A F5 E2 FF            lea r12, [rip - 0x1d0a66]
005499B6  83 BF DC 00 00 00 40            cmp dword ptr [rdi + 0xdc], 0x40
005499BD  BE 01 00 00 00                  mov esi, 1
005499C2  0F 84 D4 00 00 00               je 0x140549a9c
005499C8  4C 8D 25 91 FC E2 FF            lea r12, [rip - 0x1d036f]
005499CF  48 8B AF D0 00 00 00            mov rbp, qword ptr [rdi + 0xd0]
005499D6  48 8B 9F C8 00 00 00            mov rbx, qword ptr [rdi + 0xc8]
005499DD  48 8B CF                        mov rcx, rdi
005499E0  E8 1B FB CB FF                  call 0x140209500
005499E5  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
005499E9  48 8B C8                        mov rcx, rax
005499EC  49 3B D4                        cmp rdx, r12
005499EF  75 07                           jne 0x1405499f8
005499F1  E8 6A FC E2 FF                  call 0x140379660
005499F6  EB 08                           jmp 0x140549a00
005499F8  48 8B C2                        mov rax, rdx
005499FB  E8 D0 10 17 00                  call 0x1406baad0
00549A00  4C 8B D0                        mov r10, rax
00549A03  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00549A08  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
00549A0F  48 3B D8                        cmp rbx, rax
00549A12  75 C2                           jne 0x1405499d6
00549A14  48 8B 8F D0 00 00 00            mov rcx, qword ptr [rdi + 0xd0]
00549A1B  48 3B E9                        cmp rbp, rcx
00549A1E  75 AF                           jne 0x1405499cf
00549A20  44 8B 8F DC 00 00 00            mov r9d, dword ptr [rdi + 0xdc]
00549A27  4C 8D 25 22 F5 E2 FF            lea r12, [rip - 0x1d0ade]
00549A2E  41 8D 49 FF                     lea ecx, [r9 - 1]
00549A32  0F B6 D1                        movzx edx, cl
00549A35  49 8B CA                        mov rcx, r10
00549A38  48 33 CB                        xor rcx, rbx
00549A3B  48 0F A3 D1                     bt rcx, rdx
00549A3F  73 39                           jae 0x140549a7a
00549A41  41 8B C9                        mov ecx, r9d
00549A44  48 8B D6                        mov rdx, rsi
00549A47  48 D3 E2                        shl rdx, cl
00549A4A  4D 8B C6                        mov r8, r14
00549A4D  41 83 F9 40                     cmp r9d, 0x40
00549A51  48 8D 4A FF                     lea rcx, [rdx - 1]
00549A55  4C 0F 45 C1                     cmovne r8, rcx
00549A59  4C 23 C3                        and r8, rbx
00549A5C  49 8B C8                        mov rcx, r8
00549A5F  48 33 CB                        xor rcx, rbx
00549A62  49 0B CA                        or rcx, r10
00549A65  48 03 D1                        add rdx, rcx
00549A68  4D 3B D0                        cmp r10, r8
00549A6B  48 0F 43 D1                     cmovae rdx, rcx
00549A6F  F0 48 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [rdi + 0xc8], rdx
00549A78  EB 4F                           jmp 0x140549ac9
00549A7A  41 83 F9 40                     cmp r9d, 0x40
00549A7E  75 05                           jne 0x140549a85
00549A80  49 8B D6                        mov rdx, r14
00549A83  EB 0C                           jmp 0x140549a91
00549A85  41 8B C9                        mov ecx, r9d
00549A88  48 8B D6                        mov rdx, rsi
00549A8B  48 D3 E2                        shl rdx, cl
00549A8E  48 2B D6                        sub rdx, rsi
00549A91  48 F7 D2                        not rdx
00549A94  48 23 D3                        and rdx, rbx
00549A97  49 0B D2                        or rdx, r10
00549A9A  EB 2D                           jmp 0x140549ac9
00549A9C  48 8B CF                        mov rcx, rdi
00549A9F  E8 5C FA CB FF                  call 0x140209500
00549AA4  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549AA8  48 8B C8                        mov rcx, rax
00549AAB  49 3B D4                        cmp rdx, r12
00549AAE  75 07                           jne 0x140549ab7
00549AB0  E8 9B F4 E2 FF                  call 0x140378f50
00549AB5  EB 08                           jmp 0x140549abf
00549AB7  48 8B C2                        mov rax, rdx
00549ABA  E8 11 10 17 00                  call 0x1406baad0
00549ABF  48 8B AF D0 00 00 00            mov rbp, qword ptr [rdi + 0xd0]
00549AC6  48 8B D0                        mov rdx, rax
00549AC9  48 8B 05 00 A5 A7 00            mov rax, qword ptr [rip + 0xa7a500]
00549AD0  4C 8D 2C 2A                     lea r13, [rdx + rbp]
00549AD4  48 8B 3D 65 A6 A7 00            mov rdi, qword ptr [rip + 0xa7a665]
00549ADB  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00549AE0  4C 89 68 10                     mov qword ptr [rax + 0x10], r13
00549AE4  83 BF DC 00 00 00 40            cmp dword ptr [rdi + 0xdc], 0x40
00549AEB  0F 84 D2 00 00 00               je 0x140549bc3
00549AF1  4C 8D 2D 68 FB E2 FF            lea r13, [rip - 0x1d0498]
00549AF8  48 8B AF D0 00 00 00            mov rbp, qword ptr [rdi + 0xd0]
00549AFF  48 8B 9F C8 00 00 00            mov rbx, qword ptr [rdi + 0xc8]
00549B06  48 8B CF                        mov rcx, rdi
00549B09  E8 F2 F9 CB FF                  call 0x140209500
00549B0E  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549B12  48 8B C8                        mov rcx, rax
00549B15  49 3B D5                        cmp rdx, r13
00549B18  75 07                           jne 0x140549b21
00549B1A  E8 41 FB E2 FF                  call 0x140379660
00549B1F  EB 08                           jmp 0x140549b29
00549B21  48 8B C2                        mov rax, rdx
00549B24  E8 A7 0F 17 00                  call 0x1406baad0
00549B29  4C 8B D0                        mov r10, rax
00549B2C  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00549B31  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
00549B38  48 3B D8                        cmp rbx, rax
00549B3B  75 C2                           jne 0x140549aff
00549B3D  48 8B 8F D0 00 00 00            mov rcx, qword ptr [rdi + 0xd0]
00549B44  48 3B E9                        cmp rbp, rcx
00549B47  75 AF                           jne 0x140549af8
00549B49  44 8B 8F DC 00 00 00            mov r9d, dword ptr [rdi + 0xdc]
00549B50  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00549B55  41 8D 49 FF                     lea ecx, [r9 - 1]
00549B59  0F B6 D1                        movzx edx, cl
00549B5C  49 8B CA                        mov rcx, r10
00549B5F  48 33 CB                        xor rcx, rbx
00549B62  48 0F A3 D1                     bt rcx, rdx
00549B66  73 39                           jae 0x140549ba1
00549B68  41 8B C9                        mov ecx, r9d
00549B6B  48 8B D6                        mov rdx, rsi
00549B6E  48 D3 E2                        shl rdx, cl
00549B71  4D 8B C6                        mov r8, r14
00549B74  41 83 F9 40                     cmp r9d, 0x40
00549B78  48 8D 4A FF                     lea rcx, [rdx - 1]
00549B7C  4C 0F 45 C1                     cmovne r8, rcx
00549B80  4C 23 C3                        and r8, rbx
00549B83  49 8B C8                        mov rcx, r8
00549B86  48 33 CB                        xor rcx, rbx
00549B89  49 0B CA                        or rcx, r10
00549B8C  48 03 D1                        add rdx, rcx
00549B8F  4D 3B D0                        cmp r10, r8
00549B92  48 0F 43 D1                     cmovae rdx, rcx
00549B96  F0 48 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [rdi + 0xc8], rdx
00549B9F  EB 4F                           jmp 0x140549bf0
00549BA1  41 83 F9 40                     cmp r9d, 0x40
00549BA5  75 05                           jne 0x140549bac
00549BA7  49 8B D6                        mov rdx, r14
00549BAA  EB 0C                           jmp 0x140549bb8
00549BAC  41 8B C9                        mov ecx, r9d
00549BAF  48 8B D6                        mov rdx, rsi
00549BB2  48 D3 E2                        shl rdx, cl
00549BB5  48 2B D6                        sub rdx, rsi
00549BB8  48 F7 D2                        not rdx
00549BBB  48 23 D3                        and rdx, rbx
00549BBE  49 0B D2                        or rdx, r10
00549BC1  EB 2D                           jmp 0x140549bf0
00549BC3  48 8B CF                        mov rcx, rdi
00549BC6  E8 35 F9 CB FF                  call 0x140209500
00549BCB  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549BCF  48 8B C8                        mov rcx, rax
00549BD2  49 3B D4                        cmp rdx, r12
00549BD5  75 07                           jne 0x140549bde
00549BD7  E8 74 F3 E2 FF                  call 0x140378f50
00549BDC  EB 08                           jmp 0x140549be6
00549BDE  48 8B C2                        mov rax, rdx
00549BE1  E8 EA 0E 17 00                  call 0x1406baad0
00549BE6  48 8B AF D0 00 00 00            mov rbp, qword ptr [rdi + 0xd0]
00549BED  48 8B D0                        mov rdx, rax
00549BF0  48 8B 3D D9 A3 A7 00            mov rdi, qword ptr [rip + 0xa7a3d9]
00549BF7  48 8D 0C 2A                     lea rcx, [rdx + rbp]
00549BFB  48 8B 15 3E A5 A7 00            mov rdx, qword ptr [rip + 0xa7a53e]
00549C02  4C 8B 87 C0 00 00 00            mov r8, qword ptr [rdi + 0xc0]
00549C09  48 8B 92 C0 00 00 00            mov rdx, qword ptr [rdx + 0xc0]
00549C10  E8 3F 17 E3 FF                  call 0x14037b354
00549C15  48 8B D0                        mov rdx, rax
00549C18  49 8B CD                        mov rcx, r13
00549C1B  49 2B D5                        sub rdx, r13
00549C1E  48 2B C8                        sub rcx, rax
00549C21  4C 3B E8                        cmp r13, rax
00549C24  48 0F 46 CA                     cmovbe rcx, rdx
00549C28  48 3B 0D A1 A4 A7 00            cmp rcx, qword ptr [rip + 0xa7a4a1]
00549C2F  0F 86 65 01 00 00               jbe 0x140549d9a
00549C35  01 35 15 67 8C 00               add dword ptr [rip + 0x8c6715], esi
00549C3B  83 BF DC 00 00 00 40            cmp dword ptr [rdi + 0xdc], 0x40
00549C42  0F 84 CF 00 00 00               je 0x140549d17
00549C48  4C 8D 35 11 FA E2 FF            lea r14, [rip - 0x1d05ef]
00549C4F  4C 8B A7 D0 00 00 00            mov r12, qword ptr [rdi + 0xd0]
00549C56  48 8B 9F C8 00 00 00            mov rbx, qword ptr [rdi + 0xc8]
00549C5D  48 8B CF                        mov rcx, rdi
00549C60  E8 9B F8 CB FF                  call 0x140209500
00549C65  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549C69  48 8B C8                        mov rcx, rax
00549C6C  49 3B D6                        cmp rdx, r14
00549C6F  75 07                           jne 0x140549c78
00549C71  E8 EA F9 E2 FF                  call 0x140379660
00549C76  EB 08                           jmp 0x140549c80
00549C78  48 8B C2                        mov rax, rdx
00549C7B  E8 50 0E 17 00                  call 0x1406baad0
00549C80  4C 8B C8                        mov r9, rax
00549C83  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00549C88  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
00549C8F  48 3B D8                        cmp rbx, rax
00549C92  75 C2                           jne 0x140549c56
00549C94  48 8B 8F D0 00 00 00            mov rcx, qword ptr [rdi + 0xd0]
00549C9B  4C 3B E1                        cmp r12, rcx
00549C9E  75 AF                           jne 0x140549c4f
00549CA0  44 8B 87 DC 00 00 00            mov r8d, dword ptr [rdi + 0xdc]
00549CA7  49 C7 C6 FF FF FF FF            mov r14, 0xffffffffffffffff
00549CAE  41 8D 48 FF                     lea ecx, [r8 - 1]
00549CB2  0F B6 D1                        movzx edx, cl
00549CB5  49 8B C9                        mov rcx, r9
00549CB8  48 33 CB                        xor rcx, rbx
00549CBB  48 0F A3 D1                     bt rcx, rdx
00549CBF  73 34                           jae 0x140549cf5
00549CC1  41 8B C8                        mov ecx, r8d
00549CC4  48 D3 E6                        shl rsi, cl
00549CC7  41 83 F8 40                     cmp r8d, 0x40
00549CCB  48 8D 4E FF                     lea rcx, [rsi - 1]
00549CCF  4C 0F 45 F1                     cmovne r14, rcx
00549CD3  4C 23 F3                        and r14, rbx
00549CD6  49 8B CE                        mov rcx, r14
00549CD9  48 33 CB                        xor rcx, rbx
00549CDC  49 0B C9                        or rcx, r9
00549CDF  4D 3B CE                        cmp r9, r14
00549CE2  48 8D 14 31                     lea rdx, [rcx + rsi]
00549CE6  48 0F 43 D1                     cmovae rdx, rcx
00549CEA  F0 48 0F B1 97 C8 00 00 00      lock cmpxchg qword ptr [rdi + 0xc8], rdx
00549CF3  EB 4F                           jmp 0x140549d44
00549CF5  41 83 F8 40                     cmp r8d, 0x40
00549CF9  75 05                           jne 0x140549d00
00549CFB  49 8B D6                        mov rdx, r14
00549CFE  EB 0C                           jmp 0x140549d0c
00549D00  41 8B C8                        mov ecx, r8d
00549D03  48 8B D6                        mov rdx, rsi
00549D06  48 D3 E2                        shl rdx, cl
00549D09  48 2B D6                        sub rdx, rsi
00549D0C  48 F7 D2                        not rdx
00549D0F  48 23 D3                        and rdx, rbx
00549D12  49 0B D1                        or rdx, r9
00549D15  EB 2D                           jmp 0x140549d44
00549D17  48 8B CF                        mov rcx, rdi
00549D1A  E8 E1 F7 CB FF                  call 0x140209500
00549D1F  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
00549D23  48 8B C8                        mov rcx, rax
00549D26  49 3B D4                        cmp rdx, r12
00549D29  75 07                           jne 0x140549d32
00549D2B  E8 20 F2 E2 FF                  call 0x140378f50
00549D30  EB 08                           jmp 0x140549d3a
00549D32  48 8B C2                        mov rax, rdx
00549D35  E8 96 0D 17 00                  call 0x1406baad0
00549D3A  4C 8B A7 D0 00 00 00            mov r12, qword ptr [rdi + 0xd0]
00549D41  48 8B D0                        mov rdx, rax
00549D44  4C 8B 1D F5 A3 A7 00            mov r11, qword ptr [rip + 0xa7a3f5]
00549D4B  49 8D 0C 14                     lea rcx, [r12 + rdx]
00549D4F  48 8B 15 7A A2 A7 00            mov rdx, qword ptr [rip + 0xa7a27a]
00549D56  4D 8B 83 C0 00 00 00            mov r8, qword ptr [r11 + 0xc0]
00549D5D  48 8B 92 C0 00 00 00            mov rdx, qword ptr [rdx + 0xc0]
00549D64  E8 EB 15 E3 FF                  call 0x14037b354
00549D69  48 8B D0                        mov rdx, rax
00549D6C  49 8B CB                        mov rcx, r11
00549D6F  E8 00 1B F6 FF                  call 0x1404ab874
00549D74  85 C0                           test eax, eax
00549D76  79 22                           jns 0x140549d9a
00549D78  4C 8B 0D C1 A3 A7 00            mov r9, qword ptr [rip + 0xa7a3c1]
00549D7F  B9 5C 00 00 00                  mov ecx, 0x5c
00549D84  48 98                           cdqe
00549D86  BA 13 01 00 00                  mov edx, 0x113
00549D8B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00549D90  44 8D 41 CA                     lea r8d, [rcx - 0x36]
00549D94  E8 C7 38 FB FF                  call 0x1404fd660
00549D99  CC                              int3
00549D9A  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00549D9F  48 8B 41 70                     mov rax, qword ptr [rcx + 0x70]
00549DA3  48 89 05 9E 65 8C 00            mov qword ptr [rip + 0x8c659e], rax
00549DAA  48 8D 05 6F F1 FF FF            lea rax, [rip - 0xe91]
00549DB1  48 89 41 70                     mov qword ptr [rcx + 0x70], rax
00549DB5  48 8B 05 14 A2 A7 00            mov rax, qword ptr [rip + 0xa7a214]
00549DBC  48 89 05 F5 A1 A7 00            mov qword ptr [rip + 0xa7a1f5], rax
00549DC3  48 8B 05 76 A3 A7 00            mov rax, qword ptr [rip + 0xa7a376]
00549DCA  48 89 05 FF A1 A7 00            mov qword ptr [rip + 0xa7a1ff], rax
00549DD1  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00549DD6  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00549DDB  48 83 C4 30                     add rsp, 0x30
00549DDF  41 5E                           pop r14
00549DE1  41 5D                           pop r13
00549DE3  41 5C                           pop r12
00549DE5  5F                              pop rdi
00549DE6  5E                              pop rsi
00549DE7  C3                              ret
00549DE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerPerformanceCounterPowerChange(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (48);
    v_r13 = 0;
    v_stack_p18 = *(unsigned __int64 *)(v_rip + 10987619);
    if (*(unsigned __int64 *)(v_rip + 10987619) == 0) goto loc_00549961;
    if (a1 != (*(unsigned __int64 *)(v_rip + 10987619))) goto loc_00549DD1;
    if (a2 == 0) goto loc_00549DD1;
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987619), a2, a3, a4);
    result = guard_dispatch_icall(result, a2, a3, a4);
    if (sign_flag) {
        a1 = v_r13 + 92;
        a4 = *(unsigned __int64 *)(v_rip + 10987619);
        v_stack_m38 = result;
        a2 = 275;
        a3 = v_r13 + 15;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = *(unsigned __int64 *)(v_rip + 9202581);
    if (*(unsigned __int64 *)(v_rip + 9202581) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 9202569);
        result = *(unsigned __int64 *)(v_rip + 10987530);
        *(unsigned __int64 *)(result + 112) = a1;
        *(unsigned __int64 *)(v_rip + 9202551) = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)) == 64) goto loc_005498C0;
loc_005497EC:
loc_005497F3:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987512), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112)) != (v_rip - 1900940)) goto loc_00549815;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112), a3, a4);
    goto loc_0054981D;
loc_00549815:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112), a3, a4);
loc_0054981D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200))) goto loc_005497F3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 208)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 208))) goto loc_005497EC;
    a1 = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200));
    if (condition_is_above_or_equal) goto loc_00549899;
    v_r14 = (v_r14) | (-1);
    v_rsi = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220))))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)))) != 64) { v_r14 = v_rsi - 1; }
    v_r14 = (v_r14) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200));
    a1 = (v_r14) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200));
    a1 = (a1) | (result);
    a2 = a1 + v_rsi * 1;
    if (result >= v_r14) { a2 = a1; }
    goto loc_005498F4;
loc_00549899:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)))) != 64) goto loc_005498A5;
    a2 = (a2) | (-1);
    goto loc_005498B5;
loc_005498A5:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220))))));
    a2 = (a2) - (1);
loc_005498B5:
    a2 = ~(a2);
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 200));
    a2 = (a2) | (result);
    goto loc_005498F4;
loc_005498C0:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987512), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)), result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112)) != (v_rip - 1902979)) goto loc_005498E2;
    result = HalpHvCounterQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)), result);
    goto loc_005498EA;
loc_005498E2:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 112), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987512) + 220)), result);
loc_005498EA:
loc_005498F4:
    result = HalpTimerScaleCounter(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987512) + 208) + result * 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987210) + 192), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987197) + 192), result);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987197) + 16);
    if (result >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987197) + 16))) { a2 = result; }
    result = HalpTimerCalibratePerformanceCounter(v_stack_p18, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987197) + 192), result);
    if (sign_flag) {
        a1 = 92;
        a4 = v_stack_p18;
        v_stack_m38 = result;
        a2 = 275;
        a3 = a1 - 54;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 10987131) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 10987100) = 0;
    goto loc_00549DD1;
loc_00549961:
    if (a1 != (*(unsigned __int64 *)(v_rip + 10987112))) goto loc_00549DD1;
    if (a2 != 0) goto loc_00549DD1;
    *(unsigned __int64 *)(v_rip + 10987057) = *(unsigned __int64 *)(v_rip + 10987112);
    v_stack_p20 = *(unsigned __int64 *)(v_rip + 10987456);
    result = *(unsigned __int64 *)(v_rip + 10987456);
    if (*(unsigned __int64 *)(v_rip + 10987456) == 0) {
        a4 = a1;
        v_stack_m38 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 10987456) + 92;
        a2 = 275;
        a3 = *(unsigned __int64 *)(v_rip + 10987456) + 34;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_r14 = (v_r14) | (-1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)) == 64) goto loc_00549A9C;
loc_005499CF:
loc_005499D6:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987112), a2, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112)) != (v_rip - 1901423)) goto loc_005499F8;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112), a3, a4);
    goto loc_00549A00;
loc_005499F8:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112), a3, a4);
loc_00549A00:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200))) goto loc_005499D6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 208)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 208))) goto loc_005499CF;
    a1 = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200));
    if (condition_is_above_or_equal) goto loc_00549A7A;
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220))))));
    a3 = v_r14;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)))) != 64) { a3 = a2 - 1; }
    a3 = (a3) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200));
    a1 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200));
    a1 = (a1) | (result);
    a2 = (a2) + (a1);
    if (result >= a3) { a2 = a1; }
    goto loc_00549AC9;
loc_00549A7A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)))) != 64) goto loc_00549A85;
    goto loc_00549A91;
loc_00549A85:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220))))));
    a2 = (a2) - (1);
loc_00549A91:
    a2 = ~(a2);
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 200));
    a2 = (a2) | (result);
    goto loc_00549AC9;
loc_00549A9C:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987112), a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112)) != (v_rip - 1903326)) goto loc_00549AB7;
    result = HalpHvCounterQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
    goto loc_00549ABF;
loc_00549AB7:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
loc_00549ABF:
loc_00549AC9:
    v_stack_p18 = result + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 208) * 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986752) + 16) = result + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987112) + 208) * 1;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)) == 64) goto loc_00549BC3;
loc_00549AF8:
loc_00549AFF:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987109), result, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112)) != (v_rip - 1901720)) goto loc_00549B21;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
    goto loc_00549B29;
loc_00549B21:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987112) + 220)));
loc_00549B29:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200))) goto loc_00549AFF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 208)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 208))) goto loc_00549AF8;
    a1 = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200));
    if (condition_is_above_or_equal) goto loc_00549BA1;
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220))))));
    a3 = v_r14;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)))) != 64) { a3 = a2 - 1; }
    a3 = (a3) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200));
    a1 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200));
    a1 = (a1) | (result);
    a2 = (a2) + (a1);
    if (result >= a3) { a2 = a1; }
    goto loc_00549BF0;
loc_00549BA1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)))) != 64) goto loc_00549BAC;
    goto loc_00549BB8;
loc_00549BAC:
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220))))));
    a2 = (a2) - (1);
loc_00549BB8:
    a2 = ~(a2);
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 200));
    a2 = (a2) | (result);
    goto loc_00549BF0;
loc_00549BC3:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10987109), a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112)) != (v_rip - 1903326)) goto loc_00549BDE;
    result = HalpHvCounterQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
    goto loc_00549BE6;
loc_00549BDE:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 112), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
loc_00549BE6:
loc_00549BF0:
    result = HalpTimerScaleCounter(result + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10987109) + 208) * 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986814) + 192), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
    a2 = (result) - (v_stack_p18);
    a1 = (v_stack_p18) - (result);
    if (v_stack_p18 <= result) { a1 = a2; }
    if (a1 <= (*(unsigned __int64 *)(v_rip + 10986657))) goto loc_00549D9A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)) == 64) goto loc_00549D17;
loc_00549C4F:
loc_00549C56:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10986457), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112)) != (v_rip - 1902063)) goto loc_00549C78;
    result = HalpHpetQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
    goto loc_00549C80;
loc_00549C78:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 192), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10987109) + 220)));
loc_00549C80:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200))) goto loc_00549C56;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 208)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 208))) goto loc_00549C4F;
    a1 = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200));
    if (condition_is_above_or_equal) goto loc_00549CF5;
    v_rsi = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220))))));
    v_r14 = -1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)))) != 64) { v_r14 = v_rsi - 1; }
    v_r14 = (v_r14) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200));
    a1 = (v_r14) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200));
    a1 = (a1) | (result);
    a2 = a1 + v_rsi * 1;
    if (result >= v_r14) { a2 = a1; }
    goto loc_00549D44;
loc_00549CF5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)))) != 64) goto loc_00549D00;
    goto loc_00549D0C;
loc_00549D00:
    a2 = (v_rsi) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220))))));
    a2 = (a2) - (v_rsi);
loc_00549D0C:
    a2 = ~(a2);
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 200));
    a2 = (a2) | (result);
    goto loc_00549D44;
loc_00549D17:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 10986457), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)), result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 208))) goto loc_00549D32;
    result = HalpHvCounterQueryCounter(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)), result);
    goto loc_00549D3A;
loc_00549D32:
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 112), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10986457) + 220)), result);
loc_00549D3A:
loc_00549D44:
    result = HalpTimerScaleCounter(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986457) + 208) + result * 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986106) + 192), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986485) + 192), result);
    result = HalpTimerCalibratePerformanceCounter(*(unsigned __int64 *)(v_rip + 10986485), result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10986485) + 192), result);
    if (sign_flag) {
        a4 = *(unsigned __int64 *)(v_rip + 10986433);
        a1 = 92;
        a2 = 275;
        v_stack_m38 = result;
        a3 = a1 - 54;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 9201054) = *(unsigned __int64 *)(v_stack_p20 + 112);
    *(unsigned __int64 *)(v_stack_p20 + 112) = v_rip - 3729;
    *(unsigned __int64 *)(v_rip + 10985973) = *(unsigned __int64 *)(v_rip + 10986004);
    *(unsigned __int64 *)(v_rip + 10985983) = *(unsigned __int64 *)(v_rip + 10986358);
loc_00549DD1:
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(v_rip + 10986358);
}
```

## 5. (Beta) C Style

```c
int64_t HalpTimerPerformanceCounterPowerChange(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (48);
    local_r13 = 0;
    v_stack_p18 = *(uint64_t *)(v_rip + 0xA7A863);
    if (*(uint64_t *)(v_rip + 0xA7A863) == 0) goto loc_00549961;
    if (Arg1 != (*(uint64_t *)(v_rip + 0xA7A863))) goto loc_00549DD1;
    if (Arg2 == 0) goto loc_00549DD1;
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A863), Arg2, a3, a4);
    result = guard_dispatch_icall(result, Arg2, a3, a4);
    if (sign_flag) {
        Arg1 = local_r13 + 92;
        a4 = *(uint64_t *)(v_rip + 0xA7A863);
        v_stack_m38 = result;
        Arg2 = 275;
        a3 = local_r13 + 15;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = *(uint64_t *)(v_rip + 0x8C6B95);
    if (*(uint64_t *)(v_rip + 0x8C6B95) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x8C6B89);
        result = *(uint64_t *)(v_rip + 0xA7A80A);
        *(uint64_t *)(result + 0x70) = Arg1;
        *(uint64_t *)(v_rip + 0x8C6B77) = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)) == 64) goto loc_005498C0;
loc_005497EC:
loc_005497F3:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A7F8), Arg2, a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70)) != (v_rip - 1900940)) goto loc_00549815;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70), a3, a4);
    goto loc_0054981D;
loc_00549815:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70), a3, a4);
loc_0054981D:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8))) goto loc_005497F3;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xD0)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xD0))) goto loc_005497EC;
    Arg1 = (result) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8));
    if (condition_is_above_or_equal) goto loc_00549899;
    local_r14 = (local_r14) | (-1);
    local_rsi = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC))))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)))) != 64) { local_r14 = local_rsi - 1; }
    local_r14 = (local_r14) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8));
    Arg1 = (local_r14) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8));
    Arg1 = (Arg1) | (result);
    Arg2 = Arg1 + local_rsi * 1;
    if (result >= local_r14) { Arg2 = Arg1; }
    goto loc_005498F4;
loc_00549899:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)))) != 64) goto loc_005498A5;
    Arg2 = (Arg2) | (-1);
    goto loc_005498B5;
loc_005498A5:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC))))));
    Arg2 = (Arg2) - (1);
loc_005498B5:
    Arg2 = ~(Arg2);
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_005498F4;
loc_005498C0:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A7F8), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)), result);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70)) != (v_rip - 1902979)) goto loc_005498E2;
    result = HalpHvCounterQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)), result);
    goto loc_005498EA;
loc_005498E2:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0x70), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xDC)), result);
loc_005498EA:
loc_005498F4:
    result = HalpTimerScaleCounter(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A7F8) + 0xD0) + result * 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A6CA) + 0xC0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A6BD) + 0xC0), result);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A6BD) + 0x10);
    if (result >= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A6BD) + 0x10))) { Arg2 = result; }
    result = HalpTimerCalibratePerformanceCounter(v_stack_p18, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A6BD) + 0xC0), result);
    if (sign_flag) {
        Arg1 = 92;
        a4 = v_stack_p18;
        v_stack_m38 = result;
        Arg2 = 275;
        a3 = Arg1 - 54;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(v_rip + 0xA7A67B) = v_stack_p18;
    *(uint64_t *)(v_rip + 0xA7A65C) = 0;
    goto loc_00549DD1;
loc_00549961:
    if (Arg1 != (*(uint64_t *)(v_rip + 0xA7A668))) goto loc_00549DD1;
    if (Arg2 != 0) goto loc_00549DD1;
    *(uint64_t *)(v_rip + 0xA7A631) = *(uint64_t *)(v_rip + 0xA7A668);
    v_stack_p20 = *(uint64_t *)(v_rip + 0xA7A7C0);
    result = *(uint64_t *)(v_rip + 0xA7A7C0);
    if (*(uint64_t *)(v_rip + 0xA7A7C0) == 0) {
        a4 = Arg1;
        v_stack_m38 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0xA7A7C0) + 92;
        Arg2 = 275;
        a3 = *(uint64_t *)(v_rip + 0xA7A7C0) + 34;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    local_r14 = (local_r14) | (-1);
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)) == 64) goto loc_00549A9C;
loc_005499CF:
loc_005499D6:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A668), Arg2, a3, a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70)) != (v_rip - 1901423)) goto loc_005499F8;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70), a3, a4);
    goto loc_00549A00;
loc_005499F8:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70), a3, a4);
loc_00549A00:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8))) goto loc_005499D6;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xD0)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xD0))) goto loc_005499CF;
    Arg1 = (result) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8));
    if (condition_is_above_or_equal) goto loc_00549A7A;
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC))))));
    a3 = local_r14;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)))) != 64) { a3 = Arg2 - 1; }
    a3 = (a3) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8));
    Arg1 = (a3) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8));
    Arg1 = (Arg1) | (result);
    Arg2 = (Arg2) + (Arg1);
    if (result >= a3) { Arg2 = Arg1; }
    goto loc_00549AC9;
loc_00549A7A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)))) != 64) goto loc_00549A85;
    goto loc_00549A91;
loc_00549A85:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC))))));
    Arg2 = (Arg2) - (1);
loc_00549A91:
    Arg2 = ~(Arg2);
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_00549AC9;
loc_00549A9C:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A668), Arg2, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70)) != (v_rip - 1903326)) goto loc_00549AB7;
    result = HalpHvCounterQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
    goto loc_00549ABF;
loc_00549AB7:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
loc_00549ABF:
loc_00549AC9:
    v_stack_p18 = result + *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xD0) * 1;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A500) + 0x10) = result + *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xD0) * 1;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)) == 64) goto loc_00549BC3;
loc_00549AF8:
loc_00549AFF:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A665), result, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70)) != (v_rip - 1901720)) goto loc_00549B21;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
    goto loc_00549B29;
loc_00549B21:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A668) + 0xDC)));
loc_00549B29:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8))) goto loc_00549AFF;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xD0)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xD0))) goto loc_00549AF8;
    Arg1 = (result) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8));
    if (condition_is_above_or_equal) goto loc_00549BA1;
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC))))));
    a3 = local_r14;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)))) != 64) { a3 = Arg2 - 1; }
    a3 = (a3) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8));
    Arg1 = (a3) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8));
    Arg1 = (Arg1) | (result);
    Arg2 = (Arg2) + (Arg1);
    if (result >= a3) { Arg2 = Arg1; }
    goto loc_00549BF0;
loc_00549BA1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)))) != 64) goto loc_00549BAC;
    goto loc_00549BB8;
loc_00549BAC:
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC))))));
    Arg2 = (Arg2) - (1);
loc_00549BB8:
    Arg2 = ~(Arg2);
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_00549BF0;
loc_00549BC3:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A665), Arg2, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70)) != (v_rip - 1903326)) goto loc_00549BDE;
    result = HalpHvCounterQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
    goto loc_00549BE6;
loc_00549BDE:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0x70), a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
loc_00549BE6:
loc_00549BF0:
    result = HalpTimerScaleCounter(result + *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xD0) * 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A53E) + 0xC0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
    Arg2 = (result) - (v_stack_p18);
    Arg1 = (v_stack_p18) - (result);
    if (v_stack_p18 <= result) { Arg1 = Arg2; }
    if (Arg1 <= (*(uint64_t *)(v_rip + 0xA7A4A1))) goto loc_00549D9A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)) == 64) goto loc_00549D17;
loc_00549C4F:
loc_00549C56:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A3D9), Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70)) != (v_rip - 1902063)) goto loc_00549C78;
    result = HalpHpetQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70), *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
    goto loc_00549C80;
loc_00549C78:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70), *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC0), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A665) + 0xDC)));
loc_00549C80:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8))) goto loc_00549C56;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xD0)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xD0))) goto loc_00549C4F;
    Arg1 = (result) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8));
    if (condition_is_above_or_equal) goto loc_00549CF5;
    local_rsi = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC))))));
    local_r14 = -1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)))) != 64) { local_r14 = local_rsi - 1; }
    local_r14 = (local_r14) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8));
    Arg1 = (local_r14) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8));
    Arg1 = (Arg1) | (result);
    Arg2 = Arg1 + local_rsi * 1;
    if (result >= local_r14) { Arg2 = Arg1; }
    goto loc_00549D44;
loc_00549CF5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)))) != 64) goto loc_00549D00;
    goto loc_00549D0C;
loc_00549D00:
    Arg2 = (local_rsi) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC))))));
    Arg2 = (Arg2) - (local_rsi);
loc_00549D0C:
    Arg2 = ~(Arg2);
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xC8));
    Arg2 = (Arg2) | (result);
    goto loc_00549D44;
loc_00549D17:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xA7A3D9), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)), result);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xD0))) goto loc_00549D32;
    result = HalpHvCounterQueryCounter(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)), result);
    goto loc_00549D3A;
loc_00549D32:
    result = guard_dispatch_icall(result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0x70), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xDC)), result);
loc_00549D3A:
loc_00549D44:
    result = HalpTimerScaleCounter(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3D9) + 0xD0) + result * 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A27A) + 0xC0), *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3F5) + 0xC0), result);
    result = HalpTimerCalibratePerformanceCounter(*(uint64_t *)(v_rip + 0xA7A3F5), result, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7A3F5) + 0xC0), result);
    if (sign_flag) {
        a4 = *(uint64_t *)(v_rip + 0xA7A3C1);
        Arg1 = 92;
        Arg2 = 275;
        v_stack_m38 = result;
        a3 = Arg1 - 54;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(v_rip + 0x8C659E) = *(uint64_t *)(v_stack_p20 + 0x70);
    *(uint64_t *)(v_stack_p20 + 0x70) = v_rip - 3729;
    *(uint64_t *)(v_rip + 0xA7A1F5) = *(uint64_t *)(v_rip + 0xA7A214);
    *(uint64_t *)(v_rip + 0xA7A1FF) = *(uint64_t *)(v_rip + 0xA7A376);
loc_00549DD1:
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(v_rip + 0xA7A376);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00549738&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
