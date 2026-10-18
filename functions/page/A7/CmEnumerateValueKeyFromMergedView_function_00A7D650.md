# CmEnumerateValueKeyFromMergedView

- RVA: `0x00A7D650`–`0x00A7DAB9` (길이 `1,129` bytes)
- VA: `0x0000000140A7D650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B6AF8`
- 디코드: `283`개 명령, `1,129/1,129` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7D6F4` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x00A7D708` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00A7D751` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00A7D764` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00A7D798` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A7D80A` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A7D85F` → [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00A7D8A3` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A7D8C2` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A7D8D8` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A7D8FE` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A7D91B` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A7D922` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A7D92C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A7D97D` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x00A7D987` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00A7D9A0` → [CmpLockTwoKcbsShared](../84/CmpLockTwoKcbsShared_function_008485B4.md) (function, `0x008485B4`)
- `0x00A7DA00` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A7DA55` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A7DA73` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A7DA91` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A7DAAF` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmQueryKey](../85/CmQueryKey_function_00858240.md) at `0x0085893A`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B460D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00A7D708` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00A7D751` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00A7D764` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x00A7D987` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x00A7D792` → [sub_00B428B8 + 0x20](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7D79E` → [sub_00B428B8 + 0x25](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7D9CE` → [sub_00B428B8](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7D9DF` → [sub_00B428B8 + 0x3](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7D9FA` → [sub_00B428B8 + 0x45](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA06` → [sub_00B428B8 + 0x4A](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA0F` → [sub_00B428B8 + 0xDB](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA1F` → [sub_00B428B8 + 0x6E](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA4F` → [sub_00B428B8 + 0x136](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA6D` → [sub_00B428B8 + 0x141](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DA8B` → [sub_00B428B8 + 0x14C](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)
  - `0x00A7DAA9` → [sub_00B428B8 + 0x157](../B4/Unknown_function_00B428B8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A7D650  48 8B C4                        mov rax, rsp
00A7D653  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00A7D657  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00A7D65B  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
00A7D65F  55                              push rbp
00A7D660  56                              push rsi
00A7D661  57                              push rdi
00A7D662  41 54                           push r12
00A7D664  41 55                           push r13
00A7D666  41 56                           push r14
00A7D668  41 57                           push r15
00A7D66A  48 8D 68 C1                     lea rbp, [rax - 0x3f]
00A7D66E  48 81 EC D0 00 00 00            sub rsp, 0xd0
00A7D675  45 33 ED                        xor r13d, r13d
00A7D678  48 8B F9                        mov rdi, rcx
00A7D67B  83 C9 FF                        or ecx, 0xffffffff
00A7D67E  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
00A7D682  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
00A7D686  0F 57 C0                        xorps xmm0, xmm0
00A7D689  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
00A7D68C  45 8A F8                        mov r15b, r8b
00A7D68F  44 89 6D B3                     mov dword ptr [rbp - 0x4d], r13d
00A7D693  4C 8B F2                        mov r14, rdx
00A7D696  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
00A7D69A  41 8B F5                        mov esi, r13d
00A7D69D  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
00A7D6A0  41 8B DD                        mov ebx, r13d
00A7D6A3  44 89 6D BB                     mov dword ptr [rbp - 0x45], r13d
00A7D6A7  45 8B E5                        mov r12d, r13d
00A7D6AA  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
00A7D6AE  4C 89 6D C7                     mov qword ptr [rbp - 0x39], r13
00A7D6B2  44 89 6D 97                     mov dword ptr [rbp - 0x69], r13d
00A7D6B6  44 89 6D 47                     mov dword ptr [rbp + 0x47], r13d
00A7D6BA  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00A7D6BF  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
00A7D6C2  44 89 6D 8B                     mov dword ptr [rbp - 0x75], r13d
00A7D6C6  89 4D A7                        mov dword ptr [rbp - 0x59], ecx
00A7D6C9  44 89 6D AB                     mov dword ptr [rbp - 0x55], r13d
00A7D6CD  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A7D6D1  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
00A7D6D6  44 89 6D BF                     mov dword ptr [rbp - 0x41], r13d
00A7D6DA  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00A7D6DE  45 84 C0                        test r8b, r8b
00A7D6E1  0F 84 A0 02 00 00               je 0x140a7d987
00A7D6E7  4C 39 6F 38                     cmp qword ptr [rdi + 0x38], r13
00A7D6EB  74 3E                           je 0x140a7d72b
00A7D6ED  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00A7D6F1  48 8B CF                        mov rcx, rdi
00A7D6F4  E8 BF 5F DF FF                  call 0x1408736b8
00A7D6F9  8B D8                           mov ebx, eax
00A7D6FB  85 C0                           test eax, eax
00A7D6FD  0F 89 8E 02 00 00               jns 0x140a7d991
00A7D703  45 84 FF                        test r15b, r15b
00A7D706  75 05                           jne 0x140a7d70d
00A7D708  E8 77 C3 14 00                  call 0x140bc9a84
00A7D70D  8B C3                           mov eax, ebx
00A7D70F  48 8B 9C 24 18 01 00 00         mov rbx, qword ptr [rsp + 0x118]
00A7D717  48 81 C4 D0 00 00 00            add rsp, 0xd0
00A7D71E  41 5F                           pop r15
00A7D720  41 5E                           pop r14
00A7D722  41 5D                           pop r13
00A7D724  41 5C                           pop r12
00A7D726  5F                              pop rdi
00A7D727  5E                              pop rsi
00A7D728  5D                              pop rbp
00A7D729  C3                              ret
00A7D72A  CC                              int3
00A7D72B  4C 39 6F 40                     cmp qword ptr [rdi + 0x40], r13
00A7D72F  75 BC                           jne 0x140a7d6ed
00A7D731  4C 8B 6F 08                     mov r13, qword ptr [rdi + 8]
00A7D735  4D 8B 7E 08                     mov r15, qword ptr [r14 + 8]
00A7D739  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
00A7D73D  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
00A7D741  44 38 65 57                     cmp byte ptr [rbp + 0x57], r12b
00A7D745  0F 84 4F 02 00 00               je 0x140a7d99a
00A7D74B  48 8B D6                        mov rdx, rsi
00A7D74E  48 8B CF                        mov rcx, rdi
00A7D751  E8 2A BD 14 00                  call 0x140bc9480
00A7D756  84 C0                           test al, al
00A7D758  0F 85 4C 02 00 00               jne 0x140a7d9aa
00A7D75E  48 8B D6                        mov rdx, rsi
00A7D761  49 8B CE                        mov rcx, r14
00A7D764  E8 17 BD 14 00                  call 0x140bc9480
00A7D769  84 C0                           test al, al
00A7D76B  0F 85 3E 02 00 00               jne 0x140a7d9af
00A7D771  BF 01 00 00 00                  mov edi, 1
00A7D776  48 85 F6                        test rsi, rsi
00A7D779  0F 85 48 02 00 00               jne 0x140a7d9c7
00A7D77F  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A7D783  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00A7D787  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00A7D78B  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7D792  0F 84 40 51 0C 00               je 0x140b428d8
00A7D798  E8 C3 74 DD FF                  call 0x140854c60
00A7D79D  90                              nop
00A7D79E  E9 3A 51 0C 00                  jmp 0x140b428dd
00A7D7A3  48 85 C9                        test rcx, rcx
00A7D7A6  74 D7                           je 0x140a7d77f
00A7D7A8  4C 39 65 C7                     cmp qword ptr [rbp - 0x39], r12
00A7D7AC  0F 84 32 02 00 00               je 0x140a7d9e4
00A7D7B2  4C 8B 75 9F                     mov r14, qword ptr [rbp - 0x61]
00A7D7B6  49 8D 75 20                     lea rsi, [r13 + 0x20]
00A7D7BA  45 33 FF                        xor r15d, r15d
00A7D7BD  45 8B EC                        mov r13d, r12d
00A7D7C0  49 83 C6 20                     add r14, 0x20
00A7D7C4  8B 4D 47                        mov ecx, dword ptr [rbp + 0x47]
00A7D7C7  3B 4D 5F                        cmp ecx, dword ptr [rbp + 0x5f]
00A7D7CA  0F 87 6D 01 00 00               ja 0x140a7d93d
00A7D7D0  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00A7D7D4  44 3B 28                        cmp r13d, dword ptr [rax]
00A7D7D7  0F 83 37 02 00 00               jae 0x140a7da14
00A7D7DD  4D 85 E4                        test r12, r12
00A7D7E0  0F 84 05 01 00 00               je 0x140a7d8eb
00A7D7E6  41 8B C5                        mov eax, r13d
00A7D7E9  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00A7D7EE  4C 8B 2E                        mov r13, qword ptr [rsi]
00A7D7F1  41 8B 0C 84                     mov ecx, dword ptr [r12 + rax*4]
00A7D7F5  8B D1                           mov edx, ecx
00A7D7F7  89 4D C3                        mov dword ptr [rbp - 0x3d], ecx
00A7D7FA  49 8B CD                        mov rcx, r13
00A7D7FD  41 84 BD 8C 00 00 00            test byte ptr [r13 + 0x8c], dil
00A7D804  0F 84 CE 00 00 00               je 0x140a7d8d8
00A7D80A  E8 51 74 DD FF                  call 0x140854c60
00A7D80F  4C 8B E0                        mov r12, rax
00A7D812  48 85 C0                        test rax, rax
00A7D815  0F 84 18 01 00 00               je 0x140a7d933
00A7D81B  45 0F B7 4C 24 10               movzx r9d, word ptr [r12 + 0x10]
00A7D821  48 8D 40 14                     lea rax, [rax + 0x14]
00A7D825  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
00A7D829  4C 8D 45 EF                     lea r8, [rbp - 0x11]
00A7D82D  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00A7D831  44 23 CF                        and r9d, edi
00A7D834  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
00A7D83A  66 89 45 EF                     mov word ptr [rbp - 0x11], ax
00A7D83E  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00A7D842  48 83 C0 20                     add rax, 0x20
00A7D846  41 C1 E1 10                     shl r9d, 0x10
00A7D84A  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00A7D84E  48 8B 08                        mov rcx, qword ptr [rax]
00A7D851  48 8D 45 BF                     lea rax, [rbp - 0x41]
00A7D855  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A7D85A  4C 21 7C 24 20                  and qword ptr [rsp + 0x20], r15
00A7D85F  E8 1C 93 DC FF                  call 0x140846b80
00A7D864  BA 00 00 00 80                  mov edx, 0x80000000
00A7D869  8D 0C 10                        lea ecx, [rax + rdx]
00A7D86C  85 CA                           test edx, ecx
00A7D86E  74 72                           je 0x140a7d8e2
00A7D870  83 7D BF FF                     cmp dword ptr [rbp - 0x41], -1
00A7D874  75 11                           jne 0x140a7d887
00A7D876  8B 45 47                        mov eax, dword ptr [rbp + 0x47]
00A7D879  3B 45 5F                        cmp eax, dword ptr [rbp + 0x5f]
00A7D87C  0F 84 89 01 00 00               je 0x140a7da0b
00A7D882  03 C7                           add eax, edi
00A7D884  89 45 47                        mov dword ptr [rbp + 0x47], eax
00A7D887  44 8B 6D 97                     mov r13d, dword ptr [rbp - 0x69]
00A7D88B  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00A7D890  48 8B 0E                        mov rcx, qword ptr [rsi]
00A7D893  44 03 EF                        add r13d, edi
00A7D896  44 89 6D 97                     mov dword ptr [rbp - 0x69], r13d
00A7D89A  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7D8A1  75 7F                           jne 0x140a7d922
00A7D8A3  E8 98 86 DD FF                  call 0x140855f40
00A7D8A8  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00A7D8AD  4D 85 E4                        test r12, r12
00A7D8B0  74 1D                           je 0x140a7d8cf
00A7D8B2  48 8B 0E                        mov rcx, qword ptr [rsi]
00A7D8B5  48 8D 55 87                     lea rdx, [rbp - 0x79]
00A7D8B9  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7D8C0  75 6A                           jne 0x140a7d92c
00A7D8C2  E8 79 86 DD FF                  call 0x140855f40
00A7D8C7  45 33 E4                        xor r12d, r12d
00A7D8CA  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00A7D8CF  4C 8B 75 E7                     mov r14, qword ptr [rbp - 0x19]
00A7D8D3  E9 EC FE FF FF                  jmp 0x140a7d7c4
00A7D8D8  E8 D3 73 DD FF                  call 0x140854cb0
00A7D8DD  E9 2D FF FF FF                  jmp 0x140a7d80f
00A7D8E2  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A7D8E7  74 87                           je 0x140a7d870
00A7D8E9  EB 9C                           jmp 0x140a7d887
00A7D8EB  48 8B 0E                        mov rcx, qword ptr [rsi]
00A7D8EE  4C 8D 45 87                     lea r8, [rbp - 0x79]
00A7D8F2  8B 50 04                        mov edx, dword ptr [rax + 4]
00A7D8F5  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7D8FC  74 1D                           je 0x140a7d91b
00A7D8FE  E8 5D 73 DD FF                  call 0x140854c60
00A7D903  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A7D908  4C 8B E0                        mov r12, rax
00A7D90B  48 85 C0                        test rax, rax
00A7D90E  0F 85 D2 FE FF FF               jne 0x140a7d7e6
00A7D914  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A7D919  EB 34                           jmp 0x140a7d94f
00A7D91B  E8 90 73 DD FF                  call 0x140854cb0
00A7D920  EB E1                           jmp 0x140a7d903
00A7D922  E8 F9 F2 DD FF                  call 0x14085cc20
00A7D927  E9 7C FF FF FF                  jmp 0x140a7d8a8
00A7D92C  E8 EF F2 DD FF                  call 0x14085cc20
00A7D931  EB 94                           jmp 0x140a7d8c7
00A7D933  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A7D938  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00A7D93D  4D 85 E4                        test r12, r12
00A7D940  0F 85 FB 00 00 00               jne 0x140a7da41
00A7D946  4D 85 FF                        test r15, r15
00A7D949  0F 85 10 01 00 00               jne 0x140a7da5f
00A7D94F  4C 8B 7D 9F                     mov r15, qword ptr [rbp - 0x61]
00A7D953  4C 8B 6D 8F                     mov r13, qword ptr [rbp - 0x71]
00A7D957  48 83 7D D7 00                  cmp qword ptr [rbp - 0x29], 0
00A7D95C  0F 85 1B 01 00 00               jne 0x140a7da7d
00A7D962  48 83 7D DF 00                  cmp qword ptr [rbp - 0x21], 0
00A7D967  0F 85 2E 01 00 00               jne 0x140a7da9b
00A7D96D  80 7D 57 00                     cmp byte ptr [rbp + 0x57], 0
00A7D971  0F 85 96 FD FF FF               jne 0x140a7d70d
00A7D977  49 8B D7                        mov rdx, r15
00A7D97A  49 8B CD                        mov rcx, r13
00A7D97D  E8 1A AD DC FF                  call 0x14084869c
00A7D982  E9 81 FD FF FF                  jmp 0x140a7d708
00A7D987  E8 A8 C1 14 00                  call 0x140bc9b34
00A7D98C  E9 56 FD FF FF                  jmp 0x140a7d6e7
00A7D991  48 8B 75 8F                     mov rsi, qword ptr [rbp - 0x71]
00A7D995  E9 97 FD FF FF                  jmp 0x140a7d731
00A7D99A  49 8B D7                        mov rdx, r15
00A7D99D  49 8B CD                        mov rcx, r13
00A7D9A0  E8 0F AC DC FF                  call 0x1408485b4
00A7D9A5  E9 A1 FD FF FF                  jmp 0x140a7d74b
00A7D9AA  8A 47 30                        mov al, byte ptr [rdi + 0x30]
00A7D9AD  EB 04                           jmp 0x140a7d9b3
00A7D9AF  41 8A 46 30                     mov al, byte ptr [r14 + 0x30]
00A7D9B3  24 01                           and al, 1
00A7D9B5  F6 D8                           neg al
00A7D9B7  1B DB                           sbb ebx, ebx
00A7D9B9  81 E3 A9 02 00 00               and ebx, 0x2a9
00A7D9BF  81 C3 7C 01 00 C0               add ebx, 0xc000017c
00A7D9C5  EB A6                           jmp 0x140a7d96d
00A7D9C7  49 39 B5 20 01 00 00            cmp qword ptr [r13 + 0x120], rsi
00A7D9CE  0F 85 E4 4E 0C 00               jne 0x140b428b8
00A7D9D4  49 8D 8D 18 01 00 00            lea rcx, [r13 + 0x118]
00A7D9DB  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00A7D9DF  E9 D7 4E 0C 00                  jmp 0x140b428bb
00A7D9E4  41 8B 57 28                     mov edx, dword ptr [r15 + 0x28]
00A7D9E8  4D 8D 77 20                     lea r14, [r15 + 0x20]
00A7D9EC  49 8B 0E                        mov rcx, qword ptr [r14]
00A7D9EF  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00A7D9F3  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7D9FA  0F 84 FD 4E 0C 00               je 0x140b428fd
00A7DA00  E8 5B 72 DD FF                  call 0x140854c60
00A7DA05  90                              nop
00A7DA06  E9 F7 4E 0C 00                  jmp 0x140b42902
00A7DA0B  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00A7DA0F  E9 7F 4F 0C 00                  jmp 0x140b42993
00A7DA14  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
00A7DA18  8B 5D 5F                        mov ebx, dword ptr [rbp + 0x5f]
00A7DA1B  03 0A                           add ecx, dword ptr [rdx]
00A7DA1D  3B CB                           cmp ecx, ebx
00A7DA1F  0F 87 01 4F 0C 00               ja 0x140b42926
00A7DA25  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00A7DA2C  BB 1A 00 00 80                  mov ebx, 0x8000001a
00A7DA31  48 85 C0                        test rax, rax
00A7DA34  0F 84 03 FF FF FF               je 0x140a7d93d
00A7DA3A  89 08                           mov dword ptr [rax], ecx
00A7DA3C  E9 FC FE FF FF                  jmp 0x140a7d93d
00A7DA41  48 8B 0E                        mov rcx, qword ptr [rsi]
00A7DA44  48 8D 55 87                     lea rdx, [rbp - 0x79]
00A7DA48  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7DA4F  0F 84 99 4F 0C 00               je 0x140b429ee
00A7DA55  E8 C6 F1 DD FF                  call 0x14085cc20
00A7DA5A  E9 E7 FE FF FF                  jmp 0x140a7d946
00A7DA5F  49 8B 0E                        mov rcx, qword ptr [r14]
00A7DA62  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00A7DA66  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7DA6D  0F 84 86 4F 0C 00               je 0x140b429f9
00A7DA73  E8 A8 F1 DD FF                  call 0x14085cc20
00A7DA78  E9 D2 FE FF FF                  jmp 0x140a7d94f
00A7DA7D  48 8B 0E                        mov rcx, qword ptr [rsi]
00A7DA80  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00A7DA84  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7DA8B  0F 84 73 4F 0C 00               je 0x140b42a04
00A7DA91  E8 8A F1 DD FF                  call 0x14085cc20
00A7DA96  E9 C7 FE FF FF                  jmp 0x140a7d962
00A7DA9B  49 8B 0E                        mov rcx, qword ptr [r14]
00A7DA9E  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00A7DAA2  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00A7DAA9  0F 84 60 4F 0C 00               je 0x140b42a0f
00A7DAAF  E8 6C F1 DD FF                  call 0x14085cc20
00A7DAB4  E9 B4 FE FF FF                  jmp 0x140a7d96d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmEnumerateValueKeyFromMergedView(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (208);
    v_r13 = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 63 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = 0;
    *(unsigned int *)(v_rsp - 63 - 81) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = 0;
    *(unsigned int *)(v_rsp - 63 - 73) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 63 - 69) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 57) = 0;
    *(unsigned int *)(v_rsp - 63 - 105) = 0;
    *(unsigned int *)(v_rsp - 63 + 71) = 0;
    v_stack_mC0 = 0;
    *(unsigned int *)(v_rsp - 63 - 121) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 63 - 117) = 0;
    *(unsigned int *)(v_rsp - 63 - 89) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 63 - 85) = 0;
    v_stack_mC8 = (unsigned int)(a1);
    v_stack_mC4 = 0;
    *(unsigned int *)(v_rsp - 63 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 17) = v_xmm0;
    if (a3 == 0) goto loc_00A7D987;
loc_00A7D6E7:
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_00A7D72B;
loc_00A7D6ED:
    result = CmpTransSearchAddTransFromKeyBody(a1, v_rsp - 63 - 113, a3, a4);
    if (!sign_flag) goto loc_00A7D991;
    if (a3 == 0) {
        result = CmpUnlockRegistry(a1, v_rsp - 63 - 113, a3, a4);
    }
    v_rsp = (v_rsp) + (208);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A7D72B:
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_00A7D6ED;
loc_00A7D731:
    *(unsigned __int64 *)(v_rsp - 63 - 113) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(v_rsp - 63 - 97) = *(unsigned __int64 *)(a2 + 8);
    if ((*(unsigned __int8 *)(v_rsp - 63 + 87)) == 0) goto loc_00A7D99A;
loc_00A7D74B:
    result = CmpIsKeyDeletedForKeyBody(a1, 0, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A7D9AA;
    result = CmpIsKeyDeletedForKeyBody(a2, 0, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A7D9AF;
    if (0 != 0) goto loc_00A7D9C7;
loc_00A7D77F:
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_rsp - 63 - 81, a4);
loc_00A7D96D:
    if ((*(unsigned __int8 *)(v_rsp - 63 + 87)) != 0) goto loc_00A7D70D;
    result = CmpUnlockTwoKcbs(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a2 + 8), v_rsp - 63 - 81, a4);
    goto loc_00A7D708;
loc_00A7D987:
    result = CmpLockRegistry(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a2 + 8), v_rsp - 63 - 81, a4);
    goto loc_00A7D6E7;
loc_00A7D991:
    goto loc_00A7D731;
loc_00A7D99A:
    result = CmpLockTwoKcbsShared(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a2 + 8), v_rsp - 63 - 81, a4);
    goto loc_00A7D74B;
loc_00A7D9AA:
    goto loc_00A7D9B3;
loc_00A7D9AF:
loc_00A7D9B3:
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 48)) & (1));
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)((v_stack_p10) & (681));
    v_rbx = (unsigned int)((v_rbx) + (0xC000017CULL));
    goto loc_00A7D96D;
loc_00A7D9C7:
    *(unsigned __int64 *)(v_rsp - 63 - 49) = *(unsigned __int64 *)(a1 + 8) + 280;
}
```

## 5. (Beta) C Style

```c
int64_t CmEnumerateValueKeyFromMergedView(void *Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (208);
    local_r13 = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x3F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x49) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x3F - 0x45) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x39) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x69) = 0;
    *(uint32_t *)(local_rsp - 0x3F + 0x47) = 0;
    v_stack_mC0 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x79) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x3F - 0x75) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x59) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x3F - 0x55) = 0;
    v_stack_mC8 = (uint32_t)(Arg1);
    v_stack_mC4 = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = v_xmm0;
    if (Arg3 == 0) goto loc_00A7D987;
loc_00A7D6E7:
    if ((*(uint64_t *)(arg1 + 0x38)) == 0) goto loc_00A7D72B;
loc_00A7D6ED:
    result = CmpTransSearchAddTransFromKeyBody(Arg1, local_rsp - 63 - 113, Arg3, Arg4);
    if (!sign_flag) goto loc_00A7D991;
    if (Arg3 == 0) {
        result = CmpUnlockRegistry(Arg1, local_rsp - 63 - 113, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (208);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A7D72B:
    if ((*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_00A7D6ED;
loc_00A7D731:
    *(uint64_t *)(local_rsp - 0x3F - 0x71) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = *(uint64_t *)(arg2 + 0x8);
    if ((*(uint8_t *)(local_rsp - 0x3F + 0x57)) == 0) goto loc_00A7D99A;
loc_00A7D74B:
    result = CmpIsKeyDeletedForKeyBody(Arg1, 0, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A7D9AA;
    result = CmpIsKeyDeletedForKeyBody(Arg2, 0, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A7D9AF;
    if (0 != 0) goto loc_00A7D9C7;
loc_00A7D77F:
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), local_rsp - 63 - 81, Arg4);
loc_00A7D96D:
    if ((*(uint8_t *)(local_rsp - 0x3F + 0x57)) != 0) goto loc_00A7D70D;
    result = CmpUnlockTwoKcbs(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg2 + 0x8), local_rsp - 63 - 81, Arg4);
    goto loc_00A7D708;
loc_00A7D987:
    result = CmpLockRegistry(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg2 + 0x8), local_rsp - 63 - 81, Arg4);
    goto loc_00A7D6E7;
loc_00A7D991:
    goto loc_00A7D731;
loc_00A7D99A:
    result = CmpLockTwoKcbsShared(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg2 + 0x8), local_rsp - 63 - 81, Arg4);
    goto loc_00A7D74B;
loc_00A7D9AA:
    goto loc_00A7D9B3;
loc_00A7D9AF:
loc_00A7D9B3:
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x30)) & (1));
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)((v_stack_p10) & (681));
    local_rbx = (uint32_t)((local_rbx) + (0xC000017CULL));
    goto loc_00A7D96D;
loc_00A7D9C7:
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = *(uint64_t *)(arg1 + 0x8) + 280;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x30` | `8` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x30` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7D650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
