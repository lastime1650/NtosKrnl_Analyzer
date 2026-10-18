# ObpParseSymbolicLinkEx

- RVA: `0x008B35C0`–`0x008B3A9C` (길이 `1,244` bytes)
- VA: `0x00000001408B35C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008273C`
- 디코드: `305`개 명령, `1,244/1,244` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008B3712` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B3721` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B377F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B37C6` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x008B3818` → [SeQueryInformationToken](SeQueryInformationToken_function_008B5090.md) (function, `0x008B5090`)
- `0x008B3838` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x008B3883` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B38AF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B38D6` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008B38E0` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x008B3929` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B398F` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008B39AE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B39D4` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008B3A12` → [RtlIsSandboxedToken](RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x008B3A51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B3A63` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x008B3A92` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089C4F8`
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089CB10`

### Static image references
- `0x008B35DC` → RVA `0x00E0A740` (`.data`; read)
- `0x008B37A0` → RVA `0x00F0F658` (`.data`; read)
- `0x008B3961` → RVA `0x00B01420` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008B39E4` → RVA `0x00E074A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x008B3712` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B3721` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B377F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B37C6` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x008B3883` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B38AF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B38E0` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x008B3929` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B39AE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B3A51` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B3A63` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x008B3A92` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008B39EB` → [sub_00B1A802](../B1/Unknown_function_00B1A802.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008B35C0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008B35C5  55                              push rbp
008B35C6  56                              push rsi
008B35C7  57                              push rdi
008B35C8  41 54                           push r12
008B35CA  41 55                           push r13
008B35CC  41 56                           push r14
008B35CE  41 57                           push r15
008B35D0  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
008B35D5  48 81 EC 40 01 00 00            sub rsp, 0x140
008B35DC  48 8B 05 5D 71 55 00            mov rax, qword ptr [rip + 0x55715d]
008B35E3  48 33 C4                        xor rax, rsp
008B35E6  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
008B35EA  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
008B35F1  4C 8B E2                        mov r12, rdx
008B35F4  4C 8B BD A8 00 00 00            mov r15, qword ptr [rbp + 0xa8]
008B35FB  45 32 F6                        xor r14b, r14b
008B35FE  48 8B B5 B0 00 00 00            mov rsi, qword ptr [rbp + 0xb0]
008B3605  0F 57 C0                        xorps xmm0, xmm0
008B3608  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B360D  4D 8B E8                        mov r13, r8
008B3610  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
008B3617  48 8B D9                        mov rbx, rcx
008B361A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
008B361F  33 D2                           xor edx, edx
008B3621  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008B3626  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008B3629  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
008B362E  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
008B3632  8D 7A 01                        lea edi, [rdx + 1]
008B3635  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
008B363A  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
008B363F  A8 02                           test al, 2
008B3641  0F 85 C3 03 00 00               jne 0x1408b3a0a
008B3647  BF 00 40 00 00                  mov edi, 0x4000
008B364C  39 7B 24                        cmp dword ptr [rbx + 0x24], edi
008B364F  0F 82 8B 01 00 00               jb 0x1408b37e0
008B3655  45 84 F6                        test r14b, r14b
008B3658  0F 85 82 01 00 00               jne 0x1408b37e0
008B365E  8B FA                           mov edi, edx
008B3660  39 7B 24                        cmp dword ptr [rbx + 0x24], edi
008B3663  0F 82 DA 02 00 00               jb 0x1408b3943
008B3669  45 84 F6                        test r14b, r14b
008B366C  0F 85 D1 02 00 00               jne 0x1408b3943
008B3672  66 83 3E 00                     cmp word ptr [rsi], 0
008B3676  0F 84 24 01 00 00               je 0x1408b37a0
008B367C  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
008B3680  66 83 38 5C                     cmp word ptr [rax], 0x5c
008B3684  0F 85 7F 02 00 00               jne 0x1408b3909
008B368A  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B368D  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
008B3692  A8 08                           test al, 8
008B3694  0F 85 BE 03 00 00               jne 0x1408b3a58
008B369A  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B369D  A8 04                           test al, 4
008B369F  0F 85 BE 03 00 00               jne 0x1408b3a63
008B36A5  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B36A8  4C 8D 6B 08                     lea r13, [rbx + 8]
008B36AC  A8 10                           test al, 0x10
008B36AE  0F 85 60 02 00 00               jne 0x1408b3914
008B36B4  45 0F B7 75 00                  movzx r14d, word ptr [r13]
008B36B9  45 85 F6                        test r14d, r14d
008B36BC  74 16                           je 0x1408b36d4
008B36BE  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
008B36C2  41 8B CE                        mov ecx, r14d
008B36C5  48 D1 E9                        shr rcx, 1
008B36C8  66 83 7C 48 FE 5C               cmp word ptr [rax + rcx*2 - 2], 0x5c
008B36CE  0F 84 9D 03 00 00               je 0x1408b3a71
008B36D4  0F B7 3E                        movzx edi, word ptr [rsi]
008B36D7  41 03 FE                        add edi, r14d
008B36DA  81 FF F0 FF 00 00               cmp edi, 0xfff0
008B36E0  0F 87 B6 01 00 00               ja 0x1408b389c
008B36E6  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
008B36EB  66 89 44 24 32                  mov word ptr [rsp + 0x32], ax
008B36F0  66 3B C7                        cmp ax, di
008B36F3  0F 86 74 01 00 00               jbe 0x1408b386d
008B36F9  4D 8B 67 08                     mov r12, qword ptr [r15 + 8]
008B36FD  0F B7 06                        movzx eax, word ptr [rsi]
008B3700  66 85 C0                        test ax, ax
008B3703  74 12                           je 0x1408b3717
008B3705  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
008B3709  44 8B C0                        mov r8d, eax
008B370C  41 8B CE                        mov ecx, r14d
008B370F  49 03 CC                        add rcx, r12
008B3712  E8 29 31 E1 FF                  call 0x1406c6840
008B3717  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
008B371B  49 8B CC                        mov rcx, r12
008B371E  45 8B C6                        mov r8d, r14d
008B3721  E8 1A 31 E1 FF                  call 0x1406c6840
008B3726  33 C9                           xor ecx, ecx
008B3728  0F B7 C7                        movzx eax, di
008B372B  48 D1 E8                        shr rax, 1
008B372E  66 41 89 0C 44                  mov word ptr [r12 + rax*2], cx
008B3733  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008B3737  4C 3B E1                        cmp r12, rcx
008B373A  0F 85 64 01 00 00               jne 0x1408b38a4
008B3740  0F B7 44 24 32                  movzx eax, word ptr [rsp + 0x32]
008B3745  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008B374A  66 41 89 47 02                  mov word ptr [r15 + 2], ax
008B374F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008B3754  4D 89 67 08                     mov qword ptr [r15 + 8], r12
008B3758  66 41 89 3F                     mov word ptr [r15], di
008B375C  48 85 C0                        test rax, rax
008B375F  0F 85 FB 00 00 00               jne 0x1408b3860
008B3765  48 89 19                        mov qword ptr [rcx], rbx
008B3768  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B376B  A8 01                           test al, 1
008B376D  0F 85 BB 02 00 00               jne 0x1408b3a2e
008B3773  B8 04 01 00 00                  mov eax, 0x104
008B3778  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
008B377C  48 33 CC                        xor rcx, rsp
008B377F  E8 BC 8E DF FF                  call 0x1406ac640
008B3784  48 8B 9C 24 88 01 00 00         mov rbx, qword ptr [rsp + 0x188]
008B378C  48 81 C4 40 01 00 00            add rsp, 0x140
008B3793  41 5F                           pop r15
008B3795  41 5E                           pop r14
008B3797  41 5D                           pop r13
008B3799  41 5C                           pop r12
008B379B  5F                              pop rdi
008B379C  5E                              pop rsi
008B379D  5D                              pop rbp
008B379E  C3                              ret
008B379F  CC                              int3
008B37A0  4C 3B 25 B1 BE 65 00            cmp r12, qword ptr [rip + 0x65beb1]
008B37A7  0F 85 DD FE FF FF               jne 0x1408b368a
008B37AD  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B37B0  A8 01                           test al, 1
008B37B2  0F 85 28 01 00 00               jne 0x1408b38e0
008B37B8  44 0F B6 4C 24 30               movzx r9d, byte ptr [rsp + 0x30]
008B37BE  4D 8B C4                        mov r8, r12
008B37C1  33 D2                           xor edx, edx
008B37C3  48 8B CB                        mov rcx, rbx
008B37C6  E8 35 55 B8 FF                  call 0x140438d00
008B37CB  44 8B E0                        mov r12d, eax
008B37CE  85 C0                           test eax, eax
008B37D0  0F 88 1C 01 00 00               js 0x1408b38f2
008B37D6  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008B37DB  48 89 19                        mov qword ptr [rcx], rbx
008B37DE  EB 6A                           jmp 0x1408b384a
008B37E0  0F 57 C0                        xorps xmm0, xmm0
008B37E3  49 83 C5 20                     add r13, 0x20
008B37E7  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
008B37EB  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
008B37EF  45 84 C9                        test r9b, r9b
008B37F2  0F 84 C1 00 00 00               je 0x1408b38b9
008B37F8  4D 85 ED                        test r13, r13
008B37FB  0F 84 CD 00 00 00               je 0x1408b38ce
008B3801  49 8B 4D 00                     mov rcx, qword ptr [r13]
008B3805  48 85 C9                        test rcx, rcx
008B3808  75 04                           jne 0x1408b380e
008B380A  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
008B380E  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
008B3813  BA 19 00 00 00                  mov edx, 0x19
008B3818  E8 73 18 00 00                  call 0x1408b5090
008B381D  44 8B E0                        mov r12d, eax
008B3820  85 C0                           test eax, eax
008B3822  0F 88 10 02 00 00               js 0x1408b3a38
008B3828  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
008B382C  48 8D 4D 88                     lea rcx, [rbp - 0x78]
008B3830  4C 3B E9                        cmp r13, rcx
008B3833  75 0C                           jne 0x1408b3841
008B3835  49 8B CD                        mov rcx, r13
008B3838  E8 D3 7E FB FF                  call 0x14086b710
008B383D  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
008B3841  45 85 E4                        test r12d, r12d
008B3844  0F 89 B8 00 00 00               jns 0x1408b3902
008B384A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B384F  48 85 C9                        test rcx, rcx
008B3852  0F 85 3A 02 00 00               jne 0x1408b3a92
008B3858  41 8B C4                        mov eax, r12d
008B385B  E9 18 FF FF FF                  jmp 0x1408b3778
008B3860  48 89 01                        mov qword ptr [rcx], rax
008B3863  B8 18 01 00 00                  mov eax, 0x118
008B3868  E9 0B FF FF FF                  jmp 0x1408b3778
008B386D  8D 47 02                        lea eax, [rdi + 2]
008B3870  B9 00 01 00 00                  mov ecx, 0x100
008B3875  0F B7 D0                        movzx edx, ax
008B3878  41 B8 4F 62 4E 6D               mov r8d, 0x6d4e624f
008B387E  66 89 44 24 32                  mov word ptr [rsp + 0x32], ax
008B3883  E8 68 E8 2C 00                  call 0x140b820f0
008B3888  4C 8B E0                        mov r12, rax
008B388B  48 85 C0                        test rax, rax
008B388E  0F 85 69 FE FF FF               jne 0x1408b36fd
008B3894  41 BC 9A 00 00 C0               mov r12d, 0xc000009a
008B389A  EB AE                           jmp 0x1408b384a
008B389C  41 BC 06 01 00 C0               mov r12d, 0xc0000106
008B38A2  EB A6                           jmp 0x1408b384a
008B38A4  48 85 C9                        test rcx, rcx
008B38A7  0F 84 93 FE FF FF               je 0x1408b3740
008B38AD  33 D2                           xor edx, edx
008B38AF  E8 BC EF 2C 00                  call 0x140b82870
008B38B4  E9 87 FE FF FF                  jmp 0x1408b3740
008B38B9  B8 00 50 00 00                  mov eax, 0x5000
008B38BE  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
008B38C2  3B C7                           cmp eax, edi
008B38C4  0F 42 F8                        cmovb edi, eax
008B38C7  33 D2                           xor edx, edx
008B38C9  E9 92 FD FF FF                  jmp 0x1408b3660
008B38CE  48 8D 4D 88                     lea rcx, [rbp - 0x78]
008B38D2  4C 8D 6D 88                     lea r13, [rbp - 0x78]
008B38D6  E8 45 7F FB FF                  call 0x14086b820
008B38DB  E9 21 FF FF FF                  jmp 0x1408b3801
008B38E0  E8 FB 29 B8 FF                  call 0x1404362e0
008B38E5  84 C0                           test al, al
008B38E7  0F 85 9D FD FF FF               jne 0x1408b368a
008B38ED  E9 C6 FE FF FF                  jmp 0x1408b37b8
008B38F2  3D 24 00 00 C0                  cmp eax, 0xc0000024
008B38F7  0F 84 8D FD FF FF               je 0x1408b368a
008B38FD  E9 48 FF FF FF                  jmp 0x1408b384a
008B3902  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
008B3907  EB B9                           jmp 0x1408b38c2
008B3909  41 BC 24 00 00 C0               mov r12d, 0xc0000024
008B390F  E9 36 FF FF FF                  jmp 0x1408b384a
008B3914  49 8B 45 00                     mov rax, qword ptr [r13]
008B3918  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
008B391D  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
008B3921  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008B3926  48 8B CB                        mov rcx, rbx
008B3929  E8 A2 71 E0 FF                  call 0x1406baad0
008B392E  44 8B E0                        mov r12d, eax
008B3931  85 C0                           test eax, eax
008B3933  0F 88 11 FF FF FF               js 0x1408b384a
008B3939  4C 8D 6C 24 78                  lea r13, [rsp + 0x78]
008B393E  E9 71 FD FF FF                  jmp 0x1408b36b4
008B3943  0F 0D 4B 1C                     prefetchw byte ptr [rbx + 0x1c]
008B3947  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008B394A  8B C8                           mov ecx, eax
008B394C  81 C9 00 00 00 80               or ecx, 0x80000000
008B3952  F0 0F B1 4B 1C                  lock cmpxchg dword ptr [rbx + 0x1c], ecx
008B3957  75 F1                           jne 0x1408b394a
008B3959  85 C0                           test eax, eax
008B395B  0F 88 95 00 00 00               js 0x1408b39f6
008B3961  48 8D 05 B8 DA 24 00            lea rax, [rip + 0x24dab8]
008B3968  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
008B396C  4C 8B EA                        mov r13, rdx
008B396F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008B3974  33 D2                           xor edx, edx
008B3976  48 C7 44 24 40 0E 00 10 00      mov qword ptr [rsp + 0x40], 0x10000e
008B397F  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
008B3984  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008B3989  45 33 C0                        xor r8d, r8d
008B398C  48 8B CB                        mov rcx, rbx
008B398F  E8 3C 45 FF FF                  call 0x1408a7ed0
008B3994  3D 04 00 00 C0                  cmp eax, 0xc0000004
008B3999  0F 85 A6 00 00 00               jne 0x1408b3a45
008B399F  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
008B39A3  B9 00 01 00 00                  mov ecx, 0x100
008B39A8  41 B8 4F 62 4E 6D               mov r8d, 0x6d4e624f
008B39AE  E8 3D E7 2C 00                  call 0x140b820f0
008B39B3  4C 8B E8                        mov r13, rax
008B39B6  48 85 C0                        test rax, rax
008B39B9  0F 84 86 00 00 00               je 0x1408b3a45
008B39BF  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
008B39C4  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
008B39C9  48 8B D0                        mov rdx, rax
008B39CC  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008B39D1  48 8B CB                        mov rcx, rbx
008B39D4  E8 F7 44 FF FF                  call 0x1408a7ed0
008B39D9  85 C0                           test eax, eax
008B39DB  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
008B39E0  4D 0F 49 C5                     cmovns r8, r13
008B39E4  83 3D B5 3A 55 00 05            cmp dword ptr [rip + 0x553ab5], 5
008B39EB  0F 87 11 6E 26 00               ja 0x140b1a802
008B39F1  4D 85 ED                        test r13, r13
008B39F4  75 56                           jne 0x1408b3a4c
008B39F6  45 84 F6                        test r14b, r14b
008B39F9  0F 84 73 FC FF FF               je 0x1408b3672
008B39FF  41 BC 34 00 00 C0               mov r12d, 0xc0000034
008B3A05  E9 40 FE FF FF                  jmp 0x1408b384a
008B3A0A  49 8D 48 20                     lea rcx, [r8 + 0x20]
008B3A0E  41 0F B6 D1                     movzx edx, r9b
008B3A12  E8 99 00 00 00                  call 0x1408b3ab0
008B3A17  44 0F B6 4C 24 30               movzx r9d, byte ptr [rsp + 0x30]
008B3A1D  84 C0                           test al, al
008B3A1F  45 0F B6 F6                     movzx r14d, r14b
008B3A23  44 0F 44 F7                     cmove r14d, edi
008B3A27  33 D2                           xor edx, edx
008B3A29  E9 19 FC FF FF                  jmp 0x1408b3647
008B3A2E  B8 68 03 00 00                  mov eax, 0x368
008B3A33  E9 40 FD FF FF                  jmp 0x1408b3778
008B3A38  33 C9                           xor ecx, ecx
008B3A3A  8B C1                           mov eax, ecx
008B3A3C  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
008B3A40  E9 E7 FD FF FF                  jmp 0x1408b382c
008B3A45  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
008B3A4A  EB 98                           jmp 0x1408b39e4
008B3A4C  33 D2                           xor edx, edx
008B3A4E  49 8B CD                        mov rcx, r13
008B3A51  E8 1A EE 2C 00                  call 0x140b82870
008B3A56  EB 9E                           jmp 0x1408b39f6
008B3A58  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
008B3A5B  21 47 04                        and dword ptr [rdi + 4], eax
008B3A5E  E9 37 FC FF FF                  jmp 0x1408b369a
008B3A63  E8 58 C3 BD FF                  call 0x14048fdc0
008B3A68  48 89 47 08                     mov qword ptr [rdi + 8], rax
008B3A6C  E9 34 FC FF FF                  jmp 0x1408b36a5
008B3A71  66 83 3E 00                     cmp word ptr [rsi], 0
008B3A75  0F 84 59 FC FF FF               je 0x1408b36d4
008B3A7B  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
008B3A7F  66 83 38 5C                     cmp word ptr [rax], 0x5c
008B3A83  0F 85 4B FC FF FF               jne 0x1408b36d4
008B3A89  41 83 C6 FE                     add r14d, -2
008B3A8D  E9 42 FC FF FF                  jmp 0x1408b36d4
008B3A92  E8 B9 58 A4 FF                  call 0x1402f9350
008B3A97  E9 BC FD FF FF                  jmp 0x1408b3858
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpParseSymbolicLinkEx(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m144;
    unsigned __int16 v_stack_m146;
    unsigned __int8 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int16 v_stack_p32;
    unsigned __int64 v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 5599581)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m108 = a10;
    v_stack_m120 = a2;
    a2 = 0;
    v_stack_m118 = a11;
    v_stack_m148 = a4;
    v_stack_m144 = 0;
    v_stack_m110 = 0;
    v_stack_m100 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (2)) != 0) goto loc_008B3A0A;
loc_008B3647:
    if ((*(unsigned int *)(a1 + 36)) < ((unsigned int)((unsigned int)(0x4000ULL)))) goto loc_008B37E0;
    if (0 != 0) goto loc_008B37E0;
loc_008B3660:
    if ((*(unsigned int *)(a1 + 36)) < 0) goto loc_008B3943;
    if (0 != 0) goto loc_008B3943;
loc_008B3672:
    if ((*(unsigned __int16 *)(a7)) == 0) goto loc_008B37A0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a7 + 8))) != 92) goto loc_008B3909;
loc_008B368A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (8)) != 0) goto loc_008B3A58;
loc_008B369A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (4)) != 0) goto loc_008B3A63;
loc_008B36A5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (16)) != 0) goto loc_008B3914;
loc_008B36B4:
    if ((unsigned int)(*(unsigned __int16 *)(a1 + 8)) == 0) goto loc_008B36D4;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 8)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8 + 8) + a1 * 2 - 2)) == 92) goto loc_008B3A71;
loc_008B36D4:
    v_rdi = (unsigned int)((*(unsigned __int16 *)(a7)) + ((unsigned int)(*(unsigned __int16 *)(a1 + 8))));
    if (((unsigned int)(v_rdi)) > 0xFFF0ULL) goto loc_008B389C;
    v_stack_m146 = (unsigned __int16)(*(unsigned __int16 *)(a6 + 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(a6 + 2))) <= ((unsigned __int16)(v_rdi))) goto loc_008B386D;
loc_008B36FD:
    result = *(unsigned __int16 *)(a7);
    if ((unsigned __int16)(*(unsigned __int16 *)(a7)) != 0) {
        a2 = *(unsigned __int64 *)(a7 + 8);
        a3 = (unsigned int)(*(unsigned __int16 *)(a7));
        a1 = (unsigned int)(*(unsigned __int16 *)(a1 + 8));
        a1 = (a1) + (*(unsigned __int64 *)(a6 + 8));
        result = memcpy(a1, a2, a3, a4);
    }
    result = memcpy(*(unsigned __int64 *)(a6 + 8), *(unsigned __int64 *)(a1 + 8 + 8), (unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 8))), a4);
    a1 = 0;
    result = ((unsigned __int16)(v_rdi)) >> (1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 8) + result * 2) = 0;
    if ((*(unsigned __int64 *)(a6 + 8)) != (*(unsigned __int64 *)(a6 + 8))) goto loc_008B38A4;
loc_008B3740:
    *(unsigned __int16 *)(a6 + 2) = (unsigned __int16)(v_stack_m146);
    *(unsigned __int64 *)(a6 + 8) = *(unsigned __int64 *)(a6 + 8);
    *(unsigned __int16 *)(a6) = (unsigned __int16)(v_rdi);
    if (v_stack_m110 != 0) goto loc_008B3860;
    *(unsigned __int64 *)(v_stack_m118) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (1)) != 0) goto loc_008B3A2E;
loc_008B3778:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 8 + 8), (unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 8))), a4);
    v_rsp = (v_rsp) + (320);
    return result;
loc_008B37A0:
    if ((*(unsigned __int64 *)(a6 + 8)) != (*(unsigned __int64 *)(v_rip + 6667953))) goto loc_008B368A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 28)))) & (1)) != 0) goto loc_008B38E0;
loc_008B37B8:
    a2 = 0;
    result = ObReferenceObjectByPointer(v_stack_p10, a2, *(unsigned __int64 *)(a6 + 8), v_stack_p30);
    if (sign_flag) goto loc_008B38F2;
    *(unsigned __int64 *)(v_stack_p60) = v_stack_p10;
    goto loc_008B384A;
loc_008B37E0:
    v_r13 = (a1 + 8) + (32);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    if ((unsigned __int8)(v_stack_p30) == 0) goto loc_008B38B9;
    if (v_r13 == 0) goto loc_008B38CE;
loc_008B3801:
    if (*(unsigned __int64 *)(v_r13) == 0) {
        a1 = *(unsigned __int64 *)(v_r13 + 16);
    }
    result = SeQueryInformationToken(a1, 25, v_stack_p34, v_stack_p30);
    if (sign_flag) goto loc_008B3A38;
loc_008B382C:
    result = (unsigned int)(v_stack_p34);
    if (v_r13 == v_stack_mF0) {
        a1 = v_r13;
        result = SeReleaseSubjectContext(a1, 25, v_stack_p34, v_stack_p30);
        result = v_stack_p34;
    }
    if (!sign_flag) goto loc_008B3902;
loc_008B384A:
    if (v_stack_p68 != 0) goto loc_008B3A92;
loc_008B3858:
    goto loc_008B3778;
loc_008B3860:
    *(unsigned __int64 *)(v_stack_p68) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    goto loc_008B3778;
loc_008B386D:
    v_stack_p32 = (unsigned __int16)(v_rdi + 2);
    result = ExAllocatePool2(256, (unsigned __int16)(v_rdi + 2), (unsigned int)(0x6D4E624FULL), v_stack_p30);
    if (result != 0) goto loc_008B36FD;
    goto loc_008B384A;
loc_008B389C:
    goto loc_008B384A;
loc_008B38A4:
    if (256 == 0) goto loc_008B3740;
    a2 = 0;
    result = ExFreePoolWithTag(256, a2, (unsigned int)(0x6D4E624FULL), v_stack_p30);
    goto loc_008B3740;
loc_008B38B9:
    v_stack_p34 = (unsigned int)((unsigned int)(0x5000ULL));
loc_008B38C2:
    if (((unsigned int)((unsigned int)(0x5000ULL))) < ((unsigned int)(v_rdi))) { v_rdi = (unsigned int)((unsigned int)(0x5000ULL)); }
    a2 = 0;
    goto loc_008B3660;
loc_008B38CE:
    result = SeCaptureSubjectContext(v_stack_mF0, a2, (unsigned int)(0x6D4E624FULL), v_stack_p30);
    goto loc_008B3801;
loc_008B38E0:
    result = PsIsCurrentThreadInServerSilo(v_stack_mF0, a2, (unsigned int)(0x6D4E624FULL), v_stack_p30);
    if ((unsigned __int8)(result) != 0) goto loc_008B368A;
    goto loc_008B37B8;
loc_008B38F2:
    if (((unsigned int)(result)) == 0xC0000024ULL) goto loc_008B368A;
    goto loc_008B384A;
loc_008B3902:
    goto loc_008B38C2;
loc_008B3909:
    goto loc_008B384A;
loc_008B3914:
    result = guard_dispatch_icall(v_stack_p10, *(unsigned __int64 *)(v_stack_p10 + 16), v_stack_p78, v_stack_p68);
    if (sign_flag) goto loc_008B384A;
    goto loc_008B36B4;
loc_008B3943:
loc_008B394A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 28))))) | (0x80000000ULL));
    if (condition_is_not_equal) goto loc_008B394A;
    if (sign_flag) goto loc_008B39F6;
    v_stack_p38 = (unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 16));
    v_stack_p48 = v_rip + 2415288;
    a2 = 0;
    v_stack_p40 = 0x10000EULL;
    v_stack_p20 = 0;
    a3 = 0;
    result = ObQueryNameStringMode(v_stack_p10, a2, a3, v_stack_p38);
    if (((unsigned int)(result)) != 0xC0000004ULL) goto loc_008B3A45;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_p38), (unsigned int)(0x6D4E624FULL), v_stack_p38);
    if (result == 0) goto loc_008B3A45;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p10, result, (unsigned int)(v_stack_p38), v_stack_p38);
    a3 = v_stack_p40;
    if (!sign_flag) { a3 = result; }
loc_008B39E4:
    if (result != 0) goto loc_008B3A4C;
loc_008B39F6:
    if ((unsigned __int8)(*(unsigned __int16 *)(a1 + 8)) == 0) goto loc_008B3672;
    goto loc_008B384A;
loc_008B3A0A:
    result = RtlIsSandboxedToken(a3 + 32, (unsigned __int8)(v_stack_p38), a3, v_stack_p38);
    v_r14 = (unsigned __int8)(*(unsigned __int16 *)(a1 + 8));
    if ((unsigned __int8)(result) == 0) { v_r14 = (unsigned int)(v_rdi); }
    a2 = 0;
    goto loc_008B3647;
loc_008B3A2E:
    goto loc_008B3778;
loc_008B3A38:
    a1 = 0;
    v_stack_p34 = 0;
    goto loc_008B382C;
loc_008B3A45:
    goto loc_008B39E4;
loc_008B3A4C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_p40, v_stack_p30);
    goto loc_008B39F6;
loc_008B3A58:
    goto loc_008B369A;
loc_008B3A63:
    result = HalAdjustResourceList(result, a2, v_stack_p40, v_stack_p30);
    *(unsigned __int64 *)(v_rdi + 8) = result;
    goto loc_008B36A5;
loc_008B3A71:
    if ((*(unsigned __int16 *)(a7)) == 0) goto loc_008B36D4;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a7 + 8))) != 92) goto loc_008B36D4;
    v_r14 = (unsigned int)((v_r14) + (-2));
    goto loc_008B36D4;
loc_008B3A92:
    result = ObfDereferenceObject(result, a2, v_stack_p40, v_stack_p30);
    goto loc_008B3858;
}
```

## 5. (Beta) C Style

```c
int64_t ObpParseSymbolicLinkEx(void *Arg1, int64_t Arg2, void *Arg3, uint8_t Arg4, uint64_t Arg5, void *Arg6, void *Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m144;
    uint16_t v_stack_m146;
    uint8_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m78;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p30;
    uint16_t v_stack_p32;
    uint64_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x55715D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m108 = Arg10;
    v_stack_m120 = Arg2;
    Arg2 = 0;
    v_stack_m118 = Arg11;
    v_stack_m148 = Arg4;
    v_stack_m144 = 0;
    v_stack_m110 = 0;
    v_stack_m100 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (2)) != 0) goto loc_008B3A0A;
loc_008B3647:
    if ((*(uint32_t *)(arg1 + 0x24)) < ((uint32_t)((uint32_t)(0x4000ULL)))) goto loc_008B37E0;
    if (0 != 0) goto loc_008B37E0;
loc_008B3660:
    if ((*(uint32_t *)(arg1 + 0x24)) < 0) goto loc_008B3943;
    if (0 != 0) goto loc_008B3943;
loc_008B3672:
    if ((*(uint16_t *)(arg7)) == 0) goto loc_008B37A0;
    if ((*(uint16_t *)(*(uint64_t *)(arg7 + 0x8))) != 92) goto loc_008B3909;
loc_008B368A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (8)) != 0) goto loc_008B3A58;
loc_008B369A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (4)) != 0) goto loc_008B3A63;
loc_008B36A5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (16)) != 0) goto loc_008B3914;
loc_008B36B4:
    if ((uint32_t)(*(uint16_t *)(arg1 + 0x8)) == 0) goto loc_008B36D4;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x8)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8 + 0x8) + arg1 * 2 - 0x2)) == 92) goto loc_008B3A71;
loc_008B36D4:
    local_rdi = (uint32_t)((*(uint16_t *)(arg7)) + ((uint32_t)(*(uint16_t *)(arg1 + 0x8))));
    if (((uint32_t)(local_rdi)) > 0xFFF0ULL) goto loc_008B389C;
    v_stack_m146 = (uint16_t)(*(uint16_t *)(arg6 + 0x2));
    if (((uint16_t)(*(uint16_t *)(arg6 + 0x2))) <= ((uint16_t)(local_rdi))) goto loc_008B386D;
loc_008B36FD:
    result = *(uint16_t *)(arg7);
    if ((uint16_t)(*(uint16_t *)(arg7)) != 0) {
        Arg2 = *(uint64_t *)(arg7 + 0x8);
        Arg3 = (uint32_t)(*(uint16_t *)(arg7));
        Arg1 = (uint32_t)(*(uint16_t *)(arg1 + 0x8));
        Arg1 = (Arg1) + (*(uint64_t *)(arg6 + 0x8));
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    result = memcpy(*(uint64_t *)(arg6 + 0x8), *(uint64_t *)(arg1 + 0x8 + 0x8), (uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x8))), Arg4);
    Arg1 = 0;
    result = ((uint16_t)(local_rdi)) >> (1);
    *(uint16_t *)(*(uint64_t *)(arg6 + 0x8) + result * 2) = 0;
    if ((*(uint64_t *)(arg6 + 0x8)) != (*(uint64_t *)(arg6 + 0x8))) goto loc_008B38A4;
loc_008B3740:
    *(uint16_t *)(arg6 + 0x2) = (uint16_t)(v_stack_m146);
    *(uint64_t *)(arg6 + 0x8) = *(uint64_t *)(arg6 + 0x8);
    *(uint16_t *)(arg6) = (uint16_t)(local_rdi);
    if (v_stack_m110 != 0) goto loc_008B3860;
    *(uint64_t *)(v_stack_m118) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (1)) != 0) goto loc_008B3A2E;
loc_008B3778:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x8 + 0x8), (uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x8))), Arg4);
    local_rsp = (local_rsp) + (320);
    return result;
loc_008B37A0:
    if ((*(uint64_t *)(arg6 + 0x8)) != (*(uint64_t *)(v_rip + 0x65BEB1))) goto loc_008B368A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x1C)))) & (1)) != 0) goto loc_008B38E0;
loc_008B37B8:
    Arg2 = 0;
    result = ObReferenceObjectByPointer(v_stack_p10, Arg2, *(uint64_t *)(arg6 + 0x8), v_stack_p30);
    if (sign_flag) goto loc_008B38F2;
    *(uint64_t *)(v_stack_p60) = v_stack_p10;
    goto loc_008B384A;
loc_008B37E0:
    local_r13 = (Arg1 + 8) + (32);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    if ((uint8_t)(v_stack_p30) == 0) goto loc_008B38B9;
    if (local_r13 == 0) goto loc_008B38CE;
loc_008B3801:
    if (*(uint64_t *)(local_r13) == 0) {
        Arg1 = *(uint64_t *)(local_r13 + 0x10);
    }
    result = SeQueryInformationToken(Arg1, 25, v_stack_p34, v_stack_p30);
    if (sign_flag) goto loc_008B3A38;
loc_008B382C:
    result = (uint32_t)(v_stack_p34);
    if (local_r13 == v_stack_mF0) {
        Arg1 = local_r13;
        result = SeReleaseSubjectContext(Arg1, 25, v_stack_p34, v_stack_p30);
        result = v_stack_p34;
    }
    if (!sign_flag) goto loc_008B3902;
loc_008B384A:
    if (v_stack_p68 != 0) goto loc_008B3A92;
loc_008B3858:
    goto loc_008B3778;
loc_008B3860:
    *(uint64_t *)(v_stack_p68) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    goto loc_008B3778;
loc_008B386D:
    v_stack_p32 = (uint16_t)(local_rdi + 2);
    result = ExAllocatePool2(256, (uint16_t)(local_rdi + 2), (uint32_t)(0x6D4E624FULL), v_stack_p30);
    if (result != 0) goto loc_008B36FD;
    goto loc_008B384A;
loc_008B389C:
    goto loc_008B384A;
loc_008B38A4:
    if (256 == 0) goto loc_008B3740;
    Arg2 = 0;
    result = ExFreePoolWithTag(256, Arg2, (uint32_t)(0x6D4E624FULL), v_stack_p30);
    goto loc_008B3740;
loc_008B38B9:
    v_stack_p34 = (uint32_t)((uint32_t)(0x5000ULL));
loc_008B38C2:
    if (((uint32_t)((uint32_t)(0x5000ULL))) < ((uint32_t)(local_rdi))) { local_rdi = (uint32_t)((uint32_t)(0x5000ULL)); }
    Arg2 = 0;
    goto loc_008B3660;
loc_008B38CE:
    result = SeCaptureSubjectContext(v_stack_mF0, Arg2, (uint32_t)(0x6D4E624FULL), v_stack_p30);
    goto loc_008B3801;
loc_008B38E0:
    result = PsIsCurrentThreadInServerSilo(v_stack_mF0, Arg2, (uint32_t)(0x6D4E624FULL), v_stack_p30);
    if ((uint8_t)(result) != 0) goto loc_008B368A;
    goto loc_008B37B8;
loc_008B38F2:
    if (((uint32_t)(result)) == 0xC0000024ULL) goto loc_008B368A;
    goto loc_008B384A;
loc_008B3902:
    goto loc_008B38C2;
loc_008B3909:
    goto loc_008B384A;
loc_008B3914:
    result = guard_dispatch_icall(v_stack_p10, *(uint64_t *)(v_stack_p10 + 0x10), v_stack_p78, v_stack_p68);
    if (sign_flag) goto loc_008B384A;
    goto loc_008B36B4;
loc_008B3943:
loc_008B394A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x1C))))) | (0x80000000ULL));
    if (condition_is_not_equal) goto loc_008B394A;
    if (sign_flag) goto loc_008B39F6;
    v_stack_p38 = (uint32_t)(*(uint64_t *)(v_stack_p10 + 0x10));
    v_stack_p48 = v_rip + 2415288;
    Arg2 = 0;
    v_stack_p40 = 0x10000EULL;
    v_stack_p20 = 0;
    Arg3 = 0;
    result = ObQueryNameStringMode(v_stack_p10, Arg2, Arg3, v_stack_p38);
    if (((uint32_t)(result)) != 0xC0000004ULL) goto loc_008B3A45;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_p38), (uint32_t)(0x6D4E624FULL), v_stack_p38);
    if (result == 0) goto loc_008B3A45;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_p10, result, (uint32_t)(v_stack_p38), v_stack_p38);
    Arg3 = v_stack_p40;
    if (!sign_flag) { Arg3 = result; }
loc_008B39E4:
    if (result != 0) goto loc_008B3A4C;
loc_008B39F6:
    if ((uint8_t)(*(uint16_t *)(arg1 + 0x8)) == 0) goto loc_008B3672;
    goto loc_008B384A;
loc_008B3A0A:
    result = RtlIsSandboxedToken(Arg3 + 32, (uint8_t)(v_stack_p38), Arg3, v_stack_p38);
    local_r14 = (uint8_t)(*(uint16_t *)(arg1 + 0x8));
    if ((uint8_t)(result) == 0) { local_r14 = (uint32_t)(local_rdi); }
    Arg2 = 0;
    goto loc_008B3647;
loc_008B3A2E:
    goto loc_008B3778;
loc_008B3A38:
    Arg1 = 0;
    v_stack_p34 = 0;
    goto loc_008B382C;
loc_008B3A45:
    goto loc_008B39E4;
loc_008B3A4C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_p40, v_stack_p30);
    goto loc_008B39F6;
loc_008B3A58:
    goto loc_008B369A;
loc_008B3A63:
    result = HalAdjustResourceList(result, Arg2, v_stack_p40, v_stack_p30);
    *(uint64_t *)(local_rdi + 0x8) = result;
    goto loc_008B36A5;
loc_008B3A71:
    if ((*(uint16_t *)(arg7)) == 0) goto loc_008B36D4;
    if ((*(uint16_t *)(*(uint64_t *)(arg7 + 0x8))) != 92) goto loc_008B36D4;
    local_r14 = (uint32_t)((local_r14) + (-2));
    goto loc_008B36D4;
loc_008B3A92:
    result = ObfDereferenceObject(result, Arg2, v_stack_p40, v_stack_p30);
    goto loc_008B3858;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg6` | `+ 0x0` | `16` | `W` |
| `Arg6` | `+ 0x2` | `16` | `R` |
| `Arg6` | `+ 0x2` | `16` | `W` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x8` | `64` | `W` |
| `Arg7` | `+ 0x0` | `16` | `R` |
| `Arg7` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B35C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
