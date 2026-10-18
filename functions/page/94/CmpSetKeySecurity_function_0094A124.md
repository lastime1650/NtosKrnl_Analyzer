# CmpSetKeySecurity

- RVA: `0x0094A124`–`0x0094A722` (길이 `1,534` bytes)
- VA: `0x000000014094A124`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090E0C`
- 디코드: `382`개 명령, `1,534/1,534` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0094A1BE` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0094A1D7` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0094A1E0` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x0094A1E5` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x0094A1FF` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0094A229` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x0094A242` → [CmpLockKcbStackTopExclusiveRestShared](../84/CmpLockKcbStackTopExclusiveRestShared_function_00846B04.md) (function, `0x00846B04`)
- `0x0094A24F` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x0094A26D` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x0094A283` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x0094A296` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x0094A327` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0094A333` → [CmLockHiveSecurityExclusive](../84/CmLockHiveSecurityExclusive_function_0084B1A8.md) (function, `0x0084B1A8`)
- `0x0094A36D` → [CmpSetSecurityDescriptorInfo](CmpSetSecurityDescriptorInfo_function_00949688.md) (function, `0x00949688`)
- `0x0094A38E` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x0094A3AA` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0094A3E8` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x0094A412` → [CmpReportNotifyHelper](../8C/CmpReportNotifyHelper_function_008C7230.md) (function, `0x008C7230`)
- `0x0094A449` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0094A458` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0094A462` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0094A475` → [CmpSignalDeferredPosts](../84/CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x0094A47F` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x0094A488` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x0094A491` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0094A49F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0094A4F5` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0094A507` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0094A521` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0094A526` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x0094A539` → [CmpSnapshotTxOwnerArray](../84/CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x0094A554` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0094A566` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0094A580` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0094A58A` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x0094A59F` → [CmpRollbackTransactionArray](CmpRollbackTransactionArray_function_0094B3AC.md) (function, `0x0094B3AC`)
- `0x0094A5D8` → [SeSetSecurityAccessMask](../A2/SeSetSecurityAccessMask_function_00A25E0C.md) (function, `0x00A25E0C`)
- `0x0094A5F1` → [CmpCheckKcbStackAccess](../70/CmpCheckKcbStackAccess_function_00701174.md) (function, `0x00701174`)
- `0x0094A60C` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x0094A623` → [CmpPromoteKey](../84/CmpPromoteKey_function_00844388.md) (function, `0x00844388`)
- `0x0094A637` → [CmpPartialPromoteSubkeys](../7F/CmpPartialPromoteSubkeys_function_007F4070.md) (function, `0x007F4070`)
- `0x0094A656` → [CmpSnapshotTxOwnerArray](../84/CmpSnapshotTxOwnerArray_function_00846808.md) (function, `0x00846808`)
- `0x0094A675` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x0094A6A4` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x0094A6BB` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x0094A6E1` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0094A6F0` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (function, `0x00BC99C8`)
- `0x0094A6FE` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0094A70B` → [CmpRundownUnitOfWork](../87/CmpRundownUnitOfWork_function_0087497C.md) (function, `0x0087497C`)
- `0x0094A718` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) at `0x0087125B`

### Static image references
- `0x0094A13D` → RVA `0x00E0A740` (`.data`; read)
- `0x0094A3ED` → RVA `0x00FD9A90` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x0094A1E0` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A1E5` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A1FF` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A24F` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A283` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A38E` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A458` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0094A462` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A47F` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A488` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A49F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0094A507` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0094A521` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A526` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A566` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0094A580` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A58A` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A6F0` → [CmUnlockHiveSecurity](../../pagecmrc/BC/CmUnlockHiveSecurity_function_00BC99C8.md) (`PAGE` → `PAGECMRC`)
  - `0x0094A718` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0094A66A` → [sub_00B25E36](../B2/Unknown_function_00B25E36.md) (`tail-transfer`)
  - `0x0094A67D` → [sub_00B25E36](../B2/Unknown_function_00B25E36.md) (`tail-transfer`)
  - `0x0094A68F` → [sub_00B25E36 + 0x4F](../B2/Unknown_function_00B25E36.md) (`tail-transfer`)
  - `0x0094A6DB` → [sub_00B25E36 + 0xC3](../B2/Unknown_function_00B25E36.md) (`tail-transfer`)
  - `0x0094A6E7` → [sub_00B25E36 + 0xC8](../B2/Unknown_function_00B25E36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0094A124  40 55                           push rbp
0094A126  53                              push rbx
0094A127  56                              push rsi
0094A128  57                              push rdi
0094A129  41 54                           push r12
0094A12B  41 55                           push r13
0094A12D  41 56                           push r14
0094A12F  41 57                           push r15
0094A131  48 8D 6C 24 D8                  lea rbp, [rsp - 0x28]
0094A136  48 81 EC 28 01 00 00            sub rsp, 0x128
0094A13D  48 8B 05 FC 05 4C 00            mov rax, qword ptr [rip + 0x4c05fc]
0094A144  48 33 C4                        xor rax, rsp
0094A147  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0094A14B  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
0094A152  33 DB                           xor ebx, ebx
0094A154  0F 57 C0                        xorps xmm0, xmm0
0094A157  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0094A15B  0F 57 C9                        xorps xmm1, xmm1
0094A15E  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
0094A162  83 C8 FF                        or eax, 0xffffffff
0094A165  4C 89 45 C0                     mov qword ptr [rbp - 0x40], r8
0094A169  4C 8B F1                        mov r14, rcx
0094A16C  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0094A170  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0094A175  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0094A179  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
0094A17E  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
0094A182  44 8A E3                        mov r12b, bl
0094A185  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0094A189  44 8A FB                        mov r15b, bl
0094A18C  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
0094A190  44 8A EB                        mov r13b, bl
0094A193  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
0094A197  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0094A19B  8B F3                           mov esi, ebx
0094A19D  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0094A1A1  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
0094A1A5  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
0094A1A9  88 5C 24 52                     mov byte ptr [rsp + 0x52], bl
0094A1AD  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
0094A1B1  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
0094A1B5  0F 11 4D 08                     movups xmmword ptr [rbp + 8], xmm1
0094A1B9  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0094A1BE  E8 4D BD F0 FF                  call 0x140855f10
0094A1C3  48 8D 45 98                     lea rax, [rbp - 0x68]
0094A1C7  48 8D 55 98                     lea rdx, [rbp - 0x68]
0094A1CB  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0094A1CF  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0094A1D3  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
0094A1D7  E8 44 16 F2 FF                  call 0x14086b820
0094A1DC  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0094A1E0  E8 FB F6 27 00                  call 0x140bc98e0
0094A1E5  E8 16 F2 27 00                  call 0x140bc9400
0094A1EA  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0094A1EE  84 C0                           test al, al
0094A1F0  0F 84 AA 00 00 00               je 0x14094a2a0
0094A1F6  45 84 E4                        test r12b, r12b
0094A1F9  0F 85 97 00 00 00               jne 0x14094a296
0094A1FF  E8 30 F9 27 00                  call 0x140bc9b34
0094A204  49 8B 7E 08                     mov rdi, qword ptr [r14 + 8]
0094A208  C6 44 24 51 01                  mov byte ptr [rsp + 0x51], 1
0094A20D  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0094A211  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
0094A21B  0F 85 AB 02 00 00               jne 0x14094a4cc
0094A221  48 8B D7                        mov rdx, rdi
0094A224  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A229  E8 62 E1 EF FF                  call 0x140848390
0094A22E  8B D8                           mov ebx, eax
0094A230  85 C0                           test eax, eax
0094A232  0F 88 FD 01 00 00               js 0x14094a435
0094A238  45 84 E4                        test r12b, r12b
0094A23B  75 0D                           jne 0x14094a24a
0094A23D  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A242  E8 BD C8 EF FF                  call 0x140846b04
0094A247  41 B5 01                        mov r13b, 1
0094A24A  33 D2                           xor edx, edx
0094A24C  49 8B CE                        mov rcx, r14
0094A24F  E8 7C F5 27 00                  call 0x140bc97d0
0094A254  8B D8                           mov ebx, eax
0094A256  85 C0                           test eax, eax
0094A258  0F 88 D7 01 00 00               js 0x14094a435
0094A25E  33 DB                           xor ebx, ebx
0094A260  49 39 5E 38                     cmp qword ptr [r14 + 0x38], rbx
0094A264  74 4E                           je 0x14094a2b4
0094A266  48 8D 55 80                     lea rdx, [rbp - 0x80]
0094A26A  49 8B CE                        mov rcx, r14
0094A26D  E8 46 94 F2 FF                  call 0x1408736b8
0094A272  8B D8                           mov ebx, eax
0094A274  85 C0                           test eax, eax
0094A276  0F 88 B9 01 00 00               js 0x14094a435
0094A27C  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0094A280  49 8B CE                        mov rcx, r14
0094A283  E8 48 F5 27 00                  call 0x140bc97d0
0094A288  8B D8                           mov ebx, eax
0094A28A  85 C0                           test eax, eax
0094A28C  0F 88 A3 01 00 00               js 0x14094a435
0094A292  33 DB                           xor ebx, ebx
0094A294  EB 24                           jmp 0x14094a2ba
0094A296  E8 19 57 F0 FF                  call 0x14084f9b4
0094A29B  E9 64 FF FF FF                  jmp 0x14094a204
0094A2A0  44 8A 64 24 50                  mov r12b, byte ptr [rsp + 0x50]
0094A2A5  33 C0                           xor eax, eax
0094A2A7  40 8A F8                        mov dil, al
0094A2AA  BB 89 01 00 C0                  mov ebx, 0xc0000189
0094A2AF  E9 8B 01 00 00                  jmp 0x14094a43f
0094A2B4  49 39 5E 40                     cmp qword ptr [r14 + 0x40], rbx
0094A2B8  75 AC                           jne 0x14094a266
0094A2BA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0094A2C3  44 8A 90 32 02 00 00            mov r10b, byte ptr [rax + 0x232]
0094A2CA  45 84 D2                        test r10b, r10b
0094A2CD  0F 85 E6 01 00 00               jne 0x14094a4b9
0094A2D3  66 39 5F 42                     cmp word ptr [rdi + 0x42], bx
0094A2D7  0F 85 F9 01 00 00               jne 0x14094a4d6
0094A2DD  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
0094A2E1  66 41 39 5E 04                  cmp word ptr [r14 + 4], bx
0094A2E6  0F 85 E1 02 00 00               jne 0x14094a5cd
0094A2EC  66 39 5F 42                     cmp word ptr [rdi + 0x42], bx
0094A2F0  0F 85 11 03 00 00               jne 0x14094a607
0094A2F6  4D 85 E4                        test r12, r12
0094A2F9  0F 85 83 03 00 00               jne 0x14094a682
0094A2FF  48 8D 8F F8 00 00 00            lea rcx, [rdi + 0xf8]
0094A306  39 19                           cmp dword ptr [rcx], ebx
0094A308  0F 85 3F 03 00 00               jne 0x14094a64d
0094A30E  48 8D 8F 08 01 00 00            lea rcx, [rdi + 0x108]
0094A315  39 19                           cmp dword ptr [rcx], ebx
0094A317  0F 85 13 02 00 00               jne 0x14094a530
0094A31D  38 5C 24 52                     cmp byte ptr [rsp + 0x52], bl
0094A321  75 15                           jne 0x14094a338
0094A323  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A327  E8 30 56 F0 FF                  call 0x14084f95c
0094A32C  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A330  41 B7 01                        mov r15b, 1
0094A333  E8 70 0E F0 FF                  call 0x14084b1a8
0094A338  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
0094A33C  48 8D 45 C8                     lea rax, [rbp - 0x38]
0094A340  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
0094A344  48 8B CF                        mov rcx, rdi
0094A347  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
0094A34B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0094A350  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
0094A354  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0094A359  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
0094A35E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0094A363  8B 85 90 00 00 00               mov eax, dword ptr [rbp + 0x90]
0094A369  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0094A36D  E8 16 F3 FF FF                  call 0x140949688
0094A372  45 33 E4                        xor r12d, r12d
0094A375  8B D8                           mov ebx, eax
0094A377  45 8A F7                        mov r14b, r15b
0094A37A  85 C0                           test eax, eax
0094A37C  0F 88 98 00 00 00               js 0x14094a41a
0094A382  41 8B F4                        mov esi, r12d
0094A385  45 84 FF                        test r15b, r15b
0094A388  74 0C                           je 0x14094a396
0094A38A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A38E  E8 35 F6 27 00                  call 0x140bc99c8
0094A393  45 8A F4                        mov r14b, r12b
0094A396  66 44 39 67 42                  cmp word ptr [rdi + 0x42], r12w
0094A39B  0F 85 FE 02 00 00               jne 0x14094a69f
0094A3A1  45 84 FF                        test r15b, r15b
0094A3A4  74 0C                           je 0x14094a3b2
0094A3A6  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A3AA  E8 89 E3 EF FF                  call 0x140848738
0094A3AF  45 8A FC                        mov r15b, r12b
0094A3B2  66 83 7C 24 5A 02               cmp word ptr [rsp + 0x5a], 2
0094A3B8  0F AE E8                        lfence
0094A3BB  0F 8D F7 01 00 00               jge 0x14094a5b8
0094A3C1  48 0F BF 44 24 5A               movsx rax, word ptr [rsp + 0x5a]
0094A3C7  48 8B 5C C4 60                  mov rbx, qword ptr [rsp + rax*8 + 0x60]
0094A3CC  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
0094A3D0  48 8D 45 98                     lea rax, [rbp - 0x68]
0094A3D4  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
0094A3D8  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A3DD  41 B9 0A 00 00 00               mov r9d, 0xa
0094A3E3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094A3E8  E8 43 CE F7 FF                  call 0x1408c7230
0094A3ED  48 8B 15 9C F6 68 00            mov rdx, qword ptr [rip + 0x68f69c]
0094A3F4  48 39 53 20                     cmp qword ptr [rbx + 0x20], rdx
0094A3F8  74 1D                           je 0x14094a417
0094A3FA  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
0094A3FE  48 8D 45 98                     lea rax, [rbp - 0x68]
0094A402  41 B9 0A 00 00 00               mov r9d, 0xa
0094A408  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094A40D  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A412  E8 19 CE F7 FF                  call 0x1408c7230
0094A417  41 8B DC                        mov ebx, r12d
0094A41A  45 84 F6                        test r14b, r14b
0094A41D  0F 85 C9 02 00 00               jne 0x14094a6ec
0094A423  45 84 FF                        test r15b, r15b
0094A426  0F 85 CE 02 00 00               jne 0x14094a6fa
0094A42C  48 85 F6                        test rsi, rsi
0094A42F  0F 85 D3 02 00 00               jne 0x14094a708
0094A435  44 8A 64 24 50                  mov r12b, byte ptr [rsp + 0x50]
0094A43A  40 8A 7C 24 51                  mov dil, byte ptr [rsp + 0x51]
0094A43F  45 84 ED                        test r13b, r13b
0094A442  74 0A                           je 0x14094a44e
0094A444  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A449  E8 12 E0 EF FF                  call 0x140848460
0094A44E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0094A453  48 85 C9                        test rcx, rcx
0094A456  74 05                           je 0x14094a45d
0094A458  E8 23 B9 B2 FF                  call 0x140475d80
0094A45D  40 84 FF                        test dil, dil
0094A460  74 05                           je 0x14094a467
0094A462  E8 1D F6 27 00                  call 0x140bc9a84
0094A467  48 8D 45 98                     lea rax, [rbp - 0x68]
0094A46B  48 39 45 98                     cmp qword ptr [rbp - 0x68], rax
0094A46F  74 09                           je 0x14094a47a
0094A471  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0094A475  E8 36 E0 EF FF                  call 0x1408484b0
0094A47A  45 84 E4                        test r12b, r12b
0094A47D  74 05                           je 0x14094a484
0094A47F  E8 FC F3 27 00                  call 0x140bc9880
0094A484  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0094A488  E8 93 F4 27 00                  call 0x140bc9920
0094A48D  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0094A491  E8 7A 12 F2 FF                  call 0x14086b710
0094A496  8B C3                           mov eax, ebx
0094A498  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0094A49C  48 33 CC                        xor rcx, rsp
0094A49F  E8 9C 21 D6 FF                  call 0x1406ac640
0094A4A4  48 81 C4 28 01 00 00            add rsp, 0x128
0094A4AB  41 5F                           pop r15
0094A4AD  41 5E                           pop r14
0094A4AF  41 5D                           pop r13
0094A4B1  41 5C                           pop r12
0094A4B3  5F                              pop rdi
0094A4B4  5E                              pop rsi
0094A4B5  5B                              pop rbx
0094A4B6  5D                              pop rbp
0094A4B7  C3                              ret
0094A4B8  CC                              int3
0094A4B9  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0094A4BD  8B 88 10 10 00 00               mov ecx, dword ptr [rax + 0x1010]
0094A4C3  F6 C1 20                        test cl, 0x20
0094A4C6  0F 84 07 FE FF FF               je 0x14094a2d3
0094A4CC  BB 22 00 00 C0                  mov ebx, 0xc0000022
0094A4D1  E9 5F FF FF FF                  jmp 0x14094a435
0094A4D6  38 5F 41                        cmp byte ptr [rdi + 0x41], bl
0094A4D9  0F 85 FE FD FF FF               jne 0x14094a2dd
0094A4DF  45 84 E4                        test r12b, r12b
0094A4E2  0F 85 F5 FD FF FF               jne 0x14094a2dd
0094A4E8  41 B4 01                        mov r12b, 1
0094A4EB  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A4F0  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
0094A4F5  E8 66 DF EF FF                  call 0x140848460
0094A4FA  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0094A4FF  44 8A EB                        mov r13b, bl
0094A502  48 85 C9                        test rcx, rcx
0094A505  74 05                           je 0x14094a50c
0094A507  E8 74 B8 B2 FF                  call 0x140475d80
0094A50C  0F 57 C0                        xorps xmm0, xmm0
0094A50F  83 C8 FF                        or eax, 0xffffffff
0094A512  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0094A517  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
0094A51C  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0094A521  E8 5E F5 27 00                  call 0x140bc9a84
0094A526  E8 55 F3 27 00                  call 0x140bc9880
0094A52B  E9 B5 FC FF FF                  jmp 0x14094a1e5
0094A530  4C 8D 45 88                     lea r8, [rbp - 0x78]
0094A534  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
0094A539  E8 CA C2 EF FF                  call 0x140846808
0094A53E  33 FF                           xor edi, edi
0094A540  8B D8                           mov ebx, eax
0094A542  85 C0                           test eax, eax
0094A544  0F 88 EB FE FF FF               js 0x14094a435
0094A54A  45 84 ED                        test r13b, r13b
0094A54D  74 0D                           je 0x14094a55c
0094A54F  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A554  E8 07 DF EF FF                  call 0x140848460
0094A559  44 8A EF                        mov r13b, dil
0094A55C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0094A561  48 85 C9                        test rcx, rcx
0094A564  74 05                           je 0x14094a56b
0094A566  E8 15 B8 B2 FF                  call 0x140475d80
0094A56B  0F 57 C0                        xorps xmm0, xmm0
0094A56E  83 C8 FF                        or eax, 0xffffffff
0094A571  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0094A576  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
0094A57B  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0094A580  E8 FF F4 27 00                  call 0x140bc9a84
0094A585  40 88 7C 24 51                  mov byte ptr [rsp + 0x51], dil
0094A58A  E8 F1 F2 27 00                  call 0x140bc9880
0094A58F  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0094A593  4C 8D 4C 24 7C                  lea r9, [rsp + 0x7c]
0094A598  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
0094A59C  44 8A E7                        mov r12b, dil
0094A59F  E8 08 0E 00 00                  call 0x14094b3ac
0094A5A4  8B D8                           mov ebx, eax
0094A5A6  85 C0                           test eax, eax
0094A5A8  0F 88 8C FE FF FF               js 0x14094a43a
0094A5AE  44 8A 64 24 52                  mov r12b, byte ptr [rsp + 0x52]
0094A5B3  E9 2D FC FF FF                  jmp 0x14094a1e5
0094A5B8  48 0F BF 4C 24 5A               movsx rcx, word ptr [rsp + 0x5a]
0094A5BE  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0094A5C3  48 8B 5C C8 F0                  mov rbx, qword ptr [rax + rcx*8 - 0x10]
0094A5C8  E9 FF FD FF FF                  jmp 0x14094a3cc
0094A5CD  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0094A5D1  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0094A5D6  8B 08                           mov ecx, dword ptr [rax]
0094A5D8  E8 2F B8 0D 00                  call 0x140a25e0c
0094A5DD  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
0094A5E2  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A5E7  45 8A C2                        mov r8b, r10b
0094A5EA  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0094A5EE  49 8B D4                        mov rdx, r12
0094A5F1  E8 7E 6B DB FF                  call 0x140701174
0094A5F6  8B D8                           mov ebx, eax
0094A5F8  85 C0                           test eax, eax
0094A5FA  0F 88 35 FE FF FF               js 0x14094a435
0094A600  33 DB                           xor ebx, ebx
0094A602  E9 E5 FC FF FF                  jmp 0x14094a2ec
0094A607  33 D2                           xor edx, edx
0094A609  48 8B CF                        mov rcx, rdi
0094A60C  E8 0F E8 EF FF                  call 0x140848e20
0094A611  85 C0                           test eax, eax
0094A613  0F 85 DD FC FF FF               jne 0x14094a2f6
0094A619  45 33 C0                        xor r8d, r8d
0094A61C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A621  B2 01                           mov dl, 1
0094A623  E8 60 9D EF FF                  call 0x140844388
0094A628  8B D8                           mov ebx, eax
0094A62A  85 C0                           test eax, eax
0094A62C  0F 88 03 FE FF FF               js 0x14094a435
0094A632  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A637  E8 34 9A EA FF                  call 0x1407f4070
0094A63C  8B D8                           mov ebx, eax
0094A63E  85 C0                           test eax, eax
0094A640  0F 88 EF FD FF FF               js 0x14094a435
0094A646  33 DB                           xor ebx, ebx
0094A648  E9 A9 FC FF FF                  jmp 0x14094a2f6
0094A64D  4C 8D 45 88                     lea r8, [rbp - 0x78]
0094A651  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
0094A656  E8 AD C1 EF FF                  call 0x140846808
0094A65B  33 FF                           xor edi, edi
0094A65D  8B D8                           mov ebx, eax
0094A65F  85 C0                           test eax, eax
0094A661  0F 88 CE FD FF FF               js 0x14094a435
0094A667  45 84 ED                        test r13b, r13b
0094A66A  0F 84 C6 B7 1D 00               je 0x140b25e36
0094A670  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0094A675  E8 E6 DD EF FF                  call 0x140848460
0094A67A  44 8A EF                        mov r13b, dil
0094A67D  E9 B4 B7 1D 00                  jmp 0x140b25e36
0094A682  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0094A686  8B 88 A0 00 00 00               mov ecx, dword ptr [rax + 0xa0]
0094A68C  F6 C1 02                        test cl, 2
0094A68F  0F 84 F0 B7 1D 00               je 0x140b25e85
0094A695  BB 01 00 19 C0                  mov ebx, 0xc0190001
0094A69A  E9 96 FD FF FF                  jmp 0x14094a435
0094A69F  33 D2                           xor edx, edx
0094A6A1  48 8B CF                        mov rcx, rdi
0094A6A4  E8 77 E7 EF FF                  call 0x140848e20
0094A6A9  85 C0                           test eax, eax
0094A6AB  0F 85 F0 FC FF FF               jne 0x14094a3a1
0094A6B1  45 8A C7                        mov r8b, r15b
0094A6B4  48 8D 55 90                     lea rdx, [rbp - 0x70]
0094A6B8  48 8B CF                        mov rcx, rdi
0094A6BB  E8 C0 BD F0 FF                  call 0x140856480
0094A6C0  48 8D 55 90                     lea rdx, [rbp - 0x70]
0094A6C4  8A 48 0D                        mov cl, byte ptr [rax + 0xd]
0094A6C7  80 E1 FE                        and cl, 0xfe
0094A6CA  80 C9 02                        or cl, 2
0094A6CD  88 48 0D                        mov byte ptr [rax + 0xd], cl
0094A6D0  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A6D4  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0094A6DB  0F 84 18 B8 1D 00               je 0x140b25ef9
0094A6E1  E8 3A 25 F1 FF                  call 0x14085cc20
0094A6E6  90                              nop
0094A6E7  E9 12 B8 1D 00                  jmp 0x140b25efe
0094A6EC  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A6F0  E8 D3 F2 27 00                  call 0x140bc99c8
0094A6F5  E9 29 FD FF FF                  jmp 0x14094a423
0094A6FA  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0094A6FE  E8 35 E0 EF FF                  call 0x140848738
0094A703  E9 24 FD FF FF                  jmp 0x14094a42c
0094A708  48 8B CE                        mov rcx, rsi
0094A70B  E8 6C A2 F2 FF                  call 0x14087497c
0094A710  BA 43 4D 55 77                  mov edx, 0x77554d43
0094A715  48 8B CE                        mov rcx, rsi
0094A718  E8 53 81 23 00                  call 0x140b82870
0094A71D  E9 13 FD FF FF                  jmp 0x14094a435
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSetKeySecurity(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int16 v_stack_m10E;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int8 v_stack_m116;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned __int64 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int16 v_stack_p5A;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p7C;

    v_rsp = (v_rsp) - (296);
    result = (*(unsigned __int64 *)(v_rip + 4982268)) ^ (v_rsp);
    v_stack_m50 = result;
    v_rbx = 0;
    v_stack_mB8 = a6;
    v_stack_mB0 = a4;
    result = (unsigned int)((a6) | (0xFFFFFFFFULL));
    v_stack_mA8 = a3;
    v_stack_mC0 = a2;
    v_stack_m110 = v_xmm0;
    v_stack_m10E = (unsigned __int16)(result);
    v_stack_m114 = 0;
    v_stack_mE0 = 0;
    v_stack_mD8 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_m80 = v_xmm1;
    v_stack_m116 = 0;
    v_stack_m70 = v_xmm1;
    v_stack_mEC = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m100 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_mD8, a2, a3, a4);
    v_stack_mD0 = v_stack_mD0;
    v_stack_mC8 = v_stack_mD0;
    result = SeCaptureSubjectContext(v_stack_mA0, v_stack_mD0, a3, a4);
    result = CmpAttachToRegistryProcess(v_stack_m80, v_stack_mD0, a3, a4);
loc_0094A1E5:
    result = CmpAcquireShutdownRundown(v_stack_m80, v_stack_mD0, a3, a4);
    v_stack_m118 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_0094A2A0;
    if (0 != 0) goto loc_0094A296;
    result = CmpLockRegistry(v_stack_m80, v_stack_mD0, a3, a4);
loc_0094A204:
    v_stack_m117 = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_0094A4CC;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m110, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if (sign_flag) goto loc_0094A435;
    v_r13 = 0;
    if (0 == 0) {
        a1 = v_stack_m110;
        result = CmpLockKcbStackTopExclusiveRestShared(a1, *(unsigned __int64 *)(a1 + 8), a3, a4);
        v_r13 = 1;
    }
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(a1, a2, a3, a4);
    if (sign_flag) goto loc_0094A435;
    v_rbx = 0;
    if ((*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_0094A2B4;
loc_0094A266:
    result = CmpTransSearchAddTransFromKeyBody(a1, v_stack_mE8, a3, a4);
    if (sign_flag) goto loc_0094A435;
    result = CmpPerformKeyBodyDeletionCheck(a1, v_stack_mE8, a3, a4);
    if (sign_flag) goto loc_0094A435;
    v_rbx = 0;
    goto loc_0094A2BA;
loc_0094A296:
    result = CmpLockRegistryExclusive(a1, v_stack_mE8, a3, a4);
    goto loc_0094A204;
loc_0094A2A0:
    result = 0;
    goto loc_0094A43F;
loc_0094A2B4:
    if ((*(unsigned __int64 *)(a1 + 64)) != ((unsigned int)(0xC0000189ULL))) goto loc_0094A266;
loc_0094A2BA:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0094A4B9;
loc_0094A2D3:
    if ((*(unsigned __int16 *)(0 + 66)) != ((unsigned __int16)((unsigned int)(0xC0000189ULL)))) goto loc_0094A4D6;
loc_0094A2DD:
    if ((*(unsigned __int16 *)(a1 + 4)) != ((unsigned __int16)((unsigned int)(0xC0000189ULL)))) goto loc_0094A5CD;
loc_0094A2EC:
    if ((*(unsigned __int16 *)(0 + 66)) != ((unsigned __int16)((unsigned int)(0xC0000189ULL)))) goto loc_0094A607;
loc_0094A2F6:
    if (v_stack_mE8 != 0) goto loc_0094A682;
    if ((*(unsigned int *)(0 + 248)) != ((unsigned int)((unsigned int)(0xC0000189ULL)))) goto loc_0094A64D;
    if ((*(unsigned int *)(0 + 264)) != ((unsigned int)((unsigned int)(0xC0000189ULL)))) goto loc_0094A530;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r15 = 0;
    if (v_stack_m116 == ((unsigned __int8)((unsigned int)(0xC0000189ULL)))) {
        a1 = *(unsigned __int64 *)(0 + 32);
        result = HvLockHiveFlusherShared(a1, v_stack_mE8, a3, a4);
        a1 = *(unsigned __int64 *)(0 + 32);
        v_r15 = 1;
        result = CmLockHiveSecurityExclusive(a1, v_stack_mE8, a3, a4);
    }
    v_stack_m128 = v_stack_mA0;
    v_stack_m130 = 0;
    v_stack_m138 = v_stack_mE8;
    v_stack_m140 = v_stack_mB8;
    v_stack_m148 = (unsigned int)((unsigned int)(a5));
    result = CmpSetSecurityDescriptorInfo(0, v_stack_mC0, v_stack_mA8, v_stack_mB0);
    v_r12 = 0;
    if (sign_flag) goto loc_0094A41A;
    v_r14 = (unsigned __int8)(v_r15);
    if ((unsigned __int8)(v_r15) != 0) {
        a1 = *(unsigned __int64 *)(0 + 32);
        result = CmUnlockHiveSecurity(a1, v_stack_mC0, v_stack_mA8, v_stack_mB0);
        v_r14 = 0;
    }
    if ((*(unsigned __int16 *)(0 + 66)) != 0) goto loc_0094A69F;
loc_0094A3A1:
    if ((unsigned __int8)(v_r15) != 0) {
        a1 = *(unsigned __int64 *)(0 + 32);
        result = HvUnlockHiveFlusherShared(a1, v_stack_mC0, v_stack_mA8, v_stack_mB0);
        v_r15 = 0;
    }
    if (v_stack_m10E >= 2) goto loc_0094A5B8;
loc_0094A3CC:
    v_stack_m148 = v_stack_mD0;
    result = CmpReportNotifyHelper(v_stack_m110, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m10E) * 8 + 96) + 32), v_stack_mE8, 10);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)(v_stack_m10E) * 8 + 96) + 32)) != (*(unsigned __int64 *)(v_rip + 6878876))) {
        a3 = v_stack_mE8;
        result = v_stack_mD0;
        a4 = 10;
        v_stack_m148 = result;
        a1 = v_stack_m110;
        result = CmpReportNotifyHelper(a1, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
loc_0094A41A:
    if ((unsigned __int8)(v_r14) != 0) goto loc_0094A6EC;
loc_0094A423:
    if ((unsigned __int8)(v_r15) != 0) goto loc_0094A6FA;
loc_0094A42C:
    if (0 != 0) goto loc_0094A708;
loc_0094A435:
loc_0094A43A:
loc_0094A43F:
    if ((unsigned __int8)(v_r13) != 0) {
        a1 = v_stack_m110;
        result = CmpUnlockKcbStack(a1, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    if (v_stack_mF8 != 0) {
        result = CmSiFreeMemory(v_stack_mF8, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    if ((unsigned __int8)(v_stack_m117) != 0) {
        result = CmpUnlockRegistry(v_stack_mF8, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    result = v_stack_mD0;
    if (v_stack_mD0 != v_stack_mD0) {
        a1 = v_stack_mD0;
        result = CmpSignalDeferredPosts(a1, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    if ((unsigned __int8)(v_stack_m118) != 0) {
        result = CmpReleaseShutdownRundown(a1, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m80, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    result = SeReleaseSubjectContext(v_stack_mA0, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    v_rsp = (v_rsp) + (296);
    return result;
loc_0094A4B9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m117 + 32) + 4112)))) & (32)) == 0) goto loc_0094A2D3;
loc_0094A4CC:
    goto loc_0094A435;
loc_0094A4D6:
    if ((*(unsigned __int8 *)(v_stack_m117 + 65)) != ((unsigned __int8)((unsigned int)(0xC0000022ULL)))) goto loc_0094A2DD;
    if ((unsigned __int8)(v_stack_m118) != 0) goto loc_0094A2DD;
    v_stack_p52 = 1;
    result = CmpUnlockKcbStack(v_stack_p58, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    if (v_stack_p70 != 0) {
        result = CmSiFreeMemory(v_stack_p70, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    }
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_p58 = v_xmm0;
    v_stack_p5A = (unsigned __int16)(result);
    v_stack_p68 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_p70, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    result = CmpReleaseShutdownRundown(v_stack_p70, *(unsigned __int64 *)(v_rip + 6878876), a3, a4);
    goto loc_0094A1E5;
loc_0094A530:
    result = CmpSnapshotTxOwnerArray(v_stack_p70, v_stack_p54, v_stack_mE0, a4);
    v_rdi = 0;
    if (sign_flag) goto loc_0094A435;
    v_r13 = (unsigned __int8)((unsigned int)(0xC0000022ULL));
    if ((unsigned __int8)((unsigned __int8)((unsigned int)(0xC0000022ULL))) != 0) {
        a1 = v_stack_p58;
        result = CmpUnlockKcbStack(a1, v_stack_p54, v_stack_mE0, a4);
        v_r13 = 0;
    }
    if (v_stack_p70 != 0) {
        result = CmSiFreeMemory(v_stack_p70, v_stack_p54, v_stack_mE0, a4);
    }
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_p58 = v_xmm0;
    v_stack_p5A = (unsigned __int16)(result);
    v_stack_p68 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_p70, v_stack_p54, v_stack_mE0, a4);
    v_stack_p51 = 0;
    result = CmpReleaseShutdownRundown(v_stack_p70, v_stack_p54, v_stack_mE0, a4);
    result = CmpRollbackTransactionArray((unsigned int)(v_stack_p54), v_stack_mE0, v_stack_mE0, v_stack_p7C);
    if (sign_flag) goto loc_0094A43A;
    goto loc_0094A1E5;
loc_0094A5B8:
    goto loc_0094A3CC;
loc_0094A5CD:
    result = SeSetSecurityAccessMask((unsigned int)(*(unsigned int *)(v_stack_mC0)), v_stack_p78, v_stack_mE0, v_stack_p7C);
    v_stack_p20 = (unsigned __int8)(*(unsigned __int64 *)(v_stack_p70 + (__int16)(v_stack_p5A) * 8 - 16));
    result = CmpCheckKcbStackAccess(v_stack_p58, v_stack_p52, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    v_rbx = 0;
    goto loc_0094A2EC;
loc_0094A607:
    a2 = 0;
    result = CmpGetEffectiveKcbSemantics(0, a2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(v_stack_p78));
    if ((unsigned int)(result) != 0) goto loc_0094A2F6;
    a3 = 0;
    result = CmpPromoteKey(v_stack_p58, 1, a3, (unsigned int)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    result = CmpPartialPromoteSubkeys(v_stack_p58, 1, a3, (unsigned int)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    v_rbx = 0;
    goto loc_0094A2F6;
loc_0094A64D:
    result = CmpSnapshotTxOwnerArray(v_stack_p58, v_stack_p54, v_stack_mE0, (unsigned int)(v_stack_p78));
    v_rdi = 0;
    if (sign_flag) goto loc_0094A435;
    result = CmpUnlockKcbStack(v_stack_p58, v_stack_p54, v_stack_mE0, (unsigned int)(v_stack_p78));
loc_0094A682:
    goto loc_0094A435;
loc_0094A69F:
    a2 = 0;
    result = CmpGetEffectiveKcbSemantics(0, a2, v_stack_mE0, (unsigned int)(v_stack_p78));
    if ((unsigned int)(result) != 0) goto loc_0094A3A1;
    result = CmpGetKeyNodeForKcb(0, v_stack_mD8, (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 13)) & (254));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(result + 13) = (unsigned __int8)(a1);
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rdi + 32), v_stack_mD8, (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
loc_0094A6EC:
    result = CmUnlockHiveSecurity(*(unsigned __int64 *)(v_rdi + 32), v_stack_mD8, (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
    goto loc_0094A423;
loc_0094A6FA:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(v_rdi + 32), v_stack_mD8, (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
    goto loc_0094A42C;
loc_0094A708:
    result = CmpRundownUnitOfWork(0, v_stack_mD8, (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
    result = ExFreePoolWithTag(0, (unsigned int)(0x77554D43ULL), (unsigned __int8)(v_r15), (unsigned int)(v_stack_p78));
    goto loc_0094A435;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSetKeySecurity(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint16_t v_stack_m10E;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint8_t v_stack_m116;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p20;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint64_t v_stack_p54;
    uint64_t v_stack_p58;
    uint16_t v_stack_p5A;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p7C;

    local_rsp = (local_rsp) - (296);
    result = (*(uint64_t *)(v_rip + 0x4C05FC)) ^ (local_rsp);
    v_stack_m50 = result;
    local_rbx = 0;
    v_stack_mB8 = Arg6;
    v_stack_mB0 = Arg4;
    result = (uint32_t)((Arg6) | (0xFFFFFFFFULL));
    v_stack_mA8 = Arg3;
    v_stack_mC0 = Arg2;
    v_stack_m110 = v_xmm0;
    v_stack_m10E = (uint16_t)(result);
    v_stack_m114 = 0;
    v_stack_mE0 = 0;
    v_stack_mD8 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_mE8 = 0;
    v_stack_m80 = v_xmm1;
    v_stack_m116 = 0;
    v_stack_m70 = v_xmm1;
    v_stack_mEC = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m100 = v_xmm0;
    result = HvpGetCellContextInitialize(v_stack_mD8, Arg2, Arg3, Arg4);
    v_stack_mD0 = v_stack_mD0;
    v_stack_mC8 = v_stack_mD0;
    result = SeCaptureSubjectContext(v_stack_mA0, v_stack_mD0, Arg3, Arg4);
    result = CmpAttachToRegistryProcess(v_stack_m80, v_stack_mD0, Arg3, Arg4);
loc_0094A1E5:
    result = CmpAcquireShutdownRundown(v_stack_m80, v_stack_mD0, Arg3, Arg4);
    v_stack_m118 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_0094A2A0;
    if (0 != 0) goto loc_0094A296;
    result = CmpLockRegistry(v_stack_m80, v_stack_mD0, Arg3, Arg4);
loc_0094A204:
    v_stack_m117 = 1;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_0094A4CC;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m110, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
    if (sign_flag) goto loc_0094A435;
    local_r13 = 0;
    if (0 == 0) {
        Arg1 = v_stack_m110;
        result = CmpLockKcbStackTopExclusiveRestShared(Arg1, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
        local_r13 = 1;
    }
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0094A435;
    local_rbx = 0;
    if ((*(uint64_t *)(arg1 + 0x38)) == 0) goto loc_0094A2B4;
loc_0094A266:
    result = CmpTransSearchAddTransFromKeyBody(Arg1, v_stack_mE8, Arg3, Arg4);
    if (sign_flag) goto loc_0094A435;
    result = CmpPerformKeyBodyDeletionCheck(Arg1, v_stack_mE8, Arg3, Arg4);
    if (sign_flag) goto loc_0094A435;
    local_rbx = 0;
    goto loc_0094A2BA;
loc_0094A296:
    result = CmpLockRegistryExclusive(Arg1, v_stack_mE8, Arg3, Arg4);
    goto loc_0094A204;
loc_0094A2A0:
    result = 0;
    goto loc_0094A43F;
loc_0094A2B4:
    if ((*(uint64_t *)(arg1 + 0x40)) != ((uint32_t)(0xC0000189ULL))) goto loc_0094A266;
loc_0094A2BA:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0094A4B9;
loc_0094A2D3:
    if ((*(uint16_t *)(0 + 0x42)) != ((uint16_t)((uint32_t)(0xC0000189ULL)))) goto loc_0094A4D6;
loc_0094A2DD:
    if ((*(uint16_t *)(arg1 + 0x4)) != ((uint16_t)((uint32_t)(0xC0000189ULL)))) goto loc_0094A5CD;
loc_0094A2EC:
    if ((*(uint16_t *)(0 + 0x42)) != ((uint16_t)((uint32_t)(0xC0000189ULL)))) goto loc_0094A607;
loc_0094A2F6:
    if (v_stack_mE8 != 0) goto loc_0094A682;
    if ((*(uint32_t *)(0 + 0xF8)) != ((uint32_t)((uint32_t)(0xC0000189ULL)))) goto loc_0094A64D;
    if ((*(uint32_t *)(0 + 0x108)) != ((uint32_t)((uint32_t)(0xC0000189ULL)))) goto loc_0094A530;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r15 = 0;
    if (v_stack_m116 == ((uint8_t)((uint32_t)(0xC0000189ULL)))) {
        Arg1 = *(uint64_t *)(0 + 0x20);
        result = HvLockHiveFlusherShared(Arg1, v_stack_mE8, Arg3, Arg4);
        Arg1 = *(uint64_t *)(0 + 0x20);
        local_r15 = 1;
        result = CmLockHiveSecurityExclusive(Arg1, v_stack_mE8, Arg3, Arg4);
    }
    v_stack_m128 = v_stack_mA0;
    v_stack_m130 = 0;
    v_stack_m138 = v_stack_mE8;
    v_stack_m140 = v_stack_mB8;
    v_stack_m148 = (uint32_t)((uint32_t)(Arg5));
    result = CmpSetSecurityDescriptorInfo(0, v_stack_mC0, v_stack_mA8, v_stack_mB0);
    local_r12 = 0;
    if (sign_flag) goto loc_0094A41A;
    local_r14 = (uint8_t)(local_r15);
    if ((uint8_t)(local_r15) != 0) {
        Arg1 = *(uint64_t *)(0 + 0x20);
        result = CmUnlockHiveSecurity(Arg1, v_stack_mC0, v_stack_mA8, v_stack_mB0);
        local_r14 = 0;
    }
    if ((*(uint16_t *)(0 + 0x42)) != 0) goto loc_0094A69F;
loc_0094A3A1:
    if ((uint8_t)(local_r15) != 0) {
        Arg1 = *(uint64_t *)(0 + 0x20);
        result = HvUnlockHiveFlusherShared(Arg1, v_stack_mC0, v_stack_mA8, v_stack_mB0);
        local_r15 = 0;
    }
    if (v_stack_m10E >= 2) goto loc_0094A5B8;
loc_0094A3CC:
    v_stack_m148 = v_stack_mD0;
    result = CmpReportNotifyHelper(v_stack_m110, *(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m10E) * 8 + 0x60) + 0x20), v_stack_mE8, 10);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)(v_stack_m10E) * 8 + 0x60) + 0x20)) != (*(uint64_t *)(v_rip + 0x68F69C))) {
        Arg3 = v_stack_mE8;
        result = v_stack_mD0;
        Arg4 = 10;
        v_stack_m148 = result;
        Arg1 = v_stack_m110;
        result = CmpReportNotifyHelper(Arg1, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
loc_0094A41A:
    if ((uint8_t)(local_r14) != 0) goto loc_0094A6EC;
loc_0094A423:
    if ((uint8_t)(local_r15) != 0) goto loc_0094A6FA;
loc_0094A42C:
    if (0 != 0) goto loc_0094A708;
loc_0094A435:
loc_0094A43A:
loc_0094A43F:
    if ((uint8_t)(local_r13) != 0) {
        Arg1 = v_stack_m110;
        result = CmpUnlockKcbStack(Arg1, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    if (v_stack_mF8 != 0) {
        result = CmSiFreeMemory(v_stack_mF8, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    if ((uint8_t)(v_stack_m117) != 0) {
        result = CmpUnlockRegistry(v_stack_mF8, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    result = v_stack_mD0;
    if (v_stack_mD0 != v_stack_mD0) {
        Arg1 = v_stack_mD0;
        result = CmpSignalDeferredPosts(Arg1, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    if ((uint8_t)(v_stack_m118) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    result = CmpDetachFromRegistryProcess(v_stack_m80, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    result = SeReleaseSubjectContext(v_stack_mA0, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    local_rsp = (local_rsp) + (296);
    return result;
loc_0094A4B9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m117 + 0x20) + 0x1010)))) & (32)) == 0) goto loc_0094A2D3;
loc_0094A4CC:
    goto loc_0094A435;
loc_0094A4D6:
    if ((*(uint8_t *)(v_stack_m117 + 0x41)) != ((uint8_t)((uint32_t)(0xC0000022ULL)))) goto loc_0094A2DD;
    if ((uint8_t)(v_stack_m118) != 0) goto loc_0094A2DD;
    v_stack_p52 = 1;
    result = CmpUnlockKcbStack(v_stack_p58, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    if (v_stack_p70 != 0) {
        result = CmSiFreeMemory(v_stack_p70, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    }
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_p58 = v_xmm0;
    v_stack_p5A = (uint16_t)(result);
    v_stack_p68 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_p70, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    result = CmpReleaseShutdownRundown(v_stack_p70, *(uint64_t *)(v_rip + 0x68F69C), Arg3, Arg4);
    goto loc_0094A1E5;
loc_0094A530:
    result = CmpSnapshotTxOwnerArray(v_stack_p70, v_stack_p54, v_stack_mE0, Arg4);
    local_rdi = 0;
    if (sign_flag) goto loc_0094A435;
    local_r13 = (uint8_t)((uint32_t)(0xC0000022ULL));
    if ((uint8_t)((uint8_t)((uint32_t)(0xC0000022ULL))) != 0) {
        Arg1 = v_stack_p58;
        result = CmpUnlockKcbStack(Arg1, v_stack_p54, v_stack_mE0, Arg4);
        local_r13 = 0;
    }
    if (v_stack_p70 != 0) {
        result = CmSiFreeMemory(v_stack_p70, v_stack_p54, v_stack_mE0, Arg4);
    }
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_p58 = v_xmm0;
    v_stack_p5A = (uint16_t)(result);
    v_stack_p68 = v_xmm0;
    result = CmpUnlockRegistry(v_stack_p70, v_stack_p54, v_stack_mE0, Arg4);
    v_stack_p51 = 0;
    result = CmpReleaseShutdownRundown(v_stack_p70, v_stack_p54, v_stack_mE0, Arg4);
    result = CmpRollbackTransactionArray((uint32_t)(v_stack_p54), v_stack_mE0, v_stack_mE0, v_stack_p7C);
    if (sign_flag) goto loc_0094A43A;
    goto loc_0094A1E5;
loc_0094A5B8:
    goto loc_0094A3CC;
loc_0094A5CD:
    result = SeSetSecurityAccessMask((uint32_t)(*(uint32_t *)(v_stack_mC0)), v_stack_p78, v_stack_mE0, v_stack_p7C);
    v_stack_p20 = (uint8_t)(*(uint64_t *)(v_stack_p70 + (int16_t)(v_stack_p5A) * 8 - 0x10));
    result = CmpCheckKcbStackAccess(v_stack_p58, v_stack_p52, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    local_rbx = 0;
    goto loc_0094A2EC;
loc_0094A607:
    Arg2 = 0;
    result = CmpGetEffectiveKcbSemantics(0, Arg2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(v_stack_p78));
    if ((uint32_t)(result) != 0) goto loc_0094A2F6;
    Arg3 = 0;
    result = CmpPromoteKey(v_stack_p58, 1, Arg3, (uint32_t)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    result = CmpPartialPromoteSubkeys(v_stack_p58, 1, Arg3, (uint32_t)(v_stack_p78));
    if (sign_flag) goto loc_0094A435;
    local_rbx = 0;
    goto loc_0094A2F6;
loc_0094A64D:
    result = CmpSnapshotTxOwnerArray(v_stack_p58, v_stack_p54, v_stack_mE0, (uint32_t)(v_stack_p78));
    local_rdi = 0;
    if (sign_flag) goto loc_0094A435;
    result = CmpUnlockKcbStack(v_stack_p58, v_stack_p54, v_stack_mE0, (uint32_t)(v_stack_p78));
loc_0094A682:
    goto loc_0094A435;
loc_0094A69F:
    Arg2 = 0;
    result = CmpGetEffectiveKcbSemantics(0, Arg2, v_stack_mE0, (uint32_t)(v_stack_p78));
    if ((uint32_t)(result) != 0) goto loc_0094A3A1;
    result = CmpGetKeyNodeForKcb(0, v_stack_mD8, (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0xD)) & (254));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(result + 0xD) = (uint8_t)(Arg1);
    result = HvpReleaseCellFlat(*(uint64_t *)(local_rdi + 0x20), v_stack_mD8, (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
loc_0094A6EC:
    result = CmUnlockHiveSecurity(*(uint64_t *)(local_rdi + 0x20), v_stack_mD8, (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
    goto loc_0094A423;
loc_0094A6FA:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(local_rdi + 0x20), v_stack_mD8, (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
    goto loc_0094A42C;
loc_0094A708:
    result = CmpRundownUnitOfWork(0, v_stack_mD8, (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
    result = ExFreePoolWithTag(0, (uint32_t)(0x77554D43ULL), (uint8_t)(local_r15), (uint32_t)(v_stack_p78));
    goto loc_0094A435;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094A124&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
