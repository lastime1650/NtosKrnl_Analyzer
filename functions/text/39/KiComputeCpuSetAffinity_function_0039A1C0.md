# KiComputeCpuSetAffinity

- RVA: `0x0039A1C0`–`0x0039A843` (길이 `1,667` bytes)
- VA: `0x000000014039A1C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081838`
- 디코드: `409`개 명령, `1,667/1,667` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0039A20F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A223` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A235` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A256` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A278` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A293` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A2A6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A3B1` → [KiOrAffinityEx](KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x0039A483` → [KiOrAffinityEx](KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x0039A4D2` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A4E6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0039A55F` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0039A63B` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0039A654` → [KiAndAffinityEx](../3C/KiAndAffinityEx_function_003C0680.md) (function, `0x003C0680`)
- `0x0039A66F` → [KiCopyGroupMasksToAffinityEx](../41/KiCopyGroupMasksToAffinityEx_function_00415740.md) (function, `0x00415740`)
- `0x0039A67F` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x0039A695` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0039A6A8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039A734` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0039A7C0` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0039A7E0` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x0039A7FA` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0039A810` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0039A839` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)

### Direct callers
- [KiComputeThreadAffinity](KiComputeThreadAffinity_function_00399DE0.md) at `0x00399EFB`

### Static image references
- `0x0039A1E7` → RVA `0x00E0A740` (`.data`; read)
- `0x0039A2B5` → RVA `0x00FC5014` (`ALMOSTRO`; read)
- `0x0039A2DE` → RVA `0x00FC8320` (`ALMOSTRO`; read)
- `0x0039A4B0` → RVA `0x00FC6E68` (`ALMOSTRO`; read)
- `0x0039A665` → RVA `0x00FC81C0` (`ALMOSTRO`; read)
- `0x0039A6F0` → RVA `0x00FC6E18` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0039A7E7` → [sub_006E5A56](../6E/Unknown_function_006E5A56.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039A1C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039A1C5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0039A1CA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0039A1CF  55                              push rbp
0039A1D0  41 54                           push r12
0039A1D2  41 55                           push r13
0039A1D4  41 56                           push r14
0039A1D6  41 57                           push r15
0039A1D8  48 8D AC 24 90 FD FF FF         lea rbp, [rsp - 0x270]
0039A1E0  48 81 EC 70 03 00 00            sub rsp, 0x370
0039A1E7  48 8B 05 52 05 A7 00            mov rax, qword ptr [rip + 0xa70552]
0039A1EE  48 33 C4                        xor rax, rsp
0039A1F1  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
0039A1F8  48 8B DA                        mov rbx, rdx
0039A1FB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0039A200  4C 8B F1                        mov r14, rcx
0039A203  33 D2                           xor edx, edx
0039A205  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0039A209  41 B8 00 01 00 00               mov r8d, 0x100
0039A20F  E8 2C CA 32 00                  call 0x1406c6c40
0039A214  33 D2                           xor edx, edx
0039A216  48 8D 8D 58 01 00 00            lea rcx, [rbp + 0x158]
0039A21D  41 B8 00 01 00 00               mov r8d, 0x100
0039A223  E8 18 CA 32 00                  call 0x1406c6c40
0039A228  33 D2                           xor edx, edx
0039A22A  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0039A22F  41 B8 00 01 00 00               mov r8d, 0x100
0039A235  E8 06 CA 32 00                  call 0x1406c6c40
0039A23A  BF 20 00 00 00                  mov edi, 0x20
0039A23F  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0039A243  45 33 FF                        xor r15d, r15d
0039A246  66 89 7D 42                     mov word ptr [rbp + 0x42], di
0039A24A  33 D2                           xor edx, edx
0039A24C  44 89 7D 44                     mov dword ptr [rbp + 0x44], r15d
0039A250  41 B8 00 01 00 00               mov r8d, 0x100
0039A256  E8 E5 C9 32 00                  call 0x1406c6c40
0039A25B  33 D2                           xor edx, edx
0039A25D  48 C7 85 50 01 00 00 01 00 20 00  mov qword ptr [rbp + 0x150], 0x200001
0039A268  41 B8 00 01 00 00               mov r8d, 0x100
0039A26E  48 8D 8D 58 01 00 00            lea rcx, [rbp + 0x158]
0039A275  8D 77 E1                        lea esi, [rdi - 0x1f]
0039A278  E8 C3 C9 32 00                  call 0x1406c6c40
0039A27D  33 D2                           xor edx, edx
0039A27F  48 C7 44 24 30 01 00 20 00      mov qword ptr [rsp + 0x30], 0x200001
0039A288  41 B8 00 01 00 00               mov r8d, 0x100
0039A28E  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0039A293  E8 A8 C9 32 00                  call 0x1406c6c40
0039A298  44 0F B7 03                     movzx r8d, word ptr [rbx]
0039A29C  48 8D 4B 08                     lea rcx, [rbx + 8]
0039A2A0  49 C1 E0 03                     shl r8, 3
0039A2A4  33 D2                           xor edx, edx
0039A2A6  E8 95 C9 32 00                  call 0x1406c6c40
0039A2AB  66 89 33                        mov word ptr [rbx], si
0039A2AE  4D 8B BE 20 02 00 00            mov r15, qword ptr [r14 + 0x220]
0039A2B5  44 0F B7 25 57 AD C2 00         movzx r12d, word ptr [rip + 0xc2ad57]
0039A2BD  41 8B 87 FC 05 00 00            mov eax, dword ptr [r15 + 0x5fc]
0039A2C4  49 8D B7 C8 06 00 00            lea rsi, [r15 + 0x6c8]
0039A2CB  4D 8D AF D0 06 00 00            lea r13, [r15 + 0x6d0]
0039A2D2  84 C0                           test al, al
0039A2D4  0F 88 33 02 00 00               js 0x14039a50d
0039A2DA  0F B7 7D 42                     movzx edi, word ptr [rbp + 0x42]
0039A2DE  4C 8D 1D 3B E0 C2 00            lea r11, [rip + 0xc2e03b]
0039A2E5  66 44 3B E7                     cmp r12w, di
0039A2E9  41 0F B7 C4                     movzx eax, r12w
0039A2ED  66 0F 47 C7                     cmova ax, di
0039A2F1  45 33 D2                        xor r10d, r10d
0039A2F4  66 89 45 40                     mov word ptr [rbp + 0x40], ax
0039A2F8  41 0F B7 CA                     movzx ecx, r10w
0039A2FC  66 44 3B D0                     cmp r10w, ax
0039A300  73 26                           jae 0x14039a328
0039A302  48 8D 55 48                     lea rdx, [rbp + 0x48]
0039A306  44 0F B7 C8                     movzx r9d, ax
0039A30A  4D 8B C3                        mov r8, r11
0039A30D  0F B7 C8                        movzx ecx, ax
0039A310  49 8B 00                        mov rax, qword ptr [r8]
0039A313  4D 8D 40 10                     lea r8, [r8 + 0x10]
0039A317  48 89 02                        mov qword ptr [rdx], rax
0039A31A  48 8D 52 08                     lea rdx, [rdx + 8]
0039A31E  49 83 E9 01                     sub r9, 1
0039A322  75 EC                           jne 0x14039a310
0039A324  0F B7 7D 42                     movzx edi, word ptr [rbp + 0x42]
0039A328  66 3B CF                        cmp cx, di
0039A32B  73 17                           jae 0x14039a344
0039A32D  0F 1F 00                        nop dword ptr [rax]
0039A330  0F B7 C1                        movzx eax, cx
0039A333  66 FF C1                        inc cx
0039A336  4C 89 54 C5 48                  mov qword ptr [rbp + rax*8 + 0x48], r10
0039A33B  0F B7 7D 42                     movzx edi, word ptr [rbp + 0x42]
0039A33F  66 3B CF                        cmp cx, di
0039A342  72 EC                           jb 0x14039a330
0039A344  41 8B 86 A4 05 00 00            mov eax, dword ptr [r14 + 0x5a4]
0039A34B  C1 E8 0B                        shr eax, 0xb
0039A34E  83 E0 01                        and eax, 1
0039A351  74 6A                           je 0x14039a3bd
0039A353  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
0039A358  41 0F B7 D2                     movzx edx, r10w
0039A35C  66 45 3B E0                     cmp r12w, r8w
0039A360  66 45 0F 46 C4                  cmovbe r8w, r12w
0039A365  66 44 89 03                     mov word ptr [rbx], r8w
0039A369  66 45 3B D0                     cmp r10w, r8w
0039A36D  73 1C                           jae 0x14039a38b
0039A36F  44 8B C8                        mov r9d, eax
0039A372  0F B7 CA                        movzx ecx, dx
0039A375  66 FF C2                        inc dx
0039A378  49 8D 04 49                     lea rax, [r9 + rcx*2]
0039A37C  49 8B 04 C3                     mov rax, qword ptr [r11 + rax*8]
0039A380  48 89 44 CB 08                  mov qword ptr [rbx + rcx*8 + 8], rax
0039A385  66 41 3B D0                     cmp dx, r8w
0039A389  72 E7                           jb 0x14039a372
0039A38B  66 3B 53 02                     cmp dx, word ptr [rbx + 2]
0039A38F  73 11                           jae 0x14039a3a2
0039A391  0F B7 C2                        movzx eax, dx
0039A394  66 FF C2                        inc dx
0039A397  4C 89 54 C3 08                  mov qword ptr [rbx + rax*8 + 8], r10
0039A39C  66 3B 53 02                     cmp dx, word ptr [rbx + 2]
0039A3A0  72 EF                           jb 0x14039a391
0039A3A2  44 0F B7 CF                     movzx r9d, di
0039A3A6  4C 8D 45 40                     lea r8, [rbp + 0x40]
0039A3AA  48 8B D3                        mov rdx, rbx
0039A3AD  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0039A3B1  E8 96 04 00 00                  call 0x14039a84c
0039A3B6  0F B7 7D 42                     movzx edi, word ptr [rbp + 0x42]
0039A3BA  45 33 D2                        xor r10d, r10d
0039A3BD  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0039A3C1  41 0F B7 D4                     movzx edx, r12w
0039A3C5  66 44 3B E0                     cmp r12w, ax
0039A3C9  0F 87 06 04 00 00               ja 0x14039a7d5
0039A3CF  66 89 13                        mov word ptr [rbx], dx
0039A3D2  41 0F B7 CA                     movzx ecx, r10w
0039A3D6  66 44 3B D2                     cmp r10w, dx
0039A3DA  73 1F                           jae 0x14039a3fb
0039A3DC  4C 8B CB                        mov r9, rbx
0039A3DF  44 0F B7 C2                     movzx r8d, dx
0039A3E3  4C 2B CE                        sub r9, rsi
0039A3E6  0F B7 CA                        movzx ecx, dx
0039A3E9  48 8B 06                        mov rax, qword ptr [rsi]
0039A3EC  49 89 44 31 08                  mov qword ptr [r9 + rsi + 8], rax
0039A3F1  48 8D 76 08                     lea rsi, [rsi + 8]
0039A3F5  49 83 E8 01                     sub r8, 1
0039A3F9  75 EE                           jne 0x14039a3e9
0039A3FB  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
0039A3FF  73 11                           jae 0x14039a412
0039A401  0F B7 C1                        movzx eax, cx
0039A404  66 FF C1                        inc cx
0039A407  4C 89 54 C3 08                  mov qword ptr [rbx + rax*8 + 8], r10
0039A40C  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
0039A410  72 EF                           jb 0x14039a401
0039A412  41 F7 87 F0 01 00 00 00 00 00 08  test dword ptr [r15 + 0x1f0], 0x8000000
0039A41D  0F 85 BA 03 00 00               jne 0x14039a7dd
0039A423  0F B7 8D 52 01 00 00            movzx ecx, word ptr [rbp + 0x152]
0039A42A  41 B7 01                        mov r15b, 1
0039A42D  66 39 4D 40                     cmp word ptr [rbp + 0x40], cx
0039A431  44 0F B7 F1                     movzx r14d, cx
0039A435  44 89 95 54 01 00 00            mov dword ptr [rbp + 0x154], r10d
0039A43C  41 0F B7 F2                     movzx esi, r10w
0039A440  66 44 0F 46 75 40               cmovbe r14w, word ptr [rbp + 0x40]
0039A446  66 44 89 B5 50 01 00 00         mov word ptr [rbp + 0x150], r14w
0039A44E  66 45 3B D6                     cmp r10w, r14w
0039A452  0F 82 C9 02 00 00               jb 0x14039a721
0039A458  66 3B F1                        cmp si, cx
0039A45B  73 17                           jae 0x14039a474
0039A45D  0F B7 C6                        movzx eax, si
0039A460  66 FF C6                        inc si
0039A463  4C 89 94 C5 58 01 00 00         mov qword ptr [rbp + rax*8 + 0x158], r10
0039A46B  66 3B B5 52 01 00 00            cmp si, word ptr [rbp + 0x152]
0039A472  72 E9                           jb 0x14039a45d
0039A474  44 0F B7 CF                     movzx r9d, di
0039A478  4C 8D 45 40                     lea r8, [rbp + 0x40]
0039A47C  48 8B D3                        mov rdx, rbx
0039A47F  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0039A483  E8 C4 03 00 00                  call 0x14039a84c
0039A488  4C 8B 74 24 20                  mov r14, qword ptr [rsp + 0x20]
0039A48D  0F B7 55 40                     movzx edx, word ptr [rbp + 0x40]
0039A491  33 F6                           xor esi, esi
0039A493  0F B7 CE                        movzx ecx, si
0039A496  66 3B CA                        cmp cx, dx
0039A499  73 0F                           jae 0x14039a4aa
0039A49B  0F B7 C1                        movzx eax, cx
0039A49E  48 39 74 C5 48                  cmp qword ptr [rbp + rax*8 + 0x48], rsi
0039A4A3  75 74                           jne 0x14039a519
0039A4A5  66 FF C1                        inc cx
0039A4A8  EB EC                           jmp 0x14039a496
0039A4AA  44 0F B7 03                     movzx r8d, word ptr [rbx]
0039A4AE  EB 18                           jmp 0x14039a4c8
0039A4B0  39 35 B2 C9 C2 00               cmp dword ptr [rip + 0xc2c9b2], esi
0039A4B6  0F 85 9D 02 00 00               jne 0x14039a759
0039A4BC  45 84 FF                        test r15b, r15b
0039A4BF  0F 84 94 02 00 00               je 0x14039a759
0039A4C5  4C 8B C2                        mov r8, rdx
0039A4C8  49 C1 E0 03                     shl r8, 3
0039A4CC  48 8D 4B 08                     lea rcx, [rbx + 8]
0039A4D0  33 D2                           xor edx, edx
0039A4D2  E8 69 C7 32 00                  call 0x1406c6c40
0039A4D7  66 C7 03 01 00                  mov word ptr [rbx], 1
0039A4DC  48 8B 8D 60 02 00 00            mov rcx, qword ptr [rbp + 0x260]
0039A4E3  48 33 CC                        xor rcx, rsp
0039A4E6  E8 55 21 31 00                  call 0x1406ac640
0039A4EB  4C 8D 9C 24 70 03 00 00         lea r11, [rsp + 0x370]
0039A4F3  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0039A4F7  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0039A4FB  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0039A4FF  49 8B E3                        mov rsp, r11
0039A502  41 5F                           pop r15
0039A504  41 5E                           pop r14
0039A506  41 5D                           pop r13
0039A508  41 5C                           pop r12
0039A50A  5D                              pop rbp
0039A50B  C3                              ret
0039A50C  CC                              int3
0039A50D  48 8B 36                        mov rsi, qword ptr [rsi]
0039A510  4D 8B 6D 00                     mov r13, qword ptr [r13]
0039A514  E9 C1 FD FF FF                  jmp 0x14039a2da
0039A519  41 F7 86 A0 05 00 00 00 00 02 00  test dword ptr [r14 + 0x5a0], 0x20000
0039A524  49 8D 96 90 06 00 00            lea rdx, [r14 + 0x690]
0039A52B  0F 85 20 02 00 00               jne 0x14039a751
0039A531  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A537  41 0F B7 FC                     movzx edi, r12w
0039A53B  66 45 3B E1                     cmp r12w, r9w
0039A53F  0F 87 D5 02 00 00               ja 0x14039a81a
0039A545  66 89 7C 24 30                  mov word ptr [rsp + 0x30], di
0039A54A  0F B7 CE                        movzx ecx, si
0039A54D  66 3B F7                        cmp si, di
0039A550  73 20                           jae 0x14039a572
0039A552  44 0F B7 C7                     movzx r8d, di
0039A556  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0039A55B  49 C1 E0 03                     shl r8, 3
0039A55F  E8 DC C2 32 00                  call 0x1406c6840
0039A564  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A56A  0F B7 CF                        movzx ecx, di
0039A56D  0F B7 7C 24 30                  movzx edi, word ptr [rsp + 0x30]
0039A572  66 41 3B C9                     cmp cx, r9w
0039A576  73 24                           jae 0x14039a59c
0039A578  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0039A580  0F B7 C1                        movzx eax, cx
0039A583  66 FF C1                        inc cx
0039A586  48 89 74 C4 38                  mov qword ptr [rsp + rax*8 + 0x38], rsi
0039A58B  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A591  66 41 3B C9                     cmp cx, r9w
0039A595  72 E9                           jb 0x14039a580
0039A597  0F B7 7C 24 30                  movzx edi, word ptr [rsp + 0x30]
0039A59C  0F B7 CE                        movzx ecx, si
0039A59F  66 3B CF                        cmp cx, di
0039A5A2  73 13                           jae 0x14039a5b7
0039A5A4  0F B7 C1                        movzx eax, cx
0039A5A7  48 39 74 C4 38                  cmp qword ptr [rsp + rax*8 + 0x38], rsi
0039A5AC  0F 85 94 00 00 00               jne 0x14039a646
0039A5B2  66 FF C1                        inc cx
0039A5B5  EB E8                           jmp 0x14039a59f
0039A5B7  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0039A5BB  41 0F B7 D4                     movzx edx, r12w
0039A5BF  66 44 3B E0                     cmp r12w, ax
0039A5C3  0F 87 5A 02 00 00               ja 0x14039a823
0039A5C9  66 89 13                        mov word ptr [rbx], dx
0039A5CC  0F B7 CE                        movzx ecx, si
0039A5CF  66 3B F2                        cmp si, dx
0039A5D2  73 20                           jae 0x14039a5f4
0039A5D4  4C 8B D3                        mov r10, rbx
0039A5D7  44 0F B7 C2                     movzx r8d, dx
0039A5DB  4D 2B D5                        sub r10, r13
0039A5DE  0F B7 CA                        movzx ecx, dx
0039A5E1  49 8B 45 00                     mov rax, qword ptr [r13]
0039A5E5  4B 89 44 2A 08                  mov qword ptr [r10 + r13 + 8], rax
0039A5EA  4D 8D 6D 08                     lea r13, [r13 + 8]
0039A5EE  49 83 E8 01                     sub r8, 1
0039A5F2  75 ED                           jne 0x14039a5e1
0039A5F4  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
0039A5F8  73 17                           jae 0x14039a611
0039A5FA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0039A600  0F B7 C1                        movzx eax, cx
0039A603  66 FF C1                        inc cx
0039A606  48 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], rsi
0039A60B  66 3B 4B 02                     cmp cx, word ptr [rbx + 2]
0039A60F  72 EF                           jb 0x14039a600
0039A611  0F B7 13                        movzx edx, word ptr [rbx]
0039A614  0F B7 CE                        movzx ecx, si
0039A617  66 3B CA                        cmp cx, dx
0039A61A  0F 83 90 FE FF FF               jae 0x14039a4b0
0039A620  0F B7 C1                        movzx eax, cx
0039A623  48 39 74 C3 08                  cmp qword ptr [rbx + rax*8 + 8], rsi
0039A628  75 05                           jne 0x14039a62f
0039A62A  66 FF C1                        inc cx
0039A62D  EB E8                           jmp 0x14039a617
0039A62F  4C 8B C3                        mov r8, rbx
0039A632  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0039A637  41 0F B7 D1                     movzx edx, r9w
0039A63B  E8 20 42 F3 FF                  call 0x1402ce860
0039A640  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A646  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0039A64B  48 8D 55 40                     lea rdx, [rbp + 0x40]
0039A64F  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0039A654  E8 27 60 02 00                  call 0x1403c0680
0039A659  85 C0                           test eax, eax
0039A65B  0F 84 CA 01 00 00               je 0x14039a82b
0039A661  45 0F B7 C4                     movzx r8d, r12w
0039A665  48 8D 15 54 DB C2 00            lea rdx, [rip + 0xc2db54]
0039A66C  48 8B CB                        mov rcx, rbx
0039A66F  E8 CC B0 07 00                  call 0x140415740
0039A674  4C 8B C3                        mov r8, rbx
0039A677  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0039A67C  48 8B D3                        mov rdx, rbx
0039A67F  E8 BC 60 02 00                  call 0x1403c0740
0039A684  85 C0                           test eax, eax
0039A686  74 12                           je 0x14039a69a
0039A688  0F B7 54 24 32                  movzx edx, word ptr [rsp + 0x32]
0039A68D  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0039A692  4C 8B C3                        mov r8, rbx
0039A695  E8 C6 41 F3 FF                  call 0x1402ce860
0039A69A  44 0F B7 03                     movzx r8d, word ptr [rbx]
0039A69E  48 8D 4B 08                     lea rcx, [rbx + 8]
0039A6A2  49 C1 E0 03                     shl r8, 3
0039A6A6  33 D2                           xor edx, edx
0039A6A8  E8 93 C5 32 00                  call 0x1406c6c40
0039A6AD  44 0F B7 4B 02                  movzx r9d, word ptr [rbx + 2]
0039A6B2  44 0F B7 DE                     movzx r11d, si
0039A6B6  66 45 3B E1                     cmp r12w, r9w
0039A6BA  66 45 0F 46 CC                  cmovbe r9w, r12w
0039A6BF  66 44 89 0B                     mov word ptr [rbx], r9w
0039A6C3  66 41 3B F1                     cmp si, r9w
0039A6C7  0F 83 0F FE FF FF               jae 0x14039a4dc
0039A6CD  45 33 FF                        xor r15d, r15d
0039A6D0  41 0F B7 C3                     movzx eax, r11w
0039A6D4  48 8D 34 C3                     lea rsi, [rbx + rax*8]
0039A6D8  4C 89 7E 08                     mov qword ptr [rsi + 8], r15
0039A6DC  4C 8B 44 C4 38                  mov r8, qword ptr [rsp + rax*8 + 0x38]
0039A6E1  4D 85 C0                        test r8, r8
0039A6E4  74 2B                           je 0x14039a711
0039A6E6  41 0F B7 FB                     movzx edi, r11w
0039A6EA  4D 8B D7                        mov r10, r15
0039A6ED  C1 E7 06                        shl edi, 6
0039A6F0  48 8B 05 21 C7 C2 00            mov rax, qword ptr [rip + 0xc2c721]
0039A6F7  49 0F BC D0                     bsf rdx, r8
0039A6FB  8D 0C 17                        lea ecx, [rdi + rdx]
0039A6FE  4C 0B 14 C8                     or r10, qword ptr [rax + rcx*8]
0039A702  8B C2                           mov eax, edx
0039A704  49 0F B3 C0                     btr r8, rax
0039A708  4C 89 56 08                     mov qword ptr [rsi + 8], r10
0039A70C  4D 85 C0                        test r8, r8
0039A70F  75 DF                           jne 0x14039a6f0
0039A711  66 41 FF C3                     inc r11w
0039A715  66 45 3B D9                     cmp r11w, r9w
0039A719  0F 83 BD FD FF FF               jae 0x14039a4dc
0039A71F  EB AF                           jmp 0x14039a6d0
0039A721  45 0F B7 C6                     movzx r8d, r14w
0039A725  48 8D 55 48                     lea rdx, [rbp + 0x48]
0039A729  49 C1 E0 03                     shl r8, 3
0039A72D  48 8D 8D 58 01 00 00            lea rcx, [rbp + 0x158]
0039A734  E8 07 C1 32 00                  call 0x1406c6840
0039A739  66 FF C6                        inc si
0039A73C  66 41 3B F6                     cmp si, r14w
0039A740  72 F7                           jb 0x14039a739
0039A742  0F B7 8D 52 01 00 00            movzx ecx, word ptr [rbp + 0x152]
0039A749  45 33 D2                        xor r10d, r10d
0039A74C  E9 07 FD FF FF                  jmp 0x14039a458
0039A751  48 8B 12                        mov rdx, qword ptr [rdx]
0039A754  E9 D8 FD FF FF                  jmp 0x14039a531
0039A759  66 44 39 8D 50 01 00 00         cmp word ptr [rbp + 0x150], r9w
0039A761  41 0F B7 F1                     movzx esi, r9w
0039A765  66 0F 46 B5 50 01 00 00         cmovbe si, word ptr [rbp + 0x150]
0039A76D  45 33 FF                        xor r15d, r15d
0039A770  66 89 74 24 30                  mov word ptr [rsp + 0x30], si
0039A775  41 0F B7 FF                     movzx edi, r15w
0039A779  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
0039A77E  66 44 3B FE                     cmp r15w, si
0039A782  72 28                           jb 0x14039a7ac
0039A784  33 F6                           xor esi, esi
0039A786  66 41 3B F9                     cmp di, r9w
0039A78A  0F 83 B6 FE FF FF               jae 0x14039a646
0039A790  0F B7 C7                        movzx eax, di
0039A793  66 FF C7                        inc di
0039A796  48 89 74 C4 38                  mov qword ptr [rsp + rax*8 + 0x38], rsi
0039A79B  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A7A1  66 41 3B F9                     cmp di, r9w
0039A7A5  72 E9                           jb 0x14039a790
0039A7A7  E9 9A FE FF FF                  jmp 0x14039a646
0039A7AC  44 0F B7 C6                     movzx r8d, si
0039A7B0  48 8D 95 58 01 00 00            lea rdx, [rbp + 0x158]
0039A7B7  49 C1 E0 03                     shl r8, 3
0039A7BB  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0039A7C0  E8 7B C0 32 00                  call 0x1406c6840
0039A7C5  66 FF C7                        inc di
0039A7C8  66 3B FE                        cmp di, si
0039A7CB  72 F8                           jb 0x14039a7c5
0039A7CD  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
0039A7D3  EB AF                           jmp 0x14039a784
0039A7D5  0F B7 D0                        movzx edx, ax
0039A7D8  E9 F2 FB FF FF                  jmp 0x14039a3cf
0039A7DD  48 8B CB                        mov rcx, rbx
0039A7E0  E8 9B 6D F3 FF                  call 0x1402d1580
0039A7E5  85 C0                           test eax, eax
0039A7E7  0F 85 69 B2 34 00               jne 0x1406e5a56
0039A7ED  4C 8B C3                        mov r8, rbx
0039A7F0  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0039A7F4  0F B7 D7                        movzx edx, di
0039A7F7  45 32 FF                        xor r15b, r15b
0039A7FA  E8 61 40 F3 FF                  call 0x1402ce860
0039A7FF  0F B7 95 52 01 00 00            movzx edx, word ptr [rbp + 0x152]
0039A806  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
0039A80D  4C 8B C3                        mov r8, rbx
0039A810  E8 4B 40 F3 FF                  call 0x1402ce860
0039A815  E9 73 FC FF FF                  jmp 0x14039a48d
0039A81A  41 0F B7 F9                     movzx edi, r9w
0039A81E  E9 22 FD FF FF                  jmp 0x14039a545
0039A823  0F B7 D0                        movzx edx, ax
0039A826  E9 9E FD FF FF                  jmp 0x14039a5c9
0039A82B  0F B7 54 24 32                  movzx edx, word ptr [rsp + 0x32]
0039A830  4C 8D 45 40                     lea r8, [rbp + 0x40]
0039A834  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0039A839  E8 22 40 F3 FF                  call 0x1402ce860
0039A83E  E9 1E FE FF FF                  jmp 0x14039a661
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiComputeCpuSetAffinity(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int16 v_stack_m146;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int16 v_stack_m256;
    unsigned __int16 v_stack_m258;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m338;
    unsigned int v_stack_m33C;
    unsigned __int16 v_stack_m33E;
    unsigned __int16 v_stack_m340;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (880);
    result = (*(unsigned __int64 *)(v_rip + 10945874)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m378 = a1;
    a2 = 0;
    result = memset(v_stack_m250, a2, 256, a4);
    a2 = 0;
    result = memset(v_stack_m140, a2, 256, a4);
    a2 = 0;
    result = memset(v_stack_m360, a2, 256, a4);
    v_r15 = 0;
    v_stack_m256 = 32;
    a2 = 0;
    v_stack_m254 = 0;
    result = memset(v_stack_m250, a2, 256, a4);
    a2 = 0;
    v_stack_m148 = 0x200001ULL;
    result = memset(v_stack_m140, a2, 256, a4);
    a2 = 0;
    v_stack_m368 = 0x200001ULL;
    result = memset(v_stack_m360, a2, 256, a4);
    a3 = (*(unsigned __int16 *)(a2)) << (3);
    a2 = 0;
    result = memset(a2 + 8, a2, a3, a4);
    *(unsigned __int16 *)(a2) = (unsigned __int16)(32 - 31);
    if (sign_flag) goto loc_0039A50D;
loc_0039A2DA:
    result = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) > ((unsigned __int16)(v_stack_m256))) { result = (unsigned __int16)(v_stack_m256); }
    v_r10 = 0;
    v_stack_m258 = (unsigned __int16)(result);
    if (0 >= ((unsigned __int16)(result))) goto loc_0039A328;
loc_0039A310:
    *(unsigned __int64 *)(v_stack_m250) = *(unsigned __int64 *)(v_rip + 12771387);
    a4 = ((unsigned __int16)(result)) - (1);
    if (condition_is_not_equal) goto loc_0039A310;
loc_0039A328:
    if (((unsigned __int16)((unsigned __int16)(result))) >= ((unsigned __int16)(v_stack_m256))) goto loc_0039A344;
loc_0039A330:
    a1 = (unsigned __int16)(((unsigned __int16)(result)) + 1);
    *(unsigned __int64 *)(v_stack_m298 + (unsigned __int16)((unsigned __int16)(result)) * 8 + 72) = 0;
    if (((unsigned __int16)(a1)) < ((unsigned __int16)(v_stack_m256))) goto loc_0039A330;
loc_0039A344:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1444))) >> (11));
    result = (unsigned int)((result) & (1));
    if (condition_is_equal) goto loc_0039A3BD;
    a3 = *(unsigned __int16 *)(a2 + 2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) <= ((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) { a3 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)); }
    *(unsigned __int16 *)(a2) = (unsigned __int16)(a3);
    if (0 >= ((unsigned __int16)(a3))) goto loc_0039A38B;
loc_0039A372:
    a2 = (unsigned __int16)((0) + 1);
    *(unsigned __int64 *)(a2 + 0 * 8 + 8) = *(unsigned __int64 *)(v_rip + 12771387 + (unsigned int)((unsigned int)(result)) + 0 * 2 * 8);
    if (((unsigned __int16)(a2)) < ((unsigned __int16)(a3))) goto loc_0039A372;
loc_0039A38B:
    if (((unsigned __int16)(a2)) >= (*(unsigned __int16 *)(a2 + 2))) goto loc_0039A3A2;
loc_0039A391:
    a2 = (unsigned __int16)((a2) + 1);
    *(unsigned __int64 *)(a2 + (unsigned __int16)(a2) * 8 + 8) = 0;
    if (((unsigned __int16)(a2)) < (*(unsigned __int16 *)(a2 + 2))) goto loc_0039A391;
loc_0039A3A2:
    result = KiOrAffinityEx(v_stack_m258, a2, v_stack_m258, (unsigned __int16)(v_stack_m256));
    v_r10 = 0;
loc_0039A3BD:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) > ((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) goto loc_0039A7D5;
loc_0039A3CF:
    *(unsigned __int16 *)(a2) = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)));
    if (0 >= ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))))) goto loc_0039A3FB;
    a4 = (a2) - (*(unsigned __int64 *)(a1 + 544) + 1736);
loc_0039A3E9:
    *(unsigned __int64 *)(a4 + *(unsigned __int64 *)(a1 + 544) + 1736 * 1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1736);
    a3 = ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) - (1);
    if (condition_is_not_equal) goto loc_0039A3E9;
loc_0039A3FB:
    if (((unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))))) >= (*(unsigned __int16 *)(a2 + 2))) goto loc_0039A412;
loc_0039A401:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) + 1);
    *(unsigned __int64 *)(a2 + (unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) * 8 + 8) = 0;
    if (((unsigned __int16)(a1)) < (*(unsigned __int16 *)(a2 + 2))) goto loc_0039A401;
loc_0039A412:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 544) + 496)) & (0x8000000ULL)) != 0) goto loc_0039A7DD;
    v_stack_m144 = 0;
    v_r14 = (unsigned __int16)(v_stack_m146);
    if (v_stack_m258 <= ((unsigned __int16)(v_stack_m146))) { v_r14 = v_stack_m258; }
    v_stack_m148 = (unsigned __int16)(v_r14);
    if (0 < ((unsigned __int16)(v_r14))) goto loc_0039A721;
loc_0039A458:
    if (0 >= ((unsigned __int16)(v_stack_m146))) goto loc_0039A474;
loc_0039A45D:
    v_rsi = (unsigned __int16)((0) + 1);
    *(unsigned __int64 *)(v_stack_m298 + 0 * 8 + 344) = 0;
    if (((unsigned __int16)(v_rsi)) < v_stack_m146) goto loc_0039A45D;
loc_0039A474:
    result = KiOrAffinityEx(v_stack_m258, a2, v_stack_m258, (unsigned __int16)(v_stack_m256));
loc_0039A48D:
    v_rsi = 0;
loc_0039A496:
    if (0 >= ((unsigned __int16)(v_stack_m258))) goto loc_0039A4AA;
    if ((*(unsigned __int64 *)(v_stack_m298 + 0 * 8 + 72)) != 0) goto loc_0039A519;
    a1 = (unsigned __int16)((0) + 1);
    goto loc_0039A496;
loc_0039A4AA:
    goto loc_0039A4C8;
loc_0039A4B0:
    if ((*(unsigned int *)(v_rip + 12765618)) != 0) goto loc_0039A759;
    if (1 == 0) goto loc_0039A759;
loc_0039A4C8:
    a3 = (v_stack_m258) << (3);
    a2 = 0;
    result = memset(a2 + 8, a2, a3, (unsigned __int16)(v_stack_m256));
    *(unsigned __int16 *)(a2) = 1;
loc_0039A4DC:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned __int16)(v_stack_m256));
    return result;
loc_0039A50D:
    goto loc_0039A2DA;
loc_0039A519:
    if (((*(unsigned int *)(v_stack_m378 + 1440)) & (0x20000ULL)) != 0) goto loc_0039A751;
loc_0039A531:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) > ((unsigned __int16)(v_stack_m33E))) goto loc_0039A81A;
loc_0039A545:
    v_stack_m340 = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)));
    v_rdi = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359));
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) < ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))))) {
        a3 = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)));
        a1 = v_stack_m338;
        a3 = (a3) << (3);
        result = memcpy(a1, v_stack_m378 + 1680, a3, v_stack_m33E);
        a4 = v_stack_m33E;
        a1 = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)));
        v_rdi = v_stack_m340;
    }
    if (((unsigned __int16)(a1)) >= ((unsigned __int16)(a4))) goto loc_0039A59C;
loc_0039A580:
    a1 = (unsigned __int16)((a1) + 1);
    *(unsigned __int64 *)(v_stack_m28 + (unsigned __int16)(a1) * 8 + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if (((unsigned __int16)(a1)) < ((unsigned __int16)(v_stack_m33E))) goto loc_0039A580;
loc_0039A59C:
loc_0039A59F:
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) >= ((unsigned __int16)(v_stack_m340))) goto loc_0039A5B7;
    if ((*(unsigned __int64 *)(v_stack_m28 + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 56)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_0039A646;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) + 1);
    goto loc_0039A59F;
loc_0039A5B7:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) > ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 2)))) goto loc_0039A823;
loc_0039A5C9:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48)) = (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)));
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) >= ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))))) goto loc_0039A5F4;
    v_r10 = (*(unsigned __int64 *)(v_stack_m28 + 48)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1744));
loc_0039A5E1:
    *(unsigned __int64 *)(v_r10 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1744) * 1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1744));
    a3 = ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) - (1);
    if (condition_is_not_equal) goto loc_0039A5E1;
loc_0039A5F4:
    if (((unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 2))) goto loc_0039A611;
loc_0039A600:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + (unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)))) * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if (((unsigned __int16)(a1)) < (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 2))) goto loc_0039A600;
loc_0039A611:
loc_0039A617:
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48))))) goto loc_0039A4B0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_0039A62F;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) + 1);
    goto loc_0039A617;
loc_0039A62F:
    result = KiCopyAffinityEx(v_stack_m340, (unsigned __int16)(v_stack_m33E), *(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m33E);
loc_0039A646:
    result = KiAndAffinityEx(v_stack_m340, v_stack_m258, v_stack_m340, v_stack_m33E);
    if ((unsigned int)(result) == 0) goto loc_0039A82B;
loc_0039A661:
    result = KiCopyGroupMasksToAffinityEx(*(unsigned __int64 *)(v_stack_m28 + 48), v_rip + 12770132, (unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)), v_stack_m33E);
    result = KeAndAffinityEx2(v_stack_m340, *(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m33E);
    if ((unsigned int)(result) != 0) {
        a2 = v_stack_m33E;
        a1 = v_stack_m340;
        a3 = *(unsigned __int64 *)(v_stack_m28 + 48);
        result = KiCopyAffinityEx(a1, a2, a3, v_stack_m33E);
    }
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48))) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_stack_m28 + 48) + 8, a2, a3, v_stack_m33E);
    a4 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359))) <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 2)))) { a4 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 12758359)); }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48)) = (unsigned __int16)(a4);
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) >= ((unsigned __int16)(a4))) goto loc_0039A4DC;
    v_r15 = 0;
loc_0039A6D0:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 8) = 0;
    if (*(unsigned __int64 *)(v_stack_m28 + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 56) == 0) goto loc_0039A711;
    v_rdi = (unsigned int)(((unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64))))) << (6));
loc_0039A6F0:
    v_r10 = (0) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12764961) + v_rdi + a2 * 1 * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 8) = v_r10;
    if (*(unsigned __int64 *)(v_stack_m28 + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8 + 56) != 0) goto loc_0039A6F0;
loc_0039A711:
    v_r11 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) + 1);
    if (((unsigned __int16)(v_r11)) >= ((unsigned __int16)(a4))) goto loc_0039A4DC;
    goto loc_0039A6D0;
loc_0039A721:
    a3 = ((unsigned __int16)(v_stack_m378)) << (3);
    result = memcpy(v_stack_m140, v_stack_m250, a3, a4);
loc_0039A739:
    v_rsi = (unsigned __int16)((*(unsigned __int64 *)(v_stack_m28 + 48) + (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)))) * 8) + 1);
    if (((unsigned __int16)(v_rsi)) < ((unsigned __int16)(v_stack_m378))) goto loc_0039A739;
    v_r10 = 0;
    goto loc_0039A458;
loc_0039A751:
    goto loc_0039A531;
loc_0039A759:
    v_rsi = (unsigned __int16)(a4);
    if (v_stack_m148 <= ((unsigned __int16)(a4))) { v_rsi = v_stack_m148; }
    v_r15 = 0;
    v_stack_m340 = (unsigned __int16)(v_rsi);
    v_stack_m33C = 0;
    if (0 < ((unsigned __int16)(v_rsi))) goto loc_0039A7AC;
loc_0039A784:
    v_rsi = 0;
    if (0 >= ((unsigned __int16)(a4))) goto loc_0039A646;
loc_0039A790:
    v_rdi = (unsigned __int16)((0) + 1);
    *(unsigned __int64 *)(v_stack_m28 + 0 * 8 + 56) = 0;
    if (((unsigned __int16)(v_rdi)) < ((unsigned __int16)(v_stack_m33E))) goto loc_0039A790;
    goto loc_0039A646;
loc_0039A7AC:
    a3 = (0) << (3);
    result = memcpy(v_stack_m338, v_stack_m140, a3, v_stack_m33E);
loc_0039A7C5:
    v_rdi = (unsigned __int16)((v_rdi) + 1);
    if (((unsigned __int16)(v_rdi)) < 0) goto loc_0039A7C5;
    goto loc_0039A784;
loc_0039A7D5:
    goto loc_0039A3CF;
loc_0039A7DD:
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(v_stack_m28 + 48), (unsigned __int16)(result), a3, v_stack_m33E);
    v_r15 = 0;
    result = KiCopyAffinityEx(v_stack_m258, (unsigned __int16)(v_rdi), *(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m33E);
    result = KiCopyAffinityEx(v_stack_m148, v_stack_m146, *(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m33E);
    goto loc_0039A48D;
loc_0039A81A:
    goto loc_0039A545;
loc_0039A823:
    goto loc_0039A5C9;
loc_0039A82B:
    result = KiCopyAffinityEx(v_stack_m340, v_stack_m33E, v_stack_m258, v_stack_m33E);
    goto loc_0039A661;
}
```

## 5. (Beta) C Style

```c
int64_t KiComputeCpuSetAffinity(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint16_t v_stack_m146;
    uint64_t v_stack_m148;
    uint64_t v_stack_m250;
    uint32_t v_stack_m254;
    uint16_t v_stack_m256;
    uint16_t v_stack_m258;
    uint64_t v_stack_m28;
    uint64_t v_stack_m298;
    uint64_t v_stack_m338;
    uint32_t v_stack_m33C;
    uint16_t v_stack_m33E;
    uint16_t v_stack_m340;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m378;
    uint64_t v_stack_m38;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (880);
    result = (*(uint64_t *)(v_rip + 0xA70552)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m378 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m250, Arg2, 256, a4);
    Arg2 = 0;
    result = memset(v_stack_m140, Arg2, 256, a4);
    Arg2 = 0;
    result = memset(v_stack_m360, Arg2, 256, a4);
    local_r15 = 0;
    v_stack_m256 = 32;
    Arg2 = 0;
    v_stack_m254 = 0;
    result = memset(v_stack_m250, Arg2, 256, a4);
    Arg2 = 0;
    v_stack_m148 = 0x200001ULL;
    result = memset(v_stack_m140, Arg2, 256, a4);
    Arg2 = 0;
    v_stack_m368 = 0x200001ULL;
    result = memset(v_stack_m360, Arg2, 256, a4);
    a3 = (*(uint16_t *)(arg2)) << (3);
    Arg2 = 0;
    result = memset(Arg2 + 8, Arg2, a3, a4);
    *(uint16_t *)(arg2) = (uint16_t)(32 - 31);
    if (sign_flag) goto loc_0039A50D;
loc_0039A2DA:
    result = (uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57));
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) > ((uint16_t)(v_stack_m256))) { result = (uint16_t)(v_stack_m256); }
    local_r10 = 0;
    v_stack_m258 = (uint16_t)(result);
    if (0 >= ((uint16_t)(result))) goto loc_0039A328;
loc_0039A310:
    *(uint64_t *)(v_stack_m250) = *(uint64_t *)(v_rip + 0xC2E03B);
    a4 = ((uint16_t)(result)) - (1);
    if (condition_is_not_equal) goto loc_0039A310;
loc_0039A328:
    if (((uint16_t)((uint16_t)(result))) >= ((uint16_t)(v_stack_m256))) goto loc_0039A344;
loc_0039A330:
    Arg1 = (uint16_t)(((uint16_t)(result)) + 1);
    *(uint64_t *)(v_stack_m298 + (uint16_t)((uint16_t)(result)) * 8 + 0x48) = 0;
    if (((uint16_t)(Arg1)) < ((uint16_t)(v_stack_m256))) goto loc_0039A330;
loc_0039A344:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x5A4))) >> (11));
    result = (uint32_t)((result) & (1));
    if (condition_is_equal) goto loc_0039A3BD;
    a3 = *(uint16_t *)(arg2 + 0x2);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) <= ((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) { a3 = (uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)); }
    *(uint16_t *)(arg2) = (uint16_t)(a3);
    if (0 >= ((uint16_t)(a3))) goto loc_0039A38B;
loc_0039A372:
    Arg2 = (uint16_t)((0) + 1);
    *(uint64_t *)(arg2 + 0x0 * 8 + 0x8) = *(uint64_t *)(v_rip + 0xC2E03B + (uint32_t)((uint32_t)(result)) + 0x0 * 2 * 8);
    if (((uint16_t)(Arg2)) < ((uint16_t)(a3))) goto loc_0039A372;
loc_0039A38B:
    if (((uint16_t)(Arg2)) >= (*(uint16_t *)(arg2 + 0x2))) goto loc_0039A3A2;
loc_0039A391:
    Arg2 = (uint16_t)((Arg2) + 1);
    *(uint64_t *)(arg2 + (uint16_t)(arg2) * 8 + 0x8) = 0;
    if (((uint16_t)(Arg2)) < (*(uint16_t *)(arg2 + 0x2))) goto loc_0039A391;
loc_0039A3A2:
    result = KiOrAffinityEx(v_stack_m258, Arg2, v_stack_m258, (uint16_t)(v_stack_m256));
    local_r10 = 0;
loc_0039A3BD:
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) > ((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) goto loc_0039A7D5;
loc_0039A3CF:
    *(uint16_t *)(arg2) = (uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)));
    if (0 >= ((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))))) goto loc_0039A3FB;
    a4 = (Arg2) - (*(uint64_t *)(arg1 + 0x220) + 1736);
loc_0039A3E9:
    *(uint64_t *)(a4 + *(uint64_t *)(arg1 + 0x220) + 0x6C8 * 1 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x6C8);
    a3 = ((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) - (1);
    if (condition_is_not_equal) goto loc_0039A3E9;
loc_0039A3FB:
    if (((uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))))) >= (*(uint16_t *)(arg2 + 0x2))) goto loc_0039A412;
loc_0039A401:
    Arg1 = (uint16_t)(((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) + 1);
    *(uint64_t *)(arg2 + (uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) * 8 + 0x8) = 0;
    if (((uint16_t)(Arg1)) < (*(uint16_t *)(arg2 + 0x2))) goto loc_0039A401;
loc_0039A412:
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x220) + 0x1F0)) & (0x8000000ULL)) != 0) goto loc_0039A7DD;
    v_stack_m144 = 0;
    local_r14 = (uint16_t)(v_stack_m146);
    if (v_stack_m258 <= ((uint16_t)(v_stack_m146))) { local_r14 = v_stack_m258; }
    v_stack_m148 = (uint16_t)(local_r14);
    if (0 < ((uint16_t)(local_r14))) goto loc_0039A721;
loc_0039A458:
    if (0 >= ((uint16_t)(v_stack_m146))) goto loc_0039A474;
loc_0039A45D:
    local_rsi = (uint16_t)((0) + 1);
    *(uint64_t *)(v_stack_m298 + 0x0 * 8 + 0x158) = 0;
    if (((uint16_t)(local_rsi)) < v_stack_m146) goto loc_0039A45D;
loc_0039A474:
    result = KiOrAffinityEx(v_stack_m258, Arg2, v_stack_m258, (uint16_t)(v_stack_m256));
loc_0039A48D:
    local_rsi = 0;
loc_0039A496:
    if (0 >= ((uint16_t)(v_stack_m258))) goto loc_0039A4AA;
    if ((*(uint64_t *)(v_stack_m298 + 0x0 * 8 + 0x48)) != 0) goto loc_0039A519;
    Arg1 = (uint16_t)((0) + 1);
    goto loc_0039A496;
loc_0039A4AA:
    goto loc_0039A4C8;
loc_0039A4B0:
    if ((*(uint32_t *)(v_rip + 0xC2C9B2)) != 0) goto loc_0039A759;
    if (1 == 0) goto loc_0039A759;
loc_0039A4C8:
    a3 = (v_stack_m258) << (3);
    Arg2 = 0;
    result = memset(Arg2 + 8, Arg2, a3, (uint16_t)(v_stack_m256));
    *(uint16_t *)(arg2) = 1;
loc_0039A4DC:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, (uint16_t)(v_stack_m256));
    return result;
loc_0039A50D:
    goto loc_0039A2DA;
loc_0039A519:
    if (((*(uint32_t *)(v_stack_m378 + 0x5A0)) & (0x20000ULL)) != 0) goto loc_0039A751;
loc_0039A531:
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) > ((uint16_t)(v_stack_m33E))) goto loc_0039A81A;
loc_0039A545:
    v_stack_m340 = (uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)));
    local_rdi = (uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57));
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) < ((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))))) {
        a3 = (uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)));
        Arg1 = v_stack_m338;
        a3 = (a3) << (3);
        result = memcpy(Arg1, v_stack_m378 + 1680, a3, v_stack_m33E);
        a4 = v_stack_m33E;
        Arg1 = (uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)));
        local_rdi = v_stack_m340;
    }
    if (((uint16_t)(Arg1)) >= ((uint16_t)(a4))) goto loc_0039A59C;
loc_0039A580:
    Arg1 = (uint16_t)((Arg1) + 1);
    *(uint64_t *)(v_stack_m28 + (uint16_t)(arg1) * 8 + 0x38) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40));
    if (((uint16_t)(Arg1)) < ((uint16_t)(v_stack_m33E))) goto loc_0039A580;
loc_0039A59C:
loc_0039A59F:
    if (((uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) >= ((uint16_t)(v_stack_m340))) goto loc_0039A5B7;
    if ((*(uint64_t *)(v_stack_m28 + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x38)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_0039A646;
    Arg1 = (uint16_t)(((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) + 1);
    goto loc_0039A59F;
loc_0039A5B7:
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) > ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x2)))) goto loc_0039A823;
loc_0039A5C9:
    *(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30)) = (uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)));
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) >= ((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))))) goto loc_0039A5F4;
    local_r10 = (*(uint64_t *)(v_stack_m28 + 0x30)) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x6D0));
loc_0039A5E1:
    *(uint64_t *)(local_r10 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x6D0) * 1 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x6D0));
    a3 = ((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) - (1);
    if (condition_is_not_equal) goto loc_0039A5E1;
loc_0039A5F4:
    if (((uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))))) >= (*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x2))) goto loc_0039A611;
loc_0039A600:
    Arg1 = (uint16_t)(((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) + 1);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + (uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)))) * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40));
    if (((uint16_t)(Arg1)) < (*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x2))) goto loc_0039A600;
loc_0039A611:
loc_0039A617:
    if (((uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30))))) goto loc_0039A4B0;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_0039A62F;
    Arg1 = (uint16_t)(((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) + 1);
    goto loc_0039A617;
loc_0039A62F:
    result = KiCopyAffinityEx(v_stack_m340, (uint16_t)(v_stack_m33E), *(uint64_t *)(v_stack_m28 + 0x30), v_stack_m33E);
loc_0039A646:
    result = KiAndAffinityEx(v_stack_m340, v_stack_m258, v_stack_m340, v_stack_m33E);
    if ((uint32_t)(result) == 0) goto loc_0039A82B;
loc_0039A661:
    result = KiCopyGroupMasksToAffinityEx(*(uint64_t *)(v_stack_m28 + 0x30), v_rip + 12770132, (uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)), v_stack_m33E);
    result = KeAndAffinityEx2(v_stack_m340, *(uint64_t *)(v_stack_m28 + 0x30), *(uint64_t *)(v_stack_m28 + 0x30), v_stack_m33E);
    if ((uint32_t)(result) != 0) {
        Arg2 = v_stack_m33E;
        Arg1 = v_stack_m340;
        a3 = *(uint64_t *)(v_stack_m28 + 0x30);
        result = KiCopyAffinityEx(Arg1, Arg2, a3, v_stack_m33E);
    }
    a3 = (*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30))) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_stack_m28 + 0x30) + 8, Arg2, a3, v_stack_m33E);
    a4 = *(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x2);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57))) <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x2)))) { a4 = (uint16_t)(*(uint16_t *)(v_rip + 0xC2AD57)); }
    *(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30)) = (uint16_t)(a4);
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) >= ((uint16_t)(a4))) goto loc_0039A4DC;
    local_r15 = 0;
loc_0039A6D0:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x8) = 0;
    if (*(uint64_t *)(v_stack_m28 + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x38) == 0) goto loc_0039A711;
    local_rdi = (uint32_t)(((uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40))))) << (6));
loc_0039A6F0:
    local_r10 = (0) | (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC2C721) + local_rdi + arg2 * 1 * 8));
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x8) = local_r10;
    if (*(uint64_t *)(v_stack_m28 + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8 + 0x38) != 0) goto loc_0039A6F0;
loc_0039A711:
    local_r11 = (uint16_t)(((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) + 1);
    if (((uint16_t)(local_r11)) >= ((uint16_t)(a4))) goto loc_0039A4DC;
    goto loc_0039A6D0;
loc_0039A721:
    a3 = ((uint16_t)(v_stack_m378)) << (3);
    result = memcpy(v_stack_m140, v_stack_m250, a3, a4);
loc_0039A739:
    local_rsi = (uint16_t)((*(uint64_t *)(v_stack_m28 + 0x30) + (uint16_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)))) * 8) + 1);
    if (((uint16_t)(local_rsi)) < ((uint16_t)(v_stack_m378))) goto loc_0039A739;
    local_r10 = 0;
    goto loc_0039A458;
loc_0039A751:
    goto loc_0039A531;
loc_0039A759:
    local_rsi = (uint16_t)(a4);
    if (v_stack_m148 <= ((uint16_t)(a4))) { local_rsi = v_stack_m148; }
    local_r15 = 0;
    v_stack_m340 = (uint16_t)(local_rsi);
    v_stack_m33C = 0;
    if (0 < ((uint16_t)(local_rsi))) goto loc_0039A7AC;
loc_0039A784:
    local_rsi = 0;
    if (0 >= ((uint16_t)(a4))) goto loc_0039A646;
loc_0039A790:
    local_rdi = (uint16_t)((0) + 1);
    *(uint64_t *)(v_stack_m28 + 0x0 * 8 + 0x38) = 0;
    if (((uint16_t)(local_rdi)) < ((uint16_t)(v_stack_m33E))) goto loc_0039A790;
    goto loc_0039A646;
loc_0039A7AC:
    a3 = (0) << (3);
    result = memcpy(v_stack_m338, v_stack_m140, a3, v_stack_m33E);
loc_0039A7C5:
    local_rdi = (uint16_t)((local_rdi) + 1);
    if (((uint16_t)(local_rdi)) < 0) goto loc_0039A7C5;
    goto loc_0039A784;
loc_0039A7D5:
    goto loc_0039A3CF;
loc_0039A7DD:
    result = KeIsEmptyAffinityEx(*(uint64_t *)(v_stack_m28 + 0x30), (uint16_t)(result), a3, v_stack_m33E);
    local_r15 = 0;
    result = KiCopyAffinityEx(v_stack_m258, (uint16_t)(local_rdi), *(uint64_t *)(v_stack_m28 + 0x30), v_stack_m33E);
    result = KiCopyAffinityEx(v_stack_m148, v_stack_m146, *(uint64_t *)(v_stack_m28 + 0x30), v_stack_m33E);
    goto loc_0039A48D;
loc_0039A81A:
    goto loc_0039A545;
loc_0039A823:
    goto loc_0039A5C9;
loc_0039A82B:
    result = KiCopyAffinityEx(v_stack_m340, v_stack_m33E, v_stack_m258, v_stack_m33E);
    goto loc_0039A661;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x5A4` | `32` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `16` | `W` |
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x8 + r13*1` | `64` | `W` |
| `Arg2` | `+ 0x8 + rax*8` | `64` | `R` |
| `Arg2` | `+ 0x8 + rax*8` | `64` | `W` |
| `Arg2` | `+ 0x8 + rcx*8` | `64` | `W` |
| `Arg2` | `+ 0x8 + rsi*1` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039A1C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
