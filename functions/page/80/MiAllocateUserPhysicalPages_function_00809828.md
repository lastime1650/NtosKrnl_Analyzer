# MiAllocateUserPhysicalPages

- RVA: `0x00809828`–`0x0080A65D` (길이 `3,637` bytes)
- VA: `0x0000000140809828`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8B58`
- 디코드: `817`개 명령, `3,637/3,637` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008098A1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008098B4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00809901` → [MiCaptureAllocateMapExtendedParameters](../9A/MiCaptureAllocateMapExtendedParameters_function_009A2110.md) (function, `0x009A2110`)
- `0x00809971` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (function, `0x004A0650`)
- `0x00809A37` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00809A64` → [MiReferenceAweHandle](../../text/4E/MiReferenceAweHandle_function_004E00A4.md) (function, `0x004E00A4`)
- `0x00809A7E` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00809AD1` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00809AF7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00809B22` → [MiCreateProcessDefaultAweInfo](MiCreateProcessDefaultAweInfo_function_0080A8C0.md) (function, `0x0080A8C0`)
- `0x00809B42` → [MiGetAwePageSize](../../text/46/MiGetAwePageSize_function_0046CFA8.md) (function, `0x0046CFA8`)
- `0x00809C1F` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (function, `0x002A8B3C`)
- `0x00809C34` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x00809C4A` → [MiChargeProcessPhysicalPages](../A9/MiChargeProcessPhysicalPages_function_00A99CDC.md) (function, `0x00A99CDC`)
- `0x00809C59` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x00809C6C` → [MiChargeProcessCommitment](../../text/43/MiChargeProcessCommitment_function_004384C0.md) (function, `0x004384C0`)
- `0x00809C7B` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x00809C92` → [MiGetAweInfoPartition](../../text/2A/MiGetAweInfoPartition_function_002AA2CC.md) (function, `0x002AA2CC`)
- `0x00809D47` → [KeGetIdealNodeNumberThread](../../text/49/KeGetIdealNodeNumberThread_function_00492A1C.md) (function, `0x00492A1C`)
- `0x00809DA4` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x00809EF3` → [MiAllocateUserPhysicalRanges](../AC/MiAllocateUserPhysicalRanges_function_00ACD988.md) (function, `0x00ACD988`)
- `0x00809F3F` → [MiAllocateFastAwePages](MiAllocateFastAwePages_function_0080969C.md) (function, `0x0080969C`)
- `0x0080A030` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (function, `0x003EABEC`)
- `0x0080A13C` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (function, `0x003EABEC`)
- `0x0080A1B8` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (function, `0x002A8B3C`)
- `0x0080A1DB` → [MiLockAwePagesShared](../../text/4B/MiLockAwePagesShared_function_004B9D2C.md) (function, `0x004B9D2C`)
- `0x0080A201` → [MiUnlockAwePagesShared](../../text/4C/MiUnlockAwePagesShared_function_004C66C4.md) (function, `0x004C66C4`)
- `0x0080A218` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x0080A222` → [MiResizeAweBitMap](MiResizeAweBitMap_function_0080AD00.md) (function, `0x0080AD00`)
- `0x0080A2B3` → [MiUnlockAwePagesShared](../../text/4C/MiUnlockAwePagesShared_function_004C66C4.md) (function, `0x004C66C4`)
- `0x0080A2D7` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x0080A336` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x0080A359` → [MiGetCrossPartitionCharges](../../text/32/MiGetCrossPartitionCharges_function_00325BFC.md) (function, `0x00325BFC`)
- `0x0080A3D6` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0080A418` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x0080A42A` → [MiFreeAwePagesFromMdl](../../text/68/MiFreeAwePagesFromMdl_function_00688984.md) (function, `0x00688984`)
- `0x0080A441` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0080A461` → [MiFreeAwePagesFromMdl](../../text/68/MiFreeAwePagesFromMdl_function_00688984.md) (function, `0x00688984`)
- `0x0080A47C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0080A584` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0080A5C4` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (function, `0x002A8B3C`)
- `0x0080A5CF` → [MiReturnProcessCommitment](../../text/45/MiReturnProcessCommitment_function_0045CED4.md) (function, `0x0045CED4`)
- `0x0080A5DA` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (function, `0x002A8ACC`)
- `0x0080A608` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0080A628` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0080A644` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtAllocateUserPhysicalPages](NtAllocateUserPhysicalPages_function_0080AEF0.md) at `0x0080AEFC`
- [NtAllocateUserPhysicalPagesEx](NtAllocateUserPhysicalPagesEx_function_0080AF10.md) at `0x0080AF1C`

### Static image references
- `0x0080983D` → RVA `0x00E0A740` (`.data`; read)
- `0x0080999A` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00809ACA` → RVA `0x00FD9AD0` (`PAGEDATA`; read)
- `0x00809FC5` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **38**
  - `0x008098A1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008098B4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00809971` → [MiHugePagesSupported](../../text/4A/MiHugePagesSupported_function_004A0650.md) (`PAGE` → `.text`)
  - `0x00809A64` → [MiReferenceAweHandle](../../text/4E/MiReferenceAweHandle_function_004E00A4.md) (`PAGE` → `.text`)
  - `0x00809A7E` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00809AF7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00809B42` → [MiGetAwePageSize](../../text/46/MiGetAwePageSize_function_0046CFA8.md) (`PAGE` → `.text`)
  - `0x00809C1F` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (`PAGE` → `.text`)
  - `0x00809C34` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x00809C59` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x00809C6C` → [MiChargeProcessCommitment](../../text/43/MiChargeProcessCommitment_function_004384C0.md) (`PAGE` → `.text`)
  - `0x00809C7B` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x00809C92` → [MiGetAweInfoPartition](../../text/2A/MiGetAweInfoPartition_function_002AA2CC.md) (`PAGE` → `.text`)
  - `0x00809D47` → [KeGetIdealNodeNumberThread](../../text/49/KeGetIdealNodeNumberThread_function_00492A1C.md) (`PAGE` → `.text`)
  - `0x00809DA4` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x0080A030` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (`PAGE` → `.text`)
  - `0x0080A13C` → [MiAllocatePagesForMdl](../../text/3E/MiAllocatePagesForMdl_function_003EABEC.md) (`PAGE` → `.text`)
  - `0x0080A1B8` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (`PAGE` → `.text`)
  - `0x0080A1DB` → [MiLockAwePagesShared](../../text/4B/MiLockAwePagesShared_function_004B9D2C.md) (`PAGE` → `.text`)
  - `0x0080A201` → [MiUnlockAwePagesShared](../../text/4C/MiUnlockAwePagesShared_function_004C66C4.md) (`PAGE` → `.text`)
  - `0x0080A218` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x0080A2B3` → [MiUnlockAwePagesShared](../../text/4C/MiUnlockAwePagesShared_function_004C66C4.md) (`PAGE` → `.text`)
  - `0x0080A2D7` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x0080A336` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x0080A359` → [MiGetCrossPartitionCharges](../../text/32/MiGetCrossPartitionCharges_function_00325BFC.md) (`PAGE` → `.text`)
  - `0x0080A3D6` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0080A418` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x0080A42A` → [MiFreeAwePagesFromMdl](../../text/68/MiFreeAwePagesFromMdl_function_00688984.md) (`PAGE` → `.text`)
  - `0x0080A441` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0080A461` → [MiFreeAwePagesFromMdl](../../text/68/MiFreeAwePagesFromMdl_function_00688984.md) (`PAGE` → `.text`)
  - `0x0080A47C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0080A584` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0080A5C4` → [LOCK_ADDRESS_SPACE_SHARED](../../text/2A/LOCK_ADDRESS_SPACE_SHARED_function_002A8B3C.md) (`PAGE` → `.text`)
  - `0x0080A5CF` → [MiReturnProcessCommitment](../../text/45/MiReturnProcessCommitment_function_0045CED4.md) (`PAGE` → `.text`)
  - `0x0080A5DA` → [UNLOCK_ADDRESS_SPACE_SHARED](../../text/2A/UNLOCK_ADDRESS_SPACE_SHARED_function_002A8ACC.md) (`PAGE` → `.text`)
  - `0x0080A608` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0080A628` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0080A644` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00809828  4C 8B DC                        mov r11, rsp
0080982B  53                              push rbx
0080982C  56                              push rsi
0080982D  57                              push rdi
0080982E  41 54                           push r12
00809830  41 55                           push r13
00809832  41 56                           push r14
00809834  41 57                           push r15
00809836  48 81 EC 00 03 00 00            sub rsp, 0x300
0080983D  48 8B 05 FC 0E 60 00            mov rax, qword ptr [rip + 0x600efc]
00809844  48 33 C4                        xor rax, rsp
00809847  48 89 84 24 F0 02 00 00         mov qword ptr [rsp + 0x2f0], rax
0080984F  49 8B F1                        mov rsi, r9
00809852  4C 8B F2                        mov r14, rdx
00809855  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
0080985D  4C 8B E9                        mov r13, rcx
00809860  4D 89 83 B8 FD FF FF            mov qword ptr [r11 - 0x248], r8
00809867  0F 57 C0                        xorps xmm0, xmm0
0080986A  0F 11 84 24 90 01 00 00         movups xmmword ptr [rsp + 0x190], xmm0
00809872  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
0080987A  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00809882  33 DB                           xor ebx, ebx
00809884  49 89 9B 78 FD FF FF            mov qword ptr [r11 - 0x288], rbx
0080988B  49 89 9B 48 FD FF FF            mov qword ptr [r11 - 0x2b8], rbx
00809892  33 D2                           xor edx, edx
00809894  41 B8 30 01 00 00               mov r8d, 0x130
0080989A  49 8D 8B 88 FE FF FF            lea rcx, [r11 - 0x178]
008098A1  E8 9A D3 EB FF                  call 0x1406c6c40
008098A6  33 D2                           xor edx, edx
008098A8  44 8D 43 48                     lea r8d, [rbx + 0x48]
008098AC  48 8D 8C 24 40 01 00 00         lea rcx, [rsp + 0x140]
008098B4  E8 87 D3 EB FF                  call 0x1406c6c40
008098B9  8B FB                           mov edi, ebx
008098BB  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008098BF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008098C8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008098CD  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008098D4  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
008098DC  44 8A A0 32 02 00 00            mov r12b, byte ptr [rax + 0x232]
008098E3  48 8D 84 24 40 01 00 00         lea rax, [rsp + 0x140]
008098EB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008098F0  44 8D 4B 24                     lea r9d, [rbx + 0x24]
008098F4  45 8A C4                        mov r8b, r12b
008098F7  8B 94 24 60 03 00 00            mov edx, dword ptr [rsp + 0x360]
008098FE  48 8B CE                        mov rcx, rsi
00809901  E8 0A 88 19 00                  call 0x1409a2110
00809906  85 C0                           test eax, eax
00809908  0F 88 2B 0D 00 00               js 0x14080a639
0080990E  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00809916  48 F7 C1 E5 FF FF FF            test rcx, -0x1b
0080991D  0F 85 11 0D 00 00               jne 0x14080a634
00809923  48 8B C1                        mov rax, rcx
00809926  83 E0 1A                        and eax, 0x1a
00809929  74 0A                           je 0x140809935
0080992B  04 FF                           add al, 0xff
0080992D  22 C1                           and al, cl
0080992F  A8 1A                           test al, 0x1a
00809931  8B C3                           mov eax, ebx
00809933  75 05                           jne 0x14080993a
00809935  B8 01 00 00 00                  mov eax, 1
0080993A  85 C0                           test eax, eax
0080993C  0F 84 F2 0C 00 00               je 0x14080a634
00809942  BA 02 00 00 00                  mov edx, 2
00809947  84 CA                           test dl, cl
00809949  74 0E                           je 0x140809959
0080994B  48 C7 84 24 88 00 00 00 10 00 00 00  mov qword ptr [rsp + 0x88], 0x10
00809957  EB 41                           jmp 0x14080999a
00809959  F6 C1 08                        test cl, 8
0080995C  74 0E                           je 0x14080996c
0080995E  48 C7 84 24 88 00 00 00 00 02 00 00  mov qword ptr [rsp + 0x88], 0x200
0080996A  EB 2E                           jmp 0x14080999a
0080996C  F6 C1 10                        test cl, 0x10
0080996F  74 21                           je 0x140809992
00809971  E8 DA 6C C9 FF                  call 0x1404a0650
00809976  85 C0                           test eax, eax
00809978  75 0A                           jne 0x140809984
0080997A  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0080997F  E9 B5 0C 00 00                  jmp 0x14080a639
00809984  48 C7 84 24 88 00 00 00 00 00 04 00  mov qword ptr [rsp + 0x88], 0x40000
00809990  EB 08                           jmp 0x14080999a
00809992  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0080999A  0F B7 05 5F B6 7B 00            movzx eax, word ptr [rip + 0x7bb65f]
008099A1  39 84 24 60 01 00 00            cmp dword ptr [rsp + 0x160], eax
008099A8  0F 87 86 0C 00 00               ja 0x14080a634
008099AE  45 84 E4                        test r12b, r12b
008099B1  75 1F                           jne 0x1408099d2
008099B3  4D 8B 36                        mov r14, qword ptr [r14]
008099B6  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
008099BE  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
008099C6  4D 85 F6                        test r14, r14
008099C9  75 76                           jne 0x140809a41
008099CB  33 C0                           xor eax, eax
008099CD  E9 67 0C 00 00                  jmp 0x14080a639
008099D2  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008099DC  4C 3B F1                        cmp r14, rcx
008099DF  49 0F 42 CE                     cmovb rcx, r14
008099E3  48 8B 01                        mov rax, qword ptr [rcx]
008099E6  48 89 01                        mov qword ptr [rcx], rax
008099E9  4D 8B 36                        mov r14, qword ptr [r14]
008099EC  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
008099F4  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
008099FC  4D 85 F6                        test r14, r14
008099FF  75 07                           jne 0x140809a08
00809A01  33 C0                           xor eax, eax
00809A03  E9 31 0C 00 00                  jmp 0x14080a639
00809A08  48 B8 FF FF FF FF FF FF FF 1F   movabs rax, 0x1fffffffffffffff
00809A12  4C 3B F0                        cmp r14, rax
00809A15  76 0A                           jbe 0x140809a21
00809A17  B8 F0 00 00 C0                  mov eax, 0xc00000f0
00809A1C  E9 18 0C 00 00                  jmp 0x14080a639
00809A21  4A 8D 14 F5 00 00 00 00         lea rdx, [r14*8]
00809A29  41 B8 08 00 00 00               mov r8d, 8
00809A2F  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00809A37  E8 84 F7 0D 00                  call 0x1408e91c0
00809A3C  BA 02 00 00 00                  mov edx, 2
00809A41  4C 8B FB                        mov r15, rbx
00809A44  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00809A49  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00809A51  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00809A56  4C 8D 8C 24 80 00 00 00         lea r9, [rsp + 0x80]
00809A5E  45 8A C4                        mov r8b, r12b
00809A61  49 8B CD                        mov rcx, r13
00809A64  E8 3B 66 CD FF                  call 0x1404e00a4
00809A69  85 C0                           test eax, eax
00809A6B  0F 88 C8 0B 00 00               js 0x14080a639
00809A71  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00809A79  48 85 C9                        test rcx, rcx
00809A7C  74 18                           je 0x140809a96
00809A7E  E8 2D B2 A8 FF                  call 0x140294cb0
00809A83  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
00809A8B  4C 8B 78 08                     mov r15, qword ptr [rax + 8]
00809A8F  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00809A94  EB 21                           jmp 0x140809ab7
00809A96  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
00809A9E  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00809AA3  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
00809AAB  48 85 F6                        test rsi, rsi
00809AAE  75 17                           jne 0x140809ac7
00809AB0  8D 7E 08                        lea edi, [rsi + 8]
00809AB3  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809AB7  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
00809ABF  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
00809AC4  49 8B F5                        mov rsi, r13
00809AC7  41 8A D4                        mov dl, r12b
00809ACA  48 8B 0D FF FF 7C 00            mov rcx, qword ptr [rip + 0x7cffff]
00809AD1  E8 4A 83 06 00                  call 0x140871e20
00809AD6  84 C0                           test al, al
00809AD8  75 0B                           jne 0x140809ae5
00809ADA  41 BD 61 00 00 C0               mov r13d, 0xc0000061
00809AE0  E9 C9 0A 00 00                  jmp 0x14080a5ae
00809AE5  49 3B F5                        cmp rsi, r13
00809AE8  74 19                           je 0x140809b03
00809AEA  4C 8D 84 24 90 01 00 00         lea r8, [rsp + 0x190]
00809AF2  33 D2                           xor edx, edx
00809AF4  48 8B CE                        mov rcx, rsi
00809AF7  E8 24 CD A0 FF                  call 0x140216820
00809AFC  83 CF 01                        or edi, 1
00809AFF  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809B03  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
00809B0B  4D 85 FF                        test r15, r15
00809B0E  74 0A                           je 0x140809b1a
00809B10  4C 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r15
00809B18  EB 25                           jmp 0x140809b3f
00809B1A  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00809B1F  41 8A CC                        mov cl, r12b
00809B22  E8 99 0D 00 00                  call 0x14080a8c0
00809B27  44 8B E8                        mov r13d, eax
00809B2A  85 C0                           test eax, eax
00809B2C  0F 88 7C 0A 00 00               js 0x14080a5ae
00809B32  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
00809B3A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00809B3F  49 8B CF                        mov rcx, r15
00809B42  E8 61 34 C6 FF                  call 0x14046cfa8
00809B47  48 8B C8                        mov rcx, rax
00809B4A  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00809B52  48 83 F8 10                     cmp rax, 0x10
00809B56  75 0A                           jne 0x140809b62
00809B58  C7 44 24 54 00 10 00 00         mov dword ptr [rsp + 0x54], 0x1000
00809B60  EB 28                           jmp 0x140809b8a
00809B62  48 81 F9 00 02 00 00            cmp rcx, 0x200
00809B69  75 0A                           jne 0x140809b75
00809B6B  C7 44 24 54 00 00 00 01         mov dword ptr [rsp + 0x54], 0x1000000
00809B73  EB 15                           jmp 0x140809b8a
00809B75  8B C3                           mov eax, ebx
00809B77  BA 00 00 00 02                  mov edx, 0x2000000
00809B7C  48 81 F9 00 00 04 00            cmp rcx, 0x40000
00809B83  0F 44 C2                        cmove eax, edx
00809B86  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00809B8A  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00809B8E  A8 08                           test al, 8
00809B90  74 07                           je 0x140809b99
00809B92  83 CF 20                        or edi, 0x20
00809B95  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809B99  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
00809BA1  4D 85 C9                        test r9, r9
00809BA4  75 0D                           jne 0x140809bb3
00809BA6  4C 8B C9                        mov r9, rcx
00809BA9  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00809BB1  EB 27                           jmp 0x140809bda
00809BB3  4C 3B C9                        cmp r9, rcx
00809BB6  0F 86 EC 09 00 00               jbe 0x14080a5a8
00809BBC  33 D2                           xor edx, edx
00809BBE  49 8B C1                        mov rax, r9
00809BC1  48 F7 F1                        div rcx
00809BC4  48 85 D2                        test rdx, rdx
00809BC7  0F 85 DB 09 00 00               jne 0x14080a5a8
00809BCD  49 8D 41 FF                     lea rax, [r9 - 1]
00809BD1  49 85 C1                        test r9, rax
00809BD4  0F 85 CE 09 00 00               jne 0x14080a5a8
00809BDA  49 83 F9 01                     cmp r9, 1
00809BDE  76 2A                           jbe 0x140809c0a
00809BE0  49 8B C6                        mov rax, r14
00809BE3  49 0F AF C1                     imul rax, r9
00809BE7  4C 3B F0                        cmp r14, rax
00809BEA  72 0B                           jb 0x140809bf7
00809BEC  41 BD F0 00 00 C0               mov r13d, 0xc00000f0
00809BF2  E9 B7 09 00 00                  jmp 0x14080a5ae
00809BF7  4C 8B F0                        mov r14, rax
00809BFA  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00809C02  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00809C0A  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00809C0F  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
00809C17  75 76                           jne 0x140809c8f
00809C19  48 8B D6                        mov rdx, rsi
00809C1C  49 8B CC                        mov rcx, r12
00809C1F  E8 18 EF A9 FF                  call 0x1402a8b3c
00809C24  8B 86 F4 01 00 00               mov eax, dword ptr [rsi + 0x1f4]
00809C2A  A8 20                           test al, 0x20
00809C2C  74 16                           je 0x140809c44
00809C2E  48 8B D6                        mov rdx, rsi
00809C31  49 8B CC                        mov rcx, r12
00809C34  E8 93 EE A9 FF                  call 0x1402a8acc
00809C39  41 BD 0A 01 00 C0               mov r13d, 0xc000010a
00809C3F  E9 6F 09 00 00                  jmp 0x14080a5b3
00809C44  49 8B D6                        mov rdx, r14
00809C47  48 8B CE                        mov rcx, rsi
00809C4A  E8 8D 00 29 00                  call 0x140a99cdc
00809C4F  85 C0                           test eax, eax
00809C51  75 16                           jne 0x140809c69
00809C53  48 8B D6                        mov rdx, rsi
00809C56  49 8B CC                        mov rcx, r12
00809C59  E8 6E EE A9 FF                  call 0x1402a8acc
00809C5E  41 BD 2D 01 00 C0               mov r13d, 0xc000012d
00809C64  E9 4A 09 00 00                  jmp 0x14080a5b3
00809C69  83 CF 04                        or edi, 4
00809C6C  E8 4F E8 C2 FF                  call 0x1404384c0
00809C71  48 8B D6                        mov rdx, rsi
00809C74  49 8B CC                        mov rcx, r12
00809C77  85 C0                           test eax, eax
00809C79  74 DE                           je 0x140809c59
00809C7B  E8 4C EE A9 FF                  call 0x1402a8acc
00809C80  83 CF 02                        or edi, 2
00809C83  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809C87  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
00809C8F  49 8B CF                        mov rcx, r15
00809C92  E8 35 06 AA FF                  call 0x1402aa2cc
00809C97  4C 8B D8                        mov r11, rax
00809C9A  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00809CA2  48 8B 90 48 48 00 00            mov rdx, qword ptr [rax + 0x4848]
00809CA9  48 FF C2                        inc rdx
00809CAC  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
00809CB4  48 89 9C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbx
00809CBC  48 89 9C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rbx
00809CC4  48 39 9E 10 03 00 00            cmp qword ptr [rsi + 0x310], rbx
00809CCB  74 3C                           je 0x140809d09
00809CCD  0F B7 8E EC 06 00 00            movzx ecx, word ptr [rsi + 0x6ec]
00809CD4  B8 4C 01 00 00                  mov eax, 0x14c
00809CD9  66 3B C8                        cmp cx, ax
00809CDC  74 0C                           je 0x140809cea
00809CDE  B8 C4 01 00 00                  mov eax, 0x1c4
00809CE3  66 3B C8                        cmp cx, ax
00809CE6  8A C3                           mov al, bl
00809CE8  75 02                           jne 0x140809cec
00809CEA  B0 01                           mov al, 1
00809CEC  84 C0                           test al, al
00809CEE  74 19                           je 0x140809d09
00809CF0  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
00809CFA  48 3B D0                        cmp rdx, rax
00809CFD  48 0F 47 D0                     cmova rdx, rax
00809D01  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
00809D09  4C 8B FA                        mov r15, rdx
00809D0C  49 C1 E7 0C                     shl r15, 0xc
00809D10  44 8B EB                        mov r13d, ebx
00809D13  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00809D17  BA 00 00 00 80                  mov edx, 0x80000000
00809D1C  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00809D21  44 0B C2                        or r8d, edx
00809D24  8B 84 24 60 01 00 00            mov eax, dword ptr [rsp + 0x160]
00809D2B  85 C0                           test eax, eax
00809D2D  74 15                           je 0x140809d44
00809D2F  44 8D 70 FF                     lea r14d, [rax - 1]
00809D33  8A 84 24 71 01 00 00            mov al, byte ptr [rsp + 0x171]
00809D3A  84 C0                           test al, al
00809D3C  74 19                           je 0x140809d57
00809D3E  41 83 C8 02                     or r8d, 2
00809D42  EB 13                           jmp 0x140809d57
00809D44  49 8B CC                        mov rcx, r12
00809D47  E8 D0 8C C8 FF                  call 0x140492a1c
00809D4C  44 0F B7 F0                     movzx r14d, ax
00809D50  8A 84 24 71 01 00 00            mov al, byte ptr [rsp + 0x171]
00809D57  45 8B E6                        mov r12d, r14d
00809D5A  84 C0                           test al, al
00809D5C  75 03                           jne 0x140809d61
00809D5E  44 0B E2                        or r12d, edx
00809D61  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
00809D66  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
00809D6A  A8 04                           test al, 4
00809D6C  74 04                           je 0x140809d72
00809D6E  41 83 C8 01                     or r8d, 1
00809D72  49 8B F1                        mov rsi, r9
00809D75  48 C1 E6 0C                     shl rsi, 0xc
00809D79  48 8B C3                        mov rax, rbx
00809D7C  49 83 F9 01                     cmp r9, 1
00809D80  48 0F 45 C6                     cmovne rax, rsi
00809D84  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00809D8C  41 8B C0                        mov eax, r8d
00809D8F  83 C8 30                        or eax, 0x30
00809D92  49 83 F9 01                     cmp r9, 1
00809D96  44 0F 45 C0                     cmovne r8d, eax
00809D9A  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00809D9F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00809DA4  E8 67 9D C3 FF                  call 0x140443b10
00809DA9  4C 3B D8                        cmp r11, rax
00809DAC  75 4E                           jne 0x140809dfc
00809DAE  41 0F BA E0 0C                  bt r8d, 0xc
00809DB3  0F 92 C1                        setb cl
00809DB6  40 F6 C7 20                     test dil, 0x20
00809DBA  0F 94 C0                        sete al
00809DBD  84 C8                           test al, cl
00809DBF  74 3B                           je 0x140809dfc
00809DC1  49 83 F9 10                     cmp r9, 0x10
00809DC5  75 35                           jne 0x140809dfc
00809DC7  41 8B 43 04                     mov eax, dword ptr [r11 + 4]
00809DCB  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
00809DD0  41 84 C1                        test r9b, al
00809DD3  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00809DDB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00809DE0  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00809DE8  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00809DF0  75 12                           jne 0x140809e04
00809DF2  0F BA EF 07                     bts edi, 7
00809DF6  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809DFA  EB 08                           jmp 0x140809e04
00809DFC  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00809E04  49 8D 4A 08                     lea rcx, [r10 + 8]
00809E08  48 89 8C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rcx
00809E10  BA 00 00 0C 00                  mov edx, 0xc0000
00809E15  48 8B CB                        mov rcx, rbx
00809E18  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00809E1D  4C 8B D8                        mov r11, rax
00809E20  4C 2B 9C 24 90 00 00 00         sub r11, qword ptr [rsp + 0x90]
00809E28  4C 89 9C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r11
00809E30  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00809E38  49 83 F8 01                     cmp r8, 1
00809E3C  75 0F                           jne 0x140809e4d
00809E3E  4C 3B DA                        cmp r11, rdx
00809E41  4C 0F 47 DA                     cmova r11, rdx
00809E45  4C 89 9C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r11
00809E4D  40 F6 C7 40                     test dil, 0x40
00809E51  75 69                           jne 0x140809ebc
00809E53  33 D2                           xor edx, edx
00809E55  49 8B C3                        mov rax, r11
00809E58  49 F7 F0                        div r8
00809E5B  48 83 F8 20                     cmp rax, 0x20
00809E5F  77 5B                           ja 0x140809ebc
00809E61  83 CF 40                        or edi, 0x40
00809E64  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809E68  4C 8D 84 24 C0 01 00 00         lea r8, [rsp + 0x1c0]
00809E70  48 C1 E0 0C                     shl rax, 0xc
00809E74  48 89 9C 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rbx
00809E7C  48 8D 88 FF 0F 00 00            lea rcx, [rax + 0xfff]
00809E83  48 C1 E9 0C                     shr rcx, 0xc
00809E87  66 83 C1 06                     add cx, 6
00809E8B  66 C1 E1 03                     shl cx, 3
00809E8F  66 89 8C 24 C8 01 00 00         mov word ptr [rsp + 0x1c8], cx
00809E97  66 89 9C 24 CA 01 00 00         mov word ptr [rsp + 0x1ca], bx
00809E9F  48 89 9C 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rbx
00809EA7  89 9C 24 EC 01 00 00            mov dword ptr [rsp + 0x1ec], ebx
00809EAE  89 84 24 E8 01 00 00            mov dword ptr [rsp + 0x1e8], eax
00809EB5  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00809EBA  EB 03                           jmp 0x140809ebf
00809EBC  4C 8B C3                        mov r8, rbx
00809EBF  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
00809EC7  40 F6 C7 20                     test dil, 0x20
00809ECB  74 30                           je 0x140809efd
00809ECD  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00809ED5  44 8B 08                        mov r9d, dword ptr [rax]
00809ED8  41 C1 E9 02                     shr r9d, 2
00809EDC  41 83 E1 01                     and r9d, 1
00809EE0  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00809EE5  45 8B C4                        mov r8d, r12d
00809EE8  49 8B D3                        mov rdx, r11
00809EEB  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00809EF3  E8 90 3A 2C 00                  call 0x140acd988
00809EF8  E9 44 02 00 00                  jmp 0x14080a141
00809EFD  4D 85 C0                        test r8, r8
00809F00  0F 84 90 00 00 00               je 0x140809f96
00809F06  8B C7                           mov eax, edi
00809F08  24 90                           and al, 0x90
00809F0A  3C 80                           cmp al, 0x80
00809F0C  0F 85 84 00 00 00               jne 0x140809f96
00809F12  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00809F1A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00809F1F  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00809F27  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00809F2C  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00809F31  45 8B C6                        mov r8d, r14d
00809F34  49 8B D2                        mov rdx, r10
00809F37  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00809F3F  E8 58 F7 FF FF                  call 0x14080969c
00809F44  44 8B E8                        mov r13d, eax
00809F47  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00809F4B  85 C0                           test eax, eax
00809F4D  79 22                           jns 0x140809f71
00809F4F  3D 2D 01 00 C0                  cmp eax, 0xc000012d
00809F54  0F 84 54 04 00 00               je 0x14080a3ae
00809F5A  81 E7 3F FF FF FF               and edi, 0xffffff3f
00809F60  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00809F64  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00809F6C  E9 21 04 00 00                  jmp 0x14080a392
00809F71  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
00809F79  49 8B C8                        mov rcx, r8
00809F7C  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00809F81  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
00809F86  4C 8B 9C 24 B8 00 00 00         mov r11, qword ptr [rsp + 0xb8]
00809F8E  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
00809F96  48 85 C9                        test rcx, rcx
00809F99  0F 85 B3 01 00 00               jne 0x14080a152
00809F9F  49 83 FB 10                     cmp r11, 0x10
00809FA3  0F 82 30 01 00 00               jb 0x14080a0d9
00809FA9  40 F6 C7 10                     test dil, 0x10
00809FAD  0F 85 26 01 00 00               jne 0x14080a0d9
00809FB3  48 81 FE 00 10 00 00            cmp rsi, 0x1000
00809FBA  75 29                           jne 0x140809fe5
00809FBC  8B CB                           mov ecx, ebx
00809FBE  83 F9 03                        cmp ecx, 3
00809FC1  73 22                           jae 0x140809fe5
00809FC3  8B C1                           mov eax, ecx
00809FC5  48 8D 15 94 7C 80 FF            lea rdx, [rip - 0x7f836c]
00809FCC  48 8B 14 C2                     mov rdx, qword ptr [rdx + rax*8]
00809FD0  4C 3B DA                        cmp r11, rdx
00809FD3  72 05                           jb 0x140809fda
00809FD5  4C 3B CA                        cmp r9, rdx
00809FD8  73 04                           jae 0x140809fde
00809FDA  FF C1                           inc ecx
00809FDC  EB E0                           jmp 0x140809fbe
00809FDE  48 8B F2                        mov rsi, rdx
00809FE1  48 C1 E6 0C                     shl rsi, 0xc
00809FE5  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00809FE9  83 C8 42                        or eax, 0x42
00809FEC  49 8B CB                        mov rcx, r11
00809FEF  48 C1 E1 0C                     shl rcx, 0xc
00809FF3  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
00809FF8  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0080A000  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0080A005  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0080A009  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0080A00E  41 8B 42 34                     mov eax, dword ptr [r10 + 0x34]
0080A012  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0080A016  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0080A01B  4C 8B CE                        mov r9, rsi
0080A01E  4D 8D 87 00 F0 FF FF            lea r8, [r15 - 0x1000]
0080A025  48 8B D3                        mov rdx, rbx
0080A028  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0080A030  E8 B7 0B BE FF                  call 0x1403eabec
0080A035  48 8B C8                        mov rcx, rax
0080A038  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0080A03D  48 85 C0                        test rax, rax
0080A040  0F 85 93 00 00 00               jne 0x14080a0d9
0080A046  8B D3                           mov edx, ebx
0080A048  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
0080A050  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0080A058  83 FA 01                        cmp edx, 1
0080A05B  77 60                           ja 0x14080a0bd
0080A05D  48 3B B4 24 00 01 00 00         cmp rsi, qword ptr [rsp + 0x100]
0080A065  7E 27                           jle 0x14080a08e
0080A067  8B C2                           mov eax, edx
0080A069  4C 8D 15 F0 7B 80 FF            lea r10, [rip - 0x7f8410]
0080A070  49 8B 0C C2                     mov rcx, qword ptr [r10 + rax*8]
0080A074  48 C1 E1 0C                     shl rcx, 0xc
0080A078  48 3B F1                        cmp rsi, rcx
0080A07B  75 11                           jne 0x14080a08e
0080A07D  8D 42 01                        lea eax, [rdx + 1]
0080A080  49 8B 04 C2                     mov rax, qword ptr [r10 + rax*8]
0080A084  4C 3B C0                        cmp r8, rax
0080A087  72 05                           jb 0x14080a08e
0080A089  4C 3B C8                        cmp r9, rax
0080A08C  73 04                           jae 0x14080a092
0080A08E  FF C2                           inc edx
0080A090  EB C6                           jmp 0x14080a058
0080A092  85 D2                           test edx, edx
0080A094  75 12                           jne 0x14080a0a8
0080A096  F7 44 24 54 00 00 00 02         test dword ptr [rsp + 0x54], 0x2000000
0080A09E  74 24                           je 0x14080a0c4
0080A0A0  83 CF 10                        or edi, 0x10
0080A0A3  E9 B8 FE FF FF                  jmp 0x140809f60
0080A0A8  83 FA 01                        cmp edx, 1
0080A0AB  75 1A                           jne 0x14080a0c7
0080A0AD  F7 44 24 54 00 00 00 01         test dword ptr [rsp + 0x54], 0x1000000
0080A0B5  8D 42 01                        lea eax, [rdx + 1]
0080A0B8  0F 45 D0                        cmovne edx, eax
0080A0BB  EB 07                           jmp 0x14080a0c4
0080A0BD  4C 8D 15 9C 7B 80 FF            lea r10, [rip - 0x7f8464]
0080A0C4  83 FA 01                        cmp edx, 1
0080A0C7  77 D7                           ja 0x14080a0a0
0080A0C9  8D 42 01                        lea eax, [rdx + 1]
0080A0CC  49 8B 34 C2                     mov rsi, qword ptr [r10 + rax*8]
0080A0D0  48 C1 E6 0C                     shl rsi, 0xc
0080A0D4  E9 8B FE FF FF                  jmp 0x140809f64
0080A0D9  48 85 C9                        test rcx, rcx
0080A0DC  75 74                           jne 0x14080a152
0080A0DE  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
0080A0E6  49 C1 E0 0C                     shl r8, 0xc
0080A0EA  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0080A0F2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0080A0F7  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0080A0FF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0080A104  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0080A108  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0080A10C  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0080A111  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0080A116  8B 40 34                        mov eax, dword ptr [rax + 0x34]
0080A119  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0080A11D  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0080A122  4C 8B 8C 24 00 01 00 00         mov r9, qword ptr [rsp + 0x100]
0080A12A  4D 8D 87 00 F0 FF FF            lea r8, [r15 - 0x1000]
0080A131  48 8B D3                        mov rdx, rbx
0080A134  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0080A13C  E8 AB 0A BE FF                  call 0x1403eabec
0080A141  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0080A146  48 8B C8                        mov rcx, rax
0080A149  48 85 C0                        test rax, rax
0080A14C  0F 84 34 03 00 00               je 0x14080a486
0080A152  48 8D 51 30                     lea rdx, [rcx + 0x30]
0080A156  48 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdx
0080A15E  8B 49 28                        mov ecx, dword ptr [rcx + 0x28]
0080A161  48 C1 E9 0C                     shr rcx, 0xc
0080A165  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
0080A16D  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
0080A175  48 8B C3                        mov rax, rbx
0080A178  4C 8D 04 CA                     lea r8, [rdx + rcx*8]
0080A17C  48 8B 0A                        mov rcx, qword ptr [rdx]
0080A17F  48 3B C8                        cmp rcx, rax
0080A182  48 0F 46 C8                     cmovbe rcx, rax
0080A186  48 8B C1                        mov rax, rcx
0080A189  48 83 C2 08                     add rdx, 8
0080A18D  49 3B D0                        cmp rdx, r8
0080A190  75 EA                           jne 0x14080a17c
0080A192  33 D2                           xor edx, edx
0080A194  48 F7 B4 24 C0 00 00 00         div qword ptr [rsp + 0xc0]
0080A19C  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0080A1A4  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
0080A1AC  75 23                           jne 0x14080a1d1
0080A1AE  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0080A1B3  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0080A1B8  E8 7F E9 A9 FF                  call 0x1402a8b3c
0080A1BD  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0080A1C2  8B 88 F4 01 00 00               mov ecx, dword ptr [rax + 0x1f4]
0080A1C8  F6 C1 20                        test cl, 0x20
0080A1CB  0F 85 3A 02 00 00               jne 0x14080a40b
0080A1D1  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0080A1D6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080A1DB  E8 4C FB CA FF                  call 0x1404b9d2c
0080A1E0  4C 8B C8                        mov r9, rax
0080A1E3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0080A1E8  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0080A1EC  48 39 8C 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rcx
0080A1F4  72 5F                           jb 0x14080a255
0080A1F6  49 8B D1                        mov rdx, r9
0080A1F9  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0080A1FE  49 8B CD                        mov rcx, r13
0080A201  E8 BE C4 CB FF                  call 0x1404c66c4
0080A206  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
0080A20E  75 0D                           jne 0x14080a21d
0080A210  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0080A215  49 8B CD                        mov rcx, r13
0080A218  E8 AF E8 A9 FF                  call 0x1402a8acc
0080A21D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080A222  E8 D9 0A 00 00                  call 0x14080ad00
0080A227  44 8B E8                        mov r13d, eax
0080A22A  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0080A22E  85 C0                           test eax, eax
0080A230  79 17                           jns 0x14080a249
0080A232  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0080A237  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0080A23F  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0080A243  0F 83 0D 02 00 00               jae 0x14080a456
0080A249  44 8B EB                        mov r13d, ebx
0080A24C  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
0080A250  E9 4F FF FF FF                  jmp 0x14080a1a4
0080A255  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
0080A259  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
0080A261  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0080A269  4C 8D 14 C1                     lea r10, [rcx + rax*8]
0080A26D  48 8B 01                        mov rax, qword ptr [rcx]
0080A270  33 D2                           xor edx, edx
0080A272  48 F7 B4 24 C0 00 00 00         div qword ptr [rsp + 0xc0]
0080A27A  48 8B D0                        mov rdx, rax
0080A27D  48 C1 EA 05                     shr rdx, 5
0080A281  8A C8                           mov cl, al
0080A283  80 E1 1F                        and cl, 0x1f
0080A286  B8 01 00 00 00                  mov eax, 1
0080A28B  D3 E0                           shl eax, cl
0080A28D  F0 41 09 04 90                  lock or dword ptr [r8 + rdx*4], eax
0080A292  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0080A29A  48 83 C1 08                     add rcx, 8
0080A29E  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0080A2A6  49 3B CA                        cmp rcx, r10
0080A2A9  75 C2                           jne 0x14080a26d
0080A2AB  49 8B D1                        mov rdx, r9
0080A2AE  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0080A2B3  E8 0C C4 CB FF                  call 0x1404c66c4
0080A2B8  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0080A2C0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0080A2C5  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
0080A2CD  75 0D                           jne 0x14080a2dc
0080A2CF  48 8B D0                        mov rdx, rax
0080A2D2  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0080A2D7  E8 F0 E7 A9 FF                  call 0x1402a8acc
0080A2DC  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0080A2E1  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
0080A2E9  48 89 08                        mov qword ptr [rax], rcx
0080A2EC  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0080A2F4  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
0080A2FC  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
0080A304  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0080A30C  4D 0F AF C1                     imul r8, r9
0080A310  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
0080A318  40 F6 C7 20                     test dil, 0x20
0080A31C  75 5C                           jne 0x14080a37a
0080A31E  4C 8B 94 24 D0 00 00 00         mov r10, qword ptr [rsp + 0xd0]
0080A326  F0 4D 01 82 A8 4C 00 00         lock add qword ptr [r10 + 0x4ca8], r8
0080A32E  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0080A336  E8 D5 97 C3 FF                  call 0x140443b10
0080A33B  49 3B C2                        cmp rax, r10
0080A33E  74 2D                           je 0x14080a36d
0080A340  BA 04 00 00 00                  mov edx, 4
0080A345  49 83 F9 01                     cmp r9, 1
0080A349  8D 42 FE                        lea eax, [rdx - 2]
0080A34C  0F 45 D0                        cmovne edx, eax
0080A34F  4D 8B C8                        mov r9, r8
0080A352  44 8D 40 FF                     lea r8d, [rax - 1]
0080A356  49 8B CA                        mov rcx, r10
0080A359  E8 9E B8 B1 FF                  call 0x140325bfc
0080A35E  44 8B E8                        mov r13d, eax
0080A361  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0080A365  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
0080A36D  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0080A375  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0080A37A  4C 01 84 24 90 00 00 00         add qword ptr [rsp + 0x90], r8
0080A382  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0080A38A  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0080A392  48 39 84 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rax
0080A39A  74 1D                           je 0x14080a3b9
0080A39C  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
0080A3A1  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0080A3A9  E9 62 FA FF FF                  jmp 0x140809e10
0080A3AE  41 BD 9A 00 00 C0               mov r13d, 0xc000009a
0080A3B4  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
0080A3B9  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0080A3BE  4C 8B B4 24 90 00 00 00         mov r14, qword ptr [rsp + 0x90]
0080A3C6  40 F6 C7 01                     test dil, 1
0080A3CA  74 16                           je 0x14080a3e2
0080A3CC  33 D2                           xor edx, edx
0080A3CE  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
0080A3D6  E8 55 D9 A0 FF                  call 0x140217d30
0080A3DB  83 E7 FE                        and edi, 0xfffffffe
0080A3DE  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
0080A3E2  45 85 ED                        test r13d, r13d
0080A3E5  0F 88 C4 00 00 00               js 0x14080a4af
0080A3EB  33 D2                           xor edx, edx
0080A3ED  49 8B C6                        mov rax, r14
0080A3F0  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
0080A3F8  49 F7 F6                        div r14
0080A3FB  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
0080A403  48 89 01                        mov qword ptr [rcx], rax
0080A406  E9 AC 00 00 00                  jmp 0x14080a4b7
0080A40B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0080A410  48 8B D6                        mov rdx, rsi
0080A413  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0080A418  E8 AF E6 A9 FF                  call 0x1402a8acc
0080A41D  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0080A422  49 8B D6                        mov rdx, r14
0080A425  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0080A42A  E8 55 E5 E7 FF                  call 0x140688984
0080A42F  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
0080A437  4C 3B F0                        cmp r14, rax
0080A43A  74 0A                           je 0x14080a446
0080A43C  33 D2                           xor edx, edx
0080A43E  49 8B CE                        mov rcx, r14
0080A441  E8 2A 84 37 00                  call 0x140b82870
0080A446  41 BD 0A 01 00 C0               mov r13d, 0xc000010a
0080A44C  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
0080A451  E9 68 FF FF FF                  jmp 0x14080a3be
0080A456  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0080A45B  49 8B D6                        mov rdx, r14
0080A45E  48 8B C8                        mov rcx, rax
0080A461  E8 1E E5 E7 FF                  call 0x140688984
0080A466  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
0080A46E  4C 3B F0                        cmp r14, rax
0080A471  0F 84 42 FF FF FF               je 0x14080a3b9
0080A477  33 D2                           xor edx, edx
0080A479  49 8B CE                        mov rcx, r14
0080A47C  E8 EF 83 37 00                  call 0x140b82870
0080A481  E9 33 FF FF FF                  jmp 0x14080a3b9
0080A486  41 8B C5                        mov eax, r13d
0080A489  41 BD 9A 00 00 C0               mov r13d, 0xc000009a
0080A48F  4C 8B B4 24 90 00 00 00         mov r14, qword ptr [rsp + 0x90]
0080A497  4D 85 F6                        test r14, r14
0080A49A  41 0F 44 C5                     cmove eax, r13d
0080A49E  44 8B E8                        mov r13d, eax
0080A4A1  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0080A4A5  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0080A4AA  E9 17 FF FF FF                  jmp 0x14080a3c6
0080A4AF  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
0080A4B7  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
0080A4BF  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0080A4C4  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
0080A4CC  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0080A4D4  48 85 C9                        test rcx, rcx
0080A4D7  74 5E                           je 0x14080a537
0080A4D9  4C 8D 59 30                     lea r11, [rcx + 0x30]
0080A4DD  4C 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r11
0080A4E5  44 8B 49 28                     mov r9d, dword ptr [rcx + 0x28]
0080A4E9  49 C1 E9 0C                     shr r9, 0xc
0080A4ED  4C 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], r9
0080A4F5  4C 8B C3                        mov r8, rbx
0080A4F8  48 89 9C 24 28 01 00 00         mov qword ptr [rsp + 0x128], rbx
0080A500  4D 3B C1                        cmp r8, r9
0080A503  73 28                           jae 0x14080a52d
0080A505  4B 8B 04 C3                     mov rax, qword ptr [r11 + r8*8]
0080A509  49 89 02                        mov qword ptr [r10], rax
0080A50C  49 83 C2 08                     add r10, 8
0080A510  4C 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r10
0080A518  33 D2                           xor edx, edx
0080A51A  49 8B C6                        mov rax, r14
0080A51D  49 F7 F7                        div r15
0080A520  4C 03 C0                        add r8, rax
0080A523  4C 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], r8
0080A52B  EB D3                           jmp 0x14080a500
0080A52D  48 8B 09                        mov rcx, qword ptr [rcx]
0080A530  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0080A535  EB 9D                           jmp 0x14080a4d4
0080A537  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
0080A53F  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
0080A547  EB 21                           jmp 0x14080a56a
0080A549  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0080A551  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
0080A556  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
0080A55E  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0080A566  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
0080A56A  48 85 C0                        test rax, rax
0080A56D  EB 20                           jmp 0x14080a58f
0080A56F  4C 8B 38                        mov r15, qword ptr [rax]
0080A572  48 8D 8C 24 C0 01 00 00         lea rcx, [rsp + 0x1c0]
0080A57A  48 3B C1                        cmp rax, rcx
0080A57D  74 0A                           je 0x14080a589
0080A57F  33 D2                           xor edx, edx
0080A581  48 8B C8                        mov rcx, rax
0080A584  E8 E7 82 37 00                  call 0x140b82870
0080A589  49 8B C7                        mov rax, r15
0080A58C  4D 85 FF                        test r15, r15
0080A58F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0080A594  75 D9                           jne 0x14080a56f
0080A596  4C 2B B4 24 90 00 00 00         sub r14, qword ptr [rsp + 0x90]
0080A59E  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
0080A5A6  EB 06                           jmp 0x14080a5ae
0080A5A8  41 BD 0D 00 00 C0               mov r13d, 0xc000000d
0080A5AE  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0080A5B3  4D 85 F6                        test r14, r14
0080A5B6  74 40                           je 0x14080a5f8
0080A5B8  40 F6 C7 02                     test dil, 2
0080A5BC  74 21                           je 0x14080a5df
0080A5BE  48 8B D6                        mov rdx, rsi
0080A5C1  49 8B CC                        mov rcx, r12
0080A5C4  E8 73 E5 A9 FF                  call 0x1402a8b3c
0080A5C9  49 8B D6                        mov rdx, r14
0080A5CC  48 8B CE                        mov rcx, rsi
0080A5CF  E8 00 29 C5 FF                  call 0x14045ced4
0080A5D4  48 8B D6                        mov rdx, rsi
0080A5D7  49 8B CC                        mov rcx, r12
0080A5DA  E8 ED E4 A9 FF                  call 0x1402a8acc
0080A5DF  40 F6 C7 04                     test dil, 4
0080A5E3  74 13                           je 0x14080a5f8
0080A5E5  49 F7 DE                        neg r14
0080A5E8  F0 4C 01 B6 70 05 00 00         lock add qword ptr [rsi + 0x570], r14
0080A5F0  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0080A5F8  40 F6 C7 01                     test dil, 1
0080A5FC  74 0F                           je 0x14080a60d
0080A5FE  33 D2                           xor edx, edx
0080A600  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
0080A608  E8 23 D7 A0 FF                  call 0x140217d30
0080A60D  40 F6 C7 08                     test dil, 8
0080A611  75 1A                           jne 0x14080a62d
0080A613  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0080A61B  BA 4D 6D 50 68                  mov edx, 0x68506d4d
0080A620  48 85 C9                        test rcx, rcx
0080A623  75 03                           jne 0x14080a628
0080A625  48 8B CE                        mov rcx, rsi
0080A628  E8 B3 D2 AE FF                  call 0x1402f78e0
0080A62D  41 8B C5                        mov eax, r13d
0080A630  EB 07                           jmp 0x14080a639
0080A632  EB 05                           jmp 0x14080a639
0080A634  B8 0D 00 00 C0                  mov eax, 0xc000000d
0080A639  48 8B 8C 24 F0 02 00 00         mov rcx, qword ptr [rsp + 0x2f0]
0080A641  48 33 CC                        xor rcx, rsp
0080A644  E8 F7 1F EA FF                  call 0x1406ac640
0080A649  48 81 C4 00 03 00 00            add rsp, 0x300
0080A650  41 5F                           pop r15
0080A652  41 5E                           pop r14
0080A654  41 5D                           pop r13
0080A656  41 5C                           pop r12
0080A658  5F                              pop rdi
0080A659  5E                              pop rsi
0080A65A  5B                              pop rbx
0080A65B  C3                              ret
0080A65C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateUserPhysicalPages(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int16 v_stack_m16E;
    unsigned __int16 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C7;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned int v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned int v_stack_m2E4;
    unsigned int v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned int v_stack_m300;
    unsigned int v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (768);
    result = (*(unsigned __int64 *)(v_rip + 6295292)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m218 = a2;
    *(unsigned __int64 *)(v_rsp - 584) = a3;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 648) = 0;
    *(unsigned __int64 *)(v_rsp - 696) = 0;
    a2 = 0;
    result = memset(v_rsp - 376, a2, 304, a4);
    a2 = 0;
    result = memset(v_stack_m1F8, a2, v_rbx + 72, a4);
    v_stack_m2E8 = 0;
    v_stack_m2C8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m260 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m318 = v_stack_m1F8;
    result = MiCaptureAllocateMapExtendedParameters(a4, (unsigned int)(a5), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rbx + 36);
    if (sign_flag) goto loc_0080A639;
    if (((v_stack_m1C0) & (-27)) != 0) goto loc_0080A634;
    result = (unsigned int)((v_stack_m1C0) & (26));
    if (condition_is_equal) goto loc_00809935;
    result = (unsigned __int8)((result) + (255));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_stack_m1C0)));
    result = 0;
    if ((((unsigned __int8)(result)) & (26)) == 0) {
        result = 1;
    }
    if ((unsigned int)(result) == 0) goto loc_0080A634;
    if (((2) & ((unsigned __int8)(v_stack_m1C0))) == 0) goto loc_00809959;
    v_stack_m2B0 = 16;
    goto loc_0080999A;
loc_00809959:
    if ((((unsigned __int8)(v_stack_m1C0)) & (8)) == 0) goto loc_0080996C;
    v_stack_m2B0 = 512;
    goto loc_0080999A;
loc_0080996C:
    if ((((unsigned __int8)(v_stack_m1C0)) & (16)) == 0) goto loc_00809992;
    result = MiHugePagesSupported(v_stack_m1C0, 2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rbx + 36);
    if ((unsigned int)(result) != 0) goto loc_00809984;
    goto loc_0080A639;
loc_00809984:
    v_stack_m2B0 = 0x40000ULL;
    goto loc_0080999A;
loc_00809992:
    v_stack_m2B0 = 0;
loc_0080999A:
    if (v_stack_m1D8 > ((unsigned int)(*(unsigned __int16 *)(v_rip + 8107615)))) goto loc_0080A634;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008099D2;
    v_stack_m2A0 = *(unsigned __int64 *)(a2);
    v_stack_m290 = *(unsigned __int64 *)(a2);
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00809A41;
    result = 0;
    goto loc_0080A639;
loc_008099D2:
    a1 = v_stack_m1C0;
    if ((*(unsigned __int64 *)(a2)) < v_stack_m1C0) { a1 = *(unsigned __int64 *)(a2); }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    v_stack_m2A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2));
    v_stack_m290 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) != 0) goto loc_00809A08;
    result = 0;
    goto loc_0080A639;
loc_00809A08:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) <= 0) goto loc_00809A21;
    goto loc_0080A639;
loc_00809A21:
    result = ProbeForWrite(v_stack_m248, *(unsigned __int64 *)(*(unsigned __int64 *)(a2)) * 8, 8, v_rbx + 36);
loc_00809A41:
    v_stack_m2D0 = 0;
    v_stack_m318 = v_stack_m288;
    result = MiReferenceAweHandle(a1, 2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m2B8);
    if (sign_flag) goto loc_0080A639;
    if (v_stack_m288 == 0) goto loc_00809A96;
    result = MiSectionControlArea(v_stack_m288, 2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m2B8);
    v_stack_m2D0 = *(unsigned __int64 *)(result + 8);
    goto loc_00809AB7;
loc_00809A96:
    v_stack_m2E0 = v_stack_m2B8;
    if (v_stack_m2B8 != 0) goto loc_00809AC7;
    v_stack_m2E8 = (unsigned int)(v_stack_m2B8 + 8);
loc_00809AB7:
    v_stack_m2B8 = v_stack_m260;
    v_stack_m2E0 = v_stack_m260;
loc_00809AC7:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8191999), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m2B8);
    if ((unsigned __int8)(result) != 0) goto loc_00809AE5;
    goto loc_0080A5AE;
loc_00809AE5:
    v_rdi = v_stack_m2B8 + 8;
    if (v_stack_m260 != ((unsigned int)(0xC0000061ULL))) {
        a3 = v_stack_m1A8;
        a2 = 0;
        a1 = v_stack_m260;
        result = KiStackAttachProcess(a1, a2, a3, v_stack_m2B8);
        v_rdi = (unsigned int)((v_stack_m2B8 + 8) | (1));
        v_stack_m2E8 = (unsigned int)(v_rdi);
    }
    v_stack_m2A8 = 0;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00809B1A;
    v_stack_m270 = *(unsigned __int64 *)(result + 8);
    goto loc_00809B3F;
loc_00809B1A:
    result = MiCreateProcessDefaultAweInfo((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m2D0, a3, v_stack_m2B8);
    if (sign_flag) goto loc_0080A5AE;
    v_stack_m270 = v_stack_m260;
loc_00809B3F:
    result = MiGetAwePageSize(v_stack_m2D0, v_stack_m2D0, a3, v_stack_m2B8);
    v_stack_m278 = result;
    if (result != 16) goto loc_00809B62;
    v_stack_m2E4 = 0x1000ULL;
    goto loc_00809B8A;
loc_00809B62:
    if (result != 512) goto loc_00809B75;
    v_stack_m2E4 = 0x1000000ULL;
    goto loc_00809B8A;
loc_00809B75:
    result = 0;
    if (result == 0x40000ULL) { result = (unsigned int)((unsigned int)(0x2000000ULL)); }
    v_stack_m2E4 = (unsigned int)(result);
loc_00809B8A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m2D0 + 8)))) & (8)) != 0) {
        v_rdi = (unsigned int)((v_rdi) | (32));
        v_stack_m2E8 = (unsigned int)(v_rdi);
    }
    if (v_stack_m2B0 != 0) goto loc_00809BB3;
    v_stack_m2B0 = result;
    goto loc_00809BDA;
loc_00809BB3:
    if (result <= result) goto loc_0080A5A8;
    a2 = 0;
    if (0 != 0) goto loc_0080A5A8;
    if (((result) & (result - 1)) != 0) goto loc_0080A5A8;
loc_00809BDA:
    if (result <= 1) goto loc_00809C0A;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) * (result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) < result) goto loc_00809BF7;
    goto loc_0080A5AE;
loc_00809BF7:
    v_stack_m2A0 = result;
    v_stack_m290 = result;
loc_00809C0A:
    if (v_stack_m288 != 0) goto loc_00809C8F;
    result = LOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, a3, result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m260 + 500)))) & (32)) == 0) goto loc_00809C44;
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, a3, result);
    goto loc_0080A5B3;
loc_00809C44:
    result = MiChargeProcessPhysicalPages(v_stack_m260, result, a3, result);
    if ((unsigned int)(result) != 0) goto loc_00809C69;
loc_00809C59:
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, a3, result);
    goto loc_0080A5B3;
loc_00809C69:
    v_rdi = (unsigned int)((v_rdi) | (4));
    result = MiChargeProcessCommitment(v_stack_m2C8, v_stack_m260, a3, result);
    if ((unsigned int)(result) == 0) goto loc_00809C59;
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, a3, result);
    v_rdi = (unsigned int)((v_rdi) | (2));
    v_stack_m2E8 = (unsigned int)(v_rdi);
loc_00809C8F:
    result = MiGetAweInfoPartition(v_stack_m2D0, v_stack_m260, a3, v_stack_m2B0);
    v_stack_m268 = result;
    a2 = (*(unsigned __int64 *)(result + 18504)) + 1;
    v_stack_m240 = a2;
    v_stack_m250 = 0;
    v_stack_m228 = 0;
    if ((*(unsigned __int64 *)(v_stack_m260 + 784)) == 0) goto loc_00809D09;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m260 + 1772))) == 332) goto loc_00809CEA;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m260 + 1772))) == 452) {
        result = 1;
    }
    if ((unsigned __int8)(result) != 0) {
        if (a2 > result) { a2 = result; }
        v_stack_m240 = a2;
    }
    v_r15 = (a2) << (12);
    v_stack_m2D8 = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_m2E4)) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((unsigned int)((unsigned int)(v_stack_m1D8)) == 0) goto loc_00809D44;
    if ((unsigned __int8)(v_stack_m1C7) == 0) goto loc_00809D57;
    a3 = (unsigned int)((a3) | (2));
    goto loc_00809D57;
loc_00809D44:
    result = KeGetIdealNodeNumberThread(v_stack_m2C8, (unsigned int)(0x80000000ULL), a3, v_stack_m2B0);
loc_00809D57:
    v_r12 = (unsigned int)((unsigned int)((unsigned __int16)(result)));
    if ((unsigned __int8)(v_stack_m1C7) == 0) {
        v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(result)))) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m2D0 + 8)))) & (4)) != 0) {
        a3 = (unsigned int)((a3) | (1));
    }
    v_rsi = (v_stack_m2B0) << (12);
    result = 0;
    if (v_stack_m2B0 != 1) { result = v_rsi; }
    v_stack_m238 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) | (48));
    if (v_stack_m2B0 != 1) { a3 = (unsigned int)(result); }
    v_stack_m2E4 = (unsigned int)(a3);
    result = MiGetProcessPartition(v_stack_m2E0, (unsigned int)(0x80000000ULL), a3, v_stack_m2B0);
    if (result != result) goto loc_00809DFC;
    a1 = (result < result) ? 1 : 0;
    result = ((((unsigned __int8)(v_rdi)) & (32)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00809DFC;
    if (v_stack_m2B0 != 16) goto loc_00809DFC;
    v_stack_m2E0 = v_stack_m2B8;
    v_stack_m2A0 = v_stack_m290;
    if ((((unsigned __int8)(v_stack_m2B0)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4))))) != 0) goto loc_00809E04;
    v_stack_m2E8 = (unsigned int)(v_rdi);
    goto loc_00809E04;
loc_00809DFC:
loc_00809E04:
    v_stack_m220 = v_stack_m2D0 + 8;
loc_00809E10:
    v_stack_m2C0 = 0;
    v_r11 = (v_stack_m2A0) - (v_stack_m2A8);
    v_stack_m280 = v_r11;
    if (v_stack_m278 == 1) {
        if (v_r11 > ((unsigned int)(0xC0000ULL))) { v_r11 = (unsigned int)(0xC0000ULL); }
        v_stack_m280 = v_r11;
    }
    if ((((unsigned __int8)(v_rdi)) & (64)) != 0) goto loc_00809EBC;
    a2 = 0;
    if (v_r11 > 32) goto loc_00809EBC;
    v_rdi = (unsigned int)((v_rdi) | (64));
    v_stack_m2E8 = (unsigned int)(v_rdi);
    result = (v_r11) << (12);
    v_stack_m178 = 0;
    a1 = (result + 4095) >> (12);
    a1 = (unsigned __int16)((a1) + (6));
    a1 = (unsigned __int16)((a1) << (3));
    v_stack_m170 = (unsigned __int16)(a1);
    v_stack_m16E = 0;
    v_stack_m158 = 0;
    v_stack_m14C = 0;
    v_stack_m150 = (unsigned int)(result);
    goto loc_00809EBF;
loc_00809EBC:
loc_00809EBF:
    v_stack_m298 = 0;
    if ((((unsigned __int8)(v_rdi)) & (32)) == 0) goto loc_00809EFD;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m220))) >> (2));
    a4 = (unsigned int)((a4) & (1));
    v_stack_m318 = 0;
    result = MiAllocateUserPhysicalRanges(v_stack_m268, v_r11, (unsigned int)((unsigned int)(v_r12)), a4);
    goto loc_0080A141;
loc_00809EFD:
    if ((unsigned int)((unsigned int)(v_r12)) == 0) goto loc_00809F96;
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rdi))) & (144));
    if (((unsigned __int8)(result)) != 128) goto loc_00809F96;
    v_stack_m310 = v_stack_m270;
    v_stack_m318 = v_stack_m240;
    result = MiAllocateFastAwePages(v_stack_m298, v_stack_m2D0, (unsigned int)((unsigned int)((unsigned __int16)(result))), (unsigned int)(v_stack_m2E4));
    v_stack_m2D8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00809F71;
    if (((unsigned int)(result)) == 0xC000012DULL) goto loc_0080A3AE;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFF3FULL));
loc_00809F60:
    v_stack_m2E8 = (unsigned int)(v_rdi);
loc_00809F64:
    goto loc_0080A392;
loc_00809F71:
    v_stack_m2C0 = v_stack_m298;
loc_00809F96:
    if (v_stack_m298 != 0) goto loc_0080A152;
    if (v_stack_m280 < 16) goto loc_0080A0D9;
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_0080A0D9;
    if (v_rsi != 0x1000ULL) goto loc_00809FE5;
loc_00809FBE:
    if (0 >= 3) goto loc_00809FE5;
    if (v_stack_m280 < (*(unsigned __int64 *)(v_rip - 8356716 + 0 * 8))) goto loc_00809FDA;
    if (v_stack_m2B0 >= (*(unsigned __int64 *)(v_rip - 8356716 + 0 * 8))) goto loc_00809FDE;
loc_00809FDA:
    a1 = (unsigned int)((0) + 1);
    goto loc_00809FBE;
loc_00809FDE:
    v_rsi = (*(unsigned __int64 *)(v_rip - 8356716 + 0 * 8)) << (12);
loc_00809FE5:
    result = (unsigned int)(((unsigned int)(v_stack_m2E4)) | (66));
    a1 = (v_stack_m280) << (12);
    v_stack_m2F0 = v_stack_m298;
    v_stack_m2F8 = v_stack_m270;
    v_stack_m300 = (unsigned int)(result);
    v_stack_m308 = (unsigned int)((unsigned __int16)(result));
    v_stack_m310 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2D0 + 52)));
    v_stack_m318 = a1;
    result = MiAllocatePagesForMdl(v_stack_m268, 0, v_r15 - 4096, v_rsi);
    v_stack_m2C0 = result;
    if (result != 0) goto loc_0080A0D9;
loc_0080A058:
    if (0 > 1) goto loc_0080A0BD;
    if (v_rsi <= v_stack_m238) goto loc_0080A08E;
    a1 = (*(unsigned __int64 *)(v_rip - 8356880 + 0 * 8)) << (12);
    if (v_rsi != a1) goto loc_0080A08E;
    if (v_stack_m280 < (*(unsigned __int64 *)(v_rip - 8356880 + 0 + 1 * 8))) goto loc_0080A08E;
    if (v_stack_m2B0 >= (*(unsigned __int64 *)(v_rip - 8356880 + 0 + 1 * 8))) goto loc_0080A092;
loc_0080A08E:
    a2 = (unsigned int)((0) + 1);
    goto loc_0080A058;
loc_0080A092:
    if ((unsigned int)(a2) != 0) goto loc_0080A0A8;
    if (((v_stack_m2E4) & (0x2000000ULL)) == 0) goto loc_0080A0C4;
loc_0080A0A0:
    v_rdi = (unsigned int)((v_rdi) | (16));
    goto loc_00809F60;
loc_0080A0A8:
    if (((unsigned int)(a2)) != 1) goto loc_0080A0C7;
    if (((v_stack_m2E4) & (0x1000000ULL)) != 0) { a2 = (unsigned int)(a2 + 1); }
    goto loc_0080A0C4;
loc_0080A0BD:
loc_0080A0C4:
loc_0080A0C7:
    if (((unsigned int)(a2)) > 1) goto loc_0080A0A0;
    v_rsi = (*(unsigned __int64 *)(v_rip - 8356964 + a2 + 1 * 8)) << (12);
    goto loc_00809F64;
loc_0080A0D9:
    if (a1 != 0) goto loc_0080A152;
    a3 = (v_stack_m280) << (12);
    v_stack_m2F0 = v_stack_m298;
    v_stack_m2F8 = v_stack_m270;
    v_stack_m300 = (unsigned int)((unsigned int)(v_stack_m2E4));
    v_stack_m308 = (unsigned int)((unsigned __int16)(result));
    v_stack_m310 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2D0 + 52)));
    v_stack_m318 = a3;
    result = MiAllocatePagesForMdl(v_stack_m268, 0, v_r15 - 4096, v_stack_m238);
loc_0080A141:
    v_stack_m2C0 = result;
    if (result == 0) goto loc_0080A486;
loc_0080A152:
    v_stack_m258 = result + 48;
    a1 = ((unsigned int)(*(unsigned int *)(result + 40))) >> (12);
    v_stack_m280 = a1;
    v_stack_m230 = a1;
loc_0080A17C:
    a1 = *(unsigned __int64 *)(result + 48);
    if ((*(unsigned __int64 *)(result + 48)) <= 0) { a1 = 0; }
    a2 = (result + 48) + (8);
    if (a2 != (result + 48 + a1 * 8)) goto loc_0080A17C;
    a2 = 0;
    v_stack_m298 = a1;
loc_0080A1A4:
    if (v_stack_m288 != 0) goto loc_0080A1D1;
    result = LOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m2E0, result + 48 + a1 * 8, v_stack_m238);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m2E0 + 500)))) & (32)) != 0) goto loc_0080A40B;
loc_0080A1D1:
    result = MiLockAwePagesShared(v_stack_m2D0, v_stack_m2C8, result + 48 + a1 * 8, v_stack_m238);
    if (v_stack_m298 < (*(unsigned __int64 *)(v_stack_m2D0 + 24))) goto loc_0080A255;
    result = MiUnlockAwePagesShared(v_stack_m2C8, result, result + 48 + a1 * 8, result);
    if (v_stack_m288 == 0) {
        a2 = v_stack_m2E0;
        a1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(a1, a2, result + 48 + a1 * 8, result);
    }
    result = MiResizeAweBitMap(v_stack_m2D0, a2, result + 48 + a1 * 8, result);
    v_stack_m2D8 = (unsigned int)(result);
    if (!sign_flag) goto loc_0080A249;
    if (v_stack_m298 >= (*(unsigned __int64 *)(v_stack_m2D0 + 24))) goto loc_0080A456;
loc_0080A249:
    v_stack_m2D8 = 0;
    goto loc_0080A1A4;
loc_0080A255:
loc_0080A26D:
    a2 = 0;
    a2 = (*(unsigned __int64 *)(v_stack_m258)) >> (5);
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_m258))) & (31));
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a1 = (v_stack_m258) + (8);
    v_stack_m258 = a1;
    if (a1 != (v_stack_m258 + v_stack_m280 * 8)) goto loc_0080A26D;
    result = MiUnlockAwePagesShared(v_stack_m2C8, result, *(unsigned __int64 *)(v_stack_m2D0 + 32), result);
    v_stack_m2E0 = v_stack_m2B8;
    result = v_stack_m2B8;
    if (v_stack_m288 == 0) {
        a2 = v_stack_m2B8;
        a1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(a1, a2, *(unsigned __int64 *)(v_stack_m2D0 + 32), result);
    }
    *(unsigned __int64 *)(v_stack_m2C0) = v_stack_m250;
    v_stack_m250 = v_stack_m2C0;
    v_stack_m228 = v_stack_m2C0;
    a3 = (v_stack_m230) * (v_stack_m278);
    v_stack_m298 = a3;
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_0080A37A;
    result = MiGetProcessPartition(v_stack_m260, a2, a3, v_stack_m278);
    v_r13 = 0;
    if (result != v_stack_m268) {
        a2 = 4;
        result = a2 - 2;
        if (v_stack_m278 != 1) { a2 = (unsigned int)(result); }
        a4 = a3;
        a3 = result - 1;
        a1 = v_stack_m268;
        result = MiGetCrossPartitionCharges(a1, a2, a3, a4);
        v_r13 = (unsigned int)(result);
        v_stack_m2D8 = (unsigned int)(result);
        a3 = v_stack_m298;
    }
    v_stack_m2E0 = v_stack_m2B8;
loc_0080A37A:
    v_stack_m2A0 = v_stack_m290;
loc_0080A392:
    if (v_stack_m2A8 == v_stack_m290) goto loc_0080A3B9;
    goto loc_00809E10;
loc_0080A3AE:
    v_stack_m2D8 = (unsigned int)((unsigned int)(0xC000009AULL));
loc_0080A3B9:
loc_0080A3BE:
loc_0080A3C6:
    result = v_stack_m290;
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) {
        a2 = 0;
        a1 = v_stack_m1A8;
        result = KiUnstackDetachProcess(a1, a2, a3, v_stack_m2B0);
        v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFEULL));
        v_stack_m2E8 = (unsigned int)(v_rdi);
    }
    if (sign_flag) goto loc_0080A4AF;
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m218) = v_stack_m2A8;
    goto loc_0080A4B7;
loc_0080A40B:
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m2E0, a3, v_stack_m2B0);
    result = MiFreeAwePagesFromMdl(v_stack_m2D0, v_stack_m2C0, a3, v_stack_m2B0);
    result = v_stack_m178;
    if (v_stack_m2C0 != v_stack_m178) {
        a2 = 0;
        a1 = v_stack_m2C0;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m2B0);
    }
    v_stack_m2D8 = (unsigned int)((unsigned int)(0xC000010AULL));
    goto loc_0080A3BE;
loc_0080A456:
    result = MiFreeAwePagesFromMdl(result, v_stack_m2C0, a3, v_stack_m2B0);
    if (v_stack_m2C0 == v_stack_m178) goto loc_0080A3B9;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C0, a2, a3, v_stack_m2B0);
    goto loc_0080A3B9;
loc_0080A486:
    result = (unsigned int)((unsigned int)((unsigned int)(0xC000010AULL)));
    if (v_stack_m2A8 == 0) { result = (unsigned int)((unsigned int)(0xC000009AULL)); }
    v_stack_m2D8 = (unsigned int)(result);
    goto loc_0080A3C6;
loc_0080A4AF:
loc_0080A4B7:
    v_stack_m2C0 = v_stack_m250;
loc_0080A4D4:
    if (v_stack_m250 == 0) goto loc_0080A537;
    v_stack_m258 = v_stack_m250 + 48;
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_m250 + 40))) >> (12);
    v_stack_m230 = a4;
    v_stack_m210 = 0;
loc_0080A500:
    if (0 >= a4) goto loc_0080A52D;
    *(unsigned __int64 *)(v_stack_m248) = *(unsigned __int64 *)(v_stack_m250 + 48 + 0 * 8);
    v_r10 = (v_stack_m248) + (8);
    v_stack_m248 = v_r10;
    a2 = 0;
    a3 = (0) + (v_stack_m2B0);
    v_stack_m210 = a3;
    goto loc_0080A500;
loc_0080A52D:
    v_stack_m2C0 = *(unsigned __int64 *)(v_stack_m250);
    goto loc_0080A4D4;
loc_0080A537:
    goto loc_0080A56A;
loc_0080A56A:
    goto loc_0080A58F;
loc_0080A56F:
    result = v_stack_m250;
    if (v_stack_m250 != v_stack_m178) {
        a2 = 0;
        a1 = v_stack_m250;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
loc_0080A58F:
    v_stack_m2C0 = *(unsigned __int64 *)(v_stack_m250);
    if (*(unsigned __int64 *)(v_stack_m250) != 0) goto loc_0080A56F;
    v_r14 = (v_stack_m2A0) - (v_stack_m2A8);
    v_stack_m290 = v_r14;
    goto loc_0080A5AE;
loc_0080A5A8:
loc_0080A5AE:
loc_0080A5B3:
    if (v_r14 == 0) goto loc_0080A5F8;
    result = *(unsigned __int64 *)(v_stack_m250);
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) {
        a2 = v_stack_m2E0;
        a1 = v_stack_m2C8;
        result = LOCK_ADDRESS_SPACE_SHARED(a1, a2, a3, a4);
        a2 = v_r14;
        a1 = v_stack_m2E0;
        result = MiReturnProcessCommitment(a1, a2, a3, a4);
        a2 = v_stack_m2E0;
        a1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(a1, a2, a3, a4);
    }
    v_rsi = v_stack_m2E0;
    if ((((unsigned __int8)(v_rdi)) & (4)) != 0) {
        v_r14 = -(v_r14);
        v_rsi = v_stack_m2B8;
    }
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) {
        a2 = 0;
        a1 = v_stack_m1A8;
        result = KiUnstackDetachProcess(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rdi)) & (8)) != 0) goto loc_0080A62D;
    if (v_stack_m288 == 0) {
        a1 = v_rsi;
    }
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x68506D4DULL), a3, a4);
loc_0080A62D:
    goto loc_0080A639;
loc_0080A634:
loc_0080A639:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x68506D4DULL), a3, a4);
    v_rsp = (v_rsp) + (768);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateUserPhysicalPages(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint16_t v_stack_m16E;
    uint16_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C7;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint32_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint32_t v_stack_m2E4;
    uint32_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint32_t v_stack_m300;
    uint32_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (768);
    result = (*(uint64_t *)(v_rip + 0x600EFC)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m218 = Arg2;
    *(uint64_t *)(local_rsp - 0x248) = Arg3;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x288) = 0;
    *(uint64_t *)(local_rsp - 0x2B8) = 0;
    Arg2 = 0;
    result = memset(local_rsp - 376, Arg2, 304, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, local_rbx + 72, Arg4);
    v_stack_m2E8 = 0;
    v_stack_m2C8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m260 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m318 = v_stack_m1F8;
    result = MiCaptureAllocateMapExtendedParameters(Arg4, (uint32_t)(Arg5), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rbx + 36);
    if (sign_flag) goto loc_0080A639;
    if (((v_stack_m1C0) & (-27)) != 0) goto loc_0080A634;
    result = (uint32_t)((v_stack_m1C0) & (26));
    if (condition_is_equal) goto loc_00809935;
    result = (uint8_t)((result) + (255));
    result = (uint8_t)((result) & ((uint8_t)(v_stack_m1C0)));
    result = 0;
    if ((((uint8_t)(result)) & (26)) == 0) {
        result = 1;
    }
    if ((uint32_t)(result) == 0) goto loc_0080A634;
    if (((2) & ((uint8_t)(v_stack_m1C0))) == 0) goto loc_00809959;
    v_stack_m2B0 = 16;
    goto loc_0080999A;
loc_00809959:
    if ((((uint8_t)(v_stack_m1C0)) & (8)) == 0) goto loc_0080996C;
    v_stack_m2B0 = 512;
    goto loc_0080999A;
loc_0080996C:
    if ((((uint8_t)(v_stack_m1C0)) & (16)) == 0) goto loc_00809992;
    result = MiHugePagesSupported(v_stack_m1C0, 2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rbx + 36);
    if ((uint32_t)(result) != 0) goto loc_00809984;
    goto loc_0080A639;
loc_00809984:
    v_stack_m2B0 = 0x40000ULL;
    goto loc_0080999A;
loc_00809992:
    v_stack_m2B0 = 0;
loc_0080999A:
    if (v_stack_m1D8 > ((uint32_t)(*(uint16_t *)(v_rip + 0x7BB65F)))) goto loc_0080A634;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008099D2;
    v_stack_m2A0 = *(uint64_t *)(arg2);
    v_stack_m290 = *(uint64_t *)(arg2);
    if (*(uint64_t *)(arg2) != 0) goto loc_00809A41;
    result = 0;
    goto loc_0080A639;
loc_008099D2:
    Arg1 = v_stack_m1C0;
    if ((*(uint64_t *)(arg2)) < v_stack_m1C0) { Arg1 = *(uint64_t *)(arg2); }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    v_stack_m2A0 = *(uint64_t *)(*(uint64_t *)(arg2));
    v_stack_m290 = *(uint64_t *)(*(uint64_t *)(arg2));
    if (*(uint64_t *)(*(uint64_t *)(arg2)) != 0) goto loc_00809A08;
    result = 0;
    goto loc_0080A639;
loc_00809A08:
    if ((*(uint64_t *)(*(uint64_t *)(arg2))) <= 0) goto loc_00809A21;
    goto loc_0080A639;
loc_00809A21:
    result = ProbeForWrite(v_stack_m248, *(uint64_t *)(*(uint64_t *)(arg2)) * 8, 8, local_rbx + 36);
loc_00809A41:
    v_stack_m2D0 = 0;
    v_stack_m318 = v_stack_m288;
    result = MiReferenceAweHandle(Arg1, 2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m2B8);
    if (sign_flag) goto loc_0080A639;
    if (v_stack_m288 == 0) goto loc_00809A96;
    result = MiSectionControlArea(v_stack_m288, 2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m2B8);
    v_stack_m2D0 = *(uint64_t *)(result + 0x8);
    goto loc_00809AB7;
loc_00809A96:
    v_stack_m2E0 = v_stack_m2B8;
    if (v_stack_m2B8 != 0) goto loc_00809AC7;
    v_stack_m2E8 = (uint32_t)(v_stack_m2B8 + 8);
loc_00809AB7:
    v_stack_m2B8 = v_stack_m260;
    v_stack_m2E0 = v_stack_m260;
loc_00809AC7:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x7CFFFF), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m2B8);
    if ((uint8_t)(result) != 0) goto loc_00809AE5;
    goto loc_0080A5AE;
loc_00809AE5:
    local_rdi = v_stack_m2B8 + 8;
    if (v_stack_m260 != ((uint32_t)(0xC0000061ULL))) {
        Arg3 = v_stack_m1A8;
        Arg2 = 0;
        Arg1 = v_stack_m260;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, v_stack_m2B8);
        local_rdi = (uint32_t)((v_stack_m2B8 + 8) | (1));
        v_stack_m2E8 = (uint32_t)(local_rdi);
    }
    v_stack_m2A8 = 0;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00809B1A;
    v_stack_m270 = *(uint64_t *)(result + 0x8);
    goto loc_00809B3F;
loc_00809B1A:
    result = MiCreateProcessDefaultAweInfo((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m2D0, Arg3, v_stack_m2B8);
    if (sign_flag) goto loc_0080A5AE;
    v_stack_m270 = v_stack_m260;
loc_00809B3F:
    result = MiGetAwePageSize(v_stack_m2D0, v_stack_m2D0, Arg3, v_stack_m2B8);
    v_stack_m278 = result;
    if (result != 16) goto loc_00809B62;
    v_stack_m2E4 = 0x1000ULL;
    goto loc_00809B8A;
loc_00809B62:
    if (result != 512) goto loc_00809B75;
    v_stack_m2E4 = 0x1000000ULL;
    goto loc_00809B8A;
loc_00809B75:
    result = 0;
    if (result == 0x40000ULL) { result = (uint32_t)((uint32_t)(0x2000000ULL)); }
    v_stack_m2E4 = (uint32_t)(result);
loc_00809B8A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m2D0 + 0x8)))) & (8)) != 0) {
        local_rdi = (uint32_t)((local_rdi) | (32));
        v_stack_m2E8 = (uint32_t)(local_rdi);
    }
    if (v_stack_m2B0 != 0) goto loc_00809BB3;
    v_stack_m2B0 = result;
    goto loc_00809BDA;
loc_00809BB3:
    if (result <= result) goto loc_0080A5A8;
    Arg2 = 0;
    if (0 != 0) goto loc_0080A5A8;
    if (((result) & (result - 1)) != 0) goto loc_0080A5A8;
loc_00809BDA:
    if (result <= 1) goto loc_00809C0A;
    result = (*(uint64_t *)(*(uint64_t *)(arg2))) * (result);
    if ((*(uint64_t *)(*(uint64_t *)(arg2))) < result) goto loc_00809BF7;
    goto loc_0080A5AE;
loc_00809BF7:
    v_stack_m2A0 = result;
    v_stack_m290 = result;
loc_00809C0A:
    if (v_stack_m288 != 0) goto loc_00809C8F;
    result = LOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, Arg3, result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x1F4)))) & (32)) == 0) goto loc_00809C44;
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, Arg3, result);
    goto loc_0080A5B3;
loc_00809C44:
    result = MiChargeProcessPhysicalPages(v_stack_m260, result, Arg3, result);
    if ((uint32_t)(result) != 0) goto loc_00809C69;
loc_00809C59:
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, Arg3, result);
    goto loc_0080A5B3;
loc_00809C69:
    local_rdi = (uint32_t)((local_rdi) | (4));
    result = MiChargeProcessCommitment(v_stack_m2C8, v_stack_m260, Arg3, result);
    if ((uint32_t)(result) == 0) goto loc_00809C59;
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m260, Arg3, result);
    local_rdi = (uint32_t)((local_rdi) | (2));
    v_stack_m2E8 = (uint32_t)(local_rdi);
loc_00809C8F:
    result = MiGetAweInfoPartition(v_stack_m2D0, v_stack_m260, Arg3, v_stack_m2B0);
    v_stack_m268 = result;
    Arg2 = (*(uint64_t *)(result + 0x4848)) + 1;
    v_stack_m240 = Arg2;
    v_stack_m250 = 0;
    v_stack_m228 = 0;
    if ((*(uint64_t *)(v_stack_m260 + 0x310)) == 0) goto loc_00809D09;
    if (((uint16_t)(*(uint16_t *)(v_stack_m260 + 0x6EC))) == 332) goto loc_00809CEA;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(v_stack_m260 + 0x6EC))) == 452) {
        result = 1;
    }
    if ((uint8_t)(result) != 0) {
        if (Arg2 > result) { Arg2 = result; }
        v_stack_m240 = Arg2;
    }
    local_r15 = (Arg2) << (12);
    v_stack_m2D8 = 0;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m2E4)) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((uint32_t)((uint32_t)(v_stack_m1D8)) == 0) goto loc_00809D44;
    if ((uint8_t)(v_stack_m1C7) == 0) goto loc_00809D57;
    Arg3 = (uint32_t)((Arg3) | (2));
    goto loc_00809D57;
loc_00809D44:
    result = KeGetIdealNodeNumberThread(v_stack_m2C8, (uint32_t)(0x80000000ULL), Arg3, v_stack_m2B0);
loc_00809D57:
    local_r12 = (uint32_t)((uint32_t)((uint16_t)(result)));
    if ((uint8_t)(v_stack_m1C7) == 0) {
        local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(result)))) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m2D0 + 0x8)))) & (4)) != 0) {
        Arg3 = (uint32_t)((Arg3) | (1));
    }
    local_rsi = (v_stack_m2B0) << (12);
    result = 0;
    if (v_stack_m2B0 != 1) { result = local_rsi; }
    v_stack_m238 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) | (48));
    if (v_stack_m2B0 != 1) { Arg3 = (uint32_t)(result); }
    v_stack_m2E4 = (uint32_t)(Arg3);
    result = MiGetProcessPartition(v_stack_m2E0, (uint32_t)(0x80000000ULL), Arg3, v_stack_m2B0);
    if (result != result) goto loc_00809DFC;
    Arg1 = (result < result) ? 1 : 0;
    result = ((((uint8_t)(local_rdi)) & (32)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00809DFC;
    if (v_stack_m2B0 != 16) goto loc_00809DFC;
    v_stack_m2E0 = v_stack_m2B8;
    v_stack_m2A0 = v_stack_m290;
    if ((((uint8_t)(v_stack_m2B0)) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) != 0) goto loc_00809E04;
    v_stack_m2E8 = (uint32_t)(local_rdi);
    goto loc_00809E04;
loc_00809DFC:
loc_00809E04:
    v_stack_m220 = v_stack_m2D0 + 8;
loc_00809E10:
    v_stack_m2C0 = 0;
    local_r11 = (v_stack_m2A0) - (v_stack_m2A8);
    v_stack_m280 = local_r11;
    if (v_stack_m278 == 1) {
        if (local_r11 > ((uint32_t)(0xC0000ULL))) { local_r11 = (uint32_t)(0xC0000ULL); }
        v_stack_m280 = local_r11;
    }
    if ((((uint8_t)(local_rdi)) & (64)) != 0) goto loc_00809EBC;
    Arg2 = 0;
    if (local_r11 > 32) goto loc_00809EBC;
    local_rdi = (uint32_t)((local_rdi) | (64));
    v_stack_m2E8 = (uint32_t)(local_rdi);
    result = (local_r11) << (12);
    v_stack_m178 = 0;
    Arg1 = (result + 4095) >> (12);
    Arg1 = (uint16_t)((Arg1) + (6));
    Arg1 = (uint16_t)((Arg1) << (3));
    v_stack_m170 = (uint16_t)(Arg1);
    v_stack_m16E = 0;
    v_stack_m158 = 0;
    v_stack_m14C = 0;
    v_stack_m150 = (uint32_t)(result);
    goto loc_00809EBF;
loc_00809EBC:
loc_00809EBF:
    v_stack_m298 = 0;
    if ((((uint8_t)(local_rdi)) & (32)) == 0) goto loc_00809EFD;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m220))) >> (2));
    Arg4 = (uint32_t)((Arg4) & (1));
    v_stack_m318 = 0;
    result = MiAllocateUserPhysicalRanges(v_stack_m268, local_r11, (uint32_t)((uint32_t)(local_r12)), Arg4);
    goto loc_0080A141;
loc_00809EFD:
    if ((uint32_t)((uint32_t)(local_r12)) == 0) goto loc_00809F96;
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rdi))) & (144));
    if (((uint8_t)(result)) != 128) goto loc_00809F96;
    v_stack_m310 = v_stack_m270;
    v_stack_m318 = v_stack_m240;
    result = MiAllocateFastAwePages(v_stack_m298, v_stack_m2D0, (uint32_t)((uint32_t)((uint16_t)(result))), (uint32_t)(v_stack_m2E4));
    v_stack_m2D8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00809F71;
    if (((uint32_t)(result)) == 0xC000012DULL) goto loc_0080A3AE;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFF3FULL));
loc_00809F60:
    v_stack_m2E8 = (uint32_t)(local_rdi);
loc_00809F64:
    goto loc_0080A392;
loc_00809F71:
    v_stack_m2C0 = v_stack_m298;
loc_00809F96:
    if (v_stack_m298 != 0) goto loc_0080A152;
    if (v_stack_m280 < 16) goto loc_0080A0D9;
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_0080A0D9;
    if (local_rsi != 0x1000ULL) goto loc_00809FE5;
loc_00809FBE:
    if (0 >= 3) goto loc_00809FE5;
    if (v_stack_m280 < (*(uint64_t *)(v_rip - 0x7F836C + 0x0 * 8))) goto loc_00809FDA;
    if (v_stack_m2B0 >= (*(uint64_t *)(v_rip - 0x7F836C + 0x0 * 8))) goto loc_00809FDE;
loc_00809FDA:
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00809FBE;
loc_00809FDE:
    local_rsi = (*(uint64_t *)(v_rip - 0x7F836C + 0x0 * 8)) << (12);
loc_00809FE5:
    result = (uint32_t)(((uint32_t)(v_stack_m2E4)) | (66));
    Arg1 = (v_stack_m280) << (12);
    v_stack_m2F0 = v_stack_m298;
    v_stack_m2F8 = v_stack_m270;
    v_stack_m300 = (uint32_t)(result);
    v_stack_m308 = (uint32_t)((uint16_t)(result));
    v_stack_m310 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2D0 + 0x34)));
    v_stack_m318 = Arg1;
    result = MiAllocatePagesForMdl(v_stack_m268, 0, local_r15 - 4096, local_rsi);
    v_stack_m2C0 = result;
    if (result != 0) goto loc_0080A0D9;
loc_0080A058:
    if (0 > 1) goto loc_0080A0BD;
    if (local_rsi <= v_stack_m238) goto loc_0080A08E;
    Arg1 = (*(uint64_t *)(v_rip - 0x7F8410 + 0x0 * 8)) << (12);
    if (local_rsi != Arg1) goto loc_0080A08E;
    if (v_stack_m280 < (*(uint64_t *)(v_rip - 0x7F8410 + 0x0 + 0x1 * 8))) goto loc_0080A08E;
    if (v_stack_m2B0 >= (*(uint64_t *)(v_rip - 0x7F8410 + 0x0 + 0x1 * 8))) goto loc_0080A092;
loc_0080A08E:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0080A058;
loc_0080A092:
    if ((uint32_t)(Arg2) != 0) goto loc_0080A0A8;
    if (((v_stack_m2E4) & (0x2000000ULL)) == 0) goto loc_0080A0C4;
loc_0080A0A0:
    local_rdi = (uint32_t)((local_rdi) | (16));
    goto loc_00809F60;
loc_0080A0A8:
    if (((uint32_t)(Arg2)) != 1) goto loc_0080A0C7;
    if (((v_stack_m2E4) & (0x1000000ULL)) != 0) { Arg2 = (uint32_t)(Arg2 + 1); }
    goto loc_0080A0C4;
loc_0080A0BD:
loc_0080A0C4:
loc_0080A0C7:
    if (((uint32_t)(Arg2)) > 1) goto loc_0080A0A0;
    local_rsi = (*(uint64_t *)(v_rip - 0x7F8464 + arg2 + 0x1 * 8)) << (12);
    goto loc_00809F64;
loc_0080A0D9:
    if (Arg1 != 0) goto loc_0080A152;
    Arg3 = (v_stack_m280) << (12);
    v_stack_m2F0 = v_stack_m298;
    v_stack_m2F8 = v_stack_m270;
    v_stack_m300 = (uint32_t)((uint32_t)(v_stack_m2E4));
    v_stack_m308 = (uint32_t)((uint16_t)(result));
    v_stack_m310 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2D0 + 0x34)));
    v_stack_m318 = Arg3;
    result = MiAllocatePagesForMdl(v_stack_m268, 0, local_r15 - 4096, v_stack_m238);
loc_0080A141:
    v_stack_m2C0 = result;
    if (result == 0) goto loc_0080A486;
loc_0080A152:
    v_stack_m258 = result + 48;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x28))) >> (12);
    v_stack_m280 = Arg1;
    v_stack_m230 = Arg1;
loc_0080A17C:
    Arg1 = *(uint64_t *)(result + 0x30);
    if ((*(uint64_t *)(result + 0x30)) <= 0) { Arg1 = 0; }
    Arg2 = (result + 48) + (8);
    if (Arg2 != (result + 48 + Arg1 * 8)) goto loc_0080A17C;
    Arg2 = 0;
    v_stack_m298 = Arg1;
loc_0080A1A4:
    if (v_stack_m288 != 0) goto loc_0080A1D1;
    result = LOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m2E0, result + 48 + Arg1 * 8, v_stack_m238);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m2E0 + 0x1F4)))) & (32)) != 0) goto loc_0080A40B;
loc_0080A1D1:
    result = MiLockAwePagesShared(v_stack_m2D0, v_stack_m2C8, result + 48 + Arg1 * 8, v_stack_m238);
    if (v_stack_m298 < (*(uint64_t *)(v_stack_m2D0 + 0x18))) goto loc_0080A255;
    result = MiUnlockAwePagesShared(v_stack_m2C8, result, result + 48 + Arg1 * 8, result);
    if (v_stack_m288 == 0) {
        Arg2 = v_stack_m2E0;
        Arg1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(Arg1, Arg2, result + 48 + Arg1 * 8, result);
    }
    result = MiResizeAweBitMap(v_stack_m2D0, Arg2, result + 48 + Arg1 * 8, result);
    v_stack_m2D8 = (uint32_t)(result);
    if (!sign_flag) goto loc_0080A249;
    if (v_stack_m298 >= (*(uint64_t *)(v_stack_m2D0 + 0x18))) goto loc_0080A456;
loc_0080A249:
    v_stack_m2D8 = 0;
    goto loc_0080A1A4;
loc_0080A255:
loc_0080A26D:
    Arg2 = 0;
    Arg2 = (*(uint64_t *)(v_stack_m258)) >> (5);
    Arg1 = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_m258))) & (31));
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg1 = (v_stack_m258) + (8);
    v_stack_m258 = Arg1;
    if (Arg1 != (v_stack_m258 + v_stack_m280 * 8)) goto loc_0080A26D;
    result = MiUnlockAwePagesShared(v_stack_m2C8, result, *(uint64_t *)(v_stack_m2D0 + 0x20), result);
    v_stack_m2E0 = v_stack_m2B8;
    result = v_stack_m2B8;
    if (v_stack_m288 == 0) {
        Arg2 = v_stack_m2B8;
        Arg1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(Arg1, Arg2, *(uint64_t *)(v_stack_m2D0 + 0x20), result);
    }
    *(uint64_t *)(v_stack_m2C0) = v_stack_m250;
    v_stack_m250 = v_stack_m2C0;
    v_stack_m228 = v_stack_m2C0;
    Arg3 = (v_stack_m230) * (v_stack_m278);
    v_stack_m298 = Arg3;
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_0080A37A;
    result = MiGetProcessPartition(v_stack_m260, Arg2, Arg3, v_stack_m278);
    local_r13 = 0;
    if (result != v_stack_m268) {
        Arg2 = 4;
        result = Arg2 - 2;
        if (v_stack_m278 != 1) { Arg2 = (uint32_t)(result); }
        Arg4 = Arg3;
        Arg3 = result - 1;
        Arg1 = v_stack_m268;
        result = MiGetCrossPartitionCharges(Arg1, Arg2, Arg3, Arg4);
        local_r13 = (uint32_t)(result);
        v_stack_m2D8 = (uint32_t)(result);
        Arg3 = v_stack_m298;
    }
    v_stack_m2E0 = v_stack_m2B8;
loc_0080A37A:
    v_stack_m2A0 = v_stack_m290;
loc_0080A392:
    if (v_stack_m2A8 == v_stack_m290) goto loc_0080A3B9;
    goto loc_00809E10;
loc_0080A3AE:
    v_stack_m2D8 = (uint32_t)((uint32_t)(0xC000009AULL));
loc_0080A3B9:
loc_0080A3BE:
loc_0080A3C6:
    result = v_stack_m290;
    if ((((uint8_t)(local_rdi)) & (1)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1A8;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, v_stack_m2B0);
        local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFEULL));
        v_stack_m2E8 = (uint32_t)(local_rdi);
    }
    if (sign_flag) goto loc_0080A4AF;
    Arg2 = 0;
    *(uint64_t *)(v_stack_m218) = v_stack_m2A8;
    goto loc_0080A4B7;
loc_0080A40B:
    result = UNLOCK_ADDRESS_SPACE_SHARED(v_stack_m2C8, v_stack_m2E0, Arg3, v_stack_m2B0);
    result = MiFreeAwePagesFromMdl(v_stack_m2D0, v_stack_m2C0, Arg3, v_stack_m2B0);
    result = v_stack_m178;
    if (v_stack_m2C0 != v_stack_m178) {
        Arg2 = 0;
        Arg1 = v_stack_m2C0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m2B0);
    }
    v_stack_m2D8 = (uint32_t)((uint32_t)(0xC000010AULL));
    goto loc_0080A3BE;
loc_0080A456:
    result = MiFreeAwePagesFromMdl(result, v_stack_m2C0, Arg3, v_stack_m2B0);
    if (v_stack_m2C0 == v_stack_m178) goto loc_0080A3B9;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C0, Arg2, Arg3, v_stack_m2B0);
    goto loc_0080A3B9;
loc_0080A486:
    result = (uint32_t)((uint32_t)((uint32_t)(0xC000010AULL)));
    if (v_stack_m2A8 == 0) { result = (uint32_t)((uint32_t)(0xC000009AULL)); }
    v_stack_m2D8 = (uint32_t)(result);
    goto loc_0080A3C6;
loc_0080A4AF:
loc_0080A4B7:
    v_stack_m2C0 = v_stack_m250;
loc_0080A4D4:
    if (v_stack_m250 == 0) goto loc_0080A537;
    v_stack_m258 = v_stack_m250 + 48;
    Arg4 = ((uint32_t)(*(uint32_t *)(v_stack_m250 + 0x28))) >> (12);
    v_stack_m230 = Arg4;
    v_stack_m210 = 0;
loc_0080A500:
    if (0 >= Arg4) goto loc_0080A52D;
    *(uint64_t *)(v_stack_m248) = *(uint64_t *)(v_stack_m250 + 0x30 + 0x0 * 8);
    local_r10 = (v_stack_m248) + (8);
    v_stack_m248 = local_r10;
    Arg2 = 0;
    Arg3 = (0) + (v_stack_m2B0);
    v_stack_m210 = Arg3;
    goto loc_0080A500;
loc_0080A52D:
    v_stack_m2C0 = *(uint64_t *)(v_stack_m250);
    goto loc_0080A4D4;
loc_0080A537:
    goto loc_0080A56A;
loc_0080A56A:
    goto loc_0080A58F;
loc_0080A56F:
    result = v_stack_m250;
    if (v_stack_m250 != v_stack_m178) {
        Arg2 = 0;
        Arg1 = v_stack_m250;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
loc_0080A58F:
    v_stack_m2C0 = *(uint64_t *)(v_stack_m250);
    if (*(uint64_t *)(v_stack_m250) != 0) goto loc_0080A56F;
    local_r14 = (v_stack_m2A0) - (v_stack_m2A8);
    v_stack_m290 = local_r14;
    goto loc_0080A5AE;
loc_0080A5A8:
loc_0080A5AE:
loc_0080A5B3:
    if (local_r14 == 0) goto loc_0080A5F8;
    result = *(uint64_t *)(v_stack_m250);
    if ((((uint8_t)(local_rdi)) & (2)) != 0) {
        Arg2 = v_stack_m2E0;
        Arg1 = v_stack_m2C8;
        result = LOCK_ADDRESS_SPACE_SHARED(Arg1, Arg2, Arg3, Arg4);
        Arg2 = local_r14;
        Arg1 = v_stack_m2E0;
        result = MiReturnProcessCommitment(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m2E0;
        Arg1 = v_stack_m2C8;
        result = UNLOCK_ADDRESS_SPACE_SHARED(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = v_stack_m2E0;
    if ((((uint8_t)(local_rdi)) & (4)) != 0) {
        local_r14 = -(local_r14);
        local_rsi = v_stack_m2B8;
    }
    if ((((uint8_t)(local_rdi)) & (1)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1A8;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(local_rdi)) & (8)) != 0) goto loc_0080A62D;
    if (v_stack_m288 == 0) {
        Arg1 = local_rsi;
    }
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x68506D4DULL), Arg3, Arg4);
loc_0080A62D:
    goto loc_0080A639;
loc_0080A634:
loc_0080A639:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x68506D4DULL), Arg3, Arg4);
    local_rsp = (local_rsp) + (768);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00809828&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
