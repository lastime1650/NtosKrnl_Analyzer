# IopGetSetSecurityObject

- RVA: `0x00873A80`–`0x0087408E` (길이 `1,550` bytes)
- VA: `0x0000000140873A80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C76C`
- 디코드: `352`개 명령, `1,550/1,550` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00873B1D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00873B3B` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00873B46` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x00873B4E` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00873B65` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x00873BF5` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x00873C18` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x00873C49` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00873CAB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00873CD8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00873D05` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00873D4C` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00873D5B` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x00873D99` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00873DCA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00873DD2` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00873DEA` → [SeQuerySecurityDescriptorInfo](SeQuerySecurityDescriptorInfo_function_00872820.md) (function, `0x00872820`)
- `0x00873E04` → [ObDereferenceSecurityDescriptor](ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x00873E51` → [ObLogSecurityDescriptor](../8C/ObLogSecurityDescriptor_function_008C0020.md) (function, `0x008C0020`)
- `0x00873E69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00873E88` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00873EAE` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00873EB6` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00873EC7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00873F00` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00873F31` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00873F39` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00873F75` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x00873F8F` → [SeAssignWorldSecurityDescriptor](../A7/SeAssignWorldSecurityDescriptor_function_00A70D20.md) (function, `0x00A70D20`)
- `0x00873FAD` → [IopGetDevicePDO](../../text/27/IopGetDevicePDO_function_002724D8.md) (function, `0x002724D8`)
- `0x00873FD8` → [IopSetDeviceSecurityDescriptor](../A7/IopSetDeviceSecurityDescriptor_function_00A7199C.md) (function, `0x00A7199C`)
- `0x00873FE2` → [AstLogDeviceSDDLUpdated](../9A/AstLogDeviceSDDLUpdated_function_009A36A8.md) (function, `0x009A36A8`)
- `0x0087401C` → [IopSetDeviceSecurityDescriptors](../A7/IopSetDeviceSecurityDescriptors_function_00A718FC.md) (function, `0x00A718FC`)
- `0x00874026` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0087402E` → [AstLogDeviceSDDLUpdated](../9A/AstLogDeviceSDDLUpdated_function_009A36A8.md) (function, `0x009A36A8`)
- `0x00874047` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)

### Direct callers
- [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) at `0x0086D03E`
- [ObpGrantAccess](../86/ObpGrantAccess_function_0086F250.md) at `0x0086F78C`
- [ObpGetObjectSecurity](ObpGetObjectSecurity_function_008717E0.md) at `0x008719DA`
- [ObCheckObjectAccess](ObCheckObjectAccess_function_00872260.md) at `0x0087267E`
- [NtQuerySecurityObject](NtQuerySecurityObject_function_008737B0.md) at `0x008739AC`
- [ObpAllocateAndQuerySecurityDescriptorInfo](ObpAllocateAndQuerySecurityDescriptorInfo_function_0087421C.md) at `0x008742F6`
- [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) at `0x008B6BF9`
- [ObGetObjectSecurity](../9D/ObGetObjectSecurity_function_009D45F0.md) at `0x009D47D7`

### Static image references
- `0x00873D92` → RVA `0x00F8D2A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x00873B1D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00873B3B` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x00873B46` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x00873B4E` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x00873B65` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x00873BF5` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x00873C18` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x00873C49` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00873CAB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00873CD8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00873D05` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00873D4C` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00873D5B` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x00873D99` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00873DCA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00873DD2` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00873E69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00873E88` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00873EAE` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00873EB6` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00873EC7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00873F00` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00873F31` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00873F39` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00873FAD` → [IopGetDevicePDO](../../text/27/IopGetDevicePDO_function_002724D8.md) (`PAGE` → `.text`)
  - `0x00874026` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00874047` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00873A80  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00873A85  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00873A8A  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00873A8F  57                              push rdi
00873A90  41 54                           push r12
00873A92  41 55                           push r13
00873A94  41 56                           push r14
00873A96  41 57                           push r15
00873A98  48 83 EC 70                     sub rsp, 0x70
00873A9C  4D 8B E9                        mov r13, r9
00873A9F  49 8B F8                        mov rdi, r8
00873AA2  8B F2                           mov esi, edx
00873AA4  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
00873AAD  0F B7 01                        movzx eax, word ptr [rcx]
00873AB0  66 83 F8 03                     cmp ax, 3
00873AB4  0F 84 76 03 00 00               je 0x140873e30
00873ABA  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
00873ABE  33 DB                           xor ebx, ebx
00873AC0  66 83 F8 03                     cmp ax, 3
00873AC4  48 0F 45 D9                     cmovne rbx, rcx
00873AC8  48 85 DB                        test rbx, rbx
00873ACB  0F 84 94 02 00 00               je 0x140873d65
00873AD1  66 83 7B 58 00                  cmp word ptr [rbx + 0x58], 0
00873AD6  0F 84 44 03 00 00               je 0x140873e20
00873ADC  F7 43 50 00 08 00 00            test dword ptr [rbx + 0x50], 0x800
00873AE3  0F 85 7C 02 00 00               jne 0x140873d65
00873AE9  83 FE 02                        cmp esi, 2
00873AEC  0F 84 64 04 00 00               je 0x140873f56
00873AF2  0F 57 C0                        xorps xmm0, xmm0
00873AF5  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00873AFA  0F 57 C9                        xorps xmm1, xmm1
00873AFD  33 C0                           xor eax, eax
00873AFF  0F 11 4C 24 58                  movups xmmword ptr [rsp + 0x58], xmm1
00873B04  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00873B09  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00873B12  45 0F B6 BE 32 02 00 00         movzx r15d, byte ptr [r14 + 0x232]
00873B1A  48 8B CB                        mov rcx, rbx
00873B1D  E8 FE BE 99 FF                  call 0x14020fa20
00873B22  8B 7B 50                        mov edi, dword ptr [rbx + 0x50]
00873B25  45 33 C0                        xor r8d, r8d
00873B28  40 F6 C7 02                     test dil, 2
00873B2C  0F 85 85 01 00 00               jne 0x140873cb7
00873B32  41 8D 50 01                     lea edx, [r8 + 1]
00873B36  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00873B3B  E8 D0 A1 B9 FF                  call 0x14040dd10
00873B40  45 32 E4                        xor r12b, r12b
00873B43  48 8B CB                        mov rcx, rbx
00873B46  E8 A5 9A A2 FF                  call 0x14029d5f0
00873B4B  48 8B CB                        mov rcx, rbx
00873B4E  E8 CD 75 A2 FF                  call 0x14029b120
00873B53  4C 8B F8                        mov r15, rax
00873B56  45 0F B6 C4                     movzx r8d, r12b
00873B5A  41 80 F0 01                     xor r8b, 1
00873B5E  0F B6 50 4C                     movzx edx, byte ptr [rax + 0x4c]
00873B62  48 8B C8                        mov rcx, rax
00873B65  E8 B6 3B 99 FF                  call 0x140207720
00873B6A  48 8B F8                        mov rdi, rax
00873B6D  48 85 C0                        test rax, rax
00873B70  0F 84 27 01 00 00               je 0x140873c9d
00873B76  48 89 98 C0 00 00 00            mov qword ptr [rax + 0xc0], rbx
00873B7D  4C 89 B0 98 00 00 00            mov qword ptr [rax + 0x98], r14
00873B84  0F B6 84 24 E0 00 00 00         movzx eax, byte ptr [rsp + 0xe0]
00873B8C  88 47 40                        mov byte ptr [rdi + 0x40], al
00873B8F  8B 43 50                        mov eax, dword ptr [rbx + 0x50]
00873B92  A8 02                           test al, 2
00873B94  0F 85 88 01 00 00               jne 0x140873d22
00873B9A  C7 47 10 04 00 00 00            mov dword ptr [rdi + 0x10], 4
00873BA1  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00873BA6  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
00873BAA  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00873BAF  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
00873BB3  48 C7 47 58 00 00 00 00         mov qword ptr [rdi + 0x58], 0
00873BBB  48 8B 8F B8 00 00 00            mov rcx, qword ptr [rdi + 0xb8]
00873BC2  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00873BCA  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
00873BD2  83 FE 01                        cmp esi, 1
00873BD5  0F 85 33 02 00 00               jne 0x140873e0e
00873BDB  C6 41 B8 14                     mov byte ptr [rcx - 0x48], 0x14
00873BDF  8B 00                           mov eax, dword ptr [rax]
00873BE1  89 41 C0                        mov dword ptr [rcx - 0x40], eax
00873BE4  41 8B 06                        mov eax, dword ptr [r14]
00873BE7  89 41 C8                        mov dword ptr [rcx - 0x38], eax
00873BEA  4C 89 6F 70                     mov qword ptr [rdi + 0x70], r13
00873BEE  48 89 59 E8                     mov qword ptr [rcx - 0x18], rbx
00873BF2  48 8B CF                        mov rcx, rdi
00873BF5  E8 C6 39 99 FF                  call 0x1402075c0
00873BFA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00873C03  48 FF 80 90 03 00 00            inc qword ptr [rax + 0x390]
00873C0A  65 FF 04 25 E4 2E 00 00         inc dword ptr gs:[0x2ee4]
00873C12  48 8B D7                        mov rdx, rdi
00873C15  49 8B CF                        mov rcx, r15
00873C18  E8 93 78 A2 FF                  call 0x14029b4b0
00873C1D  8B F8                           mov edi, eax
00873C1F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00873C23  45 84 E4                        test r12b, r12b
00873C26  0F 85 01 01 00 00               jne 0x140873d2d
00873C2C  3D 03 01 00 00                  cmp eax, 0x103
00873C31  75 23                           jne 0x140873c56
00873C33  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00873C3C  45 33 C9                        xor r9d, r9d
00873C3F  45 33 C0                        xor r8d, r8d
00873C42  33 D2                           xor edx, edx
00873C44  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00873C49  E8 62 AA 99 FF                  call 0x14020e6b0
00873C4E  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
00873C52  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00873C56  81 FF 10 00 00 C0               cmp edi, 0xc0000010
00873C5C  0F 84 6F 02 00 00               je 0x140873ed1
00873C62  83 FE 01                        cmp esi, 1
00873C65  75 19                           jne 0x140873c80
00873C67  B8 23 00 00 C0                  mov eax, 0xc0000023
00873C6C  81 FF 05 00 00 80               cmp edi, 0x80000005
00873C72  0F 44 F8                        cmove edi, eax
00873C75  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00873C79  41 89 06                        mov dword ptr [r14], eax
00873C7C  EB 02                           jmp 0x140873c80
00873C7E  8B F8                           mov edi, eax
00873C80  8B C7                           mov eax, edi
00873C82  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00873C87  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00873C8B  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00873C8F  49 8B E3                        mov rsp, r11
00873C92  41 5F                           pop r15
00873C94  41 5E                           pop r14
00873C96  41 5D                           pop r13
00873C98  41 5C                           pop r12
00873C9A  5F                              pop rdi
00873C9B  C3                              ret
00873C9C  CC                              int3
00873C9D  8B 43 50                        mov eax, dword ptr [rbx + 0x50]
00873CA0  A8 02                           test al, 2
00873CA2  0F 85 9C 03 00 00               jne 0x140874044
00873CA8  48 8B CB                        mov rcx, rbx
00873CAB  E8 A0 56 A8 FF                  call 0x1402f9350
00873CB0  B8 9A 00 00 C0                  mov eax, 0xc000009a
00873CB5  EB CB                           jmp 0x140873c82
00873CB7  C1 EF 02                        shr edi, 2
00873CBA  40 80 E7 01                     and dil, 1
00873CBE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00873CC7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00873CCE  90                              nop
00873CCF  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
00873CD6  33 D2                           xor edx, edx
00873CD8  E8 53 C5 99 FF                  call 0x140210230
00873CDD  4C 8B C8                        mov r9, rax
00873CE0  C6 84 24 A0 00 00 00 00         mov byte ptr [rsp + 0xa0], 0
00873CE8  B8 01 00 00 00                  mov eax, 1
00873CED  87 43 74                        xchg dword ptr [rbx + 0x74], eax
00873CF0  85 C0                           test eax, eax
00873CF2  0F 85 65 02 00 00               jne 0x140873f5d
00873CF8  4D 85 C9                        test r9, r9
00873CFB  74 05                           je 0x140873d02
00873CFD  41 C6 41 0A 01                  mov byte ptr [r9 + 0xa], 1
00873D02  48 8B CB                        mov rcx, rbx
00873D05  E8 16 BD 99 FF                  call 0x14020fa20
00873D0A  33 FF                           xor edi, edi
00873D0C  80 BC 24 A0 00 00 00 00         cmp byte ptr [rsp + 0xa0], 0
00873D14  0F 85 AA 01 00 00               jne 0x140873ec4
00873D1A  41 B4 01                        mov r12b, 1
00873D1D  E9 21 FE FF FF                  jmp 0x140873b43
00873D22  80 4F 47 02                     or byte ptr [rdi + 0x47], 2
00873D26  33 C0                           xor eax, eax
00873D28  E9 79 FE FF FF                  jmp 0x140873ba6
00873D2D  3D 03 01 00 00                  cmp eax, 0x103
00873D32  75 24                           jne 0x140873d58
00873D34  48 8D 8B 98 00 00 00            lea rcx, [rbx + 0x98]
00873D3B  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00873D44  45 33 C9                        xor r9d, r9d
00873D47  45 33 C0                        xor r8d, r8d
00873D4A  33 D2                           xor edx, edx
00873D4C  E8 5F A9 99 FF                  call 0x14020e6b0
00873D51  8B 7B 38                        mov edi, dword ptr [rbx + 0x38]
00873D54  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00873D58  48 8B CB                        mov rcx, rbx
00873D5B  E8 30 CD 9D FF                  call 0x140250a90
00873D60  E9 F1 FE FF FF                  jmp 0x140873c56
00873D65  83 FE 03                        cmp esi, 3
00873D68  0F 84 CA 00 00 00               je 0x140873e38
00873D6E  85 F6                           test esi, esi
00873D70  0F 84 34 02 00 00               je 0x140873faa
00873D76  83 FE 01                        cmp esi, 1
00873D79  0F 85 D7 01 00 00               jne 0x140873f56
00873D7F  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00873D88  66 FF 8E E4 01 00 00            dec word ptr [rsi + 0x1e4]
00873D8F  90                              nop
00873D90  B2 01                           mov dl, 1
00873D92  48 8D 0D 07 95 71 00            lea rcx, [rip + 0x719507]
00873D99  E8 22 DE 99 FF                  call 0x140211bc0
00873D9E  49 8B 9E 10 01 00 00            mov rbx, qword ptr [r14 + 0x110]
00873DA5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00873DAA  48 85 DB                        test rbx, rbx
00873DAD  74 14                           je 0x140873dc3
00873DAF  B8 01 00 00 00                  mov eax, 1
00873DB4  F0 48 0F C1 43 E8               lock xadd qword ptr [rbx - 0x18], rax
00873DBA  48 85 C0                        test rax, rax
00873DBD  0F 8E 29 02 00 00               jle 0x140873fec
00873DC3  48 8D 0D D6 94 71 00            lea rcx, [rip + 0x7194d6]
00873DCA  E8 41 BC 9E FF                  call 0x14025fa10
00873DCF  48 8B CE                        mov rcx, rsi
00873DD2  E8 39 B2 9E FF                  call 0x14025f010
00873DD7  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00873DDF  48 8B CF                        mov rcx, rdi
00873DE2  49 8B D5                        mov rdx, r13
00873DE5  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00873DEA  E8 31 EA FF FF                  call 0x140872820
00873DEF  8B F8                           mov edi, eax
00873DF1  48 85 DB                        test rbx, rbx
00873DF4  0F 84 86 FE FF FF               je 0x140873c80
00873DFA  BA 01 00 00 00                  mov edx, 1
00873DFF  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00873E04  E8 97 02 00 00                  call 0x1408740a0
00873E09  E9 72 FE FF FF                  jmp 0x140873c80
00873E0E  C6 41 B8 15                     mov byte ptr [rcx - 0x48], 0x15
00873E12  8B 00                           mov eax, dword ptr [rax]
00873E14  89 41 C0                        mov dword ptr [rcx - 0x40], eax
00873E17  4C 89 69 C8                     mov qword ptr [rcx - 0x38], r13
00873E1B  E9 CE FD FF FF                  jmp 0x140873bee
00873E20  48 83 7B 40 00                  cmp qword ptr [rbx + 0x40], 0
00873E25  0F 85 B1 FC FF FF               jne 0x140873adc
00873E2B  E9 35 FF FF FF                  jmp 0x140873d65
00873E30  4C 8B F1                        mov r14, rcx
00873E33  E9 86 FC FF FF                  jmp 0x140873abe
00873E38  33 FF                           xor edi, edi
00873E3A  48 85 DB                        test rbx, rbx
00873E3D  0F 85 26 02 00 00               jne 0x140874069
00873E43  41 B8 01 00 00 00               mov r8d, 1
00873E49  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00873E4E  49 8B CD                        mov rcx, r13
00873E51  E8 CA C1 04 00                  call 0x1408c0020
00873E56  8B F8                           mov edi, eax
00873E58  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00873E5C  85 C0                           test eax, eax
00873E5E  0F 88 1C FE FF FF               js 0x140873c80
00873E64  33 D2                           xor edx, edx
00873E66  49 8B CD                        mov rcx, r13
00873E69  E8 02 EA 30 00                  call 0x140b82870
00873E6E  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00873E77  66 FF 8B E4 01 00 00            dec word ptr [rbx + 0x1e4]
00873E7E  90                              nop
00873E7F  B2 01                           mov dl, 1
00873E81  48 8D 0D 18 94 71 00            lea rcx, [rip + 0x719418]
00873E88  E8 93 0F 9A FF                  call 0x140214e20
00873E8D  49 83 BE 10 01 00 00 00         cmp qword ptr [r14 + 0x110], 0
00873E95  0F 85 E0 01 00 00               jne 0x14087407b
00873E9B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00873EA0  49 89 86 10 01 00 00            mov qword ptr [r14 + 0x110], rax
00873EA7  48 8D 0D F2 93 71 00            lea rcx, [rip + 0x7193f2]
00873EAE  E8 5D BB 9E FF                  call 0x14025fa10
00873EB3  48 8B CB                        mov rcx, rbx
00873EB6  E8 55 B1 9E FF                  call 0x14025f010
00873EBB  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00873EBF  E9 BC FD FF FF                  jmp 0x140873c80
00873EC4  48 8B CB                        mov rcx, rbx
00873EC7  E8 84 54 A8 FF                  call 0x1402f9350
00873ECC  E9 AF FD FF FF                  jmp 0x140873c80
00873ED1  83 FE 01                        cmp esi, 1
00873ED4  75 78                           jne 0x140873f4e
00873ED6  41 F7 47 34 00 01 00 00         test dword ptr [r15 + 0x34], 0x100
00873EDE  0F 84 9D 00 00 00               je 0x140873f81
00873EE4  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00873EED  66 FF 8F E4 01 00 00            dec word ptr [rdi + 0x1e4]
00873EF4  90                              nop
00873EF5  40 0F B6 D6                     movzx edx, sil
00873EF9  48 8D 0D A0 93 71 00            lea rcx, [rip + 0x7193a0]
00873F00  E8 BB DC 99 FF                  call 0x140211bc0
00873F05  49 8B 9F 10 01 00 00            mov rbx, qword ptr [r15 + 0x110]
00873F0C  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00873F11  48 85 DB                        test rbx, rbx
00873F14  74 14                           je 0x140873f2a
00873F16  B8 01 00 00 00                  mov eax, 1
00873F1B  F0 48 0F C1 43 E8               lock xadd qword ptr [rbx - 0x18], rax
00873F21  48 85 C0                        test rax, rax
00873F24  0F 8E 0E 01 00 00               jle 0x140874038
00873F2A  48 8D 0D 6F 93 71 00            lea rcx, [rip + 0x71936f]
00873F31  E8 DA BA 9E FF                  call 0x14025fa10
00873F36  48 8B CF                        mov rcx, rdi
00873F39  E8 D2 B0 9E FF                  call 0x14025f010
00873F3E  4D 8B C6                        mov r8, r14
00873F41  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00873F49  E9 94 FE FF FF                  jmp 0x140873de2
00873F4E  85 F6                           test esi, esi
00873F50  0F 84 FB 00 00 00               je 0x140874051
00873F56  33 FF                           xor edi, edi
00873F58  E9 23 FD FF FF                  jmp 0x140873c80
00873F5D  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00873F65  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00873F6A  44 0F B6 C7                     movzx r8d, dil
00873F6E  41 0F B6 D7                     movzx edx, r15b
00873F72  48 8B CB                        mov rcx, rbx
00873F75  E8 5E A7 03 00                  call 0x1408ae6d8
00873F7A  8B F8                           mov edi, eax
00873F7C  E9 8B FD FF FF                  jmp 0x140873d0c
00873F81  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00873F89  49 8B D6                        mov rdx, r14
00873F8C  49 8B CD                        mov rcx, r13
00873F8F  E8 8C CD 1F 00                  call 0x140a70d20
00873F94  8B F8                           mov edi, eax
00873F96  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00873F9A  E9 E1 FC FF FF                  jmp 0x140873c80
00873F9F  8B F8                           mov edi, eax
00873FA1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00873FA5  E9 D6 FC FF FF                  jmp 0x140873c80
00873FAA  49 8B CE                        mov rcx, r14
00873FAD  E8 26 E5 9F FF                  call 0x1402724d8
00873FB2  48 8B D8                        mov rbx, rax
00873FB5  48 85 C0                        test rax, rax
00873FB8  75 3E                           jne 0x140873ff8
00873FBA  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00873FC2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00873FC7  44 8B 8C 24 D0 00 00 00         mov r9d, dword ptr [rsp + 0xd0]
00873FCF  4D 8B C5                        mov r8, r13
00873FD2  48 8B D7                        mov rdx, rdi
00873FD5  49 8B CE                        mov rcx, r14
00873FD8  E8 BF D9 1F 00                  call 0x140a7199c
00873FDD  8B F8                           mov edi, eax
00873FDF  49 8B CE                        mov rcx, r14
00873FE2  E8 C1 F6 12 00                  call 0x1409a36a8
00873FE7  E9 94 FC FF FF                  jmp 0x140873c80
00873FEC  B9 0E 00 00 00                  mov ecx, 0xe
00873FF1  CD 29                           int 0x29
00873FF3  E9 CB FD FF FF                  jmp 0x140873dc3
00873FF8  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00874000  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00874005  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
0087400C  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00874010  4D 8B CD                        mov r9, r13
00874013  4C 8B C7                        mov r8, rdi
00874016  48 8B D3                        mov rdx, rbx
00874019  49 8B CE                        mov rcx, r14
0087401C  E8 DB D8 1F 00                  call 0x140a718fc
00874021  8B F8                           mov edi, eax
00874023  48 8B CB                        mov rcx, rbx
00874026  E8 25 53 A8 FF                  call 0x1402f9350
0087402B  49 8B CE                        mov rcx, r14
0087402E  E8 75 F6 12 00                  call 0x1409a36a8
00874033  E9 48 FC FF FF                  jmp 0x140873c80
00874038  B9 0E 00 00 00                  mov ecx, 0xe
0087403D  CD 29                           int 0x29
0087403F  E9 E6 FE FF FF                  jmp 0x140873f2a
00874044  48 8B CB                        mov rcx, rbx
00874047  E8 44 CA 9D FF                  call 0x140250a90
0087404C  E9 57 FC FF FF                  jmp 0x140873ca8
00874051  41 F7 47 30 00 01 00 00         test dword ptr [r15 + 0x30], 0x100
00874059  0F 84 F7 FE FF FF               je 0x140873f56
0087405F  BF 10 00 00 C0                  mov edi, 0xc0000010
00874064  E9 17 FC FF FF                  jmp 0x140873c80
00874069  F7 43 50 00 01 00 00            test dword ptr [rbx + 0x50], 0x100
00874070  0F 85 0A FC FF FF               jne 0x140873c80
00874076  E9 C8 FD FF FF                  jmp 0x140873e43
0087407B  49 8B 86 38 01 00 00            mov rax, qword ptr [r14 + 0x138]
00874082  81 60 20 FF F7 FF FF            and dword ptr [rax + 0x20], 0xfffff7ff
00874089  E9 0D FE FF FF                  jmp 0x140873e9b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetSetSecurityObject(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p40;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    v_stack_m58 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) == 3) goto loc_00873E30;
loc_00873ABE:
    v_rbx = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) != 3) { v_rbx = a1; }
    if (v_rbx == 0) goto loc_00873D65;
    if ((*(unsigned __int16 *)(v_rbx + 88)) == 0) goto loc_00873E20;
loc_00873ADC:
    if (((*(unsigned int *)(v_rbx + 80)) & (0x800ULL)) != 0) goto loc_00873D65;
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_00873F56;
    v_stack_m50 = v_xmm0;
    result = 0;
    v_stack_m40 = v_xmm1;
    v_stack_m30 = 0;
    result = ObfReferenceObject(v_rbx, a2, a3, a4);
    a3 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 80)))) & (2)) != 0) goto loc_00873CB7;
    result = KeInitializeEvent(v_stack_m40, a3 + 1, a3, a4);
    v_r12 = 0;
loc_00873B43:
    result = IopResetEvent(v_rbx, a3 + 1, a3, a4);
    result = IoGetRelatedDeviceObject(v_rbx, a3 + 1, a3, a4);
    a3 = (unsigned __int8)((0) ^ (1));
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, a4);
    if (result == 0) goto loc_00873C9D;
    *(unsigned __int64 *)(result + 192) = v_rbx;
    *(unsigned __int64 *)(result + 152) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(result + 64) = a9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 80)))) & (2)) != 0) goto loc_00873D22;
    *(unsigned int *)(result + 16) = 4;
loc_00873BA6:
    *(unsigned __int64 *)(result + 80) = v_stack_m40;
    *(unsigned __int64 *)(result + 72) = v_stack_m50;
    *(unsigned __int64 *)(result + 88) = 0;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_00873E0E;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 20;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18)));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    *(unsigned __int64 *)(result + 112) = a4;
loc_00873BEE:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_rbx;
    result = IopQueueThreadIrp(result, *(unsigned __int8 *)(result + 76), a3, a4);
    result = IofCallDriver(result, result, a3, a4);
    v_stack_m68 = (unsigned int)(result);
    if (0 != 0) goto loc_00873D2D;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 259) {
        v_stack_m78 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_m40;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        v_rdi = v_stack_m50;
        v_stack_m68 = (unsigned int)(v_rdi);
    }
    if (((unsigned int)(v_rdi)) == 0xC0000010ULL) goto loc_00873ED1;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_00873C80;
    if (((unsigned int)(v_rdi)) == 0x80000005ULL) { v_rdi = (unsigned int)((unsigned int)(0xC0000023ULL)); }
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_m48));
    goto loc_00873C80;
loc_00873C80:
loc_00873C82:
    return (unsigned int)((unsigned int)(v_rdi));
loc_00873C9D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 80)))) & (2)) != 0) goto loc_00874044;
loc_00873CA8:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, a4);
    goto loc_00873C82;
loc_00873CB7:
    v_rdi = (unsigned int)((v_rdi) >> (2));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_stack_m28 + 56) + 128, a2, a3, a4);
    v_stack_p30 = 0;
    if (1 != 0) goto loc_00873F5D;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, result);
    v_rdi = 0;
loc_00873D0C:
    if (v_stack_p30 != 0) goto loc_00873EC4;
    goto loc_00873B43;
loc_00873D22:
    result = 0;
    goto loc_00873BA6;
loc_00873D2D:
    if (0 == 259) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 56) + 152;
        v_stack_m50 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        v_rdi = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56);
        v_stack_m40 = (unsigned int)(v_rdi);
    }
    result = IopReleaseFileObjectLock(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, a4);
    goto loc_00873C56;
loc_00873D65:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))) == 3) goto loc_00873E38;
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)) == 0) goto loc_00873FAA;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))) != 1) goto loc_00873F56;
    result = ExAcquireResourceSharedLite(v_rip + 7443719, 1, a3, a4);
    v_stack_m38 = *(unsigned __int64 *)(a5 + 272);
    if (*(unsigned __int64 *)(a5 + 272) == 0) goto loc_00873DC3;
    if (condition_is_less_or_equal) goto loc_00873FEC;
loc_00873DC3:
    result = ExReleaseResourceLite(v_rip + 7443670, 1, a3, a4);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
loc_00873DE2:
    result = SeQuerySecurityDescriptorInfo(v_rdi, 0, a5, v_stack_m38);
    if (*(unsigned __int64 *)(a5 + 272) == 0) goto loc_00873C80;
    result = ObDereferenceSecurityDescriptor(v_stack_m38, 1, a5, v_stack_m38);
    goto loc_00873C80;
loc_00873E0E:
    *(unsigned __int8 *)(v_stack_m38 - 72) = 21;
    *(unsigned int *)(v_stack_m38 - 64) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    *(unsigned __int64 *)(v_stack_m38 - 56) = 0;
    goto loc_00873BEE;
loc_00873E20:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 272) + 64)) != 0) goto loc_00873ADC;
    goto loc_00873D65;
loc_00873E30:
    goto loc_00873ABE;
loc_00873E38:
    v_rdi = 0;
    if (*(unsigned __int64 *)(a5 + 272) != 0) goto loc_00874069;
loc_00873E43:
    result = ObLogSecurityDescriptor(0, v_stack_m30, 1, v_stack_m38);
    v_stack_m40 = (unsigned int)(result);
    if (sign_flag) goto loc_00873C80;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, 1, v_stack_m38);
    result = ExAcquireResourceExclusiveLite(v_rip + 7443480, 1, 1, v_stack_m38);
    if ((*(unsigned __int64 *)(v_stack_m38 + 272)) != 0) goto loc_0087407B;
loc_00873E9B:
    *(unsigned __int64 *)(v_stack_m38 + 272) = v_stack_m30;
    result = ExReleaseResourceLite(v_rip + 7443442, 1, 1, v_stack_m38);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, 1, v_stack_m38);
    goto loc_00873C80;
loc_00873EC4:
    result = ObfDereferenceObject(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, 1, v_stack_m38);
    goto loc_00873C80;
loc_00873ED1:
    if (((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392)))) != 1) goto loc_00873F4E;
    if (((*(unsigned int *)(result + 52)) & (256)) == 0) goto loc_00873F81;
    result = ExAcquireResourceSharedLite(v_rip + 7443360, (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392))), 1, v_stack_m38);
    v_stack_m38 = *(unsigned __int64 *)(result + 272);
    if (*(unsigned __int64 *)(result + 272) == 0) goto loc_00873F2A;
    if (condition_is_less_or_equal) goto loc_00874038;
loc_00873F2A:
    result = ExReleaseResourceLite(v_rip + 7443311, (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392))), 1, v_stack_m38);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392))), 1, v_stack_m38);
    goto loc_00873DE2;
loc_00873F4E:
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392))) == 0) goto loc_00874051;
loc_00873F56:
    v_rdi = 0;
    goto loc_00873C80;
loc_00873F5D:
    v_stack_m50 = v_stack_p30;
    result = IopWaitAndAcquireFileObjectLock(*(unsigned __int64 *)(result + 272), (unsigned __int8)(result), 0, v_stack_m38);
    goto loc_00873D0C;
loc_00873F81:
    result = SeAssignWorldSecurityDescriptor(0, v_stack_m38, v_stack_p40, v_stack_m38);
    v_stack_m40 = (unsigned int)(result);
    goto loc_00873C80;
loc_00873FAA:
    result = IopGetDevicePDO(v_stack_m38, v_stack_m38, v_stack_p40, v_stack_m38);
    if (result != 0) goto loc_00873FF8;
    v_stack_m50 = a8;
    result = IopSetDeviceSecurityDescriptor(v_stack_m38, (unsigned int)((unsigned int)(result)), 0, (unsigned int)(a7));
    result = AstLogDeviceSDDLUpdated(v_stack_m38, (unsigned int)((unsigned int)(result)), 0, (unsigned int)(a7));
    goto loc_00873C80;
loc_00873FEC:
    goto loc_00873DC3;
loc_00873FF8:
    v_stack_m48 = a8;
    v_stack_m50 = (unsigned int)((unsigned int)(a7));
    result = IopSetDeviceSecurityDescriptors(v_stack_m38, result, (unsigned int)((unsigned int)(result)), 0);
    result = ObfDereferenceObject(result, result, (unsigned int)((unsigned int)(result)), 0);
    result = AstLogDeviceSDDLUpdated(v_stack_m38, result, (unsigned int)((unsigned int)(result)), 0);
    goto loc_00873C80;
loc_00874038:
    goto loc_00873F2A;
loc_00874044:
    result = IopReleaseFileObjectLock(result, result, (unsigned int)((unsigned int)(result)), 0);
    goto loc_00873CA8;
loc_00874051:
    if (((*(unsigned int *)(result + 48)) & (256)) == 0) goto loc_00873F56;
    goto loc_00873C80;
loc_00874069:
    if (((*(unsigned int *)(result + 80)) & (256)) != 0) goto loc_00873C80;
    goto loc_00873E43;
loc_0087407B:
    goto loc_00873E9B;
}
```

## 5. (Beta) C Style

```c
int64_t IopGetSetSecurityObject(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint64_t Arg6, uint32_t Arg7, int64_t Arg8, uint8_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p40;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    v_stack_m58 = 0;
    if (((uint16_t)(*(uint16_t *)(arg1))) == 3) goto loc_00873E30;
loc_00873ABE:
    local_rbx = 0;
    if (((uint16_t)(*(uint16_t *)(arg1))) != 3) { local_rbx = Arg1; }
    if (local_rbx == 0) goto loc_00873D65;
    if ((*(uint16_t *)(local_rbx + 0x58)) == 0) goto loc_00873E20;
loc_00873ADC:
    if (((*(uint32_t *)(local_rbx + 0x50)) & (0x800ULL)) != 0) goto loc_00873D65;
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_00873F56;
    v_stack_m50 = v_xmm0;
    result = 0;
    v_stack_m40 = v_xmm1;
    v_stack_m30 = 0;
    result = ObfReferenceObject(local_rbx, Arg2, Arg3, Arg4);
    Arg3 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x50)))) & (2)) != 0) goto loc_00873CB7;
    result = KeInitializeEvent(v_stack_m40, Arg3 + 1, Arg3, Arg4);
    local_r12 = 0;
loc_00873B43:
    result = IopResetEvent(local_rbx, Arg3 + 1, Arg3, Arg4);
    result = IoGetRelatedDeviceObject(local_rbx, Arg3 + 1, Arg3, Arg4);
    Arg3 = (uint8_t)((0) ^ (1));
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, Arg4);
    if (result == 0) goto loc_00873C9D;
    *(uint64_t *)(result + 0xC0) = local_rbx;
    *(uint64_t *)(result + 0x98) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(result + 0x40) = Arg9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x50)))) & (2)) != 0) goto loc_00873D22;
    *(uint32_t *)(result + 0x10) = 4;
loc_00873BA6:
    *(uint64_t *)(result + 0x50) = v_stack_m40;
    *(uint64_t *)(result + 0x48) = v_stack_m50;
    *(uint64_t *)(result + 0x58) = 0;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_00873E0E;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 20;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18)));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    *(uint64_t *)(result + 0x70) = Arg4;
loc_00873BEE:
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = local_rbx;
    result = IopQueueThreadIrp(result, *(uint8_t *)(result + 0x4C), Arg3, Arg4);
    result = IofCallDriver(result, result, Arg3, Arg4);
    v_stack_m68 = (uint32_t)(result);
    if (0 != 0) goto loc_00873D2D;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 259) {
        v_stack_m78 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_m40;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m50;
        v_stack_m68 = (uint32_t)(local_rdi);
    }
    if (((uint32_t)(local_rdi)) == 0xC0000010ULL) goto loc_00873ED1;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_00873C80;
    if (((uint32_t)(local_rdi)) == 0x80000005ULL) { local_rdi = (uint32_t)((uint32_t)(0xC0000023ULL)); }
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(v_stack_m48));
    goto loc_00873C80;
loc_00873C80:
loc_00873C82:
    return (uint32_t)((uint32_t)(local_rdi));
loc_00873C9D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x50)))) & (2)) != 0) goto loc_00874044;
loc_00873CA8:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, Arg3, Arg4);
    goto loc_00873C82;
loc_00873CB7:
    local_rdi = (uint32_t)((local_rdi) >> (2));
    local_rdi = (uint8_t)((local_rdi) & (1));
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_stack_m28 + 0x38) + 128, Arg2, Arg3, Arg4);
    v_stack_p30 = 0;
    if (1 != 0) goto loc_00873F5D;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, Arg3, result);
    local_rdi = 0;
loc_00873D0C:
    if (v_stack_p30 != 0) goto loc_00873EC4;
    goto loc_00873B43;
loc_00873D22:
    result = 0;
    goto loc_00873BA6;
loc_00873D2D:
    if (0 == 259) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x38) + 152;
        v_stack_m50 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
        local_rdi = *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38);
        v_stack_m40 = (uint32_t)(local_rdi);
    }
    result = IopReleaseFileObjectLock(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, Arg3, Arg4);
    goto loc_00873C56;
loc_00873D65:
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))) == 3) goto loc_00873E38;
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)) == 0) goto loc_00873FAA;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))) != 1) goto loc_00873F56;
    result = ExAcquireResourceSharedLite(v_rip + 7443719, 1, Arg3, Arg4);
    v_stack_m38 = *(uint64_t *)(arg5 + 0x110);
    if (*(uint64_t *)(arg5 + 0x110) == 0) goto loc_00873DC3;
    if (condition_is_less_or_equal) goto loc_00873FEC;
loc_00873DC3:
    result = ExReleaseResourceLite(v_rip + 7443670, 1, Arg3, Arg4);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
loc_00873DE2:
    result = SeQuerySecurityDescriptorInfo(local_rdi, 0, Arg5, v_stack_m38);
    if (*(uint64_t *)(arg5 + 0x110) == 0) goto loc_00873C80;
    result = ObDereferenceSecurityDescriptor(v_stack_m38, 1, Arg5, v_stack_m38);
    goto loc_00873C80;
loc_00873E0E:
    *(uint8_t *)(v_stack_m38 - 0x48) = 21;
    *(uint32_t *)(v_stack_m38 - 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    *(uint64_t *)(v_stack_m38 - 0x38) = 0;
    goto loc_00873BEE;
loc_00873E20:
    if ((*(uint64_t *)(*(uint64_t *)(arg5 + 0x110) + 0x40)) != 0) goto loc_00873ADC;
    goto loc_00873D65;
loc_00873E30:
    goto loc_00873ABE;
loc_00873E38:
    local_rdi = 0;
    if (*(uint64_t *)(arg5 + 0x110) != 0) goto loc_00874069;
loc_00873E43:
    result = ObLogSecurityDescriptor(0, v_stack_m30, 1, v_stack_m38);
    v_stack_m40 = (uint32_t)(result);
    if (sign_flag) goto loc_00873C80;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, 1, v_stack_m38);
    result = ExAcquireResourceExclusiveLite(v_rip + 7443480, 1, 1, v_stack_m38);
    if ((*(uint64_t *)(v_stack_m38 + 0x110)) != 0) goto loc_0087407B;
loc_00873E9B:
    *(uint64_t *)(v_stack_m38 + 0x110) = v_stack_m30;
    result = ExReleaseResourceLite(v_rip + 7443442, 1, 1, v_stack_m38);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), 1, 1, v_stack_m38);
    goto loc_00873C80;
loc_00873EC4:
    result = ObfDereferenceObject(*(uint64_t *)(gs_base + (0 + 0x188)), 1, 1, v_stack_m38);
    goto loc_00873C80;
loc_00873ED1:
    if (((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188)))) != 1) goto loc_00873F4E;
    if (((*(uint32_t *)(result + 0x34)) & (256)) == 0) goto loc_00873F81;
    result = ExAcquireResourceSharedLite(v_rip + 7443360, (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188))), 1, v_stack_m38);
    v_stack_m38 = *(uint64_t *)(result + 0x110);
    if (*(uint64_t *)(result + 0x110) == 0) goto loc_00873F2A;
    if (condition_is_less_or_equal) goto loc_00874038;
loc_00873F2A:
    result = ExReleaseResourceLite(v_rip + 7443311, (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188))), 1, v_stack_m38);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188))), 1, v_stack_m38);
    goto loc_00873DE2;
loc_00873F4E:
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188))) == 0) goto loc_00874051;
loc_00873F56:
    local_rdi = 0;
    goto loc_00873C80;
loc_00873F5D:
    v_stack_m50 = v_stack_p30;
    result = IopWaitAndAcquireFileObjectLock(*(uint64_t *)(result + 0x110), (uint8_t)(result), 0, v_stack_m38);
    goto loc_00873D0C;
loc_00873F81:
    result = SeAssignWorldSecurityDescriptor(0, v_stack_m38, v_stack_p40, v_stack_m38);
    v_stack_m40 = (uint32_t)(result);
    goto loc_00873C80;
loc_00873FAA:
    result = IopGetDevicePDO(v_stack_m38, v_stack_m38, v_stack_p40, v_stack_m38);
    if (result != 0) goto loc_00873FF8;
    v_stack_m50 = Arg8;
    result = IopSetDeviceSecurityDescriptor(v_stack_m38, (uint32_t)((uint32_t)(result)), 0, (uint32_t)(Arg7));
    result = AstLogDeviceSDDLUpdated(v_stack_m38, (uint32_t)((uint32_t)(result)), 0, (uint32_t)(Arg7));
    goto loc_00873C80;
loc_00873FEC:
    goto loc_00873DC3;
loc_00873FF8:
    v_stack_m48 = Arg8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg7));
    result = IopSetDeviceSecurityDescriptors(v_stack_m38, result, (uint32_t)((uint32_t)(result)), 0);
    result = ObfDereferenceObject(result, result, (uint32_t)((uint32_t)(result)), 0);
    result = AstLogDeviceSDDLUpdated(v_stack_m38, result, (uint32_t)((uint32_t)(result)), 0);
    goto loc_00873C80;
loc_00874038:
    goto loc_00873F2A;
loc_00874044:
    result = IopReleaseFileObjectLock(result, result, (uint32_t)((uint32_t)(result)), 0);
    goto loc_00873CA8;
loc_00874051:
    if (((*(uint32_t *)(result + 0x30)) & (256)) == 0) goto loc_00873F56;
    goto loc_00873C80;
loc_00874069:
    if (((*(uint32_t *)(result + 0x50)) & (256)) != 0) goto loc_00873C80;
    goto loc_00873E43;
loc_0087407B:
    goto loc_00873E9B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00873A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
