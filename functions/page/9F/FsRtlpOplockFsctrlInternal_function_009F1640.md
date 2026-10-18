# FsRtlpOplockFsctrlInternal

- RVA: `0x009F1640`–`0x009F1C6D` (길이 `1,581` bytes)
- VA: `0x00000001409F1640`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5EC4`
- 디코드: `414`개 명령, `1,581/1,581` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009F1712` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (function, `0x0041E6A0`)
- `0x009F174A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F17A4` → [FsRtlpRequestShareableOplock](../../text/4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) (function, `0x004E6EC8`)
- `0x009F17CA` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x009F17D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F1804` → [FsRtlpAttachOplockKey](../../text/41/FsRtlpAttachOplockKey_function_0041DD70.md) (function, `0x0041DD70`)
- `0x009F182A` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x009F1848` → [FsRtlCheckOplockEx](../../text/3F/FsRtlCheckOplockEx_function_003F2960.md) (function, `0x003F2960`)
- `0x009F1861` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F1899` → [FsRtlpRequestShareableOplock](../../text/4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) (function, `0x004E6EC8`)
- `0x009F18BB` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x009F18C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F18D3` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009F18DD` → [FsRtlpAllocateOplock](FsRtlpAllocateOplock_function_009F1C74.md) (function, `0x009F1C74`)
- `0x009F1903` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (function, `0x0041E6A0`)
- `0x009F1964` → [FsRtlpRequestExclusiveOplock](../../text/3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) (function, `0x003F3800`)
- `0x009F19B7` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x009F19FA` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (function, `0x0041E6A0`)
- `0x009F1A2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F1A80` → [FsRtlpAcknowledgeOplockBreakByCacheFlags](../../text/3F/FsRtlpAcknowledgeOplockBreakByCacheFlags_function_003F1988.md) (function, `0x003F1988`)
- `0x009F1A9C` → [FsRtlpClearOwner](../../text/26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x009F1AA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F1AC2` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (function, `0x0041E6A0`)
- `0x009F1B0E` → [FsRtlpRequestExclusiveOplock](../../text/3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) (function, `0x003F3800`)
- `0x009F1B3D` → [FsRtlpAcknowledgeOplockBreak](../../text/58/FsRtlpAcknowledgeOplockBreak_function_00582144.md) (function, `0x00582144`)
- `0x009F1B50` → [FsRtlpOpBatchBreakClosePending](../71/FsRtlpOpBatchBreakClosePending_function_00714CDC.md) (function, `0x00714CDC`)
- `0x009F1B60` → [FsRtlpOplockBreakNotify](../71/FsRtlpOplockBreakNotify_function_00714E10.md) (function, `0x00714E10`)
- `0x009F1B8D` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)

### Direct callers
- [FsRtlUpperOplockFsctrl](../71/FsRtlUpperOplockFsctrl_function_00714B40.md) at `0x00714CA4`
- [FsRtlOplockFsctrl](FsRtlOplockFsctrl_function_009F1600.md) at `0x009F160F`
- [FsRtlOplockFsctrlEx](FsRtlOplockFsctrlEx_function_009F1620.md) at `0x009F162C`

### Static image references
- `0x009F197E` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x009F1712` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (`PAGE` → `.text`)
  - `0x009F174A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F17A4` → [FsRtlpRequestShareableOplock](../../text/4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) (`PAGE` → `.text`)
  - `0x009F17CA` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x009F17D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F1804` → [FsRtlpAttachOplockKey](../../text/41/FsRtlpAttachOplockKey_function_0041DD70.md) (`PAGE` → `.text`)
  - `0x009F182A` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x009F1848` → [FsRtlCheckOplockEx](../../text/3F/FsRtlCheckOplockEx_function_003F2960.md) (`PAGE` → `.text`)
  - `0x009F1861` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F1899` → [FsRtlpRequestShareableOplock](../../text/4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) (`PAGE` → `.text`)
  - `0x009F18BB` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x009F18C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F18D3` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009F1903` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (`PAGE` → `.text`)
  - `0x009F1964` → [FsRtlpRequestExclusiveOplock](../../text/3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) (`PAGE` → `.text`)
  - `0x009F19B7` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x009F19FA` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (`PAGE` → `.text`)
  - `0x009F1A2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F1A80` → [FsRtlpAcknowledgeOplockBreakByCacheFlags](../../text/3F/FsRtlpAcknowledgeOplockBreakByCacheFlags_function_003F1988.md) (`PAGE` → `.text`)
  - `0x009F1A9C` → [FsRtlpClearOwner](../../text/26/FsRtlpClearOwner_function_00265BE8.md) (`PAGE` → `.text`)
  - `0x009F1AA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F1AC2` → [IoIsOperationSynchronous](../../text/41/IoIsOperationSynchronous_function_0041E6A0.md) (`PAGE` → `.text`)
  - `0x009F1B0E` → [FsRtlpRequestExclusiveOplock](../../text/3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) (`PAGE` → `.text`)
  - `0x009F1B3D` → [FsRtlpAcknowledgeOplockBreak](../../text/58/FsRtlpAcknowledgeOplockBreak_function_00582144.md) (`PAGE` → `.text`)
  - `0x009F1B8D` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x009F17F5` → [sub_00B3115E](../B3/Unknown_function_00B3115E.md) (`tail-transfer`)
  - `0x009F18EF` → [sub_00B3115E + 0xD0](../B3/Unknown_function_00B3115E.md) (`tail-transfer`)
  - `0x009F1BE7` → [sub_00B3115E + 0x177](../B3/Unknown_function_00B3115E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009F1640  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
009F1645  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
009F164A  53                              push rbx
009F164B  56                              push rsi
009F164C  57                              push rdi
009F164D  41 54                           push r12
009F164F  41 55                           push r13
009F1651  41 56                           push r14
009F1653  41 57                           push r15
009F1655  48 83 EC 60                     sub rsp, 0x60
009F1659  45 8B E0                        mov r12d, r8d
009F165C  48 8B F2                        mov rsi, rdx
009F165F  4C 8B F1                        mov r14, rcx
009F1662  45 33 ED                        xor r13d, r13d
009F1665  41 8B FD                        mov edi, r13d
009F1668  45 8B FD                        mov r15d, r13d
009F166B  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
009F1670  48 8B 9A B8 00 00 00            mov rbx, qword ptr [rdx + 0xb8]
009F1677  44 38 2B                        cmp byte ptr [rbx], r13b
009F167A  0F 84 6E 01 00 00               je 0x1409f17ee
009F1680  41 8D 7D 02                     lea edi, [r13 + 2]
009F1684  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
009F1687  3D 40 02 09 00                  cmp eax, 0x90240
009F168C  0F 85 DE 02 00 00               jne 0x1409f1970
009F1692  4C 8B 6A 18                     mov r13, qword ptr [rdx + 0x18]
009F1696  83 7B 10 0C                     cmp dword ptr [rbx + 0x10], 0xc
009F169A  0F 82 7A 04 00 00               jb 0x1409f1b1a
009F16A0  83 7B 08 18                     cmp dword ptr [rbx + 8], 0x18
009F16A4  0F 82 70 04 00 00               jb 0x1409f1b1a
009F16AA  66 41 83 7D 00 01               cmp word ptr [r13], 1
009F16B0  0F 87 FC 03 00 00               ja 0x1409f1ab2
009F16B6  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
009F16BA  A8 01                           test al, 1
009F16BC  0F 84 08 03 00 00               je 0x1409f19ca
009F16C2  41 8B 7D 04                     mov edi, dword ptr [r13 + 4]
009F16C6  8B CF                           mov ecx, edi
009F16C8  83 E1 01                        and ecx, 1
009F16CB  C1 E1 0C                        shl ecx, 0xc
009F16CE  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
009F16D2  8B C7                           mov eax, edi
009F16D4  83 E0 04                        and eax, 4
009F16D7  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
009F16DE  8B D7                           mov edx, edi
009F16E0  83 E2 02                        and edx, 2
009F16E3  C1 E2 0C                        shl edx, 0xc
009F16E6  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
009F16EA  F7 D8                           neg eax
009F16EC  1B C0                           sbb eax, eax
009F16EE  25 00 40 00 00                  and eax, 0x4000
009F16F3  0B C2                           or eax, edx
009F16F5  0B C1                           or eax, ecx
009F16F7  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009F16FB  3D 00 30 00 00                  cmp eax, 0x3000
009F1700  0F 85 E7 01 00 00               jne 0x1409f18ed
009F1706  45 85 E4                        test r12d, r12d
009F1709  0F 85 9B 02 00 00               jne 0x1409f19aa
009F170F  48 8B CE                        mov rcx, rsi
009F1712  E8 89 CF A2 FF                  call 0x14041e6a0
009F1717  84 C0                           test al, al
009F1719  0F 85 8B 02 00 00               jne 0x1409f19aa
009F171F  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F1723  F7 40 50 00 40 00 00            test dword ptr [rax + 0x50], 0x4000
009F172A  0F 85 7A 02 00 00               jne 0x1409f19aa
009F1730  F7 44 24 48 00 20 00 00         test dword ptr [rsp + 0x48], 0x2000
009F1738  74 21                           je 0x1409f175b
009F173A  41 8D 54 24 60                  lea edx, [r12 + 0x60]
009F173F  B9 20 01 00 00                  mov ecx, 0x120
009F1744  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F174A  E8 A1 09 19 00                  call 0x140b820f0
009F174F  4C 8B F8                        mov r15, rax
009F1752  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F1757  41 8B 7D 04                     mov edi, dword ptr [r13 + 4]
009F175B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
009F1760  4D 85 FF                        test r15, r15
009F1763  41 BF 00 00 00 00               mov r15d, 0
009F1769  49 0F 44 CF                     cmove rcx, r15
009F176D  44 8B CF                        mov r9d, edi
009F1770  41 83 E1 06                     and r9d, 6
009F1774  41 C1 E1 0C                     shl r9d, 0xc
009F1778  83 E7 01                        and edi, 1
009F177B  C1 E7 0C                        shl edi, 0xc
009F177E  44 0B CF                        or r9d, edi
009F1781  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1788  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009F178C  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
009F1791  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009F1796  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009F179B  4C 8B C6                        mov r8, rsi
009F179E  48 8B D3                        mov rdx, rbx
009F17A1  49 8B CE                        mov rcx, r14
009F17A4  E8 1F 57 AF FF                  call 0x1404e6ec8
009F17A9  8B F8                           mov edi, eax
009F17AB  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
009F17AF  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F17B4  48 85 C0                        test rax, rax
009F17B7  74 22                           je 0x1409f17db
009F17B9  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
009F17BD  4C 89 78 28                     mov qword ptr [rax + 0x28], r15
009F17C1  4C 89 78 20                     mov qword ptr [rax + 0x20], r15
009F17C5  48 85 C9                        test rcx, rcx
009F17C8  74 05                           je 0x1409f17cf
009F17CA  E8 71 B6 A0 FF                  call 0x1403fce40
009F17CF  33 D2                           xor edx, edx
009F17D1  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009F17D6  E8 95 10 19 00                  call 0x140b82870
009F17DB  8B C7                           mov eax, edi
009F17DD  48 83 C4 60                     add rsp, 0x60
009F17E1  41 5F                           pop r15
009F17E3  41 5E                           pop r14
009F17E5  41 5D                           pop r13
009F17E7  41 5C                           pop r12
009F17E9  5F                              pop rdi
009F17EA  5E                              pop rsi
009F17EB  5B                              pop rbx
009F17EC  C3                              ret
009F17ED  CC                              int3
009F17EE  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
009F17F1  0F BA E0 14                     bt eax, 0x14
009F17F5  0F 82 63 F9 13 00               jb 0x140b3115e
009F17FB  0F BA E0 10                     bt eax, 0x10
009F17FF  73 DA                           jae 0x1409f17db
009F1801  48 8B CE                        mov rcx, rsi
009F1804  E8 67 C5 A2 FF                  call 0x14041dd70
009F1809  8B F8                           mov edi, eax
009F180B  85 C0                           test eax, eax
009F180D  75 CC                           jne 0x1409f17db
009F180F  4D 8B 3E                        mov r15, qword ptr [r14]
009F1812  4D 85 FF                        test r15, r15
009F1815  0F 84 C2 00 00 00               je 0x1409f18dd
009F181B  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
009F1823  49 8B 8F 98 00 00 00            mov rcx, qword ptr [r15 + 0x98]
009F182A  E8 F1 1E A0 FF                  call 0x1403f3720
009F182F  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
009F1834  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009F1839  45 33 C9                        xor r9d, r9d
009F183C  41 B8 00 00 00 30               mov r8d, 0x30000000
009F1842  48 8B D6                        mov rdx, rsi
009F1845  49 8B CE                        mov rcx, r14
009F1848  E8 13 11 A0 FF                  call 0x1403f2960
009F184D  8B F8                           mov edi, eax
009F184F  85 C0                           test eax, eax
009F1851  75 4D                           jne 0x1409f18a0
009F1853  8D 50 60                        lea edx, [rax + 0x60]
009F1856  B9 20 01 00 00                  mov ecx, 0x120
009F185B  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F1861  E8 8A 08 19 00                  call 0x140b820f0
009F1866  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F186B  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1872  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009F1876  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
009F187B  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
009F1880  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009F1885  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F188A  41 B9 00 00 01 00               mov r9d, 0x10000
009F1890  45 33 C0                        xor r8d, r8d
009F1893  48 8B D3                        mov rdx, rbx
009F1896  49 8B CE                        mov rcx, r14
009F1899  E8 2A 56 AF FF                  call 0x1404e6ec8
009F189E  8B F8                           mov edi, eax
009F18A0  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F18A5  48 85 C0                        test rax, rax
009F18A8  74 22                           je 0x1409f18cc
009F18AA  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
009F18AE  4C 89 68 28                     mov qword ptr [rax + 0x28], r13
009F18B2  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
009F18B6  48 85 C9                        test rcx, rcx
009F18B9  74 05                           je 0x1409f18c0
009F18BB  E8 80 B5 A0 FF                  call 0x1403fce40
009F18C0  33 D2                           xor edx, edx
009F18C2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009F18C7  E8 A4 0F 19 00                  call 0x140b82870
009F18CC  49 8B 8F 98 00 00 00            mov rcx, qword ptr [r15 + 0x98]
009F18D3  E8 C8 EA 85 FF                  call 0x1402503a0
009F18D8  E9 FE FE FF FF                  jmp 0x1409f17db
009F18DD  E8 92 03 00 00                  call 0x1409f1c74
009F18E2  4C 8B F8                        mov r15, rax
009F18E5  49 89 06                        mov qword ptr [r14], rax
009F18E8  E9 2E FF FF FF                  jmp 0x1409f181b
009F18ED  85 C0                           test eax, eax
009F18EF  0F 84 39 F9 13 00               je 0x140b3122e
009F18F5  3D 00 70 00 00                  cmp eax, 0x7000
009F18FA  0F 85 6A 02 00 00               jne 0x1409f1b6a
009F1900  48 8B CE                        mov rcx, rsi
009F1903  E8 98 CD A2 FF                  call 0x14041e6a0
009F1908  84 C0                           test al, al
009F190A  0F 85 9A 00 00 00               jne 0x1409f19aa
009F1910  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F1914  F7 40 50 00 40 00 00            test dword ptr [rax + 0x50], 0x4000
009F191B  0F 85 89 00 00 00               jne 0x1409f19aa
009F1921  B9 40 40 00 00                  mov ecx, 0x4040
009F1926  B8 40 00 00 00                  mov eax, 0x40
009F192B  44 39 BC 24 A8 00 00 00         cmp dword ptr [rsp + 0xa8], r15d
009F1933  0F 44 C8                        cmove ecx, eax
009F1936  0B 4C 24 40                     or ecx, dword ptr [rsp + 0x40]
009F193A  0B 4C 24 44                     or ecx, dword ptr [rsp + 0x44]
009F193E  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1945  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F1949  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
009F194D  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
009F1954  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009F1958  45 8B CC                        mov r9d, r12d
009F195B  4C 8B C6                        mov r8, rsi
009F195E  48 8B D3                        mov rdx, rbx
009F1961  49 8B CE                        mov rcx, r14
009F1964  E8 97 1E A0 FF                  call 0x1403f3800
009F1969  8B F8                           mov edi, eax
009F196B  E9 6B FE FF FF                  jmp 0x1409f17db
009F1970  05 00 00 F7 FF                  add eax, 0xfff70000
009F1975  83 F8 5C                        cmp eax, 0x5c
009F1978  0F 87 02 02 00 00               ja 0x1409f1b80
009F197E  48 8D 15 7B E6 60 FF            lea rdx, [rip - 0x9f1985]
009F1985  0F B6 84 02 10 1C 9F 00         movzx eax, byte ptr [rdx + rax + 0x9f1c10]
009F198D  8B 8C 82 EC 1B 9F 00            mov ecx, dword ptr [rdx + rax*4 + 0x9f1bec]
009F1994  48 03 CA                        add rcx, rdx
009F1997  FF E1                           jmp rcx
009F1999  CC                              int3
009F199A  CC                              int3
009F199B  CC                              int3
009F199C  CC                              int3
009F199D  83 CF 40                        or edi, 0x40
009F19A0  41 83 FC 01                     cmp r12d, 1
009F19A4  0F 84 15 01 00 00               je 0x1409f1abf
009F19AA  BF E2 00 00 C0                  mov edi, 0xc00000e2
009F19AF  89 7E 30                        mov dword ptr [rsi + 0x30], edi
009F19B2  B2 01                           mov dl, 1
009F19B4  48 8B CE                        mov rcx, rsi
009F19B7  E8 04 9C 8A FF                  call 0x14029b5c0
009F19BC  E9 1A FE FF FF                  jmp 0x1409f17db
009F19C1  BF 04 00 00 00                  mov edi, 4
009F19C6  03 FF                           add edi, edi
009F19C8  EB D3                           jmp 0x1409f199d
009F19CA  40 84 C7                        test dil, al
009F19CD  0F 84 DF 00 00 00               je 0x1409f1ab2
009F19D3  45 8B 65 04                     mov r12d, dword ptr [r13 + 4]
009F19D7  41 8B FC                        mov edi, r12d
009F19DA  83 E7 06                        and edi, 6
009F19DD  C1 E7 0C                        shl edi, 0xc
009F19E0  41 8B C4                        mov eax, r12d
009F19E3  83 E0 01                        and eax, 1
009F19E6  C1 E0 0C                        shl eax, 0xc
009F19E9  0B F8                           or edi, eax
009F19EB  81 FF 00 70 00 00               cmp edi, 0x7000
009F19F1  0F 85 A0 01 00 00               jne 0x1409f1b97
009F19F7  48 8B CE                        mov rcx, rsi
009F19FA  E8 A1 CC A2 FF                  call 0x14041e6a0
009F19FF  84 C0                           test al, al
009F1A01  0F 85 79 01 00 00               jne 0x1409f1b80
009F1A07  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F1A0B  F7 40 50 00 40 00 00            test dword ptr [rax + 0x50], 0x4000
009F1A12  0F 85 B0 01 00 00               jne 0x1409f1bc8
009F1A18  0F BA E7 0D                     bt edi, 0xd
009F1A1C  73 21                           jae 0x1409f1a3f
009F1A1E  BA 60 00 00 00                  mov edx, 0x60
009F1A23  B9 20 01 00 00                  mov ecx, 0x120
009F1A28  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F1A2E  E8 BD 06 19 00                  call 0x140b820f0
009F1A33  4C 8B F8                        mov r15, rax
009F1A36  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F1A3B  45 8B 65 04                     mov r12d, dword ptr [r13 + 4]
009F1A3F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
009F1A44  4D 85 FF                        test r15, r15
009F1A47  41 BF 00 00 00 00               mov r15d, 0
009F1A4D  49 0F 44 CF                     cmove rcx, r15
009F1A51  45 8B CC                        mov r9d, r12d
009F1A54  41 83 E1 06                     and r9d, 6
009F1A58  41 C1 E1 0C                     shl r9d, 0xc
009F1A5C  41 83 E4 01                     and r12d, 1
009F1A60  41 C1 E4 0C                     shl r12d, 0xc
009F1A64  45 0B CC                        or r9d, r12d
009F1A67  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1A6E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009F1A72  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009F1A77  4C 8B C6                        mov r8, rsi
009F1A7A  48 8B D3                        mov rdx, rbx
009F1A7D  49 8B 0E                        mov rcx, qword ptr [r14]
009F1A80  E8 03 FF 9F FF                  call 0x1403f1988
009F1A85  8B F8                           mov edi, eax
009F1A87  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
009F1A8B  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
009F1A90  48 85 D2                        test rdx, rdx
009F1A93  0F 84 42 FD FF FF               je 0x1409f17db
009F1A99  49 8B 0E                        mov rcx, qword ptr [r14]
009F1A9C  E8 47 41 87 FF                  call 0x140265be8
009F1AA1  33 D2                           xor edx, edx
009F1AA3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009F1AA8  E8 C3 0D 19 00                  call 0x140b82870
009F1AAD  E9 29 FD FF FF                  jmp 0x1409f17db
009F1AB2  BF 0D 00 00 C0                  mov edi, 0xc000000d
009F1AB7  89 7A 30                        mov dword ptr [rdx + 0x30], edi
009F1ABA  E9 F3 FE FF FF                  jmp 0x1409f19b2
009F1ABF  48 8B CE                        mov rcx, rsi
009F1AC2  E8 D9 CB A2 FF                  call 0x14041e6a0
009F1AC7  84 C0                           test al, al
009F1AC9  0F 85 DB FE FF FF               jne 0x1409f19aa
009F1ACF  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
009F1AD2  A8 40                           test al, 0x40
009F1AD4  0F 85 D0 FE FF FF               jne 0x1409f19aa
009F1ADA  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
009F1ADE  F7 40 50 00 40 00 00            test dword ptr [rax + 0x50], 0x4000
009F1AE5  0F 85 BF FE FF FF               jne 0x1409f19aa
009F1AEB  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1AF2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F1AF6  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009F1AFA  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009F1AFF  41 B9 01 00 00 00               mov r9d, 1
009F1B05  4C 8B C6                        mov r8, rsi
009F1B08  48 8B D3                        mov rdx, rbx
009F1B0B  49 8B CE                        mov rcx, r14
009F1B0E  E8 ED 1C A0 FF                  call 0x1403f3800
009F1B13  8B F8                           mov edi, eax
009F1B15  E9 C1 FC FF FF                  jmp 0x1409f17db
009F1B1A  BF 23 00 00 C0                  mov edi, 0xc0000023
009F1B1F  EB 96                           jmp 0x1409f1ab7
009F1B21  41 B1 01                        mov r9b, 1
009F1B24  EB 03                           jmp 0x1409f1b29
009F1B26  45 33 C9                        xor r9d, r9d
009F1B29  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F1B30  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009F1B34  4C 8B C6                        mov r8, rsi
009F1B37  48 8B D3                        mov rdx, rbx
009F1B3A  49 8B 0E                        mov rcx, qword ptr [r14]
009F1B3D  E8 02 06 B9 FF                  call 0x140582144
009F1B42  E9 22 FE FF FF                  jmp 0x1409f1969
009F1B47  4C 8B C6                        mov r8, rsi
009F1B4A  48 8B D3                        mov rdx, rbx
009F1B4D  49 8B 0E                        mov rcx, qword ptr [r14]
009F1B50  E8 87 31 D2 FF                  call 0x140714cdc
009F1B55  E9 0F FE FF FF                  jmp 0x1409f1969
009F1B5A  4C 8B C6                        mov r8, rsi
009F1B5D  49 8B 0E                        mov rcx, qword ptr [r14]
009F1B60  E8 AB 32 D2 FF                  call 0x140714e10
009F1B65  E9 FF FD FF FF                  jmp 0x1409f1969
009F1B6A  3D 00 10 00 00                  cmp eax, 0x1000
009F1B6F  0F 84 91 FB FF FF               je 0x1409f1706
009F1B75  3D 00 50 00 00                  cmp eax, 0x5000
009F1B7A  0F 84 80 FD FF FF               je 0x1409f1900
009F1B80  BF 0D 00 00 C0                  mov edi, 0xc000000d
009F1B85  89 7E 30                        mov dword ptr [rsi + 0x30], edi
009F1B88  B2 01                           mov dl, 1
009F1B8A  48 8B CE                        mov rcx, rsi
009F1B8D  E8 2E 9A 8A FF                  call 0x14029b5c0
009F1B92  E9 44 FC FF FF                  jmp 0x1409f17db
009F1B97  85 FF                           test edi, edi
009F1B99  0F 84 58 FE FF FF               je 0x1409f19f7
009F1B9F  81 FF 00 10 00 00               cmp edi, 0x1000
009F1BA5  0F 84 4C FE FF FF               je 0x1409f19f7
009F1BAB  81 FF 00 30 00 00               cmp edi, 0x3000
009F1BB1  0F 84 40 FE FF FF               je 0x1409f19f7
009F1BB7  81 FF 00 50 00 00               cmp edi, 0x5000
009F1BBD  0F 85 EF FE FF FF               jne 0x1409f1ab2
009F1BC3  E9 2F FE FF FF                  jmp 0x1409f19f7
009F1BC8  0F 57 C0                        xorps xmm0, xmm0
009F1BCB  33 C0                           xor eax, eax
009F1BCD  41 0F 11 45 00                  movups xmmword ptr [r13], xmm0
009F1BD2  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
009F1BD6  41 C7 45 00 01 00 18 00         mov dword ptr [r13], 0x180001
009F1BDE  B8 18 00 00 00                  mov eax, 0x18
009F1BE3  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
009F1BE7  E9 E9 F6 13 00                  jmp 0x140b312d5
009F1BEC  9D                              popfq
009F1BED  19 9F 00 C6 11 B3               sbb dword ptr [rdi - 0x4cee3a00], ebx
009F1BF3  00 C6                           add dh, al
009F1BF5  19 9F 00 21 1B 9F               sbb dword ptr [rdi - 0x60e4df00], ebx
009F1BFB  00 47 1B                        add byte ptr [rdi + 0x1b], al
009F1BFE  9F                              lahf
009F1BFF  00 5A 1B                        add byte ptr [rdx + 0x1b], bl
009F1C02  9F                              lahf
009F1C03  00 26                           add byte ptr [rsi], ah
009F1C05  1B 9F 00 C1 19 9F               sbb ebx, dword ptr [rdi - 0x60e63f00]
009F1C0B  00 80 1B 9F 00 00               add byte ptr [rax + 0x9f1b], al
009F1C11  08 08                           or byte ptr [rax], cl
009F1C13  08 01                           or byte ptr [rcx], al
009F1C15  08 08                           or byte ptr [rax], cl
009F1C17  08 02                           or byte ptr [rdx], al
009F1C19  08 08                           or byte ptr [rax], cl
009F1C1B  08 03                           or byte ptr [rbx], al
009F1C1D  08 08                           or byte ptr [rax], cl
009F1C1F  08 04 08                        or byte ptr [rax + rcx], al
009F1C22  08 08                           or byte ptr [rax], cl
009F1C24  05 08 08 08 08                  add eax, 0x8080808
009F1C29  08 08                           or byte ptr [rax], cl
009F1C2B  08 08                           or byte ptr [rax], cl
009F1C2D  08 08                           or byte ptr [rax], cl
009F1C2F  08 08                           or byte ptr [rax], cl
009F1C31  08 08                           or byte ptr [rax], cl
009F1C33  08 08                           or byte ptr [rax], cl
009F1C35  08 08                           or byte ptr [rax], cl
009F1C37  08 08                           or byte ptr [rax], cl
009F1C39  08 08                           or byte ptr [rax], cl
009F1C3B  08 08                           or byte ptr [rax], cl
009F1C3D  08 08                           or byte ptr [rax], cl
009F1C3F  08 08                           or byte ptr [rax], cl
009F1C41  08 08                           or byte ptr [rax], cl
009F1C43  08 08                           or byte ptr [rax], cl
009F1C45  08 08                           or byte ptr [rax], cl
009F1C47  08 08                           or byte ptr [rax], cl
009F1C49  08 08                           or byte ptr [rax], cl
009F1C4B  08 08                           or byte ptr [rax], cl
009F1C4D  08 08                           or byte ptr [rax], cl
009F1C4F  08 08                           or byte ptr [rax], cl
009F1C51  08 08                           or byte ptr [rax], cl
009F1C53  08 08                           or byte ptr [rax], cl
009F1C55  08 08                           or byte ptr [rax], cl
009F1C57  08 08                           or byte ptr [rax], cl
009F1C59  08 08                           or byte ptr [rax], cl
009F1C5B  08 08                           or byte ptr [rax], cl
009F1C5D  08 08                           or byte ptr [rax], cl
009F1C5F  08 06                           or byte ptr [rsi], al
009F1C61  08 08                           or byte ptr [rax], cl
009F1C63  08 08                           or byte ptr [rax], cl
009F1C65  08 08                           or byte ptr [rax], cl
009F1C67  08 08                           or byte ptr [rax], cl
009F1C69  08 08                           or byte ptr [rax], cl
009F1C6B  08 07                           or byte ptr [rdi], al
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpOplockFsctrlInternal(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC0;

    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r13 = 0;
    v_stack_m48 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184))) == 0) goto loc_009F17EE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24)))) != 0x90240ULL) goto loc_009F1970;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 16)) < 12) goto loc_009F1B1A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)) < 24) goto loc_009F1B1A;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 24))) > 1) goto loc_009F1AB2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)))) & (1)) == 0) goto loc_009F19CA;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4))))) & (1));
    a1 = (unsigned int)((a1) << (12));
    v_stack_m58 = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4))))) & (4));
    v_stack_p10 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4))))) & (2));
    a2 = (unsigned int)((a2) << (12));
    v_stack_m54 = (unsigned int)(a2);
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) & (0x4000ULL));
    result = (unsigned int)((result) | ((unsigned int)(a2)));
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    v_stack_m50 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0x3000ULL) goto loc_009F18ED;
loc_009F1706:
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_009F19AA;
    result = IoIsOperationSynchronous(a2, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009F19AA;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48) + 80)) & (0x4000ULL)) != 0) goto loc_009F19AA;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48);
    v_rdi = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4));
    v_r15 = 0;
    if (((v_stack_m50) & (0x2000ULL)) != 0) {
        a2 = (unsigned int)(a3) + 96;
        a1 = 288;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, a4);
        v_r15 = result;
        v_stack_m48 = result;
        v_rdi = *(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4);
    }
    a1 = v_stack_m48;
    if (v_r15 == 0) { a1 = 0; }
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (6));
    a4 = (unsigned int)((a4) << (12));
    v_rdi = (unsigned int)((v_rdi) & (1));
    v_rdi = (unsigned int)((v_rdi) << (12));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_rdi)));
    v_stack_m60 = (unsigned int)((unsigned int)(a5));
    v_stack_m68 = 0;
    v_stack_m70 = 1;
    v_stack_m78 = a1;
    result = FsRtlpRequestShareableOplock(a1, *(unsigned __int64 *)(a2 + 184), a2, a4);
    v_stack_m4C = (unsigned int)(result);
    if (v_stack_m48 == 0) goto loc_009F17DB;
    *(unsigned __int64 *)(v_stack_m48 + 40) = 0;
    *(unsigned __int64 *)(v_stack_m48 + 32) = 0;
    result = v_stack_m48;
    if (*(unsigned __int64 *)(v_stack_m48 + 40) != 0) {
        result = ObDereferenceObjectDeferDelete(*(unsigned __int64 *)(v_stack_m48 + 40), *(unsigned __int64 *)(a2 + 184), a2, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m48, a2, a2, a4);
loc_009F17DB:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009F17EE:
    if (condition_is_above_or_equal) goto loc_009F17DB;
    result = FsRtlpAttachOplockKey(0, a2, a2, a4);
    if ((unsigned int)(result) != 0) goto loc_009F17DB;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_009F18DD;
loc_009F181B:
    v_stack_pA8 = *(unsigned __int64 *)(a1);
    result = ExAcquireFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a2, a4);
    v_stack_p28 = *(unsigned __int64 *)(a2 + 24);
    v_stack_p20 = *(unsigned __int64 *)(a2 + 24);
    a4 = 0;
    result = FsRtlCheckOplockEx(a1, 0, (unsigned int)(0x30000000ULL), a4);
    v_rdi = (unsigned int)((unsigned int)(result));
    if ((unsigned int)(result) == 0) {
        a2 = result + 96;
        a1 = 288;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, a4);
        v_stack_p50 = result;
        result = a5;
        v_stack_p38 = (unsigned int)(result);
        v_stack_p30 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
        v_stack_p28 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
        result = v_stack_p50;
        v_stack_p20 = result;
        a4 = 0x10000ULL;
        a3 = 0;
        a2 = *(unsigned __int64 *)(a2 + 184);
        a1 = a1;
        result = FsRtlpRequestShareableOplock(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
    }
    if (v_stack_p50 == 0) goto loc_009F18CC;
    *(unsigned __int64 *)(v_stack_p50 + 40) = *(unsigned __int64 *)(a2 + 24);
    *(unsigned __int64 *)(v_stack_p50 + 32) = *(unsigned __int64 *)(a2 + 24);
    result = v_stack_p50;
    if (*(unsigned __int64 *)(v_stack_p50 + 40) != 0) {
        result = ObDereferenceObjectDeferDelete(*(unsigned __int64 *)(v_stack_p50 + 40), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, a2, a3, a4);
loc_009F18CC:
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a3, a4);
    goto loc_009F17DB;
loc_009F18DD:
    result = FsRtlpAllocateOplock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 152), a2, a3, a4);
    *(unsigned __int64 *)(a1) = result;
    goto loc_009F181B;
loc_009F18ED:
    if (((unsigned int)(result)) != 0x7000ULL) goto loc_009F1B6A;
loc_009F1900:
    result = IoIsOperationSynchronous(0, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009F19AA;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48) + 80)) & (0x4000ULL)) != 0) goto loc_009F19AA;
    a1 = (unsigned int)(0x4040ULL);
    if (v_stack_pA8 == ((unsigned int)(result))) { a1 = 64; }
    a1 = (unsigned int)((a1) | (v_stack_p40));
    a1 = (unsigned int)((a1) | (v_stack_p44));
    v_stack_p30 = (unsigned int)((unsigned int)(a5));
    v_stack_p28 = (unsigned int)(a1);
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_pB8));
    result = FsRtlpRequestExclusiveOplock(a1, *(unsigned __int64 *)(a2 + 184), 0, (unsigned int)((unsigned int)((unsigned int)(a3))));
loc_009F1969:
    goto loc_009F17DB;
loc_009F1970:
    result = (unsigned int)((result) + (0xFFF70000ULL));
    if (((unsigned int)(result)) > 92) goto loc_009F1B80;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 10426757 + *(unsigned __int8 *)(v_rip - 10426757 + result * 1 + 10427408) * 4 + 10427372))) + (v_rip - 10426757);
loc_009F19AA:
    *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)(0xC00000E2ULL));
loc_009F19B2:
    result = IofCompleteRequest(0, 1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))));
    goto loc_009F17DB;
loc_009F19CA:
    if ((((unsigned __int8)((unsigned int)(0xC00000E2ULL))) & ((unsigned __int8)(result))) == 0) goto loc_009F1AB2;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4))))) & (6));
    v_rdi = (unsigned int)((v_rdi) << (12));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4))))) & (1));
    result = (unsigned int)((result) << (12));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    if (((unsigned int)(v_rdi)) != 0x7000ULL) goto loc_009F1B97;
loc_009F19F7:
    result = IoIsOperationSynchronous(0, 1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))));
    if ((unsigned __int8)(result) != 0) goto loc_009F1B80;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48) + 80)) & (0x4000ULL)) != 0) goto loc_009F1BC8;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48);
    v_r12 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4));
    v_r15 = result;
    if (!(condition_is_above_or_equal)) {
        a2 = 96;
        a1 = 288;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a3))));
        v_r15 = result;
        v_stack_p50 = result;
        v_r12 = *(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 4);
    }
    a1 = v_stack_p50;
    if (v_r15 == 0) { a1 = 0; }
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (6));
    a4 = (unsigned int)((a4) << (12));
    v_r12 = (unsigned int)((v_r12) & (1));
    v_r12 = (unsigned int)((v_r12) << (12));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_r12)));
    v_stack_p28 = (unsigned int)((unsigned int)(a5));
    v_stack_p20 = a1;
    result = FsRtlpAcknowledgeOplockBreakByCacheFlags(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a2 + 184), a2, a4);
    v_stack_p4C = (unsigned int)(result);
    if (v_stack_p50 == 0) goto loc_009F17DB;
    result = FsRtlpClearOwner(*(unsigned __int64 *)(a1), v_stack_p50, a2, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, a2, a2, a4);
    goto loc_009F17DB;
loc_009F1AB2:
loc_009F1AB7:
    *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009F19B2;
loc_009F1B1A:
    goto loc_009F1AB7;
loc_009F1B6A:
    if (((unsigned int)(result)) == 0x1000ULL) goto loc_009F1706;
    if (((unsigned int)(result)) == 0x5000ULL) goto loc_009F1900;
loc_009F1B80:
    *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    result = IofCompleteRequest(0, 1, a2, a4);
    goto loc_009F17DB;
loc_009F1B97:
    if ((unsigned int)((unsigned int)(0xC000000DULL)) == 0) goto loc_009F19F7;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0x1000ULL) goto loc_009F19F7;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0x3000ULL) goto loc_009F19F7;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0x5000ULL) goto loc_009F1AB2;
    goto loc_009F19F7;
loc_009F1BC8:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 24)) = 0x180001ULL;
    *(unsigned __int64 *)(a2 + 56) = 24;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpOplockFsctrlInternal(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint8_t v_stack_m68;
    uint8_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC0;

    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r13 = 0;
    v_stack_m48 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8))) == 0) goto loc_009F17EE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18)))) != 0x90240ULL) goto loc_009F1970;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)) < 12) goto loc_009F1B1A;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)) < 24) goto loc_009F1B1A;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x18))) > 1) goto loc_009F1AB2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)))) & (1)) == 0) goto loc_009F19CA;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4))))) & (1));
    Arg1 = (uint32_t)((Arg1) << (12));
    v_stack_m58 = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4))))) & (4));
    v_stack_p10 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4))))) & (2));
    Arg2 = (uint32_t)((Arg2) << (12));
    v_stack_m54 = (uint32_t)(Arg2);
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) & (0x4000ULL));
    result = (uint32_t)((result) | ((uint32_t)(Arg2)));
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    v_stack_m50 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0x3000ULL) goto loc_009F18ED;
loc_009F1706:
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_009F19AA;
    result = IoIsOperationSynchronous(Arg2, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009F19AA;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30) + 0x50)) & (0x4000ULL)) != 0) goto loc_009F19AA;
    result = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30);
    local_rdi = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4));
    local_r15 = 0;
    if (((v_stack_m50) & (0x2000ULL)) != 0) {
        Arg2 = (uint32_t)(Arg3) + 96;
        Arg1 = 288;
        Arg3 = 0x6F725346ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, Arg4);
        local_r15 = result;
        v_stack_m48 = result;
        local_rdi = *(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4);
    }
    Arg1 = v_stack_m48;
    if (local_r15 == 0) { Arg1 = 0; }
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (6));
    Arg4 = (uint32_t)((Arg4) << (12));
    local_rdi = (uint32_t)((local_rdi) & (1));
    local_rdi = (uint32_t)((local_rdi) << (12));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_rdi)));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m68 = 0;
    v_stack_m70 = 1;
    v_stack_m78 = Arg1;
    result = FsRtlpRequestShareableOplock(Arg1, *(uint64_t *)(arg2 + 0xB8), Arg2, Arg4);
    v_stack_m4C = (uint32_t)(result);
    if (v_stack_m48 == 0) goto loc_009F17DB;
    *(uint64_t *)(v_stack_m48 + 0x28) = 0;
    *(uint64_t *)(v_stack_m48 + 0x20) = 0;
    result = v_stack_m48;
    if (*(uint64_t *)(v_stack_m48 + 0x28) != 0) {
        result = ObDereferenceObjectDeferDelete(*(uint64_t *)(v_stack_m48 + 0x28), *(uint64_t *)(arg2 + 0xB8), Arg2, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m48, Arg2, Arg2, Arg4);
loc_009F17DB:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009F17EE:
    if (condition_is_above_or_equal) goto loc_009F17DB;
    result = FsRtlpAttachOplockKey(0, Arg2, Arg2, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009F17DB;
    if (*(uint64_t *)(arg1) == 0) goto loc_009F18DD;
loc_009F181B:
    v_stack_pA8 = *(uint64_t *)(arg1);
    result = ExAcquireFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg2, Arg4);
    v_stack_p28 = *(uint64_t *)(arg2 + 0x18);
    v_stack_p20 = *(uint64_t *)(arg2 + 0x18);
    Arg4 = 0;
    result = FsRtlCheckOplockEx(Arg1, 0, (uint32_t)(0x30000000ULL), Arg4);
    local_rdi = (uint32_t)((uint32_t)(result));
    if ((uint32_t)(result) == 0) {
        Arg2 = result + 96;
        Arg1 = 288;
        Arg3 = 0x6F725346ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, Arg4);
        v_stack_p50 = result;
        result = Arg5;
        v_stack_p38 = (uint32_t)(result);
        v_stack_p30 = (uint8_t)((uint32_t)((uint32_t)(result)));
        v_stack_p28 = (uint8_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_p50;
        v_stack_p20 = result;
        Arg4 = 0x10000ULL;
        Arg3 = 0;
        Arg2 = *(uint64_t *)(arg2 + 0xB8);
        Arg1 = Arg1;
        result = FsRtlpRequestShareableOplock(Arg1, Arg2, Arg3, Arg4);
        local_rdi = (uint32_t)(result);
    }
    if (v_stack_p50 == 0) goto loc_009F18CC;
    *(uint64_t *)(v_stack_p50 + 0x28) = *(uint64_t *)(arg2 + 0x18);
    *(uint64_t *)(v_stack_p50 + 0x20) = *(uint64_t *)(arg2 + 0x18);
    result = v_stack_p50;
    if (*(uint64_t *)(v_stack_p50 + 0x28) != 0) {
        result = ObDereferenceObjectDeferDelete(*(uint64_t *)(v_stack_p50 + 0x28), Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, Arg2, Arg3, Arg4);
loc_009F18CC:
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg3, Arg4);
    goto loc_009F17DB;
loc_009F18DD:
    result = FsRtlpAllocateOplock(*(uint64_t *)(*(uint64_t *)(arg1) + 0x98), Arg2, Arg3, Arg4);
    *(uint64_t *)(arg1) = result;
    goto loc_009F181B;
loc_009F18ED:
    if (((uint32_t)(result)) != 0x7000ULL) goto loc_009F1B6A;
loc_009F1900:
    result = IoIsOperationSynchronous(0, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009F19AA;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30) + 0x50)) & (0x4000ULL)) != 0) goto loc_009F19AA;
    Arg1 = (uint32_t)(0x4040ULL);
    if (v_stack_pA8 == ((uint32_t)(result))) { Arg1 = 64; }
    Arg1 = (uint32_t)((Arg1) | (v_stack_p40));
    Arg1 = (uint32_t)((Arg1) | (v_stack_p44));
    v_stack_p30 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p28 = (uint32_t)(Arg1);
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_pB8));
    result = FsRtlpRequestExclusiveOplock(Arg1, *(uint64_t *)(arg2 + 0xB8), 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
loc_009F1969:
    goto loc_009F17DB;
loc_009F1970:
    result = (uint32_t)((result) + (0xFFF70000ULL));
    if (((uint32_t)(result)) > 92) goto loc_009F1B80;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x9F1985 + *(uint8_t *)(v_rip - 0x9F1985 + result * 1 + 0x9F1C10) * 4 + 0x9F1BEC))) + (v_rip - 10426757);
loc_009F19AA:
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)(0xC00000E2ULL));
loc_009F19B2:
    result = IofCompleteRequest(0, 1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    goto loc_009F17DB;
loc_009F19CA:
    if ((((uint8_t)((uint32_t)(0xC00000E2ULL))) & ((uint8_t)(result))) == 0) goto loc_009F1AB2;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4))))) & (6));
    local_rdi = (uint32_t)((local_rdi) << (12));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4))))) & (1));
    result = (uint32_t)((result) << (12));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    if (((uint32_t)(local_rdi)) != 0x7000ULL) goto loc_009F1B97;
loc_009F19F7:
    result = IoIsOperationSynchronous(0, 1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if ((uint8_t)(result) != 0) goto loc_009F1B80;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30) + 0x50)) & (0x4000ULL)) != 0) goto loc_009F1BC8;
    result = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x30);
    local_r12 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4));
    local_r15 = result;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 96;
        Arg1 = 288;
        Arg3 = 0x6F725346ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
        local_r15 = result;
        v_stack_p50 = result;
        local_r12 = *(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x4);
    }
    Arg1 = v_stack_p50;
    if (local_r15 == 0) { Arg1 = 0; }
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (6));
    Arg4 = (uint32_t)((Arg4) << (12));
    local_r12 = (uint32_t)((local_r12) & (1));
    local_r12 = (uint32_t)((local_r12) << (12));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_r12)));
    v_stack_p28 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p20 = Arg1;
    result = FsRtlpAcknowledgeOplockBreakByCacheFlags(*(uint64_t *)(arg1), *(uint64_t *)(arg2 + 0xB8), Arg2, Arg4);
    v_stack_p4C = (uint32_t)(result);
    if (v_stack_p50 == 0) goto loc_009F17DB;
    result = FsRtlpClearOwner(*(uint64_t *)(arg1), v_stack_p50, Arg2, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, Arg2, Arg2, Arg4);
    goto loc_009F17DB;
loc_009F1AB2:
loc_009F1AB7:
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009F19B2;
loc_009F1B1A:
    goto loc_009F1AB7;
loc_009F1B6A:
    if (((uint32_t)(result)) == 0x1000ULL) goto loc_009F1706;
    if (((uint32_t)(result)) == 0x5000ULL) goto loc_009F1900;
loc_009F1B80:
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    result = IofCompleteRequest(0, 1, Arg2, Arg4);
    goto loc_009F17DB;
loc_009F1B97:
    if ((uint32_t)((uint32_t)(0xC000000DULL)) == 0) goto loc_009F19F7;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0x1000ULL) goto loc_009F19F7;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0x3000ULL) goto loc_009F19F7;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0x5000ULL) goto loc_009F1AB2;
    goto loc_009F19F7;
loc_009F1BC8:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x18)) = 0x180001ULL;
    *(uint64_t *)(arg2 + 0x38) = 24;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F1640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
