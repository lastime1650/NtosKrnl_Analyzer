# CcPinFileData

- RVA: `0x0033FB40`–`0x00340C96` (길이 `4,438` bytes)
- VA: `0x000000014033FB40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00077474`
- 디코드: `1,008`개 명령, `4,438/4,438` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **68**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0033FBF2` → [CcGetVirtualAddress](../34/CcGetVirtualAddress_function_00340C9C.md) (function, `0x00340C9C`)
- `0x0033FC09` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0033FC66` → [KeAbPreWait](../20/KeAbPreWait_function_0020E560.md) (function, `0x0020E560`)
- `0x0033FC7F` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0033FC9F` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0033FE41` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0033FE80` → [ExpAcquireSharedStarveExclusive](../34/ExpAcquireSharedStarveExclusive_function_003411C0.md) (function, `0x003411C0`)
- `0x0033FF41` → [MmCheckCachedPageStates](../2F/MmCheckCachedPageStates_function_002F6C60.md) (function, `0x002F6C60`)
- `0x0033FFC5` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0033FFD2` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00340010` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0034013C` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x00340182` → [ExInitializeResourceLite2](../41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00340190` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x003401AC` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x003401EE` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340215` → [ExAcquireSharedStarveExclusive](../3B/ExAcquireSharedStarveExclusive_function_003BDB00.md) (function, `0x003BDB00`)
- `0x0034024B` → [CcAllocateInitializeBcb](../41/CcAllocateInitializeBcb_function_0041F5A4.md) (function, `0x0041F5A4`)
- `0x003402B2` → [CcAdjustVacbLevelLockCount](../41/CcAdjustVacbLevelLockCount_function_0041F8A4.md) (function, `0x0041F8A4`)
- `0x003402EF` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00340302` → [ExDisableResourceBoostLite](../41/ExDisableResourceBoostLite_function_0041F840.md) (function, `0x0041F840`)
- `0x0034032A` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0034033A` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0034035C` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340373` → [CcMapAndRead](../2F/CcMapAndRead_function_002F6AC0.md) (function, `0x002F6AC0`)
- `0x00340387` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x003403B5` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x003403D7` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x003403E7` → [ExAcquireSharedStarveExclusive](../3B/ExAcquireSharedStarveExclusive_function_003BDB00.md) (function, `0x003BDB00`)
- `0x00340459` → [ExAcquireSharedStarveExclusive](../3B/ExAcquireSharedStarveExclusive_function_003BDB00.md) (function, `0x003BDB00`)
- `0x00340475` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0034049B` → [ExAcquireSharedStarveExclusive](../3B/ExAcquireSharedStarveExclusive_function_003BDB00.md) (function, `0x003BDB00`)
- `0x003404BD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003404FA` → [ExpAcquireSharedStarveExclusive](../34/ExpAcquireSharedStarveExclusive_function_003411C0.md) (function, `0x003411C0`)
- `0x0034051F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034052B` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340624` → [MmCheckCachedPageStates](../2F/MmCheckCachedPageStates_function_002F6C60.md) (function, `0x002F6C60`)
- `0x00340685` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00340692` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x003406D0` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340708` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x0034072A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034072F` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00340743` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340763` → [CcMapAndRead](../2F/CcMapAndRead_function_002F6AC0.md) (function, `0x002F6AC0`)
- `0x00340777` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x003407D8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003407EF` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00340854` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0034089E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340903` → [CcGetBcbListHeadLargeOffset](../34/CcGetBcbListHeadLargeOffset_function_00341990.md) (function, `0x00341990`)
- `0x0034097E` → [ExpFastResourceLegacyAcquireSharedStarveExclusive](../3B/ExpFastResourceLegacyAcquireSharedStarveExclusive_function_003BDC18.md) (function, `0x003BDC18`)
- `0x003409AE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003409D4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340A0A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340A2B` → [ExpFastResourceLegacyAcquireSharedStarveExclusive](../3B/ExpFastResourceLegacyAcquireSharedStarveExclusive_function_003BDC18.md) (function, `0x003BDC18`)
- `0x00340A5B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340A86` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340AE8` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00340B1B` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00340B96` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x00340BA5` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00340C2D` → [CcAllocateVacbLevels](../48/CcAllocateVacbLevels_function_00482050.md) (function, `0x00482050`)
- `0x00340C3F` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00340C5D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00340C6F` → [CcAcquireBcbLockAndVacbLock](../26/CcAcquireBcbLockAndVacbLock_function_0026FC58.md) (function, `0x0026FC58`)
- `0x00340C81` → [SetVacb](../27/SetVacb_function_00273340.md) (function, `0x00273340`)
- `0x00340C8C` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)

### Direct callers
- [CcZeroDataInCache](../29/CcZeroDataInCache_function_0029E894.md) at `0x0029E913`
- [CcMapData](../../page/96/CcMapData_function_0096C430.md) at `0x0096C58A`
- [CcMapDataCommon](../../page/99/CcMapDataCommon_function_0099E560.md) at `0x0099E61D`
- [CcPinMappedData](../../page/9D/CcPinMappedData_function_009D5B50.md) at `0x009D5C30`
- [CcPreparePinWrite](../../page/A4/CcPreparePinWrite_function_00A4C1C0.md) at `0x00A4C297`
- [CcPinRead](../../page/A7/CcPinRead_function_00A703B0.md) at `0x00A70485`

### Static image references
- `0x0033FC27` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00340C1D` → RVA `0x00E0A894` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0034013C` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00340C34` → [sub_006E2024](../6E/Unknown_function_006E2024.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033FB40  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0033FB45  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0033FB4A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0033FB4F  53                              push rbx
0033FB50  56                              push rsi
0033FB51  57                              push rdi
0033FB52  41 54                           push r12
0033FB54  41 55                           push r13
0033FB56  41 56                           push r14
0033FB58  41 57                           push r15
0033FB5A  48 81 EC F0 00 00 00            sub rsp, 0xf0
0033FB61  4C 8B F2                        mov r14, rdx
0033FB64  44 8B AC 24 58 01 00 00         mov r13d, dword ptr [rsp + 0x158]
0033FB6C  45 33 E4                        xor r12d, r12d
0033FB6F  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0033FB74  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
0033FB79  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
0033FB7E  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
0033FB83  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0033FB88  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0033FB8C  48 8B 70 08                     mov rsi, qword ptr [rax + 8]
0033FB90  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
0033FB98  41 8B F8                        mov edi, r8d
0033FB9B  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
0033FBA0  48 8B 0A                        mov rcx, qword ptr [rdx]
0033FBA3  48 03 CF                        add rcx, rdi
0033FBA6  48 3B 4E 20                     cmp rcx, qword ptr [rsi + 0x20]
0033FBAA  0F 8F 95 10 00 00               jg 0x140340c45
0033FBB0  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
0033FBB8  4C 89 20                        mov qword ptr [rax], r12
0033FBBB  48 8B 9C 24 68 01 00 00         mov rbx, qword ptr [rsp + 0x168]
0033FBC3  4C 89 23                        mov qword ptr [rbx], r12
0033FBC6  41 F6 C5 04                     test r13b, 4
0033FBCA  0F 85 ED 0F 00 00               jne 0x140340bbd
0033FBD0  41 8B C5                        mov eax, r13d
0033FBD3  C1 E8 06                        shr eax, 6
0033FBD6  83 E0 01                        and eax, 1
0033FBD9  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
0033FBDE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0033FBE2  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
0033FBE7  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0033FBEC  48 8B 12                        mov rdx, qword ptr [rdx]
0033FBEF  48 8B CE                        mov rcx, rsi
0033FBF2  E8 A5 10 00 00                  call 0x140340c9c
0033FBF7  48 89 03                        mov qword ptr [rbx], rax
0033FBFA  48 8D 9E 20 01 00 00            lea rbx, [rsi + 0x120]
0033FC01  45 33 C0                        xor r8d, r8d
0033FC04  33 D2                           xor edx, edx
0033FC06  48 8B CB                        mov rcx, rbx
0033FC09  E8 22 06 ED FF                  call 0x140210230
0033FC0E  4C 8B F8                        mov r15, rax
0033FC11  45 0F 20 C0                     mov r8, cr8
0033FC15  4C 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], r8
0033FC1D  41 BB 01 00 00 00               mov r11d, 1
0033FC23  45 0F 22 C3                     mov cr8, r11
0033FC27  44 39 25 F2 70 C8 00            cmp dword ptr [rip + 0xc870f2], r12d
0033FC2E  0F 85 69 0F 00 00               jne 0x140340b9d
0033FC34  F0 0F BA 33 00                  lock btr dword ptr [rbx], 0
0033FC39  0F 82 93 00 00 00               jb 0x14033fcd2
0033FC3F  49 8B FF                        mov rdi, r15
0033FC42  FF 43 10                        inc dword ptr [rbx + 0x10]
0033FC45  45 8B EB                        mov r13d, r11d
0033FC48  41 BC 04 00 00 00               mov r12d, 4
0033FC4E  8B 03                           mov eax, dword ptr [rbx]
0033FC50  A8 01                           test al, 1
0033FC52  75 55                           jne 0x14033fca9
0033FC54  41 8D 0C 04                     lea ecx, [r12 + rax]
0033FC58  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
0033FC5C  75 F2                           jne 0x14033fc50
0033FC5E  48 85 FF                        test rdi, rdi
0033FC61  74 08                           je 0x14033fc6b
0033FC63  48 8B CF                        mov rcx, rdi
0033FC66  E8 F5 E8 EC FF                  call 0x14020e560
0033FC6B  48 8D 4B 18                     lea rcx, [rbx + 0x18]
0033FC6F  33 C0                           xor eax, eax
0033FC71  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0033FC76  45 33 C9                        xor r9d, r9d
0033FC79  45 33 C0                        xor r8d, r8d
0033FC7C  8D 50 22                        lea edx, [rax + 0x22]
0033FC7F  E8 2C EA EC FF                  call 0x14020e6b0
0033FC84  0F 0D 0B                        prefetchw byte ptr [rbx]
0033FC87  41 BD 03 00 00 00               mov r13d, 3
0033FC8D  45 8D 65 FF                     lea r12d, [r13 - 1]
0033FC91  48 85 FF                        test rdi, rdi
0033FC94  74 B8                           je 0x14033fc4e
0033FC96  45 33 C0                        xor r8d, r8d
0033FC99  48 8B D7                        mov rdx, rdi
0033FC9C  48 8B CB                        mov rcx, rbx
0033FC9F  E8 8C 05 ED FF                  call 0x140210230
0033FCA4  48 8B F8                        mov rdi, rax
0033FCA7  EB A5                           jmp 0x14033fc4e
0033FCA9  8B C8                           mov ecx, eax
0033FCAB  41 33 CD                        xor ecx, r13d
0033FCAE  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
0033FCB2  75 9C                           jne 0x14033fc50
0033FCB4  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0033FCB9  4C 8B 84 24 30 01 00 00         mov r8, qword ptr [rsp + 0x130]
0033FCC1  44 8B AC 24 58 01 00 00         mov r13d, dword ptr [rsp + 0x158]
0033FCC9  41 BB 01 00 00 00               mov r11d, 1
0033FCCF  45 33 E4                        xor r12d, r12d
0033FCD2  4D 85 FF                        test r15, r15
0033FCD5  74 05                           je 0x14033fcdc
0033FCD7  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0033FCDC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0033FCE5  48 89 43 08                     mov qword ptr [rbx + 8], rax
0033FCE9  41 0F B6 C0                     movzx eax, r8b
0033FCED  89 43 30                        mov dword ptr [rbx + 0x30], eax
0033FCF0  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
0033FCF5  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0033FCFA  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0033FCFF  4D 8B 06                        mov r8, qword ptr [r14]
0033FD02  4D 8B F8                        mov r15, r8
0033FD05  49 C1 EF 20                     shr r15, 0x20
0033FD09  49 8D 1C 38                     lea rbx, [r8 + rdi]
0033FD0D  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0033FD15  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
0033FD1D  45 32 E4                        xor r12b, r12b
0033FD20  44 88 64 24 31                  mov byte ptr [rsp + 0x31], r12b
0033FD25  49 8D B8 00 00 08 00            lea rdi, [r8 + 0x80000]
0033FD2C  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0033FD30  4C 8B C9                        mov r9, rcx
0033FD33  49 C1 E9 20                     shr r9, 0x20
0033FD37  48 81 F9 00 00 20 00            cmp rcx, 0x200000
0033FD3E  0F 8F 9D 0B 00 00               jg 0x1403408e1
0033FD44  48 8D 7E 10                     lea rdi, [rsi + 0x10]
0033FD48  48 8B 3F                        mov rdi, qword ptr [rdi]
0033FD4B  48 83 EF 10                     sub rdi, 0x10
0033FD4F  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
0033FD57  45 85 FF                        test r15d, r15d
0033FD5A  41 BF FD 02 00 00               mov r15d, 0x2fd
0033FD60  0F 85 CD 02 00 00               jne 0x140340033
0033FD66  66 44 39 3F                     cmp word ptr [rdi], r15w
0033FD6A  75 5C                           jne 0x14033fdc8
0033FD6C  83 7F 24 00                     cmp dword ptr [rdi + 0x24], 0
0033FD70  0F 85 BD 02 00 00               jne 0x140340033
0033FD76  41 0F B7 C7                     movzx eax, r15w
0033FD7A  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
0033FD81  66 41 3B C7                     cmp ax, r15w
0033FD85  75 41                           jne 0x14033fdc8
0033FD87  41 8B 0E                        mov ecx, dword ptr [r14]
0033FD8A  3B 4F 20                        cmp ecx, dword ptr [rdi + 0x20]
0033FD8D  73 39                           jae 0x14033fdc8
0033FD8F  8B 47 08                        mov eax, dword ptr [rdi + 8]
0033FD92  3B C8                           cmp ecx, eax
0033FD94  73 2A                           jae 0x14033fdc0
0033FD96  3B D0                           cmp edx, eax
0033FD98  72 11                           jb 0x14033fdab
0033FD9A  8B D0                           mov edx, eax
0033FD9C  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0033FDA3  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0033FDAB  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
0033FDAF  48 83 EF 10                     sub rdi, 0x10
0033FDB3  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
0033FDBB  0F B7 07                        movzx eax, word ptr [rdi]
0033FDBE  EB C1                           jmp 0x14033fd81
0033FDC0  41 B4 01                        mov r12b, 1
0033FDC3  44 88 64 24 31                  mov byte ptr [rsp + 0x31], r12b
0033FDC8  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0033FDCD  45 84 E4                        test r12b, r12b
0033FDD0  0F 84 95 01 00 00               je 0x14033ff6b
0033FDD6  F7 86 98 00 00 00 00 02 00 00   test dword ptr [rsi + 0x98], 0x200
0033FDE0  0F B6 9C 24 48 01 00 00         movzx ebx, byte ptr [rsp + 0x148]
0033FDE8  41 0F 44 DB                     cmove ebx, r11d
0033FDEC  88 9C 24 48 01 00 00            mov byte ptr [rsp + 0x148], bl
0033FDF3  41 8B D5                        mov edx, r13d
0033FDF6  83 E2 01                        and edx, 1
0033FDF9  48 83 BF B8 00 00 00 00         cmp qword ptr [rdi + 0xb8], 0
0033FE01  0F 85 D0 03 00 00               jne 0x1403401d7
0033FE07  41 8B 06                        mov eax, dword ptr [r14]
0033FE0A  2B 47 08                        sub eax, dword ptr [rdi + 8]
0033FE0D  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
0033FE15  49 29 04 24                     sub qword ptr [r12], rax
0033FE19  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0033FE1D  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0033FE22  8B 47 04                        mov eax, dword ptr [rdi + 4]
0033FE25  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0033FE2A  85 D2                           test edx, edx
0033FE2C  0F 84 0D 05 00 00               je 0x14034033f
0033FE32  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0033FE35  FF C0                           inc eax
0033FE37  89 47 40                        mov dword ptr [rdi + 0x40], eax
0033FE3A  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
0033FE41  E8 7A 1B F1 FF                  call 0x1402519c0
0033FE46  45 33 DB                        xor r11d, r11d
0033FE49  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
0033FE4E  84 DB                           test bl, bl
0033FE50  75 36                           jne 0x14033fe88
0033FE52  4C 8D 47 48                     lea r8, [rdi + 0x48]
0033FE56  41 F6 C5 02                     test r13b, 2
0033FE5A  0F 85 8A 09 00 00               jne 0x1403407ea
0033FE60  41 0F B7 48 1A                  movzx ecx, word ptr [r8 + 0x1a]
0033FE65  0F B6 C1                        movzx eax, cl
0033FE68  24 41                           and al, 0x41
0033FE6A  3C 01                           cmp al, 1
0033FE6C  0F 84 55 09 00 00               je 0x1403407c7
0033FE72  F6 C1 01                        test cl, 1
0033FE75  0F 85 0D 0B 00 00               jne 0x140340988
0033FE7B  B2 01                           mov dl, 1
0033FE7D  49 8B C8                        mov rcx, r8
0033FE80  E8 3B 13 00 00                  call 0x1403411c0
0033FE85  45 33 DB                        xor r11d, r11d
0033FE88  41 F6 C5 04                     test r13b, 4
0033FE8C  0F 85 94 01 00 00               jne 0x140340026
0033FE92  49 8B 1C 24                     mov rbx, qword ptr [r12]
0033FE96  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0033FE9B  8B CB                           mov ecx, ebx
0033FE9D  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0033FEA6  44 89 9C 24 94 00 00 00         mov dword ptr [rsp + 0x94], r11d
0033FEAE  44 89 9C 24 E4 00 00 00         mov dword ptr [rsp + 0xe4], r11d
0033FEB6  44 89 9C 24 80 00 00 00         mov dword ptr [rsp + 0x80], r11d
0033FEBE  45 8B C3                        mov r8d, r11d
0033FEC1  44 89 9C 24 98 00 00 00         mov dword ptr [rsp + 0x98], r11d
0033FEC9  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0033FECE  81 E1 FF 0F 00 00               and ecx, 0xfff
0033FED4  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0033FED8  48 81 C2 FF 0F 00 00            add rdx, 0xfff
0033FEDF  48 03 D1                        add rdx, rcx
0033FEE2  48 C1 EA 0C                     shr rdx, 0xc
0033FEE6  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
0033FEED  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0033FEF4  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0033FEF9  0F B6 8F AC 05 00 00            movzx ecx, byte ptr [rdi + 0x5ac]
0033FF00  8B 87 98 05 00 00               mov eax, dword ptr [rdi + 0x598]
0033FF06  44 8D 3C 41                     lea r15d, [rcx + rax*2]
0033FF0A  85 D2                           test edx, edx
0033FF0C  0F 84 95 00 00 00               je 0x14033ffa7
0033FF12  C6 87 AC 05 00 00 01            mov byte ptr [rdi + 0x5ac], 1
0033FF19  8D 42 FF                        lea eax, [rdx - 1]
0033FF1C  3B 87 98 05 00 00               cmp eax, dword ptr [rdi + 0x598]
0033FF22  0F 87 87 08 00 00               ja 0x1403407af
0033FF28  44 89 9C 24 94 00 00 00         mov dword ptr [rsp + 0x94], r11d
0033FF30  C1 E2 0C                        shl edx, 0xc
0033FF33  44 8B E2                        mov r12d, edx
0033FF36  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0033FF3B  45 33 C0                        xor r8d, r8d
0033FF3E  48 8B CB                        mov rcx, rbx
0033FF41  E8 1A 6D FB FF                  call 0x1402f6c60
0033FF46  44 8B C0                        mov r8d, eax
0033FF49  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
0033FF50  85 C0                           test eax, eax
0033FF52  78 53                           js 0x14033ffa7
0033FF54  49 03 DC                        add rbx, r12
0033FF57  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0033FF5C  45 33 DB                        xor r11d, r11d
0033FF5F  41 8B D3                        mov edx, r11d
0033FF62  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
0033FF69  EB 9F                           jmp 0x14033ff0a
0033FF6B  41 F6 C5 08                     test r13b, 8
0033FF6F  0F 84 FD 00 00 00               je 0x140340072
0033FF75  45 33 C0                        xor r8d, r8d
0033FF78  41 8B F8                        mov edi, r8d
0033FF7B  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0033FF80  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
0033FF85  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
0033FF8D  41 8B C5                        mov eax, r13d
0033FF90  83 E0 06                        and eax, 6
0033FF93  3C 06                           cmp al, 6
0033FF95  0F 84 73 08 00 00               je 0x14034080e
0033FF9B  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
0033FFA2  E9 33 0B 00 00                  jmp 0x140340ada
0033FFA7  41 0F B6 C7                     movzx eax, r15b
0033FFAB  24 01                           and al, 1
0033FFAD  88 87 AC 05 00 00               mov byte ptr [rdi + 0x5ac], al
0033FFB3  41 D1 EF                        shr r15d, 1
0033FFB6  44 89 BF 98 05 00 00            mov dword ptr [rdi + 0x598], r15d
0033FFBD  45 85 C0                        test r8d, r8d
0033FFC0  79 09                           jns 0x14033ffcb
0033FFC2  41 8B C8                        mov ecx, r8d
0033FFC5  E8 86 6A FB FF                  call 0x1402f6a50
0033FFCA  CC                              int3
0033FFCB  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
0033FFD2  E8 C9 E5 EC FF                  call 0x14020e5a0
0033FFD7  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0033FFDC  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
0033FFE4  48 83 BF B8 00 00 00 00         cmp qword ptr [rdi + 0xb8], 0
0033FFEC  75 1B                           jne 0x140340009
0033FFEE  49 8B 04 24                     mov rax, qword ptr [r12]
0033FFF2  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
0033FFF9  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0033FFFE  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
00340002  33 C0                           xor eax, eax
00340004  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00340009  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340010  E8 AB 19 F1 FF                  call 0x1402519c0
00340015  41 8B 06                        mov eax, dword ptr [r14]
00340018  2B 47 08                        sub eax, dword ptr [rdi + 8]
0034001B  48 03 87 B8 00 00 00            add rax, qword ptr [rdi + 0xb8]
00340022  49 89 04 24                     mov qword ptr [r12], rax
00340026  45 33 C0                        xor r8d, r8d
00340029  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0034002E  E9 5A FF FF FF                  jmp 0x14033ff8d
00340033  66 44 39 3F                     cmp word ptr [rdi], r15w
00340037  0F 85 8B FD FF FF               jne 0x14033fdc8
0034003D  49 8B 06                        mov rax, qword ptr [r14]
00340040  48 3B 47 20                     cmp rax, qword ptr [rdi + 0x20]
00340044  0F 8D 7E FD FF FF               jge 0x14033fdc8
0034004A  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0034004E  48 3B C1                        cmp rax, rcx
00340051  0F 8D 69 FD FF FF               jge 0x14033fdc0
00340057  48 3B D9                        cmp rbx, rcx
0034005A  0F 8D 65 08 00 00               jge 0x1403408c5
00340060  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
00340064  48 83 EF 10                     sub rdi, 0x10
00340068  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00340070  EB C1                           jmp 0x140340033
00340072  49 8B 0E                        mov rcx, qword ptr [r14]
00340075  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0034007A  48 2B D9                        sub rbx, rcx
0034007D  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00340082  8B D1                           mov edx, ecx
00340084  81 E2 FF 0F 00 00               and edx, 0xfff
0034008A  44 8D 24 13                     lea r12d, [rbx + rdx]
0034008E  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00340093  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00340098  44 03 C2                        add r8d, edx
0034009B  44 89 44 24 58                  mov dword ptr [rsp + 0x58], r8d
003400A0  44 0F B6 94 24 48 01 00 00      movzx r10d, byte ptr [rsp + 0x148]
003400A9  45 84 D2                        test r10b, r10b
003400AC  75 0E                           jne 0x1403400bc
003400AE  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
003400B4  A8 04                           test al, 4
003400B6  0F 84 4D 03 00 00               je 0x140340409
003400BC  44 8B C9                        mov r9d, ecx
003400BF  80 BC 24 50 01 00 00 00         cmp byte ptr [rsp + 0x150], 0
003400C7  0F 85 3C 03 00 00               jne 0x140340409
003400CD  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
003400D1  F7 86 98 00 00 00 00 02 00 00   test dword ptr [rsi + 0x98], 0x200
003400DB  41 8B C2                        mov eax, r10d
003400DE  41 0F 44 C3                     cmove eax, r11d
003400E2  88 84 24 48 01 00 00            mov byte ptr [rsp + 0x148], al
003400E9  41 81 C4 FF 0F 00 00            add r12d, 0xfff
003400F0  41 81 E4 00 F0 FF FF            and r12d, 0xfffff000
003400F7  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
003400FC  41 81 E1 FF 0F 00 00            and r9d, 0xfff
00340103  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
0034010B  4C 29 09                        sub qword ptr [rcx], r9
0034010E  81 64 24 68 00 F0 FF FF         and dword ptr [rsp + 0x68], 0xfffff000
00340116  45 3B E0                        cmp r12d, r8d
00340119  45 0F 47 E0                     cmova r12d, r8d
0034011D  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00340122  41 F6 C5 01                     test r13b, 1
00340126  0F 84 0F 01 00 00               je 0x14034023b
0034012C  BA C0 00 00 00                  mov edx, 0xc0
00340131  B9 00 06 00 00                  mov ecx, 0x600
00340136  41 B8 43 63 42 63               mov r8d, 0x63426343
0034013C  E8 CF 1E 84 00                  call 0x140b82010
00340141  48 8B D8                        mov rbx, rax
00340144  48 85 C0                        test rax, rax
00340147  0F 84 28 01 00 00               je 0x140340275
0034014D  66 44 89 38                     mov word ptr [rax], r15w
00340151  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00340156  48 89 43 08                     mov qword ptr [rbx + 8], rax
0034015A  44 89 63 04                     mov dword ptr [rbx + 4], r12d
0034015E  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00340163  4C 03 C0                        add r8, rax
00340166  4C 89 43 20                     mov qword ptr [rbx + 0x20], r8
0034016A  48 89 B3 B0 00 00 00            mov qword ptr [rbx + 0xb0], rsi
00340171  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00340174  FF C0                           inc eax
00340176  89 43 40                        mov dword ptr [rbx + 0x40], eax
00340179  48 8D 4B 48                     lea rcx, [rbx + 0x48]
0034017D  BA FF FF FF FF                  mov edx, 0xffffffff
00340182  E8 89 F5 0D 00                  call 0x14041f710
00340187  45 33 C0                        xor r8d, r8d
0034018A  33 D2                           xor edx, edx
0034018C  48 8D 4E 68                     lea rcx, [rsi + 0x68]
00340190  E8 9B 00 ED FF                  call 0x140210230
00340195  4C 8B F8                        mov r15, rax
00340198  F0 48 0F BA 6E 68 00            lock bts qword ptr [rsi + 0x68], 0
0034019F  73 10                           jae 0x1403401b1
003401A1  4C 8D 46 68                     lea r8, [rsi + 0x68]
003401A5  48 8B D0                        mov rdx, rax
003401A8  48 8D 4E 68                     lea rcx, [rsi + 0x68]
003401AC  E8 DF FA EC FF                  call 0x14020fc90
003401B1  4D 85 FF                        test r15, r15
003401B4  74 05                           je 0x1403401bb
003401B6  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
003401BB  48 8D 43 10                     lea rax, [rbx + 0x10]
003401BF  48 83 C7 10                     add rdi, 0x10
003401C3  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
003401C7  48 39 3A                        cmp qword ptr [rdx], rdi
003401CA  0F 84 B0 00 00 00               je 0x140340280
003401D0  B9 03 00 00 00                  mov ecx, 3
003401D5  CD 29                           int 0x29
003401D7  85 D2                           test edx, edx
003401D9  0F 84 6A 02 00 00               je 0x140340449
003401DF  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
003401E2  FF C0                           inc eax
003401E4  89 47 40                        mov dword ptr [rdi + 0x40], eax
003401E7  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
003401EE  E8 CD 17 F1 FF                  call 0x1402519c0
003401F3  45 33 C0                        xor r8d, r8d
003401F6  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
003401FB  44 38 84 24 48 01 00 00         cmp byte ptr [rsp + 0x148], r8b
00340203  75 18                           jne 0x14034021d
00340205  48 8D 4F 48                     lea rcx, [rdi + 0x48]
00340209  B2 01                           mov dl, 1
0034020B  41 F6 C5 02                     test r13b, 2
0034020F  0F 85 1A 05 00 00               jne 0x14034072f
00340215  E8 E6 D8 07 00                  call 0x1403bdb00
0034021A  45 33 C0                        xor r8d, r8d
0034021D  41 8B 06                        mov eax, dword ptr [r14]
00340220  2B 47 08                        sub eax, dword ptr [rdi + 8]
00340223  48 03 87 B8 00 00 00            add rax, qword ptr [rdi + 0xb8]
0034022A  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
00340232  49 89 04 24                     mov qword ptr [r12], rax
00340236  E9 EE FD FF FF                  jmp 0x140340029
0034023B  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00340240  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00340245  48 8B D7                        mov rdx, rdi
00340248  48 8B CE                        mov rcx, rsi
0034024B  E8 54 F3 0D 00                  call 0x14041f5a4
00340250  48 8B F8                        mov rdi, rax
00340253  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00340258  48 85 C0                        test rax, rax
0034025B  0F 85 26 02 00 00               jne 0x140340487
00340261  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00340265  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
0034026D  45 33 C0                        xor r8d, r8d
00340270  E9 18 FD FF FF                  jmp 0x14033ff8d
00340275  45 33 DB                        xor r11d, r11d
00340278  41 8B DB                        mov ebx, r11d
0034027B  E9 8A 00 00 00                  jmp 0x14034030a
00340280  48 89 38                        mov qword ptr [rax], rdi
00340283  48 89 50 08                     mov qword ptr [rax + 8], rdx
00340287  48 89 02                        mov qword ptr [rdx], rax
0034028A  48 89 47 08                     mov qword ptr [rdi + 8], rax
0034028E  48 81 7E 20 00 00 00 02         cmp qword ptr [rsi + 0x20], 0x2000000
00340296  7E 1F                           jle 0x1403402b7
00340298  F7 86 98 00 00 00 00 02 00 00   test dword ptr [rsi + 0x98], 0x200
003402A2  74 13                           je 0x1403402b7
003402A4  41 B8 01 00 00 00               mov r8d, 1
003402AA  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
003402AF  48 8B CE                        mov rcx, rsi
003402B2  E8 ED F5 0D 00                  call 0x14041f8a4
003402B7  0F 0D 4E 68                     prefetchw byte ptr [rsi + 0x68]
003402BB  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
003402BF  48 8B C8                        mov rcx, rax
003402C2  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
003402C6  48 8D 50 F0                     lea rdx, [rax - 0x10]
003402CA  48 83 F9 10                     cmp rcx, 0x10
003402CE  B9 00 00 00 00                  mov ecx, 0
003402D3  48 0F 46 D1                     cmovbe rdx, rcx
003402D7  A8 02                           test al, 2
003402D9  0F 85 F4 00 00 00               jne 0x1403403d3
003402DF  F0 48 0F B1 56 68               lock cmpxchg qword ptr [rsi + 0x68], rdx
003402E5  0F 85 E8 00 00 00               jne 0x1403403d3
003402EB  48 8D 4E 68                     lea rcx, [rsi + 0x68]
003402EF  E8 0C 13 FA FF                  call 0x1402e1600
003402F4  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
003402FA  A8 02                           test al, 2
003402FC  74 09                           je 0x140340307
003402FE  48 8D 4B 48                     lea rcx, [rbx + 0x48]
00340302  E8 39 F5 0D 00                  call 0x14041f840
00340307  45 33 DB                        xor r11d, r11d
0034030A  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00340312  48 8B FB                        mov rdi, rbx
00340315  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0034031A  48 85 DB                        test rbx, rbx
0034031D  0F 85 9F 01 00 00               jne 0x1403404c2
00340323  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
0034032A  E8 91 16 F1 FF                  call 0x1402519c0
0034032F  33 C0                           xor eax, eax
00340331  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00340335  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0034033A  E8 11 67 FB FF                  call 0x1402f6a50
0034033F  80 BC 24 48 01 00 00 00         cmp byte ptr [rsp + 0x148], 0
00340347  0F 84 94 00 00 00               je 0x1403403e1
0034034D  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
00340350  FF C0                           inc eax
00340352  89 47 40                        mov dword ptr [rdi + 0x40], eax
00340355  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
0034035C  E8 5F 16 F1 FF                  call 0x1402519c0
00340361  33 DB                           xor ebx, ebx
00340363  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00340367  4D 8B 0C 24                     mov r9, qword ptr [r12]
0034036B  45 33 C0                        xor r8d, r8d
0034036E  33 D2                           xor edx, edx
00340370  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00340373  E8 48 67 FB FF                  call 0x1402f6ac0
00340378  84 C0                           test al, al
0034037A  0F 84 5E 04 00 00               je 0x1403407de
00340380  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340387  E8 14 E2 EC FF                  call 0x14020e5a0
0034038C  48 39 9F B8 00 00 00            cmp qword ptr [rdi + 0xb8], rbx
00340393  75 19                           jne 0x1403403ae
00340395  49 8B 04 24                     mov rax, qword ptr [r12]
00340399  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
003403A0  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003403A5  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
003403A9  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003403AE  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
003403B5  E8 06 16 F1 FF                  call 0x1402519c0
003403BA  41 8B 06                        mov eax, dword ptr [r14]
003403BD  2B 47 08                        sub eax, dword ptr [rdi + 8]
003403C0  48 03 87 B8 00 00 00            add rax, qword ptr [rdi + 0xb8]
003403C7  45 33 C0                        xor r8d, r8d
003403CA  49 89 04 24                     mov qword ptr [r12], rax
003403CE  E9 56 FC FF FF                  jmp 0x140340029
003403D3  48 8D 4E 68                     lea rcx, [rsi + 0x68]
003403D7  E8 F4 34 F2 FF                  call 0x1402638d0
003403DC  E9 0A FF FF FF                  jmp 0x1403402eb
003403E1  48 8D 4F 48                     lea rcx, [rdi + 0x48]
003403E5  33 D2                           xor edx, edx
003403E7  E8 14 D7 07 00                  call 0x1403bdb00
003403EC  84 C0                           test al, al
003403EE  0F 85 59 FF FF FF               jne 0x14034034d
003403F4  45 33 C0                        xor r8d, r8d
003403F7  41 8B F8                        mov edi, r8d
003403FA  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
003403FF  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00340404  E9 84 FB FF FF                  jmp 0x14033ff8d
00340409  BB 02 00 00 00                  mov ebx, 2
0034040E  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00340412  85 D2                           test edx, edx
00340414  75 17                           jne 0x14034042d
00340416  81 BC 24 40 01 00 00 00 10 00 00  cmp dword ptr [rsp + 0x140], 0x1000
00340421  B8 03 00 00 00                  mov eax, 3
00340426  0F 43 D8                        cmovae ebx, eax
00340429  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
0034042D  44 8B C9                        mov r9d, ecx
00340430  41 F7 C4 FF 0F 00 00            test r12d, 0xfff
00340437  0F 85 94 FC FF FF               jne 0x1403400d1
0034043D  83 CB 04                        or ebx, 4
00340440  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00340444  E9 88 FC FF FF                  jmp 0x1403400d1
00340449  80 BC 24 48 01 00 00 00         cmp byte ptr [rsp + 0x148], 0
00340451  75 13                           jne 0x140340466
00340453  48 8D 4F 48                     lea rcx, [rdi + 0x48]
00340457  33 D2                           xor edx, edx
00340459  E8 A2 D6 07 00                  call 0x1403bdb00
0034045E  84 C0                           test al, al
00340460  0F 84 0F FB FF FF               je 0x14033ff75
00340466  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
00340469  FF C0                           inc eax
0034046B  89 47 40                        mov dword ptr [rdi + 0x40], eax
0034046E  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340475  E8 46 15 F1 FF                  call 0x1402519c0
0034047A  45 33 C0                        xor r8d, r8d
0034047D  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00340482  E9 96 FD FF FF                  jmp 0x14034021d
00340487  80 BC 24 48 01 00 00 00         cmp byte ptr [rsp + 0x148], 0
0034048F  0F 85 A7 02 00 00               jne 0x14034073c
00340495  48 8D 48 48                     lea rcx, [rax + 0x48]
00340499  33 D2                           xor edx, edx
0034049B  E8 60 D6 07 00                  call 0x1403bdb00
003404A0  84 C0                           test al, al
003404A2  0F 85 94 02 00 00               jne 0x14034073c
003404A8  33 C0                           xor eax, eax
003404AA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003404AF  45 33 C9                        xor r9d, r9d
003404B2  4C 8B C7                        mov r8, rdi
003404B5  BA 7A 02 02 00                  mov edx, 0x2027a
003404BA  8D 48 34                        lea ecx, [rax + 0x34]
003404BD  E8 9E D1 1B 00                  call 0x1404fd660
003404C2  80 BC 24 48 01 00 00 00         cmp byte ptr [rsp + 0x148], 0
003404CA  75 58                           jne 0x140340524
003404CC  4C 8D 43 48                     lea r8, [rbx + 0x48]
003404D0  41 F6 C5 02                     test r13b, 2
003404D4  0F 85 29 02 00 00               jne 0x140340703
003404DA  41 0F B7 48 1A                  movzx ecx, word ptr [r8 + 0x1a]
003404DF  0F B6 C1                        movzx eax, cl
003404E2  24 41                           and al, 0x41
003404E4  3C 01                           cmp al, 1
003404E6  0F 84 A1 03 00 00               je 0x14034088d
003404EC  F6 C1 01                        test cl, 1
003404EF  0F 85 40 05 00 00               jne 0x140340a35
003404F5  33 D2                           xor edx, edx
003404F7  49 8B C8                        mov rcx, r8
003404FA  E8 C1 0C 00 00                  call 0x1403411c0
003404FF  88 84 24 40 01 00 00            mov byte ptr [rsp + 0x140], al
00340506  84 C0                           test al, al
00340508  75 1A                           jne 0x140340524
0034050A  33 C0                           xor eax, eax
0034050C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00340511  45 33 C9                        xor r9d, r9d
00340514  4C 8B C3                        mov r8, rbx
00340517  BA 1A 02 02 00                  mov edx, 0x2021a
0034051C  8D 48 34                        lea ecx, [rax + 0x34]
0034051F  E8 3C D1 1B 00                  call 0x1404fd660
00340524  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
0034052B  E8 90 14 F1 FF                  call 0x1402519c0
00340530  45 33 C0                        xor r8d, r8d
00340533  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00340538  41 F6 C5 04                     test r13b, 4
0034053C  0F 85 AF 01 00 00               jne 0x1403406f1
00340542  4C 8B AC 24 68 01 00 00         mov r13, qword ptr [rsp + 0x168]
0034054A  49 8B 7D 00                     mov rdi, qword ptr [r13]
0034054E  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00340556  8B CF                           mov ecx, edi
00340558  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
00340561  41 BA 01 00 00 00               mov r10d, 1
00340567  45 8B CA                        mov r9d, r10d
0034056A  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
0034056F  44 89 84 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r8d
00340577  44 89 44 24 7C                  mov dword ptr [rsp + 0x7c], r8d
0034057C  41 8B D0                        mov edx, r8d
0034057F  89 94 24 90 00 00 00            mov dword ptr [rsp + 0x90], edx
00340586  44 88 8C 24 30 01 00 00         mov byte ptr [rsp + 0x130], r9b
0034058E  81 E1 FF 0F 00 00               and ecx, 0xfff
00340594  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
00340598  48 81 C3 FF 0F 00 00            add rbx, 0xfff
0034059F  48 03 D9                        add rbx, rcx
003405A2  48 C1 EB 0C                     shr rbx, 0xc
003405A6  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
003405AA  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
003405B1  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
003405B9  41 0F B6 8F AC 05 00 00         movzx ecx, byte ptr [r15 + 0x5ac]
003405C1  41 8B 87 98 05 00 00            mov eax, dword ptr [r15 + 0x598]
003405C8  44 8D 24 41                     lea r12d, [rcx + rax*2]
003405CC  85 DB                           test ebx, ebx
003405CE  0F 84 94 00 00 00               je 0x140340668
003405D4  41 C6 87 AC 05 00 00 01         mov byte ptr [r15 + 0x5ac], 1
003405DC  8D 43 FF                        lea eax, [rbx - 1]
003405DF  41 3B 87 98 05 00 00            cmp eax, dword ptr [r15 + 0x598]
003405E6  0F 87 8C 02 00 00               ja 0x140340878
003405EC  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
003405F1  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
003405F5  44 85 C8                        test eax, r9d
003405F8  45 0F 45 C2                     cmovne r8d, r10d
003405FC  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
00340601  85 C0                           test eax, eax
00340603  0F 85 9B 02 00 00               jne 0x1403408a4
00340609  44 8B EB                        mov r13d, ebx
0034060C  41 8B C5                        mov eax, r13d
0034060F  C1 E0 0C                        shl eax, 0xc
00340612  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00340617  4C 8D 8C 24 30 01 00 00         lea r9, [rsp + 0x130]
0034061F  8B D0                           mov edx, eax
00340621  48 8B CF                        mov rcx, rdi
00340624  E8 37 66 FB FF                  call 0x1402f6c60
00340629  8B D0                           mov edx, eax
0034062B  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
00340632  85 C0                           test eax, eax
00340634  78 32                           js 0x140340668
00340636  48 03 7C 24 70                  add rdi, qword ptr [rsp + 0x70]
0034063B  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00340643  41 2B DD                        sub ebx, r13d
00340646  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
0034064A  41 B9 02 00 00 00               mov r9d, 2
00340650  83 FB 01                        cmp ebx, 1
00340653  B8 04 00 00 00                  mov eax, 4
00340658  44 0F 44 C8                     cmove r9d, eax
0034065C  44 8D 50 FD                     lea r10d, [rax - 3]
00340660  45 33 C0                        xor r8d, r8d
00340663  E9 64 FF FF FF                  jmp 0x1403405cc
00340668  41 0F B6 C4                     movzx eax, r12b
0034066C  24 01                           and al, 1
0034066E  41 88 87 AC 05 00 00            mov byte ptr [r15 + 0x5ac], al
00340675  41 D1 EC                        shr r12d, 1
00340678  45 89 A7 98 05 00 00            mov dword ptr [r15 + 0x598], r12d
0034067F  85 D2                           test edx, edx
00340681  79 08                           jns 0x14034068b
00340683  8B CA                           mov ecx, edx
00340685  E8 C6 63 FB FF                  call 0x1402f6a50
0034068A  CC                              int3
0034068B  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340692  E8 09 DF EC FF                  call 0x14020e5a0
00340697  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0034069C  4C 8B AC 24 68 01 00 00         mov r13, qword ptr [rsp + 0x168]
003406A4  48 83 BF B8 00 00 00 00         cmp qword ptr [rdi + 0xb8], 0
003406AC  75 1B                           jne 0x1403406c9
003406AE  49 8B 45 00                     mov rax, qword ptr [r13]
003406B2  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
003406B9  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003406BE  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
003406C2  33 C0                           xor eax, eax
003406C4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003406C9  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
003406D0  E8 EB 12 F1 FF                  call 0x1402519c0
003406D5  41 8B 06                        mov eax, dword ptr [r14]
003406D8  2B 47 08                        sub eax, dword ptr [rdi + 8]
003406DB  48 03 87 B8 00 00 00            add rax, qword ptr [rdi + 0xb8]
003406E2  49 89 45 00                     mov qword ptr [r13], rax
003406E6  44 8B AC 24 58 01 00 00         mov r13d, dword ptr [rsp + 0x158]
003406EE  45 33 C0                        xor r8d, r8d
003406F1  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
003406F9  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
003406FE  E9 8A F8 FF FF                  jmp 0x14033ff8d
00340703  33 D2                           xor edx, edx
00340705  49 8B C8                        mov rcx, r8
00340708  E8 13 47 ED FF                  call 0x140214e20
0034070D  84 C0                           test al, al
0034070F  0F 85 0F FE FF FF               jne 0x140340524
00340715  33 C0                           xor eax, eax
00340717  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0034071C  45 33 C9                        xor r9d, r9d
0034071F  4C 8B C3                        mov r8, rbx
00340722  BA 13 02 02 00                  mov edx, 0x20213
00340727  8D 48 34                        lea ecx, [rax + 0x34]
0034072A  E8 31 CF 1B 00                  call 0x1404fd660
0034072F  E8 EC 46 ED FF                  call 0x140214e20
00340734  45 33 C0                        xor r8d, r8d
00340737  E9 E1 FA FF FF                  jmp 0x14034021d
0034073C  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340743  E8 78 12 F1 FF                  call 0x1402519c0
00340748  45 33 FF                        xor r15d, r15d
0034074B  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00340750  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
00340758  4D 8B 09                        mov r9, qword ptr [r9]
0034075B  45 33 C0                        xor r8d, r8d
0034075E  8B D3                           mov edx, ebx
00340760  41 8B CC                        mov ecx, r12d
00340763  E8 58 63 FB FF                  call 0x1402f6ac0
00340768  84 C0                           test al, al
0034076A  0F 84 89 00 00 00               je 0x1403407f9
00340770  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340777  E8 24 DE EC FF                  call 0x14020e5a0
0034077C  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
00340784  4C 39 BF B8 00 00 00            cmp qword ptr [rdi + 0xb8], r15
0034078B  0F 85 1D FC FF FF               jne 0x1403403ae
00340791  49 8B 04 24                     mov rax, qword ptr [r12]
00340795  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
0034079C  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003407A1  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
003407A5  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
003407AA  E9 FF FB FF FF                  jmp 0x1403403ae
003407AF  83 F8 0F                        cmp eax, 0xf
003407B2  0F 86 02 01 00 00               jbe 0x1403408ba
003407B8  C7 87 98 05 00 00 0F 00 00 00   mov dword ptr [rdi + 0x598], 0xf
003407C2  E9 61 F7 FF FF                  jmp 0x14033ff28
003407C7  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003407CC  45 33 C9                        xor r9d, r9d
003407CF  41 8D 51 0F                     lea edx, [r9 + 0xf]
003407D3  B9 C6 01 00 00                  mov ecx, 0x1c6
003407D8  E8 83 CE 1B 00                  call 0x1404fd660
003407DD  CC                              int3
003407DE  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
003407E2  45 33 C0                        xor r8d, r8d
003407E5  E9 A3 F7 FF FF                  jmp 0x14033ff8d
003407EA  B2 01                           mov dl, 1
003407EC  49 8B C8                        mov rcx, r8
003407EF  E8 2C 46 ED FF                  call 0x140214e20
003407F4  E9 8C F6 FF FF                  jmp 0x14033fe85
003407F9  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
003407FE  4C 8B A4 24 68 01 00 00         mov r12, qword ptr [rsp + 0x168]
00340806  45 33 C0                        xor r8d, r8d
00340809  E9 7F F7 FF FF                  jmp 0x14033ff8d
0034080E  48 85 FF                        test rdi, rdi
00340811  0F 84 84 F7 FF FF               je 0x14033ff9b
00340817  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
0034081E  48 83 BF B8 00 00 00 00         cmp qword ptr [rdi + 0xb8], 0
00340826  0F 84 AE 02 00 00               je 0x140340ada
0034082C  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00340830  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
00340834  41 8B CF                        mov ecx, r15d
00340837  F0 0F C1 48 10                  lock xadd dword ptr [rax + 0x10], ecx
0034083C  FF C9                           dec ecx
0034083E  66 85 C9                        test cx, cx
00340841  75 20                           jne 0x140340863
00340843  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
0034084A  48 85 C9                        test rcx, rcx
0034084D  74 0A                           je 0x140340859
0034084F  45 33 C0                        xor r8d, r8d
00340852  33 D2                           xor edx, edx
00340854  E8 B7 EA FF FF                  call 0x14033f310
00340859  F0 FF 8B 28 02 00 00            lock dec dword ptr [rbx + 0x228]
00340860  45 33 C0                        xor r8d, r8d
00340863  4C 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], r8
0034086A  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
0034086E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00340873  E9 62 02 00 00                  jmp 0x140340ada
00340878  83 F8 0F                        cmp eax, 0xf
0034087B  76 58                           jbe 0x1403408d5
0034087D  41 C7 87 98 05 00 00 0F 00 00 00  mov dword ptr [r15 + 0x598], 0xf
00340888  E9 5F FD FF FF                  jmp 0x1403405ec
0034088D  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00340892  45 33 C9                        xor r9d, r9d
00340895  41 8D 51 0F                     lea edx, [r9 + 0xf]
00340899  B9 C6 01 00 00                  mov ecx, 0x1c6
0034089E  E8 BD CD 1B 00                  call 0x1404fd660
003408A3  CC                              int3
003408A4  41 83 F9 02                     cmp r9d, 2
003408A8  44 8D 6B FF                     lea r13d, [rbx - 1]
003408AC  0F 84 5A FD FF FF               je 0x14034060c
003408B2  45 8B EA                        mov r13d, r10d
003408B5  E9 52 FD FF FF                  jmp 0x14034060c
003408BA  89 87 98 05 00 00               mov dword ptr [rdi + 0x598], eax
003408C0  E9 63 F6 FF FF                  jmp 0x14033ff28
003408C5  48 8B D9                        mov rbx, rcx
003408C8  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
003408D0  E9 8B F7 FF FF                  jmp 0x140340060
003408D5  41 89 87 98 05 00 00            mov dword ptr [r15 + 0x598], eax
003408DC  E9 0B FD FF FF                  jmp 0x1403405ec
003408E1  F7 86 98 00 00 00 00 02 00 00   test dword ptr [rsi + 0x98], 0x200
003408EB  0F 84 53 F4 FF FF               je 0x14033fd44
003408F1  48 81 F9 00 00 00 02            cmp rcx, 0x2000000
003408F8  7E 1C                           jle 0x140340916
003408FA  41 B0 01                        mov r8b, 1
003408FD  48 8B D7                        mov rdx, rdi
00340900  48 8B CE                        mov rcx, rsi
00340903  E8 88 10 00 00                  call 0x140341990
00340908  48 8B F8                        mov rdi, rax
0034090B  41 BB 01 00 00 00               mov r11d, 1
00340911  E9 32 F4 FF FF                  jmp 0x14033fd48
00340916  8B C1                           mov eax, ecx
00340918  C1 F8 12                        sar eax, 0x12
0034091B  FF C0                           inc eax
0034091D  83 E0 FE                        and eax, 0xfffffffe
00340920  99                              cdq
00340921  2B C2                           sub eax, edx
00340923  D1 F8                           sar eax, 1
00340925  C1 E0 13                        shl eax, 0x13
00340928  2D 00 00 08 00                  sub eax, 0x80000
0034092D  48 98                           cdqe
0034092F  4C 3B C0                        cmp r8, rax
00340932  0F 8D 0C F4 FF FF               jge 0x14033fd44
00340938  45 85 C9                        test r9d, r9d
0034093B  0F 85 85 01 00 00               jne 0x140340ac6
00340941  81 F9 00 00 10 00               cmp ecx, 0x100000
00340947  0F 86 83 01 00 00               jbe 0x140340ad0
0034094D  8B C9                           mov ecx, ecx
0034094F  48 C1 E9 12                     shr rcx, 0x12
00340953  48 C1 E1 03                     shl rcx, 3
00340957  48 03 4E 58                     add rcx, qword ptr [rsi + 0x58]
0034095B  48 C1 FF 13                     sar rdi, 0x13
0034095F  48 C1 E7 04                     shl rdi, 4
00340963  48 03 F9                        add rdi, rcx
00340966  E9 DD F3 FF FF                  jmp 0x14033fd48
0034096B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00340970  F6 C1 01                        test cl, 1
00340973  0F 84 02 F5 FF FF               je 0x14033fe7b
00340979  B2 01                           mov dl, 1
0034097B  49 8B C8                        mov rcx, r8
0034097E  E8 95 D2 07 00                  call 0x1403bdc18
00340983  E9 FD F4 FF FF                  jmp 0x14033fe85
00340988  44 0F 20 C2                     mov rdx, cr8
0034098C  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
00340995  80 FA 01                        cmp dl, 1
00340998  76 1A                           jbe 0x1403409b4
0034099A  44 0F B6 C2                     movzx r8d, dl
0034099E  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003409A3  33 D2                           xor edx, edx
003409A5  B9 C6 01 00 00                  mov ecx, 0x1c6
003409AA  44 8D 4A 01                     lea r9d, [rdx + 1]
003409AE  E8 AD CC 1B 00                  call 0x1404fd660
003409B3  CC                              int3
003409B4  41 0F B6 82 C0 00 00 00         movzx eax, byte ptr [r10 + 0xc0]
003409BC  A8 02                           test al, 2
003409BE  74 1A                           je 0x1403409da
003409C0  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003409C5  45 33 C9                        xor r9d, r9d
003409C8  45 33 C0                        xor r8d, r8d
003409CB  41 8D 51 06                     lea edx, [r9 + 6]
003409CF  B9 C6 01 00 00                  mov ecx, 0x1c6
003409D4  E8 87 CC 1B 00                  call 0x1404fd660
003409D9  CC                              int3
003409DA  80 FA 01                        cmp dl, 1
003409DD  73 8C                           jae 0x14034096b
003409DF  41 F7 42 74 00 04 00 00         test dword ptr [r10 + 0x74], 0x400
003409E7  75 82                           jne 0x14034096b
003409E9  45 39 9A E4 01 00 00            cmp dword ptr [r10 + 0x1e4], r11d
003409F0  0F 85 75 FF FF FF               jne 0x14034096b
003409F6  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003409FB  45 33 C9                        xor r9d, r9d
003409FE  45 33 C0                        xor r8d, r8d
00340A01  41 8D 51 07                     lea edx, [r9 + 7]
00340A05  B9 C6 01 00 00                  mov ecx, 0x1c6
00340A0A  E8 51 CC 1B 00                  call 0x1404fd660
00340A0F  CC                              int3
00340A10  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00340A15  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
00340A1D  F6 C1 01                        test cl, 1
00340A20  0F 84 CF FA FF FF               je 0x1403404f5
00340A26  33 D2                           xor edx, edx
00340A28  49 8B C8                        mov rcx, r8
00340A2B  E8 E8 D1 07 00                  call 0x1403bdc18
00340A30  E9 CA FA FF FF                  jmp 0x1403404ff
00340A35  44 0F 20 C2                     mov rdx, cr8
00340A39  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
00340A42  80 FA 02                        cmp dl, 2
00340A45  76 1A                           jbe 0x140340a61
00340A47  44 0F B6 C2                     movzx r8d, dl
00340A4B  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00340A50  33 D2                           xor edx, edx
00340A52  B9 C6 01 00 00                  mov ecx, 0x1c6
00340A57  44 8D 4A 02                     lea r9d, [rdx + 2]
00340A5B  E8 00 CC 1B 00                  call 0x1404fd660
00340A60  CC                              int3
00340A61  72 29                           jb 0x140340a8c
00340A63  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
00340A6B  A9 01 00 01 00                  test eax, 0x10001
00340A70  74 1A                           je 0x140340a8c
00340A72  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00340A77  45 33 C9                        xor r9d, r9d
00340A7A  45 33 C0                        xor r8d, r8d
00340A7D  41 8D 51 05                     lea edx, [r9 + 5]
00340A81  B9 C6 01 00 00                  mov ecx, 0x1c6
00340A86  E8 D5 CB 1B 00                  call 0x1404fd660
00340A8B  CC                              int3
00340A8C  41 0F B6 81 C0 00 00 00         movzx eax, byte ptr [r9 + 0xc0]
00340A94  A8 02                           test al, 2
00340A96  0F 85 24 FF FF FF               jne 0x1403409c0
00340A9C  80 FA 01                        cmp dl, 1
00340A9F  0F 83 6B FF FF FF               jae 0x140340a10
00340AA5  41 F7 41 74 00 04 00 00         test dword ptr [r9 + 0x74], 0x400
00340AAD  0F 85 5D FF FF FF               jne 0x140340a10
00340AB3  41 83 B9 E4 01 00 00 00         cmp dword ptr [r9 + 0x1e4], 0
00340ABB  0F 84 35 FF FF FF               je 0x1403409f6
00340AC1  E9 4A FF FF FF                  jmp 0x140340a10
00340AC6  B9 FF FF FF FF                  mov ecx, 0xffffffff
00340ACB  E9 87 FE FF FF                  jmp 0x140340957
00340AD0  B9 20 00 00 00                  mov ecx, 0x20
00340AD5  E9 7D FE FF FF                  jmp 0x140340957
00340ADA  83 7C 24 34 00                  cmp dword ptr [rsp + 0x34], 0
00340ADF  74 0C                           je 0x140340aed
00340AE1  48 8D 8E 20 01 00 00            lea rcx, [rsi + 0x120]
00340AE8  E8 D3 0E F1 FF                  call 0x1402519c0
00340AED  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00340AF2  48 85 C0                        test rax, rax
00340AF5  74 35                           je 0x140340b2c
00340AF7  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
00340AFB  F0 44 0F C1 78 10               lock xadd dword ptr [rax + 0x10], r15d
00340B01  41 FF CF                        dec r15d
00340B04  66 45 85 FF                     test r15w, r15w
00340B08  75 1D                           jne 0x140340b27
00340B0A  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
00340B11  48 85 C9                        test rcx, rcx
00340B14  74 0A                           je 0x140340b20
00340B16  45 33 C0                        xor r8d, r8d
00340B19  33 D2                           xor edx, edx
00340B1B  E8 F0 E7 FF FF                  call 0x14033f310
00340B20  F0 FF 8B 28 02 00 00            lock dec dword ptr [rbx + 0x228]
00340B27  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00340B2C  41 F6 C5 04                     test r13b, 4
00340B30  74 11                           je 0x140340b43
00340B32  49 8B 1E                        mov rbx, qword ptr [r14]
00340B35  48 81 7E 20 00 00 00 02         cmp qword ptr [rsi + 0x20], 0x2000000
00340B3D  0F 8F 20 01 00 00               jg 0x140340c63
00340B43  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00340B48  74 33                           je 0x140340b7d
00340B4A  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00340B52  48 89 38                        mov qword ptr [rax], rdi
00340B55  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00340B59  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
00340B61  48 89 08                        mov qword ptr [rax], rcx
00340B64  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
00340B69  48 81 C4 F0 00 00 00            add rsp, 0xf0
00340B70  41 5F                           pop r15
00340B72  41 5E                           pop r14
00340B74  41 5D                           pop r13
00340B76  41 5C                           pop r12
00340B78  5F                              pop rdi
00340B79  5E                              pop rsi
00340B7A  5B                              pop rbx
00340B7B  C3                              ret
00340B7C  CC                              int3
00340B7D  33 C0                           xor eax, eax
00340B7F  49 89 04 24                     mov qword ptr [r12], rax
00340B83  48 85 FF                        test rdi, rdi
00340B86  74 DC                           je 0x140340b64
00340B88  45 33 C0                        xor r8d, r8d
00340B8B  0F B6 94 24 48 01 00 00         movzx edx, byte ptr [rsp + 0x148]
00340B93  48 8B CF                        mov rcx, rdi
00340B96  E8 51 92 01 00                  call 0x140359dec
00340B9B  EB C7                           jmp 0x140340b64
00340B9D  41 0F B6 D3                     movzx edx, r11b
00340BA1  41 0F B6 C8                     movzx ecx, r8b
00340BA5  E8 52 4B 1B 00                  call 0x1404f56fc
00340BAA  4C 8B 84 24 30 01 00 00         mov r8, qword ptr [rsp + 0x130]
00340BB2  41 BB 01 00 00 00               mov r11d, 1
00340BB8  E9 77 F0 FF FF                  jmp 0x14033fc34
00340BBD  8B 0A                           mov ecx, dword ptr [rdx]
00340BBF  81 E1 FF FF 03 00               and ecx, 0x3ffff
00340BC5  B8 00 00 04 00                  mov eax, 0x40000
00340BCA  2B C1                           sub eax, ecx
00340BCC  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00340BD0  48 8B 1A                        mov rbx, qword ptr [rdx]
00340BD3  48 81 7E 20 00 00 00 02         cmp qword ptr [rsi + 0x20], 0x2000000
00340BDB  0F 8E 19 F0 FF FF               jle 0x14033fbfa
00340BE1  4C 89 A4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r12
00340BE9  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00340BF1  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00340BF9  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00340C01  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00340C09  4C 89 A4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r12
00340C11  8B 96 98 00 00 00               mov edx, dword ptr [rsi + 0x98]
00340C17  C1 EA 09                        shr edx, 9
00340C1A  80 E2 01                        and dl, 1
00340C1D  8B 0D 71 9C AC 00               mov ecx, dword ptr [rip + 0xac9c71]
00340C23  FF C9                           dec ecx
00340C25  4C 8D 84 24 C0 00 00 00         lea r8, [rsp + 0xc0]
00340C2D  E8 1E 14 14 00                  call 0x140482050
00340C32  84 C0                           test al, al
00340C34  0F 85 EA 13 3A 00               jne 0x1406e2024
00340C3A  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00340C3F  E8 0C 5E FB FF                  call 0x1402f6a50
00340C44  CC                              int3
00340C45  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00340C4A  45 33 C9                        xor r9d, r9d
00340C4D  BA 45 01 00 00                  mov edx, 0x145
00340C52  41 8D 49 34                     lea ecx, [r9 + 0x34]
00340C56  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00340C5D  E8 FE C9 1B 00                  call 0x1404fd660
00340C62  CC                              int3
00340C63  48 8B D6                        mov rdx, rsi
00340C66  41 BE 01 00 00 00               mov r14d, 1
00340C6C  41 8B CE                        mov ecx, r14d
00340C6F  E8 E4 EF F2 FF                  call 0x14026fc58
00340C74  45 33 C9                        xor r9d, r9d
00340C77  4D 8D 46 FD                     lea r8, [r14 - 3]
00340C7B  48 8B D3                        mov rdx, rbx
00340C7E  48 8B CE                        mov rcx, rsi
00340C81  E8 BA 26 F3 FF                  call 0x140273340
00340C86  48 8B D6                        mov rdx, rsi
00340C89  41 8B CE                        mov ecx, r14d
00340C8C  E8 5F F1 F9 FF                  call 0x1402dfdf0
00340C91  E9 AD FE FF FF                  jmp 0x140340b43
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPinFileData(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, unsigned __int8 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int8 v_stack_mF7;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p130;
    unsigned __int8 v_stack_p148;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (240);
    v_r12 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mF8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8);
    v_stack_mB8 = (unsigned int)(a3);
    a1 = (*(unsigned __int64 *)(a2)) + ((unsigned int)(a3));
    if (a1 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32))) goto loc_00340C45;
    *(unsigned __int64 *)(a7) = 0;
    *(unsigned __int64 *)(a8) = 0;
    if ((((unsigned __int8)((unsigned int)(a6))) & (4)) != 0) goto loc_00340BBD;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) >> (6));
    result = (unsigned int)((result) & (1));
    v_stack_m100 = 0;
    v_stack_m108 = (unsigned int)(result);
    result = CcGetVirtualAddress(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), *(unsigned __int64 *)(a2), v_stack_mD8, v_stack_mD0);
    *(unsigned __int64 *)(a8) = result;
loc_0033FBFA:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, v_stack_mD0);
    v_stack_p8 = v_cr8;
    if ((*(unsigned int *)(v_rip + 13136114)) != 0) goto loc_00340B9D;
loc_0033FC34:
    if ((*(unsigned int *)(v_rip + 13136114)) < 0) goto loc_0033FCD2;
loc_0033FC4E:
loc_0033FC50:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288)))) & (1)) != 0) goto loc_0033FCA9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288)))) & (1)) != 0) goto loc_0033FC50;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288));
    if (result != 0) {
        a1 = result;
        result = KeAbPreWait(a1, a2, v_cr8, v_stack_mD0);
    }
    result = 0;
    v_stack_m108 = 0;
    a4 = 0;
    a3 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288 + 24, result + 34, a3, a4);
    if (result == 0) goto loc_0033FC4E;
    a3 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, result, a3, a4);
    goto loc_0033FC4E;
loc_0033FCA9:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) ^ (3));
    if (condition_is_not_equal) goto loc_0033FC50;
    v_r12 = 0;
loc_0033FCD2:
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288 + 48) = (unsigned int)((unsigned __int8)(v_stack_p8));
    v_stack_mF4 = 1;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    v_r15 = (*(unsigned __int64 *)(a2)) >> (32);
    v_stack_mA0 = *(unsigned __int64 *)(a2) + v_stack_mB8 * 1;
    v_stack_m88 = 0;
    v_r12 = 0;
    v_stack_mF7 = 0;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32)) >> (32);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32)) > 0x200000ULL) goto loc_003408E1;
loc_0033FD44:
loc_0033FD48:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 16)) - (16);
    v_stack_m88 = v_rdi;
    if ((unsigned int)(v_r15) != 0) goto loc_00340033;
    if ((*(unsigned __int16 *)(v_rdi)) != 765) goto loc_0033FDC8;
    if ((*(unsigned int *)(v_rdi + 36)) != 0) goto loc_00340033;
loc_0033FD81:
    if (765 != 765) goto loc_0033FDC8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) >= (*(unsigned int *)(v_rdi + 32))) goto loc_0033FDC8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) goto loc_0033FDC0;
    v_rbx = *(unsigned __int64 *)(a2) + v_stack_mB8 * 1;
    if (((unsigned int)((unsigned int)(v_stack_mA0))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) {
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)));
        v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)));
        v_rbx = v_stack_mA0;
    }
    v_rdi = (*(unsigned __int64 *)(v_rdi + 16)) - (16);
    v_stack_m88 = v_rdi;
    goto loc_0033FD81;
loc_0033FDC0:
    v_stack_mF7 = 1;
loc_0033FDC8:
    v_stack_mE8 = v_rdi;
    if (1 == 0) goto loc_0033FF6B;
    v_rbx = v_stack_p20;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)) & (512)) == 0) { v_rbx = 1; }
    v_stack_p20 = (unsigned __int8)(v_rbx);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (1));
    if ((*(unsigned __int64 *)(v_rdi + 184)) != 0) goto loc_003401D7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (*(unsigned int *)(v_rdi + 8)));
    v_stack_mC0 = *(unsigned __int64 *)(v_rdi + 8);
    v_stack_mC8 = (unsigned int)(*(unsigned int *)(v_rdi + 4));
    if ((unsigned int)(a2) == 0) goto loc_0034033F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 64))) + 1);
    *(unsigned int *)(v_rdi + 64) = (unsigned int)(result);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, *(unsigned __int64 *)(a2), a4);
    v_r11 = 0;
    v_stack_mF4 = 0;
    if ((unsigned __int8)(v_rbx) != 0) goto loc_0033FE88;
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_003407EA;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int16 *)(v_rdi + 72 + 26))) & (65));
    if (((unsigned __int8)(result)) == 1) goto loc_003407C7;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rdi + 72 + 26))) & (1)) != 0) goto loc_00340988;
loc_0033FE7B:
    result = ExpAcquireSharedStarveExclusive(v_rdi + 72, 1, v_rdi + 72, a4);
loc_0033FE85:
    v_r11 = 0;
loc_0033FE88:
    if ((((unsigned __int8)((unsigned int)(a6))) & (4)) != 0) goto loc_00340026;
    v_stack_mB8 = *(unsigned __int64 *)(a8);
    v_stack_m94 = 0;
    v_stack_m44 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
    v_stack_mF0 = 1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a8)))) & (0xFFFULL));
    a2 = ((unsigned int)(v_stack_mC8)) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    v_stack_mA8 = (unsigned int)(a2);
    v_rbx = (*(unsigned __int64 *)(a8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mB8 = v_rbx;
loc_0033FF0A:
    if ((unsigned int)(a2) == 0) goto loc_0033FFA7;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) = 1;
    if (((unsigned int)(a2 - 1)) > (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432))) goto loc_003407AF;
loc_0033FF28:
    v_stack_m94 = 0;
    a2 = (unsigned int)((a2) << (12));
    a3 = 0;
    result = MmCheckCachedPageStates(v_rbx, a2, a3, v_stack_mF0);
    v_stack_m90 = (unsigned int)(result);
    if (sign_flag) goto loc_0033FFA7;
    v_rbx = (v_rbx) + ((unsigned int)((unsigned int)(a2)));
    v_stack_mB8 = v_rbx;
    v_r11 = 0;
    v_stack_mA8 = 0;
    goto loc_0033FF0A;
loc_0033FF6B:
    if ((((unsigned __int8)((unsigned int)(a6))) & (8)) == 0) goto loc_00340072;
loc_0033FF75:
    a3 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 0;
loc_0033FF8D:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (6));
    if (((unsigned __int8)(result)) == 6) goto loc_0034080E;
loc_0033FF9B:
    goto loc_00340ADA;
loc_0033FFA7:
    result = (unsigned __int8)((-1) & (1));
    *(unsigned __int8 *)(0 + 1452) = (unsigned __int8)(result);
    v_r15 = (unsigned int)((-1) >> (1));
    *(unsigned int *)(0 + 1432) = (unsigned int)(v_r15);
    if (sign_flag) {
        a1 = 0;
        result = RtlRaiseStatus(a1, 0, a3, v_stack_mF0);
    }
    result = ExAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, 0, a3, v_stack_mF0);
    if ((*(unsigned __int64 *)(v_stack_mE8 + 184)) == 0) {
        result = *(unsigned __int64 *)(a8);
        *(unsigned __int64 *)(v_stack_mE8 + 184) = result;
        result = v_stack_mD8;
        *(unsigned __int64 *)(v_stack_mE8 + 56) = result;
        result = 0;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, 0, a3, v_stack_mF0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (*(unsigned int *)(v_stack_mE8 + 8)));
    result = (result) + (*(unsigned __int64 *)(v_stack_mE8 + 184));
    *(unsigned __int64 *)(a8) = result;
loc_00340026:
    a3 = 0;
loc_00340029:
    v_stack_mF8 = 1;
    goto loc_0033FF8D;
loc_00340033:
    if ((*(unsigned __int16 *)(v_stack_mE8)) != ((unsigned __int16)(v_r15))) goto loc_0033FDC8;
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(v_stack_mE8 + 32))) goto loc_0033FDC8;
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(v_stack_mE8 + 8))) goto loc_0033FDC0;
    if (v_rbx >= (*(unsigned __int64 *)(v_stack_mE8 + 8))) goto loc_003408C5;
loc_00340060:
    v_rdi = (*(unsigned __int64 *)(v_stack_mE8 + 16)) - (16);
    v_stack_m88 = v_rdi;
    goto loc_00340033;
loc_00340072:
    v_stack_mC0 = *(unsigned __int64 *)(a2);
    v_rbx = (v_rbx) - (*(unsigned __int64 *)(a2));
    v_stack_mC8 = v_rbx;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2)))) & (0xFFFULL));
    v_stack_mC8 = (unsigned int)(v_rbx + a2 * 1);
    a3 = (unsigned int)(((unsigned int)(v_stack_mD0)) + ((unsigned int)(a2)));
    v_stack_mD0 = a3;
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_003400BC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)))) & (4)) == 0) goto loc_00340409;
loc_003400BC:
    if (a5 != 0) goto loc_00340409;
loc_003400D1:
    result = (unsigned int)((unsigned int)(v_stack_p20));
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)) & (512)) == 0) { result = 0; }
    v_stack_p20 = (unsigned __int8)(result);
    v_r12 = (unsigned int)((v_rbx + a2 * 1) + (0xFFFULL));
    v_r12 = (unsigned int)((v_r12) & (0xFFFFF000ULL));
    v_stack_mC8 = (unsigned int)(v_r12);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2)))) & (0xFFFULL));
    if (((unsigned int)(v_r12)) > a3) { v_r12 = a3; }
    v_stack_mC8 = (unsigned int)(v_r12);
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) == 0) goto loc_0034023B;
    result = ExAllocatePoolWithTag((unsigned int)(0x600ULL), 192, (unsigned int)(0x63426343ULL), a4);
    if (result == 0) goto loc_00340275;
    *(unsigned __int16 *)(result) = (unsigned __int16)(v_r15);
    *(unsigned __int64 *)(result + 8) = v_stack_mC0;
    *(unsigned int *)(result + 4) = (unsigned int)(v_r12);
    a3 = (v_stack_mC8) + (v_stack_mC0);
    *(unsigned __int64 *)(result + 32) = a3;
    *(unsigned __int64 *)(result + 176) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 64))) + 1);
    *(unsigned int *)(result + 64) = (unsigned int)(result);
    result = ExInitializeResourceLite2(result + 72, (unsigned int)(0xFFFFFFFFULL), a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rdi = (v_rdi) + (16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) == v_rdi) goto loc_00340280;
loc_003401D7:
    if ((unsigned int)(*(unsigned __int64 *)(v_rdi + 8)) == 0) goto loc_00340449;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 64))) + 1);
    *(unsigned int *)(v_rdi + 64) = (unsigned int)(result);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, *(unsigned __int64 *)(v_rdi + 8), a3, a4);
    a3 = 0;
    v_stack_mF4 = 0;
    if (v_stack_p20 != 0) goto loc_0034021D;
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_0034072F;
    result = ExAcquireSharedStarveExclusive(v_rdi + 72, 1, a3, a4);
    a3 = 0;
loc_0034021D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (*(unsigned int *)(v_rdi + 8)));
    result = (result) + (*(unsigned __int64 *)(v_rdi + 184));
    *(unsigned __int64 *)(a8) = result;
    goto loc_00340029;
loc_0034023B:
    result = CcAllocateInitializeBcb(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), v_rdi, v_stack_mC0, v_stack_mC8);
    v_stack_mE8 = result;
    if (result != 0) goto loc_00340487;
    v_stack_mF8 = (unsigned __int8)(result);
    a3 = 0;
    goto loc_0033FF8D;
loc_00340275:
    v_r11 = 0;
    goto loc_0034030A;
loc_00340280:
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = result;
    *(unsigned __int64 *)(result + 8) = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32)) <= 0x2000000ULL) goto loc_003402B7;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)) & (512)) != 0) {
        a3 = 1;
        a2 = v_stack_mC0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8);
        result = CcAdjustVacbLevelLockCount(a1, a2, a3, v_stack_mC8);
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104))) & (2)) != 0) goto loc_003403D3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104))) & (2)) != 0) goto loc_003403D3;
loc_003402EB:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104, a2, a3, v_stack_mC8);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)))) & (2)) != 0) {
        a1 = 0 + 72;
        result = ExDisableResourceBoostLite(a1, a2, a3, v_stack_mC8);
    }
    v_r11 = 0;
loc_0034030A:
    v_stack_m80 = 0;
    v_stack_mE8 = 0;
    if (0 != 0) goto loc_003404C2;
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, v_stack_mC8);
    result = 0;
    v_stack_mF4 = 0;
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), a2, a3, v_stack_mC8);
loc_0034033F:
    if (v_stack_p20 == 0) goto loc_003403E1;
loc_0034034D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 64))) + 1);
    *(unsigned int *)(0 + 64) = (unsigned int)(result);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, v_stack_mC8);
    v_rbx = 0;
    v_stack_mF4 = 0;
    a3 = 0;
    a2 = 0;
    result = CcMapAndRead((unsigned int)(*(unsigned int *)(0 + 4)), a2, a3, *(unsigned __int64 *)(a8));
    if ((unsigned __int8)(result) == 0) goto loc_003407DE;
    result = ExAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, *(unsigned __int64 *)(a8));
    if ((*(unsigned __int64 *)(0 + 184)) == 0) {
        result = *(unsigned __int64 *)(a8);
        *(unsigned __int64 *)(0 + 184) = result;
        result = v_stack_mD8;
        *(unsigned __int64 *)(0 + 56) = result;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, *(unsigned __int64 *)(a8));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (*(unsigned int *)(0 + 8)));
    result = (result) + (*(unsigned __int64 *)(0 + 184));
    a3 = 0;
    *(unsigned __int64 *)(a8) = result;
    goto loc_00340029;
loc_003403D3:
    result = ExfReleasePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 104, a2, a3, *(unsigned __int64 *)(a8));
    goto loc_003402EB;
loc_003403E1:
    a2 = 0;
    result = ExAcquireSharedStarveExclusive(0 + 72, a2, a3, *(unsigned __int64 *)(a8));
    if ((unsigned __int8)(result) != 0) goto loc_0034034D;
    a3 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 0;
    goto loc_0033FF8D;
loc_00340409:
    v_stack_mE0 = 2;
    v_rbx = 2;
    if (0 == 0) {
        result = 3;
        v_rbx = 2;
        if (v_stack_p18 >= 0x1000ULL) { v_rbx = (unsigned int)(result); }
        v_stack_mE0 = (unsigned int)(v_rbx);
    }
    if ((((unsigned int)(a8)) & (0xFFFULL)) != 0) goto loc_003400D1;
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_stack_mE0 = (unsigned int)(v_rbx);
    goto loc_003400D1;
loc_00340449:
    if (v_stack_p20 != 0) goto loc_00340466;
    a2 = 0;
    result = ExAcquireSharedStarveExclusive(0 + 72, a2, a3, (unsigned int)((unsigned int)(0 + 72)));
    if ((unsigned __int8)(result) == 0) goto loc_0033FF75;
loc_00340466:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 64))) + 1);
    *(unsigned int *)(0 + 64) = (unsigned int)(result);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, (unsigned int)((unsigned int)(0 + 72)));
    a3 = 0;
    v_stack_mF4 = 0;
    goto loc_0034021D;
loc_00340487:
    if (v_stack_p20 != 0) goto loc_0034073C;
    a2 = 0;
    result = ExAcquireSharedStarveExclusive(result + 72, a2, a3, (unsigned int)((unsigned int)(0 + 72)));
    if ((unsigned __int8)(result) != 0) goto loc_0034073C;
    result = 0;
    v_stack_m108 = 0;
    a4 = 0;
    result = KeBugCheckEx(result + 52, (unsigned int)(0x2027AULL), 0, a4);
loc_003404C2:
    if (v_stack_p20 != 0) goto loc_00340524;
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_00340703;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 72 + 26))) & (65));
    if (((unsigned __int8)(result)) == 1) goto loc_0034088D;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 72 + 26))) & (1)) != 0) goto loc_00340A35;
loc_003404F5:
    a2 = 0;
    result = ExpAcquireSharedStarveExclusive(v_rbx + 72, a2, v_rbx + 72, a4);
loc_003404FF:
    v_stack_p18 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) {
        result = 0;
        v_stack_m108 = 0;
        a4 = 0;
        a3 = v_rbx;
        a2 = 0x2021AULL;
        a1 = result + 52;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, a2, a3, a4);
    a3 = 0;
    v_stack_mF4 = 0;
    if ((((unsigned __int8)((unsigned int)(a6))) & (4)) != 0) goto loc_003406F1;
    v_stack_m78 = *(unsigned __int64 *)(a8);
    v_stack_mB0 = 0;
    v_stack_m48 = 0;
    v_stack_mAC = 0;
    v_stack_m98 = 0;
    v_stack_p8 = 1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a8)))) & (0xFFFULL));
    v_rbx = ((unsigned int)(v_stack_mC8)) + (0xFFFULL);
    v_rbx = (v_rbx) + (a1);
    v_rbx = (v_rbx) >> (12);
    v_stack_mAC = (unsigned int)(v_rbx);
    v_rdi = (*(unsigned __int64 *)(a8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m78 = v_rdi;
loc_003405CC:
    if ((unsigned int)(v_rbx) == 0) goto loc_00340668;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) = 1;
    if (((unsigned int)(v_rbx - 1)) > (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432))) goto loc_00340878;
loc_003405EC:
    v_stack_mB0 = 0;
    if ((((unsigned int)((unsigned int)(v_stack_mE0))) & (1)) != 0) { a3 = 1; }
    v_stack_mB0 = a3;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) != 0) goto loc_003408A4;
loc_0034060C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) << (12));
    v_stack_mB8 = result;
    result = MmCheckCachedPageStates(v_rdi, (unsigned int)((unsigned int)(result)), a3, v_stack_p8);
    v_stack_m98 = (unsigned int)(result);
    if (sign_flag) goto loc_00340668;
    v_rdi = (v_rdi) + (v_stack_mB8);
    v_stack_m78 = v_rdi;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    v_stack_mAC = (unsigned int)(v_rbx);
    a4 = 2;
    if (((unsigned int)(v_rbx)) == 1) { a4 = 4; }
    a3 = 0;
    goto loc_003405CC;
loc_00340668:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2)) & (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) = (unsigned __int8)(result);
    v_r12 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2) >> (1));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432) = (unsigned int)(v_r12);
    if (sign_flag) {
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    }
    result = ExAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, (unsigned int)((unsigned int)(result)), a3, a4);
    if ((*(unsigned __int64 *)(v_stack_mE8 + 184)) == 0) {
        result = *(unsigned __int64 *)(a8);
        *(unsigned __int64 *)(v_stack_mE8 + 184) = result;
        result = v_stack_mD8;
        *(unsigned __int64 *)(v_stack_mE8 + 56) = result;
        result = 0;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, (unsigned int)((unsigned int)(result)), a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) - (*(unsigned int *)(v_stack_mE8 + 8)));
    result = (result) + (*(unsigned __int64 *)(v_stack_mE8 + 184));
    *(unsigned __int64 *)(a8) = result;
    a3 = 0;
loc_003406F1:
    v_stack_mF8 = 1;
    goto loc_0033FF8D;
loc_00340703:
    a2 = 0;
    result = ExAcquireResourceExclusiveLite(0, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00340524;
    result = 0;
    v_stack_m108 = 0;
    a4 = 0;
    result = KeBugCheckEx(result + 52, (unsigned int)(0x20213ULL), v_rbx, a4);
loc_0034072F:
    result = ExAcquireResourceExclusiveLite(result + 52, (unsigned int)(0x20213ULL), v_rbx, a4);
    a3 = 0;
    goto loc_0034021D;
loc_0034073C:
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, (unsigned int)(0x20213ULL), a3, a4);
    v_r15 = 0;
    v_stack_mF4 = 0;
    a3 = 0;
    result = CcMapAndRead((unsigned int)((unsigned int)(a8)), (unsigned int)((unsigned int)(v_rbx)), a3, *(unsigned __int64 *)(a8));
    if ((unsigned __int8)(result) == 0) goto loc_003407F9;
    result = ExAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288, (unsigned int)((unsigned int)(v_rbx)), a3, *(unsigned __int64 *)(a8));
    if ((*(unsigned __int64 *)(v_stack_mE8 + 184)) != 0) goto loc_003403AE;
    *(unsigned __int64 *)(v_stack_mE8 + 184) = *(unsigned __int64 *)(a8);
    *(unsigned __int64 *)(v_stack_mE8 + 56) = v_stack_mD8;
    v_stack_mD8 = 0;
    goto loc_003403AE;
loc_003407AF:
    if (((unsigned int)(v_stack_mD8)) <= 15) goto loc_003408BA;
    *(unsigned int *)(v_stack_mE8 + 1432) = 15;
    goto loc_0033FF28;
loc_003407C7:
    v_stack_m108 = 0;
    a4 = 0;
    result = KeBugCheckEx(454, a4 + 15, a3, a4);
loc_003407DE:
    v_stack_mF8 = (unsigned __int8)(v_rbx);
    a3 = 0;
    goto loc_0033FF8D;
loc_003407EA:
    result = ExAcquireResourceExclusiveLite(0, 1, a3, a4);
    goto loc_0033FE85;
loc_003407F9:
    v_stack_mF8 = 0;
    a3 = 0;
    goto loc_0033FF8D;
loc_0034080E:
    if (v_stack_mE8 == 0) goto loc_0033FF9B;
    if ((*(unsigned __int64 *)(v_stack_mE8 + 184)) == 0) goto loc_00340ADA;
    a1 = (unsigned int)((-1) - 1);
    if ((unsigned __int16)(a1) != 0) goto loc_00340863;
    result = *(unsigned __int64 *)(v_stack_mE8 + 56);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) + 192) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) + 192), a2, a3, a4);
    }
    a3 = 0;
loc_00340863:
    *(unsigned __int64 *)(v_stack_mE8 + 184) = 0;
    *(unsigned __int64 *)(v_stack_mE8 + 56) = 0;
    goto loc_00340ADA;
loc_00340878:
    if (((unsigned int)(result)) <= 15) goto loc_003408D5;
    *(unsigned int *)(-1 + 1432) = 15;
    goto loc_003405EC;
loc_0034088D:
    v_stack_m108 = 0;
    a4 = 0;
    result = KeBugCheckEx(454, a4 + 15, a3, a4);
loc_003408A4:
    if (0 == 2) goto loc_0034060C;
    goto loc_0034060C;
loc_003408BA:
    *(unsigned int *)(v_stack_mE8 + 1432) = (unsigned int)(result);
    goto loc_0033FF28;
loc_003408C5:
    v_stack_mA0 = 454;
    goto loc_00340060;
loc_003408D5:
    *(unsigned int *)(-1 + 1432) = (unsigned int)(result);
    goto loc_003405EC;
loc_003408E1:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152)) & (512)) == 0) goto loc_0033FD44;
    if (454 <= 0x2000000ULL) goto loc_00340916;
    result = CcGetBcbListHeadLargeOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), v_stack_mE8, 1, a4);
    goto loc_0033FD48;
loc_00340916:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8)))) >> (18));
    result = (unsigned int)((result) + 1);
    result = (unsigned int)((result) & (0xFFFFFFFEULL));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_mE8)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) << (19));
    result = (unsigned int)((result) - (0x80000ULL));
    if (1 >= result) goto loc_0033FD44;
    if (0 != 0) goto loc_00340AC6;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8))) <= 0x100000ULL) goto loc_00340AD0;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8)))) >> (18);
    a1 = (a1) << (3);
loc_00340957:
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 88));
    v_rdi = (result) >> (19);
    v_rdi = (v_rdi) << (4);
    v_rdi = (v_rdi) + (a1);
    goto loc_0033FD48;
loc_0034096B:
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_0033FE7B;
    result = ExpFastResourceLegacyAcquireSharedStarveExclusive(1, 1, 1, a4);
    goto loc_0033FE85;
loc_00340988:
    if (1 >= = 1) {
        a3 = 1;
        v_stack_m108 = 1;
        a2 = 0;
        a1 = 454;
        a4 = a2 + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 192);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 192))) & (2)) != 0) {
        v_stack_m108 = 1;
        a4 = 0;
        a3 = 0;
        a2 = a4 + 6;
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(a2)) >= 1) goto loc_0034096B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_0034096B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) != 1) goto loc_0034096B;
loc_003409F6:
    v_stack_m108 = 1;
    a4 = 0;
    a3 = 0;
    result = KeBugCheckEx(454, a4 + 7, a3, a4);
loc_00340A10:
    if (((454) & (1)) == 0) goto loc_003404F5;
    a2 = 0;
    result = ExpFastResourceLegacyAcquireSharedStarveExclusive(0, a2, a3, a4);
    goto loc_003404FF;
loc_00340A35:
    if (1 >= = 2) {
        a3 = 1;
        v_stack_m108 = 1;
        a2 = 0;
        a1 = 454;
        a4 = a2 + 2;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (condition_is_below) goto loc_00340A8C;
    result = (unsigned int)(*(unsigned int *)(gs_base + (0 + 14908)));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) {
        v_stack_m108 = 1;
        a4 = 0;
        a3 = 0;
        a2 = a4 + 5;
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 192))) & (2)) != 0) goto loc_003409C0;
    if (((unsigned __int8)(a2)) >= 1) goto loc_00340A10;
    if (((*(unsigned int *)(a4 + 116)) & (0x400ULL)) != 0) goto loc_00340A10;
    if ((*(unsigned int *)(a4 + 484)) == 0) goto loc_003409F6;
    goto loc_00340A10;
loc_00340AC6:
    goto loc_00340957;
loc_00340AD0:
    goto loc_00340957;
loc_00340ADA:
    result = *(unsigned __int8 *)(a4 + 192);
    if (v_stack_mF4 != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 288;
        result = ExReleaseFastMutex(a1, a2, a3, a4);
    }
    if (v_stack_mD8 == 0) goto loc_00340B2C;
    v_r15 = (unsigned int)((-1) - 1);
    if ((unsigned __int16)(v_r15) != 0) goto loc_00340B27;
    result = v_stack_mD8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 8) + 192) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 8) + 192), a2, a3, a4);
    }
loc_00340B27:
loc_00340B2C:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(4 - 3)))) & (4)) == 0) goto loc_00340B43;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32)) > 0x2000000ULL) goto loc_00340C63;
loc_00340B43:
    if (v_stack_mF8 == 0) goto loc_00340B7D;
    *(unsigned __int64 *)(a7) = v_stack_mE8;
    *(unsigned __int64 *)(a9) = *(unsigned __int64 *)(v_stack_mE8 + 32);
loc_00340B64:
    v_rsp = (v_rsp) + (240);
    return v_stack_mF8;
loc_00340B7D:
    result = 0;
    *(unsigned __int64 *)(a8) = 0;
    if (v_stack_mE8 == 0) goto loc_00340B64;
    a3 = 0;
    result = CcUnpinFileDataEx(v_stack_mE8, v_stack_p148, a3, a4);
    goto loc_00340B64;
loc_00340B9D:
    result = KiRaiseIrqlProcessIrqlFlags(0, 1, a3, a4);
    goto loc_0033FC34;
loc_00340BBD:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(1))) & (0x3FFFFULL));
    result = (unsigned int)(((unsigned int)(0x40000ULL)) - ((unsigned int)(a1)));
    v_stack_p58 = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 32)) <= 0x2000000ULL) goto loc_0033FBFA;
    v_stack_pD8 = a8;
    v_stack_pC8 = v_stack_pC0;
    v_stack_pC0 = v_stack_pC0;
    v_stack_pD0 = a8;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8) + 152))) >> (9));
    a2 = (unsigned __int8)((a2) & (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11312241))) - 1);
    result = CcAllocateVacbLevels(a1, a2, v_stack_pC0, a4);
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), a2, v_stack_pC0, a4);
loc_00340C45:
    v_stack_p20 = a8;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, 325, 0xFFFFFFFFC0000420ULL, a4);
loc_00340C63:
    result = CcAcquireBcbLockAndVacbLock(1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), 0xFFFFFFFFC0000420ULL, a4);
    a4 = 0;
    result = SetVacb(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), *(unsigned __int64 *)(1), 1 - 3, a4);
    result = CcReleaseBcbLockAndVacbLock(1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8), 1 - 3, a4);
    goto loc_00340B43;
}
```

## 5. (Beta) C Style

```c
int64_t CcPinFileData(void *Arg1, void *Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, uint32_t Arg6, void *Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint8_t v_stack_mF7;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p130;
    uint8_t v_stack_p148;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint32_t v_stack_p58;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (240);
    local_r12 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mF8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8);
    v_stack_mB8 = (uint32_t)(Arg3);
    Arg1 = (*(uint64_t *)(arg2)) + ((uint32_t)(Arg3));
    if (Arg1 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20))) goto loc_00340C45;
    *(uint64_t *)(arg7) = 0;
    *(uint64_t *)(arg8) = 0;
    if ((((uint8_t)((uint32_t)(Arg6))) & (4)) != 0) goto loc_00340BBD;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) >> (6));
    result = (uint32_t)((result) & (1));
    v_stack_m100 = 0;
    v_stack_m108 = (uint32_t)(result);
    result = CcGetVirtualAddress(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), *(uint64_t *)(arg2), v_stack_mD8, v_stack_mD0);
    *(uint64_t *)(arg8) = result;
loc_0033FBFA:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, v_stack_mD0);
    v_stack_p8 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC870F2)) != 0) goto loc_00340B9D;
loc_0033FC34:
    if ((*(uint32_t *)(v_rip + 0xC870F2)) < 0) goto loc_0033FCD2;
loc_0033FC4E:
loc_0033FC50:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x120)))) & (1)) != 0) goto loc_0033FCA9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x120)))) & (1)) != 0) goto loc_0033FC50;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x120));
    if (result != 0) {
        Arg1 = result;
        result = KeAbPreWait(Arg1, Arg2, v_cr8, v_stack_mD0);
    }
    result = 0;
    v_stack_m108 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288 + 24, result + 34, Arg3, Arg4);
    if (result == 0) goto loc_0033FC4E;
    Arg3 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, result, Arg3, Arg4);
    goto loc_0033FC4E;
loc_0033FCA9:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) ^ (3));
    if (condition_is_not_equal) goto loc_0033FC50;
    local_r12 = 0;
loc_0033FCD2:
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x120 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x120 + 0x30) = (uint32_t)((uint8_t)(v_stack_p8));
    v_stack_mF4 = 1;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    local_r15 = (*(uint64_t *)(arg2)) >> (32);
    v_stack_mA0 = *(uint64_t *)(arg2) + v_stack_mB8 * 1;
    v_stack_m88 = 0;
    local_r12 = 0;
    v_stack_mF7 = 0;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20)) >> (32);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20)) > 0x200000ULL) goto loc_003408E1;
loc_0033FD44:
loc_0033FD48:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x10)) - (16);
    v_stack_m88 = local_rdi;
    if ((uint32_t)(local_r15) != 0) goto loc_00340033;
    if ((*(uint16_t *)(local_rdi)) != 765) goto loc_0033FDC8;
    if ((*(uint32_t *)(local_rdi + 0x24)) != 0) goto loc_00340033;
loc_0033FD81:
    if (765 != 765) goto loc_0033FDC8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) >= (*(uint32_t *)(local_rdi + 0x20))) goto loc_0033FDC8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) goto loc_0033FDC0;
    local_rbx = *(uint64_t *)(arg2) + v_stack_mB8 * 1;
    if (((uint32_t)((uint32_t)(v_stack_mA0))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) {
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)));
        v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)));
        local_rbx = v_stack_mA0;
    }
    local_rdi = (*(uint64_t *)(local_rdi + 0x10)) - (16);
    v_stack_m88 = local_rdi;
    goto loc_0033FD81;
loc_0033FDC0:
    v_stack_mF7 = 1;
loc_0033FDC8:
    v_stack_mE8 = local_rdi;
    if (1 == 0) goto loc_0033FF6B;
    local_rbx = v_stack_p20;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)) & (512)) == 0) { local_rbx = 1; }
    v_stack_p20 = (uint8_t)(local_rbx);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (1));
    if ((*(uint64_t *)(local_rdi + 0xB8)) != 0) goto loc_003401D7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) - (*(uint32_t *)(local_rdi + 0x8)));
    v_stack_mC0 = *(uint64_t *)(local_rdi + 0x8);
    v_stack_mC8 = (uint32_t)(*(uint32_t *)(local_rdi + 0x4));
    if ((uint32_t)(Arg2) == 0) goto loc_0034033F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x40))) + 1);
    *(uint32_t *)(local_rdi + 0x40) = (uint32_t)(result);
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, *(uint64_t *)(arg2), Arg4);
    local_r11 = 0;
    v_stack_mF4 = 0;
    if ((uint8_t)(local_rbx) != 0) goto loc_0033FE88;
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_003407EA;
    result = (uint8_t)(((uint8_t)(*(uint16_t *)(local_rdi + 0x48 + 0x1A))) & (65));
    if (((uint8_t)(result)) == 1) goto loc_003407C7;
    if ((((uint8_t)(*(uint16_t *)(local_rdi + 0x48 + 0x1A))) & (1)) != 0) goto loc_00340988;
loc_0033FE7B:
    result = ExpAcquireSharedStarveExclusive(local_rdi + 72, 1, local_rdi + 72, Arg4);
loc_0033FE85:
    local_r11 = 0;
loc_0033FE88:
    if ((((uint8_t)((uint32_t)(Arg6))) & (4)) != 0) goto loc_00340026;
    v_stack_mB8 = *(uint64_t *)(arg8);
    v_stack_m94 = 0;
    v_stack_m44 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
    v_stack_mF0 = 1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg8)))) & (0xFFFULL));
    Arg2 = ((uint32_t)(v_stack_mC8)) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    v_stack_mA8 = (uint32_t)(Arg2);
    local_rbx = (*(uint64_t *)(arg8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mB8 = local_rbx;
loc_0033FF0A:
    if ((uint32_t)(Arg2) == 0) goto loc_0033FFA7;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) = 1;
    if (((uint32_t)(Arg2 - 1)) > (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598))) goto loc_003407AF;
loc_0033FF28:
    v_stack_m94 = 0;
    Arg2 = (uint32_t)((Arg2) << (12));
    Arg3 = 0;
    result = MmCheckCachedPageStates(local_rbx, Arg2, Arg3, v_stack_mF0);
    v_stack_m90 = (uint32_t)(result);
    if (sign_flag) goto loc_0033FFA7;
    local_rbx = (local_rbx) + ((uint32_t)((uint32_t)(Arg2)));
    v_stack_mB8 = local_rbx;
    local_r11 = 0;
    v_stack_mA8 = 0;
    goto loc_0033FF0A;
loc_0033FF6B:
    if ((((uint8_t)((uint32_t)(Arg6))) & (8)) == 0) goto loc_00340072;
loc_0033FF75:
    Arg3 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 0;
loc_0033FF8D:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (6));
    if (((uint8_t)(result)) == 6) goto loc_0034080E;
loc_0033FF9B:
    goto loc_00340ADA;
loc_0033FFA7:
    result = (uint8_t)((-1) & (1));
    *(uint8_t *)(0 + 0x5AC) = (uint8_t)(result);
    local_r15 = (uint32_t)((-1) >> (1));
    *(uint32_t *)(0 + 0x598) = (uint32_t)(local_r15);
    if (sign_flag) {
        Arg1 = 0;
        result = RtlRaiseStatus(Arg1, 0, Arg3, v_stack_mF0);
    }
    result = ExAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, 0, Arg3, v_stack_mF0);
    if ((*(uint64_t *)(v_stack_mE8 + 0xB8)) == 0) {
        result = *(uint64_t *)(arg8);
        *(uint64_t *)(v_stack_mE8 + 0xB8) = result;
        result = v_stack_mD8;
        *(uint64_t *)(v_stack_mE8 + 0x38) = result;
        result = 0;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, 0, Arg3, v_stack_mF0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) - (*(uint32_t *)(v_stack_mE8 + 0x8)));
    result = (result) + (*(uint64_t *)(v_stack_mE8 + 0xB8));
    *(uint64_t *)(arg8) = result;
loc_00340026:
    Arg3 = 0;
loc_00340029:
    v_stack_mF8 = 1;
    goto loc_0033FF8D;
loc_00340033:
    if ((*(uint16_t *)(v_stack_mE8)) != ((uint16_t)(local_r15))) goto loc_0033FDC8;
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(v_stack_mE8 + 0x20))) goto loc_0033FDC8;
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(v_stack_mE8 + 0x8))) goto loc_0033FDC0;
    if (local_rbx >= (*(uint64_t *)(v_stack_mE8 + 0x8))) goto loc_003408C5;
loc_00340060:
    local_rdi = (*(uint64_t *)(v_stack_mE8 + 0x10)) - (16);
    v_stack_m88 = local_rdi;
    goto loc_00340033;
loc_00340072:
    v_stack_mC0 = *(uint64_t *)(arg2);
    local_rbx = (local_rbx) - (*(uint64_t *)(arg2));
    v_stack_mC8 = local_rbx;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg2)))) & (0xFFFULL));
    v_stack_mC8 = (uint32_t)(local_rbx + Arg2 * 1);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mD0)) + ((uint32_t)(Arg2)));
    v_stack_mD0 = Arg3;
    if ((uint8_t)(v_stack_p20) != 0) goto loc_003400BC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)))) & (4)) == 0) goto loc_00340409;
loc_003400BC:
    if (Arg5 != 0) goto loc_00340409;
loc_003400D1:
    result = (uint32_t)((uint32_t)(v_stack_p20));
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)) & (512)) == 0) { result = 0; }
    v_stack_p20 = (uint8_t)(result);
    local_r12 = (uint32_t)((local_rbx + Arg2 * 1) + (0xFFFULL));
    local_r12 = (uint32_t)((local_r12) & (0xFFFFF000ULL));
    v_stack_mC8 = (uint32_t)(local_r12);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg2)))) & (0xFFFULL));
    if (((uint32_t)(local_r12)) > Arg3) { local_r12 = Arg3; }
    v_stack_mC8 = (uint32_t)(local_r12);
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) == 0) goto loc_0034023B;
    result = ExAllocatePoolWithTag((uint32_t)(0x600ULL), 192, (uint32_t)(0x63426343ULL), Arg4);
    if (result == 0) goto loc_00340275;
    *(uint16_t *)(result) = (uint16_t)(local_r15);
    *(uint64_t *)(result + 0x8) = v_stack_mC0;
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r12);
    Arg3 = (v_stack_mC8) + (v_stack_mC0);
    *(uint64_t *)(result + 0x20) = Arg3;
    *(uint64_t *)(result + 0xB0) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x40))) + 1);
    *(uint32_t *)(result + 0x40) = (uint32_t)(result);
    result = ExInitializeResourceLite2(result + 72, (uint32_t)(0xFFFFFFFFULL), Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 104, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 104;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rdi = (local_rdi) + (16);
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) == local_rdi) goto loc_00340280;
loc_003401D7:
    if ((uint32_t)(*(uint64_t *)(local_rdi + 0x8)) == 0) goto loc_00340449;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x40))) + 1);
    *(uint32_t *)(local_rdi + 0x40) = (uint32_t)(result);
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, *(uint64_t *)(local_rdi + 0x8), Arg3, Arg4);
    Arg3 = 0;
    v_stack_mF4 = 0;
    if (v_stack_p20 != 0) goto loc_0034021D;
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_0034072F;
    result = ExAcquireSharedStarveExclusive(local_rdi + 72, 1, Arg3, Arg4);
    Arg3 = 0;
loc_0034021D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) - (*(uint32_t *)(local_rdi + 0x8)));
    result = (result) + (*(uint64_t *)(local_rdi + 0xB8));
    *(uint64_t *)(arg8) = result;
    goto loc_00340029;
loc_0034023B:
    result = CcAllocateInitializeBcb(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), local_rdi, v_stack_mC0, v_stack_mC8);
    v_stack_mE8 = result;
    if (result != 0) goto loc_00340487;
    v_stack_mF8 = (uint8_t)(result);
    Arg3 = 0;
    goto loc_0033FF8D;
loc_00340275:
    local_r11 = 0;
    goto loc_0034030A;
loc_00340280:
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = result;
    *(uint64_t *)(result + 0x8) = result;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20)) <= 0x2000000ULL) goto loc_003402B7;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)) & (512)) != 0) {
        Arg3 = 1;
        Arg2 = v_stack_mC0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8);
        result = CcAdjustVacbLevelLockCount(Arg1, Arg2, Arg3, v_stack_mC8);
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x68)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x68) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x68))) & (2)) != 0) goto loc_003403D3;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x68))) & (2)) != 0) goto loc_003403D3;
loc_003402EB:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 104, Arg2, Arg3, v_stack_mC8);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)))) & (2)) != 0) {
        Arg1 = 0 + 72;
        result = ExDisableResourceBoostLite(Arg1, Arg2, Arg3, v_stack_mC8);
    }
    local_r11 = 0;
loc_0034030A:
    v_stack_m80 = 0;
    v_stack_mE8 = 0;
    if (0 != 0) goto loc_003404C2;
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, v_stack_mC8);
    result = 0;
    v_stack_mF4 = 0;
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), Arg2, Arg3, v_stack_mC8);
loc_0034033F:
    if (v_stack_p20 == 0) goto loc_003403E1;
loc_0034034D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x40))) + 1);
    *(uint32_t *)(0 + 0x40) = (uint32_t)(result);
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, v_stack_mC8);
    local_rbx = 0;
    v_stack_mF4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = CcMapAndRead((uint32_t)(*(uint32_t *)(0 + 0x4)), Arg2, Arg3, *(uint64_t *)(arg8));
    if ((uint8_t)(result) == 0) goto loc_003407DE;
    result = ExAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, *(uint64_t *)(arg8));
    if ((*(uint64_t *)(0 + 0xB8)) == 0) {
        result = *(uint64_t *)(arg8);
        *(uint64_t *)(0 + 0xB8) = result;
        result = v_stack_mD8;
        *(uint64_t *)(0 + 0x38) = result;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, *(uint64_t *)(arg8));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) - (*(uint32_t *)(0 + 0x8)));
    result = (result) + (*(uint64_t *)(0 + 0xB8));
    Arg3 = 0;
    *(uint64_t *)(arg8) = result;
    goto loc_00340029;
loc_003403D3:
    result = ExfReleasePushLock(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 104, Arg2, Arg3, *(uint64_t *)(arg8));
    goto loc_003402EB;
loc_003403E1:
    Arg2 = 0;
    result = ExAcquireSharedStarveExclusive(0 + 72, Arg2, Arg3, *(uint64_t *)(arg8));
    if ((uint8_t)(result) != 0) goto loc_0034034D;
    Arg3 = 0;
    v_stack_mE8 = 0;
    v_stack_mF8 = 0;
    goto loc_0033FF8D;
loc_00340409:
    v_stack_mE0 = 2;
    local_rbx = 2;
    if (0 == 0) {
        result = 3;
        local_rbx = 2;
        if (v_stack_p18 >= 0x1000ULL) { local_rbx = (uint32_t)(result); }
        v_stack_mE0 = (uint32_t)(local_rbx);
    }
    if ((((uint32_t)(Arg8)) & (0xFFFULL)) != 0) goto loc_003400D1;
    local_rbx = (uint32_t)((local_rbx) | (4));
    v_stack_mE0 = (uint32_t)(local_rbx);
    goto loc_003400D1;
loc_00340449:
    if (v_stack_p20 != 0) goto loc_00340466;
    Arg2 = 0;
    result = ExAcquireSharedStarveExclusive(0 + 72, Arg2, Arg3, (uint32_t)((uint32_t)(0 + 72)));
    if ((uint8_t)(result) == 0) goto loc_0033FF75;
loc_00340466:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x40))) + 1);
    *(uint32_t *)(0 + 0x40) = (uint32_t)(result);
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, (uint32_t)((uint32_t)(0 + 72)));
    Arg3 = 0;
    v_stack_mF4 = 0;
    goto loc_0034021D;
loc_00340487:
    if (v_stack_p20 != 0) goto loc_0034073C;
    Arg2 = 0;
    result = ExAcquireSharedStarveExclusive(result + 72, Arg2, Arg3, (uint32_t)((uint32_t)(0 + 72)));
    if ((uint8_t)(result) != 0) goto loc_0034073C;
    result = 0;
    v_stack_m108 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(result + 52, (uint32_t)(0x2027AULL), 0, Arg4);
loc_003404C2:
    if (v_stack_p20 != 0) goto loc_00340524;
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_00340703;
    result = (uint8_t)(((uint8_t)(*(uint16_t *)(local_rbx + 0x48 + 0x1A))) & (65));
    if (((uint8_t)(result)) == 1) goto loc_0034088D;
    if ((((uint8_t)(*(uint16_t *)(local_rbx + 0x48 + 0x1A))) & (1)) != 0) goto loc_00340A35;
loc_003404F5:
    Arg2 = 0;
    result = ExpAcquireSharedStarveExclusive(local_rbx + 72, Arg2, local_rbx + 72, Arg4);
loc_003404FF:
    v_stack_p18 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) {
        result = 0;
        v_stack_m108 = 0;
        Arg4 = 0;
        Arg3 = local_rbx;
        Arg2 = 0x2021AULL;
        Arg1 = result + 52;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, Arg2, Arg3, Arg4);
    Arg3 = 0;
    v_stack_mF4 = 0;
    if ((((uint8_t)((uint32_t)(Arg6))) & (4)) != 0) goto loc_003406F1;
    v_stack_m78 = *(uint64_t *)(arg8);
    v_stack_mB0 = 0;
    v_stack_m48 = 0;
    v_stack_mAC = 0;
    v_stack_m98 = 0;
    v_stack_p8 = 1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg8)))) & (0xFFFULL));
    local_rbx = ((uint32_t)(v_stack_mC8)) + (0xFFFULL);
    local_rbx = (local_rbx) + (Arg1);
    local_rbx = (local_rbx) >> (12);
    v_stack_mAC = (uint32_t)(local_rbx);
    local_rdi = (*(uint64_t *)(arg8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m78 = local_rdi;
loc_003405CC:
    if ((uint32_t)(local_rbx) == 0) goto loc_00340668;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) = 1;
    if (((uint32_t)(local_rbx - 1)) > (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598))) goto loc_00340878;
loc_003405EC:
    v_stack_mB0 = 0;
    if ((((uint32_t)((uint32_t)(v_stack_mE0))) & (1)) != 0) { Arg3 = 1; }
    v_stack_mB0 = Arg3;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) != 0) goto loc_003408A4;
loc_0034060C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) << (12));
    v_stack_mB8 = result;
    result = MmCheckCachedPageStates(local_rdi, (uint32_t)((uint32_t)(result)), Arg3, v_stack_p8);
    v_stack_m98 = (uint32_t)(result);
    if (sign_flag) goto loc_00340668;
    local_rdi = (local_rdi) + (v_stack_mB8);
    v_stack_m78 = local_rdi;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    v_stack_mAC = (uint32_t)(local_rbx);
    Arg4 = 2;
    if (((uint32_t)(local_rbx)) == 1) { Arg4 = 4; }
    Arg3 = 0;
    goto loc_003405CC;
loc_00340668:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2)) & (1));
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) = (uint8_t)(result);
    local_r12 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2) >> (1));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598) = (uint32_t)(local_r12);
    if (sign_flag) {
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    }
    result = ExAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    if ((*(uint64_t *)(v_stack_mE8 + 0xB8)) == 0) {
        result = *(uint64_t *)(arg8);
        *(uint64_t *)(v_stack_mE8 + 0xB8) = result;
        result = v_stack_mD8;
        *(uint64_t *)(v_stack_mE8 + 0x38) = result;
        result = 0;
        v_stack_mD8 = 0;
    }
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) - (*(uint32_t *)(v_stack_mE8 + 0x8)));
    result = (result) + (*(uint64_t *)(v_stack_mE8 + 0xB8));
    *(uint64_t *)(arg8) = result;
    Arg3 = 0;
loc_003406F1:
    v_stack_mF8 = 1;
    goto loc_0033FF8D;
loc_00340703:
    Arg2 = 0;
    result = ExAcquireResourceExclusiveLite(0, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00340524;
    result = 0;
    v_stack_m108 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(result + 52, (uint32_t)(0x20213ULL), local_rbx, Arg4);
loc_0034072F:
    result = ExAcquireResourceExclusiveLite(result + 52, (uint32_t)(0x20213ULL), local_rbx, Arg4);
    Arg3 = 0;
    goto loc_0034021D;
loc_0034073C:
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, (uint32_t)(0x20213ULL), Arg3, Arg4);
    local_r15 = 0;
    v_stack_mF4 = 0;
    Arg3 = 0;
    result = CcMapAndRead((uint32_t)((uint32_t)(Arg8)), (uint32_t)((uint32_t)(local_rbx)), Arg3, *(uint64_t *)(arg8));
    if ((uint8_t)(result) == 0) goto loc_003407F9;
    result = ExAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288, (uint32_t)((uint32_t)(local_rbx)), Arg3, *(uint64_t *)(arg8));
    if ((*(uint64_t *)(v_stack_mE8 + 0xB8)) != 0) goto loc_003403AE;
    *(uint64_t *)(v_stack_mE8 + 0xB8) = *(uint64_t *)(arg8);
    *(uint64_t *)(v_stack_mE8 + 0x38) = v_stack_mD8;
    v_stack_mD8 = 0;
    goto loc_003403AE;
loc_003407AF:
    if (((uint32_t)(v_stack_mD8)) <= 15) goto loc_003408BA;
    *(uint32_t *)(v_stack_mE8 + 0x598) = 15;
    goto loc_0033FF28;
loc_003407C7:
    v_stack_m108 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(454, Arg4 + 15, Arg3, Arg4);
loc_003407DE:
    v_stack_mF8 = (uint8_t)(local_rbx);
    Arg3 = 0;
    goto loc_0033FF8D;
loc_003407EA:
    result = ExAcquireResourceExclusiveLite(0, 1, Arg3, Arg4);
    goto loc_0033FE85;
loc_003407F9:
    v_stack_mF8 = 0;
    Arg3 = 0;
    goto loc_0033FF8D;
loc_0034080E:
    if (v_stack_mE8 == 0) goto loc_0033FF9B;
    if ((*(uint64_t *)(v_stack_mE8 + 0xB8)) == 0) goto loc_00340ADA;
    Arg1 = (uint32_t)((-1) - 1);
    if ((uint16_t)(Arg1) != 0) goto loc_00340863;
    result = *(uint64_t *)(v_stack_mE8 + 0x38);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) + 0xC0) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) + 0xC0), Arg2, Arg3, Arg4);
    }
    Arg3 = 0;
loc_00340863:
    *(uint64_t *)(v_stack_mE8 + 0xB8) = 0;
    *(uint64_t *)(v_stack_mE8 + 0x38) = 0;
    goto loc_00340ADA;
loc_00340878:
    if (((uint32_t)(result)) <= 15) goto loc_003408D5;
    *(uint32_t *)(- 0x1 + 0x598) = 15;
    goto loc_003405EC;
loc_0034088D:
    v_stack_m108 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(454, Arg4 + 15, Arg3, Arg4);
loc_003408A4:
    if (0 == 2) goto loc_0034060C;
    goto loc_0034060C;
loc_003408BA:
    *(uint32_t *)(v_stack_mE8 + 0x598) = (uint32_t)(result);
    goto loc_0033FF28;
loc_003408C5:
    v_stack_mA0 = 454;
    goto loc_00340060;
loc_003408D5:
    *(uint32_t *)(- 0x1 + 0x598) = (uint32_t)(result);
    goto loc_003405EC;
loc_003408E1:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98)) & (512)) == 0) goto loc_0033FD44;
    if (454 <= 0x2000000ULL) goto loc_00340916;
    result = CcGetBcbListHeadLargeOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), v_stack_mE8, 1, Arg4);
    goto loc_0033FD48;
loc_00340916:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) >> (18));
    result = (uint32_t)((result) + 1);
    result = (uint32_t)((result) & (0xFFFFFFFEULL));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_mE8)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) << (19));
    result = (uint32_t)((result) - (0x80000ULL));
    if (1 >= result) goto loc_0033FD44;
    if (0 != 0) goto loc_00340AC6;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8))) <= 0x100000ULL) goto loc_00340AD0;
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) >> (18);
    Arg1 = (Arg1) << (3);
loc_00340957:
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x58));
    local_rdi = (result) >> (19);
    local_rdi = (local_rdi) << (4);
    local_rdi = (local_rdi) + (Arg1);
    goto loc_0033FD48;
loc_0034096B:
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_0033FE7B;
    result = ExpFastResourceLegacyAcquireSharedStarveExclusive(1, 1, 1, Arg4);
    goto loc_0033FE85;
loc_00340988:
    if (1 >= = 1) {
        Arg3 = 1;
        v_stack_m108 = 1;
        Arg2 = 0;
        Arg1 = 454;
        Arg4 = Arg2 + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC0);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC0))) & (2)) != 0) {
        v_stack_m108 = 1;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = Arg4 + 6;
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint8_t)(Arg2)) >= 1) goto loc_0034096B;
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_0034096B;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) != 1) goto loc_0034096B;
loc_003409F6:
    v_stack_m108 = 1;
    Arg4 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(454, Arg4 + 7, Arg3, Arg4);
loc_00340A10:
    if (((454) & (1)) == 0) goto loc_003404F5;
    Arg2 = 0;
    result = ExpFastResourceLegacyAcquireSharedStarveExclusive(0, Arg2, Arg3, Arg4);
    goto loc_003404FF;
loc_00340A35:
    if (1 >= = 2) {
        Arg3 = 1;
        v_stack_m108 = 1;
        Arg2 = 0;
        Arg1 = 454;
        Arg4 = Arg2 + 2;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (condition_is_below) goto loc_00340A8C;
    result = (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C)));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) {
        v_stack_m108 = 1;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = Arg4 + 5;
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0xC0))) & (2)) != 0) goto loc_003409C0;
    if (((uint8_t)(Arg2)) >= 1) goto loc_00340A10;
    if (((*(uint32_t *)(Arg4 + 0x74)) & (0x400ULL)) != 0) goto loc_00340A10;
    if ((*(uint32_t *)(Arg4 + 0x1E4)) == 0) goto loc_003409F6;
    goto loc_00340A10;
loc_00340AC6:
    goto loc_00340957;
loc_00340AD0:
    goto loc_00340957;
loc_00340ADA:
    result = *(uint8_t *)(Arg4 + 0xC0);
    if (v_stack_mF4 != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 288;
        result = ExReleaseFastMutex(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mD8 == 0) goto loc_00340B2C;
    local_r15 = (uint32_t)((-1) - 1);
    if ((uint16_t)(local_r15) != 0) goto loc_00340B27;
    result = v_stack_mD8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x8) + 0xC0) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x8) + 0xC0), Arg2, Arg3, Arg4);
    }
loc_00340B27:
loc_00340B2C:
    if ((((uint8_t)((uint32_t)((uint32_t)(4 - 3)))) & (4)) == 0) goto loc_00340B43;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20)) > 0x2000000ULL) goto loc_00340C63;
loc_00340B43:
    if (v_stack_mF8 == 0) goto loc_00340B7D;
    *(uint64_t *)(arg7) = v_stack_mE8;
    *(uint64_t *)(arg9) = *(uint64_t *)(v_stack_mE8 + 0x20);
loc_00340B64:
    local_rsp = (local_rsp) + (240);
    return v_stack_mF8;
loc_00340B7D:
    result = 0;
    *(uint64_t *)(arg8) = 0;
    if (v_stack_mE8 == 0) goto loc_00340B64;
    Arg3 = 0;
    result = CcUnpinFileDataEx(v_stack_mE8, v_stack_p148, Arg3, Arg4);
    goto loc_00340B64;
loc_00340B9D:
    result = KiRaiseIrqlProcessIrqlFlags(0, 1, Arg3, Arg4);
    goto loc_0033FC34;
loc_00340BBD:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(1))) & (0x3FFFFULL));
    result = (uint32_t)(((uint32_t)(0x40000ULL)) - ((uint32_t)(Arg1)));
    v_stack_p58 = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x20)) <= 0x2000000ULL) goto loc_0033FBFA;
    v_stack_pD8 = Arg8;
    v_stack_pC8 = v_stack_pC0;
    v_stack_pC0 = v_stack_pC0;
    v_stack_pD0 = Arg8;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) + 0x98))) >> (9));
    Arg2 = (uint8_t)((Arg2) & (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAC9C71))) - 1);
    result = CcAllocateVacbLevels(Arg1, Arg2, v_stack_pC0, Arg4);
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), Arg2, v_stack_pC0, Arg4);
loc_00340C45:
    v_stack_p20 = Arg8;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, 325, 0xFFFFFFFFC0000420ULL, Arg4);
loc_00340C63:
    result = CcAcquireBcbLockAndVacbLock(1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), 0xFFFFFFFFC0000420ULL, Arg4);
    Arg4 = 0;
    result = SetVacb(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), *(uint64_t *)(1), 1 - 3, Arg4);
    result = CcReleaseBcbLockAndVacbLock(1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8), 1 - 3, Arg4);
    goto loc_00340B43;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `R/W` |
| `Arg8` | `+ 0x0` | `64` | `W` |
| `Arg9` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033FB40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
