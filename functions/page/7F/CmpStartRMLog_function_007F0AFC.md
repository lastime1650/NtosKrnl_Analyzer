# CmpStartRMLog

- RVA: `0x007F0AFC`–`0x007F1098` (길이 `1,436` bytes)
- VA: `0x00000001407F0AFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D71A8`
- 디코드: `361`개 명령, `1,436/1,436` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x007F0B5D` → [LockRMLog](../84/LockRMLog_function_00842B88.md) (function, `0x00842B88`)
- `0x007F0B77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007F0B94` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x007F0B99` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007F0BFA` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x007F0C1F` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (function, `0x004F79EC`)
- `0x007F0C44` → [CmpQueryNameString](../9B/CmpQueryNameString_function_009BA2AC.md) (function, `0x009BA2AC`)
- `0x007F0C87` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x007F0CA9` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (function, `0x004F79EC`)
- `0x007F0CBA` → [CmpIsFileInSystemConfig](CmpIsFileInSystemConfig_function_007F1F80.md) (function, `0x007F1F80`)
- `0x007F0CD6` → [CmpQueryFileSecurityDescriptor](../87/CmpQueryFileSecurityDescriptor_function_0087B318.md) (function, `0x0087B318`)
- `0x007F0D23` → [CmpStartCLFSLog](CmpStartCLFSLog_function_007F7228.md) (function, `0x007F7228`)
- `0x007F0D47` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007F0D5F` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation`)
- `0x007F0D70` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007F0D87` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation`)
- `0x007F0DBE` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadRestartArea` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadRestartArea`)
- `0x007F0DF1` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnEqual` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnEqual`)
- `0x007F0E66` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadLogRecord` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadLogRecord`)
- `0x007F0EAA` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadNextLogRecord` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadNextLogRecord`)
- `0x007F0ED9` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog`)
- `0x007F0EF9` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog`)
- `0x007F0F12` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnEqual` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnEqual`)
- `0x007F0F33` → [CmpRmAnalysisPhase](CmpRmAnalysisPhase_function_007F0568.md) (function, `0x007F0568`)
- `0x007F0F42` → [CmpRmReDoPhase](CmpRmReDoPhase_function_007F0794.md) (function, `0x007F0794`)
- `0x007F0F4A` → [CmpRmUnDoPhase](CmpRmUnDoPhase_function_007F0968.md) (function, `0x007F0968`)
- `0x007F0F7C` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsWriteRestartArea` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsWriteRestartArea`)
- `0x007F0FAA` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog`)
- `0x007F0FBE` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteLogByPointer` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteLogByPointer`)
- `0x007F0FCD` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteMarshallingArea` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteMarshallingArea`)
- `0x007F0FE0` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject`)
- `0x007F100C` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog`)
- `0x007F1039` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x007F103E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007F104D` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007F105C` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007F1066` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007F1075` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) at `0x0087D121`
- [sub_00B15E66](../B1/Unknown_function_00B15E66.md) at `0x00B15E92`
- [sub_00B15E66](../B1/Unknown_function_00B15E66.md) at `0x00B15EC4`

### Static image references
- `0x007F0BA9` → RVA `0x00EEFC78` (`.data`; read)
- `0x007F0BB0` → RVA `0x000108B8` (`.rdata`; read)
- `0x007F0BBD` → RVA `0x000013C8` (`.rdata`; read)
- `0x007F0BCD` → RVA `0x00E09AE0` (`.data`; read)
- `0x007F0D5F` → RVA `0x00151240` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsGetLogFileInformation (IAT)`; read)
- `0x007F0DBE` → RVA `0x00151238` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadRestartArea (IAT)`; read)
- `0x007F0DF1` → RVA `0x001511F8` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsLsnEqual (IAT)`; read)
- `0x007F0E66` → RVA `0x00151270` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadLogRecord (IAT)`; read)
- `0x007F0EAA` → RVA `0x001511D0` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReadNextLogRecord (IAT)`; read)
- `0x007F0ED9` → RVA `0x001511D8` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsTerminateReadLog (IAT)`; read)
- `0x007F0F7C` → RVA `0x001511E0` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsWriteRestartArea (IAT)`; read)
- `0x007F0FBE` → RVA `0x001511E8` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteLogByPointer (IAT)`; read)
- `0x007F0FCD` → RVA `0x001511F0` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsDeleteMarshallingArea (IAT)`; read)
- `0x007F0FE0` → RVA `0x00151250` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x007F0B77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007F0B94` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x007F0B99` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007F0C1F` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (`PAGE` → `.text`)
  - `0x007F0CA9` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (`PAGE` → `.text`)
  - `0x007F0D47` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007F0D70` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007F1039` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x007F103E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007F1066` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007F1075` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F0AFC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
007F0B01  55                              push rbp
007F0B02  56                              push rsi
007F0B03  57                              push rdi
007F0B04  41 54                           push r12
007F0B06  41 55                           push r13
007F0B08  41 56                           push r14
007F0B0A  41 57                           push r15
007F0B0C  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
007F0B11  48 81 EC F0 00 00 00            sub rsp, 0xf0
007F0B18  33 FF                           xor edi, edi
007F0B1A  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
007F0B1E  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
007F0B22  44 8B FF                        mov r15d, edi
007F0B25  48 89 7D B7                     mov qword ptr [rbp - 0x49], rdi
007F0B29  4C 8B F2                        mov r14, rdx
007F0B2C  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
007F0B30  48 8B F1                        mov rsi, rcx
007F0B33  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
007F0B37  48 89 7D E7                     mov qword ptr [rbp - 0x19], rdi
007F0B3B  89 7D CF                        mov dword ptr [rbp - 0x31], edi
007F0B3E  48 89 7D EF                     mov qword ptr [rbp - 0x11], rdi
007F0B42  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
007F0B46  48 89 7D 87                     mov qword ptr [rbp - 0x79], rdi
007F0B4A  89 7D 8F                        mov dword ptr [rbp - 0x71], edi
007F0B4D  48 89 7D 17                     mov qword ptr [rbp + 0x17], rdi
007F0B51  48 89 7D 9F                     mov qword ptr [rbp - 0x61], rdi
007F0B55  40 88 7D 67                     mov byte ptr [rbp + 0x67], dil
007F0B59  40 88 7D 77                     mov byte ptr [rbp + 0x77], dil
007F0B5D  E8 26 20 05 00                  call 0x140842b88
007F0B62  8B 46 68                        mov eax, dword ptr [rsi + 0x68]
007F0B65  A8 01                           test al, 1
007F0B67  75 24                           jne 0x1407f0b8d
007F0B69  8D 57 78                        lea edx, [rdi + 0x78]
007F0B6C  B9 00 01 00 00                  mov ecx, 0x100
007F0B71  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007F0B77  E8 74 15 39 00                  call 0x140b820f0
007F0B7C  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
007F0B80  4C 8B E0                        mov r12, rax
007F0B83  48 85 C0                        test rax, rax
007F0B86  75 1D                           jne 0x1407f0ba5
007F0B88  BF 9A 00 00 C0                  mov edi, 0xc000009a
007F0B8D  48 8B 8E 80 00 00 00            mov rcx, qword ptr [rsi + 0x80]
007F0B94  E8 77 EE A6 FF                  call 0x14025fa10
007F0B99  E8 12 CD A6 FF                  call 0x14025d8b0
007F0B9E  8B C7                           mov eax, edi
007F0BA0  E9 D7 04 00 00                  jmp 0x1407f107c
007F0BA5  83 4E 68 02                     or dword ptr [rsi + 0x68], 2
007F0BA9  48 3B 35 C8 F0 6F 00            cmp rsi, qword ptr [rip + 0x6ff0c8]
007F0BB0  48 8B 05 01 FD 81 FF            mov rax, qword ptr [rip - 0x7e02ff]
007F0BB7  48 89 46 78                     mov qword ptr [rsi + 0x78], rax
007F0BBB  75 78                           jne 0x1407f0c35
007F0BBD  4C 8D 2D 04 08 81 FF            lea r13, [rip - 0x7ef7fc]
007F0BC4  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
007F0BC8  4D 85 F6                        test r14, r14
007F0BCB  74 17                           je 0x1407f0be4
007F0BCD  48 8B 05 0C 8F 61 00            mov rax, qword ptr [rip + 0x618f0c]
007F0BD4  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
007F0BD8  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
007F0BDC  F3 0F 7F 81 80 00 00 00         movdqu xmmword ptr [rcx + 0x80], xmm0
007F0BE4  48 8B 05 F5 8E 61 00            mov rax, qword ptr [rip + 0x618ef5]
007F0BEB  48 8D 55 BF                     lea rdx, [rbp - 0x41]
007F0BEF  41 B0 01                        mov r8b, 1
007F0BF2  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
007F0BF6  48 83 E9 80                     sub rcx, -0x80
007F0BFA  E8 51 48 12 00                  call 0x140915450
007F0BFF  8B D8                           mov ebx, eax
007F0C01  85 C0                           test eax, eax
007F0C03  0F 88 29 04 00 00               js 0x1407f1032
007F0C09  48 C7 46 48 00 00 50 00         mov qword ptr [rsi + 0x48], 0x500000
007F0C11  48 8B 05 C8 8E 61 00            mov rax, qword ptr [rip + 0x618ec8]
007F0C18  4C 8B B0 08 06 00 00            mov r14, qword ptr [rax + 0x608]
007F0C1F  E8 C8 6D D0 FF                  call 0x1404f79ec
007F0C24  85 C0                           test eax, eax
007F0C26  0F 84 A3 00 00 00               je 0x1407f0ccf
007F0C2C  C6 45 67 01                     mov byte ptr [rbp + 0x67], 1
007F0C30  E9 9A 00 00 00                  jmp 0x1407f0ccf
007F0C35  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
007F0C39  48 8D 55 AF                     lea rdx, [rbp - 0x51]
007F0C3D  48 8B 89 08 06 00 00            mov rcx, qword ptr [rcx + 0x608]
007F0C44  E8 63 96 1C 00                  call 0x1409ba2ac
007F0C49  8B D8                           mov ebx, eax
007F0C4B  85 C0                           test eax, eax
007F0C4D  0F 88 DF 03 00 00               js 0x1407f1032
007F0C53  48 8D 45 AF                     lea rax, [rbp - 0x51]
007F0C57  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
007F0C5B  4D 85 F6                        test r14, r14
007F0C5E  74 14                           je 0x1407f0c74
007F0C60  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
007F0C64  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
007F0C68  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
007F0C6C  F3 0F 7F 81 80 00 00 00         movdqu xmmword ptr [rcx + 0x80], xmm0
007F0C74  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
007F0C78  48 8D 55 BF                     lea rdx, [rbp - 0x41]
007F0C7C  41 B0 01                        mov r8b, 1
007F0C7F  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
007F0C83  48 83 E9 80                     sub rcx, -0x80
007F0C87  E8 C4 47 12 00                  call 0x140915450
007F0C8C  8B D8                           mov ebx, eax
007F0C8E  85 C0                           test eax, eax
007F0C90  0F 88 9C 03 00 00               js 0x1407f1032
007F0C96  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
007F0C9A  48 C7 46 48 00 00 10 00         mov qword ptr [rsi + 0x48], 0x100000
007F0CA2  4C 8B B0 08 06 00 00            mov r14, qword ptr [rax + 0x608]
007F0CA9  E8 3E 6D D0 FF                  call 0x1404f79ec
007F0CAE  85 C0                           test eax, eax
007F0CB0  74 1D                           je 0x1407f0ccf
007F0CB2  48 8D 55 77                     lea rdx, [rbp + 0x77]
007F0CB6  48 8D 4D AF                     lea rcx, [rbp - 0x51]
007F0CBA  E8 C1 12 00 00                  call 0x1407f1f80
007F0CBF  8B D8                           mov ebx, eax
007F0CC1  85 C0                           test eax, eax
007F0CC3  0F 88 69 03 00 00               js 0x1407f1032
007F0CC9  8A 45 77                        mov al, byte ptr [rbp + 0x77]
007F0CCC  88 45 67                        mov byte ptr [rbp + 0x67], al
007F0CCF  48 8D 55 9F                     lea rdx, [rbp - 0x61]
007F0CD3  49 8B CE                        mov rcx, r14
007F0CD6  E8 3D A6 08 00                  call 0x14087b318
007F0CDB  8B D8                           mov ebx, eax
007F0CDD  85 C0                           test eax, eax
007F0CDF  0F 88 4D 03 00 00               js 0x1407f1032
007F0CE5  4C 8B 7D 9F                     mov r15, qword ptr [rbp - 0x61]
007F0CE9  4C 8D 76 60                     lea r14, [rsi + 0x60]
007F0CED  4C 8D 6E 58                     lea r13, [rsi + 0x58]
007F0CF1  48 8D 4E 44                     lea rcx, [rsi + 0x44]
007F0CF5  40 38 7D 67                     cmp byte ptr [rbp + 0x67], dil
007F0CF9  48 8D 55 BF                     lea rdx, [rbp - 0x41]
007F0CFD  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007F0D02  4D 8B CF                        mov r9, r15
007F0D05  0F 94 C0                        sete al
007F0D08  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
007F0D0D  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
007F0D12  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
007F0D16  88 44 24 30                     mov byte ptr [rsp + 0x30], al
007F0D1A  48 8D 46 48                     lea rax, [rsi + 0x48]
007F0D1E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F0D23  E8 00 65 00 00                  call 0x1407f7228
007F0D28  8B D8                           mov ebx, eax
007F0D2A  85 C0                           test eax, eax
007F0D2C  0F 88 D1 02 00 00               js 0x1407f1003
007F0D32  B8 78 00 00 00                  mov eax, 0x78
007F0D37  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007F0D3D  8B D0                           mov edx, eax
007F0D3F  89 45 77                        mov dword ptr [rbp + 0x77], eax
007F0D42  B9 00 01 00 00                  mov ecx, 0x100
007F0D47  E8 A4 13 39 00                  call 0x140b820f0
007F0D4C  48 8B D8                        mov rbx, rax
007F0D4F  48 85 C0                        test rax, rax
007F0D52  74 21                           je 0x1407f0d75
007F0D54  49 8B 4D 00                     mov rcx, qword ptr [r13]
007F0D58  4C 8D 45 77                     lea r8, [rbp + 0x77]
007F0D5C  48 8B D0                        mov rdx, rax
007F0D5F  48 FF 15 DA 04 96 FF            call qword ptr [rip - 0x69fb26]
007F0D66  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0D6B  33 D2                           xor edx, edx
007F0D6D  48 8B CB                        mov rcx, rbx
007F0D70  E8 FB 1A 39 00                  call 0x140b82870
007F0D75  49 8B 4D 00                     mov rcx, qword ptr [r13]
007F0D79  4C 8D 45 8F                     lea r8, [rbp - 0x71]
007F0D7D  49 8B D4                        mov rdx, r12
007F0D80  C7 45 8F 78 00 00 00            mov dword ptr [rbp - 0x71], 0x78
007F0D87  48 FF 15 B2 04 96 FF            call qword ptr [rip - 0x69fb4e]
007F0D8E  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0D93  8B D8                           mov ebx, eax
007F0D95  49 8B 44 24 48                  mov rax, qword ptr [r12 + 0x48]
007F0D9A  48 89 46 78                     mov qword ptr [rsi + 0x78], rax
007F0D9E  85 DB                           test ebx, ebx
007F0DA0  0F 88 5D 02 00 00               js 0x1407f1003
007F0DA6  49 8B 0E                        mov rcx, qword ptr [r14]
007F0DA9  48 8D 45 97                     lea rax, [rbp - 0x69]
007F0DAD  4C 8D 4D EF                     lea r9, [rbp - 0x11]
007F0DB1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007F0DB6  4C 8D 45 CF                     lea r8, [rbp - 0x31]
007F0DBA  48 8D 55 E7                     lea rdx, [rbp - 0x19]
007F0DBE  48 FF 15 73 04 96 FF            call qword ptr [rip - 0x69fb8d]
007F0DC5  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0DCA  3D 0C 00 1A 40                  cmp eax, 0x401a000c
007F0DCF  0F 84 12 01 00 00               je 0x1407f0ee7
007F0DD5  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
007F0DD9  48 85 C0                        test rax, rax
007F0DDC  0F 84 05 01 00 00               je 0x1407f0ee7
007F0DE2  48 8B 00                        mov rax, qword ptr [rax]
007F0DE5  48 8D 55 87                     lea rdx, [rbp - 0x79]
007F0DE9  48 8D 4D EF                     lea rcx, [rbp - 0x11]
007F0DED  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
007F0DF1  48 FF 15 00 04 96 FF            call qword ptr [rip - 0x69fc00]
007F0DF8  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0DFD  84 C0                           test al, al
007F0DFF  0F 84 EB 00 00 00               je 0x1407f0ef0
007F0E05  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
007F0E09  4C 8D 4D 07                     lea r9, [rbp + 7]
007F0E0D  49 8B 0E                        mov rcx, qword ptr [r14]
007F0E10  48 8D 55 1F                     lea rdx, [rbp + 0x1f]
007F0E14  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
007F0E18  41 B8 03 00 00 00               mov r8d, 3
007F0E1E  48 8D 45 9F                     lea rax, [rbp - 0x61]
007F0E22  48 89 7D 9F                     mov qword ptr [rbp - 0x61], rdi
007F0E26  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007F0E2B  48 8D 45 F7                     lea rax, [rbp - 9]
007F0E2F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007F0E34  48 8D 45 FF                     lea rax, [rbp - 1]
007F0E38  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007F0E3D  48 8D 45 77                     lea rax, [rbp + 0x77]
007F0E41  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F0E46  48 8D 45 A7                     lea rax, [rbp - 0x59]
007F0E4A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007F0E4F  48 89 7D 07                     mov qword ptr [rbp + 7], rdi
007F0E53  89 7D A7                        mov dword ptr [rbp - 0x59], edi
007F0E56  48 89 7D FF                     mov qword ptr [rbp - 1], rdi
007F0E5A  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
007F0E5E  48 89 7D 0F                     mov qword ptr [rbp + 0xf], rdi
007F0E62  40 88 7D 77                     mov byte ptr [rbp + 0x77], dil
007F0E66  48 FF 15 03 04 96 FF            call qword ptr [rip - 0x69fbfd]
007F0E6D  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0E72  85 C0                           test eax, eax
007F0E74  78 5A                           js 0x1407f0ed0
007F0E76  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
007F0E7A  48 8D 45 0F                     lea rax, [rbp + 0xf]
007F0E7E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007F0E83  4C 8D 4D 77                     lea r9, [rbp + 0x77]
007F0E87  48 8D 45 F7                     lea rax, [rbp - 9]
007F0E8B  C6 45 77 01                     mov byte ptr [rbp + 0x77], 1
007F0E8F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007F0E94  4C 8D 45 A7                     lea r8, [rbp - 0x59]
007F0E98  48 8D 45 FF                     lea rax, [rbp - 1]
007F0E9C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F0EA1  48 8D 55 07                     lea rdx, [rbp + 7]
007F0EA5  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007F0EAA  48 FF 15 1F 03 96 FF            call qword ptr [rip - 0x69fce1]
007F0EB1  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0EB6  3D 11 00 00 C0                  cmp eax, 0xc0000011
007F0EBB  75 07                           jne 0x1407f0ec4
007F0EBD  49 8B 44 24 58                  mov rax, qword ptr [r12 + 0x58]
007F0EC2  EB 08                           jmp 0x1407f0ecc
007F0EC4  85 C0                           test eax, eax
007F0EC6  78 08                           js 0x1407f0ed0
007F0EC8  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
007F0ECC  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
007F0ED0  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
007F0ED4  48 85 C9                        test rcx, rcx
007F0ED7  74 17                           je 0x1407f0ef0
007F0ED9  48 FF 15 F8 02 96 FF            call qword ptr [rip - 0x69fd08]
007F0EE0  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0EE5  EB 09                           jmp 0x1407f0ef0
007F0EE7  49 8B 44 24 48                  mov rax, qword ptr [r12 + 0x48]
007F0EEC  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
007F0EF0  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
007F0EF4  48 85 C9                        test rcx, rcx
007F0EF7  74 10                           je 0x1407f0f09
007F0EF9  48 FF 15 D8 02 96 FF            call qword ptr [rip - 0x69fd28]
007F0F00  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0F05  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
007F0F09  49 8D 54 24 58                  lea rdx, [r12 + 0x58]
007F0F0E  48 8D 4D 87                     lea rcx, [rbp - 0x79]
007F0F12  48 FF 15 DF 02 96 FF            call qword ptr [rip - 0x69fd21]
007F0F19  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0F1E  84 C0                           test al, al
007F0F20  75 31                           jne 0x1407f0f53
007F0F22  8B 46 68                        mov eax, dword ptr [rsi + 0x68]
007F0F25  A8 04                           test al, 4
007F0F27  74 2A                           je 0x1407f0f53
007F0F29  48 8B 5D 87                     mov rbx, qword ptr [rbp - 0x79]
007F0F2D  48 8B CE                        mov rcx, rsi
007F0F30  48 8B D3                        mov rdx, rbx
007F0F33  E8 30 F6 FF FF                  call 0x1407f0568
007F0F38  85 C0                           test eax, eax
007F0F3A  78 13                           js 0x1407f0f4f
007F0F3C  48 8B D3                        mov rdx, rbx
007F0F3F  48 8B CE                        mov rcx, rsi
007F0F42  E8 4D F8 FF FF                  call 0x1407f0794
007F0F47  48 8B CE                        mov rcx, rsi
007F0F4A  E8 19 FA FF FF                  call 0x1407f0968
007F0F4F  83 66 68 FB                     and dword ptr [rsi + 0x68], 0xfffffffb
007F0F53  49 8B 44 24 58                  mov rax, qword ptr [r12 + 0x58]
007F0F58  48 8D 55 17                     lea rdx, [rbp + 0x17]
007F0F5C  49 8B 0E                        mov rcx, qword ptr [r14]
007F0F5F  45 33 C9                        xor r9d, r9d
007F0F62  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007F0F66  48 8D 45 8F                     lea rax, [rbp - 0x71]
007F0F6A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
007F0F6F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F0F74  45 8D 41 08                     lea r8d, [r9 + 8]
007F0F78  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
007F0F7C  48 FF 15 5D 02 96 FF            call qword ptr [rip - 0x69fda3]
007F0F83  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0F88  8B D8                           mov ebx, eax
007F0F8A  40 38 7D 7F                     cmp byte ptr [rbp + 0x7f], dil
007F0F8E  74 6F                           je 0x1407f0fff
007F0F90  3D 1D 00 1A C0                  cmp eax, 0xc01a001d
007F0F95  74 06                           je 0x1407f0f9d
007F0F97  83 7E 44 0A                     cmp dword ptr [rsi + 0x44], 0xa
007F0F9B  76 62                           jbe 0x1407f0fff
007F0F9D  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
007F0FA1  40 88 7D 7F                     mov byte ptr [rbp + 0x7f], dil
007F0FA5  48 85 C9                        test rcx, rcx
007F0FA8  74 10                           je 0x1407f0fba
007F0FAA  48 FF 15 27 02 96 FF            call qword ptr [rip - 0x69fdd9]
007F0FB1  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0FB6  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
007F0FBA  49 8B 4D 00                     mov rcx, qword ptr [r13]
007F0FBE  48 FF 15 23 02 96 FF            call qword ptr [rip - 0x69fddd]
007F0FC5  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0FCA  49 8B 0E                        mov rcx, qword ptr [r14]
007F0FCD  48 FF 15 1C 02 96 FF            call qword ptr [rip - 0x69fde4]
007F0FD4  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0FD9  49 8B 4D 00                     mov rcx, qword ptr [r13]
007F0FDD  49 89 3E                        mov qword ptr [r14], rdi
007F0FE0  48 FF 15 69 02 96 FF            call qword ptr [rip - 0x69fd97]
007F0FE7  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F0FEC  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
007F0FF0  48 8D 4E 44                     lea rcx, [rsi + 0x44]
007F0FF4  89 39                           mov dword ptr [rcx], edi
007F0FF6  49 89 7D 00                     mov qword ptr [r13], rdi
007F0FFA  E9 F6 FC FF FF                  jmp 0x1407f0cf5
007F0FFF  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
007F1003  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
007F1007  48 85 C9                        test rcx, rcx
007F100A  74 0C                           je 0x1407f1018
007F100C  48 FF 15 C5 01 96 FF            call qword ptr [rip - 0x69fe3b]
007F1013  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007F1018  85 DB                           test ebx, ebx
007F101A  79 0A                           jns 0x1407f1026
007F101C  49 39 3E                        cmp qword ptr [r14], rdi
007F101F  74 11                           je 0x1407f1032
007F1021  49 89 3E                        mov qword ptr [r14], rdi
007F1024  EB 0C                           jmp 0x1407f1032
007F1026  8B 46 68                        mov eax, dword ptr [rsi + 0x68]
007F1029  83 E0 FD                        and eax, 0xfffffffd
007F102C  83 C8 01                        or eax, 1
007F102F  89 46 68                        mov dword ptr [rsi + 0x68], eax
007F1032  48 8B 8E 80 00 00 00            mov rcx, qword ptr [rsi + 0x80]
007F1039  E8 D2 E9 A6 FF                  call 0x14025fa10
007F103E  E8 6D C8 A6 FF                  call 0x14025d8b0
007F1043  48 39 7D B7                     cmp qword ptr [rbp - 0x49], rdi
007F1047  74 09                           je 0x1407f1052
007F1049  48 8D 4D AF                     lea rcx, [rbp - 0x51]
007F104D  E8 AE F7 1C 00                  call 0x1409c0800
007F1052  48 39 7D C7                     cmp qword ptr [rbp - 0x39], rdi
007F1056  74 09                           je 0x1407f1061
007F1058  48 8D 4D BF                     lea rcx, [rbp - 0x41]
007F105C  E8 9F F7 1C 00                  call 0x1409c0800
007F1061  33 D2                           xor edx, edx
007F1063  49 8B CC                        mov rcx, r12
007F1066  E8 05 18 39 00                  call 0x140b82870
007F106B  4D 85 FF                        test r15, r15
007F106E  74 0A                           je 0x1407f107a
007F1070  33 D2                           xor edx, edx
007F1072  49 8B CF                        mov rcx, r15
007F1075  E8 F6 17 39 00                  call 0x140b82870
007F107A  8B C3                           mov eax, ebx
007F107C  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
007F1084  48 81 C4 F0 00 00 00            add rsp, 0xf0
007F108B  41 5F                           pop r15
007F108D  41 5E                           pop r14
007F108F  41 5D                           pop r13
007F1091  41 5C                           pop r12
007F1093  5F                              pop rdi
007F1094  5E                              pop rsi
007F1095  5D                              pop rbp
007F1096  C3                              ret
007F1097  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpStartRMLog(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (240);
    v_rdi = 0;
    v_stack_p20 = 1;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    v_stack_m70 = 0;
    v_stack_mC8 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = 0;
    v_stack_m48 = 0;
    v_stack_mC0 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    result = LockRMLog(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 104)))) & (1)) != 0) goto loc_007F0B8D;
    result = ExAllocatePool2(256, v_rdi + 120, (unsigned int)(0x20204D43ULL), a4);
    v_stack_m88 = result;
    if (result != 0) goto loc_007F0BA5;
loc_007F0B8D:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 128), v_rdi + 120, (unsigned int)(0x20204D43ULL), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 128), v_rdi + 120, (unsigned int)(0x20204D43ULL), a4);
    goto loc_007F107C;
loc_007F0BA5:
    *(unsigned __int64 *)(a1 + 120) = *(unsigned __int64 *)(v_rip - 8258303);
    if (a1 != (*(unsigned __int64 *)(v_rip + 7336136))) goto loc_007F0C35;
    v_stack_m80 = v_rip - 8321020;
    result = *(unsigned __int64 *)(v_rip - 8258303);
    if (a2 != 0) {
        result = *(unsigned __int64 *)(v_rip + 6393612);
        a1 = *(unsigned __int64 *)(result + 64);
        *(unsigned __int64 *)(a1 + 128) = v_xmm0;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6393589) + 64)) - (-128);
    result = RtlStringFromGUIDEx(a1, v_stack_mA0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    *(unsigned __int64 *)(a1 + 72) = 0x500000ULL;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(a1, v_stack_mA0, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_007F0CCF;
    v_stack_p8 = 1;
    goto loc_007F0CCF;
loc_007F0C35:
    result = CmpQueryNameString(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 1544), v_stack_mB0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    v_stack_m80 = v_stack_mB0;
    result = v_stack_mB0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6393544) + 1544) != 0) {
        result = *(unsigned __int64 *)(a1 + 80);
        a1 = *(unsigned __int64 *)(result + 64);
        *(unsigned __int64 *)(a1 + 128) = v_xmm0;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 64)) - (-128);
    result = RtlStringFromGUIDEx(a1, v_stack_mA0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    *(unsigned __int64 *)(a1 + 72) = 0x100000ULL;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(a1, v_stack_mA0, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_007F0CCF;
    result = CmpIsFileInSystemConfig(v_stack_mB0, v_stack_p18, 1, a4);
    if (sign_flag) goto loc_007F1032;
    v_stack_p8 = (unsigned __int8)(v_stack_p18);
loc_007F0CCF:
    result = CmpQueryFileSecurityDescriptor(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 80) + 1544), v_stack_mC0, 1, a4);
    if (sign_flag) goto loc_007F1032;
loc_007F0CF5:
    v_stack_mE0 = a1 + 96;
    result = (v_stack_p8 == ((unsigned __int8)((unsigned int)(0xC000009AULL)))) ? 1 : 0;
    v_stack_mE8 = a1 + 88;
    v_stack_mF0 = a1 + 68;
    v_stack_mF8 = (unsigned __int8)(result);
    v_stack_m100 = a1 + 72;
    result = CmpStartCLFSLog(v_stack_m80, v_stack_mA0, 1, v_stack_mC0);
    if (sign_flag) goto loc_007F1003;
    v_stack_p18 = 120;
    result = ExAllocatePool2(256, 120, (unsigned int)(0x20204D43ULL), v_stack_mC0);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(a1 + 88);
        a3 = v_stack_p18;
        a2 = result;
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsGetLogFileInformation(a1, a2, a3, v_stack_mC0);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_mC0);
    }
    v_stack_mD0 = 120;
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsGetLogFileInformation(*(unsigned __int64 *)(a1 + 88), result, v_stack_mD0, v_stack_mC0);
    *(unsigned __int64 *)(a1 + 120) = *(unsigned __int64 *)(result + 72);
    if (sign_flag) goto loc_007F1003;
    v_stack_m108 = v_stack_mC8;
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsReadRestartArea(*(unsigned __int64 *)(a1 + 96), v_stack_m78, v_stack_m90, v_stack_m70);
    if (((unsigned int)(result)) == 0x401A000CULL) goto loc_007F0EE7;
    if (v_stack_m78 == 0) goto loc_007F0EE7;
    v_stack_mD8 = *(unsigned __int64 *)(v_stack_m78);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsLsnEqual(v_stack_m70, v_stack_mD8, v_stack_m90, v_stack_m70);
    if ((unsigned __int8)(result) == 0) goto loc_007F0EF0;
    v_stack_m40 = v_stack_mD8;
    v_stack_mC0 = (unsigned int)(0xC000009AULL);
    v_stack_mE8 = v_stack_mC0;
    v_stack_mF0 = v_stack_m68;
    v_stack_mF8 = v_stack_m60;
    v_stack_m100 = v_stack_p18;
    v_stack_m108 = v_stack_mB8;
    v_stack_m58 = (unsigned int)(0xC000009AULL);
    v_stack_mB8 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m60 = (unsigned int)(0xC000009AULL);
    v_stack_m68 = (unsigned int)(0xC000009AULL);
    v_stack_m50 = (unsigned int)(0xC000009AULL);
    v_stack_p18 = (unsigned __int8)((unsigned int)(0xC000009AULL));
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsReadLogRecord(*(unsigned __int64 *)(a1 + 96), v_stack_m40, 3, v_stack_m58);
    if (sign_flag) goto loc_007F0ED0;
    v_stack_mF0 = v_stack_m50;
    v_stack_p18 = 1;
    v_stack_mF8 = v_stack_m68;
    v_stack_m100 = v_stack_m60;
    v_stack_m108 = (unsigned int)(0xC000009AULL);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsReadNextLogRecord(v_stack_mC0, v_stack_m58, v_stack_mB8, v_stack_p18);
    if (((unsigned int)(result)) != 0xC0000011ULL) goto loc_007F0EC4;
    goto loc_007F0ECC;
loc_007F0EC4:
    if (sign_flag) goto loc_007F0ED0;
loc_007F0ECC:
    v_stack_mD8 = v_stack_m50;
loc_007F0ED0:
    if (v_stack_mC0 == 0) goto loc_007F0EF0;
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsTerminateReadLog(v_stack_mC0, v_stack_m58, v_stack_mB8, v_stack_p18);
    goto loc_007F0EF0;
loc_007F0EE7:
    v_stack_mD8 = *(unsigned __int64 *)(result + 72);
loc_007F0EF0:
    result = *(unsigned __int64 *)(result + 72);
    if (v_stack_mC8 != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsTerminateReadLog(v_stack_mC8, v_stack_m58, v_stack_mB8, v_stack_p18);
        v_stack_mC8 = (unsigned int)(0xC000009AULL);
    }
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsLsnEqual(v_stack_mD8, result + 88, v_stack_mB8, v_stack_p18);
    if ((unsigned __int8)(result) != 0) goto loc_007F0F53;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 104)))) & (4)) == 0) goto loc_007F0F53;
    result = CmpRmAnalysisPhase(a1, v_stack_mD8, v_stack_mB8, v_stack_p18);
    if (!(sign_flag)) {
        a2 = v_stack_mD8;
        a1 = a1;
        result = CmpRmReDoPhase(a1, a2, v_stack_mB8, v_stack_p18);
        a1 = a1;
        result = CmpRmUnDoPhase(a1, a2, v_stack_mB8, v_stack_p18);
    }
loc_007F0F53:
    a4 = 0;
    v_stack_m48 = *(unsigned __int64 *)(result + 88);
    v_stack_mF8 = (unsigned int)(0xC000009AULL);
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = (unsigned int)((unsigned int)(0xC000009AULL));
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsWriteRestartArea(*(unsigned __int64 *)(a1 + 96), v_stack_m48, a4 + 8, a4);
    if (v_stack_p20 == ((unsigned __int8)((unsigned int)(0xC000009AULL)))) goto loc_007F0FFF;
    if (((unsigned int)(result)) == 0xC01A001DULL) goto loc_007F0F9D;
    if ((*(unsigned int *)(a1 + 68)) <= 10) goto loc_007F0FFF;
loc_007F0F9D:
    v_stack_p20 = (unsigned __int8)((unsigned int)(0xC000009AULL));
    if (v_stack_mC8 != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsTerminateReadLog(v_stack_mC8, v_stack_m48, a4 + 8, a4);
        v_stack_mC8 = (unsigned int)(0xC000009AULL);
    }
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsDeleteLogByPointer(*(unsigned __int64 *)(a1 + 88), v_stack_m48, a4 + 8, a4);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsDeleteMarshallingArea(*(unsigned __int64 *)(a1 + 96), v_stack_m48, a4 + 8, a4);
    *(unsigned __int64 *)(a1 + 96) = (unsigned int)(0xC000009AULL);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsCloseLogFileObject(*(unsigned __int64 *)(a1 + 88), v_stack_m48, a4 + 8, a4);
    *(unsigned int *)(a1 + 68) = (unsigned int)((unsigned int)(0xC000009AULL));
    *(unsigned __int64 *)(a1 + 88) = (unsigned int)(0xC000009AULL);
    goto loc_007F0CF5;
loc_007F0FFF:
loc_007F1003:
    if (v_stack_mC8 != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsTerminateReadLog(v_stack_mC8, v_stack_m48, a4 + 8, a4);
    }
    if (!sign_flag) goto loc_007F1026;
    if ((*(unsigned __int64 *)(a1 + 96)) == ((unsigned int)(0xC000009AULL))) goto loc_007F1032;
    *(unsigned __int64 *)(a1 + 96) = (unsigned int)(0xC000009AULL);
    goto loc_007F1032;
loc_007F1026:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 104))) & (0xFFFFFFFDULL));
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 104) = (unsigned int)(result);
loc_007F1032:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 128), v_stack_m48, a4 + 8, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 128), v_stack_m48, a4 + 8, a4);
    if (v_stack_mA8 != ((unsigned int)(0xC000009AULL))) {
        a1 = v_stack_mB0;
        result = RtlFreeAnsiString(a1, v_stack_m48, a4 + 8, a4);
    }
    if (v_stack_m98 != ((unsigned int)(0xC000009AULL))) {
        a1 = v_stack_mA0;
        result = RtlFreeAnsiString(a1, v_stack_m48, a4 + 8, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, a4 + 8, a4);
    if (v_stack_mC0 != 0) {
        a2 = 0;
        a1 = v_stack_mC0;
        result = ExFreePoolWithTag(a1, a2, a4 + 8, a4);
    }
loc_007F107C:
    v_rsp = (v_rsp) + (240);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t CmpStartRMLog(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (240);
    local_rdi = 0;
    v_stack_p20 = 1;
    v_stack_mB0 = 0;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    v_stack_m70 = 0;
    v_stack_mC8 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = 0;
    v_stack_m48 = 0;
    v_stack_mC0 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    result = LockRMLog(Arg1, Arg2, a3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)))) & (1)) != 0) goto loc_007F0B8D;
    result = ExAllocatePool2(256, local_rdi + 120, (uint32_t)(0x20204D43ULL), a4);
    v_stack_m88 = result;
    if (result != 0) goto loc_007F0BA5;
loc_007F0B8D:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x80), local_rdi + 120, (uint32_t)(0x20204D43ULL), a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x80), local_rdi + 120, (uint32_t)(0x20204D43ULL), a4);
    goto loc_007F107C;
loc_007F0BA5:
    *(uint64_t *)(arg1 + 0x78) = *(uint64_t *)(v_rip - 0x7E02FF);
    if (Arg1 != (*(uint64_t *)(v_rip + 0x6FF0C8))) goto loc_007F0C35;
    v_stack_m80 = v_rip - 8321020;
    result = *(uint64_t *)(v_rip - 0x7E02FF);
    if (Arg2 != 0) {
        result = *(uint64_t *)(v_rip + 0x618F0C);
        Arg1 = *(uint64_t *)(result + 0x40);
        *(uint64_t *)(arg1 + 0x80) = v_xmm0;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x618EF5) + 0x40)) - (-128);
    result = RtlStringFromGUIDEx(Arg1, v_stack_mA0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    *(uint64_t *)(arg1 + 0x48) = 0x500000ULL;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_mA0, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_007F0CCF;
    v_stack_p8 = 1;
    goto loc_007F0CCF;
loc_007F0C35:
    result = CmpQueryNameString(*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x608), v_stack_mB0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    v_stack_m80 = v_stack_mB0;
    result = v_stack_mB0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x618EC8) + 0x608) != 0) {
        result = *(uint64_t *)(arg1 + 0x50);
        Arg1 = *(uint64_t *)(result + 0x40);
        *(uint64_t *)(arg1 + 0x80) = v_xmm0;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x40)) - (-128);
    result = RtlStringFromGUIDEx(Arg1, v_stack_mA0, 1, a4);
    if (sign_flag) goto loc_007F1032;
    *(uint64_t *)(arg1 + 0x48) = 0x100000ULL;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_mA0, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_007F0CCF;
    result = CmpIsFileInSystemConfig(v_stack_mB0, v_stack_p18, 1, a4);
    if (sign_flag) goto loc_007F1032;
    v_stack_p8 = (uint8_t)(v_stack_p18);
loc_007F0CCF:
    result = CmpQueryFileSecurityDescriptor(*(uint64_t *)(*(uint64_t *)(arg1 + 0x50) + 0x608), v_stack_mC0, 1, a4);
    if (sign_flag) goto loc_007F1032;
loc_007F0CF5:
    v_stack_mE0 = Arg1 + 96;
    result = (v_stack_p8 == ((uint8_t)((uint32_t)(0xC000009AULL)))) ? 1 : 0;
    v_stack_mE8 = Arg1 + 88;
    v_stack_mF0 = Arg1 + 68;
    v_stack_mF8 = (uint8_t)(result);
    v_stack_m100 = Arg1 + 72;
    result = CmpStartCLFSLog(v_stack_m80, v_stack_mA0, 1, v_stack_mC0);
    if (sign_flag) goto loc_007F1003;
    v_stack_p18 = 120;
    result = ExAllocatePool2(256, 120, (uint32_t)(0x20204D43ULL), v_stack_mC0);
    if (result != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x58);
        a3 = v_stack_p18;
        Arg2 = result;
        result = kernel_indirect_call(Arg1, Arg2, a3, v_stack_mC0);
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, v_stack_mC0);
    }
    v_stack_mD0 = 120;
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x58), result, v_stack_mD0, v_stack_mC0);
    *(uint64_t *)(arg1 + 0x78) = *(uint64_t *)(result + 0x48);
    if (sign_flag) goto loc_007F1003;
    v_stack_m108 = v_stack_mC8;
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x60), v_stack_m78, v_stack_m90, v_stack_m70);
    if (((uint32_t)(result)) == 0x401A000CULL) goto loc_007F0EE7;
    if (v_stack_m78 == 0) goto loc_007F0EE7;
    v_stack_mD8 = *(uint64_t *)(v_stack_m78);
    result = kernel_indirect_call(v_stack_m70, v_stack_mD8, v_stack_m90, v_stack_m70);
    if ((uint8_t)(result) == 0) goto loc_007F0EF0;
    v_stack_m40 = v_stack_mD8;
    v_stack_mC0 = (uint32_t)(0xC000009AULL);
    v_stack_mE8 = v_stack_mC0;
    v_stack_mF0 = v_stack_m68;
    v_stack_mF8 = v_stack_m60;
    v_stack_m100 = v_stack_p18;
    v_stack_m108 = v_stack_mB8;
    v_stack_m58 = (uint32_t)(0xC000009AULL);
    v_stack_mB8 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m60 = (uint32_t)(0xC000009AULL);
    v_stack_m68 = (uint32_t)(0xC000009AULL);
    v_stack_m50 = (uint32_t)(0xC000009AULL);
    v_stack_p18 = (uint8_t)((uint32_t)(0xC000009AULL));
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x60), v_stack_m40, 3, v_stack_m58);
    if (sign_flag) goto loc_007F0ED0;
    v_stack_mF0 = v_stack_m50;
    v_stack_p18 = 1;
    v_stack_mF8 = v_stack_m68;
    v_stack_m100 = v_stack_m60;
    v_stack_m108 = (uint32_t)(0xC000009AULL);
    result = kernel_indirect_call(v_stack_mC0, v_stack_m58, v_stack_mB8, v_stack_p18);
    if (((uint32_t)(result)) != 0xC0000011ULL) goto loc_007F0EC4;
    goto loc_007F0ECC;
loc_007F0EC4:
    if (sign_flag) goto loc_007F0ED0;
loc_007F0ECC:
    v_stack_mD8 = v_stack_m50;
loc_007F0ED0:
    if (v_stack_mC0 == 0) goto loc_007F0EF0;
    result = kernel_indirect_call(v_stack_mC0, v_stack_m58, v_stack_mB8, v_stack_p18);
    goto loc_007F0EF0;
loc_007F0EE7:
    v_stack_mD8 = *(uint64_t *)(result + 0x48);
loc_007F0EF0:
    result = *(uint64_t *)(result + 0x48);
    if (v_stack_mC8 != 0) {
        result = kernel_indirect_call(v_stack_mC8, v_stack_m58, v_stack_mB8, v_stack_p18);
        v_stack_mC8 = (uint32_t)(0xC000009AULL);
    }
    result = kernel_indirect_call(v_stack_mD8, result + 88, v_stack_mB8, v_stack_p18);
    if ((uint8_t)(result) != 0) goto loc_007F0F53;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x68)))) & (4)) == 0) goto loc_007F0F53;
    result = CmpRmAnalysisPhase(Arg1, v_stack_mD8, v_stack_mB8, v_stack_p18);
    if (!(sign_flag)) {
        Arg2 = v_stack_mD8;
        Arg1 = Arg1;
        result = CmpRmReDoPhase(Arg1, Arg2, v_stack_mB8, v_stack_p18);
        Arg1 = Arg1;
        result = CmpRmUnDoPhase(Arg1, Arg2, v_stack_mB8, v_stack_p18);
    }
loc_007F0F53:
    a4 = 0;
    v_stack_m48 = *(uint64_t *)(result + 0x58);
    v_stack_mF8 = (uint32_t)(0xC000009AULL);
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = (uint32_t)((uint32_t)(0xC000009AULL));
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x60), v_stack_m48, a4 + 8, a4);
    if (v_stack_p20 == ((uint8_t)((uint32_t)(0xC000009AULL)))) goto loc_007F0FFF;
    if (((uint32_t)(result)) == 0xC01A001DULL) goto loc_007F0F9D;
    if ((*(uint32_t *)(arg1 + 0x44)) <= 10) goto loc_007F0FFF;
loc_007F0F9D:
    v_stack_p20 = (uint8_t)((uint32_t)(0xC000009AULL));
    if (v_stack_mC8 != 0) {
        result = kernel_indirect_call(v_stack_mC8, v_stack_m48, a4 + 8, a4);
        v_stack_mC8 = (uint32_t)(0xC000009AULL);
    }
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x58), v_stack_m48, a4 + 8, a4);
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x60), v_stack_m48, a4 + 8, a4);
    *(uint64_t *)(arg1 + 0x60) = (uint32_t)(0xC000009AULL);
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x58), v_stack_m48, a4 + 8, a4);
    *(uint32_t *)(arg1 + 0x44) = (uint32_t)((uint32_t)(0xC000009AULL));
    *(uint64_t *)(arg1 + 0x58) = (uint32_t)(0xC000009AULL);
    goto loc_007F0CF5;
loc_007F0FFF:
loc_007F1003:
    if (v_stack_mC8 != 0) {
        result = kernel_indirect_call(v_stack_mC8, v_stack_m48, a4 + 8, a4);
    }
    if (!sign_flag) goto loc_007F1026;
    if ((*(uint64_t *)(arg1 + 0x60)) == ((uint32_t)(0xC000009AULL))) goto loc_007F1032;
    *(uint64_t *)(arg1 + 0x60) = (uint32_t)(0xC000009AULL);
    goto loc_007F1032;
loc_007F1026:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x68))) & (0xFFFFFFFDULL));
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x68) = (uint32_t)(result);
loc_007F1032:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x80), v_stack_m48, a4 + 8, a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x80), v_stack_m48, a4 + 8, a4);
    if (v_stack_mA8 != ((uint32_t)(0xC000009AULL))) {
        Arg1 = v_stack_mB0;
        result = RtlFreeAnsiString(Arg1, v_stack_m48, a4 + 8, a4);
    }
    if (v_stack_m98 != ((uint32_t)(0xC000009AULL))) {
        Arg1 = v_stack_mA0;
        result = RtlFreeAnsiString(Arg1, v_stack_m48, a4 + 8, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, Arg2, a4 + 8, a4);
    if (v_stack_mC0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mC0;
        result = ExFreePoolWithTag(Arg1, Arg2, a4 + 8, a4);
    }
loc_007F107C:
    local_rsp = (local_rsp) + (240);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F0AFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
