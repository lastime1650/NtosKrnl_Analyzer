# FsRtlCheckOplockEx2

- RVA: `0x003F2BC0`–`0x003F36B8` (길이 `2,808` bytes)
- VA: `0x00000001403F2BC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097084`
- 디코드: `626`개 명령, `2,808/2,808` bytes 표시
- 미해석 바이트: `16` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003F2CAD` → [ExAcquireFastMutexUnsafe](ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x003F2CC5` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x003F2CD2` → [Feature_3528882490__private_IsEnabledDeviceUsageNoInline](../58/Feature_3528882490__private_IsEnabledDeviceUsageNoInline_function_00581CDC.md) (function, `0x00581CDC`)
- `0x003F2D34` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x003F2D79` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F2D82` → [FsRtlpSyncWithAckTimeout](../4F/FsRtlpSyncWithAckTimeout_function_004F23C4.md) (function, `0x004F23C4`)
- `0x003F2D8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003F2D94` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x003F2D9C` → [FsRtlpReleaseIrpsWaitingForRH](../42/FsRtlpReleaseIrpsWaitingForRH_function_00425CBC.md) (function, `0x00425CBC`)
- `0x003F2DA8` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x003F2DEE` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x003F2E33` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x003F2E71` → [FsRtlpAttachOplockKey](../41/FsRtlpAttachOplockKey_function_0041DD70.md) (function, `0x0041DD70`)
- `0x003F2E89` → [FsRtlpOplockStoreKeyForDeleteOperation](FsRtlpOplockStoreKeyForDeleteOperation_function_003F2A90.md) (function, `0x003F2A90`)
- `0x003F2FDA` → [ExAcquireFastMutexUnsafe](ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x003F30F9` → [FsRtlpOplockCleanup](../42/FsRtlpOplockCleanup_function_00425030.md) (function, `0x00425030`)
- `0x003F31ED` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x003F329A` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F332A` → [FsRtlpOplockBreakToII](../4B/FsRtlpOplockBreakToII_function_004BB824.md) (function, `0x004BB824`)
- `0x003F33BB` → [FsRtlGetMarkHandleInfo](../58/FsRtlGetMarkHandleInfo_function_00581E5C.md) (function, `0x00581E5C`)
- `0x003F3434` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F34C4` → [FsRtlpOplockBreakToNone](../4F/FsRtlpOplockBreakToNone_function_004F8354.md) (function, `0x004F8354`)
- `0x003F358B` → [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) (function, `0x004E4990`)
- `0x003F35C6` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x003F35F4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlCheckOplockEx](FsRtlCheckOplockEx_function_003F2960.md) at `0x003F2997`
- [FsRtlCheckOplock](FsRtlCheckOplock_function_003F29B0.md) at `0x003F2A5E`

### Static image references
- `0x003F2BD3` → RVA `0x00E0A740` (`.data`; read)
- `0x003F2EE8` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003F3124` → RVA `0x00E06C50` (`.data`; read)
- `0x003F31DF` → RVA `0x000458EF` (`.rdata`; read)
- `0x003F361F` → RVA `0x723F7557` (`image boundary/outside`; read/write)
- `0x003F366F` → RVA `0x4F3F75A7` (`image boundary/outside`; read/write)
- `0x003F3681` → RVA `0x05443B88` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003F2D8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F2BC0  40 53                           push rbx
003F2BC2  56                              push rsi
003F2BC3  57                              push rdi
003F2BC4  41 54                           push r12
003F2BC6  41 55                           push r13
003F2BC8  41 56                           push r14
003F2BCA  41 57                           push r15
003F2BCC  48 81 EC 60 01 00 00            sub rsp, 0x160
003F2BD3  48 8B 05 66 7B A1 00            mov rax, qword ptr [rip + 0xa17b66]
003F2BDA  48 33 C4                        xor rax, rsp
003F2BDD  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
003F2BE5  44 89 8C 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r9d
003F2BED  41 8B F0                        mov esi, r8d
003F2BF0  44 89 84 24 90 00 00 00         mov dword ptr [rsp + 0x90], r8d
003F2BF8  4C 8B FA                        mov r15, rdx
003F2BFB  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
003F2C03  48 8B F9                        mov rdi, rcx
003F2C06  44 89 84 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r8d
003F2C0E  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
003F2C16  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
003F2C1E  48 8B 84 24 C8 01 00 00         mov rax, qword ptr [rsp + 0x1c8]
003F2C26  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
003F2C2E  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
003F2C36  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
003F2C3E  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
003F2C46  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
003F2C4E  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
003F2C56  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
003F2C5E  45 33 F6                        xor r14d, r14d
003F2C61  45 8B E6                        mov r12d, r14d
003F2C64  44 89 B4 24 94 00 00 00         mov dword ptr [rsp + 0x94], r14d
003F2C6C  48 8B 19                        mov rbx, qword ptr [rcx]
003F2C6F  45 85 C9                        test r9d, r9d
003F2C72  74 0A                           je 0x1403f2c7e
003F2C74  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F2C79  E9 6B 09 00 00                  jmp 0x1403f35e9
003F2C7E  4C 8B AA B8 00 00 00            mov r13, qword ptr [rdx + 0xb8]
003F2C85  40 F6 C6 04                     test sil, 4
003F2C89  0F 84 D9 01 00 00               je 0x1403f2e68
003F2C8F  49 8B FE                        mov rdi, r14
003F2C92  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
003F2C9A  48 85 DB                        test rbx, rbx
003F2C9D  75 07                           jne 0x1403f2ca6
003F2C9F  33 C0                           xor eax, eax
003F2CA1  E9 43 09 00 00                  jmp 0x1403f35e9
003F2CA6  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
003F2CAD  E8 6E 0A 00 00                  call 0x1403f3720
003F2CB2  41 38 7D 00                     cmp byte ptr [r13], dil
003F2CB6  74 1A                           je 0x1403f2cd2
003F2CB8  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
003F2CBE  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
003F2CC5  E8 D6 D6 E5 FF                  call 0x1402503a0
003F2CCA  41 8B C6                        mov eax, r14d
003F2CCD  E9 17 09 00 00                  jmp 0x1403f35e9
003F2CD2  E8 05 F0 18 00                  call 0x140581cdc
003F2CD7  8B 8B 90 00 00 00               mov ecx, dword ptr [rbx + 0x90]
003F2CDD  81 E1 00 00 01 00               and ecx, 0x10000
003F2CE3  85 C0                           test eax, eax
003F2CE5  0F 84 0A 01 00 00               je 0x1403f2df5
003F2CEB  85 C9                           test ecx, ecx
003F2CED  0F 84 C2 00 00 00               je 0x1403f2db5
003F2CF3  49 8B 55 30                     mov rdx, qword ptr [r13 + 0x30]
003F2CF7  45 32 C0                        xor r8b, r8b
003F2CFA  4C 8D 4B 78                     lea r9, [rbx + 0x78]
003F2CFE  49 8B 01                        mov rax, qword ptr [r9]
003F2D01  49 3B C1                        cmp rax, r9
003F2D04  74 22                           je 0x1403f2d28
003F2D06  48 8D 48 C8                     lea rcx, [rax - 0x38]
003F2D0A  48 3B 51 18                     cmp rdx, qword ptr [rcx + 0x18]
003F2D0E  74 0A                           je 0x1403f2d1a
003F2D10  48 8B 00                        mov rax, qword ptr [rax]
003F2D13  49 3B C1                        cmp rax, r9
003F2D16  75 EE                           jne 0x1403f2d06
003F2D18  EB 0E                           jmp 0x1403f2d28
003F2D1A  41 B0 01                        mov r8b, 1
003F2D1D  48 8B F9                        mov rdi, rcx
003F2D20  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
003F2D28  45 84 C0                        test r8b, r8b
003F2D2B  0F 84 84 00 00 00               je 0x1403f2db5
003F2D31  48 8B CF                        mov rcx, rdi
003F2D34  E8 C3 2B 03 00                  call 0x1404258fc
003F2D39  4C 8D 57 38                     lea r10, [rdi + 0x38]
003F2D3D  49 8B 0A                        mov rcx, qword ptr [r10]
003F2D40  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
003F2D44  4C 39 51 08                     cmp qword ptr [rcx + 8], r10
003F2D48  0F 85 13 01 00 00               jne 0x1403f2e61
003F2D4E  4C 39 10                        cmp qword ptr [rax], r10
003F2D51  0F 85 0A 01 00 00               jne 0x1403f2e61
003F2D57  48 89 08                        mov qword ptr [rax], rcx
003F2D5A  48 89 41 08                     mov qword ptr [rcx + 8], rax
003F2D5E  4D 39 09                        cmp qword ptr [r9], r9
003F2D61  75 0A                           jne 0x1403f2d6d
003F2D63  81 A3 90 00 00 00 FF FF FC FF   and dword ptr [rbx + 0x90], 0xfffcffff
003F2D6D  4C 39 67 28                     cmp qword ptr [rdi + 0x28], r12
003F2D71  74 0B                           je 0x1403f2d7e
003F2D73  48 8B D7                        mov rdx, rdi
003F2D76  48 8B CB                        mov rcx, rbx
003F2D79  E8 6A 2E E7 FF                  call 0x140265be8
003F2D7E  48 8D 4F 58                     lea rcx, [rdi + 0x58]
003F2D82  E8 3D F6 0F 00                  call 0x1404f23c4
003F2D87  33 D2                           xor edx, edx
003F2D89  48 8B CF                        mov rcx, rdi
003F2D8C  E8 DF FA 78 00                  call 0x140b82870
003F2D91  48 8B CB                        mov rcx, rbx
003F2D94  E8 53 29 03 00                  call 0x1404256ec
003F2D99  48 8B CB                        mov rcx, rbx
003F2D9C  E8 1B 2F 03 00                  call 0x140425cbc
003F2DA1  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
003F2DA8  E8 F3 D5 E5 FF                  call 0x1402503a0
003F2DAD  41 8B C6                        mov eax, r14d
003F2DB0  E9 34 08 00 00                  jmp 0x1403f35e9
003F2DB5  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F2DBB  84 C0                           test al, al
003F2DBD  79 E2                           jns 0x1403f2da1
003F2DBF  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F2DC3  48 39 43 08                     cmp qword ptr [rbx + 8], rax
003F2DC7  75 D8                           jne 0x1403f2da1
003F2DC9  4C 89 73 08                     mov qword ptr [rbx + 8], r14
003F2DCD  4C 89 33                        mov qword ptr [rbx], r14
003F2DD0  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F2DD6  83 E0 20                        and eax, 0x20
003F2DD9  83 C8 01                        or eax, 1
003F2DDC  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
003F2DE2  48 8D 7B 58                     lea rdi, [rbx + 0x58]
003F2DE6  48 8B 0F                        mov rcx, qword ptr [rdi]
003F2DE9  48 3B CF                        cmp rcx, rdi
003F2DEC  74 B3                           je 0x1403f2da1
003F2DEE  E8 CD 31 03 00                  call 0x140425fc0
003F2DF3  EB F1                           jmp 0x1403f2de6
003F2DF5  85 C9                           test ecx, ecx
003F2DF7  74 A8                           je 0x1403f2da1
003F2DF9  4D 8B 45 30                     mov r8, qword ptr [r13 + 0x30]
003F2DFD  45 32 C9                        xor r9b, r9b
003F2E00  48 8D 53 78                     lea rdx, [rbx + 0x78]
003F2E04  48 8B 02                        mov rax, qword ptr [rdx]
003F2E07  48 3B C2                        cmp rax, rdx
003F2E0A  74 1B                           je 0x1403f2e27
003F2E0C  0F 1F 40 00                     nop dword ptr [rax]
003F2E10  4C 3B 40 E0                     cmp r8, qword ptr [rax - 0x20]
003F2E14  74 0A                           je 0x1403f2e20
003F2E16  48 8B 00                        mov rax, qword ptr [rax]
003F2E19  48 3B C2                        cmp rax, rdx
003F2E1C  75 F2                           jne 0x1403f2e10
003F2E1E  EB 07                           jmp 0x1403f2e27
003F2E20  41 B1 01                        mov r9b, 1
003F2E23  48 8D 78 C8                     lea rdi, [rax - 0x38]
003F2E27  45 84 C9                        test r9b, r9b
003F2E2A  0F 84 71 FF FF FF               je 0x1403f2da1
003F2E30  48 8B CF                        mov rcx, rdi
003F2E33  E8 C4 2A 03 00                  call 0x1404258fc
003F2E38  4C 8D 4F 38                     lea r9, [rdi + 0x38]
003F2E3C  49 8B 09                        mov rcx, qword ptr [r9]
003F2E3F  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
003F2E43  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
003F2E47  75 18                           jne 0x1403f2e61
003F2E49  4C 39 08                        cmp qword ptr [rax], r9
003F2E4C  75 13                           jne 0x1403f2e61
003F2E4E  48 89 08                        mov qword ptr [rax], rcx
003F2E51  48 89 41 08                     mov qword ptr [rcx + 8], rax
003F2E55  48 8D 43 78                     lea rax, [rbx + 0x78]
003F2E59  48 39 00                        cmp qword ptr [rax], rax
003F2E5C  E9 00 FF FF FF                  jmp 0x1403f2d61
003F2E61  B9 03 00 00 00                  mov ecx, 3
003F2E66  CD 29                           int 0x29
003F2E68  0F BA E6 1C                     bt esi, 0x1c
003F2E6C  72 12                           jb 0x1403f2e80
003F2E6E  49 8B CF                        mov rcx, r15
003F2E71  E8 FA AE 02 00                  call 0x14041dd70
003F2E76  44 8B E0                        mov r12d, eax
003F2E79  89 84 24 94 00 00 00            mov dword ptr [rsp + 0x94], eax
003F2E80  44 8B C6                        mov r8d, esi
003F2E83  49 8B D7                        mov rdx, r15
003F2E86  48 8B CF                        mov rcx, rdi
003F2E89  E8 02 FC FF FF                  call 0x1403f2a90
003F2E8E  48 8B 0F                        mov rcx, qword ptr [rdi]
003F2E91  48 3B D9                        cmp rbx, rcx
003F2E94  48 0F 45 D9                     cmovne rbx, rcx
003F2E98  48 89 9C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbx
003F2EA0  40 F6 C6 02                     test sil, 2
003F2EA4  0F 85 3C 07 00 00               jne 0x1403f35e6
003F2EAA  48 85 DB                        test rbx, rbx
003F2EAD  0F 84 33 07 00 00               je 0x1403f35e6
003F2EB3  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
003F2EB7  A8 02                           test al, 2
003F2EB9  0F 85 27 07 00 00               jne 0x1403f35e6
003F2EBF  45 85 E4                        test r12d, r12d
003F2EC2  0F 85 1E 07 00 00               jne 0x1403f35e6
003F2EC8  8B C6                           mov eax, esi
003F2ECA  C1 E8 1D                        shr eax, 0x1d
003F2ECD  24 01                           and al, 1
003F2ECF  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
003F2ED6  40 B7 01                        mov dil, 1
003F2ED9  89 BC 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edi
003F2EE0  40 88 BC 24 82 00 00 00         mov byte ptr [rsp + 0x82], dil
003F2EE8  4C 8D 05 11 D1 C0 FF            lea r8, [rip - 0x3f2eef]
003F2EEF  45 8D 4C 24 01                  lea r9d, [r12 + 1]
003F2EF4  C6 84 24 84 00 00 00 00         mov byte ptr [rsp + 0x84], 0
003F2EFC  40 F6 C6 10                     test sil, 0x10
003F2F00  0F 85 BA 00 00 00               jne 0x1403f2fc0
003F2F06  80 BC 24 80 00 00 00 00         cmp byte ptr [rsp + 0x80], 0
003F2F0E  0F 85 AC 00 00 00               jne 0x1403f2fc0
003F2F14  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F2F1A  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
003F2F21  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003F2F25  41 0F B6 4D 00                  movzx ecx, byte ptr [r13]
003F2F2A  8B 84 24 8C 00 00 00            mov eax, dword ptr [rsp + 0x8c]
003F2F31  80 F9 03                        cmp cl, 3
003F2F34  75 1B                           jne 0x1403f2f51
003F2F36  A9 FE 4F FF FF                  test eax, 0xffff4ffe
003F2F3B  0F B6 BC 24 82 00 00 00         movzx edi, byte ptr [rsp + 0x82]
003F2F43  41 0F 44 FE                     cmove edi, r14d
003F2F47  40 88 BC 24 82 00 00 00         mov byte ptr [rsp + 0x82], dil
003F2F4F  EB 08                           jmp 0x1403f2f59
003F2F51  0F B6 BC 24 82 00 00 00         movzx edi, byte ptr [rsp + 0x82]
003F2F59  89 BC 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edi
003F2F60  80 F9 04                        cmp cl, 4
003F2F63  75 1E                           jne 0x1403f2f83
003F2F65  A9 FE DF FF FF                  test eax, 0xffffdffe
003F2F6A  40 0F B6 C7                     movzx eax, dil
003F2F6E  41 0F 44 C6                     cmove eax, r14d
003F2F72  0F B6 F8                        movzx edi, al
003F2F75  89 BC 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edi
003F2F7C  88 84 24 82 00 00 00            mov byte ptr [rsp + 0x82], al
003F2F83  40 F6 C6 08                     test sil, 8
003F2F87  75 2F                           jne 0x1403f2fb8
003F2F89  80 F9 12                        cmp cl, 0x12
003F2F8C  74 2A                           je 0x1403f2fb8
003F2F8E  48 85 D2                        test rdx, rdx
003F2F91  74 25                           je 0x1403f2fb8
003F2F93  49 3B 55 30                     cmp rdx, qword ptr [r13 + 0x30]
003F2F97  75 1F                           jne 0x1403f2fb8
003F2F99  40 32 FF                        xor dil, dil
003F2F9C  89 BC 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edi
003F2FA3  40 88 BC 24 82 00 00 00         mov byte ptr [rsp + 0x82], dil
003F2FAB  44 8B A4 24 94 00 00 00         mov r12d, dword ptr [rsp + 0x94]
003F2FB3  E9 F7 05 00 00                  jmp 0x1403f35af
003F2FB8  44 8B A4 24 94 00 00 00         mov r12d, dword ptr [rsp + 0x94]
003F2FC0  40 84 FF                        test dil, dil
003F2FC3  0F 84 E6 05 00 00               je 0x1403f35af
003F2FC9  80 BC 24 80 00 00 00 00         cmp byte ptr [rsp + 0x80], 0
003F2FD1  75 19                           jne 0x1403f2fec
003F2FD3  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
003F2FDA  E8 41 07 00 00                  call 0x1403f3720
003F2FDF  4C 8D 05 1A D0 C0 FF            lea r8, [rip - 0x3f2fe6]
003F2FE6  41 B9 01 00 00 00               mov r9d, 1
003F2FEC  C6 84 24 80 00 00 00 01         mov byte ptr [rsp + 0x80], 1
003F2FF4  8B B3 90 00 00 00               mov esi, dword ptr [rbx + 0x90]
003F2FFA  83 FE 01                        cmp esi, 1
003F2FFD  0F 84 99 05 00 00               je 0x1403f359c
003F3003  45 32 FF                        xor r15b, r15b
003F3006  44 88 BC 24 83 00 00 00         mov byte ptr [rsp + 0x83], r15b
003F300E  45 32 F6                        xor r14b, r14b
003F3011  44 88 B4 24 81 00 00 00         mov byte ptr [rsp + 0x81], r14b
003F3019  33 FF                           xor edi, edi
003F301B  89 BC 24 88 00 00 00            mov dword ptr [rsp + 0x88], edi
003F3022  F6 84 24 90 00 00 00 10         test byte ptr [rsp + 0x90], 0x10
003F302A  74 0A                           je 0x1403f3036
003F302C  BF 00 50 00 00                  mov edi, 0x5000
003F3031  E9 35 02 00 00                  jmp 0x1403f326b
003F3036  41 0F B6 45 00                  movzx eax, byte ptr [r13]
003F303B  83 F8 15                        cmp eax, 0x15
003F303E  0F 87 2E 02 00 00               ja 0x1403f3272
003F3044  41 8B 8C 80 10 36 3F 00         mov ecx, dword ptr [r8 + rax*4 + 0x3f3610]
003F304C  49 03 C8                        add rcx, r8
003F304F  FF E1                           jmp rcx
003F3051  CC                              int3
003F3052  CC                              int3
003F3053  CC                              int3
003F3054  CC                              int3
003F3055  F7 C6 00 70 00 00               test esi, 0x7000
003F305B  74 0D                           je 0x1403f306a
003F305D  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
003F3061  F7 40 10 7F FE ED FF            test dword ptr [rax + 0x10], 0xffedfe7f
003F3068  75 21                           jne 0x1403f308b
003F306A  40 F6 C6 1E                     test sil, 0x1e
003F306E  74 0D                           je 0x1403f307d
003F3070  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
003F3074  F7 40 10 7F FE EF FF            test dword ptr [rax + 0x10], 0xffeffe7f
003F307B  75 0E                           jne 0x1403f308b
003F307D  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
003F3081  0F BA E0 14                     bt eax, 0x14
003F3085  0F 83 E7 01 00 00               jae 0x1403f3272
003F308B  40 F6 C6 08                     test sil, 8
003F308F  74 1A                           je 0x1403f30ab
003F3091  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
003F3095  F7 40 10 56 FE ED FF            test dword ptr [rax + 0x10], 0xffedfe56
003F309C  75 0D                           jne 0x1403f30ab
003F309E  41 0F B6 45 1A                  movzx eax, byte ptr [r13 + 0x1a]
003F30A3  A8 01                           test al, 1
003F30A5  0F 85 C7 01 00 00               jne 0x1403f3272
003F30AB  41 0F B6 45 13                  movzx eax, byte ptr [r13 + 0x13]
003F30B0  A8 FA                           test al, 0xfa
003F30B2  75 08                           jne 0x1403f30bc
003F30B4  3C 01                           cmp al, 1
003F30B6  0F 85 59 01 00 00               jne 0x1403f3215
003F30BC  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
003F30C0  0F BA E0 14                     bt eax, 0x14
003F30C4  0F 82 4B 01 00 00               jb 0x1403f3215
003F30CA  41 B7 01                        mov r15b, 1
003F30CD  44 88 BC 24 83 00 00 00         mov byte ptr [rsp + 0x83], r15b
003F30D5  BF 00 40 00 00                  mov edi, 0x4000
003F30DA  E9 8C 01 00 00                  jmp 0x1403f326b
003F30DF  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F30E3  F7 40 50 00 40 00 00            test dword ptr [rax + 0x50], 0x4000
003F30EA  0F 85 82 01 00 00               jne 0x1403f3272
003F30F0  45 33 C0                        xor r8d, r8d
003F30F3  49 8B D5                        mov rdx, r13
003F30F6  48 8B CB                        mov rcx, rbx
003F30F9  E8 32 1F 03 00                  call 0x140425030
003F30FE  41 80 7D 00 12                  cmp byte ptr [r13], 0x12
003F3103  0F 85 69 01 00 00               jne 0x1403f3272
003F3109  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
003F3110  A8 20                           test al, 0x20
003F3112  0F 84 5A 01 00 00               je 0x1403f3272
003F3118  BF 00 20 00 00                  mov edi, 0x2000
003F311D  89 BC 24 88 00 00 00            mov dword ptr [rsp + 0x88], edi
003F3124  83 3D 25 3B A1 00 05            cmp dword ptr [rip + 0xa13b25], 5
003F312B  0F 86 41 01 00 00               jbe 0x1403f3272
003F3131  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
003F3138  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
003F3140  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
003F3148  48 C7 84 24 18 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x118], 4
003F3154  89 BC 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], edi
003F315B  48 8D 84 24 B4 00 00 00         lea rax, [rsp + 0xb4]
003F3163  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
003F316B  48 C7 84 24 28 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x128], 4
003F3177  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
003F317F  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
003F3187  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
003F318F  48 C7 84 24 38 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x138], 8
003F319B  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F31A1  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
003F31A8  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
003F31B0  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
003F31B8  48 C7 84 24 48 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x148], 4
003F31C4  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
003F31CC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F31D1  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
003F31D9  45 33 C9                        xor r9d, r9d
003F31DC  45 33 C0                        xor r8d, r8d
003F31DF  48 8D 15 09 27 C5 FF            lea rdx, [rip - 0x3ad8f7]
003F31E6  48 8D 0D 63 3A A1 00            lea rcx, [rip + 0xa13a63]
003F31ED  E8 EE 2E 03 00                  call 0x1404260e0
003F31F2  EB 7E                           jmp 0x1403f3272
003F31F4  40 F6 C6 08                     test sil, 8
003F31F8  45 0F B6 FF                     movzx r15d, r15b
003F31FC  45 0F 44 F9                     cmove r15d, r9d
003F3200  44 88 BC 24 83 00 00 00         mov byte ptr [rsp + 0x83], r15b
003F3208  BF 00 40 00 00                  mov edi, 0x4000
003F320D  EB 5C                           jmp 0x1403f326b
003F320F  40 F6 C6 08                     test sil, 8
003F3213  75 5D                           jne 0x1403f3272
003F3215  41 B6 01                        mov r14b, 1
003F3218  44 88 B4 24 81 00 00 00         mov byte ptr [rsp + 0x81], r14b
003F3220  BF 00 50 00 00                  mov edi, 0x5000
003F3225  EB 44                           jmp 0x1403f326b
003F3227  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
003F322B  83 C0 F6                        add eax, -0xa
003F322E  83 F8 37                        cmp eax, 0x37
003F3231  77 3F                           ja 0x1403f3272
003F3233  48 98                           cdqe
003F3235  41 0F B6 84 00 80 36 3F 00      movzx eax, byte ptr [r8 + rax + 0x3f3680]
003F323E  41 8B 8C 80 68 36 3F 00         mov ecx, dword ptr [r8 + rax*4 + 0x3f3668]
003F3246  49 03 C8                        add rcx, r8
003F3249  FF E1                           jmp rcx
003F324B  CC                              int3
003F324C  CC                              int3
003F324D  CC                              int3
003F324E  CC                              int3
003F324F  41 38 7D 21                     cmp byte ptr [r13 + 0x21], dil
003F3253  EB BE                           jmp 0x1403f3213
003F3255  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003F325D  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003F3261  40 38 38                        cmp byte ptr [rax], dil
003F3264  74 0C                           je 0x1403f3272
003F3266  BF 00 20 00 00                  mov edi, 0x2000
003F326B  89 BC 24 88 00 00 00            mov dword ptr [rsp + 0x88], edi
003F3272  45 84 FF                        test r15b, r15b
003F3275  0F 84 95 01 00 00               je 0x1403f3410
003F327B  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F3281  25 DF FF F0 01                  and eax, 0x1f0ffdf
003F3286  83 F8 10                        cmp eax, 0x10
003F3289  0F 84 46 02 00 00               je 0x1403f34d5
003F328F  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003F3293  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3297  45 33 C0                        xor r8d, r8d
003F329A  E8 11 F4 FF FF                  call 0x1403f26b0
003F329F  84 C0                           test al, al
003F32A1  0F 85 2E 02 00 00               jne 0x1403f34d5
003F32A7  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
003F32AF  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003F32B4  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
003F32BC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F32C1  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
003F32C9  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003F32CE  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
003F32D6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003F32DB  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
003F32E3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003F32E8  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
003F32F0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003F32F5  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
003F32FD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003F3302  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
003F330A  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003F330F  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003F3316  44 8B CE                        mov r9d, esi
003F3319  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
003F3321  4D 8B C7                        mov r8, r15
003F3324  49 8B D5                        mov rdx, r13
003F3327  48 8B CB                        mov rcx, rbx
003F332A  E8 F5 84 0C 00                  call 0x1404bb824
003F332F  44 8B E0                        mov r12d, eax
003F3332  89 84 24 94 00 00 00            mov dword ptr [rsp + 0x94], eax
003F3339  E9 AE 01 00 00                  jmp 0x1403f34ec
003F333E  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003F3346  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003F334A  8B 08                           mov ecx, dword ptr [rax]
003F334C  F6 C1 01                        test cl, 1
003F334F  E9 10 FF FF FF                  jmp 0x1403f3264
003F3354  41 8B 45 18                     mov eax, dword ptr [r13 + 0x18]
003F3358  3D 68 82 09 00                  cmp eax, 0x98268
003F335D  0F 87 8D 00 00 00               ja 0x1403f33f0
003F3363  0F 84 AC FE FF FF               je 0x1403f3215
003F3369  3D FC 00 09 00                  cmp eax, 0x900fc
003F336E  74 43                           je 0x1403f33b3
003F3370  3D 64 42 09 00                  cmp eax, 0x94264
003F3375  74 1B                           je 0x1403f3392
003F3377  3D C8 80 09 00                  cmp eax, 0x980c8
003F337C  0F 84 93 FE FF FF               je 0x1403f3215
003F3382  3D 08 82 09 00                  cmp eax, 0x98208
003F3387  0F 84 88 FE FF FF               je 0x1403f3215
003F338D  E9 E0 FE FF FF                  jmp 0x1403f3272
003F3392  40 F6 C6 08                     test sil, 8
003F3396  41 0F B6 C7                     movzx eax, r15b
003F339A  41 0F 44 C1                     cmove eax, r9d
003F339E  44 0F B6 F8                     movzx r15d, al
003F33A2  88 84 24 83 00 00 00            mov byte ptr [rsp + 0x83], al
003F33A9  BF 00 40 00 00                  mov edi, 0x4000
003F33AE  E9 B8 FE FF FF                  jmp 0x1403f326b
003F33B3  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003F33BB  E8 9C EA 18 00                  call 0x140581e5c
003F33C0  0F BA E0 0E                     bt eax, 0xe
003F33C4  0F 83 A8 FE FF FF               jae 0x1403f3272
003F33CA  BF 00 20 00 00                  mov edi, 0x2000
003F33CF  89 BC 24 88 00 00 00            mov dword ptr [rsp + 0x88], edi
003F33D6  40 F6 C6 0C                     test sil, 0xc
003F33DA  0F 84 92 FE FF FF               je 0x1403f3272
003F33E0  41 B6 01                        mov r14b, 1
003F33E3  44 88 B4 24 81 00 00 00         mov byte ptr [rsp + 0x81], r14b
003F33EB  E9 82 FE FF FF                  jmp 0x1403f3272
003F33F0  3D 44 83 09 00                  cmp eax, 0x98344
003F33F5  0F 84 1A FE FF FF               je 0x1403f3215
003F33FB  3D E8 83 09 00                  cmp eax, 0x983e8
003F3400  0F 84 0F FE FF FF               je 0x1403f3215
003F3406  3D B4 C2 09 00                  cmp eax, 0x9c2b4
003F340B  E9 03 FE FF FF                  jmp 0x1403f3213
003F3410  45 84 F6                        test r14b, r14b
003F3413  0F 84 BC 00 00 00               je 0x1403f34d5
003F3419  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F341F  25 DF FF F0 01                  and eax, 0x1f0ffdf
003F3424  83 F8 10                        cmp eax, 0x10
003F3427  74 18                           je 0x1403f3441
003F3429  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
003F342D  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3431  45 33 C0                        xor r8d, r8d
003F3434  E8 77 F2 FF FF                  call 0x1403f26b0
003F3439  84 C0                           test al, al
003F343B  0F 85 94 00 00 00               jne 0x1403f34d5
003F3441  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
003F3449  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003F344E  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
003F3456  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F345B  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
003F3463  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003F3468  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
003F3470  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003F3475  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
003F347D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003F3482  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
003F348A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003F348F  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
003F3497  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003F349C  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
003F34A4  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003F34A9  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003F34B0  44 8B CE                        mov r9d, esi
003F34B3  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
003F34BB  4D 8B C7                        mov r8, r15
003F34BE  49 8B D5                        mov rdx, r13
003F34C1  48 8B CB                        mov rcx, rbx
003F34C4  E8 8B 4E 10 00                  call 0x1404f8354
003F34C9  44 8B E0                        mov r12d, eax
003F34CC  89 84 24 94 00 00 00            mov dword ptr [rsp + 0x94], eax
003F34D3  EB 17                           jmp 0x1403f34ec
003F34D5  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003F34DC  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
003F34E4  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
003F34EC  45 85 E4                        test r12d, r12d
003F34EF  0F 85 B0 00 00 00               jne 0x1403f35a5
003F34F5  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
003F34FB  85 C7                           test edi, eax
003F34FD  0F 84 A2 00 00 00               je 0x1403f35a5
003F3503  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
003F350B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003F3510  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
003F3518  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003F351D  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
003F3525  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003F352A  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
003F3532  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003F3537  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
003F353F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F3544  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
003F354C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003F3551  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
003F3559  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003F355E  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
003F3563  45 33 F6                        xor r14d, r14d
003F3566  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
003F356B  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003F3570  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
003F3574  8B 84 24 BC 00 00 00            mov eax, dword ptr [rsp + 0xbc]
003F357B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003F357F  44 8B CE                        mov r9d, esi
003F3582  4D 8B C7                        mov r8, r15
003F3585  49 8B D5                        mov rdx, r13
003F3588  48 8B CB                        mov rcx, rbx
003F358B  E8 00 14 0F 00                  call 0x1404e4990
003F3590  44 8B E0                        mov r12d, eax
003F3593  89 84 24 94 00 00 00            mov dword ptr [rsp + 0x94], eax
003F359A  EB 0C                           jmp 0x1403f35a8
003F359C  8B B4 24 90 00 00 00            mov esi, dword ptr [rsp + 0x90]
003F35A3  EB 0A                           jmp 0x1403f35af
003F35A5  45 33 F6                        xor r14d, r14d
003F35A8  8B BC 24 8C 00 00 00            mov edi, dword ptr [rsp + 0x8c]
003F35AF  80 BC 24 80 00 00 00 00         cmp byte ptr [rsp + 0x80], 0
003F35B7  74 12                           je 0x1403f35cb
003F35B9  0F BA E6 1D                     bt esi, 0x1d
003F35BD  72 0C                           jb 0x1403f35cb
003F35BF  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
003F35C6  E8 D5 CD E5 FF                  call 0x1402503a0
003F35CB  80 BC 24 84 00 00 00 00         cmp byte ptr [rsp + 0x84], 0
003F35D3  4C 8D 05 26 CA C0 FF            lea r8, [rip - 0x3f35da]
003F35DA  41 B9 01 00 00 00               mov r9d, 1
003F35E0  0F 85 0E F9 FF FF               jne 0x1403f2ef4
003F35E6  41 8B C4                        mov eax, r12d
003F35E9  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
003F35F1  48 33 CC                        xor rcx, rsp
003F35F4  E8 47 90 2B 00                  call 0x1406ac640
003F35F9  48 81 C4 60 01 00 00            add rsp, 0x160
003F3600  41 5F                           pop r15
003F3602  41 5E                           pop r14
003F3604  41 5D                           pop r13
003F3606  41 5C                           pop r12
003F3608  5F                              pop rdi
003F3609  5E                              pop rsi
003F360A  5B                              pop rbx
003F360B  C3                              ret
003F360C  CC                              int3
003F360D  0F 1F 00                        nop dword ptr [rax]
003F3610  55                              push rbp
003F3611  30 3F                           xor byte ptr [rdi], bh
003F3613  00 72 32                        add byte ptr [rdx + 0x32], dh
003F3616  3F                              .byte 0x3f
003F3617  00 DF                           add bh, bl
003F3619  30 3F                           xor byte ptr [rdi], bh
003F361B  00 F4                           add ah, dh
003F361D  31 3F                           xor dword ptr [rdi], edi
003F361F  00 15 32 3F 00 72               add byte ptr [rip + 0x72003f32], dl
003F3625  32 3F                           xor bh, byte ptr [rdi]
003F3627  00 27                           add byte ptr [rdi], ah
003F3629  32 3F                           xor bh, byte ptr [rdi]
003F362B  00 72 32                        add byte ptr [rdx + 0x32], dh
003F362E  3F                              .byte 0x3f
003F362F  00 72 32                        add byte ptr [rdx + 0x32], dh
003F3632  3F                              .byte 0x3f
003F3633  00 CA                           add dl, cl
003F3635  30 3F                           xor byte ptr [rdi], bh
003F3637  00 72 32                        add byte ptr [rdx + 0x32], dh
003F363A  3F                              .byte 0x3f
003F363B  00 72 32                        add byte ptr [rdx + 0x32], dh
003F363E  3F                              .byte 0x3f
003F363F  00 72 32                        add byte ptr [rdx + 0x32], dh
003F3642  3F                              .byte 0x3f
003F3643  00 54 33 3F                     add byte ptr [rbx + rsi + 0x3f], dl
003F3647  00 72 32                        add byte ptr [rdx + 0x32], dh
003F364A  3F                              .byte 0x3f
003F364B  00 72 32                        add byte ptr [rdx + 0x32], dh
003F364E  3F                              .byte 0x3f
003F364F  00 72 32                        add byte ptr [rdx + 0x32], dh
003F3652  3F                              .byte 0x3f
003F3653  00 0F                           add byte ptr [rdi], cl
003F3655  32 3F                           xor bh, byte ptr [rdi]
003F3657  00 F0                           add al, dh
003F3659  30 3F                           xor byte ptr [rdi], bh
003F365B  00 72 32                        add byte ptr [rdx + 0x32], dh
003F365E  3F                              .byte 0x3f
003F365F  00 72 32                        add byte ptr [rdx + 0x32], dh
003F3662  3F                              .byte 0x3f
003F3663  00 66 32                        add byte ptr [rsi + 0x32], ah
003F3666  3F                              .byte 0x3f
003F3667  00 CA                           add dl, cl
003F3669  33 3F                           xor edi, dword ptr [rdi]
003F366B  00 55 32                        add byte ptr [rbp + 0x32], dl
003F366E  3F                              .byte 0x3f
003F366F  00 15 32 3F 00 4F               add byte ptr [rip + 0x4f003f32], dl
003F3675  32 3F                           xor bh, byte ptr [rdi]
003F3677  00 3E                           add byte ptr [rsi], bh
003F3679  33 3F                           xor edi, dword ptr [rdi]
003F367B  00 72 32                        add byte ptr [rdx + 0x32], dh
003F367E  3F                              .byte 0x3f
003F367F  00 00                           add byte ptr [rax], al
003F3681  00 05 01 05 05 05               add byte ptr [rip + 0x5050501], al
003F3687  05 05 02 03 05                  add eax, 0x5030205
003F368C  05 05 05 05 05                  add eax, 0x5050505
003F3691  05 05 05 05 05                  add eax, 0x5050505
003F3696  05 05 05 05 05                  add eax, 0x5050505
003F369B  05 05 02 00 05                  add eax, 0x5000205
003F36A0  05 05 05 05 05                  add eax, 0x5050505
003F36A5  05 05 05 05 05                  add eax, 0x5050505
003F36AA  05 05 05 05 05                  add eax, 0x5050505
003F36AF  05 05 05 05 05                  add eax, 0x5050505
003F36B4  05                              .byte 0x05
003F36B5  05                              .byte 0x05
003F36B6  04 00                           add al, 0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlCheckOplockEx2(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int8 v_stack_m114;
    unsigned __int8 v_stack_m115;
    unsigned __int8 v_stack_m116;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 10582886)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mDC = a4;
    v_stack_m108 = a3;
    v_stack_m100 = a2;
    v_stack_mD8 = a3;
    v_stack_mF8 = a5;
    v_stack_mF0 = a6;
    v_stack_mC0 = a7;
    v_stack_mC8 = a9;
    v_stack_mD0 = a10;
    v_r14 = 0;
    v_stack_m104 = 0;
    if (a4 == 0) goto loc_003F2C7E;
    goto loc_003F35E9;
loc_003F2C7E:
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) == 0) goto loc_003F2E68;
    v_stack_mF0 = 0;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_003F2CA6;
    result = 0;
    goto loc_003F35E9;
loc_003F2CA6:
    result = ExAcquireFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184))) == 0) goto loc_003F2CD2;
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a3, a4);
    goto loc_003F35E9;
loc_003F2CD2:
    result = Feature_3528882490__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 144))) & (0x10000ULL));
    if ((unsigned int)(result) == 0) goto loc_003F2DF5;
    if ((unsigned int)(a1) == 0) goto loc_003F2DB5;
    a3 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) == (*(unsigned __int64 *)(a1) + 120)) goto loc_003F2D28;
loc_003F2D06:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 24))) goto loc_003F2D1A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120))) != (*(unsigned __int64 *)(a1) + 120)) goto loc_003F2D06;
    goto loc_003F2D28;
loc_003F2D1A:
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56;
loc_003F2D28:
    if (1 == 0) goto loc_003F2DB5;
    result = FsRtlpOplockDequeueRH(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48), 1, *(unsigned __int64 *)(a1) + 120);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56)) goto loc_003F2E61;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56 + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56)) goto loc_003F2E61;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56 + 8);
loc_003F2D61:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) == (*(unsigned __int64 *)(a1) + 120)) {
    }
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 56 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 40)) != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56;
        a1 = *(unsigned __int64 *)(a1);
        result = FsRtlpClearOwner(a1, a2, 1, *(unsigned __int64 *)(a1) + 120);
    }
    result = FsRtlpSyncWithAckTimeout(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56 + 88, a2, 1, *(unsigned __int64 *)(a1) + 120);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 56, a2, 1, *(unsigned __int64 *)(a1) + 120);
    result = FsRtlpComputeShareableOplockState(*(unsigned __int64 *)(a1), a2, 1, *(unsigned __int64 *)(a1) + 120);
    result = FsRtlpReleaseIrpsWaitingForRH(*(unsigned __int64 *)(a1), a2, 1, *(unsigned __int64 *)(a1) + 120);
loc_003F2DA1:
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, 1, *(unsigned __int64 *)(a1) + 120);
    goto loc_003F35E9;
loc_003F2DB5:
    if (!sign_flag) goto loc_003F2DA1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48))) goto loc_003F2DA1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = (unsigned int)(0xC000000DULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = (unsigned int)(0xC000000DULL);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 144))) & (32));
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 144) = (unsigned int)(result);
loc_003F2DE6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88)) == (*(unsigned __int64 *)(a1) + 88)) goto loc_003F2DA1;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88), a2, 1, *(unsigned __int64 *)(a1) + 120);
    goto loc_003F2DE6;
loc_003F2DF5:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88)) == 0) goto loc_003F2DA1;
    a4 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) == (*(unsigned __int64 *)(a1) + 120)) goto loc_003F2E27;
loc_003F2E10:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120) - 32))) goto loc_003F2E20;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120))) != (*(unsigned __int64 *)(a1) + 120)) goto loc_003F2E10;
    goto loc_003F2E27;
loc_003F2E20:
loc_003F2E27:
    if (1 == 0) goto loc_003F2DA1;
    result = FsRtlpOplockDequeueRH(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56, *(unsigned __int64 *)(a1) + 120, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48), 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56)) goto loc_003F2E61;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56 + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56)) goto loc_003F2E61;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56 + 8);
    goto loc_003F2D61;
loc_003F2E61:
loc_003F2E68:
    result = *(unsigned __int64 *)(a1) + 120;
    v_r12 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) >= (*(unsigned __int64 *)(a1) + 120)) {
        a1 = 0;
        result = FsRtlpAttachOplockKey(a1, *(unsigned __int64 *)(a1) + 120, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56);
        v_r12 = (unsigned int)(result);
        v_stack_m104 = (unsigned int)(result);
    }
    result = FsRtlpOplockStoreKeyForDeleteOperation(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56 + 56);
    v_rbx = *(unsigned __int64 *)(a1);
    if ((*(unsigned __int64 *)(a1)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56))) { v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) - 56); }
    v_stack_mB0 = v_rbx;
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) != 0) goto loc_003F35E6;
    if (v_rbx == 0) goto loc_003F35E6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (2)) != 0) goto loc_003F35E6;
    if ((unsigned int)(v_r12) != 0) goto loc_003F35E6;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (29));
    result = (unsigned __int8)((result) & (1));
    v_stack_m118 = (unsigned __int8)(result);
    v_stack_m10C = 1;
    v_stack_m116 = 1;
loc_003F2EF4:
    v_stack_m114 = 0;
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) != 0) goto loc_003F2FC0;
    if (v_stack_m118 != 0) goto loc_003F2FC0;
    v_stack_m10C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 144)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184)))) != 3) goto loc_003F2F51;
    v_rdi = v_stack_m116;
    if ((((unsigned int)((unsigned int)(v_stack_m10C))) & (0xFFFF4FFEULL)) == 0) { v_rdi = (unsigned int)((unsigned int)(0xC000000DULL)); }
    v_stack_m116 = (unsigned __int8)(v_rdi);
    goto loc_003F2F59;
loc_003F2F51:
loc_003F2F59:
    v_stack_m10C = (unsigned int)(v_stack_m116);
    result = (unsigned int)(v_stack_m10C);
    v_rdi = v_stack_m116;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184)))) == 4) {
        result = (unsigned __int8)(v_stack_m116);
        if ((((unsigned int)((unsigned int)(v_stack_m10C))) & (0xFFFFDFFEULL)) == 0) { result = (unsigned int)((unsigned int)(0xC000000DULL)); }
        v_rdi = (unsigned __int8)(result);
        v_stack_m10C = (unsigned int)(v_rdi);
        v_stack_m116 = (unsigned __int8)(result);
    }
    if ((((unsigned __int8)((unsigned int)(a3))) & (8)) != 0) goto loc_003F2FB8;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184)))) == 18) goto loc_003F2FB8;
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_003F2FB8;
    if ((*(unsigned __int64 *)(v_rbx + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48))) goto loc_003F2FB8;
    v_rdi = 0;
    v_stack_m10C = 0;
    v_stack_m116 = 0;
    goto loc_003F35AF;
loc_003F2FB8:
loc_003F2FC0:
    if (0 == 0) goto loc_003F35AF;
    if (v_stack_m118 == 0) {
        a1 = *(unsigned __int64 *)(v_rbx + 152);
        result = ExAcquireFastMutexUnsafe(a1, *(unsigned __int64 *)(v_rbx + 8), v_rip - 4140783, v_r12 + 1);
        a3 = v_rip - 4141030;
        a4 = 1;
    }
    v_stack_m118 = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 144)))) == 1) goto loc_003F359C;
    v_r15 = 0;
    v_stack_m115 = 0;
    v_r14 = 0;
    v_stack_m117 = 0;
    v_rdi = 0;
    v_stack_m110 = 0;
    if (((v_stack_m108) & (16)) == 0) goto loc_003F3036;
    goto loc_003F326B;
loc_003F3036:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184)))) > 21) goto loc_003F3272;
    a1 = ((unsigned int)(*(unsigned int *)(a3 + *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184)) * 4 + 4142608))) + (a3);
loc_003F326B:
    v_stack_m110 = (unsigned int)((unsigned int)(0x5000ULL));
loc_003F3272:
    if (0 == 0) goto loc_003F3410;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_003F34D5;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48), *(unsigned __int64 *)(v_rbx + 8), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003F34D5;
    v_stack_m138 = v_stack_m114;
    v_stack_m140 = v_stack_m118;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = a8;
    v_stack_m160 = v_stack_mC0;
    v_stack_m168 = v_stack_mF0;
    v_stack_m170 = v_stack_mF8;
    result = FsRtlpOplockBreakToII(v_rbx, *(unsigned __int64 *)(a2 + 184), v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))));
    v_stack_m104 = (unsigned int)(result);
    goto loc_003F34EC;
loc_003F3410:
    if ((unsigned __int8)(v_stack_mF8) == 0) goto loc_003F34D5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_003F3441;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48), *(unsigned __int64 *)(v_rbx + 8), a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))));
    if ((unsigned __int8)(result) != 0) goto loc_003F34D5;
loc_003F3441:
    v_stack_m138 = v_stack_m114;
    v_stack_m140 = v_stack_m118;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = a8;
    v_stack_m160 = v_stack_mC0;
    v_stack_m168 = v_stack_mF0;
    v_stack_m170 = v_stack_mF8;
    result = FsRtlpOplockBreakToNone(v_rbx, *(unsigned __int64 *)(a2 + 184), v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))));
    v_stack_m104 = (unsigned int)(result);
    goto loc_003F34EC;
loc_003F34D5:
loc_003F34EC:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_003F35A5;
    if ((((unsigned int)((unsigned int)(0x5000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 144))))) == 0) goto loc_003F35A5;
    v_stack_m120 = v_stack_m114;
    v_stack_m128 = v_stack_m118;
    v_stack_m130 = v_stack_mD0;
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = a8;
    v_stack_m148 = v_stack_mC0;
    v_stack_m150 = v_stack_mF0;
    v_stack_m158 = v_stack_mF8;
    v_r14 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = (unsigned int)((unsigned int)(0x5000ULL));
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_mDC));
    result = FsRtlpOplockBreakByCacheFlags(v_rbx, *(unsigned __int64 *)(a2 + 184), v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))));
    v_stack_m104 = (unsigned int)(result);
    goto loc_003F35A8;
loc_003F359C:
    goto loc_003F35AF;
loc_003F35A5:
    v_r14 = 0;
loc_003F35A8:
loc_003F35AF:
    if (v_stack_m118 == 0) goto loc_003F35CB;
    if (v_stack_m118 >= 0) {
        a1 = *(unsigned __int64 *)(v_rbx + 152);
        result = ExReleaseFastMutexUnsafe(a1, *(unsigned __int64 *)(a2 + 184), v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))));
    }
    if (v_stack_m114 != 0) goto loc_003F2EF4;
loc_003F35E6:
loc_003F35E9:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a2 + 184), v_rip - 4142554, 1);
    v_rsp = (v_rsp) + (352);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlCheckOplockEx2(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint8_t v_stack_m114;
    uint8_t v_stack_m115;
    uint8_t v_stack_m116;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0xA17B66)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mDC = Arg4;
    v_stack_m108 = Arg3;
    v_stack_m100 = Arg2;
    v_stack_mD8 = Arg3;
    v_stack_mF8 = Arg5;
    v_stack_mF0 = Arg6;
    v_stack_mC0 = Arg7;
    v_stack_mC8 = Arg9;
    v_stack_mD0 = Arg10;
    local_r14 = 0;
    v_stack_m104 = 0;
    if (Arg4 == 0) goto loc_003F2C7E;
    goto loc_003F35E9;
loc_003F2C7E:
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) == 0) goto loc_003F2E68;
    v_stack_mF0 = 0;
    if (*(uint64_t *)(arg1) != 0) goto loc_003F2CA6;
    result = 0;
    goto loc_003F35E9;
loc_003F2CA6:
    result = ExAcquireFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8))) == 0) goto loc_003F2CD2;
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg3, Arg4);
    goto loc_003F35E9;
loc_003F2CD2:
    result = Feature_3528882490__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x90))) & (0x10000ULL));
    if ((uint32_t)(result) == 0) goto loc_003F2DF5;
    if ((uint32_t)(Arg1) == 0) goto loc_003F2DB5;
    Arg3 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) == (*(uint64_t *)(arg1) + 120)) goto loc_003F2D28;
loc_003F2D06:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x18))) goto loc_003F2D1A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78))) != (*(uint64_t *)(arg1) + 120)) goto loc_003F2D06;
    goto loc_003F2D28;
loc_003F2D1A:
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56;
loc_003F2D28:
    if (1 == 0) goto loc_003F2DB5;
    result = FsRtlpOplockDequeueRH(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56, *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30), 1, *(uint64_t *)(arg1) + 120);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56 + 56)) goto loc_003F2E61;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38 + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56 + 56)) goto loc_003F2E61;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38 + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38 + 0x8);
loc_003F2D61:
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) == (*(uint64_t *)(arg1) + 120)) {
    }
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x38 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x38 + 0x28)) != 0) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56;
        Arg1 = *(uint64_t *)(arg1);
        result = FsRtlpClearOwner(Arg1, Arg2, 1, *(uint64_t *)(arg1) + 120);
    }
    result = FsRtlpSyncWithAckTimeout(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56 + 88, Arg2, 1, *(uint64_t *)(arg1) + 120);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 56, Arg2, 1, *(uint64_t *)(arg1) + 120);
    result = FsRtlpComputeShareableOplockState(*(uint64_t *)(arg1), Arg2, 1, *(uint64_t *)(arg1) + 120);
    result = FsRtlpReleaseIrpsWaitingForRH(*(uint64_t *)(arg1), Arg2, 1, *(uint64_t *)(arg1) + 120);
loc_003F2DA1:
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, 1, *(uint64_t *)(arg1) + 120);
    goto loc_003F35E9;
loc_003F2DB5:
    if (!sign_flag) goto loc_003F2DA1;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30))) goto loc_003F2DA1;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = (uint32_t)(0xC000000DULL);
    *(uint64_t *)(*(uint64_t *)(arg1)) = (uint32_t)(0xC000000DULL);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x90))) & (32));
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x90) = (uint32_t)(result);
loc_003F2DE6:
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x58)) == (*(uint64_t *)(arg1) + 88)) goto loc_003F2DA1;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(*(uint64_t *)(arg1) + 0x58), Arg2, 1, *(uint64_t *)(arg1) + 120);
    goto loc_003F2DE6;
loc_003F2DF5:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x58)) == 0) goto loc_003F2DA1;
    Arg4 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) == (*(uint64_t *)(arg1) + 120)) goto loc_003F2E27;
loc_003F2E10:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78) - 0x20))) goto loc_003F2E20;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78))) != (*(uint64_t *)(arg1) + 120)) goto loc_003F2E10;
    goto loc_003F2E27;
loc_003F2E20:
loc_003F2E27:
    if (1 == 0) goto loc_003F2DA1;
    result = FsRtlpOplockDequeueRH(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56, *(uint64_t *)(arg1) + 120, *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30), 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56 + 56)) goto loc_003F2E61;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38 + 0x8))) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56 + 56)) goto loc_003F2E61;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38 + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38 + 0x38 + 0x8);
    goto loc_003F2D61;
loc_003F2E61:
loc_003F2E68:
    result = *(uint64_t *)(arg1) + 120;
    local_r12 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) >= (*(uint64_t *)(arg1) + 120)) {
        Arg1 = 0;
        result = FsRtlpAttachOplockKey(Arg1, *(uint64_t *)(arg1) + 120, *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56 + 56);
        local_r12 = (uint32_t)(result);
        v_stack_m104 = (uint32_t)(result);
    }
    result = FsRtlpOplockStoreKeyForDeleteOperation(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 56 + 56);
    local_rbx = *(uint64_t *)(arg1);
    if ((*(uint64_t *)(arg1)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38))) { local_rbx = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) - 0x38); }
    v_stack_mB0 = local_rbx;
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) != 0) goto loc_003F35E6;
    if (local_rbx == 0) goto loc_003F35E6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) & (2)) != 0) goto loc_003F35E6;
    if ((uint32_t)(local_r12) != 0) goto loc_003F35E6;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (29));
    result = (uint8_t)((result) & (1));
    v_stack_m118 = (uint8_t)(result);
    v_stack_m10C = 1;
    v_stack_m116 = 1;
loc_003F2EF4:
    v_stack_m114 = 0;
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) != 0) goto loc_003F2FC0;
    if (v_stack_m118 != 0) goto loc_003F2FC0;
    v_stack_m10C = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x90)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8)))) != 3) goto loc_003F2F51;
    local_rdi = v_stack_m116;
    if ((((uint32_t)((uint32_t)(v_stack_m10C))) & (0xFFFF4FFEULL)) == 0) { local_rdi = (uint32_t)((uint32_t)(0xC000000DULL)); }
    v_stack_m116 = (uint8_t)(local_rdi);
    goto loc_003F2F59;
loc_003F2F51:
loc_003F2F59:
    v_stack_m10C = (uint32_t)(v_stack_m116);
    result = (uint32_t)(v_stack_m10C);
    local_rdi = v_stack_m116;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8)))) == 4) {
        result = (uint8_t)(v_stack_m116);
        if ((((uint32_t)((uint32_t)(v_stack_m10C))) & (0xFFFFDFFEULL)) == 0) { result = (uint32_t)((uint32_t)(0xC000000DULL)); }
        local_rdi = (uint8_t)(result);
        v_stack_m10C = (uint32_t)(local_rdi);
        v_stack_m116 = (uint8_t)(result);
    }
    if ((((uint8_t)((uint32_t)(Arg3))) & (8)) != 0) goto loc_003F2FB8;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8)))) == 18) goto loc_003F2FB8;
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_003F2FB8;
    if ((*(uint64_t *)(local_rbx + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30))) goto loc_003F2FB8;
    local_rdi = 0;
    v_stack_m10C = 0;
    v_stack_m116 = 0;
    goto loc_003F35AF;
loc_003F2FB8:
loc_003F2FC0:
    if (0 == 0) goto loc_003F35AF;
    if (v_stack_m118 == 0) {
        Arg1 = *(uint64_t *)(local_rbx + 0x98);
        result = ExAcquireFastMutexUnsafe(Arg1, *(uint64_t *)(local_rbx + 0x8), v_rip - 4140783, local_r12 + 1);
        Arg3 = v_rip - 4141030;
        Arg4 = 1;
    }
    v_stack_m118 = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x90)))) == 1) goto loc_003F359C;
    local_r15 = 0;
    v_stack_m115 = 0;
    local_r14 = 0;
    v_stack_m117 = 0;
    local_rdi = 0;
    v_stack_m110 = 0;
    if (((v_stack_m108) & (16)) == 0) goto loc_003F3036;
    goto loc_003F326B;
loc_003F3036:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8)))) > 21) goto loc_003F3272;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg3 + *(uint8_t *)(*(uint64_t *)(arg2 + 0xB8)) * 4 + 0x3F3610))) + (Arg3);
loc_003F326B:
    v_stack_m110 = (uint32_t)((uint32_t)(0x5000ULL));
loc_003F3272:
    if (0 == 0) goto loc_003F3410;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_003F34D5;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30), *(uint64_t *)(local_rbx + 0x8), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_003F34D5;
    v_stack_m138 = v_stack_m114;
    v_stack_m140 = v_stack_m118;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = Arg8;
    v_stack_m160 = v_stack_mC0;
    v_stack_m168 = v_stack_mF0;
    v_stack_m170 = v_stack_mF8;
    result = FsRtlpOplockBreakToII(local_rbx, *(uint64_t *)(arg2 + 0xB8), v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))));
    v_stack_m104 = (uint32_t)(result);
    goto loc_003F34EC;
loc_003F3410:
    if ((uint8_t)(v_stack_mF8) == 0) goto loc_003F34D5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_003F3441;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30), *(uint64_t *)(local_rbx + 0x8), Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))));
    if ((uint8_t)(result) != 0) goto loc_003F34D5;
loc_003F3441:
    v_stack_m138 = v_stack_m114;
    v_stack_m140 = v_stack_m118;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = Arg8;
    v_stack_m160 = v_stack_mC0;
    v_stack_m168 = v_stack_mF0;
    v_stack_m170 = v_stack_mF8;
    result = FsRtlpOplockBreakToNone(local_rbx, *(uint64_t *)(arg2 + 0xB8), v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))));
    v_stack_m104 = (uint32_t)(result);
    goto loc_003F34EC;
loc_003F34D5:
loc_003F34EC:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_003F35A5;
    if ((((uint32_t)((uint32_t)(0x5000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x90))))) == 0) goto loc_003F35A5;
    v_stack_m120 = v_stack_m114;
    v_stack_m128 = v_stack_m118;
    v_stack_m130 = v_stack_mD0;
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = Arg8;
    v_stack_m148 = v_stack_mC0;
    v_stack_m150 = v_stack_mF0;
    v_stack_m158 = v_stack_mF8;
    local_r14 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = (uint32_t)((uint32_t)(0x5000ULL));
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_mDC));
    result = FsRtlpOplockBreakByCacheFlags(local_rbx, *(uint64_t *)(arg2 + 0xB8), v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))));
    v_stack_m104 = (uint32_t)(result);
    goto loc_003F35A8;
loc_003F359C:
    goto loc_003F35AF;
loc_003F35A5:
    local_r14 = 0;
loc_003F35A8:
loc_003F35AF:
    if (v_stack_m118 == 0) goto loc_003F35CB;
    if (v_stack_m118 >= 0) {
        Arg1 = *(uint64_t *)(local_rbx + 0x98);
        result = ExReleaseFastMutexUnsafe(Arg1, *(uint64_t *)(arg2 + 0xB8), v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))));
    }
    if (v_stack_m114 != 0) goto loc_003F2EF4;
loc_003F35E6:
loc_003F35E9:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg2 + 0xB8), v_rip - 4142554, 1);
    local_rsp = (local_rsp) + (352);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F2BC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
