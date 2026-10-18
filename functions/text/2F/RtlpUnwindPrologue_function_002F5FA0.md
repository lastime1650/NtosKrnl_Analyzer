# RtlpUnwindPrologue

- RVA: `0x002F5FA0`–`0x002F6A3C` (길이 `2,716` bytes)
- VA: `0x00000001402F5FA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007220C`
- 디코드: `657`개 명령, `2,716/2,716` bytes 표시
- 미해석 바이트: `12` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002F6056` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F6100` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F61E7` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F626B` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F6352` → [RtlRaiseStatus](RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x002F6400` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F6489` → [RtlLocateExtendedFeature2](RtlLocateExtendedFeature2_function_002F82F0.md) (function, `0x002F82F0`)
- `0x002F652D` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F6577` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F6674` → [RtlpIsNoShadowStackUnwindMachineFrameEntry](../48/RtlpIsNoShadowStackUnwindMachineFrameEntry_function_00481958.md) (function, `0x00481958`)
- `0x002F6714` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F67C2` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [RtlpxVirtualUnwind](RtlpxVirtualUnwind_function_002F5110.md) at `0x002F5251`

### Static image references
- `0x002F6004` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x002F6056` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F6100` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F61E7` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F626B` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F6400` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F652D` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F6577` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F6714` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002F67C2` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F5FA0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002F5FA5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
002F5FAA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002F5FAF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002F5FB4  53                              push rbx
002F5FB5  56                              push rsi
002F5FB6  57                              push rdi
002F5FB7  41 54                           push r12
002F5FB9  41 55                           push r13
002F5FBB  41 56                           push r14
002F5FBD  41 57                           push r15
002F5FBF  48 83 EC 70                     sub rsp, 0x70
002F5FC3  4C 8B E2                        mov r12, rdx
002F5FC6  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F5FCE  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
002F5FD3  45 33 D2                        xor r10d, r10d
002F5FD6  44 89 54 24 40                  mov dword ptr [rsp + 0x40], r10d
002F5FDB  48 8D 86 A0 01 00 00            lea rax, [rsi + 0x1a0]
002F5FE2  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002F5FE7  48 8D 46 78                     lea rax, [rsi + 0x78]
002F5FEB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002F5FF0  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F5FFA  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F6004  48 8D 1D F5 9F D0 FF            lea rbx, [rip - 0x2f600b]
002F600B  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F6013  41 8B FA                        mov edi, r10d
002F6016  44 89 54 24 24                  mov dword ptr [rsp + 0x24], r10d
002F601B  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
002F6020  41 8B CC                        mov ecx, r12d
002F6023  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002F602B  2B 0A                           sub ecx, dword ptr [rdx]
002F602D  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
002F6035  2B C8                           sub ecx, eax
002F6037  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
002F603B  44 8B 5A 08                     mov r11d, dword ptr [rdx + 8]
002F603F  4C 03 D8                        add r11, rax
002F6042  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
002F6047  4D 3B E5                        cmp r12, r13
002F604A  77 14                           ja 0x1402f6060
002F604C  41 F6 C3 03                     test r11b, 3
002F6050  0F 84 22 09 00 00               je 0x1402f6978
002F6056  E8 75 3F 5A 00                  call 0x140899fd0
002F605B  CC                              int3
002F605C  0F 1F 40 00                     nop dword ptr [rax]
002F6060  41 0F B6 4B 02                  movzx ecx, byte ptr [r11 + 2]
002F6065  3B F9                           cmp edi, ecx
002F6067  73 72                           jae 0x1402f60db
002F6069  8B C7                           mov eax, edi
002F606B  45 0F B6 4C 43 05               movzx r9d, byte ptr [r11 + rax*2 + 5]
002F6071  41 8B C9                        mov ecx, r9d
002F6074  83 E1 0F                        and ecx, 0xf
002F6077  41 C1 E9 04                     shr r9d, 4
002F607B  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
002F6080  49 8D 14 43                     lea rdx, [r11 + rax*2]
002F6084  0F B6 42 04                     movzx eax, byte ptr [rdx + 4]
002F6088  39 44 24 50                     cmp dword ptr [rsp + 0x50], eax
002F608C  0F 82 14 06 00 00               jb 0x1402f66a6
002F6092  85 C9                           test ecx, ecx
002F6094  0F 84 2E 01 00 00               je 0x1402f61c8
002F609A  83 F9 04                        cmp ecx, 4
002F609D  0F 84 A1 01 00 00               je 0x1402f6244
002F60A3  83 F9 02                        cmp ecx, 2
002F60A6  0F 84 38 02 00 00               je 0x1402f62e4
002F60AC  FF C9                           dec ecx
002F60AE  83 F9 09                        cmp ecx, 9
002F60B1  0F 87 96 02 00 00               ja 0x1402f634d
002F60B7  8B 8C 8B 14 6A 2F 00            mov ecx, dword ptr [rbx + rcx*4 + 0x2f6a14]
002F60BE  48 03 CB                        add rcx, rbx
002F60C1  FF E1                           jmp rcx
002F60C3  CC                              int3
002F60C4  CC                              int3
002F60C5  CC                              int3
002F60C6  CC                              int3
002F60C7  FF C7                           inc edi
002F60C9  FF C7                           inc edi
002F60CB  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F60CF  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F60D9  EB 85                           jmp 0x1402f6060
002F60DB  41 F6 03 20                     test byte ptr [r11], 0x20
002F60DF  0F 85 23 02 00 00               jne 0x1402f6308
002F60E5  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
002F60EA  0F 85 68 02 00 00               jne 0x1402f6358
002F60F0  4D 3B E5                        cmp r12, r13
002F60F3  77 1C                           ja 0x1402f6111
002F60F5  48 8B 86 98 00 00 00            mov rax, qword ptr [rsi + 0x98]
002F60FC  A8 03                           test al, 3
002F60FE  74 06                           je 0x1402f6106
002F6100  E8 CB 3E 5A 00                  call 0x140899fd0
002F6105  CC                              int3
002F6106  49 3B C6                        cmp rax, r14
002F6109  49 0F 43 C6                     cmovae rax, r14
002F610D  90                              nop
002F610E  0F B6 00                        movzx eax, byte ptr [rax]
002F6111  EB 05                           jmp 0x1402f6118
002F6113  E9 00 07 00 00                  jmp 0x1402f6818
002F6118  49 8B 07                        mov rax, qword ptr [r15]
002F611B  48 85 C0                        test rax, rax
002F611E  0F 84 04 07 00 00               je 0x1402f6828
002F6124  4C 8D 86 98 00 00 00            lea r8, [rsi + 0x98]
002F612B  49 8B 10                        mov rdx, qword ptr [r8]
002F612E  48 3B 10                        cmp rdx, qword ptr [rax]
002F6131  0F 82 CB 06 00 00               jb 0x1402f6802
002F6137  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F613B  48 8B 08                        mov rcx, qword ptr [rax]
002F613E  48 83 E9 08                     sub rcx, 8
002F6142  48 3B D1                        cmp rdx, rcx
002F6145  0F 87 5F 03 00 00               ja 0x1402f64aa
002F614B  49 8B 08                        mov rcx, qword ptr [r8]
002F614E  48 8B 01                        mov rax, qword ptr [rcx]
002F6151  48 89 86 F8 00 00 00            mov qword ptr [rsi + 0xf8], rax
002F6158  48 8D 41 08                     lea rax, [rcx + 8]
002F615C  49 89 00                        mov qword ptr [r8], rax
002F615F  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002F6162  25 40 00 10 00                  and eax, 0x100040
002F6167  3D 40 00 10 00                  cmp eax, 0x100040
002F616C  0F 84 FF 02 00 00               je 0x1402f6471
002F6172  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002F6175  25 80 00 10 00                  and eax, 0x100080
002F617A  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002F6182  3D 80 00 10 00                  cmp eax, 0x100080
002F6187  75 10                           jne 0x1402f6199
002F6189  48 63 86 E8 04 00 00            movsxd rax, dword ptr [rsi + 0x4e8]
002F6190  48 83 84 30 D0 04 00 00 08      add qword ptr [rax + rsi + 0x4d0], 8
002F6199  48 85 C9                        test rcx, rcx
002F619C  0F 85 EB 01 00 00               jne 0x1402f638d
002F61A2  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
002F61AA  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
002F61B2  48 89 01                        mov qword ptr [rcx], rax
002F61B5  33 C0                           xor eax, eax
002F61B7  48 83 C4 70                     add rsp, 0x70
002F61BB  41 5F                           pop r15
002F61BD  41 5E                           pop r14
002F61BF  41 5D                           pop r13
002F61C1  41 5C                           pop r12
002F61C3  5F                              pop rdi
002F61C4  5E                              pop rsi
002F61C5  5B                              pop rbx
002F61C6  C3                              ret
002F61C7  CC                              int3
002F61C8  48 8D 96 98 00 00 00            lea rdx, [rsi + 0x98]
002F61CF  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
002F61D4  4C 8B 02                        mov r8, qword ptr [rdx]
002F61D7  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
002F61DC  4D 3B E5                        cmp r12, r13
002F61DF  77 1A                           ja 0x1402f61fb
002F61E1  41 F6 C0 03                     test r8b, 3
002F61E5  74 06                           je 0x1402f61ed
002F61E7  E8 E4 3D 5A 00                  call 0x140899fd0
002F61EC  CC                              int3
002F61ED  49 8B C0                        mov rax, r8
002F61F0  4D 3B C6                        cmp r8, r14
002F61F3  49 0F 43 C6                     cmovae rax, r14
002F61F7  90                              nop
002F61F8  0F B6 00                        movzx eax, byte ptr [rax]
002F61FB  EB 05                           jmp 0x1402f6202
002F61FD  E9 D9 06 00 00                  jmp 0x1402f68db
002F6202  49 8B 07                        mov rax, qword ptr [r15]
002F6205  48 85 C0                        test rax, rax
002F6208  0F 85 B2 02 00 00               jne 0x1402f64c0
002F620E  49 8B 08                        mov rcx, qword ptr [r8]
002F6211  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002F6216  4A 89 0C C8                     mov qword ptr [rax + r9*8], rcx
002F621A  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
002F621E  48 85 C0                        test rax, rax
002F6221  74 08                           je 0x1402f622b
002F6223  4E 89 84 C8 80 00 00 00         mov qword ptr [rax + r9*8 + 0x80], r8
002F622B  48 83 02 08                     add qword ptr [rdx], 8
002F622F  FF C7                           inc edi
002F6231  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F6235  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F623F  E9 1C FE FF FF                  jmp 0x1402f6060
002F6244  FF C7                           inc edi
002F6246  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F624A  41 0F B7 4C 7B 04               movzx ecx, word ptr [r11 + rdi*2 + 4]
002F6250  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
002F6258  48 8D 14 C8                     lea rdx, [rax + rcx*8]
002F625C  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
002F6261  4D 3B E5                        cmp r12, r13
002F6264  77 19                           ja 0x1402f627f
002F6266  F6 C2 03                        test dl, 3
002F6269  74 06                           je 0x1402f6271
002F626B  E8 60 3D 5A 00                  call 0x140899fd0
002F6270  CC                              int3
002F6271  48 8B C2                        mov rax, rdx
002F6274  49 3B D6                        cmp rdx, r14
002F6277  49 0F 43 C6                     cmovae rax, r14
002F627B  90                              nop
002F627C  0F B6 00                        movzx eax, byte ptr [rax]
002F627F  EB 05                           jmp 0x1402f6286
002F6281  E9 A6 06 00 00                  jmp 0x1402f692c
002F6286  49 8B 07                        mov rax, qword ptr [r15]
002F6289  48 85 C0                        test rax, rax
002F628C  74 1D                           je 0x1402f62ab
002F628E  48 3B 10                        cmp rdx, qword ptr [rax]
002F6291  0F 82 6B 05 00 00               jb 0x1402f6802
002F6297  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F629B  48 8B 08                        mov rcx, qword ptr [rax]
002F629E  48 83 E9 08                     sub rcx, 8
002F62A2  48 3B D1                        cmp rdx, rcx
002F62A5  0F 87 5D 07 00 00               ja 0x1402f6a08
002F62AB  45 8B C1                        mov r8d, r9d
002F62AE  48 8B 0A                        mov rcx, qword ptr [rdx]
002F62B1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002F62B6  4A 89 0C C0                     mov qword ptr [rax + r8*8], rcx
002F62BA  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
002F62BE  48 85 C0                        test rax, rax
002F62C1  0F 84 68 FF FF FF               je 0x1402f622f
002F62C7  4A 89 94 C0 80 00 00 00         mov qword ptr [rax + r8*8 + 0x80], rdx
002F62CF  FF C7                           inc edi
002F62D1  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F62D5  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F62DF  E9 7C FD FF FF                  jmp 0x1402f6060
002F62E4  42 8D 0C CD 08 00 00 00         lea ecx, [r9*8 + 8]
002F62EC  48 01 8E 98 00 00 00            add qword ptr [rsi + 0x98], rcx
002F62F3  FF C7                           inc edi
002F62F5  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F62F9  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F6303  E9 58 FD FF FF                  jmp 0x1402f6060
002F6308  F6 C1 01                        test cl, 1
002F630B  74 02                           je 0x1402f630f
002F630D  FF C1                           inc ecx
002F630F  8B D1                           mov edx, ecx
002F6311  48 83 C2 02                     add rdx, 2
002F6315  49 8D 14 53                     lea rdx, [r11 + rdx*2]
002F6319  48 89 94 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdx
002F6321  4D 3B E5                        cmp r12, r13
002F6324  77 14                           ja 0x1402f633a
002F6326  F6 C2 03                        test dl, 3
002F6329  0F 85 27 FD FF FF               jne 0x1402f6056
002F632F  49 3B D6                        cmp rdx, r14
002F6332  49 0F 43 D6                     cmovae rdx, r14
002F6336  90                              nop
002F6337  0F B6 02                        movzx eax, byte ptr [rdx]
002F633A  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002F633E  FF C0                           inc eax
002F6340  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002F6344  83 F8 20                        cmp eax, 0x20
002F6347  0F 86 C6 FC FF FF               jbe 0x1402f6013
002F634D  B9 FF 00 00 C0                  mov ecx, 0xc00000ff
002F6352  E8 F9 06 00 00                  call 0x1402f6a50
002F6357  CC                              int3
002F6358  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002F6360  48 85 C9                        test rcx, rcx
002F6363  0F 84 39 FE FF FF               je 0x1402f61a2
002F6369  0F 1F 80 00 00 00 00            nop dword ptr [rax]
002F6370  41 83 FA 04                     cmp r10d, 4
002F6374  0F 83 1F FE FF FF               jae 0x1402f6199
002F637A  4E 3B 9C D3 A8 1E E0 00         cmp r11, qword ptr [rbx + r10*8 + 0xe01ea8]
002F6382  0F 84 3A 02 00 00               je 0x1402f65c2
002F6388  41 FF C2                        inc r10d
002F638B  EB E3                           jmp 0x1402f6370
002F638D  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
002F6392  88 01                           mov byte ptr [rcx], al
002F6394  E9 09 FE FF FF                  jmp 0x1402f61a2
002F6399  41 0F B6 4B 03                  movzx ecx, byte ptr [r11 + 3]
002F639E  83 E1 0F                        and ecx, 0xf
002F63A1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002F63A6  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002F63AA  48 89 96 98 00 00 00            mov qword ptr [rsi + 0x98], rdx
002F63B1  41 0F B6 43 03                  movzx eax, byte ptr [r11 + 3]
002F63B6  83 E0 F0                        and eax, 0xfffffff0
002F63B9  48 2B D0                        sub rdx, rax
002F63BC  48 89 96 98 00 00 00            mov qword ptr [rsi + 0x98], rdx
002F63C3  FF C7                           inc edi
002F63C5  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F63C9  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F63D3  E9 88 FC FF FF                  jmp 0x1402f6060
002F63D8  FF C7                           inc edi
002F63DA  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F63DE  45 0F B7 74 7B 04               movzx r14d, word ptr [r11 + rdi*2 + 4]
002F63E4  49 C1 E6 04                     shl r14, 4
002F63E8  4C 03 B4 24 C0 00 00 00         add r14, qword ptr [rsp + 0xc0]
002F63F0  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
002F63F5  4D 3B E5                        cmp r12, r13
002F63F8  77 24                           ja 0x1402f641e
002F63FA  41 F6 C6 03                     test r14b, 3
002F63FE  74 06                           je 0x1402f6406
002F6400  E8 CB 3B 5A 00                  call 0x140899fd0
002F6405  CC                              int3
002F6406  49 8B C6                        mov rax, r14
002F6409  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002F6413  4C 3B F1                        cmp r14, rcx
002F6416  48 0F 43 C1                     cmovae rax, rcx
002F641A  90                              nop
002F641B  0F B6 00                        movzx eax, byte ptr [rax]
002F641E  EB 05                           jmp 0x1402f6425
002F6420  E9 8D 05 00 00                  jmp 0x1402f69b2
002F6425  49 8B 07                        mov rax, qword ptr [r15]
002F6428  48 85 C0                        test rax, rax
002F642B  0F 85 5A 05 00 00               jne 0x1402f698b
002F6431  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
002F6435  49 8B D1                        mov rdx, r9
002F6438  48 C1 E2 04                     shl rdx, 4
002F643C  48 03 54 24 60                  add rdx, qword ptr [rsp + 0x60]
002F6441  49 8B 06                        mov rax, qword ptr [r14]
002F6444  48 89 02                        mov qword ptr [rdx], rax
002F6447  4C 89 42 08                     mov qword ptr [rdx + 8], r8
002F644B  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
002F644F  48 85 C0                        test rax, rax
002F6452  0F 84 D7 FD FF FF               je 0x1402f622f
002F6458  4E 89 34 C8                     mov qword ptr [rax + r9*8], r14
002F645C  FF C7                           inc edi
002F645E  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F6462  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F646C  E9 EF FB FF FF                  jmp 0x1402f6060
002F6471  48 8D 8E D0 04 00 00            lea rcx, [rsi + 0x4d0]
002F6478  45 33 C9                        xor r9d, r9d
002F647B  41 8D 51 0B                     lea edx, [r9 + 0xb]
002F647F  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
002F6489  E8 62 1E 00 00                  call 0x1402f82f0
002F648E  48 85 C0                        test rax, rax
002F6491  0F 84 DB FC FF FF               je 0x1402f6172
002F6497  F6 00 01                        test byte ptr [rax], 1
002F649A  0F 84 D2 FC FF FF               je 0x1402f6172
002F64A0  48 83 40 08 08                  add qword ptr [rax + 8], 8
002F64A5  E9 C8 FC FF FF                  jmp 0x1402f6172
002F64AA  B8 28 00 00 C0                  mov eax, 0xc0000028
002F64AF  48 83 C4 70                     add rsp, 0x70
002F64B3  41 5F                           pop r15
002F64B5  41 5E                           pop r14
002F64B7  41 5D                           pop r13
002F64B9  41 5C                           pop r12
002F64BB  5F                              pop rdi
002F64BC  5E                              pop rsi
002F64BD  5B                              pop rbx
002F64BE  C3                              ret
002F64BF  CC                              int3
002F64C0  4C 3B 00                        cmp r8, qword ptr [rax]
002F64C3  0F 82 39 03 00 00               jb 0x1402f6802
002F64C9  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F64CD  48 8B 08                        mov rcx, qword ptr [rax]
002F64D0  48 83 E9 08                     sub rcx, 8
002F64D4  4C 3B C1                        cmp r8, rcx
002F64D7  0F 86 31 FD FF FF               jbe 0x1402f620e
002F64DD  B8 28 00 00 C0                  mov eax, 0xc0000028
002F64E2  E9 D0 FC FF FF                  jmp 0x1402f61b7
002F64E7  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
002F64EC  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
002F64F3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002F64F8  48 8B 08                        mov rcx, qword ptr [rax]
002F64FB  4C 8D 41 08                     lea r8, [rcx + 8]
002F64FF  45 85 C9                        test r9d, r9d
002F6502  4C 0F 44 C1                     cmove r8, rcx
002F6506  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
002F650B  BA 20 00 00 00                  mov edx, 0x20
002F6510  41 B9 18 00 00 00               mov r9d, 0x18
002F6516  41 0F 44 D1                     cmove edx, r9d
002F651A  48 03 D1                        add rdx, rcx
002F651D  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
002F6522  4D 3B E5                        cmp r12, r13
002F6525  77 1A                           ja 0x1402f6541
002F6527  41 F6 C0 03                     test r8b, 3
002F652B  74 06                           je 0x1402f6533
002F652D  E8 9E 3A 5A 00                  call 0x140899fd0
002F6532  CC                              int3
002F6533  49 8B C0                        mov rax, r8
002F6536  4D 3B C6                        cmp r8, r14
002F6539  49 0F 43 C6                     cmovae rax, r14
002F653D  90                              nop
002F653E  0F B6 00                        movzx eax, byte ptr [rax]
002F6541  EB 05                           jmp 0x1402f6548
002F6543  E9 F1 02 00 00                  jmp 0x1402f6839
002F6548  49 8B 07                        mov rax, qword ptr [r15]
002F654B  48 85 C0                        test rax, rax
002F654E  74 1D                           je 0x1402f656d
002F6550  4C 3B 00                        cmp r8, qword ptr [rax]
002F6553  0F 82 A9 02 00 00               jb 0x1402f6802
002F6559  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F655D  48 8B 08                        mov rcx, qword ptr [rax]
002F6560  48 83 E9 08                     sub rcx, 8
002F6564  4C 3B C1                        cmp r8, rcx
002F6567  0F 87 91 04 00 00               ja 0x1402f69fe
002F656D  4D 3B E5                        cmp r12, r13
002F6570  77 19                           ja 0x1402f658b
002F6572  F6 C2 03                        test dl, 3
002F6575  74 06                           je 0x1402f657d
002F6577  E8 54 3A 5A 00                  call 0x140899fd0
002F657C  CC                              int3
002F657D  48 8B C2                        mov rax, rdx
002F6580  49 3B D6                        cmp rdx, r14
002F6583  49 0F 43 C6                     cmovae rax, r14
002F6587  90                              nop
002F6588  0F B6 00                        movzx eax, byte ptr [rax]
002F658B  EB 02                           jmp 0x1402f658f
002F658D  EB 73                           jmp 0x1402f6602
002F658F  49 8B 07                        mov rax, qword ptr [r15]
002F6592  48 85 C0                        test rax, rax
002F6595  0F 84 AE 00 00 00               je 0x1402f6649
002F659B  48 3B 10                        cmp rdx, qword ptr [rax]
002F659E  0F 82 5E 02 00 00               jb 0x1402f6802
002F65A4  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F65A8  48 8B 08                        mov rcx, qword ptr [rax]
002F65AB  48 83 E9 08                     sub rcx, 8
002F65AF  48 3B D1                        cmp rdx, rcx
002F65B2  0F 86 91 00 00 00               jbe 0x1402f6649
002F65B8  B8 28 00 00 C0                  mov eax, 0xc0000028
002F65BD  E9 F5 FB FF FF                  jmp 0x1402f61b7
002F65C2  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
002F65C7  E9 CD FB FF FF                  jmp 0x1402f6199
002F65CC  FF C7                           inc edi
002F65CE  41 0F B7 54 7B 04               movzx edx, word ptr [r11 + rdi*2 + 4]
002F65D4  45 85 C9                        test r9d, r9d
002F65D7  0F 85 9B 01 00 00               jne 0x1402f6778
002F65DD  8D 14 D5 00 00 00 00            lea edx, [rdx*8]
002F65E4  8B C2                           mov eax, edx
002F65E6  48 01 86 98 00 00 00            add qword ptr [rsi + 0x98], rax
002F65ED  FF C7                           inc edi
002F65EF  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F65F3  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F65FD  E9 5E FA FF FF                  jmp 0x1402f6060
002F6602  85 C0                           test eax, eax
002F6604  0F 88 AD FB FF FF               js 0x1402f61b7
002F660A  45 33 D2                        xor r10d, r10d
002F660D  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F6617  48 8D 1D E2 99 D0 FF            lea rbx, [rip - 0x2f661e]
002F661E  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F6626  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F662E  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F6636  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F663A  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F663F  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
002F6644  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002F6649  49 8B 00                        mov rax, qword ptr [r8]
002F664C  48 89 86 F8 00 00 00            mov qword ptr [rsi + 0xf8], rax
002F6653  48 8B 0A                        mov rcx, qword ptr [rdx]
002F6656  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002F665B  48 89 08                        mov qword ptr [rax], rcx
002F665E  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002F6661  25 80 00 10 00                  and eax, 0x100080
002F6666  3D 80 00 10 00                  cmp eax, 0x100080
002F666B  0F 85 BE FB FF FF               jne 0x1402f622f
002F6671  49 8B CB                        mov rcx, r11
002F6674  E8 DF B2 18 00                  call 0x140481958
002F6679  84 C0                           test al, al
002F667B  0F 85 AE FB FF FF               jne 0x1402f622f
002F6681  48 63 86 E8 04 00 00            movsxd rax, dword ptr [rsi + 0x4e8]
002F6688  48 83 84 30 D0 04 00 00 18      add qword ptr [rax + rsi + 0x4d0], 0x18
002F6691  FF C7                           inc edi
002F6693  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F6697  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F66A1  E9 BA F9 FF FF                  jmp 0x1402f6060
002F66A6  44 0F B6 42 05                  movzx r8d, byte ptr [rdx + 5]
002F66AB  41 8B C8                        mov ecx, r8d
002F66AE  83 E1 0F                        and ecx, 0xf
002F66B1  83 F9 0B                        cmp ecx, 0xb
002F66B4  0F 83 93 FC FF FF               jae 0x1402f634d
002F66BA  0F B6 94 19 98 30 01 00         movzx edx, byte ptr [rcx + rbx + 0x13098]
002F66C2  83 F9 01                        cmp ecx, 1
002F66C5  74 0B                           je 0x1402f66d2
002F66C7  03 FA                           add edi, edx
002F66C9  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F66CD  E9 8E F9 FF FF                  jmp 0x1402f6060
002F66D2  41 F6 C0 F0                     test r8b, 0xf0
002F66D6  74 EF                           je 0x1402f66c7
002F66D8  FF C2                           inc edx
002F66DA  EB EB                           jmp 0x1402f66c7
002F66DC  83 C7 02                        add edi, 2
002F66DF  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F66E3  41 0F B7 54 7B 04               movzx edx, word ptr [r11 + rdi*2 + 4]
002F66E9  48 C1 E2 10                     shl rdx, 0x10
002F66ED  8D 47 FF                        lea eax, [rdi - 1]
002F66F0  45 0F B7 44 43 04               movzx r8d, word ptr [r11 + rax*2 + 4]
002F66F6  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
002F66FE  48 03 CA                        add rcx, rdx
002F6701  4C 03 C1                        add r8, rcx
002F6704  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
002F6709  4D 3B E5                        cmp r12, r13
002F670C  77 1A                           ja 0x1402f6728
002F670E  41 F6 C0 03                     test r8b, 3
002F6712  74 06                           je 0x1402f671a
002F6714  E8 B7 38 5A 00                  call 0x140899fd0
002F6719  CC                              int3
002F671A  49 8B C0                        mov rax, r8
002F671D  4D 3B C6                        cmp r8, r14
002F6720  49 0F 43 C6                     cmovae rax, r14
002F6724  90                              nop
002F6725  0F B6 00                        movzx eax, byte ptr [rax]
002F6728  EB 05                           jmp 0x1402f672f
002F672A  E9 60 01 00 00                  jmp 0x1402f688f
002F672F  49 8B 07                        mov rax, qword ptr [r15]
002F6732  48 85 C0                        test rax, rax
002F6735  74 1D                           je 0x1402f6754
002F6737  4C 3B 00                        cmp r8, qword ptr [rax]
002F673A  0F 82 C2 00 00 00               jb 0x1402f6802
002F6740  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F6744  48 8B 08                        mov rcx, qword ptr [rax]
002F6747  48 83 E9 08                     sub rcx, 8
002F674B  4C 3B C1                        cmp r8, rcx
002F674E  0F 87 AE 00 00 00               ja 0x1402f6802
002F6754  41 8B D1                        mov edx, r9d
002F6757  49 8B 08                        mov rcx, qword ptr [r8]
002F675A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002F675F  48 89 0C D0                     mov qword ptr [rax + rdx*8], rcx
002F6763  FF C7                           inc edi
002F6765  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F6769  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F6773  E9 E8 F8 FF FF                  jmp 0x1402f6060
002F6778  FF C7                           inc edi
002F677A  41 0F B7 4C 7B 04               movzx ecx, word ptr [r11 + rdi*2 + 4]
002F6780  C1 E1 10                        shl ecx, 0x10
002F6783  03 D1                           add edx, ecx
002F6785  E9 5A FE FF FF                  jmp 0x1402f65e4
002F678A  83 C7 02                        add edi, 2
002F678D  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F6791  41 0F B7 54 7B 04               movzx edx, word ptr [r11 + rdi*2 + 4]
002F6797  48 C1 E2 10                     shl rdx, 0x10
002F679B  8D 47 FF                        lea eax, [rdi - 1]
002F679E  45 0F B7 74 43 04               movzx r14d, word ptr [r11 + rax*2 + 4]
002F67A4  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
002F67AC  48 03 CA                        add rcx, rdx
002F67AF  4C 03 F1                        add r14, rcx
002F67B2  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
002F67B7  4D 3B E5                        cmp r12, r13
002F67BA  77 24                           ja 0x1402f67e0
002F67BC  41 F6 C6 03                     test r14b, 3
002F67C0  74 06                           je 0x1402f67c8
002F67C2  E8 09 38 5A 00                  call 0x140899fd0
002F67C7  CC                              int3
002F67C8  49 8B C6                        mov rax, r14
002F67CB  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002F67D5  4C 3B F1                        cmp r14, rcx
002F67D8  48 0F 43 C1                     cmovae rax, rcx
002F67DC  90                              nop
002F67DD  0F B6 00                        movzx eax, byte ptr [rax]
002F67E0  E9 40 FC FF FF                  jmp 0x1402f6425
002F67E5  E9 C8 01 00 00                  jmp 0x1402f69b2
002F67EA  83 C7 02                        add edi, 2
002F67ED  FF C7                           inc edi
002F67EF  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
002F67F3  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F67FD  E9 5E F8 FF FF                  jmp 0x1402f6060
002F6802  B8 28 00 00 C0                  mov eax, 0xc0000028
002F6807  48 83 C4 70                     add rsp, 0x70
002F680B  41 5F                           pop r15
002F680D  41 5E                           pop r14
002F680F  41 5D                           pop r13
002F6811  41 5C                           pop r12
002F6813  5F                              pop rdi
002F6814  5E                              pop rsi
002F6815  5B                              pop rbx
002F6816  C3                              ret
002F6817  CC                              int3
002F6818  85 C0                           test eax, eax
002F681A  0F 88 97 F9 FF FF               js 0x1402f61b7
002F6820  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F6828  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
002F682D  49 81 C0 98 00 00 00            add r8, 0x98
002F6834  E9 12 F9 FF FF                  jmp 0x1402f614b
002F6839  85 C0                           test eax, eax
002F683B  0F 88 76 F9 FF FF               js 0x1402f61b7
002F6841  45 33 D2                        xor r10d, r10d
002F6844  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F684E  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
002F6858  48 8D 1D A1 97 D0 FF            lea rbx, [rip - 0x2f685f]
002F685F  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F6867  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F686F  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F6877  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F687B  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F6880  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
002F6885  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002F688A  E9 DE FC FF FF                  jmp 0x1402f656d
002F688F  85 C0                           test eax, eax
002F6891  0F 88 20 F9 FF FF               js 0x1402f61b7
002F6897  45 33 D2                        xor r10d, r10d
002F689A  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F68A4  48 8D 1D 55 97 D0 FF            lea rbx, [rip - 0x2f68ab]
002F68AB  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F68B3  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F68BB  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F68C3  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F68C7  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
002F68CC  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
002F68D1  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F68D6  E9 79 FE FF FF                  jmp 0x1402f6754
002F68DB  85 C0                           test eax, eax
002F68DD  0F 88 D4 F8 FF FF               js 0x1402f61b7
002F68E3  45 33 D2                        xor r10d, r10d
002F68E6  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F68F0  48 8D 1D 09 97 D0 FF            lea rbx, [rip - 0x2f68f7]
002F68F7  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F68FF  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F6907  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F690F  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F6913  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
002F6918  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
002F691D  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F6922  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002F6927  E9 E2 F8 FF FF                  jmp 0x1402f620e
002F692C  85 C0                           test eax, eax
002F692E  0F 88 83 F8 FF FF               js 0x1402f61b7
002F6934  45 33 D2                        xor r10d, r10d
002F6937  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F6941  48 8D 1D B8 96 D0 FF            lea rbx, [rip - 0x2f6948]
002F6948  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F6950  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F6958  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F6960  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F6964  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
002F6969  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
002F696E  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F6973  E9 33 F9 FF FF                  jmp 0x1402f62ab
002F6978  49 8B C3                        mov rax, r11
002F697B  4D 3B DE                        cmp r11, r14
002F697E  49 0F 43 C6                     cmovae rax, r14
002F6982  90                              nop
002F6983  0F B6 00                        movzx eax, byte ptr [rax]
002F6986  E9 D5 F6 FF FF                  jmp 0x1402f6060
002F698B  4C 3B 30                        cmp r14, qword ptr [rax]
002F698E  0F 82 6E FE FF FF               jb 0x1402f6802
002F6994  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002F6998  48 8B 08                        mov rcx, qword ptr [rax]
002F699B  48 83 E9 10                     sub rcx, 0x10
002F699F  4C 3B F1                        cmp r14, rcx
002F69A2  0F 86 89 FA FF FF               jbe 0x1402f6431
002F69A8  B8 28 00 00 C0                  mov eax, 0xc0000028
002F69AD  E9 05 F8 FF FF                  jmp 0x1402f61b7
002F69B2  85 C0                           test eax, eax
002F69B4  0F 88 FD F7 FF FF               js 0x1402f61b7
002F69BA  45 33 D2                        xor r10d, r10d
002F69BD  49 BD FF FF FE FF FF 7F 00 00   movabs r13, 0x7ffffffeffff
002F69C7  48 8D 1D 32 96 D0 FF            lea rbx, [rip - 0x2f69ce]
002F69CE  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
002F69D6  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002F69DE  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
002F69E6  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
002F69EB  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
002F69EF  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
002F69F4  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
002F69F9  E9 33 FA FF FF                  jmp 0x1402f6431
002F69FE  B8 28 00 00 C0                  mov eax, 0xc0000028
002F6A03  E9 AF F7 FF FF                  jmp 0x1402f61b7
002F6A08  B8 28 00 00 C0                  mov eax, 0xc0000028
002F6A0D  E9 A5 F7 FF FF                  jmp 0x1402f61b7
002F6A12  66 90                           nop
002F6A14  CC                              int3
002F6A15  65                              .byte 0x65
002F6A16  2F                              .byte 0x2f
002F6A17  00 4D 63                        add byte ptr [rbp + 0x63], cl
002F6A1A  2F                              .byte 0x2f
002F6A1B  00 99 63 2F 00 4D               add byte ptr [rcx + 0x4d002f63], bl
002F6A21  63 2F                           movsxd ebp, dword ptr [rdi]
002F6A23  00 DC                           add ah, bl
002F6A25  66                              .byte 0x66
002F6A26  2F                              .byte 0x2f
002F6A27  00 C7                           add bh, al
002F6A29  60                              .byte 0x60
002F6A2A  2F                              .byte 0x2f
002F6A2B  00 EA                           add dl, ch
002F6A2D  67                              .byte 0x67
002F6A2E  2F                              .byte 0x2f
002F6A2F  00 D8                           add al, bl
002F6A31  63 2F                           movsxd ebp, dword ptr [rdi]
002F6A33  00 8A 67 2F 00 E7               add byte ptr [rdx - 0x18ffd099], cl
002F6A39  64                              .byte 0x64
002F6A3A  2F                              .byte 0x2f
002F6A3B  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpUnwindPrologue(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned int v_stack_p174;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p1B8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p220;
    unsigned __int64 v_stack_p238;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    v_stack_m40 = a5;
    v_r10 = 0;
    v_stack_m68 = 0;
    v_stack_m48 = a5 + 416;
    v_stack_m60 = a5 + 120;
loc_002F6013:
    v_stack_m84 = 0;
    v_stack_m88 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - (*(unsigned int *)(v_stack_p20)));
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_p8)));
    v_stack_m58 = (unsigned int)(a1);
    v_r11 = ((unsigned int)(*(unsigned int *)(v_stack_p20 + 8))) + (v_stack_p8);
    v_stack_m70 = v_r11;
    if (a2 > v_r13) goto loc_002F6060;
    if ((((unsigned __int8)(v_r11)) & (3)) == 0) goto loc_002F6978;
loc_002F6056:
    result = ExRaiseDatatypeMisalignment(a1, v_stack_p20, a3, a4);
loc_002F6060:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(v_r11 + 2)))) goto loc_002F60DB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r11 + 0 * 2 + 5)))) & (15));
    a4 = (unsigned int)((*(unsigned __int8 *)(v_r11 + 0 * 2 + 5)) >> (4));
    v_stack_m78 = (unsigned int)(a4);
    if (v_stack_m58 < ((unsigned int)(*(unsigned __int8 *)(v_r11 + 0 * 2 + 4)))) goto loc_002F66A6;
    if ((unsigned int)(a1) == 0) goto loc_002F61C8;
    if (((unsigned int)(a1)) == 4) goto loc_002F6244;
    if (((unsigned int)(a1)) == 2) goto loc_002F62E4;
    a1 = (unsigned int)((a1) - 1);
    if (((unsigned int)(a1)) > 9) goto loc_002F634D;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3104779 + a1 * 4 + 3107348))) + (v_rip - 3104779);
loc_002F60DB:
    if (((*(unsigned __int8 *)(v_r11)) & (32)) != 0) goto loc_002F6308;
    if (v_stack_m88 != 0) goto loc_002F6358;
    if (a2 > v_r13) goto loc_002F6111;
    result = *(unsigned __int64 *)(a5 + 152);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, v_r11 + 0 * 2, a3, a4);
    }
    if (result >= v_r14) { result = v_r14; }
loc_002F6111:
    goto loc_002F6118;
loc_002F6118:
    if (*(unsigned __int64 *)(a8) == 0) goto loc_002F6828;
    if ((*(unsigned __int64 *)(a5 + 152)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a8)))) goto loc_002F6802;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8))) - (8);
    if ((*(unsigned __int64 *)(a5 + 152)) > a1) goto loc_002F64AA;
loc_002F614B:
    *(unsigned __int64 *)(a5 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    *(unsigned __int64 *)(a5 + 152) = *(unsigned __int64 *)(a5 + 152) + 8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 48))) & (0x100040ULL));
    if (((unsigned int)(result)) == 0x100040ULL) goto loc_002F6471;
loc_002F6172:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 48))) & (0x100080ULL));
    if (((unsigned int)(result)) == 0x100080ULL) {
        result = (int)(*(unsigned int *)(a5 + 1256));
    }
    if (a6 != 0) goto loc_002F638D;
loc_002F61A2:
    *(unsigned __int64 *)(a7) = v_stack_p20;
    result = 0;
loc_002F61B7:
    v_rsp = (v_rsp) + (112);
    return result;
loc_002F61C8:
    v_stack_p58 = a5 + 152;
    v_stack_p28 = *(unsigned __int64 *)(a5 + 152);
    if (a2 > v_r13) goto loc_002F61FB;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a7, a5 + 152, *(unsigned __int64 *)(a5 + 152), a4);
    }
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= v_r14) { result = v_r14; }
loc_002F61FB:
    goto loc_002F6202;
loc_002F6202:
    if (*(unsigned __int64 *)(a8) != 0) goto loc_002F64C0;
loc_002F620E:
    *(unsigned __int64 *)(v_stack_p48 + a4 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    if (*(unsigned __int64 *)(a8 + 16) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + a4 * 8 + 128) = *(unsigned __int64 *)(a5 + 152);
    }
loc_002F622F:
    v_rdi = (unsigned int)((0) + 1);
    v_stack_p24 = (unsigned int)(v_rdi);
    goto loc_002F6060;
loc_002F6244:
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_stack_p24 = (unsigned int)(v_rdi);
    v_stack_p28 = v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8;
    if (a2 > v_r13) goto loc_002F627F;
    result = v_stack_pC0;
    if ((((unsigned __int8)(v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(*(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4), v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8, *(unsigned __int64 *)(a5 + 152), a4);
    }
    result = v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8;
    if ((v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8) >= v_r14) { result = v_r14; }
loc_002F627F:
    goto loc_002F6286;
loc_002F6286:
    if (*(unsigned __int64 *)(a8) == 0) goto loc_002F62AB;
    if ((v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a8)))) goto loc_002F6802;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8))) - (8);
    if ((v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8) > a1) goto loc_002F6A08;
loc_002F62AB:
    *(unsigned __int64 *)(v_stack_p48 + (unsigned int)((unsigned int)(a4)) * 8) = *(unsigned __int64 *)(v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8);
    if (*(unsigned __int64 *)(a8 + 16) == 0) goto loc_002F622F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + (unsigned int)((unsigned int)(a4)) * 8 + 128) = v_stack_pC0 + *(unsigned __int16 *)(v_r11 + v_rdi * 2 + 4) * 8;
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_stack_p24 = (unsigned int)(v_rdi);
    goto loc_002F6060;
loc_002F62E4:
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_stack_p24 = (unsigned int)(v_rdi);
    goto loc_002F6060;
loc_002F6308:
    if ((((unsigned __int8)(a4 * 8 + 8)) & (1)) != 0) {
        a1 = (unsigned int)((a4 * 8 + 8) + 1);
    }
    a2 = ((unsigned int)((unsigned int)(a1))) + (2);
    v_stack_pC8 = v_r11 + a2 * 2;
    if (a2 > v_r13) goto loc_002F633A;
    if ((((unsigned __int8)(v_r11 + a2 * 2)) & (3)) != 0) goto loc_002F6056;
    a2 = v_r11 + a2 * 2;
    if ((v_r11 + a2 * 2) >= v_r14) { a2 = v_r14; }
loc_002F633A:
    result = (unsigned int)(((unsigned int)(v_stack_p40)) + 1);
    v_stack_p40 = (unsigned int)(result);
    if (((unsigned int)(result)) <= 32) goto loc_002F6013;
loc_002F634D:
    result = RtlRaiseStatus((unsigned int)(0xC00000FFULL), a2, (unsigned int)((unsigned int)(a4)), a4);
loc_002F6358:
    if (a6 == 0) goto loc_002F61A2;
loc_002F6370:
    if (0 >= 4) goto loc_002F6199;
    if (v_r11 == (*(unsigned __int64 *)(v_rip - 3104779 + v_r10 * 8 + 14687912))) goto loc_002F65C2;
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_002F6370;
loc_002F638D:
    *(unsigned __int8 *)(a6) = (unsigned __int8)(v_stack_p20);
    goto loc_002F61A2;
loc_002F6471:
    a4 = 0;
    result = RtlLocateExtendedFeature2(a5 + 1232, a4 + 11, (unsigned int)((unsigned int)(a4)), a4);
    if (result == 0) goto loc_002F6172;
    if (((*(unsigned __int8 *)(result)) & (1)) == 0) goto loc_002F6172;
    goto loc_002F6172;
loc_002F64AA:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000028ULL);
loc_002F64C0:
    if (((unsigned int)((unsigned int)(a4))) < (*(unsigned __int64 *)((unsigned int)(0xC0000028ULL)))) goto loc_002F6802;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 8))) - (8);
    if (((unsigned int)((unsigned int)(a4))) <= a1) goto loc_002F620E;
    goto loc_002F61B7;
loc_002F65C2:
    v_stack_pC8 = 0;
    goto loc_002F6199;
loc_002F66A6:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a4 + 11 + 5)))) & (15));
    if (((unsigned int)(a1)) >= 11) goto loc_002F634D;
    if (((unsigned int)(a1)) == 1) goto loc_002F66D2;
loc_002F66C7:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(*(unsigned __int8 *)(a1 + v_rip - 3104779 * 1 + 77976))));
    v_stack_pCC = (unsigned int)(v_rdi);
    goto loc_002F6060;
loc_002F66D2:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 11 + 5))) & (240)) == 0) goto loc_002F66C7;
    a2 = (unsigned int)((*(unsigned __int8 *)(a1 + v_rip - 3104779 * 1 + 77976)) + 1);
    goto loc_002F66C7;
loc_002F6802:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000028ULL);
loc_002F6828:
    a3 = (v_stack_p1B8) + (152);
    goto loc_002F614B;
loc_002F6978:
    result = v_r11;
    if (v_r11 >= v_r14) { result = v_r14; }
    goto loc_002F6060;
loc_002F6A08:
    goto loc_002F61B7;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpUnwindPrologue(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m84;
    uint8_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p100;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint32_t v_stack_p174;
    uint64_t v_stack_p178;
    uint64_t v_stack_p18;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p1B8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p208;
    uint64_t v_stack_p220;
    uint64_t v_stack_p238;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    v_stack_m40 = Arg5;
    local_r10 = 0;
    v_stack_m68 = 0;
    v_stack_m48 = Arg5 + 416;
    v_stack_m60 = Arg5 + 120;
loc_002F6013:
    v_stack_m84 = 0;
    v_stack_m88 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - (*(uint32_t *)(v_stack_p20)));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_p8)));
    v_stack_m58 = (uint32_t)(Arg1);
    local_r11 = ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8))) + (v_stack_p8);
    v_stack_m70 = local_r11;
    if (Arg2 > local_r13) goto loc_002F6060;
    if ((((uint8_t)(local_r11)) & (3)) == 0) goto loc_002F6978;
loc_002F6056:
    result = ExRaiseDatatypeMisalignment(Arg1, v_stack_p20, Arg3, Arg4);
loc_002F6060:
    if (0 >= ((uint32_t)(*(uint8_t *)(local_r11 + 0x2)))) goto loc_002F60DB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_r11 + 0x0 * 2 + 0x5)))) & (15));
    Arg4 = (uint32_t)((*(uint8_t *)(local_r11 + 0x0 * 2 + 0x5)) >> (4));
    v_stack_m78 = (uint32_t)(Arg4);
    if (v_stack_m58 < ((uint32_t)(*(uint8_t *)(local_r11 + 0x0 * 2 + 0x4)))) goto loc_002F66A6;
    if ((uint32_t)(Arg1) == 0) goto loc_002F61C8;
    if (((uint32_t)(Arg1)) == 4) goto loc_002F6244;
    if (((uint32_t)(Arg1)) == 2) goto loc_002F62E4;
    Arg1 = (uint32_t)((Arg1) - 1);
    if (((uint32_t)(Arg1)) > 9) goto loc_002F634D;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x2F600B + Arg1 * 4 + 0x2F6A14))) + (v_rip - 3104779);
loc_002F60DB:
    if (((*(uint8_t *)(local_r11)) & (32)) != 0) goto loc_002F6308;
    if (v_stack_m88 != 0) goto loc_002F6358;
    if (Arg2 > local_r13) goto loc_002F6111;
    result = *(uint64_t *)(arg5 + 0x98);
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, local_r11 + 0 * 2, Arg3, Arg4);
    }
    if (result >= local_r14) { result = local_r14; }
loc_002F6111:
    goto loc_002F6118;
loc_002F6118:
    if (*(uint64_t *)(arg8) == 0) goto loc_002F6828;
    if ((*(uint64_t *)(arg5 + 0x98)) < (*(uint64_t *)(*(uint64_t *)(arg8)))) goto loc_002F6802;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg8 + 0x8))) - (8);
    if ((*(uint64_t *)(arg5 + 0x98)) > Arg1) goto loc_002F64AA;
loc_002F614B:
    *(uint64_t *)(arg5 + 0xF8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    *(uint64_t *)(arg5 + 0x98) = *(uint64_t *)(arg5 + 0x98) + 8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x30))) & (0x100040ULL));
    if (((uint32_t)(result)) == 0x100040ULL) goto loc_002F6471;
loc_002F6172:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x30))) & (0x100080ULL));
    if (((uint32_t)(result)) == 0x100080ULL) {
        result = (int32_t)(*(uint32_t *)(arg5 + 0x4E8));
    }
    if (Arg6 != 0) goto loc_002F638D;
loc_002F61A2:
    *(uint64_t *)(arg7) = v_stack_p20;
    result = 0;
loc_002F61B7:
    local_rsp = (local_rsp) + (112);
    return result;
loc_002F61C8:
    v_stack_p58 = Arg5 + 152;
    v_stack_p28 = *(uint64_t *)(arg5 + 0x98);
    if (Arg2 > local_r13) goto loc_002F61FB;
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg7, Arg5 + 152, *(uint64_t *)(arg5 + 0x98), Arg4);
    }
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= local_r14) { result = local_r14; }
loc_002F61FB:
    goto loc_002F6202;
loc_002F6202:
    if (*(uint64_t *)(arg8) != 0) goto loc_002F64C0;
loc_002F620E:
    *(uint64_t *)(v_stack_p48 + Arg4 * 8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    if (*(uint64_t *)(arg8 + 0x10) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg8 + 0x10) + Arg4 * 8 + 0x80) = *(uint64_t *)(arg5 + 0x98);
    }
loc_002F622F:
    local_rdi = (uint32_t)((0) + 1);
    v_stack_p24 = (uint32_t)(local_rdi);
    goto loc_002F6060;
loc_002F6244:
    local_rdi = (uint32_t)((local_rdi) + 1);
    v_stack_p24 = (uint32_t)(local_rdi);
    v_stack_p28 = v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8;
    if (Arg2 > local_r13) goto loc_002F627F;
    result = v_stack_pC0;
    if ((((uint8_t)(v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(*(uint16_t *)(local_r11 + local_rdi * 2 + 0x4), v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8, *(uint64_t *)(arg5 + 0x98), Arg4);
    }
    result = v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8;
    if ((v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8) >= local_r14) { result = local_r14; }
loc_002F627F:
    goto loc_002F6286;
loc_002F6286:
    if (*(uint64_t *)(arg8) == 0) goto loc_002F62AB;
    if ((v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8) < (*(uint64_t *)(*(uint64_t *)(arg8)))) goto loc_002F6802;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg8 + 0x8))) - (8);
    if ((v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8) > Arg1) goto loc_002F6A08;
loc_002F62AB:
    *(uint64_t *)(v_stack_p48 + (uint32_t)((uint32_t)(Arg4)) * 8) = *(uint64_t *)(v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8);
    if (*(uint64_t *)(arg8 + 0x10) == 0) goto loc_002F622F;
    *(uint64_t *)(*(uint64_t *)(arg8 + 0x10) + (uint32_t)((uint32_t)(Arg4)) * 8 + 0x80) = v_stack_pC0 + *(uint16_t *)(local_r11 + local_rdi * 2 + 0x4) * 8;
    local_rdi = (uint32_t)((local_rdi) + 1);
    v_stack_p24 = (uint32_t)(local_rdi);
    goto loc_002F6060;
loc_002F62E4:
    local_rdi = (uint32_t)((local_rdi) + 1);
    v_stack_p24 = (uint32_t)(local_rdi);
    goto loc_002F6060;
loc_002F6308:
    if ((((uint8_t)(Arg4 * 8 + 8)) & (1)) != 0) {
        Arg1 = (uint32_t)((Arg4 * 8 + 8) + 1);
    }
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (2);
    v_stack_pC8 = local_r11 + Arg2 * 2;
    if (Arg2 > local_r13) goto loc_002F633A;
    if ((((uint8_t)(local_r11 + Arg2 * 2)) & (3)) != 0) goto loc_002F6056;
    Arg2 = local_r11 + Arg2 * 2;
    if ((local_r11 + Arg2 * 2) >= local_r14) { Arg2 = local_r14; }
loc_002F633A:
    result = (uint32_t)(((uint32_t)(v_stack_p40)) + 1);
    v_stack_p40 = (uint32_t)(result);
    if (((uint32_t)(result)) <= 32) goto loc_002F6013;
loc_002F634D:
    result = RtlRaiseStatus((uint32_t)(0xC00000FFULL), Arg2, (uint32_t)((uint32_t)(Arg4)), Arg4);
loc_002F6358:
    if (Arg6 == 0) goto loc_002F61A2;
loc_002F6370:
    if (0 >= 4) goto loc_002F6199;
    if (local_r11 == (*(uint64_t *)(v_rip - 0x2F600B + local_r10 * 8 + 0xE01EA8))) goto loc_002F65C2;
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_002F6370;
loc_002F638D:
    *(uint8_t *)(Arg6) = (uint8_t)(v_stack_p20);
    goto loc_002F61A2;
loc_002F6471:
    Arg4 = 0;
    result = RtlLocateExtendedFeature2(Arg5 + 1232, Arg4 + 11, (uint32_t)((uint32_t)(Arg4)), Arg4);
    if (result == 0) goto loc_002F6172;
    if (((*(uint8_t *)(result)) & (1)) == 0) goto loc_002F6172;
    goto loc_002F6172;
loc_002F64AA:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000028ULL);
loc_002F64C0:
    if (((uint32_t)((uint32_t)(Arg4))) < (*(uint64_t *)((uint32_t)(0xC0000028ULL)))) goto loc_002F6802;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg8 + 0x8))) - (8);
    if (((uint32_t)((uint32_t)(Arg4))) <= Arg1) goto loc_002F620E;
    goto loc_002F61B7;
loc_002F65C2:
    v_stack_pC8 = 0;
    goto loc_002F6199;
loc_002F66A6:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg4 + 0xB + 0x5)))) & (15));
    if (((uint32_t)(Arg1)) >= 11) goto loc_002F634D;
    if (((uint32_t)(Arg1)) == 1) goto loc_002F66D2;
loc_002F66C7:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(*(uint8_t *)(Arg1 + v_rip - 0x2F600B * 1 + 0x13098))));
    v_stack_pCC = (uint32_t)(local_rdi);
    goto loc_002F6060;
loc_002F66D2:
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0xB + 0x5))) & (240)) == 0) goto loc_002F66C7;
    Arg2 = (uint32_t)((*(uint8_t *)(Arg1 + v_rip - 0x2F600B * 1 + 0x13098)) + 1);
    goto loc_002F66C7;
loc_002F6802:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000028ULL);
loc_002F6828:
    Arg3 = (v_stack_p1B8) + (152);
    goto loc_002F614B;
loc_002F6978:
    result = local_r11;
    if (local_r11 >= local_r14) { result = local_r14; }
    goto loc_002F6060;
loc_002F6A08:
    goto loc_002F61B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x30` | `32` | `R` |
| `Arg5` | `+ 0x78` | `64` | `R` |
| `Arg5` | `+ 0x98` | `64` | `R` |
| `Arg5` | `+ 0x98` | `64` | `R/W` |
| `Arg5` | `+ 0xF8` | `64` | `W` |
| `Arg5` | `+ 0x1A0` | `64` | `R` |
| `Arg5` | `+ 0x4D0` | `64` | `R` |
| `Arg5` | `+ 0x4E8` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x8` | `64` | `R` |
| `Arg8` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F5FA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
