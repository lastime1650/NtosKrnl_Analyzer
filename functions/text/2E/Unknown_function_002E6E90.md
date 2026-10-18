# sub_002E6E90

- RVA: `0x002E6E90`–`0x002E7362` (길이 `1,234` bytes)
- VA: `0x00000001402E6E90`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071290`
- 디코드: `315`개 명령, `1,234/1,234` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002E706F` → [RtlpHpVsFreeChunkRemove](RtlpHpVsFreeChunkRemove_function_002E6BA0.md) (function, `0x002E6BA0`)
- `0x002E70F0` → [RtlpHpVsChunkFree](RtlpHpVsChunkFree_function_002E3980.md) (function, `0x002E3980`)
- `0x002E71AB` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x002E71C1` → [RtlpHpReleaseQueuedLockExclusive](RtlpHpReleaseQueuedLockExclusive_function_002E2A70.md) (function, `0x002E2A70`)
- `0x002E7202` → [RtlpHpVsSubsegmentFree](RtlpHpVsSubsegmentFree_function_002E7D9C.md) (function, `0x002E7D9C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002E6EC7` → RVA `0x00E28300` (`.data`; read)
- `0x002E6F7D` → RVA `0x00E28302` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002E7127` → [sub_002E7373](Unknown_function_002E7373.md) (`tail-transfer`)
  - `0x002E72A3` → [sub_002E7373 + 0xD](Unknown_function_002E7373.md) (`tail-transfer`)
  - `0x002E730F` → [sub_002E7373 + 0x8](Unknown_function_002E7373.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E6E90  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
002E6E98  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
002E6EA0  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
002E6EA5  41 BB FF 7F 00 00               mov r11d, 0x7fff
002E6EAB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002E6EB0  41 B9 ED 2B 00 00               mov r9d, 0x2bed
002E6EB6  48 85 DB                        test rbx, rbx
002E6EB9  0F 84 F1 02 00 00               je 0x1402e71b0
002E6EBF  48 8B 4B F8                     mov rcx, qword ptr [rbx - 8]
002E6EC3  48 8D 73 F8                     lea rsi, [rbx - 8]
002E6EC7  4C 8B 05 32 14 B4 00            mov r8, qword ptr [rip + 0xb41432]
002E6ECE  48 8B D6                        mov rdx, rsi
002E6ED1  48 33 D1                        xor rdx, rcx
002E6ED4  48 8B FE                        mov rdi, rsi
002E6ED7  49 33 D0                        xor rdx, r8
002E6EDA  48 C1 EA 20                     shr rdx, 0x20
002E6EDE  F7 C2 00 00 FF 00               test edx, 0xff0000
002E6EE4  75 4C                           jne 0x1402e6f32
002E6EE6  66 85 D2                        test dx, dx
002E6EE9  0F 84 91 02 00 00               je 0x1402e7180
002E6EEF  0F B7 C2                        movzx eax, dx
002E6EF2  48 C1 E0 04                     shl rax, 4
002E6EF6  48 2B F8                        sub rdi, rax
002E6EF9  48 8B D7                        mov rdx, rdi
002E6EFC  49 33 D0                        xor rdx, r8
002E6EFF  48 33 17                        xor rdx, qword ptr [rdi]
002E6F02  48 C1 EA 20                     shr rdx, 0x20
002E6F06  F7 C2 00 00 FF 00               test edx, 0xff0000
002E6F0C  0F 85 0B 01 00 00               jne 0x1402e701d
002E6F12  66 85 D2                        test dx, dx
002E6F15  0F 84 65 02 00 00               je 0x1402e7180
002E6F1B  0F B7 C2                        movzx eax, dx
002E6F1E  48 C1 E0 04                     shl rax, 4
002E6F22  48 2B F8                        sub rdi, rax
002E6F25  8B C7                           mov eax, edi
002E6F27  33 47 08                        xor eax, dword ptr [rdi + 8]
002E6F2A  41 33 C0                        xor eax, r8d
002E6F2D  0F B6 D0                        movzx edx, al
002E6F30  EB 0A                           jmp 0x1402e6f3c
002E6F32  8B C6                           mov eax, esi
002E6F34  33 03                           xor eax, dword ptr [rbx]
002E6F36  41 33 C0                        xor eax, r8d
002E6F39  0F B6 D0                        movzx edx, al
002E6F3C  49 33 C8                        xor rcx, r8
002E6F3F  C1 E2 0C                        shl edx, 0xc
002E6F42  48 33 CE                        xor rcx, rsi
002E6F45  8B C2                           mov eax, edx
002E6F47  48 2B F8                        sub rdi, rax
002E6F4A  48 C1 E9 20                     shr rcx, 0x20
002E6F4E  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
002E6F55  F7 C1 00 00 FF 00               test ecx, 0xff0000
002E6F5B  0F 85 26 02 00 00               jne 0x1402e7187
002E6F61  0F B7 4F 24                     movzx ecx, word ptr [rdi + 0x24]
002E6F65  66 33 4F 20                     xor cx, word ptr [rdi + 0x20]
002E6F69  66 41 33 C9                     xor cx, r9w
002E6F6D  66 41 85 CB                     test r11w, cx
002E6F71  0F 85 10 02 00 00               jne 0x1402e7187
002E6F77  44 8B 36                        mov r14d, dword ptr [rsi]
002E6F7A  41 8B CE                        mov ecx, r14d
002E6F7D  0F B7 05 7E 13 B4 00            movzx eax, word ptr [rip + 0xb4137e]
002E6F84  33 CE                           xor ecx, esi
002E6F86  C1 E9 10                        shr ecx, 0x10
002E6F89  33 C8                           xor ecx, eax
002E6F8B  C1 E1 04                        shl ecx, 4
002E6F8E  81 F9 00 10 00 00               cmp ecx, 0x1000
002E6F94  0F 82 16 02 00 00               jb 0x1402e71b0
002E6F9A  44 33 F6                        xor r14d, esi
002E6F9D  44 8B FE                        mov r15d, esi
002E6FA0  45 33 F0                        xor r14d, r8d
002E6FA3  44 2B FF                        sub r15d, edi
002E6FA6  41 8B C6                        mov eax, r14d
002E6FA9  C1 E8 10                        shr eax, 0x10
002E6FAC  C1 E0 04                        shl eax, 4
002E6FAF  2B C7                           sub eax, edi
002E6FB1  45 8D 8F 1F 10 00 00            lea r9d, [r15 + 0x101f]
002E6FB8  03 C6                           add eax, esi
002E6FBA  41 81 E1 00 F0 FF FF            and r9d, 0xfffff000
002E6FC1  25 00 F0 FF FF                  and eax, 0xfffff000
002E6FC6  44 3B C8                        cmp r9d, eax
002E6FC9  72 62                           jb 0x1402e702d
002E6FCB  41 0F B6 4D 05                  movzx ecx, byte ptr [r13 + 5]
002E6FD0  4C 8B C3                        mov r8, rbx
002E6FD3  48 8B 13                        mov rdx, qword ptr [rbx]
002E6FD6  83 E1 01                        and ecx, 1
002E6FD9  48 85 D2                        test rdx, rdx
002E6FDC  0F 84 36 01 00 00               je 0x1402e7118
002E6FE2  48 8B C2                        mov rax, rdx
002E6FE5  48 33 C3                        xor rax, rbx
002E6FE8  48 8B DA                        mov rbx, rdx
002E6FEB  85 C9                           test ecx, ecx
002E6FED  48 0F 45 D8                     cmovne rbx, rax
002E6FF1  48 83 7B 08 00                  cmp qword ptr [rbx + 8], 0
002E6FF6  0F 84 B4 FE FF FF               je 0x1402e6eb0
002E6FFC  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002E7000  85 C9                           test ecx, ecx
002E7002  74 09                           je 0x1402e700d
002E7004  48 85 C0                        test rax, rax
002E7007  0F 85 43 03 00 00               jne 0x1402e7350
002E700D  48 8B D8                        mov rbx, rax
002E7010  48 83 7B 08 00                  cmp qword ptr [rbx + 8], 0
002E7015  0F 84 95 FE FF FF               je 0x1402e6eb0
002E701B  EB DF                           jmp 0x1402e6ffc
002E701D  8B C7                           mov eax, edi
002E701F  33 47 08                        xor eax, dword ptr [rdi + 8]
002E7022  41 33 C0                        xor eax, r8d
002E7025  0F B6 D0                        movzx edx, al
002E7028  E9 0F FF FF FF                  jmp 0x1402e6f3c
002E702D  FF C8                           dec eax
002E702F  41 C1 E9 0C                     shr r9d, 0xc
002E7033  48 C1 E8 0C                     shr rax, 0xc
002E7037  B9 3F 00 00 00                  mov ecx, 0x3f
002E703C  2A C8                           sub cl, al
002E703E  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
002E7045  48 D3 EA                        shr rdx, cl
002E7048  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002E704F  41 0F B6 C9                     movzx ecx, r9b
002E7053  48 D3 E0                        shl rax, cl
002E7056  48 23 D0                        and rdx, rax
002E7059  48 23 57 10                     and rdx, qword ptr [rdi + 0x10]
002E705D  0F 84 68 FF FF FF               je 0x1402e6fcb
002E7063  4C 8B CE                        mov r9, rsi
002E7066  4C 8B C7                        mov r8, rdi
002E7069  49 8B D2                        mov rdx, r10
002E706C  49 8B CD                        mov rcx, r13
002E706F  E8 2C FB FF FF                  call 0x1402e6ba0
002E7074  48 8B 05 85 12 B4 00            mov rax, qword ptr [rip + 0xb41285]
002E707B  4C 8B CE                        mov r9, rsi
002E707E  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
002E7086  4C 8B C7                        mov r8, rdi
002E7089  48 C1 E8 20                     shr rax, 0x20
002E708D  C1 E8 10                        shr eax, 0x10
002E7090  48 C7 84 24 90 00 00 00 00 00 00 00  mov qword ptr [rsp + 0x90], 0
002E709C  41 C1 EF 0C                     shr r15d, 0xc
002E70A0  C7 84 24 94 00 00 00 00 00 01 00  mov dword ptr [rsp + 0x94], 0x10000
002E70AB  44 33 FE                        xor r15d, esi
002E70AE  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
002E70B6  48 C1 E9 20                     shr rcx, 0x20
002E70BA  C1 E9 10                        shr ecx, 0x10
002E70BD  32 C8                           xor cl, al
002E70BF  48 8B C6                        mov rax, rsi
002E70C2  48 C1 E8 20                     shr rax, 0x20
002E70C6  C1 E8 10                        shr eax, 0x10
002E70C9  32 C8                           xor cl, al
002E70CB  88 4E 06                        mov byte ptr [rsi + 6], cl
002E70CE  49 8B CD                        mov rcx, r13
002E70D1  44 33 3D 28 12 B4 00            xor r15d, dword ptr [rip + 0xb41228]
002E70D8  41 0F B6 C7                     movzx eax, r15b
002E70DC  89 03                           mov dword ptr [rbx], eax
002E70DE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
002E70E3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002E70E8  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
002E70F0  E8 8B C8 FF FF                  call 0x1402e3980
002E70F5  48 85 C0                        test rax, rax
002E70F8  0F 84 41 01 00 00               je 0x1402e723f
002E70FE  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002E7103  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002E7108  48 39 11                        cmp qword ptr [rcx], rdx
002E710B  0F 84 1A 01 00 00               je 0x1402e722b
002E7111  B9 03 00 00 00                  mov ecx, 3
002E7116  CD 29                           int 0x29
002E7118  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
002E711C  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E7120  85 C9                           test ecx, ecx
002E7122  74 09                           je 0x1402e712d
002E7124  48 85 C0                        test rax, rax
002E7127  0F 85 46 02 00 00               jne 0x1402e7373
002E712D  48 8B D8                        mov rbx, rax
002E7130  48 85 DB                        test rbx, rbx
002E7133  0F 84 77 FD FF FF               je 0x1402e6eb0
002E7139  0F 1F 80 00 00 00 00            nop dword ptr [rax]
002E7140  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002E7144  85 C9                           test ecx, ecx
002E7146  74 09                           je 0x1402e7151
002E7148  48 85 C0                        test rax, rax
002E714B  0F 85 DE 01 00 00               jne 0x1402e732f
002E7151  49 3B C0                        cmp rax, r8
002E7154  0F 84 56 FD FF FF               je 0x1402e6eb0
002E715A  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
002E715E  4C 8B C3                        mov r8, rbx
002E7161  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E7165  85 C9                           test ecx, ecx
002E7167  74 09                           je 0x1402e7172
002E7169  48 85 C0                        test rax, rax
002E716C  0F 85 C5 01 00 00               jne 0x1402e7337
002E7172  48 8B D8                        mov rbx, rax
002E7175  48 85 DB                        test rbx, rbx
002E7178  0F 84 32 FD FF FF               je 0x1402e6eb0
002E717E  EB C0                           jmp 0x1402e7140
002E7180  33 D2                           xor edx, edx
002E7182  E9 B5 FD FF FF                  jmp 0x1402e6f3c
002E7187  49 8B D5                        mov rdx, r13
002E718A  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
002E7193  49 33 55 08                     xor rdx, qword ptr [r13 + 8]
002E7197  4C 8B CE                        mov r9, rsi
002E719A  4C 8B C7                        mov r8, rdi
002E719D  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002E71A6  B9 12 00 00 00                  mov ecx, 0x12
002E71AB  E8 0C 46 07 00                  call 0x14035b7bc
002E71B0  41 F6 45 05 01                  test byte ptr [r13 + 5], 1
002E71B5  75 0F                           jne 0x1402e71c6
002E71B7  41 0F B6 4D 03                  movzx ecx, byte ptr [r13 + 3]
002E71BC  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002E71C1  E8 AA B8 FF FF                  call 0x1402e2a70
002E71C6  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002E71CB  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002E71D0  48 3B D0                        cmp rdx, rax
002E71D3  74 34                           je 0x1402e7209
002E71D5  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002E71DA  48 39 42 08                     cmp qword ptr [rdx + 8], rax
002E71DE  0F 85 2D FF FF FF               jne 0x1402e7111
002E71E4  48 8B 02                        mov rax, qword ptr [rdx]
002E71E7  48 39 50 08                     cmp qword ptr [rax + 8], rdx
002E71EB  0F 85 20 FF FF FF               jne 0x1402e7111
002E71F1  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002E71F6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002E71FB  48 89 48 08                     mov qword ptr [rax + 8], rcx
002E71FF  49 8B CD                        mov rcx, r13
002E7202  E8 95 0B 00 00                  call 0x1402e7d9c
002E7207  EB BD                           jmp 0x1402e71c6
002E7209  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
002E720E  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
002E7216  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
002E721E  48 83 C4 68                     add rsp, 0x68
002E7222  41 5E                           pop r14
002E7224  41 5D                           pop r13
002E7226  41 5C                           pop r12
002E7228  5B                              pop rbx
002E7229  C3                              ret
002E722A  CC                              int3
002E722B  48 89 48 08                     mov qword ptr [rax + 8], rcx
002E722F  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002E7234  48 89 10                        mov qword ptr [rax], rdx
002E7237  48 89 01                        mov qword ptr [rcx], rax
002E723A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002E723F  49 0F BF 45 06                  movsx rax, word ptr [r13 + 6]
002E7244  66 85 C0                        test ax, ax
002E7247  0F 84 D9 00 00 00               je 0x1402e7326
002E724D  4A 8B 4C 28 20                  mov rcx, qword ptr [rax + r13 + 0x20]
002E7252  48 85 C9                        test rcx, rcx
002E7255  0F 84 55 FF FF FF               je 0x1402e71b0
002E725B  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
002E7260  41 FF C6                        inc r14d
002E7263  49 8B 1C 24                     mov rbx, qword ptr [r12]
002E7267  4C 8B C8                        mov r9, rax
002E726A  41 83 E1 01                     and r9d, 1
002E726E  0F 85 CB 00 00 00               jne 0x1402e733f
002E7274  44 0F B6 C0                     movzx r8d, al
002E7278  41 8B C8                        mov ecx, r8d
002E727B  83 E1 01                        and ecx, 1
002E727E  33 D2                           xor edx, edx
002E7280  48 85 DB                        test rbx, rbx
002E7283  74 4A                           je 0x1402e72cf
002E7285  48 8D 43 F8                     lea rax, [rbx - 8]
002E7289  33 00                           xor eax, dword ptr [rax]
002E728B  33 05 6F 10 B4 00               xor eax, dword ptr [rip + 0xb4106f]
002E7291  44 3B F0                        cmp r14d, eax
002E7294  72 25                           jb 0x1402e72bb
002E7296  76 16                           jbe 0x1402e72ae
002E7298  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002E729C  85 C9                           test ecx, ecx
002E729E  74 09                           je 0x1402e72a9
002E72A0  48 85 C0                        test rax, rax
002E72A3  0F 85 D7 00 00 00               jne 0x1402e7380
002E72A9  48 8B D8                        mov rbx, rax
002E72AC  EB D2                           jmp 0x1402e7280
002E72AE  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
002E72B6  E9 EA FB FF FF                  jmp 0x1402e6ea5
002E72BB  48 8B 03                        mov rax, qword ptr [rbx]
002E72BE  48 8B D3                        mov rdx, rbx
002E72C1  85 C9                           test ecx, ecx
002E72C3  74 E4                           je 0x1402e72a9
002E72C5  48 85 C0                        test rax, rax
002E72C8  74 DF                           je 0x1402e72a9
002E72CA  48 33 D8                        xor rbx, rax
002E72CD  EB B1                           jmp 0x1402e7280
002E72CF  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
002E72D7  48 8B DA                        mov rbx, rdx
002E72DA  41 BB FF 7F 00 00               mov r11d, 0x7fff
002E72E0  48 85 D2                        test rdx, rdx
002E72E3  0F 85 C7 FB FF FF               jne 0x1402e6eb0
002E72E9  49 8B 04 24                     mov rax, qword ptr [r12]
002E72ED  33 DB                           xor ebx, ebx
002E72EF  4D 85 C9                        test r9, r9
002E72F2  75 64                           jne 0x1402e7358
002E72F4  48 85 C0                        test rax, rax
002E72F7  74 20                           je 0x1402e7319
002E72F9  41 80 E0 01                     and r8b, 1
002E72FD  0F 1F 00                        nop dword ptr [rax]
002E7300  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002E7304  48 8B D8                        mov rbx, rax
002E7307  45 84 C0                        test r8b, r8b
002E730A  74 05                           je 0x1402e7311
002E730C  48 85 C9                        test rcx, rcx
002E730F  75 6A                           jne 0x1402e737b
002E7311  48 8B C1                        mov rax, rcx
002E7314  48 85 C0                        test rax, rax
002E7317  75 E7                           jne 0x1402e7300
002E7319  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
002E7321  E9 8A FB FF FF                  jmp 0x1402e6eb0
002E7326  49 8B 4D 58                     mov rcx, qword ptr [r13 + 0x58]
002E732A  E9 23 FF FF FF                  jmp 0x1402e7252
002E732F  48 33 C3                        xor rax, rbx
002E7332  E9 1A FE FF FF                  jmp 0x1402e7151
002E7337  48 33 D8                        xor rbx, rax
002E733A  E9 36 FE FF FF                  jmp 0x1402e7175
002E733F  48 85 DB                        test rbx, rbx
002E7342  0F 84 2C FF FF FF               je 0x1402e7274
002E7348  49 33 DC                        xor rbx, r12
002E734B  E9 24 FF FF FF                  jmp 0x1402e7274
002E7350  48 33 D8                        xor rbx, rax
002E7353  E9 B8 FC FF FF                  jmp 0x1402e7010
002E7358  48 85 C0                        test rax, rax
002E735B  74 BC                           je 0x1402e7319
002E735D  49 33 C4                        xor rax, r12
002E7360  EB 92                           jmp 0x1402e72f4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E6E90(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_p94;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pC0;

    v_stack_pA0 = v_rsi;
    v_stack_pA8 = v_rdi;
    v_stack_p60 = v_r15;
loc_002E6EA5:
loc_002E6EB0:
    if (v_rbx == 0) goto loc_002E71B0;
    a2 = (v_rbx - 8) ^ (*(unsigned __int64 *)(v_rbx - 8));
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 11801650));
    a2 = (a2) >> (32);
    if ((((unsigned int)(a2)) & (0xFF0000ULL)) != 0) goto loc_002E6F32;
    if ((unsigned __int16)(a2) == 0) goto loc_002E7180;
    result = ((unsigned __int16)(a2)) << (4);
    v_rdi = (v_rbx - 8) - (result);
    a2 = (v_rdi) ^ (*(unsigned __int64 *)(v_rip + 11801650));
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rdi));
    a2 = (a2) >> (32);
    if ((((unsigned int)(a2)) & (0xFF0000ULL)) != 0) goto loc_002E701D;
    if ((unsigned __int16)(a2) == 0) goto loc_002E7180;
    result = ((unsigned __int16)(a2)) << (4);
    v_rdi = (v_rdi) - (result);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) ^ (*(unsigned int *)(v_rdi + 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11801650))));
    goto loc_002E6F3C;
loc_002E6F32:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx - 8))) ^ (*(unsigned int *)(v_rbx)));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11801650))));
loc_002E6F3C:
    a1 = (*(unsigned __int64 *)(v_rbx - 8)) ^ (*(unsigned __int64 *)(v_rip + 11801650));
    a2 = (unsigned int)(((unsigned __int8)(result)) << (12));
    a1 = (a1) ^ (v_rbx - 8);
    v_rdi = (v_rdi) - ((unsigned int)((unsigned int)(a2)));
    a1 = (a1) >> (32);
    v_rdi = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    if ((((unsigned int)(a1)) & (0xFF0000ULL)) != 0) goto loc_002E7187;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + 36)) ^ (*(unsigned __int16 *)(v_rdi + 32)));
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)((unsigned int)(0x2BEDULL))));
    if ((((unsigned __int16)((unsigned int)(0x7FFFULL))) & ((unsigned __int16)(a1))) != 0) goto loc_002E7187;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx - 8))))) ^ ((unsigned int)(v_rbx - 8)));
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11801470))));
    a1 = (unsigned int)((a1) << (4));
    if (((unsigned int)(a1)) < 0x1000ULL) goto loc_002E71B0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx - 8))) ^ ((unsigned int)(v_rbx - 8)));
    v_r14 = (unsigned int)((v_r14) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip + 11801650))));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx - 8))) - ((unsigned int)(v_rdi)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (16));
    result = (unsigned int)((result) << (4));
    result = (unsigned int)((result) - ((unsigned int)(v_rdi)));
    result = (unsigned int)((result) + ((unsigned int)(v_rbx - 8)));
    a4 = (unsigned int)((v_r15 + 4127) & (0xFFFFF000ULL));
    result = (unsigned int)((result) & (0xFFFFF000ULL));
    if (((unsigned int)(a4)) < ((unsigned int)(result))) goto loc_002E702D;
loc_002E6FCB:
    a1 = (unsigned int)((*(unsigned __int8 *)(v_r13 + 5)) & (1));
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_002E7118;
    result = (*(unsigned __int64 *)(v_rbx)) ^ (v_rbx);
    v_rbx = *(unsigned __int64 *)(v_rbx);
    if ((unsigned int)(a1) != 0) { v_rbx = result; }
    if ((*(unsigned __int64 *)(v_rbx + 8)) == 0) goto loc_002E6EB0;
loc_002E6FFC:
    if ((unsigned int)(a1) == 0) goto loc_002E700D;
    if (*(unsigned __int64 *)(v_rbx + 8) != 0) goto loc_002E7350;
loc_002E700D:
loc_002E7010:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8)) == 0) goto loc_002E6EB0;
    goto loc_002E6FFC;
loc_002E701D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) ^ (*(unsigned int *)(v_rdi + 8)));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    goto loc_002E6F3C;
loc_002E702D:
    result = (unsigned int)((result) - 1);
    a4 = (unsigned int)((a4) >> (12));
    result = (result) >> (12);
    a1 = (unsigned __int8)((63) - ((unsigned __int8)(result)));
    a2 = (-1) >> ((unsigned __int8)(a1));
    result = (-1) << ((unsigned __int8)((unsigned __int8)(a4)));
    a2 = (a2) & (result);
    a2 = (a2) & (*(unsigned __int64 *)(v_rdi + 16));
    if (condition_is_equal) goto loc_002E6FCB;
    result = RtlpHpVsFreeChunkRemove(v_r13, v_r10, v_rdi, v_rbx - 8);
    result = (*(unsigned __int64 *)(v_rip + 11801221)) >> (32);
    result = (unsigned int)((result) >> (16));
    v_stack_p90 = 0;
    v_r15 = (unsigned int)((v_r15) >> (12));
    v_stack_p94 = 0x10000ULL;
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(v_rbx - 8)));
    a1 = (a18) >> (32);
    a1 = (unsigned int)((a1) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    result = (v_rbx - 8) >> (32);
    result = (unsigned int)((result) >> (16));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_rbx - 8 + 6) = (unsigned __int8)(a1);
    v_r15 = (unsigned int)((v_r15) ^ (*(unsigned int *)(v_rip + 11801128)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 8)) = (unsigned int)((unsigned __int8)(v_r15));
    v_stack_p28 = a8;
    v_stack_p20 = 1;
    result = RtlpHpVsChunkFree(v_r13, a19, v_rdi, v_rbx - 8);
    if (result == 0) goto loc_002E723F;
    if ((*(unsigned __int64 *)(a7)) == a6) goto loc_002E722B;
loc_002E7111:
loc_002E7118:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 16)) & (-4);
    if (3 == 0) goto loc_002E712D;
loc_002E712D:
    if (result == 0) goto loc_002E6EB0;
loc_002E7140:
    if (3 == 0) goto loc_002E7151;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_002E732F;
loc_002E7151:
    if ((*(unsigned __int64 *)(result + 8)) == v_rdi) goto loc_002E6EB0;
    result = (*(unsigned __int64 *)(result + 16)) & (-4);
    if (3 == 0) goto loc_002E7172;
    if (result != 0) goto loc_002E7337;
loc_002E7172:
loc_002E7175:
    if (result == 0) goto loc_002E6EB0;
    goto loc_002E7140;
loc_002E7180:
    a2 = 0;
    goto loc_002E6F3C;
loc_002E7187:
    v_stack_p28 = 0;
    a2 = (v_r13) ^ (*(unsigned __int64 *)(v_r13 + 8));
    v_stack_p20 = 0;
    result = RtlpLogHeapFailure(18, a2, v_rdi, v_rbx - 8);
loc_002E71B0:
    if (((*(unsigned __int8 *)(v_r13 + 5)) & (1)) == 0) {
        a1 = *(unsigned __int8 *)(v_r13 + 3);
        a2 = a8;
        result = RtlpHpReleaseQueuedLockExclusive(a1, a2, v_rdi, v_rbx - 8);
    }
    if (a6 == a6) goto loc_002E7209;
    if ((*(unsigned __int64 *)(a6 + 8)) != a6) goto loc_002E7111;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a6) + 8)) != a6) goto loc_002E7111;
    v_stack_p30 = *(unsigned __int64 *)(a6);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a6) + 8) = a6;
    result = RtlpHpVsSubsegmentFree(v_r13, a6, v_rdi, v_rbx - 8);
    goto loc_002E71C6;
loc_002E7209:
    v_rsp = (v_rsp) + (104);
    return result;
loc_002E722B:
    *(unsigned __int64 *)(result + 8) = v_r13;
    *(unsigned __int64 *)(result) = a6;
    *(unsigned __int64 *)(v_r13) = result;
    v_stack_pC0 = result;
loc_002E723F:
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(v_r13 + 6))) == 0) goto loc_002E7326;
loc_002E7252:
    if (*(unsigned __int64 *)((__int16)(*(unsigned __int16 *)(v_r13 + 6)) + v_r13 * 1 + 32) == 0) goto loc_002E71B0;
    v_r14 = (unsigned int)((v_r14) + 1);
    a4 = (unsigned int)((*(unsigned __int64 *)(v_r12 + 8)) & (1));
    if (condition_is_not_equal) goto loc_002E733F;
loc_002E7274:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(*(unsigned __int64 *)(v_r12 + 8))))) & (1));
    a2 = 0;
loc_002E7280:
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_002E72CF;
    result = (unsigned int)((*(unsigned __int64 *)(v_r12) - 8) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_r12) - 8)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11800687)));
    if (((unsigned int)(v_r14)) < ((unsigned int)(result))) goto loc_002E72BB;
    if (((unsigned int)(v_r14)) <= ((unsigned int)(result))) goto loc_002E72AE;
    if ((unsigned int)(a1) == 0) goto loc_002E72A9;
loc_002E72A9:
    goto loc_002E7280;
loc_002E72AE:
    goto loc_002E6EA5;
loc_002E72BB:
    if ((unsigned int)(a1) == 0) goto loc_002E72A9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) == 0) goto loc_002E72A9;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)));
    goto loc_002E7280;
loc_002E72CF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8) != 0) goto loc_002E6EB0;
    v_rbx = 0;
    if (a4 != 0) goto loc_002E7358;
loc_002E72F4:
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_002E7319;
    a3 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r12 + 8))) & (1));
loc_002E7300:
    if ((unsigned __int8)(a3) == 0) goto loc_002E7311;
loc_002E7311:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8) != 0) goto loc_002E7300;
loc_002E7319:
    goto loc_002E6EB0;
loc_002E7326:
    goto loc_002E7252;
loc_002E732F:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12) + 8)) ^ (*(unsigned __int64 *)(v_r12));
    goto loc_002E7151;
loc_002E7337:
    v_rbx = (*(unsigned __int64 *)(v_r12)) ^ (result);
    goto loc_002E7175;
loc_002E733F:
    if (v_rbx == 0) goto loc_002E7274;
    v_rbx = (v_rbx) ^ (v_r12);
    goto loc_002E7274;
loc_002E7350:
    v_rbx = (v_rbx) ^ (result);
    goto loc_002E7010;
loc_002E7358:
    if (result == 0) goto loc_002E7319;
    result = (result) ^ (v_r12);
    goto loc_002E72F4;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E6E90(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, int64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, int64_t Arg18, int64_t Arg19, int64_t Arg20, int64_t Arg21)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p60;
    uint64_t v_stack_p90;
    uint32_t v_stack_p94;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pC0;

    v_stack_pA0 = local_rsi;
    v_stack_pA8 = local_rdi;
    v_stack_p60 = local_r15;
loc_002E6EA5:
loc_002E6EB0:
    if (local_rbx == 0) goto loc_002E71B0;
    Arg2 = (local_rbx - 8) ^ (*(uint64_t *)(local_rbx - 0x8));
    Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0xB41432));
    Arg2 = (Arg2) >> (32);
    if ((((uint32_t)(Arg2)) & (0xFF0000ULL)) != 0) goto loc_002E6F32;
    if ((uint16_t)(Arg2) == 0) goto loc_002E7180;
    result = ((uint16_t)(Arg2)) << (4);
    local_rdi = (local_rbx - 8) - (result);
    Arg2 = (local_rdi) ^ (*(uint64_t *)(v_rip + 0xB41432));
    Arg2 = (Arg2) ^ (*(uint64_t *)(local_rdi));
    Arg2 = (Arg2) >> (32);
    if ((((uint32_t)(Arg2)) & (0xFF0000ULL)) != 0) goto loc_002E701D;
    if ((uint16_t)(Arg2) == 0) goto loc_002E7180;
    result = ((uint16_t)(Arg2)) << (4);
    local_rdi = (local_rdi) - (result);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) ^ (*(uint32_t *)(local_rdi + 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41432))));
    goto loc_002E6F3C;
loc_002E6F32:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx - 8))) ^ (*(uint32_t *)(local_rbx)));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41432))));
loc_002E6F3C:
    Arg1 = (*(uint64_t *)(local_rbx - 0x8)) ^ (*(uint64_t *)(v_rip + 0xB41432));
    Arg2 = (uint32_t)(((uint8_t)(result)) << (12));
    Arg1 = (Arg1) ^ (local_rbx - 8);
    local_rdi = (local_rdi) - ((uint32_t)((uint32_t)(Arg2)));
    Arg1 = (Arg1) >> (32);
    local_rdi = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    if ((((uint32_t)(Arg1)) & (0xFF0000ULL)) != 0) goto loc_002E7187;
    Arg1 = (uint16_t)((*(uint16_t *)(local_rdi + 0x24)) ^ (*(uint16_t *)(local_rdi + 0x20)));
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)((uint32_t)(0x2BEDULL))));
    if ((((uint16_t)((uint32_t)(0x7FFFULL))) & ((uint16_t)(Arg1))) != 0) goto loc_002E7187;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx - 0x8))))) ^ ((uint32_t)(local_rbx - 8)));
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB4137E))));
    Arg1 = (uint32_t)((Arg1) << (4));
    if (((uint32_t)(Arg1)) < 0x1000ULL) goto loc_002E71B0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx - 0x8))) ^ ((uint32_t)(local_rbx - 8)));
    local_r14 = (uint32_t)((local_r14) ^ ((uint32_t)(*(uint64_t *)(v_rip + 0xB41432))));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx - 8))) - ((uint32_t)(local_rdi)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (16));
    result = (uint32_t)((result) << (4));
    result = (uint32_t)((result) - ((uint32_t)(local_rdi)));
    result = (uint32_t)((result) + ((uint32_t)(local_rbx - 8)));
    Arg4 = (uint32_t)((local_r15 + 4127) & (0xFFFFF000ULL));
    result = (uint32_t)((result) & (0xFFFFF000ULL));
    if (((uint32_t)(Arg4)) < ((uint32_t)(result))) goto loc_002E702D;
loc_002E6FCB:
    Arg1 = (uint32_t)((*(uint8_t *)(local_r13 + 0x5)) & (1));
    if (*(uint64_t *)(local_rbx) == 0) goto loc_002E7118;
    result = (*(uint64_t *)(local_rbx)) ^ (local_rbx);
    local_rbx = *(uint64_t *)(local_rbx);
    if ((uint32_t)(Arg1) != 0) { local_rbx = result; }
    if ((*(uint64_t *)(local_rbx + 0x8)) == 0) goto loc_002E6EB0;
loc_002E6FFC:
    if ((uint32_t)(Arg1) == 0) goto loc_002E700D;
    if (*(uint64_t *)(local_rbx + 0x8) != 0) goto loc_002E7350;
loc_002E700D:
loc_002E7010:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8)) == 0) goto loc_002E6EB0;
    goto loc_002E6FFC;
loc_002E701D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) ^ (*(uint32_t *)(local_rdi + 0x8)));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    goto loc_002E6F3C;
loc_002E702D:
    result = (uint32_t)((result) - 1);
    Arg4 = (uint32_t)((Arg4) >> (12));
    result = (result) >> (12);
    Arg1 = (uint8_t)((63) - ((uint8_t)(result)));
    Arg2 = (-1) >> ((uint8_t)(Arg1));
    result = (-1) << ((uint8_t)((uint8_t)(Arg4)));
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) & (*(uint64_t *)(local_rdi + 0x10));
    if (condition_is_equal) goto loc_002E6FCB;
    result = RtlpHpVsFreeChunkRemove(local_r13, local_r10, local_rdi, local_rbx - 8);
    result = (*(uint64_t *)(v_rip + 0xB41285)) >> (32);
    result = (uint32_t)((result) >> (16));
    v_stack_p90 = 0;
    local_r15 = (uint32_t)((local_r15) >> (12));
    v_stack_p94 = 0x10000ULL;
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(local_rbx - 8)));
    Arg1 = (Arg18) >> (32);
    Arg1 = (uint32_t)((Arg1) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    result = (local_rbx - 8) >> (32);
    result = (uint32_t)((result) >> (16));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    *(uint8_t *)(local_rbx - 0x8 + 0x6) = (uint8_t)(Arg1);
    local_r15 = (uint32_t)((local_r15) ^ (*(uint32_t *)(v_rip + 0xB41228)));
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x8)) = (uint32_t)((uint8_t)(local_r15));
    v_stack_p28 = Arg8;
    v_stack_p20 = 1;
    result = RtlpHpVsChunkFree(local_r13, Arg19, local_rdi, local_rbx - 8);
    if (result == 0) goto loc_002E723F;
    if ((*(uint64_t *)(arg7)) == Arg6) goto loc_002E722B;
loc_002E7111:
loc_002E7118:
    result = (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x10)) & (-4);
    if (3 == 0) goto loc_002E712D;
loc_002E712D:
    if (result == 0) goto loc_002E6EB0;
loc_002E7140:
    if (3 == 0) goto loc_002E7151;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_002E732F;
loc_002E7151:
    if ((*(uint64_t *)(result + 0x8)) == local_rdi) goto loc_002E6EB0;
    result = (*(uint64_t *)(result + 0x10)) & (-4);
    if (3 == 0) goto loc_002E7172;
    if (result != 0) goto loc_002E7337;
loc_002E7172:
loc_002E7175:
    if (result == 0) goto loc_002E6EB0;
    goto loc_002E7140;
loc_002E7180:
    Arg2 = 0;
    goto loc_002E6F3C;
loc_002E7187:
    v_stack_p28 = 0;
    Arg2 = (local_r13) ^ (*(uint64_t *)(local_r13 + 0x8));
    v_stack_p20 = 0;
    result = RtlpLogHeapFailure(18, Arg2, local_rdi, local_rbx - 8);
loc_002E71B0:
    if (((*(uint8_t *)(local_r13 + 0x5)) & (1)) == 0) {
        Arg1 = *(uint8_t *)(local_r13 + 0x3);
        Arg2 = Arg8;
        result = RtlpHpReleaseQueuedLockExclusive(Arg1, Arg2, local_rdi, local_rbx - 8);
    }
    if (Arg6 == Arg6) goto loc_002E7209;
    if ((*(uint64_t *)(Arg6 + 0x8)) != Arg6) goto loc_002E7111;
    if ((*(uint64_t *)(*(uint64_t *)(Arg6) + 0x8)) != Arg6) goto loc_002E7111;
    v_stack_p30 = *(uint64_t *)(Arg6);
    *(uint64_t *)(*(uint64_t *)(Arg6) + 0x8) = Arg6;
    result = RtlpHpVsSubsegmentFree(local_r13, Arg6, local_rdi, local_rbx - 8);
    goto loc_002E71C6;
loc_002E7209:
    local_rsp = (local_rsp) + (104);
    return result;
loc_002E722B:
    *(uint64_t *)(result + 0x8) = local_r13;
    *(uint64_t *)(result) = Arg6;
    *(uint64_t *)(local_r13) = result;
    v_stack_pC0 = result;
loc_002E723F:
    if ((uint16_t)((int16_t)(*(uint16_t *)(local_r13 + 0x6))) == 0) goto loc_002E7326;
loc_002E7252:
    if (*(uint64_t *)((int16_t)(*(uint16_t *)(local_r13 + 0x6)) + local_r13 * 1 + 0x20) == 0) goto loc_002E71B0;
    local_r14 = (uint32_t)((local_r14) + 1);
    Arg4 = (uint32_t)((*(uint64_t *)(local_r12 + 0x8)) & (1));
    if (condition_is_not_equal) goto loc_002E733F;
loc_002E7274:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(*(uint64_t *)(local_r12 + 0x8))))) & (1));
    Arg2 = 0;
loc_002E7280:
    if (*(uint64_t *)(local_r12) == 0) goto loc_002E72CF;
    result = (uint32_t)((*(uint64_t *)(local_r12) - 8) ^ (*(uint32_t *)(*(uint64_t *)(local_r12) - 0x8)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB4106F)));
    if (((uint32_t)(local_r14)) < ((uint32_t)(result))) goto loc_002E72BB;
    if (((uint32_t)(local_r14)) <= ((uint32_t)(result))) goto loc_002E72AE;
    if ((uint32_t)(Arg1) == 0) goto loc_002E72A9;
loc_002E72A9:
    goto loc_002E7280;
loc_002E72AE:
    goto loc_002E6EA5;
loc_002E72BB:
    if ((uint32_t)(Arg1) == 0) goto loc_002E72A9;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) == 0) goto loc_002E72A9;
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)));
    goto loc_002E7280;
loc_002E72CF:
    if (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8) != 0) goto loc_002E6EB0;
    local_rbx = 0;
    if (Arg4 != 0) goto loc_002E7358;
loc_002E72F4:
    if (*(uint64_t *)(local_r12) == 0) goto loc_002E7319;
    Arg3 = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r12 + 0x8))) & (1));
loc_002E7300:
    if ((uint8_t)(Arg3) == 0) goto loc_002E7311;
loc_002E7311:
    if (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8) != 0) goto loc_002E7300;
loc_002E7319:
    goto loc_002E6EB0;
loc_002E7326:
    goto loc_002E7252;
loc_002E732F:
    result = (*(uint64_t *)(*(uint64_t *)(local_r12) + 0x8)) ^ (*(uint64_t *)(local_r12));
    goto loc_002E7151;
loc_002E7337:
    local_rbx = (*(uint64_t *)(local_r12)) ^ (result);
    goto loc_002E7175;
loc_002E733F:
    if (local_rbx == 0) goto loc_002E7274;
    local_rbx = (local_rbx) ^ (local_r12);
    goto loc_002E7274;
loc_002E7350:
    local_rbx = (local_rbx) ^ (result);
    goto loc_002E7010;
loc_002E7358:
    if (result == 0) goto loc_002E7319;
    result = (result) ^ (local_r12);
    goto loc_002E72F4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E6E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
