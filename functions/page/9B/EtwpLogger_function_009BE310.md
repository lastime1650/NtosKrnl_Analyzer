# EtwpLogger

- RVA: `0x009BE310`–`0x009BE913` (길이 `1,539` bytes)
- VA: `0x00000001409BE310`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009F314`
- 디코드: `355`개 명령, `1,539/1,539` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x009BE352` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x009BE36D` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x009BE39E` → [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) (function, `0x008C9F60`)
- `0x009BE3C7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009BE435` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x009BE457` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009BE472` → [EtwpAdjustFreeBuffers](EtwpAdjustFreeBuffers_function_009BE91C.md) (function, `0x009BE91C`)
- `0x009BE4F3` → [EtwpFlushActiveBuffers](EtwpFlushActiveBuffers_function_009BDEF4.md) (function, `0x009BDEF4`)
- `0x009BE562` → [EtwpFlushActiveBuffers](EtwpFlushActiveBuffers_function_009BDEF4.md) (function, `0x009BDEF4`)
- `0x009BE578` → [EtwpRealtimeCreateLogfile](EtwpRealtimeCreateLogfile_function_009BE96C.md) (function, `0x009BE96C`)
- `0x009BE5A0` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009BE5B2` → [EtwpStopLoggerInstance](EtwpStopLoggerInstance_function_009BEB94.md) (function, `0x009BEB94`)
- `0x009BE5BF` → [EtwpRealtimeUpdateConsumers](EtwpRealtimeUpdateConsumers_function_009BEF80.md) (function, `0x009BEF80`)
- `0x009BE5C7` → [EtwpRealtimeFlushSavedBuffers](EtwpRealtimeFlushSavedBuffers_function_009BF1B0.md) (function, `0x009BF1B0`)
- `0x009BE5EB` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (function, `0x002FE6B0`)
- `0x009BE607` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009BE61C` → [EtwpRealtimeNotifyConsumers](../9C/EtwpRealtimeNotifyConsumers_function_009C019C.md) (function, `0x009C019C`)
- `0x009BE63F` → [EtwpCreateLogFile](../9C/EtwpCreateLogFile_function_009C035C.md) (function, `0x009C035C`)
- `0x009BE658` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009BE6BD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x009BE6C8` → [EtwpFlushActiveBuffers](EtwpFlushActiveBuffers_function_009BDEF4.md) (function, `0x009BDEF4`)
- `0x009BE706` → [EtwpFinalizeHeader](../9C/EtwpFinalizeHeader_function_009C1EF0.md) (function, `0x009C1EF0`)
- `0x009BE712` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009BE73A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009BE74A` → [EtwpFreeLoggerContext](../9C/EtwpFreeLoggerContext_function_009C1688.md) (function, `0x009C1688`)
- `0x009BE752` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x009BE759` → [PsTerminateSystemThread](PsTerminateSystemThread_function_009BCE50.md) (function, `0x009BCE50`)
- `0x009BE766` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009BE7A4` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x009BE7D6` → [EtwpFinalizeHeader](../9C/EtwpFinalizeHeader_function_009C1EF0.md) (function, `0x009C1EF0`)
- `0x009BE7FD` → [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) (function, `0x008C9F60`)
- `0x009BE80A` → [EtwpRealtimeSaveState](EtwpRealtimeSaveState_function_009BCBD4.md) (function, `0x009BCBD4`)
- `0x009BE816` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009BE82A` → [EtwpRealtimeDisconnectAllConsumers](../9C/EtwpRealtimeDisconnectAllConsumers_function_009C1DE4.md) (function, `0x009C1DE4`)
- `0x009BE845` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009BE87A` → [EtwpFlushActiveBuffers](EtwpFlushActiveBuffers_function_009BDEF4.md) (function, `0x009BDEF4`)
- `0x009BE8A3` → [EtwpFinalizeHeader](../9C/EtwpFinalizeHeader_function_009C1EF0.md) (function, `0x009C1EF0`)
- `0x009BE8DA` → [EtwpEventWriteTemplateSessionEnd](../AC/EtwpEventWriteTemplateSessionEnd_function_00ACEC4C.md) (function, `0x00ACEC4C`)
- `0x009BE8F2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009BE909` → [EtwpEventWriteTemplateSession](EtwpEventWriteTemplateSession_function_009BD120.md) (function, `0x009BD120`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009BE32F` → RVA `0x00E0A740` (`.data`; read)
- `0x009BE462` → RVA `0x00EFF284` (`.data`; read)
- `0x009BE592` → RVA `0x00EFF840` (`.data`; read)
- `0x009BE599` → RVA `0x00013D88` (`.rdata`; read)
- `0x009BE6A6` → RVA `0x00013DD0` (`.rdata`; read)
- `0x009BE8EB` → RVA `0x00013D68` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x009BE352` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x009BE36D` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (`PAGE` → `.text`)
  - `0x009BE3C7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009BE435` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (`PAGE` → `.text`)
  - `0x009BE457` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009BE5A0` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009BE5EB` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (`PAGE` → `.text`)
  - `0x009BE607` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009BE658` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009BE6BD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x009BE712` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009BE73A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009BE752` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x009BE766` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009BE7A4` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (`PAGE` → `.text`)
  - `0x009BE816` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009BE845` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009BE8F2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x009BE64A` → [sub_00B2E9EA](../B2/Unknown_function_00B2E9EA.md) (`tail-transfer`)
  - `0x009BE6E2` → [sub_00B2E9EA + 0x6A](../B2/Unknown_function_00B2E9EA.md) (`tail-transfer`)
  - `0x009BE6F2` → [sub_00B2E9EA + 0x6A](../B2/Unknown_function_00B2E9EA.md) (`tail-transfer`)
  - `0x009BE8AC` → [sub_00B2E9EA + 0x52](../B2/Unknown_function_00B2E9EA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009BE310  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009BE315  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
009BE31A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009BE31F  57                              push rdi
009BE320  41 54                           push r12
009BE322  41 55                           push r13
009BE324  41 56                           push r14
009BE326  41 57                           push r15
009BE328  48 81 EC 80 00 00 00            sub rsp, 0x80
009BE32F  48 8B 05 0A C4 44 00            mov rax, qword ptr [rip + 0x44c40a]
009BE336  48 33 C4                        xor rax, rsp
009BE339  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009BE33E  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
009BE342  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009BE34B  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
009BE34F  48 8B 09                        mov rcx, qword ptr [rcx]
009BE352  E8 69 45 A8 FF                  call 0x1404428c0
009BE357  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009BE360  BA 0F 00 00 00                  mov edx, 0xf
009BE365  48 8B E8                        mov rbp, rax
009BE368  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009BE36D  E8 FE 5F A0 FF                  call 0x1403c4370
009BE372  41 BE 01 00 00 00               mov r14d, 1
009BE378  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
009BE37D  48 C7 C7 FE FF FF FF            mov rdi, 0xfffffffffffffffe
009BE384  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
009BE389  48 8B CF                        mov rcx, rdi
009BE38C  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
009BE391  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
009BE396  45 8D 4E 0B                     lea r9d, [r14 + 0xb]
009BE39A  41 8D 56 30                     lea edx, [r14 + 0x30]
009BE39E  E8 BD BB F0 FF                  call 0x1408c9f60
009BE3A3  4C 8D A3 88 00 00 00            lea r12, [rbx + 0x88]
009BE3AA  45 33 FF                        xor r15d, r15d
009BE3AD  66 45 39 3C 24                  cmp word ptr [r12], r15w
009BE3B2  0F 87 28 04 00 00               ja 0x1409be7e0
009BE3B8  4C 8D AB C8 01 00 00            lea r13, [rbx + 0x1c8]
009BE3BF  45 33 C0                        xor r8d, r8d
009BE3C2  49 8B CD                        mov rcx, r13
009BE3C5  33 D2                           xor edx, edx
009BE3C7  E8 44 0F 98 FF                  call 0x14033f310
009BE3CC  48 8D 83 F8 01 00 00            lea rax, [rbx + 0x1f8]
009BE3D3  48 8D B3 E0 01 00 00            lea rsi, [rbx + 0x1e0]
009BE3DA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009BE3DF  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
009BE3E4  44 39 BB 40 01 00 00            cmp dword ptr [rbx + 0x140], r15d
009BE3EB  0F 84 D1 02 00 00               je 0x1409be6c2
009BE3F1  48 8D AB 30 03 00 00            lea rbp, [rbx + 0x330]
009BE3F8  8B 83 D0 00 00 00               mov eax, dword ptr [rbx + 0xd0]
009BE3FE  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
009BE403  41 8B CF                        mov ecx, r15d
009BE406  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
009BE40B  85 C0                           test eax, eax
009BE40D  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
009BE412  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
009BE417  48 8B FD                        mov rdi, rbp
009BE41A  48 0F 45 FD                     cmovne rdi, rbp
009BE41E  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
009BE423  0F 95 C1                        setne cl
009BE426  45 8B F7                        mov r14d, r15d
009BE429  45 33 C9                        xor r9d, r9d
009BE42C  FF C1                           inc ecx
009BE42E  45 8D 79 01                     lea r15d, [r9 + 1]
009BE432  45 8B C7                        mov r8d, r15d
009BE435  E8 D6 EC 84 FF                  call 0x14020d110
009BE43A  41 3B C7                        cmp eax, r15d
009BE43D  75 23                           jne 0x1409be462
009BE43F  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE445  0F BA E0 0A                     bt eax, 0xa
009BE449  73 09                           jae 0x1409be454
009BE44B  F0 0F BA B3 38 03 00 00 0A      lock btr dword ptr [rbx + 0x338], 0xa
009BE454  48 8B CE                        mov rcx, rsi
009BE457  E8 F4 9E 88 FF                  call 0x140248350
009BE45C  45 8B F7                        mov r14d, r15d
009BE45F  48 8B FD                        mov rdi, rbp
009BE462  80 3D 1B 0E 54 00 03            cmp byte ptr [rip + 0x540e1b], 3
009BE469  76 04                           jbe 0x1409be46f
009BE46B  F0 83 0F 04                     lock or dword ptr [rdi], 4
009BE46F  48 8B CB                        mov rcx, rbx
009BE472  E8 A5 04 00 00                  call 0x1409be91c
009BE477  44 8B BB 38 03 00 00            mov r15d, dword ptr [rbx + 0x338]
009BE47E  41 83 E7 04                     and r15d, 4
009BE482  0F 85 EB 01 00 00               jne 0x1409be673
009BE488  8B 45 00                        mov eax, dword ptr [rbp]
009BE48B  A8 04                           test al, 4
009BE48D  0F 84 C9 00 00 00               je 0x1409be55c
009BE493  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE499  84 C0                           test al, al
009BE49B  0F 88 16 03 00 00               js 0x1409be7b7
009BE4A1  F7 43 0C 00 01 00 00            test dword ptr [rbx + 0xc], 0x100
009BE4A8  0F 85 BE 00 00 00               jne 0x1409be56c
009BE4AE  F0 83 27 F7                     lock and dword ptr [rdi], 0xfffffff7
009BE4B2  8B 45 00                        mov eax, dword ptr [rbp]
009BE4B5  A8 08                           test al, 8
009BE4B7  0F 85 B8 00 00 00               jne 0x1409be575
009BE4BD  33 FF                           xor edi, edi
009BE4BF  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE4C5  A8 40                           test al, 0x40
009BE4C7  0F 85 44 01 00 00               jne 0x1409be611
009BE4CD  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE4D3  A8 08                           test al, 8
009BE4D5  0F 85 4C 03 00 00               jne 0x1409be827
009BE4DB  48 8D 73 28                     lea rsi, [rbx + 0x28]
009BE4DF  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE4E5  A8 03                           test al, 3
009BE4E7  0F 85 39 01 00 00               jne 0x1409be626
009BE4ED  41 8B D6                        mov edx, r14d
009BE4F0  48 8B CB                        mov rcx, rbx
009BE4F3  E8 FC F9 FF FF                  call 0x1409bdef4
009BE4F8  8B F8                           mov edi, eax
009BE4FA  33 ED                           xor ebp, ebp
009BE4FC  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE502  A8 01                           test al, 1
009BE504  0F 85 58 03 00 00               jne 0x1409be862
009BE50A  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE510  0F BA E0 0C                     bt eax, 0xc
009BE514  0F 82 6C 03 00 00               jb 0x1409be886
009BE51A  F6 43 0C 40                     test byte ptr [rbx + 0xc], 0x40
009BE51E  0F 45 FD                        cmovne edi, ebp
009BE521  45 85 FF                        test r15d, r15d
009BE524  0F 85 CB 00 00 00               jne 0x1409be5f5
009BE52A  45 33 FF                        xor r15d, r15d
009BE52D  85 FF                           test edi, edi
009BE52F  78 61                           js 0x1409be592
009BE531  48 8D B3 E0 01 00 00            lea rsi, [rbx + 0x1e0]
009BE538  48 8D AB 30 03 00 00            lea rbp, [rbx + 0x330]
009BE53F  44 39 BB 40 01 00 00            cmp dword ptr [rbx + 0x140], r15d
009BE546  0F 85 AC FE FF FF               jne 0x1409be3f8
009BE54C  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
009BE551  41 BE 01 00 00 00               mov r14d, 1
009BE557  E9 66 01 00 00                  jmp 0x1409be6c2
009BE55C  41 8B D6                        mov edx, r14d
009BE55F  48 8B CB                        mov rcx, rbx
009BE562  E8 8D F9 FF FF                  call 0x1409bdef4
009BE567  45 33 FF                        xor r15d, r15d
009BE56A  EB CC                           jmp 0x1409be538
009BE56C  F0 83 0F 08                     lock or dword ptr [rdi], 8
009BE570  E9 3D FF FF FF                  jmp 0x1409be4b2
009BE575  48 8B CB                        mov rcx, rbx
009BE578  E8 EF 03 00 00                  call 0x1409be96c
009BE57D  8B F8                           mov edi, eax
009BE57F  85 C0                           test eax, eax
009BE581  79 39                           jns 0x1409be5bc
009BE583  8B 4B 0C                        mov ecx, dword ptr [rbx + 0xc]
009BE586  F6 C1 40                        test cl, 0x40
009BE589  75 31                           jne 0x1409be5bc
009BE58B  48 8D 73 28                     lea rsi, [rbx + 0x28]
009BE58F  45 33 FF                        xor r15d, r15d
009BE592  48 8B 0D A7 12 54 00            mov rcx, qword ptr [rip + 0x5412a7]
009BE599  48 8D 15 E8 57 65 FF            lea rdx, [rip - 0x9aa818]
009BE5A0  E8 AB 3E 9D FF                  call 0x140392450
009BE5A5  84 C0                           test al, al
009BE5A7  0F 85 0C 03 00 00               jne 0x1409be8b9
009BE5AD  48 8B CB                        mov rcx, rbx
009BE5B0  89 3E                           mov dword ptr [rsi], edi
009BE5B2  E8 DD 05 00 00                  call 0x1409beb94
009BE5B7  E9 75 FF FF FF                  jmp 0x1409be531
009BE5BC  48 8B CB                        mov rcx, rbx
009BE5BF  E8 BC 09 00 00                  call 0x1409bef80
009BE5C4  48 8B CB                        mov rcx, rbx
009BE5C7  E8 E4 0B 00 00                  call 0x1409bf1b0
009BE5CC  33 FF                           xor edi, edi
009BE5CE  39 BB 58 01 00 00               cmp dword ptr [rbx + 0x158], edi
009BE5D4  0F 86 E5 FE FF FF               jbe 0x1409be4bf
009BE5DA  39 BB A8 01 00 00               cmp dword ptr [rbx + 0x1a8], edi
009BE5E0  0F 86 D9 FE FF FF               jbe 0x1409be4bf
009BE5E6  33 D2                           xor edx, edx
009BE5E8  48 8B CB                        mov rcx, rbx
009BE5EB  E8 C0 00 94 FF                  call 0x1402fe6b0
009BE5F0  E9 CA FE FF FF                  jmp 0x1409be4bf
009BE5F5  F0 83 A3 38 03 00 00 FB         lock and dword ptr [rbx + 0x338], 0xfffffffb
009BE5FD  45 33 C0                        xor r8d, r8d
009BE600  89 3E                           mov dword ptr [rsi], edi
009BE602  33 D2                           xor edx, edx
009BE604  49 8B CD                        mov rcx, r13
009BE607  E8 04 0D 98 FF                  call 0x14033f310
009BE60C  E9 19 FF FF FF                  jmp 0x1409be52a
009BE611  F0 83 A3 38 03 00 00 BF         lock and dword ptr [rbx + 0x338], 0xffffffbf
009BE619  48 8B CB                        mov rcx, rbx
009BE61C  E8 7B 1B 00 00                  call 0x1409c019c
009BE621  E9 A7 FE FF FF                  jmp 0x1409be4cd
009BE626  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE62C  40 B5 01                        mov bpl, 1
009BE62F  A8 02                           test al, 2
009BE631  0F 85 18 02 00 00               jne 0x1409be84f
009BE637  45 33 C0                        xor r8d, r8d
009BE63A  B2 01                           mov dl, 1
009BE63C  48 8B CB                        mov rcx, rbx
009BE63F  E8 18 1D 00 00                  call 0x1409c035c
009BE644  89 06                           mov dword ptr [rsi], eax
009BE646  8B F8                           mov edi, eax
009BE648  85 C0                           test eax, eax
009BE64A  0F 88 9A 03 17 00               js 0x140b2e9ea
009BE650  45 33 C0                        xor r8d, r8d
009BE653  33 D2                           xor edx, edx
009BE655  49 8B CD                        mov rcx, r13
009BE658  E8 B3 0C 98 FF                  call 0x14033f310
009BE65D  85 FF                           test edi, edi
009BE65F  0F 89 88 FE FF FF               jns 0x1409be4ed
009BE665  40 84 ED                        test bpl, bpl
009BE668  0F 85 21 FF FF FF               jne 0x1409be58f
009BE66E  E9 7A FE FF FF                  jmp 0x1409be4ed
009BE673  33 C9                           xor ecx, ecx
009BE675  39 8B D0 00 00 00               cmp dword ptr [rbx + 0xd0], ecx
009BE67B  0F 87 0C 01 00 00               ja 0x1409be78d
009BE681  41 BE 01 00 00 00               mov r14d, 1
009BE687  E9 FC FD FF FF                  jmp 0x1409be488
009BE68C  8B 8B E8 00 00 00               mov ecx, dword ptr [rbx + 0xe8]
009BE692  85 C9                           test ecx, ecx
009BE694  7E 62                           jle 0x1409be6f8
009BE696  8B 93 E8 00 00 00               mov edx, dword ptr [rbx + 0xe8]
009BE69C  8B 8B E4 00 00 00               mov ecx, dword ptr [rbx + 0xe4]
009BE6A2  3B D1                           cmp edx, ecx
009BE6A4  7E 52                           jle 0x1409be6f8
009BE6A6  48 8D 05 23 57 65 FF            lea rax, [rip - 0x9aa8dd]
009BE6AD  45 33 C9                        xor r9d, r9d
009BE6B0  45 33 C0                        xor r8d, r8d
009BE6B3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009BE6B8  33 D2                           xor edx, edx
009BE6BA  48 8B CE                        mov rcx, rsi
009BE6BD  E8 EE FF 84 FF                  call 0x14020e6b0
009BE6C2  41 8B D6                        mov edx, r14d
009BE6C5  48 8B CB                        mov rcx, rbx
009BE6C8  E8 27 F8 FF FF                  call 0x1409bdef4
009BE6CD  8B F8                           mov edi, eax
009BE6CF  85 C0                           test eax, eax
009BE6D1  78 25                           js 0x1409be6f8
009BE6D3  3D 03 01 00 00                  cmp eax, 0x103
009BE6D8  75 B2                           jne 0x1409be68c
009BE6DA  8B 83 30 03 00 00               mov eax, dword ptr [rbx + 0x330]
009BE6E0  A8 08                           test al, 8
009BE6E2  0F 84 6C 03 17 00               je 0x140b2ea54
009BE6E8  41 8B FF                        mov edi, r15d
009BE6EB  4C 39 BB 68 01 00 00            cmp qword ptr [rbx + 0x168], r15
009BE6F2  0F 85 5C 03 17 00               jne 0x140b2ea54
009BE6F8  4C 39 BB 20 03 00 00            cmp qword ptr [rbx + 0x320], r15
009BE6FF  74 1D                           je 0x1409be71e
009BE701  33 D2                           xor edx, edx
009BE703  48 8B CB                        mov rcx, rbx
009BE706  E8 E5 37 00 00                  call 0x1409c1ef0
009BE70B  48 8B 8B 20 03 00 00            mov rcx, qword ptr [rbx + 0x320]
009BE712  E8 99 EB CE FF                  call 0x1406ad2b0
009BE717  4C 89 BB 20 03 00 00            mov qword ptr [rbx + 0x320], r15
009BE71E  4C 39 BB 68 01 00 00            cmp qword ptr [rbx + 0x168], r15
009BE725  0F 85 DC 00 00 00               jne 0x1409be807
009BE72B  48 8D 8B C8 01 00 00            lea rcx, [rbx + 0x1c8]
009BE732  89 7B 28                        mov dword ptr [rbx + 0x28], edi
009BE735  45 33 C0                        xor r8d, r8d
009BE738  33 D2                           xor edx, edx
009BE73A  E8 D1 0B 98 FF                  call 0x14033f310
009BE73F  85 FF                           test edi, edi
009BE741  0F 88 9D 01 00 00               js 0x1409be8e4
009BE747  48 8B CB                        mov rcx, rbx
009BE74A  E8 39 2F 00 00                  call 0x1409c1688
009BE74F  48 8B CD                        mov rcx, rbp
009BE752  E8 69 B3 A8 FF                  call 0x140449ac0
009BE757  8B CF                           mov ecx, edi
009BE759  E8 F2 E6 FF FF                  call 0x1409bce50
009BE75E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009BE763  48 33 CC                        xor rcx, rsp
009BE766  E8 D5 DE CE FF                  call 0x1406ac640
009BE76B  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
009BE773  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
009BE777  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
009BE77B  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009BE77F  49 8B E3                        mov rsp, r11
009BE782  41 5F                           pop r15
009BE784  41 5E                           pop r14
009BE786  41 5D                           pop r13
009BE788  41 5C                           pop r12
009BE78A  5F                              pop rdi
009BE78B  C3                              ret
009BE78C  CC                              int3
009BE78D  8B 83 38 03 00 00               mov eax, dword ptr [rbx + 0x338]
009BE793  0F BA E0 0A                     bt eax, 0xa
009BE797  0F 83 E4 FE FF FF               jae 0x1409be681
009BE79D  48 8D 8B F8 01 00 00            lea rcx, [rbx + 0x1f8]
009BE7A4  E8 37 40 87 FF                  call 0x1402327e0
009BE7A9  F0 0F BA B3 38 03 00 00 0A      lock btr dword ptr [rbx + 0x338], 0xa
009BE7B2  E9 CA FE FF FF                  jmp 0x1409be681
009BE7B7  F0 81 A3 38 03 00 00 7F FF FF FF  lock and dword ptr [rbx + 0x338], 0xffffff7f
009BE7C2  33 F6                           xor esi, esi
009BE7C4  48 39 B3 20 03 00 00            cmp qword ptr [rbx + 0x320], rsi
009BE7CB  0F 84 D0 FC FF FF               je 0x1409be4a1
009BE7D1  B2 01                           mov dl, 1
009BE7D3  48 8B CB                        mov rcx, rbx
009BE7D6  E8 15 37 00 00                  call 0x1409c1ef0
009BE7DB  E9 C1 FC FF FF                  jmp 0x1409be4a1
009BE7E0  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
009BE7E5  41 B9 10 00 00 00               mov r9d, 0x10
009BE7EB  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
009BE7F0  48 8B CF                        mov rcx, rdi
009BE7F3  F3 0F 7F 44 24 58               movdqu xmmword ptr [rsp + 0x58], xmm0
009BE7F9  41 8D 51 16                     lea edx, [r9 + 0x16]
009BE7FD  E8 5E B7 F0 FF                  call 0x1408c9f60
009BE802  E9 B1 FB FF FF                  jmp 0x1409be3b8
009BE807  48 8B CB                        mov rcx, rbx
009BE80A  E8 C5 E3 FF FF                  call 0x1409bcbd4
009BE80F  48 8B 8B 68 01 00 00            mov rcx, qword ptr [rbx + 0x168]
009BE816  E8 95 EA CE FF                  call 0x1406ad2b0
009BE81B  4C 89 BB 68 01 00 00            mov qword ptr [rbx + 0x168], r15
009BE822  E9 04 FF FF FF                  jmp 0x1409be72b
009BE827  48 8B CB                        mov rcx, rbx
009BE82A  E8 B5 35 00 00                  call 0x1409c1de4
009BE82F  F0 83 A3 38 03 00 00 F7         lock and dword ptr [rbx + 0x338], 0xfffffff7
009BE837  48 8D 73 28                     lea rsi, [rbx + 0x28]
009BE83B  45 33 C0                        xor r8d, r8d
009BE83E  33 D2                           xor edx, edx
009BE840  89 3E                           mov dword ptr [rsi], edi
009BE842  49 8B CD                        mov rcx, r13
009BE845  E8 C6 0A 98 FF                  call 0x14033f310
009BE84A  E9 90 FC FF FF                  jmp 0x1409be4df
009BE84F  48 39 BB 20 03 00 00            cmp qword ptr [rbx + 0x320], rdi
009BE856  40 0F B6 ED                     movzx ebp, bpl
009BE85A  0F 45 EF                        cmovne ebp, edi
009BE85D  E9 D5 FD FF FF                  jmp 0x1409be637
009BE862  85 FF                           test edi, edi
009BE864  0F 88 A0 FC FF FF               js 0x1409be50a
009BE86A  45 85 F6                        test r14d, r14d
009BE86D  0F 85 97 FC FF FF               jne 0x1409be50a
009BE873  41 8D 56 01                     lea edx, [r14 + 1]
009BE877  48 8B CB                        mov rcx, rbx
009BE87A  E8 75 F6 FF FF                  call 0x1409bdef4
009BE87F  8B F8                           mov edi, eax
009BE881  E9 84 FC FF FF                  jmp 0x1409be50a
009BE886  F0 81 A3 38 03 00 00 FF EF FF FF  lock and dword ptr [rbx + 0x338], 0xffffefff
009BE891  48 39 AB 20 03 00 00            cmp qword ptr [rbx + 0x320], rbp
009BE898  0F 84 7C FC FF FF               je 0x1409be51a
009BE89E  33 D2                           xor edx, edx
009BE8A0  48 8B CB                        mov rcx, rbx
009BE8A3  E8 48 36 00 00                  call 0x1409c1ef0
009BE8A8  8B F8                           mov edi, eax
009BE8AA  85 C0                           test eax, eax
009BE8AC  0F 89 8A 01 17 00               jns 0x140b2ea3c
009BE8B2  89 06                           mov dword ptr [rsi], eax
009BE8B4  E9 61 FC FF FF                  jmp 0x1409be51a
009BE8B9  8B 43 2C                        mov eax, dword ptr [rbx + 0x2c]
009BE8BC  48 8D 8B 98 00 00 00            lea rcx, [rbx + 0x98]
009BE8C3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009BE8C7  4D 8B CC                        mov r9, r12
009BE8CA  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
009BE8CD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BE8D1  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009BE8D5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009BE8DA  E8 6D 03 11 00                  call 0x140acec4c
009BE8DF  E9 C9 FC FF FF                  jmp 0x1409be5ad
009BE8E4  48 8B 0D 55 0F 54 00            mov rcx, qword ptr [rip + 0x540f55]
009BE8EB  48 8D 15 76 54 65 FF            lea rdx, [rip - 0x9aab8a]
009BE8F2  E8 59 3B 9D FF                  call 0x140392450
009BE8F7  84 C0                           test al, al
009BE8F9  0F 84 48 FE FF FF               je 0x1409be747
009BE8FF  4C 8B C3                        mov r8, rbx
009BE902  48 8D 15 5F 54 65 FF            lea rdx, [rip - 0x9aaba1]
009BE909  E8 12 E8 FF FF                  call 0x1409bd120
009BE90E  E9 34 FE FF FF                  jmp 0x1409be747
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogger(__int64 a1)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 4506634)) ^ (v_rsp);
    v_stack_m30 = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PsAttachSiloToCurrentThread(*(unsigned __int64 *)(a1), a2, a3, a4);
    v_stack_m68 = result;
    result = KeSetActualBasePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 15, a3, a4);
    v_stack_m3C = 1;
    v_stack_m38 = 1;
    v_stack_m40 = 1;
    result = NtSetInformationThread(-2, 1 + 48, v_stack_m40, 1 + 11);
    v_r15 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 136)) > 0) goto loc_009BE7E0;
loc_009BE3B8:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8) + 456, a2, a3, 1 + 11);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 8) + 504;
    v_stack_m60 = *(unsigned __int64 *)(a1 + 8) + 480;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 320)) == 0) goto loc_009BE6C2;
loc_009BE3F8:
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    v_rdi = *(unsigned __int64 *)(a1 + 8) + 816;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 208))) != 0) { v_rdi = *(unsigned __int64 *)(a1 + 8) + 816; }
    v_stack_m88 = 0;
    a1 = ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 208))) != 0) ? 1 : 0;
    a4 = 0;
    a1 = (unsigned int)((a1) + 1);
    result = KeWaitForMultipleObjects(a1, v_stack_m60, (unsigned int)((unsigned int)(a4 + 1)), a4);
    if (((unsigned int)(result)) != ((unsigned int)(a4 + 1))) goto loc_009BE462;
    if (((unsigned int)(result)) < ((unsigned int)(a4 + 1))) {
    }
    result = KeResetEvent(*(unsigned __int64 *)(a1 + 8) + 480, v_stack_m60, (unsigned int)((unsigned int)(a4 + 1)), a4);
loc_009BE462:
    if ((*(unsigned __int8 *)(v_rip + 5508635)) >= = 3) {
    }
    result = EtwpAdjustFreeBuffers(*(unsigned __int64 *)(a1 + 8), v_stack_m60, (unsigned int)((unsigned int)(a4 + 1)), a4);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824))) & (4));
    if (condition_is_not_equal) goto loc_009BE673;
loc_009BE488:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 816)))) & (4)) == 0) goto loc_009BE55C;
    if (sign_flag) goto loc_009BE7B7;
loc_009BE4A1:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 12)) & (256)) != 0) goto loc_009BE56C;
loc_009BE4B2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 816)))) & (8)) != 0) goto loc_009BE575;
    v_rdi = 0;
loc_009BE4BF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824)))) & (64)) != 0) goto loc_009BE611;
loc_009BE4CD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824)))) & (8)) != 0) goto loc_009BE827;
loc_009BE4DF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824)))) & (3)) != 0) goto loc_009BE626;
loc_009BE4ED:
    result = EtwpFlushActiveBuffers(*(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 1)))), (unsigned int)((unsigned int)(a4 + 1)), a4);
    v_rbp = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824)))) & (1)) != 0) goto loc_009BE862;
loc_009BE50A:
    if (condition_is_below) goto loc_009BE886;
loc_009BE51A:
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 12)) & (64)) != 0) { v_rdi = 0; }
    if ((unsigned int)(v_r15) != 0) goto loc_009BE5F5;
loc_009BE52A:
    v_r15 = 0;
    if (sign_flag) goto loc_009BE592;
loc_009BE531:
loc_009BE538:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 320)) != 0) goto loc_009BE3F8;
    goto loc_009BE6C2;
loc_009BE55C:
    result = EtwpFlushActiveBuffers(*(unsigned __int64 *)(a1 + 8), 1, (unsigned int)((unsigned int)(a4 + 1)), a4);
    v_r15 = 0;
    goto loc_009BE538;
loc_009BE56C:
    goto loc_009BE4B2;
loc_009BE575:
    result = EtwpRealtimeCreateLogfile(*(unsigned __int64 *)(a1 + 8), 1, (unsigned int)((unsigned int)(a4 + 1)), a4);
    if (!sign_flag) goto loc_009BE5BC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 12)))) & (64)) != 0) goto loc_009BE5BC;
loc_009BE58F:
    v_r15 = 0;
loc_009BE592:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5509799), v_rip - 10135576, (unsigned int)((unsigned int)(a4 + 1)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_009BE8B9;
loc_009BE5AD:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = EtwpStopLoggerInstance(*(unsigned __int64 *)(a1 + 8), v_rip - 10135576, (unsigned int)((unsigned int)(a4 + 1)), a4);
    goto loc_009BE531;
loc_009BE5BC:
    result = EtwpRealtimeUpdateConsumers(*(unsigned __int64 *)(a1 + 8), v_rip - 10135576, (unsigned int)((unsigned int)(a4 + 1)), a4);
    result = EtwpRealtimeFlushSavedBuffers(*(unsigned __int64 *)(a1 + 8), v_rip - 10135576, (unsigned int)((unsigned int)(a4 + 1)), a4);
    v_rdi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 344)) <= 0) goto loc_009BE4BF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 424)) <= 0) goto loc_009BE4BF;
    a2 = 0;
    result = EtwpRequestFlushTimer(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)((unsigned int)(a4 + 1)), a4);
    goto loc_009BE4BF;
loc_009BE5F5:
    a3 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8) + 456, a2, a3, a4);
    goto loc_009BE52A;
loc_009BE611:
    result = EtwpRealtimeNotifyConsumers(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    goto loc_009BE4CD;
loc_009BE626:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 824)))) & (2)) != 0) goto loc_009BE84F;
loc_009BE637:
    a3 = 0;
    result = EtwpCreateLogFile(*(unsigned __int64 *)(a1 + 8), 1, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = (unsigned int)(result);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8) + 456, a2, a3, a4);
    if (!sign_flag) goto loc_009BE4ED;
    if (1 != 0) goto loc_009BE58F;
    goto loc_009BE4ED;
loc_009BE673:
    a1 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 208)) > 0) goto loc_009BE78D;
loc_009BE681:
    goto loc_009BE488;
loc_009BE68C:
    if (condition_is_less_or_equal) goto loc_009BE6F8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 232)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 228))))) goto loc_009BE6F8;
    a4 = 0;
    a3 = 0;
    v_stack_m88 = v_rip - 10135773;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(a1 + 8) + 40, a2, a3, a4);
loc_009BE6C2:
    result = EtwpFlushActiveBuffers(*(unsigned __int64 *)(a1 + 8), 1, a3, a4);
    if (sign_flag) goto loc_009BE6F8;
    if (((unsigned int)(result)) != 259) goto loc_009BE68C;
loc_009BE6F8:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 816));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 800)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = EtwpFinalizeHeader(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 800);
        result = ZwClose(a1, a2, a3, a4);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 800) = 0;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 360)) != 0) goto loc_009BE807;
loc_009BE72B:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = 0;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8) + 456, a2, a3, a4);
    if (sign_flag) goto loc_009BE8E4;
loc_009BE747:
    result = EtwpFreeLoggerContext(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    result = PsDetachSiloFromCurrentThread(1, a2, a3, a4);
    result = PsTerminateSystemThread(0, a2, a3, a4);
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_009BE78D:
    if (condition_is_above_or_equal) goto loc_009BE681;
    result = KeCancelTimer(*(unsigned __int64 *)(v_stack_m28 + 56) + 504, a2, a3, a4);
    goto loc_009BE681;
loc_009BE7B7:
    v_rsi = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 800)) == 0) goto loc_009BE4A1;
    result = EtwpFinalizeHeader(*(unsigned __int64 *)(v_stack_m28 + 56), 1, a3, a4);
    goto loc_009BE4A1;
loc_009BE7E0:
    v_stack_m28 = v_xmm0;
    result = NtSetInformationThread(0, 16 + 22, v_stack_m28, 16);
    goto loc_009BE3B8;
loc_009BE807:
    result = EtwpRealtimeSaveState(*(unsigned __int64 *)(v_stack_m28 + 56), 16 + 22, v_stack_m28, 16);
    result = ZwClose(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 360), 16 + 22, v_stack_m28, 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 360) = 0;
    goto loc_009BE72B;
loc_009BE827:
    result = EtwpRealtimeDisconnectAllConsumers(*(unsigned __int64 *)(v_stack_m28 + 56), 16 + 22, v_stack_m28, 16);
    a3 = 0;
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 40) = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 8) + 456, a2, a3, 16);
    goto loc_009BE4DF;
loc_009BE84F:
    v_rbp = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 800)) != 0) { v_rbp = 0; }
    goto loc_009BE637;
loc_009BE862:
    if (sign_flag) goto loc_009BE50A;
    if (1 != 0) goto loc_009BE50A;
    result = EtwpFlushActiveBuffers(*(unsigned __int64 *)(v_stack_m28 + 56), 1 + 1, a3, 16);
    goto loc_009BE50A;
loc_009BE886:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 800)) == v_rbp) goto loc_009BE51A;
    a2 = 0;
    result = EtwpFinalizeHeader(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, 16);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 40) = (unsigned int)(result);
    goto loc_009BE51A;
loc_009BE8B9:
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 44)));
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 12)));
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m28 + 56) + 152;
    result = EtwpEventWriteTemplateSessionEnd(*(unsigned __int64 *)(v_stack_m28 + 56) + 152, a2, a3, *(unsigned __int64 *)(a1 + 8) + 136);
    goto loc_009BE5AD;
loc_009BE8E4:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5508949), v_rip - 10136458, a3, *(unsigned __int64 *)(a1 + 8) + 136);
    if ((unsigned __int8)(result) == 0) goto loc_009BE747;
    result = EtwpEventWriteTemplateSession(*(unsigned __int64 *)(v_rip + 5508949), v_rip - 10136481, *(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int64 *)(a1 + 8) + 136);
    goto loc_009BE747;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogger(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_m80;
    uint8_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x44C40A)) ^ (local_rsp);
    v_stack_m30 = result;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PsAttachSiloToCurrentThread(*(uint64_t *)(arg1), a2, a3, a4);
    v_stack_m68 = result;
    result = KeSetActualBasePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 15, a3, a4);
    v_stack_m3C = 1;
    v_stack_m38 = 1;
    v_stack_m40 = 1;
    result = NtSetInformationThread(-2, 1 + 48, v_stack_m40, 1 + 11);
    local_r15 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x88)) > 0) goto loc_009BE7E0;
loc_009BE3B8:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8) + 456, a2, a3, 1 + 11);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x8) + 504;
    v_stack_m60 = *(uint64_t *)(arg1 + 0x8) + 480;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x140)) == 0) goto loc_009BE6C2;
loc_009BE3F8:
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    local_rdi = *(uint64_t *)(arg1 + 0x8) + 816;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xD0))) != 0) { local_rdi = *(uint64_t *)(arg1 + 0x8) + 816; }
    v_stack_m88 = 0;
    Arg1 = ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xD0))) != 0) ? 1 : 0;
    a4 = 0;
    Arg1 = (uint32_t)((Arg1) + 1);
    result = KeWaitForMultipleObjects(Arg1, v_stack_m60, (uint32_t)((uint32_t)(a4 + 1)), a4);
    if (((uint32_t)(result)) != ((uint32_t)(a4 + 1))) goto loc_009BE462;
    if (((uint32_t)(result)) < ((uint32_t)(a4 + 1))) {
    }
    result = KeResetEvent(*(uint64_t *)(arg1 + 0x8) + 480, v_stack_m60, (uint32_t)((uint32_t)(a4 + 1)), a4);
loc_009BE462:
    if ((*(uint8_t *)(v_rip + 0x540E1B)) >= = 3) {
    }
    result = EtwpAdjustFreeBuffers(*(uint64_t *)(arg1 + 0x8), v_stack_m60, (uint32_t)((uint32_t)(a4 + 1)), a4);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338))) & (4));
    if (condition_is_not_equal) goto loc_009BE673;
loc_009BE488:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x330)))) & (4)) == 0) goto loc_009BE55C;
    if (sign_flag) goto loc_009BE7B7;
loc_009BE4A1:
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC)) & (256)) != 0) goto loc_009BE56C;
loc_009BE4B2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x330)))) & (8)) != 0) goto loc_009BE575;
    local_rdi = 0;
loc_009BE4BF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338)))) & (64)) != 0) goto loc_009BE611;
loc_009BE4CD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338)))) & (8)) != 0) goto loc_009BE827;
loc_009BE4DF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338)))) & (3)) != 0) goto loc_009BE626;
loc_009BE4ED:
    result = EtwpFlushActiveBuffers(*(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(a4 + 1)))), (uint32_t)((uint32_t)(a4 + 1)), a4);
    local_rbp = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338)))) & (1)) != 0) goto loc_009BE862;
loc_009BE50A:
    if (condition_is_below) goto loc_009BE886;
loc_009BE51A:
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC)) & (64)) != 0) { local_rdi = 0; }
    if ((uint32_t)(local_r15) != 0) goto loc_009BE5F5;
loc_009BE52A:
    local_r15 = 0;
    if (sign_flag) goto loc_009BE592;
loc_009BE531:
loc_009BE538:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x140)) != 0) goto loc_009BE3F8;
    goto loc_009BE6C2;
loc_009BE55C:
    result = EtwpFlushActiveBuffers(*(uint64_t *)(arg1 + 0x8), 1, (uint32_t)((uint32_t)(a4 + 1)), a4);
    local_r15 = 0;
    goto loc_009BE538;
loc_009BE56C:
    goto loc_009BE4B2;
loc_009BE575:
    result = EtwpRealtimeCreateLogfile(*(uint64_t *)(arg1 + 0x8), 1, (uint32_t)((uint32_t)(a4 + 1)), a4);
    if (!sign_flag) goto loc_009BE5BC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC)))) & (64)) != 0) goto loc_009BE5BC;
loc_009BE58F:
    local_r15 = 0;
loc_009BE592:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x5412A7), v_rip - 10135576, (uint32_t)((uint32_t)(a4 + 1)), a4);
    if ((uint8_t)(result) != 0) goto loc_009BE8B9;
loc_009BE5AD:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = EtwpStopLoggerInstance(*(uint64_t *)(arg1 + 0x8), v_rip - 10135576, (uint32_t)((uint32_t)(a4 + 1)), a4);
    goto loc_009BE531;
loc_009BE5BC:
    result = EtwpRealtimeUpdateConsumers(*(uint64_t *)(arg1 + 0x8), v_rip - 10135576, (uint32_t)((uint32_t)(a4 + 1)), a4);
    result = EtwpRealtimeFlushSavedBuffers(*(uint64_t *)(arg1 + 0x8), v_rip - 10135576, (uint32_t)((uint32_t)(a4 + 1)), a4);
    local_rdi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x158)) <= 0) goto loc_009BE4BF;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1A8)) <= 0) goto loc_009BE4BF;
    a2 = 0;
    result = EtwpRequestFlushTimer(*(uint64_t *)(arg1 + 0x8), a2, (uint32_t)((uint32_t)(a4 + 1)), a4);
    goto loc_009BE4BF;
loc_009BE5F5:
    a3 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = 0;
    a2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8) + 456, a2, a3, a4);
    goto loc_009BE52A;
loc_009BE611:
    result = EtwpRealtimeNotifyConsumers(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    goto loc_009BE4CD;
loc_009BE626:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x338)))) & (2)) != 0) goto loc_009BE84F;
loc_009BE637:
    a3 = 0;
    result = EtwpCreateLogFile(*(uint64_t *)(arg1 + 0x8), 1, a3, a4);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = (uint32_t)(result);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8) + 456, a2, a3, a4);
    if (!sign_flag) goto loc_009BE4ED;
    if (1 != 0) goto loc_009BE58F;
    goto loc_009BE4ED;
loc_009BE673:
    Arg1 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xD0)) > 0) goto loc_009BE78D;
loc_009BE681:
    goto loc_009BE488;
loc_009BE68C:
    if (condition_is_less_or_equal) goto loc_009BE6F8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xE8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xE4))))) goto loc_009BE6F8;
    a4 = 0;
    a3 = 0;
    v_stack_m88 = v_rip - 10135773;
    a2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(arg1 + 0x8) + 40, a2, a3, a4);
loc_009BE6C2:
    result = EtwpFlushActiveBuffers(*(uint64_t *)(arg1 + 0x8), 1, a3, a4);
    if (sign_flag) goto loc_009BE6F8;
    if (((uint32_t)(result)) != 259) goto loc_009BE68C;
loc_009BE6F8:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x330));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x320)) != 0) {
        a2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        result = EtwpFinalizeHeader(Arg1, a2, a3, a4);
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x320);
        result = ZwClose(Arg1, a2, a3, a4);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x320) = 0;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x168)) != 0) goto loc_009BE807;
loc_009BE72B:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = 0;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8) + 456, a2, a3, a4);
    if (sign_flag) goto loc_009BE8E4;
loc_009BE747:
    result = EtwpFreeLoggerContext(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    result = PsDetachSiloFromCurrentThread(1, a2, a3, a4);
    result = PsTerminateSystemThread(0, a2, a3, a4);
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    return result;
loc_009BE78D:
    if (condition_is_above_or_equal) goto loc_009BE681;
    result = KeCancelTimer(*(uint64_t *)(v_stack_m28 + 0x38) + 504, a2, a3, a4);
    goto loc_009BE681;
loc_009BE7B7:
    local_rsi = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x320)) == 0) goto loc_009BE4A1;
    result = EtwpFinalizeHeader(*(uint64_t *)(v_stack_m28 + 0x38), 1, a3, a4);
    goto loc_009BE4A1;
loc_009BE7E0:
    v_stack_m28 = v_xmm0;
    result = NtSetInformationThread(0, 16 + 22, v_stack_m28, 16);
    goto loc_009BE3B8;
loc_009BE807:
    result = EtwpRealtimeSaveState(*(uint64_t *)(v_stack_m28 + 0x38), 16 + 22, v_stack_m28, 16);
    result = ZwClose(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x168), 16 + 22, v_stack_m28, 16);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x168) = 0;
    goto loc_009BE72B;
loc_009BE827:
    result = EtwpRealtimeDisconnectAllConsumers(*(uint64_t *)(v_stack_m28 + 0x38), 16 + 22, v_stack_m28, 16);
    a3 = 0;
    a2 = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x28) = 0;
    result = KeSetEvent(*(uint64_t *)(arg1 + 0x8) + 456, a2, a3, 16);
    goto loc_009BE4DF;
loc_009BE84F:
    local_rbp = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x320)) != 0) { local_rbp = 0; }
    goto loc_009BE637;
loc_009BE862:
    if (sign_flag) goto loc_009BE50A;
    if (1 != 0) goto loc_009BE50A;
    result = EtwpFlushActiveBuffers(*(uint64_t *)(v_stack_m28 + 0x38), 1 + 1, a3, 16);
    goto loc_009BE50A;
loc_009BE886:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x320)) == local_rbp) goto loc_009BE51A;
    a2 = 0;
    result = EtwpFinalizeHeader(*(uint64_t *)(v_stack_m28 + 0x38), a2, a3, 16);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x28) = (uint32_t)(result);
    goto loc_009BE51A;
loc_009BE8B9:
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2C)));
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xC)));
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m60 = *(uint64_t *)(v_stack_m28 + 0x38) + 152;
    result = EtwpEventWriteTemplateSessionEnd(*(uint64_t *)(v_stack_m28 + 0x38) + 152, a2, a3, *(uint64_t *)(arg1 + 0x8) + 136);
    goto loc_009BE5AD;
loc_009BE8E4:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x540F55), v_rip - 10136458, a3, *(uint64_t *)(arg1 + 0x8) + 136);
    if ((uint8_t)(result) == 0) goto loc_009BE747;
    result = EtwpEventWriteTemplateSession(*(uint64_t *)(v_rip + 0x540F55), v_rip - 10136481, *(uint64_t *)(v_stack_m28 + 0x38), *(uint64_t *)(arg1 + 0x8) + 136);
    goto loc_009BE747;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BE310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
