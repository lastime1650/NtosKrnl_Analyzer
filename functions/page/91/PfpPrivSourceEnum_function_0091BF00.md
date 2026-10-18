# PfpPrivSourceEnum

- RVA: `0x0091BF00`–`0x0091C58C` (길이 `1,676` bytes)
- VA: `0x000000014091BF00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B0D0`
- 디코드: `385`개 명령, `1,676/1,676` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0091BF4C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091BFAB` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x0091C01C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0091C039` → [ExGetNextProcess](ExGetNextProcess_function_0091CAD0.md) (function, `0x0091CAD0`)
- `0x0091C04E` → [PsGetNextProcess](PsGetNextProcess_function_0091C900.md) (function, `0x0091C900`)
- `0x0091C0DE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091C14D` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x0091C164` → [MmQuerySystemMemoryInformation](../../text/3B/MmQuerySystemMemoryInformation_function_003B98C8.md) (function, `0x003B98C8`)
- `0x0091C1A8` → [PfpPrivSourceAdd](PfpPrivSourceAdd_function_0091CA58.md) (function, `0x0091CA58`)
- `0x0091C1BD` → [ExGetNextProcess](ExGetNextProcess_function_0091CAD0.md) (function, `0x0091CAD0`)
- `0x0091C1E0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091C291` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0091C2A5` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x0091C2B7` → [SeSecurityAttributePresent](../../text/21/SeSecurityAttributePresent_function_00213660.md) (function, `0x00213660`)
- `0x0091C2CF` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x0091C2D7` → [SmStoreExistsForProcess](../../text/34/SmStoreExistsForProcess_function_00349F54.md) (function, `0x00349F54`)
- `0x0091C330` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0091C351` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0091C390` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (function, `0x00263950`)
- `0x0091C434` → [PfpPrivSourceAdd](PfpPrivSourceAdd_function_0091CA58.md) (function, `0x0091CA58`)
- `0x0091C446` → [ExGetNextProcess](ExGetNextProcess_function_0091CAD0.md) (function, `0x0091CAD0`)
- `0x0091C45B` → [MmQueryProcessWorkingSetSwapPages](../../text/2A/MmQueryProcessWorkingSetSwapPages_function_002A49BC.md) (function, `0x002A49BC`)
- `0x0091C47E` → [SmProcessQueryStoreStats](SmProcessQueryStoreStats_function_0091D324.md) (function, `0x0091D324`)
- `0x0091C4D1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0091C52A` → [SeIsAppContainerOrIdentifyLevelContext](../A2/SeIsAppContainerOrIdentifyLevelContext_function_00A21A74.md) (function, `0x00A21A74`)
- `0x0091C582` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [PfQuerySuperfetchInformation](../90/PfQuerySuperfetchInformation_function_0090210C.md) at `0x00902298`

### Static image references
- `0x0091BF15` → RVA `0x00E0A740` (`.data`; read)
- `0x0091C015` → RVA `0x00FD9B08` (`PAGEDATA`; read)
- `0x0091C0FB` → RVA `0x00B01500` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0091C2AD` → RVA `0x00B4BEA8` (`PspSysAppIdClaim`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x0091BF4C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091C0DE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091C14D` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x0091C164` → [MmQuerySystemMemoryInformation](../../text/3B/MmQuerySystemMemoryInformation_function_003B98C8.md) (`PAGE` → `.text`)
  - `0x0091C1E0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091C291` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0091C2A5` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x0091C2B7` → [SeSecurityAttributePresent](../../text/21/SeSecurityAttributePresent_function_00213660.md) (`PAGE` → `.text`)
  - `0x0091C2CF` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x0091C2D7` → [SmStoreExistsForProcess](../../text/34/SmStoreExistsForProcess_function_00349F54.md) (`PAGE` → `.text`)
  - `0x0091C330` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0091C351` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0091C390` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (`PAGE` → `.text`)
  - `0x0091C45B` → [MmQueryProcessWorkingSetSwapPages](../../text/2A/MmQueryProcessWorkingSetSwapPages_function_002A49BC.md) (`PAGE` → `.text`)
  - `0x0091C4D1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0091C582` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0091BF00  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0091BF05  57                              push rdi
0091BF06  41 54                           push r12
0091BF08  41 55                           push r13
0091BF0A  41 56                           push r14
0091BF0C  41 57                           push r15
0091BF0E  48 81 EC C0 01 00 00            sub rsp, 0x1c0
0091BF15  48 8B 05 24 E8 4E 00            mov rax, qword ptr [rip + 0x4ee824]
0091BF1C  48 33 C4                        xor rax, rsp
0091BF1F  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
0091BF27  49 8B C0                        mov rax, r8
0091BF2A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0091BF2F  8A DA                           mov bl, dl
0091BF31  4C 8B E9                        mov r13, rcx
0091BF34  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0091BF39  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0091BF3E  33 D2                           xor edx, edx
0091BF40  44 8D 42 40                     lea r8d, [rdx + 0x40]
0091BF44  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
0091BF4C  E8 EF AC DA FF                  call 0x1406c6c40
0091BF51  0F 57 C0                        xorps xmm0, xmm0
0091BF54  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
0091BF5C  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
0091BF64  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0091BF69  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
0091BF6F  33 C0                           xor eax, eax
0091BF71  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0091BF76  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0091BF7B  45 33 F6                        xor r14d, r14d
0091BF7E  4C 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r14
0091BF86  45 33 FF                        xor r15d, r15d
0091BF89  49 8B 7D 10                     mov rdi, qword ptr [r13 + 0x10]
0091BF8D  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
0091BF91  45 8D 6E 10                     lea r13d, [r14 + 0x10]
0091BF95  41 3B C5                        cmp eax, r13d
0091BF98  0F 82 BA 05 00 00               jb 0x14091c558
0091BF9E  84 DB                           test bl, bl
0091BFA0  74 0E                           je 0x14091bfb0
0091BFA2  8B D0                           mov edx, eax
0091BFA4  45 8D 46 08                     lea r8d, [r14 + 8]
0091BFA8  48 8B CF                        mov rcx, rdi
0091BFAB  E8 10 D2 FC FF                  call 0x1408e91c0
0091BFB0  0F 10 07                        movups xmm0, xmmword ptr [rdi]
0091BFB3  F3 0F 7F 84 24 40 01 00 00      movdqu xmmword ptr [rsp + 0x140], xmm0
0091BFBC  C7 47 08 00 00 00 00            mov dword ptr [rdi + 8], 0
0091BFC3  EB 23                           jmp 0x14091bfe8
0091BFC5  8B D8                           mov ebx, eax
0091BFC7  41 BD 10 00 00 00               mov r13d, 0x10
0091BFCD  41 BC FF FF FF FF               mov r12d, 0xffffffff
0091BFD3  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
0091BFDB  45 8B FE                        mov r15d, r14d
0091BFDE  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
0091BFE3  E9 C8 04 00 00                  jmp 0x14091c4b0
0091BFE8  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
0091BFF0  83 F8 08                        cmp eax, 8
0091BFF3  0F 85 66 05 00 00               jne 0x14091c55f
0091BFF9  48 C1 E8 20                     shr rax, 0x20
0091BFFD  A9 F8 FF FF FF                  test eax, 0xfffffff8
0091C002  0F 85 57 05 00 00               jne 0x14091c55f
0091C008  83 E0 03                        and eax, 3
0091C00B  3C 03                           cmp al, 3
0091C00D  0F 84 4C 05 00 00               je 0x14091c55f
0091C013  8A D3                           mov dl, bl
0091C015  48 8B 0D EC DA 6B 00            mov rcx, qword ptr [rip + 0x6bdaec]
0091C01C  E8 FF 5D F5 FF                  call 0x140871e20
0091C021  84 C0                           test al, al
0091C023  0F 84 FA 04 00 00               je 0x14091c523
0091C029  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
0091C02E  75 05                           jne 0x14091c035
0091C030  48 FF 44 24 38                  inc qword ptr [rsp + 0x38]
0091C035  33 D2                           xor edx, edx
0091C037  33 C9                           xor ecx, ecx
0091C039  E8 92 0A 00 00                  call 0x14091cad0
0091C03E  4C 8B F0                        mov r14, rax
0091C041  48 85 C0                        test rax, rax
0091C044  74 26                           je 0x14091c06c
0091C046  48 FF 44 24 38                  inc qword ptr [rsp + 0x38]
0091C04B  49 8B CE                        mov rcx, r14
0091C04E  E8 AD 08 00 00                  call 0x14091c900
0091C053  4C 8B F0                        mov r14, rax
0091C056  48 85 C0                        test rax, rax
0091C059  74 0E                           je 0x14091c069
0091C05B  F7 80 F4 01 00 00 00 00 00 04   test dword ptr [rax + 0x1f4], 0x4000000
0091C065  75 DF                           jne 0x14091c046
0091C067  EB E2                           jmp 0x14091c04b
0091C069  45 33 F6                        xor r14d, r14d
0091C06C  41 BC FF FF FF FF               mov r12d, 0xffffffff
0091C072  4C 39 64 24 38                  cmp qword ptr [rsp + 0x38], r12
0091C077  0F 87 E9 04 00 00               ja 0x14091c566
0091C07D  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0091C082  48 8D 0C 40                     lea rcx, [rax + rax*2]
0091C086  48 C1 E1 05                     shl rcx, 5
0091C08A  49 03 CD                        add rcx, r13
0091C08D  49 3B CC                        cmp rcx, r12
0091C090  0F 87 D0 04 00 00               ja 0x14091c566
0091C096  44 8B F9                        mov r15d, ecx
0091C099  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0091C09E  8B 40 18                        mov eax, dword ptr [rax + 0x18]
0091C0A1  3B C8                           cmp ecx, eax
0091C0A3  0F 87 47 04 00 00               ja 0x14091c4f0
0091C0A9  83 C0 F0                        add eax, -0x10
0091C0AC  8B C8                           mov ecx, eax
0091C0AE  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0091C0B8  48 F7 E1                        mul rcx
0091C0BB  48 C1 EA 06                     shr rdx, 6
0091C0BF  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0091C0C3  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0091C0C8  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
0091C0CD  0F 85 E4 00 00 00               jne 0x14091c1b7
0091C0D3  33 D2                           xor edx, edx
0091C0D5  44 8D 42 60                     lea r8d, [rdx + 0x60]
0091C0D9  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0091C0DE  E8 5D AB DA FF                  call 0x1406c6c40
0091C0E3  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0091C0E8  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
0091C0F0  49 8B D5                        mov rdx, r13
0091C0F3  48 8D 8C 24 A4 00 00 00         lea rcx, [rsp + 0xa4]
0091C0FB  4C 8D 0D FE 53 1E 00            lea r9, [rip + 0x1e53fe]
0091C102  48 8D 84 24 A4 00 00 00         lea rax, [rsp + 0xa4]
0091C10A  4C 2B C8                        sub r9, rax
0091C10D  48 8D 82 EE FF FF 7F            lea rax, [rdx + 0x7fffffee]
0091C114  48 85 C0                        test rax, rax
0091C117  74 13                           je 0x14091c12c
0091C119  42 8A 04 09                     mov al, byte ptr [rcx + r9]
0091C11D  84 C0                           test al, al
0091C11F  74 0B                           je 0x14091c12c
0091C121  88 01                           mov byte ptr [rcx], al
0091C123  48 FF C1                        inc rcx
0091C126  48 83 EA 01                     sub rdx, 1
0091C12A  75 E1                           jne 0x14091c10d
0091C12C  48 8D 41 FF                     lea rax, [rcx - 1]
0091C130  48 85 D2                        test rdx, rdx
0091C133  48 0F 45 C1                     cmovne rax, rcx
0091C137  C6 00 00                        mov byte ptr [rax], 0
0091C13A  45 33 C9                        xor r9d, r9d
0091C13D  45 8D 41 40                     lea r8d, [r9 + 0x40]
0091C141  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
0091C149  41 8D 49 77                     lea ecx, [r9 + 0x77]
0091C14D  E8 3E 16 D9 FF                  call 0x1406ad790
0091C152  8B D8                           mov ebx, eax
0091C154  85 C0                           test eax, eax
0091C156  0F 88 4F 03 00 00               js 0x14091c4ab
0091C15C  48 8D 8C 24 D8 00 00 00         lea rcx, [rsp + 0xd8]
0091C164  E8 5F D7 A9 FF                  call 0x1403b98c8
0091C169  8B D8                           mov ebx, eax
0091C16B  85 C0                           test eax, eax
0091C16D  0F 88 38 03 00 00               js 0x14091c4ab
0091C173  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
0091C17B  48 C1 E9 0C                     shr rcx, 0xc
0091C17F  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0091C187  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0091C18F  48 3B C1                        cmp rax, rcx
0091C192  48 0F 46 C1                     cmovbe rax, rcx
0091C196  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0091C19E  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0091C1A3  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0091C1A8  E8 AB 08 00 00                  call 0x14091ca58
0091C1AD  8B D8                           mov ebx, eax
0091C1AF  85 C0                           test eax, eax
0091C1B1  0F 88 F4 02 00 00               js 0x14091c4ab
0091C1B7  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
0091C1BB  33 C9                           xor ecx, ecx
0091C1BD  E8 0E 09 00 00                  call 0x14091cad0
0091C1C2  8B BC 24 44 01 00 00            mov edi, dword ptr [rsp + 0x144]
0091C1C9  4C 8B F0                        mov r14, rax
0091C1CC  48 85 C0                        test rax, rax
0091C1CF  0F 84 C5 02 00 00               je 0x14091c49a
0091C1D5  33 D2                           xor edx, edx
0091C1D7  44 8D 42 60                     lea r8d, [rdx + 0x60]
0091C1DB  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0091C1E0  E8 5B AA DA FF                  call 0x1406c6c40
0091C1E5  40 F6 C7 04                     test dil, 4
0091C1E9  0F 85 73 02 00 00               jne 0x14091c462
0091C1EF  C7 44 24 70 02 00 00 00         mov dword ptr [rsp + 0x70], 2
0091C1F7  41 8B 96 D0 01 00 00            mov edx, dword ptr [r14 + 0x1d0]
0091C1FE  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
0091C202  41 8B 86 84 03 00 00            mov eax, dword ptr [r14 + 0x384]
0091C209  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0091C20D  49 8B 8E F8 01 00 00            mov rcx, qword ptr [r14 + 0x1f8]
0091C214  49 33 8E D0 01 00 00            xor rcx, qword ptr [r14 + 0x1d0]
0091C21B  48 B8 FF FF FF FF FF FF FF 1F   movabs rax, 0x1fffffffffffffff
0091C225  48 23 C8                        and rcx, rax
0091C228  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
0091C230  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0091C238  49 8B 86 98 04 00 00            mov rax, qword ptr [r14 + 0x498]
0091C23F  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0091C247  49 8B 86 90 04 00 00            mov rax, qword ptr [r14 + 0x490]
0091C24E  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0091C256  48 3B C8                        cmp rcx, rax
0091C259  0F 87 EC 02 00 00               ja 0x14091c54b
0091C25F  49 8B 86 90 04 00 00            mov rax, qword ptr [r14 + 0x490]
0091C266  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0091C26E  49 8B 86 88 02 00 00            mov rax, qword ptr [r14 + 0x288]
0091C275  48 3B 84 24 90 00 00 00         cmp rax, qword ptr [rsp + 0x90]
0091C27D  48 0F 46 84 24 90 00 00 00      cmovbe rax, qword ptr [rsp + 0x90]
0091C286  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0091C28E  49 8B CE                        mov rcx, r14
0091C291  E8 5A 36 91 FF                  call 0x14022f8f0
0091C296  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
0091C29D  BA 44 66 6C 74                  mov edx, 0x746c6644
0091C2A2  49 8B CE                        mov rcx, r14
0091C2A5  E8 D6 3C 8F FF                  call 0x14020ff80
0091C2AA  48 8B F8                        mov rdi, rax
0091C2AD  48 8D 15 F4 FB 22 00            lea rdx, [rip + 0x22fbf4]
0091C2B4  48 8B C8                        mov rcx, rax
0091C2B7  E8 A4 73 8F FF                  call 0x140213660
0091C2BC  0F B6 D8                        movzx ebx, al
0091C2BF  49 8D 8E 48 02 00 00            lea rcx, [r14 + 0x248]
0091C2C6  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0091C2CC  48 8B D7                        mov rdx, rdi
0091C2CF  E8 1C 13 AD FF                  call 0x1403ed5f0
0091C2D4  49 8B CE                        mov rcx, r14
0091C2D7  E8 78 DC A2 FF                  call 0x140349f54
0091C2DC  49 8B 8E 70 06 00 00            mov rcx, qword ptr [r14 + 0x670]
0091C2E3  48 F7 D9                        neg rcx
0091C2E6  1B D2                           sbb edx, edx
0091C2E8  41 23 D5                        and edx, r13d
0091C2EB  83 E0 01                        and eax, 1
0091C2EE  C1 E0 03                        shl eax, 3
0091C2F1  0B D0                           or edx, eax
0091C2F3  83 E3 01                        and ebx, 1
0091C2F6  0B D3                           or edx, ebx
0091C2F8  8B 84 24 CC 00 00 00            mov eax, dword ptr [rsp + 0xcc]
0091C2FF  83 E0 E6                        and eax, 0xffffffe6
0091C302  0B D0                           or edx, eax
0091C304  89 94 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], edx
0091C30B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0091C314  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0091C319  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0091C320  90                              nop
0091C321  49 8D BE C8 01 00 00            lea rdi, [r14 + 0x1c8]
0091C328  45 33 C0                        xor r8d, r8d
0091C32B  33 D2                           xor edx, edx
0091C32D  48 8B CF                        mov rcx, rdi
0091C330  E8 FB 3E 8F FF                  call 0x140210230
0091C335  48 8B D8                        mov rbx, rax
0091C338  B9 11 00 00 00                  mov ecx, 0x11
0091C33D  33 C0                           xor eax, eax
0091C33F  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0091C344  74 10                           je 0x14091c356
0091C346  4C 8B CF                        mov r9, rdi
0091C349  4C 8B C3                        mov r8, rbx
0091C34C  33 D2                           xor edx, edx
0091C34E  48 8B CF                        mov rcx, rdi
0091C351  E8 F6 40 8F FF                  call 0x14021044c
0091C356  48 85 DB                        test rbx, rbx
0091C359  74 04                           je 0x14091c35f
0091C35B  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0091C35F  49 8B 9E 30 06 00 00            mov rbx, qword ptr [r14 + 0x630]
0091C366  48 BA 08 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000008
0091C370  49 B8 B0 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003b0
0091C37A  49 8B 08                        mov rcx, qword ptr [r8]
0091C37D  48 8B 02                        mov rax, qword ptr [rdx]
0091C380  49 8B 00                        mov rax, qword ptr [r8]
0091C383  48 3B C8                        cmp rcx, rax
0091C386  75 F2                           jne 0x14091c37a
0091C388  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0091C38D  49 8B CE                        mov rcx, r14
0091C390  E8 BB 75 94 FF                  call 0x140263950
0091C395  48 85 DB                        test rbx, rbx
0091C398  74 20                           je 0x14091c3ba
0091C39A  83 8C 24 CC 00 00 00 02         or dword ptr [rsp + 0xcc], 2
0091C3A2  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
0091C3AC  48 F7 E3                        mul rbx
0091C3AF  48 C1 EA 0B                     shr rdx, 0xb
0091C3B3  89 94 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edx
0091C3BA  41 8A 86 BA 04 00 00            mov al, byte ptr [r14 + 0x4ba]
0091C3C1  3C 02                           cmp al, 2
0091C3C3  75 08                           jne 0x14091c3cd
0091C3C5  83 8C 24 CC 00 00 00 04         or dword ptr [rsp + 0xcc], 4
0091C3CD  49 8B D5                        mov rdx, r13
0091C3D0  48 8D 8C 24 A4 00 00 00         lea rcx, [rsp + 0xa4]
0091C3D8  48 8D 84 24 A4 00 00 00         lea rax, [rsp + 0xa4]
0091C3E0  4D 8B C6                        mov r8, r14
0091C3E3  4C 2B C0                        sub r8, rax
0091C3E6  48 8D 82 EE FF FF 7F            lea rax, [rdx + 0x7fffffee]
0091C3ED  48 85 C0                        test rax, rax
0091C3F0  74 17                           je 0x14091c409
0091C3F2  42 8A 84 01 38 03 00 00         mov al, byte ptr [rcx + r8 + 0x338]
0091C3FA  84 C0                           test al, al
0091C3FC  74 0B                           je 0x14091c409
0091C3FE  88 01                           mov byte ptr [rcx], al
0091C400  48 FF C1                        inc rcx
0091C403  48 83 EA 01                     sub rdx, 1
0091C407  75 DD                           jne 0x14091c3e6
0091C409  48 8D 41 FF                     lea rax, [rcx - 1]
0091C40D  48 85 D2                        test rdx, rdx
0091C410  48 0F 45 C1                     cmovne rax, rcx
0091C414  C6 00 00                        mov byte ptr [rax], 0
0091C417  8B BC 24 44 01 00 00            mov edi, dword ptr [rsp + 0x144]
0091C41E  40 F6 C7 01                     test dil, 1
0091C422  75 2C                           jne 0x14091c450
0091C424  40 F6 C7 02                     test dil, 2
0091C428  75 49                           jne 0x14091c473
0091C42A  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0091C42F  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0091C434  E8 1F 06 00 00                  call 0x14091ca58
0091C439  8B D8                           mov ebx, eax
0091C43B  85 C0                           test eax, eax
0091C43D  78 6C                           js 0x14091c4ab
0091C43F  8A 54 24 20                     mov dl, byte ptr [rsp + 0x20]
0091C443  49 8B CE                        mov rcx, r14
0091C446  E8 85 06 00 00                  call 0x14091cad0
0091C44B  E9 79 FD FF FF                  jmp 0x14091c1c9
0091C450  48 8D 94 24 B8 00 00 00         lea rdx, [rsp + 0xb8]
0091C458  49 8B CE                        mov rcx, r14
0091C45B  E8 5C 85 98 FF                  call 0x1402a49bc
0091C460  EB C8                           jmp 0x14091c42a
0091C462  41 8B 86 FC 05 00 00            mov eax, dword ptr [r14 + 0x5fc]
0091C469  A8 01                           test al, 1
0091C46B  0F 84 7E FD FF FF               je 0x14091c1ef
0091C471  EB CC                           jmp 0x14091c43f
0091C473  45 33 C0                        xor r8d, r8d
0091C476  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0091C47B  49 8B CE                        mov rcx, r14
0091C47E  E8 A1 0E 00 00                  call 0x14091d324
0091C483  85 C0                           test eax, eax
0091C485  78 A3                           js 0x14091c42a
0091C487  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0091C48C  48 C1 E8 0C                     shr rax, 0xc
0091C490  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0091C498  EB 90                           jmp 0x14091c42a
0091C49A  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0091C49E  44 8D 3C 40                     lea r15d, [rax + rax*2]
0091C4A2  41 C1 E7 05                     shl r15d, 5
0091C4A6  45 03 FD                        add r15d, r13d
0091C4A9  33 DB                           xor ebx, ebx
0091C4AB  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
0091C4B0  4D 85 F6                        test r14, r14
0091C4B3  0F 85 C1 00 00 00               jne 0x14091c57a
0091C4B9  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
0091C4BF  74 36                           je 0x14091c4f7
0091C4C1  44 89 3F                        mov dword ptr [rdi], r15d
0091C4C4  8B C3                           mov eax, ebx
0091C4C6  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
0091C4CE  48 33 CC                        xor rcx, rsp
0091C4D1  E8 6A 01 D9 FF                  call 0x1406ac640
0091C4D6  48 8B 9C 24 F8 01 00 00         mov rbx, qword ptr [rsp + 0x1f8]
0091C4DE  48 81 C4 C0 01 00 00            add rsp, 0x1c0
0091C4E5  41 5F                           pop r15
0091C4E7  41 5E                           pop r14
0091C4E9  41 5D                           pop r13
0091C4EB  41 5C                           pop r12
0091C4ED  5F                              pop rdi
0091C4EE  C3                              ret
0091C4EF  CC                              int3
0091C4F0  BB 23 00 00 C0                  mov ebx, 0xc0000023
0091C4F5  EB B4                           jmp 0x14091c4ab
0091C4F7  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
0091C4FB  FF C1                           inc ecx
0091C4FD  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0091C502  48 3B C8                        cmp rcx, rax
0091C505  48 0F 47 C1                     cmova rax, rcx
0091C509  4C 8D 3C 40                     lea r15, [rax + rax*2]
0091C50D  49 C1 E7 05                     shl r15, 5
0091C511  4D 03 FD                        add r15, r13
0091C514  4D 3B FC                        cmp r15, r12
0091C517  76 A8                           jbe 0x14091c4c1
0091C519  45 33 FF                        xor r15d, r15d
0091C51C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0091C521  EB 9E                           jmp 0x14091c4c1
0091C523  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0091C528  33 C9                           xor ecx, ecx
0091C52A  E8 45 55 10 00                  call 0x140a21a74
0091C52F  8B D8                           mov ebx, eax
0091C531  3D A5 00 00 C0                  cmp eax, 0xc00000a5
0091C536  74 38                           je 0x14091c570
0091C538  85 C0                           test eax, eax
0091C53A  0F 89 E9 FA FF FF               jns 0x14091c029
0091C540  41 BC FF FF FF FF               mov r12d, 0xffffffff
0091C546  E9 60 FF FF FF                  jmp 0x14091c4ab
0091C54B  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
0091C553  E9 16 FD FF FF                  jmp 0x14091c26e
0091C558  BB 23 00 00 C0                  mov ebx, 0xc0000023
0091C55D  EB E1                           jmp 0x14091c540
0091C55F  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0091C564  EB DA                           jmp 0x14091c540
0091C566  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0091C56B  E9 3B FF FF FF                  jmp 0x14091c4ab
0091C570  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0091C575  E9 BB FA FF FF                  jmp 0x14091c035
0091C57A  BA 50 73 45 6E                  mov edx, 0x6e457350
0091C57F  49 8B CE                        mov rcx, r14
0091C582  E8 59 B3 9D FF                  call 0x1402f78e0
0091C587  E9 2D FF FF FF                  jmp 0x14091c4b9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpPrivSourceEnum(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A4;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_pC0;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 5171236)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1C0 = a3;
    v_stack_m198 = a1;
    v_stack_m188 = a3;
    a2 = 0;
    result = memset(v_stack_mE8, a2, a2 + 64, a4);
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    v_stack_m1C8 = 0;
    result = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = 0;
    v_r14 = 0;
    v_stack_m118 = 0;
    v_r15 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))) < ((unsigned int)(v_r14 + 16))) goto loc_0091C558;
    result = (unsigned int)(*(unsigned int *)(a1 + 24));
    if ((unsigned __int8)((unsigned __int8)(a2)) != 0) {
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
        a3 = v_r14 + 8;
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    v_stack_mA8 = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 8) = 0;
    goto loc_0091BFE8;
loc_0091BFE8:
    if (((unsigned int)(v_stack_mA8)) != 8) goto loc_0091C55F;
    result = (v_stack_mA8) >> (32);
    if ((((unsigned int)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_0091C55F;
    result = (unsigned int)((result) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_0091C55F;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 7068396), (unsigned __int8)((unsigned __int8)(a2)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0091C523;
loc_0091C029:
    if (v_stack_m1C8 == 0) {
    }
    a2 = 0;
    a1 = 0;
    result = ExGetNextProcess(a1, a2, a3, a4);
    if (result == 0) goto loc_0091C06C;
loc_0091C046:
loc_0091C04B:
    result = PsGetNextProcess(result, a2, a3, a4);
    if (result == 0) goto loc_0091C069;
    if (((*(unsigned int *)(result + 500)) & (0x4000000ULL)) != 0) goto loc_0091C046;
    goto loc_0091C04B;
loc_0091C069:
    v_r14 = 0;
loc_0091C06C:
    if (v_stack_m1B0 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0091C566;
    a1 = (v_stack_m1B0 + v_stack_m1B0 * 2) << (5);
    a1 = (a1) + (v_r14 + 16);
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0091C566;
    if (((unsigned int)(a1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m198 + 24))))) goto loc_0091C4F0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m198 + 24))) + (-16));
    a2 = (a2) >> (6);
    v_stack_m1A4 = a2;
    v_stack_m1B8 = *(unsigned __int64 *)(a1 + 16);
    if (v_stack_m1C8 != 0) goto loc_0091C1B7;
    a2 = 0;
    result = memset(v_stack_m178, a2, a2 + 96, a4);
    v_stack_m174 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m160 = (unsigned int)(0xFFFFFFFFULL);
    a4 = (v_rip + 1987582) - (v_stack_m144);
loc_0091C10D:
    if (v_r14 + 16 + 2147483630 == 0) goto loc_0091C12C;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m144 + a4 * 1)) == 0) goto loc_0091C12C;
    *(unsigned __int8 *)(v_stack_m144) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m144 + a4 * 1));
    a1 = (v_stack_m144) + 1;
    a2 = (v_r14 + 16) - (1);
    if (condition_is_not_equal) goto loc_0091C10D;
loc_0091C12C:
    result = a1 - 1;
    if (a2 != 0) { result = a1; }
    *(unsigned __int8 *)(result) = 0;
    a4 = 0;
    result = ZwQuerySystemInformation(a4 + 119, v_stack_mE8, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
    result = MmQuerySystemMemoryInformation(v_stack_m110, v_stack_mE8, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
    a1 = (v_stack_mE8) >> (12);
    v_stack_m158 = a1;
    result = v_stack_m110;
    if (v_stack_m110 <= a1) { result = a1; }
    v_stack_m150 = result;
    result = PfpPrivSourceAdd(v_stack_m1B8, v_stack_m178, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
loc_0091C1B7:
    a1 = 0;
    result = ExGetNextProcess(a1, v_stack_m1C8, a4 + 64, a4);
loc_0091C1C9:
    if (result == 0) goto loc_0091C49A;
    a2 = 0;
    result = memset(v_stack_m178, a2, a2 + 96, a4);
    if ((((unsigned __int8)((unsigned int)(v_stack_mA4))) & (4)) != 0) goto loc_0091C462;
loc_0091C1EF:
    v_stack_m178 = 2;
    v_stack_m174 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 464)));
    v_stack_m170 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 900)));
    a1 = (*(unsigned __int64 *)(result + 504)) ^ (*(unsigned __int64 *)(result + 464));
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(result + 900)));
    v_stack_m168 = a1;
    v_stack_m160 = (unsigned int)(*(unsigned int *)(result + 464));
    v_stack_m158 = *(unsigned __int64 *)(result + 1176);
    if (v_stack_m158 > (*(unsigned __int64 *)(result + 1168))) goto loc_0091C54B;
    v_stack_m128 = *(unsigned __int64 *)(result + 1168);
loc_0091C26E:
    result = *(unsigned __int64 *)(result + 648);
    if ((*(unsigned __int64 *)(result + 648)) <= v_stack_m158) { result = v_stack_m158; }
    v_stack_m150 = result;
    result = PsGetProcessSessionIdEx(result, (unsigned int)(*(unsigned int *)(result + 464)), a2 + 96, a4);
    v_stack_m148 = (unsigned int)(result);
    result = PsReferencePrimaryTokenWithTag(result, (unsigned int)(0x746C6644ULL), a2 + 96, a4);
    result = SeSecurityAttributePresent(result, v_rip + 2292724, a2 + 96, a4);
    result = ObFastDereferenceObject(result + 584, result, (unsigned int)(0x746C6644ULL), a4);
    result = SmStoreExistsForProcess(result, result, (unsigned int)(0x746C6644ULL), a4);
    a1 = -(*(unsigned __int64 *)(result + 1648));
    a2 = (unsigned int)((result) & ((unsigned int)(v_r14 + 16)));
    result = (unsigned int)((result) & (1));
    result = (unsigned int)((result) << (3));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    v_rbx = (unsigned int)(((unsigned __int8)(result)) & (1));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_rbx)));
    result = (unsigned int)(((unsigned int)(v_stack_m11C)) & (0xFFFFFFE6ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    v_stack_m11C = a2;
    v_stack_m198 = *(unsigned __int64 *)(gs_base + (0 + 392));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 456, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 456;
        a3 = 0;
        a2 = 0;
        a1 = result + 456;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_0091C37A:
    if ((*(unsigned __int64 *)(a3)) != (*(unsigned __int64 *)(a3))) goto loc_0091C37A;
    result = PspUnlockProcessShared(result, v_stack_m198, a3, a4);
    if (*(unsigned __int64 *)(result + 1584) != 0) {
        a2 = (v_stack_m198) >> (11);
        v_stack_m120 = a2;
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 1210))) == 2) {
    }
    a3 = (result) - (v_stack_m144);
loc_0091C3E6:
    if (v_r14 + 16 + 2147483630 == 0) goto loc_0091C409;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m144 + a3 * 1 + 824)) == 0) goto loc_0091C409;
    *(unsigned __int8 *)(v_stack_m144) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m144 + a3 * 1 + 824));
    a1 = (v_stack_m144) + 1;
    a2 = (v_r14 + 16) - (1);
    if (condition_is_not_equal) goto loc_0091C3E6;
loc_0091C409:
    result = a1 - 1;
    if (a2 != 0) { result = a1; }
    *(unsigned __int8 *)(result) = 0;
    if ((((unsigned __int8)((unsigned int)(v_stack_mA4))) & (1)) != 0) goto loc_0091C450;
    if ((((unsigned __int8)((unsigned int)(v_stack_mA4))) & (2)) != 0) goto loc_0091C473;
loc_0091C42A:
    result = PfpPrivSourceAdd(v_stack_m1B8, v_stack_m178, a3, a4);
    if (sign_flag) goto loc_0091C4AB;
loc_0091C43F:
    result = ExGetNextProcess(result, v_stack_m1C8, a3, a4);
    goto loc_0091C1C9;
loc_0091C450:
    result = MmQueryProcessWorkingSetSwapPages(result, v_stack_m130, a3, a4);
    goto loc_0091C42A;
loc_0091C462:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 1532)))) & (1)) == 0) goto loc_0091C1EF;
    goto loc_0091C43F;
loc_0091C473:
    a3 = 0;
    result = SmProcessQueryStoreStats(result, v_stack_m190, a3, a4);
    if (sign_flag) goto loc_0091C42A;
    result = (v_stack_m190) >> (12);
    v_stack_m130 = result;
    goto loc_0091C42A;
loc_0091C49A:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m1A8) + (unsigned int)(v_stack_m1A8) * 2) << (5));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_r14 + 16)));
    v_rbx = 0;
loc_0091C4AB:
loc_0091C4B0:
    if (result != 0) goto loc_0091C57A;
loc_0091C4B9:
    if (0 == 0xC0000023ULL) goto loc_0091C4F7;
loc_0091C4C1:
    *(unsigned int *)(v_stack_m1C0) = (unsigned int)(v_r15);
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m190, a3, a4);
    v_rsp = (v_rsp) + (448);
    return result;
loc_0091C4F0:
    goto loc_0091C4AB;
loc_0091C4F7:
    a1 = (unsigned int)(((unsigned int)(v_stack_p40)) + 1);
    result = v_stack_p38;
    if (a1 > v_stack_p38) { result = a1; }
    v_r15 = (result + result * 2) << (5);
    v_r15 = (v_r15) + (v_r14 + 16);
    if (v_r15 <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_0091C4C1;
    v_r15 = 0;
    goto loc_0091C4C1;
loc_0091C523:
    a1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(a1, v_stack_p20, a3, a4);
    if (((unsigned int)(result)) == 0xC00000A5ULL) goto loc_0091C570;
    if (!sign_flag) goto loc_0091C029;
loc_0091C540:
    goto loc_0091C4AB;
loc_0091C54B:
    v_stack_pC0 = 0;
    goto loc_0091C26E;
loc_0091C558:
    goto loc_0091C540;
loc_0091C55F:
    goto loc_0091C540;
loc_0091C566:
    goto loc_0091C4AB;
loc_0091C570:
    v_stack_p20 = 1;
    goto loc_0091C035;
loc_0091C57A:
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x6E457350ULL), a3, a4);
    goto loc_0091C4B9;
}
```

## 5. (Beta) C Style

```c
int64_t PfpPrivSourceEnum(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A4;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m38;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_pC0;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x4EE824)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1C0 = Arg3;
    v_stack_m198 = Arg1;
    v_stack_m188 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, Arg2 + 64, a4);
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    v_stack_m1C8 = 0;
    result = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = 0;
    local_r14 = 0;
    v_stack_m118 = 0;
    local_r15 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) < ((uint32_t)(local_r14 + 16))) goto loc_0091C558;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x18));
    if ((uint8_t)((uint8_t)(Arg2)) != 0) {
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
        Arg3 = local_r14 + 8;
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = ProbeForWrite(Arg1, Arg2, Arg3, a4);
    }
    v_stack_mA8 = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) = 0;
    goto loc_0091BFE8;
loc_0091BFE8:
    if (((uint32_t)(v_stack_mA8)) != 8) goto loc_0091C55F;
    result = (v_stack_mA8) >> (32);
    if ((((uint32_t)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_0091C55F;
    result = (uint32_t)((result) & (3));
    if (((uint8_t)(result)) == 3) goto loc_0091C55F;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x6BDAEC), (uint8_t)((uint8_t)(Arg2)), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0091C523;
loc_0091C029:
    if (v_stack_m1C8 == 0) {
    }
    Arg2 = 0;
    Arg1 = 0;
    result = ExGetNextProcess(Arg1, Arg2, Arg3, a4);
    if (result == 0) goto loc_0091C06C;
loc_0091C046:
loc_0091C04B:
    result = PsGetNextProcess(result, Arg2, Arg3, a4);
    if (result == 0) goto loc_0091C069;
    if (((*(uint32_t *)(result + 0x1F4)) & (0x4000000ULL)) != 0) goto loc_0091C046;
    goto loc_0091C04B;
loc_0091C069:
    local_r14 = 0;
loc_0091C06C:
    if (v_stack_m1B0 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0091C566;
    Arg1 = (v_stack_m1B0 + v_stack_m1B0 * 2) << (5);
    Arg1 = (Arg1) + (local_r14 + 16);
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0091C566;
    if (((uint32_t)(Arg1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x18))))) goto loc_0091C4F0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x18))) + (-16));
    Arg2 = (Arg2) >> (6);
    v_stack_m1A4 = Arg2;
    v_stack_m1B8 = *(uint64_t *)(arg1 + 0x10);
    if (v_stack_m1C8 != 0) goto loc_0091C1B7;
    Arg2 = 0;
    result = memset(v_stack_m178, Arg2, Arg2 + 96, a4);
    v_stack_m174 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m160 = (uint32_t)(0xFFFFFFFFULL);
    a4 = (v_rip + 1987582) - (v_stack_m144);
loc_0091C10D:
    if (local_r14 + 16 + 2147483630 == 0) goto loc_0091C12C;
    if ((uint8_t)(*(uint8_t *)(v_stack_m144 + a4 * 1)) == 0) goto loc_0091C12C;
    *(uint8_t *)(v_stack_m144) = (uint8_t)(*(uint8_t *)(v_stack_m144 + a4 * 1));
    Arg1 = (v_stack_m144) + 1;
    Arg2 = (local_r14 + 16) - (1);
    if (condition_is_not_equal) goto loc_0091C10D;
loc_0091C12C:
    result = Arg1 - 1;
    if (Arg2 != 0) { result = Arg1; }
    *(uint8_t *)(result) = 0;
    a4 = 0;
    result = ZwQuerySystemInformation(a4 + 119, v_stack_mE8, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
    result = MmQuerySystemMemoryInformation(v_stack_m110, v_stack_mE8, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
    Arg1 = (v_stack_mE8) >> (12);
    v_stack_m158 = Arg1;
    result = v_stack_m110;
    if (v_stack_m110 <= Arg1) { result = Arg1; }
    v_stack_m150 = result;
    result = PfpPrivSourceAdd(v_stack_m1B8, v_stack_m178, a4 + 64, a4);
    if (sign_flag) goto loc_0091C4AB;
loc_0091C1B7:
    Arg1 = 0;
    result = ExGetNextProcess(Arg1, v_stack_m1C8, a4 + 64, a4);
loc_0091C1C9:
    if (result == 0) goto loc_0091C49A;
    Arg2 = 0;
    result = memset(v_stack_m178, Arg2, Arg2 + 96, a4);
    if ((((uint8_t)((uint32_t)(v_stack_mA4))) & (4)) != 0) goto loc_0091C462;
loc_0091C1EF:
    v_stack_m178 = 2;
    v_stack_m174 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1D0)));
    v_stack_m170 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x384)));
    Arg1 = (*(uint64_t *)(result + 0x1F8)) ^ (*(uint64_t *)(result + 0x1D0));
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(result + 0x384)));
    v_stack_m168 = Arg1;
    v_stack_m160 = (uint32_t)(*(uint32_t *)(result + 0x1D0));
    v_stack_m158 = *(uint64_t *)(result + 0x498);
    if (v_stack_m158 > (*(uint64_t *)(result + 0x490))) goto loc_0091C54B;
    v_stack_m128 = *(uint64_t *)(result + 0x490);
loc_0091C26E:
    result = *(uint64_t *)(result + 0x288);
    if ((*(uint64_t *)(result + 0x288)) <= v_stack_m158) { result = v_stack_m158; }
    v_stack_m150 = result;
    result = PsGetProcessSessionIdEx(result, (uint32_t)(*(uint32_t *)(result + 0x1D0)), Arg2 + 96, a4);
    v_stack_m148 = (uint32_t)(result);
    result = PsReferencePrimaryTokenWithTag(result, (uint32_t)(0x746C6644ULL), Arg2 + 96, a4);
    result = SeSecurityAttributePresent(result, v_rip + 2292724, Arg2 + 96, a4);
    result = ObFastDereferenceObject(result + 584, result, (uint32_t)(0x746C6644ULL), a4);
    result = SmStoreExistsForProcess(result, result, (uint32_t)(0x746C6644ULL), a4);
    Arg1 = -(*(uint64_t *)(result + 0x670));
    Arg2 = (uint32_t)((result) & ((uint32_t)(local_r14 + 16)));
    result = (uint32_t)((result) & (1));
    result = (uint32_t)((result) << (3));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    local_rbx = (uint32_t)(((uint8_t)(result)) & (1));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_rbx)));
    result = (uint32_t)(((uint32_t)(v_stack_m11C)) & (0xFFFFFFE6ULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    v_stack_m11C = Arg2;
    v_stack_m198 = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 456, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 456;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 456;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_0091C37A:
    if ((*(uint64_t *)(Arg3)) != (*(uint64_t *)(Arg3))) goto loc_0091C37A;
    result = PspUnlockProcessShared(result, v_stack_m198, Arg3, a4);
    if (*(uint64_t *)(result + 0x630) != 0) {
        Arg2 = (v_stack_m198) >> (11);
        v_stack_m120 = Arg2;
    }
    if (((uint8_t)(*(uint8_t *)(result + 0x4BA))) == 2) {
    }
    Arg3 = (result) - (v_stack_m144);
loc_0091C3E6:
    if (local_r14 + 16 + 2147483630 == 0) goto loc_0091C409;
    if ((uint8_t)(*(uint8_t *)(v_stack_m144 + Arg3 * 1 + 0x338)) == 0) goto loc_0091C409;
    *(uint8_t *)(v_stack_m144) = (uint8_t)(*(uint8_t *)(v_stack_m144 + Arg3 * 1 + 0x338));
    Arg1 = (v_stack_m144) + 1;
    Arg2 = (local_r14 + 16) - (1);
    if (condition_is_not_equal) goto loc_0091C3E6;
loc_0091C409:
    result = Arg1 - 1;
    if (Arg2 != 0) { result = Arg1; }
    *(uint8_t *)(result) = 0;
    if ((((uint8_t)((uint32_t)(v_stack_mA4))) & (1)) != 0) goto loc_0091C450;
    if ((((uint8_t)((uint32_t)(v_stack_mA4))) & (2)) != 0) goto loc_0091C473;
loc_0091C42A:
    result = PfpPrivSourceAdd(v_stack_m1B8, v_stack_m178, Arg3, a4);
    if (sign_flag) goto loc_0091C4AB;
loc_0091C43F:
    result = ExGetNextProcess(result, v_stack_m1C8, Arg3, a4);
    goto loc_0091C1C9;
loc_0091C450:
    result = MmQueryProcessWorkingSetSwapPages(result, v_stack_m130, Arg3, a4);
    goto loc_0091C42A;
loc_0091C462:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x5FC)))) & (1)) == 0) goto loc_0091C1EF;
    goto loc_0091C43F;
loc_0091C473:
    Arg3 = 0;
    result = SmProcessQueryStoreStats(result, v_stack_m190, Arg3, a4);
    if (sign_flag) goto loc_0091C42A;
    result = (v_stack_m190) >> (12);
    v_stack_m130 = result;
    goto loc_0091C42A;
loc_0091C49A:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m1A8) + (uint32_t)(v_stack_m1A8) * 2) << (5));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_r14 + 16)));
    local_rbx = 0;
loc_0091C4AB:
loc_0091C4B0:
    if (result != 0) goto loc_0091C57A;
loc_0091C4B9:
    if (0 == 0xC0000023ULL) goto loc_0091C4F7;
loc_0091C4C1:
    *(uint32_t *)(v_stack_m1C0) = (uint32_t)(local_r15);
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m190, Arg3, a4);
    local_rsp = (local_rsp) + (448);
    return result;
loc_0091C4F0:
    goto loc_0091C4AB;
loc_0091C4F7:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p40)) + 1);
    result = v_stack_p38;
    if (Arg1 > v_stack_p38) { result = Arg1; }
    local_r15 = (result + result * 2) << (5);
    local_r15 = (local_r15) + (local_r14 + 16);
    if (local_r15 <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_0091C4C1;
    local_r15 = 0;
    goto loc_0091C4C1;
loc_0091C523:
    Arg1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(Arg1, v_stack_p20, Arg3, a4);
    if (((uint32_t)(result)) == 0xC00000A5ULL) goto loc_0091C570;
    if (!sign_flag) goto loc_0091C029;
loc_0091C540:
    goto loc_0091C4AB;
loc_0091C54B:
    v_stack_pC0 = 0;
    goto loc_0091C26E;
loc_0091C558:
    goto loc_0091C540;
loc_0091C55F:
    goto loc_0091C540;
loc_0091C566:
    goto loc_0091C4AB;
loc_0091C570:
    v_stack_p20 = 1;
    goto loc_0091C035;
loc_0091C57A:
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x6E457350ULL), Arg3, a4);
    goto loc_0091C4B9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091BF00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
