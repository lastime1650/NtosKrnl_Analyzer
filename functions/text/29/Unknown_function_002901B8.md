# sub_002901B8

- RVA: `0x002901B8`–`0x0029061D` (길이 `1,125` bytes)
- VA: `0x00000001402901B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067408`
- 디코드: `259`개 명령, `1,125/1,125` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00290206` → [MiAcquirePrcbAgeTrimLists](MiAcquirePrcbAgeTrimLists_function_002918B0.md) (function, `0x002918B0`)
- `0x002902FF` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002903C3` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002904CE` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x002904FD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0029050C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00290591` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00290599` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x002905FA` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002902B2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00290354` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00290397` → RVA `0x00E35C00` (`.data`; read)
- `0x002904EF` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00290584` → RVA `0x00695890` (`MiTbFlushSort`; read)
- `0x002905CB` → RVA `0x01011694` (`INITDATA`; write)
- `0x002905D5` → RVA `0x0100F4C0` (`INITDATA`; read)
- `0x002905DC` → RVA `0x0100F620` (`INITDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x002901C4` → [sub_0028FBD9 + 0x6F](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002901DE` → [sub_0028FBD9 + 0x6F](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002901EC` → [sub_0028FBD9 + 0x6F](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002902C7` → [sub_0028FBD9 + 0x156](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002902DF` → [sub_0028FBD9 + 0x8F](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x00290333` → [sub_0028FBD9 + 0xED](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x00290343` → [sub_0028FDDD + 0x286](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x0029034E` → [sub_0028FDDD + 0xDD](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x00290376` → [sub_0028FDDD + 0xDD](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002903AD` → [sub_0028FDDD + 0xDD](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002903BA` → [sub_0028FBD9 + 0x140](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002903CB` → [sub_0028FDDD + 0xDD](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002903D1` → [sub_0028FBD9 + 0x140](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002903E4` → [sub_0028FDDD + 0x28A](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x00290498` → [sub_0028FDDD + 0x1F](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002904BF` → [sub_0028FBD9 + 0xFF](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002904D3` → [sub_0028FBD9 + 0xFF](../28/Unknown_function_0028FBD9.md) (`tail-transfer`)
  - `0x002904DF` → [sub_0028FDDD + 0x1EF](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002904EA` → [sub_0028FDDD + 0x262](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)
  - `0x002905E3` → [sub_0028FDDD + 0x118](../28/Unknown_function_0028FDDD.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002901B8  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002901BC  48 C1 E8 3C                     shr rax, 0x3c
002901C0  22 C1                           and al, cl
002901C2  3C 04                           cmp al, 4
002901C4  0F 85 7E FA FF FF               jne 0x14028fc48
002901CA  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002901CE  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
002901D8  48 23 C1                        and rax, rcx
002901DB  49 3B C4                        cmp rax, r12
002901DE  0F 85 64 FA FF FF               jne 0x14028fc48
002901E4  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002901E8  66 41 3B C4                     cmp ax, r12w
002901EC  0F 85 56 FA FF FF               jne 0x14028fc48
002901F2  48 FF 47 20                     inc qword ptr [rdi + 0x20]
002901F6  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
002901FA  4D 85 F6                        test r14, r14
002901FD  75 10                           jne 0x14029020f
002901FF  48 8D 57 38                     lea rdx, [rdi + 0x38]
00290203  48 8B CE                        mov rcx, rsi
00290206  E8 A5 16 00 00                  call 0x1402918b0
0029020B  4C 8B 77 40                     mov r14, qword ptr [rdi + 0x40]
0029020F  49 8B FC                        mov rdi, r12
00290212  45 39 66 08                     cmp dword ptr [r14 + 8], r12d
00290216  0F 85 FA 02 00 00               jne 0x140290516
0029021C  33 DB                           xor ebx, ebx
0029021E  44 8B DB                        mov r11d, ebx
00290221  45 8B 4E 1C                     mov r9d, dword ptr [r14 + 0x1c]
00290225  45 85 C9                        test r9d, r9d
00290228  0F 84 01 02 00 00               je 0x14029042f
0029022E  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00290232  A8 02                           test al, 2
00290234  0F 85 AF 01 00 00               jne 0x1402903e9
0029023A  41 8D 41 FF                     lea eax, [r9 - 1]
0029023E  4D 8D 14 C6                     lea r10, [r14 + rax*8]
00290242  49 8B 44 C6 28                  mov rax, qword ptr [r14 + rax*8 + 0x28]
00290247  48 A9 00 0C 00 00               test rax, 0xc00
0029024D  0F 85 DC 01 00 00               jne 0x14029042f
00290253  4C 8B C0                        mov r8, rax
00290256  48 8B C8                        mov rcx, rax
00290259  41 81 E0 FF 03 00 00            and r8d, 0x3ff
00290260  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00290267  49 8D 50 01                     lea rdx, [r8 + 1]
0029026B  48 C1 E2 0C                     shl rdx, 0xc
0029026F  48 03 D1                        add rdx, rcx
00290272  49 3B D5                        cmp rdx, r13
00290275  75 16                           jne 0x14029028d
00290277  4A 8D 0C 07                     lea rcx, [rdi + r8]
0029027B  49 3B C8                        cmp rcx, r8
0029027E  76 0D                           jbe 0x14029028d
00290280  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
00290287  0F 86 73 03 00 00               jbe 0x140290600
0029028D  41 8D 49 FF                     lea ecx, [r9 - 1]
00290291  48 8D 49 05                     lea rcx, [rcx + 5]
00290295  49 8B 04 CE                     mov rax, qword ptr [r14 + rcx*8]
00290299  4D 8D 14 CE                     lea r10, [r14 + rcx*8]
0029029D  48 8B C8                        mov rcx, rax
002902A0  E9 6C 01 00 00                  jmp 0x140290411
002902A5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
002902B0  FF C7                           inc edi
002902B2  85 3D F4 4F D3 00               test dword ptr [rip + 0xd34ff4], edi
002902B8  0F 84 31 02 00 00               je 0x1402904ef
002902BE  F3 90                           pause
002902C0  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002902C4  48 85 C0                        test rax, rax
002902C7  0F 89 62 FA FF FF               jns 0x14028fd2f
002902CD  EB E1                           jmp 0x1402902b0
002902CF  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002902D9  48 8B C0                        mov rax, rax
002902DC  4C 3B E8                        cmp r13, rax
002902DF  0F 87 83 F9 FF FF               ja 0x14028fc68
002902E5  49 8B CD                        mov rcx, r13
002902E8  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002902F2  48 C1 E9 09                     shr rcx, 9
002902F6  48 23 C8                        and rcx, rax
002902F9  48 8B C2                        mov rax, rdx
002902FC  48 03 C8                        add rcx, rax
002902FF  E8 9C 25 FF FF                  call 0x1402828a0
00290304  48 C1 E8 0C                     shr rax, 0xc
00290308  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00290312  48 23 C1                        and rax, rcx
00290315  48 8D 0C 40                     lea rcx, [rax + rax*2]
00290319  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00290323  48 03 C9                        add rcx, rcx
00290326  48 8B C0                        mov rax, rax
00290329  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0029032D  48 C1 E8 2A                     shr rax, 0x2a
00290331  24 07                           and al, 7
00290333  E9 8E F9 FF FF                  jmp 0x14028fcc6
00290338  49 8D 80 50 20 00 00            lea rax, [r8 + 0x2050]
0029033F  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
00290343  E9 1B FD FF FF                  jmp 0x140290063
00290348  48 8B CF                        mov rcx, rdi
0029034B  4C 3B F1                        cmp r14, rcx
0029034E  0F 82 66 FB FF FF               jb 0x14028feba
00290354  48 8B 0D 85 D9 B9 00            mov rcx, qword ptr [rip + 0xb9d985]
0029035B  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0029035F  48 B9 30 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000030
00290369  48 C1 E2 04                     shl rdx, 4
0029036D  48 8B C9                        mov rcx, rcx
00290370  48 03 D1                        add rdx, rcx
00290373  4C 3B F2                        cmp r14, rdx
00290376  0F 83 3E FB FF FF               jae 0x14028feba
0029037C  48 8B CF                        mov rcx, rdi
0029037F  49 8B D6                        mov rdx, r14
00290382  48 2B D1                        sub rdx, rcx
00290385  48 B9 AB AA AA AA AA AA AA AA   movabs rcx, 0xaaaaaaaaaaaaaaab
0029038F  48 C1 FA 04                     sar rdx, 4
00290393  48 0F AF D1                     imul rdx, rcx
00290397  48 8B 0D 62 58 BA 00            mov rcx, qword ptr [rip + 0xba5862]
0029039E  48 3B D1                        cmp rdx, rcx
002903A1  72 10                           jb 0x1402903b3
002903A3  48 81 C1 00 08 00 00            add rcx, 0x800
002903AA  48 3B D1                        cmp rdx, rcx
002903AD  0F 82 07 FB FF FF               jb 0x14028feba
002903B3  C1 E8 10                        shr eax, 0x10
002903B6  24 07                           and al, 7
002903B8  3C 06                           cmp al, 6
002903BA  0F 84 59 F9 FF FF               je 0x14028fd19
002903C0  49 8B CE                        mov rcx, r14
002903C3  E8 08 DF FF FF                  call 0x14028e2d0
002903C8  83 F8 09                        cmp eax, 9
002903CB  0F 84 E9 FA FF FF               je 0x14028feba
002903D1  E9 43 F9 FF FF                  jmp 0x14028fd19
002903D6  41 F6 C7 04                     test r15b, 4
002903DA  41 BA 02 00 00 00               mov r10d, 2
002903E0  41 0F 45 DA                     cmovne ebx, r10d
002903E4  E9 7E FC FF FF                  jmp 0x140290067
002903E9  45 85 C9                        test r9d, r9d
002903EC  74 41                           je 0x14029042f
002903EE  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
002903F2  A8 02                           test al, 2
002903F4  75 39                           jne 0x14029042f
002903F6  41 8D 49 FF                     lea ecx, [r9 - 1]
002903FA  48 8D 49 05                     lea rcx, [rcx + 5]
002903FE  49 8B 04 CE                     mov rax, qword ptr [r14 + rcx*8]
00290402  4D 8D 14 CE                     lea r10, [r14 + rcx*8]
00290406  48 8B C8                        mov rcx, rax
00290409  48 A9 00 0C 00 00               test rax, 0xc00
0029040F  75 1E                           jne 0x14029042f
00290411  4C 8B FF                        mov r15, rdi
00290414  48 8B D1                        mov rdx, rcx
00290417  49 C1 E7 0C                     shl r15, 0xc
0029041B  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00290422  4F 8D 04 2F                     lea r8, [r15 + r13]
00290426  49 3B D0                        cmp rdx, r8
00290429  0F 84 77 01 00 00               je 0x1402905a6
0029042F  45 3B 4E 0C                     cmp r9d, dword ptr [r14 + 0xc]
00290433  0F 84 22 01 00 00               je 0x14029055b
00290439  48 85 FF                        test rdi, rdi
0029043C  74 79                           je 0x1402904b7
0029043E  48 8D 47 FF                     lea rax, [rdi - 1]
00290442  49 8B CD                        mov rcx, r13
00290445  48 3D FF 03 00 00               cmp rax, 0x3ff
0029044B  BA 00 04 00 00                  mov edx, 0x400
00290450  48 0F 46 D7                     cmovbe rdx, rdi
00290454  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0029045B  48 8D 42 FF                     lea rax, [rdx - 1]
0029045F  25 FF 03 00 00                  and eax, 0x3ff
00290464  48 0B C1                        or rax, rcx
00290467  48 8B CA                        mov rcx, rdx
0029046A  4B 89 44 CE 28                  mov qword ptr [r14 + r9*8 + 0x28], rax
0029046F  45 8B 4E 1C                     mov r9d, dword ptr [r14 + 0x1c]
00290473  49 01 56 20                     add qword ptr [r14 + 0x20], rdx
00290477  41 FF C1                        inc r9d
0029047A  48 C1 E1 0C                     shl rcx, 0xc
0029047E  4C 03 E9                        add r13, rcx
00290481  45 89 4E 1C                     mov dword ptr [r14 + 0x1c], r9d
00290485  48 2B FA                        sub rdi, rdx
00290488  74 AF                           je 0x140290439
0029048A  45 3B 4E 0C                     cmp r9d, dword ptr [r14 + 0xc]
0029048E  0F 84 8A FD FF FF               je 0x14029021e
00290494  EB A3                           jmp 0x140290439
00290496  B0 06                           mov al, 6
00290498  E9 5F F9 FF FF                  jmp 0x14028fdfc
0029049D  49 01 7E 20                     add qword ptr [r14 + 0x20], rdi
002904A1  49 2B C7                        sub rax, r15
002904A4  48 8D 0C 38                     lea rcx, [rax + rdi]
002904A8  48 33 C1                        xor rax, rcx
002904AB  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
002904B1  48 33 C1                        xor rax, rcx
002904B4  49 89 02                        mov qword ptr [r10], rax
002904B7  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
002904BB  41 39 46 1C                     cmp dword ptr [r14 + 0x1c], eax
002904BF  0F 85 13 F8 FF FF               jne 0x14028fcd8
002904C5  45 33 C0                        xor r8d, r8d
002904C8  49 8B D6                        mov rdx, r14
002904CB  48 8B CE                        mov rcx, rsi
002904CE  E8 95 0C FB FF                  call 0x140241168
002904D3  E9 00 F8 FF FF                  jmp 0x14028fcd8
002904D8  41 83 48 10 09                  or dword ptr [r8 + 0x10], 9
002904DD  8B CB                           mov ecx, ebx
002904DF  E9 E8 FA FF FF                  jmp 0x14028ffcc
002904E4  83 4A 10 09                     or dword ptr [rdx + 0x10], 9
002904E8  8B CB                           mov ecx, ebx
002904EA  E9 50 FB FF FF                  jmp 0x14029003f
002904EF  8B 05 C3 65 D3 00               mov eax, dword ptr [rip + 0xd365c3]
002904F5  A8 40                           test al, 0x40
002904F7  0F 84 C1 FD FF FF               je 0x1402902be
002904FD  E8 8E EF 07 00                  call 0x14030f490
00290502  84 C0                           test al, al
00290504  0F 84 B4 FD FF FF               je 0x1402902be
0029050A  8B CF                           mov ecx, edi
0029050C  E8 4F EF 07 00                  call 0x14030f460
00290511  E9 AA FD FF FF                  jmp 0x1402902c0
00290516  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
0029051A  F6 C1 04                        test cl, 4
0029051D  0F 85 F9 FC FF FF               jne 0x14029021c
00290523  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0029052D  48 8B C0                        mov rax, rax
00290530  4C 3B E8                        cmp r13, rax
00290533  0F 82 E3 FC FF FF               jb 0x14029021c
00290539  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00290543  48 8B C0                        mov rax, rax
00290546  4C 3B E8                        cmp r13, rax
00290549  0F 87 CD FC FF FF               ja 0x14029021c
0029054F  83 C9 04                        or ecx, 4
00290552  41 89 4E 10                     mov dword ptr [r14 + 0x10], ecx
00290556  E9 C1 FC FF FF                  jmp 0x14029021c
0029055B  45 85 DB                        test r11d, r11d
0029055E  74 13                           je 0x140290573
00290560  41 38 5E 19                     cmp byte ptr [r14 + 0x19], bl
00290564  0F 85 4D FF FF FF               jne 0x1402904b7
0029056A  45 88 66 19                     mov byte ptr [r14 + 0x19], r12b
0029056E  E9 44 FF FF FF                  jmp 0x1402904b7
00290573  41 38 5E 19                     cmp byte ptr [r14 + 0x19], bl
00290577  0F 85 3A FF FF FF               jne 0x1402904b7
0029057D  49 8B D1                        mov rdx, r9
00290580  49 8D 4E 28                     lea rcx, [r14 + 0x28]
00290584  4C 8D 0D 05 53 40 00            lea r9, [rip + 0x405305]
0029058B  41 B8 08 00 00 00               mov r8d, 8
00290591  E8 5A 04 27 00                  call 0x1405009f0
00290596  49 8B CE                        mov rcx, r14
00290599  E8 0A 8E 01 00                  call 0x1402a93a8
0029059E  45 8B DC                        mov r11d, r12d
002905A1  E9 7B FC FF FF                  jmp 0x140290221
002905A6  81 E1 FF 03 00 00               and ecx, 0x3ff
002905AC  48 8D 14 0F                     lea rdx, [rdi + rcx]
002905B0  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
002905B7  0F 87 72 FE FF FF               ja 0x14029042f
002905BD  48 3B D1                        cmp rdx, rcx
002905C0  0F 86 69 FE FF FF               jbe 0x14029042f
002905C6  E9 D2 FE FF FF                  jmp 0x14029049d
002905CB  C7 05 BF 10 D8 00 00 02 00 00   mov dword ptr [rip + 0xd810bf], 0x200
002905D5  48 8D 15 E4 EE D7 00            lea rdx, [rip + 0xd7eee4]
002905DC  44 89 25 3D F0 D7 00            mov dword ptr [rip + 0xd7f03d], r12d
002905E3  E9 0D F9 FF FF                  jmp 0x14028fef5
002905E8  4C 8B C8                        mov r9, rax
002905EB  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
002905F0  BA 40 04 00 00                  mov edx, 0x440
002905F5  B9 1A 00 00 00                  mov ecx, 0x1a
002905FA  E8 61 D0 26 00                  call 0x1404fd660
002905FF  CC                              int3
00290600  49 01 7E 20                     add qword ptr [r14 + 0x20], rdi
00290604  48 8D 0C 38                     lea rcx, [rax + rdi]
00290608  48 33 C1                        xor rax, rcx
0029060B  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00290611  48 33 C1                        xor rax, rcx
00290614  49 89 42 28                     mov qword ptr [r10 + 0x28], rax
00290618  E9 9A FE FF FF                  jmp 0x1402904b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002901B8(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    unsigned __int64 v_stack_p20;

    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (60);
    result = (unsigned __int8)((result) & (a1));
    result = (*(unsigned __int64 *)(v_r14 + 24)) & (a1);
    result = (unsigned int)(*(unsigned int *)(v_r14 + 32));
    v_r14 = *(unsigned __int64 *)(v_rdi + 64);
    if (*(unsigned __int64 *)(v_rdi + 64) == 0) {
        a2 = v_rdi + 56;
        a1 = v_rsi;
        result = MiAcquirePrcbAgeTrimLists(a1, a2, a3, a4);
        v_r14 = *(unsigned __int64 *)(v_rdi + 64);
    }
    if ((*(unsigned int *)(v_r14 + 8)) != ((unsigned int)(v_r12))) goto loc_00290516;
loc_0029021C:
    v_rbx = 0;
loc_0029021E:
loc_00290221:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 28))) == 0) goto loc_0029042F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 16)))) & (2)) != 0) goto loc_002903E9;
    if (((*(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_0029042F;
    a3 = (unsigned int)((*(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_r13) goto loc_0029028D;
    if ((v_r12 + a3 * 1) <= a3) goto loc_0029028D;
    if ((v_r12 + a3 * 1) <= 0x3FFULL) goto loc_00290600;
loc_0029028D:
    goto loc_00290411;
loc_002903E9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 28))) == 0) goto loc_0029042F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 16)))) & (2)) != 0) goto loc_0029042F;
    if (((*(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_0029042F;
loc_00290411:
    v_r15 = (v_r12) << (12);
    a2 = (*(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (v_r15 + v_r13 * 1)) goto loc_002905A6;
loc_0029042F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 28)))) == (*(unsigned int *)(v_r14 + 12))) goto loc_0029055B;
loc_00290439:
    if (v_r12 == 0) goto loc_002904B7;
    a2 = (unsigned int)(0x400ULL);
    if ((v_r12 - 1) <= 0x3FFULL) { a2 = v_r12; }
    a1 = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) * 8 + 40) = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 28))) + 1);
    a1 = (a2) << (12);
    v_r13 = (v_r13) + (a1);
    *(unsigned int *)(v_r14 + 28) = (unsigned int)(a4);
    v_rdi = (v_r12) - (a2);
    if (condition_is_equal) goto loc_00290439;
    if (((unsigned int)(a4)) == (*(unsigned int *)(v_r14 + 12))) goto loc_0029021E;
    goto loc_00290439;
loc_0029049D:
    result = (result) - (v_r15);
    result = (result) ^ (result + v_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_rdi * 1);
    *(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 + 5 * 8) = result;
loc_002904B7:
    a3 = 0;
    result = MiFreeWsleList(v_rsi, v_r14, a3, a4);
loc_00290516:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 16)))) & (4)) != 0) goto loc_0029021C;
    if (v_r13 < result) goto loc_0029021C;
    if (v_r13 > result) goto loc_0029021C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 16))) | (4));
    *(unsigned int *)(v_r14 + 16) = a1;
    goto loc_0029021C;
loc_0029055B:
    if (0 == 0) goto loc_00290573;
    if ((*(unsigned __int8 *)(v_r14 + 25)) != 0) goto loc_002904B7;
    *(unsigned __int8 *)(v_r14 + 25) = (unsigned __int8)(v_r12);
    goto loc_002904B7;
loc_00290573:
    if ((*(unsigned __int8 *)(v_r14 + 25)) != 0) goto loc_002904B7;
    result = qsort(v_r14 + 40, a4, 8, v_rip + 4215557);
    result = MiCompressTbFlushList(v_r14, a4, 8, v_rip + 4215557);
    goto loc_00290221;
loc_002905A6:
    a1 = (unsigned int)((v_r14) & (0x3FFULL));
    if ((v_rdi + a1 * 1) > 0x3FFULL) goto loc_0029042F;
    if ((v_rdi + a1 * 1) <= a1) goto loc_0029042F;
    goto loc_0029049D;
loc_00290600:
    result = (result) ^ (result + v_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + v_rdi * 1);
    *(unsigned __int64 *)(v_r14 + (unsigned int)(*(unsigned int *)(v_r14 + 28)) - 1 + 5 * 8 + 40) = result;
    goto loc_002904B7;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002901B8(uint8_t Arg1)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    uint64_t v_stack_p20;

    result = (*(uint64_t *)(local_r14 + 0x28)) >> (60);
    result = (uint8_t)((result) & (Arg1));
    result = (*(uint64_t *)(local_r14 + 0x18)) & (Arg1);
    result = (uint32_t)(*(uint32_t *)(local_r14 + 0x20));
    local_r14 = *(uint64_t *)(local_rdi + 0x40);
    if (*(uint64_t *)(local_rdi + 0x40) == 0) {
        a2 = local_rdi + 56;
        Arg1 = local_rsi;
        result = MiAcquirePrcbAgeTrimLists(Arg1, a2, a3, a4);
        local_r14 = *(uint64_t *)(local_rdi + 0x40);
    }
    if ((*(uint32_t *)(local_r14 + 0x8)) != ((uint32_t)(local_r12))) goto loc_00290516;
loc_0029021C:
    local_rbx = 0;
loc_0029021E:
loc_00290221:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x1C))) == 0) goto loc_0029042F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x10)))) & (2)) != 0) goto loc_002903E9;
    if (((*(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_0029042F;
    a3 = (uint32_t)((*(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (Arg1);
    if (a2 != local_r13) goto loc_0029028D;
    if ((local_r12 + a3 * 1) <= a3) goto loc_0029028D;
    if ((local_r12 + a3 * 1) <= 0x3FFULL) goto loc_00290600;
loc_0029028D:
    goto loc_00290411;
loc_002903E9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x1C))) == 0) goto loc_0029042F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x10)))) & (2)) != 0) goto loc_0029042F;
    if (((*(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_0029042F;
loc_00290411:
    local_r15 = (local_r12) << (12);
    a2 = (*(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (local_r15 + local_r13 * 1)) goto loc_002905A6;
loc_0029042F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x1C)))) == (*(uint32_t *)(local_r14 + 0xC))) goto loc_0029055B;
loc_00290439:
    if (local_r12 == 0) goto loc_002904B7;
    a2 = (uint32_t)(0x400ULL);
    if ((local_r12 - 1) <= 0x3FFULL) { a2 = local_r12; }
    Arg1 = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((a2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    *(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) * 8 + 0x28) = result;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x1C))) + 1);
    Arg1 = (a2) << (12);
    local_r13 = (local_r13) + (Arg1);
    *(uint32_t *)(local_r14 + 0x1C) = (uint32_t)(a4);
    local_rdi = (local_r12) - (a2);
    if (condition_is_equal) goto loc_00290439;
    if (((uint32_t)(a4)) == (*(uint32_t *)(local_r14 + 0xC))) goto loc_0029021E;
    goto loc_00290439;
loc_0029049D:
    result = (result) - (local_r15);
    result = (result) ^ (result + local_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + local_rdi * 1);
    *(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 + 0x5 * 8) = result;
loc_002904B7:
    a3 = 0;
    result = MiFreeWsleList(local_rsi, local_r14, a3, a4);
loc_00290516:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x10)))) & (4)) != 0) goto loc_0029021C;
    if (local_r13 < result) goto loc_0029021C;
    if (local_r13 > result) goto loc_0029021C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x10))) | (4));
    *(uint32_t *)(local_r14 + 0x10) = Arg1;
    goto loc_0029021C;
loc_0029055B:
    if (0 == 0) goto loc_00290573;
    if ((*(uint8_t *)(local_r14 + 0x19)) != 0) goto loc_002904B7;
    *(uint8_t *)(local_r14 + 0x19) = (uint8_t)(local_r12);
    goto loc_002904B7;
loc_00290573:
    if ((*(uint8_t *)(local_r14 + 0x19)) != 0) goto loc_002904B7;
    result = qsort(local_r14 + 40, a4, 8, v_rip + 4215557);
    result = MiCompressTbFlushList(local_r14, a4, 8, v_rip + 4215557);
    goto loc_00290221;
loc_002905A6:
    Arg1 = (uint32_t)((local_r14) & (0x3FFULL));
    if ((local_rdi + Arg1 * 1) > 0x3FFULL) goto loc_0029042F;
    if ((local_rdi + Arg1 * 1) <= Arg1) goto loc_0029042F;
    goto loc_0029049D;
loc_00290600:
    result = (result) ^ (result + local_rdi * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + local_rdi * 1);
    *(uint64_t *)(local_r14 + (uint32_t)(*(uint32_t *)(local_r14 + 0x1C)) - 0x1 + 0x5 * 8 + 0x28) = result;
    goto loc_002904B7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002901B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
