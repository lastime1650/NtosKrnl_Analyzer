# MiSnapDriverRange

- RVA: `0x00A4B328`–`0x00A4B786` (길이 `1,118` bytes)
- VA: `0x0000000140A4B328`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B0204`
- 디코드: `269`개 명령, `1,118/1,118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A4B3A5` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00A4B50E` → [MmImageSectionPagable](MmImageSectionPagable_function_00A4B78C.md) (function, `0x00A4B78C`)
- `0x00A4B556` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00A4B579` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00A4B5E5` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00A4B610` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A4B6B8` → [MiIsKernelHalPadSection](../../text/4C/MiIsKernelHalPadSection_function_004CCFB0.md) (function, `0x004CCFB0`)
- `0x00A4B6C7` → [MmImageSectionPagable](MmImageSectionPagable_function_00A4B78C.md) (function, `0x00A4B78C`)

### Direct callers
- [MmProtectDriverSection](../../text/67/MmProtectDriverSection_function_00670A80.md) at `0x00670BB4`
- [MiCheckForDiscardableLongJumpTable](../../text/68/MiCheckForDiscardableLongJumpTable_function_0068F748.md) at `0x0068F784`
- [MiBackSingleImageWithPagefile](../7F/MiBackSingleImageWithPagefile_function_007F8664.md) at `0x007F869F`
- [MiLockRegistryRecoverySection](../7F/MiLockRegistryRecoverySection_function_007F8C10.md) at `0x007F8C4D`
- [MiIdentifyImageDiscardablePages](../80/MiIdentifyImageDiscardablePages_function_00803DB4.md) at `0x00803E5D`
- [MiHandleDriverNonPagedSections](MiHandleDriverNonPagedSections_function_00A4AEA8.md) at `0x00A4AFF5`
- [MiDisablePagingOfDriver](MiDisablePagingOfDriver_function_00A4B074.md) at `0x00A4B0CE`
- [MiFreeDriverInitialization](MiFreeDriverInitialization_function_00A4B120.md) at `0x00A4B17D`
- [MiMarkKernelImageCfgBits](MiMarkKernelImageCfgBits_function_00A4B1E0.md) at `0x00A4B296`
- [MiEnablePagingOfDriver](../../init/C5/MiEnablePagingOfDriver_function_00C5F550.md) at `0x00C5F59E`
- [MmDiscardDriverSection](../../init/C6/MmDiscardDriverSection_function_00C6C8D0.md) at `0x00C6C93B`

### Static image references
- `0x00A4B341` → RVA `0x00E0A740` (`.data`; read)
- `0x00A4B69F` → RVA `0x00FC6B28` (`ALMOSTRO`; read)
- `0x00A4B6A8` → RVA `0x00FC6B98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00A4B3A5` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00A4B556` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x00A4B579` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x00A4B5E5` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x00A4B610` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A4B6B8` → [MiIsKernelHalPadSection](../../text/4C/MiIsKernelHalPadSection_function_004CCFB0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00A4B6BF` → [sub_00B3B816](../B3/Unknown_function_00B3B816.md) (`tail-transfer`)
  - `0x00A4B706` → [sub_00B3B816](../B3/Unknown_function_00B3B816.md) (`tail-transfer`)
  - `0x00A4B754` → [sub_00B3B816](../B3/Unknown_function_00B3B816.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A4B328  4C 8B DC                        mov r11, rsp
00A4B32B  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
00A4B32F  55                              push rbp
00A4B330  56                              push rsi
00A4B331  57                              push rdi
00A4B332  41 54                           push r12
00A4B334  41 55                           push r13
00A4B336  41 56                           push r14
00A4B338  41 57                           push r15
00A4B33A  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A4B341  48 8B 05 F8 F3 3B 00            mov rax, qword ptr [rip + 0x3bf3f8]
00A4B348  48 33 C4                        xor rax, rsp
00A4B34B  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00A4B353  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00A4B35B  33 F6                           xor esi, esi
00A4B35D  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00A4B365  0F 57 C0                        xorps xmm0, xmm0
00A4B368  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A4B36D  49 8B F9                        mov rdi, r9
00A4B370  49 89 73 98                     mov qword ptr [r11 - 0x68], rsi
00A4B374  45 8B E0                        mov r12d, r8d
00A4B377  48 89 33                        mov qword ptr [rbx], rsi
00A4B37A  44 8B FA                        mov r15d, edx
00A4B37D  48 89 30                        mov qword ptr [rax], rsi
00A4B380  F3 0F 7F 44 24 7C               movdqu xmmword ptr [rsp + 0x7c], xmm0
00A4B386  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A4B38B  48 8B 59 30                     mov rbx, qword ptr [rcx + 0x30]
00A4B38F  48 8B CB                        mov rcx, rbx
00A4B392  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00A4B397  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A4B39C  49 89 73 B4                     mov qword ptr [r11 - 0x4c], rsi
00A4B3A0  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00A4B3A5  E8 B6 87 9F FF                  call 0x140443b60
00A4B3AA  48 8B D0                        mov rdx, rax
00A4B3AD  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A4B3B2  4C 8B D7                        mov r10, rdi
00A4B3B5  4C 2B D3                        sub r10, rbx
00A4B3B8  44 8B 58 38                     mov r11d, dword ptr [rax + 0x38]
00A4B3BC  B8 00 10 00 00                  mov eax, 0x1000
00A4B3C1  44 0F B7 4A 06                  movzx r9d, word ptr [rdx + 6]
00A4B3C6  4C 3B D8                        cmp r11, rax
00A4B3C9  45 8B F3                        mov r14d, r11d
00A4B3CC  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00A4B3D1  44 0F 47 F0                     cmova r14d, eax
00A4B3D5  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00A4B3DA  44 89 4C 24 24                  mov dword ptr [rsp + 0x24], r9d
00A4B3DF  45 3B F9                        cmp r15d, r9d
00A4B3E2  0F 87 1B 02 00 00               ja 0x140a4b603
00A4B3E8  44 0F B7 42 14                  movzx r8d, word ptr [rdx + 0x14]
00A4B3ED  4A 8D 3C 8D 03 00 00 00         lea rdi, [r9*4 + 3]
00A4B3F5  49 03 F9                        add rdi, r9
00A4B3F8  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
00A4B3FD  C7 84 24 94 00 00 00 00 00 00 40  mov dword ptr [rsp + 0x94], 0x40000000
00A4B408  8B EE                           mov ebp, esi
00A4B40A  44 8B EE                        mov r13d, esi
00A4B40D  49 8D 3C F8                     lea rdi, [r8 + rdi*8]
00A4B411  48 03 FA                        add rdi, rdx
00A4B414  8B C7                           mov eax, edi
00A4B416  2B C3                           sub eax, ebx
00A4B418  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00A4B41F  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00A4B423  45 3B F9                        cmp r15d, r9d
00A4B426  0F 87 89 01 00 00               ja 0x140a4b5b5
00A4B42C  45 85 FF                        test r15d, r15d
00A4B42F  0F 84 FC 01 00 00               je 0x140a4b631
00A4B435  41 8D 47 FF                     lea eax, [r15 - 1]
00A4B439  8B C8                           mov ecx, eax
00A4B43B  48 8D 3C 85 03 00 00 00         lea rdi, [rax*4 + 3]
00A4B443  48 03 F9                        add rdi, rcx
00A4B446  49 8D 3C F8                     lea rdi, [r8 + rdi*8]
00A4B44A  48 03 FA                        add rdi, rdx
00A4B44D  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
00A4B451  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A4B454  44 3B C0                        cmp r8d, eax
00A4B457  44 0F 42 C0                     cmovb r8d, eax
00A4B45B  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00A4B460  48 39 74 24 50                  cmp qword ptr [rsp + 0x50], rsi
00A4B465  0F 85 E0 01 00 00               jne 0x140a4b64b
00A4B46B  41 F6 C4 08                     test r12b, 8
00A4B46F  0F 85 08 02 00 00               jne 0x140a4b67d
00A4B475  41 F6 C4 01                     test r12b, 1
00A4B479  0F 85 45 02 00 00               jne 0x140a4b6c4
00A4B47F  41 F6 C4 04                     test r12b, 4
00A4B483  75 7D                           jne 0x140a4b502
00A4B485  41 F6 C4 10                     test r12b, 0x10
00A4B489  0F 85 FF 01 00 00               jne 0x140a4b68e
00A4B48F  41 F6 C4 20                     test r12b, 0x20
00A4B493  0F 85 38 02 00 00               jne 0x140a4b6d1
00A4B499  45 84 E4                        test r12b, r12b
00A4B49C  0F 88 69 02 00 00               js 0x140a4b70b
00A4B4A2  8B 17                           mov edx, dword ptr [rdi]
00A4B4A4  85 D2                           test edx, edx
00A4B4A6  0F 84 8F 01 00 00               je 0x140a4b63b
00A4B4AC  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00A4B4B1  8B 4F 24                        mov ecx, dword ptr [rdi + 0x24]
00A4B4B4  81 E1 00 00 00 02               and ecx, 0x2000000
00A4B4BA  F7 40 68 00 00 00 04            test dword ptr [rax + 0x68], 0x4000000
00A4B4C1  0F 85 92 02 00 00               jne 0x140a4b759
00A4B4C7  85 C9                           test ecx, ecx
00A4B4C9  0F 85 CC 01 00 00               jne 0x140a4b69b
00A4B4CF  48 85 ED                        test rbp, rbp
00A4B4D2  0F 84 CB 00 00 00               je 0x140a4b5a3
00A4B4D8  49 3B ED                        cmp rbp, r13
00A4B4DB  0F 87 BF 00 00 00               ja 0x140a4b5a0
00A4B4E1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A4B4E6  48 89 29                        mov qword ptr [rcx], rbp
00A4B4E9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A4B4EE  4C 89 29                        mov qword ptr [rcx], r13
00A4B4F1  41 8D 4F 01                     lea ecx, [r15 + 1]
00A4B4F5  41 3B C9                        cmp ecx, r9d
00A4B4F8  0F 46 F1                        cmovbe esi, ecx
00A4B4FB  8B C6                           mov eax, esi
00A4B4FD  E9 03 01 00 00                  jmp 0x140a4b605
00A4B502  8B 5F 24                        mov ebx, dword ptr [rdi + 0x24]
00A4B505  48 8B CF                        mov rcx, rdi
00A4B508  81 E3 00 00 00 E0               and ebx, 0xe0000000
00A4B50E  E8 79 02 00 00                  call 0x140a4b78c
00A4B513  85 C0                           test eax, eax
00A4B515  8B CE                           mov ecx, esi
00A4B517  0F 94 C1                        sete cl
00A4B51A  F7 DB                           neg ebx
00A4B51C  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00A4B521  1B C0                           sbb eax, eax
00A4B523  23 C1                           and eax, ecx
00A4B525  44 8B 44 24 20                  mov r8d, dword ptr [rsp + 0x20]
00A4B52A  44 8B 4C 24 24                  mov r9d, dword ptr [rsp + 0x24]
00A4B52F  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
00A4B534  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
00A4B539  85 C0                           test eax, eax
00A4B53B  74 92                           je 0x140a4b4cf
00A4B53D  48 85 ED                        test rbp, rbp
00A4B540  75 1C                           jne 0x140a4b55e
00A4B542  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
00A4B545  48 81 C1 FF 0F 00 00            add rcx, 0xfff
00A4B54C  48 03 CB                        add rcx, rbx
00A4B54F  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00A4B556  E8 D5 2B 9F FF                  call 0x14043e130
00A4B55B  48 8B E8                        mov rbp, rax
00A4B55E  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00A4B561  49 8B C6                        mov rax, r14
00A4B564  41 03 D0                        add edx, r8d
00A4B567  48 F7 D8                        neg rax
00A4B56A  48 FF CA                        dec rdx
00A4B56D  49 03 D6                        add rdx, r14
00A4B570  48 03 D3                        add rdx, rbx
00A4B573  48 23 D0                        and rdx, rax
00A4B576  48 8B CA                        mov rcx, rdx
00A4B579  E8 B2 2B 9F FF                  call 0x14043e130
00A4B57E  4C 8B E8                        mov r13, rax
00A4B581  F7 C2 FF 0F 00 00               test edx, 0xfff
00A4B587  0F 85 DD 01 00 00               jne 0x140a4b76a
00A4B58D  49 83 ED 08                     sub r13, 8
00A4B591  49 81 FB 00 10 00 00            cmp r11, 0x1000
00A4B598  0F 87 31 FF FF FF               ja 0x140a4b4cf
00A4B59E  EB 03                           jmp 0x140a4b5a3
00A4B5A0  48 8B EE                        mov rbp, rsi
00A4B5A3  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00A4B5A8  41 FF C7                        inc r15d
00A4B5AB  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00A4B5B0  E9 6E FE FF FF                  jmp 0x140a4b423
00A4B5B5  48 85 ED                        test rbp, rbp
00A4B5B8  74 49                           je 0x140a4b603
00A4B5BA  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
00A4B5BD  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A4B5C0  3B C8                           cmp ecx, eax
00A4B5C2  0F 42 C8                        cmovb ecx, eax
00A4B5C5  03 4F 0C                        add ecx, dword ptr [rdi + 0xc]
00A4B5C8  48 FF C9                        dec rcx
00A4B5CB  49 03 CE                        add rcx, r14
00A4B5CE  49 F7 DE                        neg r14
00A4B5D1  48 03 CB                        add rcx, rbx
00A4B5D4  49 23 CE                        and rcx, r14
00A4B5D7  48 81 C1 FF 0F 00 00            add rcx, 0xfff
00A4B5DE  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00A4B5E5  E8 46 2B 9F FF                  call 0x14043e130
00A4B5EA  48 83 E8 08                     sub rax, 8
00A4B5EE  48 3B E8                        cmp rbp, rax
00A4B5F1  77 10                           ja 0x140a4b603
00A4B5F3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A4B5F8  48 89 29                        mov qword ptr [rcx], rbp
00A4B5FB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A4B600  48 89 01                        mov qword ptr [rcx], rax
00A4B603  33 C0                           xor eax, eax
00A4B605  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A4B60D  48 33 CC                        xor rcx, rsp
00A4B610  E8 2B 10 C6 FF                  call 0x1406ac640
00A4B615  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A4B61D  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A4B624  41 5F                           pop r15
00A4B626  41 5E                           pop r14
00A4B628  41 5D                           pop r13
00A4B62A  41 5C                           pop r12
00A4B62C  5F                              pop rdi
00A4B62D  5E                              pop rsi
00A4B62E  5D                              pop rbp
00A4B62F  C3                              ret
00A4B630  CC                              int3
00A4B631  48 8D 7C 24 70                  lea rdi, [rsp + 0x70]
00A4B636  E9 12 FE FF FF                  jmp 0x140a4b44d
00A4B63B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00A4B640  48 3B F8                        cmp rdi, rax
00A4B643  0F 84 63 FE FF FF               je 0x140a4b4ac
00A4B649  EB B8                           jmp 0x140a4b603
00A4B64B  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
00A4B64E  4C 3B D0                        cmp r10, rax
00A4B651  0F 82 78 FE FF FF               jb 0x140a4b4cf
00A4B657  41 8D 0C 00                     lea ecx, [r8 + rax]
00A4B65B  4C 3B D1                        cmp r10, rcx
00A4B65E  0F 83 6B FE FF FF               jae 0x140a4b4cf
00A4B664  41 F6 C4 40                     test r12b, 0x40
00A4B668  0F 84 CF FE FF FF               je 0x140a4b53d
00A4B66E  F7 47 24 00 00 00 02            test dword ptr [rdi + 0x24], 0x2000000
00A4B675  0F 84 C2 FE FF FF               je 0x140a4b53d
00A4B67B  EB 86                           jmp 0x140a4b603
00A4B67D  F7 47 24 00 00 00 E0            test dword ptr [rdi + 0x24], 0xe0000000
00A4B684  8B C6                           mov eax, esi
00A4B686  0F 95 C0                        setne al
00A4B689  E9 AB FE FF FF                  jmp 0x140a4b539
00A4B68E  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00A4B691  25 00 00 00 20                  and eax, 0x20000000
00A4B696  E9 9E FE FF FF                  jmp 0x140a4b539
00A4B69B  48 8B 40 30                     mov rax, qword ptr [rax + 0x30]
00A4B69F  48 3B 05 82 B4 57 00            cmp rax, qword ptr [rip + 0x57b482]
00A4B6A6  74 0D                           je 0x140a4b6b5
00A4B6A8  48 3B 05 E9 B4 57 00            cmp rax, qword ptr [rip + 0x57b4e9]
00A4B6AF  0F 85 88 FE FF FF               jne 0x140a4b53d
00A4B6B5  48 8B CF                        mov rcx, rdi
00A4B6B8  E8 F3 18 A8 FF                  call 0x1404ccfb0
00A4B6BD  85 C0                           test eax, eax
00A4B6BF  E9 52 01 0F 00                  jmp 0x140b3b816
00A4B6C4  48 8B CF                        mov rcx, rdi
00A4B6C7  E8 C0 00 00 00                  call 0x140a4b78c
00A4B6CC  E9 54 FE FF FF                  jmp 0x140a4b525
00A4B6D1  80 3F 50                        cmp byte ptr [rdi], 0x50
00A4B6D4  0F 85 F5 FD FF FF               jne 0x140a4b4cf
00A4B6DA  80 7F 01 41                     cmp byte ptr [rdi + 1], 0x41
00A4B6DE  0F 85 EB FD FF FF               jne 0x140a4b4cf
00A4B6E4  80 7F 02 47                     cmp byte ptr [rdi + 2], 0x47
00A4B6E8  0F 85 E1 FD FF FF               jne 0x140a4b4cf
00A4B6EE  80 7F 03 45                     cmp byte ptr [rdi + 3], 0x45
00A4B6F2  0F 85 D7 FD FF FF               jne 0x140a4b4cf
00A4B6F8  80 7F 04 4B                     cmp byte ptr [rdi + 4], 0x4b
00A4B6FC  0F 85 CD FD FF FF               jne 0x140a4b4cf
00A4B702  80 7F 05 44                     cmp byte ptr [rdi + 5], 0x44
00A4B706  E9 0B 01 0F 00                  jmp 0x140b3b816
00A4B70B  80 3F 50                        cmp byte ptr [rdi], 0x50
00A4B70E  0F 85 BB FD FF FF               jne 0x140a4b4cf
00A4B714  80 7F 01 41                     cmp byte ptr [rdi + 1], 0x41
00A4B718  0F 85 B1 FD FF FF               jne 0x140a4b4cf
00A4B71E  80 7F 02 47                     cmp byte ptr [rdi + 2], 0x47
00A4B722  0F 85 A7 FD FF FF               jne 0x140a4b4cf
00A4B728  80 7F 03 45                     cmp byte ptr [rdi + 3], 0x45
00A4B72C  0F 85 9D FD FF FF               jne 0x140a4b4cf
00A4B732  80 7F 04 43                     cmp byte ptr [rdi + 4], 0x43
00A4B736  0F 85 93 FD FF FF               jne 0x140a4b4cf
00A4B73C  80 7F 05 4D                     cmp byte ptr [rdi + 5], 0x4d
00A4B740  0F 85 89 FD FF FF               jne 0x140a4b4cf
00A4B746  80 7F 06 52                     cmp byte ptr [rdi + 6], 0x52
00A4B74A  0F 85 7F FD FF FF               jne 0x140a4b4cf
00A4B750  80 7F 07 43                     cmp byte ptr [rdi + 7], 0x43
00A4B754  E9 BD 00 0F 00                  jmp 0x140b3b816
00A4B759  81 FA 49 4E 49 54               cmp edx, 0x54494e49
00A4B75F  0F 84 6A FD FF FF               je 0x140a4b4cf
00A4B765  E9 5D FD FF FF                  jmp 0x140a4b4c7
00A4B76A  41 F6 C4 0C                     test r12b, 0xc
00A4B76E  0F 84 19 FE FF FF               je 0x140a4b58d
00A4B774  49 81 FE 00 10 00 00            cmp r14, 0x1000
00A4B77B  0F 82 10 FE FF FF               jb 0x140a4b591
00A4B781  E9 07 FE FF FF                  jmp 0x140a4b58d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSnapDriverRange(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p70;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3929080)) ^ (v_rsp);
    v_stack_m40 = result;
    v_rsi = 0;
    v_stack_mA0 = a1;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned __int64 *)(a5) = 0;
    *(unsigned __int64 *)(a6) = 0;
    v_stack_m5C = v_xmm0;
    v_stack_m98 = a5;
    v_stack_m88 = a4;
    v_stack_m90 = a6;
    *(unsigned __int64 *)(v_rsp - 76) = 0;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 48);
    result = RtlImageNtHeader(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    v_stack_m78 = result;
    v_r10 = (a4) - (*(unsigned __int64 *)(a1 + 48));
    v_stack_mB0 = v_r10;
    v_r14 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 56))));
    if (((unsigned int)(*(unsigned int *)(result + 56))) > ((unsigned int)(0x1000ULL))) { v_r14 = (unsigned int)((unsigned int)(0x1000ULL)); }
    v_stack_mA8 = (unsigned int)(*(unsigned int *)(result + 56));
    v_stack_mB4 = (unsigned int)(*(unsigned __int16 *)(result + 6));
    if (((unsigned int)((unsigned int)(a2))) > ((unsigned int)(*(unsigned __int16 *)(result + 6)))) goto loc_00A4B603;
    v_rdi = (*(unsigned __int16 *)(result + 6) * 4 + 3) + (*(unsigned __int16 *)(result + 6));
    v_stack_m70 = *(unsigned __int16 *)(result + 20);
    v_stack_m44 = 0x40000000ULL;
    v_rdi = (*(unsigned __int16 *)(result + 20) + v_rdi * 8) + (result);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(*(unsigned __int64 *)(a1 + 48))));
    v_stack_m58 = (unsigned int)(result);
    v_stack_m60 = (unsigned int)(result);
loc_00A4B423:
    if (((unsigned int)((unsigned int)(a2))) > ((unsigned int)(*(unsigned __int16 *)(result + 6)))) goto loc_00A4B5B5;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_00A4B631;
    v_rdi = ((unsigned int)(a2) - 1 * 4 + 3) + ((unsigned int)((unsigned int)((unsigned int)(a2) - 1)));
    v_rdi = (*(unsigned __int16 *)(result + 20) + v_rdi * 8) + (result);
loc_00A4B44D:
    a3 = (unsigned int)(*(unsigned int *)(v_rdi + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))); }
    v_stack_mB8 = a3;
    if (v_stack_m88 != 0) goto loc_00A4B64B;
    if ((((unsigned __int8)((unsigned int)(a3))) & (8)) != 0) goto loc_00A4B67D;
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) != 0) goto loc_00A4B6C4;
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) != 0) goto loc_00A4B502;
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) != 0) goto loc_00A4B68E;
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) != 0) goto loc_00A4B6D1;
    if (sign_flag) goto loc_00A4B70B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi))) == 0) goto loc_00A4B63B;
loc_00A4B4AC:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 36))) & (0x2000000ULL));
    if (((*(unsigned int *)(v_stack_mA0 + 104)) & (0x4000000ULL)) != 0) goto loc_00A4B759;
loc_00A4B4C7:
    if ((unsigned int)(a1) != 0) goto loc_00A4B69B;
loc_00A4B4CF:
    if (0 == 0) goto loc_00A4B5A3;
    if (0 > 0) goto loc_00A4B5A0;
    *(unsigned __int64 *)(v_stack_m98) = 0;
    *(unsigned __int64 *)(v_stack_m90) = 0;
    if (((unsigned int)((unsigned int)(a2) + 1)) <= ((unsigned int)(*(unsigned __int16 *)(result + 6)))) { v_rsi = (unsigned int)((unsigned int)(a2) + 1); }
    goto loc_00A4B605;
loc_00A4B502:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 36))) & (0xE0000000ULL));
    result = MmImageSectionPagable(v_rdi, (unsigned int)(*(unsigned int *)(v_rdi)), a3, *(unsigned __int16 *)(result + 6));
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    v_rbx = (unsigned int)(-(v_rbx));
    result = (unsigned int)((result) & ((unsigned int)(a1)));
loc_00A4B525:
loc_00A4B539:
    if ((unsigned int)(result) == 0) goto loc_00A4B4CF;
loc_00A4B53D:
    v_rbp = 0;
    if (0 == 0) {
        a1 = *(unsigned int *)(v_rdi + 12);
        a1 = (a1) + (0xFFFULL);
        a1 = (a1) + (v_stack_m80);
        a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
        result = MiGetPteAddress(a1, (unsigned int)(*(unsigned int *)(v_rdi)), (unsigned int)(v_stack_mB8), (unsigned int)(v_stack_mB4));
        v_rbp = result;
    }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 12))) + ((unsigned int)((unsigned int)(v_stack_mB8))));
    result = -(v_r14);
    a2 = (a2) - 1;
    a2 = (a2) + (v_r14);
    a2 = (a2) + (v_stack_m80);
    a2 = (a2) & (result);
    result = MiGetPteAddress(a2, a2, (unsigned int)(v_stack_mB8), (unsigned int)(v_stack_mB4));
    if (((a2) & (0xFFFULL)) != 0) goto loc_00A4B76A;
loc_00A4B58D:
    v_r13 = (result) - (8);
loc_00A4B591:
    if (v_stack_mA8 > 0x1000ULL) goto loc_00A4B4CF;
    goto loc_00A4B5A3;
loc_00A4B5A0:
loc_00A4B5A3:
    v_r15 = (unsigned int)(((unsigned int)(a2)) + 1);
    goto loc_00A4B423;
loc_00A4B5B5:
    if (v_rsi == 0) goto loc_00A4B603;
    a1 = (unsigned int)(*(unsigned int *)(v_rdi + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))); }
    a1 = (unsigned int)((a1) + (*(unsigned int *)(v_rdi + 12)));
    a1 = (a1) - 1;
    a1 = (a1) + (v_r14);
    v_r14 = -(v_r14);
    a1 = (a1) + (v_stack_m80);
    a1 = (a1) & (v_r14);
    a1 = (a1) + (0xFFFULL);
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    result = MiGetPteAddress(a1, v_stack_m78, v_stack_m70, (unsigned int)(v_stack_mB4));
    result = (result) - (8);
    if (v_rsi <= result) {
        a1 = v_stack_m98;
        *(unsigned __int64 *)(a1) = v_rsi;
        a1 = v_stack_m90;
        *(unsigned __int64 *)(a1) = result;
    }
    result = 0;
loc_00A4B605:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m78, v_stack_m70, (unsigned int)(v_stack_mB4));
    v_rsp = (v_rsp) + (160);
    return result;
loc_00A4B631:
    goto loc_00A4B44D;
loc_00A4B63B:
    if (v_stack_p70 == v_stack_p70) goto loc_00A4B4AC;
    goto loc_00A4B603;
loc_00A4B64B:
    if (v_stack_mB0 < ((unsigned int)(*(unsigned int *)(v_stack_p70 + 12)))) goto loc_00A4B4CF;
    if (v_stack_mB0 >= (v_stack_m70 + (unsigned int)(*(unsigned int *)(v_stack_p70 + 12)) * 1)) goto loc_00A4B4CF;
    if ((((unsigned __int8)((unsigned int)(a3))) & (64)) == 0) goto loc_00A4B53D;
    if (((*(unsigned int *)(v_stack_p70 + 36)) & (0x2000000ULL)) == 0) goto loc_00A4B53D;
    goto loc_00A4B603;
loc_00A4B67D:
    result = (((*(unsigned int *)(v_stack_p70 + 36)) & (0xE0000000ULL)) != 0) ? 1 : 0;
    goto loc_00A4B539;
loc_00A4B68E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p70 + 36))) & (0x20000000ULL));
    goto loc_00A4B539;
loc_00A4B69B:
    if ((*(unsigned __int64 *)(result + 48)) == (*(unsigned __int64 *)(v_rip + 5747842))) goto loc_00A4B6B5;
    if ((*(unsigned __int64 *)(result + 48)) != (*(unsigned __int64 *)(v_rip + 5747945))) goto loc_00A4B53D;
loc_00A4B6B5:
    result = MiIsKernelHalPadSection(v_stack_p70, v_stack_m78, v_stack_m70, (unsigned int)(v_stack_mB4));
loc_00A4B6C4:
    result = MmImageSectionPagable(v_stack_p70, v_stack_m78, v_stack_m70, (unsigned int)(v_stack_mB4));
    goto loc_00A4B525;
loc_00A4B6D1:
    if ((*(unsigned __int8 *)(v_stack_p70)) != 80) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 1)) != 65) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 2)) != 71) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 3)) != 69) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 4)) != 75) goto loc_00A4B4CF;
loc_00A4B70B:
    if ((*(unsigned __int8 *)(v_stack_p70)) != 80) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 1)) != 65) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 2)) != 71) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 3)) != 69) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 4)) != 67) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 5)) != 77) goto loc_00A4B4CF;
    if ((*(unsigned __int8 *)(v_stack_p70 + 6)) != 82) goto loc_00A4B4CF;
loc_00A4B759:
    if (((unsigned int)(v_stack_m78)) == 0x54494E49ULL) goto loc_00A4B4CF;
    goto loc_00A4B4C7;
loc_00A4B76A:
    if ((((unsigned __int8)((unsigned int)(a3))) & (12)) == 0) goto loc_00A4B58D;
    if (v_r14 < 0x1000ULL) goto loc_00A4B591;
    goto loc_00A4B58D;
}
```

## 5. (Beta) C Style

```c
int64_t MiSnapDriverRange(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint32_t v_stack_m58;
    uint64_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p70;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x3BF3F8)) ^ (local_rsp);
    v_stack_m40 = result;
    local_rsi = 0;
    v_stack_mA0 = Arg1;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint64_t *)(arg5) = 0;
    *(uint64_t *)(arg6) = 0;
    v_stack_m5C = v_xmm0;
    v_stack_m98 = Arg5;
    v_stack_m88 = Arg4;
    v_stack_m90 = Arg6;
    *(uint64_t *)(local_rsp - 0x4C) = 0;
    v_stack_m80 = *(uint64_t *)(arg1 + 0x30);
    result = RtlImageNtHeader(*(uint64_t *)(arg1 + 0x30), Arg2, Arg3, Arg4);
    v_stack_m78 = result;
    local_r10 = (Arg4) - (*(uint64_t *)(arg1 + 0x30));
    v_stack_mB0 = local_r10;
    local_r14 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x38))));
    if (((uint32_t)(*(uint32_t *)(result + 0x38))) > ((uint32_t)(0x1000ULL))) { local_r14 = (uint32_t)((uint32_t)(0x1000ULL)); }
    v_stack_mA8 = (uint32_t)(*(uint32_t *)(result + 0x38));
    v_stack_mB4 = (uint32_t)(*(uint16_t *)(result + 0x6));
    if (((uint32_t)((uint32_t)(Arg2))) > ((uint32_t)(*(uint16_t *)(result + 0x6)))) goto loc_00A4B603;
    local_rdi = (*(uint16_t *)(result + 0x6) * 4 + 3) + (*(uint16_t *)(result + 0x6));
    v_stack_m70 = *(uint16_t *)(result + 0x14);
    v_stack_m44 = 0x40000000ULL;
    local_rdi = (*(uint16_t *)(result + 0x14) + local_rdi * 8) + (result);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(*(uint64_t *)(arg1 + 0x30))));
    v_stack_m58 = (uint32_t)(result);
    v_stack_m60 = (uint32_t)(result);
loc_00A4B423:
    if (((uint32_t)((uint32_t)(Arg2))) > ((uint32_t)(*(uint16_t *)(result + 0x6)))) goto loc_00A4B5B5;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_00A4B631;
    local_rdi = ((uint32_t)(Arg2) - 1 * 4 + 3) + ((uint32_t)((uint32_t)((uint32_t)(Arg2) - 1)));
    local_rdi = (*(uint16_t *)(result + 0x14) + local_rdi * 8) + (result);
loc_00A4B44D:
    Arg3 = (uint32_t)(*(uint32_t *)(local_rdi + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))); }
    v_stack_mB8 = Arg3;
    if (v_stack_m88 != 0) goto loc_00A4B64B;
    if ((((uint8_t)((uint32_t)(Arg3))) & (8)) != 0) goto loc_00A4B67D;
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) != 0) goto loc_00A4B6C4;
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) != 0) goto loc_00A4B502;
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) != 0) goto loc_00A4B68E;
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) != 0) goto loc_00A4B6D1;
    if (sign_flag) goto loc_00A4B70B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi))) == 0) goto loc_00A4B63B;
loc_00A4B4AC:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x24))) & (0x2000000ULL));
    if (((*(uint32_t *)(v_stack_mA0 + 0x68)) & (0x4000000ULL)) != 0) goto loc_00A4B759;
loc_00A4B4C7:
    if ((uint32_t)(Arg1) != 0) goto loc_00A4B69B;
loc_00A4B4CF:
    if (0 == 0) goto loc_00A4B5A3;
    if (0 > 0) goto loc_00A4B5A0;
    *(uint64_t *)(v_stack_m98) = 0;
    *(uint64_t *)(v_stack_m90) = 0;
    if (((uint32_t)((uint32_t)(Arg2) + 1)) <= ((uint32_t)(*(uint16_t *)(result + 0x6)))) { local_rsi = (uint32_t)((uint32_t)(Arg2) + 1); }
    goto loc_00A4B605;
loc_00A4B502:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x24))) & (0xE0000000ULL));
    result = MmImageSectionPagable(local_rdi, (uint32_t)(*(uint32_t *)(local_rdi)), Arg3, *(uint16_t *)(result + 0x6));
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    local_rbx = (uint32_t)(-(local_rbx));
    result = (uint32_t)((result) & ((uint32_t)(Arg1)));
loc_00A4B525:
loc_00A4B539:
    if ((uint32_t)(result) == 0) goto loc_00A4B4CF;
loc_00A4B53D:
    local_rbp = 0;
    if (0 == 0) {
        Arg1 = *(uint32_t *)(local_rdi + 0xC);
        Arg1 = (Arg1) + (0xFFFULL);
        Arg1 = (Arg1) + (v_stack_m80);
        Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
        result = MiGetPteAddress(Arg1, (uint32_t)(*(uint32_t *)(local_rdi)), (uint32_t)(v_stack_mB8), (uint32_t)(v_stack_mB4));
        local_rbp = result;
    }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC))) + ((uint32_t)((uint32_t)(v_stack_mB8))));
    result = -(local_r14);
    Arg2 = (Arg2) - 1;
    Arg2 = (Arg2) + (local_r14);
    Arg2 = (Arg2) + (v_stack_m80);
    Arg2 = (Arg2) & (result);
    result = MiGetPteAddress(Arg2, Arg2, (uint32_t)(v_stack_mB8), (uint32_t)(v_stack_mB4));
    if (((Arg2) & (0xFFFULL)) != 0) goto loc_00A4B76A;
loc_00A4B58D:
    local_r13 = (result) - (8);
loc_00A4B591:
    if (v_stack_mA8 > 0x1000ULL) goto loc_00A4B4CF;
    goto loc_00A4B5A3;
loc_00A4B5A0:
loc_00A4B5A3:
    local_r15 = (uint32_t)(((uint32_t)(Arg2)) + 1);
    goto loc_00A4B423;
loc_00A4B5B5:
    if (local_rsi == 0) goto loc_00A4B603;
    Arg1 = (uint32_t)(*(uint32_t *)(local_rdi + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))); }
    Arg1 = (uint32_t)((Arg1) + (*(uint32_t *)(local_rdi + 0xC)));
    Arg1 = (Arg1) - 1;
    Arg1 = (Arg1) + (local_r14);
    local_r14 = -(local_r14);
    Arg1 = (Arg1) + (v_stack_m80);
    Arg1 = (Arg1) & (local_r14);
    Arg1 = (Arg1) + (0xFFFULL);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    result = MiGetPteAddress(Arg1, v_stack_m78, v_stack_m70, (uint32_t)(v_stack_mB4));
    result = (result) - (8);
    if (local_rsi <= result) {
        Arg1 = v_stack_m98;
        *(uint64_t *)(arg1) = local_rsi;
        Arg1 = v_stack_m90;
        *(uint64_t *)(arg1) = result;
    }
    result = 0;
loc_00A4B605:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m78, v_stack_m70, (uint32_t)(v_stack_mB4));
    local_rsp = (local_rsp) + (160);
    return result;
loc_00A4B631:
    goto loc_00A4B44D;
loc_00A4B63B:
    if (v_stack_p70 == v_stack_p70) goto loc_00A4B4AC;
    goto loc_00A4B603;
loc_00A4B64B:
    if (v_stack_mB0 < ((uint32_t)(*(uint32_t *)(v_stack_p70 + 0xC)))) goto loc_00A4B4CF;
    if (v_stack_mB0 >= (v_stack_m70 + (uint32_t)(*(uint32_t *)(v_stack_p70 + 0xC)) * 1)) goto loc_00A4B4CF;
    if ((((uint8_t)((uint32_t)(Arg3))) & (64)) == 0) goto loc_00A4B53D;
    if (((*(uint32_t *)(v_stack_p70 + 0x24)) & (0x2000000ULL)) == 0) goto loc_00A4B53D;
    goto loc_00A4B603;
loc_00A4B67D:
    result = (((*(uint32_t *)(v_stack_p70 + 0x24)) & (0xE0000000ULL)) != 0) ? 1 : 0;
    goto loc_00A4B539;
loc_00A4B68E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p70 + 0x24))) & (0x20000000ULL));
    goto loc_00A4B539;
loc_00A4B69B:
    if ((*(uint64_t *)(result + 0x30)) == (*(uint64_t *)(v_rip + 0x57B482))) goto loc_00A4B6B5;
    if ((*(uint64_t *)(result + 0x30)) != (*(uint64_t *)(v_rip + 0x57B4E9))) goto loc_00A4B53D;
loc_00A4B6B5:
    result = MiIsKernelHalPadSection(v_stack_p70, v_stack_m78, v_stack_m70, (uint32_t)(v_stack_mB4));
loc_00A4B6C4:
    result = MmImageSectionPagable(v_stack_p70, v_stack_m78, v_stack_m70, (uint32_t)(v_stack_mB4));
    goto loc_00A4B525;
loc_00A4B6D1:
    if ((*(uint8_t *)(v_stack_p70)) != 80) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x1)) != 65) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x2)) != 71) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x3)) != 69) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x4)) != 75) goto loc_00A4B4CF;
loc_00A4B70B:
    if ((*(uint8_t *)(v_stack_p70)) != 80) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x1)) != 65) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x2)) != 71) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x3)) != 69) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x4)) != 67) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x5)) != 77) goto loc_00A4B4CF;
    if ((*(uint8_t *)(v_stack_p70 + 0x6)) != 82) goto loc_00A4B4CF;
loc_00A4B759:
    if (((uint32_t)(v_stack_m78)) == 0x54494E49ULL) goto loc_00A4B4CF;
    goto loc_00A4B4C7;
loc_00A4B76A:
    if ((((uint8_t)((uint32_t)(Arg3))) & (12)) == 0) goto loc_00A4B58D;
    if (local_r14 < 0x1000ULL) goto loc_00A4B591;
    goto loc_00A4B58D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4B328&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
