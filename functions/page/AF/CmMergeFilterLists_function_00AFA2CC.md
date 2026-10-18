# CmMergeFilterLists

- RVA: `0x00AFA2CC`–`0x00AFA5FC` (길이 `816` bytes)
- VA: `0x0000000140AFA2CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DAAC8`
- 디코드: `247`개 명령, `816/816` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AFA308` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA348` → [CmFindFilterListInflectionPoint](../AC/CmFindFilterListInflectionPoint_function_00ACC9D8.md) (function, `0x00ACC9D8`)
- `0x00AFA375` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AFA38A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AFA3C8` → [PnpMultiSzAppend](../9D/PnpMultiSzAppend_function_009D04D8.md) (function, `0x009D04D8`)
- `0x00AFA3DF` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA3EF` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA46A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AFA4AB` → [PnpMultiSzAppend](../9D/PnpMultiSzAppend_function_009D04D8.md) (function, `0x009D04D8`)
- `0x00AFA4C2` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA4D2` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA536` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AFA57C` → [PnpMultiSzAppend](../9D/PnpMultiSzAppend_function_009D04D8.md) (function, `0x009D04D8`)
- `0x00AFA595` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)
- `0x00AFA5A5` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (function, `0x006A2DE8`)

### Direct callers
- [CmGetInstallerClassCompoundFiltersWorker](../83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x0083065B`
- [CmGetDeviceCompoundFiltersWorker](CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AFA223`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00AFA308` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA375` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AFA38A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AFA3DF` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA3EF` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA46A` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AFA4C2` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA4D2` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA536` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AFA595` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
  - `0x00AFA5A5` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline_function_006A2DE8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AFA2CC  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00AFA2D1  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00AFA2D6  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00AFA2DB  55                              push rbp
00AFA2DC  53                              push rbx
00AFA2DD  56                              push rsi
00AFA2DE  57                              push rdi
00AFA2DF  41 54                           push r12
00AFA2E1  41 55                           push r13
00AFA2E3  41 56                           push r14
00AFA2E5  41 57                           push r15
00AFA2E7  48 8B EC                        mov rbp, rsp
00AFA2EA  48 83 EC 38                     sub rsp, 0x38
00AFA2EE  33 C0                           xor eax, eax
00AFA2F0  49 8B F9                        mov rdi, r9
00AFA2F3  44 8B E8                        mov r13d, eax
00AFA2F6  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00AFA2FA  8B D8                           mov ebx, eax
00AFA2FC  44 8B F8                        mov r15d, eax
00AFA2FF  44 8B F0                        mov r14d, eax
00AFA302  4C 8B E2                        mov r12, rdx
00AFA305  48 8B F1                        mov rsi, rcx
00AFA308  E8 DB 8A BA FF                  call 0x1406a2de8
00AFA30D  33 C9                           xor ecx, ecx
00AFA30F  85 C0                           test eax, eax
00AFA311  74 06                           je 0x140afa319
00AFA313  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00AFA317  89 08                           mov dword ptr [rax], ecx
00AFA319  48 85 FF                        test rdi, rdi
00AFA31C  74 20                           je 0x140afa33e
00AFA31E  83 7D 68 02                     cmp dword ptr [rbp + 0x68], 2
00AFA322  72 10                           jb 0x140afa334
00AFA324  44 8B 75 68                     mov r14d, dword ptr [rbp + 0x68]
00AFA328  48 8B DF                        mov rbx, rdi
00AFA32B  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00AFA32F  66 89 0F                        mov word ptr [rdi], cx
00AFA332  EB 0A                           jmp 0x140afa33e
00AFA334  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00AFA338  EB 04                           jmp 0x140afa33e
00AFA33A  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
00AFA33E  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
00AFA342  49 8B D4                        mov rdx, r12
00AFA345  48 8B CE                        mov rcx, rsi
00AFA348  E8 8B 26 FD FF                  call 0x140acc9d8
00AFA34D  48 8B F0                        mov rsi, rax
00AFA350  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00AFA354  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AFA358  33 C9                           xor ecx, ecx
00AFA35A  48 8B F8                        mov rdi, rax
00AFA35D  66 39 08                        cmp word ptr [rax], cx
00AFA360  0F 84 BD 00 00 00               je 0x140afa423
00AFA366  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
00AFA36A  48 85 F6                        test rsi, rsi
00AFA36D  74 15                           je 0x140afa384
00AFA36F  48 8B D6                        mov rdx, rsi
00AFA372  48 8B CF                        mov rcx, rdi
00AFA375  E8 06 5D A0 FF                  call 0x140500080
00AFA37A  33 C9                           xor ecx, ecx
00AFA37C  85 C0                           test eax, eax
00AFA37E  0F 84 9B 00 00 00               je 0x140afa41f
00AFA384  49 8B D4                        mov rdx, r12
00AFA387  48 8B CF                        mov rcx, rdi
00AFA38A  E8 F1 5C A0 FF                  call 0x140500080
00AFA38F  33 C9                           xor ecx, ecx
00AFA391  85 C0                           test eax, eax
00AFA393  74 6C                           je 0x140afa401
00AFA395  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AFA399  48 FF C0                        inc rax
00AFA39C  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA3A0  75 F7                           jne 0x140afa399
00AFA3A2  45 8D 3C 47                     lea r15d, [r15 + rax*2]
00AFA3A6  41 83 C7 02                     add r15d, 2
00AFA3AA  8D 34 45 02 00 00 00            lea esi, [rax*2 + 2]
00AFA3B1  48 85 DB                        test rbx, rbx
00AFA3B4  74 47                           je 0x140afa3fd
00AFA3B6  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00AFA3BA  44 89 75 60                     mov dword ptr [rbp + 0x60], r14d
00AFA3BE  4C 8B C7                        mov r8, rdi
00AFA3C1  48 8D 55 60                     lea rdx, [rbp + 0x60]
00AFA3C5  48 8B CB                        mov rcx, rbx
00AFA3C8  E8 0B 61 ED FF                  call 0x1409d04d8
00AFA3CD  33 DB                           xor ebx, ebx
00AFA3CF  84 C0                           test al, al
00AFA3D1  75 0C                           jne 0x140afa3df
00AFA3D3  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00AFA3D7  41 BD 23 00 00 C0               mov r13d, 0xc0000023
00AFA3DD  EB 10                           jmp 0x140afa3ef
00AFA3DF  E8 04 8A BA FF                  call 0x1406a2de8
00AFA3E4  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00AFA3E8  85 C0                           test eax, eax
00AFA3EA  74 03                           je 0x140afa3ef
00AFA3EC  44 2B F6                        sub r14d, esi
00AFA3EF  E8 F4 89 BA FF                  call 0x1406a2de8
00AFA3F4  33 C9                           xor ecx, ecx
00AFA3F6  85 C0                           test eax, eax
00AFA3F8  75 03                           jne 0x140afa3fd
00AFA3FA  44 2B F6                        sub r14d, esi
00AFA3FD  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
00AFA401  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AFA405  48 FF C0                        inc rax
00AFA408  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA40C  75 F7                           jne 0x140afa405
00AFA40E  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00AFA412  48 83 C7 02                     add rdi, 2
00AFA416  66 39 0F                        cmp word ptr [rdi], cx
00AFA419  0F 85 4B FF FF FF               jne 0x140afa36a
00AFA41F  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
00AFA423  48 89 7D 48                     mov qword ptr [rbp + 0x48], rdi
00AFA427  66 39 0F                        cmp word ptr [rdi], cx
00AFA42A  74 18                           je 0x140afa444
00AFA42C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AFA430  48 FF C0                        inc rax
00AFA433  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA437  75 F7                           jne 0x140afa430
00AFA439  48 FF C0                        inc rax
00AFA43C  48 8D 04 47                     lea rax, [rdi + rax*2]
00AFA440  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00AFA444  4D 85 E4                        test r12, r12
00AFA447  0F 84 D9 00 00 00               je 0x140afa526
00AFA44D  49 8B FC                        mov rdi, r12
00AFA450  66 41 39 0C 24                  cmp word ptr [r12], cx
00AFA455  0F 84 A6 00 00 00               je 0x140afa501
00AFA45B  49 83 CC FF                     or r12, 0xffffffffffffffff
00AFA45F  48 85 F6                        test rsi, rsi
00AFA462  74 15                           je 0x140afa479
00AFA464  48 8B D6                        mov rdx, rsi
00AFA467  48 8B CF                        mov rcx, rdi
00AFA46A  E8 11 5C A0 FF                  call 0x140500080
00AFA46F  33 C9                           xor ecx, ecx
00AFA471  85 C0                           test eax, eax
00AFA473  0F 84 88 00 00 00               je 0x140afa501
00AFA479  49 8B C4                        mov rax, r12
00AFA47C  48 FF C0                        inc rax
00AFA47F  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA483  75 F7                           jne 0x140afa47c
00AFA485  45 8D 3C 47                     lea r15d, [r15 + rax*2]
00AFA489  41 83 C7 02                     add r15d, 2
00AFA48D  8D 34 45 02 00 00 00            lea esi, [rax*2 + 2]
00AFA494  48 85 DB                        test rbx, rbx
00AFA497  74 47                           je 0x140afa4e0
00AFA499  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00AFA49D  44 89 75 60                     mov dword ptr [rbp + 0x60], r14d
00AFA4A1  4C 8B C7                        mov r8, rdi
00AFA4A4  48 8D 55 60                     lea rdx, [rbp + 0x60]
00AFA4A8  48 8B CB                        mov rcx, rbx
00AFA4AB  E8 28 60 ED FF                  call 0x1409d04d8
00AFA4B0  33 DB                           xor ebx, ebx
00AFA4B2  84 C0                           test al, al
00AFA4B4  75 0C                           jne 0x140afa4c2
00AFA4B6  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00AFA4BA  41 BD 23 00 00 C0               mov r13d, 0xc0000023
00AFA4C0  EB 10                           jmp 0x140afa4d2
00AFA4C2  E8 21 89 BA FF                  call 0x1406a2de8
00AFA4C7  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00AFA4CB  85 C0                           test eax, eax
00AFA4CD  74 03                           je 0x140afa4d2
00AFA4CF  44 2B F6                        sub r14d, esi
00AFA4D2  E8 11 89 BA FF                  call 0x1406a2de8
00AFA4D7  33 C9                           xor ecx, ecx
00AFA4D9  85 C0                           test eax, eax
00AFA4DB  75 03                           jne 0x140afa4e0
00AFA4DD  44 2B F6                        sub r14d, esi
00AFA4E0  49 8B C4                        mov rax, r12
00AFA4E3  48 FF C0                        inc rax
00AFA4E6  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA4EA  75 F7                           jne 0x140afa4e3
00AFA4EC  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
00AFA4F0  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00AFA4F4  48 83 C7 02                     add rdi, 2
00AFA4F8  66 39 0F                        cmp word ptr [rdi], cx
00AFA4FB  0F 85 5E FF FF FF               jne 0x140afa45f
00AFA501  4C 8B E7                        mov r12, rdi
00AFA504  48 89 7D 50                     mov qword ptr [rbp + 0x50], rdi
00AFA508  66 39 0F                        cmp word ptr [rdi], cx
00AFA50B  74 19                           je 0x140afa526
00AFA50D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AFA511  48 FF C0                        inc rax
00AFA514  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00AFA518  75 F7                           jne 0x140afa511
00AFA51A  4C 8D 60 01                     lea r12, [rax + 1]
00AFA51E  4E 8D 24 67                     lea r12, [rdi + r12*2]
00AFA522  4C 89 65 50                     mov qword ptr [rbp + 0x50], r12
00AFA526  48 85 F6                        test rsi, rsi
00AFA529  0F 84 8F 00 00 00               je 0x140afa5be
00AFA52F  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00AFA533  48 8B CE                        mov rcx, rsi
00AFA536  E8 45 5B A0 FF                  call 0x140500080
00AFA53B  33 C9                           xor ecx, ecx
00AFA53D  85 C0                           test eax, eax
00AFA53F  0F 84 F5 FD FF FF               je 0x140afa33a
00AFA545  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AFA549  48 FF C0                        inc rax
00AFA54C  66 39 0C 46                     cmp word ptr [rsi + rax*2], cx
00AFA550  75 F7                           jne 0x140afa549
00AFA552  45 8D 3C 47                     lea r15d, [r15 + rax*2]
00AFA556  41 83 C7 02                     add r15d, 2
00AFA55A  8D 3C 45 02 00 00 00            lea edi, [rax*2 + 2]
00AFA561  48 85 DB                        test rbx, rbx
00AFA564  0F 84 D0 FD FF FF               je 0x140afa33a
00AFA56A  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00AFA56E  44 89 75 60                     mov dword ptr [rbp + 0x60], r14d
00AFA572  4C 8B C6                        mov r8, rsi
00AFA575  48 8D 55 60                     lea rdx, [rbp + 0x60]
00AFA579  48 8B CB                        mov rcx, rbx
00AFA57C  E8 57 5F ED FF                  call 0x1409d04d8
00AFA581  33 F6                           xor esi, esi
00AFA583  84 C0                           test al, al
00AFA585  75 0E                           jne 0x140afa595
00AFA587  8B DE                           mov ebx, esi
00AFA589  41 BD 23 00 00 C0               mov r13d, 0xc0000023
00AFA58F  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00AFA593  EB 10                           jmp 0x140afa5a5
00AFA595  E8 4E 88 BA FF                  call 0x1406a2de8
00AFA59A  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00AFA59E  85 C0                           test eax, eax
00AFA5A0  74 03                           je 0x140afa5a5
00AFA5A2  44 2B F7                        sub r14d, edi
00AFA5A5  E8 3E 88 BA FF                  call 0x1406a2de8
00AFA5AA  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
00AFA5AE  85 C0                           test eax, eax
00AFA5B0  0F 85 88 FD FF FF               jne 0x140afa33e
00AFA5B6  44 2B F7                        sub r14d, edi
00AFA5B9  E9 7C FD FF FF                  jmp 0x140afa33a
00AFA5BE  45 85 FF                        test r15d, r15d
00AFA5C1  75 08                           jne 0x140afa5cb
00AFA5C3  41 BD 25 02 00 C0               mov r13d, 0xc0000225
00AFA5C9  EB 1C                           jmp 0x140afa5e7
00AFA5CB  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00AFA5CF  41 83 C7 02                     add r15d, 2
00AFA5D3  44 89 38                        mov dword ptr [rax], r15d
00AFA5D6  48 85 DB                        test rbx, rbx
00AFA5D9  74 06                           je 0x140afa5e1
00AFA5DB  44 39 7D 68                     cmp dword ptr [rbp + 0x68], r15d
00AFA5DF  73 06                           jae 0x140afa5e7
00AFA5E1  41 BD 23 00 00 C0               mov r13d, 0xc0000023
00AFA5E7  41 8B C5                        mov eax, r13d
00AFA5EA  48 83 C4 38                     add rsp, 0x38
00AFA5EE  41 5F                           pop r15
00AFA5F0  41 5E                           pop r14
00AFA5F2  41 5D                           pop r13
00AFA5F4  41 5C                           pop r12
00AFA5F6  5F                              pop rdi
00AFA5F7  5E                              pop rsi
00AFA5F8  5B                              pop rbx
00AFA5F9  5D                              pop rbp
00AFA5FA  C3                              ret
00AFA5FB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmMergeFilterLists(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
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
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (56);
    result = 0;
    v_stack_m58 = 0;
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a1 = 0;
    if ((unsigned int)(result) != 0) {
        result = a6;
        *(unsigned int *)(result) = 0;
    }
    if (a4 == 0) goto loc_00AFA33E;
    if (a5 < 2) goto loc_00AFA334;
    v_stack_m58 = a4;
    *(unsigned __int16 *)(a4) = 0;
    goto loc_00AFA33E;
loc_00AFA334:
    v_stack_m58 = 0;
    goto loc_00AFA33E;
loc_00AFA33A:
loc_00AFA33E:
    result = CmFindFilterListInflectionPoint(v_stack_p8, a2, v_stack_p18, a4);
    v_stack_m50 = result;
    a1 = 0;
    if ((*(unsigned __int16 *)(v_stack_p8)) == 0) goto loc_00AFA423;
loc_00AFA36A:
    if (result == 0) goto loc_00AFA384;
    result = wcsicmp(v_stack_p8, result, v_stack_p18, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AFA41F;
loc_00AFA384:
    result = wcsicmp(v_stack_p8, v_stack_p18, v_stack_p18, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AFA401;
    result = (result) | (-1);
loc_00AFA399:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_p8 + result * 2)) != 0) goto loc_00AFA399;
    v_r15 = (unsigned int)((0 + result * 2) + (2));
    if (a4 == 0) goto loc_00AFA3FD;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = PnpMultiSzAppend(a4, v_stack_p20, v_stack_p8, v_stack_m58);
    v_rbx = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AFA3DF;
    v_stack_m58 = 0;
    goto loc_00AFA3EF;
loc_00AFA3DF:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(a4, v_stack_p20, v_stack_p8, v_stack_m58);
    v_r14 = (unsigned int)(a5);
    if ((unsigned int)(result) != 0) {
        v_r14 = (unsigned int)(((unsigned int)(a5)) - ((unsigned int)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(a4, v_stack_p20, v_stack_p8, v_stack_m58);
    a1 = 0;
    if ((unsigned int)(result) == 0) {
        v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result * 2 + 2)));
    }
loc_00AFA401:
    result = (result) | (-1);
loc_00AFA405:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_p8 + result * 2)) != 0) goto loc_00AFA405;
    v_rdi = (v_stack_p8 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_00AFA36A;
loc_00AFA41F:
loc_00AFA423:
    v_stack_p8 = v_rdi;
    if ((*(unsigned __int16 *)(v_rdi)) == 0) goto loc_00AFA444;
    result = (result) | (-1);
loc_00AFA430:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rdi + result * 2)) != 0) goto loc_00AFA430;
    result = (result) + 1;
    v_stack_p8 = v_rdi + result * 2;
loc_00AFA444:
    if (v_stack_p10 == 0) goto loc_00AFA526;
    if ((*(unsigned __int16 *)(v_stack_p10)) == 0) goto loc_00AFA501;
    v_r12 = (v_stack_p10) | (-1);
loc_00AFA45F:
    if (v_stack_m50 == 0) goto loc_00AFA479;
    result = wcsicmp(v_stack_p10, v_stack_m50, v_stack_p8, v_stack_m58);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AFA501;
loc_00AFA479:
loc_00AFA47C:
    result = (v_r12) + 1;
    if ((*(unsigned __int16 *)(v_stack_p10 + result * 2)) != 0) goto loc_00AFA47C;
    v_r15 = (unsigned int)((v_r15 + result * 2) + (2));
    if (v_stack_m58 == 0) goto loc_00AFA4E0;
    v_stack_p20 = (unsigned int)(v_r14);
    result = PnpMultiSzAppend(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    v_rbx = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AFA4C2;
    v_stack_m58 = 0;
    goto loc_00AFA4D2;
loc_00AFA4C2:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    if ((unsigned int)(result) != 0) {
        v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    a1 = 0;
    if ((unsigned int)(result) == 0) {
        v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result * 2 + 2)));
    }
loc_00AFA4E3:
    result = (v_r12) + 1;
    if ((*(unsigned __int16 *)(v_stack_p10 + result * 2)) != 0) goto loc_00AFA4E3;
    v_rdi = (v_stack_p10 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_00AFA45F;
loc_00AFA501:
    v_stack_p10 = v_rdi;
    if ((*(unsigned __int16 *)(v_rdi)) == 0) goto loc_00AFA526;
    result = (result) | (-1);
loc_00AFA511:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rdi + result * 2)) != 0) goto loc_00AFA511;
    v_stack_p10 = v_rdi + result + 1 * 2;
loc_00AFA526:
    if (v_stack_m50 == 0) goto loc_00AFA5BE;
    result = wcsicmp(v_stack_m50, v_stack_p18, v_stack_p10, v_stack_m58);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AFA33A;
    result = (result) | (-1);
loc_00AFA549:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m50 + result * 2)) != 0) goto loc_00AFA549;
    v_r15 = (unsigned int)((v_r15 + result * 2) + (2));
    if (v_stack_m58 == 0) goto loc_00AFA33A;
    v_stack_p20 = (unsigned int)(v_r14);
    result = PnpMultiSzAppend(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    v_rsi = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AFA595;
    v_stack_m58 = 0;
    goto loc_00AFA5A5;
loc_00AFA595:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    if ((unsigned int)(result) != 0) {
        v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    if ((unsigned int)(result) != 0) goto loc_00AFA33E;
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result * 2 + 2)));
    goto loc_00AFA33A;
loc_00AFA5BE:
    if ((unsigned int)(v_r15) != 0) goto loc_00AFA5CB;
    goto loc_00AFA5E7;
loc_00AFA5CB:
    v_r15 = (unsigned int)((v_r15) + (2));
    *(unsigned int *)(a6) = (unsigned int)(v_r15);
    if (v_stack_m58 == 0) goto loc_00AFA5E1;
    v_r13 = (unsigned int)(0xC0000225ULL);
    if (a5 < ((unsigned int)(v_r15))) {
        v_r13 = 0xC0000023ULL;
    }
    v_rsp = (v_rsp) + (56);
    return (unsigned int)((unsigned int)(v_r13));
}
```

## 5. (Beta) C Style

```c
int64_t CmMergeFilterLists(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (56);
    result = 0;
    v_stack_m58 = 0;
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) {
        result = Arg6;
        *(uint32_t *)(result) = 0;
    }
    if (Arg4 == 0) goto loc_00AFA33E;
    if (Arg5 < 2) goto loc_00AFA334;
    v_stack_m58 = Arg4;
    *(uint16_t *)(Arg4) = 0;
    goto loc_00AFA33E;
loc_00AFA334:
    v_stack_m58 = 0;
    goto loc_00AFA33E;
loc_00AFA33A:
loc_00AFA33E:
    result = CmFindFilterListInflectionPoint(v_stack_p8, Arg2, v_stack_p18, Arg4);
    v_stack_m50 = result;
    Arg1 = 0;
    if ((*(uint16_t *)(v_stack_p8)) == 0) goto loc_00AFA423;
loc_00AFA36A:
    if (result == 0) goto loc_00AFA384;
    result = wcsicmp(v_stack_p8, result, v_stack_p18, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AFA41F;
loc_00AFA384:
    result = wcsicmp(v_stack_p8, v_stack_p18, v_stack_p18, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AFA401;
    result = (result) | (-1);
loc_00AFA399:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_p8 + result * 2)) != 0) goto loc_00AFA399;
    local_r15 = (uint32_t)((0 + result * 2) + (2));
    if (Arg4 == 0) goto loc_00AFA3FD;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = PnpMultiSzAppend(Arg4, v_stack_p20, v_stack_p8, v_stack_m58);
    local_rbx = 0;
    if ((uint8_t)(result) != 0) goto loc_00AFA3DF;
    v_stack_m58 = 0;
    goto loc_00AFA3EF;
loc_00AFA3DF:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(Arg4, v_stack_p20, v_stack_p8, v_stack_m58);
    local_r14 = (uint32_t)(Arg5);
    if ((uint32_t)(result) != 0) {
        local_r14 = (uint32_t)(((uint32_t)(Arg5)) - ((uint32_t)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(Arg4, v_stack_p20, v_stack_p8, v_stack_m58);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) {
        local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result * 2 + 2)));
    }
loc_00AFA401:
    result = (result) | (-1);
loc_00AFA405:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_p8 + result * 2)) != 0) goto loc_00AFA405;
    local_rdi = (v_stack_p8 + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_00AFA36A;
loc_00AFA41F:
loc_00AFA423:
    v_stack_p8 = local_rdi;
    if ((*(uint16_t *)(local_rdi)) == 0) goto loc_00AFA444;
    result = (result) | (-1);
loc_00AFA430:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rdi + result * 2)) != 0) goto loc_00AFA430;
    result = (result) + 1;
    v_stack_p8 = local_rdi + result * 2;
loc_00AFA444:
    if (v_stack_p10 == 0) goto loc_00AFA526;
    if ((*(uint16_t *)(v_stack_p10)) == 0) goto loc_00AFA501;
    local_r12 = (v_stack_p10) | (-1);
loc_00AFA45F:
    if (v_stack_m50 == 0) goto loc_00AFA479;
    result = wcsicmp(v_stack_p10, v_stack_m50, v_stack_p8, v_stack_m58);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AFA501;
loc_00AFA479:
loc_00AFA47C:
    result = (local_r12) + 1;
    if ((*(uint16_t *)(v_stack_p10 + result * 2)) != 0) goto loc_00AFA47C;
    local_r15 = (uint32_t)((local_r15 + result * 2) + (2));
    if (v_stack_m58 == 0) goto loc_00AFA4E0;
    v_stack_p20 = (uint32_t)(local_r14);
    result = PnpMultiSzAppend(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    local_rbx = 0;
    if ((uint8_t)(result) != 0) goto loc_00AFA4C2;
    v_stack_m58 = 0;
    goto loc_00AFA4D2;
loc_00AFA4C2:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    if ((uint32_t)(result) != 0) {
        local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_p10, v_stack_m58);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) {
        local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result * 2 + 2)));
    }
loc_00AFA4E3:
    result = (local_r12) + 1;
    if ((*(uint16_t *)(v_stack_p10 + result * 2)) != 0) goto loc_00AFA4E3;
    local_rdi = (v_stack_p10 + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_00AFA45F;
loc_00AFA501:
    v_stack_p10 = local_rdi;
    if ((*(uint16_t *)(local_rdi)) == 0) goto loc_00AFA526;
    result = (result) | (-1);
loc_00AFA511:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rdi + result * 2)) != 0) goto loc_00AFA511;
    v_stack_p10 = local_rdi + result + 1 * 2;
loc_00AFA526:
    if (v_stack_m50 == 0) goto loc_00AFA5BE;
    result = wcsicmp(v_stack_m50, v_stack_p18, v_stack_p10, v_stack_m58);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AFA33A;
    result = (result) | (-1);
loc_00AFA549:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m50 + result * 2)) != 0) goto loc_00AFA549;
    local_r15 = (uint32_t)((local_r15 + result * 2) + (2));
    if (v_stack_m58 == 0) goto loc_00AFA33A;
    v_stack_p20 = (uint32_t)(local_r14);
    result = PnpMultiSzAppend(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    local_rsi = 0;
    if ((uint8_t)(result) != 0) goto loc_00AFA595;
    v_stack_m58 = 0;
    goto loc_00AFA5A5;
loc_00AFA595:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    if ((uint32_t)(result) != 0) {
        local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result * 2 + 2)));
    }
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_stack_p20, v_stack_m50, v_stack_m58);
    if ((uint32_t)(result) != 0) goto loc_00AFA33E;
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result * 2 + 2)));
    goto loc_00AFA33A;
loc_00AFA5BE:
    if ((uint32_t)(local_r15) != 0) goto loc_00AFA5CB;
    goto loc_00AFA5E7;
loc_00AFA5CB:
    local_r15 = (uint32_t)((local_r15) + (2));
    *(uint32_t *)(arg6) = (uint32_t)(local_r15);
    if (v_stack_m58 == 0) goto loc_00AFA5E1;
    local_r13 = (uint32_t)(0xC0000225ULL);
    if (Arg5 < ((uint32_t)(local_r15))) {
        local_r13 = 0xC0000023ULL;
    }
    local_rsp = (local_rsp) + (56);
    return (uint32_t)((uint32_t)(local_r13));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AFA2CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
