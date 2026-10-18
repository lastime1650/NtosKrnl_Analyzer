# PopEnableHiberFile

- RVA: `0x0090F850`–`0x0090FDC9` (길이 `1,401` bytes)
- VA: `0x000000014090F850`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A050`
- 디코드: `343`개 명령, `1,401/1,401` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **30**

### Outgoing calls
- `0x0090F8BA` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8C2` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8CA` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8D2` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8DA` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8E2` → [PopRemoveReasonRecordByReasonCode](../91/PopRemoveReasonRecordByReasonCode_function_00911B30.md) (function, `0x00911B30`)
- `0x0090F8E9` → [MmGetHighestPhysicalPage](../../text/47/MmGetHighestPhysicalPage_function_00479040.md) (function, `0x00479040`)
- `0x0090F91F` → [PopCheckDisabledReason](../91/PopCheckDisabledReason_function_009102A0.md) (function, `0x009102A0`)
- `0x0090F92A` → [PopCheckDisabledReason](../91/PopCheckDisabledReason_function_009102A0.md) (function, `0x009102A0`)
- `0x0090F936` → [PopCheckDisabledReason](../91/PopCheckDisabledReason_function_009102A0.md) (function, `0x009102A0`)
- `0x0090F947` → [PopCheckDisabledReason](../91/PopCheckDisabledReason_function_009102A0.md) (function, `0x009102A0`)
- `0x0090F964` → [PopCheckDisabledReason](../91/PopCheckDisabledReason_function_009102A0.md) (function, `0x009102A0`)
- `0x0090F993` → [MmZeroPageFileAtShutdown](../7F/MmZeroPageFileAtShutdown_function_007F9164.md) (function, `0x007F9164`)
- `0x0090F9AA` → [PopZeroHiberFile](../75/PopZeroHiberFile_function_0075E47C.md) (function, `0x0075E47C`)
- `0x0090F9BB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0090F9C7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0090F9D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090FA16` → [PopResetCurrentPolicies](PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)
- `0x0090FA65` → [PopOpenPowerKey](../../text/4B/PopOpenPowerKey_function_004B4314.md) (function, `0x004B4314`)
- `0x0090FA7D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0090FAA8` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x0090FAE2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0090FB15` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x0090FB3E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0090FB71` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x0090FB9B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0090FBBB` → [MmAllocateDumpHibernateResources](../AB/MmAllocateDumpHibernateResources_function_00AB3B4C.md) (function, `0x00AB3B4C`)
- `0x0090FC03` → [PopCalculateHiberFileSize](../75/PopCalculateHiberFileSize_function_0075CC98.md) (function, `0x0075CC98`)
- `0x0090FC0C` → [PopCreateHiberFile](../75/PopCreateHiberFile_function_0075CE70.md) (function, `0x0075CE70`)
- `0x0090FC40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0090FC67` → [PopPreallocateHibernateMemory](../75/PopPreallocateHibernateMemory_function_0075DB98.md) (function, `0x0075DB98`)
- `0x0090FC9F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0090FCB8` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (function, `0x00B77D70`)
- `0x0090FCF5` → [PopClearHiberFileSignature](../75/PopClearHiberFileSignature_function_0075CD90.md) (function, `0x0075CD90`)
- `0x0090FCFA` → [PopResetCurrentPolicies](PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)
- `0x0090FD1A` → [PopLogSleepDisabled](../91/PopLogSleepDisabled_function_009102D8.md) (function, `0x009102D8`)
- `0x0090FD2F` → [MmReleaseDumpHibernateResources](../7F/MmReleaseDumpHibernateResources_function_007FE418.md) (function, `0x007FE418`)
- `0x0090FD43` → [MmReturnChargesToLockPagedPool](../AD/MmReturnChargesToLockPagedPool_function_00AD3A00.md) (function, `0x00AD3A00`)
- `0x0090FD4D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090FD61` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0090FD73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090FD94` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0090FDA2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopNotifyPolicyDevice](../76/PopNotifyPolicyDevice_function_00765FF0.md) at `0x00766048`
- [PopNotifyPolicyDevice](../76/PopNotifyPolicyDevice_function_00765FF0.md) at `0x00766053`
- [PopHibernateEvaluation](PopHibernateEvaluation_function_0090F7B0.md) at `0x0090F83C`

### Static image references
- `0x0090F873` → RVA `0x00E0A740` (`.data`; read)
- `0x0090F911` → RVA `0x00F0CEC6` (`.data`; read)
- `0x0090F980` → RVA `0x00F0BF28` (`.data`; read)
- `0x0090F987` → RVA `0x00FC6AFF` (`ALMOSTRO`; write)
- `0x0090F9A3` → RVA `0x00F0BF20` (`.data`; read)
- `0x0090F9CC` → RVA `0x00F0BF38` (`.data`; read)
- `0x0090F9DD` → RVA `0x00F0BF48` (`.data`; read)
- `0x0090F9E7` → RVA `0x00F0BF70` (`.data`; read)
- `0x0090F9EE` → RVA `0x00F0BF68` (`.data`; read)
- `0x0090F9F5` → RVA `0x00F0BF48` (`.data`; write)
- `0x0090F9FD` → RVA `0x00F0CEC8` (`.data`; write)
- `0x0090FA03` → RVA `0x00F0CED6` (`.data`; write)
- `0x0090FA09` → RVA `0x00F0CED2` (`.data`; write)
- `0x0090FA0F` → RVA `0x00F0BF58` (`.data`; write)
- `0x0090FA49` → RVA `0x00F0BF64` (`.data`; write)
- `0x0090FA4F` → RVA `0x00F0BF44` (`.data`; write)
- `0x0090FA59` → RVA `0x00F0BF61` (`.data`; write)
- `0x0090FA5F` → RVA `0x00F0BFF8` (`.data`; write)
- `0x0090FA72` → RVA `0x00B01E70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0090FAD7` → RVA `0x00B01E90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0090FB33` → RVA `0x00B01EC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0090FB91` → RVA `0x00F0BFF8` (`.data`; read/write)
- `0x0090FC30` → RVA `0x00F0BF50` (`.data`; write)
- `0x0090FC5D` → RVA `0x00F0BF68` (`.data`; write)
- `0x0090FC7B` → RVA `0x00F0C2E0` (`.data`; read)
- `0x0090FCAE` → RVA `0x00029248` (`.rdata`; read)
- `0x0090FCD0` → RVA `0x00FC41C4` (`.data`; read)
- `0x0090FCED` → RVA `0x00E675C8` (`.data`; reference)
- `0x0090FD39` → RVA `0x00F0BF78` (`.data`; read)
- `0x0090FD78` → RVA `0x00F0BF68` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x0090F8E9` → [MmGetHighestPhysicalPage](../../text/47/MmGetHighestPhysicalPage_function_00479040.md) (`PAGE` → `.text`)
  - `0x0090F9BB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0090F9C7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0090F9D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090FA65` → [PopOpenPowerKey](../../text/4B/PopOpenPowerKey_function_004B4314.md) (`PAGE` → `.text`)
  - `0x0090FA7D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0090FAA8` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x0090FAE2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0090FB15` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x0090FB3E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0090FB71` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x0090FB9B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0090FC40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0090FC9F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0090FCB8` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (`PAGE` → `PAGELK`)
  - `0x0090FD4D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090FD61` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0090FD73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090FD94` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0090FDA2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0090F850  48 8B C4                        mov rax, rsp
0090F853  48 89 58 08                     mov qword ptr [rax + 8], rbx
0090F857  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0090F85B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0090F85F  55                              push rbp
0090F860  41 54                           push r12
0090F862  41 55                           push r13
0090F864  41 56                           push r14
0090F866  41 57                           push r15
0090F868  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0090F86C  48 81 EC A0 00 00 00            sub rsp, 0xa0
0090F873  48 8B 05 C6 AE 4F 00            mov rax, qword ptr [rip + 0x4faec6]
0090F87A  48 33 C4                        xor rax, rsp
0090F87D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0090F881  33 DB                           xor ebx, ebx
0090F883  0F 57 C0                        xorps xmm0, xmm0
0090F886  44 8A E9                        mov r13b, cl
0090F889  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
0090F88D  0F 57 C9                        xorps xmm1, xmm1
0090F890  88 5D C7                        mov byte ptr [rbp - 0x39], bl
0090F893  33 C0                           xor eax, eax
0090F895  89 5D D7                        mov dword ptr [rbp - 0x29], ebx
0090F898  8D 4B 06                        lea ecx, [rbx + 6]
0090F89B  89 45 27                        mov dword ptr [rbp + 0x27], eax
0090F89E  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0090F8A2  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
0090F8A6  44 8B FB                        mov r15d, ebx
0090F8A9  0F 11 4D 07                     movups xmmword ptr [rbp + 7], xmm1
0090F8AD  8B F3                           mov esi, ebx
0090F8AF  44 8B E3                        mov r12d, ebx
0090F8B2  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
0090F8B6  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0090F8BA  E8 71 22 00 00                  call 0x140911b30
0090F8BF  8D 4B 08                        lea ecx, [rbx + 8]
0090F8C2  E8 69 22 00 00                  call 0x140911b30
0090F8C7  8D 4B 16                        lea ecx, [rbx + 0x16]
0090F8CA  E8 61 22 00 00                  call 0x140911b30
0090F8CF  8D 4B 17                        lea ecx, [rbx + 0x17]
0090F8D2  E8 59 22 00 00                  call 0x140911b30
0090F8D7  8D 4B 18                        lea ecx, [rbx + 0x18]
0090F8DA  E8 51 22 00 00                  call 0x140911b30
0090F8DF  8D 4B 19                        lea ecx, [rbx + 0x19]
0090F8E2  E8 49 22 00 00                  call 0x140911b30
0090F8E7  33 C9                           xor ecx, ecx
0090F8E9  E8 52 97 B6 FF                  call 0x140479040
0090F8EE  48 B9 00 00 00 00 01 00 00 00   movabs rcx, 0x100000000
0090F8F8  8D 7B 01                        lea edi, [rbx + 1]
0090F8FB  48 3B C1                        cmp rax, rcx
0090F8FE  45 1B F6                        sbb r14d, r14d
0090F901  41 F7 D6                        not r14d
0090F904  41 83 E6 08                     and r14d, 8
0090F908  48 3B C1                        cmp rax, rcx
0090F90B  8D 4B 02                        lea ecx, [rbx + 2]
0090F90E  0F 93 C0                        setae al
0090F911  38 1D AF D5 5F 00               cmp byte ptr [rip + 0x5fd5af], bl
0090F917  44 0F B6 D8                     movzx r11d, al
0090F91B  44 0F 44 DF                     cmove r11d, edi
0090F91F  E8 7C 09 00 00                  call 0x1409102a0
0090F924  84 C0                           test al, al
0090F926  75 17                           jne 0x14090f93f
0090F928  8B CF                           mov ecx, edi
0090F92A  E8 71 09 00 00                  call 0x1409102a0
0090F92F  84 C0                           test al, al
0090F931  75 0C                           jne 0x14090f93f
0090F933  8D 4B 0F                        lea ecx, [rbx + 0xf]
0090F936  E8 65 09 00 00                  call 0x1409102a0
0090F93B  84 C0                           test al, al
0090F93D  74 03                           je 0x14090f942
0090F93F  44 8A DF                        mov r11b, dil
0090F942  B9 10 00 00 00                  mov ecx, 0x10
0090F947  E8 54 09 00 00                  call 0x1409102a0
0090F94C  84 C0                           test al, al
0090F94E  74 0F                           je 0x14090f95f
0090F950  B9 BB 00 00 C0                  mov ecx, 0xc00000bb
0090F955  8B D9                           mov ebx, ecx
0090F957  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
0090F95A  E9 CB 00 00 00                  jmp 0x14090fa2a
0090F95F  B9 0D 00 00 00                  mov ecx, 0xd
0090F964  E8 37 09 00 00                  call 0x1409102a0
0090F969  84 C0                           test al, al
0090F96B  41 0F B6 FB                     movzx edi, r11b
0090F96F  B8 01 00 00 00                  mov eax, 1
0090F974  0F 45 F8                        cmovne edi, eax
0090F977  45 84 ED                        test r13b, r13b
0090F97A  0F 85 B8 00 00 00               jne 0x14090fa38
0090F980  48 39 1D A1 C5 5F 00            cmp qword ptr [rip + 0x5fc5a1], rbx
0090F987  88 1D 72 71 6B 00               mov byte ptr [rip + 0x6b7172], bl
0090F98D  0F 84 6E 03 00 00               je 0x14090fd01
0090F993  E8 CC 97 EE FF                  call 0x1407f9164
0090F998  85 C0                           test eax, eax
0090F99A  74 13                           je 0x14090f9af
0090F99C  48 8B 15 85 C5 5F 00            mov rdx, qword ptr [rip + 0x5fc585]
0090F9A3  48 8B 0D 76 C5 5F 00            mov rcx, qword ptr [rip + 0x5fc576]
0090F9AA  E8 CD EA E4 FF                  call 0x14075e47c
0090F9AF  48 8B 0D 72 C5 5F 00            mov rcx, qword ptr [rip + 0x5fc572]
0090F9B6  BA 50 6F 48 62                  mov edx, 0x62486f50
0090F9BB  E8 20 7F 9E FF                  call 0x1402f78e0
0090F9C0  48 8B 0D 59 C5 5F 00            mov rcx, qword ptr [rip + 0x5fc559]
0090F9C7  E8 E4 D8 D9 FF                  call 0x1406ad2b0
0090F9CC  48 8B 0D 65 C5 5F 00            mov rcx, qword ptr [rip + 0x5fc565]
0090F9D3  BA 68 69 62 72                  mov edx, 0x72626968
0090F9D8  E8 93 2E 27 00                  call 0x140b82870
0090F9DD  48 8B 35 64 C5 5F 00            mov rsi, qword ptr [rip + 0x5fc564]
0090F9E4  0F 57 C0                        xorps xmm0, xmm0
0090F9E7  4C 8B 25 82 C5 5F 00            mov r12, qword ptr [rip + 0x5fc582]
0090F9EE  4C 8B 3D 73 C5 5F 00            mov r15, qword ptr [rip + 0x5fc573]
0090F9F5  F3 0F 7F 05 4B C5 5F 00         movdqu xmmword ptr [rip + 0x5fc54b], xmm0
0090F9FD  88 1D C5 D4 5F 00               mov byte ptr [rip + 0x5fd4c5], bl
0090FA03  88 1D CD D4 5F 00               mov byte ptr [rip + 0x5fd4cd], bl
0090FA09  88 1D C3 D4 5F 00               mov byte ptr [rip + 0x5fd4c3], bl
0090FA0F  48 89 1D 42 C5 5F 00            mov qword ptr [rip + 0x5fc542], rbx
0090FA16  E8 49 05 00 00                  call 0x14090ff64
0090FA1B  8B D8                           mov ebx, eax
0090FA1D  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0090FA20  8B C8                           mov ecx, eax
0090FA22  85 C0                           test eax, eax
0090FA24  0F 89 DA 02 00 00               jns 0x14090fd04
0090FA2A  45 84 ED                        test r13b, r13b
0090FA2D  0F 85 48 02 00 00               jne 0x14090fc7b
0090FA33  E9 CC 02 00 00                  jmp 0x14090fd04
0090FA38  48 39 1D E9 C4 5F 00            cmp qword ptr [rip + 0x5fc4e9], rbx
0090FA3F  0F 85 BC 02 00 00               jne 0x14090fd01
0090FA45  48 8D 4D DF                     lea rcx, [rbp - 0x21]
0090FA49  89 05 15 C5 5F 00               mov dword ptr [rip + 0x5fc515], eax
0090FA4F  C7 05 EB C4 5F 00 41 06 00 00   mov dword ptr [rip + 0x5fc4eb], 0x641
0090FA59  88 1D 02 C5 5F 00               mov byte ptr [rip + 0x5fc502], bl
0090FA5F  89 1D 93 C5 5F 00               mov dword ptr [rip + 0x5fc593], ebx
0090FA65  E8 AA 48 BA FF                  call 0x1404b4314
0090FA6A  85 C0                           test eax, eax
0090FA6C  0F 88 2E 01 00 00               js 0x14090fba0
0090FA72  48 8D 15 F7 23 1F 00            lea rdx, [rip + 0x1f23f7]
0090FA79  48 8D 4D E7                     lea rcx, [rbp - 0x19]
0090FA7D  E8 FE AC B1 FF                  call 0x14042a780
0090FA82  48 8B 5D DF                     mov rbx, qword ptr [rbp - 0x21]
0090FA86  48 8D 45 D7                     lea rax, [rbp - 0x29]
0090FA8A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090FA8F  4C 8D 4D 17                     lea r9, [rbp + 0x17]
0090FA93  41 B8 02 00 00 00               mov r8d, 2
0090FA99  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
0090FAA1  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0090FAA5  48 8B CB                        mov rcx, rbx
0090FAA8  E8 03 D9 D9 FF                  call 0x1406ad3b0
0090FAAD  85 C0                           test eax, eax
0090FAAF  78 26                           js 0x14090fad7
0090FAB1  83 7D 1B 04                     cmp dword ptr [rbp + 0x1b], 4
0090FAB5  75 20                           jne 0x14090fad7
0090FAB7  83 7D 1F 04                     cmp dword ptr [rbp + 0x1f], 4
0090FABB  75 1A                           jne 0x14090fad7
0090FABD  8B 45 23                        mov eax, dword ptr [rbp + 0x23]
0090FAC0  89 05 9E C4 5F 00               mov dword ptr [rip + 0x5fc49e], eax
0090FAC6  FF C8                           dec eax
0090FAC8  83 F8 62                        cmp eax, 0x62
0090FACB  76 0A                           jbe 0x14090fad7
0090FACD  C7 05 8D C4 5F 00 01 00 00 00   mov dword ptr [rip + 0x5fc48d], 1
0090FAD7  48 8D 15 B2 23 1F 00            lea rdx, [rip + 0x1f23b2]
0090FADE  48 8D 4D F7                     lea rcx, [rbp - 9]
0090FAE2  E8 99 AC B1 FF                  call 0x14042a780
0090FAE7  33 C0                           xor eax, eax
0090FAE9  4C 8D 4D 17                     lea r9, [rbp + 0x17]
0090FAED  89 45 27                        mov dword ptr [rbp + 0x27], eax
0090FAF0  48 8D 55 F7                     lea rdx, [rbp - 9]
0090FAF4  48 8D 45 D7                     lea rax, [rbp - 0x29]
0090FAF8  0F 57 C0                        xorps xmm0, xmm0
0090FAFB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090FB00  41 B8 02 00 00 00               mov r8d, 2
0090FB06  48 8B CB                        mov rcx, rbx
0090FB09  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
0090FB11  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
0090FB15  E8 96 D8 D9 FF                  call 0x1406ad3b0
0090FB1A  85 C0                           test eax, eax
0090FB1C  78 15                           js 0x14090fb33
0090FB1E  83 7D 1B 04                     cmp dword ptr [rbp + 0x1b], 4
0090FB22  75 0F                           jne 0x14090fb33
0090FB24  83 7D 1F 04                     cmp dword ptr [rbp + 0x1f], 4
0090FB28  75 09                           jne 0x14090fb33
0090FB2A  8B 45 23                        mov eax, dword ptr [rbp + 0x23]
0090FB2D  89 05 11 C4 5F 00               mov dword ptr [rip + 0x5fc411], eax
0090FB33  48 8D 15 86 23 1F 00            lea rdx, [rip + 0x1f2386]
0090FB3A  48 8D 4D 07                     lea rcx, [rbp + 7]
0090FB3E  E8 3D AC B1 FF                  call 0x14042a780
0090FB43  33 C0                           xor eax, eax
0090FB45  4C 8D 4D 17                     lea r9, [rbp + 0x17]
0090FB49  89 45 27                        mov dword ptr [rbp + 0x27], eax
0090FB4C  48 8D 55 07                     lea rdx, [rbp + 7]
0090FB50  48 8D 45 D7                     lea rax, [rbp - 0x29]
0090FB54  0F 57 C0                        xorps xmm0, xmm0
0090FB57  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090FB5C  41 B8 02 00 00 00               mov r8d, 2
0090FB62  48 8B CB                        mov rcx, rbx
0090FB65  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
0090FB6D  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
0090FB71  E8 3A D8 D9 FF                  call 0x1406ad3b0
0090FB76  85 C0                           test eax, eax
0090FB78  78 1E                           js 0x14090fb98
0090FB7A  83 7D 1B 04                     cmp dword ptr [rbp + 0x1b], 4
0090FB7E  75 18                           jne 0x14090fb98
0090FB80  83 7D 1F 04                     cmp dword ptr [rbp + 0x1f], 4
0090FB84  75 12                           jne 0x14090fb98
0090FB86  83 7D 23 01                     cmp dword ptr [rbp + 0x23], 1
0090FB8A  0F 94 05 D0 C3 5F 00            sete byte ptr [rip + 0x5fc3d0]
0090FB91  83 0D 60 C4 5F 00 20            or dword ptr [rip + 0x5fc460], 0x20
0090FB98  48 8B CB                        mov rcx, rbx
0090FB9B  E8 10 D7 D9 FF                  call 0x1406ad2b0
0090FBA0  C6 05 58 6F 6B 00 01            mov byte ptr [rip + 0x6b6f58], 1
0090FBA7  40 84 FF                        test dil, dil
0090FBAA  74 0A                           je 0x14090fbb6
0090FBAC  B9 BB 00 00 C0                  mov ecx, 0xc00000bb
0090FBB1  E9 A0 00 00 00                  jmp 0x14090fc56
0090FBB6  B9 00 30 01 00                  mov ecx, 0x13000
0090FBBB  E8 8C 3F 1A 00                  call 0x140ab3b4c
0090FBC0  48 8B F0                        mov rsi, rax
0090FBC3  48 85 C0                        test rax, rax
0090FBC6  75 09                           jne 0x14090fbd1
0090FBC8  44 8D 70 17                     lea r14d, [rax + 0x17]
0090FBCC  E9 80 00 00 00                  jmp 0x14090fc51
0090FBD1  48 8D B8 00 00 20 00            lea rdi, [rax + 0x200000]
0090FBD8  48 F7 C6 FF FF 1F 00            test rsi, 0x1fffff
0090FBDF  74 0A                           je 0x14090fbeb
0090FBE1  48 FF CF                        dec rdi
0090FBE4  48 81 E7 00 00 E0 FF            and rdi, 0xffffffffffe00000
0090FBEB  48 8B C7                        mov rax, rdi
0090FBEE  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0090FBF2  48 2B C6                        sub rax, rsi
0090FBF5  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0090FBF9  48 3D 00 A0 00 00               cmp rax, 0xa000
0090FBFF  48 0F 43 FE                     cmovae rdi, rsi
0090FC03  E8 90 D0 E4 FF                  call 0x14075cc98
0090FC08  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0090FC0C  E8 5F D2 E4 FF                  call 0x14075ce70
0090FC11  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0090FC14  8B D8                           mov ebx, eax
0090FC16  85 C0                           test eax, eax
0090FC18  79 08                           jns 0x14090fc22
0090FC1A  41 BE 06 00 00 00               mov r14d, 6
0090FC20  EB 57                           jmp 0x14090fc79
0090FC22  48 89 35 1F C3 5F 00            mov qword ptr [rip + 0x5fc31f], rsi
0090FC29  BA F0 01 00 00                  mov edx, 0x1f0
0090FC2E  33 F6                           xor esi, esi
0090FC30  48 89 3D 19 C3 5F 00            mov qword ptr [rip + 0x5fc319], rdi
0090FC37  41 B8 48 6D 61 70               mov r8d, 0x70616d48
0090FC3D  8D 4E 40                        lea ecx, [rsi + 0x40]
0090FC40  E8 AB 24 27 00                  call 0x140b820f0
0090FC45  4C 8B F8                        mov r15, rax
0090FC48  48 85 C0                        test rax, rax
0090FC4B  75 10                           jne 0x14090fc5d
0090FC4D  44 8D 76 18                     lea r14d, [rsi + 0x18]
0090FC51  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0090FC56  8B D9                           mov ebx, ecx
0090FC58  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
0090FC5B  EB 1E                           jmp 0x14090fc7b
0090FC5D  48 89 05 04 C3 5F 00            mov qword ptr [rip + 0x5fc304], rax
0090FC64  45 33 FF                        xor r15d, r15d
0090FC67  E8 2C DF E4 FF                  call 0x14075db98
0090FC6C  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0090FC6F  8B D8                           mov ebx, eax
0090FC71  85 C0                           test eax, eax
0090FC73  79 30                           jns 0x14090fca5
0090FC75  45 8D 77 19                     lea r14d, [r15 + 0x19]
0090FC79  8B C8                           mov ecx, eax
0090FC7B  F7 05 5B C6 5F 00 00 08 00 00   test dword ptr [rip + 0x5fc65b], 0x800
0090FC85  74 7D                           je 0x14090fd04
0090FC87  49 83 C9 FF                     or r9, 0xffffffffffffffff
0090FC8B  41 8B C6                        mov eax, r14d
0090FC8E  4C 63 C1                        movsxd r8, ecx
0090FC91  B9 A0 00 00 00                  mov ecx, 0xa0
0090FC96  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090FC9B  41 8D 51 0A                     lea edx, [r9 + 0xa]
0090FC9F  E8 BC D9 BE FF                  call 0x1404fd660
0090FCA4  CC                              int3
0090FCA5  BB 01 00 00 00                  mov ebx, 1
0090FCAA  48 8D 55 CF                     lea rdx, [rbp - 0x31]
0090FCAE  48 8D 0D 93 95 71 FF            lea rcx, [rip - 0x8e6a6d]
0090FCB5  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
0090FCB8  E8 B3 80 26 00                  call 0x140b77d70
0090FCBD  83 7D CF 02                     cmp dword ptr [rbp - 0x31], 2
0090FCC1  75 0D                           jne 0x14090fcd0
0090FCC3  83 0D 2E C3 5F 00 10            or dword ptr [rip + 0x5fc32e], 0x10
0090FCCA  88 1D 91 C2 5F 00               mov byte ptr [rip + 0x5fc291], bl
0090FCD0  39 35 EE 44 6B 00               cmp dword ptr [rip + 0x6b44ee], esi
0090FCD6  8A 45 C7                        mov al, byte ptr [rbp - 0x39]
0090FCD9  88 05 F7 D1 5F 00               mov byte ptr [rip + 0x5fd1f7], al
0090FCDF  88 1D E3 D1 5F 00               mov byte ptr [rip + 0x5fd1e3], bl
0090FCE5  75 06                           jne 0x14090fced
0090FCE7  88 1D E5 D1 5F 00               mov byte ptr [rip + 0x5fd1e5], bl
0090FCED  84 1D D5 78 55 00               test byte ptr [rip + 0x5578d5], bl
0090FCF3  75 05                           jne 0x14090fcfa
0090FCF5  E8 96 D0 E4 FF                  call 0x14075cd90
0090FCFA  E8 65 02 00 00                  call 0x14090ff64
0090FCFF  33 DB                           xor ebx, ebx
0090FD01  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
0090FD04  45 85 F6                        test r14d, r14d
0090FD07  74 19                           je 0x14090fd22
0090FD09  41 B9 04 00 00 00               mov r9d, 4
0090FD0F  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0090FD13  41 8B CE                        mov ecx, r14d
0090FD16  41 8D 51 04                     lea edx, [r9 + 4]
0090FD1A  E8 B9 05 00 00                  call 0x1409102d8
0090FD1F  8B 5D CF                        mov ebx, dword ptr [rbp - 0x31]
0090FD22  48 85 F6                        test rsi, rsi
0090FD25  74 0D                           je 0x14090fd34
0090FD27  BA 00 30 01 00                  mov edx, 0x13000
0090FD2C  48 8B CE                        mov rcx, rsi
0090FD2F  E8 E4 E6 EE FF                  call 0x1407fe418
0090FD34  4D 85 E4                        test r12, r12
0090FD37  74 2D                           je 0x14090fd66
0090FD39  48 8B 15 38 C2 5F 00            mov rdx, qword ptr [rip + 0x5fc238]
0090FD40  49 8B CC                        mov rcx, r12
0090FD43  E8 B8 3C 1C 00                  call 0x140ad3a00
0090FD48  33 D2                           xor edx, edx
0090FD4A  49 8B CC                        mov rcx, r12
0090FD4D  E8 1E 2B 27 00                  call 0x140b82870
0090FD52  33 D2                           xor edx, edx
0090FD54  48 8D 0D 15 C2 5F 00            lea rcx, [rip + 0x5fc215]
0090FD5B  41 B8 88 00 00 00               mov r8d, 0x88
0090FD61  E8 DA 6E DB FF                  call 0x1406c6c40
0090FD66  4D 85 FF                        test r15, r15
0090FD69  74 15                           je 0x14090fd80
0090FD6B  BA 48 6D 61 70                  mov edx, 0x70616d48
0090FD70  49 8B CF                        mov rcx, r15
0090FD73  E8 F8 2A 27 00                  call 0x140b82870
0090FD78  48 83 25 E8 C1 5F 00 00         and qword ptr [rip + 0x5fc1e8], 0
0090FD80  45 84 ED                        test r13b, r13b
0090FD83  75 14                           jne 0x14090fd99
0090FD85  33 D2                           xor edx, edx
0090FD87  48 8D 0D 92 C1 5F 00            lea rcx, [rip + 0x5fc192]
0090FD8E  41 B8 E8 00 00 00               mov r8d, 0xe8
0090FD94  E8 A7 6E DB FF                  call 0x1406c6c40
0090FD99  8B C3                           mov eax, ebx
0090FD9B  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
0090FD9F  48 33 CC                        xor rcx, rsp
0090FDA2  E8 99 C8 D9 FF                  call 0x1406ac640
0090FDA7  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
0090FDAF  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0090FDB3  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0090FDB7  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0090FDBB  49 8B E3                        mov rsp, r11
0090FDBE  41 5F                           pop r15
0090FDC0  41 5E                           pop r14
0090FDC2  41 5D                           pop r13
0090FDC4  41 5C                           pop r12
0090FDC6  5D                              pop rbp
0090FDC7  C3                              ret
0090FDC8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEnableHiberFile(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 5222086)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 57) = 0;
    result = 0;
    *(unsigned int *)(v_rsp - 95 - 41) = 0;
    *(unsigned int *)(v_rsp - 95 + 39) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm0;
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 6, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 8, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 22, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 23, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 24, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(v_rbx + 25, a2, a3, a4);
    a1 = 0;
    result = MmGetHighestPhysicalPage(a1, a2, a3, a4);
    v_r14 = (unsigned int)(~(v_r14));
    v_r14 = (unsigned int)((v_r14) & (8));
    result = (result >= 0) ? 1 : 0;
    v_r11 = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_rip + 6280623)) == 0) { v_r11 = (unsigned int)(v_rbx + 1); }
    result = PopCheckDisabledReason(v_rbx + 2, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0090F93F;
    result = PopCheckDisabledReason((unsigned int)((unsigned int)(v_rbx + 1)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0090F93F;
    result = PopCheckDisabledReason(v_rbx + 15, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        v_r11 = (unsigned __int8)(v_rbx + 1);
    }
    result = PopCheckDisabledReason(16, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0090F95F;
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_0090FA2A;
loc_0090F95F:
    result = PopCheckDisabledReason(13, a2, a3, a4);
    v_rdi = (unsigned __int8)(v_r11);
    if ((unsigned __int8)(result) != 0) { v_rdi = 1; }
    if (0 != 0) goto loc_0090FA38;
    *(unsigned __int8 *)(v_rip + 7041394) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))));
    if ((*(unsigned __int64 *)(v_rip + 6276513)) == ((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))))) goto loc_0090FD01;
    result = MmZeroPageFileAtShutdown(13, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 6276485);
        a1 = *(unsigned __int64 *)(v_rip + 6276470);
        result = PopZeroHiberFile(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_rip + 6276466), (unsigned int)(0x62486F50ULL), a3, a4);
    result = ZwClose(*(unsigned __int64 *)(v_rip + 6276441), (unsigned int)(0x62486F50ULL), a3, a4);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 6276453), (unsigned int)(0x72626968ULL), a3, a4);
    *(unsigned __int64 *)(v_rip + 6276427) = v_xmm0;
    *(unsigned __int8 *)(v_rip + 6280389) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))));
    *(unsigned __int8 *)(v_rip + 6280397) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))));
    *(unsigned __int8 *)(v_rip + 6280387) = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))));
    *(unsigned __int64 *)(v_rip + 6276418) = (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
    result = PopResetCurrentPolicies(*(unsigned __int64 *)(v_rip + 6276453), (unsigned int)(0x72626968ULL), a3, a4);
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    if (!sign_flag) goto loc_0090FD04;
loc_0090FA2A:
    if (a1 != 0) goto loc_0090FC7B;
    goto loc_0090FD04;
loc_0090FA38:
    if ((*(unsigned __int64 *)(v_rip + 6276329)) != ((unsigned int)((unsigned int)(result)))) goto loc_0090FD01;
    *(unsigned int *)(v_rip + 6276373) = (unsigned int)(result);
    *(unsigned int *)(v_rip + 6276331) = 0x641ULL;
    *(unsigned __int8 *)(v_rip + 6276354) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_rip + 6276499) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = PopOpenPowerKey(v_rsp - 95 - 33, (unsigned int)(0x72626968ULL), a3, a4);
    if (sign_flag) goto loc_0090FBA0;
    result = RtlInitUnicodeString(v_rsp - 95 - 25, v_rip + 2040823, a3, a4);
    v_stack_mA0 = v_rsp - 95 - 41;
    v_stack_mA8 = 20;
    result = ZwQueryValueKey(*(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 - 25, 2, v_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FAD7;
    if ((*(unsigned int *)(v_rsp - 95 + 27)) != 4) goto loc_0090FAD7;
    if ((*(unsigned int *)(v_rsp - 95 + 31)) != 4) goto loc_0090FAD7;
    *(unsigned int *)(v_rip + 6276254) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 35)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 35))) - 1);
    if (((unsigned int)(result)) >= = 98) {
        *(unsigned int *)(v_rip + 6276237) = 1;
    }
    result = RtlInitUnicodeString(v_rsp - 95 - 9, v_rip + 2040754, 2, v_rsp - 95 + 23);
    result = 0;
    *(unsigned int *)(v_rsp - 95 + 39) = 0;
    v_stack_mA0 = v_rsp - 95 - 41;
    v_stack_mA8 = 20;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    result = ZwQueryValueKey(*(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 - 9, 2, v_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FB33;
    if ((*(unsigned int *)(v_rsp - 95 + 27)) != 4) goto loc_0090FB33;
    if ((*(unsigned int *)(v_rsp - 95 + 31)) == 4) {
        result = *(unsigned int *)(v_rsp - 95 + 35);
        *(unsigned int *)(v_rip + 6276113) = (unsigned int)(result);
    }
    result = RtlInitUnicodeString(v_rsp - 95 + 7, v_rip + 2040710, 2, v_rsp - 95 + 23);
    result = 0;
    *(unsigned int *)(v_rsp - 95 + 39) = 0;
    v_stack_mA0 = v_rsp - 95 - 41;
    v_stack_mA8 = 20;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_xmm0;
    result = ZwQueryValueKey(*(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 + 7, 2, v_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FB98;
    if ((*(unsigned int *)(v_rsp - 95 + 27)) != 4) goto loc_0090FB98;
    if ((*(unsigned int *)(v_rsp - 95 + 31)) == 4) {
    }
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 33), v_rsp - 95 + 7, 2, v_rsp - 95 + 23);
loc_0090FBA0:
    *(unsigned __int8 *)(v_rip + 7040856) = 1;
    if ((unsigned __int8)(v_rdi) == 0) goto loc_0090FBB6;
    goto loc_0090FC56;
loc_0090FBB6:
    result = MmAllocateDumpHibernateResources((unsigned int)(0x13000ULL), v_rsp - 95 + 7, 2, v_rsp - 95 + 23);
    if (result != 0) goto loc_0090FBD1;
    goto loc_0090FC51;
loc_0090FBD1:
    v_rdi = result + 2097152;
    if (((result) & (0x1FFFFFULL)) != 0) {
        v_rdi = (result + 2097152) - 1;
        v_rdi = (v_rdi) & (0xFFFFFFFFFFE00000ULL);
    }
    result = (v_rdi) - (result);
    if (result >= 0xA000ULL) { v_rdi = result; }
    result = PopCalculateHiberFileSize(v_rsp - 95 - 49, v_rsp - 95 - 57, 2, v_rsp - 95 + 23);
    result = PopCreateHiberFile(*(unsigned __int64 *)(v_rsp - 95 - 49), v_rsp - 95 - 57, 2, v_rsp - 95 + 23);
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    if (!sign_flag) goto loc_0090FC22;
    goto loc_0090FC79;
loc_0090FC22:
    *(unsigned __int64 *)(v_rip + 6275871) = result;
    v_rsi = 0;
    *(unsigned __int64 *)(v_rip + 6275865) = v_rdi;
    result = ExAllocatePool2(v_rsi + 64, 496, (unsigned int)(0x70616D48ULL), v_rsp - 95 + 23);
    if (result != 0) goto loc_0090FC5D;
loc_0090FC51:
loc_0090FC56:
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0090FC7B;
loc_0090FC5D:
    *(unsigned __int64 *)(v_rip + 6275844) = result;
    v_r15 = 0;
    result = PopPreallocateHibernateMemory((unsigned int)(0xC000009AULL), 496, (unsigned int)(0x70616D48ULL), v_rsp - 95 + 23);
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(result);
    if (!sign_flag) goto loc_0090FCA5;
loc_0090FC79:
loc_0090FC7B:
    if (((*(unsigned int *)(v_rip + 6276699)) & (0x800ULL)) == 0) goto loc_0090FD04;
    a4 = (v_rsp - 95 + 23) | (-1);
    v_stack_mA8 = (unsigned int)((unsigned int)(v_r15 + 25));
    result = KeBugCheckEx(160, a4 + 10, (int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_0090FCA5:
    *(unsigned int *)(v_rsp - 95 - 49) = 1;
    result = EmClientQueryRuleState(v_rip - 9333357, v_rsp - 95 - 49, (int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if ((*(unsigned int *)(v_rsp - 95 - 49)) == 2) {
        *(unsigned __int8 *)(v_rip + 6275729) = 1;
    }
    *(unsigned __int8 *)(v_rip + 6279671) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 - 57));
    *(unsigned __int8 *)(v_rip + 6279651) = 1;
    if ((*(unsigned int *)(v_rip + 7029998)) == 0) {
        *(unsigned __int8 *)(v_rip + 6279653) = 1;
    }
    result = *(unsigned __int8 *)(v_rsp - 95 - 57);
    if (((*(unsigned __int8 *)(v_rip + 5601493)) & (1)) == 0) {
        result = PopClearHiberFileSignature(v_rip - 9333357, v_rsp - 95 - 49, (int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    }
    result = PopResetCurrentPolicies(v_rip - 9333357, v_rsp - 95 - 49, (int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    v_rbx = 0;
loc_0090FD01:
    *(unsigned int *)(v_rsp - 95 - 49) = 0;
loc_0090FD04:
    if ((unsigned int)(v_r15 + 25) != 0) {
        a4 = 4;
        a3 = v_rsp - 95 - 49;
        a1 = (unsigned int)(v_r15 + 25);
        a2 = a4 + 4;
        result = PopLogSleepDisabled(a1, a2, a3, a4);
        v_rbx = *(unsigned int *)(v_rsp - 95 - 49);
    }
    if (0 != 0) {
        a2 = 0x13000ULL;
        a1 = 0;
        result = MmReleaseDumpHibernateResources(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rip + 6276482) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 6275640);
        a1 = *(unsigned __int64 *)(v_rip + 6276482);
        result = MmReturnChargesToLockPagedPool(a1, a2, a3, a4);
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 6276482);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_rip + 6275605;
        a3 = 136;
        result = memset(a1, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0x70616D48ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (a1 == 0) {
        a2 = 0;
        a1 = v_rip + 6275474;
        a3 = 232;
        result = memset(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopEnableHiberFile(uint8_t Arg1)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x4FAEC6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x39) = 0;
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x27) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm0;
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 6, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 8, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 22, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 23, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 24, a2, a3, a4);
    result = PopRemoveReasonRecordByReasonCode(local_rbx + 25, a2, a3, a4);
    Arg1 = 0;
    result = MmGetHighestPhysicalPage(Arg1, a2, a3, a4);
    local_r14 = (uint32_t)(~(local_r14));
    local_r14 = (uint32_t)((local_r14) & (8));
    result = (result >= 0) ? 1 : 0;
    local_r11 = (uint8_t)(result);
    if ((*(uint8_t *)(v_rip + 0x5FD5AF)) == 0) { local_r11 = (uint32_t)(local_rbx + 1); }
    result = PopCheckDisabledReason(local_rbx + 2, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_0090F93F;
    result = PopCheckDisabledReason((uint32_t)((uint32_t)(local_rbx + 1)), a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_0090F93F;
    result = PopCheckDisabledReason(local_rbx + 15, a2, a3, a4);
    if ((uint8_t)(result) != 0) {
        local_r11 = (uint8_t)(local_rbx + 1);
    }
    result = PopCheckDisabledReason(16, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0090F95F;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_0090FA2A;
loc_0090F95F:
    result = PopCheckDisabledReason(13, a2, a3, a4);
    local_rdi = (uint8_t)(local_r11);
    if ((uint8_t)(result) != 0) { local_rdi = 1; }
    if (0 != 0) goto loc_0090FA38;
    *(uint8_t *)(v_rip + 0x6B7172) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))));
    if ((*(uint64_t *)(v_rip + 0x5FC5A1)) == ((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))))) goto loc_0090FD01;
    result = MmZeroPageFileAtShutdown(13, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a2 = *(uint64_t *)(v_rip + 0x5FC585);
        Arg1 = *(uint64_t *)(v_rip + 0x5FC576);
        result = PopZeroHiberFile(Arg1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_rip + 0x5FC572), (uint32_t)(0x62486F50ULL), a3, a4);
    result = ZwClose(*(uint64_t *)(v_rip + 0x5FC559), (uint32_t)(0x62486F50ULL), a3, a4);
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x5FC565), (uint32_t)(0x72626968ULL), a3, a4);
    *(uint64_t *)(v_rip + 0x5FC54B) = v_xmm0;
    *(uint8_t *)(v_rip + 0x5FD4C5) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))));
    *(uint8_t *)(v_rip + 0x5FD4CD) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))));
    *(uint8_t *)(v_rip + 0x5FD4C3) = (uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))));
    *(uint64_t *)(v_rip + 0x5FC542) = (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
    result = PopResetCurrentPolicies(*(uint64_t *)(v_rip + 0x5FC565), (uint32_t)(0x72626968ULL), a3, a4);
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    if (!sign_flag) goto loc_0090FD04;
loc_0090FA2A:
    if (Arg1 != 0) goto loc_0090FC7B;
    goto loc_0090FD04;
loc_0090FA38:
    if ((*(uint64_t *)(v_rip + 0x5FC4E9)) != ((uint32_t)((uint32_t)(result)))) goto loc_0090FD01;
    *(uint32_t *)(v_rip + 0x5FC515) = (uint32_t)(result);
    *(uint32_t *)(v_rip + 0x5FC4EB) = 0x641ULL;
    *(uint8_t *)(v_rip + 0x5FC502) = (uint8_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_rip + 0x5FC593) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = PopOpenPowerKey(local_rsp - 95 - 33, (uint32_t)(0x72626968ULL), a3, a4);
    if (sign_flag) goto loc_0090FBA0;
    result = RtlInitUnicodeString(local_rsp - 95 - 25, v_rip + 2040823, a3, a4);
    v_stack_mA0 = local_rsp - 95 - 41;
    v_stack_mA8 = 20;
    result = ZwQueryValueKey(*(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 - 25, 2, local_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FAD7;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1B)) != 4) goto loc_0090FAD7;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1F)) != 4) goto loc_0090FAD7;
    *(uint32_t *)(v_rip + 0x5FC49E) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x23)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x23))) - 1);
    if (((uint32_t)(result)) >= = 98) {
        *(uint32_t *)(v_rip + 0x5FC48D) = 1;
    }
    result = RtlInitUnicodeString(local_rsp - 95 - 9, v_rip + 2040754, 2, local_rsp - 95 + 23);
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x27) = 0;
    v_stack_mA0 = local_rsp - 95 - 41;
    v_stack_mA8 = 20;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    result = ZwQueryValueKey(*(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 - 9, 2, local_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FB33;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1B)) != 4) goto loc_0090FB33;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1F)) == 4) {
        result = *(uint32_t *)(local_rsp - 0x5F + 0x23);
        *(uint32_t *)(v_rip + 0x5FC411) = (uint32_t)(result);
    }
    result = RtlInitUnicodeString(local_rsp - 95 + 7, v_rip + 2040710, 2, local_rsp - 95 + 23);
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x27) = 0;
    v_stack_mA0 = local_rsp - 95 - 41;
    v_stack_mA8 = 20;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = v_xmm0;
    result = ZwQueryValueKey(*(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 + 7, 2, local_rsp - 95 + 23);
    if (sign_flag) goto loc_0090FB98;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1B)) != 4) goto loc_0090FB98;
    if ((*(uint32_t *)(local_rsp - 0x5F + 0x1F)) == 4) {
    }
    result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x21), local_rsp - 95 + 7, 2, local_rsp - 95 + 23);
loc_0090FBA0:
    *(uint8_t *)(v_rip + 0x6B6F58) = 1;
    if ((uint8_t)(local_rdi) == 0) goto loc_0090FBB6;
    goto loc_0090FC56;
loc_0090FBB6:
    result = MmAllocateDumpHibernateResources((uint32_t)(0x13000ULL), local_rsp - 95 + 7, 2, local_rsp - 95 + 23);
    if (result != 0) goto loc_0090FBD1;
    goto loc_0090FC51;
loc_0090FBD1:
    local_rdi = result + 2097152;
    if (((result) & (0x1FFFFFULL)) != 0) {
        local_rdi = (result + 2097152) - 1;
        local_rdi = (local_rdi) & (0xFFFFFFFFFFE00000ULL);
    }
    result = (local_rdi) - (result);
    if (result >= 0xA000ULL) { local_rdi = result; }
    result = PopCalculateHiberFileSize(local_rsp - 95 - 49, local_rsp - 95 - 57, 2, local_rsp - 95 + 23);
    result = PopCreateHiberFile(*(uint64_t *)(local_rsp - 0x5F - 0x31), local_rsp - 95 - 57, 2, local_rsp - 95 + 23);
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    if (!sign_flag) goto loc_0090FC22;
    goto loc_0090FC79;
loc_0090FC22:
    *(uint64_t *)(v_rip + 0x5FC31F) = result;
    local_rsi = 0;
    *(uint64_t *)(v_rip + 0x5FC319) = local_rdi;
    result = ExAllocatePool2(local_rsi + 64, 496, (uint32_t)(0x70616D48ULL), local_rsp - 95 + 23);
    if (result != 0) goto loc_0090FC5D;
loc_0090FC51:
loc_0090FC56:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0090FC7B;
loc_0090FC5D:
    *(uint64_t *)(v_rip + 0x5FC304) = result;
    local_r15 = 0;
    result = PopPreallocateHibernateMemory((uint32_t)(0xC000009AULL), 496, (uint32_t)(0x70616D48ULL), local_rsp - 95 + 23);
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(result);
    if (!sign_flag) goto loc_0090FCA5;
loc_0090FC79:
loc_0090FC7B:
    if (((*(uint32_t *)(v_rip + 0x5FC65B)) & (0x800ULL)) == 0) goto loc_0090FD04;
    a4 = (local_rsp - 95 + 23) | (-1);
    v_stack_mA8 = (uint32_t)((uint32_t)(local_r15 + 25));
    result = KeBugCheckEx(160, a4 + 10, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
loc_0090FCA5:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 1;
    result = EmClientQueryRuleState(v_rip - 9333357, local_rsp - 95 - 49, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x31)) == 2) {
        *(uint8_t *)(v_rip + 0x5FC291) = 1;
    }
    *(uint8_t *)(v_rip + 0x5FD1F7) = (uint8_t)(*(uint8_t *)(local_rsp - 0x5F - 0x39));
    *(uint8_t *)(v_rip + 0x5FD1E3) = 1;
    if ((*(uint32_t *)(v_rip + 0x6B44EE)) == 0) {
        *(uint8_t *)(v_rip + 0x5FD1E5) = 1;
    }
    result = *(uint8_t *)(local_rsp - 0x5F - 0x39);
    if (((*(uint8_t *)(v_rip + 0x5578D5)) & (1)) == 0) {
        result = PopClearHiberFileSignature(v_rip - 9333357, local_rsp - 95 - 49, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    }
    result = PopResetCurrentPolicies(v_rip - 9333357, local_rsp - 95 - 49, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    local_rbx = 0;
loc_0090FD01:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0;
loc_0090FD04:
    if ((uint32_t)(local_r15 + 25) != 0) {
        a4 = 4;
        a3 = local_rsp - 95 - 49;
        Arg1 = (uint32_t)(local_r15 + 25);
        a2 = a4 + 4;
        result = PopLogSleepDisabled(Arg1, a2, a3, a4);
        local_rbx = *(uint32_t *)(local_rsp - 0x5F - 0x31);
    }
    if (0 != 0) {
        a2 = 0x13000ULL;
        Arg1 = 0;
        result = MmReleaseDumpHibernateResources(Arg1, a2, a3, a4);
    }
    if (*(uint64_t *)(v_rip + 0x5FC582) != 0) {
        a2 = *(uint64_t *)(v_rip + 0x5FC238);
        Arg1 = *(uint64_t *)(v_rip + 0x5FC582);
        result = MmReturnChargesToLockPagedPool(Arg1, a2, a3, a4);
        a2 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x5FC582);
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
        a2 = 0;
        Arg1 = v_rip + 6275605;
        a3 = 136;
        result = memset(Arg1, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0x70616D48ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    if (Arg1 == 0) {
        a2 = 0;
        Arg1 = v_rip + 6275474;
        a3 = 232;
        result = memset(Arg1, a2, a3, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090F850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
