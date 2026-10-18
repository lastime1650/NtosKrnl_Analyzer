# MiCheckVirtualAddress

- RVA: `0x0032E4F0`–`0x0032E91C` (길이 `1,068` bytes)
- VA: `0x000000014032E4F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00076384`
- 디코드: `245`개 명령, `1,068/1,068` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0032E597` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x0032E6D2` → [MiGetProtoPteAddress](MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0032E708` → [MiVadExtentCommitted](MiVadExtentCommitted_function_0032E930.md) (function, `0x0032E930`)
- `0x0032E7A4` → [MiLockVadCore](../29/MiLockVadCore_function_00297170.md) (function, `0x00297170`)
- `0x0032E7B1` → [MiLocateLockedVadEvent](../2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0032E7D7` → [MiUnlockVadCore](../43/MiUnlockVadCore_function_004311C0.md) (function, `0x004311C0`)
- `0x0032E7F3` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0032E826` → [MiIsVadLargePrivate](MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x0032E8BB` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [MiTranslatePageForCopy](../22/MiTranslatePageForCopy_function_00228960.md) at `0x00228E3A`
- [sub_002B5C0F](../2B/Unknown_function_002B5C0F.md) at `0x002B5CB8`
- [MiIsFaultPteIntact](MiIsFaultPteIntact_function_003288A0.md) at `0x00328957`
- [MiFindActualFaultingPte](MiFindActualFaultingPte_function_0032899C.md) at `0x00328B16`
- [MiInPagePageTable](../3E/MiInPagePageTable_function_003EF8DC.md) at `0x003EF9C5`

### Static image references
- `0x0032E557` → RVA `0x00E2DB78` (`.data`; read)
- `0x0032E582` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0032E58B` → RVA `0x00F0DE58` (`.data`; read)
- `0x0032E73C` → RVA `0x00E2DB70` (`.data`; read)
- `0x0032E88D` → RVA `0x00E2DB68` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0032E7B9` → [sub_006E1EFA](../6E/Unknown_function_006E1EFA.md) (`tail-transfer`)
  - `0x0032E7CC` → [sub_006E1EFA](../6E/Unknown_function_006E1EFA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032E4F0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0032E4F5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0032E4FA  56                              push rsi
0032E4FB  57                              push rdi
0032E4FC  41 54                           push r12
0032E4FE  41 56                           push r14
0032E500  41 57                           push r15
0032E502  48 83 EC 20                     sub rsp, 0x20
0032E506  45 33 F6                        xor r14d, r14d
0032E509  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0032E513  4D 89 30                        mov qword ptr [r8], r14
0032E516  4D 8B F8                        mov r15, r8
0032E519  4C 8B E2                        mov r12, rdx
0032E51C  48 8B E9                        mov rbp, rcx
0032E51F  48 3B C8                        cmp rcx, rax
0032E522  0F 87 32 03 00 00               ja 0x14032e85a
0032E528  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032E531  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
0032E538  8B 82 FC 05 00 00               mov eax, dword ptr [rdx + 0x5fc]
0032E53E  A8 01                           test al, 1
0032E540  75 22                           jne 0x14032e564
0032E542  48 8B C1                        mov rax, rcx
0032E545  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032E54B  48 3D 00 00 FE 7F               cmp rax, 0x7ffe0000
0032E551  0F 84 36 03 00 00               je 0x14032e88d
0032E557  48 3B 05 1A F6 AF 00            cmp rax, qword ptr [rip + 0xaff61a]
0032E55E  0F 84 CF 01 00 00               je 0x14032e733
0032E564  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032E56D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032E574  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
0032E57B  48 81 C1 EC 03 00 00            add rcx, 0x3ec
0032E582  F6 05 7D 85 C9 00 21            test byte ptr [rip + 0xc9857d], 0x21
0032E589  74 13                           je 0x14032e59e
0032E58B  8B 05 C7 F8 BD 00               mov eax, dword ptr [rip + 0xbdf8c7]
0032E591  85 C0                           test eax, eax
0032E593  75 09                           jne 0x14032e59e
0032E595  B2 FF                           mov dl, 0xff
0032E597  E8 84 E7 F4 FF                  call 0x14027cd20
0032E59C  EB 16                           jmp 0x14032e5b4
0032E59E  0F 0D 09                        prefetchw byte ptr [rcx]
0032E5A1  8B 01                           mov eax, dword ptr [rcx]
0032E5A3  0F BA F0 1F                     btr eax, 0x1f
0032E5A7  8D 50 01                        lea edx, [rax + 1]
0032E5AA  F0 0F B1 11                     lock cmpxchg dword ptr [rcx], edx
0032E5AE  0F 85 35 02 00 00               jne 0x14032e7e9
0032E5B4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032E5BD  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
0032E5C4  48 8B 9A 60 05 00 00            mov rbx, qword ptr [rdx + 0x560]
0032E5CB  48 85 DB                        test rbx, rbx
0032E5CE  0F 84 79 01 00 00               je 0x14032e74d
0032E5D4  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
0032E5D8  48 8B FD                        mov rdi, rbp
0032E5DB  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0032E5DE  48 C1 E1 20                     shl rcx, 0x20
0032E5E2  48 0B C8                        or rcx, rax
0032E5E5  48 C1 EF 0C                     shr rdi, 0xc
0032E5E9  48 3B F9                        cmp rdi, rcx
0032E5EC  72 13                           jb 0x14032e601
0032E5EE  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
0032E5F2  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0032E5F5  48 C1 E1 20                     shl rcx, 0x20
0032E5F9  48 0B C8                        or rcx, rax
0032E5FC  48 3B F9                        cmp rdi, rcx
0032E5FF  76 54                           jbe 0x14032e655
0032E601  48 8B 9A 58 05 00 00            mov rbx, qword ptr [rdx + 0x558]
0032E608  48 85 DB                        test rbx, rbx
0032E60B  0F 84 3C 01 00 00               je 0x14032e74d
0032E611  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
0032E615  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0032E618  48 C1 E1 20                     shl rcx, 0x20
0032E61C  48 0B C8                        or rcx, rax
0032E61F  48 3B F9                        cmp rdi, rcx
0032E622  77 18                           ja 0x14032e63c
0032E624  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
0032E628  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0032E62B  48 C1 E1 20                     shl rcx, 0x20
0032E62F  48 0B C8                        or rcx, rax
0032E632  48 3B F9                        cmp rdi, rcx
0032E635  73 0E                           jae 0x14032e645
0032E637  48 8B 1B                        mov rbx, qword ptr [rbx]
0032E63A  EB 04                           jmp 0x14032e640
0032E63C  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
0032E640  48 85 DB                        test rbx, rbx
0032E643  75 CC                           jne 0x14032e611
0032E645  48 85 DB                        test rbx, rbx
0032E648  0F 84 FF 00 00 00               je 0x14032e74d
0032E64E  48 89 9A 60 05 00 00            mov qword ptr [rdx + 0x560], rbx
0032E655  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032E65E  48 8B F3                        mov rsi, rbx
0032E661  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032E668  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
0032E66E  A8 01                           test al, 1
0032E670  75 22                           jne 0x14032e694
0032E672  48 8B C5                        mov rax, rbp
0032E675  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032E67B  48 3D 00 00 FE 7F               cmp rax, 0x7ffe0000
0032E681  0F 84 48 02 00 00               je 0x14032e8cf
0032E687  48 3B 05 EA F4 AF 00            cmp rax, qword ptr [rip + 0xaff4ea]
0032E68E  0F 84 4F 02 00 00               je 0x14032e8e3
0032E694  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0032E697  A8 04                           test al, 4
0032E699  0F 85 3D 01 00 00               jne 0x14032e7dc
0032E69F  24 70                           and al, 0x70
0032E6A1  3C 20                           cmp al, 0x20
0032E6A3  0F 84 E8 00 00 00               je 0x14032e791
0032E6A9  8B 4B 30                        mov ecx, dword ptr [rbx + 0x30]
0032E6AC  0F BA E1 15                     bt ecx, 0x15
0032E6B0  0F 82 5D 01 00 00               jb 0x14032e813
0032E6B6  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
0032E6B9  A8 01                           test al, 1
0032E6BB  0F 85 3F 02 00 00               jne 0x14032e900
0032E6C1  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0032E6C6  41 B8 0C 00 00 00               mov r8d, 0xc
0032E6CC  48 8B D7                        mov rdx, rdi
0032E6CF  48 8B CB                        mov rcx, rbx
0032E6D2  E8 99 02 00 00                  call 0x14032e970
0032E6D7  4C 8B F0                        mov r14, rax
0032E6DA  41 BA 18 00 00 00               mov r10d, 0x18
0032E6E0  48 85 C0                        test rax, rax
0032E6E3  0F 84 2A 02 00 00               je 0x14032e913
0032E6E9  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0032E6EC  8B C8                           mov ecx, eax
0032E6EE  C1 E9 07                        shr ecx, 7
0032E6F1  24 70                           and al, 0x70
0032E6F3  83 E1 1F                        and ecx, 0x1f
0032E6F6  41 89 0C 24                     mov dword ptr [r12], ecx
0032E6FA  3C 20                           cmp al, 0x20
0032E6FC  0F 84 FB 00 00 00               je 0x14032e7fd
0032E702  48 8B D5                        mov rdx, rbp
0032E705  48 8B CB                        mov rcx, rbx
0032E708  E8 23 02 00 00                  call 0x14032e930
0032E70D  85 C0                           test eax, eax
0032E70F  0F 84 2D 01 00 00               je 0x14032e842
0032E715  49 89 1F                        mov qword ptr [r15], rbx
0032E718  49 8B C6                        mov rax, r14
0032E71B  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0032E720  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0032E725  48 83 C4 20                     add rsp, 0x20
0032E729  41 5F                           pop r15
0032E72B  41 5E                           pop r14
0032E72D  41 5C                           pop r12
0032E72F  5F                              pop rdi
0032E730  5E                              pop rsi
0032E731  C3                              ret
0032E732  CC                              int3
0032E733  48 85 C0                        test rax, rax
0032E736  0F 84 28 FE FF FF               je 0x14032e564
0032E73C  48 8B 05 2D F4 AF 00            mov rax, qword ptr [rip + 0xaff42d]
0032E743  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
0032E74B  EB CE                           jmp 0x14032e71b
0032E74D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032E756  F6 05 A9 83 C9 00 01            test byte ptr [rip + 0xc983a9], 1
0032E75D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032E764  4C 8B 81 10 04 00 00            mov r8, qword ptr [rcx + 0x410]
0032E76B  0F 85 30 01 00 00               jne 0x14032e8a1
0032E771  F0 41 81 A0 EC 03 00 00 FF FF FF BF  lock and dword ptr [r8 + 0x3ec], 0xbfffffff
0032E77D  F0 41 FF 88 EC 03 00 00         lock dec dword ptr [r8 + 0x3ec]
0032E785  41 C7 04 24 18 00 00 00         mov dword ptr [r12], 0x18
0032E78D  33 C0                           xor eax, eax
0032E78F  EB 8A                           jmp 0x14032e71b
0032E791  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
0032E794  A8 10                           test al, 0x10
0032E796  0F 84 0D FF FF FF               je 0x14032e6a9
0032E79C  BA 01 00 00 00                  mov edx, 1
0032E7A1  48 8B CB                        mov rcx, rbx
0032E7A4  E8 C7 89 F6 FF                  call 0x140297170
0032E7A9  BA 20 00 00 00                  mov edx, 0x20
0032E7AE  48 8B CB                        mov rcx, rbx
0032E7B1  E8 56 92 F7 FF                  call 0x1402a7a0c
0032E7B6  48 85 C0                        test rax, rax
0032E7B9  0F 84 3B 37 3B 00               je 0x1406e1efa
0032E7BF  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
0032E7C8  48 39 50 08                     cmp qword ptr [rax + 8], rdx
0032E7CC  0F 84 28 37 3B 00               je 0x1406e1efa
0032E7D2  B2 11                           mov dl, 0x11
0032E7D4  48 8B CE                        mov rcx, rsi
0032E7D7  E8 E4 29 10 00                  call 0x1404311c0
0032E7DC  41 C7 04 24 18 00 00 00         mov dword ptr [r12], 0x18
0032E7E4  E9 2C FF FF FF                  jmp 0x14032e715
0032E7E9  85 C0                           test eax, eax
0032E7EB  0F 89 B6 FD FF FF               jns 0x14032e5a7
0032E7F1  B2 FF                           mov dl, 0xff
0032E7F3  E8 88 3B 03 00                  call 0x140362380
0032E7F8  E9 B7 FD FF FF                  jmp 0x14032e5b4
0032E7FD  83 F9 07                        cmp ecx, 7
0032E800  0F 85 FC FE FF FF               jne 0x14032e702
0032E806  41 C7 04 24 00 01 00 00         mov dword ptr [r12], 0x100
0032E80E  E9 EF FE FF FF                  jmp 0x14032e702
0032E813  8B C1                           mov eax, ecx
0032E815  24 70                           and al, 0x70
0032E817  3C 10                           cmp al, 0x10
0032E819  74 30                           je 0x14032e84b
0032E81B  83 E1 70                        and ecx, 0x70
0032E81E  80 F9 30                        cmp cl, 0x30
0032E821  74 28                           je 0x14032e84b
0032E823  48 8B CB                        mov rcx, rbx
0032E826  E8 F5 0E 00 00                  call 0x14032f720
0032E82B  85 C0                           test eax, eax
0032E82D  75 1C                           jne 0x14032e84b
0032E82F  44 8B 53 30                     mov r10d, dword ptr [rbx + 0x30]
0032E833  41 0F BA E2 19                  bt r10d, 0x19
0032E838  73 11                           jae 0x14032e84b
0032E83A  41 C1 EA 07                     shr r10d, 7
0032E83E  41 83 E2 1F                     and r10d, 0x1f
0032E842  45 89 14 24                     mov dword ptr [r12], r10d
0032E846  E9 CA FE FF FF                  jmp 0x14032e715
0032E84B  41 BA 18 00 00 00               mov r10d, 0x18
0032E851  45 89 14 24                     mov dword ptr [r12], r10d
0032E855  E9 BB FE FF FF                  jmp 0x14032e715
0032E85A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032E864  48 3B E8                        cmp rbp, rax
0032E867  0F 82 18 FF FF FF               jb 0x14032e785
0032E86D  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0032E877  48 3B E8                        cmp rbp, rax
0032E87A  0F 87 05 FF FF FF               ja 0x14032e785
0032E880  C7 02 04 00 00 00               mov dword ptr [rdx], 4
0032E886  33 C0                           xor eax, eax
0032E888  E9 8E FE FF FF                  jmp 0x14032e71b
0032E88D  48 8B 05 D4 F2 AF 00            mov rax, qword ptr [rip + 0xaff2d4]
0032E894  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
0032E89C  E9 7A FE FF FF                  jmp 0x14032e71b
0032E8A1  8B 05 B1 F5 BD 00               mov eax, dword ptr [rip + 0xbdf5b1]
0032E8A7  85 C0                           test eax, eax
0032E8A9  0F 85 C2 FE FF FF               jne 0x14032e771
0032E8AF  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0032E8B4  49 8D 88 EC 03 00 00            lea rcx, [r8 + 0x3ec]
0032E8BB  E8 88 26 FC FF                  call 0x1402f0f48
0032E8C0  33 C0                           xor eax, eax
0032E8C2  41 C7 04 24 18 00 00 00         mov dword ptr [r12], 0x18
0032E8CA  E9 4C FE FF FF                  jmp 0x14032e71b
0032E8CF  4C 8B 35 92 F2 AF 00            mov r14, qword ptr [rip + 0xaff292]
0032E8D6  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
0032E8DE  E9 32 FE FF FF                  jmp 0x14032e715
0032E8E3  48 85 C0                        test rax, rax
0032E8E6  0F 84 A8 FD FF FF               je 0x14032e694
0032E8EC  4C 8B 35 7D F2 AF 00            mov r14, qword ptr [rip + 0xaff27d]
0032E8F3  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
0032E8FB  E9 15 FE FF FF                  jmp 0x14032e715
0032E900  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0032E903  83 E0 70                        and eax, 0x70
0032E906  3C 50                           cmp al, 0x50
0032E908  0F 85 CE FE FF FF               jne 0x14032e7dc
0032E90E  E9 AE FD FF FF                  jmp 0x14032e6c1
0032E913  45 89 14 24                     mov dword ptr [r12], r10d
0032E917  E9 E6 FD FF FF                  jmp 0x14032e702
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCheckVirtualAddress(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (32);
    v_r14 = 0;
    *(unsigned __int64 *)(a3) = 0;
    if (a1 > result) goto loc_0032E85A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)))) & (1)) != 0) goto loc_0032E564;
    result = (a1) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_0032E88D;
    if (result == (*(unsigned __int64 *)(v_rip + 11531802))) goto loc_0032E733;
loc_0032E564:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    if (((*(unsigned __int8 *)(v_rip + 13206909)) & (33)) == 0) goto loc_0032E59E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12449991))) != 0) goto loc_0032E59E;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(a1, 255, a3, a4);
    goto loc_0032E5B4;
loc_0032E59E:
loc_0032E5A7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12449991))) != 0) goto loc_0032E7E9;
loc_0032E5B4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) == 0) goto loc_0032E74D;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 24)));
    v_rdi = (a1) >> (12);
    if (v_rdi < a1) goto loc_0032E601;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 28)));
    if (v_rdi <= a1) goto loc_0032E655;
loc_0032E601:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) == 0) goto loc_0032E74D;
loc_0032E611:
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 28)));
    if (v_rdi > a1) goto loc_0032E63C;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 24)));
    if (v_rdi >= a1) goto loc_0032E645;
    goto loc_0032E640;
loc_0032E63C:
loc_0032E640:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) != 0) goto loc_0032E611;
loc_0032E645:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) == 0) goto loc_0032E74D;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8);
loc_0032E655:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)))) & (1)) != 0) goto loc_0032E694;
    result = (a1) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_0032E8CF;
    if (result == (*(unsigned __int64 *)(v_rip + 11531498))) goto loc_0032E8E3;
loc_0032E694:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48)))) & (4)) != 0) goto loc_0032E7DC;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))) & (112));
    if (((unsigned __int8)(result)) == 32) goto loc_0032E791;
loc_0032E6A9:
    if (((unsigned __int8)(result)) < 32) goto loc_0032E813;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 64)))) & (1)) != 0) goto loc_0032E900;
loc_0032E6C1:
    result = MiGetProtoPteAddress(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), v_rdi, 12, v_stack_p8);
    if (result == 0) goto loc_0032E913;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))))) >> (7));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))) & (112));
    a1 = (unsigned int)((a1) & (31));
    *(unsigned int *)(a2) = (unsigned int)(a1);
    if (((unsigned __int8)(result)) == 32) goto loc_0032E7FD;
loc_0032E702:
    result = MiVadExtentCommitted(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), a1, 12, v_stack_p8);
    if ((unsigned int)(result) == 0) goto loc_0032E842;
loc_0032E715:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8);
loc_0032E71B:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0032E733:
    if (result == 0) goto loc_0032E564;
    *(unsigned int *)(a2) = 1;
    goto loc_0032E71B;
loc_0032E74D:
    if (((*(unsigned __int8 *)(v_rip + 13206441)) & (1)) != 0) goto loc_0032E8A1;
loc_0032E771:
loc_0032E785:
    *(unsigned int *)(a2) = 24;
    result = 0;
    goto loc_0032E71B;
loc_0032E791:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 64)))) & (16)) == 0) goto loc_0032E6A9;
    result = MiLockVadCore(v_stack_p10, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
    result = MiLocateLockedVadEvent(v_stack_p10, 32, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
    result = MiUnlockVadCore(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), 17, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
loc_0032E7DC:
    *(unsigned int *)(a2) = 24;
    goto loc_0032E715;
loc_0032E7E9:
    if (!sign_flag) goto loc_0032E5A7;
    result = ExpWaitForSpinLockSharedAndAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), 255, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
    goto loc_0032E5B4;
loc_0032E7FD:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8))) != 7) goto loc_0032E702;
    *(unsigned int *)(a2) = 256;
    goto loc_0032E702;
loc_0032E813:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8)))) & (112));
    if (((unsigned __int8)(result)) == 16) goto loc_0032E84B;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8)) & (112));
    if (((unsigned __int8)(a1)) == 48) goto loc_0032E84B;
    result = MiIsVadLargePrivate(v_stack_p10, 255, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
    if ((unsigned int)(result) != 0) goto loc_0032E84B;
    if (condition_is_above_or_equal) goto loc_0032E84B;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 48))) >> (7));
    v_r10 = (unsigned int)((v_r10) & (31));
loc_0032E842:
    *(unsigned int *)(a2) = (unsigned int)(v_r10);
    goto loc_0032E715;
loc_0032E84B:
    *(unsigned int *)(a2) = 24;
    goto loc_0032E715;
loc_0032E85A:
    if (v_stack_p18 < result) goto loc_0032E785;
    if (v_stack_p18 > result) goto loc_0032E785;
    *(unsigned int *)(255) = 4;
    result = 0;
    goto loc_0032E71B;
loc_0032E88D:
    *(unsigned int *)(a2) = 1;
    goto loc_0032E71B;
loc_0032E8A1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12449201))) != 0) goto loc_0032E771;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1004, v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_stack_p8);
    result = 0;
    *(unsigned int *)(a2) = 24;
    goto loc_0032E71B;
loc_0032E8CF:
    *(unsigned int *)(a2) = 1;
    goto loc_0032E715;
loc_0032E8E3:
    if (0 == 0) goto loc_0032E694;
    *(unsigned int *)(a2) = 1;
    goto loc_0032E715;
loc_0032E900:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 48))) & (112));
    if (((unsigned __int8)(result)) != 80) goto loc_0032E7DC;
    goto loc_0032E6C1;
loc_0032E913:
    *(unsigned int *)(a2) = 24;
    goto loc_0032E702;
}
```

## 5. (Beta) C Style

```c
int64_t MiCheckVirtualAddress(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (32);
    local_r14 = 0;
    *(uint64_t *)(arg3) = 0;
    if (Arg1 > result) goto loc_0032E85A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)))) & (1)) != 0) goto loc_0032E564;
    result = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_0032E88D;
    if (result == (*(uint64_t *)(v_rip + 0xAFF61A))) goto loc_0032E733;
loc_0032E564:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    if (((*(uint8_t *)(v_rip + 0xC9857D)) & (33)) == 0) goto loc_0032E59E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDF8C7))) != 0) goto loc_0032E59E;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(Arg1, 255, Arg3, a4);
    goto loc_0032E5B4;
loc_0032E59E:
loc_0032E5A7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDF8C7))) != 0) goto loc_0032E7E9;
loc_0032E5B4:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) == 0) goto loc_0032E74D;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x18)));
    local_rdi = (Arg1) >> (12);
    if (local_rdi < Arg1) goto loc_0032E601;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x1C)));
    if (local_rdi <= Arg1) goto loc_0032E655;
loc_0032E601:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) == 0) goto loc_0032E74D;
loc_0032E611:
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x1C)));
    if (local_rdi > Arg1) goto loc_0032E63C;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x18)));
    if (local_rdi >= Arg1) goto loc_0032E645;
    goto loc_0032E640;
loc_0032E63C:
loc_0032E640:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) != 0) goto loc_0032E611;
loc_0032E645:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) == 0) goto loc_0032E74D;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8);
loc_0032E655:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)))) & (1)) != 0) goto loc_0032E694;
    result = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    if (result == 0x7FFE0000ULL) goto loc_0032E8CF;
    if (result == (*(uint64_t *)(v_rip + 0xAFF4EA))) goto loc_0032E8E3;
loc_0032E694:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30)))) & (4)) != 0) goto loc_0032E7DC;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))) & (112));
    if (((uint8_t)(result)) == 32) goto loc_0032E791;
loc_0032E6A9:
    if (((uint8_t)(result)) < 32) goto loc_0032E813;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x40)))) & (1)) != 0) goto loc_0032E900;
loc_0032E6C1:
    result = MiGetProtoPteAddress(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), local_rdi, 12, v_stack_p8);
    if (result == 0) goto loc_0032E913;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))))) >> (7));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))) & (112));
    Arg1 = (uint32_t)((Arg1) & (31));
    *(uint32_t *)(arg2) = (uint32_t)(Arg1);
    if (((uint8_t)(result)) == 32) goto loc_0032E7FD;
loc_0032E702:
    result = MiVadExtentCommitted(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), Arg1, 12, v_stack_p8);
    if ((uint32_t)(result) == 0) goto loc_0032E842;
loc_0032E715:
    *(uint64_t *)(arg3) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8);
loc_0032E71B:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0032E733:
    if (result == 0) goto loc_0032E564;
    *(uint32_t *)(arg2) = 1;
    goto loc_0032E71B;
loc_0032E74D:
    if (((*(uint8_t *)(v_rip + 0xC983A9)) & (1)) != 0) goto loc_0032E8A1;
loc_0032E771:
loc_0032E785:
    *(uint32_t *)(arg2) = 24;
    result = 0;
    goto loc_0032E71B;
loc_0032E791:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x40)))) & (16)) == 0) goto loc_0032E6A9;
    result = MiLockVadCore(v_stack_p10, 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
    result = MiLocateLockedVadEvent(v_stack_p10, 32, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
    result = MiUnlockVadCore(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), 17, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
loc_0032E7DC:
    *(uint32_t *)(arg2) = 24;
    goto loc_0032E715;
loc_0032E7E9:
    if (!sign_flag) goto loc_0032E5A7;
    result = ExpWaitForSpinLockSharedAndAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), 255, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
    goto loc_0032E5B4;
loc_0032E7FD:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8))) != 7) goto loc_0032E702;
    *(uint32_t *)(arg2) = 256;
    goto loc_0032E702;
loc_0032E813:
    result = (uint8_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8)))) & (112));
    if (((uint8_t)(result)) == 16) goto loc_0032E84B;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8)) & (112));
    if (((uint8_t)(Arg1)) == 48) goto loc_0032E84B;
    result = MiIsVadLargePrivate(v_stack_p10, 255, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
    if ((uint32_t)(result) != 0) goto loc_0032E84B;
    if (condition_is_above_or_equal) goto loc_0032E84B;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x30))) >> (7));
    local_r10 = (uint32_t)((local_r10) & (31));
loc_0032E842:
    *(uint32_t *)(arg2) = (uint32_t)(local_r10);
    goto loc_0032E715;
loc_0032E84B:
    *(uint32_t *)(arg2) = 24;
    goto loc_0032E715;
loc_0032E85A:
    if (v_stack_p18 < result) goto loc_0032E785;
    if (v_stack_p18 > result) goto loc_0032E785;
    *(uint32_t *)(255) = 4;
    result = 0;
    goto loc_0032E71B;
loc_0032E88D:
    *(uint32_t *)(arg2) = 1;
    goto loc_0032E71B;
loc_0032E8A1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDF5B1))) != 0) goto loc_0032E771;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 1004, v_stack_p48, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), v_stack_p8);
    result = 0;
    *(uint32_t *)(arg2) = 24;
    goto loc_0032E71B;
loc_0032E8CF:
    *(uint32_t *)(arg2) = 1;
    goto loc_0032E715;
loc_0032E8E3:
    if (0 == 0) goto loc_0032E694;
    *(uint32_t *)(arg2) = 1;
    goto loc_0032E715;
loc_0032E900:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x30))) & (112));
    if (((uint8_t)(result)) != 80) goto loc_0032E7DC;
    goto loc_0032E6C1;
loc_0032E913:
    *(uint32_t *)(arg2) = 24;
    goto loc_0032E702;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032E4F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
