# MiWritePteHighLevelIsr

- RVA: `0x004C2FC0`–`0x004C3742` (길이 `1,922` bytes)
- VA: `0x00000001404C2FC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCB44`
- 디코드: `563`개 명령, `1,922/1,922` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004C3006` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C30B2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x004C30F6` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004C3103` → [MiStackCopyHighLevel](../67/MiStackCopyHighLevel_function_0067B204.md) (function, `0x0067B204`)
- `0x004C3124` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x004C312E` → [MiWriteValidPteNewPage](../37/MiWriteValidPteNewPage_function_00376068.md) (function, `0x00376068`)
- `0x004C3171` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004C31A4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C31B0` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C31FE` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C3220` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C3261` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C326D` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C32C3` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C32E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C332B` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004C335E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C336A` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C33B8` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C33DA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C3409` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004C3439` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004C3465` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x004C349B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C34AB` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C34FD` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C3521` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C3565` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C3571` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C35BF` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C35E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C363D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C364D` → [KeCanUseHaltOnAddress](../4F/KeCanUseHaltOnAddress_function_004FC22C.md) (function, `0x004FC22C`)
- `0x004C369F` → [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) (function, `0x004FBA3C`)
- `0x004C36C3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C36EF` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004C3708` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x004C371B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004C2FE3` → RVA `0x00E0A740` (`.data`; read)
- `0x004C30A7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x004C3189` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x004C3196` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x004C31B9` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C2FC0  48 8B C4                        mov rax, rsp
004C2FC3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
004C2FC7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
004C2FCB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
004C2FCF  55                              push rbp
004C2FD0  41 54                           push r12
004C2FD2  41 55                           push r13
004C2FD4  41 56                           push r14
004C2FD6  41 57                           push r15
004C2FD8  48 8D 68 A8                     lea rbp, [rax - 0x58]
004C2FDC  48 81 EC 30 01 00 00            sub rsp, 0x130
004C2FE3  48 8B 05 56 77 94 00            mov rax, qword ptr [rip + 0x947756]
004C2FEA  48 33 C4                        xor rax, rsp
004C2FED  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
004C2FF1  48 8B F1                        mov rsi, rcx
004C2FF4  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
004C2FF9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004C2FFE  33 D2                           xor edx, edx
004C3000  41 B8 C8 00 00 00               mov r8d, 0xc8
004C3006  E8 35 3C 20 00                  call 0x1406c6c40
004C300B  4C 8B 26                        mov r12, qword ptr [rsi]
004C300E  48 8D 46 20                     lea rax, [rsi + 0x20]
004C3012  4C 8B BE E8 00 00 00            mov r15, qword ptr [rsi + 0xe8]
004C3019  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004C301E  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
004C3022  BA 80 00 00 00                  mov edx, 0x80
004C3027  49 8B 3C 24                     mov rdi, qword ptr [r12]
004C302B  0F 10 00                        movups xmm0, xmmword ptr [rax]
004C302E  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
004C3032  0F 11 01                        movups xmmword ptr [rcx], xmm0
004C3035  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
004C3039  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
004C303D  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
004C3041  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
004C3045  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
004C3049  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
004C304D  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
004C3051  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
004C3055  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
004C3059  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
004C305D  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
004C3061  48 03 CA                        add rcx, rdx
004C3064  0F 10 40 70                     movups xmm0, xmmword ptr [rax + 0x70]
004C3068  48 03 C2                        add rax, rdx
004C306B  0F 11 41 F0                     movups xmmword ptr [rcx - 0x10], xmm0
004C306F  0F 10 08                        movups xmm1, xmmword ptr [rax]
004C3072  0F 10 40 10                     movups xmm0, xmmword ptr [rax + 0x10]
004C3076  0F 11 09                        movups xmmword ptr [rcx], xmm1
004C3079  0F 10 48 20                     movups xmm1, xmmword ptr [rax + 0x20]
004C307D  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
004C3081  0F 10 40 30                     movups xmm0, xmmword ptr [rax + 0x30]
004C3085  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
004C3089  0F 11 49 20                     movups xmmword ptr [rcx + 0x20], xmm1
004C308D  0F 11 41 30                     movups xmmword ptr [rcx + 0x30], xmm0
004C3091  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
004C3095  44 0F 20 C0                     mov rax, cr8
004C3099  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004C309E  BA 0F 00 00 00                  mov edx, 0xf
004C30A3  44 0F 22 C2                     mov cr8, rdx
004C30A7  83 3D 72 3C B0 00 00            cmp dword ptr [rip + 0xb03c72], 0
004C30AE  74 07                           je 0x1404c30b7
004C30B0  8A C8                           mov cl, al
004C30B2  E8 45 26 03 00                  call 0x1404f56fc
004C30B7  48 83 C6 14                     add rsi, 0x14
004C30BB  83 C8 FF                        or eax, 0xffffffff
004C30BE  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C30C2  FF C8                           dec eax
004C30C4  41 BD 00 00 00 40               mov r13d, 0x40000000
004C30CA  44 8B F0                        mov r14d, eax
004C30CD  41 F7 D6                        not r14d
004C30D0  41 81 E6 00 00 00 80            and r14d, 0x80000000
004C30D7  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C30DC  0F 85 59 01 00 00               jne 0x1404c323b
004C30E2  44 0B 76 04                     or r14d, dword ptr [rsi + 4]
004C30E6  44 87 36                        xchg dword ptr [rsi], r14d
004C30E9  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
004C30EE  45 85 F5                        test r13d, r14d
004C30F1  74 08                           je 0x1404c30fb
004C30F3  48 8B CE                        mov rcx, rsi
004C30F6  E8 25 4B D5 FF                  call 0x140217c20
004C30FB  4D 85 FF                        test r15, r15
004C30FE  74 08                           je 0x1404c3108
004C3100  49 8B CF                        mov rcx, r15
004C3103  E8 FC 80 1B 00                  call 0x14067b204
004C3108  48 83 CB 20                     or rbx, 0x20
004C310C  48 B8 00 F0 FF FF FF FF 0F 00   movabs rax, 0xffffffffff000
004C3116  48 33 FB                        xor rdi, rbx
004C3119  48 8B D3                        mov rdx, rbx
004C311C  49 8B CC                        mov rcx, r12
004C311F  48 85 F8                        test rax, rdi
004C3122  75 07                           jne 0x1404c312b
004C3124  E8 E7 E6 DB FF                  call 0x140281810
004C3129  EB 08                           jmp 0x1404c3133
004C312B  45 33 C0                        xor r8d, r8d
004C312E  E8 35 2F EB FF                  call 0x140376068
004C3133  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
004C3137  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
004C313C  41 89 44 24 10                  mov dword ptr [r12 + 0x10], eax
004C3141  83 C8 FF                        or eax, 0xffffffff
004C3144  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C3148  FF C8                           dec eax
004C314A  BF 00 00 00 80                  mov edi, 0x80000000
004C314F  8B D8                           mov ebx, eax
004C3151  F7 D3                           not ebx
004C3153  23 DF                           and ebx, edi
004C3155  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C315A  75 1F                           jne 0x1404c317b
004C315C  0B 5E 04                        or ebx, dword ptr [rsi + 4]
004C315F  87 1E                           xchg dword ptr [rsi], ebx
004C3161  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
004C3165  41 85 DD                        test r13d, ebx
004C3168  0F 84 87 02 00 00               je 0x1404c33f5
004C316E  48 8B CE                        mov rcx, rsi
004C3171  E8 AA 4A D5 FF                  call 0x140217c20
004C3176  E9 7A 02 00 00                  jmp 0x1404c33f5
004C317B  45 33 F6                        xor r14d, r14d
004C317E  45 33 FF                        xor r15d, r15d
004C3181  E9 A3 00 00 00                  jmp 0x1404c3229
004C3186  41 FF C6                        inc r14d
004C3189  44 85 35 1C 21 B0 00            test dword ptr [rip + 0xb0211c], r14d
004C3190  0F 85 91 00 00 00               jne 0x1404c3227
004C3196  8B 05 1C 39 B0 00               mov eax, dword ptr [rip + 0xb0391c]
004C319C  A8 40                           test al, 0x40
004C319E  0F 84 83 00 00 00               je 0x1404c3227
004C31A4  E8 E7 C2 E4 FF                  call 0x14030f490
004C31A9  84 C0                           test al, al
004C31AB  74 7A                           je 0x1404c3227
004C31AD  41 FF C7                        inc r15d
004C31B0  E8 77 90 03 00                  call 0x1404fc22c
004C31B5  84 C0                           test al, al
004C31B7  74 64                           je 0x1404c321d
004C31B9  F7 05 75 39 B0 00 00 00 02 00   test dword ptr [rip + 0xb03975], 0x20000
004C31C3  74 58                           je 0x1404c321d
004C31C5  41 F6 C7 07                     test r15b, 7
004C31C9  75 52                           jne 0x1404c321d
004C31CB  8B 0E                           mov ecx, dword ptr [rsi]
004C31CD  8B C1                           mov eax, ecx
004C31CF  23 C7                           and eax, edi
004C31D1  3B C3                           cmp eax, ebx
004C31D3  74 54                           je 0x1404c3229
004C31D5  8B D1                           mov edx, ecx
004C31D7  44 8B C1                        mov r8d, ecx
004C31DA  41 0B CD                        or ecx, r13d
004C31DD  8B C2                           mov eax, edx
004C31DF  8B F9                           mov edi, ecx
004C31E1  F0 0F B1 3E                     lock cmpxchg dword ptr [rsi], edi
004C31E5  8B C8                           mov ecx, eax
004C31E7  41 3B C0                        cmp eax, r8d
004C31EA  75 1D                           jne 0x1404c3209
004C31EC  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
004C31F0  41 B8 04 00 00 00               mov r8d, 4
004C31F6  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
004C31FB  48 8B CE                        mov rcx, rsi
004C31FE  E8 39 88 03 00                  call 0x1404fba3c
004C3203  8B 0E                           mov ecx, dword ptr [rsi]
004C3205  3B CF                           cmp ecx, edi
004C3207  74 E7                           je 0x1404c31f0
004C3209  8B C1                           mov eax, ecx
004C320B  BF 00 00 00 80                  mov edi, 0x80000000
004C3210  23 C7                           and eax, edi
004C3212  8B D1                           mov edx, ecx
004C3214  44 8B C1                        mov r8d, ecx
004C3217  3B C3                           cmp eax, ebx
004C3219  75 BF                           jne 0x1404c31da
004C321B  EB 0C                           jmp 0x1404c3229
004C321D  41 8B CE                        mov ecx, r14d
004C3220  E8 3B C2 E4 FF                  call 0x14030f460
004C3225  EB 02                           jmp 0x1404c3229
004C3227  F3 90                           pause
004C3229  8B 06                           mov eax, dword ptr [rsi]
004C322B  23 C7                           and eax, edi
004C322D  3B C3                           cmp eax, ebx
004C322F  0F 85 51 FF FF FF               jne 0x1404c3186
004C3235  90                              nop
004C3236  E9 BA 01 00 00                  jmp 0x1404c33f5
004C323B  33 FF                           xor edi, edi
004C323D  45 33 FF                        xor r15d, r15d
004C3240  E9 A5 00 00 00                  jmp 0x1404c32ea
004C3245  FF C7                           inc edi
004C3247  85 3D 5F 20 B0 00               test dword ptr [rip + 0xb0205f], edi
004C324D  0F 85 95 00 00 00               jne 0x1404c32e8
004C3253  8B 05 5F 38 B0 00               mov eax, dword ptr [rip + 0xb0385f]
004C3259  A8 40                           test al, 0x40
004C325B  0F 84 87 00 00 00               je 0x1404c32e8
004C3261  E8 2A C2 E4 FF                  call 0x14030f490
004C3266  84 C0                           test al, al
004C3268  74 7E                           je 0x1404c32e8
004C326A  41 FF C7                        inc r15d
004C326D  E8 BA 8F 03 00                  call 0x1404fc22c
004C3272  84 C0                           test al, al
004C3274  74 69                           je 0x1404c32df
004C3276  F7 05 B8 38 B0 00 00 00 02 00   test dword ptr [rip + 0xb038b8], 0x20000
004C3280  74 5D                           je 0x1404c32df
004C3282  41 F6 C7 07                     test r15b, 7
004C3286  75 57                           jne 0x1404c32df
004C3288  8B 0E                           mov ecx, dword ptr [rsi]
004C328A  41 BC 00 00 00 80               mov r12d, 0x80000000
004C3290  8B C1                           mov eax, ecx
004C3292  41 23 C4                        and eax, r12d
004C3295  41 3B C6                        cmp eax, r14d
004C3298  74 50                           je 0x1404c32ea
004C329A  8B D1                           mov edx, ecx
004C329C  44 8B C1                        mov r8d, ecx
004C329F  41 0B CD                        or ecx, r13d
004C32A2  8B C2                           mov eax, edx
004C32A4  8B D9                           mov ebx, ecx
004C32A6  F0 0F B1 1E                     lock cmpxchg dword ptr [rsi], ebx
004C32AA  8B C8                           mov ecx, eax
004C32AC  41 3B C0                        cmp eax, r8d
004C32AF  75 1D                           jne 0x1404c32ce
004C32B1  89 5C 24 24                     mov dword ptr [rsp + 0x24], ebx
004C32B5  41 B8 04 00 00 00               mov r8d, 4
004C32BB  48 8D 54 24 24                  lea rdx, [rsp + 0x24]
004C32C0  48 8B CE                        mov rcx, rsi
004C32C3  E8 74 87 03 00                  call 0x1404fba3c
004C32C8  8B 0E                           mov ecx, dword ptr [rsi]
004C32CA  3B CB                           cmp ecx, ebx
004C32CC  74 E7                           je 0x1404c32b5
004C32CE  8B C1                           mov eax, ecx
004C32D0  8B D1                           mov edx, ecx
004C32D2  41 23 C4                        and eax, r12d
004C32D5  44 8B C1                        mov r8d, ecx
004C32D8  41 3B C6                        cmp eax, r14d
004C32DB  75 C2                           jne 0x1404c329f
004C32DD  EB 0B                           jmp 0x1404c32ea
004C32DF  8B CF                           mov ecx, edi
004C32E1  E8 7A C1 E4 FF                  call 0x14030f460
004C32E6  EB 02                           jmp 0x1404c32ea
004C32E8  F3 90                           pause
004C32EA  8B 06                           mov eax, dword ptr [rsi]
004C32EC  25 00 00 00 80                  and eax, 0x80000000
004C32F1  41 3B C6                        cmp eax, r14d
004C32F4  0F 85 4B FF FF FF               jne 0x1404c3245
004C32FA  90                              nop
004C32FB  83 C8 FF                        or eax, 0xffffffff
004C32FE  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C3302  FF C8                           dec eax
004C3304  BF 00 00 00 80                  mov edi, 0x80000000
004C3309  8B D8                           mov ebx, eax
004C330B  F7 D3                           not ebx
004C330D  23 DF                           and ebx, edi
004C330F  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C3314  75 1F                           jne 0x1404c3335
004C3316  0B 5E 04                        or ebx, dword ptr [rsi + 4]
004C3319  87 1E                           xchg dword ptr [rsi], ebx
004C331B  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
004C331F  41 85 DD                        test r13d, ebx
004C3322  0F 84 C8 00 00 00               je 0x1404c33f0
004C3328  48 8B CE                        mov rcx, rsi
004C332B  E8 F0 48 D5 FF                  call 0x140217c20
004C3330  E9 BB 00 00 00                  jmp 0x1404c33f0
004C3335  45 33 F6                        xor r14d, r14d
004C3338  45 33 FF                        xor r15d, r15d
004C333B  E9 A3 00 00 00                  jmp 0x1404c33e3
004C3340  41 FF C6                        inc r14d
004C3343  44 85 35 62 1F B0 00            test dword ptr [rip + 0xb01f62], r14d
004C334A  0F 85 91 00 00 00               jne 0x1404c33e1
004C3350  8B 05 62 37 B0 00               mov eax, dword ptr [rip + 0xb03762]
004C3356  A8 40                           test al, 0x40
004C3358  0F 84 83 00 00 00               je 0x1404c33e1
004C335E  E8 2D C1 E4 FF                  call 0x14030f490
004C3363  84 C0                           test al, al
004C3365  74 7A                           je 0x1404c33e1
004C3367  41 FF C7                        inc r15d
004C336A  E8 BD 8E 03 00                  call 0x1404fc22c
004C336F  84 C0                           test al, al
004C3371  74 64                           je 0x1404c33d7
004C3373  F7 05 BB 37 B0 00 00 00 02 00   test dword ptr [rip + 0xb037bb], 0x20000
004C337D  74 58                           je 0x1404c33d7
004C337F  41 F6 C7 07                     test r15b, 7
004C3383  75 52                           jne 0x1404c33d7
004C3385  8B 0E                           mov ecx, dword ptr [rsi]
004C3387  8B C1                           mov eax, ecx
004C3389  23 C7                           and eax, edi
004C338B  3B C3                           cmp eax, ebx
004C338D  74 54                           je 0x1404c33e3
004C338F  8B D1                           mov edx, ecx
004C3391  44 8B C1                        mov r8d, ecx
004C3394  41 0B CD                        or ecx, r13d
004C3397  8B C2                           mov eax, edx
004C3399  8B F9                           mov edi, ecx
004C339B  F0 0F B1 3E                     lock cmpxchg dword ptr [rsi], edi
004C339F  8B C8                           mov ecx, eax
004C33A1  41 3B C0                        cmp eax, r8d
004C33A4  75 1D                           jne 0x1404c33c3
004C33A6  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
004C33AA  41 B8 04 00 00 00               mov r8d, 4
004C33B0  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
004C33B5  48 8B CE                        mov rcx, rsi
004C33B8  E8 7F 86 03 00                  call 0x1404fba3c
004C33BD  8B 0E                           mov ecx, dword ptr [rsi]
004C33BF  3B CF                           cmp ecx, edi
004C33C1  74 E7                           je 0x1404c33aa
004C33C3  8B C1                           mov eax, ecx
004C33C5  BF 00 00 00 80                  mov edi, 0x80000000
004C33CA  23 C7                           and eax, edi
004C33CC  8B D1                           mov edx, ecx
004C33CE  44 8B C1                        mov r8d, ecx
004C33D1  3B C3                           cmp eax, ebx
004C33D3  75 BF                           jne 0x1404c3394
004C33D5  EB 0C                           jmp 0x1404c33e3
004C33D7  41 8B CE                        mov ecx, r14d
004C33DA  E8 81 C0 E4 FF                  call 0x14030f460
004C33DF  EB 02                           jmp 0x1404c33e3
004C33E1  F3 90                           pause
004C33E3  8B 06                           mov eax, dword ptr [rsi]
004C33E5  23 C7                           and eax, edi
004C33E7  3B C3                           cmp eax, ebx
004C33E9  0F 85 51 FF FF FF               jne 0x1404c3340
004C33EF  90                              nop
004C33F0  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
004C33F5  49 8B CC                        mov rcx, r12
004C33F8  B8 10 00 00 00                  mov eax, 0x10
004C33FD  8B 04 01                        mov eax, dword ptr [rcx + rax]
004C3400  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004C3405  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
004C3409  E8 B2 EB E4 FF                  call 0x140311fc0
004C340E  83 C8 FF                        or eax, 0xffffffff
004C3411  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C3415  FF C8                           dec eax
004C3417  8B D8                           mov ebx, eax
004C3419  F7 D3                           not ebx
004C341B  23 DF                           and ebx, edi
004C341D  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C3422  0F 85 14 01 00 00               jne 0x1404c353c
004C3428  0B 5E 04                        or ebx, dword ptr [rsi + 4]
004C342B  87 1E                           xchg dword ptr [rsi], ebx
004C342D  89 5C 24 2C                     mov dword ptr [rsp + 0x2c], ebx
004C3431  41 85 DD                        test r13d, ebx
004C3434  74 08                           je 0x1404c343e
004C3436  48 8B CE                        mov rcx, rsi
004C3439  E8 E2 47 D5 FF                  call 0x140217c20
004C343E  83 C8 FF                        or eax, 0xffffffff
004C3441  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C3445  FF C8                           dec eax
004C3447  8B D8                           mov ebx, eax
004C3449  F7 D3                           not ebx
004C344B  23 DF                           and ebx, edi
004C344D  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C3452  75 1B                           jne 0x1404c346f
004C3454  0B 5E 04                        or ebx, dword ptr [rsi + 4]
004C3457  87 1E                           xchg dword ptr [rsi], ebx
004C3459  41 85 DD                        test r13d, ebx
004C345C  0F 84 78 02 00 00               je 0x1404c36da
004C3462  48 8B CE                        mov rcx, rsi
004C3465  E8 B6 47 D5 FF                  call 0x140217c20
004C346A  E9 6B 02 00 00                  jmp 0x1404c36da
004C346F  33 FF                           xor edi, edi
004C3471  41 BE 00 00 00 80               mov r14d, 0x80000000
004C3477  45 33 FF                        xor r15d, r15d
004C347A  E9 AB 00 00 00                  jmp 0x1404c352a
004C347F  FF C7                           inc edi
004C3481  85 3D 25 1E B0 00               test dword ptr [rip + 0xb01e25], edi
004C3487  0F 85 9B 00 00 00               jne 0x1404c3528
004C348D  8B 05 25 36 B0 00               mov eax, dword ptr [rip + 0xb03625]
004C3493  A8 40                           test al, 0x40
004C3495  0F 84 8D 00 00 00               je 0x1404c3528
004C349B  E8 F0 BF E4 FF                  call 0x14030f490
004C34A0  84 C0                           test al, al
004C34A2  0F 84 80 00 00 00               je 0x1404c3528
004C34A8  41 FF C7                        inc r15d
004C34AB  E8 7C 8D 03 00                  call 0x1404fc22c
004C34B0  84 C0                           test al, al
004C34B2  74 6B                           je 0x1404c351f
004C34B4  F7 05 7A 36 B0 00 00 00 02 00   test dword ptr [rip + 0xb0367a], 0x20000
004C34BE  74 5F                           je 0x1404c351f
004C34C0  41 F6 C7 07                     test r15b, 7
004C34C4  75 59                           jne 0x1404c351f
004C34C6  8B 0E                           mov ecx, dword ptr [rsi]
004C34C8  8B C1                           mov eax, ecx
004C34CA  41 23 C6                        and eax, r14d
004C34CD  3B C3                           cmp eax, ebx
004C34CF  74 59                           je 0x1404c352a
004C34D1  8B D1                           mov edx, ecx
004C34D3  44 8B C1                        mov r8d, ecx
004C34D6  41 0B CD                        or ecx, r13d
004C34D9  8B C2                           mov eax, edx
004C34DB  44 8B F1                        mov r14d, ecx
004C34DE  F0 44 0F B1 36                  lock cmpxchg dword ptr [rsi], r14d
004C34E3  8B C8                           mov ecx, eax
004C34E5  41 3B C0                        cmp eax, r8d
004C34E8  75 1F                           jne 0x1404c3509
004C34EA  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
004C34EF  41 B8 04 00 00 00               mov r8d, 4
004C34F5  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
004C34FA  48 8B CE                        mov rcx, rsi
004C34FD  E8 3A 85 03 00                  call 0x1404fba3c
004C3502  8B 0E                           mov ecx, dword ptr [rsi]
004C3504  41 3B CE                        cmp ecx, r14d
004C3507  74 E6                           je 0x1404c34ef
004C3509  8B C1                           mov eax, ecx
004C350B  41 BE 00 00 00 80               mov r14d, 0x80000000
004C3511  41 23 C6                        and eax, r14d
004C3514  8B D1                           mov edx, ecx
004C3516  44 8B C1                        mov r8d, ecx
004C3519  3B C3                           cmp eax, ebx
004C351B  75 B9                           jne 0x1404c34d6
004C351D  EB 0B                           jmp 0x1404c352a
004C351F  8B CF                           mov ecx, edi
004C3521  E8 3A BF E4 FF                  call 0x14030f460
004C3526  EB 02                           jmp 0x1404c352a
004C3528  F3 90                           pause
004C352A  8B 06                           mov eax, dword ptr [rsi]
004C352C  41 23 C6                        and eax, r14d
004C352F  3B C3                           cmp eax, ebx
004C3531  0F 85 48 FF FF FF               jne 0x1404c347f
004C3537  E9 9D 01 00 00                  jmp 0x1404c36d9
004C353C  45 33 F6                        xor r14d, r14d
004C353F  45 33 FF                        xor r15d, r15d
004C3542  E9 A3 00 00 00                  jmp 0x1404c35ea
004C3547  41 FF C6                        inc r14d
004C354A  44 85 35 5B 1D B0 00            test dword ptr [rip + 0xb01d5b], r14d
004C3551  0F 85 91 00 00 00               jne 0x1404c35e8
004C3557  8B 05 5B 35 B0 00               mov eax, dword ptr [rip + 0xb0355b]
004C355D  A8 40                           test al, 0x40
004C355F  0F 84 83 00 00 00               je 0x1404c35e8
004C3565  E8 26 BF E4 FF                  call 0x14030f490
004C356A  84 C0                           test al, al
004C356C  74 7A                           je 0x1404c35e8
004C356E  41 FF C7                        inc r15d
004C3571  E8 B6 8C 03 00                  call 0x1404fc22c
004C3576  84 C0                           test al, al
004C3578  74 64                           je 0x1404c35de
004C357A  F7 05 B4 35 B0 00 00 00 02 00   test dword ptr [rip + 0xb035b4], 0x20000
004C3584  74 58                           je 0x1404c35de
004C3586  41 F6 C7 07                     test r15b, 7
004C358A  75 52                           jne 0x1404c35de
004C358C  8B 0E                           mov ecx, dword ptr [rsi]
004C358E  8B C1                           mov eax, ecx
004C3590  23 C7                           and eax, edi
004C3592  3B C3                           cmp eax, ebx
004C3594  74 54                           je 0x1404c35ea
004C3596  8B D1                           mov edx, ecx
004C3598  44 8B C1                        mov r8d, ecx
004C359B  41 0B CD                        or ecx, r13d
004C359E  8B C2                           mov eax, edx
004C35A0  8B F9                           mov edi, ecx
004C35A2  F0 0F B1 3E                     lock cmpxchg dword ptr [rsi], edi
004C35A6  8B C8                           mov ecx, eax
004C35A8  41 3B C0                        cmp eax, r8d
004C35AB  75 1D                           jne 0x1404c35ca
004C35AD  89 7C 24 2C                     mov dword ptr [rsp + 0x2c], edi
004C35B1  41 B8 04 00 00 00               mov r8d, 4
004C35B7  48 8D 54 24 2C                  lea rdx, [rsp + 0x2c]
004C35BC  48 8B CE                        mov rcx, rsi
004C35BF  E8 78 84 03 00                  call 0x1404fba3c
004C35C4  8B 0E                           mov ecx, dword ptr [rsi]
004C35C6  3B CF                           cmp ecx, edi
004C35C8  74 E7                           je 0x1404c35b1
004C35CA  8B C1                           mov eax, ecx
004C35CC  BF 00 00 00 80                  mov edi, 0x80000000
004C35D1  23 C7                           and eax, edi
004C35D3  8B D1                           mov edx, ecx
004C35D5  44 8B C1                        mov r8d, ecx
004C35D8  3B C3                           cmp eax, ebx
004C35DA  75 BF                           jne 0x1404c359b
004C35DC  EB 0C                           jmp 0x1404c35ea
004C35DE  41 8B CE                        mov ecx, r14d
004C35E1  E8 7A BE E4 FF                  call 0x14030f460
004C35E6  EB 02                           jmp 0x1404c35ea
004C35E8  F3 90                           pause
004C35EA  8B 06                           mov eax, dword ptr [rsi]
004C35EC  23 C7                           and eax, edi
004C35EE  3B C3                           cmp eax, ebx
004C35F0  0F 85 51 FF FF FF               jne 0x1404c3547
004C35F6  90                              nop
004C35F7  83 C8 FF                        or eax, 0xffffffff
004C35FA  F0 0F C1 06                     lock xadd dword ptr [rsi], eax
004C35FE  FF C8                           dec eax
004C3600  8B D8                           mov ebx, eax
004C3602  F7 D3                           not ebx
004C3604  23 DF                           and ebx, edi
004C3606  A9 FF FF FF 3F                  test eax, 0x3fffffff
004C360B  0F 84 43 FE FF FF               je 0x1404c3454
004C3611  33 FF                           xor edi, edi
004C3613  41 BE 00 00 00 80               mov r14d, 0x80000000
004C3619  45 33 FF                        xor r15d, r15d
004C361C  E9 AB 00 00 00                  jmp 0x1404c36cc
004C3621  FF C7                           inc edi
004C3623  85 3D 83 1C B0 00               test dword ptr [rip + 0xb01c83], edi
004C3629  0F 85 9B 00 00 00               jne 0x1404c36ca
004C362F  8B 05 83 34 B0 00               mov eax, dword ptr [rip + 0xb03483]
004C3635  A8 40                           test al, 0x40
004C3637  0F 84 8D 00 00 00               je 0x1404c36ca
004C363D  E8 4E BE E4 FF                  call 0x14030f490
004C3642  84 C0                           test al, al
004C3644  0F 84 80 00 00 00               je 0x1404c36ca
004C364A  41 FF C7                        inc r15d
004C364D  E8 DA 8B 03 00                  call 0x1404fc22c
004C3652  84 C0                           test al, al
004C3654  74 6B                           je 0x1404c36c1
004C3656  F7 05 D8 34 B0 00 00 00 02 00   test dword ptr [rip + 0xb034d8], 0x20000
004C3660  74 5F                           je 0x1404c36c1
004C3662  41 F6 C7 07                     test r15b, 7
004C3666  75 59                           jne 0x1404c36c1
004C3668  8B 0E                           mov ecx, dword ptr [rsi]
004C366A  8B C1                           mov eax, ecx
004C366C  41 23 C6                        and eax, r14d
004C366F  3B C3                           cmp eax, ebx
004C3671  74 59                           je 0x1404c36cc
004C3673  8B D1                           mov edx, ecx
004C3675  44 8B C1                        mov r8d, ecx
004C3678  41 0B CD                        or ecx, r13d
004C367B  8B C2                           mov eax, edx
004C367D  44 8B F1                        mov r14d, ecx
004C3680  F0 44 0F B1 36                  lock cmpxchg dword ptr [rsi], r14d
004C3685  8B C8                           mov ecx, eax
004C3687  41 3B C0                        cmp eax, r8d
004C368A  75 1F                           jne 0x1404c36ab
004C368C  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
004C3691  41 B8 04 00 00 00               mov r8d, 4
004C3697  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
004C369C  48 8B CE                        mov rcx, rsi
004C369F  E8 98 83 03 00                  call 0x1404fba3c
004C36A4  8B 0E                           mov ecx, dword ptr [rsi]
004C36A6  41 3B CE                        cmp ecx, r14d
004C36A9  74 E6                           je 0x1404c3691
004C36AB  8B C1                           mov eax, ecx
004C36AD  41 BE 00 00 00 80               mov r14d, 0x80000000
004C36B3  41 23 C6                        and eax, r14d
004C36B6  8B D1                           mov edx, ecx
004C36B8  44 8B C1                        mov r8d, ecx
004C36BB  3B C3                           cmp eax, ebx
004C36BD  75 B9                           jne 0x1404c3678
004C36BF  EB 0B                           jmp 0x1404c36cc
004C36C1  8B CF                           mov ecx, edi
004C36C3  E8 98 BD E4 FF                  call 0x14030f460
004C36C8  EB 02                           jmp 0x1404c36cc
004C36CA  F3 90                           pause
004C36CC  8B 06                           mov eax, dword ptr [rsi]
004C36CE  41 23 C6                        and eax, r14d
004C36D1  3B C3                           cmp eax, ebx
004C36D3  0F 85 48 FF FF FF               jne 0x1404c3621
004C36D9  90                              nop
004C36DA  41 8B 44 24 34                  mov eax, dword ptr [r12 + 0x34]
004C36DF  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004C36E4  83 E0 BD                        and eax, 0xffffffbd
004C36E7  0F BA E8 08                     bts eax, 8
004C36EB  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
004C36EF  E8 CC E8 E4 FF                  call 0x140311fc0
004C36F4  83 3D 25 36 B0 00 00            cmp dword ptr [rip + 0xb03625], 0
004C36FB  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
004C3700  74 0B                           je 0x1404c370d
004C3702  44 0F 20 C1                     mov rcx, cr8
004C3706  8A D3                           mov dl, bl
004C3708  E8 8B 1F 03 00                  call 0x1404f5698
004C370D  0F B6 C3                        movzx eax, bl
004C3710  44 0F 22 C0                     mov cr8, rax
004C3714  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
004C3718  48 33 CC                        xor rcx, rsp
004C371B  E8 20 8F 1E 00                  call 0x1406ac640
004C3720  4C 8D 9C 24 30 01 00 00         lea r11, [rsp + 0x130]
004C3728  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
004C372C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
004C3730  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
004C3734  49 8B E3                        mov rsp, r11
004C3737  41 5F                           pop r15
004C3739  41 5E                           pop r14
004C373B  41 5D                           pop r13
004C373D  41 5C                           pop r12
004C373F  5D                              pop rbp
004C3740  C3                              ret
004C3741  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWritePteHighLevelIsr(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_mF4;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 9729878)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 88 + 32) = result;
    v_stack_m120 = a1;
    a2 = 0;
    result = memset(v_stack_m108, a2, 200, a4);
    *(unsigned __int64 *)(v_stack_m108) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m108 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m108 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m108 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m108 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m108 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m108 + 96) = v_xmm0;
    a1 = (v_stack_m108) + (128);
    result = (a1 + 32) + (128);
    *(unsigned __int64 *)(a1 - 16) = v_xmm0;
    *(unsigned __int64 *)(a1) = v_xmm1;
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    *(unsigned __int64 *)(a1 + 32) = v_xmm1;
    *(unsigned __int64 *)(a1 + 48) = v_xmm0;
    *(unsigned __int64 *)(a1 + 64) = *(unsigned __int64 *)(result + 64);
    v_stack_m118 = v_cr8;
    result = v_cr8;
    if ((*(unsigned int *)(v_rip + 11549810)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, 200, a4);
    }
    v_rsi = (a1) + (20);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_r14 = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_r14 = (unsigned int)((v_r14) & (0x80000000ULL));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C323B;
    v_r14 = (unsigned int)((v_r14) | (*(unsigned int *)(v_rsi + 4)));
    v_stack_m134 = (unsigned int)(v_r14);
    if ((((unsigned int)((unsigned int)(0x40000000ULL))) & ((unsigned int)(v_r14))) != 0) {
        a1 = v_rsi;
        result = KeWakeAddressAll(a1, 15, 200, a4);
    }
    if (*(unsigned __int64 *)(a1 + 232) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 232);
        result = MiStackCopyHighLevel(a1, 15, 200, a4);
    }
    v_rbx = (*(unsigned __int64 *)(a1 + 8)) | (32);
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) ^ (v_rbx);
    if (((result) & (v_rdi)) != 0) goto loc_004C312B;
    result = MiWriteValidPteNewProtection(*(unsigned __int64 *)(a1), v_rbx, 200, a4);
    goto loc_004C3133;
loc_004C312B:
    a3 = 0;
    result = MiWriteValidPteNewPage(*(unsigned __int64 *)(a1), v_rbx, a3, a4);
loc_004C3133:
    *(unsigned int *)(v_stack_m120 + 16) = (unsigned int)((unsigned int)(v_stack_mF4));
    result = (unsigned int)(((unsigned int)(v_stack_mF4)) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C317B;
    v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(v_rsi + 4)));
    v_stack_m138 = (unsigned int)(v_rbx);
    if ((((unsigned int)((unsigned int)(0x40000000ULL))) & ((unsigned int)(v_rbx))) == 0) goto loc_004C33F5;
    result = KeWakeAddressAll(v_rsi, v_rbx, a3, a4);
    goto loc_004C33F5;
loc_004C317B:
    v_r14 = 0;
    v_r15 = 0;
    goto loc_004C3229;
loc_004C3186:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 11542812)) & ((unsigned int)(v_r14))) != 0) goto loc_004C3227;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11548956)))) & (64)) == 0) goto loc_004C3227;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rsi, v_rbx, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C3227;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(v_rsi, v_rbx, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C321D;
    if (((*(unsigned int *)(v_rip + 11549045)) & (0x20000ULL)) == 0) goto loc_004C321D;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C321D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbx))) goto loc_004C3229;
loc_004C31DA:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C3209;
    v_stack_m138 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C31F0:
    result = KiHaltOnAddress(v_rsi, v_stack_m138, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C31F0;
loc_004C3209:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C31DA;
    goto loc_004C3229;
loc_004C321D:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C3229;
loc_004C3227:
loc_004C3229:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3186;
    goto loc_004C33F5;
loc_004C323B:
    v_rdi = 0;
    v_r15 = 0;
    goto loc_004C32EA;
loc_004C3245:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 11542623)) & ((unsigned int)(v_rdi))) != 0) goto loc_004C32E8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11548767)))) & (64)) == 0) goto loc_004C32E8;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C32E8;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C32DF;
    if (((*(unsigned int *)(v_rip + 11548856)) & (0x20000ULL)) == 0) goto loc_004C32DF;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C32DF;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_r14))) goto loc_004C32EA;
loc_004C329F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C32CE;
    v_stack_m134 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C32B5:
    result = KiHaltOnAddress(v_rsi, v_stack_m134, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C32B5;
loc_004C32CE:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_r14))) goto loc_004C329F;
    goto loc_004C32EA;
loc_004C32DF:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C32EA;
loc_004C32E8:
loc_004C32EA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & (0x80000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_r14))) goto loc_004C3245;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C3335;
    v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(v_rsi + 4)));
    v_stack_m130 = (unsigned int)(v_rbx);
    if ((((unsigned int)((unsigned int)(0x40000000ULL))) & ((unsigned int)(v_rbx))) == 0) goto loc_004C33F0;
    result = KeWakeAddressAll(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C33F0;
loc_004C3335:
    v_r14 = 0;
    v_r15 = 0;
    goto loc_004C33E3;
loc_004C3340:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 11542370)) & ((unsigned int)(v_r14))) != 0) goto loc_004C33E1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11548514)))) & (64)) == 0) goto loc_004C33E1;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C33E1;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C33D7;
    if (((*(unsigned int *)(v_rip + 11548603)) & (0x20000ULL)) == 0) goto loc_004C33D7;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C33D7;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbx))) goto loc_004C33E3;
loc_004C3394:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C33C3;
    v_stack_m130 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C33AA:
    result = KiHaltOnAddress(v_rsi, v_stack_m130, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C33AA;
loc_004C33C3:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3394;
    goto loc_004C33E3;
loc_004C33D7:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C33E3;
loc_004C33E1:
loc_004C33E3:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3340;
loc_004C33F0:
loc_004C33F5:
    v_stack_mF4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 16 * 1)));
    result = MiFlushTbList(v_stack_m108, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C353C;
    v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(v_rsi + 4)));
    v_stack_m12C = (unsigned int)(v_rbx);
    if ((((unsigned int)((unsigned int)(0x40000000ULL))) & ((unsigned int)(v_rbx))) != 0) {
        a1 = v_rsi;
        result = KeWakeAddressAll(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    }
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C346F;
loc_004C3454:
    v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(v_rsi + 4)));
    if ((((unsigned int)((unsigned int)(0x40000000ULL))) & ((unsigned int)(v_rbx))) == 0) goto loc_004C36DA;
    result = KeWakeAddressAll(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C36DA;
loc_004C346F:
    v_rdi = 0;
    v_r15 = 0;
    goto loc_004C352A;
loc_004C347F:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 11542053)) & ((unsigned int)(v_rdi))) != 0) goto loc_004C3528;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11548197)))) & (64)) == 0) goto loc_004C3528;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C3528;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress(v_rsi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C351F;
    if (((*(unsigned int *)(v_rip + 11548282)) & (0x20000ULL)) == 0) goto loc_004C351F;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C351F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbx))) goto loc_004C352A;
loc_004C34D6:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C3509;
    v_stack_m128 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C34EF:
    result = KiHaltOnAddress(v_rsi, v_stack_m128, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C34EF;
loc_004C3509:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C34D6;
    goto loc_004C352A;
loc_004C351F:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C352A;
loc_004C3528:
loc_004C352A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C347F;
    goto loc_004C36D9;
loc_004C353C:
    v_r14 = 0;
    v_r15 = 0;
    goto loc_004C35EA;
loc_004C3547:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 11541851)) & ((unsigned int)(v_r14))) != 0) goto loc_004C35E8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11547995)))) & (64)) == 0) goto loc_004C35E8;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C35E8;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C35DE;
    if (((*(unsigned int *)(v_rip + 11548084)) & (0x20000ULL)) == 0) goto loc_004C35DE;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C35DE;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)(v_rdi)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbx))) goto loc_004C35EA;
loc_004C359B:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C35CA;
    v_stack_m12C = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C35B1:
    result = KiHaltOnAddress(v_rsi, v_stack_m12C, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C35B1;
loc_004C35CA:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C359B;
    goto loc_004C35EA;
loc_004C35DE:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C35EA;
loc_004C35E8:
loc_004C35EA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3547;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    v_rbx = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_004C3454;
    v_rdi = 0;
    v_r15 = 0;
    goto loc_004C36CC;
loc_004C3621:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 11541635)) & ((unsigned int)(v_rdi))) != 0) goto loc_004C36CA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11547779)))) & (64)) == 0) goto loc_004C36CA;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C36CA;
    v_r15 = (unsigned int)((v_r15) + 1);
    result = KeCanUseHaltOnAddress((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004C36C1;
    if (((*(unsigned int *)(v_rip + 11547864)) & (0x20000ULL)) == 0) goto loc_004C36C1;
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_004C36C1;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbx))) goto loc_004C36CC;
loc_004C3678:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) | ((unsigned int)((unsigned int)(0x40000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))))))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))))) goto loc_004C36AB;
    v_stack_m124 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004C3691:
    result = KiHaltOnAddress(v_rsi, v_stack_m124, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))) == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_004C3691;
loc_004C36AB:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3678;
    goto loc_004C36CC;
loc_004C36C1:
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    goto loc_004C36CC;
loc_004C36CA:
loc_004C36CC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx))) goto loc_004C3621;
loc_004C36D9:
loc_004C36DA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m120 + 52))) & (0xFFFFFFBDULL));
    v_stack_mF4 = (unsigned int)(result);
    result = MiFlushTbList(v_stack_m108, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    if ((*(unsigned int *)(v_rip + 11548197)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_stack_m118);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 88 + 32)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiWritePteHighLevelIsr(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m28;
    uint32_t v_stack_mF4;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x947756)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x58 + 0x20) = result;
    v_stack_m120 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, 200, a4);
    *(uint64_t *)(v_stack_m108) = v_xmm0;
    *(uint64_t *)(v_stack_m108 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m108 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m108 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m108 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m108 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m108 + 0x60) = v_xmm0;
    Arg1 = (v_stack_m108) + (128);
    result = (Arg1 + 32) + (128);
    *(uint64_t *)(arg1 - 0x10) = v_xmm0;
    *(uint64_t *)(arg1) = v_xmm1;
    *(uint64_t *)(arg1 + 0x10) = v_xmm0;
    *(uint64_t *)(arg1 + 0x20) = v_xmm1;
    *(uint64_t *)(arg1 + 0x30) = v_xmm0;
    *(uint64_t *)(arg1 + 0x40) = *(uint64_t *)(result + 0x40);
    v_stack_m118 = v_cr8;
    result = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xB03C72)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, 200, a4);
    }
    local_rsi = (Arg1) + (20);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_r14 = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_r14 = (uint32_t)((local_r14) & (0x80000000ULL));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C323B;
    local_r14 = (uint32_t)((local_r14) | (*(uint32_t *)(local_rsi + 0x4)));
    v_stack_m134 = (uint32_t)(local_r14);
    if ((((uint32_t)((uint32_t)(0x40000000ULL))) & ((uint32_t)(local_r14))) != 0) {
        Arg1 = local_rsi;
        result = KeWakeAddressAll(Arg1, 15, 200, a4);
    }
    if (*(uint64_t *)(arg1 + 0xE8) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0xE8);
        result = MiStackCopyHighLevel(Arg1, 15, 200, a4);
    }
    local_rbx = (*(uint64_t *)(arg1 + 0x8)) | (32);
    local_rdi = (*(uint64_t *)(*(uint64_t *)(arg1))) ^ (local_rbx);
    if (((result) & (local_rdi)) != 0) goto loc_004C312B;
    result = MiWriteValidPteNewProtection(*(uint64_t *)(arg1), local_rbx, 200, a4);
    goto loc_004C3133;
loc_004C312B:
    a3 = 0;
    result = MiWriteValidPteNewPage(*(uint64_t *)(arg1), local_rbx, a3, a4);
loc_004C3133:
    *(uint32_t *)(v_stack_m120 + 0x10) = (uint32_t)((uint32_t)(v_stack_mF4));
    result = (uint32_t)(((uint32_t)(v_stack_mF4)) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C317B;
    local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(local_rsi + 0x4)));
    v_stack_m138 = (uint32_t)(local_rbx);
    if ((((uint32_t)((uint32_t)(0x40000000ULL))) & ((uint32_t)(local_rbx))) == 0) goto loc_004C33F5;
    result = KeWakeAddressAll(local_rsi, local_rbx, a3, a4);
    goto loc_004C33F5;
loc_004C317B:
    local_r14 = 0;
    local_r15 = 0;
    goto loc_004C3229;
loc_004C3186:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xB0211C)) & ((uint32_t)(local_r14))) != 0) goto loc_004C3227;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0391C)))) & (64)) == 0) goto loc_004C3227;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rsi, local_rbx, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_004C3227;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(local_rsi, local_rbx, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_004C321D;
    if (((*(uint32_t *)(v_rip + 0xB03975)) & (0x20000ULL)) == 0) goto loc_004C321D;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C321D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbx))) goto loc_004C3229;
loc_004C31DA:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C3209;
    v_stack_m138 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C31F0:
    result = KiHaltOnAddress(local_rsi, v_stack_m138, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C31F0;
loc_004C3209:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C31DA;
    goto loc_004C3229;
loc_004C321D:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C3229;
loc_004C3227:
loc_004C3229:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3186;
    goto loc_004C33F5;
loc_004C323B:
    local_rdi = 0;
    local_r15 = 0;
    goto loc_004C32EA;
loc_004C3245:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xB0205F)) & ((uint32_t)(local_rdi))) != 0) goto loc_004C32E8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0385F)))) & (64)) == 0) goto loc_004C32E8;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C32E8;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C32DF;
    if (((*(uint32_t *)(v_rip + 0xB038B8)) & (0x20000ULL)) == 0) goto loc_004C32DF;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C32DF;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_r14))) goto loc_004C32EA;
loc_004C329F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C32CE;
    v_stack_m134 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C32B5:
    result = KiHaltOnAddress(local_rsi, v_stack_m134, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C32B5;
loc_004C32CE:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_r14))) goto loc_004C329F;
    goto loc_004C32EA;
loc_004C32DF:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C32EA;
loc_004C32E8:
loc_004C32EA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & (0x80000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_r14))) goto loc_004C3245;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C3335;
    local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(local_rsi + 0x4)));
    v_stack_m130 = (uint32_t)(local_rbx);
    if ((((uint32_t)((uint32_t)(0x40000000ULL))) & ((uint32_t)(local_rbx))) == 0) goto loc_004C33F0;
    result = KeWakeAddressAll(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C33F0;
loc_004C3335:
    local_r14 = 0;
    local_r15 = 0;
    goto loc_004C33E3;
loc_004C3340:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xB01F62)) & ((uint32_t)(local_r14))) != 0) goto loc_004C33E1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB03762)))) & (64)) == 0) goto loc_004C33E1;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C33E1;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C33D7;
    if (((*(uint32_t *)(v_rip + 0xB037BB)) & (0x20000ULL)) == 0) goto loc_004C33D7;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C33D7;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbx))) goto loc_004C33E3;
loc_004C3394:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C33C3;
    v_stack_m130 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C33AA:
    result = KiHaltOnAddress(local_rsi, v_stack_m130, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C33AA;
loc_004C33C3:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3394;
    goto loc_004C33E3;
loc_004C33D7:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C33E3;
loc_004C33E1:
loc_004C33E3:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3340;
loc_004C33F0:
loc_004C33F5:
    v_stack_mF4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x10 * 1)));
    result = MiFlushTbList(v_stack_m108, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C353C;
    local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(local_rsi + 0x4)));
    v_stack_m12C = (uint32_t)(local_rbx);
    if ((((uint32_t)((uint32_t)(0x40000000ULL))) & ((uint32_t)(local_rbx))) != 0) {
        Arg1 = local_rsi;
        result = KeWakeAddressAll(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    }
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) != 0) goto loc_004C346F;
loc_004C3454:
    local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(local_rsi + 0x4)));
    if ((((uint32_t)((uint32_t)(0x40000000ULL))) & ((uint32_t)(local_rbx))) == 0) goto loc_004C36DA;
    result = KeWakeAddressAll(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C36DA;
loc_004C346F:
    local_rdi = 0;
    local_r15 = 0;
    goto loc_004C352A;
loc_004C347F:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xB01E25)) & ((uint32_t)(local_rdi))) != 0) goto loc_004C3528;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB03625)))) & (64)) == 0) goto loc_004C3528;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C3528;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress(local_rsi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C351F;
    if (((*(uint32_t *)(v_rip + 0xB0367A)) & (0x20000ULL)) == 0) goto loc_004C351F;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C351F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbx))) goto loc_004C352A;
loc_004C34D6:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C3509;
    v_stack_m128 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C34EF:
    result = KiHaltOnAddress(local_rsi, v_stack_m128, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C34EF;
loc_004C3509:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C34D6;
    goto loc_004C352A;
loc_004C351F:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C352A;
loc_004C3528:
loc_004C352A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C347F;
    goto loc_004C36D9;
loc_004C353C:
    local_r14 = 0;
    local_r15 = 0;
    goto loc_004C35EA;
loc_004C3547:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xB01D5B)) & ((uint32_t)(local_r14))) != 0) goto loc_004C35E8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0355B)))) & (64)) == 0) goto loc_004C35E8;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C35E8;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C35DE;
    if (((*(uint32_t *)(v_rip + 0xB035B4)) & (0x20000ULL)) == 0) goto loc_004C35DE;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C35DE;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)(local_rdi)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbx))) goto loc_004C35EA;
loc_004C359B:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C35CA;
    v_stack_m12C = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C35B1:
    result = KiHaltOnAddress(local_rsi, v_stack_m12C, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C35B1;
loc_004C35CA:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C359B;
    goto loc_004C35EA;
loc_004C35DE:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C35EA;
loc_004C35E8:
loc_004C35EA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3547;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    local_rbx = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)(result)) & (0x3FFFFFFFULL)) == 0) goto loc_004C3454;
    local_rdi = 0;
    local_r15 = 0;
    goto loc_004C36CC;
loc_004C3621:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xB01C83)) & ((uint32_t)(local_rdi))) != 0) goto loc_004C36CA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB03483)))) & (64)) == 0) goto loc_004C36CA;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C36CA;
    local_r15 = (uint32_t)((local_r15) + 1);
    result = KeCanUseHaltOnAddress((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((uint8_t)(result) == 0) goto loc_004C36C1;
    if (((*(uint32_t *)(v_rip + 0xB034D8)) & (0x20000ULL)) == 0) goto loc_004C36C1;
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_004C36C1;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbx))) goto loc_004C36CC;
loc_004C3678:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) | ((uint32_t)((uint32_t)(0x40000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))))))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))))) goto loc_004C36AB;
    v_stack_m124 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004C3691:
    result = KiHaltOnAddress(local_rsi, v_stack_m124, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))) == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_004C3691;
loc_004C36AB:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3678;
    goto loc_004C36CC;
loc_004C36C1:
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    goto loc_004C36CC;
loc_004C36CA:
loc_004C36CC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx))) goto loc_004C3621;
loc_004C36D9:
loc_004C36DA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x34))) & (0xFFFFFFBDULL));
    v_stack_mF4 = (uint32_t)(result);
    result = MiFlushTbList(v_stack_m108, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    if ((*(uint32_t *)(v_rip + 0xB03625)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_stack_m118);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x58 + 0x20)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |
| `Arg1` | `+ 0xE8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C2FC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
