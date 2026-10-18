# CmpSelectLeaf

- RVA: `0x0084BFB4`–`0x0084C305` (길이 `849` bytes)
- VA: `0x000000014084BFB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069744`
- 디코드: `216`개 명령, `849/849` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084C000` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0084C027` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C049` → [CmpFindSubKeyInRoot](../85/CmpFindSubKeyInRoot_function_0085D890.md) (function, `0x0085D890`)
- `0x0084C083` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C099` → [CmpDoCompareKeyName](../85/CmpDoCompareKeyName_function_00854E80.md) (function, `0x00854E80`)
- `0x0084C0C3` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C0E3` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C120` → [CmpSplitLeaf](../A7/CmpSplitLeaf_function_00A7C7E0.md) (function, `0x00A7C7E0`)
- `0x0084C143` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C163` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C17F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C198` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C1D2` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C1EC` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C20C` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C21D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C227` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C231` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C23B` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C24C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C253` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C25D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C267` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C271` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C28C` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0084C2AC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0084C2C5` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084C2CC` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C2DB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084C2FA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmpAddSubKeyToList](CmpAddSubKeyToList_function_0084D644.md) at `0x0084D84F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0084C2D5` → [sub_00B1686C](../B1/Unknown_function_00B1686C.md) (`tail-transfer`)
  - `0x0084C2E1` → [sub_00B1686C + 0x5](../B1/Unknown_function_00B1686C.md) (`tail-transfer`)
  - `0x0084C2F4` → [sub_00B1686C + 0xB](../B1/Unknown_function_00B1686C.md) (`tail-transfer`)
  - `0x0084C300` → [sub_00B1686C + 0x10](../B1/Unknown_function_00B1686C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0084BFB4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0084BFB9  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0084BFBE  55                              push rbp
0084BFBF  56                              push rsi
0084BFC0  57                              push rdi
0084BFC1  41 54                           push r12
0084BFC3  41 55                           push r13
0084BFC5  41 56                           push r14
0084BFC7  41 57                           push r15
0084BFC9  48 8B EC                        mov rbp, rsp
0084BFCC  48 83 EC 50                     sub rsp, 0x50
0084BFD0  45 33 F6                        xor r14d, r14d
0084BFD3  48 8B D9                        mov rbx, rcx
0084BFD6  83 C9 FF                        or ecx, 0xffffffff
0084BFD9  44 89 75 48                     mov dword ptr [rbp + 0x48], r14d
0084BFDD  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
0084BFE0  4D 8B E8                        mov r13, r8
0084BFE3  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
0084BFE6  4C 8B E2                        mov r12, rdx
0084BFE9  8B 12                           mov edx, dword ptr [rdx]
0084BFEB  48 8B CB                        mov rcx, rbx
0084BFEE  45 33 C9                        xor r9d, r9d
0084BFF1  44 89 75 E0                     mov dword ptr [rbp - 0x20], r14d
0084BFF5  45 33 C0                        xor r8d, r8d
0084BFF8  44 89 75 F4                     mov dword ptr [rbp - 0xc], r14d
0084BFFC  44 89 75 EC                     mov dword ptr [rbp - 0x14], r14d
0084C000  E8 7B C0 00 00                  call 0x140858080
0084C005  8B F8                           mov edi, eax
0084C007  85 C0                           test eax, eax
0084C009  0F 88 E2 01 00 00               js 0x14084c1f1
0084C00F  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C016  4C 8D 45 F0                     lea r8, [rbp - 0x10]
0084C01A  41 8B 14 24                     mov edx, dword ptr [r12]
0084C01E  48 8B CB                        mov rcx, rbx
0084C021  0F 84 E5 01 00 00               je 0x14084c20c
0084C027  E8 34 8C 00 00                  call 0x140854c60
0084C02C  4C 8B F0                        mov r14, rax
0084C02F  BE F5 03 00 00                  mov esi, 0x3f5
0084C034  48 8D 45 48                     lea rax, [rbp + 0x48]
0084C038  45 33 C9                        xor r9d, r9d
0084C03B  4D 8B C5                        mov r8, r13
0084C03E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084C043  49 8B D6                        mov rdx, r14
0084C046  48 8B CB                        mov rcx, rbx
0084C049  E8 42 18 01 00                  call 0x14085d890
0084C04E  44 8B F8                        mov r15d, eax
0084C051  85 C0                           test eax, eax
0084C053  0F 88 EC 01 00 00               js 0x14084c245
0084C059  8B 7D 48                        mov edi, dword ptr [rbp + 0x48]
0084C05C  4C 8D 45 E8                     lea r8, [rbp - 0x18]
0084C060  48 8B CB                        mov rcx, rbx
0084C063  83 FF FF                        cmp edi, -1
0084C066  0F 85 1D 01 00 00               jne 0x14084c189
0084C06C  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C073  49 8D 77 01                     lea rsi, [r15 + 1]
0084C077  49 8D 34 B6                     lea rsi, [r14 + rsi*4]
0084C07B  8B 16                           mov edx, dword ptr [rsi]
0084C07D  0F 84 9A 01 00 00               je 0x14084c21d
0084C083  E8 D8 8B 00 00                  call 0x140854c60
0084C088  44 8B 48 04                     mov r9d, dword ptr [rax + 4]
0084C08C  45 33 C0                        xor r8d, r8d
0084C08F  49 8B D5                        mov rdx, r13
0084C092  44 89 4D E0                     mov dword ptr [rbp - 0x20], r9d
0084C096  48 8B CB                        mov rcx, rbx
0084C099  E8 E2 8D 00 00                  call 0x140854e80
0084C09E  83 F8 02                        cmp eax, 2
0084C0A1  0F 84 6F 01 00 00               je 0x14084c216
0084C0A7  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0084C0AB  48 8B CB                        mov rcx, rbx
0084C0AE  85 C0                           test eax, eax
0084C0B0  0F 88 C5 01 00 00               js 0x14084c27b
0084C0B6  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C0BD  0F 85 9A 01 00 00               jne 0x14084c25d
0084C0C3  E8 78 9E 00 00                  call 0x140855f40
0084C0C8  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C0CF  4C 8D 45 E8                     lea r8, [rbp - 0x18]
0084C0D3  8B 3E                           mov edi, dword ptr [rsi]
0084C0D5  48 8B CB                        mov rcx, rbx
0084C0D8  89 7D 48                        mov dword ptr [rbp + 0x48], edi
0084C0DB  8B D7                           mov edx, edi
0084C0DD  0F 84 4E 01 00 00               je 0x14084c231
0084C0E3  E8 78 8B 00 00                  call 0x140854c60
0084C0E8  B9 F5 03 00 00                  mov ecx, 0x3f5
0084C0ED  66 39 48 02                     cmp word ptr [rax + 2], cx
0084C0F1  0F 82 B8 00 00 00               jb 0x14084c1af
0084C0F7  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0084C0FC  FF C8                           dec eax
0084C0FE  44 3B F8                        cmp r15d, eax
0084C101  0F 82 DF 01 00 00               jb 0x14084c2e6
0084C107  8B F1                           mov esi, ecx
0084C109  44 8B 4D 58                     mov r9d, dword ptr [rbp + 0x58]
0084C10D  48 8D 45 E0                     lea rax, [rbp - 0x20]
0084C111  41 8B 14 24                     mov edx, dword ptr [r12]
0084C115  45 8B C7                        mov r8d, r15d
0084C118  48 8B CB                        mov rcx, rbx
0084C11B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084C120  E8 BB 06 23 00                  call 0x140a7c7e0
0084C125  8B F8                           mov edi, eax
0084C127  85 C0                           test eax, eax
0084C129  0F 88 8F 00 00 00               js 0x14084c1be
0084C12F  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C136  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0084C13A  48 8B CB                        mov rcx, rbx
0084C13D  0F 85 24 01 00 00               jne 0x14084c267
0084C143  E8 F8 9D 00 00                  call 0x140855f40
0084C148  8B 55 E0                        mov edx, dword ptr [rbp - 0x20]
0084C14B  4C 8D 45 F0                     lea r8, [rbp - 0x10]
0084C14F  41 89 14 24                     mov dword ptr [r12], edx
0084C153  48 8B CB                        mov rcx, rbx
0084C156  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C15D  0F 84 D8 00 00 00               je 0x14084c23b
0084C163  E8 F8 8A 00 00                  call 0x140854c60
0084C168  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C16F  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0084C173  4C 8B F0                        mov r14, rax
0084C176  48 8B CB                        mov rcx, rbx
0084C179  0F 85 F2 00 00 00               jne 0x14084c271
0084C17F  E8 BC 9D 00 00                  call 0x140855f40
0084C184  E9 AB FE FF FF                  jmp 0x14084c034
0084C189  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C190  8B D7                           mov edx, edi
0084C192  0F 84 8F 00 00 00               je 0x14084c227
0084C198  E8 C3 8A 00 00                  call 0x140854c60
0084C19D  66 39 70 02                     cmp word ptr [rax + 2], si
0084C1A1  0F 83 62 FF FF FF               jae 0x14084c109
0084C1A7  49 8D 77 01                     lea rsi, [r15 + 1]
0084C1AB  49 8D 34 B6                     lea rsi, [r14 + rsi*4]
0084C1AF  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0084C1B3  48 89 30                        mov qword ptr [rax], rsi
0084C1B6  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0084C1BA  89 38                           mov dword ptr [rax], edi
0084C1BC  33 FF                           xor edi, edi
0084C1BE  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C1C5  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0084C1C9  48 8B CB                        mov rcx, rbx
0084C1CC  0F 85 81 00 00 00               jne 0x14084c253
0084C1D2  E8 69 9D 00 00                  call 0x140855f40
0084C1D7  4D 85 F6                        test r14, r14
0084C1DA  74 15                           je 0x14084c1f1
0084C1DC  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C1E3  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0084C1E7  48 8B CB                        mov rcx, rbx
0084C1EA  75 60                           jne 0x14084c24c
0084C1EC  E8 4F 9D 00 00                  call 0x140855f40
0084C1F1  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0084C1F9  8B C7                           mov eax, edi
0084C1FB  48 83 C4 50                     add rsp, 0x50
0084C1FF  41 5F                           pop r15
0084C201  41 5E                           pop r14
0084C203  41 5D                           pop r13
0084C205  41 5C                           pop r12
0084C207  5F                              pop rdi
0084C208  5E                              pop rsi
0084C209  5D                              pop rbp
0084C20A  C3                              ret
0084C20B  CC                              int3
0084C20C  E8 9F 8A 00 00                  call 0x140854cb0
0084C211  E9 16 FE FF FF                  jmp 0x14084c02c
0084C216  BF 9A 00 00 C0                  mov edi, 0xc000009a
0084C21B  EB A1                           jmp 0x14084c1be
0084C21D  E8 8E 8A 00 00                  call 0x140854cb0
0084C222  E9 61 FE FF FF                  jmp 0x14084c088
0084C227  E8 84 8A 00 00                  call 0x140854cb0
0084C22C  E9 6C FF FF FF                  jmp 0x14084c19d
0084C231  E8 7A 8A 00 00                  call 0x140854cb0
0084C236  E9 AD FE FF FF                  jmp 0x14084c0e8
0084C23B  E8 70 8A 00 00                  call 0x140854cb0
0084C240  E9 23 FF FF FF                  jmp 0x14084c168
0084C245  BF 9A 00 00 C0                  mov edi, 0xc000009a
0084C24A  EB 8B                           jmp 0x14084c1d7
0084C24C  E8 CF 09 01 00                  call 0x14085cc20
0084C251  EB 9E                           jmp 0x14084c1f1
0084C253  E8 C8 09 01 00                  call 0x14085cc20
0084C258  E9 7A FF FF FF                  jmp 0x14084c1d7
0084C25D  E8 BE 09 01 00                  call 0x14085cc20
0084C262  E9 61 FE FF FF                  jmp 0x14084c0c8
0084C267  E8 B4 09 01 00                  call 0x14085cc20
0084C26C  E9 D7 FE FF FF                  jmp 0x14084c148
0084C271  E8 AA 09 01 00                  call 0x14085cc20
0084C276  E9 B9 FD FF FF                  jmp 0x14084c034
0084C27B  8A 83 8C 00 00 00               mov al, byte ptr [rbx + 0x8c]
0084C281  24 01                           and al, 1
0084C283  45 85 FF                        test r15d, r15d
0084C286  75 4B                           jne 0x14084c2d3
0084C288  84 C0                           test al, al
0084C28A  75 40                           jne 0x14084c2cc
0084C28C  E8 AF 9C 00 00                  call 0x140855f40
0084C291  49 8D 76 04                     lea rsi, [r14 + 4]
0084C295  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C29C  4C 8D 45 E8                     lea r8, [rbp - 0x18]
0084C2A0  8B 3E                           mov edi, dword ptr [rsi]
0084C2A2  48 8B CB                        mov rcx, rbx
0084C2A5  89 7D 48                        mov dword ptr [rbp + 0x48], edi
0084C2A8  8B D7                           mov edx, edi
0084C2AA  74 19                           je 0x14084c2c5
0084C2AC  E8 AF 89 00 00                  call 0x140854c60
0084C2B1  B9 F5 03 00 00                  mov ecx, 0x3f5
0084C2B6  66 39 48 02                     cmp word ptr [rax + 2], cx
0084C2BA  0F 82 EF FE FF FF               jb 0x14084c1af
0084C2C0  E9 42 FE FF FF                  jmp 0x14084c107
0084C2C5  E8 E6 89 00 00                  call 0x140854cb0
0084C2CA  EB E5                           jmp 0x14084c2b1
0084C2CC  E8 4F 09 01 00                  call 0x14085cc20
0084C2D1  EB BE                           jmp 0x14084c291
0084C2D3  84 C0                           test al, al
0084C2D5  0F 84 91 A5 2C 00               je 0x140b1686c
0084C2DB  E8 40 09 01 00                  call 0x14085cc20
0084C2E0  90                              nop
0084C2E1  E9 8B A5 2C 00                  jmp 0x140b16871
0084C2E6  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0084C2ED  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0084C2F1  48 8B CB                        mov rcx, rbx
0084C2F4  0F 84 7D A5 2C 00               je 0x140b16877
0084C2FA  E8 21 09 01 00                  call 0x14085cc20
0084C2FF  90                              nop
0084C300  E9 77 A5 2C 00                  jmp 0x140b1687c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSelectLeaf(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (80);
    v_r14 = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_stack_p10 = 0;
    v_stack_m48 = (unsigned int)(a1);
    v_stack_m50 = (unsigned int)(a1);
    a4 = 0;
    v_stack_m58 = 0;
    a3 = 0;
    v_stack_m44 = 0;
    v_stack_m4C = 0;
    result = HvpMarkCellDirty(a1, (unsigned int)(*(unsigned int *)(a2)), a3, a4);
    if (sign_flag) goto loc_0084C1F1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084C20C;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a2)), v_stack_m48, a4);
loc_0084C02C:
loc_0084C034:
    a4 = 0;
    v_stack_m68 = v_stack_p10;
    result = CmpFindSubKeyInRoot(a1, result, 0, a4);
    if (sign_flag) goto loc_0084C245;
    if (((unsigned int)((unsigned int)(v_stack_p10))) != -1) goto loc_0084C189;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084C21D;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + (unsigned int)((unsigned int)(result)) + 1 * 4)), v_stack_m50, a4);
loc_0084C088:
    a3 = 0;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    result = CmpDoCompareKeyName(a1, 0, a3, (unsigned int)(*(unsigned int *)(result + 4)));
    if (((unsigned int)(result)) == 2) goto loc_0084C216;
    if (sign_flag) goto loc_0084C27B;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084C25D;
    result = HvpReleaseCellPaged(a1, v_stack_m50, a3, (unsigned int)(*(unsigned int *)(result + 4)));
loc_0084C0C8:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)((unsigned int)(result)) + 1 * 4)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084C231;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)((unsigned int)(result)) + 1 * 4)))), v_stack_m50, (unsigned int)(*(unsigned int *)(result + 4)));
loc_0084C0E8:
    if ((*(unsigned __int16 *)(result + 2)) < ((unsigned __int16)((unsigned int)(0x3F5ULL)))) goto loc_0084C1AF;
    result = (unsigned int)((*(unsigned __int16 *)(result + 2)) - 1);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < ((unsigned int)(result))) goto loc_0084C2E6;
loc_0084C107:
loc_0084C109:
    v_stack_m68 = v_stack_m58;
    result = CmpSplitLeaf(a1, (unsigned int)(*(unsigned int *)(a2)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_p20));
    if (sign_flag) goto loc_0084C1BE;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084C267;
    result = HvpReleaseCellPaged(a1, v_stack_m48, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_p20));
loc_0084C148:
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(v_stack_m58));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084C23B;
    result = HvpGetCellFlat(a1, (unsigned int)(v_stack_m58), v_stack_m48, (unsigned int)(v_stack_p20));
loc_0084C168:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084C271;
    result = HvpReleaseCellPaged(a1, v_stack_m50, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C034;
loc_0084C189:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0084C227;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m48, (unsigned int)(v_stack_p20));
loc_0084C19D:
    if ((*(unsigned __int16 *)(result + 2)) >= ((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(0x3F5ULL)))))) goto loc_0084C109;
loc_0084C1AF:
    *(unsigned __int64 *)(a5) = result + (unsigned int)((unsigned int)(result)) + 1 * 4;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_rdi = 0;
loc_0084C1BE:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084C253;
    result = HvpReleaseCellPaged(a1, v_stack_m50, v_stack_m48, (unsigned int)(v_stack_p20));
loc_0084C1D7:
    if (result == 0) goto loc_0084C1F1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0084C24C;
    result = HvpReleaseCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
loc_0084C1F1:
    v_rsp = (v_rsp) + (80);
    return 0;
loc_0084C20C:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C02C;
loc_0084C216:
    goto loc_0084C1BE;
loc_0084C21D:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C088;
loc_0084C227:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C19D;
loc_0084C231:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C0E8;
loc_0084C23B:
    result = HvpGetCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C168;
loc_0084C245:
    goto loc_0084C1D7;
loc_0084C24C:
    result = HvpReleaseCellFlat(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C1F1;
loc_0084C253:
    result = HvpReleaseCellFlat(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C1D7;
loc_0084C25D:
    result = HvpReleaseCellFlat(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C0C8;
loc_0084C267:
    result = HvpReleaseCellFlat(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C148;
loc_0084C271:
    result = HvpReleaseCellFlat(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
    goto loc_0084C034;
loc_0084C27B:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0084C2D3;
    if ((unsigned __int8)(result) != 0) goto loc_0084C2CC;
    result = HvpReleaseCellPaged(a1, v_stack_m48, v_stack_m48, (unsigned int)(v_stack_p20));
loc_0084C291:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_0084C2C5;
    result = HvpGetCellFlat(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m50, (unsigned int)(v_stack_p20));
loc_0084C2B1:
    if ((*(unsigned __int16 *)(result + 2)) < ((unsigned __int16)((unsigned int)(0x3F5ULL)))) goto loc_0084C1AF;
    goto loc_0084C107;
loc_0084C2C5:
    result = HvpGetCellPaged((unsigned int)(0x3F5ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m50, (unsigned int)(v_stack_p20));
    goto loc_0084C2B1;
loc_0084C2CC:
    result = HvpReleaseCellFlat((unsigned int)(0x3F5ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m50, (unsigned int)(v_stack_p20));
    goto loc_0084C291;
loc_0084C2D3:
    result = HvpReleaseCellFlat((unsigned int)(0x3F5ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m50, (unsigned int)(v_stack_p20));
loc_0084C2E6:
    result = HvpReleaseCellFlat(v_stack_p8, v_stack_m50, v_stack_m50, (unsigned int)(v_stack_p20));
}
```

## 5. (Beta) C Style

```c
int64_t CmpSelectLeaf(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (80);
    local_r14 = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    v_stack_p10 = 0;
    v_stack_m48 = (uint32_t)(Arg1);
    v_stack_m50 = (uint32_t)(Arg1);
    Arg4 = 0;
    v_stack_m58 = 0;
    Arg3 = 0;
    v_stack_m44 = 0;
    v_stack_m4C = 0;
    result = HvpMarkCellDirty(Arg1, (uint32_t)(*(uint32_t *)(arg2)), Arg3, Arg4);
    if (sign_flag) goto loc_0084C1F1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084C20C;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg2)), v_stack_m48, Arg4);
loc_0084C02C:
loc_0084C034:
    Arg4 = 0;
    v_stack_m68 = v_stack_p10;
    result = CmpFindSubKeyInRoot(Arg1, result, 0, Arg4);
    if (sign_flag) goto loc_0084C245;
    if (((uint32_t)((uint32_t)(v_stack_p10))) != -1) goto loc_0084C189;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084C21D;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + (uint32_t)((uint32_t)(result)) + 0x1 * 4)), v_stack_m50, Arg4);
loc_0084C088:
    Arg3 = 0;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    result = CmpDoCompareKeyName(Arg1, 0, Arg3, (uint32_t)(*(uint32_t *)(result + 0x4)));
    if (((uint32_t)(result)) == 2) goto loc_0084C216;
    if (sign_flag) goto loc_0084C27B;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084C25D;
    result = HvpReleaseCellPaged(Arg1, v_stack_m50, Arg3, (uint32_t)(*(uint32_t *)(result + 0x4)));
loc_0084C0C8:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)((uint32_t)(result)) + 0x1 * 4)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084C231;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)((uint32_t)(result)) + 0x1 * 4)))), v_stack_m50, (uint32_t)(*(uint32_t *)(result + 0x4)));
loc_0084C0E8:
    if ((*(uint16_t *)(result + 0x2)) < ((uint16_t)((uint32_t)(0x3F5ULL)))) goto loc_0084C1AF;
    result = (uint32_t)((*(uint16_t *)(result + 0x2)) - 1);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < ((uint32_t)(result))) goto loc_0084C2E6;
loc_0084C107:
loc_0084C109:
    v_stack_m68 = v_stack_m58;
    result = CmpSplitLeaf(Arg1, (uint32_t)(*(uint32_t *)(arg2)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_p20));
    if (sign_flag) goto loc_0084C1BE;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084C267;
    result = HvpReleaseCellPaged(Arg1, v_stack_m48, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_p20));
loc_0084C148:
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(v_stack_m58));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084C23B;
    result = HvpGetCellFlat(Arg1, (uint32_t)(v_stack_m58), v_stack_m48, (uint32_t)(v_stack_p20));
loc_0084C168:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084C271;
    result = HvpReleaseCellPaged(Arg1, v_stack_m50, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C034;
loc_0084C189:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0084C227;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m48, (uint32_t)(v_stack_p20));
loc_0084C19D:
    if ((*(uint16_t *)(result + 0x2)) >= ((uint16_t)((uint32_t)((uint32_t)((uint32_t)(0x3F5ULL)))))) goto loc_0084C109;
loc_0084C1AF:
    *(uint64_t *)(arg5) = result + (uint32_t)((uint32_t)(result)) + 1 * 4;
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)((uint32_t)(result)));
    local_rdi = 0;
loc_0084C1BE:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084C253;
    result = HvpReleaseCellPaged(Arg1, v_stack_m50, v_stack_m48, (uint32_t)(v_stack_p20));
loc_0084C1D7:
    if (result == 0) goto loc_0084C1F1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0084C24C;
    result = HvpReleaseCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
loc_0084C1F1:
    local_rsp = (local_rsp) + (80);
    return 0;
loc_0084C20C:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C02C;
loc_0084C216:
    goto loc_0084C1BE;
loc_0084C21D:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C088;
loc_0084C227:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C19D;
loc_0084C231:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C0E8;
loc_0084C23B:
    result = HvpGetCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C168;
loc_0084C245:
    goto loc_0084C1D7;
loc_0084C24C:
    result = HvpReleaseCellFlat(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C1F1;
loc_0084C253:
    result = HvpReleaseCellFlat(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C1D7;
loc_0084C25D:
    result = HvpReleaseCellFlat(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C0C8;
loc_0084C267:
    result = HvpReleaseCellFlat(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C148;
loc_0084C271:
    result = HvpReleaseCellFlat(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
    goto loc_0084C034;
loc_0084C27B:
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0084C2D3;
    if ((uint8_t)(result) != 0) goto loc_0084C2CC;
    result = HvpReleaseCellPaged(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(v_stack_p20));
loc_0084C291:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_0084C2C5;
    result = HvpGetCellFlat(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m50, (uint32_t)(v_stack_p20));
loc_0084C2B1:
    if ((*(uint16_t *)(result + 0x2)) < ((uint16_t)((uint32_t)(0x3F5ULL)))) goto loc_0084C1AF;
    goto loc_0084C107;
loc_0084C2C5:
    result = HvpGetCellPaged((uint32_t)(0x3F5ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m50, (uint32_t)(v_stack_p20));
    goto loc_0084C2B1;
loc_0084C2CC:
    result = HvpReleaseCellFlat((uint32_t)(0x3F5ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m50, (uint32_t)(v_stack_p20));
    goto loc_0084C291;
loc_0084C2D3:
    result = HvpReleaseCellFlat((uint32_t)(0x3F5ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m50, (uint32_t)(v_stack_p20));
loc_0084C2E6:
    result = HvpReleaseCellFlat(v_stack_p8, v_stack_m50, v_stack_m50, (uint32_t)(v_stack_p20));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084BFB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
