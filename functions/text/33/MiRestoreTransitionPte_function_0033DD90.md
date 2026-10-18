# MiRestoreTransitionPte

- RVA: `0x0033DD90`–`0x0033E25D` (길이 `1,229` bytes)
- VA: `0x000000014033DD90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077208`
- 디코드: `311`개 명령, `1,229/1,229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0033DE77` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0033DECA` → [MiMapPageInHyperSpaceWorker](MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x0033DEEF` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x0033DF6F` → [MiDecrementShareCountEx](MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x0033DFE8` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x0033E013` → [MiLogStandbyRepurpose](../46/MiLogStandbyRepurpose_function_0046BD14.md) (function, `0x0046BD14`)
- `0x0033E071` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x0033E082` → [MI_IS_RESET_PTE](../38/MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x0033E092` → [MiClearResetPfn](../47/MiClearResetPfn_function_00473B3C.md) (function, `0x00473B3C`)
- `0x0033E0D6` → [MiDereferenceControlAreaPfnList](../2A/MiDereferenceControlAreaPfnList_function_002A45E8.md) (function, `0x002A45E8`)
- `0x0033E125` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0033E130` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0033E13B` → [MI_IS_RESET_PTE](../38/MI_IS_RESET_PTE_function_00383E80.md) (function, `0x00383E80`)
- `0x0033E147` → [MiClearResetPfn](../47/MiClearResetPfn_function_00473B3C.md) (function, `0x00473B3C`)
- `0x0033E14F` → [MiGetTopLevelPfn](../2B/MiGetTopLevelPfn_function_002B44E0.md) (function, `0x002B44E0`)
- `0x0033E15A` → [MiGetPageTablePfnBuddyRaw](../2B/MiGetPageTablePfnBuddyRaw_function_002B4470.md) (function, `0x002B4470`)
- `0x0033E1A1` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x0033E1B8` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x0033E1CF` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x0033E1F7` → [VslRemoveProtectedPage](../40/VslRemoveProtectedPage_function_004079D0.md) (function, `0x004079D0`)
- `0x0033E205` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x0033E234` → [VslMakeProtectedPageExecutable](../40/VslMakeProtectedPageExecutable_function_00407A50.md) (function, `0x00407A50`)
- `0x0033E24F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiRelinkStandbyPage](../2B/MiRelinkStandbyPage_function_002B9D30.md) at `0x002B9DC2`
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA76C`
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA8B9`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F7399`
- [sub_0033D4D7](Unknown_function_0033D4D7.md) at `0x0033DA44`
- [MiHandleInPageError](../36/MiHandleInPageError_function_00368EBC.md) at `0x00368ECA`
- [MiWriteCompletePfn](../37/MiWriteCompletePfn_function_003737C4.md) at `0x003739D5`
- [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) at `0x0037598C`
- [MiReuseStandbyPage](../44/MiReuseStandbyPage_function_0044CA90.md) at `0x0044CAB2`
- [MiRepointPteAtExtendedStandby](../68/MiRepointPteAtExtendedStandby_function_0068B6F4.md) at `0x0068B757`
- [MiRepointPteAtExtendedStandby](../68/MiRepointPteAtExtendedStandby_function_0068B6F4.md) at `0x0068B7D7`

### Static image references
- `0x0033DE57` → RVA `0x00E30088` (`.data`; read)
- `0x0033DF3B` → RVA `0x00010880` (`.rdata`; read)
- `0x0033E0AB` → RVA `0x00E2DC80` (`.data`; read)
- `0x0033E0E2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0033E11B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033DD90  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0033DD94  55                              push rbp
0033DD95  53                              push rbx
0033DD96  56                              push rsi
0033DD97  57                              push rdi
0033DD98  41 54                           push r12
0033DD9A  41 55                           push r13
0033DD9C  41 56                           push r14
0033DD9E  41 57                           push r15
0033DDA0  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0033DDA5  48 81 EC A8 00 00 00            sub rsp, 0xa8
0033DDAC  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0033DDB0  45 33 F6                        xor r14d, r14d
0033DDB3  4C 8B E8                        mov r13, rax
0033DDB6  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
0033DDC0  49 C1 ED 35                     shr r13, 0x35
0033DDC4  0F 57 C0                        xorps xmm0, xmm0
0033DDC7  48 C1 E8 3C                     shr rax, 0x3c
0033DDCB  41 83 E5 01                     and r13d, 1
0033DDCF  24 07                           and al, 7
0033DDD1  48 8B F9                        mov rdi, rcx
0033DDD4  49 BF AB AA AA AA AA AA AA AA   movabs r15, 0xaaaaaaaaaaaaaaab
0033DDDE  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
0033DDE2  3C 03                           cmp al, 3
0033DDE4  0F 84 D8 03 00 00               je 0x14033e1c2
0033DDEA  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033DDEE  BE 00 04 00 00                  mov esi, 0x400
0033DDF3  48 BB FF FF FF FF FF 00 00 00   movabs rbx, 0xffffffffff
0033DDFD  48 85 C0                        test rax, rax
0033DE00  0F 88 43 02 00 00               js 0x14033e049
0033DE06  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
0033DE0A  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0033DE14  48 0B D8                        or rbx, rax
0033DE17  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0033DE1A  C0 E8 02                        shr al, 2
0033DE1D  A8 01                           test al, 1
0033DE1F  0F 84 12 03 00 00               je 0x14033e137
0033DE25  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033DE29  49 8B CC                        mov rcx, r12
0033DE2C  48 8B D7                        mov rdx, rdi
0033DE2F  48 2B D1                        sub rdx, rcx
0033DE32  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0033DE3C  48 C1 FA 04                     sar rdx, 4
0033DE40  48 23 C1                        and rax, rcx
0033DE43  49 0F AF D7                     imul rdx, r15
0033DE47  48 3B C2                        cmp rax, rdx
0033DE4A  0F 84 05 04 00 00               je 0x14033e255
0033DE50  48 8B D9                        mov rbx, rcx
0033DE53  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033DE57  48 8B 0D 2A 22 AF 00            mov rcx, qword ptr [rip + 0xaf222a]
0033DE5E  48 C1 E8 2B                     shr rax, 0x2b
0033DE62  25 FF 03 00 00                  and eax, 0x3ff
0033DE67  4C 8B 24 C1                     mov r12, qword ptr [rcx + rax*8]
0033DE6B  48 8D 4D 67                     lea rcx, [rbp + 0x67]
0033DE6F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0033DE73  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
0033DE77  E8 24 4A F4 FF                  call 0x1402828a0
0033DE7C  48 8B C8                        mov rcx, rax
0033DE7F  48 23 CE                        and rcx, rsi
0033DE82  48 F7 D9                        neg rcx
0033DE85  48 1B D2                        sbb rdx, rdx
0033DE88  48 81 E2 08 F8 FF FF            and rdx, 0xfffffffffffff808
0033DE8F  48 83 C2 F7                     add rdx, -9
0033DE93  48 23 D0                        and rdx, rax
0033DE96  48 89 55 67                     mov qword ptr [rbp + 0x67], rdx
0033DE9A  4D 85 F6                        test r14, r14
0033DE9D  0F 85 71 02 00 00               jne 0x14033e114
0033DEA3  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0033DEA7  48 23 CB                        and rcx, rbx
0033DEAA  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033DEB4  48 8D 34 49                     lea rsi, [rcx + rcx*2]
0033DEB8  48 C1 E6 04                     shl rsi, 4
0033DEBC  48 8B C0                        mov rax, rax
0033DEBF  33 D2                           xor edx, edx
0033DEC1  41 B8 00 00 00 80               mov r8d, 0x80000000
0033DEC7  48 03 F0                        add rsi, rax
0033DECA  E8 41 4C FF FF                  call 0x140332b10
0033DECF  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0033DED3  48 C1 E9 03                     shr rcx, 3
0033DED7  81 E1 FF 01 00 00               and ecx, 0x1ff
0033DEDD  4C 8D 34 C8                     lea r14, [rax + rcx*8]
0033DEE1  48 8B 5D 67                     mov rbx, qword ptr [rbp + 0x67]
0033DEE5  49 8B CE                        mov rcx, r14
0033DEE8  48 89 5D 77                     mov qword ptr [rbp + 0x77], rbx
0033DEEC  45 33 FF                        xor r15d, r15d
0033DEEF  E8 0C 1C F0 FF                  call 0x14023fb00
0033DEF4  85 C0                           test eax, eax
0033DEF6  0F 85 A1 02 00 00               jne 0x14033e19d
0033DEFC  49 89 1E                        mov qword ptr [r14], rbx
0033DEFF  45 85 FF                        test r15d, r15d
0033DF02  0F 85 AA 02 00 00               jne 0x14033e1b2
0033DF08  48 85 F6                        test rsi, rsi
0033DF0B  74 3C                           je 0x14033df49
0033DF0D  49 C1 EE 09                     shr r14, 9
0033DF11  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0033DF1B  4C 23 F0                        and r14, rax
0033DF1E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0033DF28  4C 03 F0                        add r14, rax
0033DF2B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0033DF34  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0033DF3B  48 8B 05 3E 29 CD FF            mov rax, qword ptr [rip - 0x32d6c2]
0033DF42  48 83 21 00                     and qword ptr [rcx], 0
0033DF46  49 89 06                        mov qword ptr [r14], rax
0033DF49  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033DF4D  48 85 C0                        test rax, rax
0033DF50  0F 88 46 01 00 00               js 0x14033e09c
0033DF56  48 85 F6                        test rsi, rsi
0033DF59  74 28                           je 0x14033df83
0033DF5B  33 DB                           xor ebx, ebx
0033DF5D  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
0033DF64  0F 82 76 01 00 00               jb 0x14033e0e0
0033DF6A  33 D2                           xor edx, edx
0033DF6C  48 8B CE                        mov rcx, rsi
0033DF6F  E8 FC 5F FF FF                  call 0x140333f70
0033DF74  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0033DF7E  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0033DF83  45 85 ED                        test r13d, r13d
0033DF86  0F 85 8C 00 00 00               jne 0x14033e018
0033DF8C  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
0033DF90  0F 57 C0                        xorps xmm0, xmm0
0033DF93  0F 57 C9                        xorps xmm1, xmm1
0033DF96  48 8B CA                        mov rcx, rdx
0033DF99  49 B9 FF FF FF FF FF FF FF 8F   movabs r9, 0x8fffffffffffffff
0033DFA3  48 8B C2                        mov rax, rdx
0033DFA6  49 23 C9                        and rcx, r9
0033DFA9  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
0033DFAD  48 89 55 0F                     mov qword ptr [rbp + 0xf], rdx
0033DFB1  0F 11 4D D7                     movups xmmword ptr [rbp - 0x29], xmm1
0033DFB5  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
0033DFB9  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0033DFBD  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0033DFC1  0F 11 4D B7                     movups xmmword ptr [rbp - 0x49], xmm1
0033DFC5  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
0033DFC9  F0 48 0F B1 4F 28               lock cmpxchg qword ptr [rdi + 0x28], rcx
0033DFCF  48 3B D0                        cmp rdx, rax
0033DFD2  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0033DFD6  4C 8B C0                        mov r8, rax
0033DFD9  75 52                           jne 0x14033e02d
0033DFDB  F6 45 6F 01                     test byte ptr [rbp + 0x6f], 1
0033DFDF  0F 85 16 01 00 00               jne 0x14033e0fb
0033DFE5  48 8B CF                        mov rcx, rdi
0033DFE8  E8 03 47 FE FF                  call 0x1403226f0
0033DFED  44 8B D0                        mov r10d, eax
0033DFF0  F0 43 FF 84 94 20 1C 00 00      lock inc dword ptr [r12 + r10*4 + 0x1c20]
0033DFF9  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0033DFFC  48 8B D7                        mov rdx, rdi
0033DFFF  89 45 67                        mov dword ptr [rbp + 0x67], eax
0033E002  49 8B CC                        mov rcx, r12
0033E005  C1 E8 18                        shr eax, 0x18
0033E008  24 F8                           and al, 0xf8
0033E00A  88 45 6A                        mov byte ptr [rbp + 0x6a], al
0033E00D  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0033E010  89 47 20                        mov dword ptr [rdi + 0x20], eax
0033E013  E8 FC DC 12 00                  call 0x14046bd14
0033E018  48 81 C4 A8 00 00 00            add rsp, 0xa8
0033E01F  41 5F                           pop r15
0033E021  41 5E                           pop r14
0033E023  41 5D                           pop r13
0033E025  41 5C                           pop r12
0033E027  5F                              pop rdi
0033E028  5E                              pop rsi
0033E029  5B                              pop rbx
0033E02A  5D                              pop rbp
0033E02B  C3                              ret
0033E02C  CC                              int3
0033E02D  49 8B C8                        mov rcx, r8
0033E030  4C 89 45 0F                     mov qword ptr [rbp + 0xf], r8
0033E034  49 8B C0                        mov rax, r8
0033E037  4D 23 C1                        and r8, r9
0033E03A  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
0033E03E  F0 4C 0F B1 47 28               lock cmpxchg qword ptr [rdi + 0x28], r8
0033E044  48 3B C8                        cmp rcx, rax
0033E047  EB 89                           jmp 0x14033dfd2
0033E049  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033E04D  48 0F BA E0 28                  bt rax, 0x28
0033E052  72 0D                           jb 0x14033e061
0033E054  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0033E058  48 85 C0                        test rax, rax
0033E05B  0F 89 B1 01 00 00               jns 0x14033e212
0033E061  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0033E064  48 85 C6                        test rsi, rax
0033E067  0F 85 E6 FD FF FF               jne 0x14033de53
0033E06D  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0033E071  E8 BA 14 03 00                  call 0x14036f530
0033E076  85 C0                           test eax, eax
0033E078  0F 85 D5 FD FF FF               jne 0x14033de53
0033E07E  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0033E082  E8 F9 5D 04 00                  call 0x140383e80
0033E087  85 C0                           test eax, eax
0033E089  0F 84 C4 FD FF FF               je 0x14033de53
0033E08F  48 8B CF                        mov rcx, rdi
0033E092  E8 A5 5A 13 00                  call 0x140473b3c
0033E097  E9 B7 FD FF FF                  jmp 0x14033de53
0033E09C  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0033E0A0  48 0F BA E1 0A                  bt rcx, 0xa
0033E0A5  0F 83 AB FE FF FF               jae 0x14033df56
0033E0AB  48 8B 05 CE FB AE 00            mov rax, qword ptr [rip + 0xaefbce]
0033E0B2  48 85 C0                        test rax, rax
0033E0B5  74 0B                           je 0x14033e0c2
0033E0B7  F6 C1 10                        test cl, 0x10
0033E0BA  75 06                           jne 0x14033e0c2
0033E0BC  48 F7 D0                        not rax
0033E0BF  48 23 C8                        and rcx, rax
0033E0C2  48 C1 F9 10                     sar rcx, 0x10
0033E0C6  41 B9 03 00 00 00               mov r9d, 3
0033E0CC  48 8B D1                        mov rdx, rcx
0033E0CF  48 8B 09                        mov rcx, qword ptr [rcx]
0033E0D2  45 8D 41 FE                     lea r8d, [r9 - 2]
0033E0D6  E8 0D 65 F6 FF                  call 0x1402a45e8
0033E0DB  E9 76 FE FF FF                  jmp 0x14033df56
0033E0E0  FF C3                           inc ebx
0033E0E2  85 1D C4 71 C8 00               test dword ptr [rip + 0xc871c4], ebx
0033E0E8  74 31                           je 0x14033e11b
0033E0EA  F3 90                           pause
0033E0EC  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0033E0F0  48 85 C0                        test rax, rax
0033E0F3  0F 89 64 FE FF FF               jns 0x14033df5d
0033E0F9  EB E5                           jmp 0x14033e0e0
0033E0FB  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0033E0FE  89 45 67                        mov dword ptr [rbp + 0x67], eax
0033E101  C1 E8 18                        shr eax, 0x18
0033E104  24 F8                           and al, 0xf8
0033E106  88 45 6A                        mov byte ptr [rbp + 0x6a], al
0033E109  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0033E10C  89 47 20                        mov dword ptr [rdi + 0x20], eax
0033E10F  E9 04 FF FF FF                  jmp 0x14033e018
0033E114  33 F6                           xor esi, esi
0033E116  E9 C6 FD FF FF                  jmp 0x14033dee1
0033E11B  8B 05 97 89 C8 00               mov eax, dword ptr [rip + 0xc88997]
0033E121  A8 40                           test al, 0x40
0033E123  74 C5                           je 0x14033e0ea
0033E125  E8 66 13 FD FF                  call 0x14030f490
0033E12A  84 C0                           test al, al
0033E12C  74 BC                           je 0x14033e0ea
0033E12E  8B CB                           mov ecx, ebx
0033E130  E8 2B 13 FD FF                  call 0x14030f460
0033E135  EB B5                           jmp 0x14033e0ec
0033E137  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0033E13B  E8 40 5D 04 00                  call 0x140383e80
0033E140  85 C0                           test eax, eax
0033E142  74 08                           je 0x14033e14c
0033E144  48 8B CF                        mov rcx, rdi
0033E147  E8 F0 59 13 00                  call 0x140473b3c
0033E14C  48 8B CF                        mov rcx, rdi
0033E14F  E8 8C 63 F7 FF                  call 0x1402b44e0
0033E154  48 8B C8                        mov rcx, rax
0033E157  4C 8B C0                        mov r8, rax
0033E15A  E8 11 63 F7 FF                  call 0x1402b4470
0033E15F  4C 3B C7                        cmp r8, rdi
0033E162  74 0F                           je 0x14033e173
0033E164  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0033E16E  F0 49 21 48 18                  lock and qword ptr [r8 + 0x18], rcx
0033E173  F0 48 FF 88 88 02 00 00         lock dec qword ptr [rax + 0x288]
0033E17B  8B 88 B8 04 00 00               mov ecx, dword ptr [rax + 0x4b8]
0033E181  C1 E9 18                        shr ecx, 0x18
0033E184  80 E1 30                        and cl, 0x30
0033E187  80 F9 20                        cmp cl, 0x20
0033E18A  0F 85 95 FC FF FF               jne 0x14033de25
0033E190  F0 48 FF 80 D0 04 00 00         lock inc qword ptr [rax + 0x4d0]
0033E198  E9 88 FC FF FF                  jmp 0x14033de25
0033E19D  48 8D 55 77                     lea rdx, [rbp + 0x77]
0033E1A1  E8 C2 69 F5 FF                  call 0x140294b68
0033E1A6  48 8B 5D 77                     mov rbx, qword ptr [rbp + 0x77]
0033E1AA  44 8B F8                        mov r15d, eax
0033E1AD  E9 4A FD FF FF                  jmp 0x14033defc
0033E1B2  48 8B D3                        mov rdx, rbx
0033E1B5  49 8B CE                        mov rcx, r14
0033E1B8  E8 EF 6C F5 FF                  call 0x140294eac
0033E1BD  E9 46 FD FF FF                  jmp 0x14033df08
0033E1C2  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0033E1C6  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0033E1CA  BA 01 00 00 00                  mov edx, 1
0033E1CF  E8 4C 72 F4 FF                  call 0x140285420
0033E1D4  85 C0                           test eax, eax
0033E1D6  74 28                           je 0x14033e200
0033E1D8  49 8B CC                        mov rcx, r12
0033E1DB  48 8B DF                        mov rbx, rdi
0033E1DE  45 33 C0                        xor r8d, r8d
0033E1E1  48 2B D9                        sub rbx, rcx
0033E1E4  48 C1 FB 04                     sar rbx, 4
0033E1E8  49 0F AF DF                     imul rbx, r15
0033E1EC  48 8B CB                        mov rcx, rbx
0033E1EF  A8 20                           test al, 0x20
0033E1F1  75 3F                           jne 0x14033e232
0033E1F3  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0033E1F7  E8 D4 97 0C 00                  call 0x1404079d0
0033E1FC  85 C0                           test eax, eax
0033E1FE  78 3B                           js 0x14033e23b
0033E200  33 D2                           xor edx, edx
0033E202  48 8B CF                        mov rcx, rdi
0033E205  E8 46 41 F6 FF                  call 0x1402a2350
0033E20A  48 8B CF                        mov rcx, rdi
0033E20D  E9 D8 FB FF FF                  jmp 0x14033ddea
0033E212  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0033E216  48 85 C0                        test rax, rax
0033E219  0F 84 42 FE FF FF               je 0x14033e061
0033E21F  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0033E229  48 09 41 08                     or qword ptr [rcx + 8], rax
0033E22D  E9 21 FC FF FF                  jmp 0x14033de53
0033E232  33 D2                           xor edx, edx
0033E234  E8 17 98 0C 00                  call 0x140407a50
0033E239  EB C1                           jmp 0x14033e1fc
0033E23B  4C 21 74 24 20                  and qword ptr [rsp + 0x20], r14
0033E240  45 33 C9                        xor r9d, r9d
0033E243  4C 8B C3                        mov r8, rbx
0033E246  BA 0B 15 05 00                  mov edx, 0x5150b
0033E24B  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0033E24F  E8 0C F4 1B 00                  call 0x1404fd660
0033E254  CC                              int3
0033E255  4C 8B F3                        mov r14, rbx
0033E258  E9 F3 FB FF FF                  jmp 0x14033de50
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRestoreTransitionPte(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pB;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (168);
    v_r14 = 0;
    v_r13 = (*(unsigned __int64 *)(a1 + 40)) >> (53);
    result = (*(unsigned __int64 *)(a1 + 40)) >> (60);
    v_r13 = (unsigned int)((v_r13) & (1));
    result = (unsigned __int8)((result) & (7));
    v_stack_mB8 = v_xmm0;
    if (((unsigned __int8)(result)) == 3) goto loc_0033E1C2;
loc_0033DDEA:
    if (sign_flag) goto loc_0033E049;
    v_rbx = (*(unsigned __int64 *)(a1 + 8)) | (*(unsigned __int64 *)(a1 + 40));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0033E137;
loc_0033DE25:
    a2 = (a1) - (v_r12);
    a2 = (a2) >> (4);
    result = (*(unsigned __int64 *)(a1 + 40)) & (v_r12);
    a2 = (a2) * (v_r15);
    if (result == a2) goto loc_0033E255;
loc_0033DE50:
loc_0033DE53:
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_p8 = *(unsigned __int64 *)(a1 + 16);
    result = MI_READ_PTE_LOCK_FREE(v_stack_p8, a2, a3, a4);
    a1 = (result) & ((unsigned int)(0x400ULL));
    a1 = -(a1);
    a2 = (a2) & (0xFFFFFFFFFFFFF808ULL);
    a2 = (a2) + (-9);
    a2 = (a2) & (result);
    v_stack_p8 = a2;
    if (0 != 0) goto loc_0033E114;
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (v_r12);
    v_rsi = (a1 + a1 * 2) << (4);
    a2 = 0;
    v_rsi = (v_rsi) + (result);
    result = MiMapPageInHyperSpaceWorker(a1, a2, (unsigned int)(0x80000000ULL), a4);
    a1 = (*(unsigned __int64 *)(a1 + 8)) >> (3);
    a1 = (unsigned int)((a1) & (511));
loc_0033DEE1:
    v_stack_p18 = v_stack_p8;
    v_r15 = 0;
    result = MiPteInShadowRange(result + a1 * 8, a2, (unsigned int)(0x80000000ULL), a4);
    if ((unsigned int)(result) != 0) goto loc_0033E19D;
loc_0033DEFC:
    *(unsigned __int64 *)(result + a1 * 8) = v_stack_p8;
    if (0 != 0) goto loc_0033E1B2;
loc_0033DF08:
    v_r14 = result + a1 * 8;
    if (v_rsi != 0) {
        v_r14 = (result + a1 * 8) >> (9);
        v_r14 = (v_r14) & (result);
        v_r14 = (v_r14) + (result);
        result = *(unsigned __int64 *)(gs_base + (0 + 32));
        a1 = *(unsigned __int64 *)(result + 34872);
        result = *(unsigned __int64 *)(v_rip - 3331778);
        *(unsigned __int64 *)(v_r14) = result;
    }
    if (sign_flag) goto loc_0033E09C;
loc_0033DF56:
    if (v_rsi == 0) goto loc_0033DF83;
    v_rbx = 0;
loc_0033DF5D:
    if (condition_is_below) goto loc_0033E0E0;
    a2 = 0;
    result = MiDecrementShareCountEx(v_rsi, a2, (unsigned int)(0x80000000ULL), a4);
loc_0033DF83:
    if ((unsigned int)(v_r13) != 0) goto loc_0033E018;
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (a4);
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m88 = v_xmm1;
    v_stack_m80 = a1;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
loc_0033DFD2:
    v_stack_m80 = *(unsigned __int64 *)(a1 + 40);
    if ((*(unsigned __int64 *)(a1 + 40)) != (*(unsigned __int64 *)(a1 + 40))) goto loc_0033E02D;
    if (((v_stack_p10) & (1)) != 0) goto loc_0033E0FB;
    result = MiGetPfnPriority(a1, *(unsigned __int64 *)(a1 + 40), *(unsigned __int64 *)(a1 + 40), a4);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    result = (unsigned __int8)((result) & (248));
    v_stack_pB = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = MiLogStandbyRepurpose(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11477546) + result * 8), a1, *(unsigned __int64 *)(a1 + 40), a4);
loc_0033E018:
    v_rsp = (v_rsp) + (168);
    return result;
loc_0033E02D:
    v_stack_m50 = *(unsigned __int64 *)(a1 + 40);
    a3 = (*(unsigned __int64 *)(a1 + 40)) & (a4);
    v_stack_m80 = a3;
    goto loc_0033DFD2;
loc_0033E049:
    if ((*(unsigned __int64 *)(a1 + 40)) < (*(unsigned __int64 *)(a1 + 40))) goto loc_0033E061;
    if (!sign_flag) goto loc_0033E212;
loc_0033E061:
    if (((v_rsi) & ((unsigned int)(*(unsigned int *)(a1 + 16)))) != 0) goto loc_0033DE53;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(a1 + 16), a1, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0033DE53;
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(a1 + 16), a1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0033DE53;
    result = MiClearResetPfn(a1, a1, a3, a4);
    goto loc_0033DE53;
loc_0033E09C:
    if (condition_is_above_or_equal) goto loc_0033DF56;
    if (*(unsigned __int64 *)(v_rip + 11467726) == 0) goto loc_0033E0C2;
    result = *(unsigned __int64 *)(v_rip + 11467726);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11467726));
        a1 = (*(unsigned __int64 *)(a1 + 16)) & (result);
    }
    a1 = (a1) >> (16);
    result = MiDereferenceControlAreaPfnList(*(unsigned __int64 *)(a1), a1, 3 - 2, 3);
    goto loc_0033DF56;
loc_0033E0E0:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13136324)) & ((unsigned int)(v_rbx))) == 0) goto loc_0033E11B;
loc_0033E0EA:
loc_0033E0EC:
    if (!sign_flag) goto loc_0033DF5D;
    goto loc_0033E0E0;
loc_0033E0FB:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    result = (unsigned __int8)((result) & (248));
    v_stack_pB = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    goto loc_0033E018;
loc_0033E114:
    v_rsi = 0;
    goto loc_0033DEE1;
loc_0033E11B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13142423)))) & (64)) == 0) goto loc_0033E0EA;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a1), a1, 3 - 2, 3);
    if ((unsigned __int8)(result) == 0) goto loc_0033E0EA;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a1, 3 - 2, 3);
    goto loc_0033E0EC;
loc_0033E137:
    result = MI_IS_RESET_PTE(*(unsigned __int64 *)(a1 + 16), a1, 3 - 2, 3);
    if ((unsigned int)(result) != 0) {
        a1 = a1;
        result = MiClearResetPfn(a1, a1, 3 - 2, 3);
    }
    result = MiGetTopLevelPfn(a1, a1, 3 - 2, 3);
    result = MiGetPageTablePfnBuddyRaw(result, a1, result, 3);
    if (result != a1) {
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 1208))) >> (24));
    a1 = (unsigned __int8)((a1) & (48));
    if (((unsigned __int8)(a1)) != 32) goto loc_0033DE25;
    goto loc_0033DE25;
loc_0033E19D:
    result = MiSanitizeShadowPxe(a1, v_stack_p18, result, 3);
    goto loc_0033DEFC;
loc_0033E1B2:
    result = MiWritePteShadow(v_r14, v_stack_p18, result, 3);
    goto loc_0033DF08;
loc_0033E1C2:
    result = MiGetPagePrivilege(v_r14, 1, v_stack_mB8, 3);
    if ((unsigned int)(result) == 0) goto loc_0033E200;
    a3 = 0;
    v_rbx = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11477546) + result * 8));
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * ((unsigned int)((unsigned int)(result)));
    if ((((unsigned __int8)(result)) & (32)) != 0) goto loc_0033E232;
    result = VslRemoveProtectedPage(v_rbx, v_stack_mB8, a3, 3);
loc_0033E1FC:
    if (sign_flag) goto loc_0033E23B;
loc_0033E200:
    a2 = 0;
    result = MiSetPfnIdentity(a1, a2, a3, 3);
    goto loc_0033DDEA;
loc_0033E212:
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_0033E061;
    goto loc_0033DE53;
loc_0033E232:
    a2 = 0;
    result = VslMakeProtectedPageExecutable(a1, a2, a3, 3);
    goto loc_0033E1FC;
loc_0033E23B:
    a4 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5150BULL), v_rbx, a4);
loc_0033E255:
    goto loc_0033DE50;
}
```

## 5. (Beta) C Style

```c
int64_t MiRestoreTransitionPte(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;
    uint8_t v_stack_pB;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (168);
    local_r14 = 0;
    local_r13 = (*(uint64_t *)(arg1 + 0x28)) >> (53);
    result = (*(uint64_t *)(arg1 + 0x28)) >> (60);
    local_r13 = (uint32_t)((local_r13) & (1));
    result = (uint8_t)((result) & (7));
    v_stack_mB8 = v_xmm0;
    if (((uint8_t)(result)) == 3) goto loc_0033E1C2;
loc_0033DDEA:
    if (sign_flag) goto loc_0033E049;
    local_rbx = (*(uint64_t *)(arg1 + 0x8)) | (*(uint64_t *)(arg1 + 0x28));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0033E137;
loc_0033DE25:
    Arg2 = (Arg1) - (local_r12);
    Arg2 = (Arg2) >> (4);
    result = (*(uint64_t *)(arg1 + 0x28)) & (local_r12);
    Arg2 = (Arg2) * (local_r15);
    if (result == Arg2) goto loc_0033E255;
loc_0033DE50:
loc_0033DE53:
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_p8 = *(uint64_t *)(arg1 + 0x10);
    result = MI_READ_PTE_LOCK_FREE(v_stack_p8, Arg2, a3, a4);
    Arg1 = (result) & ((uint32_t)(0x400ULL));
    Arg1 = -(Arg1);
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF808ULL);
    Arg2 = (Arg2) + (-9);
    Arg2 = (Arg2) & (result);
    v_stack_p8 = Arg2;
    if (0 != 0) goto loc_0033E114;
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (local_r12);
    local_rsi = (Arg1 + Arg1 * 2) << (4);
    Arg2 = 0;
    local_rsi = (local_rsi) + (result);
    result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, (uint32_t)(0x80000000ULL), a4);
    Arg1 = (*(uint64_t *)(arg1 + 0x8)) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
loc_0033DEE1:
    v_stack_p18 = v_stack_p8;
    local_r15 = 0;
    result = MiPteInShadowRange(result + Arg1 * 8, Arg2, (uint32_t)(0x80000000ULL), a4);
    if ((uint32_t)(result) != 0) goto loc_0033E19D;
loc_0033DEFC:
    *(uint64_t *)(result + arg1 * 8) = v_stack_p8;
    if (0 != 0) goto loc_0033E1B2;
loc_0033DF08:
    local_r14 = result + Arg1 * 8;
    if (local_rsi != 0) {
        local_r14 = (result + Arg1 * 8) >> (9);
        local_r14 = (local_r14) & (result);
        local_r14 = (local_r14) + (result);
        result = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg1 = *(uint64_t *)(result + 0x8838);
        result = *(uint64_t *)(v_rip - 0x32D6C2);
        *(uint64_t *)(local_r14) = result;
    }
    if (sign_flag) goto loc_0033E09C;
loc_0033DF56:
    if (local_rsi == 0) goto loc_0033DF83;
    local_rbx = 0;
loc_0033DF5D:
    if (condition_is_below) goto loc_0033E0E0;
    Arg2 = 0;
    result = MiDecrementShareCountEx(local_rsi, Arg2, (uint32_t)(0x80000000ULL), a4);
loc_0033DF83:
    if ((uint32_t)(local_r13) != 0) goto loc_0033E018;
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (a4);
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m88 = v_xmm1;
    v_stack_m80 = Arg1;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
loc_0033DFD2:
    v_stack_m80 = *(uint64_t *)(arg1 + 0x28);
    if ((*(uint64_t *)(arg1 + 0x28)) != (*(uint64_t *)(arg1 + 0x28))) goto loc_0033E02D;
    if (((v_stack_p10) & (1)) != 0) goto loc_0033E0FB;
    result = MiGetPfnPriority(Arg1, *(uint64_t *)(arg1 + 0x28), *(uint64_t *)(arg1 + 0x28), a4);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    result = (uint8_t)((result) & (248));
    v_stack_pB = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = MiLogStandbyRepurpose(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF222A) + result * 8), Arg1, *(uint64_t *)(arg1 + 0x28), a4);
loc_0033E018:
    local_rsp = (local_rsp) + (168);
    return result;
loc_0033E02D:
    v_stack_m50 = *(uint64_t *)(arg1 + 0x28);
    a3 = (*(uint64_t *)(arg1 + 0x28)) & (a4);
    v_stack_m80 = a3;
    goto loc_0033DFD2;
loc_0033E049:
    if ((*(uint64_t *)(arg1 + 0x28)) < (*(uint64_t *)(arg1 + 0x28))) goto loc_0033E061;
    if (!sign_flag) goto loc_0033E212;
loc_0033E061:
    if (((local_rsi) & ((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) != 0) goto loc_0033DE53;
    result = MiGetPagingFileOffset(*(uint64_t *)(arg1 + 0x10), Arg1, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0033DE53;
    result = MI_IS_RESET_PTE(*(uint64_t *)(arg1 + 0x10), Arg1, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0033DE53;
    result = MiClearResetPfn(Arg1, Arg1, a3, a4);
    goto loc_0033DE53;
loc_0033E09C:
    if (condition_is_above_or_equal) goto loc_0033DF56;
    if (*(uint64_t *)(v_rip + 0xAEFBCE) == 0) goto loc_0033E0C2;
    result = *(uint64_t *)(v_rip + 0xAEFBCE);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xAEFBCE));
        Arg1 = (*(uint64_t *)(arg1 + 0x10)) & (result);
    }
    Arg1 = (Arg1) >> (16);
    result = MiDereferenceControlAreaPfnList(*(uint64_t *)(arg1), Arg1, 3 - 2, 3);
    goto loc_0033DF56;
loc_0033E0E0:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xC871C4)) & ((uint32_t)(local_rbx))) == 0) goto loc_0033E11B;
loc_0033E0EA:
loc_0033E0EC:
    if (!sign_flag) goto loc_0033DF5D;
    goto loc_0033E0E0;
loc_0033E0FB:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    result = (uint8_t)((result) & (248));
    v_stack_pB = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    goto loc_0033E018;
loc_0033E114:
    local_rsi = 0;
    goto loc_0033DEE1;
loc_0033E11B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC88997)))) & (64)) == 0) goto loc_0033E0EA;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(arg1), Arg1, 3 - 2, 3);
    if ((uint8_t)(result) == 0) goto loc_0033E0EA;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg1, 3 - 2, 3);
    goto loc_0033E0EC;
loc_0033E137:
    result = MI_IS_RESET_PTE(*(uint64_t *)(arg1 + 0x10), Arg1, 3 - 2, 3);
    if ((uint32_t)(result) != 0) {
        Arg1 = Arg1;
        result = MiClearResetPfn(Arg1, Arg1, 3 - 2, 3);
    }
    result = MiGetTopLevelPfn(Arg1, Arg1, 3 - 2, 3);
    result = MiGetPageTablePfnBuddyRaw(result, Arg1, result, 3);
    if (result != Arg1) {
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4B8))) >> (24));
    Arg1 = (uint8_t)((Arg1) & (48));
    if (((uint8_t)(Arg1)) != 32) goto loc_0033DE25;
    goto loc_0033DE25;
loc_0033E19D:
    result = MiSanitizeShadowPxe(Arg1, v_stack_p18, result, 3);
    goto loc_0033DEFC;
loc_0033E1B2:
    result = MiWritePteShadow(local_r14, v_stack_p18, result, 3);
    goto loc_0033DF08;
loc_0033E1C2:
    result = MiGetPagePrivilege(local_r14, 1, v_stack_mB8, 3);
    if ((uint32_t)(result) == 0) goto loc_0033E200;
    a3 = 0;
    local_rbx = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF222A) + result * 8));
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * ((uint32_t)((uint32_t)(result)));
    if ((((uint8_t)(result)) & (32)) != 0) goto loc_0033E232;
    result = VslRemoveProtectedPage(local_rbx, v_stack_mB8, a3, 3);
loc_0033E1FC:
    if (sign_flag) goto loc_0033E23B;
loc_0033E200:
    Arg2 = 0;
    result = MiSetPfnIdentity(Arg1, Arg2, a3, 3);
    goto loc_0033DDEA;
loc_0033E212:
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_0033E061;
    goto loc_0033DE53;
loc_0033E232:
    Arg2 = 0;
    result = VslMakeProtectedPageExecutable(Arg1, Arg2, a3, 3);
    goto loc_0033E1FC;
loc_0033E23B:
    a4 = 0;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x5150BULL), local_rbx, a4);
loc_0033E255:
    goto loc_0033DE50;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033DD90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
