# CmpOpenHiveFile

- RVA: `0x0087A71C`–`0x0087ADD4` (길이 `1,720` bytes)
- VA: `0x000000014087A71C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006CDD0`
- 디코드: `419`개 명령, `1,720/1,720` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0087A802` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0087A80B` → [CmSiEventTupleInitialize](../../text/49/CmSiEventTupleInitialize_function_00495EE0.md) (function, `0x00495EE0`)
- `0x0087A814` → [CmSiCreateEvent](../../text/47/CmSiCreateEvent_function_00478F6C.md) (function, `0x00478F6C`)
- `0x0087A82F` → [CmpGetCompleteFileName](CmpGetCompleteFileName_function_0087ADDC.md) (function, `0x0087ADDC`)
- `0x0087A91D` → [ZwCreateFile](../../text/6A/ZwCreateFile_function_006ADB70.md) (function, `0x006ADB70`)
- `0x0087A945` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087A973` → [ZwQueryAttributesFile](../../text/6A/ZwQueryAttributesFile_function_006AD870.md) (function, `0x006AD870`)
- `0x0087A996` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087A9FE` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (function, `0x006AD5B0`)
- `0x0087AA4C` → [ZwFsControlFile](../../text/6A/ZwFsControlFile_function_006AD7F0.md) (function, `0x006AD7F0`)
- `0x0087AA5C` → [CmSiWaitForSingleEvent](../../text/49/CmSiWaitForSingleEvent_function_0049E4BC.md) (function, `0x0049E4BC`)
- `0x0087AA89` → [ZwQueryInformationFile](../../text/6A/ZwQueryInformationFile_function_006AD2F0.md) (function, `0x006AD2F0`)
- `0x0087AABA` → [CmpQueryFileSecurityDescriptor](CmpQueryFileSecurityDescriptor_function_0087B318.md) (function, `0x0087B318`)
- `0x0087AAF6` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0087AB08` → [CmSiEventTupleCleanup](../../text/48/CmSiEventTupleCleanup_function_00487E8C.md) (function, `0x00487E8C`)
- `0x0087AB27` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0087AB4F` → [CmpLogHiveFileInaccessible](CmpLogHiveFileInaccessible_function_0087AEAC.md) (function, `0x0087AEAC`)
- `0x0087AB67` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087AB99` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0087ABD0` → [CmpGetVolumeClusterSize](CmpGetVolumeClusterSize_function_0087B3D4.md) (function, `0x0087B3D4`)
- `0x0087ABE0` → [CmpGetVolumeLogFileSizeCap](CmpGetVolumeLogFileSizeCap_function_0087B718.md) (function, `0x0087B718`)
- `0x0087AC22` → [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)
- `0x0087AC3C` → [CmSiBugCheck](../../text/66/CmSiBugCheck_function_0066DF38.md) (function, `0x0066DF38`)
- `0x0087AC6B` → [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)
- `0x0087ACA5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0087ACC2` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x0087AD0B` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0087AD30` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x0087AD3A` → [PsRevertToSelf](../8C/PsRevertToSelf_function_008CD200.md) (function, `0x008CD200`)
- `0x0087AD97` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (function, `0x006AD730`)
- `0x0087ADB3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0087ADCA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB5C8`
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB620`
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB666`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC09B`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC0F0`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC133`
- [CmLoadAppKey](CmLoadAppKey_function_00876FFC.md) at `0x008771DD`
- [CmLoadKey](CmLoadKey_function_008787CC.md) at `0x00878ED4`
- [CmpOpenHiveFiles](CmpOpenHiveFiles_function_00879A68.md) at `0x00879B44`
- [CmpOpenHiveFiles](CmpOpenHiveFiles_function_00879A68.md) at `0x00879C1C`
- [CmpOpenHiveFiles](CmpOpenHiveFiles_function_00879A68.md) at `0x00879C61`
- [CmpOpenHiveFiles](CmpOpenHiveFiles_function_00879A68.md) at `0x00879D53`
- [sub_00B179DA](../B1/Unknown_function_00B179DA.md) at `0x00B17A10`

### Static image references
- `0x0087A738` → RVA `0x00E0A740` (`.data`; read)
- `0x0087A9C8` → RVA `0x00010850` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x0087A802` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0087A80B` → [CmSiEventTupleInitialize](../../text/49/CmSiEventTupleInitialize_function_00495EE0.md) (`PAGE` → `.text`)
  - `0x0087A814` → [CmSiCreateEvent](../../text/47/CmSiCreateEvent_function_00478F6C.md) (`PAGE` → `.text`)
  - `0x0087A91D` → [ZwCreateFile](../../text/6A/ZwCreateFile_function_006ADB70.md) (`PAGE` → `.text`)
  - `0x0087A945` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087A973` → [ZwQueryAttributesFile](../../text/6A/ZwQueryAttributesFile_function_006AD870.md) (`PAGE` → `.text`)
  - `0x0087A996` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087A9FE` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (`PAGE` → `.text`)
  - `0x0087AA4C` → [ZwFsControlFile](../../text/6A/ZwFsControlFile_function_006AD7F0.md) (`PAGE` → `.text`)
  - `0x0087AA5C` → [CmSiWaitForSingleEvent](../../text/49/CmSiWaitForSingleEvent_function_0049E4BC.md) (`PAGE` → `.text`)
  - `0x0087AA89` → [ZwQueryInformationFile](../../text/6A/ZwQueryInformationFile_function_006AD2F0.md) (`PAGE` → `.text`)
  - `0x0087AAF6` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0087AB08` → [CmSiEventTupleCleanup](../../text/48/CmSiEventTupleCleanup_function_00487E8C.md) (`PAGE` → `.text`)
  - `0x0087AB27` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0087AB67` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087AB99` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0087AC3C` → [CmSiBugCheck](../../text/66/CmSiBugCheck_function_0066DF38.md) (`PAGE` → `.text`)
  - `0x0087ACA5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0087ACC2` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x0087AD0B` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0087AD30` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x0087AD97` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (`PAGE` → `.text`)
  - `0x0087ADB3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0087ADCA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0087AA0B` → [sub_00B1833E + 0x9A](../B1/Unknown_function_00B1833E.md) (`tail-transfer`)
  - `0x0087ADA0` → [sub_00B1833E](../B1/Unknown_function_00B1833E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0087A71C  40 55                           push rbp
0087A71E  53                              push rbx
0087A71F  56                              push rsi
0087A720  57                              push rdi
0087A721  41 54                           push r12
0087A723  41 55                           push r13
0087A725  41 56                           push r14
0087A727  41 57                           push r15
0087A729  48 8D AC 24 48 FF FF FF         lea rbp, [rsp - 0xb8]
0087A731  48 81 EC B8 01 00 00            sub rsp, 0x1b8
0087A738  48 8B 05 01 00 59 00            mov rax, qword ptr [rip + 0x590001]
0087A73F  48 33 C4                        xor rax, rsp
0087A742  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
0087A749  48 8B 85 28 01 00 00            mov rax, qword ptr [rbp + 0x128]
0087A750  0F 57 C0                        xorps xmm0, xmm0
0087A753  4C 8B B5 48 01 00 00            mov r14, qword ptr [rbp + 0x148]
0087A75A  8B FA                           mov edi, edx
0087A75C  44 8B BD 20 01 00 00            mov r15d, dword ptr [rbp + 0x120]
0087A763  4C 8B E9                        mov r13, rcx
0087A766  89 55 A4                        mov dword ptr [rbp - 0x5c], edx
0087A769  0F 57 C9                        xorps xmm1, xmm1
0087A76C  48 8B 95 30 01 00 00            mov rdx, qword ptr [rbp + 0x130]
0087A773  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0087A777  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
0087A77E  48 89 55 20                     mov qword ptr [rbp + 0x20], rdx
0087A782  48 8B 95 40 01 00 00            mov rdx, qword ptr [rbp + 0x140]
0087A789  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
0087A78D  33 C9                           xor ecx, ecx
0087A78F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0087A793  8B F1                           mov esi, ecx
0087A795  33 C0                           xor eax, eax
0087A797  48 89 55 28                     mov qword ptr [rbp + 0x28], rdx
0087A79B  89 4D A0                        mov dword ptr [rbp - 0x60], ecx
0087A79E  44 8B E1                        mov r12d, ecx
0087A7A1  88 4C 24 60                     mov byte ptr [rsp + 0x60], cl
0087A7A5  33 D2                           xor edx, edx
0087A7A7  88 4C 24 62                     mov byte ptr [rsp + 0x62], cl
0087A7AB  49 89 08                        mov qword ptr [r8], rcx
0087A7AE  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0087A7B3  88 4C 24 61                     mov byte ptr [rsp + 0x61], cl
0087A7B7  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0087A7BB  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
0087A7C2  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0087A7C9  48 89 45 00                     mov qword ptr [rbp], rax
0087A7CD  89 45 08                        mov dword ptr [rbp + 8], eax
0087A7D0  4C 89 4D 38                     mov qword ptr [rbp + 0x38], r9
0087A7D4  4C 89 45 30                     mov qword ptr [rbp + 0x30], r8
0087A7D8  0F 11 45 68                     movups xmmword ptr [rbp + 0x68], xmm0
0087A7DC  C7 45 88 02 00 00 00            mov dword ptr [rbp - 0x78], 2
0087A7E3  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
0087A7E7  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
0087A7EB  0F 11 8D 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm1
0087A7F2  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
0087A7F6  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0087A7FA  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0087A7FE  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0087A802  E8 79 FF BA FF                  call 0x14042a780
0087A807  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0087A80B  E8 D0 B6 C1 FF                  call 0x140495ee0
0087A810  48 8D 55 A8                     lea rdx, [rbp - 0x58]
0087A814  E8 53 E7 BF FF                  call 0x140478f6c
0087A819  8B D8                           mov ebx, eax
0087A81B  85 C0                           test eax, eax
0087A81D  0F 88 62 03 00 00               js 0x14087ab85
0087A823  4C 8D 4D C0                     lea r9, [rbp - 0x40]
0087A827  4D 8B C6                        mov r8, r14
0087A82A  8B D7                           mov edx, edi
0087A82C  49 8B CD                        mov rcx, r13
0087A82F  E8 A8 05 00 00                  call 0x14087addc
0087A834  45 33 C9                        xor r9d, r9d
0087A837  8B D8                           mov ebx, eax
0087A839  85 C0                           test eax, eax
0087A83B  0F 88 03 05 00 00               js 0x14087ad44
0087A841  41 8B D7                        mov edx, r15d
0087A844  41 8D 4C 24 01                  lea ecx, [r12 + 1]
0087A849  41 8B C7                        mov eax, r15d
0087A84C  83 E2 20                        and edx, 0x20
0087A84F  0F 85 1C 03 00 00               jne 0x14087ab71
0087A855  24 08                           and al, 8
0087A857  44 89 4C 24 7C                  mov dword ptr [rsp + 0x7c], r9d
0087A85C  F6 D8                           neg al
0087A85E  1B C9                           sbb ecx, ecx
0087A860  F7 D1                           not ecx
0087A862  83 E1 03                        and ecx, 3
0087A865  44 8B C1                        mov r8d, ecx
0087A868  41 0F BA E8 11                  bts r8d, 0x11
0087A86D  85 FF                           test edi, edi
0087A86F  44 0F 45 C1                     cmovne r8d, ecx
0087A873  41 8D 4C 24 01                  lea ecx, [r12 + 1]
0087A878  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
0087A87D  85 FF                           test edi, edi
0087A87F  0F 85 1E 03 00 00               jne 0x14087aba3
0087A885  C7 44 24 78 80 00 00 00         mov dword ptr [rsp + 0x78], 0x80
0087A88D  44 84 F9                        test cl, r15b
0087A890  0F 85 BB 04 00 00               jne 0x14087ad51
0087A896  8B F9                           mov edi, ecx
0087A898  41 BD 24 C0 00 00               mov r13d, 0xc024
0087A89E  41 0F BA E7 08                  bt r15d, 8
0087A8A3  0F 82 BA 04 00 00               jb 0x14087ad63
0087A8A9  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
0087A8AD  48 85 DB                        test rbx, rbx
0087A8B0  0F 85 8C 03 00 00               jne 0x14087ac42
0087A8B6  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
0087A8BA  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0087A8BE  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
0087A8C3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
0087A8C8  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0087A8CD  41 8B C7                        mov eax, r15d
0087A8D0  83 E0 40                        and eax, 0x40
0087A8D3  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
0087A8D8  83 C8 24                        or eax, 0x24
0087A8DB  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
0087A8DF  C1 E0 04                        shl eax, 4
0087A8E2  89 45 F8                        mov dword ptr [rbp - 8], eax
0087A8E5  48 8D 45 C0                     lea rax, [rbp - 0x40]
0087A8E9  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0087A8ED  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0087A8F1  48 89 45 00                     mov qword ptr [rbp], rax
0087A8F5  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0087A8F9  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0087A8FD  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0087A901  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0087A905  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0087A90A  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
0087A90E  4C 89 4D 08                     mov qword ptr [rbp + 8], r9
0087A912  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0087A916  C7 45 E0 30 00 00 00            mov dword ptr [rbp - 0x20], 0x30
0087A91D  E8 4E 32 E3 FF                  call 0x1406adb70
0087A922  41 B9 22 00 00 C0               mov r9d, 0xc0000022
0087A928  8B D8                           mov ebx, eax
0087A92A  BF 23 00 00 00                  mov edi, 0x23
0087A92F  41 3B C1                        cmp eax, r9d
0087A932  75 75                           jne 0x14087a9a9
0087A934  44 8B C7                        mov r8d, edi
0087A937  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
0087A93F  8D 57 DE                        lea edx, [rdi - 0x22]
0087A942  49 8B CE                        mov rcx, r14
0087A945  E8 0A 46 BF FF                  call 0x14046ef54
0087A94A  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
0087A950  48 8D 55 40                     lea rdx, [rbp + 0x40]
0087A954  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
0087A95A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0087A95E  0F 57 C0                        xorps xmm0, xmm0
0087A961  33 C0                           xor eax, eax
0087A963  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0087A967  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0087A96B  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
0087A96F  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
0087A973  E8 F8 2E E3 FF                  call 0x1406ad870
0087A978  8B D8                           mov ebx, eax
0087A97A  85 C0                           test eax, eax
0087A97C  0F 89 EF 03 00 00               jns 0x14087ad71
0087A982  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
0087A98A  33 D2                           xor edx, edx
0087A98C  44 8B C8                        mov r9d, eax
0087A98F  49 8B CE                        mov rcx, r14
0087A992  44 8D 42 24                     lea r8d, [rdx + 0x24]
0087A996  E8 B9 45 BF FF                  call 0x14046ef54
0087A99B  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0087A9A0  48 85 C9                        test rcx, rcx
0087A9A3  0F 85 0A 04 00 00               jne 0x14087adb3
0087A9A9  80 7C 24 61 00                  cmp byte ptr [rsp + 0x61], 0
0087A9AE  0F 85 4E 02 00 00               jne 0x14087ac02
0087A9B4  85 DB                           test ebx, ebx
0087A9B6  0F 88 85 01 00 00               js 0x14087ab41
0087A9BC  8B 75 98                        mov esi, dword ptr [rbp - 0x68]
0087A9BF  45 33 ED                        xor r13d, r13d
0087A9C2  41 F6 C7 28                     test r15b, 0x28
0087A9C6  75 3B                           jne 0x14087aa03
0087A9C8  66 0F 6F 05 80 5E 79 FF         movdqa xmm0, xmmword ptr [rip - 0x86a180]
0087A9D0  45 8D 4D 28                     lea r9d, [r13 + 0x28]
0087A9D4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087A9D9  4C 8D 45 68                     lea r8, [rbp + 0x68]
0087A9DD  66 0F 6F C8                     movdqa xmm1, xmm0
0087A9E1  44 89 AD 88 00 00 00            mov dword ptr [rbp + 0x88], r13d
0087A9E8  48 8D 55 90                     lea rdx, [rbp - 0x70]
0087A9EC  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0087A9F4  F3 0F 7F 45 68                  movdqu xmmword ptr [rbp + 0x68], xmm0
0087A9F9  F3 0F 7F 45 78                  movdqu xmmword ptr [rbp + 0x78], xmm0
0087A9FE  E8 AD 2B E3 FF                  call 0x1406ad5b0
0087AA03  BB 02 00 00 00                  mov ebx, 2
0087AA08  44 84 FB                        test bl, r15b
0087AA0B  0F 85 C7 D9 29 00               jne 0x140b183d8
0087AA11  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
0087AA15  48 8D 45 A0                     lea rax, [rbp - 0x60]
0087AA19  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087AA1E  45 33 C9                        xor r9d, r9d
0087AA21  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
0087AA26  45 33 C0                        xor r8d, r8d
0087AA29  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
0087AA2E  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
0087AA36  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0087AA3B  48 8D 45 90                     lea rax, [rbp - 0x70]
0087AA3F  C7 44 24 28 40 C0 09 00         mov dword ptr [rsp + 0x28], 0x9c040
0087AA47  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087AA4C  E8 9F 2D E3 FF                  call 0x1406ad7f0
0087AA51  3D 03 01 00 00                  cmp eax, 0x103
0087AA56  75 09                           jne 0x14087aa61
0087AA58  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0087AA5C  E8 5B 3A C2 FF                  call 0x14049e4bc
0087AA61  44 39 6D A4                     cmp dword ptr [rbp - 0x5c], r13d
0087AA65  75 62                           jne 0x14087aac9
0087AA67  3B F3                           cmp esi, ebx
0087AA69  74 31                           je 0x14087aa9c
0087AA6B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087AA70  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
0087AA77  41 B9 18 00 00 00               mov r9d, 0x18
0087AA7D  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
0087AA85  48 8D 55 90                     lea rdx, [rbp - 0x70]
0087AA89  E8 62 28 E3 FF                  call 0x1406ad2f0
0087AA8E  85 C0                           test eax, eax
0087AA90  78 0A                           js 0x14087aa9c
0087AA92  4C 39 AD 98 00 00 00            cmp qword ptr [rbp + 0x98], r13
0087AA99  0F 44 F3                        cmove esi, ebx
0087AA9C  4C 8B 7D 20                     mov r15, qword ptr [rbp + 0x20]
0087AAA0  4D 85 FF                        test r15, r15
0087AAA3  0F 85 1F 01 00 00               jne 0x14087abc8
0087AAA9  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0087AAAD  48 85 C0                        test rax, rax
0087AAB0  74 17                           je 0x14087aac9
0087AAB2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087AAB7  48 8B D0                        mov rdx, rax
0087AABA  E8 59 08 00 00                  call 0x14087b318
0087AABF  8B D8                           mov ebx, eax
0087AAC1  85 C0                           test eax, eax
0087AAC3  0F 88 F4 02 00 00               js 0x14087adbd
0087AAC9  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0087AACE  41 8B DD                        mov ebx, r13d
0087AAD1  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0087AAD5  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0087AADA  48 89 01                        mov qword ptr [rcx], rax
0087AADD  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
0087AAE1  89 30                           mov dword ptr [rax], esi
0087AAE3  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0087AAE7  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0087AAEB  48 85 C9                        test rcx, rcx
0087AAEE  74 0B                           je 0x14087aafb
0087AAF0  49 3B 4D 08                     cmp rcx, qword ptr [r13 + 8]
0087AAF4  74 05                           je 0x14087aafb
0087AAF6  E8 85 B2 BF FF                  call 0x140475d80
0087AAFB  4D 85 E4                        test r12, r12
0087AAFE  0F 85 99 01 00 00               jne 0x14087ac9d
0087AB04  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0087AB08  E8 7F D3 C0 FF                  call 0x140487e8c
0087AB0D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087AB12  48 85 C9                        test rcx, rcx
0087AB15  0F 85 AF 02 00 00               jne 0x14087adca
0087AB1B  8B C3                           mov eax, ebx
0087AB1D  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
0087AB24  48 33 CC                        xor rcx, rsp
0087AB27  E8 14 1B E3 FF                  call 0x1406ac640
0087AB2C  48 81 C4 B8 01 00 00            add rsp, 0x1b8
0087AB33  41 5F                           pop r15
0087AB35  41 5E                           pop r14
0087AB37  41 5D                           pop r13
0087AB39  41 5C                           pop r12
0087AB3B  5F                              pop rdi
0087AB3C  5E                              pop rsi
0087AB3D  5B                              pop rbx
0087AB3E  5D                              pop rbp
0087AB3F  C3                              ret
0087AB40  CC                              int3
0087AB41  44 8B 4C 24 7C                  mov r9d, dword ptr [rsp + 0x7c]
0087AB46  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0087AB4A  45 8B C5                        mov r8d, r13d
0087AB4D  8B D3                           mov edx, ebx
0087AB4F  E8 58 03 00 00                  call 0x14087aeac
0087AB54  C7 44 24 20 50 00 00 00         mov dword ptr [rsp + 0x20], 0x50
0087AB5C  44 8B CB                        mov r9d, ebx
0087AB5F  44 8B C7                        mov r8d, edi
0087AB62  33 D2                           xor edx, edx
0087AB64  49 8B CE                        mov rcx, r14
0087AB67  E8 E8 43 BF FF                  call 0x14046ef54
0087AB6C  E9 72 FF FF FF                  jmp 0x14087aae3
0087AB71  C1 E8 07                        shr eax, 7
0087AB74  F7 D0                           not eax
0087AB76  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0087AB7A  23 C1                           and eax, ecx
0087AB7C  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0087AB80  E9 F8 FC FF FF                  jmp 0x14087a87d
0087AB85  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
0087AB8D  33 D2                           xor edx, edx
0087AB8F  44 8B C8                        mov r9d, eax
0087AB92  49 8B CE                        mov rcx, r14
0087AB95  44 8D 42 23                     lea r8d, [rdx + 0x23]
0087AB99  E8 B6 43 BF FF                  call 0x14046ef54
0087AB9E  E9 44 FF FF FF                  jmp 0x14087aae7
0087ABA3  C7 44 24 78 06 00 00 00         mov dword ptr [rsp + 0x78], 6
0087ABAB  85 D2                           test edx, edx
0087ABAD  75 3F                           jne 0x14087abee
0087ABAF  41 8A C7                        mov al, r15b
0087ABB2  24 10                           and al, 0x10
0087ABB4  F6 D8                           neg al
0087ABB6  1B FF                           sbb edi, edi
0087ABB8  F7 D7                           not edi
0087ABBA  83 E7 03                        and edi, 3
0087ABBD  41 BD 04 80 00 00               mov r13d, 0x8004
0087ABC3  E9 D6 FC FF FF                  jmp 0x14087a89e
0087ABC8  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087ABCD  49 8B D7                        mov rdx, r15
0087ABD0  E8 FF 07 00 00                  call 0x14087b3d4
0087ABD5  8B D8                           mov ebx, eax
0087ABD7  85 C0                           test eax, eax
0087ABD9  78 17                           js 0x14087abf2
0087ABDB  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087ABE0  E8 33 0B 00 00                  call 0x14087b718
0087ABE5  41 89 47 04                     mov dword ptr [r15 + 4], eax
0087ABE9  E9 BB FE FF FF                  jmp 0x14087aaa9
0087ABEE  8B F9                           mov edi, ecx
0087ABF0  EB CB                           jmp 0x14087abbd
0087ABF2  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0087ABFA  44 8B C8                        mov r9d, eax
0087ABFD  E9 5D FF FF FF                  jmp 0x14087ab5f
0087AC02  4D 85 E4                        test r12, r12
0087AC05  0F 84 2F 01 00 00               je 0x14087ad3a
0087AC0B  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
0087AC0E  49 8B D4                        mov rdx, r12
0087AC11  44 8A 4C 24 62                  mov r9b, byte ptr [rsp + 0x62]
0087AC16  48 8B CE                        mov rcx, rsi
0087AC19  44 8A 44 24 60                  mov r8b, byte ptr [rsp + 0x60]
0087AC1E  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087AC22  E8 E9 11 05 00                  call 0x1408cbe10
0087AC27  85 C0                           test eax, eax
0087AC29  0F 89 85 FD FF FF               jns 0x14087a9b4
0087AC2F  45 33 C9                        xor r9d, r9d
0087AC32  45 33 C0                        xor r8d, r8d
0087AC35  49 8B D4                        mov rdx, r12
0087AC38  41 8D 49 26                     lea ecx, [r9 + 0x26]
0087AC3C  E8 F7 32 DF FF                  call 0x14066df38
0087AC41  CC                              int3
0087AC42  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
0087AC4B  8B 86 A0 05 00 00               mov eax, dword ptr [rsi + 0x5a0]
0087AC51  A8 08                           test al, 8
0087AC53  75 5A                           jne 0x14087acaf
0087AC55  8B 83 C4 00 00 00               mov eax, dword ptr [rbx + 0xc4]
0087AC5B  45 33 C9                        xor r9d, r9d
0087AC5E  45 33 C0                        xor r8d, r8d
0087AC61  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087AC65  48 8B D3                        mov rdx, rbx
0087AC68  48 8B CE                        mov rcx, rsi
0087AC6B  E8 A0 11 05 00                  call 0x1408cbe10
0087AC70  45 33 C9                        xor r9d, r9d
0087AC73  8B D8                           mov ebx, eax
0087AC75  85 C0                           test eax, eax
0087AC77  79 16                           jns 0x14087ac8f
0087AC79  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
0087AC81  44 8B C8                        mov r9d, eax
0087AC84  41 B8 23 00 00 00               mov r8d, 0x23
0087AC8A  E9 D3 FE FF FF                  jmp 0x14087ab62
0087AC8F  41 83 CF 40                     or r15d, 0x40
0087AC93  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
0087AC98  E9 19 FC FF FF                  jmp 0x14087a8b6
0087AC9D  BA 44 66 6C 74                  mov edx, 0x746c6644
0087ACA2  49 8B CC                        mov rcx, r12
0087ACA5  E8 36 CC A7 FF                  call 0x1402f78e0
0087ACAA  E9 55 FE FF FF                  jmp 0x14087ab04
0087ACAF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0087ACB8  48 8B CE                        mov rcx, rsi
0087ACBB  48 8B D0                        mov rdx, rax
0087ACBE  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0087ACC2  E8 59 9A B4 FF                  call 0x1403c4720
0087ACC7  8B 86 A0 05 00 00               mov eax, dword ptr [rsi + 0x5a0]
0087ACCD  A8 08                           test al, 8
0087ACCF  74 58                           je 0x14087ad29
0087ACD1  4C 8B A6 48 06 00 00            mov r12, qword ptr [rsi + 0x648]
0087ACD8  4D 85 E4                        test r12, r12
0087ACDB  75 1C                           jne 0x14087acf9
0087ACDD  4C 8B A6 38 05 00 00            mov r12, qword ptr [rsi + 0x538]
0087ACE4  49 83 E4 F8                     and r12, 0xfffffffffffffff8
0087ACE8  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
0087ACED  F7 86 A0 05 00 00 00 01 00 00   test dword ptr [rsi + 0x5a0], 0x100
0087ACF7  75 05                           jne 0x14087acfe
0087ACF9  C6 44 24 60 00                  mov byte ptr [rsp + 0x60], 0
0087ACFE  BA 44 66 6C 74                  mov edx, 0x746c6644
0087AD03  49 8B CC                        mov rcx, r12
0087AD06  BB 38 05 00 00                  mov ebx, 0x538
0087AD0B  E8 00 5A 99 FF                  call 0x140210710
0087AD10  8B 04 33                        mov eax, dword ptr [rbx + rsi]
0087AD13  83 E0 03                        and eax, 3
0087AD16  89 45 88                        mov dword ptr [rbp - 0x78], eax
0087AD19  8A 04 33                        mov al, byte ptr [rbx + rsi]
0087AD1C  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
0087AD20  C0 E8 02                        shr al, 2
0087AD23  24 01                           and al, 1
0087AD25  88 44 24 62                     mov byte ptr [rsp + 0x62], al
0087AD29  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0087AD2D  48 8B CE                        mov rcx, rsi
0087AD30  E8 0B 81 B4 FF                  call 0x1403c2e40
0087AD35  E9 1B FF FF FF                  jmp 0x14087ac55
0087AD3A  E8 C1 24 05 00                  call 0x1408cd200
0087AD3F  E9 70 FC FF FF                  jmp 0x14087a9b4
0087AD44  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0087AD4C  E9 3C FE FF FF                  jmp 0x14087ab8d
0087AD51  BF 03 00 00 00                  mov edi, 3
0087AD56  85 D2                           test edx, edx
0087AD58  0F 84 3A FB FF FF               je 0x14087a898
0087AD5E  E9 33 FB FF FF                  jmp 0x14087a896
0087AD63  41 83 E5 DF                     and r13d, 0xffffffdf
0087AD67  41 0F BA ED 10                  bts r13d, 0x10
0087AD6C  E9 38 FB FF FF                  jmp 0x14087a8a9
0087AD71  83 65 60 FE                     and dword ptr [rbp + 0x60], 0xfffffffe
0087AD75  4C 8D 4D D0                     lea r9, [rbp - 0x30]
0087AD79  C7 44 24 28 00 40 00 00         mov dword ptr [rsp + 0x28], 0x4000
0087AD81  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0087AD85  BA 00 01 00 00                  mov edx, 0x100
0087AD8A  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0087AD92  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0087AD97  E8 94 29 E3 FF                  call 0x1406ad730
0087AD9C  8B D8                           mov ebx, eax
0087AD9E  85 C0                           test eax, eax
0087ADA0  0F 89 98 D5 29 00               jns 0x140b1833e
0087ADA6  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0087ADAE  E9 D7 FB FF FF                  jmp 0x14087a98a
0087ADB3  E8 F8 24 E3 FF                  call 0x1406ad2b0
0087ADB8  E9 EC FB FF FF                  jmp 0x14087a9a9
0087ADBD  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
0087ADC5  E9 30 FE FF FF                  jmp 0x14087abfa
0087ADCA  E8 E1 24 E3 FF                  call 0x1406ad2b0
0087ADCF  E9 47 FD FF FF                  jmp 0x14087ab1b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpOpenHiveFile(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int8 v_stack_m196;
    unsigned __int8 v_stack_m197;
    unsigned __int8 v_stack_m198;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p60;
    unsigned __int8 v_stack_p61;
    unsigned __int8 v_stack_p62;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_p7C;

    v_rsp = (v_rsp) - (440);
    result = (*(unsigned __int64 *)(v_rip + 5832705)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_m154 = a2;
    v_stack_m140 = a6;
    v_stack_mD8 = a7;
    v_stack_m178 = a1;
    a1 = 0;
    v_stack_m128 = a8;
    result = 0;
    v_stack_mD0 = a9;
    v_stack_m158 = 0;
    v_stack_m198 = 0;
    a2 = 0;
    v_stack_m196 = 0;
    *(unsigned __int64 *)(a3) = 0;
    v_stack_m190 = 0;
    v_stack_m197 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_mC0 = a4;
    v_stack_mC8 = a3;
    v_stack_m90 = v_xmm0;
    v_stack_m170 = 2;
    v_stack_m80 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m168 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m138 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m138, a2, a3, a4);
    result = CmSiEventTupleInitialize(v_stack_m150, a2, a3, a4);
    result = CmSiCreateEvent(v_stack_m150, v_stack_m150, a3, a4);
    if (sign_flag) goto loc_0087AB85;
    result = CmpGetCompleteFileName(0, (unsigned int)((unsigned int)((unsigned int)(a2))), a10, v_stack_m138);
    a4 = 0;
    if (sign_flag) goto loc_0087AD44;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (32));
    if (condition_is_not_equal) goto loc_0087AB71;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (8));
    v_stack_m17C = 0;
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)(~(0 + 1));
    a1 = (unsigned int)((a1) & (3));
    a3 = (unsigned int)((unsigned int)(a1));
    if ((unsigned int)((unsigned int)(a2)) != 0) { a3 = (unsigned int)(a1); }
    v_stack_m188 = (unsigned int)(a3);
loc_0087A87D:
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_0087ABA3;
    v_stack_m180 = 128;
    if ((((unsigned __int8)(0 + 1)) & ((unsigned __int8)((unsigned int)(a5)))) != 0) goto loc_0087AD51;
loc_0087A896:
loc_0087A898:
loc_0087A89E:
    if (condition_is_below) goto loc_0087AD63;
loc_0087A8A9:
    if (v_stack_m140 != 0) goto loc_0087AC42;
loc_0087A8B6:
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (64));
    v_stack_m1B8 = (unsigned int)((unsigned int)(0xC024ULL));
    result = (unsigned int)((result) | (36));
    v_stack_m1C0 = (unsigned int)((unsigned int)((unsigned int)(0 + 1)));
    result = (unsigned int)((result) << (4));
    v_stack_m100 = (unsigned int)(result);
    v_stack_m108 = v_stack_m138;
    v_stack_mF8 = v_stack_m128;
    v_stack_m1C8 = (unsigned int)((unsigned int)(v_stack_m17C));
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_stack_m180));
    v_stack_m1D8 = 0;
    v_stack_m110 = 0;
    v_stack_mF0 = 0;
    v_stack_m118 = 48;
    result = ZwCreateFile(v_stack_m190, (unsigned int)(v_stack_m188), v_stack_m118, v_stack_m168);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000022ULL)))) goto loc_0087A9A9;
    v_stack_m1D8 = 64;
    result = SetFailureLocation(a10, 35 - 34, 35, (unsigned int)(0xC0000022ULL));
    result = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m98 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = ZwQueryAttributesFile(v_stack_m118, v_stack_mB8, 35, (unsigned int)(0xC0000022ULL));
    if (!sign_flag) goto loc_0087AD71;
    v_stack_m1D8 = 16;
loc_0087A98A:
    a2 = 0;
    result = SetFailureLocation(a10, a2, a2 + 36, (unsigned int)((unsigned int)(result)));
    if (v_stack_m188 != 0) goto loc_0087ADB3;
loc_0087A9A9:
    if (v_stack_m197 != 0) goto loc_0087AC02;
loc_0087A9B4:
    if (sign_flag) goto loc_0087AB41;
    v_r13 = 0;
    if ((((unsigned __int8)((unsigned int)(a5))) & (40)) == 0) {
        a4 = v_r13 + 40;
        a1 = v_stack_m190;
        a3 = v_stack_m90;
        v_stack_m70 = 0;
        a2 = v_stack_m168;
        v_stack_m1D8 = 4;
        v_stack_m90 = v_xmm0;
        v_stack_m80 = v_xmm0;
        result = ZwSetInformationFile(a1, a2, a3, a4);
    }
    a4 = 0;
    v_stack_m1B0 = 0;
    a3 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = 4;
    v_stack_m1C8 = v_stack_m158;
    v_stack_m1D0 = 0x9C040ULL;
    v_stack_m1D8 = v_stack_m168;
    result = ZwFsControlFile(v_stack_m190, v_stack_m150, a3, a4);
    if (((unsigned int)(result)) == 259) {
        a1 = v_stack_m150;
        result = CmSiWaitForSingleEvent(a1, v_stack_m150, a3, a4);
    }
    if (v_stack_m154 != 0) goto loc_0087AAC9;
    if (((unsigned int)((unsigned int)(v_stack_m160))) == 2) goto loc_0087AA9C;
    v_stack_m1D8 = 5;
    result = ZwQueryInformationFile(v_stack_m190, v_stack_m168, v_stack_m68, 24);
    v_rsi = (unsigned int)(v_stack_m160);
    if (!(sign_flag)) {
        v_rsi = (unsigned int)(v_stack_m160);
        if (v_stack_m60 == 0) { v_rsi = 2; }
    }
    if (v_stack_mD8 != 0) goto loc_0087ABC8;
loc_0087AAA9:
    if (v_stack_mD0 == 0) goto loc_0087AAC9;
    result = CmpQueryFileSecurityDescriptor(v_stack_m190, v_stack_mD0, v_stack_m68, 24);
    if (sign_flag) goto loc_0087ADBD;
loc_0087AAC9:
    v_stack_m190 = 0;
    *(unsigned __int64 *)(v_stack_mC8) = v_stack_m190;
    *(unsigned int *)(v_stack_mC0) = (unsigned int)(v_rsi);
loc_0087AAE3:
loc_0087AAE7:
    if (v_stack_m130 == 0) goto loc_0087AAFB;
    result = v_stack_mC0;
    if (v_stack_m130 != (*(unsigned __int64 *)(v_stack_m178 + 8))) {
        result = CmSiFreeMemory(v_stack_m130, v_stack_mD0, v_stack_m68, 24);
    }
    if (0 != 0) goto loc_0087AC9D;
loc_0087AB04:
    result = CmSiEventTupleCleanup(v_stack_m150, v_stack_mD0, v_stack_m68, 24);
    if (v_stack_m190 != 0) goto loc_0087ADCA;
loc_0087AB1B:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mD0, v_stack_m68, 24);
    v_rsp = (v_rsp) + (440);
    return result;
loc_0087AB41:
    result = CmpLogHiveFileInaccessible(v_stack_m138, 0, (unsigned int)((unsigned int)(v_stack_m178)), (unsigned int)(v_stack_p7C));
    v_stack_p20 = 80;
loc_0087AB5F:
loc_0087AB62:
    a2 = 0;
    result = SetFailureLocation(a10, a2, 35, 0);
    goto loc_0087AAE3;
loc_0087AB71:
    result = (unsigned int)((result) >> (7));
    result = (unsigned int)(~(result));
    v_stack_p70 = (unsigned int)(a10);
    result = (unsigned int)((result) & ((unsigned int)(a10)));
    v_stack_p7C = (unsigned int)(result);
    goto loc_0087A87D;
loc_0087AB85:
    v_stack_p20 = 16;
loc_0087AB8D:
    a2 = 0;
    result = SetFailureLocation(a10, a2, a2 + 35, (unsigned int)((unsigned int)(result)));
    goto loc_0087AAE7;
loc_0087ABA3:
    v_stack_p78 = 6;
    if (0 != 0) goto loc_0087ABEE;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_mD8)) & (16));
    result = (unsigned __int8)(-(result));
    v_rdi = (unsigned int)(~(35));
    v_rdi = (unsigned int)((v_rdi) & (3));
loc_0087ABBD:
    goto loc_0087A89E;
loc_0087ABC8:
    result = CmpGetVolumeClusterSize(v_stack_p68, v_stack_mD8, a2 + 35, (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_0087ABF2;
    result = CmpGetVolumeLogFileSizeCap(v_stack_p68, v_stack_mD8, a2 + 35, (unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_stack_mD8 + 4) = (unsigned int)(result);
    goto loc_0087AAA9;
loc_0087ABEE:
    goto loc_0087ABBD;
loc_0087ABF2:
    v_stack_p20 = 112;
loc_0087ABFA:
    goto loc_0087AB5F;
loc_0087AC02:
    if (0 == 0) goto loc_0087AD3A;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m170));
    result = PsImpersonateClient(v_rsi, 0, v_stack_p60, v_stack_p62);
    if (!sign_flag) goto loc_0087A9B4;
    a4 = 0;
    a3 = 0;
    result = CmSiBugCheck(a4 + 38, 0, a3, a4);
loc_0087AC42:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) goto loc_0087ACAF;
loc_0087AC55:
    a4 = 0;
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 196)));
    result = PsImpersonateClient(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(result)), a3, a4);
    a4 = 0;
    if (!sign_flag) goto loc_0087AC8F;
    v_stack_p20 = 48;
    goto loc_0087AB62;
loc_0087AC8F:
    v_r15 = (unsigned int)((v_stack_mD8) | (64));
    v_stack_p61 = 1;
    goto loc_0087A8B6;
loc_0087AC9D:
    result = ObfDereferenceObjectWithTag(0, (unsigned int)(0x746C6644ULL), 35, (unsigned int)((unsigned int)(result)));
    goto loc_0087AB04;
loc_0087ACAF:
    v_stack_mE0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PspLockThreadSecurityShared(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), 35, (unsigned int)((unsigned int)(result)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) == 0) goto loc_0087AD29;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1608) != 0) goto loc_0087ACF9;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336)) & (-8);
    v_stack_p60 = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)) & (256)) == 0) {
        v_stack_p60 = 0;
    }
    result = ObfReferenceObjectWithTag(v_r12, (unsigned int)(0x746C6644ULL), 35, (unsigned int)((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0x538ULL) + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1))) & (3));
    v_stack_m170 = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(0x538ULL) + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1)) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_p62 = (unsigned __int8)(result);
loc_0087AD29:
    result = PspUnlockThreadSecurityShared(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mE0, 35, (unsigned int)((unsigned int)(result)));
    goto loc_0087AC55;
loc_0087AD3A:
    result = PsRevertToSelf(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mE0, 35, (unsigned int)((unsigned int)(result)));
    goto loc_0087A9B4;
loc_0087AD44:
    v_stack_p20 = 32;
    goto loc_0087AB8D;
loc_0087AD51:
    if ((unsigned int)(v_stack_mE0) == 0) goto loc_0087A898;
    goto loc_0087A896;
loc_0087AD63:
    v_r13 = (unsigned int)(((unsigned int)(0x8004ULL)) & (0xFFFFFFDFULL));
    goto loc_0087A8A9;
loc_0087AD71:
    v_stack_p28 = 0x4000ULL;
    v_stack_p20 = 7;
    result = ZwOpenFile(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    v_stack_p20 = 32;
    goto loc_0087A98A;
loc_0087ADB3:
    result = ZwClose(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    goto loc_0087A9A9;
loc_0087ADBD:
    v_stack_p20 = 128;
    goto loc_0087ABFA;
loc_0087ADCA:
    result = ZwClose(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    goto loc_0087AB1B;
}
```

## 5. (Beta) C Style

```c
int64_t CmpOpenHiveFile(int64_t Arg1, int32_t Arg2, void *Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint8_t v_stack_m196;
    uint8_t v_stack_m197;
    uint8_t v_stack_m198;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p60;
    uint8_t v_stack_p61;
    uint8_t v_stack_p62;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_p7C;

    local_rsp = (local_rsp) - (440);
    result = (*(uint64_t *)(v_rip + 0x590001)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_m154 = Arg2;
    v_stack_m140 = Arg6;
    v_stack_mD8 = Arg7;
    v_stack_m178 = Arg1;
    Arg1 = 0;
    v_stack_m128 = Arg8;
    result = 0;
    v_stack_mD0 = Arg9;
    v_stack_m158 = 0;
    v_stack_m198 = 0;
    Arg2 = 0;
    v_stack_m196 = 0;
    *(uint64_t *)(arg3) = 0;
    v_stack_m190 = 0;
    v_stack_m197 = 0;
    v_stack_m70 = 0;
    v_stack_m58 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_mC0 = Arg4;
    v_stack_mC8 = Arg3;
    v_stack_m90 = v_xmm0;
    v_stack_m170 = 2;
    v_stack_m80 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m68 = v_xmm1;
    v_stack_m168 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m138 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m138, Arg2, Arg3, Arg4);
    result = CmSiEventTupleInitialize(v_stack_m150, Arg2, Arg3, Arg4);
    result = CmSiCreateEvent(v_stack_m150, v_stack_m150, Arg3, Arg4);
    if (sign_flag) goto loc_0087AB85;
    result = CmpGetCompleteFileName(0, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg10, v_stack_m138);
    Arg4 = 0;
    if (sign_flag) goto loc_0087AD44;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (32));
    if (condition_is_not_equal) goto loc_0087AB71;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (8));
    v_stack_m17C = 0;
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)(~(0 + 1));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg3 = (uint32_t)((uint32_t)(Arg1));
    if ((uint32_t)((uint32_t)(Arg2)) != 0) { Arg3 = (uint32_t)(Arg1); }
    v_stack_m188 = (uint32_t)(Arg3);
loc_0087A87D:
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_0087ABA3;
    v_stack_m180 = 128;
    if ((((uint8_t)(0 + 1)) & ((uint8_t)((uint32_t)(Arg5)))) != 0) goto loc_0087AD51;
loc_0087A896:
loc_0087A898:
loc_0087A89E:
    if (condition_is_below) goto loc_0087AD63;
loc_0087A8A9:
    if (v_stack_m140 != 0) goto loc_0087AC42;
loc_0087A8B6:
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (64));
    v_stack_m1B8 = (uint32_t)((uint32_t)(0xC024ULL));
    result = (uint32_t)((result) | (36));
    v_stack_m1C0 = (uint32_t)((uint32_t)((uint32_t)(0 + 1)));
    result = (uint32_t)((result) << (4));
    v_stack_m100 = (uint32_t)(result);
    v_stack_m108 = v_stack_m138;
    v_stack_mF8 = v_stack_m128;
    v_stack_m1C8 = (uint32_t)((uint32_t)(v_stack_m17C));
    v_stack_m1D0 = (uint32_t)((uint32_t)(v_stack_m180));
    v_stack_m1D8 = 0;
    v_stack_m110 = 0;
    v_stack_mF0 = 0;
    v_stack_m118 = 48;
    result = ZwCreateFile(v_stack_m190, (uint32_t)(v_stack_m188), v_stack_m118, v_stack_m168);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000022ULL)))) goto loc_0087A9A9;
    v_stack_m1D8 = 64;
    result = SetFailureLocation(Arg10, 35 - 34, 35, (uint32_t)(0xC0000022ULL));
    result = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m98 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = ZwQueryAttributesFile(v_stack_m118, v_stack_mB8, 35, (uint32_t)(0xC0000022ULL));
    if (!sign_flag) goto loc_0087AD71;
    v_stack_m1D8 = 16;
loc_0087A98A:
    Arg2 = 0;
    result = SetFailureLocation(Arg10, Arg2, Arg2 + 36, (uint32_t)((uint32_t)(result)));
    if (v_stack_m188 != 0) goto loc_0087ADB3;
loc_0087A9A9:
    if (v_stack_m197 != 0) goto loc_0087AC02;
loc_0087A9B4:
    if (sign_flag) goto loc_0087AB41;
    local_r13 = 0;
    if ((((uint8_t)((uint32_t)(Arg5))) & (40)) == 0) {
        Arg4 = local_r13 + 40;
        Arg1 = v_stack_m190;
        Arg3 = v_stack_m90;
        v_stack_m70 = 0;
        Arg2 = v_stack_m168;
        v_stack_m1D8 = 4;
        v_stack_m90 = v_xmm0;
        v_stack_m80 = v_xmm0;
        result = ZwSetInformationFile(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    v_stack_m1B0 = 0;
    Arg3 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = 4;
    v_stack_m1C8 = v_stack_m158;
    v_stack_m1D0 = 0x9C040ULL;
    v_stack_m1D8 = v_stack_m168;
    result = ZwFsControlFile(v_stack_m190, v_stack_m150, Arg3, Arg4);
    if (((uint32_t)(result)) == 259) {
        Arg1 = v_stack_m150;
        result = CmSiWaitForSingleEvent(Arg1, v_stack_m150, Arg3, Arg4);
    }
    if (v_stack_m154 != 0) goto loc_0087AAC9;
    if (((uint32_t)((uint32_t)(v_stack_m160))) == 2) goto loc_0087AA9C;
    v_stack_m1D8 = 5;
    result = ZwQueryInformationFile(v_stack_m190, v_stack_m168, v_stack_m68, 24);
    local_rsi = (uint32_t)(v_stack_m160);
    if (!(sign_flag)) {
        local_rsi = (uint32_t)(v_stack_m160);
        if (v_stack_m60 == 0) { local_rsi = 2; }
    }
    if (v_stack_mD8 != 0) goto loc_0087ABC8;
loc_0087AAA9:
    if (v_stack_mD0 == 0) goto loc_0087AAC9;
    result = CmpQueryFileSecurityDescriptor(v_stack_m190, v_stack_mD0, v_stack_m68, 24);
    if (sign_flag) goto loc_0087ADBD;
loc_0087AAC9:
    v_stack_m190 = 0;
    *(uint64_t *)(v_stack_mC8) = v_stack_m190;
    *(uint32_t *)(v_stack_mC0) = (uint32_t)(local_rsi);
loc_0087AAE3:
loc_0087AAE7:
    if (v_stack_m130 == 0) goto loc_0087AAFB;
    result = v_stack_mC0;
    if (v_stack_m130 != (*(uint64_t *)(v_stack_m178 + 0x8))) {
        result = CmSiFreeMemory(v_stack_m130, v_stack_mD0, v_stack_m68, 24);
    }
    if (0 != 0) goto loc_0087AC9D;
loc_0087AB04:
    result = CmSiEventTupleCleanup(v_stack_m150, v_stack_mD0, v_stack_m68, 24);
    if (v_stack_m190 != 0) goto loc_0087ADCA;
loc_0087AB1B:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mD0, v_stack_m68, 24);
    local_rsp = (local_rsp) + (440);
    return result;
loc_0087AB41:
    result = CmpLogHiveFileInaccessible(v_stack_m138, 0, (uint32_t)((uint32_t)(v_stack_m178)), (uint32_t)(v_stack_p7C));
    v_stack_p20 = 80;
loc_0087AB5F:
loc_0087AB62:
    Arg2 = 0;
    result = SetFailureLocation(Arg10, Arg2, 35, 0);
    goto loc_0087AAE3;
loc_0087AB71:
    result = (uint32_t)((result) >> (7));
    result = (uint32_t)(~(result));
    v_stack_p70 = (uint32_t)(Arg10);
    result = (uint32_t)((result) & ((uint32_t)(Arg10)));
    v_stack_p7C = (uint32_t)(result);
    goto loc_0087A87D;
loc_0087AB85:
    v_stack_p20 = 16;
loc_0087AB8D:
    Arg2 = 0;
    result = SetFailureLocation(Arg10, Arg2, Arg2 + 35, (uint32_t)((uint32_t)(result)));
    goto loc_0087AAE7;
loc_0087ABA3:
    v_stack_p78 = 6;
    if (0 != 0) goto loc_0087ABEE;
    result = (uint8_t)(((uint8_t)(v_stack_mD8)) & (16));
    result = (uint8_t)(-(result));
    local_rdi = (uint32_t)(~(35));
    local_rdi = (uint32_t)((local_rdi) & (3));
loc_0087ABBD:
    goto loc_0087A89E;
loc_0087ABC8:
    result = CmpGetVolumeClusterSize(v_stack_p68, v_stack_mD8, Arg2 + 35, (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_0087ABF2;
    result = CmpGetVolumeLogFileSizeCap(v_stack_p68, v_stack_mD8, Arg2 + 35, (uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_stack_mD8 + 0x4) = (uint32_t)(result);
    goto loc_0087AAA9;
loc_0087ABEE:
    goto loc_0087ABBD;
loc_0087ABF2:
    v_stack_p20 = 112;
loc_0087ABFA:
    goto loc_0087AB5F;
loc_0087AC02:
    if (0 == 0) goto loc_0087AD3A;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m170));
    result = PsImpersonateClient(local_rsi, 0, v_stack_p60, v_stack_p62);
    if (!sign_flag) goto loc_0087A9B4;
    Arg4 = 0;
    Arg3 = 0;
    result = CmSiBugCheck(Arg4 + 38, 0, Arg3, Arg4);
loc_0087AC42:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) goto loc_0087ACAF;
loc_0087AC55:
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xC4)));
    result = PsImpersonateClient(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    Arg4 = 0;
    if (!sign_flag) goto loc_0087AC8F;
    v_stack_p20 = 48;
    goto loc_0087AB62;
loc_0087AC8F:
    local_r15 = (uint32_t)((v_stack_mD8) | (64));
    v_stack_p61 = 1;
    goto loc_0087A8B6;
loc_0087AC9D:
    result = ObfDereferenceObjectWithTag(0, (uint32_t)(0x746C6644ULL), 35, (uint32_t)((uint32_t)(result)));
    goto loc_0087AB04;
loc_0087ACAF:
    v_stack_mE0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PspLockThreadSecurityShared(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), 35, (uint32_t)((uint32_t)(result)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) == 0) goto loc_0087AD29;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x648) != 0) goto loc_0087ACF9;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538)) & (-8);
    v_stack_p60 = 1;
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)) & (256)) == 0) {
        v_stack_p60 = 0;
    }
    result = ObfReferenceObjectWithTag(local_r12, (uint32_t)(0x746C6644ULL), 35, (uint32_t)((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0x538ULL) + *(uint64_t *)(gs_base + (0 + 0x188)) * 1))) & (3));
    v_stack_m170 = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)((uint32_t)(0x538ULL) + *(uint64_t *)(gs_base + (0 + 0x188)) * 1)) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_p62 = (uint8_t)(result);
loc_0087AD29:
    result = PspUnlockThreadSecurityShared(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mE0, 35, (uint32_t)((uint32_t)(result)));
    goto loc_0087AC55;
loc_0087AD3A:
    result = PsRevertToSelf(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mE0, 35, (uint32_t)((uint32_t)(result)));
    goto loc_0087A9B4;
loc_0087AD44:
    v_stack_p20 = 32;
    goto loc_0087AB8D;
loc_0087AD51:
    if ((uint32_t)(v_stack_mE0) == 0) goto loc_0087A898;
    goto loc_0087A896;
loc_0087AD63:
    local_r13 = (uint32_t)(((uint32_t)(0x8004ULL)) & (0xFFFFFFDFULL));
    goto loc_0087A8A9;
loc_0087AD71:
    v_stack_p28 = 0x4000ULL;
    v_stack_p20 = 7;
    result = ZwOpenFile(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    v_stack_p20 = 32;
    goto loc_0087A98A;
loc_0087ADB3:
    result = ZwClose(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    goto loc_0087A9A9;
loc_0087ADBD:
    v_stack_p20 = 128;
    goto loc_0087ABFA;
loc_0087ADCA:
    result = ZwClose(v_stack_p70, 256, v_stack_m118, v_stack_m128);
    goto loc_0087AB1B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087A71C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
