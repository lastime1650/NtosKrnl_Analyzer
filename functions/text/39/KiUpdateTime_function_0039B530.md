# KiUpdateTime

- RVA: `0x0039B530`–`0x0039BB5F` (길이 `1,583` bytes)
- VA: `0x000000014039B530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000818FC`
- 디코드: `345`개 명령, `1,583/1,583` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **43**

### Outgoing calls
- `0x0039B584` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039B5A7` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039B5CC` → [RtlBeginReadTickLock](RtlBeginReadTickLock_function_0039D2A0.md) (function, `0x0039D2A0`)
- `0x0039B5D6` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0039B5E3` → [KiComputeNewInterruptTime](KiComputeNewInterruptTime_function_0039D330.md) (function, `0x0039D330`)
- `0x0039B612` → [RtlWriteTryAcquireTickLock](RtlWriteTryAcquireTickLock_function_0039D3D8.md) (function, `0x0039D3D8`)
- `0x0039B631` → [RtlWriteAcquireTickLock](RtlWriteAcquireTickLock_function_0039D3B4.md) (function, `0x0039D3B4`)
- `0x0039B638` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0039B643` → [KiComputeNewSystemTime](KiComputeNewSystemTime_function_0039D2B8.md) (function, `0x0039D2B8`)
- `0x0039B658` → [KiComputeNewInterruptTime](KiComputeNewInterruptTime_function_0039D330.md) (function, `0x0039D330`)
- `0x0039B7CA` → [Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline](Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline_function_0039CEE8.md) (function, `0x0039CEE8`)
- `0x0039B843` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039B873` → [PoExecuteIdleCheck](PoExecuteIdleCheck_function_0039CF20.md) (function, `0x0039CF20`)
- `0x0039B886` → [PpmExecutePeriodicPerfCheck](PpmExecutePeriodicPerfCheck_function_0039D0CC.md) (function, `0x0039D0CC`)
- `0x0039B8BB` → [KiUpdateRunTime](KiUpdateRunTime_function_0039BB70.md) (function, `0x0039BB70`)
- `0x0039B8CA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0039B980` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0039B99A` → [KiForwardTick](KiForwardTick_function_0039D40C.md) (function, `0x0039D40C`)
- `0x0039B9B9` → [KiOrAffinityEx](KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x0039B9CA` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039BA00` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0039BA5F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039BA6E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0039BA96` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039BADB` → [KiSetForceIdleState](../48/KiSetForceIdleState_function_0048DCC0.md) (function, `0x0048DCC0`)
- `0x0039BB0F` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0039BB52` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)

### Direct callers
- [KeClockInterruptNotify](KeClockInterruptNotify_function_0039A970.md) at `0x0039AC2A`

### Static image references
- `0x0039B557` → RVA `0x00E0A740` (`.data`; read)
- `0x0039B5AC` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x0039B5E8` → RVA `0x00FC6AF8` (`ALMOSTRO`; read)
- `0x0039B602` → RVA `0x00FC7058` (`ALMOSTRO`; read)
- `0x0039B6BB` → RVA `0x00E66898` (`.data`; read)
- `0x0039B6DB` → RVA `0x00E66898` (`.data`; write)
- `0x0039B6F0` → RVA `0x00F23140` (`.data`; read/write)
- `0x0039B6FE` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0039B70C` → RVA `0x00F23140` (`.data`; read)
- `0x0039B71A` → RVA `0x00F23148` (`.data`; read)
- `0x0039B72A` → RVA `0x00F233CC` (`.data`; read)
- `0x0039B74F` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x0039B757` → RVA `0x00E668B0` (`.data`; read)
- `0x0039B761` → RVA `0x00FC6BEC` (`ALMOSTRO`; read)
- `0x0039B76B` → RVA `0x00E668B0` (`.data`; write)
- `0x0039B77A` → RVA `0x00E668A8` (`.data`; read)
- `0x0039B784` → RVA `0x00FC6BB8` (`ALMOSTRO`; read)
- `0x0039B78E` → RVA `0x00E668A8` (`.data`; write)
- `0x0039B795` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x0039B7AF` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0039B7DF` → RVA `0x00FC6AA5` (`ALMOSTRO`; read)
- `0x0039B7F9` → RVA `0x00E070D8` (`.data`; read)
- `0x0039B85A` → RVA `0x00F23158` (`.data`; read)
- `0x0039B87D` → RVA `0x00F0B3E8` (`.data`; read)
- `0x0039B88F` → RVA `0x00FC6ABC` (`ALMOSTRO`; read)
- `0x0039B89F` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x0039B937` → RVA `0x00F23150` (`.data`; read)
- `0x0039B947` → RVA `0x00FC6DB8` (`ALMOSTRO`; read)
- `0x0039B953` → RVA `0x00F23150` (`.data`; write)
- `0x0039B99F` → RVA `0x00E0AB72` (`.data`; read)
- `0x0039B9A7` → RVA `0x00E0AB70` (`.data`; read)
- `0x0039B9D4` → RVA `0x00F231A8` (`.data`; read/write)
- `0x0039B9DB` → RVA `0x00F23158` (`.data`; write)
- `0x0039B9E8` → RVA `0x00FC52A8` (`ALMOSTRO`; read)
- `0x0039B9EE` → RVA `0x00F23160` (`.data`; read)
- `0x0039B9F8` → RVA `0x00F231A8` (`.data`; write)
- `0x0039BA0A` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x0039BA51` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0039BAE8` → RVA `0x00F23138` (`.data`; read)
- `0x0039BAFC` → RVA `0x00F23102` (`.data`; write)
- `0x0039BB06` → RVA `0x00F23100` (`.data`; read)
- `0x0039BB19` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x0039BB29` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0039B800` → [sub_006E5BD0](../6E/Unknown_function_006E5BD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039B530  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039B535  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0039B53A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0039B53F  55                              push rbp
0039B540  41 54                           push r12
0039B542  41 55                           push r13
0039B544  41 56                           push r14
0039B546  41 57                           push r15
0039B548  48 8D AC 24 C0 FE FF FF         lea rbp, [rsp - 0x140]
0039B550  48 81 EC 40 02 00 00            sub rsp, 0x240
0039B557  48 8B 05 E2 F1 A6 00            mov rax, qword ptr [rip + 0xa6f1e2]
0039B55E  48 33 C4                        xor rax, rsp
0039B561  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
0039B568  45 8B E0                        mov r12d, r8d
0039B56B  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
0039B570  88 54 24 32                     mov byte ptr [rsp + 0x32], dl
0039B574  41 B8 08 01 00 00               mov r8d, 0x108
0039B57A  88 4C 24 33                     mov byte ptr [rsp + 0x33], cl
0039B57E  33 D2                           xor edx, edx
0039B580  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0039B584  E8 B7 B6 32 00                  call 0x1406c6c40
0039B589  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0039B592  48 BE 20 03 00 00 80 F7 FF FF   movabs rsi, 0xfffff78000000320
0039B59C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0039B5A1  45 32 ED                        xor r13b, r13b
0039B5A4  48 8B 06                        mov rax, qword ptr [rsi]
0039B5A7  E8 34 C6 E7 FF                  call 0x140217be0
0039B5AC  4C 8B 35 55 9A C2 00            mov r14, qword ptr [rip + 0xc29a55]
0039B5B3  32 DB                           xor bl, bl
0039B5B5  49 81 C6 40 03 00 00            add r14, 0x340
0039B5BC  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
0039B5C5  44 0F B6 F8                     movzx r15d, al
0039B5C9  49 8B CE                        mov rcx, r14
0039B5CC  E8 CF 1C 00 00                  call 0x14039d2a0
0039B5D1  33 C9                           xor ecx, ecx
0039B5D3  48 8B F8                        mov rdi, rax
0039B5D6  E8 05 32 FE FF                  call 0x14037e7e0
0039B5DB  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0039B5E0  48 8B C8                        mov rcx, rax
0039B5E3  E8 48 1D 00 00                  call 0x14039d330
0039B5E8  38 1D 0A B5 C2 00               cmp byte ptr [rip + 0xc2b50a], bl
0039B5EE  90                              nop
0039B5EF  0F 84 B5 04 00 00               je 0x14039baaa
0039B5F5  49 8B 0E                        mov rcx, qword ptr [r14]
0039B5F8  48 3B CF                        cmp rcx, rdi
0039B5FB  75 CC                           jne 0x14039b5c9
0039B5FD  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0039B602  4C 3B 0D 4F BA C2 00            cmp r9, qword ptr [rip + 0xc2ba4f]
0039B609  0F 86 EF 02 00 00               jbe 0x14039b8fe
0039B60F  49 8B CE                        mov rcx, r14
0039B612  E8 C1 1D 00 00                  call 0x14039d3d8
0039B617  84 C0                           test al, al
0039B619  74 AE                           je 0x14039b5c9
0039B61B  B3 01                           mov bl, 1
0039B61D  44 38 2D D4 B4 C2 00            cmp byte ptr [rip + 0xc2b4d4], r13b
0039B624  0F 84 C7 02 00 00               je 0x14039b8f1
0039B62A  84 DB                           test bl, bl
0039B62C  75 08                           jne 0x14039b636
0039B62E  49 8B CE                        mov rcx, r14
0039B631  E8 7E 1D 00 00                  call 0x14039d3b4
0039B636  33 C9                           xor ecx, ecx
0039B638  E8 A3 31 FE FF                  call 0x14037e7e0
0039B63D  48 8B C8                        mov rcx, rax
0039B640  48 8B F0                        mov rsi, rax
0039B643  E8 70 1C 00 00                  call 0x14039d2b8
0039B648  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0039B64D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0039B652  48 8B CE                        mov rcx, rsi
0039B655  48 8B F8                        mov rdi, rax
0039B658  E8 D3 1C 00 00                  call 0x14039d330
0039B65D  48 8B 15 A4 99 C2 00            mov rdx, qword ptr [rip + 0xc299a4]
0039B664  48 8B D8                        mov rbx, rax
0039B667  8B 4C 24 3C                     mov ecx, dword ptr [rsp + 0x3c]
0039B66B  48 C1 E8 20                     shr rax, 0x20
0039B66F  89 4A 1C                        mov dword ptr [rdx + 0x1c], ecx
0039B672  48 8B 0D 8F 99 C2 00            mov rcx, qword ptr [rip + 0xc2998f]
0039B679  48 89 79 14                     mov qword ptr [rcx + 0x14], rdi
0039B67D  48 8B 0D 84 99 C2 00            mov rcx, qword ptr [rip + 0xc29984]
0039B684  89 41 10                        mov dword ptr [rcx + 0x10], eax
0039B687  48 8B 05 7A 99 C2 00            mov rax, qword ptr [rip + 0xc2997a]
0039B68E  48 89 58 08                     mov qword ptr [rax + 8], rbx
0039B692  48 8B 05 6F 99 C2 00            mov rax, qword ptr [rip + 0xc2996f]
0039B699  48 89 B0 48 03 00 00            mov qword ptr [rax + 0x348], rsi
0039B6A0  48 8B 05 61 99 C2 00            mov rax, qword ptr [rip + 0xc29961]
0039B6A7  48 89 B0 50 03 00 00            mov qword ptr [rax + 0x350], rsi
0039B6AE  48 BE 20 03 00 00 80 F7 FF FF   movabs rsi, 0xfffff78000000320
0039B6B8  48 8B 36                        mov rsi, qword ptr [rsi]
0039B6BB  44 8B 05 D6 B1 AC 00            mov r8d, dword ptr [rip + 0xacb1d6]
0039B6C2  4C 2B 44 24 40                  sub r8, qword ptr [rsp + 0x40]
0039B6C7  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0039B6CC  4D 85 C0                        test r8, r8
0039B6CF  0F 8E 35 03 00 00               jle 0x14039ba0a
0039B6D5  49 8B 06                        mov rax, qword ptr [r14]
0039B6D8  48 FF C0                        inc rax
0039B6DB  44 89 05 B6 B1 AC 00            mov dword ptr [rip + 0xacb1b6], r8d
0039B6E2  49 89 06                        mov qword ptr [r14], rax
0039B6E5  33 FF                           xor edi, edi
0039B6E7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0039B6F0  F0 48 0F BA 2D 46 7A B8 00 00   lock bts qword ptr [rip + 0xb87a46], 0
0039B6FA  73 1E                           jae 0x14039b71a
0039B6FC  FF C7                           inc edi
0039B6FE  85 3D A8 9B C2 00               test dword ptr [rip + 0xc29ba8], edi
0039B704  0F 84 47 03 00 00               je 0x14039ba51
0039B70A  F3 90                           pause
0039B70C  48 8B 05 2D 7A B8 00            mov rax, qword ptr [rip + 0xb87a2d]
0039B713  48 85 C0                        test rax, rax
0039B716  74 D8                           je 0x14039b6f0
0039B718  EB E2                           jmp 0x14039b6fc
0039B71A  48 8B 05 27 7A B8 00            mov rax, qword ptr [rip + 0xb87a27]
0039B721  48 85 C0                        test rax, rax
0039B724  0F 85 96 03 00 00               jne 0x14039bac0
0039B72A  8B 05 9C 7C B8 00               mov eax, dword ptr [rip + 0xb87c9c]
0039B730  FF C8                           dec eax
0039B732  A9 FD FF FF FF                  test eax, 0xfffffffd
0039B737  0F 84 08 04 00 00               je 0x14039bb45
0039B73D  F0 48 83 25 FA 79 B8 00 00      lock and qword ptr [rip + 0xb879fa], 0
0039B746  45 84 FF                        test r15b, r15b
0039B749  0F 85 C9 01 00 00               jne 0x14039b918
0039B74F  8B 05 E7 B3 C2 00               mov eax, dword ptr [rip + 0xc2b3e7]
0039B755  8B CB                           mov ecx, ebx
0039B757  2B 0D 53 B1 AC 00               sub ecx, dword ptr [rip + 0xacb153]
0039B75D  FF C8                           dec eax
0039B75F  03 C8                           add ecx, eax
0039B761  8B 05 85 B4 C2 00               mov eax, dword ptr [rip + 0xc2b485]
0039B767  3B C8                           cmp ecx, eax
0039B769  72 07                           jb 0x14039b772
0039B76B  48 89 1D 3E B1 AC 00            mov qword ptr [rip + 0xacb13e], rbx
0039B772  8B 05 C4 B3 C2 00               mov eax, dword ptr [rip + 0xc2b3c4]
0039B778  8B CB                           mov ecx, ebx
0039B77A  2B 0D 28 B1 AC 00               sub ecx, dword ptr [rip + 0xacb128]
0039B780  FF C8                           dec eax
0039B782  03 C8                           add ecx, eax
0039B784  8B 05 2E B4 C2 00               mov eax, dword ptr [rip + 0xc2b42e]
0039B78A  3B C8                           cmp ecx, eax
0039B78C  72 07                           jb 0x14039b795
0039B78E  48 89 1D 13 B1 AC 00            mov qword ptr [rip + 0xacb113], rbx
0039B795  80 3D E9 B2 C2 00 00            cmp byte ptr [rip + 0xc2b2e9], 0
0039B79C  0F 84 FE 02 00 00               je 0x14039baa0
0039B7A2  44 0F 20 C6                     mov rsi, cr8
0039B7A6  B8 0F 00 00 00                  mov eax, 0xf
0039B7AB  44 0F 22 C0                     mov cr8, rax
0039B7AF  83 3D 6A B5 C2 00 00            cmp dword ptr [rip + 0xc2b56a], 0
0039B7B6  0F 85 07 02 00 00               jne 0x14039b9c3
0039B7BC  4C 63 3D F5 B3 C2 00            movsxd r15, dword ptr [rip + 0xc2b3f5]
0039B7C3  4C 03 3D DE B0 AC 00            add r15, qword ptr [rip + 0xacb0de]
0039B7CA  E8 19 17 00 00                  call 0x14039cee8
0039B7CF  44 8B 25 66 B3 C2 00            mov r12d, dword ptr [rip + 0xc2b366]
0039B7D6  85 C0                           test eax, eax
0039B7D8  48 8B CB                        mov rcx, rbx
0039B7DB  41 0F 94 C6                     sete r14b
0039B7DF  80 3D BF B2 C2 00 00            cmp byte ptr [rip + 0xc2b2bf], 0
0039B7E6  0F 84 61 03 00 00               je 0x14039bb4d
0039B7EC  48 8B F9                        mov rdi, rcx
0039B7EF  49 2B FF                        sub rdi, r15
0039B7F2  4D 85 FF                        test r15, r15
0039B7F5  49 0F 4F FF                     cmovg rdi, r15
0039B7F9  83 3D D8 B8 A6 00 05            cmp dword ptr [rip + 0xa6b8d8], 5
0039B800  0F 87 CA A3 34 00               ja 0x1406e5bd0
0039B806  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0039B80B  45 02 F6                        add r14b, r14b
0039B80E  41 0F B6 87 B4 95 00 00         movzx eax, byte ptr [r15 + 0x95b4]
0039B816  24 FD                           and al, 0xfd
0039B818  49 89 BF A8 95 00 00            mov qword ptr [r15 + 0x95a8], rdi
0039B81F  41 0A C6                        or al, r14b
0039B822  45 89 A7 B0 95 00 00            mov dword ptr [r15 + 0x95b0], r12d
0039B829  0C 01                           or al, 1
0039B82B  41 88 87 B4 95 00 00            mov byte ptr [r15 + 0x95b4], al
0039B832  83 3D E7 B4 C2 00 00            cmp dword ptr [rip + 0xc2b4e7], 0
0039B839  74 0D                           je 0x14039b848
0039B83B  44 0F 20 C1                     mov rcx, cr8
0039B83F  40 0F B6 D6                     movzx edx, sil
0039B843  E8 50 9E 15 00                  call 0x1404f5698
0039B848  40 0F B6 C6                     movzx eax, sil
0039B84C  44 0F 22 C0                     mov cr8, rax
0039B850  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0039B855  44 8B 64 24 50                  mov r12d, dword ptr [rsp + 0x50]
0039B85A  48 3B 35 F7 78 B8 00            cmp rsi, qword ptr [rip + 0xb878f7]
0039B861  0F 87 6D 01 00 00               ja 0x14039b9d4
0039B867  80 3D 17 B2 C2 00 00            cmp byte ptr [rip + 0xc2b217], 0
0039B86E  75 08                           jne 0x14039b878
0039B870  48 8B CB                        mov rcx, rbx
0039B873  E8 A8 16 00 00                  call 0x14039cf20
0039B878  45 84 ED                        test r13b, r13b
0039B87B  75 0E                           jne 0x14039b88b
0039B87D  83 3D 64 FB B6 00 00            cmp dword ptr [rip + 0xb6fb64], 0
0039B884  75 05                           jne 0x14039b88b
0039B886  E8 41 18 00 00                  call 0x14039d0cc
0039B88B  48 C1 EB 12                     shr rbx, 0x12
0039B88F  80 3D 26 B2 C2 00 00            cmp byte ptr [rip + 0xc2b226], 0
0039B896  0F 85 9B 00 00 00               jne 0x14039b937
0039B89C  40 32 F6                        xor sil, sil
0039B89F  8B 3D DB B1 C2 00               mov edi, dword ptr [rip + 0xc2b1db]
0039B8A5  83 FF 01                        cmp edi, 1
0039B8A8  0F 87 B1 00 00 00               ja 0x14039b95f
0039B8AE  0F B6 54 24 32                  movzx edx, byte ptr [rsp + 0x32]
0039B8B3  45 8B C4                        mov r8d, r12d
0039B8B6  0F B6 4C 24 33                  movzx ecx, byte ptr [rsp + 0x33]
0039B8BB  E8 B0 02 00 00                  call 0x14039bb70
0039B8C0  48 8B 8D 30 01 00 00            mov rcx, qword ptr [rbp + 0x130]
0039B8C7  48 33 CC                        xor rcx, rsp
0039B8CA  E8 71 0D 31 00                  call 0x1406ac640
0039B8CF  4C 8D 9C 24 40 02 00 00         lea r11, [rsp + 0x240]
0039B8D7  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0039B8DB  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0039B8DF  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0039B8E3  49 8B E3                        mov rsp, r11
0039B8E6  41 5F                           pop r15
0039B8E8  41 5E                           pop r14
0039B8EA  41 5D                           pop r13
0039B8EC  41 5C                           pop r12
0039B8EE  5D                              pop rbp
0039B8EF  C3                              ret
0039B8F0  CC                              int3
0039B8F1  4C 3B 0D 60 B7 C2 00            cmp r9, qword ptr [rip + 0xc2b760]
0039B8F8  0F 87 30 FD FF FF               ja 0x14039b62e
0039B8FE  48 BB 08 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000008
0039B908  48 8B 1B                        mov rbx, qword ptr [rbx]
0039B90B  48 8B 36                        mov rsi, qword ptr [rsi]
0039B90E  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0039B913  E9 CD FD FF FF                  jmp 0x14039b6e5
0039B918  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039B921  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039B928  4D 85 C0                        test r8, r8
0039B92B  0F 85 47 01 00 00               jne 0x14039ba78
0039B931  FB                              sti
0039B932  E9 18 FE FF FF                  jmp 0x14039b74f
0039B937  48 8B 0D 12 78 B8 00            mov rcx, qword ptr [rip + 0xb87812]
0039B93E  48 3B F1                        cmp rsi, rcx
0039B941  0F 86 55 FF FF FF               jbe 0x14039b89c
0039B947  8B 05 6B B4 C2 00               mov eax, dword ptr [rip + 0xc2b46b]
0039B94D  40 B6 01                        mov sil, 1
0039B950  48 03 C8                        add rcx, rax
0039B953  48 89 0D F6 77 B8 00            mov qword ptr [rip + 0xb877f6], rcx
0039B95A  E9 40 FF FF FF                  jmp 0x14039b89f
0039B95F  80 3D 1F B1 C2 00 00            cmp byte ptr [rip + 0xc2b11f], 0
0039B966  0F 85 42 FF FF FF               jne 0x14039b8ae
0039B96C  33 D2                           xor edx, edx
0039B96E  48 C7 45 80 01 00 20 00         mov qword ptr [rbp - 0x80], 0x200001
0039B976  41 B8 00 01 00 00               mov r8d, 0x100
0039B97C  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0039B980  E8 BB B2 32 00                  call 0x1406c6c40
0039B985  48 8D 45 80                     lea rax, [rbp - 0x80]
0039B989  44 0F B6 CE                     movzx r9d, sil
0039B98D  4C 8B C3                        mov r8, rbx
0039B990  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0039B995  8B D7                           mov edx, edi
0039B997  49 8B CF                        mov rcx, r15
0039B99A  E8 6D 1A 00 00                  call 0x14039d40c
0039B99F  44 0F B7 0D CB F1 A6 00         movzx r9d, word ptr [rip + 0xa6f1cb]
0039B9A7  4C 8D 05 C2 F1 A6 00            lea r8, [rip + 0xa6f1c2]
0039B9AE  48 8D 55 80                     lea rdx, [rbp - 0x80]
0039B9B2  48 8D 0D B7 F1 A6 00            lea rcx, [rip + 0xa6f1b7]
0039B9B9  E8 8E EE FF FF                  call 0x14039a84c
0039B9BE  E9 EB FE FF FF                  jmp 0x14039b8ae
0039B9C3  0F B6 D0                        movzx edx, al
0039B9C6  40 0F B6 CE                     movzx ecx, sil
0039B9CA  E8 2D 9D 15 00                  call 0x1404f56fc
0039B9CF  E9 E8 FD FF FF                  jmp 0x14039b7bc
0039B9D4  83 05 CD 77 B8 00 FF            add dword ptr [rip + 0xb877cd], -1
0039B9DB  48 89 35 76 77 B8 00            mov qword ptr [rip + 0xb87776], rsi
0039B9E2  0F 85 7F FE FF FF               jne 0x14039b867
0039B9E8  8B 05 BA 98 C2 00               mov eax, dword ptr [rip + 0xc298ba]
0039B9EE  48 8D 0D 6B 77 B8 00            lea rcx, [rip + 0xb8776b]
0039B9F5  45 33 C0                        xor r8d, r8d
0039B9F8  89 05 AA 77 B8 00               mov dword ptr [rip + 0xb877aa], eax
0039B9FE  33 D2                           xor edx, edx
0039BA00  E8 4B C2 E6 FF                  call 0x140207c50
0039BA05  E9 5D FE FF FF                  jmp 0x14039b867
0039BA0A  44 8B 0D 8F B0 C2 00            mov r9d, dword ptr [rip + 0xc2b08f]
0039BA11  BA 01 00 00 00                  mov edx, 1
0039BA16  4D 03 C1                        add r8, r9
0039BA19  4D 85 C0                        test r8, r8
0039BA1C  0F 8E F7 00 00 00               jle 0x14039bb19
0039BA22  48 8B 0D DF 95 C2 00            mov rcx, qword ptr [rip + 0xc295df]
0039BA29  48 03 F2                        add rsi, rdx
0039BA2C  48 8B C6                        mov rax, rsi
0039BA2F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0039BA34  48 C1 E8 20                     shr rax, 0x20
0039BA38  89 81 28 03 00 00               mov dword ptr [rcx + 0x328], eax
0039BA3E  48 8B 05 C3 95 C2 00            mov rax, qword ptr [rip + 0xc295c3]
0039BA45  48 89 B0 20 03 00 00            mov qword ptr [rax + 0x320], rsi
0039BA4C  E9 84 FC FF FF                  jmp 0x14039b6d5
0039BA51  8B 05 61 B0 C2 00               mov eax, dword ptr [rip + 0xc2b061]
0039BA57  A8 40                           test al, 0x40
0039BA59  0F 84 AB FC FF FF               je 0x14039b70a
0039BA5F  E8 2C 3A F7 FF                  call 0x14030f490
0039BA64  84 C0                           test al, al
0039BA66  0F 84 9E FC FF FF               je 0x14039b70a
0039BA6C  8B CF                           mov ecx, edi
0039BA6E  E8 ED 39 F7 FF                  call 0x14030f460
0039BA73  E9 94 FC FF FF                  jmp 0x14039b70c
0039BA78  41 0F 0D 08                     prefetchw byte ptr [r8]
0039BA7C  41 8B 00                        mov eax, dword ptr [r8]
0039BA7F  8B D0                           mov edx, eax
0039BA81  0F BA F2 15                     btr edx, 0x15
0039BA85  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039BA8A  75 F3                           jne 0x14039ba7f
0039BA8C  0F BA E0 15                     bt eax, 0x15
0039BA90  0F 83 9B FE FF FF               jae 0x14039b931
0039BA96  E8 35 77 EC FF                  call 0x1402631d0
0039BA9B  E9 91 FE FF FF                  jmp 0x14039b931
0039BAA0  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0039BAA5  E9 B0 FD FF FF                  jmp 0x14039b85a
0039BAAA  49 8B 06                        mov rax, qword ptr [r14]
0039BAAD  48 3B C7                        cmp rax, rdi
0039BAB0  0F 85 13 FB FF FF               jne 0x14039b5c9
0039BAB6  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0039BABB  E9 5D FB FF FF                  jmp 0x14039b61d
0039BAC0  48 3B D8                        cmp rbx, rax
0039BAC3  0F 82 61 FC FF FF               jb 0x14039b72a
0039BAC9  8B 05 FD 78 B8 00               mov eax, dword ptr [rip + 0xb878fd]
0039BACF  83 F8 02                        cmp eax, 2
0039BAD2  0F 85 52 FC FF FF               jne 0x14039b72a
0039BAD8  8D 48 FF                        lea ecx, [rax - 1]
0039BADB  E8 E0 21 0F 00                  call 0x14048dcc0
0039BAE0  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0039BAE5  8B 48 24                        mov ecx, dword ptr [rax + 0x24]
0039BAE8  48 8B 05 49 76 B8 00            mov rax, qword ptr [rip + 0xb87649]
0039BAEF  48 85 C0                        test rax, rax
0039BAF2  75 0F                           jne 0x14039bb03
0039BAF4  B8 00 08 00 00                  mov eax, 0x800
0039BAF9  66 03 C8                        add cx, ax
0039BAFC  66 89 0D FF 75 B8 00            mov word ptr [rip + 0xb875ff], cx
0039BB03  45 33 C0                        xor r8d, r8d
0039BB06  48 8D 0D F3 75 B8 00            lea rcx, [rip + 0xb875f3]
0039BB0D  33 D2                           xor edx, edx
0039BB0F  E8 3C C1 E6 FF                  call 0x140207c50
0039BB14  E9 11 FC FF FF                  jmp 0x14039b72a
0039BB19  48 8B 05 F8 B7 C2 00            mov rax, qword ptr [rip + 0xc2b7f8]
0039BB20  49 8B C8                        mov rcx, r8
0039BB23  48 F7 D9                        neg rcx
0039BB26  48 F7 E1                        mul rcx
0039BB29  0F B6 0D 96 B0 C2 00            movzx ecx, byte ptr [rip + 0xc2b096]
0039BB30  48 D3 EA                        shr rdx, cl
0039BB33  48 FF C2                        inc rdx
0039BB36  4C 0F AF CA                     imul r9, rdx
0039BB3A  4D 03 C1                        add r8, r9
0039BB3D  48 FF C2                        inc rdx
0039BB40  E9 DD FE FF FF                  jmp 0x14039ba22
0039BB45  41 B5 01                        mov r13b, 1
0039BB48  E9 F0 FB FF FF                  jmp 0x14039b73d
0039BB4D  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0039BB52  E8 69 E9 E6 FF                  call 0x14020a4c0
0039BB57  48 8B C8                        mov rcx, rax
0039BB5A  E9 8D FC FF FF                  jmp 0x14039b7ec
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiUpdateTime(unsigned __int8 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned __int64 v_stack_m230;
    unsigned __int8 v_stack_m235;
    unsigned __int8 v_stack_m236;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (576);
    result = (*(unsigned __int64 *)(v_rip + 10940898)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m218 = a3;
    v_stack_m236 = (unsigned __int8)(a2);
    v_stack_m235 = a1;
    a2 = 0;
    result = memset(v_stack_m1E8, a2, 264, a4);
    v_stack_m210 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_r13 = 0;
    result = KeDisableInterrupts(v_stack_m1E8, a2, 264, a4);
    v_rbx = 0;
    v_r14 = (*(unsigned __int64 *)(v_rip + 12753493)) + (832);
    v_stack_m228 = 0;
loc_0039B5C9:
    result = RtlBeginReadTickLock(v_r14, a2, 264, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, 264, a4);
    result = KiComputeNewInterruptTime(result, v_stack_m228, 264, a4);
    if ((*(unsigned __int8 *)(v_rip + 12760330)) == 0) goto loc_0039BAAA;
    if ((*(unsigned __int64 *)(v_r14)) != result) goto loc_0039B5C9;
    if (v_stack_m228 <= (*(unsigned __int64 *)(v_rip + 12761679))) goto loc_0039B8FE;
    result = RtlWriteTryAcquireTickLock(v_r14, v_stack_m228, 264, v_stack_m228);
    if ((unsigned __int8)(result) == 0) goto loc_0039B5C9;
loc_0039B61D:
    if ((*(unsigned __int8 *)(v_rip + 12760276)) == 0) goto loc_0039B8F1;
    if (1 == 0) {
        a1 = v_r14;
        result = RtlWriteAcquireTickLock(a1, v_stack_m228, 264, v_stack_m228);
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_stack_m228, 264, v_stack_m228);
    result = KiComputeNewSystemTime(result, v_stack_m228, 264, v_stack_m228);
    v_stack_m230 = result;
    result = KiComputeNewInterruptTime(result, v_stack_m228, 264, v_stack_m228);
    result = (result) >> (32);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12753316) + 28) = (unsigned int)((unsigned int)(v_stack_m22C));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12753295) + 20) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12753284) + 16) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12753274) + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12753263) + 840) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12753249) + 848) = result;
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11317718))) - (v_stack_m228);
    v_stack_m230 = *(unsigned __int64 *)(result);
    if (condition_is_less_or_equal) goto loc_0039BA0A;
loc_0039B6D5:
    result = (*(unsigned __int64 *)(v_r14)) + 1;
    *(unsigned int *)(v_rip + 11317686) = a3;
    *(unsigned __int64 *)(v_r14) = result;
loc_0039B6E5:
    v_rdi = 0;
loc_0039B6F0:
    if (condition_is_above_or_equal) goto loc_0039B71A;
loc_0039B6FC:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 12753832)) & ((unsigned int)(v_rdi))) == 0) goto loc_0039BA51;
loc_0039B70A:
loc_0039B70C:
    if (*(unsigned __int64 *)(v_rip + 12089901) == 0) goto loc_0039B6F0;
    goto loc_0039B6FC;
loc_0039B71A:
    if (*(unsigned __int64 *)(v_rip + 12089895) != 0) goto loc_0039BAC0;
loc_0039B72A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12090524))) - 1);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_0039BB45;
loc_0039B73D:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0039B918;
loc_0039B74F:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (*(unsigned int *)(v_rip + 11317587)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12760039))) - 1);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (a1 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12760197))))) {
        *(unsigned __int64 *)(v_rip + 11317566) = result;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (*(unsigned int *)(v_rip + 11317544)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12760004))) - 1);
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (a1 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12760110))))) {
        *(unsigned __int64 *)(v_rip + 11317523) = result;
    }
    if ((*(unsigned __int8 *)(v_rip + 12759785)) == 0) goto loc_0039BAA0;
    if ((*(unsigned int *)(v_rip + 12760426)) != 0) goto loc_0039B9C3;
loc_0039B7BC:
    v_r15 = ((int)(*(unsigned int *)(v_rip + 12760053))) + (*(unsigned __int64 *)(v_rip + 11317470));
    result = Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline(a1, *(unsigned __int64 *)(v_rip + 12753316), a3, v_stack_m228);
    v_r14 = ((unsigned int)(result) == 0) ? 1 : 0;
    if ((*(unsigned __int8 *)(v_rip + 12759743)) == 0) goto loc_0039BB4D;
loc_0039B7EC:
    v_rdi = (result) - (v_r15);
    if (condition_is_greater) { v_rdi = v_r15; }
    v_r14 = (unsigned __int8)((v_r14) + ((unsigned __int8)(v_r14)));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m210 + 38324)) & (253));
    *(unsigned __int64 *)(v_stack_m210 + 38312) = v_rdi;
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_r14)));
    *(unsigned int *)(v_stack_m210 + 38320) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12759910)));
    result = (unsigned __int8)((result) | (1));
    *(unsigned __int8 *)(v_stack_m210 + 38324) = (unsigned __int8)(result);
    if ((*(unsigned int *)(v_rip + 12760295)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, v_stack_m228);
    }
loc_0039B85A:
    if (v_stack_m230 > (*(unsigned __int64 *)(v_rip + 12089591))) goto loc_0039B9D4;
loc_0039B867:
    result = (unsigned __int8)(v_cr8);
    if ((*(unsigned __int8 *)(v_rip + 12759575)) == 0) {
        a1 = result;
        result = PoExecuteIdleCheck(a1, a2, a3, v_stack_m228);
    }
    if (0 != 0) goto loc_0039B88B;
    if ((*(unsigned int *)(v_rip + 11991908)) == 0) {
        result = PpmExecutePeriodicPerfCheck(a1, a2, a3, v_stack_m228);
    }
    v_rbx = (result) >> (18);
    if ((*(unsigned __int8 *)(v_rip + 12759590)) != 0) goto loc_0039B937;
loc_0039B89C:
    v_rsi = 0;
loc_0039B89F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12759515)))) > 1) goto loc_0039B95F;
loc_0039B8AE:
    result = KiUpdateRunTime(v_stack_m235, v_stack_m236, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), v_stack_m228);
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m236, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), v_stack_m228);
    return result;
loc_0039B8F1:
    if (v_stack_m228 > (*(unsigned __int64 *)(v_rip + 12760928))) goto loc_0039B62E;
loc_0039B8FE:
    v_stack_m208 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_0039B6E5;
loc_0039B918:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039BA78;
loc_0039B931:
    goto loc_0039B74F;
loc_0039B937:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) <= (*(unsigned __int64 *)(v_rip + 12089362))) goto loc_0039B89C;
    a1 = (*(unsigned __int64 *)(v_rip + 12089362)) + ((unsigned int)(*(unsigned int *)(v_rip + 12760171)));
    *(unsigned __int64 *)(v_rip + 12089334) = a1;
    goto loc_0039B89F;
loc_0039B95F:
    if ((*(unsigned __int8 *)(v_rip + 12759327)) != 0) goto loc_0039B8AE;
    a2 = 0;
    v_stack_m1E8 = 0x200001ULL;
    result = memset(v_stack_m1E0, a2, 256, v_stack_m228);
    v_stack_m220 = v_stack_m1E8;
    result = KiForwardTick(v_stack_m210, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), 1);
    result = KiOrAffinityEx(v_rip + 10940855, v_stack_m1E8, v_rip + 10940866, *(unsigned __int16 *)(v_rip + 10940875));
    goto loc_0039B8AE;
loc_0039B9C3:
    result = KiRaiseIrqlProcessIrqlFlags(1, (unsigned __int8)(result), v_rip + 10940866, *(unsigned __int16 *)(v_rip + 10940875));
    goto loc_0039B7BC;
loc_0039B9D4:
    *(unsigned __int64 *)(v_rip + 12089206) = 1;
    if (condition_is_not_equal) goto loc_0039B867;
    a3 = 0;
    *(unsigned int *)(v_rip + 12089258) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12753082)));
    a2 = 0;
    result = KeInsertQueueDpc(v_rip + 12089195, a2, a3, *(unsigned __int16 *)(v_rip + 10940875));
    goto loc_0039B867;
loc_0039BA0A:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(v_rip + 12759183)));
    if (condition_is_less_or_equal) goto loc_0039BB19;
loc_0039BA22:
    v_rsi = (1) + (1);
    v_stack_m208 = v_rsi;
    result = (v_rsi) >> (32);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12752351) + 808) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12752323) + 800) = v_rsi;
    goto loc_0039B6D5;
loc_0039BA51:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12759137)))) & (64)) == 0) goto loc_0039B70A;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rip + 12752351), 1, a3, (unsigned int)(*(unsigned int *)(v_rip + 12759183)));
    if ((unsigned __int8)(result) == 0) goto loc_0039B70A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), 1, a3, (unsigned int)(*(unsigned int *)(v_rip + 12759183)));
    goto loc_0039B70C;
loc_0039BA78:
loc_0039BA7F:
    if ((unsigned __int8)(result) != 0) goto loc_0039BA7F;
    if (condition_is_above_or_equal) goto loc_0039B931;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, (unsigned int)(*(unsigned int *)(v_rip + 12759183)));
    goto loc_0039B931;
loc_0039BAA0:
    goto loc_0039B85A;
loc_0039BAAA:
    if ((*(unsigned __int64 *)(v_r14)) != (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_0039B5C9;
    goto loc_0039B61D;
loc_0039BAC0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48))) < (*(unsigned __int64 *)(v_r14))) goto loc_0039B72A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12089597)))) != 2) goto loc_0039B72A;
    result = KiSetForceIdleState((unsigned int)(*(unsigned int *)(v_rip + 12089597)) - 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_m200);
    result = *(unsigned __int64 *)(v_rip + 12088905);
    if (*(unsigned __int64 *)(v_rip + 12088905) == 0) {
        result = 0x800ULL;
        a1 = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_stack_m1E8 + 36))) + ((unsigned __int16)(result)));
        *(unsigned __int16 *)(v_rip + 12088831) = a1;
    }
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(v_rip + 12088819, a2, a3, v_stack_m200);
    goto loc_0039B72A;
loc_0039BB19:
    a1 = -(0);
    a2 = (a2) >> ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12759190)));
    a2 = (a2) + 1;
    a4 = (v_stack_m200) * (a2);
    a3 = (a3) + (a4);
    a2 = (a2) + 1;
    goto loc_0039BA22;
loc_0039BB45:
    goto loc_0039B73D;
loc_0039BB4D:
    result = RtlGetInterruptTimePrecise(v_stack_m1E0, a2, a3, a4);
    goto loc_0039B7EC;
}
```

## 5. (Beta) C Style

```c
int64_t KiUpdateTime(uint8_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m168;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint64_t v_stack_m230;
    uint8_t v_stack_m235;
    uint8_t v_stack_m236;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (576);
    result = (*(uint64_t *)(v_rip + 0xA6F1E2)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m218 = Arg3;
    v_stack_m236 = (uint8_t)(Arg2);
    v_stack_m235 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m1E8, Arg2, 264, a4);
    v_stack_m210 = *(uint64_t *)(gs_base + (0 + 0x20));
    local_r13 = 0;
    result = KeDisableInterrupts(v_stack_m1E8, Arg2, 264, a4);
    local_rbx = 0;
    local_r14 = (*(uint64_t *)(v_rip + 0xC29A55)) + (832);
    v_stack_m228 = 0;
loc_0039B5C9:
    result = RtlBeginReadTickLock(local_r14, Arg2, 264, a4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, 264, a4);
    result = KiComputeNewInterruptTime(result, v_stack_m228, 264, a4);
    if ((*(uint8_t *)(v_rip + 0xC2B50A)) == 0) goto loc_0039BAAA;
    if ((*(uint64_t *)(local_r14)) != result) goto loc_0039B5C9;
    if (v_stack_m228 <= (*(uint64_t *)(v_rip + 0xC2BA4F))) goto loc_0039B8FE;
    result = RtlWriteTryAcquireTickLock(local_r14, v_stack_m228, 264, v_stack_m228);
    if ((uint8_t)(result) == 0) goto loc_0039B5C9;
loc_0039B61D:
    if ((*(uint8_t *)(v_rip + 0xC2B4D4)) == 0) goto loc_0039B8F1;
    if (1 == 0) {
        Arg1 = local_r14;
        result = RtlWriteAcquireTickLock(Arg1, v_stack_m228, 264, v_stack_m228);
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_stack_m228, 264, v_stack_m228);
    result = KiComputeNewSystemTime(result, v_stack_m228, 264, v_stack_m228);
    v_stack_m230 = result;
    result = KiComputeNewInterruptTime(result, v_stack_m228, 264, v_stack_m228);
    result = (result) >> (32);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xC299A4) + 0x1C) = (uint32_t)((uint32_t)(v_stack_m22C));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xC2998F) + 0x14) = result;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xC29984) + 0x10) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xC2997A) + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xC2996F) + 0x348) = result;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xC29961) + 0x350) = result;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xACB1D6))) - (v_stack_m228);
    v_stack_m230 = *(uint64_t *)(result);
    if (condition_is_less_or_equal) goto loc_0039BA0A;
loc_0039B6D5:
    result = (*(uint64_t *)(local_r14)) + 1;
    *(uint32_t *)(v_rip + 0xACB1B6) = Arg3;
    *(uint64_t *)(local_r14) = result;
loc_0039B6E5:
    local_rdi = 0;
loc_0039B6F0:
    if (condition_is_above_or_equal) goto loc_0039B71A;
loc_0039B6FC:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC29BA8)) & ((uint32_t)(local_rdi))) == 0) goto loc_0039BA51;
loc_0039B70A:
loc_0039B70C:
    if (*(uint64_t *)(v_rip + 0xB87A2D) == 0) goto loc_0039B6F0;
    goto loc_0039B6FC;
loc_0039B71A:
    if (*(uint64_t *)(v_rip + 0xB87A27) != 0) goto loc_0039BAC0;
loc_0039B72A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB87C9C))) - 1);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) == 0) goto loc_0039BB45;
loc_0039B73D:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0039B918;
loc_0039B74F:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (*(uint32_t *)(v_rip + 0xACB153)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC2B3E7))) - 1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (Arg1 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2B485))))) {
        *(uint64_t *)(v_rip + 0xACB13E) = result;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (*(uint32_t *)(v_rip + 0xACB128)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC2B3C4))) - 1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (Arg1 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2B42E))))) {
        *(uint64_t *)(v_rip + 0xACB113) = result;
    }
    if ((*(uint8_t *)(v_rip + 0xC2B2E9)) == 0) goto loc_0039BAA0;
    if ((*(uint32_t *)(v_rip + 0xC2B56A)) != 0) goto loc_0039B9C3;
loc_0039B7BC:
    local_r15 = ((int32_t)(*(uint32_t *)(v_rip + 0xC2B3F5))) + (*(uint64_t *)(v_rip + 0xACB0DE));
    result = Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline(Arg1, *(uint64_t *)(v_rip + 0xC299A4), Arg3, v_stack_m228);
    local_r14 = ((uint32_t)(result) == 0) ? 1 : 0;
    if ((*(uint8_t *)(v_rip + 0xC2B2BF)) == 0) goto loc_0039BB4D;
loc_0039B7EC:
    local_rdi = (result) - (local_r15);
    if (condition_is_greater) { local_rdi = local_r15; }
    local_r14 = (uint8_t)((local_r14) + ((uint8_t)(local_r14)));
    result = (uint8_t)((*(uint8_t *)(v_stack_m210 + 0x95B4)) & (253));
    *(uint64_t *)(v_stack_m210 + 0x95A8) = local_rdi;
    result = (uint8_t)((result) | ((uint8_t)(local_r14)));
    *(uint32_t *)(v_stack_m210 + 0x95B0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2B366)));
    result = (uint8_t)((result) | (1));
    *(uint8_t *)(v_stack_m210 + 0x95B4) = (uint8_t)(result);
    if ((*(uint32_t *)(v_rip + 0xC2B4E7)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, v_stack_m228);
    }
loc_0039B85A:
    if (v_stack_m230 > (*(uint64_t *)(v_rip + 0xB878F7))) goto loc_0039B9D4;
loc_0039B867:
    result = (uint8_t)(v_cr8);
    if ((*(uint8_t *)(v_rip + 0xC2B217)) == 0) {
        Arg1 = result;
        result = PoExecuteIdleCheck(Arg1, Arg2, Arg3, v_stack_m228);
    }
    if (0 != 0) goto loc_0039B88B;
    if ((*(uint32_t *)(v_rip + 0xB6FB64)) == 0) {
        result = PpmExecutePeriodicPerfCheck(Arg1, Arg2, Arg3, v_stack_m228);
    }
    local_rbx = (result) >> (18);
    if ((*(uint8_t *)(v_rip + 0xC2B226)) != 0) goto loc_0039B937;
loc_0039B89C:
    local_rsi = 0;
loc_0039B89F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2B1DB)))) > 1) goto loc_0039B95F;
loc_0039B8AE:
    result = KiUpdateRunTime(v_stack_m235, v_stack_m236, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), v_stack_m228);
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m236, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), v_stack_m228);
    return result;
loc_0039B8F1:
    if (v_stack_m228 > (*(uint64_t *)(v_rip + 0xC2B760))) goto loc_0039B62E;
loc_0039B8FE:
    v_stack_m208 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_0039B6E5;
loc_0039B918:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039BA78;
loc_0039B931:
    goto loc_0039B74F;
loc_0039B937:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) <= (*(uint64_t *)(v_rip + 0xB87812))) goto loc_0039B89C;
    Arg1 = (*(uint64_t *)(v_rip + 0xB87812)) + ((uint32_t)(*(uint32_t *)(v_rip + 0xC2B46B)));
    *(uint64_t *)(v_rip + 0xB877F6) = Arg1;
    goto loc_0039B89F;
loc_0039B95F:
    if ((*(uint8_t *)(v_rip + 0xC2B11F)) != 0) goto loc_0039B8AE;
    Arg2 = 0;
    v_stack_m1E8 = 0x200001ULL;
    result = memset(v_stack_m1E0, Arg2, 256, v_stack_m228);
    v_stack_m220 = v_stack_m1E8;
    result = KiForwardTick(v_stack_m210, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), 1);
    result = KiOrAffinityEx(v_rip + 10940855, v_stack_m1E8, v_rip + 10940866, *(uint16_t *)(v_rip + 0xA6F1CB));
    goto loc_0039B8AE;
loc_0039B9C3:
    result = KiRaiseIrqlProcessIrqlFlags(1, (uint8_t)(result), v_rip + 10940866, *(uint16_t *)(v_rip + 0xA6F1CB));
    goto loc_0039B7BC;
loc_0039B9D4:
    *(uint64_t *)(v_rip + 0xB87776) = 1;
    if (condition_is_not_equal) goto loc_0039B867;
    Arg3 = 0;
    *(uint32_t *)(v_rip + 0xB877AA) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC298BA)));
    Arg2 = 0;
    result = KeInsertQueueDpc(v_rip + 12089195, Arg2, Arg3, *(uint16_t *)(v_rip + 0xA6F1CB));
    goto loc_0039B867;
loc_0039BA0A:
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(v_rip + 0xC2B08F)));
    if (condition_is_less_or_equal) goto loc_0039BB19;
loc_0039BA22:
    local_rsi = (1) + (1);
    v_stack_m208 = local_rsi;
    result = (local_rsi) >> (32);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xC295DF) + 0x328) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xC295C3) + 0x320) = local_rsi;
    goto loc_0039B6D5;
loc_0039BA51:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2B061)))) & (64)) == 0) goto loc_0039B70A;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_rip + 0xC295DF), 1, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2B08F)));
    if ((uint8_t)(result) == 0) goto loc_0039B70A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), 1, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2B08F)));
    goto loc_0039B70C;
loc_0039BA78:
loc_0039BA7F:
    if ((uint8_t)(result) != 0) goto loc_0039BA7F;
    if (condition_is_above_or_equal) goto loc_0039B931;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2B08F)));
    goto loc_0039B931;
loc_0039BAA0:
    goto loc_0039B85A;
loc_0039BAAA:
    if ((*(uint64_t *)(local_r14)) != (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_0039B5C9;
    goto loc_0039B61D;
loc_0039BAC0:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30))) < (*(uint64_t *)(local_r14))) goto loc_0039B72A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB878FD)))) != 2) goto loc_0039B72A;
    result = KiSetForceIdleState((uint32_t)(*(uint32_t *)(v_rip + 0xB878FD)) - 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, v_stack_m200);
    result = *(uint64_t *)(v_rip + 0xB87649);
    if (*(uint64_t *)(v_rip + 0xB87649) == 0) {
        result = 0x800ULL;
        Arg1 = (uint16_t)(((uint32_t)(*(uint32_t *)(v_stack_m1E8 + 0x24))) + ((uint16_t)(result)));
        *(uint16_t *)(v_rip + 0xB875FF) = Arg1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(v_rip + 12088819, Arg2, Arg3, v_stack_m200);
    goto loc_0039B72A;
loc_0039BB19:
    Arg1 = -(0);
    Arg2 = (Arg2) >> ((uint8_t)(*(uint8_t *)(v_rip + 0xC2B096)));
    Arg2 = (Arg2) + 1;
    a4 = (v_stack_m200) * (Arg2);
    Arg3 = (Arg3) + (a4);
    Arg2 = (Arg2) + 1;
    goto loc_0039BA22;
loc_0039BB45:
    goto loc_0039B73D;
loc_0039BB4D:
    result = RtlGetInterruptTimePrecise(v_stack_m1E0, Arg2, Arg3, a4);
    goto loc_0039B7EC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039B530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
