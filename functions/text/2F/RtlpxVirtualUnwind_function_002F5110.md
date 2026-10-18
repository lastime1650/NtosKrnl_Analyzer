# RtlpxVirtualUnwind

- RVA: `0x002F5110`–`0x002F5D33` (길이 `3,107` bytes)
- VA: `0x00000001402F5110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00072180`
- 디코드: `739`개 명령, `3,107/3,107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002F517D` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F5251` → [RtlpUnwindPrologue](RtlpUnwindPrologue_function_002F5FA0.md) (function, `0x002F5FA0`)
- `0x002F5303` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x002F5536` → [RtlpUnwindEpilogue](../3F/RtlpUnwindEpilogue_function_003F8E90.md) (function, `0x003F8E90`)
- `0x002F55BB` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F5645` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F56A0` → [RtlpVirtualPopShadowStack](../3F/RtlpVirtualPopShadowStack_function_003F92C0.md) (function, `0x003F92C0`)
- `0x002F584E` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F59F6` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F5A4B` → [RtlpVirtualPopShadowStack](../3F/RtlpVirtualPopShadowStack_function_003F92C0.md) (function, `0x003F92C0`)
- `0x002F5AC9` → [RtlpUnwindOpSlots](../3F/RtlpUnwindOpSlots_function_003F9270.md) (function, `0x003F9270`)
- `0x002F5B69` → [RtlpSameFunction](../48/RtlpSameFunction_function_0048E81C.md) (function, `0x0048E81C`)

### Direct callers
- [RtlDispatchException](RtlDispatchException_function_002F22A0.md) at `0x002F24D6`
- [RtlUnwindEx](RtlUnwindEx_function_002F2830.md) at `0x002F29C2`
- [RtlVirtualUnwind2](RtlVirtualUnwind2_function_002F3E20.md) at `0x002F3EA4`
- [RtlpWalkFrameChain](RtlpWalkFrameChain_function_002F3ED0.md) at `0x002F4272`
- [RtlVirtualUnwind](../47/RtlVirtualUnwind_function_0047D210.md) at `0x0047D271`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x002F517D` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F55BB` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F5645` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F584E` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F59F6` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F5110  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002F5115  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
002F511A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002F511F  53                              push rbx
002F5120  56                              push rsi
002F5121  57                              push rdi
002F5122  41 54                           push r12
002F5124  41 55                           push r13
002F5126  41 56                           push r14
002F5128  41 57                           push r15
002F512A  48 81 EC 80 00 00 00            sub rsp, 0x80
002F5131  49 8B F0                        mov rsi, r8
002F5134  4C 8B D2                        mov r10, rdx
002F5137  44 8B E1                        mov r12d, ecx
002F513A  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
002F5142  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
002F5147  4D 85 C9                        test r9, r9
002F514A  0F 84 CD 04 00 00               je 0x1402f561d
002F5150  33 FF                           xor edi, edi
002F5152  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
002F5157  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
002F515B  44 8B FF                        mov r15d, edi
002F515E  41 8B 59 08                     mov ebx, dword ptr [r9 + 8]
002F5162  48 03 DA                        add rbx, rdx
002F5165  49 BB FF FF FE FF FF 7F 00 00   movabs r11, 0x7ffffffeffff
002F516F  4D 3B C3                        cmp r8, r11
002F5172  77 0F                           ja 0x1402f5183
002F5174  F6 C3 03                        test bl, 3
002F5177  0F 84 91 0B 00 00               je 0x1402f5d0e
002F517D  E8 4E 4E 5A 00                  call 0x140899fd0
002F5182  CC                              int3
002F5183  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
002F518D  44 0F B6 33                     movzx r14d, byte ptr [rbx]
002F5191  41 83 E6 07                     and r14d, 7
002F5195  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
002F519D  48 85 C0                        test rax, rax
002F51A0  0F 85 00 01 00 00               jne 0x1402f52a6
002F51A6  41 83 FE 02                     cmp r14d, 2
002F51AA  73 26                           jae 0x1402f51d2
002F51AC  48 8B CB                        mov rcx, rbx
002F51AF  8B D7                           mov edx, edi
002F51B1  40 38 79 02                     cmp byte ptr [rcx + 2], dil
002F51B5  0F 85 C9 00 00 00               jne 0x1402f5284
002F51BB  F6 01 20                        test byte ptr [rcx], 0x20
002F51BE  0F 85 2F 01 00 00               jne 0x1402f52f3
002F51C4  41 BF 01 00 00 00               mov r15d, 1
002F51CA  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
002F51D2  41 0F BA F4 1F                  btr r12d, 0x1f
002F51D7  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
002F51DB  F6 43 03 0F                     test byte ptr [rbx + 3], 0xf
002F51DF  0F 85 D5 00 00 00               jne 0x1402f52ba
002F51E5  39 7C 24 58                     cmp dword ptr [rsp + 0x58], edi
002F51E9  0F 85 EB 00 00 00               jne 0x1402f52da
002F51EF  49 8B 8D 98 00 00 00            mov rcx, qword ptr [r13 + 0x98]
002F51F6  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
002F51FE  48 89 08                        mov qword ptr [rax], rcx
002F5201  45 85 FF                        test r15d, r15d
002F5204  0F 84 FF 00 00 00               je 0x1402f5309
002F520A  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F5214  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
002F521C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002F5221  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
002F5229  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002F522E  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
002F5236  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002F523B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
002F5240  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
002F5248  4D 8B 00                        mov r8, qword ptr [r8]
002F524B  48 8B D6                        mov rdx, rsi
002F524E  49 8B CA                        mov rcx, r10
002F5251  E8 4A 0D 00 00                  call 0x1402f5fa0
002F5256  85 C0                           test eax, eax
002F5258  78 38                           js 0x1402f5292
002F525A  45 85 E4                        test r12d, r12d
002F525D  0F 85 57 01 00 00               jne 0x1402f53ba
002F5263  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
002F526B  48 85 C9                        test rcx, rcx
002F526E  74 08                           je 0x1402f5278
002F5270  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002F5275  48 89 01                        mov qword ptr [rcx], rax
002F5278  85 FF                           test edi, edi
002F527A  0F 85 01 05 00 00               jne 0x1402f5781
002F5280  33 C0                           xor eax, eax
002F5282  EB 0E                           jmp 0x1402f5292
002F5284  45 85 E4                        test r12d, r12d
002F5287  0F 89 3D FF FF FF               jns 0x1402f51ca
002F528D  B8 28 00 00 C0                  mov eax, 0xc0000028
002F5292  48 81 C4 80 00 00 00            add rsp, 0x80
002F5299  41 5F                           pop r15
002F529B  41 5E                           pop r14
002F529D  41 5D                           pop r13
002F529F  41 5C                           pop r12
002F52A1  5F                              pop rdi
002F52A2  5E                              pop rsi
002F52A3  5B                              pop rbx
002F52A4  C3                              ret
002F52A5  CC                              int3
002F52A6  40 38 38                        cmp byte ptr [rax], dil
002F52A9  0F 85 F7 FE FF FF               jne 0x1402f51a6
002F52AF  41 BF 01 00 00 00               mov r15d, 1
002F52B5  E9 18 FF FF FF                  jmp 0x1402f51d2
002F52BA  8B D6                           mov edx, esi
002F52BC  41 2B D2                        sub edx, r10d
002F52BF  41 2B 11                        sub edx, dword ptr [r9]
002F52C2  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
002F52C6  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
002F52CA  3B D0                           cmp edx, eax
002F52CC  0F 82 CC 07 00 00               jb 0x1402f5a9e
002F52D2  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
002F52DA  0F B6 43 03                     movzx eax, byte ptr [rbx + 3]
002F52DE  8B C8                           mov ecx, eax
002F52E0  83 E1 0F                        and ecx, 0xf
002F52E3  83 E0 F0                        and eax, 0xfffffff0
002F52E6  49 8B 4C CD 78                  mov rcx, qword ptr [r13 + rcx*8 + 0x78]
002F52EB  48 2B C8                        sub rcx, rax
002F52EE  E9 03 FF FF FF                  jmp 0x1402f51f6
002F52F3  FF C2                           inc edx
002F52F5  83 FA 20                        cmp edx, 0x20
002F52F8  0F 86 A9 04 00 00               jbe 0x1402f57a7
002F52FE  B9 FF 00 00 C0                  mov ecx, 0xc00000ff
002F5303  E8 48 17 00 00                  call 0x1402f6a50
002F5308  CC                              int3
002F5309  41 83 FE 02                     cmp r14d, 2
002F530D  0F 82 4F 01 00 00               jb 0x1402f5462
002F5313  44 0F B6 43 02                  movzx r8d, byte ptr [rbx + 2]
002F5318  45 84 C0                        test r8b, r8b
002F531B  0F 84 E9 FE FF FF               je 0x1402f520a
002F5321  0F B7 53 04                     movzx edx, word ptr [rbx + 4]
002F5325  0F B7 CA                        movzx ecx, dx
002F5328  66 C1 E9 08                     shr cx, 8
002F532C  0F B6 C1                        movzx eax, cl
002F532F  24 0F                           and al, 0xf
002F5331  3C 06                           cmp al, 6
002F5333  0F 85 D1 FE FF FF               jne 0x1402f520a
002F5339  0F B6 D2                        movzx edx, dl
002F533C  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
002F5340  44 8B DE                        mov r11d, esi
002F5343  45 2B DA                        sub r11d, r10d
002F5346  F6 C1 10                        test cl, 0x10
002F5349  0F 85 AE 01 00 00               jne 0x1402f54fd
002F534F  8B CF                           mov ecx, edi
002F5351  85 FF                           test edi, edi
002F5353  0F 85 BF 01 00 00               jne 0x1402f5518
002F5359  BA 01 00 00 00                  mov edx, 1
002F535E  45 8B F8                        mov r15d, r8d
002F5361  41 3B D7                        cmp edx, r15d
002F5364  0F 83 EB 00 00 00               jae 0x1402f5455
002F536A  8B C2                           mov eax, edx
002F536C  44 0F B7 74 43 04               movzx r14d, word ptr [rbx + rax*2 + 4]
002F5372  45 0F B7 C6                     movzx r8d, r14w
002F5376  66 41 C1 E8 08                  shr r8w, 8
002F537B  41 0F B6 C0                     movzx eax, r8b
002F537F  24 0F                           and al, 0xf
002F5381  3C 06                           cmp al, 6
002F5383  0F 85 CC 00 00 00               jne 0x1402f5455
002F5389  41 0F B6 C8                     movzx ecx, r8b
002F538D  C1 E9 04                        shr ecx, 4
002F5390  C1 E1 08                        shl ecx, 8
002F5393  41 0F B6 C6                     movzx eax, r14b
002F5397  03 C8                           add ecx, eax
002F5399  0F 84 B6 00 00 00               je 0x1402f5455
002F539F  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
002F53A3  2B C1                           sub eax, ecx
002F53A5  8B C8                           mov ecx, eax
002F53A7  41 8B C3                        mov eax, r11d
002F53AA  2B C1                           sub eax, ecx
002F53AC  3B 44 24 50                     cmp eax, dword ptr [rsp + 0x50]
002F53B0  0F 82 5D 01 00 00               jb 0x1402f5513
002F53B6  FF C2                           inc edx
002F53B8  EB A7                           jmp 0x1402f5361
002F53BA  8B CE                           mov ecx, esi
002F53BC  4C 8B 8C 24 C8 00 00 00         mov r9, qword ptr [rsp + 0xc8]
002F53C4  41 2B C9                        sub ecx, r9d
002F53C7  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
002F53CF  2B 08                           sub ecx, dword ptr [rax]
002F53D1  44 8B 50 08                     mov r10d, dword ptr [rax + 8]
002F53D5  4D 03 D1                        add r10, r9
002F53D8  49 BE FF FF FE FF FF 7F 00 00   movabs r14, 0x7ffffffeffff
002F53E2  49 3B F6                        cmp rsi, r14
002F53E5  77 18                           ja 0x1402f53ff
002F53E7  41 F6 C2 03                     test r10b, 3
002F53EB  0F 85 8C FD FF FF               jne 0x1402f517d
002F53F1  49 8B C2                        mov rax, r10
002F53F4  4C 3B D3                        cmp r10, rbx
002F53F7  48 0F 43 C3                     cmovae rax, rbx
002F53FB  90                              nop
002F53FC  0F B6 00                        movzx eax, byte ptr [rax]
002F53FF  41 0F B6 42 01                  movzx eax, byte ptr [r10 + 1]
002F5404  3B C8                           cmp ecx, eax
002F5406  0F 82 57 FE FF FF               jb 0x1402f5263
002F540C  41 0F B6 02                     movzx eax, byte ptr [r10]
002F5410  C1 E8 03                        shr eax, 3
002F5413  41 84 C4                        test r12b, al
002F5416  0F 84 47 FE FF FF               je 0x1402f5263
002F541C  41 0F B6 4A 02                  movzx ecx, byte ptr [r10 + 2]
002F5421  F6 C1 01                        test cl, 1
002F5424  8D 41 01                        lea eax, [rcx + 1]
002F5427  0F 44 C1                        cmove eax, ecx
002F542A  44 8B C0                        mov r8d, eax
002F542D  8D 50 02                        lea edx, [rax + 2]
002F5430  48 8D 52 02                     lea rdx, [rdx + 2]
002F5434  49 8D 14 52                     lea rdx, [r10 + rdx*2]
002F5438  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002F5440  48 89 10                        mov qword ptr [rax], rdx
002F5443  43 8B 44 42 04                  mov eax, dword ptr [r10 + r8*2 + 4]
002F5448  49 03 C1                        add rax, r9
002F544B  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002F5450  E9 0E FE FF FF                  jmp 0x1402f5263
002F5455  85 FF                           test edi, edi
002F5457  0F 84 AD FD FF FF               je 0x1402f520a
002F545D  E9 B6 00 00 00                  jmp 0x1402f5518
002F5462  4C 8B C6                        mov r8, rsi
002F5465  44 8B FF                        mov r15d, edi
002F5468  0F B6 0E                        movzx ecx, byte ptr [rsi]
002F546B  80 F9 48                        cmp cl, 0x48
002F546E  0F 84 5E 03 00 00               je 0x1402f57d2
002F5474  0F B6 C1                        movzx eax, cl
002F5477  24 FE                           and al, 0xfe
002F5479  3C 48                           cmp al, 0x48
002F547B  0F 84 AF 02 00 00               je 0x1402f5730
002F5481  41 0F B6 08                     movzx ecx, byte ptr [r8]
002F5485  49 8D 50 01                     lea rdx, [r8 + 1]
002F5489  0F B6 C1                        movzx eax, cl
002F548C  24 F8                           and al, 0xf8
002F548E  3C 58                           cmp al, 0x58
002F5490  0F 84 11 05 00 00               je 0x1402f59a7
002F5496  0F B6 C1                        movzx eax, cl
002F5499  24 F0                           and al, 0xf0
002F549B  3C 40                           cmp al, 0x40
002F549D  0F 84 45 02 00 00               je 0x1402f56e8
002F54A3  80 F9 F2                        cmp cl, 0xf2
002F54A6  75 06                           jne 0x1402f54ae
002F54A8  4C 8B C2                        mov r8, rdx
002F54AB  0F B6 0A                        movzx ecx, byte ptr [rdx]
002F54AE  8D 41 3E                        lea eax, [rcx + 0x3e]
002F54B1  3C 01                           cmp al, 1
002F54B3  0F 86 9B 00 00 00               jbe 0x1402f5554
002F54B9  80 F9 F3                        cmp cl, 0xf3
002F54BC  0F 84 93 05 00 00               je 0x1402f5a55
002F54C2  8D 41 17                        lea eax, [rcx + 0x17]
002F54C5  A8 FD                           test al, 0xfd
002F54C7  0F 84 7B 04 00 00               je 0x1402f5948
002F54CD  80 F9 FF                        cmp cl, 0xff
002F54D0  0F 84 D9 04 00 00               je 0x1402f59af
002F54D6  80 E1 F8                        and cl, 0xf8
002F54D9  80 F9 48                        cmp cl, 0x48
002F54DC  0F 84 1C 02 00 00               je 0x1402f56fe
002F54E2  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F54EC  85 FF                           test edi, edi
002F54EE  75 6D                           jne 0x1402f555d
002F54F0  4C 8B 94 24 C8 00 00 00         mov r10, qword ptr [rsp + 0xc8]
002F54F8  E9 17 FD FF FF                  jmp 0x1402f5214
002F54FD  41 8B 49 04                     mov ecx, dword ptr [r9 + 4]
002F5501  2B CA                           sub ecx, edx
002F5503  41 8B C3                        mov eax, r11d
002F5506  2B C1                           sub eax, ecx
002F5508  3B C2                           cmp eax, edx
002F550A  40 0F 92 C7                     setb dil
002F550E  E9 3E FE FF FF                  jmp 0x1402f5351
002F5513  BF 01 00 00 00                  mov edi, 1
002F5518  44 2B D9                        sub r11d, ecx
002F551B  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
002F5523  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002F5528  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
002F552D  45 8B C3                        mov r8d, r11d
002F5530  48 8B D6                        mov rdx, rsi
002F5533  49 8B CA                        mov rcx, r10
002F5536  E8 55 39 10 00                  call 0x1403f8e90
002F553B  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
002F5543  48 85 C0                        test rax, rax
002F5546  0F 84 17 FD FF FF               je 0x1402f5263
002F554C  C6 00 00                        mov byte ptr [rax], 0
002F554F  E9 0F FD FF FF                  jmp 0x1402f5263
002F5554  BF 01 00 00 00                  mov edi, 1
002F5559  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
002F555D  49 8D 5D 78                     lea rbx, [r13 + 0x78]
002F5561  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
002F5566  48 8B D6                        mov rdx, rsi
002F5569  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F556E  0F B6 06                        movzx eax, byte ptr [rsi]
002F5571  24 F8                           and al, 0xf8
002F5573  3C 48                           cmp al, 0x48
002F5575  0F 84 5A 03 00 00               je 0x1402f58d5
002F557B  4C 8B 8C 24 08 01 00 00         mov r9, qword ptr [rsp + 0x108]
002F5583  49 BE FF FF FE FF FF 7F 00 00   movabs r14, 0x7ffffffeffff
002F558D  44 0F B6 02                     movzx r8d, byte ptr [rdx]
002F5591  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
002F5596  41 0F B6 C0                     movzx eax, r8b
002F559A  24 F8                           and al, 0xf8
002F559C  3C 58                           cmp al, 0x58
002F559E  0F 85 6D 02 00 00               jne 0x1402f5811
002F55A4  4D 8B 95 98 00 00 00            mov r10, qword ptr [r13 + 0x98]
002F55AB  4C 89 54 24 60                  mov qword ptr [rsp + 0x60], r10
002F55B0  49 3B F6                        cmp rsi, r14
002F55B3  77 24                           ja 0x1402f55d9
002F55B5  41 F6 C2 03                     test r10b, 3
002F55B9  74 06                           je 0x1402f55c1
002F55BB  E8 10 4A 5A 00                  call 0x140899fd0
002F55C0  CC                              int3
002F55C1  49 8B C2                        mov rax, r10
002F55C4  49 BB 00 00 FF FF FF 7F 00 00   movabs r11, 0x7fffffff0000
002F55CE  4D 3B D3                        cmp r10, r11
002F55D1  49 0F 43 C3                     cmovae rax, r11
002F55D5  90                              nop
002F55D6  0F B6 00                        movzx eax, byte ptr [rax]
002F55D9  EB 05                           jmp 0x1402f55e0
002F55DB  E9 7F 06 00 00                  jmp 0x1402f5c5f
002F55E0  49 8B 01                        mov rax, qword ptr [r9]
002F55E3  48 85 C0                        test rax, rax
002F55E6  0F 85 D3 03 00 00               jne 0x1402f59bf
002F55EC  41 83 E0 07                     and r8d, 7
002F55F0  49 8B 02                        mov rax, qword ptr [r10]
002F55F3  4A 89 04 C3                     mov qword ptr [rbx + r8*8], rax
002F55F7  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
002F55FB  48 85 C0                        test rax, rax
002F55FE  74 08                           je 0x1402f5608
002F5600  4E 89 94 C0 80 00 00 00         mov qword ptr [rax + r8*8 + 0x80], r10
002F5608  49 83 85 98 00 00 00 08         add qword ptr [r13 + 0x98], 8
002F5610  48 FF C2                        inc rdx
002F5613  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F5618  E9 70 FF FF FF                  jmp 0x1402f558d
002F561D  49 8D 95 98 00 00 00            lea rdx, [r13 + 0x98]
002F5624  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
002F5629  48 8B 1A                        mov rbx, qword ptr [rdx]
002F562C  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
002F5631  49 BE FF FF FE FF FF 7F 00 00   movabs r14, 0x7ffffffeffff
002F563B  49 3B F6                        cmp rsi, r14
002F563E  77 23                           ja 0x1402f5663
002F5640  F6 C3 03                        test bl, 3
002F5643  74 06                           je 0x1402f564b
002F5645  E8 86 49 5A 00                  call 0x140899fd0
002F564A  CC                              int3
002F564B  48 8B C3                        mov rax, rbx
002F564E  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002F5658  48 3B D9                        cmp rbx, rcx
002F565B  48 0F 43 C1                     cmovae rax, rcx
002F565F  90                              nop
002F5660  0F B6 00                        movzx eax, byte ptr [rax]
002F5663  EB 05                           jmp 0x1402f566a
002F5665  E9 B6 05 00 00                  jmp 0x1402f5c20
002F566A  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
002F5672  48 8B 01                        mov rax, qword ptr [rcx]
002F5675  48 85 C0                        test rax, rax
002F5678  0F 85 71 01 00 00               jne 0x1402f57ef
002F567E  48 8B 03                        mov rax, qword ptr [rbx]
002F5681  48 3B F0                        cmp rsi, rax
002F5684  0F 84 05 05 00 00               je 0x1402f5b8f
002F568A  49 89 85 F8 00 00 00            mov qword ptr [r13 + 0xf8], rax
002F5691  48 83 02 08                     add qword ptr [rdx], 8
002F5695  BA 01 00 00 00                  mov edx, 1
002F569A  44 8B C2                        mov r8d, edx
002F569D  49 8B CD                        mov rcx, r13
002F56A0  E8 1B 3C 10 00                  call 0x1403f92c0
002F56A5  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
002F56AD  48 89 18                        mov qword ptr [rax], rbx
002F56B0  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
002F56B8  48 85 C0                        test rax, rax
002F56BB  74 03                           je 0x1402f56c0
002F56BD  C6 00 00                        mov byte ptr [rax], 0
002F56C0  33 FF                           xor edi, edi
002F56C2  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002F56CA  48 89 38                        mov qword ptr [rax], rdi
002F56CD  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
002F56D5  48 85 C0                        test rax, rax
002F56D8  0F 84 A2 FB FF FF               je 0x1402f5280
002F56DE  48 89 38                        mov qword ptr [rax], rdi
002F56E1  33 C0                           xor eax, eax
002F56E3  E9 AA FB FF FF                  jmp 0x1402f5292
002F56E8  0F B6 02                        movzx eax, byte ptr [rdx]
002F56EB  24 F8                           and al, 0xf8
002F56ED  3C 58                           cmp al, 0x58
002F56EF  0F 85 AE FD FF FF               jne 0x1402f54a3
002F56F5  49 83 C0 02                     add r8, 2
002F56F9  E9 83 FD FF FF                  jmp 0x1402f5481
002F56FE  41 80 78 01 FF                  cmp byte ptr [r8 + 1], 0xff
002F5703  0F 85 D9 FD FF FF               jne 0x1402f54e2
002F5709  41 0F B6 40 02                  movzx eax, byte ptr [r8 + 2]
002F570E  24 38                           and al, 0x38
002F5710  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F571A  3C 20                           cmp al, 0x20
002F571C  0F 85 CA FD FF FF               jne 0x1402f54ec
002F5722  BF 01 00 00 00                  mov edi, 1
002F5727  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
002F572B  E9 BC FD FF FF                  jmp 0x1402f54ec
002F5730  80 7E 01 8D                     cmp byte ptr [rsi + 1], 0x8d
002F5734  0F 85 47 FD FF FF               jne 0x1402f5481
002F573A  0F B6 56 02                     movzx edx, byte ptr [rsi + 2]
002F573E  44 8B F9                        mov r15d, ecx
002F5741  41 83 E7 01                     and r15d, 1
002F5745  41 C1 E7 03                     shl r15d, 3
002F5749  8B C2                           mov eax, edx
002F574B  83 E0 07                        and eax, 7
002F574E  44 0B F8                        or r15d, eax
002F5751  0F 84 2A FD FF FF               je 0x1402f5481
002F5757  0F B6 43 03                     movzx eax, byte ptr [rbx + 3]
002F575B  83 E0 0F                        and eax, 0xf
002F575E  44 3B F8                        cmp r15d, eax
002F5761  0F 85 1A FD FF FF               jne 0x1402f5481
002F5767  80 E2 F8                        and dl, 0xf8
002F576A  80 FA 60                        cmp dl, 0x60
002F576D  0F 84 6F 04 00 00               je 0x1402f5be2
002F5773  80 FA A0                        cmp dl, 0xa0
002F5776  0F 85 05 FD FF FF               jne 0x1402f5481
002F577C  E9 58 04 00 00                  jmp 0x1402f5bd9
002F5781  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
002F5786  0F 84 F4 FA FF FF               je 0x1402f5280
002F578C  49 8B 8D 98 00 00 00            mov rcx, qword ptr [r13 + 0x98]
002F5793  48 83 E9 08                     sub rcx, 8
002F5797  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
002F579F  48 89 08                        mov qword ptr [rax], rcx
002F57A2  E9 D9 FA FF FF                  jmp 0x1402f5280
002F57A7  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
002F57AA  49 03 CA                        add rcx, r10
002F57AD  49 3B F3                        cmp rsi, r11
002F57B0  0F 87 FB F9 FF FF               ja 0x1402f51b1
002F57B6  F6 C1 03                        test cl, 3
002F57B9  0F 85 BE F9 FF FF               jne 0x1402f517d
002F57BF  48 8B C1                        mov rax, rcx
002F57C2  49 3B C8                        cmp rcx, r8
002F57C5  49 0F 43 C0                     cmovae rax, r8
002F57C9  90                              nop
002F57CA  0F B6 00                        movzx eax, byte ptr [rax]
002F57CD  E9 DF F9 FF FF                  jmp 0x1402f51b1
002F57D2  80 7E 01 83                     cmp byte ptr [rsi + 1], 0x83
002F57D6  0F 85 6B 04 00 00               jne 0x1402f5c47
002F57DC  80 7E 02 C4                     cmp byte ptr [rsi + 2], 0xc4
002F57E0  0F 85 61 04 00 00               jne 0x1402f5c47
002F57E6  4C 8D 46 04                     lea r8, [rsi + 4]
002F57EA  E9 92 FC FF FF                  jmp 0x1402f5481
002F57EF  48 3B 18                        cmp rbx, qword ptr [rax]
002F57F2  0F 82 95 FA FF FF               jb 0x1402f528d
002F57F8  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002F57FC  48 8B 08                        mov rcx, qword ptr [rax]
002F57FF  48 83 E9 08                     sub rcx, 8
002F5803  48 3B D9                        cmp rbx, rcx
002F5806  0F 87 81 FA FF FF               ja 0x1402f528d
002F580C  E9 6D FE FF FF                  jmp 0x1402f567e
002F5811  41 0F B6 C0                     movzx eax, r8b
002F5815  24 F0                           and al, 0xf0
002F5817  3C 40                           cmp al, 0x40
002F5819  0F 85 C7 01 00 00               jne 0x1402f59e6
002F581F  44 0F B6 52 01                  movzx r10d, byte ptr [rdx + 1]
002F5824  44 88 54 24 48                  mov byte ptr [rsp + 0x48], r10b
002F5829  41 0F B6 C2                     movzx eax, r10b
002F582D  24 F8                           and al, 0xf8
002F582F  3C 58                           cmp al, 0x58
002F5831  0F 85 AF 01 00 00               jne 0x1402f59e6
002F5837  4D 8B 9D 98 00 00 00            mov r11, qword ptr [r13 + 0x98]
002F583E  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
002F5843  49 3B F6                        cmp rsi, r14
002F5846  77 24                           ja 0x1402f586c
002F5848  41 F6 C3 03                     test r11b, 3
002F584C  74 06                           je 0x1402f5854
002F584E  E8 7D 47 5A 00                  call 0x140899fd0
002F5853  CC                              int3
002F5854  49 8B C3                        mov rax, r11
002F5857  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
002F5861  4D 3B DF                        cmp r11, r15
002F5864  49 0F 43 C7                     cmovae rax, r15
002F5868  90                              nop
002F5869  0F B6 00                        movzx eax, byte ptr [rax]
002F586C  EB 05                           jmp 0x1402f5873
002F586E  E9 4D 04 00 00                  jmp 0x1402f5cc0
002F5873  49 8B 01                        mov rax, qword ptr [r9]
002F5876  48 85 C0                        test rax, rax
002F5879  74 1D                           je 0x1402f5898
002F587B  4C 3B 18                        cmp r11, qword ptr [rax]
002F587E  0F 82 09 FA FF FF               jb 0x1402f528d
002F5884  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002F5888  48 8B 08                        mov rcx, qword ptr [rax]
002F588B  48 83 E9 08                     sub rcx, 8
002F588F  4C 3B D9                        cmp r11, rcx
002F5892  0F 87 53 03 00 00               ja 0x1402f5beb
002F5898  41 83 E0 01                     and r8d, 1
002F589C  49 C1 E0 03                     shl r8, 3
002F58A0  41 83 E2 07                     and r10d, 7
002F58A4  4D 0B C2                        or r8, r10
002F58A7  49 8B 03                        mov rax, qword ptr [r11]
002F58AA  4A 89 04 C3                     mov qword ptr [rbx + r8*8], rax
002F58AE  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
002F58B2  48 85 C0                        test rax, rax
002F58B5  74 08                           je 0x1402f58bf
002F58B7  4E 89 9C C0 80 00 00 00         mov qword ptr [rax + r8*8 + 0x80], r11
002F58BF  49 83 85 98 00 00 00 08         add qword ptr [r13 + 0x98], 8
002F58C7  48 83 C2 02                     add rdx, 2
002F58CB  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F58D0  E9 B8 FC FF FF                  jmp 0x1402f558d
002F58D5  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
002F58D9  3C 83                           cmp al, 0x83
002F58DB  0F 84 3E 02 00 00               je 0x1402f5b1f
002F58E1  3C 81                           cmp al, 0x81
002F58E3  0F 84 B0 02 00 00               je 0x1402f5b99
002F58E9  3C 8D                           cmp al, 0x8d
002F58EB  0F 85 8A FC FF FF               jne 0x1402f557b
002F58F1  0F B6 46 02                     movzx eax, byte ptr [rsi + 2]
002F58F5  24 F8                           and al, 0xf8
002F58F7  3C 60                           cmp al, 0x60
002F58F9  0F 84 F6 02 00 00               je 0x1402f5bf5
002F58FF  3C A0                           cmp al, 0xa0
002F5901  0F 85 74 FC FF FF               jne 0x1402f557b
002F5907  0F B6 56 06                     movzx edx, byte ptr [rsi + 6]
002F590B  C1 E2 08                        shl edx, 8
002F590E  0F B6 46 05                     movzx eax, byte ptr [rsi + 5]
002F5912  0B D0                           or edx, eax
002F5914  C1 E2 08                        shl edx, 8
002F5917  0F B6 46 04                     movzx eax, byte ptr [rsi + 4]
002F591B  0B D0                           or edx, eax
002F591D  C1 E2 08                        shl edx, 8
002F5920  0F B6 46 03                     movzx eax, byte ptr [rsi + 3]
002F5924  0B D0                           or edx, eax
002F5926  41 8B C7                        mov eax, r15d
002F5929  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
002F592D  48 63 C2                        movsxd rax, edx
002F5930  48 03 C1                        add rax, rcx
002F5933  49 89 85 98 00 00 00            mov qword ptr [r13 + 0x98], rax
002F593A  48 8D 56 07                     lea rdx, [rsi + 7]
002F593E  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F5943  E9 33 FC FF FF                  jmp 0x1402f557b
002F5948  4D 8B F0                        mov r14, r8
002F594B  4D 2B F2                        sub r14, r10
002F594E  80 F9 EB                        cmp cl, 0xeb
002F5951  0F 85 3B 01 00 00               jne 0x1402f5a92
002F5957  41 0F BE 40 01                  movsx eax, byte ptr [r8 + 1]
002F595C  83 C0 02                        add eax, 2
002F595F  48 98                           cdqe
002F5961  4C 03 F0                        add r14, rax
002F5964  41 8B 09                        mov ecx, dword ptr [r9]
002F5967  4C 3B F1                        cmp r14, rcx
002F596A  0F 82 C9 01 00 00               jb 0x1402f5b39
002F5970  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
002F5974  4C 3B F0                        cmp r14, rax
002F5977  0F 83 BC 01 00 00               jae 0x1402f5b39
002F597D  4C 3B F1                        cmp r14, rcx
002F5980  0F 85 5C FB FF FF               jne 0x1402f54e2
002F5986  F6 03 20                        test byte ptr [rbx], 0x20
002F5989  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F5993  0F 85 53 FB FF FF               jne 0x1402f54ec
002F5999  BF 01 00 00 00                  mov edi, 1
002F599E  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
002F59A2  E9 45 FB FF FF                  jmp 0x1402f54ec
002F59A7  4C 8B C2                        mov r8, rdx
002F59AA  E9 D2 FA FF FF                  jmp 0x1402f5481
002F59AF  41 80 78 01 25                  cmp byte ptr [r8 + 1], 0x25
002F59B4  0F 85 1C FB FF FF               jne 0x1402f54d6
002F59BA  E9 95 FB FF FF                  jmp 0x1402f5554
002F59BF  4C 3B 10                        cmp r10, qword ptr [rax]
002F59C2  0F 82 C5 F8 FF FF               jb 0x1402f528d
002F59C8  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002F59CC  48 8B 08                        mov rcx, qword ptr [rax]
002F59CF  48 83 E9 08                     sub rcx, 8
002F59D3  4C 3B D1                        cmp r10, rcx
002F59D6  0F 86 10 FC FF FF               jbe 0x1402f55ec
002F59DC  B8 28 00 00 C0                  mov eax, 0xc0000028
002F59E1  E9 AC F8 FF FF                  jmp 0x1402f5292
002F59E6  49 3B F6                        cmp rsi, r14
002F59E9  77 26                           ja 0x1402f5a11
002F59EB  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
002F59F2  A8 03                           test al, 3
002F59F4  74 06                           je 0x1402f59fc
002F59F6  E8 D5 45 5A 00                  call 0x140899fd0
002F59FB  CC                              int3
002F59FC  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F5A06  48 3B C3                        cmp rax, rbx
002F5A09  48 0F 43 C3                     cmovae rax, rbx
002F5A0D  90                              nop
002F5A0E  0F B6 00                        movzx eax, byte ptr [rax]
002F5A11  EB 05                           jmp 0x1402f5a18
002F5A13  E9 8F 02 00 00                  jmp 0x1402f5ca7
002F5A18  49 8B 01                        mov rax, qword ptr [r9]
002F5A1B  48 85 C0                        test rax, rax
002F5A1E  75 45                           jne 0x1402f5a65
002F5A20  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
002F5A25  48 81 C2 98 00 00 00            add rdx, 0x98
002F5A2C  48 8B 0A                        mov rcx, qword ptr [rdx]
002F5A2F  48 8B 01                        mov rax, qword ptr [rcx]
002F5A32  49 89 85 F8 00 00 00            mov qword ptr [r13 + 0xf8], rax
002F5A39  48 8D 41 08                     lea rax, [rcx + 8]
002F5A3D  48 89 02                        mov qword ptr [rdx], rax
002F5A40  BA 01 00 00 00                  mov edx, 1
002F5A45  44 8B C2                        mov r8d, edx
002F5A48  49 8B CD                        mov rcx, r13
002F5A4B  E8 70 38 10 00                  call 0x1403f92c0
002F5A50  E9 E6 FA FF FF                  jmp 0x1402f553b
002F5A55  41 80 78 01 C3                  cmp byte ptr [r8 + 1], 0xc3
002F5A5A  0F 85 62 FA FF FF               jne 0x1402f54c2
002F5A60  E9 EF FA FF FF                  jmp 0x1402f5554
002F5A65  49 8D 95 98 00 00 00            lea rdx, [r13 + 0x98]
002F5A6C  4C 8B 02                        mov r8, qword ptr [rdx]
002F5A6F  4C 3B 00                        cmp r8, qword ptr [rax]
002F5A72  0F 82 15 F8 FF FF               jb 0x1402f528d
002F5A78  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002F5A7C  48 8B 08                        mov rcx, qword ptr [rax]
002F5A7F  48 83 E9 08                     sub rcx, 8
002F5A83  4C 3B C1                        cmp r8, rcx
002F5A86  76 A4                           jbe 0x1402f5a2c
002F5A88  B8 28 00 00 C0                  mov eax, 0xc0000028
002F5A8D  E9 00 F8 FF FF                  jmp 0x1402f5292
002F5A92  41 8B 40 01                     mov eax, dword ptr [r8 + 1]
002F5A96  83 C0 05                        add eax, 5
002F5A99  E9 C1 FE FF FF                  jmp 0x1402f595f
002F5A9E  F6 03 20                        test byte ptr [rbx], 0x20
002F5AA1  0F 85 2B F8 FF FF               jne 0x1402f52d2
002F5AA7  44 8B C7                        mov r8d, edi
002F5AAA  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
002F5AAE  40 38 7B 02                     cmp byte ptr [rbx + 2], dil
002F5AB2  76 4E                           jbe 0x1402f5b02
002F5AB4  41 8B C8                        mov ecx, r8d
002F5AB7  0F B7 4C 4B 04                  movzx ecx, word ptr [rbx + rcx*2 + 4]
002F5ABC  0F B7 C1                        movzx eax, cx
002F5ABF  66 C1 E8 08                     shr ax, 8
002F5AC3  24 0F                           and al, 0xf
002F5AC5  3C 03                           cmp al, 3
002F5AC7  74 1B                           je 0x1402f5ae4
002F5AC9  E8 A2 37 10 00                  call 0x1403f9270
002F5ACE  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
002F5AD3  44 03 C0                        add r8d, eax
002F5AD6  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
002F5ADB  0F B6 43 02                     movzx eax, byte ptr [rbx + 2]
002F5ADF  44 3B C0                        cmp r8d, eax
002F5AE2  72 D0                           jb 0x1402f5ab4
002F5AE4  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
002F5AEC  4C 8B 94 24 C8 00 00 00         mov r10, qword ptr [rsp + 0xc8]
002F5AF4  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
002F5AF8  49 BB FF FF FE FF FF 7F 00 00   movabs r11, 0x7ffffffeffff
002F5B02  41 8B C0                        mov eax, r8d
002F5B05  0F B6 4C 43 04                  movzx ecx, byte ptr [rbx + rax*2 + 4]
002F5B0A  3B D1                           cmp edx, ecx
002F5B0C  0F 82 D3 F6 FF FF               jb 0x1402f51e5
002F5B12  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
002F5B1A  E9 C6 F6 FF FF                  jmp 0x1402f51e5
002F5B1F  48 0F BE 46 03                  movsx rax, byte ptr [rsi + 3]
002F5B24  49 01 85 98 00 00 00            add qword ptr [r13 + 0x98], rax
002F5B2B  48 8D 56 04                     lea rdx, [rsi + 4]
002F5B2F  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F5B34  E9 42 FA FF FF                  jmp 0x1402f557b
002F5B39  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
002F5B43  49 3B F3                        cmp rsi, r11
002F5B46  77 17                           ja 0x1402f5b5f
002F5B48  4B 8D 04 16                     lea rax, [r14 + r10]
002F5B4C  48 3B C3                        cmp rax, rbx
002F5B4F  48 0F 43 C3                     cmovae rax, rbx
002F5B53  90                              nop
002F5B54  0F B6 00                        movzx eax, byte ptr [rax]
002F5B57  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
002F5B5F  4F 8D 04 16                     lea r8, [r14 + r10]
002F5B63  49 8B D2                        mov rdx, r10
002F5B66  49 8B C9                        mov rcx, r9
002F5B69  E8 AE 8C 19 00                  call 0x14048e81c
002F5B6E  48 85 C0                        test rax, rax
002F5B71  0F 84 DD F9 FF FF               je 0x1402f5554
002F5B77  8B 00                           mov eax, dword ptr [rax]
002F5B79  4C 3B F0                        cmp r14, rax
002F5B7C  0F 84 D2 F9 FF FF               je 0x1402f5554
002F5B82  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
002F5B8A  E9 5D F9 FF FF                  jmp 0x1402f54ec
002F5B8F  B8 FF 00 00 C0                  mov eax, 0xc00000ff
002F5B94  E9 F9 F6 FF FF                  jmp 0x1402f5292
002F5B99  0F B6 4E 06                     movzx ecx, byte ptr [rsi + 6]
002F5B9D  C1 E1 08                        shl ecx, 8
002F5BA0  0F B6 46 05                     movzx eax, byte ptr [rsi + 5]
002F5BA4  0B C8                           or ecx, eax
002F5BA6  C1 E1 08                        shl ecx, 8
002F5BA9  0F B6 46 04                     movzx eax, byte ptr [rsi + 4]
002F5BAD  0B C8                           or ecx, eax
002F5BAF  C1 E1 08                        shl ecx, 8
002F5BB2  0F B6 46 03                     movzx eax, byte ptr [rsi + 3]
002F5BB6  0B C1                           or eax, ecx
002F5BB8  48 98                           cdqe
002F5BBA  49 01 85 98 00 00 00            add qword ptr [r13 + 0x98], rax
002F5BC1  48 8D 56 07                     lea rdx, [rsi + 7]
002F5BC5  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F5BCA  E9 AC F9 FF FF                  jmp 0x1402f557b
002F5BCF  80 7E 02 C4                     cmp byte ptr [rsi + 2], 0xc4
002F5BD3  0F 85 9B F8 FF FF               jne 0x1402f5474
002F5BD9  4C 8D 46 07                     lea r8, [rsi + 7]
002F5BDD  E9 9F F8 FF FF                  jmp 0x1402f5481
002F5BE2  4C 8D 46 04                     lea r8, [rsi + 4]
002F5BE6  E9 96 F8 FF FF                  jmp 0x1402f5481
002F5BEB  B8 28 00 00 C0                  mov eax, 0xc0000028
002F5BF0  E9 9D F6 FF FF                  jmp 0x1402f5292
002F5BF5  41 8B C7                        mov eax, r15d
002F5BF8  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
002F5BFC  49 89 8D 98 00 00 00            mov qword ptr [r13 + 0x98], rcx
002F5C03  48 0F BE 46 03                  movsx rax, byte ptr [rsi + 3]
002F5C08  48 03 C1                        add rax, rcx
002F5C0B  49 89 85 98 00 00 00            mov qword ptr [r13 + 0x98], rax
002F5C12  48 8D 56 04                     lea rdx, [rsi + 4]
002F5C16  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
002F5C1B  E9 5B F9 FF FF                  jmp 0x1402f557b
002F5C20  85 C0                           test eax, eax
002F5C22  0F 88 6A F6 FF FF               js 0x1402f5292
002F5C28  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
002F5C30  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F5C38  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
002F5C3D  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002F5C42  E9 37 FA FF FF                  jmp 0x1402f567e
002F5C47  80 F9 48                        cmp cl, 0x48
002F5C4A  0F 85 24 F8 FF FF               jne 0x1402f5474
002F5C50  80 7E 01 81                     cmp byte ptr [rsi + 1], 0x81
002F5C54  0F 85 1A F8 FF FF               jne 0x1402f5474
002F5C5A  E9 70 FF FF FF                  jmp 0x1402f5bcf
002F5C5F  85 C0                           test eax, eax
002F5C61  0F 88 2B F6 FF FF               js 0x1402f5292
002F5C67  49 BE FF FF FE FF FF 7F 00 00   movabs r14, 0x7ffffffeffff
002F5C71  4C 8B 8C 24 08 01 00 00         mov r9, qword ptr [rsp + 0x108]
002F5C79  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
002F5C81  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F5C89  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
002F5C8D  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
002F5C92  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002F5C97  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
002F5C9C  44 0F B6 44 24 40               movzx r8d, byte ptr [rsp + 0x40]
002F5CA2  E9 45 F9 FF FF                  jmp 0x1402f55ec
002F5CA7  85 C0                           test eax, eax
002F5CA9  0F 88 E3 F5 FF FF               js 0x1402f5292
002F5CAF  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
002F5CB7  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
002F5CBB  E9 60 FD FF FF                  jmp 0x1402f5a20
002F5CC0  85 C0                           test eax, eax
002F5CC2  0F 88 CA F5 FF FF               js 0x1402f5292
002F5CC8  49 BE FF FF FE FF FF 7F 00 00   movabs r14, 0x7ffffffeffff
002F5CD2  4C 8B 8C 24 08 01 00 00         mov r9, qword ptr [rsp + 0x108]
002F5CDA  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
002F5CE2  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F5CEA  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
002F5CEE  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
002F5CF3  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002F5CF8  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
002F5CFD  44 0F B6 44 24 40               movzx r8d, byte ptr [rsp + 0x40]
002F5D03  44 0F B6 54 24 48               movzx r10d, byte ptr [rsp + 0x48]
002F5D09  E9 8A FB FF FF                  jmp 0x1402f5898
002F5D0E  48 8B C3                        mov rax, rbx
002F5D11  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
002F5D1B  49 3B D8                        cmp rbx, r8
002F5D1E  49 0F 43 C0                     cmovae rax, r8
002F5D22  90                              nop
002F5D23  0F B6 00                        movzx eax, byte ptr [rax]
002F5D26  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
002F5D2E  E9 5A F4 FF FF                  jmp 0x1402f518d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpxVirtualUnwind(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m60;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int8 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_stack_m40 = a5;
    if (a4 == 0) goto loc_002F561D;
    v_rdi = 0;
    v_stack_m50 = 0;
    v_stack_m74 = 0;
    v_rbx = ((unsigned int)(*(unsigned int *)(a4 + 8))) + (a2);
    if (a3 > v_r11) goto loc_002F5183;
    if ((((unsigned __int8)(v_rbx)) & (3)) == 0) goto loc_002F5D0E;
loc_002F517D:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_002F5183:
loc_002F518D:
    v_r14 = (unsigned int)((*(unsigned __int8 *)(v_rbx)) & (7));
    if (a6 != 0) goto loc_002F52A6;
loc_002F51A6:
    if (((unsigned int)(v_r14)) >= 2) goto loc_002F51D2;
loc_002F51B1:
    if ((*(unsigned __int8 *)(v_rbx + 2)) != 0) goto loc_002F5284;
    if (((*(unsigned __int8 *)(v_rbx)) & (32)) != 0) goto loc_002F52F3;
loc_002F51CA:
loc_002F51D2:
    v_stack_m60 = 0;
    if (((*(unsigned __int8 *)(v_rbx + 3)) & (15)) != 0) goto loc_002F52BA;
loc_002F51E5:
    if (v_stack_m60 != 0) goto loc_002F52DA;
loc_002F51F6:
    *(unsigned __int64 *)(a8) = *(unsigned __int64 *)(a5 + 152);
    if (1 == 0) goto loc_002F5309;
loc_002F520A:
loc_002F5214:
    v_stack_m80 = a10;
    v_stack_m88 = v_stack_p20;
    v_stack_m90 = a6;
    v_stack_m98 = a5;
    result = RtlpUnwindPrologue(a2, a3, *(unsigned __int64 *)(a8), v_stack_p20);
    if (sign_flag) goto loc_002F5292;
    if ((unsigned int)((unsigned int)(a1)) != 0) goto loc_002F53BA;
loc_002F5263:
    if (a9 != 0) {
        result = v_stack_m50;
        *(unsigned __int64 *)(a9) = result;
    }
    if (0 != 0) goto loc_002F5781;
loc_002F5280:
    result = 0;
    goto loc_002F5292;
loc_002F5284:
    if (!sign_flag) goto loc_002F51CA;
loc_002F528D:
loc_002F5292:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)(0xC0000028ULL);
loc_002F52A6:
    if ((*(unsigned __int8 *)((unsigned int)(0xC0000028ULL))) != 0) goto loc_002F51A6;
    goto loc_002F51D2;
loc_002F52BA:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) - (*(unsigned int *)(v_stack_p20)));
    v_stack_p50 = (unsigned int)(a2);
    if (((unsigned int)(a2)) < ((unsigned int)(*(unsigned __int8 *)(v_rbx + 1)))) goto loc_002F5A9E;
loc_002F52D2:
    v_stack_p58 = 1;
loc_002F52DA:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + 3)))) & (15));
    result = (unsigned int)((*(unsigned __int8 *)(v_rbx + 3)) & (0xFFFFFFF0ULL));
    a1 = (*(unsigned __int64 *)(a5 + a1 * 8 + 120)) - (result);
    goto loc_002F51F6;
loc_002F52F3:
    a2 = (unsigned int)((a2) + 1);
    if (((unsigned int)(a2)) <= 32) goto loc_002F57A7;
    result = RtlRaiseStatus((unsigned int)(0xC00000FFULL), a2, *(unsigned __int64 *)(a8), v_stack_p20);
loc_002F5309:
    if (((unsigned int)(v_r14)) < 2) goto loc_002F5462;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 2)) == 0) goto loc_002F520A;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 4))) >> (8));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (15));
    if (((unsigned __int8)(result)) != 6) goto loc_002F520A;
    v_stack_p50 = (unsigned int)((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 4)));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(a2)));
    if ((((unsigned __int8)(a1)) & (16)) != 0) goto loc_002F54FD;
loc_002F5351:
    if (0 != 0) goto loc_002F5518;
loc_002F5361:
    if (1 >= ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + 2)))))) goto loc_002F5455;
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1 * 2 + 4))) >> (8));
    result = (unsigned __int8)(((unsigned __int8)(a3)) & (15));
    if (((unsigned __int8)(result)) != 6) goto loc_002F5455;
    a1 = (unsigned int)(((unsigned __int8)(a3)) >> (4));
    a1 = (unsigned int)((a1) << (8));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 1 * 2 + 4)))));
    if (condition_is_equal) goto loc_002F5455;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 4))) - (a1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - ((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (((unsigned int)(result)) < v_stack_p50) goto loc_002F5513;
    a2 = (unsigned int)((1) + 1);
    goto loc_002F5361;
loc_002F53BA:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_stack_pC8)));
    a1 = (unsigned int)((a1) - (*(unsigned int *)(v_stack_pD8)));
    v_r10 = ((unsigned int)(*(unsigned int *)(v_stack_pD8 + 8))) + (v_stack_pC8);
    if (a3 > (*(unsigned __int16 *)(v_rbx + 1 * 2 + 4))) goto loc_002F53FF;
    if ((((unsigned __int8)(v_r10)) & (3)) != 0) goto loc_002F517D;
    result = v_r10;
    if (v_r10 >= v_rbx) { result = v_rbx; }
loc_002F53FF:
    if (a1 < ((unsigned int)(*(unsigned __int8 *)(v_r10 + 1)))) goto loc_002F5263;
    result = (unsigned int)((*(unsigned __int8 *)(v_r10)) >> (3));
    if ((((unsigned __int8)((unsigned int)(a1))) & ((unsigned __int8)(result))) == 0) goto loc_002F5263;
    result = *(unsigned __int8 *)(v_r10 + 2) + 1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r10 + 2))) & (1)) == 0) { result = (unsigned int)(*(unsigned __int8 *)(v_r10 + 2)); }
    *(unsigned __int64 *)(a7) = v_r10 + result + 2 + 2 * 2;
    result = ((unsigned int)(*(unsigned int *)(v_r10 + (unsigned int)((unsigned int)(result)) * 2 + 4))) + (v_stack_pC8);
    v_stack_p68 = result;
    goto loc_002F5263;
loc_002F5455:
    if (0 == 0) goto loc_002F520A;
    goto loc_002F5518;
loc_002F5462:
    if (((unsigned __int8)(*(unsigned __int8 *)(a3))) == 72) goto loc_002F57D2;
loc_002F5474:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3))) & (254));
    if (((unsigned __int8)(result)) == 72) goto loc_002F5730;
loc_002F5481:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3))) & (248));
    if (((unsigned __int8)(result)) == 88) goto loc_002F59A7;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3))) & (240));
    if (((unsigned __int8)(result)) == 64) goto loc_002F56E8;
loc_002F54A3:
    if (((unsigned __int8)(*(unsigned __int8 *)(a3))) == 242) {
        a3 = a3 + 1;
        a1 = *(unsigned __int8 *)(a3 + 1);
    }
    if (((unsigned __int8)(a1 + 62)) <= 1) goto loc_002F5554;
    if (((unsigned __int8)(a1)) == 243) goto loc_002F5A55;
loc_002F54C2:
    if ((((unsigned __int8)(a1 + 23)) & (253)) == 0) goto loc_002F5948;
    if (((unsigned __int8)(a1)) == 255) goto loc_002F59AF;
loc_002F54D6:
    a1 = (unsigned __int8)((a1) & (248));
    if (((unsigned __int8)(a1)) == 72) goto loc_002F56FE;
loc_002F54E2:
loc_002F54EC:
    if (0 != 0) goto loc_002F555D;
    goto loc_002F5214;
loc_002F54FD:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pC8 + 4))) - ((unsigned int)(a3 + 1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - (a1));
    v_rdi = (((unsigned int)(result)) < ((unsigned int)(a3 + 1))) ? 1 : 0;
    goto loc_002F5351;
loc_002F5513:
loc_002F5518:
    v_r11 = (unsigned int)((v_r11) - (a1));
    v_stack_p28 = a10;
    v_stack_p20 = a5;
    result = RtlpUnwindEpilogue(v_stack_pC8, a3, (unsigned int)((unsigned int)(v_r11)), v_stack_pC8);
loc_002F553B:
    if (a6 == 0) goto loc_002F5263;
    *(unsigned __int8 *)(a6) = 0;
    goto loc_002F5263;
loc_002F5554:
    v_stack_p44 = 1;
loc_002F555D:
    v_stack_p70 = a5 + 120;
    v_stack_p50 = a3;
    result = (unsigned __int8)((*(unsigned __int8 *)(a3)) & (248));
    if (((unsigned __int8)(result)) == 72) goto loc_002F58D5;
loc_002F557B:
loc_002F558D:
    v_stack_p40 = (unsigned __int8)(*(unsigned __int8 *)(a3));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a3))) & (248));
    if (((unsigned __int8)(result)) != 88) goto loc_002F5811;
    v_stack_p60 = *(unsigned __int64 *)(a5 + 152);
    if (a3 > (*(unsigned __int16 *)(v_rbx + 1 * 2 + 4))) goto loc_002F55D9;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_pC8, a3, *(unsigned __int8 *)(a3), a10);
    }
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= v_r11) { result = v_r11; }
loc_002F55D9:
    goto loc_002F55E0;
loc_002F55E0:
    if (*(unsigned __int64 *)(a10) != 0) goto loc_002F59BF;
loc_002F55EC:
    a3 = (unsigned int)((*(unsigned __int8 *)(a3)) & (7));
    *(unsigned __int64 *)(a5 + 120 + a3 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    if (*(unsigned __int64 *)(a10 + 16) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a10 + 16) + a3 * 8 + 128) = *(unsigned __int64 *)(a5 + 152);
    }
    a2 = (a3) + 1;
    v_stack_p50 = a2;
    goto loc_002F558D;
loc_002F561D:
    v_stack_p68 = a5 + 152;
    v_stack_p60 = *(unsigned __int64 *)(a5 + 152);
    if (a3 > (*(unsigned __int16 *)(v_rbx + 1 * 2 + 4))) goto loc_002F5663;
    result = *(unsigned __int64 *)(a10 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_pC8, a5 + 152, a3, a10);
    }
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= v_stack_pC8) { result = v_stack_pC8; }
loc_002F5663:
    goto loc_002F566A;
loc_002F566A:
    if (*(unsigned __int64 *)(a10) != 0) goto loc_002F57EF;
loc_002F567E:
    if (a3 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152)))) goto loc_002F5B8F;
    *(unsigned __int64 *)(a5 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    result = RtlpVirtualPopShadowStack(a5, 1, 1, a10);
    *(unsigned __int64 *)(a8) = *(unsigned __int64 *)(a5 + 152);
    if (a6 != 0) {
        *(unsigned __int8 *)(a6) = 0;
    }
    v_rdi = 0;
    *(unsigned __int64 *)(a7) = 0;
    if (a9 == 0) goto loc_002F5280;
    *(unsigned __int64 *)(a9) = 0;
    result = 0;
    goto loc_002F5292;
loc_002F56E8:
    result = (unsigned __int8)((*(unsigned __int8 *)(1)) & (248));
    if (((unsigned __int8)(result)) != 88) goto loc_002F54A3;
    a3 = (1) + (2);
    goto loc_002F5481;
loc_002F56FE:
    if ((*(unsigned __int8 *)(a3 + 1)) != 255) goto loc_002F54E2;
    result = (unsigned __int8)((*(unsigned __int8 *)(a3 + 2)) & (56));
    if (((unsigned __int8)(result)) != 32) goto loc_002F54EC;
    v_stack_p44 = 1;
    goto loc_002F54EC;
loc_002F5730:
    if ((*(unsigned __int8 *)(a3 + 1)) != 141) goto loc_002F5481;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a5))) & (1));
    v_r15 = (unsigned int)((v_r15) << (3));
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3 + 2)))) & (7));
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    if (condition_is_equal) goto loc_002F5481;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152) + 3)) & (15));
    if (((unsigned int)(v_r15)) != ((unsigned int)(result))) goto loc_002F5481;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a3 + 2)) & (248));
    if (((unsigned __int8)(a2)) == 96) goto loc_002F5BE2;
    if (((unsigned __int8)(a2)) != 160) goto loc_002F5481;
    goto loc_002F5BD9;
loc_002F5781:
    if (v_stack_p58 == 0) goto loc_002F5280;
    a1 = (*(unsigned __int64 *)(a5 + 152)) - (8);
    *(unsigned __int64 *)(a8) = a1;
    goto loc_002F5280;
loc_002F57A7:
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 12))) + (*(unsigned __int64 *)(a5 + 152));
    if (a3 > v_r11) goto loc_002F51B1;
    if ((((unsigned __int8)(a1)) & (3)) != 0) goto loc_002F517D;
    if (a1 >= a3) { a1 = a3; }
    goto loc_002F51B1;
loc_002F57D2:
    if ((*(unsigned __int8 *)(a3 + 1)) != 131) goto loc_002F5C47;
    if ((*(unsigned __int8 *)(a3 + 2)) != 196) goto loc_002F5C47;
    goto loc_002F5481;
loc_002F57EF:
    if ((*(unsigned __int64 *)(a5 + 152)) < (*(unsigned __int64 *)(*(unsigned __int8 *)(a1)))) goto loc_002F528D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) - (8);
    if ((*(unsigned __int64 *)(a5 + 152)) > a1) goto loc_002F528D;
    goto loc_002F567E;
loc_002F5811:
    result = (unsigned __int8)(((unsigned __int8)(a3 + 4)) & (240));
    if (((unsigned __int8)(result)) != 64) goto loc_002F59E6;
    v_stack_p48 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 1));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))) & (248));
    if (((unsigned __int8)(result)) != 88) goto loc_002F59E6;
    v_stack_p60 = *(unsigned __int64 *)(a5 + 152);
    if (a3 > (*(unsigned __int16 *)(v_rbx + 1 * 2 + 4))) goto loc_002F586C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3 + 4, a10);
    }
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= v_r15) { result = v_r15; }
loc_002F586C:
    goto loc_002F5873;
loc_002F5873:
    if (*(unsigned __int64 *)(a10) == 0) goto loc_002F5898;
    if ((*(unsigned __int64 *)(a5 + 152)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a10)))) goto loc_002F528D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a10 + 8))) - (8);
    if ((*(unsigned __int64 *)(a5 + 152)) > a1) goto loc_002F5BEB;
loc_002F5898:
    a3 = (unsigned int)((a3 + 4) & (1));
    a3 = (a3) << (3);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(a2 + 1)) & (7));
    a3 = (a3) | (v_r10);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + a3 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    if (*(unsigned __int64 *)(a10 + 16) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a10 + 16) + a3 * 8 + 128) = *(unsigned __int64 *)(a5 + 152);
    }
    a2 = (a2) + (2);
    v_stack_p50 = a2;
    goto loc_002F558D;
loc_002F58D5:
    if (((unsigned __int8)(*(unsigned __int8 *)(a3 + 1))) == 131) goto loc_002F5B1F;
    if (((unsigned __int8)(*(unsigned __int8 *)(a3 + 1))) == 129) goto loc_002F5B99;
    if (((unsigned __int8)(*(unsigned __int8 *)(a3 + 1))) != 141) goto loc_002F557B;
    result = (unsigned __int8)((*(unsigned __int8 *)(a3 + 2)) & (248));
    if (((unsigned __int8)(result)) == 96) goto loc_002F5BF5;
    if (((unsigned __int8)(result)) != 160) goto loc_002F557B;
    a2 = (unsigned int)((*(unsigned __int8 *)(a3 + 6)) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(a3 + 5))));
    a2 = (unsigned int)((a2) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(a3 + 4))));
    a2 = (unsigned int)((a2) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(*(unsigned __int8 *)(a3 + 3))));
    result = ((int)((unsigned int)(a2))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(v_r15)) * 8));
    *(unsigned __int64 *)(a5 + 152) = result;
    v_stack_p50 = a3 + 7;
    goto loc_002F557B;
loc_002F5948:
    v_r14 = (a3) - (v_r10);
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(v_r15)) * 8))) != 235) goto loc_002F5A92;
    result = (unsigned int)(((__int8)(*(unsigned __int8 *)(a3 + 1))) + (2));
loc_002F595F:
    v_r14 = (v_r14) + (result);
    if (v_r14 < ((unsigned int)(*(unsigned int *)(a10)))) goto loc_002F5B39;
    if (v_r14 >= ((unsigned int)(*(unsigned int *)(a10 + 4)))) goto loc_002F5B39;
    if (v_r14 != ((unsigned int)(*(unsigned int *)(a10)))) goto loc_002F54E2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152))) & (32)) != 0) goto loc_002F54EC;
    v_stack_p44 = 1;
    goto loc_002F54EC;
loc_002F59A7:
    goto loc_002F5481;
loc_002F59AF:
    if ((*(unsigned __int8 *)(a3 + 7 + 1)) != 37) goto loc_002F54D6;
    goto loc_002F5554;
loc_002F59BF:
    if (v_r10 < (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a10 + 4))))) goto loc_002F528D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a10 + 8))) - (8);
    if (v_r10 <= a1) goto loc_002F55EC;
    goto loc_002F5292;
loc_002F59E6:
    if (a3 > v_r14) goto loc_002F5A11;
    result = *(unsigned __int64 *)(a5 + 152);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a3 + 7, a3 + 7, a10);
    }
    if (result >= (*(unsigned __int64 *)(a5 + 152))) { result = *(unsigned __int64 *)(a5 + 152); }
loc_002F5A11:
    goto loc_002F5A18;
loc_002F5A18:
    if (*(unsigned __int64 *)(a10) != 0) goto loc_002F5A65;
loc_002F5A20:
    a2 = (v_stack_p78) + (152);
loc_002F5A2C:
    *(unsigned __int64 *)(a5 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2));
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(a2) + 8;
    result = RtlpVirtualPopShadowStack(a5, 1, 1, a10);
    goto loc_002F553B;
loc_002F5A55:
    if ((*(unsigned __int8 *)(1 + 1)) != 195) goto loc_002F54C2;
    goto loc_002F5554;
loc_002F5A65:
    if ((*(unsigned __int64 *)(a5 + 152)) < (*(unsigned __int64 *)(result))) goto loc_002F528D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a10 + 8))) - (8);
    if ((*(unsigned __int64 *)(a5 + 152)) <= a1) goto loc_002F5A2C;
    goto loc_002F5292;
loc_002F5A92:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a5 + 152) + 1))) + (5));
    goto loc_002F595F;
loc_002F5A9E:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152))) & (32)) != 0) goto loc_002F52D2;
    v_stack_p60 = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152) + 2)) <= 1) goto loc_002F5B02;
loc_002F5AB4:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a5 + 152) + 1 * 2 + 4))) >> (8));
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 3) goto loc_002F5AE4;
    result = RtlpUnwindOpSlots(*(unsigned __int16 *)(*(unsigned __int64 *)(a5 + 152) + 1 * 2 + 4), a5 + 152, 1, a10);
    a3 = (unsigned int)(((unsigned int)(v_stack_p60)) + ((unsigned int)(result)));
    v_stack_p60 = (unsigned int)(a3);
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152) + 2)))) goto loc_002F5AB4;
loc_002F5AE4:
loc_002F5B02:
    if (((unsigned int)((unsigned int)(v_stack_p50))) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(a3)) * 2 + 4)))) goto loc_002F51E5;
    v_stack_p58 = 1;
    goto loc_002F51E5;
loc_002F5B1F:
    v_stack_p50 = a3 + 4;
    goto loc_002F557B;
loc_002F5B39:
    result = (__int8)(*(unsigned __int8 *)(a3 + 3));
    if (a3 <= (*(unsigned __int64 *)(a5 + 152))) {
        result = v_r14 + v_stack_pC8 * 1;
        if (result >= (*(unsigned __int64 *)(a5 + 152))) { result = *(unsigned __int64 *)(a5 + 152); }
        result = *(unsigned __int8 *)(result);
        a4 = v_stack_pD8;
    }
    result = RtlpSameFunction(a4, v_stack_pC8, v_r14 + v_stack_pC8 * 1, a4);
    if (result == 0) goto loc_002F5554;
    if (v_r14 == ((unsigned int)(*(unsigned int *)(result)))) goto loc_002F5554;
    goto loc_002F54EC;
loc_002F5B8F:
    goto loc_002F5292;
loc_002F5B99:
    a1 = (unsigned int)((*(unsigned __int8 *)(a3 + 6)) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int8 *)(a3 + 5))));
    a1 = (unsigned int)((a1) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int8 *)(a3 + 4))));
    a1 = (unsigned int)((a1) << (8));
    result = (unsigned int)((*(unsigned __int8 *)(a3 + 3)) | (a1));
    v_stack_p50 = a3 + 7;
    goto loc_002F557B;
loc_002F5BCF:
    if ((*(unsigned __int8 *)(a3 + 2)) != 196) goto loc_002F5474;
loc_002F5BD9:
    goto loc_002F5481;
loc_002F5BE2:
    goto loc_002F5481;
loc_002F5BEB:
    goto loc_002F5292;
loc_002F5BF5:
    *(unsigned __int64 *)(a5 + 152) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(v_r15)) * 8);
    result = ((__int8)(*(unsigned __int8 *)(a3 + 3))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(v_r15)) * 8));
    *(unsigned __int64 *)(a5 + 152) = result;
    v_stack_p50 = a3 + 4;
    goto loc_002F557B;
loc_002F5C47:
    if (((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152) + (unsigned int)((unsigned int)(v_r15)) * 8))) != 72) goto loc_002F5474;
    if ((*(unsigned __int8 *)(a3 + 1)) != 129) goto loc_002F5474;
    goto loc_002F5BCF;
loc_002F5D0E:
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= (a3 + 4)) { result = a3 + 4; }
    goto loc_002F518D;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpxVirtualUnwind(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, void *Arg7, void *Arg8, int64_t Arg9, void *Arg10)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint32_t v_stack_m60;
    uint32_t v_stack_m74;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p108;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint8_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    v_stack_m40 = Arg5;
    if (Arg4 == 0) goto loc_002F561D;
    local_rdi = 0;
    v_stack_m50 = 0;
    v_stack_m74 = 0;
    local_rbx = ((uint32_t)(*(uint32_t *)(Arg4 + 0x8))) + (Arg2);
    if (Arg3 > local_r11) goto loc_002F5183;
    if ((((uint8_t)(local_rbx)) & (3)) == 0) goto loc_002F5D0E;
loc_002F517D:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_002F5183:
loc_002F518D:
    local_r14 = (uint32_t)((*(uint8_t *)(local_rbx)) & (7));
    if (Arg6 != 0) goto loc_002F52A6;
loc_002F51A6:
    if (((uint32_t)(local_r14)) >= 2) goto loc_002F51D2;
loc_002F51B1:
    if ((*(uint8_t *)(local_rbx + 0x2)) != 0) goto loc_002F5284;
    if (((*(uint8_t *)(local_rbx)) & (32)) != 0) goto loc_002F52F3;
loc_002F51CA:
loc_002F51D2:
    v_stack_m60 = 0;
    if (((*(uint8_t *)(local_rbx + 0x3)) & (15)) != 0) goto loc_002F52BA;
loc_002F51E5:
    if (v_stack_m60 != 0) goto loc_002F52DA;
loc_002F51F6:
    *(uint64_t *)(arg8) = *(uint64_t *)(arg5 + 0x98);
    if (1 == 0) goto loc_002F5309;
loc_002F520A:
loc_002F5214:
    v_stack_m80 = Arg10;
    v_stack_m88 = v_stack_p20;
    v_stack_m90 = Arg6;
    v_stack_m98 = Arg5;
    result = RtlpUnwindPrologue(Arg2, Arg3, *(uint64_t *)(arg8), v_stack_p20);
    if (sign_flag) goto loc_002F5292;
    if ((uint32_t)((uint32_t)(Arg1)) != 0) goto loc_002F53BA;
loc_002F5263:
    if (Arg9 != 0) {
        result = v_stack_m50;
        *(uint64_t *)(Arg9) = result;
    }
    if (0 != 0) goto loc_002F5781;
loc_002F5280:
    result = 0;
    goto loc_002F5292;
loc_002F5284:
    if (!sign_flag) goto loc_002F51CA;
loc_002F528D:
loc_002F5292:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)(0xC0000028ULL);
loc_002F52A6:
    if ((*(uint8_t *)((uint32_t)(0xC0000028ULL))) != 0) goto loc_002F51A6;
    goto loc_002F51D2;
loc_002F52BA:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(Arg2)));
    Arg2 = (uint32_t)((Arg2) - (*(uint32_t *)(v_stack_p20)));
    v_stack_p50 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) < ((uint32_t)(*(uint8_t *)(local_rbx + 0x1)))) goto loc_002F5A9E;
loc_002F52D2:
    v_stack_p58 = 1;
loc_002F52DA:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + 0x3)))) & (15));
    result = (uint32_t)((*(uint8_t *)(local_rbx + 0x3)) & (0xFFFFFFF0ULL));
    Arg1 = (*(uint64_t *)(arg5 + Arg1 * 8 + 0x78)) - (result);
    goto loc_002F51F6;
loc_002F52F3:
    Arg2 = (uint32_t)((Arg2) + 1);
    if (((uint32_t)(Arg2)) <= 32) goto loc_002F57A7;
    result = RtlRaiseStatus((uint32_t)(0xC00000FFULL), Arg2, *(uint64_t *)(arg8), v_stack_p20);
loc_002F5309:
    if (((uint32_t)(local_r14)) < 2) goto loc_002F5462;
    if ((uint8_t)(*(uint8_t *)(local_rbx + 0x2)) == 0) goto loc_002F520A;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rbx + 0x4))) >> (8));
    result = (uint8_t)(((uint8_t)(Arg1)) & (15));
    if (((uint8_t)(result)) != 6) goto loc_002F520A;
    v_stack_p50 = (uint32_t)((uint8_t)(*(uint16_t *)(local_rbx + 0x4)));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(Arg2)));
    if ((((uint8_t)(Arg1)) & (16)) != 0) goto loc_002F54FD;
loc_002F5351:
    if (0 != 0) goto loc_002F5518;
loc_002F5361:
    if (1 >= ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + 0x2)))))) goto loc_002F5455;
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4))) >> (8));
    result = (uint8_t)(((uint8_t)(Arg3)) & (15));
    if (((uint8_t)(result)) != 6) goto loc_002F5455;
    Arg1 = (uint32_t)(((uint8_t)(Arg3)) >> (4));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4)))));
    if (condition_is_equal) goto loc_002F5455;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4))) - (Arg1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - ((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (((uint32_t)(result)) < v_stack_p50) goto loc_002F5513;
    Arg2 = (uint32_t)((1) + 1);
    goto loc_002F5361;
loc_002F53BA:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(v_stack_pC8)));
    Arg1 = (uint32_t)((Arg1) - (*(uint32_t *)(v_stack_pD8)));
    local_r10 = ((uint32_t)(*(uint32_t *)(v_stack_pD8 + 0x8))) + (v_stack_pC8);
    if (Arg3 > (*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4))) goto loc_002F53FF;
    if ((((uint8_t)(local_r10)) & (3)) != 0) goto loc_002F517D;
    result = local_r10;
    if (local_r10 >= local_rbx) { result = local_rbx; }
loc_002F53FF:
    if (Arg1 < ((uint32_t)(*(uint8_t *)(local_r10 + 0x1)))) goto loc_002F5263;
    result = (uint32_t)((*(uint8_t *)(local_r10)) >> (3));
    if ((((uint8_t)((uint32_t)(Arg1))) & ((uint8_t)(result))) == 0) goto loc_002F5263;
    result = *(uint8_t *)(local_r10 + 0x2) + 1;
    if ((((uint8_t)(*(uint8_t *)(local_r10 + 0x2))) & (1)) == 0) { result = (uint32_t)(*(uint8_t *)(local_r10 + 0x2)); }
    *(uint64_t *)(arg7) = local_r10 + result + 2 + 2 * 2;
    result = ((uint32_t)(*(uint32_t *)(local_r10 + (uint32_t)((uint32_t)(result)) * 2 + 0x4))) + (v_stack_pC8);
    v_stack_p68 = result;
    goto loc_002F5263;
loc_002F5455:
    if (0 == 0) goto loc_002F520A;
    goto loc_002F5518;
loc_002F5462:
    if (((uint8_t)(*(uint8_t *)(Arg3))) == 72) goto loc_002F57D2;
loc_002F5474:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3))) & (254));
    if (((uint8_t)(result)) == 72) goto loc_002F5730;
loc_002F5481:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3))) & (248));
    if (((uint8_t)(result)) == 88) goto loc_002F59A7;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3))) & (240));
    if (((uint8_t)(result)) == 64) goto loc_002F56E8;
loc_002F54A3:
    if (((uint8_t)(*(uint8_t *)(Arg3))) == 242) {
        Arg3 = Arg3 + 1;
        Arg1 = *(uint8_t *)(Arg3 + 0x1);
    }
    if (((uint8_t)(Arg1 + 62)) <= 1) goto loc_002F5554;
    if (((uint8_t)(Arg1)) == 243) goto loc_002F5A55;
loc_002F54C2:
    if ((((uint8_t)(Arg1 + 23)) & (253)) == 0) goto loc_002F5948;
    if (((uint8_t)(Arg1)) == 255) goto loc_002F59AF;
loc_002F54D6:
    Arg1 = (uint8_t)((Arg1) & (248));
    if (((uint8_t)(Arg1)) == 72) goto loc_002F56FE;
loc_002F54E2:
loc_002F54EC:
    if (0 != 0) goto loc_002F555D;
    goto loc_002F5214;
loc_002F54FD:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pC8 + 0x4))) - ((uint32_t)(Arg3 + 1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - (Arg1));
    local_rdi = (((uint32_t)(result)) < ((uint32_t)(Arg3 + 1))) ? 1 : 0;
    goto loc_002F5351;
loc_002F5513:
loc_002F5518:
    local_r11 = (uint32_t)((local_r11) - (Arg1));
    v_stack_p28 = Arg10;
    v_stack_p20 = Arg5;
    result = RtlpUnwindEpilogue(v_stack_pC8, Arg3, (uint32_t)((uint32_t)(local_r11)), v_stack_pC8);
loc_002F553B:
    if (Arg6 == 0) goto loc_002F5263;
    *(uint8_t *)(Arg6) = 0;
    goto loc_002F5263;
loc_002F5554:
    v_stack_p44 = 1;
loc_002F555D:
    v_stack_p70 = Arg5 + 120;
    v_stack_p50 = Arg3;
    result = (uint8_t)((*(uint8_t *)(Arg3)) & (248));
    if (((uint8_t)(result)) == 72) goto loc_002F58D5;
loc_002F557B:
loc_002F558D:
    v_stack_p40 = (uint8_t)(*(uint8_t *)(Arg3));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg3))) & (248));
    if (((uint8_t)(result)) != 88) goto loc_002F5811;
    v_stack_p60 = *(uint64_t *)(arg5 + 0x98);
    if (Arg3 > (*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4))) goto loc_002F55D9;
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_pC8, Arg3, *(uint8_t *)(Arg3), Arg10);
    }
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= local_r11) { result = local_r11; }
loc_002F55D9:
    goto loc_002F55E0;
loc_002F55E0:
    if (*(uint64_t *)(arg10) != 0) goto loc_002F59BF;
loc_002F55EC:
    Arg3 = (uint32_t)((*(uint8_t *)(Arg3)) & (7));
    *(uint64_t *)(arg5 + 0x78 + Arg3 * 8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    if (*(uint64_t *)(arg10 + 0x10) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg10 + 0x10) + Arg3 * 8 + 0x80) = *(uint64_t *)(arg5 + 0x98);
    }
    Arg2 = (Arg3) + 1;
    v_stack_p50 = Arg2;
    goto loc_002F558D;
loc_002F561D:
    v_stack_p68 = Arg5 + 152;
    v_stack_p60 = *(uint64_t *)(arg5 + 0x98);
    if (Arg3 > (*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4))) goto loc_002F5663;
    result = *(uint64_t *)(arg10 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_pC8, Arg5 + 152, Arg3, Arg10);
    }
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= v_stack_pC8) { result = v_stack_pC8; }
loc_002F5663:
    goto loc_002F566A;
loc_002F566A:
    if (*(uint64_t *)(arg10) != 0) goto loc_002F57EF;
loc_002F567E:
    if (Arg3 == (*(uint64_t *)(*(uint64_t *)(arg5 + 0x98)))) goto loc_002F5B8F;
    *(uint64_t *)(arg5 + 0xF8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    result = RtlpVirtualPopShadowStack(Arg5, 1, 1, Arg10);
    *(uint64_t *)(arg8) = *(uint64_t *)(arg5 + 0x98);
    if (Arg6 != 0) {
        *(uint8_t *)(Arg6) = 0;
    }
    local_rdi = 0;
    *(uint64_t *)(arg7) = 0;
    if (Arg9 == 0) goto loc_002F5280;
    *(uint64_t *)(Arg9) = 0;
    result = 0;
    goto loc_002F5292;
loc_002F56E8:
    result = (uint8_t)((*(uint8_t *)(1)) & (248));
    if (((uint8_t)(result)) != 88) goto loc_002F54A3;
    Arg3 = (1) + (2);
    goto loc_002F5481;
loc_002F56FE:
    if ((*(uint8_t *)(Arg3 + 0x1)) != 255) goto loc_002F54E2;
    result = (uint8_t)((*(uint8_t *)(Arg3 + 0x2)) & (56));
    if (((uint8_t)(result)) != 32) goto loc_002F54EC;
    v_stack_p44 = 1;
    goto loc_002F54EC;
loc_002F5730:
    if ((*(uint8_t *)(Arg3 + 0x1)) != 141) goto loc_002F5481;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg5))) & (1));
    local_r15 = (uint32_t)((local_r15) << (3));
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg3 + 0x2)))) & (7));
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    if (condition_is_equal) goto loc_002F5481;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg5 + 0x98) + 0x3)) & (15));
    if (((uint32_t)(local_r15)) != ((uint32_t)(result))) goto loc_002F5481;
    Arg2 = (uint8_t)((*(uint8_t *)(Arg3 + 0x2)) & (248));
    if (((uint8_t)(Arg2)) == 96) goto loc_002F5BE2;
    if (((uint8_t)(Arg2)) != 160) goto loc_002F5481;
    goto loc_002F5BD9;
loc_002F5781:
    if (v_stack_p58 == 0) goto loc_002F5280;
    Arg1 = (*(uint64_t *)(arg5 + 0x98)) - (8);
    *(uint64_t *)(arg8) = Arg1;
    goto loc_002F5280;
loc_002F57A7:
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg1 + 0xC))) + (*(uint64_t *)(arg5 + 0x98));
    if (Arg3 > local_r11) goto loc_002F51B1;
    if ((((uint8_t)(Arg1)) & (3)) != 0) goto loc_002F517D;
    if (Arg1 >= Arg3) { Arg1 = Arg3; }
    goto loc_002F51B1;
loc_002F57D2:
    if ((*(uint8_t *)(Arg3 + 0x1)) != 131) goto loc_002F5C47;
    if ((*(uint8_t *)(Arg3 + 0x2)) != 196) goto loc_002F5C47;
    goto loc_002F5481;
loc_002F57EF:
    if ((*(uint64_t *)(arg5 + 0x98)) < (*(uint64_t *)(*(uint8_t *)(Arg1)))) goto loc_002F528D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x8))) - (8);
    if ((*(uint64_t *)(arg5 + 0x98)) > Arg1) goto loc_002F528D;
    goto loc_002F567E;
loc_002F5811:
    result = (uint8_t)(((uint8_t)(Arg3 + 4)) & (240));
    if (((uint8_t)(result)) != 64) goto loc_002F59E6;
    v_stack_p48 = (uint8_t)(*(uint8_t *)(Arg2 + 0x1));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg2 + 0x1))) & (248));
    if (((uint8_t)(result)) != 88) goto loc_002F59E6;
    v_stack_p60 = *(uint64_t *)(arg5 + 0x98);
    if (Arg3 > (*(uint16_t *)(local_rbx + 0x1 * 2 + 0x4))) goto loc_002F586C;
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3 + 4, Arg10);
    }
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= local_r15) { result = local_r15; }
loc_002F586C:
    goto loc_002F5873;
loc_002F5873:
    if (*(uint64_t *)(arg10) == 0) goto loc_002F5898;
    if ((*(uint64_t *)(arg5 + 0x98)) < (*(uint64_t *)(*(uint64_t *)(arg10)))) goto loc_002F528D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg10 + 0x8))) - (8);
    if ((*(uint64_t *)(arg5 + 0x98)) > Arg1) goto loc_002F5BEB;
loc_002F5898:
    Arg3 = (uint32_t)((Arg3 + 4) & (1));
    Arg3 = (Arg3) << (3);
    local_r10 = (uint32_t)((*(uint8_t *)(Arg2 + 0x1)) & (7));
    Arg3 = (Arg3) | (local_r10);
    *(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + Arg3 * 8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    if (*(uint64_t *)(arg10 + 0x10) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg10 + 0x10) + Arg3 * 8 + 0x80) = *(uint64_t *)(arg5 + 0x98);
    }
    Arg2 = (Arg2) + (2);
    v_stack_p50 = Arg2;
    goto loc_002F558D;
loc_002F58D5:
    if (((uint8_t)(*(uint8_t *)(Arg3 + 0x1))) == 131) goto loc_002F5B1F;
    if (((uint8_t)(*(uint8_t *)(Arg3 + 0x1))) == 129) goto loc_002F5B99;
    if (((uint8_t)(*(uint8_t *)(Arg3 + 0x1))) != 141) goto loc_002F557B;
    result = (uint8_t)((*(uint8_t *)(Arg3 + 0x2)) & (248));
    if (((uint8_t)(result)) == 96) goto loc_002F5BF5;
    if (((uint8_t)(result)) != 160) goto loc_002F557B;
    Arg2 = (uint32_t)((*(uint8_t *)(Arg3 + 0x6)) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(Arg3 + 0x5))));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(Arg3 + 0x4))));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(*(uint8_t *)(Arg3 + 0x3))));
    result = ((int32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(local_r15)) * 8));
    *(uint64_t *)(arg5 + 0x98) = result;
    v_stack_p50 = Arg3 + 7;
    goto loc_002F557B;
loc_002F5948:
    local_r14 = (Arg3) - (local_r10);
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(local_r15)) * 8))) != 235) goto loc_002F5A92;
    result = (uint32_t)(((int8_t)(*(uint8_t *)(Arg3 + 0x1))) + (2));
loc_002F595F:
    local_r14 = (local_r14) + (result);
    if (local_r14 < ((uint32_t)(*(uint32_t *)(arg10)))) goto loc_002F5B39;
    if (local_r14 >= ((uint32_t)(*(uint32_t *)(arg10 + 0x4)))) goto loc_002F5B39;
    if (local_r14 != ((uint32_t)(*(uint32_t *)(arg10)))) goto loc_002F54E2;
    if (((*(uint8_t *)(*(uint64_t *)(arg5 + 0x98))) & (32)) != 0) goto loc_002F54EC;
    v_stack_p44 = 1;
    goto loc_002F54EC;
loc_002F59A7:
    goto loc_002F5481;
loc_002F59AF:
    if ((*(uint8_t *)(Arg3 + 0x7 + 0x1)) != 37) goto loc_002F54D6;
    goto loc_002F5554;
loc_002F59BF:
    if (local_r10 < (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg10 + 0x4))))) goto loc_002F528D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg10 + 0x8))) - (8);
    if (local_r10 <= Arg1) goto loc_002F55EC;
    goto loc_002F5292;
loc_002F59E6:
    if (Arg3 > local_r14) goto loc_002F5A11;
    result = *(uint64_t *)(arg5 + 0x98);
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg3 + 7, Arg3 + 7, Arg10);
    }
    if (result >= (*(uint64_t *)(arg5 + 0x98))) { result = *(uint64_t *)(arg5 + 0x98); }
loc_002F5A11:
    goto loc_002F5A18;
loc_002F5A18:
    if (*(uint64_t *)(arg10) != 0) goto loc_002F5A65;
loc_002F5A20:
    Arg2 = (v_stack_p78) + (152);
loc_002F5A2C:
    *(uint64_t *)(arg5 + 0xF8) = *(uint64_t *)(*(uint64_t *)(Arg2));
    *(uint64_t *)(Arg2) = *(uint64_t *)(Arg2) + 8;
    result = RtlpVirtualPopShadowStack(Arg5, 1, 1, Arg10);
    goto loc_002F553B;
loc_002F5A55:
    if ((*(uint8_t *)(1 + 0x1)) != 195) goto loc_002F54C2;
    goto loc_002F5554;
loc_002F5A65:
    if ((*(uint64_t *)(arg5 + 0x98)) < (*(uint64_t *)(result))) goto loc_002F528D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg10 + 0x8))) - (8);
    if ((*(uint64_t *)(arg5 + 0x98)) <= Arg1) goto loc_002F5A2C;
    goto loc_002F5292;
loc_002F5A92:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg5 + 0x98) + 0x1))) + (5));
    goto loc_002F595F;
loc_002F5A9E:
    if (((*(uint8_t *)(*(uint64_t *)(arg5 + 0x98))) & (32)) != 0) goto loc_002F52D2;
    v_stack_p60 = 1;
    if ((*(uint8_t *)(*(uint64_t *)(arg5 + 0x98) + 0x2)) <= 1) goto loc_002F5B02;
loc_002F5AB4:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg5 + 0x98) + 0x1 * 2 + 0x4))) >> (8));
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 3) goto loc_002F5AE4;
    result = RtlpUnwindOpSlots(*(uint16_t *)(*(uint64_t *)(arg5 + 0x98) + 0x1 * 2 + 0x4), Arg5 + 152, 1, Arg10);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p60)) + ((uint32_t)(result)));
    v_stack_p60 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg5 + 0x98) + 0x2)))) goto loc_002F5AB4;
loc_002F5AE4:
loc_002F5B02:
    if (((uint32_t)((uint32_t)(v_stack_p50))) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(Arg3)) * 2 + 0x4)))) goto loc_002F51E5;
    v_stack_p58 = 1;
    goto loc_002F51E5;
loc_002F5B1F:
    v_stack_p50 = Arg3 + 4;
    goto loc_002F557B;
loc_002F5B39:
    result = (int8_t)(*(uint8_t *)(Arg3 + 0x3));
    if (Arg3 <= (*(uint64_t *)(arg5 + 0x98))) {
        result = local_r14 + v_stack_pC8 * 1;
        if (result >= (*(uint64_t *)(arg5 + 0x98))) { result = *(uint64_t *)(arg5 + 0x98); }
        result = *(uint8_t *)(result);
        Arg4 = v_stack_pD8;
    }
    result = RtlpSameFunction(Arg4, v_stack_pC8, local_r14 + v_stack_pC8 * 1, Arg4);
    if (result == 0) goto loc_002F5554;
    if (local_r14 == ((uint32_t)(*(uint32_t *)(result)))) goto loc_002F5554;
    goto loc_002F54EC;
loc_002F5B8F:
    goto loc_002F5292;
loc_002F5B99:
    Arg1 = (uint32_t)((*(uint8_t *)(Arg3 + 0x6)) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint8_t *)(Arg3 + 0x5))));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint8_t *)(Arg3 + 0x4))));
    Arg1 = (uint32_t)((Arg1) << (8));
    result = (uint32_t)((*(uint8_t *)(Arg3 + 0x3)) | (Arg1));
    v_stack_p50 = Arg3 + 7;
    goto loc_002F557B;
loc_002F5BCF:
    if ((*(uint8_t *)(Arg3 + 0x2)) != 196) goto loc_002F5474;
loc_002F5BD9:
    goto loc_002F5481;
loc_002F5BE2:
    goto loc_002F5481;
loc_002F5BEB:
    goto loc_002F5292;
loc_002F5BF5:
    *(uint64_t *)(arg5 + 0x98) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(local_r15)) * 8);
    result = ((int8_t)(*(uint8_t *)(Arg3 + 0x3))) + (*(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(local_r15)) * 8));
    *(uint64_t *)(arg5 + 0x98) = result;
    v_stack_p50 = Arg3 + 4;
    goto loc_002F557B;
loc_002F5C47:
    if (((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg5 + 0x98) + (uint32_t)((uint32_t)(local_r15)) * 8))) != 72) goto loc_002F5474;
    if ((*(uint8_t *)(Arg3 + 0x1)) != 129) goto loc_002F5474;
    goto loc_002F5BCF;
loc_002F5D0E:
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= (Arg3 + 4)) { result = Arg3 + 4; }
    goto loc_002F518D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0 + r8*8` | `64` | `W` |
| `Arg5` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg5` | `+ 0x78` | `64` | `R` |
| `Arg5` | `+ 0x78 + rcx*8` | `64` | `R` |
| `Arg5` | `+ 0x98` | `64` | `R` |
| `Arg5` | `+ 0x98` | `64` | `R/W` |
| `Arg5` | `+ 0x98` | `64` | `W` |
| `Arg5` | `+ 0xF8` | `64` | `W` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |
| `Arg10` | `+ 0x0` | `64` | `R` |
| `Arg10` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F5110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
