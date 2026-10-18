# MiProcessCrcList

- RVA: `0x009F6F94`–`0x009F755C` (길이 `1,480` bytes)
- VA: `0x00000001409F6F94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6CD0`
- 디코드: `401`개 명령, `1,480/1,480` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009F700A` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x009F70AC` → [MiValidCombineProtection](../../text/42/MiValidCombineProtection_function_0042EA70.md) (function, `0x0042EA70`)
- `0x009F710A` → [MiLocateCombineBlock](../../text/22/MiLocateCombineBlock_function_0022B3A8.md) (function, `0x0022B3A8`)
- `0x009F716A` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009F71CA` → [MiCapturePfnVm](../../text/46/MiCapturePfnVm_function_00465570.md) (function, `0x00465570`)
- `0x009F723C` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009F728E` → [RtlAvlInsertNodeEx](../../text/26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x009F72FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F7315` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F73B2` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x009F73EB` → [MiCompareActiveCrcEntries](../../text/43/MiCompareActiveCrcEntries_function_00437A20.md) (function, `0x00437A20`)
- `0x009F741E` → [MiCompareActiveCrcEntries](../../text/43/MiCompareActiveCrcEntries_function_00437A20.md) (function, `0x00437A20`)
- `0x009F7440` → [MiLocateCombineBlock](../../text/22/MiLocateCombineBlock_function_0022B3A8.md) (function, `0x0022B3A8`)
- `0x009F7469` → [MiSharePages](../../text/31/MiSharePages_function_00315110.md) (function, `0x00315110`)
- `0x009F747C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F7486` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F74A1` → [RtlAvlRemoveNode](../../text/29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x009F74E2` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x009F7555` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiCombineWorkingSet](../../text/68/MiCombineWorkingSet_function_0068BB18.md) at `0x0068BCB7`
- [MiCombineWorkingSetTail](../../text/68/MiCombineWorkingSetTail_function_0068BD00.md) at `0x0068BD51`
- [MiCombineAllPhysicalMemory](MiCombineAllPhysicalMemory_function_009F6B6C.md) at `0x009F6EEF`
- [MiCombineAllPhysicalMemory](MiCombineAllPhysicalMemory_function_009F6B6C.md) at `0x009F6F44`

### Static image references
- `0x009F6FE3` → RVA `0x009A8D30` (`MiCombinePageSortByHash`; read)
- `0x009F739F` → RVA `0x00418970` (`MiCombineActiveCrcSortByHash`; read)
- `0x009F74CF` → RVA `0x00458AE0` (`MiCombineActiveCrcSortByVa`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x009F700A` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
  - `0x009F70AC` → [MiValidCombineProtection](../../text/42/MiValidCombineProtection_function_0042EA70.md) (`PAGE` → `.text`)
  - `0x009F710A` → [MiLocateCombineBlock](../../text/22/MiLocateCombineBlock_function_0022B3A8.md) (`PAGE` → `.text`)
  - `0x009F716A` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009F71CA` → [MiCapturePfnVm](../../text/46/MiCapturePfnVm_function_00465570.md) (`PAGE` → `.text`)
  - `0x009F723C` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009F728E` → [RtlAvlInsertNodeEx](../../text/26/RtlAvlInsertNodeEx_function_00265790.md) (`PAGE` → `.text`)
  - `0x009F72FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F7315` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F73B2` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
  - `0x009F73EB` → [MiCompareActiveCrcEntries](../../text/43/MiCompareActiveCrcEntries_function_00437A20.md) (`PAGE` → `.text`)
  - `0x009F741E` → [MiCompareActiveCrcEntries](../../text/43/MiCompareActiveCrcEntries_function_00437A20.md) (`PAGE` → `.text`)
  - `0x009F7440` → [MiLocateCombineBlock](../../text/22/MiLocateCombineBlock_function_0022B3A8.md) (`PAGE` → `.text`)
  - `0x009F7469` → [MiSharePages](../../text/31/MiSharePages_function_00315110.md) (`PAGE` → `.text`)
  - `0x009F747C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F7486` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F74A1` → [RtlAvlRemoveNode](../../text/29/RtlAvlRemoveNode_function_00296650.md) (`PAGE` → `.text`)
  - `0x009F74E2` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
  - `0x009F7555` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F6F94  4D 85 C0                        test r8, r8
009F6F97  0F 84 A2 05 00 00               je 0x1409f753f
009F6F9D  48 8B C4                        mov rax, rsp
009F6FA0  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
009F6FA4  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009F6FA8  48 89 48 08                     mov qword ptr [rax + 8], rcx
009F6FAC  55                              push rbp
009F6FAD  53                              push rbx
009F6FAE  56                              push rsi
009F6FAF  57                              push rdi
009F6FB0  41 54                           push r12
009F6FB2  41 55                           push r13
009F6FB4  41 56                           push r14
009F6FB6  41 57                           push r15
009F6FB8  48 8D 68 A1                     lea rbp, [rax - 0x5f]
009F6FBC  48 81 EC 88 00 00 00            sub rsp, 0x88
009F6FC3  48 83 65 C7 00                  and qword ptr [rbp - 0x39], 0
009F6FC8  48 8B C1                        mov rax, rcx
009F6FCB  8B 89 8C 00 00 00               mov ecx, dword ptr [rcx + 0x8c]
009F6FD1  49 8B D8                        mov rbx, r8
009F6FD4  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
009F6FD7  4C 8B EA                        mov r13, rdx
009F6FDA  0F 57 C0                        xorps xmm0, xmm0
009F6FDD  41 8B F9                        mov edi, r9d
009F6FE0  48 8B 08                        mov rcx, qword ptr [rax]
009F6FE3  4C 8D 0D 46 1D FB FF            lea r9, [rip - 0x4e2ba]
009F6FEA  4C 8B 70 08                     mov r14, qword ptr [rax + 8]
009F6FEE  41 B8 28 00 00 00               mov r8d, 0x28
009F6FF4  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
009F6FF8  48 8B D3                        mov rdx, rbx
009F6FFB  49 8B CD                        mov rcx, r13
009F6FFE  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
009F7002  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
009F7006  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
009F700A  E8 E1 99 B0 FF                  call 0x1405009f0
009F700F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009F7018  48 8D 43 FF                     lea rax, [rbx - 1]
009F701C  48 8D 04 80                     lea rax, [rax + rax*4]
009F7020  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
009F7024  45 33 E4                        xor r12d, r12d
009F7027  48 8D 04 C5 00 00 00 00         lea rax, [rax*8]
009F702F  49 03 C5                        add rax, r13
009F7032  4C 89 65 CF                     mov qword ptr [rbp - 0x31], r12
009F7036  33 D2                           xor edx, edx
009F7038  4C 3B E8                        cmp r13, rax
009F703B  0F 87 07 01 00 00               ja 0x1409f7148
009F7041  49 8D 75 08                     lea rsi, [r13 + 8]
009F7045  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
009F704F  48 8B F8                        mov rdi, rax
009F7052  4D 85 F6                        test r14, r14
009F7055  74 0B                           je 0x1409f7062
009F7057  41 83 7E 04 00                  cmp dword ptr [r14 + 4], 0
009F705C  0F 85 E3 00 00 00               jne 0x1409f7145
009F7062  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
009F7068  A8 01                           test al, 1
009F706A  0F 85 D5 00 00 00               jne 0x1409f7145
009F7070  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009F7074  4C 8D 34 40                     lea r14, [rax + rax*2]
009F7078  49 C1 E6 04                     shl r14, 4
009F707C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
009F7086  4C 03 F0                        add r14, rax
009F7089  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
009F7093  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
009F7097  4D 8B 7E 08                     mov r15, qword ptr [r14 + 8]
009F709B  48 C1 EB 05                     shr rbx, 5
009F709F  4C 0B F8                        or r15, rax
009F70A2  44 8B E3                        mov r12d, ebx
009F70A5  41 83 E4 1F                     and r12d, 0x1f
009F70A9  41 8B CC                        mov ecx, r12d
009F70AC  E8 BF 79 A3 FF                  call 0x14042ea70
009F70B1  85 C0                           test eax, eax
009F70B3  0F 84 D0 00 00 00               je 0x1409f7189
009F70B9  49 8B C0                        mov rax, r8
009F70BC  4C 3B F8                        cmp r15, rax
009F70BF  0F 82 C4 00 00 00               jb 0x1409f7189
009F70C5  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
009F70CF  4C 3B F8                        cmp r15, rax
009F70D2  0F 87 B1 00 00 00               ja 0x1409f7189
009F70D8  48 8D 4E F8                     lea rcx, [rsi - 8]
009F70DC  48 3B CF                        cmp rcx, rdi
009F70DF  74 0D                           je 0x1409f70ee
009F70E1  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
009F70E5  48 39 06                        cmp qword ptr [rsi], rax
009F70E8  0F 84 AE 00 00 00               je 0x1409f719c
009F70EE  49 3B CD                        cmp rcx, r13
009F70F1  0F 85 9C 00 00 00               jne 0x1409f7193
009F70F7  48 8B 16                        mov rdx, qword ptr [rsi]
009F70FA  45 33 C9                        xor r9d, r9d
009F70FD  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
009F7101  45 8B C4                        mov r8d, r12d
009F7104  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009F710A  E8 99 42 83 FF                  call 0x14022b3a8
009F710F  48 85 C0                        test rax, rax
009F7112  0F 85 C9 01 00 00               jne 0x1409f72e1
009F7118  48 21 06                        and qword ptr [rsi], rax
009F711B  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
009F711F  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
009F7129  48 8B 16                        mov rdx, qword ptr [rsi]
009F712C  48 83 C6 28                     add rsi, 0x28
009F7130  4C 8B 75 E7                     mov r14, qword ptr [rbp - 0x19]
009F7134  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
009F7138  48 8D 46 F8                     lea rax, [rsi - 8]
009F713C  48 3B C7                        cmp rax, rdi
009F713F  0F 86 0D FF FF FF               jbe 0x1409f7052
009F7145  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
009F7148  33 F6                           xor esi, esi
009F714A  49 83 CD FF                     or r13, 0xffffffffffffffff
009F714E  4D 85 E4                        test r12, r12
009F7151  0F 84 34 03 00 00               je 0x1409f748b
009F7157  4A 8D 14 E5 00 00 00 00         lea rdx, [r12*8]
009F715F  B9 00 01 00 00                  mov ecx, 0x100
009F7164  41 B8 4D 69 56 6D               mov r8d, 0x6d56694d
009F716A  E8 D1 43 96 FF                  call 0x14035b540
009F716F  48 8B F0                        mov rsi, rax
009F7172  48 85 C0                        test rax, rax
009F7175  0F 84 10 03 00 00               je 0x1409f748b
009F717B  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
009F717F  45 33 C0                        xor r8d, r8d
009F7182  33 C9                           xor ecx, ecx
009F7184  E9 B5 01 00 00                  jmp 0x1409f733e
009F7189  48 83 26 00                     and qword ptr [rsi], 0
009F718D  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
009F7191  EB 96                           jmp 0x1409f7129
009F7193  48 39 16                        cmp qword ptr [rsi], rdx
009F7196  0F 85 5B FF FF FF               jne 0x1409f70f7
009F719C  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
009F71A0  41 BD 01 00 00 00               mov r13d, 1
009F71A6  C1 E8 10                        shr eax, 0x10
009F71A9  24 C0                           and al, 0xc0
009F71AB  3C C0                           cmp al, 0xc0
009F71AD  0F 84 7B 01 00 00               je 0x1409f732e
009F71B3  4C 8B 0E                        mov r9, qword ptr [rsi]
009F71B6  48 8D 45 F7                     lea rax, [rbp - 9]
009F71BA  44 8B 45 77                     mov r8d, dword ptr [rbp + 0x77]
009F71BE  49 8B D6                        mov rdx, r14
009F71C1  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
009F71C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F71CA  E8 A1 E3 A6 FF                  call 0x140465570
009F71CF  4C 8B F0                        mov r14, rax
009F71D2  48 85 C0                        test rax, rax
009F71D5  0F 84 2C 01 00 00               je 0x1409f7307
009F71DB  4C 39 7D FF                     cmp qword ptr [rbp - 1], r15
009F71DF  0F 85 22 01 00 00               jne 0x1409f7307
009F71E5  44 39 65 07                     cmp dword ptr [rbp + 7], r12d
009F71E9  0F 85 18 01 00 00               jne 0x1409f7307
009F71EF  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
009F71F5  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
009F71F8  33 D9                           xor ebx, ecx
009F71FA  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
009F71FE  83 E3 1F                        and ebx, 0x1f
009F7201  33 D9                           xor ebx, ecx
009F7203  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
009F7207  83 E3 DF                        and ebx, 0xffffffdf
009F720A  89 5E 18                        mov dword ptr [rsi + 0x18], ebx
009F720D  48 8B 5D C7                     mov rbx, qword ptr [rbp - 0x39]
009F7211  EB 0F                           jmp 0x1409f7222
009F7213  4C 3B 73 20                     cmp r14, qword ptr [rbx + 0x20]
009F7217  0F 87 2A 03 00 00               ja 0x1409f7547
009F721D  73 08                           jae 0x1409f7227
009F721F  48 8B 1B                        mov rbx, qword ptr [rbx]
009F7222  48 85 DB                        test rbx, rbx
009F7225  75 EC                           jne 0x1409f7213
009F7227  48 85 DB                        test rbx, rbx
009F722A  0F 85 BC 00 00 00               jne 0x1409f72ec
009F7230  8D 53 38                        lea edx, [rbx + 0x38]
009F7233  41 B8 4D 69 56 6D               mov r8d, 0x6d56694d
009F7239  8D 4B 40                        lea ecx, [rbx + 0x40]
009F723C  E8 FF 42 96 FF                  call 0x14035b540
009F7241  48 8B D8                        mov rbx, rax
009F7244  48 85 C0                        test rax, rax
009F7247  0F 84 BA 00 00 00               je 0x1409f7307
009F724D  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
009F7251  45 32 C0                        xor r8b, r8b
009F7254  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
009F7258  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
009F725C  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
009F7260  48 85 D2                        test rdx, rdx
009F7263  74 22                           je 0x1409f7287
009F7265  48 8D 42 20                     lea rax, [rdx + 0x20]
009F7269  4C 3B F0                        cmp r14, rax
009F726C  73 0D                           jae 0x1409f727b
009F726E  48 8B 02                        mov rax, qword ptr [rdx]
009F7271  48 85 C0                        test rax, rax
009F7274  74 11                           je 0x1409f7287
009F7276  48 8B D0                        mov rdx, rax
009F7279  EB EA                           jmp 0x1409f7265
009F727B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
009F727F  48 85 C0                        test rax, rax
009F7282  75 F2                           jne 0x1409f7276
009F7284  41 B0 01                        mov r8b, 1
009F7287  4C 8B CB                        mov r9, rbx
009F728A  48 8D 4D C7                     lea rcx, [rbp - 0x39]
009F728E  E8 FD E4 86 FF                  call 0x140265790
009F7293  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F7297  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
009F729B  48 89 46 F8                     mov qword ptr [rsi - 8], rax
009F729F  49 FF C4                        inc r12
009F72A2  48 FF 43 18                     inc qword ptr [rbx + 0x18]
009F72A6  48 8D 46 F8                     lea rax, [rsi - 8]
009F72AA  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
009F72AE  4C 89 65 CF                     mov qword ptr [rbp - 0x31], r12
009F72B2  49 C1 E7 19                     shl r15, 0x19
009F72B6  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
009F72C0  49 8B C0                        mov rax, r8
009F72C3  48 C1 E0 19                     shl rax, 0x19
009F72C7  4C 2B F8                        sub r15, rax
009F72CA  49 C1 FF 10                     sar r15, 0x10
009F72CE  4C 89 7E 08                     mov qword ptr [rsi + 8], r15
009F72D2  41 83 FD 02                     cmp r13d, 2
009F72D6  74 29                           je 0x1409f7301
009F72D8  4C 8B 6D 6F                     mov r13, qword ptr [rbp + 0x6f]
009F72DC  E9 48 FE FF FF                  jmp 0x1409f7129
009F72E1  41 BD 02 00 00 00               mov r13d, 2
009F72E7  E9 C7 FE FF FF                  jmp 0x1409f71b3
009F72EC  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
009F72F0  48 85 C9                        test rcx, rcx
009F72F3  74 9E                           je 0x1409f7293
009F72F5  BA 4D 6D 43 62                  mov edx, 0x62436d4d
009F72FA  E8 E1 05 90 FF                  call 0x1402f78e0
009F72FF  EB 92                           jmp 0x1409f7293
009F7301  83 4E 18 20                     or dword ptr [rsi + 0x18], 0x20
009F7305  EB D1                           jmp 0x1409f72d8
009F7307  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
009F730B  48 85 C9                        test rcx, rcx
009F730E  74 0A                           je 0x1409f731a
009F7310  BA 4D 6D 43 62                  mov edx, 0x62436d4d
009F7315  E8 C6 05 90 FF                  call 0x1402f78e0
009F731A  48 83 26 00                     and qword ptr [rsi], 0
009F731E  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
009F7322  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
009F732C  EB AA                           jmp 0x1409f72d8
009F732E  48 83 26 00                     and qword ptr [rsi], 0
009F7332  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
009F7336  EB A0                           jmp 0x1409f72d8
009F7338  48 8B C8                        mov rcx, rax
009F733B  48 8B 00                        mov rax, qword ptr [rax]
009F733E  48 85 C0                        test rax, rax
009F7341  75 F5                           jne 0x1409f7338
009F7343  EB 12                           jmp 0x1409f7357
009F7345  48 39 11                        cmp qword ptr [rcx], rdx
009F7348  74 0D                           je 0x1409f7357
009F734A  48 8B D1                        mov rdx, rcx
009F734D  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
009F7351  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
009F7355  75 EE                           jne 0x1409f7345
009F7357  48 85 C9                        test rcx, rcx
009F735A  74 43                           je 0x1409f739f
009F735C  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
009F7360  48 85 C0                        test rax, rax
009F7363  74 13                           je 0x1409f7378
009F7365  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
009F736A  74 04                           je 0x1409f7370
009F736C  4A 89 04 C6                     mov qword ptr [rsi + r8*8], rax
009F7370  48 8B 00                        mov rax, qword ptr [rax]
009F7373  49 FF C0                        inc r8
009F7376  EB E8                           jmp 0x1409f7360
009F7378  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009F737C  48 8B D1                        mov rdx, rcx
009F737F  48 85 C0                        test rax, rax
009F7382  74 C9                           je 0x1409f734d
009F7384  48 8B 10                        mov rdx, qword ptr [rax]
009F7387  48 8B C8                        mov rcx, rax
009F738A  48 85 D2                        test rdx, rdx
009F738D  74 C8                           je 0x1409f7357
009F738F  48 8B 02                        mov rax, qword ptr [rdx]
009F7392  48 8B CA                        mov rcx, rdx
009F7395  48 8B D0                        mov rdx, rax
009F7398  48 85 C0                        test rax, rax
009F739B  75 F2                           jne 0x1409f738f
009F739D  EB B8                           jmp 0x1409f7357
009F739F  4C 8D 0D CA 15 A2 FF            lea r9, [rip - 0x5dea36]
009F73A6  41 B8 08 00 00 00               mov r8d, 8
009F73AC  49 8B D4                        mov rdx, r12
009F73AF  48 8B CE                        mov rcx, rsi
009F73B2  E8 39 96 B0 FF                  call 0x1405009f0
009F73B7  45 33 FF                        xor r15d, r15d
009F73BA  4D 85 E4                        test r12, r12
009F73BD  0F 84 C8 00 00 00               je 0x1409f748b
009F73C3  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
009F73C7  4C 8D 76 08                     lea r14, [rsi + 8]
009F73CB  49 8B 5E F8                     mov rbx, qword ptr [r14 - 8]
009F73CF  44 8B 43 20                     mov r8d, dword ptr [rbx + 0x20]
009F73D3  41 F6 C0 20                     test r8b, 0x20
009F73D7  75 50                           jne 0x1409f7429
009F73D9  4D 85 FF                        test r15, r15
009F73DC  74 2A                           je 0x1409f7408
009F73DE  49 8B 56 F0                     mov rdx, qword ptr [r14 - 0x10]
009F73E2  4C 39 6A 10                     cmp qword ptr [rdx + 0x10], r13
009F73E6  74 20                           je 0x1409f7408
009F73E8  48 8B CB                        mov rcx, rbx
009F73EB  E8 30 06 A4 FF                  call 0x140437a20
009F73F0  85 C0                           test eax, eax
009F73F2  75 14                           jne 0x1409f7408
009F73F4  49 FF C7                        inc r15
009F73F7  49 83 C6 08                     add r14, 8
009F73FB  4D 3B FC                        cmp r15, r12
009F73FE  72 CB                           jb 0x1409f73cb
009F7400  8B 7D 7F                        mov edi, dword ptr [rbp + 0x7f]
009F7403  E9 83 00 00 00                  jmp 0x1409f748b
009F7408  49 8D 44 24 FF                  lea rax, [r12 - 1]
009F740D  4C 3B F8                        cmp r15, rax
009F7410  74 38                           je 0x1409f744a
009F7412  49 8B 16                        mov rdx, qword ptr [r14]
009F7415  4C 39 6A 10                     cmp qword ptr [rdx + 0x10], r13
009F7419  74 2F                           je 0x1409f744a
009F741B  48 8B CB                        mov rcx, rbx
009F741E  E8 FD 05 A4 FF                  call 0x140437a20
009F7423  85 C0                           test eax, eax
009F7425  74 CD                           je 0x1409f73f4
009F7427  EB 21                           jmp 0x1409f744a
009F7429  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
009F742D  48 8D 43 18                     lea rax, [rbx + 0x18]
009F7431  41 83 E0 1F                     and r8d, 0x1f
009F7435  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F743A  45 33 C9                        xor r9d, r9d
009F743D  48 8B CF                        mov rcx, rdi
009F7440  E8 63 3F 83 FF                  call 0x14022b3a8
009F7445  48 85 C0                        test rax, rax
009F7448  75 AA                           jne 0x1409f73f4
009F744A  4C 89 6B 10                     mov qword ptr [rbx + 0x10], r13
009F744E  EB A4                           jmp 0x1409f73f4
009F7450  48 83 7B 18 00                  cmp qword ptr [rbx + 0x18], 0
009F7455  74 17                           je 0x1409f746e
009F7457  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
009F745B  44 8B C7                        mov r8d, edi
009F745E  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009F7462  48 8B D3                        mov rdx, rbx
009F7465  48 89 41 70                     mov qword ptr [rcx + 0x70], rax
009F7469  E8 A2 DC 91 FF                  call 0x140315110
009F746E  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
009F7472  48 85 C9                        test rcx, rcx
009F7475  74 0A                           je 0x1409f7481
009F7477  BA 4D 6D 43 62                  mov edx, 0x62436d4d
009F747C  E8 5F 04 90 FF                  call 0x1402f78e0
009F7481  33 D2                           xor edx, edx
009F7483  48 8B CB                        mov rcx, rbx
009F7486  E8 E5 B3 18 00                  call 0x140b82870
009F748B  48 83 7D C7 00                  cmp qword ptr [rbp - 0x39], 0
009F7490  0F 84 91 00 00 00               je 0x1409f7527
009F7496  48 8B 5D C7                     mov rbx, qword ptr [rbp - 0x39]
009F749A  48 8D 4D C7                     lea rcx, [rbp - 0x39]
009F749E  48 8B D3                        mov rdx, rbx
009F74A1  E8 AA F1 89 FF                  call 0x140296650
009F74A6  48 85 F6                        test rsi, rsi
009F74A9  74 C3                           je 0x1409f746e
009F74AB  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F74AF  45 33 F6                        xor r14d, r14d
009F74B2  48 85 C0                        test rax, rax
009F74B5  74 18                           je 0x1409f74cf
009F74B7  4C 39 68 10                     cmp qword ptr [rax + 0x10], r13
009F74BB  74 0C                           je 0x1409f74c9
009F74BD  4A 89 04 F6                     mov qword ptr [rsi + r14*8], rax
009F74C1  49 FF C6                        inc r14
009F74C4  48 8B 00                        mov rax, qword ptr [rax]
009F74C7  EB E9                           jmp 0x1409f74b2
009F74C9  4C 01 6B 18                     add qword ptr [rbx + 0x18], r13
009F74CD  EB F5                           jmp 0x1409f74c4
009F74CF  4C 8D 0D 0A 16 A6 FF            lea r9, [rip - 0x59e9f6]
009F74D6  41 B8 08 00 00 00               mov r8d, 8
009F74DC  49 8B D6                        mov rdx, r14
009F74DF  48 8B CE                        mov rcx, rsi
009F74E2  E8 09 95 B0 FF                  call 0x1405009f0
009F74E7  48 83 63 30 00                  and qword ptr [rbx + 0x30], 0
009F74EC  33 D2                           xor edx, edx
009F74EE  4D 85 F6                        test r14, r14
009F74F1  0F 84 59 FF FF FF               je 0x1409f7450
009F74F7  4C 8B 04 D6                     mov r8, qword ptr [rsi + rdx*8]
009F74FB  48 85 D2                        test rdx, rdx
009F74FE  74 0F                           je 0x1409f750f
009F7500  48 8B 44 D6 F8                  mov rax, qword ptr [rsi + rdx*8 - 8]
009F7505  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
009F7509  49 39 48 10                     cmp qword ptr [r8 + 0x10], rcx
009F750D  74 32                           je 0x1409f7541
009F750F  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F7513  49 89 00                        mov qword ptr [r8], rax
009F7516  4C 89 43 30                     mov qword ptr [rbx + 0x30], r8
009F751A  48 FF C2                        inc rdx
009F751D  49 3B D6                        cmp rdx, r14
009F7520  72 D5                           jb 0x1409f74f7
009F7522  E9 29 FF FF FF                  jmp 0x1409f7450
009F7527  48 85 F6                        test rsi, rsi
009F752A  75 24                           jne 0x1409f7550
009F752C  48 81 C4 88 00 00 00            add rsp, 0x88
009F7533  41 5F                           pop r15
009F7535  41 5E                           pop r14
009F7537  41 5D                           pop r13
009F7539  41 5C                           pop r12
009F753B  5F                              pop rdi
009F753C  5E                              pop rsi
009F753D  5B                              pop rbx
009F753E  5D                              pop rbp
009F753F  C3                              ret
009F7540  CC                              int3
009F7541  4C 01 6B 18                     add qword ptr [rbx + 0x18], r13
009F7545  EB D3                           jmp 0x1409f751a
009F7547  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
009F754B  E9 D2 FC FF FF                  jmp 0x1409f7222
009F7550  33 D2                           xor edx, edx
009F7552  48 8B CE                        mov rcx, rsi
009F7555  E8 16 B3 18 00                  call 0x140b82870
009F755A  EB D0                           jmp 0x1409f752c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProcessCrcList(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mA8;

    if (a3 == 0) goto loc_009F753F;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    *(unsigned int *)(v_rsp - 95 + 119) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)));
    *(unsigned __int64 *)(v_rsp - 95 - 41) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_rsp - 95 - 25) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    result = qsort(a2, a3, 40, v_rip - 320186);
    *(unsigned __int64 *)(v_rsp - 95 - 17) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r12 = 0;
    result = (a3 - 1 + a3 - 1 * 4 * 8) + (a2);
    *(unsigned __int64 *)(v_rsp - 95 - 49) = 0;
    a2 = 0;
    if (0 > result) goto loc_009F7148;
loc_009F7052:
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_009F7062;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 4)) != 0) goto loc_009F7145;
loc_009F7062:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (1)) != 0) goto loc_009F7145;
    v_r14 = (*(unsigned __int64 *)(a2 + 8 + 8) + *(unsigned __int64 *)(a2 + 8 + 8) * 2) << (4);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(a2 + 8 + 8));
    v_rbx = (*(unsigned __int64 *)(v_r14 + 16)) >> (5);
    v_r15 = (*(unsigned __int64 *)(v_r14 + 8)) | (*(unsigned __int64 *)(a2 + 8 + 8));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (31));
    result = MiValidCombineProtection((unsigned int)((unsigned int)(v_r12)), a2, 40, v_rip - 320186);
    if ((unsigned int)(result) == 0) goto loc_009F7189;
    if (v_r15 < 40) goto loc_009F7189;
    if (v_r15 > 40) goto loc_009F7189;
    if ((a2 + 8 - 8) == result) goto loc_009F70EE;
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(a2 + 8 + 40))) goto loc_009F719C;
loc_009F70EE:
    if ((a2 + 8 - 8) != 0) goto loc_009F7193;
loc_009F70F7:
    a4 = 0;
    result = MiLocateCombineBlock(*(unsigned __int64 *)(v_rsp - 95 - 41), *(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)(v_r12)), a4);
    if (result != 0) goto loc_009F72E1;
loc_009F7129:
    v_rsi = (a2 + 8) + (40);
    if ((v_rsi - 8) <= result) goto loc_009F7052;
loc_009F7145:
loc_009F7148:
    v_rsi = 0;
    v_r13 = (a2) | (-1);
    if (*(unsigned __int64 *)(v_rsp - 95 - 49) == 0) goto loc_009F748B;
    result = MiAllocatePool(256, *(unsigned __int64 *)(v_rsp - 95 - 49) * 8, (unsigned int)(0x6D56694DULL), a4);
    if (result == 0) goto loc_009F748B;
    a3 = 0;
    a1 = 0;
    goto loc_009F733E;
loc_009F7189:
    goto loc_009F7129;
loc_009F7193:
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(v_rsp - 95 - 49) * 8)) goto loc_009F70F7;
loc_009F719C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 25) + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) == 192) goto loc_009F732E;
loc_009F71B3:
    v_stack_mA8 = v_rsp - 95 - 9;
    result = MiCapturePfnVm(*(unsigned __int64 *)(v_rsp - 95 + 103), *(unsigned __int64 *)(v_rsp - 95 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)), *(unsigned __int64 *)(result));
    if (result == 0) goto loc_009F7307;
    if ((*(unsigned __int64 *)(v_rsp - 95 - 1)) != v_r15) goto loc_009F7307;
    if ((*(unsigned int *)(v_rsp - 95 + 7)) != ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 49)))) goto loc_009F7307;
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))));
    v_rbx = (unsigned int)((v_rbx) & (31));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))));
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_rsp - 95 + 15);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFDFULL));
    *(unsigned int *)(result + 24) = (unsigned int)(v_rbx);
    goto loc_009F7222;
loc_009F7213:
    if (result > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 32))) goto loc_009F7547;
    if (result >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 32))) goto loc_009F7227;
loc_009F7222:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) != 0) goto loc_009F7213;
loc_009F7227:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) != 0) goto loc_009F72EC;
    result = MiAllocatePool(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) + 64, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) + 56, (unsigned int)(0x6D56694DULL), *(unsigned __int64 *)(result));
    if (result == 0) goto loc_009F7307;
    a3 = 0;
    *(unsigned __int64 *)(result + 32) = result;
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(v_rsp - 95 - 9);
    if (*(unsigned __int64 *)(v_rsp - 95 - 57) == 0) goto loc_009F7287;
loc_009F7265:
    if (result >= (*(unsigned __int64 *)(v_rsp - 95 - 57) + 32)) goto loc_009F727B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) == 0) goto loc_009F7287;
loc_009F7276:
    goto loc_009F7265;
loc_009F727B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)) + 8) != 0) goto loc_009F7276;
loc_009F7287:
    result = RtlAvlInsertNodeEx(v_rsp - 95 - 57, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57)), 1, result);
loc_009F7293:
    *(unsigned __int64 *)(result - 8) = *(unsigned __int64 *)(result + 48);
    v_r12 = (*(unsigned __int64 *)(v_rsp - 95 - 49)) + 1;
    *(unsigned __int64 *)(result + 48) = result - 8;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = v_r12;
    v_r15 = (v_r15) << (25);
    result = (1) << (25);
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) >> (16);
    *(unsigned __int64 *)(result + 8) = v_r15;
    if (1 == 2) goto loc_009F7301;
loc_009F72D8:
    goto loc_009F7129;
loc_009F72E1:
    goto loc_009F71B3;
loc_009F72EC:
    if (*(unsigned __int64 *)(v_rsp - 95 - 9) == 0) goto loc_009F7293;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_rsp - 95 - 9), (unsigned int)(0x62436D4DULL), 1, result);
    goto loc_009F7293;
loc_009F7301:
    goto loc_009F72D8;
loc_009F7307:
    if (*(unsigned __int64 *)(v_rsp - 95 - 9) != 0) {
        a2 = 0x62436D4DULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_rsp - 95 - 9), a2, 1, result);
    }
    goto loc_009F72D8;
loc_009F732E:
    goto loc_009F72D8;
loc_009F7338:
loc_009F733E:
    if (*(unsigned __int64 *)(result) != 0) goto loc_009F7338;
    goto loc_009F7357;
loc_009F7345:
    if ((*(unsigned __int64 *)(result)) == a2) goto loc_009F7357;
loc_009F734D:
    a1 = (*(unsigned __int64 *)(result + 16)) & (-4);
    if (condition_is_not_equal) goto loc_009F7345;
loc_009F7357:
    if (a1 == 0) goto loc_009F739F;
loc_009F7360:
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_009F7378;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 8)) != 0) {
        *(unsigned __int64 *)(result + 1 * 8) = *(unsigned __int64 *)(a1 + 48);
    }
    a3 = (1) + 1;
    goto loc_009F7360;
loc_009F7378:
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_009F734D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) == 0) goto loc_009F7357;
loc_009F738F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != 0) goto loc_009F738F;
    goto loc_009F7357;
loc_009F739F:
    result = qsort(result, *(unsigned __int64 *)(v_rsp - 95 - 49), 8, v_rip - 6154806);
    v_r15 = 0;
    if (*(unsigned __int64 *)(v_rsp - 95 - 49) == 0) goto loc_009F748B;
loc_009F73CB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8 - 8) + 32)))) & (32)) != 0) goto loc_009F7429;
    if (0 == 0) goto loc_009F7408;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 16) + 16)) == 2) goto loc_009F7408;
    result = MiCompareActiveCrcEntries(*(unsigned __int64 *)(result + 8 - 8), *(unsigned __int64 *)(result + 8 - 16), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8 - 8) + 32)), v_rip - 6154806);
    if ((unsigned int)(result) != 0) goto loc_009F7408;
loc_009F73F4:
    v_r15 = (v_r15) + 1;
    v_r14 = (result + 8) + (8);
    if (v_r15 < (*(unsigned __int64 *)(v_rsp - 95 - 49))) goto loc_009F73CB;
    goto loc_009F748B;
loc_009F7408:
    if (v_r15 == (*(unsigned __int64 *)(v_rsp - 95 - 49) - 1)) goto loc_009F744A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14) + 16)) == 2) goto loc_009F744A;
    result = MiCompareActiveCrcEntries(*(unsigned __int64 *)(result + 8 - 8), *(unsigned __int64 *)(v_r14), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8 - 8) + 32)), v_rip - 6154806);
    if ((unsigned int)(result) == 0) goto loc_009F73F4;
    goto loc_009F744A;
loc_009F7429:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8 - 8) + 32))) & (31));
    v_stack_mA8 = *(unsigned __int64 *)(result + 8 - 8) + 24;
    a4 = 0;
    result = MiLocateCombineBlock((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127)), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 8), a3, a4);
    if (result != 0) goto loc_009F73F4;
loc_009F744A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 16) = 2;
    goto loc_009F73F4;
loc_009F7450:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 24)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 95 + 103);
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127)));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 32);
        a2 = *(unsigned __int64 *)(result + 8 - 8);
        *(unsigned __int64 *)(a1 + 112) = result;
        result = MiSharePages(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 40) != 0) {
        a2 = 0x62436D4DULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8 - 8) + 40), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 8 - 8), a2, a3, a4);
loc_009F748B:
    if ((*(unsigned __int64 *)(v_rsp - 95 - 57)) == 0) goto loc_009F7527;
    result = RtlAvlRemoveNode(v_rsp - 95 - 57, *(unsigned __int64 *)(v_rsp - 95 - 57), a3, a4);
    if (result == 0) goto loc_009F746E;
    v_r14 = 0;
loc_009F74B2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48) == 0) goto loc_009F74CF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48) + 16)) == 2) goto loc_009F74C9;
    *(unsigned __int64 *)(result + v_r14 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48);
    v_r14 = (v_r14) + 1;
loc_009F74C4:
    goto loc_009F74B2;
loc_009F74C9:
    goto loc_009F74C4;
loc_009F74CF:
    result = qsort(result, v_r14, 8, v_rip - 5892598);
    a2 = 0;
    if (v_r14 == 0) goto loc_009F7450;
loc_009F74F7:
    if (0 == 0) goto loc_009F750F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + a2 * 8) + 16)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a2 * 8 - 8) + 16))) goto loc_009F7541;
loc_009F750F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + a2 * 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48) = *(unsigned __int64 *)(result + a2 * 8);
loc_009F751A:
    a2 = (a2) + 1;
    if (a2 < v_r14) goto loc_009F74F7;
    goto loc_009F7450;
loc_009F7527:
    if (result != 0) goto loc_009F7550;
loc_009F752C:
    v_rsp = (v_rsp) + (136);
loc_009F753F:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 57) + 48);
loc_009F7541:
    goto loc_009F751A;
loc_009F7547:
    goto loc_009F7222;
loc_009F7550:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(result + a2 * 8), v_rip - 5892598);
    goto loc_009F752C;
}
```

## 5. (Beta) C Style

```c
int64_t MiProcessCrcList(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mA8;

    if (Arg3 == 0) goto loc_009F753F;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    *(uint32_t *)(local_rsp - 0x5F + 0x77) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)));
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    result = qsort(Arg2, Arg3, 40, v_rip - 320186);
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r12 = 0;
    result = (Arg3 - 1 + Arg3 - 1 * 4 * 8) + (Arg2);
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = 0;
    Arg2 = 0;
    if (0 > result) goto loc_009F7148;
loc_009F7052:
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_009F7062;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4)) != 0) goto loc_009F7145;
loc_009F7062:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (1)) != 0) goto loc_009F7145;
    local_r14 = (*(uint64_t *)(Arg2 + 0x8 + 0x8) + *(uint64_t *)(Arg2 + 0x8 + 0x8) * 2) << (4);
    local_r14 = (local_r14) + (*(uint64_t *)(Arg2 + 0x8 + 0x8));
    local_rbx = (*(uint64_t *)(local_r14 + 0x10)) >> (5);
    local_r15 = (*(uint64_t *)(local_r14 + 0x8)) | (*(uint64_t *)(Arg2 + 0x8 + 0x8));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (31));
    result = MiValidCombineProtection((uint32_t)((uint32_t)(local_r12)), Arg2, 40, v_rip - 320186);
    if ((uint32_t)(result) == 0) goto loc_009F7189;
    if (local_r15 < 40) goto loc_009F7189;
    if (local_r15 > 40) goto loc_009F7189;
    if ((Arg2 + 8 - 8) == result) goto loc_009F70EE;
    if ((*(uint64_t *)(Arg2 + 0x8)) == (*(uint64_t *)(Arg2 + 0x8 + 0x28))) goto loc_009F719C;
loc_009F70EE:
    if ((Arg2 + 8 - 8) != 0) goto loc_009F7193;
loc_009F70F7:
    Arg4 = 0;
    result = MiLocateCombineBlock(*(uint64_t *)(local_rsp - 0x5F - 0x29), *(uint64_t *)(Arg2 + 0x8), (uint32_t)((uint32_t)(local_r12)), Arg4);
    if (result != 0) goto loc_009F72E1;
loc_009F7129:
    local_rsi = (Arg2 + 8) + (40);
    if ((local_rsi - 8) <= result) goto loc_009F7052;
loc_009F7145:
loc_009F7148:
    local_rsi = 0;
    local_r13 = (Arg2) | (-1);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x31) == 0) goto loc_009F748B;
    result = MiAllocatePool(256, *(uint64_t *)(local_rsp - 0x5F - 0x31) * 8, (uint32_t)(0x6D56694DULL), Arg4);
    if (result == 0) goto loc_009F748B;
    Arg3 = 0;
    Arg1 = 0;
    goto loc_009F733E;
loc_009F7189:
    goto loc_009F7129;
loc_009F7193:
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(local_rsp - 0x5F - 0x31) * 8)) goto loc_009F70F7;
loc_009F719C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19) + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) == 192) goto loc_009F732E;
loc_009F71B3:
    v_stack_mA8 = local_rsp - 95 - 9;
    result = MiCapturePfnVm(*(uint64_t *)(local_rsp - 0x5F + 0x67), *(uint64_t *)(local_rsp - 0x5F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)), *(uint64_t *)(result));
    if (result == 0) goto loc_009F7307;
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x1)) != local_r15) goto loc_009F7307;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x7)) != ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x31)))) goto loc_009F7307;
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))));
    local_rbx = (uint32_t)((local_rbx) & (31));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))));
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(local_rsp - 0x5F + 0xF);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFDFULL));
    *(uint32_t *)(result + 0x18) = (uint32_t)(local_rbx);
    goto loc_009F7222;
loc_009F7213:
    if (result > (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x20))) goto loc_009F7547;
    if (result >= (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x20))) goto loc_009F7227;
loc_009F7222:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) != 0) goto loc_009F7213;
loc_009F7227:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) != 0) goto loc_009F72EC;
    result = MiAllocatePool(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) + 64, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) + 56, (uint32_t)(0x6D56694DULL), *(uint64_t *)(result));
    if (result == 0) goto loc_009F7307;
    Arg3 = 0;
    *(uint64_t *)(result + 0x20) = result;
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(local_rsp - 0x5F - 0x9);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x39) == 0) goto loc_009F7287;
loc_009F7265:
    if (result >= (*(uint64_t *)(local_rsp - 0x5F - 0x39) + 32)) goto loc_009F727B;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) == 0) goto loc_009F7287;
loc_009F7276:
    goto loc_009F7265;
loc_009F727B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)) + 0x8) != 0) goto loc_009F7276;
loc_009F7287:
    result = RtlAvlInsertNodeEx(local_rsp - 95 - 57, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39)), 1, result);
loc_009F7293:
    *(uint64_t *)(result - 0x8) = *(uint64_t *)(result + 0x30);
    local_r12 = (*(uint64_t *)(local_rsp - 0x5F - 0x31)) + 1;
    *(uint64_t *)(result + 0x30) = result - 8;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = local_r12;
    local_r15 = (local_r15) << (25);
    result = (1) << (25);
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) >> (16);
    *(uint64_t *)(result + 0x8) = local_r15;
    if (1 == 2) goto loc_009F7301;
loc_009F72D8:
    goto loc_009F7129;
loc_009F72E1:
    goto loc_009F71B3;
loc_009F72EC:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x9) == 0) goto loc_009F7293;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x9), (uint32_t)(0x62436D4DULL), 1, result);
    goto loc_009F7293;
loc_009F7301:
    goto loc_009F72D8;
loc_009F7307:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x9) != 0) {
        Arg2 = 0x62436D4DULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x9), Arg2, 1, result);
    }
    goto loc_009F72D8;
loc_009F732E:
    goto loc_009F72D8;
loc_009F7338:
loc_009F733E:
    if (*(uint64_t *)(result) != 0) goto loc_009F7338;
    goto loc_009F7357;
loc_009F7345:
    if ((*(uint64_t *)(result)) == Arg2) goto loc_009F7357;
loc_009F734D:
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_009F7345;
loc_009F7357:
    if (Arg1 == NULL) goto loc_009F739F;
loc_009F7360:
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_009F7378;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x8)) != 0) {
        *(uint64_t *)(result + 0x1 * 8) = *(uint64_t *)(arg1 + 0x30);
    }
    Arg3 = (1) + 1;
    goto loc_009F7360;
loc_009F7378:
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_009F734D;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) == 0) goto loc_009F7357;
loc_009F738F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != 0) goto loc_009F738F;
    goto loc_009F7357;
loc_009F739F:
    result = qsort(result, *(uint64_t *)(local_rsp - 0x5F - 0x31), 8, v_rip - 6154806);
    local_r15 = 0;
    if (*(uint64_t *)(local_rsp - 0x5F - 0x31) == 0) goto loc_009F748B;
loc_009F73CB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x20)))) & (32)) != 0) goto loc_009F7429;
    if (0 == 0) goto loc_009F7408;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x10) + 0x10)) == 2) goto loc_009F7408;
    result = MiCompareActiveCrcEntries(*(uint64_t *)(result + 0x8 - 0x8), *(uint64_t *)(result + 0x8 - 0x10), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x20)), v_rip - 6154806);
    if ((uint32_t)(result) != 0) goto loc_009F7408;
loc_009F73F4:
    local_r15 = (local_r15) + 1;
    local_r14 = (result + 8) + (8);
    if (local_r15 < (*(uint64_t *)(local_rsp - 0x5F - 0x31))) goto loc_009F73CB;
    goto loc_009F748B;
loc_009F7408:
    if (local_r15 == (*(uint64_t *)(local_rsp - 0x5F - 0x31) - 1)) goto loc_009F744A;
    if ((*(uint64_t *)(*(uint64_t *)(local_r14) + 0x10)) == 2) goto loc_009F744A;
    result = MiCompareActiveCrcEntries(*(uint64_t *)(result + 0x8 - 0x8), *(uint64_t *)(local_r14), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x20)), v_rip - 6154806);
    if ((uint32_t)(result) == 0) goto loc_009F73F4;
    goto loc_009F744A;
loc_009F7429:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x20))) & (31));
    v_stack_mA8 = *(uint64_t *)(result + 0x8 - 0x8) + 24;
    Arg4 = 0;
    result = MiLocateCombineBlock((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F)), *(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x8), Arg3, Arg4);
    if (result != 0) goto loc_009F73F4;
loc_009F744A:
    *(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x10) = 2;
    goto loc_009F73F4;
loc_009F7450:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x18)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x5F + 0x67);
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F)));
        result = *(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x20);
        Arg2 = *(uint64_t *)(result + 0x8 - 0x8);
        *(uint64_t *)(arg1 + 0x70) = result;
        result = MiSharePages(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x28) != 0) {
        Arg2 = 0x62436D4DULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(result + 0x8 - 0x8) + 0x28), Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x8 - 0x8), Arg2, Arg3, Arg4);
loc_009F748B:
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x39)) == 0) goto loc_009F7527;
    result = RtlAvlRemoveNode(local_rsp - 95 - 57, *(uint64_t *)(local_rsp - 0x5F - 0x39), Arg3, Arg4);
    if (result == 0) goto loc_009F746E;
    local_r14 = 0;
loc_009F74B2:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30) == 0) goto loc_009F74CF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30) + 0x10)) == 2) goto loc_009F74C9;
    *(uint64_t *)(result + local_r14 * 8) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30);
    local_r14 = (local_r14) + 1;
loc_009F74C4:
    goto loc_009F74B2;
loc_009F74C9:
    goto loc_009F74C4;
loc_009F74CF:
    result = qsort(result, local_r14, 8, v_rip - 5892598);
    Arg2 = 0;
    if (local_r14 == 0) goto loc_009F7450;
loc_009F74F7:
    if (0 == 0) goto loc_009F750F;
    if ((*(uint64_t *)(*(uint64_t *)(result + Arg2 * 8) + 0x10)) == (*(uint64_t *)(*(uint64_t *)(result + Arg2 * 8 - 0x8) + 0x10))) goto loc_009F7541;
loc_009F750F:
    *(uint64_t *)(*(uint64_t *)(result + Arg2 * 8)) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30) = *(uint64_t *)(result + Arg2 * 8);
loc_009F751A:
    Arg2 = (Arg2) + 1;
    if (Arg2 < local_r14) goto loc_009F74F7;
    goto loc_009F7450;
loc_009F7527:
    if (result != 0) goto loc_009F7550;
loc_009F752C:
    local_rsp = (local_rsp) + (136);
loc_009F753F:
    return *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x39) + 0x30);
loc_009F7541:
    goto loc_009F751A;
loc_009F7547:
    goto loc_009F7222;
loc_009F7550:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(result + Arg2 * 8), v_rip - 5892598);
    goto loc_009F752C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F6F94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
