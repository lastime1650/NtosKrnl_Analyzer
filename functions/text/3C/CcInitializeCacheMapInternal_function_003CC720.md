# CcInitializeCacheMapInternal

- RVA: `0x003CC720`–`0x003CD307` (길이 `3,047` bytes)
- VA: `0x00000001403CC720`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008F958`
- 디코드: `693`개 명령, `3,047/3,047` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **72**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x003CC826` → [ExAllocateFromLookasideListEx](ExAllocateFromLookasideListEx_function_003CD390.md) (function, `0x003CD390`)
- `0x003CC839` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003CC85E` → [MmCreateCacheManagerSection](../../page/98/MmCreateCacheManagerSection_function_00983CB8.md) (function, `0x00983CB8`)
- `0x003CC87E` → [ObDeleteCapturedInsertInfo](../../page/87/ObDeleteCapturedInsertInfo_function_00876E90.md) (function, `0x00876E90`)
- `0x003CC8A6` → [CcGetPartitionWithCreate](CcGetPartitionWithCreate_function_003CD310.md) (function, `0x003CD310`)
- `0x003CC920` → [CcInitializeVolumeCacheMap](../38/CcInitializeVolumeCacheMap_function_00389D60.md) (function, `0x00389D60`)
- `0x003CCA06` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCA45` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CCA76` → [CcGetPrivateVolumeCacheMap](../38/CcGetPrivateVolumeCacheMap_function_0038B930.md) (function, `0x0038B930`)
- `0x003CCAA2` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CCB1A` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003CCB23` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CCB3A` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCB90` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x003CCBA9` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCBB2` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCBDD` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCBF2` → [CcFreeSharedCacheMapIgnoreNull](../38/CcFreeSharedCacheMapIgnoreNull_function_0038AC8C.md) (function, `0x0038AC8C`)
- `0x003CCBFA` → [CcFreePrivateCacheMapIgnoreNull](../38/CcFreePrivateCacheMapIgnoreNull_function_0038AC64.md) (function, `0x0038AC64`)
- `0x003CCCA8` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCCB1` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCCB9` → [CcFreeSharedCacheMapIgnoreNull](../38/CcFreeSharedCacheMapIgnoreNull_function_0038AC8C.md) (function, `0x0038AC8C`)
- `0x003CCCE4` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCCF4` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCD17` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003CCD30` → [PsGetPagePriorityThread](PsGetPagePriorityThread_function_003C3E80.md) (function, `0x003C3E80`)
- `0x003CCDAB` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCDB4` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCDFA` → [CcCreateVacbArray](../../page/9F/CcCreateVacbArray_function_009FE10C.md) (function, `0x009FE10C`)
- `0x003CCE14` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCE2C` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCE4F` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CCE72` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CCEA7` → [CcNotifyWriteBehindVolume](CcNotifyWriteBehindVolume_function_003CC134.md) (function, `0x003CC134`)
- `0x003CCEC5` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CCECE` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CCEE1` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCF04` → [ExAllocateFromLookasideListEx](ExAllocateFromLookasideListEx_function_003CD390.md) (function, `0x003CD390`)
- `0x003CCF3C` → [CcCreatePrivateVolumeCacheMap](CcCreatePrivateVolumeCacheMap_function_003CDB20.md) (function, `0x003CDB20`)
- `0x003CCF66` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCF97` → [CcInsertIntoCleanSharedCacheMapList](../45/CcInsertIntoCleanSharedCacheMapList_function_004511CC.md) (function, `0x004511CC`)
- `0x003CCFAF` → [MmDisableModifiedWriteOfSection](../2B/MmDisableModifiedWriteOfSection_function_002BE290.md) (function, `0x002BE290`)
- `0x003CCFBF` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CCFCF` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CCFE0` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CCFE9` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD062` → [CcNotifyWriteBehindInternal](CcNotifyWriteBehindInternal_function_003CC224.md) (function, `0x003CC224`)
- `0x003CD096` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CD0A6` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CD0C7` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CD0DF` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CD0E9` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD144` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x003CD175` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CD185` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CD196` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CD19F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD1AE` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CD1D0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003CD1F5` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD1FE` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD218` → [CcDecrementOpenCountDeferDelete](../4B/CcDecrementOpenCountDeferDelete_function_004B7134.md) (function, `0x004B7134`)
- `0x003CD229` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD231` → [CcFreeSharedCacheMapIgnoreNull](../38/CcFreeSharedCacheMapIgnoreNull_function_0038AC8C.md) (function, `0x0038AC8C`)
- `0x003CD248` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x003CD254` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x003CD277` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CD296` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD2B4` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CD2CE` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CD2DD` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x003CD2FC` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)

### Direct callers
- [CcInitializeCacheMap](CcInitializeCacheMap_function_003CC6C0.md) at `0x003CC6D9`
- [CcInitializeCacheMapEx2](CcInitializeCacheMapEx2_function_003CC6F0.md) at `0x003CC70E`
- [CcInitializeCacheMapEx](../57/CcInitializeCacheMapEx_function_0057B1F0.md) at `0x0057B20C`

### Static image references
- `0x003CC786` → RVA `0x00E65AE0` (`.data`; read)
- `0x003CC81F` → RVA `0x00E11C60` (`.data`; read)
- `0x003CC88A` → RVA `0x00E30088` (`.data`; read)
- `0x003CC92F` → RVA `0x00E65B88` (`.data`; read)
- `0x003CC9FF` → RVA `0x00E11CC0` (`.data`; read)
- `0x003CCB3F` → RVA `0x00F475F8` (`.data`; read)
- `0x003CCEFD` → RVA `0x00E11C00` (`.data`; read)
- `0x003CD121` → RVA `0x00F475DC` (`.data`; read)
- `0x003CD13D` → RVA `0x006C7C20` (` ?? ::FNODOBFM::`string'`; read)
- `0x003CD27C` → RVA `0x00E65B40` (`.data`; read)
- `0x003CD288` → RVA `0x00E65B38` (`.data`; read)
- `0x003CD2F1` → RVA `0x00E0A848` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x003CC85E` → [MmCreateCacheManagerSection](../../page/98/MmCreateCacheManagerSection_function_00983CB8.md) (`.text` → `PAGE`)
  - `0x003CC87E` → [ObDeleteCapturedInsertInfo](../../page/87/ObDeleteCapturedInsertInfo_function_00876E90.md) (`.text` → `PAGE`)
  - `0x003CCB90` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
  - `0x003CCDFA` → [CcCreateVacbArray](../../page/9F/CcCreateVacbArray_function_009FE10C.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x003CCB7A` → [sub_006E86B0](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CCE34` → [sub_006E86B0 + 0x85](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CCE44` → [sub_006E86B0 + 0x7D](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CCE55` → [sub_006E86B0 + 0x7D](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CD1EC` → [sub_006E86B0](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CD20C` → [sub_006E86B0 + 0x5F](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CD2EB` → [sub_006E86B0 + 0xD7](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)
  - `0x003CD302` → [sub_006E86B0 + 0xD7](../6E/Unknown_function_006E86B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CC720  48 8B C4                        mov rax, rsp
003CC723  48 89 58 08                     mov qword ptr [rax + 8], rbx
003CC727  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003CC72B  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
003CC72F  55                              push rbp
003CC730  56                              push rsi
003CC731  57                              push rdi
003CC732  41 54                           push r12
003CC734  41 55                           push r13
003CC736  41 56                           push r14
003CC738  41 57                           push r15
003CC73A  48 8D 68 B9                     lea rbp, [rax - 0x47]
003CC73E  48 81 EC C0 00 00 00            sub rsp, 0xc0
003CC745  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
003CC74E  33 FF                           xor edi, edi
003CC750  4C 8B E9                        mov r13, rcx
003CC753  89 7D B7                        mov dword ptr [rbp - 0x49], edi
003CC756  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
003CC759  0F 57 C0                        xorps xmm0, xmm0
003CC75C  83 E1 FE                        and ecx, 0xfffffffe
003CC75F  89 7D 83                        mov dword ptr [rbp - 0x7d], edi
003CC762  49 8B 80 B8 00 00 00            mov rax, qword ptr [r8 + 0xb8]
003CC769  0F 57 C9                        xorps xmm1, xmm1
003CC76C  48 89 45 F7                     mov qword ptr [rbp - 9], rax
003CC770  8B DF                           mov ebx, edi
003CC772  33 C0                           xor eax, eax
003CC774  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
003CC778  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
003CC77C  44 8B F7                        mov r14d, edi
003CC77F  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
003CC783  44 8B E7                        mov r12d, edi
003CC786  8A 05 54 93 A9 00               mov al, byte ptr [rip + 0xa99354]
003CC78C  8B F7                           mov esi, edi
003CC78E  84 C0                           test al, al
003CC790  4C 89 45 FF                     mov qword ptr [rbp - 1], r8
003CC794  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
003CC798  44 8B FF                        mov r15d, edi
003CC79B  0F 44 4D 7F                     cmove ecx, dword ptr [rbp + 0x7f]
003CC79F  89 4D D3                        mov dword ptr [rbp - 0x2d], ecx
003CC7A2  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
003CC7A6  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
003CC7AB  0F 11 45 9F                     movups xmmword ptr [rbp - 0x61], xmm0
003CC7AF  0F 11 4D 87                     movups xmmword ptr [rbp - 0x79], xmm1
003CC7B3  4D 85 C9                        test r9, r9
003CC7B6  0F 85 15 09 00 00               jne 0x1403cd0d1
003CC7BC  41 B9 01 00 00 00               mov r9d, 1
003CC7C2  48 85 C0                        test rax, rax
003CC7C5  0F 85 10 03 00 00               jne 0x1403ccadb
003CC7CB  0F 10 0A                        movups xmm1, xmmword ptr [rdx]
003CC7CE  F2 0F 10 42 10                  movsd xmm0, qword ptr [rdx + 0x10]
003CC7D3  66 48 0F 7E C8                  movq rax, xmm1
003CC7D8  66 0F 7E C9                     movd ecx, xmm1
003CC7DC  48 85 C0                        test rax, rax
003CC7DF  F2 0F 11 45 EF                  movsd qword ptr [rbp - 0x11], xmm0
003CC7E4  41 8B 40 74                     mov eax, dword ptr [r8 + 0x74]
003CC7E8  41 0F 44 C9                     cmove ecx, r9d
003CC7EC  25 00 04 00 00                  and eax, 0x400
003CC7F1  89 45 CF                        mov dword ptr [rbp - 0x31], eax
003CC7F4  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
003CC7F8  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
003CC7FB  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
003CC7FF  48 05 FF FF 03 00               add rax, 0x3ffff
003CC805  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
003CC809  25 00 00 FC FF                  and eax, 0xfffc0000
003CC80E  89 45 DF                        mov dword ptr [rbp - 0x21], eax
003CC811  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
003CC815  48 39 78 08                     cmp qword ptr [rax + 8], rdi
003CC819  0F 85 DC 01 00 00               jne 0x1403cc9fb
003CC81F  48 8D 0D 3A 54 A4 00            lea rcx, [rip + 0xa4543a]
003CC826  E8 65 0B 00 00                  call 0x1403cd390
003CC82B  33 D2                           xor edx, edx
003CC82D  41 B8 68 02 00 00               mov r8d, 0x268
003CC833  48 8B C8                        mov rcx, rax
003CC836  4C 8B F0                        mov r14, rax
003CC839  E8 02 A4 2F 00                  call 0x1406c6c40
003CC83E  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
003CC842  8B CB                           mov ecx, ebx
003CC844  83 C9 01                        or ecx, 1
003CC847  4D 8B CD                        mov r9, r13
003CC84A  F6 45 D3 01                     test byte ptr [rbp - 0x2d], 1
003CC84E  49 8B FE                        mov rdi, r14
003CC851  0F 44 CB                        cmove ecx, ebx
003CC854  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
003CC857  44 8B C1                        mov r8d, ecx
003CC85A  48 8D 4D C7                     lea rcx, [rbp - 0x39]
003CC85E  E8 55 74 5B 00                  call 0x140983cb8
003CC863  8B F0                           mov esi, eax
003CC865  3D 0B 06 00 C0                  cmp eax, 0xc000060b
003CC86A  0F 84 FC 09 00 00               je 0x1403cd26c
003CC870  33 DB                           xor ebx, ebx
003CC872  85 C0                           test eax, eax
003CC874  0F 88 D8 09 00 00               js 0x1403cd252
003CC87A  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
003CC87E  E8 0D A6 4A 00                  call 0x140876e90
003CC883  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
003CC887  48 8B 08                        mov rcx, qword ptr [rax]
003CC88A  48 8B 05 F7 37 A6 00            mov rax, qword ptr [rip + 0xa637f7]
003CC891  0F B7 49 3C                     movzx ecx, word ptr [rcx + 0x3c]
003CC895  81 E1 FF 03 00 00               and ecx, 0x3ff
003CC89B  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
003CC89F  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
003CC8A6  E8 65 0A 00 00                  call 0x1403cd310
003CC8AB  4C 8B F8                        mov r15, rax
003CC8AE  48 85 C0                        test rax, rax
003CC8B1  0F 84 03 03 00 00               je 0x1403ccbba
003CC8B7  83 C8 FF                        or eax, 0xffffffff
003CC8BA  41 C7 06 FF 02 68 02            mov dword ptr [r14], 0x26802ff
003CC8C1  41 89 86 2C 02 00 00            mov dword ptr [r14 + 0x22c], eax
003CC8C8  49 8D 96 00 02 00 00            lea rdx, [r14 + 0x200]
003CC8CF  41 89 86 30 02 00 00            mov dword ptr [r14 + 0x230], eax
003CC8D6  49 8B C5                        mov rax, r13
003CC8D9  48 F7 D8                        neg rax
003CC8DC  48 1B C9                        sbb rcx, rcx
003CC8DF  49 23 CD                        and rcx, r13
003CC8E2  49 89 4E 60                     mov qword ptr [r14 + 0x60], rcx
003CC8E6  49 8B CD                        mov rcx, r13
003CC8E9  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
003CC8ED  49 89 46 08                     mov qword ptr [r14 + 8], rax
003CC8F1  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
003CC8F5  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
003CC8F9  49 89 46 30                     mov qword ptr [r14 + 0x30], rax
003CC8FD  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
003CC901  8B 80 84 03 00 00               mov eax, dword ptr [rax + 0x384]
003CC907  41 89 86 08 02 00 00            mov dword ptr [r14 + 0x208], eax
003CC90E  4D 89 BE 18 02 00 00            mov qword ptr [r14 + 0x218], r15
003CC915  41 C7 86 60 02 00 00 00 00 04 00  mov dword ptr [r14 + 0x260], 0x40000
003CC920  E8 3B D4 FB FF                  call 0x140389d60
003CC925  8B F0                           mov esi, eax
003CC927  85 C0                           test eax, eax
003CC929  0F 88 90 02 00 00               js 0x1403ccbbf
003CC92F  38 1D 53 92 A9 00               cmp byte ptr [rip + 0xa99253], bl
003CC935  0F 85 F4 05 00 00               jne 0x1403ccf2f
003CC93B  41 C7 86 20 01 00 00 01 00 00 00  mov dword ptr [r14 + 0x120], 1
003CC946  49 8D 86 40 01 00 00            lea rax, [r14 + 0x140]
003CC94D  33 FF                           xor edi, edi
003CC94F  49 89 BE 28 01 00 00            mov qword ptr [r14 + 0x128], rdi
003CC956  41 89 BE 30 01 00 00            mov dword ptr [r14 + 0x130], edi
003CC95D  66 41 C7 86 38 01 00 00 01 00   mov word ptr [r14 + 0x138], 1
003CC967  41 C6 86 3A 01 00 00 06         mov byte ptr [r14 + 0x13a], 6
003CC96F  41 89 BE 3C 01 00 00            mov dword ptr [r14 + 0x13c], edi
003CC976  48 89 40 08                     mov qword ptr [rax + 8], rax
003CC97A  48 89 00                        mov qword ptr [rax], rax
003CC97D  49 89 7E 68                     mov qword ptr [r14 + 0x68], rdi
003CC981  40 38 7D 5F                     cmp byte ptr [rbp + 0x5f], dil
003CC985  0F 85 F7 02 00 00               jne 0x1403ccc82
003CC98B  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
003CC98F  A8 20                           test al, 0x20
003CC991  0F 85 F8 02 00 00               jne 0x1403ccc8f
003CC997  39 7D CF                        cmp dword ptr [rbp - 0x31], edi
003CC99A  75 09                           jne 0x1403cc9a5
003CC99C  41 0F BA AE 98 00 00 00 15      bts dword ptr [r14 + 0x98], 0x15
003CC9A5  48 8B 5D 67                     mov rbx, qword ptr [rbp + 0x67]
003CC9A9  49 8D 46 10                     lea rax, [r14 + 0x10]
003CC9AD  48 89 40 08                     mov qword ptr [rax + 8], rax
003CC9B1  48 89 00                        mov qword ptr [rax], rax
003CC9B4  41 8B 8E 9C 00 00 00            mov ecx, dword ptr [r14 + 0x9c]
003CC9BB  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
003CC9BF  49 89 86 E0 00 00 00            mov qword ptr [r14 + 0xe0], rax
003CC9C6  8B C1                           mov eax, ecx
003CC9C8  83 C8 01                        or eax, 1
003CC9CB  83 E1 FE                        and ecx, 0xfffffffe
003CC9CE  48 85 DB                        test rbx, rbx
003CC9D1  0F 44 C8                        cmove ecx, eax
003CC9D4  48 8B C3                        mov rax, rbx
003CC9D7  48 0F 44 45 6F                  cmove rax, qword ptr [rbp + 0x6f]
003CC9DC  8B 5D D7                        mov ebx, dword ptr [rbp - 0x29]
003CC9DF  41 89 8E 9C 00 00 00            mov dword ptr [r14 + 0x9c], ecx
003CC9E6  49 89 86 D8 00 00 00            mov qword ptr [r14 + 0xd8], rax
003CC9ED  49 8D 86 E8 00 00 00            lea rax, [r14 + 0xe8]
003CC9F4  48 89 40 08                     mov qword ptr [rax + 8], rax
003CC9F8  48 89 00                        mov qword ptr [rax], rax
003CC9FB  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CC9FF  48 8D 0D BA 52 A4 00            lea rcx, [rip + 0xa452ba]
003CCA06  E8 95 8D EA FF                  call 0x1402757a0
003CCA0B  49 39 7D 30                     cmp qword ptr [r13 + 0x30], rdi
003CCA0F  0F 85 10 08 00 00               jne 0x1403cd225
003CCA15  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
003CCA19  33 D2                           xor edx, edx
003CCA1B  48 8B 78 08                     mov rdi, qword ptr [rax + 8]
003CCA1F  48 85 FF                        test rdi, rdi
003CCA22  75 48                           jne 0x1403cca6c
003CCA24  4D 85 F6                        test r14, r14
003CCA27  0F 84 B8 06 00 00               je 0x1403cd0e5
003CCA2D  49 8B FE                        mov rdi, r14
003CCA30  44 8B F2                        mov r14d, edx
003CCA33  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCA37  48 8B 9F 18 02 00 00            mov rbx, qword ptr [rdi + 0x218]
003CCA3E  48 8D 8B 00 03 00 00            lea rcx, [rbx + 0x300]
003CCA45  E8 F6 8C EA FF                  call 0x140275740
003CCA4A  48 81 C3 80 02 00 00            add rbx, 0x280
003CCA51  48 8D 87 88 00 00 00            lea rax, [rdi + 0x88]
003CCA58  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
003CCA5C  48 39 19                        cmp qword ptr [rcx], rbx
003CCA5F  0F 84 A7 05 00 00               je 0x1403cd00c
003CCA65  B9 03 00 00 00                  mov ecx, 3
003CCA6A  CD 29                           int 0x29
003CCA6C  4C 8B BF 18 02 00 00            mov r15, qword ptr [rdi + 0x218]
003CCA73  48 8B CF                        mov rcx, rdi
003CCA76  E8 B5 EE FB FF                  call 0x14038b930
003CCA7B  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
003CCA82  48 8B D8                        mov rbx, rax
003CCA85  48 85 C9                        test rcx, rcx
003CCA88  74 0D                           je 0x1403cca97
003CCA8A  48 8B 49 48                     mov rcx, qword ptr [rcx + 0x48]
003CCA8E  48 85 C9                        test rcx, rcx
003CCA91  0F 85 C3 03 00 00               jne 0x1403cce5a
003CCA97  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCA9E  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCAA2  E8 99 8C EA FF                  call 0x140275740
003CCAA7  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
003CCAAB  A8 20                           test al, 0x20
003CCAAD  0F 84 3E 04 00 00               je 0x1403ccef1
003CCAB3  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
003CCAB9  33 DB                           xor ebx, ebx
003CCABB  0F BA E0 15                     bt eax, 0x15
003CCABF  0F 82 44 06 00 00               jb 0x1403cd109
003CCAC5  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
003CCAC9  8B 80 84 03 00 00               mov eax, dword ptr [rax + 0x384]
003CCACF  85 C0                           test eax, eax
003CCAD1  74 4C                           je 0x1403ccb1f
003CCAD3  89 87 08 02 00 00               mov dword ptr [rdi + 0x208], eax
003CCAD9  EB 44                           jmp 0x1403ccb1f
003CCADB  66 44 39 08                     cmp word ptr [rax], r9w
003CCADF  0F 85 F5 05 00 00               jne 0x1403cd0da
003CCAE5  66 83 78 02 28                  cmp word ptr [rax + 2], 0x28
003CCAEA  0F 84 DB FC FF FF               je 0x1403cc7cb
003CCAF0  E9 E5 05 00 00                  jmp 0x1403cd0da
003CCAF5  48 89 01                        mov qword ptr [rcx], rax
003CCAF8  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003CCAFC  48 89 0A                        mov qword ptr [rdx], rcx
003CCAFF  48 89 48 08                     mov qword ptr [rax + 8], rcx
003CCB03  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
003CCB07  BA 44 66 6C 74                  mov edx, 0x746c6644
003CCB0C  49 8B CD                        mov rcx, r13
003CCB0F  C7 45 83 01 00 00 00            mov dword ptr [rbp - 0x7d], 1
003CCB16  48 89 78 08                     mov qword ptr [rax + 8], rdi
003CCB1A  E8 F1 3B E4 FF                  call 0x140210710
003CCB1F  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCB23  E8 88 A6 E4 FF                  call 0x1402171b0
003CCB28  4C 8B BF 18 02 00 00            mov r15, qword ptr [rdi + 0x218]
003CCB2F  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCB33  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCB3A  E8 61 8C EA FF                  call 0x1402757a0
003CCB3F  38 1D B3 AA B7 00               cmp byte ptr [rip + 0xb7aab3], bl
003CCB45  0F 85 D6 05 00 00               jne 0x1403cd121
003CCB4B  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
003CCB51  B9 00 01 00 00                  mov ecx, 0x100
003CCB56  83 E0 EF                        and eax, 0xffffffef
003CCB59  89 87 98 00 00 00               mov dword ptr [rdi + 0x98], eax
003CCB5F  23 C1                           and eax, ecx
003CCB61  48 39 5F 58                     cmp qword ptr [rdi + 0x58], rbx
003CCB65  0F 84 16 02 00 00               je 0x1403ccd81
003CCB6B  85 C0                           test eax, eax
003CCB6D  0F 84 29 01 00 00               je 0x1403ccc9c
003CCB73  48 39 9F B8 00 00 00            cmp qword ptr [rdi + 0xb8], rbx
003CCB7A  0F 85 30 BB 31 00               jne 0x1406e86b0
003CCB80  BA 18 00 00 00                  mov edx, 0x18
003CCB85  B9 00 02 00 00                  mov ecx, 0x200
003CCB8A  41 B8 43 63 45 76               mov r8d, 0x76456343
003CCB90  E8 7B 54 7B 00                  call 0x140b82010
003CCB95  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
003CCB9C  48 85 C0                        test rax, rax
003CCB9F  0F 85 31 06 00 00               jne 0x1403cd1d6
003CCBA5  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCBA9  E8 32 61 F7 FF                  call 0x140342ce0
003CCBAE  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CCBB2  E8 29 61 F7 FF                  call 0x140342ce0
003CCBB7  44 8B E3                        mov r12d, ebx
003CCBBA  BE 9A 00 00 C0                  mov esi, 0xc000009a
003CCBBF  8B 45 83                        mov eax, dword ptr [rbp - 0x7d]
003CCBC2  33 D2                           xor edx, edx
003CCBC4  89 45 83                        mov dword ptr [rbp - 0x7d], eax
003CCBC7  41 8B CC                        mov ecx, r12d
003CCBCA  44 8B EB                        mov r13d, ebx
003CCBCD  48 85 FF                        test rdi, rdi
003CCBD0  75 5E                           jne 0x1403ccc30
003CCBD2  33 DB                           xor ebx, ebx
003CCBD4  45 85 ED                        test r13d, r13d
003CCBD7  74 09                           je 0x1403ccbe2
003CCBD9  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCBDD  E8 FE 60 F7 FF                  call 0x140342ce0
003CCBE2  45 85 E4                        test r12d, r12d
003CCBE5  0F 85 DF 06 00 00               jne 0x1403cd2ca
003CCBEB  4C 8B 65 BF                     mov r12, qword ptr [rbp - 0x41]
003CCBEF  49 8B CE                        mov rcx, r14
003CCBF2  E8 95 E0 FB FF                  call 0x14038ac8c
003CCBF7  49 8B CC                        mov rcx, r12
003CCBFA  E8 65 E0 FB FF                  call 0x14038ac64
003CCBFF  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
003CCC03  48 85 C9                        test rcx, rcx
003CCC06  0F 85 CC 06 00 00               jne 0x1403cd2d8
003CCC0C  85 F6                           test esi, esi
003CCC0E  0F 88 D3 06 00 00               js 0x1403cd2e7
003CCC14  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
003CCC1C  48 81 C4 C0 00 00 00            add rsp, 0xc0
003CCC23  41 5F                           pop r15
003CCC25  41 5E                           pop r14
003CCC27  41 5D                           pop r13
003CCC29  41 5C                           pop r12
003CCC2B  5F                              pop rdi
003CCC2C  5E                              pop rsi
003CCC2D  5D                              pop rbp
003CCC2E  C3                              ret
003CCC2F  CC                              int3
003CCC30  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
003CCC34  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
003CCC38  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
003CCC3C  85 C9                           test ecx, ecx
003CCC3E  0F 84 92 02 00 00               je 0x1403cced6
003CCC44  89 5D 67                        mov dword ptr [rbp + 0x67], ebx
003CCC47  44 8B EB                        mov r13d, ebx
003CCC4A  4D 85 FF                        test r15, r15
003CCC4D  0F 85 FD 02 00 00               jne 0x1403ccf50
003CCC53  33 DB                           xor ebx, ebx
003CCC55  39 5D 83                        cmp dword ptr [rbp - 0x7d], ebx
003CCC58  0F 84 24 03 00 00               je 0x1403ccf82
003CCC5E  48 8B 8F 18 01 00 00            mov rcx, qword ptr [rdi + 0x118]
003CCC65  48 85 C9                        test rcx, rcx
003CCC68  0F 85 36 06 00 00               jne 0x1403cd2a4
003CCC6E  0F BA B7 98 00 00 00 10         btr dword ptr [rdi + 0x98], 0x10
003CCC76  48 89 9F 18 01 00 00            mov qword ptr [rdi + 0x118], rbx
003CCC7D  E9 52 FF FF FF                  jmp 0x1403ccbd4
003CCC82  41 83 8E 98 00 00 00 04         or dword ptr [r14 + 0x98], 4
003CCC8A  E9 FC FC FF FF                  jmp 0x1403cc98b
003CCC8F  41 83 8E 98 00 00 00 40         or dword ptr [r14 + 0x98], 0x40
003CCC97  E9 FB FC FF FF                  jmp 0x1403cc997
003CCC9C  8B 47 04                        mov eax, dword ptr [rdi + 4]
003CCC9F  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCCA3  FF C0                           inc eax
003CCCA5  89 47 04                        mov dword ptr [rdi + 4], eax
003CCCA8  E8 33 60 F7 FF                  call 0x140342ce0
003CCCAD  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CCCB1  E8 2A 60 F7 FF                  call 0x140342ce0
003CCCB6  49 8B CE                        mov rcx, r14
003CCCB9  E8 CE DF FB FF                  call 0x14038ac8c
003CCCBE  4C 8B F3                        mov r14, rbx
003CCCC1  33 C0                           xor eax, eax
003CCCC3  48 8D 9F 80 01 00 00            lea rbx, [rdi + 0x180]
003CCCCA  66 39 03                        cmp word ptr [rbx], ax
003CCCCD  0F 85 2A 02 00 00               jne 0x1403ccefd
003CCCD3  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CCCD7  41 BC 01 00 00 00               mov r12d, 1
003CCCDD  48 8D 0D DC 4F A4 00            lea rcx, [rip + 0xa44fdc]
003CCCE4  E8 B7 8A EA FF                  call 0x1402757a0
003CCCE9  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCCF0  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCCF4  E8 A7 8A EA FF                  call 0x1402757a0
003CCCF9  33 D2                           xor edx, edx
003CCCFB  49 39 55 30                     cmp qword ptr [r13 + 0x30], rdx
003CCCFF  0F 85 03 05 00 00               jne 0x1403cd208
003CCD05  66 39 13                        cmp word ptr [rbx], dx
003CCD08  0F 85 E5 02 00 00               jne 0x1403ccff3
003CCD0E  41 B8 78 00 00 00               mov r8d, 0x78
003CCD14  48 8B CB                        mov rcx, rbx
003CCD17  E8 24 9F 2F 00                  call 0x1406c6c40
003CCD1C  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
003CCD20  66 C7 03 FE 02                  mov word ptr [rbx], 0x2fe
003CCD25  4C 89 6B 08                     mov qword ptr [rbx + 8], r13
003CCD29  C7 43 04 FF 0F 00 00            mov dword ptr [rbx + 4], 0xfff
003CCD30  E8 4B 71 FF FF                  call 0x1403c3e80
003CCD35  0F B6 C8                        movzx ecx, al
003CCD38  8B 03                           mov eax, dword ptr [rbx]
003CCD3A  C1 E1 12                        shl ecx, 0x12
003CCD3D  33 C8                           xor ecx, eax
003CCD3F  81 E1 00 00 1C 00               and ecx, 0x1c0000
003CCD45  33 C8                           xor ecx, eax
003CCD47  33 C0                           xor eax, eax
003CCD49  89 0B                           mov dword ptr [rbx], ecx
003CCD4B  48 8D 8F E8 00 00 00            lea rcx, [rdi + 0xe8]
003CCD52  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
003CCD56  48 8D 43 60                     lea rax, [rbx + 0x60]
003CCD5A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
003CCD5E  48 39 0A                        cmp qword ptr [rdx], rcx
003CCD61  0F 85 FE FC FF FF               jne 0x1403cca65
003CCD67  48 89 08                        mov qword ptr [rax], rcx
003CCD6A  48 89 50 08                     mov qword ptr [rax + 8], rdx
003CCD6E  48 89 02                        mov qword ptr [rdx], rax
003CCD71  48 89 41 08                     mov qword ptr [rcx + 8], rax
003CCD75  49 89 5D 30                     mov qword ptr [r13 + 0x30], rbx
003CCD79  41 8B DC                        mov ebx, r12d
003CCD7C  E9 3E FE FF FF                  jmp 0x1403ccbbf
003CCD81  85 C0                           test eax, eax
003CCD83  0F 85 EA FD FF FF               jne 0x1403ccb73
003CCD89  8B 47 04                        mov eax, dword ptr [rdi + 4]
003CCD8C  FF C0                           inc eax
003CCD8E  89 47 04                        mov dword ptr [rdi + 4], eax
003CCD91  09 8F 98 00 00 00               or dword ptr [rdi + 0x98], ecx
003CCD97  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
003CCD9E  48 85 C0                        test rax, rax
003CCDA1  0F 85 A8 03 00 00               jne 0x1403cd14f
003CCDA7  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCDAB  E8 30 5F F7 FF                  call 0x140342ce0
003CCDB0  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CCDB4  E8 27 5F F7 FF                  call 0x140342ce0
003CCDB9  C7 45 B7 01 00 00 00            mov dword ptr [rbp - 0x49], 1
003CCDC0  48 39 9F B0 00 00 00            cmp qword ptr [rdi + 0xb0], rbx
003CCDC7  0F 85 AB 01 00 00               jne 0x1403ccf78
003CCDCD  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
003CCDD1  48 85 C0                        test rax, rax
003CCDD4  0F 84 DE 03 00 00               je 0x1403cd1b8
003CCDDA  48 89 87 B0 00 00 00            mov qword ptr [rdi + 0xb0], rax
003CCDE1  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
003CCDE5  48 89 5D C7                     mov qword ptr [rbp - 0x39], rbx
003CCDE9  F6 40 06 01                     test byte ptr [rax + 6], 1
003CCDED  0F 84 AE 01 00 00               je 0x1403ccfa1
003CCDF3  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
003CCDF7  48 8B CF                        mov rcx, rdi
003CCDFA  E8 0D 13 63 00                  call 0x1409fe10c
003CCDFF  8B F0                           mov esi, eax
003CCE01  85 C0                           test eax, eax
003CCE03  0F 89 78 02 00 00               jns 0x1403cd081
003CCE09  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CCE0D  48 8D 0D AC 4E A4 00            lea rcx, [rip + 0xa44eac]
003CCE14  E8 87 89 EA FF                  call 0x1402757a0
003CCE19  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
003CCE1D  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCE24  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCE28  88 44 24 30                     mov byte ptr [rsp + 0x30], al
003CCE2C  E8 6F 89 EA FF                  call 0x1402757a0
003CCE31  39 5D B7                        cmp dword ptr [rbp - 0x49], ebx
003CCE34  0F 84 FB B8 31 00               je 0x1406e8735
003CCE3A  48 8B 8F B8 00 00 00            mov rcx, qword ptr [rdi + 0xb8]
003CCE41  48 85 C9                        test rcx, rcx
003CCE44  0F 84 E3 B8 31 00               je 0x1406e872d
003CCE4A  45 33 C0                        xor r8d, r8d
003CCE4D  33 D2                           xor edx, edx
003CCE4F  E8 BC 24 F7 FF                  call 0x14033f310
003CCE54  90                              nop
003CCE55  E9 D3 B8 31 00                  jmp 0x1406e872d
003CCE5A  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
003CCE5E  48 39 01                        cmp qword ptr [rcx], rax
003CCE61  0F 84 30 FC FF FF               je 0x1403cca97
003CCE67  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCE6E  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCE72  E8 C9 88 EA FF                  call 0x140275740
003CCE77  8B 47 04                        mov eax, dword ptr [rdi + 4]
003CCE7A  85 C0                           test eax, eax
003CCE7C  0F 85 71 02 00 00               jne 0x1403cd0f3
003CCE82  44 38 25 FF 8C A9 00            cmp byte ptr [rip + 0xa98cff], r12b
003CCE89  BE D8 00 00 C0                  mov esi, 0xc00000d8
003CCE8E  0F 84 BA 01 00 00               je 0x1403cd04e
003CCE94  8A 83 94 04 00 00               mov al, byte ptr [rbx + 0x494]
003CCE9A  48 8B CB                        mov rcx, rbx
003CCE9D  F6 D8                           neg al
003CCE9F  1B D2                           sbb edx, edx
003CCEA1  83 E2 0C                        and edx, 0xc
003CCEA4  83 C2 04                        add edx, 4
003CCEA7  E8 88 F2 FF FF                  call 0x1403cc134
003CCEAC  44 38 A3 94 04 00 00            cmp byte ptr [rbx + 0x494], r12b
003CCEB3  75 07                           jne 0x1403ccebc
003CCEB5  C6 83 D9 03 00 00 01            mov byte ptr [rbx + 0x3d9], 1
003CCEBC  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
003CCEC1  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCEC5  E8 E6 A2 E4 FF                  call 0x1402171b0
003CCECA  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CCECE  E8 0D 5E F7 FF                  call 0x140342ce0
003CCED3  41 8B DC                        mov ebx, r12d
003CCED6  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CCEDA  48 8D 0D DF 4D A4 00            lea rcx, [rip + 0xa44ddf]
003CCEE1  E8 BA 88 EA FF                  call 0x1402757a0
003CCEE6  41 BC 01 00 00 00               mov r12d, 1
003CCEEC  E9 53 FD FF FF                  jmp 0x1403ccc44
003CCEF1  83 A7 98 00 00 00 BF            and dword ptr [rdi + 0x98], 0xffffffbf
003CCEF8  E9 B6 FB FF FF                  jmp 0x1403ccab3
003CCEFD  48 8D 0D FC 4C A4 00            lea rcx, [rip + 0xa44cfc]
003CCF04  E8 87 04 00 00                  call 0x1403cd390
003CCF09  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
003CCF0D  4C 8B E0                        mov r12, rax
003CCF10  48 85 C0                        test rax, rax
003CCF13  0F 85 BA FD FF FF               jne 0x1403cccd3
003CCF19  33 DB                           xor ebx, ebx
003CCF1B  BE 9A 00 00 C0                  mov esi, 0xc000009a
003CCF20  89 5D B7                        mov dword ptr [rbp - 0x49], ebx
003CCF23  44 8B F3                        mov r14d, ebx
003CCF26  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
003CCF2A  E9 DA FE FF FF                  jmp 0x1403cce09
003CCF2F  4D 8D 86 58 02 00 00            lea r8, [r14 + 0x258]
003CCF36  49 8B D6                        mov rdx, r14
003CCF39  49 8B CF                        mov rcx, r15
003CCF3C  E8 DF 0B 00 00                  call 0x1403cdb20
003CCF41  8B F0                           mov esi, eax
003CCF43  85 C0                           test eax, eax
003CCF45  0F 89 F0 F9 FF FF               jns 0x1403cc93b
003CCF4B  E9 6F FC FF FF                  jmp 0x1403ccbbf
003CCF50  89 5D 67                        mov dword ptr [rbp + 0x67], ebx
003CCF53  85 DB                           test ebx, ebx
003CCF55  0F 85 F8 FC FF FF               jne 0x1403ccc53
003CCF5B  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCF62  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCF66  E8 35 88 EA FF                  call 0x1402757a0
003CCF6B  44 8D 6B 01                     lea r13d, [rbx + 1]
003CCF6F  44 89 6D 67                     mov dword ptr [rbp + 0x67], r13d
003CCF73  E9 DB FC FF FF                  jmp 0x1403ccc53
003CCF78  BE 0D 00 00 C0                  mov esi, 0xc000000d
003CCF7D  E9 87 FE FF FF                  jmp 0x1403cce09
003CCF82  39 5F 70                        cmp dword ptr [rdi + 0x70], ebx
003CCF85  0F 85 D3 FC FF FF               jne 0x1403ccc5e
003CCF8B  39 5F 04                        cmp dword ptr [rdi + 4], ebx
003CCF8E  0F 84 CA FC FF FF               je 0x1403ccc5e
003CCF94  48 8B CF                        mov rcx, rdi
003CCF97  E8 30 42 08 00                  call 0x1404511cc
003CCF9C  E9 BD FC FF FF                  jmp 0x1403ccc5e
003CCFA1  49 39 5D 20                     cmp qword ptr [r13 + 0x20], rbx
003CCFA5  0F 85 48 FE FF FF               jne 0x1403ccdf3
003CCFAB  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003CCFAF  E8 DC 12 EF FF                  call 0x1402be290
003CCFB4  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CCFB8  48 8D 0D 01 4D A4 00            lea rcx, [rip + 0xa44d01]
003CCFBF  E8 DC 87 EA FF                  call 0x1402757a0
003CCFC4  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CCFCB  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CCFCF  E8 6C 87 EA FF                  call 0x140275740
003CCFD4  0F BA AF 98 00 00 00 09         bts dword ptr [rdi + 0x98], 9
003CCFDC  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CCFE0  E8 CB A1 E4 FF                  call 0x1402171b0
003CCFE5  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CCFE9  E8 F2 5C F7 FF                  call 0x140342ce0
003CCFEE  E9 00 FE FF FF                  jmp 0x1403ccdf3
003CCFF3  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
003CCFF7  48 85 C0                        test rax, rax
003CCFFA  0F 84 F1 01 00 00               je 0x1403cd1f1
003CD000  48 8B D8                        mov rbx, rax
003CD003  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
003CD007  E9 02 FD FF FF                  jmp 0x1403ccd0e
003CD00C  48 89 18                        mov qword ptr [rax], rbx
003CD00F  48 89 48 08                     mov qword ptr [rax + 8], rcx
003CD013  48 89 01                        mov qword ptr [rcx], rax
003CD016  48 89 43 08                     mov qword ptr [rbx + 8], rax
003CD01A  33 DB                           xor ebx, ebx
003CD01C  38 1D 66 8B A9 00               cmp byte ptr [rip + 0xa98b66], bl
003CD022  0F 84 DB FA FF FF               je 0x1403ccb03
003CD028  48 8B 87 58 02 00 00            mov rax, qword ptr [rdi + 0x258]
003CD02F  48 8D 8F 38 02 00 00            lea rcx, [rdi + 0x238]
003CD036  48 05 60 02 00 00               add rax, 0x260
003CD03C  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003CD040  48 39 02                        cmp qword ptr [rdx], rax
003CD043  0F 85 1C FA FF FF               jne 0x1403cca65
003CD049  E9 A7 FA FF FF                  jmp 0x1403ccaf5
003CD04E  41 8A 87 0C 05 00 00            mov al, byte ptr [r15 + 0x50c]
003CD055  49 8B CF                        mov rcx, r15
003CD058  F6 D8                           neg al
003CD05A  1B D2                           sbb edx, edx
003CD05C  83 E2 0C                        and edx, 0xc
003CD05F  83 C2 04                        add edx, 4
003CD062  E8 BD F1 FF FF                  call 0x1403cc224
003CD067  45 38 A7 0C 05 00 00            cmp byte ptr [r15 + 0x50c], r12b
003CD06E  0F 85 48 FE FF FF               jne 0x1403ccebc
003CD074  41 C6 87 19 04 00 00 01         mov byte ptr [r15 + 0x419], 1
003CD07C  E9 3B FE FF FF                  jmp 0x1403ccebc
003CD081  F6 45 D3 01                     test byte ptr [rbp - 0x2d], 1
003CD085  0F 85 DF 00 00 00               jne 0x1403cd16a
003CD08B  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CD08F  48 8D 0D 2A 4C A4 00            lea rcx, [rip + 0xa44c2a]
003CD096  E8 05 87 EA FF                  call 0x1402757a0
003CD09B  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CD0A2  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CD0A6  E8 95 86 EA FF                  call 0x140275740
003CD0AB  48 8B 8F B8 00 00 00            mov rcx, qword ptr [rdi + 0xb8]
003CD0B2  0F BA B7 98 00 00 00 08         btr dword ptr [rdi + 0x98], 8
003CD0BA  48 85 C9                        test rcx, rcx
003CD0BD  0F 85 E6 00 00 00               jne 0x1403cd1a9
003CD0C3  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CD0C7  E8 E4 A0 E4 FF                  call 0x1402171b0
003CD0CC  E9 DC FB FF FF                  jmp 0x1403cccad
003CD0D1  48 85 C0                        test rax, rax
003CD0D4  0F 84 E2 F6 FF FF               je 0x1403cc7bc
003CD0DA  B9 0D 00 00 C0                  mov ecx, 0xc000000d
003CD0DF  E8 6C 99 F2 FF                  call 0x1402f6a50
003CD0E4  CC                              int3
003CD0E5  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD0E9  E8 F2 5B F7 FF                  call 0x140342ce0
003CD0EE  E9 2C F7 FF FF                  jmp 0x1403cc81f
003CD0F3  3B 87 20 02 00 00               cmp eax, dword ptr [rdi + 0x220]
003CD0F9  0F 84 83 FD FF FF               je 0x1403cce82
003CD0FF  BE 0B 06 00 C0                  mov esi, 0xc000060b
003CD104  E9 B8 FD FF FF                  jmp 0x1403ccec1
003CD109  39 5D CF                        cmp dword ptr [rbp - 0x31], ebx
003CD10C  0F 84 B3 F9 FF FF               je 0x1403ccac5
003CD112  0F BA F0 15                     btr eax, 0x15
003CD116  89 87 98 00 00 00               mov dword ptr [rdi + 0x98], eax
003CD11C  E9 A4 F9 FF FF                  jmp 0x1403ccac5
003CD121  38 1D B5 A4 B7 00               cmp byte ptr [rip + 0xb7a4b5], bl
003CD127  0F 85 1E FA FF FF               jne 0x1403ccb4b
003CD12D  F7 87 98 00 00 00 00 00 08 00   test dword ptr [rdi + 0x98], 0x80000
003CD137  0F 84 0E FA FF FF               je 0x1403ccb4b
003CD13D  48 8D 0D DC AA 2F 00            lea rcx, [rip + 0x2faadc]
003CD144  E8 67 BB F8 FF                  call 0x140358cb0
003CD149  CC                              int3
003CD14A  E9 FC F9 FF FF                  jmp 0x1403ccb4b
003CD14F  66 44 89 20                     mov word ptr [rax], r12w
003CD153  C6 40 02 06                     mov byte ptr [rax + 2], 6
003CD157  89 58 04                        mov dword ptr [rax + 4], ebx
003CD15A  48 83 C0 08                     add rax, 8
003CD15E  48 89 40 08                     mov qword ptr [rax + 8], rax
003CD162  48 89 00                        mov qword ptr [rax], rax
003CD165  E9 3D FC FF FF                  jmp 0x1403ccda7
003CD16A  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CD16E  48 8D 0D 4B 4B A4 00            lea rcx, [rip + 0xa44b4b]
003CD175  E8 26 86 EA FF                  call 0x1402757a0
003CD17A  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CD181  48 8D 55 87                     lea rdx, [rbp - 0x79]
003CD185  E8 B6 85 EA FF                  call 0x140275740
003CD18A  0F BA AF 98 00 00 00 1E         bts dword ptr [rdi + 0x98], 0x1e
003CD192  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CD196  E8 15 A0 E4 FF                  call 0x1402171b0
003CD19B  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD19F  E8 3C 5B F7 FF                  call 0x140342ce0
003CD1A4  E9 E2 FE FF FF                  jmp 0x1403cd08b
003CD1A9  45 33 C0                        xor r8d, r8d
003CD1AC  33 D2                           xor edx, edx
003CD1AE  E8 5D 21 F7 FF                  call 0x14033f310
003CD1B3  E9 0B FF FF FF                  jmp 0x1403cd0c3
003CD1B8  45 33 C9                        xor r9d, r9d
003CD1BB  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003CD1C0  BA CC 08 00 00                  mov edx, 0x8cc
003CD1C5  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CD1CC  41 8D 49 34                     lea ecx, [r9 + 0x34]
003CD1D0  E8 8B 04 13 00                  call 0x1404fd660
003CD1D5  CC                              int3
003CD1D6  66 44 89 20                     mov word ptr [rax], r12w
003CD1DA  C6 40 02 06                     mov byte ptr [rax + 2], 6
003CD1DE  89 58 04                        mov dword ptr [rax + 4], ebx
003CD1E1  48 83 C0 08                     add rax, 8
003CD1E5  48 89 40 08                     mov qword ptr [rax + 8], rax
003CD1E9  48 89 00                        mov qword ptr [rax], rax
003CD1EC  E9 BF B4 31 00                  jmp 0x1406e86b0
003CD1F1  48 8D 4D 87                     lea rcx, [rbp - 0x79]
003CD1F5  E8 E6 5A F7 FF                  call 0x140342ce0
003CD1FA  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD1FE  E8 DD 5A F7 FF                  call 0x140342ce0
003CD203  E9 F5 FC FF FF                  jmp 0x1403ccefd
003CD208  44 39 67 04                     cmp dword ptr [rdi + 4], r12d
003CD20C  0F 86 FD B4 31 00               jbe 0x1406e870f
003CD212  45 33 C0                        xor r8d, r8d
003CD215  48 8B CF                        mov rcx, rdi
003CD218  E8 17 9F 0E 00                  call 0x1404b7134
003CD21D  48 8B FA                        mov rdi, rdx
003CD220  E9 54 FB FF FF                  jmp 0x1403ccd79
003CD225  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD229  E8 B2 5A F7 FF                  call 0x140342ce0
003CD22E  49 8B CE                        mov rcx, r14
003CD231  E8 56 DA FB FF                  call 0x14038ac8c
003CD236  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
003CD23A  48 85 C9                        test rcx, rcx
003CD23D  0F 84 D1 F9 FF FF               je 0x1403ccc14
003CD243  BA 44 66 6C 74                  mov edx, 0x746c6644
003CD248  E8 53 6C E9 FF                  call 0x140263ea0
003CD24D  E9 C2 F9 FF FF                  jmp 0x1403ccc14
003CD252  8B CE                           mov ecx, esi
003CD254  E8 37 01 EA FF                  call 0x14026d390
003CD259  8B CE                           mov ecx, esi
003CD25B  84 C0                           test al, al
003CD25D  BE EA 00 00 C0                  mov esi, 0xc00000ea
003CD262  0F 44 CE                        cmove ecx, esi
003CD265  8B F1                           mov esi, ecx
003CD267  E9 53 F9 FF FF                  jmp 0x1403ccbbf
003CD26C  48 8D 55 9F                     lea rdx, [rbp - 0x61]
003CD270  48 8D 0D 49 4A A4 00            lea rcx, [rip + 0xa44a49]
003CD277  E8 24 85 EA FF                  call 0x1402757a0
003CD27C  48 8B 05 BD 88 A9 00            mov rax, qword ptr [rip + 0xa988bd]
003CD283  B9 08 A0 00 C0                  mov ecx, 0xc000a008
003CD288  48 39 05 A9 88 A9 00            cmp qword ptr [rip + 0xa988a9], rax
003CD28F  0F 45 F1                        cmovne esi, ecx
003CD292  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD296  E8 45 5A F7 FF                  call 0x140342ce0
003CD29B  33 C0                           xor eax, eax
003CD29D  8B D8                           mov ebx, eax
003CD29F  E9 1B F9 FF FF                  jmp 0x1403ccbbf
003CD2A4  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
003CD2A8  45 33 C0                        xor r8d, r8d
003CD2AB  33 D2                           xor edx, edx
003CD2AD  48 8B 19                        mov rbx, qword ptr [rcx]
003CD2B0  48 83 C1 08                     add rcx, 8
003CD2B4  E8 57 20 F7 FF                  call 0x14033f310
003CD2B9  48 8B CB                        mov rcx, rbx
003CD2BC  48 85 DB                        test rbx, rbx
003CD2BF  75 E3                           jne 0x1403cd2a4
003CD2C1  44 8B 6D 67                     mov r13d, dword ptr [rbp + 0x67]
003CD2C5  E9 A4 F9 FF FF                  jmp 0x1403ccc6e
003CD2CA  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
003CD2CE  E8 0D 5A F7 FF                  call 0x140342ce0
003CD2D3  E9 13 F9 FF FF                  jmp 0x1403ccbeb
003CD2D8  BA 44 66 6C 74                  mov edx, 0x746c6644
003CD2DD  E8 BE 6B E9 FF                  call 0x140263ea0
003CD2E2  E9 25 F9 FF FF                  jmp 0x1403ccc0c
003CD2E7  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
003CD2EB  0F 84 96 B4 31 00               je 0x1406e8787
003CD2F1  4C 8D 05 50 D5 A3 00            lea r8, [rip + 0xa3d550]
003CD2F8  33 D2                           xor edx, edx
003CD2FA  33 C9                           xor ecx, ecx
003CD2FC  E8 4F C2 E3 FF                  call 0x140209550
003CD301  90                              nop
003CD302  E9 80 B4 31 00                  jmp 0x1406e8787
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcInitializeCacheMapInternal(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    v_rdi = 0;
    *(unsigned int *)(v_rsp - 71 - 73) = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 127))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rsp - 71 - 125) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 9) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 105) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 1) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11113300)) == 0) { a1 = *(unsigned int *)(v_rsp - 71 + 127); }
    *(unsigned int *)(v_rsp - 71 - 45) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rsp - 71 - 57) = 0;
    v_stack_mC8 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 97) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 71 - 121) = v_xmm1;
    if (a4 != 0) goto loc_003CD0D1;
loc_003CC7BC:
    if (*(unsigned __int64 *)(v_rsp - 71 + 111) != 0) goto loc_003CCADB;
loc_003CC7CB:
    *(unsigned __int64 *)(v_rsp - 71 - 17) = v_xmm0;
    if (*(unsigned __int64 *)(v_rsp - 71 + 111) == 0) { a1 = 1; }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116))) & (0x400ULL));
    *(unsigned int *)(v_rsp - 71 - 49) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 71 - 33) = v_xmm1;
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)(a1);
    result = (*(unsigned __int64 *)(v_rsp - 71 - 33)) + (0x3FFFFULL);
    *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
    result = (unsigned int)((result) & (0xFFFC0000ULL));
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8)) != 0) goto loc_003CC9FB;
loc_003CC81F:
    result = ExAllocateFromLookasideListEx(v_rip + 10769466, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), 1);
    a2 = 0;
    result = memset(result, a2, 616, 1);
    a1 = (unsigned int)((0) | (1));
    if (((*(unsigned __int8 *)(v_rsp - 71 - 45)) & (1)) == 0) { a1 = 0; }
    *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(a1);
    result = MmCreateCacheManagerSection(v_rsp - 71 - 57, *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(a1)), a1);
    if (((unsigned int)(result)) == 0xC000060BULL) goto loc_003CD26C;
    v_rbx = 0;
    if (sign_flag) goto loc_003CD252;
    result = ObDeleteCapturedInsertInfo(*(unsigned __int64 *)(v_rsp - 71 - 57), *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(a1)), a1);
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40)) + 60)) & (0x3FFULL));
    result = CcGetPartitionWithCreate(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10893303) + a1 * 8) + 184), *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(a1)), a1);
    if (result == 0) goto loc_003CCBBA;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    *(unsigned int *)(result) = 0x26802FFULL;
    *(unsigned int *)(result + 556) = (unsigned int)(result);
    *(unsigned int *)(result + 560) = (unsigned int)(result);
    result = -(a1);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10893303) + a1 * 8) + 184)) & (a1);
    *(unsigned __int64 *)(result + 96) = a1;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rsp - 71 - 25);
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(v_rsp - 71 - 17);
    *(unsigned __int64 *)(result + 48) = *(unsigned __int64 *)(v_rsp - 71 - 17);
    *(unsigned int *)(result + 520) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900)));
    *(unsigned __int64 *)(result + 536) = result;
    *(unsigned int *)(result + 608) = 0x40000ULL;
    result = CcInitializeVolumeCacheMap(a1, result + 512, (unsigned int)((unsigned int)(a1)), a1);
    if (sign_flag) goto loc_003CCBBF;
    if ((*(unsigned __int8 *)(v_rip + 11113043)) != 0) goto loc_003CCF2F;
loc_003CC93B:
    *(unsigned int *)(result + 288) = 1;
    v_rdi = 0;
    *(unsigned __int64 *)(result + 296) = 0;
    *(unsigned int *)(result + 304) = 0;
    *(unsigned __int16 *)(result + 312) = 1;
    *(unsigned __int8 *)(result + 314) = 6;
    *(unsigned int *)(result + 316) = 0;
    *(unsigned __int64 *)(result + 320 + 8) = result + 320;
    *(unsigned __int64 *)(result + 320) = result + 320;
    *(unsigned __int64 *)(result + 104) = 0;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 95)) != 0) goto loc_003CCC82;
loc_003CC98B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (32)) != 0) goto loc_003CCC8F;
loc_003CC997:
    if ((*(unsigned int *)(v_rsp - 71 - 49)) == 0) {
    }
    *(unsigned __int64 *)(result + 16 + 8) = result + 16;
    *(unsigned __int64 *)(result + 16) = result + 16;
    *(unsigned __int64 *)(result + 224) = *(unsigned __int64 *)(v_rsp - 71 + 119);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 156))))) | (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 156))) & (0xFFFFFFFEULL));
    if (*(unsigned __int64 *)(v_rsp - 71 + 103) == 0) { a1 = (unsigned int)(result); }
    result = *(unsigned __int64 *)(v_rsp - 71 + 103);
    if (*(unsigned __int64 *)(v_rsp - 71 + 103) == 0) { result = *(unsigned __int64 *)(v_rsp - 71 + 111); }
    *(unsigned int *)(result + 156) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 216) = result;
    *(unsigned __int64 *)(result + 232 + 8) = result + 232;
    *(unsigned __int64 *)(result + 232) = result + 232;
loc_003CC9FB:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10769082, v_rsp - 71 - 97, (unsigned int)((unsigned int)(a1)), a1);
    if ((*(unsigned __int64 *)(a1 + 48)) != 0) goto loc_003CD225;
    a2 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) != 0) goto loc_003CCA6C;
    if (result == 0) goto loc_003CD0E5;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, (unsigned int)((unsigned int)(a1)), a1);
    v_rbx = (*(unsigned __int64 *)(result + 536)) + (640);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) == v_rbx) goto loc_003CD00C;
loc_003CCA65:
loc_003CCA6C:
    result = CcGetPrivateVolumeCacheMap(result, v_rsp - 71 - 121, (unsigned int)((unsigned int)(a1)), a1);
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_003CCA97;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 72) != 0) goto loc_003CCE5A;
loc_003CCA97:
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, (unsigned int)((unsigned int)(a1)), a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (32)) == 0) goto loc_003CCEF1;
loc_003CCAB3:
    v_rbx = 0;
    if (condition_is_below) goto loc_003CD109;
loc_003CCAC5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900))) == 0) goto loc_003CCB1F;
    *(unsigned int *)(result + 520) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900)));
    goto loc_003CCB1F;
loc_003CCADB:
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900)))) != ((unsigned __int16)(a1))) goto loc_003CD0DA;
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900)) + 2)) == 40) goto loc_003CC7CB;
    goto loc_003CD0DA;
loc_003CCAF5:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 536) + 768) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 536) + 768 + 8) = v_rsp - 71 - 121;
    *(unsigned __int64 *)(v_rsp - 71 - 121) = *(unsigned __int64 *)(result + 536) + 768;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 9) + 900)) + 8) = *(unsigned __int64 *)(result + 536) + 768;
loc_003CCB03:
    *(unsigned int *)(v_rsp - 71 - 125) = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) = result;
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), (unsigned int)((unsigned int)(a1)), a1);
loc_003CCB1F:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 71 - 121, (unsigned int)(0x746C6644ULL), (unsigned int)((unsigned int)(a1)), a1);
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, (unsigned int)((unsigned int)(a1)), a1);
    if ((*(unsigned __int8 *)(v_rip + 12036787)) != 0) goto loc_003CD121;
loc_003CCB4B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 152))) & (0xFFFFFFEFULL));
    *(unsigned int *)(result + 152) = (unsigned int)(result);
    result = (unsigned int)((result) & (256));
    if ((*(unsigned __int64 *)(result + 88)) == 0) goto loc_003CCD81;
    if ((unsigned int)(result) == 0) goto loc_003CCC9C;
loc_003CCB73:
    result = ExAllocatePoolWithTag(512, 24, (unsigned int)(0x76456343ULL), a1);
    *(unsigned __int64 *)(result + 184) = result;
    if (result != 0) goto loc_003CD1D6;
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 121, 24, (unsigned int)(0x76456343ULL), a1);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, 24, (unsigned int)(0x76456343ULL), a1);
loc_003CCBBA:
loc_003CCBBF:
    a2 = 0;
    *(unsigned int *)(v_rsp - 71 - 125) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 125)));
    if (result != 0) goto loc_003CCC30;
    v_rbx = 0;
loc_003CCBD4:
    result = (unsigned int)(*(unsigned int *)(v_rsp - 71 - 125));
    if (0 != 0) {
        a1 = v_rsp - 71 - 121;
        result = KeReleaseInStackQueuedSpinLock(a1, a2, (unsigned int)(0x76456343ULL), a1);
    }
    if (0 != 0) goto loc_003CD2CA;
loc_003CCBEB:
    result = CcFreeSharedCacheMapIgnoreNull(0, a2, (unsigned int)(0x76456343ULL), a1);
    result = CcFreePrivateCacheMapIgnoreNull(*(unsigned __int64 *)(v_rsp - 71 - 65), a2, (unsigned int)(0x76456343ULL), a1);
    if (*(unsigned __int64 *)(v_rsp - 71 - 57) != 0) goto loc_003CD2D8;
loc_003CCC0C:
    if (sign_flag) goto loc_003CD2E7;
loc_003CCC14:
    v_rsp = (v_rsp) + (192);
    return result;
loc_003CCC30:
    *(unsigned __int64 *)(v_rsp - 71 - 65) = *(unsigned __int64 *)(v_rsp - 71 - 65);
    v_stack_p30 = 0;
    if ((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 - 57)) == 0) goto loc_003CCED6;
loc_003CCC44:
    *(unsigned int *)(v_rsp - 71 + 103) = (unsigned int)(v_stack_p8);
    if (*(unsigned __int64 *)(result + 536) != 0) goto loc_003CCF50;
loc_003CCC53:
    v_rbx = 0;
    if ((*(unsigned int *)(v_rsp - 71 - 125)) == 0) goto loc_003CCF82;
loc_003CCC5E:
    if (*(unsigned __int64 *)(result + 280) != 0) goto loc_003CD2A4;
loc_003CCC6E:
    *(unsigned __int64 *)(result + 280) = 0;
    goto loc_003CCBD4;
loc_003CCC82:
    goto loc_003CC98B;
loc_003CCC8F:
    goto loc_003CC997;
loc_003CCC9C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) + 1);
    *(unsigned int *)(result + 4) = (unsigned int)(result);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 121, a2, (unsigned int)(0x76456343ULL), a1);
loc_003CCCAD:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, a2, (unsigned int)(0x76456343ULL), a1);
    result = CcFreeSharedCacheMapIgnoreNull(0, a2, (unsigned int)(0x76456343ULL), a1);
    result = 0;
    if ((*(unsigned __int16 *)(result + 384)) != 0) goto loc_003CCEFD;
loc_003CCCD3:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10768348, v_rsp - 71 - 97, (unsigned int)(0x76456343ULL), a1);
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, (unsigned int)(0x76456343ULL), a1);
    a2 = 0;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(v_stack_p8)) + 48)) != 0) goto loc_003CD208;
    if ((*(unsigned __int16 *)(result + 384)) != 0) goto loc_003CCFF3;
loc_003CCD0E:
    result = memset(result + 384, a2, 120, a1);
    *(unsigned __int16 *)(result + 384) = 766;
    *(unsigned __int64 *)(result + 384 + 8) = (unsigned int)((unsigned int)(v_stack_p8));
    *(unsigned int *)(result + 384 + 4) = 0xFFFULL;
    result = PsGetPagePriorityThread(*(unsigned __int64 *)(v_rsp - 71 - 1), a2, 120, a1);
    a1 = (unsigned int)(((unsigned __int8)(result)) << (18));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 384)))));
    a1 = (unsigned int)((a1) & (0x1C0000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 384)))));
    result = 0;
    *(unsigned int *)(result + 384) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 384 + 80) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 232 + 8))) != (result + 232)) goto loc_003CCA65;
    *(unsigned __int64 *)(result + 384 + 96) = result + 232;
    *(unsigned __int64 *)(result + 384 + 96 + 8) = *(unsigned __int64 *)(result + 232 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 232 + 8)) = result + 384 + 96;
    *(unsigned __int64 *)(result + 232 + 8) = result + 384 + 96;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(v_stack_p8)) + 48) = result + 384;
loc_003CCD79:
    goto loc_003CCBBF;
loc_003CCD81:
    if ((unsigned int)(result + 384 + 96) != 0) goto loc_003CCB73;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) + 1);
    *(unsigned int *)(result + 4) = (unsigned int)(result);
    if (*(unsigned __int64 *)(result + 184) != 0) goto loc_003CD14F;
loc_003CCDA7:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 121, *(unsigned __int64 *)(result + 232 + 8), 120, a1);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, *(unsigned __int64 *)(result + 232 + 8), 120, a1);
    *(unsigned int *)(v_rsp - 71 - 73) = 1;
    if ((*(unsigned __int64 *)(result + 176)) != 1) goto loc_003CCF78;
    if (*(unsigned __int64 *)(v_rsp - 71 - 57) == 0) goto loc_003CD1B8;
    *(unsigned __int64 *)(result + 176) = *(unsigned __int64 *)(v_rsp - 71 - 57);
    *(unsigned __int64 *)(v_rsp - 71 - 57) = 1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(v_stack_p8)) + 24) + 6)) & (1)) == 0) goto loc_003CCFA1;
loc_003CCDF3:
    result = CcCreateVacbArray(result, *(unsigned __int64 *)(v_rsp - 71 - 33), 120, a1);
    if (!sign_flag) goto loc_003CD081;
loc_003CCE09:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10768044, v_rsp - 71 - 97, 120, a1);
    v_stack_p30 = (unsigned __int8)(v_stack_p30);
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, 120, a1);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(result + 184), a2, a3, a1);
loc_003CCE5A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 184))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 536) + 8))) goto loc_003CCA97;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, a3, a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))) != 0) goto loc_003CD0F3;
loc_003CCE82:
    if ((*(unsigned __int8 *)(v_rip + 11111679)) == 1) goto loc_003CD04E;
    result = (unsigned __int8)(-(*(unsigned __int8 *)(1 + 1172)));
    a2 = (unsigned int)((v_rsp - 71 - 121) & (12));
    a2 = (unsigned int)((a2) + (4));
    result = CcNotifyWriteBehindVolume(1, a2, a3, a1);
    if ((*(unsigned __int8 *)(1 + 1172)) == 1) {
        *(unsigned __int8 *)(1 + 985) = 1;
    }
    v_stack_p30 = 1;
loc_003CCEC1:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 71 - 121, a2, a3, a1);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, a2, a3, a1);
loc_003CCED6:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767839, v_rsp - 71 - 97, a3, a1);
    goto loc_003CCC44;
loc_003CCEF1:
    goto loc_003CCAB3;
loc_003CCEFD:
    result = ExAllocateFromLookasideListEx(v_rip + 10767612, v_rsp - 71 - 97, a3, a1);
    *(unsigned __int64 *)(v_rsp - 71 - 65) = result;
    if (result != 0) goto loc_003CCCD3;
    v_rbx = 0;
    *(unsigned int *)(v_rsp - 71 - 73) = 0;
    v_stack_p30 = 0;
    goto loc_003CCE09;
loc_003CCF2F:
    result = CcCreatePrivateVolumeCacheMap(*(unsigned __int64 *)(result + 536), 0, 0 + 600, a1);
    if (!sign_flag) goto loc_003CC93B;
    goto loc_003CCBBF;
loc_003CCF50:
    *(unsigned int *)(v_rsp - 71 + 103) = 0;
    if (0 != 0) goto loc_003CCC53;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, 0 + 600, a1);
    *(unsigned int *)(v_rsp - 71 + 103) = (unsigned int)(v_rbx + 1);
    goto loc_003CCC53;
loc_003CCF78:
    goto loc_003CCE09;
loc_003CCF82:
    if ((*(unsigned int *)(result + 112)) != 0) goto loc_003CCC5E;
    if ((*(unsigned int *)(result + 4)) == 0) goto loc_003CCC5E;
    result = CcInsertIntoCleanSharedCacheMapList(result, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CCC5E;
loc_003CCFA1:
    if ((*(unsigned __int64 *)(v_rbx + 1 + 32)) != 0) goto loc_003CCDF3;
    result = MmDisableModifiedWriteOfSection(*(unsigned __int64 *)(v_rbx + 1 + 40), v_rsp - 71 - 121, 0 + 600, a1);
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767617, v_rsp - 71 - 97, 0 + 600, a1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, 0 + 600, a1);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 71 - 121, v_rsp - 71 - 121, 0 + 600, a1);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CCDF3;
loc_003CCFF3:
    if (*(unsigned __int64 *)(v_rsp - 71 - 65) == 0) goto loc_003CD1F1;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = v_rsp - 71 - 121;
    goto loc_003CCD0E;
loc_003CD00C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65)) = *(unsigned __int64 *)(v_rsp - 71 - 65);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + 8) = v_rsp - 71 - 97;
    *(unsigned __int64 *)(v_rsp - 71 - 97) = *(unsigned __int64 *)(v_rsp - 71 - 65);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + 8) = *(unsigned __int64 *)(v_rsp - 71 - 65);
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rip + 11111270)) == 0) goto loc_003CCB03;
    result = (*(unsigned __int64 *)(result + 600)) + (608);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_003CCA65;
    goto loc_003CCAF5;
loc_003CD04E:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 536) + 1292)));
    a2 = (unsigned int)((*(unsigned __int64 *)(result + 8)) & (12));
    a2 = (unsigned int)((a2) + (4));
    result = CcNotifyWriteBehindInternal(*(unsigned __int64 *)(result + 536), a2, 0 + 600, a1);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 536) + 1292)) != ((unsigned __int8)(result))) goto loc_003CCEBC;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 536) + 1049) = 1;
    goto loc_003CCEBC;
loc_003CD081:
    if (((*(unsigned __int8 *)(v_rsp - 71 - 45)) & (1)) != 0) goto loc_003CD16A;
loc_003CD08B:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767402, v_rsp - 71 - 97, 0 + 600, a1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, 0 + 600, a1);
    if (*(unsigned __int64 *)(result + 184) != 0) goto loc_003CD1A9;
loc_003CD0C3:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 71 - 121, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CCCAD;
loc_003CD0D1:
    if (result == 0) goto loc_003CC7BC;
loc_003CD0DA:
    result = RtlRaiseStatus((unsigned int)(0xC000000DULL), v_rsp - 71 - 121, 0 + 600, a1);
loc_003CD0E5:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CC81F;
loc_003CD0F3:
    if (((unsigned int)(result)) == (*(unsigned int *)(result + 544))) goto loc_003CCE82;
    goto loc_003CCEC1;
loc_003CD109:
    if ((*(unsigned int *)(v_rsp - 71 - 49)) == 0) goto loc_003CCAC5;
    *(unsigned int *)(result + 152) = (unsigned int)(result);
    goto loc_003CCAC5;
loc_003CD121:
    if ((*(unsigned __int8 *)(v_rip + 12035253)) != 0) goto loc_003CCB4B;
    if (((*(unsigned int *)(result + 152)) & (0x80000ULL)) == 0) goto loc_003CCB4B;
    result = DbgPrint(v_rip + 3123932, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CCB4B;
loc_003CD14F:
    *(unsigned __int16 *)(result) = (unsigned __int16)(result);
    *(unsigned __int8 *)(result + 2) = 6;
    *(unsigned int *)(result + 4) = 0;
    result = (result) + (8);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    goto loc_003CCDA7;
loc_003CD16A:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767179, v_rsp - 71 - 97, 0 + 600, a1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 536) + 768, v_rsp - 71 - 121, 0 + 600, a1);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 71 - 121, v_rsp - 71 - 121, 0 + 600, a1);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, v_rsp - 71 - 121, 0 + 600, a1);
    goto loc_003CD08B;
loc_003CD1A9:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rsp - 71 - 97, a2, a3, a1);
    goto loc_003CD0C3;
loc_003CD1B8:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x8CCULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CD1D6:
    *(unsigned __int16 *)(result) = (unsigned __int16)(result);
    *(unsigned __int8 *)(result + 2) = 6;
    *(unsigned int *)(result + 4) = 0;
    result = (result) + (8);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
loc_003CD1F1:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 121, (unsigned int)(0x8CCULL), 0xFFFFFFFFC0000420ULL, a4);
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, (unsigned int)(0x8CCULL), 0xFFFFFFFFC0000420ULL, a4);
    goto loc_003CCEFD;
loc_003CD208:
    a3 = 0;
    result = CcDecrementOpenCountDeferDelete(result, (unsigned int)(0x8CCULL), a3, a4);
    goto loc_003CCD79;
loc_003CD225:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, (unsigned int)(0x8CCULL), a3, a4);
    result = CcFreeSharedCacheMapIgnoreNull(0, (unsigned int)(0x8CCULL), a3, a4);
    if (*(unsigned __int64 *)(v_rsp - 71 - 57) == 0) goto loc_003CCC14;
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(v_rsp - 71 - 57), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_003CCC14;
loc_003CD252:
    result = FsRtlIsNtstatusExpected((unsigned int)((unsigned int)((unsigned int)(0xC000060BULL))), (unsigned int)(0x746C6644ULL), a3, a4);
    a1 = (unsigned int)((unsigned int)((unsigned int)(0xC000060BULL)));
    if ((unsigned __int8)(result) == 0) { a1 = (unsigned int)((unsigned int)(0xC00000EAULL)); }
    goto loc_003CCBBF;
loc_003CD26C:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10766921, v_rsp - 71 - 97, a3, a4);
    v_rsi = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int64 *)(v_rip + 11110569)) != (*(unsigned __int64 *)(v_rip + 11110589))) { v_rsi = (unsigned int)((unsigned int)(0xC000A008ULL)); }
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, v_rsp - 71 - 97, a3, a4);
    result = 0;
    goto loc_003CCBBF;
loc_003CD2A4:
    a1 = (v_rsp - 71 - 97) & (-2);
    a3 = 0;
    a2 = 0;
    a1 = (a1) + (8);
    result = KeSetEvent(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(a1) != 0) goto loc_003CD2A4;
    goto loc_003CCC6E;
loc_003CD2CA:
    result = KeReleaseInStackQueuedSpinLock(v_rsp - 71 - 97, a2, a3, a4);
    goto loc_003CCBEB;
loc_003CD2D8:
    result = ObDereferenceObjectDeferDeleteWithTag(v_rsp - 71 - 97, (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_003CCC0C;
loc_003CD2E7:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip + 10736976, a4);
}
```

## 5. (Beta) C Style

```c
int64_t CcInitializeCacheMapInternal(void *Arg1, void *Arg2, uint8_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    local_rdi = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x7F))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x7D) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x69) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x1) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA99354)) == 0) { Arg1 = *(uint32_t *)(local_rsp - 0x47 + 0x7F); }
    *(uint32_t *)(local_rsp - 0x47 - 0x2D) = (uint32_t)(Arg1);
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = 0;
    v_stack_mC8 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x61) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x47 - 0x79) = v_xmm1;
    if (Arg4 != 0) goto loc_003CD0D1;
loc_003CC7BC:
    if (*(uint64_t *)(local_rsp - 0x47 + 0x6F) != 0) goto loc_003CCADB;
loc_003CC7CB:
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = v_xmm0;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x6F) == 0) { Arg1 = 1; }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74))) & (0x400ULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = v_xmm1;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)(Arg1);
    result = (*(uint64_t *)(local_rsp - 0x47 - 0x21)) + (0x3FFFFULL);
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
    result = (uint32_t)((result) & (0xFFFC0000ULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)) != 0) goto loc_003CC9FB;
loc_003CC81F:
    result = ExAllocateFromLookasideListEx(v_rip + 10769466, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), 1);
    Arg2 = 0;
    result = memset(result, Arg2, 616, 1);
    Arg1 = (uint32_t)((0) | (1));
    if (((*(uint8_t *)(local_rsp - 0x47 - 0x2D)) & (1)) == 0) { Arg1 = 0; }
    *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(Arg1);
    result = MmCreateCacheManagerSection(local_rsp - 71 - 57, *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(Arg1)), Arg1);
    if (((uint32_t)(result)) == 0xC000060BULL) goto loc_003CD26C;
    local_rbx = 0;
    if (sign_flag) goto loc_003CD252;
    result = ObDeleteCapturedInsertInfo(*(uint64_t *)(local_rsp - 0x47 - 0x39), *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(Arg1)), Arg1);
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28)) + 0x3C)) & (0x3FFULL));
    result = CcGetPartitionWithCreate(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA637F7) + arg1 * 8) + 0xB8), *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(Arg1)), Arg1);
    if (result == 0) goto loc_003CCBBA;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    *(uint32_t *)(result) = 0x26802FFULL;
    *(uint32_t *)(result + 0x22C) = (uint32_t)(result);
    *(uint32_t *)(result + 0x230) = (uint32_t)(result);
    result = -(Arg1);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA637F7) + arg1 * 8) + 0xB8)) & (Arg1);
    *(void **)(result + 0x60) = Arg1;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(local_rsp - 0x47 - 0x19);
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(local_rsp - 0x47 - 0x11);
    *(uint64_t *)(result + 0x30) = *(uint64_t *)(local_rsp - 0x47 - 0x11);
    *(uint32_t *)(result + 0x208) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384)));
    *(uint64_t *)(result + 0x218) = result;
    *(uint32_t *)(result + 0x260) = 0x40000ULL;
    result = CcInitializeVolumeCacheMap(Arg1, result + 512, (uint32_t)((uint32_t)(Arg1)), Arg1);
    if (sign_flag) goto loc_003CCBBF;
    if ((*(uint8_t *)(v_rip + 0xA99253)) != 0) goto loc_003CCF2F;
loc_003CC93B:
    *(uint32_t *)(result + 0x120) = 1;
    local_rdi = 0;
    *(uint64_t *)(result + 0x128) = 0;
    *(uint32_t *)(result + 0x130) = 0;
    *(uint16_t *)(result + 0x138) = 1;
    *(uint8_t *)(result + 0x13A) = 6;
    *(uint32_t *)(result + 0x13C) = 0;
    *(uint64_t *)(result + 0x140 + 0x8) = result + 320;
    *(uint64_t *)(result + 0x140) = result + 320;
    *(uint64_t *)(result + 0x68) = 0;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x5F)) != 0) goto loc_003CCC82;
loc_003CC98B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (32)) != 0) goto loc_003CCC8F;
loc_003CC997:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x31)) == 0) {
    }
    *(uint64_t *)(result + 0x10 + 0x8) = result + 16;
    *(uint64_t *)(result + 0x10) = result + 16;
    *(uint64_t *)(result + 0xE0) = *(uint64_t *)(local_rsp - 0x47 + 0x77);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x9C))))) | (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x9C))) & (0xFFFFFFFEULL));
    if (*(uint64_t *)(local_rsp - 0x47 + 0x67) == 0) { Arg1 = (uint32_t)(result); }
    result = *(uint64_t *)(local_rsp - 0x47 + 0x67);
    if (*(uint64_t *)(local_rsp - 0x47 + 0x67) == 0) { result = *(uint64_t *)(local_rsp - 0x47 + 0x6F); }
    *(uint32_t *)(result + 0x9C) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0xD8) = result;
    *(uint64_t *)(result + 0xE8 + 0x8) = result + 232;
    *(uint64_t *)(result + 0xE8) = result + 232;
loc_003CC9FB:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10769082, local_rsp - 71 - 97, (uint32_t)((uint32_t)(Arg1)), Arg1);
    if ((*(uint64_t *)(arg1 + 0x30)) != 0) goto loc_003CD225;
    Arg2 = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) != 0) goto loc_003CCA6C;
    if (result == 0) goto loc_003CD0E5;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, (uint32_t)((uint32_t)(Arg1)), Arg1);
    local_rbx = (*(uint64_t *)(result + 0x218)) + (640);
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) == local_rbx) goto loc_003CD00C;
loc_003CCA65:
loc_003CCA6C:
    result = CcGetPrivateVolumeCacheMap(result, local_rsp - 71 - 121, (uint32_t)((uint32_t)(Arg1)), Arg1);
    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_003CCA97;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x48) != 0) goto loc_003CCE5A;
loc_003CCA97:
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, (uint32_t)((uint32_t)(Arg1)), Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (32)) == 0) goto loc_003CCEF1;
loc_003CCAB3:
    local_rbx = 0;
    if (condition_is_below) goto loc_003CD109;
loc_003CCAC5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384))) == 0) goto loc_003CCB1F;
    *(uint32_t *)(result + 0x208) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384)));
    goto loc_003CCB1F;
loc_003CCADB:
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384)))) != ((uint16_t)(Arg1))) goto loc_003CD0DA;
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384)) + 0x2)) == 40) goto loc_003CC7CB;
    goto loc_003CD0DA;
loc_003CCAF5:
    *(uint64_t *)(*(uint64_t *)(result + 0x218) + 0x300) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384));
    *(uint64_t *)(*(uint64_t *)(result + 0x218) + 0x300 + 0x8) = local_rsp - 71 - 121;
    *(uint64_t *)(local_rsp - 0x47 - 0x79) = *(uint64_t *)(result + 0x218) + 768;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x9) + 0x384)) + 0x8) = *(uint64_t *)(result + 0x218) + 768;
loc_003CCB03:
    *(uint32_t *)(local_rsp - 0x47 - 0x7D) = 1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = result;
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), (uint32_t)((uint32_t)(Arg1)), Arg1);
loc_003CCB1F:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 71 - 121, (uint32_t)(0x746C6644ULL), (uint32_t)((uint32_t)(Arg1)), Arg1);
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, (uint32_t)((uint32_t)(Arg1)), Arg1);
    if ((*(uint8_t *)(v_rip + 0xB7AAB3)) != 0) goto loc_003CD121;
loc_003CCB4B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x98))) & (0xFFFFFFEFULL));
    *(uint32_t *)(result + 0x98) = (uint32_t)(result);
    result = (uint32_t)((result) & (256));
    if ((*(uint64_t *)(result + 0x58)) == 0) goto loc_003CCD81;
    if ((uint32_t)(result) == 0) goto loc_003CCC9C;
loc_003CCB73:
    result = ExAllocatePoolWithTag(512, 24, (uint32_t)(0x76456343ULL), Arg1);
    *(uint64_t *)(result + 0xB8) = result;
    if (result != 0) goto loc_003CD1D6;
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 121, 24, (uint32_t)(0x76456343ULL), Arg1);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, 24, (uint32_t)(0x76456343ULL), Arg1);
loc_003CCBBA:
loc_003CCBBF:
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x7D) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x7D)));
    if (result != 0) goto loc_003CCC30;
    local_rbx = 0;
loc_003CCBD4:
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x7D));
    if (0 != 0) {
        Arg1 = local_rsp - 71 - 121;
        result = KeReleaseInStackQueuedSpinLock(Arg1, Arg2, (uint32_t)(0x76456343ULL), Arg1);
    }
    if (0 != 0) goto loc_003CD2CA;
loc_003CCBEB:
    result = CcFreeSharedCacheMapIgnoreNull(0, Arg2, (uint32_t)(0x76456343ULL), Arg1);
    result = CcFreePrivateCacheMapIgnoreNull(*(uint64_t *)(local_rsp - 0x47 - 0x41), Arg2, (uint32_t)(0x76456343ULL), Arg1);
    if (*(uint64_t *)(local_rsp - 0x47 - 0x39) != 0) goto loc_003CD2D8;
loc_003CCC0C:
    if (sign_flag) goto loc_003CD2E7;
loc_003CCC14:
    local_rsp = (local_rsp) + (192);
    return result;
loc_003CCC30:
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = *(uint64_t *)(local_rsp - 0x47 - 0x41);
    v_stack_p30 = 0;
    if ((uint32_t)(*(uint64_t *)(local_rsp - 0x47 - 0x39)) == 0) goto loc_003CCED6;
loc_003CCC44:
    *(uint32_t *)(local_rsp - 0x47 + 0x67) = (uint32_t)(v_stack_p8);
    if (*(uint64_t *)(result + 0x218) != 0) goto loc_003CCF50;
loc_003CCC53:
    local_rbx = 0;
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x7D)) == 0) goto loc_003CCF82;
loc_003CCC5E:
    if (*(uint64_t *)(result + 0x118) != 0) goto loc_003CD2A4;
loc_003CCC6E:
    *(uint64_t *)(result + 0x118) = 0;
    goto loc_003CCBD4;
loc_003CCC82:
    goto loc_003CC98B;
loc_003CCC8F:
    goto loc_003CC997;
loc_003CCC9C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) + 1);
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 121, Arg2, (uint32_t)(0x76456343ULL), Arg1);
loc_003CCCAD:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, Arg2, (uint32_t)(0x76456343ULL), Arg1);
    result = CcFreeSharedCacheMapIgnoreNull(0, Arg2, (uint32_t)(0x76456343ULL), Arg1);
    result = 0;
    if ((*(uint16_t *)(result + 0x180)) != 0) goto loc_003CCEFD;
loc_003CCCD3:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10768348, local_rsp - 71 - 97, (uint32_t)(0x76456343ULL), Arg1);
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, (uint32_t)(0x76456343ULL), Arg1);
    Arg2 = 0;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(v_stack_p8)) + 0x30)) != 0) goto loc_003CD208;
    if ((*(uint16_t *)(result + 0x180)) != 0) goto loc_003CCFF3;
loc_003CCD0E:
    result = memset(result + 384, Arg2, 120, Arg1);
    *(uint16_t *)(result + 0x180) = 766;
    *(uint64_t *)(result + 0x180 + 0x8) = (uint32_t)((uint32_t)(v_stack_p8));
    *(uint32_t *)(result + 0x180 + 0x4) = 0xFFFULL;
    result = PsGetPagePriorityThread(*(uint64_t *)(local_rsp - 0x47 - 0x1), Arg2, 120, Arg1);
    Arg1 = (uint32_t)(((uint8_t)(result)) << (18));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x180)))));
    Arg1 = (uint32_t)((Arg1) & (0x1C0000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x180)))));
    result = 0;
    *(uint32_t *)(result + 0x180) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x180 + 0x50) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0xE8 + 0x8))) != (result + 232)) goto loc_003CCA65;
    *(uint64_t *)(result + 0x180 + 0x60) = result + 232;
    *(uint64_t *)(result + 0x180 + 0x60 + 0x8) = *(uint64_t *)(result + 0xE8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0xE8 + 0x8)) = result + 384 + 96;
    *(uint64_t *)(result + 0xE8 + 0x8) = result + 384 + 96;
    *(uint64_t *)((uint32_t)((uint32_t)(v_stack_p8)) + 0x30) = result + 384;
loc_003CCD79:
    goto loc_003CCBBF;
loc_003CCD81:
    if ((uint32_t)(result + 384 + 96) != 0) goto loc_003CCB73;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) + 1);
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
    if (*(uint64_t *)(result + 0xB8) != 0) goto loc_003CD14F;
loc_003CCDA7:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 121, *(uint64_t *)(result + 0xE8 + 0x8), 120, Arg1);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, *(uint64_t *)(result + 0xE8 + 0x8), 120, Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = 1;
    if ((*(uint64_t *)(result + 0xB0)) != 1) goto loc_003CCF78;
    if (*(uint64_t *)(local_rsp - 0x47 - 0x39) == 0) goto loc_003CD1B8;
    *(uint64_t *)(result + 0xB0) = *(uint64_t *)(local_rsp - 0x47 - 0x39);
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = 1;
    if (((*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)(v_stack_p8)) + 0x18) + 0x6)) & (1)) == 0) goto loc_003CCFA1;
loc_003CCDF3:
    result = CcCreateVacbArray(result, *(uint64_t *)(local_rsp - 0x47 - 0x21), 120, Arg1);
    if (!sign_flag) goto loc_003CD081;
loc_003CCE09:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10768044, local_rsp - 71 - 97, 120, Arg1);
    v_stack_p30 = (uint8_t)(v_stack_p30);
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, 120, Arg1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(result + 0xB8), Arg2, Arg3, Arg1);
loc_003CCE5A:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0xB8))) == (*(uint64_t *)(*(uint64_t *)(result + 0x218) + 0x8))) goto loc_003CCA97;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, Arg3, Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))) != 0) goto loc_003CD0F3;
loc_003CCE82:
    if ((*(uint8_t *)(v_rip + 0xA98CFF)) == 1) goto loc_003CD04E;
    result = (uint8_t)(-(*(uint8_t *)(1 + 0x494)));
    Arg2 = (uint32_t)((local_rsp - 71 - 121) & (12));
    Arg2 = (uint32_t)((Arg2) + (4));
    result = CcNotifyWriteBehindVolume(1, Arg2, Arg3, Arg1);
    if ((*(uint8_t *)(1 + 0x494)) == 1) {
        *(uint8_t *)(1 + 0x3D9) = 1;
    }
    v_stack_p30 = 1;
loc_003CCEC1:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 71 - 121, Arg2, Arg3, Arg1);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, Arg2, Arg3, Arg1);
loc_003CCED6:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767839, local_rsp - 71 - 97, Arg3, Arg1);
    goto loc_003CCC44;
loc_003CCEF1:
    goto loc_003CCAB3;
loc_003CCEFD:
    result = ExAllocateFromLookasideListEx(v_rip + 10767612, local_rsp - 71 - 97, Arg3, Arg1);
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = result;
    if (result != 0) goto loc_003CCCD3;
    local_rbx = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = 0;
    v_stack_p30 = 0;
    goto loc_003CCE09;
loc_003CCF2F:
    result = CcCreatePrivateVolumeCacheMap(*(uint64_t *)(result + 0x218), 0, 0 + 600, Arg1);
    if (!sign_flag) goto loc_003CC93B;
    goto loc_003CCBBF;
loc_003CCF50:
    *(uint32_t *)(local_rsp - 0x47 + 0x67) = 0;
    if (0 != 0) goto loc_003CCC53;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, 0 + 600, Arg1);
    *(uint32_t *)(local_rsp - 0x47 + 0x67) = (uint32_t)(local_rbx + 1);
    goto loc_003CCC53;
loc_003CCF78:
    goto loc_003CCE09;
loc_003CCF82:
    if ((*(uint32_t *)(result + 0x70)) != 0) goto loc_003CCC5E;
    if ((*(uint32_t *)(result + 0x4)) == 0) goto loc_003CCC5E;
    result = CcInsertIntoCleanSharedCacheMapList(result, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CCC5E;
loc_003CCFA1:
    if ((*(uint64_t *)(local_rbx + 0x1 + 0x20)) != 0) goto loc_003CCDF3;
    result = MmDisableModifiedWriteOfSection(*(uint64_t *)(local_rbx + 0x1 + 0x28), local_rsp - 71 - 121, 0 + 600, Arg1);
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767617, local_rsp - 71 - 97, 0 + 600, Arg1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, 0 + 600, Arg1);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 71 - 121, local_rsp - 71 - 121, 0 + 600, Arg1);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CCDF3;
loc_003CCFF3:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x41) == 0) goto loc_003CD1F1;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = local_rsp - 71 - 121;
    goto loc_003CCD0E;
loc_003CD00C:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41)) = *(uint64_t *)(local_rsp - 0x47 - 0x41);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + 0x8) = local_rsp - 71 - 97;
    *(uint64_t *)(local_rsp - 0x47 - 0x61) = *(uint64_t *)(local_rsp - 0x47 - 0x41);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + 0x8) = *(uint64_t *)(local_rsp - 0x47 - 0x41);
    local_rbx = 0;
    if ((*(uint8_t *)(v_rip + 0xA98B66)) == 0) goto loc_003CCB03;
    result = (*(uint64_t *)(result + 0x258)) + (608);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_003CCA65;
    goto loc_003CCAF5;
loc_003CD04E:
    result = (uint8_t)(-(*(uint8_t *)(*(uint64_t *)(result + 0x218) + 0x50C)));
    Arg2 = (uint32_t)((*(uint64_t *)(result + 0x8)) & (12));
    Arg2 = (uint32_t)((Arg2) + (4));
    result = CcNotifyWriteBehindInternal(*(uint64_t *)(result + 0x218), Arg2, 0 + 600, Arg1);
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x218) + 0x50C)) != ((uint8_t)(result))) goto loc_003CCEBC;
    *(uint8_t *)(*(uint64_t *)(result + 0x218) + 0x419) = 1;
    goto loc_003CCEBC;
loc_003CD081:
    if (((*(uint8_t *)(local_rsp - 0x47 - 0x2D)) & (1)) != 0) goto loc_003CD16A;
loc_003CD08B:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767402, local_rsp - 71 - 97, 0 + 600, Arg1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, 0 + 600, Arg1);
    if (*(uint64_t *)(result + 0xB8) != 0) goto loc_003CD1A9;
loc_003CD0C3:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 71 - 121, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CCCAD;
loc_003CD0D1:
    if (result == 0) goto loc_003CC7BC;
loc_003CD0DA:
    result = RtlRaiseStatus((uint32_t)(0xC000000DULL), local_rsp - 71 - 121, 0 + 600, Arg1);
loc_003CD0E5:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CC81F;
loc_003CD0F3:
    if (((uint32_t)(result)) == (*(uint32_t *)(result + 0x220))) goto loc_003CCE82;
    goto loc_003CCEC1;
loc_003CD109:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x31)) == 0) goto loc_003CCAC5;
    *(uint32_t *)(result + 0x98) = (uint32_t)(result);
    goto loc_003CCAC5;
loc_003CD121:
    if ((*(uint8_t *)(v_rip + 0xB7A4B5)) != 0) goto loc_003CCB4B;
    if (((*(uint32_t *)(result + 0x98)) & (0x80000ULL)) == 0) goto loc_003CCB4B;
    result = DbgPrint(v_rip + 3123932, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CCB4B;
loc_003CD14F:
    *(uint16_t *)(result) = (uint16_t)(result);
    *(uint8_t *)(result + 0x2) = 6;
    *(uint32_t *)(result + 0x4) = 0;
    result = (result) + (8);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    goto loc_003CCDA7;
loc_003CD16A:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10767179, local_rsp - 71 - 97, 0 + 600, Arg1);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(result + 0x218) + 768, local_rsp - 71 - 121, 0 + 600, Arg1);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 71 - 121, local_rsp - 71 - 121, 0 + 600, Arg1);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, local_rsp - 71 - 121, 0 + 600, Arg1);
    goto loc_003CD08B;
loc_003CD1A9:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(local_rsp - 71 - 97, Arg2, Arg3, Arg1);
    goto loc_003CD0C3;
loc_003CD1B8:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0x8CCULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CD1D6:
    *(uint16_t *)(result) = (uint16_t)(result);
    *(uint8_t *)(result + 0x2) = 6;
    *(uint32_t *)(result + 0x4) = 0;
    result = (result) + (8);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
loc_003CD1F1:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 121, (uint32_t)(0x8CCULL), 0xFFFFFFFFC0000420ULL, Arg4);
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, (uint32_t)(0x8CCULL), 0xFFFFFFFFC0000420ULL, Arg4);
    goto loc_003CCEFD;
loc_003CD208:
    Arg3 = 0;
    result = CcDecrementOpenCountDeferDelete(result, (uint32_t)(0x8CCULL), Arg3, Arg4);
    goto loc_003CCD79;
loc_003CD225:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, (uint32_t)(0x8CCULL), Arg3, Arg4);
    result = CcFreeSharedCacheMapIgnoreNull(0, (uint32_t)(0x8CCULL), Arg3, Arg4);
    if (*(uint64_t *)(local_rsp - 0x47 - 0x39) == 0) goto loc_003CCC14;
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(local_rsp - 0x47 - 0x39), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_003CCC14;
loc_003CD252:
    result = FsRtlIsNtstatusExpected((uint32_t)((uint32_t)((uint32_t)(0xC000060BULL))), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(0xC000060BULL)));
    if ((uint8_t)(result) == 0) { Arg1 = (uint32_t)((uint32_t)(0xC00000EAULL)); }
    goto loc_003CCBBF;
loc_003CD26C:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 10766921, local_rsp - 71 - 97, Arg3, Arg4);
    local_rsi = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint64_t *)(v_rip + 0xA988A9)) != (*(uint64_t *)(v_rip + 0xA988BD))) { local_rsi = (uint32_t)((uint32_t)(0xC000A008ULL)); }
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, local_rsp - 71 - 97, Arg3, Arg4);
    result = 0;
    goto loc_003CCBBF;
loc_003CD2A4:
    Arg1 = (local_rsp - 71 - 97) & (-2);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (Arg1) + (8);
    result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg1) != 0) goto loc_003CD2A4;
    goto loc_003CCC6E;
loc_003CD2CA:
    result = KeReleaseInStackQueuedSpinLock(local_rsp - 71 - 97, Arg2, Arg3, Arg4);
    goto loc_003CCBEB;
loc_003CD2D8:
    result = ObDereferenceObjectDeferDeleteWithTag(local_rsp - 71 - 97, (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_003CCC0C;
loc_003CD2E7:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip + 10736976, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CC720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
