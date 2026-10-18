# MiFlushRelease

- RVA: `0x002982C0`–`0x002986CC` (길이 `1,036` bytes)
- VA: `0x00000001402982C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067ACC`
- 디코드: `270`개 명령, `1,036/1,036` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002982FF` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00298384` → [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) (function, `0x002861B0`)
- `0x002983E2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0029842F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00298443` → [MiControlAreaExemptFromCrossPartitionCharges](MiControlAreaExemptFromCrossPartitionCharges_function_00298930.md) (function, `0x00298930`)
- `0x002984D4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00298507` → [MiInsertUnusedSubsection](MiInsertUnusedSubsection_function_00298D50.md) (function, `0x00298D50`)
- `0x00298522` → [MiControlAreaExemptFromCrossPartitionCharges](MiControlAreaExemptFromCrossPartitionCharges_function_00298930.md) (function, `0x00298930`)
- `0x002985B3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002985E6` → [MiInsertUnusedSubsection](MiInsertUnusedSubsection_function_00298D50.md) (function, `0x00298D50`)
- `0x00298612` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x0029861D` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x00298641` → [MiUpdateSubsectionCrossPartitionRefs](../4F/MiUpdateSubsectionCrossPartitionRefs_function_004FB5DC.md) (function, `0x004FB5DC`)
- `0x00298650` → [MiComputeCrossPartitionSectionCharges](../32/MiComputeCrossPartitionSectionCharges_function_00325BBC.md) (function, `0x00325BBC`)
- `0x0029866C` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x00298677` → [MiGetSubsectionHoldingCrossPartitionReferences](../45/MiGetSubsectionHoldingCrossPartitionReferences_function_004589E4.md) (function, `0x004589E4`)
- `0x0029869B` → [MiUpdateSubsectionCrossPartitionRefs](../4F/MiUpdateSubsectionCrossPartitionRefs_function_004FB5DC.md) (function, `0x004FB5DC`)
- `0x002986AA` → [MiComputeCrossPartitionSectionCharges](../32/MiComputeCrossPartitionSectionCharges_function_00325BBC.md) (function, `0x00325BBC`)
- `0x002986C2` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)

### Direct callers
- [MmFlushSection](../23/MmFlushSection_function_002375E4.md) at `0x0023778A`
- [MiFreeOverlappedFlushEntry](MiFreeOverlappedFlushEntry_function_00298240.md) at `0x0029825E`
- [MmTrimSection](../38/MmTrimSection_function_0038A4EC.md) at `0x0038A573`
- [MiCommitFileBackedSection](../../page/88/MiCommitFileBackedSection_function_00882238.md) at `0x00882365`
- [MmFlushVirtualMemory](../../page/9D/MmFlushVirtualMemory_function_009D6F5C.md) at `0x009D71C3`

### Static image references
- `0x002982DC` → RVA `0x00E30088` (`.data`; read)
- `0x00298603` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002982C0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002982C5  55                              push rbp
002982C6  56                              push rsi
002982C7  57                              push rdi
002982C8  41 54                           push r12
002982CA  41 55                           push r13
002982CC  41 56                           push r14
002982CE  41 57                           push r15
002982D0  48 83 EC 30                     sub rsp, 0x30
002982D4  44 0F B7 49 3C                  movzx r9d, word ptr [rcx + 0x3c]
002982D9  48 8B F1                        mov rsi, rcx
002982DC  48 8B 05 A5 7D B9 00            mov rax, qword ptr [rip + 0xb97da5]
002982E3  41 81 E1 FF 03 00 00            and r9d, 0x3ff
002982EA  48 83 C1 48                     add rcx, 0x48
002982EE  4D 8B E8                        mov r13, r8
002982F1  4C 8B F2                        mov r14, rdx
002982F4  33 FF                           xor edi, edi
002982F6  4A 8B 1C C8                     mov rbx, qword ptr [rax + r9*8]
002982FA  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
002982FF  E8 8C 03 FB FF                  call 0x140248690
00298304  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00298308  4D 85 F6                        test r14, r14
0029830B  74 6D                           je 0x14029837a
0029830D  49 8B 0E                        mov rcx, qword ptr [r14]
00298310  8B EF                           mov ebp, edi
00298312  49 8B DE                        mov rbx, r14
00298315  44 8B E7                        mov r12d, edi
00298318  4C 8B 79 40                     mov r15, qword ptr [rcx + 0x40]
0029831C  48 39 7B 08                     cmp qword ptr [rbx + 8], rdi
00298320  0F 85 85 00 00 00               jne 0x1402983ab
00298326  49 3B DE                        cmp rbx, r14
00298329  74 11                           je 0x14029833c
0029832B  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0029832F  4D 85 FF                        test r15, r15
00298332  75 03                           jne 0x140298337
00298334  83 E5 F7                        and ebp, 0xfffffff7
00298337  48 85 DB                        test rbx, rbx
0029833A  75 E0                           jne 0x14029831c
0029833C  49 8B 45 00                     mov rax, qword ptr [r13]
00298340  8B EF                           mov ebp, edi
00298342  49 8B DD                        mov rbx, r13
00298345  4C 8B F7                        mov r14, rdi
00298348  4C 8B 78 40                     mov r15, qword ptr [rax + 0x40]
0029834C  48 39 7B 08                     cmp qword ptr [rbx + 8], rdi
00298350  0F 85 92 00 00 00               jne 0x1402983e8
00298356  49 3B DD                        cmp rbx, r13
00298359  74 11                           je 0x14029836c
0029835B  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0029835F  4D 85 FF                        test r15, r15
00298362  75 03                           jne 0x140298367
00298364  83 E5 F7                        and ebp, 0xfffffff7
00298367  48 85 DB                        test rbx, rbx
0029836A  75 E0                           jne 0x14029834c
0029836C  0F B6 44 24 70                  movzx eax, byte ptr [rsp + 0x70]
00298371  4B 8D 3C 26                     lea rdi, [r14 + r12]
00298375  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0029837A  48 FF 4E 28                     dec qword ptr [rsi + 0x28]
0029837E  0F B6 D0                        movzx edx, al
00298381  48 8B CE                        mov rcx, rsi
00298384  E8 27 DE FE FF                  call 0x1402861b0
00298389  48 85 FF                        test rdi, rdi
0029838C  0F 85 25 03 00 00               jne 0x1402986b7
00298392  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0029839A  48 83 C4 30                     add rsp, 0x30
0029839E  41 5F                           pop r15
002983A0  41 5E                           pop r14
002983A2  41 5D                           pop r13
002983A4  41 5C                           pop r12
002983A6  5F                              pop rdi
002983A7  5E                              pop rsi
002983A8  5D                              pop rbp
002983A9  C3                              ret
002983AA  CC                              int3
002983AB  4C 8B 03                        mov r8, qword ptr [rbx]
002983AE  4C 8B D3                        mov r10, rbx
002983B1  49 39 78 40                     cmp qword ptr [r8 + 0x40], rdi
002983B5  74 7E                           je 0x140298435
002983B7  41 8B 40 38                     mov eax, dword ptr [r8 + 0x38]
002983BB  A8 20                           test al, 0x20
002983BD  75 76                           jne 0x140298435
002983BF  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002983C2  0F BA E0 10                     bt eax, 0x10
002983C6  72 6D                           jb 0x140298435
002983C8  48 39 7B 50                     cmp qword ptr [rbx + 0x50], rdi
002983CC  75 67                           jne 0x140298435
002983CE  45 33 C9                        xor r9d, r9d
002983D1  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002983D6  4C 8B C3                        mov r8, rbx
002983D9  BA 01 20 04 00                  mov edx, 0x42001
002983DE  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
002983E2  E8 79 52 26 00                  call 0x1404fd660
002983E7  CC                              int3
002983E8  4C 8B 03                        mov r8, qword ptr [rbx]
002983EB  4C 8B D3                        mov r10, rbx
002983EE  49 39 78 40                     cmp qword ptr [r8 + 0x40], rdi
002983F2  0F 84 1C 01 00 00               je 0x140298514
002983F8  41 8B 40 38                     mov eax, dword ptr [r8 + 0x38]
002983FC  A8 20                           test al, 0x20
002983FE  0F 85 10 01 00 00               jne 0x140298514
00298404  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00298407  0F BA E0 10                     bt eax, 0x10
0029840B  0F 82 03 01 00 00               jb 0x140298514
00298411  48 39 7B 50                     cmp qword ptr [rbx + 0x50], rdi
00298415  0F 85 F9 00 00 00               jne 0x140298514
0029841B  45 33 C9                        xor r9d, r9d
0029841E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00298423  4C 8B C3                        mov r8, rbx
00298426  BA 01 20 04 00                  mov edx, 0x42001
0029842B  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0029842F  E8 2C 52 26 00                  call 0x1404fd660
00298434  CC                              int3
00298435  8B C5                           mov eax, ebp
00298437  4C 8B CF                        mov r9, rdi
0029843A  24 0C                           and al, 0xc
0029843C  3C 08                           cmp al, 8
0029843E  75 5F                           jne 0x14029849f
00298440  49 8B C8                        mov rcx, r8
00298443  E8 E8 04 00 00                  call 0x140298930
00298448  85 C0                           test eax, eax
0029844A  75 53                           jne 0x14029849f
0029844C  41 0F B7 40 3C                  movzx eax, word ptr [r8 + 0x3c]
00298451  48 8B 0D 30 7C B9 00            mov rcx, qword ptr [rip + 0xb97c30]
00298458  25 FF 03 00 00                  and eax, 0x3ff
0029845D  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00298461  40 F6 C5 10                     test bpl, 0x10
00298465  0F 85 88 01 00 00               jne 0x1402985f3
0029846B  40 84 ED                        test bpl, bpl
0029846E  0F 88 8F 01 00 00               js 0x140298603
00298474  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029847D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00298484  0F B7 81 AE 04 00 00            movzx eax, word ptr [rcx + 0x4ae]
0029848B  48 8B 0D F6 7B B9 00            mov rcx, qword ptr [rip + 0xb97bf6]
00298492  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00298496  48 3B C2                        cmp rax, rdx
00298499  0F 85 70 01 00 00               jne 0x14029860f
0029849F  49 39 78 40                     cmp qword ptr [r8 + 0x40], rdi
002984A3  74 3C                           je 0x1402984e1
002984A5  41 8B 48 38                     mov ecx, dword ptr [r8 + 0x38]
002984A9  F6 C1 20                        test cl, 0x20
002984AC  75 33                           jne 0x1402984e1
002984AE  41 8B 4A 20                     mov ecx, dword ptr [r10 + 0x20]
002984B2  0F BA E1 10                     bt ecx, 0x10
002984B6  72 29                           jb 0x1402984e1
002984B8  49 8B 42 50                     mov rax, qword ptr [r10 + 0x50]
002984BC  48 85 C0                        test rax, rax
002984BF  75 19                           jne 0x1402984da
002984C1  45 33 C9                        xor r9d, r9d
002984C4  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002984C9  4D 8B C2                        mov r8, r10
002984CC  8D 48 1A                        lea ecx, [rax + 0x1a]
002984CF  BA 01 20 04 00                  mov edx, 0x42001
002984D4  E8 87 51 26 00                  call 0x1404fd660
002984D9  CC                              int3
002984DA  48 FF C8                        dec rax
002984DD  49 89 42 50                     mov qword ptr [r10 + 0x50], rax
002984E1  4D 03 E1                        add r12, r9
002984E4  4D 85 FF                        test r15, r15
002984E7  0F 84 39 FE FF FF               je 0x140298326
002984ED  48 39 7B 50                     cmp qword ptr [rbx + 0x50], rdi
002984F1  0F 85 2F FE FF FF               jne 0x140298326
002984F7  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002984FA  0F BA E0 10                     bt eax, 0x10
002984FE  0F 82 22 FE FF FF               jb 0x140298326
00298504  48 8B CB                        mov rcx, rbx
00298507  E8 44 08 00 00                  call 0x140298d50
0029850C  4C 03 E0                        add r12, rax
0029850F  E9 12 FE FF FF                  jmp 0x140298326
00298514  8B C5                           mov eax, ebp
00298516  4C 8B CF                        mov r9, rdi
00298519  24 0C                           and al, 0xc
0029851B  3C 08                           cmp al, 8
0029851D  75 5F                           jne 0x14029857e
0029851F  49 8B C8                        mov rcx, r8
00298522  E8 09 04 00 00                  call 0x140298930
00298527  85 C0                           test eax, eax
00298529  75 53                           jne 0x14029857e
0029852B  41 0F B7 40 3C                  movzx eax, word ptr [r8 + 0x3c]
00298530  48 8B 0D 51 7B B9 00            mov rcx, qword ptr [rip + 0xb97b51]
00298537  25 FF 03 00 00                  and eax, 0x3ff
0029853C  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00298540  40 F6 C5 10                     test bpl, 0x10
00298544  0F 85 B1 00 00 00               jne 0x1402985fb
0029854A  40 84 ED                        test bpl, bpl
0029854D  0F 88 0A 01 00 00               js 0x14029865d
00298553  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029855C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00298563  0F B7 81 AE 04 00 00            movzx eax, word ptr [rcx + 0x4ae]
0029856A  48 8B 0D 17 7B B9 00            mov rcx, qword ptr [rip + 0xb97b17]
00298571  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00298575  48 3B C2                        cmp rax, rdx
00298578  0F 85 EB 00 00 00               jne 0x140298669
0029857E  49 39 78 40                     cmp qword ptr [r8 + 0x40], rdi
00298582  74 3C                           je 0x1402985c0
00298584  41 8B 48 38                     mov ecx, dword ptr [r8 + 0x38]
00298588  F6 C1 20                        test cl, 0x20
0029858B  75 33                           jne 0x1402985c0
0029858D  41 8B 4A 20                     mov ecx, dword ptr [r10 + 0x20]
00298591  0F BA E1 10                     bt ecx, 0x10
00298595  72 29                           jb 0x1402985c0
00298597  49 8B 42 50                     mov rax, qword ptr [r10 + 0x50]
0029859B  48 85 C0                        test rax, rax
0029859E  75 19                           jne 0x1402985b9
002985A0  45 33 C9                        xor r9d, r9d
002985A3  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002985A8  4D 8B C2                        mov r8, r10
002985AB  8D 48 1A                        lea ecx, [rax + 0x1a]
002985AE  BA 01 20 04 00                  mov edx, 0x42001
002985B3  E8 A8 50 26 00                  call 0x1404fd660
002985B8  CC                              int3
002985B9  48 FF C8                        dec rax
002985BC  49 89 42 50                     mov qword ptr [r10 + 0x50], rax
002985C0  4D 03 F1                        add r14, r9
002985C3  4D 85 FF                        test r15, r15
002985C6  0F 84 8A FD FF FF               je 0x140298356
002985CC  48 39 7B 50                     cmp qword ptr [rbx + 0x50], rdi
002985D0  0F 85 80 FD FF FF               jne 0x140298356
002985D6  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002985D9  0F BA E0 10                     bt eax, 0x10
002985DD  0F 82 73 FD FF FF               jb 0x140298356
002985E3  48 8B CB                        mov rcx, rbx
002985E6  E8 65 07 00 00                  call 0x140298d50
002985EB  4C 03 F0                        add r14, rax
002985EE  E9 63 FD FF FF                  jmp 0x140298356
002985F3  48 8B C7                        mov rax, rdi
002985F6  E9 9B FE FF FF                  jmp 0x140298496
002985FB  48 8B C7                        mov rax, rdi
002985FE  E9 72 FF FF FF                  jmp 0x140298575
00298603  48 8D 05 F6 06 BA 00            lea rax, [rip + 0xba06f6]
0029860A  E9 87 FE FF FF                  jmp 0x140298496
0029860F  48 8B CB                        mov rcx, rbx
00298612  E8 CD 03 1C 00                  call 0x1404589e4
00298617  48 8B C8                        mov rcx, rax
0029861A  4C 8B D0                        mov r10, rax
0029861D  E8 C2 03 1C 00                  call 0x1404589e4
00298622  44 8B 58 30                     mov r11d, dword ptr [rax + 0x30]
00298626  41 81 E3 FF FF FF 3F            and r11d, 0x3fffffff
0029862D  41 81 FB FF FF FF 3F            cmp r11d, 0x3fffffff
00298634  0F 84 65 FE FF FF               je 0x14029849f
0029863A  41 8D 53 FF                     lea edx, [r11 - 1]
0029863E  49 8B CA                        mov rcx, r10
00298641  E8 96 2F 26 00                  call 0x1404fb5dc
00298646  41 83 FB 01                     cmp r11d, 1
0029864A  0F 85 4F FE FF FF               jne 0x14029849f
00298650  E8 67 D5 08 00                  call 0x140325bbc
00298655  4C 8B C8                        mov r9, rax
00298658  E9 42 FE FF FF                  jmp 0x14029849f
0029865D  48 8D 05 9C 06 BA 00            lea rax, [rip + 0xba069c]
00298664  E9 0C FF FF FF                  jmp 0x140298575
00298669  48 8B CB                        mov rcx, rbx
0029866C  E8 73 03 1C 00                  call 0x1404589e4
00298671  48 8B C8                        mov rcx, rax
00298674  4C 8B D0                        mov r10, rax
00298677  E8 68 03 1C 00                  call 0x1404589e4
0029867C  44 8B 58 30                     mov r11d, dword ptr [rax + 0x30]
00298680  41 81 E3 FF FF FF 3F            and r11d, 0x3fffffff
00298687  41 81 FB FF FF FF 3F            cmp r11d, 0x3fffffff
0029868E  0F 84 EA FE FF FF               je 0x14029857e
00298694  41 8D 53 FF                     lea edx, [r11 - 1]
00298698  49 8B CA                        mov rcx, r10
0029869B  E8 3C 2F 26 00                  call 0x1404fb5dc
002986A0  41 83 FB 01                     cmp r11d, 1
002986A4  0F 85 D4 FE FF FF               jne 0x14029857e
002986AA  E8 0D D5 08 00                  call 0x140325bbc
002986AF  4C 8B C8                        mov r9, rax
002986B2  E9 C7 FE FF FF                  jmp 0x14029857e
002986B7  4C 8B C7                        mov r8, rdi
002986BA  BA 01 00 00 00                  mov edx, 1
002986BF  48 8B CB                        mov rcx, rbx
002986C2  E8 55 1F 22 00                  call 0x1404ba61c
002986C7  E9 C6 FC FF FF                  jmp 0x140298392
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFlushRelease(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (48);
    a4 = (unsigned int)((*(unsigned __int16 *)(a1 + 60)) & (0x3FFULL));
    a1 = (a1) + (72);
    v_rdi = 0;
    v_stack_p10 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12156325) + a4 * 8);
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    v_stack_p8 = (unsigned __int8)(result);
    if (a2 == 0) goto loc_0029837A;
loc_0029831C:
    if ((*(unsigned __int64 *)(a2 + 8)) != 0) goto loc_002983AB;
loc_00298326:
    if (a2 == a2) goto loc_0029833C;
    v_rbp = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 64) == 0) {
        v_rbp = (unsigned int)((0) & (0xFFFFFFF7ULL));
    }
    if (*(unsigned __int64 *)(a2 + 16) != 0) goto loc_0029831C;
loc_0029833C:
loc_0029834C:
    if ((*(unsigned __int64 *)(a3 + 8)) != 0) goto loc_002983E8;
loc_00298356:
    if (a3 == a3) goto loc_0029836C;
    v_rbp = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 64) == 0) {
        v_rbp = (unsigned int)((0) & (0xFFFFFFF7ULL));
    }
    if (*(unsigned __int64 *)(a3 + 16) != 0) goto loc_0029834C;
loc_0029836C:
loc_0029837A:
    result = MiCheckControlArea(a1, (unsigned __int8)(v_stack_p8), a3, a4);
    if (0 + 0 * 1 != 0) goto loc_002986B7;
loc_00298392:
    v_rsp = (v_rsp) + (48);
    return result;
loc_002983AB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 64)) == (0 + 0 * 1)) goto loc_00298435;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18) + 56)))) & (32)) != 0) goto loc_00298435;
    if (condition_is_below) goto loc_00298435;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) != (0 + 0 * 1)) goto loc_00298435;
    a4 = 0;
    v_stack_p20 = 0 + 0 * 1;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x42001ULL), v_stack_p18, a4);
loc_002983E8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 64)) == (0 + 0 * 1)) goto loc_00298514;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18) + 56)))) & (32)) != 0) goto loc_00298514;
    if (condition_is_below) goto loc_00298514;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) != (0 + 0 * 1)) goto loc_00298514;
    a4 = 0;
    v_stack_p20 = 0 + 0 * 1;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x42001ULL), v_stack_p18, a4);
loc_00298435:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rbp))) & (12));
    if (((unsigned __int8)(result)) != 8) goto loc_0029849F;
    result = MiControlAreaExemptFromCrossPartitionCharges(v_stack_p18, (unsigned int)(0x42001ULL), v_stack_p18, 0 + 0 * 1);
    if ((unsigned int)(result) != 0) goto loc_0029849F;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_p18 + 60)) & (0x3FFULL));
    if ((((unsigned __int8)(v_rbp)) & (16)) != 0) goto loc_002985F3;
    if (sign_flag) goto loc_00298603;
loc_00298496:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12155894) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12155952) + result * 8))) goto loc_0029860F;
loc_0029849F:
    if ((*(unsigned __int64 *)(v_stack_p18 + 64)) == (0 + 0 * 1)) goto loc_002984E1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 56)))) & (32)) != 0) goto loc_002984E1;
    if (condition_is_below) goto loc_002984E1;
    result = *(unsigned __int64 *)(v_stack_p18 + 80);
    if (*(unsigned __int64 *)(v_stack_p18 + 80) == 0) {
        a4 = 0;
        v_stack_p20 = 0 + 0 * 1;
        a3 = v_stack_p18;
        a1 = *(unsigned __int64 *)(v_stack_p18 + 80) + 26;
        a2 = 0x42001ULL;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = (result) - 1;
    *(unsigned __int64 *)(v_stack_p18 + 80) = result;
loc_002984E1:
    v_r12 = (0) + (0);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 64) == 0) goto loc_00298326;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) != (0 + 0 * 1)) goto loc_00298326;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) < (0 + 0 * 1)) goto loc_00298326;
    result = MiInsertUnusedSubsection(v_stack_p18, a2, a3, a4);
    v_r12 = (v_r12) + (result);
    goto loc_00298326;
loc_00298514:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rbp))) & (12));
    if (((unsigned __int8)(result)) != 8) goto loc_0029857E;
    result = MiControlAreaExemptFromCrossPartitionCharges(a3, a2, a3, 0 + 0 * 1);
    if ((unsigned int)(result) != 0) goto loc_0029857E;
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 60)) & (0x3FFULL));
    if ((((unsigned __int8)(v_rbp)) & (16)) != 0) goto loc_002985FB;
    if (sign_flag) goto loc_0029865D;
loc_00298575:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12155671) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12155729) + result * 8))) goto loc_00298669;
loc_0029857E:
    if ((*(unsigned __int64 *)(a3 + 64)) == (0 + 0 * 1)) goto loc_002985C0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 56)))) & (32)) != 0) goto loc_002985C0;
    if (condition_is_below) goto loc_002985C0;
    result = *(unsigned __int64 *)(v_stack_p18 + 80);
    if (*(unsigned __int64 *)(v_stack_p18 + 80) == 0) {
        a4 = 0;
        v_stack_p20 = 0 + 0 * 1;
        a3 = v_stack_p18;
        a1 = *(unsigned __int64 *)(v_stack_p18 + 80) + 26;
        a2 = 0x42001ULL;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = (result) - 1;
    *(unsigned __int64 *)(v_stack_p18 + 80) = result;
loc_002985C0:
    v_r14 = (0) + (0);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 64) == 0) goto loc_00298356;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) != (0 + 0 * 1)) goto loc_00298356;
    if ((*(unsigned __int64 *)(v_stack_p18 + 80)) < (0 + 0 * 1)) goto loc_00298356;
    result = MiInsertUnusedSubsection(v_stack_p18, a2, a3, a4);
    v_r14 = (v_r14) + (result);
    goto loc_00298356;
loc_002985F3:
    goto loc_00298496;
loc_002985FB:
    goto loc_00298575;
loc_00298603:
    goto loc_00298496;
loc_0029860F:
    result = MiGetSubsectionHoldingCrossPartitionReferences(v_stack_p18, a2, a3, a4);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, a2, a3, a4);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x3FFFFFFFULL));
    if (((unsigned int)(v_r11)) == 0x3FFFFFFFULL) goto loc_0029849F;
    result = MiUpdateSubsectionCrossPartitionRefs(result, v_r11 - 1, a3, a4);
    if (((unsigned int)(v_r11)) != 1) goto loc_0029849F;
    result = MiComputeCrossPartitionSectionCharges(result, v_r11 - 1, a3, a4);
    goto loc_0029849F;
loc_0029865D:
    goto loc_00298575;
loc_00298669:
    result = MiGetSubsectionHoldingCrossPartitionReferences(v_stack_p18, v_r11 - 1, a3, result);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, v_r11 - 1, a3, result);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x3FFFFFFFULL));
    if (((unsigned int)(v_r11)) == 0x3FFFFFFFULL) goto loc_0029857E;
    result = MiUpdateSubsectionCrossPartitionRefs(result, v_r11 - 1, a3, result);
    if (((unsigned int)(v_r11)) != 1) goto loc_0029857E;
    result = MiComputeCrossPartitionSectionCharges(result, v_r11 - 1, a3, result);
    goto loc_0029857E;
loc_002986B7:
    result = MiReturnCrossPartitionSectionCharges(v_stack_p18, 1, 0 + 0 * 1, result);
    goto loc_00298392;
}
```

## 5. (Beta) C Style

```c
int64_t MiFlushRelease(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (48);
    a4 = (uint32_t)((*(uint16_t *)(arg1 + 0x3C)) & (0x3FFULL));
    Arg1 = (Arg1) + (72);
    local_rdi = 0;
    v_stack_p10 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB97DA5) + a4 * 8);
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, Arg3, a4);
    v_stack_p8 = (uint8_t)(result);
    if (Arg2 == 0) goto loc_0029837A;
loc_0029831C:
    if ((*(uint64_t *)(Arg2 + 0x8)) != 0) goto loc_002983AB;
loc_00298326:
    if (Arg2 == Arg2) goto loc_0029833C;
    local_rbp = 0;
    if (*(uint64_t *)(*(uint64_t *)(Arg2) + 0x40) == 0) {
        local_rbp = (uint32_t)((0) & (0xFFFFFFF7ULL));
    }
    if (*(uint64_t *)(Arg2 + 0x10) != 0) goto loc_0029831C;
loc_0029833C:
loc_0029834C:
    if ((*(uint64_t *)(arg3 + 0x8)) != 0) goto loc_002983E8;
loc_00298356:
    if (Arg3 == Arg3) goto loc_0029836C;
    local_rbp = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg3) + 0x40) == 0) {
        local_rbp = (uint32_t)((0) & (0xFFFFFFF7ULL));
    }
    if (*(uint64_t *)(arg3 + 0x10) != 0) goto loc_0029834C;
loc_0029836C:
loc_0029837A:
    result = MiCheckControlArea(Arg1, (uint8_t)(v_stack_p8), Arg3, a4);
    if (0 + 0 * 1 != 0) goto loc_002986B7;
loc_00298392:
    local_rsp = (local_rsp) + (48);
    return result;
loc_002983AB:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x40)) == (0 + 0 * 1)) goto loc_00298435;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18) + 0x38)))) & (32)) != 0) goto loc_00298435;
    if (condition_is_below) goto loc_00298435;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) != (0 + 0 * 1)) goto loc_00298435;
    a4 = 0;
    v_stack_p20 = 0 + 0 * 1;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x42001ULL), v_stack_p18, a4);
loc_002983E8:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x40)) == (0 + 0 * 1)) goto loc_00298514;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18) + 0x38)))) & (32)) != 0) goto loc_00298514;
    if (condition_is_below) goto loc_00298514;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) != (0 + 0 * 1)) goto loc_00298514;
    a4 = 0;
    v_stack_p20 = 0 + 0 * 1;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x42001ULL), v_stack_p18, a4);
loc_00298435:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rbp))) & (12));
    if (((uint8_t)(result)) != 8) goto loc_0029849F;
    result = MiControlAreaExemptFromCrossPartitionCharges(v_stack_p18, (uint32_t)(0x42001ULL), v_stack_p18, 0 + 0 * 1);
    if ((uint32_t)(result) != 0) goto loc_0029849F;
    result = (uint32_t)((*(uint16_t *)(v_stack_p18 + 0x3C)) & (0x3FFULL));
    if ((((uint8_t)(local_rbp)) & (16)) != 0) goto loc_002985F3;
    if (sign_flag) goto loc_00298603;
loc_00298496:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97BF6) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97C30) + result * 8))) goto loc_0029860F;
loc_0029849F:
    if ((*(uint64_t *)(v_stack_p18 + 0x40)) == (0 + 0 * 1)) goto loc_002984E1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x38)))) & (32)) != 0) goto loc_002984E1;
    if (condition_is_below) goto loc_002984E1;
    result = *(uint64_t *)(v_stack_p18 + 0x50);
    if (*(uint64_t *)(v_stack_p18 + 0x50) == 0) {
        a4 = 0;
        v_stack_p20 = 0 + 0 * 1;
        Arg3 = v_stack_p18;
        Arg1 = *(uint64_t *)(v_stack_p18 + 0x50) + 26;
        Arg2 = 0x42001ULL;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    result = (result) - 1;
    *(uint64_t *)(v_stack_p18 + 0x50) = result;
loc_002984E1:
    local_r12 = (0) + (0);
    if (*(uint64_t *)(*(uint64_t *)(arg3) + 0x40) == 0) goto loc_00298326;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) != (0 + 0 * 1)) goto loc_00298326;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) < (0 + 0 * 1)) goto loc_00298326;
    result = MiInsertUnusedSubsection(v_stack_p18, Arg2, Arg3, a4);
    local_r12 = (local_r12) + (result);
    goto loc_00298326;
loc_00298514:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rbp))) & (12));
    if (((uint8_t)(result)) != 8) goto loc_0029857E;
    result = MiControlAreaExemptFromCrossPartitionCharges(Arg3, Arg2, Arg3, 0 + 0 * 1);
    if ((uint32_t)(result) != 0) goto loc_0029857E;
    result = (uint32_t)((*(uint16_t *)(arg3 + 0x3C)) & (0x3FFULL));
    if ((((uint8_t)(local_rbp)) & (16)) != 0) goto loc_002985FB;
    if (sign_flag) goto loc_0029865D;
loc_00298575:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97B17) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97B51) + result * 8))) goto loc_00298669;
loc_0029857E:
    if ((*(uint64_t *)(arg3 + 0x40)) == (0 + 0 * 1)) goto loc_002985C0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x38)))) & (32)) != 0) goto loc_002985C0;
    if (condition_is_below) goto loc_002985C0;
    result = *(uint64_t *)(v_stack_p18 + 0x50);
    if (*(uint64_t *)(v_stack_p18 + 0x50) == 0) {
        a4 = 0;
        v_stack_p20 = 0 + 0 * 1;
        Arg3 = v_stack_p18;
        Arg1 = *(uint64_t *)(v_stack_p18 + 0x50) + 26;
        Arg2 = 0x42001ULL;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    result = (result) - 1;
    *(uint64_t *)(v_stack_p18 + 0x50) = result;
loc_002985C0:
    local_r14 = (0) + (0);
    if (*(uint64_t *)(*(uint64_t *)(arg3) + 0x40) == 0) goto loc_00298356;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) != (0 + 0 * 1)) goto loc_00298356;
    if ((*(uint64_t *)(v_stack_p18 + 0x50)) < (0 + 0 * 1)) goto loc_00298356;
    result = MiInsertUnusedSubsection(v_stack_p18, Arg2, Arg3, a4);
    local_r14 = (local_r14) + (result);
    goto loc_00298356;
loc_002985F3:
    goto loc_00298496;
loc_002985FB:
    goto loc_00298575;
loc_00298603:
    goto loc_00298496;
loc_0029860F:
    result = MiGetSubsectionHoldingCrossPartitionReferences(v_stack_p18, Arg2, Arg3, a4);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, Arg2, Arg3, a4);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x3FFFFFFFULL));
    if (((uint32_t)(local_r11)) == 0x3FFFFFFFULL) goto loc_0029849F;
    result = MiUpdateSubsectionCrossPartitionRefs(result, local_r11 - 1, Arg3, a4);
    if (((uint32_t)(local_r11)) != 1) goto loc_0029849F;
    result = MiComputeCrossPartitionSectionCharges(result, local_r11 - 1, Arg3, a4);
    goto loc_0029849F;
loc_0029865D:
    goto loc_00298575;
loc_00298669:
    result = MiGetSubsectionHoldingCrossPartitionReferences(v_stack_p18, local_r11 - 1, Arg3, result);
    result = MiGetSubsectionHoldingCrossPartitionReferences(result, local_r11 - 1, Arg3, result);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x3FFFFFFFULL));
    if (((uint32_t)(local_r11)) == 0x3FFFFFFFULL) goto loc_0029857E;
    result = MiUpdateSubsectionCrossPartitionRefs(result, local_r11 - 1, Arg3, result);
    if (((uint32_t)(local_r11)) != 1) goto loc_0029857E;
    result = MiComputeCrossPartitionSectionCharges(result, local_r11 - 1, Arg3, result);
    goto loc_0029857E;
loc_002986B7:
    result = MiReturnCrossPartitionSectionCharges(v_stack_p18, 1, 0 + 0 * 1, result);
    goto loc_00298392;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x3C` | `16` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002982C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
