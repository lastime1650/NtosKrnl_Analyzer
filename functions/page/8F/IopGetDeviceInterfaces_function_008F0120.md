# IopGetDeviceInterfaces

- RVA: `0x008F0120`–`0x008F0A14` (길이 `2,292` bytes)
- VA: `0x00000001408F0120`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000871E4`
- 디코드: `544`개 명령, `2,292/2,292` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x008F01E3` → [PnpStringFromGuid](PnpStringFromGuid_function_008F5A2C.md) (function, `0x008F5A2C`)
- `0x008F0210` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x008F0226` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008F028A` → [PiPnpRtlCmActionCallback](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (function, `0x008EF110`)
- `0x008F02CF` → [_CmOpenCommonClassRegKeyWorker](_CmOpenCommonClassRegKeyWorker_function_008F0A1C.md) (function, `0x008F0A1C`)
- `0x008F0353` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E1110.md) (function, `0x008E1110`)
- `0x008F03A6` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008F03ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F0406` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F0448` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008F04D5` → [PiPnpRtlCmActionCallback](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (function, `0x008EF110`)
- `0x008F0524` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x008F0553` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008F0558` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008F0589` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008F05B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F05E4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008F0658` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F0720` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F0740` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008F076B` → [CmValidateDeviceInterfaceName](CmValidateDeviceInterfaceName_function_008F1A40.md) (function, `0x008F1A40`)
- `0x008F07BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F081D` → [CmGetMatchingFilteredDeviceInterfaceListWorker](../A0/CmGetMatchingFilteredDeviceInterfaceListWorker_function_00A097EC.md) (function, `0x00A097EC`)
- `0x008F0851` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F08B6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F08EB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F0955` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x008F0987` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008F09AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F09C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008F09EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F09FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008F0A0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IoGetDeviceInterfaces](../95/IoGetDeviceInterfaces_function_00953340.md) at `0x00953395`
- [PiCMGetDeviceInterfaceList](../A1/PiCMGetDeviceInterfaceList_function_00A163D0.md) at `0x00A16586`

### Static image references
- `0x008F013F` → RVA `0x00E0A740` (`.data`; read)
- `0x008F0208` → RVA `0x00F8C600` (`.data`; read)
- `0x008F0215` → RVA `0x00E66398` (`.data`; read)
- `0x008F0244` → RVA `0x008EF110` (`PiPnpRtlCmActionCallback`; read)
- `0x008F0339` → RVA `0x00013348` (`.rdata`; read)
- `0x008F0482` → RVA `0x008E5410` (`IopDeviceInterfaceFilterCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x008F0210` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x008F0226` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008F03ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F0406` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F0448` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008F0553` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008F0558` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008F0589` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008F05B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F05E4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008F0658` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F0720` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F0740` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008F07BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F0851` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F08B6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F08EB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F0955` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x008F0987` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008F09AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F09C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008F09EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F09FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008F0A0A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008F0361` → [sub_00B1E436 + 0xD](../B1/Unknown_function_00B1E436.md) (`tail-transfer`)
  - `0x008F0902` → [sub_00B1E436](../B1/Unknown_function_00B1E436.md) (`tail-transfer`)
  - `0x008F096E` → [sub_00B1E436 + 0x24D](../B1/Unknown_function_00B1E436.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008F0120  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008F0125  55                              push rbp
008F0126  56                              push rsi
008F0127  57                              push rdi
008F0128  41 54                           push r12
008F012A  41 55                           push r13
008F012C  41 56                           push r14
008F012E  41 57                           push r15
008F0130  48 8D AC 24 10 FF FF FF         lea rbp, [rsp - 0xf0]
008F0138  48 81 EC F0 01 00 00            sub rsp, 0x1f0
008F013F  48 8B 05 FA A5 51 00            mov rax, qword ptr [rip + 0x51a5fa]
008F0146  48 33 C4                        xor rax, rsp
008F0149  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
008F0150  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
008F0157  0F 57 C0                        xorps xmm0, xmm0
008F015A  48 8B BD 58 01 00 00            mov rdi, qword ptr [rbp + 0x158]
008F0161  4C 8B E2                        mov r12, rdx
008F0164  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
008F0168  33 D2                           xor edx, edx
008F016A  44 89 45 8C                     mov dword ptr [rbp - 0x74], r8d
008F016E  45 33 C0                        xor r8d, r8d
008F0171  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
008F0175  41 8B F0                        mov esi, r8d
008F0178  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
008F017F  4C 89 00                        mov qword ptr [rax], r8
008F0182  44 88 4C 24 6A                  mov byte ptr [rsp + 0x6a], r9b
008F0187  45 8A F8                        mov r15b, r8b
008F018A  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
008F018E  45 8B E8                        mov r13d, r8d
008F0191  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
008F0195  45 8B F0                        mov r14d, r8d
008F0198  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
008F019C  44 89 44 24 74                  mov dword ptr [rsp + 0x74], r8d
008F01A1  44 88 44 24 60                  mov byte ptr [rsp + 0x60], r8b
008F01A6  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
008F01AB  44 88 44 24 68                  mov byte ptr [rsp + 0x68], r8b
008F01B0  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
008F01B4  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
008F01B8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
008F01BC  4C 89 45 90                     mov qword ptr [rbp - 0x70], r8
008F01C0  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
008F01C4  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
008F01C9  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
008F01CE  44 89 44 24 6C                  mov dword ptr [rsp + 0x6c], r8d
008F01D3  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
008F01D7  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
008F01DB  44 89 45 88                     mov dword ptr [rbp - 0x78], r8d
008F01DF  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
008F01E3  E8 44 58 00 00                  call 0x1408f5a2c
008F01E8  8B D8                           mov ebx, eax
008F01EA  85 C0                           test eax, eax
008F01EC  0F 88 ED 07 00 00               js 0x1408f09df
008F01F2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008F01FB  48 83 C9 FF                     or rcx, 0xffffffffffffffff
008F01FF  B2 01                           mov dl, 1
008F0201  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
008F0208  48 8D 0D F1 C3 69 00            lea rcx, [rip + 0x69c3f1]
008F020F  90                              nop
008F0210  E8 0B 4C 92 FF                  call 0x140214e20
008F0215  48 8B 35 7C 61 57 00            mov rsi, qword ptr [rip + 0x57617c]
008F021C  45 8D 46 58                     lea r8d, [r14 + 0x58]
008F0220  33 D2                           xor edx, edx
008F0222  48 8D 4D 30                     lea rcx, [rbp + 0x30]
008F0226  E8 15 6A DD FF                  call 0x1406c6c40
008F022B  48 8B BE F8 01 00 00            mov rdi, qword ptr [rsi + 0x1f8]
008F0232  48 8D 45 B0                     lea rax, [rbp - 0x50]
008F0236  33 DB                           xor ebx, ebx
008F0238  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
008F023C  48 C7 45 40 40 00 00 00         mov qword ptr [rbp + 0x40], 0x40
008F0244  48 8D 05 C5 EE FF FF            lea rax, [rip - 0x113b]
008F024B  C7 45 48 3F 00 0F 00            mov dword ptr [rbp + 0x48], 0xf003f
008F0252  88 5D 4C                        mov byte ptr [rbp + 0x4c], bl
008F0255  8D 4B 0B                        lea ecx, [rbx + 0xb]
008F0258  8D 53 04                        lea edx, [rbx + 4]
008F025B  48 85 FF                        test rdi, rdi
008F025E  74 3D                           je 0x1408f029d
008F0260  48 3B F8                        cmp rdi, rax
008F0263  44 8B C9                        mov r9d, ecx
008F0266  48 8D 45 30                     lea rax, [rbp + 0x30]
008F026A  44 8B C2                        mov r8d, edx
008F026D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F0272  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
008F0279  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008F0281  48 8B CE                        mov rcx, rsi
008F0284  0F 85 29 06 00 00               jne 0x1408f08b3
008F028A  E8 81 EE FF FF                  call 0x1408ef110
008F028F  3D 02 00 00 C0                  cmp eax, 0xc0000002
008F0294  0F 85 FD 03 00 00               jne 0x1408f0697
008F029A  48 8B FB                        mov rdi, rbx
008F029D  44 8B 4D 44                     mov r9d, dword ptr [rbp + 0x44]
008F02A1  48 8D 45 58                     lea rax, [rbp + 0x58]
008F02A5  44 8B 45 40                     mov r8d, dword ptr [rbp + 0x40]
008F02A9  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
008F02B0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F02B5  48 8B CE                        mov rcx, rsi
008F02B8  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
008F02BC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F02C1  8A 45 4C                        mov al, byte ptr [rbp + 0x4c]
008F02C4  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008F02C8  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
008F02CB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008F02CF  E8 48 07 00 00                  call 0x1408f0a1c
008F02D4  8B D8                           mov ebx, eax
008F02D6  48 85 FF                        test rdi, rdi
008F02D9  0F 85 E1 05 00 00               jne 0x1408f08c0
008F02DF  33 F6                           xor esi, esi
008F02E1  81 FB 34 00 00 C0               cmp ebx, 0xc0000034
008F02E7  0F 84 53 03 00 00               je 0x1408f0640
008F02ED  81 FB 3A 00 00 C0               cmp ebx, 0xc000003a
008F02F3  0F 84 47 03 00 00               je 0x1408f0640
008F02F9  85 DB                           test ebx, ebx
008F02FB  0F 88 36 03 00 00               js 0x1408f0637
008F0301  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
008F0305  48 8D 44 24 74                  lea rax, [rsp + 0x74]
008F030A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008F030F  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
008F0316  48 8D 45 80                     lea rax, [rbp - 0x80]
008F031A  41 B9 04 00 00 00               mov r9d, 4
008F0320  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F0325  BA 00 04 00 00                  mov edx, 0x400
008F032A  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
008F032F  B9 50 6E 70 47                  mov ecx, 0x47706e50
008F0334  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F0339  48 8D 05 08 30 72 FF            lea rax, [rip - 0x8dcff8]
008F0340  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F0345  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008F0349  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008F034E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F0353  E8 B8 0D FF FF                  call 0x1408e1110
008F0358  8B D8                           mov ebx, eax
008F035A  BF 00 01 00 00                  mov edi, 0x100
008F035F  85 C0                           test eax, eax
008F0361  0F 89 DC E0 22 00               jns 0x140b1e443
008F0367  3D 25 02 00 C0                  cmp eax, 0xc0000225
008F036C  0F 85 AF 02 00 00               jne 0x1408f0621
008F0372  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
008F0376  33 DB                           xor ebx, ebx
008F0378  4D 85 E4                        test r12, r12
008F037B  0F 85 29 03 00 00               jne 0x1408f06aa
008F0381  33 C0                           xor eax, eax
008F0383  48 8D 4D D8                     lea rcx, [rbp - 0x28]
008F0387  0F 57 C0                        xorps xmm0, xmm0
008F038A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
008F038E  66 48 0F 7E C0                  movq rax, xmm0
008F0393  45 84 FF                        test r15b, r15b
008F0396  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
008F039A  48 0F 45 C6                     cmovne rax, rsi
008F039E  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008F03A2  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
008F03A6  E8 75 B4 F7 FF                  call 0x14086b820
008F03AB  B8 00 10 00 00                  mov eax, 0x1000
008F03B0  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008F03B4  45 84 FF                        test r15b, r15b
008F03B7  0F 85 60 05 00 00               jne 0x1408f091d
008F03BD  BB 23 00 00 C0                  mov ebx, 0xc0000023
008F03C2  41 8B CD                        mov ecx, r13d
008F03C5  BF E5 00 00 C0                  mov edi, 0xc00000e5
008F03CA  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
008F03CE  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008F03D4  0F 85 3F 01 00 00               jne 0x1408f0519
008F03DA  83 F9 05                        cmp ecx, 5
008F03DD  0F 83 36 01 00 00               jae 0x1408f0519
008F03E3  4D 85 F6                        test r14, r14
008F03E6  74 0E                           je 0x1408f03f6
008F03E8  33 D2                           xor edx, edx
008F03EA  49 8B CE                        mov rcx, r14
008F03ED  E8 7E 24 29 00                  call 0x140b82870
008F03F2  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
008F03F6  8B D0                           mov edx, eax
008F03F8  B9 00 01 00 00                  mov ecx, 0x100
008F03FD  48 03 D2                        add rdx, rdx
008F0400  41 B8 50 70 20 20               mov r8d, 0x20207050
008F0406  E8 E5 1C 29 00                  call 0x140b820f0
008F040B  4C 8B F0                        mov r14, rax
008F040E  48 85 C0                        test rax, rax
008F0411  0F 84 FD 00 00 00               je 0x1408f0514
008F0417  44 8B 64 24 64                  mov r12d, dword ptr [rsp + 0x64]
008F041C  44 89 65 88                     mov dword ptr [rbp - 0x78], r12d
008F0420  41 8B DC                        mov ebx, r12d
008F0423  45 84 FF                        test r15b, r15b
008F0426  0F 85 0B 05 00 00               jne 0x1408f0937
008F042C  4C 8B F8                        mov r15, rax
008F042F  4C 8B 2D 62 5F 57 00            mov r13, qword ptr [rip + 0x575f62]
008F0436  48 8D 4D 30                     lea rcx, [rbp + 0x30]
008F043A  33 D2                           xor edx, edx
008F043C  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
008F0440  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008F0444  44 8D 42 58                     lea r8d, [rdx + 0x58]
008F0448  E8 F3 67 DD FF                  call 0x1406c6c40
008F044D  4D 8B A5 F8 01 00 00            mov r12, qword ptr [r13 + 0x1f8]
008F0454  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
008F045B  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
008F045F  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008F0464  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
008F0468  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
008F046B  F7 D0                           not eax
008F046D  89 5D 70                        mov dword ptr [rbp + 0x70], ebx
008F0470  83 E0 01                        and eax, 1
008F0473  4C 89 7D 68                     mov qword ptr [rbp + 0x68], r15
008F0477  89 45 50                        mov dword ptr [rbp + 0x50], eax
008F047A  33 DB                           xor ebx, ebx
008F047C  89 9D 80 00 00 00               mov dword ptr [rbp + 0x80], ebx
008F0482  48 8D 05 87 4F FF FF            lea rax, [rip - 0xb079]
008F0489  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
008F048D  48 8D 45 D0                     lea rax, [rbp - 0x30]
008F0491  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
008F0495  48 8D 44 24 64                  lea rax, [rsp + 0x64]
008F049A  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
008F049E  4D 85 E4                        test r12, r12
008F04A1  0F 84 32 03 00 00               je 0x1408f07d9
008F04A7  48 8D 05 62 EC FF FF            lea rax, [rip - 0x139e]
008F04AE  33 D2                           xor edx, edx
008F04B0  4C 3B E0                        cmp r12, rax
008F04B3  44 8D 4B 11                     lea r9d, [rbx + 0x11]
008F04B7  48 8D 45 30                     lea rax, [rbp + 0x30]
008F04BB  49 8B CD                        mov rcx, r13
008F04BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F04C3  44 8D 43 03                     lea r8d, [rbx + 3]
008F04C7  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008F04CF  0F 85 AF 04 00 00               jne 0x1408f0984
008F04D5  E8 36 EC FF FF                  call 0x1408ef110
008F04DA  3D 02 00 00 C0                  cmp eax, 0xc0000002
008F04DF  0F 84 AC 04 00 00               je 0x1408f0991
008F04E5  3D 20 01 00 C0                  cmp eax, 0xc0000120
008F04EA  0F 85 A9 04 00 00               jne 0x1408f0999
008F04F0  8B 5D 30                        mov ebx, dword ptr [rbp + 0x30]
008F04F3  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
008F04F7  4D 2B FE                        sub r15, r14
008F04FA  8B 4C 24 74                     mov ecx, dword ptr [rsp + 0x74]
008F04FE  49 D1 FF                        sar r15, 1
008F0501  41 03 C7                        add eax, r15d
008F0504  44 8A 7C 24 60                  mov r15b, byte ptr [rsp + 0x60]
008F0509  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008F050D  FF C1                           inc ecx
008F050F  E9 B6 FE FF FF                  jmp 0x1408f03ca
008F0514  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008F0519  44 8B 65 88                     mov r12d, dword ptr [rbp - 0x78]
008F051D  45 33 FF                        xor r15d, r15d
008F0520  48 8D 4D D8                     lea rcx, [rbp - 0x28]
008F0524  E8 E7 B1 F7 FF                  call 0x14086b710
008F0529  85 DB                           test ebx, ebx
008F052B  78 16                           js 0x1408f0543
008F052D  44 39 7C 24 64                  cmp dword ptr [rsp + 0x64], r15d
008F0532  0F 84 44 01 00 00               je 0x1408f067c
008F0538  44 38 7C 24 6A                  cmp byte ptr [rsp + 0x6a], r15b
008F053D  0F 84 18 02 00 00               je 0x1408f075b
008F0543  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
008F0547  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
008F054C  48 8D 0D AD C0 69 00            lea rcx, [rip + 0x69c0ad]
008F0553  E8 B8 F4 96 FF                  call 0x14025fa10
008F0558  E8 53 D3 96 FF                  call 0x14025d8b0
008F055D  85 DB                           test ebx, ebx
008F055F  0F 88 A0 00 00 00               js 0x1408f0605
008F0565  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008F0569  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
008F056D  4C 89 30                        mov qword ptr [rax], r14
008F0570  48 85 C9                        test rcx, rcx
008F0573  74 08                           je 0x1408f057d
008F0575  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
008F0579  03 C0                           add eax, eax
008F057B  89 01                           mov dword ptr [rcx], eax
008F057D  4D 8B F7                        mov r14, r15
008F0580  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008F0584  48 85 C9                        test rcx, rcx
008F0587  74 05                           je 0x1408f058e
008F0589  E8 22 CD DB FF                  call 0x1406ad2b0
008F058E  4D 85 ED                        test r13, r13
008F0591  74 26                           je 0x1408f05b9
008F0593  4D 85 E4                        test r12, r12
008F0596  74 21                           je 0x1408f05b9
008F0598  66 45 39 7C 24 02               cmp word ptr [r12 + 2], r15w
008F059E  74 19                           je 0x1408f05b9
008F05A0  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
008F05A5  48 85 C0                        test rax, rax
008F05A8  74 0F                           je 0x1408f05b9
008F05AA  49 3B C5                        cmp rax, r13
008F05AD  74 0A                           je 0x1408f05b9
008F05AF  33 D2                           xor edx, edx
008F05B1  49 8B CD                        mov rcx, r13
008F05B4  E8 B7 22 29 00                  call 0x140b82870
008F05B9  48 85 F6                        test rsi, rsi
008F05BC  0F 85 25 04 00 00               jne 0x1408f09e7
008F05C2  4D 85 F6                        test r14, r14
008F05C5  0F 85 2B 04 00 00               jne 0x1408f09f6
008F05CB  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
008F05CF  48 85 C0                        test rax, rax
008F05D2  0F 85 2D 04 00 00               jne 0x1408f0a05
008F05D8  8B C3                           mov eax, ebx
008F05DA  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
008F05E1  48 33 CC                        xor rcx, rsp
008F05E4  E8 57 C0 DB FF                  call 0x1406ac640
008F05E9  48 8B 9C 24 40 02 00 00         mov rbx, qword ptr [rsp + 0x240]
008F05F1  48 81 C4 F0 01 00 00            add rsp, 0x1f0
008F05F8  41 5F                           pop r15
008F05FA  41 5E                           pop r14
008F05FC  41 5D                           pop r13
008F05FE  41 5C                           pop r12
008F0600  5F                              pop rdi
008F0601  5E                              pop rsi
008F0602  5D                              pop rbp
008F0603  C3                              ret
008F0604  CC                              int3
008F0605  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
008F0609  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008F060D  4C 89 38                        mov qword ptr [rax], r15
008F0610  48 85 FF                        test rdi, rdi
008F0613  0F 84 67 FF FF FF               je 0x1408f0580
008F0619  44 89 3F                        mov dword ptr [rdi], r15d
008F061C  E9 5F FF FF FF                  jmp 0x1408f0580
008F0621  3D 34 00 00 C0                  cmp eax, 0xc0000034
008F0626  0F 84 46 FD FF FF               je 0x1408f0372
008F062C  3D 3A 00 00 C0                  cmp eax, 0xc000003a
008F0631  0F 84 3B FD FF FF               je 0x1408f0372
008F0637  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
008F063B  E9 91 01 00 00                  jmp 0x1408f07d1
008F0640  BA 02 00 00 00                  mov edx, 2
008F0645  C7 44 24 64 01 00 00 00         mov dword ptr [rsp + 0x64], 1
008F064D  B9 00 01 00 00                  mov ecx, 0x100
008F0652  41 B8 50 70 20 20               mov r8d, 0x20207050
008F0658  E8 93 1A 29 00                  call 0x140b820f0
008F065D  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
008F0661  45 33 FF                        xor r15d, r15d
008F0664  4C 8B F0                        mov r14, rax
008F0667  48 85 C0                        test rax, rax
008F066A  0F 84 2F 01 00 00               je 0x1408f079f
008F0670  66 44 89 38                     mov word ptr [rax], r15w
008F0674  41 8B DF                        mov ebx, r15d
008F0677  E9 D0 FE FF FF                  jmp 0x1408f054c
008F067C  C7 44 24 64 01 00 00 00         mov dword ptr [rsp + 0x64], 1
008F0684  41 83 FC 01                     cmp r12d, 1
008F0688  0F 82 1A 03 00 00               jb 0x1408f09a8
008F068E  66 45 89 3E                     mov word ptr [r14], r15w
008F0692  E9 A1 FE FF FF                  jmp 0x1408f0538
008F0697  3D 20 01 00 C0                  cmp eax, 0xc0000120
008F069C  0F 85 FF 01 00 00               jne 0x1408f08a1
008F06A2  8B 5D 30                        mov ebx, dword ptr [rbp + 0x30]
008F06A5  E9 35 FC FF FF                  jmp 0x1408f02df
008F06AA  45 0F B7 44 24 02               movzx r8d, word ptr [r12 + 2]
008F06B0  41 B9 02 00 00 00               mov r9d, 2
008F06B6  66 45 3B C1                     cmp r8w, r9w
008F06BA  0F 82 91 00 00 00               jb 0x1408f0751
008F06C0  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
008F06C5  48 85 C9                        test rcx, rcx
008F06C8  0F 84 83 00 00 00               je 0x1408f0751
008F06CE  41 0F B7 14 24                  movzx edx, word ptr [r12]
008F06D3  66 41 3B D0                     cmp dx, r8w
008F06D7  0F 87 BA 01 00 00               ja 0x1408f0897
008F06DD  66 85 D2                        test dx, dx
008F06E0  0F 84 C3 00 00 00               je 0x1408f07a9
008F06E6  66 39 19                        cmp word ptr [rcx], bx
008F06E9  0F 84 9E 01 00 00               je 0x1408f088d
008F06EF  66 41 3B D0                     cmp dx, r8w
008F06F3  75 10                           jne 0x1408f0705
008F06F5  8B C2                           mov eax, edx
008F06F7  48 D1 E8                        shr rax, 1
008F06FA  66 39 5C 41 FE                  cmp word ptr [rcx + rax*2 - 2], bx
008F06FF  0F 84 88 01 00 00               je 0x1408f088d
008F0705  49 8B C0                        mov rax, r8
008F0708  49 2B C1                        sub rax, r9
008F070B  48 3B D0                        cmp rdx, rax
008F070E  0F 86 62 01 00 00               jbe 0x1408f0876
008F0714  49 03 D1                        add rdx, r9
008F0717  41 B8 50 70 73 75               mov r8d, 0x75737050
008F071D  48 8B CF                        mov rcx, rdi
008F0720  E8 CB 19 29 00                  call 0x140b820f0
008F0725  33 FF                           xor edi, edi
008F0727  48 8B D8                        mov rbx, rax
008F072A  48 85 C0                        test rax, rax
008F072D  0F 84 99 00 00 00               je 0x1408f07cc
008F0733  45 0F B7 04 24                  movzx r8d, word ptr [r12]
008F0738  48 8B C8                        mov rcx, rax
008F073B  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
008F0740  E8 FB 60 DD FF                  call 0x1406c6840
008F0745  41 0F B7 04 24                  movzx eax, word ptr [r12]
008F074A  48 D1 E8                        shr rax, 1
008F074D  66 89 3C 43                     mov word ptr [rbx + rax*2], di
008F0751  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
008F0756  E9 26 FC FF FF                  jmp 0x1408f0381
008F075B  49 8B FE                        mov rdi, r14
008F075E  66 44 39 3F                     cmp word ptr [rdi], r15w
008F0762  0F 84 DB FD FF FF               je 0x1408f0543
008F0768  48 8B D7                        mov rdx, rdi
008F076B  E8 D0 12 00 00                  call 0x1408f1a40
008F0770  8B D8                           mov ebx, eax
008F0772  85 C0                           test eax, eax
008F0774  0F 88 C9 FD FF FF               js 0x1408f0543
008F077A  48 B8 5C 00 3F 00 3F 00 5C 00   movabs rax, 0x5c003f003f005c
008F0784  48 89 07                        mov qword ptr [rdi], rax
008F0787  48 83 C8 FF                     or rax, 0xffffffffffffffff
008F078B  48 FF C0                        inc rax
008F078E  66 44 39 3C 47                  cmp word ptr [rdi + rax*2], r15w
008F0793  75 F6                           jne 0x1408f078b
008F0795  48 8D 3C 47                     lea rdi, [rdi + rax*2]
008F0799  48 83 C7 02                     add rdi, 2
008F079D  EB BF                           jmp 0x1408f075e
008F079F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008F07A4  E9 A3 FD FF FF                  jmp 0x1408f054c
008F07A9  66 39 19                        cmp word ptr [rcx], bx
008F07AC  0F 84 DB 00 00 00               je 0x1408f088d
008F07B2  41 B8 50 70 73 75               mov r8d, 0x75737050
008F07B8  49 8B D1                        mov rdx, r9
008F07BB  48 8B CF                        mov rcx, rdi
008F07BE  E8 2D 19 29 00                  call 0x140b820f0
008F07C3  48 85 C0                        test rax, rax
008F07C6  0F 85 44 01 00 00               jne 0x1408f0910
008F07CC  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008F07D1  45 33 FF                        xor r15d, r15d
008F07D4  E9 73 FD FF FF                  jmp 0x1408f054c
008F07D9  8B 85 80 00 00 00               mov eax, dword ptr [rbp + 0x80]
008F07DF  49 8B CD                        mov rcx, r13
008F07E2  44 8B 4D 50                     mov r9d, dword ptr [rbp + 0x50]
008F07E6  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
008F07EA  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
008F07EE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008F07F2  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
008F07F6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F07FB  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
008F07FE  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
008F0802  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
008F0806  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F080B  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
008F080F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F0814  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008F0818  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F081D  E8 CA 8F 11 00                  call 0x140a097ec
008F0822  8B D8                           mov ebx, eax
008F0824  4D 85 E4                        test r12, r12
008F0827  0F 84 C6 FC FF FF               je 0x1408f04f3
008F082D  33 D2                           xor edx, edx
008F082F  89 45 30                        mov dword ptr [rbp + 0x30], eax
008F0832  48 8D 45 30                     lea rax, [rbp + 0x30]
008F0836  49 8B CD                        mov rcx, r13
008F0839  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F083E  49 8B C4                        mov rax, r12
008F0841  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008F0849  44 8D 4A 11                     lea r9d, [rdx + 0x11]
008F084D  44 8D 42 03                     lea r8d, [rdx + 3]
008F0851  E8 7A A2 DC FF                  call 0x1406baad0
008F0856  3D 02 00 00 C0                  cmp eax, 0xc0000002
008F085B  0F 84 92 FC FF FF               je 0x1408f04f3
008F0861  3D 20 01 00 C0                  cmp eax, 0xc0000120
008F0866  0F 84 84 FC FF FF               je 0x1408f04f0
008F086C  85 C0                           test eax, eax
008F086E  0F 45 DF                        cmovne ebx, edi
008F0871  E9 7D FC FF FF                  jmp 0x1408f04f3
008F0876  48 8B C2                        mov rax, rdx
008F0879  48 D1 E8                        shr rax, 1
008F087C  66 39 5C 41 FE                  cmp word ptr [rcx + rax*2 - 2], bx
008F0881  74 0A                           je 0x1408f088d
008F0883  66 39 1C 41                     cmp word ptr [rcx + rax*2], bx
008F0887  0F 85 87 FE FF FF               jne 0x1408f0714
008F088D  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
008F0892  E9 EA FA FF FF                  jmp 0x1408f0381
008F0897  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008F089C  E9 30 FF FF FF                  jmp 0x1408f07d1
008F08A1  85 C0                           test eax, eax
008F08A3  0F 84 F4 F9 FF FF               je 0x1408f029d
008F08A9  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008F08AE  E9 84 FD FF FF                  jmp 0x1408f0637
008F08B3  48 8B C7                        mov rax, rdi
008F08B6  E8 15 A2 DC FF                  call 0x1406baad0
008F08BB  E9 CF F9 FF FF                  jmp 0x1408f028f
008F08C0  41 B9 0B 00 00 00               mov r9d, 0xb
008F08C6  89 5D 30                        mov dword ptr [rbp + 0x30], ebx
008F08C9  48 8D 45 30                     lea rax, [rbp + 0x30]
008F08CD  48 8B CE                        mov rcx, rsi
008F08D0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F08D5  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
008F08DC  48 8B C7                        mov rax, rdi
008F08DF  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008F08E7  45 8D 41 F9                     lea r8d, [r9 - 7]
008F08EB  E8 E0 A1 DC FF                  call 0x1406baad0
008F08F0  3D 02 00 00 C0                  cmp eax, 0xc0000002
008F08F5  0F 84 E4 F9 FF FF               je 0x1408f02df
008F08FB  33 F6                           xor esi, esi
008F08FD  3D 20 01 00 C0                  cmp eax, 0xc0000120
008F0902  0F 85 2E DB 22 00               jne 0x140b1e436
008F0908  8B 5D 30                        mov ebx, dword ptr [rbp + 0x30]
008F090B  E9 D1 F9 FF FF                  jmp 0x1408f02e1
008F0910  66 89 18                        mov word ptr [rax], bx
008F0913  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008F0918  E9 64 FA FF FF                  jmp 0x1408f0381
008F091D  8B 4C 24 74                     mov ecx, dword ptr [rsp + 0x74]
008F0921  D1 E9                           shr ecx, 1
008F0923  3B C8                           cmp ecx, eax
008F0925  0F 82 92 FA FF FF               jb 0x1408f03bd
008F092B  8D 41 01                        lea eax, [rcx + 1]
008F092E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008F0932  E9 86 FA FF FF                  jmp 0x1408f03bd
008F0937  48 8D 45 A0                     lea rax, [rbp - 0x60]
008F093B  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
008F0943  4C 8D 4D A8                     lea r9, [rbp - 0x58]
008F0947  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F094C  4C 8B C6                        mov r8, rsi
008F094F  48 8B D3                        mov rdx, rbx
008F0952  49 8B CE                        mov rcx, r14
008F0955  E8 66 D8 B2 FF                  call 0x14041e1c0
008F095A  45 33 FF                        xor r15d, r15d
008F095D  8B D8                           mov ebx, eax
008F095F  85 C0                           test eax, eax
008F0961  0F 88 B9 FB FF FF               js 0x1408f0520
008F0967  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
008F096B  48 85 DB                        test rbx, rbx
008F096E  0F 84 0F DD 22 00               je 0x140b1e683
008F0974  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
008F0978  48 FF CB                        dec rbx
008F097B  49 83 C7 02                     add r15, 2
008F097F  E9 AB FA FF FF                  jmp 0x1408f042f
008F0984  49 8B C4                        mov rax, r12
008F0987  E8 44 A1 DC FF                  call 0x1406baad0
008F098C  E9 49 FB FF FF                  jmp 0x1408f04da
008F0991  4C 8B E3                        mov r12, rbx
008F0994  E9 40 FE FF FF                  jmp 0x1408f07d9
008F0999  85 C0                           test eax, eax
008F099B  0F 84 38 FE FF FF               je 0x1408f07d9
008F09A1  8B DF                           mov ebx, edi
008F09A3  E9 4B FB FF FF                  jmp 0x1408f04f3
008F09A8  33 D2                           xor edx, edx
008F09AA  49 8B CE                        mov rcx, r14
008F09AD  E8 BE 1E 29 00                  call 0x140b82870
008F09B2  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
008F09B6  B9 00 01 00 00                  mov ecx, 0x100
008F09BB  48 03 D2                        add rdx, rdx
008F09BE  41 B8 50 70 20 20               mov r8d, 0x20207050
008F09C4  E8 27 17 29 00                  call 0x140b820f0
008F09C9  4C 8B F0                        mov r14, rax
008F09CC  48 85 C0                        test rax, rax
008F09CF  0F 85 B9 FC FF FF               jne 0x1408f068e
008F09D5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008F09DA  E9 64 FB FF FF                  jmp 0x1408f0543
008F09DF  45 33 FF                        xor r15d, r15d
008F09E2  E9 22 FC FF FF                  jmp 0x1408f0609
008F09E7  33 D2                           xor edx, edx
008F09E9  48 8B CE                        mov rcx, rsi
008F09EC  E8 7F 1E 29 00                  call 0x140b82870
008F09F1  E9 CC FB FF FF                  jmp 0x1408f05c2
008F09F6  33 D2                           xor edx, edx
008F09F8  49 8B CE                        mov rcx, r14
008F09FB  E8 70 1E 29 00                  call 0x140b82870
008F0A00  E9 C6 FB FF FF                  jmp 0x1408f05cb
008F0A05  33 D2                           xor edx, edx
008F0A07  48 8B C8                        mov rcx, rax
008F0A0A  E8 61 1E 29 00                  call 0x140b82870
008F0A0F  E9 C4 FB FF FF                  jmp 0x1408f05d8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetDeviceInterfaces(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B4;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned __int8 v_stack_m1BE;
    unsigned __int8 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int8 v_stack_m1C8;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p64;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 5350906)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m190 = a2;
    a2 = 0;
    v_stack_m19C = a3;
    a3 = 0;
    v_stack_m138 = 0;
    *(unsigned __int64 *)(a5) = 0;
    v_stack_m1BE = a4;
    v_stack_m168 = a5;
    v_stack_m170 = a6;
    v_stack_m1A8 = 0;
    v_stack_m1B4 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m160 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1BC = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m1A0 = 0;
    v_stack_m130 = v_xmm0;
    result = PnpStringFromGuid(a1, v_stack_m98, a3, a4);
    if (sign_flag) goto loc_008F09DF;
    a1 = (a1) | (-1);
    result = ExAcquireResourceExclusiveLite(v_rip + 6931441, 1, a3, a4);
    a2 = 0;
    result = memset(v_stack_mF8, a2, 0 + 88, a4);
    v_rbx = 0;
    v_stack_mD8 = v_stack_m178;
    v_stack_mE8 = 64;
    v_stack_mE0 = 0xF003FULL;
    v_stack_mDC = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5726588) + 504) == 0) goto loc_008F029D;
    v_stack_m200 = v_stack_mF8;
    v_stack_m208 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5726588) + 504)) != (v_rip - 4411)) goto loc_008F08B3;
    result = PiPnpRtlCmActionCallback(*(unsigned __int64 *)(v_rip + 5726588), v_stack_m98, (unsigned int)((unsigned int)(v_rbx + 4)), (unsigned int)((unsigned int)(v_rbx + 11)));
loc_008F028F:
    if (((unsigned int)(result)) != 0xC0000002ULL) goto loc_008F0697;
loc_008F029D:
    v_stack_m1F0 = v_stack_mD0;
    v_stack_m1F8 = v_stack_mD8;
    v_stack_m200 = (unsigned __int8)(v_stack_mDC);
    v_stack_m208 = (unsigned int)((unsigned int)(v_stack_mE0));
    result = _CmOpenCommonClassRegKeyWorker(*(unsigned __int64 *)(v_rip + 5726588), v_stack_m98, (unsigned int)(v_stack_mE8), (unsigned int)(v_stack_mE4));
    if (0 != 0) goto loc_008F08C0;
loc_008F02DF:
    v_rsi = 0;
loc_008F02E1:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000034ULL) goto loc_008F0640;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000003AULL) goto loc_008F0640;
    if (sign_flag) goto loc_008F0637;
    v_stack_m1D8 = 0;
    v_stack_m1E0 = v_stack_m1B4;
    v_stack_m1E8 = v_stack_m1A8;
    v_stack_m1F0 = v_stack_m1BC;
    v_stack_m1F8 = v_rip - 9293816;
    v_stack_m200 = 0;
    v_stack_m208 = v_stack_m178;
    result = PnpGetObjectProperty((unsigned int)(0x47706E50ULL), (unsigned int)(0x400ULL), v_stack_m98, 4);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_008F0621;
loc_008F0372:
    v_rbx = 0;
    if (0 != 0) goto loc_008F06AA;
loc_008F0381:
    result = 0;
    v_stack_m138 = 0;
    v_stack_m158 = v_xmm0;
    if (0 != 0) { result = v_stack_m1A8; }
    v_stack_m158 = result;
    v_stack_m148 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m150, (unsigned int)(0x400ULL), v_stack_m98, 4);
    v_stack_m1C4 = (unsigned int)((unsigned int)(0x1000ULL));
    if (0 != 0) goto loc_008F091D;
loc_008F03BD:
loc_008F03CA:
    v_stack_m1B4 = 0;
    if (((unsigned int)((unsigned int)(0xC0000023ULL))) != 0xC0000023ULL) goto loc_008F0519;
    if (0 >= 5) goto loc_008F0519;
    result = (unsigned int)(0x1000ULL);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m98, 4);
        result = v_stack_m1C4;
    }
    a2 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20207050ULL), 4);
    if (result == 0) goto loc_008F0514;
    v_stack_m1A0 = (unsigned int)((unsigned int)(v_stack_m1C4));
    if (0 != 0) goto loc_008F0937;
loc_008F042F:
    a2 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4)));
    v_stack_m180 = result;
    result = memset(v_stack_mF8, a2, a2 + 88, 4);
    v_stack_mE8 = v_stack_m98;
    v_stack_mE0 = v_stack_m1B0;
    result = (unsigned int)(~((unsigned int)(v_stack_m19C)));
    v_stack_mB8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C4))));
    result = (unsigned int)((result) & (1));
    v_stack_mC0 = result;
    v_stack_mD8 = (unsigned int)(result);
    v_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_mD0 = v_rip - 45177;
    v_stack_mC8 = v_stack_m158;
    v_stack_mB0 = v_stack_m1C4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5726050) + 504) == 0) goto loc_008F07D9;
    a2 = 0;
    v_stack_m200 = v_stack_mF8;
    v_stack_m208 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5726050) + 504)) != (v_rip - 5022)) goto loc_008F0984;
    result = PiPnpRtlCmActionCallback(*(unsigned __int64 *)(v_rip + 5726050), a2, v_rbx + 3, v_rbx + 17);
loc_008F04DA:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008F0991;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008F0999;
loc_008F04F0:
loc_008F04F3:
    v_r15 = (result) - (result);
    v_r15 = (v_r15) >> (1);
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) + ((unsigned int)(v_r15)));
    v_stack_m1C4 = (unsigned int)(result);
    a1 = (unsigned int)(((unsigned int)(v_stack_m1B4)) + 1);
    goto loc_008F03CA;
loc_008F0514:
loc_008F0519:
    v_r15 = 0;
loc_008F0520:
    result = SeReleaseSubjectContext(v_stack_m150, a2, v_rbx + 3, v_rbx + 17);
    if (sign_flag) goto loc_008F0543;
    if (v_stack_m1C4 == 0) goto loc_008F067C;
loc_008F0538:
    if (v_stack_m1BE == 0) goto loc_008F075B;
loc_008F0543:
loc_008F054C:
    result = ExReleaseResourceLite(v_rip + 6930605, a2, v_rbx + 3, v_rbx + 17);
    result = KeLeaveCriticalRegion(v_rip + 6930605, a2, v_rbx + 3, v_rbx + 17);
    if (sign_flag) goto loc_008F0605;
    *(unsigned __int64 *)(v_stack_m168) = result;
    result = v_stack_m168;
    if (v_stack_m170 != 0) {
        result = v_stack_m1C4;
        result = (unsigned int)((result) + ((unsigned int)(result)));
        *(unsigned int *)(v_stack_m170) = (unsigned int)(result);
    }
loc_008F0580:
    if (v_stack_m178 != 0) {
        result = ZwClose(v_stack_m178, a2, v_rbx + 3, v_rbx + 17);
    }
    if (v_stack_m1B0 == 0) goto loc_008F05B9;
    if (v_stack_m190 == 0) goto loc_008F05B9;
    if ((*(unsigned __int16 *)(v_stack_m190 + 2)) == 0) goto loc_008F05B9;
    if (*(unsigned __int64 *)(v_stack_m190 + 8) == 0) goto loc_008F05B9;
    result = *(unsigned __int64 *)(v_stack_m190 + 8);
    if ((*(unsigned __int64 *)(v_stack_m190 + 8)) != v_stack_m1B0) {
        a2 = 0;
        a1 = v_stack_m1B0;
        result = ExFreePoolWithTag(a1, a2, v_rbx + 3, v_rbx + 17);
    }
    if (v_stack_m1A8 != 0) goto loc_008F09E7;
loc_008F05C2:
    if (0 != 0) goto loc_008F09F6;
loc_008F05CB:
    if (v_stack_m160 != 0) goto loc_008F0A05;
loc_008F05D8:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rbx + 3, v_rbx + 17);
    v_rsp = (v_rsp) + (496);
    return result;
loc_008F0605:
loc_008F0609:
    *(unsigned __int64 *)(v_stack_m168) = 0;
    if (v_stack_m170 == 0) goto loc_008F0580;
    *(unsigned int *)(v_stack_m170) = 0;
    goto loc_008F0580;
loc_008F0621:
    if (((unsigned int)(v_stack_m168)) == 0xC0000034ULL) goto loc_008F0372;
    if (((unsigned int)(v_stack_m168)) == 0xC000003AULL) goto loc_008F0372;
loc_008F0637:
    goto loc_008F07D1;
loc_008F0640:
    v_stack_p64 = 1;
    result = ExAllocatePool2(256, 2, (unsigned int)(0x20207050ULL), v_rbx + 17);
    v_r15 = 0;
    if (result == 0) goto loc_008F079F;
    *(unsigned __int16 *)(result) = 0;
    goto loc_008F054C;
loc_008F067C:
    v_stack_p64 = 1;
    if (((unsigned int)(v_stack_m190)) < 1) goto loc_008F09A8;
loc_008F068E:
    *(unsigned __int16 *)(result) = 0;
    goto loc_008F0538;
loc_008F0697:
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008F08A1;
    goto loc_008F02DF;
loc_008F06AA:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190 + 2))) < 2) goto loc_008F0751;
    if (*(unsigned __int64 *)(v_stack_m190 + 8) == 0) goto loc_008F0751;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190))) > ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190 + 2)))) goto loc_008F0897;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190)) == 0) goto loc_008F07A9;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m190 + 8))) == ((unsigned __int16)((unsigned int)(v_stack_mF8)))) goto loc_008F088D;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190))) != ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m190 + 2)))) goto loc_008F0705;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m190)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m190 + 8) + result * 2 - 2)) == ((unsigned __int16)((unsigned int)(v_stack_mF8)))) goto loc_008F088D;
loc_008F0705:
    result = (*(unsigned __int16 *)(v_stack_m190 + 2)) - (2);
    if ((*(unsigned __int16 *)(v_stack_m190)) <= result) goto loc_008F0876;
loc_008F0714:
    a2 = (*(unsigned __int16 *)(v_stack_m190)) + (2);
    result = ExAllocatePool2(v_stack_m170, a2, (unsigned int)(0x75737050ULL), 2);
    v_rdi = 0;
    if (result == 0) goto loc_008F07CC;
    result = memcpy(result, *(unsigned __int64 *)(v_stack_m190 + 8), *(unsigned __int16 *)(v_stack_m190), 2);
    result = (*(unsigned __int16 *)(v_stack_m190)) >> (1);
    *(unsigned __int16 *)(result + result * 2) = 0;
loc_008F0751:
    v_stack_p78 = result;
    goto loc_008F0381;
loc_008F075B:
loc_008F075E:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_008F0543;
    result = CmValidateDeviceInterfaceName(result, result, *(unsigned __int16 *)(v_stack_m190), 2);
    if (sign_flag) goto loc_008F0543;
    *(unsigned __int64 *)(result) = result;
    result = (result) | (-1);
loc_008F078B:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(result + result * 2)) != 0) goto loc_008F078B;
    v_rdi = (result + result * 2) + (2);
    goto loc_008F075E;
loc_008F079F:
    goto loc_008F054C;
loc_008F07A9:
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)((unsigned int)(0xC000009AULL)))) goto loc_008F088D;
    result = ExAllocatePool2(v_rdi, 2, (unsigned int)(0x75737050ULL), 2);
    if (result != 0) goto loc_008F0910;
loc_008F07CC:
loc_008F07D1:
    v_r15 = 0;
    goto loc_008F054C;
loc_008F07D9:
    v_stack_p48 = (unsigned int)((unsigned int)(v_stack_mA8));
    v_stack_p40 = v_stack_mB0;
    v_stack_p38 = (unsigned int)((unsigned int)(v_stack_mB8));
    v_stack_p30 = v_stack_mC0;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = v_stack_mD0;
    result = CmGetMatchingFilteredDeviceInterfaceListWorker(v_stack_m1B0, v_stack_mE8, v_stack_mE0, (unsigned int)(v_stack_mD8));
    if (v_stack_m190 == 0) goto loc_008F04F3;
    a2 = 0;
    v_stack_mF8 = (unsigned int)(result);
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = guard_dispatch_icall(v_stack_m1B0, a2, a2 + 3, a2 + 17);
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008F04F3;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008F04F0;
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((unsigned int)(result) != 0) { v_rbx = (unsigned int)(v_rdi); }
    goto loc_008F04F3;
loc_008F0876:
    result = (0) >> (1);
    if ((*(unsigned __int16 *)(v_stack_m1B0 + result * 2 - 2)) == ((unsigned __int16)(v_rbx))) goto loc_008F088D;
    if ((*(unsigned __int16 *)(v_stack_m1B0 + result * 2)) != ((unsigned __int16)(v_rbx))) goto loc_008F0714;
loc_008F088D:
    v_stack_p78 = v_stack_m1B0;
    goto loc_008F0381;
loc_008F0897:
    goto loc_008F07D1;
loc_008F08A1:
    if ((unsigned int)(result) == 0) goto loc_008F029D;
    goto loc_008F0637;
loc_008F08B3:
    result = guard_dispatch_icall(v_stack_m1B0, a2, a2 + 3, a2 + 17);
    goto loc_008F028F;
loc_008F08C0:
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC00000E5ULL));
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = guard_dispatch_icall(v_stack_m1A8, v_stack_m98, 11 - 7, 11);
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008F02DF;
    v_rsi = 0;
    goto loc_008F02E1;
loc_008F0910:
    *(unsigned __int16 *)(result) = (unsigned __int16)((unsigned int)(v_stack_mF8));
    v_stack_p78 = result;
    goto loc_008F0381;
loc_008F091D:
    a1 = (unsigned int)(((unsigned int)(v_stack_p74)) >> (1));
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_008F03BD;
    v_stack_p64 = (unsigned int)(a1 + 1);
    goto loc_008F03BD;
loc_008F0937:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m188;
    result = RtlStringCchCopyExW(result, (unsigned int)(v_stack_mF8), 0, v_stack_m180);
    v_r15 = 0;
    if (sign_flag) goto loc_008F0520;
    v_rbx = (v_stack_m188) - 1;
    v_r15 = (v_stack_m180) + (2);
    goto loc_008F042F;
loc_008F0984:
    result = guard_dispatch_icall(result, (unsigned int)(v_stack_mF8), 0, v_stack_m180);
    goto loc_008F04DA;
loc_008F0991:
    goto loc_008F07D9;
loc_008F0999:
    if ((unsigned int)(result) == 0) goto loc_008F07D9;
    goto loc_008F04F3;
loc_008F09A8:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, v_stack_m180);
    a2 = ((unsigned int)(v_stack_p64)) + ((unsigned int)(v_stack_p64));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20207050ULL), v_stack_m180);
    if (result != 0) goto loc_008F068E;
    goto loc_008F0543;
loc_008F09DF:
    v_r15 = 0;
    goto loc_008F0609;
loc_008F09E7:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x20207050ULL), v_stack_m180);
    goto loc_008F05C2;
loc_008F09F6:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20207050ULL), v_stack_m180);
    goto loc_008F05CB;
loc_008F0A05:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20207050ULL), v_stack_m180);
    goto loc_008F05D8;
}
```

## 5. (Beta) C Style

```c
int64_t IopGetDeviceInterfaces(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B4;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint8_t v_stack_m1BE;
    uint8_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint8_t v_stack_m1C8;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint8_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p64;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0x51A5FA)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m190 = Arg2;
    Arg2 = 0;
    v_stack_m19C = Arg3;
    Arg3 = 0;
    v_stack_m138 = 0;
    *(uint64_t *)(arg5) = 0;
    v_stack_m1BE = Arg4;
    v_stack_m168 = Arg5;
    v_stack_m170 = Arg6;
    v_stack_m1A8 = 0;
    v_stack_m1B4 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m198 = 0;
    v_stack_m160 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1BC = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m1A0 = 0;
    v_stack_m130 = v_xmm0;
    result = PnpStringFromGuid(Arg1, v_stack_m98, Arg3, Arg4);
    if (sign_flag) goto loc_008F09DF;
    Arg1 = (Arg1) | (-1);
    result = ExAcquireResourceExclusiveLite(v_rip + 6931441, 1, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 0 + 88, Arg4);
    local_rbx = 0;
    v_stack_mD8 = v_stack_m178;
    v_stack_mE8 = 64;
    v_stack_mE0 = 0xF003FULL;
    v_stack_mDC = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x57617C) + 0x1F8) == 0) goto loc_008F029D;
    v_stack_m200 = v_stack_mF8;
    v_stack_m208 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x57617C) + 0x1F8)) != (v_rip - 4411)) goto loc_008F08B3;
    result = PiPnpRtlCmActionCallback(*(uint64_t *)(v_rip + 0x57617C), v_stack_m98, (uint32_t)((uint32_t)(local_rbx + 4)), (uint32_t)((uint32_t)(local_rbx + 11)));
loc_008F028F:
    if (((uint32_t)(result)) != 0xC0000002ULL) goto loc_008F0697;
loc_008F029D:
    v_stack_m1F0 = v_stack_mD0;
    v_stack_m1F8 = v_stack_mD8;
    v_stack_m200 = (uint8_t)(v_stack_mDC);
    v_stack_m208 = (uint32_t)((uint32_t)(v_stack_mE0));
    result = _CmOpenCommonClassRegKeyWorker(*(uint64_t *)(v_rip + 0x57617C), v_stack_m98, (uint32_t)(v_stack_mE8), (uint32_t)(v_stack_mE4));
    if (0 != 0) goto loc_008F08C0;
loc_008F02DF:
    local_rsi = 0;
loc_008F02E1:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000034ULL) goto loc_008F0640;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000003AULL) goto loc_008F0640;
    if (sign_flag) goto loc_008F0637;
    v_stack_m1D8 = 0;
    v_stack_m1E0 = v_stack_m1B4;
    v_stack_m1E8 = v_stack_m1A8;
    v_stack_m1F0 = v_stack_m1BC;
    v_stack_m1F8 = v_rip - 9293816;
    v_stack_m200 = 0;
    v_stack_m208 = v_stack_m178;
    result = PnpGetObjectProperty((uint32_t)(0x47706E50ULL), (uint32_t)(0x400ULL), v_stack_m98, 4);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_008F0621;
loc_008F0372:
    local_rbx = 0;
    if (0 != 0) goto loc_008F06AA;
loc_008F0381:
    result = 0;
    v_stack_m138 = 0;
    v_stack_m158 = v_xmm0;
    if (0 != 0) { result = v_stack_m1A8; }
    v_stack_m158 = result;
    v_stack_m148 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m150, (uint32_t)(0x400ULL), v_stack_m98, 4);
    v_stack_m1C4 = (uint32_t)((uint32_t)(0x1000ULL));
    if (0 != 0) goto loc_008F091D;
loc_008F03BD:
loc_008F03CA:
    v_stack_m1B4 = 0;
    if (((uint32_t)((uint32_t)(0xC0000023ULL))) != 0xC0000023ULL) goto loc_008F0519;
    if (0 >= 5) goto loc_008F0519;
    result = (uint32_t)(0x1000ULL);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m98, 4);
        result = v_stack_m1C4;
    }
    Arg2 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20207050ULL), 4);
    if (result == 0) goto loc_008F0514;
    v_stack_m1A0 = (uint32_t)((uint32_t)(v_stack_m1C4));
    if (0 != 0) goto loc_008F0937;
loc_008F042F:
    Arg2 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4)));
    v_stack_m180 = result;
    result = memset(v_stack_mF8, Arg2, Arg2 + 88, 4);
    v_stack_mE8 = v_stack_m98;
    v_stack_mE0 = v_stack_m1B0;
    result = (uint32_t)(~((uint32_t)(v_stack_m19C)));
    v_stack_mB8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C4))));
    result = (uint32_t)((result) & (1));
    v_stack_mC0 = result;
    v_stack_mD8 = (uint32_t)(result);
    local_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_mD0 = v_rip - 45177;
    v_stack_mC8 = v_stack_m158;
    v_stack_mB0 = v_stack_m1C4;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x575F62) + 0x1F8) == 0) goto loc_008F07D9;
    Arg2 = 0;
    v_stack_m200 = v_stack_mF8;
    v_stack_m208 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x575F62) + 0x1F8)) != (v_rip - 5022)) goto loc_008F0984;
    result = PiPnpRtlCmActionCallback(*(uint64_t *)(v_rip + 0x575F62), Arg2, local_rbx + 3, local_rbx + 17);
loc_008F04DA:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008F0991;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008F0999;
loc_008F04F0:
loc_008F04F3:
    local_r15 = (result) - (result);
    local_r15 = (local_r15) >> (1);
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) + ((uint32_t)(local_r15)));
    v_stack_m1C4 = (uint32_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m1B4)) + 1);
    goto loc_008F03CA;
loc_008F0514:
loc_008F0519:
    local_r15 = 0;
loc_008F0520:
    result = SeReleaseSubjectContext(v_stack_m150, Arg2, local_rbx + 3, local_rbx + 17);
    if (sign_flag) goto loc_008F0543;
    if (v_stack_m1C4 == 0) goto loc_008F067C;
loc_008F0538:
    if (v_stack_m1BE == 0) goto loc_008F075B;
loc_008F0543:
loc_008F054C:
    result = ExReleaseResourceLite(v_rip + 6930605, Arg2, local_rbx + 3, local_rbx + 17);
    result = KeLeaveCriticalRegion(v_rip + 6930605, Arg2, local_rbx + 3, local_rbx + 17);
    if (sign_flag) goto loc_008F0605;
    *(uint64_t *)(v_stack_m168) = result;
    result = v_stack_m168;
    if (v_stack_m170 != 0) {
        result = v_stack_m1C4;
        result = (uint32_t)((result) + ((uint32_t)(result)));
        *(uint32_t *)(v_stack_m170) = (uint32_t)(result);
    }
loc_008F0580:
    if (v_stack_m178 != 0) {
        result = ZwClose(v_stack_m178, Arg2, local_rbx + 3, local_rbx + 17);
    }
    if (v_stack_m1B0 == 0) goto loc_008F05B9;
    if (v_stack_m190 == 0) goto loc_008F05B9;
    if ((*(uint16_t *)(v_stack_m190 + 0x2)) == 0) goto loc_008F05B9;
    if (*(uint64_t *)(v_stack_m190 + 0x8) == 0) goto loc_008F05B9;
    result = *(uint64_t *)(v_stack_m190 + 0x8);
    if ((*(uint64_t *)(v_stack_m190 + 0x8)) != v_stack_m1B0) {
        Arg2 = 0;
        Arg1 = v_stack_m1B0;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rbx + 3, local_rbx + 17);
    }
    if (v_stack_m1A8 != 0) goto loc_008F09E7;
loc_008F05C2:
    if (0 != 0) goto loc_008F09F6;
loc_008F05CB:
    if (v_stack_m160 != 0) goto loc_008F0A05;
loc_008F05D8:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, local_rbx + 3, local_rbx + 17);
    local_rsp = (local_rsp) + (496);
    return result;
loc_008F0605:
loc_008F0609:
    *(uint64_t *)(v_stack_m168) = 0;
    if (v_stack_m170 == 0) goto loc_008F0580;
    *(uint32_t *)(v_stack_m170) = 0;
    goto loc_008F0580;
loc_008F0621:
    if (((uint32_t)(v_stack_m168)) == 0xC0000034ULL) goto loc_008F0372;
    if (((uint32_t)(v_stack_m168)) == 0xC000003AULL) goto loc_008F0372;
loc_008F0637:
    goto loc_008F07D1;
loc_008F0640:
    v_stack_p64 = 1;
    result = ExAllocatePool2(256, 2, (uint32_t)(0x20207050ULL), local_rbx + 17);
    local_r15 = 0;
    if (result == 0) goto loc_008F079F;
    *(uint16_t *)(result) = 0;
    goto loc_008F054C;
loc_008F067C:
    v_stack_p64 = 1;
    if (((uint32_t)(v_stack_m190)) < 1) goto loc_008F09A8;
loc_008F068E:
    *(uint16_t *)(result) = 0;
    goto loc_008F0538;
loc_008F0697:
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008F08A1;
    goto loc_008F02DF;
loc_008F06AA:
    if (((uint16_t)(*(uint16_t *)(v_stack_m190 + 0x2))) < 2) goto loc_008F0751;
    if (*(uint64_t *)(v_stack_m190 + 0x8) == 0) goto loc_008F0751;
    if (((uint16_t)(*(uint16_t *)(v_stack_m190))) > ((uint16_t)(*(uint16_t *)(v_stack_m190 + 0x2)))) goto loc_008F0897;
    if ((uint16_t)(*(uint16_t *)(v_stack_m190)) == 0) goto loc_008F07A9;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m190 + 0x8))) == ((uint16_t)((uint32_t)(v_stack_mF8)))) goto loc_008F088D;
    if (((uint16_t)(*(uint16_t *)(v_stack_m190))) != ((uint16_t)(*(uint16_t *)(v_stack_m190 + 0x2)))) goto loc_008F0705;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m190)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m190 + 0x8) + result * 2 - 0x2)) == ((uint16_t)((uint32_t)(v_stack_mF8)))) goto loc_008F088D;
loc_008F0705:
    result = (*(uint16_t *)(v_stack_m190 + 0x2)) - (2);
    if ((*(uint16_t *)(v_stack_m190)) <= result) goto loc_008F0876;
loc_008F0714:
    Arg2 = (*(uint16_t *)(v_stack_m190)) + (2);
    result = ExAllocatePool2(v_stack_m170, Arg2, (uint32_t)(0x75737050ULL), 2);
    local_rdi = 0;
    if (result == 0) goto loc_008F07CC;
    result = memcpy(result, *(uint64_t *)(v_stack_m190 + 0x8), *(uint16_t *)(v_stack_m190), 2);
    result = (*(uint16_t *)(v_stack_m190)) >> (1);
    *(uint16_t *)(result + result * 2) = 0;
loc_008F0751:
    v_stack_p78 = result;
    goto loc_008F0381;
loc_008F075B:
loc_008F075E:
    if ((*(uint16_t *)(result)) == 0) goto loc_008F0543;
    result = CmValidateDeviceInterfaceName(result, result, *(uint16_t *)(v_stack_m190), 2);
    if (sign_flag) goto loc_008F0543;
    *(uint64_t *)(result) = result;
    result = (result) | (-1);
loc_008F078B:
    result = (result) + 1;
    if ((*(uint16_t *)(result + result * 2)) != 0) goto loc_008F078B;
    local_rdi = (result + result * 2) + (2);
    goto loc_008F075E;
loc_008F079F:
    goto loc_008F054C;
loc_008F07A9:
    if ((*(uint16_t *)(result)) == ((uint16_t)((uint32_t)(0xC000009AULL)))) goto loc_008F088D;
    result = ExAllocatePool2(local_rdi, 2, (uint32_t)(0x75737050ULL), 2);
    if (result != 0) goto loc_008F0910;
loc_008F07CC:
loc_008F07D1:
    local_r15 = 0;
    goto loc_008F054C;
loc_008F07D9:
    v_stack_p48 = (uint32_t)((uint32_t)(v_stack_mA8));
    v_stack_p40 = v_stack_mB0;
    v_stack_p38 = (uint32_t)((uint32_t)(v_stack_mB8));
    v_stack_p30 = v_stack_mC0;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = v_stack_mD0;
    result = CmGetMatchingFilteredDeviceInterfaceListWorker(v_stack_m1B0, v_stack_mE8, v_stack_mE0, (uint32_t)(v_stack_mD8));
    if (v_stack_m190 == 0) goto loc_008F04F3;
    Arg2 = 0;
    v_stack_mF8 = (uint32_t)(result);
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = guard_dispatch_icall(v_stack_m1B0, Arg2, Arg2 + 3, Arg2 + 17);
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008F04F3;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008F04F0;
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((uint32_t)(result) != 0) { local_rbx = (uint32_t)(local_rdi); }
    goto loc_008F04F3;
loc_008F0876:
    result = (0) >> (1);
    if ((*(uint16_t *)(v_stack_m1B0 + result * 2 - 0x2)) == ((uint16_t)(local_rbx))) goto loc_008F088D;
    if ((*(uint16_t *)(v_stack_m1B0 + result * 2)) != ((uint16_t)(local_rbx))) goto loc_008F0714;
loc_008F088D:
    v_stack_p78 = v_stack_m1B0;
    goto loc_008F0381;
loc_008F0897:
    goto loc_008F07D1;
loc_008F08A1:
    if ((uint32_t)(result) == 0) goto loc_008F029D;
    goto loc_008F0637;
loc_008F08B3:
    result = guard_dispatch_icall(v_stack_m1B0, Arg2, Arg2 + 3, Arg2 + 17);
    goto loc_008F028F;
loc_008F08C0:
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC00000E5ULL));
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = guard_dispatch_icall(v_stack_m1A8, v_stack_m98, 11 - 7, 11);
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008F02DF;
    local_rsi = 0;
    goto loc_008F02E1;
loc_008F0910:
    *(uint16_t *)(result) = (uint16_t)((uint32_t)(v_stack_mF8));
    v_stack_p78 = result;
    goto loc_008F0381;
loc_008F091D:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p74)) >> (1));
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_008F03BD;
    v_stack_p64 = (uint32_t)(Arg1 + 1);
    goto loc_008F03BD;
loc_008F0937:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m188;
    result = RtlStringCchCopyExW(result, (uint32_t)(v_stack_mF8), 0, v_stack_m180);
    local_r15 = 0;
    if (sign_flag) goto loc_008F0520;
    local_rbx = (v_stack_m188) - 1;
    local_r15 = (v_stack_m180) + (2);
    goto loc_008F042F;
loc_008F0984:
    result = guard_dispatch_icall(result, (uint32_t)(v_stack_mF8), 0, v_stack_m180);
    goto loc_008F04DA;
loc_008F0991:
    goto loc_008F07D9;
loc_008F0999:
    if ((uint32_t)(result) == 0) goto loc_008F07D9;
    goto loc_008F04F3;
loc_008F09A8:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, v_stack_m180);
    Arg2 = ((uint32_t)(v_stack_p64)) + ((uint32_t)(v_stack_p64));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20207050ULL), v_stack_m180);
    if (result != 0) goto loc_008F068E;
    goto loc_008F0543;
loc_008F09DF:
    local_r15 = 0;
    goto loc_008F0609;
loc_008F09E7:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x20207050ULL), v_stack_m180);
    goto loc_008F05C2;
loc_008F09F6:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20207050ULL), v_stack_m180);
    goto loc_008F05CB;
loc_008F0A05:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20207050ULL), v_stack_m180);
    goto loc_008F05D8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F0120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
