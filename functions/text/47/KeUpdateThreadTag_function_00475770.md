# KeUpdateThreadTag

- RVA: `0x00475770`–`0x00475D30` (길이 `1,472` bytes)
- VA: `0x0000000140475770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ACBD4`
- 디코드: `358`개 명령, `1,472/1,472` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004757B3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004757D7` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x00475817` → [KiEndThreadCycleAccumulation](../37/KiEndThreadCycleAccumulation_function_0037BFF0.md) (function, `0x0037BFF0`)
- `0x0047583B` → [KiStartThreadCycleAccumulation](../37/KiStartThreadCycleAccumulation_function_0037DB30.md) (function, `0x0037DB30`)
- `0x0047585D` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0047588F` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x004758E9` → [KiUpdateThreadQosGroupingSummaries](../25/KiUpdateThreadQosGroupingSummaries_function_00257AEC.md) (function, `0x00257AEC`)
- `0x0047590E` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x00475913` → [Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage](Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage_function_00475D38.md) (function, `0x00475D38`)
- `0x0047592A` → [Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage](Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage_function_00475D38.md) (function, `0x00475D38`)
- `0x00475955` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0047596D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004759BA` → [KiAcquireThreadStateLockForWrite](../30/KiAcquireThreadStateLockForWrite_function_0030E8C0.md) (function, `0x0030E8C0`)
- `0x004759F9` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x00475A73` → [KiUpdateThreadQosGroupingSummaries](../25/KiUpdateThreadQosGroupingSummaries_function_00257AEC.md) (function, `0x00257AEC`)
- `0x00475A8E` → [Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage](Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage_function_00475D38.md) (function, `0x00475D38`)
- `0x00475AB5` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x00475ABE` → [Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage](Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage_function_00475D38.md) (function, `0x00475D38`)
- `0x00475AD2` → [KiSendSoftwareInterrupt](../25/KiSendSoftwareInterrupt_function_00250A30.md) (function, `0x00250A30`)
- `0x00475B06` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00475B95` → [KiIpiSendRequest](../31/KiIpiSendRequest_function_003113C0.md) (function, `0x003113C0`)
- `0x00475BA3` → [KiIpiStallOnPacketTargetsPrcb](../2C/KiIpiStallOnPacketTargetsPrcb_function_002CE670.md) (function, `0x002CE670`)
- `0x00475BB8` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00475BE5` → [KiCheckPreferredHeteroProcessor](../39/KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x00475C06` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00475C2E` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00475CB1` → [KiUpdateThreadQosGroupingSummaries](../25/KiUpdateThreadQosGroupingSummaries_function_00257AEC.md) (function, `0x00257AEC`)
- `0x00475CE5` → [KiCheckPreferredHeteroProcessor](../39/KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x00475D09` → [KiSendSoftwareInterrupt](../25/KiSendSoftwareInterrupt_function_00250A30.md) (function, `0x00250A30`)
- `0x00475D19` → [KeCheckAndApplyBamQos](../39/KeCheckAndApplyBamQos_function_00391910.md) (function, `0x00391910`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00475793` → RVA `0x00E0A740` (`.data`; read)
- `0x00475944` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00475B0B` → RVA `0x00F231B0` (`.data`; read)
- `0x00475B72` → RVA `0x003A3FE0` (`KiIpiUpdateThreadTag`; read)
- `0x00475BEA` → RVA `0x00FC6C6C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00475CEC` → [sub_006F439C](../6F/Unknown_function_006F439C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00475770  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00475775  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00475779  55                              push rbp
0047577A  56                              push rsi
0047577B  57                              push rdi
0047577C  41 54                           push r12
0047577E  41 55                           push r13
00475780  41 56                           push r14
00475782  41 57                           push r15
00475784  48 8D AC 24 30 FF FF FF         lea rbp, [rsp - 0xd0]
0047578C  48 81 EC D0 01 00 00            sub rsp, 0x1d0
00475793  48 8B 05 A6 4F 99 00            mov rax, qword ptr [rip + 0x994fa6]
0047579A  48 33 C4                        xor rax, rsp
0047579D  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
004757A4  48 8B F9                        mov rdi, rcx
004757A7  33 D2                           xor edx, edx
004757A9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
004757AD  41 B8 08 01 00 00               mov r8d, 0x108
004757B3  E8 88 14 25 00                  call 0x1406c6c40
004757B8  45 33 ED                        xor r13d, r13d
004757BB  48 8D 54 24 32                  lea rdx, [rsp + 0x32]
004757C0  48 8B CF                        mov rcx, rdi
004757C3  44 88 6C 24 32                  mov byte ptr [rsp + 0x32], r13b
004757C8  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
004757CD  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
004757D2  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
004757D7  E8 A4 0A F2 FF                  call 0x140396280
004757DC  0F B6 47 7C                     movzx eax, byte ptr [rdi + 0x7c]
004757E0  3B 85 18 01 00 00               cmp eax, dword ptr [rbp + 0x118]
004757E6  0F 84 4C 04 00 00               je 0x140475c38
004757EC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004757F5  48 3B F8                        cmp rdi, rax
004757F8  0F 85 90 01 00 00               jne 0x14047598e
004757FE  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
00475807  45 8A E5                        mov r12b, r13b
0047580A  FA                              cli
0047580B  45 33 C9                        xor r9d, r9d
0047580E  45 33 C0                        xor r8d, r8d
00475811  48 8B D7                        mov rdx, rdi
00475814  48 8B CB                        mov rcx, rbx
00475817  E8 D4 67 F0 FF                  call 0x14037bff0
0047581C  8B 85 18 01 00 00               mov eax, dword ptr [rbp + 0x118]
00475822  85 C0                           test eax, eax
00475824  0F 84 17 04 00 00               je 0x140475c41
0047582A  F0 0F BA 2F 14                  lock bts dword ptr [rdi], 0x14
0047582F  45 33 C0                        xor r8d, r8d
00475832  88 47 7C                        mov byte ptr [rdi + 0x7c], al
00475835  48 8B D7                        mov rdx, rdi
00475838  48 8B CB                        mov rcx, rbx
0047583B  E8 F0 82 F0 FF                  call 0x14037db30
00475840  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00475849  49 8B 90 B8 8E 00 00            mov rdx, qword ptr [r8 + 0x8eb8]
00475850  48 85 D2                        test rdx, rdx
00475853  0F 85 B7 03 00 00               jne 0x140475c10
00475859  FB                              sti
0047585A  48 8B CF                        mov rcx, rdi
0047585D  E8 AE 27 DE FF                  call 0x140258010
00475862  0F B6 8F 04 02 00 00            movzx ecx, byte ptr [rdi + 0x204]
00475869  44 8B F0                        mov r14d, eax
0047586C  BE 01 00 00 00                  mov esi, 1
00475871  3B C1                           cmp eax, ecx
00475873  0F 84 9A 00 00 00               je 0x140475913
00475879  0F 57 C0                        xorps xmm0, xmm0
0047587C  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
00475880  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00475885  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0047588A  8B D6                           mov edx, esi
0047588C  48 8B CB                        mov rcx, rbx
0047588F  E8 CC 94 E9 FF                  call 0x14030ed60
00475894  44 88 B7 04 02 00 00            mov byte ptr [rdi + 0x204], r14b
0047589B  4C 39 6B 10                     cmp qword ptr [rbx + 0x10], r13
0047589F  75 59                           jne 0x1404758fa
004758A1  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
004758A4  D1 E9                           shr ecx, 1
004758A6  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
004758AB  23 CE                           and ecx, esi
004758AD  0F 84 29 02 00 00               je 0x140475adc
004758B3  3B CE                           cmp ecx, esi
004758B5  75 43                           jne 0x1404758fa
004758B7  48 8B 83 58 8E 00 00            mov rax, qword ptr [rbx + 0x8e58]
004758BE  0F B6 08                        movzx ecx, byte ptr [rax]
004758C1  4C 8D 78 08                     lea r15, [rax + 8]
004758C5  85 C9                           test ecx, ecx
004758C7  74 31                           je 0x1404758fa
004758C9  44 8B E9                        mov r13d, ecx
004758CC  4D 8B 07                        mov r8, qword ptr [r15]
004758CF  49 8B 50 38                     mov rdx, qword ptr [r8 + 0x38]
004758D3  8A 42 40                        mov al, byte ptr [rdx + 0x40]
004758D6  8A C8                           mov cl, al
004758D8  32 8F 04 02 00 00               xor cl, byte ptr [rdi + 0x204]
004758DE  80 E1 07                        and cl, 7
004758E1  32 C8                           xor cl, al
004758E3  88 4A 40                        mov byte ptr [rdx + 0x40], cl
004758E6  49 8B C8                        mov rcx, r8
004758E9  E8 FE 21 DE FF                  call 0x140257aec
004758EE  4D 8D 7F 08                     lea r15, [r15 + 8]
004758F2  4C 2B EE                        sub r13, rsi
004758F5  75 D5                           jne 0x1404758cc
004758F7  45 8A EC                        mov r13b, r12b
004758FA  48 8D 45 98                     lea rax, [rbp - 0x68]
004758FE  45 33 C9                        xor r9d, r9d
00475901  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00475906  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0047590B  48 8B D3                        mov rdx, rbx
0047590E  E8 FD 1F DA FF                  call 0x140217910
00475913  E8 20 04 00 00                  call 0x140475d38
00475918  41 83 FE 04                     cmp r14d, 4
0047591C  0F 84 BA 03 00 00               je 0x140475cdc
00475922  48 C7 47 40 00 00 00 00         mov qword ptr [rdi + 0x40], 0
0047592A  E8 09 04 00 00                  call 0x140475d38
0047592F  45 84 E4                        test r12b, r12b
00475932  0F 85 C9 03 00 00               jne 0x140475d01
00475938  45 84 ED                        test r13b, r13b
0047593B  0F 85 D2 03 00 00               jne 0x140475d13
00475941  45 33 ED                        xor r13d, r13d
00475944  44 39 2D D5 13 B5 00            cmp dword ptr [rip + 0xb513d5], r13d
0047594B  74 0D                           je 0x14047595a
0047594D  44 0F 20 C1                     mov rcx, cr8
00475951  8A 54 24 32                     mov dl, byte ptr [rsp + 0x32]
00475955  E8 3E FD 07 00                  call 0x1404f5698
0047595A  0F B6 44 24 32                  movzx eax, byte ptr [rsp + 0x32]
0047595F  44 0F 22 C0                     mov cr8, rax
00475963  48 8B 8D C0 00 00 00            mov rcx, qword ptr [rbp + 0xc0]
0047596A  48 33 CC                        xor rcx, rsp
0047596D  E8 CE 6C 23 00                  call 0x1406ac640
00475972  48 8B 9C 24 20 02 00 00         mov rbx, qword ptr [rsp + 0x220]
0047597A  48 81 C4 D0 01 00 00            add rsp, 0x1d0
00475981  41 5F                           pop r15
00475983  41 5E                           pop r14
00475985  41 5D                           pop r13
00475987  41 5C                           pop r12
00475989  5F                              pop rdi
0047598A  5E                              pop rsi
0047598B  5D                              pop rbp
0047598C  C3                              ret
0047598D  CC                              int3
0047598E  0F 57 C0                        xorps xmm0, xmm0
00475991  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00475996  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0047599B  48 8B CF                        mov rcx, rdi
0047599E  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
004759A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004759A8  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
004759AD  45 8A FD                        mov r15b, r13b
004759B0  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
004759B5  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
004759BA  E8 01 8F E9 FF                  call 0x14030e8c0
004759BF  BE 01 00 00 00                  mov esi, 1
004759C4  88 44 24 31                     mov byte ptr [rsp + 0x31], al
004759C8  44 8D 76 01                     lea r14d, [rsi + 1]
004759CC  41 3A C6                        cmp al, r14b
004759CF  0F 84 13 01 00 00               je 0x140475ae8
004759D5  8A 4F 71                        mov cl, byte ptr [rdi + 0x71]
004759D8  84 C9                           test cl, cl
004759DA  0F 85 08 01 00 00               jne 0x140475ae8
004759E0  8B 8D 18 01 00 00               mov ecx, dword ptr [rbp + 0x118]
004759E6  85 C9                           test ecx, ecx
004759E8  0F 84 5D 02 00 00               je 0x140475c4b
004759EE  F0 0F BA 2F 14                  lock bts dword ptr [rdi], 0x14
004759F3  88 4F 7C                        mov byte ptr [rdi + 0x7c], cl
004759F6  48 8B CF                        mov rcx, rdi
004759F9  E8 12 26 DE FF                  call 0x140258010
004759FE  0F B6 8F 04 02 00 00            movzx ecx, byte ptr [rdi + 0x204]
00475A05  44 8B E0                        mov r12d, eax
00475A08  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00475A0D  3B C1                           cmp eax, ecx
00475A0F  74 7D                           je 0x140475a8e
00475A11  0F B6 54 24 31                  movzx edx, byte ptr [rsp + 0x31]
00475A16  44 88 A7 04 02 00 00            mov byte ptr [rdi + 0x204], r12b
00475A1D  41 2B D6                        sub edx, r14d
00475A20  0F 85 2F 02 00 00               jne 0x140475c55
00475A26  4C 39 6B 10                     cmp qword ptr [rbx + 0x10], r13
00475A2A  75 62                           jne 0x140475a8e
00475A2C  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
00475A2F  D1 E9                           shr ecx, 1
00475A31  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00475A36  23 CE                           and ecx, esi
00475A38  0F 84 88 01 00 00               je 0x140475bc6
00475A3E  3B CE                           cmp ecx, esi
00475A40  75 4C                           jne 0x140475a8e
00475A42  48 8B 83 58 8E 00 00            mov rax, qword ptr [rbx + 0x8e58]
00475A49  0F B6 08                        movzx ecx, byte ptr [rax]
00475A4C  4C 8D 78 08                     lea r15, [rax + 8]
00475A50  85 C9                           test ecx, ecx
00475A52  74 37                           je 0x140475a8b
00475A54  44 8B E9                        mov r13d, ecx
00475A57  49 8B 0F                        mov rcx, qword ptr [r15]
00475A5A  4C 8B 41 38                     mov r8, qword ptr [rcx + 0x38]
00475A5E  41 8A 40 40                     mov al, byte ptr [r8 + 0x40]
00475A62  8A D0                           mov dl, al
00475A64  32 97 04 02 00 00               xor dl, byte ptr [rdi + 0x204]
00475A6A  80 E2 07                        and dl, 7
00475A6D  32 D0                           xor dl, al
00475A6F  41 88 50 40                     mov byte ptr [r8 + 0x40], dl
00475A73  E8 74 20 DE FF                  call 0x140257aec
00475A78  4D 8D 7F 08                     lea r15, [r15 + 8]
00475A7C  4C 2B EE                        sub r13, rsi
00475A7F  75 D6                           jne 0x140475a57
00475A81  44 8A 7C 24 30                  mov r15b, byte ptr [rsp + 0x30]
00475A86  45 33 ED                        xor r13d, r13d
00475A89  EB 03                           jmp 0x140475a8e
00475A8B  45 8A FD                        mov r15b, r13b
00475A8E  E8 A5 02 00 00                  call 0x140475d38
00475A93  44 38 74 24 31                  cmp byte ptr [rsp + 0x31], r14b
00475A98  0F 84 34 01 00 00               je 0x140475bd2
00475A9E  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00475AA3  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00475AA8  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00475AAD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00475AB2  48 8B D3                        mov rdx, rbx
00475AB5  E8 56 1E DA FF                  call 0x140217910
00475ABA  4C 89 6F 40                     mov qword ptr [rdi + 0x40], r13
00475ABE  E8 75 02 00 00                  call 0x140475d38
00475AC3  45 84 FF                        test r15b, r15b
00475AC6  0F 84 78 FE FF FF               je 0x140475944
00475ACC  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
00475ACF  41 8A D6                        mov dl, r14b
00475AD2  E8 59 AF DD FF                  call 0x140250a30
00475AD7  E9 68 FE FF FF                  jmp 0x140475944
00475ADC  4C 8D 7C 24 50                  lea r15, [rsp + 0x50]
00475AE1  8B CE                           mov ecx, esi
00475AE3  E9 E1 FD FF FF                  jmp 0x1404758c9
00475AE8  8B 9F 18 02 00 00               mov ebx, dword ptr [rdi + 0x218]
00475AEE  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00475AF2  33 D2                           xor edx, edx
00475AF4  48 C7 45 B0 01 00 20 00         mov qword ptr [rbp - 0x50], 0x200001
00475AFC  41 B8 00 01 00 00               mov r8d, 0x100
00475B02  0F BA F3 1F                     btr ebx, 0x1f
00475B06  E8 35 11 25 00                  call 0x1406c6c40
00475B0B  48 8B 05 9E D6 AA 00            mov rax, qword ptr [rip + 0xaad69e]
00475B12  44 8B 04 98                     mov r8d, dword ptr [rax + rbx*4]
00475B16  41 8B C8                        mov ecx, r8d
00475B19  0F B7 45 B0                     movzx eax, word ptr [rbp - 0x50]
00475B1D  41 83 E0 3F                     and r8d, 0x3f
00475B21  C1 E9 06                        shr ecx, 6
00475B24  3B C1                           cmp eax, ecx
00475B26  0F 86 98 01 00 00               jbe 0x140475cc4
00475B2C  8B D1                           mov edx, ecx
00475B2E  48 8B 4C CD B8                  mov rcx, qword ptr [rbp + rcx*8 - 0x48]
00475B33  41 8B C0                        mov eax, r8d
00475B36  48 0F AB C1                     bts rcx, rax
00475B3A  48 89 4C D5 B8                  mov qword ptr [rbp + rdx*8 - 0x48], rcx
00475B3F  44 0F 20 C1                     mov rcx, cr8
00475B43  BA 0C 00 00 00                  mov edx, 0xc
00475B48  44 0F 22 C2                     mov cr8, rdx
00475B4C  44 39 2D CD 11 B5 00            cmp dword ptr [rip + 0xb511cd], r13d
00475B53  0F 85 AD 00 00 00               jne 0x140475c06
00475B59  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00475B62  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
00475B69  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00475B6D  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00475B72  48 8D 05 67 E4 F2 FF            lea rax, [rip - 0xd1b99]
00475B79  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00475B7E  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00475B82  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00475B86  33 D2                           xor edx, edx
00475B88  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
00475B8C  48 C7 44 24 20 05 00 00 00      mov qword ptr [rsp + 0x20], 5
00475B95  E8 26 B8 E9 FF                  call 0x1403113c0
00475B9A  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00475BA3  E8 C8 8A E5 FF                  call 0x1402ce670
00475BA8  44 39 2D 71 11 B5 00            cmp dword ptr [rip + 0xb51171], r13d
00475BAF  74 0C                           je 0x140475bbd
00475BB1  44 0F 20 C1                     mov rcx, cr8
00475BB5  41 8A D6                        mov dl, r14b
00475BB8  E8 DB FA 07 00                  call 0x1404f5698
00475BBD  45 0F 22 C6                     mov cr8, r14
00475BC1  E9 30 FE FF FF                  jmp 0x1404759f6
00475BC6  4C 8D 7C 24 60                  lea r15, [rsp + 0x60]
00475BCB  8B CE                           mov ecx, esi
00475BCD  E9 82 FE FF FF                  jmp 0x140475a54
00475BD2  41 83 FC 04                     cmp r12d, 4
00475BD6  0F 85 C2 FE FF FF               jne 0x140475a9e
00475BDC  44 8B C6                        mov r8d, esi
00475BDF  48 8B D3                        mov rdx, rbx
00475BE2  48 8B CF                        mov rcx, rdi
00475BE5  E8 42 7B F2 FF                  call 0x14039d72c
00475BEA  44 39 2D 7B 10 B5 00            cmp dword ptr [rip + 0xb5107b], r13d
00475BF1  0F 84 2C 01 00 00               je 0x140475d23
00475BF7  40 88 B3 B9 38 00 00            mov byte ptr [rbx + 0x38b9], sil
00475BFE  44 8A FE                        mov r15b, sil
00475C01  E9 98 FE FF FF                  jmp 0x140475a9e
00475C06  E8 F1 FA 07 00                  call 0x1404f56fc
00475C0B  E9 49 FF FF FF                  jmp 0x140475b59
00475C10  0F 0D 0A                        prefetchw byte ptr [rdx]
00475C13  8B 02                           mov eax, dword ptr [rdx]
00475C15  8B C8                           mov ecx, eax
00475C17  0F BA F1 15                     btr ecx, 0x15
00475C1B  F0 0F B1 0A                     lock cmpxchg dword ptr [rdx], ecx
00475C1F  75 F4                           jne 0x140475c15
00475C21  0F BA E0 15                     bt eax, 0x15
00475C25  0F 83 2E FC FF FF               jae 0x140475859
00475C2B  49 8B C8                        mov rcx, r8
00475C2E  E8 9D D5 DE FF                  call 0x1402631d0
00475C33  E9 21 FC FF FF                  jmp 0x140475859
00475C38  4C 89 6F 40                     mov qword ptr [rdi + 0x40], r13
00475C3C  E9 03 FD FF FF                  jmp 0x140475944
00475C41  F0 0F BA 37 14                  lock btr dword ptr [rdi], 0x14
00475C46  E9 E4 FB FF FF                  jmp 0x14047582f
00475C4B  F0 0F BA 37 14                  lock btr dword ptr [rdi], 0x14
00475C50  E9 9E FD FF FF                  jmp 0x1404759f3
00475C55  3B D6                           cmp edx, esi
00475C57  0F 85 31 FE FF FF               jne 0x140475a8e
00475C5D  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
00475C60  D1 E9                           shr ecx, 1
00475C62  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00475C67  23 CE                           and ecx, esi
00475C69  74 20                           je 0x140475c8b
00475C6B  3B CE                           cmp ecx, esi
00475C6D  0F 85 1B FE FF FF               jne 0x140475a8e
00475C73  48 8B 83 58 8E 00 00            mov rax, qword ptr [rbx + 0x8e58]
00475C7A  0F B6 08                        movzx ecx, byte ptr [rax]
00475C7D  4C 8D 78 08                     lea r15, [rax + 8]
00475C81  85 C9                           test ecx, ecx
00475C83  0F 84 02 FE FF FF               je 0x140475a8b
00475C89  EB 07                           jmp 0x140475c92
00475C8B  4C 8D 7C 24 58                  lea r15, [rsp + 0x58]
00475C90  8B CE                           mov ecx, esi
00475C92  44 8B E9                        mov r13d, ecx
00475C95  49 8B 0F                        mov rcx, qword ptr [r15]
00475C98  4C 8B 41 38                     mov r8, qword ptr [rcx + 0x38]
00475C9C  41 8A 40 40                     mov al, byte ptr [r8 + 0x40]
00475CA0  8A D0                           mov dl, al
00475CA2  32 97 04 02 00 00               xor dl, byte ptr [rdi + 0x204]
00475CA8  80 E2 07                        and dl, 7
00475CAB  32 D0                           xor dl, al
00475CAD  41 88 50 40                     mov byte ptr [r8 + 0x40], dl
00475CB1  E8 36 1E DE FF                  call 0x140257aec
00475CB6  4D 8D 7F 08                     lea r15, [r15 + 8]
00475CBA  4C 2B EE                        sub r13, rsi
00475CBD  75 D6                           jne 0x140475c95
00475CBF  E9 BD FD FF FF                  jmp 0x140475a81
00475CC4  0F B7 45 B2                     movzx eax, word ptr [rbp - 0x4e]
00475CC8  3B C1                           cmp eax, ecx
00475CCA  0F 86 6F FE FF FF               jbe 0x140475b3f
00475CD0  8D 04 0E                        lea eax, [rsi + rcx]
00475CD3  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
00475CD7  E9 50 FE FF FF                  jmp 0x140475b2c
00475CDC  44 8B C6                        mov r8d, esi
00475CDF  48 8B D3                        mov rdx, rbx
00475CE2  48 8B CF                        mov rcx, rdi
00475CE5  E8 42 7A F2 FF                  call 0x14039d72c
00475CEA  85 C0                           test eax, eax
00475CEC  0F 84 AA E6 27 00               je 0x1406f439c
00475CF2  40 88 B3 B9 38 00 00            mov byte ptr [rbx + 0x38b9], sil
00475CF9  44 8A E6                        mov r12b, sil
00475CFC  E9 21 FC FF FF                  jmp 0x140475922
00475D01  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
00475D04  BA 02 00 00 00                  mov edx, 2
00475D09  E8 22 AD DD FF                  call 0x140250a30
00475D0E  E9 25 FC FF FF                  jmp 0x140475938
00475D13  48 8B D7                        mov rdx, rdi
00475D16  48 8B CB                        mov rcx, rbx
00475D19  E8 F2 BB F1 FF                  call 0x140391910
00475D1E  E9 1E FC FF FF                  jmp 0x140475941
00475D23  85 C0                           test eax, eax
00475D25  0F 84 73 FD FF FF               je 0x140475a9e
00475D2B  E9 C7 FE FF FF                  jmp 0x140475bf7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeUpdateThreadTag(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m150;
    unsigned __int16 v_stack_m156;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D6;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (464);
    result = (*(unsigned __int64 *)(v_rip + 10047398)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    result = memset(v_stack_m158, a2, 264, a4);
    v_r13 = 0;
    v_stack_m1D6 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    result = KiAcquireThreadLockRaiseToDpc(a1, v_stack_m1D6, 264, a4);
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 124))) == v_stack_p10) goto loc_00475C38;
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0047598E;
    a4 = 0;
    a3 = 0;
    result = KiEndThreadCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, a3, a4);
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_00475C41;
loc_0047582F:
    a3 = 0;
    *(unsigned __int8 *)(a1 + 124) = (unsigned __int8)((unsigned int)(v_stack_p10));
    result = KiStartThreadCycleAccumulation(*(unsigned __int64 *)(gs_base + (0 + 32)), a1, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00475C10;
loc_00475859:
    result = KiComputeThreadQos(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    if (((unsigned int)(result)) == ((unsigned int)(*(unsigned __int8 *)(a1 + 516)))) goto loc_00475913;
    v_stack_m170 = v_xmm0;
    v_stack_m1C8 = *(unsigned __int64 *)(gs_base + (0 + 32));
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(gs_base + (0 + 32)), 1, v_stack_m1D0, a4);
    *(unsigned __int8 *)(a1 + 516) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16)) != 0) goto loc_004758FA;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) >> (1));
    v_stack_m1B8 = *(unsigned __int64 *)(gs_base + (0 + 32));
    a1 = (unsigned int)((a1) & (1));
    if (condition_is_equal) goto loc_00475ADC;
    if (((unsigned int)(a1)) != 1) goto loc_004758FA;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440))) == 0) goto loc_004758FA;
loc_004758C9:
loc_004758CC:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8) + 56) + 64))) ^ (*(unsigned __int8 *)(a1 + 516)));
    a1 = (unsigned __int8)((a1) & (7));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8) + 56) + 64))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8) + 56) + 64) = (unsigned __int8)(a1);
    result = KiUpdateThreadQosGroupingSummaries(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8) + 56), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8), a4);
    v_r13 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_004758CC;
loc_004758FA:
    a4 = 0;
    v_stack_m1E8 = v_stack_m170;
    result = KiReleaseThreadStateLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m1D0, a4);
loc_00475913:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m1D0, a4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 4) goto loc_00475CDC;
loc_00475922:
    *(unsigned __int64 *)(a1 + 64) = 0;
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36440) + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m1D0, a4);
    if (0 != 0) goto loc_00475D01;
loc_00475938:
    if (0 != 0) goto loc_00475D13;
loc_00475941:
    v_r13 = 0;
loc_00475944:
    if ((*(unsigned int *)(v_rip + 11867093)) != 0) {
        a1 = v_cr8;
        a2 = v_stack_m1D6;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m1D0, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1D0, a4);
    v_rsp = (v_rsp) + (464);
    return result;
loc_0047598E:
    v_stack_p30 = 0;
    v_stack_p20 = v_stack_p68;
    v_stack_p68 = v_xmm0;
    result = KiAcquireThreadStateLockForWrite(a1, v_stack_p40, v_stack_p38, v_stack_p48);
    v_stack_p31 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) == ((unsigned __int8)(1 + 1))) goto loc_00475AE8;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 113)) != 0) goto loc_00475AE8;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_00475C4B;
loc_004759F3:
    *(unsigned __int8 *)(a1 + 124) = (unsigned __int8)((unsigned int)(v_stack_p10));
loc_004759F6:
    result = KiComputeThreadQos(a1, v_stack_p40, v_stack_p38, v_stack_p48);
    if (((unsigned int)(result)) == ((unsigned int)(*(unsigned __int8 *)(a1 + 516)))) goto loc_00475A8E;
    *(unsigned __int8 *)(a1 + 516) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    a2 = (unsigned int)((v_stack_p31) - ((unsigned int)(1 + 1)));
    if (condition_is_not_equal) goto loc_00475C55;
    if ((*(unsigned __int64 *)(v_stack_p40 + 16)) != 0) goto loc_00475A8E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) >> (1));
    v_stack_p60 = v_stack_p40;
    a1 = (unsigned int)((a1) & (1));
    if (condition_is_equal) goto loc_00475BC6;
    if (((unsigned int)(a1)) != 1) goto loc_00475A8E;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p40 + 36440))) == 0) goto loc_00475A8B;
loc_00475A54:
loc_00475A57:
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8) + 56) + 64))) ^ (*(unsigned __int8 *)(a1 + 516)));
    a2 = (unsigned __int8)((a2) & (7));
    a2 = (unsigned __int8)((a2) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8) + 56) + 64))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8) + 56) + 64) = (unsigned __int8)(a2);
    result = KiUpdateThreadQosGroupingSummaries(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8) + 56), v_stack_p48);
    v_r13 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p40 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_00475A57;
loc_00475A81:
    v_r13 = 0;
    goto loc_00475A8E;
loc_00475A8B:
loc_00475A8E:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8) + 56), v_stack_p48);
    if (v_stack_p31 == ((unsigned __int8)(1 + 1))) goto loc_00475BD2;
loc_00475A9E:
    v_stack_p20 = v_stack_p68;
    result = KiReleaseThreadStateLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8), v_stack_p40, v_stack_p38, v_stack_p48);
    *(unsigned __int64 *)(a1 + 64) = 0;
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40 + 36440) + 8), v_stack_p40, v_stack_p38, v_stack_p48);
    if (0 == 0) goto loc_00475944;
    result = KiSendSoftwareInterrupt((unsigned int)(*(unsigned int *)(v_stack_p40 + 36)), (unsigned __int8)(1 + 1), v_stack_p38, v_stack_p48);
    goto loc_00475944;
loc_00475ADC:
    goto loc_004758C9;
loc_00475AE8:
    a2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, a2, 256, v_stack_p48);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11196062) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11196062) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 4))))) >> (6));
    if (((unsigned int)(v_stack_m158)) <= ((unsigned int)(a1))) goto loc_00475CC4;
loc_00475B2C:
    *(unsigned __int64 *)(v_stack_m108 + (unsigned int)((unsigned int)(a1)) * 8 - 72) = *(unsigned __int64 *)(v_stack_m108 + a1 * 8 - 72);
loc_00475B3F:
    if ((*(unsigned int *)(v_rip + 11866573)) != 0) goto loc_00475C06;
loc_00475B59:
    v_stack_m188 = v_stack_p10;
    v_stack_p78 = a1;
    v_stack_m178 = v_rip - 859033;
    a2 = 0;
    v_stack_m180 = 0;
    v_stack_p20 = 5;
    result = KiIpiSendRequest(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, v_stack_m158, v_stack_p78);
    result = KiIpiStallOnPacketTargetsPrcb(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m158, v_stack_p78);
    if ((*(unsigned int *)(v_rip + 11866481)) != 0) {
        a1 = 12;
        a2 = (unsigned __int8)(1 + 1);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m158, v_stack_p78);
    }
    goto loc_004759F6;
loc_00475BC6:
    goto loc_00475A54;
loc_00475BD2:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 4) goto loc_00475A9E;
    result = KiCheckPreferredHeteroProcessor(a1, (unsigned int)(*(unsigned int *)(a1 + 536)), 1, v_stack_p78);
    if ((*(unsigned int *)(v_rip + 11866235)) == 0) goto loc_00475D23;
loc_00475BF7:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 14521) = 1;
    goto loc_00475A9E;
loc_00475C06:
    result = KiRaiseIrqlProcessIrqlFlags(a1, (unsigned int)(*(unsigned int *)(a1 + 536)), 1, v_stack_p78);
    goto loc_00475B59;
loc_00475C10:
loc_00475C15:
    if ((*(unsigned int *)(v_rip + 11866235)) != 0) goto loc_00475C15;
    if ((*(unsigned int *)(v_rip + 11866235)) >= 0) goto loc_00475859;
    result = KiRemoveSystemWorkPriorityKick(1, (unsigned int)(*(unsigned int *)(a1 + 536)), 1, v_stack_p78);
    goto loc_00475859;
loc_00475C38:
    *(unsigned __int64 *)(a1 + 64) = 0;
    goto loc_00475944;
loc_00475C41:
    goto loc_0047582F;
loc_00475C4B:
    goto loc_004759F3;
loc_00475C55:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != 1) goto loc_00475A8E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) >> (1));
    v_stack_p58 = (unsigned int)(*(unsigned int *)(a1 + 536));
    a1 = (unsigned int)((a1) & (1));
    if (condition_is_equal) goto loc_00475C8B;
    if (((unsigned int)(a1)) != 1) goto loc_00475A8E;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 36440))) == 0) goto loc_00475A8B;
    goto loc_00475C92;
loc_00475C8B:
loc_00475C92:
loc_00475C95:
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 56) + 64))) ^ (*(unsigned __int8 *)(a1 + 516)));
    a2 = (unsigned __int8)((a2) & (7));
    a2 = (unsigned __int8)((a2) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 56) + 64))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 56) + 64) = (unsigned __int8)(a2);
    result = KiUpdateThreadQosGroupingSummaries(*(unsigned __int64 *)(v_stack_p58), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 56), v_stack_p78);
    v_r13 = (1) - (1);
    if (condition_is_not_equal) goto loc_00475C95;
    goto loc_00475A81;
loc_00475CC4:
    if (((unsigned int)(v_stack_m156)) <= ((unsigned int)(*(unsigned __int64 *)(v_stack_p58)))) goto loc_00475B3F;
    v_stack_m158 = (unsigned __int16)(1 + *(unsigned __int64 *)(v_stack_p58) * 1);
    goto loc_00475B2C;
loc_00475CDC:
    result = KiCheckPreferredHeteroProcessor(a1, (unsigned int)(*(unsigned int *)(a1 + 536)), 1, v_stack_p78);
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 14521) = 1;
    goto loc_00475922;
loc_00475D01:
    result = KiSendSoftwareInterrupt((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 36)), 2, 1, v_stack_p78);
    goto loc_00475938;
loc_00475D13:
    result = KeCheckAndApplyBamQos((unsigned int)(*(unsigned int *)(a1 + 536)), a1, 1, v_stack_p78);
    goto loc_00475941;
loc_00475D23:
    if ((unsigned int)(result) == 0) goto loc_00475A9E;
    goto loc_00475BF7;
}
```

## 5. (Beta) C Style

```c
int64_t KeUpdateThreadTag(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m150;
    uint16_t v_stack_m156;
    uint64_t v_stack_m158;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D6;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (464);
    result = (*(uint64_t *)(v_rip + 0x994FA6)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 264, Arg4);
    local_r13 = 0;
    v_stack_m1D6 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1D0 = 0;
    result = KiAcquireThreadLockRaiseToDpc(Arg1, v_stack_m1D6, 264, Arg4);
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x7C))) == v_stack_p10) goto loc_00475C38;
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0047598E;
    Arg4 = 0;
    Arg3 = 0;
    result = KiEndThreadCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_00475C41;
loc_0047582F:
    Arg3 = 0;
    *(uint8_t *)(arg1 + 0x7C) = (uint8_t)((uint32_t)(v_stack_p10));
    result = KiStartThreadCycleAccumulation(*(uint64_t *)(gs_base + (0 + 0x20)), Arg1, Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00475C10;
loc_00475859:
    result = KiComputeThreadQos(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    if (((uint32_t)(result)) == ((uint32_t)(*(uint8_t *)(arg1 + 0x204)))) goto loc_00475913;
    v_stack_m170 = v_xmm0;
    v_stack_m1C8 = *(uint64_t *)(gs_base + (0 + 0x20));
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(gs_base + (0 + 0x20)), 1, v_stack_m1D0, Arg4);
    *(uint8_t *)(arg1 + 0x204) = (uint8_t)((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10)) != 0) goto loc_004758FA;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) >> (1));
    v_stack_m1B8 = *(uint64_t *)(gs_base + (0 + 0x20));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (condition_is_equal) goto loc_00475ADC;
    if (((uint32_t)(Arg1)) != 1) goto loc_004758FA;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58))) == 0) goto loc_004758FA;
loc_004758C9:
loc_004758CC:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8) + 0x38) + 0x40))) ^ (*(uint8_t *)(arg1 + 0x204)));
    Arg1 = (uint8_t)((Arg1) & (7));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8) + 0x38) + 0x40))));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8) + 0x38) + 0x40) = (uint8_t)(Arg1);
    result = KiUpdateThreadQosGroupingSummaries(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8) + 0x38), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8), Arg4);
    local_r13 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_004758CC;
loc_004758FA:
    Arg4 = 0;
    v_stack_m1E8 = v_stack_m170;
    result = KiReleaseThreadStateLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m1D0, Arg4);
loc_00475913:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m1D0, Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 4) goto loc_00475CDC;
loc_00475922:
    *(uint64_t *)(arg1 + 0x40) = 0;
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8E58) + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m1D0, Arg4);
    if (0 != 0) goto loc_00475D01;
loc_00475938:
    if (0 != 0) goto loc_00475D13;
loc_00475941:
    local_r13 = 0;
loc_00475944:
    if ((*(uint32_t *)(v_rip + 0xB513D5)) != 0) {
        Arg1 = v_cr8;
        Arg2 = v_stack_m1D6;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m1D0, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1D0, Arg4);
    local_rsp = (local_rsp) + (464);
    return result;
loc_0047598E:
    v_stack_p30 = 0;
    v_stack_p20 = v_stack_p68;
    v_stack_p68 = v_xmm0;
    result = KiAcquireThreadStateLockForWrite(Arg1, v_stack_p40, v_stack_p38, v_stack_p48);
    v_stack_p31 = (uint8_t)(result);
    if (((uint8_t)(result)) == ((uint8_t)(1 + 1))) goto loc_00475AE8;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x71)) != 0) goto loc_00475AE8;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_00475C4B;
loc_004759F3:
    *(uint8_t *)(arg1 + 0x7C) = (uint8_t)((uint32_t)(v_stack_p10));
loc_004759F6:
    result = KiComputeThreadQos(Arg1, v_stack_p40, v_stack_p38, v_stack_p48);
    if (((uint32_t)(result)) == ((uint32_t)(*(uint8_t *)(arg1 + 0x204)))) goto loc_00475A8E;
    *(uint8_t *)(arg1 + 0x204) = (uint8_t)((uint32_t)((uint32_t)(result)));
    Arg2 = (uint32_t)((v_stack_p31) - ((uint32_t)(1 + 1)));
    if (condition_is_not_equal) goto loc_00475C55;
    if ((*(uint64_t *)(v_stack_p40 + 0x10)) != 0) goto loc_00475A8E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) >> (1));
    v_stack_p60 = v_stack_p40;
    Arg1 = (uint32_t)((Arg1) & (1));
    if (condition_is_equal) goto loc_00475BC6;
    if (((uint32_t)(Arg1)) != 1) goto loc_00475A8E;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58))) == 0) goto loc_00475A8B;
loc_00475A54:
loc_00475A57:
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8) + 0x38) + 0x40))) ^ (*(uint8_t *)(arg1 + 0x204)));
    Arg2 = (uint8_t)((Arg2) & (7));
    Arg2 = (uint8_t)((Arg2) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8) + 0x38) + 0x40))));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8) + 0x38) + 0x40) = (uint8_t)(Arg2);
    result = KiUpdateThreadQosGroupingSummaries(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8), Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8) + 0x38), v_stack_p48);
    local_r13 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_00475A57;
loc_00475A81:
    local_r13 = 0;
    goto loc_00475A8E;
loc_00475A8B:
loc_00475A8E:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8), Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8) + 0x38), v_stack_p48);
    if (v_stack_p31 == ((uint8_t)(1 + 1))) goto loc_00475BD2;
loc_00475A9E:
    v_stack_p20 = v_stack_p68;
    result = KiReleaseThreadStateLock(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8), v_stack_p40, v_stack_p38, v_stack_p48);
    *(uint64_t *)(arg1 + 0x40) = 0;
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(*(uint64_t *)(*(uint64_t *)(v_stack_p40 + 0x8E58) + 0x8), v_stack_p40, v_stack_p38, v_stack_p48);
    if (0 == 0) goto loc_00475944;
    result = KiSendSoftwareInterrupt((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x24)), (uint8_t)(1 + 1), v_stack_p38, v_stack_p48);
    goto loc_00475944;
loc_00475ADC:
    goto loc_004758C9;
loc_00475AE8:
    Arg2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, Arg2, 256, v_stack_p48);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAAD69E) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAAD69E) + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 4))))) >> (6));
    if (((uint32_t)(v_stack_m158)) <= ((uint32_t)(Arg1))) goto loc_00475CC4;
loc_00475B2C:
    *(uint64_t *)(v_stack_m108 + (uint32_t)((uint32_t)(arg1)) * 8 - 0x48) = *(uint64_t *)(v_stack_m108 + arg1 * 8 - 0x48);
loc_00475B3F:
    if ((*(uint32_t *)(v_rip + 0xB511CD)) != 0) goto loc_00475C06;
loc_00475B59:
    v_stack_m188 = v_stack_p10;
    v_stack_p78 = Arg1;
    v_stack_m178 = v_rip - 859033;
    Arg2 = 0;
    v_stack_m180 = 0;
    v_stack_p20 = 5;
    result = KiIpiSendRequest(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, v_stack_m158, v_stack_p78);
    result = KiIpiStallOnPacketTargetsPrcb(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m158, v_stack_p78);
    if ((*(uint32_t *)(v_rip + 0xB51171)) != 0) {
        Arg1 = 12;
        Arg2 = (uint8_t)(1 + 1);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m158, v_stack_p78);
    }
    goto loc_004759F6;
loc_00475BC6:
    goto loc_00475A54;
loc_00475BD2:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 4) goto loc_00475A9E;
    result = KiCheckPreferredHeteroProcessor(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x218)), 1, v_stack_p78);
    if ((*(uint32_t *)(v_rip + 0xB5107B)) == 0) goto loc_00475D23;
loc_00475BF7:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x218)) + 0x38B9) = 1;
    goto loc_00475A9E;
loc_00475C06:
    result = KiRaiseIrqlProcessIrqlFlags(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x218)), 1, v_stack_p78);
    goto loc_00475B59;
loc_00475C10:
loc_00475C15:
    if ((*(uint32_t *)(v_rip + 0xB5107B)) != 0) goto loc_00475C15;
    if ((*(uint32_t *)(v_rip + 0xB5107B)) >= 0) goto loc_00475859;
    result = KiRemoveSystemWorkPriorityKick(1, (uint32_t)(*(uint32_t *)(arg1 + 0x218)), 1, v_stack_p78);
    goto loc_00475859;
loc_00475C38:
    *(uint64_t *)(arg1 + 0x40) = 0;
    goto loc_00475944;
loc_00475C41:
    goto loc_0047582F;
loc_00475C4B:
    goto loc_004759F3;
loc_00475C55:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) != 1) goto loc_00475A8E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) >> (1));
    v_stack_p58 = (uint32_t)(*(uint32_t *)(arg1 + 0x218));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (condition_is_equal) goto loc_00475C8B;
    if (((uint32_t)(Arg1)) != 1) goto loc_00475A8E;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x218)) + 0x8E58))) == 0) goto loc_00475A8B;
    goto loc_00475C92;
loc_00475C8B:
loc_00475C92:
loc_00475C95:
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x38) + 0x40))) ^ (*(uint8_t *)(arg1 + 0x204)));
    Arg2 = (uint8_t)((Arg2) & (7));
    Arg2 = (uint8_t)((Arg2) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x38) + 0x40))));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x38) + 0x40) = (uint8_t)(Arg2);
    result = KiUpdateThreadQosGroupingSummaries(*(uint64_t *)(v_stack_p58), Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x38), v_stack_p78);
    local_r13 = (1) - (1);
    if (condition_is_not_equal) goto loc_00475C95;
    goto loc_00475A81;
loc_00475CC4:
    if (((uint32_t)(v_stack_m156)) <= ((uint32_t)(*(uint64_t *)(v_stack_p58)))) goto loc_00475B3F;
    v_stack_m158 = (uint16_t)(1 + *(uint64_t *)(v_stack_p58) * 1);
    goto loc_00475B2C;
loc_00475CDC:
    result = KiCheckPreferredHeteroProcessor(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x218)), 1, v_stack_p78);
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x218)) + 0x38B9) = 1;
    goto loc_00475922;
loc_00475D01:
    result = KiSendSoftwareInterrupt((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x218)) + 0x24)), 2, 1, v_stack_p78);
    goto loc_00475938;
loc_00475D13:
    result = KeCheckAndApplyBamQos((uint32_t)(*(uint32_t *)(arg1 + 0x218)), Arg1, 1, v_stack_p78);
    goto loc_00475941;
loc_00475D23:
    if ((uint32_t)(result) == 0) goto loc_00475A9E;
    goto loc_00475BF7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x7C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00475770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
