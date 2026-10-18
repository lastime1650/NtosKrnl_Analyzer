# sub_0025EB5D

- RVA: `0x0025EB5D`–`0x0025EFE0` (길이 `1,155` bytes)
- VA: `0x000000014025EB5D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064150`
- 디코드: `280`개 명령, `1,155/1,155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0025EBC1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025EBDF` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0025EC35` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025EC54` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0025EC92` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0025ECAD` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x0025ECCA` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0025ECEA` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0025ED15` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0025ED32` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0025ED64` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025EDC1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0025EDF5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025EE15` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x0025EE43` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025EE80` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025EECC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0025EF16` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0025EF40` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025EC03` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0025EC23` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0025ED81` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0025EDD1` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0025EE07` → RVA `0x00F0DE58` (`.data`; read)
- `0x0025EF81` → RVA `0x00E0EB18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0025EC92` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0025EECC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0025EF16` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0025EF40` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **31**
  - `0x0025EB6A` → [sub_0025E5F6 + 0x27F](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EB76` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EB8A` → [sub_0025E5F6 + 0x4BC](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EB99` → [sub_0025E5F6 + 0x276](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EBF3` → [sub_0025D903 + 0x7F2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EC68` → [sub_0025E5F6 + 0x1D5](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EC7C` → [sub_0025D903 + 0x8D0](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025ECD3` → [sub_0025D903 + 0x179](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025ECFE` → [sub_0025D903 + 0x7F2](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025ED29` → [sub_0025E5F6 + 0x1D5](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025ED37` → [sub_0025D903 + 0x1F0](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025ED49` → [sub_0025D903 + 0xC62](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EDCB` → [sub_0025D903 + 0x195](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EE02` → [sub_0025D903 + 0x195](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EEA5` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EEFA` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF04` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF24` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF2E` → [sub_0025D903 + 0x788](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF4B` → [sub_0025D903 + 0x5EC](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF59` → [sub_0025D903 + 0xC21](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF67` → [sub_0025D903 + 0xC21](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF75` → [sub_0025D903 + 0xC24](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF89` → [sub_0025E5F6 + 0x3CD](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EF8F` → [sub_0025D903 + 0xC3F](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EF97` → [sub_0025D903 + 0xBB7](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EFA5` → [sub_0025D903 + 0xBD6](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EFB3` → [sub_0025D903 + 0xBD6](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EFC1` → [sub_0025D903 + 0xBD9](Unknown_function_0025D903.md) (`tail-transfer`)
  - `0x0025EFD5` → [sub_0025E5F6 + 0x508](Unknown_function_0025E5F6.md) (`tail-transfer`)
  - `0x0025EFDB` → [sub_0025D903 + 0xBF4](Unknown_function_0025D903.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025EB5D  41 83 FE 01                     cmp r14d, 1
0025EB61  B8 01 00 00 00                  mov eax, 1
0025EB66  44 0F 44 C8                     cmove r9d, eax
0025EB6A  E9 06 FD FF FF                  jmp 0x14025e875
0025EB6F  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0025EB73  48 39 19                        cmp qword ptr [rcx], rbx
0025EB76  0F 85 0F F5 FF FF               jne 0x14025e08b
0025EB7C  48 89 18                        mov qword ptr [rax], rbx
0025EB7F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0025EB83  48 89 01                        mov qword ptr [rcx], rax
0025EB86  48 89 43 08                     mov qword ptr [rbx + 8], rax
0025EB8A  E9 23 FF FF FF                  jmp 0x14025eab2
0025EB8F  41 3B C1                        cmp eax, r9d
0025EB92  45 8B F4                        mov r14d, r12d
0025EB95  44 0F 4F C8                     cmovg r9d, eax
0025EB99  E9 CE FC FF FF                  jmp 0x14025e86c
0025EB9E  48 8B 4B D8                     mov rcx, qword ptr [rbx - 0x28]
0025EBA2  48 85 C9                        test rcx, rcx
0025EBA5  75 51                           jne 0x14025ebf8
0025EBA7  48 85 C0                        test rax, rax
0025EBAA  0F 89 7E 01 00 00               jns 0x14025ed2e
0025EBB0  33 D2                           xor edx, edx
0025EBB2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025EBB7  44 8D 49 04                     lea r9d, [rcx + 4]
0025EBBB  4C 8B C3                        mov r8, rbx
0025EBBE  8D 4A 18                        lea ecx, [rdx + 0x18]
0025EBC1  E8 9A EA 29 00                  call 0x1404fd660
0025EBC6  CC                              int3
0025EBC7  3C 04                           cmp al, 4
0025EBC9  0F 84 09 01 00 00               je 0x14025ecd8
0025EBCF  48 8B D1                        mov rdx, rcx
0025EBD2  45 33 C9                        xor r9d, r9d
0025EBD5  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0025EBD9  41 B8 00 01 00 00               mov r8d, 0x100
0025EBDF  E8 EC 1A 0F 00                  call 0x1403506d0
0025EBE4  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0025EBE9  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0025EBEE  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0025EBF3  E9 FD F4 FF FF                  jmp 0x14025e0f5
0025EBF8  41 B9 03 00 00 00               mov r9d, 3
0025EBFE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0025EC03  4C 8D 15 F6 13 DA FF            lea r10, [rip - 0x25ec0a]
0025EC0A  4C 8B C3                        mov r8, rbx
0025EC0D  48 8D 43 D0                     lea rax, [rbx - 0x30]
0025EC11  48 C1 E8 08                     shr rax, 8
0025EC15  0F B6 D0                        movzx edx, al
0025EC18  41 8D 49 15                     lea ecx, [r9 + 0x15]
0025EC1C  0F B6 43 E8                     movzx eax, byte ptr [rbx - 0x18]
0025EC20  48 33 D0                        xor rdx, rax
0025EC23  0F B6 05 22 82 D6 00            movzx eax, byte ptr [rip + 0xd68222]
0025EC2A  48 33 D0                        xor rdx, rax
0025EC2D  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
0025EC35  E8 26 EA 29 00                  call 0x1404fd660
0025EC3A  CC                              int3
0025EC3B  80 F9 04                        cmp cl, 4
0025EC3E  0F 84 BF 00 00 00               je 0x14025ed03
0025EC44  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0025EC48  45 33 C9                        xor r9d, r9d
0025EC4B  41 B8 00 01 00 00               mov r8d, 0x100
0025EC51  48 8B D0                        mov rdx, rax
0025EC54  E8 77 1A 0F 00                  call 0x1403506d0
0025EC59  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0025EC5E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0025EC63  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0025EC68  E9 5E FB FF FF                  jmp 0x14025e7cb
0025EC6D  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0025EC71  48 89 77 20                     mov qword ptr [rdi + 0x20], rsi
0025EC75  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0025EC79  89 77 48                        mov dword ptr [rdi + 0x48], esi
0025EC7C  E9 52 F5 FF FF                  jmp 0x14025e1d3
0025EC81  BA 70 00 00 00                  mov edx, 0x70
0025EC86  41 B8 42 6F 6F 73               mov r8d, 0x736f6f42
0025EC8C  41 B6 01                        mov r14b, 1
0025EC8F  8D 4A D0                        lea ecx, [rdx - 0x30]
0025EC92  E8 59 34 92 00                  call 0x140b820f0
0025EC97  4C 8B E8                        mov r13, rax
0025EC9A  48 85 C0                        test rax, rax
0025EC9D  74 24                           je 0x14025ecc3
0025EC9F  45 33 C9                        xor r9d, r9d
0025ECA2  4C 8D 40 10                     lea r8, [rax + 0x10]
0025ECA6  41 8D 51 0A                     lea edx, [r9 + 0xa]
0025ECAA  8D 4A F7                        lea ecx, [rdx - 9]
0025ECAD  E8 3E B3 09 00                  call 0x1402f9ff0
0025ECB2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025ECBB  49 89 4D 60                     mov qword ptr [r13 + 0x60], rcx
0025ECBF  49 89 75 68                     mov qword ptr [r13 + 0x68], rsi
0025ECC3  48 8D 8B 10 06 00 00            lea rcx, [rbx + 0x610]
0025ECCA  E8 A1 97 FA FF                  call 0x140208470
0025ECCF  44 0F B6 F8                     movzx r15d, al
0025ECD3  E9 A4 ED FF FF                  jmp 0x14025da7c
0025ECD8  C6 41 11 05                     mov byte ptr [rcx + 0x11], 5
0025ECDC  4C 8B C1                        mov r8, rcx
0025ECDF  41 89 71 04                     mov dword ptr [r9 + 4], esi
0025ECE3  49 8B D1                        mov rdx, r9
0025ECE6  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0025ECEA  E8 61 8F FA FF                  call 0x140207c50
0025ECEF  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0025ECF4  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0025ECF9  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0025ECFE  E9 F2 F3 FF FF                  jmp 0x14025e0f5
0025ED03  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
0025ED07  4C 8B C0                        mov r8, rax
0025ED0A  41 89 71 04                     mov dword ptr [r9 + 4], esi
0025ED0E  49 8B D1                        mov rdx, r9
0025ED11  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0025ED15  E8 36 8F FA FF                  call 0x140207c50
0025ED1A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0025ED1F  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0025ED24  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0025ED29  E9 9D FA FF FF                  jmp 0x14025e7cb
0025ED2E  48 8D 4B D0                     lea rcx, [rbx - 0x30]
0025ED32  E8 5D 36 14 00                  call 0x1403a2394
0025ED37  E9 B7 ED FF FF                  jmp 0x14025daf3
0025ED3C  4C 39 77 50                     cmp qword ptr [rdi + 0x50], r14
0025ED40  75 4F                           jne 0x14025ed91
0025ED42  48 8D 5F 40                     lea rbx, [rdi + 0x40]
0025ED46  48 85 DB                        test rbx, rbx
0025ED49  0F 85 16 F8 FF FF               jne 0x14025e565
0025ED4F  33 F6                           xor esi, esi
0025ED51  45 33 C9                        xor r9d, r9d
0025ED54  4D 8B C6                        mov r8, r14
0025ED57  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025ED5C  48 8B D7                        mov rdx, rdi
0025ED5F  B9 E3 00 00 00                  mov ecx, 0xe3
0025ED64  E8 F7 E8 29 00                  call 0x1404fd660
0025ED69  CC                              int3
0025ED6A  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
0025ED73  44 0F 20 C6                     mov rsi, cr8
0025ED77  41 BC 02 00 00 00               mov r12d, 2
0025ED7D  45 0F 22 C4                     mov cr8, r12
0025ED81  83 3D 98 7F D6 00 00            cmp dword ptr [rip + 0xd67f98], 0
0025ED88  75 2F                           jne 0x14025edb9
0025ED8A  48 8B 07                        mov rax, qword ptr [rdi]
0025ED8D  A8 01                           test al, 1
0025ED8F  75 AB                           jne 0x14025ed3c
0025ED91  49 8D 86 B8 06 00 00            lea rax, [r14 + 0x6b8]
0025ED98  48 8B 18                        mov rbx, qword ptr [rax]
0025ED9B  48 3B D8                        cmp rbx, rax
0025ED9E  74 AF                           je 0x14025ed4f
0025EDA0  0F B6 4B 25                     movzx ecx, byte ptr [rbx + 0x25]
0025EDA4  41 84 CC                        test r12b, cl
0025EDA7  75 0B                           jne 0x14025edb4
0025EDA9  48 39 7B 18                     cmp qword ptr [rbx + 0x18], rdi
0025EDAD  75 05                           jne 0x14025edb4
0025EDAF  F6 C1 01                        test cl, 1
0025EDB2  75 92                           jne 0x14025ed46
0025EDB4  48 8B 1B                        mov rbx, qword ptr [rbx]
0025EDB7  EB E2                           jmp 0x14025ed9b
0025EDB9  41 0F B6 D4                     movzx edx, r12b
0025EDBD  40 0F B6 CE                     movzx ecx, sil
0025EDC1  E8 36 69 29 00                  call 0x1404f56fc
0025EDC6  EB C2                           jmp 0x14025ed8a
0025EDC8  45 84 F6                        test r14b, r14b
0025EDCB  0F 84 C7 EC FF FF               je 0x14025da98
0025EDD1  F6 05 2E 7D D6 00 01            test byte ptr [rip + 0xd67d2e], 1
0025EDD8  48 8D 8B 10 06 00 00            lea rcx, [rbx + 0x610]
0025EDDF  75 26                           jne 0x14025ee07
0025EDE1  F0 48 21 31                     lock and qword ptr [rcx], rsi
0025EDE5  39 35 35 7F D6 00               cmp dword ptr [rip + 0xd67f35], esi
0025EDEB  74 0D                           je 0x14025edfa
0025EDED  44 0F 20 C1                     mov rcx, cr8
0025EDF1  41 0F B6 D7                     movzx edx, r15b
0025EDF5  E8 9E 68 29 00                  call 0x1404f5698
0025EDFA  41 0F B6 C7                     movzx eax, r15b
0025EDFE  44 0F 22 C0                     mov cr8, rax
0025EE02  E9 91 EC FF FF                  jmp 0x14025da98
0025EE07  8B 05 4B F0 CA 00               mov eax, dword ptr [rip + 0xcaf04b]
0025EE0D  85 C0                           test eax, eax
0025EE0F  75 D0                           jne 0x14025ede1
0025EE11  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025EE15  E8 D6 40 13 00                  call 0x140392ef0
0025EE1A  EB C9                           jmp 0x14025ede5
0025EE1C  44 0F 20 C0                     mov rax, cr8
0025EE20  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025EE29  3C 02                           cmp al, 2
0025EE2B  76 1C                           jbe 0x14025ee49
0025EE2D  33 F6                           xor esi, esi
0025EE2F  44 0F B6 C0                     movzx r8d, al
0025EE33  33 D2                           xor edx, edx
0025EE35  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025EE3A  B9 C6 01 00 00                  mov ecx, 0x1c6
0025EE3F  44 8D 4E 02                     lea r9d, [rsi + 2]
0025EE43  E8 18 E8 29 00                  call 0x1404fd660
0025EE48  CC                              int3
0025EE49  3C 01                           cmp al, 1
0025EE4B  0F 83 19 FF FF FF               jae 0x14025ed6a
0025EE51  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
0025EE58  0F 85 0C FF FF FF               jne 0x14025ed6a
0025EE5E  83 B9 E4 01 00 00 00            cmp dword ptr [rcx + 0x1e4], 0
0025EE65  0F 85 FF FE FF FF               jne 0x14025ed6a
0025EE6B  33 F6                           xor esi, esi
0025EE6D  45 33 C9                        xor r9d, r9d
0025EE70  45 33 C0                        xor r8d, r8d
0025EE73  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025EE78  B9 C6 01 00 00                  mov ecx, 0x1c6
0025EE7D  8D 56 07                        lea edx, [rsi + 7]
0025EE80  E8 DB E7 29 00                  call 0x1404fd660
0025EE85  CC                              int3
0025EE86  39 B3 E0 05 00 00               cmp dword ptr [rbx + 0x5e0], esi
0025EE8C  74 31                           je 0x14025eebf
0025EE8E  4D 85 ED                        test r13, r13
0025EE91  0F 84 3A FF FF FF               je 0x14025edd1
0025EE97  48 8D 83 00 06 00 00            lea rax, [rbx + 0x600]
0025EE9E  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0025EEA2  48 39 01                        cmp qword ptr [rcx], rax
0025EEA5  0F 85 E0 F1 FF FF               jne 0x14025e08b
0025EEAB  49 89 45 00                     mov qword ptr [r13], rax
0025EEAF  49 89 4D 08                     mov qword ptr [r13 + 8], rcx
0025EEB3  4C 89 29                        mov qword ptr [rcx], r13
0025EEB6  4C 89 68 08                     mov qword ptr [rax + 8], r13
0025EEBA  E9 12 FF FF FF                  jmp 0x14025edd1
0025EEBF  4D 85 ED                        test r13, r13
0025EEC2  74 0D                           je 0x14025eed1
0025EEC4  BA 42 6F 6F 73                  mov edx, 0x736f6f42
0025EEC9  49 8B CD                        mov rcx, r13
0025EECC  E8 9F 39 92 00                  call 0x140b82870
0025EED1  4C 8D B3 F0 05 00 00            lea r14, [rbx + 0x5f0]
0025EED8  49 8B 0E                        mov rcx, qword ptr [r14]
0025EEDB  49 3B CE                        cmp rcx, r14
0025EEDE  75 3D                           jne 0x14025ef1d
0025EEE0  4C 8D B3 00 06 00 00            lea r14, [rbx + 0x600]
0025EEE7  49 8B 0E                        mov rcx, qword ptr [r14]
0025EEEA  49 3B CE                        cmp rcx, r14
0025EEED  0F 84 DE FE FF FF               je 0x14025edd1
0025EEF3  48 8B 01                        mov rax, qword ptr [rcx]
0025EEF6  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
0025EEFA  0F 85 8B F1 FF FF               jne 0x14025e08b
0025EF00  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0025EF04  0F 85 81 F1 FF FF               jne 0x14025e08b
0025EF0A  49 89 06                        mov qword ptr [r14], rax
0025EF0D  BA 42 6F 6F 73                  mov edx, 0x736f6f42
0025EF12  4C 89 70 08                     mov qword ptr [rax + 8], r14
0025EF16  E8 55 39 92 00                  call 0x140b82870
0025EF1B  EB CA                           jmp 0x14025eee7
0025EF1D  48 8B 01                        mov rax, qword ptr [rcx]
0025EF20  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
0025EF24  0F 85 61 F1 FF FF               jne 0x14025e08b
0025EF2A  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0025EF2E  0F 85 57 F1 FF FF               jne 0x14025e08b
0025EF34  49 89 06                        mov qword ptr [r14], rax
0025EF37  BA 42 6F 6F 73                  mov edx, 0x736f6f42
0025EF3C  4C 89 70 08                     mov qword ptr [rax + 8], r14
0025EF40  E8 2B 39 92 00                  call 0x140b82870
0025EF45  EB 91                           jmp 0x14025eed8
0025EF47  44 89 6B 24                     mov dword ptr [rbx + 0x24], r13d
0025EF4B  E9 9F EF FF FF                  jmp 0x14025deef
0025EF50  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
0025EF55  66 39 4B 18                     cmp word ptr [rbx + 0x18], cx
0025EF59  0F 85 C5 F5 FF FF               jne 0x14025e524
0025EF5F  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
0025EF64  38 4B 1A                        cmp byte ptr [rbx + 0x1a], cl
0025EF67  0F 85 B7 F5 FF FF               jne 0x14025e524
0025EF6D  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0025EF72  4C 2B C8                        sub r9, rax
0025EF75  E9 AD F5 FF FF                  jmp 0x14025e527
0025EF7A  33 D2                           xor edx, edx
0025EF7C  41 8B C2                        mov eax, r10d
0025EF7F  2B C1                           sub eax, ecx
0025EF81  F7 35 91 FB BA 00               div dword ptr [rip + 0xbafb91]
0025EF87  85 D2                           test edx, edx
0025EF89  0F 84 34 FA FF FF               je 0x14025e9c3
0025EF8F  E9 AE F5 FF FF                  jmp 0x14025e542
0025EF94  89 43 24                        mov dword ptr [rbx + 0x24], eax
0025EF97  E9 1E F5 FF FF                  jmp 0x14025e4ba
0025EF9C  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
0025EFA1  66 39 4B 18                     cmp word ptr [rbx + 0x18], cx
0025EFA5  0F 85 2E F5 FF FF               jne 0x14025e4d9
0025EFAB  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
0025EFB0  38 4B 1A                        cmp byte ptr [rbx + 0x1a], cl
0025EFB3  0F 85 20 F5 FF FF               jne 0x14025e4d9
0025EFB9  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0025EFBE  4C 2B C8                        sub r9, rax
0025EFC1  E9 16 F5 FF FF                  jmp 0x14025e4dc
0025EFC6  33 D2                           xor edx, edx
0025EFC8  41 8B C2                        mov eax, r10d
0025EFCB  2B C1                           sub eax, ecx
0025EFCD  F7 35 45 FB BA 00               div dword ptr [rip + 0xbafb45]
0025EFD3  85 D2                           test edx, edx
0025EFD5  0F 84 23 FB FF FF               je 0x14025eafe
0025EFDB  E9 17 F5 FF FF                  jmp 0x14025e4f7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025EB5D(__int64 a1, int a2)
{
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int16 v_stack_p40;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    if (((unsigned int)(v_r14)) == 1) { a4 = 1; }
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025EB5D(int64_t Arg1, int32_t Arg2)
{
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint16_t v_stack_p40;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    if (((uint32_t)(local_r14)) == 1) { a4 = 1; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025EB5D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
