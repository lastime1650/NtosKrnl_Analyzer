# MiGetUltraMapping

- RVA: `0x00323270`–`0x00323899` (길이 `1,577` bytes)
- VA: `0x0000000140323270`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075908`
- 디코드: `363`개 명령, `1,577/1,577` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00323368` → [ExpWaitForSpinLockExclusiveAndAcquire](ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x0032343F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0032347C` → [MiRewritePteWithLockBit](MiRewritePteWithLockBit_function_00322FEC.md) (function, `0x00322FEC`)
- `0x0032349F` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x003234D0` → [ExpWaitForSpinLockExclusiveAndAcquire](ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x00323533` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00323554` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x003235C0` → [MiRewritePteWithLockBit](MiRewritePteWithLockBit_function_00322FEC.md) (function, `0x00322FEC`)
- `0x003235F5` → [MiReuseUltraPageTable](../47/MiReuseUltraPageTable_function_00472298.md) (function, `0x00472298`)
- `0x00323627` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00323689` → [MiReuseUltraPageTable](../47/MiReuseUltraPageTable_function_00472298.md) (function, `0x00472298`)
- `0x003236A1` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003236B1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003236C2` → [MiGetHighestUltraLevel](../29/MiGetHighestUltraLevel_function_002972AC.md) (function, `0x002972AC`)
- `0x003236DA` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0032374A` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x0032379A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003237AA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003237CE` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x003237F2` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0032382E` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0032385C` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0032388F` → [MiDeleteUltraMapHierarchy](../47/MiDeleteUltraMapHierarchy_function_004722FC.md) (function, `0x004722FC`)

### Direct callers
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x00229270`
- [MiZeroLargePage](../2C/MiZeroLargePage_function_002C6914.md) at `0x002C6B9B`
- [MiZeroLargePage](../2C/MiZeroLargePage_function_002C6914.md) at `0x002C6BB6`
- [MiZeroWithUltraSpace](../2C/MiZeroWithUltraSpace_function_002C6C9C.md) at `0x002C6CF7`
- [MiDeleteUltraMapContext](../2D/MiDeleteUltraMapContext_function_002DC9A4.md) at `0x002DCA00`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00315B10`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00315B41`
- [MiMapBackgroundPagesToZero](../31/MiMapBackgroundPagesToZero_function_0031E940.md) at `0x0031E9BA`
- [MiComputeCombineHash](MiComputeCombineHash_function_003227C0.md) at `0x003227FF`
- [sub_00322C9B](Unknown_function_00322C9B.md) at `0x00322D04`
- [sub_00322EC8](Unknown_function_00322EC8.md) at `0x00322F08`
- [MiAllocateHyperSpace](MiAllocateHyperSpace_function_00322F90.md) at `0x00322FB6`
- [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) at `0x00332CA1`
- [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) at `0x00364C7B`
- [MiScrubPage](../3F/MiScrubPage_function_003F954C.md) at `0x003F959F`
- [MiInitializeNewUltraHugeContext](../3F/MiInitializeNewUltraHugeContext_function_003FB974.md) at `0x003FBB6A`
- [MmMapMdl](../67/MmMapMdl_function_0067CBA0.md) at `0x0067CC89`
- [MiHugePageOperation](../68/MiHugePageOperation_function_0068C490.md) at `0x0068C583`
- [MiUseProcessorHugeMappingAtDpc](../68/MiUseProcessorHugeMappingAtDpc_function_0068C894.md) at `0x0068C8F0`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x0069452A`
- [MiUpdateForkMaps](../../page/A7/MiUpdateForkMaps_function_00A7DAF8.md) at `0x00A7DC08`
- [sub_00B42A1A](../../page/B4/Unknown_function_00B42A1A.md) at `0x00B42A62`

### Static image references
- `0x0032328C` → RVA `0x00011040` (`.rdata`; read)
- `0x00323335` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00323342` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0032334F` → RVA `0x00E35FE0` (`.data`; read/write)
- `0x00323361` → RVA `0x00E35FE0` (`.data`; read)
- `0x00323398` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003233D4` → RVA `0x00E35FE8` (`.data`; read)
- `0x003233FE` → RVA `0x00E36010` (`.data`; read)
- `0x00323427` → RVA `0x00E35FE0` (`.data`; write)
- `0x0032346E` → RVA `0x00010880` (`.rdata`; read)
- `0x00323486` → RVA `0x00F0DE58` (`.data`; read)
- `0x003235E4` → RVA `0x00E2DC41` (`.data`; read)
- `0x0032362C` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00323693` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00323270  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00323275  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0032327A  55                              push rbp
0032327B  56                              push rsi
0032327C  57                              push rdi
0032327D  41 54                           push r12
0032327F  41 55                           push r13
00323281  41 56                           push r14
00323283  41 57                           push r15
00323285  48 83 EC 30                     sub rsp, 0x30
00323289  48 8B 19                        mov rbx, qword ptr [rcx]
0032328C  4C 8D 35 AD DD CE FF            lea r14, [rip - 0x312253]
00323293  8B F2                           mov esi, edx
00323295  41 8B E9                        mov ebp, r9d
00323298  4D 8B E8                        mov r13, r8
0032329B  48 8B F9                        mov rdi, rcx
0032329E  4D 8B 34 F6                     mov r14, qword ptr [r14 + rsi*8]
003232A2  48 85 DB                        test rbx, rbx
003232A5  74 74                           je 0x14032331b
003232A7  83 FE 01                        cmp esi, 1
003232AA  B9 00 00 20 00                  mov ecx, 0x200000
003232AF  B8 00 00 00 40                  mov eax, 0x40000000
003232B4  4D 8B F8                        mov r15, r8
003232B7  0F 45 C1                        cmovne eax, ecx
003232BA  8B C8                           mov ecx, eax
003232BC  48 C1 E1 09                     shl rcx, 9
003232C0  85 D2                           test edx, edx
003232C2  48 0F 45 C8                     cmovne rcx, rax
003232C6  49 C1 E7 0C                     shl r15, 0xc
003232CA  48 8D 41 FF                     lea rax, [rcx - 1]
003232CE  48 23 C3                        and rax, rbx
003232D1  49 8D 14 07                     lea rdx, [r15 + rax]
003232D5  48 3B D1                        cmp rdx, rcx
003232D8  0F 87 80 02 00 00               ja 0x14032355e
003232DE  48 85 C0                        test rax, rax
003232E1  0F 84 77 02 00 00               je 0x14032355e
003232E7  41 0F BA E1 01                  bt r9d, 1
003232EC  0F 82 6C 02 00 00               jb 0x14032355e
003232F2  49 8D 04 1F                     lea rax, [r15 + rbx]
003232F6  48 89 07                        mov qword ptr [rdi], rax
003232F9  48 8B C3                        mov rax, rbx
003232FC  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00323304  48 83 C4 30                     add rsp, 0x30
00323308  41 5F                           pop r15
0032330A  41 5E                           pop r14
0032330C  41 5D                           pop r13
0032330E  41 5C                           pop r12
00323310  5F                              pop rdi
00323311  5E                              pop rsi
00323312  5D                              pop rbp
00323313  C3                              ret
00323314  CC                              int3
00323315  48 8B 1F                        mov rbx, qword ptr [rdi]
00323318  49 2B DE                        sub rbx, r14
0032331B  45 33 E4                        xor r12d, r12d
0032331E  40 F6 C5 04                     test bpl, 4
00323322  0F 85 81 01 00 00               jne 0x1403234a9
00323328  45 0F 20 C7                     mov r15, cr8
0032332C  B8 02 00 00 00                  mov eax, 2
00323331  44 0F 22 C0                     mov cr8, rax
00323335  44 39 25 E4 39 CA 00            cmp dword ptr [rip + 0xca39e4], r12d
0032333C  0F 85 EA 01 00 00               jne 0x14032352c
00323342  F6 05 BD 37 CA 00 21            test byte ptr [rip + 0xca37bd], 0x21
00323349  0F 85 37 01 00 00               jne 0x140323486
0032334F  F0 0F BA 2D 88 2C B1 00 1F      lock bts dword ptr [rip + 0xb12c88], 0x1f
00323358  45 8B F4                        mov r14d, r12d
0032335B  73 13                           jae 0x140323370
0032335D  41 0F B6 D7                     movzx edx, r15b
00323361  48 8D 0D 78 2C B1 00            lea rcx, [rip + 0xb12c78]
00323368  E8 33 06 00 00                  call 0x1403239a0
0032336D  44 8B F0                        mov r14d, eax
00323370  8B 15 6A 2C B1 00               mov edx, dword ptr [rip + 0xb12c6a]
00323376  8B CA                           mov ecx, edx
00323378  0F BA F1 1E                     btr ecx, 0x1e
0032337C  81 F9 00 00 00 80               cmp ecx, 0x80000000
00323382  74 36                           je 0x1403233ba
00323384  0F BA E2 1E                     bt edx, 0x1e
00323388  72 0B                           jb 0x140323395
0032338A  F0 81 0D 4B 2C B1 00 00 00 00 40  lock or dword ptr [rip + 0xb12c4b], 0x40000000
00323395  41 FF C6                        inc r14d
00323398  44 85 35 0D 1F CA 00            test dword ptr [rip + 0xca1f0d], r14d
0032339F  0F 84 EE 02 00 00               je 0x140323693
003233A5  F3 90                           pause
003233A7  8B 15 33 2C B1 00               mov edx, dword ptr [rip + 0xb12c33]
003233AD  8B C2                           mov eax, edx
003233AF  0F BA F0 1E                     btr eax, 0x1e
003233B3  3D 00 00 00 80                  cmp eax, 0x80000000
003233B8  75 CA                           jne 0x140323384
003233BA  48 B8 00 00 A0 7D FB F6 FF FF   movabs rax, 0xfffff6fb7da00000
003233C4  48 85 DB                        test rbx, rbx
003233C7  0F 84 99 04 00 00               je 0x140323866
003233CD  4C 8B F3                        mov r14, rbx
003233D0  48 C1 EB 1B                     shr rbx, 0x1b
003233D4  4C 2B 35 0D 2C B1 00            sub r14, qword ptr [rip + 0xb12c0d]
003233DB  81 E3 F8 FF 1F 00               and ebx, 0x1ffff8
003233E1  49 C1 EE 1E                     shr r14, 0x1e
003233E5  48 8B C0                        mov rax, rax
003233E8  48 03 D8                        add rbx, rax
003233EB  48 8B 03                        mov rax, qword ptr [rbx]
003233EE  48 85 C0                        test rax, rax
003233F1  75 7B                           jne 0x14032346e
003233F3  8B DD                           mov ebx, ebp
003233F5  83 E3 02                        and ebx, 2
003233F8  0F 84 6E 02 00 00               je 0x14032366c
003233FE  48 8B 05 0B 2C B1 00            mov rax, qword ptr [rip + 0xb12c0b]
00323405  4C 0F AB 30                     bts qword ptr [rax], r14
00323409  85 DB                           test ebx, ebx
0032340B  0F 84 AA 02 00 00               je 0x1403236bb
00323411  4C 89 27                        mov qword ptr [rdi], r12
00323414  41 80 FF 11                     cmp r15b, 0x11
00323418  74 39                           je 0x140323453
0032341A  F6 05 E5 36 CA 00 01            test byte ptr [rip + 0xca36e5], 1
00323421  0F 85 8D 03 00 00               jne 0x1403237b4
00323427  44 89 25 B2 2B B1 00            mov dword ptr [rip + 0xb12bb2], r12d
0032342E  44 39 25 EB 38 CA 00            cmp dword ptr [rip + 0xca38eb], r12d
00323435  74 0D                           je 0x140323444
00323437  44 0F 20 C1                     mov rcx, cr8
0032343B  41 0F B6 D7                     movzx edx, r15b
0032343F  E8 54 22 1D 00                  call 0x1404f5698
00323444  41 0F B6 C7                     movzx eax, r15b
00323448  44 0F 22 C0                     mov cr8, rax
0032344C  33 C0                           xor eax, eax
0032344E  E9 A9 FE FF FF                  jmp 0x1403232fc
00323453  F6 05 AC 36 CA 00 01            test byte ptr [rip + 0xca36ac], 1
0032345A  0F 85 78 03 00 00               jne 0x1403237d8
00323460  44 89 25 79 2B B1 00            mov dword ptr [rip + 0xb12b79], r12d
00323467  33 C0                           xor eax, eax
00323469  E9 8E FE FF FF                  jmp 0x1403232fc
0032346E  4C 8B 0D 0B D4 CE FF            mov r9, qword ptr [rip - 0x312bf5]
00323475  4C 8B C3                        mov r8, rbx
00323478  33 D2                           xor edx, edx
0032347A  33 C9                           xor ecx, ecx
0032347C  E8 6B FB FF FF                  call 0x140322fec
00323481  E9 6D FF FF FF                  jmp 0x1403233f3
00323486  8B 05 CC A9 BE 00               mov eax, dword ptr [rip + 0xbea9cc]
0032348C  85 C0                           test eax, eax
0032348E  0F 85 BB FE FF FF               jne 0x14032334f
00323494  41 0F B6 D7                     movzx edx, r15b
00323498  48 8D 0D 41 2B B1 00            lea rcx, [rip + 0xb12b41]
0032349F  E8 CC 05 00 00                  call 0x140323a70
003234A4  E9 11 FF FF FF                  jmp 0x1403233ba
003234A9  F6 05 56 36 CA 00 21            test byte ptr [rip + 0xca3656], 0x21
003234B0  41 B7 11                        mov r15b, 0x11
003234B3  0F 85 84 00 00 00               jne 0x14032353d
003234B9  F0 0F BA 2D 1E 2B B1 00 1F      lock bts dword ptr [rip + 0xb12b1e], 0x1f
003234C2  45 8B F4                        mov r14d, r12d
003234C5  73 11                           jae 0x1403234d8
003234C7  B2 FF                           mov dl, 0xff
003234C9  48 8D 0D 10 2B B1 00            lea rcx, [rip + 0xb12b10]
003234D0  E8 CB 04 00 00                  call 0x1403239a0
003234D5  44 8B F0                        mov r14d, eax
003234D8  8B 15 02 2B B1 00               mov edx, dword ptr [rip + 0xb12b02]
003234DE  8B CA                           mov ecx, edx
003234E0  0F BA F1 1E                     btr ecx, 0x1e
003234E4  81 F9 00 00 00 80               cmp ecx, 0x80000000
003234EA  0F 84 CA FE FF FF               je 0x1403233ba
003234F0  0F BA E2 1E                     bt edx, 0x1e
003234F4  72 0B                           jb 0x140323501
003234F6  F0 81 0D DF 2A B1 00 00 00 00 40  lock or dword ptr [rip + 0xb12adf], 0x40000000
00323501  41 FF C6                        inc r14d
00323504  44 85 35 A1 1D CA 00            test dword ptr [rip + 0xca1da1], r14d
0032350B  0F 84 7B 02 00 00               je 0x14032378c
00323511  F3 90                           pause
00323513  8B 15 C7 2A B1 00               mov edx, dword ptr [rip + 0xb12ac7]
00323519  8B C2                           mov eax, edx
0032351B  0F BA F0 1E                     btr eax, 0x1e
0032351F  3D 00 00 00 80                  cmp eax, 0x80000000
00323524  0F 84 90 FE FF FF               je 0x1403233ba
0032352A  EB C4                           jmp 0x1403234f0
0032352C  0F B6 D0                        movzx edx, al
0032352F  41 0F B6 CF                     movzx ecx, r15b
00323533  E8 C4 21 1D 00                  call 0x1404f56fc
00323538  E9 05 FE FF FF                  jmp 0x140323342
0032353D  8B 05 15 A9 BE 00               mov eax, dword ptr [rip + 0xbea915]
00323543  85 C0                           test eax, eax
00323545  0F 85 6E FF FF FF               jne 0x1403234b9
0032354B  B2 FF                           mov dl, 0xff
0032354D  48 8D 0D 8C 2A B1 00            lea rcx, [rip + 0xb12a8c]
00323554  E8 17 05 00 00                  call 0x140323a70
00323559  E9 5C FE FF FF                  jmp 0x1403233ba
0032355E  83 FE 01                        cmp esi, 1
00323561  0F 82 AE FD FF FF               jb 0x140323315
00323567  48 3B D1                        cmp rdx, rcx
0032356A  76 0F                           jbe 0x14032357b
0032356C  48 FF CB                        dec rbx
0032356F  48 03 D9                        add rbx, rcx
00323572  48 F7 D9                        neg rcx
00323575  48 23 D9                        and rbx, rcx
00323578  48 89 1F                        mov qword ptr [rdi], rbx
0032357B  48 FF CB                        dec rbx
0032357E  48 C1 EB 12                     shr rbx, 0x12
00323582  81 E3 F8 FF FF 3F               and ebx, 0x3ffffff8
00323588  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00323592  48 03 D8                        add rbx, rax
00323595  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
0032359F  83 FE 01                        cmp esi, 1
003235A2  0F 84 C8 02 00 00               je 0x140323870
003235A8  0F BA E5 01                     bt ebp, 1
003235AC  0F 82 DA 02 00 00               jb 0x14032388c
003235B2  4C 8B 0D C7 D2 CE FF            mov r9, qword ptr [rip - 0x312d39]
003235B9  4C 8B C3                        mov r8, rbx
003235BC  33 D2                           xor edx, edx
003235BE  33 C9                           xor ecx, ecx
003235C0  E8 27 FA FF FF                  call 0x140322fec
003235C5  83 FE 01                        cmp esi, 1
003235C8  0F 84 47 FD FF FF               je 0x140323315
003235CE  48 83 C3 08                     add rbx, 8
003235D2  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003235D7  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
003235DE  0F 84 31 FD FF FF               je 0x140323315
003235E4  80 3D 56 A6 B0 00 00            cmp byte ptr [rip + 0xb0a656], 0
003235EB  74 0D                           je 0x1403235fa
003235ED  BA 01 00 00 00                  mov edx, 1
003235F2  48 8B CF                        mov rcx, rdi
003235F5  E8 9E EC 14 00                  call 0x140472298
003235FA  49 8B C4                        mov rax, r12
003235FD  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
00323601  4C 8B E3                        mov r12, rbx
00323604  49 C1 E4 19                     shl r12, 0x19
00323608  41 B8 04 00 00 B8               mov r8d, 0xb8000004
0032360E  48 C1 E0 19                     shl rax, 0x19
00323612  48 8B CB                        mov rcx, rbx
00323615  4C 2B E0                        sub r12, rax
00323618  49 C1 FC 10                     sar r12, 0x10
0032361C  49 C1 E4 19                     shl r12, 0x19
00323620  4C 2B E0                        sub r12, rax
00323623  49 C1 FC 10                     sar r12, 0x10
00323627  E8 64 1F FA FF                  call 0x1402c5590
0032362C  48 0F BA 25 53 34 CA 00 24      bt qword ptr [rip + 0xca3453], 0x24
00323635  48 8B D8                        mov rbx, rax
00323638  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
00323642  0F 82 B6 01 00 00               jb 0x1403237fe
00323648  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
0032364D  4B 8D 0C 27                     lea rcx, [r15 + r12]
00323651  48 89 18                        mov qword ptr [rax], rbx
00323654  C6 47 19 01                     mov byte ptr [rdi + 0x19], 1
00323658  48 89 0F                        mov qword ptr [rdi], rcx
0032365B  4D 85 E4                        test r12, r12
0032365E  0F 84 B1 FC FF FF               je 0x140323315
00323664  49 8B C4                        mov rax, r12
00323667  E9 90 FC FF FF                  jmp 0x1403232fc
0032366C  44 38 25 CE A5 B0 00            cmp byte ptr [rip + 0xb0a5ce], r12b
00323673  0F 84 85 FD FF FF               je 0x1403233fe
00323679  48 83 7F 08 FF                  cmp qword ptr [rdi + 8], -1
0032367E  0F 84 7A FD FF FF               je 0x1403233fe
00323684  33 D2                           xor edx, edx
00323686  48 8B CF                        mov rcx, rdi
00323689  E8 0A EC 14 00                  call 0x140472298
0032368E  E9 6B FD FF FF                  jmp 0x1403233fe
00323693  8B 05 1F 34 CA 00               mov eax, dword ptr [rip + 0xca341f]
00323699  A8 40                           test al, 0x40
0032369B  0F 84 04 FD FF FF               je 0x1403233a5
003236A1  E8 EA BD FE FF                  call 0x14030f490
003236A6  84 C0                           test al, al
003236A8  0F 84 F7 FC FF FF               je 0x1403233a5
003236AE  41 8B CE                        mov ecx, r14d
003236B1  E8 AA BD FE FF                  call 0x14030f460
003236B6  E9 EC FC FF FF                  jmp 0x1403233a7
003236BB  48 8D 0D 1E 29 B1 00            lea rcx, [rip + 0xb1291e]
003236C2  E8 E5 3B F7 FF                  call 0x1402972ac
003236C7  41 0F B6 D7                     movzx edx, r15b
003236CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003236D0  48 8D 0D 09 29 B1 00            lea rcx, [rip + 0xb12909]
003236D7  48 8B D8                        mov rbx, rax
003236DA  E8 E1 4B F2 FF                  call 0x1402482c0
003236DF  40 F6 C5 01                     test bpl, 1
003236E3  75 0A                           jne 0x1403236ef
003236E5  49 C1 E5 0C                     shl r13, 0xc
003236E9  4C 03 EB                        add r13, rbx
003236EC  4C 89 2F                        mov qword ptr [rdi], r13
003236EF  85 F6                           test esi, esi
003236F1  0F 84 02 FC FF FF               je 0x1403232f9
003236F7  4C 8B F3                        mov r14, rbx
003236FA  48 B8 00 00 A0 7D FB F6 FF FF   movabs rax, 0xfffff6fb7da00000
00323704  49 C1 EE 1B                     shr r14, 0x1b
00323708  41 81 E6 F8 FF 1F 00            and r14d, 0x1ffff8
0032370F  48 8B C0                        mov rax, rax
00323712  4C 03 F0                        add r14, rax
00323715  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
0032371F  49 8B ED                        mov rbp, r13
00323722  48 C1 E5 19                     shl rbp, 0x19
00323726  4C 8D 7F 08                     lea r15, [rdi + 8]
0032372A  83 FE 01                        cmp esi, 1
0032372D  48 BF 00 00 00 00 40 00 00 00   movabs rdi, 0x4000000000
00323737  41 0F 95 C4                     setne r12b
0032373B  49 FF C4                        inc r12
0032373E  49 8B 17                        mov rdx, qword ptr [r15]
00323741  41 B8 04 00 00 B8               mov r8d, 0xb8000004
00323747  49 8B CE                        mov rcx, r14
0032374A  E8 41 1E FA FF                  call 0x1402c5590
0032374F  48 0F BA 25 30 33 CA 00 24      bt qword ptr [rip + 0xca3330], 0x24
00323758  48 8B D8                        mov rbx, rax
0032375B  0F 82 D7 00 00 00               jb 0x140323838
00323761  49 89 1E                        mov qword ptr [r14], rbx
00323764  49 83 C7 08                     add r15, 8
00323768  49 C1 E6 19                     shl r14, 0x19
0032376C  4C 2B F5                        sub r14, rbp
0032376F  49 C1 FE 10                     sar r14, 0x10
00323773  49 83 EC 01                     sub r12, 1
00323777  75 C5                           jne 0x14032373e
00323779  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0032377E  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00323783  C6 47 19 01                     mov byte ptr [rdi + 0x19], 1
00323787  E9 70 FB FF FF                  jmp 0x1403232fc
0032378C  8B 05 26 33 CA 00               mov eax, dword ptr [rip + 0xca3326]
00323792  A8 40                           test al, 0x40
00323794  0F 84 77 FD FF FF               je 0x140323511
0032379A  E8 F1 BC FE FF                  call 0x14030f490
0032379F  84 C0                           test al, al
003237A1  0F 84 6A FD FF FF               je 0x140323511
003237A7  41 8B CE                        mov ecx, r14d
003237AA  E8 B1 BC FE FF                  call 0x14030f460
003237AF  E9 5F FD FF FF                  jmp 0x140323513
003237B4  8B 05 9E A6 BE 00               mov eax, dword ptr [rip + 0xbea69e]
003237BA  85 C0                           test eax, eax
003237BC  0F 85 65 FC FF FF               jne 0x140323427
003237C2  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
003237C7  48 8D 0D 12 28 B1 00            lea rcx, [rip + 0xb12812]
003237CE  E8 71 D7 F9 FF                  call 0x1402c0f44
003237D3  E9 56 FC FF FF                  jmp 0x14032342e
003237D8  8B 05 7A A6 BE 00               mov eax, dword ptr [rip + 0xbea67a]
003237DE  85 C0                           test eax, eax
003237E0  0F 85 7A FC FF FF               jne 0x140323460
003237E6  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
003237EB  48 8D 0D EE 27 B1 00            lea rcx, [rip + 0xb127ee]
003237F2  E8 4D D7 F9 FF                  call 0x1402c0f44
003237F7  33 C0                           xor eax, eax
003237F9  E9 FE FA FF FF                  jmp 0x1403232fc
003237FE  F6 C3 20                        test bl, 0x20
00323801  0F 85 41 FE FF FF               jne 0x140323648
00323807  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00323811  48 8B C0                        mov rax, rax
00323814  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00323819  49 03 C0                        add rax, r8
0032381C  48 3B C8                        cmp rcx, rax
0032381F  0F 82 23 FE FF FF               jb 0x140323648
00323825  41 B8 80 00 00 00               mov r8d, 0x80
0032382B  48 8B D3                        mov rdx, rbx
0032382E  E8 4D F5 F6 FF                  call 0x140292d80
00323833  E9 10 FE FF FF                  jmp 0x140323648
00323838  F6 C3 20                        test bl, 0x20
0032383B  0F 85 20 FF FF FF               jne 0x140323761
00323841  49 8B C5                        mov rax, r13
00323844  48 03 C7                        add rax, rdi
00323847  4C 3B F0                        cmp r14, rax
0032384A  0F 82 11 FF FF FF               jb 0x140323761
00323850  41 B8 80 00 00 00               mov r8d, 0x80
00323856  48 8B D3                        mov rdx, rbx
00323859  49 8B CE                        mov rcx, r14
0032385C  E8 1F F5 F6 FF                  call 0x140292d80
00323861  E9 FB FE FF FF                  jmp 0x140323761
00323866  8B DD                           mov ebx, ebp
00323868  83 E3 02                        and ebx, 2
0032386B  E9 99 FB FF FF                  jmp 0x140323409
00323870  48 C1 EB 09                     shr rbx, 9
00323874  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032387E  48 23 D8                        and rbx, rax
00323881  49 8B C4                        mov rax, r12
00323884  48 03 D8                        add rbx, rax
00323887  E9 1C FD FF FF                  jmp 0x1403235a8
0032388C  48 8B CB                        mov rcx, rbx
0032388F  E8 68 EA 14 00                  call 0x1404722fc
00323894  E9 7C FA FF FF                  jmp 0x140323315
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetUltraMapping(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0032331B;
    result = (unsigned int)(0x40000000ULL);
    if (((unsigned int)((unsigned int)(a2))) != 1) { result = (unsigned int)((unsigned int)(0x200000ULL)); }
    a1 = ((unsigned int)((unsigned int)(result))) << (9);
    if (a2 != 0) { a1 = result; }
    v_r15 = (a3) << (12);
    result = (a1 - 1) & (*(unsigned __int64 *)(a1));
    if ((v_r15 + result * 1) > a1) goto loc_0032355E;
    if (result == 0) goto loc_0032355E;
    if (condition_is_below) goto loc_0032355E;
    *(unsigned __int64 *)(a1) = v_r15 + *(unsigned __int64 *)(a1) * 1;
loc_003232F9:
loc_003232FC:
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(a1);
loc_00323315:
    v_rbx = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(v_rip - 3220051 + (unsigned int)(a2) * 8));
loc_0032331B:
    v_r12 = 0;
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) != 0) goto loc_003234A9;
    if ((*(unsigned int *)(v_rip + 13253092)) != 0) goto loc_0032352C;
loc_00323342:
    if (((*(unsigned __int8 *)(v_rip + 13252541)) & (33)) != 0) goto loc_00323486;
loc_0032334F:
    result = 2;
    v_r14 = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)(v_cr8);
        a1 = v_rip + 11611256;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        v_r14 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11611242)))))) == 0x80000000ULL) goto loc_003233BA;
loc_00323384:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11611242)))))) >= 0x80000000ULL) {
    }
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 13246221)) & ((unsigned int)(v_r14))) == 0) goto loc_00323693;
loc_003233A5:
loc_003233A7:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11611187)))))) != 0x80000000ULL) goto loc_00323384;
loc_003233BA:
    if (v_rbx == 0) goto loc_00323866;
    v_rbx = (v_rbx) >> (27);
    v_r14 = (v_rbx) - (*(unsigned __int64 *)(v_rip + 11611149));
    v_rbx = (unsigned int)((v_rbx) & (0x1FFFF8ULL));
    v_r14 = (v_r14) >> (30);
    v_rbx = (v_rbx) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11611187)))));
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_0032346E;
loc_003233F3:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (2));
    if (condition_is_equal) goto loc_0032366C;
loc_003233FE:
loc_00323409:
    if ((unsigned int)(v_rbx) == 0) goto loc_003236BB;
    *(unsigned __int64 *)(a1) = 0;
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00323453;
    if (((*(unsigned __int8 *)(v_rip + 13252325)) & (1)) != 0) goto loc_003237B4;
loc_00323427:
    *(unsigned int *)(v_rip + 11611058) = 0;
loc_0032342E:
    result = *(unsigned __int64 *)(v_rip + 11611147);
    if ((*(unsigned int *)(v_rip + 13252843)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = 0;
    goto loc_003232FC;
loc_00323453:
    if (((*(unsigned __int8 *)(v_rip + 13252268)) & (1)) != 0) goto loc_003237D8;
loc_00323460:
    *(unsigned int *)(v_rip + 11611001) = 0;
    result = 0;
    goto loc_003232FC;
loc_0032346E:
    a2 = 0;
    a1 = 0;
    result = MiRewritePteWithLockBit(a1, a2, v_rbx, *(unsigned __int64 *)(v_rip - 3222517));
    goto loc_003233F3;
loc_00323486:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12495308))) != 0) goto loc_0032334F;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 11610945, (unsigned __int8)(v_cr8), v_rbx, *(unsigned __int64 *)(v_rip - 3222517));
    goto loc_003233BA;
loc_003234A9:
    if (((*(unsigned __int8 *)(v_rip + 13252182)) & (33)) != 0) goto loc_0032353D;
loc_003234B9:
    v_r14 = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        a1 = v_rip + 11610896;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, v_rbx, *(unsigned __int64 *)(v_rip - 3222517));
        v_r14 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11610882)))))) == 0x80000000ULL) goto loc_003233BA;
loc_003234F0:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11610882)))))) >= 0x80000000ULL) {
    }
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 13245857)) & ((unsigned int)(v_r14))) == 0) goto loc_0032378C;
loc_00323511:
loc_00323513:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11610823)))))) == 0x80000000ULL) goto loc_003233BA;
    goto loc_003234F0;
loc_0032352C:
    result = KiRaiseIrqlProcessIrqlFlags(17, (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11610823))))), v_rbx, *(unsigned __int64 *)(v_rip - 3222517));
    goto loc_00323342;
loc_0032353D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12495125))) != 0) goto loc_003234B9;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 11610764, 255, v_rbx, *(unsigned __int64 *)(v_rip - 3222517));
    goto loc_003233BA;
loc_0032355E:
    if (((unsigned int)((unsigned int)(a2))) < 1) goto loc_00323315;
    if (255 >= = (v_rip + 11610764)) {
        v_rbx = (v_rbx) - 1;
        v_rbx = (v_rbx) + (v_rip + 11610764);
        a1 = -(v_rip + 11610764);
        v_rbx = (v_rbx) & (a1);
        *(unsigned __int64 *)(a1) = v_rbx;
    }
    v_rbx = (v_rbx) - 1;
    v_rbx = (v_rbx) >> (18);
    v_rbx = (unsigned int)((v_rbx) & (0x3FFFFFF8ULL));
    v_rbx = (v_rbx) + (result);
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_00323870;
loc_003235A8:
    if (((unsigned int)((unsigned int)(a2))) < 1) goto loc_0032388C;
    a2 = 0;
    a1 = 0;
    result = MiRewritePteWithLockBit(a1, a2, v_rbx, *(unsigned __int64 *)(v_rip - 3222841));
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_00323315;
    v_rbx = (v_rbx) + (8);
    v_stack_p20 = v_rbx;
    if (((v_rbx) & (0xFFFULL)) == 0) goto loc_00323315;
    if ((*(unsigned __int8 *)(v_rip + 11576918)) != 0) {
        a2 = 1;
        a1 = 0;
        result = MiReuseUltraPageTable(a1, a2, v_rbx, *(unsigned __int64 *)(v_rip - 3222841));
    }
    v_r12 = (v_rbx) << (25);
    result = (0) << (25);
    v_r12 = (v_r12) - (result);
    v_r12 = (v_r12) >> (16);
    v_r12 = (v_r12) << (25);
    v_r12 = (v_r12) - (result);
    v_r12 = (v_r12) >> (16);
    result = MiMakeValidPte(v_rbx, *(unsigned __int64 *)(a1 + 16), (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    if (condition_is_below) goto loc_003237FE;
loc_00323648:
    *(unsigned __int64 *)(v_stack_p20) = result;
    *(unsigned __int8 *)(a1 + 25) = 1;
    *(unsigned __int64 *)(a1) = 17 + v_r12 * 1;
    if (v_r12 == 0) goto loc_00323315;
    goto loc_003232FC;
loc_0032366C:
    if ((*(unsigned __int8 *)(v_rip + 11576782)) == ((unsigned __int8)(v_r12))) goto loc_003233FE;
    if ((*(unsigned __int64 *)(a1 + 8)) == -1) goto loc_003233FE;
    a2 = 0;
    result = MiReuseUltraPageTable(a1, a2, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_003233FE;
loc_00323693:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13251615)))) & (64)) == 0) goto loc_003233A5;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    if ((unsigned __int8)(result) == 0) goto loc_003233A5;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), a2, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_003233A7;
loc_003236BB:
    result = MiGetHighestUltraLevel(v_rip + 11610398, a2, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    v_stack_p28 = result;
    result = MiReleaseSpinLockExclusive(v_rip + 11610377, 17, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    v_r13 = a3;
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) == 0) {
        v_r13 = (a3) << (12);
        v_r13 = (v_r13) + (result);
        *(unsigned __int64 *)(a1) = v_r13;
    }
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_003232F9;
    v_r14 = (result) >> (27);
    v_r14 = (unsigned int)((v_r14) & (0x1FFFF8ULL));
    v_r14 = (v_r14) + (result);
    v_rbp = (v_r13) << (25);
    v_r12 = (((unsigned int)((unsigned int)(a2))) != 1) ? 1 : 0;
    v_r12 = (v_r12) + 1;
loc_0032373E:
    result = MiMakeValidPte(v_r14, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    if (((unsigned int)((unsigned int)(a2))) < 1) goto loc_00323838;
loc_00323761:
    *(unsigned __int64 *)(v_r14) = result;
    v_r15 = (a1 + 8) + (8);
    v_r14 = (v_r14) << (25);
    v_r14 = (v_r14) - (v_rbp);
    v_r14 = (v_r14) >> (16);
    v_r12 = (v_r12) - (1);
    if (condition_is_not_equal) goto loc_0032373E;
    *(unsigned __int8 *)(v_stack_p70 + 25) = 1;
    goto loc_003232FC;
loc_0032378C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13251366)))) & (64)) == 0) goto loc_00323511;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r14, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    if ((unsigned __int8)(result) == 0) goto loc_00323511;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), *(unsigned __int64 *)(a1 + 8), (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_00323513;
loc_003237B4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12494494))) != 0) goto loc_00323427;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11610130, v_stack_p68, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_0032342E;
loc_003237D8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12494458))) != 0) goto loc_00323460;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11610094, v_stack_p68, (unsigned int)(0xB8000004ULL), *(unsigned __int64 *)(v_rip - 3222841));
    result = 0;
    goto loc_003232FC;
loc_003237FE:
    if (((0) & (32)) != 0) goto loc_00323648;
    result = (0) + ((unsigned int)(0xB8000004ULL));
    if (v_stack_p20 < result) goto loc_00323648;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p20, result, 128, *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_00323648;
loc_00323838:
    if ((((unsigned __int8)(result)) & (32)) != 0) goto loc_00323761;
    result = (v_r13) + (v_stack_p70);
    if (v_r14 < result) goto loc_00323761;
    result = MiCheckLinearProtectedPteAccessedBit(v_r14, result, 128, *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_00323761;
loc_00323866:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) & (2));
    goto loc_00323409;
loc_00323870:
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (v_r12);
    goto loc_003235A8;
loc_0032388C:
    result = MiDeleteUltraMapHierarchy(v_rbx, result, 128, *(unsigned __int64 *)(v_rip - 3222841));
    goto loc_00323315;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetUltraMapping(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    if (*(uint64_t *)(arg1) == 0) goto loc_0032331B;
    result = (uint32_t)(0x40000000ULL);
    if (((uint32_t)((uint32_t)(Arg2))) != 1) { result = (uint32_t)((uint32_t)(0x200000ULL)); }
    Arg1 = ((uint32_t)((uint32_t)(result))) << (9);
    if (Arg2 != 0) { Arg1 = result; }
    local_r15 = (Arg3) << (12);
    result = (Arg1 - 1) & (*(uint64_t *)(arg1));
    if ((local_r15 + result * 1) > Arg1) goto loc_0032355E;
    if (result == 0) goto loc_0032355E;
    if (condition_is_below) goto loc_0032355E;
    *(uint64_t *)(arg1) = local_r15 + *(uint64_t *)(arg1) * 1;
loc_003232F9:
loc_003232FC:
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(arg1);
loc_00323315:
    local_rbx = (*(uint64_t *)(arg1)) - (*(uint64_t *)(v_rip - 0x312253 + (uint32_t)(Arg2) * 8));
loc_0032331B:
    local_r12 = 0;
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) != 0) goto loc_003234A9;
    if ((*(uint32_t *)(v_rip + 0xCA39E4)) != 0) goto loc_0032352C;
loc_00323342:
    if (((*(uint8_t *)(v_rip + 0xCA37BD)) & (33)) != 0) goto loc_00323486;
loc_0032334F:
    result = 2;
    local_r14 = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)(v_cr8);
        Arg1 = v_rip + 11611256;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, Arg4);
        local_r14 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12C6A)))))) == 0x80000000ULL) goto loc_003233BA;
loc_00323384:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12C6A)))))) >= 0x80000000ULL) {
    }
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA1F0D)) & ((uint32_t)(local_r14))) == 0) goto loc_00323693;
loc_003233A5:
loc_003233A7:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12C33)))))) != 0x80000000ULL) goto loc_00323384;
loc_003233BA:
    if (local_rbx == 0) goto loc_00323866;
    local_rbx = (local_rbx) >> (27);
    local_r14 = (local_rbx) - (*(uint64_t *)(v_rip + 0xB12C0D));
    local_rbx = (uint32_t)((local_rbx) & (0x1FFFF8ULL));
    local_r14 = (local_r14) >> (30);
    local_rbx = (local_rbx) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12C33)))));
    if (*(uint64_t *)(local_rbx) != 0) goto loc_0032346E;
loc_003233F3:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (2));
    if (condition_is_equal) goto loc_0032366C;
loc_003233FE:
loc_00323409:
    if ((uint32_t)(local_rbx) == 0) goto loc_003236BB;
    *(uint64_t *)(arg1) = 0;
    if (((uint8_t)(v_cr8)) == 17) goto loc_00323453;
    if (((*(uint8_t *)(v_rip + 0xCA36E5)) & (1)) != 0) goto loc_003237B4;
loc_00323427:
    *(uint32_t *)(v_rip + 0xB12BB2) = 0;
loc_0032342E:
    result = *(uint64_t *)(v_rip + 0xB12C0B);
    if ((*(uint32_t *)(v_rip + 0xCA38EB)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
    goto loc_003232FC;
loc_00323453:
    if (((*(uint8_t *)(v_rip + 0xCA36AC)) & (1)) != 0) goto loc_003237D8;
loc_00323460:
    *(uint32_t *)(v_rip + 0xB12B79) = 0;
    result = 0;
    goto loc_003232FC;
loc_0032346E:
    Arg2 = 0;
    Arg1 = 0;
    result = MiRewritePteWithLockBit(Arg1, Arg2, local_rbx, *(uint64_t *)(v_rip - 0x312BF5));
    goto loc_003233F3;
loc_00323486:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBEA9CC))) != 0) goto loc_0032334F;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 11610945, (uint8_t)(v_cr8), local_rbx, *(uint64_t *)(v_rip - 0x312BF5));
    goto loc_003233BA;
loc_003234A9:
    if (((*(uint8_t *)(v_rip + 0xCA3656)) & (33)) != 0) goto loc_0032353D;
loc_003234B9:
    local_r14 = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 255;
        Arg1 = v_rip + 11610896;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, local_rbx, *(uint64_t *)(v_rip - 0x312BF5));
        local_r14 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12B02)))))) == 0x80000000ULL) goto loc_003233BA;
loc_003234F0:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12B02)))))) >= 0x80000000ULL) {
    }
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA1DA1)) & ((uint32_t)(local_r14))) == 0) goto loc_0032378C;
loc_00323511:
loc_00323513:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12AC7)))))) == 0x80000000ULL) goto loc_003233BA;
    goto loc_003234F0;
loc_0032352C:
    result = KiRaiseIrqlProcessIrqlFlags(17, (uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB12AC7))))), local_rbx, *(uint64_t *)(v_rip - 0x312BF5));
    goto loc_00323342;
loc_0032353D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBEA915))) != 0) goto loc_003234B9;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 11610764, 255, local_rbx, *(uint64_t *)(v_rip - 0x312BF5));
    goto loc_003233BA;
loc_0032355E:
    if (((uint32_t)((uint32_t)(Arg2))) < 1) goto loc_00323315;
    if (255 >= = (v_rip + 11610764)) {
        local_rbx = (local_rbx) - 1;
        local_rbx = (local_rbx) + (v_rip + 11610764);
        Arg1 = -(v_rip + 11610764);
        local_rbx = (local_rbx) & (Arg1);
        *(uint64_t *)(arg1) = local_rbx;
    }
    local_rbx = (local_rbx) - 1;
    local_rbx = (local_rbx) >> (18);
    local_rbx = (uint32_t)((local_rbx) & (0x3FFFFFF8ULL));
    local_rbx = (local_rbx) + (result);
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_00323870;
loc_003235A8:
    if (((uint32_t)((uint32_t)(Arg2))) < 1) goto loc_0032388C;
    Arg2 = 0;
    Arg1 = 0;
    result = MiRewritePteWithLockBit(Arg1, Arg2, local_rbx, *(uint64_t *)(v_rip - 0x312D39));
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_00323315;
    local_rbx = (local_rbx) + (8);
    v_stack_p20 = local_rbx;
    if (((local_rbx) & (0xFFFULL)) == 0) goto loc_00323315;
    if ((*(uint8_t *)(v_rip + 0xB0A656)) != 0) {
        Arg2 = 1;
        Arg1 = 0;
        result = MiReuseUltraPageTable(Arg1, Arg2, local_rbx, *(uint64_t *)(v_rip - 0x312D39));
    }
    local_r12 = (local_rbx) << (25);
    result = (0) << (25);
    local_r12 = (local_r12) - (result);
    local_r12 = (local_r12) >> (16);
    local_r12 = (local_r12) << (25);
    local_r12 = (local_r12) - (result);
    local_r12 = (local_r12) >> (16);
    result = MiMakeValidPte(local_rbx, *(uint64_t *)(arg1 + 0x10), (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    if (condition_is_below) goto loc_003237FE;
loc_00323648:
    *(uint64_t *)(v_stack_p20) = result;
    *(uint8_t *)(arg1 + 0x19) = 1;
    *(uint64_t *)(arg1) = 17 + local_r12 * 1;
    if (local_r12 == 0) goto loc_00323315;
    goto loc_003232FC;
loc_0032366C:
    if ((*(uint8_t *)(v_rip + 0xB0A5CE)) == ((uint8_t)(local_r12))) goto loc_003233FE;
    if ((*(uint64_t *)(arg1 + 0x8)) == -1) goto loc_003233FE;
    Arg2 = 0;
    result = MiReuseUltraPageTable(Arg1, Arg2, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    goto loc_003233FE;
loc_00323693:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA341F)))) & (64)) == 0) goto loc_003233A5;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    if ((uint8_t)(result) == 0) goto loc_003233A5;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), Arg2, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    goto loc_003233A7;
loc_003236BB:
    result = MiGetHighestUltraLevel(v_rip + 11610398, Arg2, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    v_stack_p28 = result;
    result = MiReleaseSpinLockExclusive(v_rip + 11610377, 17, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    local_r13 = Arg3;
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) == 0) {
        local_r13 = (Arg3) << (12);
        local_r13 = (local_r13) + (result);
        *(uint64_t *)(arg1) = local_r13;
    }
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_003232F9;
    local_r14 = (result) >> (27);
    local_r14 = (uint32_t)((local_r14) & (0x1FFFF8ULL));
    local_r14 = (local_r14) + (result);
    local_rbp = (local_r13) << (25);
    local_r12 = (((uint32_t)((uint32_t)(Arg2))) != 1) ? 1 : 0;
    local_r12 = (local_r12) + 1;
loc_0032373E:
    result = MiMakeValidPte(local_r14, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    if (((uint32_t)((uint32_t)(Arg2))) < 1) goto loc_00323838;
loc_00323761:
    *(uint64_t *)(local_r14) = result;
    local_r15 = (Arg1 + 8) + (8);
    local_r14 = (local_r14) << (25);
    local_r14 = (local_r14) - (local_rbp);
    local_r14 = (local_r14) >> (16);
    local_r12 = (local_r12) - (1);
    if (condition_is_not_equal) goto loc_0032373E;
    *(uint8_t *)(v_stack_p70 + 0x19) = 1;
    goto loc_003232FC;
loc_0032378C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA3326)))) & (64)) == 0) goto loc_00323511;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r14, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    if ((uint8_t)(result) == 0) goto loc_00323511;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), *(uint64_t *)(arg1 + 0x8), (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    goto loc_00323513;
loc_003237B4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBEA69E))) != 0) goto loc_00323427;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11610130, v_stack_p68, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    goto loc_0032342E;
loc_003237D8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBEA67A))) != 0) goto loc_00323460;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11610094, v_stack_p68, (uint32_t)(0xB8000004ULL), *(uint64_t *)(v_rip - 0x312D39));
    result = 0;
    goto loc_003232FC;
loc_003237FE:
    if (((0) & (32)) != 0) goto loc_00323648;
    result = (0) + ((uint32_t)(0xB8000004ULL));
    if (v_stack_p20 < result) goto loc_00323648;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p20, result, 128, *(uint64_t *)(v_rip - 0x312D39));
    goto loc_00323648;
loc_00323838:
    if ((((uint8_t)(result)) & (32)) != 0) goto loc_00323761;
    result = (local_r13) + (v_stack_p70);
    if (local_r14 < result) goto loc_00323761;
    result = MiCheckLinearProtectedPteAccessedBit(local_r14, result, 128, *(uint64_t *)(v_rip - 0x312D39));
    goto loc_00323761;
loc_00323866:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) & (2));
    goto loc_00323409;
loc_00323870:
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (local_r12);
    goto loc_003235A8;
loc_0032388C:
    result = MiDeleteUltraMapHierarchy(local_rbx, result, 128, *(uint64_t *)(v_rip - 0x312D39));
    goto loc_00323315;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x19` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00323270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
