# MiReplacePageTablePage

- RVA: `0x00229184`–`0x00229B4D` (길이 `2,505` bytes)
- VA: `0x0000000140229184`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FCE4`
- 디코드: `573`개 명령, `2,505/2,505` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00229270` → [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) (function, `0x00323270`)
- `0x002292AB` → [MiMakeProtectionPfnCompatible](MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x002292BE` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x002292FD` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002293FE` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002294B8` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00229516` → [MiReplaceActivePageTableLinks](MiReplaceActivePageTableLinks_function_00229B54.md) (function, `0x00229B54`)
- `0x0022968F` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002296C3` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0022977D` → [MiLockTransitionLeafPageEx](../40/MiLockTransitionLeafPageEx_function_00405884.md) (function, `0x00405884`)
- `0x00229791` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002297DA` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0022982C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022983C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022985C` → [MiIsPdeOrAboveAccessible](MiIsPdeOrAboveAccessible_function_00227A10.md) (function, `0x00227A10`)
- `0x0022989C` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0022996C` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002299AA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002299B9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002299D2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002299E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00229A07` → [MiCopyPfnEntryEx](../2B/MiCopyPfnEntryEx_function_002B2670.md) (function, `0x002B2670`)
- `0x00229A14` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x00229ABE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00229ACD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00229AE6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00229AF5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00229B0E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00229B1D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MmStealTopLevelPage](MmStealTopLevelPage_function_002281E0.md) at `0x00228230`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B372C`

### Static image references
- `0x002292C3` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00229419` → RVA `0x00E2DC80` (`.data`; read)
- `0x002294E9` → RVA `0x00010880` (`.rdata`; read)
- `0x00229559` → RVA `0x00E37478` (`.data`; read)
- `0x00229566` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0022969C` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0022980F` → RVA `0x00EF51DC` (`.data`; read/write)
- `0x0022981D` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00229869` → RVA `0x00EF51D8` (`.data`; read/write)
- `0x00229A9E` → RVA `0x00EF51D4` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00229184  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00229189  53                              push rbx
0022918A  55                              push rbp
0022918B  56                              push rsi
0022918C  57                              push rdi
0022918D  41 54                           push r12
0022918F  41 55                           push r13
00229191  41 56                           push r14
00229193  41 57                           push r15
00229195  48 81 EC 88 00 00 00            sub rsp, 0x88
0022919C  4C 8B 61 18                     mov r12, qword ptr [rcx + 0x18]
002291A0  4C 8B C1                        mov r8, rcx
002291A3  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
002291A7  33 ED                           xor ebp, ebp
002291A9  48 8B 59 20                     mov rbx, qword ptr [rcx + 0x20]
002291AD  4D 8B EC                        mov r13, r12
002291B0  C7 41 38 01 00 00 C0            mov dword ptr [rcx + 0x38], 0xc0000001
002291B7  4B 8D 3C 64                     lea rdi, [r12 + r12*2]
002291BB  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
002291C0  48 C1 E7 04                     shl rdi, 4
002291C4  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
002291C9  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
002291CE  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
002291D3  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
002291DD  48 8B C1                        mov rax, rcx
002291E0  48 03 F8                        add rdi, rax
002291E3  4C 8D 3C 5B                     lea r15, [rbx + rbx*2]
002291E7  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
002291EC  49 C1 E7 04                     shl r15, 4
002291F0  48 8B C1                        mov rax, rcx
002291F3  33 C9                           xor ecx, ecx
002291F5  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
002291FF  4C 03 F8                        add r15, rax
00229202  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
00229209  33 D2                           xor edx, edx
0022920B  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00229210  44 8D 55 01                     lea r10d, [rbp + 1]
00229214  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
0022921B  49 BB F8 FF FF FF 7F 00 00 00   movabs r11, 0x7ffffffff8
00229225  89 94 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edx
0022922C  49 BE FF FF FF FF FF 00 00 00   movabs r14, 0xffffffffff
00229236  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0022923A  45 39 50 40                     cmp dword ptr [r8 + 0x40], r10d
0022923E  0F 84 23 08 00 00               je 0x140229a67
00229244  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00229248  49 23 C6                        and rax, r14
0022924B  49 3B C4                        cmp rax, r12
0022924E  0F 84 22 07 00 00               je 0x140229976
00229254  21 54 24 24                     and dword ptr [rsp + 0x24], edx
00229258  49 8B 48 10                     mov rcx, qword ptr [r8 + 0x10]
0022925C  49 8B F1                        mov rsi, r9
0022925F  41 B9 04 00 00 00               mov r9d, 4
00229265  48 83 C1 60                     add rcx, 0x60
00229269  4D 8B C2                        mov r8, r10
0022926C  41 8D 51 FF                     lea edx, [r9 - 1]
00229270  E8 FB 9F 0F 00                  call 0x140323270
00229275  4C 8B F0                        mov r14, rax
00229278  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0022927D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00229287  49 C1 EE 09                     shr r14, 9
0022928B  4C 23 F0                        and r14, rax
0022928E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00229298  48 8B D0                        mov rdx, rax
0022929B  4C 03 F2                        add r14, rdx
0022929E  B9 04 00 00 00                  mov ecx, 4
002292A3  49 8B D7                        mov rdx, r15
002292A6  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
002292AB  E8 20 0A 00 00                  call 0x140229cd0
002292B0  0D 00 00 00 A0                  or eax, 0xa0000000
002292B5  48 8B D3                        mov rdx, rbx
002292B8  44 8B C0                        mov r8d, eax
002292BB  49 8B CE                        mov rcx, r14
002292BE  E8 CD C2 09 00                  call 0x1402c5590
002292C3  48 0F BA 25 BC D7 D9 00 24      bt qword ptr [rip + 0xd9d7bc], 0x24
002292CC  48 8B D8                        mov rbx, rax
002292CF  0F 82 5F 06 00 00               jb 0x140229934
002292D5  4B 8D 0C 64                     lea rcx, [r12 + r12*2]
002292D9  49 89 1E                        mov qword ptr [r14], rbx
002292DC  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
002292E1  48 C1 E1 04                     shl rcx, 4
002292E5  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002292EF  48 8B C0                        mov rax, rax
002292F2  48 03 C8                        add rcx, rax
002292F5  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002292FA  48 8B CE                        mov rcx, rsi
002292FD  E8 9E 95 05 00                  call 0x1402828a0
00229302  41 BB 01 00 00 00               mov r11d, 1
00229308  48 8B D0                        mov rdx, rax
0022930B  49 BC FF FF FF FF FF FF FF 7F   movabs r12, 0x7fffffffffffffff
00229315  41 84 C3                        test r11b, al
00229318  0F 85 1E 02 00 00               jne 0x14022953c
0022931E  25 00 0C 00 00                  and eax, 0xc00
00229323  48 3D 00 08 00 00               cmp rax, 0x800
00229329  0F 84 11 04 00 00               je 0x140229740
0022932F  4C 3B 6C 24 30                  cmp r13, qword ptr [rsp + 0x30]
00229334  0F 85 90 02 00 00               jne 0x1402295ca
0022933A  49 89 16                        mov qword ptr [r14], rdx
0022933D  48 83 C6 08                     add rsi, 8
00229341  49 83 C6 08                     add r14, 8
00229345  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
0022934C  75 AC                           jne 0x1402292fa
0022934E  33 DB                           xor ebx, ebx
00229350  41 B5 40                        mov r13b, 0x40
00229353  85 ED                           test ebp, ebp
00229355  0F 85 AA 05 00 00               jne 0x140229905
0022935B  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
00229362  0F 82 88 03 00 00               jb 0x1402296f0
00229368  83 7C 24 24 00                  cmp dword ptr [rsp + 0x24], 0
0022936D  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
00229371  0F 84 6D 04 00 00               je 0x1402297e4
00229377  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0022937A  66 41 3B C3                     cmp ax, r11w
0022937E  0F 85 8B 04 00 00               jne 0x14022980f
00229384  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00229388  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00229392  48 23 C1                        and rax, rcx
00229395  48 3D 00 00 01 00               cmp rax, 0x10000
0022939B  0F 83 6E 04 00 00               jae 0x14022980f
002293A1  33 F6                           xor esi, esi
002293A3  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002293AA  0F 82 1A 03 00 00               jb 0x1402296ca
002293B0  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002293B4  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
002293BE  48 33 C3                        xor rax, rbx
002293C1  4D 8B F4                        mov r14, r12
002293C4  48 23 C1                        and rax, rcx
002293C7  48 33 C3                        xor rax, rbx
002293CA  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
002293CE  F0 4D 21 77 18                  lock and qword ptr [r15 + 0x18], r14
002293D3  F0 4C 21 77 18                  lock and qword ptr [rdi + 0x18], r14
002293D8  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
002293DD  41 83 CC FF                     or r12d, 0xffffffff
002293E1  48 8B F0                        mov rsi, rax
002293E4  85 ED                           test ebp, ebp
002293E6  0F 84 A6 00 00 00               je 0x140229492
002293EC  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
002293F1  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
002293F6  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
002293FB  48 8B CE                        mov rcx, rsi
002293FE  E8 9D 94 05 00                  call 0x1402828a0
00229403  A8 01                           test al, 1
00229405  75 6D                           jne 0x140229474
00229407  48 8B C8                        mov rcx, rax
0022940A  81 E1 00 0C 00 00               and ecx, 0xc00
00229410  48 81 F9 00 08 00 00            cmp rcx, 0x800
00229417  75 5B                           jne 0x140229474
00229419  48 8B 0D 60 48 C0 00            mov rcx, qword ptr [rip + 0xc04860]
00229420  48 85 C9                        test rcx, rcx
00229423  74 0E                           je 0x140229433
00229425  A8 10                           test al, 0x10
00229427  0F 85 0A 03 00 00               jne 0x140229737
0022942D  48 F7 D1                        not rcx
00229430  48 23 C1                        and rax, rcx
00229433  48 C1 E8 0C                     shr rax, 0xc
00229437  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00229441  48 23 C1                        and rax, rcx
00229444  48 8D 1C 40                     lea rbx, [rax + rax*2]
00229448  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00229452  48 C1 E3 04                     shl rbx, 4
00229456  48 8B C0                        mov rax, rax
00229459  48 03 D8                        add rbx, rax
0022945C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00229460  48 23 C1                        and rax, rcx
00229463  49 3B C7                        cmp rax, r15
00229466  0F 84 5F 03 00 00               je 0x1402297cb
0022946C  41 03 EC                        add ebp, r12d
0022946F  F0 4C 21 73 18                  lock and qword ptr [rbx + 0x18], r14
00229474  48 83 C6 08                     add rsi, 8
00229478  85 ED                           test ebp, ebp
0022947A  0F 85 7B FF FF FF               jne 0x1402293fb
00229480  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00229485  41 B5 40                        mov r13b, 0x40
00229488  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0022948D  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00229492  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00229499  85 F6                           test esi, esi
0022949B  74 42                           je 0x1402294df
0022949D  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
002294A2  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
002294A7  48 2B C5                        sub rax, rbp
002294AA  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
002294AF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002294B4  48 8D 0C 28                     lea rcx, [rax + rbp]
002294B8  E8 E3 93 05 00                  call 0x1402828a0
002294BD  48 8B D8                        mov rbx, rax
002294C0  A8 01                           test al, 1
002294C2  0F 85 14 01 00 00               jne 0x1402295dc
002294C8  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
002294CD  48 83 C5 08                     add rbp, 8
002294D1  85 F6                           test esi, esi
002294D3  75 DF                           jne 0x1402294b4
002294D5  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002294DA  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
002294DF  83 7C 24 24 00                  cmp dword ptr [rsp + 0x24], 0
002294E4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002294E9  48 8B 05 90 73 DE FF            mov rax, qword ptr [rip - 0x218c70]
002294F0  48 89 01                        mov qword ptr [rcx], rax
002294F3  0F 85 F2 04 00 00               jne 0x1402299eb
002294F9  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
002294FE  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
00229502  0F BA E0 1A                     bt eax, 0x1a
00229506  73 13                           jae 0x14022951b
00229508  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00229510  49 8B D7                        mov rdx, r15
00229513  48 8B 08                        mov rcx, qword ptr [rax]
00229516  E8 39 06 00 00                  call 0x140229b54
0022951B  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00229523  83 60 38 00                     and dword ptr [rax + 0x38], 0
00229527  48 81 C4 88 00 00 00            add rsp, 0x88
0022952E  41 5F                           pop r15
00229530  41 5E                           pop r14
00229532  41 5D                           pop r13
00229534  41 5C                           pop r12
00229536  5F                              pop rdi
00229537  5E                              pop rsi
00229538  5D                              pop rbp
00229539  5B                              pop rbx
0022953A  C3                              ret
0022953B  CC                              int3
0022953C  44 01 9C 24 D8 00 00 00         add dword ptr [rsp + 0xd8], r11d
00229544  84 C0                           test al, al
00229546  78 53                           js 0x14022959b
00229548  48 C1 E8 0C                     shr rax, 0xc
0022954C  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00229556  48 23 C1                        and rax, rcx
00229559  48 3B 05 18 DF C0 00            cmp rax, qword ptr [rip + 0xc0df18]
00229560  0F 84 DA 05 00 00               je 0x140229b40
00229566  48 3B 05 73 47 C0 00            cmp rax, qword ptr [rip + 0xc04773]
0022956D  77 34                           ja 0x1402295a3
0022956F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00229573  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0022957D  48 03 C9                        add rcx, rcx
00229580  4C 8B C0                        mov r8, rax
00229583  49 8B 04 C8                     mov rax, qword ptr [r8 + rcx*8]
00229587  48 C1 E8 36                     shr rax, 0x36
0022958B  41 85 C3                        test r11d, eax
0022958E  74 13                           je 0x1402295a3
00229590  49 8B 04 C8                     mov rax, qword ptr [r8 + rcx*8]
00229594  48 0F BA E0 28                  bt rax, 0x28
00229599  73 08                           jae 0x1402295a3
0022959B  44 01 9C 24 E0 00 00 00         add dword ptr [rsp + 0xe0], r11d
002295A3  4C 3B 6C 24 30                  cmp r13, qword ptr [rsp + 0x30]
002295A8  0F 84 8C FD FF FF               je 0x14022933a
002295AE  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
002295B6  48 8B C6                        mov rax, rsi
002295B9  48 2B 44 24 28                  sub rax, qword ptr [rsp + 0x28]
002295BE  48 C1 F8 03                     sar rax, 3
002295C2  48 8B 51 48                     mov rdx, qword ptr [rcx + 0x48]
002295C6  48 8B 14 C2                     mov rdx, qword ptr [rdx + rax*8]
002295CA  8A C2                           mov al, dl
002295CC  41 22 C3                        and al, r11b
002295CF  F6 D8                           neg al
002295D1  48 1B C0                        sbb rax, rax
002295D4  48 23 D0                        and rdx, rax
002295D7  E9 5E FD FF FF                  jmp 0x14022933a
002295DC  41 03 F4                        add esi, r12d
002295DF  48 8B C8                        mov rcx, rax
002295E2  48 C1 E9 0C                     shr rcx, 0xc
002295E6  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
002295F0  49 23 C8                        and rcx, r8
002295F3  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
002295FA  48 3B 0D DF 46 C0 00            cmp rcx, qword ptr [rip + 0xc046df]
00229601  77 70                           ja 0x140229673
00229603  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00229607  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00229611  48 03 D2                        add rdx, rdx
00229614  48 8B C0                        mov rax, rax
00229617  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0022961B  48 C1 E8 36                     shr rax, 0x36
0022961F  0F BA E0 00                     bt eax, 0
00229623  73 4E                           jae 0x140229673
00229625  49 3B CF                        cmp rcx, r15
00229628  74 49                           je 0x140229673
0022962A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00229634  48 8B C0                        mov rax, rax
00229637  48 8D 34 D0                     lea rsi, [rax + rdx*8]
0022963B  45 33 F6                        xor r14d, r14d
0022963E  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00229645  72 52                           jb 0x140229699
00229647  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0022964B  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00229655  48 23 C1                        and rax, rcx
00229658  49 3B C7                        cmp rax, r15
0022965B  74 59                           je 0x1402296b6
0022965D  49 BE FF FF FF FF FF FF FF 7F   movabs r14, 0x7fffffffffffffff
00229667  F0 4C 21 76 18                  lock and qword ptr [rsi + 0x18], r14
0022966C  8B B4 24 D8 00 00 00            mov esi, dword ptr [rsp + 0xd8]
00229673  4C 3B FF                        cmp r15, rdi
00229676  0F 85 9A 00 00 00               jne 0x140229716
0022967C  F6 C3 01                        test bl, 1
0022967F  0F 84 43 FE FF FF               je 0x1402294c8
00229685  48 83 CB 20                     or rbx, 0x20
00229689  48 8B CD                        mov rcx, rbp
0022968C  48 8B D3                        mov rdx, rbx
0022968F  E8 7C 81 05 00                  call 0x140281810
00229694  E9 2F FE FF FF                  jmp 0x1402294c8
00229699  41 FF C6                        inc r14d
0022969C  44 85 35 09 BC D9 00            test dword ptr [rip + 0xd9bc09], r14d
002296A3  0F 84 74 01 00 00               je 0x14022981d
002296A9  F3 90                           pause
002296AB  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002296AF  48 85 C0                        test rax, rax
002296B2  79 8A                           jns 0x14022963e
002296B4  EB E3                           jmp 0x140229699
002296B6  4C 3B FF                        cmp r15, rdi
002296B9  75 A2                           jne 0x14022965d
002296BB  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002296C0  48 8B CE                        mov rcx, rsi
002296C3  E8 F8 A8 13 00                  call 0x140363fc0
002296C8  EB 93                           jmp 0x14022965d
002296CA  41 03 F3                        add esi, r11d
002296CD  85 35 D9 BB D9 00               test dword ptr [rip + 0xd9bbd9], esi
002296D3  0F 84 C2 02 00 00               je 0x14022999b
002296D9  F3 90                           pause
002296DB  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002296DF  41 BB 01 00 00 00               mov r11d, 1
002296E5  48 85 C0                        test rax, rax
002296E8  0F 89 B5 FC FF FF               jns 0x1402293a3
002296EE  EB DA                           jmp 0x1402296ca
002296F0  41 03 DB                        add ebx, r11d
002296F3  85 1D B3 BB D9 00               test dword ptr [rip + 0xd9bbb3], ebx
002296F9  0F 84 C4 02 00 00               je 0x1402299c3
002296FF  F3 90                           pause
00229701  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00229705  41 BB 01 00 00 00               mov r11d, 1
0022970B  48 85 C0                        test rax, rax
0022970E  0F 89 47 FC FF FF               jns 0x14022935b
00229714  EB DA                           jmp 0x1402296f0
00229716  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0022971E  48 8B C5                        mov rax, rbp
00229721  48 2B 44 24 40                  sub rax, qword ptr [rsp + 0x40]
00229726  48 C1 F8 03                     sar rax, 3
0022972A  48 8B 59 48                     mov rbx, qword ptr [rcx + 0x48]
0022972E  48 8B 1C C3                     mov rbx, qword ptr [rbx + rax*8]
00229732  E9 45 FF FF FF                  jmp 0x14022967c
00229737  48 83 E0 EF                     and rax, 0xffffffffffffffef
0022973B  E9 F3 FC FF FF                  jmp 0x140229433
00229740  45 33 D2                        xor r10d, r10d
00229743  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0022974D  85 ED                           test ebp, ebp
0022974F  48 8B CE                        mov rcx, rsi
00229752  41 0F 95 C2                     setne r10b
00229756  48 C1 E1 19                     shl rcx, 0x19
0022975A  48 8B C2                        mov rax, rdx
0022975D  48 C1 E0 19                     shl rax, 0x19
00229761  48 2B C8                        sub rcx, rax
00229764  48 C1 F9 10                     sar rcx, 0x10
00229768  48 8B C2                        mov rax, rdx
0022976B  48 3B C8                        cmp rcx, rax
0022976E  0F 83 D2 00 00 00               jae 0x140229846
00229774  45 33 C0                        xor r8d, r8d
00229777  49 8B D2                        mov rdx, r10
0022977A  48 8B CE                        mov rcx, rsi
0022977D  E8 02 C1 1D 00                  call 0x140405884
00229782  48 8B D8                        mov rbx, rax
00229785  48 85 C0                        test rax, rax
00229788  0F 84 6C FB FF FF               je 0x1402292fa
0022978E  48 8B CE                        mov rcx, rsi
00229791  E8 0A 91 05 00                  call 0x1402828a0
00229796  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0022979A  48 8B D0                        mov rdx, rax
0022979D  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002297A7  41 BB 01 00 00 00               mov r11d, 1
002297AD  48 23 C8                        and rcx, rax
002297B0  49 3B CD                        cmp rcx, r13
002297B3  0F 85 6E 03 00 00               jne 0x140229b27
002297B9  F6 43 22 20                     test byte ptr [rbx + 0x22], 0x20
002297BD  0F 85 DB 02 00 00               jne 0x140229a9e
002297C3  41 03 EB                        add ebp, r11d
002297C6  E9 64 FB FF FF                  jmp 0x14022932f
002297CB  4C 3B FF                        cmp r15, rdi
002297CE  0F 85 98 FC FF FF               jne 0x14022946c
002297D4  49 8B D5                        mov rdx, r13
002297D7  48 8B CB                        mov rcx, rbx
002297DA  E8 E1 A7 13 00                  call 0x140363fc0
002297DF  E9 88 FC FF FF                  jmp 0x14022946c
002297E4  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
002297EB  8B C5                           mov eax, ebp
002297ED  2B 84 24 E8 00 00 00            sub eax, dword ptr [rsp + 0xe8]
002297F4  FF C1                           inc ecx
002297F6  2B 44 24 20                     sub eax, dword ptr [rsp + 0x20]
002297FA  2B 84 24 E0 00 00 00            sub eax, dword ptr [rsp + 0xe0]
00229801  03 C8                           add ecx, eax
00229803  0F B7 C3                        movzx eax, bx
00229806  48 3B C1                        cmp rax, rcx
00229809  0F 84 68 FB FF FF               je 0x140229377
0022980F  44 01 1D C6 B9 CC 00            add dword ptr [rip + 0xccb9c6], r11d
00229816  F0 4C 21 67 18                  lock and qword ptr [rdi + 0x18], r12
0022981B  EB 53                           jmp 0x140229870
0022981D  8B 05 95 D2 D9 00               mov eax, dword ptr [rip + 0xd9d295]
00229823  41 84 C5                        test r13b, al
00229826  0F 84 7D FE FF FF               je 0x1402296a9
0022982C  E8 5F 5C 0E 00                  call 0x14030f490
00229831  84 C0                           test al, al
00229833  0F 84 70 FE FF FF               je 0x1402296a9
00229839  41 8B CE                        mov ecx, r14d
0022983C  E8 1F 5C 0E 00                  call 0x14030f460
00229841  E9 65 FE FF FF                  jmp 0x1402296ab
00229846  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00229850  48 3B C8                        cmp rcx, rax
00229853  0F 87 1B FF FF FF               ja 0x140229774
00229859  48 8B CE                        mov rcx, rsi
0022985C  E8 AF E1 FF FF                  call 0x140227a10
00229861  85 C0                           test eax, eax
00229863  0F 85 0B FF FF FF               jne 0x140229774
00229869  44 01 1D 68 B9 CC 00            add dword ptr [rip + 0xccb968], r11d
00229870  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00229875  48 8B 05 04 70 DE FF            mov rax, qword ptr [rip - 0x218ffc]
0022987C  48 89 01                        mov qword ptr [rcx], rax
0022987F  85 ED                           test ebp, ebp
00229881  0F 84 A0 FC FF FF               je 0x140229527
00229887  41 83 CC FF                     or r12d, 0xffffffff
0022988B  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
00229895  48 83 EE 08                     sub rsi, 8
00229899  48 8B CE                        mov rcx, rsi
0022989C  E8 FF 8F 05 00                  call 0x1402828a0
002298A1  A8 01                           test al, 1
002298A3  75 56                           jne 0x1402298fb
002298A5  48 8B C8                        mov rcx, rax
002298A8  81 E1 00 0C 00 00               and ecx, 0xc00
002298AE  48 81 F9 00 08 00 00            cmp rcx, 0x800
002298B5  75 44                           jne 0x1402298fb
002298B7  48 8B 0D C2 43 C0 00            mov rcx, qword ptr [rip + 0xc043c2]
002298BE  48 85 C9                        test rcx, rcx
002298C1  74 0E                           je 0x1402298d1
002298C3  A8 10                           test al, 0x10
002298C5  0F 85 5D 01 00 00               jne 0x140229a28
002298CB  48 F7 D1                        not rcx
002298CE  48 23 C1                        and rax, rcx
002298D1  48 C1 E8 0C                     shr rax, 0xc
002298D5  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002298DF  48 23 C1                        and rax, rcx
002298E2  41 03 EC                        add ebp, r12d
002298E5  48 8D 0C 40                     lea rcx, [rax + rax*2]
002298E9  48 03 C9                        add rcx, rcx
002298EC  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
002298F6  F0 48 21 1C C8                  lock and qword ptr [rax + rcx*8], rbx
002298FB  85 ED                           test ebp, ebp
002298FD  0F 84 24 FC FF FF               je 0x140229527
00229903  EB 90                           jmp 0x140229895
00229905  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022990C  0F 83 56 FA FF FF               jae 0x140229368
00229912  41 03 DB                        add ebx, r11d
00229915  85 1D 91 B9 D9 00               test dword ptr [rip + 0xd9b991], ebx
0022991B  0F 84 8E 01 00 00               je 0x140229aaf
00229921  F3 90                           pause
00229923  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00229927  41 BB 01 00 00 00               mov r11d, 1
0022992D  48 85 C0                        test rax, rax
00229930  79 D3                           jns 0x140229905
00229932  EB DE                           jmp 0x140229912
00229934  F6 C3 20                        test bl, 0x20
00229937  0F 85 98 F9 FF FF               jne 0x1402292d5
0022993D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00229947  48 8B C0                        mov rax, rax
0022994A  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00229954  48 03 C1                        add rax, rcx
00229957  4C 3B F0                        cmp r14, rax
0022995A  0F 82 75 F9 FF FF               jb 0x1402292d5
00229960  41 B8 80 00 00 00               mov r8d, 0x80
00229966  48 8B D3                        mov rdx, rbx
00229969  49 8B CE                        mov rcx, r14
0022996C  E8 0F 94 06 00                  call 0x140292d80
00229971  E9 5F F9 FF FF                  jmp 0x1402292d5
00229976  44 89 54 24 24                  mov dword ptr [rsp + 0x24], r10d
0022997B  45 39 50 40                     cmp dword ptr [r8 + 0x40], r10d
0022997F  0F 85 D3 F8 FF FF               jne 0x140229258
00229985  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00229989  4C 8B 68 28                     mov r13, qword ptr [rax + 0x28]
0022998D  49 C1 ED 0C                     shr r13, 0xc
00229991  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00229996  E9 BD F8 FF FF                  jmp 0x140229258
0022999B  8B 05 17 D1 D9 00               mov eax, dword ptr [rip + 0xd9d117]
002299A1  41 84 C5                        test r13b, al
002299A4  0F 84 2F FD FF FF               je 0x1402296d9
002299AA  E8 E1 5A 0E 00                  call 0x14030f490
002299AF  84 C0                           test al, al
002299B1  0F 84 22 FD FF FF               je 0x1402296d9
002299B7  8B CE                           mov ecx, esi
002299B9  E8 A2 5A 0E 00                  call 0x14030f460
002299BE  E9 18 FD FF FF                  jmp 0x1402296db
002299C3  8B 05 EF D0 D9 00               mov eax, dword ptr [rip + 0xd9d0ef]
002299C9  41 84 C5                        test r13b, al
002299CC  0F 84 2D FD FF FF               je 0x1402296ff
002299D2  E8 B9 5A 0E 00                  call 0x14030f490
002299D7  84 C0                           test al, al
002299D9  0F 84 20 FD FF FF               je 0x1402296ff
002299DF  8B CB                           mov ecx, ebx
002299E1  E8 7A 5A 0E 00                  call 0x14030f460
002299E6  E9 16 FD FF FF                  jmp 0x140229701
002299EB  33 DB                           xor ebx, ebx
002299ED  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002299F4  72 3B                           jb 0x140229a31
002299F6  33 DB                           xor ebx, ebx
002299F8  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002299FF  72 4B                           jb 0x140229a4c
00229A01  48 8B D7                        mov rdx, rdi
00229A04  49 8B CF                        mov rcx, r15
00229A07  E8 64 8C 08 00                  call 0x1402b2670
00229A0C  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00229A11  49 8B CF                        mov rcx, r15
00229A14  E8 A7 A5 13 00                  call 0x140363fc0
00229A19  F0 4D 21 77 18                  lock and qword ptr [r15 + 0x18], r14
00229A1E  F0 4C 21 77 18                  lock and qword ptr [rdi + 0x18], r14
00229A23  E9 D1 FA FF FF                  jmp 0x1402294f9
00229A28  48 83 E0 EF                     and rax, 0xffffffffffffffef
00229A2C  E9 A0 FE FF FF                  jmp 0x1402298d1
00229A31  FF C3                           inc ebx
00229A33  85 1D 73 B8 D9 00               test dword ptr [rip + 0xd9b873], ebx
00229A39  0F 84 98 00 00 00               je 0x140229ad7
00229A3F  F3 90                           pause
00229A41  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00229A45  48 85 C0                        test rax, rax
00229A48  79 A3                           jns 0x1402299ed
00229A4A  EB E5                           jmp 0x140229a31
00229A4C  FF C3                           inc ebx
00229A4E  85 1D 58 B8 D9 00               test dword ptr [rip + 0xd9b858], ebx
00229A54  0F 84 A5 00 00 00               je 0x140229aff
00229A5A  F3 90                           pause
00229A5C  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00229A60  48 85 C0                        test rax, rax
00229A63  79 93                           jns 0x1402299f8
00229A65  EB E5                           jmp 0x140229a4c
00229A67  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
00229A6B  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00229A72  48 85 C9                        test rcx, rcx
00229A75  0F 84 AC FA FF FF               je 0x140229527
00229A7B  48 C1 E9 09                     shr rcx, 9
00229A7F  49 23 CB                        and rcx, r11
00229A82  48 8B C6                        mov rax, rsi
00229A85  48 8B 04 01                     mov rax, qword ptr [rcx + rax]
00229A89  48 C1 E8 0C                     shr rax, 0xc
00229A8D  49 23 C6                        and rax, r14
00229A90  49 3B C4                        cmp rax, r12
00229A93  0F 84 AB F7 FF FF               je 0x140229244
00229A99  E9 89 FA FF FF                  jmp 0x140229527
00229A9E  44 01 1D 2F B7 CC 00            add dword ptr [rip + 0xccb72f], r11d
00229AA5  F0 4C 21 63 18                  lock and qword ptr [rbx + 0x18], r12
00229AAA  E9 C1 FD FF FF                  jmp 0x140229870
00229AAF  8B 05 03 D0 D9 00               mov eax, dword ptr [rip + 0xd9d003]
00229AB5  41 84 C5                        test r13b, al
00229AB8  0F 84 63 FE FF FF               je 0x140229921
00229ABE  E8 CD 59 0E 00                  call 0x14030f490
00229AC3  84 C0                           test al, al
00229AC5  0F 84 56 FE FF FF               je 0x140229921
00229ACB  8B CB                           mov ecx, ebx
00229ACD  E8 8E 59 0E 00                  call 0x14030f460
00229AD2  E9 4C FE FF FF                  jmp 0x140229923
00229AD7  8B 05 DB CF D9 00               mov eax, dword ptr [rip + 0xd9cfdb]
00229ADD  41 84 C5                        test r13b, al
00229AE0  0F 84 59 FF FF FF               je 0x140229a3f
00229AE6  E8 A5 59 0E 00                  call 0x14030f490
00229AEB  84 C0                           test al, al
00229AED  0F 84 4C FF FF FF               je 0x140229a3f
00229AF3  8B CB                           mov ecx, ebx
00229AF5  E8 66 59 0E 00                  call 0x14030f460
00229AFA  E9 42 FF FF FF                  jmp 0x140229a41
00229AFF  8B 05 B3 CF D9 00               mov eax, dword ptr [rip + 0xd9cfb3]
00229B05  41 84 C5                        test r13b, al
00229B08  0F 84 4C FF FF FF               je 0x140229a5a
00229B0E  E8 7D 59 0E 00                  call 0x14030f490
00229B13  84 C0                           test al, al
00229B15  0F 84 3F FF FF FF               je 0x140229a5a
00229B1B  8B CB                           mov ecx, ebx
00229B1D  E8 3E 59 0E 00                  call 0x14030f460
00229B22  E9 35 FF FF FF                  jmp 0x140229a5c
00229B27  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00229B2B  48 0F BA E0 28                  bt rax, 0x28
00229B30  0F 83 83 FC FF FF               jae 0x1402297b9
00229B36  44 01 5C 24 20                  add dword ptr [rsp + 0x20], r11d
00229B3B  E9 79 FC FF FF                  jmp 0x1402297b9
00229B40  44 01 9C 24 E8 00 00 00         add dword ptr [rsp + 0xe8], r11d
00229B48  E9 56 FA FF FF                  jmp 0x1402295a3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReplacePageTablePage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned int v_stack_pE8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    v_rbp = 0;
    *(unsigned int *)(a1 + 56) = 0xC0000001ULL;
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 8);
    v_rdi = (*(unsigned __int64 *)(a1 + 24) + *(unsigned __int64 *)(a1 + 24) * 2) << (4);
    v_stack_m98 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m80 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m90 = *(unsigned __int64 *)(a1 + 24);
    v_rdi = (v_rdi) + (a1);
    v_stack_m70 = v_rdi;
    v_r15 = (*(unsigned __int64 *)(a1 + 32) + *(unsigned __int64 *)(a1 + 32) * 2) << (4);
    a1 = 0;
    v_r15 = (v_r15) + (0);
    v_stack_p10 = 0;
    a2 = 0;
    v_stack_m78 = v_r15;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_mA8 = 0;
    if ((*(unsigned int *)(a1 + 64)) == ((unsigned int)(v_rbp + 1))) goto loc_00229A67;
loc_00229244:
    result = (*(unsigned __int64 *)(v_rdi + 40)) & (v_r14);
    if (result == (*(unsigned __int64 *)(a1 + 24))) goto loc_00229976;
loc_00229258:
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (96);
    result = MiGetUltraMapping(a1, 4 - 1, v_rbp + 1, 4);
    v_stack_m88 = result;
    v_r14 = (result) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (result);
    v_stack_m68 = v_r14;
    result = MiMakeProtectionPfnCompatible(4, v_r15, v_rbp + 1, 4);
    result = (unsigned int)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(v_r14, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(result)), 4);
    if (condition_is_below) goto loc_00229934;
loc_002292D5:
    *(unsigned __int64 *)(v_r14) = result;
    a1 = (*(unsigned __int64 *)(a1 + 24) + *(unsigned __int64 *)(a1 + 24) * 2) << (4);
    a1 = (a1) + (result);
    v_stack_m58 = a1;
loc_002292FA:
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(result)), 4);
    if (((1) & ((unsigned __int8)(result))) != 0) goto loc_0022953C;
    result = (unsigned int)((result) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_00229740;
loc_0022932F:
    if ((*(unsigned __int64 *)(a1 + 24)) != v_stack_m98) goto loc_002295CA;
loc_0022933A:
    *(unsigned __int64 *)(v_stack_m88) = result;
    v_rsi = (*(unsigned __int64 *)(a1 + 8)) + (8);
    v_r14 = (v_stack_m88) + (8);
    if (((v_rsi) & (0xFFFULL)) != 0) goto loc_002292FA;
    v_rbx = 0;
    if (0 != 0) goto loc_00229905;
loc_0022935B:
    if (condition_is_below) goto loc_002296F0;
loc_00229368:
    if (v_stack_mA4 == 0) goto loc_002297E4;
loc_00229377:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rdi + 32)))) != 1) goto loc_0022980F;
    result = (*(unsigned __int64 *)(v_rdi + 24)) & (*(unsigned __int64 *)(a1 + 8));
    if (result >= 0x10000ULL) goto loc_0022980F;
    v_rsi = 0;
loc_002293A3:
    if (condition_is_below) goto loc_002296CA;
    result = (*(unsigned __int64 *)(v_r15 + 24)) ^ (*(unsigned __int64 *)(v_rdi + 24));
    result = (result) & (*(unsigned __int64 *)(a1 + 8));
    result = (result) ^ (*(unsigned __int64 *)(v_rdi + 24));
    *(unsigned __int64 *)(v_r15 + 24) = result;
    v_r12 = (unsigned int)((*(unsigned __int64 *)(a1 + 24)) | (0xFFFFFFFFULL));
    if (0 == 0) goto loc_00229492;
loc_002293FB:
    result = MI_READ_PTE_LOCK_FREE(v_stack_mA0, result, (unsigned int)((unsigned int)(result)), 4);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00229474;
    a1 = (unsigned int)((result) & (0xC00ULL));
    if (a1 != 0x800ULL) goto loc_00229474;
    if (*(unsigned __int64 *)(v_rip + 12601440) == 0) goto loc_00229433;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00229737;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12601440));
    result = (result) & (a1);
loc_00229433:
    result = (result) >> (12);
    result = (result) & (a1);
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    result = (*(unsigned __int64 *)(v_rbx + 40)) & (a1);
    if (result == v_stack_m90) goto loc_002297CB;
loc_0022946C:
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(v_r12)));
loc_00229474:
    v_rsi = (v_stack_mA0) + (8);
    if ((unsigned int)(v_rbp) != 0) goto loc_002293FB;
loc_00229492:
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_002294DF;
    result = (v_stack_mA0) - (v_stack_m88);
    v_stack_mA0 = result;
loc_002294B4:
    result = MI_READ_PTE_LOCK_FREE(result + v_stack_m88 * 1, result, (unsigned int)((unsigned int)(result)), 4);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002295DC;
loc_002294C8:
    v_rbp = (v_stack_m88) + (8);
    if ((unsigned int)((unsigned int)(v_stack_p10)) != 0) goto loc_002294B4;
loc_002294DF:
    *(unsigned __int64 *)(v_stack_m68) = *(unsigned __int64 *)(v_rip - 2198640);
    if (v_stack_mA4 != 0) goto loc_002299EB;
loc_002294F9:
    result = (unsigned int)(*(unsigned int *)(v_stack_m58 + 36));
    if (v_stack_mA4 < 0) {
        result = v_stack_p8;
        a2 = v_stack_m78;
        a1 = *(unsigned __int64 *)(result);
        result = MiReplaceActivePageTableLinks(a1, a2, v_stack_m58, 4);
    }
loc_00229527:
    v_rsp = (v_rsp) + (136);
    return v_stack_p8;
loc_0022953C:
    if (sign_flag) goto loc_0022959B;
    result = (v_stack_p8) >> (12);
    result = (result) & (a1);
    if (result == (*(unsigned __int64 *)(v_rip + 12640024))) goto loc_00229B40;
    if (result > (*(unsigned __int64 *)(v_rip + 12601203))) goto loc_002295A3;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (((1) & ((unsigned int)(result))) == 0) goto loc_002295A3;
    if (!(condition_is_above_or_equal)) {
    }
    if (64 == v_stack_p30) goto loc_0022933A;
    result = ((unsigned int)(v_stack_p10)) - (v_stack_p28);
    result = (result) >> (3);
loc_002295CA:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 72) + result * 8))) & (1));
    result = (unsigned __int8)(-(result));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 72) + result * 8)) & (result);
    goto loc_0022933A;
loc_002295DC:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p10)) + ((unsigned int)(v_r12)));
    a1 = (result) >> (12);
    a1 = (a1) & (result);
    v_stack_pD8 = (unsigned int)(v_rsi);
    if (a1 > (*(unsigned __int64 *)(v_rip + 12601055))) goto loc_00229673;
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    result = (*(unsigned __int64 *)(result + a2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00229673;
    if (a1 == v_stack_m78) goto loc_00229673;
    v_r14 = 0;
loc_0022963E:
    if (condition_is_below) goto loc_00229699;
    result = (*(unsigned __int64 *)(result + a2 * 8 + 40)) & (a1);
    if (result == v_stack_m78) goto loc_002296B6;
loc_0022965D:
loc_00229673:
    if (v_stack_m78 != v_stack_m70) goto loc_00229716;
loc_0022967C:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002294C8;
    v_rbx = (result) | (32);
    result = MiWriteValidPteNewProtection(v_rbp, v_rbx, result, 4);
    goto loc_002294C8;
loc_00229699:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14269449)) & ((unsigned int)(v_r14))) == 0) goto loc_0022981D;
loc_002296A9:
loc_002296AB:
    if (!sign_flag) goto loc_0022963E;
    goto loc_00229699;
loc_002296B6:
    if (v_stack_m78 != v_stack_m70) goto loc_0022965D;
    result = MiSetPfnContainingFrame((unsigned int)(v_stack_pD8), v_stack_p48, result, 4);
    goto loc_0022965D;
loc_002296CA:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_pD8)) + (1));
    if (((*(unsigned int *)(v_rip + 14269401)) & ((unsigned int)(v_rsi))) == 0) goto loc_0022999B;
loc_002296D9:
loc_002296DB:
    if (!sign_flag) goto loc_002293A3;
    goto loc_002296CA;
loc_002296F0:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((*(unsigned int *)(v_rip + 14269363)) & ((unsigned int)(v_rbx))) == 0) goto loc_002299C3;
loc_002296FF:
loc_00229701:
    if (!sign_flag) goto loc_0022935B;
    goto loc_002296F0;
loc_00229716:
    result = (v_rbp) - (v_stack_p40);
    result = (result) >> (3);
    goto loc_0022967C;
loc_00229737:
    result = (result) & (-17);
    goto loc_00229433;
loc_00229740:
    v_r10 = 0;
    v_r10 = ((unsigned int)(v_rbp) != 0) ? 1 : 0;
    a1 = (v_rsi) << (25);
    result = (v_stack_p48) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    if (a1 >= v_stack_p48) goto loc_00229846;
loc_00229774:
    a3 = 0;
    result = MiLockTransitionLeafPageEx(v_rsi, v_r10, a3, 4);
    if (result == 0) goto loc_002292FA;
    result = MI_READ_PTE_LOCK_FREE(v_rsi, v_r10, a3, 4);
    a1 = (*(unsigned __int64 *)(result + 40)) & (result);
    if (a1 != 64) goto loc_00229B27;
loc_002297B9:
    if (((*(unsigned __int8 *)(result + 34)) & (32)) != 0) goto loc_00229A9E;
    v_rbp = (unsigned int)((v_rbp) + (1));
    goto loc_0022932F;
loc_002297CB:
    if (v_stack_m78 != v_stack_m70) goto loc_0022946C;
    result = MiSetPfnContainingFrame(result, 64, a3, 4);
    goto loc_0022946C;
loc_002297E4:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) - (v_stack_pE8));
    a1 = (unsigned int)(((unsigned int)(v_stack_pD8)) + 1);
    result = (unsigned int)((result) - (v_stack_p20));
    result = (unsigned int)((result) - (v_stack_pE0));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (((unsigned __int16)(result)) == a1) goto loc_00229377;
loc_0022980F:
    goto loc_00229870;
loc_0022981D:
    if (((64) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14275221))))) == 0) goto loc_002296A9;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, 64, a3, 4);
    if ((unsigned __int8)(result) == 0) goto loc_002296A9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), 64, a3, 4);
    goto loc_002296AB;
loc_00229846:
    if (((unsigned int)((unsigned int)(v_r14))) > result) goto loc_00229774;
    result = MiIsPdeOrAboveAccessible(v_rsi, 64, a3, 4);
    if ((unsigned int)(result) != 0) goto loc_00229774;
loc_00229870:
    *(unsigned __int64 *)(v_stack_p60) = *(unsigned __int64 *)(v_rip - 2199548);
    if ((unsigned int)(v_rbp) == 0) goto loc_00229527;
    v_r12 = (unsigned int)((v_r12) | (0xFFFFFFFFULL));
loc_00229895:
    v_rsi = (v_rsi) - (8);
    result = MI_READ_PTE_LOCK_FREE(v_rsi, 64, a3, 4);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002298FB;
    a1 = (unsigned int)((result) & (0xC00ULL));
    if (a1 != 0x800ULL) goto loc_002298FB;
    if (*(unsigned __int64 *)(v_rip + 12600258) == 0) goto loc_002298D1;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00229A28;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12600258));
    result = (result) & (a1);
loc_002298D1:
    result = (result) >> (12);
    result = (result) & (a1);
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(v_r12)));
    a1 = (result + result * 2) + (result + result * 2);
loc_002298FB:
    if ((unsigned int)(v_rbp) == 0) goto loc_00229527;
    goto loc_00229895;
loc_00229905:
    if (condition_is_above_or_equal) goto loc_00229368;
loc_00229912:
    v_rbx = (unsigned int)((result) + (1));
    if (((*(unsigned int *)(v_rip + 14268817)) & ((unsigned int)(v_rbx))) == 0) goto loc_00229AAF;
loc_00229921:
loc_00229923:
    if (!sign_flag) goto loc_00229905;
    goto loc_00229912;
loc_00229934:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_002292D5;
    result = (*(unsigned __int64 *)(v_stack_m70 + 24)) + (a1);
    if (v_r14 < result) goto loc_002292D5;
    result = MiCheckLinearProtectedPteAccessedBit(v_r14, v_rbx, 128, 4);
    goto loc_002292D5;
loc_00229976:
    v_stack_p24 = (unsigned int)(v_r10);
    if ((*(unsigned int *)(128 + 64)) != ((unsigned int)(v_r10))) goto loc_00229258;
    v_r13 = (*(unsigned __int64 *)(*(unsigned __int64 *)(128 + 48) + 40)) >> (12);
    v_stack_p38 = v_r13;
    goto loc_00229258;
loc_0022999B:
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14274839))))) == 0) goto loc_002296D9;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r14, v_rbx, 128, 4);
    if ((unsigned __int8)(result) == 0) goto loc_002296D9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), v_rbx, 128, 4);
    goto loc_002296DB;
loc_002299C3:
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14274799))))) == 0) goto loc_002296FF;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), v_rbx, 128, 4);
    if ((unsigned __int8)(result) == 0) goto loc_002296FF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_rbx, 128, 4);
    goto loc_00229701;
loc_002299EB:
    v_rbx = 0;
loc_002299ED:
    if (condition_is_below) goto loc_00229A31;
    v_rbx = 0;
loc_002299F8:
    if (condition_is_below) goto loc_00229A4C;
    result = MiCopyPfnEntryEx(v_stack_m78, v_stack_m70, 128, 4);
    result = MiSetPfnContainingFrame(v_stack_m78, v_stack_p48, 128, 4);
    goto loc_002294F9;
loc_00229A28:
    result = (result) & (-17);
    goto loc_002298D1;
loc_00229A31:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14268531)) & ((unsigned int)(v_rbx))) == 0) goto loc_00229AD7;
loc_00229A3F:
loc_00229A41:
    if (!sign_flag) goto loc_002299ED;
    goto loc_00229A31;
loc_00229A4C:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14268504)) & ((unsigned int)(v_rbx))) == 0) goto loc_00229AFF;
loc_00229A5A:
loc_00229A5C:
    if (!sign_flag) goto loc_002299F8;
    goto loc_00229A4C;
loc_00229A67:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(128 + 48) + 1288) == 0) goto loc_00229527;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(128 + 48) + 1288)) >> (9);
    a1 = (a1) & (1);
    result = (*(unsigned __int64 *)(a1 + v_rsi * 1)) >> (12);
    result = (result) & (v_r14);
    if (result == v_r12) goto loc_00229244;
    goto loc_00229527;
loc_00229A9E:
    goto loc_00229870;
loc_00229AAF:
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14274563))))) == 0) goto loc_00229921;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_stack_p48, 128, 4);
    if ((unsigned __int8)(result) == 0) goto loc_00229921;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_p48, 128, 4);
    goto loc_00229923;
loc_00229AD7:
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14274523))))) == 0) goto loc_00229A3F;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), v_stack_p48, 128, 4);
    if ((unsigned __int8)(result) == 0) goto loc_00229A3F;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_p48, 128, 4);
    goto loc_00229A41;
loc_00229AFF:
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14274483))))) == 0) goto loc_00229A5A;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), v_stack_p48, 128, 4);
    if ((unsigned __int8)(result) == 0) goto loc_00229A5A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_p48, 128, 4);
    goto loc_00229A5C;
loc_00229B27:
    if (condition_is_above_or_equal) goto loc_002297B9;
    goto loc_002297B9;
loc_00229B40:
    goto loc_002295A3;
}
```

## 5. (Beta) C Style

```c
int64_t MiReplacePageTablePage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint32_t v_stack_pE8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    local_rbp = 0;
    *(uint32_t *)(arg1 + 0x38) = 0xC0000001ULL;
    v_stack_mA0 = *(uint64_t *)(arg1 + 0x8);
    local_rdi = (*(uint64_t *)(arg1 + 0x18) + *(uint64_t *)(arg1 + 0x18) * 2) << (4);
    v_stack_m98 = *(uint64_t *)(arg1 + 0x18);
    v_stack_m80 = *(uint64_t *)(arg1 + 0x20);
    v_stack_m90 = *(uint64_t *)(arg1 + 0x18);
    local_rdi = (local_rdi) + (Arg1);
    v_stack_m70 = local_rdi;
    local_r15 = (*(uint64_t *)(arg1 + 0x20) + *(uint64_t *)(arg1 + 0x20) * 2) << (4);
    Arg1 = 0;
    local_r15 = (local_r15) + (0);
    v_stack_p10 = 0;
    Arg2 = 0;
    v_stack_m78 = local_r15;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_mA8 = 0;
    if ((*(uint32_t *)(arg1 + 0x40)) == ((uint32_t)(local_rbp + 1))) goto loc_00229A67;
loc_00229244:
    result = (*(uint64_t *)(local_rdi + 0x28)) & (local_r14);
    if (result == (*(uint64_t *)(arg1 + 0x18))) goto loc_00229976;
loc_00229258:
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (96);
    result = MiGetUltraMapping(Arg1, 4 - 1, local_rbp + 1, 4);
    v_stack_m88 = result;
    local_r14 = (result) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (result);
    v_stack_m68 = local_r14;
    result = MiMakeProtectionPfnCompatible(4, local_r15, local_rbp + 1, 4);
    result = (uint32_t)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(local_r14, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(result)), 4);
    if (condition_is_below) goto loc_00229934;
loc_002292D5:
    *(uint64_t *)(local_r14) = result;
    Arg1 = (*(uint64_t *)(arg1 + 0x18) + *(uint64_t *)(arg1 + 0x18) * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_m58 = Arg1;
loc_002292FA:
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(result)), 4);
    if (((1) & ((uint8_t)(result))) != 0) goto loc_0022953C;
    result = (uint32_t)((result) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_00229740;
loc_0022932F:
    if ((*(uint64_t *)(arg1 + 0x18)) != v_stack_m98) goto loc_002295CA;
loc_0022933A:
    *(uint64_t *)(v_stack_m88) = result;
    local_rsi = (*(uint64_t *)(arg1 + 0x8)) + (8);
    local_r14 = (v_stack_m88) + (8);
    if (((local_rsi) & (0xFFFULL)) != 0) goto loc_002292FA;
    local_rbx = 0;
    if (0 != 0) goto loc_00229905;
loc_0022935B:
    if (condition_is_below) goto loc_002296F0;
loc_00229368:
    if (v_stack_mA4 == 0) goto loc_002297E4;
loc_00229377:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)))) != 1) goto loc_0022980F;
    result = (*(uint64_t *)(local_rdi + 0x18)) & (*(uint64_t *)(arg1 + 0x8));
    if (result >= 0x10000ULL) goto loc_0022980F;
    local_rsi = 0;
loc_002293A3:
    if (condition_is_below) goto loc_002296CA;
    result = (*(uint64_t *)(local_r15 + 0x18)) ^ (*(uint64_t *)(local_rdi + 0x18));
    result = (result) & (*(uint64_t *)(arg1 + 0x8));
    result = (result) ^ (*(uint64_t *)(local_rdi + 0x18));
    *(uint64_t *)(local_r15 + 0x18) = result;
    local_r12 = (uint32_t)((*(uint64_t *)(arg1 + 0x18)) | (0xFFFFFFFFULL));
    if (0 == 0) goto loc_00229492;
loc_002293FB:
    result = MI_READ_PTE_LOCK_FREE(v_stack_mA0, result, (uint32_t)((uint32_t)(result)), 4);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00229474;
    Arg1 = (uint32_t)((result) & (0xC00ULL));
    if (Arg1 != 0x800ULL) goto loc_00229474;
    if (*(uint64_t *)(v_rip + 0xC04860) == 0) goto loc_00229433;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00229737;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xC04860));
    result = (result) & (Arg1);
loc_00229433:
    result = (result) >> (12);
    result = (result) & (Arg1);
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    result = (*(uint64_t *)(local_rbx + 0x28)) & (Arg1);
    if (result == v_stack_m90) goto loc_002297CB;
loc_0022946C:
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(local_r12)));
loc_00229474:
    local_rsi = (v_stack_mA0) + (8);
    if ((uint32_t)(local_rbp) != 0) goto loc_002293FB;
loc_00229492:
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_002294DF;
    result = (v_stack_mA0) - (v_stack_m88);
    v_stack_mA0 = result;
loc_002294B4:
    result = MI_READ_PTE_LOCK_FREE(result + v_stack_m88 * 1, result, (uint32_t)((uint32_t)(result)), 4);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002295DC;
loc_002294C8:
    local_rbp = (v_stack_m88) + (8);
    if ((uint32_t)((uint32_t)(v_stack_p10)) != 0) goto loc_002294B4;
loc_002294DF:
    *(uint64_t *)(v_stack_m68) = *(uint64_t *)(v_rip - 0x218C70);
    if (v_stack_mA4 != 0) goto loc_002299EB;
loc_002294F9:
    result = (uint32_t)(*(uint32_t *)(v_stack_m58 + 0x24));
    if (v_stack_mA4 < 0) {
        result = v_stack_p8;
        Arg2 = v_stack_m78;
        Arg1 = *(uint64_t *)(result);
        result = MiReplaceActivePageTableLinks(Arg1, Arg2, v_stack_m58, 4);
    }
loc_00229527:
    local_rsp = (local_rsp) + (136);
    return v_stack_p8;
loc_0022953C:
    if (sign_flag) goto loc_0022959B;
    result = (v_stack_p8) >> (12);
    result = (result) & (Arg1);
    if (result == (*(uint64_t *)(v_rip + 0xC0DF18))) goto loc_00229B40;
    if (result > (*(uint64_t *)(v_rip + 0xC04773))) goto loc_002295A3;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (((1) & ((uint32_t)(result))) == 0) goto loc_002295A3;
    if (!(condition_is_above_or_equal)) {
    }
    if (64 == v_stack_p30) goto loc_0022933A;
    result = ((uint32_t)(v_stack_p10)) - (v_stack_p28);
    result = (result) >> (3);
loc_002295CA:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x48) + result * 8))) & (1));
    result = (uint8_t)(-(result));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x48) + result * 8)) & (result);
    goto loc_0022933A;
loc_002295DC:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p10)) + ((uint32_t)(local_r12)));
    Arg1 = (result) >> (12);
    Arg1 = (Arg1) & (result);
    v_stack_pD8 = (uint32_t)(local_rsi);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xC046DF))) goto loc_00229673;
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    result = (*(uint64_t *)(result + Arg2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00229673;
    if (Arg1 == v_stack_m78) goto loc_00229673;
    local_r14 = 0;
loc_0022963E:
    if (condition_is_below) goto loc_00229699;
    result = (*(uint64_t *)(result + Arg2 * 8 + 0x28)) & (Arg1);
    if (result == v_stack_m78) goto loc_002296B6;
loc_0022965D:
loc_00229673:
    if (v_stack_m78 != v_stack_m70) goto loc_00229716;
loc_0022967C:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002294C8;
    local_rbx = (result) | (32);
    result = MiWriteValidPteNewProtection(local_rbp, local_rbx, result, 4);
    goto loc_002294C8;
loc_00229699:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9BC09)) & ((uint32_t)(local_r14))) == 0) goto loc_0022981D;
loc_002296A9:
loc_002296AB:
    if (!sign_flag) goto loc_0022963E;
    goto loc_00229699;
loc_002296B6:
    if (v_stack_m78 != v_stack_m70) goto loc_0022965D;
    result = MiSetPfnContainingFrame((uint32_t)(v_stack_pD8), v_stack_p48, result, 4);
    goto loc_0022965D;
loc_002296CA:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_pD8)) + (1));
    if (((*(uint32_t *)(v_rip + 0xD9BBD9)) & ((uint32_t)(local_rsi))) == 0) goto loc_0022999B;
loc_002296D9:
loc_002296DB:
    if (!sign_flag) goto loc_002293A3;
    goto loc_002296CA;
loc_002296F0:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((*(uint32_t *)(v_rip + 0xD9BBB3)) & ((uint32_t)(local_rbx))) == 0) goto loc_002299C3;
loc_002296FF:
loc_00229701:
    if (!sign_flag) goto loc_0022935B;
    goto loc_002296F0;
loc_00229716:
    result = (local_rbp) - (v_stack_p40);
    result = (result) >> (3);
    goto loc_0022967C;
loc_00229737:
    result = (result) & (-17);
    goto loc_00229433;
loc_00229740:
    local_r10 = 0;
    local_r10 = ((uint32_t)(local_rbp) != 0) ? 1 : 0;
    Arg1 = (local_rsi) << (25);
    result = (v_stack_p48) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= v_stack_p48) goto loc_00229846;
loc_00229774:
    a3 = 0;
    result = MiLockTransitionLeafPageEx(local_rsi, local_r10, a3, 4);
    if (result == 0) goto loc_002292FA;
    result = MI_READ_PTE_LOCK_FREE(local_rsi, local_r10, a3, 4);
    Arg1 = (*(uint64_t *)(result + 0x28)) & (result);
    if (Arg1 != 64) goto loc_00229B27;
loc_002297B9:
    if (((*(uint8_t *)(result + 0x22)) & (32)) != 0) goto loc_00229A9E;
    local_rbp = (uint32_t)((local_rbp) + (1));
    goto loc_0022932F;
loc_002297CB:
    if (v_stack_m78 != v_stack_m70) goto loc_0022946C;
    result = MiSetPfnContainingFrame(result, 64, a3, 4);
    goto loc_0022946C;
loc_002297E4:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) - (v_stack_pE8));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_pD8)) + 1);
    result = (uint32_t)((result) - (v_stack_p20));
    result = (uint32_t)((result) - (v_stack_pE0));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (((uint16_t)(result)) == Arg1) goto loc_00229377;
loc_0022980F:
    goto loc_00229870;
loc_0022981D:
    if (((64) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9D295))))) == 0) goto loc_002296A9;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, 64, a3, 4);
    if ((uint8_t)(result) == 0) goto loc_002296A9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), 64, a3, 4);
    goto loc_002296AB;
loc_00229846:
    if (((uint32_t)((uint32_t)(local_r14))) > result) goto loc_00229774;
    result = MiIsPdeOrAboveAccessible(local_rsi, 64, a3, 4);
    if ((uint32_t)(result) != 0) goto loc_00229774;
loc_00229870:
    *(uint64_t *)(v_stack_p60) = *(uint64_t *)(v_rip - 0x218FFC);
    if ((uint32_t)(local_rbp) == 0) goto loc_00229527;
    local_r12 = (uint32_t)((local_r12) | (0xFFFFFFFFULL));
loc_00229895:
    local_rsi = (local_rsi) - (8);
    result = MI_READ_PTE_LOCK_FREE(local_rsi, 64, a3, 4);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002298FB;
    Arg1 = (uint32_t)((result) & (0xC00ULL));
    if (Arg1 != 0x800ULL) goto loc_002298FB;
    if (*(uint64_t *)(v_rip + 0xC043C2) == 0) goto loc_002298D1;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00229A28;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xC043C2));
    result = (result) & (Arg1);
loc_002298D1:
    result = (result) >> (12);
    result = (result) & (Arg1);
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(local_r12)));
    Arg1 = (result + result * 2) + (result + result * 2);
loc_002298FB:
    if ((uint32_t)(local_rbp) == 0) goto loc_00229527;
    goto loc_00229895;
loc_00229905:
    if (condition_is_above_or_equal) goto loc_00229368;
loc_00229912:
    local_rbx = (uint32_t)((result) + (1));
    if (((*(uint32_t *)(v_rip + 0xD9B991)) & ((uint32_t)(local_rbx))) == 0) goto loc_00229AAF;
loc_00229921:
loc_00229923:
    if (!sign_flag) goto loc_00229905;
    goto loc_00229912;
loc_00229934:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_002292D5;
    result = (*(uint64_t *)(v_stack_m70 + 0x18)) + (Arg1);
    if (local_r14 < result) goto loc_002292D5;
    result = MiCheckLinearProtectedPteAccessedBit(local_r14, local_rbx, 128, 4);
    goto loc_002292D5;
loc_00229976:
    v_stack_p24 = (uint32_t)(local_r10);
    if ((*(uint32_t *)(128 + 0x40)) != ((uint32_t)(local_r10))) goto loc_00229258;
    local_r13 = (*(uint64_t *)(*(uint64_t *)(128 + 0x30) + 0x28)) >> (12);
    v_stack_p38 = local_r13;
    goto loc_00229258;
loc_0022999B:
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9D117))))) == 0) goto loc_002296D9;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r14, local_rbx, 128, 4);
    if ((uint8_t)(result) == 0) goto loc_002296D9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), local_rbx, 128, 4);
    goto loc_002296DB;
loc_002299C3:
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9D0EF))))) == 0) goto loc_002296FF;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), local_rbx, 128, 4);
    if ((uint8_t)(result) == 0) goto loc_002296FF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), local_rbx, 128, 4);
    goto loc_00229701;
loc_002299EB:
    local_rbx = 0;
loc_002299ED:
    if (condition_is_below) goto loc_00229A31;
    local_rbx = 0;
loc_002299F8:
    if (condition_is_below) goto loc_00229A4C;
    result = MiCopyPfnEntryEx(v_stack_m78, v_stack_m70, 128, 4);
    result = MiSetPfnContainingFrame(v_stack_m78, v_stack_p48, 128, 4);
    goto loc_002294F9;
loc_00229A28:
    result = (result) & (-17);
    goto loc_002298D1;
loc_00229A31:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9B873)) & ((uint32_t)(local_rbx))) == 0) goto loc_00229AD7;
loc_00229A3F:
loc_00229A41:
    if (!sign_flag) goto loc_002299ED;
    goto loc_00229A31;
loc_00229A4C:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9B858)) & ((uint32_t)(local_rbx))) == 0) goto loc_00229AFF;
loc_00229A5A:
loc_00229A5C:
    if (!sign_flag) goto loc_002299F8;
    goto loc_00229A4C;
loc_00229A67:
    if (*(uint64_t *)(*(uint64_t *)(128 + 0x30) + 0x508) == 0) goto loc_00229527;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(128 + 0x30) + 0x508)) >> (9);
    Arg1 = (Arg1) & (1);
    result = (*(uint64_t *)(arg1 + local_rsi * 1)) >> (12);
    result = (result) & (local_r14);
    if (result == local_r12) goto loc_00229244;
    goto loc_00229527;
loc_00229A9E:
    goto loc_00229870;
loc_00229AAF:
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9D003))))) == 0) goto loc_00229921;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, v_stack_p48, 128, 4);
    if ((uint8_t)(result) == 0) goto loc_00229921;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_p48, 128, 4);
    goto loc_00229923;
loc_00229AD7:
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9CFDB))))) == 0) goto loc_00229A3F;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), v_stack_p48, 128, 4);
    if ((uint8_t)(result) == 0) goto loc_00229A3F;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_p48, 128, 4);
    goto loc_00229A41;
loc_00229AFF:
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9CFB3))))) == 0) goto loc_00229A5A;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), v_stack_p48, 128, 4);
    if ((uint8_t)(result) == 0) goto loc_00229A5A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_p48, 128, 4);
    goto loc_00229A5C;
loc_00229B27:
    if (condition_is_above_or_equal) goto loc_002297B9;
    goto loc_002297B9;
loc_00229B40:
    goto loc_002295A3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00229184&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
