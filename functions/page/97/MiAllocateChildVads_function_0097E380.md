# MiAllocateChildVads

- RVA: `0x0097E380`–`0x0097E7EE` (길이 `1,134` bytes)
- VA: `0x000000014097E380`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000975A8`
- 디코드: `305`개 명령, `1,134/1,134` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0097E433` → [MiVadShouldBeForked](../../text/49/MiVadShouldBeForked_function_00495F90.md) (function, `0x00495F90`)
- `0x0097E477` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0097E491` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0097E4E1` → [MiVadHasSharedCommit](MiVadHasSharedCommit_function_0097E7F4.md) (function, `0x0097E7F4`)
- `0x0097E4F1` → [MiVadPureReserve](../../text/2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x0097E50D` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0097E530` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x0097E58D` → [MiCloneCaptureVadCommit](../../text/4B/MiCloneCaptureVadCommit_function_004B4554.md) (function, `0x004B4554`)
- `0x0097E59F` → [MiVadHasSharedCommit](MiVadHasSharedCommit_function_0097E7F4.md) (function, `0x0097E7F4`)
- `0x0097E5B5` → [MiRemoveSharedCommitNode](../88/MiRemoveSharedCommitNode_function_008889A0.md) (function, `0x008889A0`)
- `0x0097E5C9` → [MiInsertSharedCommitNode](../88/MiInsertSharedCommitNode_function_00887210.md) (function, `0x00887210`)
- `0x0097E5DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0097E606` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0097E615` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0097E649` → [MiCloneNoChange](MiCloneNoChange_function_0097E848.md) (function, `0x0097E848`)
- `0x0097E6AB` → [MiInsertChildVads](MiInsertChildVads_function_0097DBB0.md) (function, `0x0097DBB0`)
- `0x0097E6ED` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x0097E710` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x0097E73B` → [MiCreateLargePageVad](../A9/MiCreateLargePageVad_function_00A99B50.md) (function, `0x00A99B50`)
- `0x0097E75C` → [MiCloneImageVad](../../text/69/MiCloneImageVad_function_006979F8.md) (function, `0x006979F8`)
- `0x0097E77C` → [MiCloneLargeFileOnlyVad](../80/MiCloneLargeFileOnlyVad_function_00800A64.md) (function, `0x00800A64`)
- `0x0097E78E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0097E7AF` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x0097E7BC` → [MiVadHasSharedCommit](MiVadHasSharedCommit_function_0097E7F4.md) (function, `0x0097E7F4`)
- `0x0097E7D6` → [MiRemoveSharedCommitNode](../88/MiRemoveSharedCommitNode_function_008889A0.md) (function, `0x008889A0`)
- `0x0097E7E4` → [MiDeletePartialCloneVads](../81/MiDeletePartialCloneVads_function_008116E4.md) (function, `0x008116E4`)

### Direct callers
- [MiCloneProcessAddressSpace](../AD/MiCloneProcessAddressSpace_function_00AD6F7C.md) at `0x00AD7128`

### Static image references
- `0x0097E394` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x0097E433` → [MiVadShouldBeForked](../../text/49/MiVadShouldBeForked_function_00495F90.md) (`PAGE` → `.text`)
  - `0x0097E477` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0097E491` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0097E4F1` → [MiVadPureReserve](../../text/2C/MiVadPureReserve_function_002C34C0.md) (`PAGE` → `.text`)
  - `0x0097E50D` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
  - `0x0097E530` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (`PAGE` → `.text`)
  - `0x0097E58D` → [MiCloneCaptureVadCommit](../../text/4B/MiCloneCaptureVadCommit_function_004B4554.md) (`PAGE` → `.text`)
  - `0x0097E5DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0097E606` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0097E615` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0097E6ED` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x0097E710` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x0097E75C` → [MiCloneImageVad](../../text/69/MiCloneImageVad_function_006979F8.md) (`PAGE` → `.text`)
  - `0x0097E78E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0097E7AF` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x0097E6DD` → [sub_00B2A0A2](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E6F8` → [sub_00B2A0A2](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E700` → [sub_00B2A0A2 + 0x17](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E71B` → [sub_00B2A0A2 + 0x17](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E762` → [sub_00B2A0A2 + 0x54](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E782` → [sub_00B2A0A2 + 0x54](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E7C3` → [sub_00B2A0A2 + 0x63](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)
  - `0x0097E7DC` → [sub_00B2A0A2 + 0x63](../B2/Unknown_function_00B2A0A2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0097E380  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0097E385  55                              push rbp
0097E386  56                              push rsi
0097E387  57                              push rdi
0097E388  41 54                           push r12
0097E38A  41 55                           push r13
0097E38C  41 56                           push r14
0097E38E  41 57                           push r15
0097E390  48 83 EC 60                     sub rsp, 0x60
0097E394  48 8B 05 A5 C3 48 00            mov rax, qword ptr [rip + 0x48c3a5]
0097E39B  48 33 C4                        xor rax, rsp
0097E39E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0097E3A3  48 83 22 00                     and qword ptr [rdx], 0
0097E3A7  0F 57 C0                        xorps xmm0, xmm0
0097E3AA  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0097E3AF  4C 8B F1                        mov r14, rcx
0097E3B2  45 33 E4                        xor r12d, r12d
0097E3B5  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0097E3BA  45 33 FF                        xor r15d, r15d
0097E3BD  4C 8B EA                        mov r13, rdx
0097E3C0  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0097E3C5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0097E3CE  33 F6                           xor esi, esi
0097E3D0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0097E3D7  48 8B 81 58 05 00 00            mov rax, qword ptr [rcx + 0x558]
0097E3DE  EB 06                           jmp 0x14097e3e6
0097E3E0  48 8B F0                        mov rsi, rax
0097E3E3  48 8B 00                        mov rax, qword ptr [rax]
0097E3E6  48 85 C0                        test rax, rax
0097E3E9  75 F5                           jne 0x14097e3e0
0097E3EB  48 85 F6                        test rsi, rsi
0097E3EE  0F 84 B1 02 00 00               je 0x14097e6a5
0097E3F4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0097E3F8  48 8B EE                        mov rbp, rsi
0097E3FB  48 8B CE                        mov rcx, rsi
0097E3FE  48 85 C0                        test rax, rax
0097E401  74 23                           je 0x14097e426
0097E403  48 8B 08                        mov rcx, qword ptr [rax]
0097E406  48 8B F0                        mov rsi, rax
0097E409  48 85 C9                        test rcx, rcx
0097E40C  74 22                           je 0x14097e430
0097E40E  48 8B 01                        mov rax, qword ptr [rcx]
0097E411  48 8B F1                        mov rsi, rcx
0097E414  48 8B C8                        mov rcx, rax
0097E417  48 85 C0                        test rax, rax
0097E41A  75 F2                           jne 0x14097e40e
0097E41C  EB 12                           jmp 0x14097e430
0097E41E  48 39 0E                        cmp qword ptr [rsi], rcx
0097E421  74 0D                           je 0x14097e430
0097E423  48 8B CE                        mov rcx, rsi
0097E426  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
0097E42A  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
0097E42E  75 EE                           jne 0x14097e41e
0097E430  48 8B CD                        mov rcx, rbp
0097E433  E8 58 7B B1 FF                  call 0x140495f90
0097E438  85 C0                           test eax, eax
0097E43A  74 AF                           je 0x14097e3eb
0097E43C  44 8B 45 30                     mov r8d, dword ptr [rbp + 0x30]
0097E440  41 B9 56 61 64 6C               mov r9d, 0x6c646156
0097E446  41 8B C8                        mov ecx, r8d
0097E449  81 E1 00 00 20 00               and ecx, 0x200000
0097E44F  8B C1                           mov eax, ecx
0097E451  F7 D8                           neg eax
0097E453  48 1B D2                        sbb rdx, rdx
0097E456  48 83 E2 B8                     and rdx, 0xffffffffffffffb8
0097E45A  48 81 C2 88 00 00 00            add rdx, 0x88
0097E461  48 8B FA                        mov rdi, rdx
0097E464  85 C9                           test ecx, ecx
0097E466  0F 84 EE 01 00 00               je 0x14097e65a
0097E46C  45 8B C1                        mov r8d, r9d
0097E46F  48 8B D7                        mov rdx, rdi
0097E472  B9 40 00 00 00                  mov ecx, 0x40
0097E477  E8 C4 D0 9D FF                  call 0x14035b540
0097E47C  48 8B D8                        mov rbx, rax
0097E47F  48 85 C0                        test rax, rax
0097E482  0F 84 13 03 00 00               je 0x14097e79b
0097E488  4C 8B C7                        mov r8, rdi
0097E48B  48 8B D5                        mov rdx, rbp
0097E48E  48 8B C8                        mov rcx, rax
0097E491  E8 AA 83 D4 FF                  call 0x1406c6840
0097E496  0F BA 65 30 15                  bt dword ptr [rbp + 0x30], 0x15
0097E49B  48 8D 53 30                     lea rdx, [rbx + 0x30]
0097E49F  0F 83 8E 01 00 00               jae 0x14097e633
0097E4A5  83 22 F7                        and dword ptr [rdx], 0xfffffff7
0097E4A8  83 22 FE                        and dword ptr [rdx], 0xfffffffe
0097E4AB  83 22 FD                        and dword ptr [rdx], 0xfffffffd
0097E4AE  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
0097E4B2  83 E0 0F                        and eax, 0xf
0097E4B5  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
0097E4B9  C7 43 24 00 00 00 00            mov dword ptr [rbx + 0x24], 0
0097E4C0  48 83 63 28 00                  and qword ptr [rbx + 0x28], 0
0097E4C5  48 83 63 08 00                  and qword ptr [rbx + 8], 0
0097E4CA  8B 0A                           mov ecx, dword ptr [rdx]
0097E4CC  0F BA E1 15                     bt ecx, 0x15
0097E4D0  0F 83 DF 01 00 00               jae 0x14097e6b5
0097E4D6  48 8B CD                        mov rcx, rbp
0097E4D9  48 C7 43 10 FE FF FF FF         mov qword ptr [rbx + 0x10], 0xfffffffffffffffe
0097E4E1  E8 0E 03 00 00                  call 0x14097e7f4
0097E4E6  85 C0                           test eax, eax
0097E4E8  0F 85 CE 00 00 00               jne 0x14097e5bc
0097E4EE  48 8B CB                        mov rcx, rbx
0097E4F1  E8 CA 4F 94 FF                  call 0x1402c34c0
0097E4F6  85 C0                           test eax, eax
0097E4F8  75 6F                           jne 0x14097e569
0097E4FA  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0097E4FD  A8 08                           test al, 8
0097E4FF  0F 85 3E 01 00 00               jne 0x14097e643
0097E505  BA 80 00 00 00                  mov edx, 0x80
0097E50A  48 8B CD                        mov rcx, rbp
0097E50D  E8 FA 94 92 FF                  call 0x1402a7a0c
0097E512  48 85 C0                        test rax, rax
0097E515  0F 85 BF 01 00 00               jne 0x14097e6da
0097E51B  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0097E51E  B9 00 00 60 00                  mov ecx, 0x600000
0097E523  23 C1                           and eax, ecx
0097E525  3B C1                           cmp eax, ecx
0097E527  0F 84 D0 01 00 00               je 0x14097e6fd
0097E52D  48 8B CD                        mov rcx, rbp
0097E530  E8 EB 11 9B FF                  call 0x14032f720
0097E535  85 C0                           test eax, eax
0097E537  0F 85 E3 01 00 00               jne 0x14097e720
0097E53D  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0097E540  83 E0 70                        and eax, 0x70
0097E543  83 F8 20                        cmp eax, 0x20
0097E546  0F 84 07 02 00 00               je 0x14097e753
0097E54C  83 F8 50                        cmp eax, 0x50
0097E54F  0F 84 12 02 00 00               je 0x14097e767
0097E555  45 85 FF                        test r15d, r15d
0097E558  0F 85 29 02 00 00               jne 0x14097e787
0097E55E  4C 89 23                        mov qword ptr [rbx], r12
0097E561  4C 8B E3                        mov r12, rbx
0097E564  E9 82 FE FF FF                  jmp 0x14097e3eb
0097E569  8B 4B 34                        mov ecx, dword ptr [rbx + 0x34]
0097E56C  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
0097E576  0F B6 53 22                     movzx edx, byte ptr [rbx + 0x22]
0097E57A  48 C1 E2 20                     shl rdx, 0x20
0097E57E  48 0B D1                        or rdx, rcx
0097E581  48 3B D0                        cmp rdx, rax
0097E584  0F 83 70 FF FF FF               jae 0x14097e4fa
0097E58A  48 8B CB                        mov rcx, rbx
0097E58D  E8 C2 5F B3 FF                  call 0x1404b4554
0097E592  8B F8                           mov edi, eax
0097E594  85 C0                           test eax, eax
0097E596  0F 89 5E FF FF FF               jns 0x14097e4fa
0097E59C  48 8B CB                        mov rcx, rbx
0097E59F  E8 50 02 00 00                  call 0x14097e7f4
0097E5A4  85 C0                           test eax, eax
0097E5A6  74 30                           je 0x14097e5d8
0097E5A8  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
0097E5AC  45 33 C0                        xor r8d, r8d
0097E5AF  49 8B D6                        mov rdx, r14
0097E5B2  48 8B 09                        mov rcx, qword ptr [rcx]
0097E5B5  E8 E6 A3 F0 FF                  call 0x1408889a0
0097E5BA  EB 1C                           jmp 0x14097e5d8
0097E5BC  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0097E5C0  45 33 C0                        xor r8d, r8d
0097E5C3  49 8B D6                        mov rdx, r14
0097E5C6  48 8B 08                        mov rcx, qword ptr [rax]
0097E5C9  E8 42 8C F0 FF                  call 0x140887210
0097E5CE  8B F8                           mov edi, eax
0097E5D0  85 C0                           test eax, eax
0097E5D2  0F 89 16 FF FF FF               jns 0x14097e4ee
0097E5D8  33 D2                           xor edx, edx
0097E5DA  48 8B CB                        mov rcx, rbx
0097E5DD  E8 8E 42 20 00                  call 0x140b82870
0097E5E2  33 DB                           xor ebx, ebx
0097E5E4  45 85 FF                        test r15d, r15d
0097E5E7  0F 84 B8 01 00 00               je 0x14097e7a5
0097E5ED  48 85 DB                        test rbx, rbx
0097E5F0  0F 85 C3 01 00 00               jne 0x14097e7b9
0097E5F6  4D 85 E4                        test r12, r12
0097E5F9  0F 85 E2 01 00 00               jne 0x14097e7e1
0097E5FF  33 D2                           xor edx, edx
0097E601  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0097E606  E8 25 97 89 FF                  call 0x140217d30
0097E60B  8B C7                           mov eax, edi
0097E60D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0097E612  48 33 CC                        xor rcx, rsp
0097E615  E8 26 E0 D2 FF                  call 0x1406ac640
0097E61A  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0097E622  48 83 C4 60                     add rsp, 0x60
0097E626  41 5F                           pop r15
0097E628  41 5E                           pop r14
0097E62A  41 5D                           pop r13
0097E62C  41 5C                           pop r12
0097E62E  5F                              pop rdi
0097E62F  5E                              pop rsi
0097E630  5D                              pop rbp
0097E631  C3                              ret
0097E632  CC                              int3
0097E633  49 8B C6                        mov rax, r14
0097E636  48 83 C8 01                     or rax, 1
0097E63A  48 89 43 70                     mov qword ptr [rbx + 0x70], rax
0097E63E  E9 65 FE FF FF                  jmp 0x14097e4a8
0097E643  48 8B D3                        mov rdx, rbx
0097E646  48 8B CD                        mov rcx, rbp
0097E649  E8 FA 01 00 00                  call 0x14097e848
0097E64E  8B F8                           mov edi, eax
0097E650  85 C0                           test eax, eax
0097E652  0F 89 AD FE FF FF               jns 0x14097e505
0097E658  EB 8A                           jmp 0x14097e5e4
0097E65A  41 8B C0                        mov eax, r8d
0097E65D  24 70                           and al, 0x70
0097E65F  3C 20                           cmp al, 0x20
0097E661  0F 85 05 FE FF FF               jne 0x14097e46c
0097E667  41 0F BA E0 16                  bt r8d, 0x16
0097E66C  0F 83 FA FD FF FF               jae 0x14097e46c
0097E672  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0097E676  41 B9 56 61 64 49               mov r9d, 0x49646156
0097E67C  48 8B 08                        mov rcx, qword ptr [rax]
0097E67F  48 8B 01                        mov rax, qword ptr [rcx]
0097E682  8B 48 08                        mov ecx, dword ptr [rax + 8]
0097E685  8B C1                           mov eax, ecx
0097E687  24 3F                           and al, 0x3f
0097E689  F6 D8                           neg al
0097E68B  48 1B FF                        sbb rdi, rdi
0097E68E  48 C1 E9 06                     shr rcx, 6
0097E692  48 F7 DF                        neg rdi
0097E695  48 83 C7 15                     add rdi, 0x15
0097E699  48 03 F9                        add rdi, rcx
0097E69C  48 C1 E7 03                     shl rdi, 3
0097E6A0  E9 C7 FD FF FF                  jmp 0x14097e46c
0097E6A5  49 8B D4                        mov rdx, r12
0097E6A8  49 8B CE                        mov rcx, r14
0097E6AB  E8 00 F5 FF FF                  call 0x14097dbb0
0097E6B0  E9 58 FF FF FF                  jmp 0x14097e60d
0097E6B5  8B C1                           mov eax, ecx
0097E6B7  24 70                           and al, 0x70
0097E6B9  3C 20                           cmp al, 0x20
0097E6BB  0F 85 15 FE FF FF               jne 0x14097e4d6
0097E6C1  F7 C1 00 00 80 01               test ecx, 0x1800000
0097E6C7  0F 84 09 FE FF FF               je 0x14097e4d6
0097E6CD  81 E1 FF FF 7F FE               and ecx, 0xfe7fffff
0097E6D3  89 0A                           mov dword ptr [rdx], ecx
0097E6D5  E9 FC FD FF FF                  jmp 0x14097e4d6
0097E6DA  45 85 FF                        test r15d, r15d
0097E6DD  0F 85 BF B9 1A 00               jne 0x140b2a0a2
0097E6E3  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
0097E6E8  33 D2                           xor edx, edx
0097E6EA  49 8B CE                        mov rcx, r14
0097E6ED  E8 2E 81 89 FF                  call 0x140216820
0097E6F2  41 BF 01 00 00 00               mov r15d, 1
0097E6F8  E9 A5 B9 1A 00                  jmp 0x140b2a0a2
0097E6FD  45 85 FF                        test r15d, r15d
0097E700  0F 85 B3 B9 1A 00               jne 0x140b2a0b9
0097E706  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
0097E70B  33 D2                           xor edx, edx
0097E70D  49 8B CE                        mov rcx, r14
0097E710  E8 0B 81 89 FF                  call 0x140216820
0097E715  41 BF 01 00 00 00               mov r15d, 1
0097E71B  E9 99 B9 1A 00                  jmp 0x140b2a0b9
0097E720  8B 4D 34                        mov ecx, dword ptr [rbp + 0x34]
0097E723  41 B9 01 00 00 00               mov r9d, 1
0097E729  8A 45 22                        mov al, byte ptr [rbp + 0x22]
0097E72C  45 33 C0                        xor r8d, r8d
0097E72F  89 4B 34                        mov dword ptr [rbx + 0x34], ecx
0097E732  48 8B D3                        mov rdx, rbx
0097E735  49 8B CE                        mov rcx, r14
0097E738  88 43 22                        mov byte ptr [rbx + 0x22], al
0097E73B  E8 10 B4 11 00                  call 0x140a99b50
0097E740  8B F8                           mov edi, eax
0097E742  85 C0                           test eax, eax
0097E744  0F 88 9A FE FF FF               js 0x14097e5e4
0097E74A  49 FF 45 00                     inc qword ptr [r13]
0097E74E  E9 02 FE FF FF                  jmp 0x14097e555
0097E753  4C 8B C5                        mov r8, rbp
0097E756  48 8B D3                        mov rdx, rbx
0097E759  49 8B CE                        mov rcx, r14
0097E75C  E8 97 92 D1 FF                  call 0x1406979f8
0097E761  90                              nop
0097E762  E9 8F B9 1A 00                  jmp 0x140b2a0f6
0097E767  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0097E76B  48 8B 08                        mov rcx, qword ptr [rax]
0097E76E  48 83 79 40 00                  cmp qword ptr [rcx + 0x40], 0
0097E773  0F 84 DC FD FF FF               je 0x14097e555
0097E779  48 8B CD                        mov rcx, rbp
0097E77C  E8 E3 22 E8 FF                  call 0x140800a64
0097E781  90                              nop
0097E782  E9 6F B9 1A 00                  jmp 0x140b2a0f6
0097E787  33 D2                           xor edx, edx
0097E789  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0097E78E  E8 9D 95 89 FF                  call 0x140217d30
0097E793  45 33 FF                        xor r15d, r15d
0097E796  E9 C3 FD FF FF                  jmp 0x14097e55e
0097E79B  BF 9A 00 00 C0                  mov edi, 0xc000009a
0097E7A0  E9 3F FE FF FF                  jmp 0x14097e5e4
0097E7A5  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
0097E7AA  33 D2                           xor edx, edx
0097E7AC  49 8B CE                        mov rcx, r14
0097E7AF  E8 6C 80 89 FF                  call 0x140216820
0097E7B4  E9 34 FE FF FF                  jmp 0x14097e5ed
0097E7B9  48 8B CB                        mov rcx, rbx
0097E7BC  E8 33 00 00 00                  call 0x14097e7f4
0097E7C1  85 C0                           test eax, eax
0097E7C3  0F 84 3C B9 1A 00               je 0x140b2a105
0097E7C9  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
0097E7CD  45 33 C0                        xor r8d, r8d
0097E7D0  49 8B D6                        mov rdx, r14
0097E7D3  48 8B 09                        mov rcx, qword ptr [rcx]
0097E7D6  E8 C5 A1 F0 FF                  call 0x1408889a0
0097E7DB  90                              nop
0097E7DC  E9 24 B9 1A 00                  jmp 0x140b2a105
0097E7E1  49 8B CC                        mov rcx, r12
0097E7E4  E8 FB 2E E9 FF                  call 0x1408116e4
0097E7E9  E9 11 FE FF FF                  jmp 0x14097e5ff
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateChildVads(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 4768677)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm0;
    v_r12 = 0;
    v_stack_m68 = v_xmm0;
    v_r15 = 0;
    v_stack_m58 = v_xmm0;
    v_rsi = 0;
    goto loc_0097E3E6;
loc_0097E3E0:
loc_0097E3E6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) != 0) goto loc_0097E3E0;
loc_0097E3EB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) == 0) goto loc_0097E6A5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8) == 0) goto loc_0097E426;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8)) == 0) goto loc_0097E430;
loc_0097E40E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8))) != 0) goto loc_0097E40E;
    goto loc_0097E430;
loc_0097E41E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8))))) goto loc_0097E430;
loc_0097E426:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0097E41E;
loc_0097E430:
    result = MiVadShouldBeForked(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0097E3EB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 48))))) & (0x200000ULL));
    result = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    a2 = (a2) & (-72);
    a2 = (a2) + (136);
    if ((unsigned int)(a1) == 0) goto loc_0097E65A;
loc_0097E46C:
    result = MiAllocatePool(64, a2, (unsigned int)((unsigned int)((unsigned int)(0x6C646156ULL))), (unsigned int)(0x6C646156ULL));
    if (result == 0) goto loc_0097E79B;
    result = memcpy(result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), a2, (unsigned int)(0x6C646156ULL));
    if (condition_is_above_or_equal) goto loc_0097E633;
loc_0097E4A8:
    result = (unsigned int)((*(unsigned __int64 *)(result + 56)) & (15));
    *(unsigned __int64 *)(result + 56) = result;
    *(unsigned int *)(result + 36) = 0;
    if (condition_is_above_or_equal) goto loc_0097E6B5;
loc_0097E4D6:
    *(unsigned __int64 *)(result + 16) = -2;
    result = MiVadHasSharedCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), result + 48, a2, (unsigned int)(0x6C646156ULL));
    if ((unsigned int)(result) != 0) goto loc_0097E5BC;
loc_0097E4EE:
    result = MiVadPureReserve(result, result + 48, a2, (unsigned int)(0x6C646156ULL));
    if ((unsigned int)(result) != 0) goto loc_0097E569;
loc_0097E4FA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 48)))) & (8)) != 0) goto loc_0097E643;
loc_0097E505:
    result = MiLocateLockedVadEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), 128, a2, (unsigned int)(0x6C646156ULL));
    if (result != 0) goto loc_0097E6DA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 48))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x600000ULL)))) goto loc_0097E6FD;
    result = MiIsVadLargePrivate(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), 128, a2, (unsigned int)(0x6C646156ULL));
    if ((unsigned int)(result) != 0) goto loc_0097E720;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 48))) & (112));
    if (((unsigned int)(result)) == 32) goto loc_0097E753;
    if (((unsigned int)(result)) == 80) goto loc_0097E767;
loc_0097E555:
    if (0 != 0) goto loc_0097E787;
loc_0097E55E:
    *(unsigned __int64 *)(result) = 0;
    goto loc_0097E3EB;
loc_0097E569:
    a2 = (*(unsigned __int8 *)(result + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 52)));
    if (a2 >= result) goto loc_0097E4FA;
    result = MiCloneCaptureVadCommit(result, a2, a2, (unsigned int)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E4FA;
    result = MiVadHasSharedCommit(result, a2, a2, (unsigned int)(0x6C646156ULL));
    if ((unsigned int)(result) == 0) goto loc_0097E5D8;
    a3 = 0;
    result = MiRemoveSharedCommitNode(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)), a1, a3, (unsigned int)(0x6C646156ULL));
    goto loc_0097E5D8;
loc_0097E5BC:
    a3 = 0;
    result = MiInsertSharedCommitNode(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 72)), a1, a3, (unsigned int)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E4EE;
loc_0097E5D8:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, (unsigned int)(0x6C646156ULL));
    v_rbx = 0;
loc_0097E5E4:
    if (0 == 0) goto loc_0097E7A5;
loc_0097E5ED:
    if (0 != 0) goto loc_0097E7B9;
    if (result != 0) goto loc_0097E7E1;
loc_0097E5FF:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m78, a2, a3, (unsigned int)(0x6C646156ULL));
loc_0097E60D:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(0x6C646156ULL));
    v_rsp = (v_rsp) + (96);
    return result;
loc_0097E633:
    result = (a1) | (1);
    *(unsigned __int64 *)(v_stack_p18 + 112) = result;
    goto loc_0097E4A8;
loc_0097E643:
    result = MiCloneNoChange(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), v_stack_p18, a3, (unsigned int)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E505;
    goto loc_0097E5E4;
loc_0097E65A:
    result = (unsigned __int8)((0) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_0097E46C;
    if (((unsigned __int8)(result)) >= 32) goto loc_0097E46C;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 72))) + 8))))) & (63));
    result = (unsigned __int8)(-(result));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 72))) + 8))) >> (6);
    v_rdi = -((unsigned int)((unsigned int)(result)));
    v_rdi = (v_rdi) + (21);
    v_rdi = (v_rdi) + (a1);
    v_rdi = (v_rdi) << (3);
    goto loc_0097E46C;
loc_0097E6A5:
    result = MiInsertChildVads(a1, result, a3, (unsigned int)(0x49646156ULL));
    goto loc_0097E60D;
loc_0097E6B5:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(a1))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_0097E4D6;
    if ((((unsigned int)(a1)) & (0x1800000ULL)) == 0) goto loc_0097E4D6;
    a1 = (unsigned int)((a1) & (0xFE7FFFFFULL));
    *(unsigned int *)(result) = (unsigned int)(a1);
    goto loc_0097E4D6;
loc_0097E6DA:
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, v_stack_p20, (unsigned int)(0x49646156ULL));
loc_0097E6FD:
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, v_stack_p20, (unsigned int)(0x49646156ULL));
loc_0097E720:
    a3 = 0;
    *(unsigned int *)(v_stack_p18 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 52)));
    *(unsigned __int8 *)(v_stack_p18 + 34) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 34));
    result = MiCreateLargePageVad(a1, v_stack_p18, a3, 1);
    if (sign_flag) goto loc_0097E5E4;
    goto loc_0097E555;
loc_0097E753:
    result = MiCloneImageVad(a1, v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), 1);
loc_0097E767:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 72)) + 64)) == 0) goto loc_0097E555;
    result = MiCloneLargeFileOnlyVad(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), v_stack_p18, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), 1);
loc_0097E787:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_p20, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), 1);
    v_r15 = 0;
    goto loc_0097E55E;
loc_0097E79B:
    goto loc_0097E5E4;
loc_0097E7A5:
    a2 = 0;
    result = KiStackAttachProcess(a1, a2, v_stack_p20, 1);
    goto loc_0097E5ED;
loc_0097E7B9:
    result = MiVadHasSharedCommit(v_stack_p18, a2, v_stack_p20, 1);
    a3 = 0;
    result = MiRemoveSharedCommitNode(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 72)), a1, a3, 1);
loc_0097E7E1:
    result = MiDeletePartialCloneVads(result, a1, a3, 1);
    goto loc_0097E5FF;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateChildVads(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x48C3A5)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m78 = v_xmm0;
    local_r12 = 0;
    v_stack_m68 = v_xmm0;
    local_r15 = 0;
    v_stack_m58 = v_xmm0;
    local_rsi = 0;
    goto loc_0097E3E6;
loc_0097E3E0:
loc_0097E3E6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) != 0) goto loc_0097E3E0;
loc_0097E3EB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) == 0) goto loc_0097E6A5;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8) == 0) goto loc_0097E426;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8)) == 0) goto loc_0097E430;
loc_0097E40E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8))) != 0) goto loc_0097E40E;
    goto loc_0097E430;
loc_0097E41E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8))))) goto loc_0097E430;
loc_0097E426:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0097E41E;
loc_0097E430:
    result = MiVadShouldBeForked(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0097E3EB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x30))))) & (0x200000ULL));
    result = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    Arg2 = (Arg2) & (-72);
    Arg2 = (Arg2) + (136);
    if ((uint32_t)(Arg1) == 0) goto loc_0097E65A;
loc_0097E46C:
    result = MiAllocatePool(64, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x6C646156ULL))), (uint32_t)(0x6C646156ULL));
    if (result == 0) goto loc_0097E79B;
    result = memcpy(result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), Arg2, (uint32_t)(0x6C646156ULL));
    if (condition_is_above_or_equal) goto loc_0097E633;
loc_0097E4A8:
    result = (uint32_t)((*(uint64_t *)(result + 0x38)) & (15));
    *(uint64_t *)(result + 0x38) = result;
    *(uint32_t *)(result + 0x24) = 0;
    if (condition_is_above_or_equal) goto loc_0097E6B5;
loc_0097E4D6:
    *(uint64_t *)(result + 0x10) = -2;
    result = MiVadHasSharedCommit(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), result + 48, Arg2, (uint32_t)(0x6C646156ULL));
    if ((uint32_t)(result) != 0) goto loc_0097E5BC;
loc_0097E4EE:
    result = MiVadPureReserve(result, result + 48, Arg2, (uint32_t)(0x6C646156ULL));
    if ((uint32_t)(result) != 0) goto loc_0097E569;
loc_0097E4FA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x30)))) & (8)) != 0) goto loc_0097E643;
loc_0097E505:
    result = MiLocateLockedVadEvent(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), 128, Arg2, (uint32_t)(0x6C646156ULL));
    if (result != 0) goto loc_0097E6DA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x30))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x600000ULL)))) goto loc_0097E6FD;
    result = MiIsVadLargePrivate(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), 128, Arg2, (uint32_t)(0x6C646156ULL));
    if ((uint32_t)(result) != 0) goto loc_0097E720;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x30))) & (112));
    if (((uint32_t)(result)) == 32) goto loc_0097E753;
    if (((uint32_t)(result)) == 80) goto loc_0097E767;
loc_0097E555:
    if (0 != 0) goto loc_0097E787;
loc_0097E55E:
    *(uint64_t *)(result) = 0;
    goto loc_0097E3EB;
loc_0097E569:
    Arg2 = (*(uint8_t *)(result + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x34)));
    if (Arg2 >= result) goto loc_0097E4FA;
    result = MiCloneCaptureVadCommit(result, Arg2, Arg2, (uint32_t)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E4FA;
    result = MiVadHasSharedCommit(result, Arg2, Arg2, (uint32_t)(0x6C646156ULL));
    if ((uint32_t)(result) == 0) goto loc_0097E5D8;
    a3 = 0;
    result = MiRemoveSharedCommitNode(*(uint64_t *)(*(uint64_t *)(result + 0x48)), Arg1, a3, (uint32_t)(0x6C646156ULL));
    goto loc_0097E5D8;
loc_0097E5BC:
    a3 = 0;
    result = MiInsertSharedCommitNode(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x48)), Arg1, a3, (uint32_t)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E4EE;
loc_0097E5D8:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, (uint32_t)(0x6C646156ULL));
    local_rbx = 0;
loc_0097E5E4:
    if (0 == 0) goto loc_0097E7A5;
loc_0097E5ED:
    if (0 != 0) goto loc_0097E7B9;
    if (result != 0) goto loc_0097E7E1;
loc_0097E5FF:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m78, Arg2, a3, (uint32_t)(0x6C646156ULL));
loc_0097E60D:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, (uint32_t)(0x6C646156ULL));
    local_rsp = (local_rsp) + (96);
    return result;
loc_0097E633:
    result = (Arg1) | (1);
    *(uint64_t *)(v_stack_p18 + 0x70) = result;
    goto loc_0097E4A8;
loc_0097E643:
    result = MiCloneNoChange(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), v_stack_p18, a3, (uint32_t)(0x6C646156ULL));
    if (!sign_flag) goto loc_0097E505;
    goto loc_0097E5E4;
loc_0097E65A:
    result = (uint8_t)((0) & (112));
    if (((uint8_t)(result)) != 32) goto loc_0097E46C;
    if (((uint8_t)(result)) >= 32) goto loc_0097E46C;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x48))) + 0x8))))) & (63));
    result = (uint8_t)(-(result));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x48))) + 0x8))) >> (6);
    local_rdi = -((uint32_t)((uint32_t)(result)));
    local_rdi = (local_rdi) + (21);
    local_rdi = (local_rdi) + (Arg1);
    local_rdi = (local_rdi) << (3);
    goto loc_0097E46C;
loc_0097E6A5:
    result = MiInsertChildVads(Arg1, result, a3, (uint32_t)(0x49646156ULL));
    goto loc_0097E60D;
loc_0097E6B5:
    result = (uint8_t)(((uint32_t)((uint32_t)(Arg1))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_0097E4D6;
    if ((((uint32_t)(Arg1)) & (0x1800000ULL)) == 0) goto loc_0097E4D6;
    Arg1 = (uint32_t)((Arg1) & (0xFE7FFFFFULL));
    *(uint32_t *)(result) = (uint32_t)(Arg1);
    goto loc_0097E4D6;
loc_0097E6DA:
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, v_stack_p20, (uint32_t)(0x49646156ULL));
loc_0097E6FD:
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, v_stack_p20, (uint32_t)(0x49646156ULL));
loc_0097E720:
    a3 = 0;
    *(uint32_t *)(v_stack_p18 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x34)));
    *(uint8_t *)(v_stack_p18 + 0x22) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x22));
    result = MiCreateLargePageVad(Arg1, v_stack_p18, a3, 1);
    if (sign_flag) goto loc_0097E5E4;
    goto loc_0097E555;
loc_0097E753:
    result = MiCloneImageVad(Arg1, v_stack_p18, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), 1);
loc_0097E767:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x48)) + 0x40)) == 0) goto loc_0097E555;
    result = MiCloneLargeFileOnlyVad(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), v_stack_p18, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), 1);
loc_0097E787:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_p20, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), 1);
    local_r15 = 0;
    goto loc_0097E55E;
loc_0097E79B:
    goto loc_0097E5E4;
loc_0097E7A5:
    Arg2 = 0;
    result = KiStackAttachProcess(Arg1, Arg2, v_stack_p20, 1);
    goto loc_0097E5ED;
loc_0097E7B9:
    result = MiVadHasSharedCommit(v_stack_p18, Arg2, v_stack_p20, 1);
    a3 = 0;
    result = MiRemoveSharedCommitNode(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x48)), Arg1, a3, 1);
loc_0097E7E1:
    result = MiDeletePartialCloneVads(result, Arg1, a3, 1);
    goto loc_0097E5FF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097E380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
