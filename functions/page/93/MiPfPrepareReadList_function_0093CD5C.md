# MiPfPrepareReadList

- RVA: `0x0093CD5C`–`0x0093D4E8` (길이 `1,932` bytes)
- VA: `0x000000014093CD5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008FF6C`
- 디코드: `461`개 명령, `1,932/1,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0093CE0E` → [MiReleaseReadListResources](MiReleaseReadListResources_function_0093D570.md) (function, `0x0093D570`)
- `0x0093CE1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093CE3B` → [MiAllocateReadList](MiAllocateReadList_function_0093D4F0.md) (function, `0x0093D4F0`)
- `0x0093CE6A` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (function, `0x0043E560`)
- `0x0093CE9A` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x0093CF47` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0093CF54` → [MiColorBaseToNode](../../text/46/MiColorBaseToNode_function_004660B4.md) (function, `0x004660B4`)
- `0x0093CFF6` → [MiUpdatePfnForPrefetchByPte](../../text/32/MiUpdatePfnForPrefetchByPte_function_00321210.md) (function, `0x00321210`)
- `0x0093D020` → [IS_PTE_NOT_DEMAND_ZERO](../../text/22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x0093D054` → [MiStartingOffsetNeedLock](../../text/44/MiStartingOffsetNeedLock_function_00443964.md) (function, `0x00443964`)
- `0x0093D061` → [MiEndingOffsetWithLock](../../text/40/MiEndingOffsetWithLock_function_00404718.md) (function, `0x00404718`)
- `0x0093D099` → [MiAddViewsForSection](../../text/32/MiAddViewsForSection_function_00324990.md) (function, `0x00324990`)
- `0x0093D0D0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0093D13E` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x0093D149` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x0093D196` → [MiPrefetchNormally](../../text/45/MiPrefetchNormally_function_0045A6CC.md) (function, `0x0045A6CC`)
- `0x0093D1C1` → [MiObtainFaultCharges](../../text/28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x0093D1D7` → [MiGetNextPageColor](../../text/44/MiGetNextPageColor_function_00442D64.md) (function, `0x00442D64`)
- `0x0093D1F6` → [MiUseSlabAllocator](../../text/36/MiUseSlabAllocator_function_00365C68.md) (function, `0x00365C68`)
- `0x0093D214` → [MiGetPage](../../text/28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0093D23B` → [MiGetPfnSlabType](../../text/28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0093D250` → [MiInsertPageChainHead](../../text/2A/MiInsertPageChainHead_function_002A24EC.md) (function, `0x002A24EC`)
- `0x0093D26A` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0093D2A5` → [MiRefillPurgedExtents](../../text/47/MiRefillPurgedExtents_function_00479988.md) (function, `0x00479988`)
- `0x0093D3B4` → [MiPfAllocateMdls](MiPfAllocateMdls_function_0093E45C.md) (function, `0x0093E45C`)
- `0x0093D410` → [MiGetSlabPage](../../text/37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x0093D427` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0093D457` → [MiReleaseReadListResources](MiReleaseReadListResources_function_0093D570.md) (function, `0x0093D570`)
- `0x0093D461` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093D4A5` → [MiLocateSubsectionNode](../../text/2B/MiLocateSubsectionNode_function_002BBEE0.md) (function, `0x002BBEE0`)
- `0x0093D4DE` → [MiRemoveViewsFromSectionWithPfn](../../text/29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) (function, `0x002986D4`)

### Direct callers
- [MmPrefetchPagesEx](MmPrefetchPagesEx_function_0093C9A0.md) at `0x0093CAA2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x0093CE1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0093CE6A` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (`PAGE` → `.text`)
  - `0x0093CE9A` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (`PAGE` → `.text`)
  - `0x0093CF47` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (`PAGE` → `.text`)
  - `0x0093CF54` → [MiColorBaseToNode](../../text/46/MiColorBaseToNode_function_004660B4.md) (`PAGE` → `.text`)
  - `0x0093CFF6` → [MiUpdatePfnForPrefetchByPte](../../text/32/MiUpdatePfnForPrefetchByPte_function_00321210.md) (`PAGE` → `.text`)
  - `0x0093D020` → [IS_PTE_NOT_DEMAND_ZERO](../../text/22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (`PAGE` → `.text`)
  - `0x0093D054` → [MiStartingOffsetNeedLock](../../text/44/MiStartingOffsetNeedLock_function_00443964.md) (`PAGE` → `.text`)
  - `0x0093D061` → [MiEndingOffsetWithLock](../../text/40/MiEndingOffsetWithLock_function_00404718.md) (`PAGE` → `.text`)
  - `0x0093D099` → [MiAddViewsForSection](../../text/32/MiAddViewsForSection_function_00324990.md) (`PAGE` → `.text`)
  - `0x0093D0D0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0093D13E` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x0093D149` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x0093D196` → [MiPrefetchNormally](../../text/45/MiPrefetchNormally_function_0045A6CC.md) (`PAGE` → `.text`)
  - `0x0093D1C1` → [MiObtainFaultCharges](../../text/28/MiObtainFaultCharges_function_0028AEB0.md) (`PAGE` → `.text`)
  - `0x0093D1D7` → [MiGetNextPageColor](../../text/44/MiGetNextPageColor_function_00442D64.md) (`PAGE` → `.text`)
  - `0x0093D1F6` → [MiUseSlabAllocator](../../text/36/MiUseSlabAllocator_function_00365C68.md) (`PAGE` → `.text`)
  - `0x0093D214` → [MiGetPage](../../text/28/MiGetPage_function_002884C0.md) (`PAGE` → `.text`)
  - `0x0093D23B` → [MiGetPfnSlabType](../../text/28/MiGetPfnSlabType_function_0028E2D0.md) (`PAGE` → `.text`)
  - `0x0093D250` → [MiInsertPageChainHead](../../text/2A/MiInsertPageChainHead_function_002A24EC.md) (`PAGE` → `.text`)
  - `0x0093D26A` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0093D2A5` → [MiRefillPurgedExtents](../../text/47/MiRefillPurgedExtents_function_00479988.md) (`PAGE` → `.text`)
  - `0x0093D410` → [MiGetSlabPage](../../text/37/MiGetSlabPage_function_00376FBC.md) (`PAGE` → `.text`)
  - `0x0093D427` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (`PAGE` → `.text`)
  - `0x0093D461` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0093D4A5` → [MiLocateSubsectionNode](../../text/2B/MiLocateSubsectionNode_function_002BBEE0.md) (`PAGE` → `.text`)
  - `0x0093D4DE` → [MiRemoveViewsFromSectionWithPfn](../../text/29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0093CD5C  48 8B C4                        mov rax, rsp
0093CD5F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0093CD63  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0093CD67  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0093CD6B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0093CD6F  53                              push rbx
0093CD70  55                              push rbp
0093CD71  56                              push rsi
0093CD72  57                              push rdi
0093CD73  41 54                           push r12
0093CD75  41 55                           push r13
0093CD77  41 56                           push r14
0093CD79  41 57                           push r15
0093CD7B  48 81 EC C8 00 00 00            sub rsp, 0xc8
0093CD82  45 33 F6                        xor r14d, r14d
0093CD85  0F 57 C0                        xorps xmm0, xmm0
0093CD88  4C 89 32                        mov qword ptr [rdx], r14
0093CD8B  48 8B F1                        mov rsi, rcx
0093CD8E  8B 59 10                        mov ebx, dword ptr [rcx + 0x10]
0093CD91  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0093CD96  0F 11 40 A0                     movups xmmword ptr [rax - 0x60], xmm0
0093CD9A  F7 C3 80 01 00 00               test ebx, 0x180
0093CDA0  75 36                           jne 0x14093cdd8
0093CDA2  48 8B 01                        mov rax, qword ptr [rcx]
0093CDA5  44 8B 41 08                     mov r8d, dword ptr [rcx + 8]
0093CDA9  44 39 76 0C                     cmp dword ptr [rsi + 0xc], r14d
0093CDAD  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
0093CDB2  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
0093CDB6  48 8D 4A 10                     lea rcx, [rdx + 0x10]
0093CDBA  48 0F 44 CA                     cmove rcx, rdx
0093CDBE  48 8B 39                        mov rdi, qword ptr [rcx]
0093CDC1  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
0093CDC9  F7 47 38 00 04 00 00            test dword ptr [rdi + 0x38], 0x400
0093CDD0  75 06                           jne 0x14093cdd8
0093CDD2  4C 39 77 40                     cmp qword ptr [rdi + 0x40], r14
0093CDD6  75 60                           jne 0x14093ce38
0093CDD8  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0093CDDD  EB 44                           jmp 0x14093ce23
0093CDDF  49 3B DA                        cmp rbx, r10
0093CDE2  0F 82 13 02 00 00               jb 0x14093cffb
0093CDE8  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0093CDEB  A8 20                           test al, 0x20
0093CDED  0F 84 96 06 00 00               je 0x14093d489
0093CDF3  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
0093CDF7  4D 85 ED                        test r13, r13
0093CDFA  0F 85 2F 02 00 00               jne 0x14093d02f
0093CE00  4C 39 74 24 38                  cmp qword ptr [rsp + 0x38], r14
0093CE05  0F 85 6C 05 00 00               jne 0x14093d377
0093CE0B  49 8B CF                        mov rcx, r15
0093CE0E  E8 5D 07 00 00                  call 0x14093d570
0093CE13  45 8B F4                        mov r14d, r12d
0093CE16  33 D2                           xor edx, edx
0093CE18  49 8B CF                        mov rcx, r15
0093CE1B  E8 50 5A 24 00                  call 0x140b82870
0093CE20  41 8B C6                        mov eax, r14d
0093CE23  48 81 C4 C8 00 00 00            add rsp, 0xc8
0093CE2A  41 5F                           pop r15
0093CE2C  41 5E                           pop r14
0093CE2E  41 5D                           pop r13
0093CE30  41 5C                           pop r12
0093CE32  5F                              pop rdi
0093CE33  5E                              pop rsi
0093CE34  5D                              pop rbp
0093CE35  5B                              pop rbx
0093CE36  C3                              ret
0093CE37  CC                              int3
0093CE38  41 8B C8                        mov ecx, r8d
0093CE3B  E8 B0 06 00 00                  call 0x14093d4f0
0093CE40  4C 8B F8                        mov r15, rax
0093CE43  48 85 C0                        test rax, rax
0093CE46  0F 84 66 06 00 00               je 0x14093d4b2
0093CE4C  48 89 78 08                     mov qword ptr [rax + 8], rdi
0093CE50  4C 8D AF 80 00 00 00            lea r13, [rdi + 0x80]
0093CE57  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0093CE60  48 8B CF                        mov rcx, rdi
0093CE63  48 8B A8 B8 00 00 00            mov rbp, qword ptr [rax + 0xb8]
0093CE6A  E8 F1 16 B0 FF                  call 0x14043e560
0093CE6F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0093CE74  48 B9 00 00 00 00 00 00 40 00   movabs rcx, 0x40000000000000
0093CE7E  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0093CE81  A8 20                           test al, 0x20
0093CE83  0F 85 DE 03 00 00               jne 0x14093d267
0093CE89  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0093CE8D  48 3B D1                        cmp rdx, rcx
0093CE90  77 84                           ja 0x14093ce16
0093CE92  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0093CE97  48 8B CF                        mov rcx, rdi
0093CE9A  E8 E1 09 91 FF                  call 0x14024d880
0093CE9F  4C 8B E8                        mov r13, rax
0093CEA2  48 85 C0                        test rax, rax
0093CEA5  0F 84 6B FF FF FF               je 0x14093ce16
0093CEAB  83 4C 24 30 FF                  or dword ptr [rsp + 0x30], 0xffffffff
0093CEB0  8B C3                           mov eax, ebx
0093CEB2  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0093CEB7  83 E0 07                        and eax, 7
0093CEBA  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
0093CEBF  41 89 87 B8 00 00 00            mov dword ptr [r15 + 0xb8], eax
0093CEC6  49 8D 8F F0 00 00 00            lea rcx, [r15 + 0xf0]
0093CECD  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0093CED1  4C 8D 8C 24 A8 00 00 00         lea r9, [rsp + 0xa8]
0093CED9  8B C3                           mov eax, ebx
0093CEDB  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0093CEE3  24 40                           and al, 0x40
0093CEE5  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
0093CEEA  F6 D8                           neg al
0093CEEC  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0093CEF1  48 8D 8D 00 04 00 00            lea rcx, [rbp + 0x400]
0093CEF8  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
0093CF00  1B C0                           sbb eax, eax
0093CF02  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0093CF07  83 E0 05                        and eax, 5
0093CF0A  C1 EB 03                        shr ebx, 3
0093CF0D  41 89 87 BC 00 00 00            mov dword ptr [r15 + 0xbc], eax
0093CF14  83 E3 07                        and ebx, 7
0093CF17  41 89 9F C0 00 00 00            mov dword ptr [r15 + 0xc0], ebx
0093CF1E  BA 03 00 00 00                  mov edx, 3
0093CF23  8B 77 38                        mov esi, dword ptr [rdi + 0x38]
0093CF26  45 8B E6                        mov r12d, r14d
0093CF29  C1 EE 14                        shr esi, 0x14
0093CF2C  83 E6 7F                        and esi, 0x7f
0093CF2F  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
0093CF37  44 8B C6                        mov r8d, esi
0093CF3A  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
0093CF42  44 89 74 24 44                  mov dword ptr [rsp + 0x44], r14d
0093CF47  E8 C4 34 9E FF                  call 0x140320410
0093CF4C  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
0093CF54  E8 5B 91 B2 FF                  call 0x1404660b4
0093CF59  8B E8                           mov ebp, eax
0093CF5B  BA 01 00 00 00                  mov edx, 1
0093CF60  41 8B C6                        mov eax, r14d
0093CF63  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0093CF67  3B 44 24 78                     cmp eax, dword ptr [rsp + 0x78]
0093CF6B  0F 83 8F FE FF FF               jae 0x14093ce00
0093CF71  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
0093CF79  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0093CF7E  48 8B 5C C1 10                  mov rbx, qword ptr [rcx + rax*8 + 0x10]
0093CF83  48 83 E3 80                     and rbx, 0xffffffffffffff80
0093CF87  4C 3B D3                        cmp r10, rbx
0093CF8A  0F 87 9F 00 00 00               ja 0x14093d02f
0093CF90  48 3B 5C 24 60                  cmp rbx, qword ptr [rsp + 0x60]
0093CF95  0F 83 94 00 00 00               jae 0x14093d02f
0093CF9B  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
0093CF9F  49 2B DA                        sub rbx, r10
0093CFA2  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
0093CFA6  48 C1 EB 0C                     shr rbx, 0xc
0093CFAA  4C 8D 0C D9                     lea r9, [rcx + rbx*8]
0093CFAE  48 8D 0C C1                     lea rcx, [rcx + rax*8]
0093CFB2  4C 3B C9                        cmp r9, rcx
0093CFB5  0F 83 45 FE FF FF               jae 0x14093ce00
0093CFBB  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0093CFBF  0F BA E0 11                     bt eax, 0x11
0093CFC3  0F 82 79 04 00 00               jb 0x14093d442
0093CFC9  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
0093CFCE  4C 3B 8C 24 98 00 00 00         cmp r9, qword ptr [rsp + 0x98]
0093CFD6  74 28                           je 0x14093d000
0093CFD8  49 8B 19                        mov rbx, qword ptr [r9]
0093CFDB  4C 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r9
0093CFE3  84 DA                           test dl, bl
0093CFE5  74 24                           je 0x14093d00b
0093CFE7  4C 8B 84 24 28 01 00 00         mov r8, qword ptr [rsp + 0x128]
0093CFEF  49 8B C9                        mov rcx, r9
0093CFF2  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
0093CFF6  E8 15 42 9E FF                  call 0x140321210
0093CFFB  BA 01 00 00 00                  mov edx, 1
0093D000  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0093D004  03 C2                           add eax, edx
0093D006  E9 58 FF FF FF                  jmp 0x14093cf63
0093D00B  48 0F BA E3 0A                  bt rbx, 0xa
0093D010  0F 82 E7 00 00 00               jb 0x14093d0fd
0093D016  48 0F BA E3 0B                  bt rbx, 0xb
0093D01B  72 CA                           jb 0x14093cfe7
0093D01D  48 8B CB                        mov rcx, rbx
0093D020  E8 AB 24 8F FF                  call 0x14022f4d0
0093D025  85 C0                           test eax, eax
0093D027  0F 85 DD 00 00 00               jne 0x14093d10a
0093D02D  EB D1                           jmp 0x14093d000
0093D02F  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0093D032  A8 20                           test al, 0x20
0093D034  74 17                           je 0x14093d04d
0093D036  45 39 75 24                     cmp dword ptr [r13 + 0x24], r14d
0093D03A  75 11                           jne 0x14093d04d
0093D03C  48 8B 07                        mov rax, qword ptr [rdi]
0093D03F  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
0093D043  49 39 4D 08                     cmp qword ptr [r13 + 8], rcx
0093D047  0F 85 A6 FD FF FF               jne 0x14093cdf3
0093D04D  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0093D051  49 8B CD                        mov rcx, r13
0093D054  E8 0B 69 B0 FF                  call 0x140443964
0093D059  49 8B CD                        mov rcx, r13
0093D05C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0093D061  E8 B2 76 AC FF                  call 0x140404718
0093D066  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0093D06B  4C 8B D8                        mov r11, rax
0093D06E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0093D073  49 3B DA                        cmp rbx, r10
0093D076  72 83                           jb 0x14093cffb
0093D078  48 3B D8                        cmp rbx, rax
0093D07B  0F 83 5E FD FF FF               jae 0x14093cddf
0093D081  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0093D084  A8 20                           test al, 0x20
0093D086  0F 85 6C 02 00 00               jne 0x14093d2f8
0093D08C  41 8B 55 2C                     mov edx, dword ptr [r13 + 0x2c]
0093D090  41 B8 04 00 00 00               mov r8d, 4
0093D096  49 8B CD                        mov rcx, r13
0093D099  E8 F2 78 9E FF                  call 0x140324990
0093D09E  44 8B E0                        mov r12d, eax
0093D0A1  85 C0                           test eax, eax
0093D0A3  0F 88 57 FD FF FF               js 0x14093ce00
0093D0A9  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
0093D0AD  49 8D 47 18                     lea rax, [r15 + 0x18]
0093D0B1  48 39 00                        cmp qword ptr [rax], rax
0093D0B4  74 0A                           je 0x14093d0c0
0093D0B6  83 79 10 05                     cmp dword ptr [rcx + 0x10], 5
0093D0BA  0F 85 19 02 00 00               jne 0x14093d2d9
0093D0C0  BA 40 00 00 00                  mov edx, 0x40
0093D0C5  B9 00 01 00 00                  mov ecx, 0x100
0093D0CA  41 B8 4D 6D 53 6C               mov r8d, 0x6c536d4d
0093D0D0  E8 6B E4 A1 FF                  call 0x14035b540
0093D0D5  48 8B C8                        mov rcx, rax
0093D0D8  48 85 C0                        test rax, rax
0093D0DB  0F 84 F0 03 00 00               je 0x14093d4d1
0093D0E1  44 89 70 10                     mov dword ptr [rax + 0x10], r14d
0093D0E5  49 8D 47 18                     lea rax, [r15 + 0x18]
0093D0E9  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0093D0ED  48 39 02                        cmp qword ptr [rdx], rax
0093D0F0  0F 84 D5 01 00 00               je 0x14093d2cb
0093D0F6  B9 03 00 00 00                  mov ecx, 3
0093D0FB  CD 29                           int 0x29
0093D0FD  8A 47 3E                        mov al, byte ptr [rdi + 0x3e]
0093D100  24 0C                           and al, 0xc
0093D102  3C 04                           cmp al, 4
0093D104  0F 84 90 01 00 00               je 0x14093d29a
0093D10A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0093D112  4D 8B C1                        mov r8, r9
0093D115  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
0093D11D  48 85 C0                        test rax, rax
0093D120  49 0F 44 C2                     cmove rax, r10
0093D124  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0093D12C  4D 89 0A                        mov qword ptr [r10], r9
0093D12F  4C 39 AC 24 80 00 00 00         cmp qword ptr [rsp + 0x80], r13
0093D137  75 1A                           jne 0x14093d153
0093D139  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0093D13E  E8 ED 0F B0 FF                  call 0x14043e130
0093D143  49 8B C9                        mov rcx, r9
0093D146  48 8B D0                        mov rdx, rax
0093D149  E8 E2 0F B0 FF                  call 0x14043e130
0093D14E  48 3B D0                        cmp rdx, rax
0093D151  74 0F                           je 0x14093d162
0093D153  49 83 C8 02                     or r8, 2
0093D157  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
0093D15F  4D 89 02                        mov qword ptr [r10], r8
0093D162  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
0093D167  B8 01 00 00 00                  mov eax, 1
0093D16C  4D 3B CB                        cmp r9, r11
0093D16F  0F 84 03 01 00 00               je 0x14093d278
0093D175  45 8B 87 C0 00 00 00            mov r8d, dword ptr [r15 + 0xc0]
0093D17C  49 83 C2 08                     add r10, 8
0093D180  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0093D185  44 03 C0                        add r8d, eax
0093D188  48 8B CF                        mov rcx, rdi
0093D18B  4C 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], r10
0093D193  48 8B D0                        mov rdx, rax
0093D196  E8 31 D5 B1 FF                  call 0x14045a6cc
0093D19B  85 C0                           test eax, eax
0093D19D  0F 84 5D FC FF FF               je 0x14093ce00
0093D1A3  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
0093D1AB  48 85 C9                        test rcx, rcx
0093D1AE  0F 85 CF 00 00 00               jne 0x14093d283
0093D1B4  B8 01 00 00 00                  mov eax, 1
0093D1B9  48 8B CF                        mov rcx, rdi
0093D1BC  44 8B C0                        mov r8d, eax
0093D1BF  8B D0                           mov edx, eax
0093D1C1  E8 EA DC 94 FF                  call 0x14028aeb0
0093D1C6  48 85 C0                        test rax, rax
0093D1C9  0F 84 E6 00 00 00               je 0x14093d2b5
0093D1CF  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
0093D1D7  E8 88 5B B0 FF                  call 0x140442d64
0093D1DC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0093D1E1  8B F8                           mov edi, eax
0093D1E3  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0093D1E8  44 8B CD                        mov r9d, ebp
0093D1EB  4C 8B C3                        mov r8, rbx
0093D1EE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0093D1F3  49 8B D5                        mov rdx, r13
0093D1F6  E8 6D 8A A2 FF                  call 0x140365c68
0093D1FB  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
0093D1FF  85 C0                           test eax, eax
0093D201  0F 85 D9 01 00 00               jne 0x14093d3e0
0093D207  8B D7                           mov edx, edi
0093D209  45 8B C6                        mov r8d, r14d
0093D20C  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0093D211  48 8B CF                        mov rcx, rdi
0093D214  E8 A7 B2 94 FF                  call 0x1402884c0
0093D219  48 83 F8 FF                     cmp rax, -1
0093D21D  0F 84 F7 01 00 00               je 0x14093d41a
0093D223  4C 8D 04 40                     lea r8, [rax + rax*2]
0093D227  49 C1 E0 04                     shl r8, 4
0093D22B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0093D235  4C 03 C0                        add r8, rax
0093D238  49 8B C8                        mov rcx, r8
0093D23B  E8 90 10 95 FF                  call 0x14028e2d0
0093D240  83 F8 09                        cmp eax, 9
0093D243  0F 85 25 02 00 00               jne 0x14093d46e
0093D249  49 8D 4F 28                     lea rcx, [r15 + 0x28]
0093D24D  49 8B D0                        mov rdx, r8
0093D250  E8 97 52 96 FF                  call 0x1402a24ec
0093D255  48 FF 44 24 38                  inc qword ptr [rsp + 0x38]
0093D25A  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
0093D262  E9 94 FD FF FF                  jmp 0x14093cffb
0093D267  48 8B CD                        mov rcx, rbp
0093D26A  E8 81 26 8F FF                  call 0x14022f8f0
0093D26F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0093D273  E9 38 FC FF FF                  jmp 0x14093ceb0
0093D278  4C 0B C0                        or r8, rax
0093D27B  4D 89 02                        mov qword ptr [r10], r8
0093D27E  E9 F2 FE FF FF                  jmp 0x14093d175
0093D283  48 8B 01                        mov rax, qword ptr [rcx]
0093D286  48 85 C0                        test rax, rax
0093D289  0F 84 71 FB FF FF               je 0x14093ce00
0093D28F  48 FF C8                        dec rax
0093D292  48 89 01                        mov qword ptr [rcx], rax
0093D295  E9 1A FF FF FF                  jmp 0x14093d1b4
0093D29A  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
0093D29F  49 8B D1                        mov rdx, r9
0093D2A2  49 8B CD                        mov rcx, r13
0093D2A5  E8 DE C6 B3 FF                  call 0x140479988
0093D2AA  44 8B E0                        mov r12d, eax
0093D2AD  85 C0                           test eax, eax
0093D2AF  0F 89 46 FD FF FF               jns 0x14093cffb
0093D2B5  4C 39 74 24 38                  cmp qword ptr [rsp + 0x38], r14
0093D2BA  0F 85 B7 00 00 00               jne 0x14093d377
0093D2C0  41 BC 9A 00 00 C0               mov r12d, 0xc000009a
0093D2C6  E9 40 FB FF FF                  jmp 0x14093ce0b
0093D2CB  48 89 01                        mov qword ptr [rcx], rax
0093D2CE  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0093D2D2  48 89 0A                        mov qword ptr [rdx], rcx
0093D2D5  48 89 48 08                     mov qword ptr [rax + 8], rcx
0093D2D9  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0093D2DC  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0093D2E1  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
0093D2E6  4C 89 6C C1 18                  mov qword ptr [rcx + rax*8 + 0x18], r13
0093D2EB  FF 41 10                        inc dword ptr [rcx + 0x10]
0093D2EE  4D 39 77 10                     cmp qword ptr [r15 + 0x10], r14
0093D2F2  75 04                           jne 0x14093d2f8
0093D2F4  4D 89 6F 10                     mov qword ptr [r15 + 0x10], r13
0093D2F8  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
0093D2FC  49 2B DA                        sub rbx, r10
0093D2FF  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
0093D303  48 C1 EB 0C                     shr rbx, 0xc
0093D307  4C 8D 0C D9                     lea r9, [rcx + rbx*8]
0093D30B  48 8D 0C C1                     lea rcx, [rcx + rax*8]
0093D30F  4C 3B C9                        cmp r9, rcx
0093D312  0F 83 E8 FA FF FF               jae 0x14093ce00
0093D318  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0093D31C  45 8B C6                        mov r8d, r14d
0093D31F  0F BA E0 11                     bt eax, 0x11
0093D323  0F 82 93 01 00 00               jb 0x14093d4bc
0093D329  41 8B C3                        mov eax, r11d
0093D32C  BB FF 0F 00 00                  mov ebx, 0xfff
0093D331  41 2B C2                        sub eax, r10d
0093D334  85 C3                           test ebx, eax
0093D336  75 28                           jne 0x14093d360
0093D338  4D 8B DE                        mov r11, r14
0093D33B  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
0093D340  45 85 C0                        test r8d, r8d
0093D343  0F 85 B2 FC FF FF               jne 0x14093cffb
0093D349  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
0093D34E  4D 85 ED                        test r13, r13
0093D351  0F 84 A9 FA FF FF               je 0x14093ce00
0093D357  41 8D 50 01                     lea edx, [r8 + 1]
0093D35B  E9 6E FC FF FF                  jmp 0x14093cfce
0093D360  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0093D364  4D 2B DA                        sub r11, r10
0093D367  4C 03 DB                        add r11, rbx
0093D36A  49 C1 EB 0C                     shr r11, 0xc
0093D36E  49 FF CB                        dec r11
0093D371  4E 8D 1C D8                     lea r11, [rax + r11*8]
0093D375  EB C4                           jmp 0x14093d33b
0093D377  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0093D37F  45 33 C0                        xor r8d, r8d
0093D382  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0093D38A  4C 8B 8C 24 30 01 00 00         mov r9, qword ptr [rsp + 0x130]
0093D392  49 2B C7                        sub rax, r15
0093D395  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0093D399  48 2D F0 00 00 00               sub rax, 0xf0
0093D39F  48 C1 F8 03                     sar rax, 3
0093D3A3  49 89 8F C8 00 00 00            mov qword ptr [r15 + 0xc8], rcx
0093D3AA  49 8B CF                        mov rcx, r15
0093D3AD  41 89 87 C4 00 00 00            mov dword ptr [r15 + 0xc4], eax
0093D3B4  E8 A3 10 00 00                  call 0x14093e45c
0093D3B9  49 8D 8F E0 00 00 00            lea rcx, [r15 + 0xe0]
0093D3C0  8B D8                           mov ebx, eax
0093D3C2  48 39 09                        cmp qword ptr [rcx], rcx
0093D3C5  0F 84 89 00 00 00               je 0x14093d454
0093D3CB  41 8B DE                        mov ebx, r14d
0093D3CE  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
0093D3D6  4C 89 38                        mov qword ptr [rax], r15
0093D3D9  8B C3                           mov eax, ebx
0093D3DB  E9 43 FA FF FF                  jmp 0x14093ce23
0093D3E0  83 FB 04                        cmp ebx, 4
0093D3E3  0F 87 1E FE FF FF               ja 0x14093d207
0093D3E9  8B C6                           mov eax, esi
0093D3EB  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0093D3F0  F7 D8                           neg eax
0093D3F2  44 8B C7                        mov r8d, edi
0093D3F5  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0093D3FA  8B D3                           mov edx, ebx
0093D3FC  45 1B C9                        sbb r9d, r9d
0093D3FF  48 8B CF                        mov rcx, rdi
0093D402  48 83 4C 24 20 FF               or qword ptr [rsp + 0x20], 0xffffffffffffffff
0093D408  41 83 E1 FE                     and r9d, 0xfffffffe
0093D40C  41 83 C1 06                     add r9d, 6
0093D410  E8 A7 9B A3 FF                  call 0x140376fbc
0093D415  E9 FF FD FF FF                  jmp 0x14093d219
0093D41A  B8 01 00 00 00                  mov eax, 1
0093D41F  48 8B CF                        mov rcx, rdi
0093D422  44 8B C0                        mov r8d, eax
0093D425  8B D0                           mov edx, eax
0093D427  E8 FC 04 A3 FF                  call 0x14036d928
0093D42C  4C 39 74 24 38                  cmp qword ptr [rsp + 0x38], r14
0093D431  0F 85 40 FF FF FF               jne 0x14093d377
0093D437  41 BC 17 00 00 C0               mov r12d, 0xc0000017
0093D43D  E9 C9 F9 FF FF                  jmp 0x14093ce0b
0093D442  F7 47 38 00 00 00 08            test dword ptr [rdi + 0x38], 0x8000000
0093D449  0F 84 7A FB FF FF               je 0x14093cfc9
0093D44F  E9 AC FB FF FF                  jmp 0x14093d000
0093D454  49 8B CF                        mov rcx, r15
0093D457  E8 14 01 00 00                  call 0x14093d570
0093D45C  33 D2                           xor edx, edx
0093D45E  49 8B CF                        mov rcx, r15
0093D461  E8 0A 54 24 00                  call 0x140b82870
0093D466  4D 8B FE                        mov r15, r14
0093D469  E9 60 FF FF FF                  jmp 0x14093d3ce
0093D46E  83 FB 04                        cmp ebx, 4
0093D471  76 03                           jbe 0x14093d476
0093D473  83 C3 FB                        add ebx, -5
0093D476  8B C3                           mov eax, ebx
0093D478  48 8D 48 04                     lea rcx, [rax + 4]
0093D47C  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0093D480  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0093D484  E9 C4 FD FF FF                  jmp 0x14093d24d
0093D489  48 B8 00 00 00 00 00 00 40 00   movabs rax, 0x40000000000000
0093D493  48 3B D8                        cmp rbx, rax
0093D496  0F 87 64 F9 FF FF               ja 0x14093ce00
0093D49C  45 33 C0                        xor r8d, r8d
0093D49F  48 8B D3                        mov rdx, rbx
0093D4A2  48 8B CF                        mov rcx, rdi
0093D4A5  E8 36 EA 97 FF                  call 0x1402bbee0
0093D4AA  4C 8B E8                        mov r13, rax
0093D4AD  E9 45 F9 FF FF                  jmp 0x14093cdf7
0093D4B2  B8 9A 00 00 C0                  mov eax, 0xc000009a
0093D4B7  E9 67 F9 FF FF                  jmp 0x14093ce23
0093D4BC  F7 47 38 00 00 00 08            test dword ptr [rdi + 0x38], 0x8000000
0093D4C3  B8 01 00 00 00                  mov eax, 1
0093D4C8  44 0F 45 C0                     cmovne r8d, eax
0093D4CC  E9 58 FE FF FF                  jmp 0x14093d329
0093D4D1  41 8B 55 2C                     mov edx, dword ptr [r13 + 0x2c]
0093D4D5  41 B8 04 00 00 00               mov r8d, 4
0093D4DB  49 8B CD                        mov rcx, r13
0093D4DE  E8 F1 B1 95 FF                  call 0x1402986d4
0093D4E3  E9 18 F9 FF FF                  jmp 0x14093ce00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfPrepareReadList(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (200);
    v_r14 = 0;
    *(unsigned __int64 *)(a2) = 0;
    v_stack_m98 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (384)) != 0) goto loc_0093CDD8;
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 40) + 16;
    if ((*(unsigned int *)(a1 + 12)) == 0) { a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 40); }
    v_stack_m68 = *(unsigned __int64 *)(a1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)) & (0x400ULL)) != 0) goto loc_0093CDD8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64)) != 0) goto loc_0093CE38;
loc_0093CDD8:
    goto loc_0093CE23;
loc_0093CDDF:
    if (((unsigned int)(*(unsigned int *)(a1 + 16))) < v_r10) goto loc_0093CFFB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) == 0) goto loc_0093D489;
loc_0093CDF3:
loc_0093CDF7:
    if (*(unsigned __int64 *)(v_r13 + 16) != 0) goto loc_0093D02F;
loc_0093CE00:
    if (v_stack_mD0 != 0) goto loc_0093D377;
loc_0093CE0B:
    result = MiReleaseReadListResources(v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 40), (unsigned int)(*(unsigned int *)(a1 + 8)), a4);
loc_0093CE16:
    a2 = 0;
    result = ExFreePoolWithTag(v_r15, a2, (unsigned int)(*(unsigned int *)(a1 + 8)), a4);
loc_0093CE23:
    v_rsp = (v_rsp) + (200);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))));
loc_0093CE38:
    result = MiAllocateReadList((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))), a2, (unsigned int)(*(unsigned int *)(a1 + 8)), a4);
    if (result == 0) goto loc_0093D4B2;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1);
    result = MiGetControlAreaPartition(*(unsigned __int64 *)(a1), a2, (unsigned int)(*(unsigned int *)(a1 + 8)), a4);
    v_stack_p68 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) != 0) goto loc_0093D267;
    if ((*(unsigned __int64 *)(a1 + 16)) > (*(unsigned __int64 *)(a1))) goto loc_0093CE16;
    result = MiOffsetToProtos(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 16), v_stack_p70, a4);
    if (result == 0) goto loc_0093CE16;
loc_0093CEB0:
    v_stack_p70 = (unsigned int)((unsigned int)(v_r12));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (7));
    v_stack_p50 = (unsigned int)((unsigned int)(v_r12));
    *(unsigned int *)(result + 184) = (unsigned int)(result);
    v_stack_p40 = (unsigned int)(result);
    v_stack_p90 = result + 240;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (64));
    v_stack_p60 = (unsigned int)((unsigned int)(v_r12));
    result = (unsigned __int8)(-(result));
    v_stack_p58 = (unsigned int)((unsigned int)(v_r12));
    v_stack_p98 = (unsigned int)((unsigned int)(v_r12));
    v_stack_p38 = (unsigned int)((unsigned int)(v_r12));
    result = (unsigned int)((result) & (5));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) >> (3));
    *(unsigned int *)(result + 188) = (unsigned int)(result);
    v_rbx = (unsigned int)((v_rbx) & (7));
    *(unsigned int *)(result + 192) = (unsigned int)(v_rbx);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56))) >> (20));
    v_rsi = (unsigned int)((v_rsi) & (127));
    v_stack_p88 = (unsigned int)((unsigned int)(v_r12));
    v_stack_p80 = (unsigned int)((unsigned int)(v_r12));
    v_stack_p44 = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    result = MiInitializePageColorBase(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, 3, (unsigned int)((unsigned int)(v_rsi)), v_stack_pA8);
    result = MiColorBaseToNode(v_stack_pA8, 3, (unsigned int)((unsigned int)(v_rsi)), v_stack_pA8);
loc_0093CF63:
    v_stack_p48 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))) >= v_stack_p78) goto loc_0093CE00;
    v_rbx = (*(unsigned __int64 *)(v_stack_p110 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 8 + 16)) & (-128);
    if (v_stack_p50 > v_rbx) goto loc_0093D02F;
    if (v_rbx >= v_stack_p60) goto loc_0093D02F;
    v_rbx = (v_rbx) - (v_stack_p50);
    v_rbx = (v_rbx) >> (12);
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) >= (*(unsigned __int64 *)(result + 8) + (unsigned int)(*(unsigned int *)(result + 44)) * 8)) goto loc_0093CE00;
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) < (*(unsigned __int64 *)(result + 8) + (unsigned int)(*(unsigned int *)(result + 44)) * 8)) goto loc_0093D442;
loc_0093CFC9:
loc_0093CFCE:
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) == v_stack_p98) goto loc_0093D000;
    v_stack_p98 = *(unsigned __int64 *)(result + 8) + v_rbx * 8;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbx * 8)))) == 0) goto loc_0093D00B;
loc_0093CFE7:
    result = MiUpdatePfnForPrefetchByPte(*(unsigned __int64 *)(result + 8) + v_rbx * 8, (unsigned int)(v_stack_p40), v_stack_p128, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
loc_0093CFFB:
loc_0093D000:
    result = (unsigned int)(((unsigned int)(v_stack_p48)) + (1));
    goto loc_0093CF63;
loc_0093D00B:
    if (condition_is_below) goto loc_0093D0FD;
    if (condition_is_below) goto loc_0093CFE7;
    result = IS_PTE_NOT_DEMAND_ZERO(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbx * 8), 1, v_stack_p128, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if ((unsigned int)(result) != 0) goto loc_0093D10A;
    goto loc_0093D000;
loc_0093D02F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) == 0) goto loc_0093D04D;
    if ((*(unsigned int *)(result + 36)) != ((unsigned int)((unsigned int)((unsigned int)(v_r12))))) goto loc_0093D04D;
    if ((*(unsigned __int64 *)(result + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 64))) goto loc_0093CDF3;
loc_0093D04D:
    result = MiStartingOffsetNeedLock(result, (unsigned int)(v_stack_p30), v_stack_p128, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    v_stack_p50 = result;
    result = MiEndingOffsetWithLock(result, (unsigned int)(v_stack_p30), v_stack_p128, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    v_stack_p60 = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbx * 8)) < v_stack_p50) goto loc_0093CFFB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbx * 8)) >= result) goto loc_0093CDDF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) != 0) goto loc_0093D2F8;
    result = MiAddViewsForSection(result, (unsigned int)(*(unsigned int *)(result + 44)), 4, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if (sign_flag) goto loc_0093CE00;
    if ((*(unsigned __int64 *)(result + 24)) == (result + 24)) goto loc_0093D0C0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 16)) != 5) goto loc_0093D2D9;
loc_0093D0C0:
    result = MiAllocatePool(256, 64, (unsigned int)(0x6C536D4DULL), *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if (result == 0) goto loc_0093D4D1;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24 + 8))) == (result + 24)) goto loc_0093D2CB;
loc_0093D0FD:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_0093D29A;
loc_0093D10A:
    result = v_stack_p88;
    if (v_stack_p88 == 0) { result = v_stack_p90; }
    v_stack_p88 = result;
    *(unsigned __int64 *)(v_stack_p90) = *(unsigned __int64 *)(result + 8) + v_rbx * 8;
    if (v_stack_p80 != result) goto loc_0093D153;
    result = MiGetPteAddress(v_stack_p70, *(unsigned __int64 *)(result + 24 + 8), *(unsigned __int64 *)(result + 8) + v_rbx * 8, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    result = MiGetPteAddress(*(unsigned __int64 *)(result + 8) + v_rbx * 8, result, *(unsigned __int64 *)(result + 8) + v_rbx * 8, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if (result != result) {
        a3 = (*(unsigned __int64 *)(result + 8) + v_rbx * 8) | (2);
        v_stack_p80 = result;
        *(unsigned __int64 *)(v_stack_p90) = a3;
    }
    v_stack_p70 = *(unsigned __int64 *)(result + 8) + v_rbx * 8;
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) == result) goto loc_0093D278;
loc_0093D175:
    v_r10 = (v_stack_p90) + (8);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 192))) + (1));
    v_stack_p90 = v_r10;
    result = MiPrefetchNormally(v_stack_p68, 1, a3, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if ((unsigned int)(result) == 0) goto loc_0093CE00;
    if (v_stack_p120 != 0) goto loc_0093D283;
loc_0093D1B4:
    result = MiObtainFaultCharges(v_stack_p68, 1, 1, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    if (result == 0) goto loc_0093D2B5;
    result = MiGetNextPageColor(v_stack_pA8, 1, 1, *(unsigned __int64 *)(result + 8) + v_rbx * 8);
    v_stack_p20 = v_stack_p44;
    result = MiUseSlabAllocator(v_stack_p68, result, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbx * 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if ((unsigned int)(result) != 0) goto loc_0093D3E0;
loc_0093D207:
    result = MiGetPage(v_stack_p68, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_0093D219:
    if (result == -1) goto loc_0093D41A;
    a3 = (result + result * 2) << (4);
    a3 = (a3) + (result);
    result = MiGetPfnSlabType(a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (((unsigned int)(result)) != 9) goto loc_0093D46E;
loc_0093D24D:
    result = MiInsertPageChainHead(result + 40, a3, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0093CFFB;
loc_0093D267:
    result = PsGetProcessSessionIdEx((unsigned int)((unsigned int)(result)), a3, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p30 = (unsigned int)(result);
    goto loc_0093CEB0;
loc_0093D278:
    a3 = (a3) | (result);
    *(unsigned __int64 *)(v_r10) = a3;
    goto loc_0093D175;
loc_0093D283:
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) == 0) goto loc_0093CE00;
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) - 1;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result))) = result;
    goto loc_0093D1B4;
loc_0093D29A:
    result = MiRefillPurgedExtents(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_p30), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (!sign_flag) goto loc_0093CFFB;
loc_0093D2B5:
    if (v_stack_p38 != ((unsigned int)((unsigned int)(v_r12)))) goto loc_0093D377;
    goto loc_0093CE0B;
loc_0093D2CB:
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 8) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) = result;
    *(unsigned __int64 *)(result + 8) = result;
loc_0093D2D9:
    *(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 16)) * 8 + 24) = result;
    if ((*(unsigned __int64 *)(result + 16)) == ((unsigned int)((unsigned int)(v_r12)))) {
        *(unsigned __int64 *)(result + 16) = result;
    }
    v_rbx = ((unsigned int)(v_stack_p44)) - (v_stack_p50);
    v_rbx = (v_rbx) >> (12);
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) >= (*(unsigned __int64 *)(result + 8) + (unsigned int)(*(unsigned int *)(result + 44)) * 8)) goto loc_0093CE00;
    if ((*(unsigned __int64 *)(result + 8) + v_rbx * 8) < (*(unsigned __int64 *)(result + 8) + (unsigned int)(*(unsigned int *)(result + 44)) * 8)) goto loc_0093D4BC;
loc_0093D329:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p60))) - ((unsigned int)(v_stack_p50)));
    if ((((unsigned int)((unsigned int)(0xFFFULL))) & ((unsigned int)(result))) != 0) goto loc_0093D360;
loc_0093D33B:
    v_stack_p58 = (unsigned int)((unsigned int)(v_r12));
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))))) != 0) goto loc_0093CFFB;
    v_stack_p58 = (unsigned int)((unsigned int)(v_r12));
    if (result == 0) goto loc_0093CE00;
    goto loc_0093CFCE;
loc_0093D360:
    v_r11 = ((unsigned int)((unsigned int)(v_r12))) - (v_stack_p50);
    v_r11 = (v_r11) + ((unsigned int)(0xFFFULL));
    v_r11 = (v_r11) >> (12);
    v_r11 = (v_r11) - 1;
    goto loc_0093D33B;
loc_0093D377:
    a3 = 0;
    result = (v_stack_p90) - (result);
    result = (result) - (240);
    result = (result) >> (3);
    *(unsigned __int64 *)(result + 200) = v_stack_p88;
    *(unsigned int *)(result + 196) = (unsigned int)(result);
    result = MiPfAllocateMdls(result, (unsigned int)(v_stack_p30), a3, a5);
    if ((*(unsigned __int64 *)(result + 224)) == (result + 224)) goto loc_0093D454;
loc_0093D3CE:
    *(unsigned __int64 *)(v_stack_p118) = result;
    goto loc_0093CE23;
loc_0093D3E0:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))) > 4) goto loc_0093D207;
    v_stack_p28 = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_rsi))));
    a4 = (unsigned int)((a5) & (0xFFFFFFFEULL));
    a4 = (unsigned int)((a4) + (6));
    result = MiGetSlabPage(v_stack_p68, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))), (unsigned int)((unsigned int)(v_stack_pA0)), a4);
    goto loc_0093D219;
loc_0093D41A:
    result = MiReturnFaultCharges(v_stack_p68, 1, 1, a4);
    if (v_stack_p38 != ((unsigned int)((unsigned int)(v_r12)))) goto loc_0093D377;
    goto loc_0093CE0B;
loc_0093D442:
    if (((*(unsigned int *)(v_stack_p68 + 56)) & (0x8000000ULL)) == 0) goto loc_0093CFC9;
    goto loc_0093D000;
loc_0093D454:
    result = MiReleaseReadListResources(result, 1, 1, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 1, a4);
    goto loc_0093D3CE;
loc_0093D46E:
    v_rbx = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))))) >= = 4) {
        v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12))))) + (-5));
    }
    goto loc_0093D24D;
loc_0093D489:
    if (v_rbx > ((unsigned int)((unsigned int)(v_rbx)))) goto loc_0093CE00;
    a3 = 0;
    result = MiLocateSubsectionNode(v_stack_p68, v_rbx, a3, a4);
    goto loc_0093CDF7;
loc_0093D4B2:
    goto loc_0093CE23;
loc_0093D4BC:
    if (((*(unsigned int *)(v_stack_p68 + 56)) & (0x8000000ULL)) != 0) { a3 = 1; }
    goto loc_0093D329;
loc_0093D4D1:
    result = MiRemoveViewsFromSectionWithPfn(result, (unsigned int)(*(unsigned int *)(result + 44)), 4, a4);
    goto loc_0093CE00;
}
```

## 5. (Beta) C Style

```c
int64_t MiPfPrepareReadList(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mD0;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (200);
    local_r14 = 0;
    *(uint64_t *)(arg2) = 0;
    v_stack_m98 = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) & (384)) != 0) goto loc_0093CDD8;
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg1 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x28) + 16;
    if ((*(uint32_t *)(arg1 + 0xC)) == 0) { Arg1 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x28); }
    v_stack_m68 = *(uint64_t *)(arg1);
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)) & (0x400ULL)) != 0) goto loc_0093CDD8;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x40)) != 0) goto loc_0093CE38;
loc_0093CDD8:
    goto loc_0093CE23;
loc_0093CDDF:
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x10))) < local_r10) goto loc_0093CFFB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) == 0) goto loc_0093D489;
loc_0093CDF3:
loc_0093CDF7:
    if (*(uint64_t *)(local_r13 + 0x10) != 0) goto loc_0093D02F;
loc_0093CE00:
    if (v_stack_mD0 != 0) goto loc_0093D377;
loc_0093CE0B:
    result = MiReleaseReadListResources(local_r15, *(uint64_t *)(*(uint64_t *)(arg1) + 0x28), (uint32_t)(*(uint32_t *)(arg1 + 0x8)), Arg4);
loc_0093CE16:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r15, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x8)), Arg4);
loc_0093CE23:
    local_rsp = (local_rsp) + (200);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))));
loc_0093CE38:
    result = MiAllocateReadList((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))), Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x8)), Arg4);
    if (result == 0) goto loc_0093D4B2;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1);
    result = MiGetControlAreaPartition(*(uint64_t *)(arg1), Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x8)), Arg4);
    v_stack_p68 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) != 0) goto loc_0093D267;
    if ((*(uint64_t *)(arg1 + 0x10)) > (*(uint64_t *)(arg1))) goto loc_0093CE16;
    result = MiOffsetToProtos(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x10), v_stack_p70, Arg4);
    if (result == 0) goto loc_0093CE16;
loc_0093CEB0:
    v_stack_p70 = (uint32_t)((uint32_t)(local_r12));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (7));
    v_stack_p50 = (uint32_t)((uint32_t)(local_r12));
    *(uint32_t *)(result + 0xB8) = (uint32_t)(result);
    v_stack_p40 = (uint32_t)(result);
    v_stack_p90 = result + 240;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (64));
    v_stack_p60 = (uint32_t)((uint32_t)(local_r12));
    result = (uint8_t)(-(result));
    v_stack_p58 = (uint32_t)((uint32_t)(local_r12));
    v_stack_p98 = (uint32_t)((uint32_t)(local_r12));
    v_stack_p38 = (uint32_t)((uint32_t)(local_r12));
    result = (uint32_t)((result) & (5));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) >> (3));
    *(uint32_t *)(result + 0xBC) = (uint32_t)(result);
    local_rbx = (uint32_t)((local_rbx) & (7));
    *(uint32_t *)(result + 0xC0) = (uint32_t)(local_rbx);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38))) >> (20));
    local_rsi = (uint32_t)((local_rsi) & (127));
    v_stack_p88 = (uint32_t)((uint32_t)(local_r12));
    v_stack_p80 = (uint32_t)((uint32_t)(local_r12));
    v_stack_p44 = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    result = MiInitializePageColorBase(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, 3, (uint32_t)((uint32_t)(local_rsi)), v_stack_pA8);
    result = MiColorBaseToNode(v_stack_pA8, 3, (uint32_t)((uint32_t)(local_rsi)), v_stack_pA8);
loc_0093CF63:
    v_stack_p48 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))) >= v_stack_p78) goto loc_0093CE00;
    local_rbx = (*(uint64_t *)(v_stack_p110 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 8 + 0x10)) & (-128);
    if (v_stack_p50 > local_rbx) goto loc_0093D02F;
    if (local_rbx >= v_stack_p60) goto loc_0093D02F;
    local_rbx = (local_rbx) - (v_stack_p50);
    local_rbx = (local_rbx) >> (12);
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) >= (*(uint64_t *)(result + 0x8) + (uint32_t)(*(uint32_t *)(result + 0x2C)) * 8)) goto loc_0093CE00;
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) < (*(uint64_t *)(result + 0x8) + (uint32_t)(*(uint32_t *)(result + 0x2C)) * 8)) goto loc_0093D442;
loc_0093CFC9:
loc_0093CFCE:
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) == v_stack_p98) goto loc_0093D000;
    v_stack_p98 = *(uint64_t *)(result + 0x8) + local_rbx * 8;
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbx * 8)))) == 0) goto loc_0093D00B;
loc_0093CFE7:
    result = MiUpdatePfnForPrefetchByPte(*(uint64_t *)(result + 0x8) + local_rbx * 8, (uint32_t)(v_stack_p40), v_stack_p128, *(uint64_t *)(result + 0x8) + local_rbx * 8);
loc_0093CFFB:
loc_0093D000:
    result = (uint32_t)(((uint32_t)(v_stack_p48)) + (1));
    goto loc_0093CF63;
loc_0093D00B:
    if (condition_is_below) goto loc_0093D0FD;
    if (condition_is_below) goto loc_0093CFE7;
    result = IS_PTE_NOT_DEMAND_ZERO(*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbx * 8), 1, v_stack_p128, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if ((uint32_t)(result) != 0) goto loc_0093D10A;
    goto loc_0093D000;
loc_0093D02F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) == 0) goto loc_0093D04D;
    if ((*(uint32_t *)(result + 0x24)) != ((uint32_t)((uint32_t)((uint32_t)(local_r12))))) goto loc_0093D04D;
    if ((*(uint64_t *)(result + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x40))) goto loc_0093CDF3;
loc_0093D04D:
    result = MiStartingOffsetNeedLock(result, (uint32_t)(v_stack_p30), v_stack_p128, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    v_stack_p50 = result;
    result = MiEndingOffsetWithLock(result, (uint32_t)(v_stack_p30), v_stack_p128, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    v_stack_p60 = result;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbx * 8)) < v_stack_p50) goto loc_0093CFFB;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbx * 8)) >= result) goto loc_0093CDDF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) != 0) goto loc_0093D2F8;
    result = MiAddViewsForSection(result, (uint32_t)(*(uint32_t *)(result + 0x2C)), 4, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if (sign_flag) goto loc_0093CE00;
    if ((*(uint64_t *)(result + 0x18)) == (result + 24)) goto loc_0093D0C0;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x10)) != 5) goto loc_0093D2D9;
loc_0093D0C0:
    result = MiAllocatePool(256, 64, (uint32_t)(0x6C536D4DULL), *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if (result == 0) goto loc_0093D4D1;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x18 + 0x8))) == (result + 24)) goto loc_0093D2CB;
loc_0093D0FD:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_0093D29A;
loc_0093D10A:
    result = v_stack_p88;
    if (v_stack_p88 == 0) { result = v_stack_p90; }
    v_stack_p88 = result;
    *(uint64_t *)(v_stack_p90) = *(uint64_t *)(result + 0x8) + local_rbx * 8;
    if (v_stack_p80 != result) goto loc_0093D153;
    result = MiGetPteAddress(v_stack_p70, *(uint64_t *)(result + 0x18 + 0x8), *(uint64_t *)(result + 0x8) + local_rbx * 8, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    result = MiGetPteAddress(*(uint64_t *)(result + 0x8) + local_rbx * 8, result, *(uint64_t *)(result + 0x8) + local_rbx * 8, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if (result != result) {
        Arg3 = (*(uint64_t *)(result + 0x8) + local_rbx * 8) | (2);
        v_stack_p80 = result;
        *(uint64_t *)(v_stack_p90) = Arg3;
    }
    v_stack_p70 = *(uint64_t *)(result + 0x8) + local_rbx * 8;
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) == result) goto loc_0093D278;
loc_0093D175:
    local_r10 = (v_stack_p90) + (8);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xC0))) + (1));
    v_stack_p90 = local_r10;
    result = MiPrefetchNormally(v_stack_p68, 1, Arg3, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if ((uint32_t)(result) == 0) goto loc_0093CE00;
    if (v_stack_p120 != 0) goto loc_0093D283;
loc_0093D1B4:
    result = MiObtainFaultCharges(v_stack_p68, 1, 1, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    if (result == 0) goto loc_0093D2B5;
    result = MiGetNextPageColor(v_stack_pA8, 1, 1, *(uint64_t *)(result + 0x8) + local_rbx * 8);
    v_stack_p20 = v_stack_p44;
    result = MiUseSlabAllocator(v_stack_p68, result, *(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbx * 8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if ((uint32_t)(result) != 0) goto loc_0093D3E0;
loc_0093D207:
    result = MiGetPage(v_stack_p68, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_0093D219:
    if (result == -1) goto loc_0093D41A;
    Arg3 = (result + result * 2) << (4);
    Arg3 = (Arg3) + (result);
    result = MiGetPfnSlabType(Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (((uint32_t)(result)) != 9) goto loc_0093D46E;
loc_0093D24D:
    result = MiInsertPageChainHead(result + 40, Arg3, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0093CFFB;
loc_0093D267:
    result = PsGetProcessSessionIdEx((uint32_t)((uint32_t)(result)), Arg3, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p30 = (uint32_t)(result);
    goto loc_0093CEB0;
loc_0093D278:
    Arg3 = (Arg3) | (result);
    *(uint64_t *)(local_r10) = Arg3;
    goto loc_0093D175;
loc_0093D283:
    if (*(uint64_t *)((uint32_t)((uint32_t)(result))) == 0) goto loc_0093CE00;
    result = (*(uint64_t *)((uint32_t)((uint32_t)(result)))) - 1;
    *(uint64_t *)((uint32_t)((uint32_t)(result))) = result;
    goto loc_0093D1B4;
loc_0093D29A:
    result = MiRefillPurgedExtents(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_p30), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (!sign_flag) goto loc_0093CFFB;
loc_0093D2B5:
    if (v_stack_p38 != ((uint32_t)((uint32_t)(local_r12)))) goto loc_0093D377;
    goto loc_0093CE0B;
loc_0093D2CB:
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x8) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) = result;
    *(uint64_t *)(result + 0x8) = result;
loc_0093D2D9:
    *(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 8 + 0x18) = result;
    if ((*(uint64_t *)(result + 0x10)) == ((uint32_t)((uint32_t)(local_r12)))) {
        *(uint64_t *)(result + 0x10) = result;
    }
    local_rbx = ((uint32_t)(v_stack_p44)) - (v_stack_p50);
    local_rbx = (local_rbx) >> (12);
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) >= (*(uint64_t *)(result + 0x8) + (uint32_t)(*(uint32_t *)(result + 0x2C)) * 8)) goto loc_0093CE00;
    if ((*(uint64_t *)(result + 0x8) + local_rbx * 8) < (*(uint64_t *)(result + 0x8) + (uint32_t)(*(uint32_t *)(result + 0x2C)) * 8)) goto loc_0093D4BC;
loc_0093D329:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p60))) - ((uint32_t)(v_stack_p50)));
    if ((((uint32_t)((uint32_t)(0xFFFULL))) & ((uint32_t)(result))) != 0) goto loc_0093D360;
loc_0093D33B:
    v_stack_p58 = (uint32_t)((uint32_t)(local_r12));
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))))) != 0) goto loc_0093CFFB;
    v_stack_p58 = (uint32_t)((uint32_t)(local_r12));
    if (result == 0) goto loc_0093CE00;
    goto loc_0093CFCE;
loc_0093D360:
    local_r11 = ((uint32_t)((uint32_t)(local_r12))) - (v_stack_p50);
    local_r11 = (local_r11) + ((uint32_t)(0xFFFULL));
    local_r11 = (local_r11) >> (12);
    local_r11 = (local_r11) - 1;
    goto loc_0093D33B;
loc_0093D377:
    Arg3 = 0;
    result = (v_stack_p90) - (result);
    result = (result) - (240);
    result = (result) >> (3);
    *(uint64_t *)(result + 0xC8) = v_stack_p88;
    *(uint32_t *)(result + 0xC4) = (uint32_t)(result);
    result = MiPfAllocateMdls(result, (uint32_t)(v_stack_p30), Arg3, Arg5);
    if ((*(uint64_t *)(result + 0xE0)) == (result + 224)) goto loc_0093D454;
loc_0093D3CE:
    *(uint64_t *)(v_stack_p118) = result;
    goto loc_0093CE23;
loc_0093D3E0:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))) > 4) goto loc_0093D207;
    v_stack_p28 = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_rsi))));
    Arg4 = (uint32_t)((Arg5) & (0xFFFFFFFEULL));
    Arg4 = (uint32_t)((Arg4) + (6));
    result = MiGetSlabPage(v_stack_p68, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))), (uint32_t)((uint32_t)(v_stack_pA0)), Arg4);
    goto loc_0093D219;
loc_0093D41A:
    result = MiReturnFaultCharges(v_stack_p68, 1, 1, Arg4);
    if (v_stack_p38 != ((uint32_t)((uint32_t)(local_r12)))) goto loc_0093D377;
    goto loc_0093CE0B;
loc_0093D442:
    if (((*(uint32_t *)(v_stack_p68 + 0x38)) & (0x8000000ULL)) == 0) goto loc_0093CFC9;
    goto loc_0093D000;
loc_0093D454:
    result = MiReleaseReadListResources(result, 1, 1, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 1, Arg4);
    goto loc_0093D3CE;
loc_0093D46E:
    local_rbx = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))))) >= = 4) {
        local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12))))) + (-5));
    }
    goto loc_0093D24D;
loc_0093D489:
    if (local_rbx > ((uint32_t)((uint32_t)(local_rbx)))) goto loc_0093CE00;
    Arg3 = 0;
    result = MiLocateSubsectionNode(v_stack_p68, local_rbx, Arg3, Arg4);
    goto loc_0093CDF7;
loc_0093D4B2:
    goto loc_0093CE23;
loc_0093D4BC:
    if (((*(uint32_t *)(v_stack_p68 + 0x38)) & (0x8000000ULL)) != 0) { Arg3 = 1; }
    goto loc_0093D329;
loc_0093D4D1:
    result = MiRemoveViewsFromSectionWithPfn(result, (uint32_t)(*(uint32_t *)(result + 0x2C)), 4, Arg4);
    goto loc_0093CE00;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0093CD5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
