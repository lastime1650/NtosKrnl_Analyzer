# sub_00B1B2E4

- RVA: `0x00B1B2E4`–`0x00B1B7BF` (길이 `1,243` bytes)
- VA: `0x0000000140B1B2E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000844A8`
- 디코드: `255`개 명령, `1,243/1,243` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B1B318` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00B1B36B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00B1B3A0` → [KeDisableProfiling](../../text/4E/KeDisableProfiling_function_004E32BC.md) (function, `0x004E32BC`)
- `0x00B1B3C3` → [KeEnableProfiling](../AC/KeEnableProfiling_function_00ACED24.md) (function, `0x00ACED24`)
- `0x00B1B431` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00B1B457` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B1B46E` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (function, `0x00392F20`)
- `0x00B1B47F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B1B4AA` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (function, `0x00392F20`)
- `0x00B1B4BC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B1B4FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B1B53C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00B1B55D` → [KeSetSelectedCpuSetsThread](../../text/30/KeSetSelectedCpuSetsThread_function_003033D0.md) (function, `0x003033D0`)
- `0x00B1B5D7` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x00B1B632` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00B1B659` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B1B669` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (function, `0x00448540`)
- `0x00B1B674` → [PsGetProcessSilo](../../text/41/PsGetProcessSilo_function_00418580.md) (function, `0x00418580`)
- `0x00B1B67F` → [PspIsSiloInSilo](../A6/PspIsSiloInSilo_function_00A6EC8C.md) (function, `0x00A6EC8C`)
- `0x00B1B68B` → [PsGetEffectiveServerSilo](../../text/22/PsGetEffectiveServerSilo_function_002257F0.md) (function, `0x002257F0`)
- `0x00B1B696` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00B1B6A3` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x00B1B6B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B1B71E` → [KeUpdateThreadCpuSets](../../text/30/KeUpdateThreadCpuSets_function_0030305C.md) (function, `0x0030305C`)
- `0x00B1B785` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B1B33E` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x00B1B406` → RVA `0x00FC6E08` (`ALMOSTRO`; read)
- `0x00B1B5FF` → RVA `0x00FC6C58` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00B1B3A0` → [KeDisableProfiling](../../text/4E/KeDisableProfiling_function_004E32BC.md) (`PAGE` → `.text`)
  - `0x00B1B457` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00B1B46E` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (`PAGE` → `.text`)
  - `0x00B1B47F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00B1B4AA` → [KeSetThreadChargeOnlySchedulingGroup](../../text/39/KeSetThreadChargeOnlySchedulingGroup_function_00392F20.md) (`PAGE` → `.text`)
  - `0x00B1B4BC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00B1B4FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B1B55D` → [KeSetSelectedCpuSetsThread](../../text/30/KeSetSelectedCpuSetsThread_function_003033D0.md) (`PAGE` → `.text`)
  - `0x00B1B5D7` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x00B1B659` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00B1B669` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (`PAGE` → `.text`)
  - `0x00B1B674` → [PsGetProcessSilo](../../text/41/PsGetProcessSilo_function_00418580.md) (`PAGE` → `.text`)
  - `0x00B1B68B` → [PsGetEffectiveServerSilo](../../text/22/PsGetEffectiveServerSilo_function_002257F0.md) (`PAGE` → `.text`)
  - `0x00B1B696` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00B1B6A3` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x00B1B6B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00B1B71E` → [KeUpdateThreadCpuSets](../../text/30/KeUpdateThreadCpuSets_function_0030305C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **41**
  - `0x00B1B2E8` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B339` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B372` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B3A7` → [NtSetInformationThread + 0x44F](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B3CF` → [NtSetInformationThread + 0x44F](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B3DA` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B3E4` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B3F8` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B438` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B461` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B489` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B496` → [NtSetInformationThread + 0x509](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B4C9` → [NtSetInformationThread + 0x509](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B4D3` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B4DC` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B4E9` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B504` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B543` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B564` → [NtSetInformationThread + 0xCFE](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B56B` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B57D` → [NtSetInformationThread + 0x509](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B588` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B592` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B5A6` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B5CA` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B5E4` → [NtSetInformationThread + 0x504](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B5F9` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B639` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B65F` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B6A9` → [NtSetInformationThread + 0x509](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B6BD` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B6DB` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B6EE` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B6F6` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B724` → [NtSetInformationThread + 0x509](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B72D` → [NtSetInformationThread + 0x598](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B748` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B750` → [NtSetInformationThread + 0x389](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B78C` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B7B0` → [NtSetInformationThread + 0x4FF](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)
  - `0x00B1B7BA` → [NtSetInformationThread + 0x1A13](../8C/NtSetInformationThread_function_008C9F60.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1B2E4  41 83 FF 18                     cmp r15d, 0x18
00B1B2E8  0F 85 0A F2 DA FF               jne 0x1408ca4f8
00B1B2EE  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00B1B2F3  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
00B1B2FB  F2 41 0F 10 4C 24 10            movsd xmm1, qword ptr [r12 + 0x10]
00B1B302  F2 0F 11 8C 24 E0 00 00 00      movsd qword ptr [rsp + 0xe0], xmm1
00B1B30B  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00B1B313  F6 C1 03                        test cl, 3
00B1B316  74 06                           je 0x140b1b31e
00B1B318  E8 B3 EC D7 FF                  call 0x140899fd0
00B1B31D  CC                              int3
00B1B31E  48 3B CA                        cmp rcx, rdx
00B1B321  48 0F 43 CA                     cmovae rcx, rdx
00B1B325  0F B6 01                        movzx eax, byte ptr [rcx]
00B1B328  88 01                           mov byte ptr [rcx], al
00B1B32A  0F B6 81 BF 01 00 00            movzx eax, byte ptr [rcx + 0x1bf]
00B1B331  88 81 BF 01 00 00               mov byte ptr [rcx + 0x1bf], al
00B1B337  EB 05                           jmp 0x140b1b33e
00B1B339  E9 35 06 DB FF                  jmp 0x1408cb973
00B1B33E  4C 8B 05 83 B7 4A 00            mov r8, qword ptr [rip + 0x4ab783]
00B1B345  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B1B34A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B1B34F  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00B1B354  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1B359  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00B1B361  BA 20 00 00 00                  mov edx, 0x20
00B1B366  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00B1B36B  E8 E0 E2 D4 FF                  call 0x140869650
00B1B370  85 C0                           test eax, eax
00B1B372  0F 88 FB 05 DB FF               js 0x1408cb973
00B1B378  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B1B381  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00B1B386  48 3B D8                        cmp rbx, rax
00B1B389  75 3F                           jne 0x140b1b3ca
00B1B38B  48 8B CB                        mov rcx, rbx
00B1B38E  83 BC 24 DC 00 00 00 00         cmp dword ptr [rsp + 0xdc], 0
00B1B396  75 14                           jne 0x140b1b3ac
00B1B398  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00B1B3A0  E8 17 7F 9C FF                  call 0x1404e32bc
00B1B3A5  8B F0                           mov esi, eax
00B1B3A7  E9 03 F0 DA FF                  jmp 0x1408ca3af
00B1B3AC  4C 8B 8C 24 E0 00 00 00         mov r9, qword ptr [rsp + 0xe0]
00B1B3B4  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
00B1B3BC  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00B1B3C3  E8 5C 39 FB FF                  call 0x140aced24
00B1B3C8  EB DB                           jmp 0x140b1b3a5
00B1B3CA  BE BB 00 00 C0                  mov esi, 0xc00000bb
00B1B3CF  E9 DB EF DA FF                  jmp 0x1408ca3af
00B1B3D4  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
00B1B3DA  0F 85 09 EF DA FF               jne 0x1408ca2e9
00B1B3E0  41 83 FF 08                     cmp r15d, 8
00B1B3E4  0F 85 0E F1 DA FF               jne 0x1408ca4f8
00B1B3EA  49 8B 0C 24                     mov rcx, qword ptr [r12]
00B1B3EE  48 89 8C 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rcx
00B1B3F6  EB 05                           jmp 0x140b1b3fd
00B1B3F8  E9 76 05 DB FF                  jmp 0x1408cb973
00B1B3FD  48 85 C9                        test rcx, rcx
00B1B400  0F 84 95 00 00 00               je 0x140b1b49b
00B1B406  4C 8B 05 FB B9 4A 00            mov r8, qword ptr [rip + 0x4ab9fb]
00B1B40D  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B1B412  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B1B417  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
00B1B41F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1B424  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00B1B42C  BA 02 00 00 00                  mov edx, 2
00B1B431  E8 1A E2 D4 FF                  call 0x140869650
00B1B436  85 C0                           test eax, eax
00B1B438  0F 88 35 05 DB FF               js 0x1408cb973
00B1B43E  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00B1B446  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
00B1B44A  48 85 D2                        test rdx, rdx
00B1B44D  75 17                           jne 0x140b1b466
00B1B44F  BA 50 73 51 79                  mov edx, 0x79517350
00B1B454  48 8B CB                        mov rcx, rbx
00B1B457  E8 84 C4 7D FF                  call 0x1402f78e0
00B1B45C  B8 55 04 00 C0                  mov eax, 0xc0000455
00B1B461  E9 0D 05 DB FF                  jmp 0x1408cb973
00B1B466  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00B1B46B  49 8B CC                        mov rcx, r12
00B1B46E  E8 AD 7A 87 FF                  call 0x140392f20
00B1B473  84 C0                           test al, al
00B1B475  75 17                           jne 0x140b1b48e
00B1B477  BA 50 73 51 79                  mov edx, 0x79517350
00B1B47C  48 8B CB                        mov rcx, rbx
00B1B47F  E8 5C C4 7D FF                  call 0x1402f78e0
00B1B484  B8 56 04 00 C0                  mov eax, 0xc0000456
00B1B489  E9 E5 04 DB FF                  jmp 0x1408cb973
00B1B48E  49 89 9C 24 68 05 00 00         mov qword ptr [r12 + 0x568], rbx
00B1B496  E9 CE EF DA FF                  jmp 0x1408ca469
00B1B49B  49 83 B8 68 05 00 00 00         cmp qword ptr [r8 + 0x568], 0
00B1B4A3  74 29                           je 0x140b1b4ce
00B1B4A5  33 D2                           xor edx, edx
00B1B4A7  49 8B C8                        mov rcx, r8
00B1B4AA  E8 71 7A 87 FF                  call 0x140392f20
00B1B4AF  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00B1B4B4  49 8B 8C 24 68 05 00 00         mov rcx, qword ptr [r12 + 0x568]
00B1B4BC  E8 8F DE 7D FF                  call 0x1402f9350
00B1B4C1  49 89 BC 24 68 05 00 00         mov qword ptr [r12 + 0x568], rdi
00B1B4C9  E9 9B EF DA FF                  jmp 0x1408ca469
00B1B4CE  B8 57 04 00 C0                  mov eax, 0xc0000457
00B1B4D3  E9 9B 04 DB FF                  jmp 0x1408cb973
00B1B4D8  41 F6 C7 07                     test r15b, 7
00B1B4DC  0F 85 16 F0 DA FF               jne 0x1408ca4f8
00B1B4E2  41 81 FF 00 01 00 00            cmp r15d, 0x100
00B1B4E9  0F 87 09 F0 DA FF               ja 0x1408ca4f8
00B1B4EF  4D 8B C7                        mov r8, r15
00B1B4F2  49 8B D4                        mov rdx, r12
00B1B4F5  48 8D 8C 24 C0 02 00 00         lea rcx, [rsp + 0x2c0]
00B1B4FD  E8 3E B3 BA FF                  call 0x1406c6840
00B1B502  EB 05                           jmp 0x140b1b509
00B1B504  E9 6A 04 DB FF                  jmp 0x1408cb973
00B1B509  4C 8B 05 B8 B5 4A 00            mov r8, qword ptr [rip + 0x4ab5b8]
00B1B510  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B1B515  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B1B51A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00B1B51F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1B524  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00B1B52C  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
00B1B532  BA 00 04 00 00                  mov edx, 0x400
00B1B537  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00B1B53C  E8 0F E1 D4 FF                  call 0x140869650
00B1B541  85 C0                           test eax, eax
00B1B543  0F 88 2A 04 DB FF               js 0x1408cb973
00B1B549  41 C1 EF 03                     shr r15d, 3
00B1B54D  4C 8D 84 24 C0 02 00 00         lea r8, [rsp + 0x2c0]
00B1B555  41 8B D7                        mov edx, r15d
00B1B558  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B1B55D  E8 6E 7E 7E FF                  call 0x1403033d0
00B1B562  8B D8                           mov ebx, eax
00B1B564  E9 F5 F6 DA FF                  jmp 0x1408cac5e
00B1B569  85 C0                           test eax, eax
00B1B56B  0F 85 78 ED DA FF               jne 0x1408ca2e9
00B1B571  F0 41 81 A0 A0 05 00 00 FF FF FB FF  lock and dword ptr [r8 + 0x5a0], 0xfffbffff
00B1B57D  E9 E7 EE DA FF                  jmp 0x1408ca469
00B1B582  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
00B1B588  0F 85 5B ED DA FF               jne 0x1408ca2e9
00B1B58E  41 83 FF 08                     cmp r15d, 8
00B1B592  0F 85 60 EF DA FF               jne 0x1408ca4f8
00B1B598  49 8B 04 24                     mov rax, qword ptr [r12]
00B1B59C  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00B1B5A4  EB 05                           jmp 0x140b1b5ab
00B1B5A6  E9 C8 03 DB FF                  jmp 0x1408cb973
00B1B5AB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B1B5B4  48 83 BC 24 F0 00 00 00 00      cmp qword ptr [rsp + 0xf0], 0
00B1B5BD  75 2A                           jne 0x140b1b5e9
00B1B5BF  48 8B 80 98 06 00 00            mov rax, qword ptr [rax + 0x698]
00B1B5C6  48 83 F8 FD                     cmp rax, -3
00B1B5CA  0F 84 19 ED DA FF               je 0x1408ca2e9
00B1B5D0  48 C7 C1 FD FF FF FF            mov rcx, 0xfffffffffffffffd
00B1B5D7  E8 E4 72 92 FF                  call 0x1404428c0
00B1B5DC  BA 50 73 49 6D                  mov edx, 0x6d497350
00B1B5E1  48 8B C8                        mov rcx, rax
00B1B5E4  E9 7B EE DA FF                  jmp 0x1408ca464
00B1B5E9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B1B5EE  48 8B 80 98 06 00 00            mov rax, qword ptr [rax + 0x698]
00B1B5F5  48 83 F8 FD                     cmp rax, -3
00B1B5F9  0F 85 EA EC DA FF               jne 0x1408ca2e9
00B1B5FF  4C 8B 05 52 B6 4A 00            mov r8, qword ptr [rip + 0x4ab652]
00B1B606  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B1B60B  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B1B610  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00B1B618  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1B61D  C7 44 24 20 50 73 49 6D         mov dword ptr [rsp + 0x20], 0x6d497350
00B1B625  BA 20 00 00 00                  mov edx, 0x20
00B1B62A  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00B1B632  E8 19 E0 D4 FF                  call 0x140869650
00B1B637  85 C0                           test eax, eax
00B1B639  0F 88 34 03 DB FF               js 0x1408cb973
00B1B63F  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
00B1B647  8B 87 14 06 00 00               mov eax, dword ptr [rdi + 0x614]
00B1B64D  A8 02                           test al, 2
00B1B64F  75 13                           jne 0x140b1b664
00B1B651  BA 50 73 49 6D                  mov edx, 0x6d497350
00B1B656  48 8B CF                        mov rcx, rdi
00B1B659  E8 82 C2 7D FF                  call 0x1402f78e0
00B1B65E  90                              nop
00B1B65F  E9 85 EC DA FF                  jmp 0x1408ca2e9
00B1B664  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B1B669  E8 D2 CE 92 FF                  call 0x140448540
00B1B66E  48 8B F0                        mov rsi, rax
00B1B671  48 8B C8                        mov rcx, rax
00B1B674  E8 07 CF 8F FF                  call 0x140418580
00B1B679  48 8B D0                        mov rdx, rax
00B1B67C  48 8B CF                        mov rcx, rdi
00B1B67F  E8 08 36 F5 FF                  call 0x140a6ec8c
00B1B684  48 8B CF                        mov rcx, rdi
00B1B687  84 C0                           test al, al
00B1B689  74 23                           je 0x140b1b6ae
00B1B68B  E8 60 A1 70 FF                  call 0x1402257f0
00B1B690  48 8B D8                        mov rbx, rax
00B1B693  48 8B CE                        mov rcx, rsi
00B1B696  E8 45 08 93 FF                  call 0x14044bee0
00B1B69B  48 8B CF                        mov rcx, rdi
00B1B69E  48 3B C3                        cmp rax, rbx
00B1B6A1  75 0B                           jne 0x140b1b6ae
00B1B6A3  E8 18 72 92 FF                  call 0x1404428c0
00B1B6A8  90                              nop
00B1B6A9  E9 BB ED DA FF                  jmp 0x1408ca469
00B1B6AE  BA 50 73 49 6D                  mov edx, 0x6d497350
00B1B6B3  E8 28 C2 7D FF                  call 0x1402f78e0
00B1B6B8  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B1B6BD  E9 B1 02 DB FF                  jmp 0x1408cb973
00B1B6C2  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
00B1B6C8  0F 85 E7 00 00 00               jne 0x140b1b7b5
00B1B6CE  45 84 C9                        test r9b, r9b
00B1B6D1  0F 85 DE 00 00 00               jne 0x140b1b7b5
00B1B6D7  41 83 FF 04                     cmp r15d, 4
00B1B6DB  0F 85 17 EE DA FF               jne 0x1408ca4f8
00B1B6E1  41 8B 14 24                     mov edx, dword ptr [r12]
00B1B6E5  89 94 24 28 01 00 00            mov dword ptr [rsp + 0x128], edx
00B1B6EC  EB 05                           jmp 0x140b1b6f3
00B1B6EE  E9 80 02 DB FF                  jmp 0x1408cb973
00B1B6F3  83 FA 02                        cmp edx, 2
00B1B6F6  0F 83 ED EB DA FF               jae 0x1408ca2e9
00B1B6FC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00B1B705  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
00B1B70B  C1 E2 0B                        shl edx, 0xb
00B1B70E  33 D0                           xor edx, eax
00B1B710  81 E2 00 08 00 00               and edx, 0x800
00B1B716  33 D0                           xor edx, eax
00B1B718  89 91 A4 05 00 00               mov dword ptr [rcx + 0x5a4], edx
00B1B71E  E8 39 79 7E FF                  call 0x14030305c
00B1B723  90                              nop
00B1B724  E9 40 ED DA FF                  jmp 0x1408ca469
00B1B729  41 83 FF 04                     cmp r15d, 4
00B1B72D  0F 85 C5 ED DA FF               jne 0x1408ca4f8
00B1B733  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
00B1B739  75 7A                           jne 0x140b1b7b5
00B1B73B  41 8B 1C 24                     mov ebx, dword ptr [r12]
00B1B73F  89 9C 24 24 01 00 00            mov dword ptr [rsp + 0x124], ebx
00B1B746  EB 05                           jmp 0x140b1b74d
00B1B748  E9 26 02 DB FF                  jmp 0x1408cb973
00B1B74D  83 FB 01                        cmp ebx, 1
00B1B750  0F 87 93 EB DA FF               ja 0x1408ca2e9
00B1B756  4C 8B 05 6B B3 4A 00            mov r8, qword ptr [rip + 0x4ab36b]
00B1B75D  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00B1B762  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00B1B767  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00B1B76C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1B771  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00B1B779  BA 20 00 00 00                  mov edx, 0x20
00B1B77E  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
00B1B785  E8 C6 DE D4 FF                  call 0x140869650
00B1B78A  85 C0                           test eax, eax
00B1B78C  0F 88 E1 01 DB FF               js 0x1408cb973
00B1B792  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B1B797  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
00B1B79D  C1 E3 0C                        shl ebx, 0xc
00B1B7A0  33 D8                           xor ebx, eax
00B1B7A2  81 E3 00 10 00 00               and ebx, 0x1000
00B1B7A8  33 D8                           xor ebx, eax
00B1B7AA  89 99 A4 05 00 00               mov dword ptr [rcx + 0x5a4], ebx
00B1B7B0  E9 AA EC DA FF                  jmp 0x1408ca45f
00B1B7B5  B8 22 00 00 C0                  mov eax, 0xc0000022
00B1B7BA  E9 B4 01 DB FF                  jmp 0x1408cb973
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1B2E4(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, unsigned int a27, __int64 a28)
{
    __int64 result;
    unsigned int v_stack_p124;
    unsigned int v_stack_p128;
    unsigned __int64 v_stack_p1A0;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p2C0;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pDC;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;

    a26 = v_xmm0;
    v_stack_pE0 = v_xmm1;
    if ((((unsigned __int8)(a28)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a28, a2, a3, a4);
    }
    if (a28 >= a2) { a28 = a2; }
    *(unsigned __int8 *)(a28) = (unsigned __int8)(*(unsigned __int8 *)(a28));
    *(unsigned __int8 *)(a28 + 447) = (unsigned __int8)(*(unsigned __int8 *)(a28 + 447));
    goto loc_00B1B33E;
loc_00B1B33E:
    v_stack_p38 = v_rdi;
    v_stack_p30 = v_rdi;
    v_stack_p28 = a9;
    v_stack_p20 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(a11, 32, *(unsigned __int64 *)(v_rip + 4896643), a4);
    if (a9 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00B1B3CA;
    if (v_stack_pDC != 0) goto loc_00B1B3AC;
    result = KeDisableProfiling(a9, a28, *(unsigned __int64 *)(v_rip + 4896643), a4);
loc_00B1B3A5:
loc_00B1B3AC:
    result = KeEnableProfiling(a9, (unsigned int)(a27), a26, a28);
    goto loc_00B1B3A5;
loc_00B1B3CA:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B1B2E4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9, uint64_t Arg10, int64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, int64_t Arg26, uint32_t Arg27, int64_t Arg28)
{
    int64_t result;
    uint32_t v_stack_p124;
    uint32_t v_stack_p128;
    uint64_t v_stack_p1A0;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p2C0;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pDC;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;

    Arg26 = v_xmm0;
    v_stack_pE0 = v_xmm1;
    if ((((uint8_t)(Arg28)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg28, Arg2, Arg3, Arg4);
    }
    if (Arg28 >= Arg2) { Arg28 = Arg2; }
    *(uint8_t *)(Arg28) = (uint8_t)(*(uint8_t *)(Arg28));
    *(uint8_t *)(Arg28 + 0x1BF) = (uint8_t)(*(uint8_t *)(Arg28 + 0x1BF));
    goto loc_00B1B33E;
loc_00B1B33E:
    v_stack_p38 = local_rdi;
    v_stack_p30 = local_rdi;
    v_stack_p28 = Arg9;
    v_stack_p20 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg11, 32, *(uint64_t *)(v_rip + 0x4AB783), Arg4);
    if (Arg9 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00B1B3CA;
    if (v_stack_pDC != 0) goto loc_00B1B3AC;
    result = KeDisableProfiling(Arg9, Arg28, *(uint64_t *)(v_rip + 0x4AB783), Arg4);
loc_00B1B3A5:
loc_00B1B3AC:
    result = KeEnableProfiling(Arg9, (uint32_t)(Arg27), Arg26, Arg28);
    goto loc_00B1B3A5;
loc_00B1B3CA:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1B2E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
