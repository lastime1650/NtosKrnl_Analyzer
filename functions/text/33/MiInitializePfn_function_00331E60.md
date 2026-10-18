# MiInitializePfn

- RVA: `0x00331E60`–`0x0033257F` (길이 `1,823` bytes)
- VA: `0x0000000140331E60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076590`
- 디코드: `420`개 명령, `1,823/1,823` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00332112` → [MiChangePageAttribute](MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x00332462` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00332472` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003324AE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003324BE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003324CB` → [MiCanPfnOriginalPteBeLost](../37/MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)
- `0x00332509` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x0033251D` → [MiMakeDemandZeroPte](MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00332560` → [MiIncreaseUsedPtesInPfn](../38/MiIncreaseUsedPtesInPfn_function_00382D90.md) (function, `0x00382D90`)
- `0x00332575` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiAllocateKernelStackPages](../2A/MiAllocateKernelStackPages_function_002A1BEC.md) at `0x002A1ED5`
- [MiCreateSharedZeroPages](../2B/MiCreateSharedZeroPages_function_002B6318.md) at `0x002B6540`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B819E`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F729C`
- [MiCompletePrivateZeroFault](MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331027`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0F27`
- [MmInitializeImageViewExtensionCfg](../../init/C6/MmInitializeImageViewExtensionCfg_function_00C64FC4.md) at `0x00C6516B`

### Static image references
- `0x0033221A` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0033237A` → RVA `0x00E2DC80` (`.data`; read)
- `0x003323B3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00332454` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00331E60  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00331E65  53                              push rbx
00331E66  55                              push rbp
00331E67  56                              push rsi
00331E68  57                              push rdi
00331E69  41 54                           push r12
00331E6B  41 55                           push r13
00331E6D  41 56                           push r14
00331E6F  41 57                           push r15
00331E71  48 83 EC 38                     sub rsp, 0x38
00331E75  48 8B 1A                        mov rbx, qword ptr [rdx]
00331E78  45 8B F1                        mov r14d, r9d
00331E7B  45 8B C8                        mov r9d, r8d
00331E7E  4C 8B D2                        mov r10, rdx
00331E81  48 8B F9                        mov rdi, rcx
00331E84  48 BE 00 D0 BE 7D FB F6 FF FF   movabs rsi, 0xfffff6fb7dbed000
00331E8E  48 8B C6                        mov rax, rsi
00331E91  49 BB F8 D7 BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbed7f8
00331E9B  48 3B D0                        cmp rdx, rax
00331E9E  72 24                           jb 0x140331ec4
00331EA0  49 8B C3                        mov rax, r11
00331EA3  48 3B D0                        cmp rdx, rax
00331EA6  77 1C                           ja 0x140331ec4
00331EA8  48 8B C3                        mov rax, rbx
00331EAB  F6 C3 01                        test bl, 1
00331EAE  74 14                           je 0x140331ec4
00331EB0  F6 C3 42                        test bl, 0x42
00331EB3  0F 95 C2                        setne dl
00331EB6  F6 C3 20                        test bl, 0x20
00331EB9  0F 95 C1                        setne cl
00331EBC  84 D1                           test cl, dl
00331EBE  0F 84 56 03 00 00               je 0x14033221a
00331EC4  48 8B C3                        mov rax, rbx
00331EC7  41 F6 C6 04                     test r14b, 4
00331ECB  0F 85 AB 05 00 00               jne 0x14033247c
00331ED1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00331ED6  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00331EDB  48 8B C6                        mov rax, rsi
00331EDE  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00331EE3  48 3B D0                        cmp rdx, rax
00331EE6  72 2B                           jb 0x140331f13
00331EE8  49 8B C3                        mov rax, r11
00331EEB  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00331EF0  48 3B D0                        cmp rdx, rax
00331EF3  77 1E                           ja 0x140331f13
00331EF5  48 8B C1                        mov rax, rcx
00331EF8  F6 C1 01                        test cl, 1
00331EFB  74 16                           je 0x140331f13
00331EFD  F6 C1 42                        test cl, 0x42
00331F00  41 0F 95 C0                     setne r8b
00331F04  F6 C1 20                        test cl, 0x20
00331F07  0F 95 C2                        setne dl
00331F0A  44 84 C2                        test dl, r8b
00331F0D  0F 84 DB 03 00 00               je 0x1403322ee
00331F13  48 0F BA E1 0A                  bt rcx, 0xa
00331F18  48 C7 C0 F7 FF FF FF            mov rax, 0xfffffffffffffff7
00331F1F  48 C7 C2 FF F7 FF FF            mov rdx, 0xfffffffffffff7ff
00331F26  48 0F 42 C2                     cmovb rax, rdx
00331F2A  48 23 C1                        and rax, rcx
00331F2D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00331F32  48 89 01                        mov qword ptr [rcx], rax
00331F35  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
00331F3A  41 F6 C6 08                     test r14b, 8
00331F3E  0F 85 36 04 00 00               jne 0x14033237a
00331F44  45 33 E4                        xor r12d, r12d
00331F47  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00331F4B  4C 89 27                        mov qword ptr [rdi], r12
00331F4E  41 F6 C6 02                     test r14b, 2
00331F52  0F 85 08 04 00 00               jne 0x140332360
00331F58  B8 01 00 00 00                  mov eax, 1
00331F5D  44 8B F8                        mov r15d, eax
00331F60  45 85 C9                        test r9d, r9d
00331F63  0F 84 CB 04 00 00               je 0x140332434
00331F69  41 83 F9 1F                     cmp r9d, 0x1f
00331F6D  74 16                           je 0x140331f85
00331F6F  41 8B C1                        mov eax, r9d
00331F72  C1 E8 03                        shr eax, 3
00331F75  83 F8 03                        cmp eax, 3
00331F78  0F 84 C1 04 00 00               je 0x14033243f
00331F7E  41 3B C7                        cmp eax, r15d
00331F81  45 0F 44 FC                     cmove r15d, r12d
00331F85  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00331F8F  4D 8B CA                        mov r9, r10
00331F92  49 C1 E9 09                     shr r9, 9
00331F96  4C 23 C8                        and r9, rax
00331F99  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00331FA3  48 8B C0                        mov rax, rax
00331FA6  4C 03 C8                        add r9, rax
00331FA9  4D 8B 01                        mov r8, qword ptr [r9]
00331FAC  48 8B C6                        mov rax, rsi
00331FAF  4C 3B C8                        cmp r9, rax
00331FB2  72 27                           jb 0x140331fdb
00331FB4  49 8B C3                        mov rax, r11
00331FB7  4C 3B C8                        cmp r9, rax
00331FBA  77 1F                           ja 0x140331fdb
00331FBC  49 8B C0                        mov rax, r8
00331FBF  41 F6 C0 01                     test r8b, 1
00331FC3  74 16                           je 0x140331fdb
00331FC5  41 F6 C0 42                     test r8b, 0x42
00331FC9  0F 95 C2                        setne dl
00331FCC  41 F6 C0 20                     test r8b, 0x20
00331FD0  0F 95 C1                        setne cl
00331FD3  84 D1                           test cl, dl
00331FD5  0F 84 AA 02 00 00               je 0x140332285
00331FDB  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
00331FDF  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00331FE9  49 C1 E8 0C                     shr r8, 0xc
00331FED  49 BA 00 00 00 00 00 FF FF FF   movabs r10, 0xffffff0000000000
00331FF7  49 8B C8                        mov rcx, r8
00331FFA  4D 8B C8                        mov r9, r8
00331FFD  48 33 CA                        xor rcx, rdx
00332000  4C 23 C8                        and r9, rax
00332003  49 23 CA                        and rcx, r10
00332006  48 8B C2                        mov rax, rdx
00332009  49 33 C8                        xor rcx, r8
0033200C  F0 48 0F B1 4F 28               lock cmpxchg qword ptr [rdi + 0x28], rcx
00332012  48 3B D0                        cmp rdx, rax
00332015  74 1A                           je 0x140332031
00332017  49 8B C8                        mov rcx, r8
0033201A  48 8B D0                        mov rdx, rax
0033201D  48 33 C8                        xor rcx, rax
00332020  49 23 CA                        and rcx, r10
00332023  49 33 C8                        xor rcx, r8
00332026  F0 48 0F B1 4F 28               lock cmpxchg qword ptr [rdi + 0x28], rcx
0033202C  48 3B D0                        cmp rdx, rax
0033202F  75 E6                           jne 0x140332017
00332031  4B 8D 2C 49                     lea rbp, [r9 + r9*2]
00332035  48 C1 E5 04                     shl rbp, 4
00332039  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00332043  48 03 E8                        add rbp, rax
00332046  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0033204F  8B B0 A8 05 00 00               mov esi, dword ptr [rax + 0x5a8]
00332055  0F BA E6 08                     bt esi, 8
00332059  0F 83 A2 03 00 00               jae 0x140332401
0033205F  C1 EE 09                        shr esi, 9
00332062  45 8B EE                        mov r13d, r14d
00332065  C6 84 24 90 00 00 00 11         mov byte ptr [rsp + 0x90], 0x11
0033206D  41 83 E5 01                     and r13d, 1
00332071  75 1A                           jne 0x14033208d
00332073  41 F6 C6 10                     test r14b, 0x10
00332077  0F 84 89 04 00 00               je 0x140332506
0033207D  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00332084  0F 82 56 03 00 00               jb 0x1403323e0
0033208A  45 33 E4                        xor r12d, r12d
0033208D  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00332090  BA 01 00 00 00                  mov edx, 1
00332095  89 8C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ecx
0033209C  66 89 94 24 98 00 00 00         mov word ptr [rsp + 0x98], dx
003320A4  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
003320AB  89 4F 20                        mov dword ptr [rdi + 0x20], ecx
003320AE  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
003320B5  0F 82 F5 02 00 00               jb 0x1403323b0
003320BB  48 85 DB                        test rbx, rbx
003320BE  0F 84 63 04 00 00               je 0x140332527
003320C4  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
003320C8  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
003320D2  48 8D 48 01                     lea rcx, [rax + 1]
003320D6  4C 8B C9                        mov r9, rcx
003320D9  4C 33 C8                        xor r9, rax
003320DC  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
003320E6  4C 23 C8                        and r9, rax
003320E9  4C 33 C9                        xor r9, rcx
003320EC  4C 89 4D 18                     mov qword ptr [rbp + 0x18], r9
003320F0  F0 48 21 5D 18                  lock and qword ptr [rbp + 0x18], rbx
003320F5  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003320F8  C1 E8 10                        shr eax, 0x10
003320FB  0F B6 C0                        movzx eax, al
003320FE  C1 E8 06                        shr eax, 6
00332101  41 3B C7                        cmp eax, r15d
00332104  74 11                           je 0x140332117
00332106  41 B8 01 00 00 00               mov r8d, 1
0033210C  41 8B D7                        mov edx, r15d
0033210F  48 8B CF                        mov rcx, rdi
00332112  E8 B5 0D 00 00                  call 0x140332ecc
00332117  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0033211B  48 B9 FF FF FF FF FF FF FF C7   movabs rcx, 0xc7ffffffffffffff
00332125  48 23 C1                        and rax, rcx
00332128  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
00332132  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00332136  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0033213A  48 23 C1                        and rax, rcx
0033213D  48 83 C8 01                     or rax, 1
00332141  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00332145  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00332148  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
0033214F  C1 E8 18                        shr eax, 0x18
00332152  40 32 F0                        xor sil, al
00332155  40 80 E6 07                     and sil, 7
00332159  40 32 F0                        xor sil, al
0033215C  40 88 B4 24 9B 00 00 00         mov byte ptr [rsp + 0x9b], sil
00332164  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
0033216B  89 47 20                        mov dword ptr [rdi + 0x20], eax
0033216E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00332176  48 89 47 08                     mov qword ptr [rdi + 8], rax
0033217A  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0033217D  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
00332184  C1 E8 10                        shr eax, 0x10
00332187  24 FE                           and al, 0xfe
00332189  0C 06                           or al, 6
0033218B  88 84 24 9A 00 00 00            mov byte ptr [rsp + 0x9a], al
00332192  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
00332199  89 47 20                        mov dword ptr [rdi + 0x20], eax
0033219C  41 F6 C6 20                     test r14b, 0x20
003321A0  75 30                           jne 0x1403321d2
003321A2  44 8B 5F 20                     mov r11d, dword ptr [rdi + 0x20]
003321A6  44 89 9C 24 98 00 00 00         mov dword ptr [rsp + 0x98], r11d
003321AE  41 C1 EB 10                     shr r11d, 0x10
003321B2  41 F6 C3 08                     test r11b, 8
003321B6  0F 85 0C 03 00 00               jne 0x1403324c8
003321BC  41 80 CB 10                     or r11b, 0x10
003321C0  44 88 9C 24 9A 00 00 00         mov byte ptr [rsp + 0x9a], r11b
003321C8  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
003321CF  89 47 20                        mov dword ptr [rdi + 0x20], eax
003321D2  41 0F BA E6 0D                  bt r14d, 0xd
003321D7  73 0A                           jae 0x1403321e3
003321D9  48 8B 07                        mov rax, qword ptr [rdi]
003321DC  48 83 C8 01                     or rax, 1
003321E0  48 89 07                        mov qword ptr [rdi], rax
003321E3  C7 47 24 00 00 00 00            mov dword ptr [rdi + 0x24], 0
003321EA  41 F6 C6 40                     test r14b, 0x40
003321EE  0F 85 B2 01 00 00               jne 0x1403323a6
003321F4  45 85 ED                        test r13d, r13d
003321F7  75 0F                           jne 0x140332208
003321F9  41 F6 C6 10                     test r14b, 0x10
003321FD  0F 84 67 03 00 00               je 0x14033256a
00332203  F0 48 21 5F 18                  lock and qword ptr [rdi + 0x18], rbx
00332208  48 83 C4 38                     add rsp, 0x38
0033220C  41 5F                           pop r15
0033220E  41 5E                           pop r14
00332210  41 5D                           pop r13
00332212  41 5C                           pop r12
00332214  5F                              pop rdi
00332215  5E                              pop rsi
00332216  5D                              pop rbp
00332217  5B                              pop rbx
00332218  C3                              ret
00332219  CC                              int3
0033221A  48 F7 05 63 48 C9 00 00 00 60 00  test qword ptr [rip + 0xc94863], 0x600000
00332225  0F 84 99 FC FF FF               je 0x140331ec4
0033222B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00332234  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0033223B  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00332242  0F 84 7C FC FF FF               je 0x140331ec4
00332248  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
0033224F  4D 85 C0                        test r8, r8
00332252  0F 84 6C FC FF FF               je 0x140331ec4
00332258  49 8B CA                        mov rcx, r10
0033225B  48 C1 E9 03                     shr rcx, 3
0033225F  81 E1 FF 01 00 00               and ecx, 0x1ff
00332265  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
00332269  F6 C1 20                        test cl, 0x20
0033226C  74 04                           je 0x140332272
0033226E  48 83 C8 20                     or rax, 0x20
00332272  48 8B D8                        mov rbx, rax
00332275  48 83 CB 42                     or rbx, 0x42
00332279  F6 C1 42                        test cl, 0x42
0033227C  48 0F 44 D8                     cmove rbx, rax
00332280  E9 3F FC FF FF                  jmp 0x140331ec4
00332285  48 F7 05 F8 47 C9 00 00 00 60 00  test qword ptr [rip + 0xc947f8], 0x600000
00332290  0F 84 45 FD FF FF               je 0x140331fdb
00332296  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0033229F  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
003322A6  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
003322AD  0F 84 28 FD FF FF               je 0x140331fdb
003322B3  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
003322BA  48 85 C9                        test rcx, rcx
003322BD  0F 84 18 FD FF FF               je 0x140331fdb
003322C3  49 C1 E9 03                     shr r9, 3
003322C7  41 81 E1 FF 01 00 00            and r9d, 0x1ff
003322CE  4A 8B 0C C9                     mov rcx, qword ptr [rcx + r9*8]
003322D2  F6 C1 20                        test cl, 0x20
003322D5  74 04                           je 0x1403322db
003322D7  48 83 C8 20                     or rax, 0x20
003322DB  4C 8B C0                        mov r8, rax
003322DE  49 83 C8 42                     or r8, 0x42
003322E2  F6 C1 42                        test cl, 0x42
003322E5  4C 0F 44 C0                     cmove r8, rax
003322E9  E9 ED FC FF FF                  jmp 0x140331fdb
003322EE  48 F7 05 8F 47 C9 00 00 00 60 00  test qword ptr [rip + 0xc9478f], 0x600000
003322F9  0F 84 14 FC FF FF               je 0x140331f13
003322FF  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00332308  4C 8B 82 B8 00 00 00            mov r8, qword ptr [rdx + 0xb8]
0033230F  41 80 B8 60 01 00 00 01         cmp byte ptr [r8 + 0x160], 1
00332317  0F 84 F6 FB FF FF               je 0x140331f13
0033231D  4D 8B 90 08 05 00 00            mov r10, qword ptr [r8 + 0x508]
00332324  4D 85 D2                        test r10, r10
00332327  74 2A                           je 0x140332353
00332329  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0033232E  48 C1 EA 03                     shr rdx, 3
00332332  81 E2 FF 01 00 00               and edx, 0x1ff
00332338  49 8B 14 D2                     mov rdx, qword ptr [r10 + rdx*8]
0033233C  F6 C2 20                        test dl, 0x20
0033233F  74 04                           je 0x140332345
00332341  48 83 C8 20                     or rax, 0x20
00332345  48 8B C8                        mov rcx, rax
00332348  48 83 C9 42                     or rcx, 0x42
0033234C  F6 C2 42                        test dl, 0x42
0033234F  48 0F 44 C8                     cmove rcx, rax
00332353  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
0033235B  E9 B3 FB FF FF                  jmp 0x140331f13
00332360  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00332364  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0033236E  48 0B C1                        or rax, rcx
00332371  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00332375  E9 DE FB FF FF                  jmp 0x140331f58
0033237A  48 8B 15 FF B8 AF 00            mov rdx, qword ptr [rip + 0xafb8ff]
00332381  B8 80 00 00 00                  mov eax, 0x80
00332386  48 85 D2                        test rdx, rdx
00332389  0F 84 B5 FB FF FF               je 0x140331f44
0033238F  48 8B CA                        mov rcx, rdx
00332392  48 0B C8                        or rcx, rax
00332395  B8 90 00 00 00                  mov eax, 0x90
0033239A  F6 C2 80                        test dl, 0x80
0033239D  48 0F 44 C1                     cmove rax, rcx
003323A1  E9 9E FB FF FF                  jmp 0x140331f44
003323A6  80 4F 23 20                     or byte ptr [rdi + 0x23], 0x20
003323AA  E9 45 FE FF FF                  jmp 0x1403321f4
003323AF  90                              nop
003323B0  41 FF C4                        inc r12d
003323B3  44 85 25 F2 2E C9 00            test dword ptr [rip + 0xc92ef2], r12d
003323BA  0F 84 94 00 00 00               je 0x140332454
003323C0  F3 90                           pause
003323C2  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
003323C6  48 85 C0                        test rax, rax
003323C9  0F 89 DF FC FF FF               jns 0x1403320ae
003323CF  EB DF                           jmp 0x1403323b0
003323D1  0F 1F 40 00                     nop dword ptr [rax]
003323D5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
003323E0  41 FF C4                        inc r12d
003323E3  44 85 25 C2 2E C9 00            test dword ptr [rip + 0xc92ec2], r12d
003323EA  0F 84 B0 00 00 00               je 0x1403324a0
003323F0  F3 90                           pause
003323F2  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003323F6  48 85 C0                        test rax, rax
003323F9  0F 89 7E FC FF FF               jns 0x14033207d
003323FF  EB DF                           jmp 0x1403323e0
00332401  8B B0 A0 05 00 00               mov esi, dword ptr [rax + 0x5a0]
00332407  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
0033240E  C1 EE 0C                        shr esi, 0xc
00332411  83 E6 07                        and esi, 7
00332414  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
0033241B  48 85 C0                        test rax, rax
0033241E  0F 84 3E FC FF FF               je 0x140332062
00332424  8B 80 44 04 00 00               mov eax, dword ptr [rax + 0x444]
0033242A  3B F0                           cmp esi, eax
0033242C  0F 43 F0                        cmovae esi, eax
0033242F  E9 2E FC FF FF                  jmp 0x140332062
00332434  41 BF 03 00 00 00               mov r15d, 3
0033243A  E9 46 FB FF FF                  jmp 0x140331f85
0033243F  41 F6 C1 07                     test r9b, 7
00332443  0F 84 3C FB FF FF               je 0x140331f85
00332449  41 BF 02 00 00 00               mov r15d, 2
0033244F  E9 31 FB FF FF                  jmp 0x140331f85
00332454  8B 05 5E 46 C9 00               mov eax, dword ptr [rip + 0xc9465e]
0033245A  A8 40                           test al, 0x40
0033245C  0F 84 5E FF FF FF               je 0x1403323c0
00332462  E8 29 D0 FD FF                  call 0x14030f490
00332467  84 C0                           test al, al
00332469  0F 84 51 FF FF FF               je 0x1403323c0
0033246F  41 8B CC                        mov ecx, r12d
00332472  E8 E9 CF FD FF                  call 0x14030f460
00332477  E9 46 FF FF FF                  jmp 0x1403323c2
0033247C  48 85 DB                        test rbx, rbx
0033247F  0F 84 95 00 00 00               je 0x14033251a
00332485  49 8B C9                        mov rcx, r9
00332488  48 C1 E1 05                     shl rcx, 5
0033248C  48 8B C1                        mov rax, rcx
0033248F  48 33 C3                        xor rax, rbx
00332492  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00332498  48 33 C1                        xor rax, rcx
0033249B  E9 31 FA FF FF                  jmp 0x140331ed1
003324A0  8B 05 12 46 C9 00               mov eax, dword ptr [rip + 0xc94612]
003324A6  A8 40                           test al, 0x40
003324A8  0F 84 42 FF FF FF               je 0x1403323f0
003324AE  E8 DD CF FD FF                  call 0x14030f490
003324B3  84 C0                           test al, al
003324B5  0F 84 35 FF FF FF               je 0x1403323f0
003324BB  41 8B CC                        mov ecx, r12d
003324BE  E8 9D CF FD FF                  call 0x14030f460
003324C3  E9 2A FF FF FF                  jmp 0x1403323f2
003324C8  48 8B CF                        mov rcx, rdi
003324CB  E8 6C 18 04 00                  call 0x140373d3c
003324D0  85 C0                           test eax, eax
003324D2  0F 84 E4 FC FF FF               je 0x1403321bc
003324D8  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003324DC  0F B6 4F 22                     movzx ecx, byte ptr [rdi + 0x22]
003324E0  C0 E9 04                        shr cl, 4
003324E3  A8 04                           test al, 4
003324E5  F6 D1                           not cl
003324E7  0F 95 C0                        setne al
003324EA  22 C8                           and cl, al
003324EC  F6 C1 01                        test cl, 1
003324EF  0F 84 C7 FC FF FF               je 0x1403321bc
003324F5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003324F9  48 83 E0 FB                     and rax, 0xfffffffffffffffb
003324FD  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00332501  E9 B6 FC FF FF                  jmp 0x1403321bc
00332506  48 8B CF                        mov rcx, rdi
00332509  E8 32 7E FE FF                  call 0x14031a340
0033250E  88 84 24 90 00 00 00            mov byte ptr [rsp + 0x90], al
00332515  E9 73 FB FF FF                  jmp 0x14033208d
0033251A  41 8B C9                        mov ecx, r9d
0033251D  E8 DE 54 00 00                  call 0x140337a00
00332522  E9 AA F9 FF FF                  jmp 0x140331ed1
00332527  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00332531  48 8B C0                        mov rax, rax
00332534  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
0033253C  4C 3B D0                        cmp r10, rax
0033253F  0F 82 7F FB FF FF               jb 0x1403320c4
00332545  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0033254F  4C 3B D0                        cmp r10, rax
00332552  0F 87 6C FB FF FF               ja 0x1403320c4
00332558  BA 01 00 00 00                  mov edx, 1
0033255D  48 8B CD                        mov rcx, rbp
00332560  E8 2B 08 05 00                  call 0x140382d90
00332565  E9 5A FB FF FF                  jmp 0x1403320c4
0033256A  0F B6 94 24 90 00 00 00         movzx edx, byte ptr [rsp + 0x90]
00332572  48 8B CF                        mov rcx, rdi
00332575  E8 66 7E FE FF                  call 0x14031a3e0
0033257A  E9 89 FC FF FF                  jmp 0x140332208
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializePfn(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p22;
    unsigned __int8 v_stack_p23;
    unsigned __int64 v_stack_p88;
    unsigned __int8 v_stack_p90;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (56);
    if (a2 < v_rsi) goto loc_00331EC4;
    if (a2 > v_r11) goto loc_00331EC4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_00331EC4;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_0033221A;
loc_00331EC4:
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) != 0) goto loc_0033247C;
loc_00331ED1:
    v_stack_m58 = *(unsigned __int64 *)(a2);
    if (v_stack_m58 < v_rsi) goto loc_00331F13;
    if (v_stack_m58 > v_r11) goto loc_00331F13;
    if ((((unsigned __int8)(v_stack_m58)) & (1)) == 0) goto loc_00331F13;
    a3 = ((((unsigned __int8)(v_stack_m58)) & (66)) != 0) ? 1 : 0;
    a2 = ((((unsigned __int8)(v_stack_m58)) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a2)) & ((unsigned __int8)(a3))) == 0) goto loc_003322EE;
loc_00331F13:
    result = -9;
    if (condition_is_below) { result = 0xFFFFFFFFFFFFF7FFULL; }
    result = (result) & (v_stack_m58);
    *(unsigned __int64 *)(v_stack_m58) = result;
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) != 0) goto loc_0033237A;
loc_00331F44:
    v_r12 = 0;
    *(unsigned __int64 *)(a1 + 16) = v_stack_m58;
    *(unsigned __int64 *)(a1) = 0;
    if ((((unsigned __int8)((unsigned int)(a4))) & (2)) != 0) goto loc_00332360;
loc_00331F58:
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00332434;
    if (((unsigned int)((unsigned int)(a3))) == 31) goto loc_00331F85;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (3));
    if (((unsigned int)(result)) == 3) goto loc_0033243F;
    v_r15 = 1;
    if (((unsigned int)(result)) == 1) { v_r15 = 0; }
loc_00331F85:
    a4 = (a2) >> (9);
    a4 = (a4) & (result);
    a4 = (a4) + (result);
    if (a4 < v_rsi) goto loc_00331FDB;
    if (a4 > v_r11) goto loc_00331FDB;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) == 0) goto loc_00331FDB;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_00332285;
loc_00331FDB:
    a3 = (*(unsigned __int64 *)(a4)) >> (12);
    a1 = (a3) ^ (*(unsigned __int64 *)(a1 + 40));
    a4 = (a3) & (*(unsigned __int64 *)(a4));
    a1 = (a1) & (a2);
    a1 = (a1) ^ (a3);
    if ((*(unsigned __int64 *)(a1 + 40)) == (*(unsigned __int64 *)(a1 + 40))) goto loc_00332031;
loc_00332017:
    a1 = (a3) ^ (*(unsigned __int64 *)(a1 + 40));
    a1 = (a1) & (a2);
    a1 = (a1) ^ (a3);
    if ((*(unsigned __int64 *)(a1 + 40)) != (*(unsigned __int64 *)(a1 + 40))) goto loc_00332017;
loc_00332031:
    v_rbp = (a4 + a4 * 2) << (4);
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a1 + 40));
    if (condition_is_above_or_equal) goto loc_00332401;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448))) >> (9));
loc_00332062:
    v_stack_p18 = 17;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (1));
    if (condition_is_not_equal) goto loc_0033208D;
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) == 0) goto loc_00332506;
loc_0033207D:
    if (condition_is_below) goto loc_003323E0;
    v_r12 = 0;
loc_0033208D:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_stack_p20 = 1;
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p20));
loc_003320AE:
    if (condition_is_below) goto loc_003323B0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00332527;
loc_003320C4:
    a4 = (*(unsigned __int64 *)(v_rbp + 24) + 1) ^ (*(unsigned __int64 *)(v_rbp + 24));
    a4 = (a4) & (*(unsigned __int64 *)(v_rbp + 24));
    a4 = (a4) ^ (*(unsigned __int64 *)(v_rbp + 24) + 1);
    *(unsigned __int64 *)(v_rbp + 24) = a4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) {
        a3 = 1;
        a2 = (unsigned int)(v_r15);
        a1 = a1;
        result = MiChangePageAttribute(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    *(unsigned __int64 *)(a1 + 24) = result;
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    result = (result) | (1);
    *(unsigned __int64 *)(a1 + 24) = result;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    v_rsi = (unsigned __int8)((v_rsi) ^ ((unsigned __int8)(result)));
    v_rsi = (unsigned __int8)((v_rsi) & (7));
    v_rsi = (unsigned __int8)((v_rsi) ^ ((unsigned __int8)(result)));
    v_stack_p23 = (unsigned __int8)(v_rsi);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(a1 + 8) = v_stack_p10;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    v_stack_p22 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    if ((((unsigned __int8)((unsigned int)(a4))) & (32)) != 0) goto loc_003321D2;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    if ((((unsigned __int8)(v_r11)) & (8)) != 0) goto loc_003324C8;
loc_003321BC:
    v_r11 = (unsigned __int8)((v_r11) | (16));
    v_stack_p22 = (unsigned __int8)(v_r11);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p20));
loc_003321D2:
    result = (unsigned int)(v_stack_p20);
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(a1);
        result = (result) | (1);
        *(unsigned __int64 *)(a1) = result;
    }
    *(unsigned int *)(a1 + 36) = 0;
    if ((((unsigned __int8)((unsigned int)(a4))) & (64)) != 0) goto loc_003323A6;
loc_003321F4:
    if ((unsigned int)(v_r13) != 0) goto loc_00332208;
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) == 0) goto loc_0033256A;
loc_00332208:
    v_rsp = (v_rsp) + (56);
    return result;
loc_0033221A:
    if (((*(unsigned __int64 *)(v_rip + 13191267)) & (0x600000ULL)) == 0) goto loc_00331EC4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00331EC4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00331EC4;
    a1 = (a2) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    v_rbx = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { v_rbx = result; }
    goto loc_00331EC4;
loc_00332285:
    if (((*(unsigned __int64 *)(v_rip + 13191160)) & (0x600000ULL)) == 0) goto loc_00331FDB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00331FDB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00331FDB;
    a4 = (a4) >> (3);
    a4 = (unsigned int)((a4) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    a3 = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (66)) == 0) { a3 = result; }
    goto loc_00331FDB;
loc_003322EE:
    if (((*(unsigned __int64 *)(v_rip + 13191055)) & (0x600000ULL)) == 0) goto loc_00331F13;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00331F13;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00332353;
    a2 = (v_stack_p20) >> (3);
    a2 = (unsigned int)((a2) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    a1 = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a2 * 8))) & (66)) == 0) { a1 = result; }
loc_00332353:
    goto loc_00331F13;
loc_00332360:
    result = (*(unsigned __int64 *)(a1 + 40)) | (a1);
    *(unsigned __int64 *)(a1 + 40) = result;
    goto loc_00331F58;
loc_0033237A:
    if (*(unsigned __int64 *)(v_rip + 11516159) == 0) goto loc_00331F44;
    a1 = (*(unsigned __int64 *)(v_rip + 11516159)) | (128);
    result = 144;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 11516159))) & (128)) == 0) { result = a1; }
    goto loc_00331F44;
loc_003323A6:
    goto loc_003321F4;
loc_003323B0:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13184754)) & ((unsigned int)(v_r12))) == 0) goto loc_00332454;
loc_003323C0:
loc_003323C2:
    if (!sign_flag) goto loc_003320AE;
    goto loc_003323B0;
loc_003323E0:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13184706)) & ((unsigned int)(v_r12))) == 0) goto loc_003324A0;
loc_003323F0:
loc_003323F2:
    if (!sign_flag) goto loc_0033207D;
    goto loc_003323E0;
loc_00332401:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 1440))) >> (12));
    v_rsi = (unsigned int)((v_rsi) & (7));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 544) + 672) == 0) goto loc_00332062;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 544) + 672) + 1092))))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 544) + 672) + 1092))); }
    goto loc_00332062;
loc_00332434:
    goto loc_00331F85;
loc_0033243F:
    if ((((unsigned __int8)(a4)) & (7)) == 0) goto loc_00331F85;
    goto loc_00331F85;
loc_00332454:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13190750)))) & (64)) == 0) goto loc_003323C0;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003323C0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    goto loc_003323C2;
loc_0033247C:
    if (v_rbx == 0) goto loc_0033251A;
    a1 = (a4) << (5);
    result = (a1) ^ (v_rbx);
    result = (result) & (-993);
    result = (result) ^ (a1);
    goto loc_00331ED1;
loc_003324A0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13190674)))) & (64)) == 0) goto loc_003323F0;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003323F0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    goto loc_003323F2;
loc_003324C8:
    result = MiCanPfnOriginalPteBeLost(a1, *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    if ((unsigned int)(result) == 0) goto loc_003321BC;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (4)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_003321BC;
    result = (*(unsigned __int64 *)(a1 + 16)) & (-5);
    *(unsigned __int64 *)(a1 + 16) = result;
    goto loc_003321BC;
loc_00332506:
    result = MiLockPageInline(a1, *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    v_stack_p90 = (unsigned __int8)(result);
    goto loc_0033208D;
loc_0033251A:
    result = MiMakeDemandZeroPte((unsigned int)(a4), *(unsigned __int64 *)(v_rip + 11516159), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    goto loc_00331ED1;
loc_00332527:
    if (v_stack_p88 < result) goto loc_003320C4;
    if (v_stack_p88 > result) goto loc_003320C4;
    result = MiIncreaseUsedPtesInPfn(v_rbp, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    goto loc_003320C4;
loc_0033256A:
    result = MiUnlockPage(a1, v_stack_p90, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    goto loc_00332208;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializePfn(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p22;
    uint8_t v_stack_p23;
    uint64_t v_stack_p88;
    uint8_t v_stack_p90;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (56);
    if (Arg2 < local_rsi) goto loc_00331EC4;
    if (Arg2 > local_r11) goto loc_00331EC4;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) == 0) goto loc_00331EC4;
    Arg2 = ((((uint8_t)(*(uint64_t *)(arg2))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(arg2))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_0033221A;
loc_00331EC4:
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) != 0) goto loc_0033247C;
loc_00331ED1:
    v_stack_m58 = *(uint64_t *)(arg2);
    if (v_stack_m58 < local_rsi) goto loc_00331F13;
    if (v_stack_m58 > local_r11) goto loc_00331F13;
    if ((((uint8_t)(v_stack_m58)) & (1)) == 0) goto loc_00331F13;
    Arg3 = ((((uint8_t)(v_stack_m58)) & (66)) != 0) ? 1 : 0;
    Arg2 = ((((uint8_t)(v_stack_m58)) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg2)) & ((uint8_t)(Arg3))) == 0) goto loc_003322EE;
loc_00331F13:
    result = -9;
    if (condition_is_below) { result = 0xFFFFFFFFFFFFF7FFULL; }
    result = (result) & (v_stack_m58);
    *(uint64_t *)(v_stack_m58) = result;
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) != 0) goto loc_0033237A;
loc_00331F44:
    local_r12 = 0;
    *(uint64_t *)(arg1 + 0x10) = v_stack_m58;
    *(uint64_t *)(arg1) = 0;
    if ((((uint8_t)((uint32_t)(Arg4))) & (2)) != 0) goto loc_00332360;
loc_00331F58:
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00332434;
    if (((uint32_t)((uint32_t)(Arg3))) == 31) goto loc_00331F85;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (3));
    if (((uint32_t)(result)) == 3) goto loc_0033243F;
    local_r15 = 1;
    if (((uint32_t)(result)) == 1) { local_r15 = 0; }
loc_00331F85:
    Arg4 = (Arg2) >> (9);
    Arg4 = (Arg4) & (result);
    Arg4 = (Arg4) + (result);
    if (Arg4 < local_rsi) goto loc_00331FDB;
    if (Arg4 > local_r11) goto loc_00331FDB;
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) == 0) goto loc_00331FDB;
    Arg2 = ((((uint8_t)(*(uint64_t *)(Arg4))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg4))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_00332285;
loc_00331FDB:
    Arg3 = (*(uint64_t *)(Arg4)) >> (12);
    Arg1 = (Arg3) ^ (*(uint64_t *)(arg1 + 0x28));
    Arg4 = (Arg3) & (*(uint64_t *)(Arg4));
    Arg1 = (Arg1) & (Arg2);
    Arg1 = (Arg1) ^ (Arg3);
    if ((*(uint64_t *)(arg1 + 0x28)) == (*(uint64_t *)(arg1 + 0x28))) goto loc_00332031;
loc_00332017:
    Arg1 = (Arg3) ^ (*(uint64_t *)(arg1 + 0x28));
    Arg1 = (Arg1) & (Arg2);
    Arg1 = (Arg1) ^ (Arg3);
    if ((*(uint64_t *)(arg1 + 0x28)) != (*(uint64_t *)(arg1 + 0x28))) goto loc_00332017;
loc_00332031:
    local_rbp = (Arg4 + Arg4 * 2) << (4);
    local_rbp = (local_rbp) + (*(uint64_t *)(arg1 + 0x28));
    if (condition_is_above_or_equal) goto loc_00332401;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8))) >> (9));
loc_00332062:
    v_stack_p18 = 17;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (1));
    if (condition_is_not_equal) goto loc_0033208D;
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) == 0) goto loc_00332506;
loc_0033207D:
    if (condition_is_below) goto loc_003323E0;
    local_r12 = 0;
loc_0033208D:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    v_stack_p20 = 1;
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
loc_003320AE:
    if (condition_is_below) goto loc_003323B0;
    if (*(uint64_t *)(arg2) == 0) goto loc_00332527;
loc_003320C4:
    Arg4 = (*(uint64_t *)(local_rbp + 0x18) + 1) ^ (*(uint64_t *)(local_rbp + 0x18));
    Arg4 = (Arg4) & (*(uint64_t *)(local_rbp + 0x18));
    Arg4 = (Arg4) ^ (*(uint64_t *)(local_rbp + 0x18) + 1);
    *(uint64_t *)(local_rbp + 0x18) = Arg4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) {
        Arg3 = 1;
        Arg2 = (uint32_t)(local_r15);
        Arg1 = Arg1;
        result = MiChangePageAttribute(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    *(uint64_t *)(arg1 + 0x18) = result;
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    result = (result) | (1);
    *(uint64_t *)(arg1 + 0x18) = result;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    local_rsi = (uint8_t)((local_rsi) ^ ((uint8_t)(result)));
    local_rsi = (uint8_t)((local_rsi) & (7));
    local_rsi = (uint8_t)((local_rsi) ^ ((uint8_t)(result)));
    v_stack_p23 = (uint8_t)(local_rsi);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint64_t *)(arg1 + 0x8) = v_stack_p10;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    v_stack_p22 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    if ((((uint8_t)((uint32_t)(Arg4))) & (32)) != 0) goto loc_003321D2;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    if ((((uint8_t)(local_r11)) & (8)) != 0) goto loc_003324C8;
loc_003321BC:
    local_r11 = (uint8_t)((local_r11) | (16));
    v_stack_p22 = (uint8_t)(local_r11);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
loc_003321D2:
    result = (uint32_t)(v_stack_p20);
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(arg1);
        result = (result) | (1);
        *(uint64_t *)(arg1) = result;
    }
    *(uint32_t *)(arg1 + 0x24) = 0;
    if ((((uint8_t)((uint32_t)(Arg4))) & (64)) != 0) goto loc_003323A6;
loc_003321F4:
    if ((uint32_t)(local_r13) != 0) goto loc_00332208;
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) == 0) goto loc_0033256A;
loc_00332208:
    local_rsp = (local_rsp) + (56);
    return result;
loc_0033221A:
    if (((*(uint64_t *)(v_rip + 0xC94863)) & (0x600000ULL)) == 0) goto loc_00331EC4;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00331EC4;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00331EC4;
    Arg1 = (Arg2) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    local_rbx = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { local_rbx = result; }
    goto loc_00331EC4;
loc_00332285:
    if (((*(uint64_t *)(v_rip + 0xC947F8)) & (0x600000ULL)) == 0) goto loc_00331FDB;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00331FDB;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00331FDB;
    Arg4 = (Arg4) >> (3);
    Arg4 = (uint32_t)((Arg4) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    Arg3 = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8))) & (66)) == 0) { Arg3 = result; }
    goto loc_00331FDB;
loc_003322EE:
    if (((*(uint64_t *)(v_rip + 0xC9478F)) & (0x600000ULL)) == 0) goto loc_00331F13;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00331F13;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00332353;
    Arg2 = (v_stack_p20) >> (3);
    Arg2 = (uint32_t)((Arg2) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg2 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    Arg1 = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg2 * 8))) & (66)) == 0) { Arg1 = result; }
loc_00332353:
    goto loc_00331F13;
loc_00332360:
    result = (*(uint64_t *)(arg1 + 0x28)) | (Arg1);
    *(uint64_t *)(arg1 + 0x28) = result;
    goto loc_00331F58;
loc_0033237A:
    if (*(uint64_t *)(v_rip + 0xAFB8FF) == 0) goto loc_00331F44;
    Arg1 = (*(uint64_t *)(v_rip + 0xAFB8FF)) | (128);
    result = 144;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xAFB8FF))) & (128)) == 0) { result = Arg1; }
    goto loc_00331F44;
loc_003323A6:
    goto loc_003321F4;
loc_003323B0:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xC92EF2)) & ((uint32_t)(local_r12))) == 0) goto loc_00332454;
loc_003323C0:
loc_003323C2:
    if (!sign_flag) goto loc_003320AE;
    goto loc_003323B0;
loc_003323E0:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xC92EC2)) & ((uint32_t)(local_r12))) == 0) goto loc_003324A0;
loc_003323F0:
loc_003323F2:
    if (!sign_flag) goto loc_0033207D;
    goto loc_003323E0;
loc_00332401:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x5A0))) >> (12));
    local_rsi = (uint32_t)((local_rsi) & (7));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x220) + 0x2A0) == 0) goto loc_00332062;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x220) + 0x2A0) + 0x444))))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x220) + 0x2A0) + 0x444))); }
    goto loc_00332062;
loc_00332434:
    goto loc_00331F85;
loc_0033243F:
    if ((((uint8_t)(Arg4)) & (7)) == 0) goto loc_00331F85;
    goto loc_00331F85;
loc_00332454:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9465E)))) & (64)) == 0) goto loc_003323C0;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003323C0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    goto loc_003323C2;
loc_0033247C:
    if (local_rbx == 0) goto loc_0033251A;
    Arg1 = (Arg4) << (5);
    result = (Arg1) ^ (local_rbx);
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    goto loc_00331ED1;
loc_003324A0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC94612)))) & (64)) == 0) goto loc_003323F0;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003323F0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    goto loc_003323F2;
loc_003324C8:
    result = MiCanPfnOriginalPteBeLost(Arg1, *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    if ((uint32_t)(result) == 0) goto loc_003321BC;
    Arg1 = (uint8_t)((*(uint8_t *)(arg1 + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (4)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_003321BC;
    result = (*(uint64_t *)(arg1 + 0x10)) & (-5);
    *(uint64_t *)(arg1 + 0x10) = result;
    goto loc_003321BC;
loc_00332506:
    result = MiLockPageInline(Arg1, *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    v_stack_p90 = (uint8_t)(result);
    goto loc_0033208D;
loc_0033251A:
    result = MiMakeDemandZeroPte((uint32_t)(Arg4), *(uint64_t *)(v_rip + 0xAFB8FF), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    goto loc_00331ED1;
loc_00332527:
    if (v_stack_p88 < result) goto loc_003320C4;
    if (v_stack_p88 > result) goto loc_003320C4;
    result = MiIncreaseUsedPtesInPfn(local_rbp, 1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    goto loc_003320C4;
loc_0033256A:
    result = MiUnlockPage(Arg1, v_stack_p90, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
    goto loc_00332208;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg1` | `+ 0x23` | `8` | `R/W` |
| `Arg1` | `+ 0x24` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00331E60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
