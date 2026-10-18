# sub_0031A6F6

- RVA: `0x0031A6F6`–`0x0031AADC` (길이 `998` bytes)
- VA: `0x000000014031A6F6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074CF8`
- 디코드: `245`개 명령, `998/998` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0031A735` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0031A8D2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0031AAA5` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031AAB4` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0031A7D2` → RVA `0x00E37668` (`.data`; read)
- `0x0031A7E2` → RVA `0x00E37670` (`.data`; read)
- `0x0031A85A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0031A893` → RVA `0x00E376C0` (`.data`; read/write)
- `0x0031A89F` → RVA `0x00E376A8` (`.data`; write)
- `0x0031AA9E` → RVA `0x00E3769C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **24**
  - `0x0031A6F9` → [sub_0031A46A + 0xB9](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A747` → [sub_0031A46A + 0x1BA](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A756` → [sub_0031A46A + 0x1B7](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A75E` → [sub_0031A46A + 0x25F](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A7C7` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A7CD` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A809` → [sub_0031A46A + 0x64](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A812` → [sub_0031A46A + 0x64](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A8A6` → [sub_0031A46A + 0xDD](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A8C0` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A8E8` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A94B` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A974` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A9A5` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A9B8` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031A9CA` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA07` → [sub_0031A46A + 0xDD](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA34` → [sub_0031A46A + 0x17E](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA40` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA5F` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA7E` → [sub_0031A46A + 0x17B](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AA99` → [sub_0031A46A + 0x4D](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AAB9` → [sub_0031A46A + 0x54](Unknown_function_0031A46A.md) (`tail-transfer`)
  - `0x0031AAD7` → [sub_0031A46A + 0x4D](Unknown_function_0031A46A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031A6F6  49 8B 08                        mov rcx, qword ptr [r8]
0031A6F9  E9 25 FE FF FF                  jmp 0x14031a523
0031A6FE  85 C9                           test ecx, ecx
0031A700  74 1B                           je 0x14031a71d
0031A702  42 0F B6 84 21 20 2D 01 00      movzx eax, byte ptr [rcx + r12 + 0x12d20]
0031A70B  08 45 00                        or byte ptr [rbp], al
0031A70E  B8 08 00 00 00                  mov eax, 8
0031A713  2B C1                           sub eax, ecx
0031A715  48 FF C5                        inc rbp
0031A718  8B C8                           mov ecx, eax
0031A71A  4C 2B F1                        sub r14, rcx
0031A71D  49 83 FE 08                     cmp r14, 8
0031A721  76 1E                           jbe 0x14031a741
0031A723  49 8B FE                        mov rdi, r14
0031A726  BA FF 00 00 00                  mov edx, 0xff
0031A72B  48 C1 EF 03                     shr rdi, 3
0031A72F  48 8B CD                        mov rcx, rbp
0031A732  4C 8B C7                        mov r8, rdi
0031A735  E8 06 C5 3A 00                  call 0x1406c6c40
0031A73A  48 03 EF                        add rbp, rdi
0031A73D  41 83 E6 07                     and r14d, 7
0031A741  49 8B FF                        mov rdi, r15
0031A744  4D 85 F6                        test r14, r14
0031A747  0F 84 D7 FE FF FF               je 0x14031a624
0031A74D  43 0F B6 84 26 90 C8 02 00      movzx eax, byte ptr [r14 + r12 + 0x2c890]
0031A756  E9 C6 FE FF FF                  jmp 0x14031a621
0031A75B  4D 8B C7                        mov r8, r15
0031A75E  E9 66 FF FF FF                  jmp 0x14031a6c9
0031A763  48 C1 E9 06                     shr rcx, 6
0031A767  44 8B D7                        mov r10d, edi
0031A76A  4D 8D 2C C8                     lea r13, [r8 + rcx*8]
0031A76E  49 83 F9 FF                     cmp r9, -1
0031A772  0F 84 69 01 00 00               je 0x14031a8e1
0031A778  49 0F BC C9                     bsf rcx, r9
0031A77C  41 0F 44 CC                     cmove ecx, r12d
0031A780  41 03 CA                        add ecx, r10d
0031A783  49 3B CE                        cmp rcx, r14
0031A786  0F 83 4D 01 00 00               jae 0x14031a8d9
0031A78C  4D 8B D1                        mov r10, r9
0031A78F  45 8B E6                        mov r12d, r14d
0031A792  49 F7 D2                        not r10
0031A795  49 8B C2                        mov rax, r10
0031A798  41 8B CC                        mov ecx, r12d
0031A79B  D1 E9                           shr ecx, 1
0031A79D  48 D3 E8                        shr rax, cl
0031A7A0  4C 23 D0                        and r10, rax
0031A7A3  0F 84 1E 02 00 00               je 0x14031a9c7
0031A7A9  44 2B E1                        sub r12d, ecx
0031A7AC  41 83 FC 01                     cmp r12d, 1
0031A7B0  77 E3                           ja 0x14031a795
0031A7B2  4D 0F BC D2                     bsf r10, r10
0031A7B6  49 2B D0                        sub rdx, r8
0031A7B9  48 C1 FA 03                     sar rdx, 3
0031A7BD  48 C1 E2 06                     shl rdx, 6
0031A7C1  4C 03 D2                        add r10, rdx
0031A7C4  4D 3B D3                        cmp r10, r11
0031A7C7  0F 87 1B FE FF FF               ja 0x14031a5e8
0031A7CD  E9 13 FE FF FF                  jmp 0x14031a5e5
0031A7D2  48 8B 15 8F CE B1 00            mov rdx, qword ptr [rip + 0xb1ce8f]
0031A7D9  49 3B D3                        cmp rdx, r11
0031A7DC  0F 82 BC 02 00 00               jb 0x14031aa9e
0031A7E2  48 8B 05 87 CE B1 00            mov rax, qword ptr [rip + 0xb1ce87]
0031A7E9  48 8D 5C 24 20                  lea rbx, [rsp + 0x20]
0031A7EE  49 2B D3                        sub rdx, r11
0031A7F1  49 8B CB                        mov rcx, r11
0031A7F4  48 C1 E9 06                     shr rcx, 6
0031A7F8  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0031A7FD  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0031A801  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0031A806  48 85 F6                        test rsi, rsi
0031A809  0F 84 BF FC FF FF               je 0x14031a4ce
0031A80F  49 2B F3                        sub rsi, r11
0031A812  E9 B7 FC FF FF                  jmp 0x14031a4ce
0031A817  48 8B 05 52 CE B1 00            mov rax, qword ptr [rip + 0xb1ce52]
0031A81E  4F 8D 2C 18                     lea r13, [r8 + r11]
0031A822  49 83 E5 C0                     and r13, 0xffffffffffffffc0
0031A826  49 8B CD                        mov rcx, r13
0031A829  48 C1 E9 06                     shr rcx, 6
0031A82D  48 8B 2C C8                     mov rbp, qword ptr [rax + rcx*8]
0031A831  4C 8D 24 C8                     lea r12, [rax + rcx*8]
0031A835  49 3B EF                        cmp rbp, r15
0031A838  0F 84 51 02 00 00               je 0x14031aa8f
0031A83E  48 8B C5                        mov rax, rbp
0031A841  F0 4D 0F B1 3C 24               lock cmpxchg qword ptr [r12], r15
0031A847  0F 85 36 02 00 00               jne 0x14031aa83
0031A84D  44 0F 20 C6                     mov rsi, cr8
0031A851  B8 02 00 00 00                  mov eax, 2
0031A856  44 0F 22 C0                     mov cr8, rax
0031A85A  39 3D C0 C4 CA 00               cmp dword ptr [rip + 0xcac4c0], edi
0031A860  75 69                           jne 0x14031a8cb
0031A862  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
0031A86B  4C 39 BB B0 8F 00 00            cmp qword ptr [rbx + 0x8fb0], r15
0031A872  0F 85 8A 01 00 00               jne 0x14031aa02
0031A878  48 89 AB B0 8F 00 00            mov qword ptr [rbx + 0x8fb0], rbp
0031A87F  48 F7 D5                        not rbp
0031A882  F3 48 0F B8 CD                  popcnt rcx, rbp
0031A887  8B C9                           mov ecx, ecx
0031A889  48 F7 D9                        neg rcx
0031A88C  44 89 AB B8 8F 00 00            mov dword ptr [rbx + 0x8fb8], r13d
0031A893  F0 48 01 0D 25 CE B1 00         lock add qword ptr [rip + 0xb1ce25], rcx
0031A89B  49 8D 45 40                     lea rax, [r13 + 0x40]
0031A89F  48 89 05 02 CE B1 00            mov qword ptr [rip + 0xb1ce02], rax
0031A8A6  E9 9C FC FF FF                  jmp 0x14031a547
0031A8AB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0031A8B0  4D 85 C9                        test r9, r9
0031A8B3  0F 89 53 01 00 00               jns 0x14031aa0c
0031A8B9  48 83 C2 08                     add rdx, 8
0031A8BD  48 3B D5                        cmp rdx, rbp
0031A8C0  0F 87 22 FD FF FF               ja 0x14031a5e8
0031A8C6  4C 8B 0A                        mov r9, qword ptr [rdx]
0031A8C9  EB E5                           jmp 0x14031a8b0
0031A8CB  0F B6 D0                        movzx edx, al
0031A8CE  40 0F B6 CE                     movzx ecx, sil
0031A8D2  E8 25 AE 1D 00                  call 0x1404f56fc
0031A8D7  EB 89                           jmp 0x14031a862
0031A8D9  49 F7 DA                        neg r10
0031A8DC  E9 D5 FE FF FF                  jmp 0x14031a7b6
0031A8E1  48 83 C2 08                     add rdx, 8
0031A8E5  48 3B D5                        cmp rdx, rbp
0031A8E8  0F 87 FA FC FF FF               ja 0x14031a5e8
0031A8EE  4C 8B 0A                        mov r9, qword ptr [rdx]
0031A8F1  49 83 F9 FF                     cmp r9, -1
0031A8F5  74 EA                           je 0x14031a8e1
0031A8F7  44 8B D7                        mov r10d, edi
0031A8FA  E9 79 FE FF FF                  jmp 0x14031a778
0031A8FF  41 F6 C3 3F                     test r11b, 0x3f
0031A903  4C 8D 65 08                     lea r12, [rbp + 8]
0031A907  4C 0F 44 E5                     cmove r12, rbp
0031A90B  BD 40 00 00 00                  mov ebp, 0x40
0031A910  4D 85 C9                        test r9, r9
0031A913  0F 84 A7 00 00 00               je 0x14031a9c0
0031A919  48 83 C2 08                     add rdx, 8
0031A91D  48 83 3A 00                     cmp qword ptr [rdx], 0
0031A921  75 4B                           jne 0x14031a96e
0031A923  49 0F BD C1                     bsr rax, r9
0031A927  0F 84 91 01 00 00               je 0x14031aabe
0031A92D  B9 3F 00 00 00                  mov ecx, 0x3f
0031A932  2B C8                           sub ecx, eax
0031A934  4C 8B D2                        mov r10, rdx
0031A937  44 8B C9                        mov r9d, ecx
0031A93A  4D 2B D0                        sub r10, r8
0031A93D  49 C1 FA 03                     sar r10, 3
0031A941  49 C1 E2 06                     shl r10, 6
0031A945  4D 2B D1                        sub r10, r9
0031A948  4D 3B D3                        cmp r10, r11
0031A94B  0F 87 97 FC FF FF               ja 0x14031a5e8
0031A951  49 8B C6                        mov rax, r14
0031A954  49 2B C1                        sub rax, r9
0031A957  48 C1 E8 06                     shr rax, 6
0031A95B  4C 8D 0C C2                     lea r9, [rdx + rax*8]
0031A95F  48 83 C2 08                     add rdx, 8
0031A963  49 3B D1                        cmp rdx, r9
0031A966  74 33                           je 0x14031a99b
0031A968  48 83 3A 00                     cmp qword ptr [rdx], 0
0031A96C  74 F1                           je 0x14031a95f
0031A96E  48 8B CA                        mov rcx, rdx
0031A971  49 3B D4                        cmp rdx, r12
0031A974  0F 87 6E FC FF FF               ja 0x14031a5e8
0031A97A  48 83 C2 08                     add rdx, 8
0031A97E  48 83 3A 00                     cmp qword ptr [rdx], 0
0031A982  75 EA                           jne 0x14031a96e
0031A984  48 8B 01                        mov rax, qword ptr [rcx]
0031A987  4C 0F BD C8                     bsr r9, rax
0031A98B  0F 84 34 01 00 00               je 0x14031aac5
0031A991  B9 3F 00 00 00                  mov ecx, 0x3f
0031A996  41 2B C9                        sub ecx, r9d
0031A999  EB 99                           jmp 0x14031a934
0031A99B  45 8B CE                        mov r9d, r14d
0031A99E  44 2B C9                        sub r9d, ecx
0031A9A1  41 83 E1 3F                     and r9d, 0x3f
0031A9A5  0F 84 3A FC FF FF               je 0x14031a5e5
0031A9AB  48 8B 02                        mov rax, qword ptr [rdx]
0031A9AE  48 0F BC C8                     bsf rcx, rax
0031A9B2  0F 44 CD                        cmove ecx, ebp
0031A9B5  41 3B C9                        cmp ecx, r9d
0031A9B8  0F 83 27 FC FF FF               jae 0x14031a5e5
0031A9BE  EB AE                           jmp 0x14031a96e
0031A9C0  8B CF                           mov ecx, edi
0031A9C2  E9 6D FF FF FF                  jmp 0x14031a934
0031A9C7  49 3B D5                        cmp rdx, r13
0031A9CA  0F 84 18 FC FF FF               je 0x14031a5e8
0031A9D0  49 0F BD C1                     bsr rax, r9
0031A9D4  41 BC 40 00 00 00               mov r12d, 0x40
0031A9DA  74 16                           je 0x14031a9f2
0031A9DC  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
0031A9E0  41 BA 3F 00 00 00               mov r10d, 0x3f
0031A9E6  44 2B D0                        sub r10d, eax
0031A9E9  48 83 C2 08                     add rdx, 8
0031A9ED  E9 7C FD FF FF                  jmp 0x14031a76e
0031A9F2  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
0031A9F6  48 83 C2 08                     add rdx, 8
0031A9FA  45 8B D4                        mov r10d, r12d
0031A9FD  E9 6C FD FF FF                  jmp 0x14031a76e
0031AA02  F0 49 21 2C 24                  lock and qword ptr [r12], rbp
0031AA07  E9 3B FB FF FF                  jmp 0x14031a547
0031AA0C  49 0F BD C9                     bsr rcx, r9
0031AA10  0F 84 B6 00 00 00               je 0x14031aacc
0031AA16  B8 3F 00 00 00                  mov eax, 0x3f
0031AA1B  2B C1                           sub eax, ecx
0031AA1D  4C 8B D2                        mov r10, rdx
0031AA20  4D 2B D0                        sub r10, r8
0031AA23  49 C1 FA 03                     sar r10, 3
0031AA27  49 FF C2                        inc r10
0031AA2A  49 C1 E2 06                     shl r10, 6
0031AA2E  4C 2B D0                        sub r10, rax
0031AA31  4D 3B D3                        cmp r10, r11
0031AA34  0F 87 AE FB FF FF               ja 0x14031a5e8
0031AA3A  49 8B CE                        mov rcx, r14
0031AA3D  48 2B C8                        sub rcx, rax
0031AA40  0F 84 9F FB FF FF               je 0x14031a5e5
0031AA46  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
0031AA4A  48 83 C2 08                     add rdx, 8
0031AA4E  49 3B CC                        cmp rcx, r12
0031AA51  72 1A                           jb 0x14031aa6d
0031AA53  4D 85 C9                        test r9, r9
0031AA56  0F 85 57 FE FF FF               jne 0x14031a8b3
0031AA5C  49 2B CC                        sub rcx, r12
0031AA5F  0F 84 80 FB FF FF               je 0x14031a5e5
0031AA65  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
0031AA69  48 83 C2 08                     add rdx, 8
0031AA6D  49 0F BC C1                     bsf rax, r9
0031AA71  41 0F 44 C4                     cmove eax, r12d
0031AA75  48 3B C1                        cmp rax, rcx
0031AA78  0F 82 32 FE FF FF               jb 0x14031a8b0
0031AA7E  E9 62 FB FF FF                  jmp 0x14031a5e5
0031AA83  48 8B E8                        mov rbp, rax
0031AA86  49 3B C7                        cmp rax, r15
0031AA89  0F 85 AF FD FF FF               jne 0x14031a83e
0031AA8F  49 8D 75 40                     lea rsi, [r13 + 0x40]
0031AA93  41 BC 02 00 00 00               mov r12d, 2
0031AA99  E9 19 FA FF FF                  jmp 0x14031a4b7
0031AA9E  48 8D 0D F7 CB B1 00            lea rcx, [rip + 0xb1cbf7]
0031AAA5  E8 E6 DB F2 FF                  call 0x140248690
0031AAAA  0F B6 D0                        movzx edx, al
0031AAAD  48 8D 0D E8 CB B1 00            lea rcx, [rip + 0xb1cbe8]
0031AAB4  E8 07 D8 F2 FF                  call 0x1402482c0
0031AAB9  E9 00 FA FF FF                  jmp 0x14031a4be
0031AABE  8B CD                           mov ecx, ebp
0031AAC0  E9 6F FE FF FF                  jmp 0x14031a934
0031AAC5  8B CD                           mov ecx, ebp
0031AAC7  E9 68 FE FF FF                  jmp 0x14031a934
0031AACC  41 8B C4                        mov eax, r12d
0031AACF  E9 49 FF FF FF                  jmp 0x14031aa1d
0031AAD4  48 8B F7                        mov rsi, rdi
0031AAD7  E9 DB F9 FF FF                  jmp 0x14031a4b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0031A6F6(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0031A6F6(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031A6F6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
