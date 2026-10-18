# MiCompleteProtoPteFault

- RVA: `0x00345710`–`0x003467E7` (길이 `4,311` bytes)
- VA: `0x0000000140345710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077FC4`
- 디코드: `973`개 명령, `4,311/4,311` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x003457E4` → [MiGetContainingPageTable](MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x003459B6` → [MiIsAddressGlobal](../33/MiIsAddressGlobal_function_003308D0.md) (function, `0x003308D0`)
- `0x00345B4B` → [MiEmptyDeferredWorkingSetEntries](MiEmptyDeferredWorkingSetEntries_function_00347910.md) (function, `0x00347910`)
- `0x00345BAC` → [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) (function, `0x003332C0`)
- `0x00345CC9` → [ObpTraceObjectReferenceIfActive](../21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x00345CF2` → [MiGetSessionIdForVa](MiGetSessionIdForVa_function_00346C60.md) (function, `0x00346C60`)
- `0x00345D5B` → [PfSnReferenceProcessTrace](PfSnReferenceProcessTrace_function_00344A80.md) (function, `0x00344A80`)
- `0x00345DA6` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00345DBF` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00345E65` → [MiLocateCloneAddress](../3D/MiLocateCloneAddress_function_003D26B4.md) (function, `0x003D26B4`)
- `0x00345F32` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00345FA8` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x00345FD2` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00346004` → [MiCheckAndUpdateIoAttribution](../3C/MiCheckAndUpdateIoAttribution_function_003CB3C4.md) (function, `0x003CB3C4`)
- `0x0034609F` → [MiUserPdeOrAbove](../2C/MiUserPdeOrAbove_function_002C57F0.md) (function, `0x002C57F0`)
- `0x0034610C` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00346114` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0034613A` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x0034621E` → [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) (function, `0x003693E8`)
- `0x00346234` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x00346261` → [MiMakeTransitionPteValid](../28/MiMakeTransitionPteValid_function_00283D60.md) (function, `0x00283D60`)
- `0x0034630E` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x00346384` → [MiGetSharedProtos](MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x003463BF` → [MiSystemImageHasPrivateFixups](../45/MiSystemImageHasPrivateFixups_function_004507E0.md) (function, `0x004507E0`)
- `0x00346425` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x00346444` → [MiSetFaultPacketDirectives](../46/MiSetFaultPacketDirectives_function_004673D8.md) (function, `0x004673D8`)
- `0x00346471` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x003464E4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003464EE` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x003464FB` → [ObFastReferenceObjectLocked](../38/ObFastReferenceObjectLocked_function_00381DA0.md) (function, `0x00381DA0`)
- `0x00346509` → [MiReleaseSpinLockShared](MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x00346521` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00346530` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003465BB` → [MiOffsetToProtos](../24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x003465EC` → [MiEmptyDeferredWorkingSetEntries](MiEmptyDeferredWorkingSetEntries_function_00347910.md) (function, `0x00347910`)
- `0x00346629` → [MiIsDriverPage](../2A/MiIsDriverPage_function_002A5514.md) (function, `0x002A5514`)
- `0x00346663` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0034669E` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x003466B1` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x0034675A` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0034677A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0034678A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0034679D` → [PfSnCheckLoggingForThread](../43/PfSnCheckLoggingForThread_function_0043E090.md) (function, `0x0043E090`)
- `0x003467B8` → [PfSnLogPageFaultCommon](PfSnLogPageFaultCommon_function_00343070.md) (function, `0x00343070`)
- `0x003467DD` → [ExfReleaseRundownProtection](ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)

### Direct callers
- [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) at `0x00282D98`
- [sub_002B5D4A](../2B/Unknown_function_002B5D4A.md) at `0x002B5E75`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x00321B63`
- [MiIssueHardFault](../38/MiIssueHardFault_function_00380074.md) at `0x00380543`

### Static image references
- `0x003457A9` → RVA `0x00E30088` (`.data`; read)
- `0x00345899` → RVA `0x00E2DC80` (`.data`; read)
- `0x003458CF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0034591B` → RVA `0x00010990` (`.rdata`; read)
- `0x00345BE2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00345C6B` → RVA `0x00E67248` (`.data`; read)
- `0x00345D8D` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0034605B` → RVA `0x00E2DBC9` (`.data`; read)
- `0x00346513` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00345710  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00345715  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0034571A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0034571F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00345724  53                              push rbx
00345725  55                              push rbp
00345726  56                              push rsi
00345727  57                              push rdi
00345728  41 54                           push r12
0034572A  41 55                           push r13
0034572C  41 56                           push r14
0034572E  41 57                           push r15
00345730  48 81 EC A8 00 00 00            sub rsp, 0xa8
00345737  4C 8B 19                        mov r11, qword ptr [rcx]
0034573A  45 33 C0                        xor r8d, r8d
0034573D  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
00345741  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0034574B  4D 8B FB                        mov r15, r11
0034574E  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00345753  49 C1 EF 09                     shr r15, 9
00345757  41 8B E8                        mov ebp, r8d
0034575A  4C 23 F8                        and r15, rax
0034575D  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
00345762  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0034576C  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00345774  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
00345779  48 8B C0                        mov rax, rax
0034577C  4C 03 F8                        add r15, rax
0034577F  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
00345783  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00345788  48 C1 E7 04                     shl rdi, 4
0034578C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00345796  48 8B C0                        mov rax, rax
00345799  48 03 F8                        add rdi, rax
0034579C  45 8D 50 01                     lea r10d, [r8 + 1]
003457A0  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003457A5  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003457A9  48 8B 0D D8 A8 AE 00            mov rcx, qword ptr [rip + 0xaea8d8]
003457B0  4C 8B 77 10                     mov r14, qword ptr [rdi + 0x10]
003457B4  48 C1 E8 2B                     shr rax, 0x2b
003457B8  25 FF 03 00 00                  and eax, 0x3ff
003457BD  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003457C1  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
003457C9  49 0F BA E6 0A                  bt r14, 0xa
003457CE  0F 82 75 04 00 00               jb 0x140345c49
003457D4  45 8B E0                        mov r12d, r8d
003457D7  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
003457DC  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
003457E1  49 8B CF                        mov rcx, r15
003457E4  E8 07 10 00 00                  call 0x1403467f0
003457E9  4C 8D 2C 40                     lea r13, [rax + rax*2]
003457ED  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003457F7  49 C1 E5 04                     shl r13, 4
003457FB  48 8B C0                        mov rax, rax
003457FE  4C 03 E8                        add r13, rax
00345801  33 F6                           xor esi, esi
00345803  8B DE                           mov ebx, esi
00345805  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
0034580C  0F 82 CE 03 00 00               jb 0x140345be0
00345812  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00345816  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
00345820  48 8B C8                        mov rcx, rax
00345823  49 BB FF FF FF FF FF FF FF 7F   movabs r11, 0x7fffffffffffffff
0034582D  48 23 CA                        and rcx, rdx
00345830  48 BA 00 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000000
0034583A  48 FF C1                        inc rcx
0034583D  48 33 C1                        xor rax, rcx
00345840  48 23 C2                        and rax, rdx
00345843  48 33 C1                        xor rax, rcx
00345846  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
0034584A  F0 4D 21 5D 18                  lock and qword ptr [r13 + 0x18], r11
0034584F  49 8B 1F                        mov rbx, qword ptr [r15]
00345852  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
0034585C  BA FF 01 00 00                  mov edx, 0x1ff
00345861  4C 3B F8                        cmp r15, rax
00345864  72 28                           jb 0x14034588e
00345866  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00345870  4C 3B F8                        cmp r15, rax
00345873  77 19                           ja 0x14034588e
00345875  F6 C3 01                        test bl, 1
00345878  74 14                           je 0x14034588e
0034587A  F6 C3 42                        test bl, 0x42
0034587D  0F 95 C1                        setne cl
00345880  F6 C3 20                        test bl, 0x20
00345883  0F 95 C0                        setne al
00345886  84 C8                           test al, cl
00345888  0F 84 31 05 00 00               je 0x140345dbf
0034588E  48 0F BA E3 0A                  bt rbx, 0xa
00345893  0F 83 70 03 00 00               jae 0x140345c09
00345899  48 8B 0D E0 83 AE 00            mov rcx, qword ptr [rip + 0xae83e0]
003458A0  48 8B C3                        mov rax, rbx
003458A3  48 85 C9                        test rcx, rcx
003458A6  74 0E                           je 0x1403458b6
003458A8  F6 C3 10                        test bl, 0x10
003458AB  75 09                           jne 0x1403458b6
003458AD  48 8B C1                        mov rax, rcx
003458B0  48 F7 D0                        not rax
003458B3  48 23 C3                        and rax, rbx
003458B6  48 C1 E8 20                     shr rax, 0x20
003458BA  B9 FF FF FF FF                  mov ecx, 0xffffffff
003458BF  48 3B C1                        cmp rax, rcx
003458C2  0F 85 41 03 00 00               jne 0x140345c09
003458C8  48 C1 EB 05                     shr rbx, 5
003458CC  83 E3 1F                        and ebx, 0x1f
003458CF  48 F7 05 AE 11 C8 00 00 80 00 00  test qword ptr [rip + 0xc811ae], 0x8000
003458DA  48 BA 00 00 00 00 00 80 FF FF   movabs rdx, 0xffff800000000000
003458E4  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
003458EE  41 B9 02 00 00 00               mov r9d, 2
003458F4  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
003458FE  0F 85 01 05 00 00               jne 0x140345e05
00345904  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00345907  8B F3                           mov esi, ebx
00345909  C1 E8 10                        shr eax, 0x10
0034590C  83 E6 E7                        and esi, 0xffffffe7
0034590F  24 C0                           and al, 0xc0
00345911  3C 40                           cmp al, 0x40
00345913  0F 85 B7 09 00 00               jne 0x1403462d0
00345919  8B FE                           mov edi, esi
0034591B  48 8D 05 6E B0 CC FF            lea rax, [rip - 0x334f92]
00345922  83 E7 1F                        and edi, 0x1f
00345925  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0034592F  48 8B 3C F8                     mov rdi, qword ptr [rax + rdi*8]
00345933  48 B8 7F 0E 00 00 00 00 F0 FF   movabs rax, 0xfff0000000000e7f
0034593D  48 23 F8                        and rdi, rax
00345940  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00345948  48 23 C2                        and rax, rdx
0034594B  48 C1 E0 0C                     shl rax, 0xc
0034594F  48 0B F8                        or rdi, rax
00345952  48 83 CF 21                     or rdi, 0x21
00345956  49 8B C0                        mov rax, r8
00345959  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
00345963  4C 3B F8                        cmp r15, rax
00345966  0F 82 93 02 00 00               jb 0x140345bff
0034596C  48 8B C1                        mov rax, rcx
0034596F  4C 3B F8                        cmp r15, rax
00345972  0F 87 87 02 00 00               ja 0x140345bff
00345978  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00345982  4C 3B F8                        cmp r15, rax
00345985  0F 83 E8 06 00 00               jae 0x140346073
0034598B  49 8B CF                        mov rcx, r15
0034598E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00345998  48 C1 E1 19                     shl rcx, 0x19
0034599C  48 8B C0                        mov rax, rax
0034599F  48 C1 E0 19                     shl rax, 0x19
003459A3  48 2B C8                        sub rcx, rax
003459A6  48 C1 F9 10                     sar rcx, 0x10
003459AA  49 3B C8                        cmp rcx, r8
003459AD  77 04                           ja 0x1403459b3
003459AF  48 83 CF 04                     or rdi, 4
003459B3  48 8B D7                        mov rdx, rdi
003459B6  E8 15 AF FE FF                  call 0x1403308d0
003459BB  48 0F BA EF 08                  bts rdi, 8
003459C0  85 C0                           test eax, eax
003459C2  48 0F 44 FA                     cmove rdi, rdx
003459C6  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
003459CD  48 B8 FF FF FF FF FF FF FF FA   movabs rax, 0xfaffffffffffffff
003459D7  48 23 F8                        and rdi, rax
003459DA  48 B8 00 00 00 00 00 00 00 0A   movabs rax, 0xa00000000000000
003459E4  48 0B F8                        or rdi, rax
003459E7  85 D2                           test edx, edx
003459E9  0F 85 BA 04 00 00               jne 0x140345ea9
003459EF  48 83 BC 24 00 01 00 00 00      cmp qword ptr [rsp + 0x100], 0
003459F8  0F 85 C6 04 00 00               jne 0x140345ec4
003459FE  45 33 C9                        xor r9d, r9d
00345A01  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
00345A06  4D 8B C1                        mov r8, r9
00345A09  41 8B F1                        mov esi, r9d
00345A0C  45 8B F9                        mov r15d, r9d
00345A0F  85 D2                           test edx, edx
00345A11  75 76                           jne 0x140345a89
00345A13  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00345A18  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
00345A1D  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00345A21  48 0F BA E0 28                  bt rax, 0x28
00345A26  72 0D                           jb 0x140345a35
00345A28  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00345A2C  48 85 C0                        test rax, rax
00345A2F  0F 89 C1 08 00 00               jns 0x1403462f6
00345A35  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00345A3A  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00345A44  4C 3B F0                        cmp r14, rax
00345A47  0F 83 50 09 00 00               jae 0x14034639d
00345A4D  4D 85 E4                        test r12, r12
00345A50  0F 84 DD 03 00 00               je 0x140345e33
00345A56  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00345A5B  8B 40 38                        mov eax, dword ptr [rax + 0x38]
00345A5E  A8 20                           test al, 0x20
00345A60  74 03                           je 0x140345a65
00345A62  83 CD 04                        or ebp, 4
00345A65  83 FD 04                        cmp ebp, 4
00345A68  0F 83 62 06 00 00               jae 0x1403460d0
00345A6E  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
00345A72  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00345A77  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00345A7C  40 F6 C5 02                     test bpl, 2
00345A80  0F 85 7C 07 00 00               jne 0x140346202
00345A86  45 33 C9                        xor r9d, r9d
00345A89  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00345A8E  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
00345A96  40 F6 C5 01                     test bpl, 1
00345A9A  45 8B F1                        mov r14d, r9d
00345A9D  48 8B C2                        mov rax, rdx
00345AA0  44 0F 44 F3                     cmove r14d, ebx
00345AA4  83 E0 01                        and eax, 1
00345AA7  0F 85 A4 08 00 00               jne 0x140346351
00345AAD  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
00345AB1  48 8D 0A                        lea rcx, [rdx]
00345AB4  49 8B D1                        mov rdx, r9
00345AB7  48 89 94 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdx
00345ABF  48 85 C0                        test rax, rax
00345AC2  0F 85 A3 08 00 00               jne 0x14034636b
00345AC8  48 83 BC 24 00 01 00 00 00      cmp qword ptr [rsp + 0x100], 0
00345AD1  0F 85 3E 05 00 00               jne 0x140346015
00345AD7  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00345ADF  41 0F B6 49 45                  movzx ecx, byte ptr [r9 + 0x45]
00345AE4  4D 8D 61 38                     lea r12, [r9 + 0x38]
00345AE8  F6 C1 10                        test cl, 0x10
00345AEB  0F 85 37 08 00 00               jne 0x140346328
00345AF1  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
00345AF5  A8 01                           test al, 1
00345AF7  0F 85 BD 07 00 00               jne 0x1403462ba
00345AFD  0F B6 C1                        movzx eax, cl
00345B00  24 09                           and al, 9
00345B02  3C 08                           cmp al, 8
00345B04  75 77                           jne 0x140345b7d
00345B06  F6 C1 04                        test cl, 4
00345B09  75 72                           jne 0x140345b7d
00345B0B  41 0F B7 44 24 0A               movzx eax, word ptr [r12 + 0xa]
00345B11  BB FF 01 00 00                  mov ebx, 0x1ff
00345B16  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00345B1B  66 85 C0                        test ax, ax
00345B1E  74 35                           je 0x140345b55
00345B20  41 0F B7 4C 24 08               movzx ecx, word ptr [r12 + 8]
00345B26  03 C8                           add ecx, eax
00345B28  8B C2                           mov eax, edx
00345B2A  C1 E8 03                        shr eax, 3
00345B2D  23 C3                           and eax, ebx
00345B2F  3B C8                           cmp ecx, eax
00345B31  75 15                           jne 0x140345b48
00345B33  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
00345B37  48 85 C0                        test rax, rax
00345B3A  0F 88 E2 02 00 00               js 0x140345e22
00345B40  41 F6 44 24 0D 02               test byte ptr [r12 + 0xd], 2
00345B46  75 0D                           jne 0x140345b55
00345B48  49 8B CC                        mov rcx, r12
00345B4B  E8 C0 1D 00 00                  call 0x140347910
00345B50  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00345B55  41 0F B7 44 24 0A               movzx eax, word ptr [r12 + 0xa]
00345B5B  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00345B60  66 85 C0                        test ax, ax
00345B63  0F 84 12 03 00 00               je 0x140345e7b
00345B69  66 FF C0                        inc ax
00345B6C  66 41 89 44 24 0A               mov word ptr [r12 + 0xa], ax
00345B72  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
00345B7A  83 CE 04                        or esi, 4
00345B7D  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00345B85  8B DE                           mov ebx, esi
00345B87  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00345B8C  83 CB 10                        or ebx, 0x10
00345B8F  41 F6 44 24 0D 01               test byte ptr [r12 + 0xd], 1
00345B95  45 8B CE                        mov r9d, r14d
00345B98  0F 44 DE                        cmove ebx, esi
00345B9B  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00345B9F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00345BA4  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00345BA9  48 8B D7                        mov rdx, rdi
00345BAC  E8 0F D7 FE FF                  call 0x1403332c0
00345BB1  85 C0                           test eax, eax
00345BB3  0F 84 CB 0A 00 00               je 0x140346684
00345BB9  40 F6 C5 08                     test bpl, 8
00345BBD  0F 85 1F 08 00 00               jne 0x1403463e2
00345BC3  41 8B C7                        mov eax, r15d
00345BC6  48 81 C4 A8 00 00 00            add rsp, 0xa8
00345BCD  41 5F                           pop r15
00345BCF  41 5E                           pop r14
00345BD1  41 5D                           pop r13
00345BD3  41 5C                           pop r12
00345BD5  5F                              pop rdi
00345BD6  5E                              pop rsi
00345BD7  5D                              pop rbp
00345BD8  5B                              pop rbx
00345BD9  C3                              ret
00345BDA  CC                              int3
00345BDB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00345BE0  FF C3                           inc ebx
00345BE2  85 1D C4 F6 C7 00               test dword ptr [rip + 0xc7f6c4], ebx
00345BE8  0F 84 25 09 00 00               je 0x140346513
00345BEE  F3 90                           pause
00345BF0  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00345BF4  48 85 C0                        test rax, rax
00345BF7  0F 89 08 FC FF FF               jns 0x140345805
00345BFD  EB E1                           jmp 0x140345be0
00345BFF  48 0F BA EF 08                  bts rdi, 8
00345C04  E9 BD FD FF FF                  jmp 0x1403459c6
00345C09  41 BA 01 00 00 00               mov r10d, 1
00345C0F  49 8B C6                        mov rax, r14
00345C12  48 C1 E8 05                     shr rax, 5
00345C16  41 8B EA                        mov ebp, r10d
00345C19  83 E0 1F                        and eax, 0x1f
00345C1C  F6 C3 08                        test bl, 8
00345C1F  41 0F 45 C2                     cmovne eax, r10d
00345C23  4C 8B 94 24 00 01 00 00         mov r10, qword ptr [rsp + 0x100]
00345C2B  8B D8                           mov ebx, eax
00345C2D  4D 85 D2                        test r10, r10
00345C30  0F 84 99 FC FF FF               je 0x1403458cf
00345C36  A8 04                           test al, 4
00345C38  4C 0F 44 D6                     cmove r10, rsi
00345C3C  4C 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], r10
00345C44  E9 86 FC FF FF                  jmp 0x1403458cf
00345C49  48 8B 05 30 80 AE 00            mov rax, qword ptr [rip + 0xae8030]
00345C50  49 8B F6                        mov rsi, r14
00345C53  48 85 C0                        test rax, rax
00345C56  74 0F                           je 0x140345c67
00345C58  41 F6 C6 10                     test r14b, 0x10
00345C5C  75 09                           jne 0x140345c67
00345C5E  48 8B F0                        mov rsi, rax
00345C61  48 F7 D6                        not rsi
00345C64  49 23 F6                        and rsi, r14
00345C67  48 C1 FE 10                     sar rsi, 0x10
00345C6B  39 2D D7 15 B2 00               cmp dword ptr [rip + 0xb215d7], ebp
00345C71  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00345C76  4C 8B 2E                        mov r13, qword ptr [rsi]
00345C79  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00345C7E  0F 84 1E 05 00 00               je 0x1403461a2
00345C84  49 8D 7D 40                     lea rdi, [r13 + 0x40]
00345C88  0F 0D 0F                        prefetchw byte ptr [rdi]
00345C8B  48 8B 17                        mov rdx, qword ptr [rdi]
00345C8E  F6 C2 0F                        test dl, 0xf
00345C91  74 15                           je 0x140345ca8
00345C93  48 8D 4A FF                     lea rcx, [rdx - 1]
00345C97  48 8B C2                        mov rax, rdx
00345C9A  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00345C9F  74 07                           je 0x140345ca8
00345CA1  48 8B D0                        mov rdx, rax
00345CA4  A8 0F                           test al, 0xf
00345CA6  75 EB                           jne 0x140345c93
00345CA8  4C 8B E2                        mov r12, rdx
00345CAB  83 E2 0F                        and edx, 0xf
00345CAE  49 83 E4 F0                     and r12, 0xfffffffffffffff0
00345CB2  41 3B D2                        cmp edx, r10d
00345CB5  0F 86 EF 04 00 00               jbe 0x1403461aa
00345CBB  49 8D 4C 24 D0                  lea rcx, [r12 - 0x30]
00345CC0  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
00345CC6  41 8B D2                        mov edx, r10d
00345CC9  E8 B2 AA EC FF                  call 0x140210780
00345CCE  4D 85 E4                        test r12, r12
00345CD1  0F 84 13 08 00 00               je 0x1403464ea
00345CD7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00345CDC  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00345CE6  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00345CEA  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00345CEF  48 0B D8                        or rbx, rax
00345CF2  E8 69 0F 00 00                  call 0x140346c60
00345CF7  4C 8B 0E                        mov r9, qword ptr [rsi]
00345CFA  41 8B 49 38                     mov ecx, dword ptr [r9 + 0x38]
00345CFE  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
00345D02  F6 C1 20                        test cl, 0x20
00345D05  0F 85 5B 04 00 00               jne 0x140346166
00345D0B  4D 85 C0                        test r8, r8
00345D0E  0F 84 AD 09 00 00               je 0x1403466c1
00345D14  49 2B D8                        sub rbx, r8
00345D17  48 C1 FB 03                     sar rbx, 3
00345D1B  48 C1 E3 0C                     shl rbx, 0xc
00345D1F  33 D2                           xor edx, edx
00345D21  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
00345D24  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00345D27  81 E1 C0 FF 00 00               and ecx, 0xffc0
00345D2D  48 C1 E1 1A                     shl rcx, 0x1a
00345D31  48 0B C1                        or rax, rcx
00345D34  48 C1 E0 0C                     shl rax, 0xc
00345D38  48 03 D8                        add rbx, rax
00345D3B  41 8B 45 38                     mov eax, dword ptr [r13 + 0x38]
00345D3F  8B F2                           mov esi, edx
00345D41  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
00345D4A  A8 20                           test al, 0x20
00345D4C  B8 01 00 00 00                  mov eax, 1
00345D51  0F 45 F0                        cmovne esi, eax
00345D54  49 8B 8D B8 00 00 00            mov rcx, qword ptr [r13 + 0xb8]
00345D5B  E8 20 ED FF FF                  call 0x140344a80
00345D60  4C 8B F8                        mov r15, rax
00345D63  48 85 C0                        test rax, rax
00345D66  0F 85 28 0A 00 00               jne 0x140346794
00345D6C  0F 0D 0F                        prefetchw byte ptr [rdi]
00345D6F  48 8B 07                        mov rax, qword ptr [rdi]
00345D72  48 8B C8                        mov rcx, rax
00345D75  49 33 CC                        xor rcx, r12
00345D78  48 83 F9 0F                     cmp rcx, 0xf
00345D7C  0F 83 D9 08 00 00               jae 0x14034665b
00345D82  48 8D 48 01                     lea rcx, [rax + 1]
00345D86  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00345D8B  75 E5                           jne 0x140345d72
00345D8D  39 2D 7D F2 C7 00               cmp dword ptr [rip + 0xc7f27d], ebp
00345D93  74 16                           je 0x140345dab
00345D95  33 D2                           xor edx, edx
00345D97  49 8D 4C 24 D0                  lea rcx, [r12 - 0x30]
00345D9C  41 B9 4D 6D 53 63               mov r9d, 0x63536d4d
00345DA2  44 8D 42 01                     lea r8d, [rdx + 1]
00345DA6  E8 39 AC EC FF                  call 0x1402109e4
00345DAB  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00345DB0  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00345DB5  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00345DBA  E9 22 FA FF FF                  jmp 0x1403457e1
00345DBF  E8 D4 5B FE FF                  call 0x14032b998
00345DC4  48 85 C0                        test rax, rax
00345DC7  0F 84 C1 FA FF FF               je 0x14034588e
00345DCD  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00345DD4  48 85 C9                        test rcx, rcx
00345DD7  0F 84 B1 FA FF FF               je 0x14034588e
00345DDD  49 8B C7                        mov rax, r15
00345DE0  48 C1 E8 03                     shr rax, 3
00345DE4  48 23 C2                        and rax, rdx
00345DE7  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00345DEB  A8 20                           test al, 0x20
00345DED  74 04                           je 0x140345df3
00345DEF  48 83 CB 20                     or rbx, 0x20
00345DF3  48 8B CB                        mov rcx, rbx
00345DF6  48 83 CB 42                     or rbx, 0x42
00345DFA  A8 42                           test al, 0x42
00345DFC  48 0F 44 D9                     cmove rbx, rcx
00345E00  E9 89 FA FF FF                  jmp 0x14034588e
00345E05  4C 8B 5C 24 70                  mov r11, qword ptr [rsp + 0x70]
00345E0A  4C 3B DA                        cmp r11, rdx
00345E0D  0F 83 40 06 00 00               jae 0x140346453
00345E13  49 BB FF FF FF FF FF FF FF 7F   movabs r11, 0x7fffffffffffffff
00345E1D  E9 E2 FA FF FF                  jmp 0x140345904
00345E22  41 F6 44 24 0D 02               test byte ptr [r12 + 0xd], 2
00345E28  0F 85 1A FD FF FF               jne 0x140345b48
00345E2E  E9 22 FD FF FF                  jmp 0x140345b55
00345E33  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00345E3C  83 CD 04                        or ebp, 4
00345E3F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00345E46  48 83 B9 80 02 00 00 00         cmp qword ptr [rcx + 0x280], 0
00345E4E  0F 84 11 FC FF FF               je 0x140345a65
00345E54  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
00345E58  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00345E62  48 0B D0                        or rdx, rax
00345E65  E8 4A C8 08 00                  call 0x1403d26b4
00345E6A  48 85 C0                        test rax, rax
00345E6D  0F 84 F2 FB FF FF               je 0x140345a65
00345E73  83 E5 FB                        and ebp, 0xfffffffb
00345E76  E9 EA FB FF FF                  jmp 0x140345a65
00345E7B  8B C2                           mov eax, edx
00345E7D  66 41 C7 44 24 0A 01 00         mov word ptr [r12 + 0xa], 1
00345E85  C1 E8 03                        shr eax, 3
00345E88  66 23 C3                        and ax, bx
00345E8B  66 41 89 44 24 08               mov word ptr [r12 + 8], ax
00345E91  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
00345E95  48 85 C0                        test rax, rax
00345E98  0F 89 A8 04 00 00               jns 0x140346346
00345E9E  41 80 64 24 0D FD               and byte ptr [r12 + 0xd], 0xfd
00345EA4  E9 C9 FC FF FF                  jmp 0x140345b72
00345EA9  40 80 E6 05                     and sil, 5
00345EAD  40 80 FE 04                     cmp sil, 4
00345EB1  0F 85 38 FB FF FF               jne 0x1403459ef
00345EB7  B8 01 00 00 00                  mov eax, 1
00345EBC  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00345EC4  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00345ECC  4C 39 00                        cmp qword ptr [rax], r8
00345ECF  77 29                           ja 0x140345efa
00345ED1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00345EDA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00345EE1  48 85 FF                        test rdi, rdi
00345EE4  0F 89 0C 07 00 00               jns 0x1403465f6
00345EEA  48 8B 81 78 07 00 00            mov rax, qword ptr [rcx + 0x778]
00345EF1  48 85 C0                        test rax, rax
00345EF4  0F 85 14 08 00 00               jne 0x14034670e
00345EFA  8B C3                           mov eax, ebx
00345EFC  83 E0 05                        and eax, 5
00345EFF  3C 05                           cmp al, 5
00345F01  0F 84 F7 FA FF FF               je 0x1403459fe
00345F07  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00345F0C  48 83 CF 42                     or rdi, 0x42
00345F10  41 0F B6 4F 22                  movzx ecx, byte ptr [r15 + 0x22]
00345F15  C0 E9 04                        shr cl, 4
00345F18  49 0F BA 67 10 0A               bt qword ptr [r15 + 0x10], 0xa
00345F1E  F6 D1                           not cl
00345F20  0F 93 C0                        setae al
00345F23  22 C8                           and cl, al
00345F25  F6 C1 01                        test cl, 1
00345F28  0F 84 B0 00 00 00               je 0x140345fde
00345F2E  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00345F32  E8 F9 95 02 00                  call 0x14036f530
00345F37  85 C0                           test eax, eax
00345F39  0F 84 9F 00 00 00               je 0x140345fde
00345F3F  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00345F44  45 33 C0                        xor r8d, r8d
00345F47  41 8B F0                        mov esi, r8d
00345F4A  45 8B F8                        mov r15d, r8d
00345F4D  F0 49 0F BA 6C 24 18 3F         lock bts qword ptr [r12 + 0x18], 0x3f
00345F55  0F 82 75 07 00 00               jb 0x1403466d0
00345F5B  41 0F B6 54 24 22               movzx edx, byte ptr [r12 + 0x22]
00345F61  4D 8B FC                        mov r15, r12
00345F64  0F B6 CA                        movzx ecx, dl
00345F67  C0 E9 04                        shr cl, 4
00345F6A  49 0F BA 64 24 10 0A            bt qword ptr [r12 + 0x10], 0xa
00345F71  F6 D1                           not cl
00345F73  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00345F78  0F 93 C0                        setae al
00345F7B  22 C8                           and cl, al
00345F7D  F6 C1 01                        test cl, 1
00345F80  74 2B                           je 0x140345fad
00345F82  F6 C2 08                        test dl, 8
00345F85  75 19                           jne 0x140345fa0
00345F87  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
00345F8B  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00345F93  C0 E8 02                        shr al, 2
00345F96  A8 01                           test al, 1
00345F98  0F 85 A8 07 00 00               jne 0x140346746
00345F9E  33 D2                           xor edx, edx
00345FA0  BA 01 00 00 00                  mov edx, 1
00345FA5  49 8B CF                        mov rcx, r15
00345FA8  E8 B3 C9 01 00                  call 0x140362960
00345FAD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00345FB7  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00345FBC  48 85 F6                        test rsi, rsi
00345FBF  74 16                           je 0x140345fd7
00345FC1  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00345FC9  41 B8 01 00 00 00               mov r8d, 1
00345FCF  48 8B D6                        mov rdx, rsi
00345FD2  E8 F9 DF F3 FF                  call 0x140283fd0
00345FD7  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
00345FDE  49 0F BA E6 0A                  bt r14, 0xa
00345FE3  0F 83 15 FA FF FF               jae 0x1403459fe
00345FE9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00345FF1  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00345FF7  24 0F                           and al, 0xf
00345FF9  3C 01                           cmp al, 1
00345FFB  0F 84 FD F9 FF FF               je 0x1403459fe
00346001  49 8B CF                        mov rcx, r15
00346004  E8 BB 53 08 00                  call 0x1403cb3c4
00346009  8B 94 24 08 01 00 00            mov edx, dword ptr [rsp + 0x108]
00346010  E9 E9 F9 FF FF                  jmp 0x1403459fe
00346015  48 0F BA E7 0B                  bt rdi, 0xb
0034601A  0F 82 B7 FA FF FF               jb 0x140345ad7
00346020  48 0F BA E7 09                  bt rdi, 9
00346025  0F 83 AC FA FF FF               jae 0x140345ad7
0034602B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00346034  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0034603B  48 83 B9 70 02 00 00 00         cmp qword ptr [rcx + 0x270], 0
00346043  0F 85 8E FA FF FF               jne 0x140345ad7
00346049  48 85 D2                        test rdx, rdx
0034604C  75 1D                           jne 0x14034606b
0034604E  48 F7 05 2F 0A C8 00 00 00 00 02  test qword ptr [rip + 0xc80a2f], 0x2000000
00346059  75 10                           jne 0x14034606b
0034605B  F6 05 67 7B AE 00 01            test byte ptr [rip + 0xae7b67], 1
00346062  74 07                           je 0x14034606b
00346064  48 83 E7 DF                     and rdi, 0xffffffffffffffdf
00346068  83 CD 10                        or ebp, 0x10
0034606B  83 CD 08                        or ebp, 8
0034606E  E9 64 FA FF FF                  jmp 0x140345ad7
00346073  48 B8 FF FF FF 7F FB F6 FF FF   movabs rax, 0xfffff6fb7fffffff
0034607D  4C 3B F8                        cmp r15, rax
00346080  0F 87 05 F9 FF FF               ja 0x14034598b
00346086  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00346090  4C 3B F8                        cmp r15, rax
00346093  0F 84 B0 05 00 00               je 0x140346649
00346099  49 23 FB                        and rdi, r11
0034609C  49 8B CF                        mov rcx, r15
0034609F  E8 4C F7 F7 FF                  call 0x1402c57f0
003460A4  85 C0                           test eax, eax
003460A6  0F 84 7F 06 00 00               je 0x14034672b
003460AC  48 83 CF 04                     or rdi, 4
003460B0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003460BA  48 C1 E1 19                     shl rcx, 0x19
003460BE  48 8B C0                        mov rax, rax
003460C1  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
003460CB  E9 CF F8 FF FF                  jmp 0x14034599f
003460D0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003460D9  41 8B D1                        mov edx, r9d
003460DC  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
003460E1  4C 89 8C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r9
003460E9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003460F0  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
003460F7  48 8B 80 40 04 00 00            mov rax, qword ptr [rax + 0x440]
003460FE  48 85 C0                        test rax, rax
00346101  0F 84 6B F9 FF FF               je 0x140345a72
00346107  B9 01 00 00 00                  mov ecx, 1
0034610C  E8 DF 5F F3 FF                  call 0x14027c0f0
00346111  49 8B CE                        mov rcx, r14
00346114  E8 B7 07 FD FF                  call 0x1403168d0
00346119  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00346122  4C 8B E0                        mov r12, rax
00346125  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0034612C  48 8B 8A 10 04 00 00            mov rcx, qword ptr [rdx + 0x410]
00346133  48 81 C1 EC 03 00 00            add rcx, 0x3ec
0034613A  E8 51 44 F0 FF                  call 0x14024a590
0034613F  4D 85 E4                        test r12, r12
00346142  74 13                           je 0x140346157
00346144  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
00346149  8B C8                           mov ecx, eax
0034614B  80 E1 70                        and cl, 0x70
0034614E  80 F9 20                        cmp cl, 0x20
00346151  0F 84 E3 03 00 00               je 0x14034653a
00346157  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
0034615F  8B D6                           mov edx, esi
00346161  E9 0C F9 FF FF                  jmp 0x140345a72
00346166  49 3B D8                        cmp rbx, r8
00346169  0F 82 0D 02 00 00               jb 0x14034637c
0034616F  8B 4E 2C                        mov ecx, dword ptr [rsi + 0x2c]
00346172  49 8D 14 C8                     lea rdx, [r8 + rcx*8]
00346176  48 3B DA                        cmp rbx, rdx
00346179  0F 83 FD 01 00 00               jae 0x14034637c
0034617F  49 C1 E0 09                     shl r8, 9
00346183  48 C1 E3 09                     shl rbx, 9
00346187  49 2B D8                        sub rbx, r8
0034618A  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0034618D  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
00346194  48 C1 E0 09                     shl rax, 9
00346198  48 03 D8                        add rbx, rax
0034619B  33 D2                           xor edx, edx
0034619D  E9 99 FB FF FF                  jmp 0x140345d3b
003461A2  4C 8B E6                        mov r12, rsi
003461A5  E9 37 F6 FF FF                  jmp 0x1403457e1
003461AA  85 D2                           test edx, edx
003461AC  0F 84 38 03 00 00               je 0x1403464ea
003461B2  B8 0F 00 00 00                  mov eax, 0xf
003461B7  F0 49 0F C1 44 24 D0            lock xadd qword ptr [r12 - 0x30], rax
003461BE  48 85 C0                        test rax, rax
003461C1  0F 8E 06 03 00 00               jle 0x1403464cd
003461C7  0F 0D 0F                        prefetchw byte ptr [rdi]
003461CA  48 8B 07                        mov rax, qword ptr [rdi]
003461CD  48 8B C8                        mov rcx, rax
003461D0  83 E1 0F                        and ecx, 0xf
003461D3  48 83 C1 0F                     add rcx, 0xf
003461D7  48 83 F9 0F                     cmp rcx, 0xf
003461DB  0F 87 59 05 00 00               ja 0x14034673a
003461E1  48 8B C8                        mov rcx, rax
003461E4  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
003461E8  4C 3B E1                        cmp r12, rcx
003461EB  0F 85 49 05 00 00               jne 0x14034673a
003461F1  48 8D 48 0F                     lea rcx, [rax + 0xf]
003461F5  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
003461FA  0F 84 BB FA FF FF               je 0x140345cbb
00346200  EB CB                           jmp 0x1403461cd
00346202  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00346207  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
0034620F  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00346213  48 8B D0                        mov rdx, rax
00346216  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0034621B  45 8B C6                        mov r8d, r14d
0034621E  E8 C5 31 02 00                  call 0x1403693e8
00346223  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00346228  41 BE 02 00 00 00               mov r14d, 2
0034622E  41 8B D6                        mov edx, r14d
00346231  44 8B F8                        mov r15d, eax
00346234  E8 1B C6 F5 FF                  call 0x1402a2854
00346239  41 81 FF 29 01 00 00            cmp r15d, 0x129
00346240  0F 84 C2 00 00 00               je 0x140346308
00346246  41 81 FF 9A 00 00 C0            cmp r15d, 0xc000009a
0034624D  0F 84 B5 00 00 00               je 0x140346308
00346253  45 85 FF                        test r15d, r15d
00346256  0F 88 67 F9 FF FF               js 0x140345bc3
0034625C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00346261  E8 FA DA F3 FF                  call 0x140283d60
00346266  48 8B F8                        mov rdi, rax
00346269  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00346273  48 C1 E8 0C                     shr rax, 0xc
00346277  48 23 C1                        and rax, rcx
0034627A  4C 8D 04 40                     lea r8, [rax + rax*2]
0034627E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00346288  49 C1 E0 04                     shl r8, 4
0034628C  48 8B C0                        mov rax, rax
0034628F  4C 03 C0                        add r8, rax
00346292  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0034629C  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
003462A1  48 39 44 24 70                  cmp qword ptr [rsp + 0x70], rax
003462A6  0F 83 50 04 00 00               jae 0x1403466fc
003462AC  45 33 C9                        xor r9d, r9d
003462AF  41 8B D9                        mov ebx, r9d
003462B2  83 E5 FE                        and ebp, 0xfffffffe
003462B5  E9 D4 F7 FF FF                  jmp 0x140345a8e
003462BA  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003462BE  80 38 01                        cmp byte ptr [rax], 1
003462C1  0F 85 36 F8 FF FF               jne 0x140345afd
003462C7  48 83 E7 DF                     and rdi, 0xffffffffffffffdf
003462CB  E9 2D F8 FF FF                  jmp 0x140345afd
003462D0  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003462D3  C1 E8 10                        shr eax, 0x10
003462D6  3C 40                           cmp al, 0x40
003462D8  0F 82 9E 03 00 00               jb 0x14034667c
003462DE  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003462E1  C1 E8 10                        shr eax, 0x10
003462E4  24 C0                           and al, 0xc0
003462E6  3C 80                           cmp al, 0x80
003462E8  0F 85 2B F6 FF FF               jne 0x140345919
003462EE  83 CE 18                        or esi, 0x18
003462F1  E9 23 F6 FF FF                  jmp 0x140345919
003462F6  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003462FA  48 85 C0                        test rax, rax
003462FD  0F 85 6B F7 FF FF               jne 0x140345a6e
00346303  E9 2D F7 FF FF                  jmp 0x140345a35
00346308  41 8B D6                        mov edx, r14d
0034630B  49 8B CD                        mov rcx, r13
0034630E  E8 41 C5 F5 FF                  call 0x1402a2854
00346313  41 81 FF 29 01 00 00            cmp r15d, 0x129
0034631A  B8 34 04 00 C0                  mov eax, 0xc0000434
0034631F  44 0F 44 F8                     cmove r15d, eax
00346323  E9 9B F8 FF FF                  jmp 0x140345bc3
00346328  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
0034632C  A8 01                           test al, 1
0034632E  74 0D                           je 0x14034633d
00346330  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00346334  80 38 02                        cmp byte ptr [rax], 2
00346337  0F 84 C0 F7 FF FF               je 0x140345afd
0034633D  48 83 E7 DF                     and rdi, 0xffffffffffffffdf
00346341  E9 AB F7 FF FF                  jmp 0x140345af1
00346346  41 80 4C 24 0D 02               or byte ptr [r12 + 0xd], 2
0034634C  E9 21 F8 FF FF                  jmp 0x140345b72
00346351  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
00346355  48 89 94 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdx
0034635D  80 3A 05                        cmp byte ptr [rdx], 5
00346360  0F 85 4B F7 FF FF               jne 0x140345ab1
00346366  E9 5D F7 FF FF                  jmp 0x140345ac8
0034636B  80 39 03                        cmp byte ptr [rcx], 3
0034636E  0F 85 54 F7 FF FF               jne 0x140345ac8
00346374  83 CE 01                        or esi, 1
00346377  E9 4C F7 FF FF                  jmp 0x140345ac8
0034637C  4C 8B C6                        mov r8, rsi
0034637F  8B D0                           mov edx, eax
00346381  49 8B C9                        mov rcx, r9
00346384  E8 CF 29 00 00                  call 0x140348d58
00346389  48 C1 E3 09                     shl rbx, 9
0034638D  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
00346391  48 C1 E1 09                     shl rcx, 9
00346395  48 2B D9                        sub rbx, rcx
00346398  E9 ED FD FF FF                  jmp 0x14034618a
0034639D  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003463A2  48 85 C0                        test rax, rax
003463A5  74 0B                           je 0x1403463b2
003463A7  8B 40 38                        mov eax, dword ptr [rax + 0x38]
003463AA  A8 20                           test al, 0x20
003463AC  0F 84 BC F6 FF FF               je 0x140345a6e
003463B2  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
003463B7  49 8B CE                        mov rcx, r14
003463BA  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
003463BF  E8 1C A4 10 00                  call 0x1404507e0
003463C4  4C 8B C0                        mov r8, rax
003463C7  48 85 C0                        test rax, rax
003463CA  0F 84 9E F6 FF FF               je 0x140345a6e
003463D0  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003463D5  BA 01 00 00 00                  mov edx, 1
003463DA  83 CD 02                        or ebp, 2
003463DD  E9 95 F6 FF FF                  jmp 0x140345a77
003463E2  33 D2                           xor edx, edx
003463E4  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
003463E9  49 39 54 24 10                  cmp qword ptr [r12 + 0x10], rdx
003463EE  74 14                           je 0x140346404
003463F0  41 F6 44 24 0D 01               test byte ptr [r12 + 0xd], 1
003463F6  75 0C                           jne 0x140346404
003463F8  66 41 39 54 24 0A               cmp word ptr [r12 + 0xa], dx
003463FE  0F 85 E5 01 00 00               jne 0x1403465e9
00346404  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00346409  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0034640E  D1 ED                           shr ebp, 1
00346410  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
00346417  83 E5 08                        and ebp, 8
0034641A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0034641F  44 8B CD                        mov r9d, ebp
00346422  48 8B D7                        mov rdx, rdi
00346425  E8 E2 C5 01 00                  call 0x140362a0c
0034642A  44 8B F8                        mov r15d, eax
0034642D  85 C0                           test eax, eax
0034642F  0F 89 8E F7 FF FF               jns 0x140345bc3
00346435  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0034643A  8B D0                           mov edx, eax
0034643C  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00346444  E8 8F 0F 12 00                  call 0x1404673d8
00346449  B8 34 04 00 C0                  mov eax, 0xc0000434
0034644E  E9 73 F7 FF FF                  jmp 0x140345bc6
00346453  49 8B C0                        mov rax, r8
00346456  4C 3B D8                        cmp r11, rax
00346459  0F 83 79 01 00 00               jae 0x1403465d8
0034645F  41 84 D9                        test r9b, bl
00346462  0F 84 AB F9 FF FF               je 0x140345e13
00346468  45 33 C0                        xor r8d, r8d
0034646B  41 8B D1                        mov edx, r9d
0034646E  48 8B CF                        mov rcx, rdi
00346471  E8 AA EF F3 FF                  call 0x140285420
00346476  8B D0                           mov edx, eax
00346478  A8 01                           test al, 1
0034647A  75 11                           jne 0x14034648d
0034647C  48 F7 05 01 06 C8 00 00 00 01 00  test qword ptr [rip + 0xc80601], 0x10000
00346487  0F 84 7C 01 00 00               je 0x140346609
0034648D  F6 C2 01                        test dl, 1
00346490  0F 85 A1 01 00 00               jne 0x140346637
00346496  F6 C2 08                        test dl, 8
00346499  0F 85 53 02 00 00               jne 0x1403466f2
0034649F  83 E3 FD                        and ebx, 0xfffffffd
003464A2  B8 01 00 00 00                  mov eax, 1
003464A7  0F 44 D8                        cmove ebx, eax
003464AA  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
003464B4  49 BB FF FF FF FF FF FF FF 7F   movabs r11, 0x7fffffffffffffff
003464BE  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
003464C8  E9 37 F4 FF FF                  jmp 0x140345904
003464CD  33 D2                           xor edx, edx
003464CF  48 83 C0 0F                     add rax, 0xf
003464D3  41 B9 10 00 00 00               mov r9d, 0x10
003464D9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003464DE  4D 8B C4                        mov r8, r12
003464E1  8D 4A 18                        lea ecx, [rdx + 0x18]
003464E4  E8 77 71 1B 00                  call 0x1404fd660
003464E9  CC                              int3
003464EA  49 8D 4D 48                     lea rcx, [r13 + 0x48]
003464EE  E8 3D 29 F0 FF                  call 0x140248e30
003464F3  BA 4D 6D 53 63                  mov edx, 0x63536d4d
003464F8  48 8B CF                        mov rcx, rdi
003464FB  E8 A0 B8 03 00                  call 0x140381da0
00346500  B2 11                           mov dl, 0x11
00346502  49 8D 4D 48                     lea rcx, [r13 + 0x48]
00346506  4C 8B E0                        mov r12, rax
00346509  E8 E2 26 00 00                  call 0x140348bf0
0034650E  E9 C4 F7 FF FF                  jmp 0x140345cd7
00346513  8B 05 9F 05 C8 00               mov eax, dword ptr [rip + 0xc8059f]
00346519  A8 40                           test al, 0x40
0034651B  0F 84 CD F6 FF FF               je 0x140345bee
00346521  E8 6A 8F FC FF                  call 0x14030f490
00346526  84 C0                           test al, al
00346528  0F 84 C0 F6 FF FF               je 0x140345bee
0034652E  8B CB                           mov ecx, ebx
00346530  E8 2B 8F FC FF                  call 0x14030f460
00346535  E9 B6 F6 FF FF                  jmp 0x140345bf0
0034653A  0F BA E0 15                     bt eax, 0x15
0034653E  0F 82 13 FC FF FF               jb 0x140346157
00346544  0F BA E0 16                     bt eax, 0x16
00346548  0F 83 09 FC FF FF               jae 0x140346157
0034654E  49 8B 44 24 48                  mov rax, qword ptr [r12 + 0x48]
00346553  41 0F B6 4C 24 20               movzx ecx, byte ptr [r12 + 0x20]
00346559  4D 8B 74 24 50                  mov r14, qword ptr [r12 + 0x50]
0034655E  48 C1 E1 20                     shl rcx, 0x20
00346562  4C 8B 08                        mov r9, qword ptr [rax]
00346565  41 8B 44 24 18                  mov eax, dword ptr [r12 + 0x18]
0034656A  48 0B C8                        or rcx, rax
0034656D  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00346572  48 C1 E8 0C                     shr rax, 0xc
00346576  4D 2B B1 88 00 00 00            sub r14, qword ptr [r9 + 0x88]
0034657D  49 C1 FE 03                     sar r14, 3
00346581  4C 2B F1                        sub r14, rcx
00346584  4C 03 F0                        add r14, rax
00346587  49 8B 84 24 A0 00 00 00         mov rax, qword ptr [r12 + 0xa0]
0034658F  41 8B D6                        mov edx, r14d
00346592  41 0F B6 CE                     movzx ecx, r14b
00346596  48 C1 EA 03                     shr rdx, 3
0034659A  80 E1 07                        and cl, 7
0034659D  0F B6 14 02                     movzx edx, byte ptr [rdx + rax]
003465A1  D2 FA                           sar dl, cl
003465A3  F6 C2 01                        test dl, 1
003465A6  0F 84 AB FB FF FF               je 0x140346157
003465AC  49 8B D6                        mov rdx, r14
003465AF  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
003465B4  48 C1 E2 0C                     shl rdx, 0xc
003465B8  49 8B C9                        mov rcx, r9
003465BB  E8 C0 72 F0 FF                  call 0x14024d880
003465C0  4D 8B 84 24 90 00 00 00         mov r8, qword ptr [r12 + 0x90]
003465C8  83 CD 02                        or ebp, 2
003465CB  41 8B 94 24 88 00 00 00         mov edx, dword ptr [r12 + 0x88]
003465D3  E9 A4 F4 FF FF                  jmp 0x140345a7c
003465D8  48 8B C1                        mov rax, rcx
003465DB  4C 3B D8                        cmp r11, rax
003465DE  0F 86 2F F8 FF FF               jbe 0x140345e13
003465E4  E9 76 FE FF FF                  jmp 0x14034645f
003465E9  49 8B CC                        mov rcx, r12
003465EC  E8 1F 13 00 00                  call 0x140347910
003465F1  E9 0E FE FF FF                  jmp 0x140346404
003465F6  8B 81 F4 01 00 00               mov eax, dword ptr [rcx + 0x1f4]
003465FC  A8 10                           test al, 0x10
003465FE  0F 84 E6 F8 FF FF               je 0x140345eea
00346604  E9 12 01 00 00                  jmp 0x14034671b
00346609  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0034660D  48 85 C9                        test rcx, rcx
00346610  0F 89 80 FE FF FF               jns 0x140346496
00346616  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00346619  48 0F BA E0 0A                  bt rax, 0xa
0034661E  0F 82 69 FE FF FF               jb 0x14034648d
00346624  33 D2                           xor edx, edx
00346626  49 8B CF                        mov rcx, r15
00346629  E8 E6 EE F5 FF                  call 0x1402a5514
0034662E  48 85 C0                        test rax, rax
00346631  0F 84 68 FE FF FF               je 0x14034649f
00346637  BB 03 00 00 00                  mov ebx, 3
0034663C  48 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], rsi
00346644  E9 61 FE FF FF                  jmp 0x1403464aa
00346649  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00346653  48 0B F8                        or rdi, rax
00346656  E9 41 FA FF FF                  jmp 0x14034609c
0034665B  BA 4D 6D 53 63                  mov edx, 0x63536d4d
00346660  49 8B CC                        mov rcx, r12
00346663  E8 38 D8 F1 FF                  call 0x140263ea0
00346668  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0034666D  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00346672  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00346677  E9 65 F1 FF FF                  jmp 0x1403457e1
0034667C  83 CE 08                        or esi, 8
0034667F  E9 95 F2 FF FF                  jmp 0x140345919
00346684  F6 C3 04                        test bl, 4
00346687  74 0B                           je 0x140346694
00346689  B8 FF FF 00 00                  mov eax, 0xffff
0034668E  66 41 01 44 24 0A               add word ptr [r12 + 0xa], ax
00346694  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00346699  BA 02 00 00 00                  mov edx, 2
0034669E  E8 B1 C1 F5 FF                  call 0x1402a2854
003466A3  40 F6 C5 02                     test bpl, 2
003466A7  75 0D                           jne 0x1403466b6
003466A9  BA 02 00 00 00                  mov edx, 2
003466AE  49 8B CD                        mov rcx, r13
003466B1  E8 9E C1 F5 FF                  call 0x1402a2854
003466B6  41 BF 17 00 00 C0               mov r15d, 0xc0000017
003466BC  E9 02 F5 FF FF                  jmp 0x140345bc3
003466C1  33 D2                           xor edx, edx
003466C3  8B DA                           mov ebx, edx
003466C5  E9 57 F6 FF FF                  jmp 0x140345d21
003466CA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
003466D0  41 FF C7                        inc r15d
003466D3  44 85 3D D2 EB C7 00            test dword ptr [rip + 0xc7ebd2], r15d
003466DA  0F 84 8C 00 00 00               je 0x14034676c
003466E0  F3 90                           pause
003466E2  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
003466E7  48 85 C0                        test rax, rax
003466EA  0F 89 5D F8 FF FF               jns 0x140345f4d
003466F0  EB DE                           jmp 0x1403466d0
003466F2  BB 01 00 00 00                  mov ebx, 1
003466F7  E9 40 FF FF FF                  jmp 0x14034663c
003466FC  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
00346700  C1 E8 18                        shr eax, 0x18
00346703  A8 08                           test al, 8
00346705  41 0F 45 F6                     cmovne esi, r14d
00346709  E9 9E FB FF FF                  jmp 0x1403462ac
0034670E  48 83 C0 18                     add rax, 0x18
00346712  48 39 00                        cmp qword ptr [rax], rax
00346715  0F 84 DF F7 FF FF               je 0x140345efa
0034671B  45 33 C9                        xor r9d, r9d
0034671E  4C 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], r9
00346726  E9 D6 F2 FF FF                  jmp 0x140345a01
0034672B  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
00346735  E9 51 F2 FF FF                  jmp 0x14034598b
0034673A  F0 49 83 44 24 D0 F1            lock add qword ptr [r12 - 0x30], -0xf
00346741  E9 75 F5 FF FF                  jmp 0x140345cbb
00346746  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0034674A  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00346752  48 83 E0 FB                     and rax, 0xfffffffffffffffb
00346756  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0034675A  E8 2D 4F FE FF                  call 0x14032b68c
0034675F  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
00346767  E9 34 F8 FF FF                  jmp 0x140345fa0
0034676C  8B 05 46 03 C8 00               mov eax, dword ptr [rip + 0xc80346]
00346772  A8 40                           test al, 0x40
00346774  0F 84 66 FF FF FF               je 0x1403466e0
0034677A  E8 11 8D FC FF                  call 0x14030f490
0034677F  84 C0                           test al, al
00346781  0F 84 59 FF FF FF               je 0x1403466e0
00346787  41 8B CF                        mov ecx, r15d
0034678A  E8 D1 8C FC FF                  call 0x14030f460
0034678F  E9 4E FF FF FF                  jmp 0x1403466e2
00346794  44 8B C6                        mov r8d, esi
00346797  49 8B D7                        mov rdx, r15
0034679A  49 8B CD                        mov rcx, r13
0034679D  E8 EE 78 0F 00                  call 0x14043e090
003467A2  85 C0                           test eax, eax
003467A4  74 17                           je 0x1403467bd
003467A6  4D 8B 44 24 18                  mov r8, qword ptr [r12 + 0x18]
003467AB  4C 8B CB                        mov r9, rbx
003467AE  49 8B D4                        mov rdx, r12
003467B1  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
003467B5  49 8B CF                        mov rcx, r15
003467B8  E8 B3 C8 FF FF                  call 0x140343070
003467BD  49 8D 8F 68 01 00 00            lea rcx, [r15 + 0x168]
003467C4  0F 0D 09                        prefetchw byte ptr [rcx]
003467C7  48 8B 01                        mov rax, qword ptr [rcx]
003467CA  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003467CE  48 8D 50 FE                     lea rdx, [rax - 2]
003467D2  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
003467D7  0F 84 8F F5 FF FF               je 0x140345d6c
003467DD  E8 CE 36 00 00                  call 0x140349eb0
003467E2  E9 85 F5 FF FF                  jmp 0x140345d6c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCompleteProtoPteFault(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
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
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p100;
    unsigned int v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (168);
    a3 = 0;
    v_stack_m98 = 0;
    v_r15 = (*(unsigned __int64 *)(a1)) >> (9);
    v_r15 = (v_r15) & (result);
    v_stack_mA8 = 0;
    v_stack_m60 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m78 = *(unsigned __int64 *)(a1);
    v_r15 = (v_r15) + (result);
    v_stack_m90 = v_r15;
    v_rdi = (a2 + a2 * 2) << (4);
    v_rdi = (v_rdi) + (result);
    v_stack_mA0 = v_rdi;
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11446488) + result * 8);
    if (condition_is_below) goto loc_00345C49;
    v_stack_m88 = 0;
    v_stack_m70 = 0;
loc_003457E1:
    result = MiGetContainingPageTable(v_r15, a2, a3, a4);
    v_r13 = (result + result * 2) << (4);
    v_r13 = (v_r13) + (result);
    v_rsi = 0;
loc_00345805:
    if (condition_is_below) goto loc_00345BE0;
    a1 = (*(unsigned __int64 *)(v_r13 + 24)) & (a2);
    a1 = (a1) + 1;
    result = (*(unsigned __int64 *)(v_r13 + 24)) ^ (a1);
    result = (result) & (a2);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_r13 + 24) = result;
    if (v_r15 < result) goto loc_0034588E;
    if (v_r15 > result) goto loc_0034588E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_0034588E;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00345DBF;
loc_0034588E:
    if (condition_is_above_or_equal) goto loc_00345C09;
    if (*(unsigned __int64 *)(v_rip + 11437024) == 0) goto loc_003458B6;
    result = *(unsigned __int64 *)(v_r15);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11437024);
        result = ~(result);
        result = (result) & (*(unsigned __int64 *)(v_r15));
    }
    result = (result) >> (32);
    if (result != ((unsigned int)(0xFFFFFFFFULL))) goto loc_00345C09;
    v_rbx = (*(unsigned __int64 *)(v_r15)) >> (5);
    v_rbx = (unsigned int)((v_rbx) & (31));
loc_003458CF:
    if (((*(unsigned __int64 *)(v_rip + 13111726)) & (0x8000ULL)) != 0) goto loc_00345E05;
loc_00345904:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFFE7ULL));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) != 64) goto loc_003462D0;
loc_00345919:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (31));
    v_rdi = (*(unsigned __int64 *)(v_rip - 3362706 + v_rdi * 8)) & (v_rip - 3362706);
    result = (v_stack_p10) & (511);
    result = (result) << (12);
    v_rdi = (v_rdi) | (result);
    v_rdi = (v_rdi) | (33);
    if (v_r15 < 0) goto loc_00345BFF;
    if (v_r15 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00345BFF;
    if (v_r15 >= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00346073;
loc_0034598B:
    a1 = (v_r15) << (25);
loc_0034599F:
    result = ((unsigned int)(0xFFFFFFFFULL)) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    if (a1 <= 0) {
        v_rdi = (v_rdi) | (4);
    }
    result = MiIsAddressGlobal(a1, v_rdi, a3, 2);
    if ((unsigned int)(result) == 0) { v_rdi = v_rdi; }
loc_003459C6:
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) | (result);
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_00345EA9;
loc_003459EF:
    if (v_stack_p18 != 0) goto loc_00345EC4;
loc_003459FE:
    a4 = 0;
loc_00345A01:
    v_stack_m98 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_00345A89;
    v_stack_m80 = 0;
    if (condition_is_below) goto loc_00345A35;
    if (!sign_flag) goto loc_003462F6;
loc_00345A35:
    if (v_stack_m78 >= (*(unsigned __int64 *)(v_stack_mA0 + 8))) goto loc_0034639D;
    if (0 == 0) goto loc_00345E33;
    v_rbp = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 56)))) & (32)) != 0) {
        v_rbp = (unsigned int)((0) | (4));
    }
    if (((unsigned int)(v_rbp)) >= 4) goto loc_003460D0;
loc_00345A6E:
loc_00345A72:
loc_00345A77:
loc_00345A7C:
    if ((((unsigned __int8)(v_rbp)) & (2)) != 0) goto loc_00346202;
    a4 = 0;
loc_00345A89:
loc_00345A8E:
    v_r14 = 0;
    if ((((unsigned __int8)(v_rbp)) & (1)) == 0) { v_r14 = (unsigned int)(v_rbx); }
    result = (unsigned int)((a5) & (1));
    if (condition_is_not_equal) goto loc_00346351;
    a2 = (a5) & (-2);
loc_00345AB1:
    v_stack_p28 = 0;
    if (result != 0) goto loc_0034636B;
loc_00345AC8:
    if (v_stack_p18 != 0) goto loc_00346015;
loc_00345AD7:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 69))) & (16)) != 0) goto loc_00346328;
loc_00345AF1:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p8 + 16))) & (1)) != 0) goto loc_003462BA;
loc_00345AFD:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 69))) & (9));
    if (((unsigned __int8)(result)) != 8) goto loc_00345B7D;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 69))) & (4)) != 0) goto loc_00345B7D;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p8 + 56 + 10)) == 0) goto loc_00345B55;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p8 + 56 + 8)) + ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + 56 + 10))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m90))) >> (3));
    result = (unsigned int)((result) & (511));
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_00345B48;
    if (sign_flag) goto loc_00345E22;
    result = *(unsigned __int64 *)(v_stack_mA0 + 40);
    if (((*(unsigned __int8 *)(v_stack_p8 + 56 + 13)) & (2)) == 0) {
        a1 = v_stack_p8 + 56;
        result = MiEmptyDeferredWorkingSetEntries(a1, v_stack_m90, v_stack_mA0, v_stack_p8);
        a2 = v_stack_m90;
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p8 + 56 + 10)) == 0) goto loc_00345E7B;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p8 + 56 + 10)) + 1);
    *(unsigned __int16 *)(v_stack_p8 + 56 + 10) = (unsigned __int16)(result);
loc_00345B72:
    v_rsi = (unsigned int)((0) | (4));
loc_00345B7D:
    v_stack_mB8 = a5;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (16));
    if (((*(unsigned __int8 *)(v_stack_p8 + 56 + 13)) & (1)) == 0) { v_rbx = (unsigned int)(v_rsi); }
    v_stack_mC0 = (unsigned int)(v_rbx);
    v_stack_mC8 = v_rdi;
    result = MiAllocateWsle(v_stack_m60, v_stack_m90, v_stack_mA0, (unsigned int)((unsigned int)(v_r14)));
    if ((unsigned int)(result) == 0) goto loc_00346684;
    if ((((unsigned __int8)(v_rbp)) & (8)) != 0) goto loc_003463E2;
loc_00345BC3:
loc_00345BC6:
    v_rsp = (v_rsp) + (168);
    return 0;
loc_00345BE0:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13104836)) & ((unsigned int)(v_rbx))) == 0) goto loc_00346513;
loc_00345BEE:
loc_00345BF0:
    if (!sign_flag) goto loc_00345805;
    goto loc_00345BE0;
loc_00345BFF:
    goto loc_003459C6;
loc_00345C09:
    result = (v_r14) >> (5);
    result = (unsigned int)((result) & (31));
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) { result = 1; }
    if (v_stack_p100 == 0) goto loc_003458CF;
    v_r10 = v_stack_p100;
    if ((((unsigned __int8)(result)) & (4)) == 0) { v_r10 = v_rsi; }
    v_stack_p100 = v_r10;
    goto loc_003458CF;
loc_00345C49:
    if (*(unsigned __int64 *)(v_rip + 11436080) == 0) goto loc_00345C67;
    v_rsi = v_r14;
    if ((((unsigned __int8)(v_r14)) & (16)) == 0) {
        v_rsi = *(unsigned __int64 *)(v_rip + 11436080);
        v_rsi = ~(v_rsi);
        v_rsi = (v_rsi) & (v_r14);
    }
    v_rsi = (v_rsi) >> (16);
    v_stack_p60 = v_rsi;
    v_stack_p78 = *(unsigned __int64 *)(v_rsi);
    if ((*(unsigned int *)(v_rip + 11670999)) == 1) goto loc_003461A2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64))) & (15)) == 0) goto loc_00345CA8;
loc_00345C93:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64))) & (15)) == 0) goto loc_00345CA8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64))) & (15)) != 0) goto loc_00345C93;
loc_00345CA8:
    a2 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64)) & (15));
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64)) & (-16);
    if (((unsigned int)(a2)) <= ((unsigned int)(v_r10))) goto loc_003461AA;
loc_00345CBB:
    result = ObpTraceObjectReferenceIfActive(v_r12 - 48, (unsigned int)((unsigned int)(v_r10)), (unsigned int)(0x63536D4DULL), (unsigned int)((unsigned int)(v_r14)));
    if (v_r12 == 0) goto loc_003464EA;
loc_00345CD7:
    v_rbx = (*(unsigned __int64 *)(v_stack_p48 + 8)) | (result);
    result = MiGetSessionIdForVa(v_stack_p70, (unsigned int)((unsigned int)(v_r10)), (unsigned int)(0x63536D4DULL), (unsigned int)((unsigned int)(v_r14)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 56)))) & (32)) != 0) goto loc_00346166;
    if (*(unsigned __int64 *)(v_rsi + 8) == 0) goto loc_003466C1;
    v_rbx = (v_rbx) - (*(unsigned __int64 *)(v_rsi + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (12);
    a2 = 0;
loc_00345D21:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) & (0xFFC0ULL));
    a1 = (a1) << (26);
    result = ((unsigned int)(*(unsigned int *)(v_rsi + 36))) | (a1);
    result = (result) << (12);
    v_rbx = (v_rbx) + (result);
loc_00345D3B:
    v_rsi = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 56)))) & (32)) != 0) { v_rsi = 1; }
    result = PfSnReferenceProcessTrace(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, *(unsigned __int64 *)(v_rsi + 8), *(unsigned __int64 *)(v_rsi));
    if (result != 0) goto loc_00346794;
loc_00345D6C:
loc_00345D72:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64)) ^ (v_r12);
    if (a1 >= 15) goto loc_0034665B;
    if (a1 != 15) goto loc_00345D72;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 64);
    if ((*(unsigned int *)(v_rip + 13103741)) != 1) {
        a2 = 0;
        a1 = v_r12 - 48;
        a4 = 0x63536D4DULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    goto loc_003457E1;
loc_00345DBF:
    result = MiPteHasShadow(a1, a2, a3, a4);
    if (result == 0) goto loc_0034588E;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0034588E;
    result = (v_stack_p58) >> (3);
    result = (result) & (0);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_rbx) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_0034588E;
loc_00345E05:
    if (v_stack_p70 >= 0) goto loc_00346453;
loc_00345E13:
    goto loc_00345904;
loc_00345E22:
    if (((*(unsigned __int8 *)(v_stack_p60 + 13)) & (2)) != 0) goto loc_00345B48;
    goto loc_00345B55;
loc_00345E33:
    v_rbp = (unsigned int)((1) | (4));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640)) == 0) goto loc_00345A65;
    a2 = (*(unsigned __int64 *)(a2 + 8)) | (*(unsigned __int64 *)(gs_base + (0 + 392)));
    result = MiLocateCloneAddress(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, a4);
    if (result == 0) goto loc_00345A65;
    v_rbp = (unsigned int)((v_rbp) & (0xFFFFFFFBULL));
    goto loc_00345A65;
loc_00345E7B:
    *(unsigned __int16 *)(v_stack_p60 + 10) = 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (3));
    result = (unsigned __int16)((result) & ((unsigned __int16)(v_rbx)));
    *(unsigned __int16 *)(v_stack_p60 + 8) = (unsigned __int16)(result);
    if (!sign_flag) goto loc_00346346;
    goto loc_00345B72;
loc_00345EA9:
    v_rsi = (unsigned __int8)((v_rsi) & (5));
    if (((unsigned __int8)(v_rsi)) != 4) goto loc_003459EF;
    v_stack_p100 = 1;
loc_00345EC4:
    if ((*(unsigned __int64 *)(v_stack_pF0)) > a3) goto loc_00345EFA;
    if (!sign_flag) goto loc_003465F6;
loc_00345EEA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1912) != 0) goto loc_0034670E;
loc_00345EFA:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (5));
    if (((unsigned __int8)(result)) == 5) goto loc_003459FE;
    v_rdi = (v_stack_p48) | (66);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p48 + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_00345FDE;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_stack_p48 + 16), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00345FDE;
    a3 = 0;
loc_00345F4D:
    if (condition_is_below) goto loc_003466D0;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p48 + 34))) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_00345FAD;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p48 + 34))) & (8)) != 0) goto loc_00345FA0;
    v_stack_p80 = *(unsigned __int64 *)(v_stack_p48 + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(v_stack_p48 + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00346746;
    a2 = 0;
loc_00345FA0:
    result = MiSetPfnModified(v_stack_p48, 1, a3, a4);
loc_00345FAD:
    if (0 != 0) {
        a1 = v_stack_p90;
        a3 = 1;
        a2 = 0;
        result = MiReleasePageFileInfo(a1, a2, a3, a4);
    }
loc_00345FDE:
    if (condition_is_above_or_equal) goto loc_003459FE;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p88 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_003459FE;
    result = MiCheckAndUpdateIoAttribution(v_stack_p48, (unsigned int)(v_stack_p108), a3, a4);
    goto loc_003459FE;
loc_00346015:
    if (((unsigned __int8)(result)) < 1) goto loc_00345AD7;
    if (((unsigned __int8)(result)) >= 1) goto loc_00345AD7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624)) != 0) goto loc_00345AD7;
    if ((unsigned int)(v_stack_p108) != 0) goto loc_0034606B;
    if (((*(unsigned __int64 *)(v_rip + 13109807)) & (0x2000000ULL)) != 0) goto loc_0034606B;
    if (((*(unsigned __int8 *)(v_rip + 11434855)) & (1)) != 0) {
        v_rdi = (v_rdi) & (-33);
        v_rbp = (unsigned int)((v_rbp) | (16));
    }
    v_rbp = (unsigned int)((v_rbp) | (8));
    goto loc_00345AD7;
loc_00346073:
    if (v_stack_p48 > (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0034598B;
    if (v_stack_p48 == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00346649;
    v_rdi = (v_rdi) & (v_stack_p70);
loc_0034609C:
    result = MiUserPdeOrAbove(v_stack_p48, (unsigned int)(v_stack_p108), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0034672B;
    v_rdi = (v_rdi) | (4);
    a1 = (v_stack_p48) << (25);
    goto loc_0034599F;
loc_003460D0:
    v_stack_p68 = a4;
    v_stack_pF8 = a4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1088) == 0) goto loc_00345A72;
    result = MiLockVadTree(1, (unsigned int)(a4), a3, a4);
    result = MiLocateAddress(v_r14, (unsigned int)(a4), a3, a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    if (result == 0) goto loc_00346157;
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned __int8)(a1)) == 32) goto loc_0034653A;
loc_00346157:
    goto loc_00345A72;
loc_00346166:
    if (v_rbx < v_stack_pF8) goto loc_0034637C;
    if (v_rbx >= (v_stack_pF8 + (unsigned int)(*(unsigned int *)(0 + 44)) * 8)) goto loc_0034637C;
    a3 = (v_stack_pF8) << (9);
    v_rbx = (v_rbx) << (9);
    v_rbx = (v_rbx) - (a3);
loc_0034618A:
    v_rbx = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = ((unsigned int)(*(unsigned int *)(0 + 36))) << (9);
    v_rbx = (v_rbx) + (result);
    a2 = 0;
    goto loc_00345D3B;
loc_003461A2:
    goto loc_003457E1;
loc_003461AA:
    if (0 == 0) goto loc_003464EA;
    if (condition_is_less_or_equal) goto loc_003464CD;
loc_003461CD:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rdi)) & (15));
    a1 = (a1) + (15);
    if (a1 > 15) goto loc_0034673A;
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    if (0 != a1) goto loc_0034673A;
    if (0 == a1) goto loc_00345CBB;
    goto loc_003461CD;
loc_00346202:
    v_stack_p28 = 0;
    v_stack_p20 = a3;
    result = MiPrivateFixup(v_stack_pF0, *(unsigned __int64 *)(v_rdi), (unsigned int)((unsigned int)(v_r14)), v_stack_p48);
    result = MiLockAndDecrementShareCount(v_stack_p48, 2, (unsigned int)((unsigned int)(v_r14)), v_stack_p48);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 297) goto loc_00346308;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000009AULL) goto loc_00346308;
    if (sign_flag) goto loc_00345BC3;
    result = MiMakeTransitionPteValid(v_stack_p58, 2, (unsigned int)((unsigned int)(v_r14)), v_stack_p48);
    result = (result) >> (12);
    result = (result) & (v_stack_p58);
    a3 = (result + result * 2) << (4);
    a3 = (a3) + (result);
    v_stack_p48 = a3;
    if (v_stack_p70 >= result) goto loc_003466FC;
loc_003462AC:
    a4 = 0;
    v_rbp = (unsigned int)((v_rbp) & (0xFFFFFFFEULL));
    goto loc_00345A8E;
loc_003462BA:
    result = (result) & (-2);
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_00345AFD;
    v_rdi = (result) & (-33);
    goto loc_00345AFD;
loc_003462D0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    if (((unsigned __int8)(result)) < 64) goto loc_0034667C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) != 128) goto loc_00345919;
    v_rsi = (unsigned int)((0) | (24));
    goto loc_00345919;
loc_003462F6:
    if (*(unsigned __int64 *)(2 + 8) != 0) goto loc_00345A6E;
    goto loc_00345A35;
loc_00346308:
    result = MiLockAndDecrementShareCount(*(unsigned __int64 *)(gs_base + (0 + 392)), 2, a3, a4);
    v_r15 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 297) { v_r15 = (unsigned int)((unsigned int)(0xC0000434ULL)); }
    goto loc_00345BC3;
loc_00346328:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4 + 16))) & (1)) == 0) goto loc_0034633D;
    result = (*(unsigned __int64 *)(a4 + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 2) goto loc_00345AFD;
loc_0034633D:
    v_rdi = (v_rdi) & (-33);
    goto loc_00345AF1;
loc_00346346:
    goto loc_00345B72;
loc_00346351:
    a2 = (2) & (-2);
    v_stack_p110 = a2;
    if ((*(unsigned __int8 *)(a2)) != 5) goto loc_00345AB1;
    goto loc_00345AC8;
loc_0034636B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) != 3) goto loc_00345AC8;
    v_rsi = (unsigned int)((v_rsi) | (1));
    goto loc_00345AC8;
loc_0034637C:
    result = MiGetSharedProtos(0, (unsigned int)((unsigned int)(result)), v_rsi, a4);
    v_rbx = (0) << (9);
    a1 = (*(unsigned __int64 *)(result + 72)) << (9);
    v_rbx = (v_rbx) - (a1);
    goto loc_0034618A;
loc_0034639D:
    if (v_stack_p78 == 0) goto loc_003463B2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p78 + 56)))) & (32)) == 0) goto loc_00345A6E;
loc_003463B2:
    result = MiSystemImageHasPrivateFixups(2, v_stack_p68, v_stack_p50, a4);
    if (result == 0) goto loc_00345A6E;
    v_rbp = (unsigned int)((v_rbp) | (2));
    goto loc_00345A77;
loc_003463E2:
    a2 = 0;
    v_stack_p68 = 0;
    if ((*(unsigned __int64 *)(0 + 16)) == 0) goto loc_00346404;
    if (((*(unsigned __int8 *)(0 + 13)) & (1)) != 0) goto loc_00346404;
    if ((*(unsigned __int16 *)(0 + 10)) != 0) goto loc_003465E9;
loc_00346404:
    v_rbp = (unsigned int)((v_rbp) >> (1));
    v_rbp = (unsigned int)((v_rbp) & (8));
    v_stack_p20 = v_stack_p68;
    result = MiCopyOnWrite(v_stack_p70, v_rdi, -1, (unsigned int)((unsigned int)(v_rbp)));
    if (!sign_flag) goto loc_00345BC3;
    result = MiSetFaultPacketDirectives(v_stack_pF0, (unsigned int)((unsigned int)(result)), v_stack_p68, (unsigned int)((unsigned int)(v_rbp)));
    goto loc_00345BC6;
loc_00346453:
    if (v_stack_p70 >= v_stack_p68) goto loc_003465D8;
loc_0034645F:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_rbp)))) & ((unsigned __int8)(v_rbx))) == 0) goto loc_00345E13;
    a3 = 0;
    result = MiGetPagePrivilege(v_rdi, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbp)))), a3, (unsigned int)((unsigned int)(v_rbp)));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0034648D;
    if (((*(unsigned __int64 *)(v_rip + 13108737)) & (0x10000ULL)) == 0) goto loc_00346609;
loc_0034648D:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (1)) != 0) goto loc_00346637;
loc_00346496:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (8)) != 0) goto loc_003466F2;
loc_0034649F:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    if (condition_is_equal) { v_rbx = 1; }
loc_003464AA:
    goto loc_00345904;
loc_003464CD:
    a2 = 0;
    result = (1) + (15);
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, 0, 16);
loc_003464EA:
    result = ExAcquireSpinLockSharedAtDpcLevel(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72, a2, 0, 16);
    result = ObFastReferenceObjectLocked(v_rdi, (unsigned int)(0x63536D4DULL), 0, 16);
    result = MiReleaseSpinLockShared(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72, 17, 0, 16);
    goto loc_00345CD7;
loc_00346513:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13108639)))) & (64)) == 0) goto loc_00345BEE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72, 17, 0, 16);
    if ((unsigned __int8)(result) == 0) goto loc_00345BEE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), 17, 0, 16);
    goto loc_00345BF0;
loc_0034653A:
    if (condition_is_below) goto loc_00346157;
    if (condition_is_above_or_equal) goto loc_00346157;
    a1 = (*(unsigned __int8 *)(result + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 24)));
    result = (v_stack_p70) >> (12);
    v_r14 = (*(unsigned __int64 *)(result + 80)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 136));
    v_r14 = (v_r14) >> (3);
    v_r14 = (v_r14) - (a1);
    v_r14 = (v_r14) + (result);
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> (3);
    a1 = (unsigned __int8)(((unsigned __int8)(v_r14)) & (7));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(result + 160) * 1)) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_00346157;
    a2 = (v_r14) << (12);
    result = MiOffsetToProtos(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)), a2, v_stack_p68, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    v_rbp = (unsigned int)((v_rbp) | (2));
    goto loc_00345A7C;
loc_003465D8:
    if (v_stack_p70 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)))) goto loc_00345E13;
    goto loc_0034645F;
loc_003465E9:
    result = MiEmptyDeferredWorkingSetEntries(result, (unsigned int)(*(unsigned int *)(result + 136)), *(unsigned __int64 *)(result + 144), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    goto loc_00346404;
loc_003465F6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 500)))) & (16)) == 0) goto loc_00345EEA;
    goto loc_0034671B;
loc_00346609:
    if (!sign_flag) goto loc_00346496;
    if (condition_is_below) goto loc_0034648D;
    a2 = 0;
    result = MiIsDriverPage((unsigned int)((unsigned int)(result)), a2, *(unsigned __int64 *)(result + 144), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    if (result == 0) goto loc_0034649F;
loc_00346637:
loc_0034663C:
    v_stack_p100 = v_rsi;
    goto loc_003464AA;
loc_00346649:
    v_rdi = (v_rdi) | (result);
    goto loc_0034609C;
loc_0034665B:
    result = ObDereferenceObjectDeferDeleteWithTag(result, (unsigned int)(0x63536D4DULL), *(unsigned __int64 *)(result + 144), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    goto loc_003457E1;
loc_0034667C:
    v_rsi = (unsigned int)((v_rsi) | (8));
    goto loc_00345919;
loc_00346684:
    if (((3) & (4)) != 0) {
        result = 0xFFFFULL;
    }
    result = MiLockAndDecrementShareCount(v_stack_p48, 2, *(unsigned __int64 *)(result + 144), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    if ((((unsigned __int8)(v_rbp)) & (2)) == 0) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = MiLockAndDecrementShareCount(a1, a2, *(unsigned __int64 *)(result + 144), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)));
    }
    goto loc_00345BC3;
loc_003466C1:
    a2 = 0;
    goto loc_00345D21;
loc_003466D0:
    v_r15 = (unsigned int)(((unsigned int)(0xC0000017ULL)) + 1);
    if (((*(unsigned int *)(v_rip + 13102034)) & ((unsigned int)(v_r15))) == 0) goto loc_0034676C;
loc_003466E0:
loc_003466E2:
    if (!sign_flag) goto loc_00345F4D;
    goto loc_003466D0;
loc_003466F2:
    goto loc_0034663C;
loc_003466FC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 144) + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) { v_rsi = (unsigned int)(v_r14); }
    goto loc_003462AC;
loc_0034670E:
    result = (result) + (24);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_00345EFA;
loc_0034671B:
    a4 = 0;
    v_stack_p100 = 0;
    goto loc_00345A01;
loc_0034672B:
    goto loc_0034598B;
loc_0034673A:
    goto loc_00345CBB;
loc_00346746:
    result = (*(unsigned __int64 *)(v_r15 + 16)) & (-5);
    *(unsigned __int64 *)(v_r15 + 16) = result;
    result = MiClearPageFileReservation(v_stack_p80, a2, *(unsigned __int64 *)(result + 144), a4);
    goto loc_00345FA0;
loc_0034676C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13108038)))) & (64)) == 0) goto loc_003466E0;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p80, a2, *(unsigned __int64 *)(result + 144), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003466E0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), a2, *(unsigned __int64 *)(result + 144), a4);
    goto loc_003466E2;
loc_00346794:
    result = PfSnCheckLoggingForThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_r15, (unsigned int)((unsigned int)(v_stack_p80)), a4);
    if ((unsigned int)(result) != 0) {
        a3 = *(unsigned __int64 *)(v_stack_p60 + 24);
        a4 = 1;
        a2 = v_stack_p60;
        v_stack_p20 = (unsigned int)(v_stack_p80);
        a1 = v_r15;
        result = PfSnLogPageFaultCommon(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(v_r15 + 360)) & (-2);
    if (condition_is_equal) goto loc_00345D6C;
    result = ExfReleaseRundownProtection(v_r15 + 360, result - 2, a3, a4);
    goto loc_00345D6C;
}
```

## 5. (Beta) C Style

```c
int64_t MiCompleteProtoPteFault(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

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
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p100;
    uint32_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (168);
    Arg3 = 0;
    v_stack_m98 = 0;
    local_r15 = (*(uint64_t *)(arg1)) >> (9);
    local_r15 = (local_r15) & (result);
    v_stack_mA8 = 0;
    v_stack_m60 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m78 = *(uint64_t *)(arg1);
    local_r15 = (local_r15) + (result);
    v_stack_m90 = local_r15;
    local_rdi = (Arg2 + Arg2 * 2) << (4);
    local_rdi = (local_rdi) + (result);
    v_stack_mA0 = local_rdi;
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAEA8D8) + result * 8);
    if (condition_is_below) goto loc_00345C49;
    v_stack_m88 = 0;
    v_stack_m70 = 0;
loc_003457E1:
    result = MiGetContainingPageTable(local_r15, Arg2, Arg3, Arg4);
    local_r13 = (result + result * 2) << (4);
    local_r13 = (local_r13) + (result);
    local_rsi = 0;
loc_00345805:
    if (condition_is_below) goto loc_00345BE0;
    Arg1 = (*(uint64_t *)(local_r13 + 0x18)) & (Arg2);
    Arg1 = (Arg1) + 1;
    result = (*(uint64_t *)(local_r13 + 0x18)) ^ (Arg1);
    result = (result) & (Arg2);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_r13 + 0x18) = result;
    if (local_r15 < result) goto loc_0034588E;
    if (local_r15 > result) goto loc_0034588E;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_0034588E;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r15))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00345DBF;
loc_0034588E:
    if (condition_is_above_or_equal) goto loc_00345C09;
    if (*(uint64_t *)(v_rip + 0xAE83E0) == 0) goto loc_003458B6;
    result = *(uint64_t *)(local_r15);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xAE83E0);
        result = ~(result);
        result = (result) & (*(uint64_t *)(local_r15));
    }
    result = (result) >> (32);
    if (result != ((uint32_t)(0xFFFFFFFFULL))) goto loc_00345C09;
    local_rbx = (*(uint64_t *)(local_r15)) >> (5);
    local_rbx = (uint32_t)((local_rbx) & (31));
loc_003458CF:
    if (((*(uint64_t *)(v_rip + 0xC811AE)) & (0x8000ULL)) != 0) goto loc_00345E05;
loc_00345904:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFFE7ULL));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) != 64) goto loc_003462D0;
loc_00345919:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (31));
    local_rdi = (*(uint64_t *)(v_rip - 0x334F92 + local_rdi * 8)) & (v_rip - 3362706);
    result = (v_stack_p10) & (511);
    result = (result) << (12);
    local_rdi = (local_rdi) | (result);
    local_rdi = (local_rdi) | (33);
    if (local_r15 < 0) goto loc_00345BFF;
    if (local_r15 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00345BFF;
    if (local_r15 >= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00346073;
loc_0034598B:
    Arg1 = (local_r15) << (25);
loc_0034599F:
    result = ((uint32_t)(0xFFFFFFFFULL)) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    if (Arg1 <= 0) {
        local_rdi = (local_rdi) | (4);
    }
    result = MiIsAddressGlobal(Arg1, local_rdi, Arg3, 2);
    if ((uint32_t)(result) == 0) { local_rdi = local_rdi; }
loc_003459C6:
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) | (result);
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_00345EA9;
loc_003459EF:
    if (v_stack_p18 != 0) goto loc_00345EC4;
loc_003459FE:
    Arg4 = 0;
loc_00345A01:
    v_stack_m98 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_00345A89;
    v_stack_m80 = 0;
    if (condition_is_below) goto loc_00345A35;
    if (!sign_flag) goto loc_003462F6;
loc_00345A35:
    if (v_stack_m78 >= (*(uint64_t *)(v_stack_mA0 + 0x8))) goto loc_0034639D;
    if (0 == 0) goto loc_00345E33;
    local_rbp = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x38)))) & (32)) != 0) {
        local_rbp = (uint32_t)((0) | (4));
    }
    if (((uint32_t)(local_rbp)) >= 4) goto loc_003460D0;
loc_00345A6E:
loc_00345A72:
loc_00345A77:
loc_00345A7C:
    if ((((uint8_t)(local_rbp)) & (2)) != 0) goto loc_00346202;
    Arg4 = 0;
loc_00345A89:
loc_00345A8E:
    local_r14 = 0;
    if ((((uint8_t)(local_rbp)) & (1)) == 0) { local_r14 = (uint32_t)(local_rbx); }
    result = (uint32_t)((Arg5) & (1));
    if (condition_is_not_equal) goto loc_00346351;
    Arg2 = (Arg5) & (-2);
loc_00345AB1:
    v_stack_p28 = 0;
    if (result != 0) goto loc_0034636B;
loc_00345AC8:
    if (v_stack_p18 != 0) goto loc_00346015;
loc_00345AD7:
    if ((((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x45))) & (16)) != 0) goto loc_00346328;
loc_00345AF1:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p8 + 0x10))) & (1)) != 0) goto loc_003462BA;
loc_00345AFD:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x45))) & (9));
    if (((uint8_t)(result)) != 8) goto loc_00345B7D;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x45))) & (4)) != 0) goto loc_00345B7D;
    if ((uint16_t)(*(uint16_t *)(v_stack_p8 + 0x38 + 0xA)) == 0) goto loc_00345B55;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p8 + 0x38 + 0x8)) + ((uint32_t)(*(uint16_t *)(v_stack_p8 + 0x38 + 0xA))));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m90))) >> (3));
    result = (uint32_t)((result) & (511));
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_00345B48;
    if (sign_flag) goto loc_00345E22;
    result = *(uint64_t *)(v_stack_mA0 + 0x28);
    if (((*(uint8_t *)(v_stack_p8 + 0x38 + 0xD)) & (2)) == 0) {
        Arg1 = v_stack_p8 + 56;
        result = MiEmptyDeferredWorkingSetEntries(Arg1, v_stack_m90, v_stack_mA0, v_stack_p8);
        Arg2 = v_stack_m90;
    }
    if ((uint16_t)(*(uint16_t *)(v_stack_p8 + 0x38 + 0xA)) == 0) goto loc_00345E7B;
    result = (uint16_t)((*(uint16_t *)(v_stack_p8 + 0x38 + 0xA)) + 1);
    *(uint16_t *)(v_stack_p8 + 0x38 + 0xA) = (uint16_t)(result);
loc_00345B72:
    local_rsi = (uint32_t)((0) | (4));
loc_00345B7D:
    v_stack_mB8 = Arg5;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (16));
    if (((*(uint8_t *)(v_stack_p8 + 0x38 + 0xD)) & (1)) == 0) { local_rbx = (uint32_t)(local_rsi); }
    v_stack_mC0 = (uint32_t)(local_rbx);
    v_stack_mC8 = local_rdi;
    result = MiAllocateWsle(v_stack_m60, v_stack_m90, v_stack_mA0, (uint32_t)((uint32_t)(local_r14)));
    if ((uint32_t)(result) == 0) goto loc_00346684;
    if ((((uint8_t)(local_rbp)) & (8)) != 0) goto loc_003463E2;
loc_00345BC3:
loc_00345BC6:
    local_rsp = (local_rsp) + (168);
    return 0;
loc_00345BE0:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xC7F6C4)) & ((uint32_t)(local_rbx))) == 0) goto loc_00346513;
loc_00345BEE:
loc_00345BF0:
    if (!sign_flag) goto loc_00345805;
    goto loc_00345BE0;
loc_00345BFF:
    goto loc_003459C6;
loc_00345C09:
    result = (local_r14) >> (5);
    result = (uint32_t)((result) & (31));
    if ((((uint8_t)(local_rbx)) & (8)) != 0) { result = 1; }
    if (v_stack_p100 == 0) goto loc_003458CF;
    local_r10 = v_stack_p100;
    if ((((uint8_t)(result)) & (4)) == 0) { local_r10 = local_rsi; }
    v_stack_p100 = local_r10;
    goto loc_003458CF;
loc_00345C49:
    if (*(uint64_t *)(v_rip + 0xAE8030) == 0) goto loc_00345C67;
    local_rsi = local_r14;
    if ((((uint8_t)(local_r14)) & (16)) == 0) {
        local_rsi = *(uint64_t *)(v_rip + 0xAE8030);
        local_rsi = ~(local_rsi);
        local_rsi = (local_rsi) & (local_r14);
    }
    local_rsi = (local_rsi) >> (16);
    v_stack_p60 = local_rsi;
    v_stack_p78 = *(uint64_t *)(local_rsi);
    if ((*(uint32_t *)(v_rip + 0xB215D7)) == 1) goto loc_003461A2;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40))) & (15)) == 0) goto loc_00345CA8;
loc_00345C93:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40))) & (15)) == 0) goto loc_00345CA8;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40))) & (15)) != 0) goto loc_00345C93;
loc_00345CA8:
    Arg2 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40)) & (15));
    local_r12 = (*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40)) & (-16);
    if (((uint32_t)(Arg2)) <= ((uint32_t)(local_r10))) goto loc_003461AA;
loc_00345CBB:
    result = ObpTraceObjectReferenceIfActive(local_r12 - 48, (uint32_t)((uint32_t)(local_r10)), (uint32_t)(0x63536D4DULL), (uint32_t)((uint32_t)(local_r14)));
    if (local_r12 == 0) goto loc_003464EA;
loc_00345CD7:
    local_rbx = (*(uint64_t *)(v_stack_p48 + 0x8)) | (result);
    result = MiGetSessionIdForVa(v_stack_p70, (uint32_t)((uint32_t)(local_r10)), (uint32_t)(0x63536D4DULL), (uint32_t)((uint32_t)(local_r14)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x38)))) & (32)) != 0) goto loc_00346166;
    if (*(uint64_t *)(local_rsi + 0x8) == 0) goto loc_003466C1;
    local_rbx = (local_rbx) - (*(uint64_t *)(local_rsi + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (12);
    Arg2 = 0;
loc_00345D21:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) & (0xFFC0ULL));
    Arg1 = (Arg1) << (26);
    result = ((uint32_t)(*(uint32_t *)(local_rsi + 0x24))) | (Arg1);
    result = (result) << (12);
    local_rbx = (local_rbx) + (result);
loc_00345D3B:
    local_rsi = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x38)))) & (32)) != 0) { local_rsi = 1; }
    result = PfSnReferenceProcessTrace(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, *(uint64_t *)(local_rsi + 0x8), *(uint64_t *)(local_rsi));
    if (result != 0) goto loc_00346794;
loc_00345D6C:
loc_00345D72:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40)) ^ (local_r12);
    if (Arg1 >= 15) goto loc_0034665B;
    if (Arg1 != 15) goto loc_00345D72;
    result = *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x40);
    if ((*(uint32_t *)(v_rip + 0xC7F27D)) != 1) {
        Arg2 = 0;
        Arg1 = local_r12 - 48;
        Arg4 = 0x63536D4DULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_003457E1;
loc_00345DBF:
    result = MiPteHasShadow(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0034588E;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0034588E;
    result = (v_stack_p58) >> (3);
    result = (result) & (0);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (local_rbx) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_0034588E;
loc_00345E05:
    if (v_stack_p70 >= 0) goto loc_00346453;
loc_00345E13:
    goto loc_00345904;
loc_00345E22:
    if (((*(uint8_t *)(v_stack_p60 + 0xD)) & (2)) != 0) goto loc_00345B48;
    goto loc_00345B55;
loc_00345E33:
    local_rbp = (uint32_t)((1) | (4));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280)) == 0) goto loc_00345A65;
    Arg2 = (*(uint64_t *)(arg2 + 0x8)) | (*(uint64_t *)(gs_base + (0 + 0x188)));
    result = MiLocateCloneAddress(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00345A65;
    local_rbp = (uint32_t)((local_rbp) & (0xFFFFFFFBULL));
    goto loc_00345A65;
loc_00345E7B:
    *(uint16_t *)(v_stack_p60 + 0xA) = 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) >> (3));
    result = (uint16_t)((result) & ((uint16_t)(local_rbx)));
    *(uint16_t *)(v_stack_p60 + 0x8) = (uint16_t)(result);
    if (!sign_flag) goto loc_00346346;
    goto loc_00345B72;
loc_00345EA9:
    local_rsi = (uint8_t)((local_rsi) & (5));
    if (((uint8_t)(local_rsi)) != 4) goto loc_003459EF;
    v_stack_p100 = 1;
loc_00345EC4:
    if ((*(uint64_t *)(v_stack_pF0)) > Arg3) goto loc_00345EFA;
    if (!sign_flag) goto loc_003465F6;
loc_00345EEA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x778) != 0) goto loc_0034670E;
loc_00345EFA:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (5));
    if (((uint8_t)(result)) == 5) goto loc_003459FE;
    local_rdi = (v_stack_p48) | (66);
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_p48 + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_00345FDE;
    result = MiGetPagingFileOffset(*(uint64_t *)(v_stack_p48 + 0x10), Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00345FDE;
    Arg3 = 0;
loc_00345F4D:
    if (condition_is_below) goto loc_003466D0;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p48 + 0x22))) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_00345FAD;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p48 + 0x22))) & (8)) != 0) goto loc_00345FA0;
    v_stack_p80 = *(uint64_t *)(v_stack_p48 + 0x10);
    result = (uint8_t)((*(uint64_t *)(v_stack_p48 + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00346746;
    Arg2 = 0;
loc_00345FA0:
    result = MiSetPfnModified(v_stack_p48, 1, Arg3, Arg4);
loc_00345FAD:
    if (0 != 0) {
        Arg1 = v_stack_p90;
        Arg3 = 1;
        Arg2 = 0;
        result = MiReleasePageFileInfo(Arg1, Arg2, Arg3, Arg4);
    }
loc_00345FDE:
    if (condition_is_above_or_equal) goto loc_003459FE;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p88 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_003459FE;
    result = MiCheckAndUpdateIoAttribution(v_stack_p48, (uint32_t)(v_stack_p108), Arg3, Arg4);
    goto loc_003459FE;
loc_00346015:
    if (((uint8_t)(result)) < 1) goto loc_00345AD7;
    if (((uint8_t)(result)) >= 1) goto loc_00345AD7;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270)) != 0) goto loc_00345AD7;
    if ((uint32_t)(v_stack_p108) != 0) goto loc_0034606B;
    if (((*(uint64_t *)(v_rip + 0xC80A2F)) & (0x2000000ULL)) != 0) goto loc_0034606B;
    if (((*(uint8_t *)(v_rip + 0xAE7B67)) & (1)) != 0) {
        local_rdi = (local_rdi) & (-33);
        local_rbp = (uint32_t)((local_rbp) | (16));
    }
    local_rbp = (uint32_t)((local_rbp) | (8));
    goto loc_00345AD7;
loc_00346073:
    if (v_stack_p48 > (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0034598B;
    if (v_stack_p48 == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00346649;
    local_rdi = (local_rdi) & (v_stack_p70);
loc_0034609C:
    result = MiUserPdeOrAbove(v_stack_p48, (uint32_t)(v_stack_p108), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0034672B;
    local_rdi = (local_rdi) | (4);
    Arg1 = (v_stack_p48) << (25);
    goto loc_0034599F;
loc_003460D0:
    v_stack_p68 = Arg4;
    v_stack_pF8 = Arg4;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x440) == 0) goto loc_00345A72;
    result = MiLockVadTree(1, (uint32_t)(Arg4), Arg3, Arg4);
    result = MiLocateAddress(local_r14, (uint32_t)(Arg4), Arg3, Arg4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    if (result == 0) goto loc_00346157;
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint8_t)(Arg1)) == 32) goto loc_0034653A;
loc_00346157:
    goto loc_00345A72;
loc_00346166:
    if (local_rbx < v_stack_pF8) goto loc_0034637C;
    if (local_rbx >= (v_stack_pF8 + (uint32_t)(*(uint32_t *)(0 + 0x2C)) * 8)) goto loc_0034637C;
    Arg3 = (v_stack_pF8) << (9);
    local_rbx = (local_rbx) << (9);
    local_rbx = (local_rbx) - (Arg3);
loc_0034618A:
    local_rbx = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = ((uint32_t)(*(uint32_t *)(0 + 0x24))) << (9);
    local_rbx = (local_rbx) + (result);
    Arg2 = 0;
    goto loc_00345D3B;
loc_003461A2:
    goto loc_003457E1;
loc_003461AA:
    if (0 == 0) goto loc_003464EA;
    if (condition_is_less_or_equal) goto loc_003464CD;
loc_003461CD:
    Arg1 = (uint32_t)((*(uint64_t *)(local_rdi)) & (15));
    Arg1 = (Arg1) + (15);
    if (Arg1 > 15) goto loc_0034673A;
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    if (0 != Arg1) goto loc_0034673A;
    if (0 == Arg1) goto loc_00345CBB;
    goto loc_003461CD;
loc_00346202:
    v_stack_p28 = 0;
    v_stack_p20 = Arg3;
    result = MiPrivateFixup(v_stack_pF0, *(uint64_t *)(local_rdi), (uint32_t)((uint32_t)(local_r14)), v_stack_p48);
    result = MiLockAndDecrementShareCount(v_stack_p48, 2, (uint32_t)((uint32_t)(local_r14)), v_stack_p48);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 297) goto loc_00346308;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000009AULL) goto loc_00346308;
    if (sign_flag) goto loc_00345BC3;
    result = MiMakeTransitionPteValid(v_stack_p58, 2, (uint32_t)((uint32_t)(local_r14)), v_stack_p48);
    result = (result) >> (12);
    result = (result) & (v_stack_p58);
    Arg3 = (result + result * 2) << (4);
    Arg3 = (Arg3) + (result);
    v_stack_p48 = Arg3;
    if (v_stack_p70 >= result) goto loc_003466FC;
loc_003462AC:
    Arg4 = 0;
    local_rbp = (uint32_t)((local_rbp) & (0xFFFFFFFEULL));
    goto loc_00345A8E;
loc_003462BA:
    result = (result) & (-2);
    if ((*(uint8_t *)(result)) != 1) goto loc_00345AFD;
    local_rdi = (result) & (-33);
    goto loc_00345AFD;
loc_003462D0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    if (((uint8_t)(result)) < 64) goto loc_0034667C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) != 128) goto loc_00345919;
    local_rsi = (uint32_t)((0) | (24));
    goto loc_00345919;
loc_003462F6:
    if (*(uint64_t *)(2 + 0x8) != 0) goto loc_00345A6E;
    goto loc_00345A35;
loc_00346308:
    result = MiLockAndDecrementShareCount(*(uint64_t *)(gs_base + (0 + 0x188)), 2, Arg3, Arg4);
    local_r15 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 297) { local_r15 = (uint32_t)((uint32_t)(0xC0000434ULL)); }
    goto loc_00345BC3;
loc_00346328:
    if ((((uint8_t)(*(uint64_t *)(Arg4 + 0x10))) & (1)) == 0) goto loc_0034633D;
    result = (*(uint64_t *)(Arg4 + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 2) goto loc_00345AFD;
loc_0034633D:
    local_rdi = (local_rdi) & (-33);
    goto loc_00345AF1;
loc_00346346:
    goto loc_00345B72;
loc_00346351:
    Arg2 = (2) & (-2);
    v_stack_p110 = Arg2;
    if ((*(uint8_t *)(arg2)) != 5) goto loc_00345AB1;
    goto loc_00345AC8;
loc_0034636B:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) != 3) goto loc_00345AC8;
    local_rsi = (uint32_t)((local_rsi) | (1));
    goto loc_00345AC8;
loc_0034637C:
    result = MiGetSharedProtos(0, (uint32_t)((uint32_t)(result)), local_rsi, Arg4);
    local_rbx = (0) << (9);
    Arg1 = (*(uint64_t *)(result + 0x48)) << (9);
    local_rbx = (local_rbx) - (Arg1);
    goto loc_0034618A;
loc_0034639D:
    if (v_stack_p78 == 0) goto loc_003463B2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x38)))) & (32)) == 0) goto loc_00345A6E;
loc_003463B2:
    result = MiSystemImageHasPrivateFixups(2, v_stack_p68, v_stack_p50, Arg4);
    if (result == 0) goto loc_00345A6E;
    local_rbp = (uint32_t)((local_rbp) | (2));
    goto loc_00345A77;
loc_003463E2:
    Arg2 = 0;
    v_stack_p68 = 0;
    if ((*(uint64_t *)(0 + 0x10)) == 0) goto loc_00346404;
    if (((*(uint8_t *)(0 + 0xD)) & (1)) != 0) goto loc_00346404;
    if ((*(uint16_t *)(0 + 0xA)) != 0) goto loc_003465E9;
loc_00346404:
    local_rbp = (uint32_t)((local_rbp) >> (1));
    local_rbp = (uint32_t)((local_rbp) & (8));
    v_stack_p20 = v_stack_p68;
    result = MiCopyOnWrite(v_stack_p70, local_rdi, -1, (uint32_t)((uint32_t)(local_rbp)));
    if (!sign_flag) goto loc_00345BC3;
    result = MiSetFaultPacketDirectives(v_stack_pF0, (uint32_t)((uint32_t)(result)), v_stack_p68, (uint32_t)((uint32_t)(local_rbp)));
    goto loc_00345BC6;
loc_00346453:
    if (v_stack_p70 >= v_stack_p68) goto loc_003465D8;
loc_0034645F:
    if ((((uint8_t)((uint32_t)((uint32_t)(local_rbp)))) & ((uint8_t)(local_rbx))) == 0) goto loc_00345E13;
    Arg3 = 0;
    result = MiGetPagePrivilege(local_rdi, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbp)))), Arg3, (uint32_t)((uint32_t)(local_rbp)));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0034648D;
    if (((*(uint64_t *)(v_rip + 0xC80601)) & (0x10000ULL)) == 0) goto loc_00346609;
loc_0034648D:
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (1)) != 0) goto loc_00346637;
loc_00346496:
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (8)) != 0) goto loc_003466F2;
loc_0034649F:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    if (condition_is_equal) { local_rbx = 1; }
loc_003464AA:
    goto loc_00345904;
loc_003464CD:
    Arg2 = 0;
    result = (1) + (15);
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, 0, 16);
loc_003464EA:
    result = ExAcquireSpinLockSharedAtDpcLevel(*(uint64_t *)(gs_base + (0 + 0x188)) + 72, Arg2, 0, 16);
    result = ObFastReferenceObjectLocked(local_rdi, (uint32_t)(0x63536D4DULL), 0, 16);
    result = MiReleaseSpinLockShared(*(uint64_t *)(gs_base + (0 + 0x188)) + 72, 17, 0, 16);
    goto loc_00345CD7;
loc_00346513:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8059F)))) & (64)) == 0) goto loc_00345BEE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x188)) + 72, 17, 0, 16);
    if ((uint8_t)(result) == 0) goto loc_00345BEE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), 17, 0, 16);
    goto loc_00345BF0;
loc_0034653A:
    if (condition_is_below) goto loc_00346157;
    if (condition_is_above_or_equal) goto loc_00346157;
    Arg1 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    result = (v_stack_p70) >> (12);
    local_r14 = (*(uint64_t *)(result + 0x50)) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x88));
    local_r14 = (local_r14) >> (3);
    local_r14 = (local_r14) - (Arg1);
    local_r14 = (local_r14) + (result);
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> (3);
    Arg1 = (uint8_t)(((uint8_t)(local_r14)) & (7));
    Arg2 = (uint8_t)((*(uint8_t *)(arg2 + *(uint64_t *)(result + 0xA0) * 1)) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_00346157;
    Arg2 = (local_r14) << (12);
    result = MiOffsetToProtos(*(uint64_t *)(*(uint64_t *)(result + 0x48)), Arg2, v_stack_p68, *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    local_rbp = (uint32_t)((local_rbp) | (2));
    goto loc_00345A7C;
loc_003465D8:
    if (v_stack_p70 <= (*(uint64_t *)(*(uint64_t *)(result + 0x48)))) goto loc_00345E13;
    goto loc_0034645F;
loc_003465E9:
    result = MiEmptyDeferredWorkingSetEntries(result, (uint32_t)(*(uint32_t *)(result + 0x88)), *(uint64_t *)(result + 0x90), *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    goto loc_00346404;
loc_003465F6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1F4)))) & (16)) == 0) goto loc_00345EEA;
    goto loc_0034671B;
loc_00346609:
    if (!sign_flag) goto loc_00346496;
    if (condition_is_below) goto loc_0034648D;
    Arg2 = 0;
    result = MiIsDriverPage((uint32_t)((uint32_t)(result)), Arg2, *(uint64_t *)(result + 0x90), *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    if (result == 0) goto loc_0034649F;
loc_00346637:
loc_0034663C:
    v_stack_p100 = local_rsi;
    goto loc_003464AA;
loc_00346649:
    local_rdi = (local_rdi) | (result);
    goto loc_0034609C;
loc_0034665B:
    result = ObDereferenceObjectDeferDeleteWithTag(result, (uint32_t)(0x63536D4DULL), *(uint64_t *)(result + 0x90), *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    goto loc_003457E1;
loc_0034667C:
    local_rsi = (uint32_t)((local_rsi) | (8));
    goto loc_00345919;
loc_00346684:
    if (((3) & (4)) != 0) {
        result = 0xFFFFULL;
    }
    result = MiLockAndDecrementShareCount(v_stack_p48, 2, *(uint64_t *)(result + 0x90), *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    if ((((uint8_t)(local_rbp)) & (2)) == 0) {
        Arg2 = 2;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = MiLockAndDecrementShareCount(Arg1, Arg2, *(uint64_t *)(result + 0x90), *(uint64_t *)(*(uint64_t *)(result + 0x48)));
    }
    goto loc_00345BC3;
loc_003466C1:
    Arg2 = 0;
    goto loc_00345D21;
loc_003466D0:
    local_r15 = (uint32_t)(((uint32_t)(0xC0000017ULL)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC7EBD2)) & ((uint32_t)(local_r15))) == 0) goto loc_0034676C;
loc_003466E0:
loc_003466E2:
    if (!sign_flag) goto loc_00345F4D;
    goto loc_003466D0;
loc_003466F2:
    goto loc_0034663C;
loc_003466FC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x90) + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) { local_rsi = (uint32_t)(local_r14); }
    goto loc_003462AC;
loc_0034670E:
    result = (result) + (24);
    if ((*(uint64_t *)(result)) == result) goto loc_00345EFA;
loc_0034671B:
    Arg4 = 0;
    v_stack_p100 = 0;
    goto loc_00345A01;
loc_0034672B:
    goto loc_0034598B;
loc_0034673A:
    goto loc_00345CBB;
loc_00346746:
    result = (*(uint64_t *)(local_r15 + 0x10)) & (-5);
    *(uint64_t *)(local_r15 + 0x10) = result;
    result = MiClearPageFileReservation(v_stack_p80, Arg2, *(uint64_t *)(result + 0x90), Arg4);
    goto loc_00345FA0;
loc_0034676C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC80346)))) & (64)) == 0) goto loc_003466E0;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p80, Arg2, *(uint64_t *)(result + 0x90), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003466E0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), Arg2, *(uint64_t *)(result + 0x90), Arg4);
    goto loc_003466E2;
loc_00346794:
    result = PfSnCheckLoggingForThread(*(uint64_t *)(gs_base + (0 + 0x188)), local_r15, (uint32_t)((uint32_t)(v_stack_p80)), Arg4);
    if ((uint32_t)(result) != 0) {
        Arg3 = *(uint64_t *)(v_stack_p60 + 0x18);
        Arg4 = 1;
        Arg2 = v_stack_p60;
        v_stack_p20 = (uint32_t)(v_stack_p80);
        Arg1 = local_r15;
        result = PfSnLogPageFaultCommon(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(local_r15 + 0x168)) & (-2);
    if (condition_is_equal) goto loc_00345D6C;
    result = ExfReleaseRundownProtection(local_r15 + 360, result - 2, Arg3, Arg4);
    goto loc_00345D6C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x0 + rdx*2` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00345710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
