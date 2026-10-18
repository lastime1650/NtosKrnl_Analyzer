# IopAllocateAndPopulateWriteIrp

- RVA: `0x004011F4`–`0x004015C0` (길이 `972` bytes)
- VA: `0x00000001404011F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A340`
- 디코드: `272`개 명령, `972/972` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00401238` → [IopResetEvent](../29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x0040124F` → [IopAllocateIrpExReturn](../20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x004012BE` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0040136A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0040137E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004013DE` → [IopAllocateMdl](../3F/IopAllocateMdl_function_003FF0B0.md) (function, `0x003FF0B0`)
- `0x0040140B` → [IopProbeAndLockPages](../47/IopProbeAndLockPages_function_00479708.md) (function, `0x00479708`)
- `0x004014C2` → [IopSetCopyInformationExtension](../44/IopSetCopyInformationExtension_function_00444EEC.md) (function, `0x00444EEC`)
- `0x004014CE` → [Feature_3741482297__private_IsEnabledDeviceUsageNoInline](../59/Feature_3741482297__private_IsEnabledDeviceUsageNoInline_function_00598A10.md) (function, `0x00598A10`)
- `0x004014F0` → [IopUnlockAndFreeMdl](../29/IopUnlockAndFreeMdl_function_0029F200.md) (function, `0x0029F200`)
- `0x00401552` → [IopExceptionCleanupEx](../../page/8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00401564` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0040157D` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0040158E` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004015B9` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [IopPopulateCopyWriteWorkerData](IopPopulateCopyWriteWorkerData_function_00400B48.md) at `0x00400BFC`
- [IopWriteFile](../../page/8E/IopWriteFile_function_008E9790.md) at `0x008E9893`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0040136A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00401552` → [IopExceptionCleanupEx](../../page/8A/IopExceptionCleanupEx_function_008AE5C8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004011F4  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
004011F9  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004011FE  53                              push rbx
004011FF  56                              push rsi
00401200  57                              push rdi
00401201  41 54                           push r12
00401203  41 55                           push r13
00401205  41 56                           push r14
00401207  41 57                           push r15
00401209  48 83 EC 30                     sub rsp, 0x30
0040120D  48 8B F9                        mov rdi, rcx
00401210  4C 8B E9                        mov r13, rcx
00401213  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0040121B  45 33 F6                        xor r14d, r14d
0040121E  45 8B FE                        mov r15d, r14d
00401221  4C 39 71 60                     cmp qword ptr [rcx + 0x60], r14
00401225  75 16                           jne 0x14040123d
00401227  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0040122B  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0040122E  A8 02                           test al, 2
00401230  74 06                           je 0x140401238
00401232  45 39 75 70                     cmp dword ptr [r13 + 0x70], r14d
00401236  7C 05                           jl 0x14040123d
00401238  E8 B3 C3 E9 FF                  call 0x14029d5f0
0040123D  48 8D 5F 09                     lea rbx, [rdi + 9]
00401241  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00401245  44 38 33                        cmp byte ptr [rbx], r14b
00401248  41 0F 94 C0                     sete r8b
0040124C  8A 51 4C                        mov dl, byte ptr [rcx + 0x4c]
0040124F  E8 CC 64 E0 FF                  call 0x140207720
00401254  48 8B F0                        mov rsi, rax
00401257  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0040125F  48 85 C0                        test rax, rax
00401262  75 0B                           jne 0x14040126f
00401264  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0040126A  E9 CA 02 00 00                  jmp 0x140401539
0040126F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00401273  48 89 86 C0 00 00 00            mov qword ptr [rsi + 0xc0], rax
0040127A  48 8B 07                        mov rax, qword ptr [rdi]
0040127D  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
00401284  4C 89 B6 A0 00 00 00            mov qword ptr [rsi + 0xa0], r14
0040128B  8A 47 08                        mov al, byte ptr [rdi + 8]
0040128E  88 46 40                        mov byte ptr [rsi + 0x40], al
00401291  44 88 76 41                     mov byte ptr [rsi + 0x41], r14b
00401295  44 88 76 44                     mov byte ptr [rsi + 0x44], r14b
00401299  4C 89 76 68                     mov qword ptr [rsi + 0x68], r14
0040129D  44 89 76 10                     mov dword ptr [rsi + 0x10], r14d
004012A1  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
004012A5  48 89 46 50                     mov qword ptr [rsi + 0x50], rax
004012A9  4C 8B 67 60                     mov r12, qword ptr [rdi + 0x60]
004012AD  4D 85 E4                        test r12, r12
004012B0  74 1C                           je 0x1404012ce
004012B2  48 8B 5F 68                     mov rbx, qword ptr [rdi + 0x68]
004012B6  BA 49 6F 52 49                  mov edx, 0x49526f49
004012BB  49 8B CC                        mov rcx, r12
004012BE  E8 4D F4 E0 FF                  call 0x140210710
004012C3  0F BA 6E 10 15                  bts dword ptr [rsi + 0x10], 0x15
004012C8  48 89 5E 48                     mov qword ptr [rsi + 0x48], rbx
004012CC  EB 14                           jmp 0x1404012e2
004012CE  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
004012D2  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
004012D6  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
004012DA  48 89 46 58                     mov qword ptr [rsi + 0x58], rax
004012DE  4C 8B 67 30                     mov r12, qword ptr [rdi + 0x30]
004012E2  4C 89 66 60                     mov qword ptr [rsi + 0x60], r12
004012E6  48 8B 9E B8 00 00 00            mov rbx, qword ptr [rsi + 0xb8]
004012ED  C7 43 B8 04 00 00 00            mov dword ptr [rbx - 0x48], 4
004012F4  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
004012F8  48 89 43 E8                     mov qword ptr [rbx - 0x18], rax
004012FC  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00401300  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
00401303  41 BC 10 00 00 00               mov r12d, 0x10
00401309  41 84 CC                        test r12b, cl
0040130C  75 07                           jne 0x140401315
0040130E  8B 47 70                        mov eax, dword ptr [rdi + 0x70]
00401311  A8 01                           test al, 1
00401313  74 04                           je 0x140401319
00401315  C6 43 BA 04                     mov byte ptr [rbx - 0x46], 4
00401319  4C 89 76 18                     mov qword ptr [rsi + 0x18], r14
0040131D  4C 89 76 08                     mov qword ptr [rsi + 8], r14
00401321  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00401325  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00401328  F6 C1 04                        test cl, 4
0040132B  0F 84 89 00 00 00               je 0x1404013ba
00401331  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00401334  85 C0                           test eax, eax
00401336  74 79                           je 0x1404013b1
00401338  4C 39 B7 80 00 00 00            cmp qword ptr [rdi + 0x80], r14
0040133F  74 1B                           je 0x14040135c
00401341  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00401345  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00401349  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
0040134C  41 0B C4                        or eax, r12d
0040134F  89 46 10                        mov dword ptr [rsi + 0x10], eax
00401352  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00401356  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
0040135A  EB 30                           jmp 0x14040138c
0040135C  48 8B D0                        mov rdx, rax
0040135F  B9 69 00 00 00                  mov ecx, 0x69
00401364  41 B8 49 6F 53 42               mov r8d, 0x42536f49
0040136A  E8 81 0D 78 00                  call 0x140b820f0
0040136F  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00401373  44 8B 47 48                     mov r8d, dword ptr [rdi + 0x48]
00401377  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
0040137B  48 8B C8                        mov rcx, rax
0040137E  E8 BD 54 2C 00                  call 0x1406c6840
00401383  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00401386  83 C8 30                        or eax, 0x30
00401389  89 46 10                        mov dword ptr [rsi + 0x10], eax
0040138C  E9 D0 00 00 00                  jmp 0x140401461
00401391  44 8B F8                        mov r15d, eax
00401394  45 33 F6                        xor r14d, r14d
00401397  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0040139C  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
004013A4  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
004013AC  E9 7F 01 00 00                  jmp 0x140401530
004013B1  44 09 66 10                     or dword ptr [rsi + 0x10], r12d
004013B5  E9 A7 00 00 00                  jmp 0x140401461
004013BA  41 84 CC                        test r12b, cl
004013BD  74 73                           je 0x140401432
004013BF  8B 57 48                        mov edx, dword ptr [rdi + 0x48]
004013C2  85 D2                           test edx, edx
004013C4  0F 84 97 00 00 00               je 0x140401461
004013CA  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
004013CE  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
004013D3  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
004013D8  41 B1 01                        mov r9b, 1
004013DB  45 33 C0                        xor r8d, r8d
004013DE  E8 CD DC FF FF                  call 0x1403ff0b0
004013E3  48 85 C0                        test rax, rax
004013E6  0F 84 C8 01 00 00               je 0x1404015b4
004013EC  0F B6 4B B8                     movzx ecx, byte ptr [rbx - 0x48]
004013F0  4C 8B 4F 18                     mov r9, qword ptr [rdi + 0x18]
004013F4  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
004013F8  48 8B C8                        mov rcx, rax
004013FB  4C 39 B7 80 00 00 00            cmp qword ptr [rdi + 0x80], r14
00401402  74 04                           je 0x140401408
00401404  33 D2                           xor edx, edx
00401406  EB 03                           jmp 0x14040140b
00401408  8A 57 08                        mov dl, byte ptr [rdi + 8]
0040140B  E8 F8 82 07 00                  call 0x140479708
00401410  EB 4F                           jmp 0x140401461
00401412  44 8B F8                        mov r15d, eax
00401415  45 33 F6                        xor r14d, r14d
00401418  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0040141D  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
00401425  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
0040142D  E9 FE 00 00 00                  jmp 0x140401530
00401432  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00401436  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
0040143A  48 8B 47 78                     mov rax, qword ptr [rdi + 0x78]
0040143E  48 85 C0                        test rax, rax
00401441  74 1E                           je 0x140401461
00401443  48 8B 00                        mov rax, qword ptr [rax]
00401446  48 85 C0                        test rax, rax
00401449  74 16                           je 0x140401461
0040144B  48 89 46 08                     mov qword ptr [rsi + 8], rax
0040144F  48 8B 47 78                     mov rax, qword ptr [rdi + 0x78]
00401453  4C 89 30                        mov qword ptr [rax], r14
00401456  4C 39 77 60                     cmp qword ptr [rdi + 0x60], r14
0040145A  74 05                           je 0x140401461
0040145C  48 83 4E 60 01                  or qword ptr [rsi + 0x60], 1
00401461  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
00401464  0F BA EA 09                     bts edx, 9
00401468  89 56 10                        mov dword ptr [rsi + 0x10], edx
0040146B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0040146F  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
00401472  F6 C1 08                        test cl, 8
00401475  74 06                           je 0x14040147d
00401477  83 CA 01                        or edx, 1
0040147A  89 56 10                        mov dword ptr [rsi + 0x10], edx
0040147D  44 38 77 0A                     cmp byte ptr [rdi + 0xa], r14b
00401481  74 07                           je 0x14040148a
00401483  0F BA EA 0B                     bts edx, 0xb
00401487  89 56 10                        mov dword ptr [rsi + 0x10], edx
0040148A  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0040148E  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
00401491  F6 C1 02                        test cl, 2
00401494  74 0D                           je 0x1404014a3
00401496  44 39 77 70                     cmp dword ptr [rdi + 0x70], r14d
0040149A  7D 07                           jge 0x1404014a3
0040149C  0F BA EA 0C                     bts edx, 0xc
004014A0  89 56 10                        mov dword ptr [rsi + 0x10], edx
004014A3  4C 39 B7 80 00 00 00            cmp qword ptr [rdi + 0x80], r14
004014AA  74 4F                           je 0x1404014fb
004014AC  44 88 76 40                     mov byte ptr [rsi + 0x40], r14b
004014B0  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
004014B4  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
004014B8  48 8B 97 80 00 00 00            mov rdx, qword ptr [rdi + 0x80]
004014BF  48 8B CE                        mov rcx, rsi
004014C2  E8 25 3A 04 00                  call 0x140444eec
004014C7  44 8B F8                        mov r15d, eax
004014CA  85 C0                           test eax, eax
004014CC  79 2D                           jns 0x1404014fb
004014CE  E8 3D 75 19 00                  call 0x140598a10
004014D3  85 C0                           test eax, eax
004014D5  74 59                           je 0x140401530
004014D7  4C 89 76 18                     mov qword ptr [rsi + 0x18], r14
004014DB  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004014DF  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
004014E2  41 84 D4                        test r12b, dl
004014E5  74 49                           je 0x140401530
004014E7  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
004014EB  48 85 C9                        test rcx, rcx
004014EE  74 40                           je 0x140401530
004014F0  E8 0B DD E9 FF                  call 0x14029f200
004014F5  4C 89 76 08                     mov qword ptr [rsi + 8], r14
004014F9  EB 35                           jmp 0x140401530
004014FB  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
004014FE  89 43 C0                        mov dword ptr [rbx - 0x40], eax
00401501  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
00401504  89 43 C8                        mov dword ptr [rbx - 0x38], eax
00401507  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
0040150B  48 89 43 D0                     mov qword ptr [rbx - 0x30], rax
0040150F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00401513  48 8B 80 D0 00 00 00            mov rax, qword ptr [rax + 0xd0]
0040151A  48 85 C0                        test rax, rax
0040151D  74 11                           je 0x140401530
0040151F  8B 00                           mov eax, dword ptr [rax]
00401521  41 84 C4                        test r12b, al
00401524  74 0A                           je 0x140401530
00401526  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0040152A  8B 48 08                        mov ecx, dword ptr [rax + 8]
0040152D  89 4B CC                        mov dword ptr [rbx - 0x34], ecx
00401530  45 85 FF                        test r15d, r15d
00401533  79 63                           jns 0x140401598
00401535  49 8D 5D 09                     lea rbx, [r13 + 9]
00401539  8A 03                           mov al, byte ptr [rbx]
0040153B  48 85 F6                        test rsi, rsi
0040153E  74 19                           je 0x140401559
00401540  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00401544  45 33 C9                        xor r9d, r9d
00401547  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
0040154B  48 8B D6                        mov rdx, rsi
0040154E  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00401552  E8 71 D0 4A 00                  call 0x1408ae5c8
00401557  EB 47                           jmp 0x1404015a0
00401559  84 C0                           test al, al
0040155B  74 0E                           je 0x14040156b
0040155D  48 8D 5F 10                     lea rbx, [rdi + 0x10]
00401561  48 8B 0B                        mov rcx, qword ptr [rbx]
00401564  E8 27 F5 E4 FF                  call 0x140250a90
00401569  EB 04                           jmp 0x14040156f
0040156B  49 8D 5D 10                     lea rbx, [r13 + 0x10]
0040156F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00401573  48 85 C9                        test rcx, rcx
00401576  74 0E                           je 0x140401586
00401578  BA 44 66 6C 74                  mov edx, 0x746c6644
0040157D  E8 5E 63 EF FF                  call 0x1402f78e0
00401582  4C 89 77 20                     mov qword ptr [rdi + 0x20], r14
00401586  BA 44 66 6C 74                  mov edx, 0x746c6644
0040158B  48 8B 0B                        mov rcx, qword ptr [rbx]
0040158E  E8 4D 63 EF FF                  call 0x1402f78e0
00401593  4C 89 33                        mov qword ptr [rbx], r14
00401596  EB 08                           jmp 0x1404015a0
00401598  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0040159D  48 89 30                        mov qword ptr [rax], rsi
004015A0  41 8B C7                        mov eax, r15d
004015A3  48 83 C4 30                     add rsp, 0x30
004015A7  41 5F                           pop r15
004015A9  41 5E                           pop r14
004015AB  41 5D                           pop r13
004015AD  41 5C                           pop r12
004015AF  5F                              pop rdi
004015B0  5E                              pop rsi
004015B1  5B                              pop rbx
004015B2  C3                              ret
004015B3  CC                              int3
004015B4  B9 9A 00 00 C0                  mov ecx, 0xc000009a
004015B9  E8 92 54 EF FF                  call 0x1402f6a50
004015BE  90                              nop
004015BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopAllocateAndPopulateWriteIrp(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    v_stack_p20 = a1;
    v_r14 = 0;
    if ((*(unsigned __int64 *)(a1 + 96)) != 0) goto loc_0040123D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) & (2)) == 0) goto loc_00401238;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80));
    if ((*(unsigned int *)(a1 + 112)) >= 0) {
        result = IopResetEvent(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    }
    a3 = ((*(unsigned __int8 *)(a1 + 9)) == 0) ? 1 : 0;
    result = IopAllocateIrpExReturn(*(unsigned __int64 *)(a1 + 24), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 76), a3, a4);
    v_stack_p18 = result;
    if (result != 0) goto loc_0040126F;
    goto loc_00401539;
loc_0040126F:
    *(unsigned __int64 *)(result + 192) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(result + 152) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 8));
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 80) = *(unsigned __int64 *)(a1 + 32);
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_004012CE;
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(a1 + 96), (unsigned int)(0x49526F49ULL), a3, a4);
    *(unsigned __int64 *)(result + 72) = *(unsigned __int64 *)(a1 + 104);
    goto loc_004012E2;
loc_004012CE:
    *(unsigned __int64 *)(result + 72) = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(a1 + 40);
loc_004012E2:
    *(unsigned __int64 *)(result + 96) = *(unsigned __int64 *)(a1 + 48);
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 72) = 4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = *(unsigned __int64 *)(a1 + 16);
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80))))) != 0) goto loc_00401315;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 112)))) & (1)) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = 4;
    }
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48)))) & (4)) == 0) goto loc_004013BA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72))) == 0) goto loc_004013B1;
    if ((*(unsigned __int64 *)(a1 + 128)) == 0) goto loc_0040135C;
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a1 + 64);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) | (16));
    *(unsigned int *)(result + 16) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a1 + 64);
    goto loc_0040138C;
loc_0040135C:
    result = ExAllocatePool2(105, *(unsigned __int64 *)(a1 + 64), (unsigned int)(0x42536F49ULL), a4);
    *(unsigned __int64 *)(result + 24) = result;
    result = memcpy(result, *(unsigned __int64 *)(a1 + 64), (unsigned int)(*(unsigned int *)(a1 + 72)), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) | (48));
    *(unsigned int *)(result + 16) = (unsigned int)(result);
loc_0040138C:
    goto loc_00401461;
loc_004013B1:
    goto loc_00401461;
loc_004013BA:
    if (((16) & ((unsigned __int8)(result))) == 0) goto loc_00401432;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72))) == 0) goto loc_00401461;
    v_stack_m40 = 0;
    v_stack_m48 = result;
    a3 = 0;
    result = IopAllocateMdl(*(unsigned __int64 *)(a1 + 64), (unsigned int)(*(unsigned int *)(a1 + 72)), a3, 1);
    if (result == 0) goto loc_004015B4;
    v_stack_m48 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72));
    if ((*(unsigned __int64 *)(a1 + 128)) == 0) goto loc_00401408;
    a2 = 0;
    goto loc_0040140B;
loc_00401408:
loc_0040140B:
    result = IopProbeAndLockPages(result, *(unsigned __int8 *)(a1 + 8), a3, *(unsigned __int64 *)(a1 + 24));
    goto loc_00401461;
loc_00401432:
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a1 + 64);
    if (*(unsigned __int64 *)(a1 + 120) == 0) goto loc_00401461;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120)) == 0) goto loc_00401461;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 120)) = 0;
    if ((*(unsigned __int64 *)(a1 + 96)) != 0) {
    }
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) & (8)) != 0) {
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) | (1));
        *(unsigned int *)(result + 16) = (unsigned int)(a2);
    }
    if ((*(unsigned __int8 *)(a1 + 10)) != 0) {
        *(unsigned int *)(result + 16) = (unsigned int)(a2);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 80)))) & (2)) == 0) goto loc_004014A3;
    if ((*(unsigned int *)(a1 + 112)) < 0) {
        *(unsigned int *)(result + 16) = (unsigned int)(a2);
    }
    if ((*(unsigned __int64 *)(a1 + 128)) == 0) goto loc_004014FB;
    *(unsigned __int8 *)(result + 64) = 0;
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a1 + 64);
    result = IopSetCopyInformationExtension(result, *(unsigned __int64 *)(a1 + 128), a3, *(unsigned __int64 *)(a1 + 24));
    if (!sign_flag) goto loc_004014FB;
    result = Feature_3741482297__private_IsEnabledDeviceUsageNoInline(result, *(unsigned __int64 *)(a1 + 128), a3, *(unsigned __int64 *)(a1 + 24));
    if ((unsigned int)(result) == 0) goto loc_00401530;
    *(unsigned __int64 *)(result + 24) = 0;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48))))) == 0) goto loc_00401530;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00401530;
    result = IopUnlockAndFreeMdl(*(unsigned __int64 *)(result + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48)), a3, *(unsigned __int64 *)(a1 + 24));
    *(unsigned __int64 *)(result + 8) = 0;
    goto loc_00401530;
loc_004014FB:
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 48) = *(unsigned __int64 *)(a1 + 80);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 208) == 0) goto loc_00401530;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 208)));
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 208)))))) != 0) {
        result = *(unsigned __int64 *)(a1 + 56);
        a1 = *(unsigned int *)(result + 8);
        *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 52) = (unsigned int)(a1);
    }
    if (!sign_flag) goto loc_00401598;
loc_00401539:
    if (result == 0) goto loc_00401559;
    v_stack_m48 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 9));
    a4 = 0;
    result = IopExceptionCleanupEx(*(unsigned __int64 *)(a1 + 16), result, *(unsigned __int64 *)(a1 + 32), a4);
    goto loc_004015A0;
loc_00401559:
    if ((unsigned __int8)(result) == 0) goto loc_0040156B;
    result = IopReleaseFileObjectLock(*(unsigned __int64 *)(a1 + 16), result, *(unsigned __int64 *)(a1 + 32), a4);
    goto loc_0040156F;
loc_0040156B:
loc_0040156F:
    if (*(unsigned __int64 *)(a1 + 32) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 32), a2, *(unsigned __int64 *)(a1 + 32), a4);
        *(unsigned __int64 *)(a1 + 32) = 0;
    }
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 16), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(a1 + 32), a4);
    *(unsigned __int64 *)(a1 + 16) = 0;
    goto loc_004015A0;
loc_00401598:
    *(unsigned __int64 *)(v_stack_p10) = result;
loc_004015A0:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_004015B4:
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(a1 + 32), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopAllocateAndPopulateWriteIrp(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsp;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    v_stack_p20 = Arg1;
    local_r14 = 0;
    if ((*(uint64_t *)(arg1 + 0x60)) != 0) goto loc_0040123D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) & (2)) == 0) goto loc_00401238;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50));
    if ((*(uint32_t *)(arg1 + 0x70)) >= 0) {
        result = IopResetEvent(*(uint64_t *)(arg1 + 0x10), Arg2, a3, a4);
    }
    a3 = ((*(uint8_t *)(arg1 + 0x9)) == 0) ? 1 : 0;
    result = IopAllocateIrpExReturn(*(uint64_t *)(arg1 + 0x18), *(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x4C), a3, a4);
    v_stack_p18 = result;
    if (result != 0) goto loc_0040126F;
    goto loc_00401539;
loc_0040126F:
    *(uint64_t *)(result + 0xC0) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(result + 0x98) = *(uint64_t *)(arg1);
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(*(uint8_t *)(arg1 + 0x8));
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x50) = *(uint64_t *)(arg1 + 0x20);
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_004012CE;
    result = ObfReferenceObjectWithTag(*(uint64_t *)(arg1 + 0x60), (uint32_t)(0x49526F49ULL), a3, a4);
    *(uint64_t *)(result + 0x48) = *(uint64_t *)(arg1 + 0x68);
    goto loc_004012E2;
loc_004012CE:
    *(uint64_t *)(result + 0x48) = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(arg1 + 0x28);
loc_004012E2:
    *(uint64_t *)(result + 0x60) = *(uint64_t *)(arg1 + 0x30);
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 4;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = *(uint64_t *)(arg1 + 0x10);
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50))))) != 0) goto loc_00401315;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)))) & (1)) != 0) {
        *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = 4;
    }
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30)))) & (4)) == 0) goto loc_004013BA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48))) == 0) goto loc_004013B1;
    if ((*(uint64_t *)(arg1 + 0x80)) == 0) goto loc_0040135C;
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(arg1 + 0x40);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) | (16));
    *(uint32_t *)(result + 0x10) = (uint32_t)(result);
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(arg1 + 0x40);
    goto loc_0040138C;
loc_0040135C:
    result = ExAllocatePool2(105, *(uint64_t *)(arg1 + 0x40), (uint32_t)(0x42536F49ULL), a4);
    *(uint64_t *)(result + 0x18) = result;
    result = memcpy(result, *(uint64_t *)(arg1 + 0x40), (uint32_t)(*(uint32_t *)(arg1 + 0x48)), a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) | (48));
    *(uint32_t *)(result + 0x10) = (uint32_t)(result);
loc_0040138C:
    goto loc_00401461;
loc_004013B1:
    goto loc_00401461;
loc_004013BA:
    if (((16) & ((uint8_t)(result))) == 0) goto loc_00401432;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48))) == 0) goto loc_00401461;
    v_stack_m40 = 0;
    v_stack_m48 = result;
    a3 = 0;
    result = IopAllocateMdl(*(uint64_t *)(arg1 + 0x40), (uint32_t)(*(uint32_t *)(arg1 + 0x48)), a3, 1);
    if (result == 0) goto loc_004015B4;
    v_stack_m48 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48));
    if ((*(uint64_t *)(arg1 + 0x80)) == 0) goto loc_00401408;
    Arg2 = 0;
    goto loc_0040140B;
loc_00401408:
loc_0040140B:
    result = IopProbeAndLockPages(result, *(uint8_t *)(arg1 + 0x8), a3, *(uint64_t *)(arg1 + 0x18));
    goto loc_00401461;
loc_00401432:
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(arg1 + 0x40);
    if (*(uint64_t *)(arg1 + 0x78) == 0) goto loc_00401461;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x78)) == 0) goto loc_00401461;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x78));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x78)) = 0;
    if ((*(uint64_t *)(arg1 + 0x60)) != 0) {
    }
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) & (8)) != 0) {
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) | (1));
        *(uint32_t *)(result + 0x10) = (uint32_t)(Arg2);
    }
    if ((*(uint8_t *)(arg1 + 0xA)) != 0) {
        *(uint32_t *)(result + 0x10) = (uint32_t)(Arg2);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x50)))) & (2)) == 0) goto loc_004014A3;
    if ((*(uint32_t *)(arg1 + 0x70)) < 0) {
        *(uint32_t *)(result + 0x10) = (uint32_t)(Arg2);
    }
    if ((*(uint64_t *)(arg1 + 0x80)) == 0) goto loc_004014FB;
    *(uint8_t *)(result + 0x40) = 0;
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(arg1 + 0x40);
    result = IopSetCopyInformationExtension(result, *(uint64_t *)(arg1 + 0x80), a3, *(uint64_t *)(arg1 + 0x18));
    if (!sign_flag) goto loc_004014FB;
    result = Feature_3741482297__private_IsEnabledDeviceUsageNoInline(result, *(uint64_t *)(arg1 + 0x80), a3, *(uint64_t *)(arg1 + 0x18));
    if ((uint32_t)(result) == 0) goto loc_00401530;
    *(uint64_t *)(result + 0x18) = 0;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30))))) == 0) goto loc_00401530;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00401530;
    result = IopUnlockAndFreeMdl(*(uint64_t *)(result + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30)), a3, *(uint64_t *)(arg1 + 0x18));
    *(uint64_t *)(result + 0x8) = 0;
    goto loc_00401530;
loc_004014FB:
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = *(uint64_t *)(arg1 + 0x50);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xD0) == 0) goto loc_00401530;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xD0)));
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0xD0)))))) != 0) {
        result = *(uint64_t *)(arg1 + 0x38);
        Arg1 = *(uint32_t *)(result + 0x8);
        *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x34) = (uint32_t)(Arg1);
    }
    if (!sign_flag) goto loc_00401598;
loc_00401539:
    if (result == 0) goto loc_00401559;
    v_stack_m48 = (uint8_t)(*(uint8_t *)(arg1 + 0x9));
    a4 = 0;
    result = IopExceptionCleanupEx(*(uint64_t *)(arg1 + 0x10), result, *(uint64_t *)(arg1 + 0x20), a4);
    goto loc_004015A0;
loc_00401559:
    if ((uint8_t)(result) == 0) goto loc_0040156B;
    result = IopReleaseFileObjectLock(*(uint64_t *)(arg1 + 0x10), result, *(uint64_t *)(arg1 + 0x20), a4);
    goto loc_0040156F;
loc_0040156B:
loc_0040156F:
    if (*(uint64_t *)(arg1 + 0x20) != 0) {
        Arg2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x20), Arg2, *(uint64_t *)(arg1 + 0x20), a4);
        *(uint64_t *)(arg1 + 0x20) = 0;
    }
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x10), (uint32_t)(0x746C6644ULL), *(uint64_t *)(arg1 + 0x20), a4);
    *(uint64_t *)(arg1 + 0x10) = 0;
    goto loc_004015A0;
loc_00401598:
    *(uint64_t *)(v_stack_p10) = result;
loc_004015A0:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_004015B4:
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), (uint32_t)(0x746C6644ULL), *(uint64_t *)(arg1 + 0x20), a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `64` | `R` |
| `Arg1` | `+ 0xA` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004011F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
