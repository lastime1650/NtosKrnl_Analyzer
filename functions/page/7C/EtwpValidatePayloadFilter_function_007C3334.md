# EtwpValidatePayloadFilter

- RVA: `0x007C3334`–`0x007C3824` (길이 `1,264` bytes)
- VA: `0x00000001407C3334`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4000`
- 디코드: `328`개 명령, `1,264/1,264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpAllocatePayloadFilterData](EtwpAllocatePayloadFilterData_function_007C30F4.md) at `0x007C3125`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C3334  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007C3339  55                              push rbp
007C333A  56                              push rsi
007C333B  57                              push rdi
007C333C  41 54                           push r12
007C333E  41 55                           push r13
007C3340  41 56                           push r14
007C3342  41 57                           push r15
007C3344  48 83 EC 60                     sub rsp, 0x60
007C3348  4C 8B CA                        mov r9, rdx
007C334B  4C 8B D1                        mov r10, rcx
007C334E  41 83 F8 50                     cmp r8d, 0x50
007C3352  0F 82 AE 04 00 00               jb 0x1407c3806
007C3358  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
007C335C  41 3B C0                        cmp eax, r8d
007C335F  0F 85 A1 04 00 00               jne 0x1407c3806
007C3365  41 BB 00 10 00 00               mov r11d, 0x1000
007C336B  45 3B C3                        cmp r8d, r11d
007C336E  0F 87 92 04 00 00               ja 0x1407c3806
007C3374  0F B7 12                        movzx edx, word ptr [rdx]
007C3377  41 8D 4B FF                     lea ecx, [r11 - 1]
007C337B  0F B7 C2                        movzx eax, dx
007C337E  66 23 C1                        and ax, cx
007C3381  B9 66 0A 00 00                  mov ecx, 0xa66
007C3386  66 3B C1                        cmp ax, cx
007C3389  0F 85 77 04 00 00               jne 0x1407c3806
007C338F  B8 00 F0 00 00                  mov eax, 0xf000
007C3394  66 23 D0                        and dx, ax
007C3397  66 41 3B D3                     cmp dx, r11w
007C339B  0F 85 65 04 00 00               jne 0x1407c3806
007C33A1  41 0F B7 51 04                  movzx edx, word ptr [r9 + 4]
007C33A6  B8 AA 00 00 00                  mov eax, 0xaa
007C33AB  66 3B D0                        cmp dx, ax
007C33AE  0F 87 52 04 00 00               ja 0x1407c3806
007C33B4  45 33 ED                        xor r13d, r13d
007C33B7  66 45 39 69 06                  cmp word ptr [r9 + 6], r13w
007C33BC  0F 85 44 04 00 00               jne 0x1407c3806
007C33C2  49 8B 0A                        mov rcx, qword ptr [r10]
007C33C5  49 2B 49 10                     sub rcx, qword ptr [r9 + 0x10]
007C33C9  75 08                           jne 0x1407c33d3
007C33CB  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
007C33CF  49 2B 49 18                     sub rcx, qword ptr [r9 + 0x18]
007C33D3  48 85 C9                        test rcx, rcx
007C33D6  0F 85 2A 04 00 00               jne 0x1407c3806
007C33DC  45 0F B7 51 20                  movzx r10d, word ptr [r9 + 0x20]
007C33E1  8D 04 52                        lea eax, [rdx + rdx*2]
007C33E4  8D 04 C5 38 00 00 00            lea eax, [rax*8 + 0x38]
007C33EB  89 54 24 08                     mov dword ptr [rsp + 8], edx
007C33EF  44 8B F2                        mov r14d, edx
007C33F2  44 3B D0                        cmp r10d, eax
007C33F5  0F 85 0B 04 00 00               jne 0x1407c3806
007C33FB  41 0F B7 79 22                  movzx edi, word ptr [r9 + 0x22]
007C3400  45 0F B7 59 24                  movzx r11d, word ptr [r9 + 0x24]
007C3405  03 C7                           add eax, edi
007C3407  44 3B D8                        cmp r11d, eax
007C340A  0F 85 F6 03 00 00               jne 0x1407c3806
007C3410  41 0F B7 71 26                  movzx esi, word ptr [r9 + 0x26]
007C3415  41 0F B7 59 28                  movzx ebx, word ptr [r9 + 0x28]
007C341A  03 C6                           add eax, esi
007C341C  3B D8                           cmp ebx, eax
007C341E  0F 85 E2 03 00 00               jne 0x1407c3806
007C3424  45 0F B7 79 2C                  movzx r15d, word ptr [r9 + 0x2c]
007C3429  41 0F B7 69 2A                  movzx ebp, word ptr [r9 + 0x2a]
007C342E  03 C5                           add eax, ebp
007C3430  44 89 7C 24 04                  mov dword ptr [rsp + 4], r15d
007C3435  44 3B F8                        cmp r15d, eax
007C3438  0F 85 C8 03 00 00               jne 0x1407c3806
007C343E  45 0F B7 61 2E                  movzx r12d, word ptr [r9 + 0x2e]
007C3443  41 0F B7 49 30                  movzx ecx, word ptr [r9 + 0x30]
007C3448  41 03 C4                        add eax, r12d
007C344B  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
007C3450  89 4C 24 0C                     mov dword ptr [rsp + 0xc], ecx
007C3454  3B C8                           cmp ecx, eax
007C3456  0F 85 AA 03 00 00               jne 0x1407c3806
007C345C  41 0F B7 49 32                  movzx ecx, word ptr [r9 + 0x32]
007C3461  03 C1                           add eax, ecx
007C3463  89 4C 24 18                     mov dword ptr [rsp + 0x18], ecx
007C3467  44 3B C0                        cmp r8d, eax
007C346A  0F 85 96 03 00 00               jne 0x1407c3806
007C3470  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
007C347A  48 F7 E7                        mul rdi
007C347D  48 C1 EA 03                     shr rdx, 3
007C3481  48 8D 04 52                     lea rax, [rdx + rdx*2]
007C3485  48 C1 E0 02                     shl rax, 2
007C3489  48 3B F8                        cmp rdi, rax
007C348C  0F 85 74 03 00 00               jne 0x1407c3806
007C3492  B8 03 00 00 00                  mov eax, 3
007C3497  40 84 F0                        test al, sil
007C349A  0F 85 66 03 00 00               jne 0x1407c3806
007C34A0  40 84 E8                        test al, bpl
007C34A3  0F 85 5D 03 00 00               jne 0x1407c3806
007C34A9  41 F6 C4 01                     test r12b, 1
007C34AD  0F 85 53 03 00 00               jne 0x1407c3806
007C34B3  44 84 D0                        test al, r10b
007C34B6  0F 85 4A 03 00 00               jne 0x1407c3806
007C34BC  44 84 D8                        test al, r11b
007C34BF  0F 85 41 03 00 00               jne 0x1407c3806
007C34C5  84 D8                           test al, bl
007C34C7  0F 85 39 03 00 00               jne 0x1407c3806
007C34CD  44 84 F8                        test al, r15b
007C34D0  0F 85 30 03 00 00               jne 0x1407c3806
007C34D6  33 C0                           xor eax, eax
007C34D8  C1 EE 02                        shr esi, 2
007C34DB  8B C8                           mov ecx, eax
007C34DD  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
007C34E4  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
007C34EB  4D 8D 79 38                     lea r15, [r9 + 0x38]
007C34EF  44 8B C0                        mov r8d, eax
007C34F2  C1 ED 02                        shr ebp, 2
007C34F5  B8 AB AA AA AA                  mov eax, 0xaaaaaaab
007C34FA  44 89 2C 24                     mov dword ptr [rsp], r13d
007C34FE  F7 E7                           mul edi
007C3500  0F B7 44 24 04                  movzx eax, word ptr [rsp + 4]
007C3505  4B 8D 3C 11                     lea rdi, [r9 + r10]
007C3509  49 03 C1                        add rax, r9
007C350C  C1 EA 03                        shr edx, 3
007C350F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007C3514  0F B7 44 24 0C                  movzx eax, word ptr [rsp + 0xc]
007C3519  49 03 C1                        add rax, r9
007C351C  89 54 24 1C                     mov dword ptr [rsp + 0x1c], edx
007C3520  41 8B D4                        mov edx, r12d
007C3523  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007C3528  D1 EA                           shr edx, 1
007C352A  4F 8D 24 19                     lea r12, [r9 + r11]
007C352E  4D 8D 1C 19                     lea r11, [r9 + rbx]
007C3532  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
007C3536  33 DB                           xor ebx, ebx
007C3538  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
007C353D  44 8B D3                        mov r10d, ebx
007C3540  8B C3                           mov eax, ebx
007C3542  89 44 24 14                     mov dword ptr [rsp + 0x14], eax
007C3546  3B 44 24 1C                     cmp eax, dword ptr [rsp + 0x1c]
007C354A  0F 83 83 02 00 00               jae 0x1407c37d3
007C3550  0F B7 0F                        movzx ecx, word ptr [rdi]
007C3553  B8 05 41 10 04                  mov eax, 0x4104105
007C3558  F7 E1                           mul ecx
007C355A  8B C1                           mov eax, ecx
007C355C  2B C2                           sub eax, edx
007C355E  D1 E8                           shr eax, 1
007C3560  03 C2                           add eax, edx
007C3562  C1 E8 05                        shr eax, 5
007C3565  6B C0 3F                        imul eax, eax, 0x3f
007C3568  2B C8                           sub ecx, eax
007C356A  48 63 C1                        movsxd rax, ecx
007C356D  49 0F AB C2                     bts r10, rax
007C3571  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
007C3575  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
007C357A  41 3B C5                        cmp eax, r13d
007C357D  0F 85 83 02 00 00               jne 0x1407c3806
007C3583  0F B7 57 06                     movzx edx, word ptr [rdi + 6]
007C3587  8B C6                           mov eax, esi
007C3589  41 2B C5                        sub eax, r13d
007C358C  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
007C3590  3B D0                           cmp edx, eax
007C3592  0F 87 6E 02 00 00               ja 0x1407c3806
007C3598  44 03 EA                        add r13d, edx
007C359B  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
007C35A0  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
007C35A5  8B CB                           mov ecx, ebx
007C35A7  3B CA                           cmp ecx, edx
007C35A9  73 37                           jae 0x1407c35e2
007C35AB  66 41 83 7C 24 02 40            cmp word ptr [r12 + 2], 0x40
007C35B2  0F 83 4E 02 00 00               jae 0x1407c3806
007C35B8  41 80 7C 24 01 40               cmp byte ptr [r12 + 1], 0x40
007C35BE  0F 83 42 02 00 00               jae 0x1407c3806
007C35C4  41 8A 04 24                     mov al, byte ptr [r12]
007C35C8  3C 40                           cmp al, 0x40
007C35CA  0F 83 36 02 00 00               jae 0x1407c3806
007C35D0  24 0F                           and al, 0xf
007C35D2  3C 09                           cmp al, 9
007C35D4  0F 83 2C 02 00 00               jae 0x1407c3806
007C35DA  FF C1                           inc ecx
007C35DC  49 83 C4 04                     add r12, 4
007C35E0  EB C5                           jmp 0x1407c35a7
007C35E2  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
007C35E6  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
007C35ED  3B C1                           cmp eax, ecx
007C35EF  0F 85 11 02 00 00               jne 0x1407c3806
007C35F5  44 0F B7 6F 0A                  movzx r13d, word ptr [rdi + 0xa]
007C35FA  8B C5                           mov eax, ebp
007C35FC  2B C1                           sub eax, ecx
007C35FE  44 3B E8                        cmp r13d, eax
007C3601  0F 87 FF 01 00 00               ja 0x1407c3806
007C3607  41 03 CD                        add ecx, r13d
007C360A  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
007C3611  41 3B DD                        cmp ebx, r13d
007C3614  0F 83 97 01 00 00               jae 0x1407c37b1
007C361A  45 0F B7 13                     movzx r10d, word ptr [r11]
007C361E  B9 FC 00 00 00                  mov ecx, 0xfc
007C3623  41 0F B7 C2                     movzx eax, r10w
007C3627  66 23 C1                        and ax, cx
007C362A  66 83 F8 20                     cmp ax, 0x20
007C362E  0F 87 D2 01 00 00               ja 0x1407c3806
007C3634  41 0F B7 43 02                  movzx eax, word ptr [r11 + 2]
007C3639  8B 0C 24                        mov ecx, dword ptr [rsp]
007C363C  3B C1                           cmp eax, ecx
007C363E  0F 85 C2 01 00 00               jne 0x1407c3806
007C3644  41 C1 EA 02                     shr r10d, 2
007C3648  41 8B C6                        mov eax, r14d
007C364B  41 83 E2 3F                     and r10d, 0x3f
007C364F  2B C1                           sub eax, ecx
007C3651  44 3B D0                        cmp r10d, eax
007C3654  0F 87 AC 01 00 00               ja 0x1407c3806
007C365A  41 03 CA                        add ecx, r10d
007C365D  33 C0                           xor eax, eax
007C365F  89 0C 24                        mov dword ptr [rsp], ecx
007C3662  44 8B D8                        mov r11d, eax
007C3665  45 3B DA                        cmp r11d, r10d
007C3668  0F 83 2E 01 00 00               jae 0x1407c379c
007C366E  41 0F B7 0F                     movzx ecx, word ptr [r15]
007C3672  3B CE                           cmp ecx, esi
007C3674  0F 83 8C 01 00 00               jae 0x1407c3806
007C367A  66 3B CA                        cmp cx, dx
007C367D  0F 83 83 01 00 00               jae 0x1407c3806
007C3683  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
007C3687  66 3B C8                        cmp cx, ax
007C368A  0F 87 76 01 00 00               ja 0x1407c3806
007C3690  8B C1                           mov eax, ecx
007C3692  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007C3697  0F B6 0C 81                     movzx ecx, byte ptr [rcx + rax*4]
007C369B  83 E1 0F                        and ecx, 0xf
007C369E  83 E9 03                        sub ecx, 3
007C36A1  0F 84 88 00 00 00               je 0x1407c372f
007C36A7  83 F9 01                        cmp ecx, 1
007C36AA  0F 85 E0 00 00 00               jne 0x1407c3790
007C36B0  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
007C36B7  49 39 47 08                     cmp qword ptr [r15 + 8], rax
007C36BB  0F 85 45 01 00 00               jne 0x1407c3806
007C36C1  33 C0                           xor eax, eax
007C36C3  49 39 47 10                     cmp qword ptr [r15 + 0x10], rax
007C36C7  0F 85 39 01 00 00               jne 0x1407c3806
007C36CD  8B 54 24 04                     mov edx, dword ptr [rsp + 4]
007C36D1  45 33 F6                        xor r14d, r14d
007C36D4  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
007C36D9  03 54 24 20                     add edx, dword ptr [rsp + 0x20]
007C36DD  48 8B C8                        mov rcx, rax
007C36E0  49 03 D1                        add rdx, r9
007C36E3  66 44 39 30                     cmp word ptr [rax], r14w
007C36E7  44 8B 74 24 08                  mov r14d, dword ptr [rsp + 8]
007C36EC  74 1B                           je 0x1407c3709
007C36EE  48 8D 42 FE                     lea rax, [rdx - 2]
007C36F2  45 33 F6                        xor r14d, r14d
007C36F5  48 3B C8                        cmp rcx, rax
007C36F8  73 0A                           jae 0x1407c3704
007C36FA  48 83 C1 02                     add rcx, 2
007C36FE  66 44 39 31                     cmp word ptr [rcx], r14w
007C3702  75 F1                           jne 0x1407c36f5
007C3704  44 8B 74 24 08                  mov r14d, dword ptr [rsp + 8]
007C3709  48 83 C1 02                     add rcx, 2
007C370D  48 3B CA                        cmp rcx, rdx
007C3710  0F 87 F0 00 00 00               ja 0x1407c3806
007C3716  48 8B C1                        mov rax, rcx
007C3719  48 2B 44 24 30                  sub rax, qword ptr [rsp + 0x30]
007C371E  48 D1 F8                        sar rax, 1
007C3721  01 84 24 B0 00 00 00            add dword ptr [rsp + 0xb0], eax
007C3728  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
007C372D  EB 5D                           jmp 0x1407c378c
007C372F  41 8B C0                        mov eax, r8d
007C3732  49 39 47 08                     cmp qword ptr [r15 + 8], rax
007C3736  0F 85 CA 00 00 00               jne 0x1407c3806
007C373C  33 C0                           xor eax, eax
007C373E  49 39 47 10                     cmp qword ptr [r15 + 0x10], rax
007C3742  0F 85 BE 00 00 00               jne 0x1407c3806
007C3748  8B 54 24 18                     mov edx, dword ptr [rsp + 0x18]
007C374C  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007C3751  03 54 24 0C                     add edx, dword ptr [rsp + 0xc]
007C3755  48 8B C1                        mov rax, rcx
007C3758  49 03 D1                        add rdx, r9
007C375B  80 39 00                        cmp byte ptr [rcx], 0
007C375E  74 11                           je 0x1407c3771
007C3760  48 8D 4A FF                     lea rcx, [rdx - 1]
007C3764  48 3B C1                        cmp rax, rcx
007C3767  73 08                           jae 0x1407c3771
007C3769  48 FF C0                        inc rax
007C376C  80 38 00                        cmp byte ptr [rax], 0
007C376F  75 F3                           jne 0x1407c3764
007C3771  48 8D 48 01                     lea rcx, [rax + 1]
007C3775  48 3B CA                        cmp rcx, rdx
007C3778  0F 87 88 00 00 00               ja 0x1407c3806
007C377E  8B C1                           mov eax, ecx
007C3780  2B 44 24 38                     sub eax, dword ptr [rsp + 0x38]
007C3784  44 03 C0                        add r8d, eax
007C3787  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
007C378C  8B 54 24 10                     mov edx, dword ptr [rsp + 0x10]
007C3790  41 FF C3                        inc r11d
007C3793  49 83 C7 18                     add r15, 0x18
007C3797  E9 C9 FE FF FF                  jmp 0x1407c3665
007C379C  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
007C37A1  FF C3                           inc ebx
007C37A3  49 83 C3 04                     add r11, 4
007C37A7  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
007C37AC  E9 60 FE FF FF                  jmp 0x1407c3611
007C37B1  8B 44 24 14                     mov eax, dword ptr [rsp + 0x14]
007C37B5  48 83 C7 0C                     add rdi, 0xc
007C37B9  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
007C37C0  FF C0                           inc eax
007C37C2  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
007C37C7  33 DB                           xor ebx, ebx
007C37C9  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
007C37CE  E9 6F FD FF FF                  jmp 0x1407c3542
007C37D3  4D 3B 51 08                     cmp r10, qword ptr [r9 + 8]
007C37D7  75 2D                           jne 0x1407c3806
007C37D9  44 39 34 24                     cmp dword ptr [rsp], r14d
007C37DD  75 27                           jne 0x1407c3806
007C37DF  44 3B EE                        cmp r13d, esi
007C37E2  75 22                           jne 0x1407c3806
007C37E4  3B CD                           cmp ecx, ebp
007C37E6  75 1E                           jne 0x1407c3806
007C37E8  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
007C37EC  39 84 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], eax
007C37F3  75 11                           jne 0x1407c3806
007C37F5  44 2B 44 24 18                  sub r8d, dword ptr [rsp + 0x18]
007C37FA  41 F7 D8                        neg r8d
007C37FD  1B C0                           sbb eax, eax
007C37FF  25 0D 00 00 C0                  and eax, 0xc000000d
007C3804  EB 05                           jmp 0x1407c380b
007C3806  B8 0D 00 00 C0                  mov eax, 0xc000000d
007C380B  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
007C3813  48 83 C4 60                     add rsp, 0x60
007C3817  41 5F                           pop r15
007C3819  41 5E                           pop r14
007C381B  41 5D                           pop r13
007C381D  41 5C                           pop r12
007C381F  5F                              pop rdi
007C3820  5E                              pop rsi
007C3821  5D                              pop rbp
007C3822  C3                              ret
007C3823  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpValidatePayloadFilter(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    if (a3 < 80) goto loc_007C3806;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 2))) != a3) goto loc_007C3806;
    if (a3 > ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_007C3806;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) & ((unsigned __int16)((unsigned int)(0x1000ULL) - 1)));
    if (((unsigned __int16)(result)) != ((unsigned __int16)((unsigned int)(0xA66ULL)))) goto loc_007C3806;
    a2 = (unsigned __int16)((*(unsigned __int16 *)(a2)) & ((unsigned __int16)((unsigned int)(0xF000ULL))));
    if (((unsigned __int16)(a2)) != ((unsigned __int16)((unsigned int)(0x1000ULL)))) goto loc_007C3806;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 4))) > 170) goto loc_007C3806;
    v_r13 = 0;
    if ((*(unsigned __int16 *)(a2 + 6)) != 0) goto loc_007C3806;
    a1 = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(a2 + 16));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a2 + 24));
    }
    if (a1 != 0) goto loc_007C3806;
    v_stack_m90 = (unsigned int)(*(unsigned __int16 *)(a2 + 4));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 32))) != ((unsigned int)(*(unsigned __int16 *)(a2 + 4) + *(unsigned __int16 *)(a2 + 4) * 2 * 8 + 56))) goto loc_007C3806;
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 4) + *(unsigned __int16 *)(a2 + 4) * 2 * 8 + 56) + ((unsigned int)(*(unsigned __int16 *)(a2 + 34))));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 36))) != ((unsigned int)(result))) goto loc_007C3806;
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(a2 + 38))));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 40))) != ((unsigned int)(result))) goto loc_007C3806;
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(a2 + 42))));
    v_stack_m94 = (unsigned int)(*(unsigned __int16 *)(a2 + 44));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 44))) != ((unsigned int)(result))) goto loc_007C3806;
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(a2 + 46))));
    v_stack_m78 = (unsigned int)(*(unsigned __int16 *)(a2 + 46));
    v_stack_m8C = (unsigned int)(*(unsigned __int16 *)(a2 + 48));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 48))) != ((unsigned int)(result))) goto loc_007C3806;
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(a2 + 50))));
    v_stack_m80 = (unsigned int)(*(unsigned __int16 *)(a2 + 50));
    if (a3 != ((unsigned int)(result))) goto loc_007C3806;
    a2 = (*(unsigned __int16 *)(a2 + 4)) >> (3);
    result = (a2 + a2 * 2) << (2);
    if ((*(unsigned __int16 *)(a2 + 34)) != result) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 38)))) != 0) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 42)))) != 0) goto loc_007C3806;
    if ((((unsigned __int8)(*(unsigned __int16 *)(a2 + 46))) & (1)) != 0) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 32)))) != 0) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 36)))) != 0) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 40)))) != 0) goto loc_007C3806;
    if (((3) & ((unsigned __int8)(*(unsigned __int16 *)(a2 + 44)))) != 0) goto loc_007C3806;
    result = 0;
    v_rsi = (unsigned int)((*(unsigned __int16 *)(a2 + 38)) >> (2));
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    v_rbp = (unsigned int)((*(unsigned __int16 *)(a2 + 42)) >> (2));
    v_stack_m98 = 0;
    result = (v_stack_m94) + (a2);
    a2 = (unsigned int)((a2) >> (3));
    v_stack_m68 = result;
    result = (v_stack_m8C) + (a2);
    v_stack_m7C = (unsigned int)(a2);
    v_stack_m60 = result;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2 + 46)))) >> (1));
    v_stack_m70 = (unsigned int)(a2);
    v_rbx = 0;
    v_stack_m58 = a2 + *(unsigned __int16 *)(a2 + 40) * 1;
loc_007C3542:
    v_stack_m84 = 0;
    if (0 >= v_stack_m7C) goto loc_007C37D3;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1)))) - ((unsigned int)(a2)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    result = (unsigned int)((result) >> (5));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1)) - ((unsigned int)(result)));
    v_stack_m48 = 0;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 4))) != 0) goto loc_007C3806;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (0));
    v_stack_m88 = (unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 6));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 6))) > ((unsigned int)(result))) goto loc_007C3806;
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 6))));
    v_stack_m50 = a2 + *(unsigned __int16 *)(a2 + 36) * 1;
    v_stack_m74 = (unsigned int)(v_r13);
loc_007C35A7:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 6)))) goto loc_007C35E2;
    if ((*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 36) * 1 + 2)) >= 64) goto loc_007C3806;
    if ((*(unsigned __int8 *)(a2 + *(unsigned __int16 *)(a2 + 36) * 1 + 1)) >= 64) goto loc_007C3806;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int16 *)(a2 + 36) * 1))) >= 64) goto loc_007C3806;
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + *(unsigned __int16 *)(a2 + 36) * 1)) & (15));
    if (((unsigned __int8)(result)) >= 9) goto loc_007C3806;
    a1 = (unsigned int)((0) + 1);
    v_r12 = (a2 + *(unsigned __int16 *)(a2 + 36) * 1) + (4);
    goto loc_007C35A7;
loc_007C35E2:
    if (((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 8))) != ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_007C3806;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) - ((unsigned int)((unsigned int)(v_stack_p20))));
    if (((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 10))) > ((unsigned int)(result))) goto loc_007C3806;
    a1 = (unsigned int)(((unsigned int)(v_stack_p20)) + ((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 10))));
    v_stack_p20 = (unsigned int)(a1);
loc_007C3611:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 10)))) goto loc_007C37B1;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 40) * 1))) & (252));
    if (((unsigned __int16)(result)) > 32) goto loc_007C3806;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 40) * 1 + 2))) != ((unsigned int)((unsigned int)(v_stack_m98)))) goto loc_007C3806;
    v_r10 = (unsigned int)((*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 40) * 1)) >> (2));
    v_r10 = (unsigned int)((v_r10) & (63));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2 + 4)))))) - ((unsigned int)((unsigned int)(v_stack_m98))));
    if (((unsigned int)(v_r10)) > ((unsigned int)(result))) goto loc_007C3806;
    a1 = (unsigned int)(((unsigned int)(v_stack_m98)) + ((unsigned int)(v_r10)));
    result = 0;
    v_stack_m98 = (unsigned int)(a1);
loc_007C3665:
    if (0 >= ((unsigned int)(v_r10))) goto loc_007C379C;
    if (((unsigned int)(*(unsigned __int16 *)(a2 + 56))) >= ((unsigned int)(v_rsi))) goto loc_007C3806;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 56))) >= ((unsigned __int16)(*(unsigned __int16 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 6)))) goto loc_007C3806;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 56))) > ((unsigned __int16)(*(unsigned __int8 *)(a2 + *(unsigned __int16 *)(a2 + 32) * 1 + 3)))) goto loc_007C3806;
    a1 = (unsigned int)((*(unsigned __int8 *)(v_stack_m50 + (unsigned int)((unsigned int)(*(unsigned __int16 *)(a2 + 56))) * 4)) & (15));
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_007C372F;
    if (((unsigned int)(a1)) != 1) goto loc_007C3790;
    if ((*(unsigned __int64 *)(a2 + 56 + 8)) != ((unsigned int)(v_stack_p18))) goto loc_007C3806;
    result = 0;
    if ((*(unsigned __int64 *)(a2 + 56 + 16)) != 0) goto loc_007C3806;
    v_r14 = 0;
    a2 = (unsigned int)(((unsigned int)(v_stack_m94)) + (v_stack_m78));
    a2 = (a2) + (a2);
    if ((*(unsigned __int16 *)(v_stack_m68)) == 0) goto loc_007C3709;
    v_r14 = 0;
loc_007C36F5:
    if (v_stack_m68 >= (a2 - 2)) goto loc_007C3704;
    a1 = (v_stack_m68) + (2);
    if ((*(unsigned __int16 *)(a1)) != 0) goto loc_007C36F5;
loc_007C3704:
loc_007C3709:
    a1 = (a1) + (2);
    if (a1 > a2) goto loc_007C3806;
    result = (a1) - (v_stack_m68);
    result = (result) >> (1);
    v_stack_m68 = a1;
    goto loc_007C378C;
loc_007C372F:
    if ((*(unsigned __int64 *)(a2 + 56 + 8)) != 0) goto loc_007C3806;
    result = 0;
    if ((*(unsigned __int64 *)(a2 + 56 + 16)) != 0) goto loc_007C3806;
    a2 = (unsigned int)(((unsigned int)(v_stack_m80)) + (v_stack_m8C));
    a2 = (a2) + (a2);
    if ((*(unsigned __int8 *)(v_stack_m60)) == 0) goto loc_007C3771;
loc_007C3764:
    if (v_stack_m60 >= (a2 - 1)) goto loc_007C3771;
    result = (v_stack_m60) + 1;
    if ((*(unsigned __int8 *)(result)) != 0) goto loc_007C3764;
loc_007C3771:
    if ((result + 1) > a2) goto loc_007C3806;
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) - (v_stack_m60));
    a3 = (unsigned int)((0) + ((unsigned int)(result)));
    v_stack_m60 = result + 1;
loc_007C378C:
loc_007C3790:
    v_r11 = (unsigned int)((0) + 1);
    v_r15 = (a2 + 56) + (24);
    goto loc_007C3665;
loc_007C379C:
    v_rbx = (unsigned int)((v_rbx) + 1);
    v_r11 = (v_stack_m58) + (4);
    v_stack_m58 = v_r11;
    goto loc_007C3611;
loc_007C37B1:
    v_rdi = (a2 + *(unsigned __int16 *)(a2 + 32) * 1) + (12);
    result = (unsigned int)(((unsigned int)(v_stack_m84)) + 1);
    v_rbx = 0;
    goto loc_007C3542;
loc_007C37D3:
    if (v_stack_m48 != (*(unsigned __int64 *)(a2 + 8))) goto loc_007C3806;
    if (v_stack_m98 != ((unsigned int)((unsigned int)(v_stack_m90)))) goto loc_007C3806;
    if (((unsigned int)((unsigned int)(v_stack_m74))) != ((unsigned int)(v_rsi))) goto loc_007C3806;
    if (((unsigned int)((unsigned int)(v_stack_p20))) != ((unsigned int)(v_rbp))) goto loc_007C3806;
    if (v_stack_p18 != ((unsigned int)((unsigned int)(v_stack_m70)))) goto loc_007C3806;
    a3 = (unsigned int)((a3) - (v_stack_m80));
    a3 = (unsigned int)(-(a3));
    result = (unsigned int)(((unsigned int)(v_stack_m70)) & (0xC000000DULL));
    goto loc_007C380B;
loc_007C3806:
loc_007C380B:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t EtwpValidatePayloadFilter(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    if (Arg3 < 80) goto loc_007C3806;
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x2))) != Arg3) goto loc_007C3806;
    if (Arg3 > ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_007C3806;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2))) & ((uint16_t)((uint32_t)(0x1000ULL) - 1)));
    if (((uint16_t)(result)) != ((uint16_t)((uint32_t)(0xA66ULL)))) goto loc_007C3806;
    Arg2 = (uint16_t)((*(uint16_t *)(arg2)) & ((uint16_t)((uint32_t)(0xF000ULL))));
    if (((uint16_t)(Arg2)) != ((uint16_t)((uint32_t)(0x1000ULL)))) goto loc_007C3806;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x4))) > 170) goto loc_007C3806;
    local_r13 = 0;
    if ((*(uint16_t *)(arg2 + 0x6)) != 0) goto loc_007C3806;
    Arg1 = (*(uint64_t *)(arg1)) - (*(uint64_t *)(arg2 + 0x10));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg2 + 0x18));
    }
    if (Arg1 != NULL) goto loc_007C3806;
    v_stack_m90 = (uint32_t)(*(uint16_t *)(arg2 + 0x4));
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x20))) != ((uint32_t)(*(uint16_t *)(arg2 + 0x4) + *(uint16_t *)(arg2 + 0x4) * 2 * 8 + 56))) goto loc_007C3806;
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x4) + *(uint16_t *)(arg2 + 0x4) * 2 * 8 + 56) + ((uint32_t)(*(uint16_t *)(arg2 + 0x22))));
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x24))) != ((uint32_t)(result))) goto loc_007C3806;
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(arg2 + 0x26))));
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x28))) != ((uint32_t)(result))) goto loc_007C3806;
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(arg2 + 0x2A))));
    v_stack_m94 = (uint32_t)(*(uint16_t *)(arg2 + 0x2C));
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x2C))) != ((uint32_t)(result))) goto loc_007C3806;
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(arg2 + 0x2E))));
    v_stack_m78 = (uint32_t)(*(uint16_t *)(arg2 + 0x2E));
    v_stack_m8C = (uint32_t)(*(uint16_t *)(arg2 + 0x30));
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x30))) != ((uint32_t)(result))) goto loc_007C3806;
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(arg2 + 0x32))));
    v_stack_m80 = (uint32_t)(*(uint16_t *)(arg2 + 0x32));
    if (Arg3 != ((uint32_t)(result))) goto loc_007C3806;
    Arg2 = (*(uint16_t *)(arg2 + 0x4)) >> (3);
    result = (Arg2 + Arg2 * 2) << (2);
    if ((*(uint16_t *)(arg2 + 0x22)) != result) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x26)))) != 0) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x2A)))) != 0) goto loc_007C3806;
    if ((((uint8_t)(*(uint16_t *)(arg2 + 0x2E))) & (1)) != 0) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x20)))) != 0) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x24)))) != 0) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x28)))) != 0) goto loc_007C3806;
    if (((3) & ((uint8_t)(*(uint16_t *)(arg2 + 0x2C)))) != 0) goto loc_007C3806;
    result = 0;
    local_rsi = (uint32_t)((*(uint16_t *)(arg2 + 0x26)) >> (2));
    v_stack_p20 = 0;
    v_stack_p18 = 0;
    local_rbp = (uint32_t)((*(uint16_t *)(arg2 + 0x2A)) >> (2));
    v_stack_m98 = 0;
    result = (v_stack_m94) + (Arg2);
    Arg2 = (uint32_t)((Arg2) >> (3));
    v_stack_m68 = result;
    result = (v_stack_m8C) + (Arg2);
    v_stack_m7C = (uint32_t)(Arg2);
    v_stack_m60 = result;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg2 + 0x2E)))) >> (1));
    v_stack_m70 = (uint32_t)(Arg2);
    local_rbx = 0;
    v_stack_m58 = Arg2 + *(uint16_t *)(arg2 + 0x28) * 1;
loc_007C3542:
    v_stack_m84 = 0;
    if (0 >= v_stack_m7C) goto loc_007C37D3;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1)))) - ((uint32_t)(Arg2)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    result = (uint32_t)((result) >> (5));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1)) - ((uint32_t)(result)));
    v_stack_m48 = 0;
    if (((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x4))) != 0) goto loc_007C3806;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (0));
    v_stack_m88 = (uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x6));
    if (((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x6))) > ((uint32_t)(result))) goto loc_007C3806;
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x6))));
    v_stack_m50 = Arg2 + *(uint16_t *)(arg2 + 0x24) * 1;
    v_stack_m74 = (uint32_t)(local_r13);
loc_007C35A7:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x6)))) goto loc_007C35E2;
    if ((*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x24) * 1 + 0x2)) >= 64) goto loc_007C3806;
    if ((*(uint8_t *)(arg2 + *(uint16_t *)(arg2 + 0x24) * 1 + 0x1)) >= 64) goto loc_007C3806;
    if (((uint8_t)(*(uint8_t *)(arg2 + *(uint16_t *)(arg2 + 0x24) * 1))) >= 64) goto loc_007C3806;
    result = (uint8_t)((*(uint8_t *)(arg2 + *(uint16_t *)(arg2 + 0x24) * 1)) & (15));
    if (((uint8_t)(result)) >= 9) goto loc_007C3806;
    Arg1 = (uint32_t)((0) + 1);
    local_r12 = (Arg2 + *(uint16_t *)(arg2 + 0x24) * 1) + (4);
    goto loc_007C35A7;
loc_007C35E2:
    if (((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x8))) != ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_007C3806;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) - ((uint32_t)((uint32_t)(v_stack_p20))));
    if (((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0xA))) > ((uint32_t)(result))) goto loc_007C3806;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p20)) + ((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0xA))));
    v_stack_p20 = (uint32_t)(Arg1);
loc_007C3611:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0xA)))) goto loc_007C37B1;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x28) * 1))) & (252));
    if (((uint16_t)(result)) > 32) goto loc_007C3806;
    if (((uint32_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x28) * 1 + 0x2))) != ((uint32_t)((uint32_t)(v_stack_m98)))) goto loc_007C3806;
    local_r10 = (uint32_t)((*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x28) * 1)) >> (2));
    local_r10 = (uint32_t)((local_r10) & (63));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(arg2 + 0x4)))))) - ((uint32_t)((uint32_t)(v_stack_m98))));
    if (((uint32_t)(local_r10)) > ((uint32_t)(result))) goto loc_007C3806;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m98)) + ((uint32_t)(local_r10)));
    result = 0;
    v_stack_m98 = (uint32_t)(Arg1);
loc_007C3665:
    if (0 >= ((uint32_t)(local_r10))) goto loc_007C379C;
    if (((uint32_t)(*(uint16_t *)(arg2 + 0x38))) >= ((uint32_t)(local_rsi))) goto loc_007C3806;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x38))) >= ((uint16_t)(*(uint16_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x6)))) goto loc_007C3806;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x38))) > ((uint16_t)(*(uint8_t *)(arg2 + *(uint16_t *)(arg2 + 0x20) * 1 + 0x3)))) goto loc_007C3806;
    Arg1 = (uint32_t)((*(uint8_t *)(v_stack_m50 + (uint32_t)((uint32_t)(*(uint16_t *)(arg2 + 0x38))) * 4)) & (15));
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_007C372F;
    if (((uint32_t)(Arg1)) != 1) goto loc_007C3790;
    if ((*(uint64_t *)(arg2 + 0x38 + 0x8)) != ((uint32_t)(v_stack_p18))) goto loc_007C3806;
    result = 0;
    if ((*(uint64_t *)(arg2 + 0x38 + 0x10)) != 0) goto loc_007C3806;
    local_r14 = 0;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m94)) + (v_stack_m78));
    Arg2 = (Arg2) + (Arg2);
    if ((*(uint16_t *)(v_stack_m68)) == 0) goto loc_007C3709;
    local_r14 = 0;
loc_007C36F5:
    if (v_stack_m68 >= (Arg2 - 2)) goto loc_007C3704;
    Arg1 = (v_stack_m68) + (2);
    if ((*(uint16_t *)(arg1)) != 0) goto loc_007C36F5;
loc_007C3704:
loc_007C3709:
    Arg1 = (Arg1) + (2);
    if (Arg1 > Arg2) goto loc_007C3806;
    result = (Arg1) - (v_stack_m68);
    result = (result) >> (1);
    v_stack_m68 = Arg1;
    goto loc_007C378C;
loc_007C372F:
    if ((*(uint64_t *)(arg2 + 0x38 + 0x8)) != 0) goto loc_007C3806;
    result = 0;
    if ((*(uint64_t *)(arg2 + 0x38 + 0x10)) != 0) goto loc_007C3806;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m80)) + (v_stack_m8C));
    Arg2 = (Arg2) + (Arg2);
    if ((*(uint8_t *)(v_stack_m60)) == 0) goto loc_007C3771;
loc_007C3764:
    if (v_stack_m60 >= (Arg2 - 1)) goto loc_007C3771;
    result = (v_stack_m60) + 1;
    if ((*(uint8_t *)(result)) != 0) goto loc_007C3764;
loc_007C3771:
    if ((result + 1) > Arg2) goto loc_007C3806;
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) - (v_stack_m60));
    Arg3 = (uint32_t)((0) + ((uint32_t)(result)));
    v_stack_m60 = result + 1;
loc_007C378C:
loc_007C3790:
    local_r11 = (uint32_t)((0) + 1);
    local_r15 = (Arg2 + 56) + (24);
    goto loc_007C3665;
loc_007C379C:
    local_rbx = (uint32_t)((local_rbx) + 1);
    local_r11 = (v_stack_m58) + (4);
    v_stack_m58 = local_r11;
    goto loc_007C3611;
loc_007C37B1:
    local_rdi = (Arg2 + *(uint16_t *)(arg2 + 0x20) * 1) + (12);
    result = (uint32_t)(((uint32_t)(v_stack_m84)) + 1);
    local_rbx = 0;
    goto loc_007C3542;
loc_007C37D3:
    if (v_stack_m48 != (*(uint64_t *)(arg2 + 0x8))) goto loc_007C3806;
    if (v_stack_m98 != ((uint32_t)((uint32_t)(v_stack_m90)))) goto loc_007C3806;
    if (((uint32_t)((uint32_t)(v_stack_m74))) != ((uint32_t)(local_rsi))) goto loc_007C3806;
    if (((uint32_t)((uint32_t)(v_stack_p20))) != ((uint32_t)(local_rbp))) goto loc_007C3806;
    if (v_stack_p18 != ((uint32_t)((uint32_t)(v_stack_m70)))) goto loc_007C3806;
    Arg3 = (uint32_t)((Arg3) - (v_stack_m80));
    Arg3 = (uint32_t)(-(Arg3));
    result = (uint32_t)(((uint32_t)(v_stack_m70)) & (0xC000000DULL));
    goto loc_007C380B;
loc_007C3806:
loc_007C380B:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0 + r10*1` | `64` | `R` |
| `Arg2` | `+ 0x0 + r11*1` | `64` | `R` |
| `Arg2` | `+ 0x0 + rbx*1` | `64` | `R` |
| `Arg2` | `+ 0x1` | `8` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x3` | `8` | `R` |
| `Arg2` | `+ 0x4` | `16` | `R` |
| `Arg2` | `+ 0x6` | `16` | `R` |
| `Arg2` | `+ 0x8` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0xA` | `16` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `16` | `R` |
| `Arg2` | `+ 0x22` | `16` | `R` |
| `Arg2` | `+ 0x24` | `16` | `R` |
| `Arg2` | `+ 0x26` | `16` | `R` |
| `Arg2` | `+ 0x28` | `16` | `R` |
| `Arg2` | `+ 0x2A` | `16` | `R` |
| `Arg2` | `+ 0x2C` | `16` | `R` |
| `Arg2` | `+ 0x2E` | `16` | `R` |
| `Arg2` | `+ 0x30` | `16` | `R` |
| `Arg2` | `+ 0x32` | `16` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C3334&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
