# IommupDomainAttachPasidDevice

- RVA: `0x0054F984`–`0x0054FD47` (길이 `963` bytes)
- VA: `0x000000014054F984`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4194`
- 디코드: `266`개 명령, `963/963` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0054F9FA` → [Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline](Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline_function_0054EB38.md) (function, `0x0054EB38`)
- `0x0054FA44` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x0054FA64` → [HalpIommuGetDmarptRootAddress](../56/HalpIommuGetDmarptRootAddress_function_00568EC0.md) (function, `0x00568EC0`)
- `0x0054FAA7` → [HalpIommuGetHardwareDomain](../4D/HalpIommuGetHardwareDomain_function_004D7BCC.md) (function, `0x004D7BCC`)
- `0x0054FAD0` → [Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline](Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline_function_0054EB38.md) (function, `0x0054EB38`)
- `0x0054FAE1` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0054FB11` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0054FB24` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x0054FB45` → [IommuEnableDevicePasid](../56/IommuEnableDevicePasid_function_00565150.md) (function, `0x00565150`)
- `0x0054FB70` → [IommupHvAttachPasidDeviceDomain](../56/IommupHvAttachPasidDeviceDomain_function_00566E3C.md) (function, `0x00566E3C`)
- `0x0054FB87` → [Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline](Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline_function_0054EB38.md) (function, `0x0054EB38`)
- `0x0054FB94` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0054FBC2` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0054FBDE` → [IommuSetAddressSpace](../56/IommuSetAddressSpace_function_00566060.md) (function, `0x00566060`)
- `0x0054FBFD` → [IommupHvAttachPasidDeviceDomain](../56/IommupHvAttachPasidDeviceDomain_function_00566E3C.md) (function, `0x00566E3C`)
- `0x0054FC16` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054FC34` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054FC4E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0054FC60` → [Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline](Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline_function_0054EB38.md) (function, `0x0054EB38`)
- `0x0054FC72` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0054FCA1` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0054FCB0` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0054FCD6` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0054FCF5` → [IommupHvDetachPasidDeviceDomain](../56/IommupHvDetachPasidDeviceDomain_function_005671B4.md) (function, `0x005671B4`)
- `0x0054FD02` → [IommupHvDetachPasidDeviceDomain](../56/IommupHvDetachPasidDeviceDomain_function_005671B4.md) (function, `0x005671B4`)
- `0x0054FD17` → [IommuDisableDevicePasid](../56/IommuDisableDevicePasid_function_00564E80.md) (function, `0x00564E80`)
- `0x0054FD27` → [HalpIommuDereferenceHardwareDomain](../55/HalpIommuDereferenceHardwareDomain_function_00554E58.md) (function, `0x00554E58`)

### Direct callers
- [IommuDomainAttachDeviceEx](../56/IommuDomainAttachDeviceEx_function_00567B60.md) at `0x00567C27`
- [IommuDomainAttachPasidDevice](../../page/70/IommuDomainAttachPasidDevice_function_0070D2C0.md) at `0x0070D2FB`

### Static image references
- `0x0054FA6F` → RVA `0x00FC1710` (`.data`; read)
- `0x0054FC0A` → RVA `0x00FC1D90` (`.data`; read)
- `0x0054FC21` → RVA `0x00FC1D70` (`.data`; read)
- `0x0054FC3F` → RVA `0x00FC1D98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054F984  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0054F989  55                              push rbp
0054F98A  56                              push rsi
0054F98B  57                              push rdi
0054F98C  41 54                           push r12
0054F98E  41 55                           push r13
0054F990  41 56                           push r14
0054F992  41 57                           push r15
0054F994  48 83 EC 50                     sub rsp, 0x50
0054F998  4C 8B 72 10                     mov r14, qword ptr [rdx + 0x10]
0054F99C  33 C0                           xor eax, eax
0054F99E  4C 8B 62 38                     mov r12, qword ptr [rdx + 0x38]
0054F9A2  48 8B F2                        mov rsi, rdx
0054F9A5  48 8B E9                        mov rbp, rcx
0054F9A8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0054F9AD  8B F8                           mov edi, eax
0054F9AF  88 84 24 A8 00 00 00            mov byte ptr [rsp + 0xa8], al
0054F9B6  41 83 BE 88 01 00 00 01         cmp dword ptr [r14 + 0x188], 1
0054F9BE  44 8B F8                        mov r15d, eax
0054F9C1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0054F9C6  8A D8                           mov bl, al
0054F9C8  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0054F9CD  44 8B E8                        mov r13d, eax
0054F9D0  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
0054F9D7  88 84 24 98 00 00 00            mov byte ptr [rsp + 0x98], al
0054F9DE  75 0A                           jne 0x14054f9ea
0054F9E0  BF BB 00 00 C0                  mov edi, 0xc00000bb
0054F9E5  E9 E6 00 00 00                  jmp 0x14054fad0
0054F9EA  83 79 08 03                     cmp dword ptr [rcx + 8], 3
0054F9EE  74 0A                           je 0x14054f9fa
0054F9F0  BF EF 00 00 C0                  mov edi, 0xc00000ef
0054F9F5  E9 D6 00 00 00                  jmp 0x14054fad0
0054F9FA  E8 39 F1 FF FF                  call 0x14054eb38
0054F9FF  85 C0                           test eax, eax
0054FA01  75 14                           jne 0x14054fa17
0054FA03  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0054FA07  48 85 C0                        test rax, rax
0054FA0A  74 38                           je 0x14054fa44
0054FA0C  48 3B C5                        cmp rax, rbp
0054FA0F  0F 84 17 03 00 00               je 0x14054fd2c
0054FA15  EB 17                           jmp 0x14054fa2e
0054FA17  4C 8B 6E 18                     mov r13, qword ptr [rsi + 0x18]
0054FA1B  4C 3B ED                        cmp r13, rbp
0054FA1E  0F 84 08 03 00 00               je 0x14054fd2c
0054FA24  4D 85 ED                        test r13, r13
0054FA27  74 1B                           je 0x14054fa44
0054FA29  39 7E 30                        cmp dword ptr [rsi + 0x30], edi
0054FA2C  74 0A                           je 0x14054fa38
0054FA2E  BF 01 00 00 C0                  mov edi, 0xc0000001
0054FA33  E9 98 00 00 00                  jmp 0x14054fad0
0054FA38  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0054FA3C  38 98 11 01 00 00               cmp byte ptr [rax + 0x111], bl
0054FA42  75 EA                           jne 0x14054fa2e
0054FA44  E8 47 81 FA FF                  call 0x1404f7b90
0054FA49  85 C0                           test eax, eax
0054FA4B  74 09                           je 0x14054fa56
0054FA4D  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0054FA51  8B 50 18                        mov edx, dword ptr [rax + 0x18]
0054FA54  EB 05                           jmp 0x14054fa5b
0054FA56  BA 04 00 00 00                  mov edx, 4
0054FA5B  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0054FA5F  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0054FA64  E8 57 94 01 00                  call 0x140568ec0
0054FA69  8B F8                           mov edi, eax
0054FA6B  85 C0                           test eax, eax
0054FA6D  78 61                           js 0x14054fad0
0054FA6F  44 38 3D 9A 1C A7 00            cmp byte ptr [rip + 0xa71c9a], r15b
0054FA76  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0054FA7B  0F 85 DD 00 00 00               jne 0x14054fb5e
0054FA81  49 8B 04 24                     mov rax, qword ptr [r12]
0054FA85  41 B1 01                        mov r9b, 1
0054FA88  45 8A C1                        mov r8b, r9b
0054FA8B  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
0054FA8E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0054FA93  89 4D 30                        mov dword ptr [rbp + 0x30], ecx
0054FA96  48 8B CD                        mov rcx, rbp
0054FA99  49 8B 56 20                     mov rdx, qword ptr [r14 + 0x20]
0054FA9D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0054FAA2  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0054FAA7  E8 20 81 F8 FF                  call 0x1404d7bcc
0054FAAC  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0054FAB1  8B F8                           mov edi, eax
0054FAB3  85 C0                           test eax, eax
0054FAB5  78 12                           js 0x14054fac9
0054FAB7  49 8B 04 24                     mov rax, qword ptr [r12]
0054FABB  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
0054FABE  41 39 4F 50                     cmp dword ptr [r15 + 0x50], ecx
0054FAC2  74 75                           je 0x14054fb39
0054FAC4  BF 01 00 00 C0                  mov edi, 0xc0000001
0054FAC9  8A 9C 24 98 00 00 00            mov bl, byte ptr [rsp + 0x98]
0054FAD0  E8 63 F0 FF FF                  call 0x14054eb38
0054FAD5  85 C0                           test eax, eax
0054FAD7  75 3D                           jne 0x14054fb16
0054FAD9  84 DB                           test bl, bl
0054FADB  74 39                           je 0x14054fb16
0054FADD  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FAE1  E8 AA 8B CF FF                  call 0x140248690
0054FAE6  48 83 C6 20                     add rsi, 0x20
0054FAEA  4C 8B 06                        mov r8, qword ptr [rsi]
0054FAED  49 39 70 08                     cmp qword ptr [r8 + 8], rsi
0054FAF1  0F 85 F2 01 00 00               jne 0x14054fce9
0054FAF7  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0054FAFB  48 39 32                        cmp qword ptr [rdx], rsi
0054FAFE  0F 85 E5 01 00 00               jne 0x14054fce9
0054FB04  4C 89 02                        mov qword ptr [rdx], r8
0054FB07  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FB0B  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0054FB0F  8A D0                           mov dl, al
0054FB11  E8 DA 13 D7 FF                  call 0x1402c0ef0
0054FB16  80 BC 24 A0 00 00 00 00         cmp byte ptr [rsp + 0xa0], 0
0054FB1E  0F 84 E3 01 00 00               je 0x14054fd07
0054FB24  E8 67 80 FA FF                  call 0x1404f7b90
0054FB29  85 C0                           test eax, eax
0054FB2B  0F 85 BF 01 00 00               jne 0x14054fcf0
0054FB31  8D 50 01                        lea edx, [rax + 1]
0054FB34  E9 B9 01 00 00                  jmp 0x14054fcf2
0054FB39  83 7E 30 00                     cmp dword ptr [rsi + 0x30], 0
0054FB3D  74 48                           je 0x14054fb87
0054FB3F  49 8B D6                        mov rdx, r14
0054FB42  49 8B CC                        mov rcx, r12
0054FB45  E8 06 56 01 00                  call 0x140565150
0054FB4A  8B F8                           mov edi, eax
0054FB4C  85 C0                           test eax, eax
0054FB4E  0F 88 75 FF FF FF               js 0x14054fac9
0054FB54  C6 84 24 A8 00 00 00 01         mov byte ptr [rsp + 0xa8], 1
0054FB5C  EB 29                           jmp 0x14054fb87
0054FB5E  44 39 7E 30                     cmp dword ptr [rsi + 0x30], r15d
0054FB62  75 23                           jne 0x14054fb87
0054FB64  45 33 C9                        xor r9d, r9d
0054FB67  4C 8B C3                        mov r8, rbx
0054FB6A  48 8B D5                        mov rdx, rbp
0054FB6D  49 8B CE                        mov rcx, r14
0054FB70  E8 C7 72 01 00                  call 0x140566e3c
0054FB75  8B F8                           mov edi, eax
0054FB77  85 C0                           test eax, eax
0054FB79  0F 88 62 01 00 00               js 0x14054fce1
0054FB7F  C6 84 24 A0 00 00 00 01         mov byte ptr [rsp + 0xa0], 1
0054FB87  E8 AC EF FF FF                  call 0x14054eb38
0054FB8C  85 C0                           test eax, eax
0054FB8E  75 3F                           jne 0x14054fbcf
0054FB90  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FB94  E8 F7 8A CF FF                  call 0x140248690
0054FB99  4C 8D 45 48                     lea r8, [rbp + 0x48]
0054FB9D  4D 8B 48 08                     mov r9, qword ptr [r8 + 8]
0054FBA1  48 8D 56 20                     lea rdx, [rsi + 0x20]
0054FBA5  4D 39 01                        cmp qword ptr [r9], r8
0054FBA8  0F 85 3B 01 00 00               jne 0x14054fce9
0054FBAE  4C 89 02                        mov qword ptr [rdx], r8
0054FBB1  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FBB5  4C 89 4A 08                     mov qword ptr [rdx + 8], r9
0054FBB9  49 89 11                        mov qword ptr [r9], rdx
0054FBBC  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0054FBC0  8A D0                           mov dl, al
0054FBC2  E8 29 13 D7 FF                  call 0x1402c0ef0
0054FBC7  C6 84 24 98 00 00 00 01         mov byte ptr [rsp + 0x98], 1
0054FBCF  80 3D 3A 1B A7 00 00            cmp byte ptr [rip + 0xa71b3a], 0
0054FBD6  75 11                           jne 0x14054fbe9
0054FBD8  48 8B D3                        mov rdx, rbx
0054FBDB  49 8B CC                        mov rcx, r12
0054FBDE  E8 7D 64 01 00                  call 0x140566060
0054FBE3  8B F8                           mov edi, eax
0054FBE5  85 C0                           test eax, eax
0054FBE7  EB 71                           jmp 0x14054fc5a
0054FBE9  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
0054FBEC  85 D2                           test edx, edx
0054FBEE  75 16                           jne 0x14054fc06
0054FBF0  44 8D 4A 01                     lea r9d, [rdx + 1]
0054FBF4  45 33 C0                        xor r8d, r8d
0054FBF7  48 8B D5                        mov rdx, rbp
0054FBFA  49 8B CE                        mov rcx, r14
0054FBFD  E8 3A 72 01 00                  call 0x140566e3c
0054FC02  8B F8                           mov edi, eax
0054FC04  EB 52                           jmp 0x14054fc58
0054FC06  4C 8B 66 10                     mov r12, qword ptr [rsi + 0x10]
0054FC0A  48 8B 05 7F 21 A7 00            mov rax, qword ptr [rip + 0xa7217f]
0054FC11  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
0054FC16  E8 B5 AE 16 00                  call 0x1406baad0
0054FC1B  8B F8                           mov edi, eax
0054FC1D  85 C0                           test eax, eax
0054FC1F  78 32                           js 0x14054fc53
0054FC21  48 8B 05 48 21 A7 00            mov rax, qword ptr [rip + 0xa72148]
0054FC28  48 83 CB 01                     or rbx, 1
0054FC2C  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
0054FC2F  4C 8B C3                        mov r8, rbx
0054FC32  33 C9                           xor ecx, ecx
0054FC34  E8 97 AE 16 00                  call 0x1406baad0
0054FC39  8B F8                           mov edi, eax
0054FC3B  85 C0                           test eax, eax
0054FC3D  79 14                           jns 0x14054fc53
0054FC3F  48 8B 05 52 21 A7 00            mov rax, qword ptr [rip + 0xa72152]
0054FC46  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
0054FC49  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
0054FC4E  E8 7D AE 16 00                  call 0x1406baad0
0054FC53  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0054FC58  85 FF                           test edi, edi
0054FC5A  0F 88 69 FE FF FF               js 0x14054fac9
0054FC60  E8 D3 EE FF FF                  call 0x14054eb38
0054FC65  85 C0                           test eax, eax
0054FC67  74 72                           je 0x14054fcdb
0054FC69  4D 85 ED                        test r13, r13
0054FC6C  74 3A                           je 0x14054fca8
0054FC6E  49 8D 4D 58                     lea rcx, [r13 + 0x58]
0054FC72  E8 19 8A CF FF                  call 0x140248690
0054FC77  48 8D 5E 20                     lea rbx, [rsi + 0x20]
0054FC7B  4C 8B 03                        mov r8, qword ptr [rbx]
0054FC7E  49 39 58 08                     cmp qword ptr [r8 + 8], rbx
0054FC82  75 65                           jne 0x14054fce9
0054FC84  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0054FC88  48 39 1A                        cmp qword ptr [rdx], rbx
0054FC8B  75 5C                           jne 0x14054fce9
0054FC8D  4C 89 02                        mov qword ptr [rdx], r8
0054FC90  49 8D 4D 58                     lea rcx, [r13 + 0x58]
0054FC94  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0054FC98  8A D0                           mov dl, al
0054FC9A  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
0054FC9E  48 89 1B                        mov qword ptr [rbx], rbx
0054FCA1  E8 4A 12 D7 FF                  call 0x1402c0ef0
0054FCA6  EB 04                           jmp 0x14054fcac
0054FCA8  48 8D 5E 20                     lea rbx, [rsi + 0x20]
0054FCAC  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FCB0  E8 DB 89 CF FF                  call 0x140248690
0054FCB5  48 8D 55 48                     lea rdx, [rbp + 0x48]
0054FCB9  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
0054FCBD  49 39 10                        cmp qword ptr [r8], rdx
0054FCC0  75 27                           jne 0x14054fce9
0054FCC2  48 89 13                        mov qword ptr [rbx], rdx
0054FCC5  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0054FCC9  4C 89 43 08                     mov qword ptr [rbx + 8], r8
0054FCCD  49 89 18                        mov qword ptr [r8], rbx
0054FCD0  48 89 5A 08                     mov qword ptr [rdx + 8], rbx
0054FCD4  8A D0                           mov dl, al
0054FCD6  E8 15 12 D7 FF                  call 0x1402c0ef0
0054FCDB  48 89 6E 18                     mov qword ptr [rsi + 0x18], rbp
0054FCDF  EB 4B                           jmp 0x14054fd2c
0054FCE1  41 8A DF                        mov bl, r15b
0054FCE4  E9 E7 FD FF FF                  jmp 0x14054fad0
0054FCE9  B9 03 00 00 00                  mov ecx, 3
0054FCEE  CD 29                           int 0x29
0054FCF0  33 D2                           xor edx, edx
0054FCF2  49 8B CE                        mov rcx, r14
0054FCF5  E8 BA 74 01 00                  call 0x1405671b4
0054FCFA  BA 01 00 00 00                  mov edx, 1
0054FCFF  49 8B CE                        mov rcx, r14
0054FD02  E8 AD 74 01 00                  call 0x1405671b4
0054FD07  80 BC 24 A8 00 00 00 00         cmp byte ptr [rsp + 0xa8], 0
0054FD0F  74 0B                           je 0x14054fd1c
0054FD11  49 8B D6                        mov rdx, r14
0054FD14  49 8B CC                        mov rcx, r12
0054FD17  E8 64 51 01 00                  call 0x140564e80
0054FD1C  4D 85 FF                        test r15, r15
0054FD1F  74 0B                           je 0x14054fd2c
0054FD21  49 8B D7                        mov rdx, r15
0054FD24  48 8B CD                        mov rcx, rbp
0054FD27  E8 2C 51 00 00                  call 0x140554e58
0054FD2C  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0054FD34  8B C7                           mov eax, edi
0054FD36  48 83 C4 50                     add rsp, 0x50
0054FD3A  41 5F                           pop r15
0054FD3C  41 5E                           pop r14
0054FD3E  41 5D                           pop r13
0054FD40  41 5C                           pop r12
0054FD42  5F                              pop rdi
0054FD43  5E                              pop rsi
0054FD44  5D                              pop rbp
0054FD45  C3                              ret
0054FD46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommupDomainAttachPasidDevice(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a2 + 56);
    v_stack_p18 = 0;
    v_stack_p10 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 16) + 392)) != 1) goto loc_0054F9EA;
    goto loc_0054FAD0;
loc_0054F9EA:
    if ((*(unsigned int *)(a1 + 8)) == 3) goto loc_0054F9FA;
    goto loc_0054FAD0;
loc_0054F9FA:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0054FA17;
    if (*(unsigned __int64 *)(a2 + 24) == 0) goto loc_0054FA44;
    if ((*(unsigned __int64 *)(a2 + 24)) == a1) goto loc_0054FD2C;
    goto loc_0054FA2E;
loc_0054FA17:
    if ((*(unsigned __int64 *)(a2 + 24)) == a1) goto loc_0054FD2C;
    if (*(unsigned __int64 *)(a2 + 24) == 0) goto loc_0054FA44;
    if ((*(unsigned int *)(a2 + 48)) == ((unsigned int)((unsigned int)(0xC00000EFULL)))) goto loc_0054FA38;
loc_0054FA2E:
    goto loc_0054FAD0;
loc_0054FA38:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 16) + 273)) != 0) goto loc_0054FA2E;
loc_0054FA44:
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0054FA56;
    goto loc_0054FA5B;
loc_0054FA56:
loc_0054FA5B:
    result = HalpIommuGetDmarptRootAddress(*(unsigned __int64 *)(a1 + 40), 4, v_stack_m50, a4);
    if (sign_flag) goto loc_0054FAD0;
    if ((*(unsigned __int8 *)(v_rip + 10951834)) != 0) goto loc_0054FB5E;
    *(unsigned int *)(a1 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56)) + 16)));
    v_stack_m60 = v_stack_m58;
    v_stack_m68 = 1;
    result = HalpIommuGetHardwareDomain(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 32), 1, 1);
    if (sign_flag) goto loc_0054FAC9;
    if ((*(unsigned int *)(v_stack_m58 + 80)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56)) + 16))))) goto loc_0054FB39;
loc_0054FAC9:
loc_0054FAD0:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56)) + 16)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 32), 1, 1);
    if ((unsigned int)(result) != 0) goto loc_0054FB16;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_0054FB16;
    result = ExAcquireSpinLockExclusive(a1 + 88, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 32), 1, 1);
    v_rsi = (a2) + (32);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8)) != v_rsi) goto loc_0054FCE9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) != v_rsi) goto loc_0054FCE9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) = *(unsigned __int64 *)(v_rsi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8) = *(unsigned __int64 *)(v_rsi + 8);
    result = ExReleaseSpinLockExclusive(a1 + 88, (unsigned __int8)(result), *(unsigned __int64 *)(v_rsi), 1);
loc_0054FB16:
    if (v_stack_p18 == 0) goto loc_0054FD07;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1 + 88, (unsigned __int8)(result), *(unsigned __int64 *)(v_rsi), 1);
    if ((unsigned int)(result) != 0) goto loc_0054FCF0;
    goto loc_0054FCF2;
loc_0054FB39:
    if ((*(unsigned int *)(v_rsi + 48)) == 0) goto loc_0054FB87;
    result = IommuEnableDevicePasid(*(unsigned __int64 *)(a2 + 56), *(unsigned __int64 *)(a2 + 16), *(unsigned __int64 *)(v_rsi), 1);
    if (sign_flag) goto loc_0054FAC9;
    v_stack_p20 = 1;
    goto loc_0054FB87;
loc_0054FB5E:
    if ((*(unsigned int *)(v_rsi + 48)) != ((unsigned int)(v_stack_m58))) goto loc_0054FB87;
    a4 = 0;
    result = IommupHvAttachPasidDeviceDomain(*(unsigned __int64 *)(a2 + 16), a1, v_stack_p10, a4);
    if (sign_flag) goto loc_0054FCE1;
    v_stack_p18 = 1;
loc_0054FB87:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a2 + 16), a1, v_stack_p10, a4);
    if ((unsigned int)(result) != 0) goto loc_0054FBCF;
    result = ExAcquireSpinLockExclusive(a1 + 88, a1, v_stack_p10, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72 + 8))) != (a1 + 72)) goto loc_0054FCE9;
    *(unsigned __int64 *)(v_rsi + 32) = a1 + 72;
    *(unsigned __int64 *)(v_rsi + 32 + 8) = *(unsigned __int64 *)(a1 + 72 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72 + 8)) = v_rsi + 32;
    *(unsigned __int64 *)(a1 + 72 + 8) = v_rsi + 32;
    result = ExReleaseSpinLockExclusive(a1 + 88, (unsigned __int8)(result), a1 + 72, *(unsigned __int64 *)(a1 + 72 + 8));
    v_stack_p10 = 1;
loc_0054FBCF:
    if ((*(unsigned __int8 *)(v_rip + 10951482)) != 0) goto loc_0054FBE9;
    result = IommuSetAddressSpace(*(unsigned __int64 *)(a2 + 56), v_stack_p10, a1 + 72, *(unsigned __int64 *)(a1 + 72 + 8));
    goto loc_0054FC5A;
loc_0054FBE9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 48))) != 0) goto loc_0054FC06;
    a3 = 0;
    result = IommupHvAttachPasidDeviceDomain(*(unsigned __int64 *)(a2 + 16), a1, a3, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    goto loc_0054FC58;
loc_0054FC06:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 32), a1, a3, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    if (sign_flag) goto loc_0054FC53;
    v_rbx = (v_stack_p10) | (1);
    a1 = 0;
    result = guard_dispatch_icall(a1, (unsigned int)(*(unsigned int *)(v_rsi + 48)), v_rbx, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    if (sign_flag) {
        result = *(unsigned __int64 *)(v_rip + 10953042);
        a2 = *(unsigned int *)(v_rsi + 48);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 32);
        result = guard_dispatch_icall(a1, a2, v_rbx, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    }
loc_0054FC58:
loc_0054FC5A:
    if (sign_flag) goto loc_0054FAC9;
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(a1, a2, v_rbx, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    if ((unsigned int)(result) == 0) goto loc_0054FCDB;
    if (*(unsigned __int64 *)(a2 + 24) == 0) goto loc_0054FCA8;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a2 + 24) + 88, a2, v_rbx, (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 32) + 8)) != (v_rsi + 32)) goto loc_0054FCE9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 32 + 8))) != (v_rsi + 32)) goto loc_0054FCE9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 32 + 8)) = *(unsigned __int64 *)(v_rsi + 32);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 32) + 8) = *(unsigned __int64 *)(v_rsi + 32 + 8);
    *(unsigned __int64 *)(v_rsi + 32 + 8) = v_rsi + 32;
    *(unsigned __int64 *)(v_rsi + 32) = v_rsi + 32;
    result = ExReleaseSpinLockExclusive(*(unsigned __int64 *)(a2 + 24) + 88, (unsigned __int8)(result), *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    goto loc_0054FCAC;
loc_0054FCA8:
loc_0054FCAC:
    result = ExAcquireSpinLockExclusive(a1 + 88, (unsigned __int8)(result), *(unsigned __int64 *)(v_rsi + 32), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72 + 8))) != (a1 + 72)) goto loc_0054FCE9;
    *(unsigned __int64 *)(v_rsi + 32) = a1 + 72;
    *(unsigned __int64 *)(v_rsi + 32 + 8) = *(unsigned __int64 *)(a1 + 72 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72 + 8)) = v_rsi + 32;
    *(unsigned __int64 *)(a1 + 72 + 8) = v_rsi + 32;
    result = ExReleaseSpinLockExclusive(a1 + 88, (unsigned __int8)(result), *(unsigned __int64 *)(a1 + 72 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
loc_0054FCDB:
    *(unsigned __int64 *)(v_rsi + 24) = a1;
    goto loc_0054FD2C;
loc_0054FCE1:
    goto loc_0054FAD0;
loc_0054FCE9:
loc_0054FCF0:
    a2 = 0;
loc_0054FCF2:
    result = IommupHvDetachPasidDeviceDomain(*(unsigned __int64 *)(a2 + 16), a2, *(unsigned __int64 *)(a1 + 72 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    result = IommupHvDetachPasidDeviceDomain(*(unsigned __int64 *)(a2 + 16), 1, *(unsigned __int64 *)(a1 + 72 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
loc_0054FD07:
    if (v_stack_p20 != 0) {
        a2 = *(unsigned __int64 *)(a2 + 16);
        a1 = v_stack_m48;
        result = IommuDisableDevicePasid(a1, a2, *(unsigned __int64 *)(a1 + 72 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    }
    if (v_stack_m58 != 0) {
        a2 = v_stack_m58;
        a1 = a1;
        result = HalpIommuDereferenceHardwareDomain(a1, a2, *(unsigned __int64 *)(a1 + 72 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 48)) + 1);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t IommupDomainAttachPasidDevice(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    v_stack_m58 = 0;
    v_stack_m48 = *(uint64_t *)(arg2 + 0x38);
    v_stack_p18 = 0;
    v_stack_p10 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x10) + 0x188)) != 1) goto loc_0054F9EA;
    goto loc_0054FAD0;
loc_0054F9EA:
    if ((*(uint32_t *)(arg1 + 0x8)) == 3) goto loc_0054F9FA;
    goto loc_0054FAD0;
loc_0054F9FA:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0054FA17;
    if (*(uint64_t *)(arg2 + 0x18) == 0) goto loc_0054FA44;
    if ((*(uint64_t *)(arg2 + 0x18)) == Arg1) goto loc_0054FD2C;
    goto loc_0054FA2E;
loc_0054FA17:
    if ((*(uint64_t *)(arg2 + 0x18)) == Arg1) goto loc_0054FD2C;
    if (*(uint64_t *)(arg2 + 0x18) == 0) goto loc_0054FA44;
    if ((*(uint32_t *)(arg2 + 0x30)) == ((uint32_t)((uint32_t)(0xC00000EFULL)))) goto loc_0054FA38;
loc_0054FA2E:
    goto loc_0054FAD0;
loc_0054FA38:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x10) + 0x111)) != 0) goto loc_0054FA2E;
loc_0054FA44:
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0054FA56;
    goto loc_0054FA5B;
loc_0054FA56:
loc_0054FA5B:
    result = HalpIommuGetDmarptRootAddress(*(uint64_t *)(arg1 + 0x28), 4, v_stack_m50, a4);
    if (sign_flag) goto loc_0054FAD0;
    if ((*(uint8_t *)(v_rip + 0xA71C9A)) != 0) goto loc_0054FB5E;
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38)) + 0x10)));
    v_stack_m60 = v_stack_m58;
    v_stack_m68 = 1;
    result = HalpIommuGetHardwareDomain(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x20), 1, 1);
    if (sign_flag) goto loc_0054FAC9;
    if ((*(uint32_t *)(v_stack_m58 + 0x50)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38)) + 0x10))))) goto loc_0054FB39;
loc_0054FAC9:
loc_0054FAD0:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38)) + 0x10)), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x20), 1, 1);
    if ((uint32_t)(result) != 0) goto loc_0054FB16;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_0054FB16;
    result = ExAcquireSpinLockExclusive(Arg1 + 88, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x20), 1, 1);
    local_rsi = (Arg2) + (32);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8)) != local_rsi) goto loc_0054FCE9;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) != local_rsi) goto loc_0054FCE9;
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) = *(uint64_t *)(local_rsi);
    *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8) = *(uint64_t *)(local_rsi + 0x8);
    result = ExReleaseSpinLockExclusive(Arg1 + 88, (uint8_t)(result), *(uint64_t *)(local_rsi), 1);
loc_0054FB16:
    if (v_stack_p18 == 0) goto loc_0054FD07;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1 + 88, (uint8_t)(result), *(uint64_t *)(local_rsi), 1);
    if ((uint32_t)(result) != 0) goto loc_0054FCF0;
    goto loc_0054FCF2;
loc_0054FB39:
    if ((*(uint32_t *)(local_rsi + 0x30)) == 0) goto loc_0054FB87;
    result = IommuEnableDevicePasid(*(uint64_t *)(arg2 + 0x38), *(uint64_t *)(arg2 + 0x10), *(uint64_t *)(local_rsi), 1);
    if (sign_flag) goto loc_0054FAC9;
    v_stack_p20 = 1;
    goto loc_0054FB87;
loc_0054FB5E:
    if ((*(uint32_t *)(local_rsi + 0x30)) != ((uint32_t)(v_stack_m58))) goto loc_0054FB87;
    a4 = 0;
    result = IommupHvAttachPasidDeviceDomain(*(uint64_t *)(arg2 + 0x10), Arg1, v_stack_p10, a4);
    if (sign_flag) goto loc_0054FCE1;
    v_stack_p18 = 1;
loc_0054FB87:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg2 + 0x10), Arg1, v_stack_p10, a4);
    if ((uint32_t)(result) != 0) goto loc_0054FBCF;
    result = ExAcquireSpinLockExclusive(Arg1 + 88, Arg1, v_stack_p10, a4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48 + 0x8))) != (Arg1 + 72)) goto loc_0054FCE9;
    *(void **)(local_rsi + 0x20) = Arg1 + 72;
    *(uint64_t *)(local_rsi + 0x20 + 0x8) = *(uint64_t *)(arg1 + 0x48 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48 + 0x8)) = local_rsi + 32;
    *(uint64_t *)(arg1 + 0x48 + 0x8) = local_rsi + 32;
    result = ExReleaseSpinLockExclusive(Arg1 + 88, (uint8_t)(result), Arg1 + 72, *(uint64_t *)(arg1 + 0x48 + 0x8));
    v_stack_p10 = 1;
loc_0054FBCF:
    if ((*(uint8_t *)(v_rip + 0xA71B3A)) != 0) goto loc_0054FBE9;
    result = IommuSetAddressSpace(*(uint64_t *)(arg2 + 0x38), v_stack_p10, Arg1 + 72, *(uint64_t *)(arg1 + 0x48 + 0x8));
    goto loc_0054FC5A;
loc_0054FBE9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x30))) != 0) goto loc_0054FC06;
    a3 = 0;
    result = IommupHvAttachPasidDeviceDomain(*(uint64_t *)(arg2 + 0x10), Arg1, a3, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    goto loc_0054FC58;
loc_0054FC06:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x20), Arg1, a3, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    if (sign_flag) goto loc_0054FC53;
    local_rbx = (v_stack_p10) | (1);
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)), local_rbx, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    if (sign_flag) {
        result = *(uint64_t *)(v_rip + 0xA72152);
        Arg2 = *(uint32_t *)(local_rsi + 0x30);
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x20);
        result = guard_dispatch_icall(Arg1, Arg2, local_rbx, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    }
loc_0054FC58:
loc_0054FC5A:
    if (sign_flag) goto loc_0054FAC9;
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, local_rbx, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    if ((uint32_t)(result) == 0) goto loc_0054FCDB;
    if (*(uint64_t *)(arg2 + 0x18) == 0) goto loc_0054FCA8;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg2 + 0x18) + 88, Arg2, local_rbx, (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x20) + 0x8)) != (local_rsi + 32)) goto loc_0054FCE9;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x20 + 0x8))) != (local_rsi + 32)) goto loc_0054FCE9;
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x20 + 0x8)) = *(uint64_t *)(local_rsi + 0x20);
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x20) + 0x8) = *(uint64_t *)(local_rsi + 0x20 + 0x8);
    *(uint64_t *)(local_rsi + 0x20 + 0x8) = local_rsi + 32;
    *(uint64_t *)(local_rsi + 0x20) = local_rsi + 32;
    result = ExReleaseSpinLockExclusive(*(uint64_t *)(arg2 + 0x18) + 88, (uint8_t)(result), *(uint64_t *)(local_rsi + 0x20), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    goto loc_0054FCAC;
loc_0054FCA8:
loc_0054FCAC:
    result = ExAcquireSpinLockExclusive(Arg1 + 88, (uint8_t)(result), *(uint64_t *)(local_rsi + 0x20), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48 + 0x8))) != (Arg1 + 72)) goto loc_0054FCE9;
    *(void **)(local_rsi + 0x20) = Arg1 + 72;
    *(uint64_t *)(local_rsi + 0x20 + 0x8) = *(uint64_t *)(arg1 + 0x48 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48 + 0x8)) = local_rsi + 32;
    *(uint64_t *)(arg1 + 0x48 + 0x8) = local_rsi + 32;
    result = ExReleaseSpinLockExclusive(Arg1 + 88, (uint8_t)(result), *(uint64_t *)(arg1 + 0x48 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
loc_0054FCDB:
    *(void **)(local_rsi + 0x18) = Arg1;
    goto loc_0054FD2C;
loc_0054FCE1:
    goto loc_0054FAD0;
loc_0054FCE9:
loc_0054FCF0:
    Arg2 = 0;
loc_0054FCF2:
    result = IommupHvDetachPasidDeviceDomain(*(uint64_t *)(arg2 + 0x10), Arg2, *(uint64_t *)(arg1 + 0x48 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    result = IommupHvDetachPasidDeviceDomain(*(uint64_t *)(arg2 + 0x10), 1, *(uint64_t *)(arg1 + 0x48 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
loc_0054FD07:
    if (v_stack_p20 != 0) {
        Arg2 = *(uint64_t *)(arg2 + 0x10);
        Arg1 = v_stack_m48;
        result = IommuDisableDevicePasid(Arg1, Arg2, *(uint64_t *)(arg1 + 0x48 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    }
    if (v_stack_m58 != 0) {
        Arg2 = v_stack_m58;
        Arg1 = Arg1;
        result = HalpIommuDereferenceHardwareDomain(Arg1, Arg2, *(uint64_t *)(arg1 + 0x48 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x30)) + 1);
    }
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054F984&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
