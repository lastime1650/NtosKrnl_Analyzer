# SepAppendAceToTokenObjectAcl

- RVA: `0x008B6430`–`0x008B6D7B` (길이 `2,379` bytes)
- VA: `0x00000001408B6430`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A68`
- 디코드: `599`개 명령, `2,379/2,379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x008B64C0` → [ObpReferenceSecurityDescriptor](ObpReferenceSecurityDescriptor_function_008B6D90.md) (function, `0x008B6D90`)
- `0x008B6526` → [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) (function, `0x00870CC0`)
- `0x008B65E2` → [RtlFindAceBySid](../../text/40/RtlFindAceBySid_function_004004E0.md) (function, `0x004004E0`)
- `0x008B6638` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x008B6656` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6692` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B66B8` → [RtlGetAce](../../text/40/RtlGetAce_function_0040FAF0.md) (function, `0x0040FAF0`)
- `0x008B66D6` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B67E6` → [RtlValidAcl](../92/RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x008B6840` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B688A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B68D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B691B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008B6934` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008B6996` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008B699E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008B69AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B69EA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008B69F2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008B6A3C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008B6A63` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B6B25` → [SeDefaultObjectMethod](SeDefaultObjectMethod_function_008BA2B0.md) (function, `0x008BA2B0`)
- `0x008B6B35` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6B4C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6B7C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B6BA5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6BC8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6BF9` → [IopGetSetSecurityObject](../87/IopGetSetSecurityObject_function_00873A80.md) (function, `0x00873A80`)
- `0x008B6C12` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008B6C4B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6C58` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008B6C67` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6C82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6CC8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B6CDE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6CF8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B6D0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B6D61` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F4C78`
- [sub_00892023](../89/Unknown_function_00892023.md) at `0x00892073`
- [SepFinalizeTokenAcls](SepFinalizeTokenAcls_function_008B63F4.md) at `0x008B6409`
- [NtDuplicateToken](NtDuplicateToken_function_008B6DF0.md) at `0x008B700E`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC174`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC3EA`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC419`
- [SeCopyClientToken](../9E/SeCopyClientToken_function_009EC5A8.md) at `0x009EC69D`
- [SeCopyClientToken](../9E/SeCopyClientToken_function_009EC5A8.md) at `0x009EC741`
- [SeSubProcessToken](../AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADDB7`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA2FA`

### Static image references
- `0x008B647C` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008B648A` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x008B64A0` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x008B64E7` → RVA `0x00870CC0` (`CmpSecurityMethod`; read)
- `0x008B686D` → RVA `0x00E0B38C` (`.data`; read)
- `0x008B68FC` → RVA `0x00FD0EC0` (`CACHEALI`; read)
- `0x008B6BD8` → RVA `0x00873A80` (`IopGetSetSecurityObject`; read)
- `0x008B6C76` → RVA `0x00E0B38C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **31**
  - `0x008B65E2` → [RtlFindAceBySid](../../text/40/RtlFindAceBySid_function_004004E0.md) (`PAGE` → `.text`)
  - `0x008B6638` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x008B6656` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6692` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B66B8` → [RtlGetAce](../../text/40/RtlGetAce_function_0040FAF0.md) (`PAGE` → `.text`)
  - `0x008B6840` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B688A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B68D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B691B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008B6934` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008B6996` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008B699E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008B69AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B69EA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008B69F2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008B6A3C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008B6B35` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6B4C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6B7C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B6BA5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6BC8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6C12` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008B6C4B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6C58` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008B6C67` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6C82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6CC8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B6CDE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6CF8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B6D0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B6D61` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B6430  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008B6435  55                              push rbp
008B6436  56                              push rsi
008B6437  57                              push rdi
008B6438  41 54                           push r12
008B643A  41 55                           push r13
008B643C  41 56                           push r14
008B643E  41 57                           push r15
008B6440  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
008B6445  48 81 EC C0 00 00 00            sub rsp, 0xc0
008B644C  33 C0                           xor eax, eax
008B644E  48 89 4D 17                     mov qword ptr [rbp + 0x17], rcx
008B6452  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008B6456  45 33 E4                        xor r12d, r12d
008B6459  48 8D 41 D0                     lea rax, [rcx - 0x30]
008B645D  44 89 65 BB                     mov dword ptr [rbp - 0x45], r12d
008B6461  48 C1 E8 08                     shr rax, 8
008B6465  4C 8B E9                        mov r13, rcx
008B6468  0F B6 49 E8                     movzx ecx, byte ptr [rcx - 0x18]
008B646C  0F 57 C0                        xorps xmm0, xmm0
008B646F  0F B6 C0                        movzx eax, al
008B6472  4D 8B F8                        mov r15, r8
008B6475  48 33 C8                        xor rcx, rax
008B6478  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
008B647C  0F B6 05 C9 09 71 00            movzx eax, byte ptr [rip + 0x7109c9]
008B6483  48 33 C8                        xor rcx, rax
008B6486  44 89 65 C7                     mov dword ptr [rbp - 0x39], r12d
008B648A  48 8D 05 6F 13 71 00            lea rax, [rip + 0x71136f]
008B6491  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
008B6495  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
008B6499  89 55 D7                        mov dword ptr [rbp - 0x29], edx
008B649C  48 8B 34 C8                     mov rsi, qword ptr [rax + rcx*8]
008B64A0  48 8D 05 09 3E 00 00            lea rax, [rip + 0x3e09]
008B64A7  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
008B64AB  4C 89 65 E7                     mov qword ptr [rbp - 0x19], r12
008B64AF  48 39 86 98 00 00 00            cmp qword ptr [rsi + 0x98], rax
008B64B6  0F 85 B1 03 00 00               jne 0x1408b686d
008B64BC  49 8D 4D D0                     lea rcx, [r13 - 0x30]
008B64C0  E8 CB 08 00 00                  call 0x1408b6d90
008B64C5  45 32 F6                        xor r14b, r14b
008B64C8  48 8B F8                        mov rdi, rax
008B64CB  48 85 C0                        test rax, rax
008B64CE  0F 84 47 05 00 00               je 0x1408b6a1b
008B64D4  41 8B DC                        mov ebx, r12d
008B64D7  EB 72                           jmp 0x1408b654b
008B64D9  48 8B 86 98 00 00 00            mov rax, qword ptr [rsi + 0x98]
008B64E0  4C 8D 76 4C                     lea r14, [rsi + 0x4c]
008B64E4  8B 4E 64                        mov ecx, dword ptr [rsi + 0x64]
008B64E7  48 8D 15 D2 A7 FB FF            lea rdx, [rip - 0x4582e]
008B64EE  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
008B64F3  4D 8D 7D F8                     lea r15, [r13 - 8]
008B64F7  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
008B64FC  4C 8B CF                        mov r9, rdi
008B64FF  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
008B6503  4C 8D 45 C7                     lea r8, [rbp - 0x39]
008B6507  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008B650C  48 3B C2                        cmp rax, rdx
008B650F  0F 85 C3 06 00 00               jne 0x1408b6bd8
008B6515  48 8D 45 BB                     lea rax, [rbp - 0x45]
008B6519  BA 01 00 00 00                  mov edx, 1
008B651E  49 8B CD                        mov rcx, r13
008B6521  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B6526  E8 95 A7 FB FF                  call 0x140870cc0
008B652B  8B D8                           mov ebx, eax
008B652D  3D 23 00 00 C0                  cmp eax, 0xc0000023
008B6532  0F 84 2A 07 00 00               je 0x1408b6c62
008B6538  85 DB                           test ebx, ebx
008B653A  0F 88 83 06 00 00               js 0x1408b6bc3
008B6540  41 B6 01                        mov r14b, 1
008B6543  85 DB                           test ebx, ebx
008B6545  78 1A                           js 0x1408b6561
008B6547  4C 8B 7D DF                     mov r15, qword ptr [rbp - 0x21]
008B654B  48 85 FF                        test rdi, rdi
008B654E  74 47                           je 0x1408b6597
008B6550  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
008B6554  A8 04                           test al, 4
008B6556  75 5D                           jne 0x1408b65b5
008B6558  4C 8B EF                        mov r13, rdi
008B655B  45 0F B6 E6                     movzx r12d, r14b
008B655F  EB 0C                           jmp 0x1408b656d
008B6561  4C 8B EF                        mov r13, rdi
008B6564  45 0F B6 E6                     movzx r12d, r14b
008B6568  48 85 FF                        test rdi, rdi
008B656B  74 2A                           je 0x1408b6597
008B656D  45 84 E4                        test r12b, r12b
008B6570  0F 85 D0 06 00 00               jne 0x1408b6c46
008B6576  49 8D 7D E0                     lea rdi, [r13 - 0x20]
008B657A  0F 0D 4F 08                     prefetchw byte ptr [rdi + 8]
008B657E  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008B6582  48 8D 48 FF                     lea rcx, [rax - 1]
008B6586  48 85 C9                        test rcx, rcx
008B6589  0F 8E 53 03 00 00               jle 0x1408b68e2
008B658F  F0 48 0F B1 4F 08               lock cmpxchg qword ptr [rdi + 8], rcx
008B6595  75 EB                           jne 0x1408b6582
008B6597  8B C3                           mov eax, ebx
008B6599  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008B65A1  48 81 C4 C0 00 00 00            add rsp, 0xc0
008B65A8  41 5F                           pop r15
008B65AA  41 5E                           pop r14
008B65AC  41 5D                           pop r13
008B65AE  41 5C                           pop r12
008B65B0  5F                              pop rdi
008B65B1  5E                              pop rsi
008B65B2  5D                              pop rbp
008B65B3  C3                              ret
008B65B4  CC                              int3
008B65B5  66 85 C0                        test ax, ax
008B65B8  0F 89 70 06 00 00               jns 0x1408b6c2e
008B65BE  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008B65C1  85 C0                           test eax, eax
008B65C3  0F 84 51 07 00 00               je 0x1408b6d1a
008B65C9  48 8D 34 07                     lea rsi, [rdi + rax]
008B65CD  4C 8B EF                        mov r13, rdi
008B65D0  45 0F B6 E6                     movzx r12d, r14b
008B65D4  48 85 F6                        test rsi, rsi
008B65D7  74 94                           je 0x1408b656d
008B65D9  45 33 C0                        xor r8d, r8d
008B65DC  49 8B D7                        mov rdx, r15
008B65DF  48 8B CE                        mov rcx, rsi
008B65E2  E8 F9 9E B4 FF                  call 0x1404004e0
008B65E7  48 85 C0                        test rax, rax
008B65EA  75 81                           jne 0x1408b656d
008B65EC  0F B6 06                        movzx eax, byte ptr [rsi]
008B65EF  88 45 B7                        mov byte ptr [rbp - 0x49], al
008B65F2  2C 02                           sub al, 2
008B65F4  3C 02                           cmp al, 2
008B65F6  0F 87 C4 02 00 00               ja 0x1408b68c0
008B65FC  0F B7 56 04                     movzx edx, word ptr [rsi + 4]
008B6600  4C 8D 7E 08                     lea r15, [rsi + 8]
008B6604  45 33 C0                        xor r8d, r8d
008B6607  41 8B C8                        mov ecx, r8d
008B660A  41 0F B6 FC                     movzx edi, r12b
008B660E  4D 8B F5                        mov r14, r13
008B6611  3B CA                           cmp ecx, edx
008B6613  0F 82 8C 02 00 00               jb 0x1408b68a5
008B6619  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
008B661D  48 8D 04 0E                     lea rax, [rsi + rcx]
008B6621  4C 3B F8                        cmp r15, rax
008B6624  4D 0F 47 F8                     cmova r15, r8
008B6628  4D 85 FF                        test r15, r15
008B662B  0F 84 F5 06 00 00               je 0x1408b6d26
008B6631  44 2B FE                        sub r15d, esi
008B6634  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
008B6638  E8 33 6C BA FF                  call 0x14045d270
008B663D  41 B8 53 65 41 63               mov r8d, 0x63416553
008B6643  B9 00 01 00 00                  mov ecx, 0x100
008B6648  8D 58 0B                        lea ebx, [rax + 0xb]
008B664B  41 03 DF                        add ebx, r15d
008B664E  83 E3 FC                        and ebx, 0xfffffffc
008B6651  8B D3                           mov edx, ebx
008B6653  44 8B E3                        mov r12d, ebx
008B6656  E8 95 BA 2C 00                  call 0x140b820f0
008B665B  4C 8B E8                        mov r13, rax
008B665E  48 85 C0                        test rax, rax
008B6661  0F 84 C7 06 00 00               je 0x1408b6d2e
008B6667  83 FB 08                        cmp ebx, 8
008B666A  0F 82 CF 06 00 00               jb 0x1408b6d3f
008B6670  0F B6 45 B7                     movzx eax, byte ptr [rbp - 0x49]
008B6674  2C 02                           sub al, 2
008B6676  3C 02                           cmp al, 2
008B6678  0F 87 9E 05 00 00               ja 0x1408b6c1c
008B667E  81 FB FC FF 00 00               cmp ebx, 0xfffc
008B6684  0F 87 92 05 00 00               ja 0x1408b6c1c
008B668A  45 8B C4                        mov r8d, r12d
008B668D  33 D2                           xor edx, edx
008B668F  49 8B CD                        mov rcx, r13
008B6692  E8 A9 05 E1 FF                  call 0x1406c6c40
008B6697  0F B6 45 B7                     movzx eax, byte ptr [rbp - 0x49]
008B669B  4C 8D 45 E7                     lea r8, [rbp - 0x19]
008B669F  41 88 45 00                     mov byte ptr [r13], al
008B66A3  33 D2                           xor edx, edx
008B66A5  33 C0                           xor eax, eax
008B66A7  41 C6 45 01 00                  mov byte ptr [r13 + 1], 0
008B66AC  48 8B CE                        mov rcx, rsi
008B66AF  41 89 45 04                     mov dword ptr [r13 + 4], eax
008B66B3  66 41 89 5D 02                  mov word ptr [r13 + 2], bx
008B66B8  E8 33 94 B5 FF                  call 0x14040faf0
008B66BD  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
008B66C1  8B D8                           mov ebx, eax
008B66C3  44 0F B6 E7                     movzx r12d, dil
008B66C7  85 C0                           test eax, eax
008B66C9  0F 88 8D 06 00 00               js 0x1408b6d5c
008B66CF  49 8B CD                        mov rcx, r13
008B66D2  41 83 C7 F8                     add r15d, -8
008B66D6  E8 C5 40 07 00                  call 0x14092a7a0
008B66DB  84 C0                           test al, al
008B66DD  0F 84 66 06 00 00               je 0x1408b6d49
008B66E3  45 0F B7 45 04                  movzx r8d, word ptr [r13 + 4]
008B66E8  49 8D 5D 08                     lea rbx, [r13 + 8]
008B66EC  45 33 D2                        xor r10d, r10d
008B66EF  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
008B66F3  41 8B D2                        mov edx, r10d
008B66F6  48 8B CB                        mov rcx, rbx
008B66F9  49 8B F6                        mov rsi, r14
008B66FC  41 3B D0                        cmp edx, r8d
008B66FF  0F 82 49 01 00 00               jb 0x1408b684e
008B6705  41 0F B6 45 00                  movzx eax, byte ptr [r13]
008B670A  44 0F B6 75 B7                  movzx r14d, byte ptr [rbp - 0x49]
008B670F  4C 8B 45 E7                     mov r8, qword ptr [rbp - 0x19]
008B6713  41 8B FE                        mov edi, r14d
008B6716  45 0F B7 5D 02                  movzx r11d, word ptr [r13 + 2]
008B671B  4D 8B C8                        mov r9, r8
008B671E  4D 03 DD                        add r11, r13
008B6721  44 89 55 BF                     mov dword ptr [rbp - 0x41], r10d
008B6725  49 3B CB                        cmp rcx, r11
008B6728  41 8B D7                        mov edx, r15d
008B672B  49 0F 47 CA                     cmova rcx, r10
008B672F  44 3A F0                        cmp r14b, al
008B6732  4F 8D 14 07                     lea r10, [r15 + r8]
008B6736  0F 46 F8                        cmovbe edi, eax
008B6739  4D 3B CA                        cmp r9, r10
008B673C  0F 82 73 02 00 00               jb 0x1408b69b5
008B6742  0F 87 53 04 00 00               ja 0x1408b6b9b
008B6748  48 85 C9                        test rcx, rcx
008B674B  0F 84 83 05 00 00               je 0x1408b6cd4
008B6751  49 8D 04 0F                     lea rax, [r15 + rcx]
008B6755  49 3B C3                        cmp rax, r11
008B6758  0F 87 76 05 00 00               ja 0x1408b6cd4
008B675E  2B CB                           sub ecx, ebx
008B6760  83 E9 01                        sub ecx, 1
008B6763  4C 63 C9                        movsxd r9, ecx
008B6766  0F 89 EE 03 00 00               jns 0x1408b6b5a
008B676C  45 85 FF                        test r15d, r15d
008B676F  74 20                           je 0x1408b6791
008B6771  48 8B C3                        mov rax, rbx
008B6774  4C 2B C3                        sub r8, rbx
008B6777  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
008B6780  41 0F B6 0C 00                  movzx ecx, byte ptr [r8 + rax]
008B6785  88 08                           mov byte ptr [rax], cl
008B6787  48 8D 40 01                     lea rax, [rax + 1]
008B678B  48 83 EA 01                     sub rdx, 1
008B678F  75 EF                           jne 0x1408b6780
008B6791  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
008B6794  66 41 01 45 04                  add word ptr [r13 + 4], ax
008B6799  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
008B67A3  4C 8B 75 DF                     mov r14, qword ptr [rbp - 0x21]
008B67A7  41 88 7D 00                     mov byte ptr [r13], dil
008B67AB  4C 3B F0                        cmp r14, rax
008B67AE  0F 86 16 01 00 00               jbe 0x1408b68ca
008B67B4  41 0F B6 06                     movzx eax, byte ptr [r14]
008B67B8  24 0F                           and al, 0xf
008B67BA  3C 01                           cmp al, 1
008B67BC  0F 85 08 01 00 00               jne 0x1408b68ca
008B67C2  41 80 7E 01 0F                  cmp byte ptr [r14 + 1], 0xf
008B67C7  0F 87 FD 00 00 00               ja 0x1408b68ca
008B67CD  40 80 FF 04                     cmp dil, 4
008B67D1  0F 87 6B 03 00 00               ja 0x1408b6b42
008B67D7  0F B6 45 B7                     movzx eax, byte ptr [rbp - 0x49]
008B67DB  40 3A F8                        cmp dil, al
008B67DE  77 03                           ja 0x1408b67e3
008B67E0  0F B6 F8                        movzx edi, al
008B67E3  49 8B CD                        mov rcx, r13
008B67E6  E8 B5 3F 07 00                  call 0x14092a7a0
008B67EB  84 C0                           test al, al
008B67ED  0F 84 0F 05 00 00               je 0x1408b6d02
008B67F3  41 0F B7 55 04                  movzx edx, word ptr [r13 + 4]
008B67F8  45 33 FF                        xor r15d, r15d
008B67FB  41 8B CF                        mov ecx, r15d
008B67FE  3B CA                           cmp ecx, edx
008B6800  0F 82 F6 01 00 00               jb 0x1408b69fc
008B6806  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
008B680B  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B6810  49 03 D5                        add rdx, r13
008B6813  48 3B DA                        cmp rbx, rdx
008B6816  49 0F 47 DF                     cmova rbx, r15
008B681A  66 83 C1 04                     add cx, 4
008B681E  66 C1 E1 02                     shl cx, 2
008B6822  48 85 DB                        test rbx, rbx
008B6825  74 0F                           je 0x1408b6836
008B6827  0F B7 C1                        movzx eax, cx
008B682A  48 03 C3                        add rax, rbx
008B682D  48 3B C2                        cmp rax, rdx
008B6830  0F 86 0C 02 00 00               jbe 0x1408b6a42
008B6836  33 D2                           xor edx, edx
008B6838  49 8B CD                        mov rcx, r13
008B683B  BB 99 00 00 C0                  mov ebx, 0xc0000099
008B6840  E8 2B C0 2C 00                  call 0x140b82870
008B6845  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6849  E9 1F FD FF FF                  jmp 0x1408b656d
008B684E  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
008B6853  49 03 C5                        add rax, r13
008B6856  48 3B C8                        cmp rcx, rax
008B6859  0F 83 3C 03 00 00               jae 0x1408b6b9b
008B685F  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
008B6863  FF C2                           inc edx
008B6865  48 03 C8                        add rcx, rax
008B6868  E9 8F FE FF FF                  jmp 0x1408b66fc
008B686D  8B 05 19 4B 55 00               mov eax, dword ptr [rip + 0x554b19]
008B6873  B9 00 01 00 00                  mov ecx, 0x100
008B6878  8B D0                           mov edx, eax
008B687A  C7 45 C7 BF 01 00 00            mov dword ptr [rbp - 0x39], 0x1bf
008B6881  41 B8 4F 62 53 71               mov r8d, 0x7153624f
008B6887  89 45 BB                        mov dword ptr [rbp - 0x45], eax
008B688A  E8 61 B8 2C 00                  call 0x140b820f0
008B688F  48 8B F8                        mov rdi, rax
008B6892  48 85 C0                        test rax, rax
008B6895  0F 85 3E FC FF FF               jne 0x1408b64d9
008B689B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008B68A0  E9 F2 FC FF FF                  jmp 0x1408b6597
008B68A5  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
008B68A9  48 03 C6                        add rax, rsi
008B68AC  4C 3B F8                        cmp r15, rax
008B68AF  73 0F                           jae 0x1408b68c0
008B68B1  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
008B68B6  FF C1                           inc ecx
008B68B8  4C 03 F8                        add r15, rax
008B68BB  E9 4A FD FF FF                  jmp 0x1408b660a
008B68C0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B68C5  E9 A3 FC FF FF                  jmp 0x1408b656d
008B68CA  33 D2                           xor edx, edx
008B68CC  49 8B CD                        mov rcx, r13
008B68CF  BB 78 00 00 C0                  mov ebx, 0xc0000078
008B68D4  E8 97 BF 2C 00                  call 0x140b82870
008B68D9  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B68DD  E9 8B FC FF FF                  jmp 0x1408b656d
008B68E2  0F 85 87 04 00 00               jne 0x1408b6d6f
008B68E8  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008B68EB  45 33 C0                        xor r8d, r8d
008B68EE  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
008B68F7  33 D2                           xor edx, edx
008B68F9  0F B6 F0                        movzx esi, al
008B68FC  48 8D 05 BD A5 71 00            lea rax, [rip + 0x71a5bd]
008B6903  48 C1 E6 04                     shl rsi, 4
008B6907  48 03 F0                        add rsi, rax
008B690A  66 41 FF 8C 24 E4 01 00 00      dec word ptr [r12 + 0x1e4]
008B6913  48 8B CE                        mov rcx, rsi
008B6916  90                              nop
008B6917  4C 8D 76 08                     lea r14, [rsi + 8]
008B691B  E8 10 99 95 FF                  call 0x140210230
008B6920  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
008B6926  4C 8B F8                        mov r15, rax
008B6929  73 0E                           jae 0x1408b6939
008B692B  4C 8B C6                        mov r8, rsi
008B692E  48 8B D0                        mov rdx, rax
008B6931  48 8B CE                        mov rcx, rsi
008B6934  E8 57 93 95 FF                  call 0x14020fc90
008B6939  4D 85 FF                        test r15, r15
008B693C  74 05                           je 0x1408b6943
008B693E  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008B6943  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008B694A  48 8B C8                        mov rcx, rax
008B694D  F0 48 0F C1 4F 08               lock xadd qword ptr [rdi + 8], rcx
008B6953  48 83 E9 01                     sub rcx, 1
008B6957  7F 7F                           jg 0x1408b69d8
008B6959  48 85 C9                        test rcx, rcx
008B695C  75 73                           jne 0x1408b69d1
008B695E  49 8B 16                        mov rdx, qword ptr [r14]
008B6961  48 3B D7                        cmp rdx, rdi
008B6964  74 18                           je 0x1408b697e
008B6966  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
008B6970  48 8B 0A                        mov rcx, qword ptr [rdx]
008B6973  4C 8B F2                        mov r14, rdx
008B6976  48 8B D1                        mov rdx, rcx
008B6979  48 3B CF                        cmp rcx, rdi
008B697C  75 F2                           jne 0x1408b6970
008B697E  48 8B 17                        mov rdx, qword ptr [rdi]
008B6981  49 89 16                        mov qword ptr [r14], rdx
008B6984  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
008B6989  24 06                           and al, 6
008B698B  3C 02                           cmp al, 2
008B698D  0F 84 7C 02 00 00               je 0x1408b6c0f
008B6993  48 8B CE                        mov rcx, rsi
008B6996  E8 65 AC A2 FF                  call 0x1402e1600
008B699B  49 8B CC                        mov rcx, r12
008B699E  E8 4D 86 9A FF                  call 0x14025eff0
008B69A3  BA 4F 62 53 63                  mov edx, 0x6353624f
008B69A8  48 8B CF                        mov rcx, rdi
008B69AB  E8 C0 BE 2C 00                  call 0x140b82870
008B69B0  E9 E2 FB FF FF                  jmp 0x1408b6597
008B69B5  41 0F B6 01                     movzx eax, byte ptr [r9]
008B69B9  3C 03                           cmp al, 3
008B69BB  0F 87 C2 01 00 00               ja 0x1408b6b83
008B69C1  41 0F B7 41 02                  movzx eax, word ptr [r9 + 2]
008B69C6  4C 03 C8                        add r9, rax
008B69C9  FF 45 BF                        inc dword ptr [rbp - 0x41]
008B69CC  E9 68 FD FF FF                  jmp 0x1408b6739
008B69D1  B9 0E 00 00 00                  mov ecx, 0xe
008B69D6  CD 29                           int 0x29
008B69D8  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
008B69DD  24 06                           and al, 6
008B69DF  3C 02                           cmp al, 2
008B69E1  0F 84 6E 02 00 00               je 0x1408b6c55
008B69E7  48 8B CE                        mov rcx, rsi
008B69EA  E8 11 AC A2 FF                  call 0x1402e1600
008B69EF  49 8B CC                        mov rcx, r12
008B69F2  E8 F9 85 9A FF                  call 0x14025eff0
008B69F7  E9 9B FB FF FF                  jmp 0x1408b6597
008B69FC  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
008B6A01  49 03 C5                        add rax, r13
008B6A04  48 3B D8                        cmp rbx, rax
008B6A07  0F 83 F5 02 00 00               jae 0x1408b6d02
008B6A0D  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
008B6A11  FF C1                           inc ecx
008B6A13  48 03 D8                        add rbx, rax
008B6A16  E9 E3 FD FF FF                  jmp 0x1408b67fe
008B6A1B  F6 46 42 08                     test byte ptr [rsi + 0x42], 8
008B6A1F  0F 84 8E 01 00 00               je 0x1408b6bb3
008B6A25  41 B9 01 00 00 00               mov r9d, 1
008B6A2B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008B6A30  4C 8B C6                        mov r8, rsi
008B6A33  49 8D 55 D0                     lea rdx, [r13 - 0x30]
008B6A37  B9 89 01 00 00                  mov ecx, 0x189
008B6A3C  E8 1F 6C C4 FF                  call 0x1404fd660
008B6A41  CC                              int3
008B6A42  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
008B6A45  48 8D 53 08                     lea rdx, [rbx + 8]
008B6A49  66 89 4B 02                     mov word ptr [rbx + 2], cx
008B6A4D  4D 8B C6                        mov r8, r14
008B6A50  89 43 04                        mov dword ptr [rbx + 4], eax
008B6A53  66 44 89 3B                     mov word ptr [rbx], r15w
008B6A57  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
008B6A5C  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
008B6A63  E8 E8 2F 0F 00                  call 0x1409a9a50
008B6A68  66 41 FF 45 04                  inc word ptr [r13 + 4]
008B6A6D  33 C0                           xor eax, eax
008B6A6F  41 88 7D 00                     mov byte ptr [r13], dil
008B6A73  0F 57 C0                        xorps xmm0, xmm0
008B6A76  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
008B6A7A  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008B6A7E  0F B7 45 F1                     movzx eax, word ptr [rbp - 0xf]
008B6A82  C6 45 EF 01                     mov byte ptr [rbp - 0x11], 1
008B6A86  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
008B6A8A  66 85 C0                        test ax, ax
008B6A8D  0F 88 C0 02 00 00               js 0x1408b6d53
008B6A93  4C 89 6D 0F                     mov qword ptr [rbp + 0xf], r13
008B6A97  B9 F7 FF 00 00                  mov ecx, 0xfff7
008B6A9C  66 23 C1                        and ax, cx
008B6A9F  C7 45 BF 04 00 00 00            mov dword ptr [rbp - 0x41], 4
008B6AA6  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
008B6AAA  66 83 C8 04                     or ax, 4
008B6AAE  66 89 45 F1                     mov word ptr [rbp - 0xf], ax
008B6AB2  0F B6 45 1F                     movzx eax, byte ptr [rbp + 0x1f]
008B6AB6  0F B6 51 E8                     movzx edx, byte ptr [rcx - 0x18]
008B6ABA  4C 8D 51 F8                     lea r10, [rcx - 8]
008B6ABE  48 33 D0                        xor rdx, rax
008B6AC1  0F B6 05 84 03 71 00            movzx eax, byte ptr [rip + 0x710384]
008B6AC8  48 33 D0                        xor rdx, rax
008B6ACB  48 8D 05 2E 0D 71 00            lea rax, [rip + 0x710d2e]
008B6AD2  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
008B6AD6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B6ADF  44 8B 4A 64                     mov r9d, dword ptr [rdx + 0x64]
008B6AE3  44 0F B6 80 32 02 00 00         movzx r8d, byte ptr [rax + 0x232]
008B6AEB  48 8D 42 4C                     lea rax, [rdx + 0x4c]
008B6AEF  4C 8B 9A 98 00 00 00            mov r11, qword ptr [rdx + 0x98]
008B6AF6  48 8D 15 B3 37 00 00            lea rdx, [rip + 0x37b3]
008B6AFD  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
008B6B02  4C 8D 45 BF                     lea r8, [rbp - 0x41]
008B6B06  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B6B0B  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
008B6B10  4C 8D 4D EF                     lea r9, [rbp - 0x11]
008B6B14  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
008B6B19  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008B6B1E  4C 3B DA                        cmp r11, rdx
008B6B21  75 54                           jne 0x1408b6b77
008B6B23  33 D2                           xor edx, edx
008B6B25  E8 86 37 00 00                  call 0x1408ba2b0
008B6B2A  33 D2                           xor edx, edx
008B6B2C  48 89 75 CF                     mov qword ptr [rbp - 0x31], rsi
008B6B30  49 8B CD                        mov rcx, r13
008B6B33  8B D8                           mov ebx, eax
008B6B35  E8 36 BD 2C 00                  call 0x140b82870
008B6B3A  4C 8B EE                        mov r13, rsi
008B6B3D  E9 2B FA FF FF                  jmp 0x1408b656d
008B6B42  33 D2                           xor edx, edx
008B6B44  49 8B CD                        mov rcx, r13
008B6B47  BB 59 00 00 C0                  mov ebx, 0xc0000059
008B6B4C  E8 1F BD 2C 00                  call 0x140b82870
008B6B51  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6B55  E9 13 FA FF FF                  jmp 0x1408b656d
008B6B5A  46 8D 14 39                     lea r10d, [rcx + r15]
008B6B5E  42 0F B6 04 0B                  movzx eax, byte ptr [rbx + r9]
008B6B63  49 83 E9 01                     sub r9, 1
008B6B67  41 88 04 1A                     mov byte ptr [r10 + rbx], al
008B6B6B  45 8D 52 FF                     lea r10d, [r10 - 1]
008B6B6F  0F 88 F7 FB FF FF               js 0x1408b676c
008B6B75  EB E7                           jmp 0x1408b6b5e
008B6B77  33 D2                           xor edx, edx
008B6B79  49 8B C3                        mov rax, r11
008B6B7C  E8 4F 3F E0 FF                  call 0x1406baad0
008B6B81  EB A7                           jmp 0x1408b6b2a
008B6B83  3C 04                           cmp al, 4
008B6B85  0F 86 AC 00 00 00               jbe 0x1408b6c37
008B6B8B  3C 08                           cmp al, 8
008B6B8D  76 74                           jbe 0x1408b6c03
008B6B8F  66 41 83 79 02 00               cmp word ptr [r9 + 2], 0
008B6B95  0F 85 26 FE FF FF               jne 0x1408b69c1
008B6B9B  33 D2                           xor edx, edx
008B6B9D  49 8B CD                        mov rcx, r13
008B6BA0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B6BA5  E8 C6 BC 2C 00                  call 0x140b82870
008B6BAA  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6BAE  E9 BA F9 FF FF                  jmp 0x1408b656d
008B6BB3  41 F6 45 EA 02                  test byte ptr [r13 - 0x16], 2
008B6BB8  0F 84 16 F9 FF FF               je 0x1408b64d4
008B6BBE  E9 62 FE FF FF                  jmp 0x1408b6a25
008B6BC3  33 D2                           xor edx, edx
008B6BC5  48 8B CF                        mov rcx, rdi
008B6BC8  E8 A3 BC 2C 00                  call 0x140b82870
008B6BCD  45 32 F6                        xor r14b, r14b
008B6BD0  49 8B FC                        mov rdi, r12
008B6BD3  E9 6B F9 FF FF                  jmp 0x1408b6543
008B6BD8  48 8D 15 A1 CE FB FF            lea rdx, [rip - 0x4315f]
008B6BDF  48 3B C2                        cmp rax, rdx
008B6BE2  BA 01 00 00 00                  mov edx, 1
008B6BE7  0F 85 FF 00 00 00               jne 0x1408b6cec
008B6BED  48 8D 45 BB                     lea rax, [rbp - 0x45]
008B6BF1  49 8B CD                        mov rcx, r13
008B6BF4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B6BF9  E8 82 CE FB FF                  call 0x140873a80
008B6BFE  E9 28 F9 FF FF                  jmp 0x1408b652b
008B6C03  41 80 FE 04                     cmp r14b, 4
008B6C07  0F 83 B4 FD FF FF               jae 0x1408b69c1
008B6C0D  EB 8C                           jmp 0x1408b6b9b
008B6C0F  48 8B CE                        mov rcx, rsi
008B6C12  E8 B9 F1 9A FF                  call 0x140265dd0
008B6C17  E9 77 FD FF FF                  jmp 0x1408b6993
008B6C1C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B6C21  44 0F B6 E7                     movzx r12d, dil
008B6C25  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
008B6C29  E9 2E 01 00 00                  jmp 0x1408b6d5c
008B6C2E  48 8B 77 20                     mov rsi, qword ptr [rdi + 0x20]
008B6C32  E9 96 F9 FF FF                  jmp 0x1408b65cd
008B6C37  41 80 FE 03                     cmp r14b, 3
008B6C3B  0F 83 80 FD FF FF               jae 0x1408b69c1
008B6C41  E9 55 FF FF FF                  jmp 0x1408b6b9b
008B6C46  33 D2                           xor edx, edx
008B6C48  49 8B CD                        mov rcx, r13
008B6C4B  E8 20 BC 2C 00                  call 0x140b82870
008B6C50  E9 42 F9 FF FF                  jmp 0x1408b6597
008B6C55  48 8B CE                        mov rcx, rsi
008B6C58  E8 73 F1 9A FF                  call 0x140265dd0
008B6C5D  E9 85 FD FF FF                  jmp 0x1408b69e7
008B6C62  33 D2                           xor edx, edx
008B6C64  48 8B CF                        mov rcx, rdi
008B6C67  E8 04 BC 2C 00                  call 0x140b82870
008B6C6C  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
008B6C6F  B9 00 01 00 00                  mov ecx, 0x100
008B6C74  8B D0                           mov edx, eax
008B6C76  89 05 10 47 55 00               mov dword ptr [rip + 0x554710], eax
008B6C7C  41 B8 4F 62 53 71               mov r8d, 0x7153624f
008B6C82  E8 69 B4 2C 00                  call 0x140b820f0
008B6C87  48 8B F8                        mov rdi, rax
008B6C8A  48 85 C0                        test rax, rax
008B6C8D  0F 84 08 FC FF FF               je 0x1408b689b
008B6C93  8B 4E 64                        mov ecx, dword ptr [rsi + 0x64]
008B6C96  4C 8D 45 C7                     lea r8, [rbp - 0x39]
008B6C9A  48 8B 86 98 00 00 00            mov rax, qword ptr [rsi + 0x98]
008B6CA1  4C 8B CF                        mov r9, rdi
008B6CA4  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
008B6CA9  BA 01 00 00 00                  mov edx, 1
008B6CAE  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
008B6CB3  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
008B6CB7  48 8D 4D BB                     lea rcx, [rbp - 0x45]
008B6CBB  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008B6CC0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008B6CC5  49 8B CD                        mov rcx, r13
008B6CC8  E8 03 3E E0 FF                  call 0x1406baad0
008B6CCD  8B D8                           mov ebx, eax
008B6CCF  E9 64 F8 FF FF                  jmp 0x1408b6538
008B6CD4  33 D2                           xor edx, edx
008B6CD6  49 8B CD                        mov rcx, r13
008B6CD9  BB 23 00 00 C0                  mov ebx, 0xc0000023
008B6CDE  E8 8D BB 2C 00                  call 0x140b82870
008B6CE3  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6CE7  E9 81 F8 FF FF                  jmp 0x1408b656d
008B6CEC  48 8D 4D BB                     lea rcx, [rbp - 0x45]
008B6CF0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008B6CF5  49 8B CD                        mov rcx, r13
008B6CF8  E8 D3 3D E0 FF                  call 0x1406baad0
008B6CFD  E9 29 F8 FF FF                  jmp 0x1408b652b
008B6D02  33 D2                           xor edx, edx
008B6D04  49 8B CD                        mov rcx, r13
008B6D07  BB 77 00 00 C0                  mov ebx, 0xc0000077
008B6D0C  E8 5F BB 2C 00                  call 0x140b82870
008B6D11  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6D15  E9 53 F8 FF FF                  jmp 0x1408b656d
008B6D1A  4C 8B EF                        mov r13, rdi
008B6D1D  45 0F B6 E6                     movzx r12d, r14b
008B6D21  E9 47 F8 FF FF                  jmp 0x1408b656d
008B6D26  44 8B F9                        mov r15d, ecx
008B6D29  E9 06 F9 FF FF                  jmp 0x1408b6634
008B6D2E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008B6D33  4D 8B EE                        mov r13, r14
008B6D36  44 0F B6 E7                     movzx r12d, dil
008B6D3A  E9 2E F8 FF FF                  jmp 0x1408b656d
008B6D3F  BB 23 00 00 C0                  mov ebx, 0xc0000023
008B6D44  E9 D8 FE FF FF                  jmp 0x1408b6c21
008B6D49  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B6D4E  E9 D2 FE FF FF                  jmp 0x1408b6c25
008B6D53  BB 79 00 00 C0                  mov ebx, 0xc0000079
008B6D58  48 89 75 CF                     mov qword ptr [rbp - 0x31], rsi
008B6D5C  33 D2                           xor edx, edx
008B6D5E  49 8B CD                        mov rcx, r13
008B6D61  E8 0A BB 2C 00                  call 0x140b82870
008B6D66  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008B6D6A  E9 FE F7 FF FF                  jmp 0x1408b656d
008B6D6F  B9 0E 00 00 00                  mov ecx, 0xe
008B6D74  CD 29                           int 0x29
008B6D76  E9 6D FB FF FF                  jmp 0x1408b68e8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAppendAceToTokenObjectAcl(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m6E;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA8;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = 0;
    v_stack_m48 = a1;
    v_stack_m50 = 0;
    v_r12 = 0;
    v_stack_mA4 = 0;
    result = (a1 - 48) >> (8);
    a1 = (*(unsigned __int8 *)(a1 - 24)) ^ ((unsigned __int8)(result));
    v_stack_m40 = (unsigned __int8)(result);
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7408073));
    v_stack_m98 = 0;
    v_stack_m80 = a3;
    v_stack_m70 = v_xmm0;
    v_stack_m88 = a2;
    v_stack_m60 = v_xmm0;
    v_stack_m78 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7410543 + a1 * 8) + 152)) != (v_rip + 15881)) goto loc_008B686D;
    result = ObpReferenceSecurityDescriptor(a1 - 48, a2, a3, a4);
    v_r14 = 0;
    if (result == 0) goto loc_008B6A1B;
loc_008B64D4:
    goto loc_008B654B;
loc_008B64D9:
    v_stack_mB8 = 0;
    v_stack_mC0 = *(unsigned __int64 *)(v_rip + 7410543 + a1 * 8) + 76;
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7410543 + a1 * 8) + 100)));
    v_stack_mD0 = a1 - 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7410543 + a1 * 8) + 152)) != (v_rip - 284718)) goto loc_008B6BD8;
    v_stack_mD8 = v_stack_mA4;
    result = CmpSecurityMethod(a1, 1, v_stack_m98, result);
loc_008B652B:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008B6C62;
loc_008B6538:
    if (sign_flag) goto loc_008B6BC3;
loc_008B6543:
    if (sign_flag) goto loc_008B6561;
loc_008B654B:
    if (result == 0) goto loc_008B6597;
    if ((((unsigned __int8)(*(unsigned __int16 *)(result + 2))) & (4)) != 0) goto loc_008B65B5;
    goto loc_008B656D;
loc_008B6561:
    if (result == 0) goto loc_008B6597;
loc_008B656D:
    if (1 != 0) goto loc_008B6C46;
loc_008B6582:
    if (condition_is_less_or_equal) goto loc_008B68E2;
    if (*(unsigned __int64 *)(result - 32 + 8) - 1 != 0) goto loc_008B6582;
loc_008B6597:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008B65B5:
    if (!sign_flag) goto loc_008B6C2E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result - 32 + 16))) == 0) goto loc_008B6D1A;
loc_008B65CD:
    if (result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 == 0) goto loc_008B656D;
    a3 = 0;
    result = RtlFindAceBySid(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1, v_stack_m80, a3, result);
    if (result != 0) goto loc_008B656D;
    v_stack_mA8 = (unsigned __int8)(*(unsigned __int8 *)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1));
    result = (unsigned __int8)((*(unsigned __int8 *)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1)) - (2));
    if (((unsigned __int8)(result)) > 2) goto loc_008B68C0;
    a3 = 0;
loc_008B660A:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + 4)))) goto loc_008B68A5;
    v_r15 = result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + 8;
    if ((result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + 8) > (result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + *(unsigned __int16 *)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + 2) * 1)) { v_r15 = 0; }
    if (v_r15 == 0) goto loc_008B6D26;
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1)));
loc_008B6634:
    result = RtlLengthSid(v_stack_m80, *(unsigned __int16 *)(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1 + 4), a3, result);
    v_rbx = (unsigned int)((result + 11) + ((unsigned int)(v_r15)));
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFCULL));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x63416553ULL), result);
    if (result == 0) goto loc_008B6D2E;
    if (((unsigned int)(v_rbx)) < 8) goto loc_008B6D3F;
    result = (unsigned __int8)((v_stack_mA8) - (2));
    if (((unsigned __int8)(result)) > 2) goto loc_008B6C1C;
    if (((unsigned int)(v_rbx)) > 0xFFFCULL) goto loc_008B6C1C;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))), result);
    *(unsigned __int8 *)(result) = (unsigned __int8)(v_stack_mA8);
    a2 = 0;
    result = 0;
    *(unsigned __int8 *)(result + 1) = 0;
    *(unsigned int *)(result + 4) = 0;
    *(unsigned __int16 *)(result + 2) = (unsigned __int16)(v_rbx);
    result = RtlGetAce(result - 32 + (unsigned int)(*(unsigned int *)(result - 32 + 16)) * 1, a2, v_stack_m78, result);
    v_stack_m90 = result - 32;
    if (sign_flag) goto loc_008B6D5C;
    v_r15 = (unsigned int)((v_r15) + (-8));
    result = RtlValidAcl(result, a2, v_stack_m78, result);
    if ((unsigned __int8)(result) == 0) goto loc_008B6D49;
    v_r10 = 0;
    v_stack_m90 = result - 32;
loc_008B66FC:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B684E;
    v_r11 = (*(unsigned __int16 *)(result + 2)) + (result);
    v_stack_mA0 = 0;
    a1 = result + 8;
    if ((result + 8) > v_r11) { a1 = 0; }
    v_rdi = (unsigned int)((unsigned int)(v_stack_mA8));
    if (((unsigned __int8)(v_stack_mA8)) <= ((unsigned __int8)(*(unsigned __int8 *)(result)))) { v_rdi = (unsigned int)(*(unsigned __int8 *)(result)); }
loc_008B6739:
    if (v_stack_m78 < (v_r15 + v_stack_m78 * 1)) goto loc_008B69B5;
    if (v_stack_m78 > (v_r15 + v_stack_m78 * 1)) goto loc_008B6B9B;
    if (a1 == 0) goto loc_008B6CD4;
    if ((v_r15 + a1 * 1) > v_r11) goto loc_008B6CD4;
    a1 = (unsigned int)((a1) - ((unsigned int)(result + 8)));
    a1 = (unsigned int)((a1) - (1));
    if (!sign_flag) goto loc_008B6B5A;
loc_008B676C:
    if ((unsigned int)(v_r15) == 0) goto loc_008B6791;
    a3 = (v_stack_m78) - (result + 8);
loc_008B6780:
    *(unsigned __int8 *)(result + 8) = (unsigned __int8)(*(unsigned __int8 *)(a3 + result + 8 * 1));
    a2 = ((unsigned int)((unsigned int)(v_r15))) - (1);
    if (condition_is_not_equal) goto loc_008B6780;
loc_008B6791:
    *(unsigned __int8 *)(result) = (unsigned __int8)(v_rdi);
    if (v_stack_m80 <= ((unsigned int)(v_stack_mA0))) goto loc_008B68CA;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m80)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_008B68CA;
    if ((*(unsigned __int8 *)(v_stack_m80 + 1)) > 15) goto loc_008B68CA;
    if (((unsigned __int8)(v_rdi)) > 4) goto loc_008B6B42;
    if (((unsigned __int8)(v_rdi)) <= ((unsigned __int8)(v_stack_mA8))) {
        v_rdi = (unsigned __int8)(v_stack_mA8);
    }
    result = RtlValidAcl(result, a2, a3, (int)((unsigned int)(a1)));
    if ((unsigned __int8)(result) == 0) goto loc_008B6D02;
    v_r15 = 0;
loc_008B67FE:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(result + 4)))) goto loc_008B69FC;
    a2 = (*(unsigned __int16 *)(result + 2)) + (result);
    v_rbx = result + 8;
    if ((result + 8) > a2) { v_rbx = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_stack_m80 + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (v_rbx == 0) goto loc_008B6836;
    result = ((unsigned __int16)(a1)) + (v_rbx);
    if (result <= a2) goto loc_008B6A42;
loc_008B6836:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, (int)((unsigned int)(a1)));
    goto loc_008B656D;
loc_008B684E:
    result = (*(unsigned __int16 *)(v_stack_m90 + 2)) + (v_stack_m90);
    if (result >= result) goto loc_008B6B9B;
    a2 = (unsigned int)((a2) + 1);
    a1 = (result) + (*(unsigned __int16 *)(result + 2));
    goto loc_008B66FC;
loc_008B686D:
    v_stack_m98 = 447;
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5589785)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5589785)))), (unsigned int)(0x7153624FULL), (int)((unsigned int)(a1)));
    if (result != 0) goto loc_008B64D9;
loc_008B689B:
    goto loc_008B6597;
loc_008B68A5:
    result = (*(unsigned __int16 *)(result - 32 + 2)) + (result - 32);
    if (0 >= result) goto loc_008B68C0;
    a1 = (unsigned int)((256) + 1);
    v_r15 = (v_r15) + (*(unsigned __int16 *)(v_r15 + 2));
    goto loc_008B660A;
loc_008B68C0:
    goto loc_008B656D;
loc_008B68CA:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, (unsigned int)(0x7153624FULL), (int)((unsigned int)(a1)));
    goto loc_008B656D;
loc_008B68E2:
    if (condition_is_not_equal) goto loc_008B6D6F;
loc_008B68E8:
    a3 = 0;
    a2 = 0;
    v_rsi = ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) << (4);
    v_rsi = (v_rsi) + (v_rip + 7447997);
    result = KeAbPreAcquire(v_rsi, a2, a3, (int)((unsigned int)(a1)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rsi;
        a2 = result;
        a1 = v_rsi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (int)((unsigned int)(a1)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = (-1) - (1);
    if (condition_is_greater) goto loc_008B69D8;
    if (a1 != 0) goto loc_008B69D1;
    if ((*(unsigned __int64 *)(v_rsi + 8)) == result) goto loc_008B697E;
loc_008B6970:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) != result) goto loc_008B6970;
loc_008B697E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) = *(unsigned __int64 *)(result);
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008B6C0F;
loc_008B6993:
    result = KeAbPostRelease(v_rsi, *(unsigned __int64 *)(result), a3, (int)((unsigned int)(a1)));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(result), a3, (int)((unsigned int)(a1)));
    result = ExFreePoolWithTag(result, (unsigned int)(0x6353624FULL), a3, (int)((unsigned int)(a1)));
    goto loc_008B6597;
loc_008B69B5:
    if (((unsigned __int8)(*(unsigned __int8 *)((int)((unsigned int)(a1))))) > 3) goto loc_008B6B83;
loc_008B69C1:
    a4 = ((int)((unsigned int)(a1))) + (*(unsigned __int16 *)((int)((unsigned int)(a1)) + 2));
    goto loc_008B6739;
loc_008B69D1:
loc_008B69D8:
    result = (unsigned __int8)((*(unsigned __int16 *)((int)((unsigned int)(a1)) + 2)) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008B6C55;
loc_008B69E7:
    result = KeAbPostRelease(v_rsi, (unsigned int)(0x6353624FULL), a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x6353624FULL), a3, a4);
    goto loc_008B6597;
loc_008B69FC:
    result = (*(unsigned __int16 *)(v_stack_m90 + 2)) + (v_stack_m90);
    if (((unsigned int)(0xC0000078ULL)) >= result) goto loc_008B6D02;
    a1 = (unsigned int)((*(unsigned __int64 *)(gs_base + (0 + 392))) + 1);
    v_rbx = ((unsigned int)(0xC0000078ULL)) + (*(unsigned __int16 *)((unsigned int)(0xC0000078ULL) + 2));
    goto loc_008B67FE;
loc_008B6A1B:
    if (((*(unsigned __int8 *)(v_rsi + 66)) & (8)) == 0) goto loc_008B6BB3;
loc_008B6A25:
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeBugCheckEx(393, v_stack_m90 - 48, v_rsi, 1);
loc_008B6A42:
    *(unsigned __int16 *)(v_rbx + 2) = 393;
    *(unsigned int *)(v_rbx + 4) = (unsigned int)((unsigned int)(v_stack_m88));
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(result);
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi + 8) + 1) * 4 + 8, v_rbx + 8, *(unsigned __int64 *)(v_rsi + 8), 1);
    result = 0;
    *(unsigned __int8 *)(v_stack_m90) = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m70 = 1;
    v_stack_m60 = v_xmm0;
    if (sign_flag) goto loc_008B6D53;
    v_stack_m50 = v_stack_m90;
    result = (unsigned __int16)((v_stack_m6E) & ((unsigned __int16)((unsigned int)(0xFFF7ULL))));
    v_stack_mA0 = 4;
    result = (unsigned __int16)((result) | (4));
    v_stack_m6E = (unsigned __int16)(result);
    a2 = (*(unsigned __int8 *)(v_stack_m48 - 24)) ^ (v_stack_m40);
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7406468));
    v_stack_p40 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p38 = *(unsigned __int64 *)(v_rip + 7408942 + a2 * 8) + 76;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7408942 + a2 * 8) + 100)));
    v_stack_p28 = v_stack_m48 - 8;
    v_stack_p20 = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7408942 + a2 * 8) + 152)) != (v_rip + 14259)) goto loc_008B6B77;
    a2 = 0;
    result = SeDefaultObjectMethod(v_stack_m48, a2, v_stack_mA0, v_stack_m70);
loc_008B6B2A:
    a2 = 0;
    v_stack_m90 = v_rsi;
    result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_mA0, v_stack_m70);
    goto loc_008B656D;
loc_008B6B42:
    a2 = 0;
    result = ExFreePoolWithTag(v_rsi, a2, v_stack_mA0, v_stack_m70);
    goto loc_008B656D;
loc_008B6B5A:
loc_008B6B5E:
    a4 = (v_stack_m70) - (1);
    *(unsigned __int8 *)(v_rsi + result * 1 + (unsigned int)(0xC0000059ULL) * 1) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(0xC0000059ULL) + v_stack_m70 * 1));
    if (sign_flag) goto loc_008B676C;
    goto loc_008B6B5E;
loc_008B6B77:
    a2 = 0;
    result = guard_dispatch_icall(v_rsi, a2, v_stack_mA0, a4);
    goto loc_008B6B2A;
loc_008B6B83:
    if (((unsigned __int8)(result)) <= 4) goto loc_008B6C37;
    if (((unsigned __int8)(result)) <= 8) goto loc_008B6C03;
    if ((*(unsigned __int16 *)(a4 + 2)) != 0) goto loc_008B69C1;
loc_008B6B9B:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_mA0, a4);
    goto loc_008B656D;
loc_008B6BB3:
    if (((*(unsigned __int8 *)(v_stack_m90 - 22)) & (2)) == 0) goto loc_008B64D4;
    goto loc_008B6A25;
loc_008B6BC3:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_mA0, a4);
    v_r14 = 0;
    goto loc_008B6543;
loc_008B6BD8:
    if (result != (v_rip - 274783)) goto loc_008B6CEC;
    v_stack_p20 = v_stack_mA4;
    result = IopGetSetSecurityObject(v_stack_m90, 1, v_stack_mA0, a4);
    goto loc_008B652B;
loc_008B6C03:
    if (0 >= 4) goto loc_008B69C1;
    goto loc_008B6B9B;
loc_008B6C0F:
    result = ExfTryToWakePushLock(v_rsi, 1, v_stack_mA0, a4);
    goto loc_008B6993;
loc_008B6C1C:
loc_008B6C21:
loc_008B6C25:
    v_stack_m90 = 0;
    goto loc_008B6D5C;
loc_008B6C2E:
    goto loc_008B65CD;
loc_008B6C37:
    if (0 >= 3) goto loc_008B69C1;
    goto loc_008B6B9B;
loc_008B6C46:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_mA0, a4);
    goto loc_008B6597;
loc_008B6C55:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32), a2, v_stack_mA0, a4);
    goto loc_008B69E7;
loc_008B6C62:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_mA0, a4);
    *(unsigned int *)(v_rip + 5588752) = (unsigned int)((unsigned int)(v_stack_mA4));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA4))), (unsigned int)(0x7153624FULL), a4);
    if (result == 0) goto loc_008B689B;
    v_stack_p40 = (unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392))));
    v_stack_p38 = 0;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32) + 100)));
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mA4;
    result = guard_dispatch_icall(v_stack_m90, 1, v_stack_m98, result);
    goto loc_008B6538;
loc_008B6CD4:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6CEC:
    v_stack_p20 = v_stack_mA4;
    result = guard_dispatch_icall(v_stack_m90, a2, v_stack_m98, result);
    goto loc_008B652B;
loc_008B6D02:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6D1A:
    goto loc_008B656D;
loc_008B6D26:
    goto loc_008B6634;
loc_008B6D2E:
    goto loc_008B656D;
loc_008B6D3F:
    goto loc_008B6C21;
loc_008B6D49:
    goto loc_008B6C25;
loc_008B6D53:
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 32);
loc_008B6D5C:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6D6F:
    goto loc_008B68E8;
}
```

## 5. (Beta) C Style

```c
int64_t SepAppendAceToTokenObjectAcl(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint16_t v_stack_m6E;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA8;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = 0;
    v_stack_m48 = Arg1;
    v_stack_m50 = 0;
    local_r12 = 0;
    v_stack_mA4 = 0;
    result = (Arg1 - 48) >> (8);
    Arg1 = (*(uint8_t *)(arg1 - 0x18)) ^ ((uint8_t)(result));
    v_stack_m40 = (uint8_t)(result);
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x7109C9));
    v_stack_m98 = 0;
    v_stack_m80 = Arg3;
    v_stack_m70 = v_xmm0;
    v_stack_m88 = Arg2;
    v_stack_m60 = v_xmm0;
    v_stack_m78 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x71136F + arg1 * 8) + 0x98)) != (v_rip + 15881)) goto loc_008B686D;
    result = ObpReferenceSecurityDescriptor(Arg1 - 48, Arg2, Arg3, a4);
    local_r14 = 0;
    if (result == 0) goto loc_008B6A1B;
loc_008B64D4:
    goto loc_008B654B;
loc_008B64D9:
    v_stack_mB8 = 0;
    v_stack_mC0 = *(uint64_t *)(v_rip + 0x71136F + arg1 * 8) + 76;
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71136F + arg1 * 8) + 0x64)));
    v_stack_mD0 = Arg1 - 8;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x71136F + arg1 * 8) + 0x98)) != (v_rip - 284718)) goto loc_008B6BD8;
    v_stack_mD8 = v_stack_mA4;
    result = CmpSecurityMethod(Arg1, 1, v_stack_m98, result);
loc_008B652B:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008B6C62;
loc_008B6538:
    if (sign_flag) goto loc_008B6BC3;
loc_008B6543:
    if (sign_flag) goto loc_008B6561;
loc_008B654B:
    if (result == 0) goto loc_008B6597;
    if ((((uint8_t)(*(uint16_t *)(result + 0x2))) & (4)) != 0) goto loc_008B65B5;
    goto loc_008B656D;
loc_008B6561:
    if (result == 0) goto loc_008B6597;
loc_008B656D:
    if (1 != 0) goto loc_008B6C46;
loc_008B6582:
    if (condition_is_less_or_equal) goto loc_008B68E2;
    if (*(uint64_t *)(result - 0x20 + 0x8) - 1 != 0) goto loc_008B6582;
loc_008B6597:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008B65B5:
    if (!sign_flag) goto loc_008B6C2E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result - 0x20 + 0x10))) == 0) goto loc_008B6D1A;
loc_008B65CD:
    if (result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 == 0) goto loc_008B656D;
    Arg3 = 0;
    result = RtlFindAceBySid(result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1, v_stack_m80, Arg3, result);
    if (result != 0) goto loc_008B656D;
    v_stack_mA8 = (uint8_t)(*(uint8_t *)(result - 0x20 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1));
    result = (uint8_t)((*(uint8_t *)(result - 0x20 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1)) - (2));
    if (((uint8_t)(result)) > 2) goto loc_008B68C0;
    Arg3 = 0;
loc_008B660A:
    if (0 < ((uint32_t)(*(uint16_t *)(result - 0x20 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + 0x4)))) goto loc_008B68A5;
    local_r15 = result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + 8;
    if ((result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + 8) > (result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + *(uint16_t *)(result - 0x20 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + 0x2) * 1)) { local_r15 = 0; }
    if (local_r15 == 0) goto loc_008B6D26;
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1)));
loc_008B6634:
    result = RtlLengthSid(v_stack_m80, *(uint16_t *)(result - 0x20 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1 + 0x4), Arg3, result);
    local_rbx = (uint32_t)((result + 11) + ((uint32_t)(local_r15)));
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFCULL));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x63416553ULL), result);
    if (result == 0) goto loc_008B6D2E;
    if (((uint32_t)(local_rbx)) < 8) goto loc_008B6D3F;
    result = (uint8_t)((v_stack_mA8) - (2));
    if (((uint8_t)(result)) > 2) goto loc_008B6C1C;
    if (((uint32_t)(local_rbx)) > 0xFFFCULL) goto loc_008B6C1C;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))), result);
    *(uint8_t *)(result) = (uint8_t)(v_stack_mA8);
    Arg2 = 0;
    result = 0;
    *(uint8_t *)(result + 0x1) = 0;
    *(uint32_t *)(result + 0x4) = 0;
    *(uint16_t *)(result + 0x2) = (uint16_t)(local_rbx);
    result = RtlGetAce(result - 32 + (uint32_t)(*(uint32_t *)(result - 0x20 + 0x10)) * 1, Arg2, v_stack_m78, result);
    v_stack_m90 = result - 32;
    if (sign_flag) goto loc_008B6D5C;
    local_r15 = (uint32_t)((local_r15) + (-8));
    result = RtlValidAcl(result, Arg2, v_stack_m78, result);
    if ((uint8_t)(result) == 0) goto loc_008B6D49;
    local_r10 = 0;
    v_stack_m90 = result - 32;
loc_008B66FC:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B684E;
    local_r11 = (*(uint16_t *)(result + 0x2)) + (result);
    v_stack_mA0 = 0;
    Arg1 = result + 8;
    if ((result + 8) > local_r11) { Arg1 = 0; }
    local_rdi = (uint32_t)((uint32_t)(v_stack_mA8));
    if (((uint8_t)(v_stack_mA8)) <= ((uint8_t)(*(uint8_t *)(result)))) { local_rdi = (uint32_t)(*(uint8_t *)(result)); }
loc_008B6739:
    if (v_stack_m78 < (local_r15 + v_stack_m78 * 1)) goto loc_008B69B5;
    if (v_stack_m78 > (local_r15 + v_stack_m78 * 1)) goto loc_008B6B9B;
    if (Arg1 == NULL) goto loc_008B6CD4;
    if ((local_r15 + Arg1 * 1) > local_r11) goto loc_008B6CD4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result + 8)));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (!sign_flag) goto loc_008B6B5A;
loc_008B676C:
    if ((uint32_t)(local_r15) == 0) goto loc_008B6791;
    Arg3 = (v_stack_m78) - (result + 8);
loc_008B6780:
    *(uint8_t *)(result + 0x8) = (uint8_t)(*(uint8_t *)(Arg3 + result + 0x8 * 1));
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) - (1);
    if (condition_is_not_equal) goto loc_008B6780;
loc_008B6791:
    *(uint8_t *)(result) = (uint8_t)(local_rdi);
    if (v_stack_m80 <= ((uint32_t)(v_stack_mA0))) goto loc_008B68CA;
    result = (uint8_t)((*(uint8_t *)(v_stack_m80)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_008B68CA;
    if ((*(uint8_t *)(v_stack_m80 + 0x1)) > 15) goto loc_008B68CA;
    if (((uint8_t)(local_rdi)) > 4) goto loc_008B6B42;
    if (((uint8_t)(local_rdi)) <= ((uint8_t)(v_stack_mA8))) {
        local_rdi = (uint8_t)(v_stack_mA8);
    }
    result = RtlValidAcl(result, Arg2, Arg3, (int32_t)((uint32_t)(Arg1)));
    if ((uint8_t)(result) == 0) goto loc_008B6D02;
    local_r15 = 0;
loc_008B67FE:
    if (0 < ((uint32_t)(*(uint16_t *)(result + 0x4)))) goto loc_008B69FC;
    Arg2 = (*(uint16_t *)(result + 0x2)) + (result);
    local_rbx = result + 8;
    if ((result + 8) > Arg2) { local_rbx = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(v_stack_m80 + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (local_rbx == 0) goto loc_008B6836;
    result = ((uint16_t)(Arg1)) + (local_rbx);
    if (result <= Arg2) goto loc_008B6A42;
loc_008B6836:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, (int32_t)((uint32_t)(Arg1)));
    goto loc_008B656D;
loc_008B684E:
    result = (*(uint16_t *)(v_stack_m90 + 0x2)) + (v_stack_m90);
    if (result >= result) goto loc_008B6B9B;
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (result) + (*(uint16_t *)(result + 0x2));
    goto loc_008B66FC;
loc_008B686D:
    v_stack_m98 = 447;
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x554B19)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x554B19)))), (uint32_t)(0x7153624FULL), (int32_t)((uint32_t)(Arg1)));
    if (result != 0) goto loc_008B64D9;
loc_008B689B:
    goto loc_008B6597;
loc_008B68A5:
    result = (*(uint16_t *)(result - 0x20 + 0x2)) + (result - 32);
    if (0 >= result) goto loc_008B68C0;
    Arg1 = (uint32_t)((256) + 1);
    local_r15 = (local_r15) + (*(uint16_t *)(local_r15 + 0x2));
    goto loc_008B660A;
loc_008B68C0:
    goto loc_008B656D;
loc_008B68CA:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, (uint32_t)(0x7153624FULL), (int32_t)((uint32_t)(Arg1)));
    goto loc_008B656D;
loc_008B68E2:
    if (condition_is_not_equal) goto loc_008B6D6F;
loc_008B68E8:
    Arg3 = 0;
    Arg2 = 0;
    local_rsi = ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) << (4);
    local_rsi = (local_rsi) + (v_rip + 7447997);
    result = KeAbPreAcquire(local_rsi, Arg2, Arg3, (int32_t)((uint32_t)(Arg1)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rsi;
        Arg2 = result;
        Arg1 = local_rsi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (int32_t)((uint32_t)(Arg1)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = (-1) - (1);
    if (condition_is_greater) goto loc_008B69D8;
    if (Arg1 != NULL) goto loc_008B69D1;
    if ((*(uint64_t *)(local_rsi + 0x8)) == result) goto loc_008B697E;
loc_008B6970:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) != result) goto loc_008B6970;
loc_008B697E:
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) = *(uint64_t *)(result);
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008B6C0F;
loc_008B6993:
    result = KeAbPostRelease(local_rsi, *(uint64_t *)(result), Arg3, (int32_t)((uint32_t)(Arg1)));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(result), Arg3, (int32_t)((uint32_t)(Arg1)));
    result = ExFreePoolWithTag(result, (uint32_t)(0x6353624FULL), Arg3, (int32_t)((uint32_t)(Arg1)));
    goto loc_008B6597;
loc_008B69B5:
    if (((uint8_t)(*(uint8_t *)((int32_t)((uint32_t)(arg1))))) > 3) goto loc_008B6B83;
loc_008B69C1:
    a4 = ((int32_t)((uint32_t)(Arg1))) + (*(uint16_t *)((int32_t)((uint32_t)(arg1)) + 0x2));
    goto loc_008B6739;
loc_008B69D1:
loc_008B69D8:
    result = (uint8_t)((*(uint16_t *)((int32_t)((uint32_t)(arg1)) + 0x2)) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008B6C55;
loc_008B69E7:
    result = KeAbPostRelease(local_rsi, (uint32_t)(0x6353624FULL), Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x6353624FULL), Arg3, a4);
    goto loc_008B6597;
loc_008B69FC:
    result = (*(uint16_t *)(v_stack_m90 + 0x2)) + (v_stack_m90);
    if (((uint32_t)(0xC0000078ULL)) >= result) goto loc_008B6D02;
    Arg1 = (uint32_t)((*(uint64_t *)(gs_base + (0 + 0x188))) + 1);
    local_rbx = ((uint32_t)(0xC0000078ULL)) + (*(uint16_t *)((uint32_t)(0xC0000078ULL) + 0x2));
    goto loc_008B67FE;
loc_008B6A1B:
    if (((*(uint8_t *)(local_rsi + 0x42)) & (8)) == 0) goto loc_008B6BB3;
loc_008B6A25:
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeBugCheckEx(393, v_stack_m90 - 48, local_rsi, 1);
loc_008B6A42:
    *(uint16_t *)(local_rbx + 0x2) = 393;
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)((uint32_t)(v_stack_m88));
    *(uint16_t *)(local_rbx) = (uint16_t)(result);
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x1) * 4 + 8, local_rbx + 8, *(uint64_t *)(local_rsi + 0x8), 1);
    result = 0;
    *(uint8_t *)(v_stack_m90) = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m70 = 1;
    v_stack_m60 = v_xmm0;
    if (sign_flag) goto loc_008B6D53;
    v_stack_m50 = v_stack_m90;
    result = (uint16_t)((v_stack_m6E) & ((uint16_t)((uint32_t)(0xFFF7ULL))));
    v_stack_mA0 = 4;
    result = (uint16_t)((result) | (4));
    v_stack_m6E = (uint16_t)(result);
    Arg2 = (*(uint8_t *)(v_stack_m48 - 0x18)) ^ (v_stack_m40);
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x710384));
    v_stack_p40 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p38 = *(uint64_t *)(v_rip + 0x710D2E + Arg2 * 8) + 76;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x710D2E + Arg2 * 8) + 0x64)));
    v_stack_p28 = v_stack_m48 - 8;
    v_stack_p20 = result;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x710D2E + Arg2 * 8) + 0x98)) != (v_rip + 14259)) goto loc_008B6B77;
    Arg2 = 0;
    result = SeDefaultObjectMethod(v_stack_m48, Arg2, v_stack_mA0, v_stack_m70);
loc_008B6B2A:
    Arg2 = 0;
    v_stack_m90 = local_rsi;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_mA0, v_stack_m70);
    goto loc_008B656D;
loc_008B6B42:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rsi, Arg2, v_stack_mA0, v_stack_m70);
    goto loc_008B656D;
loc_008B6B5A:
loc_008B6B5E:
    a4 = (v_stack_m70) - (1);
    *(uint8_t *)(local_rsi + result * 1 + (uint32_t)(0xC0000059ULL) * 1) = (uint8_t)(*(uint8_t *)((uint32_t)(0xC0000059ULL) + v_stack_m70 * 1));
    if (sign_flag) goto loc_008B676C;
    goto loc_008B6B5E;
loc_008B6B77:
    Arg2 = 0;
    result = guard_dispatch_icall(local_rsi, Arg2, v_stack_mA0, a4);
    goto loc_008B6B2A;
loc_008B6B83:
    if (((uint8_t)(result)) <= 4) goto loc_008B6C37;
    if (((uint8_t)(result)) <= 8) goto loc_008B6C03;
    if ((*(uint16_t *)(a4 + 0x2)) != 0) goto loc_008B69C1;
loc_008B6B9B:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_mA0, a4);
    goto loc_008B656D;
loc_008B6BB3:
    if (((*(uint8_t *)(v_stack_m90 - 0x16)) & (2)) == 0) goto loc_008B64D4;
    goto loc_008B6A25;
loc_008B6BC3:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_mA0, a4);
    local_r14 = 0;
    goto loc_008B6543;
loc_008B6BD8:
    if (result != (v_rip - 274783)) goto loc_008B6CEC;
    v_stack_p20 = v_stack_mA4;
    result = IopGetSetSecurityObject(v_stack_m90, 1, v_stack_mA0, a4);
    goto loc_008B652B;
loc_008B6C03:
    if (0 >= 4) goto loc_008B69C1;
    goto loc_008B6B9B;
loc_008B6C0F:
    result = ExfTryToWakePushLock(local_rsi, 1, v_stack_mA0, a4);
    goto loc_008B6993;
loc_008B6C1C:
loc_008B6C21:
loc_008B6C25:
    v_stack_m90 = 0;
    goto loc_008B6D5C;
loc_008B6C2E:
    goto loc_008B65CD;
loc_008B6C37:
    if (0 >= 3) goto loc_008B69C1;
    goto loc_008B6B9B;
loc_008B6C46:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_mA0, a4);
    goto loc_008B6597;
loc_008B6C55:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20), Arg2, v_stack_mA0, a4);
    goto loc_008B69E7;
loc_008B6C62:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_mA0, a4);
    *(uint32_t *)(v_rip + 0x554710) = (uint32_t)((uint32_t)(v_stack_mA4));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA4))), (uint32_t)(0x7153624FULL), a4);
    if (result == 0) goto loc_008B689B;
    v_stack_p40 = (uint8_t)((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188))));
    v_stack_p38 = 0;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20) + 0x64)));
    v_stack_p28 = result;
    v_stack_p20 = v_stack_mA4;
    result = guard_dispatch_icall(v_stack_m90, 1, v_stack_m98, result);
    goto loc_008B6538;
loc_008B6CD4:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6CEC:
    v_stack_p20 = v_stack_mA4;
    result = guard_dispatch_icall(v_stack_m90, Arg2, v_stack_m98, result);
    goto loc_008B652B;
loc_008B6D02:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6D1A:
    goto loc_008B656D;
loc_008B6D26:
    goto loc_008B6634;
loc_008B6D2E:
    goto loc_008B656D;
loc_008B6D3F:
    goto loc_008B6C21;
loc_008B6D49:
    goto loc_008B6C25;
loc_008B6D53:
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x20);
loc_008B6D5C:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, v_stack_m98, result);
    goto loc_008B656D;
loc_008B6D6F:
    goto loc_008B68E8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x18` | `8` | `R` |
| `Arg1` | `- 0x16` | `8` | `R` |
| `Arg1` | `- 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B6430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
