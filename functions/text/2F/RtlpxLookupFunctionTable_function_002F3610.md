# RtlpxLookupFunctionTable

- RVA: `0x002F3610`–`0x002F3B0E` (길이 `1,278` bytes)
- VA: `0x00000001402F3610`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007205C`
- 디코드: `313`개 명령, `1,278/1,278` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x002F3775` → [MmLockLoadedModuleListShared](MmLockLoadedModuleListShared_function_002F21E4.md) (function, `0x002F21E4`)
- `0x002F3817` → [MmUnlockLoadedModuleListShared](MmUnlockLoadedModuleListShared_function_002F2230.md) (function, `0x002F2230`)

### Direct callers
- [RtlPcToFileHeader](RtlPcToFileHeader_function_002F1C50.md) at `0x002F1CA2`
- [RtlGuardCheckExceptionHandler](RtlGuardCheckExceptionHandler_function_002F2038.md) at `0x002F20B9`
- [RtlLookupFunctionTable](RtlLookupFunctionTable_function_002F2750.md) at `0x002F27CC`
- [RtlLookupFunctionTableEx](RtlLookupFunctionTableEx_function_002F27E0.md) at `0x002F281E`
- [sub_002F304F](Unknown_function_002F304F.md) at `0x002F3091`
- [RtlpLookupFunctionEntryForStackWalks](RtlpLookupFunctionEntryForStackWalks_function_002F4ED0.md) at `0x002F50DC`
- [KiTpBuildExcludedKernelTracepointBitmap](../../page/74/KiTpBuildExcludedKernelTracepointBitmap_function_007485B0.md) at `0x007486D6`
- [KiVerifyPdata](../../init/C3/KiVerifyPdata_function_00C3A500.md) at `0x00C3A551`
- [MiInitializeLoadedModuleList](../../init/C6/MiInitializeLoadedModuleList_function_00C6BCDC.md) at `0x00C6BE7B`

### Static image references
- `0x002F3645` → RVA `0x01200000` (`CFGRO`; read)
- `0x002F3660` → RVA `0x01201A70` (`CFGRO`; read)
- `0x002F3670` → RVA `0x00E2D83C` (`.data`; read)
- `0x002F36B0` → RVA `0x01201848` (`CFGRO`; read)
- `0x002F3723` → RVA `0x00FC6B28` (`ALMOSTRO`; read)
- `0x002F372C` → RVA `0x00FC6B98` (`ALMOSTRO`; read)
- `0x002F3758` → RVA `0x00F4754C` (`.data`; read)
- `0x002F386B` → RVA `0x00EF54C0` (`.data`; read)
- `0x002F38CB` → RVA `0x00E375AC` (`.data`; read)
- `0x002F38D2` → RVA `0x00E375B0` (`.data`; read)
- `0x002F39FA` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F3610  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002F3615  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002F361A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002F361F  57                              push rdi
002F3620  41 54                           push r12
002F3622  41 55                           push r13
002F3624  41 56                           push r14
002F3626  41 57                           push r15
002F3628  48 83 EC 40                     sub rsp, 0x40
002F362C  48 8B D9                        mov rbx, rcx
002F362F  4C 8B E2                        mov r12, rdx
002F3632  33 C9                           xor ecx, ecx
002F3634  48 BE FF FF FE FF FF 7F 00 00   movabs rsi, 0x7ffffffeffff
002F363E  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
002F3642  89 4A 10                        mov dword ptr [rdx + 0x10], ecx
002F3645  48 8B 3D B4 C9 F0 00            mov rdi, qword ptr [rip + 0xf0c9b4]
002F364C  44 8D 79 01                     lea r15d, [rcx + 1]
002F3650  44 8B 77 08                     mov r14d, dword ptr [rdi + 8]
002F3654  45 84 F7                        test r15b, r14b
002F3657  0F 85 FB 00 00 00               jne 0x1402f3758
002F365D  44 8B 1F                        mov r11d, dword ptr [rdi]
002F3660  4C 8D 2D 09 E4 F0 00            lea r13, [rip + 0xf0e409]
002F3667  45 3B DF                        cmp r11d, r15d
002F366A  0F 84 DC 00 00 00               je 0x1402f374c
002F3670  8B 2D C6 A1 B3 00               mov ebp, dword ptr [rip + 0xb3a1c6]
002F3676  45 8B D7                        mov r10d, r15d
002F3679  C1 E5 0C                        shl ebp, 0xc
002F367C  41 FF CB                        dec r11d
002F367F  90                              nop
002F3680  45 3B DA                        cmp r11d, r10d
002F3683  0F 8C C1 00 00 00               jl 0x1402f374a
002F3689  43 8D 04 1A                     lea eax, [r10 + r11]
002F368D  D1 F8                           sar eax, 1
002F368F  48 63 C8                        movsxd rcx, eax
002F3692  48 8D 14 49                     lea rdx, [rcx + rcx*2]
002F3696  4C 8B 4C D7 18                  mov r9, qword ptr [rdi + rdx*8 + 0x18]
002F369B  4C 8D 04 D7                     lea r8, [rdi + rdx*8]
002F369F  8B 54 D7 20                     mov edx, dword ptr [rdi + rdx*8 + 0x20]
002F36A3  49 03 D1                        add rdx, r9
002F36A6  49 3B D9                        cmp rbx, r9
002F36A9  72 1C                           jb 0x1402f36c7
002F36AB  48 3B DE                        cmp rbx, rsi
002F36AE  76 0C                           jbe 0x1402f36bc
002F36B0  44 8B 15 91 E1 F0 00            mov r10d, dword ptr [rip + 0xf0e191]
002F36B7  45 85 D2                        test r10d, r10d
002F36BA  75 58                           jne 0x1402f3714
002F36BC  48 3B DA                        cmp rbx, rdx
002F36BF  72 10                           jb 0x1402f36d1
002F36C1  44 8D 50 01                     lea r10d, [rax + 1]
002F36C5  EB B9                           jmp 0x1402f3680
002F36C7  85 C0                           test eax, eax
002F36C9  74 7F                           je 0x1402f374a
002F36CB  44 8D 58 FF                     lea r11d, [rax - 1]
002F36CF  EB AF                           jmp 0x1402f3680
002F36D1  41 0F 10 40 10                  movups xmm0, xmmword ptr [r8 + 0x10]
002F36D6  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
002F36DB  F2 41 0F 10 48 20               movsd xmm1, qword ptr [r8 + 0x20]
002F36E1  F2 41 0F 11 4C 24 10            movsd qword ptr [r12 + 0x10], xmm1
002F36E8  49 8B 04 24                     mov rax, qword ptr [r12]
002F36EC  90                              nop
002F36ED  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
002F36F0  41 3B CE                        cmp ecx, r14d
002F36F3  75 63                           jne 0x1402f3758
002F36F5  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
002F36FA  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
002F36FE  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
002F3702  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
002F3706  49 8B E3                        mov rsp, r11
002F3709  41 5F                           pop r15
002F370B  41 5E                           pop r14
002F370D  41 5D                           pop r13
002F370F  41 5C                           pop r12
002F3711  5F                              pop rdi
002F3712  C3                              ret
002F3713  CC                              int3
002F3714  48 3B DA                        cmp rbx, rdx
002F3717  72 B8                           jb 0x1402f36d1
002F3719  8B CD                           mov ecx, ebp
002F371B  48 03 CA                        add rcx, rdx
002F371E  48 3B D9                        cmp rbx, rcx
002F3721  73 9E                           jae 0x1402f36c1
002F3723  4C 3B 0D FE 33 CD 00            cmp r9, qword ptr [rip + 0xcd33fe]
002F372A  74 95                           je 0x1402f36c1
002F372C  4C 3B 0D 65 34 CD 00            cmp r9, qword ptr [rip + 0xcd3465]
002F3733  74 87                           je 0x1402f36bc
002F3735  4D 89 2C 24                     mov qword ptr [r12], r13
002F3739  49 89 54 24 08                  mov qword ptr [r12 + 8], rdx
002F373E  41 89 6C 24 10                  mov dword ptr [r12 + 0x10], ebp
002F3743  45 89 54 24 14                  mov dword ptr [r12 + 0x14], r10d
002F3748  EB 9E                           jmp 0x1402f36e8
002F374A  33 C9                           xor ecx, ecx
002F374C  0F B6 47 0C                     movzx eax, byte ptr [rdi + 0xc]
002F3750  84 C0                           test al, al
002F3752  0F 84 9D 03 00 00               je 0x1402f3af5
002F3758  8B 05 EE 3D C5 00               mov eax, dword ptr [rip + 0xc53dee]
002F375E  4C 8D 35 0B E3 F0 00            lea r14, [rip + 0xf0e30b]
002F3765  45 32 ED                        xor r13b, r13b
002F3768  A8 03                           test al, 3
002F376A  0F 85 8D 03 00 00               jne 0x1402f3afd
002F3770  44 88 6C 24 78                  mov byte ptr [rsp + 0x78], r13b
002F3775  E8 6A EA FF FF                  call 0x1402f21e4
002F377A  44 0F B6 E8                     movzx r13d, al
002F377E  48 8B 3D 7B C8 F0 00            mov rdi, qword ptr [rip + 0xf0c87b]
002F3785  44 8B 17                        mov r10d, dword ptr [rdi]
002F3788  41 83 FA 01                     cmp r10d, 1
002F378C  0F 84 C8 00 00 00               je 0x1402f385a
002F3792  8B 2D A4 A0 B3 00               mov ebp, dword ptr [rip + 0xb3a0a4]
002F3798  C1 E5 0C                        shl ebp, 0xc
002F379B  41 FF CA                        dec r10d
002F379E  66 90                           nop
002F37A0  45 3B D7                        cmp r10d, r15d
002F37A3  0F 8C B1 00 00 00               jl 0x1402f385a
002F37A9  43 8D 14 17                     lea edx, [r15 + r10]
002F37AD  D1 FA                           sar edx, 1
002F37AF  48 63 C2                        movsxd rax, edx
002F37B2  48 8D 0C 40                     lea rcx, [rax + rax*2]
002F37B6  4C 8B 4C CF 18                  mov r9, qword ptr [rdi + rcx*8 + 0x18]
002F37BB  4C 8D 04 CF                     lea r8, [rdi + rcx*8]
002F37BF  8B 4C CF 20                     mov ecx, dword ptr [rdi + rcx*8 + 0x20]
002F37C3  49 03 C9                        add rcx, r9
002F37C6  49 3B D9                        cmp rbx, r9
002F37C9  72 1C                           jb 0x1402f37e7
002F37CB  48 3B DE                        cmp rbx, rsi
002F37CE  76 0C                           jbe 0x1402f37dc
002F37D0  44 8B 1D 71 E0 F0 00            mov r11d, dword ptr [rip + 0xf0e071]
002F37D7  45 85 DB                        test r11d, r11d
002F37DA  75 48                           jne 0x1402f3824
002F37DC  48 3B D9                        cmp rbx, rcx
002F37DF  72 10                           jb 0x1402f37f1
002F37E1  44 8D 7A 01                     lea r15d, [rdx + 1]
002F37E5  EB B9                           jmp 0x1402f37a0
002F37E7  85 D2                           test edx, edx
002F37E9  74 6F                           je 0x1402f385a
002F37EB  44 8D 52 FF                     lea r10d, [rdx - 1]
002F37EF  EB AF                           jmp 0x1402f37a0
002F37F1  41 0F 10 40 10                  movups xmm0, xmmword ptr [r8 + 0x10]
002F37F6  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
002F37FB  F2 41 0F 10 48 20               movsd xmm1, qword ptr [r8 + 0x20]
002F3801  F2 41 0F 11 4C 24 10            movsd qword ptr [r12 + 0x10], xmm1
002F3808  49 8B 1C 24                     mov rbx, qword ptr [r12]
002F380C  80 7C 24 78 00                  cmp byte ptr [rsp + 0x78], 0
002F3811  75 09                           jne 0x1402f381c
002F3813  41 0F B6 CD                     movzx ecx, r13b
002F3817  E8 14 EA FF FF                  call 0x1402f2230
002F381C  48 8B C3                        mov rax, rbx
002F381F  E9 D1 FE FF FF                  jmp 0x1402f36f5
002F3824  48 3B D9                        cmp rbx, rcx
002F3827  72 C8                           jb 0x1402f37f1
002F3829  8B C5                           mov eax, ebp
002F382B  48 03 C1                        add rax, rcx
002F382E  48 3B D8                        cmp rbx, rax
002F3831  73 AE                           jae 0x1402f37e1
002F3833  4C 3B 0D EE 32 CD 00            cmp r9, qword ptr [rip + 0xcd32ee]
002F383A  74 A5                           je 0x1402f37e1
002F383C  4C 3B 0D 55 33 CD 00            cmp r9, qword ptr [rip + 0xcd3355]
002F3843  74 97                           je 0x1402f37dc
002F3845  4D 89 34 24                     mov qword ptr [r12], r14
002F3849  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
002F384E  41 89 6C 24 10                  mov dword ptr [r12 + 0x10], ebp
002F3853  45 89 5C 24 14                  mov dword ptr [r12 + 0x14], r11d
002F3858  EB AE                           jmp 0x1402f3808
002F385A  80 7F 0C 00                     cmp byte ptr [rdi + 0xc], 0
002F385E  0F 84 A3 02 00 00               je 0x1402f3b07
002F3864  44 8B 3D D1 9F B3 00            mov r15d, dword ptr [rip + 0xb39fd1]
002F386B  48 8B 35 4E 1C C0 00            mov rsi, qword ptr [rip + 0xc01c4e]
002F3872  41 C1 E7 0C                     shl r15d, 0xc
002F3876  48 85 F6                        test rsi, rsi
002F3879  0F 84 88 02 00 00               je 0x1402f3b07
002F387F  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
002F3889  48 8D 05 30 1C C0 00            lea rax, [rip + 0xc01c30]
002F3890  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
002F389A  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
002F38A4  48 3B F0                        cmp rsi, rax
002F38A7  0F 84 5A 02 00 00               je 0x1402f3b07
002F38AD  48 8B 7E 30                     mov rdi, qword ptr [rsi + 0x30]
002F38B1  48 3B 3D 70 32 CD 00            cmp rdi, qword ptr [rip + 0xcd3270]
002F38B8  0F 84 CC 01 00 00               je 0x1402f3a8a
002F38BE  48 3B 3D D3 32 CD 00            cmp rdi, qword ptr [rip + 0xcd32d3]
002F38C5  0F 84 BF 01 00 00               je 0x1402f3a8a
002F38CB  44 8B 1D DA 3C B4 00            mov r11d, dword ptr [rip + 0xb43cda]
002F38D2  44 03 1D D7 3C B4 00            add r11d, dword ptr [rip + 0xb43cd7]
002F38D9  45 85 DB                        test r11d, r11d
002F38DC  0F 84 B4 01 00 00               je 0x1402f3a96
002F38E2  44 8B 4E 40                     mov r9d, dword ptr [rsi + 0x40]
002F38E6  48 8B CF                        mov rcx, rdi
002F38E9  48 C1 E9 09                     shr rcx, 9
002F38ED  BD 04 00 00 00                  mov ebp, 4
002F38F2  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002F38FC  4C 03 CF                        add r9, rdi
002F38FF  48 23 C8                        and rcx, rax
002F3902  44 8B F5                        mov r14d, ebp
002F3905  49 8B C2                        mov rax, r10
002F3908  48 03 C8                        add rcx, rax
002F390B  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002F3915  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002F391A  48 C1 E9 09                     shr rcx, 9
002F391E  48 23 C8                        and rcx, rax
002F3921  49 8B C2                        mov rax, r10
002F3924  48 03 C8                        add rcx, rax
002F3927  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002F3931  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002F3936  48 C1 E9 09                     shr rcx, 9
002F393A  48 23 C8                        and rcx, rax
002F393D  49 8B C2                        mov rax, r10
002F3940  48 03 C8                        add rcx, rax
002F3943  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002F394D  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002F3952  48 C1 E9 09                     shr rcx, 9
002F3956  48 23 C8                        and rcx, rax
002F3959  49 8B C2                        mov rax, r10
002F395C  48 03 C8                        add rcx, rax
002F395F  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002F3964  4C 8B 54 EC 18                  mov r10, qword ptr [rsp + rbp*8 + 0x18]
002F3969  48 FF CD                        dec rbp
002F396C  41 FF CE                        dec r14d
002F396F  49 8B 02                        mov rax, qword ptr [r10]
002F3972  49 8B C8                        mov rcx, r8
002F3975  4C 3B D1                        cmp r10, rcx
002F3978  72 33                           jb 0x1402f39ad
002F397A  48 8B CA                        mov rcx, rdx
002F397D  4C 3B D1                        cmp r10, rcx
002F3980  77 2B                           ja 0x1402f39ad
002F3982  48 8B C8                        mov rcx, rax
002F3985  A8 01                           test al, 1
002F3987  74 47                           je 0x1402f39d0
002F3989  A8 42                           test al, 0x42
002F398B  41 0F 95 C0                     setne r8b
002F398F  A8 20                           test al, 0x20
002F3991  0F 95 C2                        setne dl
002F3994  44 84 C2                        test dl, r8b
002F3997  74 61                           je 0x1402f39fa
002F3999  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
002F39A3  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
002F39AD  A8 01                           test al, 1
002F39AF  74 1F                           je 0x1402f39d0
002F39B1  84 C0                           test al, al
002F39B3  78 08                           js 0x1402f39bd
002F39B5  48 83 FD 01                     cmp rbp, 1
002F39B9  74 15                           je 0x1402f39d0
002F39BB  EB A7                           jmp 0x1402f3964
002F39BD  45 85 F6                        test r14d, r14d
002F39C0  74 0E                           je 0x1402f39d0
002F39C2  49 81 C1 FF FF 1F 00            add r9, 0x1fffff
002F39C9  49 81 E1 00 00 E0 FF            and r9, 0xffffffffffe00000
002F39D0  4D 85 C9                        test r9, r9
002F39D3  0F 84 BD 00 00 00               je 0x1402f3a96
002F39D9  41 8B CB                        mov ecx, r11d
002F39DC  49 03 C9                        add rcx, r9
002F39DF  48 3B D9                        cmp rbx, rcx
002F39E2  72 7C                           jb 0x1402f3a60
002F39E4  8B 15 5E DE F0 00               mov edx, dword ptr [rip + 0xf0de5e]
002F39EA  85 D2                           test edx, edx
002F39EC  0F 85 AF 00 00 00               jne 0x1402f3aa1
002F39F2  48 8B 36                        mov rsi, qword ptr [rsi]
002F39F5  E9 8F FE FF FF                  jmp 0x1402f3889
002F39FA  48 F7 05 83 30 CD 00 00 00 60 00  test qword ptr [rip + 0xcd3083], 0x600000
002F3A05  74 92                           je 0x1402f3999
002F3A07  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
002F3A10  4C 8B 82 B8 00 00 00            mov r8, qword ptr [rdx + 0xb8]
002F3A17  41 80 B8 60 01 00 00 01         cmp byte ptr [r8 + 0x160], 1
002F3A1F  0F 84 74 FF FF FF               je 0x1402f3999
002F3A25  49 8B 90 08 05 00 00            mov rdx, qword ptr [r8 + 0x508]
002F3A2C  48 85 D2                        test rdx, rdx
002F3A2F  0F 84 64 FF FF FF               je 0x1402f3999
002F3A35  49 C1 EA 03                     shr r10, 3
002F3A39  41 81 E2 FF 01 00 00            and r10d, 0x1ff
002F3A40  4A 8B 14 D2                     mov rdx, qword ptr [rdx + r10*8]
002F3A44  F6 C2 20                        test dl, 0x20
002F3A47  74 04                           je 0x1402f3a4d
002F3A49  48 83 C9 20                     or rcx, 0x20
002F3A4D  48 8B C1                        mov rax, rcx
002F3A50  48 83 C8 42                     or rax, 0x42
002F3A54  F6 C2 42                        test dl, 0x42
002F3A57  48 0F 44 C1                     cmove rax, rcx
002F3A5B  E9 39 FF FF FF                  jmp 0x1402f3999
002F3A60  48 3B DF                        cmp rbx, rdi
002F3A63  0F 82 7B FF FF FF               jb 0x1402f39e4
002F3A69  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
002F3A6D  2B CF                           sub ecx, edi
002F3A6F  49 89 1C 24                     mov qword ptr [r12], rbx
002F3A73  41 89 4C 24 10                  mov dword ptr [r12 + 0x10], ecx
002F3A78  49 89 7C 24 08                  mov qword ptr [r12 + 8], rdi
002F3A7D  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
002F3A80  41 89 44 24 14                  mov dword ptr [r12 + 0x14], eax
002F3A85  E9 82 FD FF FF                  jmp 0x1402f380c
002F3A8A  44 8B 1D 1B 3B B4 00            mov r11d, dword ptr [rip + 0xb43b1b]
002F3A91  E9 43 FE FF FF                  jmp 0x1402f38d9
002F3A96  8B 4E 40                        mov ecx, dword ptr [rsi + 0x40]
002F3A99  48 03 CF                        add rcx, rdi
002F3A9C  E9 3E FF FF FF                  jmp 0x1402f39df
002F3AA1  48 3B D9                        cmp rbx, rcx
002F3AA4  0F 82 48 FF FF FF               jb 0x1402f39f2
002F3AAA  41 8B C7                        mov eax, r15d
002F3AAD  48 03 C1                        add rax, rcx
002F3AB0  48 3B D8                        cmp rbx, rax
002F3AB3  0F 83 39 FF FF FF               jae 0x1402f39f2
002F3AB9  48 3B 3D 68 30 CD 00            cmp rdi, qword ptr [rip + 0xcd3068]
002F3AC0  0F 84 2C FF FF FF               je 0x1402f39f2
002F3AC6  48 3B 3D CB 30 CD 00            cmp rdi, qword ptr [rip + 0xcd30cb]
002F3ACD  0F 84 1F FF FF FF               je 0x1402f39f2
002F3AD3  48 8D 05 96 DF F0 00            lea rax, [rip + 0xf0df96]
002F3ADA  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
002F3ADF  48 8B D8                        mov rbx, rax
002F3AE2  49 89 04 24                     mov qword ptr [r12], rax
002F3AE6  45 89 7C 24 10                  mov dword ptr [r12 + 0x10], r15d
002F3AEB  41 89 54 24 14                  mov dword ptr [r12 + 0x14], edx
002F3AF0  E9 17 FD FF FF                  jmp 0x1402f380c
002F3AF5  48 8B C1                        mov rax, rcx
002F3AF8  E9 EF FB FF FF                  jmp 0x1402f36ec
002F3AFD  C6 44 24 78 01                  mov byte ptr [rsp + 0x78], 1
002F3B02  E9 77 FC FF FF                  jmp 0x1402f377e
002F3B07  33 DB                           xor ebx, ebx
002F3B09  E9 FE FC FF FF                  jmp 0x1402f380c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpxLookupFunctionTable(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (64);
    a1 = 0;
    *(unsigned __int64 *)(a2 + 8) = 0;
    *(unsigned int *)(a2 + 16) = 0;
    if ((((unsigned __int8)(a1 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276) + 8))))) != 0) goto loc_002F3758;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276))))) == ((unsigned int)(a1 + 1))) goto loc_002F374C;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11772358))) << (12));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276)))) - 1);
loc_002F3680:
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned int)((unsigned int)(a1 + 1))))) goto loc_002F374A;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1 + 1)) + v_r11 * 1) >> (1));
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 32))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 24));
    if (0 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 24))) goto loc_002F36C7;
    if (0 <= v_rsi) goto loc_002F36BC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 15786385))) != 0) goto loc_002F3714;
loc_002F36BC:
    if (0 < a2) goto loc_002F36D1;
loc_002F36C1:
    goto loc_002F3680;
loc_002F36C7:
    if ((unsigned int)(result) == 0) goto loc_002F374A;
    goto loc_002F3680;
loc_002F36D1:
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
loc_002F36E8:
loc_002F36EC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276) + 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15780276) + 8))))) goto loc_002F3758;
loc_002F36F5:
    return *(unsigned __int64 *)(a2);
loc_002F3714:
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < a2) goto loc_002F36D1;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)))) + (a2);
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) >= a1) goto loc_002F36C1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 24)) == (*(unsigned __int64 *)(v_rip + 13448190))) goto loc_002F36C1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 24)) == (*(unsigned __int64 *)(v_rip + 13448293))) goto loc_002F36BC;
    *(unsigned __int64 *)(a2) = v_rip + 15787017;
    *(unsigned __int64 *)(a2 + 8) = a2;
    *(unsigned int *)(a2 + 16) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    *(unsigned int *)(a2 + 20) = (unsigned int)(result + 1);
    goto loc_002F36E8;
loc_002F374A:
    a1 = 0;
loc_002F374C:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 15780276) + 12)) == 0) goto loc_002F3AF5;
loc_002F3758:
    v_r13 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12926446)))) & (3)) != 0) goto loc_002F3AFD;
    v_stack_p38 = 0;
    result = MmLockLoadedModuleListShared(a1, a2, *(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15780276) + (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 2 * 8 + 24));
loc_002F377E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15779963))))) == 1) goto loc_002F385A;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11772068))) << (12));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15779963)))) - 1);
loc_002F37A0:
    if (((unsigned int)(v_r10)) < ((unsigned int)(a1 + 1))) goto loc_002F385A;
    a2 = (unsigned int)((a1 + 1 + v_r10 * 1) >> (1));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 32))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 24));
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 24))) goto loc_002F37E7;
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) <= (*(unsigned __int64 *)(v_stack_m28 + 72))) goto loc_002F37DC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 15786097))) != 0) goto loc_002F3824;
loc_002F37DC:
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < a1) goto loc_002F37F1;
loc_002F37E1:
    goto loc_002F37A0;
loc_002F37E7:
    if ((unsigned int)(a2) == 0) goto loc_002F385A;
    goto loc_002F37A0;
loc_002F37F1:
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
loc_002F3808:
loc_002F380C:
    result = (int)((unsigned int)(a2));
    if (v_stack_p38 == 0) {
        a1 = (unsigned __int8)((unsigned __int8)(result));
        result = MmUnlockLoadedModuleListShared(a1, a2, *(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 24));
    }
    goto loc_002F36F5;
loc_002F3824:
    if ((*(unsigned __int64 *)(a2)) < a1) goto loc_002F37F1;
    result = ((unsigned int)((unsigned int)(v_rbp))) + (a1);
    if ((*(unsigned __int64 *)(a2)) >= result) goto loc_002F37E1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 24)) == (*(unsigned __int64 *)(v_rip + 13447918))) goto loc_002F37E1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8 + 24)) == (*(unsigned __int64 *)(v_rip + 13448021))) goto loc_002F37DC;
    *(unsigned __int64 *)(a2) = v_rip + 15786763;
    *(unsigned __int64 *)(a2 + 8) = a1;
    *(unsigned int *)(a2 + 16) = (unsigned int)(v_rbp);
    *(unsigned int *)(a2 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 15786097)));
    goto loc_002F3808;
loc_002F385A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 15779963) + 12)) == 0) goto loc_002F3B07;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11771857))) << (12));
    if (*(unsigned __int64 *)(v_rip + 12590158) == 0) goto loc_002F3B07;
loc_002F3889:
    if ((*(unsigned __int64 *)(v_rip + 12590158)) == (v_rip + 12590128)) goto loc_002F3B07;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48)) == (*(unsigned __int64 *)(v_rip + 13447792))) goto loc_002F3A8A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48)) == (*(unsigned __int64 *)(v_rip + 13447891))) goto loc_002F3A8A;
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11812058))) + (*(unsigned int *)(v_rip + 11812055)));
loc_002F38D9:
    if ((unsigned int)(v_r11) == 0) goto loc_002F3A96;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48)) >> (9);
    a4 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12590158) + 64))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48));
    a1 = (a1) & (v_rip + 12590128);
    a1 = (a1) + (a2 - 1);
    v_stack_m20 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a2 - 1);
    a1 = (a1) + (a2 - 1);
    v_stack_m18 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a2 - 1);
    a1 = (a1) + (a2 - 1);
    v_stack_m10 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a2 - 1);
    a1 = (a1) + (a2 - 1);
    v_stack_m8 = a1;
loc_002F3964:
    v_rbp = (4) - 1;
    v_r14 = (unsigned int)((4) - 1);
    if ((*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)) < (*(unsigned __int64 *)(v_rip + 15779963) + (int)((unsigned int)(a2)) + (int)((unsigned int)(a2)) * 2 * 8)) goto loc_002F39AD;
    if ((*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)) > a2) goto loc_002F39AD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)))) & (1)) == 0) goto loc_002F39D0;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)))) & (66)) != 0) ? 1 : 0;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a2)) & ((unsigned __int8)(a3))) == 0) goto loc_002F39FA;
loc_002F3999:
loc_002F39AD:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)))) & (1)) == 0) goto loc_002F39D0;
    if (sign_flag) goto loc_002F39BD;
    if (v_rbp == 1) goto loc_002F39D0;
    goto loc_002F3964;
loc_002F39BD:
    if ((unsigned int)(v_r14) != 0) {
        a4 = (a4) + (0x1FFFFFULL);
        a4 = (a4) & (0xFFFFFFFFFFE00000ULL);
    }
    if (a4 == 0) goto loc_002F3A96;
    a1 = ((unsigned int)((unsigned int)(v_r11))) + (a4);
loc_002F39DF:
    if ((*(unsigned __int64 *)(a2)) < a1) goto loc_002F3A60;
loc_002F39E4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 15785566))) != 0) goto loc_002F3AA1;
loc_002F39F2:
    goto loc_002F3889;
loc_002F39FA:
    if (((*(unsigned __int64 *)(v_rip + 13447299)) & (0x600000ULL)) == 0) goto loc_002F3999;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002F3999;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002F3999;
    v_r10 = (*(unsigned __int64 *)(v_stack_m28 + 4 * 8 + 24)) >> (3);
    v_r10 = (unsigned int)((v_r10) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) & (32)) != 0) {
        a1 = (a1) | (32);
    }
    result = (a1) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) & (66)) == 0) { result = a1; }
    goto loc_002F3999;
loc_002F3A60:
    if ((*(unsigned __int64 *)(a2)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48))) goto loc_002F39E4;
    a1 = (unsigned int)((a1) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48))));
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158)) + 16);
    *(unsigned int *)(a2 + 16) = (unsigned int)(a1);
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48);
    *(unsigned int *)(a2 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158)) + 24)));
    goto loc_002F380C;
loc_002F3A8A:
    goto loc_002F38D9;
loc_002F3A96:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158)) + 64))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48));
    goto loc_002F39DF;
loc_002F3AA1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158)) + 16)) < a1) goto loc_002F39F2;
    result = ((unsigned int)((unsigned int)(v_r15))) + (a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158)) + 16)) >= result) goto loc_002F39F2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48)) == (*(unsigned __int64 *)(v_rip + 13447272))) goto loc_002F39F2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12590158) + 48)) == (*(unsigned __int64 *)(v_rip + 13447371))) goto loc_002F39F2;
    *(unsigned __int64 *)(a2 + 8) = a1;
    *(unsigned __int64 *)(a2) = v_rip + 15785878;
    *(unsigned int *)(a2 + 16) = (unsigned int)(v_r15);
    *(unsigned int *)(a2 + 20) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8));
    goto loc_002F380C;
loc_002F3AF5:
    goto loc_002F36EC;
loc_002F3AFD:
    v_stack_p38 = 1;
    goto loc_002F377E;
loc_002F3B07:
    v_rbx = 0;
    goto loc_002F380C;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpxLookupFunctionTable(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (64);
    Arg1 = 0;
    *(uint64_t *)(arg2 + 0x8) = 0;
    *(uint32_t *)(arg2 + 0x10) = 0;
    if ((((uint8_t)(Arg1 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + 0x8))))) != 0) goto loc_002F3758;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4))))) == ((uint32_t)(Arg1 + 1))) goto loc_002F374C;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB3A1C6))) << (12));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4)))) - 1);
loc_002F3680:
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1 + 1))))) goto loc_002F374A;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1 + 1)) + local_r11 * 1) >> (1));
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x20))) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x18));
    if (0 < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x18))) goto loc_002F36C7;
    if (0 <= local_rsi) goto loc_002F36BC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xF0E191))) != 0) goto loc_002F3714;
loc_002F36BC:
    if (0 < Arg2) goto loc_002F36D1;
loc_002F36C1:
    goto loc_002F3680;
loc_002F36C7:
    if ((uint32_t)(result) == 0) goto loc_002F374A;
    goto loc_002F3680;
loc_002F36D1:
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint64_t *)(arg2 + 0x10) = v_xmm1;
loc_002F36E8:
loc_002F36EC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + 0x8))))) goto loc_002F3758;
loc_002F36F5:
    return *(uint64_t *)(arg2);
loc_002F3714:
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < Arg2) goto loc_002F36D1;
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) + (Arg2);
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) >= Arg1) goto loc_002F36C1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x18)) == (*(uint64_t *)(v_rip + 0xCD33FE))) goto loc_002F36C1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x18)) == (*(uint64_t *)(v_rip + 0xCD3465))) goto loc_002F36BC;
    *(uint64_t *)(arg2) = v_rip + 15787017;
    *(void **)(arg2 + 0x8) = Arg2;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)(result + 1);
    goto loc_002F36E8;
loc_002F374A:
    Arg1 = 0;
loc_002F374C:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + 0xC)) == 0) goto loc_002F3AF5;
loc_002F3758:
    local_r13 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC53DEE)))) & (3)) != 0) goto loc_002F3AFD;
    v_stack_p38 = 0;
    result = MmLockLoadedModuleListShared(Arg1, Arg2, *(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C9B4) + (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 2 * 8 + 0x18));
loc_002F377E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C87B))))) == 1) goto loc_002F385A;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB3A0A4))) << (12));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C87B)))) - 1);
loc_002F37A0:
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg1 + 1))) goto loc_002F385A;
    Arg2 = (uint32_t)((Arg1 + 1 + local_r10 * 1) >> (1));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x20))) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x18));
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x18))) goto loc_002F37E7;
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) <= (*(uint64_t *)(v_stack_m28 + 0x48))) goto loc_002F37DC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xF0E071))) != 0) goto loc_002F3824;
loc_002F37DC:
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < Arg1) goto loc_002F37F1;
loc_002F37E1:
    goto loc_002F37A0;
loc_002F37E7:
    if ((uint32_t)(Arg2) == 0) goto loc_002F385A;
    goto loc_002F37A0;
loc_002F37F1:
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint64_t *)(arg2 + 0x10) = v_xmm1;
loc_002F3808:
loc_002F380C:
    result = (int32_t)((uint32_t)(Arg2));
    if (v_stack_p38 == 0) {
        Arg1 = (uint8_t)((uint8_t)(result));
        result = MmUnlockLoadedModuleListShared(Arg1, Arg2, *(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(Arg2)) + (int32_t)((uint32_t)(Arg2)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x18));
    }
    goto loc_002F36F5;
loc_002F3824:
    if ((*(uint64_t *)(arg2)) < Arg1) goto loc_002F37F1;
    result = ((uint32_t)((uint32_t)(local_rbp))) + (Arg1);
    if ((*(uint64_t *)(arg2)) >= result) goto loc_002F37E1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x18)) == (*(uint64_t *)(v_rip + 0xCD32EE))) goto loc_002F37E1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(arg2)) + (int32_t)((uint32_t)(arg2)) * 2 * 8 + 0x18)) == (*(uint64_t *)(v_rip + 0xCD3355))) goto loc_002F37DC;
    *(uint64_t *)(arg2) = v_rip + 15786763;
    *(uint64_t *)(arg2 + 0x8) = Arg1;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(local_rbp);
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xF0E071)));
    goto loc_002F3808;
loc_002F385A:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0xF0C87B) + 0xC)) == 0) goto loc_002F3B07;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB39FD1))) << (12));
    if (*(uint64_t *)(v_rip + 0xC01C4E) == 0) goto loc_002F3B07;
loc_002F3889:
    if ((*(uint64_t *)(v_rip + 0xC01C4E)) == (v_rip + 12590128)) goto loc_002F3B07;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30)) == (*(uint64_t *)(v_rip + 0xCD3270))) goto loc_002F3A8A;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30)) == (*(uint64_t *)(v_rip + 0xCD32D3))) goto loc_002F3A8A;
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB43CDA))) + (*(uint32_t *)(v_rip + 0xB43CD7)));
loc_002F38D9:
    if ((uint32_t)(local_r11) == 0) goto loc_002F3A96;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30)) >> (9);
    a4 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x40))) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30));
    Arg1 = (Arg1) & (v_rip + 12590128);
    Arg1 = (Arg1) + (Arg2 - 1);
    v_stack_m20 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg2 - 1);
    Arg1 = (Arg1) + (Arg2 - 1);
    v_stack_m18 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg2 - 1);
    Arg1 = (Arg1) + (Arg2 - 1);
    v_stack_m10 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg2 - 1);
    Arg1 = (Arg1) + (Arg2 - 1);
    v_stack_m8 = Arg1;
loc_002F3964:
    local_rbp = (4) - 1;
    local_r14 = (uint32_t)((4) - 1);
    if ((*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)) < (*(uint64_t *)(v_rip + 0xF0C87B) + (int32_t)((uint32_t)(Arg2)) + (int32_t)((uint32_t)(Arg2)) * 2 * 8)) goto loc_002F39AD;
    if ((*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)) > Arg2) goto loc_002F39AD;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)))) & (1)) == 0) goto loc_002F39D0;
    a3 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)))) & (66)) != 0) ? 1 : 0;
    Arg2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg2)) & ((uint8_t)(a3))) == 0) goto loc_002F39FA;
loc_002F3999:
loc_002F39AD:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)))) & (1)) == 0) goto loc_002F39D0;
    if (sign_flag) goto loc_002F39BD;
    if (local_rbp == 1) goto loc_002F39D0;
    goto loc_002F3964;
loc_002F39BD:
    if ((uint32_t)(local_r14) != 0) {
        a4 = (a4) + (0x1FFFFFULL);
        a4 = (a4) & (0xFFFFFFFFFFE00000ULL);
    }
    if (a4 == 0) goto loc_002F3A96;
    Arg1 = ((uint32_t)((uint32_t)(local_r11))) + (a4);
loc_002F39DF:
    if ((*(uint64_t *)(arg2)) < Arg1) goto loc_002F3A60;
loc_002F39E4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xF0DE5E))) != 0) goto loc_002F3AA1;
loc_002F39F2:
    goto loc_002F3889;
loc_002F39FA:
    if (((*(uint64_t *)(v_rip + 0xCD3083)) & (0x600000ULL)) == 0) goto loc_002F3999;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002F3999;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002F3999;
    local_r10 = (*(uint64_t *)(v_stack_m28 + 0x4 * 8 + 0x18)) >> (3);
    local_r10 = (uint32_t)((local_r10) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) & (32)) != 0) {
        Arg1 = (Arg1) | (32);
    }
    result = (Arg1) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) & (66)) == 0) { result = Arg1; }
    goto loc_002F3999;
loc_002F3A60:
    if ((*(uint64_t *)(arg2)) < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30))) goto loc_002F39E4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30))));
    *(uint64_t *)(arg2) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E)) + 0x10);
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg1);
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30);
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E)) + 0x18)));
    goto loc_002F380C;
loc_002F3A8A:
    goto loc_002F38D9;
loc_002F3A96:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E)) + 0x40))) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30));
    goto loc_002F39DF;
loc_002F3AA1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E)) + 0x10)) < Arg1) goto loc_002F39F2;
    result = ((uint32_t)((uint32_t)(local_r15))) + (Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E)) + 0x10)) >= result) goto loc_002F39F2;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30)) == (*(uint64_t *)(v_rip + 0xCD3068))) goto loc_002F39F2;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01C4E) + 0x30)) == (*(uint64_t *)(v_rip + 0xCD30CB))) goto loc_002F39F2;
    *(uint64_t *)(arg2 + 0x8) = Arg1;
    *(uint64_t *)(arg2) = v_rip + 15785878;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(local_r15);
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8));
    goto loc_002F380C;
loc_002F3AF5:
    goto loc_002F36EC;
loc_002F3AFD:
    v_stack_p38 = 1;
    goto loc_002F377E;
loc_002F3B07:
    local_rbx = 0;
    goto loc_002F380C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x14` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F3610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
