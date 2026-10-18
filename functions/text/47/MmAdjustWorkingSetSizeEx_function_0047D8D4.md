# MmAdjustWorkingSetSizeEx

- RVA: `0x0047D8D4`–`0x0047DD3C` (길이 `1,128` bytes)
- VA: `0x000000014047D8D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ADB34`
- 디코드: `261`개 명령, `1,128/1,128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0047D95C` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0047D967` → [MiLockWorkingSetCoreExclusive](../2C/MiLockWorkingSetCoreExclusive_function_002C0CFC.md) (function, `0x002C0CFC`)
- `0x0047D9C0` → [MiCheckWsLimits](MiCheckWsLimits_function_0047DD44.md) (function, `0x0047DD44`)
- `0x0047DA3F` → [MiUnlockWorkingSetCoreExclusive](../2C/MiUnlockWorkingSetCoreExclusive_function_002C0DC4.md) (function, `0x002C0DC4`)
- `0x0047DA4A` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0047DA7D` → [PsReturnProcessQuota](PsReturnProcessQuota_function_0047DE8C.md) (function, `0x0047DE8C`)
- `0x0047DA8A` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x0047DAC7` → [MiChargeResident](../28/MiChargeResident_function_0028A0F0.md) (function, `0x0028A0F0`)
- `0x0047DB26` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0047DB61` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0047DBA8` → [MiTrimWorkingSet](../2A/MiTrimWorkingSet_function_002AD134.md) (function, `0x002AD134`)
- `0x0047DBB4` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0047DC2D` → [PsChargeProcessQuota](PsChargeProcessQuota_function_0047DEC0.md) (function, `0x0047DEC0`)
- `0x0047DC4B` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0047DC9B` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0047DCB2` → [MiMapWorkingSetTypeToVm](../2C/MiMapWorkingSetTypeToVm_function_002C08C4.md) (function, `0x002C08C4`)
- `0x0047DCE1` → [PsReturnProcessQuota](PsReturnProcessQuota_function_0047DE8C.md) (function, `0x0047DE8C`)
- `0x0047DD0F` → [PsReturnProcessQuota](PsReturnProcessQuota_function_0047DE8C.md) (function, `0x0047DE8C`)

### Direct callers
- [CmSiAcquireProcessLockedPagesCharge](CmSiAcquireProcessLockedPagesCharge_function_0047D714.md) at `0x0047D78C`
- [MmAdjustWorkingSetSize](MmAdjustWorkingSetSize_function_0047D7F0.md) at `0x0047D808`
- [CmSiReleaseProcessLockedPagesCharge](CmSiReleaseProcessLockedPagesCharge_function_0047D81C.md) at `0x0047D88E`
- [KeSetExpectedConcurrencyCountProcess](../5C/KeSetExpectedConcurrencyCountProcess_function_005C1AC0.md) at `0x005C1B6B`
- [SmKmVirtualLockContextIncreaseWsMin](../60/SmKmVirtualLockContextIncreaseWsMin_function_0060FE94.md) at `0x0060FF82`
- [SmKmVirtualLockCtxMemoryUnlocked](../61/SmKmVirtualLockCtxMemoryUnlocked_function_0061015C.md) at `0x0061026D`
- [CmSiSetProcessWorkingSetMaximum](../66/CmSiSetProcessWorkingSetMaximum_function_0066DD6C.md) at `0x0066DDD8`
- [sub_006D8170](../6D/Unknown_function_006D8170.md) at `0x006D81B5`
- [PspSetQuotaLimits](../../page/9B/PspSetQuotaLimits_function_009BA8A8.md) at `0x009BABD9`
- [NtSetSystemInformation](../../page/AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5646`

### Static image references
- `0x0047D949` → RVA `0x00E30088` (`.data`; read)
- `0x0047DB3F` → RVA `0x002413C0` (`MiEmptyPte`; read)
- `0x0047DB4E` → RVA `0x0046CC90` (`MiEmptyWorkingSetTail`; read)
- `0x0047DC41` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0047DCD5` → [sub_006F4BA0](../6F/Unknown_function_006F4BA0.md) (`tail-transfer`)
  - `0x0047DCE7` → [sub_006F4BA0](../6F/Unknown_function_006F4BA0.md) (`tail-transfer`)
  - `0x0047DD03` → [sub_006F4BA0 + 0xA](../6F/Unknown_function_006F4BA0.md) (`tail-transfer`)
  - `0x0047DD15` → [sub_006F4BA0 + 0xA](../6F/Unknown_function_006F4BA0.md) (`tail-transfer`)
  - `0x0047DD2F` → [sub_006F4BA0 + 0x1D](../6F/Unknown_function_006F4BA0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0047D8D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0047D8D9  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0047D8DE  55                              push rbp
0047D8DF  56                              push rsi
0047D8E0  57                              push rdi
0047D8E1  41 54                           push r12
0047D8E3  41 55                           push r13
0047D8E5  41 56                           push r14
0047D8E7  41 57                           push r15
0047D8E9  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
0047D8EE  48 81 EC 20 01 00 00            sub rsp, 0x120
0047D8F5  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
0047D8FC  33 DB                           xor ebx, ebx
0047D8FE  45 8B F8                        mov r15d, r8d
0047D901  4C 8B F2                        mov r14, rdx
0047D904  48 8B F1                        mov rsi, rcx
0047D907  44 8B EB                        mov r13d, ebx
0047D90A  88 18                           mov byte ptr [rax], bl
0047D90C  45 85 C0                        test r8d, r8d
0047D90F  0F 85 AB 02 00 00               jne 0x14047dbc0
0047D915  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0047D91E  4C 8B A8 B8 00 00 00            mov r13, qword ptr [rax + 0xb8]
0047D925  49 8D BD 00 04 00 00            lea rdi, [r13 + 0x400]
0047D92C  48 85 FF                        test rdi, rdi
0047D92F  0F 84 C9 01 00 00               je 0x14047dafe
0047D935  49 83 CC FF                     or r12, 0xffffffffffffffff
0047D939  49 3B F4                        cmp rsi, r12
0047D93C  0F 84 C6 01 00 00               je 0x14047db08
0047D942  0F B7 8F AE 00 00 00            movzx ecx, word ptr [rdi + 0xae]
0047D949  48 8B 05 38 27 9B 00            mov rax, qword ptr [rip + 0x9b2738]
0047D950  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0047D954  48 8B CF                        mov rcx, rdi
0047D957  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0047D95C  E8 3F 5F EA FF                  call 0x1403238a0
0047D961  48 8B CF                        mov rcx, rdi
0047D964  88 45 70                        mov byte ptr [rbp + 0x70], al
0047D967  E8 90 33 E4 FF                  call 0x1402c0cfc
0047D96C  45 85 FF                        test r15d, r15d
0047D96F  75 10                           jne 0x14047d981
0047D971  41 8B 8D F4 01 00 00            mov ecx, dword ptr [r13 + 0x1f4]
0047D978  F6 C1 20                        test cl, 0x20
0047D97B  0F 85 9C 02 00 00               jne 0x14047dc1d
0047D981  48 85 F6                        test rsi, rsi
0047D984  0F 84 07 01 00 00               je 0x14047da91
0047D98A  48 C1 EE 0C                     shr rsi, 0xc
0047D98E  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0047D993  4D 85 F6                        test r14, r14
0047D996  0F 84 23 03 00 00               je 0x14047dcbf
0047D99C  49 C1 EE 0C                     shr r14, 0xc
0047D9A0  44 8B A5 80 00 00 00            mov r12d, dword ptr [rbp + 0x80]
0047D9A7  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0047D9AC  45 8B CC                        mov r9d, r12d
0047D9AF  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0047D9B4  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0047D9B9  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0047D9BD  48 8B CF                        mov rcx, rdi
0047D9C0  E8 7F 03 00 00                  call 0x14047dd44
0047D9C5  8B C8                           mov ecx, eax
0047D9C7  8B F0                           mov esi, eax
0047D9C9  B8 00 00 00 C0                  mov eax, 0xc0000000
0047D9CE  23 C8                           and ecx, eax
0047D9D0  3B C8                           cmp ecx, eax
0047D9D2  74 68                           je 0x14047da3c
0047D9D4  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
0047D9D8  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0047D9DD  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0047D9E1  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0047D9E6  4C 3B F0                        cmp r14, rax
0047D9E9  0F 87 AB 00 00 00               ja 0x14047da9a
0047D9EF  49 2B C6                        sub rax, r14
0047D9F2  4C 8B F0                        mov r14, rax
0047D9F5  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0047D9F9  48 39 44 24 38                  cmp qword ptr [rsp + 0x38], rax
0047D9FE  0F 82 0F 02 00 00               jb 0x14047dc13
0047DA04  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
0047DA0B  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
0047DA10  0F 82 C8 00 00 00               jb 0x14047dade
0047DA16  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
0047DA1D  38 18                           cmp byte ptr [rax], bl
0047DA1F  74 4C                           je 0x14047da6d
0047DA21  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0047DA26  48 89 47 78                     mov qword ptr [rdi + 0x78], rax
0047DA2A  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0047DA2F  48 89 47 70                     mov qword ptr [rdi + 0x70], rax
0047DA33  45 85 E4                        test r12d, r12d
0047DA36  0F 85 05 02 00 00               jne 0x14047dc41
0047DA3C  48 8B CF                        mov rcx, rdi
0047DA3F  E8 80 33 E4 FF                  call 0x1402c0dc4
0047DA44  8A 55 70                        mov dl, byte ptr [rbp + 0x70]
0047DA47  48 8B CF                        mov rcx, rdi
0047DA4A  E8 21 12 E0 FF                  call 0x14027ec70
0047DA4F  8B C6                           mov eax, esi
0047DA51  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
0047DA59  48 81 C4 20 01 00 00            add rsp, 0x120
0047DA60  41 5F                           pop r15
0047DA62  41 5E                           pop r14
0047DA64  41 5D                           pop r13
0047DA66  41 5C                           pop r12
0047DA68  5F                              pop rdi
0047DA69  5E                              pop rsi
0047DA6A  5D                              pop rbp
0047DA6B  C3                              ret
0047DA6C  CC                              int3
0047DA6D  4D 85 F6                        test r14, r14
0047DA70  74 AF                           je 0x14047da21
0047DA72  45 85 FF                        test r15d, r15d
0047DA75  75 0B                           jne 0x14047da82
0047DA77  4D 8B C6                        mov r8, r14
0047DA7A  49 8B CD                        mov rcx, r13
0047DA7D  E8 0A 04 00 00                  call 0x14047de8c
0047DA82  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0047DA87  49 8B D6                        mov rdx, r14
0047DA8A  E8 01 8E E0 FF                  call 0x140286890
0047DA8F  EB 90                           jmp 0x14047da21
0047DA91  48 8B 77 70                     mov rsi, qword ptr [rdi + 0x70]
0047DA95  E9 F4 FE FF FF                  jmp 0x14047d98e
0047DA9A  4C 2B F0                        sub r14, rax
0047DA9D  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
0047DAA4  C6 00 01                        mov byte ptr [rax], 1
0047DAA7  38 5D 78                        cmp byte ptr [rbp + 0x78], bl
0047DAAA  0F 84 18 02 00 00               je 0x14047dcc8
0047DAB0  45 85 FF                        test r15d, r15d
0047DAB3  0F 84 6E 01 00 00               je 0x14047dc27
0047DAB9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0047DABE  41 B8 00 02 00 00               mov r8d, 0x200
0047DAC4  49 8B D6                        mov rdx, r14
0047DAC7  E8 24 C6 E0 FF                  call 0x14028a0f0
0047DACC  85 C0                           test eax, eax
0047DACE  0F 84 FE 01 00 00               je 0x14047dcd2
0047DAD4  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0047DAD9  E9 26 FF FF FF                  jmp 0x14047da04
0047DADE  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0047DAE2  48 83 C0 06                     add rax, 6
0047DAE6  48 3B 44 24 30                  cmp rax, qword ptr [rsp + 0x30]
0047DAEB  0F 83 FB 01 00 00               jae 0x14047dcec
0047DAF1  F0 83 8F BC 00 00 00 02         lock or dword ptr [rdi + 0xbc], 2
0047DAF9  E9 18 FF FF FF                  jmp 0x14047da16
0047DAFE  B8 F1 00 00 C0                  mov eax, 0xc00000f1
0047DB03  E9 49 FF FF FF                  jmp 0x14047da51
0047DB08  4D 3B F4                        cmp r14, r12
0047DB0B  0F 85 31 FE FF FF               jne 0x14047d942
0047DB11  0F 57 C0                        xorps xmm0, xmm0
0047DB14  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0047DB19  33 D2                           xor edx, edx
0047DB1B  41 B8 C0 00 00 00               mov r8d, 0xc0
0047DB21  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0047DB26  E8 15 91 24 00                  call 0x1406c6c40
0047DB2B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0047DB30  C7 44 24 60 06 00 00 00         mov dword ptr [rsp + 0x60], 6
0047DB38  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0047DB3C  48 8B CF                        mov rcx, rdi
0047DB3F  48 8D 05 7A 38 DC FF            lea rax, [rip - 0x23c786]
0047DB46  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
0047DB4A  48 89 45 08                     mov qword ptr [rbp + 8], rax
0047DB4E  48 8D 05 3B F1 FE FF            lea rax, [rip - 0x10ec5]
0047DB55  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0047DB59  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
0047DB5D  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
0047DB61  E8 8A F0 DF FF                  call 0x14027cbf0
0047DB66  88 44 24 69                     mov byte ptr [rsp + 0x69], al
0047DB6A  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
0047DB70  A8 0F                           test al, 0xf
0047DB72  75 1E                           jne 0x14047db92
0047DB74  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0047DB7D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0047DB84  8B 81 F4 01 00 00               mov eax, dword ptr [rcx + 0x1f4]
0047DB8A  A8 20                           test al, 0x20
0047DB8C  0F 85 13 01 00 00               jne 0x14047dca5
0047DB92  44 8A 44 24 69                  mov r8b, byte ptr [rsp + 0x69]
0047DB97  45 33 C9                        xor r9d, r9d
0047DB9A  49 8B D4                        mov rdx, r12
0047DB9D  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
0047DBA5  48 8B CF                        mov rcx, rdi
0047DBA8  E8 87 F5 E2 FF                  call 0x1402ad134
0047DBAD  8A 54 24 69                     mov dl, byte ptr [rsp + 0x69]
0047DBB1  48 8B CF                        mov rcx, rdi
0047DBB4  E8 D7 FA DF FF                  call 0x14027d690
0047DBB9  8B C3                           mov eax, ebx
0047DBBB  E9 91 FE FF FF                  jmp 0x14047da51
0047DBC0  41 8D 40 FF                     lea eax, [r8 - 1]
0047DBC4  83 F8 03                        cmp eax, 3
0047DBC7  0F 87 31 FF FF FF               ja 0x14047dafe
0047DBCD  41 83 FF 01                     cmp r15d, 1
0047DBD1  0F 85 D8 00 00 00               jne 0x14047dcaf
0047DBD7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0047DBE0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0047DBE7  48 8B 05 9A 24 9B 00            mov rax, qword ptr [rip + 0x9b249a]
0047DBEE  0F B7 91 AE 04 00 00            movzx edx, word ptr [rcx + 0x4ae]
0047DBF5  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
0047DBF9  8A 81 5C 48 00 00               mov al, byte ptr [rcx + 0x485c]
0047DBFF  48 81 C1 80 49 00 00            add rcx, 0x4980
0047DC06  F6 D8                           neg al
0047DC08  48 1B FF                        sbb rdi, rdi
0047DC0B  48 23 F9                        and rdi, rcx
0047DC0E  E9 19 FD FF FF                  jmp 0x14047d92c
0047DC13  BE 4C 00 00 C0                  mov esi, 0xc000004c
0047DC18  E9 1F FE FF FF                  jmp 0x14047da3c
0047DC1D  BE 0A 01 00 C0                  mov esi, 0xc000010a
0047DC22  E9 15 FE FF FF                  jmp 0x14047da3c
0047DC27  4D 8B C6                        mov r8, r14
0047DC2A  49 8B CD                        mov rcx, r13
0047DC2D  E8 8E 02 00 00                  call 0x14047dec0
0047DC32  8B F0                           mov esi, eax
0047DC34  85 C0                           test eax, eax
0047DC36  0F 89 7D FE FF FF               jns 0x14047dab9
0047DC3C  E9 FB FD FF FF                  jmp 0x14047da3c
0047DC41  48 8D 0D 78 98 9B 00            lea rcx, [rip + 0x9b9878]
0047DC48  44 8B F3                        mov r14d, ebx
0047DC4B  E8 30 B2 DC FF                  call 0x140248e80
0047DC50  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
0047DC56  89 85 88 00 00 00               mov dword ptr [rbp + 0x88], eax
0047DC5C  41 F6 C4 04                     test r12b, 4
0047DC60  0F 84 B4 00 00 00               je 0x14047dd1a
0047DC66  0C 80                           or al, 0x80
0047DC68  41 BE 01 00 00 00               mov r14d, 1
0047DC6E  88 85 88 00 00 00               mov byte ptr [rbp + 0x88], al
0047DC74  41 F6 C4 01                     test r12b, 1
0047DC78  0F 84 AD 00 00 00               je 0x14047dd2b
0047DC7E  0C 40                           or al, 0x40
0047DC80  88 85 88 00 00 00               mov byte ptr [rbp + 0x88], al
0047DC86  0F B7 85 88 00 00 00            movzx eax, word ptr [rbp + 0x88]
0047DC8D  66 89 87 B8 00 00 00            mov word ptr [rdi + 0xb8], ax
0047DC94  48 8D 0D 25 98 9B 00            lea rcx, [rip + 0x9b9825]
0047DC9B  E8 40 BB DC FF                  call 0x1402497e0
0047DCA0  E9 97 FD FF FF                  jmp 0x14047da3c
0047DCA5  BB 0A 01 00 C0                  mov ebx, 0xc000010a
0047DCAA  E9 FE FE FF FF                  jmp 0x14047dbad
0047DCAF  41 8B CF                        mov ecx, r15d
0047DCB2  E8 0D 2C E4 FF                  call 0x1402c08c4
0047DCB7  48 8B F8                        mov rdi, rax
0047DCBA  E9 6D FC FF FF                  jmp 0x14047d92c
0047DCBF  4C 8B 77 78                     mov r14, qword ptr [rdi + 0x78]
0047DCC3  E9 D8 FC FF FF                  jmp 0x14047d9a0
0047DCC8  BE 61 00 00 C0                  mov esi, 0xc0000061
0047DCCD  E9 6A FD FF FF                  jmp 0x14047da3c
0047DCD2  45 85 FF                        test r15d, r15d
0047DCD5  0F 85 C5 6E 27 00               jne 0x1406f4ba0
0047DCDB  4D 8B C6                        mov r8, r14
0047DCDE  49 8B CD                        mov rcx, r13
0047DCE1  E8 A6 01 00 00                  call 0x14047de8c
0047DCE6  90                              nop
0047DCE7  E9 B4 6E 27 00                  jmp 0x1406f4ba0
0047DCEC  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
0047DCF3  BE 4C 00 00 C0                  mov esi, 0xc000004c
0047DCF8  38 18                           cmp byte ptr [rax], bl
0047DCFA  0F 84 3C FD FF FF               je 0x14047da3c
0047DD00  45 85 FF                        test r15d, r15d
0047DD03  0F 85 A1 6E 27 00               jne 0x1406f4baa
0047DD09  4D 8B C6                        mov r8, r14
0047DD0C  49 8B CD                        mov rcx, r13
0047DD0F  E8 78 01 00 00                  call 0x14047de8c
0047DD14  90                              nop
0047DD15  E9 90 6E 27 00                  jmp 0x1406f4baa
0047DD1A  41 F6 C4 08                     test r12b, 8
0047DD1E  0F 84 50 FF FF FF               je 0x14047dc74
0047DD24  24 7F                           and al, 0x7f
0047DD26  E9 3D FF FF FF                  jmp 0x14047dc68
0047DD2B  41 F6 C4 02                     test r12b, 2
0047DD2F  0F 84 88 6E 27 00               je 0x1406f4bbd
0047DD35  24 BF                           and al, 0xbf
0047DD37  E9 44 FF FF FF                  jmp 0x14047dc80
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAdjustWorkingSetSizeEx(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, unsigned int a5, unsigned __int16 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p69;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (288);
    v_rbx = 0;
    *(unsigned __int8 *)(a6) = 0;
    if (a3 != 0) goto loc_0047DBC0;
loc_0047D92C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 == 0) goto loc_0047DAFE;
    v_r12 = (v_r12) | (-1);
    if (a1 == v_r12) goto loc_0047DB08;
loc_0047D942:
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10168120) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 174) * 8);
    result = MiLockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, a3, a4);
    v_stack_p18 = (unsigned __int8)(result);
    result = MiLockWorkingSetCoreExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, a3, a4);
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_0047D981;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) & (32)) != 0) goto loc_0047DC1D;
loc_0047D981:
    if (a1 == 0) goto loc_0047DA91;
    v_rsi = (a1) >> (12);
loc_0047D98E:
    v_stack_m120 = v_rsi;
    if (a2 == 0) goto loc_0047DCBF;
    v_r14 = (a2) >> (12);
loc_0047D9A0:
    v_stack_m128 = v_r14;
    v_stack_m138 = 0;
    result = MiCheckWsLimits(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_stack_m120, v_stack_m128, (unsigned int)((unsigned int)((unsigned int)(a5))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_0047DA3C;
    v_stack_m110 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 16);
    if (v_stack_m120 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 112))) goto loc_0047DA9A;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 112)) - (v_stack_m120);
    if (v_stack_m120 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 16) + 32))) goto loc_0047DC13;
loc_0047DA04:
    if (v_stack_m128 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 128))) goto loc_0047DADE;
loc_0047DA16:
    if ((*(unsigned __int8 *)(a6)) == 0) goto loc_0047DA6D;
loc_0047DA21:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 120) = v_stack_m128;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 112) = v_stack_m120;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_0047DC41;
loc_0047DA3C:
    result = MiUnlockWorkingSetCoreExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_stack_m120, v_stack_m128, (unsigned int)((unsigned int)((unsigned int)(a5))));
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_stack_p18, v_stack_m128, (unsigned int)((unsigned int)((unsigned int)(a5))));
loc_0047DA51:
    v_rsp = (v_rsp) + (288);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0047DA6D:
    if (result == 0) goto loc_0047DA21;
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    if ((unsigned int)((unsigned int)(a3)) == 0) {
        a3 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
        result = PsReturnProcessQuota(a1, v_stack_p18, a3, (unsigned int)((unsigned int)((unsigned int)(a5))));
    }
    result = MiReturnResident(v_stack_p40, result, a3, (unsigned int)((unsigned int)((unsigned int)(a5))));
    goto loc_0047DA21;
loc_0047DA91:
    goto loc_0047D98E;
loc_0047DA9A:
    v_r14 = (result) - (result);
    *(unsigned __int8 *)(a6) = 1;
    if (v_stack_p20 == ((unsigned __int8)(v_stack_p8))) goto loc_0047DCC8;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_0047DC27;
loc_0047DAB9:
    result = MiChargeResident(v_stack_p40, v_r14, 512, (unsigned int)((unsigned int)((unsigned int)(a5))));
    if ((unsigned int)(result) == 0) goto loc_0047DCD2;
    goto loc_0047DA04;
loc_0047DADE:
    result = (*(unsigned __int64 *)(v_stack_p48 + 32)) + (6);
    if (result >= v_stack_p30) goto loc_0047DCEC;
    goto loc_0047DA16;
loc_0047DAFE:
    goto loc_0047DA51;
loc_0047DB08:
    if (v_r14 != ((unsigned int)(a5))) goto loc_0047D942;
    a2 = 0;
    v_stack_p50 = v_xmm0;
    result = memset(v_stack_p60, a2, 192, (unsigned int)((unsigned int)((unsigned int)(a5))));
    v_stack_p60 = 6;
    v_stack_m40 = v_stack_p50;
    v_stack_mD8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_stack_m50 = v_rip - 2344838;
    v_stack_m48 = v_rip - 69317;
    v_stack_mD0 = v_stack_p8;
    v_stack_mC8 = (unsigned int)(a5);
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, 192, (unsigned int)((unsigned int)((unsigned int)(a5))));
    v_stack_p69 = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024 + 184)))) & (15)) != 0) goto loc_0047DB92;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) & (32)) != 0) goto loc_0047DCA5;
loc_0047DB92:
    a4 = 0;
    v_stack_p20 = 64;
    result = MiTrimWorkingSet(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned int)(a5), v_stack_p69, a4);
loc_0047DBAD:
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_stack_p69, v_stack_p69, a4);
    goto loc_0047DA51;
loc_0047DBC0:
    if (((unsigned int)(v_stack_p69 - 1)) > 3) goto loc_0047DAFE;
    if (((unsigned int)((unsigned int)(a3))) != 1) goto loc_0047DCAF;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10167450) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)) + (0x4980ULL);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10167450) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8) + 18524)));
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024) & (a1);
    goto loc_0047D92C;
loc_0047DC13:
    goto loc_0047DA3C;
loc_0047DC1D:
    goto loc_0047DA3C;
loc_0047DC27:
    result = PsChargeProcessQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), v_r14, a4);
    if (!sign_flag) goto loc_0047DAB9;
    goto loc_0047DA3C;
loc_0047DC41:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10197112, *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), v_r14, a4);
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 184)));
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) == 0) goto loc_0047DD1A;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rdi + 184))) | (128));
loc_0047DC68:
    v_stack_p30 = (unsigned __int8)(result);
loc_0047DC74:
    if ((((unsigned __int8)((unsigned int)(a5))) & (1)) == 0) goto loc_0047DD2B;
    result = (unsigned __int8)((result) | (64));
loc_0047DC80:
    v_stack_p30 = (unsigned __int8)(result);
    *(unsigned __int16 *)(v_rdi + 184) = a6;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10197029, *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), v_r14, a4);
    goto loc_0047DA3C;
loc_0047DCA5:
    goto loc_0047DBAD;
loc_0047DCAF:
    result = MiMapWorkingSetTypeToVm((unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), v_r14, a4);
    goto loc_0047D92C;
loc_0047DCBF:
    goto loc_0047D9A0;
loc_0047DCC8:
    goto loc_0047DA3C;
loc_0047DCD2:
    result = PsReturnProcessQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), *(unsigned __int64 *)(result + 120), a4);
loc_0047DCEC:
    if ((*(unsigned __int8 *)(a6)) == ((unsigned __int8)((unsigned int)(0xC000010AULL)))) goto loc_0047DA3C;
    result = PsReturnProcessQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198), *(unsigned __int64 *)(result + 120), a4);
loc_0047DD1A:
    if ((((unsigned __int8)((unsigned int)(a5))) & (8)) == 0) goto loc_0047DC74;
    result = (unsigned __int8)((result) & (127));
    goto loc_0047DC68;
loc_0047DD2B:
    result = (unsigned __int8)((result) & (191));
    goto loc_0047DC80;
}
```

## 5. (Beta) C Style

```c
int64_t MmAdjustWorkingSetSizeEx(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m138;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint8_t v_stack_p69;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (288);
    local_rbx = 0;
    *(uint8_t *)(arg6) = 0;
    if (Arg3 != 0) goto loc_0047DBC0;
loc_0047D92C:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024 == 0) goto loc_0047DAFE;
    local_r12 = (local_r12) | (-1);
    if (Arg1 == local_r12) goto loc_0047DB08;
loc_0047D942:
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x9B2738) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xAE) * 8);
    result = MiLockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, Arg3, Arg4);
    v_stack_p18 = (uint8_t)(result);
    result = MiLockWorkingSetCoreExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_0047D981;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) & (32)) != 0) goto loc_0047DC1D;
loc_0047D981:
    if (Arg1 == 0) goto loc_0047DA91;
    local_rsi = (Arg1) >> (12);
loc_0047D98E:
    v_stack_m120 = local_rsi;
    if (Arg2 == 0) goto loc_0047DCBF;
    local_r14 = (Arg2) >> (12);
loc_0047D9A0:
    v_stack_m128 = local_r14;
    v_stack_m138 = 0;
    result = MiCheckWsLimits(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_stack_m120, v_stack_m128, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_0047DA3C;
    v_stack_m110 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x10);
    if (v_stack_m120 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x70))) goto loc_0047DA9A;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x70)) - (v_stack_m120);
    if (v_stack_m120 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x10) + 0x20))) goto loc_0047DC13;
loc_0047DA04:
    if (v_stack_m128 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x80))) goto loc_0047DADE;
loc_0047DA16:
    if ((*(uint8_t *)(arg6)) == 0) goto loc_0047DA6D;
loc_0047DA21:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x78) = v_stack_m128;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0x70) = v_stack_m120;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_0047DC41;
loc_0047DA3C:
    result = MiUnlockWorkingSetCoreExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_stack_m120, v_stack_m128, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_stack_p18, v_stack_m128, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
loc_0047DA51:
    local_rsp = (local_rsp) + (288);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0047DA6D:
    if (result == 0) goto loc_0047DA21;
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    if ((uint32_t)((uint32_t)(Arg3)) == 0) {
        Arg3 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
        result = PsReturnProcessQuota(Arg1, v_stack_p18, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    }
    result = MiReturnResident(v_stack_p40, result, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    goto loc_0047DA21;
loc_0047DA91:
    goto loc_0047D98E;
loc_0047DA9A:
    local_r14 = (result) - (result);
    *(uint8_t *)(arg6) = 1;
    if (v_stack_p20 == ((uint8_t)(v_stack_p8))) goto loc_0047DCC8;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_0047DC27;
loc_0047DAB9:
    result = MiChargeResident(v_stack_p40, local_r14, 512, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    if ((uint32_t)(result) == 0) goto loc_0047DCD2;
    goto loc_0047DA04;
loc_0047DADE:
    result = (*(uint64_t *)(v_stack_p48 + 0x20)) + (6);
    if (result >= v_stack_p30) goto loc_0047DCEC;
    goto loc_0047DA16;
loc_0047DAFE:
    goto loc_0047DA51;
loc_0047DB08:
    if (local_r14 != ((uint32_t)(Arg5))) goto loc_0047D942;
    Arg2 = 0;
    v_stack_p50 = v_xmm0;
    result = memset(v_stack_p60, Arg2, 192, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    v_stack_p60 = 6;
    v_stack_m40 = v_stack_p50;
    v_stack_mD8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    v_stack_m50 = v_rip - 2344838;
    v_stack_m48 = v_rip - 69317;
    v_stack_mD0 = v_stack_p8;
    v_stack_mC8 = (uint32_t)(Arg5);
    result = MiLockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, 192, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    v_stack_p69 = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x400 + 0xB8)))) & (15)) != 0) goto loc_0047DB92;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) & (32)) != 0) goto loc_0047DCA5;
loc_0047DB92:
    Arg4 = 0;
    v_stack_p20 = 64;
    result = MiTrimWorkingSet(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint32_t)(Arg5), v_stack_p69, Arg4);
loc_0047DBAD:
    result = MiUnlockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_stack_p69, v_stack_p69, Arg4);
    goto loc_0047DA51;
loc_0047DBC0:
    if (((uint32_t)(v_stack_p69 - 1)) > 3) goto loc_0047DAFE;
    if (((uint32_t)((uint32_t)(Arg3))) != 1) goto loc_0047DCAF;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9B249A) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)) + (0x4980ULL);
    result = (uint8_t)(-(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x9B249A) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8) + 0x485C)));
    local_rdi = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024) & (Arg1);
    goto loc_0047D92C;
loc_0047DC13:
    goto loc_0047DA3C;
loc_0047DC1D:
    goto loc_0047DA3C;
loc_0047DC27:
    result = PsChargeProcessQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), local_r14, Arg4);
    if (!sign_flag) goto loc_0047DAB9;
    goto loc_0047DA3C;
loc_0047DC41:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 10197112, *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), local_r14, Arg4);
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB8)));
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) == 0) goto loc_0047DD1A;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xB8))) | (128));
loc_0047DC68:
    v_stack_p30 = (uint8_t)(result);
loc_0047DC74:
    if ((((uint8_t)((uint32_t)(Arg5))) & (1)) == 0) goto loc_0047DD2B;
    result = (uint8_t)((result) | (64));
loc_0047DC80:
    v_stack_p30 = (uint8_t)(result);
    *(uint16_t *)(local_rdi + 0xB8) = Arg6;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 10197029, *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), local_r14, Arg4);
    goto loc_0047DA3C;
loc_0047DCA5:
    goto loc_0047DBAD;
loc_0047DCAF:
    result = MiMapWorkingSetTypeToVm((uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), local_r14, Arg4);
    goto loc_0047D92C;
loc_0047DCBF:
    goto loc_0047D9A0;
loc_0047DCC8:
    goto loc_0047DA3C;
loc_0047DCD2:
    result = PsReturnProcessQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), *(uint64_t *)(result + 0x78), Arg4);
loc_0047DCEC:
    if ((*(uint8_t *)(arg6)) == ((uint8_t)((uint32_t)(0xC000010AULL)))) goto loc_0047DA3C;
    result = PsReturnProcessQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE), *(uint64_t *)(result + 0x78), Arg4);
loc_0047DD1A:
    if ((((uint8_t)((uint32_t)(Arg5))) & (8)) == 0) goto loc_0047DC74;
    result = (uint8_t)((result) & (127));
    goto loc_0047DC68;
loc_0047DD2B:
    result = (uint8_t)((result) & (191));
    goto loc_0047DC80;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `8` | `R` |
| `Arg6` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047D8D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
