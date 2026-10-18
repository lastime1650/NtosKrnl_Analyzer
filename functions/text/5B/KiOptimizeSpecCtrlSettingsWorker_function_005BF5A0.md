# KiOptimizeSpecCtrlSettingsWorker

- RVA: `0x005BF5A0`–`0x005C039F` (길이 `3,583` bytes)
- VA: `0x00000001405BF5A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA5E4`
- 디코드: `805`개 명령, `3,583/3,583` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x005BF5EE` → [HvlIsCoreSharingPossible](../58/HvlIsCoreSharingPossible_function_00583B38.md) (function, `0x00583B38`)
- `0x005BF638` → [KiDetectAmdNonArchSsbdSupport](KiDetectAmdNonArchSsbdSupport_function_005BEB64.md) (function, `0x005BEB64`)
- `0x005BF6F9` → [HvlIsCoreSharingPossible](../58/HvlIsCoreSharingPossible_function_00583B38.md) (function, `0x00583B38`)
- `0x005BF806` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x005BF848` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x005BF858` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x005BF8B1` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x005BF8D8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x005BFB79` → [KiSetMicrocodeUpdateOptions](../4F/KiSetMicrocodeUpdateOptions_function_004FADE4.md) (function, `0x004FADE4`)
- `0x005BFB81` → [KiSetVirtualMitigationControl](../4F/KiSetVirtualMitigationControl_function_004FD38C.md) (function, `0x004FD38C`)
- `0x005BFC9C` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x005BFCCF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x005BFCDF` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x005BFD38` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x005BFD63` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x005BFDA0` → [KeExitRetpoline](../46/KeExitRetpoline_function_00468E7C.md) (function, `0x00468E7C`)
- `0x005BFE72` → [HvlIsCoreSharingPossible](../58/HvlIsCoreSharingPossible_function_00583B38.md) (function, `0x00583B38`)
- `0x005BFEF2` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005BFF6B` → [HvlIsCoreSharingPossible](../58/HvlIsCoreSharingPossible_function_00583B38.md) (function, `0x00583B38`)
- `0x005C0006` → [KiIsBranchConfusionPresent](KiIsBranchConfusionPresent_function_005BF2E8.md) (function, `0x005BF2E8`)
- `0x005C0025` → [KiIsBranchConfusionMitigationDesired](KiIsBranchConfusionMitigationDesired_function_005BF27C.md) (function, `0x005BF27C`)
- `0x005C0041` → [KiIsBranchConfusionMitigationSupported](KiIsBranchConfusionMitigationSupported_function_005BF2BC.md) (function, `0x005BF2BC`)
- `0x005C006A` → [KiIsTsaMitigationDesired](KiIsTsaMitigationDesired_function_005BF438.md) (function, `0x005BF438`)
- `0x005C0082` → [KiIsTsaMitigationSupported](KiIsTsaMitigationSupported_function_005BF454.md) (function, `0x005BF454`)
- `0x005C01C0` → [KiIsBranchConfusionPresent](KiIsBranchConfusionPresent_function_005BF2E8.md) (function, `0x005BF2E8`)
- `0x005C01D0` → [KiIsBranchConfusionMitigationSupported](KiIsBranchConfusionMitigationSupported_function_005BF2BC.md) (function, `0x005BF2BC`)
- `0x005C01E3` → [KiIsBranchConfusionMitigationDesired](KiIsBranchConfusionMitigationDesired_function_005BF27C.md) (function, `0x005BF27C`)
- `0x005C0242` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x005C0275` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x005C0285` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x005C02DC` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x005C0307` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x005C032E` → [KiUpdateSpeculationControl](../3E/KiUpdateSpeculationControl_function_003E63E0.md) (function, `0x003E63E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005BF5DA` → RVA `0x00FC6B48` (`ALMOSTRO`; read/write)
- `0x005BF5E5` → RVA `0x00FC6A97` (`ALMOSTRO`; read)
- `0x005BF5FF` → RVA `0x00F10EC0` (`.data`; read)
- `0x005BF62E` → RVA `0x00FC6B48` (`ALMOSTRO`; read)
- `0x005BF67E` → RVA `0x00E0B1F8` (`.data`; read)
- `0x005BF6EE` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x005BF781` → RVA `0x01201840` (`CFGRO`; read)
- `0x005BF82D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x005BF83A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x005BF861` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x005BFA8B` → RVA `0x00FC6B54` (`ALMOSTRO`; read)
- `0x005BFB69` → RVA `0x00E0B1F0` (`.data`; read)
- `0x005BFE90` → RVA `0x00FC6CEC` (`ALMOSTRO`; read)
- `0x005BFEE8` → RVA `0x00F231B8` (`.data`; read)
- `0x005C01AF` → RVA `0x00F10EC0` (`.data`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BF5A0  40 55                           push rbp
005BF5A2  53                              push rbx
005BF5A3  56                              push rsi
005BF5A4  57                              push rdi
005BF5A5  41 54                           push r12
005BF5A7  41 55                           push r13
005BF5A9  41 56                           push r14
005BF5AB  41 57                           push r15
005BF5AD  48 8B EC                        mov rbp, rsp
005BF5B0  48 83 EC 38                     sub rsp, 0x38
005BF5B4  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
005BF5BD  48 8B F1                        mov rsi, rcx
005BF5C0  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
005BF5C4  41 BF 02 00 00 00               mov r15d, 2
005BF5CA  48 8B 93 60 8E 00 00            mov rdx, qword ptr [rbx + 0x8e60]
005BF5D1  48 8D 42 FF                     lea rax, [rdx - 1]
005BF5D5  48 85 C2                        test rdx, rax
005BF5D8  74 08                           je 0x1405bf5e2
005BF5DA  F0 4C 09 3D 66 75 A0 00         lock or qword ptr [rip + 0xa07566], r15
005BF5E2  45 33 ED                        xor r13d, r13d
005BF5E5  44 38 2D AB 74 A0 00            cmp byte ptr [rip + 0xa074ab], r13b
005BF5EC  74 11                           je 0x1405bf5ff
005BF5EE  E8 45 45 FC FF                  call 0x140583b38
005BF5F3  84 C0                           test al, al
005BF5F5  74 08                           je 0x1405bf5ff
005BF5F7  F0 4C 09 3D 49 75 A0 00         lock or qword ptr [rip + 0xa07549], r15
005BF5FF  8B 05 BB 18 95 00               mov eax, dword ptr [rip + 0x9518bb]
005BF605  BF 80 00 00 00                  mov edi, 0x80
005BF60A  48 B9 00 00 00 00 00 01 00 00   movabs rcx, 0x10000000000
005BF614  40 84 C7                        test dil, al
005BF617  74 08                           je 0x1405bf621
005BF619  F0 48 09 0D 27 75 A0 00         lock or qword ptr [rip + 0xa07527], rcx
005BF621  B9 01 00 00 00                  mov ecx, 1
005BF626  38 8B 8D 00 00 00               cmp byte ptr [rbx + 0x8d], cl
005BF62C  75 14                           jne 0x1405bf642
005BF62E  48 8D 15 13 75 A0 00            lea rdx, [rip + 0xa07513]
005BF635  48 8B CB                        mov rcx, rbx
005BF638  E8 27 F5 FF FF                  call 0x1405beb64
005BF63D  B9 01 00 00 00                  mov ecx, 1
005BF642  48 8B 05 FF 74 A0 00            mov rax, qword ptr [rip + 0xa074ff]
005BF649  48 BA 00 00 00 00 40 00 00 00   movabs rdx, 0x4000000000
005BF653  49 BC 00 00 00 00 80 00 00 00   movabs r12, 0x8000000000
005BF65D  40 84 C7                        test dil, al
005BF660  74 37                           je 0x1405bf699
005BF662  48 8B 05 DF 74 A0 00            mov rax, qword ptr [rip + 0xa074df]
005BF669  48 0F BA E0 08                  bt rax, 8
005BF66E  72 29                           jb 0x1405bf699
005BF670  8B 05 4A 18 95 00               mov eax, dword ptr [rip + 0x95184a]
005BF676  A8 08                           test al, 8
005BF678  75 17                           jne 0x1405bf691
005BF67A  A8 10                           test al, 0x10
005BF67C  74 1B                           je 0x1405bf699
005BF67E  83 3D 73 BB 84 00 48            cmp dword ptr [rip + 0x84bb73], 0x48
005BF685  75 0A                           jne 0x1405bf691
005BF687  F0 4C 09 25 B9 74 A0 00         lock or qword ptr [rip + 0xa074b9], r12
005BF68F  EB 08                           jmp 0x1405bf699
005BF691  F0 48 09 15 AF 74 A0 00         lock or qword ptr [rip + 0xa074af], rdx
005BF699  48 8B 05 A8 74 A0 00            mov rax, qword ptr [rip + 0xa074a8]
005BF6A0  BA 04 00 00 00                  mov edx, 4
005BF6A5  48 BF 00 00 00 00 08 00 00 00   movabs rdi, 0x800000000
005BF6AF  84 C2                           test dl, al
005BF6B1  75 08                           jne 0x1405bf6bb
005BF6B3  F0 48 09 3D 8D 74 A0 00         lock or qword ptr [rip + 0xa0748d], rdi
005BF6BB  8B 05 FF 17 95 00               mov eax, dword ptr [rip + 0x9517ff]
005BF6C1  49 BE 00 00 00 00 04 00 00 00   movabs r14, 0x400000000
005BF6CB  84 C2                           test dl, al
005BF6CD  74 0A                           je 0x1405bf6d9
005BF6CF  F0 4C 09 35 71 74 A0 00         lock or qword ptr [rip + 0xa07471], r14
005BF6D7  EB 4C                           jmp 0x1405bf725
005BF6D9  84 C1                           test cl, al
005BF6DB  74 48                           je 0x1405bf725
005BF6DD  F0 4C 09 35 63 74 A0 00         lock or qword ptr [rip + 0xa07463], r14
005BF6E5  44 38 2D AB 73 A0 00            cmp byte ptr [rip + 0xa073ab], r13b
005BF6EC  74 37                           je 0x1405bf725
005BF6EE  8B 05 9C 73 A0 00               mov eax, dword ptr [rip + 0xa0739c]
005BF6F4  41 84 C7                        test r15b, al
005BF6F7  74 2C                           je 0x1405bf725
005BF6F9  E8 3A 44 FC FF                  call 0x140583b38
005BF6FE  84 C0                           test al, al
005BF700  74 23                           je 0x1405bf725
005BF702  48 8B 05 3F 74 A0 00            mov rax, qword ptr [rip + 0xa0743f]
005BF709  A8 40                           test al, 0x40
005BF70B  74 18                           je 0x1405bf725
005BF70D  66 44 89 BB E8 06 00 00         mov word ptr [rbx + 0x6e8], r15w
005BF715  66 44 89 BB EC 06 00 00         mov word ptr [rbx + 0x6ec], r15w
005BF71D  66 44 89 BB E2 06 00 00         mov word ptr [rbx + 0x6e2], r15w
005BF725  F7 05 91 17 95 00 00 00 00 02   test dword ptr [rip + 0x951791], 0x2000000
005BF72F  74 12                           je 0x1405bf743
005BF731  48 B8 00 00 00 00 00 40 00 00   movabs rax, 0x400000000000
005BF73B  F0 48 09 05 05 74 A0 00         lock or qword ptr [rip + 0xa07405], rax
005BF743  48 8B 05 FE 73 A0 00            mov rax, qword ptr [rip + 0xa073fe]
005BF74A  48 B9 00 00 00 00 00 00 08 00   movabs rcx, 0x8000000000000
005BF754  48 0F BA E0 17                  bt rax, 0x17
005BF759  73 4B                           jae 0x1405bf7a6
005BF75B  48 8B 05 E6 73 A0 00            mov rax, qword ptr [rip + 0xa073e6]
005BF762  48 0F BA E0 18                  bt rax, 0x18
005BF767  72 0C                           jb 0x1405bf775
005BF769  48 B8 00 00 00 00 00 00 04 00   movabs rax, 0x4000000000000
005BF773  EB 29                           jmp 0x1405bf79e
005BF775  F7 05 41 17 95 00 00 00 00 08   test dword ptr [rip + 0x951741], 0x8000000
005BF77F  75 13                           jne 0x1405bf794
005BF781  44 38 2D B8 20 C4 00            cmp byte ptr [rip + 0xc420b8], r13b
005BF788  75 1C                           jne 0x1405bf7a6
005BF78A  F0 48 09 0D B6 73 A0 00         lock or qword ptr [rip + 0xa073b6], rcx
005BF792  EB 12                           jmp 0x1405bf7a6
005BF794  48 B8 00 00 00 00 00 00 02 00   movabs rax, 0x2000000000000
005BF79E  F0 48 09 05 A2 73 A0 00         lock or qword ptr [rip + 0xa073a2], rax
005BF7A6  48 8B 05 9B 73 A0 00            mov rax, qword ptr [rip + 0xa0739b]
005BF7AD  48 85 C1                        test rcx, rax
005BF7B0  74 18                           je 0x1405bf7ca
005BF7B2  B8 00 02 00 00                  mov eax, 0x200
005BF7B7  66 09 83 D8 06 00 00            or word ptr [rbx + 0x6d8], ax
005BF7BE  B8 18 00 00 00                  mov eax, 0x18
005BF7C3  66 89 83 AA AE 00 00            mov word ptr [rbx + 0xaeaa], ax
005BF7CA  48 85 F6                        test rsi, rsi
005BF7CD  0F 84 46 01 00 00               je 0x1405bf919
005BF7D3  44 89 6D 48                     mov dword ptr [rbp + 0x48], r13d
005BF7D7  83 C8 FF                        or eax, 0xffffffff
005BF7DA  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
005BF7DE  FF C8                           dec eax
005BF7E0  8B F8                           mov edi, eax
005BF7E2  F7 D7                           not edi
005BF7E4  81 E7 00 00 00 80               and edi, 0x80000000
005BF7EA  A9 FF FF FF 3F                  test eax, 0x3fffffff
005BF7EF  75 1F                           jne 0x1405bf810
005BF7F1  0B 7E 04                        or edi, dword ptr [rsi + 4]
005BF7F4  87 3E                           xchg dword ptr [rsi], edi
005BF7F6  89 7D 48                        mov dword ptr [rbp + 0x48], edi
005BF7F9  0F BA E7 1E                     bt edi, 0x1e
005BF7FD  0F 83 0C 01 00 00               jae 0x1405bf90f
005BF803  48 8B CE                        mov rcx, rsi
005BF806  E8 15 84 C5 FF                  call 0x140217c20
005BF80B  E9 FF 00 00 00                  jmp 0x1405bf90f
005BF810  8B 06                           mov eax, dword ptr [rsi]
005BF812  45 8B FD                        mov r15d, r13d
005BF815  25 00 00 00 80                  and eax, 0x80000000
005BF81A  45 8B E5                        mov r12d, r13d
005BF81D  3B C7                           cmp eax, edi
005BF81F  0F 84 D9 00 00 00               je 0x1405bf8fe
005BF825  BB 01 00 00 00                  mov ebx, 1
005BF82A  44 03 FB                        add r15d, ebx
005BF82D  44 85 3D 78 5A A0 00            test dword ptr [rip + 0xa05a78], r15d
005BF834  0F 85 A5 00 00 00               jne 0x1405bf8df
005BF83A  8B 05 78 72 A0 00               mov eax, dword ptr [rip + 0xa07278]
005BF840  A8 40                           test al, 0x40
005BF842  0F 84 97 00 00 00               je 0x1405bf8df
005BF848  E8 43 FC D4 FF                  call 0x14030f490
005BF84D  84 C0                           test al, al
005BF84F  0F 84 8A 00 00 00               je 0x1405bf8df
005BF855  44 03 E3                        add r12d, ebx
005BF858  E8 CF C9 F3 FF                  call 0x1404fc22c
005BF85D  84 C0                           test al, al
005BF85F  74 74                           je 0x1405bf8d5
005BF861  F7 05 CD 72 A0 00 00 00 02 00   test dword ptr [rip + 0xa072cd], 0x20000
005BF86B  74 68                           je 0x1405bf8d5
005BF86D  41 F6 C4 07                     test r12b, 7
005BF871  75 62                           jne 0x1405bf8d5
005BF873  8B 0E                           mov ecx, dword ptr [rsi]
005BF875  8B C1                           mov eax, ecx
005BF877  25 00 00 00 80                  and eax, 0x80000000
005BF87C  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
005BF87F  3B C7                           cmp eax, edi
005BF881  74 5E                           je 0x1405bf8e1
005BF883  8B D1                           mov edx, ecx
005BF885  44 8B C1                        mov r8d, ecx
005BF888  41 BD 04 00 00 00               mov r13d, 4
005BF88E  0F BA E9 1E                     bts ecx, 0x1e
005BF892  8B C2                           mov eax, edx
005BF894  44 8B F1                        mov r14d, ecx
005BF897  F0 44 0F B1 36                  lock cmpxchg dword ptr [rsi], r14d
005BF89C  8B C8                           mov ecx, eax
005BF89E  41 3B C0                        cmp eax, r8d
005BF8A1  75 1A                           jne 0x1405bf8bd
005BF8A3  44 89 75 48                     mov dword ptr [rbp + 0x48], r14d
005BF8A7  4D 8B C5                        mov r8, r13
005BF8AA  48 8D 55 48                     lea rdx, [rbp + 0x48]
005BF8AE  48 8B CE                        mov rcx, rsi
005BF8B1  E8 86 C1 F3 FF                  call 0x1404fba3c
005BF8B6  8B 0E                           mov ecx, dword ptr [rsi]
005BF8B8  41 3B CE                        cmp ecx, r14d
005BF8BB  74 EA                           je 0x1405bf8a7
005BF8BD  8B C1                           mov eax, ecx
005BF8BF  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
005BF8C2  25 00 00 00 80                  and eax, 0x80000000
005BF8C7  8B D1                           mov edx, ecx
005BF8C9  44 8B C1                        mov r8d, ecx
005BF8CC  3B C7                           cmp eax, edi
005BF8CE  75 BE                           jne 0x1405bf88e
005BF8D0  45 33 ED                        xor r13d, r13d
005BF8D3  EB 0C                           jmp 0x1405bf8e1
005BF8D5  41 8B CF                        mov ecx, r15d
005BF8D8  E8 83 FB D4 FF                  call 0x14030f460
005BF8DD  EB 02                           jmp 0x1405bf8e1
005BF8DF  F3 90                           pause
005BF8E1  8B 06                           mov eax, dword ptr [rsi]
005BF8E3  25 00 00 00 80                  and eax, 0x80000000
005BF8E8  3B C7                           cmp eax, edi
005BF8EA  0F 85 3A FF FF FF               jne 0x1405bf82a
005BF8F0  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
005BF8F4  49 BE 00 00 00 00 04 00 00 00   movabs r14, 0x400000000
005BF8FE  90                              nop
005BF8FF  41 BF 02 00 00 00               mov r15d, 2
005BF905  49 BC 00 00 00 00 80 00 00 00   movabs r12, 0x8000000000
005BF90F  48 BF 00 00 00 00 08 00 00 00   movabs rdi, 0x800000000
005BF919  48 8B 05 28 72 A0 00            mov rax, qword ptr [rip + 0xa07228]
005BF920  49 85 C6                        test r14, rax
005BF923  0F 85 0F 0A 00 00               jne 0x1405c0338
005BF929  48 8B 05 18 72 A0 00            mov rax, qword ptr [rip + 0xa07218]
005BF930  48 85 C7                        test rdi, rax
005BF933  0F 85 FF 09 00 00               jne 0x1405c0338
005BF939  48 B8 00 00 00 00 10 00 00 00   movabs rax, 0x1000000000
005BF943  F0 48 09 05 FD 71 A0 00         lock or qword ptr [rip + 0xa071fd], rax
005BF94B  44 08 BB DC 06 00 00            or byte ptr [rbx + 0x6dc], r15b
005BF952  41 BE 01 00 00 00               mov r14d, 1
005BF958  48 8B 05 E9 71 A0 00            mov rax, qword ptr [rip + 0xa071e9]
005BF95F  BF 00 40 00 00                  mov edi, 0x4000
005BF964  49 BA 00 00 00 00 00 00 10 00   movabs r10, 0x10000000000000
005BF96E  41 B9 00 04 00 00               mov r9d, 0x400
005BF974  49 BB 00 00 00 00 00 00 20 00   movabs r11, 0x20000000000000
005BF97E  41 84 C6                        test r14b, al
005BF981  0F 84 13 02 00 00               je 0x1405bfb9a
005BF987  48 8B 05 BA 71 A0 00            mov rax, qword ptr [rip + 0xa071ba]
005BF98E  41 0F B7 CE                     movzx ecx, r14w
005BF992  48 85 C7                        test rdi, rax
005BF995  74 04                           je 0x1405bf99b
005BF997  41 8D 4E 02                     lea ecx, [r14 + 2]
005BF99B  66 89 8B E8 06 00 00            mov word ptr [rbx + 0x6e8], cx
005BF9A2  66 89 8B EC 06 00 00            mov word ptr [rbx + 0x6ec], cx
005BF9A9  66 89 8B E2 06 00 00            mov word ptr [rbx + 0x6e2], cx
005BF9B0  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
005BF9BA  48 8B 05 87 71 A0 00            mov rax, qword ptr [rip + 0xa07187]
005BF9C1  48 85 C1                        test rcx, rax
005BF9C4  75 0C                           jne 0x1405bf9d2
005BF9C6  48 8B 05 7B 71 A0 00            mov rax, qword ptr [rip + 0xa0717b]
005BF9CD  49 85 C4                        test r12, rax
005BF9D0  74 29                           je 0x1405bf9fb
005BF9D2  83 3D 1F B8 84 00 48            cmp dword ptr [rip + 0x84b81f], 0x48
005BF9D9  0F B7 83 E8 06 00 00            movzx eax, word ptr [rbx + 0x6e8]
005BF9E0  75 04                           jne 0x1405bf9e6
005BF9E2  66 83 C8 04                     or ax, 4
005BF9E6  66 89 83 E8 06 00 00            mov word ptr [rbx + 0x6e8], ax
005BF9ED  66 89 83 EC 06 00 00            mov word ptr [rbx + 0x6ec], ax
005BF9F4  66 89 83 E2 06 00 00            mov word ptr [rbx + 0x6e2], ax
005BF9FB  66 44 89 B3 EA 06 00 00         mov word ptr [rbx + 0x6ea], r14w
005BFA03  48 8B 05 3E 71 A0 00            mov rax, qword ptr [rip + 0xa0713e]
005BFA0A  48 85 C1                        test rcx, rax
005BFA0D  75 0C                           jne 0x1405bfa1b
005BFA0F  48 8B 05 32 71 A0 00            mov rax, qword ptr [rip + 0xa07132]
005BFA16  49 85 C4                        test r12, rax
005BFA19  74 15                           je 0x1405bfa30
005BFA1B  83 3D D6 B7 84 00 48            cmp dword ptr [rip + 0x84b7d6], 0x48
005BFA22  75 0C                           jne 0x1405bfa30
005BFA24  B8 04 00 00 00                  mov eax, 4
005BFA29  66 09 83 EA 06 00 00            or word ptr [rbx + 0x6ea], ax
005BFA30  48 8B 05 11 71 A0 00            mov rax, qword ptr [rip + 0xa07111]
005BFA37  48 85 C7                        test rdi, rax
005BFA3A  74 08                           je 0x1405bfa44
005BFA3C  66 44 09 BB EA 06 00 00         or word ptr [rbx + 0x6ea], r15w
005BFA44  48 8B 05 FD 70 A0 00            mov rax, qword ptr [rip + 0xa070fd]
005BFA4B  41 B8 80 00 00 00               mov r8d, 0x80
005BFA51  48 0F BA E0 0D                  bt rax, 0xd
005BFA56  73 08                           jae 0x1405bfa60
005BFA58  66 44 09 83 EA 06 00 00         or word ptr [rbx + 0x6ea], r8w
005BFA60  48 8B 05 E1 70 A0 00            mov rax, qword ptr [rip + 0xa070e1]
005BFA67  48 0F BA E0 10                  bt rax, 0x10
005BFA6C  0F 83 9D 00 00 00               jae 0x1405bfb0f
005BFA72  F7 05 44 14 95 00 00 00 80 00   test dword ptr [rip + 0x951444], 0x800000
005BFA7C  75 0D                           jne 0x1405bfa8b
005BFA7E  F0 4C 09 15 C2 70 A0 00         lock or qword ptr [rip + 0xa070c2], r10
005BFA86  E9 84 00 00 00                  jmp 0x1405bfb0f
005BFA8B  8A 05 C3 70 A0 00               mov al, byte ptr [rip + 0xa070c3]
005BFA91  84 C0                           test al, al
005BFA93  74 30                           je 0x1405bfac5
005BFA95  48 B8 00 00 00 00 00 00 80 00   movabs rax, 0x80000000000000
005BFA9F  F0 48 09 05 A1 70 A0 00         lock or qword ptr [rip + 0xa070a1], rax
005BFAA7  8A 0D A7 70 A0 00               mov cl, byte ptr [rip + 0xa070a7]
005BFAAD  8A 83 DC 06 00 00               mov al, byte ptr [rbx + 0x6dc]
005BFAB3  80 E1 03                        and cl, 3
005BFAB6  C0 E1 04                        shl cl, 4
005BFAB9  24 CF                           and al, 0xcf
005BFABB  0A C8                           or cl, al
005BFABD  88 8B DC 06 00 00               mov byte ptr [rbx + 0x6dc], cl
005BFAC3  EB 4A                           jmp 0x1405bfb0f
005BFAC5  48 8B 05 7C 70 A0 00            mov rax, qword ptr [rip + 0xa0707c]
005BFACC  48 0F BA E0 11                  bt rax, 0x11
005BFAD1  73 34                           jae 0x1405bfb07
005BFAD3  48 B8 00 00 00 00 00 00 40 00   movabs rax, 0x40000000000000
005BFADD  F0 48 09 05 63 70 A0 00         lock or qword ptr [rip + 0xa07063], rax
005BFAE5  66 44 09 8B E8 06 00 00         or word ptr [rbx + 0x6e8], r9w
005BFAED  66 44 09 8B E2 06 00 00         or word ptr [rbx + 0x6e2], r9w
005BFAF5  66 44 09 8B EC 06 00 00         or word ptr [rbx + 0x6ec], r9w
005BFAFD  66 44 09 8B EA 06 00 00         or word ptr [rbx + 0x6ea], r9w
005BFB05  EB 08                           jmp 0x1405bfb0f
005BFB07  F0 4C 09 1D 39 70 A0 00         lock or qword ptr [rip + 0xa07039], r11
005BFB0F  48 8B 05 32 70 A0 00            mov rax, qword ptr [rip + 0xa07032]
005BFB16  49 85 C4                        test r12, rax
005BFB19  0F 85 81 00 00 00               jne 0x1405bfba0
005BFB1F  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
005BFB29  0F B7 83 E8 06 00 00            movzx eax, word ptr [rbx + 0x6e8]
005BFB30  66 89 83 E6 06 00 00            mov word ptr [rbx + 0x6e6], ax
005BFB37  66 85 C0                        test ax, ax
005BFB3A  74 0D                           je 0x1405bfb49
005BFB3C  8B D0                           mov edx, eax
005BFB3E  B9 48 00 00 00                  mov ecx, 0x48
005BFB43  48 C1 EA 20                     shr rdx, 0x20
005BFB47  0F 30                           wrmsr
005BFB49  48 8B 05 F8 6F A0 00            mov rax, qword ptr [rip + 0xa06ff8]
005BFB50  49 85 C0                        test r8, rax
005BFB53  74 24                           je 0x1405bfb79
005BFB55  8B 0D 9D B6 84 00               mov ecx, dword ptr [rip + 0x84b69d]
005BFB5B  83 F9 48                        cmp ecx, 0x48
005BFB5E  74 19                           je 0x1405bfb79
005BFB60  0F 32                           rdmsr
005BFB62  48 C1 E2 20                     shl rdx, 0x20
005BFB66  48 0B C2                        or rax, rdx
005BFB69  48 0B 05 80 B6 84 00            or rax, qword ptr [rip + 0x84b680]
005BFB70  48 8B D0                        mov rdx, rax
005BFB73  48 C1 EA 20                     shr rdx, 0x20
005BFB77  0F 30                           wrmsr
005BFB79  E8 66 B2 F3 FF                  call 0x1404fade4
005BFB7E  48 8B CB                        mov rcx, rbx
005BFB81  E8 06 D8 F3 FF                  call 0x1404fd38c
005BFB86  33 C0                           xor eax, eax
005BFB88  48 83 C4 38                     add rsp, 0x38
005BFB8C  41 5F                           pop r15
005BFB8E  41 5E                           pop r14
005BFB90  41 5D                           pop r13
005BFB92  41 5C                           pop r12
005BFB94  5F                              pop rdi
005BFB95  5E                              pop rsi
005BFB96  5B                              pop rbx
005BFB97  5D                              pop rbp
005BFB98  C3                              ret
005BFB99  CC                              int3
005BFB9A  41 B8 80 00 00 00               mov r8d, 0x80
005BFBA0  48 8B 05 A1 6F A0 00            mov rax, qword ptr [rip + 0xa06fa1]
005BFBA7  A8 10                           test al, 0x10
005BFBA9  74 0A                           je 0x1405bfbb5
005BFBAB  66 44 89 B3 EA 06 00 00         mov word ptr [rbx + 0x6ea], r14w
005BFBB3  EB 1F                           jmp 0x1405bfbd4
005BFBB5  48 8B 05 8C 6F A0 00            mov rax, qword ptr [rip + 0xa06f8c]
005BFBBC  A8 40                           test al, 0x40
005BFBBE  74 14                           je 0x1405bfbd4
005BFBC0  48 8B 05 81 6F A0 00            mov rax, qword ptr [rip + 0xa06f81]
005BFBC7  41 84 C7                        test r15b, al
005BFBCA  74 08                           je 0x1405bfbd4
005BFBCC  66 44 89 BB EA 06 00 00         mov word ptr [rbx + 0x6ea], r15w
005BFBD4  48 8B 05 6D 6F A0 00            mov rax, qword ptr [rip + 0xa06f6d]
005BFBDB  48 85 C7                        test rdi, rax
005BFBDE  74 08                           je 0x1405bfbe8
005BFBE0  66 44 09 BB EA 06 00 00         or word ptr [rbx + 0x6ea], r15w
005BFBE8  48 8B 05 59 6F A0 00            mov rax, qword ptr [rip + 0xa06f59]
005BFBEF  48 0F BA E0 0D                  bt rax, 0xd
005BFBF4  73 08                           jae 0x1405bfbfe
005BFBF6  66 44 09 83 EA 06 00 00         or word ptr [rbx + 0x6ea], r8w
005BFBFE  48 8B 05 43 6F A0 00            mov rax, qword ptr [rip + 0xa06f43]
005BFC05  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
005BFC0F  49 85 C0                        test r8, rax
005BFC12  75 0C                           jne 0x1405bfc20
005BFC14  48 8B 05 2D 6F A0 00            mov rax, qword ptr [rip + 0xa06f2d]
005BFC1B  49 85 C4                        test r12, rax
005BFC1E  74 15                           je 0x1405bfc35
005BFC20  83 3D D1 B5 84 00 48            cmp dword ptr [rip + 0x84b5d1], 0x48
005BFC27  75 0C                           jne 0x1405bfc35
005BFC29  B8 04 00 00 00                  mov eax, 4
005BFC2E  66 09 83 EA 06 00 00            or word ptr [rbx + 0x6ea], ax
005BFC35  48 8B 05 0C 6F A0 00            mov rax, qword ptr [rip + 0xa06f0c]
005BFC3C  41 84 C6                        test r14b, al
005BFC3F  0F 85 E4 FE FF FF               jne 0x1405bfb29
005BFC45  44 38 B3 8D 00 00 00            cmp byte ptr [rbx + 0x8d], r14b
005BFC4C  75 12                           jne 0x1405bfc60
005BFC4E  48 B8 00 00 00 00 00 00 00 01   movabs rax, 0x100000000000000
005BFC58  F0 48 09 05 E8 6E A0 00         lock or qword ptr [rip + 0xa06ee8], rax
005BFC60  48 85 F6                        test rsi, rsi
005BFC63  0F 84 1E 01 00 00               je 0x1405bfd87
005BFC69  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
005BFC6D  83 C8 FF                        or eax, 0xffffffff
005BFC70  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
005BFC74  FF C8                           dec eax
005BFC76  8B F8                           mov edi, eax
005BFC78  F7 D7                           not edi
005BFC7A  81 E7 00 00 00 80               and edi, 0x80000000
005BFC80  A9 FF FF FF 3F                  test eax, 0x3fffffff
005BFC85  75 1F                           jne 0x1405bfca6
005BFC87  0B 7E 04                        or edi, dword ptr [rsi + 4]
005BFC8A  87 3E                           xchg dword ptr [rsi], edi
005BFC8C  89 7D 50                        mov dword ptr [rbp + 0x50], edi
005BFC8F  0F BA E7 1E                     bt edi, 0x1e
005BFC93  0F 83 E9 00 00 00               jae 0x1405bfd82
005BFC99  48 8B CE                        mov rcx, rsi
005BFC9C  E8 7F 7F C5 FF                  call 0x140217c20
005BFCA1  E9 DC 00 00 00                  jmp 0x1405bfd82
005BFCA6  45 8B FD                        mov r15d, r13d
005BFCA9  45 8B E5                        mov r12d, r13d
005BFCAC  E9 BB 00 00 00                  jmp 0x1405bfd6c
005BFCB1  45 03 FE                        add r15d, r14d
005BFCB4  44 85 3D F1 55 A0 00            test dword ptr [rip + 0xa055f1], r15d
005BFCBB  0F 85 A9 00 00 00               jne 0x1405bfd6a
005BFCC1  8B 05 F1 6D A0 00               mov eax, dword ptr [rip + 0xa06df1]
005BFCC7  A8 40                           test al, 0x40
005BFCC9  0F 84 9B 00 00 00               je 0x1405bfd6a
005BFCCF  E8 BC F7 D4 FF                  call 0x14030f490
005BFCD4  84 C0                           test al, al
005BFCD6  0F 84 8E 00 00 00               je 0x1405bfd6a
005BFCDC  45 03 E6                        add r12d, r14d
005BFCDF  E8 48 C5 F3 FF                  call 0x1404fc22c
005BFCE4  84 C0                           test al, al
005BFCE6  74 78                           je 0x1405bfd60
005BFCE8  F7 05 46 6E A0 00 00 00 02 00   test dword ptr [rip + 0xa06e46], 0x20000
005BFCF2  74 6C                           je 0x1405bfd60
005BFCF4  41 F6 C4 07                     test r12b, 7
005BFCF8  75 66                           jne 0x1405bfd60
005BFCFA  8B 0E                           mov ecx, dword ptr [rsi]
005BFCFC  8B C1                           mov eax, ecx
005BFCFE  25 00 00 00 80                  and eax, 0x80000000
005BFD03  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
005BFD06  3B C7                           cmp eax, edi
005BFD08  74 62                           je 0x1405bfd6c
005BFD0A  8B D1                           mov edx, ecx
005BFD0C  44 8B C1                        mov r8d, ecx
005BFD0F  41 BD 04 00 00 00               mov r13d, 4
005BFD15  0F BA E9 1E                     bts ecx, 0x1e
005BFD19  8B C2                           mov eax, edx
005BFD1B  44 8B F1                        mov r14d, ecx
005BFD1E  F0 44 0F B1 36                  lock cmpxchg dword ptr [rsi], r14d
005BFD23  8B C8                           mov ecx, eax
005BFD25  41 3B C0                        cmp eax, r8d
005BFD28  75 1A                           jne 0x1405bfd44
005BFD2A  44 89 75 50                     mov dword ptr [rbp + 0x50], r14d
005BFD2E  4D 8B C5                        mov r8, r13
005BFD31  48 8D 55 50                     lea rdx, [rbp + 0x50]
005BFD35  48 8B CE                        mov rcx, rsi
005BFD38  E8 FF BC F3 FF                  call 0x1404fba3c
005BFD3D  8B 0E                           mov ecx, dword ptr [rsi]
005BFD3F  41 3B CE                        cmp ecx, r14d
005BFD42  74 EA                           je 0x1405bfd2e
005BFD44  8B C1                           mov eax, ecx
005BFD46  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
005BFD49  25 00 00 00 80                  and eax, 0x80000000
005BFD4E  8B D1                           mov edx, ecx
005BFD50  44 8B C1                        mov r8d, ecx
005BFD53  3B C7                           cmp eax, edi
005BFD55  75 BE                           jne 0x1405bfd15
005BFD57  45 33 ED                        xor r13d, r13d
005BFD5A  45 8D 75 01                     lea r14d, [r13 + 1]
005BFD5E  EB 0C                           jmp 0x1405bfd6c
005BFD60  41 8B CF                        mov ecx, r15d
005BFD63  E8 F8 F6 D4 FF                  call 0x14030f460
005BFD68  EB 02                           jmp 0x1405bfd6c
005BFD6A  F3 90                           pause
005BFD6C  8B 06                           mov eax, dword ptr [rsi]
005BFD6E  25 00 00 00 80                  and eax, 0x80000000
005BFD73  3B C7                           cmp eax, edi
005BFD75  0F 85 36 FF FF FF               jne 0x1405bfcb1
005BFD7B  90                              nop
005BFD7C  41 BF 02 00 00 00               mov r15d, 2
005BFD82  BF 00 40 00 00                  mov edi, 0x4000
005BFD87  48 8B 05 BA 6D A0 00            mov rax, qword ptr [rip + 0xa06dba]
005BFD8E  48 0F BA E0 29                  bt rax, 0x29
005BFD93  73 10                           jae 0x1405bfda5
005BFD95  B8 04 00 00 00                  mov eax, 4
005BFD9A  08 83 DE 06 00 00               or byte ptr [rbx + 0x6de], al
005BFDA0  E8 D7 90 EA FF                  call 0x140468e7c
005BFDA5  48 8B 05 9C 6D A0 00            mov rax, qword ptr [rip + 0xa06d9c]
005BFDAC  41 84 C7                        test r15b, al
005BFDAF  74 44                           je 0x1405bfdf5
005BFDB1  48 8B 05 90 6D A0 00            mov rax, qword ptr [rip + 0xa06d90]
005BFDB8  48 85 C7                        test rdi, rax
005BFDBB  75 38                           jne 0x1405bfdf5
005BFDBD  44 38 2D D3 6C A0 00            cmp byte ptr [rip + 0xa06cd3], r13b
005BFDC4  75 2F                           jne 0x1405bfdf5
005BFDC6  48 8B 05 7B 6D A0 00            mov rax, qword ptr [rip + 0xa06d7b]
005BFDCD  A8 10                           test al, 0x10
005BFDCF  75 0B                           jne 0x1405bfddc
005BFDD1  48 8B 05 70 6D A0 00            mov rax, qword ptr [rip + 0xa06d70]
005BFDD8  A8 40                           test al, 0x40
005BFDDA  74 19                           je 0x1405bfdf5
005BFDDC  48 B8 00 00 00 00 02 00 00 00   movabs rax, 0x200000000
005BFDE6  F0 48 09 05 5A 6D A0 00         lock or qword ptr [rip + 0xa06d5a], rax
005BFDEE  44 08 B3 DC 06 00 00            or byte ptr [rbx + 0x6dc], r14b
005BFDF5  48 8B 05 4C 6D A0 00            mov rax, qword ptr [rip + 0xa06d4c]
005BFDFC  45 8B C5                        mov r8d, r13d
005BFDFF  41 B4 40                        mov r12b, 0x40
005BFE02  41 84 C7                        test r15b, al
005BFE05  0F 84 02 01 00 00               je 0x1405bff0d
005BFE0B  48 8B 05 36 6D A0 00            mov rax, qword ptr [rip + 0xa06d36]
005BFE12  41 84 C4                        test r12b, al
005BFE15  0F 84 F2 00 00 00               je 0x1405bff0d
005BFE1B  48 8B 05 26 6D A0 00            mov rax, qword ptr [rip + 0xa06d26]
005BFE22  A8 10                           test al, 0x10
005BFE24  0F 84 E3 00 00 00               je 0x1405bff0d
005BFE2A  48 8B 05 17 6D A0 00            mov rax, qword ptr [rip + 0xa06d17]
005BFE31  48 BA 00 00 00 00 00 01 00 00   movabs rdx, 0x10000000000
005BFE3B  48 85 C7                        test rdi, rax
005BFE3E  0F 85 D3 00 00 00               jne 0x1405bff17
005BFE44  48 8B 05 FD 6C A0 00            mov rax, qword ptr [rip + 0xa06cfd]
005BFE4B  48 85 C2                        test rdx, rax
005BFE4E  0F 85 C3 00 00 00               jne 0x1405bff17
005BFE54  48 8B 93 60 8E 00 00            mov rdx, qword ptr [rbx + 0x8e60]
005BFE5B  F3 48 0F B8 C2                  popcnt rax, rdx
005BFE60  41 3B C7                        cmp eax, r15d
005BFE63  0F 85 A4 00 00 00               jne 0x1405bff0d
005BFE69  44 38 2D 27 6C A0 00            cmp byte ptr [rip + 0xa06c27], r13b
005BFE70  74 51                           je 0x1405bfec3
005BFE72  E8 C1 3C FC FF                  call 0x140583b38
005BFE77  84 C0                           test al, al
005BFE79  74 48                           je 0x1405bfec3
005BFE7B  8B 05 0F 6C A0 00               mov eax, dword ptr [rip + 0xa06c0f]
005BFE81  41 84 C7                        test r15b, al
005BFE84  0F 84 83 00 00 00               je 0x1405bff0d
005BFE8A  0F BA E0 16                     bt eax, 0x16
005BFE8E  73 7D                           jae 0x1405bff0d
005BFE90  8B 0D 56 6E A0 00               mov ecx, dword ptr [rip + 0xa06e56]
005BFE96  83 E9 01                        sub ecx, 1
005BFE99  74 72                           je 0x1405bff0d
005BFE9B  83 E9 01                        sub ecx, 1
005BFE9E  74 6D                           je 0x1405bff0d
005BFEA0  83 E9 01                        sub ecx, 1
005BFEA3  74 1E                           je 0x1405bfec3
005BFEA5  83 F9 01                        cmp ecx, 1
005BFEA8  75 63                           jne 0x1405bff0d
005BFEAA  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
005BFEB3  48 8B 88 60 8E 00 00            mov rcx, qword ptr [rax + 0x8e60]
005BFEBA  48 8D 41 FF                     lea rax, [rcx - 1]
005BFEBE  48 85 C1                        test rcx, rax
005BFEC1  74 4A                           je 0x1405bff0d
005BFEC3  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
005BFECA  41 03 CE                        add ecx, r14d
005BFECD  48 D3 CA                        ror rdx, cl
005BFED0  48 0F BC C2                     bsf rax, rdx
005BFED4  03 C8                           add ecx, eax
005BFED6  89 45 60                        mov dword ptr [rbp + 0x60], eax
005BFED9  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
005BFEE0  83 E1 3F                        and ecx, 0x3f
005BFEE3  C1 E0 06                        shl eax, 6
005BFEE6  03 C8                           add ecx, eax
005BFEE8  48 8B 05 C9 32 96 00            mov rax, qword ptr [rip + 0x9632c9]
005BFEEF  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
005BFEF2  E8 D9 86 D1 FF                  call 0x1402d85d0
005BFEF7  48 89 83 B0 2D 00 00            mov qword ptr [rbx + 0x2db0], rax
005BFEFE  45 8B C6                        mov r8d, r14d
005BFF01  B8 06 00 00 00                  mov eax, 6
005BFF06  66 89 83 E0 06 00 00            mov word ptr [rbx + 0x6e0], ax
005BFF0D  48 BA 00 00 00 00 00 01 00 00   movabs rdx, 0x10000000000
005BFF17  8B 05 A3 0F 95 00               mov eax, dword ptr [rip + 0x950fa3]
005BFF1D  A8 20                           test al, 0x20
005BFF1F  74 18                           je 0x1405bff39
005BFF21  48 8B 05 20 6C A0 00            mov rax, qword ptr [rip + 0xa06c20]
005BFF28  41 84 C7                        test r15b, al
005BFF2B  74 0C                           je 0x1405bff39
005BFF2D  48 8B 05 14 6C A0 00            mov rax, qword ptr [rip + 0xa06c14]
005BFF34  41 84 C4                        test r12b, al
005BFF37  75 3B                           jne 0x1405bff74
005BFF39  48 8B 05 08 6C A0 00            mov rax, qword ptr [rip + 0xa06c08]
005BFF40  41 84 C7                        test r15b, al
005BFF43  74 41                           je 0x1405bff86
005BFF45  48 8B 05 FC 6B A0 00            mov rax, qword ptr [rip + 0xa06bfc]
005BFF4C  41 84 C4                        test r12b, al
005BFF4F  74 35                           je 0x1405bff86
005BFF51  45 85 C0                        test r8d, r8d
005BFF54  75 30                           jne 0x1405bff86
005BFF56  48 8B 05 EB 6B A0 00            mov rax, qword ptr [rip + 0xa06beb]
005BFF5D  48 85 C2                        test rdx, rax
005BFF60  75 24                           jne 0x1405bff86
005BFF62  44 38 2D 2E 6B A0 00            cmp byte ptr [rip + 0xa06b2e], r13b
005BFF69  74 1B                           je 0x1405bff86
005BFF6B  E8 C8 3B FC FF                  call 0x140583b38
005BFF70  84 C0                           test al, al
005BFF72  74 12                           je 0x1405bff86
005BFF74  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
005BFF7E  F0 48 09 05 C2 6B A0 00         lock or qword ptr [rip + 0xa06bc2], rax
005BFF86  48 8B 05 BB 6B A0 00            mov rax, qword ptr [rip + 0xa06bbb]
005BFF8D  41 84 C7                        test r15b, al
005BFF90  74 3B                           je 0x1405bffcd
005BFF92  48 8B 05 AF 6B A0 00            mov rax, qword ptr [rip + 0xa06baf]
005BFF99  41 84 C4                        test r12b, al
005BFF9C  74 2F                           je 0x1405bffcd
005BFF9E  48 8B 05 A3 6B A0 00            mov rax, qword ptr [rip + 0xa06ba3]
005BFFA5  48 85 C7                        test rdi, rax
005BFFA8  74 23                           je 0x1405bffcd
005BFFAA  45 85 C0                        test r8d, r8d
005BFFAD  75 1E                           jne 0x1405bffcd
005BFFAF  48 8B 05 92 6B A0 00            mov rax, qword ptr [rip + 0xa06b92]
005BFFB6  48 85 C2                        test rdx, rax
005BFFB9  75 12                           jne 0x1405bffcd
005BFFBB  48 B8 00 00 00 00 00 08 00 00   movabs rax, 0x80000000000
005BFFC5  F0 48 09 05 7B 6B A0 00         lock or qword ptr [rip + 0xa06b7b], rax
005BFFCD  44 38 B3 8D 00 00 00            cmp byte ptr [rbx + 0x8d], r14b
005BFFD4  75 2D                           jne 0x1405c0003
005BFFD6  48 8B 05 6B 6B A0 00            mov rax, qword ptr [rip + 0xa06b6b]
005BFFDD  A8 10                           test al, 0x10
005BFFDF  75 22                           jne 0x1405c0003
005BFFE1  8B 05 D9 0E 95 00               mov eax, dword ptr [rip + 0x950ed9]
005BFFE7  41 84 C4                        test r12b, al
005BFFEA  75 17                           jne 0x1405c0003
005BFFEC  48 B8 00 00 00 00 20 00 00 00   movabs rax, 0x2000000000
005BFFF6  F0 48 09 05 4A 6B A0 00         lock or qword ptr [rip + 0xa06b4a], rax
005BFFFE  E9 1C FB FF FF                  jmp 0x1405bfb1f
005C0003  48 8B CB                        mov rcx, rbx
005C0006  E8 DD F2 FF FF                  call 0x1405bf2e8
005C000B  85 C0                           test eax, eax
005C000D  74 4D                           je 0x1405c005c
005C000F  F0 48 81 0D 2D 6B A0 00 00 80 00 00  lock or qword ptr [rip + 0xa06b2d], 0x8000
005C001B  48 8D 15 26 6B A0 00            lea rdx, [rip + 0xa06b26]
005C0022  48 8B CB                        mov rcx, rbx
005C0025  E8 52 F2 FF FF                  call 0x1405bf27c
005C002A  85 C0                           test eax, eax
005C002C  75 0C                           jne 0x1405c003a
005C002E  48 B8 00 00 00 00 00 10 00 00   movabs rax, 0x100000000000
005C0038  EB 1A                           jmp 0x1405c0054
005C003A  48 8D 15 07 6B A0 00            lea rdx, [rip + 0xa06b07]
005C0041  E8 76 F2 FF FF                  call 0x1405bf2bc
005C0046  85 C0                           test eax, eax
005C0048  75 12                           jne 0x1405c005c
005C004A  48 B8 00 00 00 00 00 20 00 00   movabs rax, 0x200000000000
005C0054  F0 48 09 05 EC 6A A0 00         lock or qword ptr [rip + 0xa06aec], rax
005C005C  48 8B 05 E5 6A A0 00            mov rax, qword ptr [rip + 0xa06ae5]
005C0063  48 0F BA E0 1B                  bt rax, 0x1b
005C0068  73 3C                           jae 0x1405c00a6
005C006A  E8 C9 F3 FF FF                  call 0x1405bf438
005C006F  85 C0                           test eax, eax
005C0071  75 0C                           jne 0x1405c007f
005C0073  48 B8 00 00 00 00 00 00 00 02   movabs rax, 0x200000000000000
005C007D  EB 16                           jmp 0x1405c0095
005C007F  48 8B CB                        mov rcx, rbx
005C0082  E8 CD F3 FF FF                  call 0x1405bf454
005C0087  85 C0                           test eax, eax
005C0089  75 14                           jne 0x1405c009f
005C008B  48 B8 00 00 00 00 00 00 00 04   movabs rax, 0x400000000000000
005C0095  F0 48 09 05 AB 6A A0 00         lock or qword ptr [rip + 0xa06aab], rax
005C009D  EB 07                           jmp 0x1405c00a6
005C009F  44 08 A3 DC 06 00 00            or byte ptr [rbx + 0x6dc], r12b
005C00A6  48 8B 05 9B 6A A0 00            mov rax, qword ptr [rip + 0xa06a9b]
005C00AD  48 0F BA E0 10                  bt rax, 0x10
005C00B2  0F 83 AA 00 00 00               jae 0x1405c0162
005C00B8  F7 05 FE 0D 95 00 00 00 80 00   test dword ptr [rip + 0x950dfe], 0x800000
005C00C2  75 0F                           jne 0x1405c00d3
005C00C4  48 B8 00 00 00 00 00 00 10 00   movabs rax, 0x10000000000000
005C00CE  E9 87 00 00 00                  jmp 0x1405c015a
005C00D3  8A 05 7B 6A A0 00               mov al, byte ptr [rip + 0xa06a7b]
005C00D9  84 C0                           test al, al
005C00DB  74 30                           je 0x1405c010d
005C00DD  48 B8 00 00 00 00 00 00 80 00   movabs rax, 0x80000000000000
005C00E7  F0 48 09 05 59 6A A0 00         lock or qword ptr [rip + 0xa06a59], rax
005C00EF  8A 0D 5F 6A A0 00               mov cl, byte ptr [rip + 0xa06a5f]
005C00F5  8A 83 DC 06 00 00               mov al, byte ptr [rbx + 0x6dc]
005C00FB  80 E1 03                        and cl, 3
005C00FE  C0 E1 04                        shl cl, 4
005C0101  24 CF                           and al, 0xcf
005C0103  0A C8                           or cl, al
005C0105  88 8B DC 06 00 00               mov byte ptr [rbx + 0x6dc], cl
005C010B  EB 55                           jmp 0x1405c0162
005C010D  48 8B 05 34 6A A0 00            mov rax, qword ptr [rip + 0xa06a34]
005C0114  48 0F BA E0 11                  bt rax, 0x11
005C0119  73 35                           jae 0x1405c0150
005C011B  48 B8 00 00 00 00 00 00 40 00   movabs rax, 0x40000000000000
005C0125  F0 48 09 05 1B 6A A0 00         lock or qword ptr [rip + 0xa06a1b], rax
005C012D  B8 00 04 00 00                  mov eax, 0x400
005C0132  66 09 83 E8 06 00 00            or word ptr [rbx + 0x6e8], ax
005C0139  66 09 83 E2 06 00 00            or word ptr [rbx + 0x6e2], ax
005C0140  66 09 83 EC 06 00 00            or word ptr [rbx + 0x6ec], ax
005C0147  66 09 83 EA 06 00 00            or word ptr [rbx + 0x6ea], ax
005C014E  EB 12                           jmp 0x1405c0162
005C0150  48 B8 00 00 00 00 00 00 20 00   movabs rax, 0x20000000000000
005C015A  F0 48 09 05 E6 69 A0 00         lock or qword ptr [rip + 0xa069e6], rax
005C0162  48 8B 05 DF 69 A0 00            mov rax, qword ptr [rip + 0xa069df]
005C0169  48 0F BA E0 15                  bt rax, 0x15
005C016E  0F 83 96 00 00 00               jae 0x1405c020a
005C0174  48 8B 05 CD 69 A0 00            mov rax, qword ptr [rip + 0xa069cd]
005C017B  B9 04 00 00 00                  mov ecx, 4
005C0180  84 C1                           test cl, al
005C0182  75 0C                           jne 0x1405c0190
005C0184  48 B8 00 00 00 00 00 00 01 00   movabs rax, 0x1000000000000
005C018E  EB 72                           jmp 0x1405c0202
005C0190  8B 05 2A 0D 95 00               mov eax, dword ptr [rip + 0x950d2a]
005C0196  A8 05                           test al, 5
005C0198  75 5E                           jne 0x1405c01f8
005C019A  44 38 B3 8D 00 00 00            cmp byte ptr [rbx + 0x8d], r14b
005C01A1  75 1A                           jne 0x1405c01bd
005C01A3  48 8B 05 9E 69 A0 00            mov rax, qword ptr [rip + 0xa0699e]
005C01AA  A8 10                           test al, 0x10
005C01AC  0F 94 C1                        sete cl
005C01AF  44 84 25 0A 0D 95 00            test byte ptr [rip + 0x950d0a], r12b
005C01B6  0F 94 C0                        sete al
005C01B9  84 C8                           test al, cl
005C01BB  75 3B                           jne 0x1405c01f8
005C01BD  48 8B CB                        mov rcx, rbx
005C01C0  E8 23 F1 FF FF                  call 0x1405bf2e8
005C01C5  85 C0                           test eax, eax
005C01C7  74 23                           je 0x1405c01ec
005C01C9  48 8D 15 78 69 A0 00            lea rdx, [rip + 0xa06978]
005C01D0  E8 E7 F0 FF FF                  call 0x1405bf2bc
005C01D5  85 C0                           test eax, eax
005C01D7  74 13                           je 0x1405c01ec
005C01D9  48 8D 15 68 69 A0 00            lea rdx, [rip + 0xa06968]
005C01E0  48 8B CB                        mov rcx, rbx
005C01E3  E8 94 F0 FF FF                  call 0x1405bf27c
005C01E8  85 C0                           test eax, eax
005C01EA  75 1E                           jne 0x1405c020a
005C01EC  F7 05 CA 0C 95 00 00 00 00 04   test dword ptr [rip + 0x950cca], 0x4000000
005C01F6  75 12                           jne 0x1405c020a
005C01F8  48 B8 00 00 00 00 00 80 00 00   movabs rax, 0x800000000000
005C0202  F0 48 09 05 3E 69 A0 00         lock or qword ptr [rip + 0xa0693e], rax
005C020A  48 85 F6                        test rsi, rsi
005C020D  0F 84 0B 01 00 00               je 0x1405c031e
005C0213  83 C8 FF                        or eax, 0xffffffff
005C0216  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
005C021A  FF C8                           dec eax
005C021C  41 BF 00 00 00 80               mov r15d, 0x80000000
005C0222  8B F8                           mov edi, eax
005C0224  F7 D7                           not edi
005C0226  41 23 FF                        and edi, r15d
005C0229  A9 FF FF FF 3F                  test eax, 0x3fffffff
005C022E  75 1C                           jne 0x1405c024c
005C0230  0B 7E 04                        or edi, dword ptr [rsi + 4]
005C0233  87 3E                           xchg dword ptr [rsi], edi
005C0235  0F BA E7 1E                     bt edi, 0x1e
005C0239  0F 83 DF 00 00 00               jae 0x1405c031e
005C023F  48 8B CE                        mov rcx, rsi
005C0242  E8 D9 79 C5 FF                  call 0x140217c20
005C0247  E9 D2 00 00 00                  jmp 0x1405c031e
005C024C  45 8B F5                        mov r14d, r13d
005C024F  45 8B E5                        mov r12d, r13d
005C0252  E9 B9 00 00 00                  jmp 0x1405c0310
005C0257  41 FF C6                        inc r14d
005C025A  44 85 35 4B 50 A0 00            test dword ptr [rip + 0xa0504b], r14d
005C0261  0F 85 A7 00 00 00               jne 0x1405c030e
005C0267  8B 05 4B 68 A0 00               mov eax, dword ptr [rip + 0xa0684b]
005C026D  A8 40                           test al, 0x40
005C026F  0F 84 99 00 00 00               je 0x1405c030e
005C0275  E8 16 F2 D4 FF                  call 0x14030f490
005C027A  84 C0                           test al, al
005C027C  0F 84 8C 00 00 00               je 0x1405c030e
005C0282  41 FF C4                        inc r12d
005C0285  E8 A2 BF F3 FF                  call 0x1404fc22c
005C028A  84 C0                           test al, al
005C028C  74 76                           je 0x1405c0304
005C028E  F7 05 A0 68 A0 00 00 00 02 00   test dword ptr [rip + 0xa068a0], 0x20000
005C0298  74 6A                           je 0x1405c0304
005C029A  41 F6 C4 07                     test r12b, 7
005C029E  75 64                           jne 0x1405c0304
005C02A0  8B 0E                           mov ecx, dword ptr [rsi]
005C02A2  8B C1                           mov eax, ecx
005C02A4  41 23 C7                        and eax, r15d
005C02A7  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
005C02AA  3B C7                           cmp eax, edi
005C02AC  74 62                           je 0x1405c0310
005C02AE  8B D1                           mov edx, ecx
005C02B0  44 8B C1                        mov r8d, ecx
005C02B3  41 BD 04 00 00 00               mov r13d, 4
005C02B9  0F BA E9 1E                     bts ecx, 0x1e
005C02BD  8B C2                           mov eax, edx
005C02BF  44 8B F9                        mov r15d, ecx
005C02C2  F0 44 0F B1 3E                  lock cmpxchg dword ptr [rsi], r15d
005C02C7  8B C8                           mov ecx, eax
005C02C9  41 3B C0                        cmp eax, r8d
005C02CC  75 1A                           jne 0x1405c02e8
005C02CE  44 89 7D 58                     mov dword ptr [rbp + 0x58], r15d
005C02D2  4D 8B C5                        mov r8, r13
005C02D5  48 8D 55 58                     lea rdx, [rbp + 0x58]
005C02D9  48 8B CE                        mov rcx, rsi
005C02DC  E8 5B B7 F3 FF                  call 0x1404fba3c
005C02E1  8B 0E                           mov ecx, dword ptr [rsi]
005C02E3  41 3B CF                        cmp ecx, r15d
005C02E6  74 EA                           je 0x1405c02d2
005C02E8  8B C1                           mov eax, ecx
005C02EA  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
005C02ED  41 BF 00 00 00 80               mov r15d, 0x80000000
005C02F3  8B D1                           mov edx, ecx
005C02F5  41 23 C7                        and eax, r15d
005C02F8  44 8B C1                        mov r8d, ecx
005C02FB  3B C7                           cmp eax, edi
005C02FD  75 BA                           jne 0x1405c02b9
005C02FF  45 33 ED                        xor r13d, r13d
005C0302  EB 0C                           jmp 0x1405c0310
005C0304  41 8B CE                        mov ecx, r14d
005C0307  E8 54 F1 D4 FF                  call 0x14030f460
005C030C  EB 02                           jmp 0x1405c0310
005C030E  F3 90                           pause
005C0310  8B 06                           mov eax, dword ptr [rsi]
005C0312  41 23 C7                        and eax, r15d
005C0315  3B C7                           cmp eax, edi
005C0317  0F 85 3A FF FF FF               jne 0x1405c0257
005C031D  90                              nop
005C031E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
005C0327  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
005C032E  E8 AD 60 E2 FF                  call 0x1403e63e0
005C0333  E9 E7 F7 FF FF                  jmp 0x1405bfb1f
005C0338  48 8B 05 09 68 A0 00            mov rax, qword ptr [rip + 0xa06809]
005C033F  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
005C0349  49 85 C4                        test r12, rax
005C034C  74 1A                           je 0x1405c0368
005C034E  F0 4C 09 05 F2 67 A0 00         lock or qword ptr [rip + 0xa067f2], r8
005C0356  48 B8 FF FF FF FF 7F FF FF FF   movabs rax, 0xffffff7fffffffff
005C0360  F0 48 21 05 E0 67 A0 00         lock and qword ptr [rip + 0xa067e0], rax
005C0368  48 8B 05 D9 67 A0 00            mov rax, qword ptr [rip + 0xa067d9]
005C036F  49 85 C0                        test r8, rax
005C0372  0F 84 B1 F7 FF FF               je 0x1405bfb29
005C0378  83 3D 79 AE 84 00 48            cmp dword ptr [rip + 0x84ae79], 0x48
005C037F  0F B7 83 E8 06 00 00            movzx eax, word ptr [rbx + 0x6e8]
005C0386  75 04                           jne 0x1405c038c
005C0388  66 83 C8 04                     or ax, 4
005C038C  66 89 83 E8 06 00 00            mov word ptr [rbx + 0x6e8], ax
005C0393  66 89 83 EC 06 00 00            mov word ptr [rbx + 0x6ec], ax
005C039A  E9 8A F7 FF FF                  jmp 0x1405bfb29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiOptimizeSpecCtrlSettingsWorker(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (56);
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448) - 1)) != 0) {
    }
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10515627)) == 0) goto loc_005BF5FF;
    result = HvlIsCoreSharingPossible(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448), a3, a4);
    if ((unsigned __int8)(result) != 0) {
    }
    if (((128) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9771195))))) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 9771195));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) == 1) {
        a2 = v_rip + 10515731;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiDetectAmdNonArchSsbdSupport(a1, a2, a3, a4);
        a1 = 1;
    }
    if (((128) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10515711)))) == 0) goto loc_005BF699;
    if (condition_is_below) goto loc_005BF699;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9771082)))) & (8)) != 0) goto loc_005BF691;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9771082)))) & (16)) == 0) goto loc_005BF699;
    if ((*(unsigned int *)(v_rip + 8698739)) != 72) goto loc_005BF691;
    goto loc_005BF699;
loc_005BF691:
loc_005BF699:
    if (((4) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10515624)))) == 0) {
    }
    if (((4) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9771007))))) == 0) goto loc_005BF6D9;
    goto loc_005BF725;
loc_005BF6D9:
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9771007))))) == 0) goto loc_005BF725;
    if ((*(unsigned __int8 *)(v_rip + 10515371)) == 0) goto loc_005BF725;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10515356))))) == 0) goto loc_005BF725;
    result = HvlIsCoreSharingPossible(a1, 4, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005BF725;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10515519))) & (64)) != 0) {
        *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1768) = 2;
        *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1772) = 2;
        *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 1762) = 2;
    }
    if (((*(unsigned int *)(v_rip + 9770897)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_005BF7A6;
    if (condition_is_below) goto loc_005BF775;
    goto loc_005BF79E;
loc_005BF775:
    if (((*(unsigned int *)(v_rip + 9770817)) & (0x8000000ULL)) != 0) goto loc_005BF794;
    if ((*(unsigned __int8 *)(v_rip + 12853432)) != 0) goto loc_005BF7A6;
    goto loc_005BF7A6;
loc_005BF794:
loc_005BF79E:
loc_005BF7A6:
    result = *(unsigned __int64 *)(v_rip + 10515355);
    if (((a1) & (*(unsigned __int64 *)(v_rip + 10515355))) != 0) {
        result = 512;
        result = 24;
        *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 44714) = (unsigned __int16)(result);
    }
    if (a1 == 0) goto loc_005BF919;
    v_stack_p8 = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & (0x80000000ULL));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005BF810;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a1 + 4)));
    v_stack_p8 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_005BF90F;
    result = KeWakeAddressAll(a1, 4, a3, a4);
    goto loc_005BF90F;
loc_005BF810:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0x80000000ULL));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_005BF8FE;
loc_005BF82A:
    v_r15 = (unsigned int)((0) + (1));
    if (((*(unsigned int *)(v_rip + 10508920)) & ((unsigned int)(v_r15))) != 0) goto loc_005BF8DF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10515064)))) & (64)) == 0) goto loc_005BF8DF;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, 4, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005BF8DF;
    v_r12 = (unsigned int)((0) + (1));
    result = KeCanUseHaltOnAddress(a1, 4, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005BF8D5;
    if (((*(unsigned int *)(v_rip + 10515149)) & (0x20000ULL)) == 0) goto loc_005BF8D5;
    if ((((unsigned __int8)(v_r12)) & (7)) != 0) goto loc_005BF8D5;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0x80000000ULL));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_005BF8E1;
loc_005BF88E:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005BF8BD;
    v_stack_p8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
loc_005BF8A7:
    result = KiHaltOnAddress(a1, v_stack_p8, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005BF8A7;
loc_005BF8BD:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0x80000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005BF88E;
    v_r13 = 0;
    goto loc_005BF8E1;
loc_005BF8D5:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), a4);
    goto loc_005BF8E1;
loc_005BF8DF:
loc_005BF8E1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0x80000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005BF82A;
loc_005BF8FE:
loc_005BF90F:
loc_005BF919:
    if ((((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (*(unsigned __int64 *)(v_rip + 10514984))) != 0) goto loc_005C0338;
    if (((v_rdi) & (*(unsigned __int64 *)(v_rip + 10514968))) != 0) goto loc_005C0338;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10514921)))) == 0) goto loc_005BFB9A;
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10514874))) != 0) {
        a1 = 1 + 2;
    }
    *(unsigned __int16 *)(v_stack_m58 + 1768) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(v_stack_m58 + 1772) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(v_stack_m58 + 1762) = (unsigned __int16)(a1);
    if (((a1) & (*(unsigned __int64 *)(v_rip + 10514823))) != 0) goto loc_005BF9D2;
    if (((v_r12) & (*(unsigned __int64 *)(v_rip + 10514811))) == 0) goto loc_005BF9FB;
loc_005BF9D2:
    result = *(unsigned __int16 *)(v_stack_m58 + 1768);
    if ((*(unsigned int *)(v_rip + 8697887)) == 72) {
        result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m58 + 1768)) | (4));
    }
    *(unsigned __int16 *)(v_stack_m58 + 1768) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_stack_m58 + 1772) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_stack_m58 + 1762) = (unsigned __int16)(result);
loc_005BF9FB:
    *(unsigned __int16 *)(v_stack_m58 + 1770) = 1;
    if (((a1) & (*(unsigned __int64 *)(v_rip + 10514750))) != 0) goto loc_005BFA1B;
    if (((v_r12) & (*(unsigned __int64 *)(v_rip + 10514738))) == 0) goto loc_005BFA30;
loc_005BFA1B:
    result = *(unsigned __int64 *)(v_rip + 10514738);
    if ((*(unsigned int *)(v_rip + 8697814)) == 72) {
        result = 4;
    }
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10514705))) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_005BFB0F;
    if (((*(unsigned int *)(v_rip + 9770052)) & (0x800000ULL)) != 0) goto loc_005BFA8B;
    goto loc_005BFB0F;
loc_005BFA8B:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 10514627)) == 0) goto loc_005BFAC5;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 10514599)) & (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m58 + 1756)) & (207));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_stack_m58 + 1756) = (unsigned __int8)(a1);
    goto loc_005BFB0F;
loc_005BFAC5:
    if (condition_is_above_or_equal) goto loc_005BFB07;
    goto loc_005BFB0F;
loc_005BFB07:
loc_005BFB0F:
    if (((v_r12) & (*(unsigned __int64 *)(v_rip + 10514482))) != 0) goto loc_005BFBA0;
loc_005BFB1F:
loc_005BFB29:
    *(unsigned __int16 *)(v_stack_m58 + 1766) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + 1768));
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + 1768)) != 0) {
        a2 = (unsigned int)(*(unsigned __int16 *)(v_stack_m58 + 1768));
        a1 = 72;
        a2 = (a2) >> (32);
    }
    if (((128) & (*(unsigned __int64 *)(v_rip + 10514424))) == 0) goto loc_005BFB79;
    result = *(unsigned __int64 *)(v_rip + 10514424);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8697501)))) != 72) {
        a2 = (a2) << (32);
        result = (*(unsigned __int64 *)(v_rip + 10514424)) | (a2);
        result = (result) | (*(unsigned __int64 *)(v_rip + 8697472));
        a2 = result;
        a2 = (a2) >> (32);
    }
    result = KiSetMicrocodeUpdateOptions((unsigned int)(*(unsigned int *)(v_rip + 8697501)), a2, 128, (unsigned int)(0x400ULL));
    result = KiSetVirtualMitigationControl(v_stack_m58, a2, 128, (unsigned int)(0x400ULL));
    result = 0;
    v_rsp = (v_rsp) + (56);
    return result;
loc_005BFB9A:
loc_005BFBA0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10514337))) & (16)) == 0) goto loc_005BFBB5;
    *(unsigned __int16 *)(v_stack_m58 + 1770) = 1;
    goto loc_005BFBD4;
loc_005BFBB5:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10514316))) & (64)) == 0) goto loc_005BFBD4;
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10514305)))) != 0) {
        *(unsigned __int16 *)(v_stack_m58 + 1770) = 2;
    }
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10514285))) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (((128) & (*(unsigned __int64 *)(v_rip + 10514243))) != 0) goto loc_005BFC20;
    if (((v_r12) & (*(unsigned __int64 *)(v_rip + 10514221))) == 0) goto loc_005BFC35;
loc_005BFC20:
    result = *(unsigned __int64 *)(v_rip + 10514221);
    if ((*(unsigned int *)(v_rip + 8697297)) == 72) {
        result = 4;
    }
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10514188)))) != 0) goto loc_005BFB29;
    if ((*(unsigned __int8 *)(v_stack_m58 + 141)) == 1) {
    }
    if (a1 == 0) goto loc_005BFD87;
    v_stack_p10 = 0;
    result = (unsigned int)((*(unsigned __int64 *)(v_rip + 10514188)) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & (0x80000000ULL));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005BFCA6;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a1 + 4)));
    v_stack_p10 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_005BFD82;
    result = KeWakeAddressAll(a1, a2, 128, (unsigned int)(0x400ULL));
    goto loc_005BFD82;
loc_005BFCA6:
    goto loc_005BFD6C;
loc_005BFCB1:
    v_r15 = (unsigned int)((0) + (1));
    if (((*(unsigned int *)(v_rip + 10507761)) & ((unsigned int)(v_r15))) != 0) goto loc_005BFD6A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10513905)))) & (64)) == 0) goto loc_005BFD6A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, 128, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) == 0) goto loc_005BFD6A;
    v_r12 = (unsigned int)((0) + (1));
    result = KeCanUseHaltOnAddress(a1, a2, 128, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) == 0) goto loc_005BFD60;
    if (((*(unsigned int *)(v_rip + 10513990)) & (0x20000ULL)) == 0) goto loc_005BFD60;
    if ((((unsigned __int8)(v_r12)) & (7)) != 0) goto loc_005BFD60;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0x80000000ULL));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_005BFD6C;
loc_005BFD15:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005BFD44;
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
loc_005BFD2E:
    result = KiHaltOnAddress(a1, v_stack_p10, 4, (unsigned int)(0x400ULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005BFD2E;
loc_005BFD44:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (0x80000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005BFD15;
    v_r13 = 0;
    goto loc_005BFD6C;
loc_005BFD60:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)(0x400ULL));
    goto loc_005BFD6C;
loc_005BFD6A:
loc_005BFD6C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0x80000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005BFCB1;
loc_005BFD82:
loc_005BFD87:
    result = *(unsigned __int64 *)(v_rip + 10513850);
    if (((unsigned int)(result)) < ((unsigned int)(v_rdi))) {
        result = 4;
        result = KeExitRetpoline((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)(0x400ULL));
    }
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513820)))) == 0) goto loc_005BFDF5;
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10513808))) != 0) goto loc_005BFDF5;
    if ((*(unsigned __int8 *)(v_rip + 10513619)) != 0) goto loc_005BFDF5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513787))) & (16)) != 0) goto loc_005BFDDC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513776))) & (64)) != 0) {
    }
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513740)))) == 0) goto loc_005BFF0D;
    if (((64) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513718)))) == 0) goto loc_005BFF0D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513702))) & (16)) == 0) goto loc_005BFF0D;
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10513687))) != 0) goto loc_005BFF17;
    if ((((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (*(unsigned __int64 *)(v_rip + 10513661))) != 0) goto loc_005BFF17;
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 10513661))) != 2) goto loc_005BFF0D;
    if ((*(unsigned __int8 *)(v_rip + 10513447)) == 0) goto loc_005BFEC3;
    result = HvlIsCoreSharingPossible((unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(v_stack_m58 + 36448), 0, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) == 0) goto loc_005BFEC3;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10513423))))) == 0) goto loc_005BFF0D;
    if (condition_is_above_or_equal) goto loc_005BFF0D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10514006))) - (1));
    if (condition_is_equal) goto loc_005BFF0D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005BFF0D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005BFEC3;
    if (((unsigned int)(a1)) != 1) goto loc_005BFF0D;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448) - 1;
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448) - 1)) != 0) {
        a1 = *(unsigned __int8 *)(v_stack_m58 + 209);
        a1 = (unsigned int)((a1) + ((unsigned int)(v_r13 + 1)));
        a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448) - 1)));
        v_stack_p20 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36448) - 1);
        result = *(unsigned __int8 *)(v_stack_m58 + 208);
        a1 = (unsigned int)((a1) & (63));
        result = (unsigned int)((result) << (6));
        a1 = (unsigned int)((a1) + ((unsigned int)(result)));
        result = *(unsigned __int64 *)(v_rip + 9843401);
        a1 = *(unsigned int *)(result + a1 * 4);
        result = KeGetPrcb(a1, *(unsigned __int64 *)(v_stack_m58 + 36448), 0, (unsigned int)(0x400ULL));
        *(unsigned __int64 *)(v_stack_m58 + 11696) = result;
        a3 = (unsigned int)(v_r13 + 1);
        result = 6;
        *(unsigned __int16 *)(v_stack_m58 + 1760) = (unsigned __int16)(result);
    }
loc_005BFF17:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9768867)))) & (32)) == 0) goto loc_005BFF39;
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513440)))) == 0) goto loc_005BFF39;
    if (((64) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513428)))) != 0) goto loc_005BFF74;
loc_005BFF39:
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513416)))) == 0) goto loc_005BFF86;
    if (((64) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513404)))) == 0) goto loc_005BFF86;
    if ((unsigned int)(a3) != 0) goto loc_005BFF86;
    if (((*(unsigned __int64 *)(v_stack_m58 + 36448)) & (*(unsigned __int64 *)(v_rip + 10513387))) != 0) goto loc_005BFF86;
    if ((*(unsigned __int8 *)(v_rip + 10513198)) == 0) goto loc_005BFF86;
    result = HvlIsCoreSharingPossible(a1, *(unsigned __int64 *)(v_stack_m58 + 36448), a3, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) != 0) {
    }
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513339)))) == 0) goto loc_005BFFCD;
    if (((64) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513327)))) == 0) goto loc_005BFFCD;
    if ((((unsigned int)(0x4000ULL)) & (*(unsigned __int64 *)(v_rip + 10513315))) == 0) goto loc_005BFFCD;
    if ((unsigned int)(a3) != 0) goto loc_005BFFCD;
    if (((*(unsigned __int64 *)(v_stack_m58 + 36448)) & (*(unsigned __int64 *)(v_rip + 10513298))) == 0) {
    }
    if ((*(unsigned __int8 *)(v_stack_m58 + 141)) != ((unsigned __int8)(v_r13 + 1))) goto loc_005C0003;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10513259))) & (16)) != 0) goto loc_005C0003;
    if (((64) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9768665))))) != 0) goto loc_005C0003;
    goto loc_005BFB1F;
loc_005C0003:
    result = KiIsBranchConfusionPresent(v_stack_m58, *(unsigned __int64 *)(v_stack_m58 + 36448), a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) == 0) goto loc_005C005C;
    result = KiIsBranchConfusionMitigationDesired(v_stack_m58, v_rip + 10513190, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) != 0) goto loc_005C003A;
    goto loc_005C0054;
loc_005C003A:
    result = KiIsBranchConfusionMitigationSupported(v_stack_m58, v_rip + 10513159, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) != 0) goto loc_005C005C;
loc_005C0054:
loc_005C005C:
    if (condition_is_above_or_equal) goto loc_005C00A6;
    result = KiIsTsaMitigationDesired(v_stack_m58, v_rip + 10513159, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) != 0) goto loc_005C007F;
    goto loc_005C0095;
loc_005C007F:
    result = KiIsTsaMitigationSupported(v_stack_m58, v_rip + 10513159, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) != 0) goto loc_005C009F;
loc_005C0095:
    goto loc_005C00A6;
loc_005C009F:
loc_005C00A6:
    if (condition_is_above_or_equal) goto loc_005C0162;
    if (((*(unsigned int *)(v_rip + 9768446)) & (0x800000ULL)) != 0) goto loc_005C00D3;
    goto loc_005C015A;
loc_005C00D3:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 10513019)) == 0) goto loc_005C010D;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 10512991)) & (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m58 + 1756)) & (207));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_stack_m58 + 1756) = (unsigned __int8)(a1);
    goto loc_005C0162;
loc_005C010D:
    if (condition_is_above_or_equal) goto loc_005C0150;
    goto loc_005C0162;
loc_005C0150:
loc_005C015A:
loc_005C0162:
    if (condition_is_above_or_equal) goto loc_005C020A;
    if (((4) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10512845)))) != 0) goto loc_005C0190;
    goto loc_005C0202;
loc_005C0190:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9768234)))) & (5)) != 0) goto loc_005C01F8;
    if ((*(unsigned __int8 *)(v_stack_m58 + 141)) != ((unsigned __int8)(v_r13 + 1))) goto loc_005C01BD;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10512798))) & (16)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_rip + 9768202)) & (64)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_005C01F8;
loc_005C01BD:
    result = KiIsBranchConfusionPresent(v_stack_m58, v_rip + 10513159, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) == 0) goto loc_005C01EC;
    result = KiIsBranchConfusionMitigationSupported(v_stack_m58, v_rip + 10512760, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) == 0) goto loc_005C01EC;
    result = KiIsBranchConfusionMitigationDesired(v_stack_m58, v_rip + 10512744, a3, (unsigned int)(0x400ULL));
    if ((unsigned int)(result) != 0) goto loc_005C020A;
loc_005C01EC:
    if (((*(unsigned int *)(v_rip + 9768138)) & (0x4000000ULL)) != 0) goto loc_005C020A;
loc_005C01F8:
loc_005C0202:
loc_005C020A:
    if (a1 == 0) goto loc_005C031E;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005C024C;
    v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(a1 + 4)));
    if (condition_is_above_or_equal) goto loc_005C031E;
    result = KeWakeAddressAll(a1, v_rip + 10512744, a3, (unsigned int)(0x400ULL));
    goto loc_005C031E;
loc_005C024C:
    goto loc_005C0310;
loc_005C0257:
    v_r14 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 10506315)) & ((unsigned int)(v_r14))) != 0) goto loc_005C030E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10512459)))) & (64)) == 0) goto loc_005C030E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_rip + 10512744, a3, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) == 0) goto loc_005C030E;
    v_r12 = (unsigned int)((0) + 1);
    result = KeCanUseHaltOnAddress(a1, v_rip + 10512744, a3, (unsigned int)(0x400ULL));
    if ((unsigned __int8)(result) == 0) goto loc_005C0304;
    if (((*(unsigned int *)(v_rip + 10512544)) & (0x20000ULL)) == 0) goto loc_005C0304;
    if ((((unsigned __int8)(v_r12)) & (7)) != 0) goto loc_005C0304;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_005C0310;
loc_005C02B9:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005C02E8;
    v_stack_p18 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
loc_005C02D2:
    result = KiHaltOnAddress(a1, v_stack_p18, 4, (unsigned int)(0x400ULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))))) goto loc_005C02D2;
loc_005C02E8:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005C02B9;
    v_r13 = 0;
    goto loc_005C0310;
loc_005C0304:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)(0x400ULL));
    goto loc_005C0310;
loc_005C030E:
loc_005C0310:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi))) goto loc_005C0257;
loc_005C031E:
    result = KiUpdateSpeculationControl(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), (unsigned int)(0x400ULL));
    goto loc_005BFB1F;
loc_005C0338:
    if (((v_r12) & (*(unsigned __int64 *)(v_rip + 10512393))) != 0) {
    }
    if ((((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (*(unsigned __int64 *)(v_rip + 10512345))) == 0) goto loc_005BFB29;
    result = *(unsigned __int16 *)(v_stack_m58 + 1768);
    if ((*(unsigned int *)(v_rip + 8695417)) == 72) {
        result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m58 + 1768)) | (4));
    }
    *(unsigned __int16 *)(v_stack_m58 + 1768) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_stack_m58 + 1772) = (unsigned __int16)(result);
    goto loc_005BFB29;
}
```

## 5. (Beta) C Style

```c
int64_t KiOptimizeSpecCtrlSettingsWorker(int64_t Arg1)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (56);
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x20));
    if (((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60)) & (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60) - 1)) != 0) {
    }
    local_r13 = 0;
    if ((*(uint8_t *)(v_rip + 0xA074AB)) == 0) goto loc_005BF5FF;
    result = HvlIsCoreSharingPossible(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60), a3, a4);
    if ((uint8_t)(result) != 0) {
    }
    if (((128) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9518BB))))) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x9518BB));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) == 1) {
        a2 = v_rip + 10515731;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiDetectAmdNonArchSsbdSupport(Arg1, a2, a3, a4);
        Arg1 = 1;
    }
    if (((128) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA074FF)))) == 0) goto loc_005BF699;
    if (condition_is_below) goto loc_005BF699;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95184A)))) & (8)) != 0) goto loc_005BF691;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95184A)))) & (16)) == 0) goto loc_005BF699;
    if ((*(uint32_t *)(v_rip + 0x84BB73)) != 72) goto loc_005BF691;
    goto loc_005BF699;
loc_005BF691:
loc_005BF699:
    if (((4) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA074A8)))) == 0) {
    }
    if (((4) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9517FF))))) == 0) goto loc_005BF6D9;
    goto loc_005BF725;
loc_005BF6D9:
    if ((((uint8_t)(Arg1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9517FF))))) == 0) goto loc_005BF725;
    if ((*(uint8_t *)(v_rip + 0xA073AB)) == 0) goto loc_005BF725;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0739C))))) == 0) goto loc_005BF725;
    result = HvlIsCoreSharingPossible(Arg1, 4, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_005BF725;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA0743F))) & (64)) != 0) {
        *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E8) = 2;
        *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6EC) = 2;
        *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6E2) = 2;
    }
    if (((*(uint32_t *)(v_rip + 0x951791)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_005BF7A6;
    if (condition_is_below) goto loc_005BF775;
    goto loc_005BF79E;
loc_005BF775:
    if (((*(uint32_t *)(v_rip + 0x951741)) & (0x8000000ULL)) != 0) goto loc_005BF794;
    if ((*(uint8_t *)(v_rip + 0xC420B8)) != 0) goto loc_005BF7A6;
    goto loc_005BF7A6;
loc_005BF794:
loc_005BF79E:
loc_005BF7A6:
    result = *(uint64_t *)(v_rip + 0xA0739B);
    if (((Arg1) & (*(uint64_t *)(v_rip + 0xA0739B))) != 0) {
        result = 512;
        result = 24;
        *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAEAA) = (uint16_t)(result);
    }
    if (Arg1 == 0) goto loc_005BF919;
    v_stack_p8 = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & (0x80000000ULL));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005BF810;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(Arg1 + 0x4)));
    v_stack_p8 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_005BF90F;
    result = KeWakeAddressAll(Arg1, 4, a3, a4);
    goto loc_005BF90F;
loc_005BF810:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) & (0x80000000ULL));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_005BF8FE;
loc_005BF82A:
    local_r15 = (uint32_t)((0) + (1));
    if (((*(uint32_t *)(v_rip + 0xA05A78)) & ((uint32_t)(local_r15))) != 0) goto loc_005BF8DF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA07278)))) & (64)) == 0) goto loc_005BF8DF;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, 4, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_005BF8DF;
    local_r12 = (uint32_t)((0) + (1));
    result = KeCanUseHaltOnAddress(Arg1, 4, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_005BF8D5;
    if (((*(uint32_t *)(v_rip + 0xA072CD)) & (0x20000ULL)) == 0) goto loc_005BF8D5;
    if ((((uint8_t)(local_r12)) & (7)) != 0) goto loc_005BF8D5;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (0x80000000ULL));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_005BF8E1;
loc_005BF88E:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005BF8BD;
    v_stack_p8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
loc_005BF8A7:
    result = KiHaltOnAddress(Arg1, v_stack_p8, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005BF8A7;
loc_005BF8BD:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (0x80000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005BF88E;
    local_r13 = 0;
    goto loc_005BF8E1;
loc_005BF8D5:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), a4);
    goto loc_005BF8E1;
loc_005BF8DF:
loc_005BF8E1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) & (0x80000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005BF82A;
loc_005BF8FE:
loc_005BF90F:
loc_005BF919:
    if ((((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (*(uint64_t *)(v_rip + 0xA07228))) != 0) goto loc_005C0338;
    if (((local_rdi) & (*(uint64_t *)(v_rip + 0xA07218))) != 0) goto loc_005C0338;
    if (((1) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA071E9)))) == 0) goto loc_005BFB9A;
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA071BA))) != 0) {
        Arg1 = 1 + 2;
    }
    *(uint16_t *)(v_stack_m58 + 0x6E8) = (uint16_t)(Arg1);
    *(uint16_t *)(v_stack_m58 + 0x6EC) = (uint16_t)(Arg1);
    *(uint16_t *)(v_stack_m58 + 0x6E2) = (uint16_t)(Arg1);
    if (((Arg1) & (*(uint64_t *)(v_rip + 0xA07187))) != 0) goto loc_005BF9D2;
    if (((local_r12) & (*(uint64_t *)(v_rip + 0xA0717B))) == 0) goto loc_005BF9FB;
loc_005BF9D2:
    result = *(uint16_t *)(v_stack_m58 + 0x6E8);
    if ((*(uint32_t *)(v_rip + 0x84B81F)) == 72) {
        result = (uint16_t)((*(uint16_t *)(v_stack_m58 + 0x6E8)) | (4));
    }
    *(uint16_t *)(v_stack_m58 + 0x6E8) = (uint16_t)(result);
    *(uint16_t *)(v_stack_m58 + 0x6EC) = (uint16_t)(result);
    *(uint16_t *)(v_stack_m58 + 0x6E2) = (uint16_t)(result);
loc_005BF9FB:
    *(uint16_t *)(v_stack_m58 + 0x6EA) = 1;
    if (((Arg1) & (*(uint64_t *)(v_rip + 0xA0713E))) != 0) goto loc_005BFA1B;
    if (((local_r12) & (*(uint64_t *)(v_rip + 0xA07132))) == 0) goto loc_005BFA30;
loc_005BFA1B:
    result = *(uint64_t *)(v_rip + 0xA07132);
    if ((*(uint32_t *)(v_rip + 0x84B7D6)) == 72) {
        result = 4;
    }
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA07111))) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_005BFB0F;
    if (((*(uint32_t *)(v_rip + 0x951444)) & (0x800000ULL)) != 0) goto loc_005BFA8B;
    goto loc_005BFB0F;
loc_005BFA8B:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA070C3)) == 0) goto loc_005BFAC5;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xA070A7)) & (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint8_t)((*(uint8_t *)(v_stack_m58 + 0x6DC)) & (207));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    *(uint8_t *)(v_stack_m58 + 0x6DC) = (uint8_t)(Arg1);
    goto loc_005BFB0F;
loc_005BFAC5:
    if (condition_is_above_or_equal) goto loc_005BFB07;
    goto loc_005BFB0F;
loc_005BFB07:
loc_005BFB0F:
    if (((local_r12) & (*(uint64_t *)(v_rip + 0xA07032))) != 0) goto loc_005BFBA0;
loc_005BFB1F:
loc_005BFB29:
    *(uint16_t *)(v_stack_m58 + 0x6E6) = (uint16_t)(*(uint16_t *)(v_stack_m58 + 0x6E8));
    if ((uint16_t)(*(uint16_t *)(v_stack_m58 + 0x6E8)) != 0) {
        a2 = (uint32_t)(*(uint16_t *)(v_stack_m58 + 0x6E8));
        Arg1 = 72;
        a2 = (a2) >> (32);
    }
    if (((128) & (*(uint64_t *)(v_rip + 0xA06FF8))) == 0) goto loc_005BFB79;
    result = *(uint64_t *)(v_rip + 0xA06FF8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x84B69D)))) != 72) {
        a2 = (a2) << (32);
        result = (*(uint64_t *)(v_rip + 0xA06FF8)) | (a2);
        result = (result) | (*(uint64_t *)(v_rip + 0x84B680));
        a2 = result;
        a2 = (a2) >> (32);
    }
    result = KiSetMicrocodeUpdateOptions((uint32_t)(*(uint32_t *)(v_rip + 0x84B69D)), a2, 128, (uint32_t)(0x400ULL));
    result = KiSetVirtualMitigationControl(v_stack_m58, a2, 128, (uint32_t)(0x400ULL));
    result = 0;
    local_rsp = (local_rsp) + (56);
    return result;
loc_005BFB9A:
loc_005BFBA0:
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06FA1))) & (16)) == 0) goto loc_005BFBB5;
    *(uint16_t *)(v_stack_m58 + 0x6EA) = 1;
    goto loc_005BFBD4;
loc_005BFBB5:
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06F8C))) & (64)) == 0) goto loc_005BFBD4;
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06F81)))) != 0) {
        *(uint16_t *)(v_stack_m58 + 0x6EA) = 2;
    }
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA06F6D))) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (((128) & (*(uint64_t *)(v_rip + 0xA06F43))) != 0) goto loc_005BFC20;
    if (((local_r12) & (*(uint64_t *)(v_rip + 0xA06F2D))) == 0) goto loc_005BFC35;
loc_005BFC20:
    result = *(uint64_t *)(v_rip + 0xA06F2D);
    if ((*(uint32_t *)(v_rip + 0x84B5D1)) == 72) {
        result = 4;
    }
    if (((1) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06F0C)))) != 0) goto loc_005BFB29;
    if ((*(uint8_t *)(v_stack_m58 + 0x8D)) == 1) {
    }
    if (Arg1 == 0) goto loc_005BFD87;
    v_stack_p10 = 0;
    result = (uint32_t)((*(uint64_t *)(v_rip + 0xA06F0C)) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & (0x80000000ULL));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005BFCA6;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(Arg1 + 0x4)));
    v_stack_p10 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_005BFD82;
    result = KeWakeAddressAll(Arg1, a2, 128, (uint32_t)(0x400ULL));
    goto loc_005BFD82;
loc_005BFCA6:
    goto loc_005BFD6C;
loc_005BFCB1:
    local_r15 = (uint32_t)((0) + (1));
    if (((*(uint32_t *)(v_rip + 0xA055F1)) & ((uint32_t)(local_r15))) != 0) goto loc_005BFD6A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA06DF1)))) & (64)) == 0) goto loc_005BFD6A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, a2, 128, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) == 0) goto loc_005BFD6A;
    local_r12 = (uint32_t)((0) + (1));
    result = KeCanUseHaltOnAddress(Arg1, a2, 128, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) == 0) goto loc_005BFD60;
    if (((*(uint32_t *)(v_rip + 0xA06E46)) & (0x20000ULL)) == 0) goto loc_005BFD60;
    if ((((uint8_t)(local_r12)) & (7)) != 0) goto loc_005BFD60;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (0x80000000ULL));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_005BFD6C;
loc_005BFD15:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005BFD44;
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
loc_005BFD2E:
    result = KiHaltOnAddress(Arg1, v_stack_p10, 4, (uint32_t)(0x400ULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005BFD2E;
loc_005BFD44:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (0x80000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005BFD15;
    local_r13 = 0;
    goto loc_005BFD6C;
loc_005BFD60:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)(0x400ULL));
    goto loc_005BFD6C;
loc_005BFD6A:
loc_005BFD6C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) & (0x80000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005BFCB1;
loc_005BFD82:
loc_005BFD87:
    result = *(uint64_t *)(v_rip + 0xA06DBA);
    if (((uint32_t)(result)) < ((uint32_t)(local_rdi))) {
        result = 4;
        result = KeExitRetpoline((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)(0x400ULL));
    }
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06D9C)))) == 0) goto loc_005BFDF5;
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA06D90))) != 0) goto loc_005BFDF5;
    if ((*(uint8_t *)(v_rip + 0xA06CD3)) != 0) goto loc_005BFDF5;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06D7B))) & (16)) != 0) goto loc_005BFDDC;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06D70))) & (64)) != 0) {
    }
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06D4C)))) == 0) goto loc_005BFF0D;
    if (((64) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06D36)))) == 0) goto loc_005BFF0D;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06D26))) & (16)) == 0) goto loc_005BFF0D;
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA06D17))) != 0) goto loc_005BFF17;
    if ((((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (*(uint64_t *)(v_rip + 0xA06CFD))) != 0) goto loc_005BFF17;
    if (((uint32_t)(*(uint64_t *)(v_rip + 0xA06CFD))) != 2) goto loc_005BFF0D;
    if ((*(uint8_t *)(v_rip + 0xA06C27)) == 0) goto loc_005BFEC3;
    result = HvlIsCoreSharingPossible((uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(v_stack_m58 + 0x8E60), 0, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) == 0) goto loc_005BFEC3;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA06C0F))))) == 0) goto loc_005BFF0D;
    if (condition_is_above_or_equal) goto loc_005BFF0D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA06E56))) - (1));
    if (condition_is_equal) goto loc_005BFF0D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005BFF0D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005BFEC3;
    if (((uint32_t)(Arg1)) != 1) goto loc_005BFF0D;
    result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60) - 1;
    if (((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60)) & (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60) - 1)) != 0) {
        Arg1 = *(uint8_t *)(v_stack_m58 + 0xD1);
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r13 + 1)));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60) - 1)));
        v_stack_p20 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E60) - 1);
        result = *(uint8_t *)(v_stack_m58 + 0xD0);
        Arg1 = (uint32_t)((Arg1) & (63));
        result = (uint32_t)((result) << (6));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
        result = *(uint64_t *)(v_rip + 0x9632C9);
        Arg1 = *(uint32_t *)(result + Arg1 * 4);
        result = KeGetPrcb(Arg1, *(uint64_t *)(v_stack_m58 + 0x8E60), 0, (uint32_t)(0x400ULL));
        *(uint64_t *)(v_stack_m58 + 0x2DB0) = result;
        a3 = (uint32_t)(local_r13 + 1);
        result = 6;
        *(uint16_t *)(v_stack_m58 + 0x6E0) = (uint16_t)(result);
    }
loc_005BFF17:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x950FA3)))) & (32)) == 0) goto loc_005BFF39;
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06C20)))) == 0) goto loc_005BFF39;
    if (((64) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06C14)))) != 0) goto loc_005BFF74;
loc_005BFF39:
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06C08)))) == 0) goto loc_005BFF86;
    if (((64) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06BFC)))) == 0) goto loc_005BFF86;
    if ((uint32_t)(a3) != 0) goto loc_005BFF86;
    if (((*(uint64_t *)(v_stack_m58 + 0x8E60)) & (*(uint64_t *)(v_rip + 0xA06BEB))) != 0) goto loc_005BFF86;
    if ((*(uint8_t *)(v_rip + 0xA06B2E)) == 0) goto loc_005BFF86;
    result = HvlIsCoreSharingPossible(Arg1, *(uint64_t *)(v_stack_m58 + 0x8E60), a3, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) != 0) {
    }
    if (((2) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06BBB)))) == 0) goto loc_005BFFCD;
    if (((64) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA06BAF)))) == 0) goto loc_005BFFCD;
    if ((((uint32_t)(0x4000ULL)) & (*(uint64_t *)(v_rip + 0xA06BA3))) == 0) goto loc_005BFFCD;
    if ((uint32_t)(a3) != 0) goto loc_005BFFCD;
    if (((*(uint64_t *)(v_stack_m58 + 0x8E60)) & (*(uint64_t *)(v_rip + 0xA06B92))) == 0) {
    }
    if ((*(uint8_t *)(v_stack_m58 + 0x8D)) != ((uint8_t)(local_r13 + 1))) goto loc_005C0003;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xA06B6B))) & (16)) != 0) goto loc_005C0003;
    if (((64) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x950ED9))))) != 0) goto loc_005C0003;
    goto loc_005BFB1F;
loc_005C0003:
    result = KiIsBranchConfusionPresent(v_stack_m58, *(uint64_t *)(v_stack_m58 + 0x8E60), a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) == 0) goto loc_005C005C;
    result = KiIsBranchConfusionMitigationDesired(v_stack_m58, v_rip + 10513190, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) != 0) goto loc_005C003A;
    goto loc_005C0054;
loc_005C003A:
    result = KiIsBranchConfusionMitigationSupported(v_stack_m58, v_rip + 10513159, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) != 0) goto loc_005C005C;
loc_005C0054:
loc_005C005C:
    if (condition_is_above_or_equal) goto loc_005C00A6;
    result = KiIsTsaMitigationDesired(v_stack_m58, v_rip + 10513159, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) != 0) goto loc_005C007F;
    goto loc_005C0095;
loc_005C007F:
    result = KiIsTsaMitigationSupported(v_stack_m58, v_rip + 10513159, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) != 0) goto loc_005C009F;
loc_005C0095:
    goto loc_005C00A6;
loc_005C009F:
loc_005C00A6:
    if (condition_is_above_or_equal) goto loc_005C0162;
    if (((*(uint32_t *)(v_rip + 0x950DFE)) & (0x800000ULL)) != 0) goto loc_005C00D3;
    goto loc_005C015A;
loc_005C00D3:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA06A7B)) == 0) goto loc_005C010D;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xA06A5F)) & (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint8_t)((*(uint8_t *)(v_stack_m58 + 0x6DC)) & (207));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    *(uint8_t *)(v_stack_m58 + 0x6DC) = (uint8_t)(Arg1);
    goto loc_005C0162;
loc_005C010D:
    if (condition_is_above_or_equal) goto loc_005C0150;
    goto loc_005C0162;
loc_005C0150:
loc_005C015A:
loc_005C0162:
    if (condition_is_above_or_equal) goto loc_005C020A;
    if (((4) & ((uint8_t)(*(uint64_t *)(v_rip + 0xA069CD)))) != 0) goto loc_005C0190;
    goto loc_005C0202;
loc_005C0190:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x950D2A)))) & (5)) != 0) goto loc_005C01F8;
    if ((*(uint8_t *)(v_stack_m58 + 0x8D)) != ((uint8_t)(local_r13 + 1))) goto loc_005C01BD;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_rip + 0xA0699E))) & (16)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(v_rip + 0x950D0A)) & (64)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_005C01F8;
loc_005C01BD:
    result = KiIsBranchConfusionPresent(v_stack_m58, v_rip + 10513159, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) == 0) goto loc_005C01EC;
    result = KiIsBranchConfusionMitigationSupported(v_stack_m58, v_rip + 10512760, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) == 0) goto loc_005C01EC;
    result = KiIsBranchConfusionMitigationDesired(v_stack_m58, v_rip + 10512744, a3, (uint32_t)(0x400ULL));
    if ((uint32_t)(result) != 0) goto loc_005C020A;
loc_005C01EC:
    if (((*(uint32_t *)(v_rip + 0x950CCA)) & (0x4000000ULL)) != 0) goto loc_005C020A;
loc_005C01F8:
loc_005C0202:
loc_005C020A:
    if (Arg1 == 0) goto loc_005C031E;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_005C024C;
    local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(Arg1 + 0x4)));
    if (condition_is_above_or_equal) goto loc_005C031E;
    result = KeWakeAddressAll(Arg1, v_rip + 10512744, a3, (uint32_t)(0x400ULL));
    goto loc_005C031E;
loc_005C024C:
    goto loc_005C0310;
loc_005C0257:
    local_r14 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xA0504B)) & ((uint32_t)(local_r14))) != 0) goto loc_005C030E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA0684B)))) & (64)) == 0) goto loc_005C030E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, v_rip + 10512744, a3, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) == 0) goto loc_005C030E;
    local_r12 = (uint32_t)((0) + 1);
    result = KeCanUseHaltOnAddress(Arg1, v_rip + 10512744, a3, (uint32_t)(0x400ULL));
    if ((uint8_t)(result) == 0) goto loc_005C0304;
    if (((*(uint32_t *)(v_rip + 0xA068A0)) & (0x20000ULL)) == 0) goto loc_005C0304;
    if ((((uint8_t)(local_r12)) & (7)) != 0) goto loc_005C0304;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_005C0310;
loc_005C02B9:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005C02E8;
    v_stack_p18 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
loc_005C02D2:
    result = KiHaltOnAddress(Arg1, v_stack_p18, 4, (uint32_t)(0x400ULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))) == ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))))) goto loc_005C02D2;
loc_005C02E8:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005C02B9;
    local_r13 = 0;
    goto loc_005C0310;
loc_005C0304:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)(0x400ULL));
    goto loc_005C0310;
loc_005C030E:
loc_005C0310:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi))) goto loc_005C0257;
loc_005C031E:
    result = KiUpdateSpeculationControl(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), (uint32_t)(0x400ULL));
    goto loc_005BFB1F;
loc_005C0338:
    if (((local_r12) & (*(uint64_t *)(v_rip + 0xA06809))) != 0) {
    }
    if ((((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) & (*(uint64_t *)(v_rip + 0xA067D9))) == 0) goto loc_005BFB29;
    result = *(uint16_t *)(v_stack_m58 + 0x6E8);
    if ((*(uint32_t *)(v_rip + 0x84AE79)) == 72) {
        result = (uint16_t)((*(uint16_t *)(v_stack_m58 + 0x6E8)) | (4));
    }
    *(uint16_t *)(v_stack_m58 + 0x6E8) = (uint16_t)(result);
    *(uint16_t *)(v_stack_m58 + 0x6EC) = (uint16_t)(result);
    goto loc_005BFB29;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BF5A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
