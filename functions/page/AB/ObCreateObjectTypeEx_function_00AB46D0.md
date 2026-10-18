# ObCreateObjectTypeEx

- RVA: `0x00AB46D0`–`0x00AB4D24` (길이 `1,620` bytes)
- VA: `0x0000000140AB46D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCC24`
- 디코드: `412`개 명령, `1,620/1,620` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00AB472C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AB482A` → [ObpLockDirectoryExclusive](../99/ObpLockDirectoryExclusive_function_0099F24C.md) (function, `0x0099F24C`)
- `0x00AB483A` → [ObpLookupDirectoryEntry](../85/ObpLookupDirectoryEntry_function_0085D5B0.md) (function, `0x0085D5B0`)
- `0x00AB485B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AB4874` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00AB4892` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x00AB4912` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AB4956` → [ObpAllocateObject](../89/ObpAllocateObject_function_00899FF0.md) (function, `0x00899FF0`)
- `0x00AB4966` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00AB4972` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB499F` → [ObpInitObjectTypeSD](../74/ObpInitObjectTypeSD_function_0074F1B8.md) (function, `0x0074F1B8`)
- `0x00AB49AF` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00AB49B7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AB4A0F` → [RtlUnicodeToMultiByteSize](../90/RtlUnicodeToMultiByteSize_function_0090D110.md) (function, `0x0090D110`)
- `0x00AB4A3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AB4A55` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AB4A78` → [RtlUnicodeStringToAnsiString](../90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (function, `0x0090D1F0`)
- `0x00AB4AC9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB4B07` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AB4B22` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AB4BD5` → [ObpLockObjectTypeExclusive](../9D/ObpLockObjectTypeExclusive_function_009DB5C4.md) (function, `0x009DB5C4`)
- `0x00AB4C3D` → [ObpUnlockObjectType](../9D/ObpUnlockObjectType_function_009DB54C.md) (function, `0x009DB54C`)
- `0x00AB4C75` → [ObpInsertDirectoryEntry](../A1/ObpInsertDirectoryEntry_function_00A18AC0.md) (function, `0x00A18AC0`)
- `0x00AB4CB0` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00AB4CCC` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00AB4CD4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AB4CE9` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00AB4CFE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ObCreateObjectType](../70/ObCreateObjectType_function_00705230.md) at `0x0070523C`
- [AlpcpInitSystem](../74/AlpcpInitSystem_function_0074CB9C.md) at `0x0074CCDF`
- [TtmiInitTerminals](../77/TtmiInitTerminals_function_0077CA40.md) at `0x0077CBAD`
- [TtmiInitQueues](../77/TtmiInitQueues_function_0077DB68.md) at `0x0077DC8A`
- [EtwpInitializePrivateSessionDemuxObject](../7B/EtwpInitializePrivateSessionDemuxObject_function_007BC7E4.md) at `0x007BC887`
- [CmpInitializeLightWeightTransactionType](../7E/CmpInitializeLightWeightTransactionType_function_007EE204.md) at `0x007EE2B7`
- [VRegSetup](../83/VRegSetup_function_0083AE90.md) at `0x0083B049`
- [IoCreateObjectTypes](../../init/C2/IoCreateObjectTypes_function_00C2A854.md) at `0x00C2AB70`

### Static image references
- `0x00AB46F4` → RVA `0x00E0A740` (`.data`; read)
- `0x00AB4813` → RVA `0x00F0F648` (`.data`; read)
- `0x00AB4897` → RVA `0x00F0F660` (`.data`; read)
- `0x00AB498B` → RVA `0x00FC41A0` (`.data`; read)
- `0x00AB49DB` → RVA `0x00F0F660` (`.data`; write)
- `0x00AB4B4A` → RVA `0x00FC42C0` (`.data`; read)
- `0x00AB4B85` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x00AB4BBD` → RVA `0x00F0F5A0` (`.data`; read)
- `0x00AB4C04` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00AB4CDE` → RVA `0x00B01430` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00AB472C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AB485B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AB4874` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00AB4892` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x00AB4912` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AB4966` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00AB4972` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB49AF` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00AB49B7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AB4A3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AB4A55` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AB4AC9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB4B07` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AB4B22` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AB4CB0` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00AB4CCC` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00AB4CD4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AB4CE9` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
  - `0x00AB4CFE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB46D0  48 8B C4                        mov rax, rsp
00AB46D3  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
00AB46D7  55                              push rbp
00AB46D8  56                              push rsi
00AB46D9  57                              push rdi
00AB46DA  41 54                           push r12
00AB46DC  41 55                           push r13
00AB46DE  41 56                           push r14
00AB46E0  41 57                           push r15
00AB46E2  48 8D A8 D8 FE FF FF            lea rbp, [rax - 0x128]
00AB46E9  48 81 EC F0 01 00 00            sub rsp, 0x1f0
00AB46F0  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
00AB46F4  48 8B 05 45 60 35 00            mov rax, qword ptr [rip + 0x356045]
00AB46FB  48 33 C4                        xor rax, rsp
00AB46FE  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00AB4705  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
00AB470C  49 8B D9                        mov rbx, r9
00AB470F  4D 8B F8                        mov r15, r8
00AB4712  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00AB4716  48 8B FA                        mov rdi, rdx
00AB4719  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00AB471D  4C 8B F1                        mov r14, rcx
00AB4720  33 D2                           xor edx, edx
00AB4722  41 B8 E0 00 00 00               mov r8d, 0xe0
00AB4728  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00AB472C  E8 0F 25 C1 FF                  call 0x1406c6c40
00AB4731  0F 57 C0                        xorps xmm0, xmm0
00AB4734  33 C0                           xor eax, eax
00AB4736  45 33 ED                        xor r13d, r13d
00AB4739  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00AB473E  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00AB4743  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00AB4747  89 45 E8                        mov dword ptr [rbp - 0x18], eax
00AB474A  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00AB474F  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00AB4753  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00AB4757  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00AB475B  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00AB4760  4D 85 F6                        test r14, r14
00AB4763  0F 84 75 05 00 00               je 0x140ab4cde
00AB4769  41 0F B7 0E                     movzx ecx, word ptr [r14]
00AB476D  66 85 C9                        test cx, cx
00AB4770  0F 84 68 05 00 00               je 0x140ab4cde
00AB4776  8D 50 01                        lea edx, [rax + 1]
00AB4779  84 CA                           test dl, cl
00AB477B  0F 85 5D 05 00 00               jne 0x140ab4cde
00AB4781  48 85 FF                        test rdi, rdi
00AB4784  0F 84 54 05 00 00               je 0x140ab4cde
00AB478A  F7 47 08 0D E0 FE FF            test dword ptr [rdi + 8], 0xfffee00d
00AB4791  0F 85 47 05 00 00               jne 0x140ab4cde
00AB4797  8D 42 77                        lea eax, [rdx + 0x77]
00AB479A  66 39 07                        cmp word ptr [rdi], ax
00AB479D  0F 82 3B 05 00 00               jb 0x140ab4cde
00AB47A3  45 8D 45 04                     lea r8d, [r13 + 4]
00AB47A7  44 38 47 03                     cmp byte ptr [rdi + 3], r8b
00AB47AB  0F 83 2D 05 00 00               jae 0x140ab4cde
00AB47B1  8A 47 02                        mov al, byte ptr [rdi + 2]
00AB47B4  A8 10                           test al, 0x10
00AB47B6  74 10                           je 0x140ab47c8
00AB47B8  4C 39 6F 38                     cmp qword ptr [rdi + 0x38], r13
00AB47BC  75 0A                           jne 0x140ab47c8
00AB47BE  4C 39 6F 40                     cmp qword ptr [rdi + 0x40], r13
00AB47C2  0F 84 16 05 00 00               je 0x140ab4cde
00AB47C8  41 84 C0                        test r8b, al
00AB47CB  75 16                           jne 0x140ab47e3
00AB47CD  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00AB47D0  85 C0                           test eax, eax
00AB47D2  74 0F                           je 0x140ab47e3
00AB47D4  3D 00 02 00 00                  cmp eax, 0x200
00AB47D9  74 08                           je 0x140ab47e3
00AB47DB  84 DA                           test dl, bl
00AB47DD  0F 84 FB 04 00 00               je 0x140ab4cde
00AB47E3  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00AB47E6  BE 02 00 00 00                  mov esi, 2
00AB47EB  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AB47EF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AB47F3  D1 E9                           shr ecx, 1
00AB47F5  8B C1                           mov eax, ecx
00AB47F7  FF C9                           dec ecx
00AB47F9  85 C0                           test eax, eax
00AB47FB  74 16                           je 0x140ab4813
00AB47FD  0F B7 02                        movzx eax, word ptr [rdx]
00AB4800  48 03 D6                        add rdx, rsi
00AB4803  66 83 F8 5C                     cmp ax, 0x5c
00AB4807  75 EC                           jne 0x140ab47f5
00AB4809  B8 33 00 00 C0                  mov eax, 0xc0000033
00AB480E  E9 E1 04 00 00                  jmp 0x140ab4cf4
00AB4813  48 8B 15 2E AE 45 00            mov rdx, qword ptr [rip + 0x45ae2e]
00AB481A  41 BC 40 00 00 00               mov r12d, 0x40
00AB4820  48 85 D2                        test rdx, rdx
00AB4823  74 26                           je 0x140ab484b
00AB4825  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB482A  E8 1D AA EE FF                  call 0x14099f24c
00AB482F  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00AB4834  41 8B D4                        mov edx, r12d
00AB4837  49 8B CE                        mov rcx, r14
00AB483A  E8 71 8D DA FF                  call 0x14085d5b0
00AB483F  48 85 C0                        test rax, rax
00AB4842  74 07                           je 0x140ab484b
00AB4844  BF 35 00 00 C0                  mov edi, 0xc0000035
00AB4849  EB 24                           jmp 0x140ab486f
00AB484B  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
00AB4850  B9 00 01 00 00                  mov ecx, 0x100
00AB4855  41 B8 4F 62 4E 6D               mov r8d, 0x6d4e624f
00AB485B  E8 90 D8 0C 00                  call 0x140b820f0
00AB4860  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AB4865  48 85 C0                        test rax, rax
00AB4868  75 16                           jne 0x140ab4880
00AB486A  BF 9A 00 00 C0                  mov edi, 0xc000009a
00AB486F  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB4874  E8 B7 F4 7A FF                  call 0x140263d30
00AB4879  8B C7                           mov eax, edi
00AB487B  E9 74 04 00 00                  jmp 0x140ab4cf4
00AB4880  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00AB4885  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00AB488A  49 8B D6                        mov rdx, r14
00AB488D  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
00AB4892  E8 99 A6 94 FF                  call 0x1403fef30
00AB4897  48 8B 1D C2 AD 45 00            mov rbx, qword ptr [rip + 0x45adc2]
00AB489E  0F 10 74 24 58                  movups xmm6, xmmword ptr [rsp + 0x58]
00AB48A3  48 85 DB                        test rbx, rbx
00AB48A6  75 61                           jne 0x140ab4909
00AB48A8  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00AB48AB  40 88 75 18                     mov byte ptr [rbp + 0x18], sil
00AB48AF  48 8D 5D F0                     lea rbx, [rbp - 0x10]
00AB48B3  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00AB48B7  C7 85 B0 00 00 00 4F 62 6A 54   mov dword ptr [rbp + 0xb0], 0x546a624f
00AB48C1  0F 29 45 30                     movaps xmmword ptr [rbp + 0x30], xmm0
00AB48C5  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00AB48C9  0F 29 4D 40                     movaps xmmword ptr [rbp + 0x40], xmm1
00AB48CD  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
00AB48D1  0F 29 45 50                     movaps xmmword ptr [rbp + 0x50], xmm0
00AB48D5  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
00AB48D9  0F 29 4D 60                     movaps xmmword ptr [rbp + 0x60], xmm1
00AB48DD  0F 10 4F 50                     movups xmm1, xmmword ptr [rdi + 0x50]
00AB48E1  0F 29 45 70                     movaps xmmword ptr [rbp + 0x70], xmm0
00AB48E5  0F 10 47 60                     movups xmm0, xmmword ptr [rdi + 0x60]
00AB48E9  0F 29 8D 80 00 00 00            movaps xmmword ptr [rbp + 0x80], xmm1
00AB48F0  F2 0F 10 4F 70                  movsd xmm1, qword ptr [rdi + 0x70]
00AB48F5  0F 29 85 90 00 00 00            movaps xmmword ptr [rbp + 0x90], xmm0
00AB48FC  F2 0F 11 8D A0 00 00 00         movsd qword ptr [rbp + 0xa0], xmm1
00AB4904  F3 0F 7F 75 00                  movdqu xmmword ptr [rbp], xmm6
00AB4909  4D 8B C4                        mov r8, r12
00AB490C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00AB4910  33 D2                           xor edx, edx
00AB4912  E8 29 23 C1 FF                  call 0x1406c6c40
00AB4917  C7 45 B0 10 00 00 00            mov dword ptr [rbp - 0x50], 0x10
00AB491E  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00AB4923  8B 43 68                        mov eax, dword ptr [rbx + 0x68]
00AB4926  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00AB492A  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
00AB492D  4C 8B C3                        mov r8, rbx
00AB4930  8B 43 6C                        mov eax, dword ptr [rbx + 0x6c]
00AB4933  33 D2                           xor edx, edx
00AB4935  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00AB4938  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00AB493D  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00AB4942  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AB4947  C7 44 24 20 E0 00 00 00         mov dword ptr [rsp + 0x20], 0xe0
00AB494F  C7 45 CC 00 08 00 00            mov dword ptr [rbp - 0x34], 0x800
00AB4956  E8 95 56 DE FF                  call 0x140899ff0
00AB495B  8B F0                           mov esi, eax
00AB495D  85 C0                           test eax, eax
00AB495F  79 1D                           jns 0x140ab497e
00AB4961  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB4966  E8 C5 F3 7A FF                  call 0x140263d30
00AB496B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00AB4970  33 D2                           xor edx, edx
00AB4972  E8 F9 DE 0C 00                  call 0x140b82870
00AB4977  8B C6                           mov eax, esi
00AB4979  E9 76 03 00 00                  jmp 0x140ab4cf4
00AB497E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AB4983  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
00AB4987  48 8D 58 30                     lea rbx, [rax + 0x30]
00AB498B  44 39 2D 0E F8 50 00            cmp dword ptr [rip + 0x50f80e], r13d
00AB4992  F3 0F 7F 73 10                  movdqu xmmword ptr [rbx + 0x10], xmm6
00AB4997  74 25                           je 0x140ab49be
00AB4999  49 8B D7                        mov rdx, r15
00AB499C  48 8B CB                        mov rcx, rbx
00AB499F  E8 14 A8 C9 FF                  call 0x14074f1b8
00AB49A4  8B F0                           mov esi, eax
00AB49A6  85 C0                           test eax, eax
00AB49A8  79 14                           jns 0x140ab49be
00AB49AA  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB49AF  E8 7C F3 7A FF                  call 0x140263d30
00AB49B4  48 8B CB                        mov rcx, rbx
00AB49B7  E8 94 49 84 FF                  call 0x1402f9350
00AB49BC  EB B9                           jmp 0x140ab4977
00AB49BE  33 C0                           xor eax, eax
00AB49C0  0F 57 C0                        xorps xmm0, xmm0
00AB49C3  0F 11 43 2C                     movups xmmword ptr [rbx + 0x2c], xmm0
00AB49C7  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AB49CA  4C 39 2D 8F AC 45 00            cmp qword ptr [rip + 0x45ac8f], r13
00AB49D1  44 8D 78 03                     lea r15d, [rax + 3]
00AB49D5  44 8D 60 20                     lea r12d, [rax + 0x20]
00AB49D9  75 1D                           jne 0x140ab49f8
00AB49DB  48 89 1D 7E AC 45 00            mov qword ptr [rip + 0x45ac7e], rbx
00AB49E2  C7 43 2C 01 00 00 00            mov dword ptr [rbx + 0x2c], 1
00AB49E9  C7 83 C0 00 00 00 4F 62 6A 54   mov dword ptr [rbx + 0xc0], 0x546a624f
00AB49F3  E9 00 01 00 00                  jmp 0x140ab4af8
00AB49F8  45 0F B7 06                     movzx r8d, word ptr [r14]
00AB49FC  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
00AB4A01  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AB4A05  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00AB4A0A  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
00AB4A0F  E8 FC 86 E5 FF                  call 0x14090d110
00AB4A14  44 0F B7 6C 24 44               movzx r13d, word ptr [rsp + 0x44]
00AB4A1A  B8 FC FF 00 00                  mov eax, 0xfffc
00AB4A1F  66 45 03 EF                     add r13w, r15w
00AB4A23  B9 00 01 00 00                  mov ecx, 0x100
00AB4A28  66 44 23 E8                     and r13w, ax
00AB4A2C  41 B8 4F 62 54 6E               mov r8d, 0x6e54624f
00AB4A32  66 41 FF C5                     inc r13w
00AB4A36  41 0F B7 D5                     movzx edx, r13w
00AB4A3A  E8 B1 D6 0C 00                  call 0x140b820f0
00AB4A3F  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00AB4A43  48 85 C0                        test rax, rax
00AB4A46  0F 84 89 00 00 00               je 0x140ab4ad5
00AB4A4C  45 0F B7 C5                     movzx r8d, r13w
00AB4A50  33 D2                           xor edx, edx
00AB4A52  48 8B C8                        mov rcx, rax
00AB4A55  E8 E6 21 C1 FF                  call 0x1406c6c40
00AB4A5A  0F 57 C0                        xorps xmm0, xmm0
00AB4A5D  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00AB4A61  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00AB4A65  66 44 89 6D 8A                  mov word ptr [rbp - 0x76], r13w
00AB4A6A  45 33 C0                        xor r8d, r8d
00AB4A6D  4C 8B 6D 98                     mov r13, qword ptr [rbp - 0x68]
00AB4A71  49 8B D6                        mov rdx, r14
00AB4A74  4C 89 6D 90                     mov qword ptr [rbp - 0x70], r13
00AB4A78  E8 73 87 E5 FF                  call 0x14090d1f0
00AB4A7D  85 C0                           test eax, eax
00AB4A7F  78 43                           js 0x140ab4ac4
00AB4A81  41 0F B7 0E                     movzx ecx, word ptr [r14]
00AB4A85  41 BA 04 00 00 00               mov r10d, 4
00AB4A8B  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
00AB4A8F  D1 E9                           shr ecx, 1
00AB4A91  41 3B CA                        cmp ecx, r10d
00AB4A94  73 20                           jae 0x140ab4ab6
00AB4A96  44 0F B7 4D 8A                  movzx r9d, word ptr [rbp - 0x76]
00AB4A9B  41 8D 42 FD                     lea eax, [r10 - 3]
00AB4A9F  8B D1                           mov edx, ecx
00AB4AA1  49 03 D0                        add rdx, r8
00AB4AA4  41 3B C9                        cmp ecx, r9d
00AB4AA7  73 03                           jae 0x140ab4aac
00AB4AA9  44 88 22                        mov byte ptr [rdx], r12b
00AB4AAC  03 C8                           add ecx, eax
00AB4AAE  48 03 D0                        add rdx, rax
00AB4AB1  41 3B CA                        cmp ecx, r10d
00AB4AB4  72 EE                           jb 0x140ab4aa4
00AB4AB6  41 8B 00                        mov eax, dword ptr [r8]
00AB4AB9  89 83 C0 00 00 00               mov dword ptr [rbx + 0xc0], eax
00AB4ABF  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
00AB4AC4  33 D2                           xor edx, edx
00AB4AC6  49 8B CD                        mov rcx, r13
00AB4AC9  E8 A2 DD 0C 00                  call 0x140b82870
00AB4ACE  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
00AB4AD3  74 23                           je 0x140ab4af8
00AB4AD5  B8 04 00 00 00                  mov eax, 4
00AB4ADA  66 41 39 06                     cmp word ptr [r14], ax
00AB4ADE  72 0E                           jb 0x140ab4aee
00AB4AE0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00AB4AE4  8B 08                           mov ecx, dword ptr [rax]
00AB4AE6  89 8B C0 00 00 00               mov dword ptr [rbx + 0xc0], ecx
00AB4AEC  EB 0A                           jmp 0x140ab4af8
00AB4AEE  C7 83 C0 00 00 00 4F 62 6A 3F   mov dword ptr [rbx + 0xc0], 0x3f6a624f
00AB4AF8  41 BD 78 00 00 00               mov r13d, 0x78
00AB4AFE  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00AB4B02  45 8B C5                        mov r8d, r13d
00AB4B05  33 D2                           xor edx, edx
00AB4B07  E8 34 21 C1 FF                  call 0x1406c6c40
00AB4B0C  0F B7 07                        movzx eax, word ptr [rdi]
00AB4B0F  66 44 3B E8                     cmp r13w, ax
00AB4B13  72 03                           jb 0x140ab4b18
00AB4B15  44 8B E8                        mov r13d, eax
00AB4B18  4D 8B C5                        mov r8, r13
00AB4B1B  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00AB4B1F  48 8B D7                        mov rdx, rdi
00AB4B22  E8 19 1D C1 FF                  call 0x1406c6840
00AB4B27  B8 80 00 00 00                  mov eax, 0x80
00AB4B2C  66 39 07                        cmp word ptr [rdi], ax
00AB4B2F  72 12                           jb 0x140ab4b43
00AB4B31  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
00AB4B34  89 83 D8 00 00 00               mov dword ptr [rbx + 0xd8], eax
00AB4B3A  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
00AB4B3D  89 83 DC 00 00 00               mov dword ptr [rbx + 0xdc], eax
00AB4B43  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
00AB4B47  89 53 64                        mov dword ptr [rbx + 0x64], edx
00AB4B4A  F7 05 6C F7 50 00 00 40 00 00   test dword ptr [rip + 0x50f76c], 0x4000
00AB4B54  74 04                           je 0x140ab4b5a
00AB4B56  44 08 63 42                     or byte ptr [rbx + 0x42], r12b
00AB4B5A  8A 47 02                        mov al, byte ptr [rdi + 2]
00AB4B5D  41 BD 01 00 00 00               mov r13d, 1
00AB4B63  24 10                           and al, 0x10
00AB4B65  F6 D8                           neg al
00AB4B67  1B C9                           sbb ecx, ecx
00AB4B69  83 E1 10                        and ecx, 0x10
00AB4B6C  83 C1 58                        add ecx, 0x58
00AB4B6F  41 84 D5                        test r13b, dl
00AB4B72  75 05                           jne 0x140ab4b79
00AB4B74  01 4B 6C                        add dword ptr [rbx + 0x6c], ecx
00AB4B77  EB 03                           jmp 0x140ab4b7c
00AB4B79  01 4B 68                        add dword ptr [rbx + 0x68], ecx
00AB4B7C  45 33 F6                        xor r14d, r14d
00AB4B7F  4C 39 77 58                     cmp qword ptr [rdi + 0x58], r14
00AB4B83  75 0E                           jne 0x140ab4b93
00AB4B85  48 8D 05 24 57 E0 FF            lea rax, [rip - 0x1fa8dc]
00AB4B8C  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
00AB4B93  4C 89 B3 B8 00 00 00            mov qword ptr [rbx + 0xb8], r14
00AB4B9A  48 8D 83 C8 00 00 00            lea rax, [rbx + 0xc8]
00AB4BA1  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
00AB4BA5  48 89 1B                        mov qword ptr [rbx], rbx
00AB4BA8  48 89 40 08                     mov qword ptr [rax + 8], rax
00AB4BAC  48 89 00                        mov qword ptr [rax], rax
00AB4BAF  48 8B C3                        mov rax, rbx
00AB4BB2  F6 43 42 04                     test byte ptr [rbx + 0x42], 4
00AB4BB6  74 0E                           je 0x140ab4bc6
00AB4BB8  0F BA 6B 5C 14                  bts dword ptr [rbx + 0x5c], 0x14
00AB4BBD  48 8D 0D DC A9 45 00            lea rcx, [rip + 0x45a9dc]
00AB4BC4  EB 04                           jmp 0x140ab4bca
00AB4BC6  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00AB4BCA  4A 89 0C 20                     mov qword ptr [rax + r12], rcx
00AB4BCE  48 8B 0D 8B AA 45 00            mov rcx, qword ptr [rip + 0x45aa8b]
00AB4BD5  E8 EA 69 F2 FF                  call 0x1409db5c4
00AB4BDA  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AB4BDF  48 8D 41 E0                     lea rax, [rcx - 0x20]
00AB4BE3  44 84 69 1A                     test byte ptr [rcx + 0x1a], r13b
00AB4BE7  75 03                           jne 0x140ab4bec
00AB4BE9  49 8B C6                        mov rax, r14
00AB4BEC  48 8B 15 6D AA 45 00            mov rdx, qword ptr [rip + 0x45aa6d]
00AB4BF3  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
00AB4BF7  49 39 10                        cmp qword ptr [r8], rdx
00AB4BFA  74 05                           je 0x140ab4c01
00AB4BFC  49 8B CF                        mov rcx, r15
00AB4BFF  CD 29                           int 0x29
00AB4C01  48 89 10                        mov qword ptr [rax], rdx
00AB4C04  4C 8D 25 F5 B3 54 FF            lea r12, [rip - 0xab4c0b]
00AB4C0B  4C 89 40 08                     mov qword ptr [rax + 8], r8
00AB4C0F  BF 9A 00 00 C0                  mov edi, 0xc000009a
00AB4C14  49 89 00                        mov qword ptr [r8], rax
00AB4C17  48 89 42 08                     mov qword ptr [rdx + 8], rax
00AB4C1B  48 8B 15 3E AA 45 00            mov rdx, qword ptr [rip + 0x45aa3e]
00AB4C22  8B 42 2C                        mov eax, dword ptr [rdx + 0x2c]
00AB4C25  3D 00 01 00 00                  cmp eax, 0x100
00AB4C2A  73 0C                           jae 0x140ab4c38
00AB4C2C  FF C8                           dec eax
00AB4C2E  49 89 9C C4 80 F6 F0 00         mov qword ptr [r12 + rax*8 + 0xf0f680], rbx
00AB4C36  EB 02                           jmp 0x140ab4c3a
00AB4C38  8B F7                           mov esi, edi
00AB4C3A  48 8B CA                        mov rcx, rdx
00AB4C3D  E8 0A 69 F2 FF                  call 0x1409db54c
00AB4C42  48 3B 1D 17 AA 45 00            cmp rbx, qword ptr [rip + 0x45aa17]
00AB4C49  75 3D                           jne 0x140ab4c88
00AB4C4B  41 BF 02 00 00 00               mov r15d, 2
00AB4C51  41 0F B6 F7                     movzx esi, r15b
00AB4C55  49 89 9C F4 00 78 FC 00         mov qword ptr [r12 + rsi*8 + 0xfc7800], rbx
00AB4C5D  44 88 7B 28                     mov byte ptr [rbx + 0x28], r15b
00AB4C61  48 8B 0D E0 A9 45 00            mov rcx, qword ptr [rip + 0x45a9e0]
00AB4C68  48 85 C9                        test rcx, rcx
00AB4C6B  74 3E                           je 0x140ab4cab
00AB4C6D  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00AB4C72  48 8B D3                        mov rdx, rbx
00AB4C75  E8 46 3E F6 FF                  call 0x140a18ac0
00AB4C7A  84 C0                           test al, al
00AB4C7C  75 2D                           jne 0x140ab4cab
00AB4C7E  4D 89 B4 F4 00 78 FC 00         mov qword ptr [r12 + rsi*8 + 0xfc7800], r14
00AB4C86  EB 3F                           jmp 0x140ab4cc7
00AB4C88  85 F6                           test esi, esi
00AB4C8A  78 39                           js 0x140ab4cc5
00AB4C8C  49 63 CF                        movsxd rcx, r15d
00AB4C8F  48 81 F9 00 01 00 00            cmp rcx, 0x100
00AB4C96  73 28                           jae 0x140ab4cc0
00AB4C98  33 C0                           xor eax, eax
00AB4C9A  F0 4D 0F B1 AC CC 00 78 FC 00   lock cmpxchg qword ptr [r12 + rcx*8 + 0xfc7800], r13
00AB4CA4  74 AB                           je 0x140ab4c51
00AB4CA6  45 03 FD                        add r15d, r13d
00AB4CA9  EB E1                           jmp 0x140ab4c8c
00AB4CAB  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB4CB0  E8 7B F0 7A FF                  call 0x140263d30
00AB4CB5  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00AB4CB9  48 89 18                        mov qword ptr [rax], rbx
00AB4CBC  33 C0                           xor eax, eax
00AB4CBE  EB 34                           jmp 0x140ab4cf4
00AB4CC0  BE 01 00 00 C0                  mov esi, 0xc0000001
00AB4CC5  8B FE                           mov edi, esi
00AB4CC7  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AB4CCC  E8 5F F0 7A FF                  call 0x140263d30
00AB4CD1  48 8B CB                        mov rcx, rbx
00AB4CD4  E8 77 46 84 FF                  call 0x1402f9350
00AB4CD9  E9 9B FB FF FF                  jmp 0x140ab4879
00AB4CDE  4C 8D 05 4B C7 04 00            lea r8, [rip + 0x4c74b]
00AB4CE5  33 D2                           xor edx, edx
00AB4CE7  33 C9                           xor ecx, ecx
00AB4CE9  E8 A2 45 8A FF                  call 0x140359290
00AB4CEE  CC                              int3
00AB4CEF  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AB4CF4  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
00AB4CFB  48 33 CC                        xor rcx, rsp
00AB4CFE  E8 3D 79 BF FF                  call 0x1406ac640
00AB4D03  4C 8D 9C 24 F0 01 00 00         lea r11, [rsp + 0x1f0]
00AB4D0B  49 8B 5B 58                     mov rbx, qword ptr [r11 + 0x58]
00AB4D0F  41 0F 28 73 F0                  movaps xmm6, xmmword ptr [r11 - 0x10]
00AB4D14  49 8B E3                        mov rsp, r11
00AB4D17  41 5F                           pop r15
00AB4D19  41 5E                           pop r14
00AB4D1B  41 5D                           pop r13
00AB4D1D  41 5C                           pop r12
00AB4D1F  5F                              pop rdi
00AB4D20  5E                              pop rsi
00AB4D21  5D                              pop rbp
00AB4D22  C3                              ret
00AB4D23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCreateObjectTypeEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int16 v_stack_m1CE;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E4;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m38;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    v_rsp = (v_rsp) - (496);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    result = (*(unsigned __int64 *)(v_rip + 3498053)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 296 + 208) = result;
    *(unsigned __int64 *)(v_rsp - 296 - 128) = a4;
    *(unsigned __int64 *)(v_rsp - 296 - 96) = *(unsigned __int64 *)(v_rsp - 296 + 336);
    a2 = 0;
    result = memset(v_rsp - 296 - 16, a2, 224, a4);
    result = 0;
    v_r13 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1D8 = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 32) = 0;
    *(unsigned int *)(v_rsp - 296 - 24) = 0;
    v_stack_m1C0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 296 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 296 - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 296 - 48) = v_xmm0;
    v_stack_m1D0 = v_xmm0;
    if (a1 == 0) goto loc_00AB4CDE;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_00AB4CDE;
    if ((((unsigned __int8)(result + 1)) & ((unsigned __int8)(*(unsigned __int16 *)(a1)))) != 0) goto loc_00AB4CDE;
    if (0 == 0) goto loc_00AB4CDE;
    if (((*(unsigned int *)(a2 + 8)) & (0xFFFEE00DULL)) != 0) goto loc_00AB4CDE;
    if ((*(unsigned __int16 *)(a2)) < ((unsigned __int16)(result + 1 + 119))) goto loc_00AB4CDE;
    if ((*(unsigned __int8 *)(a2 + 3)) >= ((unsigned __int8)(v_r13 + 4))) goto loc_00AB4CDE;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 2))) & (16)) == 0) goto loc_00AB47C8;
    if ((*(unsigned __int64 *)(a2 + 56)) != 0) goto loc_00AB47C8;
    if ((*(unsigned __int64 *)(a2 + 64)) == 0) goto loc_00AB4CDE;
loc_00AB47C8:
    if ((((unsigned __int8)(v_r13 + 4)) & ((unsigned __int8)(*(unsigned __int8 *)(a2 + 2)))) != 0) goto loc_00AB47E3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36))) == 0) goto loc_00AB47E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36)))) == 512) goto loc_00AB47E3;
    if ((((unsigned __int8)(result + 1)) & ((unsigned __int8)(a4))) == 0) goto loc_00AB4CDE;
loc_00AB47E3:
    v_stack_m1E0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 36)));
    a1 = (unsigned int)((*(unsigned __int16 *)(a1)) >> (1));
loc_00AB47F5:
    a1 = (unsigned int)((a1) - 1);
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) == 0) goto loc_00AB4813;
    a2 = (*(unsigned __int64 *)(a1 + 8)) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)))) != 92) goto loc_00AB47F5;
    goto loc_00AB4CF4;
loc_00AB4813:
    if (*(unsigned __int64 *)(v_rip + 4566574) == 0) goto loc_00AB484B;
    result = ObpLockDirectoryExclusive(v_stack_m1C0, *(unsigned __int64 *)(v_rip + 4566574), v_r13 + 4, a4);
    result = ObpLookupDirectoryEntry(a1, 64, v_stack_m1C0, a4);
    if (result == 0) goto loc_00AB484B;
    goto loc_00AB486F;
loc_00AB484B:
    result = ExAllocatePool2(256, *(unsigned __int16 *)(a1 + 2), (unsigned int)(0x6D4E624FULL), a4);
    v_stack_m1C8 = result;
    if (result != 0) goto loc_00AB4880;
loc_00AB486F:
    result = ObpReleaseLookupContext(v_stack_m1C0, *(unsigned __int16 *)(a1 + 2), (unsigned int)(0x6D4E624FULL), a4);
loc_00AB4879:
    goto loc_00AB4CF4;
loc_00AB4880:
    v_stack_m1CE = (unsigned __int16)(*(unsigned __int16 *)(a1 + 2));
    result = RtlCopyUnicodeString(v_stack_m1D0, a1, (unsigned int)(0x6D4E624FULL), a4);
    v_rbx = *(unsigned __int64 *)(v_rip + 4566466);
    if (*(unsigned __int64 *)(v_rip + 4566466) == 0) {
        *(unsigned __int8 *)(v_rsp - 296 + 24) = 2;
        v_rbx = v_rsp - 296 - 16;
        *(unsigned int *)(v_rsp - 296 + 176) = 0x546A624FULL;
        *(unsigned __int64 *)(v_rsp - 296 + 48) = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 296 + 64) = v_xmm1;
        *(unsigned __int64 *)(v_rsp - 296 + 80) = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 296 + 96) = v_xmm1;
        *(unsigned __int64 *)(v_rsp - 296 + 112) = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 296 + 128) = v_xmm1;
        *(unsigned __int64 *)(v_rsp - 296 + 144) = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 296 + 160) = v_xmm1;
        *(unsigned __int64 *)(v_rsp - 296) = v_xmm6;
    }
    a2 = 0;
    result = memset(v_rsp - 296 - 80, a2, 64, a4);
    *(unsigned int *)(v_rsp - 296 - 80) = 16;
    *(unsigned int *)(v_rsp - 296 - 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 104)));
    a2 = 0;
    *(unsigned int *)(v_rsp - 296 - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 108)));
    v_stack_m1F8 = 0;
    v_stack_m200 = v_stack_m1D8;
    v_stack_m208 = 224;
    *(unsigned int *)(v_rsp - 296 - 52) = 0x800ULL;
    result = ObpAllocateObject(v_rsp - 296 - 80, a2, v_rbx, v_stack_m1D0);
    if (!sign_flag) goto loc_00AB497E;
    result = ObpReleaseLookupContext(v_stack_m1C0, a2, v_rbx, v_stack_m1D0);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, a2, v_rbx, v_stack_m1D0);
loc_00AB4977:
    goto loc_00AB4CF4;
loc_00AB497E:
    *(unsigned __int64 *)(v_stack_m1D8 + 32) = 0;
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 16) = v_xmm6;
    if ((*(unsigned int *)(v_rip + 5306382)) == 0) goto loc_00AB49BE;
    result = ObpInitObjectTypeSD(v_stack_m1D8 + 48, a3, v_rbx, v_stack_m1D0);
    if (!sign_flag) goto loc_00AB49BE;
    result = ObpReleaseLookupContext(v_stack_m1C0, a3, v_rbx, v_stack_m1D0);
    result = ObfDereferenceObject(v_stack_m1D8 + 48, a3, v_rbx, v_stack_m1D0);
    goto loc_00AB4977;
loc_00AB49BE:
    result = 0;
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 44) = v_xmm0;
    *(unsigned int *)(v_stack_m1D8 + 48 + 60) = 0;
    if ((*(unsigned __int64 *)(v_rip + 4566159)) != 0) goto loc_00AB49F8;
    *(unsigned __int64 *)(v_rip + 4566142) = v_stack_m1D8 + 48;
    *(unsigned int *)(v_stack_m1D8 + 48 + 44) = 1;
    *(unsigned int *)(v_stack_m1D8 + 48 + 192) = 0x546A624FULL;
    goto loc_00AB4AF8;
loc_00AB49F8:
    v_stack_m1E8 = 1;
    v_stack_m1E4 = 0;
    result = RtlUnicodeToMultiByteSize(v_stack_m1E4, *(unsigned __int64 *)(a1 + 8), *(unsigned __int16 *)(a1), v_stack_m1D0);
    v_r13 = (unsigned __int16)((v_stack_m1E4) + ((unsigned __int16)(result + 3)));
    v_r13 = (unsigned __int16)((v_r13) & ((unsigned __int16)((unsigned int)(0xFFFCULL))));
    v_r13 = (unsigned __int16)((v_r13) + 1);
    result = ExAllocatePool2(256, (unsigned __int16)(v_r13), (unsigned int)(0x6E54624FULL), v_stack_m1D0);
    *(unsigned __int64 *)(v_rsp - 296 - 104) = result;
    if (result == 0) goto loc_00AB4AD5;
    a2 = 0;
    result = memset(result, a2, (unsigned __int16)(v_r13), v_stack_m1D0);
    *(unsigned __int64 *)(v_rsp - 296 - 120) = v_xmm0;
    *(unsigned __int16 *)(v_rsp - 296 - 118) = (unsigned __int16)(v_r13);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 112) = *(unsigned __int64 *)(v_rsp - 296 - 104);
    result = RtlUnicodeStringToAnsiString(v_rsp - 296 - 120, a1, a3, v_stack_m1D0);
    if (sign_flag) goto loc_00AB4AC4;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1)) >> (1));
    if (((unsigned int)(a1)) >= 4) goto loc_00AB4AB6;
    a2 = ((unsigned int)((unsigned int)(a1))) + (*(unsigned __int64 *)(v_rsp - 296 - 112));
loc_00AB4AA4:
    if (((unsigned int)(a1)) < ((unsigned int)(*(unsigned __int16 *)(v_rsp - 296 - 118)))) {
        *(unsigned __int8 *)(a2) = (unsigned __int8)(result + 32);
    }
    a1 = (unsigned int)((a1) + ((unsigned int)(4 - 3)));
    a2 = (a2) + (4 - 3);
    if (((unsigned int)(a1)) < 4) goto loc_00AB4AA4;
loc_00AB4AB6:
    *(unsigned int *)(v_stack_m1D8 + 48 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 296 - 112))));
    v_stack_m1E8 = 0;
loc_00AB4AC4:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 296 - 104), a2, *(unsigned __int64 *)(v_rsp - 296 - 112), *(unsigned __int16 *)(v_rsp - 296 - 118));
    if (v_stack_m1E8 == 0) goto loc_00AB4AF8;
loc_00AB4AD5:
    if ((*(unsigned __int16 *)(a1)) < 4) goto loc_00AB4AEE;
    *(unsigned int *)(v_stack_m1D8 + 48 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    goto loc_00AB4AF8;
loc_00AB4AEE:
    *(unsigned int *)(v_stack_m1D8 + 48 + 192) = 0x3F6A624FULL;
loc_00AB4AF8:
    a2 = 0;
    result = memset(v_stack_m1D8 + 48 + 64, a2, 120, *(unsigned __int16 *)(v_rsp - 296 - 118));
    v_r13 = 120;
    if (120 >= ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC000009AULL))))) {
        v_r13 = (unsigned int)(*(unsigned __int16 *)((unsigned int)(0xC000009AULL)));
    }
    result = memcpy(v_stack_m1D8 + 48 + 64, (unsigned int)(0xC000009AULL), v_r13, *(unsigned __int16 *)(v_rsp - 296 - 118));
    result = 128;
    if ((*(unsigned __int16 *)((unsigned int)(0xC000009AULL))) >= 128) {
        result = *(unsigned int *)((unsigned int)(0xC000009AULL) + 120);
        *(unsigned int *)(v_stack_m1D8 + 48 + 216) = (unsigned int)(result);
        result = *(unsigned int *)((unsigned int)(0xC000009AULL) + 124);
        *(unsigned int *)(v_stack_m1D8 + 48 + 220) = (unsigned int)(result);
    }
    *(unsigned int *)(v_stack_m1D8 + 48 + 100) = (unsigned int)((unsigned int)(v_stack_m1E0));
    if (((*(unsigned int *)(v_rip + 5306220)) & (0x4000ULL)) != 0) {
    }
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(0xC000009AULL) + 2)) & (16));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((v_stack_m1D8 + 48 + 64) & (16));
    a1 = (unsigned int)((a1) + (88));
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_m1E0)))) != 0) goto loc_00AB4B79;
    goto loc_00AB4B7C;
loc_00AB4B79:
loc_00AB4B7C:
    v_r14 = 0;
    if ((*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 88)) == 0) {
        result = v_rip - 2074844;
        *(unsigned __int64 *)(v_stack_m1D8 + 48 + 152) = result;
    }
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 184) = 0;
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 8) = v_stack_m1D8 + 48;
    *(unsigned __int64 *)(v_stack_m1D8 + 48) = v_stack_m1D8 + 48;
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 200 + 8) = v_stack_m1D8 + 48 + 200;
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + 200) = v_stack_m1D8 + 48 + 200;
    if (((*(unsigned __int8 *)(v_stack_m1D8 + 48 + 66)) & (4)) == 0) goto loc_00AB4BC6;
    goto loc_00AB4BCA;
loc_00AB4BC6:
loc_00AB4BCA:
    *(unsigned __int64 *)(v_stack_m1D8 + 48 + result + 32 * 1) = *(unsigned __int64 *)(v_rsp - 296 - 128);
    result = ObpLockObjectTypeExclusive(*(unsigned __int64 *)(v_rip + 4565643), (unsigned int)(v_stack_m1E0), v_r13, *(unsigned __int16 *)(v_rsp - 296 - 118));
    result = v_stack_m1D8 - 32;
    if (((*(unsigned __int8 *)(v_stack_m1D8 + 26)) & (1)) == 0) {
        result = 0;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4565613) + 8))) != (*(unsigned __int64 *)(v_rip + 4565613))) {
        a1 = result + 3;
    }
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rip + 4565613);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4565613) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4565613) + 8)) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4565613) + 8) = result;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4565566) + 44)))) >= 256) goto loc_00AB4C38;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4565566) + 44))) - 1);
    *(unsigned __int64 *)(v_rip - 11226123 + result * 8 + 15791744) = v_stack_m1D8 + 48;
    goto loc_00AB4C3A;
loc_00AB4C38:
loc_00AB4C3A:
    result = ObpUnlockObjectType(*(unsigned __int64 *)(v_rip + 4565566), *(unsigned __int64 *)(v_rip + 4565566), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4565613) + 8), *(unsigned __int16 *)(v_rsp - 296 - 118));
    if ((v_stack_m1D8 + 48) != (*(unsigned __int64 *)(v_rip + 4565527))) goto loc_00AB4C88;
loc_00AB4C51:
    *(unsigned __int64 *)(v_rip - 11226123 + 2 * 8 + 16545792) = v_stack_m1D8 + 48;
    *(unsigned __int8 *)(v_stack_m1D8 + 48 + 40) = 2;
    if (*(unsigned __int64 *)(v_rip + 4565472) == 0) goto loc_00AB4CAB;
    result = ObpInsertDirectoryEntry(*(unsigned __int64 *)(v_rip + 4565472), v_stack_m1D8 + 48, v_stack_m1C0, *(unsigned __int16 *)(v_rsp - 296 - 118));
    if ((unsigned __int8)(result) != 0) goto loc_00AB4CAB;
    *(unsigned __int64 *)(v_rip - 11226123 + 2 * 8 + 16545792) = 0;
    goto loc_00AB4CC7;
loc_00AB4C88:
    if (sign_flag) goto loc_00AB4CC5;
loc_00AB4C8C:
    if (((int)(2)) >= 256) goto loc_00AB4CC0;
    result = 0;
    if (condition_is_equal) goto loc_00AB4C51;
    v_r15 = (unsigned int)((2) + (1));
    goto loc_00AB4C8C;
loc_00AB4CAB:
    result = ObpReleaseLookupContext(v_stack_m1C0, v_stack_m1D8 + 48, v_stack_m1C0, *(unsigned __int16 *)(v_rsp - 296 - 118));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 96)) = v_stack_m1D8 + 48;
    result = 0;
    goto loc_00AB4CF4;
loc_00AB4CC0:
loc_00AB4CC5:
loc_00AB4CC7:
    result = ObpReleaseLookupContext(v_stack_m1C0, v_stack_m1D8 + 48, v_stack_m1C0, *(unsigned __int16 *)(v_rsp - 296 - 118));
    result = ObfDereferenceObject(v_stack_m1D8 + 48, v_stack_m1D8 + 48, v_stack_m1C0, *(unsigned __int16 *)(v_rsp - 296 - 118));
    goto loc_00AB4879;
loc_00AB4CDE:
    a2 = 0;
    a1 = 0;
    result = DbgPrintEx(a1, a2, v_rip + 313163, *(unsigned __int16 *)(v_rsp - 296 - 118));
loc_00AB4CF4:
    a1 = (*(unsigned __int64 *)(v_rsp - 296 + 208)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 313163, *(unsigned __int16 *)(v_rsp - 296 - 118));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObCreateObjectTypeEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint16_t v_stack_m1CE;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E4;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m38;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    local_rsp = (local_rsp) - (496);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    result = (*(uint64_t *)(v_rip + 0x356045)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x128 + 0xD0) = result;
    *(uint64_t *)(local_rsp - 0x128 - 0x80) = Arg4;
    *(uint64_t *)(local_rsp - 0x128 - 0x60) = *(uint64_t *)(local_rsp - 0x128 + 0x150);
    Arg2 = 0;
    result = memset(local_rsp - 296 - 16, Arg2, 224, Arg4);
    result = 0;
    local_r13 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1D8 = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x20) = 0;
    *(uint32_t *)(local_rsp - 0x128 - 0x18) = 0;
    v_stack_m1C0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x128 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x128 - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x128 - 0x30) = v_xmm0;
    v_stack_m1D0 = v_xmm0;
    if (Arg1 == 0) goto loc_00AB4CDE;
    if ((uint16_t)(*(uint16_t *)(Arg1)) == 0) goto loc_00AB4CDE;
    if ((((uint8_t)(result + 1)) & ((uint8_t)(*(uint16_t *)(Arg1)))) != 0) goto loc_00AB4CDE;
    if (0 == 0) goto loc_00AB4CDE;
    if (((*(uint32_t *)(Arg2 + 0x8)) & (0xFFFEE00DULL)) != 0) goto loc_00AB4CDE;
    if ((*(uint16_t *)(Arg2)) < ((uint16_t)(result + 1 + 119))) goto loc_00AB4CDE;
    if ((*(uint8_t *)(Arg2 + 0x3)) >= ((uint8_t)(local_r13 + 4))) goto loc_00AB4CDE;
    if ((((uint8_t)(*(uint8_t *)(Arg2 + 0x2))) & (16)) == 0) goto loc_00AB47C8;
    if ((*(uint64_t *)(Arg2 + 0x38)) != 0) goto loc_00AB47C8;
    if ((*(uint64_t *)(Arg2 + 0x40)) == 0) goto loc_00AB4CDE;
loc_00AB47C8:
    if ((((uint8_t)(local_r13 + 4)) & ((uint8_t)(*(uint8_t *)(Arg2 + 0x2)))) != 0) goto loc_00AB47E3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x24))) == 0) goto loc_00AB47E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x24)))) == 512) goto loc_00AB47E3;
    if ((((uint8_t)(result + 1)) & ((uint8_t)(Arg4))) == 0) goto loc_00AB4CDE;
loc_00AB47E3:
    v_stack_m1E0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x24)));
    Arg1 = (uint32_t)((*(uint16_t *)(Arg1)) >> (1));
loc_00AB47F5:
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) == 0) goto loc_00AB4813;
    Arg2 = (*(uint64_t *)(Arg1 + 0x8)) + (2);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg1 + 0x8)))) != 92) goto loc_00AB47F5;
    goto loc_00AB4CF4;
loc_00AB4813:
    if (*(uint64_t *)(v_rip + 0x45AE2E) == 0) goto loc_00AB484B;
    result = ObpLockDirectoryExclusive(v_stack_m1C0, *(uint64_t *)(v_rip + 0x45AE2E), local_r13 + 4, Arg4);
    result = ObpLookupDirectoryEntry(Arg1, 64, v_stack_m1C0, Arg4);
    if (result == 0) goto loc_00AB484B;
    goto loc_00AB486F;
loc_00AB484B:
    result = ExAllocatePool2(256, *(uint16_t *)(Arg1 + 0x2), (uint32_t)(0x6D4E624FULL), Arg4);
    v_stack_m1C8 = result;
    if (result != 0) goto loc_00AB4880;
loc_00AB486F:
    result = ObpReleaseLookupContext(v_stack_m1C0, *(uint16_t *)(Arg1 + 0x2), (uint32_t)(0x6D4E624FULL), Arg4);
loc_00AB4879:
    goto loc_00AB4CF4;
loc_00AB4880:
    v_stack_m1CE = (uint16_t)(*(uint16_t *)(Arg1 + 0x2));
    result = RtlCopyUnicodeString(v_stack_m1D0, Arg1, (uint32_t)(0x6D4E624FULL), Arg4);
    local_rbx = *(uint64_t *)(v_rip + 0x45ADC2);
    if (*(uint64_t *)(v_rip + 0x45ADC2) == 0) {
        *(uint8_t *)(local_rsp - 0x128 + 0x18) = 2;
        local_rbx = local_rsp - 296 - 16;
        *(uint32_t *)(local_rsp - 0x128 + 0xB0) = 0x546A624FULL;
        *(uint64_t *)(local_rsp - 0x128 + 0x30) = v_xmm0;
        *(uint64_t *)(local_rsp - 0x128 + 0x40) = v_xmm1;
        *(uint64_t *)(local_rsp - 0x128 + 0x50) = v_xmm0;
        *(uint64_t *)(local_rsp - 0x128 + 0x60) = v_xmm1;
        *(uint64_t *)(local_rsp - 0x128 + 0x70) = v_xmm0;
        *(uint64_t *)(local_rsp - 0x128 + 0x80) = v_xmm1;
        *(uint64_t *)(local_rsp - 0x128 + 0x90) = v_xmm0;
        *(uint64_t *)(local_rsp - 0x128 + 0xA0) = v_xmm1;
        *(uint64_t *)(local_rsp - 0x128) = v_xmm6;
    }
    Arg2 = 0;
    result = memset(local_rsp - 296 - 80, Arg2, 64, Arg4);
    *(uint32_t *)(local_rsp - 0x128 - 0x50) = 16;
    *(uint32_t *)(local_rsp - 0x128 - 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x68)));
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x128 - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x6C)));
    v_stack_m1F8 = 0;
    v_stack_m200 = v_stack_m1D8;
    v_stack_m208 = 224;
    *(uint32_t *)(local_rsp - 0x128 - 0x34) = 0x800ULL;
    result = ObpAllocateObject(local_rsp - 296 - 80, Arg2, local_rbx, v_stack_m1D0);
    if (!sign_flag) goto loc_00AB497E;
    result = ObpReleaseLookupContext(v_stack_m1C0, Arg2, local_rbx, v_stack_m1D0);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, Arg2, local_rbx, v_stack_m1D0);
loc_00AB4977:
    goto loc_00AB4CF4;
loc_00AB497E:
    *(uint64_t *)(v_stack_m1D8 + 0x20) = 0;
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0x10) = v_xmm6;
    if ((*(uint32_t *)(v_rip + 0x50F80E)) == 0) goto loc_00AB49BE;
    result = ObpInitObjectTypeSD(v_stack_m1D8 + 48, Arg3, local_rbx, v_stack_m1D0);
    if (!sign_flag) goto loc_00AB49BE;
    result = ObpReleaseLookupContext(v_stack_m1C0, Arg3, local_rbx, v_stack_m1D0);
    result = ObfDereferenceObject(v_stack_m1D8 + 48, Arg3, local_rbx, v_stack_m1D0);
    goto loc_00AB4977;
loc_00AB49BE:
    result = 0;
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0x2C) = v_xmm0;
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0x3C) = 0;
    if ((*(uint64_t *)(v_rip + 0x45AC8F)) != 0) goto loc_00AB49F8;
    *(uint64_t *)(v_rip + 0x45AC7E) = v_stack_m1D8 + 48;
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0x2C) = 1;
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xC0) = 0x546A624FULL;
    goto loc_00AB4AF8;
loc_00AB49F8:
    v_stack_m1E8 = 1;
    v_stack_m1E4 = 0;
    result = RtlUnicodeToMultiByteSize(v_stack_m1E4, *(uint64_t *)(Arg1 + 0x8), *(uint16_t *)(Arg1), v_stack_m1D0);
    local_r13 = (uint16_t)((v_stack_m1E4) + ((uint16_t)(result + 3)));
    local_r13 = (uint16_t)((local_r13) & ((uint16_t)((uint32_t)(0xFFFCULL))));
    local_r13 = (uint16_t)((local_r13) + 1);
    result = ExAllocatePool2(256, (uint16_t)(local_r13), (uint32_t)(0x6E54624FULL), v_stack_m1D0);
    *(uint64_t *)(local_rsp - 0x128 - 0x68) = result;
    if (result == 0) goto loc_00AB4AD5;
    Arg2 = 0;
    result = memset(result, Arg2, (uint16_t)(local_r13), v_stack_m1D0);
    *(uint64_t *)(local_rsp - 0x128 - 0x78) = v_xmm0;
    *(uint16_t *)(local_rsp - 0x128 - 0x76) = (uint16_t)(local_r13);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x70) = *(uint64_t *)(local_rsp - 0x128 - 0x68);
    result = RtlUnicodeStringToAnsiString(local_rsp - 296 - 120, Arg1, Arg3, v_stack_m1D0);
    if (sign_flag) goto loc_00AB4AC4;
    Arg1 = (uint32_t)((*(uint16_t *)(Arg1)) >> (1));
    if (((uint32_t)(Arg1)) >= 4) goto loc_00AB4AB6;
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (*(uint64_t *)(local_rsp - 0x128 - 0x70));
loc_00AB4AA4:
    if (((uint32_t)(Arg1)) < ((uint32_t)(*(uint16_t *)(local_rsp - 0x128 - 0x76)))) {
        *(uint8_t *)(Arg2) = (uint8_t)(result + 32);
    }
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(4 - 3)));
    Arg2 = (Arg2) + (4 - 3);
    if (((uint32_t)(Arg1)) < 4) goto loc_00AB4AA4;
loc_00AB4AB6:
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x70))));
    v_stack_m1E8 = 0;
loc_00AB4AC4:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x128 - 0x68), Arg2, *(uint64_t *)(local_rsp - 0x128 - 0x70), *(uint16_t *)(local_rsp - 0x128 - 0x76));
    if (v_stack_m1E8 == 0) goto loc_00AB4AF8;
loc_00AB4AD5:
    if ((*(uint16_t *)(Arg1)) < 4) goto loc_00AB4AEE;
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x8))));
    goto loc_00AB4AF8;
loc_00AB4AEE:
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xC0) = 0x3F6A624FULL;
loc_00AB4AF8:
    Arg2 = 0;
    result = memset(v_stack_m1D8 + 48 + 64, Arg2, 120, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    local_r13 = 120;
    if (120 >= ((uint16_t)(*(uint16_t *)((uint32_t)(0xC000009AULL))))) {
        local_r13 = (uint32_t)(*(uint16_t *)((uint32_t)(0xC000009AULL)));
    }
    result = memcpy(v_stack_m1D8 + 48 + 64, (uint32_t)(0xC000009AULL), local_r13, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    result = 128;
    if ((*(uint16_t *)((uint32_t)(0xC000009AULL))) >= 128) {
        result = *(uint32_t *)((uint32_t)(0xC000009AULL) + 0x78);
        *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xD8) = (uint32_t)(result);
        result = *(uint32_t *)((uint32_t)(0xC000009AULL) + 0x7C);
        *(uint32_t *)(v_stack_m1D8 + 0x30 + 0xDC) = (uint32_t)(result);
    }
    *(uint32_t *)(v_stack_m1D8 + 0x30 + 0x64) = (uint32_t)((uint32_t)(v_stack_m1E0));
    if (((*(uint32_t *)(v_rip + 0x50F76C)) & (0x4000ULL)) != 0) {
    }
    result = (uint8_t)((*(uint8_t *)((uint32_t)(0xC000009AULL) + 0x2)) & (16));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((v_stack_m1D8 + 48 + 64) & (16));
    Arg1 = (uint32_t)((Arg1) + (88));
    if (((1) & ((uint8_t)((uint32_t)(v_stack_m1E0)))) != 0) goto loc_00AB4B79;
    goto loc_00AB4B7C;
loc_00AB4B79:
loc_00AB4B7C:
    local_r14 = 0;
    if ((*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x58)) == 0) {
        result = v_rip - 2074844;
        *(uint64_t *)(v_stack_m1D8 + 0x30 + 0x98) = result;
    }
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0xB8) = 0;
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0x8) = v_stack_m1D8 + 48;
    *(uint64_t *)(v_stack_m1D8 + 0x30) = v_stack_m1D8 + 48;
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0xC8 + 0x8) = v_stack_m1D8 + 48 + 200;
    *(uint64_t *)(v_stack_m1D8 + 0x30 + 0xC8) = v_stack_m1D8 + 48 + 200;
    if (((*(uint8_t *)(v_stack_m1D8 + 0x30 + 0x42)) & (4)) == 0) goto loc_00AB4BC6;
    goto loc_00AB4BCA;
loc_00AB4BC6:
loc_00AB4BCA:
    *(uint64_t *)(v_stack_m1D8 + 0x30 + result + 0x20 * 1) = *(uint64_t *)(local_rsp - 0x128 - 0x80);
    result = ObpLockObjectTypeExclusive(*(uint64_t *)(v_rip + 0x45AA8B), (uint32_t)(v_stack_m1E0), local_r13, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    result = v_stack_m1D8 - 32;
    if (((*(uint8_t *)(v_stack_m1D8 + 0x1A)) & (1)) == 0) {
        result = 0;
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x45AA6D) + 0x8))) != (*(uint64_t *)(v_rip + 0x45AA6D))) {
        Arg1 = result + 3;
    }
    *(uint64_t *)(result) = *(uint64_t *)(v_rip + 0x45AA6D);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x45AA6D) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x45AA6D) + 0x8)) = result;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x45AA6D) + 0x8) = result;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x45AA3E) + 0x2C)))) >= 256) goto loc_00AB4C38;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x45AA3E) + 0x2C))) - 1);
    *(uint64_t *)(v_rip - 0xAB4C0B + result * 8 + 0xF0F680) = v_stack_m1D8 + 48;
    goto loc_00AB4C3A;
loc_00AB4C38:
loc_00AB4C3A:
    result = ObpUnlockObjectType(*(uint64_t *)(v_rip + 0x45AA3E), *(uint64_t *)(v_rip + 0x45AA3E), *(uint64_t *)(*(uint64_t *)(v_rip + 0x45AA6D) + 0x8), *(uint16_t *)(local_rsp - 0x128 - 0x76));
    if ((v_stack_m1D8 + 48) != (*(uint64_t *)(v_rip + 0x45AA17))) goto loc_00AB4C88;
loc_00AB4C51:
    *(uint64_t *)(v_rip - 0xAB4C0B + 0x2 * 8 + 0xFC7800) = v_stack_m1D8 + 48;
    *(uint8_t *)(v_stack_m1D8 + 0x30 + 0x28) = 2;
    if (*(uint64_t *)(v_rip + 0x45A9E0) == 0) goto loc_00AB4CAB;
    result = ObpInsertDirectoryEntry(*(uint64_t *)(v_rip + 0x45A9E0), v_stack_m1D8 + 48, v_stack_m1C0, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    if ((uint8_t)(result) != 0) goto loc_00AB4CAB;
    *(uint64_t *)(v_rip - 0xAB4C0B + 0x2 * 8 + 0xFC7800) = 0;
    goto loc_00AB4CC7;
loc_00AB4C88:
    if (sign_flag) goto loc_00AB4CC5;
loc_00AB4C8C:
    if (((int32_t)(2)) >= 256) goto loc_00AB4CC0;
    result = 0;
    if (condition_is_equal) goto loc_00AB4C51;
    local_r15 = (uint32_t)((2) + (1));
    goto loc_00AB4C8C;
loc_00AB4CAB:
    result = ObpReleaseLookupContext(v_stack_m1C0, v_stack_m1D8 + 48, v_stack_m1C0, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x60)) = v_stack_m1D8 + 48;
    result = 0;
    goto loc_00AB4CF4;
loc_00AB4CC0:
loc_00AB4CC5:
loc_00AB4CC7:
    result = ObpReleaseLookupContext(v_stack_m1C0, v_stack_m1D8 + 48, v_stack_m1C0, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    result = ObfDereferenceObject(v_stack_m1D8 + 48, v_stack_m1D8 + 48, v_stack_m1C0, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    goto loc_00AB4879;
loc_00AB4CDE:
    Arg2 = 0;
    Arg1 = 0;
    result = DbgPrintEx(Arg1, Arg2, v_rip + 313163, *(uint16_t *)(local_rsp - 0x128 - 0x76));
loc_00AB4CF4:
    Arg1 = (*(uint64_t *)(local_rsp - 0x128 + 0xD0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 313163, *(uint16_t *)(local_rsp - 0x128 - 0x76));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB46D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
