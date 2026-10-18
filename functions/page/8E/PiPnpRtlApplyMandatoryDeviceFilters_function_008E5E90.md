# PiPnpRtlApplyMandatoryDeviceFilters

- RVA: `0x008E5E90`–`0x008E6451` (길이 `1,473` bytes)
- VA: `0x00000001408E5E90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000866F8`
- 디코드: `355`개 명령, `1,473/1,473` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008E5EFA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008E5F07` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008E5F15` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008E5F83` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E5F96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008E6039` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E607B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E60A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E60B9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008E60D6` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (function, `0x00225150`)
- `0x008E60F6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008E6100` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x008E6196` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E61F5` → [PiAuVerifyAccessToObject](../9E/PiAuVerifyAccessToObject_function_009E92D0.md) (function, `0x009E92D0`)
- `0x008E625C` → [PnpGetObjectPropertyWorker](PnpGetObjectPropertyWorker_function_008E1810.md) (function, `0x008E1810`)
- `0x008E62A1` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E6322` → [PnpGetObjectPropertyWorker](PnpGetObjectPropertyWorker_function_008E1810.md) (function, `0x008E1810`)
- `0x008E6366` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E63F9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E6406` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E6413` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E6420` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E6445` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiPnpRtlApplyMandatoryDeviceInterfaceFilters](PiPnpRtlApplyMandatoryDeviceInterfaceFilters_function_008E59D0.md) at `0x008E5B30`
- [PiPnpRtlApplyMandatoryFilters](PiPnpRtlApplyMandatoryFilters_function_008E5C80.md) at `0x008E5DA6`
- [PiCMMandatoryFilterCallback](PiCMMandatoryFilterCallback_function_008E6490.md) at `0x008E6575`
- [sub_008E6883](Unknown_function_008E6883.md) at `0x008E69B0`
- [PiCMValidateDeviceInstance](PiCMValidateDeviceInstance_function_008E799C.md) at `0x008E7BB8`
- [PiPnpRtlApplyMandatoryDeviceContainerFiltersCallback](../A7/PiPnpRtlApplyMandatoryDeviceContainerFiltersCallback_function_00A76760.md) at `0x00A76787`

### Static image references
- `0x008E5EA9` → RVA `0x00E0A740` (`.data`; read)
- `0x008E5F67` → RVA `0x00011478` (`.rdata`; read)
- `0x008E5FB0` → RVA `0x00E66398` (`.data`; read)
- `0x008E600B` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)
- `0x008E611A` → RVA `0x00011460` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x008E5EFA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008E5F07` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008E5F15` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008E5F83` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E5F96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008E607B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E60A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E60B9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008E60D6` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (`PAGE` → `.text`)
  - `0x008E60F6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008E6100` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x008E63F9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E6406` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E6413` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E6420` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E6445` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E5E90  40 55                           push rbp
008E5E92  53                              push rbx
008E5E93  56                              push rsi
008E5E94  57                              push rdi
008E5E95  41 54                           push r12
008E5E97  41 55                           push r13
008E5E99  41 56                           push r14
008E5E9B  41 57                           push r15
008E5E9D  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
008E5EA2  48 81 EC F8 00 00 00            sub rsp, 0xf8
008E5EA9  48 8B 05 90 48 52 00            mov rax, qword ptr [rip + 0x524890]
008E5EB0  48 33 C4                        xor rax, rsp
008E5EB3  48 89 45 FF                     mov qword ptr [rbp - 1], rax
008E5EB7  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
008E5EBB  33 FF                           xor edi, edi
008E5EBD  4D 8B F9                        mov r15, r9
008E5EC0  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
008E5EC4  4C 8B E2                        mov r12, rdx
008E5EC7  89 7D 83                        mov dword ptr [rbp - 0x7d], edi
008E5ECA  4C 8B E9                        mov r13, rcx
008E5ECD  89 7D 87                        mov dword ptr [rbp - 0x79], edi
008E5ED0  40 88 3E                        mov byte ptr [rsi], dil
008E5ED3  49 8B 19                        mov rbx, qword ptr [r9]
008E5ED6  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
008E5EDA  48 85 DB                        test rbx, rbx
008E5EDD  75 04                           jne 0x1408e5ee3
008E5EDF  49 8B 59 10                     mov rbx, qword ptr [r9 + 0x10]
008E5EE3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E5EEC  B2 01                           mov dl, 1
008E5EEE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008E5EF5  90                              nop
008E5EF6  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
008E5EFA  E8 C1 BC 92 FF                  call 0x140211bc0
008E5EFF  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
008E5F03  44 8B 73 78                     mov r14d, dword ptr [rbx + 0x78]
008E5F07  E8 04 9B 97 FF                  call 0x14025fa10
008E5F0C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008E5F15  E8 D6 90 97 FF                  call 0x14025eff0
008E5F1A  45 85 F6                        test r14d, r14d
008E5F1D  0F 85 B0 01 00 00               jne 0x1408e60d3
008E5F23  8B DF                           mov ebx, edi
008E5F25  C6 06 01                        mov byte ptr [rsi], 1
008E5F28  33 C9                           xor ecx, ecx
008E5F2A  80 3E 00                        cmp byte ptr [rsi], 0
008E5F2D  0F 84 7D 01 00 00               je 0x1408e60b0
008E5F33  B8 00 02 00 00                  mov eax, 0x200
008E5F38  89 4D 83                        mov dword ptr [rbp - 0x7d], ecx
008E5F3B  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008E5F3F  44 8B F1                        mov r14d, ecx
008E5F42  C7 45 EF 01 00 02 00            mov dword ptr [rbp - 0x11], 0x20001
008E5F49  48 8B F9                        mov rdi, rcx
008E5F4C  C7 45 F3 00 00 02 00            mov dword ptr [rbp - 0xd], 0x20000
008E5F53  4D 8B EC                        mov r13, r12
008E5F56  C7 45 F7 00 00 02 00            mov dword ptr [rbp - 9], 0x20000
008E5F5D  C7 45 FB 01 00 0F 00            mov dword ptr [rbp - 5], 0xf0001
008E5F64  C6 06 00                        mov byte ptr [rsi], 0
008E5F67  48 8D 15 0A B5 72 FF            lea rdx, [rip - 0x8d4af6]
008E5F6E  41 3B C6                        cmp eax, r14d
008E5F71  76 3D                           jbe 0x1408e5fb0
008E5F73  44 8B F0                        mov r14d, eax
008E5F76  48 85 FF                        test rdi, rdi
008E5F79  74 0D                           je 0x1408e5f88
008E5F7B  BA 50 6E 70 47                  mov edx, 0x47706e50
008E5F80  48 8B CF                        mov rcx, rdi
008E5F83  E8 E8 C8 29 00                  call 0x140b82870
008E5F88  49 8B D6                        mov rdx, r14
008E5F8B  B9 00 01 00 00                  mov ecx, 0x100
008E5F90  41 B8 50 6E 70 47               mov r8d, 0x47706e50
008E5F96  E8 55 C1 29 00                  call 0x140b820f0
008E5F9B  48 8B F8                        mov rdi, rax
008E5F9E  48 85 C0                        test rax, rax
008E5FA1  0F 84 83 04 00 00               je 0x1408e642a
008E5FA7  33 C9                           xor ecx, ecx
008E5FA9  48 8D 15 C8 B4 72 FF            lea rdx, [rip - 0x8d4b38]
008E5FB0  48 8B 1D E1 03 58 00            mov rbx, qword ptr [rip + 0x5803e1]
008E5FB7  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
008E5FBB  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
008E5FBF  48 8D 45 83                     lea rax, [rbp - 0x7d]
008E5FC3  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
008E5FC7  4C 8B A3 E8 01 00 00            mov r12, qword ptr [rbx + 0x1e8]
008E5FCE  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
008E5FD2  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008E5FD7  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008E5FDB  48 89 5D 87                     mov qword ptr [rbp - 0x79], rbx
008E5FDF  48 89 4D 8F                     mov qword ptr [rbp - 0x71], rcx
008E5FE3  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
008E5FE7  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
008E5FEA  48 C7 45 D7 00 00 00 00         mov qword ptr [rbp - 0x29], 0
008E5FF2  48 89 4D A7                     mov qword ptr [rbp - 0x59], rcx
008E5FF6  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
008E5FFA  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
008E5FFE  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
008E6002  4D 85 E4                        test r12, r12
008E6005  0F 84 06 02 00 00               je 0x1408e6211
008E600B  48 8D 05 3E C8 FF FF            lea rax, [rip - 0x37c2]
008E6012  41 B9 08 00 00 00               mov r9d, 8
008E6018  4C 3B E0                        cmp r12, rax
008E601B  49 8B D5                        mov rdx, r13
008E601E  48 8D 45 8F                     lea rax, [rbp - 0x71]
008E6022  48 8B CB                        mov rcx, rbx
008E6025  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E602A  45 8D 41 F9                     lea r8d, [r9 - 7]
008E602E  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
008E6033  0F 85 D7 03 00 00               jne 0x1408e6410
008E6039  E8 12 C8 FF FF                  call 0x1408e2850
008E603E  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E6043  0F 84 6D 03 00 00               je 0x1408e63b6
008E6049  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E604E  0F 85 B5 01 00 00               jne 0x1408e6209
008E6054  8B 5D 8F                        mov ebx, dword ptr [rbp - 0x71]
008E6057  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008E605D  0F 84 63 03 00 00               je 0x1408e63c6
008E6063  44 8B F3                        mov r14d, ebx
008E6066  85 DB                           test ebx, ebx
008E6068  0F 89 5E 01 00 00               jns 0x1408e61cc
008E606E  48 85 FF                        test rdi, rdi
008E6071  74 0F                           je 0x1408e6082
008E6073  BA 50 6E 70 47                  mov edx, 0x47706e50
008E6078  48 8B CF                        mov rcx, rdi
008E607B  E8 F0 C7 29 00                  call 0x140b82870
008E6080  33 FF                           xor edi, edi
008E6082  41 8B DE                        mov ebx, r14d
008E6085  41 81 FE 25 02 00 C0            cmp r14d, 0xc0000225
008E608C  0F 85 01 03 00 00               jne 0x1408e6393
008E6092  33 DB                           xor ebx, ebx
008E6094  C6 06 01                        mov byte ptr [rsi], 1
008E6097  48 85 FF                        test rdi, rdi
008E609A  74 0D                           je 0x1408e60a9
008E609C  BA 50 6E 70 47                  mov edx, 0x47706e50
008E60A1  48 8B CF                        mov rcx, rdi
008E60A4  E8 C7 C7 29 00                  call 0x140b82870
008E60A9  85 DB                           test ebx, ebx
008E60AB  79 03                           jns 0x1408e60b0
008E60AD  C6 06 00                        mov byte ptr [rsi], 0
008E60B0  8B C3                           mov eax, ebx
008E60B2  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
008E60B6  48 33 CC                        xor rcx, rsp
008E60B9  E8 82 65 DC FF                  call 0x1406ac640
008E60BE  48 81 C4 F8 00 00 00            add rsp, 0xf8
008E60C5  41 5F                           pop r15
008E60C7  41 5E                           pop r14
008E60C9  41 5D                           pop r13
008E60CB  41 5C                           pop r12
008E60CD  5F                              pop rdi
008E60CE  5E                              pop rsi
008E60CF  5B                              pop rbx
008E60D0  5D                              pop rbp
008E60D1  C3                              ret
008E60D2  CC                              int3
008E60D3  41 8B CE                        mov ecx, r14d
008E60D6  E8 75 F0 93 FF                  call 0x140225150
008E60DB  48 85 C0                        test rax, rax
008E60DE  74 30                           je 0x1408e6110
008E60E0  48 8B 88 E8 02 00 00            mov rcx, qword ptr [rax + 0x2e8]
008E60E7  BA 50 73 51 79                  mov edx, 0x79517350
008E60EC  48 8B B9 A0 00 00 00            mov rdi, qword ptr [rcx + 0xa0]
008E60F3  48 8B C8                        mov rcx, rax
008E60F6  E8 E5 17 A1 FF                  call 0x1402f78e0
008E60FB  48 8B CF                        mov rcx, rdi
008E60FE  33 DB                           xor ebx, ebx
008E6100  E8 FB 8B B7 FF                  call 0x14045ed00
008E6105  44 3B F0                        cmp r14d, eax
008E6108  0F 84 17 FE FF FF               je 0x1408e5f25
008E610E  33 FF                           xor edi, edi
008E6110  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
008E6114  33 DB                           xor ebx, ebx
008E6116  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
008E611A  48 8D 05 3F B3 72 FF            lea rax, [rip - 0x8d4cc1]
008E6121  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
008E6125  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008E612A  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
008E612E  48 8D 45 83                     lea rax, [rbp - 0x7d]
008E6132  48 89 7D 8F                     mov qword ptr [rbp - 0x71], rdi
008E6136  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
008E613A  49 8B BD E8 01 00 00            mov rdi, qword ptr [r13 + 0x1e8]
008E6141  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
008E6145  48 8D 45 87                     lea rax, [rbp - 0x79]
008E6149  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008E614D  48 C7 45 C7 04 00 00 00         mov qword ptr [rbp - 0x39], 4
008E6155  48 C7 45 D7 00 00 00 00         mov qword ptr [rbp - 0x29], 0
008E615D  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
008E6161  48 85 FF                        test rdi, rdi
008E6164  0F 84 6D 01 00 00               je 0x1408e62d7
008E616A  48 8D 05 DF C6 FF FF            lea rax, [rip - 0x3921]
008E6171  49 8B D4                        mov rdx, r12
008E6174  48 3B F8                        cmp rdi, rax
008E6177  44 8D 43 01                     lea r8d, [rbx + 1]
008E617B  48 8D 45 8F                     lea rax, [rbp - 0x71]
008E617F  49 8B CD                        mov rcx, r13
008E6182  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E6187  44 8D 4B 08                     lea r9d, [rbx + 8]
008E618B  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
008E6190  0F 85 60 02 00 00               jne 0x1408e63f6
008E6196  E8 B5 C6 FF FF                  call 0x1408e2850
008E619B  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E61A0  0F 84 18 02 00 00               je 0x1408e63be
008E61A6  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E61AB  0F 85 1E 01 00 00               jne 0x1408e62cf
008E61B1  8B 5D 8F                        mov ebx, dword ptr [rbp - 0x71]
008E61B4  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
008E61BA  0F 85 E1 01 00 00               jne 0x1408e63a1
008E61C0  33 C9                           xor ecx, ecx
008E61C2  C6 06 01                        mov byte ptr [rsi], 1
008E61C5  8B D9                           mov ebx, ecx
008E61C7  E9 5E FD FF FF                  jmp 0x1408e5f2a
008E61CC  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
008E61D1  0F 84 5D 02 00 00               je 0x1408e6434
008E61D7  83 7D 83 13                     cmp dword ptr [rbp - 0x7d], 0x13
008E61DB  0F 85 B3 FE FF FF               jne 0x1408e6094
008E61E1  4D 8B CF                        mov r9, r15
008E61E4  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008E61E9  4C 8D 45 EF                     lea r8, [rbp - 0x11]
008E61ED  48 8B D7                        mov rdx, rdi
008E61F0  B9 01 00 00 00                  mov ecx, 1
008E61F5  E8 D6 30 10 00                  call 0x1409e92d0
008E61FA  8B D8                           mov ebx, eax
008E61FC  85 C0                           test eax, eax
008E61FE  0F 88 8E FE FF FF               js 0x1408e6092
008E6204  E9 8E FE FF FF                  jmp 0x1408e6097
008E6209  85 C0                           test eax, eax
008E620B  0F 85 B3 00 00 00               jne 0x1408e62c4
008E6211  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
008E6214  41 B8 01 00 00 00               mov r8d, 1
008E621A  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
008E621E  49 8B D5                        mov rdx, r13
008E6221  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008E6225  48 8B CB                        mov rcx, rbx
008E6228  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
008E622C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008E6231  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
008E6234  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008E6238  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008E623C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E6241  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
008E6245  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E624A  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
008E624E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E6253  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
008E6257  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E625C  E8 AF B5 FF FF                  call 0x1408e1810
008E6261  8B D8                           mov ebx, eax
008E6263  4D 85 E4                        test r12, r12
008E6266  0F 84 EB FD FF FF               je 0x1408e6057
008E626C  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
008E6270  41 B9 08 00 00 00               mov r9d, 8
008E6276  89 45 8F                        mov dword ptr [rbp - 0x71], eax
008E6279  49 8B D5                        mov rdx, r13
008E627C  48 8D 05 CD C5 FF FF            lea rax, [rip - 0x3a33]
008E6283  4C 3B E0                        cmp r12, rax
008E6286  48 8D 45 8F                     lea rax, [rbp - 0x71]
008E628A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E628F  45 8D 41 F9                     lea r8d, [r9 - 7]
008E6293  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008E629B  0F 85 7C 01 00 00               jne 0x1408e641d
008E62A1  E8 AA C5 FF FF                  call 0x1408e2850
008E62A6  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E62AB  0F 84 A6 FD FF FF               je 0x1408e6057
008E62B1  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E62B6  0F 84 2A 01 00 00               je 0x1408e63e6
008E62BC  85 C0                           test eax, eax
008E62BE  0F 84 93 FD FF FF               je 0x1408e6057
008E62C4  41 BE E5 00 00 C0               mov r14d, 0xc00000e5
008E62CA  E9 9F FD FF FF                  jmp 0x1408e606e
008E62CF  85 C0                           test eax, eax
008E62D1  0F 85 B2 00 00 00               jne 0x1408e6389
008E62D7  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
008E62DA  41 B8 01 00 00 00               mov r8d, 1
008E62E0  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
008E62E4  49 8B D4                        mov rdx, r12
008E62E7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008E62EB  49 8B CD                        mov rcx, r13
008E62EE  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
008E62F2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008E62F7  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
008E62FA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008E62FE  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008E6302  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E6307  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
008E630B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E6310  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
008E6314  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E6319  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
008E631D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E6322  E8 E9 B4 FF FF                  call 0x1408e1810
008E6327  8B D8                           mov ebx, eax
008E6329  48 85 FF                        test rdi, rdi
008E632C  0F 84 82 FE FF FF               je 0x1408e61b4
008E6332  89 45 8F                        mov dword ptr [rbp - 0x71], eax
008E6335  41 B9 08 00 00 00               mov r9d, 8
008E633B  48 8D 05 0E C5 FF FF            lea rax, [rip - 0x3af2]
008E6342  49 8B D4                        mov rdx, r12
008E6345  48 3B F8                        cmp rdi, rax
008E6348  49 8B CD                        mov rcx, r13
008E634B  48 8D 45 8F                     lea rax, [rbp - 0x71]
008E634F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E6354  45 8D 41 F9                     lea r8d, [r9 - 7]
008E6358  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008E6360  0F 85 9D 00 00 00               jne 0x1408e6403
008E6366  E8 E5 C4 FF FF                  call 0x1408e2850
008E636B  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E6370  0F 84 3E FE FF FF               je 0x1408e61b4
008E6376  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E637B  0F 84 30 FE FF FF               je 0x1408e61b1
008E6381  85 C0                           test eax, eax
008E6383  0F 84 2B FE FF FF               je 0x1408e61b4
008E6389  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008E638E  E9 1A FD FF FF                  jmp 0x1408e60ad
008E6393  45 85 F6                        test r14d, r14d
008E6396  0F 88 FB FC FF FF               js 0x1408e6097
008E639C  E9 36 FE FF FF                  jmp 0x1408e61d7
008E63A1  8B C3                           mov eax, ebx
008E63A3  85 DB                           test ebx, ebx
008E63A5  79 2A                           jns 0x1408e63d1
008E63A7  8B D8                           mov ebx, eax
008E63A9  85 C0                           test eax, eax
008E63AB  0F 89 77 FB FF FF               jns 0x1408e5f28
008E63B1  E9 F7 FC FF FF                  jmp 0x1408e60ad
008E63B6  45 33 E4                        xor r12d, r12d
008E63B9  E9 53 FE FF FF                  jmp 0x1408e6211
008E63BE  48 8B FB                        mov rdi, rbx
008E63C1  E9 11 FF FF FF                  jmp 0x1408e62d7
008E63C6  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008E63CA  33 C9                           xor ecx, ecx
008E63CC  E9 96 FB FF FF                  jmp 0x1408e5f67
008E63D1  83 7C 24 60 07                  cmp dword ptr [rsp + 0x60], 7
008E63D6  75 16                           jne 0x1408e63ee
008E63D8  44 39 75 83                     cmp dword ptr [rbp - 0x7d], r14d
008E63DC  75 C9                           jne 0x1408e63a7
008E63DE  C6 06 01                        mov byte ptr [rsi], 1
008E63E1  E9 42 FB FF FF                  jmp 0x1408e5f28
008E63E6  8B 5D 8F                        mov ebx, dword ptr [rbp - 0x71]
008E63E9  E9 69 FC FF FF                  jmp 0x1408e6057
008E63EE  C6 06 01                        mov byte ptr [rsi], 1
008E63F1  E9 32 FB FF FF                  jmp 0x1408e5f28
008E63F6  48 8B C7                        mov rax, rdi
008E63F9  E8 D2 46 DD FF                  call 0x1406baad0
008E63FE  E9 98 FD FF FF                  jmp 0x1408e619b
008E6403  48 8B C7                        mov rax, rdi
008E6406  E8 C5 46 DD FF                  call 0x1406baad0
008E640B  E9 5B FF FF FF                  jmp 0x1408e636b
008E6410  49 8B C4                        mov rax, r12
008E6413  E8 B8 46 DD FF                  call 0x1406baad0
008E6418  E9 21 FC FF FF                  jmp 0x1408e603e
008E641D  49 8B C4                        mov rax, r12
008E6420  E8 AB 46 DD FF                  call 0x1406baad0
008E6425  E9 7C FE FF FF                  jmp 0x1408e62a6
008E642A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008E642F  E9 75 FC FF FF                  jmp 0x1408e60a9
008E6434  48 85 FF                        test rdi, rdi
008E6437  0F 84 9A FD FF FF               je 0x1408e61d7
008E643D  BA 50 6E 70 47                  mov edx, 0x47706e50
008E6442  48 8B CF                        mov rcx, rdi
008E6445  E8 26 C4 29 00                  call 0x140b82870
008E644A  33 FF                           xor edi, edi
008E644C  E9 86 FD FF FF                  jmp 0x1408e61d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlApplyMandatoryDeviceFilters(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p60;

    v_rsp = (v_rsp) - (248);
    result = (*(unsigned __int64 *)(v_rip + 5392528)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rdi = 0;
    v_stack_m78 = a3;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    *(unsigned __int8 *)(a5) = 0;
    v_stack_mD8 = 0;
    v_rbx = *(unsigned __int64 *)(a4);
    if (*(unsigned __int64 *)(a4) == 0) {
        v_rbx = *(unsigned __int64 *)(a4 + 16);
    }
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_rbx + 48), 1, a3, a4);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rbx + 48), 1, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 120))) != 0) goto loc_008E60D3;
loc_008E5F25:
    *(unsigned __int8 *)(a5) = 1;
loc_008E5F28:
    a1 = 0;
loc_008E5F2A:
    if ((*(unsigned __int8 *)(a5)) == 0) goto loc_008E60B0;
    v_stack_mD4 = 0;
    v_stack_mD8 = 512;
    v_stack_m68 = 0x20001ULL;
    v_stack_m64 = 0x20000ULL;
    v_stack_m60 = 0x20000ULL;
    v_stack_m5C = 0xF0001ULL;
    *(unsigned __int8 *)(a5) = 0;
loc_008E5F67:
    if (512 <= 0) goto loc_008E5FB0;
    result = 512;
    if (0 != 0) {
        a2 = 0x47706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExAllocatePool2(256, 512, (unsigned int)(0x47706E50ULL), a4);
    if (result == 0) goto loc_008E642A;
    a1 = 0;
loc_008E5FB0:
    v_stack_mB8 = v_stack_m78;
    v_stack_mD8 = 0;
    v_stack_mA0 = v_stack_mD4;
    v_stack_m88 = v_stack_mD8;
    v_stack_mD0 = *(unsigned __int64 *)(v_rip + 5768161);
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_m8C = 0;
    v_stack_m80 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = v_rip - 9259832;
    v_stack_m98 = result;
    v_stack_m90 = 512;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488) == 0) goto loc_008E6211;
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = (unsigned int)(8 - 7);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488)) != (v_rip - 14274)) goto loc_008E6410;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rip + 5768161), a2, 8 - 7, 8);
loc_008E603E:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E63B6;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008E6209;
loc_008E6057:
    if (((unsigned int)((unsigned int)(v_stack_mC8))) == 0xC0000023ULL) goto loc_008E63C6;
    if (!sign_flag) goto loc_008E61CC;
loc_008E606E:
    v_rdi = result;
    if (result != 0) {
        a2 = 0x47706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 8 - 7, 8);
        v_rdi = 0;
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC8))))) != 0xC0000225ULL) goto loc_008E6393;
loc_008E6092:
    v_rbx = 0;
loc_008E6094:
    *(unsigned __int8 *)(a5) = 1;
loc_008E6097:
    if (0 != 0) {
        a2 = 0x47706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 8 - 7, 8);
    }
    if (sign_flag) {
        *(unsigned __int8 *)(a5) = 0;
    }
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 8 - 7, 8);
    v_rsp = (v_rsp) + (248);
    return result;
loc_008E60D3:
    result = PsGetSessionById((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC8))))), a2, 8 - 7, 8);
    if (result == 0) goto loc_008E6110;
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x79517350ULL), 8 - 7, 8);
    v_rbx = 0;
    result = PsGetServerSiloServiceSessionId(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 744) + 160), (unsigned int)(0x79517350ULL), 8 - 7, 8);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC8))))) == ((unsigned int)(result))) goto loc_008E5F25;
    v_rdi = 0;
loc_008E6110:
    v_rbx = 0;
    v_stack_mB8 = v_stack_m78;
    v_stack_mA8 = v_rip - 9260225;
    v_stack_mA0 = v_stack_p60;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_stack_mD4;
    v_stack_m88 = v_stack_mD0;
    v_stack_m90 = 4;
    v_stack_m80 = 0;
    v_stack_mB0 = 0;
    if (*(unsigned __int64 *)(a2 + 488) == 0) goto loc_008E62D7;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = (unsigned int)(v_rbx + 1);
    if ((*(unsigned __int64 *)(a2 + 488)) != (v_rip - 14625)) goto loc_008E63F6;
    result = PiPnpRtlObjectActionCallback(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), v_rbx + 1, v_rbx + 8);
loc_008E619B:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E63BE;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008E62CF;
loc_008E61B1:
loc_008E61B4:
    if (((unsigned int)((unsigned int)(v_stack_mC8))) != 0xC0000225ULL) goto loc_008E63A1;
    a1 = 0;
    *(unsigned __int8 *)(a5) = 1;
    goto loc_008E5F2A;
loc_008E61CC:
    if (v_stack_p60 == 0) goto loc_008E6434;
loc_008E61D7:
    if (v_stack_mD4 != 19) goto loc_008E6094;
    v_stack_p20 = a5;
    result = PiAuVerifyAccessToObject(1, *(unsigned __int64 *)(a2 + 488), v_stack_m68, a4);
    if (sign_flag) goto loc_008E6092;
    goto loc_008E6097;
loc_008E6209:
    if ((unsigned int)(result) != 0) goto loc_008E62C4;
loc_008E6211:
    v_stack_p50 = (unsigned int)((unsigned int)(v_stack_m80));
    v_stack_p48 = v_stack_m88;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_m90));
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = v_stack_mA0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mB0;
    result = PnpGetObjectPropertyWorker((unsigned int)((unsigned int)(result)), a2, 1, v_stack_mB8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488) == 0) goto loc_008E6057;
    v_stack_mC8 = (unsigned int)(result);
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = 2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488)) != (v_rip - 14899)) goto loc_008E641D;
    result = PiPnpRtlObjectActionCallback(v_stack_mD0, a2, 8 - 7, 8);
loc_008E62A6:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E6057;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008E63E6;
    if ((unsigned int)(result) == 0) goto loc_008E6057;
loc_008E62C4:
    goto loc_008E606E;
loc_008E62CF:
    if ((unsigned int)(result) != 0) goto loc_008E6389;
loc_008E62D7:
    v_stack_p50 = (unsigned int)((unsigned int)(v_stack_m80));
    v_stack_p48 = v_stack_m88;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_m90));
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = v_stack_mA0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mB0;
    result = PnpGetObjectPropertyWorker(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 1, v_stack_mB8);
    if (*(unsigned __int64 *)(a2 + 488) == 0) goto loc_008E61B4;
    v_stack_mC8 = (unsigned int)(result);
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = 2;
    if ((*(unsigned __int64 *)(a2 + 488)) != (v_rip - 15090)) goto loc_008E6403;
    result = PiPnpRtlObjectActionCallback(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 8 - 7, 8);
loc_008E636B:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E61B4;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008E61B1;
    if ((unsigned int)(result) == 0) goto loc_008E61B4;
loc_008E6389:
    goto loc_008E60AD;
loc_008E6393:
    if (sign_flag) goto loc_008E6097;
    goto loc_008E61D7;
loc_008E63A1:
    if (!sign_flag) goto loc_008E63D1;
loc_008E63A7:
    if (!sign_flag) goto loc_008E5F28;
    goto loc_008E60AD;
loc_008E63B6:
    v_r12 = 0;
    goto loc_008E6211;
loc_008E63BE:
    goto loc_008E62D7;
loc_008E63C6:
    a1 = 0;
    goto loc_008E5F67;
loc_008E63D1:
    if (v_stack_p60 != 7) goto loc_008E63EE;
    if (v_stack_mD4 != ((unsigned int)((unsigned int)(0xC00000E5ULL)))) goto loc_008E63A7;
    *(unsigned __int8 *)(a5) = 1;
    goto loc_008E5F28;
loc_008E63E6:
    goto loc_008E6057;
loc_008E63EE:
    *(unsigned __int8 *)(a5) = 1;
    goto loc_008E5F28;
loc_008E63F6:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 8 - 7, 8);
    goto loc_008E619B;
loc_008E6403:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 8 - 7, 8);
    goto loc_008E636B;
loc_008E6410:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 8 - 7, 8);
    goto loc_008E603E;
loc_008E641D:
    result = guard_dispatch_icall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5768161) + 488), 8 - 7, 8);
    goto loc_008E62A6;
loc_008E642A:
    goto loc_008E60A9;
loc_008E6434:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC00000E5ULL))))) == 0) goto loc_008E61D7;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC00000E5ULL))))), (unsigned int)(0x47706E50ULL), 8 - 7, 8);
    v_rdi = 0;
    goto loc_008E61D7;
}
```

## 5. (Beta) C Style

```c
int64_t PiPnpRtlApplyMandatoryDeviceFilters(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p60;

    local_rsp = (local_rsp) - (248);
    result = (*(uint64_t *)(v_rip + 0x524890)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rdi = 0;
    v_stack_m78 = Arg3;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    *(uint8_t *)(arg5) = 0;
    v_stack_mD8 = 0;
    local_rbx = *(uint64_t *)(arg4);
    if (*(uint64_t *)(arg4) == 0) {
        local_rbx = *(uint64_t *)(arg4 + 0x10);
    }
    result = ExAcquireResourceSharedLite(*(uint64_t *)(local_rbx + 0x30), 1, Arg3, Arg4);
    result = ExReleaseResourceLite(*(uint64_t *)(local_rbx + 0x30), 1, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x78))) != 0) goto loc_008E60D3;
loc_008E5F25:
    *(uint8_t *)(arg5) = 1;
loc_008E5F28:
    Arg1 = 0;
loc_008E5F2A:
    if ((*(uint8_t *)(arg5)) == 0) goto loc_008E60B0;
    v_stack_mD4 = 0;
    v_stack_mD8 = 512;
    v_stack_m68 = 0x20001ULL;
    v_stack_m64 = 0x20000ULL;
    v_stack_m60 = 0x20000ULL;
    v_stack_m5C = 0xF0001ULL;
    *(uint8_t *)(arg5) = 0;
loc_008E5F67:
    if (512 <= 0) goto loc_008E5FB0;
    result = 512;
    if (0 != 0) {
        Arg2 = 0x47706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAllocatePool2(256, 512, (uint32_t)(0x47706E50ULL), Arg4);
    if (result == 0) goto loc_008E642A;
    Arg1 = 0;
loc_008E5FB0:
    v_stack_mB8 = v_stack_m78;
    v_stack_mD8 = 0;
    v_stack_mA0 = v_stack_mD4;
    v_stack_m88 = v_stack_mD8;
    v_stack_mD0 = *(uint64_t *)(v_rip + 0x5803E1);
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_m8C = 0;
    v_stack_m80 = 0;
    v_stack_mB0 = 0;
    v_stack_mA8 = v_rip - 9259832;
    v_stack_m98 = result;
    v_stack_m90 = 512;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8) == 0) goto loc_008E6211;
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = (uint32_t)(8 - 7);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8)) != (v_rip - 14274)) goto loc_008E6410;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(v_rip + 0x5803E1), Arg2, 8 - 7, 8);
loc_008E603E:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E63B6;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008E6209;
loc_008E6057:
    if (((uint32_t)((uint32_t)(v_stack_mC8))) == 0xC0000023ULL) goto loc_008E63C6;
    if (!sign_flag) goto loc_008E61CC;
loc_008E606E:
    local_rdi = result;
    if (result != 0) {
        Arg2 = 0x47706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 8 - 7, 8);
        local_rdi = 0;
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC8))))) != 0xC0000225ULL) goto loc_008E6393;
loc_008E6092:
    local_rbx = 0;
loc_008E6094:
    *(uint8_t *)(arg5) = 1;
loc_008E6097:
    if (0 != 0) {
        Arg2 = 0x47706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 8 - 7, 8);
    }
    if (sign_flag) {
        *(uint8_t *)(arg5) = 0;
    }
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 8 - 7, 8);
    local_rsp = (local_rsp) + (248);
    return result;
loc_008E60D3:
    result = PsGetSessionById((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC8))))), Arg2, 8 - 7, 8);
    if (result == 0) goto loc_008E6110;
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x79517350ULL), 8 - 7, 8);
    local_rbx = 0;
    result = PsGetServerSiloServiceSessionId(*(uint64_t *)(*(uint64_t *)(result + 0x2E8) + 0xA0), (uint32_t)(0x79517350ULL), 8 - 7, 8);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC8))))) == ((uint32_t)(result))) goto loc_008E5F25;
    local_rdi = 0;
loc_008E6110:
    local_rbx = 0;
    v_stack_mB8 = v_stack_m78;
    v_stack_mA8 = v_rip - 9260225;
    v_stack_mA0 = v_stack_p60;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_stack_mD4;
    v_stack_m88 = v_stack_mD0;
    v_stack_m90 = 4;
    v_stack_m80 = 0;
    v_stack_mB0 = 0;
    if (*(uint64_t *)(Arg2 + 0x1E8) == 0) goto loc_008E62D7;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = (uint32_t)(local_rbx + 1);
    if ((*(uint64_t *)(Arg2 + 0x1E8)) != (v_rip - 14625)) goto loc_008E63F6;
    result = PiPnpRtlObjectActionCallback(Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), local_rbx + 1, local_rbx + 8);
loc_008E619B:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E63BE;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008E62CF;
loc_008E61B1:
loc_008E61B4:
    if (((uint32_t)((uint32_t)(v_stack_mC8))) != 0xC0000225ULL) goto loc_008E63A1;
    Arg1 = 0;
    *(uint8_t *)(arg5) = 1;
    goto loc_008E5F2A;
loc_008E61CC:
    if (v_stack_p60 == 0) goto loc_008E6434;
loc_008E61D7:
    if (v_stack_mD4 != 19) goto loc_008E6094;
    v_stack_p20 = Arg5;
    result = PiAuVerifyAccessToObject(1, *(uint64_t *)(Arg2 + 0x1E8), v_stack_m68, Arg4);
    if (sign_flag) goto loc_008E6092;
    goto loc_008E6097;
loc_008E6209:
    if ((uint32_t)(result) != 0) goto loc_008E62C4;
loc_008E6211:
    v_stack_p50 = (uint32_t)((uint32_t)(v_stack_m80));
    v_stack_p48 = v_stack_m88;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_m90));
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = v_stack_mA0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mB0;
    result = PnpGetObjectPropertyWorker((uint32_t)((uint32_t)(result)), Arg2, 1, v_stack_mB8);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8) == 0) goto loc_008E6057;
    v_stack_mC8 = (uint32_t)(result);
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = 2;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8)) != (v_rip - 14899)) goto loc_008E641D;
    result = PiPnpRtlObjectActionCallback(v_stack_mD0, Arg2, 8 - 7, 8);
loc_008E62A6:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E6057;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008E63E6;
    if ((uint32_t)(result) == 0) goto loc_008E6057;
loc_008E62C4:
    goto loc_008E606E;
loc_008E62CF:
    if ((uint32_t)(result) != 0) goto loc_008E6389;
loc_008E62D7:
    v_stack_p50 = (uint32_t)((uint32_t)(v_stack_m80));
    v_stack_p48 = v_stack_m88;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_m90));
    v_stack_p38 = v_stack_m98;
    v_stack_p30 = v_stack_mA0;
    v_stack_p28 = v_stack_mA8;
    v_stack_p20 = v_stack_mB0;
    result = PnpGetObjectPropertyWorker(Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 1, v_stack_mB8);
    if (*(uint64_t *)(Arg2 + 0x1E8) == 0) goto loc_008E61B4;
    v_stack_mC8 = (uint32_t)(result);
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = 2;
    if ((*(uint64_t *)(Arg2 + 0x1E8)) != (v_rip - 15090)) goto loc_008E6403;
    result = PiPnpRtlObjectActionCallback(Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 8 - 7, 8);
loc_008E636B:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E61B4;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008E61B1;
    if ((uint32_t)(result) == 0) goto loc_008E61B4;
loc_008E6389:
    goto loc_008E60AD;
loc_008E6393:
    if (sign_flag) goto loc_008E6097;
    goto loc_008E61D7;
loc_008E63A1:
    if (!sign_flag) goto loc_008E63D1;
loc_008E63A7:
    if (!sign_flag) goto loc_008E5F28;
    goto loc_008E60AD;
loc_008E63B6:
    local_r12 = 0;
    goto loc_008E6211;
loc_008E63BE:
    goto loc_008E62D7;
loc_008E63C6:
    Arg1 = 0;
    goto loc_008E5F67;
loc_008E63D1:
    if (v_stack_p60 != 7) goto loc_008E63EE;
    if (v_stack_mD4 != ((uint32_t)((uint32_t)(0xC00000E5ULL)))) goto loc_008E63A7;
    *(uint8_t *)(arg5) = 1;
    goto loc_008E5F28;
loc_008E63E6:
    goto loc_008E6057;
loc_008E63EE:
    *(uint8_t *)(arg5) = 1;
    goto loc_008E5F28;
loc_008E63F6:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 8 - 7, 8);
    goto loc_008E619B;
loc_008E6403:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 8 - 7, 8);
    goto loc_008E636B;
loc_008E6410:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 8 - 7, 8);
    goto loc_008E603E;
loc_008E641D:
    result = guard_dispatch_icall(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x5803E1) + 0x1E8), 8 - 7, 8);
    goto loc_008E62A6;
loc_008E642A:
    goto loc_008E60A9;
loc_008E6434:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000E5ULL))))) == 0) goto loc_008E61D7;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000E5ULL))))), (uint32_t)(0x47706E50ULL), 8 - 7, 8);
    local_rdi = 0;
    goto loc_008E61D7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1E8` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R` |
| `Arg5` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E5E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
