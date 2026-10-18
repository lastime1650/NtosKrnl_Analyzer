# sub_002F6E32

- RVA: `0x002F6E32`–`0x002F7743` (길이 `2,321` bytes)
- VA: `0x00000001402F6E32`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00072374`
- 디코드: `528`개 명령, `2,321/2,321` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x002F6EA1` → [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) (function, `0x00320E10`)
- `0x002F6EEB` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002F6F05` → [MiMakeSystemCacheRangeValid](../34/MiMakeSystemCacheRangeValid_function_00347440.md) (function, `0x00347440`)
- `0x002F7080` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x002F7120` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002F71D5` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x002F7217` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x002F724D` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x002F725B` → [MiPfnZeroingNeeded](../29/MiPfnZeroingNeeded_function_0029FA80.md) (function, `0x0029FA80`)
- `0x002F7281` → [MiReferenceControlAreaPfn](../36/MiReferenceControlAreaPfn_function_00364084.md) (function, `0x00364084`)
- `0x002F729C` → [MiInitializePfn](../33/MiInitializePfn_function_00331E60.md) (function, `0x00331E60`)
- `0x002F72B0` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002F7399` → [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) (function, `0x0033DD90`)
- `0x002F73B6` → [MiClearPfnReuseFields](../37/MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x002F73D8` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x002F740E` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002F7453` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x002F7461` → [MiDirtyPte](../23/MiDirtyPte_function_00237C5C.md) (function, `0x00237C5C`)
- `0x002F74C2` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002F756B` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x002F759E` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x002F75C1` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002F75D9` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002F75E8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002F75FA` → [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) (function, `0x00320E10`)
- `0x002F7625` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002F762D` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x002F7644` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002F7695` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002F76A7` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002F76C1` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002F76D5` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x002F7714` → [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) (function, `0x0044C740`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002F6E43` → RVA `0x00E2DC80` (`.data`; read)
- `0x002F6F9C` → RVA `0x00E2DCE0` (`.data`; read)
- `0x002F6FEA` → RVA `0x00E30088` (`.data`; read)
- `0x002F7125` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002F71EE` → RVA `0x00E2DCC0` (`.data`; read)
- `0x002F7322` → RVA `0x00E2EE84` (`.data`; read)
- `0x002F7352` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002F75CB` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002F7632` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **16**
  - `0x002F6E87` → [sub_002F7743 + 0x40](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F6ED8` → [sub_002F6D91 + 0x2E](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F6F0D` → [sub_002F6D91 + 0x2E](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F7041` → [sub_002F7743 + 0x65](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F704F` → [sub_002F7743 + 0x65](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F7075` → [sub_006DF29A](../6D/Unknown_function_006DF29A.md) (`tail-transfer`)
  - `0x002F70ED` → [sub_002F7743 + 0x81](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F72D4` → [sub_002F7743 + 0x65](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F733A` → [sub_002F6D91 + 0x18](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F73EF` → [sub_002F6D91 + 0x2E](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F744B` → [sub_002F7743 + 0x2B](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F7466` → [sub_002F6D91 + 0x16](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F7572` → [sub_002F7743 + 0x92](Unknown_function_002F7743.md) (`tail-transfer`)
  - `0x002F7591` → [sub_002F6D91 + 0x16](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F7658` → [sub_002F6D91 + 0x2E](Unknown_function_002F6D91.md) (`tail-transfer`)
  - `0x002F771F` → [sub_002F7743 + 0x79](Unknown_function_002F7743.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F6E32  48 8B C3                        mov rax, rbx
002F6E35  49 8B F7                        mov rsi, r15
002F6E38  83 E0 08                        and eax, 8
002F6E3B  4C 8B FB                        mov r15, rbx
002F6E3E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002F6E43  48 8B 05 36 6E B3 00            mov rax, qword ptr [rip + 0xb36e36]
002F6E4A  48 85 C0                        test rax, rax
002F6E4D  74 12                           je 0x1402f6e61
002F6E4F  F6 C3 10                        test bl, 0x10
002F6E52  0F 85 BA 00 00 00               jne 0x1402f6f12
002F6E58  4C 8B F8                        mov r15, rax
002F6E5B  49 F7 D7                        not r15
002F6E5E  4C 23 FB                        and r15, rbx
002F6E61  49 C1 FF 10                     sar r15, 0x10
002F6E65  48 81 E6 00 F0 FF FF            and rsi, 0xfffffffffffff000
002F6E6C  49 8B DF                        mov rbx, r15
002F6E6F  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
002F6E76  4D 85 ED                        test r13, r13
002F6E79  0F 85 9C 00 00 00               jne 0x1402f6f1b
002F6E7F  48 3B DE                        cmp rbx, rsi
002F6E82  74 09                           je 0x1402f6e8d
002F6E84  45 85 E4                        test r12d, r12d
002F6E87  0F 85 F6 08 00 00               jne 0x1402f7783
002F6E8D  49 8B 1F                        mov rbx, qword ptr [r15]
002F6E90  F6 C3 01                        test bl, 1
002F6E93  0F 84 82 05 00 00               je 0x1402f741b
002F6E99  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
002F6E9E  49 8B CF                        mov rcx, r15
002F6EA1  E8 6A 9F 02 00                  call 0x140320e10
002F6EA6  4C 8B E8                        mov r13, rax
002F6EA9  49 B8 28 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000028
002F6EB3  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002F6EBD  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
002F6EC7  EB 5B                           jmp 0x1402f6f24
002F6EC9  4A 89 84 E4 80 00 00 00         mov qword ptr [rsp + r12*8 + 0x80], rax
002F6ED1  41 FF C4                        inc r12d
002F6ED4  41 83 FC 10                     cmp r12d, 0x10
002F6ED8  0F 85 E1 FE FF FF               jne 0x1402f6dbf
002F6EDE  4D 85 ED                        test r13, r13
002F6EE1  74 10                           je 0x1402f6ef3
002F6EE3  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002F6EE8  49 8B CD                        mov rcx, r13
002F6EEB  E8 A0 F1 F4 FF                  call 0x140246090
002F6EF0  45 33 ED                        xor r13d, r13d
002F6EF3  48 8D 4F 80                     lea rcx, [rdi - 0x80]
002F6EF7  41 B8 10 00 00 00               mov r8d, 0x10
002F6EFD  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
002F6F05  E8 36 05 05 00                  call 0x140347440
002F6F0A  45 33 E4                        xor r12d, r12d
002F6F0D  E9 AD FE FF FF                  jmp 0x1402f6dbf
002F6F12  49 83 E7 EF                     and r15, 0xffffffffffffffef
002F6F16  E9 46 FF FF FF                  jmp 0x1402f6e61
002F6F1B  48 3B DE                        cmp rbx, rsi
002F6F1E  0F 85 8C 06 00 00               jne 0x1402f75b0
002F6F24  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
002F6F2D  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002F6F32  49 8B 1F                        mov rbx, qword ptr [r15]
002F6F35  F6 C3 01                        test bl, 1
002F6F38  0F 84 22 02 00 00               je 0x1402f7160
002F6F3E  49 8B 1F                        mov rbx, qword ptr [r15]
002F6F41  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
002F6F46  48 8B C3                        mov rax, rbx
002F6F49  F6 C3 01                        test bl, 1
002F6F4C  75 47                           jne 0x1402f6f95
002F6F4E  25 00 0C 00 00                  and eax, 0xc00
002F6F53  48 3D 00 08 00 00               cmp rax, 0x800
002F6F59  0F 85 E1 04 00 00               jne 0x1402f7440
002F6F5F  48 85 DB                        test rbx, rbx
002F6F62  74 10                           je 0x1402f6f74
002F6F64  48 8B 05 15 6D B3 00            mov rax, qword ptr [rip + 0xb36d15]
002F6F6B  48 85 C0                        test rax, rax
002F6F6E  0F 85 CB 03 00 00               jne 0x1402f733f
002F6F74  48 8B 0D 05 6D B3 00            mov rcx, qword ptr [rip + 0xb36d05]
002F6F7B  48 8B C3                        mov rax, rbx
002F6F7E  48 85 C9                        test rcx, rcx
002F6F81  74 12                           je 0x1402f6f95
002F6F83  F6 C3 10                        test bl, 0x10
002F6F86  0F 85 AB 04 00 00               jne 0x1402f7437
002F6F8C  48 8B C1                        mov rax, rcx
002F6F8F  48 F7 D0                        not rax
002F6F92  48 23 C3                        and rax, rbx
002F6F95  48 C1 E8 0C                     shr rax, 0xc
002F6F99  48 23 C2                        and rax, rdx
002F6F9C  48 3B 05 3D 6D B3 00            cmp rax, qword ptr [rip + 0xb36d3d]
002F6FA3  77 99                           ja 0x1402f6f3e
002F6FA5  48 8D 0C 40                     lea rcx, [rax + rax*2]
002F6FA9  48 03 C9                        add rcx, rcx
002F6FAC  49 8B C0                        mov rax, r8
002F6FAF  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002F6FB3  48 C1 E8 36                     shr rax, 0x36
002F6FB7  0F BA E0 00                     bt eax, 0
002F6FBB  73 81                           jae 0x1402f6f3e
002F6FBD  49 8B C2                        mov rax, r10
002F6FC0  48 8D 34 C8                     lea rsi, [rax + rcx*8]
002F6FC4  33 DB                           xor ebx, ebx
002F6FC6  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
002F6FCD  0F 82 7D 03 00 00               jb 0x1402f7350
002F6FD3  49 8B 07                        mov rax, qword ptr [r15]
002F6FD6  48 3B 44 24 30                  cmp rax, qword ptr [rsp + 0x30]
002F6FDB  0F 85 EB 04 00 00               jne 0x1402f74cc
002F6FE1  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002F6FE5  BA FF 03 00 00                  mov edx, 0x3ff
002F6FEA  48 8B 0D 97 90 B3 00            mov rcx, qword ptr [rip + 0xb39097]
002F6FF1  48 C1 E8 2B                     shr rax, 0x2b
002F6FF5  48 23 C2                        and rax, rdx
002F6FF8  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002F6FFC  8B 40 04                        mov eax, dword ptr [rax + 4]
002F6FFF  84 C0                           test al, al
002F7001  0F 88 8F 05 00 00               js 0x1402f7596
002F7007  49 8B 1F                        mov rbx, qword ptr [r15]
002F700A  48 85 F6                        test rsi, rsi
002F700D  0F 84 61 01 00 00               je 0x1402f7174
002F7013  F6 C3 01                        test bl, 1
002F7016  0F 85 B0 02 00 00               jne 0x1402f72cc
002F701C  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002F7020  48 8B 0D 61 90 B3 00            mov rcx, qword ptr [rip + 0xb39061]
002F7027  48 C1 E8 2B                     shr rax, 0x2b
002F702B  48 23 C2                        and rax, rdx
002F702E  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002F7032  8B 40 04                        mov eax, dword ptr [rax + 4]
002F7035  84 C0                           test al, al
002F7037  0F 88 B0 06 00 00               js 0x1402f76ed
002F703D  F6 46 22 20                     test byte ptr [rsi + 0x22], 0x20
002F7041  0F 85 61 07 00 00               jne 0x1402f77a8
002F7047  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002F704A  C1 E8 18                        shr eax, 0x18
002F704D  A8 40                           test al, 0x40
002F704F  0F 85 53 07 00 00               jne 0x1402f77a8
002F7055  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
002F7059  48 8B D0                        mov rdx, rax
002F705C  48 8B C8                        mov rcx, rax
002F705F  48 C1 E9 0B                     shr rcx, 0xb
002F7063  81 E2 00 04 00 00               and edx, 0x400
002F7069  48 C1 E8 03                     shr rax, 3
002F706D  48 85 D2                        test rdx, rdx
002F7070  0F 45 C1                        cmovne eax, ecx
002F7073  A8 01                           test al, 1
002F7075  0F 85 1F 82 3E 00               jne 0x1406df29a
002F707B  33 D2                           xor edx, edx
002F707D  48 8B CE                        mov rcx, rsi
002F7080  E8 0B 05 F9 FF                  call 0x140287590
002F7085  A8 03                           test al, 3
002F7087  0F 85 E2 02 00 00               jne 0x1402f736f
002F708D  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
002F7091  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002F709B  48 0B C1                        or rax, rcx
002F709E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002F70A3  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002F70A6  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
002F70AA  66 FF C0                        inc ax
002F70AD  66 89 44 24 24                  mov word ptr [rsp + 0x24], ax
002F70B2  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
002F70B6  89 46 20                        mov dword ptr [rsi + 0x20], eax
002F70B9  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002F70BC  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
002F70C0  C1 E8 10                        shr eax, 0x10
002F70C3  24 FE                           and al, 0xfe
002F70C5  0C 06                           or al, 6
002F70C7  88 44 24 26                     mov byte ptr [rsp + 0x26], al
002F70CB  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
002F70CF  89 46 20                        mov dword ptr [rsi + 0x20], eax
002F70D2  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002F70D5  44 8B 46 10                     mov r8d, dword ptr [rsi + 0x10]
002F70D9  C1 E8 10                        shr eax, 0x10
002F70DC  49 C1 E8 05                     shr r8, 5
002F70E0  0F B6 C8                        movzx ecx, al
002F70E3  41 83 E0 07                     and r8d, 7
002F70E7  C1 E9 06                        shr ecx, 6
002F70EA  83 F9 01                        cmp ecx, 1
002F70ED  0F 85 D1 06 00 00               jne 0x1402f77c4
002F70F3  41 0F BA E8 1D                  bts r8d, 0x1d
002F70F8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002F7102  48 8B C0                        mov rax, rax
002F7105  48 8B D6                        mov rdx, rsi
002F7108  48 8B CF                        mov rcx, rdi
002F710B  48 2B D0                        sub rdx, rax
002F710E  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002F7118  48 C1 FA 04                     sar rdx, 4
002F711C  48 0F AF D0                     imul rdx, rax
002F7120  E8 6B E4 FC FF                  call 0x1402c5590
002F7125  48 0F BA 25 5A F9 CC 00 24      bt qword ptr [rip + 0xccf95a], 0x24
002F712E  48 8B D8                        mov rbx, rax
002F7131  0F 82 51 03 00 00               jb 0x1402f7488
002F7137  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
002F713C  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
002F7146  48 89 18                        mov qword ptr [rax], rbx
002F7149  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002F714D  48 23 C1                        and rax, rcx
002F7150  48 83 C8 01                     or rax, 1
002F7154  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002F7158  49 8B 1F                        mov rbx, qword ptr [r15]
002F715B  E9 9C 01 00 00                  jmp 0x1402f72fc
002F7160  48 8B C3                        mov rax, rbx
002F7163  25 00 0C 00 00                  and eax, 0xc00
002F7168  48 3D 00 08 00 00               cmp rax, 0x800
002F716E  0F 84 CA FD FF FF               je 0x1402f6f3e
002F7174  48 8B 0D 05 6B B3 00            mov rcx, qword ptr [rip + 0xb36b05]
002F717B  48 8B C3                        mov rax, rbx
002F717E  48 85 C9                        test rcx, rcx
002F7181  74 0E                           je 0x1402f7191
002F7183  F6 C3 10                        test bl, 0x10
002F7186  75 09                           jne 0x1402f7191
002F7188  48 8B C1                        mov rax, rcx
002F718B  48 F7 D0                        not rax
002F718E  48 23 C3                        and rax, rbx
002F7191  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002F7196  48 C1 F8 10                     sar rax, 0x10
002F719A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002F719F  F6 41 3E 0C                     test byte ptr [rcx + 0x3e], 0xc
002F71A3  0F 85 55 03 00 00               jne 0x1402f74fe
002F71A9  F6 44 24 28 01                  test byte ptr [rsp + 0x28], 1
002F71AE  0F 84 4A 03 00 00               je 0x1402f74fe
002F71B4  44 8B 41 38                     mov r8d, dword ptr [rcx + 0x38]
002F71B8  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
002F71BD  33 F6                           xor esi, esi
002F71BF  BA 03 00 00 00                  mov edx, 3
002F71C4  4D 85 ED                        test r13, r13
002F71C7  40 0F 95 C6                     setne sil
002F71CB  41 C1 E8 14                     shr r8d, 0x14
002F71CF  41 83 E0 7F                     and r8d, 0x7f
002F71D3  33 C9                           xor ecx, ecx
002F71D5  E8 36 92 02 00                  call 0x140320410
002F71DA  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
002F71DF  B8 01 00 00 00                  mov eax, 1
002F71E4  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
002F71E9  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
002F71EE  4C 8D 05 CB 6A B3 00            lea r8, [rip + 0xb36acb]
002F71F5  33 D2                           xor edx, edx
002F71F7  49 8B C9                        mov rcx, r9
002F71FA  48 C1 E9 10                     shr rcx, 0x10
002F71FE  83 E1 03                        and ecx, 3
002F7201  41 F7 34 88                     div dword ptr [r8 + rcx*4]
002F7205  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002F720A  44 8D 46 10                     lea r8d, [rsi + 0x10]
002F720E  41 33 D1                        xor edx, r9d
002F7211  0F B6 D2                        movzx edx, dl
002F7214  41 33 D1                        xor edx, r9d
002F7217  E8 A4 12 F9 FF                  call 0x1402884c0
002F721C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002F7221  48 83 F8 FF                     cmp rax, -1
002F7225  0F 84 D3 02 00 00               je 0x1402f74fe
002F722B  48 8D 34 40                     lea rsi, [rax + rax*2]
002F722F  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002F7239  48 C1 E6 04                     shl rsi, 4
002F723D  48 8B C0                        mov rax, rax
002F7240  48 8B CB                        mov rcx, rbx
002F7243  48 03 F0                        add rsi, rax
002F7246  48 C1 E9 05                     shr rcx, 5
002F724A  83 E1 1F                        and ecx, 0x1f
002F724D  E8 DE 12 FC FF                  call 0x1402b8530
002F7252  8B D0                           mov edx, eax
002F7254  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
002F7258  48 8B CE                        mov rcx, rsi
002F725B  E8 20 88 FA FF                  call 0x14029fa80
002F7260  85 C0                           test eax, eax
002F7262  0F 85 4C 04 00 00               jne 0x1402f76b4
002F7268  4D 85 ED                        test r13, r13
002F726B  0F 84 81 03 00 00               je 0x1402f75f2
002F7271  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
002F7276  41 B8 01 00 00 00               mov r8d, 1
002F727C  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002F7281  E8 FE CD 06 00                  call 0x140364084
002F7286  48 C1 EB 05                     shr rbx, 5
002F728A  41 B9 12 00 00 00               mov r9d, 0x12
002F7290  83 E3 1F                        and ebx, 0x1f
002F7293  49 8B D7                        mov rdx, r15
002F7296  44 8B C3                        mov r8d, ebx
002F7299  48 8B CE                        mov rcx, rsi
002F729C  E8 BF AB 03 00                  call 0x140331e60
002F72A1  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002F72A6  0F BA EB 1D                     bts ebx, 0x1d
002F72AA  44 8B C3                        mov r8d, ebx
002F72AD  48 8B CF                        mov rcx, rdi
002F72B0  E8 DB E2 FC FF                  call 0x1402c5590
002F72B5  48 0F BA 25 CA F7 CC 00 24      bt qword ptr [rip + 0xccf7ca], 0x24
002F72BE  48 8B D8                        mov rbx, rax
002F72C1  0F 82 96 03 00 00               jb 0x1402f765d
002F72C7  49 89 1F                        mov qword ptr [r15], rbx
002F72CA  EB 3F                           jmp 0x1402f730b
002F72CC  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002F72CF  C1 E8 18                        shr eax, 0x18
002F72D2  A8 40                           test al, 0x40
002F72D4  0F 85 CE 04 00 00               jne 0x1402f77a8
002F72DA  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002F72DE  48 8D 48 01                     lea rcx, [rax + 1]
002F72E2  48 8B D1                        mov rdx, rcx
002F72E5  48 33 D0                        xor rdx, rax
002F72E8  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
002F72F2  48 23 D0                        and rdx, rax
002F72F5  48 33 D1                        xor rdx, rcx
002F72F8  48 89 56 18                     mov qword ptr [rsi + 0x18], rdx
002F72FC  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002F7306  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002F730B  48 83 7C 24 58 00               cmp qword ptr [rsp + 0x58], 0
002F7311  0F 85 DD 00 00 00               jne 0x1402f73f4
002F7317  F6 44 24 28 04                  test byte ptr [rsp + 0x28], 4
002F731C  0F 85 49 01 00 00               jne 0x1402f746b
002F7322  0F B6 05 5B 7B B3 00            movzx eax, byte ptr [rip + 0xb37b5b]
002F7329  48 81 E3 FB FE FF FF            and rbx, 0xfffffffffffffefb
002F7330  83 E0 01                        and eax, 1
002F7333  48 C1 E0 08                     shl rax, 8
002F7337  48 0B C3                        or rax, rbx
002F733A  E9 6A FA FF FF                  jmp 0x1402f6da9
002F733F  48 85 D8                        test rax, rbx
002F7342  0F 84 F6 FB FF FF               je 0x1402f6f3e
002F7348  E9 27 FC FF FF                  jmp 0x1402f6f74
002F734D  0F 1F 00                        nop dword ptr [rax]
002F7350  FF C3                           inc ebx
002F7352  85 1D 54 DF CC 00               test dword ptr [rip + 0xccdf54], ebx
002F7358  0F 84 6D 02 00 00               je 0x1402f75cb
002F735E  F3 90                           pause
002F7360  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002F7364  48 85 C0                        test rax, rax
002F7367  0F 89 59 FC FF FF               jns 0x1402f6fc6
002F736D  EB E1                           jmp 0x1402f7350
002F736F  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002F7379  48 8B C0                        mov rax, rax
002F737C  48 8B DE                        mov rbx, rsi
002F737F  33 D2                           xor edx, edx
002F7381  48 2B D8                        sub rbx, rax
002F7384  48 8B CE                        mov rcx, rsi
002F7387  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002F7391  48 C1 FB 04                     sar rbx, 4
002F7395  48 0F AF D8                     imul rbx, rax
002F7399  E8 F2 69 04 00                  call 0x14033dd90
002F739E  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002F73A2  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
002F73AC  48 23 C1                        and rax, rcx
002F73AF  48 8B CE                        mov rcx, rsi
002F73B2  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002F73B6  E8 35 E6 07 00                  call 0x1403759f0
002F73BB  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002F73BF  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
002F73C9  48 0B C1                        or rax, rcx
002F73CC  BA 02 00 00 00                  mov edx, 2
002F73D1  48 8B CB                        mov rcx, rbx
002F73D4  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002F73D8  E8 43 D9 03 00                  call 0x140334d20
002F73DD  49 BB FF FF FF FF FF FF FF 7F   movabs r11, 0x7fffffffffffffff
002F73E7  F0 4C 21 5E 18                  lock and qword ptr [rsi + 0x18], r11
002F73EC  45 33 FF                        xor r15d, r15d
002F73EF  E9 CB F9 FF FF                  jmp 0x1402f6dbf
002F73F4  48 C1 EB 0C                     shr rbx, 0xc
002F73F8  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002F7402  48 23 D3                        and rdx, rbx
002F7405  41 B8 01 00 00 20               mov r8d, 0x20000001
002F740B  48 8B CF                        mov rcx, rdi
002F740E  E8 7D E1 FC FF                  call 0x1402c5590
002F7413  48 8B D8                        mov rbx, rax
002F7416  E9 07 FF FF FF                  jmp 0x1402f7322
002F741B  48 8B C3                        mov rax, rbx
002F741E  25 00 0C 00 00                  and eax, 0xc00
002F7423  48 3D 00 08 00 00               cmp rax, 0x800
002F7429  0F 84 6A FA FF FF               je 0x1402f6e99
002F742F  45 33 ED                        xor r13d, r13d
002F7432  E9 3D FD FF FF                  jmp 0x1402f7174
002F7437  48 83 E0 EF                     and rax, 0xffffffffffffffef
002F743B  E9 55 FB FF FF                  jmp 0x1402f6f95
002F7440  49 8B 1F                        mov rbx, qword ptr [r15]
002F7443  E9 2C FD FF FF                  jmp 0x1402f7174
002F7448  4D 85 ED                        test r13, r13
002F744B  0F 85 1D 03 00 00               jne 0x1402f776e
002F7451  33 C9                           xor ecx, ecx
002F7453  E8 78 17 15 00                  call 0x140448bd0
002F7458  48 8B C8                        mov rcx, rax
002F745B  4C 8B C3                        mov r8, rbx
002F745E  48 8B D7                        mov rdx, rdi
002F7461  E8 F6 07 F4 FF                  call 0x140237c5c
002F7466  E9 3C F9 FF FF                  jmp 0x1402f6da7
002F746B  F6 C3 42                        test bl, 0x42
002F746E  0F 85 AE FE FF FF               jne 0x1402f7322
002F7474  48 0F BA E3 0B                  bt rbx, 0xb
002F7479  0F 83 A3 FE FF FF               jae 0x1402f7322
002F747F  48 83 CB 42                     or rbx, 0x42
002F7483  E9 9A FE FF FF                  jmp 0x1402f7322
002F7488  F6 C3 20                        test bl, 0x20
002F748B  0F 85 A6 FC FF FF               jne 0x1402f7137
002F7491  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002F749B  48 8B C0                        mov rax, rax
002F749E  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002F74A8  48 03 C1                        add rax, rcx
002F74AB  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002F74B0  48 3B C8                        cmp rcx, rax
002F74B3  0F 82 7E FC FF FF               jb 0x1402f7137
002F74B9  41 B8 80 00 00 00               mov r8d, 0x80
002F74BF  48 8B D3                        mov rdx, rbx
002F74C2  E8 B9 B8 F9 FF                  call 0x140292d80
002F74C7  E9 6B FC FF FF                  jmp 0x1402f7137
002F74CC  49 BB FF FF FF FF FF FF FF 7F   movabs r11, 0x7fffffffffffffff
002F74D6  F0 4C 21 5E 18                  lock and qword ptr [rsi + 0x18], r11
002F74DB  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002F74E5  49 B8 28 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000028
002F74EF  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
002F74F9  E9 40 FA FF FF                  jmp 0x1402f6f3e
002F74FE  F6 44 24 28 02                  test byte ptr [rsp + 0x28], 2
002F7503  0F 85 83 00 00 00               jne 0x1402f758c
002F7509  4D 85 ED                        test r13, r13
002F750C  0F 85 8D 01 00 00               jne 0x1402f769f
002F7512  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
002F751B  0F B6 83 AC 05 00 00            movzx eax, byte ptr [rbx + 0x5ac]
002F7522  8B 8B 98 05 00 00               mov ecx, dword ptr [rbx + 0x598]
002F7528  C6 83 AC 05 00 00 01            mov byte ptr [rbx + 0x5ac], 1
002F752F  8D 34 48                        lea esi, [rax + rcx*2]
002F7532  49 8B C6                        mov rax, r14
002F7535  48 2B C7                        sub rax, rdi
002F7538  48 C1 F8 03                     sar rax, 3
002F753C  3B C1                           cmp eax, ecx
002F753E  0F 87 E9 01 00 00               ja 0x1402f772d
002F7544  48 8B D7                        mov rdx, rdi
002F7547  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002F7551  48 C1 E2 19                     shl rdx, 0x19
002F7555  48 8B C0                        mov rax, rax
002F7558  48 C1 E0 19                     shl rax, 0x19
002F755C  45 33 C9                        xor r9d, r9d
002F755F  48 2B D0                        sub rdx, rax
002F7562  45 33 C0                        xor r8d, r8d
002F7565  48 C1 FA 10                     sar rdx, 0x10
002F7569  33 C9                           xor ecx, ecx
002F756B  E8 10 79 F8 FF                  call 0x14027ee80
002F7570  85 C0                           test eax, eax
002F7572  0F 88 5D 02 00 00               js 0x1402f77d5
002F7578  40 0F B6 C6                     movzx eax, sil
002F757C  24 01                           and al, 1
002F757E  D1 EE                           shr esi, 1
002F7580  89 B3 98 05 00 00               mov dword ptr [rbx + 0x598], esi
002F7586  88 83 AC 05 00 00               mov byte ptr [rbx + 0x5ac], al
002F758C  C6 44 24 21 00                  mov byte ptr [rsp + 0x21], 0
002F7591  E9 11 F8 FF FF                  jmp 0x1402f6da7
002F7596  BA 02 00 00 00                  mov edx, 2
002F759B  48 8B CE                        mov rcx, rsi
002F759E  E8 4D D4 10 00                  call 0x1404049f0
002F75A3  48 8B F0                        mov rsi, rax
002F75A6  BA FF 03 00 00                  mov edx, 0x3ff
002F75AB  E9 57 FA FF FF                  jmp 0x1402f7007
002F75B0  4D 85 ED                        test r13, r13
002F75B3  0F 84 C6 F8 FF FF               je 0x1402f6e7f
002F75B9  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002F75BE  49 8B CD                        mov rcx, r13
002F75C1  E8 CA EA F4 FF                  call 0x140246090
002F75C6  E9 B4 F8 FF FF                  jmp 0x1402f6e7f
002F75CB  8B 05 E7 F4 CC 00               mov eax, dword ptr [rip + 0xccf4e7]
002F75D1  A8 40                           test al, 0x40
002F75D3  0F 84 85 FD FF FF               je 0x1402f735e
002F75D9  E8 B2 7E 01 00                  call 0x14030f490
002F75DE  84 C0                           test al, al
002F75E0  0F 84 78 FD FF FF               je 0x1402f735e
002F75E6  8B CB                           mov ecx, ebx
002F75E8  E8 73 7E 01 00                  call 0x14030f460
002F75ED  E9 6E FD FF FF                  jmp 0x1402f7360
002F75F2  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
002F75F7  49 8B CF                        mov rcx, r15
002F75FA  E8 11 98 02 00                  call 0x140320e10
002F75FF  49 8B 1F                        mov rbx, qword ptr [r15]
002F7602  4C 8B E8                        mov r13, rax
002F7605  F6 C3 01                        test bl, 1
002F7608  75 16                           jne 0x1402f7620
002F760A  48 0F BA E3 0B                  bt rbx, 0xb
002F760F  0F 83 5C FC FF FF               jae 0x1402f7271
002F7615  48 0F BA E3 0A                  bt rbx, 0xa
002F761A  0F 82 51 FC FF FF               jb 0x1402f7271
002F7620  B2 11                           mov dl, 0x11
002F7622  48 8B C8                        mov rcx, rax
002F7625  E8 66 EA F4 FF                  call 0x140246090
002F762A  48 8B CE                        mov rcx, rsi
002F762D  E8 1E D5 03 00                  call 0x140334b50
002F7632  83 3D E7 F6 CC 00 00            cmp dword ptr [rip + 0xccf6e7], 0
002F7639  74 0E                           je 0x1402f7649
002F763B  44 0F 20 C1                     mov rcx, cr8
002F763F  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002F7644  E8 4F E0 1F 00                  call 0x1404f5698
002F7649  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
002F764E  44 0F 22 C0                     mov cr8, rax
002F7652  45 33 ED                        xor r13d, r13d
002F7655  45 33 FF                        xor r15d, r15d
002F7658  E9 62 F7 FF FF                  jmp 0x1402f6dbf
002F765D  F6 C3 20                        test bl, 0x20
002F7660  0F 85 61 FC FF FF               jne 0x1402f72c7
002F7666  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002F7670  48 8B C0                        mov rax, rax
002F7673  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
002F767D  48 03 C1                        add rax, rcx
002F7680  4C 3B F8                        cmp r15, rax
002F7683  0F 82 3E FC FF FF               jb 0x1402f72c7
002F7689  41 B8 80 00 00 00               mov r8d, 0x80
002F768F  48 8B D3                        mov rdx, rbx
002F7692  49 8B CF                        mov rcx, r15
002F7695  E8 E6 B6 F9 FF                  call 0x140292d80
002F769A  E9 28 FC FF FF                  jmp 0x1402f72c7
002F769F  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002F76A4  49 8B CD                        mov rcx, r13
002F76A7  E8 E4 E9 F4 FF                  call 0x140246090
002F76AC  45 33 ED                        xor r13d, r13d
002F76AF  E9 5E FE FF FF                  jmp 0x1402f7512
002F76B4  4D 85 ED                        test r13, r13
002F76B7  74 0D                           je 0x1402f76c6
002F76B9  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002F76BE  49 8B CD                        mov rcx, r13
002F76C1  E8 CA E9 F4 FF                  call 0x140246090
002F76C6  44 8B 4C 24 24                  mov r9d, dword ptr [rsp + 0x24]
002F76CB  45 33 C0                        xor r8d, r8d
002F76CE  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
002F76D3  33 C9                           xor ecx, ecx
002F76D5  E8 B6 AE 03 00                  call 0x140332590
002F76DA  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
002F76DE  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
002F76E4  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
002F76E8  E9 05 FF FF FF                  jmp 0x1402f75f2
002F76ED  48 8B D7                        mov rdx, rdi
002F76F0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002F76FA  48 C1 E2 19                     shl rdx, 0x19
002F76FE  48 8B C0                        mov rax, rax
002F7701  48 C1 E0 19                     shl rax, 0x19
002F7705  4C 8B CE                        mov r9, rsi
002F7708  48 2B D0                        sub rdx, rax
002F770B  4D 8B C7                        mov r8, r15
002F770E  48 C1 FA 10                     sar rdx, 0x10
002F7712  33 C9                           xor ecx, ecx
002F7714  E8 27 50 15 00                  call 0x14044c740
002F7719  48 8B F0                        mov rsi, rax
002F771C  48 85 C0                        test rax, rax
002F771F  0F 84 97 00 00 00               je 0x1402f77bc
002F7725  49 8B 07                        mov rax, qword ptr [r15]
002F7728  E9 10 F9 FF FF                  jmp 0x1402f703d
002F772D  83 F8 0F                        cmp eax, 0xf
002F7730  B9 0F 00 00 00                  mov ecx, 0xf
002F7735  0F 47 C1                        cmova eax, ecx
002F7738  89 83 98 05 00 00               mov dword ptr [rbx + 0x598], eax
002F773E  E9 01 FE FF FF                  jmp 0x1402f7544
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F6E32(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p24;
    unsigned __int8 v_stack_p26;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p80;

    result = (unsigned int)((v_rbx) & (8));
    v_stack_p58 = result;
    if (*(unsigned __int64 *)(v_rip + 11759158) == 0) goto loc_002F6E61;
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_002F6F12;
    v_r15 = ~(*(unsigned __int64 *)(v_rip + 11759158));
    v_r15 = (v_r15) & (v_rbx);
loc_002F6E61:
    v_r15 = (v_r15) >> (16);
    v_rsi = (v_r15) & (0xFFFFFFFFFFFFF000ULL);
    v_rbx = (v_r15) & (0xFFFFFFFFFFFFF000ULL);
    if (v_r13 != 0) goto loc_002F6F1B;
loc_002F6E7F:
    if (v_rbx == v_rsi) goto loc_002F6E8D;
loc_002F6E8D:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_002F741B;
loc_002F6E99:
    result = MiLockProtoPoolPageForce(v_r15, v_stack_p20, a3, a4);
    goto loc_002F6F24;
loc_002F6F12:
    v_r15 = (v_r15) & (-17);
    goto loc_002F6E61;
loc_002F6F1B:
    if ((*(unsigned __int64 *)(v_r15)) != v_rsi) goto loc_002F75B0;
loc_002F6F24:
    v_stack_p40 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_002F7160;
loc_002F6F3E:
    v_stack_p30 = *(unsigned __int64 *)(v_r15);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_002F6F95;
    result = (unsigned int)((*(unsigned __int64 *)(v_r15)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_002F7440;
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_002F6F74;
    if (*(unsigned __int64 *)(v_rip + 11758869) != 0) goto loc_002F733F;
loc_002F6F74:
    if (*(unsigned __int64 *)(v_rip + 11758853) == 0) goto loc_002F6F95;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) != 0) goto loc_002F7437;
    result = ~(*(unsigned __int64 *)(v_rip + 11758853));
    result = (result) & (*(unsigned __int64 *)(v_r15));
loc_002F6F95:
    result = (result) >> (12);
    result = (result) & (v_stack_p20);
    if (result > (*(unsigned __int64 *)(v_rip + 11758909))) goto loc_002F6F3E;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(a3 + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002F6F3E;
    v_rbx = 0;
loc_002F6FC6:
    if (condition_is_below) goto loc_002F7350;
    if ((*(unsigned __int64 *)(v_r15)) != a6) goto loc_002F74CC;
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 40)) >> (43);
    result = (result) & ((unsigned int)(0x3FFULL));
    if (sign_flag) goto loc_002F7596;
loc_002F7007:
    if (v_r10 + a1 * 8 == 0) goto loc_002F7174;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_002F72CC;
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 40)) >> (43);
    result = (result) & ((unsigned int)(0x3FFULL));
    if (sign_flag) goto loc_002F76ED;
loc_002F703D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) >> (24));
    a1 = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 16)) >> (11);
    a2 = (unsigned int)((*(unsigned __int64 *)(v_r10 + a1 * 8 + 16)) & (0x400ULL));
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 16)) >> (3);
    if (a2 != 0) { result = (unsigned int)(a1); }
    a2 = 0;
    result = MiUnlinkPageFromListEx(v_r10 + a1 * 8, a2, a3, a4);
    if ((((unsigned __int8)(result)) & (3)) != 0) goto loc_002F736F;
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 8)) | (v_r10 + a1 * 8);
    v_stack_p30 = result;
    v_stack_p24 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) + 1);
    v_stack_p24 = (unsigned __int16)(result);
    *(unsigned int *)(v_r10 + a1 * 8 + 32) = (unsigned int)((unsigned int)(v_stack_p24));
    v_stack_p24 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    v_stack_p26 = (unsigned __int8)(result);
    *(unsigned int *)(v_r10 + a1 * 8 + 32) = (unsigned int)((unsigned int)(v_stack_p24));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) >> (16));
    a3 = ((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 16))) >> (5);
    a3 = (unsigned int)((a3) & (7));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    a2 = (v_r10 + a1 * 8) - (result);
    a2 = (a2) >> (4);
    a2 = (a2) * (result);
    result = MiMakeValidPte(v_rdi, a2, a3, a4);
    if (condition_is_below) goto loc_002F7488;
loc_002F7137:
    *(unsigned __int64 *)(a6) = result;
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 24)) & (v_rdi);
    result = (result) | (1);
    *(unsigned __int64 *)(v_r10 + a1 * 8 + 24) = result;
    goto loc_002F72FC;
loc_002F7160:
    result = (unsigned int)((*(unsigned __int64 *)(v_r15)) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002F6F3E;
loc_002F7174:
    if (*(unsigned __int64 *)(v_rip + 11758341) == 0) goto loc_002F7191;
    result = *(unsigned __int64 *)(v_r15);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11758341);
        result = ~(result);
        result = (result) & (*(unsigned __int64 *)(v_r15));
    }
    result = (result) >> (16);
    v_stack_p50 = result;
    if (((*(unsigned __int8 *)(a7 + 62)) & (12)) != 0) goto loc_002F74FE;
    if (((a5) & (1)) == 0) goto loc_002F74FE;
    v_rsi = 0;
    v_rsi = (result != 0) ? 1 : 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a7 + 56))) >> (20));
    a3 = (unsigned int)((a3) & (127));
    a1 = 0;
    result = MiInitializePageColorBase(a1, 3, a3, a13);
    a2 = 0;
    a1 = (a14) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a14)));
    a2 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(a14)));
    result = MiGetPage(a9, a2, v_rsi + 16, a14);
    v_stack_p30 = result;
    if (result == -1) goto loc_002F74FE;
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    a1 = (*(unsigned __int64 *)(v_r15)) >> (5);
    a1 = (unsigned int)((a1) & (31));
    result = MiProtectionToCacheAttribute(a1, a2, v_rsi + 16, a14);
    v_stack_p24 = (unsigned int)(result);
    result = MiPfnZeroingNeeded(v_rsi, (unsigned int)((unsigned int)(result)), v_rsi + 16, a14);
    if ((unsigned int)(result) != 0) goto loc_002F76B4;
    if (result == 0) goto loc_002F75F2;
loc_002F7271:
    result = MiReferenceControlAreaPfn(a7, a10, 1, a14);
    v_rbx = (*(unsigned __int64 *)(v_r15)) >> (5);
    v_rbx = (unsigned int)((v_rbx) & (31));
    result = MiInitializePfn(v_rsi, v_r15, (unsigned int)((unsigned int)(v_rbx)), 18);
    result = MiMakeValidPte(v_rdi, a6, (unsigned int)((unsigned int)(v_rbx)), 18);
    if (condition_is_below) goto loc_002F765D;
loc_002F72C7:
    *(unsigned __int64 *)(v_r15) = result;
    goto loc_002F730B;
loc_002F72CC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    a2 = (*(unsigned __int64 *)(v_rsi + 24) + 1) ^ (*(unsigned __int64 *)(v_rsi + 24));
    a2 = (a2) & (*(unsigned __int64 *)(v_rsi + 24));
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rsi + 24) + 1);
    *(unsigned __int64 *)(v_rsi + 24) = a2;
loc_002F72FC:
loc_002F730B:
    if (a11 != 0) goto loc_002F73F4;
    if (((a5) & (4)) != 0) goto loc_002F746B;
loc_002F7322:
    v_rbx = (result) & (-261);
    result = (unsigned int)((*(unsigned __int8 *)(v_rip + 11762523)) & (1));
    result = (result) << (8);
    result = (result) | (v_rbx);
loc_002F733F:
    if (((result) & (v_rbx)) == 0) goto loc_002F6F3E;
    goto loc_002F6F74;
loc_002F7350:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13426516)) & ((unsigned int)(v_rbx))) == 0) goto loc_002F75CB;
loc_002F735E:
loc_002F7360:
    if (!sign_flag) goto loc_002F6FC6;
    goto loc_002F7350;
loc_002F736F:
    a2 = 0;
    v_rbx = (v_rsi) - (*(unsigned __int64 *)(v_rsi + 24));
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * (*(unsigned __int64 *)(v_rsi + 24));
    result = MiRestoreTransitionPte(v_rsi, a2, (unsigned int)((unsigned int)(v_rbx)), 18);
    result = (*(unsigned __int64 *)(v_rsi + 24)) & (v_rsi);
    *(unsigned __int64 *)(v_rsi + 24) = result;
    result = MiClearPfnReuseFields(v_rsi, a2, (unsigned int)((unsigned int)(v_rbx)), 18);
    result = (*(unsigned __int64 *)(v_rsi + 24)) | (v_rsi);
    *(unsigned __int64 *)(v_rsi + 24) = result;
    result = MiInsertPageInFreeOrZeroedList(v_rbx, 2, (unsigned int)((unsigned int)(v_rbx)), 18);
    v_r15 = 0;
loc_002F73F4:
    v_rbx = (v_rbx) >> (12);
    a2 = (2) & (v_rbx);
    result = MiMakeValidPte(v_rdi, a2, (unsigned int)(0x20000001ULL), 18);
    goto loc_002F7322;
loc_002F741B:
    result = (unsigned int)((result) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002F6E99;
    v_r13 = 0;
    goto loc_002F7174;
loc_002F7437:
    result = (result) & (-17);
    goto loc_002F6F95;
loc_002F7440:
    goto loc_002F7174;
loc_002F746B:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) goto loc_002F7322;
    if (condition_is_above_or_equal) goto loc_002F7322;
    v_rbx = (*(unsigned __int64 *)(v_r15)) | (66);
    goto loc_002F7322;
loc_002F7488:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_002F7137;
    result = (result) + (v_rdi);
    if (a6 < result) goto loc_002F7137;
    result = MiCheckLinearProtectedPteAccessedBit(a6, v_rbx, 128, 18);
    goto loc_002F7137;
loc_002F74CC:
    goto loc_002F6F3E;
loc_002F74FE:
    if (((a5) & (2)) != 0) goto loc_002F758C;
    if (0 != 0) goto loc_002F769F;
loc_002F7512:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) = 1;
    result = (v_r14) - (v_rdi);
    result = (result) >> (3);
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432))))) goto loc_002F772D;
loc_002F7544:
    a2 = (v_rdi) << (25);
    result = (result) << (25);
    a4 = 0;
    a2 = (a2) - (result);
    a3 = 0;
    a2 = (a2) >> (16);
    a1 = 0;
    result = MmAccessFault(a1, a2, a3, a4);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2)) & (1));
    v_rsi = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2) >> (1));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432) = (unsigned int)(v_rsi);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) = (unsigned __int8)(result);
loc_002F758C:
    v_stack_p21 = 0;
loc_002F7596:
    result = MiLockSpecialPurposeMemoryCachedPage(v_rsi, 2, a3, a4);
    goto loc_002F7007;
loc_002F75B0:
    if (0 == 0) goto loc_002F6E7F;
    result = MiUnlockProtoPoolPage(0, v_stack_p20, a3, a4);
    goto loc_002F6E7F;
loc_002F75CB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13432039)))) & (64)) == 0) goto loc_002F735E;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_p20, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002F735E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 392)))), v_stack_p20, a3, a4);
    goto loc_002F7360;
loc_002F75F2:
    result = MiLockProtoPoolPageForce(0, v_stack_p20, a3, a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_002F7620;
    if (condition_is_above_or_equal) goto loc_002F7271;
    if (condition_is_below) goto loc_002F7271;
loc_002F7620:
    result = MiUnlockProtoPoolPage(result, 17, a3, a4);
    result = MiReleaseFreshPageAtDpc(result, 17, a3, a4);
    if ((*(unsigned int *)(v_rip + 13432551)) != 0) {
        a1 = v_cr8;
        a2 = v_stack_p20;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_r13 = 0;
    v_r15 = 0;
loc_002F765D:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (32)) != 0) goto loc_002F72C7;
    result = (v_stack_p20) + (a1);
    if (0 < result) goto loc_002F72C7;
    result = MiCheckLinearProtectedPteAccessedBit(0, *(unsigned __int64 *)(v_r15), 128, a4);
    goto loc_002F72C7;
loc_002F769F:
    result = MiUnlockProtoPoolPage(0, v_stack_p20, 128, a4);
    v_r13 = 0;
    goto loc_002F7512;
loc_002F76B4:
    if (0 != 0) {
        a2 = v_stack_p20;
        a1 = 0;
        result = MiUnlockProtoPoolPage(a1, a2, 128, a4);
    }
    a3 = 0;
    a1 = 0;
    result = MiZeroPhysicalPage(a1, a6, a3, (unsigned int)(v_stack_p24));
    result = (*(unsigned __int64 *)(result + 16)) & (-993);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_002F75F2;
loc_002F76ED:
    a2 = (v_rdi) << (25);
    result = (result) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    a1 = 0;
    result = MiHandleSpecialPurposeMemoryCachedFault(a1, a2, 0, result);
    goto loc_002F703D;
loc_002F772D:
    result = *(unsigned __int64 *)(v_r15);
    if (((unsigned int)(*(unsigned __int64 *)(v_r15))) > 15) { result = 15; }
    *(unsigned int *)(*(unsigned __int64 *)(v_r15) + 1432) = (unsigned int)(result);
    goto loc_002F7544;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F6E32(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, void *Arg6, void *Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, uint64_t Arg12, void *Arg13, int64_t Arg14)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p24;
    uint8_t v_stack_p26;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p80;

    result = (uint32_t)((local_rbx) & (8));
    v_stack_p58 = result;
    if (*(uint64_t *)(v_rip + 0xB36E36) == 0) goto loc_002F6E61;
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_002F6F12;
    local_r15 = ~(*(uint64_t *)(v_rip + 0xB36E36));
    local_r15 = (local_r15) & (local_rbx);
loc_002F6E61:
    local_r15 = (local_r15) >> (16);
    local_rsi = (local_r15) & (0xFFFFFFFFFFFFF000ULL);
    local_rbx = (local_r15) & (0xFFFFFFFFFFFFF000ULL);
    if (local_r13 != 0) goto loc_002F6F1B;
loc_002F6E7F:
    if (local_rbx == local_rsi) goto loc_002F6E8D;
loc_002F6E8D:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_002F741B;
loc_002F6E99:
    result = MiLockProtoPoolPageForce(local_r15, v_stack_p20, Arg3, Arg4);
    goto loc_002F6F24;
loc_002F6F12:
    local_r15 = (local_r15) & (-17);
    goto loc_002F6E61;
loc_002F6F1B:
    if ((*(uint64_t *)(local_r15)) != local_rsi) goto loc_002F75B0;
loc_002F6F24:
    v_stack_p40 = 0;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_002F7160;
loc_002F6F3E:
    v_stack_p30 = *(uint64_t *)(local_r15);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_002F6F95;
    result = (uint32_t)((*(uint64_t *)(local_r15)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_002F7440;
    if (*(uint64_t *)(local_r15) == 0) goto loc_002F6F74;
    if (*(uint64_t *)(v_rip + 0xB36D15) != 0) goto loc_002F733F;
loc_002F6F74:
    if (*(uint64_t *)(v_rip + 0xB36D05) == 0) goto loc_002F6F95;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) != 0) goto loc_002F7437;
    result = ~(*(uint64_t *)(v_rip + 0xB36D05));
    result = (result) & (*(uint64_t *)(local_r15));
loc_002F6F95:
    result = (result) >> (12);
    result = (result) & (v_stack_p20);
    if (result > (*(uint64_t *)(v_rip + 0xB36D3D))) goto loc_002F6F3E;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(Arg3 + Arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002F6F3E;
    local_rbx = 0;
loc_002F6FC6:
    if (condition_is_below) goto loc_002F7350;
    if ((*(uint64_t *)(local_r15)) != Arg6) goto loc_002F74CC;
    result = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x28)) >> (43);
    result = (result) & ((uint32_t)(0x3FFULL));
    if (sign_flag) goto loc_002F7596;
loc_002F7007:
    if (local_r10 + Arg1 * 8 == 0) goto loc_002F7174;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_002F72CC;
    result = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x28)) >> (43);
    result = (result) & ((uint32_t)(0x3FFULL));
    if (sign_flag) goto loc_002F76ED;
loc_002F703D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20))) >> (24));
    Arg1 = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x10)) >> (11);
    Arg2 = (uint32_t)((*(uint64_t *)(local_r10 + Arg1 * 8 + 0x10)) & (0x400ULL));
    result = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x10)) >> (3);
    if (Arg2 != 0) { result = (uint32_t)(Arg1); }
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(local_r10 + Arg1 * 8, Arg2, Arg3, Arg4);
    if ((((uint8_t)(result)) & (3)) != 0) goto loc_002F736F;
    result = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x8)) | (local_r10 + Arg1 * 8);
    v_stack_p30 = result;
    v_stack_p24 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20))) + 1);
    v_stack_p24 = (uint16_t)(result);
    *(uint32_t *)(local_r10 + Arg1 * 8 + 0x20) = (uint32_t)((uint32_t)(v_stack_p24));
    v_stack_p24 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    v_stack_p26 = (uint8_t)(result);
    *(uint32_t *)(local_r10 + Arg1 * 8 + 0x20) = (uint32_t)((uint32_t)(v_stack_p24));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x20))) >> (16));
    Arg3 = ((uint32_t)(*(uint32_t *)(local_r10 + Arg1 * 8 + 0x10))) >> (5);
    Arg3 = (uint32_t)((Arg3) & (7));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    Arg2 = (local_r10 + Arg1 * 8) - (result);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (result);
    result = MiMakeValidPte(local_rdi, Arg2, Arg3, Arg4);
    if (condition_is_below) goto loc_002F7488;
loc_002F7137:
    *(uint64_t *)(arg6) = result;
    result = (*(uint64_t *)(local_r10 + Arg1 * 8 + 0x18)) & (local_rdi);
    result = (result) | (1);
    *(uint64_t *)(local_r10 + Arg1 * 8 + 0x18) = result;
    goto loc_002F72FC;
loc_002F7160:
    result = (uint32_t)((*(uint64_t *)(local_r15)) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002F6F3E;
loc_002F7174:
    if (*(uint64_t *)(v_rip + 0xB36B05) == 0) goto loc_002F7191;
    result = *(uint64_t *)(local_r15);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xB36B05);
        result = ~(result);
        result = (result) & (*(uint64_t *)(local_r15));
    }
    result = (result) >> (16);
    v_stack_p50 = result;
    if (((*(uint8_t *)(arg7 + 0x3E)) & (12)) != 0) goto loc_002F74FE;
    if (((Arg5) & (1)) == 0) goto loc_002F74FE;
    local_rsi = 0;
    local_rsi = (result != 0) ? 1 : 0;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg7 + 0x38))) >> (20));
    Arg3 = (uint32_t)((Arg3) & (127));
    Arg1 = 0;
    result = MiInitializePageColorBase(Arg1, 3, Arg3, Arg13);
    Arg2 = 0;
    Arg1 = (Arg14) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg14)));
    Arg2 = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(Arg14)));
    result = MiGetPage(Arg9, Arg2, local_rsi + 16, Arg14);
    v_stack_p30 = result;
    if (result == -1) goto loc_002F74FE;
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    Arg1 = (*(uint64_t *)(local_r15)) >> (5);
    Arg1 = (uint32_t)((Arg1) & (31));
    result = MiProtectionToCacheAttribute(Arg1, Arg2, local_rsi + 16, Arg14);
    v_stack_p24 = (uint32_t)(result);
    result = MiPfnZeroingNeeded(local_rsi, (uint32_t)((uint32_t)(result)), local_rsi + 16, Arg14);
    if ((uint32_t)(result) != 0) goto loc_002F76B4;
    if (result == 0) goto loc_002F75F2;
loc_002F7271:
    result = MiReferenceControlAreaPfn(Arg7, Arg10, 1, Arg14);
    local_rbx = (*(uint64_t *)(local_r15)) >> (5);
    local_rbx = (uint32_t)((local_rbx) & (31));
    result = MiInitializePfn(local_rsi, local_r15, (uint32_t)((uint32_t)(local_rbx)), 18);
    result = MiMakeValidPte(local_rdi, Arg6, (uint32_t)((uint32_t)(local_rbx)), 18);
    if (condition_is_below) goto loc_002F765D;
loc_002F72C7:
    *(uint64_t *)(local_r15) = result;
    goto loc_002F730B;
loc_002F72CC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    Arg2 = (*(uint64_t *)(local_rsi + 0x18) + 1) ^ (*(uint64_t *)(local_rsi + 0x18));
    Arg2 = (Arg2) & (*(uint64_t *)(local_rsi + 0x18));
    Arg2 = (Arg2) ^ (*(uint64_t *)(local_rsi + 0x18) + 1);
    *(uint64_t *)(local_rsi + 0x18) = Arg2;
loc_002F72FC:
loc_002F730B:
    if (Arg11 != 0) goto loc_002F73F4;
    if (((Arg5) & (4)) != 0) goto loc_002F746B;
loc_002F7322:
    local_rbx = (result) & (-261);
    result = (uint32_t)((*(uint8_t *)(v_rip + 0xB37B5B)) & (1));
    result = (result) << (8);
    result = (result) | (local_rbx);
loc_002F733F:
    if (((result) & (local_rbx)) == 0) goto loc_002F6F3E;
    goto loc_002F6F74;
loc_002F7350:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xCCDF54)) & ((uint32_t)(local_rbx))) == 0) goto loc_002F75CB;
loc_002F735E:
loc_002F7360:
    if (!sign_flag) goto loc_002F6FC6;
    goto loc_002F7350;
loc_002F736F:
    Arg2 = 0;
    local_rbx = (local_rsi) - (*(uint64_t *)(local_rsi + 0x18));
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * (*(uint64_t *)(local_rsi + 0x18));
    result = MiRestoreTransitionPte(local_rsi, Arg2, (uint32_t)((uint32_t)(local_rbx)), 18);
    result = (*(uint64_t *)(local_rsi + 0x18)) & (local_rsi);
    *(uint64_t *)(local_rsi + 0x18) = result;
    result = MiClearPfnReuseFields(local_rsi, Arg2, (uint32_t)((uint32_t)(local_rbx)), 18);
    result = (*(uint64_t *)(local_rsi + 0x18)) | (local_rsi);
    *(uint64_t *)(local_rsi + 0x18) = result;
    result = MiInsertPageInFreeOrZeroedList(local_rbx, 2, (uint32_t)((uint32_t)(local_rbx)), 18);
    local_r15 = 0;
loc_002F73F4:
    local_rbx = (local_rbx) >> (12);
    Arg2 = (2) & (local_rbx);
    result = MiMakeValidPte(local_rdi, Arg2, (uint32_t)(0x20000001ULL), 18);
    goto loc_002F7322;
loc_002F741B:
    result = (uint32_t)((result) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002F6E99;
    local_r13 = 0;
    goto loc_002F7174;
loc_002F7437:
    result = (result) & (-17);
    goto loc_002F6F95;
loc_002F7440:
    goto loc_002F7174;
loc_002F746B:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) goto loc_002F7322;
    if (condition_is_above_or_equal) goto loc_002F7322;
    local_rbx = (*(uint64_t *)(local_r15)) | (66);
    goto loc_002F7322;
loc_002F7488:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_002F7137;
    result = (result) + (local_rdi);
    if (Arg6 < result) goto loc_002F7137;
    result = MiCheckLinearProtectedPteAccessedBit(Arg6, local_rbx, 128, 18);
    goto loc_002F7137;
loc_002F74CC:
    goto loc_002F6F3E;
loc_002F74FE:
    if (((Arg5) & (2)) != 0) goto loc_002F758C;
    if (0 != 0) goto loc_002F769F;
loc_002F7512:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) = 1;
    result = (local_r14) - (local_rdi);
    result = (result) >> (3);
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598))))) goto loc_002F772D;
loc_002F7544:
    Arg2 = (local_rdi) << (25);
    result = (result) << (25);
    Arg4 = 0;
    Arg2 = (Arg2) - (result);
    Arg3 = 0;
    Arg2 = (Arg2) >> (16);
    Arg1 = 0;
    result = MmAccessFault(Arg1, Arg2, Arg3, Arg4);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2)) & (1));
    local_rsi = (uint32_t)((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2) >> (1));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598) = (uint32_t)(local_rsi);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) = (uint8_t)(result);
loc_002F758C:
    v_stack_p21 = 0;
loc_002F7596:
    result = MiLockSpecialPurposeMemoryCachedPage(local_rsi, 2, Arg3, Arg4);
    goto loc_002F7007;
loc_002F75B0:
    if (0 == 0) goto loc_002F6E7F;
    result = MiUnlockProtoPoolPage(0, v_stack_p20, Arg3, Arg4);
    goto loc_002F6E7F;
loc_002F75CB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCCF4E7)))) & (64)) == 0) goto loc_002F735E;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_p20, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002F735E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x188)))), v_stack_p20, Arg3, Arg4);
    goto loc_002F7360;
loc_002F75F2:
    result = MiLockProtoPoolPageForce(0, v_stack_p20, Arg3, Arg4);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_002F7620;
    if (condition_is_above_or_equal) goto loc_002F7271;
    if (condition_is_below) goto loc_002F7271;
loc_002F7620:
    result = MiUnlockProtoPoolPage(result, 17, Arg3, Arg4);
    result = MiReleaseFreshPageAtDpc(result, 17, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xCCF6E7)) != 0) {
        Arg1 = v_cr8;
        Arg2 = v_stack_p20;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_r13 = 0;
    local_r15 = 0;
loc_002F765D:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (32)) != 0) goto loc_002F72C7;
    result = (v_stack_p20) + (Arg1);
    if (0 < result) goto loc_002F72C7;
    result = MiCheckLinearProtectedPteAccessedBit(0, *(uint64_t *)(local_r15), 128, Arg4);
    goto loc_002F72C7;
loc_002F769F:
    result = MiUnlockProtoPoolPage(0, v_stack_p20, 128, Arg4);
    local_r13 = 0;
    goto loc_002F7512;
loc_002F76B4:
    if (0 != 0) {
        Arg2 = v_stack_p20;
        Arg1 = 0;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, 128, Arg4);
    }
    Arg3 = 0;
    Arg1 = 0;
    result = MiZeroPhysicalPage(Arg1, Arg6, Arg3, (uint32_t)(v_stack_p24));
    result = (*(uint64_t *)(result + 0x10)) & (-993);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_002F75F2;
loc_002F76ED:
    Arg2 = (local_rdi) << (25);
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    Arg1 = 0;
    result = MiHandleSpecialPurposeMemoryCachedFault(Arg1, Arg2, 0, result);
    goto loc_002F703D;
loc_002F772D:
    result = *(uint64_t *)(local_r15);
    if (((uint32_t)(*(uint64_t *)(local_r15))) > 15) { result = 15; }
    *(uint32_t *)(*(uint64_t *)(local_r15) + 0x598) = (uint32_t)(result);
    goto loc_002F7544;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x38` | `32` | `R` |
| `Arg7` | `+ 0x3E` | `8` | `R` |
| `Arg13` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F6E32&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
