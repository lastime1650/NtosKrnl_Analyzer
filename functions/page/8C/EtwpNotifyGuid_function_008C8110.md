# EtwpNotifyGuid

- RVA: `0x008C8110`–`0x008C8529` (길이 `1,049` bytes)
- VA: `0x00000001408C8110`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00084024`
- 디코드: `279`개 명령, `1,049/1,049` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008C815E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008C817F` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x008C81AC` → [EtwpFindGuidEntryByGuid](EtwpFindGuidEntryByGuid_function_008C1DB0.md) (function, `0x008C1DB0`)
- `0x008C81D0` → [EtwpAccessCheck](EtwpAccessCheck_function_008C6C2C.md) (function, `0x008C6C2C`)
- `0x008C81DE` → [EtwpUnreferenceGuidEntry](EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x008C81E7` → [EtwpFreeFilterInfo](EtwpFreeFilterInfo_function_008C8A24.md) (function, `0x008C8A24`)
- `0x008C822A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008C8243` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008C8283` → [EtwpAllocDataBlock](../9F/EtwpAllocDataBlock_function_009FEE38.md) (function, `0x009FEE38`)
- `0x008C82D8` → [EtwpSendDataBlock](EtwpSendDataBlock_function_008C8530.md) (function, `0x008C8530`)
- `0x008C82F1` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x008C830E` → [EtwpApplyTransientFilters](EtwpApplyTransientFilters_function_008C8994.md) (function, `0x008C8994`)
- `0x008C836E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C8373` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008C8381` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x008C8393` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)
- `0x008C83B0` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x008C83C7` → [EtwpDemuxPrivateTraceHandle](../AC/EtwpDemuxPrivateTraceHandle_function_00ACDB1C.md) (function, `0x00ACDB1C`)
- `0x008C83ED` → [EtwpAllocDataBlock](../9F/EtwpAllocDataBlock_function_009FEE38.md) (function, `0x009FEE38`)
- `0x008C8406` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008C8479` → [EtwpCheckCurrentUserProcessAccess](../9E/EtwpCheckCurrentUserProcessAccess_function_009EB530.md) (function, `0x009EB530`)
- `0x008C84B5` → [EtwpValidateTraceControlFilterDescriptors](../7C/EtwpValidateTraceControlFilterDescriptors_function_007C321C.md) (function, `0x007C321C`)
- `0x008C84F4` → [EtwpCreateUmReplyObject](../A8/EtwpCreateUmReplyObject_function_00A8DBE4.md) (function, `0x00A8DBE4`)
- `0x008C8513` → [EtwpUnreferenceDataBlock](../8B/EtwpUnreferenceDataBlock_function_008BFC5C.md) (function, `0x008BFC5C`)

### Direct callers
- [EtwpSendSessionNotification](../9B/EtwpSendSessionNotification_function_009BFE28.md) at `0x009BFEB6`
- [NtTraceControl](../A9/NtTraceControl_function_00A9ED40.md) at `0x00A9F211`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008C815E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008C817F` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x008C822A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008C8243` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008C82F1` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x008C836E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C8373` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008C83B0` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
  - `0x008C8406` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008C838D` → [sub_00B1B0BE + 0x30](../B1/Unknown_function_00B1B0BE.md) (`tail-transfer`)
  - `0x008C8399` → [sub_00B1B0BE + 0x30](../B1/Unknown_function_00B1B0BE.md) (`tail-transfer`)
  - `0x008C84CF` → [sub_00B1B0BE](../B1/Unknown_function_00B1B0BE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C8110  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008C8115  55                              push rbp
008C8116  56                              push rsi
008C8117  57                              push rdi
008C8118  41 54                           push r12
008C811A  41 55                           push r13
008C811C  41 56                           push r14
008C811E  41 57                           push r15
008C8120  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
008C8125  48 81 EC C0 00 00 00            sub rsp, 0xc0
008C812C  45 33 E4                        xor r12d, r12d
008C812F  45 8A F0                        mov r14b, r8b
008C8132  48 8B FA                        mov rdi, rdx
008C8135  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
008C8139  4C 8B F9                        mov r15, rcx
008C813C  4C 89 65 9F                     mov qword ptr [rbp - 0x61], r12
008C8140  33 D2                           xor edx, edx
008C8142  4C 89 65 97                     mov qword ptr [rbp - 0x69], r12
008C8146  45 8D 44 24 68                  lea r8d, [r12 + 0x68]
008C814B  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
008C814F  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008C8153  44 88 65 87                     mov byte ptr [rbp - 0x79], r12b
008C8157  45 8B EC                        mov r13d, r12d
008C815A  4C 89 65 A7                     mov qword ptr [rbp - 0x59], r12
008C815E  E8 DD EA DF FF                  call 0x1406c6c40
008C8163  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
008C8167  41 81 F8 00 00 01 00            cmp r8d, 0x10000
008C816E  0F 87 ED 02 00 00               ja 0x1408c8461
008C8174  8B 1F                           mov ebx, dword ptr [rdi]
008C8176  83 FB 0B                        cmp ebx, 0xb
008C8179  0F 84 A6 02 00 00               je 0x1408c8425
008C817F  E8 DC B3 B6 FF                  call 0x140433560
008C8184  89 47 24                        mov dword ptr [rdi + 0x24], eax
008C8187  83 FB 04                        cmp ebx, 4
008C818A  0F 84 38 03 00 00               je 0x1408c84c8
008C8190  BB 04 00 00 00                  mov ebx, 4
008C8195  8D 73 FD                        lea esi, [rbx - 3]
008C8198  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
008C819B  48 8D 57 28                     lea rdx, [rdi + 0x28]
008C819F  44 8B C6                        mov r8d, esi
008C81A2  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
008C81A5  49 8B CF                        mov rcx, r15
008C81A8  44 89 67 14                     mov dword ptr [rdi + 0x14], r12d
008C81AC  E8 FF 9B FF FF                  call 0x1408c1db0
008C81B1  48 8B F0                        mov rsi, rax
008C81B4  48 85 C0                        test rax, rax
008C81B7  0F 84 22 03 00 00               je 0x1408c84df
008C81BD  45 84 F6                        test r14b, r14b
008C81C0  74 48                           je 0x1408c820a
008C81C2  83 3F 04                        cmp dword ptr [rdi], 4
008C81C5  74 43                           je 0x1408c820a
008C81C7  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
008C81CB  45 33 C0                        xor r8d, r8d
008C81CE  8B D3                           mov edx, ebx
008C81D0  E8 57 EA FF FF                  call 0x1408c6c2c
008C81D5  8B D8                           mov ebx, eax
008C81D7  85 C0                           test eax, eax
008C81D9  79 2F                           jns 0x1408c820a
008C81DB  48 8B CE                        mov rcx, rsi
008C81DE  E8 3D B1 FF FF                  call 0x1408c3320
008C81E3  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008C81E7  E8 38 08 00 00                  call 0x1408c8a24
008C81EC  8B C3                           mov eax, ebx
008C81EE  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
008C81F6  48 81 C4 C0 00 00 00            add rsp, 0xc0
008C81FD  41 5F                           pop r15
008C81FF  41 5E                           pop r14
008C8201  41 5D                           pop r13
008C8203  41 5C                           pop r12
008C8205  5F                              pop rdi
008C8206  5E                              pop rsi
008C8207  5D                              pop rbp
008C8208  C3                              ret
008C8209  CC                              int3
008C820A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C8213  48 8D 9E 98 02 00 00            lea rbx, [rsi + 0x298]
008C821A  45 33 C0                        xor r8d, r8d
008C821D  33 D2                           xor edx, edx
008C821F  48 8B CB                        mov rcx, rbx
008C8222  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008C8229  90                              nop
008C822A  E8 01 80 94 FF                  call 0x140210230
008C822F  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
008C8235  4C 8B F0                        mov r14, rax
008C8238  73 0E                           jae 0x1408c8248
008C823A  4C 8B C3                        mov r8, rbx
008C823D  48 8B D0                        mov rdx, rax
008C8240  48 8B CB                        mov rcx, rbx
008C8243  E8 48 7A 94 FF                  call 0x14020fc90
008C8248  4D 85 F6                        test r14, r14
008C824B  74 05                           je 0x1408c8252
008C824D  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
008C8252  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C825B  4C 8D 7E 38                     lea r15, [rsi + 0x38]
008C825F  48 89 86 A0 02 00 00            mov qword ptr [rsi + 0x2a0], rax
008C8266  4D 39 3F                        cmp qword ptr [r15], r15
008C8269  0F 84 FC 01 00 00               je 0x1408c846b
008C826F  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
008C8273  0F 85 70 02 00 00               jne 0x1408c84e9
008C8279  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
008C827C  4C 8D 45 97                     lea r8, [rbp - 0x69]
008C8280  48 8B D7                        mov rdx, rdi
008C8283  E8 B0 6B 13 00                  call 0x1409fee38
008C8288  44 8B F0                        mov r14d, eax
008C828B  85 C0                           test eax, eax
008C828D  0F 88 66 01 00 00               js 0x1408c83f9
008C8293  49 8B 1F                        mov rbx, qword ptr [r15]
008C8296  4C 8B 7D 8F                     mov r15, qword ptr [rbp - 0x71]
008C829A  48 8D 46 38                     lea rax, [rsi + 0x38]
008C829E  48 3B D8                        cmp rbx, rax
008C82A1  74 78                           je 0x1408c831b
008C82A3  0F B7 43 62                     movzx eax, word ptr [rbx + 0x62]
008C82A7  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
008C82AB  A8 02                           test al, 2
008C82AD  74 50                           je 0x1408c82ff
008C82AF  A8 20                           test al, 0x20
008C82B1  75 4C                           jne 0x1408c82ff
008C82B3  33 C0                           xor eax, eax
008C82B5  48 39 45 A7                     cmp qword ptr [rbp - 0x59], rax
008C82B9  75 4C                           jne 0x1408c8307
008C82BB  39 45 7F                        cmp dword ptr [rbp + 0x7f], eax
008C82BE  75 2D                           jne 0x1408c82ed
008C82C0  38 45 87                        cmp byte ptr [rbp - 0x79], al
008C82C3  0F 85 AC 01 00 00               jne 0x1408c8475
008C82C9  83 3F 04                        cmp dword ptr [rdi], 4
008C82CC  0F 84 CC 00 00 00               je 0x1408c839e
008C82D2  49 8B D4                        mov rdx, r12
008C82D5  48 8B CB                        mov rcx, rbx
008C82D8  E8 53 02 00 00                  call 0x1408c8530
008C82DD  45 33 E4                        xor r12d, r12d
008C82E0  85 C0                           test eax, eax
008C82E2  0F 88 39 02 00 00               js 0x1408c8521
008C82E8  41 FF C5                        inc r13d
008C82EB  EB 15                           jmp 0x1408c8302
008C82ED  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
008C82F1  E8 1A 56 B7 FF                  call 0x14043d910
008C82F6  3B 45 7F                        cmp eax, dword ptr [rbp + 0x7f]
008C82F9  0F 84 5B 01 00 00               je 0x1408c845a
008C82FF  45 33 E4                        xor r12d, r12d
008C8302  48 8B 1B                        mov rbx, qword ptr [rbx]
008C8305  EB 93                           jmp 0x1408c829a
008C8307  48 8D 55 B7                     lea rdx, [rbp - 0x49]
008C830B  48 8B CB                        mov rcx, rbx
008C830E  E8 81 06 00 00                  call 0x1408c8994
008C8313  84 C0                           test al, al
008C8315  74 E8                           je 0x1408c82ff
008C8317  33 C0                           xor eax, eax
008C8319  EB A0                           jmp 0x1408c82bb
008C831B  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
008C831F  45 85 ED                        test r13d, r13d
008C8322  41 8B DC                        mov ebx, r12d
008C8325  44 89 6F 14                     mov dword ptr [rdi + 0x14], r13d
008C8329  41 0F 44 DE                     cmove ebx, r14d
008C832D  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008C8331  4C 89 A6 A0 02 00 00            mov qword ptr [rsi + 0x2a0], r12
008C8338  48 8D BE 98 02 00 00            lea rdi, [rsi + 0x298]
008C833F  0F 0D 0F                        prefetchw byte ptr [rdi]
008C8342  48 8B 07                        mov rax, qword ptr [rdi]
008C8345  48 8B C8                        mov rcx, rax
008C8348  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008C834C  48 83 F9 10                     cmp rcx, 0x10
008C8350  48 8D 50 F0                     lea rdx, [rax - 0x10]
008C8354  49 0F 46 D4                     cmovbe rdx, r12
008C8358  A8 02                           test al, 2
008C835A  0F 85 A3 00 00 00               jne 0x1408c8403
008C8360  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
008C8365  0F 85 98 00 00 00               jne 0x1408c8403
008C836B  48 8B CF                        mov rcx, rdi
008C836E  E8 8D 92 A1 FF                  call 0x1402e1600
008C8373  E8 38 55 99 FF                  call 0x14025d8b0
008C8378  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
008C837C  48 85 C9                        test rcx, rcx
008C837F  74 05                           je 0x1408c8386
008C8381  E8 D6 78 FF FF                  call 0x1408bfc5c
008C8386  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
008C838A  48 85 C9                        test rcx, rcx
008C838D  0F 84 5B 2D 25 00               je 0x140b1b0ee
008C8393  E8 C4 78 FF FF                  call 0x1408bfc5c
008C8398  90                              nop
008C8399  E9 50 2D 25 00                  jmp 0x140b1b0ee
008C839E  83 7F 4C 01                     cmp dword ptr [rdi + 0x4c], 1
008C83A2  66 89 45 6F                     mov word ptr [rbp + 0x6f], ax
008C83A6  0F 84 26 FF FF FF               je 0x1408c82d2
008C83AC  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
008C83B0  E8 5B 55 B7 FF                  call 0x14043d910
008C83B5  0F B7 57 50                     movzx edx, word ptr [rdi + 0x50]
008C83B9  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
008C83BD  B9 FF 7F 00 00                  mov ecx, 0x7fff
008C83C2  66 23 D1                        and dx, cx
008C83C5  8B C8                           mov ecx, eax
008C83C7  E8 50 57 20 00                  call 0x140acdb1c
008C83CC  45 33 E4                        xor r12d, r12d
008C83CF  44 8B F0                        mov r14d, eax
008C83D2  85 C0                           test eax, eax
008C83D4  0F 88 28 FF FF FF               js 0x1408c8302
008C83DA  4D 85 FF                        test r15, r15
008C83DD  0F 85 2D 01 00 00               jne 0x1408c8510
008C83E3  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
008C83E6  4C 8D 45 8F                     lea r8, [rbp - 0x71]
008C83EA  48 8B D7                        mov rdx, rdi
008C83ED  E8 46 6A 13 00                  call 0x1409fee38
008C83F2  44 8B F0                        mov r14d, eax
008C83F5  85 C0                           test eax, eax
008C83F7  79 17                           jns 0x1408c8410
008C83F9  BB 17 00 00 C0                  mov ebx, 0xc0000017
008C83FE  E9 2E FF FF FF                  jmp 0x1408c8331
008C8403  48 8B CF                        mov rcx, rdi
008C8406  E8 C5 B4 99 FF                  call 0x1402638d0
008C840B  E9 5B FF FF FF                  jmp 0x1408c836b
008C8410  4C 8B 7D 8F                     mov r15, qword ptr [rbp - 0x71]
008C8414  0F B7 45 6F                     movzx eax, word ptr [rbp + 0x6f]
008C8418  4D 8B E7                        mov r12, r15
008C841B  66 41 89 47 50                  mov word ptr [r15 + 0x50], ax
008C8420  E9 AD FE FF FF                  jmp 0x1408c82d2
008C8425  41 83 F8 78                     cmp r8d, 0x78
008C8429  72 66                           jb 0x1408c8491
008C842B  8B 4F 48                        mov ecx, dword ptr [rdi + 0x48]
008C842E  B8 F8 FF FF FF                  mov eax, 0xfffffff8
008C8433  83 C1 07                        add ecx, 7
008C8436  48 23 C8                        and rcx, rax
008C8439  49 8D 40 B4                     lea rax, [r8 - 0x4c]
008C843D  48 3B C8                        cmp rcx, rax
008C8440  73 4F                           jae 0x1408c8491
008C8442  8B 44 39 48                     mov eax, dword ptr [rcx + rdi + 0x48]
008C8446  85 C0                           test eax, eax
008C8448  75 51                           jne 0x1408c849b
008C844A  C7 07 04 00 00 00               mov dword ptr [rdi], 4
008C8450  BB 04 00 00 00                  mov ebx, 4
008C8455  E9 25 FD FF FF                  jmp 0x1408c817f
008C845A  33 C0                           xor eax, eax
008C845C  E9 5F FE FF FF                  jmp 0x1408c82c0
008C8461  B8 06 02 00 C0                  mov eax, 0xc0000206
008C8466  E9 83 FD FF FF                  jmp 0x1408c81ee
008C846B  BB 96 02 00 C0                  mov ebx, 0xc0000296
008C8470  E9 BC FE FF FF                  jmp 0x1408c8331
008C8475  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
008C8479  E8 B2 30 12 00                  call 0x1409eb530
008C847E  44 8B F0                        mov r14d, eax
008C8481  33 C0                           xor eax, eax
008C8483  45 85 F6                        test r14d, r14d
008C8486  0F 89 3D FE FF FF               jns 0x1408c82c9
008C848C  E9 6E FE FF FF                  jmp 0x1408c82ff
008C8491  BB 05 00 00 80                  mov ebx, 0x80000005
008C8496  E9 48 FD FF FF                  jmp 0x1408c81e3
008C849B  48 8D 77 4C                     lea rsi, [rdi + 0x4c]
008C849F  48 03 F1                        add rsi, rcx
008C84A2  4C 8D 4D B7                     lea r9, [rbp - 0x49]
008C84A6  44 2B C6                        sub r8d, esi
008C84A9  48 89 75 A7                     mov qword ptr [rbp - 0x59], rsi
008C84AD  44 03 C7                        add r8d, edi
008C84B0  48 8B D6                        mov rdx, rsi
008C84B3  8B C8                           mov ecx, eax
008C84B5  E8 62 AD EF FF                  call 0x1407c321c
008C84BA  85 C0                           test eax, eax
008C84BC  74 8C                           je 0x1408c844a
008C84BE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008C84C3  E9 1B FD FF FF                  jmp 0x1408c81e3
008C84C8  81 7F 04 F8 00 00 00            cmp dword ptr [rdi + 4], 0xf8
008C84CF  0F 83 E9 2B 25 00               jae 0x140b1b0be
008C84D5  BB 23 00 00 C0                  mov ebx, 0xc0000023
008C84DA  E9 04 FD FF FF                  jmp 0x1408c81e3
008C84DF  BB 95 02 00 C0                  mov ebx, 0xc0000295
008C84E4  E9 FA FC FF FF                  jmp 0x1408c81e3
008C84E9  4C 8D 45 9F                     lea r8, [rbp - 0x61]
008C84ED  48 8B CE                        mov rcx, rsi
008C84F0  48 8D 55 AF                     lea rdx, [rbp - 0x51]
008C84F4  E8 EB 56 1C 00                  call 0x140a8dbe4
008C84F9  8B D8                           mov ebx, eax
008C84FB  85 C0                           test eax, eax
008C84FD  0F 88 2E FE FF FF               js 0x1408c8331
008C8503  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
008C8507  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008C850B  E9 69 FD FF FF                  jmp 0x1408c8279
008C8510  49 8B CF                        mov rcx, r15
008C8513  E8 44 77 FF FF                  call 0x1408bfc5c
008C8518  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
008C851C  E9 C2 FE FF FF                  jmp 0x1408c83e3
008C8521  44 8B F0                        mov r14d, eax
008C8524  E9 D9 FD FF FF                  jmp 0x1408c8302
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpNotifyGuid(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD8;
    unsigned __int16 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (192);
    v_r12 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    a2 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mB8 = 0;
    result = memset(v_stack_mA8, a2, v_r12 + 104, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))) > 0x10000ULL) goto loc_008C8461;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == 11) goto loc_008C8425;
loc_008C817F:
    result = PsGetCurrentProcessId(v_stack_mA8, a2, (unsigned int)(*(unsigned int *)(a2 + 4)), a4);
    *(unsigned int *)(a2 + 36) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == 4) goto loc_008C84C8;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    *(unsigned int *)(a2 + 20) = 0;
    result = EtwpFindGuidEntryByGuid(a1, a2 + 40, (unsigned int)((unsigned int)(4 - 3)), a4);
    if (result == 0) goto loc_008C84DF;
    if (a3 == 0) goto loc_008C820A;
    if ((*(unsigned int *)(a2)) == 4) goto loc_008C820A;
    a3 = 0;
    result = EtwpAccessCheck(*(unsigned __int64 *)(result + 72), 4, a3, a4);
    if (!sign_flag) goto loc_008C820A;
    result = EtwpUnreferenceGuidEntry(result, 4, a3, a4);
loc_008C81E3:
    result = EtwpFreeFilterInfo(v_stack_mA8, 4, a3, a4);
loc_008C81EE:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008C820A:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 664, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 664;
        a2 = result;
        a1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(result + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(result + 56)) == (result + 56)) goto loc_008C846B;
    if ((*(unsigned __int8 *)(a2 + 12)) != 0) goto loc_008C84E9;
loc_008C8279:
    result = EtwpAllocDataBlock((unsigned int)(*(unsigned int *)(a2 + 4)), a2, v_stack_mC8, a4);
    if (sign_flag) goto loc_008C83F9;
loc_008C829A:
    if ((*(unsigned __int64 *)(result + 56)) == (result + 56)) goto loc_008C831B;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(result + 56) + 98))) & (2)) == 0) goto loc_008C82FF;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(result + 56) + 98))) & (32)) != 0) goto loc_008C82FF;
    result = 0;
    if (v_stack_mB8 != 0) goto loc_008C8307;
loc_008C82BB:
    if (v_stack_p20 != 0) goto loc_008C82ED;
loc_008C82C0:
    if (v_stack_mD8 != 0) goto loc_008C8475;
loc_008C82C9:
    if ((*(unsigned int *)(a2)) == 4) goto loc_008C839E;
loc_008C82D2:
    result = EtwpSendDataBlock(*(unsigned __int64 *)(result + 56), v_stack_mC8, v_stack_mC8, a4);
    v_r12 = 0;
    if (sign_flag) goto loc_008C8521;
    v_r13 = (unsigned int)((0) + 1);
    goto loc_008C8302;
loc_008C82ED:
    result = PsGetProcessId(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56) + 80), v_stack_mC8, v_stack_mC8, a4);
    if (((unsigned int)(result)) == v_stack_p20) goto loc_008C845A;
loc_008C82FF:
    v_r12 = 0;
loc_008C8302:
    goto loc_008C829A;
loc_008C8307:
    result = EtwpApplyTransientFilters(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)), v_stack_mA8, v_stack_mC8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008C82FF;
    result = 0;
    goto loc_008C82BB;
loc_008C831B:
    *(unsigned int *)(a2 + 20) = (unsigned int)(v_r13);
    v_rbx = 0;
    if ((unsigned int)(v_r13) == 0) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(result))); }
    *(unsigned __int64 *)(a2 + 24) = v_stack_mB0;
loc_008C8331:
    *(unsigned __int64 *)(result + 672) = 0;
    a1 = (*(unsigned __int64 *)(result + 664)) & (-16);
    a2 = *(unsigned __int64 *)(result + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_008C8403;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_008C8403;
loc_008C836B:
    result = KeAbPostRelease(result + 664, a2, v_stack_mC8, a4);
    result = KeLeaveCriticalRegion(result + 664, a2, v_stack_mC8, a4);
    if (v_stack_mC8 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_mC8, a2, v_stack_mC8, a4);
    }
    result = EtwpUnreferenceDataBlock(v_stack_mD0, a2, v_stack_mC8, a4);
loc_008C839E:
    v_stack_p10 = (unsigned __int16)(result);
    if ((*(unsigned int *)(result + 664 + 76)) == 1) goto loc_008C82D2;
    result = PsGetProcessId(*(unsigned __int64 *)(v_rbx + 80), a2, v_stack_mC8, a4);
    a2 = (unsigned __int16)((*(unsigned __int16 *)(result + 664 + 80)) & ((unsigned __int16)((unsigned int)(0x7FFFULL))));
    result = EtwpDemuxPrivateTraceHandle((unsigned int)((unsigned int)(result)), a2, v_stack_p10, a4);
    v_r12 = 0;
    if (sign_flag) goto loc_008C8302;
    if (v_stack_mD0 != 0) goto loc_008C8510;
loc_008C83E3:
    result = EtwpAllocDataBlock((unsigned int)(*(unsigned int *)(result + 664 + 4)), result + 664, v_stack_mD0, a4);
    if (!sign_flag) goto loc_008C8410;
loc_008C83F9:
    goto loc_008C8331;
loc_008C8403:
    result = ExfReleasePushLock(result + 664, result + 664, v_stack_mD0, a4);
    goto loc_008C836B;
loc_008C8410:
    *(unsigned __int16 *)(v_stack_mD0 + 80) = (unsigned __int16)(v_stack_p10);
    goto loc_008C82D2;
loc_008C8425:
    if (((unsigned int)(v_stack_mD0)) < 120) goto loc_008C8491;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 664 + 72))) + (7));
    a1 = (a1) & ((unsigned int)(0xFFFFFFF8ULL));
    if (a1 >= (v_stack_mD0 - 76)) goto loc_008C8491;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + result + 664 * 1 + 72))) != 0) goto loc_008C849B;
loc_008C844A:
    *(unsigned int *)(result + 664) = 4;
    goto loc_008C817F;
loc_008C845A:
    result = 0;
    goto loc_008C82C0;
loc_008C8461:
    goto loc_008C81EE;
loc_008C846B:
    goto loc_008C8331;
loc_008C8475:
    result = EtwpCheckCurrentUserProcessAccess(*(unsigned __int64 *)((unsigned int)(0xC0000296ULL) + 80), result + 664, v_stack_mD0, a4);
    result = 0;
    if (!sign_flag) goto loc_008C82C9;
    goto loc_008C82FF;
loc_008C8491:
    goto loc_008C81E3;
loc_008C849B:
    v_rsi = (result + 664 + 76) + (*(unsigned __int64 *)((unsigned int)(0xC0000296ULL) + 80));
    a3 = (unsigned int)((v_stack_mD0) - ((unsigned int)(v_rsi)));
    v_stack_mB8 = v_rsi;
    a3 = (unsigned int)((a3) + ((unsigned int)(result + 664)));
    result = EtwpValidateTraceControlFilterDescriptors(0, v_rsi, a3, v_stack_mA8);
    if ((unsigned int)(result) == 0) goto loc_008C844A;
    goto loc_008C81E3;
loc_008C84C8:
    goto loc_008C81E3;
loc_008C84DF:
    goto loc_008C81E3;
loc_008C84E9:
    result = EtwpCreateUmReplyObject(v_rsi, v_stack_mB0, v_stack_mC0, v_stack_mA8);
    if (sign_flag) goto loc_008C8331;
    *(unsigned __int64 *)(result + 664 + 24) = v_stack_mC0;
    goto loc_008C8279;
loc_008C8510:
    result = EtwpUnreferenceDataBlock(v_stack_mD0, v_stack_mB0, v_stack_mC0, v_stack_mA8);
    v_stack_mD0 = v_stack_mD0;
    goto loc_008C83E3;
loc_008C8521:
    goto loc_008C8302;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpNotifyGuid(int64_t Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5F;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD8;
    uint16_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (192);
    local_r12 = 0;
    v_stack_mB0 = 0;
    v_stack_mC0 = 0;
    Arg2 = 0;
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mB8 = 0;
    result = memset(v_stack_mA8, Arg2, local_r12 + 104, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) > 0x10000ULL) goto loc_008C8461;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) == 11) goto loc_008C8425;
loc_008C817F:
    result = PsGetCurrentProcessId(v_stack_mA8, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x4)), a4);
    *(uint32_t *)(arg2 + 0x24) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))) == 4) goto loc_008C84C8;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    *(uint32_t *)(arg2 + 0x14) = 0;
    result = EtwpFindGuidEntryByGuid(Arg1, Arg2 + 40, (uint32_t)((uint32_t)(4 - 3)), a4);
    if (result == 0) goto loc_008C84DF;
    if (Arg3 == 0) goto loc_008C820A;
    if ((*(uint32_t *)(arg2)) == 4) goto loc_008C820A;
    Arg3 = 0;
    result = EtwpAccessCheck(*(uint64_t *)(result + 0x48), 4, Arg3, a4);
    if (!sign_flag) goto loc_008C820A;
    result = EtwpUnreferenceGuidEntry(result, 4, Arg3, a4);
loc_008C81E3:
    result = EtwpFreeFilterInfo(v_stack_mA8, 4, Arg3, a4);
loc_008C81EE:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008C820A:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 664, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 664;
        Arg2 = result;
        Arg1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(result + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(result + 0x38)) == (result + 56)) goto loc_008C846B;
    if ((*(uint8_t *)(arg2 + 0xC)) != 0) goto loc_008C84E9;
loc_008C8279:
    result = EtwpAllocDataBlock((uint32_t)(*(uint32_t *)(arg2 + 0x4)), Arg2, v_stack_mC8, a4);
    if (sign_flag) goto loc_008C83F9;
loc_008C829A:
    if ((*(uint64_t *)(result + 0x38)) == (result + 56)) goto loc_008C831B;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(result + 0x38) + 0x62))) & (2)) == 0) goto loc_008C82FF;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(result + 0x38) + 0x62))) & (32)) != 0) goto loc_008C82FF;
    result = 0;
    if (v_stack_mB8 != 0) goto loc_008C8307;
loc_008C82BB:
    if (v_stack_p20 != 0) goto loc_008C82ED;
loc_008C82C0:
    if (v_stack_mD8 != 0) goto loc_008C8475;
loc_008C82C9:
    if ((*(uint32_t *)(arg2)) == 4) goto loc_008C839E;
loc_008C82D2:
    result = EtwpSendDataBlock(*(uint64_t *)(result + 0x38), v_stack_mC8, v_stack_mC8, a4);
    local_r12 = 0;
    if (sign_flag) goto loc_008C8521;
    local_r13 = (uint32_t)((0) + 1);
    goto loc_008C8302;
loc_008C82ED:
    result = PsGetProcessId(*(uint64_t *)(*(uint64_t *)(result + 0x38) + 0x50), v_stack_mC8, v_stack_mC8, a4);
    if (((uint32_t)(result)) == v_stack_p20) goto loc_008C845A;
loc_008C82FF:
    local_r12 = 0;
loc_008C8302:
    goto loc_008C829A;
loc_008C8307:
    result = EtwpApplyTransientFilters(*(uint64_t *)(*(uint64_t *)(result + 0x38)), v_stack_mA8, v_stack_mC8, a4);
    if ((uint8_t)(result) == 0) goto loc_008C82FF;
    result = 0;
    goto loc_008C82BB;
loc_008C831B:
    *(uint32_t *)(arg2 + 0x14) = (uint32_t)(local_r13);
    local_rbx = 0;
    if ((uint32_t)(local_r13) == 0) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(result))); }
    *(uint64_t *)(arg2 + 0x18) = v_stack_mB0;
loc_008C8331:
    *(uint64_t *)(result + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)(result + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_008C8403;
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_008C8403;
loc_008C836B:
    result = KeAbPostRelease(result + 664, Arg2, v_stack_mC8, a4);
    result = KeLeaveCriticalRegion(result + 664, Arg2, v_stack_mC8, a4);
    if (v_stack_mC8 != 0) {
        result = EtwpUnreferenceDataBlock(v_stack_mC8, Arg2, v_stack_mC8, a4);
    }
    result = EtwpUnreferenceDataBlock(v_stack_mD0, Arg2, v_stack_mC8, a4);
loc_008C839E:
    v_stack_p10 = (uint16_t)(result);
    if ((*(uint32_t *)(result + 0x298 + 0x4C)) == 1) goto loc_008C82D2;
    result = PsGetProcessId(*(uint64_t *)(local_rbx + 0x50), Arg2, v_stack_mC8, a4);
    Arg2 = (uint16_t)((*(uint16_t *)(result + 0x298 + 0x50)) & ((uint16_t)((uint32_t)(0x7FFFULL))));
    result = EtwpDemuxPrivateTraceHandle((uint32_t)((uint32_t)(result)), Arg2, v_stack_p10, a4);
    local_r12 = 0;
    if (sign_flag) goto loc_008C8302;
    if (v_stack_mD0 != 0) goto loc_008C8510;
loc_008C83E3:
    result = EtwpAllocDataBlock((uint32_t)(*(uint32_t *)(result + 0x298 + 0x4)), result + 664, v_stack_mD0, a4);
    if (!sign_flag) goto loc_008C8410;
loc_008C83F9:
    goto loc_008C8331;
loc_008C8403:
    result = ExfReleasePushLock(result + 664, result + 664, v_stack_mD0, a4);
    goto loc_008C836B;
loc_008C8410:
    *(uint16_t *)(v_stack_mD0 + 0x50) = (uint16_t)(v_stack_p10);
    goto loc_008C82D2;
loc_008C8425:
    if (((uint32_t)(v_stack_mD0)) < 120) goto loc_008C8491;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x298 + 0x48))) + (7));
    Arg1 = (Arg1) & ((uint32_t)(0xFFFFFFF8ULL));
    if (Arg1 >= (v_stack_mD0 - 76)) goto loc_008C8491;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + result + 0x298 * 1 + 0x48))) != 0) goto loc_008C849B;
loc_008C844A:
    *(uint32_t *)(result + 0x298) = 4;
    goto loc_008C817F;
loc_008C845A:
    result = 0;
    goto loc_008C82C0;
loc_008C8461:
    goto loc_008C81EE;
loc_008C846B:
    goto loc_008C8331;
loc_008C8475:
    result = EtwpCheckCurrentUserProcessAccess(*(uint64_t *)((uint32_t)(0xC0000296ULL) + 0x50), result + 664, v_stack_mD0, a4);
    result = 0;
    if (!sign_flag) goto loc_008C82C9;
    goto loc_008C82FF;
loc_008C8491:
    goto loc_008C81E3;
loc_008C849B:
    local_rsi = (result + 664 + 76) + (*(uint64_t *)((uint32_t)(0xC0000296ULL) + 0x50));
    Arg3 = (uint32_t)((v_stack_mD0) - ((uint32_t)(local_rsi)));
    v_stack_mB8 = local_rsi;
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result + 664)));
    result = EtwpValidateTraceControlFilterDescriptors(0, local_rsi, Arg3, v_stack_mA8);
    if ((uint32_t)(result) == 0) goto loc_008C844A;
    goto loc_008C81E3;
loc_008C84C8:
    goto loc_008C81E3;
loc_008C84DF:
    goto loc_008C81E3;
loc_008C84E9:
    result = EtwpCreateUmReplyObject(local_rsi, v_stack_mB0, v_stack_mC0, v_stack_mA8);
    if (sign_flag) goto loc_008C8331;
    *(uint64_t *)(result + 0x298 + 0x18) = v_stack_mC0;
    goto loc_008C8279;
loc_008C8510:
    result = EtwpUnreferenceDataBlock(v_stack_mD0, v_stack_mB0, v_stack_mC0, v_stack_mA8);
    v_stack_mD0 = v_stack_mD0;
    goto loc_008C83E3;
loc_008C8521:
    goto loc_008C8302;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0xC` | `8` | `R` |
| `Arg2` | `+ 0x14` | `32` | `W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x4C` | `32` | `R` |
| `Arg2` | `+ 0x4C` | `64` | `R` |
| `Arg2` | `+ 0x50` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C8110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
