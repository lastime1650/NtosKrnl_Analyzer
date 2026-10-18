# LdrpSearchResourceSection_U

- RVA: `0x0099B2DC`–`0x0099BE16` (길이 `2,874` bytes)
- VA: `0x000000014099B2DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000996BC`
- 디코드: `621`개 명령, `2,874/2,874` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0099B3F1` → [LdrpCompareResourceNamesWithValidation](../../text/47/LdrpCompareResourceNamesWithValidation_function_0047E3D4.md) (function, `0x0047E3D4`)
- `0x0099B54E` → [LdrpCompareResourceNamesWithValidation](../../text/47/LdrpCompareResourceNamesWithValidation_function_0047E3D4.md) (function, `0x0047E3D4`)
- `0x0099B60E` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099B6BB` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099B80A` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099B8BA` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099B9AF` → [LdrpGetParentLangId](../../text/4B/LdrpGetParentLangId_function_004BDAC0.md) (function, `0x004BDAC0`)
- `0x0099BA20` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099BA6B` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (function, `0x004328D0`)
- `0x0099BB21` → [LdrIsResItemExist](../../text/45/LdrIsResItemExist_function_004554DC.md) (function, `0x004554DC`)
- `0x0099BC4D` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x0099BCF4` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099BD67` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (function, `0x00455698`)
- `0x0099BDD7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [LdrpGetRcConfig](../../text/45/LdrpGetRcConfig_function_0045555C.md) at `0x004555F1`
- [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) at `0x00455719`
- [LdrFindResourceDirectory_U](../78/LdrFindResourceDirectory_U_function_0078BCC0.md) at `0x0078BCCF`
- [LdrFindResourceEx_U](../78/LdrFindResourceEx_U_function_0078BCE0.md) at `0x0078BD05`
- [LdrFindResource_U](../78/LdrFindResource_U_function_0078BD20.md) at `0x0078BD2C`
- [RtlLoadString](../78/RtlLoadString_function_0078C570.md) at `0x0078C6EB`
- [RtlFindMessage](RtlFindMessage_function_0099B220.md) at `0x0099B285`

### Static image references
- `0x0099B2EF` → RVA `0x00E0A740` (`.data`; read)
- `0x0099B5D9` → RVA `0x00FD9A70` (`PAGEDATA`; read)
- `0x0099B8F2` → RVA `0x00FD9A60` (`PAGEDATA`; read)
- `0x0099BAD6` → RVA `0x00F8C5FA` (`.data`; read)
- `0x0099BC46` → RVA `0x00B05460` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0099BC9D` → RVA `0x00FD9A98` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0099B3F1` → [LdrpCompareResourceNamesWithValidation](../../text/47/LdrpCompareResourceNamesWithValidation_function_0047E3D4.md) (`PAGE` → `.text`)
  - `0x0099B54E` → [LdrpCompareResourceNamesWithValidation](../../text/47/LdrpCompareResourceNamesWithValidation_function_0047E3D4.md) (`PAGE` → `.text`)
  - `0x0099B60E` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099B6BB` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099B80A` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099B8BA` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099B9AF` → [LdrpGetParentLangId](../../text/4B/LdrpGetParentLangId_function_004BDAC0.md) (`PAGE` → `.text`)
  - `0x0099BA20` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099BA6B` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (`PAGE` → `.text`)
  - `0x0099BB21` → [LdrIsResItemExist](../../text/45/LdrIsResItemExist_function_004554DC.md) (`PAGE` → `.text`)
  - `0x0099BC4D` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x0099BCF4` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099BD67` → [LdrpLoadResourceFromAlternativeModule](../../text/45/LdrpLoadResourceFromAlternativeModule_function_00455698.md) (`PAGE` → `.text`)
  - `0x0099BDD7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0099B2DC  40 53                           push rbx
0099B2DE  56                              push rsi
0099B2DF  57                              push rdi
0099B2E0  41 54                           push r12
0099B2E2  41 55                           push r13
0099B2E4  41 56                           push r14
0099B2E6  41 57                           push r15
0099B2E8  48 81 EC 10 01 00 00            sub rsp, 0x110
0099B2EF  48 8B 05 4A F4 46 00            mov rax, qword ptr [rip + 0x46f44a]
0099B2F6  48 33 C4                        xor rax, rsp
0099B2F9  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0099B301  45 8B F9                        mov r15d, r9d
0099B304  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
0099B309  45 8B E0                        mov r12d, r8d
0099B30C  44 89 84 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r8d
0099B314  4C 8B EA                        mov r13, rdx
0099B317  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0099B31C  48 8B 94 24 70 01 00 00         mov rdx, qword ptr [rsp + 0x170]
0099B324  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0099B329  33 FF                           xor edi, edi
0099B32B  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0099B330  4C 89 AC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r13
0099B338  40 88 7C 24 35                  mov byte ptr [rsp + 0x35], dil
0099B33D  44 8D 57 01                     lea r10d, [rdi + 1]
0099B341  44 88 54 24 3C                  mov byte ptr [rsp + 0x3c], r10b
0099B346  44 88 54 24 36                  mov byte ptr [rsp + 0x36], r10b
0099B34B  41 83 F8 03                     cmp r8d, 3
0099B34F  0F 82 B6 0A 00 00               jb 0x14099be0b
0099B355  41 83 FC 04                     cmp r12d, 4
0099B359  0F 87 9B 0A 00 00               ja 0x14099bdfa
0099B35F  41 8B C7                        mov eax, r15d
0099B362  83 E0 41                        and eax, 0x41
0099B365  0F 85 85 0A 00 00               jne 0x14099bdf0
0099B36B  41 83 FC 04                     cmp r12d, 4
0099B36F  0F 84 8C 0A 00 00               je 0x14099be01
0099B375  B8 03 00 00 00                  mov eax, 3
0099B37A  41 83 FC 04                     cmp r12d, 4
0099B37E  41 0F 45 C4                     cmovne eax, r12d
0099B382  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0099B386  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0099B38A  66 89 7C 24 40                  mov word ptr [rsp + 0x40], di
0099B38F  44 0F B7 F7                     movzx r14d, di
0099B393  66 89 7C 24 30                  mov word ptr [rsp + 0x30], di
0099B398  49 8D 45 FF                     lea rax, [r13 - 1]
0099B39C  48 83 F8 FD                     cmp rax, -3
0099B3A0  0F 87 1B 0A 00 00               ja 0x14099bdc1
0099B3A6  E9 96 06 00 00                  jmp 0x14099ba41
0099B3AB  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
0099B3B3  41 0F B7 C4                     movzx eax, r12w
0099B3B7  48 C1 E0 03                     shl rax, 3
0099B3BB  40 80 E7 01                     and dil, 1
0099B3BF  0F 84 B4 05 00 00               je 0x14099b979
0099B3C5  4C 8D 3C 30                     lea r15, [rax + rsi]
0099B3C9  4C 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r15
0099B3D1  4D 8B 45 00                     mov r8, qword ptr [r13]
0099B3D5  44 88 54 24 44                  mov byte ptr [rsp + 0x44], r10b
0099B3DA  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0099B3DF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0099B3E4  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0099B3E9  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
0099B3F1  E8 DE 2F AE FF                  call 0x14047e3d4
0099B3F6  45 33 D2                        xor r10d, r10d
0099B3F9  85 C0                           test eax, eax
0099B3FB  0F 85 1E 04 00 00               jne 0x14099b81f
0099B401  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0099B405  45 39 57 04                     cmp dword ptr [r15 + 4], r10d
0099B409  0F 8D BF 05 00 00               jge 0x14099b9ce
0099B40F  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0099B417  48 8B D8                        mov rbx, rax
0099B41A  0F BA F3 1F                     btr ebx, 0x1f
0099B41E  48 03 DF                        add rbx, rdi
0099B421  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0099B429  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0099B42E  49 83 C5 08                     add r13, 8
0099B432  4C 89 AC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r13
0099B43A  44 8B 7C 24 54                  mov r15d, dword ptr [rsp + 0x54]
0099B43F  44 8B A4 24 A8 00 00 00         mov r12d, dword ptr [rsp + 0xa8]
0099B447  40 8A 7C 24 34                  mov dil, byte ptr [rsp + 0x34]
0099B44C  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099B451  8A 54 24 36                     mov dl, byte ptr [rsp + 0x36]
0099B455  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0099B459  41 BB 09 04 00 00               mov r11d, 0x409
0099B45F  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0099B464  48 85 DB                        test rbx, rbx
0099B467  0F 84 E1 02 00 00               je 0x14099b74e
0099B46D  41 8B C0                        mov eax, r8d
0099B470  41 FF C8                        dec r8d
0099B473  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
0099B478  44 89 84 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r8d
0099B480  85 C0                           test eax, eax
0099B482  0F 84 C6 02 00 00               je 0x14099b74e
0099B488  45 85 C0                        test r8d, r8d
0099B48B  0F 84 04 02 00 00               je 0x14099b695
0099B491  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0099B499  48 85 D2                        test rdx, rdx
0099B49C  0F 85 D2 00 00 00               jne 0x14099b574
0099B4A2  0F B7 7B 0C                     movzx edi, word ptr [rbx + 0xc]
0099B4A6  66 89 7C 24 4C                  mov word ptr [rsp + 0x4c], di
0099B4AB  48 8D 73 10                     lea rsi, [rbx + 0x10]
0099B4AF  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
0099B4B7  0F B7 CF                        movzx ecx, di
0099B4BA  49 F7 45 00 00 00 FF FF         test qword ptr [r13], -0x10000
0099B4C2  75 18                           jne 0x14099b4dc
0099B4C4  48 8D 34 FE                     lea rsi, [rsi + rdi*8]
0099B4C8  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
0099B4D0  0F B7 7B 0E                     movzx edi, word ptr [rbx + 0xe]
0099B4D4  66 89 7C 24 4C                  mov word ptr [rsp + 0x4c], di
0099B4D9  0F B7 CF                        movzx ecx, di
0099B4DC  66 85 C9                        test cx, cx
0099B4DF  0F 84 32 04 00 00               je 0x14099b917
0099B4E5  48 85 D2                        test rdx, rdx
0099B4E8  0F 85 1B 02 00 00               jne 0x14099b709
0099B4EE  49 8B DA                        mov rbx, r10
0099B4F1  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0099B4F9  0F B7 C1                        movzx eax, cx
0099B4FC  48 FF C8                        dec rax
0099B4FF  48 8D 04 C6                     lea rax, [rsi + rax*8]
0099B503  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0099B50B  48 3B F0                        cmp rsi, rax
0099B50E  0F 87 15 FF FF FF               ja 0x14099b429
0099B514  44 0F B7 E7                     movzx r12d, di
0099B518  66 41 D1 EC                     shr r12w, 1
0099B51C  0F 85 89 FE FF FF               jne 0x14099b3ab
0099B522  66 85 FF                        test di, di
0099B525  0F 84 FE FE FF FF               je 0x14099b429
0099B52B  4D 8B 45 00                     mov r8, qword ptr [r13]
0099B52F  44 88 54 24 45                  mov byte ptr [rsp + 0x45], r10b
0099B534  48 8D 44 24 45                  lea rax, [rsp + 0x45]
0099B539  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0099B53E  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0099B543  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0099B54B  4C 8B CF                        mov r9, rdi
0099B54E  E8 81 2E AE FF                  call 0x14047e3d4
0099B553  45 33 D2                        xor r10d, r10d
0099B556  85 C0                           test eax, eax
0099B558  0F 85 CB FE FF FF               jne 0x14099b429
0099B55E  8B 46 04                        mov eax, dword ptr [rsi + 4]
0099B561  44 39 56 04                     cmp dword ptr [rsi + 4], r10d
0099B565  0F 8C AC FE FF FF               jl 0x14099b417
0099B56B  48 8D 34 38                     lea rsi, [rax + rdi]
0099B56F  E9 70 04 00 00                  jmp 0x14099b9e4
0099B574  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
0099B57C  45 0F B7 49 10                  movzx r9d, word ptr [r9 + 0x10]
0099B581  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
0099B586  66 44 89 4C 24 7C               mov word ptr [rsp + 0x7c], r9w
0099B58C  B8 FF 03 00 00                  mov eax, 0x3ff
0099B591  66 44 85 C8                     test ax, r9w
0099B595  0F 94 C1                        sete cl
0099B598  88 4C 24 35                     mov byte ptr [rsp + 0x35], cl
0099B59C  88 4C 24 78                     mov byte ptr [rsp + 0x78], cl
0099B5A0  8B 9C 24 80 00 00 00            mov ebx, dword ptr [rsp + 0x80]
0099B5A7  8B C3                           mov eax, ebx
0099B5A9  FF C3                           inc ebx
0099B5AB  89 9C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ebx
0099B5B2  85 C0                           test eax, eax
0099B5B4  74 71                           je 0x14099b627
0099B5B6  83 E8 01                        sub eax, 1
0099B5B9  0F 84 05 02 00 00               je 0x14099b7c4
0099B5BF  83 E8 01                        sub eax, 1
0099B5C2  0F 85 25 03 00 00               jne 0x14099b8ed
0099B5C8  84 C9                           test cl, cl
0099B5CA  0F 84 E3 07 00 00               je 0x14099bdb3
0099B5D0  40 84 FF                        test dil, dil
0099B5D3  0F 84 AC 03 00 00               je 0x14099b985
0099B5D9  0F B7 05 90 E4 63 00            movzx eax, word ptr [rip + 0x63e490]
0099B5E0  66 85 C0                        test ax, ax
0099B5E3  0F 84 9C 03 00 00               je 0x14099b985
0099B5E9  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
0099B5F1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099B5F6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099B5FB  45 8B CF                        mov r9d, r15d
0099B5FE  45 8B C4                        mov r8d, r12d
0099B601  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099B609  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099B60E  E8 85 A0 AB FF                  call 0x140455698
0099B613  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B617  45 33 D2                        xor r10d, r10d
0099B61A  85 C0                           test eax, eax
0099B61C  0F 88 B6 02 00 00               js 0x14099b8d8
0099B622  E9 A5 07 00 00                  jmp 0x14099bdcc
0099B627  40 84 FF                        test dil, dil
0099B62A  0F 85 57 02 00 00               jne 0x14099b887
0099B630  45 0F B7 F1                     movzx r14d, r9w
0099B634  66 44 89 4C 24 30               mov word ptr [rsp + 0x30], r9w
0099B63A  41 8B C7                        mov eax, r15d
0099B63D  F7 D0                           not eax
0099B63F  A8 20                           test al, 0x20
0099B641  74 1F                           je 0x14099b662
0099B643  41 0F B7 C6                     movzx eax, r14w
0099B647  48 3B 44 24 60                  cmp rax, qword ptr [rsp + 0x60]
0099B64C  75 14                           jne 0x14099b662
0099B64E  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099B653  8A 4C 24 35                     mov cl, byte ptr [rsp + 0x35]
0099B657  41 BB 09 04 00 00               mov r11d, 0x409
0099B65D  E9 45 FF FF FF                  jmp 0x14099b5a7
0099B662  41 0F B7 C6                     movzx eax, r14w
0099B666  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0099B66B  4C 8D 6C 24 60                  lea r13, [rsp + 0x60]
0099B670  4C 89 AC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r13
0099B678  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0099B680  48 8B DA                        mov rbx, rdx
0099B683  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0099B68B  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0099B690  E9 0D FE FF FF                  jmp 0x14099b4a2
0099B695  84 D2                           test dl, dl
0099B697  74 41                           je 0x14099b6da
0099B699  45 8B CF                        mov r9d, r15d
0099B69C  41 0F BA E9 18                  bts r9d, 0x18
0099B6A1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099B6A6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099B6AB  45 8B C4                        mov r8d, r12d
0099B6AE  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099B6B6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099B6BB  E8 D8 9F AB FF                  call 0x140455698
0099B6C0  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B6C4  45 33 D2                        xor r10d, r10d
0099B6C7  85 C0                           test eax, eax
0099B6C9  0F 89 A5 02 00 00               jns 0x14099b974
0099B6CF  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0099B6D4  41 BB 09 04 00 00               mov r11d, 0x409
0099B6DA  45 85 C0                        test r8d, r8d
0099B6DD  0F 85 AE FD FF FF               jne 0x14099b491
0099B6E3  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0099B6EB  83 7C 24 48 03                  cmp dword ptr [rsp + 0x48], 3
0099B6F0  48 0F 44 D3                     cmove rdx, rbx
0099B6F4  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
0099B6FC  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
0099B704  E9 90 FD FF FF                  jmp 0x14099b499
0099B709  41 F6 C7 20                     test r15b, 0x20
0099B70D  0F 84 DB FD FF FF               je 0x14099b4ee
0099B713  49 8B DA                        mov rbx, r10
0099B716  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0099B71E  8B 06                           mov eax, dword ptr [rsi]
0099B720  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0099B725  8B 76 04                        mov esi, dword ptr [rsi + 4]
0099B728  48 03 B4 24 98 00 00 00         add rsi, qword ptr [rsp + 0x98]
0099B730  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
0099B738  40 8A 7C 24 34                  mov dil, byte ptr [rsp + 0x34]
0099B73D  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099B742  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0099B746  41 BB 09 04 00 00               mov r11d, 0x409
0099B74C  EB 08                           jmp 0x14099b756
0099B74E  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0099B756  41 8B C7                        mov eax, r15d
0099B759  83 E0 02                        and eax, 2
0099B75C  48 85 F6                        test rsi, rsi
0099B75F  0F 85 E3 00 00 00               jne 0x14099b848
0099B765  48 85 DB                        test rbx, rbx
0099B768  0F 85 F3 04 00 00               jne 0x14099bc61
0099B76E  8B C1                           mov eax, ecx
0099B770  41 2B C0                        sub eax, r8d
0099B773  83 E8 01                        sub eax, 1
0099B776  0F 84 0E 05 00 00               je 0x14099bc8a
0099B77C  83 E8 01                        sub eax, 1
0099B77F  0F 84 FB 04 00 00               je 0x14099bc80
0099B785  83 F8 01                        cmp eax, 1
0099B788  0F 85 E8 04 00 00               jne 0x14099bc76
0099B78E  B8 04 02 00 C0                  mov eax, 0xc0000204
0099B793  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B797  48 85 D2                        test rdx, rdx
0099B79A  0F 84 CA 00 00 00               je 0x14099b86a
0099B7A0  49 8B C2                        mov rax, r10
0099B7A3  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0099B7A8  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0099B7B0  44 38 54 24 3C                  cmp byte ptr [rsp + 0x3c], r10b
0099B7B5  0F 84 F8 05 00 00               je 0x14099bdb3
0099B7BB  8A 4C 24 35                     mov cl, byte ptr [rsp + 0x35]
0099B7BF  E9 DC FD FF FF                  jmp 0x14099b5a0
0099B7C4  66 45 85 F6                     test r14w, r14w
0099B7C8  0F 85 D8 01 00 00               jne 0x14099b9a6
0099B7CE  40 84 FF                        test dil, dil
0099B7D1  0F 84 98 00 00 00               je 0x14099b86f
0099B7D7  66 45 85 F6                     test r14w, r14w
0099B7DB  0F 84 59 FE FF FF               je 0x14099b63a
0099B7E1  41 0F B7 C6                     movzx eax, r14w
0099B7E5  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
0099B7ED  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099B7F2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099B7F7  45 8B CF                        mov r9d, r15d
0099B7FA  45 8B C4                        mov r8d, r12d
0099B7FD  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099B805  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099B80A  E8 89 9E AB FF                  call 0x140455698
0099B80F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B813  45 33 D2                        xor r10d, r10d
0099B816  85 C0                           test eax, eax
0099B818  78 55                           js 0x14099b86f
0099B81A  E9 AD 05 00 00                  jmp 0x14099bdcc
0099B81F  0F 88 63 05 00 00               js 0x14099bd88
0099B825  49 8D 77 08                     lea rsi, [r15 + 8]
0099B829  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
0099B831  66 44 89 64 24 4C               mov word ptr [rsp + 0x4c], r12w
0099B837  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0099B83F  41 0F B7 FC                     movzx edi, r12w
0099B843  E9 C3 FC FF FF                  jmp 0x14099b50b
0099B848  85 C0                           test eax, eax
0099B84A  0F 85 15 FF FF FF               jne 0x14099b765
0099B850  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099B855  48 89 30                        mov qword ptr [rax], rsi
0099B858  41 8B C2                        mov eax, r10d
0099B85B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B85F  3D 04 02 00 C0                  cmp eax, 0xc0000204
0099B864  0F 84 2D FF FF FF               je 0x14099b797
0099B86A  E9 5D 05 00 00                  jmp 0x14099bdcc
0099B86F  66 45 85 F6                     test r14w, r14w
0099B873  0F 84 C1 FD FF FF               je 0x14099b63a
0099B879  FF CB                           dec ebx
0099B87B  89 9C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ebx
0099B882  E9 B3 FD FF FF                  jmp 0x14099b63a
0099B887  66 45 85 C9                     test r9w, r9w
0099B88B  0F 84 9F FD FF FF               je 0x14099b630
0099B891  41 0F B7 C1                     movzx eax, r9w
0099B895  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
0099B89D  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099B8A2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099B8A7  45 8B CF                        mov r9d, r15d
0099B8AA  45 8B C4                        mov r8d, r12d
0099B8AD  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099B8B5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099B8BA  E8 D9 9D AB FF                  call 0x140455698
0099B8BF  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099B8C3  45 33 D2                        xor r10d, r10d
0099B8C6  85 C0                           test eax, eax
0099B8C8  0F 89 FE 04 00 00               jns 0x14099bdcc
0099B8CE  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099B8D3  E9 58 FD FF FF                  jmp 0x14099b630
0099B8D8  0F B7 05 91 E1 63 00            movzx eax, word ptr [rip + 0x63e191]
0099B8DF  44 0F B7 F0                     movzx r14d, ax
0099B8E3  66 89 44 24 30                  mov word ptr [rsp + 0x30], ax
0099B8E8  E9 4D FD FF FF                  jmp 0x14099b63a
0099B8ED  83 E8 01                        sub eax, 1
0099B8F0  75 51                           jne 0x14099b943
0099B8F2  0F B7 0D 67 E1 63 00            movzx ecx, word ptr [rip + 0x63e167]
0099B8F9  66 3B 0D 70 E1 63 00            cmp cx, word ptr [rip + 0x63e170]
0099B900  0F 85 F0 00 00 00               jne 0x14099b9f6
0099B906  44 0F B7 74 24 60               movzx r14d, word ptr [rsp + 0x60]
0099B90C  66 44 89 74 24 30               mov word ptr [rsp + 0x30], r14w
0099B912  E9 23 FD FF FF                  jmp 0x14099b63a
0099B917  4C 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], r10
0099B91F  41 8A C2                        mov al, r10b
0099B922  88 44 24 3C                     mov byte ptr [rsp + 0x3c], al
0099B926  88 44 24 79                     mov byte ptr [rsp + 0x79], al
0099B92A  40 8A 7C 24 34                  mov dil, byte ptr [rsp + 0x34]
0099B92F  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099B934  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0099B938  41 BB 09 04 00 00               mov r11d, 0x409
0099B93E  E9 2B FE FF FF                  jmp 0x14099b76e
0099B943  83 E8 01                        sub eax, 1
0099B946  0F 84 C1 03 00 00               je 0x14099bd0d
0099B94C  83 E8 01                        sub eax, 1
0099B94F  0F 84 3F 03 00 00               je 0x14099bc94
0099B955  83 F8 01                        cmp eax, 1
0099B958  0F 85 55 04 00 00               jne 0x14099bdb3
0099B95E  41 83 CF 20                     or r15d, 0x20
0099B962  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
0099B967  44 89 BC 24 68 01 00 00         mov dword ptr [rsp + 0x168], r15d
0099B96F  E9 C6 FC FF FF                  jmp 0x14099b63a
0099B974  E9 53 04 00 00                  jmp 0x14099bdcc
0099B979  4C 8D 7E F8                     lea r15, [rsi - 8]
0099B97D  4C 03 F8                        add r15, rax
0099B980  E9 44 FA FF FF                  jmp 0x14099b3c9
0099B985  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
0099B98A  0F B7 05 DF E0 63 00            movzx eax, word ptr [rip + 0x63e0df]
0099B991  66 85 C0                        test ax, ax
0099B994  66 0F 45 C8                     cmovne cx, ax
0099B998  44 0F B7 F1                     movzx r14d, cx
0099B99C  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
0099B9A1  E9 94 FC FF FF                  jmp 0x14099b63a
0099B9A6  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0099B9AB  41 0F B7 CE                     movzx ecx, r14w
0099B9AF  E8 0C 21 B2 FF                  call 0x1404bdac0
0099B9B4  45 33 D2                        xor r10d, r10d
0099B9B7  85 C0                           test eax, eax
0099B9B9  0F 89 BE 03 00 00               jns 0x14099bd7d
0099B9BF  45 0F B7 F2                     movzx r14d, r10w
0099B9C3  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
0099B9C9  E9 00 FE FF FF                  jmp 0x14099b7ce
0099B9CE  49 8B DA                        mov rbx, r10
0099B9D1  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0099B9D9  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
0099B9E1  48 03 F0                        add rsi, rax
0099B9E4  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0099B9E9  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
0099B9F1  E9 38 FA FF FF                  jmp 0x14099b42e
0099B9F6  40 84 FF                        test dil, dil
0099B9F9  74 35                           je 0x14099ba30
0099B9FB  48 89 8C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rcx
0099BA03  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099BA08  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099BA0D  45 8B CF                        mov r9d, r15d
0099BA10  45 8B C4                        mov r8d, r12d
0099BA13  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099BA1B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099BA20  E8 73 9C AB FF                  call 0x140455698
0099BA25  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099BA29  45 33 D2                        xor r10d, r10d
0099BA2C  85 C0                           test eax, eax
0099BA2E  79 0C                           jns 0x14099ba3c
0099BA30  0F B7 05 29 E0 63 00            movzx eax, word ptr [rip + 0x63e029]
0099BA37  E9 A3 FE FF FF                  jmp 0x14099b8df
0099BA3C  E9 8B 03 00 00                  jmp 0x14099bdcc
0099BA41  48 8D 41 FF                     lea rax, [rcx - 1]
0099BA45  48 83 F8 FD                     cmp rax, -3
0099BA49  0F 87 72 03 00 00               ja 0x14099bdc1
0099BA4F  48 8D 42 FF                     lea rax, [rdx - 1]
0099BA53  48 83 F8 FD                     cmp rax, -3
0099BA57  0F 87 64 03 00 00               ja 0x14099bdc1
0099BA5D  41 B8 02 00 00 00               mov r8d, 2
0099BA63  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
0099BA68  41 8A D2                        mov dl, r10b
0099BA6B  E8 60 6E A9 FF                  call 0x1404328d0
0099BA70  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0099BA78  48 85 C0                        test rax, rax
0099BA7B  0F 84 70 01 00 00               je 0x14099bbf1
0099BA81  48 8B D8                        mov rbx, rax
0099BA84  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0099BA8C  48 C7 44 24 60 EE EE 00 00      mov qword ptr [rsp + 0x60], 0xeeee
0099BA95  89 BC 24 80 00 00 00            mov dword ptr [rsp + 0x80], edi
0099BA9C  48 8B F7                        mov rsi, rdi
0099BA9F  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
0099BAA4  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
0099BAAC  48 8B C7                        mov rax, rdi
0099BAAF  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0099BAB7  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
0099BABF  41 8B FF                        mov edi, r15d
0099BAC2  F7 D7                           not edi
0099BAC4  40 F6 C7 10                     test dil, 0x10
0099BAC8  74 6C                           je 0x14099bb36
0099BACA  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0099BACE  8D 41 FF                        lea eax, [rcx - 1]
0099BAD1  83 F8 02                        cmp eax, 2
0099BAD4  77 60                           ja 0x14099bb36
0099BAD6  80 3D 1D 0B 5F 00 01            cmp byte ptr [rip + 0x5f0b1d], 1
0099BADD  75 57                           jne 0x14099bb36
0099BADF  83 F9 03                        cmp ecx, 3
0099BAE2  0F 85 56 01 00 00               jne 0x14099bc3e
0099BAE8  45 0F B7 4D 10                  movzx r9d, word ptr [r13 + 0x10]
0099BAED  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
0099BAF2  66 44 89 4C 24 7C               mov word ptr [rsp + 0x7c], r9w
0099BAF8  49 8B 4D 00                     mov rcx, qword ptr [r13]
0099BAFC  48 8D 41 F0                     lea rax, [rcx - 0x10]
0099BB00  48 A9 F7 FF FF FF               test rax, -9
0099BB06  0F 84 EF 00 00 00               je 0x14099bbfb
0099BB0C  48 F7 C1 00 00 FF FF            test rcx, -0x10000
0099BB13  0F 85 2D 01 00 00               jne 0x14099bc46
0099BB19  49 8B D5                        mov rdx, r13
0099BB1C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099BB21  E8 B6 99 AB FF                  call 0x1404554dc
0099BB26  44 0B F8                        or r15d, eax
0099BB29  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
0099BB2E  44 89 BC 24 68 01 00 00         mov dword ptr [rsp + 0x168], r15d
0099BB36  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099BB3B  44 8A 05 B8 0A 5F 00            mov r8b, byte ptr [rip + 0x5f0ab8]
0099BB42  41 BA 01 00 00 00               mov r10d, 1
0099BB48  45 3A C2                        cmp r8b, r10b
0099BB4B  0F 85 93 00 00 00               jne 0x14099bbe4
0099BB51  41 8B D7                        mov edx, r15d
0099BB54  F7 D2                           not edx
0099BB56  0F BA E2 13                     bt edx, 0x13
0099BB5A  0F 92 C1                        setb cl
0099BB5D  0F BA E2 11                     bt edx, 0x11
0099BB61  0F 92 C0                        setb al
0099BB64  22 C8                           and cl, al
0099BB66  F6 C2 10                        test dl, 0x10
0099BB69  0F 95 C0                        setne al
0099BB6C  84 C8                           test al, cl
0099BB6E  74 74                           je 0x14099bbe4
0099BB70  41 8A FA                        mov dil, r10b
0099BB73  44 88 54 24 34                  mov byte ptr [rsp + 0x34], r10b
0099BB78  45 33 D2                        xor r10d, r10d
0099BB7B  45 84 C0                        test r8b, r8b
0099BB7E  74 14                           je 0x14099bb94
0099BB80  41 0F BA E7 19                  bt r15d, 0x19
0099BB85  72 0D                           jb 0x14099bb94
0099BB87  41 0F BA E7 12                  bt r15d, 0x12
0099BB8C  72 06                           jb 0x14099bb94
0099BB8E  8A 54 24 36                     mov dl, byte ptr [rsp + 0x36]
0099BB92  EB 07                           jmp 0x14099bb9b
0099BB94  41 8A D2                        mov dl, r10b
0099BB97  88 54 24 36                     mov byte ptr [rsp + 0x36], dl
0099BB9B  40 84 FF                        test dil, dil
0099BB9E  75 08                           jne 0x14099bba8
0099BBA0  84 D2                           test dl, dl
0099BBA2  0F 84 AD F8 FF FF               je 0x14099b455
0099BBA8  49 8B 45 00                     mov rax, qword ptr [r13]
0099BBAC  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0099BBB4  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0099BBB8  83 F9 02                        cmp ecx, 2
0099BBBB  72 7C                           jb 0x14099bc39
0099BBBD  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0099BBC1  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0099BBC9  41 83 FC 04                     cmp r12d, 4
0099BBCD  0F 85 86 F8 FF FF               jne 0x14099b459
0099BBD3  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0099BBD7  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0099BBDF  E9 75 F8 FF FF                  jmp 0x14099b459
0099BBE4  45 33 D2                        xor r10d, r10d
0099BBE7  41 8A FA                        mov dil, r10b
0099BBEA  44 88 54 24 34                  mov byte ptr [rsp + 0x34], r10b
0099BBEF  EB 8A                           jmp 0x14099bb7b
0099BBF1  B8 89 00 00 C0                  mov eax, 0xc0000089
0099BBF6  E9 D1 01 00 00                  jmp 0x14099bdcc
0099BBFB  40 F6 C7 08                     test dil, 8
0099BBFF  0F 84 14 FF FF FF               je 0x14099bb19
0099BC05  B8 FF F3 00 00                  mov eax, 0xf3ff
0099BC0A  66 44 85 C8                     test ax, r9w
0099BC0E  0F 85 05 FF FF FF               jne 0x14099bb19
0099BC14  B8 00 0C 00 00                  mov eax, 0xc00
0099BC19  66 44 3B C8                     cmp r9w, ax
0099BC1D  0F 84 F6 FE FF FF               je 0x14099bb19
0099BC23  41 83 CF 10                     or r15d, 0x10
0099BC27  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
0099BC2C  44 89 BC 24 68 01 00 00         mov dword ptr [rsp + 0x168], r15d
0099BC34  E9 02 FF FF FF                  jmp 0x14099bb3b
0099BC39  49 8B C2                        mov rax, r10
0099BC3C  EB 83                           jmp 0x14099bbc1
0099BC3E  45 33 C9                        xor r9d, r9d
0099BC41  E9 A7 FE FF FF                  jmp 0x14099baed
0099BC46  48 8D 15 13 98 16 00            lea rdx, [rip + 0x169813]
0099BC4D  E8 2E 44 B6 FF                  call 0x140500080
0099BC52  85 C0                           test eax, eax
0099BC54  0F 85 BF FE FF FF               jne 0x14099bb19
0099BC5A  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0099BC5F  EB 9A                           jmp 0x14099bbfb
0099BC61  85 C0                           test eax, eax
0099BC63  0F 84 05 FB FF FF               je 0x14099b76e
0099BC69  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099BC6E  48 89 18                        mov qword ptr [rax], rbx
0099BC71  E9 E2 FB FF FF                  jmp 0x14099b858
0099BC76  B8 0D 00 00 C0                  mov eax, 0xc000000d
0099BC7B  E9 DB FB FF FF                  jmp 0x14099b85b
0099BC80  B8 8B 00 00 C0                  mov eax, 0xc000008b
0099BC85  E9 2E 01 00 00                  jmp 0x14099bdb8
0099BC8A  B8 8A 00 00 C0                  mov eax, 0xc000008a
0099BC8F  E9 C7 FB FF FF                  jmp 0x14099b85b
0099BC94  45 8B F3                        mov r14d, r11d
0099BC97  66 44 89 5C 24 30               mov word ptr [rsp + 0x30], r11w
0099BC9D  44 39 1D F4 DD 63 00            cmp dword ptr [rip + 0x63ddf4], r11d
0099BCA4  0F 84 5C FC FF FF               je 0x14099b906
0099BCAA  66 44 3B 1D AE DD 63 00         cmp r11w, word ptr [rip + 0x63ddae]
0099BCB2  0F 84 4E FC FF FF               je 0x14099b906
0099BCB8  66 44 3B 1D B0 DD 63 00         cmp r11w, word ptr [rip + 0x63ddb0]
0099BCC0  0F 84 40 FC FF FF               je 0x14099b906
0099BCC6  40 84 FF                        test dil, dil
0099BCC9  0F 84 6B F9 FF FF               je 0x14099b63a
0099BCCF  4C 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r11
0099BCD7  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099BCDC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099BCE1  45 8B CF                        mov r9d, r15d
0099BCE4  45 8B C4                        mov r8d, r12d
0099BCE7  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099BCEF  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099BCF4  E8 9F 99 AB FF                  call 0x140455698
0099BCF9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099BCFD  45 33 D2                        xor r10d, r10d
0099BD00  85 C0                           test eax, eax
0099BD02  0F 88 32 F9 FF FF               js 0x14099b63a
0099BD08  E9 BF 00 00 00                  jmp 0x14099bdcc
0099BD0D  8B 0D 85 DD 63 00               mov ecx, dword ptr [rip + 0x63dd85]
0099BD13  44 0F B7 F1                     movzx r14d, cx
0099BD17  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
0099BD1C  66 3B 0D 3D DD 63 00            cmp cx, word ptr [rip + 0x63dd3d]
0099BD23  0F 84 DD FB FF FF               je 0x14099b906
0099BD29  66 3B 0D 40 DD 63 00            cmp cx, word ptr [rip + 0x63dd40]
0099BD30  0F 84 D0 FB FF FF               je 0x14099b906
0099BD36  40 84 FF                        test dil, dil
0099BD39  0F 84 FB F8 FF FF               je 0x14099b63a
0099BD3F  0F B7 C1                        movzx eax, cx
0099BD42  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
0099BD4A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0099BD4F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0099BD54  45 8B CF                        mov r9d, r15d
0099BD57  45 8B C4                        mov r8d, r12d
0099BD5A  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0099BD62  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0099BD67  E8 2C 99 AB FF                  call 0x140455698
0099BD6C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099BD70  45 33 D2                        xor r10d, r10d
0099BD73  85 C0                           test eax, eax
0099BD75  0F 88 BF F8 FF FF               js 0x14099b63a
0099BD7B  EB 4F                           jmp 0x14099bdcc
0099BD7D  44 0F B7 74 24 30               movzx r14d, word ptr [rsp + 0x30]
0099BD83  E9 46 FA FF FF                  jmp 0x14099b7ce
0099BD88  49 8D 47 F8                     lea rax, [r15 - 8]
0099BD8C  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0099BD94  40 84 FF                        test dil, dil
0099BD97  74 0B                           je 0x14099bda4
0099BD99  66 44 89 64 24 4C               mov word ptr [rsp + 0x4c], r12w
0099BD9F  E9 9B FA FF FF                  jmp 0x14099b83f
0099BDA4  41 8D 7C 24 FF                  lea edi, [r12 - 1]
0099BDA9  66 89 7C 24 4C                  mov word ptr [rsp + 0x4c], di
0099BDAE  E9 90 FA FF FF                  jmp 0x14099b843
0099BDB3  B8 04 02 00 C0                  mov eax, 0xc0000204
0099BDB8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099BDBC  E9 A9 FA FF FF                  jmp 0x14099b86a
0099BDC1  B8 0D 00 00 C0                  mov eax, 0xc000000d
0099BDC6  EB 04                           jmp 0x14099bdcc
0099BDC8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0099BDCC  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
0099BDD4  48 33 CC                        xor rcx, rsp
0099BDD7  E8 64 08 D1 FF                  call 0x1406ac640
0099BDDC  48 81 C4 10 01 00 00            add rsp, 0x110
0099BDE3  41 5F                           pop r15
0099BDE5  41 5E                           pop r14
0099BDE7  41 5D                           pop r13
0099BDE9  41 5C                           pop r12
0099BDEB  5F                              pop rdi
0099BDEC  5E                              pop rsi
0099BDED  5B                              pop rbx
0099BDEE  C3                              ret
0099BDEF  CC                              int3
0099BDF0  41 83 FC 04                     cmp r12d, 4
0099BDF4  0F 84 71 F5 FF FF               je 0x14099b36b
0099BDFA  B8 F1 00 00 C0                  mov eax, 0xc00000f1
0099BDFF  EB CB                           jmp 0x14099bdcc
0099BE01  85 C0                           test eax, eax
0099BE03  0F 85 6C F5 FF FF               jne 0x14099b375
0099BE09  EB EF                           jmp 0x14099bdfa
0099BE0B  41 F6 C7 02                     test r15b, 2
0099BE0F  74 E9                           je 0x14099bdfa
0099BE11  E9 3F F5 FF FF                  jmp 0x14099b355
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpSearchResourceSection_U(__int64 a1, __int64 a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int8 v_stack_m103;
    unsigned __int8 v_stack_m104;
    unsigned __int16 v_stack_m108;
    unsigned __int8 v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int8 v_stack_m112;
    unsigned __int8 v_stack_m113;
    unsigned __int8 v_stack_m114;
    unsigned __int16 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int16 v_stack_mCC;
    unsigned __int8 v_stack_mCF;
    unsigned __int8 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int16 v_stack_mFC;
    unsigned int v_stack_p20;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 4650058)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mF4 = a4;
    v_stack_mA0 = a3;
    v_stack_mE0 = a1;
    v_stack_mF0 = a5;
    v_rdi = 0;
    v_stack_mE8 = 0;
    v_stack_m70 = a2;
    v_stack_m113 = 0;
    v_stack_m10C = (unsigned __int8)(v_rdi + 1);
    v_stack_m112 = (unsigned __int8)(v_rdi + 1);
    if (a3 < 3) goto loc_0099BE0B;
loc_0099B355:
    if (((unsigned int)((unsigned int)(a3))) > 4) goto loc_0099BDFA;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (65));
    if (condition_is_not_equal) goto loc_0099BDF0;
loc_0099B36B:
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_0099BE01;
loc_0099B375:
    result = 3;
    if (((unsigned int)((unsigned int)(a3))) != 4) { result = (unsigned int)((unsigned int)(a3)); }
    v_stack_m100 = (unsigned int)(result);
    v_stack_mF8 = (unsigned int)(result);
    v_stack_m108 = 0;
    v_stack_m118 = 0;
    if ((a2 - 1) > -3) goto loc_0099BDC1;
    goto loc_0099BA41;
loc_0099B3AB:
    v_stack_m98 = v_rsi;
    result = ((unsigned __int16)((unsigned int)(a3))) << (3);
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    if (condition_is_equal) goto loc_0099B979;
loc_0099B3C9:
    v_stack_m98 = result + v_rsi * 1;
    v_stack_m104 = (unsigned __int8)(v_rdi + 1);
    v_stack_m120 = v_stack_m104;
    v_stack_m128 = result + v_rsi * 1;
    result = LdrpCompareResourceNamesWithValidation(a1, a5, *(unsigned __int64 *)(a2), v_stack_mB0);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_0099B81F;
    if ((*(unsigned int *)(result + v_rsi * 1 + 4)) >= 0) goto loc_0099B9CE;
loc_0099B417:
    v_rbx = ((unsigned int)(*(unsigned int *)(result + v_rsi * 1 + 4))) + (v_stack_mB0);
    v_stack_mC0 = v_rbx;
loc_0099B429:
loc_0099B42E:
    v_r13 = (a2) + (8);
    v_stack_m68 = v_r13;
loc_0099B455:
loc_0099B459:
    if (v_rbx == 0) goto loc_0099B74E;
    a3 = (unsigned int)(((unsigned int)(v_stack_mF8)) - 1);
    v_stack_mF8 = a3;
    v_stack_m80 = a3;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF8)))) == 0) goto loc_0099B74E;
    if (a3 == 0) goto loc_0099B695;
loc_0099B491:
loc_0099B499:
    if (v_stack_mB8 != 0) goto loc_0099B574;
loc_0099B4A2:
    v_stack_mFC = (unsigned __int16)(*(unsigned __int16 *)(v_rbx + 12));
    v_stack_m90 = v_rbx + 16;
    v_rsi = v_rbx + 16;
    v_rdi = *(unsigned __int16 *)(v_rbx + 12);
    if (((*(unsigned __int64 *)(v_r13)) & (0xFFFFFFFFFFFF0000ULL)) == 0) {
        v_rsi = v_rbx + 16 + *(unsigned __int16 *)(v_rbx + 12) * 8;
        v_stack_m90 = v_rsi;
        v_rdi = *(unsigned __int16 *)(v_rbx + 14);
        v_stack_mFC = (unsigned __int16)(v_rdi);
        a1 = (unsigned __int16)(v_rdi);
    }
    if ((unsigned __int16)(a1) == 0) goto loc_0099B917;
    if (v_stack_mB8 != 0) goto loc_0099B709;
loc_0099B4EE:
    v_stack_mC0 = 0;
    result = ((unsigned __int16)(a1)) - 1;
    v_stack_m88 = v_rsi + result * 8;
loc_0099B50B:
    if (v_rsi > (v_rsi + result * 8)) goto loc_0099B429;
    v_r12 = (unsigned __int16)(((unsigned __int16)(v_rdi)) >> (1));
    if (condition_is_not_equal) goto loc_0099B3AB;
    if ((unsigned __int16)(v_rdi) == 0) goto loc_0099B429;
    v_stack_m103 = 0;
    v_stack_m120 = v_stack_m103;
    v_stack_m128 = v_rsi;
    result = LdrpCompareResourceNamesWithValidation(a1, v_stack_mB8, *(unsigned __int64 *)(v_r13), v_stack_mB0);
    v_r10 = 0;
    if ((unsigned int)(result) != 0) goto loc_0099B429;
    if ((*(unsigned int *)(v_rsi + 4)) < 0) goto loc_0099B417;
    goto loc_0099B9E4;
loc_0099B574:
    v_stack_m108 = (unsigned int)(*(unsigned __int16 *)(v_stack_m70 + 16));
    v_stack_mCC = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m70 + 16));
    a1 = ((((unsigned __int16)((unsigned int)(0x3FFULL))) & ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m70 + 16)))) == 0) ? 1 : 0;
    v_stack_m113 = (unsigned __int8)(a1);
    v_stack_mD0 = (unsigned __int8)(a1);
loc_0099B5A0:
loc_0099B5A7:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mC8)) + 1);
    v_stack_mC8 = (unsigned int)(v_rbx);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC8)))) == 0) goto loc_0099B627;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mC8)))) - (1));
    if (condition_is_equal) goto loc_0099B7C4;
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_0099B8ED;
    if ((unsigned __int8)(a1) == 0) goto loc_0099BDB3;
    if ((unsigned __int8)(v_stack_mB0) == 0) goto loc_0099B985;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 6546576)) == 0) goto loc_0099B985;
    v_stack_m50 = *(unsigned __int16 *)(v_rip + 6546576);
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (sign_flag) goto loc_0099B8D8;
    goto loc_0099BDCC;
loc_0099B627:
    if ((unsigned __int8)(v_stack_mB0) != 0) goto loc_0099B887;
loc_0099B630:
    v_stack_m118 = (unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
loc_0099B63A:
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))));
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_0099B662;
    if (((unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))))) != v_stack_mE8) goto loc_0099B662;
    goto loc_0099B5A7;
loc_0099B662:
    v_stack_mE8 = (unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))));
    v_stack_m68 = v_stack_mE8;
    v_stack_mC0 = v_stack_mB8;
    goto loc_0099B4A2;
loc_0099B695:
    if ((unsigned __int8)(v_stack_mB8) == 0) goto loc_0099B6DA;
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (!sign_flag) goto loc_0099B974;
loc_0099B6DA:
    if ((unsigned int)((unsigned int)(v_stack_mF8)) != 0) goto loc_0099B491;
    a2 = v_stack_mB8;
    if (v_stack_m100 == 3) { a2 = v_stack_mB8; }
    v_stack_mB8 = a2;
    v_stack_m78 = a2;
    goto loc_0099B499;
loc_0099B709:
    if ((((unsigned __int8)((unsigned int)(v_stack_mF4))) & (32)) == 0) goto loc_0099B4EE;
    v_stack_mC0 = 0;
    v_stack_mE8 = (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi + 4)) + v_stack_mB0 * 1));
    v_rsi = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi + 4)) + v_stack_mB0 * 1 + 4))) + (v_stack_mB0);
    v_stack_mA8 = v_rsi;
    goto loc_0099B756;
loc_0099B74E:
loc_0099B756:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))) & (2));
    if (v_rsi != 0) goto loc_0099B848;
loc_0099B765:
    if (0 != 0) goto loc_0099BC61;
loc_0099B76E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m100)))) - ((unsigned int)((unsigned int)(v_stack_mF8))));
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0099BC8A;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0099BC80;
    if (((unsigned int)(result)) != 1) goto loc_0099BC76;
    v_stack_m110 = (unsigned int)((unsigned int)(0xC0000204ULL));
loc_0099B797:
    if (v_stack_mB8 == 0) goto loc_0099B86A;
    v_stack_mD8 = 0;
    v_stack_mA8 = 0;
    if (v_stack_m10C == 0) goto loc_0099BDB3;
    goto loc_0099B5A0;
loc_0099B7C4:
    if ((unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))))) != 0) goto loc_0099B9A6;
loc_0099B7CE:
    if ((unsigned __int8)(v_stack_m114) == 0) goto loc_0099B86F;
    if ((unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))))) == 0) goto loc_0099B63A;
    v_stack_m50 = (unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (sign_flag) goto loc_0099B86F;
    goto loc_0099BDCC;
loc_0099B81F:
    if (sign_flag) goto loc_0099BD88;
    v_stack_m90 = (unsigned int)(v_stack_mF4) + 8;
    v_stack_mFC = (unsigned __int16)(v_r12);
loc_0099B83F:
loc_0099B843:
    goto loc_0099B50B;
loc_0099B848:
    if ((unsigned int)(v_stack_m88) != 0) goto loc_0099B765;
    *(unsigned __int64 *)(v_stack_mF0) = (unsigned int)(v_stack_mF4) + 8;
loc_0099B858:
loc_0099B85B:
    v_stack_m110 = 0;
    if (0 == 0xC0000204ULL) goto loc_0099B797;
loc_0099B86A:
    goto loc_0099BDCC;
loc_0099B86F:
    if ((unsigned __int16)((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))))) == 0) goto loc_0099B63A;
    v_rbx = (unsigned int)((0) - 1);
    v_stack_mC8 = (unsigned int)(v_rbx);
    goto loc_0099B63A;
loc_0099B887:
    if ((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4)))) == 0) goto loc_0099B630;
    v_stack_m50 = (unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)((unsigned int)(v_stack_mF4))));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (!sign_flag) goto loc_0099BDCC;
    goto loc_0099B630;
loc_0099B8D8:
loc_0099B8DF:
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 6545809));
    goto loc_0099B63A;
loc_0099B8ED:
    result = (unsigned int)((*(unsigned __int16 *)(v_rip + 6545809)) - (1));
    if (condition_is_not_equal) goto loc_0099B943;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 6545767))) != (*(unsigned __int16 *)(v_rip + 6545776))) goto loc_0099B9F6;
loc_0099B906:
    v_stack_m118 = (unsigned __int16)(v_stack_mE8);
    goto loc_0099B63A;
loc_0099B917:
    v_stack_mC0 = 0;
    v_stack_m10C = 0;
    v_stack_mCF = 0;
    goto loc_0099B76E;
loc_0099B943:
    result = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_0099BD0D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0099BC94;
    if (((unsigned int)(result)) != 1) goto loc_0099BDB3;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mF4)) | (32));
    v_stack_mF4 = (unsigned int)(v_r15);
    v_stack_p20 = (unsigned int)(v_r15);
    goto loc_0099B63A;
loc_0099B974:
    goto loc_0099BDCC;
loc_0099B979:
    v_r15 = ((unsigned int)(v_stack_mF4) + 8 - 8) + (result);
    goto loc_0099B3C9;
loc_0099B985:
    a1 = v_stack_mE8;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 6545631)) != 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 6545631)); }
    v_stack_m118 = (unsigned __int16)(a1);
    goto loc_0099B63A;
loc_0099B9A6:
    result = LdrpGetParentLangId((unsigned __int16)((unsigned __int16)(a1)), v_stack_m118, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(v_stack_m108));
    v_r10 = 0;
    if (!sign_flag) goto loc_0099BD7D;
    v_stack_m118 = 0;
    goto loc_0099B7CE;
loc_0099B9CE:
    v_stack_mC0 = 0;
    v_rsi = (v_stack_mB0) + (result);
loc_0099B9E4:
    v_stack_mD8 = v_rsi;
    v_stack_mA8 = v_rsi;
    goto loc_0099B42E;
loc_0099B9F6:
    if ((unsigned __int8)(v_stack_m114) == 0) goto loc_0099BA30;
    v_stack_m50 = (unsigned __int16)((unsigned __int16)(a1));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_r15)));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (!sign_flag) goto loc_0099BA3C;
loc_0099BA30:
    goto loc_0099B8DF;
loc_0099BA3C:
    goto loc_0099BDCC;
loc_0099BA41:
    if ((v_stack_mE0 - 1) > -3) goto loc_0099BDC1;
    if ((v_stack_m60 - 1) > -3) goto loc_0099BDC1;
    result = RtlImageDirectoryEntryToData(v_stack_mE0, 0, 2, v_stack_mFC);
    v_stack_mB0 = result;
    if (result == 0) goto loc_0099BBF1;
    v_stack_mC0 = result;
    v_stack_mE8 = 0xEEEEULL;
    v_stack_mC8 = (unsigned int)(v_stack_m114);
    v_stack_mD8 = v_stack_m114;
    v_stack_mA8 = v_stack_m114;
    v_stack_mB8 = v_stack_m114;
    v_stack_m78 = v_stack_m114;
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_0099BB36;
    if (((unsigned int)((unsigned int)(v_stack_m100) - 1)) > 2) goto loc_0099BB36;
    if ((*(unsigned __int8 *)(v_rip + 6228765)) != 1) goto loc_0099BB36;
    if (((unsigned int)((unsigned int)(v_stack_m100))) != 3) goto loc_0099BC3E;
loc_0099BAED:
    v_stack_m108 = (unsigned int)(*(unsigned __int16 *)(v_stack_mE8 + 16));
    v_stack_mCC = (unsigned __int16)(*(unsigned __int16 *)(v_stack_mE8 + 16));
    if (((*(unsigned __int64 *)(v_stack_mE8) - 16) & (-9)) == 0) goto loc_0099BBFB;
    if (((*(unsigned __int64 *)(v_stack_mE8)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0099BC46;
loc_0099BB19:
    result = LdrIsResItemExist(v_stack_mE0, v_stack_mE8, 2, *(unsigned __int16 *)(v_stack_mE8 + 16));
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    v_stack_mF4 = (unsigned int)(v_r15);
    v_stack_p20 = (unsigned int)(v_r15);
loc_0099BB36:
loc_0099BB3B:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6228664))) != 1) goto loc_0099BBE4;
    a2 = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
    a1 = (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6228664))) < 1) ? 1 : 0;
    result = (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6228664))) < 1) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    result = ((((unsigned __int8)(a2)) & (16)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0099BBE4;
    v_stack_m114 = 1;
    v_r10 = 0;
loc_0099BB7B:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6228664)) == 0) goto loc_0099BB94;
    if (condition_is_below) goto loc_0099BB94;
    if (condition_is_below) goto loc_0099BB94;
    goto loc_0099BB9B;
loc_0099BB94:
    v_stack_m112 = 0;
loc_0099BB9B:
    if (1 != 0) goto loc_0099BBA8;
    if (0 == 0) goto loc_0099B455;
loc_0099BBA8:
    v_stack_m60 = *(unsigned __int64 *)(v_stack_mE8);
    if (((unsigned int)((unsigned int)(v_stack_m100))) < 2) goto loc_0099BC39;
loc_0099BBC1:
    v_stack_m58 = *(unsigned __int64 *)(v_stack_mE8 + 8);
    if (((unsigned int)(v_r12)) != 4) goto loc_0099B459;
    v_stack_m48 = *(unsigned __int64 *)(v_stack_mE8 + 24);
    goto loc_0099B459;
loc_0099BBE4:
    v_r10 = 0;
    v_stack_m114 = 0;
    goto loc_0099BB7B;
loc_0099BBF1:
    goto loc_0099BDCC;
loc_0099BBFB:
    if (((0) & (8)) == 0) goto loc_0099BB19;
    if ((((unsigned __int16)((unsigned int)(0xF3FFULL))) & ((unsigned __int16)((unsigned int)(v_stack_m108)))) != 0) goto loc_0099BB19;
    if (((unsigned __int16)((unsigned int)(v_stack_m108))) == ((unsigned __int16)((unsigned int)(0xC00ULL)))) goto loc_0099BB19;
    v_r15 = (unsigned int)((v_r15) | (16));
    v_stack_mF4 = (unsigned int)(v_r15);
    v_stack_p20 = (unsigned int)(v_r15);
    goto loc_0099BB3B;
loc_0099BC39:
    goto loc_0099BBC1;
loc_0099BC3E:
    a4 = 0;
    goto loc_0099BAED;
loc_0099BC46:
    result = wcsicmp((unsigned int)(v_stack_m100), v_rip + 1480723, *(unsigned __int8 *)(v_rip + 6228664), a4);
    if ((unsigned int)(result) != 0) goto loc_0099BB19;
    goto loc_0099BBFB;
loc_0099BC61:
    if ((unsigned int)(result) == 0) goto loc_0099B76E;
    *(unsigned __int64 *)(v_stack_mF0) = result;
    goto loc_0099B858;
loc_0099BC76:
    goto loc_0099B85B;
loc_0099BC80:
    goto loc_0099BDB8;
loc_0099BC8A:
    goto loc_0099B85B;
loc_0099BC94:
    v_stack_m118 = (unsigned __int16)((unsigned int)(0x409ULL));
    if ((*(unsigned int *)(v_rip + 6544884)) == ((unsigned int)((unsigned int)(0x409ULL)))) goto loc_0099B906;
    if (((unsigned __int16)((unsigned int)(0x409ULL))) == (*(unsigned __int16 *)(v_rip + 6544814))) goto loc_0099B906;
    if (((unsigned __int16)((unsigned int)(0x409ULL))) == (*(unsigned __int16 *)(v_rip + 6544816))) goto loc_0099B906;
    if (0 == 0) goto loc_0099B63A;
    v_stack_m50 = (unsigned int)(0x409ULL);
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_r15)));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (sign_flag) goto loc_0099B63A;
    goto loc_0099BDCC;
loc_0099BD0D:
    v_stack_m118 = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 6544773)));
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 6544773)))) == (*(unsigned __int16 *)(v_rip + 6544701))) goto loc_0099B906;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 6544773)))) == (*(unsigned __int16 *)(v_rip + 6544704))) goto loc_0099B906;
    if (0 == 0) goto loc_0099B63A;
    v_stack_m50 = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 6544773)));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_r15)));
    v_stack_m110 = (unsigned int)(result);
    v_r10 = 0;
    if (sign_flag) goto loc_0099B63A;
    goto loc_0099BDCC;
loc_0099BD7D:
    goto loc_0099B7CE;
loc_0099BD88:
    v_stack_m88 = v_r15 - 8;
    if (0 == 0) goto loc_0099BDA4;
    v_stack_mFC = (unsigned __int16)(v_r12);
    goto loc_0099B83F;
loc_0099BDA4:
    v_stack_mFC = (unsigned __int16)(v_r12 - 1);
    goto loc_0099B843;
loc_0099BDB3:
loc_0099BDB8:
    v_stack_m110 = (unsigned int)((unsigned int)(0xC0000204ULL));
    goto loc_0099B86A;
loc_0099BDC1:
    goto loc_0099BDCC;
loc_0099BDCC:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m60, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_r15)));
    v_rsp = (v_rsp) + (272);
    return result;
loc_0099BDF0:
    if (((unsigned int)(v_r12)) == 4) goto loc_0099B36B;
loc_0099BDFA:
    goto loc_0099BDCC;
loc_0099BE01:
    if ((unsigned int)((unsigned int)(0xC00000F1ULL)) != 0) goto loc_0099B375;
    goto loc_0099BDFA;
loc_0099BE0B:
    if ((((unsigned __int8)(v_r15)) & (2)) == 0) goto loc_0099BDFA;
    goto loc_0099B355;
}
```

## 5. (Beta) C Style

```c
int64_t LdrpSearchResourceSection_U(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint8_t v_stack_m103;
    uint8_t v_stack_m104;
    uint16_t v_stack_m108;
    uint8_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint8_t v_stack_m112;
    uint8_t v_stack_m113;
    uint8_t v_stack_m114;
    uint16_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint16_t v_stack_mCC;
    uint8_t v_stack_mCF;
    uint8_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint16_t v_stack_mFC;
    uint32_t v_stack_p20;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x46F44A)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mF4 = Arg4;
    v_stack_mA0 = Arg3;
    v_stack_mE0 = Arg1;
    v_stack_mF0 = Arg5;
    local_rdi = 0;
    v_stack_mE8 = 0;
    v_stack_m70 = Arg2;
    v_stack_m113 = 0;
    v_stack_m10C = (uint8_t)(local_rdi + 1);
    v_stack_m112 = (uint8_t)(local_rdi + 1);
    if (Arg3 < 3) goto loc_0099BE0B;
loc_0099B355:
    if (((uint32_t)((uint32_t)(Arg3))) > 4) goto loc_0099BDFA;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (65));
    if (condition_is_not_equal) goto loc_0099BDF0;
loc_0099B36B:
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_0099BE01;
loc_0099B375:
    result = 3;
    if (((uint32_t)((uint32_t)(Arg3))) != 4) { result = (uint32_t)((uint32_t)(Arg3)); }
    v_stack_m100 = (uint32_t)(result);
    v_stack_mF8 = (uint32_t)(result);
    v_stack_m108 = 0;
    v_stack_m118 = 0;
    if ((Arg2 - 1) > -3) goto loc_0099BDC1;
    goto loc_0099BA41;
loc_0099B3AB:
    v_stack_m98 = local_rsi;
    result = ((uint16_t)((uint32_t)(Arg3))) << (3);
    local_rdi = (uint8_t)((local_rdi) & (1));
    if (condition_is_equal) goto loc_0099B979;
loc_0099B3C9:
    v_stack_m98 = result + local_rsi * 1;
    v_stack_m104 = (uint8_t)(local_rdi + 1);
    v_stack_m120 = v_stack_m104;
    v_stack_m128 = result + local_rsi * 1;
    result = LdrpCompareResourceNamesWithValidation(Arg1, Arg5, *(uint64_t *)(arg2), v_stack_mB0);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_0099B81F;
    if ((*(uint32_t *)(result + local_rsi * 1 + 0x4)) >= 0) goto loc_0099B9CE;
loc_0099B417:
    local_rbx = ((uint32_t)(*(uint32_t *)(result + local_rsi * 1 + 0x4))) + (v_stack_mB0);
    v_stack_mC0 = local_rbx;
loc_0099B429:
loc_0099B42E:
    local_r13 = (Arg2) + (8);
    v_stack_m68 = local_r13;
loc_0099B455:
loc_0099B459:
    if (local_rbx == 0) goto loc_0099B74E;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mF8)) - 1);
    v_stack_mF8 = Arg3;
    v_stack_m80 = Arg3;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF8)))) == 0) goto loc_0099B74E;
    if (Arg3 == 0) goto loc_0099B695;
loc_0099B491:
loc_0099B499:
    if (v_stack_mB8 != 0) goto loc_0099B574;
loc_0099B4A2:
    v_stack_mFC = (uint16_t)(*(uint16_t *)(local_rbx + 0xC));
    v_stack_m90 = local_rbx + 16;
    local_rsi = local_rbx + 16;
    local_rdi = *(uint16_t *)(local_rbx + 0xC);
    if (((*(uint64_t *)(local_r13)) & (0xFFFFFFFFFFFF0000ULL)) == 0) {
        local_rsi = local_rbx + 16 + *(uint16_t *)(local_rbx + 0xC) * 8;
        v_stack_m90 = local_rsi;
        local_rdi = *(uint16_t *)(local_rbx + 0xE);
        v_stack_mFC = (uint16_t)(local_rdi);
        Arg1 = (uint16_t)(local_rdi);
    }
    if ((uint16_t)(Arg1) == 0) goto loc_0099B917;
    if (v_stack_mB8 != 0) goto loc_0099B709;
loc_0099B4EE:
    v_stack_mC0 = 0;
    result = ((uint16_t)(Arg1)) - 1;
    v_stack_m88 = local_rsi + result * 8;
loc_0099B50B:
    if (local_rsi > (local_rsi + result * 8)) goto loc_0099B429;
    local_r12 = (uint16_t)(((uint16_t)(local_rdi)) >> (1));
    if (condition_is_not_equal) goto loc_0099B3AB;
    if ((uint16_t)(local_rdi) == 0) goto loc_0099B429;
    v_stack_m103 = 0;
    v_stack_m120 = v_stack_m103;
    v_stack_m128 = local_rsi;
    result = LdrpCompareResourceNamesWithValidation(Arg1, v_stack_mB8, *(uint64_t *)(local_r13), v_stack_mB0);
    local_r10 = 0;
    if ((uint32_t)(result) != 0) goto loc_0099B429;
    if ((*(uint32_t *)(local_rsi + 0x4)) < 0) goto loc_0099B417;
    goto loc_0099B9E4;
loc_0099B574:
    v_stack_m108 = (uint32_t)(*(uint16_t *)(v_stack_m70 + 0x10));
    v_stack_mCC = (uint16_t)(*(uint16_t *)(v_stack_m70 + 0x10));
    Arg1 = ((((uint16_t)((uint32_t)(0x3FFULL))) & ((uint16_t)(*(uint16_t *)(v_stack_m70 + 0x10)))) == 0) ? 1 : 0;
    v_stack_m113 = (uint8_t)(Arg1);
    v_stack_mD0 = (uint8_t)(Arg1);
loc_0099B5A0:
loc_0099B5A7:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mC8)) + 1);
    v_stack_mC8 = (uint32_t)(local_rbx);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC8)))) == 0) goto loc_0099B627;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mC8)))) - (1));
    if (condition_is_equal) goto loc_0099B7C4;
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_0099B8ED;
    if ((uint8_t)(Arg1) == 0) goto loc_0099BDB3;
    if ((uint8_t)(v_stack_mB0) == 0) goto loc_0099B985;
    if ((uint16_t)(*(uint16_t *)(v_rip + 0x63E490)) == 0) goto loc_0099B985;
    v_stack_m50 = *(uint16_t *)(v_rip + 0x63E490);
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (sign_flag) goto loc_0099B8D8;
    goto loc_0099BDCC;
loc_0099B627:
    if ((uint8_t)(v_stack_mB0) != 0) goto loc_0099B887;
loc_0099B630:
    v_stack_m118 = (uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
loc_0099B63A:
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))));
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_0099B662;
    if (((uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))))) != v_stack_mE8) goto loc_0099B662;
    goto loc_0099B5A7;
loc_0099B662:
    v_stack_mE8 = (uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))));
    v_stack_m68 = v_stack_mE8;
    v_stack_mC0 = v_stack_mB8;
    goto loc_0099B4A2;
loc_0099B695:
    if ((uint8_t)(v_stack_mB8) == 0) goto loc_0099B6DA;
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (!sign_flag) goto loc_0099B974;
loc_0099B6DA:
    if ((uint32_t)((uint32_t)(v_stack_mF8)) != 0) goto loc_0099B491;
    Arg2 = v_stack_mB8;
    if (v_stack_m100 == 3) { Arg2 = v_stack_mB8; }
    v_stack_mB8 = Arg2;
    v_stack_m78 = Arg2;
    goto loc_0099B499;
loc_0099B709:
    if ((((uint8_t)((uint32_t)(v_stack_mF4))) & (32)) == 0) goto loc_0099B4EE;
    v_stack_mC0 = 0;
    v_stack_mE8 = (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)) + v_stack_mB0 * 1));
    local_rsi = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)) + v_stack_mB0 * 1 + 0x4))) + (v_stack_mB0);
    v_stack_mA8 = local_rsi;
    goto loc_0099B756;
loc_0099B74E:
loc_0099B756:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))) & (2));
    if (local_rsi != 0) goto loc_0099B848;
loc_0099B765:
    if (0 != 0) goto loc_0099BC61;
loc_0099B76E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m100)))) - ((uint32_t)((uint32_t)(v_stack_mF8))));
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0099BC8A;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0099BC80;
    if (((uint32_t)(result)) != 1) goto loc_0099BC76;
    v_stack_m110 = (uint32_t)((uint32_t)(0xC0000204ULL));
loc_0099B797:
    if (v_stack_mB8 == 0) goto loc_0099B86A;
    v_stack_mD8 = 0;
    v_stack_mA8 = 0;
    if (v_stack_m10C == 0) goto loc_0099BDB3;
    goto loc_0099B5A0;
loc_0099B7C4:
    if ((uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))))) != 0) goto loc_0099B9A6;
loc_0099B7CE:
    if ((uint8_t)(v_stack_m114) == 0) goto loc_0099B86F;
    if ((uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))))) == 0) goto loc_0099B63A;
    v_stack_m50 = (uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (sign_flag) goto loc_0099B86F;
    goto loc_0099BDCC;
loc_0099B81F:
    if (sign_flag) goto loc_0099BD88;
    v_stack_m90 = (uint32_t)(v_stack_mF4) + 8;
    v_stack_mFC = (uint16_t)(local_r12);
loc_0099B83F:
loc_0099B843:
    goto loc_0099B50B;
loc_0099B848:
    if ((uint32_t)(v_stack_m88) != 0) goto loc_0099B765;
    *(uint64_t *)(v_stack_mF0) = (uint32_t)(v_stack_mF4) + 8;
loc_0099B858:
loc_0099B85B:
    v_stack_m110 = 0;
    if (0 == 0xC0000204ULL) goto loc_0099B797;
loc_0099B86A:
    goto loc_0099BDCC;
loc_0099B86F:
    if ((uint16_t)((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))))) == 0) goto loc_0099B63A;
    local_rbx = (uint32_t)((0) - 1);
    v_stack_mC8 = (uint32_t)(local_rbx);
    goto loc_0099B63A;
loc_0099B887:
    if ((uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4)))) == 0) goto loc_0099B630;
    v_stack_m50 = (uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)((uint32_t)(v_stack_mF4))));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (!sign_flag) goto loc_0099BDCC;
    goto loc_0099B630;
loc_0099B8D8:
loc_0099B8DF:
    v_stack_m118 = (uint16_t)(*(uint16_t *)(v_rip + 0x63E191));
    goto loc_0099B63A;
loc_0099B8ED:
    result = (uint32_t)((*(uint16_t *)(v_rip + 0x63E191)) - (1));
    if (condition_is_not_equal) goto loc_0099B943;
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x63E167))) != (*(uint16_t *)(v_rip + 0x63E170))) goto loc_0099B9F6;
loc_0099B906:
    v_stack_m118 = (uint16_t)(v_stack_mE8);
    goto loc_0099B63A;
loc_0099B917:
    v_stack_mC0 = 0;
    v_stack_m10C = 0;
    v_stack_mCF = 0;
    goto loc_0099B76E;
loc_0099B943:
    result = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_0099BD0D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0099BC94;
    if (((uint32_t)(result)) != 1) goto loc_0099BDB3;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mF4)) | (32));
    v_stack_mF4 = (uint32_t)(local_r15);
    v_stack_p20 = (uint32_t)(local_r15);
    goto loc_0099B63A;
loc_0099B974:
    goto loc_0099BDCC;
loc_0099B979:
    local_r15 = ((uint32_t)(v_stack_mF4) + 8 - 8) + (result);
    goto loc_0099B3C9;
loc_0099B985:
    Arg1 = v_stack_mE8;
    if ((uint16_t)(*(uint16_t *)(v_rip + 0x63E0DF)) != 0) { Arg1 = (uint16_t)(*(uint16_t *)(v_rip + 0x63E0DF)); }
    v_stack_m118 = (uint16_t)(Arg1);
    goto loc_0099B63A;
loc_0099B9A6:
    result = LdrpGetParentLangId((uint16_t)((uint16_t)(Arg1)), v_stack_m118, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(v_stack_m108));
    local_r10 = 0;
    if (!sign_flag) goto loc_0099BD7D;
    v_stack_m118 = 0;
    goto loc_0099B7CE;
loc_0099B9CE:
    v_stack_mC0 = 0;
    local_rsi = (v_stack_mB0) + (result);
loc_0099B9E4:
    v_stack_mD8 = local_rsi;
    v_stack_mA8 = local_rsi;
    goto loc_0099B42E;
loc_0099B9F6:
    if ((uint8_t)(v_stack_m114) == 0) goto loc_0099BA30;
    v_stack_m50 = (uint16_t)((uint16_t)(Arg1));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_r15)));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (!sign_flag) goto loc_0099BA3C;
loc_0099BA30:
    goto loc_0099B8DF;
loc_0099BA3C:
    goto loc_0099BDCC;
loc_0099BA41:
    if ((v_stack_mE0 - 1) > -3) goto loc_0099BDC1;
    if ((v_stack_m60 - 1) > -3) goto loc_0099BDC1;
    result = RtlImageDirectoryEntryToData(v_stack_mE0, 0, 2, v_stack_mFC);
    v_stack_mB0 = result;
    if (result == 0) goto loc_0099BBF1;
    v_stack_mC0 = result;
    v_stack_mE8 = 0xEEEEULL;
    v_stack_mC8 = (uint32_t)(v_stack_m114);
    v_stack_mD8 = v_stack_m114;
    v_stack_mA8 = v_stack_m114;
    v_stack_mB8 = v_stack_m114;
    v_stack_m78 = v_stack_m114;
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_0099BB36;
    if (((uint32_t)((uint32_t)(v_stack_m100) - 1)) > 2) goto loc_0099BB36;
    if ((*(uint8_t *)(v_rip + 0x5F0B1D)) != 1) goto loc_0099BB36;
    if (((uint32_t)((uint32_t)(v_stack_m100))) != 3) goto loc_0099BC3E;
loc_0099BAED:
    v_stack_m108 = (uint32_t)(*(uint16_t *)(v_stack_mE8 + 0x10));
    v_stack_mCC = (uint16_t)(*(uint16_t *)(v_stack_mE8 + 0x10));
    if (((*(uint64_t *)(v_stack_mE8) - 16) & (-9)) == 0) goto loc_0099BBFB;
    if (((*(uint64_t *)(v_stack_mE8)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0099BC46;
loc_0099BB19:
    result = LdrIsResItemExist(v_stack_mE0, v_stack_mE8, 2, *(uint16_t *)(v_stack_mE8 + 0x10));
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    v_stack_mF4 = (uint32_t)(local_r15);
    v_stack_p20 = (uint32_t)(local_r15);
loc_0099BB36:
loc_0099BB3B:
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x5F0AB8))) != 1) goto loc_0099BBE4;
    Arg2 = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
    Arg1 = (((uint8_t)(*(uint8_t *)(v_rip + 0x5F0AB8))) < 1) ? 1 : 0;
    result = (((uint8_t)(*(uint8_t *)(v_rip + 0x5F0AB8))) < 1) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    result = ((((uint8_t)(Arg2)) & (16)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0099BBE4;
    v_stack_m114 = 1;
    local_r10 = 0;
loc_0099BB7B:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x5F0AB8)) == 0) goto loc_0099BB94;
    if (condition_is_below) goto loc_0099BB94;
    if (condition_is_below) goto loc_0099BB94;
    goto loc_0099BB9B;
loc_0099BB94:
    v_stack_m112 = 0;
loc_0099BB9B:
    if (1 != 0) goto loc_0099BBA8;
    if (0 == 0) goto loc_0099B455;
loc_0099BBA8:
    v_stack_m60 = *(uint64_t *)(v_stack_mE8);
    if (((uint32_t)((uint32_t)(v_stack_m100))) < 2) goto loc_0099BC39;
loc_0099BBC1:
    v_stack_m58 = *(uint64_t *)(v_stack_mE8 + 0x8);
    if (((uint32_t)(local_r12)) != 4) goto loc_0099B459;
    v_stack_m48 = *(uint64_t *)(v_stack_mE8 + 0x18);
    goto loc_0099B459;
loc_0099BBE4:
    local_r10 = 0;
    v_stack_m114 = 0;
    goto loc_0099BB7B;
loc_0099BBF1:
    goto loc_0099BDCC;
loc_0099BBFB:
    if (((0) & (8)) == 0) goto loc_0099BB19;
    if ((((uint16_t)((uint32_t)(0xF3FFULL))) & ((uint16_t)((uint32_t)(v_stack_m108)))) != 0) goto loc_0099BB19;
    if (((uint16_t)((uint32_t)(v_stack_m108))) == ((uint16_t)((uint32_t)(0xC00ULL)))) goto loc_0099BB19;
    local_r15 = (uint32_t)((local_r15) | (16));
    v_stack_mF4 = (uint32_t)(local_r15);
    v_stack_p20 = (uint32_t)(local_r15);
    goto loc_0099BB3B;
loc_0099BC39:
    goto loc_0099BBC1;
loc_0099BC3E:
    Arg4 = 0;
    goto loc_0099BAED;
loc_0099BC46:
    result = wcsicmp((uint32_t)(v_stack_m100), v_rip + 1480723, *(uint8_t *)(v_rip + 0x5F0AB8), Arg4);
    if ((uint32_t)(result) != 0) goto loc_0099BB19;
    goto loc_0099BBFB;
loc_0099BC61:
    if ((uint32_t)(result) == 0) goto loc_0099B76E;
    *(uint64_t *)(v_stack_mF0) = result;
    goto loc_0099B858;
loc_0099BC76:
    goto loc_0099B85B;
loc_0099BC80:
    goto loc_0099BDB8;
loc_0099BC8A:
    goto loc_0099B85B;
loc_0099BC94:
    v_stack_m118 = (uint16_t)((uint32_t)(0x409ULL));
    if ((*(uint32_t *)(v_rip + 0x63DDF4)) == ((uint32_t)((uint32_t)(0x409ULL)))) goto loc_0099B906;
    if (((uint16_t)((uint32_t)(0x409ULL))) == (*(uint16_t *)(v_rip + 0x63DDAE))) goto loc_0099B906;
    if (((uint16_t)((uint32_t)(0x409ULL))) == (*(uint16_t *)(v_rip + 0x63DDB0))) goto loc_0099B906;
    if (0 == 0) goto loc_0099B63A;
    v_stack_m50 = (uint32_t)(0x409ULL);
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_r15)));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (sign_flag) goto loc_0099B63A;
    goto loc_0099BDCC;
loc_0099BD0D:
    v_stack_m118 = (uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63DD85)));
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63DD85)))) == (*(uint16_t *)(v_rip + 0x63DD3D))) goto loc_0099B906;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63DD85)))) == (*(uint16_t *)(v_rip + 0x63DD40))) goto loc_0099B906;
    if (0 == 0) goto loc_0099B63A;
    v_stack_m50 = (uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63DD85)));
    v_stack_m128 = v_stack_mF0;
    result = LdrpLoadResourceFromAlternativeModule(v_stack_mE0, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_r15)));
    v_stack_m110 = (uint32_t)(result);
    local_r10 = 0;
    if (sign_flag) goto loc_0099B63A;
    goto loc_0099BDCC;
loc_0099BD7D:
    goto loc_0099B7CE;
loc_0099BD88:
    v_stack_m88 = local_r15 - 8;
    if (0 == 0) goto loc_0099BDA4;
    v_stack_mFC = (uint16_t)(local_r12);
    goto loc_0099B83F;
loc_0099BDA4:
    v_stack_mFC = (uint16_t)(local_r12 - 1);
    goto loc_0099B843;
loc_0099BDB3:
loc_0099BDB8:
    v_stack_m110 = (uint32_t)((uint32_t)(0xC0000204ULL));
    goto loc_0099B86A;
loc_0099BDC1:
    goto loc_0099BDCC;
loc_0099BDCC:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m60, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_r15)));
    local_rsp = (local_rsp) + (272);
    return result;
loc_0099BDF0:
    if (((uint32_t)(local_r12)) == 4) goto loc_0099B36B;
loc_0099BDFA:
    goto loc_0099BDCC;
loc_0099BE01:
    if ((uint32_t)((uint32_t)(0xC00000F1ULL)) != 0) goto loc_0099B375;
    goto loc_0099BDFA;
loc_0099BE0B:
    if ((((uint8_t)(local_r15)) & (2)) == 0) goto loc_0099BDFA;
    goto loc_0099B355;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x1` | `64` | `R` |
| `Arg2` | `- 0x1` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `16` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg5` | `- 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099B2DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
