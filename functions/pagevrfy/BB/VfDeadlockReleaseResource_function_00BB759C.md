# VfDeadlockReleaseResource

- RVA: `0x00BB759C`–`0x00BB7A66` (길이 `1,226` bytes)
- VA: `0x0000000140BB759C`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B50E4`
- 디코드: `307`개 명령, `1,226/1,226` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00BB75E3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00BB75F2` → [ViDeadlockCanProceed](ViDeadlockCanProceed_function_00BB7B84.md) (function, `0x00BB7B84`)
- `0x00BB75FF` → [ViIsThreadInsidePagingCodePaths](../BA/ViIsThreadInsidePagingCodePaths_function_00BAA2D4.md) (function, `0x00BAA2D4`)
- `0x00BB764B` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)
- `0x00BB7670` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (function, `0x006162B0`)
- `0x00BB7681` → [ViDeadlockDetectionLock](../BA/ViDeadlockDetectionLock_function_00BA91C4.md) (function, `0x00BA91C4`)
- `0x00BB76A9` → [ViDeadlockSearchResource](../BA/ViDeadlockSearchResource_function_00BAA0D0.md) (function, `0x00BAA0D0`)
- `0x00BB771C` → [ViDeadlockSearchThread](../BA/ViDeadlockSearchThread_function_00BAA1AC.md) (function, `0x00BAA1AC`)
- `0x00BB7747` → [ViDeadlockPreprocessOptions](../BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) (function, `0x00BA9BB4`)
- `0x00BB774F` → [ViDeadlockSearchThread](../BA/ViDeadlockSearchThread_function_00BAA1AC.md) (function, `0x00BAA1AC`)
- `0x00BB77AB` → [ViDeadlockPreprocessOptions](../BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) (function, `0x00BA9BB4`)
- `0x00BB77C8` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (function, `0x00614444`)
- `0x00BB784F` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00BB787A` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00BB78A8` → [ViDeadlockPreprocessOptions](../BA/ViDeadlockPreprocessOptions_function_00BA9BB4.md) (function, `0x00BA9BB4`)
- `0x00BB78D3` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (function, `0x00614444`)
- `0x00BB798D` → [ViDeadlockRemoveThread](../BA/ViDeadlockRemoveThread_function_00BA9F8C.md) (function, `0x00BA9F8C`)
- `0x00BB79FC` → [ViDeadlockDetectionUnlock](../BA/ViDeadlockDetectionUnlock_function_00BA91FC.md) (function, `0x00BA91FC`)
- `0x00BB7A04` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (function, `0x00616278`)
- `0x00BB7A1B` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB7A35` → [ViDeadlockFree](../BA/ViDeadlockFree_function_00BA9670.md) (function, `0x00BA9670`)
- `0x00BB7A45` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ViDeadlockExReleaseFastMutexUnsafe_Entry](../BA/ViDeadlockExReleaseFastMutexUnsafe_Entry_function_00BA94C0.md) at `0x00BA94D9`
- [ViDeadlockExReleaseFastMutex_Entry](../BA/ViDeadlockExReleaseFastMutex_Entry_function_00BA94F0.md) at `0x00BA9509`
- [ViDeadlockKeReleaseInStackQueuedSpinLockForDpc_Entry](../BA/ViDeadlockKeReleaseInStackQueuedSpinLockForDpc_Entry_function_00BA9770.md) at `0x00BA9794`
- [ViDeadlockKeReleaseMutant_Entry](../BA/ViDeadlockKeReleaseMutant_Entry_function_00BA97B0.md) at `0x00BA97CF`
- [ViDeadlockKeReleaseMutex_Entry](../BA/ViDeadlockKeReleaseMutex_Entry_function_00BA97E0.md) at `0x00BA97F9`
- [ViDeadlockKeReleaseSpinLockFromDpcLevel_Entry](../BA/ViDeadlockKeReleaseSpinLockFromDpcLevel_Entry_function_00BA9810.md) at `0x00BA9829`
- [ViDeadlockKeReleaseSpinLock_Entry](ViDeadlockKeReleaseSpinLock_Entry_function_00BB7570.md) at `0x00BB7589`

### Static image references
- `0x00BB75B3` → RVA `0x00E0A740` (`.data`; read)
- `0x00BB760C` → RVA `0x00FFDA00` (`PAGEVRFD`; read)
- `0x00BB7693` → RVA `0x00FFDA78` (`PAGEVRFD`; read)
- `0x00BB7726` → RVA `0x00E0EA20` (`.data`; read)
- `0x00BB773A` → RVA `0x00BBB0D0` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB778F` → RVA `0x00E0EA24` (`.data`; read)
- `0x00BB779E` → RVA `0x00BBB110` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB781C` → RVA `0x00B8B0A8` (`ViDeadlockResourceTypeInfo`; read)
- `0x00BB7843` → RVA `0x00BBAFB0` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB7858` → RVA `0x00BBAF50` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB7883` → RVA `0x00BBB020` (` ?? ::JKADOLAD::`string'`; read)
- `0x00BB788F` → RVA `0x00E0EA34` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00BB75E3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGEVRFY` → `.text`)
  - `0x00BB764B` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB7670` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB77C8` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (`PAGEVRFY` → `.text`)
  - `0x00BB784F` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGEVRFY` → `.text`)
  - `0x00BB787A` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGEVRFY` → `.text`)
  - `0x00BB78D3` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (`PAGEVRFY` → `.text`)
  - `0x00BB7A04` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (`PAGEVRFY` → `.text`)
  - `0x00BB7A45` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB759C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00BB75A1  55                              push rbp
00BB75A2  56                              push rsi
00BB75A3  57                              push rdi
00BB75A4  41 54                           push r12
00BB75A6  41 55                           push r13
00BB75A8  41 56                           push r14
00BB75AA  41 57                           push r15
00BB75AC  48 81 EC A0 00 00 00            sub rsp, 0xa0
00BB75B3  48 8B 05 86 31 25 00            mov rax, qword ptr [rip + 0x253186]
00BB75BA  48 33 C4                        xor rax, rsp
00BB75BD  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00BB75C5  33 F6                           xor esi, esi
00BB75C7  48 63 FA                        movsxd rdi, edx
00BB75CA  4D 8B E8                        mov r13, r8
00BB75CD  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00BB75D2  4C 8B F9                        mov r15, rcx
00BB75D5  33 D2                           xor edx, edx
00BB75D7  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00BB75DC  49 8B D9                        mov rbx, r9
00BB75DF  44 8D 46 40                     lea r8d, [rsi + 0x40]
00BB75E3  E8 58 F6 B0 FF                  call 0x1406c6c40
00BB75E8  49 8B CF                        mov rcx, r15
00BB75EB  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
00BB75EF  44 8B E6                        mov r12d, esi
00BB75F2  E8 8D 05 00 00                  call 0x140bb7b84
00BB75F7  85 C0                           test eax, eax
00BB75F9  0F 84 3B 04 00 00               je 0x140bb7a3a
00BB75FF  E8 D0 2C FF FF                  call 0x140baa2d4
00BB7604  85 C0                           test eax, eax
00BB7606  0F 85 2E 04 00 00               jne 0x140bb7a3a
00BB760C  48 8B 05 ED 63 44 00            mov rax, qword ptr [rip + 0x4463ed]
00BB7613  8B 88 10 80 00 00               mov ecx, dword ptr [rax + 0x8010]
00BB7619  85 C9                           test ecx, ecx
00BB761B  0F 85 19 04 00 00               jne 0x140bb7a3a
00BB7621  48 8B 05 D8 63 44 00            mov rax, qword ptr [rip + 0x4463d8]
00BB7628  81 B8 68 81 00 00 00 04 00 00   cmp dword ptr [rax + 0x8168], 0x400
00BB7632  0F 8F 02 04 00 00               jg 0x140bb7a3a
00BB7638  45 33 C9                        xor r9d, r9d
00BB763B  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00BB7640  8D 56 08                        lea edx, [rsi + 8]
00BB7643  8B EE                           mov ebp, esi
00BB7645  8D 4E 02                        lea ecx, [rsi + 2]
00BB7648  44 8B F6                        mov r14d, esi
00BB764B  E8 A0 29 74 FF                  call 0x1402f9ff0
00BB7650  0F B7 C8                        movzx ecx, ax
00BB7653  66 85 C9                        test cx, cx
00BB7656  75 05                           jne 0x140bb765d
00BB7658  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00BB765D  66 85 C9                        test cx, cx
00BB7660  8D 41 01                        lea eax, [rcx + 1]
00BB7663  0F 45 C1                        cmovne eax, ecx
00BB7666  83 F8 08                        cmp eax, 8
00BB7669  73 05                           jae 0x140bb7670
00BB766B  48 89 74 C4 50                  mov qword ptr [rsp + rax*8 + 0x50], rsi
00BB7670  E8 3B EC A5 FF                  call 0x1406162b0
00BB7675  B9 01 00 00 00                  mov ecx, 1
00BB767A  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00BB767E  40 8A F0                        mov sil, al
00BB7681  E8 3E 1B FF FF                  call 0x140ba91c4
00BB7686  48 B9 20 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000320
00BB7690  48 8B 19                        mov rbx, qword ptr [rcx]
00BB7693  8B 0D DF 63 44 00               mov ecx, dword ptr [rip + 0x4463df]
00BB7699  85 C9                           test ecx, ecx
00BB769B  0F 84 35 03 00 00               je 0x140bb79d6
00BB76A1  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00BB76A6  49 8B CF                        mov rcx, r15
00BB76A9  E8 22 2A FF FF                  call 0x140baa0d0
00BB76AE  33 D2                           xor edx, edx
00BB76B0  48 8B F0                        mov rsi, rax
00BB76B3  48 85 C0                        test rax, rax
00BB76B6  0F 84 15 03 00 00               je 0x140bb79d1
00BB76BC  48 63 00                        movsxd rax, dword ptr [rax]
00BB76BF  44 8D 42 01                     lea r8d, [rdx + 1]
00BB76C3  3B C7                           cmp eax, edi
00BB76C5  74 19                           je 0x140bb76e0
00BB76C7  83 F8 07                        cmp eax, 7
00BB76CA  0F 85 95 00 00 00               jne 0x140bb7765
00BB76D0  8D 4F FB                        lea ecx, [rdi - 5]
00BB76D3  41 3B C8                        cmp ecx, r8d
00BB76D6  0F 87 A8 00 00 00               ja 0x140bb7784
00BB76DC  89 3E                           mov dword ptr [rsi], edi
00BB76DE  8B C7                           mov eax, edi
00BB76E0  0F B7 4E 06                     movzx ecx, word ptr [rsi + 6]
00BB76E4  66 85 C9                        test cx, cx
00BB76E7  0F 85 E5 00 00 00               jne 0x140bb77d2
00BB76ED  48 8B 05 0C 63 44 00            mov rax, qword ptr [rip + 0x44630c]
00BB76F4  8B 88 10 80 00 00               mov ecx, dword ptr [rax + 0x8010]
00BB76FA  85 C9                           test ecx, ecx
00BB76FC  0F 85 9C 02 00 00               jne 0x140bb799e
00BB7702  48 8B 05 F7 62 44 00            mov rax, qword ptr [rip + 0x4462f7]
00BB7709  81 B8 68 81 00 00 00 04 00 00   cmp dword ptr [rax + 0x8168], 0x400
00BB7713  0F 8F 85 02 00 00               jg 0x140bb799e
00BB7719  49 8B CD                        mov rcx, r13
00BB771C  E8 8B 2A FF FF                  call 0x140baa1ac
00BB7721  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BB7726  48 8D 3D F3 72 25 00            lea rdi, [rip + 0x2572f3]
00BB772D  BD 07 10 00 00                  mov ebp, 0x1007
00BB7732  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00BB7737  44 8B C5                        mov r8d, ebp
00BB773A  48 8D 15 8F 39 00 00            lea rdx, [rip + 0x398f]
00BB7741  48 8B CF                        mov rcx, rdi
00BB7744  4D 8B CF                        mov r9, r15
00BB7747  E8 68 24 FF FF                  call 0x140ba9bb4
00BB774C  49 8B CD                        mov rcx, r13
00BB774F  E8 58 2A FF FF                  call 0x140baa1ac
00BB7754  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00BB7759  4C 8B CE                        mov r9, rsi
00BB775C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB7761  8B D5                           mov edx, ebp
00BB7763  EB 5B                           jmp 0x140bb77c0
00BB7765  41 3B C0                        cmp eax, r8d
00BB7768  75 1A                           jne 0x140bb7784
00BB776A  83 FF 02                        cmp edi, 2
00BB776D  75 15                           jne 0x140bb7784
00BB776F  66 44 39 46 06                  cmp word ptr [rsi + 6], r8w
00BB7774  0F 86 66 FF FF FF               jbe 0x140bb76e0
00BB777A  66 44 89 46 06                  mov word ptr [rsi + 6], r8w
00BB777F  E9 5C FF FF FF                  jmp 0x140bb76e0
00BB7784  41 BD 09 10 00 00               mov r13d, 0x1009
00BB778A  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00BB778F  48 8D 2D 8E 72 25 00            lea rbp, [rip + 0x25728e]
00BB7796  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB779B  45 8B C5                        mov r8d, r13d
00BB779E  48 8D 15 6B 39 00 00            lea rdx, [rip + 0x396b]
00BB77A5  48 8B CD                        mov rcx, rbp
00BB77A8  4D 8B CF                        mov r9, r15
00BB77AB  E8 04 24 FF FF                  call 0x140ba9bb4
00BB77B0  4C 63 0E                        movsxd r9, dword ptr [rsi]
00BB77B3  41 8B D5                        mov edx, r13d
00BB77B6  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00BB77BB  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00BB77C0  4D 8B C7                        mov r8, r15
00BB77C3  B9 C4 00 00 00                  mov ecx, 0xc4
00BB77C8  E8 77 CC A5 FF                  call 0x140614444
00BB77CD  E9 CC 01 00 00                  jmp 0x140bb799e
00BB77D2  4C 8B 76 10                     mov r14, qword ptr [rsi + 0x10]
00BB77D6  83 C0 FB                        add eax, -5
00BB77D9  4D 8B 26                        mov r12, qword ptr [r14]
00BB77DC  41 3B C0                        cmp eax, r8d
00BB77DF  76 06                           jbe 0x140bb77e7
00BB77E1  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
00BB77E5  EB 04                           jmp 0x140bb77eb
00BB77E7  49 8B 7E 08                     mov rdi, qword ptr [r14 + 8]
00BB77EB  66 41 2B C8                     sub cx, r8w
00BB77EF  66 89 4E 06                     mov word ptr [rsi + 6], cx
00BB77F3  0F 85 9B 01 00 00               jne 0x140bb7994
00BB77F9  48 8B 05 00 62 44 00            mov rax, qword ptr [rip + 0x446200]
00BB7800  48 89 56 10                     mov qword ptr [rsi + 0x10], rdx
00BB7804  44 01 80 48 80 00 00            add dword ptr [rax + 0x8048], r8d
00BB780B  48 39 77 38                     cmp qword ptr [rdi + 0x38], rsi
00BB780F  0F 84 FD 00 00 00               je 0x140bb7912
00BB7815  44 01 80 40 80 00 00            add dword ptr [rax + 0x8040], r8d
00BB781C  48 8D 0D 85 38 FD FF            lea rcx, [rip - 0x2c77b]
00BB7823  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00BB7827  48 63 00                        movsxd rax, dword ptr [rax]
00BB782A  8B 04 81                        mov eax, dword ptr [rcx + rax*4]
00BB782D  A8 04                           test al, 4
00BB782F  0F 85 A9 00 00 00               jne 0x140bb78de
00BB7835  48 63 06                        movsxd rax, dword ptr [rsi]
00BB7838  8B 04 81                        mov eax, dword ptr [rcx + rax*4]
00BB783B  A8 04                           test al, 4
00BB783D  0F 85 9B 00 00 00               jne 0x140bb78de
00BB7843  4C 8D 05 66 37 00 00            lea r8, [rip + 0x3766]
00BB784A  B9 5D 00 00 00                  mov ecx, 0x5d
00BB784F  E8 3C 1A 7A FF                  call 0x140359290
00BB7854  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00BB7858  4C 8D 05 F1 36 00 00            lea r8, [rip + 0x36f1]
00BB785F  33 D2                           xor edx, edx
00BB7861  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00BB7866  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00BB786B  4D 8B CF                        mov r9, r15
00BB786E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00BB7872  8D 4A 5D                        lea ecx, [rdx + 0x5d]
00BB7875  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB787A  E8 11 1A 7A FF                  call 0x140359290
00BB787F  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00BB7883  48 8D 15 96 37 00 00            lea rdx, [rip + 0x3796]
00BB788A  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00BB788F  48 8D 0D 9E 71 25 00            lea rcx, [rip + 0x25719e]
00BB7896  4D 8B CF                        mov r9, r15
00BB7899  41 B8 03 10 00 00               mov r8d, 0x1003
00BB789F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00BB78A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB78A8  E8 07 23 FF FF                  call 0x140ba9bb4
00BB78AD  4C 8B 4F 38                     mov r9, qword ptr [rdi + 0x38]
00BB78B1  48 8D 05 7C 71 25 00            lea rax, [rip + 0x25717c]
00BB78B8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BB78BD  4D 8B C7                        mov r8, r15
00BB78C0  BA 03 10 00 00                  mov edx, 0x1003
00BB78C5  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00BB78CA  B9 C4 00 00 00                  mov ecx, 0xc4
00BB78CF  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
00BB78D3  E8 6C CB A5 FF                  call 0x140614444
00BB78D8  33 D2                           xor edx, edx
00BB78DA  44 8D 42 01                     lea r8d, [rdx + 1]
00BB78DE  48 85 FF                        test rdi, rdi
00BB78E1  74 36                           je 0x140bb7919
00BB78E3  48 39 77 38                     cmp qword ptr [rdi + 0x38], rsi
00BB78E7  74 05                           je 0x140bb78ee
00BB78E9  48 8B 3F                        mov rdi, qword ptr [rdi]
00BB78EC  EB F0                           jmp 0x140bb78de
00BB78EE  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00BB78F1  48 8B EF                        mov rbp, rdi
00BB78F4  83 E0 FE                        and eax, 0xfffffffe
00BB78F7  89 47 48                        mov dword ptr [rdi + 0x48], eax
00BB78FA  A8 04                           test al, 4
00BB78FC  75 0E                           jne 0x140bb790c
00BB78FE  48 8B 05 FB 60 44 00            mov rax, qword ptr [rip + 0x4460fb]
00BB7905  44 01 80 44 80 00 00            add dword ptr [rax + 0x8044], r8d
00BB790C  83 4F 48 04                     or dword ptr [rdi + 0x48], 4
00BB7910  EB 07                           jmp 0x140bb7919
00BB7912  83 67 48 FE                     and dword ptr [rdi + 0x48], 0xfffffffe
00BB7916  48 8B EF                        mov rbp, rdi
00BB7919  8B 06                           mov eax, dword ptr [rsi]
00BB791B  83 E8 05                        sub eax, 5
00BB791E  41 3B C0                        cmp eax, r8d
00BB7921  76 20                           jbe 0x140bb7943
00BB7923  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00BB7927  48 85 C9                        test rcx, rcx
00BB792A  74 3D                           je 0x140bb7969
00BB792C  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
00BB792F  41 84 C0                        test r8b, al
00BB7932  74 06                           je 0x140bb793a
00BB7934  4C 39 71 40                     cmp qword ptr [rcx + 0x40], r14
00BB7938  74 2F                           je 0x140bb7969
00BB793A  48 8B 01                        mov rax, qword ptr [rcx]
00BB793D  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00BB7941  EB E0                           jmp 0x140bb7923
00BB7943  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00BB7947  48 85 C9                        test rcx, rcx
00BB794A  74 1D                           je 0x140bb7969
00BB794C  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
00BB794F  41 84 C0                        test r8b, al
00BB7952  74 06                           je 0x140bb795a
00BB7954  4C 39 71 40                     cmp qword ptr [rcx + 0x40], r14
00BB7958  74 0F                           je 0x140bb7969
00BB795A  48 8B 01                        mov rax, qword ptr [rcx]
00BB795D  49 89 46 08                     mov qword ptr [r14 + 8], rax
00BB7961  48 8B C8                        mov rcx, rax
00BB7964  48 85 C0                        test rax, rax
00BB7967  75 E3                           jne 0x140bb794c
00BB7969  48 85 ED                        test rbp, rbp
00BB796C  74 2B                           je 0x140bb7999
00BB796E  48 89 55 40                     mov qword ptr [rbp + 0x40], rdx
00BB7972  45 29 46 28                     sub dword ptr [r14 + 0x28], r8d
00BB7976  4D 3B E5                        cmp r12, r13
00BB7979  74 04                           je 0x140bb797f
00BB797B  83 4D 48 04                     or dword ptr [rbp + 0x48], 4
00BB797F  41 39 56 28                     cmp dword ptr [r14 + 0x28], edx
00BB7983  75 14                           jne 0x140bb7999
00BB7985  33 D2                           xor edx, edx
00BB7987  49 8B CE                        mov rcx, r14
00BB798A  45 8B E0                        mov r12d, r8d
00BB798D  E8 FA 25 FF FF                  call 0x140ba9f8c
00BB7992  EB 0A                           jmp 0x140bb799e
00BB7994  44 8B E2                        mov r12d, edx
00BB7997  EB 05                           jmp 0x140bb799e
00BB7999  44 8B 64 24 44                  mov r12d, dword ptr [rsp + 0x44]
00BB799E  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
00BB79A3  0F 11 86 B8 00 00 00            movups xmmword ptr [rsi + 0xb8], xmm0
00BB79AA  0F 28 4C 24 60                  movaps xmm1, xmmword ptr [rsp + 0x60]
00BB79AF  0F 11 8E C8 00 00 00            movups xmmword ptr [rsi + 0xc8], xmm1
00BB79B6  0F 28 44 24 70                  movaps xmm0, xmmword ptr [rsp + 0x70]
00BB79BB  0F 11 86 D8 00 00 00            movups xmmword ptr [rsi + 0xd8], xmm0
00BB79C2  0F 28 8C 24 80 00 00 00         movaps xmm1, xmmword ptr [rsp + 0x80]
00BB79CA  0F 11 8E E8 00 00 00            movups xmmword ptr [rsi + 0xe8], xmm1
00BB79D1  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
00BB79D6  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00BB79E0  48 8B 00                        mov rax, qword ptr [rax]
00BB79E3  48 8B 15 16 60 44 00            mov rdx, qword ptr [rip + 0x446016]
00BB79EA  48 2B C3                        sub rax, rbx
00BB79ED  48 3B 42 08                     cmp rax, qword ptr [rdx + 8]
00BB79F1  7E 04                           jle 0x140bb79f7
00BB79F3  48 89 42 08                     mov qword ptr [rdx + 8], rax
00BB79F7  B9 01 00 00 00                  mov ecx, 1
00BB79FC  E8 FB 17 FF FF                  call 0x140ba91fc
00BB7A01  40 8A CE                        mov cl, sil
00BB7A04  E8 6F E8 A5 FF                  call 0x140616278
00BB7A09  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00BB7A0E  48 85 C9                        test rcx, rcx
00BB7A11  74 15                           je 0x140bb7a28
00BB7A13  48 8B 19                        mov rbx, qword ptr [rcx]
00BB7A16  BA 02 00 00 00                  mov edx, 2
00BB7A1B  E8 50 1C FF FF                  call 0x140ba9670
00BB7A20  48 8B CB                        mov rcx, rbx
00BB7A23  48 85 DB                        test rbx, rbx
00BB7A26  75 EB                           jne 0x140bb7a13
00BB7A28  45 85 E4                        test r12d, r12d
00BB7A2B  74 0D                           je 0x140bb7a3a
00BB7A2D  BA 03 00 00 00                  mov edx, 3
00BB7A32  49 8B CE                        mov rcx, r14
00BB7A35  E8 36 1C FF FF                  call 0x140ba9670
00BB7A3A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00BB7A42  48 33 CC                        xor rcx, rsp
00BB7A45  E8 F6 4B AF FF                  call 0x1406ac640
00BB7A4A  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00BB7A52  48 81 C4 A0 00 00 00            add rsp, 0xa0
00BB7A59  41 5F                           pop r15
00BB7A5B  41 5E                           pop r14
00BB7A5D  41 5D                           pop r13
00BB7A5F  41 5C                           pop r12
00BB7A61  5F                              pop rdi
00BB7A62  5E                              pop rsi
00BB7A63  5D                              pop rbp
00BB7A64  C3                              ret
00BB7A65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfDeadlockReleaseResource(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 2437510)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m90 = 0;
    a2 = 0;
    result = memset(v_stack_m88, a2, v_rsi + 64, a4);
    v_stack_m94 = 0;
    result = ViDeadlockCanProceed(a1, a2, v_rsi + 64, a4);
    if ((unsigned int)(result) == 0) goto loc_00BB7A3A;
    result = ViIsThreadInsidePagingCodePaths(a1, a2, v_rsi + 64, a4);
    if ((unsigned int)(result) != 0) goto loc_00BB7A3A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4482029) + 32784))) != 0) goto loc_00BB7A3A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4482008) + 33128)) > 0x400ULL) goto loc_00BB7A3A;
    a4 = 0;
    result = RtlCaptureStackBackTrace(v_rsi + 2, v_rsi + 8, v_stack_m88, a4);
    if ((unsigned __int16)((unsigned __int16)(result)) == 0) {
        v_stack_m88 = 0;
    }
    result = (unsigned __int16)(result) + 1;
    if ((unsigned __int16)((unsigned __int16)(result)) != 0) { result = (unsigned int)((unsigned __int16)(result)); }
    if (((unsigned int)(result)) < 8) {
        *(unsigned __int64 *)(v_rsp + result * 8 + 80) = 0;
    }
    result = ViRaiseIrqlToDpcLevel((unsigned __int16)(result), v_rsi + 8, v_stack_m88, a4);
    v_stack_m98 = (unsigned __int8)(result);
    result = ViDeadlockDetectionLock(1, v_rsi + 8, v_stack_m88, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4482015))) == 0) goto loc_00BB79D6;
    result = ViDeadlockSearchResource(a1, v_stack_m90, v_stack_m88, a4);
    a2 = 0;
    if (result == 0) goto loc_00BB79D1;
    if (((unsigned int)((int)(*(unsigned int *)(result)))) == ((unsigned int)((int)(a2)))) goto loc_00BB76E0;
    if (((unsigned int)((int)(*(unsigned int *)(result)))) != 7) goto loc_00BB7765;
    if (((unsigned int)((int)(a2) - 5)) > ((unsigned int)(a2 + 1))) goto loc_00BB7784;
    *(unsigned int *)(result) = (unsigned int)((int)(a2));
loc_00BB76E0:
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 6)) != 0) goto loc_00BB77D2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4481804) + 32784))) != 0) goto loc_00BB799E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4481783) + 33128)) > 0x400ULL) goto loc_00BB799E;
    result = ViDeadlockSearchThread(a3, a2, a2 + 1, a4);
    v_stack_mB0 = result;
    v_stack_mB8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2454259, v_rip + 14735, (unsigned int)((unsigned int)((unsigned int)(0x1007ULL))), a1);
    result = ViDeadlockSearchThread(a3, v_rip + 14735, (unsigned int)((unsigned int)((unsigned int)(0x1007ULL))), a1);
    v_stack_mB0 = v_rip + 2454259;
    v_stack_mB8 = result;
    goto loc_00BB77C0;
loc_00BB7765:
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x1007ULL)))))) goto loc_00BB7784;
    if (((unsigned int)(v_rip + 2454259)) != 2) goto loc_00BB7784;
    if ((*(unsigned __int16 *)(result + 6)) <= ((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(0x1007ULL)))))) goto loc_00BB76E0;
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(0x1007ULL))));
    goto loc_00BB76E0;
loc_00BB7784:
    v_stack_mB0 = v_rip + 2454259;
    v_stack_mB8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2454158, v_rip + 14699, (unsigned int)((unsigned int)((unsigned int)(0x1009ULL))), a1);
    v_stack_mB0 = v_rip + 2454158;
    v_stack_mB8 = v_rip + 2454259;
loc_00BB77C0:
    result = VfReportIssueWithOptions(196, (unsigned int)((unsigned int)((unsigned int)(0x1009ULL))), a1, (int)(*(unsigned int *)(result)));
    goto loc_00BB799E;
loc_00BB77D2:
    result = (unsigned int)((result) + (-5));
    if (((unsigned int)(result)) <= ((unsigned int)(a1))) goto loc_00BB77E7;
    goto loc_00BB77EB;
loc_00BB77E7:
loc_00BB77EB:
    a1 = (unsigned __int16)((196) - ((unsigned __int16)(a1)));
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(a1);
    if (condition_is_not_equal) goto loc_00BB7994;
    *(unsigned __int64 *)(result + 16) = (unsigned int)((unsigned int)((unsigned int)(0x1009ULL)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56)) == result) goto loc_00BB7912;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 182139 + (int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56))) * 4)))) & (4)) != 0) goto loc_00BB78DE;
    result = (unsigned int)(*(unsigned int *)(v_rip - 182139 + (int)(*(unsigned int *)(result)) * 4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 182139 + (int)(*(unsigned int *)(result)) * 4)))) & (4)) == 0) {
        a3 = v_rip + 14182;
        a1 = 93;
        result = DbgPrintEx(a1, (unsigned int)((unsigned int)((unsigned int)(0x1009ULL))), a3, (int)(*(unsigned int *)(result)));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56);
        a3 = v_rip + 14065;
        a2 = 0;
        v_stack_mA8 = a1;
        v_stack_mB0 = *(unsigned __int64 *)(result + 16);
        a4 = a1;
        result = *(unsigned __int64 *)(result + 8);
        a1 = a2 + 93;
        v_stack_mB8 = result;
        result = DbgPrintEx(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56);
        a2 = v_rip + 14230;
        v_stack_mB0 = *(unsigned __int64 *)(result + 16);
        a1 = v_rip + 2453918;
        a4 = a1;
        a3 = 0x1003ULL;
        result = *(unsigned __int64 *)(result + 8);
        v_stack_mB8 = result;
        result = ViDeadlockPreprocessOptions(a1, a2, a3, a4);
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56);
        result = v_rip + 2453884;
        v_stack_mB0 = result;
        a3 = a1;
        a2 = 0x1003ULL;
        v_stack_mB8 = *(unsigned __int64 *)(result + 16);
        a1 = 196;
        a4 = *(unsigned __int64 *)(a4 + 8);
        result = VfReportIssueWithOptions(a1, a2, a3, a4);
        a2 = 0;
        a3 = a2 + 1;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) == 0) goto loc_00BB7919;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 56)) == result) goto loc_00BB78EE;
    goto loc_00BB78DE;
loc_00BB78EE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) + 72))) & (0xFFFFFFFEULL));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) + 72) = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (4)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 4481275);
    }
    goto loc_00BB7919;
loc_00BB7912:
loc_00BB7919:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - (5));
    if (((unsigned int)(result)) <= ((unsigned int)(a3))) goto loc_00BB7943;
loc_00BB7923:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16) == 0) goto loc_00BB7969;
    if ((((unsigned __int8)(a3)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16) + 72))))) == 0) goto loc_00BB793A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16) + 64)) == (*(unsigned __int64 *)(result + 16))) goto loc_00BB7969;
loc_00BB793A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16));
    goto loc_00BB7923;
loc_00BB7943:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) == 0) goto loc_00BB7969;
loc_00BB794C:
    if ((((unsigned __int8)(a3)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 72))))) == 0) goto loc_00BB795A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) + 64)) == (*(unsigned __int64 *)(result + 16))) goto loc_00BB7969;
loc_00BB795A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != 0) goto loc_00BB794C;
loc_00BB7969:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) == 0) goto loc_00BB7999;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) + 64) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16))) != ((unsigned int)(0x1009ULL))) {
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 40)) != 0) goto loc_00BB7999;
    a2 = 0;
    result = ViDeadlockRemoveThread(*(unsigned __int64 *)(result + 16), a2, a3, a4);
    goto loc_00BB799E;
loc_00BB7994:
    goto loc_00BB799E;
loc_00BB7999:
loc_00BB799E:
    *(unsigned __int64 *)(result + 184) = v_xmm0;
    *(unsigned __int64 *)(result + 200) = v_xmm1;
    *(unsigned __int64 *)(result + 216) = v_xmm0;
    *(unsigned __int64 *)(result + 232) = v_xmm1;
loc_00BB79D1:
loc_00BB79D6:
    result = (*(unsigned __int64 *)(result)) - (*(unsigned __int64 *)(1));
    if (result >= = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4481046) + 8))) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4481046) + 8) = result;
    }
    result = ViDeadlockDetectionUnlock(1, *(unsigned __int64 *)(v_rip + 4481046), a3, a4);
    result = ViLowerIrql((unsigned __int8)(v_stack_m98), *(unsigned __int64 *)(v_rip + 4481046), a3, a4);
    if (v_stack_m90 == 0) goto loc_00BB7A28;
loc_00BB7A13:
    result = ViDeadlockFree(v_stack_m90, 2, a3, a4);
    if (*(unsigned __int64 *)(v_stack_m90) != 0) goto loc_00BB7A13;
loc_00BB7A28:
    if ((unsigned int)((unsigned int)(v_stack_m94)) != 0) {
        a2 = 3;
        a1 = *(unsigned __int64 *)(result + 16);
        result = ViDeadlockFree(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfDeadlockReleaseResource(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x253186)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m90 = 0;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, local_rsi + 64, Arg4);
    v_stack_m94 = 0;
    result = ViDeadlockCanProceed(Arg1, Arg2, local_rsi + 64, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00BB7A3A;
    result = ViIsThreadInsidePagingCodePaths(Arg1, Arg2, local_rsi + 64, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00BB7A3A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4463ED) + 0x8010))) != 0) goto loc_00BB7A3A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x4463D8) + 0x8168)) > 0x400ULL) goto loc_00BB7A3A;
    Arg4 = 0;
    result = RtlCaptureStackBackTrace(local_rsi + 2, local_rsi + 8, v_stack_m88, Arg4);
    if ((uint16_t)((uint16_t)(result)) == 0) {
        v_stack_m88 = 0;
    }
    result = (uint16_t)(result) + 1;
    if ((uint16_t)((uint16_t)(result)) != 0) { result = (uint32_t)((uint16_t)(result)); }
    if (((uint32_t)(result)) < 8) {
        *(uint64_t *)(local_rsp + result * 8 + 0x50) = 0;
    }
    result = ViRaiseIrqlToDpcLevel((uint16_t)(result), local_rsi + 8, v_stack_m88, Arg4);
    v_stack_m98 = (uint8_t)(result);
    result = ViDeadlockDetectionLock(1, local_rsi + 8, v_stack_m88, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4463DF))) == 0) goto loc_00BB79D6;
    result = ViDeadlockSearchResource(Arg1, v_stack_m90, v_stack_m88, Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_00BB79D1;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result)))) == ((uint32_t)((int32_t)(Arg2)))) goto loc_00BB76E0;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result)))) != 7) goto loc_00BB7765;
    if (((uint32_t)((int32_t)(Arg2) - 5)) > ((uint32_t)(Arg2 + 1))) goto loc_00BB7784;
    *(uint32_t *)(result) = (uint32_t)((int32_t)(Arg2));
loc_00BB76E0:
    if ((uint16_t)(*(uint16_t *)(result + 0x6)) != 0) goto loc_00BB77D2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x44630C) + 0x8010))) != 0) goto loc_00BB799E;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x4462F7) + 0x8168)) > 0x400ULL) goto loc_00BB799E;
    result = ViDeadlockSearchThread(Arg3, Arg2, Arg2 + 1, Arg4);
    v_stack_mB0 = result;
    v_stack_mB8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2454259, v_rip + 14735, (uint32_t)((uint32_t)((uint32_t)(0x1007ULL))), Arg1);
    result = ViDeadlockSearchThread(Arg3, v_rip + 14735, (uint32_t)((uint32_t)((uint32_t)(0x1007ULL))), Arg1);
    v_stack_mB0 = v_rip + 2454259;
    v_stack_mB8 = result;
    goto loc_00BB77C0;
loc_00BB7765:
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x1007ULL)))))) goto loc_00BB7784;
    if (((uint32_t)(v_rip + 2454259)) != 2) goto loc_00BB7784;
    if ((*(uint16_t *)(result + 0x6)) <= ((uint16_t)((uint32_t)((uint32_t)((uint32_t)(0x1007ULL)))))) goto loc_00BB76E0;
    *(uint16_t *)(result + 0x6) = (uint16_t)((uint32_t)((uint32_t)((uint32_t)(0x1007ULL))));
    goto loc_00BB76E0;
loc_00BB7784:
    v_stack_mB0 = v_rip + 2454259;
    v_stack_mB8 = result;
    result = ViDeadlockPreprocessOptions(v_rip + 2454158, v_rip + 14699, (uint32_t)((uint32_t)((uint32_t)(0x1009ULL))), Arg1);
    v_stack_mB0 = v_rip + 2454158;
    v_stack_mB8 = v_rip + 2454259;
loc_00BB77C0:
    result = VfReportIssueWithOptions(196, (uint32_t)((uint32_t)((uint32_t)(0x1009ULL))), Arg1, (int32_t)(*(uint32_t *)(result)));
    goto loc_00BB799E;
loc_00BB77D2:
    result = (uint32_t)((result) + (-5));
    if (((uint32_t)(result)) <= ((uint32_t)(Arg1))) goto loc_00BB77E7;
    goto loc_00BB77EB;
loc_00BB77E7:
loc_00BB77EB:
    Arg1 = (uint16_t)((196) - ((uint16_t)(Arg1)));
    *(uint16_t *)(result + 0x6) = (uint16_t)(Arg1);
    if (condition_is_not_equal) goto loc_00BB7994;
    *(uint64_t *)(result + 0x10) = (uint32_t)((uint32_t)((uint32_t)(0x1009ULL)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38)) == result) goto loc_00BB7912;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2C77B + (int32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38))) * 4)))) & (4)) != 0) goto loc_00BB78DE;
    result = (uint32_t)(*(uint32_t *)(v_rip - 0x2C77B + (int32_t)(*(uint32_t *)(result)) * 4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2C77B + (int32_t)(*(uint32_t *)(result)) * 4)))) & (4)) == 0) {
        Arg3 = v_rip + 14182;
        Arg1 = 93;
        result = DbgPrintEx(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x1009ULL))), Arg3, (int32_t)(*(uint32_t *)(result)));
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38);
        Arg3 = v_rip + 14065;
        Arg2 = 0;
        v_stack_mA8 = Arg1;
        v_stack_mB0 = *(uint64_t *)(result + 0x10);
        Arg4 = Arg1;
        result = *(uint64_t *)(result + 0x8);
        Arg1 = Arg2 + 93;
        v_stack_mB8 = result;
        result = DbgPrintEx(Arg1, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38);
        Arg2 = v_rip + 14230;
        v_stack_mB0 = *(uint64_t *)(result + 0x10);
        Arg1 = v_rip + 2453918;
        Arg4 = Arg1;
        Arg3 = 0x1003ULL;
        result = *(uint64_t *)(result + 0x8);
        v_stack_mB8 = result;
        result = ViDeadlockPreprocessOptions(Arg1, Arg2, Arg3, Arg4);
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38);
        result = v_rip + 2453884;
        v_stack_mB0 = result;
        Arg3 = Arg1;
        Arg2 = 0x1003ULL;
        v_stack_mB8 = *(uint64_t *)(result + 0x10);
        Arg1 = 196;
        Arg4 = *(uint64_t *)(Arg4 + 0x8);
        result = VfReportIssueWithOptions(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0;
        Arg3 = Arg2 + 1;
    }
    if (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) == 0) goto loc_00BB7919;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x38)) == result) goto loc_00BB78EE;
    goto loc_00BB78DE;
loc_00BB78EE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) + 0x48))) & (0xFFFFFFFEULL));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) + 0x48) = (uint32_t)(result);
    if ((((uint8_t)(result)) & (4)) == 0) {
        result = *(uint64_t *)(v_rip + 0x4460FB);
    }
    goto loc_00BB7919;
loc_00BB7912:
loc_00BB7919:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - (5));
    if (((uint32_t)(result)) <= ((uint32_t)(Arg3))) goto loc_00BB7943;
loc_00BB7923:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10) == 0) goto loc_00BB7969;
    if ((((uint8_t)(Arg3)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10) + 0x48))))) == 0) goto loc_00BB793A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10) + 0x40)) == (*(uint64_t *)(result + 0x10))) goto loc_00BB7969;
loc_00BB793A:
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10));
    goto loc_00BB7923;
loc_00BB7943:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) == 0) goto loc_00BB7969;
loc_00BB794C:
    if ((((uint8_t)(Arg3)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x48))))) == 0) goto loc_00BB795A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) + 0x40)) == (*(uint64_t *)(result + 0x10))) goto loc_00BB7969;
loc_00BB795A:
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != 0) goto loc_00BB794C;
loc_00BB7969:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) == 0) goto loc_00BB7999;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) + 0x40) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10))) != ((uint32_t)(0x1009ULL))) {
    }
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0x28)) != 0) goto loc_00BB7999;
    Arg2 = 0;
    result = ViDeadlockRemoveThread(*(uint64_t *)(result + 0x10), Arg2, Arg3, Arg4);
    goto loc_00BB799E;
loc_00BB7994:
    goto loc_00BB799E;
loc_00BB7999:
loc_00BB799E:
    *(uint64_t *)(result + 0xB8) = v_xmm0;
    *(uint64_t *)(result + 0xC8) = v_xmm1;
    *(uint64_t *)(result + 0xD8) = v_xmm0;
    *(uint64_t *)(result + 0xE8) = v_xmm1;
loc_00BB79D1:
loc_00BB79D6:
    result = (*(uint64_t *)(result)) - (*(uint64_t *)(1));
    if (result >= = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x446016) + 0x8))) {
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x446016) + 0x8) = result;
    }
    result = ViDeadlockDetectionUnlock(1, *(uint64_t *)(v_rip + 0x446016), Arg3, Arg4);
    result = ViLowerIrql((uint8_t)(v_stack_m98), *(uint64_t *)(v_rip + 0x446016), Arg3, Arg4);
    if (v_stack_m90 == 0) goto loc_00BB7A28;
loc_00BB7A13:
    result = ViDeadlockFree(v_stack_m90, 2, Arg3, Arg4);
    if (*(uint64_t *)(v_stack_m90) != 0) goto loc_00BB7A13;
loc_00BB7A28:
    if ((uint32_t)((uint32_t)(v_stack_m94)) != 0) {
        Arg2 = 3;
        Arg1 = *(uint64_t *)(result + 0x10);
        result = ViDeadlockFree(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x5` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB759C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
