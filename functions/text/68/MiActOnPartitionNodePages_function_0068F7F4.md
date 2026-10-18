# MiActOnPartitionNodePages

- RVA: `0x0068F7F4`–`0x00690117` (길이 `2,339` bytes)
- VA: `0x000000014068F7F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D90E4`
- 디코드: `646`개 명령, `2,339/2,339` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0068FAEF` → [MiFreePartitionPageRun](../69/MiFreePartitionPageRun_function_00690DA0.md) (function, `0x00690DA0`)
- `0x0068FB42` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x0068FB5B` → [MiSplitPfnBitMapsForPartitionHierarchy](../69/MiSplitPfnBitMapsForPartitionHierarchy_function_00691D64.md) (function, `0x00691D64`)
- `0x0068FBAC` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x0068FBBE` → [MiTransferPartitionPageRun](../69/MiTransferPartitionPageRun_function_00691DCC.md) (function, `0x00691DCC`)
- `0x0068FBE3` → [MiSetHugeRangePartitionId](../67/MiSetHugeRangePartitionId_function_006773E4.md) (function, `0x006773E4`)
- `0x0068FBFF` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x0068FC46` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0068FC66` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x0068FC89` → [MiMoveBadPageChargesCrossPartition](MiMoveBadPageChargesCrossPartition_function_00689F60.md) (function, `0x00689F60`)
- `0x0068FCD7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0068FCF0` → [MiUpdatePartitionChildPageCounts](../69/MiUpdatePartitionChildPageCounts_function_006921D4.md) (function, `0x006921D4`)
- `0x0068FD9E` → [RtlClearBitsEx](../29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)
- `0x0068FE9B` → [RtlAvlRemoveNode](../29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x0068FEEE` → [RtlAvlInsertNodeEx](../26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x0068FF55` → [MiHotAddHugeRange](../../page/7F/MiHotAddHugeRange_function_007FBF6C.md) (function, `0x007FBF6C`)
- `0x0068FFD1` → [MiAddPhysicalMemoryChunks](../../page/7F/MiAddPhysicalMemoryChunks_function_007F98D4.md) (function, `0x007F98D4`)
- `0x00690022` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x00690044` → [MiHotRemoveHugeRange](../67/MiHotRemoveHugeRange_function_00675DD0.md) (function, `0x00675DD0`)
- `0x0069005C` → [MiHotRemovePartitionPageRun](../../page/80/MiHotRemovePartitionPageRun_function_0080D8B8.md) (function, `0x0080D8B8`)
- `0x00690075` → [RtlClearBitsEx](../29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)
- `0x006900DF` → [RtlClearBitsEx](../29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)

### Direct callers
- [MiClearPartitionPageBitMap](../69/MiClearPartitionPageBitMap_function_00690614.md) at `0x006906D2`
- [MiFreePartitionNodePages](../69/MiFreePartitionNodePages_function_00690D14.md) at `0x00690D7E`
- [MiInsertPartitionPages](../69/MiInsertPartitionPages_function_006911A0.md) at `0x006912A2`
- [MiInsertPartitionPages](../69/MiInsertPartitionPages_function_006911A0.md) at `0x006914C2`
- [MiReturnPartitionPagesToParent](../69/MiReturnPartitionPagesToParent_function_00691B5C.md) at `0x00691C7A`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D7F1`
- [MiMakePartitionMemoryBlock](../../page/80/MiMakePartitionMemoryBlock_function_0080D94C.md) at `0x0080DA08`
- [MiMakePartitionMemoryBlock](../../page/80/MiMakePartitionMemoryBlock_function_0080D94C.md) at `0x0080DACE`
- [MiUpdatePartitionLargePfnBitMap](../../page/80/MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) at `0x0080DBFB`

### Static image references
- `0x0068F878` → RVA `0x00E38D00` (`.data`; read)
- `0x0068FA87` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0068FC3B` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0068FF55` → [MiHotAddHugeRange](../../page/7F/MiHotAddHugeRange_function_007FBF6C.md) (`.text` → `PAGE`)
  - `0x0068FFD1` → [MiAddPhysicalMemoryChunks](../../page/7F/MiAddPhysicalMemoryChunks_function_007F98D4.md) (`.text` → `PAGE`)
  - `0x0069005C` → [MiHotRemovePartitionPageRun](../../page/80/MiHotRemovePartitionPageRun_function_0080D8B8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068F7F4  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0068F7F9  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0068F7FD  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0068F802  55                              push rbp
0068F803  53                              push rbx
0068F804  56                              push rsi
0068F805  57                              push rdi
0068F806  41 54                           push r12
0068F808  41 55                           push r13
0068F80A  41 56                           push r14
0068F80C  41 57                           push r15
0068F80E  48 8B EC                        mov rbp, rsp
0068F811  48 83 EC 78                     sub rsp, 0x78
0068F815  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0068F81A  49 8B F1                        mov rsi, r9
0068F81D  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
0068F822  44 8B EA                        mov r13d, edx
0068F825  83 65 60 00                     and dword ptr [rbp + 0x60], 0
0068F829  45 8B C8                        mov r9d, r8d
0068F82C  4C 8B E1                        mov r12, rcx
0068F82F  BA 01 00 00 00                  mov edx, 1
0068F834  83 66 18 00                     and dword ptr [rsi + 0x18], 0
0068F838  41 83 FD 03                     cmp r13d, 3
0068F83C  77 20                           ja 0x14068f85e
0068F83E  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0068F842  48 0F BA E0 3E                  bt rax, 0x3e
0068F847  73 15                           jae 0x14068f85e
0068F849  48 B9 FF FF FF FF FF FF FF BF   movabs rcx, 0xbfffffffffffffff
0068F853  89 55 60                        mov dword ptr [rbp + 0x60], edx
0068F856  48 23 C1                        and rax, rcx
0068F859  49 89 44 24 18                  mov qword ptr [r12 + 0x18], rax
0068F85E  49 8D 5C 24 20                  lea rbx, [r12 + 0x20]
0068F863  45 33 F6                        xor r14d, r14d
0068F866  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
0068F86A  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
0068F874  49 83 CF FF                     or r15, 0xffffffffffffffff
0068F878  4C 8D 1D 81 94 7A 00            lea r11, [rip + 0x7a9481]
0068F87F  49 83 7C 24 18 00               cmp qword ptr [r12 + 0x18], 0
0068F885  41 BA 02 00 00 00               mov r10d, 2
0068F88B  7D 0C                           jge 0x14068f899
0068F88D  4C 8B 33                        mov r14, qword ptr [rbx]
0068F890  33 FF                           xor edi, edi
0068F892  33 D2                           xor edx, edx
0068F894  E9 C7 01 00 00                  jmp 0x14068fa60
0068F899  4C 8B 13                        mov r10, qword ptr [rbx]
0068F89C  41 BD 01 00 00 00               mov r13d, 1
0068F8A2  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
0068F8A6  4D 3B F2                        cmp r14, r10
0068F8A9  4D 1B C9                        sbb r9, r9
0068F8AC  4D 23 CE                        and r9, r14
0068F8AF  4D 8D 42 FF                     lea r8, [r10 - 1]
0068F8B3  83 65 D0 00                     and dword ptr [rbp - 0x30], 0
0068F8B7  49 8B C0                        mov rax, r8
0068F8BA  49 2B C1                        sub rax, r9
0068F8BD  49 03 C5                        add rax, r13
0068F8C0  49 3B C5                        cmp rax, r13
0068F8C3  73 05                           jae 0x14068f8ca
0068F8C5  49 8B FF                        mov rdi, r15
0068F8C8  EB 66                           jmp 0x14068f930
0068F8CA  49 8B C0                        mov rax, r8
0068F8CD  41 8A C9                        mov cl, r9b
0068F8D0  48 C1 E8 06                     shr rax, 6
0068F8D4  80 E1 3F                        and cl, 0x3f
0068F8D7  49 8B D5                        mov rdx, r13
0068F8DA  48 D3 E2                        shl rdx, cl
0068F8DD  49 2B D5                        sub rdx, r13
0068F8E0  4C 8D 1C C3                     lea r11, [rbx + rax*8]
0068F8E4  49 8B C1                        mov rax, r9
0068F8E7  48 C1 E8 06                     shr rax, 6
0068F8EB  48 8D 3C C3                     lea rdi, [rbx + rax*8]
0068F8EF  48 8B 07                        mov rax, qword ptr [rdi]
0068F8F2  48 F7 D0                        not rax
0068F8F5  48 0B D0                        or rdx, rax
0068F8F8  49 3B D7                        cmp rdx, r15
0068F8FB  75 11                           jne 0x14068f90e
0068F8FD  48 83 C7 08                     add rdi, 8
0068F901  49 3B FB                        cmp rdi, r11
0068F904  77 BF                           ja 0x14068f8c5
0068F906  48 8B 17                        mov rdx, qword ptr [rdi]
0068F909  48 F7 D2                        not rdx
0068F90C  EB EA                           jmp 0x14068f8f8
0068F90E  48 2B FB                        sub rdi, rbx
0068F911  48 F7 D2                        not rdx
0068F914  48 0F BC C2                     bsf rax, rdx
0068F918  48 C1 FF 03                     sar rdi, 3
0068F91C  48 C1 E7 06                     shl rdi, 6
0068F920  48 03 F8                        add rdi, rax
0068F923  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0068F926  49 3B F8                        cmp rdi, r8
0068F929  77 9A                           ja 0x14068f8c5
0068F92B  49 3B FF                        cmp rdi, r15
0068F92E  75 1B                           jne 0x14068f94b
0068F930  4D 85 C9                        test r9, r9
0068F933  74 16                           je 0x14068f94b
0068F935  4D 8D 46 01                     lea r8, [r14 + 1]
0068F939  4D 3B C2                        cmp r8, r10
0068F93C  4D 0F 47 C2                     cmova r8, r10
0068F940  4D 2B C5                        sub r8, r13
0068F943  45 33 C9                        xor r9d, r9d
0068F946  E9 68 FF FF FF                  jmp 0x14068f8b3
0068F94B  44 8B 6D 50                     mov r13d, dword ptr [rbp + 0x50]
0068F94F  49 3B FE                        cmp rdi, r14
0068F952  0F 82 AD 07 00 00               jb 0x140690105
0068F958  49 3B FF                        cmp rdi, r15
0068F95B  0F 84 A4 07 00 00               je 0x140690105
0068F961  83 65 B8 00                     and dword ptr [rbp - 0x48], 0
0068F965  33 D2                           xor edx, edx
0068F967  4D 8B 54 24 20                  mov r10, qword ptr [r12 + 0x20]
0068F96C  4C 3B D7                        cmp r10, rdi
0068F96F  0F 86 C5 00 00 00               jbe 0x14068fa3a
0068F975  44 8D 7A 01                     lea r15d, [rdx + 1]
0068F979  40 8A CF                        mov cl, dil
0068F97C  80 E1 3F                        and cl, 0x3f
0068F97F  49 8D 42 FF                     lea rax, [r10 - 1]
0068F983  48 C1 E8 06                     shr rax, 6
0068F987  4C 8D 1C C3                     lea r11, [rbx + rax*8]
0068F98B  48 8B C7                        mov rax, rdi
0068F98E  48 C1 E8 06                     shr rax, 6
0068F992  4C 8D 04 C3                     lea r8, [rbx + rax*8]
0068F996  41 8B C7                        mov eax, r15d
0068F999  4D 8B 08                        mov r9, qword ptr [r8]
0068F99C  48 D3 E0                        shl rax, cl
0068F99F  49 2B C7                        sub rax, r15
0068F9A2  4C 0B C8                        or r9, rax
0068F9A5  49 8D 40 08                     lea rax, [r8 + 8]
0068F9A9  49 F7 D1                        not r9
0068F9AC  4D 85 C9                        test r9, r9
0068F9AF  75 12                           jne 0x14068f9c3
0068F9B1  49 3B C3                        cmp rax, r11
0068F9B4  77 2C                           ja 0x14068f9e2
0068F9B6  49 83 C0 08                     add r8, 8
0068F9BA  48 83 C0 08                     add rax, 8
0068F9BE  4D 8B 08                        mov r9, qword ptr [r8]
0068F9C1  EB E6                           jmp 0x14068f9a9
0068F9C3  49 0F BC C9                     bsf rcx, r9
0068F9C7  4D 8B F0                        mov r14, r8
0068F9CA  4C 2B F3                        sub r14, rbx
0068F9CD  8B C1                           mov eax, ecx
0068F9CF  49 C1 FE 03                     sar r14, 3
0068F9D3  49 C1 E6 06                     shl r14, 6
0068F9D7  4C 03 F0                        add r14, rax
0068F9DA  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
0068F9DD  4D 3B F2                        cmp r14, r10
0068F9E0  76 05                           jbe 0x14068f9e7
0068F9E2  4D 8B F2                        mov r14, r10
0068F9E5  EB 4E                           jmp 0x14068fa35
0068F9E7  49 8B C7                        mov rax, r15
0068F9EA  48 D3 E0                        shl rax, cl
0068F9ED  49 2B C7                        sub rax, r15
0068F9F0  49 0B C1                        or rax, r9
0068F9F3  48 F7 D0                        not rax
0068F9F6  48 85 C0                        test rax, rax
0068F9F9  75 18                           jne 0x14068fa13
0068F9FB  49 8D 40 08                     lea rax, [r8 + 8]
0068F9FF  49 3B C3                        cmp rax, r11
0068FA02  77 08                           ja 0x14068fa0c
0068FA04  4C 8B C0                        mov r8, rax
0068FA07  48 8B 00                        mov rax, qword ptr [rax]
0068FA0A  EB EA                           jmp 0x14068f9f6
0068FA0C  B8 40 00 00 00                  mov eax, 0x40
0068FA11  EB 04                           jmp 0x14068fa17
0068FA13  48 0F BC C0                     bsf rax, rax
0068FA17  49 8B D0                        mov rdx, r8
0068FA1A  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0068FA1D  48 2B D3                        sub rdx, rbx
0068FA20  48 C1 FA 03                     sar rdx, 3
0068FA24  48 C1 E2 06                     shl rdx, 6
0068FA28  48 03 D0                        add rdx, rax
0068FA2B  49 3B D2                        cmp rdx, r10
0068FA2E  49 0F 47 D2                     cmova rdx, r10
0068FA32  49 2B D6                        sub rdx, r14
0068FA35  48 85 D2                        test rdx, rdx
0068FA38  75 03                           jne 0x14068fa3d
0068FA3A  4D 8B F2                        mov r14, r10
0068FA3D  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
0068FA41  4C 8D 1D B8 92 7A 00            lea r11, [rip + 0x7a92b8]
0068FA48  41 BA 02 00 00 00               mov r10d, 2
0068FA4E  49 8D 5C 24 20                  lea rbx, [r12 + 0x20]
0068FA53  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
0068FA5D  4C 2B F7                        sub r14, rdi
0068FA60  4D 8B 7C 24 18                  mov r15, qword ptr [r12 + 0x18]
0068FA65  4A 8D 04 37                     lea rax, [rdi + r14]
0068FA69  48 03 C2                        add rax, rdx
0068FA6C  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0068FA70  33 C9                           xor ecx, ecx
0068FA72  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0068FA76  4D 23 F8                        and r15, r8
0068FA79  41 8D 45 F5                     lea eax, [r13 - 0xb]
0068FA7D  4C 03 FF                        add r15, rdi
0068FA80  8D 51 01                        lea edx, [rcx + 1]
0068FA83  3B C2                           cmp eax, edx
0068FA85  76 72                           jbe 0x14068faf9
0068FA87  4C 3B 3D 52 E2 79 00            cmp r15, qword ptr [rip + 0x79e252]
0068FA8E  77 20                           ja 0x14068fab0
0068FA90  4B 8D 04 7F                     lea rax, [r15 + r15*2]
0068FA94  48 03 C0                        add rax, rax
0068FA97  48 BA 28 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000028
0068FAA1  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0068FAA5  8D 51 01                        lea edx, [rcx + 1]
0068FAA8  48 C1 E8 36                     shr rax, 0x36
0068FAAC  85 C2                           test edx, eax
0068FAAE  75 02                           jne 0x14068fab2
0068FAB0  8B CA                           mov ecx, edx
0068FAB2  41 83 FD 07                     cmp r13d, 7
0068FAB6  0F 84 D7 05 00 00               je 0x140690093
0068FABC  41 83 FD 08                     cmp r13d, 8
0068FAC0  75 1B                           jne 0x14068fadd
0068FAC2  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0068FAC6  48 03 C2                        add rax, rdx
0068FAC9  48 C1 E0 04                     shl rax, 4
0068FACD  48 03 46 40                     add rax, qword ptr [rsi + 0x40]
0068FAD1  4C 89 38                        mov qword ptr [rax], r15
0068FAD4  4C 89 70 08                     mov qword ptr [rax + 8], r14
0068FAD8  E9 B6 05 00 00                  jmp 0x140690093
0068FADD  45 85 ED                        test r13d, r13d
0068FAE0  75 17                           jne 0x14068faf9
0068FAE2  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
0068FAE5  4D 8B C6                        mov r8, r14
0068FAE8  49 8B D7                        mov rdx, r15
0068FAEB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0068FAEF  E8 AC 12 00 00                  call 0x140690da0
0068FAF4  E9 90 05 00 00                  jmp 0x140690089
0068FAF9  41 8D 45 FF                     lea eax, [r13 - 1]
0068FAFD  A9 FD FF FF FF                  test eax, 0xfffffffd
0068FB02  0F 84 2F 05 00 00               je 0x140690037
0068FB08  41 83 FD 04                     cmp r13d, 4
0068FB0C  75 3E                           jne 0x14068fb4c
0068FB0E  85 C9                           test ecx, ecx
0068FB10  0F 85 7D 05 00 00               jne 0x140690093
0068FB16  49 8D 97 FF 01 00 00            lea rdx, [r15 + 0x1ff]
0068FB1D  48 81 E2 00 FE FF FF            and rdx, 0xfffffffffffffe00
0068FB24  4E 8D 04 32                     lea r8, [rdx + r14]
0068FB28  49 81 E0 00 FE FF FF            and r8, 0xfffffffffffffe00
0068FB2F  49 3B D0                        cmp rdx, r8
0068FB32  0F 83 51 05 00 00               jae 0x140690089
0068FB38  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FB3B  45 8D 4D FD                     lea r9d, [r13 - 3]
0068FB3F  4C 2B C2                        sub r8, rdx
0068FB42  E8 55 66 CE FF                  call 0x14037619c
0068FB47  E9 3D 05 00 00                  jmp 0x140690089
0068FB4C  41 83 FD 05                     cmp r13d, 5
0068FB50  75 2C                           jne 0x14068fb7e
0068FB52  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FB55  4D 8B C6                        mov r8, r14
0068FB58  49 8B D7                        mov rdx, r15
0068FB5B  E8 04 22 00 00                  call 0x140691d64
0068FB60  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
0068FB6A  85 C0                           test eax, eax
0068FB6C  0F 85 21 05 00 00               jne 0x140690093
0068FB72  C7 46 18 9A 00 00 C0            mov dword ptr [rsi + 0x18], 0xc000009a
0068FB79  E9 15 05 00 00                  jmp 0x140690093
0068FB7E  41 83 FD 06                     cmp r13d, 6
0068FB82  75 44                           jne 0x14068fbc8
0068FB84  85 C9                           test ecx, ecx
0068FB86  75 29                           jne 0x14068fbb1
0068FB88  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FB8B  4D 8D 86 FF 01 00 00            lea r8, [r14 + 0x1ff]
0068FB92  4D 03 C7                        add r8, r15
0068FB95  49 8B D7                        mov rdx, r15
0068FB98  49 81 E0 00 FE FF FF            and r8, 0xfffffffffffffe00
0068FB9F  48 81 E2 00 FE FF FF            and rdx, 0xfffffffffffffe00
0068FBA6  4C 2B C2                        sub r8, rdx
0068FBA9  45 33 C9                        xor r9d, r9d
0068FBAC  E8 EB 65 CE FF                  call 0x14037619c
0068FBB1  48 8B 16                        mov rdx, qword ptr [rsi]
0068FBB4  4D 8B CE                        mov r9, r14
0068FBB7  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0068FBBB  4D 8B C7                        mov r8, r15
0068FBBE  E8 09 22 00 00                  call 0x140691dcc
0068FBC3  E9 C1 04 00 00                  jmp 0x140690089
0068FBC8  41 83 FD 0A                     cmp r13d, 0xa
0068FBCC  0F 85 34 01 00 00               jne 0x14068fd06
0068FBD2  85 C9                           test ecx, ecx
0068FBD4  74 17                           je 0x14068fbed
0068FBD6  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0068FBDA  4D 8B CE                        mov r9, r14
0068FBDD  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FBE0  4D 8B C7                        mov r8, r15
0068FBE3  E8 FC 77 FE FF                  call 0x1406773e4
0068FBE8  E9 9C 04 00 00                  jmp 0x140690089
0068FBED  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0068FBF1  49 3B CB                        cmp rcx, r11
0068FBF4  74 0E                           je 0x14068fc04
0068FBF6  45 33 C9                        xor r9d, r9d
0068FBF9  4D 8B C6                        mov r8, r14
0068FBFC  49 8B D7                        mov rdx, r15
0068FBFF  E8 98 65 CE FF                  call 0x14037619c
0068FC04  48 8B 06                        mov rax, qword ptr [rsi]
0068FC07  4B 8D 3C 7F                     lea rdi, [r15 + r15*2]
0068FC0B  48 C1 E7 04                     shl rdi, 4
0068FC0F  0F B7 18                        movzx ebx, word ptr [rax]
0068FC12  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0068FC1C  4F 8D 2C 76                     lea r13, [r14 + r14*2]
0068FC20  48 03 F8                        add rdi, rax
0068FC23  49 C1 E5 04                     shl r13, 4
0068FC27  4C 03 EF                        add r13, rdi
0068FC2A  44 0F 20 C0                     mov rax, cr8
0068FC2E  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0068FC32  BA 02 00 00 00                  mov edx, 2
0068FC37  44 0F 22 C2                     mov cr8, rdx
0068FC3B  83 3D DE 70 93 00 00            cmp dword ptr [rip + 0x9370de], 0
0068FC42  74 07                           je 0x14068fc4b
0068FC44  8A C8                           mov cl, al
0068FC46  E8 B1 5A E6 FF                  call 0x1404f56fc
0068FC4B  4C 8B E3                        mov r12, rbx
0068FC4E  48 8D 5F 18                     lea rbx, [rdi + 0x18]
0068FC52  49 C1 E4 2B                     shl r12, 0x2b
0068FC56  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
0068FC5A  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
0068FC60  73 13                           jae 0x14068fc75
0068FC62  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0068FC66  E8 95 C0 D6 FF                  call 0x1403fbd00
0068FC6B  48 8B 03                        mov rax, qword ptr [rbx]
0068FC6E  48 85 C0                        test rax, rax
0068FC71  78 EF                           js 0x14068fc62
0068FC73  EB E5                           jmp 0x14068fc5a
0068FC75  8B 43 08                        mov eax, dword ptr [rbx + 8]
0068FC78  C1 E8 18                        shr eax, 0x18
0068FC7B  A8 40                           test al, 0x40
0068FC7D  74 0F                           je 0x14068fc8e
0068FC7F  4C 8B 06                        mov r8, qword ptr [rsi]
0068FC82  48 8B CF                        mov rcx, rdi
0068FC85  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0068FC89  E8 D2 A2 FF FF                  call 0x140689f60
0068FC8E  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0068FC92  48 B9 FF FF FF FF FF 07 E0 FF   movabs rcx, 0xffe007ffffffffff
0068FC9C  49 33 C4                        xor rax, r12
0068FC9F  48 23 C1                        and rax, rcx
0068FCA2  49 33 C4                        xor rax, r12
0068FCA5  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0068FCA9  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0068FCB3  F0 48 21 03                     lock and qword ptr [rbx], rax
0068FCB7  48 83 C7 30                     add rdi, 0x30
0068FCBB  48 83 C3 30                     add rbx, 0x30
0068FCBF  49 3B FD                        cmp rdi, r13
0068FCC2  75 92                           jne 0x14068fc56
0068FCC4  83 3D 55 70 93 00 00            cmp dword ptr [rip + 0x937055], 0
0068FCCB  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
0068FCCF  74 0B                           je 0x14068fcdc
0068FCD1  44 0F 20 C1                     mov rcx, cr8
0068FCD5  8A D3                           mov dl, bl
0068FCD7  E8 BC 59 E6 FF                  call 0x1404f5698
0068FCDC  0F B6 C3                        movzx eax, bl
0068FCDF  44 0F 22 C0                     mov cr8, rax
0068FCE3  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0068FCE7  4D 8B CE                        mov r9, r14
0068FCEA  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FCED  4D 8B C7                        mov r8, r15
0068FCF0  E8 DF 24 00 00                  call 0x1406921d4
0068FCF5  44 8B 6D 50                     mov r13d, dword ptr [rbp + 0x50]
0068FCF9  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
0068FCFD  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
0068FD01  E9 83 03 00 00                  jmp 0x140690089
0068FD06  45 3B EA                        cmp r13d, r10d
0068FD09  0F 84 0C 02 00 00               je 0x14068ff1b
0068FD0F  41 8D 45 F5                     lea eax, [r13 - 0xb]
0068FD13  3B C2                           cmp eax, edx
0068FD15  0F 86 00 02 00 00               jbe 0x14068ff1b
0068FD1B  41 83 FD 0D                     cmp r13d, 0xd
0068FD1F  75 06                           jne 0x14068fd27
0068FD21  CC                              int3
0068FD22  E9 6C 03 00 00                  jmp 0x140690093
0068FD27  48 8B 06                        mov rax, qword ptr [rsi]
0068FD2A  4C 29 B0 50 48 00 00            sub qword ptr [rax + 0x4850], r14
0068FD31  48 8B 06                        mov rax, qword ptr [rsi]
0068FD34  88 50 0C                        mov byte ptr [rax + 0xc], dl
0068FD37  48 8B 06                        mov rax, qword ptr [rsi]
0068FD3A  48 8B 78 18                     mov rdi, qword ptr [rax + 0x18]
0068FD3E  48 85 FF                        test rdi, rdi
0068FD41  74 2B                           je 0x14068fd6e
0068FD43  49 8B 54 24 18                  mov rdx, qword ptr [r12 + 0x18]
0068FD48  49 23 D0                        and rdx, r8
0068FD4B  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0068FD4F  49 23 C8                        and rcx, r8
0068FD52  48 3B D1                        cmp rdx, rcx
0068FD55  73 05                           jae 0x14068fd5c
0068FD57  48 8B 3F                        mov rdi, qword ptr [rdi]
0068FD5A  EB 0D                           jmp 0x14068fd69
0068FD5C  48 03 4F 20                     add rcx, qword ptr [rdi + 0x20]
0068FD60  48 3B D1                        cmp rdx, rcx
0068FD63  72 09                           jb 0x14068fd6e
0068FD65  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
0068FD69  48 85 FF                        test rdi, rdi
0068FD6C  75 DD                           jne 0x14068fd4b
0068FD6E  4C 8D 67 20                     lea r12, [rdi + 0x20]
0068FD72  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
0068FD76  4C 8D 6F 18                     lea r13, [rdi + 0x18]
0068FD7A  49 8B D7                        mov rdx, r15
0068FD7D  49 8B 45 00                     mov rax, qword ptr [r13]
0068FD81  49 8B DE                        mov rbx, r14
0068FD84  49 23 C0                        and rax, r8
0068FD87  49 8B CC                        mov rcx, r12
0068FD8A  48 2B D0                        sub rdx, rax
0068FD8D  49 8B 04 24                     mov rax, qword ptr [r12]
0068FD91  48 2B C2                        sub rax, rdx
0068FD94  49 3B C6                        cmp rax, r14
0068FD97  48 0F 46 D8                     cmovbe rbx, rax
0068FD9B  4C 8B C3                        mov r8, rbx
0068FD9E  E8 9D 79 C0 FF                  call 0x140297740
0068FDA3  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0068FDAD  4C 03 FB                        add r15, rbx
0068FDB0  49 21 45 00                     and qword ptr [r13], rax
0068FDB4  4C 2B F3                        sub r14, rbx
0068FDB7  74 39                           je 0x14068fdf2
0068FDB9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0068FDBD  48 8B CF                        mov rcx, rdi
0068FDC0  48 85 C0                        test rax, rax
0068FDC3  74 23                           je 0x14068fde8
0068FDC5  48 8B 08                        mov rcx, qword ptr [rax]
0068FDC8  48 8B F8                        mov rdi, rax
0068FDCB  48 85 C9                        test rcx, rcx
0068FDCE  74 22                           je 0x14068fdf2
0068FDD0  48 8B 01                        mov rax, qword ptr [rcx]
0068FDD3  48 8B F9                        mov rdi, rcx
0068FDD6  48 8B C8                        mov rcx, rax
0068FDD9  48 85 C0                        test rax, rax
0068FDDC  75 F2                           jne 0x14068fdd0
0068FDDE  EB 12                           jmp 0x14068fdf2
0068FDE0  48 39 0F                        cmp qword ptr [rdi], rcx
0068FDE3  74 0D                           je 0x14068fdf2
0068FDE5  48 8B CF                        mov rcx, rdi
0068FDE8  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
0068FDEC  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
0068FDF0  75 EE                           jne 0x14068fde0
0068FDF2  49 8B 04 24                     mov rax, qword ptr [r12]
0068FDF6  49 8B 14 24                     mov rdx, qword ptr [r12]
0068FDFA  48 85 C0                        test rax, rax
0068FDFD  0F 84 F0 00 00 00               je 0x14068fef3
0068FE03  B9 01 00 00 00                  mov ecx, 1
0068FE08  48 3B D1                        cmp rdx, rcx
0068FE0B  77 18                           ja 0x14068fe25
0068FE0D  0F 85 E0 00 00 00               jne 0x14068fef3
0068FE13  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0068FE18  48 0F BA 20 00                  bt qword ptr [rax], 0
0068FE1D  0F 82 D0 00 00 00               jb 0x14068fef3
0068FE23  EB 68                           jmp 0x14068fe8d
0068FE25  48 3B C2                        cmp rax, rdx
0068FE28  0F 82 C5 00 00 00               jb 0x14068fef3
0068FE2E  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0068FE33  4C 8D 52 FF                     lea r10, [rdx - 1]
0068FE37  49 8B C2                        mov rax, r10
0068FE3A  48 C1 E8 06                     shr rax, 6
0068FE3E  4C 8B 01                        mov r8, qword ptr [rcx]
0068FE41  4C 8D 0C C1                     lea r9, [rcx + rax*8]
0068FE45  49 3B C9                        cmp rcx, r9
0068FE48  75 13                           jne 0x14068fe5d
0068FE4A  48 83 C8 FF                     or rax, 0xffffffffffffffff
0068FE4E  B9 40 00 00 00                  mov ecx, 0x40
0068FE53  2A CA                           sub cl, dl
0068FE55  48 D3 E8                        shr rax, cl
0068FE58  49 85 C0                        test r8, rax
0068FE5B  EB 29                           jmp 0x14068fe86
0068FE5D  4D 85 C0                        test r8, r8
0068FE60  0F 85 8D 00 00 00               jne 0x14068fef3
0068FE66  48 83 C1 08                     add rcx, 8
0068FE6A  48 8B 11                        mov rdx, qword ptr [rcx]
0068FE6D  49 3B C9                        cmp rcx, r9
0068FE70  74 05                           je 0x14068fe77
0068FE72  48 85 D2                        test rdx, rdx
0068FE75  EB E9                           jmp 0x14068fe60
0068FE77  48 83 C8 FF                     or rax, 0xffffffffffffffff
0068FE7B  41 8A CA                        mov cl, r10b
0068FE7E  F6 D1                           not cl
0068FE80  48 D3 E8                        shr rax, cl
0068FE83  48 85 D0                        test rax, rdx
0068FE86  0F 94 C0                        sete al
0068FE89  84 C0                           test al, al
0068FE8B  74 66                           je 0x14068fef3
0068FE8D  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FE90  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
0068FE94  48 83 C1 18                     add rcx, 0x18
0068FE98  48 8B D3                        mov rdx, rbx
0068FE9B  E8 B0 67 C0 FF                  call 0x140296650
0068FEA0  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
0068FEA4  45 32 C0                        xor r8b, r8b
0068FEA7  48 85 D2                        test rdx, rdx
0068FEAA  74 3B                           je 0x14068fee7
0068FEAC  49 8B 4D 00                     mov rcx, qword ptr [r13]
0068FEB0  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
0068FEBA  49 23 C8                        and rcx, r8
0068FEBD  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0068FEC1  49 23 C0                        and rax, r8
0068FEC4  48 3B C8                        cmp rcx, rax
0068FEC7  73 0D                           jae 0x14068fed6
0068FEC9  48 8B 02                        mov rax, qword ptr [rdx]
0068FECC  48 85 C0                        test rax, rax
0068FECF  75 0E                           jne 0x14068fedf
0068FED1  45 32 C0                        xor r8b, r8b
0068FED4  EB 11                           jmp 0x14068fee7
0068FED6  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0068FEDA  48 85 C0                        test rax, rax
0068FEDD  74 05                           je 0x14068fee4
0068FEDF  48 8B D0                        mov rdx, rax
0068FEE2  EB D9                           jmp 0x14068febd
0068FEE4  41 B0 01                        mov r8b, 1
0068FEE7  4C 8B CB                        mov r9, rbx
0068FEEA  48 8D 4E 20                     lea rcx, [rsi + 0x20]
0068FEEE  E8 9D 58 BD FF                  call 0x140265790
0068FEF3  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
0068FEFD  4D 85 F6                        test r14, r14
0068FF00  0F 85 68 FE FF FF               jne 0x14068fd6e
0068FF06  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
0068FF0A  44 8B 6D 50                     mov r13d, dword ptr [rbp + 0x50]
0068FF0E  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
0068FF12  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
0068FF16  E9 78 01 00 00                  jmp 0x140690093
0068FF1B  49 8B DE                        mov rbx, r14
0068FF1E  48 C1 E3 0C                     shl rbx, 0xc
0068FF22  80 7E 11 00                     cmp byte ptr [rsi + 0x11], 0
0068FF26  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
0068FF2A  74 30                           je 0x14068ff5c
0068FF2C  83 7D 60 00                     cmp dword ptr [rbp + 0x60], 0
0068FF30  74 09                           je 0x14068ff3b
0068FF32  44 39 56 14                     cmp dword ptr [rsi + 0x14], r10d
0068FF36  75 03                           jne 0x14068ff3b
0068FF38  89 56 14                        mov dword ptr [rsi + 0x14], edx
0068FF3B  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
0068FF40  4D 8B C6                        mov r8, r14
0068FF43  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0068FF46  49 8B D7                        mov rdx, r15
0068FF49  44 0F B6 4E 10                  movzx r9d, byte ptr [rsi + 0x10]
0068FF4E  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FF51  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0068FF55  E8 12 C0 16 00                  call 0x1407fbf6c
0068FF5A  EB 7E                           jmp 0x14068ffda
0068FF5C  49 8B C7                        mov rax, r15
0068FF5F  48 C1 E0 0C                     shl rax, 0xc
0068FF63  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0068FF67  45 3B EA                        cmp r13d, r10d
0068FF6A  75 0E                           jne 0x14068ff7a
0068FF6C  8B 55 60                        mov edx, dword ptr [rbp + 0x60]
0068FF6F  45 33 C0                        xor r8d, r8d
0068FF72  83 EA 80                        sub edx, -0x80
0068FF75  C1 E2 09                        shl edx, 9
0068FF78  EB 14                           jmp 0x14068ff8e
0068FF7A  44 8B C2                        mov r8d, edx
0068FF7D  41 83 FD 0B                     cmp r13d, 0xb
0068FF81  BA 80 00 00 00                  mov edx, 0x80
0068FF86  B8 00 00 02 00                  mov eax, 0x20000
0068FF8B  0F 45 D0                        cmovne edx, eax
0068FF8E  48 8B 06                        mov rax, qword ptr [rsi]
0068FF91  8B CA                           mov ecx, edx
0068FF93  0F BA E9 0A                     bts ecx, 0xa
0068FF97  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
0068FF9C  80 7E 10 00                     cmp byte ptr [rsi + 0x10], 0
0068FFA0  4C 8D 45 D8                     lea r8, [rbp - 0x28]
0068FFA4  8B 40 04                        mov eax, dword ptr [rax + 4]
0068FFA7  0F 44 CA                        cmove ecx, edx
0068FFAA  8B D1                           mov edx, ecx
0068FFAC  0F BA EA 0B                     bts edx, 0xb
0068FFB0  41 F6 C1 40                     test r9b, 0x40
0068FFB4  4C 8B 4E 38                     mov r9, qword ptr [rsi + 0x38]
0068FFB8  0F 44 D1                        cmove edx, ecx
0068FFBB  8B CA                           mov ecx, edx
0068FFBD  0F BA E9 13                     bts ecx, 0x13
0068FFC1  A8 80                           test al, 0x80
0068FFC3  0F 44 CA                        cmove ecx, edx
0068FFC6  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0068FFCA  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0068FFCE  48 8B 0E                        mov rcx, qword ptr [rsi]
0068FFD1  E8 FE 98 16 00                  call 0x1407f98d4
0068FFD6  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
0068FFDA  48 8B C3                        mov rax, rbx
0068FFDD  B9 00 10 00 00                  mov ecx, 0x1000
0068FFE2  48 99                           cqo
0068FFE4  48 F7 F9                        idiv rcx
0068FFE7  80 7E 11 00                     cmp byte ptr [rsi + 0x11], 0
0068FFEB  48 8B D8                        mov rbx, rax
0068FFEE  75 37                           jne 0x140690027
0068FFF0  48 8D 0D 09 8D 7A 00            lea rcx, [rip + 0x7a8d09]
0068FFF7  48 39 0E                        cmp qword ptr [rsi], rcx
0068FFFA  74 2B                           je 0x140690027
0068FFFC  48 C7 C0 00 FE FF FF            mov rax, 0xfffffffffffffe00
00690003  49 8D 97 FF 01 00 00            lea rdx, [r15 + 0x1ff]
0069000A  48 23 D0                        and rdx, rax
0069000D  4C 8D 04 1A                     lea r8, [rdx + rbx]
00690011  4C 23 C0                        and r8, rax
00690014  49 3B D0                        cmp rdx, r8
00690017  73 0E                           jae 0x140690027
00690019  4C 2B C2                        sub r8, rdx
0069001C  41 B9 01 00 00 00               mov r9d, 1
00690022  E8 75 61 CE FF                  call 0x14037619c
00690027  49 3B DE                        cmp rbx, r14
0069002A  0F 85 96 00 00 00               jne 0x1406900c6
00690030  49 8D 5C 24 20                  lea rbx, [r12 + 0x20]
00690035  EB 52                           jmp 0x140690089
00690037  85 C9                           test ecx, ecx
00690039  49 8B CF                        mov rcx, r15
0069003C  74 0F                           je 0x14069004d
0069003E  44 8B C2                        mov r8d, edx
00690041  49 8B D6                        mov rdx, r14
00690044  E8 87 5D FE FF                  call 0x140675dd0
00690049  33 C0                           xor eax, eax
0069004B  EB 14                           jmp 0x140690061
0069004D  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00690052  45 8B C5                        mov r8d, r13d
00690055  44 8B 4D 60                     mov r9d, dword ptr [rbp + 0x60]
00690059  49 8B D6                        mov rdx, r14
0069005C  E8 57 D8 17 00                  call 0x14080d8b8
00690061  89 46 18                        mov dword ptr [rsi + 0x18], eax
00690064  85 C0                           test eax, eax
00690066  0F 88 99 00 00 00               js 0x140690105
0069006C  4D 8B C6                        mov r8, r14
0069006F  48 8B D7                        mov rdx, rdi
00690072  48 8B CB                        mov rcx, rbx
00690075  E8 C6 76 C0 FF                  call 0x140297740
0069007A  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00690084  49 21 44 24 18                  and qword ptr [r12 + 0x18], rax
00690089  49 B8 FF FF FF FF FF FF FF 3F   movabs r8, 0x3fffffffffffffff
00690093  66 49 0F 6E C6                  movq xmm0, r14
00690098  B8 01 00 00 00                  mov eax, 1
0069009D  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
006900A1  66 48 0F 6E C8                  movq xmm1, rax
006900A6  66 0F 6C C8                     punpcklqdq xmm1, xmm0
006900AA  F3 0F 6F 46 28                  movdqu xmm0, xmmword ptr [rsi + 0x28]
006900AF  66 0F D4 C8                     paddq xmm1, xmm0
006900B3  F3 0F 7F 4E 28                  movdqu xmmword ptr [rsi + 0x28], xmm1
006900B8  4C 3B 33                        cmp r14, qword ptr [rbx]
006900BB  73 48                           jae 0x140690105
006900BD  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
006900C1  E9 AE F7 FF FF                  jmp 0x14068f874
006900C6  49 8D 4C 24 20                  lea rcx, [r12 + 0x20]
006900CB  C7 46 18 01 00 00 C0            mov dword ptr [rsi + 0x18], 0xc0000001
006900D2  4C 8B 01                        mov r8, qword ptr [rcx]
006900D5  48 8D 14 1F                     lea rdx, [rdi + rbx]
006900D9  4C 2B C7                        sub r8, rdi
006900DC  4C 2B C3                        sub r8, rbx
006900DF  E8 5C 76 C0 FF                  call 0x140297740
006900E4  48 85 DB                        test rbx, rbx
006900E7  74 09                           je 0x1406900f2
006900E9  B8 01 00 00 00                  mov eax, 1
006900EE  48 01 46 28                     add qword ptr [rsi + 0x28], rax
006900F2  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
006900FC  49 21 4C 24 18                  and qword ptr [r12 + 0x18], rcx
00690101  48 01 5E 30                     add qword ptr [rsi + 0x30], rbx
00690105  48 83 C4 78                     add rsp, 0x78
00690109  41 5F                           pop r15
0069010B  41 5E                           pop r14
0069010D  41 5D                           pop r13
0069010F  41 5C                           pop r12
00690111  5F                              pop rdi
00690112  5E                              pop rsi
00690113  5B                              pop rbx
00690114  5D                              pop rbp
00690115  C3                              ret
00690116  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiActOnPartitionNodePages(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    if (((unsigned int)((unsigned int)(a2))) > 3) goto loc_0068F85E;
    result = *(unsigned __int64 *)(a1 + 24);
    if (((unsigned int)((unsigned int)(a2))) < 3) {
        v_stack_p20 = 1;
        result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
        *(unsigned __int64 *)(a1 + 24) = result;
    }
    v_r14 = 0;
    v_stack_m60 = a1 + 32;
loc_0068F874:
    v_r15 = (v_r15) | (-1);
    if ((*(unsigned __int64 *)(a1 + 24)) >= 0) goto loc_0068F899;
    v_rdi = 0;
    a2 = 0;
    goto loc_0068FA60;
loc_0068F899:
    a4 = ((unsigned int)(a3)) & (*(unsigned __int64 *)(a1 + 32));
loc_0068F8B3:
    result = (*(unsigned __int64 *)(a1 + 32) - 1) - (a4);
    result = (result) + (1);
    if (result >= 1) goto loc_0068F8CA;
loc_0068F8C5:
    goto loc_0068F930;
loc_0068F8CA:
    result = (*(unsigned __int64 *)(a1 + 32) - 1) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(a4)) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - (1);
    result = (a4) >> (6);
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8) + result * 8));
    a2 = (a2) | (result);
loc_0068F8F8:
    if (a2 != v_r15) goto loc_0068F90E;
    v_rdi = (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8) + (8);
    if (v_rdi > (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8)) goto loc_0068F8C5;
    a2 = ~(*(unsigned __int64 *)(v_rdi));
    goto loc_0068F8F8;
loc_0068F90E:
    v_rdi = (v_rdi) - (*(unsigned __int64 *)(a1 + 32 + 8));
    a2 = ~(a2);
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) + (result);
    v_stack_m70 = (unsigned int)(result);
    if (v_rdi > (*(unsigned __int64 *)(a1 + 32) - 1)) goto loc_0068F8C5;
    if (v_rdi != v_r15) goto loc_0068F94B;
loc_0068F930:
    if (a4 == 0) goto loc_0068F94B;
    a3 = *(unsigned __int64 *)(a1 + 32) + 1;
    if ((*(unsigned __int64 *)(a1 + 32) + 1) > (*(unsigned __int64 *)(a1 + 32))) { a3 = *(unsigned __int64 *)(a1 + 32); }
    a3 = (a3) - (1);
    a4 = 0;
    goto loc_0068F8B3;
loc_0068F94B:
    if (v_rdi < (*(unsigned __int64 *)(a1 + 32))) goto loc_00690105;
    if (v_rdi == v_r15) goto loc_00690105;
    a2 = 0;
    if ((*(unsigned __int64 *)(a1 + 32)) <= v_rdi) goto loc_0068FA3A;
    a1 = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (63));
    result = (*(unsigned __int64 *)(a1 + 32) - 1) >> (6);
    result = (v_rdi) >> (6);
    result = ((unsigned int)((unsigned int)(a2 + 1))) << ((unsigned __int8)(a1));
    result = (result) - (a2 + 1);
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8) + result * 8)) | (result);
loc_0068F9A9:
    a4 = ~(a4);
    if (a4 != 0) goto loc_0068F9C3;
    if ((*(unsigned __int64 *)(a1 + 32 + 8) + result * 8 + 8) > (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8)) goto loc_0068F9E2;
    a3 = (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8) + (8);
    result = (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8 + 8) + (8);
    goto loc_0068F9A9;
loc_0068F9C3:
    v_r14 = (a3) - (*(unsigned __int64 *)(a1 + 32 + 8));
    v_r14 = (v_r14) >> (3);
    v_r14 = (v_r14) << (6);
    v_r14 = (v_r14) + ((unsigned int)((unsigned int)(a1)));
    v_stack_m88 = (unsigned int)(a1);
    if (v_r14 <= (*(unsigned __int64 *)(a1 + 32))) goto loc_0068F9E7;
loc_0068F9E2:
    goto loc_0068FA35;
loc_0068F9E7:
    result = (a2 + 1) << ((unsigned __int8)(a1));
    result = (result) - (a2 + 1);
    result = (result) | (*(unsigned __int64 *)(a3));
    result = ~(result);
loc_0068F9F6:
    if (result != 0) goto loc_0068FA13;
    if ((a3 + 8) > (*(unsigned __int64 *)(a1 + 32 + 8) + result * 8)) goto loc_0068FA0C;
    goto loc_0068F9F6;
loc_0068FA0C:
    goto loc_0068FA17;
loc_0068FA13:
loc_0068FA17:
    v_stack_m88 = 64;
    a2 = (a3 + 8) - (*(unsigned __int64 *)(a1 + 32 + 8));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    a2 = (a2) + (64);
    if (a2 > (*(unsigned __int64 *)(a1 + 32))) { a2 = *(unsigned __int64 *)(a1 + 32); }
    a2 = (a2) - (*(unsigned __int64 *)(a1 + 32));
loc_0068FA35:
    v_r14 = *(unsigned __int64 *)(a1 + 32);
    if (a2 == 0) {
        v_r14 = *(unsigned __int64 *)(a1 + 32);
    }
    v_r14 = (v_r14) - (v_rdi);
loc_0068FA60:
    result = (v_rdi + v_r14 * 1) + (a2);
    v_stack_m78 = v_r14;
    a1 = 0;
    v_stack_m50 = result;
    v_r15 = (*(unsigned __int64 *)(a1 + 24)) & (a3 + 8);
    v_r15 = (v_r15) + (v_rdi);
    if (((unsigned int)((unsigned int)(v_stack_p10) - 11)) <= ((unsigned int)(a1 + 1))) goto loc_0068FAF9;
    if (v_r15 > (*(unsigned __int64 *)(v_rip + 7987794))) goto loc_0068FAB0;
    result = (v_r15 + v_r15 * 2) + (v_r15 + v_r15 * 2);
    result = (*(unsigned __int64 *)(a1 + 1 + result * 8)) >> (54);
    if ((((unsigned int)(a1 + 1)) & ((unsigned int)(result))) == 0) {
        a1 = (unsigned int)(a1 + 1);
    }
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 7) goto loc_00690093;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 8) goto loc_0068FADD;
    result = (*(unsigned __int64 *)(a4 + 40)) + (a1 + 1);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(a4 + 64));
    *(unsigned __int64 *)(result) = v_r15;
    *(unsigned __int64 *)(result + 8) = v_r14;
    goto loc_00690093;
loc_0068FADD:
    if ((unsigned int)((unsigned int)(v_stack_p10)) != 0) goto loc_0068FAF9;
    v_stack_m98 = (unsigned int)((unsigned int)(v_stack_p20));
    result = MiFreePartitionPageRun(a1, v_r15, v_r14, (unsigned int)(v_stack_p18));
    goto loc_00690089;
loc_0068FAF9:
    if ((((unsigned int)((unsigned int)(v_stack_p10) - 1)) & (0xFFFFFFFDULL)) == 0) goto loc_00690037;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 4) goto loc_0068FB4C;
    if ((unsigned int)(a1) != 0) goto loc_00690093;
    a2 = (v_r15 + 511) & (-512);
    a3 = (a2 + v_r14 * 1) & (-512);
    if (a2 >= a3) goto loc_00690089;
    a3 = (a3) - (a2);
    result = MiUpdateLargePageBitMap(*(unsigned __int64 *)(a4), a2, a3, (unsigned int)(v_stack_p10) - 3);
    goto loc_00690089;
loc_0068FB4C:
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 5) goto loc_0068FB7E;
    result = MiSplitPfnBitMapsForPartitionHierarchy(*(unsigned __int64 *)(a4), v_r15, v_r14, (unsigned int)(v_stack_p10) - 3);
    if ((unsigned int)(result) != 0) goto loc_00690093;
    *(unsigned int *)(a4 + 24) = 0xC000009AULL;
    goto loc_00690093;
loc_0068FB7E:
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 6) goto loc_0068FBC8;
    if ((unsigned int)(*(unsigned __int64 *)(a4)) == 0) {
        a1 = *(unsigned __int64 *)(a4);
        a3 = v_r14 + 511;
        a3 = (a3) + (v_r15);
        a2 = v_r15;
        a3 = (a3) & (-512);
        a2 = (a2) & (-512);
        a3 = (a3) - (a2);
        a4 = 0;
        result = MiUpdateLargePageBitMap(a1, a2, a3, a4);
    }
    result = MiTransferPartitionPageRun(*(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4), v_r15, v_r14);
    goto loc_00690089;
loc_0068FBC8:
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 10) goto loc_0068FD06;
    if ((unsigned int)(*(unsigned __int64 *)(a4 + 8)) == 0) goto loc_0068FBED;
    result = MiSetHugeRangePartitionId(*(unsigned __int64 *)(a4), *(unsigned __int64 *)(a4 + 8), v_r15, v_r14);
    goto loc_00690089;
loc_0068FBED:
    if ((*(unsigned __int64 *)(a4 + 8)) != (v_rip + 8032952)) {
        a4 = 0;
        a3 = v_r14;
        a2 = v_r15;
        result = MiUpdateLargePageBitMap(*(unsigned __int64 *)(a4 + 8), a2, a3, a4);
    }
    v_rdi = (v_r15 + v_r15 * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a4));
    v_r13 = (v_r14 + v_r14 * 2) << (4);
    v_r13 = (v_r13) + (v_rdi);
    v_stack_m78 = v_cr8;
    result = v_cr8;
    if ((*(unsigned int *)(v_rip + 9662686)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 2, a3, a4);
    }
    v_r12 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a4))) << (43);
loc_0068FC56:
loc_0068FC5A:
    if (condition_is_above_or_equal) goto loc_0068FC75;
loc_0068FC62:
    result = KeYieldProcessorEx(v_stack_m80, 2, a3, a4);
    if (sign_flag) goto loc_0068FC62;
    goto loc_0068FC5A;
loc_0068FC75:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 24 + 8))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) {
        a3 = *(unsigned __int64 *)(a4);
        a1 = v_rdi;
        a2 = *(unsigned __int64 *)(a4 + 8);
        result = MiMoveBadPageChargesCrossPartition(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(v_rdi + 24 + 16)) ^ (v_r12);
    result = (result) & (a1);
    result = (result) ^ (v_r12);
    *(unsigned __int64 *)(v_rdi + 24 + 16) = result;
    v_rdi = (v_rdi) + (48);
    v_rbx = (v_rdi + 24) + (48);
    if (v_rdi != v_r13) goto loc_0068FC56;
    if ((*(unsigned int *)(v_rip + 9662549)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m78);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = MiUpdatePartitionChildPageCounts(*(unsigned __int64 *)(a4), *(unsigned __int64 *)(a4 + 8), v_r15, v_r14);
    goto loc_00690089;
loc_0068FD06:
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 2) goto loc_0068FF1B;
    if (((unsigned int)((unsigned int)(v_stack_p10) - 11)) <= ((unsigned int)(*(unsigned __int64 *)(a4 + 8)))) goto loc_0068FF1B;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 13) goto loc_0068FD27;
    goto loc_00690093;
loc_0068FD27:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a4) + 12) = (unsigned __int8)(*(unsigned __int64 *)(a4 + 8));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24) == 0) goto loc_0068FD6E;
    a2 = (*(unsigned __int64 *)(v_stack_p8 + 24)) & (v_r15);
loc_0068FD4B:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24) + 24)) & (v_r15);
    if (a2 >= a1) goto loc_0068FD5C;
    goto loc_0068FD69;
loc_0068FD5C:
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 32));
    if (a2 < a1) goto loc_0068FD6E;
loc_0068FD69:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) != 0) goto loc_0068FD4B;
loc_0068FD6E:
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 24)) & (v_r15);
    a2 = (v_r15) - (result);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32)) - (a2);
    v_rbx = v_r14;
    if (result <= v_r14) { v_rbx = result; }
    result = RtlClearBitsEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32, a2, v_rbx, v_r14);
    v_r15 = (v_r15) + (v_rbx);
    v_r14 = (v_r14) - (v_rbx);
    if (condition_is_equal) goto loc_0068FDF2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8) == 0) goto loc_0068FDE8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8)) == 0) goto loc_0068FDF2;
loc_0068FDD0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8))) != 0) goto loc_0068FDD0;
    goto loc_0068FDF2;
loc_0068FDE0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8))))) goto loc_0068FDF2;
loc_0068FDE8:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0068FDE0;
loc_0068FDF2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32) == 0) goto loc_0068FEF3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32)) > 1) goto loc_0068FE25;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32)) != 1) goto loc_0068FEF3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32)) < 1) goto loc_0068FEF3;
    goto loc_0068FE8D;
loc_0068FE25:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32))) goto loc_0068FEF3;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32) - 1) >> (6);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8) + result * 8)) goto loc_0068FE5D;
    result = (result) | (-1);
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32))));
    result = (result) >> ((unsigned __int8)(a1));
    goto loc_0068FE86;
loc_0068FE5D:
loc_0068FE60:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8)) != 0) goto loc_0068FEF3;
    a1 = (a1) + (8);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8) + result * 8)) goto loc_0068FE77;
    goto loc_0068FE60;
loc_0068FE77:
    result = (result) | (-1);
    a1 = (unsigned __int8)(~((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32) - 1)));
    result = (result) >> ((unsigned __int8)(a1));
loc_0068FE86:
    result = (((result) & (*(unsigned __int64 *)(a1))) == 0) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_0068FEF3;
loc_0068FE8D:
    a1 = (*(unsigned __int64 *)(a4)) + (24);
    result = RtlAvlRemoveNode(a1, v_stack_m80, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32 + 8) + result * 8);
    a3 = 0;
    if (*(unsigned __int64 *)(a4 + 32) == 0) goto loc_0068FEE7;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 24)) & (0);
loc_0068FEBD:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 24)) & (0);
    if (a1 >= result) goto loc_0068FED6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32)) != 0) goto loc_0068FEDF;
    a3 = 0;
    goto loc_0068FEE7;
loc_0068FED6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 8) == 0) goto loc_0068FEE4;
loc_0068FEDF:
    goto loc_0068FEBD;
loc_0068FEE4:
loc_0068FEE7:
    result = RtlAvlInsertNodeEx(a4 + 32, *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 8), 1, v_stack_m80);
loc_0068FEF3:
    if (v_r14 != 0) goto loc_0068FD6E;
    goto loc_00690093;
loc_0068FF1B:
    v_rbx = (v_stack_m78) << (12);
    v_stack_m68 = v_rbx;
    if ((*(unsigned __int8 *)(a4 + 17)) == 0) goto loc_0068FF5C;
    if (v_stack_p20 == 0) goto loc_0068FF3B;
    if ((*(unsigned int *)(a4 + 20)) == ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32) - 1))) {
        *(unsigned int *)(a4 + 20) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 8));
    }
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20)));
    result = MiHotAddHugeRange(*(unsigned __int64 *)(a4), v_r15, v_stack_m78, *(unsigned __int8 *)(a4 + 16));
    goto loc_0068FFDA;
loc_0068FF5C:
    result = (v_r15) << (12);
    v_stack_m58 = result;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24)) + 8) + 32) - 1))) goto loc_0068FF7A;
    a3 = 0;
    a2 = (unsigned int)(((unsigned int)(v_stack_p20)) - (-128));
    a2 = (unsigned int)((a2) << (9));
    goto loc_0068FF8E;
loc_0068FF7A:
    a2 = 128;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 11) { a2 = (unsigned int)((unsigned int)(0x20000ULL)); }
loc_0068FF8E:
    v_stack_m90 = (unsigned int)((unsigned int)(a2));
    a1 = (unsigned int)(a2);
    if ((*(unsigned __int8 *)(a4 + 16)) == 0) { a1 = a2; }
    a2 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 16))) & (64)) == 0) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)(a2);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)))) & (128)) == 0) { a1 = a2; }
    v_stack_m98 = (unsigned int)(a1);
    result = MiAddPhysicalMemoryChunks(*(unsigned __int64 *)(a4), v_stack_m58, v_stack_m68, *(unsigned __int64 *)(a4 + 56));
loc_0068FFDA:
    if ((*(unsigned __int8 *)(a4 + 17)) != 0) goto loc_00690027;
    if ((*(unsigned __int64 *)(a4)) == (v_rip + 8031497)) goto loc_00690027;
    a2 = (v_r15 + 511) & (-512);
    a3 = (a2 + v_stack_m68 * 1) & (-512);
    result = -512;
    if (a2 < a3) {
        a3 = (a3) - (a2);
        a4 = 1;
        result = MiUpdateLargePageBitMap(v_rip + 8031497, a2, a3, a4);
    }
    if (v_stack_m68 != v_stack_m78) goto loc_006900C6;
    goto loc_00690089;
loc_00690037:
    if ((unsigned int)(v_rip + 8031497) == 0) goto loc_0069004D;
    result = MiHotRemoveHugeRange(v_r15, v_stack_m78, (unsigned int)(a2), a4);
    result = 0;
    goto loc_00690061;
loc_0069004D:
    v_stack_m98 = (unsigned int)(a4);
    result = MiHotRemovePartitionPageRun(v_r15, v_stack_m78, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), (unsigned int)(v_stack_p20));
loc_00690061:
    *(unsigned int *)(a4 + 24) = (unsigned int)(result);
    if (sign_flag) goto loc_00690105;
    result = RtlClearBitsEx(v_stack_p8 + 32, v_rdi, v_stack_m78, (unsigned int)(v_stack_p20));
loc_00690089:
loc_00690093:
    *(unsigned __int64 *)(a4 + 40) = v_xmm1;
    if (v_stack_m50 >= (*(unsigned __int64 *)(v_stack_p8 + 32))) goto loc_00690105;
    goto loc_0068F874;
loc_006900C6:
    *(unsigned int *)(a4 + 24) = 0xC0000001ULL;
    a3 = (*(unsigned __int64 *)(v_stack_p8 + 32)) - (v_rdi);
    a3 = (a3) - (v_stack_p8 + 32);
    result = RtlClearBitsEx(v_stack_p8 + 32, v_rdi + v_stack_p8 + 32 * 1, a3, (unsigned int)(v_stack_p18));
    if (v_stack_p8 + 32 != 0) {
        result = 1;
    }
loc_00690105:
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiActOnPartitionNodePages(void *Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    if (((uint32_t)((uint32_t)(Arg2))) > 3) goto loc_0068F85E;
    result = *(uint64_t *)(arg1 + 0x18);
    if (((uint32_t)((uint32_t)(Arg2))) < 3) {
        v_stack_p20 = 1;
        result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
        *(uint64_t *)(arg1 + 0x18) = result;
    }
    local_r14 = 0;
    v_stack_m60 = Arg1 + 32;
loc_0068F874:
    local_r15 = (local_r15) | (-1);
    if ((*(uint64_t *)(arg1 + 0x18)) >= 0) goto loc_0068F899;
    local_rdi = 0;
    Arg2 = 0;
    goto loc_0068FA60;
loc_0068F899:
    Arg4 = ((uint32_t)(Arg3)) & (*(uint64_t *)(arg1 + 0x20));
loc_0068F8B3:
    result = (*(uint64_t *)(arg1 + 0x20) - 1) - (Arg4);
    result = (result) + (1);
    if (result >= 1) goto loc_0068F8CA;
loc_0068F8C5:
    goto loc_0068F930;
loc_0068F8CA:
    result = (*(uint64_t *)(arg1 + 0x20) - 1) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(Arg4)) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - (1);
    result = (Arg4) >> (6);
    result = ~(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8));
    Arg2 = (Arg2) | (result);
loc_0068F8F8:
    if (Arg2 != local_r15) goto loc_0068F90E;
    local_rdi = (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8) + (8);
    if (local_rdi > (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8)) goto loc_0068F8C5;
    Arg2 = ~(*(uint64_t *)(local_rdi));
    goto loc_0068F8F8;
loc_0068F90E:
    local_rdi = (local_rdi) - (*(uint64_t *)(arg1 + 0x20 + 0x8));
    Arg2 = ~(Arg2);
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) + (result);
    v_stack_m70 = (uint32_t)(result);
    if (local_rdi > (*(uint64_t *)(arg1 + 0x20) - 1)) goto loc_0068F8C5;
    if (local_rdi != local_r15) goto loc_0068F94B;
loc_0068F930:
    if (Arg4 == NULL) goto loc_0068F94B;
    Arg3 = *(uint64_t *)(arg1 + 0x20) + 1;
    if ((*(uint64_t *)(arg1 + 0x20) + 1) > (*(uint64_t *)(arg1 + 0x20))) { Arg3 = *(uint64_t *)(arg1 + 0x20); }
    Arg3 = (Arg3) - (1);
    Arg4 = 0;
    goto loc_0068F8B3;
loc_0068F94B:
    if (local_rdi < (*(uint64_t *)(arg1 + 0x20))) goto loc_00690105;
    if (local_rdi == local_r15) goto loc_00690105;
    Arg2 = 0;
    if ((*(uint64_t *)(arg1 + 0x20)) <= local_rdi) goto loc_0068FA3A;
    Arg1 = (uint8_t)(((uint8_t)(local_rdi)) & (63));
    result = (*(uint64_t *)(arg1 + 0x20) - 1) >> (6);
    result = (local_rdi) >> (6);
    result = ((uint32_t)((uint32_t)(Arg2 + 1))) << ((uint8_t)(Arg1));
    result = (result) - (Arg2 + 1);
    Arg4 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8)) | (result);
loc_0068F9A9:
    Arg4 = ~(Arg4);
    if (Arg4 != NULL) goto loc_0068F9C3;
    if ((*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8 + 8) > (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8)) goto loc_0068F9E2;
    Arg3 = (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8) + (8);
    result = (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8 + 8) + (8);
    goto loc_0068F9A9;
loc_0068F9C3:
    local_r14 = (Arg3) - (*(uint64_t *)(arg1 + 0x20 + 0x8));
    local_r14 = (local_r14) >> (3);
    local_r14 = (local_r14) << (6);
    local_r14 = (local_r14) + ((uint32_t)((uint32_t)(Arg1)));
    v_stack_m88 = (uint32_t)(Arg1);
    if (local_r14 <= (*(uint64_t *)(arg1 + 0x20))) goto loc_0068F9E7;
loc_0068F9E2:
    goto loc_0068FA35;
loc_0068F9E7:
    result = (Arg2 + 1) << ((uint8_t)(Arg1));
    result = (result) - (Arg2 + 1);
    result = (result) | (*(uint64_t *)(Arg3));
    result = ~(result);
loc_0068F9F6:
    if (result != 0) goto loc_0068FA13;
    if ((Arg3 + 8) > (*(uint64_t *)(arg1 + 0x20 + 0x8) + result * 8)) goto loc_0068FA0C;
    goto loc_0068F9F6;
loc_0068FA0C:
    goto loc_0068FA17;
loc_0068FA13:
loc_0068FA17:
    v_stack_m88 = 64;
    Arg2 = (Arg3 + 8) - (*(uint64_t *)(arg1 + 0x20 + 0x8));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    Arg2 = (Arg2) + (64);
    if (Arg2 > (*(uint64_t *)(arg1 + 0x20))) { Arg2 = *(uint64_t *)(arg1 + 0x20); }
    Arg2 = (Arg2) - (*(uint64_t *)(arg1 + 0x20));
loc_0068FA35:
    local_r14 = *(uint64_t *)(arg1 + 0x20);
    if (Arg2 == 0) {
        local_r14 = *(uint64_t *)(arg1 + 0x20);
    }
    local_r14 = (local_r14) - (local_rdi);
loc_0068FA60:
    result = (local_rdi + local_r14 * 1) + (Arg2);
    v_stack_m78 = local_r14;
    Arg1 = 0;
    v_stack_m50 = result;
    local_r15 = (*(uint64_t *)(arg1 + 0x18)) & (Arg3 + 8);
    local_r15 = (local_r15) + (local_rdi);
    if (((uint32_t)((uint32_t)(v_stack_p10) - 11)) <= ((uint32_t)(Arg1 + 1))) goto loc_0068FAF9;
    if (local_r15 > (*(uint64_t *)(v_rip + 0x79E252))) goto loc_0068FAB0;
    result = (local_r15 + local_r15 * 2) + (local_r15 + local_r15 * 2);
    result = (*(uint64_t *)(arg1 + 0x1 + result * 8)) >> (54);
    if ((((uint32_t)(Arg1 + 1)) & ((uint32_t)(result))) == 0) {
        Arg1 = (uint32_t)(Arg1 + 1);
    }
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 7) goto loc_00690093;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 8) goto loc_0068FADD;
    result = (*(uint64_t *)(arg4 + 0x28)) + (Arg1 + 1);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(arg4 + 0x40));
    *(uint64_t *)(result) = local_r15;
    *(uint64_t *)(result + 0x8) = local_r14;
    goto loc_00690093;
loc_0068FADD:
    if ((uint32_t)((uint32_t)(v_stack_p10)) != 0) goto loc_0068FAF9;
    v_stack_m98 = (uint32_t)((uint32_t)(v_stack_p20));
    result = MiFreePartitionPageRun(Arg1, local_r15, local_r14, (uint32_t)(v_stack_p18));
    goto loc_00690089;
loc_0068FAF9:
    if ((((uint32_t)((uint32_t)(v_stack_p10) - 1)) & (0xFFFFFFFDULL)) == 0) goto loc_00690037;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 4) goto loc_0068FB4C;
    if ((uint32_t)(Arg1) != 0) goto loc_00690093;
    Arg2 = (local_r15 + 511) & (-512);
    Arg3 = (Arg2 + local_r14 * 1) & (-512);
    if (Arg2 >= Arg3) goto loc_00690089;
    Arg3 = (Arg3) - (Arg2);
    result = MiUpdateLargePageBitMap(*(uint64_t *)(arg4), Arg2, Arg3, (uint32_t)(v_stack_p10) - 3);
    goto loc_00690089;
loc_0068FB4C:
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 5) goto loc_0068FB7E;
    result = MiSplitPfnBitMapsForPartitionHierarchy(*(uint64_t *)(arg4), local_r15, local_r14, (uint32_t)(v_stack_p10) - 3);
    if ((uint32_t)(result) != 0) goto loc_00690093;
    *(uint32_t *)(arg4 + 0x18) = 0xC000009AULL;
    goto loc_00690093;
loc_0068FB7E:
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 6) goto loc_0068FBC8;
    if ((uint32_t)(*(uint64_t *)(arg4)) == 0) {
        Arg1 = *(uint64_t *)(arg4);
        Arg3 = local_r14 + 511;
        Arg3 = (Arg3) + (local_r15);
        Arg2 = local_r15;
        Arg3 = (Arg3) & (-512);
        Arg2 = (Arg2) & (-512);
        Arg3 = (Arg3) - (Arg2);
        Arg4 = 0;
        result = MiUpdateLargePageBitMap(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiTransferPartitionPageRun(*(uint64_t *)(arg4 + 0x8), *(uint64_t *)(arg4), local_r15, local_r14);
    goto loc_00690089;
loc_0068FBC8:
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 10) goto loc_0068FD06;
    if ((uint32_t)(*(uint64_t *)(arg4 + 0x8)) == 0) goto loc_0068FBED;
    result = MiSetHugeRangePartitionId(*(uint64_t *)(arg4), *(uint64_t *)(arg4 + 0x8), local_r15, local_r14);
    goto loc_00690089;
loc_0068FBED:
    if ((*(uint64_t *)(arg4 + 0x8)) != (v_rip + 8032952)) {
        Arg4 = 0;
        Arg3 = local_r14;
        Arg2 = local_r15;
        result = MiUpdateLargePageBitMap(*(uint64_t *)(arg4 + 0x8), Arg2, Arg3, Arg4);
    }
    local_rdi = (local_r15 + local_r15 * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg4));
    local_r13 = (local_r14 + local_r14 * 2) << (4);
    local_r13 = (local_r13) + (local_rdi);
    v_stack_m78 = v_cr8;
    result = v_cr8;
    if ((*(uint32_t *)(v_rip + 0x9370DE)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 2, Arg3, Arg4);
    }
    local_r12 = (*(uint16_t *)(*(uint64_t *)(arg4))) << (43);
loc_0068FC56:
loc_0068FC5A:
    if (condition_is_above_or_equal) goto loc_0068FC75;
loc_0068FC62:
    result = KeYieldProcessorEx(v_stack_m80, 2, Arg3, Arg4);
    if (sign_flag) goto loc_0068FC62;
    goto loc_0068FC5A;
loc_0068FC75:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x18 + 0x8))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) {
        Arg3 = *(uint64_t *)(arg4);
        Arg1 = local_rdi;
        Arg2 = *(uint64_t *)(arg4 + 0x8);
        result = MiMoveBadPageChargesCrossPartition(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(local_rdi + 0x18 + 0x10)) ^ (local_r12);
    result = (result) & (Arg1);
    result = (result) ^ (local_r12);
    *(uint64_t *)(local_rdi + 0x18 + 0x10) = result;
    local_rdi = (local_rdi) + (48);
    local_rbx = (local_rdi + 24) + (48);
    if (local_rdi != local_r13) goto loc_0068FC56;
    if ((*(uint32_t *)(v_rip + 0x937055)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m78);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUpdatePartitionChildPageCounts(*(uint64_t *)(arg4), *(uint64_t *)(arg4 + 0x8), local_r15, local_r14);
    goto loc_00690089;
loc_0068FD06:
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 2) goto loc_0068FF1B;
    if (((uint32_t)((uint32_t)(v_stack_p10) - 11)) <= ((uint32_t)(*(uint64_t *)(arg4 + 0x8)))) goto loc_0068FF1B;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 13) goto loc_0068FD27;
    goto loc_00690093;
loc_0068FD27:
    *(uint8_t *)(*(uint64_t *)(arg4) + 0xC) = (uint8_t)(*(uint64_t *)(arg4 + 0x8));
    if (*(uint64_t *)(*(uint64_t *)(arg4) + 0x18) == 0) goto loc_0068FD6E;
    Arg2 = (*(uint64_t *)(v_stack_p8 + 0x18)) & (local_r15);
loc_0068FD4B:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18) + 0x18)) & (local_r15);
    if (Arg2 >= Arg1) goto loc_0068FD5C;
    goto loc_0068FD69;
loc_0068FD5C:
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x20));
    if (Arg2 < Arg1) goto loc_0068FD6E;
loc_0068FD69:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) != 0) goto loc_0068FD4B;
loc_0068FD6E:
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x18)) & (local_r15);
    Arg2 = (local_r15) - (result);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20)) - (Arg2);
    local_rbx = local_r14;
    if (result <= local_r14) { local_rbx = result; }
    result = RtlClearBitsEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 32, Arg2, local_rbx, local_r14);
    local_r15 = (local_r15) + (local_rbx);
    local_r14 = (local_r14) - (local_rbx);
    if (condition_is_equal) goto loc_0068FDF2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8) == 0) goto loc_0068FDE8;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8)) == 0) goto loc_0068FDF2;
loc_0068FDD0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8))) != 0) goto loc_0068FDD0;
    goto loc_0068FDF2;
loc_0068FDE0:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8))))) goto loc_0068FDF2;
loc_0068FDE8:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0068FDE0;
loc_0068FDF2:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20) == 0) goto loc_0068FEF3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20)) > 1) goto loc_0068FE25;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20)) != 1) goto loc_0068FEF3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20)) < 1) goto loc_0068FEF3;
    goto loc_0068FE8D;
loc_0068FE25:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8)) < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20))) goto loc_0068FEF3;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20) - 1) >> (6);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8) + result * 8)) goto loc_0068FE5D;
    result = (result) | (-1);
    Arg1 = (uint8_t)((64) - ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20))));
    result = (result) >> ((uint8_t)(Arg1));
    goto loc_0068FE86;
loc_0068FE5D:
loc_0068FE60:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8)) != 0) goto loc_0068FEF3;
    Arg1 = (Arg1) + (8);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8) + result * 8)) goto loc_0068FE77;
    goto loc_0068FE60;
loc_0068FE77:
    result = (result) | (-1);
    Arg1 = (uint8_t)(~((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20) - 1)));
    result = (result) >> ((uint8_t)(Arg1));
loc_0068FE86:
    result = (((result) & (*(uint64_t *)(arg1))) == 0) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_0068FEF3;
loc_0068FE8D:
    Arg1 = (*(uint64_t *)(arg4)) + (24);
    result = RtlAvlRemoveNode(Arg1, v_stack_m80, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20 + 0x8) + result * 8);
    Arg3 = 0;
    if (*(uint64_t *)(arg4 + 0x20) == 0) goto loc_0068FEE7;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x18)) & (0);
loc_0068FEBD:
    result = (*(uint64_t *)(*(uint64_t *)(arg4 + 0x20) + 0x18)) & (0);
    if (Arg1 >= result) goto loc_0068FED6;
    if (*(uint64_t *)(*(uint64_t *)(arg4 + 0x20)) != 0) goto loc_0068FEDF;
    Arg3 = 0;
    goto loc_0068FEE7;
loc_0068FED6:
    if (*(uint64_t *)(*(uint64_t *)(arg4 + 0x20) + 0x8) == 0) goto loc_0068FEE4;
loc_0068FEDF:
    goto loc_0068FEBD;
loc_0068FEE4:
loc_0068FEE7:
    result = RtlAvlInsertNodeEx(Arg4 + 32, *(uint64_t *)(*(uint64_t *)(arg4 + 0x20) + 0x8), 1, v_stack_m80);
loc_0068FEF3:
    if (local_r14 != 0) goto loc_0068FD6E;
    goto loc_00690093;
loc_0068FF1B:
    local_rbx = (v_stack_m78) << (12);
    v_stack_m68 = local_rbx;
    if ((*(uint8_t *)(arg4 + 0x11)) == 0) goto loc_0068FF5C;
    if (v_stack_p20 == 0) goto loc_0068FF3B;
    if ((*(uint32_t *)(arg4 + 0x14)) == ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20) - 1))) {
        *(uint32_t *)(arg4 + 0x14) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(arg4 + 0x20) + 0x8));
    }
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x14)));
    result = MiHotAddHugeRange(*(uint64_t *)(arg4), local_r15, v_stack_m78, *(uint8_t *)(arg4 + 0x10));
    goto loc_0068FFDA;
loc_0068FF5C:
    result = (local_r15) << (12);
    v_stack_m58 = result;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x18)) + 0x8) + 0x20) - 1))) goto loc_0068FF7A;
    Arg3 = 0;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p20)) - (-128));
    Arg2 = (uint32_t)((Arg2) << (9));
    goto loc_0068FF8E;
loc_0068FF7A:
    Arg2 = 128;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 11) { Arg2 = (uint32_t)((uint32_t)(0x20000ULL)); }
loc_0068FF8E:
    v_stack_m90 = (uint32_t)((uint32_t)(Arg2));
    Arg1 = (uint32_t)(Arg2);
    if ((*(uint8_t *)(arg4 + 0x10)) == 0) { Arg1 = Arg2; }
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)(*(uint8_t *)(arg4 + 0x10))) & (64)) == 0) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)(Arg2);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)))) & (128)) == 0) { Arg1 = Arg2; }
    v_stack_m98 = (uint32_t)(Arg1);
    result = MiAddPhysicalMemoryChunks(*(uint64_t *)(arg4), v_stack_m58, v_stack_m68, *(uint64_t *)(arg4 + 0x38));
loc_0068FFDA:
    if ((*(uint8_t *)(arg4 + 0x11)) != 0) goto loc_00690027;
    if ((*(uint64_t *)(arg4)) == (v_rip + 8031497)) goto loc_00690027;
    Arg2 = (local_r15 + 511) & (-512);
    Arg3 = (Arg2 + v_stack_m68 * 1) & (-512);
    result = -512;
    if (Arg2 < Arg3) {
        Arg3 = (Arg3) - (Arg2);
        Arg4 = 1;
        result = MiUpdateLargePageBitMap(v_rip + 8031497, Arg2, Arg3, Arg4);
    }
    if (v_stack_m68 != v_stack_m78) goto loc_006900C6;
    goto loc_00690089;
loc_00690037:
    if ((uint32_t)(v_rip + 8031497) == 0) goto loc_0069004D;
    result = MiHotRemoveHugeRange(local_r15, v_stack_m78, (uint32_t)(Arg2), Arg4);
    result = 0;
    goto loc_00690061;
loc_0069004D:
    v_stack_m98 = (uint32_t)(Arg4);
    result = MiHotRemovePartitionPageRun(local_r15, v_stack_m78, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), (uint32_t)(v_stack_p20));
loc_00690061:
    *(uint32_t *)(arg4 + 0x18) = (uint32_t)(result);
    if (sign_flag) goto loc_00690105;
    result = RtlClearBitsEx(v_stack_p8 + 32, local_rdi, v_stack_m78, (uint32_t)(v_stack_p20));
loc_00690089:
loc_00690093:
    *(uint64_t *)(arg4 + 0x28) = v_xmm1;
    if (v_stack_m50 >= (*(uint64_t *)(v_stack_p8 + 0x20))) goto loc_00690105;
    goto loc_0068F874;
loc_006900C6:
    *(uint32_t *)(arg4 + 0x18) = 0xC0000001ULL;
    Arg3 = (*(uint64_t *)(v_stack_p8 + 0x20)) - (local_rdi);
    Arg3 = (Arg3) - (v_stack_p8 + 32);
    result = RtlClearBitsEx(v_stack_p8 + 32, local_rdi + v_stack_p8 + 32 * 1, Arg3, (uint32_t)(v_stack_p18));
    if (v_stack_p8 + 32 != 0) {
        result = 1;
    }
loc_00690105:
    local_rsp = (local_rsp) + (120);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `8` | `R` |
| `Arg4` | `+ 0x11` | `8` | `R` |
| `Arg4` | `+ 0x14` | `32` | `R` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `32` | `R/W` |
| `Arg4` | `+ 0x18` | `32` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x28` | `64` | `R/W` |
| `Arg4` | `+ 0x28` | `128` | `R` |
| `Arg4` | `+ 0x28` | `128` | `W` |
| `Arg4` | `+ 0x30` | `64` | `R/W` |
| `Arg4` | `+ 0x38` | `64` | `R` |
| `Arg4` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068F7F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
