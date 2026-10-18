# IoFillTriageDumpBuffer

- RVA: `0x005921CC`–`0x005927A2` (길이 `1,494` bytes)
- VA: `0x00000001405921CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8448`
- 디코드: `415`개 명령, `1,494/1,494` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0059224E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00592397` → [IopIsAddressRangeValid](../4B/IopIsAddressRangeValid_function_004B6CBC.md) (function, `0x004B6CBC`)
- `0x005923E0` → [IopGetMaxValidMemorySize](IopGetMaxValidMemorySize_function_0059559C.md) (function, `0x0059559C`)
- `0x0059246F` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0059249D` → [MmWriteUnloadedDriverInformation](../67/MmWriteUnloadedDriverInformation_function_0067E08C.md) (function, `0x0067E08C`)
- `0x005924BC` → [IoGetLoadedDriverInfo](../4B/IoGetLoadedDriverInfo_function_004B6C20.md) (function, `0x004B6C20`)
- `0x00592546` → [IopWriteDriverList](../4B/IopWriteDriverList_function_004B6AD0.md) (function, `0x004B6AD0`)
- `0x00592566` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0059256B` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x005925BB` → [IopAddRunTimeTriageDataBlocks](IopAddRunTimeTriageDataBlocks_function_0059462C.md) (function, `0x0059462C`)
- `0x00592635` → [MmWriteTriageInformation](../67/MmWriteTriageInformation_function_0067DF6C.md) (function, `0x0067DF6C`)
- `0x00592660` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00592692` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005926C4` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005926E4` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00592703` → [KdCopyDataBlock](../5B/KdCopyDataBlock_function_005B04E4.md) (function, `0x005B04E4`)
- `0x00592719` → [IopFillTriageDumpDataBlocks](IopFillTriageDumpDataBlocks_function_005953E8.md) (function, `0x005953E8`)

### Direct callers
- [IopCollectTriageDumpData](IopCollectTriageDumpData_function_00594754.md) at `0x00594867`
- [IopWriteCapsuleTriageDumpToFirmware](IopWriteCapsuleTriageDumpToFirmware_function_005967AC.md) at `0x00596900`
- [DbgkpTriageDumpFillHeaders](../../page/71/DbgkpTriageDumpFillHeaders_function_00712950.md) at `0x00712A22`

### Static image references
- `0x005921F3` → RVA `0x00FC41C0` (`.data`; read)
- `0x0059245E` → RVA `0x00EF54E0` (`.data`; read)
- `0x00592474` → RVA `0x00EF54B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005921CC  48 8B C4                        mov rax, rsp
005921CF  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
005921D3  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005921D7  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
005921DB  55                              push rbp
005921DC  56                              push rsi
005921DD  57                              push rdi
005921DE  41 54                           push r12
005921E0  41 55                           push r13
005921E2  41 56                           push r14
005921E4  41 57                           push r15
005921E6  48 83 EC 40                     sub rsp, 0x40
005921EA  8B BC 24 C0 00 00 00            mov edi, dword ptr [rsp + 0xc0]
005921F1  33 ED                           xor ebp, ebp
005921F3  8B 35 C7 1F A3 00               mov esi, dword ptr [rip + 0xa31fc7]
005921F9  45 8B F9                        mov r15d, r9d
005921FC  89 68 B8                        mov dword ptr [rax - 0x48], ebp
005921FF  45 8A F0                        mov r14b, r8b
00592202  89 68 08                        mov dword ptr [rax + 8], ebp
00592205  48 8B DA                        mov rbx, rdx
00592208  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00592210  44 8B E9                        mov r13d, ecx
00592213  89 AC 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ebp
0059221A  48 85 C0                        test rax, rax
0059221D  74 02                           je 0x140592221
0059221F  89 28                           mov dword ptr [rax], ebp
00592221  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00592229  48 85 C0                        test rax, rax
0059222C  74 02                           je 0x140592230
0059222E  89 28                           mov dword ptr [rax], ebp
00592230  41 81 FD 84 00 00 00            cmp r13d, 0x84
00592237  73 0A                           jae 0x140592243
00592239  B8 17 00 00 C0                  mov eax, 0xc0000017
0059223E  E9 46 05 00 00                  jmp 0x140592789
00592243  33 D2                           xor edx, edx
00592245  41 B8 80 00 00 00               mov r8d, 0x80
0059224B  48 8B CB                        mov rcx, rbx
0059224E  E8 ED 49 13 00                  call 0x1406c6c40
00592253  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
0059225B  41 8D 85 00 20 00 00            lea eax, [r13 + 0x2000]
00592262  89 43 04                        mov dword ptr [rbx + 4], eax
00592265  41 83 C5 FC                     add r13d, -4
00592269  83 C0 FC                        add eax, -4
0059226C  45 8B E5                        mov r12d, r13d
0059226F  89 43 08                        mov dword ptr [rbx + 8], eax
00592272  41 B8 00 01 00 00               mov r8d, 0x100
00592278  33 C0                           xor eax, eax
0059227A  41 89 44 1D 00                  mov dword ptr [r13 + rbx], eax
0059227F  48 8B C2                        mov rax, rdx
00592282  89 6B 40                        mov dword ptr [rbx + 0x40], ebp
00592285  48 F7 D8                        neg rax
00592288  89 33                           mov dword ptr [rbx], esi
0059228A  BE 80 20 00 00                  mov esi, 0x2080
0059228F  1B ED                           sbb ebp, ebp
00592291  C7 43 0C 48 03 00 00            mov dword ptr [rbx + 0xc], 0x348
00592298  F7 DD                           neg ebp
0059229A  C7 43 10 00 0F 00 00            mov dword ptr [rbx + 0x10], 0xf00
005922A1  81 C5 82 00 00 00               add ebp, 0x82
005922A7  89 7B 44                        mov dword ptr [rbx + 0x44], edi
005922AA  45 85 F8                        test r8d, r15d
005922AD  74 18                           je 0x1405922c7
005922AF  8D 46 50                        lea eax, [rsi + 0x50]
005922B2  44 3B E8                        cmp r13d, eax
005922B5  76 0A                           jbe 0x1405922c1
005922B7  89 73 14                        mov dword ptr [rbx + 0x14], esi
005922BA  41 0B E8                        or ebp, r8d
005922BD  8B F0                           mov esi, eax
005922BF  EB 06                           jmp 0x1405922c7
005922C1  41 0B F8                        or edi, r8d
005922C4  89 7B 44                        mov dword ptr [rbx + 0x44], edi
005922C7  41 F6 C7 04                     test r15b, 4
005922CB  74 1B                           je 0x1405922e8
005922CD  8D 86 00 CF 00 00               lea eax, [rsi + 0xcf00]
005922D3  41 3B C5                        cmp eax, r13d
005922D6  73 0A                           jae 0x1405922e2
005922D8  89 73 1C                        mov dword ptr [rbx + 0x1c], esi
005922DB  83 CD 04                        or ebp, 4
005922DE  8B F0                           mov esi, eax
005922E0  EB 06                           jmp 0x1405922e8
005922E2  41 0B F8                        or edi, r8d
005922E5  89 7B 44                        mov dword ptr [rbx + 0x44], edi
005922E8  41 F6 C7 08                     test r15b, 8
005922EC  74 1B                           je 0x140592309
005922EE  8D 86 40 08 00 00               lea eax, [rsi + 0x840]
005922F4  41 3B C5                        cmp eax, r13d
005922F7  73 0A                           jae 0x140592303
005922F9  89 73 20                        mov dword ptr [rbx + 0x20], esi
005922FC  83 CD 08                        or ebp, 8
005922FF  8B F0                           mov esi, eax
00592301  EB 06                           jmp 0x140592309
00592303  41 0B F8                        or edi, r8d
00592306  89 7B 44                        mov dword ptr [rbx + 0x44], edi
00592309  41 F6 C7 10                     test r15b, 0x10
0059230D  74 1B                           je 0x14059232a
0059230F  8D 86 98 07 00 00               lea eax, [rsi + 0x798]
00592315  41 3B C5                        cmp eax, r13d
00592318  73 0A                           jae 0x140592324
0059231A  89 73 24                        mov dword ptr [rbx + 0x24], esi
0059231D  83 CD 10                        or ebp, 0x10
00592320  8B F0                           mov esi, eax
00592322  EB 06                           jmp 0x14059232a
00592324  41 0B F8                        or edi, r8d
00592327  89 7B 44                        mov dword ptr [rbx + 0x44], edi
0059232A  41 F6 C7 20                     test r15b, 0x20
0059232E  0F 84 E7 00 00 00               je 0x14059241b
00592334  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0059233C  F7 41 78 00 00 02 00            test dword ptr [rcx + 0x78], 0x20000
00592343  0F 84 D2 00 00 00               je 0x14059241b
00592349  48 8B BA 98 00 00 00            mov rdi, qword ptr [rdx + 0x98]
00592350  4C 8B 61 30                     mov r12, qword ptr [rcx + 0x30]
00592354  4C 8B 71 38                     mov r14, qword ptr [rcx + 0x38]
00592358  4C 3B E7                        cmp r12, rdi
0059235B  77 05                           ja 0x140592362
0059235D  49 3B FE                        cmp rdi, r14
00592360  72 60                           jb 0x1405923c2
00592362  48 8B 79 30                     mov rdi, qword ptr [rcx + 0x30]
00592366  65 8A 04 25 3C 3A 00 00         mov al, byte ptr gs:[0x3a3c]
0059236E  A8 01                           test al, 1
00592370  74 50                           je 0x1405923c2
00592372  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0059237B  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0059237F  74 41                           je 0x1405923c2
00592381  65 48 8B 04 25 20 3A 00 00      mov rax, qword ptr gs:[0x3a20]
0059238A  BA 50 00 00 00                  mov edx, 0x50
0059238F  4C 8D 3C 02                     lea r15, [rdx + rax]
00592393  49 8D 4F B0                     lea rcx, [r15 - 0x50]
00592397  E8 20 49 F2 FF                  call 0x1404b6cbc
0059239C  84 C0                           test al, al
0059239E  74 1A                           je 0x1405923ba
005923A0  49 8B 47 F0                     mov rax, qword ptr [r15 - 0x10]
005923A4  44 8B BC 24 98 00 00 00         mov r15d, dword ptr [rsp + 0x98]
005923AC  4C 3B E0                        cmp r12, rax
005923AF  77 11                           ja 0x1405923c2
005923B1  49 3B C6                        cmp rax, r14
005923B4  48 0F 42 F8                     cmovb rdi, rax
005923B8  EB 08                           jmp 0x1405923c2
005923BA  44 8B BC 24 98 00 00 00         mov r15d, dword ptr [rsp + 0x98]
005923C2  49 8B C6                        mov rax, r14
005923C5  B9 FF 7F 00 00                  mov ecx, 0x7fff
005923CA  48 2B C7                        sub rax, rdi
005923CD  48 3B C1                        cmp rax, rcx
005923D0  73 05                           jae 0x1405923d7
005923D2  44 2B F7                        sub r14d, edi
005923D5  EB 03                           jmp 0x1405923da
005923D7  44 8B F1                        mov r14d, ecx
005923DA  41 8B D6                        mov edx, r14d
005923DD  48 8B CF                        mov rcx, rdi
005923E0  E8 B7 31 00 00                  call 0x14059559c
005923E5  44 8A B4 24 90 00 00 00         mov r14b, byte ptr [rsp + 0x90]
005923ED  41 B8 00 01 00 00               mov r8d, 0x100
005923F3  45 8B E5                        mov r12d, r13d
005923F6  85 C0                           test eax, eax
005923F8  74 21                           je 0x14059241b
005923FA  8D 0C 06                        lea ecx, [rsi + rax]
005923FD  41 3B CD                        cmp ecx, r13d
00592400  73 15                           jae 0x140592417
00592402  89 73 28                        mov dword ptr [rbx + 0x28], esi
00592405  8D 71 07                        lea esi, [rcx + 7]
00592408  83 E6 F8                        and esi, 0xfffffff8
0059240B  89 43 2C                        mov dword ptr [rbx + 0x2c], eax
0059240E  83 CD 20                        or ebp, 0x20
00592411  48 89 7B 48                     mov qword ptr [rbx + 0x48], rdi
00592415  EB 04                           jmp 0x14059241b
00592417  44 09 43 44                     or dword ptr [rbx + 0x44], r8d
0059241B  BA 00 04 00 00                  mov edx, 0x400
00592420  44 85 FA                        test edx, r15d
00592423  74 24                           je 0x140592449
00592425  8B C6                           mov eax, esi
00592427  8D 4A A0                        lea ecx, [rdx - 0x60]
0059242A  48 03 C1                        add rax, rcx
0059242D  49 3B C4                        cmp rax, r12
00592430  73 13                           jae 0x140592445
00592432  89 73 70                        mov dword ptr [rbx + 0x70], esi
00592435  81 C6 A7 03 00 00               add esi, 0x3a7
0059243B  83 E6 F8                        and esi, 0xfffffff8
0059243E  89 4B 74                        mov dword ptr [rbx + 0x74], ecx
00592441  0B EA                           or ebp, edx
00592443  EB 04                           jmp 0x140592449
00592445  44 09 43 44                     or dword ptr [rbx + 0x44], r8d
00592449  48 8D BB 00 E0 FF FF            lea rdi, [rbx - 0x2000]
00592450  45 84 F6                        test r14b, r14b
00592453  75 1F                           jne 0x140592474
00592455  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0059245E  48 8D 0D 7B 30 96 00            lea rcx, [rip + 0x96307b]
00592465  B2 01                           mov dl, 1
00592467  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0059246E  90                              nop
0059246F  E8 4C F7 C7 FF                  call 0x140211bc0
00592474  48 8B 05 35 30 96 00            mov rax, qword ptr [rip + 0x963035]
0059247B  48 F7 D8                        neg rax
0059247E  1B C9                           sbb ecx, ecx
00592480  81 E1 F0 0A 00 00               and ecx, 0xaf0
00592486  8D 41 08                        lea eax, [rcx + 8]
00592489  03 C6                           add eax, esi
0059248B  41 3B C5                        cmp eax, r13d
0059248E  73 14                           jae 0x1405924a4
00592490  8B CE                           mov ecx, esi
00592492  83 CD 40                        or ebp, 0x40
00592495  89 73 18                        mov dword ptr [rbx + 0x18], esi
00592498  48 03 CF                        add rcx, rdi
0059249B  8B F0                           mov esi, eax
0059249D  E8 EA BB 0E 00                  call 0x14067e08c
005924A2  EB 05                           jmp 0x1405924a9
005924A4  0F BA 6B 44 08                  bts dword ptr [rbx + 0x44], 8
005924A9  41 F6 C7 40                     test r15b, 0x40
005924AD  74 4A                           je 0x1405924f9
005924AF  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
005924B4  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
005924BC  E8 5F 47 F2 FF                  call 0x1404b6c20
005924C1  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
005924C8  85 C0                           test eax, eax
005924CA  78 2D                           js 0x1405924f9
005924CC  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
005924D3  8D 0C D2                        lea ecx, [rdx + rdx*8]
005924D6  C1 E1 04                        shl ecx, 4
005924D9  85 C9                           test ecx, ecx
005924DB  74 1C                           je 0x1405924f9
005924DD  44 8D 04 0E                     lea r8d, [rsi + rcx]
005924E1  45 3B C5                        cmp r8d, r13d
005924E4  73 0E                           jae 0x1405924f4
005924E6  89 73 30                        mov dword ptr [rbx + 0x30], esi
005924E9  83 CD 40                        or ebp, 0x40
005924EC  41 8B F0                        mov esi, r8d
005924EF  89 53 34                        mov dword ptr [rbx + 0x34], edx
005924F2  EB 05                           jmp 0x1405924f9
005924F4  0F BA 6B 44 08                  bts dword ptr [rbx + 0x44], 8
005924F9  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00592500  8D 0C 40                        lea ecx, [rax + rax*2]
00592503  8D 14 4D 07 00 00 00            lea edx, [rcx*2 + 7]
0059250A  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
0059250F  03 54 24 30                     add edx, dword ptr [rsp + 0x30]
00592513  23 D1                           and edx, ecx
00592515  74 1A                           je 0x140592531
00592517  8D 04 16                        lea eax, [rsi + rdx]
0059251A  41 3B C5                        cmp eax, r13d
0059251D  73 0D                           jae 0x14059252c
0059251F  89 73 38                        mov dword ptr [rbx + 0x38], esi
00592522  8D 70 07                        lea esi, [rax + 7]
00592525  23 F1                           and esi, ecx
00592527  89 53 3C                        mov dword ptr [rbx + 0x3c], edx
0059252A  EB 05                           jmp 0x140592531
0059252C  0F BA 6B 44 08                  bts dword ptr [rbx + 0x44], 8
00592531  44 8B 43 30                     mov r8d, dword ptr [rbx + 0x30]
00592535  45 85 C0                        test r8d, r8d
00592538  74 20                           je 0x14059255a
0059253A  44 8B 4B 38                     mov r9d, dword ptr [rbx + 0x38]
0059253E  45 85 C9                        test r9d, r9d
00592541  74 17                           je 0x14059255a
00592543  48 8B CF                        mov rcx, rdi
00592546  E8 85 45 F2 FF                  call 0x1404b6ad0
0059254B  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00592552  85 C0                           test eax, eax
00592554  79 04                           jns 0x14059255a
00592556  83 63 30 00                     and dword ptr [rbx + 0x30], 0
0059255A  45 84 F6                        test r14b, r14b
0059255D  75 11                           jne 0x140592570
0059255F  48 8D 0D 7A 2F 96 00            lea rcx, [rip + 0x962f7a]
00592566  E8 A5 D4 CC FF                  call 0x14025fa10
0059256B  E8 40 B3 CC FF                  call 0x14025d8b0
00592570  F7 84 24 98 00 00 00 00 08 00 00  test dword ptr [rsp + 0x98], 0x800
0059257B  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00592583  44 8B B4 24 C8 00 00 00         mov r14d, dword ptr [rsp + 0xc8]
0059258B  0F 84 99 00 00 00               je 0x14059262a
00592591  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
00592595  49 8B D7                        mov rdx, r15
00592598  8B 43 2C                        mov eax, dword ptr [rbx + 0x2c]
0059259B  4C 8B 8C 24 A8 00 00 00         mov r9, qword ptr [rsp + 0xa8]
005925A3  48 03 C1                        add rax, rcx
005925A6  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
005925AE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005925B3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005925B8  41 8B CE                        mov ecx, r14d
005925BB  E8 6C 20 00 00                  call 0x14059462c
005925C0  83 63 7C 00                     and dword ptr [rbx + 0x7c], 0
005925C4  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
005925CA  45 33 C0                        xor r8d, r8d
005925CD  45 3B C6                        cmp r8d, r14d
005925D0  73 48                           jae 0x14059261a
005925D2  45 8B C8                        mov r9d, r8d
005925D5  4D 03 C9                        add r9, r9
005925D8  33 D2                           xor edx, edx
005925DA  4F 8B 54 CF 08                  mov r10, qword ptr [r15 + r9*8 + 8]
005925DF  43 3B 14 CF                     cmp edx, dword ptr [r15 + r9*8]
005925E3  73 2B                           jae 0x140592610
005925E5  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
005925E9  41 2B 02                        sub eax, dword ptr [r10]
005925EC  83 C0 07                        add eax, 7
005925EF  41 23 C3                        and eax, r11d
005925F2  83 C0 10                        add eax, 0x10
005925F5  03 C6                           add eax, esi
005925F7  41 3B C5                        cmp eax, r13d
005925FA  73 19                           jae 0x140592615
005925FC  85 D2                           test edx, edx
005925FE  75 03                           jne 0x140592603
00592600  89 73 78                        mov dword ptr [rbx + 0x78], esi
00592603  FF 43 7C                        inc dword ptr [rbx + 0x7c]
00592606  FF C2                           inc edx
00592608  49 83 C2 10                     add r10, 0x10
0059260C  8B F0                           mov esi, eax
0059260E  EB CF                           jmp 0x1405925df
00592610  41 FF C0                        inc r8d
00592613  EB B8                           jmp 0x1405925cd
00592615  0F BA 6B 44 08                  bts dword ptr [rbx + 0x44], 8
0059261A  83 C6 07                        add esi, 7
0059261D  41 23 F3                        and esi, r11d
00592620  83 7B 7C 00                     cmp dword ptr [rbx + 0x7c], 0
00592624  74 04                           je 0x14059262a
00592626  0F BA ED 0B                     bts ebp, 0xb
0059262A  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0059262D  85 C0                           test eax, eax
0059262F  74 09                           je 0x14059263a
00592631  48 8D 0C 07                     lea rcx, [rdi + rax]
00592635  E8 32 B9 0E 00                  call 0x14067df6c
0059263A  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0059263D  85 C0                           test eax, eax
0059263F  74 24                           je 0x140592665
00592641  8B C8                           mov ecx, eax
00592643  48 05 00 CF 00 00               add rax, 0xcf00
00592649  49 3B C4                        cmp rax, r12
0059264C  77 17                           ja 0x140592665
0059264E  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00592657  48 03 CF                        add rcx, rdi
0059265A  41 B8 00 CF 00 00               mov r8d, 0xcf00
00592660  E8 DB 41 13 00                  call 0x1406c6840
00592665  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00592668  85 C0                           test eax, eax
0059266A  74 2D                           je 0x140592699
0059266C  8B C8                           mov ecx, eax
0059266E  48 05 40 08 00 00               add rax, 0x840
00592674  49 3B C4                        cmp rax, r12
00592677  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
0059267F  77 20                           ja 0x1405926a1
00592681  49 8B 94 24 B8 00 00 00         mov rdx, qword ptr [r12 + 0xb8]
00592689  48 03 CF                        add rcx, rdi
0059268C  41 B8 40 08 00 00               mov r8d, 0x840
00592692  E8 A9 41 13 00                  call 0x1406c6840
00592697  EB 08                           jmp 0x1405926a1
00592699  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
005926A1  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
005926A4  85 C0                           test eax, eax
005926A6  74 21                           je 0x1405926c9
005926A8  8B C8                           mov ecx, eax
005926AA  41 8B D5                        mov edx, r13d
005926AD  48 05 98 07 00 00               add rax, 0x798
005926B3  48 3B C2                        cmp rax, rdx
005926B6  77 11                           ja 0x1405926c9
005926B8  48 03 CF                        add rcx, rdi
005926BB  49 8B D4                        mov rdx, r12
005926BE  41 B8 98 07 00 00               mov r8d, 0x798
005926C4  E8 77 41 13 00                  call 0x1406c6840
005926C9  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
005926CC  85 C9                           test ecx, ecx
005926CE  74 19                           je 0x1405926e9
005926D0  44 8B 43 2C                     mov r8d, dword ptr [rbx + 0x2c]
005926D4  48 8B 53 48                     mov rdx, qword ptr [rbx + 0x48]
005926D8  42 8D 04 01                     lea eax, [rcx + r8]
005926DC  41 3B C5                        cmp eax, r13d
005926DF  77 08                           ja 0x1405926e9
005926E1  48 03 CF                        add rcx, rdi
005926E4  E8 57 41 13 00                  call 0x1406c6840
005926E9  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
005926EC  45 8B E5                        mov r12d, r13d
005926EF  85 C0                           test eax, eax
005926F1  74 15                           je 0x140592708
005926F3  8B C8                           mov ecx, eax
005926F5  48 05 A0 03 00 00               add rax, 0x3a0
005926FB  49 3B C4                        cmp rax, r12
005926FE  77 08                           ja 0x140592708
00592700  48 03 CF                        add rcx, rdi
00592703  E8 DC DD 01 00                  call 0x1405b04e4
00592708  45 85 F6                        test r14d, r14d
0059270B  74 11                           je 0x14059271e
0059270D  4C 8B CF                        mov r9, rdi
00592710  4D 8B C7                        mov r8, r15
00592713  41 8B D6                        mov edx, r14d
00592716  48 8B CB                        mov rcx, rbx
00592719  E8 CA 2C 00 00                  call 0x1405953e8
0059271E  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00592726  41 81 FD FC DF 03 00            cmp r13d, 0x3dffc
0059272D  75 0C                           jne 0x14059273b
0059272F  48 85 C9                        test rcx, rcx
00592732  75 07                           jne 0x14059273b
00592734  BE 00 00 04 00                  mov esi, 0x40000
00592739  EB 10                           jmp 0x14059274b
0059273B  83 C6 04                        add esi, 4
0059273E  48 85 C9                        test rcx, rcx
00592741  74 08                           je 0x14059274b
00592743  8D 86 00 E0 FF FF               lea eax, [rsi - 0x2000]
00592749  89 01                           mov dword ptr [rcx], eax
0059274B  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00592753  48 85 C0                        test rax, rax
00592756  74 02                           je 0x14059275a
00592758  89 28                           mov dword ptr [rax], ebp
0059275A  8D 46 FC                        lea eax, [rsi - 4]
0059275D  89 73 04                        mov dword ptr [rbx + 4], esi
00592760  89 43 08                        mov dword ptr [rbx + 8], eax
00592763  8B C8                           mov ecx, eax
00592765  48 05 00 E0 FF FF               add rax, -0x2000
0059276B  49 3B C4                        cmp rax, r12
0059276E  77 14                           ja 0x140592784
00592770  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00592777  C7 84 19 00 E0 FF FF 54 52 47 44  mov dword ptr [rcx + rbx - 0x2000], 0x44475254
00592782  EB 05                           jmp 0x140592789
00592784  B8 9A 00 00 C0                  mov eax, 0xc000009a
00592789  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00592791  48 83 C4 40                     add rsp, 0x40
00592795  41 5F                           pop r15
00592797  41 5E                           pop r14
00592799  41 5D                           pop r13
0059279B  41 5C                           pop r12
0059279D  5F                              pop rdi
0059279E  5E                              pop rsi
0059279F  5D                              pop rbp
005927A0  C3                              ret
005927A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoFillTriageDumpBuffer(int a1, __int64 a2, unsigned __int8 a3, int a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned int a9, unsigned int a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (64);
    v_rbp = 0;
    *(unsigned int *)(v_rsp - 72) = 0;
    *(unsigned int *)(v_rsp + 8) = 0;
    v_stack_p40 = 0;
    if (a13 != 0) {
        *(unsigned int *)(a13) = 0;
    }
    if (a5 != 0) {
        *(unsigned int *)(a5) = 0;
    }
    if (((unsigned int)((unsigned int)(a1))) >= 132) goto loc_00592243;
    goto loc_00592789;
loc_00592243:
    a2 = 0;
    result = memset(0, a2, 128, a4);
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(a1) + 8192);
    v_r13 = (unsigned int)(((unsigned int)(a1)) + (-4));
    result = (unsigned int)(((unsigned int)(a1) + 8192) + (-4));
    *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    result = 0;
    *(unsigned int *)(v_r13 + a2 * 1) = 0;
    *(unsigned int *)(a2 + 64) = 0;
    result = -(a6);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10690503)));
    *(unsigned int *)(a2 + 12) = 840;
    v_rbp = (unsigned int)(-(v_rbp));
    *(unsigned int *)(a2 + 16) = 0xF00ULL;
    v_rbp = (unsigned int)((v_rbp) + (130));
    *(unsigned int *)(a2 + 68) = (unsigned int)((unsigned int)(a9));
    if (((256) & ((unsigned int)((unsigned int)(a4)))) == 0) goto loc_005922C7;
    if (((unsigned int)(v_r13)) <= ((unsigned int)((unsigned int)(0x2080ULL) + 80))) goto loc_005922C1;
    *(unsigned int *)(a2 + 20) = (unsigned int)((unsigned int)(0x2080ULL));
    v_rbp = (unsigned int)((v_rbp) | (256));
    goto loc_005922C7;
loc_005922C1:
    v_rdi = (unsigned int)(((unsigned int)(a9)) | (256));
    *(unsigned int *)(a2 + 68) = (unsigned int)(v_rdi);
loc_005922C7:
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) goto loc_005922E8;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) >= ((unsigned int)(v_r13))) goto loc_005922E2;
    *(unsigned int *)(a2 + 28) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)));
    v_rbp = (unsigned int)((v_rbp) | (4));
    goto loc_005922E8;
loc_005922E2:
    v_rdi = (unsigned int)((v_rdi) | (256));
    *(unsigned int *)(a2 + 68) = (unsigned int)(v_rdi);
loc_005922E8:
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) == 0) goto loc_00592309;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)) >= ((unsigned int)(v_r13))) goto loc_00592303;
    *(unsigned int *)(a2 + 32) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)));
    v_rbp = (unsigned int)((v_rbp) | (8));
    goto loc_00592309;
loc_00592303:
    v_rdi = (unsigned int)((v_rdi) | (256));
    *(unsigned int *)(a2 + 68) = (unsigned int)(v_rdi);
loc_00592309:
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) == 0) goto loc_0059232A;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) >= ((unsigned int)(v_r13))) goto loc_00592324;
    *(unsigned int *)(a2 + 36) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)));
    v_rbp = (unsigned int)((v_rbp) | (16));
    goto loc_0059232A;
loc_00592324:
    v_rdi = (unsigned int)((v_rdi) | (256));
    *(unsigned int *)(a2 + 68) = (unsigned int)(v_rdi);
loc_0059232A:
    if ((((unsigned __int8)((unsigned int)(a4))) & (32)) == 0) goto loc_0059241B;
    if (((*(unsigned int *)(a7 + 120)) & (0x20000ULL)) == 0) goto loc_0059241B;
    if ((*(unsigned __int64 *)(a7 + 48)) > (*(unsigned __int64 *)(a6 + 152))) goto loc_00592362;
    if ((*(unsigned __int64 *)(a6 + 152)) < (*(unsigned __int64 *)(a7 + 56))) goto loc_005923C2;
loc_00592362:
    if ((((unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 14908)))) & (1)) == 0) goto loc_005923C2;
    if (a7 == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_005923C2;
    result = IopIsAddressRangeValid(80 + *(unsigned __int64 *)(gs_base + (0 + 14880)) * 1 - 80, 80, 256, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005923BA;
    if ((*(unsigned __int64 *)(a7 + 48)) > (*(unsigned __int64 *)(80 + *(unsigned __int64 *)(gs_base + (0 + 14880)) * 1 - 16))) goto loc_005923C2;
    v_rdi = *(unsigned __int64 *)(a7 + 48);
    if ((*(unsigned __int64 *)(80 + *(unsigned __int64 *)(gs_base + (0 + 14880)) * 1 - 16)) < (*(unsigned __int64 *)(a7 + 56))) { v_rdi = *(unsigned __int64 *)(80 + *(unsigned __int64 *)(gs_base + (0 + 14880)) * 1 - 16); }
    goto loc_005923C2;
loc_005923BA:
loc_005923C2:
    result = (*(unsigned __int64 *)(a7 + 56)) - (v_rdi);
    if (result >= ((unsigned int)(0x7FFFULL))) goto loc_005923D7;
    v_r14 = (unsigned int)((*(unsigned __int64 *)(a7 + 56)) - ((unsigned int)(v_rdi)));
    goto loc_005923DA;
loc_005923D7:
loc_005923DA:
    result = IopGetMaxValidMemorySize(v_rdi, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x7FFFULL))))), 256, a4);
    if ((unsigned int)(result) == 0) goto loc_0059241B;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) + result * 1)) >= ((unsigned int)(v_r13))) goto loc_00592417;
    *(unsigned int *)(a2 + 40) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) + result * 1 + 7) & (0xFFFFFFF8ULL));
    *(unsigned int *)(a2 + 44) = (unsigned int)(result);
    v_rbp = (unsigned int)((v_rbp) | (32));
    *(unsigned __int64 *)(a2 + 72) = v_rdi;
    goto loc_0059241B;
loc_00592417:
loc_0059241B:
    if ((((unsigned int)((unsigned int)(0x400ULL))) & ((unsigned int)((unsigned int)(v_stack_p20)))) == 0) goto loc_00592449;
    result = ((unsigned int)((unsigned int)(v_rsi))) + ((unsigned int)(0x400ULL) - 96);
    if (result >= ((unsigned int)((unsigned int)(v_r13)))) goto loc_00592445;
    *(unsigned int *)(a2 + 112) = (unsigned int)(v_rsi);
    v_rsi = (unsigned int)((v_rsi) + (935));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFF8ULL));
    *(unsigned int *)(a2 + 116) = (unsigned int)((unsigned int)(0x400ULL) - 96);
    v_rbp = (unsigned int)((v_rbp) | ((unsigned int)((unsigned int)(0x400ULL))));
    goto loc_00592449;
loc_00592445:
loc_00592449:
    if ((unsigned __int8)(v_stack_p18) == 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = v_rip + 9842811;
        a2 = 1;
        result = ExAcquireResourceSharedLite(a1, a2, 256, a4);
    }
    result = -(*(unsigned __int64 *)(v_rip + 9842741));
    a1 = (unsigned int)((a1) & (0xAF0ULL));
    result = (unsigned int)((a1 + 8) + ((unsigned int)(v_rsi)));
    if (((unsigned int)(result)) >= ((unsigned int)(v_r13))) goto loc_005924A4;
    v_rbp = (unsigned int)((v_rbp) | (64));
    *(unsigned int *)(a2 + 24) = (unsigned int)(v_rsi);
    a1 = ((unsigned int)((unsigned int)(v_rsi))) + (a2 - 8192);
    result = MmWriteUnloadedDriverInformation(a1, a2, 256, a4);
    goto loc_005924A9;
loc_005924A4:
loc_005924A9:
    if ((((unsigned __int8)((unsigned int)(v_stack_p20))) & (64)) == 0) goto loc_005924F9;
    result = IoGetLoadedDriverInfo(a1, v_stack_p8, v_stack_m48, a4);
    v_stack_p40 = (unsigned int)(result);
    if (sign_flag) goto loc_005924F9;
    a1 = (unsigned int)(((unsigned int)(v_stack_p8) + (unsigned int)(v_stack_p8) * 8) << (4));
    if (a1 == 0) goto loc_005924F9;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + a1 * 1)) >= ((unsigned int)(v_r13))) goto loc_005924F4;
    *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_rbp = (unsigned int)((v_rbp) | (64));
    *(unsigned int *)(a2 + 52) = (unsigned int)((unsigned int)(v_stack_p8));
    goto loc_005924F9;
loc_005924F4:
loc_005924F9:
    a2 = (unsigned int)(((unsigned int)(v_stack_p8) + (unsigned int)(v_stack_p8) * 2 * 2 + 7) + (v_stack_m48));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    if (condition_is_equal) goto loc_00592531;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + a1 * 1)) + a2 * 1)) >= ((unsigned int)(v_r13))) goto loc_0059252C;
    *(unsigned int *)(a2 + 56) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + a1 * 1)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + a1 * 1)) + a2 * 1 + 7) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned int *)(a2 + 60) = (unsigned int)(a2);
    goto loc_00592531;
loc_0059252C:
loc_00592531:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))) == 0) goto loc_0059255A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56))) == 0) goto loc_0059255A;
    result = IopWriteDriverList(a2 - 8192, a2, (unsigned int)(*(unsigned int *)(a2 + 48)), (unsigned int)(*(unsigned int *)(a2 + 56)));
    v_stack_p40 = (unsigned int)(result);
    if (sign_flag) {
    }
    if ((unsigned __int8)(v_stack_p18) == 0) {
        a1 = v_rip + 9842554;
        result = ExReleaseResourceLite(a1, a2, (unsigned int)(*(unsigned int *)(a2 + 48)), (unsigned int)(*(unsigned int *)(a2 + 56)));
        result = KeLeaveCriticalRegion(a1, a2, (unsigned int)(*(unsigned int *)(a2 + 48)), (unsigned int)(*(unsigned int *)(a2 + 56)));
    }
    if (((v_stack_p20) & (0x800ULL)) == 0) goto loc_0059262A;
    result = ((unsigned int)(*(unsigned int *)(a2 + 44))) + (*(unsigned __int64 *)(a2 + 72));
    v_stack_m50 = result;
    v_stack_m58 = *(unsigned __int64 *)(a2 + 72);
    result = IopAddRunTimeTriageDataBlocks((unsigned int)((unsigned int)((unsigned int)(a10))), a11, a12, a6);
    a3 = 0;
loc_005925CD:
    if (0 >= ((unsigned int)((unsigned int)(a10)))) goto loc_0059261A;
    a4 = (0) + (0);
    a2 = 0;
loc_005925DF:
    if (0 >= (*(unsigned int *)(a11 + a4 * 8))) goto loc_00592610;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11 + a4 * 8 + 8) + 8))) - (*(unsigned int *)(*(unsigned __int64 *)(a11 + a4 * 8 + 8))));
    result = (unsigned int)((result) + (7));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (unsigned int)((result) + (16));
    result = (unsigned int)((result) + ((unsigned int)(v_rsi)));
    if (((unsigned int)(result)) >= ((unsigned int)(v_r13))) goto loc_00592615;
    if (0 == 0) {
        *(unsigned int *)(a2 + 120) = (unsigned int)(v_rsi);
    }
    a2 = (unsigned int)((a2) + 1);
    v_r10 = (*(unsigned __int64 *)(a11 + a4 * 8 + 8)) + (16);
    goto loc_005925DF;
loc_00592610:
    a3 = (unsigned int)((a3) + 1);
    goto loc_005925CD;
loc_00592615:
loc_0059261A:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) + (7));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    if ((*(unsigned int *)(a2 + 124)) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(a2 + 20));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 20))) != 0) {
        a1 = a2 - 8192 + (unsigned int)(*(unsigned int *)(a2 + 20)) * 1;
        result = MmWriteTriageInformation(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28))) == 0) goto loc_00592665;
    result = ((unsigned int)(*(unsigned int *)(a2 + 28))) + (0xCF00ULL);
    if (result <= ((unsigned int)((unsigned int)(v_r13)))) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 32));
        a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28))))) + (a2 - 8192);
        a3 = 0xCF00ULL;
        result = memcpy(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32))) == 0) goto loc_00592699;
    result = ((unsigned int)(*(unsigned int *)(a2 + 32))) + (0x840ULL);
    if (result > ((unsigned int)((unsigned int)(v_r13)))) goto loc_005926A1;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32))))) + (a2 - 8192);
    result = memcpy(a1, *(unsigned __int64 *)(a7 + 184), (unsigned int)(0x840ULL), a4);
    goto loc_005926A1;
loc_00592699:
loc_005926A1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36))) == 0) goto loc_005926C9;
    result = ((unsigned int)(*(unsigned int *)(a2 + 36))) + (0x798ULL);
    if (result <= ((unsigned int)((unsigned int)(v_r13)))) {
        a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36))))) + (a2 - 8192);
        a2 = a7;
        a3 = 0x798ULL;
        result = memcpy(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40))) == 0) goto loc_005926E9;
    result = (unsigned int)(*(unsigned int *)(a2 + 40)) + (unsigned int)(*(unsigned int *)(a2 + 44)) * 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)) + (unsigned int)(*(unsigned int *)(a2 + 44)) * 1)) <= ((unsigned int)(v_r13))) {
        a1 = ((unsigned int)(*(unsigned int *)(a2 + 40))) + (a2 - 8192);
        result = memcpy(a1, *(unsigned __int64 *)(a2 + 72), (unsigned int)(*(unsigned int *)(a2 + 44)), a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 112))) == 0) goto loc_00592708;
    result = ((unsigned int)(*(unsigned int *)(a2 + 112))) + (928);
    if (result <= ((unsigned int)((unsigned int)(v_r13)))) {
        a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 112))))) + (a2 - 8192);
        result = KdCopyDataBlock(a1, *(unsigned __int64 *)(a2 + 72), (unsigned int)(*(unsigned int *)(a2 + 44)), a4);
    }
    if ((unsigned int)((unsigned int)(a10)) != 0) {
        a4 = a2 - 8192;
        a3 = a11;
        a2 = (unsigned int)((unsigned int)(a10));
        a1 = a2;
        result = IopFillTriageDumpDataBlocks(a1, a2, a3, a4);
    }
    if (((unsigned int)(v_r13)) != 0x3DFFCULL) goto loc_0059273B;
    if (a13 != 0) goto loc_0059273B;
    goto loc_0059274B;
loc_0059273B:
    v_rsi = (unsigned int)(((unsigned int)(0x40000ULL)) + (4));
    if (a13 != 0) {
        result = v_rsi - 8192;
        *(unsigned int *)(a13) = (unsigned int)(result);
    }
    if (a5 != 0) {
        *(unsigned int *)(a5) = (unsigned int)(v_rbp);
    }
    *(unsigned int *)(a2 + 4) = (unsigned int)(v_rsi);
    *(unsigned int *)(a2 + 8) = (unsigned int)(v_rsi - 4);
    result = (v_rsi - 4) + (0xFFFFFFFFFFFFE000ULL);
    if (result > ((unsigned int)((unsigned int)(v_r13)))) goto loc_00592784;
    *(unsigned int *)((unsigned int)((unsigned int)(v_rsi - 4)) + a2 * 1 - 8192) = 0x44475254ULL;
    goto loc_00592789;
loc_00592784:
loc_00592789:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(0xC000009AULL);
}
```

## 5. (Beta) C Style

```c
int64_t IoFillTriageDumpBuffer(int32_t Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, uint32_t Arg8, uint32_t Arg9, uint32_t Arg10, void *Arg11, int64_t Arg12, int64_t Arg13)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p40;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (64);
    local_rbp = 0;
    *(uint32_t *)(local_rsp - 0x48) = 0;
    *(uint32_t *)(local_rsp + 0x8) = 0;
    v_stack_p40 = 0;
    if (Arg13 != 0) {
        *(uint32_t *)(Arg13) = 0;
    }
    if (Arg5 != 0) {
        *(uint32_t *)(Arg5) = 0;
    }
    if (((uint32_t)((uint32_t)(Arg1))) >= 132) goto loc_00592243;
    goto loc_00592789;
loc_00592243:
    Arg2 = 0;
    result = memset(0, Arg2, 128, Arg4);
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)((uint32_t)(Arg1) + 8192);
    local_r13 = (uint32_t)(((uint32_t)(Arg1)) + (-4));
    result = (uint32_t)(((uint32_t)(Arg1) + 8192) + (-4));
    *(uint32_t *)(arg2 + 0x8) = (uint32_t)(result);
    result = 0;
    *(uint32_t *)(local_r13 + arg2 * 1) = 0;
    *(uint32_t *)(arg2 + 0x40) = 0;
    result = -(Arg6);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA31FC7)));
    *(uint32_t *)(arg2 + 0xC) = 840;
    local_rbp = (uint32_t)(-(local_rbp));
    *(uint32_t *)(arg2 + 0x10) = 0xF00ULL;
    local_rbp = (uint32_t)((local_rbp) + (130));
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)((uint32_t)(Arg9));
    if (((256) & ((uint32_t)((uint32_t)(Arg4)))) == 0) goto loc_005922C7;
    if (((uint32_t)(local_r13)) <= ((uint32_t)((uint32_t)(0x2080ULL) + 80))) goto loc_005922C1;
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)((uint32_t)(0x2080ULL));
    local_rbp = (uint32_t)((local_rbp) | (256));
    goto loc_005922C7;
loc_005922C1:
    local_rdi = (uint32_t)(((uint32_t)(Arg9)) | (256));
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)(local_rdi);
loc_005922C7:
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) goto loc_005922E8;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) >= ((uint32_t)(local_r13))) goto loc_005922E2;
    *(uint32_t *)(arg2 + 0x1C) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)));
    local_rbp = (uint32_t)((local_rbp) | (4));
    goto loc_005922E8;
loc_005922E2:
    local_rdi = (uint32_t)((local_rdi) | (256));
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)(local_rdi);
loc_005922E8:
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) == 0) goto loc_00592309;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)) >= ((uint32_t)(local_r13))) goto loc_00592303;
    *(uint32_t *)(arg2 + 0x20) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)));
    local_rbp = (uint32_t)((local_rbp) | (8));
    goto loc_00592309;
loc_00592303:
    local_rdi = (uint32_t)((local_rdi) | (256));
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)(local_rdi);
loc_00592309:
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) == 0) goto loc_0059232A;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) >= ((uint32_t)(local_r13))) goto loc_00592324;
    *(uint32_t *)(arg2 + 0x24) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)));
    local_rbp = (uint32_t)((local_rbp) | (16));
    goto loc_0059232A;
loc_00592324:
    local_rdi = (uint32_t)((local_rdi) | (256));
    *(uint32_t *)(arg2 + 0x44) = (uint32_t)(local_rdi);
loc_0059232A:
    if ((((uint8_t)((uint32_t)(Arg4))) & (32)) == 0) goto loc_0059241B;
    if (((*(uint32_t *)(arg7 + 0x78)) & (0x20000ULL)) == 0) goto loc_0059241B;
    if ((*(uint64_t *)(arg7 + 0x30)) > (*(uint64_t *)(arg6 + 0x98))) goto loc_00592362;
    if ((*(uint64_t *)(arg6 + 0x98)) < (*(uint64_t *)(arg7 + 0x38))) goto loc_005923C2;
loc_00592362:
    if ((((uint8_t)(*(uint8_t *)(gs_base + (0 + 0x3A3C)))) & (1)) == 0) goto loc_005923C2;
    if (Arg7 == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_005923C2;
    result = IopIsAddressRangeValid(80 + *(uint64_t *)(gs_base + (0 + 0x3A20)) * 1 - 80, 80, 256, Arg4);
    if ((uint8_t)(result) == 0) goto loc_005923BA;
    if ((*(uint64_t *)(arg7 + 0x30)) > (*(uint64_t *)(80 + *(uint64_t *)(gs_base + (0 + 0x3A20)) * 1 - 0x10))) goto loc_005923C2;
    local_rdi = *(uint64_t *)(arg7 + 0x30);
    if ((*(uint64_t *)(80 + *(uint64_t *)(gs_base + (0 + 0x3A20)) * 1 - 0x10)) < (*(uint64_t *)(arg7 + 0x38))) { local_rdi = *(uint64_t *)(80 + *(uint64_t *)(gs_base + (0 + 0x3A20)) * 1 - 0x10); }
    goto loc_005923C2;
loc_005923BA:
loc_005923C2:
    result = (*(uint64_t *)(arg7 + 0x38)) - (local_rdi);
    if (result >= ((uint32_t)(0x7FFFULL))) goto loc_005923D7;
    local_r14 = (uint32_t)((*(uint64_t *)(arg7 + 0x38)) - ((uint32_t)(local_rdi)));
    goto loc_005923DA;
loc_005923D7:
loc_005923DA:
    result = IopGetMaxValidMemorySize(local_rdi, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x7FFFULL))))), 256, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0059241B;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) + result * 1)) >= ((uint32_t)(local_r13))) goto loc_00592417;
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x2080ULL) + 80)) + 52992)) + 2112)) + 1944)) + result * 1 + 7) & (0xFFFFFFF8ULL));
    *(uint32_t *)(arg2 + 0x2C) = (uint32_t)(result);
    local_rbp = (uint32_t)((local_rbp) | (32));
    *(uint64_t *)(arg2 + 0x48) = local_rdi;
    goto loc_0059241B;
loc_00592417:
loc_0059241B:
    if ((((uint32_t)((uint32_t)(0x400ULL))) & ((uint32_t)((uint32_t)(v_stack_p20)))) == 0) goto loc_00592449;
    result = ((uint32_t)((uint32_t)(local_rsi))) + ((uint32_t)(0x400ULL) - 96);
    if (result >= ((uint32_t)((uint32_t)(local_r13)))) goto loc_00592445;
    *(uint32_t *)(arg2 + 0x70) = (uint32_t)(local_rsi);
    local_rsi = (uint32_t)((local_rsi) + (935));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFF8ULL));
    *(uint32_t *)(arg2 + 0x74) = (uint32_t)((uint32_t)(0x400ULL) - 96);
    local_rbp = (uint32_t)((local_rbp) | ((uint32_t)((uint32_t)(0x400ULL))));
    goto loc_00592449;
loc_00592445:
loc_00592449:
    if ((uint8_t)(v_stack_p18) == 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = v_rip + 9842811;
        Arg2 = 1;
        result = ExAcquireResourceSharedLite(Arg1, Arg2, 256, Arg4);
    }
    result = -(*(uint64_t *)(v_rip + 0x963035));
    Arg1 = (uint32_t)((Arg1) & (0xAF0ULL));
    result = (uint32_t)((Arg1 + 8) + ((uint32_t)(local_rsi)));
    if (((uint32_t)(result)) >= ((uint32_t)(local_r13))) goto loc_005924A4;
    local_rbp = (uint32_t)((local_rbp) | (64));
    *(uint32_t *)(arg2 + 0x18) = (uint32_t)(local_rsi);
    Arg1 = ((uint32_t)((uint32_t)(local_rsi))) + (Arg2 - 8192);
    result = MmWriteUnloadedDriverInformation(Arg1, Arg2, 256, Arg4);
    goto loc_005924A9;
loc_005924A4:
loc_005924A9:
    if ((((uint8_t)((uint32_t)(v_stack_p20))) & (64)) == 0) goto loc_005924F9;
    result = IoGetLoadedDriverInfo(Arg1, v_stack_p8, v_stack_m48, Arg4);
    v_stack_p40 = (uint32_t)(result);
    if (sign_flag) goto loc_005924F9;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p8) + (uint32_t)(v_stack_p8) * 8) << (4));
    if (Arg1 == 0) goto loc_005924F9;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + Arg1 * 1)) >= ((uint32_t)(local_r13))) goto loc_005924F4;
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
    local_rbp = (uint32_t)((local_rbp) | (64));
    *(uint32_t *)(arg2 + 0x34) = (uint32_t)((uint32_t)(v_stack_p8));
    goto loc_005924F9;
loc_005924F4:
loc_005924F9:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p8) + (uint32_t)(v_stack_p8) * 2 * 2 + 7) + (v_stack_m48));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    if (condition_is_equal) goto loc_00592531;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + Arg1 * 1)) + Arg2 * 1)) >= ((uint32_t)(local_r13))) goto loc_0059252C;
    *(uint32_t *)(arg2 + 0x38) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + Arg1 * 1)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + Arg1 * 1)) + Arg2 * 1 + 7) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint32_t *)(arg2 + 0x3C) = (uint32_t)(Arg2);
    goto loc_00592531;
loc_0059252C:
loc_00592531:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))) == 0) goto loc_0059255A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38))) == 0) goto loc_0059255A;
    result = IopWriteDriverList(Arg2 - 8192, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), (uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    v_stack_p40 = (uint32_t)(result);
    if (sign_flag) {
    }
    if ((uint8_t)(v_stack_p18) == 0) {
        Arg1 = v_rip + 9842554;
        result = ExReleaseResourceLite(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), (uint32_t)(*(uint32_t *)(arg2 + 0x38)));
        result = KeLeaveCriticalRegion(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x30)), (uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    }
    if (((v_stack_p20) & (0x800ULL)) == 0) goto loc_0059262A;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x2C))) + (*(uint64_t *)(arg2 + 0x48));
    v_stack_m50 = result;
    v_stack_m58 = *(uint64_t *)(arg2 + 0x48);
    result = IopAddRunTimeTriageDataBlocks((uint32_t)((uint32_t)((uint32_t)(Arg10))), Arg11, Arg12, Arg6);
    Arg3 = 0;
loc_005925CD:
    if (0 >= ((uint32_t)((uint32_t)(Arg10)))) goto loc_0059261A;
    Arg4 = (0) + (0);
    Arg2 = 0;
loc_005925DF:
    if (0 >= (*(uint32_t *)(arg11 + Arg4 * 8))) goto loc_00592610;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg11 + Arg4 * 8 + 0x8) + 0x8))) - (*(uint32_t *)(*(uint64_t *)(arg11 + Arg4 * 8 + 0x8))));
    result = (uint32_t)((result) + (7));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (uint32_t)((result) + (16));
    result = (uint32_t)((result) + ((uint32_t)(local_rsi)));
    if (((uint32_t)(result)) >= ((uint32_t)(local_r13))) goto loc_00592615;
    if (0 == 0) {
        *(uint32_t *)(arg2 + 0x78) = (uint32_t)(local_rsi);
    }
    Arg2 = (uint32_t)((Arg2) + 1);
    local_r10 = (*(uint64_t *)(arg11 + Arg4 * 8 + 0x8)) + (16);
    goto loc_005925DF;
loc_00592610:
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_005925CD;
loc_00592615:
loc_0059261A:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) + (7));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    if ((*(uint32_t *)(arg2 + 0x7C)) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x14));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x14))) != 0) {
        Arg1 = Arg2 - 8192 + (uint32_t)(*(uint32_t *)(arg2 + 0x14)) * 1;
        result = MmWriteTriageInformation(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1C))) == 0) goto loc_00592665;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x1C))) + (0xCF00ULL);
    if (result <= ((uint32_t)((uint32_t)(local_r13)))) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1C))))) + (Arg2 - 8192);
        Arg3 = 0xCF00ULL;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))) == 0) goto loc_00592699;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x20))) + (0x840ULL);
    if (result > ((uint32_t)((uint32_t)(local_r13)))) goto loc_005926A1;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))))) + (Arg2 - 8192);
    result = memcpy(Arg1, *(uint64_t *)(arg7 + 0xB8), (uint32_t)(0x840ULL), Arg4);
    goto loc_005926A1;
loc_00592699:
loc_005926A1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24))) == 0) goto loc_005926C9;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x24))) + (0x798ULL);
    if (result <= ((uint32_t)((uint32_t)(local_r13)))) {
        Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24))))) + (Arg2 - 8192);
        Arg2 = Arg7;
        Arg3 = 0x798ULL;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28))) == 0) goto loc_005926E9;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x28)) + (uint32_t)(*(uint32_t *)(arg2 + 0x2C)) * 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)) + (uint32_t)(*(uint32_t *)(arg2 + 0x2C)) * 1)) <= ((uint32_t)(local_r13))) {
        Arg1 = ((uint32_t)(*(uint32_t *)(arg2 + 0x28))) + (Arg2 - 8192);
        result = memcpy(Arg1, *(uint64_t *)(arg2 + 0x48), (uint32_t)(*(uint32_t *)(arg2 + 0x2C)), Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))) == 0) goto loc_00592708;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x70))) + (928);
    if (result <= ((uint32_t)((uint32_t)(local_r13)))) {
        Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x70))))) + (Arg2 - 8192);
        result = KdCopyDataBlock(Arg1, *(uint64_t *)(arg2 + 0x48), (uint32_t)(*(uint32_t *)(arg2 + 0x2C)), Arg4);
    }
    if ((uint32_t)((uint32_t)(Arg10)) != 0) {
        Arg4 = Arg2 - 8192;
        Arg3 = Arg11;
        Arg2 = (uint32_t)((uint32_t)(Arg10));
        Arg1 = Arg2;
        result = IopFillTriageDumpDataBlocks(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)(local_r13)) != 0x3DFFCULL) goto loc_0059273B;
    if (Arg13 != 0) goto loc_0059273B;
    goto loc_0059274B;
loc_0059273B:
    local_rsi = (uint32_t)(((uint32_t)(0x40000ULL)) + (4));
    if (Arg13 != 0) {
        result = local_rsi - 8192;
        *(uint32_t *)(Arg13) = (uint32_t)(result);
    }
    if (Arg5 != 0) {
        *(uint32_t *)(Arg5) = (uint32_t)(local_rbp);
    }
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)(local_rsi);
    *(uint32_t *)(arg2 + 0x8) = (uint32_t)(local_rsi - 4);
    result = (local_rsi - 4) + (0xFFFFFFFFFFFFE000ULL);
    if (result > ((uint32_t)((uint32_t)(local_r13)))) goto loc_00592784;
    *(uint32_t *)((uint32_t)((uint32_t)(local_rsi - 0x4)) + arg2 * 1 - 0x2000) = 0x44475254ULL;
    goto loc_00592789;
loc_00592784:
loc_00592789:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(0xC000009AULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x2000` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |
| `Arg2` | `+ 0xC` | `32` | `W` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x14` | `32` | `R` |
| `Arg2` | `+ 0x14` | `32` | `W` |
| `Arg2` | `+ 0x18` | `32` | `W` |
| `Arg2` | `+ 0x1C` | `32` | `R` |
| `Arg2` | `+ 0x1C` | `32` | `W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x24` | `32` | `R` |
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x28` | `32` | `W` |
| `Arg2` | `+ 0x2C` | `32` | `R` |
| `Arg2` | `+ 0x2C` | `32` | `W` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R/W` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x34` | `32` | `W` |
| `Arg2` | `+ 0x38` | `32` | `R` |
| `Arg2` | `+ 0x38` | `32` | `W` |
| `Arg2` | `+ 0x3C` | `32` | `W` |
| `Arg2` | `+ 0x40` | `32` | `W` |
| `Arg2` | `+ 0x44` | `32` | `R/W` |
| `Arg2` | `+ 0x44` | `32` | `W` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `W` |

추가 오프셋 13개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005921CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
