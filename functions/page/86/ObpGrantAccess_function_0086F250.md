# ObpGrantAccess

- RVA: `0x0086F250`–`0x0086F9F2` (길이 `1,954` bytes)
- VA: `0x000000014086F250`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C1A4`
- 디코드: `487`개 명령, `1,954/1,954` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x0086F35C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086F383` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086F3C6` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0086F425` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0086F437` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0086F48C` → [SeOpenObjectAuditAlarmWithTransaction](SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)
- `0x0086F499` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086F4A7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086F4B9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086F4C7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086F514` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0086F60B` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (function, `0x003A6080`)
- `0x0086F666` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086F6CD` → [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) (function, `0x00870CC0`)
- `0x0086F711` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086F739` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0086F760` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086F78C` → [IopGetSetSecurityObject](../87/IopGetSetSecurityObject_function_00873A80.md) (function, `0x00873A80`)
- `0x0086F7DF` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (function, `0x0040B6B0`)
- `0x0086F7F9` → [SePrivilegedServiceAuditAlarm](../87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) (function, `0x00871CB0`)
- `0x0086F81E` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x0086F82F` → [ObpReferenceSecurityDescriptorSlow](../87/ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x0086F847` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x0086F858` → [ObpReferenceSecurityDescriptorSlow](../87/ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x0086F889` → [SeAppendPrivileges](../9D/SeAppendPrivileges_function_009D7980.md) (function, `0x009D7980`)
- `0x0086F89B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086F8B6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086F909` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086F95B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086F98F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0086F99C` → [SepConcatenatePrivileges](../9D/SepConcatenatePrivileges_function_009D7AD0.md) (function, `0x009D7AD0`)
- `0x0086F9AC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086F9D8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5AC3`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F676`

### Static image references
- `0x0086F26C` → RVA `0x00E0A740` (`.data`; read)
- `0x0086F2C0` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0086F2CE` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x0086F2E1` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x0086F649` → RVA `0x00E0B38C` (`.data`; read)
- `0x0086F68F` → RVA `0x00870CC0` (`CmpSecurityMethod`; read)
- `0x0086F76D` → RVA `0x00873A80` (`IopGetSetSecurityObject`; read)
- `0x0086F796` → RVA `0x00FD9B00` (`PAGEDATA`; read)
- `0x0086F8AA` → RVA `0x00E0B38C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x0086F35C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086F383` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086F3C6` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0086F425` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0086F437` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0086F499` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086F4A7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086F4B9` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086F4C7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086F514` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0086F60B` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (`PAGE` → `.text`)
  - `0x0086F666` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086F711` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086F739` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0086F760` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086F7DF` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (`PAGE` → `.text`)
  - `0x0086F89B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086F8B6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086F909` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086F95B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086F98F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0086F9AC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086F9D8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086F250  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0086F255  55                              push rbp
0086F256  56                              push rsi
0086F257  57                              push rdi
0086F258  41 54                           push r12
0086F25A  41 55                           push r13
0086F25C  41 56                           push r14
0086F25E  41 57                           push r15
0086F260  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
0086F265  48 81 EC B0 00 00 00            sub rsp, 0xb0
0086F26C  48 8B 05 CD B4 59 00            mov rax, qword ptr [rip + 0x59b4cd]
0086F273  48 33 C4                        xor rax, rsp
0086F276  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0086F27A  4C 8B 65 7F                     mov r12, qword ptr [rbp + 0x7f]
0086F27E  49 8B D8                        mov rbx, r8
0086F281  45 33 C0                        xor r8d, r8d
0086F284  41 0F B6 C1                     movzx eax, r9b
0086F288  F7 45 77 00 04 00 00            test dword ptr [rbp + 0x77], 0x400
0086F28F  BE 01 00 00 00                  mov esi, 1
0086F294  4C 8B F2                        mov r14, rdx
0086F297  44 89 45 D3                     mov dword ptr [rbp - 0x2d], r8d
0086F29B  0F 44 F0                        cmove esi, eax
0086F29E  8D 41 FF                        lea eax, [rcx - 1]
0086F2A1  83 F8 01                        cmp eax, 1
0086F2A4  48 8D 42 D0                     lea rax, [rdx - 0x30]
0086F2A8  0F 87 87 02 00 00               ja 0x14086f535
0086F2AE  48 C1 E8 08                     shr rax, 8
0086F2B2  0F B6 C8                        movzx ecx, al
0086F2B5  0F B6 42 E8                     movzx eax, byte ptr [rdx - 0x18]
0086F2B9  48 33 C8                        xor rcx, rax
0086F2BC  44 89 45 CF                     mov dword ptr [rbp - 0x31], r8d
0086F2C0  0F B6 05 85 7B 75 00            movzx eax, byte ptr [rip + 0x757b85]
0086F2C7  48 33 C8                        xor rcx, rax
0086F2CA  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
0086F2CE  48 8D 05 2B 85 75 00            lea rax, [rip + 0x75852b]
0086F2D5  44 89 45 BB                     mov dword ptr [rbp - 0x45], r8d
0086F2D9  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
0086F2DD  4C 8B 2C C8                     mov r13, qword ptr [rax + rcx*8]
0086F2E1  48 8D 05 C8 AF 04 00            lea rax, [rip + 0x4afc8]
0086F2E8  4C 89 6D EF                     mov qword ptr [rbp - 0x11], r13
0086F2EC  49 39 85 98 00 00 00            cmp qword ptr [r13 + 0x98], rax
0086F2F3  0F 85 50 03 00 00               jne 0x14086f649
0086F2F9  0F 0D 4A F8                     prefetchw byte ptr [rdx - 8]
0086F2FD  48 8B 52 F8                     mov rdx, qword ptr [rdx - 8]
0086F301  F6 C2 0F                        test dl, 0xf
0086F304  74 16                           je 0x14086f31c
0086F306  48 8D 4A FF                     lea rcx, [rdx - 1]
0086F30A  48 8B C2                        mov rax, rdx
0086F30D  F0 49 0F B1 4E F8               lock cmpxchg qword ptr [r14 - 8], rcx
0086F313  74 07                           je 0x14086f31c
0086F315  48 8B D0                        mov rdx, rax
0086F318  A8 0F                           test al, 0xf
0086F31A  75 EA                           jne 0x14086f306
0086F31C  48 8B FA                        mov rdi, rdx
0086F31F  83 E2 0F                        and edx, 0xf
0086F322  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
0086F326  83 FA 01                        cmp edx, 1
0086F329  77 09                           ja 0x14086f334
0086F32B  48 85 FF                        test rdi, rdi
0086F32E  0F 85 F4 04 00 00               jne 0x14086f828
0086F334  C6 45 B7 00                     mov byte ptr [rbp - 0x49], 0
0086F338  48 85 FF                        test rdi, rdi
0086F33B  0F 84 DA 03 00 00               je 0x14086f71b
0086F341  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086F34A  B2 01                           mov dl, 1
0086F34C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086F353  90                              nop
0086F354  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086F358  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086F35C  E8 5F 28 9A FF                  call 0x140211bc0
0086F361  48 83 7B 20 00                  cmp qword ptr [rbx + 0x20], 0
0086F366  74 20                           je 0x14086f388
0086F368  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086F371  B2 01                           mov dl, 1
0086F373  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086F37A  90                              nop
0086F37B  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0086F37F  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086F383  E8 38 28 9A FF                  call 0x140211bc0
0086F388  44 8B 4B 10                     mov r9d, dword ptr [rbx + 0x10]
0086F38C  48 8D 4D D3                     lea rcx, [rbp - 0x2d]
0086F390  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0086F395  49 8D 45 4C                     lea rax, [r13 + 0x4c]
0086F399  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0086F39D  41 B0 01                        mov r8b, 1
0086F3A0  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0086F3A5  48 8D 53 20                     lea rdx, [rbx + 0x20]
0086F3A9  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
0086F3AE  48 8B CF                        mov rcx, rdi
0086F3B1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086F3B6  48 8D 45 DF                     lea rax, [rbp - 0x21]
0086F3BA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086F3BF  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0086F3C2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0086F3C6  E8 F5 77 B3 FF                  call 0x1403a6bc0
0086F3CB  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
0086F3CF  44 0F B6 E8                     movzx r13d, al
0086F3D3  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
0086F3D7  48 85 D2                        test rdx, rdx
0086F3DA  74 60                           je 0x14086f43c
0086F3DC  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0086F3E0  44 8B 02                        mov r8d, dword ptr [rdx]
0086F3E3  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0086F3E7  4C 8B 38                        mov r15, qword ptr [rax]
0086F3EA  45 8B 0F                        mov r9d, dword ptr [r15]
0086F3ED  43 8D 0C 08                     lea ecx, [r8 + r9]
0086F3F1  83 F9 03                        cmp ecx, 3
0086F3F4  0F 87 1C 05 00 00               ja 0x14086f916
0086F3FA  4D 85 FF                        test r15, r15
0086F3FD  0F 84 FD 02 00 00               je 0x14086f700
0086F403  45 85 C9                        test r9d, r9d
0086F406  0F 85 3C 03 00 00               jne 0x14086f748
0086F40C  C7 45 C7 08 00 00 00            mov dword ptr [rbp - 0x39], 8
0086F413  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
0086F416  47 8D 04 40                     lea r8d, [r8 + r8*2]
0086F41A  41 C1 E0 02                     shl r8d, 2
0086F41E  49 03 CF                        add rcx, r15
0086F421  48 83 C2 08                     add rdx, 8
0086F425  E8 16 74 E5 FF                  call 0x1406c6840
0086F42A  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0086F42E  8B 01                           mov eax, dword ptr [rcx]
0086F430  41 01 07                        add dword ptr [r15], eax
0086F433  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
0086F437  E8 44 69 C0 FF                  call 0x140475d80
0086F43C  45 84 ED                        test r13b, r13b
0086F43F  74 0F                           je 0x14086f450
0086F441  8B 4D CF                        mov ecx, dword ptr [rbp - 0x31]
0086F444  09 4B 14                        or dword ptr [rbx + 0x14], ecx
0086F447  0F BA E9 19                     bts ecx, 0x19
0086F44B  F7 D1                           not ecx
0086F44D  21 4B 10                        and dword ptr [rbx + 0x10], ecx
0086F450  40 84 F6                        test sil, sil
0086F453  74 3C                           je 0x14086f491
0086F455  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
0086F459  48 8D 43 0A                     lea rax, [rbx + 0xa]
0086F45D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0086F462  48 83 C1 10                     add rcx, 0x10
0086F466  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
0086F46F  4C 8B CF                        mov r9, rdi
0086F472  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
0086F477  45 33 C0                        xor r8d, r8d
0086F47A  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
0086F47F  49 8B D6                        mov rdx, r14
0086F482  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0086F487  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0086F48C  E8 FF F2 FF FF                  call 0x14086e790
0086F491  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086F495  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086F499  E8 72 05 9F FF                  call 0x14025fa10
0086F49E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086F4A7  E8 44 FB 9E FF                  call 0x14025eff0
0086F4AC  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0086F4B0  48 85 C9                        test rcx, rcx
0086F4B3  74 17                           je 0x14086f4cc
0086F4B5  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086F4B9  E8 52 05 9F FF                  call 0x14025fa10
0086F4BE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086F4C7  E8 24 FB 9E FF                  call 0x14025eff0
0086F4CC  80 7D B7 00                     cmp byte ptr [rbp - 0x49], 0
0086F4D0  0F 85 36 02 00 00               jne 0x14086f70c
0086F4D6  41 0F 0D 4E F8                  prefetchw byte ptr [r14 - 8]
0086F4DB  49 8B 46 F8                     mov rax, qword ptr [r14 - 8]
0086F4DF  48 8B C8                        mov rcx, rax
0086F4E2  48 33 CF                        xor rcx, rdi
0086F4E5  48 83 F9 0F                     cmp rcx, 0xf
0086F4E9  0F 83 27 03 00 00               jae 0x14086f816
0086F4EF  48 8D 48 01                     lea rcx, [rax + 1]
0086F4F3  F0 49 0F B1 4E F8               lock cmpxchg qword ptr [r14 - 8], rcx
0086F4F9  75 E4                           jne 0x14086f4df
0086F4FB  45 84 ED                        test r13b, r13b
0086F4FE  0F 84 E5 04 00 00               je 0x14086f9e9
0086F504  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0086F507  41 89 04 24                     mov dword ptr [r12], eax
0086F50B  33 C0                           xor eax, eax
0086F50D  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
0086F511  48 33 CC                        xor rcx, rsp
0086F514  E8 27 D1 E3 FF                  call 0x1406ac640
0086F519  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
0086F521  48 81 C4 B0 00 00 00            add rsp, 0xb0
0086F528  41 5F                           pop r15
0086F52A  41 5E                           pop r14
0086F52C  41 5D                           pop r13
0086F52E  41 5C                           pop r12
0086F530  5F                              pop rdi
0086F531  5E                              pop rsi
0086F532  5D                              pop rbp
0086F533  C3                              ret
0086F534  CC                              int3
0086F535  48 C1 E8 08                     shr rax, 8
0086F539  0F B6 D0                        movzx edx, al
0086F53C  41 0F B6 46 E8                  movzx eax, byte ptr [r14 - 0x18]
0086F541  48 33 D0                        xor rdx, rax
0086F544  0F B6 05 01 79 75 00            movzx eax, byte ptr [rip + 0x757901]
0086F54B  48 33 D0                        xor rdx, rax
0086F54E  48 8D 05 AB 82 75 00            lea rax, [rip + 0x7582ab]
0086F555  48 8B 3C D0                     mov rdi, qword ptr [rax + rdx*8]
0086F559  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0086F55C  0F BA E0 19                     bt eax, 0x19
0086F560  73 0B                           jae 0x14086f56d
0086F562  0F BA F0 19                     btr eax, 0x19
0086F566  0F BA E8 1C                     bts eax, 0x1c
0086F56A  89 43 10                        mov dword ptr [rbx + 0x10], eax
0086F56D  A9 00 00 00 F0                  test eax, 0xf0000000
0086F572  74 2A                           je 0x14086f59e
0086F574  85 C0                           test eax, eax
0086F576  79 03                           jns 0x14086f57b
0086F578  0B 47 4C                        or eax, dword ptr [rdi + 0x4c]
0086F57B  0F BA E0 1E                     bt eax, 0x1e
0086F57F  73 03                           jae 0x14086f584
0086F581  0B 47 50                        or eax, dword ptr [rdi + 0x50]
0086F584  0F BA E0 1D                     bt eax, 0x1d
0086F588  73 03                           jae 0x14086f58d
0086F58A  0B 47 54                        or eax, dword ptr [rdi + 0x54]
0086F58D  0F BA E0 1C                     bt eax, 0x1c
0086F591  73 03                           jae 0x14086f596
0086F593  0B 47 58                        or eax, dword ptr [rdi + 0x58]
0086F596  25 FF FF FF 0F                  and eax, 0xfffffff
0086F59B  89 43 10                        mov dword ptr [rbx + 0x10], eax
0086F59E  0F BA E0 18                     bt eax, 0x18
0086F5A2  0F 82 EE 01 00 00               jb 0x14086f796
0086F5A8  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0086F5AB  0B 4B 14                        or ecx, dword ptr [rbx + 0x14]
0086F5AE  89 4B 14                        mov dword ptr [rbx + 0x14], ecx
0086F5B1  44 89 43 10                     mov dword ptr [rbx + 0x10], r8d
0086F5B5  8B 47 5C                        mov eax, dword ptr [rdi + 0x5c]
0086F5B8  0F BA E8 18                     bts eax, 0x18
0086F5BC  23 C1                           and eax, ecx
0086F5BE  89 43 14                        mov dword ptr [rbx + 0x14], eax
0086F5C1  41 0F 0D 4E F8                  prefetchw byte ptr [r14 - 8]
0086F5C6  49 8B 56 F8                     mov rdx, qword ptr [r14 - 8]
0086F5CA  F6 C2 0F                        test dl, 0xf
0086F5CD  74 16                           je 0x14086f5e5
0086F5CF  48 8D 4A FF                     lea rcx, [rdx - 1]
0086F5D3  48 8B C2                        mov rax, rdx
0086F5D6  F0 49 0F B1 4E F8               lock cmpxchg qword ptr [r14 - 8], rcx
0086F5DC  74 07                           je 0x14086f5e5
0086F5DE  48 8B D0                        mov rdx, rax
0086F5E1  A8 0F                           test al, 0xf
0086F5E3  75 EA                           jne 0x14086f5cf
0086F5E5  48 8B F2                        mov rsi, rdx
0086F5E8  83 E2 0F                        and edx, 0xf
0086F5EB  48 83 E6 F0                     and rsi, 0xfffffffffffffff0
0086F5EF  83 FA 01                        cmp edx, 1
0086F5F2  77 09                           ja 0x14086f5fd
0086F5F4  48 85 F6                        test rsi, rsi
0086F5F7  0F 85 54 02 00 00               jne 0x14086f851
0086F5FD  44 8B 43 14                     mov r8d, dword ptr [rbx + 0x14]
0086F601  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0086F605  4C 8B CE                        mov r9, rsi
0086F608  48 8B D3                        mov rdx, rbx
0086F60B  E8 70 6A B3 FF                  call 0x1403a6080
0086F610  F7 D0                           not eax
0086F612  21 43 14                        and dword ptr [rbx + 0x14], eax
0086F615  48 85 F6                        test rsi, rsi
0086F618  0F 84 E6 FE FF FF               je 0x14086f504
0086F61E  41 0F 0D 4E F8                  prefetchw byte ptr [r14 - 8]
0086F623  49 8B 46 F8                     mov rax, qword ptr [r14 - 8]
0086F627  48 8B C8                        mov rcx, rax
0086F62A  48 33 CE                        xor rcx, rsi
0086F62D  48 83 F9 0F                     cmp rcx, 0xf
0086F631  0F 83 08 02 00 00               jae 0x14086f83f
0086F637  48 8D 48 01                     lea rcx, [rax + 1]
0086F63B  F0 49 0F B1 4E F8               lock cmpxchg qword ptr [r14 - 8], rcx
0086F641  0F 84 BD FE FF FF               je 0x14086f504
0086F647  EB DE                           jmp 0x14086f627
0086F649  8B 05 3D BD 59 00               mov eax, dword ptr [rip + 0x59bd3d]
0086F64F  B9 00 01 00 00                  mov ecx, 0x100
0086F654  8B D0                           mov edx, eax
0086F656  C7 45 BF BF 01 00 00            mov dword ptr [rbp - 0x41], 0x1bf
0086F65D  41 B8 4F 62 53 71               mov r8d, 0x7153624f
0086F663  89 45 BB                        mov dword ptr [rbp - 0x45], eax
0086F666  E8 85 2A 31 00                  call 0x140b820f0
0086F66B  48 8B F8                        mov rdi, rax
0086F66E  48 85 C0                        test rax, rax
0086F671  0F 84 91 01 00 00               je 0x14086f808
0086F677  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
0086F67B  4D 8D 46 F8                     lea r8, [r14 - 8]
0086F67F  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
0086F686  49 8D 55 4C                     lea rdx, [r13 + 0x4c]
0086F68A  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
0086F68F  4C 8D 0D 2A 16 00 00            lea r9, [rip + 0x162a]
0086F696  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0086F69B  BA 01 00 00 00                  mov edx, 1
0086F6A0  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0086F6A4  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0086F6A9  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
0086F6AD  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0086F6B1  C6 45 B7 01                     mov byte ptr [rbp - 0x49], 1
0086F6B5  49 3B C1                        cmp rax, r9
0086F6B8  0F 85 AF 00 00 00               jne 0x14086f76d
0086F6BE  48 8D 45 BB                     lea rax, [rbp - 0x45]
0086F6C2  4C 8B CF                        mov r9, rdi
0086F6C5  49 8B CE                        mov rcx, r14
0086F6C8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086F6CD  E8 EE 15 00 00                  call 0x140870cc0
0086F6D2  44 8B F8                        mov r15d, eax
0086F6D5  3D 23 00 00 C0                  cmp eax, 0xc0000023
0086F6DA  0F 84 B6 01 00 00               je 0x14086f896
0086F6E0  45 85 FF                        test r15d, r15d
0086F6E3  78 76                           js 0x14086f75b
0086F6E5  48 85 FF                        test rdi, rdi
0086F6E8  0F 85 53 FC FF FF               jne 0x14086f341
0086F6EE  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0086F6F1  09 43 14                        or dword ptr [rbx + 0x14], eax
0086F6F4  C7 43 10 00 00 00 00            mov dword ptr [rbx + 0x10], 0
0086F6FB  E9 04 FE FF FF                  jmp 0x14086f504
0086F700  C7 45 C7 00 00 00 00            mov dword ptr [rbp - 0x39], 0
0086F707  E9 07 FD FF FF                  jmp 0x14086f413
0086F70C  33 D2                           xor edx, edx
0086F70E  48 8B CF                        mov rcx, rdi
0086F711  E8 5A 31 31 00                  call 0x140b82870
0086F716  E9 E0 FD FF FF                  jmp 0x14086f4fb
0086F71B  41 F6 45 42 08                  test byte ptr [r13 + 0x42], 8
0086F720  74 1D                           je 0x14086f73f
0086F722  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0086F727  49 8D 56 D0                     lea rdx, [r14 - 0x30]
0086F72B  4D 8B C5                        mov r8, r13
0086F72E  41 B9 01 00 00 00               mov r9d, 1
0086F734  B9 89 01 00 00                  mov ecx, 0x189
0086F739  E8 22 DF C8 FF                  call 0x1404fd660
0086F73E  CC                              int3
0086F73F  41 F6 46 EA 02                  test byte ptr [r14 - 0x16], 2
0086F744  74 A8                           je 0x14086f6ee
0086F746  EB DA                           jmp 0x14086f722
0086F748  43 8D 04 49                     lea eax, [r9 + r9*2]
0086F74C  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086F753  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0086F756  E9 B8 FC FF FF                  jmp 0x14086f413
0086F75B  33 D2                           xor edx, edx
0086F75D  48 8B CF                        mov rcx, rdi
0086F760  E8 0B 31 31 00                  call 0x140b82870
0086F765  41 8B C7                        mov eax, r15d
0086F768  E9 A0 FD FF FF                  jmp 0x14086f50d
0086F76D  4C 8D 0D 0C 43 00 00            lea r9, [rip + 0x430c]
0086F774  49 3B C1                        cmp rax, r9
0086F777  4C 8B CF                        mov r9, rdi
0086F77A  0F 85 4C 02 00 00               jne 0x14086f9cc
0086F780  48 8D 45 BB                     lea rax, [rbp - 0x45]
0086F784  49 8B CE                        mov rcx, r14
0086F787  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086F78C  E8 EF 42 00 00                  call 0x140873a80
0086F791  E9 3C FF FF FF                  jmp 0x14086f6d2
0086F796  48 8B 05 63 A3 76 00            mov rax, qword ptr [rip + 0x76a363]
0086F79D  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0086F7A1  C7 45 F7 01 00 00 00            mov dword ptr [rbp - 9], 1
0086F7A8  C7 45 FB 01 00 00 00            mov dword ptr [rbp - 5], 1
0086F7AF  44 89 45 07                     mov dword ptr [rbp + 7], r8d
0086F7B3  40 84 F6                        test sil, sil
0086F7B6  0F 84 B8 00 00 00               je 0x14086f874
0086F7BC  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0086F7C0  48 85 C9                        test rcx, rcx
0086F7C3  0F 85 9C 00 00 00               jne 0x14086f865
0086F7C9  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086F7CD  41 B9 01 00 00 00               mov r9d, 1
0086F7D3  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
0086F7D8  45 8B C1                        mov r8d, r9d
0086F7DB  48 8D 55 FF                     lea rdx, [rbp - 1]
0086F7DF  E8 CC BE B9 FF                  call 0x14040b6b0
0086F7E4  84 C0                           test al, al
0086F7E6  0F 85 88 00 00 00               jne 0x14086f874
0086F7EC  45 33 C9                        xor r9d, r9d
0086F7EF  4C 8D 45 F7                     lea r8, [rbp - 9]
0086F7F3  48 8D 53 20                     lea rdx, [rbx + 0x20]
0086F7F7  33 C9                           xor ecx, ecx
0086F7F9  E8 B2 24 00 00                  call 0x140871cb0
0086F7FE  B8 61 00 00 C0                  mov eax, 0xc0000061
0086F803  E9 05 FD FF FF                  jmp 0x14086f50d
0086F808  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0086F80E  41 8B C7                        mov eax, r15d
0086F811  E9 F7 FC FF FF                  jmp 0x14086f50d
0086F816  BA 01 00 00 00                  mov edx, 1
0086F81B  48 8B CF                        mov rcx, rdi
0086F81E  E8 7D 48 00 00                  call 0x1408740a0
0086F823  E9 D3 FC FF FF                  jmp 0x14086f4fb
0086F828  4C 8B C7                        mov r8, rdi
0086F82B  49 8D 4E D0                     lea rcx, [r14 - 0x30]
0086F82F  E8 18 50 00 00                  call 0x14087484c
0086F834  48 8B F8                        mov rdi, rax
0086F837  45 33 C0                        xor r8d, r8d
0086F83A  E9 F5 FA FF FF                  jmp 0x14086f334
0086F83F  BA 01 00 00 00                  mov edx, 1
0086F844  48 8B CE                        mov rcx, rsi
0086F847  E8 54 48 00 00                  call 0x1408740a0
0086F84C  E9 B3 FC FF FF                  jmp 0x14086f504
0086F851  4C 8B C6                        mov r8, rsi
0086F854  49 8D 4E D0                     lea rcx, [r14 - 0x30]
0086F858  E8 EF 4F 00 00                  call 0x14087484c
0086F85D  48 8B F0                        mov rsi, rax
0086F860  E9 98 FD FF FF                  jmp 0x14086f5fd
0086F865  83 7B 28 02                     cmp dword ptr [rbx + 0x28], 2
0086F869  0F 8D 5E FF FF FF               jge 0x14086f7cd
0086F86F  E9 78 FF FF FF                  jmp 0x14086f7ec
0086F874  81 63 10 FF FF FF FE            and dword ptr [rbx + 0x10], 0xfeffffff
0086F87B  48 8D 55 F7                     lea rdx, [rbp - 9]
0086F87F  81 4B 14 00 00 00 01            or dword ptr [rbx + 0x14], 0x1000000
0086F886  48 8B CB                        mov rcx, rbx
0086F889  E8 F2 80 16 00                  call 0x1409d7980
0086F88E  45 33 C0                        xor r8d, r8d
0086F891  E9 12 FD FF FF                  jmp 0x14086f5a8
0086F896  33 D2                           xor edx, edx
0086F898  48 8B CF                        mov rcx, rdi
0086F89B  E8 D0 2F 31 00                  call 0x140b82870
0086F8A0  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
0086F8A3  B9 00 01 00 00                  mov ecx, 0x100
0086F8A8  8B D0                           mov edx, eax
0086F8AA  89 05 DC BA 59 00               mov dword ptr [rip + 0x59badc], eax
0086F8B0  41 B8 4F 62 53 71               mov r8d, 0x7153624f
0086F8B6  E8 35 28 31 00                  call 0x140b820f0
0086F8BB  48 8B F8                        mov rdi, rax
0086F8BE  48 85 C0                        test rax, rax
0086F8C1  0F 84 41 FF FF FF               je 0x14086f808
0086F8C7  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
0086F8CE  49 8D 4D 4C                     lea rcx, [r13 + 0x4c]
0086F8D2  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
0086F8D7  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0086F8DB  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0086F8E0  4C 8B CF                        mov r9, rdi
0086F8E3  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
0086F8E7  BA 01 00 00 00                  mov edx, 1
0086F8EC  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0086F8F0  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0086F8F4  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0086F8F9  48 8D 4D BB                     lea rcx, [rbp - 0x45]
0086F8FD  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086F902  49 8B CE                        mov rcx, r14
0086F905  C6 45 B7 01                     mov byte ptr [rbp - 0x49], 1
0086F909  E8 C2 B1 E4 FF                  call 0x1406baad0
0086F90E  44 8B F8                        mov r15d, eax
0086F911  E9 CA FD FF FF                  jmp 0x14086f6e0
0086F916  B8 08 00 00 00                  mov eax, 8
0086F91B  45 85 C0                        test r8d, r8d
0086F91E  0F 84 9D 00 00 00               je 0x14086f9c1
0086F924  43 8D 04 40                     lea eax, [r8 + r8*2]
0086F928  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
0086F92F  B8 08 00 00 00                  mov eax, 8
0086F934  4D 85 FF                        test r15, r15
0086F937  74 12                           je 0x14086f94b
0086F939  45 85 C9                        test r9d, r9d
0086F93C  74 0F                           je 0x14086f94d
0086F93E  43 8D 04 49                     lea eax, [r9 + r9*2]
0086F942  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086F949  EB 02                           jmp 0x14086f94d
0086F94B  33 C0                           xor eax, eax
0086F94D  8D 14 01                        lea edx, [rcx + rax]
0086F950  41 B8 53 65 50 72               mov r8d, 0x72506553
0086F956  B9 00 01 00 00                  mov ecx, 0x100
0086F95B  E8 90 27 31 00                  call 0x140b820f0
0086F960  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0086F964  48 8B C8                        mov rcx, rax
0086F967  48 85 C0                        test rax, rax
0086F96A  0F 84 C3 FA FF FF               je 0x14086f433
0086F970  4C 8B 7D E7                     mov r15, qword ptr [rbp - 0x19]
0086F974  49 8B 17                        mov rdx, qword ptr [r15]
0086F977  48 85 D2                        test rdx, rdx
0086F97A  74 4C                           je 0x14086f9c8
0086F97C  8B 02                           mov eax, dword ptr [rdx]
0086F97E  85 C0                           test eax, eax
0086F980  74 60                           je 0x14086f9e2
0086F982  8D 04 40                        lea eax, [rax + rax*2]
0086F985  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086F98C  44 8B C0                        mov r8d, eax
0086F98F  E8 AC 6E E5 FF                  call 0x1406c6840
0086F994  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
0086F998  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0086F99C  E8 2F 81 16 00                  call 0x1409d7ad0
0086F9A1  80 7B 0B 00                     cmp byte ptr [rbx + 0xb], 0
0086F9A5  74 0A                           je 0x14086f9b1
0086F9A7  49 8B 0F                        mov rcx, qword ptr [r15]
0086F9AA  33 D2                           xor edx, edx
0086F9AC  E8 BF 2E 31 00                  call 0x140b82870
0086F9B1  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0086F9B5  49 89 07                        mov qword ptr [r15], rax
0086F9B8  C6 43 0B 01                     mov byte ptr [rbx + 0xb], 1
0086F9BC  E9 72 FA FF FF                  jmp 0x14086f433
0086F9C1  8B C8                           mov ecx, eax
0086F9C3  E9 6C FF FF FF                  jmp 0x14086f934
0086F9C8  33 C0                           xor eax, eax
0086F9CA  EB C0                           jmp 0x14086f98c
0086F9CC  48 8D 4D BB                     lea rcx, [rbp - 0x45]
0086F9D0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086F9D5  49 8B CE                        mov rcx, r14
0086F9D8  E8 F3 B0 E4 FF                  call 0x1406baad0
0086F9DD  E9 F0 FC FF FF                  jmp 0x14086f6d2
0086F9E2  B8 08 00 00 00                  mov eax, 8
0086F9E7  EB A3                           jmp 0x14086f98c
0086F9E9  44 8B 7D D3                     mov r15d, dword ptr [rbp - 0x2d]
0086F9ED  E9 73 FD FF FF                  jmp 0x14086f765
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpGrantAccess(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m4F;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 5878989)) ^ (v_rsp);
    v_stack_m40 = result;
    a3 = 0;
    v_stack_m7C = 0;
    v_rsi = 1;
    if (((a5) & (0x400ULL)) == 0) { v_rsi = a4; }
    if (((unsigned int)(a1 - 1)) > 1) goto loc_0086F535;
    result = (a2 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 - 24));
    v_stack_m80 = 0;
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7699333));
    v_stack_m70 = 0;
    v_stack_m94 = 0;
    v_stack_m90 = 0;
    v_stack_m60 = *(unsigned __int64 *)(v_rip + 7701803 + a1 * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7701803 + a1 * 8) + 152)) != (v_rip + 307144)) goto loc_0086F649;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086F31C;
loc_0086F306:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086F31C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) != 0) goto loc_0086F306;
loc_0086F31C:
    a2 = (unsigned int)((*(unsigned __int64 *)(a2 - 8)) & (15));
    v_rdi = (*(unsigned __int64 *)(a2 - 8)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_0086F334;
    if (v_rdi != 0) goto loc_0086F828;
loc_0086F334:
    v_stack_m98 = 0;
    if (v_rdi == 0) goto loc_0086F71B;
loc_0086F341:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 48) + 48), 1, a3, a4);
    if ((*(unsigned __int64 *)(a3 + 32)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(a3 + 32);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, a3, a4);
    }
    v_stack_mA0 = v_stack_m7C;
    v_stack_mA8 = v_stack_m80;
    v_stack_mB0 = (unsigned __int8)(v_rsi);
    v_stack_mB8 = *(unsigned __int64 *)(v_rip + 7701803 + a1 * 8) + 76;
    v_stack_mC0 = v_stack_m70;
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 20)));
    result = SeAccessCheck(v_rdi, a3 + 32, 1, (unsigned int)(*(unsigned int *)(a3 + 16)));
    v_stack_m78 = v_stack_m70;
    if (v_stack_m70 == 0) goto loc_0086F43C;
    v_stack_m68 = *(unsigned __int64 *)(a3 + 72);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72)))) * 1)) > 3) goto loc_0086F916;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72)) == 0) goto loc_0086F700;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72))))) != 0) goto loc_0086F748;
    v_stack_m88 = 8;
loc_0086F413:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70)) + (unsigned int)(*(unsigned int *)(v_stack_m70)) * 2) << (2));
    a1 = ((unsigned int)(v_stack_m88)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72)));
    a2 = (v_stack_m70) + (8);
    result = memcpy(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72)))));
loc_0086F433:
    result = CmSiFreeMemory(v_stack_m70, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 72)))));
loc_0086F43C:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_stack_m80;
        a1 = (unsigned int)(~(a1));
    }
    if ((unsigned __int8)(v_rsi) != 0) {
        a1 = v_stack_m60;
        result = a3 + 10;
        v_stack_mA0 = result;
        a1 = (a1) + (16);
        v_stack_mA8 = 0;
        a4 = v_rdi;
        v_stack_mB0 = (unsigned __int8)(v_rsi);
        a3 = 0;
        v_stack_mB8 = (unsigned __int8)((unsigned __int8)(result));
        a2 = a2;
        v_stack_mC0 = 0;
        v_stack_mC8 = 0;
        result = SeOpenObjectAuditAlarmWithTransaction(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 48) + 48), a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (*(unsigned __int64 *)(a3 + 32) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 32) + 48);
        result = ExReleaseResourceLite(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
    }
    if (v_stack_m98 != 0) goto loc_0086F70C;
loc_0086F4DF:
    a1 = (*(unsigned __int64 *)(a2 - 8)) ^ (v_rdi);
    if (a1 >= 15) goto loc_0086F816;
    if (a1 != 15) goto loc_0086F4DF;
loc_0086F4FB:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0086F9E9;
loc_0086F504:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 20)));
    result = 0;
loc_0086F50D:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
loc_0086F535:
    result = (result) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7698689));
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)));
    }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)))) & (0xF0000000ULL)) == 0) goto loc_0086F59E;
    result = (unsigned int)(*(unsigned int *)(v_stack_p8 + 16));
    if (sign_flag) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7701163 + a2 * 8) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7701163 + a2 * 8) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7701163 + a2 * 8) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7701163 + a2 * 8) + 88)));
    }
    result = (unsigned int)((result) & (0xFFFFFFFULL));
    *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)(result);
loc_0086F59E:
    if (condition_is_below) goto loc_0086F796;
loc_0086F5A8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 16))) | (*(unsigned int *)(v_stack_p8 + 20)));
    *(unsigned int *)(v_stack_p8 + 20) = (unsigned int)(a1);
    *(unsigned int *)(v_stack_p8 + 16) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7701163 + a2 * 8) + 92))) & ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_p8 + 20) = (unsigned int)(result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086F5E5;
loc_0086F5CF:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086F5E5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) != 0) goto loc_0086F5CF;
loc_0086F5E5:
    a2 = (unsigned int)((*(unsigned __int64 *)(a2 - 8)) & (15));
    v_rsi = (*(unsigned __int64 *)(a2 - 8)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_0086F5FD;
    if (v_rsi != 0) goto loc_0086F851;
loc_0086F5FD:
    result = SeComputeCreatorDeniedRights(v_stack_p8 + 32, v_stack_p8, (unsigned int)(*(unsigned int *)(v_stack_p8 + 20)), v_rsi);
    result = (unsigned int)(~(result));
    if (v_rsi == 0) goto loc_0086F504;
loc_0086F627:
    a1 = (*(unsigned __int64 *)(a2 - 8)) ^ (v_rsi);
    if (a1 >= 15) goto loc_0086F83F;
    if (a1 == 15) goto loc_0086F504;
    goto loc_0086F627;
loc_0086F649:
    v_stack_m90 = 447;
    v_stack_m94 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5881149)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5881149)))), (unsigned int)(0x7153624FULL), v_rsi);
    if (result == 0) goto loc_0086F808;
    v_stack_p40 = (unsigned __int8)(v_rsi);
    v_stack_p38 = (unsigned __int8)(result) + 76;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 100)));
    v_stack_p28 = a2 - 8;
    v_stack_m78 = a2 - 8;
    v_stack_m98 = 1;
    if ((*(unsigned __int64 *)((unsigned __int8)(result) + 152)) != (v_rip + 5674)) goto loc_0086F76D;
    v_stack_p20 = v_stack_m94;
    result = CmpSecurityMethod(a2, 1, v_stack_m90, result);
loc_0086F6D2:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_0086F896;
loc_0086F6E0:
    if (sign_flag) goto loc_0086F75B;
    if (result != 0) goto loc_0086F341;
loc_0086F6EE:
    *(unsigned int *)(v_stack_p8 + 16) = 0;
    goto loc_0086F504;
loc_0086F700:
    v_stack_m88 = 0;
    goto loc_0086F413;
loc_0086F70C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m90, result);
    goto loc_0086F4FB;
loc_0086F71B:
    if (((*(unsigned __int8 *)((unsigned __int8)(result) + 66)) & (8)) != 0) {
        v_stack_p20 = v_stack_m90;
        a2 = a2 - 48;
        a3 = (unsigned __int8)(result);
        a4 = 1;
        a1 = 393;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(a2 - 22)) & (2)) == 0) goto loc_0086F6EE;
    goto loc_0086F722;
loc_0086F748:
    v_stack_m88 = (unsigned int)(a4 + a4 * 2 * 4 + 8);
    goto loc_0086F413;
loc_0086F75B:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_0086F765:
    goto loc_0086F50D;
loc_0086F76D:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) != (v_rip + 17164)) goto loc_0086F9CC;
    v_stack_p20 = v_stack_m94;
    result = IopGetSetSecurityObject(0, a2, a3, result);
    goto loc_0086F6D2;
loc_0086F796:
    v_stack_m50 = *(unsigned __int64 *)(v_rip + 7775075);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m48 = (unsigned int)(a3);
    if ((unsigned __int8)(v_rsi) == 0) goto loc_0086F874;
    if (*(unsigned __int64 *)(v_stack_p8 + 32) != 0) goto loc_0086F865;
loc_0086F7CD:
    v_stack_p20 = (unsigned __int8)(v_rsi);
    result = SepPrivilegeCheck(*(unsigned __int64 *)(v_stack_p8 + 48), v_stack_m50, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0086F874;
loc_0086F7EC:
    a4 = 0;
    a1 = 0;
    result = SePrivilegedServiceAuditAlarm(a1, v_stack_p8 + 32, v_stack_m58, a4);
    goto loc_0086F50D;
loc_0086F808:
    goto loc_0086F50D;
loc_0086F816:
    result = ObDereferenceSecurityDescriptor(result, 1, v_stack_m58, a4);
    goto loc_0086F4FB;
loc_0086F828:
    result = ObpReferenceSecurityDescriptorSlow(a2 - 48, 1, result, a4);
    a3 = 0;
    goto loc_0086F334;
loc_0086F83F:
    result = ObDereferenceSecurityDescriptor(v_rsi, 1, a3, a4);
    goto loc_0086F504;
loc_0086F851:
    result = ObpReferenceSecurityDescriptorSlow(a2 - 48, 1, v_rsi, a4);
    goto loc_0086F5FD;
loc_0086F865:
    if ((*(unsigned int *)(v_stack_p8 + 40)) >= 2) goto loc_0086F7CD;
    goto loc_0086F7EC;
loc_0086F874:
    result = SeAppendPrivileges(v_stack_p8, v_stack_m58, v_rsi, a4);
    a3 = 0;
    goto loc_0086F5A8;
loc_0086F896:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(v_rip + 5880540) = (unsigned int)((unsigned int)(v_stack_m94));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_m94))), (unsigned int)(0x7153624FULL), a4);
    if (result == 0) goto loc_0086F808;
    v_stack_p40 = (unsigned __int8)(result);
    v_stack_p38 = (unsigned __int8)(result) + 76;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 100)));
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = v_stack_m94;
    v_stack_m98 = 1;
    result = guard_dispatch_icall(0, 1, v_stack_m90, result);
    goto loc_0086F6E0;
loc_0086F916:
    if ((unsigned int)(v_stack_m90) == 0) goto loc_0086F9C1;
loc_0086F934:
    if ((unsigned int)((unsigned int)(result)) == 0) goto loc_0086F94B;
    if ((unsigned int)(result) == 0) goto loc_0086F94D;
    goto loc_0086F94D;
loc_0086F94B:
    result = 0;
loc_0086F94D:
    result = ExAllocatePool2(256, v_stack_m90 + v_stack_m90 * 2 * 4 + 8 + result * 1, (unsigned int)(0x72506553ULL), result);
    v_stack_m88 = result;
    if (result == 0) goto loc_0086F433;
    if (*(unsigned __int64 *)(v_stack_m68) == 0) goto loc_0086F9C8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68)))) == 0) goto loc_0086F9E2;
loc_0086F98C:
    result = memcpy(result, *(unsigned __int64 *)(v_stack_m68), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68))) * 2 * 4 + 8)), result);
    result = SepConcatenatePrivileges(v_stack_m88, *(unsigned __int64 *)(v_stack_m68), v_stack_m78, result);
    if ((*(unsigned __int8 *)(v_stack_p8 + 11)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m68);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m78, result);
    }
    *(unsigned __int64 *)(v_stack_m68) = v_stack_m88;
    *(unsigned __int8 *)(v_stack_p8 + 11) = 1;
    goto loc_0086F433;
loc_0086F9C1:
    goto loc_0086F934;
loc_0086F9C8:
    result = 0;
    goto loc_0086F98C;
loc_0086F9CC:
    v_stack_p20 = v_stack_m94;
    result = guard_dispatch_icall(0, a2, v_stack_m78, result);
    goto loc_0086F6D2;
loc_0086F9E2:
    goto loc_0086F98C;
loc_0086F9E9:
    goto loc_0086F765;
}
```

## 5. (Beta) C Style

```c
int64_t ObpGrantAccess(void *Arg1, void *Arg2, void *Arg3, uint8_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m4F;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x59B4CD)) ^ (local_rsp);
    v_stack_m40 = result;
    Arg3 = 0;
    v_stack_m7C = 0;
    local_rsi = 1;
    if (((Arg5) & (0x400ULL)) == 0) { local_rsi = Arg4; }
    if (((uint32_t)(Arg1 - 1)) > 1) goto loc_0086F535;
    result = (Arg2 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 - 0x18));
    v_stack_m80 = 0;
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x757B85));
    v_stack_m70 = 0;
    v_stack_m94 = 0;
    v_stack_m90 = 0;
    v_stack_m60 = *(uint64_t *)(v_rip + 0x75852B + arg1 * 8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x75852B + arg1 * 8) + 0x98)) != (v_rip + 307144)) goto loc_0086F649;
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086F31C;
loc_0086F306:
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086F31C;
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) != 0) goto loc_0086F306;
loc_0086F31C:
    Arg2 = (uint32_t)((*(uint64_t *)(arg2 - 0x8)) & (15));
    local_rdi = (*(uint64_t *)(arg2 - 0x8)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_0086F334;
    if (local_rdi != 0) goto loc_0086F828;
loc_0086F334:
    v_stack_m98 = 0;
    if (local_rdi == 0) goto loc_0086F71B;
loc_0086F341:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg3 + 0x30) + 0x30), 1, Arg3, Arg4);
    if ((*(uint64_t *)(arg3 + 0x20)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg3 + 0x20);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mA0 = v_stack_m7C;
    v_stack_mA8 = v_stack_m80;
    v_stack_mB0 = (uint8_t)(local_rsi);
    v_stack_mB8 = *(uint64_t *)(v_rip + 0x75852B + arg1 * 8) + 76;
    v_stack_mC0 = v_stack_m70;
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x14)));
    result = SeAccessCheck(local_rdi, Arg3 + 32, 1, (uint32_t)(*(uint32_t *)(arg3 + 0x10)));
    v_stack_m78 = v_stack_m70;
    if (v_stack_m70 == 0) goto loc_0086F43C;
    v_stack_m68 = *(uint64_t *)(arg3 + 0x48);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48)))) * 1)) > 3) goto loc_0086F916;
    if (*(uint64_t *)(*(uint64_t *)(arg3 + 0x48)) == 0) goto loc_0086F700;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48))))) != 0) goto loc_0086F748;
    v_stack_m88 = 8;
loc_0086F413:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70)) + (uint32_t)(*(uint32_t *)(v_stack_m70)) * 2) << (2));
    Arg1 = ((uint32_t)(v_stack_m88)) + (*(uint64_t *)(*(uint64_t *)(arg3 + 0x48)));
    Arg2 = (v_stack_m70) + (8);
    result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48)))));
loc_0086F433:
    result = CmSiFreeMemory(v_stack_m70, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg3 + 0x48)))));
loc_0086F43C:
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_stack_m80;
        Arg1 = (uint32_t)(~(Arg1));
    }
    if ((uint8_t)(local_rsi) != 0) {
        Arg1 = v_stack_m60;
        result = Arg3 + 10;
        v_stack_mA0 = result;
        Arg1 = (Arg1) + (16);
        v_stack_mA8 = 0;
        Arg4 = local_rdi;
        v_stack_mB0 = (uint8_t)(local_rsi);
        Arg3 = 0;
        v_stack_mB8 = (uint8_t)((uint8_t)(result));
        Arg2 = Arg2;
        v_stack_mC0 = 0;
        v_stack_mC8 = 0;
        result = SeOpenObjectAuditAlarmWithTransaction(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg3 + 0x30) + 0x30), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg3 + 0x20) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg3 + 0x20) + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m98 != 0) goto loc_0086F70C;
loc_0086F4DF:
    Arg1 = (*(uint64_t *)(arg2 - 0x8)) ^ (local_rdi);
    if (Arg1 >= 15) goto loc_0086F816;
    if (Arg1 != 15) goto loc_0086F4DF;
loc_0086F4FB:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0086F9E9;
loc_0086F504:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x14)));
    result = 0;
loc_0086F50D:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
loc_0086F535:
    result = (result) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x757901));
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)));
    }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)))) & (0xF0000000ULL)) == 0) goto loc_0086F59E;
    result = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10));
    if (sign_flag) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7582AB + arg2 * 8) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7582AB + arg2 * 8) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7582AB + arg2 * 8) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x7582AB + arg2 * 8) + 0x58)));
    }
    result = (uint32_t)((result) & (0xFFFFFFFULL));
    *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)(result);
loc_0086F59E:
    if (condition_is_below) goto loc_0086F796;
loc_0086F5A8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10))) | (*(uint32_t *)(v_stack_p8 + 0x14)));
    *(uint32_t *)(v_stack_p8 + 0x14) = (uint32_t)(Arg1);
    *(uint32_t *)(v_stack_p8 + 0x10) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7582AB + arg2 * 8) + 0x5C))) & ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_p8 + 0x14) = (uint32_t)(result);
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086F5E5;
loc_0086F5CF:
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086F5E5;
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) != 0) goto loc_0086F5CF;
loc_0086F5E5:
    Arg2 = (uint32_t)((*(uint64_t *)(arg2 - 0x8)) & (15));
    local_rsi = (*(uint64_t *)(arg2 - 0x8)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_0086F5FD;
    if (local_rsi != 0) goto loc_0086F851;
loc_0086F5FD:
    result = SeComputeCreatorDeniedRights(v_stack_p8 + 32, v_stack_p8, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x14)), local_rsi);
    result = (uint32_t)(~(result));
    if (local_rsi == 0) goto loc_0086F504;
loc_0086F627:
    Arg1 = (*(uint64_t *)(arg2 - 0x8)) ^ (local_rsi);
    if (Arg1 >= 15) goto loc_0086F83F;
    if (Arg1 == 15) goto loc_0086F504;
    goto loc_0086F627;
loc_0086F649:
    v_stack_m90 = 447;
    v_stack_m94 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x59BD3D)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x59BD3D)))), (uint32_t)(0x7153624FULL), local_rsi);
    if (result == 0) goto loc_0086F808;
    v_stack_p40 = (uint8_t)(local_rsi);
    v_stack_p38 = (uint8_t)(result) + 76;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x64)));
    v_stack_p28 = Arg2 - 8;
    v_stack_m78 = Arg2 - 8;
    v_stack_m98 = 1;
    if ((*(uint64_t *)((uint8_t)(result) + 0x98)) != (v_rip + 5674)) goto loc_0086F76D;
    v_stack_p20 = v_stack_m94;
    result = CmpSecurityMethod(Arg2, 1, v_stack_m90, result);
loc_0086F6D2:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_0086F896;
loc_0086F6E0:
    if (sign_flag) goto loc_0086F75B;
    if (result != 0) goto loc_0086F341;
loc_0086F6EE:
    *(uint32_t *)(v_stack_p8 + 0x10) = 0;
    goto loc_0086F504;
loc_0086F700:
    v_stack_m88 = 0;
    goto loc_0086F413;
loc_0086F70C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m90, result);
    goto loc_0086F4FB;
loc_0086F71B:
    if (((*(uint8_t *)((uint8_t)(result) + 0x42)) & (8)) != 0) {
        v_stack_p20 = v_stack_m90;
        Arg2 = Arg2 - 48;
        Arg3 = (uint8_t)(result);
        Arg4 = 1;
        Arg1 = 393;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(arg2 - 0x16)) & (2)) == 0) goto loc_0086F6EE;
    goto loc_0086F722;
loc_0086F748:
    v_stack_m88 = (uint32_t)(Arg4 + Arg4 * 2 * 4 + 8);
    goto loc_0086F413;
loc_0086F75B:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
loc_0086F765:
    goto loc_0086F50D;
loc_0086F76D:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) != (v_rip + 17164)) goto loc_0086F9CC;
    v_stack_p20 = v_stack_m94;
    result = IopGetSetSecurityObject(0, Arg2, Arg3, result);
    goto loc_0086F6D2;
loc_0086F796:
    v_stack_m50 = *(uint64_t *)(v_rip + 0x76A363);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m48 = (uint32_t)(Arg3);
    if ((uint8_t)(local_rsi) == 0) goto loc_0086F874;
    if (*(uint64_t *)(v_stack_p8 + 0x20) != 0) goto loc_0086F865;
loc_0086F7CD:
    v_stack_p20 = (uint8_t)(local_rsi);
    result = SepPrivilegeCheck(*(uint64_t *)(v_stack_p8 + 0x30), v_stack_m50, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_0086F874;
loc_0086F7EC:
    Arg4 = 0;
    Arg1 = 0;
    result = SePrivilegedServiceAuditAlarm(Arg1, v_stack_p8 + 32, v_stack_m58, Arg4);
    goto loc_0086F50D;
loc_0086F808:
    goto loc_0086F50D;
loc_0086F816:
    result = ObDereferenceSecurityDescriptor(result, 1, v_stack_m58, Arg4);
    goto loc_0086F4FB;
loc_0086F828:
    result = ObpReferenceSecurityDescriptorSlow(Arg2 - 48, 1, result, Arg4);
    Arg3 = 0;
    goto loc_0086F334;
loc_0086F83F:
    result = ObDereferenceSecurityDescriptor(local_rsi, 1, Arg3, Arg4);
    goto loc_0086F504;
loc_0086F851:
    result = ObpReferenceSecurityDescriptorSlow(Arg2 - 48, 1, local_rsi, Arg4);
    goto loc_0086F5FD;
loc_0086F865:
    if ((*(uint32_t *)(v_stack_p8 + 0x28)) >= 2) goto loc_0086F7CD;
    goto loc_0086F7EC;
loc_0086F874:
    result = SeAppendPrivileges(v_stack_p8, v_stack_m58, local_rsi, Arg4);
    Arg3 = 0;
    goto loc_0086F5A8;
loc_0086F896:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x59BADC) = (uint32_t)((uint32_t)(v_stack_m94));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_m94))), (uint32_t)(0x7153624FULL), Arg4);
    if (result == 0) goto loc_0086F808;
    v_stack_p40 = (uint8_t)(result);
    v_stack_p38 = (uint8_t)(result) + 76;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x64)));
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = v_stack_m94;
    v_stack_m98 = 1;
    result = guard_dispatch_icall(0, 1, v_stack_m90, result);
    goto loc_0086F6E0;
loc_0086F916:
    if ((uint32_t)(v_stack_m90) == 0) goto loc_0086F9C1;
loc_0086F934:
    if ((uint32_t)((uint32_t)(result)) == 0) goto loc_0086F94B;
    if ((uint32_t)(result) == 0) goto loc_0086F94D;
    goto loc_0086F94D;
loc_0086F94B:
    result = 0;
loc_0086F94D:
    result = ExAllocatePool2(256, v_stack_m90 + v_stack_m90 * 2 * 4 + 8 + result * 1, (uint32_t)(0x72506553ULL), result);
    v_stack_m88 = result;
    if (result == 0) goto loc_0086F433;
    if (*(uint64_t *)(v_stack_m68) == 0) goto loc_0086F9C8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68)))) == 0) goto loc_0086F9E2;
loc_0086F98C:
    result = memcpy(result, *(uint64_t *)(v_stack_m68), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68))) * 2 * 4 + 8)), result);
    result = SepConcatenatePrivileges(v_stack_m88, *(uint64_t *)(v_stack_m68), v_stack_m78, result);
    if ((*(uint8_t *)(v_stack_p8 + 0xB)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m68);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m78, result);
    }
    *(uint64_t *)(v_stack_m68) = v_stack_m88;
    *(uint8_t *)(v_stack_p8 + 0xB) = 1;
    goto loc_0086F433;
loc_0086F9C1:
    goto loc_0086F934;
loc_0086F9C8:
    result = 0;
    goto loc_0086F98C;
loc_0086F9CC:
    v_stack_p20 = v_stack_m94;
    result = guard_dispatch_icall(0, Arg2, v_stack_m78, result);
    goto loc_0086F6D2;
loc_0086F9E2:
    goto loc_0086F98C;
loc_0086F9E9:
    goto loc_0086F765;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x1` | `32` | `R` |
| `Arg2` | `- 0x30` | `64` | `R` |
| `Arg2` | `- 0x18` | `8` | `R` |
| `Arg2` | `- 0x16` | `8` | `R` |
| `Arg2` | `- 0x8` | `8` | `R` |
| `Arg2` | `- 0x8` | `64` | `R` |
| `Arg3` | `+ 0xA` | `64` | `R` |
| `Arg3` | `+ 0xB` | `8` | `R` |
| `Arg3` | `+ 0xB` | `8` | `W` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R/W` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg3` | `+ 0x14` | `32` | `R` |
| `Arg3` | `+ 0x14` | `32` | `R/W` |
| `Arg3` | `+ 0x14` | `32` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x28` | `32` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |
| `Arg3` | `+ 0x48` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086F250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
