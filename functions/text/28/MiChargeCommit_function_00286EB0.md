# MiChargeCommit

- RVA: `0x00286EB0`–`0x00287587` (길이 `1,751` bytes)
- VA: `0x0000000140286EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066CA4`
- 디코드: `383`개 명령, `1,751/1,751` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **44**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00287095` → [MiExtendPageFilesIfNecessary](../47/MiExtendPageFilesIfNecessary_function_00475264.md) (function, `0x00475264`)
- `0x0028710A` → [MiReplenishLocalCommit](../43/MiReplenishLocalCommit_function_0043D920.md) (function, `0x0043D920`)
- `0x00287152` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x002871B8` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002871D4` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002871F6` → [MiIssuePageExtendRequest](../47/MiIssuePageExtendRequest_function_004752F4.md) (function, `0x004752F4`)
- `0x0028724B` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x002872EA` → [MiConsumeOverCommit](../4B/MiConsumeOverCommit_function_004B3E0C.md) (function, `0x004B3E0C`)
- `0x00287342` → [MiPulseCommitSignal](../4D/MiPulseCommitSignal_function_004DEFF4.md) (function, `0x004DEFF4`)
- `0x0028735A` → [MiCauseOverCommitPopup](../48/MiCauseOverCommitPopup_function_0048B2C4.md) (function, `0x0048B2C4`)
- `0x00287370` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x002873A2` → [MiIssuePageExtendRequest](../47/MiIssuePageExtendRequest_function_004752F4.md) (function, `0x004752F4`)
- `0x002873E3` → [MiFreeExcessSegments](../32/MiFreeExcessSegments_function_00327F50.md) (function, `0x00327F50`)
- `0x002873F4` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x0028740A` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x0028741D` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x0028743E` → [MiIssuePageExtendRequest](../47/MiIssuePageExtendRequest_function_004752F4.md) (function, `0x004752F4`)
- `0x00287459` → [MiCauseOverCommitPopup](../48/MiCauseOverCommitPopup_function_0048B2C4.md) (function, `0x0048B2C4`)
- `0x00287461` → [MiPulseCommitSignal](../4D/MiPulseCommitSignal_function_004DEFF4.md) (function, `0x004DEFF4`)
- `0x0028746E` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002874B4` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x002874C4` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002874E8` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x002874FB` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00287502` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00287516` → [MiIssuePageExtendRequest](../47/MiIssuePageExtendRequest_function_004752F4.md) (function, `0x004752F4`)
- `0x00287526` → [MiCauseOverCommitPopup](../48/MiCauseOverCommitPopup_function_0048B2C4.md) (function, `0x0048B2C4`)
- `0x00287566` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00287571` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0028757D` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)

### Direct callers
- [MiGetCloneCharges](../22/MiGetCloneCharges_function_0022CB5C.md) at `0x0022CB97`
- [MiGetCloneCharges](../22/MiGetCloneCharges_function_0022CB5C.md) at `0x0022CBD3`
- [sub_0023C62B](../23/Unknown_function_0023C62B.md) at `0x0023C66A`
- [MiChargeForLockedPage](MiChargeForLockedPage_function_00285AA0.md) at `0x00285BC8`
- [sub_00285C73](Unknown_function_00285C73.md) at `0x00285CA9`
- [MiAcquireNonPagedResources](MiAcquireNonPagedResources_function_00286C60.md) at `0x00286CB0`
- [MiAcquireNonPagedResources](MiAcquireNonPagedResources_function_00286C60.md) at `0x00286D19`
- [MiChargeForWriteInProgressPage](MiChargeForWriteInProgressPage_function_00286D60.md) at `0x00286DE9`
- [MmChargeResources](MmChargeResources_function_002880E0.md) at `0x0028811F`
- [MiCreateUltraThreadContext](MiCreateUltraThreadContext_function_00288200.md) at `0x0028829F`
- [MiObtainFaultCharges](MiObtainFaultCharges_function_0028AEB0.md) at `0x0028AF3C`
- [MiObtainFaultCharges](MiObtainFaultCharges_function_0028AEB0.md) at `0x0028AF89`
- [MiAddLockedPageCharge](MiAddLockedPageCharge_function_0028B550.md) at `0x0028B720`
- [MiHardFaultPageRelease](../2B/MiHardFaultPageRelease_function_002B5728.md) at `0x002B58C4`
- [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) at `0x002B9031`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C4400`
- [MiCreateUltraThreadContextHelper](../2C/MiCreateUltraThreadContextHelper_function_002CB380.md) at `0x002CB3EF`
- [MiReplenishUltraPageTables](../2C/MiReplenishUltraPageTables_function_002CB4EC.md) at `0x002CB5B9`
- [MiCheckProtoPtePageState](../31/MiCheckProtoPtePageState_function_003183E0.md) at `0x003185A9`
- [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) at `0x003210FC`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x00321BDF`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x0032565B`
- [sub_00328FA3](../32/Unknown_function_00328FA3.md) at `0x00329156`
- [sub_0034D947](../34/Unknown_function_0034D947.md) at `0x0034D9A5`
- [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) at `0x003635A3`
- [MiDecommitPrivatePageTail](../36/MiDecommitPrivatePageTail_function_0036F564.md) at `0x0036F738`
- [MiDecommitSharedPageTail](../37/MiDecommitSharedPageTail_function_00370240.md) at `0x003705D3`
- [MiObtainSystemCharges](../37/MiObtainSystemCharges_function_003771F4.md) at `0x00377218`
- [MiInsertInSystemSpace](../3B/MiInsertInSystemSpace_function_003B2F5C.md) at `0x003B33DD`
- [MiCreateLargePfnList](../3D/MiCreateLargePfnList_function_003D2DA8.md) at `0x003D2FFB`
- [NtLockVirtualMemory](../40/NtLockVirtualMemory_function_004088A0.md) at `0x00408C60`
- [MiGetSubsectionCharges](../45/MiGetSubsectionCharges_function_00458A04.md) at `0x00458A7C`
- [MiObtainPoolCharges](../46/MiObtainPoolCharges_function_00460AD8.md) at `0x00460B03`
- [MiSetPagesModified](../49/MiSetPagesModified_function_0049DC2C.md) at `0x0049DCC1`
- [MiReAcquireOutSwappedProcessCommit](../66/MiReAcquireOutSwappedProcessCommit_function_0066F598.md) at `0x0066F63A`
- [MiInitializeCommitment](../68/MiInitializeCommitment_function_0068CC08.md) at `0x0068CD5B`
- [sub_006E3D4A](../6E/Unknown_function_006E3D4A.md) at `0x006E3DA4`
- [sub_006F503A](../6F/Unknown_function_006F503A.md) at `0x006F518E`
- [sub_006F7544](../6F/Unknown_function_006F7544.md) at `0x006F7551`
- [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) at `0x008876C3`
- [MiChargeSegmentCommit](../../page/8C/MiChargeSegmentCommit_function_008CEDE4.md) at `0x008CEF07`
- [MiCreatePagingFileMap](../../page/98/MiCreatePagingFileMap_function_009852F8.md) at `0x00985452`
- [MiCreateImageFileMap](../../page/98/MiCreateImageFileMap_function_00986830.md) at `0x00986DF6`
- [MiCreateFileOnlyImageFixupList](../../page/98/MiCreateFileOnlyImageFixupList_function_00989AD0.md) at `0x00989B6F`
- [MiRotateToFrameBuffer](../../page/A3/MiRotateToFrameBuffer_function_00A38214.md) at `0x00A38304`
- [MmCreateProcessAddressSpace](../../page/A5/MmCreateProcessAddressSpace_function_00A5EE5C.md) at `0x00A5EF08`
- [MiAllocatePerSessionProtos](../../page/A6/MiAllocatePerSessionProtos_function_00A66830.md) at `0x00A66867`

### Static image references
- `0x00286ECD` → RVA `0x00E38D00` (`.data`; read)
- `0x002871C3` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002872D2` → RVA `0x00E30244` (`.data`; read/write)
- `0x002873B7` → RVA `0x00E30240` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0028732A` → [sub_006DA254](../6D/Unknown_function_006DA254.md) (`tail-transfer`)
  - `0x0028755B` → [sub_006DA254 + 0xD2](../6D/Unknown_function_006DA254.md) (`tail-transfer`)
  - `0x0028756C` → [sub_006DA254 + 0xD2](../6D/Unknown_function_006DA254.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00286EB0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00286EB5  55                              push rbp
00286EB6  56                              push rsi
00286EB7  57                              push rdi
00286EB8  41 54                           push r12
00286EBA  41 55                           push r13
00286EBC  41 56                           push r14
00286EBE  41 57                           push r15
00286EC0  48 83 EC 40                     sub rsp, 0x40
00286EC4  41 8B E8                        mov ebp, r8d
00286EC7  48 8B FA                        mov rdi, rdx
00286ECA  48 8B F1                        mov rsi, rcx
00286ECD  48 8D 15 2C 1E BB 00            lea rdx, [rip + 0xbb1e2c]
00286ED4  0F 1F 40 00                     nop dword ptr [rax]
00286ED8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00286EE0  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
00286EE9  48 3B F2                        cmp rsi, rdx
00286EEC  75 57                           jne 0x140286f45
00286EEE  40 F6 C5 10                     test bpl, 0x10
00286EF2  75 51                           jne 0x140286f45
00286EF4  0F 0D 8B 98 8B 00 00            prefetchw byte ptr [rbx + 0x8b98]
00286EFB  8B 8B 98 8B 00 00               mov ecx, dword ptr [rbx + 0x8b98]
00286F01  48 3B F9                        cmp rdi, rcx
00286F04  77 38                           ja 0x140286f3e
00286F06  8B D1                           mov edx, ecx
00286F08  8B C1                           mov eax, ecx
00286F0A  2B D7                           sub edx, edi
00286F0C  F0 0F B1 93 98 8B 00 00         lock cmpxchg dword ptr [rbx + 0x8b98], edx
00286F14  48 63 D0                        movsxd rdx, eax
00286F17  48 3B D1                        cmp rdx, rcx
00286F1A  0F 85 23 03 00 00               jne 0x140287243
00286F20  B8 01 00 00 00                  mov eax, 1
00286F25  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00286F2D  48 83 C4 40                     add rsp, 0x40
00286F31  41 5F                           pop r15
00286F33  41 5E                           pop r14
00286F35  41 5D                           pop r13
00286F37  41 5C                           pop r12
00286F39  5F                              pop rdi
00286F3A  5E                              pop rsi
00286F3B  5D                              pop rbp
00286F3C  C3                              ret
00286F3D  CC                              int3
00286F3E  48 8D 15 BB 1D BB 00            lea rdx, [rip + 0xbb1dbb]
00286F45  44 8B F5                        mov r14d, ebp
00286F48  C7 84 24 80 00 00 00 00 00 00 00  mov dword ptr [rsp + 0x80], 0
00286F53  41 83 CE 02                     or r14d, 2
00286F57  40 F6 C5 04                     test bpl, 4
00286F5B  44 0F 44 F5                     cmove r14d, ebp
00286F5F  41 F6 C6 08                     test r14b, 8
00286F63  0F 84 A4 02 00 00               je 0x14028720d
00286F69  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00286F72  41 83 CE 02                     or r14d, 2
00286F76  8B 88 A4 05 00 00               mov ecx, dword ptr [rax + 0x5a4]
00286F7C  F6 C1 02                        test cl, 2
00286F7F  0F 84 FA 02 00 00               je 0x14028727f
00286F85  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
00286F8D  A9 01 00 01 00                  test eax, 0x10001
00286F92  0F 85 E7 02 00 00               jne 0x14028727f
00286F98  41 83 CE 04                     or r14d, 4
00286F9C  33 C9                           xor ecx, ecx
00286F9E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00286FA3  45 8B E6                        mov r12d, r14d
00286FA6  41 83 E4 04                     and r12d, 4
00286FAA  44 89 A4 24 98 00 00 00         mov dword ptr [rsp + 0x98], r12d
00286FB2  4C 8B AE 40 4B 00 00            mov r13, qword ptr [rsi + 0x4b40]
00286FB9  4E 8D 3C 2F                     lea r15, [rdi + r13]
00286FBD  4D 3B FD                        cmp r15, r13
00286FC0  0F 86 5D 02 00 00               jbe 0x140287223
00286FC6  4A 8D 04 39                     lea rax, [rcx + r15]
00286FCA  49 3B C7                        cmp rax, r15
00286FCD  0F 82 7C 05 00 00               jb 0x14028754f
00286FD3  48 8B 96 98 4C 00 00            mov rdx, qword ptr [rsi + 0x4c98]
00286FDA  48 3B C2                        cmp rax, rdx
00286FDD  0F 87 31 01 00 00               ja 0x140287114
00286FE3  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00286FEB  75 2A                           jne 0x140287017
00286FED  48 8B 86 E8 41 00 00            mov rax, qword ptr [rsi + 0x41e8]
00286FF4  4C 3B F8                        cmp r15, rax
00286FF7  72 1E                           jb 0x140287017
00286FF9  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
00287002  41 F6 C6 04                     test r14b, 4
00287006  0F 84 FE 02 00 00               je 0x14028730a
0028700C  C7 84 24 80 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x80], 1
00287017  49 8B C5                        mov rax, r13
0028701A  F0 4C 0F B1 BE 40 4B 00 00      lock cmpxchg qword ptr [rsi + 0x4b40], r15
00287023  0F 85 3D 03 00 00               jne 0x140287366
00287029  48 8B 96 E0 41 00 00            mov rdx, qword ptr [rsi + 0x41e0]
00287030  48 8D 2C 38                     lea rbp, [rax + rdi]
00287034  48 8B 8E D8 41 00 00            mov rcx, qword ptr [rsi + 0x41d8]
0028703B  48 3B E8                        cmp rbp, rax
0028703E  0F 87 1B 02 00 00               ja 0x14028725f
00287044  48 3B C2                        cmp rax, rdx
00287047  0F 83 E5 04 00 00               jae 0x140287532
0028704D  48 3B C1                        cmp rax, rcx
00287050  0F 83 A6 02 00 00               jae 0x1402872fc
00287056  41 F6 C6 10                     test r14b, 0x10
0028705A  75 1F                           jne 0x14028707b
0028705C  48 8B D7                        mov rdx, rdi
0028705F  F0 48 0F C1 96 80 4B 00 00      lock xadd qword ptr [rsi + 0x4b80], rdx
00287068  48 8B 86 C0 41 00 00            mov rax, qword ptr [rsi + 0x41c0]
0028706F  48 03 D7                        add rdx, rdi
00287072  48 3B D0                        cmp rdx, rax
00287075  0F 87 38 02 00 00               ja 0x1402872b3
0028707B  41 F6 C6 02                     test r14b, 2
0028707F  0F 85 9B FE FF FF               jne 0x140286f20
00287085  48 8B BE 98 4C 00 00            mov rdi, qword ptr [rsi + 0x4c98]
0028708C  48 8B D5                        mov rdx, rbp
0028708F  4C 8B C7                        mov r8, rdi
00287092  48 8B CE                        mov rcx, rsi
00287095  E8 CA E1 1E 00                  call 0x140475264
0028709A  41 F6 C6 01                     test r14b, 1
0028709E  75 10                           jne 0x1402870b0
002870A0  48 8B 86 E0 41 00 00            mov rax, qword ptr [rsi + 0x41e0]
002870A7  48 3B E8                        cmp rbp, rax
002870AA  0F 83 20 03 00 00               jae 0x1402873d0
002870B0  48 8D 05 49 1C BB 00            lea rax, [rip + 0xbb1c49]
002870B7  48 3B F0                        cmp rsi, rax
002870BA  0F 85 60 FE FF FF               jne 0x140286f20
002870C0  8B 83 98 8B 00 00               mov eax, dword ptr [rbx + 0x8b98]
002870C6  48 3D 80 00 00 00               cmp rax, 0x80
002870CC  0F 83 4E FE FF FF               jae 0x140286f20
002870D2  4C 8B C5                        mov r8, rbp
002870D5  41 B9 00 01 00 00               mov r9d, 0x100
002870DB  4C 2B C8                        sub r9, rax
002870DE  49 03 E9                        add rbp, r9
002870E1  49 3B E8                        cmp rbp, r8
002870E4  0F 86 36 FE FF FF               jbe 0x140286f20
002870EA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002870EF  48 03 CD                        add rcx, rbp
002870F2  49 3B C8                        cmp rcx, r8
002870F5  0F 86 25 FE FF FF               jbe 0x140286f20
002870FB  48 3B CF                        cmp rcx, rdi
002870FE  0F 87 1C FE FF FF               ja 0x140286f20
00287104  48 8B D3                        mov rdx, rbx
00287107  48 8B CE                        mov rcx, rsi
0028710A  E8 11 68 1B 00                  call 0x14043d920
0028710F  E9 0C FE FF FF                  jmp 0x140286f20
00287114  48 8B 86 E0 41 00 00            mov rax, qword ptr [rsi + 0x41e0]
0028711B  4C 3B F8                        cmp r15, rax
0028711E  0F 83 12 02 00 00               jae 0x140287336
00287124  41 8B C6                        mov eax, r14d
00287127  83 E0 04                        and eax, 4
0028712A  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
00287131  0F 85 77 02 00 00               jne 0x1402873ae
00287137  44 0F 20 C0                     mov rax, cr8
0028713B  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
00287142  3C 02                           cmp al, 2
00287144  0F 85 01 01 00 00               jne 0x14028724b
0028714A  C6 84 24 90 00 00 00 11         mov byte ptr [rsp + 0x90], 0x11
00287152  E8 D9 1C FC FF                  call 0x140248e30
00287157  B2 11                           mov dl, 0x11
00287159  4C 8B AE 40 4B 00 00            mov r13, qword ptr [rsi + 0x4b40]
00287160  48 8B 8E 98 4C 00 00            mov rcx, qword ptr [rsi + 0x4c98]
00287167  4E 8D 3C 2F                     lea r15, [rdi + r13]
0028716B  4D 3B FD                        cmp r15, r13
0028716E  0F 86 A2 02 00 00               jbe 0x140287416
00287174  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00287179  49 03 C7                        add rax, r15
0028717C  49 3B C7                        cmp rax, r15
0028717F  0F 82 91 02 00 00               jb 0x140287416
00287185  48 3B C1                        cmp rax, rcx
00287188  0F 86 5F 02 00 00               jbe 0x1402873ed
0028718E  41 F6 C6 02                     test r14b, 2
00287192  0F 85 6B 02 00 00               jne 0x140287403
00287198  48 8B 86 C8 41 00 00            mov rax, qword ptr [rsi + 0x41c8]
0028719F  48 3B C8                        cmp rcx, rax
002871A2  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
002871A9  0F 84 C1 01 00 00               je 0x140287370
002871AF  44 0F B6 BC 24 90 00 00 00      movzx r15d, byte ptr [rsp + 0x90]
002871B8  E8 D3 33 FC FF                  call 0x14024a590
002871BD  41 80 FF 11                     cmp r15b, 0x11
002871C1  74 1A                           je 0x1402871dd
002871C3  83 3D 56 FB D3 00 00            cmp dword ptr [rip + 0xd3fb56], 0
002871CA  74 0D                           je 0x1402871d9
002871CC  44 0F 20 C1                     mov rcx, cr8
002871D0  41 0F B6 D7                     movzx edx, r15b
002871D4  E8 BF E4 26 00                  call 0x1404f5698
002871D9  45 0F 22 C7                     mov cr8, r15
002871DD  48 8B CE                        mov rcx, rsi
002871E0  41 F6 C6 01                     test r14b, 1
002871E4  0F 85 42 02 00 00               jne 0x14028742c
002871EA  41 B9 FF 00 00 00               mov r9d, 0xff
002871F0  45 33 C0                        xor r8d, r8d
002871F3  48 8B D7                        mov rdx, rdi
002871F6  E8 F9 E0 1E 00                  call 0x1404752f4
002871FB  85 C0                           test eax, eax
002871FD  0F 84 4E 01 00 00               je 0x140287351
00287203  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00287208  E9 96 FD FF FF                  jmp 0x140286fa3
0028720D  41 F6 C6 07                     test r14b, 7
00287211  0F 85 18 01 00 00               jne 0x14028732f
00287217  48 8B 8E 00 42 00 00            mov rcx, qword ptr [rsi + 0x4200]
0028721E  E9 7B FD FF FF                  jmp 0x140286f9e
00287223  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
0028722A  85 C0                           test eax, eax
0028722C  0F 85 9B 00 00 00               jne 0x1402872cd
00287232  41 F6 C6 02                     test r14b, 2
00287236  0F 84 0E 02 00 00               je 0x14028744a
0028723C  33 C0                           xor eax, eax
0028723E  E9 E2 FC FF FF                  jmp 0x140286f25
00287243  48 8B CA                        mov rcx, rdx
00287246  E9 B6 FC FF FF                  jmp 0x140286f01
0028724B  E8 90 6A FC FF                  call 0x14024dce0
00287250  0F B6 D0                        movzx edx, al
00287253  88 84 24 90 00 00 00            mov byte ptr [rsp + 0x90], al
0028725A  E9 FA FE FF FF                  jmp 0x140287159
0028725F  48 3B EA                        cmp rbp, rdx
00287262  0F 83 5A 01 00 00               jae 0x1402873c2
00287268  48 3B E9                        cmp rbp, rcx
0028726B  0F 82 E5 FD FF FF               jb 0x140287056
00287271  48 3B C1                        cmp rax, rcx
00287274  0F 83 DC FD FF FF               jae 0x140287056
0028727A  E9 BC 02 00 00                  jmp 0x14028753b
0028727F  B9 40 00 00 00                  mov ecx, 0x40
00287284  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00287289  48 3B F2                        cmp rsi, rdx
0028728C  0F 84 11 FD FF FF               je 0x140286fa3
00287292  48 8B 86 50 48 00 00            mov rax, qword ptr [rsi + 0x4850]
00287299  48 C1 E8 06                     shr rax, 6
0028729D  48 3B C1                        cmp rax, rcx
002872A0  0F 83 FD FC FF FF               jae 0x140286fa3
002872A6  48 8B C8                        mov rcx, rax
002872A9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002872AE  E9 F0 FC FF FF                  jmp 0x140286fa3
002872B3  48 8B C8                        mov rcx, rax
002872B6  F0 48 0F B1 96 C0 41 00 00      lock cmpxchg qword ptr [rsi + 0x41c0], rdx
002872BF  48 3B C8                        cmp rcx, rax
002872C2  0F 85 AA FD FF FF               jne 0x140287072
002872C8  E9 AE FD FF FF                  jmp 0x14028707b
002872CD  48 85 C9                        test rcx, rcx
002872D0  75 06                           jne 0x1402872d8
002872D2  FF 05 6C 8F BA 00               inc dword ptr [rip + 0xba8f6c]
002872D8  48 85 FF                        test rdi, rdi
002872DB  0F 84 36 FD FF FF               je 0x140287017
002872E1  4C 8B C1                        mov r8, rcx
002872E4  48 8B D7                        mov rdx, rdi
002872E7  48 8B CE                        mov rcx, rsi
002872EA  E8 1D CB 22 00                  call 0x1404b3e0c
002872EF  85 C0                           test eax, eax
002872F1  0F 84 D6 FB FF FF               je 0x140286ecd
002872F7  E9 24 FC FF FF                  jmp 0x140286f20
002872FC  48 3B E9                        cmp rbp, rcx
002872FF  0F 83 51 FD FF FF               jae 0x140287056
00287305  E9 31 02 00 00                  jmp 0x14028753b
0028730A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00287313  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028731A  F7 81 FC 05 00 00 00 10 00 00   test dword ptr [rcx + 0x5fc], 0x1000
00287324  0F 85 E2 FC FF FF               jne 0x14028700c
0028732A  E9 25 2F 45 00                  jmp 0x1406da254
0028732F  33 C9                           xor ecx, ecx
00287331  E9 68 FC FF FF                  jmp 0x140286f9e
00287336  4C 3B E8                        cmp r13, rax
00287339  0F 83 E5 FD FF FF               jae 0x140287124
0028733F  48 8B CE                        mov rcx, rsi
00287342  E8 AD 7C 25 00                  call 0x1404deff4
00287347  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0028734C  E9 D3 FD FF FF                  jmp 0x140287124
00287351  FF 86 F0 4C 00 00               inc dword ptr [rsi + 0x4cf0]
00287357  48 8B CE                        mov rcx, rsi
0028735A  E8 65 3F 20 00                  call 0x14048b2c4
0028735F  33 C0                           xor eax, eax
00287361  E9 BF FB FF FF                  jmp 0x140286f25
00287366  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0028736B  E9 33 FC FF FF                  jmp 0x140286fa3
00287370  E8 7B 18 0C 00                  call 0x140348bf0
00287375  FF 86 F4 4C 00 00               inc dword ptr [rsi + 0x4cf4]
0028737B  48 8D 05 7E 19 BB 00            lea rax, [rip + 0xbb197e]
00287382  48 3B F0                        cmp rsi, rax
00287385  0F 85 B1 FE FF FF               jne 0x14028723c
0028738B  45 33 C9                        xor r9d, r9d
0028738E  48 8B D7                        mov rdx, rdi
00287391  48 8B CE                        mov rcx, rsi
00287394  41 F6 C6 01                     test r14b, 1
00287398  0F 84 72 01 00 00               je 0x140287510
0028739E  45 8D 41 0A                     lea r8d, [r9 + 0xa]
002873A2  E8 4D DF 1E 00                  call 0x1404752f4
002873A7  33 C0                           xor eax, eax
002873A9  E9 77 FB FF FF                  jmp 0x140286f25
002873AE  48 85 C9                        test rcx, rcx
002873B1  0F 85 21 FF FF FF               jne 0x1402872d8
002873B7  FF 05 83 8E BA 00               inc dword ptr [rip + 0xba8e83]
002873BD  E9 16 FF FF FF                  jmp 0x1402872d8
002873C2  48 3B C2                        cmp rax, rdx
002873C5  0F 82 70 01 00 00               jb 0x14028753b
002873CB  E9 98 FE FF FF                  jmp 0x140287268
002873D0  48 8B 86 C8 41 00 00            mov rax, qword ptr [rsi + 0x41c8]
002873D7  48 3B F8                        cmp rdi, rax
002873DA  0F 85 D0 FC FF FF               jne 0x1402870b0
002873E0  48 8B CE                        mov rcx, rsi
002873E3  E8 68 0B 0A 00                  call 0x140327f50
002873E8  E9 C3 FC FF FF                  jmp 0x1402870b0
002873ED  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
002873F4  E8 F7 17 0C 00                  call 0x140348bf0
002873F9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002873FE  E9 A0 FB FF FF                  jmp 0x140286fa3
00287403  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
0028740A  E8 E1 17 0C 00                  call 0x140348bf0
0028740F  33 C0                           xor eax, eax
00287411  E9 0F FB FF FF                  jmp 0x140286f25
00287416  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
0028741D  E8 CE 17 0C 00                  call 0x140348bf0
00287422  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00287427  E9 86 FB FF FF                  jmp 0x140286fb2
0028742C  FF 86 F8 4C 00 00               inc dword ptr [rsi + 0x4cf8]
00287432  45 33 C9                        xor r9d, r9d
00287435  BA 00 10 00 00                  mov edx, 0x1000
0028743A  45 8D 41 02                     lea r8d, [r9 + 2]
0028743E  E8 B1 DE 1E 00                  call 0x1404752f4
00287443  33 C0                           xor eax, eax
00287445  E9 DB FA FF FF                  jmp 0x140286f25
0028744A  FF 86 FC 4C 00 00               inc dword ptr [rsi + 0x4cfc]
00287450  41 F6 C6 01                     test r14b, 1
00287454  75 08                           jne 0x14028745e
00287456  48 8B CE                        mov rcx, rsi
00287459  E8 66 3E 20 00                  call 0x14048b2c4
0028745E  48 8B CE                        mov rcx, rsi
00287461  E8 8E 7B 25 00                  call 0x1404deff4
00287466  E9 D1 FD FF FF                  jmp 0x14028723c
0028746B  41 B4 11                        mov r12b, 0x11
0028746E  E8 0D 1A FC FF                  call 0x140248e80
00287473  48 8B 96 40 4B 00 00            mov rdx, qword ptr [rsi + 0x4b40]
0028747A  48 8B 8E D8 41 00 00            mov rcx, qword ptr [rsi + 0x41d8]
00287481  4C 8B 86 E0 41 00 00            mov r8, qword ptr [rsi + 0x41e0]
00287488  48 3B D1                        cmp rdx, rcx
0028748B  72 41                           jb 0x1402874ce
0028748D  48 8B 8E 30 01 00 00            mov rcx, qword ptr [rsi + 0x130]
00287494  49 3B D0                        cmp rdx, r8
00287497  0F 83 BA 00 00 00               jae 0x140287557
0028749D  83 79 04 01                     cmp dword ptr [rcx + 4], 1
002874A1  0F 84 CA 00 00 00               je 0x140287571
002874A7  48 8B 8E 28 01 00 00            mov rcx, qword ptr [rsi + 0x128]
002874AE  83 79 04 01                     cmp dword ptr [rcx + 4], 1
002874B2  75 05                           jne 0x1402874b9
002874B4  E8 97 0E FC FF                  call 0x140248350
002874B9  41 0F B6 D4                     movzx edx, r12b
002874BD  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
002874C4  E8 F7 0D FC FF                  call 0x1402482c0
002874C9  E9 88 FB FF FF                  jmp 0x140287056
002874CE  48 8B 8E 28 01 00 00            mov rcx, qword ptr [rsi + 0x128]
002874D5  83 79 04 00                     cmp dword ptr [rcx + 4], 0
002874D9  74 1B                           je 0x1402874f6
002874DB  48 8B 8E 30 01 00 00            mov rcx, qword ptr [rsi + 0x130]
002874E2  83 79 04 01                     cmp dword ptr [rcx + 4], 1
002874E6  75 D1                           jne 0x1402874b9
002874E8  E8 63 0E FC FF                  call 0x140248350
002874ED  48 8B 8E 38 01 00 00            mov rcx, qword ptr [rsi + 0x138]
002874F4  EB BE                           jmp 0x1402874b4
002874F6  45 33 C0                        xor r8d, r8d
002874F9  33 D2                           xor edx, edx
002874FB  E8 10 7E 0B 00                  call 0x14033f310
00287500  EB D9                           jmp 0x1402874db
00287502  E8 89 11 FC FF                  call 0x140248690
00287507  44 0F B6 E0                     movzx r12d, al
0028750B  E9 63 FF FF FF                  jmp 0x140287473
00287510  41 B8 08 00 00 00               mov r8d, 8
00287516  E8 D9 DD 1E 00                  call 0x1404752f4
0028751B  85 C0                           test eax, eax
0028751D  0F 85 F4 FA FF FF               jne 0x140287017
00287523  48 8B CE                        mov rcx, rsi
00287526  E8 99 3D 20 00                  call 0x14048b2c4
0028752B  33 C0                           xor eax, eax
0028752D  E9 F3 F9 FF FF                  jmp 0x140286f25
00287532  48 3B EA                        cmp rbp, rdx
00287535  0F 83 12 FB FF FF               jae 0x14028704d
0028753B  44 0F 20 C0                     mov rax, cr8
0028753F  48 8D 8E F8 41 00 00            lea rcx, [rsi + 0x41f8]
00287546  3C 02                           cmp al, 2
00287548  75 B8                           jne 0x140287502
0028754A  E9 1C FF FF FF                  jmp 0x14028746b
0028754F  41 8B C4                        mov eax, r12d
00287552  E9 D3 FC FF FF                  jmp 0x14028722a
00287557  83 79 04 00                     cmp dword ptr [rcx + 4], 0
0028755B  0F 85 C5 2D 45 00               jne 0x1406da326
00287561  45 33 C0                        xor r8d, r8d
00287564  33 D2                           xor edx, edx
00287566  E8 A5 7D 0B 00                  call 0x14033f310
0028756B  90                              nop
0028756C  E9 B5 2D 45 00                  jmp 0x1406da326
00287571  E8 DA 0D FC FF                  call 0x140248350
00287576  48 8B 8E 38 01 00 00            mov rcx, qword ptr [rsi + 0x138]
0028757D  E8 CE 0D FC FF                  call 0x140248350
00287582  E9 20 FF FF FF                  jmp 0x1402874a7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiChargeCommit(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p80;
    unsigned __int8 v_stack_p90;
    unsigned int v_stack_p98;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (64);
loc_00286ECD:
    if (a1 != (v_rip + 12262956)) goto loc_00286F45;
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) != 0) goto loc_00286F45;
loc_00286F01:
    if (a2 > ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736)))) goto loc_00286F3E;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736))))) - ((unsigned int)(a2)));
    if (((int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736))))))) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35736)))) goto loc_00287243;
loc_00286F20:
loc_00286F25:
    v_rsp = (v_rsp) + (64);
    return 1;
loc_00286F3E:
loc_00286F45:
    v_stack_p80 = 0;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) | (2));
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) == 0) { v_r14 = (unsigned int)((unsigned int)(a3)); }
    if ((((unsigned __int8)(v_r14)) & (8)) == 0) goto loc_0028720D;
    v_r14 = (unsigned int)((v_r14) | (2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (2)) == 0) goto loc_0028727F;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) goto loc_0028727F;
    v_r14 = (unsigned int)((v_r14) | (4));
    a1 = 0;
loc_00286F9E:
    v_stack_p30 = 0;
loc_00286FA3:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (4));
    v_stack_p98 = (unsigned int)(v_r12);
loc_00286FB2:
    if ((a2 + *(unsigned __int64 *)(a1 + 19264) * 1) <= (*(unsigned __int64 *)(a1 + 19264))) goto loc_00287223;
    if ((a1 + a2 + *(unsigned __int64 *)(a1 + 19264) * 1 * 1) < (a2 + *(unsigned __int64 *)(a1 + 19264) * 1)) goto loc_0028754F;
    if ((a1 + a2 + *(unsigned __int64 *)(a1 + 19264) * 1 * 1) > (*(unsigned __int64 *)(a1 + 19608))) goto loc_00287114;
    if (v_stack_p80 != 0) goto loc_00287017;
    if ((a2 + *(unsigned __int64 *)(a1 + 19264) * 1) < (*(unsigned __int64 *)(a1 + 16872))) goto loc_00287017;
    v_stack_p38 = 0;
    if ((((unsigned __int8)(v_r14)) & (4)) == 0) goto loc_0028730A;
loc_0028700C:
    v_stack_p80 = 1;
loc_00287017:
    if ((((unsigned __int8)(v_r14)) & (4)) != 0) goto loc_00287366;
    if ((*(unsigned __int64 *)(a1 + 19264) + a2 * 1) > (*(unsigned __int64 *)(a1 + 19264))) goto loc_0028725F;
    if ((*(unsigned __int64 *)(a1 + 19264)) >= (*(unsigned __int64 *)(a1 + 16864))) goto loc_00287532;
loc_0028704D:
    if ((*(unsigned __int64 *)(a1 + 19264)) >= (*(unsigned __int64 *)(a1 + 16856))) goto loc_002872FC;
loc_00287056:
    if ((((unsigned __int8)(v_r14)) & (16)) != 0) goto loc_0028707B;
    a2 = (a2) + (a2);
loc_00287072:
    if (a2 > (*(unsigned __int64 *)(a1 + 16832))) goto loc_002872B3;
loc_0028707B:
    if ((((unsigned __int8)(v_r14)) & (2)) != 0) goto loc_00286F20;
    result = MiExtendPageFilesIfNecessary(0, *(unsigned __int64 *)(a1 + 19264) + a2 * 1, *(unsigned __int64 *)(a1 + 19608), a4);
    if ((((unsigned __int8)(v_r14)) & (1)) != 0) goto loc_002870B0;
    if ((*(unsigned __int64 *)(a1 + 19264) + a2 * 1) >= (*(unsigned __int64 *)(a1 + 16864))) goto loc_002873D0;
loc_002870B0:
    if (0 != (v_rip + 12262473)) goto loc_00286F20;
    if (((unsigned int)(*(unsigned int *)(v_stack_p10 + 35736))) >= 128) goto loc_00286F20;
    a4 = (256) - ((unsigned int)(*(unsigned int *)(v_stack_p10 + 35736)));
    v_rbp = (*(unsigned __int64 *)(a1 + 19264) + a2 * 1) + (a4);
    if (v_rbp <= (*(unsigned __int64 *)(a1 + 19264) + a2 * 1)) goto loc_00286F20;
    a1 = (v_stack_p30) + (v_rbp);
    if (a1 <= (*(unsigned __int64 *)(a1 + 19264) + a2 * 1)) goto loc_00286F20;
    if (a1 > (*(unsigned __int64 *)(a1 + 19608))) goto loc_00286F20;
    result = MiReplenishLocalCommit(a1, v_stack_p10, *(unsigned __int64 *)(a1 + 19264) + a2 * 1, a4);
    goto loc_00286F20;
loc_00287114:
    if ((a2 + *(unsigned __int64 *)(a1 + 19264) * 1) >= (*(unsigned __int64 *)(a1 + 16864))) goto loc_00287336;
loc_00287124:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (4));
    v_stack_p98 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_002873AE;
    if (((unsigned __int8)(v_cr8)) != 2) goto loc_0028724B;
    v_stack_p90 = 17;
    result = ExAcquireSpinLockSharedAtDpcLevel(a1 + 16888, v_stack_p10, *(unsigned __int64 *)(a1 + 19264) + a2 * 1, a4);
loc_00287159:
    if ((*(unsigned __int64 *)(a1 + 19608) + *(unsigned __int64 *)(a1 + 19264) * 1) <= (*(unsigned __int64 *)(a1 + 19264))) goto loc_00287416;
    result = (v_stack_p30) + (*(unsigned __int64 *)(a1 + 19608) + *(unsigned __int64 *)(a1 + 19264) * 1);
    if (result < (*(unsigned __int64 *)(a1 + 19608) + *(unsigned __int64 *)(a1 + 19264) * 1)) goto loc_00287416;
    if (result <= (*(unsigned __int64 *)(a1 + 19608))) goto loc_002873ED;
    if ((((unsigned __int8)(v_r14)) & (2)) != 0) goto loc_00287403;
    if ((*(unsigned __int64 *)(a1 + 19608)) == (*(unsigned __int64 *)(a1 + 16840))) goto loc_00287370;
    result = ExReleaseSpinLockSharedFromDpcLevel(a1 + 16888, 17, *(unsigned __int64 *)(a1 + 19264) + a2 * 1, a4);
    if (((unsigned __int8)(v_stack_p90)) == 17) goto loc_002871DD;
    if ((*(unsigned int *)(v_rip + 13892438)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_p90);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(a1 + 19264) + a2 * 1, a4);
    }
loc_002871DD:
    if ((((unsigned __int8)(v_r14)) & (1)) != 0) goto loc_0028742C;
    a3 = 0;
    result = MiIssuePageExtendRequest(a1, *(unsigned __int64 *)(a1 + 19608), a3, 255);
    if ((unsigned int)(result) == 0) goto loc_00287351;
    goto loc_00286FA3;
loc_0028720D:
    if ((((unsigned __int8)(v_r14)) & (7)) != 0) goto loc_0028732F;
    goto loc_00286F9E;
loc_00287223:
loc_0028722A:
    if ((unsigned int)((unsigned int)(v_stack_p98)) != 0) goto loc_002872CD;
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) goto loc_0028744A;
loc_0028723C:
    result = 0;
    goto loc_00286F25;
loc_00287243:
    goto loc_00286F01;
loc_0028724B:
    result = ExAcquireSpinLockShared(*(unsigned __int64 *)(a1 + 19608), *(unsigned __int64 *)(a1 + 19608), a3, 255);
    v_stack_p90 = (unsigned __int8)(result);
    goto loc_00287159;
loc_0028725F:
    if (v_rbp >= ((unsigned __int8)(result))) goto loc_002873C2;
loc_00287268:
    if (v_rbp < (*(unsigned __int64 *)(a1 + 19608))) goto loc_00287056;
    if (result >= (*(unsigned __int64 *)(a1 + 19608))) goto loc_00287056;
    goto loc_0028753B;
loc_0028727F:
    v_stack_p30 = 64;
    if (a1 == ((unsigned __int8)(result))) goto loc_00286FA3;
    result = (*(unsigned __int64 *)(a1 + 18512)) >> (6);
    if (result >= 64) goto loc_00286FA3;
    v_stack_p30 = result;
    goto loc_00286FA3;
loc_002872B3:
    if (result != result) goto loc_00287072;
    goto loc_0028707B;
loc_002872CD:
    if (result == 0) {
    }
    if (*(unsigned __int64 *)(a1 + 19608) == 0) goto loc_00287017;
    result = MiConsumeOverCommit(a1, *(unsigned __int64 *)(a1 + 19608), result, 255);
    if ((unsigned int)(result) == 0) goto loc_00286ECD;
    goto loc_00286F20;
loc_002872FC:
    if (v_rbp >= a1) goto loc_00287056;
    goto loc_0028753B;
loc_0028730A:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)) & (0x1000ULL)) != 0) goto loc_0028700C;
loc_0028732F:
    a1 = 0;
    goto loc_00286F9E;
loc_00287336:
    if ((*(unsigned __int64 *)(a1 + 19264)) >= (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00287124;
    result = MiPulseCommitSignal(0, *(unsigned __int64 *)(a1 + 19608), result, 255);
    goto loc_00287124;
loc_00287351:
    result = MiCauseOverCommitPopup(0, *(unsigned __int64 *)(a1 + 19608), result, 255);
    result = 0;
    goto loc_00286F25;
loc_00287366:
    goto loc_00286FA3;
loc_00287370:
    result = MiReleaseSpinLockShared(v_stack_p30, *(unsigned __int64 *)(a1 + 19608), result, 255);
    if (0 != (v_rip + 12261758)) goto loc_0028723C;
    a4 = 0;
    if ((((unsigned __int8)(v_r14)) & (1)) == 0) goto loc_00287510;
    result = MiIssuePageExtendRequest(0, *(unsigned __int64 *)(a1 + 19608), a4 + 10, a4);
    result = 0;
    goto loc_00286F25;
loc_002873AE:
    if (0 != 0) goto loc_002872D8;
    goto loc_002872D8;
loc_002873C2:
    if (0 < (*(unsigned __int64 *)(a1 + 19608))) goto loc_0028753B;
    goto loc_00287268;
loc_002873D0:
    if ((*(unsigned __int64 *)(a1 + 19608)) != (*(unsigned __int64 *)(a1 + 16840))) goto loc_002870B0;
    result = MiFreeExcessSegments(0, *(unsigned __int64 *)(a1 + 19608), a4 + 10, a4);
    goto loc_002870B0;
loc_002873ED:
    result = MiReleaseSpinLockShared(a1 + 16888, *(unsigned __int64 *)(a1 + 19608), a4 + 10, a4);
    goto loc_00286FA3;
loc_00287403:
    result = MiReleaseSpinLockShared(a1 + 16888, *(unsigned __int64 *)(a1 + 19608), a4 + 10, a4);
    result = 0;
    goto loc_00286F25;
loc_00287416:
    result = MiReleaseSpinLockShared(a1 + 16888, *(unsigned __int64 *)(a1 + 19608), a4 + 10, a4);
    goto loc_00286FB2;
loc_0028742C:
    a4 = 0;
    result = MiIssuePageExtendRequest(v_stack_p30, (unsigned int)(0x1000ULL), a4 + 2, a4);
    result = 0;
    goto loc_00286F25;
loc_0028744A:
    if ((((unsigned __int8)(v_r14)) & (1)) == 0) {
        a1 = 0;
        result = MiCauseOverCommitPopup(a1, (unsigned int)(0x1000ULL), a4 + 2, a4);
    }
    result = MiPulseCommitSignal(a1, (unsigned int)(0x1000ULL), a4 + 2, a4);
    goto loc_0028723C;
loc_0028746B:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, (unsigned int)(0x1000ULL), a4 + 2, a4);
loc_00287473:
    if ((*(unsigned __int64 *)(a1 + 19264)) < (*(unsigned __int64 *)(a1 + 16856))) goto loc_002874CE;
    if ((*(unsigned __int64 *)(a1 + 19264)) >= (*(unsigned __int64 *)(a1 + 16864))) goto loc_00287557;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 304) + 4)) == 1) goto loc_00287571;
loc_002874A7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 296) + 4)) == 1) {
        result = KeResetEvent(*(unsigned __int64 *)(a1 + 296), *(unsigned __int64 *)(a1 + 19264), *(unsigned __int64 *)(a1 + 16864), a4);
    }
    result = MiReleaseSpinLockExclusive(a1 + 16888, 17, *(unsigned __int64 *)(a1 + 16864), a4);
    goto loc_00287056;
loc_002874CE:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 296) + 4)) == 0) goto loc_002874F6;
loc_002874DB:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 304) + 4)) != 1) goto loc_002874B9;
    result = KeResetEvent(*(unsigned __int64 *)(a1 + 304), 17, *(unsigned __int64 *)(a1 + 16864), a4);
    goto loc_002874B4;
loc_002874F6:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 312), a2, a3, a4);
    goto loc_002874DB;
loc_00287502:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1 + 312), a2, a3, a4);
    goto loc_00287473;
loc_00287510:
    result = MiIssuePageExtendRequest(*(unsigned __int64 *)(a1 + 312), a2, 8, a4);
    if ((unsigned int)(result) != 0) goto loc_00287017;
    result = MiCauseOverCommitPopup(a1, a2, 8, a4);
    result = 0;
    goto loc_00286F25;
loc_00287532:
    if (v_rbp >= 0) goto loc_0028704D;
loc_0028753B:
    if (((unsigned __int8)(v_stack_p90)) != 2) goto loc_00287502;
    goto loc_0028746B;
loc_0028754F:
    goto loc_0028722A;
loc_00287557:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a1 + 16888, a2, a3, a4);
loc_00287571:
    result = KeResetEvent(a1 + 16888, a2, a3, a4);
    result = KeResetEvent(*(unsigned __int64 *)(a1 + 312), a2, a3, a4);
    goto loc_002874A7;
}
```

## 5. (Beta) C Style

```c
int64_t MiChargeCommit(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p80;
    uint8_t v_stack_p90;
    uint32_t v_stack_p98;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (64);
loc_00286ECD:
    if (Arg1 != (v_rip + 12262956)) goto loc_00286F45;
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) != 0) goto loc_00286F45;
loc_00286F01:
    if (Arg2 > ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98)))) goto loc_00286F3E;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98))))) - ((uint32_t)(Arg2)));
    if (((int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98))))))) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B98)))) goto loc_00287243;
loc_00286F20:
loc_00286F25:
    local_rsp = (local_rsp) + (64);
    return 1;
loc_00286F3E:
loc_00286F45:
    v_stack_p80 = 0;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) | (2));
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) == 0) { local_r14 = (uint32_t)((uint32_t)(Arg3)); }
    if ((((uint8_t)(local_r14)) & (8)) == 0) goto loc_0028720D;
    local_r14 = (uint32_t)((local_r14) | (2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (2)) == 0) goto loc_0028727F;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) goto loc_0028727F;
    local_r14 = (uint32_t)((local_r14) | (4));
    Arg1 = 0;
loc_00286F9E:
    v_stack_p30 = 0;
loc_00286FA3:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (4));
    v_stack_p98 = (uint32_t)(local_r12);
loc_00286FB2:
    if ((Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1) <= (*(uint64_t *)(Arg1 + 0x4B40))) goto loc_00287223;
    if ((Arg1 + Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1 * 1) < (Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1)) goto loc_0028754F;
    if ((Arg1 + Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1 * 1) > (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_00287114;
    if (v_stack_p80 != 0) goto loc_00287017;
    if ((Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1) < (*(uint64_t *)(Arg1 + 0x41E8))) goto loc_00287017;
    v_stack_p38 = 0;
    if ((((uint8_t)(local_r14)) & (4)) == 0) goto loc_0028730A;
loc_0028700C:
    v_stack_p80 = 1;
loc_00287017:
    if ((((uint8_t)(local_r14)) & (4)) != 0) goto loc_00287366;
    if ((*(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1) > (*(uint64_t *)(Arg1 + 0x4B40))) goto loc_0028725F;
    if ((*(uint64_t *)(Arg1 + 0x4B40)) >= (*(uint64_t *)(Arg1 + 0x41E0))) goto loc_00287532;
loc_0028704D:
    if ((*(uint64_t *)(Arg1 + 0x4B40)) >= (*(uint64_t *)(Arg1 + 0x41D8))) goto loc_002872FC;
loc_00287056:
    if ((((uint8_t)(local_r14)) & (16)) != 0) goto loc_0028707B;
    Arg2 = (Arg2) + (Arg2);
loc_00287072:
    if (Arg2 > (*(uint64_t *)(Arg1 + 0x41C0))) goto loc_002872B3;
loc_0028707B:
    if ((((uint8_t)(local_r14)) & (2)) != 0) goto loc_00286F20;
    result = MiExtendPageFilesIfNecessary(0, *(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1, *(uint64_t *)(Arg1 + 0x4C98), a4);
    if ((((uint8_t)(local_r14)) & (1)) != 0) goto loc_002870B0;
    if ((*(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1) >= (*(uint64_t *)(Arg1 + 0x41E0))) goto loc_002873D0;
loc_002870B0:
    if (0 != (v_rip + 12262473)) goto loc_00286F20;
    if (((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x8B98))) >= 128) goto loc_00286F20;
    a4 = (256) - ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x8B98)));
    local_rbp = (*(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1) + (a4);
    if (local_rbp <= (*(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1)) goto loc_00286F20;
    Arg1 = (v_stack_p30) + (local_rbp);
    if (Arg1 <= (*(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1)) goto loc_00286F20;
    if (Arg1 > (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_00286F20;
    result = MiReplenishLocalCommit(Arg1, v_stack_p10, *(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1, a4);
    goto loc_00286F20;
loc_00287114:
    if ((Arg2 + *(uint64_t *)(Arg1 + 0x4B40) * 1) >= (*(uint64_t *)(Arg1 + 0x41E0))) goto loc_00287336;
loc_00287124:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (4));
    v_stack_p98 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_002873AE;
    if (((uint8_t)(v_cr8)) != 2) goto loc_0028724B;
    v_stack_p90 = 17;
    result = ExAcquireSpinLockSharedAtDpcLevel(Arg1 + 16888, v_stack_p10, *(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1, a4);
loc_00287159:
    if ((*(uint64_t *)(Arg1 + 0x4C98) + *(uint64_t *)(Arg1 + 0x4B40) * 1) <= (*(uint64_t *)(Arg1 + 0x4B40))) goto loc_00287416;
    result = (v_stack_p30) + (*(uint64_t *)(Arg1 + 0x4C98) + *(uint64_t *)(Arg1 + 0x4B40) * 1);
    if (result < (*(uint64_t *)(Arg1 + 0x4C98) + *(uint64_t *)(Arg1 + 0x4B40) * 1)) goto loc_00287416;
    if (result <= (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_002873ED;
    if ((((uint8_t)(local_r14)) & (2)) != 0) goto loc_00287403;
    if ((*(uint64_t *)(Arg1 + 0x4C98)) == (*(uint64_t *)(Arg1 + 0x41C8))) goto loc_00287370;
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1 + 16888, 17, *(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1, a4);
    if (((uint8_t)(v_stack_p90)) == 17) goto loc_002871DD;
    if ((*(uint32_t *)(v_rip + 0xD3FB56)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_p90);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(Arg1 + 0x4B40) + Arg2 * 1, a4);
    }
loc_002871DD:
    if ((((uint8_t)(local_r14)) & (1)) != 0) goto loc_0028742C;
    Arg3 = 0;
    result = MiIssuePageExtendRequest(Arg1, *(uint64_t *)(Arg1 + 0x4C98), Arg3, 255);
    if ((uint32_t)(result) == 0) goto loc_00287351;
    goto loc_00286FA3;
loc_0028720D:
    if ((((uint8_t)(local_r14)) & (7)) != 0) goto loc_0028732F;
    goto loc_00286F9E;
loc_00287223:
loc_0028722A:
    if ((uint32_t)((uint32_t)(v_stack_p98)) != 0) goto loc_002872CD;
    if ((((uint8_t)(local_r14)) & (2)) == 0) goto loc_0028744A;
loc_0028723C:
    result = 0;
    goto loc_00286F25;
loc_00287243:
    goto loc_00286F01;
loc_0028724B:
    result = ExAcquireSpinLockShared(*(uint64_t *)(Arg1 + 0x4C98), *(uint64_t *)(Arg1 + 0x4C98), Arg3, 255);
    v_stack_p90 = (uint8_t)(result);
    goto loc_00287159;
loc_0028725F:
    if (local_rbp >= ((uint8_t)(result))) goto loc_002873C2;
loc_00287268:
    if (local_rbp < (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_00287056;
    if (result >= (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_00287056;
    goto loc_0028753B;
loc_0028727F:
    v_stack_p30 = 64;
    if (Arg1 == ((uint8_t)(result))) goto loc_00286FA3;
    result = (*(uint64_t *)(Arg1 + 0x4850)) >> (6);
    if (result >= 64) goto loc_00286FA3;
    v_stack_p30 = result;
    goto loc_00286FA3;
loc_002872B3:
    if (result != result) goto loc_00287072;
    goto loc_0028707B;
loc_002872CD:
    if (result == 0) {
    }
    if (*(uint64_t *)(Arg1 + 0x4C98) == 0) goto loc_00287017;
    result = MiConsumeOverCommit(Arg1, *(uint64_t *)(Arg1 + 0x4C98), result, 255);
    if ((uint32_t)(result) == 0) goto loc_00286ECD;
    goto loc_00286F20;
loc_002872FC:
    if (local_rbp >= Arg1) goto loc_00287056;
    goto loc_0028753B;
loc_0028730A:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)) & (0x1000ULL)) != 0) goto loc_0028700C;
loc_0028732F:
    Arg1 = 0;
    goto loc_00286F9E;
loc_00287336:
    if ((*(uint64_t *)(Arg1 + 0x4B40)) >= (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00287124;
    result = MiPulseCommitSignal(0, *(uint64_t *)(Arg1 + 0x4C98), result, 255);
    goto loc_00287124;
loc_00287351:
    result = MiCauseOverCommitPopup(0, *(uint64_t *)(Arg1 + 0x4C98), result, 255);
    result = 0;
    goto loc_00286F25;
loc_00287366:
    goto loc_00286FA3;
loc_00287370:
    result = MiReleaseSpinLockShared(v_stack_p30, *(uint64_t *)(Arg1 + 0x4C98), result, 255);
    if (0 != (v_rip + 12261758)) goto loc_0028723C;
    a4 = 0;
    if ((((uint8_t)(local_r14)) & (1)) == 0) goto loc_00287510;
    result = MiIssuePageExtendRequest(0, *(uint64_t *)(Arg1 + 0x4C98), a4 + 10, a4);
    result = 0;
    goto loc_00286F25;
loc_002873AE:
    if (0 != 0) goto loc_002872D8;
    goto loc_002872D8;
loc_002873C2:
    if (0 < (*(uint64_t *)(Arg1 + 0x4C98))) goto loc_0028753B;
    goto loc_00287268;
loc_002873D0:
    if ((*(uint64_t *)(Arg1 + 0x4C98)) != (*(uint64_t *)(Arg1 + 0x41C8))) goto loc_002870B0;
    result = MiFreeExcessSegments(0, *(uint64_t *)(Arg1 + 0x4C98), a4 + 10, a4);
    goto loc_002870B0;
loc_002873ED:
    result = MiReleaseSpinLockShared(Arg1 + 16888, *(uint64_t *)(Arg1 + 0x4C98), a4 + 10, a4);
    goto loc_00286FA3;
loc_00287403:
    result = MiReleaseSpinLockShared(Arg1 + 16888, *(uint64_t *)(Arg1 + 0x4C98), a4 + 10, a4);
    result = 0;
    goto loc_00286F25;
loc_00287416:
    result = MiReleaseSpinLockShared(Arg1 + 16888, *(uint64_t *)(Arg1 + 0x4C98), a4 + 10, a4);
    goto loc_00286FB2;
loc_0028742C:
    a4 = 0;
    result = MiIssuePageExtendRequest(v_stack_p30, (uint32_t)(0x1000ULL), a4 + 2, a4);
    result = 0;
    goto loc_00286F25;
loc_0028744A:
    if ((((uint8_t)(local_r14)) & (1)) == 0) {
        Arg1 = 0;
        result = MiCauseOverCommitPopup(Arg1, (uint32_t)(0x1000ULL), a4 + 2, a4);
    }
    result = MiPulseCommitSignal(Arg1, (uint32_t)(0x1000ULL), a4 + 2, a4);
    goto loc_0028723C;
loc_0028746B:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, (uint32_t)(0x1000ULL), a4 + 2, a4);
loc_00287473:
    if ((*(uint64_t *)(Arg1 + 0x4B40)) < (*(uint64_t *)(Arg1 + 0x41D8))) goto loc_002874CE;
    if ((*(uint64_t *)(Arg1 + 0x4B40)) >= (*(uint64_t *)(Arg1 + 0x41E0))) goto loc_00287557;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x130) + 0x4)) == 1) goto loc_00287571;
loc_002874A7:
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x128) + 0x4)) == 1) {
        result = KeResetEvent(*(uint64_t *)(Arg1 + 0x128), *(uint64_t *)(Arg1 + 0x4B40), *(uint64_t *)(Arg1 + 0x41E0), a4);
    }
    result = MiReleaseSpinLockExclusive(Arg1 + 16888, 17, *(uint64_t *)(Arg1 + 0x41E0), a4);
    goto loc_00287056;
loc_002874CE:
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x128) + 0x4)) == 0) goto loc_002874F6;
loc_002874DB:
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x130) + 0x4)) != 1) goto loc_002874B9;
    result = KeResetEvent(*(uint64_t *)(Arg1 + 0x130), 17, *(uint64_t *)(Arg1 + 0x41E0), a4);
    goto loc_002874B4;
loc_002874F6:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(Arg1 + 0x138), Arg2, Arg3, a4);
    goto loc_002874DB;
loc_00287502:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(Arg1 + 0x138), Arg2, Arg3, a4);
    goto loc_00287473;
loc_00287510:
    result = MiIssuePageExtendRequest(*(uint64_t *)(Arg1 + 0x138), Arg2, 8, a4);
    if ((uint32_t)(result) != 0) goto loc_00287017;
    result = MiCauseOverCommitPopup(Arg1, Arg2, 8, a4);
    result = 0;
    goto loc_00286F25;
loc_00287532:
    if (local_rbp >= 0) goto loc_0028704D;
loc_0028753B:
    if (((uint8_t)(v_stack_p90)) != 2) goto loc_00287502;
    goto loc_0028746B;
loc_0028754F:
    goto loc_0028722A;
loc_00287557:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 16888, Arg2, Arg3, a4);
loc_00287571:
    result = KeResetEvent(Arg1 + 16888, Arg2, Arg3, a4);
    result = KeResetEvent(*(uint64_t *)(Arg1 + 0x138), Arg2, Arg3, a4);
    goto loc_002874A7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00286EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
