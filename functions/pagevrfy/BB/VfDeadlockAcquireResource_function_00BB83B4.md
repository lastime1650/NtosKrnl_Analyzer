# VfDeadlockAcquireResource

- RVA: `0x00BB83B4`–`0x00BB8A81` (길이 `1,741` bytes)
- VA: `0x0000000140BB83B4`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD158`
- 디코드: `456`개 명령, `1,741/1,741` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00BB8400` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00BB844F` → [ViDeadlockCanProceed](ViDeadlockCanProceed_function_00BB7B84.md) (function, `0x00BB7B84`)
- `0x00BB845C` → [ViIsThreadInsidePagingCodePaths](../BA/ViIsThreadInsidePagingCodePaths_function_00BAA2D4.md) (function, `0x00BAA2D4`)
- `0x00BB84B1` → [ViDeadlockAllocate](../BA/ViDeadlockAllocate_function_00BA8B78.md) (function, `0x00BA8B78`)
- `0x00BB84C0` → [ViDeadlockAllocate](../BA/ViDeadlockAllocate_function_00BA8B78.md) (function, `0x00BA8B78`)
- `0x00BB84CE` → [ViDeadlockAllocate](../BA/ViDeadlockAllocate_function_00BA8B78.md) (function, `0x00BA8B78`)
- `0x00BB84E6` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x00BB8509` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (function, `0x006162B0`)
- `0x00BB8517` → [ViDeadlockDetectionLock](../BA/ViDeadlockDetectionLock_function_00BA91C4.md) (function, `0x00BA91C4`)
- `0x00BB8552` → [ViDeadlockSearchThread](../BA/ViDeadlockSearchThread_function_00BAA1AC.md) (function, `0x00BAA1AC`)
- `0x00BB8567` → [ViDeadlockAddThread](../BA/ViDeadlockAddThread_function_00BA8AB8.md) (function, `0x00BA8AB8`)
- `0x00BB85AC` → [ViDeadlockSearchResource](../BA/ViDeadlockSearchResource_function_00BAA0D0.md) (function, `0x00BAA0D0`)
- `0x00BB85DF` → [ViDeadlockAddResource](../BA/ViDeadlockAddResource_function_00BA8870.md) (function, `0x00BA8870`)
- `0x00BB85F7` → [ViDeadlockSearchResource](../BA/ViDeadlockSearchResource_function_00BAA0D0.md) (function, `0x00BAA0D0`)
- `0x00BB864F` → [ViDeadlockRemoveThread](../BA/ViDeadlockRemoveThread_function_00BA9F8C.md) (function, `0x00BA9F8C`)
- `0x00BB8683` → [ViDeadlockPreprocessOptions](../BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) (function, `0x00BA9BB4`)
- `0x00BB86A0` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (function, `0x00614444`)
- `0x00BB871A` → [ViDeadlockPreprocessOptions](../BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) (function, `0x00BA9BB4`)
- `0x00BB874D` → [ViDeadlockSimilarNode](../BA/ViDeadlockSimilarNode_function_00BAA248.md) (function, `0x00BAA248`)
- `0x00BB8763` → [ViDeadlockCheckDuplicatesAmongChildren](../BA/ViDeadlockCheckDuplicatesAmongChildren_function_00BA9038.md) (function, `0x00BA9038`)
- `0x00BB878A` → [ViDeadlockAnalyze](../BA/ViDeadlockAnalyze_function_00BA8BD4.md) (function, `0x00BA8BD4`)
- `0x00BB87C9` → [ViDeadlockSimilarNode](../BA/ViDeadlockSimilarNode_function_00BAA248.md) (function, `0x00BAA248`)
- `0x00BB87DC` → [ViDeadlockCheckDuplicatesAmongRoots](../BA/ViDeadlockCheckDuplicatesAmongRoots_function_00BA90B8.md) (function, `0x00BA90B8`)
- `0x00BB888F` → [ViDeadlockUpdateChildrenCount](../BA/ViDeadlockUpdateChildrenCount_function_00BAA294.md) (function, `0x00BAA294`)
- `0x00BB89BA` → [ViDeadlockDetectionUnlock](../BA/ViDeadlockDetectionUnlock_function_00BA91FC.md) (function, `0x00BA91FC`)
- `0x00BB89C3` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (function, `0x00616278`)
- `0x00BB89D9` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB89F6` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A07` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A1D` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A2C` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A42` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A54` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB8A60` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ViDeadlockExAcquireFastMutexUnsafe_Exit](../BA/ViDeadlockExAcquireFastMutexUnsafe_Exit_function_00BA93C0.md) at `0x00BA93E0`
- [ViDeadlockExAcquireFastMutex_Exit](../BA/ViDeadlockExAcquireFastMutex_Exit_function_00BA9400.md) at `0x00BA9420`
- [ViDeadlockExAcquireResourceExclusiveLite_Exit](../BA/ViDeadlockExAcquireResourceExclusiveLite_Exit_function_00BA9440.md) at `0x00BA946F`
- [ViDeadlockExEnterCriticalRegionAndAcquireResourceExclusive_Exit](../BA/ViDeadlockExEnterCriticalRegionAndAcquireResourceExclusive_Exit_function_00BA9480.md) at `0x00BA94A0`
- [ViDeadlockExTryToAcquireFastMutex_Exit](../BA/ViDeadlockExTryToAcquireFastMutex_Exit_function_00BA9520.md) at `0x00BA9548`
- [ViDeadlockKeAcquireInStackQueuedSpinLockAtDpcLevel_Exit](../BA/ViDeadlockKeAcquireInStackQueuedSpinLockAtDpcLevel_Exit_function_00BA96C0.md) at `0x00BA96E0`
- [ViDeadlockKeInitializeMutant_Exit](../BA/ViDeadlockKeInitializeMutant_Exit_function_00BA9700.md) at `0x00BA9737`
- [ViDeadlockKeTryToAcquireSpinLockAtDpcLevel_Exit](../BA/ViDeadlockKeTryToAcquireSpinLockAtDpcLevel_Exit_function_00BA9840.md) at `0x00BA9868`
- [ViDeadlockObjectAcquired](../BA/ViDeadlockObjectAcquired_function_00BA9AD4.md) at `0x00BA9B1F`
- [ViDeadlockKeAcquireSpinLockAtDpcLevel_Exit](ViDeadlockKeAcquireSpinLockAtDpcLevel_Exit_function_00BB8380.md) at `0x00BB83A0`

### Static image references
- `0x00BB83D0` → RVA `0x00E0A740` (`.data`; read)
- `0x00BB8421` → RVA `0x00FFDAC0` (`PAGEVRFD`; read)
- `0x00BB843A` → RVA `0x00FFDAEC` (`PAGEVRFD`; read)
- `0x00BB8469` → RVA `0x00FFDA00` (`PAGEVRFD`; read)
- `0x00BB8495` → RVA `0x00B8B0A8` (`ViDeadlockResourceTypeInfo`; read)
- `0x00BB852C` → RVA `0x00FFDA78` (`PAGEVRFD`; read)
- `0x00BB8661` → RVA `0x00E0EA2C` (`.data`; read)
- `0x00BB866D` → RVA `0x00BBB090` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB86FE` → RVA `0x00E0EA1C` (`.data`; read)
- `0x00BB870D` → RVA `0x00BBB060` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB88C4` → RVA `0x00FFDA20` (`PAGEVRFD`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00BB8400` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGEVRFY` → `.text`)
  - `0x00BB84E6` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8509` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB86A0` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (`PAGEVRFY` → `.text`)
  - `0x00BB89C3` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8A60` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB83B4  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00BB83B9  55                              push rbp
00BB83BA  56                              push rsi
00BB83BB  57                              push rdi
00BB83BC  41 54                           push r12
00BB83BE  41 55                           push r13
00BB83C0  41 56                           push r14
00BB83C2  41 57                           push r15
00BB83C4  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00BB83C9  48 81 EC E0 00 00 00            sub rsp, 0xe0
00BB83D0  48 8B 05 69 23 25 00            mov rax, qword ptr [rip + 0x252369]
00BB83D7  48 33 C4                        xor rax, rsp
00BB83DA  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00BB83DE  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
00BB83E2  49 8B F0                        mov rsi, r8
00BB83E5  48 63 FA                        movsxd rdi, edx
00BB83E8  4C 8B E1                        mov r12, rcx
00BB83EB  33 D2                           xor edx, edx
00BB83ED  44 89 4D 87                     mov dword ptr [rbp - 0x79], r9d
00BB83F1  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00BB83F5  89 7D AB                        mov dword ptr [rbp - 0x55], edi
00BB83F8  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
00BB83FC  44 8D 42 40                     lea r8d, [rdx + 0x40]
00BB8400  E8 3B E8 B0 FF                  call 0x1406c6c40
00BB8405  45 33 ED                        xor r13d, r13d
00BB8408  44 89 6D 97                     mov dword ptr [rbp - 0x69], r13d
00BB840C  45 8B FD                        mov r15d, r13d
00BB840F  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00BB8414  4C 89 6D B7                     mov qword ptr [rbp - 0x49], r13
00BB8418  4C 89 6D 8F                     mov qword ptr [rbp - 0x71], r13
00BB841C  83 FF 08                        cmp edi, 8
00BB841F  75 2B                           jne 0x140bb844c
00BB8421  48 8B 0D 98 56 44 00            mov rcx, qword ptr [rip + 0x445698]
00BB8428  48 85 C9                        test rcx, rcx
00BB842B  0F 84 28 06 00 00               je 0x140bb8a59
00BB8431  48 3B CB                        cmp rcx, rbx
00BB8434  0F 87 1F 06 00 00               ja 0x140bb8a59
00BB843A  8B 05 AC 56 44 00               mov eax, dword ptr [rip + 0x4456ac]
00BB8440  48 03 C1                        add rax, rcx
00BB8443  48 3B C3                        cmp rax, rbx
00BB8446  0F 86 0D 06 00 00               jbe 0x140bb8a59
00BB844C  49 8B CC                        mov rcx, r12
00BB844F  E8 30 F7 FF FF                  call 0x140bb7b84
00BB8454  85 C0                           test eax, eax
00BB8456  0F 84 FD 05 00 00               je 0x140bb8a59
00BB845C  E8 73 1E FF FF                  call 0x140baa2d4
00BB8461  85 C0                           test eax, eax
00BB8463  0F 85 F0 05 00 00               jne 0x140bb8a59
00BB8469  48 8B 05 90 55 44 00            mov rax, qword ptr [rip + 0x445590]
00BB8470  8B 88 10 80 00 00               mov ecx, dword ptr [rax + 0x8010]
00BB8476  85 C9                           test ecx, ecx
00BB8478  0F 85 DB 05 00 00               jne 0x140bb8a59
00BB847E  48 8B 05 7B 55 44 00            mov rax, qword ptr [rip + 0x44557b]
00BB8485  81 B8 68 81 00 00 00 04 00 00   cmp dword ptr [rax + 0x8168], 0x400
00BB848F  0F 8F C4 05 00 00               jg 0x140bb8a59
00BB8495  48 8D 05 0C 2C FD FF            lea rax, [rip - 0x2d3f4]
00BB849C  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
00BB84A0  8B 04 B8                        mov eax, dword ptr [rax + rdi*4]
00BB84A3  4D 8B F5                        mov r14, r13
00BB84A6  B9 03 00 00 00                  mov ecx, 3
00BB84AB  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00BB84AE  4C 8B EF                        mov r13, rdi
00BB84B1  E8 C2 06 FF FF                  call 0x140ba8b78
00BB84B6  B9 02 00 00 00                  mov ecx, 2
00BB84BB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00BB84C0  E8 B3 06 FF FF                  call 0x140ba8b78
00BB84C5  B9 01 00 00 00                  mov ecx, 1
00BB84CA  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00BB84CE  E8 A5 06 FF FF                  call 0x140ba8b78
00BB84D3  45 33 C9                        xor r9d, r9d
00BB84D6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00BB84DB  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00BB84DF  41 8D 51 08                     lea edx, [r9 + 8]
00BB84E3  8D 4A FA                        lea ecx, [rdx - 6]
00BB84E6  E8 05 1B 74 FF                  call 0x1402f9ff0
00BB84EB  0F B7 C8                        movzx ecx, ax
00BB84EE  85 C9                           test ecx, ecx
00BB84F0  75 0B                           jne 0x140bb84fd
00BB84F2  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
00BB84F6  B9 01 00 00 00                  mov ecx, 1
00BB84FB  EB 05                           jmp 0x140bb8502
00BB84FD  83 F9 08                        cmp ecx, 8
00BB8500  73 07                           jae 0x140bb8509
00BB8502  8B C1                           mov eax, ecx
00BB8504  4C 21 74 C5 CF                  and qword ptr [rbp + rax*8 - 0x31], r14
00BB8509  E8 A2 DD A5 FF                  call 0x1406162b0
00BB850E  B9 01 00 00 00                  mov ecx, 1
00BB8513  88 44 24 34                     mov byte ptr [rsp + 0x34], al
00BB8517  E8 A8 0C FF FF                  call 0x140ba91c4
00BB851C  48 B9 20 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000320
00BB8526  45 33 C0                        xor r8d, r8d
00BB8529  48 8B 19                        mov rbx, qword ptr [rcx]
00BB852C  8B 0D 46 55 44 00               mov ecx, dword ptr [rip + 0x445546]
00BB8532  85 C9                           test ecx, ecx
00BB8534  0F 84 4B 04 00 00               je 0x140bb8985
00BB853A  4C 8B 55 AF                     mov r10, qword ptr [rbp - 0x51]
00BB853E  4C 89 55 9F                     mov qword ptr [rbp - 0x61], r10
00BB8542  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
00BB8546  4D 85 D2                        test r10, r10
00BB8549  0F 84 36 04 00 00               je 0x140bb8985
00BB854F  48 8B CE                        mov rcx, rsi
00BB8552  E8 55 1C FF FF                  call 0x140baa1ac
00BB8557  4C 8B F0                        mov r14, rax
00BB855A  48 85 C0                        test rax, rax
00BB855D  75 29                           jne 0x140bb8588
00BB855F  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00BB8564  48 8B CE                        mov rcx, rsi
00BB8567  E8 4C 05 FF FF                  call 0x140ba8ab8
00BB856C  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00BB8571  4C 8B F0                        mov r14, rax
00BB8574  41 BA 01 00 00 00               mov r10d, 1
00BB857A  48 85 C0                        test rax, rax
00BB857D  0F 84 F8 03 00 00               je 0x140bb897b
00BB8583  45 8B FA                        mov r15d, r10d
00BB8586  EB 06                           jmp 0x140bb858e
00BB8588  41 BA 01 00 00 00               mov r10d, 1
00BB858E  83 FF 08                        cmp edi, 8
00BB8591  75 12                           jne 0x140bb85a5
00BB8593  45 88 56 30                     mov byte ptr [r14 + 0x30], r10b
00BB8597  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB859C  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00BB85A0  E9 EE 03 00 00                  jmp 0x140bb8993
00BB85A5  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00BB85A9  49 8B CC                        mov rcx, r12
00BB85AC  E8 1F 1B FF FF                  call 0x140baa0d0
00BB85B1  45 33 C0                        xor r8d, r8d
00BB85B4  48 8B F0                        mov rsi, rax
00BB85B7  48 85 C0                        test rax, rax
00BB85BA  75 46                           jne 0x140bb8602
00BB85BC  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB85C1  48 8D 45 8F                     lea rax, [rbp - 0x71]
00BB85C5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BB85CA  4C 8D 4D CF                     lea r9, [rbp - 0x31]
00BB85CE  48 8D 45 B7                     lea rax, [rbp - 0x49]
00BB85D2  4C 8B C6                        mov r8, rsi
00BB85D5  8B D7                           mov edx, edi
00BB85D7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB85DC  49 8B CC                        mov rcx, r12
00BB85DF  E8 8C 02 FF FF                  call 0x140ba8870
00BB85E4  45 33 C0                        xor r8d, r8d
00BB85E7  85 C0                           test eax, eax
00BB85E9  74 51                           je 0x140bb863c
00BB85EB  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00BB85EF  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00BB85F4  49 8B CC                        mov rcx, r12
00BB85F7  E8 D4 1A FF FF                  call 0x140baa0d0
00BB85FC  48 8B F0                        mov rsi, rax
00BB85FF  45 33 C0                        xor r8d, r8d
00BB8602  48 63 0E                        movsxd rcx, dword ptr [rsi]
00BB8605  41 BA 01 00 00 00               mov r10d, 1
00BB860B  3B CF                           cmp ecx, edi
00BB860D  74 1F                           je 0x140bb862e
00BB860F  8D 47 FD                        lea eax, [rdi - 3]
00BB8612  41 3B C2                        cmp eax, r10d
00BB8615  77 08                           ja 0x140bb861f
00BB8617  8D 41 FD                        lea eax, [rcx - 3]
00BB861A  41 3B C2                        cmp eax, r10d
00BB861D  76 0D                           jbe 0x140bb862c
00BB861F  83 F9 07                        cmp ecx, 7
00BB8622  75 38                           jne 0x140bb865c
00BB8624  8D 47 FB                        lea eax, [rdi - 5]
00BB8627  41 3B C2                        cmp eax, r10d
00BB862A  77 30                           ja 0x140bb865c
00BB862C  89 3E                           mov dword ptr [rsi], edi
00BB862E  8D 47 FB                        lea eax, [rdi - 5]
00BB8631  41 3B C2                        cmp eax, r10d
00BB8634  76 7D                           jbe 0x140bb86b3
00BB8636  4D 8B 6E 10                     mov r13, qword ptr [r14 + 0x10]
00BB863A  EB 7B                           jmp 0x140bb86b7
00BB863C  45 85 FF                        test r15d, r15d
00BB863F  0F 84 45 03 00 00               je 0x140bb898a
00BB8645  33 D2                           xor edx, edx
00BB8647  49 8B CE                        mov rcx, r14
00BB864A  BF 01 00 00 00                  mov edi, 1
00BB864F  E8 38 19 FF FF                  call 0x140ba9f8c
00BB8654  44 8B D7                        mov r10d, edi
00BB8657  E9 37 03 00 00                  jmp 0x140bb8993
00BB865C  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00BB8661  48 8D 3D C4 63 25 00            lea rdi, [rip + 0x2563c4]
00BB8668  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00BB866D  48 8D 15 1C 2A 00 00            lea rdx, [rip + 0x2a1c]
00BB8674  41 BF 08 10 00 00               mov r15d, 0x1008
00BB867A  48 8B CF                        mov rcx, rdi
00BB867D  45 8B C7                        mov r8d, r15d
00BB8680  4D 8B CC                        mov r9, r12
00BB8683  E8 2C 15 FF FF                  call 0x140ba9bb4
00BB8688  4C 63 0E                        movsxd r9, dword ptr [rsi]
00BB868B  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00BB8690  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00BB8695  4D 8B C4                        mov r8, r12
00BB8698  49 8B D7                        mov rdx, r15
00BB869B  B9 C4 00 00 00                  mov ecx, 0xc4
00BB86A0  E8 9F BD A5 FF                  call 0x140614444
00BB86A5  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB86AA  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00BB86AE  E9 DA 02 00 00                  jmp 0x140bb898d
00BB86B3  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
00BB86B7  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00BB86BB  48 85 C0                        test rax, rax
00BB86BE  74 0A                           je 0x140bb86ca
00BB86C0  49 3B C6                        cmp rax, r14
00BB86C3  74 05                           je 0x140bb86ca
00BB86C5  66 44 89 46 06                  mov word ptr [rsi + 6], r8w
00BB86CA  0F B7 46 06                     movzx eax, word ptr [rsi + 6]
00BB86CE  66 41 03 C2                     add ax, r10w
00BB86D2  4C 89 76 10                     mov qword ptr [rsi + 0x10], r14
00BB86D6  66 89 46 06                     mov word ptr [rsi + 6], ax
00BB86DA  4D 85 ED                        test r13, r13
00BB86DD  0F 84 C1 00 00 00               je 0x140bb87a4
00BB86E3  66 41 3B C2                     cmp ax, r10w
00BB86E7  76 48                           jbe 0x140bb8731
00BB86E9  44 84 55 A7                     test byte ptr [rbp - 0x59], r10b
00BB86ED  0F 85 A4 FE FF FF               jne 0x140bb8597
00BB86F3  41 BF 00 10 00 00               mov r15d, 0x1000
00BB86F9  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00BB86FE  48 8D 3D 17 63 25 00            lea rdi, [rip + 0x256317]
00BB8705  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00BB870A  45 8B C7                        mov r8d, r15d
00BB870D  48 8D 15 4C 29 00 00            lea rdx, [rip + 0x294c]
00BB8714  48 8B CF                        mov rcx, rdi
00BB8717  4D 8B CC                        mov r9, r12
00BB871A  E8 95 14 FF FF                  call 0x140ba9bb4
00BB871F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00BB8724  4C 8B CE                        mov r9, rsi
00BB8727  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00BB872C  E9 64 FF FF FF                  jmp 0x140bb8695
00BB8731  8B 55 87                        mov edx, dword ptr [rbp - 0x79]
00BB8734  4D 8D 7D 08                     lea r15, [r13 + 8]
00BB8738  4D 8B 0F                        mov r9, qword ptr [r15]
00BB873B  4D 3B CF                        cmp r9, r15
00BB873E  74 2A                           je 0x140bb876a
00BB8740  49 8D 79 E8                     lea rdi, [r9 - 0x18]
00BB8744  49 8B CC                        mov rcx, r12
00BB8747  4D 8B 09                        mov r9, qword ptr [r9]
00BB874A  4C 8B C7                        mov r8, rdi
00BB874D  E8 F6 1A FF FF                  call 0x140baa248
00BB8752  45 33 C0                        xor r8d, r8d
00BB8755  85 C0                           test eax, eax
00BB8757  74 E2                           je 0x140bb873b
00BB8759  4C 8D 45 8F                     lea r8, [rbp - 0x71]
00BB875D  48 8B D7                        mov rdx, rdi
00BB8760  49 8B CD                        mov rcx, r13
00BB8763  E8 D0 08 FF FF                  call 0x140ba9038
00BB8768  EB 77                           jmp 0x140bb87e1
00BB876A  66 83 7E 04 00                  cmp word ptr [rsi + 4], 0
00BB876F  74 29                           je 0x140bb879a
00BB8771  85 D2                           test edx, edx
00BB8773  75 25                           jne 0x140bb879a
00BB8775  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00BB8779  45 33 C9                        xor r9d, r9d
00BB877C  45 8B C2                        mov r8d, r10d
00BB877F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB8784  49 8B D5                        mov rdx, r13
00BB8787  49 8B CC                        mov rcx, r12
00BB878A  E8 45 04 FF FF                  call 0x140ba8bd4
00BB878F  45 33 C0                        xor r8d, r8d
00BB8792  45 8D 50 01                     lea r10d, [r8 + 1]
00BB8796  85 C0                           test eax, eax
00BB8798  75 57                           jne 0x140bb87f1
00BB879A  44 8B 5D 87                     mov r11d, dword ptr [rbp - 0x79]
00BB879E  4C 8D 4E 18                     lea r9, [rsi + 0x18]
00BB87A2  EB 68                           jmp 0x140bb880c
00BB87A4  44 8B 5D 87                     mov r11d, dword ptr [rbp - 0x79]
00BB87A8  4C 8D 4E 18                     lea r9, [rsi + 0x18]
00BB87AC  4D 8B 11                        mov r10, qword ptr [r9]
00BB87AF  4D 3B D1                        cmp r10, r9
00BB87B2  74 4A                           je 0x140bb87fe
00BB87B4  49 8D 7A D8                     lea rdi, [r10 - 0x28]
00BB87B8  4D 8B 12                        mov r10, qword ptr [r10]
00BB87BB  4C 39 07                        cmp qword ptr [rdi], r8
00BB87BE  75 EF                           jne 0x140bb87af
00BB87C0  4C 8B C7                        mov r8, rdi
00BB87C3  41 8B D3                        mov edx, r11d
00BB87C6  49 8B CC                        mov rcx, r12
00BB87C9  E8 7A 1A FF FF                  call 0x140baa248
00BB87CE  45 33 C0                        xor r8d, r8d
00BB87D1  85 C0                           test eax, eax
00BB87D3  74 DA                           je 0x140bb87af
00BB87D5  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00BB87D9  48 8B CF                        mov rcx, rdi
00BB87DC  E8 D7 08 FF FF                  call 0x140ba90b8
00BB87E1  45 33 C0                        xor r8d, r8d
00BB87E4  45 8D 50 01                     lea r10d, [r8 + 1]
00BB87E8  48 85 FF                        test rdi, rdi
00BB87EB  0F 85 DA 00 00 00               jne 0x140bb88cb
00BB87F1  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB87F6  41 8B F8                        mov edi, r8d
00BB87F9  E9 95 01 00 00                  jmp 0x140bb8993
00BB87FE  41 BA 01 00 00 00               mov r10d, 1
00BB8804  4D 8D 7D 08                     lea r15, [r13 + 8]
00BB8808  44 89 55 97                     mov dword ptr [rbp - 0x69], r10d
00BB880C  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00BB8810  48 8B F8                        mov rdi, rax
00BB8813  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
00BB8817  4C 89 40 50                     mov qword ptr [rax + 0x50], r8
00BB881B  4C 89 80 90 00 00 00            mov qword ptr [rax + 0x90], r8
00BB8822  48 8D 57 18                     lea rdx, [rdi + 0x18]
00BB8826  48 83 60 48 00                  and qword ptr [rax + 0x48], 0
00BB882B  4C 89 40 40                     mov qword ptr [rax + 0x40], r8
00BB882F  4C 89 28                        mov qword ptr [rax], r13
00BB8832  48 89 70 38                     mov qword ptr [rax + 0x38], rsi
00BB8836  48 8B 05 C3 51 44 00            mov rax, qword ptr [rip + 0x4451c3]
00BB883D  8B 88 24 80 00 00               mov ecx, dword ptr [rax + 0x8024]
00BB8843  48 8D 47 08                     lea rax, [rdi + 8]
00BB8847  C1 E1 03                        shl ecx, 3
00BB884A  89 4F 48                        mov dword ptr [rdi + 0x48], ecx
00BB884D  43 8D 0C 1B                     lea ecx, [r11 + r11]
00BB8851  48 89 40 08                     mov qword ptr [rax + 8], rax
00BB8855  48 89 00                        mov qword ptr [rax], rax
00BB8858  48 89 52 08                     mov qword ptr [rdx + 8], rdx
00BB885C  48 89 12                        mov qword ptr [rdx], rdx
00BB885F  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00BB8862  33 C8                           xor ecx, eax
00BB8864  83 E1 02                        and ecx, 2
00BB8867  33 C8                           xor ecx, eax
00BB8869  89 4F 48                        mov dword ptr [rdi + 0x48], ecx
00BB886C  44 39 45 97                     cmp dword ptr [rbp - 0x69], r8d
00BB8870  75 22                           jne 0x140bb8894
00BB8872  49 8B 07                        mov rax, qword ptr [r15]
00BB8875  4C 39 78 08                     cmp qword ptr [rax + 8], r15
00BB8879  75 26                           jne 0x140bb88a1
00BB887B  48 89 02                        mov qword ptr [rdx], rax
00BB887E  49 8B CD                        mov rcx, r13
00BB8881  4C 89 7A 08                     mov qword ptr [rdx + 8], r15
00BB8885  48 89 50 08                     mov qword ptr [rax + 8], rdx
00BB8889  49 89 17                        mov qword ptr [r15], rdx
00BB888C  41 8B D2                        mov edx, r10d
00BB888F  E8 00 1A FF FF                  call 0x140baa294
00BB8894  49 8B 11                        mov rdx, qword ptr [r9]
00BB8897  48 8D 47 28                     lea rax, [rdi + 0x28]
00BB889B  4C 39 4A 08                     cmp qword ptr [rdx + 8], r9
00BB889F  74 07                           je 0x140bb88a8
00BB88A1  B9 03 00 00 00                  mov ecx, 3
00BB88A6  CD 29                           int 0x29
00BB88A8  48 89 10                        mov qword ptr [rax], rdx
00BB88AB  4C 89 48 08                     mov qword ptr [rax + 8], r9
00BB88AF  48 89 42 08                     mov qword ptr [rdx + 8], rax
00BB88B3  49 89 01                        mov qword ptr [r9], rax
00BB88B6  66 44 01 56 04                  add word ptr [rsi + 4], r10w
00BB88BB  8B 46 04                        mov eax, dword ptr [rsi + 4]
00BB88BE  66 3D F0 FF                     cmp ax, 0xfff0
00BB88C2  76 07                           jbe 0x140bb88cb
00BB88C4  83 0D 55 51 44 00 20            or dword ptr [rip + 0x445155], 0x20
00BB88CB  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00BB88CE  44 09 57 48                     or dword ptr [rdi + 0x48], r10d
00BB88D2  83 C0 FB                        add eax, -5
00BB88D5  4C 89 77 40                     mov qword ptr [rdi + 0x40], r14
00BB88D9  41 3B C2                        cmp eax, r10d
00BB88DC  76 06                           jbe 0x140bb88e4
00BB88DE  49 89 7E 10                     mov qword ptr [r14 + 0x10], rdi
00BB88E2  EB 04                           jmp 0x140bb88e8
00BB88E4  49 89 7E 08                     mov qword ptr [r14 + 8], rdi
00BB88E8  45 01 56 28                     add dword ptr [r14 + 0x28], r10d
00BB88EC  48 8B 07                        mov rax, qword ptr [rdi]
00BB88EF  48 85 C0                        test rax, rax
00BB88F2  74 2F                           je 0x140bb8923
00BB88F4  0F 10 40 50                     movups xmm0, xmmword ptr [rax + 0x50]
00BB88F8  0F 11 87 90 00 00 00            movups xmmword ptr [rdi + 0x90], xmm0
00BB88FF  0F 10 48 60                     movups xmm1, xmmword ptr [rax + 0x60]
00BB8903  0F 11 8F A0 00 00 00            movups xmmword ptr [rdi + 0xa0], xmm1
00BB890A  0F 10 40 70                     movups xmm0, xmmword ptr [rax + 0x70]
00BB890E  0F 11 87 B0 00 00 00            movups xmmword ptr [rdi + 0xb0], xmm0
00BB8915  0F 10 88 80 00 00 00            movups xmm1, xmmword ptr [rax + 0x80]
00BB891C  0F 11 8F C0 00 00 00            movups xmmword ptr [rdi + 0xc0], xmm1
00BB8923  0F 28 45 CF                     movaps xmm0, xmmword ptr [rbp - 0x31]
00BB8927  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00BB892B  0F 11 47 50                     movups xmmword ptr [rdi + 0x50], xmm0
00BB892F  0F 28 4D DF                     movaps xmm1, xmmword ptr [rbp - 0x21]
00BB8933  0F 11 4F 60                     movups xmmword ptr [rdi + 0x60], xmm1
00BB8937  0F 28 45 EF                     movaps xmm0, xmmword ptr [rbp - 0x11]
00BB893B  0F 11 47 70                     movups xmmword ptr [rdi + 0x70], xmm0
00BB893F  0F 28 4D FF                     movaps xmm1, xmmword ptr [rbp - 1]
00BB8943  0F 11 8F 80 00 00 00            movups xmmword ptr [rdi + 0x80], xmm1
00BB894A  0F 10 47 50                     movups xmm0, xmmword ptr [rdi + 0x50]
00BB894E  0F 11 40 78                     movups xmmword ptr [rax + 0x78], xmm0
00BB8952  0F 10 4F 60                     movups xmm1, xmmword ptr [rdi + 0x60]
00BB8956  0F 11 88 88 00 00 00            movups xmmword ptr [rax + 0x88], xmm1
00BB895D  0F 10 47 70                     movups xmm0, xmmword ptr [rdi + 0x70]
00BB8961  0F 11 80 98 00 00 00            movups xmmword ptr [rax + 0x98], xmm0
00BB8968  0F 10 8F 80 00 00 00            movups xmm1, xmmword ptr [rdi + 0x80]
00BB896F  0F 11 88 A8 00 00 00            movups xmmword ptr [rax + 0xa8], xmm1
00BB8976  E9 1C FC FF FF                  jmp 0x140bb8597
00BB897B  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB8980  41 8B FF                        mov edi, r15d
00BB8983  EB 13                           jmp 0x140bb8998
00BB8985  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BB898A  41 8B F8                        mov edi, r8d
00BB898D  41 BA 01 00 00 00               mov r10d, 1
00BB8993  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00BB8998  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00BB89A2  48 8B 00                        mov rax, qword ptr [rax]
00BB89A5  48 8B 0D 54 50 44 00            mov rcx, qword ptr [rip + 0x445054]
00BB89AC  48 2B C3                        sub rax, rbx
00BB89AF  48 3B 01                        cmp rax, qword ptr [rcx]
00BB89B2  7E 03                           jle 0x140bb89b7
00BB89B4  48 89 01                        mov qword ptr [rcx], rax
00BB89B7  41 8B CA                        mov ecx, r10d
00BB89BA  E8 3D 08 FF FF                  call 0x140ba91fc
00BB89BF  8A 4C 24 34                     mov cl, byte ptr [rsp + 0x34]
00BB89C3  E8 B0 D8 A5 FF                  call 0x140616278
00BB89C8  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00BB89CC  48 85 C9                        test rcx, rcx
00BB89CF  74 15                           je 0x140bb89e6
00BB89D1  48 8B 19                        mov rbx, qword ptr [rcx]
00BB89D4  BA 02 00 00 00                  mov edx, 2
00BB89D9  E8 92 0C FF FF                  call 0x140ba9670
00BB89DE  48 8B CB                        mov rcx, rbx
00BB89E1  48 85 DB                        test rbx, rbx
00BB89E4  75 EB                           jne 0x140bb89d1
00BB89E6  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00BB89EA  BB 01 00 00 00                  mov ebx, 1
00BB89EF  48 85 C9                        test rcx, rcx
00BB89F2  74 07                           je 0x140bb89fb
00BB89F4  8B D3                           mov edx, ebx
00BB89F6  E8 75 0C FF FF                  call 0x140ba9670
00BB89FB  85 FF                           test edi, edi
00BB89FD  74 0D                           je 0x140bb8a0c
00BB89FF  BA 03 00 00 00                  mov edx, 3
00BB8A04  49 8B CE                        mov rcx, r14
00BB8A07  E8 64 0C FF FF                  call 0x140ba9670
00BB8A0C  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00BB8A10  48 85 C0                        test rax, rax
00BB8A13  74 0D                           je 0x140bb8a22
00BB8A15  BA 02 00 00 00                  mov edx, 2
00BB8A1A  48 8B C8                        mov rcx, rax
00BB8A1D  E8 4E 0C FF FF                  call 0x140ba9670
00BB8A22  48 85 F6                        test rsi, rsi
00BB8A25  74 0A                           je 0x140bb8a31
00BB8A27  8B D3                           mov edx, ebx
00BB8A29  48 8B CE                        mov rcx, rsi
00BB8A2C  E8 3F 0C FF FF                  call 0x140ba9670
00BB8A31  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00BB8A35  48 85 C0                        test rax, rax
00BB8A38  74 0D                           je 0x140bb8a47
00BB8A3A  BA 02 00 00 00                  mov edx, 2
00BB8A3F  48 8B C8                        mov rcx, rax
00BB8A42  E8 29 0C FF FF                  call 0x140ba9670
00BB8A47  4D 85 FF                        test r15, r15
00BB8A4A  74 0D                           je 0x140bb8a59
00BB8A4C  BA 03 00 00 00                  mov edx, 3
00BB8A51  49 8B CF                        mov rcx, r15
00BB8A54  E8 17 0C FF FF                  call 0x140ba9670
00BB8A59  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
00BB8A5D  48 33 CC                        xor rcx, rsp
00BB8A60  E8 DB 3B AF FF                  call 0x1406ac640
00BB8A65  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
00BB8A6D  48 81 C4 E0 00 00 00            add rsp, 0xe0
00BB8A74  41 5F                           pop r15
00BB8A76  41 5E                           pop r14
00BB8A78  41 5D                           pop r13
00BB8A7A  41 5C                           pop r12
00BB8A7C  5F                              pop rdi
00BB8A7D  5E                              pop rsi
00BB8A7E  5D                              pop rbp
00BB8A7F  C3                              ret
00BB8A80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfDeadlockAcquireResource(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 2433897)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    v_stack_mD0 = a4;
    v_stack_mAC = (unsigned int)((int)(a2));
    v_stack_m98 = a5;
    result = memset(v_stack_m88, a2, a2 + 64, a4);
    v_r13 = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = 0;
    v_stack_mA0 = 0;
    v_stack_mC8 = 0;
    if (((unsigned int)((int)(a2))) != 8) goto loc_00BB844C;
    if (*(unsigned __int64 *)(v_rip + 4478616) == 0) goto loc_00BB8A59;
    if ((*(unsigned __int64 *)(v_rip + 4478616)) > a5) goto loc_00BB8A59;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 4478636))) + (*(unsigned __int64 *)(v_rip + 4478616));
    if (result <= a5) goto loc_00BB8A59;
loc_00BB844C:
    result = ViDeadlockCanProceed(a1, a2, a2 + 64, a4);
    if ((unsigned int)(result) == 0) goto loc_00BB8A59;
    result = ViIsThreadInsidePagingCodePaths(a1, a2, a2 + 64, a4);
    if ((unsigned int)(result) != 0) goto loc_00BB8A59;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4478352) + 32784))) != 0) goto loc_00BB8A59;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4478331) + 33128)) > 0x400ULL) goto loc_00BB8A59;
    v_stack_mB8 = 0;
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 185332 + (int)(a2) * 4)));
    result = ViDeadlockAllocate(3, a2, a2 + 64, a4);
    v_stack_mE0 = result;
    result = ViDeadlockAllocate(2, a2, a2 + 64, a4);
    v_stack_mA8 = result;
    result = ViDeadlockAllocate(1, a2, a2 + 64, a4);
    a4 = 0;
    v_stack_mD8 = result;
    result = RtlCaptureStackBackTrace(a4 + 8 - 6, a4 + 8, v_stack_m88, a4);
    if ((unsigned int)((unsigned __int16)(result)) != 0) goto loc_00BB84FD;
    v_stack_m88 = a5;
    goto loc_00BB8502;
loc_00BB84FD:
    if (1 < 8) {
        result = 1;
    }
    result = ViRaiseIrqlToDpcLevel(1, a4 + 8, v_stack_m88, a4);
    v_stack_mE4 = (unsigned __int8)(result);
    result = ViDeadlockDetectionLock(1, a4 + 8, v_stack_m88, a4);
    a3 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4478278))) == 0) goto loc_00BB8985;
    v_stack_mB8 = v_stack_mA8;
    v_stack_mA8 = 0;
    if (v_stack_mA8 == 0) goto loc_00BB8985;
    result = ViDeadlockSearchThread(0, a4 + 8, a3, a4);
    if (result != 0) goto loc_00BB8588;
    result = ViDeadlockAddThread(0, v_stack_mE0, a3, a4);
    v_stack_mE0 = 0;
    if (result == 0) goto loc_00BB897B;
    goto loc_00BB858E;
loc_00BB8588:
loc_00BB858E:
    if (((unsigned int)((int)(a2))) != 8) goto loc_00BB85A5;
    *(unsigned __int8 *)(result + 48) = 1;
loc_00BB8597:
    goto loc_00BB8993;
loc_00BB85A5:
    result = ViDeadlockSearchResource(a1, v_stack_mC8, a3, a4);
    a3 = 0;
    if (result != 0) goto loc_00BB8602;
    v_stack_mF0 = v_stack_mC8;
    v_stack_mF8 = v_stack_mA0;
    result = ViDeadlockAddResource(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_mE8))), v_stack_mD8, v_stack_m88);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_00BB863C;
    v_stack_mD8 = 0;
    result = ViDeadlockSearchResource(a1, v_stack_mC8, a3, v_stack_m88);
    a3 = 0;
loc_00BB8602:
    if (((unsigned int)((int)(*(unsigned int *)(result)))) == ((unsigned int)((unsigned int)(v_stack_mE8)))) goto loc_00BB862E;
    if (((unsigned int)((unsigned int)(v_stack_mE8) - 3)) > 1) goto loc_00BB861F;
    if (((unsigned int)((int)(*(unsigned int *)(result)) - 3)) <= 1) goto loc_00BB862C;
loc_00BB861F:
    if (((unsigned int)((int)(*(unsigned int *)(result)))) != 7) goto loc_00BB865C;
    if (((unsigned int)((unsigned int)(v_stack_mE8) - 5)) > 1) goto loc_00BB865C;
loc_00BB862C:
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_mE8));
loc_00BB862E:
    if (((unsigned int)((unsigned int)(v_stack_mE8) - 5)) <= 1) goto loc_00BB86B3;
    goto loc_00BB86B7;
loc_00BB863C:
    if (1 == 0) goto loc_00BB898A;
    a2 = 0;
    result = ViDeadlockRemoveThread(result, a2, a3, v_stack_m88);
    goto loc_00BB8993;
loc_00BB865C:
    v_stack_mF0 = *(unsigned __int64 *)(result + 16);
    v_stack_mF8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2450372, v_rip + 10780, (unsigned int)((unsigned int)((unsigned int)(0x1008ULL))), a1);
    v_stack_mF0 = v_rip + 2450372;
    v_stack_mF8 = *(unsigned __int64 *)(result + 16);
loc_00BB8695:
    result = VfReportIssueWithOptions(196, (unsigned int)(0x1008ULL), a1, (int)(*(unsigned int *)(result)));
    goto loc_00BB898D;
loc_00BB86B3:
loc_00BB86B7:
    if (*(unsigned __int64 *)(v_stack_mD8 + 16) == 0) goto loc_00BB86CA;
    if ((*(unsigned __int64 *)(v_stack_mD8 + 16)) != result) {
        *(unsigned __int16 *)(v_stack_mD8 + 6) = (unsigned __int16)(a1);
    }
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_mD8 + 6)) + (1));
    *(unsigned __int64 *)(v_stack_mD8 + 16) = result;
    *(unsigned __int16 *)(v_stack_mD8 + 6) = (unsigned __int16)(result);
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00BB87A4;
    if (((unsigned __int16)(result)) <= 1) goto loc_00BB8731;
    if (((v_stack_mB0) & (1)) != 0) goto loc_00BB8597;
    v_stack_mF0 = result;
    v_stack_mF8 = v_stack_mD8;
    result = ViDeadlockPreprocessOptions(v_rip + 2450199, v_rip + 10572, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a1);
    v_stack_mF0 = v_rip + 2450199;
    v_stack_mF8 = result;
    goto loc_00BB8695;
loc_00BB8731:
loc_00BB873B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)) == (*(unsigned __int64 *)(result + 8) + 8)) goto loc_00BB876A;
    result = ViDeadlockSimilarNode(a1, (unsigned int)(v_stack_mD0), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) - 24, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)));
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_00BB873B;
    result = ViDeadlockCheckDuplicatesAmongChildren(*(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) - 24, v_stack_mC8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)));
    goto loc_00BB87E1;
loc_00BB876A:
    if ((*(unsigned __int16 *)(v_stack_mD8 + 4)) == 0) goto loc_00BB879A;
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) - 24) != 0) goto loc_00BB879A;
    a4 = 0;
    v_stack_mF8 = v_stack_m98;
    result = ViDeadlockAnalyze(a1, *(unsigned __int64 *)(result + 8), 1, a4);
    a3 = 0;
    if ((unsigned int)(result) != 0) goto loc_00BB87F1;
loc_00BB879A:
    goto loc_00BB880C;
loc_00BB87A4:
loc_00BB87AF:
    if ((*(unsigned __int64 *)(v_stack_mD8 + 24)) == (v_stack_mD8 + 24)) goto loc_00BB87FE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 24) - 40)) != 0) goto loc_00BB87AF;
    result = ViDeadlockSimilarNode(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD0))), *(unsigned __int64 *)(v_stack_mD8 + 24) - 40, v_stack_mD8 + 24);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_00BB87AF;
    result = ViDeadlockCheckDuplicatesAmongRoots(*(unsigned __int64 *)(v_stack_mD8 + 24) - 40, v_stack_mC8, a3, v_stack_mD8 + 24);
loc_00BB87E1:
    a3 = 0;
    if (*(unsigned __int64 *)(v_stack_mD8 + 24) - 40 != 0) goto loc_00BB88CB;
loc_00BB87F1:
    goto loc_00BB8993;
loc_00BB87FE:
    v_stack_mC0 = 1;
loc_00BB880C:
    v_stack_mB8 = 0;
    *(unsigned __int64 *)(v_stack_mB8 + 80) = 0;
    *(unsigned __int64 *)(v_stack_mB8 + 144) = 0;
    *(unsigned __int64 *)(v_stack_mB8 + 64) = 0;
    *(unsigned __int64 *)(v_stack_mB8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(v_stack_mB8 + 56) = v_stack_mD8;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4477379) + 32804))) << (3));
    *(unsigned int *)(v_stack_mB8 + 72) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_stack_mB8 + 8 + 8) = v_stack_mB8 + 8;
    *(unsigned __int64 *)(v_stack_mB8 + 8) = v_stack_mB8 + 8;
    *(unsigned __int64 *)(v_stack_mB8 + 24 + 8) = v_stack_mB8 + 24;
    *(unsigned __int64 *)(v_stack_mB8 + 24) = v_stack_mB8 + 24;
    a1 = (unsigned int)(((unsigned int)(v_stack_mD0) + (unsigned int)(v_stack_mD0) * 1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 72)))));
    a1 = (unsigned int)((a1) & (2));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB8 + 72)))));
    *(unsigned int *)(v_stack_mB8 + 72) = (unsigned int)(a1);
    if (v_stack_mC0 != 0) goto loc_00BB8894;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) + 8)) != (*(unsigned __int64 *)(result + 8) + 8)) goto loc_00BB88A1;
    *(unsigned __int64 *)(v_stack_mB8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8);
    *(unsigned __int64 *)(v_stack_mB8 + 24 + 8) = *(unsigned __int64 *)(result + 8) + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) + 8) = v_stack_mB8 + 24;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8) = v_stack_mB8 + 24;
    result = ViDeadlockUpdateChildrenCount(*(unsigned __int64 *)(result + 8), 1, a3, v_stack_mD8 + 24);
loc_00BB8894:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 24) + 8)) != (v_stack_mD8 + 24)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_stack_mB8 + 40) = *(unsigned __int64 *)(v_stack_mD8 + 24);
    *(unsigned __int64 *)(v_stack_mB8 + 40 + 8) = v_stack_mD8 + 24;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 24) + 8) = v_stack_mB8 + 40;
    *(unsigned __int64 *)(v_stack_mD8 + 24) = v_stack_mB8 + 40;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_mD8 + 4)))) >= = 0xFFF0ULL) {
    }
    result = (unsigned int)(((unsigned int)(v_stack_mAC)) + (-5));
    *(unsigned __int64 *)(v_stack_mB8 + 64) = result;
    if (((unsigned int)(result)) <= 1) goto loc_00BB88E4;
    *(unsigned __int64 *)(result + 16) = v_stack_mB8;
    goto loc_00BB88E8;
loc_00BB88E4:
    *(unsigned __int64 *)(result + 8) = v_stack_mB8;
loc_00BB88E8:
    if (*(unsigned __int64 *)(v_stack_mB8) != 0) {
        *(unsigned __int64 *)(v_stack_mB8 + 144) = v_xmm0;
        *(unsigned __int64 *)(v_stack_mB8 + 160) = v_xmm1;
        *(unsigned __int64 *)(v_stack_mB8 + 176) = v_xmm0;
        *(unsigned __int64 *)(v_stack_mB8 + 192) = v_xmm1;
    }
    *(unsigned __int64 *)(v_stack_mB8 + 80) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mB8 + 96) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mB8 + 112) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mB8 + 128) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 56) + 120) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 56) + 136) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 56) + 152) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 56) + 168) = v_xmm1;
    goto loc_00BB8597;
loc_00BB897B:
    goto loc_00BB8998;
loc_00BB8985:
loc_00BB898A:
loc_00BB898D:
loc_00BB8993:
loc_00BB8998:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 56))) - (*(unsigned __int64 *)(1));
    if (result >= = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4477012)))) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4477012)) = result;
    }
    result = ViDeadlockDetectionUnlock(1, *(unsigned __int64 *)(v_stack_mD8 + 24), a3, v_stack_mD8 + 24);
    result = ViLowerIrql(v_stack_mE4, *(unsigned __int64 *)(v_stack_mD8 + 24), a3, v_stack_mD8 + 24);
    if (v_stack_mC8 == 0) goto loc_00BB89E6;
loc_00BB89D1:
    result = ViDeadlockFree(v_stack_mC8, 2, a3, v_stack_mD8 + 24);
    if (*(unsigned __int64 *)(v_stack_mC8) != 0) goto loc_00BB89D1;
loc_00BB89E6:
    if (v_stack_mA0 != 0) {
        a2 = 1;
        result = ViDeadlockFree(v_stack_mA0, a2, a3, v_stack_mD8 + 24);
    }
    if (0 != 0) {
        a2 = 3;
        a1 = result;
        result = ViDeadlockFree(a1, a2, a3, v_stack_mD8 + 24);
    }
    result = v_stack_mB8;
    if (v_stack_mB8 != 0) {
        a2 = 2;
        a1 = v_stack_mB8;
        result = ViDeadlockFree(a1, a2, a3, v_stack_mD8 + 24);
    }
    if (v_stack_mD8 != 0) {
        a2 = 1;
        a1 = v_stack_mD8;
        result = ViDeadlockFree(a1, a2, a3, v_stack_mD8 + 24);
    }
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        a2 = 2;
        a1 = v_stack_mA8;
        result = ViDeadlockFree(a1, a2, a3, v_stack_mD8 + 24);
    }
    if (v_stack_mE0 != 0) {
        a2 = 3;
        a1 = v_stack_mE0;
        result = ViDeadlockFree(a1, a2, a3, v_stack_mD8 + 24);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_mD8 + 24);
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfDeadlockAcquireResource(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x252369)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    v_stack_mD0 = Arg4;
    v_stack_mAC = (uint32_t)((int32_t)(Arg2));
    v_stack_m98 = Arg5;
    result = memset(v_stack_m88, Arg2, Arg2 + 64, Arg4);
    local_r13 = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = 0;
    v_stack_mA0 = 0;
    v_stack_mC8 = 0;
    if (((uint32_t)((int32_t)(Arg2))) != 8) goto loc_00BB844C;
    if (*(uint64_t *)(v_rip + 0x445698) == 0) goto loc_00BB8A59;
    if ((*(uint64_t *)(v_rip + 0x445698)) > Arg5) goto loc_00BB8A59;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x4456AC))) + (*(uint64_t *)(v_rip + 0x445698));
    if (result <= Arg5) goto loc_00BB8A59;
loc_00BB844C:
    result = ViDeadlockCanProceed(Arg1, Arg2, Arg2 + 64, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00BB8A59;
    result = ViIsThreadInsidePagingCodePaths(Arg1, Arg2, Arg2 + 64, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00BB8A59;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x445590) + 0x8010))) != 0) goto loc_00BB8A59;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x44557B) + 0x8168)) > 0x400ULL) goto loc_00BB8A59;
    v_stack_mB8 = 0;
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2D3F4 + (int32_t)(Arg2) * 4)));
    result = ViDeadlockAllocate(3, Arg2, Arg2 + 64, Arg4);
    v_stack_mE0 = result;
    result = ViDeadlockAllocate(2, Arg2, Arg2 + 64, Arg4);
    v_stack_mA8 = result;
    result = ViDeadlockAllocate(1, Arg2, Arg2 + 64, Arg4);
    Arg4 = 0;
    v_stack_mD8 = result;
    result = RtlCaptureStackBackTrace(Arg4 + 8 - 6, Arg4 + 8, v_stack_m88, Arg4);
    if ((uint32_t)((uint16_t)(result)) != 0) goto loc_00BB84FD;
    v_stack_m88 = Arg5;
    goto loc_00BB8502;
loc_00BB84FD:
    if (1 < 8) {
        result = 1;
    }
    result = ViRaiseIrqlToDpcLevel(1, Arg4 + 8, v_stack_m88, Arg4);
    v_stack_mE4 = (uint8_t)(result);
    result = ViDeadlockDetectionLock(1, Arg4 + 8, v_stack_m88, Arg4);
    Arg3 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x445546))) == 0) goto loc_00BB8985;
    v_stack_mB8 = v_stack_mA8;
    v_stack_mA8 = 0;
    if (v_stack_mA8 == 0) goto loc_00BB8985;
    result = ViDeadlockSearchThread(0, Arg4 + 8, Arg3, Arg4);
    if (result != 0) goto loc_00BB8588;
    result = ViDeadlockAddThread(0, v_stack_mE0, Arg3, Arg4);
    v_stack_mE0 = 0;
    if (result == 0) goto loc_00BB897B;
    goto loc_00BB858E;
loc_00BB8588:
loc_00BB858E:
    if (((uint32_t)((int32_t)(Arg2))) != 8) goto loc_00BB85A5;
    *(uint8_t *)(result + 0x30) = 1;
loc_00BB8597:
    goto loc_00BB8993;
loc_00BB85A5:
    result = ViDeadlockSearchResource(Arg1, v_stack_mC8, Arg3, Arg4);
    Arg3 = 0;
    if (result != 0) goto loc_00BB8602;
    v_stack_mF0 = v_stack_mC8;
    v_stack_mF8 = v_stack_mA0;
    result = ViDeadlockAddResource(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_mE8))), v_stack_mD8, v_stack_m88);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_00BB863C;
    v_stack_mD8 = 0;
    result = ViDeadlockSearchResource(Arg1, v_stack_mC8, Arg3, v_stack_m88);
    Arg3 = 0;
loc_00BB8602:
    if (((uint32_t)((int32_t)(*(uint32_t *)(result)))) == ((uint32_t)((uint32_t)(v_stack_mE8)))) goto loc_00BB862E;
    if (((uint32_t)((uint32_t)(v_stack_mE8) - 3)) > 1) goto loc_00BB861F;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result)) - 3)) <= 1) goto loc_00BB862C;
loc_00BB861F:
    if (((uint32_t)((int32_t)(*(uint32_t *)(result)))) != 7) goto loc_00BB865C;
    if (((uint32_t)((uint32_t)(v_stack_mE8) - 5)) > 1) goto loc_00BB865C;
loc_00BB862C:
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_mE8));
loc_00BB862E:
    if (((uint32_t)((uint32_t)(v_stack_mE8) - 5)) <= 1) goto loc_00BB86B3;
    goto loc_00BB86B7;
loc_00BB863C:
    if (1 == 0) goto loc_00BB898A;
    Arg2 = 0;
    result = ViDeadlockRemoveThread(result, Arg2, Arg3, v_stack_m88);
    goto loc_00BB8993;
loc_00BB865C:
    v_stack_mF0 = *(uint64_t *)(result + 0x10);
    v_stack_mF8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2450372, v_rip + 10780, (uint32_t)((uint32_t)((uint32_t)(0x1008ULL))), Arg1);
    v_stack_mF0 = v_rip + 2450372;
    v_stack_mF8 = *(uint64_t *)(result + 0x10);
loc_00BB8695:
    result = VfReportIssueWithOptions(196, (uint32_t)(0x1008ULL), Arg1, (int32_t)(*(uint32_t *)(result)));
    goto loc_00BB898D;
loc_00BB86B3:
loc_00BB86B7:
    if (*(uint64_t *)(v_stack_mD8 + 0x10) == 0) goto loc_00BB86CA;
    if ((*(uint64_t *)(v_stack_mD8 + 0x10)) != result) {
        *(uint16_t *)(v_stack_mD8 + 0x6) = (uint16_t)(Arg1);
    }
    result = (uint16_t)((*(uint16_t *)(v_stack_mD8 + 0x6)) + (1));
    *(uint64_t *)(v_stack_mD8 + 0x10) = result;
    *(uint16_t *)(v_stack_mD8 + 0x6) = (uint16_t)(result);
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00BB87A4;
    if (((uint16_t)(result)) <= 1) goto loc_00BB8731;
    if (((v_stack_mB0) & (1)) != 0) goto loc_00BB8597;
    v_stack_mF0 = result;
    v_stack_mF8 = v_stack_mD8;
    result = ViDeadlockPreprocessOptions(v_rip + 2450199, v_rip + 10572, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), Arg1);
    v_stack_mF0 = v_rip + 2450199;
    v_stack_mF8 = result;
    goto loc_00BB8695;
loc_00BB8731:
loc_00BB873B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)) == (*(uint64_t *)(result + 0x8) + 8)) goto loc_00BB876A;
    result = ViDeadlockSimilarNode(Arg1, (uint32_t)(v_stack_mD0), *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) - 24, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)));
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_00BB873B;
    result = ViDeadlockCheckDuplicatesAmongChildren(*(uint64_t *)(result + 0x8), *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) - 24, v_stack_mC8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)));
    goto loc_00BB87E1;
loc_00BB876A:
    if ((*(uint16_t *)(v_stack_mD8 + 0x4)) == 0) goto loc_00BB879A;
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) - 24) != 0) goto loc_00BB879A;
    Arg4 = 0;
    v_stack_mF8 = v_stack_m98;
    result = ViDeadlockAnalyze(Arg1, *(uint64_t *)(result + 0x8), 1, Arg4);
    Arg3 = 0;
    if ((uint32_t)(result) != 0) goto loc_00BB87F1;
loc_00BB879A:
    goto loc_00BB880C;
loc_00BB87A4:
loc_00BB87AF:
    if ((*(uint64_t *)(v_stack_mD8 + 0x18)) == (v_stack_mD8 + 24)) goto loc_00BB87FE;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x18) - 0x28)) != 0) goto loc_00BB87AF;
    result = ViDeadlockSimilarNode(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD0))), *(uint64_t *)(v_stack_mD8 + 0x18) - 40, v_stack_mD8 + 24);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_00BB87AF;
    result = ViDeadlockCheckDuplicatesAmongRoots(*(uint64_t *)(v_stack_mD8 + 0x18) - 40, v_stack_mC8, Arg3, v_stack_mD8 + 24);
loc_00BB87E1:
    Arg3 = 0;
    if (*(uint64_t *)(v_stack_mD8 + 0x18) - 40 != 0) goto loc_00BB88CB;
loc_00BB87F1:
    goto loc_00BB8993;
loc_00BB87FE:
    v_stack_mC0 = 1;
loc_00BB880C:
    v_stack_mB8 = 0;
    *(uint64_t *)(v_stack_mB8 + 0x50) = 0;
    *(uint64_t *)(v_stack_mB8 + 0x90) = 0;
    *(uint64_t *)(v_stack_mB8 + 0x40) = 0;
    *(uint64_t *)(v_stack_mB8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(v_stack_mB8 + 0x38) = v_stack_mD8;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4451C3) + 0x8024))) << (3));
    *(uint32_t *)(v_stack_mB8 + 0x48) = (uint32_t)(Arg1);
    *(uint64_t *)(v_stack_mB8 + 0x8 + 0x8) = v_stack_mB8 + 8;
    *(uint64_t *)(v_stack_mB8 + 0x8) = v_stack_mB8 + 8;
    *(uint64_t *)(v_stack_mB8 + 0x18 + 0x8) = v_stack_mB8 + 24;
    *(uint64_t *)(v_stack_mB8 + 0x18) = v_stack_mB8 + 24;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mD0) + (uint32_t)(v_stack_mD0) * 1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x48)))));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x48)))));
    *(uint32_t *)(v_stack_mB8 + 0x48) = (uint32_t)(Arg1);
    if (v_stack_mC0 != 0) goto loc_00BB8894;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) + 0x8)) != (*(uint64_t *)(result + 0x8) + 8)) goto loc_00BB88A1;
    *(uint64_t *)(v_stack_mB8 + 0x18) = *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8);
    *(uint64_t *)(v_stack_mB8 + 0x18 + 0x8) = *(uint64_t *)(result + 0x8) + 8;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) + 0x8) = v_stack_mB8 + 24;
    *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8) = v_stack_mB8 + 24;
    result = ViDeadlockUpdateChildrenCount(*(uint64_t *)(result + 0x8), 1, Arg3, v_stack_mD8 + 24);
loc_00BB8894:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x18) + 0x8)) != (v_stack_mD8 + 24)) {
        Arg1 = 3;
    }
    *(uint64_t *)(v_stack_mB8 + 0x28) = *(uint64_t *)(v_stack_mD8 + 0x18);
    *(uint64_t *)(v_stack_mB8 + 0x28 + 0x8) = v_stack_mD8 + 24;
    *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x18) + 0x8) = v_stack_mB8 + 40;
    *(uint64_t *)(v_stack_mD8 + 0x18) = v_stack_mB8 + 40;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x4)))) >= = 0xFFF0ULL) {
    }
    result = (uint32_t)(((uint32_t)(v_stack_mAC)) + (-5));
    *(uint64_t *)(v_stack_mB8 + 0x40) = result;
    if (((uint32_t)(result)) <= 1) goto loc_00BB88E4;
    *(uint64_t *)(result + 0x10) = v_stack_mB8;
    goto loc_00BB88E8;
loc_00BB88E4:
    *(uint64_t *)(result + 0x8) = v_stack_mB8;
loc_00BB88E8:
    if (*(uint64_t *)(v_stack_mB8) != 0) {
        *(uint64_t *)(v_stack_mB8 + 0x90) = v_xmm0;
        *(uint64_t *)(v_stack_mB8 + 0xA0) = v_xmm1;
        *(uint64_t *)(v_stack_mB8 + 0xB0) = v_xmm0;
        *(uint64_t *)(v_stack_mB8 + 0xC0) = v_xmm1;
    }
    *(uint64_t *)(v_stack_mB8 + 0x50) = v_xmm0;
    *(uint64_t *)(v_stack_mB8 + 0x60) = v_xmm1;
    *(uint64_t *)(v_stack_mB8 + 0x70) = v_xmm0;
    *(uint64_t *)(v_stack_mB8 + 0x80) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x38) + 0x78) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x38) + 0x88) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x38) + 0x98) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x38) + 0xA8) = v_xmm1;
    goto loc_00BB8597;
loc_00BB897B:
    goto loc_00BB8998;
loc_00BB8985:
loc_00BB898A:
loc_00BB898D:
loc_00BB8993:
loc_00BB8998:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x38))) - (*(uint64_t *)(1));
    if (result >= = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x445054)))) {
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x445054)) = result;
    }
    result = ViDeadlockDetectionUnlock(1, *(uint64_t *)(v_stack_mD8 + 0x18), Arg3, v_stack_mD8 + 24);
    result = ViLowerIrql(v_stack_mE4, *(uint64_t *)(v_stack_mD8 + 0x18), Arg3, v_stack_mD8 + 24);
    if (v_stack_mC8 == 0) goto loc_00BB89E6;
loc_00BB89D1:
    result = ViDeadlockFree(v_stack_mC8, 2, Arg3, v_stack_mD8 + 24);
    if (*(uint64_t *)(v_stack_mC8) != 0) goto loc_00BB89D1;
loc_00BB89E6:
    if (v_stack_mA0 != 0) {
        Arg2 = 1;
        result = ViDeadlockFree(v_stack_mA0, Arg2, Arg3, v_stack_mD8 + 24);
    }
    if (0 != 0) {
        Arg2 = 3;
        Arg1 = result;
        result = ViDeadlockFree(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    }
    result = v_stack_mB8;
    if (v_stack_mB8 != 0) {
        Arg2 = 2;
        Arg1 = v_stack_mB8;
        result = ViDeadlockFree(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    }
    if (v_stack_mD8 != 0) {
        Arg2 = 1;
        Arg1 = v_stack_mD8;
        result = ViDeadlockFree(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    }
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        Arg2 = 2;
        Arg1 = v_stack_mA8;
        result = ViDeadlockFree(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    }
    if (v_stack_mE0 != 0) {
        Arg2 = 3;
        Arg1 = v_stack_mE0;
        result = ViDeadlockFree(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_mD8 + 24);
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB83B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
