# NtLoadEnclaveData

- RVA: `0x00AF8DF0`–`0x00AF93D1` (길이 `1,505` bytes)
- VA: `0x0000000140AF8DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8908`
- 디코드: `321`개 명령, `1,505/1,505` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AF8F78` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00AF8FC3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF90A4` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AF90C7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00AF90E3` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x00AF9137` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x00AF9176` → [MiLoadSectionIntoVsmEnclave](../AB/MiLoadSectionIntoVsmEnclave_function_00AB1D4C.md) (function, `0x00AB1D4C`)
- `0x00AF9184` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF91E7` → [MiLoadDataIntoVsmEnclave](../AC/MiLoadDataIntoVsmEnclave_function_00ACD114.md) (function, `0x00ACD114`)
- `0x00AF921D` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AF9279` → [MiCopyPagesIntoEnclave](../A4/MiCopyPagesIntoEnclave_function_00A472AC.md) (function, `0x00A472AC`)
- `0x00AF92A4` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00AF92BD` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AF92C2` → [Feature_4234569016__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_4234569016__private_IsEnabledDeviceUsageNoInline_function_00686CC4.md) (function, `0x00686CC4`)
- `0x00AF92E6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF9302` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF9330` → [DbgkMapViewOfSection](../89/DbgkMapViewOfSection_function_00897460.md) (function, `0x00897460`)
- `0x00AF9338` → [MiDereferenceEnclaveModule](../80/MiDereferenceEnclaveModule_function_008089B4.md) (function, `0x008089B4`)
- `0x00AF935C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AF9378` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF93B9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AF8E02` → RVA `0x00E0A740` (`.data`; read)
- `0x00AF9095` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00AF8F78` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00AF8FC3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF90C7` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00AF90E3` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x00AF9137` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x00AF9184` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF921D` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AF92A4` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00AF92BD` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AF92C2` → [Feature_4234569016__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_4234569016__private_IsEnabledDeviceUsageNoInline_function_00686CC4.md) (`PAGE` → `.text`)
  - `0x00AF92E6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF9302` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF935C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AF9378` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF93B9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF8DF0  40 53                           push rbx
00AF8DF2  56                              push rsi
00AF8DF3  41 54                           push r12
00AF8DF5  41 55                           push r13
00AF8DF7  41 56                           push r14
00AF8DF9  41 57                           push r15
00AF8DFB  48 81 EC 58 01 00 00            sub rsp, 0x158
00AF8E02  48 8B 05 37 19 31 00            mov rax, qword ptr [rip + 0x311937]
00AF8E09  48 33 C4                        xor rax, rsp
00AF8E0C  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00AF8E14  4D 8B D9                        mov r11, r9
00AF8E17  4C 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r9
00AF8E1F  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
00AF8E27  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00AF8E2F  4C 8B D1                        mov r10, rcx
00AF8E32  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00AF8E37  4C 8B 84 24 C8 01 00 00         mov r8, qword ptr [rsp + 0x1c8]
00AF8E3F  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
00AF8E44  4C 8B A4 24 D0 01 00 00         mov r12, qword ptr [rsp + 0x1d0]
00AF8E4C  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
00AF8E54  48 8B 94 24 B8 01 00 00         mov rdx, qword ptr [rsp + 0x1b8]
00AF8E5C  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
00AF8E64  44 8B AC 24 C0 01 00 00         mov r13d, dword ptr [rsp + 0x1c0]
00AF8E6C  4C 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r8
00AF8E74  4C 89 A4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r12
00AF8E7C  0F 57 C0                        xorps xmm0, xmm0
00AF8E7F  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
00AF8E87  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
00AF8E8F  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
00AF8E97  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
00AF8E9C  48 83 A4 24 B0 00 00 00 00      and qword ptr [rsp + 0xb0], 0
00AF8EA5  83 A4 24 90 00 00 00 00         and dword ptr [rsp + 0x90], 0
00AF8EAD  33 F6                           xor esi, esi
00AF8EAF  45 33 F6                        xor r14d, r14d
00AF8EB2  33 C0                           xor eax, eax
00AF8EB4  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00AF8EBB  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00AF8EC2  48 21 84 24 88 00 00 00         and qword ptr [rsp + 0x88], rax
00AF8ECA  48 21 84 24 C8 00 00 00         and qword ptr [rsp + 0xc8], rax
00AF8ED2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF8EDB  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00AF8EE2  44 88 4C 24 60                  mov byte ptr [rsp + 0x60], r9b
00AF8EE7  44 8D 7E 01                     lea r15d, [rsi + 1]
00AF8EEB  45 3A CF                        cmp r9b, r15b
00AF8EEE  75 39                           jne 0x140af8f29
00AF8EF0  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00AF8EFA  4D 85 E4                        test r12, r12
00AF8EFD  74 0E                           je 0x140af8f0d
00AF8EFF  48 8B CB                        mov rcx, rbx
00AF8F02  4C 3B E3                        cmp r12, rbx
00AF8F05  49 0F 42 CC                     cmovb rcx, r12
00AF8F09  8B 01                           mov eax, dword ptr [rcx]
00AF8F0B  89 01                           mov dword ptr [rcx], eax
00AF8F0D  4D 85 C0                        test r8, r8
00AF8F10  74 10                           je 0x140af8f22
00AF8F12  48 8B CB                        mov rcx, rbx
00AF8F15  4C 3B C3                        cmp r8, rbx
00AF8F18  49 0F 42 C8                     cmovb rcx, r8
00AF8F1C  48 8B 01                        mov rax, qword ptr [rcx]
00AF8F1F  48 89 01                        mov qword ptr [rcx], rax
00AF8F22  EB 0F                           jmp 0x140af8f33
00AF8F24  E9 85 04 00 00                  jmp 0x140af93ae
00AF8F29  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00AF8F33  45 85 ED                        test r13d, r13d
00AF8F36  0F 84 EB 00 00 00               je 0x140af9027
00AF8F3C  41 81 FD FF FF 00 00            cmp r13d, 0xffff
00AF8F43  76 0D                           jbe 0x140af8f52
00AF8F45  C7 44 24 64 04 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000004
00AF8F4D  E9 3A 03 00 00                  jmp 0x140af928c
00AF8F52  41 83 FD 20                     cmp r13d, 0x20
00AF8F56  77 12                           ja 0x140af8f6a
00AF8F58  48 8D B4 24 28 01 00 00         lea rsi, [rsp + 0x128]
00AF8F60  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
00AF8F68  EB 3D                           jmp 0x140af8fa7
00AF8F6A  41 B8 45 6E 50 49               mov r8d, 0x49506e45
00AF8F70  49 8B D5                        mov rdx, r13
00AF8F73  B9 40 00 00 00                  mov ecx, 0x40
00AF8F78  E8 C3 25 86 FF                  call 0x14035b540
00AF8F7D  48 8B F0                        mov rsi, rax
00AF8F80  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00AF8F88  48 85 C0                        test rax, rax
00AF8F8B  75 0D                           jne 0x140af8f9a
00AF8F8D  C7 44 24 64 9A 00 00 C0         mov dword ptr [rsp + 0x64], 0xc000009a
00AF8F95  E9 F2 02 00 00                  jmp 0x140af928c
00AF8F9A  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00AF8FA2  44 8A 4C 24 60                  mov r9b, byte ptr [rsp + 0x60]
00AF8FA7  41 80 F9 01                     cmp r9b, 1
00AF8FAB  75 10                           jne 0x140af8fbd
00AF8FAD  4A 8D 04 2A                     lea rax, [rdx + r13]
00AF8FB1  48 3B C3                        cmp rax, rbx
00AF8FB4  77 05                           ja 0x140af8fbb
00AF8FB6  48 3B C2                        cmp rax, rdx
00AF8FB9  73 02                           jae 0x140af8fbd
00AF8FBB  8A 03                           mov al, byte ptr [rbx]
00AF8FBD  4D 8B C5                        mov r8, r13
00AF8FC0  48 8B CE                        mov rcx, rsi
00AF8FC3  E8 78 D8 BC FF                  call 0x1406c6840
00AF8FC8  41 BF 01 00 00 00               mov r15d, 1
00AF8FCE  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00AF8FD3  44 8A 4C 24 60                  mov r9b, byte ptr [rsp + 0x60]
00AF8FD8  4C 8B 9C 24 A8 00 00 00         mov r11, qword ptr [rsp + 0xa8]
00AF8FE0  EB 45                           jmp 0x140af9027
00AF8FE2  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AF8FE6  41 BF 01 00 00 00               mov r15d, 1
00AF8FEC  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00AF8FF3  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00AF8FFA  44 8B F0                        mov r14d, eax
00AF8FFD  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
00AF9005  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00AF900D  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00AF9012  4C 8B AC 24 F0 00 00 00         mov r13, qword ptr [rsp + 0xf0]
00AF901A  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00AF9022  E9 75 02 00 00                  jmp 0x140af929c
00AF9027  B8 FF 0F 00 00                  mov eax, 0xfff
00AF902C  85 84 24 98 00 00 00            test dword ptr [rsp + 0x98], eax
00AF9033  74 0D                           je 0x140af9042
00AF9035  C7 44 24 64 F0 00 00 C0         mov dword ptr [rsp + 0x64], 0xc00000f0
00AF903D  E9 4A 02 00 00                  jmp 0x140af928c
00AF9042  44 85 D8                        test eax, r11d
00AF9045  74 0D                           je 0x140af9054
00AF9047  C7 44 24 64 F2 00 00 C0         mov dword ptr [rsp + 0x64], 0xc00000f2
00AF904F  E9 38 02 00 00                  jmp 0x140af928c
00AF9054  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF905D  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00AF9064  49 83 FA FF                     cmp r10, -1
00AF9068  75 0A                           jne 0x140af9074
00AF906A  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
00AF9072  EB 41                           jmp 0x140af90b5
00AF9074  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00AF907A  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AF9080  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AF9088  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF908D  C7 44 24 20 4D 6D 56 6D         mov dword ptr [rsp + 0x20], 0x6d566d4d
00AF9095  4C 8B 05 FC D9 4C 00            mov r8, qword ptr [rip + 0x4cd9fc]
00AF909C  BA 08 00 00 00                  mov edx, 8
00AF90A1  49 8B CA                        mov rcx, r10
00AF90A4  E8 A7 05 D7 FF                  call 0x140869650
00AF90A9  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AF90AD  85 C0                           test eax, eax
00AF90AF  0F 88 D7 01 00 00               js 0x140af928c
00AF90B5  4C 8D 84 24 F8 00 00 00         lea r8, [rsp + 0xf8]
00AF90BD  33 D2                           xor edx, edx
00AF90BF  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF90C7  E8 54 D7 71 FF                  call 0x140216820
00AF90CC  44 89 BC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r15d
00AF90D4  4C 8D 44 24 64                  lea r8, [rsp + 0x64]
00AF90D9  33 D2                           xor edx, edx
00AF90DB  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00AF90E3  E8 A8 D5 81 FF                  call 0x140316690
00AF90E8  4C 8B F0                        mov r14, rax
00AF90EB  48 85 C0                        test rax, rax
00AF90EE  0F 84 90 01 00 00               je 0x140af9284
00AF90F4  8B 40 30                        mov eax, dword ptr [rax + 0x30]
00AF90F7  0F BA E0 15                     bt eax, 0x15
00AF90FB  73 11                           jae 0x140af910e
00AF90FD  0F BA E0 1A                     bt eax, 0x1a
00AF9101  72 0B                           jb 0x140af910e
00AF9103  0F BA E0 1B                     bt eax, 0x1b
00AF9107  73 05                           jae 0x140af910e
00AF9109  41 8B C7                        mov eax, r15d
00AF910C  EB 02                           jmp 0x140af9110
00AF910E  33 C0                           xor eax, eax
00AF9110  85 C0                           test eax, eax
00AF9112  0F 84 6C 01 00 00               je 0x140af9284
00AF9118  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
00AF911C  41 84 C7                        test r15b, al
00AF911F  0F 85 D4 00 00 00               jne 0x140af91f9
00AF9125  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
00AF9129  80 78 4C 00                     cmp byte ptr [rax + 0x4c], 0
00AF912D  75 5C                           jne 0x140af918b
00AF912F  BA 44 66 6C 74                  mov edx, 0x746c6644
00AF9134  48 8B CB                        mov rcx, rbx
00AF9137  E8 44 6E 71 FF                  call 0x14020ff80
00AF913C  48 8B D8                        mov rbx, rax
00AF913F  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00AF9147  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF914C  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00AF9151  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00AF9156  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00AF915E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF9163  4C 8B CB                        mov r9, rbx
00AF9166  44 8A 44 24 60                  mov r8b, byte ptr [rsp + 0x60]
00AF916B  49 8B D6                        mov rdx, r14
00AF916E  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF9176  E8 D1 8B FB FF                  call 0x140ab1d4c
00AF917B  44 8B F8                        mov r15d, eax
00AF917E  45 33 F6                        xor r14d, r14d
00AF9181  48 8B CB                        mov rcx, rbx
00AF9184  E8 C7 01 80 FF                  call 0x1402f9350
00AF9189  EB 64                           jmp 0x140af91ef
00AF918B  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00AF9193  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AF9198  8B 84 24 B0 01 00 00            mov eax, dword ptr [rsp + 0x1b0]
00AF919F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AF91A3  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
00AF91AB  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00AF91B0  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AF91B8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF91BD  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00AF91C2  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00AF91C7  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00AF91CF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF91D4  44 8A 4C 24 60                  mov r9b, byte ptr [rsp + 0x60]
00AF91D9  4D 8B C6                        mov r8, r14
00AF91DC  48 8B D3                        mov rdx, rbx
00AF91DF  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF91E7  E8 28 3F FD FF                  call 0x140acd114
00AF91EC  44 8B F8                        mov r15d, eax
00AF91EF  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00AF91F4  E9 93 00 00 00                  jmp 0x140af928c
00AF91F9  45 85 ED                        test r13d, r13d
00AF91FC  0F 85 43 FD FF FF               jne 0x140af8f45
00AF9202  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
00AF920A  4D 85 FF                        test r15, r15
00AF920D  0F 84 34 FE FF FF               je 0x140af9047
00AF9213  33 D2                           xor edx, edx
00AF9215  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00AF921D  E8 0E EB 71 FF                  call 0x140217d30
00AF9222  44 21 AC 24 80 00 00 00         and dword ptr [rsp + 0x80], r13d
00AF922A  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AF9232  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AF9237  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00AF923F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF9244  8B 84 24 B0 01 00 00            mov eax, dword ptr [rsp + 0x1b0]
00AF924B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AF924F  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00AF9254  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AF925C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF9261  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
00AF9269  44 8A 44 24 60                  mov r8b, byte ptr [rsp + 0x60]
00AF926E  49 8B D6                        mov rdx, r14
00AF9271  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF9279  E8 2E E0 F4 FF                  call 0x140a472ac
00AF927E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AF9282  EB 08                           jmp 0x140af928c
00AF9284  C7 44 24 64 18 00 00 C0         mov dword ptr [rsp + 0x64], 0xc0000018
00AF928C  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00AF9291  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
00AF9296  41 BF 01 00 00 00               mov r15d, 1
00AF929C  4D 85 F6                        test r14, r14
00AF929F  74 08                           je 0x140af92a9
00AF92A1  49 8B CE                        mov rcx, r14
00AF92A4  E8 B7 DB 81 FF                  call 0x140316e60
00AF92A9  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00AF92B1  74 0F                           je 0x140af92c2
00AF92B3  33 D2                           xor edx, edx
00AF92B5  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00AF92BD  E8 6E EA 71 FF                  call 0x140217d30
00AF92C2  E8 FD D9 B8 FF                  call 0x140686cc4
00AF92C7  85 C0                           test eax, eax
00AF92C9  75 3C                           jne 0x140af9307
00AF92CB  45 33 FF                        xor r15d, r15d
00AF92CE  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF92D6  48 85 C9                        test rcx, rcx
00AF92D9  74 10                           je 0x140af92eb
00AF92DB  48 83 FB FF                     cmp rbx, -1
00AF92DF  74 0A                           je 0x140af92eb
00AF92E1  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00AF92E6  E8 F5 E5 7F FF                  call 0x1402f78e0
00AF92EB  48 85 F6                        test rsi, rsi
00AF92EE  74 17                           je 0x140af9307
00AF92F0  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
00AF92F8  48 3B F0                        cmp rsi, rax
00AF92FB  74 0A                           je 0x140af9307
00AF92FD  33 D2                           xor edx, edx
00AF92FF  48 8B CE                        mov rcx, rsi
00AF9302  E8 69 95 08 00                  call 0x140b82870
00AF9307  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00AF930F  48 85 DB                        test rbx, rbx
00AF9312  74 29                           je 0x140af933d
00AF9314  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00AF9317  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AF931B  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00AF931E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AF9322  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00AF9326  33 D2                           xor edx, edx
00AF9328  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF9330  E8 2B E1 D9 FF                  call 0x140897460
00AF9335  48 8B CB                        mov rcx, rbx
00AF9338  E8 77 F6 D0 FF                  call 0x1408089b4
00AF933D  45 85 FF                        test r15d, r15d
00AF9340  74 3B                           je 0x140af937d
00AF9342  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF934A  48 85 C9                        test rcx, rcx
00AF934D  74 12                           je 0x140af9361
00AF934F  48 83 7C 24 70 FF               cmp qword ptr [rsp + 0x70], -1
00AF9355  74 0A                           je 0x140af9361
00AF9357  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00AF935C  E8 7F E5 7F FF                  call 0x1402f78e0
00AF9361  48 85 F6                        test rsi, rsi
00AF9364  74 17                           je 0x140af937d
00AF9366  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
00AF936E  48 3B F0                        cmp rsi, rax
00AF9371  74 0A                           je 0x140af937d
00AF9373  33 D2                           xor edx, edx
00AF9375  48 8B CE                        mov rcx, rsi
00AF9378  E8 F3 94 08 00                  call 0x140b82870
00AF937D  4D 85 ED                        test r13, r13
00AF9380  74 16                           je 0x140af9398
00AF9382  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00AF938A  49 89 45 00                     mov qword ptr [r13], rax
00AF938E  EB 08                           jmp 0x140af9398
00AF9390  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00AF9398  4D 85 E4                        test r12, r12
00AF939B  74 0D                           je 0x140af93aa
00AF939D  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00AF93A4  41 89 04 24                     mov dword ptr [r12], eax
00AF93A8  EB 00                           jmp 0x140af93aa
00AF93AA  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00AF93AE  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
00AF93B6  48 33 CC                        xor rcx, rsp
00AF93B9  E8 82 32 BB FF                  call 0x1406ac640
00AF93BE  48 81 C4 58 01 00 00            add rsp, 0x158
00AF93C5  41 5F                           pop r15
00AF93C7  41 5E                           pop r14
00AF93C9  41 5D                           pop r13
00AF93CB  41 5C                           pop r12
00AF93CD  5E                              pop rsi
00AF93CE  5B                              pop rbx
00AF93CF  C3                              ret
00AF93D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtLoadEnclaveData(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m124;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (344);
    result = (*(unsigned __int64 *)(v_rip + 3217719)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mE0 = a4;
    v_stack_mC8 = a3;
    v_stack_mF0 = a2;
    v_stack_m118 = a1;
    v_stack_m110 = a8;
    v_stack_mA0 = a1;
    v_stack_mB0 = a6;
    v_stack_m98 = a8;
    v_stack_mB8 = a9;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_rsi = 0;
    v_r14 = 0;
    result = 0;
    v_stack_m108 = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != ((unsigned __int8)(v_rsi + 1))) goto loc_00AF8F29;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (a9 != 0) {
        a1 = v_rbx;
        if (a9 < v_rbx) { a1 = a9; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    if (a8 != 0) {
        a1 = v_rbx;
        if (a8 < v_rbx) { a1 = a8; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
    }
    goto loc_00AF8F33;
loc_00AF8F29:
loc_00AF8F33:
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00AF9027;
    if (((unsigned int)((unsigned int)(a7))) <= 0xFFFFULL) goto loc_00AF8F52;
loc_00AF8F45:
    v_stack_m124 = 0xC0000004ULL;
    goto loc_00AF928C;
loc_00AF8F52:
    if (((unsigned int)((unsigned int)(a7))) > 32) goto loc_00AF8F6A;
    v_stack_mD0 = v_stack_m60;
    goto loc_00AF8FA7;
loc_00AF8F6A:
    result = MiAllocatePool(64, (unsigned int)(a7), (unsigned int)(0x49506E45ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mD0 = result;
    if (result != 0) goto loc_00AF8F9A;
    v_stack_m124 = 0xC000009AULL;
    goto loc_00AF928C;
loc_00AF8F9A:
loc_00AF8FA7:
    if (((unsigned __int8)(v_stack_m128)) != 1) goto loc_00AF8FBD;
    if ((v_stack_mB0 + (unsigned int)(a7) * 1) > v_rbx) goto loc_00AF8FBB;
    result = v_stack_mB0 + (unsigned int)(a7) * 1;
    if ((v_stack_mB0 + (unsigned int)(a7) * 1) < v_stack_mB0) {
        result = *(unsigned __int8 *)(v_rbx);
    }
    result = memcpy(result, v_stack_mB0, (unsigned int)(a7), v_stack_m128);
    goto loc_00AF9027;
loc_00AF9027:
    if (((v_stack_mF0) & ((unsigned int)((unsigned int)(0xFFFULL)))) == 0) goto loc_00AF9042;
    v_stack_m124 = 0xC00000F0ULL;
    goto loc_00AF928C;
loc_00AF9042:
    if ((((unsigned int)((unsigned int)(0xFFFULL))) & ((unsigned int)(v_stack_mE0))) == 0) goto loc_00AF9054;
loc_00AF9047:
    v_stack_m124 = 0xC00000F2ULL;
    goto loc_00AF928C;
loc_00AF9054:
    if (v_stack_m118 != -1) goto loc_00AF9074;
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    goto loc_00AF90B5;
loc_00AF9074:
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m118, 8, *(unsigned __int64 *)(v_rip + 5036540), v_stack_m128);
    v_stack_m124 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF928C;
loc_00AF90B5:
    a2 = 0;
    result = KiStackAttachProcess(v_stack_m100, a2, v_stack_m90, v_stack_m128);
    v_stack_m108 = 1;
    a2 = 0;
    result = MiObtainReferencedVadEx(v_stack_mF0, a2, v_stack_m124, v_stack_m128);
    if (result == 0) goto loc_00AF9284;
    if (condition_is_above_or_equal) goto loc_00AF910E;
    if (condition_is_below) goto loc_00AF910E;
    if (condition_is_above_or_equal) goto loc_00AF910E;
    goto loc_00AF9110;
loc_00AF910E:
    result = 0;
loc_00AF9110:
    if (0 == 0) goto loc_00AF9284;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 64))))) != 0) goto loc_00AF91F9;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 72) + 76)) != 0) goto loc_00AF918B;
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0x746C6644ULL), v_stack_m124, v_stack_m128);
    v_stack_m150 = v_stack_mC0;
    v_stack_m158 = result;
    v_stack_m160 = (unsigned int)((unsigned int)(a7));
    v_stack_m168 = v_stack_mF0;
    result = MiLoadSectionIntoVsmEnclave(v_stack_m100, result, v_stack_m128, result);
    v_r14 = 0;
    result = ObfDereferenceObject(result, result, v_stack_m128, result);
    goto loc_00AF91EF;
loc_00AF918B:
    v_stack_m138 = v_stack_mD8;
    v_stack_m140 = (unsigned int)((unsigned int)(a5));
    v_stack_m148 = v_stack_mE0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = result;
    v_stack_m160 = (unsigned int)((unsigned int)(a7));
    v_stack_m168 = v_stack_mF0;
    result = MiLoadDataIntoVsmEnclave(v_stack_m100, result, 0, v_stack_m128);
loc_00AF91EF:
    v_stack_m124 = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00AF928C;
loc_00AF91F9:
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_00AF8F45;
    if (v_stack_mE0 == 0) goto loc_00AF9047;
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m90, a2, 0, v_stack_m128);
    v_stack_m148 = v_stack_mF8;
    v_stack_m150 = v_stack_mD8;
    v_stack_m158 = (unsigned int)((unsigned int)(a5));
    v_stack_m160 = v_stack_mE0;
    v_stack_m168 = v_stack_mC8;
    result = MiCopyPagesIntoEnclave(v_stack_m100, 0, v_stack_m128, v_stack_mF0);
    v_stack_m124 = (unsigned int)(result);
    goto loc_00AF928C;
loc_00AF9284:
    v_stack_m124 = 0xC0000018ULL;
loc_00AF928C:
loc_00AF929C:
    if (0 != 0) {
        a1 = 0;
        result = MiUnlockAndDereferenceVad(a1, 0, v_stack_m128, v_stack_mF0);
    }
    if (v_stack_m108 != 0) {
        a2 = 0;
        a1 = v_stack_m90;
        result = KiUnstackDetachProcess(a1, a2, v_stack_m128, v_stack_mF0);
    }
    result = Feature_4234569016__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m128, v_stack_mF0);
    if ((unsigned int)(result) != 0) goto loc_00AF9307;
    v_r15 = 0;
    if (v_stack_m100 == 0) goto loc_00AF92EB;
    if (v_stack_m118 != -1) {
        a2 = 0x6D566D4DULL;
        result = ObfDereferenceObjectWithTag(v_stack_m100, a2, v_stack_m128, v_stack_mF0);
    }
    if (result == 0) goto loc_00AF9307;
    result = v_stack_m60;
    if (result != v_stack_m60) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m128, v_stack_mF0);
    }
    if (v_stack_mC0 != 0) {
        result = *(unsigned int *)(v_stack_mC0 + 40);
        v_stack_m158 = (unsigned int)(result);
        result = *(unsigned int *)(v_stack_mC0 + 36);
        v_stack_m160 = (unsigned int)(result);
        a3 = *(unsigned __int64 *)(v_stack_mC0 + 16);
        a2 = 0;
        a1 = v_stack_m100;
        result = DbgkMapViewOfSection(a1, a2, a3, v_stack_mF0);
        a1 = v_stack_mC0;
        result = MiDereferenceEnclaveModule(a1, a2, a3, v_stack_mF0);
    }
    if (0 == 0) goto loc_00AF937D;
    if (v_stack_m100 == 0) goto loc_00AF9361;
    if (v_stack_m118 != -1) {
        a2 = 0x6D566D4DULL;
        result = ObfDereferenceObjectWithTag(v_stack_m100, a2, a3, v_stack_mF0);
    }
    if (result == 0) goto loc_00AF937D;
    result = v_stack_m60;
    if (result != v_stack_m60) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_mF0);
    }
    if (v_stack_m110 == 0) goto loc_00AF9398;
    *(unsigned __int64 *)(v_stack_m110) = v_stack_mD8;
    goto loc_00AF9398;
loc_00AF9398:
    if (a9 == 0) goto loc_00AF93AA;
    *(unsigned int *)(a9) = (unsigned int)((unsigned int)(v_stack_mF8));
    goto loc_00AF93AA;
loc_00AF93AA:
loc_00AF93AE:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_mF0);
    v_rsp = (v_rsp) + (344);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtLoadEnclaveData(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m124;
    uint8_t v_stack_m128;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m40;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (344);
    result = (*(uint64_t *)(v_rip + 0x311937)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mE0 = Arg4;
    v_stack_mC8 = Arg3;
    v_stack_mF0 = Arg2;
    v_stack_m118 = Arg1;
    v_stack_m110 = Arg8;
    v_stack_mA0 = Arg1;
    v_stack_mB0 = Arg6;
    v_stack_m98 = Arg8;
    v_stack_mB8 = Arg9;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    local_rsi = 0;
    local_r14 = 0;
    result = 0;
    v_stack_m108 = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != ((uint8_t)(local_rsi + 1))) goto loc_00AF8F29;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (Arg9 != 0) {
        Arg1 = local_rbx;
        if (Arg9 < local_rbx) { Arg1 = Arg9; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    if (Arg8 != 0) {
        Arg1 = local_rbx;
        if (Arg8 < local_rbx) { Arg1 = Arg8; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
    }
    goto loc_00AF8F33;
loc_00AF8F29:
loc_00AF8F33:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00AF9027;
    if (((uint32_t)((uint32_t)(Arg7))) <= 0xFFFFULL) goto loc_00AF8F52;
loc_00AF8F45:
    v_stack_m124 = 0xC0000004ULL;
    goto loc_00AF928C;
loc_00AF8F52:
    if (((uint32_t)((uint32_t)(Arg7))) > 32) goto loc_00AF8F6A;
    v_stack_mD0 = v_stack_m60;
    goto loc_00AF8FA7;
loc_00AF8F6A:
    result = MiAllocatePool(64, (uint32_t)(Arg7), (uint32_t)(0x49506E45ULL), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mD0 = result;
    if (result != 0) goto loc_00AF8F9A;
    v_stack_m124 = 0xC000009AULL;
    goto loc_00AF928C;
loc_00AF8F9A:
loc_00AF8FA7:
    if (((uint8_t)(v_stack_m128)) != 1) goto loc_00AF8FBD;
    if ((v_stack_mB0 + (uint32_t)(Arg7) * 1) > local_rbx) goto loc_00AF8FBB;
    result = v_stack_mB0 + (uint32_t)(Arg7) * 1;
    if ((v_stack_mB0 + (uint32_t)(Arg7) * 1) < v_stack_mB0) {
        result = *(uint8_t *)(local_rbx);
    }
    result = memcpy(result, v_stack_mB0, (uint32_t)(Arg7), v_stack_m128);
    goto loc_00AF9027;
loc_00AF9027:
    if (((v_stack_mF0) & ((uint32_t)((uint32_t)(0xFFFULL)))) == 0) goto loc_00AF9042;
    v_stack_m124 = 0xC00000F0ULL;
    goto loc_00AF928C;
loc_00AF9042:
    if ((((uint32_t)((uint32_t)(0xFFFULL))) & ((uint32_t)(v_stack_mE0))) == 0) goto loc_00AF9054;
loc_00AF9047:
    v_stack_m124 = 0xC00000F2ULL;
    goto loc_00AF928C;
loc_00AF9054:
    if (v_stack_m118 != -1) goto loc_00AF9074;
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    goto loc_00AF90B5;
loc_00AF9074:
    v_stack_m160 = v_stack_m100;
    v_stack_m168 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m118, 8, *(uint64_t *)(v_rip + 0x4CD9FC), v_stack_m128);
    v_stack_m124 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF928C;
loc_00AF90B5:
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_m100, Arg2, v_stack_m90, v_stack_m128);
    v_stack_m108 = 1;
    Arg2 = 0;
    result = MiObtainReferencedVadEx(v_stack_mF0, Arg2, v_stack_m124, v_stack_m128);
    if (result == 0) goto loc_00AF9284;
    if (condition_is_above_or_equal) goto loc_00AF910E;
    if (condition_is_below) goto loc_00AF910E;
    if (condition_is_above_or_equal) goto loc_00AF910E;
    goto loc_00AF9110;
loc_00AF910E:
    result = 0;
loc_00AF9110:
    if (0 == 0) goto loc_00AF9284;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x40))))) != 0) goto loc_00AF91F9;
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x48) + 0x4C)) != 0) goto loc_00AF918B;
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0x746C6644ULL), v_stack_m124, v_stack_m128);
    v_stack_m150 = v_stack_mC0;
    v_stack_m158 = result;
    v_stack_m160 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m168 = v_stack_mF0;
    result = MiLoadSectionIntoVsmEnclave(v_stack_m100, result, v_stack_m128, result);
    local_r14 = 0;
    result = ObfDereferenceObject(result, result, v_stack_m128, result);
    goto loc_00AF91EF;
loc_00AF918B:
    v_stack_m138 = v_stack_mD8;
    v_stack_m140 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m148 = v_stack_mE0;
    v_stack_m150 = v_stack_mC8;
    v_stack_m158 = result;
    v_stack_m160 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m168 = v_stack_mF0;
    result = MiLoadDataIntoVsmEnclave(v_stack_m100, result, 0, v_stack_m128);
loc_00AF91EF:
    v_stack_m124 = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00AF928C;
loc_00AF91F9:
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_00AF8F45;
    if (v_stack_mE0 == 0) goto loc_00AF9047;
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m90, Arg2, 0, v_stack_m128);
    v_stack_m148 = v_stack_mF8;
    v_stack_m150 = v_stack_mD8;
    v_stack_m158 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m160 = v_stack_mE0;
    v_stack_m168 = v_stack_mC8;
    result = MiCopyPagesIntoEnclave(v_stack_m100, 0, v_stack_m128, v_stack_mF0);
    v_stack_m124 = (uint32_t)(result);
    goto loc_00AF928C;
loc_00AF9284:
    v_stack_m124 = 0xC0000018ULL;
loc_00AF928C:
loc_00AF929C:
    if (0 != 0) {
        Arg1 = 0;
        result = MiUnlockAndDereferenceVad(Arg1, 0, v_stack_m128, v_stack_mF0);
    }
    if (v_stack_m108 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m90;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_m128, v_stack_mF0);
    }
    result = Feature_4234569016__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m128, v_stack_mF0);
    if ((uint32_t)(result) != 0) goto loc_00AF9307;
    local_r15 = 0;
    if (v_stack_m100 == 0) goto loc_00AF92EB;
    if (v_stack_m118 != -1) {
        Arg2 = 0x6D566D4DULL;
        result = ObfDereferenceObjectWithTag(v_stack_m100, Arg2, v_stack_m128, v_stack_mF0);
    }
    if (result == 0) goto loc_00AF9307;
    result = v_stack_m60;
    if (result != v_stack_m60) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m128, v_stack_mF0);
    }
    if (v_stack_mC0 != 0) {
        result = *(uint32_t *)(v_stack_mC0 + 0x28);
        v_stack_m158 = (uint32_t)(result);
        result = *(uint32_t *)(v_stack_mC0 + 0x24);
        v_stack_m160 = (uint32_t)(result);
        Arg3 = *(uint64_t *)(v_stack_mC0 + 0x10);
        Arg2 = 0;
        Arg1 = v_stack_m100;
        result = DbgkMapViewOfSection(Arg1, Arg2, Arg3, v_stack_mF0);
        Arg1 = v_stack_mC0;
        result = MiDereferenceEnclaveModule(Arg1, Arg2, Arg3, v_stack_mF0);
    }
    if (0 == 0) goto loc_00AF937D;
    if (v_stack_m100 == 0) goto loc_00AF9361;
    if (v_stack_m118 != -1) {
        Arg2 = 0x6D566D4DULL;
        result = ObfDereferenceObjectWithTag(v_stack_m100, Arg2, Arg3, v_stack_mF0);
    }
    if (result == 0) goto loc_00AF937D;
    result = v_stack_m60;
    if (result != v_stack_m60) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_mF0);
    }
    if (v_stack_m110 == 0) goto loc_00AF9398;
    *(uint64_t *)(v_stack_m110) = v_stack_mD8;
    goto loc_00AF9398;
loc_00AF9398:
    if (Arg9 == 0) goto loc_00AF93AA;
    *(uint32_t *)(Arg9) = (uint32_t)((uint32_t)(v_stack_mF8));
    goto loc_00AF93AA;
loc_00AF93AA:
loc_00AF93AE:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_mF0);
    local_rsp = (local_rsp) + (344);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF8DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
