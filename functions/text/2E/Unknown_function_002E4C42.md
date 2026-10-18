# sub_002E4C42

- RVA: `0x002E4C42`–`0x002E54EE` (길이 `2,220` bytes)
- VA: `0x00000001402E4C42`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071104`
- 디코드: `596`개 명령, `2,220/2,220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **50**
  - `0x002E4C97` → [sub_002E5502](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4CB1` → [sub_002E5502 + 0x8](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4CCE` → [sub_002E5502 + 0x55](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4CE3` → [sub_002E5502 + 0x1CA](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4CFE` → [sub_002E5502 + 0x1BA](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4D06` → [sub_002E5502 + 0x1E7](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4D6F` → [sub_002E5502 + 0x5D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4D88` → [sub_002E5502 + 0x38](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4DAD` → [sub_002E5502 + 0x18](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4DEB` → [sub_002E5502 + 0xAD](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E25` → [sub_002E5502 + 0x165](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E2D` → [sub_002E5502 + 0x122](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E5D` → [sub_002E5502 + 0x16D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E6D` → [sub_002E5502 + 0x13B](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E83` → [sub_002E5502 + 0x178](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4E91` → [sub_002E5502 + 0x180](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4EBB` → [sub_002E5502 + 0xB5](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4ECE` → [sub_002E5502 + 0x12A](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4EE3` → [sub_002E5502 + 0x216](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4F42` → [sub_002E5502 + 0x20](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4F76` → [sub_002E5502 + 0x28](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E4F97` → [sub_002E5502 + 0x1B2](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E503E` → [sub_002E5502 + 0x75](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5054` → [sub_002E5502 + 0x224](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E50CC` → [sub_002E5502 + 0x65](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E50F6` → [sub_002E5502 + 0x6D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5129` → [sub_002E5502 + 0x43](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5196` → [sub_002E5502 + 0x30](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E51EF` → [sub_002E5502 + 0x10](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5201` → [sub_002E5502 + 0x22C](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E529C` → [sub_002E5502 + 0x95](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E52BD` → [sub_002E5502 + 0x3B1](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E52D7` → [sub_002E5502 + 0x23F](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E52E0` → [sub_002E5502 + 0x23C](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E52F2` → [sub_002E5502 + 0x276](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5310` → [sub_002E5502 + 0x7D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E532D` → [sub_002E5502 + 0x8D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E534D` → [sub_002E5502 + 0x85](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E535F` → [sub_002E5502 + 0x234](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E53AC` → [sub_002E5502 + 0x9D](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E53D2` → [sub_002E5502 + 0xA5](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E53F3` → [sub_002E5502 + 0x451](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E540E` → [sub_002E5502 + 0x3CE](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E542D` → [sub_002E5502 + 0x3C6](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E543F` → [sub_002E5502 + 0x42B](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5452` → [sub_002E5502 + 0x446](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5470` → [sub_002E5502 + 0x3D9](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5479` → [sub_002E5502 + 0x3D6](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E5487` → [sub_002E5502 + 0x434](Unknown_function_002E5502.md) (`tail-transfer`)
  - `0x002E549A` → [sub_002E5502 + 0x41F](Unknown_function_002E5502.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E4C42  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
002E4C47  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
002E4C4C  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
002E4C51  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002E4C56  4C 89 64 24 18                  mov qword ptr [rsp + 0x18], r12
002E4C5B  4C 89 6C 24 10                  mov qword ptr [rsp + 0x10], r13
002E4C60  4C 89 74 24 08                  mov qword ptr [rsp + 8], r14
002E4C65  4C 89 3C 24                     mov qword ptr [rsp], r15
002E4C69  48 85 C0                        test rax, rax
002E4C6C  75 08                           jne 0x1402e4c76
002E4C6E  49 8B C0                        mov rax, r8
002E4C71  49 8B F8                        mov rdi, r8
002E4C74  EB 0C                           jmp 0x1402e4c82
002E4C76  48 8B F8                        mov rdi, rax
002E4C79  4D 85 C0                        test r8, r8
002E4C7C  0F 85 C3 00 00 00               jne 0x1402e4d45
002E4C82  4D 8B 4A 10                     mov r9, qword ptr [r10 + 0x10]
002E4C86  44 0F B6 C2                     movzx r8d, dl
002E4C8A  49 83 E1 FC                     and r9, 0xfffffffffffffffc
002E4C8E  41 80 E0 01                     and r8b, 1
002E4C92  74 09                           je 0x1402e4c9d
002E4C94  4D 85 C9                        test r9, r9
002E4C97  0F 85 65 08 00 00               jne 0x1402e5502
002E4C9D  49 8B DA                        mov rbx, r10
002E4CA0  4D 85 C9                        test r9, r9
002E4CA3  74 74                           je 0x1402e4d19
002E4CA5  49 8B 49 08                     mov rcx, qword ptr [r9 + 8]
002E4CA9  45 84 C0                        test r8b, r8b
002E4CAC  74 09                           je 0x1402e4cb7
002E4CAE  48 85 C9                        test rcx, rcx
002E4CB1  0F 85 53 08 00 00               jne 0x1402e550a
002E4CB7  45 33 FF                        xor r15d, r15d
002E4CBA  49 3B CA                        cmp rcx, r10
002E4CBD  0F 84 31 02 00 00               je 0x1402e4ef4
002E4CC3  49 8B 09                        mov rcx, qword ptr [r9]
002E4CC6  F6 C2 01                        test dl, 1
002E4CC9  74 09                           je 0x1402e4cd4
002E4CCB  48 85 C9                        test rcx, rcx
002E4CCE  0F 85 83 08 00 00               jne 0x1402e5557
002E4CD4  49 3B CA                        cmp rcx, r10
002E4CD7  75 65                           jne 0x1402e4d3e
002E4CD9  49 8B 4B 08                     mov rcx, qword ptr [r11 + 8]
002E4CDD  41 8B EF                        mov ebp, r15d
002E4CE0  F6 C1 01                        test cl, 1
002E4CE3  0F 85 E3 09 00 00               jne 0x1402e56cc
002E4CE9  4C 8B C1                        mov r8, rcx
002E4CEC  0F B6 D1                        movzx edx, cl
002E4CEF  4D 3B C2                        cmp r8, r10
002E4CF2  0F 85 01 02 00 00               jne 0x1402e4ef9
002E4CF8  80 E1 01                        and cl, 1
002E4CFB  48 85 C0                        test rax, rax
002E4CFE  0F 85 B8 09 00 00               jne 0x1402e56bc
002E4D04  84 C9                           test cl, cl
002E4D06  0F 85 DD 09 00 00               jne 0x1402e56e9
002E4D0C  4D 89 4B 08                     mov qword ptr [r11 + 8], r9
002E4D10  41 0F B6 D1                     movzx edx, r9b
002E4D14  E9 E0 01 00 00                  jmp 0x1402e4ef9
002E4D19  45 33 FF                        xor r15d, r15d
002E4D1C  48 85 C0                        test rax, rax
002E4D1F  74 04                           je 0x1402e4d25
002E4D21  4C 89 78 10                     mov qword ptr [rax + 0x10], r15
002E4D25  49 8B 4B 08                     mov rcx, qword ptr [r11 + 8]
002E4D29  49 8B 13                        mov rdx, qword ptr [r11]
002E4D2C  F6 C1 01                        test cl, 1
002E4D2F  0F 85 2B 03 00 00               jne 0x1402e5060
002E4D35  49 3B D2                        cmp rdx, r10
002E4D38  0F 84 93 02 00 00               je 0x1402e4fd1
002E4D3E  B9 1D 00 00 00                  mov ecx, 0x1d
002E4D43  CD 29                           int 0x29
002E4D45  49 8B 08                        mov rcx, qword ptr [r8]
002E4D48  45 33 FF                        xor r15d, r15d
002E4D4B  49 8B D8                        mov rbx, r8
002E4D4E  4D 8B C8                        mov r9, r8
002E4D51  BD 01 00 00 00                  mov ebp, 1
002E4D56  48 85 C9                        test rcx, rcx
002E4D59  74 25                           je 0x1402e4d80
002E4D5B  0F B6 FA                        movzx edi, dl
002E4D5E  40 22 FD                        and dil, bpl
002E4D61  41 8B EF                        mov ebp, r15d
002E4D64  4C 8B CB                        mov r9, rbx
002E4D67  40 84 FF                        test dil, dil
002E4D6A  74 09                           je 0x1402e4d75
002E4D6C  48 85 C9                        test rcx, rcx
002E4D6F  0F 85 EA 07 00 00               jne 0x1402e555f
002E4D75  48 8B D9                        mov rbx, rcx
002E4D78  48 8B 0B                        mov rcx, qword ptr [rbx]
002E4D7B  48 85 C9                        test rcx, rcx
002E4D7E  75 E4                           jne 0x1402e4d64
002E4D80  F6 C2 01                        test dl, 1
002E4D83  74 09                           je 0x1402e4d8e
002E4D85  48 85 C0                        test rax, rax
002E4D88  0F 85 AC 07 00 00               jne 0x1402e553a
002E4D8E  48 8B C8                        mov rcx, rax
002E4D91  48 89 0B                        mov qword ptr [rbx], rcx
002E4D94  48 8B 78 10                     mov rdi, qword ptr [rax + 0x10]
002E4D98  41 0F B6 73 08                  movzx esi, byte ptr [r11 + 8]
002E4D9D  48 8B CF                        mov rcx, rdi
002E4DA0  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E4DA4  40 80 E6 01                     and sil, 1
002E4DA8  74 09                           je 0x1402e4db3
002E4DAA  48 85 C9                        test rcx, rcx
002E4DAD  0F 85 67 07 00 00               jne 0x1402e551a
002E4DB3  49 3B CA                        cmp rcx, r10
002E4DB6  75 86                           jne 0x1402e4d3e
002E4DB8  48 8B CB                        mov rcx, rbx
002E4DBB  48 8B D3                        mov rdx, rbx
002E4DBE  48 33 C8                        xor rcx, rax
002E4DC1  40 84 F6                        test sil, sil
002E4DC4  48 0F 45 D1                     cmovne rdx, rcx
002E4DC8  83 E7 03                        and edi, 3
002E4DCB  48 0B FA                        or rdi, rdx
002E4DCE  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
002E4DD2  49 8B 50 10                     mov rdx, qword ptr [r8 + 0x10]
002E4DD6  41 0F B6 7B 08                  movzx edi, byte ptr [r11 + 8]
002E4DDB  48 8B C2                        mov rax, rdx
002E4DDE  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E4DE2  40 80 E7 01                     and dil, 1
002E4DE6  74 09                           je 0x1402e4df1
002E4DE8  48 85 C0                        test rax, rax
002E4DEB  0F 85 BE 07 00 00               jne 0x1402e55af
002E4DF1  49 3B C2                        cmp rax, r10
002E4DF4  0F 85 44 FF FF FF               jne 0x1402e4d3e
002E4DFA  48 8B CB                        mov rcx, rbx
002E4DFD  48 8B C3                        mov rax, rbx
002E4E00  49 33 C8                        xor rcx, r8
002E4E03  40 84 FF                        test dil, dil
002E4E06  48 0F 45 C1                     cmovne rax, rcx
002E4E0A  83 E2 03                        and edx, 3
002E4E0D  48 0B D0                        or rdx, rax
002E4E10  49 89 50 10                     mov qword ptr [r8 + 0x10], rdx
002E4E14  41 0F B6 4B 08                  movzx ecx, byte ptr [r11 + 8]
002E4E19  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002E4E1D  80 E1 01                        and cl, 1
002E4E20  74 09                           je 0x1402e4e2b
002E4E22  48 85 C0                        test rax, rax
002E4E25  0F 85 3C 08 00 00               jne 0x1402e5667
002E4E2B  84 C9                           test cl, cl
002E4E2D  0F 84 F1 07 00 00               je 0x1402e5624
002E4E33  48 8B CB                        mov rcx, rbx
002E4E36  49 33 C8                        xor rcx, r8
002E4E39  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
002E4E3D  4C 8B E8                        mov r13, rax
002E4E40  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
002E4E44  48 8B CF                        mov rcx, rdi
002E4E47  41 0F B6 53 08                  movzx edx, byte ptr [r11 + 8]
002E4E4C  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E4E50  44 0F B6 F2                     movzx r14d, dl
002E4E54  41 80 E6 01                     and r14b, 1
002E4E58  74 09                           je 0x1402e4e63
002E4E5A  48 85 C9                        test rcx, rcx
002E4E5D  0F 85 0C 08 00 00               jne 0x1402e566f
002E4E63  48 8B F1                        mov rsi, rcx
002E4E66  44 0F B6 C7                     movzx r8d, dil
002E4E6A  49 3B F1                        cmp rsi, r9
002E4E6D  0F 85 CA 07 00 00               jne 0x1402e563d
002E4E73  49 8B 4A 10                     mov rcx, qword ptr [r10 + 0x10]
002E4E77  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E4E7B  F6 C2 01                        test dl, 1
002E4E7E  74 17                           je 0x1402e4e97
002E4E80  48 85 C9                        test rcx, rcx
002E4E83  0F 85 F1 07 00 00               jne 0x1402e567a
002E4E89  F6 C2 01                        test dl, 1
002E4E8C  74 09                           je 0x1402e4e97
002E4E8E  48 85 C9                        test rcx, rcx
002E4E91  0F 85 EB 07 00 00               jne 0x1402e5682
002E4E97  8B 53 10                        mov edx, dword ptr [rbx + 0x10]
002E4E9A  83 E2 03                        and edx, 3
002E4E9D  48 0B D1                        or rdx, rcx
002E4EA0  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
002E4EA4  0F B6 CA                        movzx ecx, dl
002E4EA7  41 32 4A 10                     xor cl, byte ptr [r10 + 0x10]
002E4EAB  80 E1 01                        and cl, 1
002E4EAE  32 CA                           xor cl, dl
002E4EB0  88 4B 10                        mov byte ptr [rbx + 0x10], cl
002E4EB3  49 8B 7A 10                     mov rdi, qword ptr [r10 + 0x10]
002E4EB7  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
002E4EBB  0F 85 F6 06 00 00               jne 0x1402e55b7
002E4EC1  49 8B 53 08                     mov rdx, qword ptr [r11 + 8]
002E4EC5  49 8B 3B                        mov rdi, qword ptr [r11]
002E4EC8  48 8B CA                        mov rcx, rdx
002E4ECB  F6 C2 01                        test dl, 1
002E4ECE  0F 85 58 07 00 00               jne 0x1402e562c
002E4ED4  49 3B FA                        cmp rdi, r10
002E4ED7  0F 85 61 FE FF FF               jne 0x1402e4d3e
002E4EDD  4D 8B D3                        mov r10, r11
002E4EE0  F6 C1 01                        test cl, 1
002E4EE3  0F 85 2F 08 00 00               jne 0x1402e5718
002E4EE9  0F B6 D1                        movzx edx, cl
002E4EEC  49 89 1B                        mov qword ptr [r11], rbx
002E4EEF  48 8B CB                        mov rcx, rbx
002E4EF2  EB 0A                           jmp 0x1402e4efe
002E4EF4  BD 01 00 00 00                  mov ebp, 1
002E4EF9  45 0F B6 42 10                  movzx r8d, byte ptr [r10 + 0x10]
002E4EFE  41 80 E0 01                     and r8b, 1
002E4F02  F6 C2 01                        test dl, 1
002E4F05  74 09                           je 0x1402e4f10
002E4F07  48 85 C0                        test rax, rax
002E4F0A  0F 85 0D 01 00 00               jne 0x1402e501d
002E4F10  8B CD                           mov ecx, ebp
002E4F12  49 89 04 C9                     mov qword ptr [r9 + rcx*8], rax
002E4F16  48 85 C0                        test rax, rax
002E4F19  0F 85 0A 01 00 00               jne 0x1402e5029
002E4F1F  45 84 C0                        test r8b, r8b
002E4F22  0F 85 C8 00 00 00               jne 0x1402e4ff0
002E4F28  41 0F B6 4B 08                  movzx ecx, byte ptr [r11 + 8]
002E4F2D  49 8B F9                        mov rdi, r9
002E4F30  8B C5                           mov eax, ebp
002E4F32  48 83 F0 01                     xor rax, 1
002E4F36  49 8B 14 C1                     mov rdx, qword ptr [r9 + rax*8]
002E4F3A  F6 C1 01                        test cl, 1
002E4F3D  74 09                           je 0x1402e4f48
002E4F3F  48 85 D2                        test rdx, rdx
002E4F42  0F 85 DA 05 00 00               jne 0x1402e5522
002E4F48  F6 42 10 01                     test byte ptr [rdx + 0x10], 1
002E4F4C  0F 84 4A 02 00 00               je 0x1402e519c
002E4F52  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
002E4F56  49 8B 1B                        mov rbx, qword ptr [r11]
002E4F59  A8 01                           test al, 1
002E4F5B  0F 85 10 01 00 00               jne 0x1402e5071
002E4F61  44 0F B6 C0                     movzx r8d, al
002E4F65  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
002E4F69  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E4F6D  41 83 E0 01                     and r8d, 1
002E4F71  74 09                           je 0x1402e4f7c
002E4F73  48 85 C0                        test rax, rax
002E4F76  0F 85 AE 05 00 00               jne 0x1402e552a
002E4F7C  49 3B C1                        cmp rax, r9
002E4F7F  0F 85 B9 FD FF FF               jne 0x1402e4d3e
002E4F85  8B C5                           mov eax, ebp
002E4F87  48 83 F0 01                     xor rax, 1
002E4F8B  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
002E4F8F  45 85 C0                        test r8d, r8d
002E4F92  74 09                           je 0x1402e4f9d
002E4F94  48 85 C9                        test rcx, rcx
002E4F97  0F 85 17 07 00 00               jne 0x1402e56b4
002E4F9D  48 3B CA                        cmp rcx, rdx
002E4FA0  0F 85 98 FD FF FF               jne 0x1402e4d3e
002E4FA6  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
002E4FAA  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E4FAE  45 85 C0                        test r8d, r8d
002E4FB1  0F 84 00 01 00 00               je 0x1402e50b7
002E4FB7  48 85 C9                        test rcx, rcx
002E4FBA  0F 85 F4 00 00 00               jne 0x1402e50b4
002E4FC0  49 3B D9                        cmp rbx, r9
002E4FC3  0F 85 75 FD FF FF               jne 0x1402e4d3e
002E4FC9  48 8B DA                        mov rbx, rdx
002E4FCC  E9 1D 01 00 00                  jmp 0x1402e50ee
002E4FD1  F6 C1 01                        test cl, 1
002E4FD4  0F 85 BA 00 00 00               jne 0x1402e5094
002E4FDA  49 89 43 08                     mov qword ptr [r11 + 8], rax
002E4FDE  0F B6 D0                        movzx edx, al
002E4FE1  F6 C2 01                        test dl, 1
002E4FE4  0F 85 98 00 00 00               jne 0x1402e5082
002E4FEA  4C 8B FF                        mov r15, rdi
002E4FED  4D 89 3B                        mov qword ptr [r11], r15
002E4FF0  4C 8B 3C 24                     mov r15, qword ptr [rsp]
002E4FF4  4C 8B 74 24 08                  mov r14, qword ptr [rsp + 8]
002E4FF9  4C 8B 6C 24 10                  mov r13, qword ptr [rsp + 0x10]
002E4FFE  4C 8B 64 24 18                  mov r12, qword ptr [rsp + 0x18]
002E5003  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
002E5008  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
002E500D  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
002E5012  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
002E5017  48 83 C4 28                     add rsp, 0x28
002E501B  C3                              ret
002E501C  CC                              int3
002E501D  8B CD                           mov ecx, ebp
002E501F  49 8B D1                        mov rdx, r9
002E5022  48 33 D0                        xor rdx, rax
002E5025  49 89 14 C9                     mov qword ptr [r9 + rcx*8], rdx
002E5029  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
002E502D  41 0F B6 53 08                  movzx edx, byte ptr [r11 + 8]
002E5032  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E5036  80 E2 01                        and dl, 1
002E5039  74 09                           je 0x1402e5044
002E503B  48 85 C9                        test rcx, rcx
002E503E  0F 85 33 05 00 00               jne 0x1402e5577
002E5044  48 3B CB                        cmp rcx, rbx
002E5047  0F 85 F1 FC FF FF               jne 0x1402e4d3e
002E504D  84 D2                           test dl, dl
002E504F  74 09                           je 0x1402e505a
002E5051  4D 85 C9                        test r9, r9
002E5054  0F 85 CC 06 00 00               jne 0x1402e5726
002E505A  4C 89 48 10                     mov qword ptr [rax + 0x10], r9
002E505E  EB 90                           jmp 0x1402e4ff0
002E5060  48 85 D2                        test rdx, rdx
002E5063  0F 84 CC FC FF FF               je 0x1402e4d35
002E5069  49 33 D3                        xor rdx, r11
002E506C  E9 C4 FC FF FF                  jmp 0x1402e4d35
002E5071  48 85 DB                        test rbx, rbx
002E5074  0F 84 E7 FE FF FF               je 0x1402e4f61
002E507A  49 33 DB                        xor rbx, r11
002E507D  E9 DF FE FF FF                  jmp 0x1402e4f61
002E5082  48 8B C8                        mov rcx, rax
002E5085  49 33 CB                        xor rcx, r11
002E5088  48 85 C0                        test rax, rax
002E508B  4C 0F 45 F9                     cmovne r15, rcx
002E508F  E9 59 FF FF FF                  jmp 0x1402e4fed
002E5094  48 8B C8                        mov rcx, rax
002E5097  49 8B D7                        mov rdx, r15
002E509A  49 33 CB                        xor rcx, r11
002E509D  48 85 C0                        test rax, rax
002E50A0  48 0F 45 D1                     cmovne rdx, rcx
002E50A4  49 89 53 08                     mov qword ptr [r11 + 8], rdx
002E50A8  80 CA 01                        or dl, 1
002E50AB  41 88 53 08                     mov byte ptr [r11 + 8], dl
002E50AF  E9 2D FF FF FF                  jmp 0x1402e4fe1
002E50B4  49 33 C9                        xor rcx, r9
002E50B7  48 85 C9                        test rcx, rcx
002E50BA  0F 84 00 FF FF FF               je 0x1402e4fc0
002E50C0  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002E50C4  45 85 C0                        test r8d, r8d
002E50C7  74 09                           je 0x1402e50d2
002E50C9  48 85 C0                        test rax, rax
002E50CC  0F 85 95 04 00 00               jne 0x1402e5567
002E50D2  49 3B C1                        cmp rax, r9
002E50D5  0F 85 67 02 00 00               jne 0x1402e5342
002E50DB  45 85 C0                        test r8d, r8d
002E50DE  0F 84 B3 02 00 00               je 0x1402e5397
002E50E4  48 8B C1                        mov rax, rcx
002E50E7  48 33 C2                        xor rax, rdx
002E50EA  48 89 41 08                     mov qword ptr [rcx + 8], rax
002E50EE  45 85 C0                        test r8d, r8d
002E50F1  74 09                           je 0x1402e50fc
002E50F3  48 85 C9                        test rcx, rcx
002E50F6  0F 85 73 04 00 00               jne 0x1402e556f
002E50FC  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
002E50FF  83 E0 03                        and eax, 3
002E5102  48 0B C1                        or rax, rcx
002E5105  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
002E5109  8B C5                           mov eax, ebp
002E510B  48 8B 0C C2                     mov rcx, qword ptr [rdx + rax*8]
002E510F  45 85 C0                        test r8d, r8d
002E5112  0F 84 BB 00 00 00               je 0x1402e51d3
002E5118  48 85 C9                        test rcx, rcx
002E511B  0F 85 AF 00 00 00               jne 0x1402e51d0
002E5121  45 85 C0                        test r8d, r8d
002E5124  74 09                           je 0x1402e512f
002E5126  48 85 C9                        test rcx, rcx
002E5129  0F 85 16 04 00 00               jne 0x1402e5545
002E512F  8B C5                           mov eax, ebp
002E5131  48 83 F0 01                     xor rax, 1
002E5135  49 89 0C C1                     mov qword ptr [r9 + rax*8], rcx
002E5139  45 85 C0                        test r8d, r8d
002E513C  0F 84 47 02 00 00               je 0x1402e5389
002E5142  8B C5                           mov eax, ebp
002E5144  48 8B CA                        mov rcx, rdx
002E5147  49 33 C9                        xor rcx, r9
002E514A  48 89 0C C2                     mov qword ptr [rdx + rax*8], rcx
002E514E  48 8B CA                        mov rcx, rdx
002E5151  49 33 C9                        xor rcx, r9
002E5154  41 8B 41 10                     mov eax, dword ptr [r9 + 0x10]
002E5158  83 E0 03                        and eax, 3
002E515B  48 0B C1                        or rax, rcx
002E515E  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
002E5162  49 8B C3                        mov rax, r11
002E5165  41 F6 43 08 01                  test byte ptr [r11 + 8], 1
002E516A  0F 85 58 03 00 00               jne 0x1402e54c8
002E5170  48 8B CB                        mov rcx, rbx
002E5173  48 89 08                        mov qword ptr [rax], rcx
002E5176  80 62 10 FE                     and byte ptr [rdx + 0x10], 0xfe
002E517A  41 80 49 10 01                  or byte ptr [r9 + 0x10], 1
002E517F  41 0F B6 4B 08                  movzx ecx, byte ptr [r11 + 8]
002E5184  8B C5                           mov eax, ebp
002E5186  48 83 F0 01                     xor rax, 1
002E518A  49 8B 14 C1                     mov rdx, qword ptr [r9 + rax*8]
002E518E  F6 C1 01                        test cl, 1
002E5191  74 09                           je 0x1402e519c
002E5193  48 85 D2                        test rdx, rdx
002E5196  0F 85 96 03 00 00               jne 0x1402e5532
002E519C  48 8B 02                        mov rax, qword ptr [rdx]
002E519F  80 E1 01                        and cl, 1
002E51A2  48 85 C0                        test rax, rax
002E51A5  75 76                           jne 0x1402e521d
002E51A7  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002E51AB  48 85 C0                        test rax, rax
002E51AE  0F 85 BF 01 00 00               jne 0x1402e5373
002E51B4  41 0F B6 41 10                  movzx eax, byte ptr [r9 + 0x10]
002E51B9  A8 01                           test al, 1
002E51BB  0F 84 36 01 00 00               je 0x1402e52f7
002E51C1  24 FE                           and al, 0xfe
002E51C3  41 88 41 10                     mov byte ptr [r9 + 0x10], al
002E51C7  80 4A 10 01                     or byte ptr [rdx + 0x10], 1
002E51CB  E9 20 FE FF FF                  jmp 0x1402e4ff0
002E51D0  48 33 CA                        xor rcx, rdx
002E51D3  48 85 C9                        test rcx, rcx
002E51D6  0F 84 45 FF FF FF               je 0x1402e5121
002E51DC  4C 8B 51 10                     mov r10, qword ptr [rcx + 0x10]
002E51E0  49 8B C2                        mov rax, r10
002E51E3  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E51E7  45 85 C0                        test r8d, r8d
002E51EA  74 09                           je 0x1402e51f5
002E51EC  48 85 C0                        test rax, rax
002E51EF  0F 85 1D 03 00 00               jne 0x1402e5512
002E51F5  48 3B C2                        cmp rax, rdx
002E51F8  0F 85 40 FB FF FF               jne 0x1402e4d3e
002E51FE  45 85 C0                        test r8d, r8d
002E5201  0F 84 27 05 00 00               je 0x1402e572e
002E5207  48 8B C1                        mov rax, rcx
002E520A  49 33 C1                        xor rax, r9
002E520D  41 83 E2 03                     and r10d, 3
002E5211  4C 0B D0                        or r10, rax
002E5214  4C 89 51 10                     mov qword ptr [rcx + 0x10], r10
002E5218  E9 04 FF FF FF                  jmp 0x1402e5121
002E521D  84 C9                           test cl, cl
002E521F  74 03                           je 0x1402e5224
002E5221  48 33 C2                        xor rax, rdx
002E5224  F6 40 10 01                     test byte ptr [rax + 0x10], 1
002E5228  0F 84 79 FF FF FF               je 0x1402e51a7
002E522E  8B C5                           mov eax, ebp
002E5230  48 83 F0 01                     xor rax, 1
002E5234  4C 8B 04 C2                     mov r8, qword ptr [rdx + rax*8]
002E5238  84 C9                           test cl, cl
002E523A  74 0C                           je 0x1402e5248
002E523C  4D 85 C0                        test r8, r8
002E523F  0F 84 5A 01 00 00               je 0x1402e539f
002E5245  4C 33 C2                        xor r8, rdx
002E5248  4D 85 C0                        test r8, r8
002E524B  0F 84 4E 01 00 00               je 0x1402e539f
002E5251  41 F6 40 10 01                  test byte ptr [r8 + 0x10], 1
002E5256  0F 84 43 01 00 00               je 0x1402e539f
002E525C  0F B6 4A 10                     movzx ecx, byte ptr [rdx + 0x10]
002E5260  0F B6 C1                        movzx eax, cl
002E5263  41 32 41 10                     xor al, byte ptr [r9 + 0x10]
002E5267  24 01                           and al, 1
002E5269  32 C1                           xor al, cl
002E526B  88 42 10                        mov byte ptr [rdx + 0x10], al
002E526E  41 80 61 10 FE                  and byte ptr [r9 + 0x10], 0xfe
002E5273  41 80 60 10 FE                  and byte ptr [r8 + 0x10], 0xfe
002E5278  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
002E527C  49 8B 1B                        mov rbx, qword ptr [r11]
002E527F  A8 01                           test al, 1
002E5281  0F 85 56 02 00 00               jne 0x1402e54dd
002E5287  44 0F B6 C0                     movzx r8d, al
002E528B  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
002E528F  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E5293  41 83 E0 01                     and r8d, 1
002E5297  74 09                           je 0x1402e52a2
002E5299  48 85 C0                        test rax, rax
002E529C  0F 85 F5 02 00 00               jne 0x1402e5597
002E52A2  49 3B C1                        cmp rax, r9
002E52A5  0F 85 93 FA FF FF               jne 0x1402e4d3e
002E52AB  8B C5                           mov eax, ebp
002E52AD  48 83 F0 01                     xor rax, 1
002E52B1  49 8B 0C C1                     mov rcx, qword ptr [r9 + rax*8]
002E52B5  45 85 C0                        test r8d, r8d
002E52B8  74 09                           je 0x1402e52c3
002E52BA  48 85 C9                        test rcx, rcx
002E52BD  0F 85 F0 05 00 00               jne 0x1402e58b3
002E52C3  48 3B CA                        cmp rcx, rdx
002E52C6  0F 85 72 FA FF FF               jne 0x1402e4d3e
002E52CC  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
002E52D0  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002E52D4  45 85 C0                        test r8d, r8d
002E52D7  0F 84 64 04 00 00               je 0x1402e5741
002E52DD  48 85 C9                        test rcx, rcx
002E52E0  0F 85 58 04 00 00               jne 0x1402e573e
002E52E6  49 3B D9                        cmp rbx, r9
002E52E9  0F 85 4F FA FF FF               jne 0x1402e4d3e
002E52EF  48 8B DA                        mov rbx, rdx
002E52F2  E9 81 04 00 00                  jmp 0x1402e5778
002E52F7  80 4A 10 01                     or byte ptr [rdx + 0x10], 1
002E52FB  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
002E52FF  41 0F B6 4B 08                  movzx ecx, byte ptr [r11 + 8]
002E5304  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E5308  80 E1 01                        and cl, 1
002E530B  74 09                           je 0x1402e5316
002E530D  48 85 C0                        test rax, rax
002E5310  0F 85 69 02 00 00               jne 0x1402e557f
002E5316  4C 8B C8                        mov r9, rax
002E5319  4D 85 C9                        test r9, r9
002E531C  0F 84 CE FC FF FF               je 0x1402e4ff0
002E5322  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002E5326  84 C9                           test cl, cl
002E5328  74 09                           je 0x1402e5333
002E532A  48 85 C0                        test rax, rax
002E532D  0F 85 5C 02 00 00               jne 0x1402e558f
002E5333  48 3B C7                        cmp rax, rdi
002E5336  41 8B EF                        mov ebp, r15d
002E5339  40 0F 94 C5                     sete bpl
002E533D  E9 E6 FB FF FF                  jmp 0x1402e4f28
002E5342  48 8B 01                        mov rax, qword ptr [rcx]
002E5345  45 85 C0                        test r8d, r8d
002E5348  74 09                           je 0x1402e5353
002E534A  48 85 C0                        test rax, rax
002E534D  0F 85 34 02 00 00               jne 0x1402e5587
002E5353  49 3B C1                        cmp rax, r9
002E5356  0F 85 E2 F9 FF FF               jne 0x1402e4d3e
002E535C  45 85 C0                        test r8d, r8d
002E535F  0F 84 D1 03 00 00               je 0x1402e5736
002E5365  48 8B C1                        mov rax, rcx
002E5368  48 33 C2                        xor rax, rdx
002E536B  48 89 01                        mov qword ptr [rcx], rax
002E536E  E9 7B FD FF FF                  jmp 0x1402e50ee
002E5373  84 C9                           test cl, cl
002E5375  74 03                           je 0x1402e537a
002E5377  48 33 C2                        xor rax, rdx
002E537A  F6 40 10 01                     test byte ptr [rax + 0x10], 1
002E537E  0F 84 30 FE FF FF               je 0x1402e51b4
002E5384  E9 A5 FE FF FF                  jmp 0x1402e522e
002E5389  8B C5                           mov eax, ebp
002E538B  48 8B CA                        mov rcx, rdx
002E538E  4C 89 0C C2                     mov qword ptr [rdx + rax*8], r9
002E5392  E9 BD FD FF FF                  jmp 0x1402e5154
002E5397  48 8B C2                        mov rax, rdx
002E539A  E9 4B FD FF FF                  jmp 0x1402e50ea
002E539F  8B C5                           mov eax, ebp
002E53A1  4C 8B 14 C2                     mov r10, qword ptr [rdx + rax*8]
002E53A5  84 C9                           test cl, cl
002E53A7  74 09                           je 0x1402e53b2
002E53A9  4D 85 D2                        test r10, r10
002E53AC  0F 85 ED 01 00 00               jne 0x1402e559f
002E53B2  41 80 62 10 FE                  and byte ptr [r10 + 0x10], 0xfe
002E53B7  8B DD                           mov ebx, ebp
002E53B9  49 8B 42 10                     mov rax, qword ptr [r10 + 0x10]
002E53BD  83 F3 01                        xor ebx, 1
002E53C0  45 0F B6 43 08                  movzx r8d, byte ptr [r11 + 8]
002E53C5  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E53C9  41 83 E0 01                     and r8d, 1
002E53CD  74 09                           je 0x1402e53d8
002E53CF  48 85 C0                        test rax, rax
002E53D2  0F 85 CF 01 00 00               jne 0x1402e55a7
002E53D8  48 3B C2                        cmp rax, rdx
002E53DB  0F 85 5D F9 FF FF               jne 0x1402e4d3e
002E53E1  8B C3                           mov eax, ebx
002E53E3  48 83 F0 01                     xor rax, 1
002E53E7  48 8B 0C C2                     mov rcx, qword ptr [rdx + rax*8]
002E53EB  45 85 C0                        test r8d, r8d
002E53EE  74 09                           je 0x1402e53f9
002E53F0  48 85 C9                        test rcx, rcx
002E53F3  0F 85 5A 05 00 00               jne 0x1402e5953
002E53F9  49 3B CA                        cmp rcx, r10
002E53FC  0F 85 3C F9 FF FF               jne 0x1402e4d3e
002E5402  49 8B 04 D9                     mov rax, qword ptr [r9 + rbx*8]
002E5406  45 85 C0                        test r8d, r8d
002E5409  74 09                           je 0x1402e5414
002E540B  48 85 C0                        test rax, rax
002E540E  0F 85 BC 04 00 00               jne 0x1402e58d0
002E5414  48 3B C2                        cmp rax, rdx
002E5417  0F 85 21 F9 FF FF               jne 0x1402e4d3e
002E541D  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
002E5421  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E5425  45 85 C0                        test r8d, r8d
002E5428  74 09                           je 0x1402e5433
002E542A  48 85 C0                        test rax, rax
002E542D  0F 85 95 04 00 00               jne 0x1402e58c8
002E5433  49 3B C1                        cmp rax, r9
002E5436  0F 85 02 F9 FF FF               jne 0x1402e4d3e
002E543C  45 85 C0                        test r8d, r8d
002E543F  0F 84 E8 04 00 00               je 0x1402e592d
002E5445  49 8B CA                        mov rcx, r10
002E5448  49 33 C9                        xor rcx, r9
002E544B  49 89 0C D9                     mov qword ptr [r9 + rbx*8], rcx
002E544F  4D 85 C9                        test r9, r9
002E5452  0F 85 F0 04 00 00               jne 0x1402e5948
002E5458  49 8B C9                        mov rcx, r9
002E545B  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
002E545F  83 E0 03                        and eax, 3
002E5462  48 0B C1                        or rax, rcx
002E5465  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
002E5469  49 8B 0C DA                     mov rcx, qword ptr [r10 + rbx*8]
002E546D  45 85 C0                        test r8d, r8d
002E5470  0F 84 65 04 00 00               je 0x1402e58db
002E5476  48 85 C9                        test rcx, rcx
002E5479  0F 85 59 04 00 00               jne 0x1402e58d8
002E547F  45 85 C0                        test r8d, r8d
002E5482  74 09                           je 0x1402e548d
002E5484  48 85 C9                        test rcx, rcx
002E5487  0F 85 A9 04 00 00               jne 0x1402e5936
002E548D  8B C3                           mov eax, ebx
002E548F  48 83 F0 01                     xor rax, 1
002E5493  48 89 0C C2                     mov qword ptr [rdx + rax*8], rcx
002E5497  45 85 C0                        test r8d, r8d
002E549A  0F 84 81 04 00 00               je 0x1402e5921
002E54A0  49 8B CA                        mov rcx, r10
002E54A3  48 33 CA                        xor rcx, rdx
002E54A6  49 89 0C DA                     mov qword ptr [r10 + rbx*8], rcx
002E54AA  49 8B CA                        mov rcx, r10
002E54AD  48 33 CA                        xor rcx, rdx
002E54B0  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
002E54B3  4C 8B C2                        mov r8, rdx
002E54B6  83 E0 03                        and eax, 3
002E54B9  48 0B C1                        or rax, rcx
002E54BC  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
002E54C0  49 8B D2                        mov rdx, r10
002E54C3  E9 94 FD FF FF                  jmp 0x1402e525c
002E54C8  48 33 C3                        xor rax, rbx
002E54CB  49 8B CF                        mov rcx, r15
002E54CE  48 85 DB                        test rbx, rbx
002E54D1  48 0F 45 C8                     cmovne rcx, rax
002E54D5  49 8B C3                        mov rax, r11
002E54D8  E9 96 FC FF FF                  jmp 0x1402e5173
002E54DD  48 85 DB                        test rbx, rbx
002E54E0  0F 84 A1 FD FF FF               je 0x1402e5287
002E54E6  49 33 DB                        xor rbx, r11
002E54E9  E9 99 FD FF FF                  jmp 0x1402e5287
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E4C42(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p38 = v_rbx;
    v_stack_p40 = v_rbp;
    v_stack_p48 = v_rsi;
    v_stack_p20 = v_rdi;
    v_stack_p18 = v_r12;
    v_stack_p10 = v_r13;
    v_stack_p8 = v_r14;
    v_stack_p0 = v_r15;
    if (result != 0) goto loc_002E4C76;
    goto loc_002E4C82;
loc_002E4C76:
    if (a3 != 0) goto loc_002E4D45;
loc_002E4C82:
    a4 = (*(unsigned __int64 *)(v_r10 + 16)) & (-4);
    a3 = (unsigned __int8)((a2) & (1));
    if (condition_is_equal) goto loc_002E4C9D;
loc_002E4C9D:
    if (a4 == 0) goto loc_002E4D19;
    if ((unsigned __int8)(a3) == 0) goto loc_002E4CB7;
loc_002E4CB7:
    v_r15 = 0;
    if ((*(unsigned __int64 *)(a4 + 8)) == v_r10) goto loc_002E4EF4;
    if (((a2) & (1)) == 0) goto loc_002E4CD4;
loc_002E4CD4:
    if ((*(unsigned __int64 *)(a4)) != v_r10) goto loc_002E4D3E;
    if ((*(unsigned __int64 *)(v_r11 + 8)) != v_r10) goto loc_002E4EF9;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_r11 + 8)) & (1));
    *(unsigned __int64 *)(v_r11 + 8) = a4;
    goto loc_002E4EF9;
loc_002E4D19:
    v_r15 = 0;
    if (a3 != 0) {
        *(unsigned __int64 *)(a3 + 16) = 0;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8))) & (1)) != 0) goto loc_002E5060;
loc_002E4D35:
    if ((*(unsigned __int64 *)(v_r11)) == v_r10) goto loc_002E4FD1;
loc_002E4D3E:
loc_002E4D45:
    v_r15 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) == 0) goto loc_002E4D80;
    v_rdi = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r11))) & (1));
loc_002E4D64:
    if ((unsigned __int8)(v_rdi) == 0) goto loc_002E4D75;
loc_002E4D75:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8))) != 0) goto loc_002E4D64;
loc_002E4D80:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11))) & (1)) == 0) goto loc_002E4D8E;
loc_002E4D8E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8))) = a3;
    a1 = (*(unsigned __int64 *)(a3 + 16)) & (-4);
    v_rsi = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E4DB3;
loc_002E4DB3:
    if (a1 != v_r10) goto loc_002E4D3E;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8))) ^ (a3);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8));
    if ((unsigned __int8)(v_rsi) != 0) { a2 = a1; }
    v_rdi = (unsigned int)((*(unsigned __int64 *)(a3 + 16)) & (3));
    v_rdi = (v_rdi) | (a2);
    *(unsigned __int64 *)(a3 + 16) = v_rdi;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (-4);
    v_rdi = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E4DF1;
loc_002E4DF1:
    if (result != v_r10) goto loc_002E4D3E;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8))) ^ (*(unsigned __int64 *)(v_r11 + 8));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8));
    if ((unsigned __int8)(v_rdi) != 0) { result = a1; }
    a2 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (3));
    a2 = (a2) | (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16) = a2;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E4E2B;
loc_002E4E2B:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8))) ^ (*(unsigned __int64 *)(v_r11 + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 8) = a1;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 16)) & (-4);
    v_r14 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_r11 + 8))) & (1));
    if (condition_is_equal) goto loc_002E4E63;
loc_002E4E63:
    a1 = (*(unsigned __int64 *)(v_r10 + 16)) & (-4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r11 + 8))) & (1)) == 0) goto loc_002E4E97;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r11 + 8))) & (1)) == 0) goto loc_002E4E97;
loc_002E4E97:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 16))) & (3));
    a2 = (a2) | (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 16) = a2;
    a1 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(v_r10 + 16)));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ (a2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 16) = (unsigned __int8)(a1);
    v_rdi = (*(unsigned __int64 *)(v_r10 + 16)) & (-4);
    if ((*(unsigned __int64 *)(v_r11)) != v_r10) goto loc_002E4D3E;
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8));
    goto loc_002E4EFE;
loc_002E4EF4:
loc_002E4EF9:
loc_002E4EFE:
    a3 = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 16)) & (1));
    if ((((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8)))) & (1)) == 0) goto loc_002E4F10;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 8) != 0) goto loc_002E501D;
loc_002E4F10:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 1 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8)) + 8) != 0) goto loc_002E5029;
    if ((unsigned __int8)(a3) != 0) goto loc_002E4FF0;
loc_002E4F28:
    result = (1) ^ (1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r11 + 8))) & (1)) == 0) goto loc_002E4F48;
loc_002E4F48:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16)) & (1)) == 0) goto loc_002E519C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8))) & (1)) != 0) goto loc_002E5071;
loc_002E4F61:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16)) & (-4);
    a3 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8))) & (1));
    if (condition_is_equal) goto loc_002E4F7C;
loc_002E4F7C:
    if (result != (*(unsigned __int64 *)(v_r11 + 8))) goto loc_002E4D3E;
    result = (1) ^ (1);
    if ((unsigned int)(a3) == 0) goto loc_002E4F9D;
loc_002E4F9D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8))) goto loc_002E4D3E;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (-4);
    if ((unsigned int)(a3) == 0) goto loc_002E50B7;
    if (a1 != 0) goto loc_002E50B4;
loc_002E4FC0:
    if ((*(unsigned __int64 *)(v_r11)) != (*(unsigned __int64 *)(v_r11 + 8))) goto loc_002E4D3E;
    goto loc_002E50EE;
loc_002E4FD1:
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_002E5094;
    *(unsigned __int64 *)(v_r11 + 8) = result;
loc_002E4FE1:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (1)) != 0) goto loc_002E5082;
loc_002E4FED:
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(v_r11 + 8);
loc_002E4FF0:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002E501D:
    a2 = (*(unsigned __int64 *)(v_r11 + 8)) ^ (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + (unsigned int)((unsigned int)(a8)) * 8) = a2;
loc_002E5029:
    a1 = (*(unsigned __int64 *)(result + 16)) & (-4);
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E5044;
loc_002E5044:
    if (a1 != a7) goto loc_002E4D3E;
    if (a2 == 0) goto loc_002E505A;
loc_002E505A:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_r11 + 8);
    goto loc_002E4FF0;
loc_002E5060:
    if (a2 == 0) goto loc_002E4D35;
    a2 = (a2) ^ (v_r11);
    goto loc_002E4D35;
loc_002E5071:
    if (a7 == 0) goto loc_002E4F61;
    v_rbx = (a7) ^ (v_r11);
    goto loc_002E4F61;
loc_002E5082:
    a1 = (result) ^ (v_r11);
    v_r15 = v_stack_p0;
    if (result != 0) { v_r15 = a1; }
    goto loc_002E4FED;
loc_002E5094:
    a1 = (result) ^ (v_r11);
    a2 = v_r15;
    if (result != 0) { a2 = a1; }
    *(unsigned __int64 *)(v_r11 + 8) = a2;
    a2 = (unsigned __int8)((a2) | (1));
    *(unsigned __int8 *)(v_r11 + 8) = a2;
    goto loc_002E4FE1;
loc_002E50B4:
    a1 = (a1) ^ (*(unsigned __int64 *)(v_r11 + 8));
loc_002E50B7:
    if (a1 == 0) goto loc_002E4FC0;
    if ((unsigned int)(a3) == 0) goto loc_002E50D2;
loc_002E50D2:
    if ((*(unsigned __int64 *)(a1 + 8)) != (*(unsigned __int64 *)(v_r11 + 8))) goto loc_002E5342;
    if ((unsigned int)(a3) == 0) goto loc_002E5397;
    result = (a1) ^ (a2);
loc_002E50EA:
    *(unsigned __int64 *)(a1 + 8) = result;
loc_002E50EE:
    if ((unsigned int)(a3) == 0) goto loc_002E50FC;
loc_002E50FC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) & (3));
    result = (result) | (a1);
    *(unsigned __int64 *)(a2 + 16) = result;
    if ((unsigned int)(a3) == 0) goto loc_002E51D3;
    if (*(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)(a8)) * 8) != 0) goto loc_002E51D0;
loc_002E5121:
    if ((unsigned int)(a3) == 0) goto loc_002E512F;
loc_002E512F:
    result = ((unsigned int)((unsigned int)(a8))) ^ (1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) = *(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)(a8)) * 8);
    if ((unsigned int)(a3) == 0) goto loc_002E5389;
    a1 = (a2) ^ (*(unsigned __int64 *)(v_r11 + 8));
    *(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)(a8)) * 8) = a1;
    a1 = (a2) ^ (*(unsigned __int64 *)(v_r11 + 8));
loc_002E5154:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r11 + 8) + 16))) & (3));
    result = (result) | (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16) = result;
    if (((*(unsigned __int8 *)(v_r11 + 8)) & (1)) != 0) goto loc_002E54C8;
loc_002E5173:
    *(unsigned __int64 *)(v_r11) = v_rbx;
    result = ((unsigned int)((unsigned int)(a8))) ^ (1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r11 + 8))) & (1)) == 0) goto loc_002E519C;
loc_002E519C:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8)) != 0) goto loc_002E521D;
loc_002E51A7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 8) != 0) goto loc_002E5373;
loc_002E51B4:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + 8) + 16))) & (1)) == 0) goto loc_002E52F7;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (254));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + 8) + 16) = (unsigned __int8)(result);
    goto loc_002E4FF0;
loc_002E51D0:
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
loc_002E51D3:
    if (a1 == 0) goto loc_002E5121;
    result = (*(unsigned __int64 *)(a1 + 16)) & (-4);
    if ((unsigned int)(a3) == 0) goto loc_002E51F5;
loc_002E51F5:
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8))) goto loc_002E4D3E;
    result = (a1) ^ (*(unsigned __int64 *)(v_r11 + 8));
    v_r10 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (3));
    v_r10 = (v_r10) | (result);
    *(unsigned __int64 *)(a1 + 16) = v_r10;
    goto loc_002E5121;
loc_002E521D:
    if ((unsigned __int8)(a1) != 0) {
        result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
    }
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) goto loc_002E51A7;
loc_002E522E:
    result = ((unsigned int)((unsigned int)(a8))) ^ (1);
    if ((unsigned __int8)(a1) == 0) goto loc_002E5248;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + result * 8) == 0) goto loc_002E539F;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + result * 8)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
loc_002E5248:
    if (a3 == 0) goto loc_002E539F;
    if (((*(unsigned __int8 *)(a3 + 16)) & (1)) == 0) goto loc_002E539F;
loc_002E525C:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16) = (unsigned __int8)(result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8))) & (1)) != 0) goto loc_002E54DD;
loc_002E5287:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16)) & (-4);
    a3 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_r11 + 8))) & (1));
    if (condition_is_equal) goto loc_002E52A2;
loc_002E52A2:
    if (result != (*(unsigned __int64 *)(v_r11 + 8))) goto loc_002E4D3E;
    result = ((unsigned int)((unsigned int)(a8))) ^ (1);
    if ((unsigned int)(a3) == 0) goto loc_002E52C3;
loc_002E52C3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8))) goto loc_002E4D3E;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (-4);
    if ((*(unsigned __int64 *)(v_r11)) != (*(unsigned __int64 *)(v_r11 + 8))) goto loc_002E4D3E;
loc_002E52F7:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + 16)) & (-4);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E5316;
loc_002E5316:
    if (result == 0) goto loc_002E4FF0;
    if ((unsigned __int8)(a1) == 0) goto loc_002E5333;
loc_002E5333:
    v_rbp = ((*(unsigned __int64 *)(result + 8)) == v_stack_p20) ? 1 : 0;
    goto loc_002E4F28;
loc_002E5342:
    if ((unsigned int)(a3) == 0) goto loc_002E5353;
loc_002E5353:
    if ((*(unsigned __int64 *)(a1)) != result) goto loc_002E4D3E;
    result = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
    *(unsigned __int64 *)(a1) = result;
    goto loc_002E50EE;
loc_002E5373:
    if ((unsigned __int8)(a1) != 0) {
        result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
    }
    if (((*(unsigned __int8 *)(result + 16)) & (1)) == 0) goto loc_002E51B4;
    goto loc_002E522E;
loc_002E5389:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) = result;
    goto loc_002E5154;
loc_002E5397:
    goto loc_002E50EA;
loc_002E539F:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8)) == 0) goto loc_002E53B2;
loc_002E53B2:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) ^ (1));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) + 16)) & (-4);
    a3 = (unsigned int)((*(unsigned __int8 *)(v_r11 + 8)) & (1));
    if (condition_is_equal) goto loc_002E53D8;
loc_002E53D8:
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8))) goto loc_002E4D3E;
    result = ((unsigned int)((unsigned int)(v_rbx))) ^ (1);
    if ((unsigned int)(a3) == 0) goto loc_002E53F9;
loc_002E53F9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + result * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8))) goto loc_002E4D3E;
    if ((unsigned int)(a3) == 0) goto loc_002E5414;
loc_002E5414:
    if ((*(unsigned __int64 *)(result + v_rbx * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8))) goto loc_002E4D3E;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16)) & (-4);
    if ((unsigned int)(a3) == 0) goto loc_002E5433;
loc_002E5433:
    if (result != result) goto loc_002E4D3E;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8)) ^ (result);
    *(unsigned __int64 *)(result + v_rbx * 8) = a1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) + 16))) & (3));
    result = (result) | (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) + 16) = result;
    if ((unsigned int)(a3) == 0) goto loc_002E548D;
loc_002E548D:
    result = ((unsigned int)((unsigned int)(v_rbx))) ^ (1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + result * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) + v_rbx * 8);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8) + v_rbx * 8) = a1;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + (unsigned int)((unsigned int)(v_rbp)) * 8)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16))) & (3));
    result = (result) | (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + 8) + result * 8) + 16) = result;
    goto loc_002E525C;
loc_002E54C8:
    result = (result) ^ (v_rbx);
    a1 = v_r15;
    if (v_rbx != 0) { a1 = result; }
    goto loc_002E5173;
loc_002E54DD:
    if (v_rbx == 0) goto loc_002E5287;
    v_rbx = (v_rbx) ^ (v_r11);
    goto loc_002E5287;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E4C42(int64_t Arg1, uint8_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p38 = local_rbx;
    v_stack_p40 = local_rbp;
    v_stack_p48 = local_rsi;
    v_stack_p20 = local_rdi;
    v_stack_p18 = local_r12;
    v_stack_p10 = local_r13;
    v_stack_p8 = local_r14;
    v_stack_p0 = local_r15;
    if (result != 0) goto loc_002E4C76;
    goto loc_002E4C82;
loc_002E4C76:
    if (Arg3 != 0) goto loc_002E4D45;
loc_002E4C82:
    Arg4 = (*(uint64_t *)(local_r10 + 0x10)) & (-4);
    Arg3 = (uint8_t)((Arg2) & (1));
    if (condition_is_equal) goto loc_002E4C9D;
loc_002E4C9D:
    if (Arg4 == 0) goto loc_002E4D19;
    if ((uint8_t)(Arg3) == 0) goto loc_002E4CB7;
loc_002E4CB7:
    local_r15 = 0;
    if ((*(uint64_t *)(Arg4 + 0x8)) == local_r10) goto loc_002E4EF4;
    if (((Arg2) & (1)) == 0) goto loc_002E4CD4;
loc_002E4CD4:
    if ((*(uint64_t *)(Arg4)) != local_r10) goto loc_002E4D3E;
    if ((*(uint64_t *)(local_r11 + 0x8)) != local_r10) goto loc_002E4EF9;
    Arg1 = (uint8_t)((*(uint64_t *)(local_r11 + 0x8)) & (1));
    *(uint64_t *)(local_r11 + 0x8) = Arg4;
    goto loc_002E4EF9;
loc_002E4D19:
    local_r15 = 0;
    if (Arg3 != 0) {
        *(uint64_t *)(Arg3 + 0x10) = 0;
    }
    if ((((uint8_t)(*(uint64_t *)(local_r11 + 0x8))) & (1)) != 0) goto loc_002E5060;
loc_002E4D35:
    if ((*(uint64_t *)(local_r11)) == local_r10) goto loc_002E4FD1;
loc_002E4D3E:
loc_002E4D45:
    local_r15 = 0;
    if (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) == 0) goto loc_002E4D80;
    local_rdi = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r11))) & (1));
loc_002E4D64:
    if ((uint8_t)(local_rdi) == 0) goto loc_002E4D75;
loc_002E4D75:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8))) != 0) goto loc_002E4D64;
loc_002E4D80:
    if ((((uint8_t)(*(uint64_t *)(local_r11))) & (1)) == 0) goto loc_002E4D8E;
loc_002E4D8E:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8))) = Arg3;
    Arg1 = (*(uint64_t *)(Arg3 + 0x10)) & (-4);
    local_rsi = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E4DB3;
loc_002E4DB3:
    if (Arg1 != local_r10) goto loc_002E4D3E;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8))) ^ (Arg3);
    Arg2 = *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8));
    if ((uint8_t)(local_rsi) != 0) { Arg2 = Arg1; }
    local_rdi = (uint32_t)((*(uint64_t *)(Arg3 + 0x10)) & (3));
    local_rdi = (local_rdi) | (Arg2);
    *(uint64_t *)(Arg3 + 0x10) = local_rdi;
    result = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (-4);
    local_rdi = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E4DF1;
loc_002E4DF1:
    if (result != local_r10) goto loc_002E4D3E;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8))) ^ (*(uint64_t *)(local_r11 + 0x8));
    result = *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8));
    if ((uint8_t)(local_rdi) != 0) { result = Arg1; }
    Arg2 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (3));
    Arg2 = (Arg2) | (result);
    *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10) = Arg2;
    Arg1 = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E4E2B;
loc_002E4E2B:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8))) ^ (*(uint64_t *)(local_r11 + 0x8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x8) = Arg1;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x10)) & (-4);
    local_r14 = (uint8_t)(((uint8_t)(*(uint8_t *)(local_r11 + 0x8))) & (1));
    if (condition_is_equal) goto loc_002E4E63;
loc_002E4E63:
    Arg1 = (*(uint64_t *)(local_r10 + 0x10)) & (-4);
    if ((((uint8_t)(*(uint8_t *)(local_r11 + 0x8))) & (1)) == 0) goto loc_002E4E97;
    if ((((uint8_t)(*(uint8_t *)(local_r11 + 0x8))) & (1)) == 0) goto loc_002E4E97;
loc_002E4E97:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x10))) & (3));
    Arg2 = (Arg2) | (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x10) = Arg2;
    Arg1 = (uint8_t)((Arg2) ^ (*(uint8_t *)(local_r10 + 0x10)));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ (Arg2));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x10) = (uint8_t)(Arg1);
    local_rdi = (*(uint64_t *)(local_r10 + 0x10)) & (-4);
    if ((*(uint64_t *)(local_r11)) != local_r10) goto loc_002E4D3E;
    *(uint64_t *)(local_r11) = *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8));
    goto loc_002E4EFE;
loc_002E4EF4:
loc_002E4EF9:
loc_002E4EFE:
    Arg3 = (uint8_t)((*(uint8_t *)(local_r11 + 0x10)) & (1));
    if ((((uint8_t)((uint8_t)(*(uint64_t *)(local_r11 + 0x8)))) & (1)) == 0) goto loc_002E4F10;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x8) != 0) goto loc_002E501D;
loc_002E4F10:
    *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x1 * 8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8)) + 0x8) != 0) goto loc_002E5029;
    if ((uint8_t)(Arg3) != 0) goto loc_002E4FF0;
loc_002E4F28:
    result = (1) ^ (1);
    if ((((uint8_t)(*(uint8_t *)(local_r11 + 0x8))) & (1)) == 0) goto loc_002E4F48;
loc_002E4F48:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10)) & (1)) == 0) goto loc_002E519C;
    if ((((uint8_t)(*(uint64_t *)(local_r11 + 0x8))) & (1)) != 0) goto loc_002E5071;
loc_002E4F61:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10)) & (-4);
    Arg3 = (uint32_t)(((uint8_t)(*(uint64_t *)(local_r11 + 0x8))) & (1));
    if (condition_is_equal) goto loc_002E4F7C;
loc_002E4F7C:
    if (result != (*(uint64_t *)(local_r11 + 0x8))) goto loc_002E4D3E;
    result = (1) ^ (1);
    if ((uint32_t)(Arg3) == 0) goto loc_002E4F9D;
loc_002E4F9D:
    if ((*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8)) != (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8))) goto loc_002E4D3E;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (-4);
    if ((uint32_t)(Arg3) == 0) goto loc_002E50B7;
    if (Arg1 != 0) goto loc_002E50B4;
loc_002E4FC0:
    if ((*(uint64_t *)(local_r11)) != (*(uint64_t *)(local_r11 + 0x8))) goto loc_002E4D3E;
    goto loc_002E50EE;
loc_002E4FD1:
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_002E5094;
    *(uint64_t *)(local_r11 + 0x8) = result;
loc_002E4FE1:
    if ((((uint8_t)((uint8_t)(result))) & (1)) != 0) goto loc_002E5082;
loc_002E4FED:
    *(uint64_t *)(local_r11) = *(uint64_t *)(local_r11 + 0x8);
loc_002E4FF0:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002E501D:
    Arg2 = (*(uint64_t *)(local_r11 + 0x8)) ^ (result);
    *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + (uint32_t)((uint32_t)(Arg8)) * 8) = Arg2;
loc_002E5029:
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-4);
    Arg2 = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E5044;
loc_002E5044:
    if (Arg1 != Arg7) goto loc_002E4D3E;
    if (Arg2 == 0) goto loc_002E505A;
loc_002E505A:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(local_r11 + 0x8);
    goto loc_002E4FF0;
loc_002E5060:
    if (Arg2 == 0) goto loc_002E4D35;
    Arg2 = (Arg2) ^ (local_r11);
    goto loc_002E4D35;
loc_002E5071:
    if (Arg7 == 0) goto loc_002E4F61;
    local_rbx = (Arg7) ^ (local_r11);
    goto loc_002E4F61;
loc_002E5082:
    Arg1 = (result) ^ (local_r11);
    local_r15 = v_stack_p0;
    if (result != 0) { local_r15 = Arg1; }
    goto loc_002E4FED;
loc_002E5094:
    Arg1 = (result) ^ (local_r11);
    Arg2 = local_r15;
    if (result != 0) { Arg2 = Arg1; }
    *(uint64_t *)(local_r11 + 0x8) = Arg2;
    Arg2 = (uint8_t)((Arg2) | (1));
    *(uint8_t *)(local_r11 + 0x8) = Arg2;
    goto loc_002E4FE1;
loc_002E50B4:
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_r11 + 0x8));
loc_002E50B7:
    if (Arg1 == 0) goto loc_002E4FC0;
    if ((uint32_t)(Arg3) == 0) goto loc_002E50D2;
loc_002E50D2:
    if ((*(uint64_t *)(Arg1 + 0x8)) != (*(uint64_t *)(local_r11 + 0x8))) goto loc_002E5342;
    if ((uint32_t)(Arg3) == 0) goto loc_002E5397;
    result = (Arg1) ^ (Arg2);
loc_002E50EA:
    *(uint64_t *)(Arg1 + 0x8) = result;
loc_002E50EE:
    if ((uint32_t)(Arg3) == 0) goto loc_002E50FC;
loc_002E50FC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) & (3));
    result = (result) | (Arg1);
    *(uint64_t *)(Arg2 + 0x10) = result;
    if ((uint32_t)(Arg3) == 0) goto loc_002E51D3;
    if (*(uint64_t *)(Arg2 + (uint32_t)((uint32_t)(Arg8)) * 8) != 0) goto loc_002E51D0;
loc_002E5121:
    if ((uint32_t)(Arg3) == 0) goto loc_002E512F;
loc_002E512F:
    result = ((uint32_t)((uint32_t)(Arg8))) ^ (1);
    *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) = *(uint64_t *)(Arg2 + (uint32_t)((uint32_t)(Arg8)) * 8);
    if ((uint32_t)(Arg3) == 0) goto loc_002E5389;
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_r11 + 0x8));
    *(uint64_t *)(Arg2 + (uint32_t)((uint32_t)(Arg8)) * 8) = Arg1;
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_r11 + 0x8));
loc_002E5154:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10))) & (3));
    result = (result) | (Arg1);
    *(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10) = result;
    if (((*(uint8_t *)(local_r11 + 0x8)) & (1)) != 0) goto loc_002E54C8;
loc_002E5173:
    *(uint64_t *)(local_r11) = local_rbx;
    result = ((uint32_t)((uint32_t)(Arg8))) ^ (1);
    if ((((uint8_t)(*(uint8_t *)(local_r11 + 0x8))) & (1)) == 0) goto loc_002E519C;
loc_002E519C:
    Arg1 = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8)) != 0) goto loc_002E521D;
loc_002E51A7:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x8) != 0) goto loc_002E5373;
loc_002E51B4:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10))) & (1)) == 0) goto loc_002E52F7;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (254));
    *(uint8_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10) = (uint8_t)(result);
    goto loc_002E4FF0;
loc_002E51D0:
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
loc_002E51D3:
    if (Arg1 == 0) goto loc_002E5121;
    result = (*(uint64_t *)(Arg1 + 0x10)) & (-4);
    if ((uint32_t)(Arg3) == 0) goto loc_002E51F5;
loc_002E51F5:
    if (result != (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8))) goto loc_002E4D3E;
    result = (Arg1) ^ (*(uint64_t *)(local_r11 + 0x8));
    local_r10 = (uint32_t)((*(uint64_t *)(Arg1 + 0x10)) & (3));
    local_r10 = (local_r10) | (result);
    *(uint64_t *)(Arg1 + 0x10) = local_r10;
    goto loc_002E5121;
loc_002E521D:
    if ((uint8_t)(Arg1) != 0) {
        result = (result) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
    }
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) goto loc_002E51A7;
loc_002E522E:
    result = ((uint32_t)((uint32_t)(Arg8))) ^ (1);
    if ((uint8_t)(Arg1) == 0) goto loc_002E5248;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + result * 8) == 0) goto loc_002E539F;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + result * 8)) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
loc_002E5248:
    if (Arg3 == 0) goto loc_002E539F;
    if (((*(uint8_t *)(Arg3 + 0x10)) & (1)) == 0) goto loc_002E539F;
loc_002E525C:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10))) ^ (*(uint8_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10))));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10) = (uint8_t)(result);
    if ((((uint8_t)(*(uint64_t *)(local_r11 + 0x8))) & (1)) != 0) goto loc_002E54DD;
loc_002E5287:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10)) & (-4);
    Arg3 = (uint32_t)(((uint8_t)(*(uint64_t *)(local_r11 + 0x8))) & (1));
    if (condition_is_equal) goto loc_002E52A2;
loc_002E52A2:
    if (result != (*(uint64_t *)(local_r11 + 0x8))) goto loc_002E4D3E;
    result = ((uint32_t)((uint32_t)(Arg8))) ^ (1);
    if ((uint32_t)(Arg3) == 0) goto loc_002E52C3;
loc_002E52C3:
    if ((*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8)) != (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8))) goto loc_002E4D3E;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (-4);
    if ((*(uint64_t *)(local_r11)) != (*(uint64_t *)(local_r11 + 0x8))) goto loc_002E4D3E;
loc_002E52F7:
    result = (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + 0x10)) & (-4);
    Arg1 = (uint8_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E5316;
loc_002E5316:
    if (result == 0) goto loc_002E4FF0;
    if ((uint8_t)(Arg1) == 0) goto loc_002E5333;
loc_002E5333:
    local_rbp = ((*(uint64_t *)(result + 0x8)) == v_stack_p20) ? 1 : 0;
    goto loc_002E4F28;
loc_002E5342:
    if ((uint32_t)(Arg3) == 0) goto loc_002E5353;
loc_002E5353:
    if ((*(uint64_t *)(Arg1)) != result) goto loc_002E4D3E;
    result = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
    *(uint64_t *)(Arg1) = result;
    goto loc_002E50EE;
loc_002E5373:
    if ((uint8_t)(Arg1) != 0) {
        result = (result) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
    }
    if (((*(uint8_t *)(result + 0x10)) & (1)) == 0) goto loc_002E51B4;
    goto loc_002E522E;
loc_002E5389:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) = result;
    goto loc_002E5154;
loc_002E5397:
    goto loc_002E50EA;
loc_002E539F:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8)) == 0) goto loc_002E53B2;
loc_002E53B2:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) ^ (1));
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) + 0x10)) & (-4);
    Arg3 = (uint32_t)((*(uint8_t *)(local_r11 + 0x8)) & (1));
    if (condition_is_equal) goto loc_002E53D8;
loc_002E53D8:
    if (result != (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8))) goto loc_002E4D3E;
    result = ((uint32_t)((uint32_t)(local_rbx))) ^ (1);
    if ((uint32_t)(Arg3) == 0) goto loc_002E53F9;
loc_002E53F9:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + result * 8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8))) goto loc_002E4D3E;
    if ((uint32_t)(Arg3) == 0) goto loc_002E5414;
loc_002E5414:
    if ((*(uint64_t *)(result + local_rbx * 8)) != (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8))) goto loc_002E4D3E;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10)) & (-4);
    if ((uint32_t)(Arg3) == 0) goto loc_002E5433;
loc_002E5433:
    if (result != result) goto loc_002E4D3E;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8)) ^ (result);
    *(uint64_t *)(result + local_rbx * 8) = Arg1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) + 0x10))) & (3));
    result = (result) | (result);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) + 0x10) = result;
    if ((uint32_t)(Arg3) == 0) goto loc_002E548D;
loc_002E548D:
    result = ((uint32_t)((uint32_t)(local_rbx))) ^ (1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + result * 8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) + local_rbx * 8);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8)) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8) + local_rbx * 8) = Arg1;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + (uint32_t)((uint32_t)(local_rbp)) * 8)) ^ (*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10))) & (3));
    result = (result) | (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + 0x8) + result * 8) + 0x10) = result;
    goto loc_002E525C;
loc_002E54C8:
    result = (result) ^ (local_rbx);
    Arg1 = local_r15;
    if (local_rbx != 0) { Arg1 = result; }
    goto loc_002E5173;
loc_002E54DD:
    if (local_rbx == 0) goto loc_002E5287;
    local_rbx = (local_rbx) ^ (local_r11);
    goto loc_002E5287;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E4C42&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
