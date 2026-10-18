# HalpIvtLegacyProcessDrhdEntry

- RVA: `0x00578C58`–`0x005793E4` (길이 `1,932` bytes)
- VA: `0x0000000140578C58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5580`
- 디코드: `454`개 명령, `1,932/1,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **35**

### Outgoing calls
- `0x00578CA4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00578CB5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00578D25` → [HalSocRequestApi](../4B/HalSocRequestApi_function_004B848C.md) (function, `0x004B848C`)
- `0x00578D41` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00578D5B` → [ExtEnvAllocateMemory](../56/ExtEnvAllocateMemory_function_005610B0.md) (function, `0x005610B0`)
- `0x00578D7A` → [DmrEnumerateRmrrDomains](DmrEnumerateRmrrDomains_function_0057ABC0.md) (function, `0x0057ABC0`)
- `0x00578D98` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00578DB9` → [HalMapIoSpace](../4F/HalMapIoSpace_function_004FCD40.md) (function, `0x004FCD40`)
- `0x00578DD9` → [HalRegisterPermanentAddressUsage](../56/HalRegisterPermanentAddressUsage_function_00561500.md) (function, `0x00561500`)
- `0x00579043` → [DmrGetNextDrhdDeviceScope](DmrGetNextDrhdDeviceScope_function_0057A740.md) (function, `0x0057A740`)
- `0x005791EA` → [HalpIvtReserveDomainIds](HalpIvtReserveDomainIds_function_00579CD8.md) (function, `0x00579CD8`)
- `0x0057923A` → [DmrValidateDeviceScope](DmrValidateDeviceScope_function_0057AACC.md) (function, `0x0057AACC`)
- `0x0057925F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0057926E` → [ExtEnvRegisterIommu](../../init/C2/ExtEnvRegisterIommu_function_00C213EC.md) (function, `0x00C213EC`)
- `0x00579382` → [HalpIvtAllocateReservedDomainList](HalpIvtAllocateReservedDomainList_function_00579FB0.md) (function, `0x00579FB0`)
- `0x0057939C` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005793AD` → [HalpUnmapVirtualAddress](../3F/HalpUnmapVirtualAddress_function_003F8C30.md) (function, `0x003F8C30`)
- `0x005793BF` → [DmrFreeRmrrTree](DmrFreeRmrrTree_function_0057AD18.md) (function, `0x0057AD18`)
- `0x005793C7` → [ExtEnvFreeMemory](../56/ExtEnvFreeMemory_function_00561320.md) (function, `0x00561320`)

### Direct callers
- [HalpIvtProcessDmarTable](HalpIvtProcessDmarTable_function_005793EC.md) at `0x00579474`

### Static image references
- `0x00578E1B` → RVA `0x00B61F40` (`IvtConfigureSettings`; read)
- `0x00578E29` → RVA `0x00B61FE0` (`IvtInitializeIommu`; read)
- `0x00578E37` → RVA `0x0056E8B0` (`IvtAllocateDomain`; read)
- `0x00578E45` → RVA `0x0056F8E0` (`IvtFreeDomain`; read)
- `0x00578E53` → RVA `0x00579DE0` (`IvtCreateDevice`; read)
- `0x00578E61` → RVA `0x00579ED0` (`IvtDeleteDevice`; read)
- `0x00578E6F` → RVA `0x0070DDB0` (`IvtCheckForReservedRegion`; read)
- `0x00578E7A` → RVA `0x00579F10` (`IvtFindDevice`; read)
- `0x00578E85` → RVA `0x0057A170` (`IvtEnumerateRmrrDevices`; read)
- `0x00578F12` → RVA `0x00490120` (`IvtUpdateRemappingTableEntry`; read)
- `0x00578F24` → RVA `0x0046A500` (`IvtInvalidateRemappingTableEntry`; read)
- `0x00578F36` → RVA `0x00572910` (`IvtUpdateRemappingDestination`; read)
- `0x00578FA2` → RVA `0x00571420` (`IvtLegacyFlushDomainTb`; read)
- `0x00578FB5` → RVA `0x0049E550` (`EmpCheckErrataList`; read)
- `0x00578FD1` → RVA `0x0056ED40` (`IvtAttachDeviceDomain`; read)
- `0x00578FDF` → RVA `0x0056F3A0` (`IvtDetachDeviceDomain`; read)
- `0x00578FED` → RVA `0x00B62DA0` (`IvtProcessReservedDomains`; read)
- `0x00579086` → RVA `0x00FC1960` (`.data`; read)
- `0x00579101` → RVA `0x00572600` (`IvtSetDeviceSvmCapabilities`; read)
- `0x0057910C` → RVA `0x00571FB0` (`IvtLegacySetDeviceSvmCapabilities`; read)
- `0x0057911A` → RVA `0x00571EE0` (`IvtLegacySetDevicePasidTable`; read)
- `0x00579125` → RVA `0x00571CA0` (`IvtLegacyGrowPasidTable`; read)
- `0x00579130` → RVA `0x00571FD0` (`IvtLegacySetPasidAddressSpace`; read)
- `0x0057913B` → RVA `0x0056F3E0` (`IvtDismissPageFault`; read)
- `0x00579146` → RVA `0x0056FB80` (`IvtGetPageFault`; read)
- `0x00579151` → RVA `0x00B62BA0` (`IvtMarkHiberRegions`; read)
- `0x0057915C` → RVA `0x0056F4B0` (`IvtDrainSvmPageRequests`; read)
- `0x00579167` → RVA `0x0056F0B0` (`IvtCancelPageRequests`; read)
- `0x00579178` → RVA `0x00571270` (`IvtLegacyConfigureAts`; read)
- `0x0057918B` → RVA `0x005714A0` (`IvtLegacyFlushTb`; read)
- `0x00579196` → RVA `0x0056F7A0` (`IvtFlushDeviceTbOnly`; read)
- `0x005791FE` → RVA `0x00B61F70` (`IvtEnableInterrupt`; read)
- `0x0057920C` → RVA `0x0070DD30` (`IvtDisableInterrupt`; read)
- `0x00579217` → RVA `0x0056FF00` (`IvtHandleInterrupt`; read)
- `0x00579222` → RVA `0x00B62DF0` (`IvtSetMessageInterruptRouting`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0057926E` → [ExtEnvRegisterIommu](../../init/C2/ExtEnvRegisterIommu_function_00C213EC.md) (`.text` → `INIT`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00578C58  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00578C5D  55                              push rbp
00578C5E  53                              push rbx
00578C5F  56                              push rsi
00578C60  57                              push rdi
00578C61  41 54                           push r12
00578C63  41 55                           push r13
00578C65  41 56                           push r14
00578C67  41 57                           push r15
00578C69  48 8D AC 24 A8 FE FF FF         lea rbp, [rsp - 0x158]
00578C71  48 81 EC 58 02 00 00            sub rsp, 0x258
00578C78  4C 8B EA                        mov r13, rdx
00578C7B  48 8B D9                        mov rbx, rcx
00578C7E  33 FF                           xor edi, edi
00578C80  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
00578C87  0F 57 C0                        xorps xmm0, xmm0
00578C8A  89 BD B8 01 00 00               mov dword ptr [rbp + 0x1b8], edi
00578C90  33 D2                           xor edx, edx
00578C92  40 88 BD A8 01 00 00            mov byte ptr [rbp + 0x1a8], dil
00578C99  41 B8 98 00 00 00               mov r8d, 0x98
00578C9F  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00578CA4  E8 97 DF 14 00                  call 0x1406c6c40
00578CA9  33 D2                           xor edx, edx
00578CAB  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00578CAF  41 B8 B8 00 00 00               mov r8d, 0xb8
00578CB5  E8 86 DF 14 00                  call 0x1406c6c40
00578CBA  40 8A F7                        mov sil, dil
00578CBD  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00578CC2  44 8A E7                        mov r12b, dil
00578CC5  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
00578CC9  44 8B F7                        mov r14d, edi
00578CCC  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00578CD0  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
00578CD4  89 BD B0 01 00 00               mov dword ptr [rbp + 0x1b0], edi
00578CDA  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00578CDF  66 41 39 7D 00                  cmp word ptr [r13], di
00578CE4  74 0B                           je 0x140578cf1
00578CE6  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00578CEC  E9 DB 06 00 00                  jmp 0x1405793cc
00578CF1  B9 10 00 00 00                  mov ecx, 0x10
00578CF6  66 41 39 4D 02                  cmp word ptr [r13 + 2], cx
00578CFB  73 0B                           jae 0x140578d08
00578CFD  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00578D03  E9 C4 06 00 00                  jmp 0x1405793cc
00578D08  49 39 7D 08                     cmp qword ptr [r13 + 8], rdi
00578D0C  0F 84 BA 06 00 00               je 0x1405793cc
00578D12  33 D2                           xor edx, edx
00578D14  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00578D19  44 8B C9                        mov r9d, ecx
00578D1C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00578D21  44 8D 42 02                     lea r8d, [rdx + 2]
00578D25  E8 62 F7 F3 FF                  call 0x1404b848c
00578D2A  85 C0                           test eax, eax
00578D2C  78 1C                           js 0x140578d4a
00578D2E  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00578D33  4C 8D 8D A8 01 00 00            lea r9, [rbp + 0x1a8]
00578D3A  45 33 C0                        xor r8d, r8d
00578D3D  33 D2                           xor edx, edx
00578D3F  33 C9                           xor ecx, ecx
00578D41  E8 8A 1D 14 00                  call 0x1406baad0
00578D46  84 C0                           test al, al
00578D48  75 07                           jne 0x140578d51
00578D4A  40 88 BD A8 01 00 00            mov byte ptr [rbp + 0x1a8], dil
00578D51  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00578D56  BA 18 00 00 00                  mov edx, 0x18
00578D5B  E8 50 83 FE FF                  call 0x1405610b0
00578D60  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00578D65  44 8B F0                        mov r14d, eax
00578D68  85 C0                           test eax, eax
00578D6A  0F 88 47 06 00 00               js 0x1405793b7
00578D70  49 8D 55 04                     lea rdx, [r13 + 4]
00578D74  4D 8B C7                        mov r8, r15
00578D77  48 8B CB                        mov rcx, rbx
00578D7A  E8 41 1E 00 00                  call 0x14057abc0
00578D7F  44 8B F0                        mov r14d, eax
00578D82  85 C0                           test eax, eax
00578D84  0F 88 2D 06 00 00               js 0x1405793b7
00578D8A  BB 68 00 00 00                  mov ebx, 0x68
00578D8F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00578D93  44 8B C3                        mov r8d, ebx
00578D96  33 D2                           xor edx, edx
00578D98  E8 A3 DE 14 00                  call 0x1406c6c40
00578D9D  8D 43 99                        lea eax, [rbx - 0x67]
00578DA0  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
00578DA3  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
00578DA7  41 BE 20 02 00 00               mov r14d, 0x220
00578DAD  48 8B CB                        mov rcx, rbx
00578DB0  89 45 80                        mov dword ptr [rbp - 0x80], eax
00578DB3  45 33 C0                        xor r8d, r8d
00578DB6  41 8B D6                        mov edx, r14d
00578DB9  E8 82 3F F8 FF                  call 0x1404fcd40
00578DBE  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00578DC3  48 85 C0                        test rax, rax
00578DC6  75 0B                           jne 0x140578dd3
00578DC8  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00578DCE  E9 E4 05 00 00                  jmp 0x1405793b7
00578DD3  41 8B D6                        mov edx, r14d
00578DD6  48 8B CB                        mov rcx, rbx
00578DD9  E8 22 87 FE FF                  call 0x140561500
00578DDE  44 8B F0                        mov r14d, eax
00578DE1  85 C0                           test eax, eax
00578DE3  0F 88 B8 05 00 00               js 0x1405793a1
00578DE9  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
00578DEE  41 BF 01 00 00 00               mov r15d, 1
00578DF4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00578DF9  83 E8 10                        sub eax, 0x10
00578DFC  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00578E00  05 70 01 00 00                  add eax, 0x170
00578E05  89 45 90                        mov dword ptr [rbp - 0x70], eax
00578E08  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00578E0F  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00578E13  48 8D 45 F0                     lea rax, [rbp - 0x10]
00578E17  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00578E1B  48 8D 05 1E 91 5E 00            lea rax, [rip + 0x5e911e]
00578E22  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00578E29  48 8D 05 B0 91 5E 00            lea rax, [rip + 0x5e91b0]
00578E30  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
00578E37  48 8D 05 72 5A FF FF            lea rax, [rip - 0xa58e]
00578E3E  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00578E45  48 8D 05 94 6A FF FF            lea rax, [rip - 0x956c]
00578E4C  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
00578E53  48 8D 05 86 0F 00 00            lea rax, [rip + 0xf86]
00578E5A  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00578E61  48 8D 05 68 10 00 00            lea rax, [rip + 0x1068]
00578E68  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00578E6F  48 8D 05 3A 4F 19 00            lea rax, [rip + 0x194f3a]
00578E76  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
00578E7A  48 8D 05 8F 10 00 00            lea rax, [rip + 0x108f]
00578E81  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00578E85  48 8D 05 E4 12 00 00            lea rax, [rip + 0x12e4]
00578E8C  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00578E90  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00578E95  90                              nop
00578E96  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00578E9A  90                              nop
00578E9B  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00578E9E  48 81 E3 FF EE FF FF            and rbx, 0xffffffffffffeeff
00578EA5  48 8B D3                        mov rdx, rbx
00578EA8  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
00578EAC  48 8B 79 10                     mov rdi, qword ptr [rcx + 0x10]
00578EB0  48 C1 EA 08                     shr rdx, 8
00578EB4  48 8B CF                        mov rcx, rdi
00578EB7  48 C1 E9 23                     shr rcx, 0x23
00578EBB  8B C2                           mov eax, edx
00578EBD  83 E0 1F                        and eax, 0x1f
00578EC0  C7 45 C8 02 00 00 00            mov dword ptr [rbp - 0x38], 2
00578EC7  0F BD C0                        bsr eax, eax
00578ECA  80 E1 1F                        and cl, 0x1f
00578ECD  C7 45 94 04 00 00 00            mov dword ptr [rbp - 0x6c], 4
00578ED4  89 85 B0 01 00 00               mov dword ptr [rbp + 0x1b0], eax
00578EDA  41 02 CF                        add cl, r15b
00578EDD  41 8B C7                        mov eax, r15d
00578EE0  48 D3 E0                        shl rax, cl
00578EE3  B9 00 00 10 00                  mov ecx, 0x100000
00578EE8  48 3B C1                        cmp rax, rcx
00578EEB  48 0F 47 C1                     cmova rax, rcx
00578EEF  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00578EF2  48 8B 85 A0 01 00 00            mov rax, qword ptr [rbp + 0x1a0]
00578EF9  8A 40 25                        mov al, byte ptr [rax + 0x25]
00578EFC  24 03                           and al, 3
00578EFE  41 3A C7                        cmp al, r15b
00578F01  40 8A C7                        mov al, dil
00578F04  0F 94 C1                        sete cl
00578F07  24 18                           and al, 0x18
00578F09  3C 18                           cmp al, 0x18
00578F0B  0F 94 C0                        sete al
00578F0E  84 C8                           test al, cl
00578F10  74 34                           je 0x140578f46
00578F12  48 8D 05 07 72 F1 FF            lea rax, [rip - 0xe8df9]
00578F19  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
00578F20  45 8D 5F 43                     lea r11d, [r15 + 0x43]
00578F24  48 8D 05 D5 15 EF FF            lea rax, [rip - 0x10ea2b]
00578F2B  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
00578F2F  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00578F36  48 8D 05 D3 99 FF FF            lea rax, [rip - 0x662d]
00578F3D  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00578F44  EB 04                           jmp 0x140578f4a
00578F46  44 8B 5D 94                     mov r11d, dword ptr [rbp - 0x6c]
00578F4A  80 BD A8 01 00 00 02            cmp byte ptr [rbp + 0x1a8], 2
00578F51  41 B8 00 01 00 00               mov r8d, 0x100
00578F57  0F 85 B6 00 00 00               jne 0x140579013
00578F5D  40 F6 C7 02                     test dil, 2
00578F61  0F 84 AC 00 00 00               je 0x140579013
00578F67  84 DB                           test bl, bl
00578F69  0F 88 A4 00 00 00               js 0x140579013
00578F6F  83 E2 1F                        and edx, 0x1f
00578F72  0F 95 C1                        setne cl
00578F75  40 F6 C7 40                     test dil, 0x40
00578F79  0F 95 C0                        setne al
00578F7C  84 C8                           test al, cl
00578F7E  0F 84 8F 00 00 00               je 0x140579013
00578F84  48 0F BA E3 37                  bt rbx, 0x37
00578F89  0F 83 84 00 00 00               jae 0x140579013
00578F8F  48 0F BA E3 36                  bt rbx, 0x36
00578F94  73 7D                           jae 0x140579013
00578F96  44 8B B5 B0 01 00 00            mov r14d, dword ptr [rbp + 0x1b0]
00578F9D  F6 C3 10                        test bl, 0x10
00578FA0  75 78                           jne 0x14057901a
00578FA2  48 8D 05 77 84 FF FF            lea rax, [rip - 0x7b89]
00578FA9  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00578FAE  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00578FB5  48 8D 05 94 55 F2 FF            lea rax, [rip - 0xdaa6c]
00578FBC  48 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], rax
00578FC3  48 8D 05 86 55 F2 FF            lea rax, [rip - 0xdaa7a]
00578FCA  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00578FD1  48 8D 05 68 5D FF FF            lea rax, [rip - 0xa298]
00578FD8  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00578FDF  48 8D 05 BA 63 FF FF            lea rax, [rip - 0x9c46]
00578FE6  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00578FED  48 8D 05 AC 9D 5E 00            lea rax, [rip + 0x5e9dac]
00578FF4  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00578FFB  48 0F BD C2                     bsr rax, rdx
00578FFF  C1 E0 0D                        shl eax, 0xd
00579002  05 00 20 00 00                  add eax, 0x2000
00579007  41 0B C0                        or eax, r8d
0057900A  44 0B D8                        or r11d, eax
0057900D  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
00579011  EB 07                           jmp 0x14057901a
00579013  44 8B B5 B0 01 00 00            mov r14d, dword ptr [rbp + 0x1b0]
0057901A  45 85 D8                        test r8d, r11d
0057901D  74 1F                           je 0x14057903e
0057901F  48 B9 00 00 00 00 00 48 02 00   movabs rcx, 0x2480000000000
00579029  40 0F B6 F6                     movzx esi, sil
0057902D  48 8B C7                        mov rax, rdi
00579030  48 23 C1                        and rax, rcx
00579033  48 3B C1                        cmp rax, rcx
00579036  41 0F 44 F7                     cmove esi, r15d
0057903A  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
0057903E  33 D2                           xor edx, edx
00579040  49 8B CD                        mov rcx, r13
00579043  E8 F8 16 00 00                  call 0x14057a740
00579048  33 D2                           xor edx, edx
0057904A  40 84 F6                        test sil, sil
0057904D  75 71                           jne 0x1405790c0
0057904F  48 85 C0                        test rax, rax
00579052  74 59                           je 0x1405790ad
00579054  44 38 38                        cmp byte ptr [rax], r15b
00579057  75 54                           jne 0x1405790ad
00579059  80 78 01 08                     cmp byte ptr [rax + 1], 8
0057905D  75 4E                           jne 0x1405790ad
0057905F  38 50 05                        cmp byte ptr [rax + 5], dl
00579062  75 49                           jne 0x1405790ad
00579064  80 78 06 02                     cmp byte ptr [rax + 6], 2
00579068  75 43                           jne 0x1405790ad
0057906A  38 50 07                        cmp byte ptr [rax + 7], dl
0057906D  75 3E                           jne 0x1405790ad
0057906F  66 41 39 55 06                  cmp word ptr [r13 + 6], dx
00579074  75 37                           jne 0x1405790ad
00579076  48 8B C3                        mov rax, rbx
00579079  25 00 00 3F 00                  and eax, 0x3f0000
0057907E  48 3D 00 00 2F 00               cmp rax, 0x2f0000
00579084  73 27                           jae 0x1405790ad
00579086  38 15 D4 88 A4 00               cmp byte ptr [rip + 0xa488d4], dl
0057908C  75 09                           jne 0x140579097
0057908E  41 0F BA F3 08                  btr r11d, 8
00579093  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
00579097  45 85 F6                        test r14d, r14d
0057909A  75 07                           jne 0x1405790a3
0057909C  48 0F BA E3 22                  bt rbx, 0x22
005790A1  EB 05                           jmp 0x1405790a8
005790A3  48 0F BA E3 23                  bt rbx, 0x23
005790A8  73 03                           jae 0x1405790ad
005790AA  45 8A E7                        mov r12b, r15b
005790AD  41 84 FF                        test r15b, dil
005790B0  0F 84 EF 00 00 00               je 0x1405791a5
005790B6  41 0F BA EB 0B                  bts r11d, 0xb
005790BB  E9 E1 00 00 00                  jmp 0x1405791a1
005790C0  48 0F BA E7 30                  bt rdi, 0x30
005790C5  73 09                           jae 0x1405790d0
005790C7  41 0F BA EB 0B                  bts r11d, 0xb
005790CC  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
005790D0  48 B9 04 00 00 24 02 05 01 00   movabs rcx, 0x1050224000004
005790DA  48 8B C7                        mov rax, rdi
005790DD  48 23 C1                        and rax, rcx
005790E0  48 3B C1                        cmp rax, rcx
005790E3  0F 85 89 00 00 00               jne 0x140579172
005790E9  41 83 CB 20                     or r11d, 0x20
005790ED  48 0F BA E7 1F                  bt rdi, 0x1f
005790F2  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
005790F6  73 09                           jae 0x140579101
005790F8  41 0F BA EB 10                  bts r11d, 0x10
005790FD  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
00579101  48 8D 05 F8 94 FF FF            lea rax, [rip - 0x6b08]
00579108  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0057910C  48 8D 05 9D 8E FF FF            lea rax, [rip - 0x7163]
00579113  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0057911A  48 8D 05 BF 8D FF FF            lea rax, [rip - 0x7241]
00579121  48 89 45 00                     mov qword ptr [rbp], rax
00579125  48 8D 05 74 8B FF FF            lea rax, [rip - 0x748c]
0057912C  48 89 45 08                     mov qword ptr [rbp + 8], rax
00579130  48 8D 05 99 8E FF FF            lea rax, [rip - 0x7167]
00579137  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0057913B  48 8D 05 9E 62 FF FF            lea rax, [rip - 0x9d62]
00579142  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00579146  48 8D 05 33 6A FF FF            lea rax, [rip - 0x95cd]
0057914D  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00579151  48 8D 05 48 9A 5E 00            lea rax, [rip + 0x5e9a48]
00579158  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0057915C  48 8D 05 4D 63 FF FF            lea rax, [rip - 0x9cb3]
00579163  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00579167  48 8D 05 42 5F FF FF            lea rax, [rip - 0xa0be]
0057916E  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00579172  40 F6 C7 04                     test dil, 4
00579176  74 2D                           je 0x1405791a5
00579178  48 8D 05 F1 80 FF FF            lea rax, [rip - 0x7f0f]
0057917F  41 0F BA EB 0C                  bts r11d, 0xc
00579184  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
0057918B  48 8D 05 0E 83 FF FF            lea rax, [rip - 0x7cf2]
00579192  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00579196  48 8D 05 03 66 FF FF            lea rax, [rip - 0x99fd]
0057919D  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
005791A1  44 89 5D 94                     mov dword ptr [rbp - 0x6c], r11d
005791A5  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
005791AA  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
005791AF  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
005791B3  4C 8D 44 24 4C                  lea r8, [rsp + 0x4c]
005791B8  41 8A C4                        mov al, r12b
005791BB  8B D3                           mov edx, ebx
005791BD  F6 D8                           neg al
005791BF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005791C4  48 1B C9                        sbb rcx, rcx
005791C7  83 E2 07                        and edx, 7
005791CA  48 23 C8                        and rcx, rax
005791CD  48 8D 45 DC                     lea rax, [rbp - 0x24]
005791D1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005791D6  48 8D 85 B8 01 00 00            lea rax, [rbp + 0x1b8]
005791DD  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
005791E2  49 8B CF                        mov rcx, r15
005791E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005791EA  E8 E9 0A 00 00                  call 0x140579cd8
005791EF  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
005791F2  40 F6 C6 20                     test sil, 0x20
005791F6  75 06                           jne 0x1405791fe
005791F8  0F BA E6 08                     bt esi, 8
005791FC  73 32                           jae 0x140579230
005791FE  48 8D 05 6B 8D 5E 00            lea rax, [rip + 0x5e8d6b]
00579205  83 CE 12                        or esi, 0x12
00579208  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0057920C  48 8D 05 1D 4B 19 00            lea rax, [rip + 0x194b1d]
00579213  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00579217  48 8D 05 E2 6C FF FF            lea rax, [rip - 0x931e]
0057921E  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00579222  48 8D 05 C7 9B 5E 00            lea rax, [rip + 0x5e9bc7]
00579229  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0057922D  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00579230  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00579237  49 8B D5                        mov rdx, r13
0057923A  E8 8D 18 00 00                  call 0x14057aacc
0057923F  85 C0                           test eax, eax
00579241  79 22                           jns 0x140579265
00579243  40 F6 C6 20                     test sil, 0x20
00579247  74 1C                           je 0x140579265
00579249  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0057924F  45 33 C9                        xor r9d, r9d
00579252  BA 00 05 00 00                  mov edx, 0x500
00579257  41 8D 49 5C                     lea ecx, [r9 + 0x5c]
0057925B  45 8D 41 03                     lea r8d, [r9 + 3]
0057925F  E8 FC 43 F8 FF                  call 0x1404fd660
00579264  CC                              int3
00579265  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
0057926A  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0057926E  E8 79 81 6A 00                  call 0x140c213ec
00579273  44 8B F0                        mov r14d, eax
00579276  85 C0                           test eax, eax
00579278  0F 88 23 01 00 00               js 0x1405793a1
0057927E  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00579282  BA 01 00 00 00                  mov edx, 1
00579287  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0057928C  48 89 06                        mov qword ptr [rsi], rax
0057928F  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
00579294  89 86 FC 00 00 00               mov dword ptr [rsi + 0xfc], eax
0057929A  48 8D 86 70 01 00 00            lea rax, [rsi + 0x170]
005792A1  48 89 9E D8 00 00 00            mov qword ptr [rsi + 0xd8], rbx
005792A8  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
005792AC  48 89 BE E0 00 00 00            mov qword ptr [rsi + 0xe0], rdi
005792B3  33 FF                           xor edi, edi
005792B5  48 89 86 18 01 00 00            mov qword ptr [rsi + 0x118], rax
005792BC  89 9E 00 01 00 00               mov dword ptr [rsi + 0x100], ebx
005792C2  41 8A 45 04                     mov al, byte ptr [r13 + 4]
005792C6  22 C2                           and al, dl
005792C8  88 86 0C 01 00 00               mov byte ptr [rsi + 0x10c], al
005792CE  8B 85 B8 01 00 00               mov eax, dword ptr [rbp + 0x1b8]
005792D4  89 86 04 01 00 00               mov dword ptr [rsi + 0x104], eax
005792DA  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
005792DE  89 86 08 01 00 00               mov dword ptr [rsi + 0x108], eax
005792E4  8B 85 B0 01 00 00               mov eax, dword ptr [rbp + 0x1b0]
005792EA  89 86 F8 00 00 00               mov dword ptr [rsi + 0xf8], eax
005792F0  48 8D 86 E8 00 00 00            lea rax, [rsi + 0xe8]
005792F7  48 89 BE D0 00 00 00            mov qword ptr [rsi + 0xd0], rdi
005792FE  48 89 40 08                     mov qword ptr [rax + 8], rax
00579302  48 89 00                        mov qword ptr [rax], rax
00579305  48 8D 46 38                     lea rax, [rsi + 0x38]
00579309  48 89 40 08                     mov qword ptr [rax + 8], rax
0057930D  48 89 00                        mov qword ptr [rax], rax
00579310  48 8D 46 48                     lea rax, [rsi + 0x48]
00579314  48 89 40 08                     mov qword ptr [rax + 8], rax
00579318  48 89 00                        mov qword ptr [rax], rax
0057931B  48 8D 46 58                     lea rax, [rsi + 0x58]
0057931F  48 89 40 08                     mov qword ptr [rax + 8], rax
00579323  48 89 00                        mov qword ptr [rax], rax
00579326  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00579329  0F BA E0 08                     bt eax, 8
0057932D  73 06                           jae 0x140579335
0057932F  88 96 3E 01 00 00               mov byte ptr [rsi + 0x13e], dl
00579335  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00579339  88 8E 40 01 00 00               mov byte ptr [rsi + 0x140], cl
0057933F  A8 20                           test al, 0x20
00579341  74 06                           je 0x140579349
00579343  88 96 3C 01 00 00               mov byte ptr [rsi + 0x13c], dl
00579349  0F BA E0 0C                     bt eax, 0xc
0057934D  73 06                           jae 0x140579355
0057934F  88 96 3D 01 00 00               mov byte ptr [rsi + 0x13d], dl
00579355  45 84 E4                        test r12b, r12b
00579358  74 06                           je 0x140579360
0057935A  88 96 3F 01 00 00               mov byte ptr [rsi + 0x13f], dl
00579360  0F B6 86 E0 00 00 00            movzx eax, byte ptr [rsi + 0xe0]
00579367  48 8B CE                        mov rcx, rsi
0057936A  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
0057936F  23 C2                           and eax, edx
00579371  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
00579375  89 86 10 01 00 00               mov dword ptr [rsi + 0x110], eax
0057937B  4C 89 BE 58 01 00 00            mov qword ptr [rsi + 0x158], r15
00579382  E8 29 0C 00 00                  call 0x140579fb0
00579387  44 8B F0                        mov r14d, eax
0057938A  85 C0                           test eax, eax
0057938C  78 13                           js 0x1405793a1
0057938E  48 8B 8E 18 01 00 00            mov rcx, qword ptr [rsi + 0x118]
00579395  49 8D 55 10                     lea rdx, [r13 + 0x10]
00579399  4C 8B C3                        mov r8, rbx
0057939C  E8 9F D4 14 00                  call 0x1406c6840
005793A1  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005793A6  45 33 C0                        xor r8d, r8d
005793A9  41 8D 50 01                     lea edx, [r8 + 1]
005793AD  E8 7E F8 E7 FF                  call 0x1403f8c30
005793B2  45 85 F6                        test r14d, r14d
005793B5  79 15                           jns 0x1405793cc
005793B7  4D 85 FF                        test r15, r15
005793BA  74 10                           je 0x1405793cc
005793BC  49 8B CF                        mov rcx, r15
005793BF  E8 54 19 00 00                  call 0x14057ad18
005793C4  49 8B D7                        mov rdx, r15
005793C7  E8 54 7F FE FF                  call 0x140561320
005793CC  41 8B C6                        mov eax, r14d
005793CF  48 81 C4 58 02 00 00            add rsp, 0x258
005793D6  41 5F                           pop r15
005793D8  41 5E                           pop r14
005793DA  41 5D                           pop r13
005793DC  41 5C                           pop r12
005793DE  5F                              pop rdi
005793DF  5E                              pop rsi
005793E0  5B                              pop rbx
005793E1  5D                              pop rbp
005793E2  C3                              ret
005793E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIvtLegacyProcessDrhdEntry(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
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
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m24C;
    unsigned int v_stack_m250;
    unsigned int v_stack_m254;
    unsigned int v_stack_m258;
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
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (600);
    v_rdi = 0;
    v_stack_p20 = 0;
    a2 = 0;
    v_stack_p10 = 0;
    v_stack_m230 = v_xmm0;
    result = memset(v_stack_mE8, a2, 152, a4);
    a2 = 0;
    result = memset(v_stack_m1A8, a2, 184, a4);
    v_stack_m238 = 0;
    v_stack_m254 = 0;
    v_stack_m250 = 0;
    v_stack_m24C = 0;
    v_stack_p18 = 0;
    v_stack_m248 = 0;
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_00578CF1;
    goto loc_005793CC;
loc_00578CF1:
    if ((*(unsigned __int16 *)(a2 + 2)) >= 16) goto loc_00578D08;
    goto loc_005793CC;
loc_00578D08:
    if ((*(unsigned __int64 *)(a2 + 8)) == 0) goto loc_005793CC;
    a2 = 0;
    v_stack_m278 = v_stack_m230;
    result = HalSocRequestApi(16, a2, a2 + 2, 16);
    if (sign_flag) goto loc_00578D4A;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = guard_dispatch_icall(a1, a2, a3, v_stack_p10);
    if ((unsigned __int8)(result) == 0) {
        v_stack_p10 = 0;
    }
    result = ExtEnvAllocateMemory(a1, 24, v_stack_m248, v_stack_p10);
    if (sign_flag) goto loc_005793B7;
    result = DmrEnumerateRmrrDomains(0, a2 + 4, v_stack_m248, v_stack_p10);
    if (sign_flag) goto loc_005793B7;
    a2 = 0;
    result = memset(v_stack_m218, a2, 104, v_stack_p10);
    v_stack_m214 = 104;
    v_stack_m218 = (unsigned int)(104 - 103);
    a3 = 0;
    result = HalMapIoSpace(*(unsigned __int64 *)(a2 + 8), 544, a3, v_stack_p10);
    v_stack_m230 = result;
    if (result != 0) goto loc_00578DD3;
    goto loc_005793B7;
loc_00578DD3:
    result = HalRegisterPermanentAddressUsage(*(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a3, v_stack_p10);
    if (sign_flag) goto loc_005793A1;
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 2)) - (16));
    v_stack_m240 = (unsigned int)(result);
    result = (unsigned int)((result) + (368));
    v_stack_m208 = (unsigned int)(result);
    v_stack_m1E0 = v_stack_mE8;
    v_stack_m1D8 = v_stack_m1A8;
    v_stack_mE8 = v_rip + 6197534;
    v_stack_mE0 = v_rip + 6197680;
    v_stack_mD8 = v_rip - 42382;
    v_stack_mD0 = v_rip - 38252;
    v_stack_mC8 = v_rip + 3974;
    v_stack_mC0 = v_rip + 4200;
    v_stack_m140 = v_rip + 1658682;
    v_stack_m1A8 = v_rip + 4239;
    v_stack_m120 = v_rip + 4836;
    v_stack_m1CC = (unsigned int)(*(unsigned __int16 *)(a2 + 6));
    v_rbx = (*(unsigned __int64 *)(v_stack_m230 + 8)) & (0xFFFFFFFFFFFFEEFFULL);
    v_stack_m210 = 0;
    a2 = (v_rbx) >> (8);
    a1 = (*(unsigned __int64 *)(v_stack_m230 + 16)) >> (35);
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    v_stack_m1D0 = 2;
    a1 = (unsigned __int8)((a1) & (31));
    v_stack_m204 = 4;
    v_stack_p18 = (unsigned int)(result);
    a1 = (unsigned __int8)((a1) + (1));
    result = (1) << ((unsigned __int8)(a1));
    if (result > ((unsigned int)(0x100000ULL))) { result = (unsigned int)(0x100000ULL); }
    v_stack_m1C0 = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 37)) & (3));
    a1 = (((unsigned __int8)(result)) == 1) ? 1 : 0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_m230 + 16))) & (24));
    result = (((unsigned __int8)(result)) == 24) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00578F46;
    v_stack_m70 = v_rip - 953849;
    v_stack_m204 = (unsigned int)(1 + 67);
    v_stack_m68 = v_rip - 1108523;
    v_stack_m60 = v_rip - 26157;
    goto loc_00578F4A;
loc_00578F46:
loc_00578F4A:
    if (v_stack_p10 != 2) goto loc_00579013;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m230 + 16))) & (2)) == 0) goto loc_00579013;
    if (sign_flag) goto loc_00579013;
    a2 = (unsigned int)((a2) & (31));
    a1 = (condition_is_not_equal) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m230 + 16))) & (64)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00579013;
    if (condition_is_above_or_equal) goto loc_00579013;
    if (condition_is_above_or_equal) goto loc_00579013;
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_0057901A;
    v_stack_m258 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m98 = v_rip - 31625;
    v_stack_m90 = v_rip - 895596;
    v_stack_m88 = v_rip - 895610;
    v_stack_mA8 = v_rip - 41624;
    v_stack_mA0 = v_rip - 40006;
    v_stack_m118 = v_rip + 6200748;
    result = (unsigned int)((v_rip + 6200748) << (13));
    result = (unsigned int)((result) + (0x2000ULL));
    result = (unsigned int)((result) | (256));
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m204)) | ((unsigned int)(result)));
    v_stack_m204 = (unsigned int)(v_r11);
    goto loc_0057901A;
loc_00579013:
loc_0057901A:
    v_rsi = 0;
    if (((256) & ((unsigned int)(v_r11))) != 0) {
        v_rsi = 0;
        result = *(unsigned __int64 *)(v_stack_m230 + 16);
        result = (result) & (a1);
        if (result == a1) { v_rsi = 1; }
        v_stack_m254 = (unsigned int)(v_rsi);
    }
    a2 = 0;
    result = DmrGetNextDrhdDeviceScope(0, a2, 256, v_stack_p10);
    a2 = 0;
    if ((unsigned __int8)(v_rsi) != 0) goto loc_005790C0;
    if (result == 0) goto loc_005790AD;
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_005790AD;
    if ((*(unsigned __int8 *)(result + 1)) != 8) goto loc_005790AD;
    if ((*(unsigned __int8 *)(result + 5)) != 0) goto loc_005790AD;
    if ((*(unsigned __int8 *)(result + 6)) != 2) goto loc_005790AD;
    if ((*(unsigned __int8 *)(result + 7)) != 0) goto loc_005790AD;
    if ((*(unsigned __int16 *)(a2 + 6)) != 0) goto loc_005790AD;
    result = (unsigned int)((v_rbx) & (0x3F0000ULL));
    if (result >= 0x2F0000ULL) goto loc_005790AD;
    if ((*(unsigned __int8 *)(v_rip + 10782932)) == 0) {
        v_stack_m204 = (unsigned int)(v_r11);
    }
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_005790A3;
    goto loc_005790A8;
loc_005790A3:
loc_005790A8:
    v_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        v_r12 = 1;
    }
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m230 + 16)))) == 0) goto loc_005791A5;
    goto loc_005791A1;
loc_005790C0:
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (unsigned int)(v_r11);
    }
    result = (*(unsigned __int64 *)(v_stack_m230 + 16)) & (0);
    if (result != 0) goto loc_00579172;
    v_r11 = (unsigned int)((v_r11) | (32));
    v_stack_m204 = (unsigned int)(v_r11);
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (unsigned int)(v_r11);
    }
    v_stack_m1A0 = v_rip - 27400;
    v_stack_mF8 = v_rip - 29027;
    v_stack_m198 = v_rip - 29249;
    v_stack_m190 = v_rip - 29836;
    v_stack_m188 = v_rip - 29031;
    v_stack_m170 = v_rip - 40290;
    v_stack_m168 = v_rip - 38349;
    v_stack_m138 = v_rip + 6199880;
    v_stack_m130 = v_rip - 40115;
    v_stack_m128 = v_rip - 41150;
loc_00579172:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m230 + 16))) & (4)) == 0) goto loc_005791A5;
    v_stack_m100 = v_rip - 32527;
    v_stack_m180 = v_rip - 31986;
    v_stack_m178 = v_rip - 39421;
loc_005791A1:
    v_stack_m204 = (unsigned int)(v_r11);
loc_005791A5:
    v_stack_m258 = 0;
    result = (unsigned __int8)(-((unsigned __int8)(v_r12)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (7));
    a1 = (0) & (v_stack_m258);
    v_stack_m268 = v_stack_m1BC;
    v_stack_m270 = a1;
    v_stack_m278 = v_stack_p20;
    result = HalpIvtReserveDomainIds(v_stack_m248, a2, v_stack_m24C, v_stack_m250);
    if ((((unsigned __int8)((unsigned int)(v_stack_m204))) & (32)) != 0) goto loc_005791FE;
    v_rsi = (unsigned int)(v_stack_m204);
    if (!(condition_is_above_or_equal)) {
        result = v_rip + 6196587;
        v_rsi = (unsigned int)(((unsigned int)(v_stack_m204)) | (18));
        v_stack_m158 = result;
        result = v_rip + 1657629;
        v_stack_m150 = result;
        result = v_rip - 37662;
        v_stack_m148 = result;
        result = v_rip + 6200263;
        v_stack_m160 = result;
        v_stack_m204 = (unsigned int)(v_rsi);
    }
    result = DmrValidateDeviceScope(v_stack_p8, a2, v_stack_m24C, v_stack_m250);
    if (!sign_flag) goto loc_00579265;
    if ((((unsigned __int8)(v_rsi)) & (32)) != 0) {
        a4 = 0;
        a2 = 0x500ULL;
        a1 = a4 + 92;
        a3 = a4 + 3;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ExtEnvRegisterIommu(v_stack_m218, a2, v_stack_m238, a4);
    if (sign_flag) goto loc_005793A1;
    *(unsigned __int64 *)(v_stack_m238) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned int *)(v_stack_m238 + 252) = (unsigned int)(*(unsigned __int16 *)(a2 + 6));
    *(unsigned __int64 *)(v_stack_m238 + 216) = v_rbx;
    *(unsigned __int64 *)(v_stack_m238 + 224) = *(unsigned __int64 *)(v_stack_m230 + 16);
    v_rdi = 0;
    *(unsigned __int64 *)(v_stack_m238 + 280) = v_stack_m238 + 368;
    *(unsigned int *)(v_stack_m238 + 256) = (unsigned int)((unsigned int)(v_stack_m240));
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 4)) & (1));
    *(unsigned __int8 *)(v_stack_m238 + 268) = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m238 + 260) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned int *)(v_stack_m238 + 264) = (unsigned int)((unsigned int)(v_stack_m258));
    *(unsigned int *)(v_stack_m238 + 248) = (unsigned int)((unsigned int)(v_stack_p18));
    *(unsigned __int64 *)(v_stack_m238 + 208) = 0;
    *(unsigned __int64 *)(v_stack_m238 + 232 + 8) = v_stack_m238 + 232;
    *(unsigned __int64 *)(v_stack_m238 + 232) = v_stack_m238 + 232;
    *(unsigned __int64 *)(v_stack_m238 + 56 + 8) = v_stack_m238 + 56;
    *(unsigned __int64 *)(v_stack_m238 + 56) = v_stack_m238 + 56;
    *(unsigned __int64 *)(v_stack_m238 + 72 + 8) = v_stack_m238 + 72;
    *(unsigned __int64 *)(v_stack_m238 + 72) = v_stack_m238 + 72;
    *(unsigned __int64 *)(v_stack_m238 + 88 + 8) = v_stack_m238 + 88;
    *(unsigned __int64 *)(v_stack_m238 + 88) = v_stack_m238 + 88;
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_stack_m238 + 318) = 1;
    }
    *(unsigned __int8 *)(v_stack_m238 + 320) = (unsigned __int8)((unsigned int)(v_stack_m254));
    if ((((unsigned __int8)((unsigned int)(v_stack_m204))) & (32)) != 0) {
        *(unsigned __int8 *)(v_stack_m238 + 316) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_stack_m238 + 317) = 1;
    }
    if ((unsigned __int8)(v_r12) != 0) {
        *(unsigned __int8 *)(v_stack_m238 + 319) = 1;
    }
    result = (unsigned int)((*(unsigned __int8 *)(v_stack_m238 + 224)) & (1));
    *(unsigned int *)(v_stack_m238 + 272) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m238 + 344) = v_stack_m248;
    result = HalpIvtAllocateReservedDomainList(v_stack_m238, (unsigned int)(v_stack_m24C), (unsigned int)(v_stack_m250), a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_stack_m238 + 280);
        a2 = a2 + 16;
        a3 = (unsigned int)(v_stack_m240);
        result = memcpy(a1, a2, a3, a4);
    }
    a3 = 0;
    result = HalpUnmapVirtualAddress(v_stack_m230, a3 + 1, a3, a4);
    if (!sign_flag) goto loc_005793CC;
loc_005793B7:
    if (v_stack_m248 != 0) {
        a1 = v_stack_m248;
        result = DmrFreeRmrrTree(a1, a3 + 1, a3, a4);
        a2 = v_stack_m248;
        result = ExtEnvFreeMemory(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (600);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HalpIvtLegacyProcessDrhdEntry(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
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
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m24C;
    uint32_t v_stack_m250;
    uint32_t v_stack_m254;
    uint32_t v_stack_m258;
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
    uint64_t v_stack_mF8;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (600);
    local_rdi = 0;
    v_stack_p20 = 0;
    Arg2 = 0;
    v_stack_p10 = 0;
    v_stack_m230 = v_xmm0;
    result = memset(v_stack_mE8, Arg2, 152, a4);
    Arg2 = 0;
    result = memset(v_stack_m1A8, Arg2, 184, a4);
    v_stack_m238 = 0;
    v_stack_m254 = 0;
    v_stack_m250 = 0;
    v_stack_m24C = 0;
    v_stack_p18 = 0;
    v_stack_m248 = 0;
    if ((*(uint16_t *)(arg2)) == 0) goto loc_00578CF1;
    goto loc_005793CC;
loc_00578CF1:
    if ((*(uint16_t *)(arg2 + 0x2)) >= 16) goto loc_00578D08;
    goto loc_005793CC;
loc_00578D08:
    if ((*(uint64_t *)(arg2 + 0x8)) == 0) goto loc_005793CC;
    Arg2 = 0;
    v_stack_m278 = v_stack_m230;
    result = HalSocRequestApi(16, Arg2, Arg2 + 2, 16);
    if (sign_flag) goto loc_00578D4A;
    a3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, Arg2, a3, v_stack_p10);
    if ((uint8_t)(result) == 0) {
        v_stack_p10 = 0;
    }
    result = ExtEnvAllocateMemory(Arg1, 24, v_stack_m248, v_stack_p10);
    if (sign_flag) goto loc_005793B7;
    result = DmrEnumerateRmrrDomains(0, Arg2 + 4, v_stack_m248, v_stack_p10);
    if (sign_flag) goto loc_005793B7;
    Arg2 = 0;
    result = memset(v_stack_m218, Arg2, 104, v_stack_p10);
    v_stack_m214 = 104;
    v_stack_m218 = (uint32_t)(104 - 103);
    a3 = 0;
    result = HalMapIoSpace(*(uint64_t *)(arg2 + 0x8), 544, a3, v_stack_p10);
    v_stack_m230 = result;
    if (result != 0) goto loc_00578DD3;
    goto loc_005793B7;
loc_00578DD3:
    result = HalRegisterPermanentAddressUsage(*(uint64_t *)(arg2 + 0x8), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a3, v_stack_p10);
    if (sign_flag) goto loc_005793A1;
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x2)) - (16));
    v_stack_m240 = (uint32_t)(result);
    result = (uint32_t)((result) + (368));
    v_stack_m208 = (uint32_t)(result);
    v_stack_m1E0 = v_stack_mE8;
    v_stack_m1D8 = v_stack_m1A8;
    v_stack_mE8 = v_rip + 6197534;
    v_stack_mE0 = v_rip + 6197680;
    v_stack_mD8 = v_rip - 42382;
    v_stack_mD0 = v_rip - 38252;
    v_stack_mC8 = v_rip + 3974;
    v_stack_mC0 = v_rip + 4200;
    v_stack_m140 = v_rip + 1658682;
    v_stack_m1A8 = v_rip + 4239;
    v_stack_m120 = v_rip + 4836;
    v_stack_m1CC = (uint32_t)(*(uint16_t *)(arg2 + 0x6));
    local_rbx = (*(uint64_t *)(v_stack_m230 + 0x8)) & (0xFFFFFFFFFFFFEEFFULL);
    v_stack_m210 = 0;
    Arg2 = (local_rbx) >> (8);
    Arg1 = (*(uint64_t *)(v_stack_m230 + 0x10)) >> (35);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    v_stack_m1D0 = 2;
    Arg1 = (uint8_t)((Arg1) & (31));
    v_stack_m204 = 4;
    v_stack_p18 = (uint32_t)(result);
    Arg1 = (uint8_t)((Arg1) + (1));
    result = (1) << ((uint8_t)(Arg1));
    if (result > ((uint32_t)(0x100000ULL))) { result = (uint32_t)(0x100000ULL); }
    v_stack_m1C0 = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x25)) & (3));
    Arg1 = (((uint8_t)(result)) == 1) ? 1 : 0;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_m230 + 0x10))) & (24));
    result = (((uint8_t)(result)) == 24) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00578F46;
    v_stack_m70 = v_rip - 953849;
    v_stack_m204 = (uint32_t)(1 + 67);
    v_stack_m68 = v_rip - 1108523;
    v_stack_m60 = v_rip - 26157;
    goto loc_00578F4A;
loc_00578F46:
loc_00578F4A:
    if (v_stack_p10 != 2) goto loc_00579013;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m230 + 0x10))) & (2)) == 0) goto loc_00579013;
    if (sign_flag) goto loc_00579013;
    Arg2 = (uint32_t)((Arg2) & (31));
    Arg1 = (condition_is_not_equal) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_m230 + 0x10))) & (64)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00579013;
    if (condition_is_above_or_equal) goto loc_00579013;
    if (condition_is_above_or_equal) goto loc_00579013;
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_0057901A;
    v_stack_m258 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m98 = v_rip - 31625;
    v_stack_m90 = v_rip - 895596;
    v_stack_m88 = v_rip - 895610;
    v_stack_mA8 = v_rip - 41624;
    v_stack_mA0 = v_rip - 40006;
    v_stack_m118 = v_rip + 6200748;
    result = (uint32_t)((v_rip + 6200748) << (13));
    result = (uint32_t)((result) + (0x2000ULL));
    result = (uint32_t)((result) | (256));
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m204)) | ((uint32_t)(result)));
    v_stack_m204 = (uint32_t)(local_r11);
    goto loc_0057901A;
loc_00579013:
loc_0057901A:
    local_rsi = 0;
    if (((256) & ((uint32_t)(local_r11))) != 0) {
        local_rsi = 0;
        result = *(uint64_t *)(v_stack_m230 + 0x10);
        result = (result) & (Arg1);
        if (result == Arg1) { local_rsi = 1; }
        v_stack_m254 = (uint32_t)(local_rsi);
    }
    Arg2 = 0;
    result = DmrGetNextDrhdDeviceScope(0, Arg2, 256, v_stack_p10);
    Arg2 = 0;
    if ((uint8_t)(local_rsi) != 0) goto loc_005790C0;
    if (result == 0) goto loc_005790AD;
    if ((*(uint8_t *)(result)) != 1) goto loc_005790AD;
    if ((*(uint8_t *)(result + 0x1)) != 8) goto loc_005790AD;
    if ((*(uint8_t *)(result + 0x5)) != 0) goto loc_005790AD;
    if ((*(uint8_t *)(result + 0x6)) != 2) goto loc_005790AD;
    if ((*(uint8_t *)(result + 0x7)) != 0) goto loc_005790AD;
    if ((*(uint16_t *)(arg2 + 0x6)) != 0) goto loc_005790AD;
    result = (uint32_t)((local_rbx) & (0x3F0000ULL));
    if (result >= 0x2F0000ULL) goto loc_005790AD;
    if ((*(uint8_t *)(v_rip + 0xA488D4)) == 0) {
        v_stack_m204 = (uint32_t)(local_r11);
    }
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_005790A3;
    goto loc_005790A8;
loc_005790A3:
loc_005790A8:
    local_r12 = 0;
    if (!(condition_is_above_or_equal)) {
        local_r12 = 1;
    }
    if (((1) & ((uint8_t)(*(uint64_t *)(v_stack_m230 + 0x10)))) == 0) goto loc_005791A5;
    goto loc_005791A1;
loc_005790C0:
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (uint32_t)(local_r11);
    }
    result = (*(uint64_t *)(v_stack_m230 + 0x10)) & (0);
    if (result != 0) goto loc_00579172;
    local_r11 = (uint32_t)((local_r11) | (32));
    v_stack_m204 = (uint32_t)(local_r11);
    if (!(condition_is_above_or_equal)) {
        v_stack_m204 = (uint32_t)(local_r11);
    }
    v_stack_m1A0 = v_rip - 27400;
    v_stack_mF8 = v_rip - 29027;
    v_stack_m198 = v_rip - 29249;
    v_stack_m190 = v_rip - 29836;
    v_stack_m188 = v_rip - 29031;
    v_stack_m170 = v_rip - 40290;
    v_stack_m168 = v_rip - 38349;
    v_stack_m138 = v_rip + 6199880;
    v_stack_m130 = v_rip - 40115;
    v_stack_m128 = v_rip - 41150;
loc_00579172:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m230 + 0x10))) & (4)) == 0) goto loc_005791A5;
    v_stack_m100 = v_rip - 32527;
    v_stack_m180 = v_rip - 31986;
    v_stack_m178 = v_rip - 39421;
loc_005791A1:
    v_stack_m204 = (uint32_t)(local_r11);
loc_005791A5:
    v_stack_m258 = 0;
    result = (uint8_t)(-((uint8_t)(local_r12)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (7));
    Arg1 = (0) & (v_stack_m258);
    v_stack_m268 = v_stack_m1BC;
    v_stack_m270 = Arg1;
    v_stack_m278 = v_stack_p20;
    result = HalpIvtReserveDomainIds(v_stack_m248, Arg2, v_stack_m24C, v_stack_m250);
    if ((((uint8_t)((uint32_t)(v_stack_m204))) & (32)) != 0) goto loc_005791FE;
    local_rsi = (uint32_t)(v_stack_m204);
    if (!(condition_is_above_or_equal)) {
        result = v_rip + 6196587;
        local_rsi = (uint32_t)(((uint32_t)(v_stack_m204)) | (18));
        v_stack_m158 = result;
        result = v_rip + 1657629;
        v_stack_m150 = result;
        result = v_rip - 37662;
        v_stack_m148 = result;
        result = v_rip + 6200263;
        v_stack_m160 = result;
        v_stack_m204 = (uint32_t)(local_rsi);
    }
    result = DmrValidateDeviceScope(v_stack_p8, Arg2, v_stack_m24C, v_stack_m250);
    if (!sign_flag) goto loc_00579265;
    if ((((uint8_t)(local_rsi)) & (32)) != 0) {
        a4 = 0;
        Arg2 = 0x500ULL;
        Arg1 = a4 + 92;
        a3 = a4 + 3;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = ExtEnvRegisterIommu(v_stack_m218, Arg2, v_stack_m238, a4);
    if (sign_flag) goto loc_005793A1;
    *(uint64_t *)(v_stack_m238) = *(uint64_t *)(arg2 + 0x8);
    *(uint32_t *)(v_stack_m238 + 0xFC) = (uint32_t)(*(uint16_t *)(arg2 + 0x6));
    *(uint64_t *)(v_stack_m238 + 0xD8) = local_rbx;
    *(uint64_t *)(v_stack_m238 + 0xE0) = *(uint64_t *)(v_stack_m230 + 0x10);
    local_rdi = 0;
    *(uint64_t *)(v_stack_m238 + 0x118) = v_stack_m238 + 368;
    *(uint32_t *)(v_stack_m238 + 0x100) = (uint32_t)((uint32_t)(v_stack_m240));
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x4)) & (1));
    *(uint8_t *)(v_stack_m238 + 0x10C) = (uint8_t)(result);
    *(uint32_t *)(v_stack_m238 + 0x104) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint32_t *)(v_stack_m238 + 0x108) = (uint32_t)((uint32_t)(v_stack_m258));
    *(uint32_t *)(v_stack_m238 + 0xF8) = (uint32_t)((uint32_t)(v_stack_p18));
    *(uint64_t *)(v_stack_m238 + 0xD0) = 0;
    *(uint64_t *)(v_stack_m238 + 0xE8 + 0x8) = v_stack_m238 + 232;
    *(uint64_t *)(v_stack_m238 + 0xE8) = v_stack_m238 + 232;
    *(uint64_t *)(v_stack_m238 + 0x38 + 0x8) = v_stack_m238 + 56;
    *(uint64_t *)(v_stack_m238 + 0x38) = v_stack_m238 + 56;
    *(uint64_t *)(v_stack_m238 + 0x48 + 0x8) = v_stack_m238 + 72;
    *(uint64_t *)(v_stack_m238 + 0x48) = v_stack_m238 + 72;
    *(uint64_t *)(v_stack_m238 + 0x58 + 0x8) = v_stack_m238 + 88;
    *(uint64_t *)(v_stack_m238 + 0x58) = v_stack_m238 + 88;
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_stack_m238 + 0x13E) = 1;
    }
    *(uint8_t *)(v_stack_m238 + 0x140) = (uint8_t)((uint32_t)(v_stack_m254));
    if ((((uint8_t)((uint32_t)(v_stack_m204))) & (32)) != 0) {
        *(uint8_t *)(v_stack_m238 + 0x13C) = 1;
    }
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_stack_m238 + 0x13D) = 1;
    }
    if ((uint8_t)(local_r12) != 0) {
        *(uint8_t *)(v_stack_m238 + 0x13F) = 1;
    }
    result = (uint32_t)((*(uint8_t *)(v_stack_m238 + 0xE0)) & (1));
    *(uint32_t *)(v_stack_m238 + 0x110) = (uint32_t)(result);
    *(uint64_t *)(v_stack_m238 + 0x158) = v_stack_m248;
    result = HalpIvtAllocateReservedDomainList(v_stack_m238, (uint32_t)(v_stack_m24C), (uint32_t)(v_stack_m250), a4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(v_stack_m238 + 0x118);
        Arg2 = Arg2 + 16;
        a3 = (uint32_t)(v_stack_m240);
        result = memcpy(Arg1, Arg2, a3, a4);
    }
    a3 = 0;
    result = HalpUnmapVirtualAddress(v_stack_m230, a3 + 1, a3, a4);
    if (!sign_flag) goto loc_005793CC;
loc_005793B7:
    if (v_stack_m248 != 0) {
        Arg1 = v_stack_m248;
        result = DmrFreeRmrrTree(Arg1, a3 + 1, a3, a4);
        Arg2 = v_stack_m248;
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
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x4` | `64` | `R` |
| `Arg2` | `+ 0x6` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00578C58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
