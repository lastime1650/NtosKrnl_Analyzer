# RtlAvlRemoveNode

- RVA: `0x00296650`–`0x00296A48` (길이 `1,016` bytes)
- VA: `0x0000000140296650`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067900`
- 디코드: `281`개 명령, `1,016/1,016` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **56**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00296958` → [RtlpTreeDoubleRotateNodes](RtlpTreeDoubleRotateNodes_function_00296C74.md) (function, `0x00296C74`)

### Direct callers
- [MiCloneVads](../22/MiCloneVads_function_0022DC1C.md) at `0x0022E04E`
- [MiRemoveVad](MiRemoveVad_function_00295C78.md) at `0x00295DAA`
- [MiUpdateSystemProtoPtesTree](MiUpdateSystemProtoPtesTree_function_00295F0C.md) at `0x002960DE`
- [MiRemoveFromSystemSpace](MiRemoveFromSystemSpace_function_002962FC.md) at `0x0029640A`
- [MiFreeCombineBlock](../37/MiFreeCombineBlock_function_00372000.md) at `0x003720AD`
- [MiFlowThroughRemoveNode](../38/MiFlowThroughRemoveNode_function_00381BB0.md) at `0x00381C08`
- [MiFreeMdlTracker](../49/MiFreeMdlTracker_function_00494838.md) at `0x00494920`
- [MiRemoveMappingNode](../4A/MiRemoveMappingNode_function_004AC85C.md) at `0x004AC8AE`
- [MiUpdatePerSessionProto](../4A/MiUpdatePerSessionProto_function_004AD938.md) at `0x004AD977`
- [MiDeleteDeferredCloneDescriptors](../4D/MiDeleteDeferredCloneDescriptors_function_004D8DAC.md) at `0x004D8DF4`
- [MiRemoveFaultNode](../4F/MiRemoveFaultNode_function_004FC440.md) at `0x004FC4C4`
- [IopMcRemoveMdlPagesFromTable](../5A/IopMcRemoveMdlPagesFromTable_function_005A3D94.md) at `0x005A3E5A`
- [PsAdjustBasicEnclaveThreadList](../5E/PsAdjustBasicEnclaveThreadList_function_005E4BD8.md) at `0x005E4CAF`
- [MiRemoveLoaderEntry](../67/MiRemoveLoaderEntry_function_006713C8.md) at `0x0067141A`
- [MmUpdateMdlTrackerForMdlSwitch](../67/MmUpdateMdlTrackerForMdlSwitch_function_00674298.md) at `0x00674386`
- [MmUpdateMdlTrackerForMdlSwitch](../67/MmUpdateMdlTrackerForMdlSwitch_function_00674298.md) at `0x0067440E`
- [MiHotRemoveHugeRange](../67/MiHotRemoveHugeRange_function_00675DD0.md) at `0x00676006`
- [MiMakeEntireHugePfnGood](../67/MiMakeEntireHugePfnGood_function_00676644.md) at `0x00676706`
- [MiMarkHugePfnGood](../67/MiMarkHugePfnGood_function_00676BB0.md) at `0x00676D17`
- [MiRemovePendingBadPageNode](../67/MiRemovePendingBadPageNode_function_0067A0DC.md) at `0x0067A12F`
- [MiDeleteKernelStackNode](../67/MiDeleteKernelStackNode_function_0067B1B0.md) at `0x0067B1D5`
- [MiDeleteStaleCacheMaps](../67/MiDeleteStaleCacheMaps_function_0067B780.md) at `0x0067B9BC`
- [MiRemoveIoPageExclusion](../67/MiRemoveIoPageExclusion_function_0067C91C.md) at `0x0067C93F`
- [MiUpdatePageFileList](../68/MiUpdatePageFileList_function_006803AC.md) at `0x0068045F`
- [MiInsertCopyExtents](../68/MiInsertCopyExtents_function_00681440.md) at `0x006814A6`
- [MiMergeCopyExtents](../68/MiMergeCopyExtents_function_00681844.md) at `0x006819F2`
- [MmManageFaultRange](../68/MmManageFaultRange_function_00686AD4.md) at `0x00686C52`
- [MiRemoveUserPhysicalPagesView](../68/MiRemoveUserPhysicalPagesView_function_00689658.md) at `0x00689710`
- [MiCombiningInProgress](../68/MiCombiningInProgress_function_0068BD6C.md) at `0x0068BE7E`
- [MiActOnPartitionNodePages](../68/MiActOnPartitionNodePages_function_0068F7F4.md) at `0x0068FE9B`
- [MiClearRangeInPartitionTree](../69/MiClearRangeInPartitionTree_function_00690734.md) at `0x00690874`
- [MiDeletePartitionPageNodes](../69/MiDeletePartitionPageNodes_function_006908F0.md) at `0x00690958`
- [MiFinishChildPartitionHotAdd](../69/MiFinishChildPartitionHotAdd_function_00690C00.md) at `0x00690C87`
- [MiFreePartitionTree](../69/MiFreePartitionTree_function_00690E50.md) at `0x00690E8B`
- [MiInsertPartitionPages](../69/MiInsertPartitionPages_function_006911A0.md) at `0x00691541`
- [MiMergePageNodes](../69/MiMergePageNodes_function_006916A0.md) at `0x00691766`
- [MiPartitionDeleteMemoryNode](../69/MiPartitionDeleteMemoryNode_function_00691A20.md) at `0x00691A9B`
- [MiReturnPartitionPagesToParent](../69/MiReturnPartitionPagesToParent_function_00691B5C.md) at `0x00691C86`
- [MiReplaceSystemProtoPtesNode](../69/MiReplaceSystemProtoPtesNode_function_00699658.md) at `0x00699697`
- [sub_006DA0EA](../6D/Unknown_function_006DA0EA.md) at `0x006DA0F7`
- [sub_006DA6DC](../6D/Unknown_function_006DA6DC.md) at `0x006DA711`
- [sub_006E75BA](../6E/Unknown_function_006E75BA.md) at `0x006E7689`
- [PspProcessDynamicEHContinuationTargets](../../page/78/PspProcessDynamicEHContinuationTargets_function_00782348.md) at `0x00782547`
- [PspUnlinkSessionId](../../page/78/PspUnlinkSessionId_function_007895D8.md) at `0x00789623`
- [RtlRemoveDynamicEnforcedAddressRange](../../page/79/RtlRemoveDynamicEnforcedAddressRange_function_00794F2C.md) at `0x00794FA3`
- [MiDeleteFileExtentList](../../page/80/MiDeleteFileExtentList_function_00800F6C.md) at `0x00800FB6`
- [MiInsertHotPatchRecord](../../page/80/MiInsertHotPatchRecord_function_008041D4.md) at `0x0080428A`
- [MiInsertSecureImageActivePatch](../../page/80/MiInsertSecureImageActivePatch_function_0080448C.md) at `0x00804525`
- [MmRemoveSecureImageActivePatch](../../page/80/MmRemoveSecureImageActivePatch_function_0080760C.md) at `0x0080767D`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D82A`
- [sub_00888AF0](../../page/88/Unknown_function_00888AF0.md) at `0x00888AF3`
- [ExpWnfDeleteNameInstance](../../page/90/ExpWnfDeleteNameInstance_function_009088C8.md) at `0x0090896D`
- [Pdcv2ActivationClientDeactivate](../../page/95/Pdcv2ActivationClientDeactivate_function_009552E0.md) at `0x00955486`
- [MiProcessCrcList](../../page/9F/MiProcessCrcList_function_009F6F94.md) at `0x009F74A1`
- [sub_00B36710](../../page/B3/Unknown_function_00B36710.md) at `0x00B3696A`
- [sub_00B3976A](../../page/B3/Unknown_function_00B3976A.md) at `0x00B3977D`
- [MiInitializeDriverPtes](../../init/C6/MiInitializeDriverPtes_function_00C61818.md) at `0x00C61AA0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00296650  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00296655  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0029665A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0029665F  57                              push rdi
00296660  41 54                           push r12
00296662  41 55                           push r13
00296664  41 56                           push r14
00296666  41 57                           push r15
00296668  48 83 EC 30                     sub rsp, 0x30
0029666C  4C 8B 0A                        mov r9, qword ptr [rdx]
0029666F  4C 8B C2                        mov r8, rdx
00296672  4C 8B 52 08                     mov r10, qword ptr [rdx + 8]
00296676  4C 8B F9                        mov r15, rcx
00296679  4D 85 C9                        test r9, r9
0029667C  75 05                           jne 0x140296683
0029667E  4D 8B CA                        mov r9, r10
00296681  EB 09                           jmp 0x14029668c
00296683  4D 85 D2                        test r10, r10
00296686  0F 85 BE 00 00 00               jne 0x14029674a
0029668C  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
00296690  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
00296694  4D 85 C9                        test r9, r9
00296697  0F 85 93 01 00 00               jne 0x140296830
0029669D  48 85 D2                        test rdx, rdx
002966A0  0F 84 9A 00 00 00               je 0x140296740
002966A6  4C 39 42 08                     cmp qword ptr [rdx + 8], r8
002966AA  0F 85 80 00 00 00               jne 0x140296730
002966B0  41 B2 03                        mov r10b, 3
002966B3  4C 89 4A 08                     mov qword ptr [rdx + 8], r9
002966B7  41 BE 01 00 00 00               mov r14d, 1
002966BD  45 33 E4                        xor r12d, r12d
002966C0  41 BB 08 00 00 00               mov r11d, 8
002966C6  0F B6 5A 10                     movzx ebx, byte ptr [rdx + 0x10]
002966CA  48 8D 72 10                     lea rsi, [rdx + 0x10]
002966CE  0F B6 EB                        movzx ebp, bl
002966D1  41 0F B6 C2                     movzx eax, r10b
002966D5  40 80 E5 03                     and bpl, 3
002966D9  34 02                           xor al, 2
002966DB  40 3A E8                        cmp bpl, al
002966DE  74 2F                           je 0x14029670f
002966E0  40 84 ED                        test bpl, bpl
002966E3  0F 85 5A 01 00 00               jne 0x140296843
002966E9  80 E3 FC                        and bl, 0xfc
002966EC  41 0A DA                        or bl, r10b
002966EF  88 1E                           mov byte ptr [rsi], bl
002966F1  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
002966F6  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
002966FB  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00296700  48 83 C4 30                     add rsp, 0x30
00296704  41 5F                           pop r15
00296706  41 5E                           pop r14
00296708  41 5D                           pop r13
0029670A  41 5C                           pop r12
0029670C  5F                              pop rdi
0029670D  C3                              ret
0029670E  CC                              int3
0029670F  80 E3 FC                        and bl, 0xfc
00296712  88 1E                           mov byte ptr [rsi], bl
00296714  48 8B 3E                        mov rdi, qword ptr [rsi]
00296717  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
0029671B  74 D4                           je 0x1402966f1
0029671D  48 39 57 08                     cmp qword ptr [rdi + 8], rdx
00296721  41 BA 03 00 00 00               mov r10d, 3
00296727  48 8B D7                        mov rdx, rdi
0029672A  45 0F 45 D6                     cmovne r10d, r14d
0029672E  EB 90                           jmp 0x1402966c0
00296730  4C 39 02                        cmp qword ptr [rdx], r8
00296733  0F 84 04 03 00 00               je 0x140296a3d
00296739  B9 1D 00 00 00                  mov ecx, 0x1d
0029673E  CD 29                           int 0x29
00296740  4C 39 01                        cmp qword ptr [rcx], r8
00296743  75 F4                           jne 0x140296739
00296745  4C 89 09                        mov qword ptr [rcx], r9
00296748  EB A7                           jmp 0x1402966f1
0029674A  0F B6 42 10                     movzx eax, byte ptr [rdx + 0x10]
0029674E  45 33 E4                        xor r12d, r12d
00296751  24 03                           and al, 3
00296753  45 8D 74 24 01                  lea r14d, [r12 + 1]
00296758  3C 03                           cmp al, 3
0029675A  0F 84 BB 01 00 00               je 0x14029691b
00296760  4D 8B 1A                        mov r11, qword ptr [r10]
00296763  49 8B CA                        mov rcx, r10
00296766  49 8B D2                        mov rdx, r10
00296769  41 8B FE                        mov edi, r14d
0029676C  4D 85 DB                        test r11, r11
0029676F  74 14                           je 0x140296785
00296771  41 8B FC                        mov edi, r12d
00296774  49 8B 03                        mov rax, qword ptr [r11]
00296777  48 8B D1                        mov rdx, rcx
0029677A  49 8B CB                        mov rcx, r11
0029677D  4C 8B D8                        mov r11, rax
00296780  48 85 C0                        test rax, rax
00296783  75 EF                           jne 0x140296774
00296785  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00296789  4C 89 09                        mov qword ptr [rcx], r9
0029678C  4C 89 51 08                     mov qword ptr [rcx + 8], r10
00296790  4D 8B 59 10                     mov r11, qword ptr [r9 + 0x10]
00296794  49 8B C3                        mov rax, r11
00296797  48 83 E0 FC                     and rax, 0xfffffffffffffffc
0029679B  49 3B C0                        cmp rax, r8
0029679E  75 99                           jne 0x140296739
002967A0  41 83 E3 03                     and r11d, 3
002967A4  4C 0B D9                        or r11, rcx
002967A7  4D 89 59 10                     mov qword ptr [r9 + 0x10], r11
002967AB  4D 8B 4A 10                     mov r9, qword ptr [r10 + 0x10]
002967AF  49 8B C1                        mov rax, r9
002967B2  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002967B6  49 3B C0                        cmp rax, r8
002967B9  0F 85 7A FF FF FF               jne 0x140296739
002967BF  41 83 E1 03                     and r9d, 3
002967C3  4C 0B C9                        or r9, rcx
002967C6  4D 89 4A 10                     mov qword ptr [r10 + 0x10], r9
002967CA  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
002967CE  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002967D2  48 3B C2                        cmp rax, rdx
002967D5  0F 85 5E FF FF FF               jne 0x140296739
002967DB  8B C7                           mov eax, edi
002967DD  48 89 1C C2                     mov qword ptr [rdx + rax*8], rbx
002967E1  48 85 DB                        test rbx, rbx
002967E4  0F 85 E8 01 00 00               jne 0x1402969d2
002967EA  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
002967EE  85 FF                           test edi, edi
002967F0  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
002967F4  41 BA 03 00 00 00               mov r10d, 3
002967FA  4D 8B 48 10                     mov r9, qword ptr [r8 + 0x10]
002967FE  45 0F 44 D6                     cmove r10d, r14d
00296802  49 83 E1 FC                     and r9, 0xfffffffffffffffc
00296806  0F 84 B5 01 00 00               je 0x1402969c1
0029680C  4D 39 41 08                     cmp qword ptr [r9 + 8], r8
00296810  49 8B C4                        mov rax, r12
00296813  41 BB 08 00 00 00               mov r11d, 8
00296819  49 0F 44 C3                     cmove rax, r11
0029681D  4E 39 04 08                     cmp qword ptr [rax + r9], r8
00296821  0F 85 12 FF FF FF               jne 0x140296739
00296827  4A 89 0C 08                     mov qword ptr [rax + r9], rcx
0029682B  E9 96 FE FF FF                  jmp 0x1402966c6
00296830  4D 39 41 10                     cmp qword ptr [r9 + 0x10], r8
00296834  0F 85 FF FE FF FF               jne 0x140296739
0029683A  49 89 51 10                     mov qword ptr [r9 + 0x10], rdx
0029683E  E9 5A FE FF FF                  jmp 0x14029669d
00296843  48 8B 3E                        mov rdi, qword ptr [rsi]
00296846  4C 8B 2A                        mov r13, qword ptr [rdx]
00296849  41 80 FA 01                     cmp r10b, 1
0029684D  75 04                           jne 0x140296853
0029684F  4C 8B 6A 08                     mov r13, qword ptr [rdx + 8]
00296853  45 0F B6 45 10                  movzx r8d, byte ptr [r13 + 0x10]
00296858  41 80 E0 03                     and r8b, 3
0029685C  44 3A C0                        cmp r8b, al
0029685F  0F 84 E2 00 00 00               je 0x140296947
00296865  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00296869  48 83 E0 FC                     and rax, 0xfffffffffffffffc
0029686D  48 3B C2                        cmp rax, rdx
00296870  0F 85 C3 FE FF FF               jne 0x140296739
00296876  41 80 FA 01                     cmp r10b, 1
0029687A  49 8B C3                        mov rax, r11
0029687D  49 0F 45 C4                     cmovne rax, r12
00296881  4C 39 2C 10                     cmp qword ptr [rax + rdx], r13
00296885  0F 85 AE FE FF FF               jne 0x140296739
0029688B  48 8B CF                        mov rcx, rdi
0029688E  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00296892  0F 84 94 01 00 00               je 0x140296a2c
00296898  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
0029689C  0F 85 67 01 00 00               jne 0x140296a09
002968A2  4C 89 69 08                     mov qword ptr [rcx + 8], r13
002968A6  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
002968AA  48 8B CF                        mov rcx, rdi
002968AD  48 33 C8                        xor rcx, rax
002968B0  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002968B4  48 33 C8                        xor rcx, rax
002968B7  49 8B C4                        mov rax, r12
002968BA  41 80 FA 01                     cmp r10b, 1
002968BE  49 89 4D 10                     mov qword ptr [r13 + 0x10], rcx
002968C2  49 0F 45 C3                     cmovne rax, r11
002968C6  4A 8B 0C 28                     mov rcx, qword ptr [rax + r13]
002968CA  48 85 C9                        test rcx, rcx
002968CD  0F 85 12 01 00 00               jne 0x1402969e5
002968D3  41 80 FA 01                     cmp r10b, 1
002968D7  49 8B C4                        mov rax, r12
002968DA  49 0F 44 C3                     cmove rax, r11
002968DE  48 89 0C 10                     mov qword ptr [rax + rdx], rcx
002968E2  49 8B C4                        mov rax, r12
002968E5  49 0F 45 C3                     cmovne rax, r11
002968E9  4A 89 14 28                     mov qword ptr [rax + r13], rdx
002968ED  8B 06                           mov eax, dword ptr [rsi]
002968EF  83 E0 03                        and eax, 3
002968F2  49 0B C5                        or rax, r13
002968F5  48 89 06                        mov qword ptr [rsi], rax
002968F8  41 0F B6 4D 10                  movzx ecx, byte ptr [r13 + 0x10]
002968FD  45 84 C0                        test r8b, r8b
00296900  0F 85 14 01 00 00               jne 0x140296a1a
00296906  0F B6 C1                        movzx eax, cl
00296909  41 32 C2                        xor al, r10b
0029690C  34 FE                           xor al, 0xfe
0029690E  24 03                           and al, 3
00296910  32 C1                           xor al, cl
00296912  41 88 45 10                     mov byte ptr [r13 + 0x10], al
00296916  E9 D6 FD FF FF                  jmp 0x1402966f1
0029691B  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0029691F  49 8B C9                        mov rcx, r9
00296922  49 8B D1                        mov rdx, r9
00296925  41 8B FC                        mov edi, r12d
00296928  48 85 C0                        test rax, rax
0029692B  74 12                           je 0x14029693f
0029692D  41 8B FE                        mov edi, r14d
00296930  48 8B D1                        mov rdx, rcx
00296933  48 8B C8                        mov rcx, rax
00296936  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0029693A  48 85 C0                        test rax, rax
0029693D  75 F1                           jne 0x140296930
0029693F  48 8B 19                        mov rbx, qword ptr [rcx]
00296942  E9 42 FE FF FF                  jmp 0x140296789
00296947  41 80 FA 01                     cmp r10b, 1
0029694B  45 8B CC                        mov r9d, r12d
0029694E  4D 8B C5                        mov r8, r13
00296951  49 8B CF                        mov rcx, r15
00296954  41 0F 94 C1                     sete r9b
00296958  E8 17 03 00 00                  call 0x140296c74
0029695D  80 26 FC                        and byte ptr [rsi], 0xfc
00296960  48 8B D0                        mov rdx, rax
00296963  45 0F B6 45 10                  movzx r8d, byte ptr [r13 + 0x10]
00296968  41 0F B6 C0                     movzx eax, r8b
0029696C  44 0F B6 CD                     movzx r9d, bpl
00296970  24 FC                           and al, 0xfc
00296972  41 88 45 10                     mov byte ptr [r13 + 0x10], al
00296976  0F B6 4A 10                     movzx ecx, byte ptr [rdx + 0x10]
0029697A  8B C1                           mov eax, ecx
0029697C  83 E0 03                        and eax, 3
0029697F  44 3B C8                        cmp r9d, eax
00296982  74 21                           je 0x1402969a5
00296984  83 F1 FE                        xor ecx, 0xfffffffe
00296987  83 E1 03                        and ecx, 3
0029698A  44 3B C9                        cmp r9d, ecx
0029698D  75 0D                           jne 0x14029699c
0029698F  41 32 D8                        xor bl, r8b
00296992  80 E3 03                        and bl, 3
00296995  41 32 D8                        xor bl, r8b
00296998  41 88 5D 10                     mov byte ptr [r13 + 0x10], bl
0029699C  80 62 10 FC                     and byte ptr [rdx + 0x10], 0xfc
002969A0  E9 72 FD FF FF                  jmp 0x140296717
002969A5  0F B6 06                        movzx eax, byte ptr [rsi]
002969A8  0F B6 C8                        movzx ecx, al
002969AB  40 32 CD                        xor cl, bpl
002969AE  80 F1 FE                        xor cl, 0xfe
002969B1  80 E1 03                        and cl, 3
002969B4  32 C8                           xor cl, al
002969B6  88 0E                           mov byte ptr [rsi], cl
002969B8  80 62 10 FC                     and byte ptr [rdx + 0x10], 0xfc
002969BC  E9 56 FD FF FF                  jmp 0x140296717
002969C1  4D 39 07                        cmp qword ptr [r15], r8
002969C4  0F 85 6F FD FF FF               jne 0x140296739
002969CA  49 89 0F                        mov qword ptr [r15], rcx
002969CD  E9 EE FC FF FF                  jmp 0x1402966c0
002969D2  48 39 4B 10                     cmp qword ptr [rbx + 0x10], rcx
002969D6  0F 85 5D FD FF FF               jne 0x140296739
002969DC  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
002969E0  E9 05 FE FF FF                  jmp 0x1402967ea
002969E5  4C 8B 49 10                     mov r9, qword ptr [rcx + 0x10]
002969E9  49 8B C1                        mov rax, r9
002969EC  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002969F0  49 3B C5                        cmp rax, r13
002969F3  0F 85 40 FD FF FF               jne 0x140296739
002969F9  41 83 E1 03                     and r9d, 3
002969FD  4C 0B CA                        or r9, rdx
00296A00  4C 89 49 10                     mov qword ptr [rcx + 0x10], r9
00296A04  E9 CA FE FF FF                  jmp 0x1402968d3
00296A09  48 39 11                        cmp qword ptr [rcx], rdx
00296A0C  0F 85 27 FD FF FF               jne 0x140296739
00296A12  4C 89 29                        mov qword ptr [rcx], r13
00296A15  E9 8C FE FF FF                  jmp 0x1402968a6
00296A1A  80 E1 FC                        and cl, 0xfc
00296A1D  49 8B D5                        mov rdx, r13
00296A20  41 88 4D 10                     mov byte ptr [r13 + 0x10], cl
00296A24  80 26 FC                        and byte ptr [rsi], 0xfc
00296A27  E9 EB FC FF FF                  jmp 0x140296717
00296A2C  49 39 17                        cmp qword ptr [r15], rdx
00296A2F  0F 85 04 FD FF FF               jne 0x140296739
00296A35  4D 89 2F                        mov qword ptr [r15], r13
00296A38  E9 69 FE FF FF                  jmp 0x1402968a6
00296A3D  41 B2 01                        mov r10b, 1
00296A40  4C 89 0A                        mov qword ptr [rdx], r9
00296A43  E9 6F FC FF FF                  jmp 0x1402966b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlAvlRemoveNode(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00296683;
    goto loc_0029668C;
loc_00296683:
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_0029674A;
loc_0029668C:
    a2 = (*(unsigned __int64 *)(a2 + 16)) & (-4);
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_00296830;
loc_0029669D:
    if (a2 == 0) goto loc_00296740;
    if ((*(unsigned __int64 *)(a2 + 8)) != a2) goto loc_00296730;
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a2 + 8);
loc_002966B7:
    v_r12 = 0;
loc_002966C0:
loc_002966C6:
    v_rbp = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 16))) & (3));
    result = (unsigned __int8)((3) ^ (2));
    if (((unsigned __int8)(v_rbp)) == ((unsigned __int8)(result))) goto loc_0029670F;
    if ((unsigned __int8)(v_rbp) != 0) goto loc_00296843;
    v_rbx = (unsigned __int8)((*(unsigned __int8 *)(a2 + 16)) & (252));
    v_rbx = (unsigned __int8)((v_rbx) | (3));
    *(unsigned __int8 *)(a2 + 16) = (unsigned __int8)(v_rbx);
loc_002966F1:
    v_rsp = (v_rsp) + (48);
    return result;
loc_0029670F:
    v_rbx = (unsigned __int8)((v_stack_p8) & (252));
    *(unsigned __int8 *)(v_stack_p18) = (unsigned __int8)(v_rbx);
loc_00296717:
    v_rdi = (*(unsigned __int64 *)(v_stack_p18)) & (-4);
    if (condition_is_equal) goto loc_002966F1;
    v_r10 = 3;
    if ((*(unsigned __int64 *)(v_rdi + 8)) != a2) { v_r10 = 1; }
    goto loc_002966C0;
loc_00296730:
    if ((*(unsigned __int64 *)(v_rdi)) == a2) goto loc_00296A3D;
loc_00296739:
loc_00296740:
    if ((*(unsigned __int64 *)(29)) != a2) goto loc_00296739;
    *(unsigned __int64 *)(29) = *(unsigned __int64 *)(a2 + 8);
    goto loc_002966F1;
loc_0029674A:
    v_r12 = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 16)) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_0029691B;
    if (*(unsigned __int64 *)(v_r10) == 0) goto loc_00296785;
loc_00296774:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r10)) != 0) goto loc_00296774;
loc_00296785:
loc_00296789:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10)) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 8) = v_r10;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16)) & (-4);
    if (result != a2) goto loc_00296739;
    v_r11 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16)) & (3));
    v_r11 = (v_r11) | (*(unsigned __int64 *)(v_r10));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 16) = v_r11;
    result = (*(unsigned __int64 *)(v_r10 + 16)) & (-4);
    if (result != a2) goto loc_00296739;
    a4 = (unsigned int)((*(unsigned __int64 *)(v_r10 + 16)) & (3));
    a4 = (a4) | (*(unsigned __int64 *)(v_r10));
    *(unsigned __int64 *)(v_r10 + 16) = a4;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 16)) & (-4);
    if (result != v_r10) goto loc_00296739;
    *(unsigned __int64 *)(v_r10 + 0 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 8) != 0) goto loc_002969D2;
loc_002967EA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 16) = *(unsigned __int64 *)(a2 + 16);
    v_r10 = 3;
    if (0 == 0) { v_r10 = (unsigned int)(v_r12 + 1); }
    a4 = (*(unsigned __int64 *)(a2 + 16)) & (-4);
    if (condition_is_equal) goto loc_002969C1;
    result = 0;
    if ((*(unsigned __int64 *)(a4 + 8)) == a2) { result = 8; }
    if ((*(unsigned __int64 *)(result + a4 * 1)) != a2) goto loc_00296739;
    *(unsigned __int64 *)(result + a4 * 1) = *(unsigned __int64 *)(v_r10);
    goto loc_002966C6;
loc_00296830:
    if ((*(unsigned __int64 *)(a4 + 16)) != a2) goto loc_00296739;
    *(unsigned __int64 *)(a4 + 16) = v_r10;
    goto loc_0029669D;
loc_00296843:
    v_r13 = *(unsigned __int64 *)(v_r10);
    if (((unsigned __int8)(v_r10)) == 1) {
        v_r13 = *(unsigned __int64 *)(v_r10 + 8);
    }
    a3 = (unsigned __int8)((*(unsigned __int8 *)(v_r13 + 16)) & (3));
    if (((unsigned __int8)(a3)) == ((unsigned __int8)(result))) goto loc_00296947;
    result = (*(unsigned __int64 *)(v_r13 + 16)) & (-4);
    if (result != v_r10) goto loc_00296739;
    result = 8;
    if (((unsigned __int8)(v_r10)) != 1) { result = 0; }
    if ((*(unsigned __int64 *)(result + v_r10 * 1)) != v_r13) goto loc_00296739;
    a1 = (*(unsigned __int64 *)(v_stack_p18)) & (-4);
    if (condition_is_equal) goto loc_00296A2C;
    if ((*(unsigned __int64 *)(a1 + 8)) != v_r10) goto loc_00296A09;
    *(unsigned __int64 *)(a1 + 8) = v_r13;
loc_002968A6:
    a1 = (*(unsigned __int64 *)(v_stack_p18)) ^ (*(unsigned __int64 *)(v_r13 + 16));
    a1 = (a1) & (-4);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_r13 + 16));
    *(unsigned __int64 *)(v_r13 + 16) = a1;
    result = 0;
    if (((unsigned __int8)(v_r10)) != 1) { result = 8; }
    if (*(unsigned __int64 *)(result + v_r13 * 1) != 0) goto loc_002969E5;
loc_002968D3:
    result = 0;
    if (((unsigned __int8)(v_r10)) == 1) { result = 8; }
    *(unsigned __int64 *)(result + v_r10 * 1) = *(unsigned __int64 *)(result + v_r13 * 1);
    result = 0;
    if (((unsigned __int8)(v_r10)) != 1) { result = 8; }
    *(unsigned __int64 *)(result + v_r13 * 1) = v_r10;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18))) & (3));
    result = (result) | (v_r13);
    *(unsigned __int64 *)(v_stack_p18) = result;
    if ((unsigned __int8)(a3) != 0) goto loc_00296A1A;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 16))) ^ ((unsigned __int8)(v_r10)));
    result = (unsigned __int8)((result) ^ (254));
    result = (unsigned __int8)((result) & (3));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 16))));
    *(unsigned __int8 *)(v_r13 + 16) = (unsigned __int8)(result);
    goto loc_002966F1;
loc_0029691B:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_0029693F;
loc_00296930:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + 8) != 0) goto loc_00296930;
loc_0029693F:
    goto loc_00296789;
loc_00296947:
    a4 = (((unsigned __int8)(v_r10)) == 1) ? 1 : 0;
    result = RtlpTreeDoubleRotateNodes(a1, a4, v_r13, a4);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 16))) & (252));
    *(unsigned __int8 *)(v_r13 + 16) = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 16)))) & (3));
    if (((unsigned int)((unsigned __int8)(v_stack_p10))) == ((unsigned int)(result))) goto loc_002969A5;
    a1 = (unsigned int)((*(unsigned __int8 *)(result + 16)) ^ (0xFFFFFFFEULL));
    a1 = (unsigned int)((a1) & (3));
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8));
    if (((unsigned int)((unsigned __int8)(v_stack_p10))) == ((unsigned int)(a1))) {
        v_rbx = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8))) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 16))));
        v_rbx = (unsigned __int8)((v_rbx) & (3));
        v_rbx = (unsigned __int8)((v_rbx) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 16))));
        *(unsigned __int8 *)(v_r13 + 16) = (unsigned __int8)(v_rbx);
    }
    goto loc_00296717;
loc_002969A5:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18))) ^ ((unsigned __int8)(v_stack_p10)));
    a1 = (unsigned __int8)((a1) ^ (254));
    a1 = (unsigned __int8)((a1) & (3));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18))));
    *(unsigned __int8 *)(v_stack_p18) = (unsigned __int8)(a1);
    goto loc_00296717;
loc_002969C1:
    if ((*(unsigned __int64 *)(a1)) != (*(unsigned __int8 *)(v_r13 + 16))) goto loc_00296739;
    *(unsigned __int64 *)(a1) = a1;
    goto loc_002966C0;
loc_002969D2:
    if ((*(unsigned __int64 *)(v_rbx + 16)) != a1) goto loc_00296739;
    *(unsigned __int64 *)(v_rbx + 16) = result;
    goto loc_002967EA;
loc_002969E5:
    result = (*(unsigned __int64 *)(a1 + 16)) & (-4);
    if (result != v_r13) goto loc_00296739;
    a4 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (3));
    a4 = (a4) | (result);
    *(unsigned __int64 *)(a1 + 16) = a4;
    goto loc_002968D3;
loc_00296A09:
    if ((*(unsigned __int64 *)(a1)) != result) goto loc_00296739;
    *(unsigned __int64 *)(a1) = v_r13;
    goto loc_002968A6;
loc_00296A1A:
    a1 = (unsigned __int8)((a1) & (252));
    *(unsigned __int8 *)(v_r13 + 16) = (unsigned __int8)(a1);
    goto loc_00296717;
loc_00296A2C:
    if ((*(unsigned __int64 *)(a1)) != v_r13) goto loc_00296739;
    *(unsigned __int64 *)(a1) = v_r13;
    goto loc_002968A6;
loc_00296A3D:
    *(unsigned __int64 *)(v_r13) = a4;
    goto loc_002966B7;
}
```

## 5. (Beta) C Style

```c
int64_t RtlAvlRemoveNode(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    if (*(uint64_t *)(arg2) != 0) goto loc_00296683;
    goto loc_0029668C;
loc_00296683:
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_0029674A;
loc_0029668C:
    Arg2 = (*(uint64_t *)(arg2 + 0x10)) & (-4);
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_00296830;
loc_0029669D:
    if (Arg2 == NULL) goto loc_00296740;
    if ((*(uint64_t *)(arg2 + 0x8)) != Arg2) goto loc_00296730;
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg2 + 0x8);
loc_002966B7:
    local_r12 = 0;
loc_002966C0:
loc_002966C6:
    local_rbp = (uint8_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x10))) & (3));
    result = (uint8_t)((3) ^ (2));
    if (((uint8_t)(local_rbp)) == ((uint8_t)(result))) goto loc_0029670F;
    if ((uint8_t)(local_rbp) != 0) goto loc_00296843;
    local_rbx = (uint8_t)((*(uint8_t *)(arg2 + 0x10)) & (252));
    local_rbx = (uint8_t)((local_rbx) | (3));
    *(uint8_t *)(arg2 + 0x10) = (uint8_t)(local_rbx);
loc_002966F1:
    local_rsp = (local_rsp) + (48);
    return result;
loc_0029670F:
    local_rbx = (uint8_t)((v_stack_p8) & (252));
    *(uint8_t *)(v_stack_p18) = (uint8_t)(local_rbx);
loc_00296717:
    local_rdi = (*(uint64_t *)(v_stack_p18)) & (-4);
    if (condition_is_equal) goto loc_002966F1;
    local_r10 = 3;
    if ((*(uint64_t *)(local_rdi + 0x8)) != Arg2) { local_r10 = 1; }
    goto loc_002966C0;
loc_00296730:
    if ((*(uint64_t *)(local_rdi)) == Arg2) goto loc_00296A3D;
loc_00296739:
loc_00296740:
    if ((*(uint64_t *)(29)) != Arg2) goto loc_00296739;
    *(uint64_t *)(29) = *(uint64_t *)(arg2 + 0x8);
    goto loc_002966F1;
loc_0029674A:
    local_r12 = 0;
    result = (uint8_t)((*(uint8_t *)(local_rdi + 0x10)) & (3));
    if (((uint8_t)(result)) == 3) goto loc_0029691B;
    if (*(uint64_t *)(local_r10) == 0) goto loc_00296785;
loc_00296774:
    if (*(uint64_t *)(*(uint64_t *)(local_r10)) != 0) goto loc_00296774;
loc_00296785:
loc_00296789:
    *(uint64_t *)(*(uint64_t *)(local_r10)) = *(uint64_t *)(arg2 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r10) + 0x8) = local_r10;
    result = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10)) & (-4);
    if (result != Arg2) goto loc_00296739;
    local_r11 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10)) & (3));
    local_r11 = (local_r11) | (*(uint64_t *)(local_r10));
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10) = local_r11;
    result = (*(uint64_t *)(local_r10 + 0x10)) & (-4);
    if (result != Arg2) goto loc_00296739;
    a4 = (uint32_t)((*(uint64_t *)(local_r10 + 0x10)) & (3));
    a4 = (a4) | (*(uint64_t *)(local_r10));
    *(uint64_t *)(local_r10 + 0x10) = a4;
    result = (*(uint64_t *)(*(uint64_t *)(local_r10) + 0x10)) & (-4);
    if (result != local_r10) goto loc_00296739;
    *(uint64_t *)(local_r10 + 0x0 * 8) = *(uint64_t *)(*(uint64_t *)(local_r10) + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(local_r10) + 0x8) != 0) goto loc_002969D2;
loc_002967EA:
    *(uint64_t *)(*(uint64_t *)(local_r10) + 0x10) = *(uint64_t *)(arg2 + 0x10);
    local_r10 = 3;
    if (0 == 0) { local_r10 = (uint32_t)(local_r12 + 1); }
    a4 = (*(uint64_t *)(arg2 + 0x10)) & (-4);
    if (condition_is_equal) goto loc_002969C1;
    result = 0;
    if ((*(uint64_t *)(a4 + 0x8)) == Arg2) { result = 8; }
    if ((*(uint64_t *)(result + a4 * 1)) != Arg2) goto loc_00296739;
    *(uint64_t *)(result + a4 * 1) = *(uint64_t *)(local_r10);
    goto loc_002966C6;
loc_00296830:
    if ((*(uint64_t *)(a4 + 0x10)) != Arg2) goto loc_00296739;
    *(uint64_t *)(a4 + 0x10) = local_r10;
    goto loc_0029669D;
loc_00296843:
    local_r13 = *(uint64_t *)(local_r10);
    if (((uint8_t)(local_r10)) == 1) {
        local_r13 = *(uint64_t *)(local_r10 + 0x8);
    }
    a3 = (uint8_t)((*(uint8_t *)(local_r13 + 0x10)) & (3));
    if (((uint8_t)(a3)) == ((uint8_t)(result))) goto loc_00296947;
    result = (*(uint64_t *)(local_r13 + 0x10)) & (-4);
    if (result != local_r10) goto loc_00296739;
    result = 8;
    if (((uint8_t)(local_r10)) != 1) { result = 0; }
    if ((*(uint64_t *)(result + local_r10 * 1)) != local_r13) goto loc_00296739;
    Arg1 = (*(uint64_t *)(v_stack_p18)) & (-4);
    if (condition_is_equal) goto loc_00296A2C;
    if ((*(uint64_t *)(arg1 + 0x8)) != local_r10) goto loc_00296A09;
    *(uint64_t *)(arg1 + 0x8) = local_r13;
loc_002968A6:
    Arg1 = (*(uint64_t *)(v_stack_p18)) ^ (*(uint64_t *)(local_r13 + 0x10));
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_r13 + 0x10));
    *(void **)(local_r13 + 0x10) = Arg1;
    result = 0;
    if (((uint8_t)(local_r10)) != 1) { result = 8; }
    if (*(uint64_t *)(result + local_r13 * 1) != 0) goto loc_002969E5;
loc_002968D3:
    result = 0;
    if (((uint8_t)(local_r10)) == 1) { result = 8; }
    *(uint64_t *)(result + local_r10 * 1) = *(uint64_t *)(result + local_r13 * 1);
    result = 0;
    if (((uint8_t)(local_r10)) != 1) { result = 8; }
    *(uint64_t *)(result + local_r13 * 1) = local_r10;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18))) & (3));
    result = (result) | (local_r13);
    *(uint64_t *)(v_stack_p18) = result;
    if ((uint8_t)(a3) != 0) goto loc_00296A1A;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_r13 + 0x10))) ^ ((uint8_t)(local_r10)));
    result = (uint8_t)((result) ^ (254));
    result = (uint8_t)((result) & (3));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(local_r13 + 0x10))));
    *(uint8_t *)(local_r13 + 0x10) = (uint8_t)(result);
    goto loc_002966F1;
loc_0029691B:
    if (*(uint64_t *)(a4 + 0x8) == 0) goto loc_0029693F;
loc_00296930:
    if (*(uint64_t *)(*(uint64_t *)(a4 + 0x8) + 0x8) != 0) goto loc_00296930;
loc_0029693F:
    goto loc_00296789;
loc_00296947:
    a4 = (((uint8_t)(local_r10)) == 1) ? 1 : 0;
    result = RtlpTreeDoubleRotateNodes(Arg1, a4, local_r13, a4);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_r13 + 0x10))) & (252));
    *(uint8_t *)(local_r13 + 0x10) = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x10)))) & (3));
    if (((uint32_t)((uint8_t)(v_stack_p10))) == ((uint32_t)(result))) goto loc_002969A5;
    Arg1 = (uint32_t)((*(uint8_t *)(result + 0x10)) ^ (0xFFFFFFFEULL));
    Arg1 = (uint32_t)((Arg1) & (3));
    local_rbx = *(uint64_t *)(*(uint64_t *)(a4 + 0x8));
    if (((uint32_t)((uint8_t)(v_stack_p10))) == ((uint32_t)(Arg1))) {
        local_rbx = (uint8_t)((*(uint64_t *)(*(uint64_t *)(a4 + 0x8))) ^ ((uint8_t)(*(uint8_t *)(local_r13 + 0x10))));
        local_rbx = (uint8_t)((local_rbx) & (3));
        local_rbx = (uint8_t)((local_rbx) ^ ((uint8_t)(*(uint8_t *)(local_r13 + 0x10))));
        *(uint8_t *)(local_r13 + 0x10) = (uint8_t)(local_rbx);
    }
    goto loc_00296717;
loc_002969A5:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p18))) ^ ((uint8_t)(v_stack_p10)));
    Arg1 = (uint8_t)((Arg1) ^ (254));
    Arg1 = (uint8_t)((Arg1) & (3));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(v_stack_p18))));
    *(uint8_t *)(v_stack_p18) = (uint8_t)(Arg1);
    goto loc_00296717;
loc_002969C1:
    if ((*(uint64_t *)(arg1)) != (*(uint8_t *)(local_r13 + 0x10))) goto loc_00296739;
    *(void **)(arg1) = Arg1;
    goto loc_002966C0;
loc_002969D2:
    if ((*(uint64_t *)(local_rbx + 0x10)) != Arg1) goto loc_00296739;
    *(uint64_t *)(local_rbx + 0x10) = result;
    goto loc_002967EA;
loc_002969E5:
    result = (*(uint64_t *)(arg1 + 0x10)) & (-4);
    if (result != local_r13) goto loc_00296739;
    a4 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (3));
    a4 = (a4) | (result);
    *(uint64_t *)(arg1 + 0x10) = a4;
    goto loc_002968D3;
loc_00296A09:
    if ((*(uint64_t *)(arg1)) != result) goto loc_00296739;
    *(uint64_t *)(arg1) = local_r13;
    goto loc_002968A6;
loc_00296A1A:
    Arg1 = (uint8_t)((Arg1) & (252));
    *(uint8_t *)(local_r13 + 0x10) = (uint8_t)(Arg1);
    goto loc_00296717;
loc_00296A2C:
    if ((*(uint64_t *)(arg1)) != local_r13) goto loc_00296739;
    *(uint64_t *)(arg1) = local_r13;
    goto loc_002968A6;
loc_00296A3D:
    *(uint64_t *)(local_r13) = a4;
    goto loc_002966B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `8` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00296650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
