# MiFillSystemPtes

- RVA: `0x00319850`–`0x0031A337` (길이 `2,791` bytes)
- VA: `0x0000000140319850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074C84`
- 디코드: `640`개 명령, `2,791/2,791` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00319BA4` → [MiLockPageInline](MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00319C05` → [MiUnlockPage](MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00319D0D` → [MiUserPdeOrAbove](../2C/MiUserPdeOrAbove_function_002C57F0.md) (function, `0x002C57F0`)
- `0x00319D7E` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00319E09` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00319E4D` → [MiIoSpaceGetBounds](../2A/MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x00319E62` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00319EB5` → [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) (function, `0x0023C804`)
- `0x00319F53` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00319F98` → [MiGetPfnPageSizeIndexUnsynchronized](../46/MiGetPfnPageSizeIndexUnsynchronized_function_0046C008.md) (function, `0x0046C008`)
- `0x0031A04E` → [MiGetPageTablePfnBuddyRaw](../2B/MiGetPageTablePfnBuddyRaw_function_002B4470.md) (function, `0x002B4470`)
- `0x0031A0E7` → [MiIoPagesInRun](../48/MiIoPagesInRun_function_00482E10.md) (function, `0x00482E10`)
- `0x0031A13D` → [MiVaToFlushVm](MiVaToFlushVm_function_0031AD84.md) (function, `0x0031AD84`)
- `0x0031A14B` → [MiClearMappingAndDereferenceIoSpace](../24/MiClearMappingAndDereferenceIoSpace_function_00247DF0.md) (function, `0x00247DF0`)
- `0x0031A174` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x0031A194` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x0031A1A2` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x0031A1AA` → [MiFlushTbList](MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0031A1AF` → [MiReleaseProcessorFlushList](MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0031A1CF` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0031A298` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0031A2C4` → [MiShowBadMapper](../2F/MiShowBadMapper_function_002F1840.md) (function, `0x002F1840`)
- `0x0031A306` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0031A313` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [MmMapLockedPagesSpecifyCache](MmMapLockedPagesSpecifyCache_function_00318800.md) at `0x00318929`
- [MiMapContiguousMemory](../32/MiMapContiguousMemory_function_0032787C.md) at `0x00327A06`
- [MmMapMdl](../67/MmMapMdl_function_0067CBA0.md) at `0x0067CD1D`
- [MiAllocateZeroCalibrationBuffer](../69/MiAllocateZeroCalibrationBuffer_function_00699844.md) at `0x00699984`
- [MiLockAndMapEntireDriver](../../page/80/MiLockAndMapEntireDriver_function_008015C8.md) at `0x00801746`
- [MiMapHotPatchImageInSystemSpace](../../page/80/MiMapHotPatchImageInSystemSpace_function_00806438.md) at `0x00806596`

### Static image references
- `0x003198DD` → RVA `0x00010990` (`.rdata`; read)
- `0x003199A5` → RVA `0x00E2F380` (`.data`; read)
- `0x003199B2` → RVA `0x00E2EE84` (`.data`; read)
- `0x003199BF` → RVA `0x00E2EE85` (`.data`; read)
- `0x00319ABF` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00319B94` → RVA `0x00E3014C` (`.data`; read)
- `0x00319C4A` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00319CB8` → RVA `0x00E2F390` (`.data`; read)
- `0x00319D9B` → RVA `0x00E2DC38` (`.data`; read)
- `0x00319E38` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0031A098` → RVA `0x00E30188` (`.data`; read)
- `0x0031A1EA` → RVA `0x00E37438` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00319850  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00319855  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0031985A  53                              push rbx
0031985B  55                              push rbp
0031985C  56                              push rsi
0031985D  57                              push rdi
0031985E  41 54                           push r12
00319860  41 55                           push r13
00319862  41 56                           push r14
00319864  41 57                           push r15
00319866  48 83 EC 78                     sub rsp, 0x78
0031986A  45 33 DB                        xor r11d, r11d
0031986D  33 C0                           xor eax, eax
0031986F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00319874  0F 57 C0                        xorps xmm0, xmm0
00319877  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
0031987F  4C 8B F9                        mov r15, rcx
00319882  44 89 9C 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r11d
0031988A  41 8B F1                        mov esi, r9d
0031988D  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
00319892  41 8D 6B 01                     lea ebp, [r11 + 1]
00319896  8D 4D 01                        lea ecx, [rbp + 1]
00319899  4D 8B D0                        mov r10, r8
0031989C  44 89 18                        mov dword ptr [rax], r11d
0031989F  4C 8B E2                        mov r12, rdx
003198A2  41 8B FB                        mov edi, r11d
003198A5  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
003198AA  45 85 C9                        test r9d, r9d
003198AD  0F 84 D5 04 00 00               je 0x140319d88
003198B3  41 83 F9 1F                     cmp r9d, 0x1f
003198B7  74 15                           je 0x1403198ce
003198B9  41 8B C1                        mov eax, r9d
003198BC  C1 E8 03                        shr eax, 3
003198BF  83 F8 03                        cmp eax, 3
003198C2  0F 84 A2 06 00 00               je 0x140319f6a
003198C8  3B C5                           cmp eax, ebp
003198CA  41 0F 44 EB                     cmove ebp, r11d
003198CE  8B C6                           mov eax, esi
003198D0  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
003198DA  83 E0 1F                        and eax, 0x1f
003198DD  48 8D 1D AC 70 CF FF            lea rbx, [rip - 0x308f54]
003198E4  44 8B F0                        mov r14d, eax
003198E7  48 8B 1C C3                     mov rbx, qword ptr [rbx + rax*8]
003198EB  48 B8 7F 0E 00 00 00 00 F0 FF   movabs rax, 0xfff0000000000e7f
003198F5  48 23 D8                        and rbx, rax
003198F8  48 83 CB 21                     or rbx, 0x21
003198FC  49 8B C5                        mov rax, r13
003198FF  4C 3B F8                        cmp r15, rax
00319902  0F 82 9F 03 00 00               jb 0x140319ca7
00319908  49 BB FF FF FF FF FF F6 FF FF   movabs r11, 0xfffff6ffffffffff
00319912  49 8B C3                        mov rax, r11
00319915  4C 3B F8                        cmp r15, rax
00319918  0F 87 86 03 00 00               ja 0x140319ca4
0031991E  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00319928  4C 3B F8                        cmp r15, rax
0031992B  0F 83 A0 03 00 00               jae 0x140319cd1
00319931  49 8B D5                        mov rdx, r13
00319934  48 C1 E2 19                     shl rdx, 0x19
00319938  49 8B C7                        mov rax, r15
0031993B  48 C1 E0 19                     shl rax, 0x19
0031993F  44 8B CE                        mov r9d, esi
00319942  48 2B C2                        sub rax, rdx
00319945  48 C1 F8 10                     sar rax, 0x10
00319949  41 81 E1 00 00 00 04            and r9d, 0x4000000
00319950  74 29                           je 0x14031997b
00319952  49 8B CD                        mov rcx, r13
00319955  48 3B C1                        cmp rax, rcx
00319958  72 21                           jb 0x14031997b
0031995A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00319960  49 8B CB                        mov rcx, r11
00319963  48 3B C1                        cmp rax, rcx
00319966  77 13                           ja 0x14031997b
00319968  48 C1 E0 19                     shl rax, 0x19
0031996C  48 2B C2                        sub rax, rdx
0031996F  48 C1 F8 10                     sar rax, 0x10
00319973  49 8B CD                        mov rcx, r13
00319976  48 3B C1                        cmp rax, rcx
00319979  73 E5                           jae 0x140319960
0031997B  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
00319985  48 3B C1                        cmp rax, rcx
00319988  76 31                           jbe 0x1403199bb
0031998A  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
00319994  48 3B C1                        cmp rax, rcx
00319997  72 26                           jb 0x1403199bf
00319999  49 8B CD                        mov rcx, r13
0031999C  48 3B C1                        cmp rax, rcx
0031999F  0F 83 90 03 00 00               jae 0x140319d35
003199A5  48 3B 05 D4 59 B1 00            cmp rax, qword ptr [rip + 0xb159d4]
003199AC  0F 83 06 03 00 00               jae 0x140319cb8
003199B2  0F B6 05 CB 54 B1 00            movzx eax, byte ptr [rip + 0xb154cb]
003199B9  EB 0B                           jmp 0x1403199c6
003199BB  48 83 CB 04                     or rbx, 4
003199BF  0F B6 05 BF 54 B1 00            movzx eax, byte ptr [rip + 0xb154bf]
003199C6  85 C0                           test eax, eax
003199C8  74 05                           je 0x1403199cf
003199CA  48 0F BA EB 08                  bts rbx, 8
003199CF  45 33 DB                        xor r11d, r11d
003199D2  0F B6 0D AB 54 B1 00            movzx ecx, byte ptr [rip + 0xb154ab]
003199D9  41 80 E6 05                     and r14b, 5
003199DD  48 8B D3                        mov rdx, rbx
003199E0  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
003199E5  48 83 CA 42                     or rdx, 0x42
003199E9  4D 8B EC                        mov r13, r12
003199EC  41 80 FE 04                     cmp r14b, 4
003199F0  4D 8B E3                        mov r12, r11
003199F3  49 BE FF 0F 00 00 00 00 F0 FF   movabs r14, 0xfff0000000000fff
003199FD  48 0F 45 D3                     cmovne rdx, rbx
00319A01  48 C1 E1 08                     shl rcx, 8
00319A05  4C 8B C2                        mov r8, rdx
00319A08  49 83 E0 FB                     and r8, 0xfffffffffffffffb
00319A0C  0F BA E6 1E                     bt esi, 0x1e
00319A10  4C 0F 43 C2                     cmovae r8, rdx
00319A14  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00319A1B  4C 33 C1                        xor r8, rcx
00319A1E  49 0F BA F0 08                  btr r8, 8
00319A23  4C 33 C1                        xor r8, rcx
00319A26  49 8B C8                        mov rcx, r8
00319A29  48 0F BA F1 08                  btr rcx, 8
00319A2E  0F BA E6 1B                     bt esi, 0x1b
00319A32  49 0F 43 C8                     cmovae rcx, r8
00319A36  4D 8B C3                        mov r8, r11
00319A39  48 8B C1                        mov rax, rcx
00319A3C  48 0F BA E8 07                  bts rax, 7
00319A41  45 85 C9                        test r9d, r9d
00319A44  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
00319A4E  48 0F 44 C1                     cmove rax, rcx
00319A52  48 B9 FF FF FF FF FF FF FF FA   movabs rcx, 0xfaffffffffffffff
00319A5C  48 23 C1                        and rax, rcx
00319A5F  48 B9 00 00 00 00 00 00 00 0A   movabs rcx, 0xa00000000000000
00319A69  48 0B C1                        or rax, rcx
00319A6C  49 8D 4A F8                     lea rcx, [r10 - 8]
00319A70  4D 85 D2                        test r10, r10
00319A73  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00319A78  49 8D 42 FF                     lea rax, [r10 - 1]
00319A7C  49 BA 00 00 00 00 00 01 00 00   movabs r10, 0x10000000000
00319A86  4C 0F 49 E0                     cmovns r12, rax
00319A8A  49 0F 49 CB                     cmovns rcx, r11
00319A8E  4D 85 ED                        test r13, r13
00319A91  0F 84 F9 01 00 00               je 0x140319c90
00319A97  48 8D 41 08                     lea rax, [rcx + 8]
00319A9B  48 85 C9                        test rcx, rcx
00319A9E  0F 84 EC 05 00 00               je 0x14031a090
00319AA4  4C 8B 20                        mov r12, qword ptr [rax]
00319AA7  48 85 C9                        test rcx, rcx
00319AAA  48 0F 44 C1                     cmove rax, rcx
00319AAE  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00319AB3  48 8B C8                        mov rcx, rax
00319AB6  F6 C2 02                        test dl, 2
00319AB9  0F 85 2B 07 00 00               jne 0x14031a1ea
00319ABF  4C 3B 25 1A 42 B1 00            cmp r12, qword ptr [rip + 0xb1421a]
00319AC6  0F 87 C6 02 00 00               ja 0x140319d92
00319ACC  4B 8D 1C 64                     lea rbx, [r12 + r12*2]
00319AD0  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00319ADA  48 03 DB                        add rbx, rbx
00319ADD  48 8B C0                        mov rax, rax
00319AE0  48 8B 04 D8                     mov rax, qword ptr [rax + rbx*8]
00319AE4  48 C1 E8 36                     shr rax, 0x36
00319AE8  0F BA E0 00                     bt eax, 0
00319AEC  0F 83 A0 02 00 00               jae 0x140319d92
00319AF2  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00319AFC  48 8B C0                        mov rax, rax
00319AFF  44 8B C2                        mov r8d, edx
00319B02  4C 8D 34 D8                     lea r14, [rax + rbx*8]
00319B06  41 83 E0 01                     and r8d, 1
00319B0A  48 B8 22 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000022
00319B14  48 8B C0                        mov rax, rax
00319B17  48 8D 14 D8                     lea rdx, [rax + rbx*8]
00319B1B  0F 85 4E 07 00 00               jne 0x14031a26f
00319B21  49 8B C1                        mov rax, r9
00319B24  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
00319B27  66 85 C9                        test cx, cx
00319B2A  0F 84 6E 07 00 00               je 0x14031a29e
00319B30  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00319B34  48 85 C0                        test rax, rax
00319B37  78 46                           js 0x140319b7f
00319B39  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00319B3D  49 85 C2                        test r10, rax
00319B40  0F 85 35 04 00 00               jne 0x140319f7b
00319B46  48 B8 08 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000008
00319B50  48 8B C0                        mov rax, rax
00319B53  48 8B 0C D8                     mov rcx, qword ptr [rax + rbx*8]
00319B57  48 C1 E1 19                     shl rcx, 0x19
00319B5B  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00319B65  49 8B C0                        mov rax, r8
00319B68  48 C1 E0 19                     shl rax, 0x19
00319B6C  48 2B C8                        sub rcx, rax
00319B6F  48 C1 F9 10                     sar rcx, 0x10
00319B73  49 8B C0                        mov rax, r8
00319B76  48 3B C8                        cmp rcx, rax
00319B79  0F 83 4C 04 00 00               jae 0x140319fcb
00319B7F  49 8B C1                        mov rax, r9
00319B82  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
00319B85  C1 E9 10                        shr ecx, 0x10
00319B88  80 E1 C0                        and cl, 0xc0
00319B8B  80 F9 C0                        cmp cl, 0xc0
00319B8E  0F 85 80 00 00 00               jne 0x140319c14
00319B94  83 3D B1 65 B1 00 02            cmp dword ptr [rip + 0xb165b1], 2
00319B9B  0F 84 F7 04 00 00               je 0x14031a098
00319BA1  49 8B CE                        mov rcx, r14
00319BA4  E8 97 07 00 00                  call 0x14031a340
00319BA9  44 0F B6 C0                     movzx r8d, al
00319BAD  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
00319BB7  49 8B C9                        mov rcx, r9
00319BBA  8B 14 D9                        mov edx, dword ptr [rcx + rbx*8]
00319BBD  C1 EA 10                        shr edx, 0x10
00319BC0  80 E2 C0                        and dl, 0xc0
00319BC3  80 FA C0                        cmp dl, 0xc0
00319BC6  75 30                           jne 0x140319bf8
00319BC8  49 8B C9                        mov rcx, r9
00319BCB  8B 14 D9                        mov edx, dword ptr [rcx + rbx*8]
00319BCE  40 0F B6 C5                     movzx eax, bpl
00319BD2  89 94 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], edx
00319BD9  C1 EA 10                        shr edx, 0x10
00319BDC  80 E2 3F                        and dl, 0x3f
00319BDF  C0 E0 06                        shl al, 6
00319BE2  0A D0                           or dl, al
00319BE4  88 94 24 D2 00 00 00            mov byte ptr [rsp + 0xd2], dl
00319BEB  49 8B D1                        mov rdx, r9
00319BEE  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
00319BF5  89 04 DA                        mov dword ptr [rdx + rbx*8], eax
00319BF8  41 80 F8 11                     cmp r8b, 0x11
00319BFC  74 16                           je 0x140319c14
00319BFE  41 0F B6 D0                     movzx edx, r8b
00319C02  49 8B CE                        mov rcx, r14
00319C05  E8 D6 07 00 00                  call 0x14031a3e0
00319C0A  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
00319C14  49 8B C1                        mov rax, r9
00319C17  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
00319C1A  C1 E9 10                        shr ecx, 0x10
00319C1D  0F B6 C1                        movzx eax, cl
00319C20  C1 E8 06                        shr eax, 6
00319C23  3B E8                           cmp ebp, eax
00319C25  0F 85 EF 02 00 00               jne 0x140319f1a
00319C2B  49 8B C4                        mov rax, r12
00319C2E  49 BE FF 0F 00 00 00 00 F0 FF   movabs r14, 0xfff0000000000fff
00319C38  48 C1 E0 0C                     shl rax, 0xc
00319C3C  48 8B D8                        mov rbx, rax
00319C3F  48 33 5C 24 50                  xor rbx, qword ptr [rsp + 0x50]
00319C44  49 23 DE                        and rbx, r14
00319C47  48 33 D8                        xor rbx, rax
00319C4A  48 0F BA 25 35 CE CA 00 24      bt qword ptr [rip + 0xcace35], 0x24
00319C53  0F 82 ED 00 00 00               jb 0x140319d46
00319C59  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00319C5E  45 33 DB                        xor r11d, r11d
00319C61  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00319C68  49 BA 00 00 00 00 00 01 00 00   movabs r10, 0x10000000000
00319C72  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00319C77  49 89 1F                        mov qword ptr [r15], rbx
00319C7A  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
00319C84  49 FF CD                        dec r13
00319C87  49 83 C7 08                     add r15, 8
00319C8B  E9 FE FD FF FF                  jmp 0x140319a8e
00319C90  33 C0                           xor eax, eax
00319C92  48 83 C4 78                     add rsp, 0x78
00319C96  41 5F                           pop r15
00319C98  41 5E                           pop r14
00319C9A  41 5D                           pop r13
00319C9C  41 5C                           pop r12
00319C9E  5F                              pop rdi
00319C9F  5E                              pop rsi
00319CA0  5D                              pop rbp
00319CA1  5B                              pop rbx
00319CA2  C3                              ret
00319CA3  CC                              int3
00319CA4  45 33 DB                        xor r11d, r11d
00319CA7  48 0F BA EB 08                  bts rbx, 8
00319CAC  41 81 E1 00 00 00 04            and r9d, 0x4000000
00319CB3  E9 1A FD FF FF                  jmp 0x1403199d2
00319CB8  48 3B 05 D1 56 B1 00            cmp rax, qword ptr [rip + 0xb156d1]
00319CBF  0F 87 ED FC FF FF               ja 0x1403199b2
00319CC5  0F B6 05 B9 51 B1 00            movzx eax, byte ptr [rip + 0xb151b9]
00319CCC  E9 F5 FC FF FF                  jmp 0x1403199c6
00319CD1  48 B8 FF FF FF 7F FB F6 FF FF   movabs rax, 0xfffff6fb7fffffff
00319CDB  4C 3B F8                        cmp r15, rax
00319CDE  0F 87 4D FC FF FF               ja 0x140319931
00319CE4  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00319CEE  4C 3B F8                        cmp r15, rax
00319CF1  0F 84 26 06 00 00               je 0x14031a31d
00319CF7  0F BA E6 1A                     bt esi, 0x1a
00319CFB  72 0D                           jb 0x140319d0a
00319CFD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00319D07  48 23 D8                        and rbx, rax
00319D0A  49 8B CF                        mov rcx, r15
00319D0D  E8 DE BA FA FF                  call 0x1402c57f0
00319D12  4C 8B 94 24 D0 00 00 00         mov r10, qword ptr [rsp + 0xd0]
00319D1A  49 BB FF FF FF FF FF F6 FF FF   movabs r11, 0xfffff6ffffffffff
00319D24  85 C0                           test eax, eax
00319D26  0F 84 05 FC FF FF               je 0x140319931
00319D2C  48 83 CB 04                     or rbx, 4
00319D30  E9 FC FB FF FF                  jmp 0x140319931
00319D35  49 8B CB                        mov rcx, r11
00319D38  48 3B C1                        cmp rax, rcx
00319D3B  0F 87 64 FC FF FF               ja 0x1403199a5
00319D41  E9 89 FC FF FF                  jmp 0x1403199cf
00319D46  F6 C3 20                        test bl, 0x20
00319D49  0F 85 0A FF FF FF               jne 0x140319c59
00319D4F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00319D59  48 8B C0                        mov rax, rax
00319D5C  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00319D66  48 03 C1                        add rax, rcx
00319D69  4C 3B F8                        cmp r15, rax
00319D6C  0F 82 E7 FE FF FF               jb 0x140319c59
00319D72  41 B8 80 00 00 00               mov r8d, 0x80
00319D78  48 8B D3                        mov rdx, rbx
00319D7B  49 8B CF                        mov rcx, r15
00319D7E  E8 FD 8F F7 FF                  call 0x140292d80
00319D83  E9 D1 FE FF FF                  jmp 0x140319c59
00319D88  BD 03 00 00 00                  mov ebp, 3
00319D8D  E9 3C FB FF FF                  jmp 0x1403198ce
00319D92  4D 85 C0                        test r8, r8
00319D95  0F 84 85 00 00 00               je 0x140319e20
00319D9B  0F B6 0D 96 3E B1 00            movzx ecx, byte ptr [rip + 0xb13e96]
00319DA2  B8 01 00 00 00                  mov eax, 1
00319DA7  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00319DAC  80 C1 F4                        add cl, 0xf4
00319DAF  48 D3 E0                        shl rax, cl
00319DB2  FF C8                           dec eax
00319DB4  41 23 C4                        and eax, r12d
00319DB7  2B 42 18                        sub eax, dword ptr [rdx + 0x18]
00319DBA  03 C0                           add eax, eax
00319DBC  8B C8                           mov ecx, eax
00319DBE  48 C1 E8 05                     shr rax, 5
00319DC2  83 E1 1F                        and ecx, 0x1f
00319DC5  8B 54 82 2C                     mov edx, dword ptr [rdx + rax*4 + 0x2c]
00319DC9  D3 EA                           shr edx, cl
00319DCB  83 E2 03                        and edx, 3
00319DCE  49 FF C8                        dec r8
00319DD1  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00319DD6  83 E6 07                        and esi, 7
00319DD9  85 D2                           test edx, edx
00319DDB  0F 84 F8 02 00 00               je 0x14031a0d9
00319DE1  83 FA 02                        cmp edx, 2
00319DE4  0F 84 D9 01 00 00               je 0x140319fc3
00319DEA  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00319DF1  85 C0                           test eax, eax
00319DF3  0F 85 FB 02 00 00               jne 0x14031a0f4
00319DF9  44 8B C6                        mov r8d, esi
00319DFC  49 8B D4                        mov rdx, r12
00319DFF  41 81 C8 00 00 00 A0            or r8d, 0xa0000000
00319E06  49 8B CF                        mov rcx, r15
00319E09  E8 82 B7 FA FF                  call 0x1402c5590
00319E0E  48 8B D8                        mov rbx, rax
00319E11  89 B4 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], esi
00319E18  48 8B F8                        mov rdi, rax
00319E1B  E9 2A FE FF FF                  jmp 0x140319c4a
00319E20  83 7C 24 6C 00                  cmp dword ptr [rsp + 0x6c], 0
00319E25  0F 85 BA 04 00 00               jne 0x14031a2e5
00319E2B  44 0F 20 C3                     mov rbx, cr8
00319E2F  B8 02 00 00 00                  mov eax, 2
00319E34  44 0F 22 C0                     mov cr8, rax
00319E38  83 3D E1 CE CA 00 00            cmp dword ptr [rip + 0xcacee1], 0
00319E3F  0F 85 BB 04 00 00               jne 0x14031a300
00319E45  49 8B D4                        mov rdx, r12
00319E48  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00319E4D  E8 D6 28 F9 FF                  call 0x1402ac728
00319E52  83 3D C7 CE CA 00 00            cmp dword ptr [rip + 0xcacec7], 0
00319E59  74 0C                           je 0x140319e67
00319E5B  44 0F 20 C1                     mov rcx, cr8
00319E5F  0F B6 D3                        movzx edx, bl
00319E62  E8 31 B8 1D 00                  call 0x1404f5698
00319E67  0F B6 C3                        movzx eax, bl
00319E6A  44 0F 22 C0                     mov cr8, rax
00319E6E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00319E73  45 33 DB                        xor r11d, r11d
00319E76  83 7C 24 6C 03                  cmp dword ptr [rsp + 0x6c], 3
00319E7B  0F 85 60 03 00 00               jne 0x14031a1e1
00319E81  48 85 C9                        test rcx, rcx
00319E84  0F 84 57 02 00 00               je 0x14031a0e1
00319E8A  BB 01 00 00 00                  mov ebx, 1
00319E8F  4C 3B EB                        cmp r13, rbx
00319E92  0F 87 64 03 00 00               ja 0x14031a1fc
00319E98  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00319E9D  44 8B CD                        mov r9d, ebp
00319EA0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00319EA5  4C 8B C3                        mov r8, rbx
00319EA8  49 8B D4                        mov rdx, r12
00319EAB  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00319EB0  B9 01 00 00 00                  mov ecx, 1
00319EB5  E8 4A 29 F2 FF                  call 0x14023c804
00319EBA  44 8B F0                        mov r14d, eax
00319EBD  85 C0                           test eax, eax
00319EBF  0F 88 A5 01 00 00               js 0x14031a06a
00319EC5  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00319ECD  49 BE FF 0F 00 00 00 00 F0 FF   movabs r14, 0xfff0000000000fff
00319ED7  0F B6 0D 5A 3D B1 00            movzx ecx, byte ptr [rip + 0xb13d5a]
00319EDE  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00319EE3  80 C1 F4                        add cl, 0xf4
00319EE6  83 08 01                        or dword ptr [rax], 1
00319EE9  B8 01 00 00 00                  mov eax, 1
00319EEE  48 D3 E0                        shl rax, cl
00319EF1  FF C8                           dec eax
00319EF3  41 23 C4                        and eax, r12d
00319EF6  2B 42 18                        sub eax, dword ptr [rdx + 0x18]
00319EF9  03 C0                           add eax, eax
00319EFB  8B C8                           mov ecx, eax
00319EFD  48 C1 E8 05                     shr rax, 5
00319F01  83 E1 1F                        and ecx, 0x1f
00319F04  8B 54 82 2C                     mov edx, dword ptr [rdx + rax*4 + 0x2c]
00319F08  D3 EA                           shr edx, cl
00319F0A  83 E2 03                        and edx, 3
00319F0D  48 FF CB                        dec rbx
00319F10  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00319F15  E9 BC FE FF FF                  jmp 0x140319dd6
00319F1A  83 E6 07                        and esi, 7
00319F1D  49 8B C1                        mov rax, r9
00319F20  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
00319F23  C1 E9 10                        shr ecx, 0x10
00319F26  80 F9 40                        cmp cl, 0x40
00319F29  0F 82 00 04 00 00               jb 0x14031a32f
00319F2F  49 8B C1                        mov rax, r9
00319F32  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
00319F35  C1 E9 10                        shr ecx, 0x10
00319F38  80 E1 C0                        and cl, 0xc0
00319F3B  80 F9 80                        cmp cl, 0x80
00319F3E  75 03                           jne 0x140319f43
00319F40  83 CE 18                        or esi, 0x18
00319F43  44 8B C6                        mov r8d, esi
00319F46  49 8B D4                        mov rdx, r12
00319F49  41 81 C8 00 00 00 A0            or r8d, 0xa0000000
00319F50  49 8B CF                        mov rcx, r15
00319F53  E8 38 B6 FA FF                  call 0x1402c5590
00319F58  48 8B D8                        mov rbx, rax
00319F5B  49 BE FF 0F 00 00 00 00 F0 FF   movabs r14, 0xfff0000000000fff
00319F65  E9 E0 FC FF FF                  jmp 0x140319c4a
00319F6A  40 F6 C6 07                     test sil, 7
00319F6E  0F 84 5A F9 FF FF               je 0x1403198ce
00319F74  8B E9                           mov ebp, ecx
00319F76  E9 53 F9 FF FF                  jmp 0x1403198ce
00319F7B  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00319F80  44 89 9C 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r11d
00319F88  48 8D 94 24 D8 00 00 00         lea rdx, [rsp + 0xd8]
00319F90  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00319F95  49 8B CE                        mov rcx, r14
00319F98  E8 6B 20 15 00                  call 0x14046c008
00319F9D  83 F8 03                        cmp eax, 3
00319FA0  0F 84 BE 00 00 00               je 0x14031a064
00319FA6  83 BC 24 D8 00 00 00 06         cmp dword ptr [rsp + 0xd8], 6
00319FAE  0F 85 B0 00 00 00               jne 0x14031a064
00319FB4  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
00319FBE  E9 BC FB FF FF                  jmp 0x140319b7f
00319FC3  83 CE 18                        or esi, 0x18
00319FC6  E9 1F FE FF FF                  jmp 0x140319dea
00319FCB  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00319FD5  48 8B C0                        mov rax, rax
00319FD8  48 3B C8                        cmp rcx, rax
00319FDB  0F 87 9E FB FF FF               ja 0x140319b7f
00319FE1  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00319FE5  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00319FEF  48 23 C1                        and rax, rcx
00319FF2  48 B9 FE FF FF FF 3F 00 00 00   movabs rcx, 0x3ffffffffe
00319FFC  48 3B C1                        cmp rax, rcx
00319FFF  0F 84 7A FB FF FF               je 0x140319b7f
0031A005  49 8B C1                        mov rax, r9
0031A008  8B 14 D8                        mov edx, dword ptr [rax + rbx*8]
0031A00B  C1 EA 10                        shr edx, 0x10
0031A00E  F6 C2 20                        test dl, 0x20
0031A011  74 2F                           je 0x14031a042
0031A013  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
0031A01D  48 8B C0                        mov rax, rax
0031A020  48 8B 04 D8                     mov rax, qword ptr [rax + rbx*8]
0031A024  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
0031A02E  48 85 C1                        test rcx, rax
0031A031  75 0F                           jne 0x14031a042
0031A033  49 8B C1                        mov rax, r9
0031A036  8B 0C D8                        mov ecx, dword ptr [rax + rbx*8]
0031A039  66 85 C9                        test cx, cx
0031A03C  0F 85 3D FB FF FF               jne 0x140319b7f
0031A042  F6 C2 08                        test dl, 8
0031A045  0F 85 34 FB FF FF               jne 0x140319b7f
0031A04B  49 8B CE                        mov rcx, r14
0031A04E  E8 1D A4 F9 FF                  call 0x1402b4470
0031A053  49 3B C2                        cmp rax, r10
0031A056  0F 84 23 FB FF FF               je 0x140319b7f
0031A05C  41 BE 18 00 00 C0               mov r14d, 0xc0000018
0031A062  EB 10                           jmp 0x14031a074
0031A064  41 BE 18 00 00 C0               mov r14d, 0xc0000018
0031A06A  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
0031A074  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0031A07C  48 8B F8                        mov rdi, rax
0031A07F  49 2B FD                        sub rdi, r13
0031A082  0F 85 96 00 00 00               jne 0x14031a11e
0031A088  41 8B C6                        mov eax, r14d
0031A08B  E9 02 FC FF FF                  jmp 0x140319c92
0031A090  49 FF C4                        inc r12
0031A093  E9 0F FA FF FF                  jmp 0x140319aa7
0031A098  48 8B 0D E9 60 B1 00            mov rcx, qword ptr [rip + 0xb160e9]
0031A09F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0031A0A8  48 3B C8                        cmp rcx, rax
0031A0AB  74 24                           je 0x14031a0d1
0031A0AD  48 85 C9                        test rcx, rcx
0031A0B0  0F 84 EB FA FF FF               je 0x140319ba1
0031A0B6  48 0F BA 25 C9 C9 CA 00 28      bt qword ptr [rip + 0xcac9c9], 0x28
0031A0BF  0F 83 DC FA FF FF               jae 0x140319ba1
0031A0C5  44 0F 20 C0                     mov rax, cr8
0031A0C9  3C 0F                           cmp al, 0xf
0031A0CB  0F 85 D0 FA FF FF               jne 0x140319ba1
0031A0D1  41 B0 11                        mov r8b, 0x11
0031A0D4  E9 DE FA FF FF                  jmp 0x140319bb7
0031A0D9  83 CE 10                        or esi, 0x10
0031A0DC  E9 09 FD FF FF                  jmp 0x140319dea
0031A0E1  49 8B D5                        mov rdx, r13
0031A0E4  49 8B CC                        mov rcx, r12
0031A0E7  E8 24 8D 16 00                  call 0x140482e10
0031A0EC  48 8B D8                        mov rbx, rax
0031A0EF  E9 A4 FD FF FF                  jmp 0x140319e98
0031A0F4  3B C6                           cmp eax, esi
0031A0F6  0F 85 FD FC FF FF               jne 0x140319df9
0031A0FC  49 8B C4                        mov rax, r12
0031A0FF  89 B4 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], esi
0031A106  48 C1 E0 0C                     shl rax, 0xc
0031A10A  48 8B D8                        mov rbx, rax
0031A10D  48 33 DF                        xor rbx, rdi
0031A110  49 23 DE                        and rbx, r14
0031A113  48 33 D8                        xor rbx, rax
0031A116  48 8B FB                        mov rdi, rbx
0031A119  E9 2C FB FF FF                  jmp 0x140319c4a
0031A11E  4C 2B E8                        sub r13, rax
0031A121  49 C1 E5 1C                     shl r13, 0x1c
0031A125  49 8B C0                        mov rax, r8
0031A128  48 C1 E0 19                     shl rax, 0x19
0031A12C  4C 2B E8                        sub r13, rax
0031A12F  49 C1 E7 19                     shl r15, 0x19
0031A133  4D 03 EF                        add r13, r15
0031A136  49 C1 FD 10                     sar r13, 0x10
0031A13A  49 8B CD                        mov rcx, r13
0031A13D  E8 42 0C 00 00                  call 0x14031ad84
0031A142  48 8B D7                        mov rdx, rdi
0031A145  49 8B CD                        mov rcx, r13
0031A148  48 8B E8                        mov rbp, rax
0031A14B  E8 A0 DC F2 FF                  call 0x140247df0
0031A150  44 0F 20 C6                     mov rsi, cr8
0031A154  40 80 FE 02                     cmp sil, 2
0031A158  73 1A                           jae 0x14031a174
0031A15A  44 0F 20 C1                     mov rcx, cr8
0031A15E  B8 02 00 00 00                  mov eax, 2
0031A163  44 0F 22 C0                     mov cr8, rax
0031A167  83 3D B2 CB CA 00 00            cmp dword ptr [rip + 0xcacbb2], 0
0031A16E  0F 85 9C 01 00 00               jne 0x14031a310
0031A174  E8 17 8B F2 FF                  call 0x140242c90
0031A179  41 B9 08 00 00 00               mov r9d, 8
0031A17F  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0031A187  48 8B D5                        mov rdx, rbp
0031A18A  48 8B C8                        mov rcx, rax
0031A18D  48 8B D8                        mov rbx, rax
0031A190  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
0031A194  E8 67 AD F7 FF                  call 0x140294f00
0031A199  4C 8B C7                        mov r8, rdi
0031A19C  49 8B D5                        mov rdx, r13
0031A19F  45 33 C9                        xor r9d, r9d
0031A1A2  E8 C9 94 F7 FF                  call 0x140293670
0031A1A7  48 8B CB                        mov rcx, rbx
0031A1AA  E8 11 7E FF FF                  call 0x140311fc0
0031A1AF  E8 BC 9A FF FF                  call 0x140313c70
0031A1B4  40 80 FE 02                     cmp sil, 2
0031A1B8  0F 83 CA FE FF FF               jae 0x14031a088
0031A1BE  83 3D 5B CB CA 00 00            cmp dword ptr [rip + 0xcacb5b], 0
0031A1C5  74 0D                           je 0x14031a1d4
0031A1C7  44 0F 20 C1                     mov rcx, cr8
0031A1CB  40 0F B6 D6                     movzx edx, sil
0031A1CF  E8 C4 B4 1D 00                  call 0x1404f5698
0031A1D4  40 0F B6 C6                     movzx eax, sil
0031A1D8  44 0F 22 C0                     mov cr8, rax
0031A1DC  E9 A7 FE FF FF                  jmp 0x14031a088
0031A1E1  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
0031A1E5  E9 EC FB FF FF                  jmp 0x140319dd6
0031A1EA  4C 3B 25 47 D2 B1 00            cmp r12, qword ptr [rip + 0xb1d247]
0031A1F1  0F 85 C8 F8 FF FF               jne 0x140319abf
0031A1F7  E9 88 FA FF FF                  jmp 0x140319c84
0031A1FC  4D 8D 45 FF                     lea r8, [r13 - 1]
0031A200  48 8D 51 08                     lea rdx, [rcx + 8]
0031A204  4D 85 C0                        test r8, r8
0031A207  0F 84 8B FC FF FF               je 0x140319e98
0031A20D  48 8B 42 F8                     mov rax, qword ptr [rdx - 8]
0031A211  48 8B 0A                        mov rcx, qword ptr [rdx]
0031A214  48 FF C0                        inc rax
0031A217  48 3B C8                        cmp rcx, rax
0031A21A  0F 85 78 FC FF FF               jne 0x140319e98
0031A220  48 F7 C1 FF 01 00 00            test rcx, 0x1ff
0031A227  0F 84 6B FC FF FF               je 0x140319e98
0031A22D  48 3B 0D AC 3A B1 00            cmp rcx, qword ptr [rip + 0xb13aac]
0031A234  77 26                           ja 0x14031a25c
0031A236  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
0031A23A  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0031A244  48 03 C9                        add rcx, rcx
0031A247  48 8B C0                        mov rax, rax
0031A24A  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0031A24E  48 C1 E8 36                     shr rax, 0x36
0031A252  0F BA E0 00                     bt eax, 0
0031A256  0F 82 3C FC FF FF               jb 0x140319e98
0031A25C  48 FF C3                        inc rbx
0031A25F  48 83 C2 08                     add rdx, 8
0031A263  49 83 E8 01                     sub r8, 1
0031A267  0F 84 2B FC FF FF               je 0x140319e98
0031A26D  EB 9E                           jmp 0x14031a20d
0031A26F  0F B6 02                        movzx eax, byte ptr [rdx]
0031A272  24 07                           and al, 7
0031A274  3C 05                           cmp al, 5
0031A276  75 0C                           jne 0x14031a284
0031A278  49 0F BA 66 28 35               bt qword ptr [r14 + 0x28], 0x35
0031A27E  0F 82 9D F8 FF FF               jb 0x140319b21
0031A284  45 33 C9                        xor r9d, r9d
0031A287  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0031A28C  4D 8B C4                        mov r8, r12
0031A28F  BA 46 12 00 00                  mov edx, 0x1246
0031A294  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0031A298  E8 C3 33 1E 00                  call 0x1404fd660
0031A29D  CC                              int3
0031A29E  45 85 C0                        test r8d, r8d
0031A2A1  74 15                           je 0x14031a2b8
0031A2A3  0F B6 02                        movzx eax, byte ptr [rdx]
0031A2A6  24 07                           and al, 7
0031A2A8  3C 05                           cmp al, 5
0031A2AA  75 0C                           jne 0x14031a2b8
0031A2AC  49 0F BA 66 28 35               bt qword ptr [r14 + 0x28], 0x35
0031A2B2  0F 82 78 F8 FF FF               jb 0x140319b30
0031A2B8  BA 01 00 00 00                  mov edx, 1
0031A2BD  49 8B CC                        mov rcx, r12
0031A2C0  44 8D 42 02                     lea r8d, [rdx + 2]
0031A2C4  E8 77 75 FD FF                  call 0x1402f1840
0031A2C9  45 33 DB                        xor r11d, r11d
0031A2CC  49 B9 20 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000020
0031A2D6  49 BA 00 00 00 00 00 01 00 00   movabs r10, 0x10000000000
0031A2E0  E9 4B F8 FF FF                  jmp 0x140319b30
0031A2E5  4C 3B 64 24 60                  cmp r12, qword ptr [rsp + 0x60]
0031A2EA  0F 87 3B FB FF FF               ja 0x140319e2b
0031A2F0  4C 3B 64 24 58                  cmp r12, qword ptr [rsp + 0x58]
0031A2F5  0F 83 7B FB FF FF               jae 0x140319e76
0031A2FB  E9 2B FB FF FF                  jmp 0x140319e2b
0031A300  0F B6 D0                        movzx edx, al
0031A303  0F B6 CB                        movzx ecx, bl
0031A306  E8 F1 B3 1D 00                  call 0x1404f56fc
0031A30B  E9 35 FB FF FF                  jmp 0x140319e45
0031A310  0F B6 D0                        movzx edx, al
0031A313  E8 E4 B3 1D 00                  call 0x1404f56fc
0031A318  E9 57 FE FF FF                  jmp 0x14031a174
0031A31D  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0031A327  48 0B D8                        or rbx, rax
0031A32A  E9 DB F9 FF FF                  jmp 0x140319d0a
0031A32F  83 CE 08                        or esi, 8
0031A332  E9 0C FC FF FF                  jmp 0x140319f43
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFillSystemPtes(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p1A;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p8;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    v_r11 = 0;
    result = 0;
    v_stack_m50 = 0;
    v_stack_p8 = 0;
    v_stack_m80 = 0;
    *(unsigned int *)(a6) = 0;
    v_stack_m60 = v_xmm0;
    if (a4 == 0) goto loc_00319D88;
    if (a4 == 31) goto loc_003198CE;
    result = (unsigned int)(((unsigned int)(a4)) >> (3));
    if (((unsigned int)(result)) == 3) goto loc_00319F6A;
    v_rbp = v_r11 + 1;
    if (((unsigned int)(result)) == ((unsigned int)(v_r11 + 1))) { v_rbp = 0; }
loc_003198CE:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (31));
    v_rbx = (*(unsigned __int64 *)(v_rip - 3182420 + result * 8)) & (result);
    v_rbx = (v_rbx) | (33);
    if (a1 < v_r13) goto loc_00319CA7;
    if (a1 > 0) goto loc_00319CA4;
    if (a1 >= 0) goto loc_00319CD1;
loc_00319931:
    a2 = (v_r13) << (25);
    result = (a1) << (25);
    result = (result) - (a2);
    result = (result) >> (16);
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x4000000ULL));
    if (condition_is_equal) goto loc_0031997B;
    if (result < v_r13) goto loc_0031997B;
loc_00319960:
    if (result > 0) goto loc_0031997B;
    result = (result) << (25);
    result = (result) - (a2);
    result = (result) >> (16);
    if (result >= v_r13) goto loc_00319960;
loc_0031997B:
    if (result <= v_r13) goto loc_003199BB;
    if (result < v_r13) goto loc_003199BF;
    if (result >= v_r13) goto loc_00319D35;
loc_003199A5:
    if (result >= (*(unsigned __int64 *)(v_rip + 11622868))) goto loc_00319CB8;
loc_003199B2:
    goto loc_003199C6;
loc_003199BB:
    v_rbx = (v_rbx) | (4);
loc_003199BF:
loc_003199C6:
    if ((unsigned int)(*(unsigned __int8 *)(v_rip + 11621567)) != 0) {
    }
    v_r11 = 0;
loc_003199D2:
    v_r14 = (unsigned __int8)(((unsigned int)((unsigned int)(result))) & (5));
    v_stack_m78 = 0;
    a2 = (v_rbx) | (66);
    if (((unsigned __int8)(v_r14)) != 4) { a2 = v_rbx; }
    a1 = (*(unsigned __int8 *)(v_rip + 11621547)) << (8);
    a3 = (a2) & (-5);
    if (condition_is_above_or_equal) { a3 = a2; }
    a3 = (a3) ^ (a1);
    a3 = (a3) ^ (a1);
    if (condition_is_above_or_equal) { a3 = a3; }
    if (a4 == 0) { a3 = a3; }
    result = (a3) & (a3);
    result = (result) | (a3);
    v_stack_m68 = result;
    v_r12 = 0;
    if (!sign_flag) { v_r12 = a3 - 1; }
    a1 = a3 - 8;
    if (!sign_flag) { a1 = 0; }
loc_00319A8E:
    if (a2 == 0) goto loc_00319C90;
    if (a1 == 0) goto loc_0031A090;
loc_00319AA7:
    result = a1 + 8;
    if (a1 == 0) { result = a1; }
    v_stack_m70 = result;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) != 0) goto loc_0031A1EA;
loc_00319ABF:
    if ((*(unsigned __int64 *)(a1 + 8)) > (*(unsigned __int64 *)(v_rip + 11616794))) goto loc_00319D92;
    v_rbx = (*(unsigned __int64 *)(a1 + 8) + *(unsigned __int64 *)(a1 + 8) * 2) + (*(unsigned __int64 *)(a1 + 8) + *(unsigned __int64 *)(a1 + 8) * 2);
    result = (*(unsigned __int64 *)(result + v_rbx * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00319D92;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    if (condition_is_not_equal) goto loc_0031A26F;
loc_00319B21:
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a4 + v_rbx * 8))) == 0) goto loc_0031A29E;
loc_00319B30:
    if (sign_flag) goto loc_00319B7F;
    if (((a3) & (*(unsigned __int64 *)(result + v_rbx * 8 + 40))) != 0) goto loc_00319F7B;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rbx * 8 + 40) + v_rbx * 8)) << (25);
    result = (a3) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    if (a1 >= a3) goto loc_00319FCB;
loc_00319B7F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + v_rbx * 8))) >> (16));
    a1 = (unsigned __int8)((a1) & (192));
    if (((unsigned __int8)(a1)) != 192) goto loc_00319C14;
    if ((*(unsigned int *)(v_rip + 11625905)) == 2) goto loc_0031A098;
loc_00319BA1:
    result = MiLockPageInline(result + v_rbx * 8, result + v_rbx * 8, a3, a4);
loc_00319BB7:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + v_rbx * 8))) >> (16));
    a2 = (unsigned __int8)((a2) & (192));
    if (((unsigned __int8)(a2)) == 192) {
        a1 = a4;
        a2 = *(unsigned int *)(a1 + v_rbx * 8);
        result = (unsigned __int8)(v_rbp);
        v_stack_p18 = (unsigned int)(a2);
        a2 = (unsigned int)((a2) >> (16));
        a2 = (unsigned __int8)((a2) & (63));
        result = (unsigned __int8)((result) << (6));
        a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
        v_stack_p1A = (unsigned __int8)(a2);
        a2 = a4;
        result = v_stack_p18;
        *(unsigned int *)(a2 + v_rbx * 8) = (unsigned int)(result);
    }
    if (((unsigned __int8)((unsigned __int8)(result))) != 17) {
        a2 = (unsigned __int8)((unsigned __int8)(result));
        a1 = result + v_rbx * 8;
        result = MiUnlockPage(a1, a2, (unsigned __int8)(result), a4);
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + v_rbx * 8))) >> (16));
    result = (unsigned int)(((unsigned __int8)(a1)) >> (6));
    if (((unsigned int)(v_rbp)) != ((unsigned int)(result))) goto loc_00319F1A;
    result = (*(unsigned __int64 *)(a1 + 8)) << (12);
    v_rbx = (result) ^ (v_stack_m68);
    v_rbx = (v_rbx) & (result + v_rbx * 8);
    v_rbx = (v_rbx) ^ (result);
loc_00319C4A:
    if (condition_is_below) goto loc_00319D46;
loc_00319C59:
    v_r11 = 0;
    *(unsigned __int64 *)(a1) = v_rbx;
loc_00319C84:
    v_r13 = (a2) - 1;
    v_r15 = (a1) + (8);
    goto loc_00319A8E;
loc_00319C90:
    result = 0;
loc_00319C92:
    v_rsp = (v_rsp) + (120);
    return result;
loc_00319CA4:
    v_r11 = 0;
loc_00319CA7:
    a4 = (unsigned int)((a4) & (0x4000000ULL));
    goto loc_003199D2;
loc_00319CB8:
    if (0 > (*(unsigned __int64 *)(v_rip + 11622097))) goto loc_003199B2;
    goto loc_003199C6;
loc_00319CD1:
    if (v_r15 > (*(unsigned __int8 *)(v_rip + 11620793))) goto loc_00319931;
    if (v_r15 == (*(unsigned __int8 *)(v_rip + 11620793))) goto loc_0031A31D;
    if (v_r15 >= (*(unsigned __int8 *)(v_rip + 11620793))) {
        v_rbx = (v_rbx) & (*(unsigned __int8 *)(v_rip + 11620793));
    }
    result = MiUserPdeOrAbove(v_r15, (unsigned int)(a5), v_stack_m78, a4);
    if ((unsigned int)(result) == 0) goto loc_00319931;
    v_rbx = (v_rbx) | (4);
    goto loc_00319931;
loc_00319D35:
    if (result > 0) goto loc_003199A5;
    goto loc_003199CF;
loc_00319D46:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00319C59;
    result = (result) + (0);
    if (v_r15 < result) goto loc_00319C59;
    result = MiCheckLinearProtectedPteAccessedBit(v_r15, v_rbx, 128, a4);
    goto loc_00319C59;
loc_00319D88:
    goto loc_003198CE;
loc_00319D92:
    if (128 == 0) goto loc_00319E20;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 11615894)) + (244));
    result = (1) << ((unsigned __int8)(a1));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(*(unsigned __int64 *)(a1 + 8))));
    result = (unsigned int)((result) - (*(unsigned int *)(v_stack_p38 + 24)));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    result = (result) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p38 + result * 4 + 44))) >> ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) & (3));
    a3 = (128) - 1;
    v_stack_p40 = a3;
loc_00319DD6:
    v_rsi = (unsigned int)(((unsigned int)(a4)) & (7));
    if ((unsigned int)(a2) == 0) goto loc_0031A0D9;
    if (((unsigned int)(a2)) == 2) goto loc_00319FC3;
loc_00319DEA:
    if ((unsigned int)((unsigned int)(v_stack_pC0)) != 0) goto loc_0031A0F4;
loc_00319DF9:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (0xA0000000ULL));
    result = MiMakeValidPte(v_r15, *(unsigned __int64 *)(a1 + 8), a3, a4);
    v_stack_pC0 = (unsigned int)(v_rsi);
    goto loc_00319C4A;
loc_00319E20:
    if (v_stack_p6C != 0) goto loc_0031A2E5;
loc_00319E2B:
    if ((*(unsigned int *)(v_rip + 13291233)) != 0) goto loc_0031A300;
loc_00319E45:
    result = MiIoSpaceGetBounds(v_stack_p58, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if ((*(unsigned int *)(v_rip + 13291207)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_r11 = 0;
loc_00319E76:
    if (v_stack_p6C != 3) goto loc_0031A1E1;
    if (v_stack_p48 == 0) goto loc_0031A0E1;
    if (v_r13 > 1) goto loc_0031A1FC;
loc_00319E98:
    v_stack_p28 = v_stack_p38;
    v_stack_p20 = 0;
    result = MiReferenceIoPages(1, *(unsigned __int64 *)(a1 + 8), 1, 3);
    if (sign_flag) goto loc_0031A06A;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 11615578)) + (244));
    result = (1) << ((unsigned __int8)(a1));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(*(unsigned __int64 *)(a1 + 8))));
    result = (unsigned int)((result) - (*(unsigned int *)(v_stack_p38 + 24)));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    result = (result) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p38 + result * 4 + 44))) >> ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) & (3));
    v_rbx = (1) - 1;
    v_stack_p40 = v_rbx;
    goto loc_00319DD6;
loc_00319F1A:
    v_rsi = (unsigned int)((v_rsi) & (7));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(3 + v_rbx * 8))) >> (16));
    if (((unsigned __int8)(a1)) < 64) goto loc_0031A32F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(3 + v_rbx * 8))) >> (16));
    a1 = (unsigned __int8)((a1) & (192));
    if (((unsigned __int8)(a1)) == 128) {
        v_rsi = (unsigned int)((v_rsi) | (24));
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (0xA0000000ULL));
    result = MiMakeValidPte(v_r15, *(unsigned __int64 *)(a1 + 8), a3, 3);
    goto loc_00319C4A;
loc_00319F6A:
    if ((((unsigned __int8)(v_rsi)) & (7)) == 0) goto loc_003198CE;
    goto loc_003198CE;
loc_00319F7B:
    v_stack_pD8 = 0;
    v_stack_p30 = 0;
    result = MiGetPfnPageSizeIndexUnsynchronized((unsigned int)((unsigned int)(result)), v_stack_pD8, v_stack_p30, 3);
    if (((unsigned int)(result)) == 3) goto loc_0031A064;
    if (v_stack_pD8 != 6) goto loc_0031A064;
    goto loc_00319B7F;
loc_00319FC3:
    v_rsi = (unsigned int)((v_rsi) | (24));
    goto loc_00319DEA;
loc_00319FCB:
    if (((unsigned int)((unsigned int)(result))) > result) goto loc_00319B7F;
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 40)) & ((unsigned int)((unsigned int)(result)));
    if (result == ((unsigned int)((unsigned int)(result)))) goto loc_00319B7F;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(3 + result * 8))) >> (16));
    if ((((unsigned __int8)(a2)) & (32)) == 0) goto loc_0031A042;
    if ((((unsigned int)((unsigned int)(result))) & (*(unsigned __int64 *)(3 + result * 8))) != 0) goto loc_0031A042;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(3 + result * 8))) != 0) goto loc_00319B7F;
loc_0031A042:
    if ((((unsigned __int8)(a2)) & (8)) != 0) goto loc_00319B7F;
    result = MiGetPageTablePfnBuddyRaw((unsigned int)((unsigned int)(result)), a2, v_stack_p30, 3);
    if (result == v_stack_pD0) goto loc_00319B7F;
    goto loc_0031A074;
loc_0031A064:
loc_0031A06A:
loc_0031A074:
    v_rdi = (v_stack_pC8) - (v_r13);
    if (condition_is_not_equal) goto loc_0031A11E;
loc_0031A088:
    goto loc_00319C92;
loc_0031A090:
    v_r12 = (*(unsigned __int64 *)(a1 + 8)) + 1;
    goto loc_00319AA7;
loc_0031A098:
    if ((*(unsigned __int64 *)(v_rip + 11624681)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0031A0D1;
    if (*(unsigned __int64 *)(v_rip + 11624681) == 0) goto loc_00319BA1;
    if (condition_is_above_or_equal) goto loc_00319BA1;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) != 15) goto loc_00319BA1;
loc_0031A0D1:
    goto loc_00319BB7;
loc_0031A0D9:
    v_rsi = (unsigned int)((v_rsi) | (16));
    goto loc_00319DEA;
loc_0031A0E1:
    result = MiIoPagesInRun(v_r12, v_r13, 17, 3);
    goto loc_00319E98;
loc_0031A0F4:
    if (((unsigned int)(result)) != ((unsigned int)(v_rsi))) goto loc_00319DF9;
    v_stack_pC0 = (unsigned int)(v_rsi);
    result = (v_r12) << (12);
    v_rbx = (result) ^ (v_rdi);
    v_rbx = (v_rbx) & ((unsigned int)(0xC0000018ULL));
    v_rbx = (v_rbx) ^ (result);
    goto loc_00319C4A;
loc_0031A11E:
    v_r13 = (v_r13) - (result);
    v_r13 = (v_r13) << (28);
    result = (17) << (25);
    v_r13 = (v_r13) - (result);
    v_r15 = (v_r15) << (25);
    v_r13 = (v_r13) + (v_r15);
    v_r13 = (v_r13) >> (16);
    result = MiVaToFlushVm(v_r13, v_r13, 17, 3);
    result = MiClearMappingAndDereferenceIoSpace(v_r13, v_rbx, 17, 3);
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 2) goto loc_0031A174;
    if ((*(unsigned int *)(v_rip + 13290418)) != 0) goto loc_0031A310;
loc_0031A174:
    result = MiGetProcessorFlushList((unsigned __int8)(v_cr8), v_rbx, 17, 3);
    v_stack_p20 = 1;
    result = MiInitializeTbFlushList(result, result, (unsigned int)(*(unsigned int *)(result + 12)), 8);
    a4 = 0;
    result = MiInsertTbFlushEntry(result, v_r13, v_rbx, a4);
    result = MiFlushTbList(result, v_r13, v_rbx, a4);
    result = MiReleaseProcessorFlushList(result, v_r13, v_rbx, a4);
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 2) goto loc_0031A088;
    if ((*(unsigned int *)(v_rip + 13290331)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rbx, a4);
    }
    goto loc_0031A088;
loc_0031A1E1:
    goto loc_00319DD6;
loc_0031A1EA:
    if (v_r12 != (*(unsigned __int64 *)(v_rip + 11653703))) goto loc_00319ABF;
    goto loc_00319C84;
loc_0031A1FC:
    if (v_r13 - 1 == 0) goto loc_00319E98;
loc_0031A20D:
    result = (*(unsigned __int64 *)(a1 + 8 - 8)) + 1;
    if ((*(unsigned __int64 *)(a1 + 8)) != result) goto loc_00319E98;
    if (((*(unsigned __int64 *)(a1 + 8)) & (511)) == 0) goto loc_00319E98;
    if ((*(unsigned __int64 *)(a1 + 8)) > (*(unsigned __int64 *)(v_rip + 11614892))) goto loc_0031A25C;
    a1 = (*(unsigned __int64 *)(a1 + 8) + *(unsigned __int64 *)(a1 + 8) * 2) + (*(unsigned __int64 *)(a1 + 8) + *(unsigned __int64 *)(a1 + 8) * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_below) goto loc_00319E98;
loc_0031A25C:
    v_rbx = (result) + 1;
    a2 = (a1 + 8) + (8);
    a3 = (v_r13 - 1) - (1);
    if (condition_is_equal) goto loc_00319E98;
    goto loc_0031A20D;
loc_0031A26F:
    result = (unsigned __int8)((*(unsigned __int8 *)(a2)) & (7));
    if (((unsigned __int8)(result)) != 5) goto loc_0031A284;
    if (((unsigned __int8)(result)) < 5) goto loc_00319B21;
loc_0031A284:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x1246ULL), v_r12, a4);
loc_0031A29E:
    if ((unsigned int)(v_r12) == 0) goto loc_0031A2B8;
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(0x1246ULL))) & (7));
    if (((unsigned __int8)(result)) != 5) goto loc_0031A2B8;
    if (((unsigned __int8)(result)) < 5) goto loc_00319B30;
loc_0031A2B8:
    result = MiShowBadMapper(v_r12, 1, 1 + 2, a4);
    v_r11 = 0;
    goto loc_00319B30;
loc_0031A2E5:
    if (v_r12 > v_stack_p60) goto loc_00319E2B;
    if (v_r12 >= v_stack_p58) goto loc_00319E76;
    goto loc_00319E2B;
loc_0031A300:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rbx), (unsigned __int8)(result), 1 + 2, a4);
    goto loc_00319E45;
loc_0031A310:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rbx), (unsigned __int8)(result), 1 + 2, a4);
    goto loc_0031A174;
loc_0031A31D:
    v_rbx = (v_rbx) | (result);
    goto loc_00319D0A;
loc_0031A32F:
    v_rsi = (unsigned int)(((unsigned __int8)(v_cr8)) | (8));
    goto loc_00319F43;
}
```

## 5. (Beta) C Style

```c
int64_t MiFillSystemPtes(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p1A;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p8;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    local_r11 = 0;
    result = 0;
    v_stack_m50 = 0;
    v_stack_p8 = 0;
    v_stack_m80 = 0;
    *(uint32_t *)(arg6) = 0;
    v_stack_m60 = v_xmm0;
    if (Arg4 == 0) goto loc_00319D88;
    if (Arg4 == 31) goto loc_003198CE;
    result = (uint32_t)(((uint32_t)(Arg4)) >> (3));
    if (((uint32_t)(result)) == 3) goto loc_00319F6A;
    local_rbp = local_r11 + 1;
    if (((uint32_t)(result)) == ((uint32_t)(local_r11 + 1))) { local_rbp = 0; }
loc_003198CE:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (31));
    local_rbx = (*(uint64_t *)(v_rip - 0x308F54 + result * 8)) & (result);
    local_rbx = (local_rbx) | (33);
    if (Arg1 < local_r13) goto loc_00319CA7;
    if (Arg1 > 0) goto loc_00319CA4;
    if (Arg1 >= 0) goto loc_00319CD1;
loc_00319931:
    Arg2 = (local_r13) << (25);
    result = (Arg1) << (25);
    result = (result) - (Arg2);
    result = (result) >> (16);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x4000000ULL));
    if (condition_is_equal) goto loc_0031997B;
    if (result < local_r13) goto loc_0031997B;
loc_00319960:
    if (result > 0) goto loc_0031997B;
    result = (result) << (25);
    result = (result) - (Arg2);
    result = (result) >> (16);
    if (result >= local_r13) goto loc_00319960;
loc_0031997B:
    if (result <= local_r13) goto loc_003199BB;
    if (result < local_r13) goto loc_003199BF;
    if (result >= local_r13) goto loc_00319D35;
loc_003199A5:
    if (result >= (*(uint64_t *)(v_rip + 0xB159D4))) goto loc_00319CB8;
loc_003199B2:
    goto loc_003199C6;
loc_003199BB:
    local_rbx = (local_rbx) | (4);
loc_003199BF:
loc_003199C6:
    if ((uint32_t)(*(uint8_t *)(v_rip + 0xB154BF)) != 0) {
    }
    local_r11 = 0;
loc_003199D2:
    local_r14 = (uint8_t)(((uint32_t)((uint32_t)(result))) & (5));
    v_stack_m78 = 0;
    Arg2 = (local_rbx) | (66);
    if (((uint8_t)(local_r14)) != 4) { Arg2 = local_rbx; }
    Arg1 = (*(uint8_t *)(v_rip + 0xB154AB)) << (8);
    Arg3 = (Arg2) & (-5);
    if (condition_is_above_or_equal) { Arg3 = Arg2; }
    Arg3 = (Arg3) ^ (Arg1);
    Arg3 = (Arg3) ^ (Arg1);
    if (condition_is_above_or_equal) { Arg3 = Arg3; }
    if (Arg4 == 0) { Arg3 = Arg3; }
    result = (Arg3) & (Arg3);
    result = (result) | (Arg3);
    v_stack_m68 = result;
    local_r12 = 0;
    if (!sign_flag) { local_r12 = Arg3 - 1; }
    Arg1 = Arg3 - 8;
    if (!sign_flag) { Arg1 = 0; }
loc_00319A8E:
    if (Arg2 == 0) goto loc_00319C90;
    if (Arg1 == 0) goto loc_0031A090;
loc_00319AA7:
    result = Arg1 + 8;
    if (Arg1 == 0) { result = Arg1; }
    v_stack_m70 = result;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) != 0) goto loc_0031A1EA;
loc_00319ABF:
    if ((*(uint64_t *)(Arg1 + 0x8)) > (*(uint64_t *)(v_rip + 0xB1421A))) goto loc_00319D92;
    local_rbx = (*(uint64_t *)(Arg1 + 0x8) + *(uint64_t *)(Arg1 + 0x8) * 2) + (*(uint64_t *)(Arg1 + 0x8) + *(uint64_t *)(Arg1 + 0x8) * 2);
    result = (*(uint64_t *)(result + local_rbx * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00319D92;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    if (condition_is_not_equal) goto loc_0031A26F;
loc_00319B21:
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 8))) == 0) goto loc_0031A29E;
loc_00319B30:
    if (sign_flag) goto loc_00319B7F;
    if (((Arg3) & (*(uint64_t *)(result + local_rbx * 8 + 0x28))) != 0) goto loc_00319F7B;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(result + local_rbx * 8 + 0x28) + local_rbx * 8)) << (25);
    result = (Arg3) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= Arg3) goto loc_00319FCB;
loc_00319B7F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 8))) >> (16));
    Arg1 = (uint8_t)((Arg1) & (192));
    if (((uint8_t)(Arg1)) != 192) goto loc_00319C14;
    if ((*(uint32_t *)(v_rip + 0xB165B1)) == 2) goto loc_0031A098;
loc_00319BA1:
    result = MiLockPageInline(result + local_rbx * 8, result + local_rbx * 8, Arg3, Arg4);
loc_00319BB7:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 8))) >> (16));
    Arg2 = (uint8_t)((Arg2) & (192));
    if (((uint8_t)(Arg2)) == 192) {
        Arg1 = Arg4;
        Arg2 = *(uint32_t *)(Arg1 + local_rbx * 8);
        result = (uint8_t)(local_rbp);
        v_stack_p18 = (uint32_t)(Arg2);
        Arg2 = (uint32_t)((Arg2) >> (16));
        Arg2 = (uint8_t)((Arg2) & (63));
        result = (uint8_t)((result) << (6));
        Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
        v_stack_p1A = (uint8_t)(Arg2);
        Arg2 = Arg4;
        result = v_stack_p18;
        *(uint32_t *)(Arg2 + local_rbx * 8) = (uint32_t)(result);
    }
    if (((uint8_t)((uint8_t)(result))) != 17) {
        Arg2 = (uint8_t)((uint8_t)(result));
        Arg1 = result + local_rbx * 8;
        result = MiUnlockPage(Arg1, Arg2, (uint8_t)(result), Arg4);
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 8))) >> (16));
    result = (uint32_t)(((uint8_t)(Arg1)) >> (6));
    if (((uint32_t)(local_rbp)) != ((uint32_t)(result))) goto loc_00319F1A;
    result = (*(uint64_t *)(Arg1 + 0x8)) << (12);
    local_rbx = (result) ^ (v_stack_m68);
    local_rbx = (local_rbx) & (result + local_rbx * 8);
    local_rbx = (local_rbx) ^ (result);
loc_00319C4A:
    if (condition_is_below) goto loc_00319D46;
loc_00319C59:
    local_r11 = 0;
    *(uint64_t *)(Arg1) = local_rbx;
loc_00319C84:
    local_r13 = (Arg2) - 1;
    local_r15 = (Arg1) + (8);
    goto loc_00319A8E;
loc_00319C90:
    result = 0;
loc_00319C92:
    local_rsp = (local_rsp) + (120);
    return result;
loc_00319CA4:
    local_r11 = 0;
loc_00319CA7:
    Arg4 = (uint32_t)((Arg4) & (0x4000000ULL));
    goto loc_003199D2;
loc_00319CB8:
    if (0 > (*(uint64_t *)(v_rip + 0xB156D1))) goto loc_003199B2;
    goto loc_003199C6;
loc_00319CD1:
    if (local_r15 > (*(uint8_t *)(v_rip + 0xB151B9))) goto loc_00319931;
    if (local_r15 == (*(uint8_t *)(v_rip + 0xB151B9))) goto loc_0031A31D;
    if (local_r15 >= (*(uint8_t *)(v_rip + 0xB151B9))) {
        local_rbx = (local_rbx) & (*(uint8_t *)(v_rip + 0xB151B9));
    }
    result = MiUserPdeOrAbove(local_r15, (uint32_t)(Arg5), v_stack_m78, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00319931;
    local_rbx = (local_rbx) | (4);
    goto loc_00319931;
loc_00319D35:
    if (result > 0) goto loc_003199A5;
    goto loc_003199CF;
loc_00319D46:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00319C59;
    result = (result) + (0);
    if (local_r15 < result) goto loc_00319C59;
    result = MiCheckLinearProtectedPteAccessedBit(local_r15, local_rbx, 128, Arg4);
    goto loc_00319C59;
loc_00319D88:
    goto loc_003198CE;
loc_00319D92:
    if (128 == 0) goto loc_00319E20;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xB13E96)) + (244));
    result = (1) << ((uint8_t)(Arg1));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(*(uint64_t *)(Arg1 + 0x8))));
    result = (uint32_t)((result) - (*(uint32_t *)(v_stack_p38 + 0x18)));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    result = (result) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + result * 4 + 0x2C))) >> ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & (3));
    Arg3 = (128) - 1;
    v_stack_p40 = Arg3;
loc_00319DD6:
    local_rsi = (uint32_t)(((uint32_t)(Arg4)) & (7));
    if ((uint32_t)(Arg2) == 0) goto loc_0031A0D9;
    if (((uint32_t)(Arg2)) == 2) goto loc_00319FC3;
loc_00319DEA:
    if ((uint32_t)((uint32_t)(v_stack_pC0)) != 0) goto loc_0031A0F4;
loc_00319DF9:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (0xA0000000ULL));
    result = MiMakeValidPte(local_r15, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    v_stack_pC0 = (uint32_t)(local_rsi);
    goto loc_00319C4A;
loc_00319E20:
    if (v_stack_p6C != 0) goto loc_0031A2E5;
loc_00319E2B:
    if ((*(uint32_t *)(v_rip + 0xCACEE1)) != 0) goto loc_0031A300;
loc_00319E45:
    result = MiIoSpaceGetBounds(v_stack_p58, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xCACEC7)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_r11 = 0;
loc_00319E76:
    if (v_stack_p6C != 3) goto loc_0031A1E1;
    if (v_stack_p48 == 0) goto loc_0031A0E1;
    if (local_r13 > 1) goto loc_0031A1FC;
loc_00319E98:
    v_stack_p28 = v_stack_p38;
    v_stack_p20 = 0;
    result = MiReferenceIoPages(1, *(uint64_t *)(Arg1 + 0x8), 1, 3);
    if (sign_flag) goto loc_0031A06A;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xB13D5A)) + (244));
    result = (1) << ((uint8_t)(Arg1));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(*(uint64_t *)(Arg1 + 0x8))));
    result = (uint32_t)((result) - (*(uint32_t *)(v_stack_p38 + 0x18)));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    result = (result) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + result * 4 + 0x2C))) >> ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & (3));
    local_rbx = (1) - 1;
    v_stack_p40 = local_rbx;
    goto loc_00319DD6;
loc_00319F1A:
    local_rsi = (uint32_t)((local_rsi) & (7));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(3 + local_rbx * 8))) >> (16));
    if (((uint8_t)(Arg1)) < 64) goto loc_0031A32F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(3 + local_rbx * 8))) >> (16));
    Arg1 = (uint8_t)((Arg1) & (192));
    if (((uint8_t)(Arg1)) == 128) {
        local_rsi = (uint32_t)((local_rsi) | (24));
    }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (0xA0000000ULL));
    result = MiMakeValidPte(local_r15, *(uint64_t *)(Arg1 + 0x8), Arg3, 3);
    goto loc_00319C4A;
loc_00319F6A:
    if ((((uint8_t)(local_rsi)) & (7)) == 0) goto loc_003198CE;
    goto loc_003198CE;
loc_00319F7B:
    v_stack_pD8 = 0;
    v_stack_p30 = 0;
    result = MiGetPfnPageSizeIndexUnsynchronized((uint32_t)((uint32_t)(result)), v_stack_pD8, v_stack_p30, 3);
    if (((uint32_t)(result)) == 3) goto loc_0031A064;
    if (v_stack_pD8 != 6) goto loc_0031A064;
    goto loc_00319B7F;
loc_00319FC3:
    local_rsi = (uint32_t)((local_rsi) | (24));
    goto loc_00319DEA;
loc_00319FCB:
    if (((uint32_t)((uint32_t)(result))) > result) goto loc_00319B7F;
    result = (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x28)) & ((uint32_t)((uint32_t)(result)));
    if (result == ((uint32_t)((uint32_t)(result)))) goto loc_00319B7F;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(3 + result * 8))) >> (16));
    if ((((uint8_t)(Arg2)) & (32)) == 0) goto loc_0031A042;
    if ((((uint32_t)((uint32_t)(result))) & (*(uint64_t *)(3 + result * 8))) != 0) goto loc_0031A042;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(3 + result * 8))) != 0) goto loc_00319B7F;
loc_0031A042:
    if ((((uint8_t)(Arg2)) & (8)) != 0) goto loc_00319B7F;
    result = MiGetPageTablePfnBuddyRaw((uint32_t)((uint32_t)(result)), Arg2, v_stack_p30, 3);
    if (result == v_stack_pD0) goto loc_00319B7F;
    goto loc_0031A074;
loc_0031A064:
loc_0031A06A:
loc_0031A074:
    local_rdi = (v_stack_pC8) - (local_r13);
    if (condition_is_not_equal) goto loc_0031A11E;
loc_0031A088:
    goto loc_00319C92;
loc_0031A090:
    local_r12 = (*(uint64_t *)(Arg1 + 0x8)) + 1;
    goto loc_00319AA7;
loc_0031A098:
    if ((*(uint64_t *)(v_rip + 0xB160E9)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0031A0D1;
    if (*(uint64_t *)(v_rip + 0xB160E9) == 0) goto loc_00319BA1;
    if (condition_is_above_or_equal) goto loc_00319BA1;
    if (((uint8_t)((uint8_t)(v_cr8))) != 15) goto loc_00319BA1;
loc_0031A0D1:
    goto loc_00319BB7;
loc_0031A0D9:
    local_rsi = (uint32_t)((local_rsi) | (16));
    goto loc_00319DEA;
loc_0031A0E1:
    result = MiIoPagesInRun(local_r12, local_r13, 17, 3);
    goto loc_00319E98;
loc_0031A0F4:
    if (((uint32_t)(result)) != ((uint32_t)(local_rsi))) goto loc_00319DF9;
    v_stack_pC0 = (uint32_t)(local_rsi);
    result = (local_r12) << (12);
    local_rbx = (result) ^ (local_rdi);
    local_rbx = (local_rbx) & ((uint32_t)(0xC0000018ULL));
    local_rbx = (local_rbx) ^ (result);
    goto loc_00319C4A;
loc_0031A11E:
    local_r13 = (local_r13) - (result);
    local_r13 = (local_r13) << (28);
    result = (17) << (25);
    local_r13 = (local_r13) - (result);
    local_r15 = (local_r15) << (25);
    local_r13 = (local_r13) + (local_r15);
    local_r13 = (local_r13) >> (16);
    result = MiVaToFlushVm(local_r13, local_r13, 17, 3);
    result = MiClearMappingAndDereferenceIoSpace(local_r13, local_rbx, 17, 3);
    if (((uint8_t)((uint8_t)(v_cr8))) >= 2) goto loc_0031A174;
    if ((*(uint32_t *)(v_rip + 0xCACBB2)) != 0) goto loc_0031A310;
loc_0031A174:
    result = MiGetProcessorFlushList((uint8_t)(v_cr8), local_rbx, 17, 3);
    v_stack_p20 = 1;
    result = MiInitializeTbFlushList(result, result, (uint32_t)(*(uint32_t *)(result + 0xC)), 8);
    Arg4 = 0;
    result = MiInsertTbFlushEntry(result, local_r13, local_rbx, Arg4);
    result = MiFlushTbList(result, local_r13, local_rbx, Arg4);
    result = MiReleaseProcessorFlushList(result, local_r13, local_rbx, Arg4);
    if (((uint8_t)((uint8_t)(v_cr8))) >= 2) goto loc_0031A088;
    if ((*(uint32_t *)(v_rip + 0xCACB5B)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_rbx, Arg4);
    }
    goto loc_0031A088;
loc_0031A1E1:
    goto loc_00319DD6;
loc_0031A1EA:
    if (local_r12 != (*(uint64_t *)(v_rip + 0xB1D247))) goto loc_00319ABF;
    goto loc_00319C84;
loc_0031A1FC:
    if (local_r13 - 1 == 0) goto loc_00319E98;
loc_0031A20D:
    result = (*(uint64_t *)(Arg1 + 0x8 - 0x8)) + 1;
    if ((*(uint64_t *)(Arg1 + 0x8)) != result) goto loc_00319E98;
    if (((*(uint64_t *)(Arg1 + 0x8)) & (511)) == 0) goto loc_00319E98;
    if ((*(uint64_t *)(Arg1 + 0x8)) > (*(uint64_t *)(v_rip + 0xB13AAC))) goto loc_0031A25C;
    Arg1 = (*(uint64_t *)(Arg1 + 0x8) + *(uint64_t *)(Arg1 + 0x8) * 2) + (*(uint64_t *)(Arg1 + 0x8) + *(uint64_t *)(Arg1 + 0x8) * 2);
    result = (*(uint64_t *)(result + Arg1 * 8)) >> (54);
    if (condition_is_below) goto loc_00319E98;
loc_0031A25C:
    local_rbx = (result) + 1;
    Arg2 = (Arg1 + 8) + (8);
    Arg3 = (local_r13 - 1) - (1);
    if (condition_is_equal) goto loc_00319E98;
    goto loc_0031A20D;
loc_0031A26F:
    result = (uint8_t)((*(uint8_t *)(Arg2)) & (7));
    if (((uint8_t)(result)) != 5) goto loc_0031A284;
    if (((uint8_t)(result)) < 5) goto loc_00319B21;
loc_0031A284:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x1246ULL), local_r12, Arg4);
loc_0031A29E:
    if ((uint32_t)(local_r12) == 0) goto loc_0031A2B8;
    result = (uint8_t)((*(uint8_t *)((uint32_t)(0x1246ULL))) & (7));
    if (((uint8_t)(result)) != 5) goto loc_0031A2B8;
    if (((uint8_t)(result)) < 5) goto loc_00319B30;
loc_0031A2B8:
    result = MiShowBadMapper(local_r12, 1, 1 + 2, Arg4);
    local_r11 = 0;
    goto loc_00319B30;
loc_0031A2E5:
    if (local_r12 > v_stack_p60) goto loc_00319E2B;
    if (local_r12 >= v_stack_p58) goto loc_00319E76;
    goto loc_00319E2B;
loc_0031A300:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rbx), (uint8_t)(result), 1 + 2, Arg4);
    goto loc_00319E45;
loc_0031A310:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rbx), (uint8_t)(result), 1 + 2, Arg4);
    goto loc_0031A174;
loc_0031A31D:
    local_rbx = (local_rbx) | (result);
    goto loc_00319D0A;
loc_0031A32F:
    local_rsi = (uint32_t)(((uint8_t)(v_cr8)) | (8));
    goto loc_00319F43;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `R/W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00319850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
