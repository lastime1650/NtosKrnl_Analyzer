# HalpIvtProcessDrhdEntry

- RVA: `0x005794B4`–`0x00579CCF` (길이 `2,075` bytes)
- VA: `0x00000001405794B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5580`
- 디코드: `497`개 명령, `2,075/2,075` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **34**

### Outgoing calls
- `0x005794FE` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0057950F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0057958F` → [HalSocRequestApi](../4B/HalSocRequestApi_function_004B848C.md) (function, `0x004B848C`)
- `0x005795B5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005795CF` → [ExtEnvAllocateMemory](../56/ExtEnvAllocateMemory_function_005610B0.md) (function, `0x005610B0`)
- `0x005795EE` → [DmrEnumerateRmrrDomains](DmrEnumerateRmrrDomains_function_0057ABC0.md) (function, `0x0057ABC0`)
- `0x0057960C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0057962D` → [HalMapIoSpace](../4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x0057964D` → [HalRegisterPermanentAddressUsage](../56/HalRegisterPermanentAddressUsage_function_00561500.md) (function, `0x00561500`)
- `0x0057989B` → [RtlIsProcessorFeaturePresent](../4B/RtlIsProcessorFeaturePresent_function_004B22C0.md) (function, `0x004B22C0`)
- `0x005798AB` → [DmrGetNextDrhdDeviceScope](DmrGetNextDrhdDeviceScope_function_0057A740.md) (function, `0x0057A740`)
- `0x00579AC8` → [HalpIvtReserveDomainIds](HalpIvtReserveDomainIds_function_00579CD8.md) (function, `0x00579CD8`)
- `0x00579B1D` → [DmrValidateDeviceScope](DmrValidateDeviceScope_function_0057AACC.md) (function, `0x0057AACC`)
- `0x00579B43` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00579B52` → [ExtEnvRegisterIommu](../../init/C2/ExtEnvRegisterIommu_function_00C213EC.md) (function, `0x00C213EC`)
- `0x00579C6D` → [HalpIvtAllocateReservedDomainList](HalpIvtAllocateReservedDomainList_function_00579FB0.md) (function, `0x00579FB0`)
- `0x00579C87` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00579C98` → [HalpUnmapVirtualAddress](../3F/HalpUnmapVirtualAddress_function_003F8C30.md) (function, `0x003F8C30`)
- `0x00579CAA` → [DmrFreeRmrrTree](DmrFreeRmrrTree_function_0057AD18.md) (function, `0x0057AD18`)
- `0x00579CB2` → [ExtEnvFreeMemory](../56/ExtEnvFreeMemory_function_00561320.md) (function, `0x00561320`)

### Direct callers
- [HalpIvtProcessDmarTable](HalpIvtProcessDmarTable_function_005793EC.md) at `0x0057947B`

### Static image references
- `0x0057968F` → RVA `0x00B61F40` (`IvtConfigureSettings`; read)
- `0x0057969D` → RVA `0x00B61FE0` (`IvtInitializeIommu`; read)
- `0x005796AB` → RVA `0x0056E8B0` (`IvtAllocateDomain`; read)
- `0x005796B9` → RVA `0x0056F8E0` (`IvtFreeDomain`; read)
- `0x005796C7` → RVA `0x00579DE0` (`IvtCreateDevice`; read)
- `0x005796D5` → RVA `0x00579ED0` (`IvtDeleteDevice`; read)
- `0x005796E3` → RVA `0x0070DDB0` (`IvtCheckForReservedRegion`; read)
- `0x005796EE` → RVA `0x00579F10` (`IvtFindDevice`; read)
- `0x005796F9` → RVA `0x0057A170` (`IvtEnumerateRmrrDevices`; read)
- `0x0057977C` → RVA `0x00490120` (`IvtUpdateRemappingTableEntry`; read)
- `0x0057978E` → RVA `0x0046A500` (`IvtInvalidateRemappingTableEntry`; read)
- `0x0057979F` → RVA `0x00572910` (`IvtUpdateRemappingDestination`; read)
- `0x00579808` → RVA `0x002D1BD0` (`IvtFlushDomainTb`; read)
- `0x0057981B` → RVA `0x0049E550` (`EmpCheckErrataList`; read)
- `0x00579837` → RVA `0x0056ED40` (`IvtAttachDeviceDomain`; read)
- `0x00579845` → RVA `0x0056F3A0` (`IvtDetachDeviceDomain`; read)
- `0x00579853` → RVA `0x00B62DA0` (`IvtProcessReservedDomains`; read)
- `0x005798F1` → RVA `0x00FC1960` (`.data`; read)
- `0x00579977` → RVA `0x00572600` (`IvtSetDeviceSvmCapabilities`; read)
- `0x00579981` → RVA `0x005724D0` (`IvtSetDevicePasidTable`; read)
- `0x0057998B` → RVA `0x0056FDD0` (`IvtGrowPasidTable`; read)
- `0x00579992` → RVA `0x0056F830` (`IvtFlushTb`; read)
- `0x005799A2` → RVA `0x00572630` (`IvtSetPasidAddressSpace`; read)
- `0x005799B5` → RVA `0x00B62BA0` (`IvtMarkHiberRegions`; read)
- `0x005799D9` → RVA `0x0056F1F0` (`IvtConfigureAts`; read)
- `0x005799E3` → RVA `0x0056F7A0` (`IvtFlushDeviceTbOnly`; read)
- `0x00579A2B` → RVA `0x0056F3E0` (`IvtDismissPageFault`; read)
- `0x00579A36` → RVA `0x0056FB80` (`IvtGetPageFault`; read)
- `0x00579A41` → RVA `0x0056F4B0` (`IvtDrainSvmPageRequests`; read)
- `0x00579A4C` → RVA `0x0056F0B0` (`IvtCancelPageRequests`; read)
- `0x00579AE1` → RVA `0x00B61F70` (`IvtEnableInterrupt`; read)
- `0x00579AEF` → RVA `0x0070DD30` (`IvtDisableInterrupt`; read)
- `0x00579AFA` → RVA `0x0056FF00` (`IvtHandleInterrupt`; read)
- `0x00579B05` → RVA `0x00B62DF0` (`IvtSetMessageInterruptRouting`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00579B52` → [ExtEnvRegisterIommu](../../init/C2/ExtEnvRegisterIommu_function_00C213EC.md) (`.text` → `INIT`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005794B4  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005794B9  55                              push rbp
005794BA  53                              push rbx
005794BB  56                              push rsi
005794BC  57                              push rdi
005794BD  41 54                           push r12
005794BF  41 55                           push r13
005794C1  41 56                           push r14
005794C3  41 57                           push r15
005794C5  48 8D AC 24 A8 FE FF FF         lea rbp, [rsp - 0x158]
005794CD  48 81 EC 58 02 00 00            sub rsp, 0x258
005794D4  4C 8B EA                        mov r13, rdx
005794D7  48 8B F1                        mov rsi, rcx
005794DA  33 FF                           xor edi, edi
005794DC  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
005794E3  0F 57 C0                        xorps xmm0, xmm0
005794E6  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
005794EA  33 D2                           xor edx, edx
005794EC  40 88 BD B0 01 00 00            mov byte ptr [rbp + 0x1b0], dil
005794F3  41 B8 98 00 00 00               mov r8d, 0x98
005794F9  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
005794FE  E8 3D D7 14 00                  call 0x1406c6c40
00579503  33 D2                           xor edx, edx
00579505  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00579509  41 B8 B8 00 00 00               mov r8d, 0xb8
0057950F  E8 2C D7 14 00                  call 0x1406c6c40
00579514  44 8B F7                        mov r14d, edi
00579517  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0057951C  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00579520  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00579524  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00579528  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0057952D  44 0F B6 E7                     movzx r12d, dil
00579531  40 88 BD A8 01 00 00            mov byte ptr [rbp + 0x1a8], dil
00579538  40 88 BD B8 01 00 00            mov byte ptr [rbp + 0x1b8], dil
0057953F  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00579544  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00579549  66 41 39 7D 00                  cmp word ptr [r13], di
0057954E  74 0B                           je 0x14057955b
00579550  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00579556  E9 5C 07 00 00                  jmp 0x140579cb7
0057955B  B9 10 00 00 00                  mov ecx, 0x10
00579560  66 41 39 4D 02                  cmp word ptr [r13 + 2], cx
00579565  73 0B                           jae 0x140579572
00579567  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
0057956D  E9 45 07 00 00                  jmp 0x140579cb7
00579572  49 39 7D 08                     cmp qword ptr [r13 + 8], rdi
00579576  0F 84 3B 07 00 00               je 0x140579cb7
0057957C  33 D2                           xor edx, edx
0057957E  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00579583  44 8B C9                        mov r9d, ecx
00579586  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0057958B  44 8D 42 02                     lea r8d, [rdx + 2]
0057958F  E8 F8 EE F3 FF                  call 0x1404b848c
00579594  85 C0                           test eax, eax
00579596  78 26                           js 0x1405795be
00579598  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0057959D  4C 8D 8D B0 01 00 00            lea r9, [rbp + 0x1b0]
005795A4  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
005795A9  48 8D 54 24 41                  lea rdx, [rsp + 0x41]
005795AE  48 8D 8D B8 01 00 00            lea rcx, [rbp + 0x1b8]
005795B5  E8 16 15 14 00                  call 0x1406baad0
005795BA  84 C0                           test al, al
005795BC  75 07                           jne 0x1405795c5
005795BE  40 88 BD B0 01 00 00            mov byte ptr [rbp + 0x1b0], dil
005795C5  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
005795CA  BA 18 00 00 00                  mov edx, 0x18
005795CF  E8 DC 7A FE FF                  call 0x1405610b0
005795D4  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
005795D9  44 8B F0                        mov r14d, eax
005795DC  85 C0                           test eax, eax
005795DE  0F 88 BE 06 00 00               js 0x140579ca2
005795E4  49 8D 55 04                     lea rdx, [r13 + 4]
005795E8  4D 8B C7                        mov r8, r15
005795EB  48 8B CE                        mov rcx, rsi
005795EE  E8 CD 15 00 00                  call 0x14057abc0
005795F3  44 8B F0                        mov r14d, eax
005795F6  85 C0                           test eax, eax
005795F8  0F 88 A4 06 00 00               js 0x140579ca2
005795FE  BB 68 00 00 00                  mov ebx, 0x68
00579603  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00579607  44 8B C3                        mov r8d, ebx
0057960A  33 D2                           xor edx, edx
0057960C  E8 2F D6 14 00                  call 0x1406c6c40
00579611  8D 43 99                        lea eax, [rbx - 0x67]
00579614  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
00579617  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
0057961B  41 BE 20 02 00 00               mov r14d, 0x220
00579621  48 8B CB                        mov rcx, rbx
00579624  89 45 80                        mov dword ptr [rbp - 0x80], eax
00579627  45 33 C0                        xor r8d, r8d
0057962A  41 8B D6                        mov edx, r14d
0057962D  E8 0E 37 F8 FF                  call 0x1404fcd40
00579632  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00579637  48 85 C0                        test rax, rax
0057963A  75 0B                           jne 0x140579647
0057963C  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00579642  E9 5B 06 00 00                  jmp 0x140579ca2
00579647  41 8B D6                        mov edx, r14d
0057964A  48 8B CB                        mov rcx, rbx
0057964D  E8 AE 7E FE FF                  call 0x140561500
00579652  44 8B F0                        mov r14d, eax
00579655  85 C0                           test eax, eax
00579657  0F 88 2F 06 00 00               js 0x140579c8c
0057965D  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
00579662  41 BF 01 00 00 00               mov r15d, 1
00579668  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0057966D  83 E8 10                        sub eax, 0x10
00579670  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00579674  05 70 01 00 00                  add eax, 0x170
00579679  89 45 90                        mov dword ptr [rbp - 0x70], eax
0057967C  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00579683  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00579687  48 8D 45 F0                     lea rax, [rbp - 0x10]
0057968B  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0057968F  48 8D 05 AA 88 5E 00            lea rax, [rip + 0x5e88aa]
00579696  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
0057969D  48 8D 05 3C 89 5E 00            lea rax, [rip + 0x5e893c]
005796A4  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
005796AB  48 8D 05 FE 51 FF FF            lea rax, [rip - 0xae02]
005796B2  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
005796B9  48 8D 05 20 62 FF FF            lea rax, [rip - 0x9de0]
005796C0  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
005796C7  48 8D 05 12 07 00 00            lea rax, [rip + 0x712]
005796CE  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
005796D5  48 8D 05 F4 07 00 00            lea rax, [rip + 0x7f4]
005796DC  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
005796E3  48 8D 05 C6 46 19 00            lea rax, [rip + 0x1946c6]
005796EA  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
005796EE  48 8D 05 1B 08 00 00            lea rax, [rip + 0x81b]
005796F5  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005796F9  48 8D 05 70 0A 00 00            lea rax, [rip + 0xa70]
00579700  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00579704  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00579709  90                              nop
0057970A  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0057970D  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
00579711  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
00579715  90                              nop
00579716  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
0057971A  48 81 E7 FF EE FF FF            and rdi, 0xffffffffffffeeff
00579721  48 8B D7                        mov rdx, rdi
00579724  C7 45 C8 02 00 00 00            mov dword ptr [rbp - 0x38], 2
0057972B  48 C1 EA 08                     shr rdx, 8
0057972F  48 8B CB                        mov rcx, rbx
00579732  48 C1 E9 23                     shr rcx, 0x23
00579736  8B C2                           mov eax, edx
00579738  83 E0 1F                        and eax, 0x1f
0057973B  C7 45 94 04 00 00 00            mov dword ptr [rbp - 0x6c], 4
00579742  0F BD C0                        bsr eax, eax
00579745  80 E1 1F                        and cl, 0x1f
00579748  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0057974C  41 02 CF                        add cl, r15b
0057974F  41 8B C7                        mov eax, r15d
00579752  48 D3 E0                        shl rax, cl
00579755  B9 00 00 10 00                  mov ecx, 0x100000
0057975A  48 3B C1                        cmp rax, rcx
0057975D  48 0F 47 C1                     cmova rax, rcx
00579761  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00579764  8A 46 25                        mov al, byte ptr [rsi + 0x25]
00579767  24 03                           and al, 3
00579769  41 3A C7                        cmp al, r15b
0057976C  8A C3                           mov al, bl
0057976E  0F 94 C1                        sete cl
00579771  24 18                           and al, 0x18
00579773  3C 18                           cmp al, 0x18
00579775  0F 94 C0                        sete al
00579778  84 C8                           test al, cl
0057977A  74 33                           je 0x1405797af
0057977C  48 8D 05 9D 69 F1 FF            lea rax, [rip - 0xe9663]
00579783  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
0057978A  41 8D 77 43                     lea esi, [r15 + 0x43]
0057978E  48 8D 05 6B 0D EF FF            lea rax, [rip - 0x10f295]
00579795  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579798  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
0057979F  48 8D 05 6A 91 FF FF            lea rax, [rip - 0x6e96]
005797A6  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
005797AD  EB 03                           jmp 0x1405797b2
005797AF  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
005797B2  80 BD B0 01 00 00 02            cmp byte ptr [rbp + 0x1b0], 2
005797B9  41 B8 00 01 00 00               mov r8d, 0x100
005797BF  0F 85 B2 00 00 00               jne 0x140579877
005797C5  F6 C3 02                        test bl, 2
005797C8  0F 84 A9 00 00 00               je 0x140579877
005797CE  40 84 FF                        test dil, dil
005797D1  0F 88 A0 00 00 00               js 0x140579877
005797D7  83 E2 1F                        and edx, 0x1f
005797DA  0F 95 C1                        setne cl
005797DD  F6 C3 40                        test bl, 0x40
005797E0  0F 95 C0                        setne al
005797E3  84 C8                           test al, cl
005797E5  0F 84 8C 00 00 00               je 0x140579877
005797EB  48 0F BA E7 37                  bt rdi, 0x37
005797F0  0F 83 81 00 00 00               jae 0x140579877
005797F6  48 0F BA E7 36                  bt rdi, 0x36
005797FB  73 7A                           jae 0x140579877
005797FD  44 8B 74 24 44                  mov r14d, dword ptr [rsp + 0x44]
00579802  40 F6 C7 10                     test dil, 0x10
00579806  75 74                           jne 0x14057987c
00579808  48 8D 05 C1 83 D5 FF            lea rax, [rip - 0x2a7c3f]
0057980F  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00579814  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
0057981B  48 8D 05 2E 4D F2 FF            lea rax, [rip - 0xdb2d2]
00579822  48 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], rax
00579829  48 8D 05 20 4D F2 FF            lea rax, [rip - 0xdb2e0]
00579830  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00579837  48 8D 05 02 55 FF FF            lea rax, [rip - 0xaafe]
0057983E  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00579845  48 8D 05 54 5B FF FF            lea rax, [rip - 0xa4ac]
0057984C  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00579853  48 8D 05 46 95 5E 00            lea rax, [rip + 0x5e9546]
0057985A  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00579861  48 0F BD C2                     bsr rax, rdx
00579865  C1 E0 0D                        shl eax, 0xd
00579868  05 00 20 00 00                  add eax, 0x2000
0057986D  41 0B C0                        or eax, r8d
00579870  0B F0                           or esi, eax
00579872  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579875  EB 05                           jmp 0x14057987c
00579877  44 8B 74 24 44                  mov r14d, dword ptr [rsp + 0x44]
0057987C  41 85 F0                        test r8d, esi
0057987F  74 25                           je 0x1405798a6
00579881  48 B9 00 00 00 00 00 48 02 00   movabs rcx, 0x2480000000000
0057988B  48 8B C3                        mov rax, rbx
0057988E  48 23 C1                        and rax, rcx
00579891  48 3B C1                        cmp rax, rcx
00579894  75 10                           jne 0x1405798a6
00579896  B9 3D 00 00 00                  mov ecx, 0x3d
0057989B  E8 20 8A F3 FF                  call 0x1404b22c0
005798A0  84 C0                           test al, al
005798A2  45 0F 45 E7                     cmovne r12d, r15d
005798A6  33 D2                           xor edx, edx
005798A8  49 8B CD                        mov rcx, r13
005798AB  E8 90 0E 00 00                  call 0x14057a740
005798B0  45 33 C9                        xor r9d, r9d
005798B3  45 84 E4                        test r12b, r12b
005798B6  75 78                           jne 0x140579930
005798B8  48 85 C0                        test rax, rax
005798BB  74 62                           je 0x14057991f
005798BD  44 38 38                        cmp byte ptr [rax], r15b
005798C0  75 5D                           jne 0x14057991f
005798C2  80 78 01 08                     cmp byte ptr [rax + 1], 8
005798C6  75 57                           jne 0x14057991f
005798C8  44 38 48 05                     cmp byte ptr [rax + 5], r9b
005798CC  75 51                           jne 0x14057991f
005798CE  80 78 06 02                     cmp byte ptr [rax + 6], 2
005798D2  75 4B                           jne 0x14057991f
005798D4  44 38 48 07                     cmp byte ptr [rax + 7], r9b
005798D8  75 45                           jne 0x14057991f
005798DA  66 45 39 4D 06                  cmp word ptr [r13 + 6], r9w
005798DF  75 3E                           jne 0x14057991f
005798E1  48 8B C7                        mov rax, rdi
005798E4  25 00 00 3F 00                  and eax, 0x3f0000
005798E9  48 3D 00 00 2F 00               cmp rax, 0x2f0000
005798EF  73 2E                           jae 0x14057991f
005798F1  44 38 0D 68 80 A4 00            cmp byte ptr [rip + 0xa48068], r9b
005798F8  75 07                           jne 0x140579901
005798FA  0F BA F6 08                     btr esi, 8
005798FE  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579901  45 85 F6                        test r14d, r14d
00579904  75 07                           jne 0x14057990d
00579906  48 0F BA E7 22                  bt rdi, 0x22
0057990B  EB 05                           jmp 0x140579912
0057990D  48 0F BA E7 23                  bt rdi, 0x23
00579912  73 0B                           jae 0x14057991f
00579914  41 8A D7                        mov dl, r15b
00579917  88 95 A8 01 00 00               mov byte ptr [rbp + 0x1a8], dl
0057991D  EB 03                           jmp 0x140579922
0057991F  41 8A D1                        mov dl, r9b
00579922  41 84 DF                        test r15b, bl
00579925  74 20                           je 0x140579947
00579927  0F BA EE 0B                     bts esi, 0xb
0057992B  89 75 94                        mov dword ptr [rbp - 0x6c], esi
0057992E  EB 17                           jmp 0x140579947
00579930  48 0F BA E3 30                  bt rbx, 0x30
00579935  73 07                           jae 0x14057993e
00579937  0F BA EE 0B                     bts esi, 0xb
0057993B  89 75 94                        mov dword ptr [rbp - 0x6c], esi
0057993E  41 8A D1                        mov dl, r9b
00579941  88 95 A8 01 00 00               mov byte ptr [rbp + 0x1a8], dl
00579947  80 BD B8 01 00 00 06            cmp byte ptr [rbp + 0x1b8], 6
0057994E  75 11                           jne 0x140579961
00579950  80 7C 24 40 BD                  cmp byte ptr [rsp + 0x40], 0xbd
00579955  75 0A                           jne 0x140579961
00579957  41 8A CF                        mov cl, r15b
0057995A  44 38 7C 24 41                  cmp byte ptr [rsp + 0x41], r15b
0057995F  76 03                           jbe 0x140579964
00579961  41 8A C9                        mov cl, r9b
00579964  45 84 E4                        test r12b, r12b
00579967  0F 84 18 01 00 00               je 0x140579a85
0057996D  49 B8 00 00 00 04 00 80 00 00   movabs r8, 0x800004000000
00579977  4C 8D 35 82 8C FF FF            lea r14, [rip - 0x737e]
0057997E  48 8B C3                        mov rax, rbx
00579981  4C 8D 3D 48 8B FF FF            lea r15, [rip - 0x74b8]
00579988  49 23 C0                        and rax, r8
0057998B  4C 8D 1D 3E 64 FF FF            lea r11, [rip - 0x9bc2]
00579992  4C 8D 15 97 5E FF FF            lea r10, [rip - 0xa169]
00579999  49 3B C0                        cmp rax, r8
0057999C  75 31                           jne 0x1405799cf
0057999E  84 C9                           test cl, cl
005799A0  75 2D                           jne 0x1405799cf
005799A2  48 8D 05 87 8C FF FF            lea rax, [rip - 0x7379]
005799A9  4C 89 75 F8                     mov qword ptr [rbp - 8], r14
005799AD  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
005799B1  0F BA EE 07                     bts esi, 7
005799B5  48 8D 05 E4 91 5E 00            lea rax, [rip + 0x5e91e4]
005799BC  89 75 94                        mov dword ptr [rbp - 0x6c], esi
005799BF  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
005799C3  4C 89 7D 00                     mov qword ptr [rbp], r15
005799C7  4C 89 5D 08                     mov qword ptr [rbp + 8], r11
005799CB  4C 89 55 18                     mov qword ptr [rbp + 0x18], r10
005799CF  48 B9 04 00 00 24 02 85 01 00   movabs rcx, 0x1850224000004
005799D9  4C 8D 05 10 58 FF FF            lea r8, [rip - 0xa7f0]
005799E0  48 8B C3                        mov rax, rbx
005799E3  4C 8D 1D B6 5D FF FF            lea r11, [rip - 0xa24a]
005799EA  48 23 C1                        and rax, rcx
005799ED  48 3B C1                        cmp rax, rcx
005799F0  75 78                           jne 0x140579a6a
005799F2  83 CE 20                        or esi, 0x20
005799F5  48 0F BA E3 1F                  bt rbx, 0x1f
005799FA  89 75 94                        mov dword ptr [rbp - 0x6c], esi
005799FD  73 07                           jae 0x140579a06
005799FF  0F BA EE 10                     bts esi, 0x10
00579A03  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579A06  48 8D 05 C3 63 FF FF            lea rax, [rip - 0x9c3d]
00579A0D  4C 89 75 F8                     mov qword ptr [rbp - 8], r14
00579A11  48 89 45 08                     mov qword ptr [rbp + 8], rax
00579A15  48 8D 05 14 8C FF FF            lea rax, [rip - 0x73ec]
00579A1C  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00579A20  48 8D 05 79 91 5E 00            lea rax, [rip + 0x5e9179]
00579A27  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00579A2B  48 8D 05 AE 59 FF FF            lea rax, [rip - 0xa652]
00579A32  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00579A36  48 8D 05 43 61 FF FF            lea rax, [rip - 0x9ebd]
00579A3D  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00579A41  48 8D 05 68 5A FF FF            lea rax, [rip - 0xa598]
00579A48  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00579A4C  48 8D 05 5D 56 FF FF            lea rax, [rip - 0xa9a3]
00579A53  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00579A57  4C 89 7D 00                     mov qword ptr [rbp], r15
00579A5B  4C 89 55 18                     mov qword ptr [rbp + 0x18], r10
00579A5F  4C 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], r8
00579A66  4C 89 5D 20                     mov qword ptr [rbp + 0x20], r11
00579A6A  F6 C3 04                        test bl, 4
00579A6D  74 16                           je 0x140579a85
00579A6F  0F BA EE 0C                     bts esi, 0xc
00579A73  4C 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], r8
00579A7A  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579A7D  4C 89 55 18                     mov qword ptr [rbp + 0x18], r10
00579A81  4C 89 5D 20                     mov qword ptr [rbp + 0x20], r11
00579A85  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00579A8A  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00579A8F  8A C2                           mov al, dl
00579A91  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00579A96  F6 D8                           neg al
00579A98  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00579A9D  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00579AA2  8B D7                           mov edx, edi
00579AA4  48 1B C9                        sbb rcx, rcx
00579AA7  83 E2 07                        and edx, 7
00579AAA  48 23 C8                        and rcx, rax
00579AAD  48 8D 45 DC                     lea rax, [rbp - 0x24]
00579AB1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00579AB6  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
00579ABB  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00579AC0  49 8B CF                        mov rcx, r15
00579AC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00579AC8  E8 0B 02 00 00                  call 0x140579cd8
00579ACD  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
00579AD0  40 F6 C6 20                     test sil, 0x20
00579AD4  75 0B                           jne 0x140579ae1
00579AD6  0F BA E6 08                     bt esi, 8
00579ADA  72 05                           jb 0x140579ae1
00579ADC  40 84 F6                        test sil, sil
00579ADF  79 32                           jns 0x140579b13
00579AE1  48 8D 05 88 84 5E 00            lea rax, [rip + 0x5e8488]
00579AE8  83 CE 12                        or esi, 0x12
00579AEB  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00579AEF  48 8D 05 3A 42 19 00            lea rax, [rip + 0x19423a]
00579AF6  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00579AFA  48 8D 05 FF 63 FF FF            lea rax, [rip - 0x9c01]
00579B01  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00579B05  48 8D 05 E4 92 5E 00            lea rax, [rip + 0x5e92e4]
00579B0C  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00579B10  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579B13  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00579B1A  49 8B D5                        mov rdx, r13
00579B1D  E8 AA 0F 00 00                  call 0x14057aacc
00579B22  33 C9                           xor ecx, ecx
00579B24  85 C0                           test eax, eax
00579B26  79 21                           jns 0x140579b49
00579B28  40 F6 C6 20                     test sil, 0x20
00579B2C  74 1B                           je 0x140579b49
00579B2E  45 33 C9                        xor r9d, r9d
00579B31  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00579B36  BA 00 05 00 00                  mov edx, 0x500
00579B3B  41 8D 49 5C                     lea ecx, [r9 + 0x5c]
00579B3F  45 8D 41 03                     lea r8d, [r9 + 3]
00579B43  E8 18 3B F8 FF                  call 0x1404fd660
00579B48  CC                              int3
00579B49  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00579B4E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00579B52  E8 95 78 6A 00                  call 0x140c213ec
00579B57  44 8B F0                        mov r14d, eax
00579B5A  85 C0                           test eax, eax
00579B5C  0F 88 2A 01 00 00               js 0x140579c8c
00579B62  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00579B66  B9 01 00 00 00                  mov ecx, 1
00579B6B  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00579B70  48 89 06                        mov qword ptr [rsi], rax
00579B73  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00579B78  89 86 FC 00 00 00               mov dword ptr [rsi + 0xfc], eax
00579B7E  48 8D 86 70 01 00 00            lea rax, [rsi + 0x170]
00579B85  48 89 BE D8 00 00 00            mov qword ptr [rsi + 0xd8], rdi
00579B8C  33 FF                           xor edi, edi
00579B8E  48 89 9E E0 00 00 00            mov qword ptr [rsi + 0xe0], rbx
00579B95  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
00579B99  48 89 86 18 01 00 00            mov qword ptr [rsi + 0x118], rax
00579BA0  89 9E 00 01 00 00               mov dword ptr [rsi + 0x100], ebx
00579BA6  41 8A 45 04                     mov al, byte ptr [r13 + 4]
00579BAA  22 C1                           and al, cl
00579BAC  88 86 0C 01 00 00               mov byte ptr [rsi + 0x10c], al
00579BB2  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00579BB6  89 86 04 01 00 00               mov dword ptr [rsi + 0x104], eax
00579BBC  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00579BC0  89 86 08 01 00 00               mov dword ptr [rsi + 0x108], eax
00579BC6  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00579BCA  89 86 F8 00 00 00               mov dword ptr [rsi + 0xf8], eax
00579BD0  48 8D 86 E8 00 00 00            lea rax, [rsi + 0xe8]
00579BD7  48 89 BE D0 00 00 00            mov qword ptr [rsi + 0xd0], rdi
00579BDE  48 89 40 08                     mov qword ptr [rax + 8], rax
00579BE2  48 89 00                        mov qword ptr [rax], rax
00579BE5  48 8D 46 38                     lea rax, [rsi + 0x38]
00579BE9  48 89 40 08                     mov qword ptr [rax + 8], rax
00579BED  48 89 00                        mov qword ptr [rax], rax
00579BF0  48 8D 46 48                     lea rax, [rsi + 0x48]
00579BF4  48 89 40 08                     mov qword ptr [rax + 8], rax
00579BF8  48 89 00                        mov qword ptr [rax], rax
00579BFB  48 8D 46 58                     lea rax, [rsi + 0x58]
00579BFF  48 89 40 08                     mov qword ptr [rax + 8], rax
00579C03  48 89 00                        mov qword ptr [rax], rax
00579C06  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00579C09  0F BA E0 08                     bt eax, 8
00579C0D  73 06                           jae 0x140579c15
00579C0F  88 8E 3E 01 00 00               mov byte ptr [rsi + 0x13e], cl
00579C15  84 C0                           test al, al
00579C17  79 06                           jns 0x140579c1f
00579C19  88 8E 68 01 00 00               mov byte ptr [rsi + 0x168], cl
00579C1F  44 88 A6 40 01 00 00            mov byte ptr [rsi + 0x140], r12b
00579C26  A8 20                           test al, 0x20
00579C28  74 06                           je 0x140579c30
00579C2A  88 8E 3C 01 00 00               mov byte ptr [rsi + 0x13c], cl
00579C30  0F BA E0 0C                     bt eax, 0xc
00579C34  73 06                           jae 0x140579c3c
00579C36  88 8E 3D 01 00 00               mov byte ptr [rsi + 0x13d], cl
00579C3C  40 38 BD A8 01 00 00            cmp byte ptr [rbp + 0x1a8], dil
00579C43  74 06                           je 0x140579c4b
00579C45  88 8E 3F 01 00 00               mov byte ptr [rsi + 0x13f], cl
00579C4B  0F B6 86 E0 00 00 00            movzx eax, byte ptr [rsi + 0xe0]
00579C52  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
00579C57  23 C1                           and eax, ecx
00579C59  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00579C5D  48 8B CE                        mov rcx, rsi
00579C60  89 86 10 01 00 00               mov dword ptr [rsi + 0x110], eax
00579C66  4C 89 BE 58 01 00 00            mov qword ptr [rsi + 0x158], r15
00579C6D  E8 3E 03 00 00                  call 0x140579fb0
00579C72  44 8B F0                        mov r14d, eax
00579C75  85 C0                           test eax, eax
00579C77  78 13                           js 0x140579c8c
00579C79  48 8B 8E 18 01 00 00            mov rcx, qword ptr [rsi + 0x118]
00579C80  49 8D 55 10                     lea rdx, [r13 + 0x10]
00579C84  4C 8B C3                        mov r8, rbx
00579C87  E8 B4 CB 14 00                  call 0x1406c6840
00579C8C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00579C91  45 33 C0                        xor r8d, r8d
00579C94  41 8D 50 01                     lea edx, [r8 + 1]
00579C98  E8 93 EF E7 FF                  call 0x1403f8c30
00579C9D  45 85 F6                        test r14d, r14d
00579CA0  79 15                           jns 0x140579cb7
00579CA2  4D 85 FF                        test r15, r15
00579CA5  74 10                           je 0x140579cb7
00579CA7  49 8B CF                        mov rcx, r15
00579CAA  E8 69 10 00 00                  call 0x14057ad18
00579CAF  49 8B D7                        mov rdx, r15
00579CB2  E8 69 76 FE FF                  call 0x140561320
00579CB7  41 8B C6                        mov eax, r14d
00579CBA  48 81 C4 58 02 00 00            add rsp, 0x258
00579CC1  41 5F                           pop r15
00579CC3  41 5E                           pop r14
00579CC5  41 5D                           pop r13
00579CC7  41 5C                           pop r12
00579CC9  5F                              pop rdi
00579CCA  5E                              pop rsi
00579CCB  5B                              pop rbx
00579CCC  5D                              pop rbp
00579CCD  C3                              ret
00579CCE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIvtProcessDrhdEntry(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m118;
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
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1BC;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m204;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned int v_stack_m244;
    unsigned int v_stack_m248;
    unsigned int v_stack_m24C;
    unsigned int v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int8 v_stack_m257;
    unsigned __int8 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (600);
    v_rdi = 0;
    v_stack_m24C = 0;
    a2 = 0;
    v_stack_p18 = 0;
    v_stack_m228 = v_xmm0;
    result = memset(v_stack_mE8, a2, 152, a4);
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 184, a4);
    v_stack_m230 = 0;
    v_stack_m248 = 0;
    v_stack_m244 = 0;
    v_stack_m254 = 0;
    v_stack_m240 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    v_stack_m257 = 0;
    v_stack_m258 = 0;
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_0057955B;
    goto loc_00579CB7;
loc_0057955B:
    if ((*(unsigned __int16 *)(a2 + 2)) >= 16) goto loc_00579572;
    goto loc_00579CB7;
loc_00579572:
    if ((*(unsigned __int64 *)(a2 + 8)) == 0) goto loc_00579CB7;
    a2 = 0;
    v_stack_m278 = v_stack_m228;
    result = HalSocRequestApi(16, a2, a2 + 2, 16);
    if (sign_flag) goto loc_005795BE;
    result = guard_dispatch_icall(v_stack_p20, v_stack_m257, v_stack_m258, v_stack_p18);
    if ((unsigned __int8)(result) == 0) {
        v_stack_p18 = 0;
    }
    result = ExtEnvAllocateMemory(v_stack_p20, 24, v_stack_m240, v_stack_p18);
    if (sign_flag) goto loc_00579CA2;
    result = DmrEnumerateRmrrDomains(a1, a2 + 4, v_stack_m240, v_stack_p18);
    if (sign_flag) goto loc_00579CA2;
    a2 = 0;
    result = memset(v_stack_m218, a2, 104, v_stack_p18);
    v_stack_m214 = 104;
    v_stack_m218 = (unsigned int)(104 - 103);
    a3 = 0;
    result = HalMapIoSpace(*(unsigned __int64 *)(a2 + 8), 544, a3, v_stack_p18);
    v_stack_m228 = result;
    if (result != 0) goto loc_00579647;
    goto loc_00579CA2;
loc_00579647:
    result = HalRegisterPermanentAddressUsage(*(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a3, v_stack_p18);
    if (sign_flag) goto loc_00579C8C;
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 2)) - (16));
    v_stack_m238 = (unsigned int)(result);
    result = (unsigned int)((result) + (368));
    v_stack_m208 = (unsigned int)(result);
    v_stack_m1E0 = v_stack_mE8;
    v_stack_m1D8 = v_stack_m1A8;
    v_stack_mE8 = v_rip + 6195370;
    v_stack_mE0 = v_rip + 6195516;
    v_stack_mD8 = v_rip - 44546;
    v_stack_mD0 = v_rip - 40416;
    v_stack_mC8 = v_rip + 1810;
    v_stack_mC0 = v_rip + 2036;
    v_stack_m140 = v_rip + 1656518;
    v_stack_m1A8 = v_rip + 2075;
    v_stack_m120 = v_rip + 2672;
    v_stack_m1CC = (unsigned int)(*(unsigned __int16 *)(a2 + 6));
    v_stack_m210 = 0;
    v_rdi = (*(unsigned __int64 *)(v_stack_m228 + 8)) & (0xFFFFFFFFFFFFEEFFULL);
    v_stack_m1D0 = 2;
    a2 = (v_rdi) >> (8);
    a1 = (*(unsigned __int64 *)(v_stack_m228 + 16)) >> (35);
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    v_stack_m204 = 4;
    a1 = (unsigned __int8)((a1) & (31));
    v_stack_m254 = (unsigned int)(result);
    a1 = (unsigned __int8)((a1) + (1));
    result = (1) << ((unsigned __int8)(a1));
    if (result > ((unsigned int)(0x100000ULL))) { result = (unsigned int)(0x100000ULL); }
    v_stack_m1C0 = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 37)) & (3));
    a1 = (((unsigned __int8)(result)) == 1) ? 1 : 0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 16))) & (24));
    result = (((unsigned __int8)(result)) == 24) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_005797AF;
    v_stack_m70 = v_rip - 956003;
    v_stack_m204 = (unsigned int)(1 + 67);
    v_stack_m68 = v_rip - 1110677;
    v_stack_m60 = v_rip - 28310;
    goto loc_005797B2;
loc_005797AF:
loc_005797B2:
    if (v_stack_p18 != 2) goto loc_00579877;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 16))) & (2)) == 0) goto loc_00579877;
    if (sign_flag) goto loc_00579877;
    a2 = (unsigned int)((a2) & (31));
    a1 = (condition_is_not_equal) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 16))) & (64)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00579877;
    if (condition_is_above_or_equal) goto loc_00579877;
    if (condition_is_above_or_equal) goto loc_00579877;
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_0057987C;
    v_stack_m250 = (unsigned int)((unsigned int)(v_stack_m254));
    v_stack_m98 = v_rip - 2784319;
    v_stack_m90 = v_rip - 897746;
    v_stack_m88 = v_rip - 897760;
    v_stack_mA8 = v_rip - 43774;
    v_stack_mA0 = v_rip - 42156;
    v_stack_m118 = v_rip + 6198598;
    result = (unsigned int)((v_rip + 6198598) << (13));
    result = (unsigned int)((result) + (0x2000ULL));
    result = (unsigned int)((result) | (256));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m204)) | ((unsigned int)(result)));
    v_stack_m204 = (unsigned int)(v_rsi);
    goto loc_0057987C;
loc_00579877:
loc_0057987C:
    if (((256) & ((unsigned int)(v_rsi))) == 0) goto loc_005798A6;
    result = (*(unsigned __int64 *)(v_stack_m228 + 16)) & (a1);
    v_r12 = 0;
    if (result == a1) {
        a1 = 61;
        result = RtlIsProcessorFeaturePresent(a1, a2, 256, v_stack_p18);
        v_r12 = 0;
        if ((unsigned __int8)(result) != 0) { v_r12 = 1; }
    }
    a2 = 0;
    result = DmrGetNextDrhdDeviceScope(0, a2, 256, v_stack_p18);
    a4 = 0;
    if ((unsigned __int8)(v_r12) != 0) goto loc_00579930;
    if (result == 0) goto loc_0057991F;
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_0057991F;
    if ((*(unsigned __int8 *)(result + 1)) != 8) goto loc_0057991F;
    if ((*(unsigned __int8 *)(result + 5)) != 0) goto loc_0057991F;
    if ((*(unsigned __int8 *)(result + 6)) != 2) goto loc_0057991F;
    if ((*(unsigned __int8 *)(result + 7)) != 0) goto loc_0057991F;
    if ((*(unsigned __int16 *)(a2 + 6)) != 0) goto loc_0057991F;
    result = (unsigned int)((v_rdi) & (0x3F0000ULL));
    if (result >= 0x2F0000ULL) goto loc_0057991F;
    if ((*(unsigned __int8 *)(v_rip + 10780776)) == 0) {
        v_stack_m204 = (unsigned int)(v_rsi);
    }
    if ((unsigned int)((unsigned int)(v_stack_m254)) != 0) goto loc_0057990D;
    goto loc_00579912;
loc_0057990D:
loc_00579912:
    if (condition_is_above_or_equal) goto loc_0057991F;
    v_stack_p10 = 1;
    goto loc_00579922;
loc_0057991F:
loc_00579922:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 16)))) == 0) goto loc_00579947;
    v_stack_m204 = (unsigned int)(v_rsi);
    goto loc_00579947;
loc_00579930:
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (unsigned int)(v_rsi);
    }
    v_stack_p10 = 0;
loc_00579947:
    if (v_stack_p20 != 6) goto loc_00579961;
    if (v_stack_m258 != 189) goto loc_00579961;
    if (v_stack_m257 >= = 1) {
        a1 = 0;
    }
    if ((unsigned __int8)(v_r12) == 0) goto loc_00579A85;
    result = (*(unsigned __int64 *)(v_stack_m228 + 16)) & (256);
    if (result != 256) goto loc_005799CF;
    if ((unsigned __int8)(a1) == 0) {
        result = v_rip - 29561;
        v_stack_m1A0 = v_rip - 29566;
        v_stack_m188 = result;
        result = v_rip + 6197732;
        v_stack_m204 = (unsigned int)(v_rsi);
        v_stack_m138 = result;
        v_stack_m198 = v_rip - 29880;
        v_stack_m190 = v_rip - 39874;
        v_stack_m180 = v_rip - 41321;
    }
    result = (*(unsigned __int64 *)(v_stack_m228 + 16)) & (a1);
    if (result != a1) goto loc_00579A6A;
    v_rsi = (unsigned int)((v_rsi) | (32));
    v_stack_m204 = (unsigned int)(v_rsi);
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (unsigned int)(v_rsi);
    }
    v_stack_m1A0 = v_rip - 29566;
    v_stack_m190 = v_rip - 39997;
    v_stack_m188 = v_rip - 29676;
    v_stack_m138 = v_rip + 6197625;
    v_stack_m170 = v_rip - 42578;
    v_stack_m168 = v_rip - 40637;
    v_stack_m130 = v_rip - 42392;
    v_stack_m128 = v_rip - 43427;
    v_stack_m198 = v_rip - 29880;
    v_stack_m180 = v_rip - 41321;
    v_stack_m100 = v_rip - 42992;
    v_stack_m178 = v_rip - 41546;
loc_00579A6A:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 16))) & (4)) != 0) {
        v_stack_m100 = v_rip - 42992;
        v_stack_m204 = (unsigned int)(v_rsi);
        v_stack_m180 = v_rip - 41321;
        v_stack_m178 = v_rip - 41546;
    }
    v_stack_m250 = 0;
    result = (unsigned __int8)(-(0));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (7));
    a1 = (a1) & (v_stack_m250);
    v_stack_m268 = v_stack_m1BC;
    v_stack_m270 = a1;
    v_stack_m278 = v_stack_m24C;
    result = HalpIvtReserveDomainIds(v_stack_m240, a2, v_stack_m244, v_stack_m248);
    if ((((unsigned __int8)((unsigned int)(v_stack_m204))) & (32)) != 0) goto loc_00579AE1;
    if (condition_is_below) goto loc_00579AE1;
    v_rsi = (unsigned int)(v_stack_m204);
    if (sign_flag) {
        result = v_rip + 6194312;
        v_rsi = (unsigned int)(((unsigned int)(v_stack_m204)) | (18));
        v_stack_m158 = result;
        result = v_rip + 1655354;
        v_stack_m150 = result;
        result = v_rip - 39937;
        v_stack_m148 = result;
        result = v_rip + 6197988;
        v_stack_m160 = result;
        v_stack_m204 = (unsigned int)(v_rsi);
    }
    result = DmrValidateDeviceScope(v_stack_p8, a2, v_stack_m244, v_stack_m248);
    a1 = 0;
    if (!sign_flag) goto loc_00579B49;
    if ((((unsigned __int8)(v_rsi)) & (32)) != 0) {
        a4 = 0;
        v_stack_m278 = 0;
        a2 = 0x500ULL;
        a1 = a4 + 92;
        a3 = a4 + 3;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ExtEnvRegisterIommu(v_stack_m218, a2, v_stack_m230, a4);
    if (sign_flag) goto loc_00579C8C;
    *(unsigned __int64 *)(v_stack_m230) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned int *)(v_stack_m230 + 252) = (unsigned int)(*(unsigned __int16 *)(a2 + 6));
    *(unsigned __int64 *)(v_stack_m230 + 216) = v_rdi;
    v_rdi = 0;
    *(unsigned __int64 *)(v_stack_m230 + 224) = *(unsigned __int64 *)(v_stack_m228 + 16);
    *(unsigned __int64 *)(v_stack_m230 + 280) = v_stack_m230 + 368;
    *(unsigned int *)(v_stack_m230 + 256) = (unsigned int)((unsigned int)(v_stack_m238));
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 4)) & (1));
    *(unsigned __int8 *)(v_stack_m230 + 268) = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m230 + 260) = (unsigned int)((unsigned int)(v_stack_m24C));
    *(unsigned int *)(v_stack_m230 + 264) = (unsigned int)((unsigned int)(v_stack_m250));
    *(unsigned int *)(v_stack_m230 + 248) = (unsigned int)((unsigned int)(v_stack_m254));
    *(unsigned __int64 *)(v_stack_m230 + 208) = 0;
    *(unsigned __int64 *)(v_stack_m230 + 232 + 8) = v_stack_m230 + 232;
    *(unsigned __int64 *)(v_stack_m230 + 232) = v_stack_m230 + 232;
    *(unsigned __int64 *)(v_stack_m230 + 56 + 8) = v_stack_m230 + 56;
    *(unsigned __int64 *)(v_stack_m230 + 56) = v_stack_m230 + 56;
    *(unsigned __int64 *)(v_stack_m230 + 72 + 8) = v_stack_m230 + 72;
    *(unsigned __int64 *)(v_stack_m230 + 72) = v_stack_m230 + 72;
    *(unsigned __int64 *)(v_stack_m230 + 88 + 8) = v_stack_m230 + 88;
    *(unsigned __int64 *)(v_stack_m230 + 88) = v_stack_m230 + 88;
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_stack_m230 + 318) = 1;
    }
    if (sign_flag) {
        *(unsigned __int8 *)(v_stack_m230 + 360) = 1;
    }
    *(unsigned __int8 *)(v_stack_m230 + 320) = (unsigned __int8)(v_r12);
    if ((((unsigned __int8)((unsigned int)(v_stack_m204))) & (32)) != 0) {
        *(unsigned __int8 *)(v_stack_m230 + 316) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_stack_m230 + 317) = 1;
    }
    if (v_stack_p10 != 0) {
        *(unsigned __int8 *)(v_stack_m230 + 319) = 1;
    }
    result = (unsigned int)((*(unsigned __int8 *)(v_stack_m230 + 224)) & (1));
    *(unsigned int *)(v_stack_m230 + 272) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m230 + 344) = v_stack_m240;
    result = HalpIvtAllocateReservedDomainList(v_stack_m230, (unsigned int)(v_stack_m244), (unsigned int)(v_stack_m248), a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_stack_m230 + 280);
        a2 = a2 + 16;
        a3 = (unsigned int)(v_stack_m238);
        result = memcpy(a1, a2, a3, a4);
    }
    a3 = 0;
    result = HalpUnmapVirtualAddress(v_stack_m228, a3 + 1, a3, a4);
    if (!sign_flag) goto loc_00579CB7;
loc_00579CA2:
    if (v_stack_m240 != 0) {
        a1 = v_stack_m240;
        result = DmrFreeRmrrTree(a1, a3 + 1, a3, a4);
        a2 = v_stack_m240;
        result = ExtEnvFreeMemory(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (600);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HalpIvtProcessDrhdEntry(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m118;
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
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1BC;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m204;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m214;
    uint64_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint32_t v_stack_m244;
    uint32_t v_stack_m248;
    uint32_t v_stack_m24C;
    uint32_t v_stack_m250;
    uint32_t v_stack_m254;
    uint8_t v_stack_m257;
    uint8_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (600);
    local_rdi = 0;
    v_stack_m24C = 0;
    Arg2 = 0;
    v_stack_p18 = 0;
    v_stack_m228 = v_xmm0;
    result = memset(v_stack_mE8, Arg2, 152, a4);
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 184, a4);
    v_stack_m230 = 0;
    v_stack_m248 = 0;
    v_stack_m244 = 0;
    v_stack_m254 = 0;
    v_stack_m240 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    v_stack_m257 = 0;
    v_stack_m258 = 0;
    if ((*(uint16_t *)(arg2)) == 0) goto loc_0057955B;
    goto loc_00579CB7;
loc_0057955B:
    if ((*(uint16_t *)(arg2 + 0x2)) >= 16) goto loc_00579572;
    goto loc_00579CB7;
loc_00579572:
    if ((*(uint64_t *)(arg2 + 0x8)) == 0) goto loc_00579CB7;
    Arg2 = 0;
    v_stack_m278 = v_stack_m228;
    result = HalSocRequestApi(16, Arg2, Arg2 + 2, 16);
    if (sign_flag) goto loc_005795BE;
    result = guard_dispatch_icall(v_stack_p20, v_stack_m257, v_stack_m258, v_stack_p18);
    if ((uint8_t)(result) == 0) {
        v_stack_p18 = 0;
    }
    result = ExtEnvAllocateMemory(v_stack_p20, 24, v_stack_m240, v_stack_p18);
    if (sign_flag) goto loc_00579CA2;
    result = DmrEnumerateRmrrDomains(Arg1, Arg2 + 4, v_stack_m240, v_stack_p18);
    if (sign_flag) goto loc_00579CA2;
    Arg2 = 0;
    result = memset(v_stack_m218, Arg2, 104, v_stack_p18);
    v_stack_m214 = 104;
    v_stack_m218 = (uint32_t)(104 - 103);
    a3 = 0;
    result = HalMapIoSpace(*(uint64_t *)(arg2 + 0x8), 544, a3, v_stack_p18);
    v_stack_m228 = result;
    if (result != 0) goto loc_00579647;
    goto loc_00579CA2;
loc_00579647:
    result = HalRegisterPermanentAddressUsage(*(uint64_t *)(arg2 + 0x8), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a3, v_stack_p18);
    if (sign_flag) goto loc_00579C8C;
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x2)) - (16));
    v_stack_m238 = (uint32_t)(result);
    result = (uint32_t)((result) + (368));
    v_stack_m208 = (uint32_t)(result);
    v_stack_m1E0 = v_stack_mE8;
    v_stack_m1D8 = v_stack_m1A8;
    v_stack_mE8 = v_rip + 6195370;
    v_stack_mE0 = v_rip + 6195516;
    v_stack_mD8 = v_rip - 44546;
    v_stack_mD0 = v_rip - 40416;
    v_stack_mC8 = v_rip + 1810;
    v_stack_mC0 = v_rip + 2036;
    v_stack_m140 = v_rip + 1656518;
    v_stack_m1A8 = v_rip + 2075;
    v_stack_m120 = v_rip + 2672;
    v_stack_m1CC = (uint32_t)(*(uint16_t *)(arg2 + 0x6));
    v_stack_m210 = 0;
    local_rdi = (*(uint64_t *)(v_stack_m228 + 0x8)) & (0xFFFFFFFFFFFFEEFFULL);
    v_stack_m1D0 = 2;
    Arg2 = (local_rdi) >> (8);
    Arg1 = (*(uint64_t *)(v_stack_m228 + 0x10)) >> (35);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    v_stack_m204 = 4;
    Arg1 = (uint8_t)((Arg1) & (31));
    v_stack_m254 = (uint32_t)(result);
    Arg1 = (uint8_t)((Arg1) + (1));
    result = (1) << ((uint8_t)(Arg1));
    if (result > ((uint32_t)(0x100000ULL))) { result = (uint32_t)(0x100000ULL); }
    v_stack_m1C0 = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x25)) & (3));
    Arg1 = (((uint8_t)(result)) == 1) ? 1 : 0;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_m228 + 0x10))) & (24));
    result = (((uint8_t)(result)) == 24) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_005797AF;
    v_stack_m70 = v_rip - 956003;
    v_stack_m204 = (uint32_t)(1 + 67);
    v_stack_m68 = v_rip - 1110677;
    v_stack_m60 = v_rip - 28310;
    goto loc_005797B2;
loc_005797AF:
loc_005797B2:
    if (v_stack_p18 != 2) goto loc_00579877;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 + 0x10))) & (2)) == 0) goto loc_00579877;
    if (sign_flag) goto loc_00579877;
    Arg2 = (uint32_t)((Arg2) & (31));
    Arg1 = (condition_is_not_equal) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_m228 + 0x10))) & (64)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00579877;
    if (condition_is_above_or_equal) goto loc_00579877;
    if (condition_is_above_or_equal) goto loc_00579877;
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_0057987C;
    v_stack_m250 = (uint32_t)((uint32_t)(v_stack_m254));
    v_stack_m98 = v_rip - 2784319;
    v_stack_m90 = v_rip - 897746;
    v_stack_m88 = v_rip - 897760;
    v_stack_mA8 = v_rip - 43774;
    v_stack_mA0 = v_rip - 42156;
    v_stack_m118 = v_rip + 6198598;
    result = (uint32_t)((v_rip + 6198598) << (13));
    result = (uint32_t)((result) + (0x2000ULL));
    result = (uint32_t)((result) | (256));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m204)) | ((uint32_t)(result)));
    v_stack_m204 = (uint32_t)(local_rsi);
    goto loc_0057987C;
loc_00579877:
loc_0057987C:
    if (((256) & ((uint32_t)(local_rsi))) == 0) goto loc_005798A6;
    result = (*(uint64_t *)(v_stack_m228 + 0x10)) & (Arg1);
    local_r12 = 0;
    if (result == Arg1) {
        Arg1 = 61;
        result = RtlIsProcessorFeaturePresent(Arg1, Arg2, 256, v_stack_p18);
        local_r12 = 0;
        if ((uint8_t)(result) != 0) { local_r12 = 1; }
    }
    Arg2 = 0;
    result = DmrGetNextDrhdDeviceScope(0, Arg2, 256, v_stack_p18);
    a4 = 0;
    if ((uint8_t)(local_r12) != 0) goto loc_00579930;
    if (result == 0) goto loc_0057991F;
    if ((*(uint8_t *)(result)) != 1) goto loc_0057991F;
    if ((*(uint8_t *)(result + 0x1)) != 8) goto loc_0057991F;
    if ((*(uint8_t *)(result + 0x5)) != 0) goto loc_0057991F;
    if ((*(uint8_t *)(result + 0x6)) != 2) goto loc_0057991F;
    if ((*(uint8_t *)(result + 0x7)) != 0) goto loc_0057991F;
    if ((*(uint16_t *)(arg2 + 0x6)) != 0) goto loc_0057991F;
    result = (uint32_t)((local_rdi) & (0x3F0000ULL));
    if (result >= 0x2F0000ULL) goto loc_0057991F;
    if ((*(uint8_t *)(v_rip + 0xA48068)) == 0) {
        v_stack_m204 = (uint32_t)(local_rsi);
    }
    if ((uint32_t)((uint32_t)(v_stack_m254)) != 0) goto loc_0057990D;
    goto loc_00579912;
loc_0057990D:
loc_00579912:
    if (condition_is_above_or_equal) goto loc_0057991F;
    v_stack_p10 = 1;
    goto loc_00579922;
loc_0057991F:
loc_00579922:
    if (((1) & ((uint8_t)(*(uint64_t *)(v_stack_m228 + 0x10)))) == 0) goto loc_00579947;
    v_stack_m204 = (uint32_t)(local_rsi);
    goto loc_00579947;
loc_00579930:
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (uint32_t)(local_rsi);
    }
    v_stack_p10 = 0;
loc_00579947:
    if (v_stack_p20 != 6) goto loc_00579961;
    if (v_stack_m258 != 189) goto loc_00579961;
    if (v_stack_m257 >= = 1) {
        Arg1 = 0;
    }
    if ((uint8_t)(local_r12) == 0) goto loc_00579A85;
    result = (*(uint64_t *)(v_stack_m228 + 0x10)) & (256);
    if (result != 256) goto loc_005799CF;
    if ((uint8_t)(Arg1) == 0) {
        result = v_rip - 29561;
        v_stack_m1A0 = v_rip - 29566;
        v_stack_m188 = result;
        result = v_rip + 6197732;
        v_stack_m204 = (uint32_t)(local_rsi);
        v_stack_m138 = result;
        v_stack_m198 = v_rip - 29880;
        v_stack_m190 = v_rip - 39874;
        v_stack_m180 = v_rip - 41321;
    }
    result = (*(uint64_t *)(v_stack_m228 + 0x10)) & (Arg1);
    if (result != Arg1) goto loc_00579A6A;
    local_rsi = (uint32_t)((local_rsi) | (32));
    v_stack_m204 = (uint32_t)(local_rsi);
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (uint32_t)(local_rsi);
    }
    v_stack_m1A0 = v_rip - 29566;
    v_stack_m190 = v_rip - 39997;
    v_stack_m188 = v_rip - 29676;
    v_stack_m138 = v_rip + 6197625;
    v_stack_m170 = v_rip - 42578;
    v_stack_m168 = v_rip - 40637;
    v_stack_m130 = v_rip - 42392;
    v_stack_m128 = v_rip - 43427;
    v_stack_m198 = v_rip - 29880;
    v_stack_m180 = v_rip - 41321;
    v_stack_m100 = v_rip - 42992;
    v_stack_m178 = v_rip - 41546;
loc_00579A6A:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 + 0x10))) & (4)) != 0) {
        v_stack_m100 = v_rip - 42992;
        v_stack_m204 = (uint32_t)(local_rsi);
        v_stack_m180 = v_rip - 41321;
        v_stack_m178 = v_rip - 41546;
    }
    v_stack_m250 = 0;
    result = (uint8_t)(-(0));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (7));
    Arg1 = (Arg1) & (v_stack_m250);
    v_stack_m268 = v_stack_m1BC;
    v_stack_m270 = Arg1;
    v_stack_m278 = v_stack_m24C;
    result = HalpIvtReserveDomainIds(v_stack_m240, Arg2, v_stack_m244, v_stack_m248);
    if ((((uint8_t)((uint32_t)(v_stack_m204))) & (32)) != 0) goto loc_00579AE1;
    if (condition_is_below) goto loc_00579AE1;
    local_rsi = (uint32_t)(v_stack_m204);
    if (sign_flag) {
        result = v_rip + 6194312;
        local_rsi = (uint32_t)(((uint32_t)(v_stack_m204)) | (18));
        v_stack_m158 = result;
        result = v_rip + 1655354;
        v_stack_m150 = result;
        result = v_rip - 39937;
        v_stack_m148 = result;
        result = v_rip + 6197988;
        v_stack_m160 = result;
        v_stack_m204 = (uint32_t)(local_rsi);
    }
    result = DmrValidateDeviceScope(v_stack_p8, Arg2, v_stack_m244, v_stack_m248);
    Arg1 = 0;
    if (!sign_flag) goto loc_00579B49;
    if ((((uint8_t)(local_rsi)) & (32)) != 0) {
        a4 = 0;
        v_stack_m278 = 0;
        Arg2 = 0x500ULL;
        Arg1 = a4 + 92;
        a3 = a4 + 3;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = ExtEnvRegisterIommu(v_stack_m218, Arg2, v_stack_m230, a4);
    if (sign_flag) goto loc_00579C8C;
    *(uint64_t *)(v_stack_m230) = *(uint64_t *)(arg2 + 0x8);
    *(uint32_t *)(v_stack_m230 + 0xFC) = (uint32_t)(*(uint16_t *)(arg2 + 0x6));
    *(uint64_t *)(v_stack_m230 + 0xD8) = local_rdi;
    local_rdi = 0;
    *(uint64_t *)(v_stack_m230 + 0xE0) = *(uint64_t *)(v_stack_m228 + 0x10);
    *(uint64_t *)(v_stack_m230 + 0x118) = v_stack_m230 + 368;
    *(uint32_t *)(v_stack_m230 + 0x100) = (uint32_t)((uint32_t)(v_stack_m238));
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x4)) & (1));
    *(uint8_t *)(v_stack_m230 + 0x10C) = (uint8_t)(result);
    *(uint32_t *)(v_stack_m230 + 0x104) = (uint32_t)((uint32_t)(v_stack_m24C));
    *(uint32_t *)(v_stack_m230 + 0x108) = (uint32_t)((uint32_t)(v_stack_m250));
    *(uint32_t *)(v_stack_m230 + 0xF8) = (uint32_t)((uint32_t)(v_stack_m254));
    *(uint64_t *)(v_stack_m230 + 0xD0) = 0;
    *(uint64_t *)(v_stack_m230 + 0xE8 + 0x8) = v_stack_m230 + 232;
    *(uint64_t *)(v_stack_m230 + 0xE8) = v_stack_m230 + 232;
    *(uint64_t *)(v_stack_m230 + 0x38 + 0x8) = v_stack_m230 + 56;
    *(uint64_t *)(v_stack_m230 + 0x38) = v_stack_m230 + 56;
    *(uint64_t *)(v_stack_m230 + 0x48 + 0x8) = v_stack_m230 + 72;
    *(uint64_t *)(v_stack_m230 + 0x48) = v_stack_m230 + 72;
    *(uint64_t *)(v_stack_m230 + 0x58 + 0x8) = v_stack_m230 + 88;
    *(uint64_t *)(v_stack_m230 + 0x58) = v_stack_m230 + 88;
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_stack_m230 + 0x13E) = 1;
    }
    if (sign_flag) {
        *(uint8_t *)(v_stack_m230 + 0x168) = 1;
    }
    *(uint8_t *)(v_stack_m230 + 0x140) = (uint8_t)(local_r12);
    if ((((uint8_t)((uint32_t)(v_stack_m204))) & (32)) != 0) {
        *(uint8_t *)(v_stack_m230 + 0x13C) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_stack_m230 + 0x13D) = 1;
    }
    if (v_stack_p10 != 0) {
        *(uint8_t *)(v_stack_m230 + 0x13F) = 1;
    }
    result = (uint32_t)((*(uint8_t *)(v_stack_m230 + 0xE0)) & (1));
    *(uint32_t *)(v_stack_m230 + 0x110) = (uint32_t)(result);
    *(uint64_t *)(v_stack_m230 + 0x158) = v_stack_m240;
    result = HalpIvtAllocateReservedDomainList(v_stack_m230, (uint32_t)(v_stack_m244), (uint32_t)(v_stack_m248), a4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(v_stack_m230 + 0x118);
        Arg2 = Arg2 + 16;
        a3 = (uint32_t)(v_stack_m238);
        result = memcpy(Arg1, Arg2, a3, a4);
    }
    a3 = 0;
    result = HalpUnmapVirtualAddress(v_stack_m228, a3 + 1, a3, a4);
    if (!sign_flag) goto loc_00579CB7;
loc_00579CA2:
    if (v_stack_m240 != 0) {
        Arg1 = v_stack_m240;
        result = DmrFreeRmrrTree(Arg1, a3 + 1, a3, a4);
        Arg2 = v_stack_m240;
        result = ExtEnvFreeMemory(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (600);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x25` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x4` | `64` | `R` |
| `Arg2` | `+ 0x6` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005794B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
