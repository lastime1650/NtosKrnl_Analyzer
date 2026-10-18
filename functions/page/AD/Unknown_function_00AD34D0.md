# sub_00AD34D0

- RVA: `0x00AD34D0`–`0x00AD39F9` (길이 `1,321` bytes)
- VA: `0x0000000140AD34D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C3C`
- 디코드: `399`개 명령, `1,321/1,321` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AD3655` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD3674` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AD36B6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD3783` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD3932` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD39D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A7D2`

### Static image references
- `0x00AD3680` → RVA `0x00FD83D8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00AD3655` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD3674` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AD36B6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD3783` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD3932` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD39D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD34D0  48 8B C4                        mov rax, rsp
00AD34D3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AD34D7  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00AD34DB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AD34DF  55                              push rbp
00AD34E0  56                              push rsi
00AD34E1  57                              push rdi
00AD34E2  41 54                           push r12
00AD34E4  41 55                           push r13
00AD34E6  41 56                           push r14
00AD34E8  41 57                           push r15
00AD34EA  48 83 EC 50                     sub rsp, 0x50
00AD34EE  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00AD34F2  45 33 ED                        xor r13d, r13d
00AD34F5  44 21 68 18                     and dword ptr [rax + 0x18], r13d
00AD34F9  49 8B F1                        mov rsi, r9
00AD34FC  4C 8B C9                        mov r9, rcx
00AD34FF  4D 85 C0                        test r8, r8
00AD3502  0F 84 A1 00 00 00               je 0x140ad35a9
00AD3508  83 39 03                        cmp dword ptr [rcx], 3
00AD350B  0F 86 98 00 00 00               jbe 0x140ad35a9
00AD3511  49 8B C0                        mov rax, r8
00AD3514  45 8D 5D 01                     lea r11d, [r13 + 1]
00AD3518  33 D2                           xor edx, edx
00AD351A  44 8B 10                        mov r10d, dword ptr [rax]
00AD351D  48 8D 48 04                     lea rcx, [rax + 4]
00AD3521  83 FA 03                        cmp edx, 3
00AD3524  73 1B                           jae 0x140ad3541
00AD3526  48 3B C8                        cmp rcx, rax
00AD3529  0F 82 AA 04 00 00               jb 0x140ad39d9
00AD352F  4A 8D 04 11                     lea rax, [rcx + r10]
00AD3533  48 3B C1                        cmp rax, rcx
00AD3536  0F 82 9D 04 00 00               jb 0x140ad39d9
00AD353C  41 03 D3                        add edx, r11d
00AD353F  EB D9                           jmp 0x140ad351a
00AD3541  48 3B C8                        cmp rcx, rax
00AD3544  0F 82 8F 04 00 00               jb 0x140ad39d9
00AD354A  45 33 F6                        xor r14d, r14d
00AD354D  45 85 D2                        test r10d, r10d
00AD3550  4C 0F 45 F1                     cmovne r14, rcx
00AD3554  41 83 FA 08                     cmp r10d, 8
00AD3558  0F 85 D9 00 00 00               jne 0x140ad3637
00AD355E  41 83 39 04                     cmp dword ptr [r9], 4
00AD3562  4D 8B 36                        mov r14, qword ptr [r14]
00AD3565  76 42                           jbe 0x140ad35a9
00AD3567  49 8B C0                        mov rax, r8
00AD356A  33 D2                           xor edx, edx
00AD356C  8B 18                           mov ebx, dword ptr [rax]
00AD356E  48 8D 48 04                     lea rcx, [rax + 4]
00AD3572  83 FA 04                        cmp edx, 4
00AD3575  73 1B                           jae 0x140ad3592
00AD3577  48 3B C8                        cmp rcx, rax
00AD357A  0F 82 59 04 00 00               jb 0x140ad39d9
00AD3580  48 8D 04 19                     lea rax, [rcx + rbx]
00AD3584  48 3B C1                        cmp rax, rcx
00AD3587  0F 82 4C 04 00 00               jb 0x140ad39d9
00AD358D  41 03 D3                        add edx, r11d
00AD3590  EB DA                           jmp 0x140ad356c
00AD3592  48 3B C8                        cmp rcx, rax
00AD3595  0F 82 3E 04 00 00               jb 0x140ad39d9
00AD359B  33 FF                           xor edi, edi
00AD359D  85 DB                           test ebx, ebx
00AD359F  48 0F 45 F9                     cmovne rdi, rcx
00AD35A3  41 83 39 05                     cmp dword ptr [r9], 5
00AD35A7  77 0A                           ja 0x140ad35b3
00AD35A9  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD35AE  E9 2B 04 00 00                  jmp 0x140ad39de
00AD35B3  49 8B C0                        mov rax, r8
00AD35B6  33 D2                           xor edx, edx
00AD35B8  44 8B 20                        mov r12d, dword ptr [rax]
00AD35BB  48 8D 48 04                     lea rcx, [rax + 4]
00AD35BF  83 FA 05                        cmp edx, 5
00AD35C2  73 1B                           jae 0x140ad35df
00AD35C4  48 3B C8                        cmp rcx, rax
00AD35C7  0F 82 0C 04 00 00               jb 0x140ad39d9
00AD35CD  4A 8D 04 21                     lea rax, [rcx + r12]
00AD35D1  48 3B C1                        cmp rax, rcx
00AD35D4  0F 82 FF 03 00 00               jb 0x140ad39d9
00AD35DA  41 03 D3                        add edx, r11d
00AD35DD  EB D9                           jmp 0x140ad35b8
00AD35DF  48 3B C8                        cmp rcx, rax
00AD35E2  0F 82 F1 03 00 00               jb 0x140ad39d9
00AD35E8  45 33 FF                        xor r15d, r15d
00AD35EB  45 85 E4                        test r12d, r12d
00AD35EE  4C 0F 45 F9                     cmovne r15, rcx
00AD35F2  41 83 39 06                     cmp dword ptr [r9], 6
00AD35F6  76 B1                           jbe 0x140ad35a9
00AD35F8  33 D2                           xor edx, edx
00AD35FA  41 8B 00                        mov eax, dword ptr [r8]
00AD35FD  49 8D 48 04                     lea rcx, [r8 + 4]
00AD3601  83 FA 06                        cmp edx, 6
00AD3604  73 1B                           jae 0x140ad3621
00AD3606  49 3B C8                        cmp rcx, r8
00AD3609  0F 82 CA 03 00 00               jb 0x140ad39d9
00AD360F  4C 8D 04 01                     lea r8, [rcx + rax]
00AD3613  4C 3B C1                        cmp r8, rcx
00AD3616  0F 82 BD 03 00 00               jb 0x140ad39d9
00AD361C  41 03 D3                        add edx, r11d
00AD361F  EB D9                           jmp 0x140ad35fa
00AD3621  49 3B C8                        cmp rcx, r8
00AD3624  0F 82 AF 03 00 00               jb 0x140ad39d9
00AD362A  33 ED                           xor ebp, ebp
00AD362C  85 C0                           test eax, eax
00AD362E  48 0F 45 E9                     cmovne rbp, rcx
00AD3632  83 F8 04                        cmp eax, 4
00AD3635  74 0A                           je 0x140ad3641
00AD3637  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD363C  E9 9D 03 00 00                  jmp 0x140ad39de
00AD3641  8B 6D 00                        mov ebp, dword ptr [rbp]
00AD3644  85 ED                           test ebp, ebp
00AD3646  74 35                           je 0x140ad367d
00AD3648  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD364E  8B D5                           mov edx, ebp
00AD3650  B9 00 01 00 00                  mov ecx, 0x100
00AD3655  E8 96 EA 0A 00                  call 0x140b820f0
00AD365A  48 85 C0                        test rax, rax
00AD365D  75 0A                           jne 0x140ad3669
00AD365F  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD3664  E9 75 03 00 00                  jmp 0x140ad39de
00AD3669  4C 8B C5                        mov r8, rbp
00AD366C  33 D2                           xor edx, edx
00AD366E  48 8B C8                        mov rcx, rax
00AD3671  4C 8B E8                        mov r13, rax
00AD3674  E8 C7 35 BF FF                  call 0x1406c6c40
00AD3679  33 C9                           xor ecx, ecx
00AD367B  EB 03                           jmp 0x140ad3680
00AD367D  41 8B CB                        mov ecx, r11d
00AD3680  48 8B 05 51 4D 50 00            mov rax, qword ptr [rip + 0x504d51]
00AD3687  48 85 C0                        test rax, rax
00AD368A  74 34                           je 0x140ad36c0
00AD368C  45 33 C0                        xor r8d, r8d
00AD368F  45 8B CC                        mov r9d, r12d
00AD3692  85 C9                           test ecx, ecx
00AD3694  8B D3                           mov edx, ebx
00AD3696  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AD369E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AD36A3  4D 0F 44 C5                     cmove r8, r13
00AD36A7  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
00AD36AB  48 8B CF                        mov rcx, rdi
00AD36AE  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00AD36B3  4D 8B C7                        mov r8, r15
00AD36B6  E8 15 74 BE FF                  call 0x1406baad0
00AD36BB  44 8B F8                        mov r15d, eax
00AD36BE  EB 06                           jmp 0x140ad36c6
00AD36C0  41 BF BB 00 00 C0               mov r15d, 0xc00000bb
00AD36C6  8D 45 04                        lea eax, [rbp + 4]
00AD36C9  83 F8 04                        cmp eax, 4
00AD36CC  0F 82 F1 02 00 00               jb 0x140ad39c3
00AD36D2  83 C0 14                        add eax, 0x14
00AD36D5  83 F8 14                        cmp eax, 0x14
00AD36D8  0F 82 E5 02 00 00               jb 0x140ad39c3
00AD36DE  8D 48 08                        lea ecx, [rax + 8]
00AD36E1  3B C8                           cmp ecx, eax
00AD36E3  0F 82 DA 02 00 00               jb 0x140ad39c3
00AD36E9  8D 41 08                        lea eax, [rcx + 8]
00AD36EC  83 F8 08                        cmp eax, 8
00AD36EF  0F 82 CE 02 00 00               jb 0x140ad39c3
00AD36F5  48 8D 50 07                     lea rdx, [rax + 7]
00AD36F9  83 E2 F8                        and edx, 0xfffffff8
00AD36FC  3B D0                           cmp edx, eax
00AD36FE  0F 82 BF 02 00 00               jb 0x140ad39c3
00AD3704  8D 42 08                        lea eax, [rdx + 8]
00AD3707  3B C2                           cmp eax, edx
00AD3709  0F 82 B4 02 00 00               jb 0x140ad39c3
00AD370F  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
00AD3717  83 C0 04                        add eax, 4
00AD371A  45 8B 48 20                     mov r9d, dword ptr [r8 + 0x20]
00AD371E  45 8B 40 10                     mov r8d, dword ptr [r8 + 0x10]
00AD3722  83 F8 04                        cmp eax, 4
00AD3725  72 27                           jb 0x140ad374e
00AD3727  8D 50 04                        lea edx, [rax + 4]
00AD372A  3B D0                           cmp edx, eax
00AD372C  72 20                           jb 0x140ad374e
00AD372E  42 8D 04 02                     lea eax, [rdx + r8]
00AD3732  3B C2                           cmp eax, edx
00AD3734  72 18                           jb 0x140ad374e
00AD3736  8D 50 04                        lea edx, [rax + 4]
00AD3739  BF 95 00 00 C0                  mov edi, 0xc0000095
00AD373E  3B D0                           cmp edx, eax
00AD3740  72 11                           jb 0x140ad3753
00AD3742  42 8D 04 0A                     lea eax, [rdx + r9]
00AD3746  3B C2                           cmp eax, edx
00AD3748  1B DB                           sbb ebx, ebx
00AD374A  23 DF                           and ebx, edi
00AD374C  EB 07                           jmp 0x140ad3755
00AD374E  BF 95 00 00 C0                  mov edi, 0xc0000095
00AD3753  8B DF                           mov ebx, edi
00AD3755  85 DB                           test ebx, ebx
00AD3757  0F 88 6B 02 00 00               js 0x140ad39c8
00AD375D  48 85 F6                        test rsi, rsi
00AD3760  0F 84 36 01 00 00               je 0x140ad389c
00AD3766  33 DB                           xor ebx, ebx
00AD3768  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD376B  85 C9                           test ecx, ecx
00AD376D  75 07                           jne 0x140ad3776
00AD376F  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD3774  EB 24                           jmp 0x140ad379a
00AD3776  8B D1                           mov edx, ecx
00AD3778  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD377E  B9 00 01 00 00                  mov ecx, 0x100
00AD3783  E8 68 E9 0A 00                  call 0x140b820f0
00AD3788  48 85 C0                        test rax, rax
00AD378B  75 07                           jne 0x140ad3794
00AD378D  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD3792  EB 06                           jmp 0x140ad379a
00AD3794  48 89 46 08                     mov qword ptr [rsi + 8], rax
00AD3798  21 1E                           and dword ptr [rsi], ebx
00AD379A  85 DB                           test ebx, ebx
00AD379C  0F 88 26 02 00 00               js 0x140ad39c8
00AD37A2  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD37A6  41 0F BA EF 1C                  bts r15d, 0x1c
00AD37AB  48 85 D2                        test rdx, rdx
00AD37AE  75 17                           jne 0x140ad37c7
00AD37B0  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD37B3  8D 48 08                        lea ecx, [rax + 8]
00AD37B6  3B C8                           cmp ecx, eax
00AD37B8  0F 82 0C 01 00 00               jb 0x140ad38ca
00AD37BE  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD37C1  44 8D 62 01                     lea r12d, [rdx + 1]
00AD37C5  EB 5D                           jmp 0x140ad3824
00AD37C7  44 8B 16                        mov r10d, dword ptr [rsi]
00AD37CA  33 C9                           xor ecx, ecx
00AD37CC  44 8D 61 01                     lea r12d, [rcx + 1]
00AD37D0  41 3B CA                        cmp ecx, r10d
00AD37D3  73 25                           jae 0x140ad37fa
00AD37D5  8B 02                           mov eax, dword ptr [rdx]
00AD37D7  83 C0 04                        add eax, 4
00AD37DA  83 F8 04                        cmp eax, 4
00AD37DD  0F 82 EB 00 00 00               jb 0x140ad38ce
00AD37E3  44 8B C0                        mov r8d, eax
00AD37E6  4C 03 C2                        add r8, rdx
00AD37E9  4C 3B C2                        cmp r8, rdx
00AD37EC  0F 82 DC 00 00 00               jb 0x140ad38ce
00AD37F2  49 8B D0                        mov rdx, r8
00AD37F5  41 03 CC                        add ecx, r12d
00AD37F8  EB D6                           jmp 0x140ad37d0
00AD37FA  4C 8D 42 04                     lea r8, [rdx + 4]
00AD37FE  4C 3B C2                        cmp r8, rdx
00AD3801  0F 82 C7 00 00 00               jb 0x140ad38ce
00AD3807  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD380A  48 8D 42 08                     lea rax, [rdx + 8]
00AD380E  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD3812  48 3B C1                        cmp rax, rcx
00AD3815  0F 87 00 01 00 00               ja 0x140ad391b
00AD381B  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD3821  45 89 38                        mov dword ptr [r8], r15d
00AD3824  44 01 26                        add dword ptr [rsi], r12d
00AD3827  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD382B  48 85 D2                        test rdx, rdx
00AD382E  75 13                           jne 0x140ad3843
00AD3830  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD3833  8D 48 0C                        lea ecx, [rax + 0xc]
00AD3836  3B C8                           cmp ecx, eax
00AD3838  0F 82 8C 00 00 00               jb 0x140ad38ca
00AD383E  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD3841  EB 4D                           jmp 0x140ad3890
00AD3843  44 8B 0E                        mov r9d, dword ptr [rsi]
00AD3846  33 C9                           xor ecx, ecx
00AD3848  41 3B C9                        cmp ecx, r9d
00AD384B  73 1D                           jae 0x140ad386a
00AD384D  8B 02                           mov eax, dword ptr [rdx]
00AD384F  83 C0 04                        add eax, 4
00AD3852  83 F8 04                        cmp eax, 4
00AD3855  72 77                           jb 0x140ad38ce
00AD3857  44 8B C0                        mov r8d, eax
00AD385A  4C 03 C2                        add r8, rdx
00AD385D  4C 3B C2                        cmp r8, rdx
00AD3860  72 6C                           jb 0x140ad38ce
00AD3862  49 8B D0                        mov rdx, r8
00AD3865  41 03 CC                        add ecx, r12d
00AD3868  EB DE                           jmp 0x140ad3848
00AD386A  4C 8D 42 04                     lea r8, [rdx + 4]
00AD386E  4C 3B C2                        cmp r8, rdx
00AD3871  72 5B                           jb 0x140ad38ce
00AD3873  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD3876  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD387A  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD387E  48 3B C1                        cmp rax, rcx
00AD3881  0F 87 94 00 00 00               ja 0x140ad391b
00AD3887  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD388D  4D 89 30                        mov qword ptr [r8], r14
00AD3890  44 01 26                        add dword ptr [rsi], r12d
00AD3893  4D 85 ED                        test r13, r13
00AD3896  75 0E                           jne 0x140ad38a6
00AD3898  85 ED                           test ebp, ebp
00AD389A  74 0E                           je 0x140ad38aa
00AD389C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD38A1  E9 22 01 00 00                  jmp 0x140ad39c8
00AD38A6  85 ED                           test ebp, ebp
00AD38A8  74 F2                           je 0x140ad389c
00AD38AA  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD38AE  48 85 D2                        test rdx, rdx
00AD38B1  75 22                           jne 0x140ad38d5
00AD38B3  83 C5 04                        add ebp, 4
00AD38B6  83 FD 04                        cmp ebp, 4
00AD38B9  72 13                           jb 0x140ad38ce
00AD38BB  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD38BE  8D 0C 28                        lea ecx, [rax + rbp]
00AD38C1  3B C8                           cmp ecx, eax
00AD38C3  72 05                           jb 0x140ad38ca
00AD38C5  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD38C8  EB 6D                           jmp 0x140ad3937
00AD38CA  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
00AD38CE  8B DF                           mov ebx, edi
00AD38D0  E9 F3 00 00 00                  jmp 0x140ad39c8
00AD38D5  44 8B 0E                        mov r9d, dword ptr [rsi]
00AD38D8  33 C9                           xor ecx, ecx
00AD38DA  41 3B C9                        cmp ecx, r9d
00AD38DD  73 1D                           jae 0x140ad38fc
00AD38DF  8B 02                           mov eax, dword ptr [rdx]
00AD38E1  83 C0 04                        add eax, 4
00AD38E4  83 F8 04                        cmp eax, 4
00AD38E7  72 E5                           jb 0x140ad38ce
00AD38E9  44 8B C0                        mov r8d, eax
00AD38EC  4C 03 C2                        add r8, rdx
00AD38EF  4C 3B C2                        cmp r8, rdx
00AD38F2  72 DA                           jb 0x140ad38ce
00AD38F4  49 8B D0                        mov rdx, r8
00AD38F7  41 03 CC                        add ecx, r12d
00AD38FA  EB DE                           jmp 0x140ad38da
00AD38FC  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD3900  4C 3B CA                        cmp r9, rdx
00AD3903  72 C9                           jb 0x140ad38ce
00AD3905  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD3908  48 8D 45 04                     lea rax, [rbp + 4]
00AD390C  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD3910  48 03 C2                        add rax, rdx
00AD3913  44 8B C5                        mov r8d, ebp
00AD3916  48 3B C1                        cmp rax, rcx
00AD3919  76 0A                           jbe 0x140ad3925
00AD391B  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD3920  E9 A3 00 00 00                  jmp 0x140ad39c8
00AD3925  89 2A                           mov dword ptr [rdx], ebp
00AD3927  4D 85 ED                        test r13, r13
00AD392A  74 0B                           je 0x140ad3937
00AD392C  49 8B D5                        mov rdx, r13
00AD392F  49 8B C9                        mov rcx, r9
00AD3932  E8 09 2F BF FF                  call 0x1406c6840
00AD3937  44 01 26                        add dword ptr [rsi], r12d
00AD393A  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD393E  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00AD3946  48 85 D2                        test rdx, rdx
00AD3949  75 18                           jne 0x140ad3963
00AD394B  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD394E  8D 48 08                        lea ecx, [rax + 8]
00AD3951  3B C8                           cmp ecx, eax
00AD3953  0F 82 71 FF FF FF               jb 0x140ad38ca
00AD3959  44 01 26                        add dword ptr [rsi], r12d
00AD395C  33 DB                           xor ebx, ebx
00AD395E  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD3961  EB 65                           jmp 0x140ad39c8
00AD3963  44 8B 16                        mov r10d, dword ptr [rsi]
00AD3966  33 C9                           xor ecx, ecx
00AD3968  41 3B CA                        cmp ecx, r10d
00AD396B  73 25                           jae 0x140ad3992
00AD396D  8B 02                           mov eax, dword ptr [rdx]
00AD396F  83 C0 04                        add eax, 4
00AD3972  83 F8 04                        cmp eax, 4
00AD3975  0F 82 53 FF FF FF               jb 0x140ad38ce
00AD397B  44 8B C8                        mov r9d, eax
00AD397E  4C 03 CA                        add r9, rdx
00AD3981  4C 3B CA                        cmp r9, rdx
00AD3984  0F 82 44 FF FF FF               jb 0x140ad38ce
00AD398A  49 8B D1                        mov rdx, r9
00AD398D  41 03 CC                        add ecx, r12d
00AD3990  EB D6                           jmp 0x140ad3968
00AD3992  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD3996  4C 3B CA                        cmp r9, rdx
00AD3999  0F 82 2F FF FF FF               jb 0x140ad38ce
00AD399F  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD39A2  48 8D 42 08                     lea rax, [rdx + 8]
00AD39A6  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD39AA  33 DB                           xor ebx, ebx
00AD39AC  48 3B C1                        cmp rax, rcx
00AD39AF  0F 87 66 FF FF FF               ja 0x140ad391b
00AD39B5  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD39BB  45 89 01                        mov dword ptr [r9], r8d
00AD39BE  44 01 26                        add dword ptr [rsi], r12d
00AD39C1  EB 05                           jmp 0x140ad39c8
00AD39C3  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD39C8  4D 85 ED                        test r13, r13
00AD39CB  74 11                           je 0x140ad39de
00AD39CD  33 D2                           xor edx, edx
00AD39CF  49 8B CD                        mov rcx, r13
00AD39D2  E8 99 EE 0A 00                  call 0x140b82870
00AD39D7  EB 05                           jmp 0x140ad39de
00AD39D9  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD39DE  8B C3                           mov eax, ebx
00AD39E0  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00AD39E8  48 83 C4 50                     add rsp, 0x50
00AD39EC  41 5F                           pop r15
00AD39EE  41 5E                           pop r14
00AD39F0  41 5D                           pop r13
00AD39F2  41 5C                           pop r12
00AD39F4  5F                              pop rdi
00AD39F5  5E                              pop rsi
00AD39F6  5D                              pop rbp
00AD39F7  C3                              ret
00AD39F8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD34D0(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (80);
    v_r13 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD35A9;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00AD35A9;
    a2 = 0;
loc_00AD351A:
    if (0 >= 3) goto loc_00AD3541;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD39D9;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD39D9;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13 + 1)));
    goto loc_00AD351A;
loc_00AD3541:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD39D9;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r14 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00AD3637;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00AD35A9;
    a2 = 0;
loc_00AD356C:
    if (0 >= 4) goto loc_00AD3592;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD39D9;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD39D9;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13 + 1)));
    goto loc_00AD356C;
loc_00AD3592:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD39D9;
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rdi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) > 5) goto loc_00AD35B3;
loc_00AD35A9:
    goto loc_00AD39DE;
loc_00AD35B3:
    a2 = 0;
loc_00AD35B8:
    if (0 >= 5) goto loc_00AD35DF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD39D9;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD39D9;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13 + 1)));
    goto loc_00AD35B8;
loc_00AD35DF:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD39D9;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) <= 6) goto loc_00AD35A9;
    a2 = 0;
loc_00AD35FA:
    if (0 >= 6) goto loc_00AD3621;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD39D9;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD39D9;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13 + 1)));
    goto loc_00AD35FA;
loc_00AD3621:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD39D9;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_00AD3641;
loc_00AD3637:
    goto loc_00AD39DE;
loc_00AD3641:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD367D;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))), (unsigned int)(0x20534C53ULL), a1);
    if (result != 0) goto loc_00AD3669;
    goto loc_00AD39DE;
loc_00AD3669:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(*(unsigned int *)(v_rbp)), a1);
    a1 = 0;
    goto loc_00AD3680;
loc_00AD367D:
loc_00AD3680:
    if (*(unsigned __int64 *)(v_rip + 5262673) == 0) goto loc_00AD36C0;
    a3 = 0;
    v_stack_m58 = v_stack_p18;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r13 + 1))) == 0) { a3 = result; }
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)));
    v_stack_m68 = a3;
    result = guard_dispatch_icall(v_rdi, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), v_r15, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))));
    goto loc_00AD36C6;
loc_00AD36C0:
loc_00AD36C6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)) + 4)) < 4) goto loc_00AD39C3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp)) + 4) + (20));
    if (((unsigned int)(result)) < 20) goto loc_00AD39C3;
    if (((unsigned int)(result + 8)) < ((unsigned int)(result))) goto loc_00AD39C3;
    if (((unsigned int)(result + 8 + 8)) < 8) goto loc_00AD39C3;
    a2 = (unsigned int)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(result + 8 + 8))) goto loc_00AD39C3;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_00AD39C3;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD374E;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD374E;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1)) < ((unsigned int)(result + 4))) goto loc_00AD374E;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1 + 4)) < ((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1))) goto loc_00AD3753;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    goto loc_00AD3755;
loc_00AD374E:
loc_00AD3753:
loc_00AD3755:
    if (sign_flag) goto loc_00AD39C8;
    if (a4 == 0) goto loc_00AD389C;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)(result + 8);
    if ((unsigned int)(result + 8) != 0) goto loc_00AD3776;
    goto loc_00AD379A;
loc_00AD3776:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    if (result != 0) goto loc_00AD3794;
    goto loc_00AD379A;
loc_00AD3794:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_00AD379A:
    if (sign_flag) goto loc_00AD39C8;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD37C7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD38CA;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD3824;
loc_00AD37C7:
    a1 = 0;
loc_00AD37D0:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD37FA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD38CE;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD38CE;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD37D0;
loc_00AD37FA:
    if ((a3 + 4) < a3) goto loc_00AD38CE;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00AD391B;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_00AD3824:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3843;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD38CA;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_00AD3890;
loc_00AD3843:
    a1 = 0;
loc_00AD3848:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD386A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD38CE;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD38CE;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD3848;
loc_00AD386A:
    if ((a3 + 4) < a3) goto loc_00AD38CE;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00AD391B;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_r14);
loc_00AD3890:
    if (result != 0) goto loc_00AD38A6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD38AA;
loc_00AD389C:
    goto loc_00AD39C8;
loc_00AD38A6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD389C;
loc_00AD38AA:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD38D5;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp))) + (4));
    if (((unsigned int)(v_rbp)) < 4) goto loc_00AD38CE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD38CA;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1);
    goto loc_00AD3937;
loc_00AD38CA:
loc_00AD38CE:
    goto loc_00AD39C8;
loc_00AD38D5:
    a1 = 0;
loc_00AD38DA:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD38FC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD38CE;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD38CE;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD38DA;
loc_00AD38FC:
    if ((a3 + 4) < a3) goto loc_00AD38CE;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = (v_rbp + 4) + (a3);
    if (result <= a1) goto loc_00AD3925;
loc_00AD391B:
    goto loc_00AD39C8;
loc_00AD3925:
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    if (result != 0) {
        a2 = result;
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_rbp)), a3 + 4);
    }
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3963;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD38CA;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD39C8;
loc_00AD3963:
    a1 = 0;
loc_00AD3968:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3992;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD38CE;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD38CE;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD3968;
loc_00AD3992:
    if ((a4 + 4) < a4) goto loc_00AD38CE;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a4 + 8) > a1) goto loc_00AD391B;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_00AD39C8;
loc_00AD39C3:
loc_00AD39C8:
    if (result == 0) goto loc_00AD39DE;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_p18), a4 + 4);
    goto loc_00AD39DE;
loc_00AD39D9:
loc_00AD39DE:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD34D0(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (80);
    local_r13 = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD35A9;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00AD35A9;
    Arg2 = 0;
loc_00AD351A:
    if (0 >= 3) goto loc_00AD3541;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD39D9;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD39D9;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r13 + 1)));
    goto loc_00AD351A;
loc_00AD3541:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD39D9;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r14 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00AD3637;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00AD35A9;
    Arg2 = 0;
loc_00AD356C:
    if (0 >= 4) goto loc_00AD3592;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD39D9;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD39D9;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r13 + 1)));
    goto loc_00AD356C;
loc_00AD3592:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD39D9;
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rdi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) > 5) goto loc_00AD35B3;
loc_00AD35A9:
    goto loc_00AD39DE;
loc_00AD35B3:
    Arg2 = 0;
loc_00AD35B8:
    if (0 >= 5) goto loc_00AD35DF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD39D9;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD39D9;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r13 + 1)));
    goto loc_00AD35B8;
loc_00AD35DF:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD39D9;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) <= 6) goto loc_00AD35A9;
    Arg2 = 0;
loc_00AD35FA:
    if (0 >= 6) goto loc_00AD3621;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD39D9;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD39D9;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r13 + 1)));
    goto loc_00AD35FA;
loc_00AD3621:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD39D9;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_00AD3641;
loc_00AD3637:
    goto loc_00AD39DE;
loc_00AD3641:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD367D;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))), (uint32_t)(0x20534C53ULL), Arg1);
    if (result != 0) goto loc_00AD3669;
    goto loc_00AD39DE;
loc_00AD3669:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(*(uint32_t *)(local_rbp)), Arg1);
    Arg1 = 0;
    goto loc_00AD3680;
loc_00AD367D:
loc_00AD3680:
    if (*(uint64_t *)(v_rip + 0x504D51) == 0) goto loc_00AD36C0;
    Arg3 = 0;
    v_stack_m58 = v_stack_p18;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r13 + 1))) == 0) { Arg3 = result; }
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)));
    v_stack_m68 = Arg3;
    result = guard_dispatch_icall(local_rdi, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), local_r15, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))));
    goto loc_00AD36C6;
loc_00AD36C0:
loc_00AD36C6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)) + 4)) < 4) goto loc_00AD39C3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp)) + 4) + (20));
    if (((uint32_t)(result)) < 20) goto loc_00AD39C3;
    if (((uint32_t)(result + 8)) < ((uint32_t)(result))) goto loc_00AD39C3;
    if (((uint32_t)(result + 8 + 8)) < 8) goto loc_00AD39C3;
    Arg2 = (uint32_t)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(result + 8 + 8))) goto loc_00AD39C3;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_00AD39C3;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD374E;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD374E;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1)) < ((uint32_t)(result + 4))) goto loc_00AD374E;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1 + 4)) < ((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1))) goto loc_00AD3753;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    goto loc_00AD3755;
loc_00AD374E:
loc_00AD3753:
loc_00AD3755:
    if (sign_flag) goto loc_00AD39C8;
    if (Arg4 == 0) goto loc_00AD389C;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result + 8);
    if ((uint32_t)(result + 8) != 0) goto loc_00AD3776;
    goto loc_00AD379A;
loc_00AD3776:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    if (result != 0) goto loc_00AD3794;
    goto loc_00AD379A;
loc_00AD3794:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_00AD379A:
    if (sign_flag) goto loc_00AD39C8;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD37C7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD38CA;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD3824;
loc_00AD37C7:
    Arg1 = 0;
loc_00AD37D0:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD37FA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD38CE;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD38CE;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD37D0;
loc_00AD37FA:
    if ((Arg3 + 4) < Arg3) goto loc_00AD38CE;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00AD391B;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_00AD3824:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3843;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD38CA;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_00AD3890;
loc_00AD3843:
    Arg1 = 0;
loc_00AD3848:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD386A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD38CE;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD38CE;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD3848;
loc_00AD386A:
    if ((Arg3 + 4) < Arg3) goto loc_00AD38CE;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00AD391B;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_r14);
loc_00AD3890:
    if (result != 0) goto loc_00AD38A6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD38AA;
loc_00AD389C:
    goto loc_00AD39C8;
loc_00AD38A6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD389C;
loc_00AD38AA:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD38D5;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp))) + (4));
    if (((uint32_t)(local_rbp)) < 4) goto loc_00AD38CE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD38CA;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1);
    goto loc_00AD3937;
loc_00AD38CA:
loc_00AD38CE:
    goto loc_00AD39C8;
loc_00AD38D5:
    Arg1 = 0;
loc_00AD38DA:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD38FC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD38CE;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD38CE;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD38DA;
loc_00AD38FC:
    if ((Arg3 + 4) < Arg3) goto loc_00AD38CE;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = (local_rbp + 4) + (Arg3);
    if (result <= Arg1) goto loc_00AD3925;
loc_00AD391B:
    goto loc_00AD39C8;
loc_00AD3925:
    *(uint32_t *)(Arg3) = (uint32_t)(local_rbp);
    if (result != 0) {
        Arg2 = result;
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbp)), Arg3 + 4);
    }
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3963;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD38CA;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD39C8;
loc_00AD3963:
    Arg1 = 0;
loc_00AD3968:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3992;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD38CE;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD38CE;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD3968;
loc_00AD3992:
    if ((Arg4 + 4) < Arg4) goto loc_00AD38CE;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg4 + 8) > Arg1) goto loc_00AD391B;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_00AD39C8;
loc_00AD39C3:
loc_00AD39C8:
    if (result == 0) goto loc_00AD39DE;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(v_stack_p18), Arg4 + 4);
    goto loc_00AD39DE;
loc_00AD39D9:
loc_00AD39DE:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD34D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
