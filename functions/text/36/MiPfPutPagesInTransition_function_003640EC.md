# MiPfPutPagesInTransition

- RVA: `0x003640EC`–`0x00364BB1` (길이 `2,757` bytes)
- VA: `0x00000001403640EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079EBC`
- 디코드: `664`개 명령, `2,757/2,757` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003641AF` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x003641F3` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0036430E` → [MiGetInPageSupportBlock](MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)
- `0x00364331` → [MiSetInPagePriority](MiSetInPagePriority_function_0036A9A4.md) (function, `0x0036A9A4`)
- `0x0036439A` → [MiLockLeafPage](MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00364470` → [MiUseSlabAllocator](MiUseSlabAllocator_function_00365C68.md) (function, `0x00365C68`)
- `0x0036448E` → [MiUnlinkPageChainHead](MiUnlinkPageChainHead_function_00365C40.md) (function, `0x00365C40`)
- `0x00364541` → [MiInitializeReadInProgressPfn](../2B/MiInitializeReadInProgressPfn_function_002B6990.md) (function, `0x002B6990`)
- `0x00364555` → [MiReferenceControlAreaPfn](MiReferenceControlAreaPfn_function_00364084.md) (function, `0x00364084`)
- `0x003645D6` → [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) (function, `0x00320E10`)
- `0x0036463A` → [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) (function, `0x00318178`)
- `0x0036466B` → [MiPrefetchPagesViable](../45/MiPrefetchPagesViable_function_0045A644.md) (function, `0x0045A644`)
- `0x003646A7` → [MiReturnPfnReferenceCountAtDpc](MiReturnPfnReferenceCountAtDpc_function_00364010.md) (function, `0x00364010`)
- `0x00364707` → [MiUpdatePfnPriority](../2B/MiUpdatePfnPriority_function_002B8570.md) (function, `0x002B8570`)
- `0x00364748` → [MiPrefetchPagesViable](../45/MiPrefetchPagesViable_function_0045A644.md) (function, `0x0045A644`)
- `0x0036477B` → [MiGetPageForHeader](../2A/MiGetPageForHeader_function_002AC120.md) (function, `0x002AC120`)
- `0x0036481B` → [MiReturnPfnReferenceCountAtDpc](MiReturnPfnReferenceCountAtDpc_function_00364010.md) (function, `0x00364010`)
- `0x0036482E` → [MiReduceMdl](../44/MiReduceMdl_function_0044BA80.md) (function, `0x0044BA80`)
- `0x00364864` → [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) (function, `0x0093D600`)
- `0x00364871` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x003648B2` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003648BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00364A5C` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00364AAC` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x00364ABC` → [MiPfnZeroingNeeded](../29/MiPfnZeroingNeeded_function_0029FA80.md) (function, `0x0029FA80`)
- `0x00364ADD` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00364AF6` → [MiRefillPurgedExtents](../47/MiRefillPurgedExtents_function_00479988.md) (function, `0x00479988`)
- `0x00364B28` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x00364B3B` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00364B57` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00364B6A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00364B7D` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)

### Direct callers
- [MmPrefetchPagesEx](../../page/93/MmPrefetchPagesEx_function_0093C9A0.md) at `0x0093CBCD`
- [MmPrefetchForCacheManager](../../page/93/MmPrefetchForCacheManager_function_0093D714.md) at `0x0093D7E4`
- [MiPrefetchControlArea](../../page/93/MiPrefetchControlArea_function_0093E830.md) at `0x0093E948`

### Static image references
- `0x00364157` → RVA `0x00E30088` (`.data`; read)
- `0x0036422A` → RVA `0x00E37438` (`.data`; read)
- `0x003643C1` → RVA `0x00E2DC80` (`.data`; read)
- `0x00364A2B` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00364B49` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00364864` → [MiFreeReadListPages](../../page/93/MiFreeReadListPages_function_0093D600.md) (`.text` → `PAGE`)
  - `0x003648BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00364509` → [sub_006E313A + 0xB2](../6E/Unknown_function_006E313A.md) (`tail-transfer`)
  - `0x00364675` → [sub_006E313A](../6E/Unknown_function_006E313A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003640EC  48 8B C4                        mov rax, rsp
003640EF  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
003640F3  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
003640F7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
003640FB  48 89 48 08                     mov qword ptr [rax + 8], rcx
003640FF  55                              push rbp
00364100  53                              push rbx
00364101  56                              push rsi
00364102  57                              push rdi
00364103  41 54                           push r12
00364105  41 55                           push r13
00364107  41 56                           push r14
00364109  41 57                           push r15
0036410B  48 8D 68 98                     lea rbp, [rax - 0x68]
0036410F  48 81 EC 28 01 00 00            sub rsp, 0x128
00364116  44 8B 89 B8 00 00 00            mov r9d, dword ptr [rcx + 0xb8]
0036411D  33 C0                           xor eax, eax
0036411F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00364124  4C 8B E1                        mov r12, rcx
00364127  8B 81 BC 00 00 00               mov eax, dword ptr [rcx + 0xbc]
0036412D  45 33 D2                        xor r10d, r10d
00364130  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00364133  0F 57 C0                        xorps xmm0, xmm0
00364136  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0036413F  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00364143  4C 89 55 C0                     mov qword ptr [rbp - 0x40], r10
00364147  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0036414C  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
00364153  0F B7 4A 3C                     movzx ecx, word ptr [rdx + 0x3c]
00364157  48 8B 05 2A BF AC 00            mov rax, qword ptr [rip + 0xacbf2a]
0036415E  81 E1 FF 03 00 00               and ecx, 0x3ff
00364164  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
00364169  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0036416D  44 89 4C 24 7C                  mov dword ptr [rsp + 0x7c], r9d
00364172  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00364176  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0036417F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00364184  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
00364187  83 E0 08                        and eax, 8
0036418A  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0036418F  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00364192  41 8B 84 24 C0 00 00 00         mov eax, dword ptr [r12 + 0xc0]
0036419A  FF C0                           inc eax
0036419C  4C 89 55 E0                     mov qword ptr [rbp - 0x20], r10
003641A0  89 45 98                        mov dword ptr [rbp - 0x68], eax
003641A3  C6 85 80 00 00 00 11            mov byte ptr [rbp + 0x80], 0x11
003641AA  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
003641AF  E8 7C F7 FD FF                  call 0x140343930
003641B4  49 8B 5C 24 08                  mov rbx, qword ptr [r12 + 8]
003641B9  41 8D 52 03                     lea edx, [r10 + 3]
003641BD  41 8A C9                        mov cl, r9b
003641C0  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
003641C5  80 E1 07                        and cl, 7
003641C8  89 45 A0                        mov dword ptr [rbp - 0x60], eax
003641CB  80 C9 18                        or cl, 0x18
003641CE  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
003641D2  8B 5B 38                        mov ebx, dword ptr [rbx + 0x38]
003641D5  4C 8D 4D F0                     lea r9, [rbp - 0x10]
003641D9  88 4C 24 3C                     mov byte ptr [rsp + 0x3c], cl
003641DD  45 8B FA                        mov r15d, r10d
003641E0  C1 EB 14                        shr ebx, 0x14
003641E3  48 8D 8F 00 04 00 00            lea rcx, [rdi + 0x400]
003641EA  83 E3 7F                        and ebx, 0x7f
003641ED  44 8B C3                        mov r8d, ebx
003641F0  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
003641F3  E8 18 C2 FB FF                  call 0x140320410
003641F8  8B 75 F8                        mov esi, dword ptr [rbp - 8]
003641FB  49 8D 84 24 E0 00 00 00         lea rax, [r12 + 0xe0]
00364203  4C 8B 28                        mov r13, qword ptr [rax]
00364206  C1 EE 09                        shr esi, 9
00364209  83 E6 3F                        and esi, 0x3f
0036420C  48 89 45 00                     mov qword ptr [rbp], rax
00364210  89 75 9C                        mov dword ptr [rbp - 0x64], esi
00364213  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00364218  4C 3B E8                        cmp r13, rax
0036421B  0F 84 40 06 00 00               je 0x140364861
00364221  44 8B 74 24 3C                  mov r14d, dword ptr [rsp + 0x3c]
00364226  83 7D A0 02                     cmp dword ptr [rbp - 0x60], 2
0036422A  48 8D 15 07 32 AD 00            lea rdx, [rip + 0xad3207]
00364231  4C 89 6D 10                     mov qword ptr [rbp + 0x10], r13
00364235  0F 8C 52 06 00 00               jl 0x14036488d
0036423B  41 8B 84 24 D0 00 00 00         mov eax, dword ptr [r12 + 0xd0]
00364243  B9 01 00 00 00                  mov ecx, 1
00364248  84 C1                           test cl, al
0036424A  74 12                           je 0x14036425e
0036424C  41 8B 85 C0 00 00 00            mov eax, dword ptr [r13 + 0xc0]
00364253  0F BA E8 07                     bts eax, 7
00364257  41 89 85 C0 00 00 00            mov dword ptr [r13 + 0xc0], eax
0036425E  49 8B BD F0 00 00 00            mov rdi, qword ptr [r13 + 0xf0]
00364265  45 33 DB                        xor r11d, r11d
00364268  4D 8B A5 C8 00 00 00            mov r12, qword ptr [r13 + 0xc8]
0036426F  45 8B C3                        mov r8d, r11d
00364272  49 83 C4 08                     add r12, 8
00364276  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
0036427A  4C 89 65 08                     mov qword ptr [rbp + 8], r12
0036427E  48 8B 07                        mov rax, qword ptr [rdi]
00364281  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00364285  49 89 85 F0 00 00 00            mov qword ptr [r13 + 0xf0], rax
0036428C  48 8B 07                        mov rax, qword ptr [rdi]
0036428F  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00364293  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00364297  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
0036429E  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003642A2  8B 48 2C                        mov ecx, dword ptr [rax + 0x2c]
003642A5  4C 8D 48 30                     lea r9, [rax + 0x30]
003642A9  03 48 20                        add ecx, dword ptr [rax + 0x20]
003642AC  44 8B 50 28                     mov r10d, dword ptr [rax + 0x28]
003642B0  81 E1 FF 0F 00 00               and ecx, 0xfff
003642B6  49 81 C2 FF 0F 00 00            add r10, 0xfff
003642BD  4C 03 D1                        add r10, rcx
003642C0  49 C1 EA 0C                     shr r10, 0xc
003642C4  49 83 FA 02                     cmp r10, 2
003642C8  0F 83 E0 03 00 00               jae 0x1403646ae
003642CE  41 8B C0                        mov eax, r8d
003642D1  49 3B C2                        cmp rax, r10
003642D4  73 22                           jae 0x1403642f8
003642D6  41 BB 01 00 00 00               mov r11d, 1
003642DC  48 8B 05 55 31 AD 00            mov rax, qword ptr [rip + 0xad3155]
003642E3  45 03 C3                        add r8d, r11d
003642E6  49 89 01                        mov qword ptr [r9], rax
003642E9  4D 8D 49 08                     lea r9, [r9 + 8]
003642ED  41 8B C0                        mov eax, r8d
003642F0  49 3B C2                        cmp rax, r10
003642F3  72 E7                           jb 0x1403642dc
003642F5  45 33 DB                        xor r11d, r11d
003642F8  44 89 5D 84                     mov dword ptr [rbp - 0x7c], r11d
003642FC  4C 89 5D B0                     mov qword ptr [rbp - 0x50], r11
00364300  4D 85 FF                        test r15, r15
00364303  75 31                           jne 0x140364336
00364305  48 8B 95 90 00 00 00            mov rdx, qword ptr [rbp + 0x90]
0036430C  33 C9                           xor ecx, ecx
0036430E  E8 ED E1 FF FF                  call 0x140362500
00364313  45 33 DB                        xor r11d, r11d
00364316  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0036431A  48 85 C0                        test rax, rax
0036431D  74 17                           je 0x140364336
0036431F  8B 55 A4                        mov edx, dword ptr [rbp - 0x5c]
00364322  48 8B C8                        mov rcx, rax
00364325  44 8B 44 24 7C                  mov r8d, dword ptr [rsp + 0x7c]
0036432A  4C 89 98 F8 00 00 00            mov qword ptr [rax + 0xf8], r11
00364331  E8 6E 66 00 00                  call 0x14036a9a4
00364336  49 3B FC                        cmp rdi, r12
00364339  0F 83 0A 07 00 00               jae 0x140364a49
0036433F  4C 8B 27                        mov r12, qword ptr [rdi]
00364342  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00364347  49 83 E4 FC                     and r12, 0xfffffffffffffffc
0036434B  49 8B FC                        mov rdi, r12
0036434E  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
00364352  48 C1 EF 09                     shr rdi, 9
00364356  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
0036435A  48 85 C9                        test rcx, rcx
0036435D  0F 84 45 02 00 00               je 0x1403645a8
00364363  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0036436D  48 8B D7                        mov rdx, rdi
00364370  48 23 D0                        and rdx, rax
00364373  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0036437D  48 8B C0                        mov rax, rax
00364380  48 03 D0                        add rdx, rax
00364383  48 39 55 E0                     cmp qword ptr [rbp - 0x20], rdx
00364387  0F 85 EA 07 00 00               jne 0x140364b77
0036438D  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00364392  BA 02 00 00 00                  mov edx, 2
00364397  49 8B CC                        mov rcx, r12
0036439A  E8 21 15 00 00                  call 0x1403658c0
0036439F  49 8B 3C 24                     mov rdi, qword ptr [r12]
003643A3  45 33 DB                        xor r11d, r11d
003643A6  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
003643AA  4C 8B F8                        mov r15, rax
003643AD  48 85 C0                        test rax, rax
003643B0  0F 85 47 03 00 00               jne 0x1403646fd
003643B6  48 0F BA E7 0A                  bt rdi, 0xa
003643BB  0F 83 0C 05 00 00               jae 0x1403648cd
003643C1  48 8B 05 B8 98 AC 00            mov rax, qword ptr [rip + 0xac98b8]
003643C8  4C 8B FF                        mov r15, rdi
003643CB  48 85 C0                        test rax, rax
003643CE  74 13                           je 0x1403643e3
003643D0  40 F6 C7 10                     test dil, 0x10
003643D4  0F 85 52 02 00 00               jne 0x14036462c
003643DA  4C 8B F8                        mov r15, rax
003643DD  49 F7 D7                        not r15
003643E0  4C 23 FF                        and r15, rdi
003643E3  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
003643E7  B9 01 00 00 00                  mov ecx, 1
003643EC  49 C1 FF 10                     sar r15, 0x10
003643F0  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
003643F4  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
003643F8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
003643FC  44 8A 40 3E                     mov r8b, byte ptr [rax + 0x3e]
00364400  41 80 E0 0C                     and r8b, 0xc
00364404  41 80 F8 04                     cmp r8b, 4
00364408  0F 84 C4 06 00 00               je 0x140364ad2
0036440E  41 80 F8 08                     cmp r8b, 8
00364412  0F 84 7B 01 00 00               je 0x140364593
00364418  33 C0                           xor eax, eax
0036441A  0F 57 C0                        xorps xmm0, xmm0
0036441D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00364422  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00364427  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
0036442B  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00364430  48 85 C0                        test rax, rax
00364433  0F 84 AC 01 00 00               je 0x1403645e5
00364439  44 39 5D D0                     cmp dword ptr [rbp - 0x30], r11d
0036443D  0F 85 E0 02 00 00               jne 0x140364723
00364443  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00364448  B8 01 00 00 00                  mov eax, 1
0036444D  44 89 5D 80                     mov dword ptr [rbp - 0x80], r11d
00364451  39 44 24 78                     cmp dword ptr [rsp + 0x78], eax
00364455  75 29                           jne 0x140364480
00364457  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0036445B  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00364460  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00364465  44 8B CE                        mov r9d, esi
00364468  4C 8B C7                        mov r8, rdi
0036446B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00364470  E8 F3 17 00 00                  call 0x140365c68
00364475  45 33 DB                        xor r11d, r11d
00364478  85 C0                           test eax, eax
0036447A  0F 85 A7 04 00 00               jne 0x140364927
00364480  4C 8B 65 70                     mov r12, qword ptr [rbp + 0x70]
00364484  49 83 C4 28                     add r12, 0x28
00364488  4D 8B EC                        mov r13, r12
0036448B  49 8B CC                        mov rcx, r12
0036448E  E8 AD 17 00 00                  call 0x140365c40
00364493  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00364497  4C 8B C0                        mov r8, rax
0036449A  48 85 C0                        test rax, rax
0036449D  0F 84 AF 01 00 00               je 0x140364652
003644A3  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
003644AD  49 8B C9                        mov rcx, r9
003644B0  48 8B D0                        mov rdx, rax
003644B3  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
003644B8  48 2B D1                        sub rdx, rcx
003644BB  48 B9 AB AA AA AA AA AA AA AA   movabs rcx, 0xaaaaaaaaaaaaaaab
003644C5  48 C1 FA 04                     sar rdx, 4
003644C9  48 0F AF D1                     imul rdx, rcx
003644CD  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
003644D2  48 85 C0                        test rax, rax
003644D5  0F 85 7B 04 00 00               jne 0x140364956
003644DB  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003644DF  41 BC 01 00 00 00               mov r12d, 1
003644E5  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
003644EA  45 3B CC                        cmp r9d, r12d
003644ED  4C 8B 7D E8                     mov r15, qword ptr [rbp - 0x18]
003644F1  49 0F 44 C7                     cmove rax, r15
003644F5  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
003644F9  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
003644FD  44 84 20                        test byte ptr [rax], r12b
00364500  0F 85 B0 05 00 00               jne 0x140364ab6
00364506  45 3B CC                        cmp r9d, r12d
00364509  0F 85 DD EC 37 00               jne 0x1406e31ec
0036450F  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00364514  4D 39 9D F8 00 00 00            cmp qword ptr [r13 + 0xf8], r11
0036451B  75 07                           jne 0x140364524
0036451D  4D 89 85 F8 00 00 00            mov qword ptr [r13 + 0xf8], r8
00364524  44 01 65 84                     add dword ptr [rbp - 0x7c], r12d
00364528  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
0036452D  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00364532  4D 8B CF                        mov r9, r15
00364535  45 8B C4                        mov r8d, r12d
00364538  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0036453D  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00364541  E8 4A 24 F5 FF                  call 0x1402b6990
00364546  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0036454A  45 8B C4                        mov r8d, r12d
0036454D  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00364551  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00364555  E8 2A FB FF FF                  call 0x140364084
0036455A  4C 2B 7D B8                     sub r15, qword ptr [rbp - 0x48]
0036455E  45 33 DB                        xor r11d, r11d
00364561  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00364565  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0036456A  49 C1 FF 03                     sar r15, 3
0036456E  4A 89 44 F9 30                  mov qword ptr [rcx + r15*8 + 0x30], rax
00364573  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00364578  4D 39 9D A0 00 00 00            cmp qword ptr [r13 + 0xa0], r11
0036457F  0F 84 B0 00 00 00               je 0x140364635
00364585  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
00364589  44 39 5D 80                     cmp dword ptr [rbp - 0x80], r11d
0036458D  0F 85 78 05 00 00               jne 0x140364b0b
00364593  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
00364597  4C 8B 65 08                     mov r12, qword ptr [rbp + 8]
0036459B  48 83 C7 08                     add rdi, 8
0036459F  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
003645A3  E9 8E FD FF FF                  jmp 0x140364336
003645A8  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003645B2  48 8B CF                        mov rcx, rdi
003645B5  48 23 C8                        and rcx, rax
003645B8  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003645C2  48 8B C0                        mov rax, rax
003645C5  48 03 C8                        add rcx, rax
003645C8  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
003645CF  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
003645D3  49 8B CC                        mov rcx, r12
003645D6  E8 35 C8 FB FF                  call 0x140320e10
003645DB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003645E0  E9 AD FD FF FF                  jmp 0x140364392
003645E5  49 8B CC                        mov rcx, r12
003645E8  48 2B 4D B8                     sub rcx, qword ptr [rbp - 0x48]
003645EC  48 C1 F9 03                     sar rcx, 3
003645F0  48 85 C9                        test rcx, rcx
003645F3  0F 84 4A FE FF FF               je 0x140364443
003645F9  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
003645FD  0F B7 C1                        movzx eax, cx
00364600  66 F7 D8                        neg ax
00364603  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
00364607  66 C1 E0 03                     shl ax, 3
0036460B  66 01 42 08                     add word ptr [rdx + 8], ax
0036460F  69 C1 00 F0 FF FF               imul eax, ecx, 0xfffff000
00364615  48 C1 E1 0C                     shl rcx, 0xc
00364619  01 42 28                        add dword ptr [rdx + 0x28], eax
0036461C  49 01 4D 60                     add qword ptr [r13 + 0x60], rcx
00364620  4D 89 A5 F0 00 00 00            mov qword ptr [r13 + 0xf0], r12
00364627  E9 17 FE FF FF                  jmp 0x140364443
0036462C  49 83 E7 EF                     and r15, 0xffffffffffffffef
00364630  E9 AE FD FF FF                  jmp 0x1403643e3
00364635  33 D2                           xor edx, edx
00364637  49 8B CF                        mov rcx, r15
0036463A  E8 39 3B FB FF                  call 0x140318178
0036463F  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
00364643  45 33 DB                        xor r11d, r11d
00364646  4D 89 BD A0 00 00 00            mov qword ptr [r13 + 0xa0], r15
0036464D  E9 37 FF FF FF                  jmp 0x140364589
00364652  44 8B 45 98                     mov r8d, dword ptr [rbp - 0x68]
00364656  B8 01 00 00 00                  mov eax, 1
0036465B  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
0036465F  44 8B C8                        mov r9d, eax
00364662  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00364667  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0036466B  E8 D4 5F 0F 00                  call 0x14045a644
00364670  45 33 DB                        xor r11d, r11d
00364673  85 C0                           test eax, eax
00364675  0F 85 BF EA 37 00               jne 0x1406e313a
0036467B  49 8B CF                        mov rcx, r15
0036467E  4D 85 FF                        test r15, r15
00364681  0F 84 20 05 00 00               je 0x140364ba7
00364687  4D 8B 3F                        mov r15, qword ptr [r15]
0036468A  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0036468F  48 FF C8                        dec rax
00364692  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00364697  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0036469C  48 F7 D8                        neg rax
0036469F  48 1B C0                        sbb rax, rax
003646A2  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
003646A7  E8 64 F9 FF FF                  call 0x140364010
003646AC  EB CD                           jmp 0x14036467b
003646AE  4C 8B 1D 83 2D AD 00            mov r11, qword ptr [rip + 0xad2d83]
003646B5  41 8D 42 FF                     lea eax, [r10 - 1]
003646B9  49 8D 04 C1                     lea rax, [r9 + rax*8]
003646BD  4C 3B CA                        cmp r9, rdx
003646C0  77 05                           ja 0x1403646c7
003646C2  48 3B C2                        cmp rax, rdx
003646C5  73 2E                           jae 0x1403646f5
003646C7  49 8B D2                        mov rdx, r10
003646CA  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
003646CE  41 83 C0 02                     add r8d, 2
003646D2  41 8B C8                        mov ecx, r8d
003646D5  48 3B CA                        cmp rcx, rdx
003646D8  72 F4                           jb 0x1403646ce
003646DA  48 C1 E2 03                     shl rdx, 3
003646DE  49 8B F9                        mov rdi, r9
003646E1  48 8B CA                        mov rcx, rdx
003646E4  49 8B C3                        mov rax, r11
003646E7  48 C1 E9 03                     shr rcx, 3
003646EB  F3 48 AB                        rep stosq qword ptr [rdi], rax
003646EE  4C 03 CA                        add r9, rdx
003646F1  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
003646F5  45 33 DB                        xor r11d, r11d
003646F8  E9 D1 FB FF FF                  jmp 0x1403642ce
003646FD  8B 54 24 7C                     mov edx, dword ptr [rsp + 0x7c]
00364701  45 33 C0                        xor r8d, r8d
00364704  49 8B CF                        mov rcx, r15
00364707  E8 64 3E F5 FF                  call 0x1402b8570
0036470C  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00364716  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
0036471B  45 33 DB                        xor r11d, r11d
0036471E  E9 70 FE FF FF                  jmp 0x140364593
00364723  4C 2B E0                        sub r12, rax
00364726  49 C1 FC 03                     sar r12, 3
0036472A  4C 2B E1                        sub r12, rcx
0036472D  0F 84 10 FD FF FF               je 0x140364443
00364733  44 8B 45 98                     mov r8d, dword ptr [rbp - 0x68]
00364737  4D 8B CC                        mov r9, r12
0036473A  48 8B 55 78                     mov rdx, qword ptr [rbp + 0x78]
0036473E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00364743  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
00364748  E8 F7 5E 0F 00                  call 0x14045a644
0036474D  45 33 DB                        xor r11d, r11d
00364750  85 C0                           test eax, eax
00364752  0F 84 F1 02 00 00               je 0x140364a49
00364758  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0036475D  41 8D 53 01                     lea edx, [r11 + 1]
00364761  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00364766  45 8B F3                        mov r14d, r11d
00364769  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0036476E  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00364773  44 8B C2                        mov r8d, edx
00364776  48 8B CF                        mov rcx, rdi
00364779  8B D3                           mov edx, ebx
0036477B  E8 A0 79 F4 FF                  call 0x1402ac120
00364780  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00364785  48 83 F8 FF                     cmp rax, -1
00364789  0F 84 F8 03 00 00               je 0x140364b87
0036478F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00364793  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036479D  48 C1 E1 04                     shl rcx, 4
003647A1  48 8B C0                        mov rax, rax
003647A4  48 03 C8                        add rcx, rax
003647A7  45 33 DB                        xor r11d, r11d
003647AA  4D 85 ED                        test r13, r13
003647AD  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003647B2  4C 0F 44 E9                     cmove r13, rcx
003647B6  41 8D 53 01                     lea edx, [r11 + 1]
003647BA  4C 89 39                        mov qword ptr [rcx], r15
003647BD  48 03 F2                        add rsi, rdx
003647C0  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
003647C5  4C 03 F2                        add r14, rdx
003647C8  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
003647CD  4C 8B F9                        mov r15, rcx
003647D0  4D 3B F4                        cmp r14, r12
003647D3  75 9E                           jne 0x140364773
003647D5  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
003647D9  4D 3B F4                        cmp r14, r12
003647DC  44 8B 74 24 3C                  mov r14d, dword ptr [rsp + 0x3c]
003647E1  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
003647E6  8B 75 9C                        mov esi, dword ptr [rbp - 0x64]
003647E9  0F 84 59 FC FF FF               je 0x140364448
003647EF  49 8B CF                        mov rcx, r15
003647F2  4D 85 FF                        test r15, r15
003647F5  0F 84 AC 03 00 00               je 0x140364ba7
003647FB  4D 8B 3F                        mov r15, qword ptr [r15]
003647FE  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00364803  48 2B C2                        sub rax, rdx
00364806  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
0036480B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00364810  48 F7 D8                        neg rax
00364813  48 1B C0                        sbb rax, rax
00364816  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
0036481B  E8 F0 F7 FF FF                  call 0x140364010
00364820  BA 01 00 00 00                  mov edx, 1
00364825  EB C8                           jmp 0x1403647ef
00364827  4C 8B 7D C8                     mov r15, qword ptr [rbp - 0x38]
0036482B  49 8B CF                        mov rcx, r15
0036482E  E8 4D 72 0E 00                  call 0x14044ba80
00364833  49 8D BD 10 01 00 00            lea rdi, [r13 + 0x110]
0036483A  4C 3B FF                        cmp r15, rdi
0036483D  75 5E                           jne 0x14036489d
0036483F  4D 8B 6D 00                     mov r13, qword ptr [r13]
00364843  4C 8B 65 70                     mov r12, qword ptr [rbp + 0x70]
00364847  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0036484C  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
00364850  49 8D 84 24 E0 00 00 00         lea rax, [r12 + 0xe0]
00364858  4C 3B E8                        cmp r13, rax
0036485B  0F 85 C5 F9 FF FF               jne 0x140364226
00364861  49 8B CC                        mov rcx, r12
00364864  E8 97 8D 5D 00                  call 0x14093d600
00364869  4D 85 FF                        test r15, r15
0036486C  74 08                           je 0x140364876
0036486E  49 8B CF                        mov rcx, r15
00364871  E8 8A 10 F5 FF                  call 0x1402b5900
00364876  33 C0                           xor eax, eax
00364878  48 81 C4 28 01 00 00            add rsp, 0x128
0036487F  41 5F                           pop r15
00364881  41 5E                           pop r14
00364883  41 5D                           pop r13
00364885  41 5C                           pop r12
00364887  5F                              pop rdi
00364888  5E                              pop rsi
00364889  5B                              pop rbx
0036488A  5D                              pop rbp
0036488B  C3                              ret
0036488C  CC                              int3
0036488D  41 8B 85 C0 00 00 00            mov eax, dword ptr [r13 + 0xc0]
00364894  0F BA E8 09                     bts eax, 9
00364898  E9 BA F9 FF FF                  jmp 0x140364257
0036489D  41 81 7F 28 00 00 01 00         cmp dword ptr [r15 + 0x28], 0x10000
003648A5  77 98                           ja 0x14036483f
003648A7  4D 0F BF 47 08                  movsx r8, word ptr [r15 + 8]
003648AC  49 8B D7                        mov rdx, r15
003648AF  48 8B CF                        mov rcx, rdi
003648B2  E8 89 1F 36 00                  call 0x1406c6840
003648B7  33 D2                           xor edx, edx
003648B9  49 8B CF                        mov rcx, r15
003648BC  E8 AF DF 81 00                  call 0x140b82870
003648C1  49 89 BD 00 01 00 00            mov qword ptr [r13 + 0x100], rdi
003648C8  E9 72 FF FF FF                  jmp 0x14036483f
003648CD  B9 01 00 00 00                  mov ecx, 1
003648D2  C7 44 24 78 02 00 00 00         mov dword ptr [rsp + 0x78], 2
003648DA  40 84 F9                        test cl, dil
003648DD  75 39                           jne 0x140364918
003648DF  48 8B 0D 9A 93 AC 00            mov rcx, qword ptr [rip + 0xac939a]
003648E6  48 8B C7                        mov rax, rdi
003648E9  48 85 C9                        test rcx, rcx
003648EC  74 0F                           je 0x1403648fd
003648EE  40 F6 C7 10                     test dil, 0x10
003648F2  75 5C                           jne 0x140364950
003648F4  48 8B C1                        mov rax, rcx
003648F7  48 F7 D0                        not rax
003648FA  48 23 C7                        and rax, rdi
003648FD  48 0F BA E0 0A                  bt rax, 0xa
00364902  72 0F                           jb 0x140364913
00364904  48 0F BA E0 0B                  bt rax, 0xb
00364909  72 08                           jb 0x140364913
0036490B  A8 04                           test al, 4
0036490D  0F 84 80 FC FF FF               je 0x140364593
00364913  B9 01 00 00 00                  mov ecx, 1
00364918  4C 39 5D 90                     cmp qword ptr [rbp - 0x70], r11
0036491C  0F 84 71 FC FF FF               je 0x140364593
00364922  E9 F1 FA FF FF                  jmp 0x140364418
00364927  83 7C 24 38 04                  cmp dword ptr [rsp + 0x38], 4
0036492C  0F 87 4E FB FF FF               ja 0x140364480
00364932  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00364936  4C 8D 24 40                     lea r12, [rax + rax*2]
0036493A  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0036493E  4D 8D 64 24 08                  lea r12, [r12 + 8]
00364943  4E 8D 24 E0                     lea r12, [rax + r12*8]
00364947  4C 8D 68 28                     lea r13, [rax + 0x28]
0036494B  E9 3B FB FF FF                  jmp 0x14036448b
00364950  48 83 E0 EF                     and rax, 0xffffffffffffffef
00364954  EB A7                           jmp 0x1403648fd
00364956  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0036495A  BE 01 00 00 00                  mov esi, 1
0036495F  4C 2B 6D B8                     sub r13, qword ptr [rbp - 0x48]
00364963  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
0036496D  4C 8B 65 C8                     mov r12, qword ptr [rbp - 0x38]
00364971  49 C1 FD 03                     sar r13, 3
00364975  49 83 C4 38                     add r12, 0x38
00364979  49 BE 00 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000000
00364983  4F 8D 2C EC                     lea r13, [r12 + r13*8]
00364987  4D 85 FF                        test r15, r15
0036498A  0F 84 03 02 00 00               je 0x140364b93
00364990  49 8B 07                        mov rax, qword ptr [r15]
00364993  45 8B E3                        mov r12d, r11d
00364996  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0036499B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
003649A0  48 2B C6                        sub rax, rsi
003649A3  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003649A8  48 F7 D8                        neg rax
003649AB  48 1B C0                        sbb rax, rax
003649AE  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
003649B3  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
003649BA  72 6C                           jb 0x140364a28
003649BC  49 C7 47 08 FD FF FF FF         mov qword ptr [r15 + 8], 0xfffffffffffffffd
003649C4  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
003649C8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003649CC  C1 E8 10                        shr eax, 0x10
003649CF  0C 07                           or al, 7
003649D1  88 44 24 42                     mov byte ptr [rsp + 0x42], al
003649D5  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
003649D9  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
003649DD  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
003649E1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003649E5  C1 E8 10                        shr eax, 0x10
003649E8  0C 20                           or al, 0x20
003649EA  88 44 24 42                     mov byte ptr [rsp + 0x42], al
003649EE  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
003649F2  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
003649F6  4D 89 1F                        mov qword ptr [r15], r11
003649F9  F0 49 21 5F 18                  lock and qword ptr [r15 + 0x18], rbx
003649FE  49 8B C6                        mov rax, r14
00364A01  4C 2B F8                        sub r15, rax
00364A04  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00364A0E  49 C1 FF 04                     sar r15, 4
00364A12  4C 0F AF F8                     imul r15, rax
00364A16  4D 89 7D 00                     mov qword ptr [r13], r15
00364A1A  49 83 C5 08                     add r13, 8
00364A1E  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00364A23  E9 5F FF FF FF                  jmp 0x140364987
00364A28  44 03 E6                        add r12d, esi
00364A2B  44 85 25 7A 08 C6 00            test dword ptr [rip + 0xc6087a], r12d
00364A32  0F 84 11 01 00 00               je 0x140364b49
00364A38  F3 90                           pause
00364A3A  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00364A3E  48 85 C0                        test rax, rax
00364A41  0F 89 6C FF FF FF               jns 0x1403649b3
00364A47  EB DF                           jmp 0x140364a28
00364A49  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00364A4E  48 85 FF                        test rdi, rdi
00364A51  74 16                           je 0x140364a69
00364A53  8A 95 80 00 00 00               mov dl, byte ptr [rbp + 0x80]
00364A59  48 8B CF                        mov rcx, rdi
00364A5C  E8 2F 16 EE FF                  call 0x140246090
00364A61  45 33 DB                        xor r11d, r11d
00364A64  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00364A69  83 7D 84 00                     cmp dword ptr [rbp - 0x7c], 0
00364A6D  0F 85 B4 FD FF FF               jne 0x140364827
00364A73  49 8B 45 00                     mov rax, qword ptr [r13]
00364A77  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00364A7B  4C 8B E8                        mov r13, rax
00364A7E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00364A83  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00364A87  75 09                           jne 0x140364a92
00364A89  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00364A8D  48 39 0A                        cmp qword ptr [rdx], rcx
00364A90  74 07                           je 0x140364a99
00364A92  B9 03 00 00 00                  mov ecx, 3
00364A97  CD 29                           int 0x29
00364A99  4C 8B 65 70                     mov r12, qword ptr [rbp + 0x70]
00364A9D  48 89 02                        mov qword ptr [rdx], rax
00364AA0  48 89 50 08                     mov qword ptr [rax + 8], rdx
00364AA4  41 FF 8C 24 D4 00 00 00         dec dword ptr [r12 + 0xd4]
00364AAC  E8 4F 0E F5 FF                  call 0x1402b5900
00364AB1  E9 96 FD FF FF                  jmp 0x14036484c
00364AB6  41 8B D4                        mov edx, r12d
00364AB9  49 8B C8                        mov rcx, r8
00364ABC  E8 BF AF F3 FF                  call 0x14029fa80
00364AC1  8B 4D 80                        mov ecx, dword ptr [rbp - 0x80]
00364AC4  85 C0                           test eax, eax
00364AC6  41 0F 45 CC                     cmovne ecx, r12d
00364ACA  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
00364ACD  E9 34 FA FF FF                  jmp 0x140364506
00364AD2  8A 95 80 00 00 00               mov dl, byte ptr [rbp + 0x80]
00364AD8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00364ADD  E8 AE 15 EE FF                  call 0x140246090
00364AE2  44 8B 85 88 00 00 00            mov r8d, dword ptr [rbp + 0x88]
00364AE9  33 C9                           xor ecx, ecx
00364AEB  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00364AF0  49 8B D4                        mov rdx, r12
00364AF3  49 8B CF                        mov rcx, r15
00364AF6  E8 8D 4E 11 00                  call 0x140479988
00364AFB  45 33 DB                        xor r11d, r11d
00364AFE  85 C0                           test eax, eax
00364B00  0F 88 63 FF FF FF               js 0x140364a69
00364B06  E9 88 FA FF FF                  jmp 0x140364593
00364B0B  4D 85 FF                        test r15, r15
00364B0E  75 22                           jne 0x140364b32
00364B10  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00364B13  45 33 C0                        xor r8d, r8d
00364B16  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00364B1B  33 C9                           xor ecx, ecx
00364B1D  C1 E8 10                        shr eax, 0x10
00364B20  44 0F B6 C8                     movzx r9d, al
00364B24  41 C1 E9 06                     shr r9d, 6
00364B28  E8 63 DA FC FF                  call 0x140332590
00364B2D  E9 E9 FB FF FF                  jmp 0x14036471b
00364B32  8A 95 80 00 00 00               mov dl, byte ptr [rbp + 0x80]
00364B38  49 8B CF                        mov rcx, r15
00364B3B  E8 50 15 EE FF                  call 0x140246090
00364B40  33 C9                           xor ecx, ecx
00364B42  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00364B47  EB C7                           jmp 0x140364b10
00364B49  8B 05 69 1F C6 00               mov eax, dword ptr [rip + 0xc61f69]
00364B4F  A8 40                           test al, 0x40
00364B51  0F 84 E1 FE FF FF               je 0x140364a38
00364B57  E8 34 A9 FA FF                  call 0x14030f490
00364B5C  45 33 DB                        xor r11d, r11d
00364B5F  84 C0                           test al, al
00364B61  0F 84 D1 FE FF FF               je 0x140364a38
00364B67  41 8B CC                        mov ecx, r12d
00364B6A  E8 F1 A8 FA FF                  call 0x14030f460
00364B6F  45 33 DB                        xor r11d, r11d
00364B72  E9 C3 FE FF FF                  jmp 0x140364a3a
00364B77  8A 95 80 00 00 00               mov dl, byte ptr [rbp + 0x80]
00364B7D  E8 0E 15 EE FF                  call 0x140246090
00364B82  E9 21 FA FF FF                  jmp 0x1403645a8
00364B87  45 33 DB                        xor r11d, r11d
00364B8A  41 8D 53 01                     lea edx, [r11 + 1]
00364B8E  E9 42 FC FF FF                  jmp 0x1403647d5
00364B93  8B 5D D4                        mov ebx, dword ptr [rbp - 0x2c]
00364B96  8B 75 9C                        mov esi, dword ptr [rbp - 0x64]
00364B99  44 8B 74 24 3C                  mov r14d, dword ptr [rsp + 0x3c]
00364B9E  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
00364BA2  E9 34 F9 FF FF                  jmp 0x1403644db
00364BA7  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00364BAC  E9 98 FE FF FF                  jmp 0x140364a49
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfPutPagesInTransition(__int64 a1, __int64 a2, int a3, int a4)
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
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p42;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (296);
    result = 0;
    v_stack_m108 = 0;
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 104 - 92) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 188)));
    *(unsigned __int64 *)(v_rsp - 104 - 64) = 0;
    v_stack_m118 = v_xmm0;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 60)) & (0x3FFULL));
    v_stack_m100 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 16) = v_xmm0;
    v_stack_mEC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    v_stack_m120 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11321130) + a1 * 8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56))) & (8));
    v_stack_m138 = 0;
    *(unsigned int *)(v_rsp - 104 - 48) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 192))) + 1);
    *(unsigned __int64 *)(v_rsp - 104 - 32) = 0;
    *(unsigned int *)(v_rsp - 104 - 104) = (unsigned int)(result);
    *(unsigned __int8 *)(v_rsp - 104 + 128) = 17;
    v_stack_m130 = 0;
    result = PsGetIoPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 8), a3, (unsigned int)(*(unsigned int *)(a1 + 184)));
    v_stack_m12C = 0;
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (7));
    *(unsigned int *)(v_rsp - 104 - 96) = (unsigned int)(result);
    a1 = (unsigned __int8)((a1) | (24));
    *(unsigned __int64 *)(v_rsp - 104 - 112) = 0;
    v_stack_m12C = (unsigned __int8)(a1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56))) >> (20));
    v_rbx = (unsigned int)((v_rbx) & (127));
    *(unsigned int *)(v_rsp - 104 - 44) = (unsigned int)(v_rbx);
    result = MiInitializePageColorBase(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_r10 + 3, (unsigned int)((unsigned int)(v_rbx)), v_rsp - 104 - 16);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 104 - 8))) >> (9));
    v_rsi = (unsigned int)((v_rsi) & (63));
    *(unsigned __int64 *)(v_rsp - 104) = a1 + 224;
    *(unsigned int *)(v_rsp - 104 - 100) = (unsigned int)(v_rsi);
    v_stack_mF8 = *(unsigned __int64 *)(a1 + 224);
    if ((*(unsigned __int64 *)(a1 + 224)) == (a1 + 224)) goto loc_00364861;
loc_00364226:
    *(unsigned __int64 *)(v_rsp - 104 + 16) = *(unsigned __int64 *)(a1 + 224);
    if ((*(unsigned int *)(v_rsp - 104 - 96)) < 2) goto loc_0036488D;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 208))))) == 0) goto loc_0036425E;
loc_00364257:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 224) + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 224) + 192)));
loc_0036425E:
    v_r11 = 0;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 200)) + (8);
    *(unsigned __int64 *)(v_rsp - 104 - 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240);
    *(unsigned __int64 *)(v_rsp - 104 + 8) = v_r12;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240))) & (-4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240) = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240))) & (-4);
    *(unsigned __int64 *)(v_rsp - 104 - 72) = result;
    *(unsigned __int64 *)(v_rsp - 104 - 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 44))) + (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 32)));
    a1 = (unsigned int)((a1) & (0xFFFULL));
    v_r10 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 40))) + (0xFFFULL);
    v_r10 = (v_r10) + (a1);
    v_r10 = (v_r10) >> (12);
    if (v_r10 >= 2) goto loc_003646AE;
loc_003642CE:
    if (0 >= v_r10) goto loc_003642F8;
loc_003642DC:
    a3 = (unsigned int)((0) + (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 48) = *(unsigned __int64 *)(v_rip + 11350357);
    if (((unsigned int)(a3)) < v_r10) goto loc_003642DC;
    v_r11 = 0;
loc_003642F8:
    *(unsigned int *)(v_rsp - 104 - 124) = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 80) = 0;
    if (0 != 0) goto loc_00364336;
    a1 = 0;
    result = MiGetInPageSupportBlock(a1, *(unsigned __int64 *)(v_rsp - 104 + 144), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 48 + 8);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 112) = result;
    if (result != 0) {
        a2 = *(unsigned int *)(v_rsp - 104 - 92);
        a1 = result;
        a3 = v_stack_mEC;
        *(unsigned __int64 *)(result + 248) = 0;
        result = MiSetInPagePriority(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 48 + 8);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240)) >= v_r12) goto loc_00364A49;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 240))) & (-4);
    *(unsigned __int64 *)(v_rsp - 104 - 24) = v_r12;
    v_rdi = (v_r12) >> (9);
    *(unsigned __int64 *)(v_rsp - 104 - 40) = 0;
    if (v_stack_m138 == 0) goto loc_003645A8;
    a2 = (v_rdi) & (result);
    a2 = (a2) + (result);
    if ((*(unsigned __int64 *)(v_rsp - 104 - 32)) != a2) goto loc_00364B77;
    v_stack_m138 = v_stack_m138;
loc_00364392:
    result = MiLockLeafPage(v_r12, 2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 256) + 48 + 8);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 120) = *(unsigned __int64 *)(v_r12);
    if (result != 0) goto loc_003646FD;
    if (condition_is_above_or_equal) goto loc_003648CD;
    if (*(unsigned __int64 *)(v_rip + 11311288) == 0) goto loc_003643E3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r12))) & (16)) != 0) goto loc_0036462C;
    v_r15 = ~(*(unsigned __int64 *)(v_rip + 11311288));
    v_r15 = (v_r15) & (*(unsigned __int64 *)(v_r12));
loc_003643E3:
    v_r15 = (v_r15) >> (16);
    *(unsigned __int64 *)(v_rsp - 104 - 40) = v_r15;
    v_stack_mF0 = 1;
    a3 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 112) + 8) + 62)) & (12));
    if (((unsigned __int8)(a3)) == 4) goto loc_00364AD2;
    if (((unsigned __int8)(a3)) == 8) goto loc_00364593;
loc_00364418:
    result = 0;
    v_stack_m128 = 0;
    v_stack_m108 = 0;
    v_stack_m118 = v_xmm0;
    if (*(unsigned __int64 *)(v_rsp - 104 - 80) == 0) goto loc_003645E5;
    if ((*(unsigned int *)(v_rsp - 104 - 48)) != 0) goto loc_00364723;
loc_00364443:
loc_00364448:
    *(unsigned int *)(v_rsp - 104 - 128) = 0;
    if (v_stack_mF0 != 1) goto loc_00364480;
    v_stack_m148 = v_stack_m130;
    result = MiUseSlabAllocator(v_stack_m120, *(unsigned __int64 *)(v_rsp - 104 - 40), *(unsigned __int64 *)(v_r12), (unsigned int)((unsigned int)(v_rsi)));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00364927;
loc_00364480:
    v_r12 = (*(unsigned __int64 *)(v_rsp - 104 + 112)) + (40);
loc_0036448B:
    result = MiUnlinkPageChainHead(v_r12, *(unsigned __int64 *)(v_rsp - 104 - 40), *(unsigned __int64 *)(v_r12), (unsigned int)((unsigned int)(v_rsi)));
    *(unsigned __int64 *)(v_rsp - 104 - 120) = result;
    if (result == 0) goto loc_00364652;
    a2 = (result) - ((unsigned int)((unsigned int)(v_rsi)));
    a2 = (a2) >> (4);
    a2 = (a2) * ((unsigned int)((unsigned int)(v_rsi)));
    v_stack_m100 = a2;
    if (v_stack_m128 != 0) goto loc_00364956;
loc_003644DB:
    result = *(unsigned __int64 *)(v_rsp - 104 - 80);
    if (((unsigned int)((unsigned int)(v_stack_mF0))) == 1) { result = *(unsigned __int64 *)(v_rsp - 104 - 24); }
    *(unsigned __int64 *)(v_rsp - 104 - 80) = result;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 104 - 88))) & (1)) != 0) goto loc_00364AB6;
loc_00364506:
    if ((*(unsigned __int64 *)(v_stack_mF8 + 248)) == 0) {
        *(unsigned __int64 *)(v_stack_mF8 + 248) = result;
    }
    v_stack_m140 = (unsigned int)((unsigned int)(v_stack_m12C));
    v_stack_m148 = v_stack_mF8;
    a1 = ((unsigned int)((unsigned int)(v_rsi))) | (-1);
    result = MiInitializeReadInProgressPfn(a1, v_stack_m100, 1, *(unsigned __int64 *)(v_rsp - 104 - 24));
    result = MiReferenceControlAreaPfn(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 112) + 8), *(unsigned __int64 *)(v_rsp - 104 - 40), 1, *(unsigned __int64 *)(v_rsp - 104 - 24));
    v_r15 = (*(unsigned __int64 *)(v_rsp - 104 - 24)) - (*(unsigned __int64 *)(v_rsp - 104 - 72));
    v_r11 = 0;
    v_r15 = (v_r15) >> (3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 - 56) + v_r15 * 8 + 48) = v_stack_m100;
    if ((*(unsigned __int64 *)(v_stack_mF8 + 160)) == 0) goto loc_00364635;
loc_00364589:
    if ((*(unsigned int *)(v_rsp - 104 - 128)) != 0) goto loc_00364B0B;
loc_00364593:
    v_rdi = (*(unsigned __int64 *)(v_rsp - 104 - 88)) + (8);
    *(unsigned __int64 *)(v_rsp - 104 - 88) = v_rdi;
    goto loc_00364336;
loc_003645A8:
    a1 = (v_rdi) & (v_stack_m100);
    a1 = (a1) + (v_stack_m100);
    *(unsigned __int64 *)(v_rsp - 104 - 32) = a1;
    result = MiLockProtoPoolPageForce(*(unsigned __int64 *)(v_rsp - 104 + 8), v_rsp - 104 + 128, 1, *(unsigned __int64 *)(v_rsp - 104 - 24));
    v_stack_m138 = result;
    goto loc_00364392;
loc_003645E5:
    a1 = (*(unsigned __int64 *)(v_rsp - 104 + 8)) - (*(unsigned __int64 *)(v_rsp - 104 - 72));
    a1 = (a1) >> (3);
    if (a1 == 0) goto loc_00364443;
    result = (unsigned __int16)(-((unsigned __int16)(a1)));
    *(unsigned __int64 *)(v_rsp - 104 - 72) = *(unsigned __int64 *)(v_rsp - 104 + 8);
    result = (unsigned __int16)((result) << (3));
    result = (unsigned int)((result) * ((unsigned int)(a1)));
    a1 = (a1) << (12);
    *(unsigned __int64 *)(v_stack_mF8 + 240) = *(unsigned __int64 *)(v_rsp - 104 + 8);
    goto loc_00364443;
loc_0036462C:
    v_r15 = (v_stack_m138) & (-17);
    goto loc_003643E3;
loc_00364635:
    a2 = 0;
    result = MiObtainProtoReference(v_r15, a2, 1, *(unsigned __int64 *)(v_rsp - 104 - 24));
    v_r11 = 0;
    *(unsigned __int64 *)(v_stack_mF8 + 160) = v_r15;
    goto loc_00364589;
loc_00364652:
    v_stack_m148 = 1;
    result = MiPrefetchPagesViable(v_stack_m120, *(unsigned __int64 *)(v_rsp - 104 + 120), (unsigned int)(*(unsigned int *)(v_rsp - 104 - 104)), 1);
    v_r11 = 0;
loc_0036467B:
    if (v_r15 == 0) goto loc_00364BA7;
    result = (v_stack_m108) - 1;
    v_stack_m118 = *(unsigned __int64 *)(v_r15);
    v_stack_m108 = result;
    result = -(result);
    result = MiReturnPfnReferenceCountAtDpc(v_r15, *(unsigned __int64 *)(v_rsp - 104 + 120), (unsigned int)(*(unsigned int *)(v_rsp - 104 - 104)), 1);
    goto loc_0036467B;
loc_003646AE:
    if (1 > (*(unsigned __int64 *)(v_rsp - 104 + 120))) goto loc_003646C7;
    if ((1 + v_r10 - 1 * 8) >= (*(unsigned __int64 *)(v_rsp - 104 + 120))) goto loc_003646F5;
loc_003646C7:
    a2 = (v_r10) & (-2);
loc_003646CE:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 104 - 104))) + (2));
    if (((unsigned int)(a3)) < a2) goto loc_003646CE;
    a2 = (a2) << (3);
    a1 = (a2) >> (3);
    a4 = (1) + (a2);
loc_003646F5:
    v_r11 = 0;
    goto loc_003642CE;
loc_003646FD:
    a3 = 0;
    result = MiUpdatePfnPriority(*(unsigned __int64 *)(v_r15), (unsigned int)(v_stack_mEC), a3, a4);
loc_0036471B:
    v_r11 = 0;
    goto loc_00364593;
loc_00364723:
    v_r12 = (*(unsigned __int64 *)(v_rsp - 104 + 8)) - (result);
    v_r12 = (v_r12) >> (3);
    v_r12 = (v_r12) - (*(unsigned __int64 *)(v_r15));
    if (condition_is_equal) goto loc_00364443;
    v_stack_m148 = 0;
    result = MiPrefetchPagesViable(v_stack_m120, *(unsigned __int64 *)(v_rsp - 104 + 120), (unsigned int)(*(unsigned int *)(v_rsp - 104 - 104)), v_r12);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00364A49;
loc_00364773:
    result = MiGetPageForHeader(v_stack_m120, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r11 + 1)), v_r12);
    v_stack_m100 = result;
    if (result == -1) goto loc_00364B87;
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    v_r11 = 0;
    v_stack_m118 = a1;
    v_r13 = v_stack_m110;
    if (v_stack_m110 == 0) { v_r13 = a1; }
    *(unsigned __int64 *)(a1) = v_stack_m118;
    v_rsi = (v_stack_m128) + (v_r11 + 1);
    v_stack_m110 = v_r13;
    v_r14 = (0) + (v_r11 + 1);
    v_stack_m108 = v_rsi;
    if (v_r14 != v_r12) goto loc_00364773;
loc_003647D5:
    v_stack_m128 = v_rsi;
    if (v_r14 == v_r12) goto loc_00364448;
loc_003647EF:
    if (a1 == 0) goto loc_00364BA7;
    result = (v_stack_m108) - (v_r11 + 1);
    v_stack_m118 = *(unsigned __int64 *)(a1);
    v_stack_m108 = result;
    result = -(result);
    result = MiReturnPfnReferenceCountAtDpc(a1, v_r11 + 1, (unsigned int)((unsigned int)(v_r11 + 1)), v_r12);
    goto loc_003647EF;
loc_00364827:
    result = MiReduceMdl(*(unsigned __int64 *)(v_rsp - 104 - 56), 1, (unsigned int)((unsigned int)(v_r11 + 1)), v_r12);
    if ((*(unsigned __int64 *)(v_rsp - 104 - 56)) != (v_r13 + 272)) goto loc_0036489D;
loc_0036483F:
    v_stack_mF8 = *(unsigned __int64 *)(v_r13);
loc_0036484C:
    if ((*(unsigned __int64 *)(v_r13)) != (*(unsigned __int64 *)(v_rsp - 104 + 112) + 224)) goto loc_00364226;
loc_00364861:
    result = MiFreeReadListPages(*(unsigned __int64 *)(v_rsp - 104 + 112), 1, (unsigned int)((unsigned int)(v_r11 + 1)), v_r12);
    if (*(unsigned __int64 *)(v_rsp - 104 - 112) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 104 - 112);
        result = MiFreeInPageSupportBlock(a1, 1, (unsigned int)((unsigned int)(v_r11 + 1)), v_r12);
    }
    result = 0;
    v_rsp = (v_rsp) + (296);
    return result;
loc_0036488D:
    goto loc_00364257;
loc_0036489D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 40)) > 0x10000ULL) goto loc_0036483F;
    result = memcpy(v_r13 + 272, *(unsigned __int64 *)(v_rsp - 104 - 112), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 104 - 112), a2, (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 256) = v_r13 + 272;
    goto loc_0036483F;
loc_003648CD:
    v_stack_p78 = 2;
    if (((1) & ((unsigned __int8)(v_r13 + 272))) != 0) goto loc_00364918;
    if (*(unsigned __int64 *)(v_rip + 11309978) == 0) goto loc_003648FD;
    if ((((unsigned __int8)(v_r13 + 272)) & (16)) != 0) goto loc_00364950;
    result = ~(*(unsigned __int64 *)(v_rip + 11309978));
    result = (result) & (v_r13 + 272);
loc_003648FD:
    if (condition_is_below) goto loc_00364913;
    if (condition_is_below) goto loc_00364913;
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00364593;
loc_00364913:
loc_00364918:
    if ((*(unsigned __int64 *)(v_rsp - 104 - 112)) == 0) goto loc_00364593;
    goto loc_00364418;
loc_00364927:
    if (v_stack_p38 > 4) goto loc_00364480;
    goto loc_0036448B;
loc_00364950:
    result = (*(unsigned __int64 *)(v_rsp - 104 + 112)) & (-17);
    goto loc_003648FD;
loc_00364956:
    v_r13 = (*(unsigned __int64 *)(v_rsp - 104 - 80)) - (*(unsigned __int64 *)(v_rsp - 104 - 72));
    v_r13 = (v_r13) >> (3);
    v_r12 = (*(unsigned __int64 *)(v_rsp - 104 - 56)) + (56);
loc_00364987:
    if (*(unsigned __int64 *)(v_rsp - 104 - 112) == 0) goto loc_00364B93;
    v_stack_p50 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 - 112));
    result = (v_stack_p60) - (1);
    v_stack_p60 = result;
    result = -(result);
loc_003649B3:
    if (condition_is_below) goto loc_00364A28;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8) = -3;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32))) >> (16));
    result = (unsigned __int8)((result) | (7));
    v_stack_p42 = (unsigned __int8)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32) = (unsigned int)((unsigned int)(v_stack_p40));
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32))) >> (16));
    result = (unsigned __int8)((result) | (32));
    v_stack_p42 = (unsigned __int8)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 32) = (unsigned int)((unsigned int)(v_stack_p40));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 - 112)) = 0;
    v_r15 = (*(unsigned __int64 *)(v_rsp - 104 - 112)) - ((unsigned int)(v_stack_m12C));
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * ((unsigned int)(v_stack_m12C));
    *(unsigned __int64 *)(v_r12 + v_r13 * 8) = v_r15;
    v_r13 = (v_r12 + v_r13 * 8) + (8);
    goto loc_00364987;
loc_00364A28:
    v_r12 = (unsigned int)((0) + (1));
    if (((*(unsigned int *)(v_rip + 12978298)) & ((unsigned int)(v_r12))) == 0) goto loc_00364B49;
loc_00364A38:
loc_00364A3A:
    if (!sign_flag) goto loc_003649B3;
    goto loc_00364A28;
loc_00364A49:
    result = *(unsigned __int64 *)(v_stack_p50 + 24);
    if (v_stack_p30 != 0) {
        a2 = *(unsigned __int8 *)(v_rsp - 104 + 128);
        a1 = v_stack_p30;
        result = MiUnlockProtoPoolPage(a1, a2, (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
        v_r11 = 0;
        v_stack_p30 = 0;
    }
    if ((*(unsigned int *)(v_rsp - 104 - 124)) != 0) goto loc_00364827;
    v_stack_p70 = *(unsigned __int64 *)(v_r13);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) != (*(unsigned __int64 *)(v_rsp - 104 + 16))) goto loc_00364A92;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 16) + 8))) != (*(unsigned __int64 *)(v_rsp - 104 + 16))) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 16) + 8)) = *(unsigned __int64 *)(v_r13);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 16) + 8);
    result = MiFreeInPageSupportBlock(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 16) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
    goto loc_0036484C;
loc_00364AB6:
    result = MiPfnZeroingNeeded((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 104 + 112))), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
    a1 = (unsigned int)(*(unsigned int *)(v_rsp - 104 - 128));
    if ((unsigned int)(result) != 0) { a1 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 104 + 112)); }
    *(unsigned int *)(v_rsp - 104 - 128) = (unsigned int)(a1);
    goto loc_00364506;
loc_00364AD2:
    result = MiUnlockProtoPoolPage(v_stack_p30, *(unsigned __int8 *)(v_rsp - 104 + 128), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 104 - 112) + 8)), v_r12);
    a1 = 0;
    v_stack_p30 = 0;
    result = MiRefillPurgedExtents(v_stack_p50, *(unsigned __int64 *)(v_rsp - 104 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 104 + 136)), v_r12);
    v_r11 = 0;
    if (sign_flag) goto loc_00364A69;
    goto loc_00364593;
loc_00364B0B:
    if (v_stack_p50 != 0) goto loc_00364B32;
loc_00364B10:
    a3 = 0;
    a1 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p30 + 32))) >> (16));
    a4 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiZeroPhysicalPage(a1, v_stack_p68, a3, a4);
    goto loc_0036471B;
loc_00364B32:
    result = MiUnlockProtoPoolPage(v_stack_p50, *(unsigned __int8 *)(v_rsp - 104 + 128), a3, a4);
    a1 = 0;
    v_stack_p30 = 0;
    goto loc_00364B10;
loc_00364B49:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12984169)))) & (64)) == 0) goto loc_00364A38;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int8 *)(v_rsp - 104 + 128), a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00364A38;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 104 + 112))), *(unsigned __int8 *)(v_rsp - 104 + 128), a3, a4);
    v_r11 = 0;
    goto loc_00364A3A;
loc_00364B77:
    result = MiUnlockProtoPoolPage((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 104 + 112))), *(unsigned __int8 *)(v_rsp - 104 + 128), a3, a4);
    goto loc_003645A8;
loc_00364B87:
    v_r11 = 0;
    goto loc_003647D5;
loc_00364B93:
    goto loc_003644DB;
loc_00364BA7:
    goto loc_00364A49;
}
```

## 5. (Beta) C Style

```c
int64_t MiPfPutPagesInTransition(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint32_t v_stack_p40;
    uint8_t v_stack_p42;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (296);
    result = 0;
    v_stack_m108 = 0;
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0x68 - 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xBC)));
    *(uint64_t *)(local_rsp - 0x68 - 0x40) = 0;
    v_stack_m118 = v_xmm0;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C)) & (0x3FFULL));
    v_stack_m100 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x10) = v_xmm0;
    v_stack_mEC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    v_stack_m120 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xACBF2A) + arg1 * 8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38))) & (8));
    v_stack_m138 = 0;
    *(uint32_t *)(local_rsp - 0x68 - 0x30) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC0))) + 1);
    *(uint64_t *)(local_rsp - 0x68 - 0x20) = 0;
    *(uint32_t *)(local_rsp - 0x68 - 0x68) = (uint32_t)(result);
    *(uint8_t *)(local_rsp - 0x68 + 0x80) = 17;
    v_stack_m130 = 0;
    result = PsGetIoPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x8), Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    v_stack_m12C = 0;
    Arg1 = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (7));
    *(uint32_t *)(local_rsp - 0x68 - 0x60) = (uint32_t)(result);
    Arg1 = (uint8_t)((Arg1) | (24));
    *(uint64_t *)(local_rsp - 0x68 - 0x70) = 0;
    v_stack_m12C = (uint8_t)(Arg1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38))) >> (20));
    local_rbx = (uint32_t)((local_rbx) & (127));
    *(uint32_t *)(local_rsp - 0x68 - 0x2C) = (uint32_t)(local_rbx);
    result = MiInitializePageColorBase(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, local_r10 + 3, (uint32_t)((uint32_t)(local_rbx)), local_rsp - 104 - 16);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x8))) >> (9));
    local_rsi = (uint32_t)((local_rsi) & (63));
    *(void **)(local_rsp - 0x68) = Arg1 + 224;
    *(uint32_t *)(local_rsp - 0x68 - 0x64) = (uint32_t)(local_rsi);
    v_stack_mF8 = *(uint64_t *)(arg1 + 0xE0);
    if ((*(uint64_t *)(arg1 + 0xE0)) == (Arg1 + 224)) goto loc_00364861;
loc_00364226:
    *(uint64_t *)(local_rsp - 0x68 + 0x10) = *(uint64_t *)(arg1 + 0xE0);
    if ((*(uint32_t *)(local_rsp - 0x68 - 0x60)) < 2) goto loc_0036488D;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD0))))) == 0) goto loc_0036425E;
loc_00364257:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xC0)));
loc_0036425E:
    local_r11 = 0;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xC8)) + (8);
    *(uint64_t *)(local_rsp - 0x68 - 0x58) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0);
    *(uint64_t *)(local_rsp - 0x68 + 0x8) = local_r12;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0))) & (-4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0) = result;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0))) & (-4);
    *(uint64_t *)(local_rsp - 0x68 - 0x48) = result;
    *(uint64_t *)(local_rsp - 0x68 - 0x38) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 0x2C))) + (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 0x20)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    local_r10 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 0x28))) + (0xFFFULL);
    local_r10 = (local_r10) + (Arg1);
    local_r10 = (local_r10) >> (12);
    if (local_r10 >= 2) goto loc_003646AE;
loc_003642CE:
    if (0 >= local_r10) goto loc_003642F8;
loc_003642DC:
    Arg3 = (uint32_t)((0) + (1));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 0x30) = *(uint64_t *)(v_rip + 0xAD3155);
    if (((uint32_t)(Arg3)) < local_r10) goto loc_003642DC;
    local_r11 = 0;
loc_003642F8:
    *(uint32_t *)(local_rsp - 0x68 - 0x7C) = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x50) = 0;
    if (0 != 0) goto loc_00364336;
    Arg1 = 0;
    result = MiGetInPageSupportBlock(Arg1, *(uint64_t *)(local_rsp - 0x68 + 0x90), Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 48 + 8);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x70) = result;
    if (result != 0) {
        Arg2 = *(uint32_t *)(local_rsp - 0x68 - 0x5C);
        Arg1 = result;
        Arg3 = v_stack_mEC;
        *(uint64_t *)(result + 0xF8) = 0;
        result = MiSetInPagePriority(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 48 + 8);
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0)) >= local_r12) goto loc_00364A49;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0xF0))) & (-4);
    *(uint64_t *)(local_rsp - 0x68 - 0x18) = local_r12;
    local_rdi = (local_r12) >> (9);
    *(uint64_t *)(local_rsp - 0x68 - 0x28) = 0;
    if (v_stack_m138 == 0) goto loc_003645A8;
    Arg2 = (local_rdi) & (result);
    Arg2 = (Arg2) + (result);
    if ((*(uint64_t *)(local_rsp - 0x68 - 0x20)) != Arg2) goto loc_00364B77;
    v_stack_m138 = v_stack_m138;
loc_00364392:
    result = MiLockLeafPage(local_r12, 2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x100) + 48 + 8);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = *(uint64_t *)(local_r12);
    if (result != 0) goto loc_003646FD;
    if (condition_is_above_or_equal) goto loc_003648CD;
    if (*(uint64_t *)(v_rip + 0xAC98B8) == 0) goto loc_003643E3;
    if ((((uint8_t)(*(uint64_t *)(local_r12))) & (16)) != 0) goto loc_0036462C;
    local_r15 = ~(*(uint64_t *)(v_rip + 0xAC98B8));
    local_r15 = (local_r15) & (*(uint64_t *)(local_r12));
loc_003643E3:
    local_r15 = (local_r15) >> (16);
    *(uint64_t *)(local_rsp - 0x68 - 0x28) = local_r15;
    v_stack_mF0 = 1;
    Arg3 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x70) + 0x8) + 0x3E)) & (12));
    if (((uint8_t)(Arg3)) == 4) goto loc_00364AD2;
    if (((uint8_t)(Arg3)) == 8) goto loc_00364593;
loc_00364418:
    result = 0;
    v_stack_m128 = 0;
    v_stack_m108 = 0;
    v_stack_m118 = v_xmm0;
    if (*(uint64_t *)(local_rsp - 0x68 - 0x50) == 0) goto loc_003645E5;
    if ((*(uint32_t *)(local_rsp - 0x68 - 0x30)) != 0) goto loc_00364723;
loc_00364443:
loc_00364448:
    *(uint32_t *)(local_rsp - 0x68 - 0x80) = 0;
    if (v_stack_mF0 != 1) goto loc_00364480;
    v_stack_m148 = v_stack_m130;
    result = MiUseSlabAllocator(v_stack_m120, *(uint64_t *)(local_rsp - 0x68 - 0x28), *(uint64_t *)(local_r12), (uint32_t)((uint32_t)(local_rsi)));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00364927;
loc_00364480:
    local_r12 = (*(uint64_t *)(local_rsp - 0x68 + 0x70)) + (40);
loc_0036448B:
    result = MiUnlinkPageChainHead(local_r12, *(uint64_t *)(local_rsp - 0x68 - 0x28), *(uint64_t *)(local_r12), (uint32_t)((uint32_t)(local_rsi)));
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = result;
    if (result == 0) goto loc_00364652;
    Arg2 = (result) - ((uint32_t)((uint32_t)(local_rsi)));
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(local_rsi)));
    v_stack_m100 = Arg2;
    if (v_stack_m128 != 0) goto loc_00364956;
loc_003644DB:
    result = *(uint64_t *)(local_rsp - 0x68 - 0x50);
    if (((uint32_t)((uint32_t)(v_stack_mF0))) == 1) { result = *(uint64_t *)(local_rsp - 0x68 - 0x18); }
    *(uint64_t *)(local_rsp - 0x68 - 0x50) = result;
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x58))) & (1)) != 0) goto loc_00364AB6;
loc_00364506:
    if ((*(uint64_t *)(v_stack_mF8 + 0xF8)) == 0) {
        *(uint64_t *)(v_stack_mF8 + 0xF8) = result;
    }
    v_stack_m140 = (uint32_t)((uint32_t)(v_stack_m12C));
    v_stack_m148 = v_stack_mF8;
    Arg1 = ((uint32_t)((uint32_t)(local_rsi))) | (-1);
    result = MiInitializeReadInProgressPfn(Arg1, v_stack_m100, 1, *(uint64_t *)(local_rsp - 0x68 - 0x18));
    result = MiReferenceControlAreaPfn(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x70) + 0x8), *(uint64_t *)(local_rsp - 0x68 - 0x28), 1, *(uint64_t *)(local_rsp - 0x68 - 0x18));
    local_r15 = (*(uint64_t *)(local_rsp - 0x68 - 0x18)) - (*(uint64_t *)(local_rsp - 0x68 - 0x48));
    local_r11 = 0;
    local_r15 = (local_r15) >> (3);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x38) + local_r15 * 8 + 0x30) = v_stack_m100;
    if ((*(uint64_t *)(v_stack_mF8 + 0xA0)) == 0) goto loc_00364635;
loc_00364589:
    if ((*(uint32_t *)(local_rsp - 0x68 - 0x80)) != 0) goto loc_00364B0B;
loc_00364593:
    local_rdi = (*(uint64_t *)(local_rsp - 0x68 - 0x58)) + (8);
    *(uint64_t *)(local_rsp - 0x68 - 0x58) = local_rdi;
    goto loc_00364336;
loc_003645A8:
    Arg1 = (local_rdi) & (v_stack_m100);
    Arg1 = (Arg1) + (v_stack_m100);
    *(void **)(local_rsp - 0x68 - 0x20) = Arg1;
    result = MiLockProtoPoolPageForce(*(uint64_t *)(local_rsp - 0x68 + 0x8), local_rsp - 104 + 128, 1, *(uint64_t *)(local_rsp - 0x68 - 0x18));
    v_stack_m138 = result;
    goto loc_00364392;
loc_003645E5:
    Arg1 = (*(uint64_t *)(local_rsp - 0x68 + 0x8)) - (*(uint64_t *)(local_rsp - 0x68 - 0x48));
    Arg1 = (Arg1) >> (3);
    if (Arg1 == NULL) goto loc_00364443;
    result = (uint16_t)(-((uint16_t)(Arg1)));
    *(uint64_t *)(local_rsp - 0x68 - 0x48) = *(uint64_t *)(local_rsp - 0x68 + 0x8);
    result = (uint16_t)((result) << (3));
    result = (uint32_t)((result) * ((uint32_t)(Arg1)));
    Arg1 = (Arg1) << (12);
    *(uint64_t *)(v_stack_mF8 + 0xF0) = *(uint64_t *)(local_rsp - 0x68 + 0x8);
    goto loc_00364443;
loc_0036462C:
    local_r15 = (v_stack_m138) & (-17);
    goto loc_003643E3;
loc_00364635:
    Arg2 = 0;
    result = MiObtainProtoReference(local_r15, Arg2, 1, *(uint64_t *)(local_rsp - 0x68 - 0x18));
    local_r11 = 0;
    *(uint64_t *)(v_stack_mF8 + 0xA0) = local_r15;
    goto loc_00364589;
loc_00364652:
    v_stack_m148 = 1;
    result = MiPrefetchPagesViable(v_stack_m120, *(uint64_t *)(local_rsp - 0x68 + 0x78), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x68)), 1);
    local_r11 = 0;
loc_0036467B:
    if (local_r15 == 0) goto loc_00364BA7;
    result = (v_stack_m108) - 1;
    v_stack_m118 = *(uint64_t *)(local_r15);
    v_stack_m108 = result;
    result = -(result);
    result = MiReturnPfnReferenceCountAtDpc(local_r15, *(uint64_t *)(local_rsp - 0x68 + 0x78), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x68)), 1);
    goto loc_0036467B;
loc_003646AE:
    if (1 > (*(uint64_t *)(local_rsp - 0x68 + 0x78))) goto loc_003646C7;
    if ((1 + local_r10 - 1 * 8) >= (*(uint64_t *)(local_rsp - 0x68 + 0x78))) goto loc_003646F5;
loc_003646C7:
    Arg2 = (local_r10) & (-2);
loc_003646CE:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x68))) + (2));
    if (((uint32_t)(Arg3)) < Arg2) goto loc_003646CE;
    Arg2 = (Arg2) << (3);
    Arg1 = (Arg2) >> (3);
    Arg4 = (1) + (Arg2);
loc_003646F5:
    local_r11 = 0;
    goto loc_003642CE;
loc_003646FD:
    Arg3 = 0;
    result = MiUpdatePfnPriority(*(uint64_t *)(local_r15), (uint32_t)(v_stack_mEC), Arg3, Arg4);
loc_0036471B:
    local_r11 = 0;
    goto loc_00364593;
loc_00364723:
    local_r12 = (*(uint64_t *)(local_rsp - 0x68 + 0x8)) - (result);
    local_r12 = (local_r12) >> (3);
    local_r12 = (local_r12) - (*(uint64_t *)(local_r15));
    if (condition_is_equal) goto loc_00364443;
    v_stack_m148 = 0;
    result = MiPrefetchPagesViable(v_stack_m120, *(uint64_t *)(local_rsp - 0x68 + 0x78), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x68)), local_r12);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00364A49;
loc_00364773:
    result = MiGetPageForHeader(v_stack_m120, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r11 + 1)), local_r12);
    v_stack_m100 = result;
    if (result == -1) goto loc_00364B87;
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    local_r11 = 0;
    v_stack_m118 = Arg1;
    local_r13 = v_stack_m110;
    if (v_stack_m110 == 0) { local_r13 = Arg1; }
    *(uint64_t *)(arg1) = v_stack_m118;
    local_rsi = (v_stack_m128) + (local_r11 + 1);
    v_stack_m110 = local_r13;
    local_r14 = (0) + (local_r11 + 1);
    v_stack_m108 = local_rsi;
    if (local_r14 != local_r12) goto loc_00364773;
loc_003647D5:
    v_stack_m128 = local_rsi;
    if (local_r14 == local_r12) goto loc_00364448;
loc_003647EF:
    if (Arg1 == NULL) goto loc_00364BA7;
    result = (v_stack_m108) - (local_r11 + 1);
    v_stack_m118 = *(uint64_t *)(arg1);
    v_stack_m108 = result;
    result = -(result);
    result = MiReturnPfnReferenceCountAtDpc(Arg1, local_r11 + 1, (uint32_t)((uint32_t)(local_r11 + 1)), local_r12);
    goto loc_003647EF;
loc_00364827:
    result = MiReduceMdl(*(uint64_t *)(local_rsp - 0x68 - 0x38), 1, (uint32_t)((uint32_t)(local_r11 + 1)), local_r12);
    if ((*(uint64_t *)(local_rsp - 0x68 - 0x38)) != (local_r13 + 272)) goto loc_0036489D;
loc_0036483F:
    v_stack_mF8 = *(uint64_t *)(local_r13);
loc_0036484C:
    if ((*(uint64_t *)(local_r13)) != (*(uint64_t *)(local_rsp - 0x68 + 0x70) + 224)) goto loc_00364226;
loc_00364861:
    result = MiFreeReadListPages(*(uint64_t *)(local_rsp - 0x68 + 0x70), 1, (uint32_t)((uint32_t)(local_r11 + 1)), local_r12);
    if (*(uint64_t *)(local_rsp - 0x68 - 0x70) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x68 - 0x70);
        result = MiFreeInPageSupportBlock(Arg1, 1, (uint32_t)((uint32_t)(local_r11 + 1)), local_r12);
    }
    result = 0;
    local_rsp = (local_rsp) + (296);
    return result;
loc_0036488D:
    goto loc_00364257;
loc_0036489D:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x28)) > 0x10000ULL) goto loc_0036483F;
    result = memcpy(local_r13 + 272, *(uint64_t *)(local_rsp - 0x68 - 0x70), (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x68 - 0x70), Arg2, (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
    *(uint64_t *)(*(uint64_t *)(local_r13) + 0x100) = local_r13 + 272;
    goto loc_0036483F;
loc_003648CD:
    v_stack_p78 = 2;
    if (((1) & ((uint8_t)(local_r13 + 272))) != 0) goto loc_00364918;
    if (*(uint64_t *)(v_rip + 0xAC939A) == 0) goto loc_003648FD;
    if ((((uint8_t)(local_r13 + 272)) & (16)) != 0) goto loc_00364950;
    result = ~(*(uint64_t *)(v_rip + 0xAC939A));
    result = (result) & (local_r13 + 272);
loc_003648FD:
    if (condition_is_below) goto loc_00364913;
    if (condition_is_below) goto loc_00364913;
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00364593;
loc_00364913:
loc_00364918:
    if ((*(uint64_t *)(local_rsp - 0x68 - 0x70)) == 0) goto loc_00364593;
    goto loc_00364418;
loc_00364927:
    if (v_stack_p38 > 4) goto loc_00364480;
    goto loc_0036448B;
loc_00364950:
    result = (*(uint64_t *)(local_rsp - 0x68 + 0x70)) & (-17);
    goto loc_003648FD;
loc_00364956:
    local_r13 = (*(uint64_t *)(local_rsp - 0x68 - 0x50)) - (*(uint64_t *)(local_rsp - 0x68 - 0x48));
    local_r13 = (local_r13) >> (3);
    local_r12 = (*(uint64_t *)(local_rsp - 0x68 - 0x38)) + (56);
loc_00364987:
    if (*(uint64_t *)(local_rsp - 0x68 - 0x70) == 0) goto loc_00364B93;
    v_stack_p50 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70));
    result = (v_stack_p60) - (1);
    v_stack_p60 = result;
    result = -(result);
loc_003649B3:
    if (condition_is_below) goto loc_00364A28;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8) = -3;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20))) >> (16));
    result = (uint8_t)((result) | (7));
    v_stack_p42 = (uint8_t)(result);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20) = (uint32_t)((uint32_t)(v_stack_p40));
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20))) >> (16));
    result = (uint8_t)((result) | (32));
    v_stack_p42 = (uint8_t)(result);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x20) = (uint32_t)((uint32_t)(v_stack_p40));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70)) = 0;
    local_r15 = (*(uint64_t *)(local_rsp - 0x68 - 0x70)) - ((uint32_t)(v_stack_m12C));
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * ((uint32_t)(v_stack_m12C));
    *(uint64_t *)(local_r12 + local_r13 * 8) = local_r15;
    local_r13 = (local_r12 + local_r13 * 8) + (8);
    goto loc_00364987;
loc_00364A28:
    local_r12 = (uint32_t)((0) + (1));
    if (((*(uint32_t *)(v_rip + 0xC6087A)) & ((uint32_t)(local_r12))) == 0) goto loc_00364B49;
loc_00364A38:
loc_00364A3A:
    if (!sign_flag) goto loc_003649B3;
    goto loc_00364A28;
loc_00364A49:
    result = *(uint64_t *)(v_stack_p50 + 0x18);
    if (v_stack_p30 != 0) {
        Arg2 = *(uint8_t *)(local_rsp - 0x68 + 0x80);
        Arg1 = v_stack_p30;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
        local_r11 = 0;
        v_stack_p30 = 0;
    }
    if ((*(uint32_t *)(local_rsp - 0x68 - 0x7C)) != 0) goto loc_00364827;
    v_stack_p70 = *(uint64_t *)(local_r13);
    if ((*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) != (*(uint64_t *)(local_rsp - 0x68 + 0x10))) goto loc_00364A92;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x10) + 0x8))) != (*(uint64_t *)(local_rsp - 0x68 + 0x10))) {
        Arg1 = 3;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x10) + 0x8)) = *(uint64_t *)(local_r13);
    *(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x10) + 0x8);
    result = MiFreeInPageSupportBlock(Arg1, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x10) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
    goto loc_0036484C;
loc_00364AB6:
    result = MiPfnZeroingNeeded((int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x68 + 0x70))), (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
    Arg1 = (uint32_t)(*(uint32_t *)(local_rsp - 0x68 - 0x80));
    if ((uint32_t)(result) != 0) { Arg1 = (uint32_t)(*(uint64_t *)(local_rsp - 0x68 + 0x70)); }
    *(uint32_t *)(local_rsp - 0x68 - 0x80) = (uint32_t)(Arg1);
    goto loc_00364506;
loc_00364AD2:
    result = MiUnlockProtoPoolPage(v_stack_p30, *(uint8_t *)(local_rsp - 0x68 + 0x80), (int16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x68 - 0x70) + 0x8)), local_r12);
    Arg1 = 0;
    v_stack_p30 = 0;
    result = MiRefillPurgedExtents(v_stack_p50, *(uint64_t *)(local_rsp - 0x68 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x88)), local_r12);
    local_r11 = 0;
    if (sign_flag) goto loc_00364A69;
    goto loc_00364593;
loc_00364B0B:
    if (v_stack_p50 != 0) goto loc_00364B32;
loc_00364B10:
    Arg3 = 0;
    Arg1 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20))) >> (16));
    Arg4 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiZeroPhysicalPage(Arg1, v_stack_p68, Arg3, Arg4);
    goto loc_0036471B;
loc_00364B32:
    result = MiUnlockProtoPoolPage(v_stack_p50, *(uint8_t *)(local_rsp - 0x68 + 0x80), Arg3, Arg4);
    Arg1 = 0;
    v_stack_p30 = 0;
    goto loc_00364B10;
loc_00364B49:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC61F69)))) & (64)) == 0) goto loc_00364A38;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint8_t *)(local_rsp - 0x68 + 0x80), Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00364A38;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x68 + 0x70))), *(uint8_t *)(local_rsp - 0x68 + 0x80), Arg3, Arg4);
    local_r11 = 0;
    goto loc_00364A3A;
loc_00364B77:
    result = MiUnlockProtoPoolPage((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x68 + 0x70))), *(uint8_t *)(local_rsp - 0x68 + 0x80), Arg3, Arg4);
    goto loc_003645A8;
loc_00364B87:
    local_r11 = 0;
    goto loc_003647D5;
loc_00364B93:
    goto loc_003644DB;
loc_00364BA7:
    goto loc_00364A49;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003640EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
