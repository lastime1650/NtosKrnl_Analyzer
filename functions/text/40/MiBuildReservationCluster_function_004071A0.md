# MiBuildReservationCluster

- RVA: `0x004071A0`–`0x00407968` (길이 `1,992` bytes)
- VA: `0x00000001404071A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A940`
- 디코드: `506`개 명령, `1,992/1,992` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0040721D` → [MiRefPageFileSpaceBitmaps](MiRefPageFileSpaceBitmaps_function_00407DC4.md) (function, `0x00407DC4`)
- `0x0040725A` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x004072C5` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x0040733D` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x0040735B` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0040737B` → [MiReservePtes](../31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x0040739D` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00407476` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x00407497` → [MiGetPageForWriteCluster](MiGetPageForWriteCluster_function_00405704.md) (function, `0x00405704`)
- `0x0040755D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0040757C` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x0040759D` → [MiGetPageForWriteCluster](MiGetPageForWriteCluster_function_00405704.md) (function, `0x00405704`)
- `0x004075FF` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00407648` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x00407654` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x0040765F` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x0040766A` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x004076DE` → [MiAddToReservationCluster](MiAddToReservationCluster_function_00405474.md) (function, `0x00405474`)
- `0x004076F2` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0040770C` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00407748` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00407765` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00407770` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0040777E` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x004077B5` → [MiReferencePfBackedSection](../2B/MiReferencePfBackedSection_function_002B9B70.md) (function, `0x002B9B70`)
- `0x0040782D` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x004078A5` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x004078BB` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x004078C6` → [MiDecrementModifiedWriteCount](../29/MiDecrementModifiedWriteCount_function_00298184.md) (function, `0x00298184`)
- `0x004078D7` → [MiReleaseControlAreaWaiters](../28/MiReleaseControlAreaWaiters_function_002865F0.md) (function, `0x002865F0`)
- `0x004078FA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00407906` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0040791A` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00407945` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0040795E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x00372FF9`

### Static image references
- `0x0040727E` → RVA `0x00E2DC80` (`.data`; read)
- `0x00407374` → RVA `0x00E37668` (`.data`; read)
- `0x004073A2` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x004074B6` → RVA `0x00E37478` (`.data`; read)
- `0x00407794` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x004078EC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0040795E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0040794B` → [sub_006EC69A](../6E/Unknown_function_006EC69A.md) (`tail-transfer`)
  - `0x00407954` → [sub_006EC69A](../6E/Unknown_function_006EC69A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004071A0  48 8B C4                        mov rax, rsp
004071A3  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
004071A7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
004071AB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
004071AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
004071B3  55                              push rbp
004071B4  53                              push rbx
004071B5  56                              push rsi
004071B6  57                              push rdi
004071B7  41 54                           push r12
004071B9  41 55                           push r13
004071BB  41 56                           push r14
004071BD  41 57                           push r15
004071BF  48 8D 68 A1                     lea rbp, [rax - 0x5f]
004071C3  48 81 EC D8 00 00 00            sub rsp, 0xd8
004071CA  4C 8B AA D8 00 00 00            mov r13, qword ptr [rdx + 0xd8]
004071D1  33 C0                           xor eax, eax
004071D3  21 44 24 34                     and dword ptr [rsp + 0x34], eax
004071D7  4C 8B C2                        mov r8, rdx
004071DA  21 45 83                        and dword ptr [rbp - 0x7d], eax
004071DD  0F 57 C0                        xorps xmm0, xmm0
004071E0  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
004071E5  0F 57 C9                        xorps xmm1, xmm1
004071E8  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
004071EC  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
004071F0  0F B7 82 AC 00 00 00            movzx eax, word ptr [rdx + 0xac]
004071F7  48 8D 55 A7                     lea rdx, [rbp - 0x59]
004071FB  83 E0 0F                        and eax, 0xf
004071FE  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
00407202  48 83 C0 30                     add rax, 0x30
00407206  49 8B C8                        mov rcx, r8
00407209  4C 6B F0 58                     imul r14, rax, 0x58
0040720D  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
00407211  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
00407215  0F 11 4D CF                     movups xmmword ptr [rbp - 0x31], xmm1
00407219  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
0040721D  E8 A2 0B 00 00                  call 0x140407dc4
00407222  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00407227  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00407231  4B 8B 7C 2E 10                  mov rdi, qword ptr [r14 + r13 + 0x10]
00407236  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
00407240  48 3B F8                        cmp rdi, rax
00407243  0F 84 07 07 00 00               je 0x140407950
00407249  48 8D 34 7F                     lea rsi, [rdi + rdi*2]
0040724D  48 C1 E6 04                     shl rsi, 4
00407251  48 8B C1                        mov rax, rcx
00407254  48 8B CF                        mov rcx, rdi
00407257  48 03 F0                        add rsi, rax
0040725A  E8 C1 A3 F1 FF                  call 0x140321620
0040725F  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00407269  44 8A F8                        mov r15b, al
0040726C  3C 11                           cmp al, 0x11
0040726E  74 C1                           je 0x140407231
00407270  4B 8B 54 2E 10                  mov rdx, qword ptr [r14 + r13 + 0x10]
00407275  48 3B FA                        cmp rdi, rdx
00407278  0F 85 96 06 00 00               jne 0x140407914
0040727E  48 8B 05 FB 69 A2 00            mov rax, qword ptr [rip + 0xa269fb]
00407285  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
00407289  48 85 C0                        test rax, rax
0040728C  74 0B                           je 0x140407299
0040728E  F6 C3 10                        test bl, 0x10
00407291  75 06                           jne 0x140407299
00407293  48 F7 D0                        not rax
00407296  48 23 D8                        and rbx, rax
00407299  4C 8B 65 AF                     mov r12, qword ptr [rbp - 0x51]
0040729D  48 8B CE                        mov rcx, rsi
004072A0  48 C1 EB 20                     shr rbx, 0x20
004072A4  41 3B DC                        cmp ebx, r12d
004072A7  0F 83 95 06 00 00               jae 0x140407942
004072AD  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
004072B1  48 0F A3 18                     bt qword ptr [rax], rbx
004072B5  0F 92 C0                        setb al
004072B8  84 C0                           test al, al
004072BA  0F 85 86 04 00 00               jne 0x140407746
004072C0  BA 01 00 00 00                  mov edx, 1
004072C5  E8 E2 EA FF FF                  call 0x140405dac
004072CA  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
004072CE  41 BE 01 00 00 00               mov r14d, 1
004072D4  48 89 38                        mov qword ptr [rax], rdi
004072D7  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
004072DB  44 39 30                        cmp dword ptr [rax], r14d
004072DE  0F 84 43 05 00 00               je 0x140407827
004072E4  4C 8B 66 08                     mov r12, qword ptr [rsi + 8]
004072E8  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
004072F2  48 8B 7E 10                     mov rdi, qword ptr [rsi + 0x10]
004072F6  4C 0B E0                        or r12, rax
004072F9  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
004072FD  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00407307  48 23 C1                        and rax, rcx
0040730A  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
0040730E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00407312  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0040731C  48 C1 E1 04                     shl rcx, 4
00407320  48 8B C0                        mov rax, rax
00407323  48 03 C8                        add rcx, rax
00407326  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
0040732A  45 33 ED                        xor r13d, r13d
0040732D  F0 48 0F BA 69 18 3F            lock bts qword ptr [rcx + 0x18], 0x3f
00407334  0F 82 57 04 00 00               jb 0x140407791
0040733A  41 8B D6                        mov edx, r14d
0040733D  E8 0E 42 E8 FF                  call 0x14028b550
00407342  4C 8B 6D 97                     mov r13, qword ptr [rbp - 0x69]
00407346  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00407350  F0 49 21 45 18                  lock and qword ptr [r13 + 0x18], rax
00407355  41 8A D7                        mov dl, r15b
00407358  48 8B CE                        mov rcx, rsi
0040735B  E8 80 30 F1 FF                  call 0x14031a3e0
00407360  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00407364  48 85 C0                        test rax, rax
00407367  0F 88 45 04 00 00               js 0x1404077b2
0040736D  44 8B 7D 83                     mov r15d, dword ptr [rbp - 0x7d]
00407371  41 8B D6                        mov edx, r14d
00407374  48 8D 0D ED 02 A3 00            lea rcx, [rip + 0xa302ed]
0040737B  E8 A0 19 F1 FF                  call 0x140318d20
00407380  48 89 45 07                     mov qword ptr [rbp + 7], rax
00407384  48 8B F0                        mov rsi, rax
00407387  48 85 C0                        test rax, rax
0040738A  0F 84 85 04 00 00               je 0x140407815
00407390  48 8B 55 8F                     mov rdx, qword ptr [rbp - 0x71]
00407394  41 B8 01 00 00 20               mov r8d, 0x20000001
0040739A  48 8B C8                        mov rcx, rax
0040739D  E8 EE E1 EB FF                  call 0x1402c5590
004073A2  48 0F BA 25 DD F6 BB 00 24      bt qword ptr [rip + 0xbbf6dd], 0x24
004073AB  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
004073B5  48 8B D8                        mov rbx, rax
004073B8  0F 82 B9 04 00 00               jb 0x140407877
004073BE  48 8B D6                        mov rdx, rsi
004073C1  48 89 1E                        mov qword ptr [rsi], rbx
004073C4  48 C1 E2 19                     shl rdx, 0x19
004073C8  49 8B C5                        mov rax, r13
004073CB  48 C1 E0 19                     shl rax, 0x19
004073CF  41 B8 FF 01 00 00               mov r8d, 0x1ff
004073D5  48 2B D0                        sub rdx, rax
004073D8  49 C1 EC 03                     shr r12, 3
004073DC  48 C1 FA 10                     sar rdx, 0x10
004073E0  4D 23 E0                        and r12, r8
004073E3  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
004073E7  48 8B F2                        mov rsi, rdx
004073EA  4A 8D 14 E2                     lea rdx, [rdx + r12*8]
004073EE  48 89 55 8F                     mov qword ptr [rbp - 0x71], rdx
004073F2  45 85 FF                        test r15d, r15d
004073F5  0F 85 4E 04 00 00               jne 0x140407849
004073FB  48 81 C6 F8 0F 00 00            add rsi, 0xff8
00407402  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00407406  48 81 E7 1F FC 00 FC            and rdi, 0xfffffffffc00fc1f
0040740D  48 2B F2                        sub rsi, rdx
00407410  48 89 7D FF                     mov qword ptr [rbp - 1], rdi
00407414  48 C1 FE 03                     sar rsi, 3
00407418  48 8B DF                        mov rbx, rdi
0040741B  4C 8B EF                        mov r13, rdi
0040741E  8B 00                           mov eax, dword ptr [rax]
00407420  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00407423  FF C8                           dec eax
00407425  3B F0                           cmp esi, eax
00407427  0F 43 F0                        cmovae esi, eax
0040742A  48 8B 05 4F 68 A2 00            mov rax, qword ptr [rip + 0xa2684f]
00407431  48 85 C0                        test rax, rax
00407434  74 0E                           je 0x140407444
00407436  F6 C3 10                        test bl, 0x10
00407439  75 09                           jne 0x140407444
0040743B  4C 8B E8                        mov r13, rax
0040743E  49 F7 D5                        not r13
00407441  4C 23 EB                        and r13, rbx
00407444  4C 8B 65 AF                     mov r12, qword ptr [rbp - 0x51]
00407448  49 C1 ED 20                     shr r13, 0x20
0040744C  8B CE                           mov ecx, esi
0040744E  49 03 CD                        add rcx, r13
00407451  41 8B C4                        mov eax, r12d
00407454  48 3B C8                        cmp rcx, rax
00407457  0F 83 D0 04 00 00               jae 0x14040792d
0040745D  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00407462  48 8B FA                        mov rdi, rdx
00407465  85 F6                           test esi, esi
00407467  74 66                           je 0x1404074cf
00407469  49 FF C5                        inc r13
0040746C  48 8B CB                        mov rcx, rbx
0040746F  49 8B D5                        mov rdx, r13
00407472  48 83 C7 08                     add rdi, 8
00407476  E8 C5 63 F6 FF                  call 0x14036d840
0040747B  48 8B D8                        mov rbx, rax
0040747E  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00407483  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00407488  4C 8B C3                        mov r8, rbx
0040748B  48 8B D7                        mov rdx, rdi
0040748E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00407493  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00407497  E8 68 E2 FF FF                  call 0x140405704
0040749C  48 83 F8 FF                     cmp rax, -1
004074A0  74 2D                           je 0x1404074cf
004074A2  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
004074A6  FF CE                           dec esi
004074A8  48 83 C1 08                     add rcx, 8
004074AC  41 FF C6                        inc r14d
004074AF  48 89 4D 67                     mov qword ptr [rbp + 0x67], rcx
004074B3  48 89 01                        mov qword ptr [rcx], rax
004074B6  48 3B 05 BB FF A2 00            cmp rax, qword ptr [rip + 0xa2ffbb]
004074BD  75 03                           jne 0x1404074c2
004074BF  41 FF C7                        inc r15d
004074C2  83 7C 24 38 03                  cmp dword ptr [rsp + 0x38], 3
004074C7  75 9C                           jne 0x140407465
004074C9  41 83 FE 10                     cmp r14d, 0x10
004074CD  72 96                           jb 0x140407465
004074CF  44 2B 74 24 34                  sub r14d, dword ptr [rsp + 0x34]
004074D4  44 2B 7C 24 34                  sub r15d, dword ptr [rsp + 0x34]
004074D9  8B 75 9F                        mov esi, dword ptr [rbp - 0x61]
004074DC  48 8B 55 8F                     mov rdx, qword ptr [rbp - 0x71]
004074E0  41 2B F6                        sub esi, r14d
004074E3  83 7D 83 00                     cmp dword ptr [rbp - 0x7d], 0
004074E7  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
004074EC  0F 85 6B 03 00 00               jne 0x14040785d
004074F2  48 8B CA                        mov rcx, rdx
004074F5  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
004074FC  48 8B 7D FF                     mov rdi, qword ptr [rbp - 1]
00407500  48 8B C2                        mov rax, rdx
00407503  48 2B C1                        sub rax, rcx
00407506  48 8B DF                        mov rbx, rdi
00407509  48 C1 F8 03                     sar rax, 3
0040750D  3B C6                           cmp eax, esi
0040750F  0F 42 F0                        cmovb esi, eax
00407512  48 8B 05 67 67 A2 00            mov rax, qword ptr [rip + 0xa26767]
00407519  48 85 C0                        test rax, rax
0040751C  74 0F                           je 0x14040752d
0040751E  40 F6 C7 10                     test dil, 0x10
00407522  75 09                           jne 0x14040752d
00407524  48 8B D8                        mov rbx, rax
00407527  48 F7 D3                        not rbx
0040752A  48 23 DF                        and rbx, rdi
0040752D  48 C1 EB 20                     shr rbx, 0x20
00407531  8B C6                           mov eax, esi
00407533  48 8D 4B FF                     lea rcx, [rbx - 1]
00407537  48 3B C1                        cmp rax, rcx
0040753A  0F 87 FA 03 00 00               ja 0x14040793a
00407540  85 F6                           test esi, esi
00407542  0F 84 F8 02 00 00               je 0x140407840
00407548  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0040754C  48 8B D1                        mov rdx, rcx
0040754F  45 8B C6                        mov r8d, r14d
00407552  49 C1 E0 03                     shl r8, 3
00407556  4C 8D 2C F1                     lea r13, [rcx + rsi*8]
0040755A  49 8B CD                        mov rcx, r13
0040755D  E8 DE F2 2B 00                  call 0x1406c6840
00407562  83 64 24 34 00                  and dword ptr [rsp + 0x34], 0
00407567  4C 8B 65 8F                     mov r12, qword ptr [rbp - 0x71]
0040756B  85 F6                           test esi, esi
0040756D  74 5F                           je 0x1404075ce
0040756F  48 FF CB                        dec rbx
00407572  48 8B CF                        mov rcx, rdi
00407575  48 8B D3                        mov rdx, rbx
00407578  49 83 EC 08                     sub r12, 8
0040757C  E8 BF 62 F6 FF                  call 0x14036d840
00407581  48 8B F8                        mov rdi, rax
00407584  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00407589  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0040758E  4C 8B C7                        mov r8, rdi
00407591  49 8B D4                        mov rdx, r12
00407594  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00407599  48 8D 4D AF                     lea rcx, [rbp - 0x51]
0040759D  E8 62 E1 FF FF                  call 0x140405704
004075A2  48 83 F8 FF                     cmp rax, -1
004075A6  74 26                           je 0x1404075ce
004075A8  49 83 ED 08                     sub r13, 8
004075AC  FF CE                           dec esi
004075AE  41 FF C6                        inc r14d
004075B1  49 89 45 00                     mov qword ptr [r13], rax
004075B5  48 3B 05 BC FE A2 00            cmp rax, qword ptr [rip + 0xa2febc]
004075BC  75 03                           jne 0x1404075c1
004075BE  41 FF C7                        inc r15d
004075C1  83 7C 24 38 03                  cmp dword ptr [rsp + 0x38], 3
004075C6  75 A3                           jne 0x14040756b
004075C8  41 83 FE 10                     cmp r14d, 0x10
004075CC  72 9D                           jb 0x14040756b
004075CE  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
004075D2  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
004075D6  44 2B F9                        sub r15d, ecx
004075D9  4C 8B 65 AF                     mov r12, qword ptr [rbp - 0x51]
004075DD  44 2B F1                        sub r14d, ecx
004075E0  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
004075E5  48 8D 14 CD 00 00 00 00         lea rdx, [rcx*8]
004075ED  49 03 D5                        add rdx, r13
004075F0  48 3B F2                        cmp rsi, rdx
004075F3  74 0F                           je 0x140407604
004075F5  45 8B C6                        mov r8d, r14d
004075F8  48 8B CE                        mov rcx, rsi
004075FB  49 C1 E0 03                     shl r8, 3
004075FF  E8 3C F2 2B 00                  call 0x1406c6840
00407604  48 8B 06                        mov rax, qword ptr [rsi]
00407607  48 8D 1C 40                     lea rbx, [rax + rax*2]
0040760B  48 03 DB                        add rbx, rbx
0040760E  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
00407618  48 8B 1C D8                     mov rbx, qword ptr [rax + rbx*8]
0040761C  48 8B 05 5D 66 A2 00            mov rax, qword ptr [rip + 0xa2665d]
00407623  48 85 C0                        test rax, rax
00407626  74 0B                           je 0x140407633
00407628  F6 C3 10                        test bl, 0x10
0040762B  75 06                           jne 0x140407633
0040762D  48 F7 D0                        not rax
00407630  48 23 D8                        and rbx, rax
00407633  48 8B 55 07                     mov rdx, qword ptr [rbp + 7]
00407637  48 8D 0D 2A 00 A3 00            lea rcx, [rip + 0xa3002a]
0040763E  48 C1 EB 20                     shr rbx, 0x20
00407642  41 B8 01 00 00 00               mov r8d, 1
00407648  E8 F3 FB E3 FF                  call 0x140247240
0040764D  4C 8B 6D 97                     mov r13, qword ptr [rbp - 0x69]
00407651  49 8B CD                        mov rcx, r13
00407654  E8 E7 2C F1 FF                  call 0x14031a340
00407659  49 8B CD                        mov rcx, r13
0040765C  40 8A F8                        mov dil, al
0040765F  E8 6C E3 E3 FF                  call 0x1402459d0
00407664  40 8A D7                        mov dl, dil
00407667  49 8B CD                        mov rcx, r13
0040766A  E8 71 2D F1 FF                  call 0x14031a3e0
0040766F  83 7D 83 00                     cmp dword ptr [rbp - 0x7d], 0
00407673  0F 85 36 02 00 00               jne 0x1404078af
00407679  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0040767D  8B 08                           mov ecx, dword ptr [rax]
0040767F  44 3B F1                        cmp r14d, ecx
00407682  0F 83 00 01 00 00               jae 0x140407788
00407688  45 85 F6                        test r14d, r14d
0040768B  0F 84 F7 00 00 00               je 0x140407788
00407691  8B D3                           mov edx, ebx
00407693  45 8B CE                        mov r9d, r14d
00407696  45 8B C4                        mov r8d, r12d
00407699  4A 8D 04 0A                     lea rax, [rdx + r9]
0040769D  49 3B C0                        cmp rax, r8
004076A0  0F 83 E2 00 00 00               jae 0x140407788
004076A6  48 8D 04 0A                     lea rax, [rdx + rcx]
004076AA  49 3B C0                        cmp rax, r8
004076AD  0F 87 2E 02 00 00               ja 0x1404078e1
004076B3  41 2B CE                        sub ecx, r14d
004076B6  44 8B E1                        mov r12d, ecx
004076B9  4A 8D 04 CE                     lea rax, [rsi + r9*8]
004076BD  45 8B C4                        mov r8d, r12d
004076C0  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
004076C4  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
004076C9  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
004076CE  46 8D 0C 33                     lea r9d, [rbx + r14]
004076D2  48 8B CE                        mov rcx, rsi
004076D5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004076DA  48 8D 55 AF                     lea rdx, [rbp - 0x51]
004076DE  E8 91 DD FF FF                  call 0x140405474
004076E3  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
004076E8  44 03 F0                        add r14d, eax
004076EB  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
004076F2  E8 99 0F E4 FF                  call 0x140248690
004076F7  4C 8B 65 A7                     mov r12, qword ptr [rbp - 0x59]
004076FB  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
00407702  8A D0                           mov dl, al
00407704  41 FF 0C 24                     dec dword ptr [r12]
00407708  41 8B 3C 24                     mov edi, dword ptr [r12]
0040770C  E8 AF 0B E4 FF                  call 0x1402482c0
00407711  85 FF                           test edi, edi
00407713  75 09                           jne 0x14040771e
00407715  4D 85 E4                        test r12, r12
00407718  0F 85 3B 02 00 00               jne 0x140407959
0040771E  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00407722  44 89 30                        mov dword ptr [rax], r14d
00407725  45 2B F7                        sub r14d, r15d
00407728  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0040772C  44 89 30                        mov dword ptr [rax], r14d
0040772F  8B C3                           mov eax, ebx
00407731  48 81 C4 D8 00 00 00            add rsp, 0xd8
00407738  41 5F                           pop r15
0040773A  41 5E                           pop r14
0040773C  41 5D                           pop r13
0040773E  41 5C                           pop r12
00407740  5F                              pop rdi
00407741  5E                              pop rsi
00407742  5B                              pop rbx
00407743  5D                              pop rbp
00407744  C3                              ret
00407745  CC                              int3
00407746  33 D2                           xor edx, edx
00407748  E8 43 FE E7 FF                  call 0x140287590
0040774D  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00407751  BA 08 00 00 00                  mov edx, 8
00407756  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
0040775A  48 83 E0 FD                     and rax, 0xfffffffffffffffd
0040775E  48 8B CE                        mov rcx, rsi
00407761  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00407765  E8 96 28 EB FF                  call 0x1402ba000
0040776A  41 8A D7                        mov dl, r15b
0040776D  48 8B CE                        mov rcx, rsi
00407770  E8 6B 2C F1 FF                  call 0x14031a3e0
00407775  45 33 C0                        xor r8d, r8d
00407778  48 8B D3                        mov rdx, rbx
0040777B  49 8B CD                        mov rcx, r13
0040777E  E8 4D C8 E7 FF                  call 0x140283fd0
00407783  E9 9F FA FF FF                  jmp 0x140407227
00407788  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
0040778C  E9 5A FF FF FF                  jmp 0x1404076eb
00407791  41 FF C5                        inc r13d
00407794  44 85 2D 11 DB BB 00            test dword ptr [rip + 0xbbdb11], r13d
0040779B  0F 84 4B 01 00 00               je 0x1404078ec
004077A1  F3 90                           pause
004077A3  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
004077A7  48 85 C0                        test rax, rax
004077AA  0F 89 7D FB FF FF               jns 0x14040732d
004077B0  EB DF                           jmp 0x140407791
004077B2  49 8B CC                        mov rcx, r12
004077B5  E8 B6 23 EB FF                  call 0x1402b9b70
004077BA  48 85 C0                        test rax, rax
004077BD  74 56                           je 0x140407815
004077BF  48 8B 08                        mov rcx, qword ptr [rax]
004077C2  49 8B D4                        mov rdx, r12
004077C5  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
004077CC  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
004077D0  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
004077D4  45 8B FE                        mov r15d, r14d
004077D7  8B 40 2C                        mov eax, dword ptr [rax + 0x2c]
004077DA  48 3B D1                        cmp rdx, rcx
004077DD  44 89 75 83                     mov dword ptr [rbp - 0x7d], r14d
004077E1  4C 8D 82 F8 0F 00 00            lea r8, [rdx + 0xff8]
004077E8  48 0F 42 D1                     cmovb rdx, rcx
004077EC  FF C8                           dec eax
004077EE  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
004077F2  48 8D 0C C1                     lea rcx, [rcx + rax*8]
004077F6  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
004077FA  4C 3B C1                        cmp r8, rcx
004077FD  4C 0F 47 C1                     cmova r8, rcx
00407801  48 83 65 D7 00                  and qword ptr [rbp - 0x29], 0
00407806  48 0F BA E0 3E                  bt rax, 0x3e
0040780B  4C 89 45 E7                     mov qword ptr [rbp - 0x19], r8
0040780F  0F 83 5C FB FF FF               jae 0x140407371
00407815  4C 8B 65 AF                     mov r12, qword ptr [rbp - 0x51]
00407819  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
0040781E  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
00407822  E9 2A FE FF FF                  jmp 0x140407651
00407827  41 8A D7                        mov dl, r15b
0040782A  48 8B CE                        mov rcx, rsi
0040782D  E8 AE 2B F1 FF                  call 0x14031a3e0
00407832  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00407837  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
0040783B  E9 39 FE FF FF                  jmp 0x140407679
00407840  48 8B 75 87                     mov rsi, qword ptr [rbp - 0x79]
00407844  E9 BB FD FF FF                  jmp 0x140407604
00407849  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0040784D  48 C1 E8 03                     shr rax, 3
00407851  49 23 C0                        and rax, r8
00407854  48 8D 34 C6                     lea rsi, [rsi + rax*8]
00407858  E9 A5 FB FF FF                  jmp 0x140407402
0040785D  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00407861  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00407865  48 C1 E8 03                     shr rax, 3
00407869  25 FF 01 00 00                  and eax, 0x1ff
0040786E  48 8D 0C C1                     lea rcx, [rcx + rax*8]
00407872  E9 85 FC FF FF                  jmp 0x1404074fc
00407877  F6 C3 20                        test bl, 0x20
0040787A  0F 85 3E FB FF FF               jne 0x1404073be
00407880  49 8B C5                        mov rax, r13
00407883  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
0040788D  48 03 C1                        add rax, rcx
00407890  48 3B F0                        cmp rsi, rax
00407893  0F 82 25 FB FF FF               jb 0x1404073be
00407899  41 B8 80 00 00 00               mov r8d, 0x80
0040789F  48 8B D3                        mov rdx, rbx
004078A2  48 8B CE                        mov rcx, rsi
004078A5  E8 D6 B4 E8 FF                  call 0x140292d80
004078AA  E9 0F FB FF FF                  jmp 0x1404073be
004078AF  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
004078B3  48 85 C9                        test rcx, rcx
004078B6  74 08                           je 0x1404078c0
004078B8  8A 55 EF                        mov dl, byte ptr [rbp - 0x11]
004078BB  E8 D0 E7 E3 FF                  call 0x140246090
004078C0  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
004078C4  33 D2                           xor edx, edx
004078C6  E8 B9 08 E9 FF                  call 0x140298184
004078CB  48 85 C0                        test rax, rax
004078CE  0F 84 A5 FD FF FF               je 0x140407679
004078D4  48 8B C8                        mov rcx, rax
004078D7  E8 14 ED E7 FF                  call 0x1402865f0
004078DC  E9 98 FD FF FF                  jmp 0x140407679
004078E1  44 2B E3                        sub r12d, ebx
004078E4  45 2B E6                        sub r12d, r14d
004078E7  E9 CD FD FF FF                  jmp 0x1404076b9
004078EC  8B 05 C6 F1 BB 00               mov eax, dword ptr [rip + 0xbbf1c6]
004078F2  A8 40                           test al, 0x40
004078F4  0F 84 A7 FE FF FF               je 0x1404077a1
004078FA  E8 91 7B F0 FF                  call 0x14030f490
004078FF  84 C0                           test al, al
00407901  74 21                           je 0x140407924
00407903  41 8B CD                        mov ecx, r13d
00407906  E8 55 7B F0 FF                  call 0x14030f460
0040790B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0040790F  E9 8F FE FF FF                  jmp 0x1404077a3
00407914  41 8A D7                        mov dl, r15b
00407917  48 8B CE                        mov rcx, rsi
0040791A  E8 C1 2A F1 FF                  call 0x14031a3e0
0040791F  E9 03 F9 FF FF                  jmp 0x140407227
00407924  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00407928  E9 74 FE FF FF                  jmp 0x1404077a1
0040792D  41 8B F4                        mov esi, r12d
00407930  41 2B F5                        sub esi, r13d
00407933  FF CE                           dec esi
00407935  E9 23 FB FF FF                  jmp 0x14040745d
0040793A  8D 73 FF                        lea esi, [rbx - 1]
0040793D  E9 FE FB FF FF                  jmp 0x140407540
00407942  41 8A D7                        mov dl, r15b
00407945  E8 96 2A F1 FF                  call 0x14031a3e0
0040794A  90                              nop
0040794B  E9 4A 4D 2E 00                  jmp 0x1406ec69a
00407950  4C 8B 65 AF                     mov r12, qword ptr [rbp - 0x51]
00407954  E9 41 4D 2E 00                  jmp 0x1406ec69a
00407959  33 D2                           xor edx, edx
0040795B  49 8B CC                        mov rcx, r12
0040795E  E8 0D AF 77 00                  call 0x140b82870
00407963  E9 B6 FD FF FF                  jmp 0x14040771e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBuildReservationCluster(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p30;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (216);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 0;
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 172)) & (15));
    *(unsigned __int64 *)(v_rsp - 95 - 121) = a1;
    result = (result) + (48);
    v_r14 = (v_r14) * (result);
    *(unsigned __int64 *)(v_rsp - 95 - 89) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_xmm1;
    result = MiRefPageFileSpaceBitmaps(a2, v_rsp - 95 - 89, a2, a4);
loc_00407227:
loc_00407231:
    if ((*(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16)) == result) goto loc_00407950;
    v_rsi = (*(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16) + *(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16) * 2) << (4);
    v_rsi = (v_rsi) + (a2);
    result = MiSafeLockPage(*(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16), v_rsp - 95 - 89, a2, a4);
    if (((unsigned __int8)(result)) == 17) goto loc_00407231;
    if ((*(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16)) != (*(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16))) goto loc_00407914;
    if (*(unsigned __int64 *)(v_rip + 10643963) == 0) goto loc_00407299;
    result = *(unsigned __int64 *)(v_rip + 10643963);
    v_rbx = *(unsigned __int64 *)(v_rsi + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10643963));
        v_rbx = (*(unsigned __int64 *)(v_rsi + 16)) & (result);
    }
    v_rbx = (v_rbx) >> (32);
    if (((unsigned int)(v_rbx)) >= ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 81)))) goto loc_00407942;
    result = (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 81)))) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00407746;
    result = MiReferencePageForModifiedWrite(v_rsi, 1, a2, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103)) = *(unsigned __int64 *)(v_r14 + *(unsigned __int64 *)(a2 + 216) * 1 + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119))) == 1) goto loc_00407827;
    v_r12 = (*(unsigned __int64 *)(v_rsi + 8)) | (*(unsigned __int64 *)(v_rsp - 95 + 119));
    result = (*(unsigned __int64 *)(v_rsi + 40)) & (v_rsi);
    *(unsigned __int64 *)(v_rsp - 95 - 113) = result;
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    *(unsigned __int64 *)(v_rsp - 95 - 105) = a1;
    v_r13 = 0;
loc_0040732D:
    if (condition_is_below) goto loc_00407791;
    result = MiAddLockedPageCharge(a1, 1, a2, a4);
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), a2, a4);
    if (sign_flag) goto loc_004077B2;
loc_00407371:
    result = MiReservePtes(v_rip + 10683117, 1, a2, a4);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
    if (result == 0) goto loc_00407815;
    result = MiMakeValidPte(result, *(unsigned __int64 *)(v_rsp - 95 - 113), (unsigned int)(0x20000001ULL), a4);
    if (condition_is_below) goto loc_00407877;
loc_004073BE:
    *(unsigned __int64 *)(result) = result;
    a2 = (result) << (25);
    result = (*(unsigned __int64 *)(v_rsp - 95 - 105)) << (25);
    a2 = (a2) - (result);
    v_r12 = (v_r12) >> (3);
    a2 = (a2) >> (16);
    v_r12 = (v_r12) & (511);
    *(unsigned __int64 *)(v_rsp - 95 - 9) = a2;
    *(unsigned __int64 *)(v_rsp - 95 - 113) = a2 + v_r12 * 8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 125))) != 0) goto loc_00407849;
    v_rsi = (a2) + (0xFF8ULL);
loc_00407402:
    v_rdi = (*(unsigned __int64 *)(v_rsi + 16)) & (0xFFFFFFFFFC00FC1FULL);
    v_rsi = (v_rsi) - (a2 + v_r12 * 8);
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_rdi;
    v_rsi = (v_rsi) >> (3);
    *(unsigned int *)(v_rsp - 95 - 97) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)))) - 1);
    if (((unsigned int)(v_rsi)) >= ((unsigned int)(result))) { v_rsi = (unsigned int)(result); }
    if (*(unsigned __int64 *)(v_rip + 10643535) == 0) goto loc_00407444;
    v_r13 = v_rdi;
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) {
        v_r13 = *(unsigned __int64 *)(v_rip + 10643535);
        v_r13 = ~(v_r13);
        v_r13 = (v_r13) & (v_rdi);
    }
    v_r13 = (v_r13) >> (32);
    a1 = ((unsigned int)((unsigned int)(v_rsi))) + (v_r13);
    if (a1 >= ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 81))))) goto loc_0040792D;
loc_0040745D:
loc_00407465:
    if ((unsigned int)(v_rsi) == 0) goto loc_004074CF;
    v_r13 = (v_r13) + 1;
    v_rdi = (a2 + v_r12 * 8) + (8);
    result = MiUpdatePageFileHighInPte(v_rdi, v_r13, 511, a4);
    v_stack_mF8 = v_stack_mE0;
    result = MiGetPageForWriteCluster(v_rsp - 95 - 81, v_rdi, result, v_stack_mE4);
    if (result == -1) goto loc_004074CF;
    v_rsi = (unsigned int)((v_rsi) - 1);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 103)) + (8);
    v_r14 = (unsigned int)((1) + 1);
    *(unsigned __int64 *)(v_rsp - 95 + 103) = a1;
    *(unsigned __int64 *)(a1) = result;
    v_r15 = (unsigned int)(v_stack_mE8);
    if (result == (*(unsigned __int64 *)(v_rip + 10682299))) {
        v_r15 = (unsigned int)(((unsigned int)(v_stack_mE8)) + 1);
    }
    if (v_stack_mE0 != 3) goto loc_00407465;
    if (((unsigned int)(v_r14)) < 16) goto loc_00407465;
loc_004074CF:
    v_r14 = (unsigned int)((v_r14) - (v_stack_mE4));
    v_r15 = (unsigned int)((v_r15) - (v_stack_mE4));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 97))) - ((unsigned int)(v_r14)));
    v_stack_mE8 = (unsigned int)(v_r15);
    if ((*(unsigned int *)(v_rsp - 95 - 125)) != 0) goto loc_0040785D;
    a1 = (*(unsigned __int64 *)(v_rsp - 95 - 113)) & (0xFFFFFFFFFFFFF000ULL);
loc_004074FC:
    result = (*(unsigned __int64 *)(v_rsp - 95 - 113)) - (a1);
    result = (result) >> (3);
    if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) { v_rsi = (unsigned int)(result); }
    if (*(unsigned __int64 *)(v_rip + 10643303) == 0) goto loc_0040752D;
    v_rbx = *(unsigned __int64 *)(v_rsp - 95 - 1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 - 1))) & (16)) == 0) {
        v_rbx = *(unsigned __int64 *)(v_rip + 10643303);
        v_rbx = ~(v_rbx);
        v_rbx = (v_rbx) & (*(unsigned __int64 *)(v_rsp - 95 - 1));
    }
    v_rbx = (v_rbx) >> (32);
    if (((unsigned int)((unsigned int)(v_rsi))) > (v_rbx - 1)) goto loc_0040793A;
loc_00407540:
    if ((unsigned int)(v_rsi) == 0) goto loc_00407840;
    a3 = ((unsigned int)((unsigned int)(v_r14))) << (3);
    result = memcpy(*(unsigned __int64 *)(v_rsp - 95 - 121) + v_rsi * 8, *(unsigned __int64 *)(v_rsp - 95 - 121), a3, v_stack_mE4);
loc_0040756B:
    if ((unsigned int)(v_rsi) == 0) goto loc_004075CE;
    v_rbx = (v_rbx) - 1;
    v_r12 = (*(unsigned __int64 *)(v_rsp - 95 - 113)) - (8);
    result = MiUpdatePageFileHighInPte(*(unsigned __int64 *)(v_rsp - 95 - 1), v_rbx, a3, v_stack_mE4);
    v_stack_mF8 = v_stack_mE0;
    result = MiGetPageForWriteCluster(v_rsp - 95 - 81, v_r12, result, v_stack_mE4);
    if (result == -1) goto loc_004075CE;
    v_r13 = (*(unsigned __int64 *)(v_rsp - 95 - 121) + v_rsi * 8) - (8);
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_r14 = (unsigned int)((v_r14) + 1);
    *(unsigned __int64 *)(v_r13) = result;
    if (result == (*(unsigned __int64 *)(v_rip + 10682044))) {
        v_r15 = (unsigned int)((v_r15) + 1);
    }
    if (v_stack_mE0 != 3) goto loc_0040756B;
    if (((unsigned int)(v_r14)) < 16) goto loc_0040756B;
loc_004075CE:
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)((unsigned int)(v_stack_mE4))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)(v_stack_mE4))));
    v_stack_mE8 = (unsigned int)(v_r15);
    a2 = ((unsigned int)(v_stack_mE4) * 8) + (v_r13);
    if ((*(unsigned __int64 *)(v_rsp - 95 - 121)) != a2) {
        a3 = (unsigned int)(v_r14);
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 121);
        a3 = (a3) << (3);
        result = memcpy(a1, a2, a3, v_stack_mE4);
    }
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) * 2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) * 2);
    if (*(unsigned __int64 *)(v_rip + 10643037) == 0) goto loc_00407633;
    result = *(unsigned __int64 *)(v_rip + 10643037);
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) + v_rbx * 8);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) + v_rbx * 8))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10643037));
        v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 121)) + v_rbx * 8)) & (result);
    }
    v_rbx = (v_rbx) >> (32);
    result = MiReleasePtes(v_rip + 10682410, *(unsigned __int64 *)(v_rsp - 95 + 7), 1, v_stack_mE4);
loc_00407651:
    result = MiLockPageInline(*(unsigned __int64 *)(v_rsp - 95 - 105), *(unsigned __int64 *)(v_rsp - 95 + 7), 1, v_stack_mE4);
    result = MiRemoveLockedPageChargeAndDecRef(*(unsigned __int64 *)(v_rsp - 95 - 105), *(unsigned __int64 *)(v_rsp - 95 + 7), 1, v_stack_mE4);
    result = MiUnlockPage(*(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned __int8)((unsigned __int8)(result)), 1, v_stack_mE4);
    if ((*(unsigned int *)(v_rsp - 95 - 125)) != 0) goto loc_004078AF;
loc_00407679:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)))))) goto loc_00407788;
    if ((unsigned int)(v_r14) == 0) goto loc_00407788;
    if (((unsigned int)((unsigned int)(v_rbx)) + (unsigned int)((unsigned int)(v_r14)) * 1) >= ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 81))))) goto loc_00407788;
    if (((unsigned int)((unsigned int)(v_rbx)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119))) * 1) > ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 - 81))))) goto loc_004078E1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)))) - ((unsigned int)(v_r14)));
loc_004076B9:
    v_stack_mF0 = v_stack_mE8;
    v_stack_mF8 = *(unsigned __int64 *)(v_rsp - 95 - 121) + (unsigned int)((unsigned int)(v_r14)) * 8;
    result = MiAddToReservationCluster(*(unsigned __int64 *)(v_rsp - 95 + 111), v_rsp - 95 - 81, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
loc_004076EB:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(v_rsp - 95 + 111) + 200, v_rsp - 95 - 81, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(v_rsp - 95 + 111) + 200, (unsigned __int8)(result), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 89)))) != 0) goto loc_0040771E;
    if (*(unsigned __int64 *)(v_rsp - 95 - 89) != 0) goto loc_00407959;
loc_0040771E:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)) = (unsigned int)(v_r14);
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)(v_stack_mE8))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 127)) = (unsigned int)(v_r14);
    v_rsp = (v_rsp) + (216);
    return (unsigned int)((unsigned int)(v_rbx));
loc_00407746:
    a2 = 0;
    result = MiUnlinkPageFromListEx(*(unsigned __int64 *)(v_rsp - 95 + 111) + 200, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16)) & (-3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16) = result;
    result = MiInsertPageInList(*(unsigned __int64 *)(v_rsp - 95 + 111), 8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    result = MiUnlockPage(*(unsigned __int64 *)(v_rsp - 95 + 111), (unsigned __int8)((unsigned int)(v_stack_mE8)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))), v_rbx + v_r14 * 1);
    a3 = 0;
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(v_rsp - 95 - 105), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16), a3, v_rbx + v_r14 * 1);
    goto loc_00407227;
loc_00407788:
    goto loc_004076EB;
loc_00407791:
    v_r13 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 105)) + 1);
    if (((*(unsigned int *)(v_rip + 12311313)) & ((unsigned int)(v_r13))) == 0) goto loc_004078EC;
loc_004077A1:
loc_004077A3:
    if (!sign_flag) goto loc_0040732D;
    goto loc_00407791;
loc_004077B2:
    result = MiReferencePfBackedSection(*(unsigned __int64 *)(v_rsp - 95 - 89), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16), a3, v_rbx + v_r14 * 1);
    if (result == 0) goto loc_00407815;
    a2 = (*(unsigned __int64 *)(v_rsp - 95 - 89)) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(v_rsp - 95 - 49) = *(unsigned __int64 *)(result);
    *(unsigned int *)(v_rsp - 95 - 125) = (unsigned int)(v_r14);
    if (a2 < (*(unsigned __int64 *)(result + 8))) { a2 = *(unsigned __int64 *)(result + 8); }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 44))) - 1);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = a2;
    a3 = a2 + 4088;
    if ((a2 + 4088) > (*(unsigned __int64 *)(result + 8) + result * 8)) { a3 = *(unsigned __int64 *)(result + 8) + result * 8; }
    *(unsigned __int64 *)(v_rsp - 95 - 25) = a3;
    if ((a2 + 4088) >= (*(unsigned __int64 *)(result + 8) + result * 8)) goto loc_00407371;
loc_00407815:
    goto loc_00407651;
loc_00407827:
    result = MiUnlockPage(*(unsigned __int64 *)(v_rsp - 95 - 121), (unsigned __int8)((unsigned int)(v_stack_p30)), a3, v_rbx + v_r14 * 1);
    goto loc_00407679;
loc_00407840:
    goto loc_00407604;
loc_00407849:
    result = (*(unsigned __int64 *)(v_rsp - 95 - 25)) >> (3);
    result = (result) & (a3);
    goto loc_00407402;
loc_0040785D:
    result = (*(unsigned __int64 *)(v_rsp - 95 - 33)) >> (3);
    result = (unsigned int)((result) & (511));
    goto loc_004074FC;
loc_00407877:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16))) & (32)) != 0) goto loc_004073BE;
    result = (v_r13) + (*(unsigned __int64 *)(v_rsp - 95 - 9) + result * 8);
    if ((*(unsigned __int64 *)(v_rsp - 95 - 121) + result * 8) < result) goto loc_004073BE;
    result = MiCheckLinearProtectedPteAccessedBit(*(unsigned __int64 *)(v_rsp - 95 - 121) + result * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16), 128, v_rbx + v_r14 * 1);
    goto loc_004073BE;
loc_004078AF:
    if (*(unsigned __int64 *)(v_rsp - 95 - 41) != 0) {
        a2 = *(unsigned __int8 *)(v_rsp - 95 - 17);
        result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(v_rsp - 95 - 41), a2, 128, v_rbx + v_r14 * 1);
    }
    a2 = 0;
    result = MiDecrementModifiedWriteCount(*(unsigned __int64 *)(v_rsp - 95 - 49), a2, 128, v_rbx + v_r14 * 1);
    if (result == 0) goto loc_00407679;
    result = MiReleaseControlAreaWaiters(result, a2, 128, v_rbx + v_r14 * 1);
    goto loc_00407679;
loc_004078E1:
    v_r12 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 95 - 81)) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 16))));
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(v_r14)));
    goto loc_004076B9;
loc_004078EC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12317126)))) & (64)) == 0) goto loc_004077A1;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, a2, 128, v_rbx + v_r14 * 1);
    if ((unsigned __int8)(result) == 0) goto loc_00407924;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), a2, 128, v_rbx + v_r14 * 1);
    goto loc_004077A3;
loc_00407914:
    result = MiUnlockPage(*(unsigned __int64 *)(v_rsp - 95 - 121) + result * 8, (unsigned __int8)((unsigned int)(v_stack_p30)), 128, v_rbx + v_r14 * 1);
    goto loc_00407227;
loc_00407924:
    goto loc_004077A1;
loc_0040792D:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(v_r13)));
    v_rsi = (unsigned int)((v_rsi) - 1);
    goto loc_0040745D;
loc_0040793A:
    goto loc_00407540;
loc_00407942:
    result = MiUnlockPage(*(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned __int8)((unsigned int)(v_stack_p30)), 128, v_rbx + v_r14 * 1);
loc_00407950:
loc_00407959:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 95 - 81), a2, 128, v_rbx + v_r14 * 1);
    goto loc_0040771E;
}
```

## 5. (Beta) C Style

```c
int64_t MiBuildReservationCluster(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p30;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (216);
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 0;
    result = (uint32_t)((*(uint16_t *)(arg2 + 0xAC)) & (15));
    *(uint64_t *)(local_rsp - 0x5F - 0x79) = Arg1;
    result = (result) + (48);
    local_r14 = (local_r14) * (result);
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = v_xmm1;
    result = MiRefPageFileSpaceBitmaps(Arg2, local_rsp - 95 - 89, Arg2, Arg4);
loc_00407227:
loc_00407231:
    if ((*(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10)) == result) goto loc_00407950;
    local_rsi = (*(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10) + *(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10) * 2) << (4);
    local_rsi = (local_rsi) + (Arg2);
    result = MiSafeLockPage(*(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10), local_rsp - 95 - 89, Arg2, Arg4);
    if (((uint8_t)(result)) == 17) goto loc_00407231;
    if ((*(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10)) != (*(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10))) goto loc_00407914;
    if (*(uint64_t *)(v_rip + 0xA269FB) == 0) goto loc_00407299;
    result = *(uint64_t *)(v_rip + 0xA269FB);
    local_rbx = *(uint64_t *)(local_rsi + 0x10);
    if ((((uint8_t)(*(uint64_t *)(local_rsi + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA269FB));
        local_rbx = (*(uint64_t *)(local_rsi + 0x10)) & (result);
    }
    local_rbx = (local_rbx) >> (32);
    if (((uint32_t)(local_rbx)) >= ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x51)))) goto loc_00407942;
    result = (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x51)))) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00407746;
    result = MiReferencePageForModifiedWrite(local_rsi, 1, Arg2, Arg4);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67)) = *(uint64_t *)(local_r14 + *(uint64_t *)(arg2 + 0xD8) * 1 + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77))) == 1) goto loc_00407827;
    local_r12 = (*(uint64_t *)(local_rsi + 0x8)) | (*(uint64_t *)(local_rsp - 0x5F + 0x77));
    result = (*(uint64_t *)(local_rsi + 0x28)) & (local_rsi);
    *(uint64_t *)(local_rsp - 0x5F - 0x71) = result;
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = Arg1;
    local_r13 = 0;
loc_0040732D:
    if (condition_is_below) goto loc_00407791;
    result = MiAddLockedPageCharge(Arg1, 1, Arg2, Arg4);
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), Arg2, Arg4);
    if (sign_flag) goto loc_004077B2;
loc_00407371:
    result = MiReservePtes(v_rip + 10683117, 1, Arg2, Arg4);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
    if (result == 0) goto loc_00407815;
    result = MiMakeValidPte(result, *(uint64_t *)(local_rsp - 0x5F - 0x71), (uint32_t)(0x20000001ULL), Arg4);
    if (condition_is_below) goto loc_00407877;
loc_004073BE:
    *(uint64_t *)(result) = result;
    Arg2 = (result) << (25);
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x69)) << (25);
    Arg2 = (Arg2) - (result);
    local_r12 = (local_r12) >> (3);
    Arg2 = (Arg2) >> (16);
    local_r12 = (local_r12) & (511);
    *(void **)(local_rsp - 0x5F - 0x9) = Arg2;
    *(void **)(local_rsp - 0x5F - 0x71) = Arg2 + local_r12 * 8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x7D))) != 0) goto loc_00407849;
    local_rsi = (Arg2) + (0xFF8ULL);
loc_00407402:
    local_rdi = (*(uint64_t *)(local_rsi + 0x10)) & (0xFFFFFFFFFC00FC1FULL);
    local_rsi = (local_rsi) - (Arg2 + local_r12 * 8);
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = local_rdi;
    local_rsi = (local_rsi) >> (3);
    *(uint32_t *)(local_rsp - 0x5F - 0x61) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)))) - 1);
    if (((uint32_t)(local_rsi)) >= ((uint32_t)(result))) { local_rsi = (uint32_t)(result); }
    if (*(uint64_t *)(v_rip + 0xA2684F) == 0) goto loc_00407444;
    local_r13 = local_rdi;
    if ((((uint8_t)(local_rdi)) & (16)) == 0) {
        local_r13 = *(uint64_t *)(v_rip + 0xA2684F);
        local_r13 = ~(local_r13);
        local_r13 = (local_r13) & (local_rdi);
    }
    local_r13 = (local_r13) >> (32);
    Arg1 = ((uint32_t)((uint32_t)(local_rsi))) + (local_r13);
    if (Arg1 >= ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x51))))) goto loc_0040792D;
loc_0040745D:
loc_00407465:
    if ((uint32_t)(local_rsi) == 0) goto loc_004074CF;
    local_r13 = (local_r13) + 1;
    local_rdi = (Arg2 + local_r12 * 8) + (8);
    result = MiUpdatePageFileHighInPte(local_rdi, local_r13, 511, Arg4);
    v_stack_mF8 = v_stack_mE0;
    result = MiGetPageForWriteCluster(local_rsp - 95 - 81, local_rdi, result, v_stack_mE4);
    if (result == -1) goto loc_004074CF;
    local_rsi = (uint32_t)((local_rsi) - 1);
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x67)) + (8);
    local_r14 = (uint32_t)((1) + 1);
    *(uint64_t *)(local_rsp - 0x5F + 0x67) = Arg1;
    *(uint64_t *)(Arg1) = result;
    local_r15 = (uint32_t)(v_stack_mE8);
    if (result == (*(uint64_t *)(v_rip + 0xA2FFBB))) {
        local_r15 = (uint32_t)(((uint32_t)(v_stack_mE8)) + 1);
    }
    if (v_stack_mE0 != 3) goto loc_00407465;
    if (((uint32_t)(local_r14)) < 16) goto loc_00407465;
loc_004074CF:
    local_r14 = (uint32_t)((local_r14) - (v_stack_mE4));
    local_r15 = (uint32_t)((local_r15) - (v_stack_mE4));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x61))) - ((uint32_t)(local_r14)));
    v_stack_mE8 = (uint32_t)(local_r15);
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x7D)) != 0) goto loc_0040785D;
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F - 0x71)) & (0xFFFFFFFFFFFFF000ULL);
loc_004074FC:
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x71)) - (Arg1);
    result = (result) >> (3);
    if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) { local_rsi = (uint32_t)(result); }
    if (*(uint64_t *)(v_rip + 0xA26767) == 0) goto loc_0040752D;
    local_rbx = *(uint64_t *)(local_rsp - 0x5F - 0x1);
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0x5F - 0x1))) & (16)) == 0) {
        local_rbx = *(uint64_t *)(v_rip + 0xA26767);
        local_rbx = ~(local_rbx);
        local_rbx = (local_rbx) & (*(uint64_t *)(local_rsp - 0x5F - 0x1));
    }
    local_rbx = (local_rbx) >> (32);
    if (((uint32_t)((uint32_t)(local_rsi))) > (local_rbx - 1)) goto loc_0040793A;
loc_00407540:
    if ((uint32_t)(local_rsi) == 0) goto loc_00407840;
    Arg3 = ((uint32_t)((uint32_t)(local_r14))) << (3);
    result = memcpy(*(uint64_t *)(local_rsp - 0x5F - 0x79) + local_rsi * 8, *(uint64_t *)(local_rsp - 0x5F - 0x79), Arg3, v_stack_mE4);
loc_0040756B:
    if ((uint32_t)(local_rsi) == 0) goto loc_004075CE;
    local_rbx = (local_rbx) - 1;
    local_r12 = (*(uint64_t *)(local_rsp - 0x5F - 0x71)) - (8);
    result = MiUpdatePageFileHighInPte(*(uint64_t *)(local_rsp - 0x5F - 0x1), local_rbx, Arg3, v_stack_mE4);
    v_stack_mF8 = v_stack_mE0;
    result = MiGetPageForWriteCluster(local_rsp - 95 - 81, local_r12, result, v_stack_mE4);
    if (result == -1) goto loc_004075CE;
    local_r13 = (*(uint64_t *)(local_rsp - 0x5F - 0x79) + local_rsi * 8) - (8);
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_r14 = (uint32_t)((local_r14) + 1);
    *(uint64_t *)(local_r13) = result;
    if (result == (*(uint64_t *)(v_rip + 0xA2FEBC))) {
        local_r15 = (uint32_t)((local_r15) + 1);
    }
    if (v_stack_mE0 != 3) goto loc_0040756B;
    if (((uint32_t)(local_r14)) < 16) goto loc_0040756B;
loc_004075CE:
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)((uint32_t)(v_stack_mE4))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)(v_stack_mE4))));
    v_stack_mE8 = (uint32_t)(local_r15);
    Arg2 = ((uint32_t)(v_stack_mE4) * 8) + (local_r13);
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x79)) != Arg2) {
        Arg3 = (uint32_t)(local_r14);
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x79);
        Arg3 = (Arg3) << (3);
        result = memcpy(Arg1, Arg2, Arg3, v_stack_mE4);
    }
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) * 2) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) * 2);
    if (*(uint64_t *)(v_rip + 0xA2665D) == 0) goto loc_00407633;
    result = *(uint64_t *)(v_rip + 0xA2665D);
    local_rbx = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) + local_rbx * 8);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) + local_rbx * 8))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA2665D));
        local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x79)) + local_rbx * 8)) & (result);
    }
    local_rbx = (local_rbx) >> (32);
    result = MiReleasePtes(v_rip + 10682410, *(uint64_t *)(local_rsp - 0x5F + 0x7), 1, v_stack_mE4);
loc_00407651:
    result = MiLockPageInline(*(uint64_t *)(local_rsp - 0x5F - 0x69), *(uint64_t *)(local_rsp - 0x5F + 0x7), 1, v_stack_mE4);
    result = MiRemoveLockedPageChargeAndDecRef(*(uint64_t *)(local_rsp - 0x5F - 0x69), *(uint64_t *)(local_rsp - 0x5F + 0x7), 1, v_stack_mE4);
    result = MiUnlockPage(*(uint64_t *)(local_rsp - 0x5F - 0x69), (uint8_t)((uint8_t)(result)), 1, v_stack_mE4);
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x7D)) != 0) goto loc_004078AF;
loc_00407679:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)))))) goto loc_00407788;
    if ((uint32_t)(local_r14) == 0) goto loc_00407788;
    if (((uint32_t)((uint32_t)(local_rbx)) + (uint32_t)((uint32_t)(local_r14)) * 1) >= ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x51))))) goto loc_00407788;
    if (((uint32_t)((uint32_t)(local_rbx)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77))) * 1) > ((uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F - 0x51))))) goto loc_004078E1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)))) - ((uint32_t)(local_r14)));
loc_004076B9:
    v_stack_mF0 = v_stack_mE8;
    v_stack_mF8 = *(uint64_t *)(local_rsp - 0x5F - 0x79) + (uint32_t)((uint32_t)(local_r14)) * 8;
    result = MiAddToReservationCluster(*(uint64_t *)(local_rsp - 0x5F + 0x6F), local_rsp - 95 - 81, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
loc_004076EB:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 200, local_rsp - 95 - 81, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 200, (uint8_t)(result), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x59)))) != 0) goto loc_0040771E;
    if (*(uint64_t *)(local_rsp - 0x5F - 0x59) != 0) goto loc_00407959;
loc_0040771E:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)) = (uint32_t)(local_r14);
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)(v_stack_mE8))));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7F)) = (uint32_t)(local_r14);
    local_rsp = (local_rsp) + (216);
    return (uint32_t)((uint32_t)(local_rbx));
loc_00407746:
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 200, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10)) & (-3);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10) = result;
    result = MiInsertPageInList(*(uint64_t *)(local_rsp - 0x5F + 0x6F), 8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    result = MiUnlockPage(*(uint64_t *)(local_rsp - 0x5F + 0x6F), (uint8_t)((uint32_t)(v_stack_mE8)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))), local_rbx + local_r14 * 1);
    Arg3 = 0;
    result = MiReleasePageFileInfo(*(uint64_t *)(local_rsp - 0x5F - 0x69), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10), Arg3, local_rbx + local_r14 * 1);
    goto loc_00407227;
loc_00407788:
    goto loc_004076EB;
loc_00407791:
    local_r13 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x69)) + 1);
    if (((*(uint32_t *)(v_rip + 0xBBDB11)) & ((uint32_t)(local_r13))) == 0) goto loc_004078EC;
loc_004077A1:
loc_004077A3:
    if (!sign_flag) goto loc_0040732D;
    goto loc_00407791;
loc_004077B2:
    result = MiReferencePfBackedSection(*(uint64_t *)(local_rsp - 0x5F - 0x59), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10), Arg3, local_rbx + local_r14 * 1);
    if (result == 0) goto loc_00407815;
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F - 0x59)) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = *(uint64_t *)(result);
    *(uint32_t *)(local_rsp - 0x5F - 0x7D) = (uint32_t)(local_r14);
    if (Arg2 < (*(uint64_t *)(result + 0x8))) { Arg2 = *(uint64_t *)(result + 0x8); }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x2C))) - 1);
    *(void **)(local_rsp - 0x5F - 0x21) = Arg2;
    Arg3 = Arg2 + 4088;
    if ((Arg2 + 4088) > (*(uint64_t *)(result + 0x8) + result * 8)) { Arg3 = *(uint64_t *)(result + 0x8) + result * 8; }
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = Arg3;
    if ((Arg2 + 4088) >= (*(uint64_t *)(result + 0x8) + result * 8)) goto loc_00407371;
loc_00407815:
    goto loc_00407651;
loc_00407827:
    result = MiUnlockPage(*(uint64_t *)(local_rsp - 0x5F - 0x79), (uint8_t)((uint32_t)(v_stack_p30)), Arg3, local_rbx + local_r14 * 1);
    goto loc_00407679;
loc_00407840:
    goto loc_00407604;
loc_00407849:
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x19)) >> (3);
    result = (result) & (Arg3);
    goto loc_00407402;
loc_0040785D:
    result = (*(uint64_t *)(local_rsp - 0x5F - 0x21)) >> (3);
    result = (uint32_t)((result) & (511));
    goto loc_004074FC;
loc_00407877:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10))) & (32)) != 0) goto loc_004073BE;
    result = (local_r13) + (*(uint64_t *)(local_rsp - 0x5F - 0x9) + result * 8);
    if ((*(uint64_t *)(local_rsp - 0x5F - 0x79) + result * 8) < result) goto loc_004073BE;
    result = MiCheckLinearProtectedPteAccessedBit(*(uint64_t *)(local_rsp - 0x5F - 0x79) + result * 8, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10), 128, local_rbx + local_r14 * 1);
    goto loc_004073BE;
loc_004078AF:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x29) != 0) {
        Arg2 = *(uint8_t *)(local_rsp - 0x5F - 0x11);
        result = MiUnlockProtoPoolPage(*(uint64_t *)(local_rsp - 0x5F - 0x29), Arg2, 128, local_rbx + local_r14 * 1);
    }
    Arg2 = 0;
    result = MiDecrementModifiedWriteCount(*(uint64_t *)(local_rsp - 0x5F - 0x31), Arg2, 128, local_rbx + local_r14 * 1);
    if (result == 0) goto loc_00407679;
    result = MiReleaseControlAreaWaiters(result, Arg2, 128, local_rbx + local_r14 * 1);
    goto loc_00407679;
loc_004078E1:
    local_r12 = (uint32_t)((*(uint64_t *)(local_rsp - 0x5F - 0x51)) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x10))));
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(local_r14)));
    goto loc_004076B9;
loc_004078EC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBBF1C6)))) & (64)) == 0) goto loc_004077A1;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, Arg2, 128, local_rbx + local_r14 * 1);
    if ((uint8_t)(result) == 0) goto loc_00407924;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), Arg2, 128, local_rbx + local_r14 * 1);
    goto loc_004077A3;
loc_00407914:
    result = MiUnlockPage(*(uint64_t *)(local_rsp - 0x5F - 0x79) + result * 8, (uint8_t)((uint32_t)(v_stack_p30)), 128, local_rbx + local_r14 * 1);
    goto loc_00407227;
loc_00407924:
    goto loc_004077A1;
loc_0040792D:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(local_r13)));
    local_rsi = (uint32_t)((local_rsi) - 1);
    goto loc_0040745D;
loc_0040793A:
    goto loc_00407540;
loc_00407942:
    result = MiUnlockPage(*(uint64_t *)(local_rsp - 0x5F - 0x69), (uint8_t)((uint32_t)(v_stack_p30)), 128, local_rbx + local_r14 * 1);
loc_00407950:
loc_00407959:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x5F - 0x51), Arg2, 128, local_rbx + local_r14 * 1);
    goto loc_0040771E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xAC` | `16` | `R` |
| `Arg2` | `+ 0xD8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004071A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
