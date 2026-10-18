# MiAllocateVirtualMemory

- RVA: `0x00883B40`–`0x008843CA` (길이 `2,186` bytes)
- VA: `0x0000000140883B40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007C820`
- 디코드: `523`개 명령, `2,186/2,186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00883BD3` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00883BF5` → [MiValidateVadMetadataFlags](MiValidateVadMetadataFlags_function_008843D0.md) (function, `0x008843D0`)
- `0x00883C57` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x00883CA7` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x00883D0B` → [MiVadSupportsPrivateCommit](../../text/31/MiVadSupportsPrivateCommit_function_00316FD0.md) (function, `0x00316FD0`)
- `0x00883DE1` → [MiCommitExistingVad](../../text/32/MiCommitExistingVad_function_0032A860.md) (function, `0x0032A860`)
- `0x00883DF4` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00883E3D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00883E74` → [MiReserveUserMemory](MiReserveUserMemory_function_00884498.md) (function, `0x00884498`)
- `0x00883EAC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00883ED1` → [EtwTiLogAllocExecVm](EtwTiLogAllocExecVm_function_00882944.md) (function, `0x00882944`)
- `0x00883EF5` → [MiResetVirtualMemory](../../text/44/MiResetVirtualMemory_function_004486F0.md) (function, `0x004486F0`)
- `0x00883F08` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00883F15` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00883F2C` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00883F40` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00883F81` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)
- `0x00883F9B` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (function, `0x0043E560`)
- `0x00883FBB` → [MiCommitFileBackedSection](MiCommitFileBackedSection_function_00882238.md) (function, `0x00882238`)
- `0x00883FE6` → [MiCommitEnclavePages](../../text/36/MiCommitEnclavePages_function_00367CCC.md) (function, `0x00367CCC`)
- `0x0088400C` → [MiAllowProtectionChange](../../text/44/MiAllowProtectionChange_function_00448834.md) (function, `0x00448834`)
- `0x00884059` → [MiCommitVadMetadataBits](../8D/MiCommitVadMetadataBits_function_008D1A00.md) (function, `0x008D1A00`)
- `0x00884071` → [MiCommitPagefileBackedSection](../8C/MiCommitPagefileBackedSection_function_008CECC0.md) (function, `0x008CECC0`)
- `0x00884083` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x008840A9` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)
- `0x008840C1` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x0088410D` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x0088418D` → [MmProtectVirtualMemory](MmProtectVirtualMemory_function_00881050.md) (function, `0x00881050`)
- `0x008841BC` → [MiLogMemResetInfo](../A8/MiLogMemResetInfo_function_00A802F8.md) (function, `0x00A802F8`)
- `0x008841F1` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x00884217` → [PerfInfoLogVirtualAlloc](../A4/PerfInfoLogVirtualAlloc_function_00A45754.md) (function, `0x00A45754`)
- `0x00884250` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x008842AD` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0088436B` → [MiCheckSecuredVad](MiCheckSecuredVad_function_00881FB4.md) (function, `0x00881FB4`)
- `0x008843C0` → [MiLogMemResetInfo](../A8/MiLogMemResetInfo_function_00A802F8.md) (function, `0x00A802F8`)

### Direct callers
- [MmCommitDecommitSecuredMemory](../7F/MmCommitDecommitSecuredMemory_function_007FE904.md) at `0x007FE9C8`
- [MmAllocateUserStack](MmAllocateUserStack_function_00882B30.md) at `0x00882C5F`
- [NtAllocateVirtualMemory](NtAllocateVirtualMemory_function_00882D20.md) at `0x00882EFA`
- [MiAllocateVirtualMemoryCommon](MiAllocateVirtualMemoryCommon_function_00883000.md) at `0x008830FC`
- [MiAllocateVirtualMemoryCommon](MiAllocateVirtualMemoryCommon_function_00883000.md) at `0x008831A3`
- [MmStoreAllocateVirtualMemory](../A6/MmStoreAllocateVirtualMemory_function_00A68238.md) at `0x00A682F6`

### Static image references
- `0x00883B5C` → RVA `0x00E0A740` (`.data`; read)
- `0x00883E09` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x008842A6` → RVA `0x00FD9AD0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00883BD3` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x00883C57` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x00883CA7` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x00883D0B` → [MiVadSupportsPrivateCommit](../../text/31/MiVadSupportsPrivateCommit_function_00316FD0.md) (`PAGE` → `.text`)
  - `0x00883DE1` → [MiCommitExistingVad](../../text/32/MiCommitExistingVad_function_0032A860.md) (`PAGE` → `.text`)
  - `0x00883DF4` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00883E3D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00883EAC` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00883EF5` → [MiResetVirtualMemory](../../text/44/MiResetVirtualMemory_function_004486F0.md) (`PAGE` → `.text`)
  - `0x00883F08` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00883F15` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00883F2C` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00883F40` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00883F9B` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (`PAGE` → `.text`)
  - `0x00883FE6` → [MiCommitEnclavePages](../../text/36/MiCommitEnclavePages_function_00367CCC.md) (`PAGE` → `.text`)
  - `0x0088400C` → [MiAllowProtectionChange](../../text/44/MiAllowProtectionChange_function_00448834.md) (`PAGE` → `.text`)
  - `0x00884083` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
  - `0x008840C1` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x0088410D` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x008841F1` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x00884250` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00884291` → [sub_00B18E9A](../B1/Unknown_function_00B18E9A.md) (`tail-transfer`)
  - `0x0088429D` → [sub_00B18E9A + 0x1E](../B1/Unknown_function_00B18E9A.md) (`tail-transfer`)
  - `0x008842B4` → [sub_00B18E9A + 0x50](../B1/Unknown_function_00B18E9A.md) (`tail-transfer`)
  - `0x00884335` → [sub_00B18E9A + 0x59](../B1/Unknown_function_00B18E9A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00883B40  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00883B45  55                              push rbp
00883B46  56                              push rsi
00883B47  57                              push rdi
00883B48  41 54                           push r12
00883B4A  41 55                           push r13
00883B4C  41 56                           push r14
00883B4E  41 57                           push r15
00883B50  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00883B55  48 81 EC D0 00 00 00            sub rsp, 0xd0
00883B5C  48 8B 05 DD 6B 58 00            mov rax, qword ptr [rip + 0x586bdd]
00883B63  48 33 C4                        xor rax, rsp
00883B66  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00883B6A  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
00883B6E  4D 8B F0                        mov r14, r8
00883B71  45 33 C0                        xor r8d, r8d
00883B74  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
00883B78  0F 57 C0                        xorps xmm0, xmm0
00883B7B  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00883B7F  4D 85 F6                        test r14, r14
00883B82  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00883B86  4C 8B D2                        mov r10, rdx
00883B89  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
00883B8D  4D 0F 44 F0                     cmove r14, r8
00883B91  66 44 89 45 B3                  mov word ptr [rbp - 0x4d], r8w
00883B96  4D 89 07                        mov qword ptr [r15], r8
00883B99  48 8B F9                        mov rdi, rcx
00883B9C  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
00883BA0  41 8B D8                        mov ebx, r8d
00883BA3  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00883BA7  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
00883BAB  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00883BAF  48 83 FA 02                     cmp rdx, 2
00883BB3  0F 83 74 06 00 00               jae 0x14088422d
00883BB9  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00883BBD  BB 02 00 00 00                  mov ebx, 2
00883BC2  48 2B 0F                        sub rcx, qword ptr [rdi]
00883BC5  48 FF C1                        inc rcx
00883BC8  48 3B 4F 18                     cmp rcx, qword ptr [rdi + 0x18]
00883BCC  8B 4F 2C                        mov ecx, dword ptr [rdi + 0x2c]
00883BCF  41 0F 45 D8                     cmovne ebx, r8d
00883BD3  E8 A8 58 AA FF                  call 0x140329480
00883BD8  44 8B E0                        mov r12d, eax
00883BDB  83 F8 FF                        cmp eax, -1
00883BDE  0F 84 9E 02 00 00               je 0x140883e82
00883BE4  48 8B 4F 58                     mov rcx, qword ptr [rdi + 0x58]
00883BE8  48 39 4F 60                     cmp qword ptr [rdi + 0x60], rcx
00883BEC  0F 85 1D 03 00 00               jne 0x140883f0f
00883BF2  48 8B CF                        mov rcx, rdi
00883BF5  E8 D6 07 00 00                  call 0x1408843d0
00883BFA  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00883BFD  49 8B F6                        mov rsi, r14
00883C00  85 C0                           test eax, eax
00883C02  0F 88 84 02 00 00               js 0x140883e8c
00883C08  F7 47 40 00 00 00 04            test dword ptr [rdi + 0x40], 0x4000000
00883C0F  0F 95 C1                        setne cl
00883C12  F6 C3 02                        test bl, 2
00883C15  0F 94 C0                        sete al
00883C18  84 C8                           test al, cl
00883C1A  0F 85 01 06 00 00               jne 0x140884221
00883C20  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00883C23  0F BA E2 1E                     bt edx, 0x1e
00883C27  0F 82 44 06 00 00               jb 0x140884271
00883C2D  8B 47 70                        mov eax, dword ptr [rdi + 0x70]
00883C30  83 E0 1A                        and eax, 0x1a
00883C33  0F 85 56 06 00 00               jne 0x14088428f
00883C39  81 E2 00 00 40 20               and edx, 0x20400000
00883C3F  81 FA 00 00 00 20               cmp edx, 0x20000000
00883C45  75 03                           jne 0x140883c4a
00883C47  83 CB 10                        or ebx, 0x10
00883C4A  83 FB 10                        cmp ebx, 0x10
00883C4D  0F 83 4F 06 00 00               jae 0x1408842a2
00883C53  48 8B 4F 58                     mov rcx, qword ptr [rdi + 0x58]
00883C57  E8 B4 FE BB FF                  call 0x140443b10
00883C5C  41 BD 00 20 00 00               mov r13d, 0x2000
00883C62  0F B7 08                        movzx ecx, word ptr [rax]
00883C65  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00883C68  66 89 4D B3                     mov word ptr [rbp - 0x4d], cx
00883C6C  41 85 C5                        test r13d, eax
00883C6F  0F 85 E9 01 00 00               jne 0x140883e5e
00883C75  0F BA E0 1E                     bt eax, 0x1e
00883C79  0F 82 47 06 00 00               jb 0x1408842c6
00883C7F  48 83 7F 48 00                  cmp qword ptr [rdi + 0x48], 0
00883C84  0F 85 48 06 00 00               jne 0x1408842d2
00883C8A  4C 8B 6F 08                     mov r13, qword ptr [rdi + 8]
00883C8E  48 8B 0F                        mov rcx, qword ptr [rdi]
00883C91  4D 8B FD                        mov r15, r13
00883C94  49 C1 EF 0C                     shr r15, 0xc
00883C98  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
00883C9C  4D 85 F6                        test r14, r14
00883C9F  75 0E                           jne 0x140883caf
00883CA1  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00883CA5  33 D2                           xor edx, edx
00883CA7  E8 E4 29 A9 FF                  call 0x140316690
00883CAC  48 8B F0                        mov rsi, rax
00883CAF  48 85 F6                        test rsi, rsi
00883CB2  0F 84 26 06 00 00               je 0x1408842de
00883CB8  0F B6 4E 21                     movzx ecx, byte ptr [rsi + 0x21]
00883CBC  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00883CBF  48 C1 E1 20                     shl rcx, 0x20
00883CC3  48 0B C8                        or rcx, rax
00883CC6  4C 3B F9                        cmp r15, rcx
00883CC9  0F 87 28 06 00 00               ja 0x1408842f7
00883CCF  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00883CD2  25 00 00 20 04                  and eax, 0x4200000
00883CD7  3D 00 00 20 04                  cmp eax, 0x4200000
00883CDC  74 0A                           je 0x140883ce8
00883CDE  83 7F 30 00                     cmp dword ptr [rdi + 0x30], 0
00883CE2  0F 85 1B 06 00 00               jne 0x140884303
00883CE8  4C 8B 7D D7                     mov r15, qword ptr [rbp - 0x29]
00883CEC  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00883CF0  49 89 0F                        mov qword ptr [r15], rcx
00883CF3  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
00883CF6  8B C2                           mov eax, edx
00883CF8  25 00 00 20 0C                  and eax, 0xc200000
00883CFD  3D 00 00 20 08                  cmp eax, 0x8200000
00883D02  0F 84 BD 02 00 00               je 0x140883fc5
00883D08  48 8B CE                        mov rcx, rsi
00883D0B  E8 C0 32 A9 FF                  call 0x140316fd0
00883D10  85 C0                           test eax, eax
00883D12  0F 84 10 06 00 00               je 0x140884328
00883D18  8B 4E 34                        mov ecx, dword ptr [rsi + 0x34]
00883D1B  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
00883D25  0F B6 56 22                     movzx edx, byte ptr [rsi + 0x22]
00883D29  48 C1 E2 20                     shl rdx, 0x20
00883D2D  48 0B D1                        or rdx, rcx
00883D30  48 3B D0                        cmp rdx, rax
00883D33  0F 83 FD 01 00 00               jae 0x140883f36
00883D39  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00883D3C  24 70                           and al, 0x70
00883D3E  3C 40                           cmp al, 0x40
00883D40  0F 84 85 03 00 00               je 0x1408840cb
00883D46  8B 4F 28                        mov ecx, dword ptr [rdi + 0x28]
00883D49  F7 C1 00 00 08 01               test ecx, 0x1080000
00883D4F  0F 85 86 01 00 00               jne 0x140883edb
00883D55  41 F6 C4 02                     test r12b, 2
00883D59  0F 85 91 02 00 00               jne 0x140883ff0
00883D5F  4C 8B 75 C7                     mov r14, qword ptr [rbp - 0x39]
00883D63  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00883D66  8B 57 2C                        mov edx, dword ptr [rdi + 0x2c]
00883D69  0F BA E1 15                     bt ecx, 0x15
00883D6D  0F 83 D7 01 00 00               jae 0x140883f4a
00883D73  F6 C2 88                        test dl, 0x88
00883D76  0F 85 A2 03 00 00               jne 0x14088411e
00883D7C  8B C1                           mov eax, ecx
00883D7E  24 70                           and al, 0x70
00883D80  3C 40                           cmp al, 0x40
00883D82  0F 84 3E 04 00 00               je 0x1408841c6
00883D88  F6 C1 08                        test cl, 8
00883D8B  0F 85 EA 02 00 00               jne 0x14088407b
00883D91  8B 47 34                        mov eax, dword ptr [rdi + 0x34]
00883D94  48 8D 4D B3                     lea rcx, [rbp - 0x4d]
00883D98  44 8B 4F 2C                     mov r9d, dword ptr [rdi + 0x2c]
00883D9C  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
00883DA0  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
00883DA4  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00883DA9  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00883DAD  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00883DB2  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00883DB6  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00883DBB  0F B6 4F 38                     movzx ecx, byte ptr [rdi + 0x38]
00883DBF  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
00883DC3  48 8B CE                        mov rcx, rsi
00883DC6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00883DCA  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
00883DCE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00883DD3  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00883DD6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00883DDA  C7 45 BF 00 00 00 00            mov dword ptr [rbp - 0x41], 0
00883DE1  E8 7A 6A AA FF                  call 0x14032a860
00883DE6  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00883DE9  85 C0                           test eax, eax
00883DEB  0F 88 14 01 00 00               js 0x140883f05
00883DF1  48 8B CE                        mov rcx, rsi
00883DF4  E8 67 30 A9 FF                  call 0x140316e60
00883DF9  83 7D BF 00                     cmp dword ptr [rbp - 0x41], 0
00883DFD  0F 85 47 03 00 00               jne 0x14088414a
00883E03  41 BD 00 20 00 00               mov r13d, 0x2000
00883E09  F7 05 F1 2C 74 00 00 80 00 00   test dword ptr [rip + 0x742cf1], 0x8000
00883E13  0F 85 7E 03 00 00               jne 0x140884197
00883E19  F6 C3 01                        test bl, 1
00883E1C  0F 85 04 01 00 00               jne 0x140883f26
00883E22  41 F6 C4 02                     test r12b, 2
00883E26  0F 85 87 00 00 00               jne 0x140883eb3
00883E2C  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00883E30  49 89 07                        mov qword ptr [r15], rax
00883E33  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
00883E36  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00883E3A  48 33 CC                        xor rcx, rsp
00883E3D  E8 FE 87 E2 FF                  call 0x1406ac640
00883E42  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
00883E4A  48 81 C4 D0 00 00 00            add rsp, 0xd0
00883E51  41 5F                           pop r15
00883E53  41 5E                           pop r14
00883E55  41 5D                           pop r13
00883E57  41 5C                           pop r12
00883E59  5F                              pop rdi
00883E5A  5E                              pop rsi
00883E5B  5D                              pop rbp
00883E5C  C3                              ret
00883E5D  CC                              int3
00883E5E  48 8D 45 B3                     lea rax, [rbp - 0x4d]
00883E62  45 8B C4                        mov r8d, r12d
00883E65  4C 8D 4D B7                     lea r9, [rbp - 0x49]
00883E69  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00883E6E  49 8B D2                        mov rdx, r10
00883E71  48 8B CF                        mov rcx, rdi
00883E74  E8 1F 06 00 00                  call 0x140884498
00883E79  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00883E7C  85 C0                           test eax, eax
00883E7E  79 89                           jns 0x140883e09
00883E80  EB 0A                           jmp 0x140883e8c
00883E82  C7 45 AF 45 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000045
00883E89  49 8B F6                        mov rsi, r14
00883E8C  48 85 F6                        test rsi, rsi
00883E8F  75 74                           jne 0x140883f05
00883E91  F7 05 69 2C 74 00 00 80 00 00   test dword ptr [rip + 0x742c69], 0x8000
00883E9B  0F 85 FA 04 00 00               jne 0x14088439b
00883EA1  F6 C3 01                        test bl, 1
00883EA4  74 8D                           je 0x140883e33
00883EA6  33 D2                           xor edx, edx
00883EA8  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00883EAC  E8 7F 3E 99 FF                  call 0x140217d30
00883EB1  EB 80                           jmp 0x140883e33
00883EB3  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
00883EB6  4C 8B 4F 20                     mov r9, qword ptr [rdi + 0x20]
00883EBA  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
00883EBE  0F B6 57 39                     movzx edx, byte ptr [rdi + 0x39]
00883EC2  48 8B 4F 58                     mov rcx, qword ptr [rdi + 0x58]
00883EC6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00883ECA  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00883ECD  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00883ED1  E8 6E EA FF FF                  call 0x140882944
00883ED6  E9 51 FF FF FF                  jmp 0x140883e2c
00883EDB  0F B6 47 39                     movzx eax, byte ptr [rdi + 0x39]
00883EDF  4C 8B CE                        mov r9, rsi
00883EE2  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
00883EE6  4D 8B C5                        mov r8, r13
00883EE9  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00883EED  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00883EF1  48 8B 4F 60                     mov rcx, qword ptr [rdi + 0x60]
00883EF5  E8 F6 47 BC FF                  call 0x1404486f0
00883EFA  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00883EFD  85 C0                           test eax, eax
00883EFF  0F 89 B9 01 00 00               jns 0x1408840be
00883F05  48 8B CE                        mov rcx, rsi
00883F08  E8 53 2F A9 FF                  call 0x140316e60
00883F0D  EB 82                           jmp 0x140883e91
00883F0F  4C 8D 45 E7                     lea r8, [rbp - 0x19]
00883F13  33 D2                           xor edx, edx
00883F15  E8 06 29 99 FF                  call 0x140216820
00883F1A  4C 8B 55 CF                     mov r10, qword ptr [rbp - 0x31]
00883F1E  83 CB 01                        or ebx, 1
00883F21  E9 CC FC FF FF                  jmp 0x140883bf2
00883F26  33 D2                           xor edx, edx
00883F28  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00883F2C  E8 FF 3D 99 FF                  call 0x140217d30
00883F31  E9 EC FE FF FF                  jmp 0x140883e22
00883F36  48 8B CE                        mov rcx, rsi
00883F39  C7 45 AF 18 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000018
00883F40  E8 1B 2F A9 FF                  call 0x140316e60
00883F45  E9 47 FF FF FF                  jmp 0x140883e91
00883F4A  F7 C2 00 06 00 00               test edx, 0x600
00883F50  0F 85 2D 04 00 00               jne 0x140884383
00883F56  F6 C1 08                        test cl, 8
00883F59  0F 95 C1                        setne cl
00883F5C  F6 C3 04                        test bl, 4
00883F5F  0F 94 C0                        sete al
00883F62  84 C8                           test al, cl
00883F64  74 2B                           je 0x140883f91
00883F66  0F B6 47 39                     movzx eax, byte ptr [rdi + 0x39]
00883F6A  45 8B CC                        mov r9d, r12d
00883F6D  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
00883F71  48 8B CE                        mov rcx, rsi
00883F74  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
00883F78  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00883F7D  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00883F81  E8 2E E0 FF FF                  call 0x140881fb4
00883F86  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00883F89  85 C0                           test eax, eax
00883F8B  0F 88 74 FF FF FF               js 0x140883f05
00883F91  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
00883F95  4C 8B 00                        mov r8, qword ptr [rax]
00883F98  49 8B C8                        mov rcx, r8
00883F9B  E8 C0 A5 BB FF                  call 0x14043e560
00883FA0  48 8B D6                        mov rdx, rsi
00883FA3  0F B7 08                        movzx ecx, word ptr [rax]
00883FA6  66 89 4D B3                     mov word ptr [rbp - 0x4d], cx
00883FAA  48 8B CF                        mov rcx, rdi
00883FAD  49 83 78 40 00                  cmp qword ptr [r8 + 0x40], 0
00883FB2  0F 84 B9 00 00 00               je 0x140884071
00883FB8  4D 8B C6                        mov r8, r14
00883FBB  E8 78 E2 FF FF                  call 0x140882238
00883FC0  E9 35 FF FF FF                  jmp 0x140883efa
00883FC5  83 E2 70                        and edx, 0x70
00883FC8  80 FA 30                        cmp dl, 0x30
00883FCB  0F 85 3E 03 00 00               jne 0x14088430f
00883FD1  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00883FD4  4D 8B CD                        mov r9, r13
00883FD7  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00883FDC  4C 8B C1                        mov r8, rcx
00883FDF  48 8B D6                        mov rdx, rsi
00883FE2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00883FE6  E8 E1 3C AE FF                  call 0x140367ccc
00883FEB  E9 0A FF FF FF                  jmp 0x140883efa
00883FF0  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00883FF4  45 8B CC                        mov r9d, r12d
00883FF7  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
00883FFB  4C 8B C6                        mov r8, rsi
00883FFE  48 8B 4F 58                     mov rcx, qword ptr [rdi + 0x58]
00884002  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00884007  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088400C  E8 23 48 BC FF                  call 0x140448834
00884011  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00884014  85 C0                           test eax, eax
00884016  0F 88 E9 FE FF FF               js 0x140883f05
0088401C  F7 46 30 00 01 00 00            test dword ptr [rsi + 0x30], 0x100
00884023  0F 85 01 01 00 00               jne 0x14088412a
00884029  83 7F 78 00                     cmp dword ptr [rdi + 0x78], 0
0088402D  4C 8B 75 C7                     mov r14, qword ptr [rbp - 0x39]
00884031  0F 84 2C FD FF FF               je 0x140883d63
00884037  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
0088403A  A8 08                           test al, 8
0088403C  0F 85 0E 03 00 00               jne 0x140884350
00884042  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00884046  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0088404A  44 8B 47 78                     mov r8d, dword ptr [rdi + 0x78]
0088404E  48 8B CE                        mov rcx, rsi
00884051  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00884055  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
00884059  E8 A2 D9 04 00                  call 0x1408d1a00
0088405E  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00884061  85 C0                           test eax, eax
00884063  0F 88 9C FE FF FF               js 0x140883f05
00884069  83 CB 20                        or ebx, 0x20
0088406C  E9 F2 FC FF FF                  jmp 0x140883d63
00884071  E8 4A AC 04 00                  call 0x1408cecc0
00884076  E9 7F FE FF FF                  jmp 0x140883efa
0088407B  BA 40 00 00 00                  mov edx, 0x40
00884080  48 8B CE                        mov rcx, rsi
00884083  E8 84 39 A2 FF                  call 0x1402a7a0c
00884088  48 85 C0                        test rax, rax
0088408B  0F 85 FE 02 00 00               jne 0x14088438f
00884091  0F B6 47 39                     movzx eax, byte ptr [rdi + 0x39]
00884095  45 8B CC                        mov r9d, r12d
00884098  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
0088409C  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
008840A0  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008840A5  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008840A9  E8 06 DF FF FF                  call 0x140881fb4
008840AE  89 45 AF                        mov dword ptr [rbp - 0x51], eax
008840B1  85 C0                           test eax, eax
008840B3  0F 89 D8 FC FF FF               jns 0x140883d91
008840B9  E9 47 FE FF FF                  jmp 0x140883f05
008840BE  48 8B CE                        mov rcx, rsi
008840C1  E8 9A 2D A9 FF                  call 0x140316e60
008840C6  E9 38 FD FF FF                  jmp 0x140883e03
008840CB  8B 57 2C                        mov edx, dword ptr [rdi + 0x2c]
008840CE  81 E2 FF F9 FF FF               and edx, 0xfffff9ff
008840D4  89 57 2C                        mov dword ptr [rdi + 0x2c], edx
008840D7  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
008840DA  44 8B C0                        mov r8d, eax
008840DD  41 81 E0 00 0C 00 00            and r8d, 0xc00
008840E4  A9 80 03 00 00                  test eax, 0x380
008840E9  0F 95 C1                        setne cl
008840EC  41 81 F8 00 0C 00 00            cmp r8d, 0xc00
008840F3  0F 94 C0                        sete al
008840F6  84 C8                           test al, cl
008840F8  0F 85 E0 00 00 00               jne 0x1408841de
008840FE  41 81 F8 00 04 00 00            cmp r8d, 0x400
00884105  0F 84 3C 02 00 00               je 0x140884347
0088410B  8B CA                           mov ecx, edx
0088410D  E8 6E 53 AA FF                  call 0x140329480
00884112  44 8B E0                        mov r12d, eax
00884115  83 F8 FF                        cmp eax, -1
00884118  0F 85 28 FC FF FF               jne 0x140883d46
0088411E  C7 45 AF 45 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000045
00884125  E9 DB FD FF FF                  jmp 0x140883f05
0088412A  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0088412D  A8 02                           test al, 2
0088412F  75 06                           jne 0x140884137
00884131  83 E0 FE                        and eax, 0xfffffffe
00884134  89 47 78                        mov dword ptr [rdi + 0x78], eax
00884137  A8 08                           test al, 8
00884139  0F 85 EA FE FF FF               jne 0x140884029
0088413F  83 E0 FB                        and eax, 0xfffffffb
00884142  89 47 78                        mov dword ptr [rdi + 0x78], eax
00884145  E9 DF FE FF FF                  jmp 0x140884029
0088414A  8B 57 2C                        mov edx, dword ptr [rdi + 0x2c]
0088414D  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00884151  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00884155  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00884159  8B CA                           mov ecx, edx
0088415B  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0088415F  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00884163  0F BA E9 1E                     bts ecx, 0x1e
00884167  F6 C3 20                        test bl, 0x20
0088416A  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0088416E  48 8D 45 C7                     lea rax, [rbp - 0x39]
00884172  C7 45 C7 00 00 00 00            mov dword ptr [rbp - 0x39], 0
00884179  0F 44 CA                        cmove ecx, edx
0088417C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00884181  48 8B 57 58                     mov rdx, qword ptr [rdi + 0x58]
00884185  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00884189  48 8B 4F 60                     mov rcx, qword ptr [rdi + 0x60]
0088418D  E8 BE CE FF FF                  call 0x140881050
00884192  E9 6C FC FF FF                  jmp 0x140883e03
00884197  44 8B 4F 28                     mov r9d, dword ptr [rdi + 0x28]
0088419B  41 F7 C1 00 30 00 00            test r9d, 0x3000
008841A2  75 46                           jne 0x1408841ea
008841A4  41 F7 C1 00 00 08 01            test r9d, 0x1080000
008841AB  0F 84 68 FC FF FF               je 0x140883e19
008841B1  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
008841B5  45 8B C1                        mov r8d, r9d
008841B8  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008841BC  E8 37 C1 1F 00                  call 0x140a802f8
008841C1  E9 53 FC FF FF                  jmp 0x140883e19
008841C6  F7 C2 F9 F9 FF FF               test edx, 0xfffff9f9
008841CC  0F 84 B6 FB FF FF               je 0x140883d88
008841D2  C7 45 AF 45 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000045
008841D9  E9 27 FD FF FF                  jmp 0x140883f05
008841DE  0F BA EA 0A                     bts edx, 0xa
008841E2  89 57 2C                        mov dword ptr [rdi + 0x2c], edx
008841E5  E9 21 FF FF FF                  jmp 0x14088410b
008841EA  4C 8B 47 58                     mov r8, qword ptr [rdi + 0x58]
008841EE  49 8B C8                        mov rcx, r8
008841F1  E8 1A F9 BB FF                  call 0x140443b10
008841F6  F6 47 40 01                     test byte ptr [rdi + 0x40], 1
008841FA  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
008841FE  45 0F 45 CD                     cmovne r9d, r13d
00884202  0F B7 08                        movzx ecx, word ptr [rax]
00884205  0F B7 45 B3                     movzx eax, word ptr [rbp - 0x4d]
00884209  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
0088420E  66 89 4C 24 20                  mov word ptr [rsp + 0x20], cx
00884213  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00884217  E8 38 15 1C 00                  call 0x140a45754
0088421C  E9 F8 FB FF FF                  jmp 0x140883e19
00884221  C7 45 AF 0D 00 00 C0            mov dword ptr [rbp - 0x51], 0xc000000d
00884228  E9 5F FC FF FF                  jmp 0x140883e8c
0088422D  48 8B 02                        mov rax, qword ptr [rdx]
00884230  8B 40 04                        mov eax, dword ptr [rax + 4]
00884233  84 C0                           test al, al
00884235  79 15                           jns 0x14088424c
00884237  F6 41 70 10                     test byte ptr [rcx + 0x70], 0x10
0088423B  74 28                           je 0x140884265
0088423D  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
00884240  25 00 00 40 20                  and eax, 0x20400000
00884245  3D 00 00 00 20                  cmp eax, 0x20000000
0088424A  75 19                           jne 0x140884265
0088424C  48 8B 49 58                     mov rcx, qword ptr [rcx + 0x58]
00884250  E8 BB F8 BB FF                  call 0x140443b10
00884255  49 39 02                        cmp qword ptr [r10], rax
00884258  4D 0F 44 D0                     cmove r10, r8
0088425C  4C 89 55 CF                     mov qword ptr [rbp - 0x31], r10
00884260  E9 54 F9 FF FF                  jmp 0x140883bb9
00884265  C7 45 AF 0D 00 00 C0            mov dword ptr [rbp - 0x51], 0xc000000d
0088426C  E9 18 FC FF FF                  jmp 0x140883e89
00884271  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00884275  48 83 B8 40 06 00 00 00         cmp qword ptr [rax + 0x640], 0
0088427D  0F 85 AA F9 FF FF               jne 0x140883c2d
00884283  C7 45 AF 0D 00 00 C0            mov dword ptr [rbp - 0x51], 0xc000000d
0088428A  E9 FD FB FF FF                  jmp 0x140883e8c
0088428F  A8 02                           test al, 2
00884291  0F 84 03 4C 29 00               je 0x140b18e9a
00884297  41 B8 FF FF 00 00               mov r8d, 0xffff
0088429D  E9 16 4C 29 00                  jmp 0x140b18eb8
008842A2  0F B6 57 39                     movzx edx, byte ptr [rdi + 0x39]
008842A6  48 8B 0D 23 58 75 00            mov rcx, qword ptr [rip + 0x755823]
008842AD  E8 6E DB FE FF                  call 0x140871e20
008842B2  84 C0                           test al, al
008842B4  0F 85 30 4C 29 00               jne 0x140b18eea
008842BA  C7 45 AF 61 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000061
008842C1  E9 C6 FB FF FF                  jmp 0x140883e8c
008842C6  C7 45 AF 0D 00 00 C0            mov dword ptr [rbp - 0x51], 0xc000000d
008842CD  E9 BA FB FF FF                  jmp 0x140883e8c
008842D2  C7 45 AF 0D 00 00 C0            mov dword ptr [rbp - 0x51], 0xc000000d
008842D9  E9 AE FB FF FF                  jmp 0x140883e8c
008842DE  81 7D AF A0 00 00 C0            cmp dword ptr [rbp - 0x51], 0xc00000a0
008842E5  0F 85 A6 FB FF FF               jne 0x140883e91
008842EB  C7 45 AF 18 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000018
008842F2  E9 9A FB FF FF                  jmp 0x140883e91
008842F7  C7 45 AF 18 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000018
008842FE  E9 02 FC FF FF                  jmp 0x140883f05
00884303  C7 45 AF 18 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000018
0088430A  E9 F6 FB FF FF                  jmp 0x140883f05
0088430F  F7 47 40 00 00 00 10            test dword ptr [rdi + 0x40], 0x10000000
00884316  0F 85 EC F9 FF FF               jne 0x140883d08
0088431C  C7 45 AF A0 00 00 C0            mov dword ptr [rbp - 0x51], 0xc00000a0
00884323  E9 DD FB FF FF                  jmp 0x140883f05
00884328  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
0088432B  25 00 00 A0 00                  and eax, 0xa00000
00884330  3D 00 00 A0 00                  cmp eax, 0xa00000
00884335  0F 84 B8 4B 29 00               je 0x140b18ef3
0088433B  C7 45 AF 18 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000018
00884342  E9 BE FB FF FF                  jmp 0x140883f05
00884347  0F BA EA 09                     bts edx, 9
0088434B  E9 92 FE FF FF                  jmp 0x1408841e2
00884350  0F B6 47 39                     movzx eax, byte ptr [rdi + 0x39]
00884354  45 8B CC                        mov r9d, r12d
00884357  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
0088435B  48 8B CE                        mov rcx, rsi
0088435E  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
00884362  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00884367  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0088436B  E8 44 DC FF FF                  call 0x140881fb4
00884370  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00884373  85 C0                           test eax, eax
00884375  0F 88 8A FB FF FF               js 0x140883f05
0088437B  83 CB 04                        or ebx, 4
0088437E  E9 BF FC FF FF                  jmp 0x140884042
00884383  C7 45 AF 45 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000045
0088438A  E9 76 FB FF FF                  jmp 0x140883f05
0088438F  C7 45 AF 45 00 00 C0            mov dword ptr [rbp - 0x51], 0xc0000045
00884396  E9 6A FB FF FF                  jmp 0x140883f05
0088439B  F7 47 28 00 00 00 01            test dword ptr [rdi + 0x28], 0x1000000
008843A2  0F 84 F9 FA FF FF               je 0x140883ea1
008843A8  81 7D AF 34 04 00 C0            cmp dword ptr [rbp - 0x51], 0xc0000434
008843AF  0F 85 EC FA FF FF               jne 0x140883ea1
008843B5  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
008843B9  45 33 C0                        xor r8d, r8d
008843BC  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008843C0  E8 33 BF 1F 00                  call 0x140a802f8
008843C5  E9 D7 FA FF FF                  jmp 0x140883ea1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateVirtualMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int16 v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 5794781)) ^ (v_rsp);
    v_stack_m40 = result;
    a3 = 0;
    v_stack_m90 = a4;
    v_stack_m88 = a2;
    v_stack_m80 = a5;
    v_stack_m98 = 0;
    if (0 == 0) { a3 = 0; }
    v_stack_mA4 = (unsigned __int16)(a3);
    *(unsigned __int64 *)(a5) = a3;
    v_stack_mA0 = a3;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (a2 >= 2) goto loc_0088422D;
loc_00883BB9:
    a1 = (*(unsigned __int64 *)(a1 + 8)) - (*(unsigned __int64 *)(a1));
    a1 = (a1) + 1;
    v_rbx = 2;
    if (a1 != (*(unsigned __int64 *)(a1 + 24))) { v_rbx = (unsigned int)(a3); }
    result = MiMakeProtectionMask((unsigned int)(*(unsigned int *)(a1 + 44)), a2, a3, a4);
    if (((unsigned int)(result)) == -1) goto loc_00883E82;
    if ((*(unsigned __int64 *)(a1 + 96)) != (*(unsigned __int64 *)(a1 + 88))) goto loc_00883F0F;
loc_00883BF2:
    result = MiValidateVadMetadataFlags(a1, a2, a3, a4);
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883E8C;
    a1 = (((*(unsigned int *)(a1 + 64)) & (0x4000000ULL)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_rbx)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00884221;
    if (condition_is_below) goto loc_00884271;
loc_00883C2D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 112))) & (26));
    if (condition_is_not_equal) goto loc_0088428F;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) & (0x20400000ULL));
    if (((unsigned int)(a2)) == 0x20000000ULL) {
        v_rbx = (unsigned int)((v_rbx) | (16));
    }
    if (((unsigned int)(v_rbx)) >= 16) goto loc_008842A2;
    result = MiGetProcessPartition(*(unsigned __int64 *)(a1 + 88), a2, a3, a4);
    v_stack_mA4 = (unsigned __int16)(*(unsigned __int16 *)(result));
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))))) != 0) goto loc_00883E5E;
    if (condition_is_below) goto loc_008842C6;
    if ((*(unsigned __int64 *)(a1 + 72)) != 0) goto loc_008842D2;
    v_r15 = (*(unsigned __int64 *)(a1 + 8)) >> (12);
    v_stack_mA0 = *(unsigned __int64 *)(a1);
    result = (unsigned int)(*(unsigned int *)(a1 + 40));
    v_rsi = a3;
    if (a3 == 0) {
        a3 = v_stack_mA8;
        a2 = 0;
        result = MiObtainReferencedVadEx(*(unsigned __int64 *)(a1), a2, a3, a4);
        v_rsi = result;
    }
    if (v_rsi == 0) goto loc_008842DE;
    a1 = (*(unsigned __int8 *)(v_rsi + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_rsi + 28)));
    if (v_r15 > a1) goto loc_008842F7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) goto loc_00883CE8;
    if ((*(unsigned int *)(a1 + 48)) != 0) goto loc_00884303;
loc_00883CE8:
    *(unsigned __int64 *)(v_stack_m80) = v_stack_mA0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 48))))) & (0xC200000ULL));
    if (((unsigned int)(result)) == 0x8200000ULL) goto loc_00883FC5;
loc_00883D08:
    result = MiVadSupportsPrivateCommit(v_rsi, (unsigned int)(*(unsigned int *)(v_rsi + 48)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00884328;
    a2 = (*(unsigned __int8 *)(v_rsi + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_rsi + 52)));
    if (a2 >= result) goto loc_00883F36;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rsi + 48))) & (112));
    if (((unsigned __int8)(result)) == 64) goto loc_008840CB;
loc_00883D46:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (0x1080000ULL)) != 0) goto loc_00883EDB;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) != 0) goto loc_00883FF0;
loc_00883D63:
    if (condition_is_above_or_equal) goto loc_00883F4A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 44)))) & (136)) != 0) goto loc_0088411E;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 48))))) & (112));
    if (((unsigned __int8)(result)) == 64) goto loc_008841C6;
loc_00883D88:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 48)))) & (8)) != 0) goto loc_0088407B;
loc_00883D91:
    v_stack_mB8 = v_stack_mA4;
    v_stack_mC0 = v_stack_m98;
    v_stack_mC8 = v_stack_m88;
    v_stack_mD0 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 56));
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 52)));
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 112);
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    v_stack_m98 = 0;
    result = MiCommitExistingVad(v_rsi, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(a1 + 44)));
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883F05;
    result = MiUnlockAndDereferenceVad(v_rsi, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(a1 + 44)));
    if (v_stack_m98 != 0) goto loc_0088414A;
loc_00883E03:
loc_00883E09:
    if (((*(unsigned int *)(v_rip + 7613681)) & (0x8000ULL)) != 0) goto loc_00884197;
loc_00883E19:
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_00883F26;
loc_00883E22:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) != 0) goto loc_00883EB3;
loc_00883E2C:
    *(unsigned __int64 *)(v_stack_m80) = v_stack_mA0;
loc_00883E33:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(a1 + 44)));
    v_rsp = (v_rsp) + (208);
    return result;
loc_00883E5E:
    v_stack_p20 = v_stack_mA4;
    result = MiReserveUserMemory(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_mA0);
    v_stack_mA8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00883E09;
    goto loc_00883E8C;
loc_00883E82:
    v_stack_mA8 = 0xC0000045ULL;
loc_00883E89:
loc_00883E8C:
    if (v_stack_m90 != 0) goto loc_00883F05;
loc_00883E91:
    if (((*(unsigned int *)(v_rip + 7613545)) & (0x8000ULL)) != 0) goto loc_0088439B;
loc_00883EA1:
    if ((((unsigned __int8)(v_stack_p20)) & (1)) == 0) goto loc_00883E33;
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_mA0);
    goto loc_00883E33;
loc_00883EB3:
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    result = EtwTiLogAllocExecVm(*(unsigned __int64 *)(a1 + 88), *(unsigned __int8 *)(a1 + 57), v_stack_mA0, *(unsigned __int64 *)(a1 + 32));
    goto loc_00883E2C;
loc_00883EDB:
    v_stack_p28 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 57));
    v_stack_p20 = (unsigned int)(*(unsigned __int64 *)(a1 + 88));
    result = MiResetVirtualMemory(*(unsigned __int64 *)(a1 + 96), v_stack_mA0, (unsigned int)(0x2000ULL), v_stack_m90);
loc_00883EFA:
    v_stack_mA8 = (unsigned int)(result);
    if (!sign_flag) goto loc_008840BE;
loc_00883F05:
    result = MiUnlockAndDereferenceVad(v_stack_m90, v_stack_mA0, (unsigned int)(0x2000ULL), v_stack_m90);
    goto loc_00883E91;
loc_00883F0F:
    a2 = 0;
    result = KiStackAttachProcess(v_stack_m90, a2, v_stack_m70, v_stack_m90);
    v_rbx = (unsigned int)((v_stack_p20) | (1));
    goto loc_00883BF2;
loc_00883F26:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, a2, v_stack_m70, v_stack_m90);
    goto loc_00883E22;
loc_00883F36:
    v_stack_mA8 = 0xC0000018ULL;
    result = MiUnlockAndDereferenceVad(v_stack_m90, a2, v_stack_m70, v_stack_m90);
    goto loc_00883E91;
loc_00883F4A:
    if (((0) & (0x600ULL)) != 0) goto loc_00884383;
    a1 = ((((unsigned __int8)(v_stack_m90)) & (8)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_rbx)) & (4)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00883F91;
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 57));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883F05;
loc_00883F91:
    result = MiGetControlAreaPartition(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 72)), v_stack_mA0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 72)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA4 = (unsigned __int16)(*(unsigned __int16 *)(result));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 72)) + 64)) == 0) goto loc_00884071;
    result = MiCommitFileBackedSection(a1, v_stack_m90, v_stack_m90, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_00883EFA;
loc_00883FC5:
    a2 = (unsigned int)((v_stack_m90) & (112));
    if (((unsigned __int8)(a2)) != 48) goto loc_0088430F;
    v_stack_p28 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    result = MiCommitEnclavePages(a1, v_stack_m90, a1, (unsigned int)(0x2000ULL));
    goto loc_00883EFA;
loc_00883FF0:
    v_stack_p28 = (unsigned int)(0x2000ULL);
    v_stack_p20 = v_stack_mA0;
    result = MiAllowProtectionChange(*(unsigned __int64 *)(a1 + 88), *(unsigned __int64 *)(a1 + 96), v_stack_m90, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883F05;
    if (((*(unsigned int *)(v_stack_m90 + 48)) & (256)) != 0) goto loc_0088412A;
loc_00884029:
    if ((*(unsigned int *)(a1 + 120)) == 0) goto loc_00883D63;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 48)))) & (8)) != 0) goto loc_00884350;
loc_00884042:
    v_stack_m80 = v_stack_mA0;
    v_stack_m78 = (unsigned int)(0x2000ULL);
    result = MiCommitVadMetadataBits(v_stack_m90, v_stack_m80, (unsigned int)(*(unsigned int *)(a1 + 120)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883F05;
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_00883D63;
loc_00884071:
    result = MiCommitPagefileBackedSection(v_stack_m90, v_stack_m80, (unsigned int)(*(unsigned int *)(a1 + 120)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_00883EFA;
loc_0088407B:
    result = MiLocateLockedVadEvent(v_stack_m90, 64, (unsigned int)(*(unsigned int *)(a1 + 120)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (result != 0) goto loc_0088438F;
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 57));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00883D91;
    goto loc_00883F05;
loc_008840BE:
    result = MiUnlockAndDereferenceVad(v_stack_m90, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_00883E03;
loc_008840CB:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 44))) & (0xFFFFF9FFULL));
    *(unsigned int *)(a1 + 44) = (unsigned int)(a2);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 48))))) & (0xC00ULL));
    a1 = ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 48)))) & (896)) != 0) ? 1 : 0;
    result = (((unsigned int)(a3)) == 0xC00ULL) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_008841DE;
    if (((unsigned int)(a3)) == 0x400ULL) goto loc_00884347;
loc_0088410B:
    result = MiMakeProtectionMask((unsigned int)((unsigned int)(a2)), a2, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (((unsigned int)(result)) != -1) goto loc_00883D46;
loc_0088411E:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088412A:
    result = (unsigned int)(*(unsigned int *)(a1 + 120));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 120)))) & (2)) == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) & (0xFFFFFFFEULL));
        *(unsigned int *)(a1 + 120) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00884029;
    result = (unsigned int)((result) & (0xFFFFFFFBULL));
    *(unsigned int *)(a1 + 120) = (unsigned int)(result);
    goto loc_00884029;
loc_0088414A:
    v_stack_m88 = v_stack_mA0;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m90 = 0;
    a1 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44))));
    if ((((unsigned __int8)(v_rbx)) & (32)) == 0) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44))); }
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (unsigned int)(a1);
    result = MmProtectVirtualMemory(*(unsigned __int64 *)(a1 + 96), *(unsigned __int64 *)(a1 + 88), v_stack_m88, v_stack_m80);
    goto loc_00883E03;
loc_00884197:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (0x3000ULL)) != 0) goto loc_008841EA;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (0x1080000ULL)) == 0) goto loc_00883E19;
    result = MiLogMemResetInfo(v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))), (unsigned int)(*(unsigned int *)(a1 + 40)));
    goto loc_00883E19;
loc_008841C6:
    if ((((unsigned int)(*(unsigned __int64 *)(a1 + 24))) & (0xFFFFF9F9ULL)) == 0) goto loc_00883D88;
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_008841DE:
loc_008841E2:
    *(unsigned int *)(a1 + 44) = (unsigned int)(*(unsigned __int64 *)(a1 + 24));
    goto loc_0088410B;
loc_008841EA:
    result = MiGetProcessPartition(*(unsigned __int64 *)(a1 + 88), *(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 88), (unsigned int)(*(unsigned int *)(a1 + 40)));
    a4 = (unsigned int)(*(unsigned int *)(a1 + 40));
    if (((*(unsigned __int8 *)(a1 + 64)) & (1)) != 0) { a4 = (unsigned int)((unsigned int)(0x2000ULL)); }
    v_stack_p28 = (unsigned __int16)(v_stack_mA4);
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(result));
    result = PerfInfoLogVirtualAlloc(v_stack_mA0, *(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 88), a4);
    goto loc_00883E19;
loc_00884221:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_0088422D:
    if (!sign_flag) goto loc_0088424C;
    if (((*(unsigned __int8 *)(v_stack_mA0 + 112)) & (16)) == 0) goto loc_00884265;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA0 + 40))) & (0x20400000ULL));
    if (((unsigned int)(result)) != 0x20000000ULL) goto loc_00884265;
loc_0088424C:
    result = MiGetProcessPartition(*(unsigned __int64 *)(v_stack_mA0 + 88), *(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 88), a4);
    v_r10 = v_stack_m88;
    if ((*(unsigned __int64 *)(v_stack_m88)) == result) { v_r10 = *(unsigned __int64 *)(a1 + 88); }
    v_stack_m88 = v_r10;
    goto loc_00883BB9;
loc_00884265:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E89;
loc_00884271:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 1600)) != 0) goto loc_00883C2D;
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_0088428F:
loc_008842A2:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 7690275), *(unsigned __int8 *)(a1 + 57), (unsigned int)(0xFFFFULL), a4);
    v_stack_mA8 = 0xC0000061ULL;
    goto loc_00883E8C;
loc_008842C6:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_008842D2:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_008842DE:
    if (v_stack_mA8 != 0xC00000A0ULL) goto loc_00883E91;
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883E91;
loc_008842F7:
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_00884303:
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_0088430F:
    if (((*(unsigned int *)(a1 + 64)) & (0x10000000ULL)) != 0) goto loc_00883D08;
    v_stack_mA8 = 0xC00000A0ULL;
    goto loc_00883F05;
loc_00884328:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90 + 48))) & (0xA00000ULL));
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_00884347:
    goto loc_008841E2;
loc_00884350:
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 57));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(unsigned __int64 *)(a1 + 24), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_mA8 = (unsigned int)(result);
    if (sign_flag) goto loc_00883F05;
    v_rbx = (unsigned int)((v_rbx) | (4));
    goto loc_00884042;
loc_00884383:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088438F:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088439B:
    if (((*(unsigned int *)(a1 + 40)) & (0x1000000ULL)) == 0) goto loc_00883EA1;
    if (v_stack_mA8 != 0xC0000434ULL) goto loc_00883EA1;
    a3 = 0;
    result = MiLogMemResetInfo(v_stack_mA0, *(unsigned __int64 *)(a1 + 24), a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_00883EA1;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateVirtualMemory(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m57;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint16_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x586BDD)) ^ (local_rsp);
    v_stack_m40 = result;
    Arg3 = 0;
    v_stack_m90 = Arg4;
    v_stack_m88 = Arg2;
    v_stack_m80 = Arg5;
    v_stack_m98 = 0;
    if (0 == 0) { Arg3 = 0; }
    v_stack_mA4 = (uint16_t)(Arg3);
    *(uint64_t *)(arg5) = Arg3;
    v_stack_mA0 = Arg3;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (Arg2 >= 2) goto loc_0088422D;
loc_00883BB9:
    Arg1 = (*(uint64_t *)(arg1 + 0x8)) - (*(uint64_t *)(arg1));
    Arg1 = (Arg1) + 1;
    local_rbx = 2;
    if (Arg1 != (*(uint64_t *)(arg1 + 0x18))) { local_rbx = (uint32_t)(Arg3); }
    result = MiMakeProtectionMask((uint32_t)(*(uint32_t *)(arg1 + 0x2C)), Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == -1) goto loc_00883E82;
    if ((*(uint64_t *)(arg1 + 0x60)) != (*(uint64_t *)(arg1 + 0x58))) goto loc_00883F0F;
loc_00883BF2:
    result = MiValidateVadMetadataFlags(Arg1, Arg2, Arg3, Arg4);
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883E8C;
    Arg1 = (((*(uint32_t *)(arg1 + 0x40)) & (0x4000000ULL)) != 0) ? 1 : 0;
    result = ((((uint8_t)(local_rbx)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00884221;
    if (condition_is_below) goto loc_00884271;
loc_00883C2D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x70))) & (26));
    if (condition_is_not_equal) goto loc_0088428F;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) & (0x20400000ULL));
    if (((uint32_t)(Arg2)) == 0x20000000ULL) {
        local_rbx = (uint32_t)((local_rbx) | (16));
    }
    if (((uint32_t)(local_rbx)) >= 16) goto loc_008842A2;
    result = MiGetProcessPartition(*(uint64_t *)(arg1 + 0x58), Arg2, Arg3, Arg4);
    v_stack_mA4 = (uint16_t)(*(uint16_t *)(result));
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))))) != 0) goto loc_00883E5E;
    if (condition_is_below) goto loc_008842C6;
    if ((*(uint64_t *)(arg1 + 0x48)) != 0) goto loc_008842D2;
    local_r15 = (*(uint64_t *)(arg1 + 0x8)) >> (12);
    v_stack_mA0 = *(uint64_t *)(arg1);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x28));
    local_rsi = Arg3;
    if (Arg3 == 0) {
        Arg3 = v_stack_mA8;
        Arg2 = 0;
        result = MiObtainReferencedVadEx(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
        local_rsi = result;
    }
    if (local_rsi == 0) goto loc_008842DE;
    Arg1 = (*(uint8_t *)(local_rsi + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(local_rsi + 0x1C)));
    if (local_r15 > Arg1) goto loc_008842F7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) goto loc_00883CE8;
    if ((*(uint32_t *)(arg1 + 0x30)) != 0) goto loc_00884303;
loc_00883CE8:
    *(uint64_t *)(v_stack_m80) = v_stack_mA0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x30))))) & (0xC200000ULL));
    if (((uint32_t)(result)) == 0x8200000ULL) goto loc_00883FC5;
loc_00883D08:
    result = MiVadSupportsPrivateCommit(local_rsi, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00884328;
    Arg2 = (*(uint8_t *)(local_rsi + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
    if (Arg2 >= result) goto loc_00883F36;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x30))) & (112));
    if (((uint8_t)(result)) == 64) goto loc_008840CB;
loc_00883D46:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (0x1080000ULL)) != 0) goto loc_00883EDB;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) != 0) goto loc_00883FF0;
loc_00883D63:
    if (condition_is_above_or_equal) goto loc_00883F4A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))) & (136)) != 0) goto loc_0088411E;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x30))))) & (112));
    if (((uint8_t)(result)) == 64) goto loc_008841C6;
loc_00883D88:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x30)))) & (8)) != 0) goto loc_0088407B;
loc_00883D91:
    v_stack_mB8 = v_stack_mA4;
    v_stack_mC0 = v_stack_m98;
    v_stack_mC8 = v_stack_m88;
    v_stack_mD0 = (uint8_t)(*(uint8_t *)(arg1 + 0x38));
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x34)));
    v_stack_mE0 = *(uint64_t *)(arg1 + 0x70);
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    v_stack_m98 = 0;
    result = MiCommitExistingVad(local_rsi, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883F05;
    result = MiUnlockAndDereferenceVad(local_rsi, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    if (v_stack_m98 != 0) goto loc_0088414A;
loc_00883E03:
loc_00883E09:
    if (((*(uint32_t *)(v_rip + 0x742CF1)) & (0x8000ULL)) != 0) goto loc_00884197;
loc_00883E19:
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_00883F26;
loc_00883E22:
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) != 0) goto loc_00883EB3;
loc_00883E2C:
    *(uint64_t *)(v_stack_m80) = v_stack_mA0;
loc_00883E33:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    local_rsp = (local_rsp) + (208);
    return result;
loc_00883E5E:
    v_stack_p20 = v_stack_mA4;
    result = MiReserveUserMemory(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_mA0);
    v_stack_mA8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00883E09;
    goto loc_00883E8C;
loc_00883E82:
    v_stack_mA8 = 0xC0000045ULL;
loc_00883E89:
loc_00883E8C:
    if (v_stack_m90 != 0) goto loc_00883F05;
loc_00883E91:
    if (((*(uint32_t *)(v_rip + 0x742C69)) & (0x8000ULL)) != 0) goto loc_0088439B;
loc_00883EA1:
    if ((((uint8_t)(v_stack_p20)) & (1)) == 0) goto loc_00883E33;
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_mA0);
    goto loc_00883E33;
loc_00883EB3:
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    result = EtwTiLogAllocExecVm(*(uint64_t *)(arg1 + 0x58), *(uint8_t *)(arg1 + 0x39), v_stack_mA0, *(uint64_t *)(arg1 + 0x20));
    goto loc_00883E2C;
loc_00883EDB:
    v_stack_p28 = (uint8_t)(*(uint8_t *)(arg1 + 0x39));
    v_stack_p20 = (uint32_t)(*(uint64_t *)(arg1 + 0x58));
    result = MiResetVirtualMemory(*(uint64_t *)(arg1 + 0x60), v_stack_mA0, (uint32_t)(0x2000ULL), v_stack_m90);
loc_00883EFA:
    v_stack_mA8 = (uint32_t)(result);
    if (!sign_flag) goto loc_008840BE;
loc_00883F05:
    result = MiUnlockAndDereferenceVad(v_stack_m90, v_stack_mA0, (uint32_t)(0x2000ULL), v_stack_m90);
    goto loc_00883E91;
loc_00883F0F:
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_m90, Arg2, v_stack_m70, v_stack_m90);
    local_rbx = (uint32_t)((v_stack_p20) | (1));
    goto loc_00883BF2;
loc_00883F26:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, Arg2, v_stack_m70, v_stack_m90);
    goto loc_00883E22;
loc_00883F36:
    v_stack_mA8 = 0xC0000018ULL;
    result = MiUnlockAndDereferenceVad(v_stack_m90, Arg2, v_stack_m70, v_stack_m90);
    goto loc_00883E91;
loc_00883F4A:
    if (((0) & (0x600ULL)) != 0) goto loc_00884383;
    Arg1 = ((((uint8_t)(v_stack_m90)) & (8)) != 0) ? 1 : 0;
    result = ((((uint8_t)(local_rbx)) & (4)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00883F91;
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg1 + 0x39));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883F05;
loc_00883F91:
    result = MiGetControlAreaPartition(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x48)), v_stack_mA0, *(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x48)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA4 = (uint16_t)(*(uint16_t *)(result));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x48)) + 0x40)) == 0) goto loc_00884071;
    result = MiCommitFileBackedSection(Arg1, v_stack_m90, v_stack_m90, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_00883EFA;
loc_00883FC5:
    Arg2 = (uint32_t)((v_stack_m90) & (112));
    if (((uint8_t)(Arg2)) != 48) goto loc_0088430F;
    v_stack_p28 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    result = MiCommitEnclavePages(Arg1, v_stack_m90, Arg1, (uint32_t)(0x2000ULL));
    goto loc_00883EFA;
loc_00883FF0:
    v_stack_p28 = (uint32_t)(0x2000ULL);
    v_stack_p20 = v_stack_mA0;
    result = MiAllowProtectionChange(*(uint64_t *)(arg1 + 0x58), *(uint64_t *)(arg1 + 0x60), v_stack_m90, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883F05;
    if (((*(uint32_t *)(v_stack_m90 + 0x30)) & (256)) != 0) goto loc_0088412A;
loc_00884029:
    if ((*(uint32_t *)(arg1 + 0x78)) == 0) goto loc_00883D63;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x30)))) & (8)) != 0) goto loc_00884350;
loc_00884042:
    v_stack_m80 = v_stack_mA0;
    v_stack_m78 = (uint32_t)(0x2000ULL);
    result = MiCommitVadMetadataBits(v_stack_m90, v_stack_m80, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883F05;
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_00883D63;
loc_00884071:
    result = MiCommitPagefileBackedSection(v_stack_m90, v_stack_m80, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_00883EFA;
loc_0088407B:
    result = MiLocateLockedVadEvent(v_stack_m90, 64, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (result != 0) goto loc_0088438F;
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg1 + 0x39));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00883D91;
    goto loc_00883F05;
loc_008840BE:
    result = MiUnlockAndDereferenceVad(v_stack_m90, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_00883E03;
loc_008840CB:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) & (0xFFFFF9FFULL));
    *(uint32_t *)(arg1 + 0x2C) = (uint32_t)(Arg2);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x30))))) & (0xC00ULL));
    Arg1 = ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x30)))) & (896)) != 0) ? 1 : 0;
    result = (((uint32_t)(Arg3)) == 0xC00ULL) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_008841DE;
    if (((uint32_t)(Arg3)) == 0x400ULL) goto loc_00884347;
loc_0088410B:
    result = MiMakeProtectionMask((uint32_t)((uint32_t)(Arg2)), Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (((uint32_t)(result)) != -1) goto loc_00883D46;
loc_0088411E:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088412A:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x78));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)))) & (2)) == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) & (0xFFFFFFFEULL));
        *(uint32_t *)(arg1 + 0x78) = (uint32_t)(result);
    }
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00884029;
    result = (uint32_t)((result) & (0xFFFFFFFBULL));
    *(uint32_t *)(arg1 + 0x78) = (uint32_t)(result);
    goto loc_00884029;
loc_0088414A:
    v_stack_m88 = v_stack_mA0;
    v_stack_m80 = *(uint64_t *)(arg1 + 0x18);
    v_stack_m90 = 0;
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C))));
    if ((((uint8_t)(local_rbx)) & (32)) == 0) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C))); }
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (uint32_t)(Arg1);
    result = MmProtectVirtualMemory(*(uint64_t *)(arg1 + 0x60), *(uint64_t *)(arg1 + 0x58), v_stack_m88, v_stack_m80);
    goto loc_00883E03;
loc_00884197:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (0x3000ULL)) != 0) goto loc_008841EA;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (0x1080000ULL)) == 0) goto loc_00883E19;
    result = MiLogMemResetInfo(v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))), (uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    goto loc_00883E19;
loc_008841C6:
    if ((((uint32_t)(*(uint64_t *)(arg1 + 0x18))) & (0xFFFFF9F9ULL)) == 0) goto loc_00883D88;
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_008841DE:
loc_008841E2:
    *(uint32_t *)(arg1 + 0x2C) = (uint32_t)(*(uint64_t *)(arg1 + 0x18));
    goto loc_0088410B;
loc_008841EA:
    result = MiGetProcessPartition(*(uint64_t *)(arg1 + 0x58), *(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x58), (uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    Arg4 = (uint32_t)(*(uint32_t *)(arg1 + 0x28));
    if (((*(uint8_t *)(arg1 + 0x40)) & (1)) != 0) { Arg4 = (uint32_t)((uint32_t)(0x2000ULL)); }
    v_stack_p28 = (uint16_t)(v_stack_mA4);
    v_stack_p20 = (uint16_t)(*(uint16_t *)(result));
    result = PerfInfoLogVirtualAlloc(v_stack_mA0, *(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x58), Arg4);
    goto loc_00883E19;
loc_00884221:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_0088422D:
    if (!sign_flag) goto loc_0088424C;
    if (((*(uint8_t *)(v_stack_mA0 + 0x70)) & (16)) == 0) goto loc_00884265;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x28))) & (0x20400000ULL));
    if (((uint32_t)(result)) != 0x20000000ULL) goto loc_00884265;
loc_0088424C:
    result = MiGetProcessPartition(*(uint64_t *)(v_stack_mA0 + 0x58), *(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x58), Arg4);
    local_r10 = v_stack_m88;
    if ((*(uint64_t *)(v_stack_m88)) == result) { local_r10 = *(uint64_t *)(arg1 + 0x58); }
    v_stack_m88 = local_r10;
    goto loc_00883BB9;
loc_00884265:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E89;
loc_00884271:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x640)) != 0) goto loc_00883C2D;
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_0088428F:
loc_008842A2:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x755823), *(uint8_t *)(arg1 + 0x39), (uint32_t)(0xFFFFULL), Arg4);
    v_stack_mA8 = 0xC0000061ULL;
    goto loc_00883E8C;
loc_008842C6:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_008842D2:
    v_stack_mA8 = 0xC000000DULL;
    goto loc_00883E8C;
loc_008842DE:
    if (v_stack_mA8 != 0xC00000A0ULL) goto loc_00883E91;
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883E91;
loc_008842F7:
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_00884303:
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_0088430F:
    if (((*(uint32_t *)(arg1 + 0x40)) & (0x10000000ULL)) != 0) goto loc_00883D08;
    v_stack_mA8 = 0xC00000A0ULL;
    goto loc_00883F05;
loc_00884328:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x30))) & (0xA00000ULL));
    v_stack_mA8 = 0xC0000018ULL;
    goto loc_00883F05;
loc_00884347:
    goto loc_008841E2;
loc_00884350:
    v_stack_p28 = v_stack_m90;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg1 + 0x39));
    result = MiCheckSecuredVad(v_stack_m90, v_stack_mA0, *(uint64_t *)(arg1 + 0x18), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_mA8 = (uint32_t)(result);
    if (sign_flag) goto loc_00883F05;
    local_rbx = (uint32_t)((local_rbx) | (4));
    goto loc_00884042;
loc_00884383:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088438F:
    v_stack_mA8 = 0xC0000045ULL;
    goto loc_00883F05;
loc_0088439B:
    if (((*(uint32_t *)(arg1 + 0x28)) & (0x1000000ULL)) == 0) goto loc_00883EA1;
    if (v_stack_mA8 != 0xC0000434ULL) goto loc_00883EA1;
    Arg3 = 0;
    result = MiLogMemResetInfo(v_stack_mA0, *(uint64_t *)(arg1 + 0x18), Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_00883EA1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `W` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x38` | `8` | `R` |
| `Arg1` | `+ 0x39` | `8` | `R` |
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00883B40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
