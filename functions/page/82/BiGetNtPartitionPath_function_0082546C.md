# BiGetNtPartitionPath

- RVA: `0x0082546C`–`0x008259F5` (길이 `1,417` bytes)
- VA: `0x000000014082546C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCE60`
- 디코드: `383`개 명령, `1,417/1,417` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00825524` → [BiVerifyBootPartition](BiVerifyBootPartition_function_00825D94.md) (function, `0x00825D94`)
- `0x00825549` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00825591` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008255C3` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (function, `0x006ADBD0`)
- `0x008255E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082561A` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (function, `0x006AFAB0`)
- `0x0082562E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00825640` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00825689` → [BiIsValidDiskDevice](../70/BiIsValidDiskDevice_function_00703190.md) (function, `0x00703190`)
- `0x008256AD` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x008256BD` → [BiGetDriveLayoutBlock](BiGetDriveLayoutBlock_function_0082538C.md) (function, `0x0082538C`)
- `0x0082571F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082575C` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x00825768` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008257AE` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (function, `0x006AD730`)
- `0x008257BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0082583A` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x0082584A` → [BiGetPartitionVhdFilePath](../A9/BiGetPartitionVhdFilePath_function_00A9E5F4.md) (function, `0x00A9E5F4`)
- `0x00825861` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00825872` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008258D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008258F4` → [BiGetPartitionVhdFilePath](../A9/BiGetPartitionVhdFilePath_function_00A9E5F4.md) (function, `0x00A9E5F4`)
- `0x00825907` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00825918` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00825946` → [BiTranslateSymbolicLink](../A9/BiTranslateSymbolicLink_function_00A9BA0C.md) (function, `0x00A9BA0C`)
- `0x0082595B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00825987` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00825997` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008259A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008259B7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008259C6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008259D4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x0082413A`
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x00824454`

### Static image references
- `0x00825488` → RVA `0x00E0A740` (`.data`; read)
- `0x00825586` → RVA `0x00B0BD30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00825699` → RVA `0x00B0BD40` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x00825549` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00825591` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008255C3` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (`PAGE` → `.text`)
  - `0x008255E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082561A` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (`PAGE` → `.text`)
  - `0x0082562E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00825640` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008256AD` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x0082571F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082575C` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x00825768` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008257AE` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (`PAGE` → `.text`)
  - `0x008257BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0082583A` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x00825861` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00825872` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008258D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00825907` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00825918` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082595B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00825987` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00825997` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008259A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008259B7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008259C6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008259D4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0082546C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00825471  55                              push rbp
00825472  56                              push rsi
00825473  57                              push rdi
00825474  41 54                           push r12
00825476  41 55                           push r13
00825478  41 56                           push r14
0082547A  41 57                           push r15
0082547C  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00825481  48 81 EC 70 01 00 00            sub rsp, 0x170
00825488  48 8B 05 B1 52 5E 00            mov rax, qword ptr [rip + 0x5e52b1]
0082548F  48 33 C4                        xor rax, rsp
00825492  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00825496  33 F6                           xor esi, esi
00825498  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
0082549C  0F 57 C0                        xorps xmm0, xmm0
0082549F  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008254A4  33 C0                           xor eax, eax
008254A6  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
008254AA  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
008254AE  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
008254B3  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008254B7  4C 8D 45 88                     lea r8, [rbp - 0x78]
008254BB  89 45 D0                        mov dword ptr [rbp - 0x30], eax
008254BE  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
008254C3  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008254C7  0F 57 C9                        xorps xmm1, xmm1
008254CA  89 45 00                        mov dword ptr [rbp], eax
008254CD  8B FE                           mov edi, esi
008254CF  48 8D 44 24 70                  lea rax, [rsp + 0x70]
008254D4  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
008254D8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008254DD  44 8B EE                        mov r13d, esi
008254E0  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
008254E4  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
008254E8  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
008254EC  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
008254F0  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
008254F4  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008254F9  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
008254FD  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00825502  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
00825506  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
0082550B  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0082550F  48 89 75 98                     mov qword ptr [rbp - 0x68], rsi
00825513  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00825517  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0082551C  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00825520  0F 11 4D 18                     movups xmmword ptr [rbp + 0x18], xmm1
00825524  E8 6B 08 00 00                  call 0x140825d94
00825529  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0082552E  8B D8                           mov ebx, eax
00825530  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00825536  85 C0                           test eax, eax
00825538  0F 88 5E 04 00 00               js 0x14082599c
0082553E  45 8B C7                        mov r8d, r15d
00825541  8D 56 58                        lea edx, [rsi + 0x58]
00825544  B9 02 01 00 00                  mov ecx, 0x102
00825549  E8 A2 CB 35 00                  call 0x140b820f0
0082554E  4C 8B F0                        mov r14, rax
00825551  48 85 C0                        test rax, rax
00825554  75 0A                           jne 0x140825560
00825556  B8 17 00 00 C0                  mov eax, 0xc0000017
0082555B  E9 6D 04 00 00                  jmp 0x1408259cd
00825560  40 8A C6                        mov al, sil
00825563  BB 01 00 00 00                  mov ebx, 1
00825568  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0082556C  4D 85 E4                        test r12, r12
0082556F  74 15                           je 0x140825586
00825571  48 39 74 24 68                  cmp qword ptr [rsp + 0x68], rsi
00825576  75 0E                           jne 0x140825586
00825578  48 39 75 88                     cmp qword ptr [rbp - 0x78], rsi
0082557C  0F B6 C0                        movzx eax, al
0082557F  0F 44 C3                        cmove eax, ebx
00825582  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00825586  48 8D 15 A3 67 2E 00            lea rdx, [rip + 0x2e67a3]
0082558D  48 8D 4D 08                     lea rcx, [rbp + 8]
00825591  E8 EA 51 C0 FF                  call 0x14042a780
00825596  48 8D 45 08                     lea rax, [rbp + 8]
0082559A  C7 45 A8 30 00 00 00            mov dword ptr [rbp - 0x58], 0x30
008255A1  0F 57 C0                        xorps xmm0, xmm0
008255A4  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
008255A8  4C 8D 45 A8                     lea r8, [rbp - 0x58]
008255AC  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
008255B0  8B D3                           mov edx, ebx
008255B2  C7 45 C0 40 02 00 00            mov dword ptr [rbp - 0x40], 0x240
008255B9  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008255BE  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
008255C3  E8 08 86 E8 FF                  call 0x1406adbd0
008255C8  8B D8                           mov ebx, eax
008255CA  85 C0                           test eax, eax
008255CC  0F 88 AF 03 00 00               js 0x140825981
008255D2  BE 00 10 00 00                  mov esi, 0x1000
008255D7  8B D6                           mov edx, esi
008255D9  45 8B C7                        mov r8d, r15d
008255DC  B9 02 01 00 00                  mov ecx, 0x102
008255E1  E8 0A CB 35 00                  call 0x140b820f0
008255E6  4C 8B E8                        mov r13, rax
008255E9  33 C0                           xor eax, eax
008255EB  4D 85 ED                        test r13, r13
008255EE  0F 84 88 03 00 00               je 0x14082597c
008255F4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008255F9  45 33 C9                        xor r9d, r9d
008255FC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00825601  44 8B C6                        mov r8d, esi
00825604  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00825608  49 8B D5                        mov rdx, r13
0082560B  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00825610  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00825615  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0082561A  E8 91 A4 E8 FF                  call 0x1406afab0
0082561F  8B D8                           mov ebx, eax
00825621  3D 05 01 00 00                  cmp eax, 0x105
00825626  75 13                           jne 0x14082563b
00825628  41 8B D7                        mov edx, r15d
0082562B  49 8B CD                        mov rcx, r13
0082562E  E8 3D D2 35 00                  call 0x140b82870
00825633  81 C6 00 10 00 00               add esi, 0x1000
00825639  EB 9C                           jmp 0x1408255d7
0082563B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00825640  E8 6B 7C E8 FF                  call 0x1406ad2b0
00825645  B9 00 00 00 80                  mov ecx, 0x80000000
0082564A  33 F6                           xor esi, esi
0082564C  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00825651  8D 04 0B                        lea eax, [rbx + rcx]
00825654  85 C1                           test ecx, eax
00825656  75 0C                           jne 0x140825664
00825658  81 FB 1A 00 00 80               cmp ebx, 0x8000001a
0082565E  0F 85 1D 03 00 00               jne 0x140825981
00825664  40 8A DE                        mov bl, sil
00825667  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
0082566B  66 41 39 75 00                  cmp word ptr [r13], si
00825670  0F 84 FF 02 00 00               je 0x140825975
00825676  4D 8D 7D 08                     lea r15, [r13 + 8]
0082567A  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
0082567F  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00825683  45 33 C0                        xor r8d, r8d
00825686  49 8B 0F                        mov rcx, qword ptr [r15]
00825689  E8 02 DB ED FF                  call 0x140703190
0082568E  84 C0                           test al, al
00825690  0F 84 91 02 00 00               je 0x140825927
00825696  4D 8B 0F                        mov r9, qword ptr [r15]
00825699  4C 8D 05 A0 66 2E 00            lea r8, [rip + 0x2e66a0]
008256A0  BA 2C 00 00 00                  mov edx, 0x2c
008256A5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008256AA  49 8B CE                        mov rcx, r14
008256AD  E8 6E F4 CD FF                  call 0x140504b20
008256B2  4C 8D 45 38                     lea r8, [rbp + 0x38]
008256B6  49 8B CE                        mov rcx, r14
008256B9  48 8D 55 80                     lea rdx, [rbp - 0x80]
008256BD  E8 CA FC FF FF                  call 0x14082538c
008256C2  85 C0                           test eax, eax
008256C4  0F 88 5D 02 00 00               js 0x140825927
008256CA  83 7D 38 07                     cmp dword ptr [rbp + 0x38], 7
008256CE  75 3F                           jne 0x14082570f
008256D0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008256D5  48 8B 4A 04                     mov rcx, qword ptr [rdx + 4]
008256D9  48 2B 4D 3C                     sub rcx, qword ptr [rbp + 0x3c]
008256DD  75 13                           jne 0x1408256f2
008256DF  48 8B 4A 0C                     mov rcx, qword ptr [rdx + 0xc]
008256E3  48 2B 4D 44                     sub rcx, qword ptr [rbp + 0x44]
008256E7  75 09                           jne 0x1408256f2
008256E9  8B 45 4C                        mov eax, dword ptr [rbp + 0x4c]
008256EC  8B 4A 14                        mov ecx, dword ptr [rdx + 0x14]
008256EF  48 2B C8                        sub rcx, rax
008256F2  48 85 C9                        test rcx, rcx
008256F5  75 1F                           jne 0x140825716
008256F7  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
008256FB  41 8B 0C 24                     mov ecx, dword ptr [r12]
008256FF  85 C9                           test ecx, ecx
00825701  74 26                           je 0x140825729
00825703  83 F9 01                        cmp ecx, 1
00825706  74 26                           je 0x14082572e
00825708  BE 02 00 00 00                  mov esi, 2
0082570D  EB 1F                           jmp 0x14082572e
0082570F  4D 85 E4                        test r12, r12
00825712  75 E3                           jne 0x1408256f7
00825714  EB BA                           jmp 0x1408256d0
00825716  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0082571A  BA 42 43 44 4B                  mov edx, 0x4b444342
0082571F  E8 4C D1 35 00                  call 0x140b82870
00825724  E9 FE 01 00 00                  jmp 0x140825927
00825729  BE 01 00 00 00                  mov esi, 1
0082572E  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00825732  33 D2                           xor edx, edx
00825734  48 85 C0                        test rax, rax
00825737  0F 84 92 00 00 00               je 0x1408257cf
0082573D  83 FE 01                        cmp esi, 1
00825740  0F 85 8E 00 00 00               jne 0x1408257d4
00825746  8B 00                           mov eax, dword ptr [rax]
00825748  4C 8D 05 F1 65 2E 00            lea r8, [rip + 0x2e65f1]
0082574F  4D 8B 0F                        mov r9, qword ptr [r15]
00825752  8D 56 2B                        lea edx, [rsi + 0x2b]
00825755  49 8B CE                        mov rcx, r14
00825758  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0082575C  E8 BF F3 CD FF                  call 0x140504b20
00825761  49 8B D6                        mov rdx, r14
00825764  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00825768  E8 13 50 C0 FF                  call 0x14042a780
0082576D  33 F6                           xor esi, esi
0082576F  C7 45 D8 30 00 00 00            mov dword ptr [rbp - 0x28], 0x30
00825776  48 8D 45 18                     lea rax, [rbp + 0x18]
0082577A  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0082577E  0F 57 C0                        xorps xmm0, xmm0
00825781  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00825785  4C 8D 4D 28                     lea r9, [rbp + 0x28]
00825789  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00825791  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00825795  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00825799  BA 00 00 00 80                  mov edx, 0x80000000
0082579E  C7 45 F0 40 02 00 00            mov dword ptr [rbp - 0x10], 0x240
008257A5  48 8D 4D 90                     lea rcx, [rbp - 0x70]
008257A9  F3 0F 7F 45 F8                  movdqu xmmword ptr [rbp - 8], xmm0
008257AE  E8 7D 7F E8 FF                  call 0x1406ad730
008257B3  85 C0                           test eax, eax
008257B5  0F 88 14 01 00 00               js 0x1408258cf
008257BB  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
008257BF  E8 EC 7A E8 FF                  call 0x1406ad2b0
008257C4  B3 01                           mov bl, 1
008257C6  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
008257CA  E9 00 01 00 00                  jmp 0x1408258cf
008257CF  83 FE 01                        cmp esi, 1
008257D2  74 08                           je 0x1408257dc
008257D4  85 F6                           test esi, esi
008257D6  0F 85 F1 00 00 00               jne 0x1408258cd
008257DC  48 8B DA                        mov rbx, rdx
008257DF  85 F6                           test esi, esi
008257E1  75 16                           jne 0x1408257f9
008257E3  48 85 C0                        test rax, rax
008257E6  74 05                           je 0x1408257ed
008257E8  48 8B D8                        mov rbx, rax
008257EB  EB 0C                           jmp 0x1408257f9
008257ED  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008257F2  48 85 C9                        test rcx, rcx
008257F5  48 0F 45 D9                     cmovne rbx, rcx
008257F9  8B C2                           mov eax, edx
008257FB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008257FF  41 3B 44 24 04                  cmp eax, dword ptr [r12 + 4]
00825804  0F 83 BA 00 00 00               jae 0x1408258c4
0082580A  4C 8D 3C C0                     lea r15, [rax + rax*8]
0082580E  49 C1 E7 04                     shl r15, 4
00825812  43 8B 44 27 48                  mov eax, dword ptr [r15 + r12 + 0x48]
00825817  85 C0                           test eax, eax
00825819  0F 84 92 00 00 00               je 0x1408258b1
0082581F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00825823  4C 8D 05 16 65 2E 00            lea r8, [rip + 0x2e6516]
0082582A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0082582F  BA 2C 00 00 00                  mov edx, 0x2c
00825834  49 8B CE                        mov rcx, r14
00825837  4C 8B 08                        mov r9, qword ptr [rax]
0082583A  E8 E1 F2 CD FF                  call 0x140504b20
0082583F  33 D2                           xor edx, edx
00825841  38 54 24 44                     cmp byte ptr [rsp + 0x44], dl
00825845  74 34                           je 0x14082587b
00825847  49 8B CE                        mov rcx, r14
0082584A  E8 A5 8D 27 00                  call 0x140a9e5f4
0082584F  33 D2                           xor edx, edx
00825851  48 8B F8                        mov rdi, rax
00825854  48 85 C0                        test rax, rax
00825857  74 22                           je 0x14082587b
00825859  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0082585E  48 8B D0                        mov rdx, rax
00825861  E8 1A A8 CD FF                  call 0x140500080
00825866  85 C0                           test eax, eax
00825868  74 52                           je 0x1408258bc
0082586A  BA 42 43 44 4B                  mov edx, 0x4b444342
0082586F  48 8B CF                        mov rcx, rdi
00825872  E8 F9 CF 35 00                  call 0x140b82870
00825877  33 D2                           xor edx, edx
00825879  8B FA                           mov edi, edx
0082587B  83 FE 01                        cmp esi, 1
0082587E  75 14                           jne 0x140825894
00825880  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00825885  48 85 C9                        test rcx, rcx
00825888  74 27                           je 0x1408258b1
0082588A  4B 8B 44 27 38                  mov rax, qword ptr [r15 + r12 + 0x38]
0082588F  48 39 01                        cmp qword ptr [rcx], rax
00825892  EB 1B                           jmp 0x1408258af
00825894  48 85 DB                        test rbx, rbx
00825897  74 18                           je 0x1408258b1
00825899  48 8B 0B                        mov rcx, qword ptr [rbx]
0082589C  4B 2B 4C 27 60                  sub rcx, qword ptr [r15 + r12 + 0x60]
008258A1  75 09                           jne 0x1408258ac
008258A3  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008258A7  4B 2B 4C 27 68                  sub rcx, qword ptr [r15 + r12 + 0x68]
008258AC  48 85 C9                        test rcx, rcx
008258AF  74 0B                           je 0x1408258bc
008258B1  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
008258B5  FF C0                           inc eax
008258B7  E9 3F FF FF FF                  jmp 0x1408257fb
008258BC  B3 01                           mov bl, 1
008258BE  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
008258C2  EB 04                           jmp 0x1408258c8
008258C4  8A 5C 24 40                     mov bl, byte ptr [rsp + 0x40]
008258C8  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
008258CD  33 F6                           xor esi, esi
008258CF  BA 42 43 44 4B                  mov edx, 0x4b444342
008258D4  49 8B CC                        mov rcx, r12
008258D7  E8 94 CF 35 00                  call 0x140b82870
008258DC  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
008258E1  4D 85 E4                        test r12, r12
008258E4  74 55                           je 0x14082593b
008258E6  84 DB                           test bl, bl
008258E8  74 3D                           je 0x140825927
008258EA  40 38 74 24 44                  cmp byte ptr [rsp + 0x44], sil
008258EF  75 4E                           jne 0x14082593f
008258F1  49 8B CE                        mov rcx, r14
008258F4  E8 FB 8C 27 00                  call 0x140a9e5f4
008258F9  48 8B F8                        mov rdi, rax
008258FC  48 85 C0                        test rax, rax
008258FF  74 1F                           je 0x140825920
00825901  48 8B D0                        mov rdx, rax
00825904  49 8B CC                        mov rcx, r12
00825907  E8 74 A7 CD FF                  call 0x140500080
0082590C  85 C0                           test eax, eax
0082590E  74 2F                           je 0x14082593f
00825910  BA 42 43 44 4B                  mov edx, 0x4b444342
00825915  48 8B CF                        mov rcx, rdi
00825918  E8 53 CF 35 00                  call 0x140b82870
0082591D  48 8B FE                        mov rdi, rsi
00825920  40 8A DE                        mov bl, sil
00825923  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00825927  49 83 C7 20                     add r15, 0x20
0082592B  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00825930  66 41 39 77 F8                  cmp word ptr [r15 - 8], si
00825935  0F 85 44 FD FF FF               jne 0x14082567f
0082593B  84 DB                           test bl, bl
0082593D  74 30                           je 0x14082596f
0082593F  48 8D 55 98                     lea rdx, [rbp - 0x68]
00825943  49 8B CE                        mov rcx, r14
00825946  E8 C1 60 27 00                  call 0x140a9ba0c
0082594B  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00825951  85 C0                           test eax, eax
00825953  78 0F                           js 0x140825964
00825955  41 8B D7                        mov edx, r15d
00825958  49 8B CE                        mov rcx, r14
0082595B  E8 10 CF 35 00                  call 0x140b82870
00825960  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
00825964  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00825968  8B DE                           mov ebx, esi
0082596A  4C 89 30                        mov qword ptr [rax], r14
0082596D  EB 22                           jmp 0x140825991
0082596F  41 BF 42 43 44 4B               mov r15d, 0x4b444342
00825975  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0082597A  EB 05                           jmp 0x140825981
0082597C  BB 17 00 00 C0                  mov ebx, 0xc0000017
00825981  41 8B D7                        mov edx, r15d
00825984  49 8B CE                        mov rcx, r14
00825987  E8 E4 CE 35 00                  call 0x140b82870
0082598C  4D 85 ED                        test r13, r13
0082598F  74 0B                           je 0x14082599c
00825991  41 8B D7                        mov edx, r15d
00825994  49 8B CD                        mov rcx, r13
00825997  E8 D4 CE 35 00                  call 0x140b82870
0082599C  4D 85 E4                        test r12, r12
0082599F  74 0B                           je 0x1408259ac
008259A1  41 8B D7                        mov edx, r15d
008259A4  49 8B CC                        mov rcx, r12
008259A7  E8 C4 CE 35 00                  call 0x140b82870
008259AC  48 85 FF                        test rdi, rdi
008259AF  74 0B                           je 0x1408259bc
008259B1  41 8B D7                        mov edx, r15d
008259B4  48 8B CF                        mov rcx, rdi
008259B7  E8 B4 CE 35 00                  call 0x140b82870
008259BC  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008259C1  48 85 C9                        test rcx, rcx
008259C4  74 05                           je 0x1408259cb
008259C6  E8 E5 78 E8 FF                  call 0x1406ad2b0
008259CB  8B C3                           mov eax, ebx
008259CD  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
008259D1  48 33 CC                        xor rcx, rsp
008259D4  E8 67 6C E8 FF                  call 0x1406ac640
008259D9  48 8B 9C 24 C0 01 00 00         mov rbx, qword ptr [rsp + 0x1c0]
008259E1  48 81 C4 70 01 00 00            add rsp, 0x170
008259E8  41 5F                           pop r15
008259EA  41 5E                           pop r14
008259EC  41 5D                           pop r13
008259EE  41 5C                           pop r12
008259F0  5F                              pop rdi
008259F1  5E                              pop rsi
008259F2  5D                              pop rbp
008259F3  C3                              ret
008259F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiGetNtPartitionPath(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 6181553)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m108 = a2;
    v_stack_m180 = 0;
    result = 0;
    v_stack_m120 = 0;
    v_stack_m50 = 0;
    v_stack_mE0 = 0;
    v_stack_mD8 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    v_stack_m118 = 0;
    v_stack_m188 = v_stack_m138;
    v_stack_m70 = v_xmm0;
    v_stack_m150 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m100 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m130 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m148 = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_m110 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m90 = v_xmm1;
    result = BiVerifyBootPartition(a1, v_stack_m140, v_stack_m120, v_stack_m130);
    if (sign_flag) goto loc_0082599C;
    result = ExAllocatePool2(258, v_rsi + 88, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_m130);
    if (result != 0) goto loc_00825560;
    goto loc_008259CD;
loc_00825560:
    v_stack_m164 = 0;
    if (v_stack_m138 == 0) goto loc_00825586;
    result = 0;
    if (v_stack_m140 == 0) {
        result = 0;
        if (v_stack_m120 == 0) { result = 1; }
        v_stack_m164 = (unsigned int)(result);
    }
    result = RtlInitUnicodeString(v_stack_mA0, v_rip + 3041187, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_m130);
    v_stack_m100 = 48;
    v_stack_mF0 = v_stack_mA0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 576;
    v_stack_mE0 = v_xmm0;
    result = ZwOpenDirectoryObject(v_stack_m148, 1, v_stack_m100, v_stack_m130);
    if (sign_flag) goto loc_00825981;
loc_008255D7:
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_stack_m130);
    result = 0;
    if (0 == 0) goto loc_0082597C;
    a4 = 0;
    v_stack_m178 = 0;
    v_stack_m150 = 0;
    v_stack_m180 = v_stack_m150;
    v_stack_m188 = 1;
    result = ZwQueryDirectoryObject(v_stack_m148, 0, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    if (((unsigned int)(result)) != 261) goto loc_0082563B;
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    v_rsi = (unsigned int)(((unsigned int)(0x1000ULL)) + (0x1000ULL));
    goto loc_008255D7;
loc_0082563B:
    result = ZwClose(v_stack_m148, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), a4);
    v_rsi = 0;
    v_stack_m148 = 0;
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00825664;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0x8000001AULL) goto loc_00825981;
loc_00825664:
    v_stack_m168 = 0;
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00825975;
    v_stack_m158 = result + 8;
loc_0082567F:
    a3 = 0;
    result = BiIsValidDiskDevice(*(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 8 + 16), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00825927;
    v_stack_m188 = 0;
    result = swprintf_s(result, 44, v_rip + 3040928, *(unsigned __int64 *)(result + 8));
    result = BiGetDriveLayoutBlock(result, v_stack_m128, v_stack_m70, *(unsigned __int64 *)(result + 8));
    if (sign_flag) goto loc_00825927;
    if (v_stack_m70 != 7) goto loc_0082570F;
loc_008256D0:
    a1 = (*(unsigned __int64 *)(v_stack_m130 + 4)) - (v_stack_m6C);
    if (condition_is_not_equal) goto loc_008256F2;
    a1 = (*(unsigned __int64 *)(v_stack_m130 + 12)) - (v_stack_m64);
    if (!(condition_is_not_equal)) {
        result = v_stack_m5C;
        a1 = *(unsigned int *)(v_stack_m130 + 20);
        a1 = (a1) - (result);
    }
    if (a1 != 0) goto loc_00825716;
loc_008256F7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128))) == 0) goto loc_00825729;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m128)))) == 1) goto loc_0082572E;
    goto loc_0082572E;
loc_0082570F:
    if (v_stack_m128 != 0) goto loc_008256F7;
    goto loc_008256D0;
loc_00825716:
    result = ExFreePoolWithTag(v_stack_m128, (unsigned int)(0x4B444342ULL), v_stack_m70, *(unsigned __int64 *)(result + 8));
    goto loc_00825927;
loc_00825729:
loc_0082572E:
    a2 = 0;
    if (v_stack_m120 == 0) goto loc_008257CF;
    if (1 != 1) goto loc_008257D4;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120)));
    result = swprintf_s(result, 1 + 43, v_rip + 3040753, *(unsigned __int64 *)(result + 8));
    result = RtlInitUnicodeString(v_stack_m90, result, v_rip + 3040753, *(unsigned __int64 *)(result + 8));
    v_rsi = 0;
    v_stack_mD0 = 48;
    v_stack_m180 = 0;
    v_stack_mC0 = v_stack_m90;
    v_stack_m188 = 3;
    v_stack_mC8 = 0;
    v_stack_mB8 = 576;
    v_stack_mB0 = v_xmm0;
    result = ZwOpenFile(v_stack_m118, (unsigned int)(0x80000000ULL), v_stack_mD0, v_stack_m80);
    if (sign_flag) goto loc_008258CF;
    result = ZwClose(v_stack_m118, (unsigned int)(0x80000000ULL), v_stack_mD0, v_stack_m80);
    v_stack_m168 = 1;
    goto loc_008258CF;
loc_008257CF:
    if (0 == 1) goto loc_008257DC;
loc_008257D4:
    if (0 != 0) goto loc_008258CD;
loc_008257DC:
    if (0 != 0) goto loc_008257F9;
    if (result == 0) goto loc_008257ED;
    goto loc_008257F9;
loc_008257ED:
    v_rbx = result;
    if (v_stack_m140 != 0) { v_rbx = v_stack_m140; }
loc_008257F9:
loc_008257FB:
    v_stack_m160 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))))) >= (*(unsigned int *)(v_stack_m128 + 4))) goto loc_008258C4;
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))) + (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))) * 8) << (4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + v_stack_m128 * 1 + 72))) == 0) goto loc_008258B1;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + v_stack_m128 * 1 + 72)));
    result = swprintf_s(result, 44, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    a2 = 0;
    if (v_stack_m164 == 0) goto loc_0082587B;
    result = BiGetPartitionVhdFilePath(result, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    a2 = 0;
    if (result == 0) goto loc_0082587B;
    result = wcsicmp(v_stack_m138, result, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    if ((unsigned int)(result) == 0) goto loc_008258BC;
    result = ExFreePoolWithTag(result, (unsigned int)(0x4B444342ULL), v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    a2 = 0;
loc_0082587B:
    if (0 != 1) goto loc_00825894;
    if (v_stack_m140 == 0) goto loc_008258B1;
    goto loc_008258AF;
loc_00825894:
    if (v_rbx == 0) goto loc_008258B1;
    a1 = (*(unsigned __int64 *)(v_rbx)) - (*(unsigned __int64 *)(v_r15 + v_stack_m128 * 1 + 96));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rbx + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_r15 + v_stack_m128 * 1 + 104));
    }
loc_008258AF:
    if (a1 == 0) goto loc_008258BC;
loc_008258B1:
    result = (unsigned int)(((unsigned int)(v_stack_m160)) + 1);
    goto loc_008257FB;
loc_008258BC:
    v_stack_m168 = 1;
    goto loc_008258C8;
loc_008258C4:
loc_008258C8:
loc_008258CD:
    v_rsi = 0;
loc_008258CF:
    result = ExFreePoolWithTag(v_stack_m128, (unsigned int)(0x4B444342ULL), v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    if (v_stack_m138 == 0) goto loc_0082593B;
    if ((unsigned __int8)(v_stack_m168) == 0) goto loc_00825927;
    if (v_stack_m164 != 0) goto loc_0082593F;
    result = BiGetPartitionVhdFilePath(result, (unsigned int)(0x4B444342ULL), v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    if (result == 0) goto loc_00825920;
    result = wcsicmp(v_stack_m138, result, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    if ((unsigned int)(result) == 0) goto loc_0082593F;
    result = ExFreePoolWithTag(result, (unsigned int)(0x4B444342ULL), v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
loc_00825920:
    v_stack_m168 = 0;
loc_00825927:
    v_r15 = (v_stack_m158) + (32);
    v_stack_m158 = v_r15;
    if ((*(unsigned __int16 *)(v_r15 - 8)) != 0) goto loc_0082567F;
loc_0082593B:
    if (0 == 0) goto loc_0082596F;
loc_0082593F:
    result = BiTranslateSymbolicLink(result, v_stack_m110, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    v_r14 = result;
    if (!(sign_flag)) {
        a2 = (unsigned int)((unsigned int)(0x4B444342ULL));
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
        v_r14 = v_stack_m110;
    }
    *(unsigned __int64 *)(v_stack_m108) = v_r14;
    goto loc_00825991;
loc_0082596F:
loc_00825975:
    goto loc_00825981;
loc_0082597C:
loc_00825981:
    result = ExFreePoolWithTag(v_r14, (unsigned int)((unsigned int)((unsigned int)(0x4B444342ULL))), v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    if (result != 0) {
        a2 = (unsigned int)((unsigned int)(0x4B444342ULL));
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    }
    if (v_stack_m138 != 0) {
        a2 = (unsigned int)((unsigned int)(0x4B444342ULL));
        a1 = v_stack_m138;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    }
    if (0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x4B444342ULL));
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    }
    if (v_stack_m148 != 0) {
        result = ZwClose(v_stack_m148, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    }
loc_008259CD:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 3040534, *(unsigned __int64 *)(v_stack_m158));
    v_rsp = (v_rsp) + (368);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BiGetNtPartitionPath(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint8_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m64;
    uint64_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x5E52B1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m108 = Arg2;
    v_stack_m180 = 0;
    result = 0;
    v_stack_m120 = 0;
    v_stack_m50 = 0;
    v_stack_mE0 = 0;
    v_stack_mD8 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    v_stack_m118 = 0;
    v_stack_m188 = v_stack_m138;
    v_stack_m70 = v_xmm0;
    v_stack_m150 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m100 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_mF0 = v_xmm0;
    v_stack_m130 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m148 = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_m110 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m90 = v_xmm1;
    result = BiVerifyBootPartition(Arg1, v_stack_m140, v_stack_m120, v_stack_m130);
    if (sign_flag) goto loc_0082599C;
    result = ExAllocatePool2(258, local_rsi + 88, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_m130);
    if (result != 0) goto loc_00825560;
    goto loc_008259CD;
loc_00825560:
    v_stack_m164 = 0;
    if (v_stack_m138 == 0) goto loc_00825586;
    result = 0;
    if (v_stack_m140 == 0) {
        result = 0;
        if (v_stack_m120 == 0) { result = 1; }
        v_stack_m164 = (uint32_t)(result);
    }
    result = RtlInitUnicodeString(v_stack_mA0, v_rip + 3041187, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_m130);
    v_stack_m100 = 48;
    v_stack_mF0 = v_stack_mA0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 576;
    v_stack_mE0 = v_xmm0;
    result = ZwOpenDirectoryObject(v_stack_m148, 1, v_stack_m100, v_stack_m130);
    if (sign_flag) goto loc_00825981;
loc_008255D7:
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_stack_m130);
    result = 0;
    if (0 == 0) goto loc_0082597C;
    a4 = 0;
    v_stack_m178 = 0;
    v_stack_m150 = 0;
    v_stack_m180 = v_stack_m150;
    v_stack_m188 = 1;
    result = ZwQueryDirectoryObject(v_stack_m148, 0, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), a4);
    if (((uint32_t)(result)) != 261) goto loc_0082563B;
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), a4);
    local_rsi = (uint32_t)(((uint32_t)(0x1000ULL)) + (0x1000ULL));
    goto loc_008255D7;
loc_0082563B:
    result = ZwClose(v_stack_m148, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), a4);
    local_rsi = 0;
    v_stack_m148 = 0;
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00825664;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0x8000001AULL) goto loc_00825981;
loc_00825664:
    v_stack_m168 = 0;
    if ((*(uint16_t *)(result)) == 0) goto loc_00825975;
    v_stack_m158 = result + 8;
loc_0082567F:
    a3 = 0;
    result = BiIsValidDiskDevice(*(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x8 + 0x10), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00825927;
    v_stack_m188 = 0;
    result = swprintf_s(result, 44, v_rip + 3040928, *(uint64_t *)(result + 0x8));
    result = BiGetDriveLayoutBlock(result, v_stack_m128, v_stack_m70, *(uint64_t *)(result + 0x8));
    if (sign_flag) goto loc_00825927;
    if (v_stack_m70 != 7) goto loc_0082570F;
loc_008256D0:
    Arg1 = (*(uint64_t *)(v_stack_m130 + 0x4)) - (v_stack_m6C);
    if (condition_is_not_equal) goto loc_008256F2;
    Arg1 = (*(uint64_t *)(v_stack_m130 + 0xC)) - (v_stack_m64);
    if (!(condition_is_not_equal)) {
        result = v_stack_m5C;
        Arg1 = *(uint32_t *)(v_stack_m130 + 0x14);
        Arg1 = (Arg1) - (result);
    }
    if (Arg1 != 0) goto loc_00825716;
loc_008256F7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128))) == 0) goto loc_00825729;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m128)))) == 1) goto loc_0082572E;
    goto loc_0082572E;
loc_0082570F:
    if (v_stack_m128 != 0) goto loc_008256F7;
    goto loc_008256D0;
loc_00825716:
    result = ExFreePoolWithTag(v_stack_m128, (uint32_t)(0x4B444342ULL), v_stack_m70, *(uint64_t *)(result + 0x8));
    goto loc_00825927;
loc_00825729:
loc_0082572E:
    Arg2 = 0;
    if (v_stack_m120 == 0) goto loc_008257CF;
    if (1 != 1) goto loc_008257D4;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120)));
    result = swprintf_s(result, 1 + 43, v_rip + 3040753, *(uint64_t *)(result + 0x8));
    result = RtlInitUnicodeString(v_stack_m90, result, v_rip + 3040753, *(uint64_t *)(result + 0x8));
    local_rsi = 0;
    v_stack_mD0 = 48;
    v_stack_m180 = 0;
    v_stack_mC0 = v_stack_m90;
    v_stack_m188 = 3;
    v_stack_mC8 = 0;
    v_stack_mB8 = 576;
    v_stack_mB0 = v_xmm0;
    result = ZwOpenFile(v_stack_m118, (uint32_t)(0x80000000ULL), v_stack_mD0, v_stack_m80);
    if (sign_flag) goto loc_008258CF;
    result = ZwClose(v_stack_m118, (uint32_t)(0x80000000ULL), v_stack_mD0, v_stack_m80);
    v_stack_m168 = 1;
    goto loc_008258CF;
loc_008257CF:
    if (0 == 1) goto loc_008257DC;
loc_008257D4:
    if (0 != 0) goto loc_008258CD;
loc_008257DC:
    if (0 != 0) goto loc_008257F9;
    if (result == 0) goto loc_008257ED;
    goto loc_008257F9;
loc_008257ED:
    local_rbx = result;
    if (v_stack_m140 != 0) { local_rbx = v_stack_m140; }
loc_008257F9:
loc_008257FB:
    v_stack_m160 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))))) >= (*(uint32_t *)(v_stack_m128 + 0x4))) goto loc_008258C4;
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))) + (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))) * 8) << (4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + v_stack_m128 * 1 + 0x48))) == 0) goto loc_008258B1;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + v_stack_m128 * 1 + 0x48)));
    result = swprintf_s(result, 44, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    Arg2 = 0;
    if (v_stack_m164 == 0) goto loc_0082587B;
    result = BiGetPartitionVhdFilePath(result, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    Arg2 = 0;
    if (result == 0) goto loc_0082587B;
    result = wcsicmp(v_stack_m138, result, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    if ((uint32_t)(result) == 0) goto loc_008258BC;
    result = ExFreePoolWithTag(result, (uint32_t)(0x4B444342ULL), v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    Arg2 = 0;
loc_0082587B:
    if (0 != 1) goto loc_00825894;
    if (v_stack_m140 == 0) goto loc_008258B1;
    goto loc_008258AF;
loc_00825894:
    if (local_rbx == 0) goto loc_008258B1;
    Arg1 = (*(uint64_t *)(local_rbx)) - (*(uint64_t *)(local_r15 + v_stack_m128 * 1 + 0x60));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rbx + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(local_r15 + v_stack_m128 * 1 + 0x68));
    }
loc_008258AF:
    if (Arg1 == 0) goto loc_008258BC;
loc_008258B1:
    result = (uint32_t)(((uint32_t)(v_stack_m160)) + 1);
    goto loc_008257FB;
loc_008258BC:
    v_stack_m168 = 1;
    goto loc_008258C8;
loc_008258C4:
loc_008258C8:
loc_008258CD:
    local_rsi = 0;
loc_008258CF:
    result = ExFreePoolWithTag(v_stack_m128, (uint32_t)(0x4B444342ULL), v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    if (v_stack_m138 == 0) goto loc_0082593B;
    if ((uint8_t)(v_stack_m168) == 0) goto loc_00825927;
    if (v_stack_m164 != 0) goto loc_0082593F;
    result = BiGetPartitionVhdFilePath(result, (uint32_t)(0x4B444342ULL), v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    if (result == 0) goto loc_00825920;
    result = wcsicmp(v_stack_m138, result, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    if ((uint32_t)(result) == 0) goto loc_0082593F;
    result = ExFreePoolWithTag(result, (uint32_t)(0x4B444342ULL), v_rip + 3040534, *(uint64_t *)(v_stack_m158));
loc_00825920:
    v_stack_m168 = 0;
loc_00825927:
    local_r15 = (v_stack_m158) + (32);
    v_stack_m158 = local_r15;
    if ((*(uint16_t *)(local_r15 - 0x8)) != 0) goto loc_0082567F;
loc_0082593B:
    if (0 == 0) goto loc_0082596F;
loc_0082593F:
    result = BiTranslateSymbolicLink(result, v_stack_m110, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    local_r14 = result;
    if (!(sign_flag)) {
        Arg2 = (uint32_t)((uint32_t)(0x4B444342ULL));
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
        local_r14 = v_stack_m110;
    }
    *(uint64_t *)(v_stack_m108) = local_r14;
    goto loc_00825991;
loc_0082596F:
loc_00825975:
    goto loc_00825981;
loc_0082597C:
loc_00825981:
    result = ExFreePoolWithTag(local_r14, (uint32_t)((uint32_t)((uint32_t)(0x4B444342ULL))), v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    if (result != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x4B444342ULL));
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    }
    if (v_stack_m138 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x4B444342ULL));
        Arg1 = v_stack_m138;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    }
    if (0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x4B444342ULL));
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    }
    if (v_stack_m148 != 0) {
        result = ZwClose(v_stack_m148, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    }
loc_008259CD:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 3040534, *(uint64_t *)(v_stack_m158));
    local_rsp = (local_rsp) + (368);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0082546C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
