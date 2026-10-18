# WmiQueryTraceInformation

- RVA: `0x007B9370`–`0x007B9BBE` (길이 `2,126` bytes)
- VA: `0x00000001407B9370`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D3A3C`
- 디코드: `516`개 명령, `2,126/2,126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x007B93A0` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x007B944D` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x007B947D` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x007B94F2` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x007B9509` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x007B970D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007B9752` → [EtwQueryTraceHandleByLoggerName](../AA/EtwQueryTraceHandleByLoggerName_function_00AA2578.md) (function, `0x00AA2578`)
- `0x007B9994` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x007B99D6` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x007B9A1F` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x007B9ACC` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x007B9B1B` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x007B9B2A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007B9B61` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x007B9B76` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)

### Direct callers
- [WdipSemWriteSemActionsEvent](../AB/WdipSemWriteSemActionsEvent_function_00ABC618.md) at `0x00ABC6B4`

### Static image references
- `0x007B97D8` → RVA `0x00EFF284` (`.data`; read)
- `0x007B9809` → RVA `0x00E0EB38` (`.data`; read)
- `0x007B9854` → RVA `0x00E036A8` (`.data`; read)
- `0x007B98A4` → RVA `0x00B4EBD0` (`EtwpAllNotifyRoutines`; read)
- `0x007B98AE` → RVA `0x00B4EBE0` (`PAGE`; read)
- `0x007B98B9` → RVA `0x00B4EBF0` (`PAGE`; read)
- `0x007B98C4` → RVA `0x00B4EC00` (`PAGE`; read)
- `0x007B98CF` → RVA `0x00B4EC10` (`PAGE`; read)
- `0x007B98DA` → RVA `0x00B4EC20` (`PAGE`; read)
- `0x007B98E5` → RVA `0x00B4EC30` (`PAGE`; read)
- `0x007B98F0` → RVA `0x00B4EC40` (`PAGE`; read)
- `0x007B993E` → RVA `0x00E684A8` (`.data`; read)
- `0x007B99A5` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x007B99CA` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007B93A0` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x007B99D6` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x007B9B2A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B9370  48 8B C4                        mov rax, rsp
007B9373  48 89 58 08                     mov qword ptr [rax + 8], rbx
007B9377  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007B937B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007B937F  4C 89 60 20                     mov qword ptr [rax + 0x20], r12
007B9383  41 55                           push r13
007B9385  41 56                           push r14
007B9387  41 57                           push r15
007B9389  48 83 EC 40                     sub rsp, 0x40
007B938D  49 8B F9                        mov rdi, r9
007B9390  45 8B F8                        mov r15d, r8d
007B9393  48 8B DA                        mov rbx, rdx
007B9396  44 8B D1                        mov r10d, ecx
007B9399  45 33 ED                        xor r13d, r13d
007B939C  44 89 68 C8                     mov dword ptr [rax - 0x38], r13d
007B93A0  E8 4B 4E B4 FF                  call 0x1402fe1f0
007B93A5  4C 8B A0 40 03 00 00            mov r12, qword ptr [rax + 0x340]
007B93AC  4D 85 C9                        test r9, r9
007B93AF  74 03                           je 0x1407b93b4
007B93B1  45 89 29                        mov dword ptr [r9], r13d
007B93B4  41 83 FA 07                     cmp r10d, 7
007B93B8  0F 8F C0 03 00 00               jg 0x1407b977e
007B93BE  0F 84 17 03 00 00               je 0x1407b96db
007B93C4  45 85 D2                        test r10d, r10d
007B93C7  0F 84 8E 02 00 00               je 0x1407b965b
007B93CD  41 83 EA 01                     sub r10d, 1
007B93D1  0F 84 0B 02 00 00               je 0x1407b95e2
007B93D7  41 83 EA 01                     sub r10d, 1
007B93DB  0F 84 AF 01 00 00               je 0x1407b9590
007B93E1  41 83 EA 01                     sub r10d, 1
007B93E5  0F 84 45 01 00 00               je 0x1407b9530
007B93EB  41 83 EA 01                     sub r10d, 1
007B93EF  0F 84 DF 00 00 00               je 0x1407b94d4
007B93F5  41 83 EA 01                     sub r10d, 1
007B93F9  0F 84 C8 00 00 00               je 0x1407b94c7
007B93FF  41 83 FA 01                     cmp r10d, 1
007B9403  0F 85 B7 03 00 00               jne 0x1407b97c0
007B9409  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
007B940E  41 8D 72 07                     lea esi, [r10 + 7]
007B9412  44 3B FE                        cmp r15d, esi
007B9415  0F 82 A2 00 00 00               jb 0x1407b94bd
007B941B  48 85 DB                        test rbx, rbx
007B941E  0F 84 99 00 00 00               je 0x1407b94bd
007B9424  41 8B F5                        mov esi, r13d
007B9427  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
007B942C  45 8B F2                        mov r14d, r10d
007B942F  45 8B EE                        mov r13d, r14d
007B9432  41 8B C6                        mov eax, r14d
007B9435  44 89 B4 24 80 00 00 00         mov dword ptr [rsp + 0x80], r14d
007B943D  41 3B 44 24 10                  cmp eax, dword ptr [r12 + 0x10]
007B9442  73 4E                           jae 0x1407b9492
007B9444  45 33 C0                        xor r8d, r8d
007B9447  41 8B D6                        mov edx, r14d
007B944A  49 8B CC                        mov rcx, r12
007B944D  E8 CE 94 17 00                  call 0x140932920
007B9452  4C 8B C0                        mov r8, rax
007B9455  48 85 C0                        test rax, rax
007B9458  74 33                           je 0x1407b948d
007B945A  8D 46 01                        lea eax, [rsi + 1]
007B945D  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
007B9464  8B D0                           mov edx, eax
007B9466  48 C1 E2 03                     shl rdx, 3
007B946A  49 3B D7                        cmp rdx, r15
007B946D  77 09                           ja 0x1407b9478
007B946F  41 8B D6                        mov edx, r14d
007B9472  8B CE                           mov ecx, esi
007B9474  48 89 14 CB                     mov qword ptr [rbx + rcx*8], rdx
007B9478  33 D2                           xor edx, edx
007B947A  49 8B C8                        mov rcx, r8
007B947D  E8 DE AC 24 00                  call 0x140a04160
007B9482  8B B4 24 80 00 00 00            mov esi, dword ptr [rsp + 0x80]
007B9489  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
007B948D  41 FF C6                        inc r14d
007B9490  EB 9D                           jmp 0x1407b942f
007B9492  8B D6                           mov edx, esi
007B9494  48 C1 E2 03                     shl rdx, 3
007B9498  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
007B949C  41 B8 05 01 00 00               mov r8d, 0x105
007B94A2  49 3B D7                        cmp rdx, r15
007B94A5  41 0F 47 C8                     cmova ecx, r8d
007B94A9  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
007B94AD  48 85 FF                        test rdi, rdi
007B94B0  0F 84 D7 06 00 00               je 0x1407b9b8d
007B94B6  89 17                           mov dword ptr [rdi], edx
007B94B8  E9 D0 06 00 00                  jmp 0x1407b9b8d
007B94BD  B8 04 00 00 C0                  mov eax, 0xc0000004
007B94C2  E9 D7 06 00 00                  jmp 0x1407b9b9e
007B94C7  C7 44 24 20 03 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000003
007B94CF  E9 B9 06 00 00                  jmp 0x1407b9b8d
007B94D4  BE 08 00 00 00                  mov esi, 8
007B94D9  44 3B FE                        cmp r15d, esi
007B94DC  74 0A                           je 0x1407b94e8
007B94DE  B8 04 00 00 C0                  mov eax, 0xc0000004
007B94E3  E9 B6 06 00 00                  jmp 0x1407b9b9e
007B94E8  45 33 C0                        xor r8d, r8d
007B94EB  41 8D 50 01                     lea edx, [r8 + 1]
007B94EF  49 8B CC                        mov rcx, r12
007B94F2  E8 29 94 17 00                  call 0x140932920
007B94F7  48 85 C0                        test rax, rax
007B94FA  74 2A                           je 0x1407b9526
007B94FC  44 8B 30                        mov r14d, dword ptr [rax]
007B94FF  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
007B9504  33 D2                           xor edx, edx
007B9506  48 8B C8                        mov rcx, rax
007B9509  E8 52 AC 24 00                  call 0x140a04160
007B950E  48 85 DB                        test rbx, rbx
007B9511  74 03                           je 0x1407b9516
007B9513  4C 89 33                        mov qword ptr [rbx], r14
007B9516  48 85 FF                        test rdi, rdi
007B9519  0F 84 6E 06 00 00               je 0x1407b9b8d
007B951F  89 37                           mov dword ptr [rdi], esi
007B9521  E9 67 06 00 00                  jmp 0x1407b9b8d
007B9526  B8 25 02 00 C0                  mov eax, 0xc0000225
007B952B  E9 6E 06 00 00                  jmp 0x1407b9b9e
007B9530  41 83 FF 04                     cmp r15d, 4
007B9534  73 0A                           jae 0x1407b9540
007B9536  B8 04 00 00 C0                  mov eax, 0xc0000004
007B953B  E9 5E 06 00 00                  jmp 0x1407b9b9e
007B9540  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B9548  48 85 C0                        test rax, rax
007B954B  75 0A                           jne 0x1407b9557
007B954D  B8 30 00 00 C0                  mov eax, 0xc0000030
007B9552  E9 47 06 00 00                  jmp 0x1407b9b9e
007B9557  48 8B 40 08                     mov rax, qword ptr [rax + 8]
007B955B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B9560  48 85 C0                        test rax, rax
007B9563  74 21                           je 0x1407b9586
007B9565  B9 FF FF FF FF                  mov ecx, 0xffffffff
007B956A  48 3B C1                        cmp rax, rcx
007B956D  74 17                           je 0x1407b9586
007B956F  48 C1 E8 10                     shr rax, 0x10
007B9573  0F B6 C8                        movzx ecx, al
007B9576  48 85 DB                        test rbx, rbx
007B9579  0F 84 3D 01 00 00               je 0x1407b96bc
007B957F  89 0A                           mov dword ptr [rdx], ecx
007B9581  E9 36 01 00 00                  jmp 0x1407b96bc
007B9586  B8 08 00 00 C0                  mov eax, 0xc0000008
007B958B  E9 0E 06 00 00                  jmp 0x1407b9b9e
007B9590  41 83 FF 04                     cmp r15d, 4
007B9594  73 0A                           jae 0x1407b95a0
007B9596  B8 04 00 00 C0                  mov eax, 0xc0000004
007B959B  E9 FE 05 00 00                  jmp 0x1407b9b9e
007B95A0  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B95A8  48 85 C0                        test rax, rax
007B95AB  75 0A                           jne 0x1407b95b7
007B95AD  B8 30 00 00 C0                  mov eax, 0xc0000030
007B95B2  E9 E7 05 00 00                  jmp 0x1407b9b9e
007B95B7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
007B95BB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B95C0  48 85 C0                        test rax, rax
007B95C3  74 13                           je 0x1407b95d8
007B95C5  B9 FF FF FF FF                  mov ecx, 0xffffffff
007B95CA  48 3B C1                        cmp rax, rcx
007B95CD  74 09                           je 0x1407b95d8
007B95CF  48 C1 E8 20                     shr rax, 0x20
007B95D3  E9 DD 00 00 00                  jmp 0x1407b96b5
007B95D8  B8 08 00 00 C0                  mov eax, 0xc0000008
007B95DD  E9 BC 05 00 00                  jmp 0x1407b9b9e
007B95E2  BE 08 00 00 00                  mov esi, 8
007B95E7  44 3B FE                        cmp r15d, esi
007B95EA  74 0A                           je 0x1407b95f6
007B95EC  B8 04 00 00 C0                  mov eax, 0xc0000004
007B95F1  E9 A8 05 00 00                  jmp 0x1407b9b9e
007B95F6  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B95FE  48 85 C0                        test rax, rax
007B9601  75 0A                           jne 0x1407b960d
007B9603  B8 30 00 00 C0                  mov eax, 0xc0000030
007B9608  E9 91 05 00 00                  jmp 0x1407b9b9e
007B960D  8B 00                           mov eax, dword ptr [rax]
007B960F  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
007B9616  41 3B 44 24 10                  cmp eax, dword ptr [r12 + 0x10]
007B961B  72 0A                           jb 0x1407b9627
007B961D  B8 08 00 00 C0                  mov eax, 0xc0000008
007B9622  E9 77 05 00 00                  jmp 0x1407b9b9e
007B9627  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
007B962C  85 C0                           test eax, eax
007B962E  0F B7 C8                        movzx ecx, ax
007B9631  75 05                           jne 0x1407b9638
007B9633  B9 FF FF 00 00                  mov ecx, 0xffff
007B9638  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
007B963D  48 85 DB                        test rbx, rbx
007B9640  74 08                           je 0x1407b964a
007B9642  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
007B9647  48 89 02                        mov qword ptr [rdx], rax
007B964A  48 85 FF                        test rdi, rdi
007B964D  0F 84 3A 05 00 00               je 0x1407b9b8d
007B9653  41 89 31                        mov dword ptr [r9], esi
007B9656  E9 32 05 00 00                  jmp 0x1407b9b8d
007B965B  41 83 FF 04                     cmp r15d, 4
007B965F  74 0A                           je 0x1407b966b
007B9661  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9666  E9 33 05 00 00                  jmp 0x1407b9b9e
007B966B  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B9673  48 85 C0                        test rax, rax
007B9676  75 0A                           jne 0x1407b9682
007B9678  B8 30 00 00 C0                  mov eax, 0xc0000030
007B967D  E9 1C 05 00 00                  jmp 0x1407b9b9e
007B9682  48 8B 40 08                     mov rax, qword ptr [rax + 8]
007B9686  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B968B  48 85 C0                        test rax, rax
007B968E  74 41                           je 0x1407b96d1
007B9690  B9 FF FF FF FF                  mov ecx, 0xffffffff
007B9695  48 3B C1                        cmp rax, rcx
007B9698  74 37                           je 0x1407b96d1
007B969A  0F B7 C0                        movzx eax, ax
007B969D  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
007B96A4  41 3B 44 24 10                  cmp eax, dword ptr [r12 + 0x10]
007B96A9  72 0A                           jb 0x1407b96b5
007B96AB  B8 08 00 00 C0                  mov eax, 0xc0000008
007B96B0  E9 E9 04 00 00                  jmp 0x1407b9b9e
007B96B5  48 85 DB                        test rbx, rbx
007B96B8  74 02                           je 0x1407b96bc
007B96BA  89 02                           mov dword ptr [rdx], eax
007B96BC  48 85 FF                        test rdi, rdi
007B96BF  0F 84 C8 04 00 00               je 0x1407b9b8d
007B96C5  41 C7 01 04 00 00 00            mov dword ptr [r9], 4
007B96CC  E9 BC 04 00 00                  jmp 0x1407b9b8d
007B96D1  B8 08 00 00 C0                  mov eax, 0xc0000008
007B96D6  E9 C3 04 00 00                  jmp 0x1407b9b9e
007B96DB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007B96E4  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
007B96EA  84 C0                           test al, al
007B96EC  74 3E                           je 0x1407b972c
007B96EE  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007B96F6  0F B7 01                        movzx eax, word ptr [rcx]
007B96F9  66 85 C0                        test ax, ax
007B96FC  74 2E                           je 0x1407b972c
007B96FE  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
007B9702  41 BE 01 00 00 00               mov r14d, 1
007B9708  41 84 CE                        test r14b, cl
007B970B  74 05                           je 0x1407b9712
007B970D  E8 BE 08 0E 00                  call 0x140899fd0
007B9712  48 8D 14 01                     lea rdx, [rcx + rax]
007B9716  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
007B9720  48 3B D0                        cmp rdx, rax
007B9723  77 05                           ja 0x1407b972a
007B9725  48 3B D1                        cmp rdx, rcx
007B9728  73 02                           jae 0x1407b972c
007B972A  8A 00                           mov al, byte ptr [rax]
007B972C  BE 08 00 00 00                  mov esi, 8
007B9731  44 3B FE                        cmp r15d, esi
007B9734  74 0A                           je 0x1407b9740
007B9736  B8 04 00 00 C0                  mov eax, 0xc0000004
007B973B  E9 5E 04 00 00                  jmp 0x1407b9b9e
007B9740  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
007B9745  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007B974A  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007B9752  E8 21 8E 2E 00                  call 0x140aa2578
007B9757  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007B975B  85 C0                           test eax, eax
007B975D  0F 88 3B 04 00 00               js 0x1407b9b9e
007B9763  48 85 DB                        test rbx, rbx
007B9766  0F 84 AA FD FF FF               je 0x1407b9516
007B976C  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
007B9771  48 89 03                        mov qword ptr [rbx], rax
007B9774  E9 9D FD FF FF                  jmp 0x1407b9516
007B9779  E9 20 04 00 00                  jmp 0x1407b9b9e
007B977E  BE 08 00 00 00                  mov esi, 8
007B9783  44 2B D6                        sub r10d, esi
007B9786  0F 84 A5 03 00 00               je 0x1407b9b31
007B978C  41 83 EA 01                     sub r10d, 1
007B9790  0F 84 A9 02 00 00               je 0x1407b9a3f
007B9796  41 83 EA 01                     sub r10d, 1
007B979A  0F 84 B2 01 00 00               je 0x1407b9952
007B97A0  41 83 EA 01                     sub r10d, 1
007B97A4  0F 84 55 01 00 00               je 0x1407b98ff
007B97AA  41 83 EA 01                     sub r10d, 1
007B97AE  0F 84 AC 00 00 00               je 0x1407b9860
007B97B4  41 83 EA 01                     sub r10d, 1
007B97B8  74 5B                           je 0x1407b9815
007B97BA  41 83 FA 02                     cmp r10d, 2
007B97BE  74 0A                           je 0x1407b97ca
007B97C0  B8 03 00 00 C0                  mov eax, 0xc0000003
007B97C5  E9 D4 03 00 00                  jmp 0x1407b9b9e
007B97CA  48 85 FF                        test rdi, rdi
007B97CD  74 03                           je 0x1407b97d2
007B97CF  41 89 31                        mov dword ptr [r9], esi
007B97D2  41 BE 01 00 00 00               mov r14d, 1
007B97D8  44 38 35 A5 5A 74 00            cmp byte ptr [rip + 0x745aa5], r14b
007B97DF  77 0A                           ja 0x1407b97eb
007B97E1  B8 A3 00 00 C0                  mov eax, 0xc00000a3
007B97E6  E9 B3 03 00 00                  jmp 0x1407b9b9e
007B97EB  44 3B FE                        cmp r15d, esi
007B97EE  74 0A                           je 0x1407b97fa
007B97F0  B8 04 00 00 C0                  mov eax, 0xc0000004
007B97F5  E9 A4 03 00 00                  jmp 0x1407b9b9e
007B97FA  48 85 DB                        test rbx, rbx
007B97FD  75 0A                           jne 0x1407b9809
007B97FF  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007B9804  E9 95 03 00 00                  jmp 0x1407b9b9e
007B9809  48 8D 05 28 53 65 00            lea rax, [rip + 0x655328]
007B9810  E9 30 01 00 00                  jmp 0x1407b9945
007B9815  48 85 FF                        test rdi, rdi
007B9818  74 03                           je 0x1407b981d
007B981A  41 89 31                        mov dword ptr [r9], esi
007B981D  41 BE 01 00 00 00               mov r14d, 1
007B9823  44 38 35 5A 5A 74 00            cmp byte ptr [rip + 0x745a5a], r14b
007B982A  77 0A                           ja 0x1407b9836
007B982C  B8 A3 00 00 C0                  mov eax, 0xc00000a3
007B9831  E9 68 03 00 00                  jmp 0x1407b9b9e
007B9836  44 3B FE                        cmp r15d, esi
007B9839  74 0A                           je 0x1407b9845
007B983B  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9840  E9 59 03 00 00                  jmp 0x1407b9b9e
007B9845  48 85 DB                        test rbx, rbx
007B9848  75 0A                           jne 0x1407b9854
007B984A  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007B984F  E9 4A 03 00 00                  jmp 0x1407b9b9e
007B9854  48 8D 05 4D 9E 64 00            lea rax, [rip + 0x649e4d]
007B985B  E9 E5 00 00 00                  jmp 0x1407b9945
007B9860  48 85 FF                        test rdi, rdi
007B9863  74 07                           je 0x1407b986c
007B9865  41 C7 01 78 00 00 00            mov dword ptr [r9], 0x78
007B986C  41 BE 01 00 00 00               mov r14d, 1
007B9872  44 38 35 0B 5A 74 00            cmp byte ptr [rip + 0x745a0b], r14b
007B9879  77 0A                           ja 0x1407b9885
007B987B  B8 A3 00 00 C0                  mov eax, 0xc00000a3
007B9880  E9 19 03 00 00                  jmp 0x1407b9b9e
007B9885  41 83 FF 78                     cmp r15d, 0x78
007B9889  74 0A                           je 0x1407b9895
007B988B  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9890  E9 09 03 00 00                  jmp 0x1407b9b9e
007B9895  48 85 DB                        test rbx, rbx
007B9898  75 0A                           jne 0x1407b98a4
007B989A  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007B989F  E9 FA 02 00 00                  jmp 0x1407b9b9e
007B98A4  0F 28 05 25 53 39 00            movaps xmm0, xmmword ptr [rip + 0x395325]
007B98AB  0F 11 02                        movups xmmword ptr [rdx], xmm0
007B98AE  0F 28 0D 2B 53 39 00            movaps xmm1, xmmword ptr [rip + 0x39532b]
007B98B5  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
007B98B9  0F 28 05 30 53 39 00            movaps xmm0, xmmword ptr [rip + 0x395330]
007B98C0  0F 11 42 20                     movups xmmword ptr [rdx + 0x20], xmm0
007B98C4  0F 28 0D 35 53 39 00            movaps xmm1, xmmword ptr [rip + 0x395335]
007B98CB  0F 11 4A 30                     movups xmmword ptr [rdx + 0x30], xmm1
007B98CF  0F 28 05 3A 53 39 00            movaps xmm0, xmmword ptr [rip + 0x39533a]
007B98D6  0F 11 42 40                     movups xmmword ptr [rdx + 0x40], xmm0
007B98DA  0F 28 0D 3F 53 39 00            movaps xmm1, xmmword ptr [rip + 0x39533f]
007B98E1  0F 11 4A 50                     movups xmmword ptr [rdx + 0x50], xmm1
007B98E5  0F 28 05 44 53 39 00            movaps xmm0, xmmword ptr [rip + 0x395344]
007B98EC  0F 11 42 60                     movups xmmword ptr [rdx + 0x60], xmm0
007B98F0  F2 0F 10 05 48 53 39 00         movsd xmm0, qword ptr [rip + 0x395348]
007B98F8  F2 0F 11 42 70                  movsd qword ptr [rdx + 0x70], xmm0
007B98FD  EB 49                           jmp 0x1407b9948
007B98FF  48 85 FF                        test rdi, rdi
007B9902  74 03                           je 0x1407b9907
007B9904  41 89 31                        mov dword ptr [r9], esi
007B9907  41 BE 01 00 00 00               mov r14d, 1
007B990D  44 38 35 70 59 74 00            cmp byte ptr [rip + 0x745970], r14b
007B9914  77 0A                           ja 0x1407b9920
007B9916  B8 A3 00 00 C0                  mov eax, 0xc00000a3
007B991B  E9 7E 02 00 00                  jmp 0x1407b9b9e
007B9920  44 3B FE                        cmp r15d, esi
007B9923  74 0A                           je 0x1407b992f
007B9925  B8 04 00 00 C0                  mov eax, 0xc0000004
007B992A  E9 6F 02 00 00                  jmp 0x1407b9b9e
007B992F  48 85 DB                        test rbx, rbx
007B9932  75 0A                           jne 0x1407b993e
007B9934  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007B9939  E9 60 02 00 00                  jmp 0x1407b9b9e
007B993E  48 8D 05 63 EB 6A 00            lea rax, [rip + 0x6aeb63]
007B9945  48 89 02                        mov qword ptr [rdx], rax
007B9948  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
007B994D  E9 3B 02 00 00                  jmp 0x1407b9b8d
007B9952  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
007B9957  45 33 F6                        xor r14d, r14d
007B995A  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
007B995F  44 3B FE                        cmp r15d, esi
007B9962  74 0A                           je 0x1407b996e
007B9964  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9969  E9 30 02 00 00                  jmp 0x1407b9b9e
007B996E  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
007B9976  48 85 D2                        test rdx, rdx
007B9979  75 0A                           jne 0x1407b9985
007B997B  B8 30 00 00 C0                  mov eax, 0xc0000030
007B9980  E9 19 02 00 00                  jmp 0x1407b9b9e
007B9985  8B 12                           mov edx, dword ptr [rdx]
007B9987  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
007B998E  45 33 C0                        xor r8d, r8d
007B9991  49 8B CC                        mov rcx, r12
007B9994  E8 87 8F 17 00                  call 0x140932920
007B9999  4C 8B E0                        mov r12, rax
007B999C  48 85 C0                        test rax, rax
007B999F  0F 84 90 00 00 00               je 0x1407b9a35
007B99A5  8B 05 D5 D0 80 00               mov eax, dword ptr [rip + 0x80d0d5]
007B99AB  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007B99AF  45 8B FE                        mov r15d, r14d
007B99B2  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
007B99B7  41 BE 01 00 00 00               mov r14d, 1
007B99BD  44 3B F8                        cmp r15d, eax
007B99C0  73 58                           jae 0x1407b9a1a
007B99C2  49 8B 8C 24 50 05 00 00         mov rcx, qword ptr [r12 + 0x550]
007B99CA  48 3B 0D D7 D0 80 00            cmp rcx, qword ptr [rip + 0x80d0d7]
007B99D1  75 17                           jne 0x1407b99ea
007B99D3  41 8B CF                        mov ecx, r15d
007B99D6  E8 F5 EB B1 FF                  call 0x1402d85d0
007B99DB  48 8B 80 A8 8B 00 00            mov rax, qword ptr [rax + 0x8ba8]
007B99E2  48 05 40 01 00 00               add rax, 0x140
007B99E8  EB 0E                           jmp 0x1407b99f8
007B99EA  41 8B C7                        mov eax, r15d
007B99ED  48 C1 E0 06                     shl rax, 6
007B99F1  48 03 81 40 11 00 00            add rax, qword ptr [rcx + 0x1140]
007B99F8  8B 8C 24 80 00 00 00            mov ecx, dword ptr [rsp + 0x80]
007B99FF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
007B9A03  4C 03 2C C8                     add r13, qword ptr [rax + rcx*8]
007B9A07  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
007B9A0C  45 03 FE                        add r15d, r14d
007B9A0F  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
007B9A14  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
007B9A18  EB A3                           jmp 0x1407b99bd
007B9A1A  33 D2                           xor edx, edx
007B9A1C  49 8B CC                        mov rcx, r12
007B9A1F  E8 3C A7 24 00                  call 0x140a04160
007B9A24  48 85 DB                        test rbx, rbx
007B9A27  0F 84 E9 FA FF FF               je 0x1407b9516
007B9A2D  4C 89 2B                        mov qword ptr [rbx], r13
007B9A30  E9 E1 FA FF FF                  jmp 0x1407b9516
007B9A35  B8 25 02 00 C0                  mov eax, 0xc0000225
007B9A3A  E9 5F 01 00 00                  jmp 0x1407b9b9e
007B9A3F  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007B9A47  48 85 C0                        test rax, rax
007B9A4A  75 0A                           jne 0x1407b9a56
007B9A4C  B8 F3 00 00 C0                  mov eax, 0xc00000f3
007B9A51  E9 48 01 00 00                  jmp 0x1407b9b9e
007B9A56  48 85 FF                        test rdi, rdi
007B9A59  75 0A                           jne 0x1407b9a65
007B9A5B  B8 F2 00 00 C0                  mov eax, 0xc00000f2
007B9A60  E9 39 01 00 00                  jmp 0x1407b9b9e
007B9A65  41 C7 01 20 00 00 00            mov dword ptr [r9], 0x20
007B9A6C  41 83 FF 20                     cmp r15d, 0x20
007B9A70  73 0A                           jae 0x1407b9a7c
007B9A72  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9A77  E9 22 01 00 00                  jmp 0x1407b9b9e
007B9A7C  48 85 DB                        test rbx, rbx
007B9A7F  75 0A                           jne 0x1407b9a8b
007B9A81  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007B9A86  E9 13 01 00 00                  jmp 0x1407b9b9e
007B9A8B  48 8B 00                        mov rax, qword ptr [rax]
007B9A8E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B9A93  0F B7 C0                        movzx eax, ax
007B9A96  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
007B9A9D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007B9AA6  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
007B9AAD  41 BE 01 00 00 00               mov r14d, 1
007B9AB3  66 41 2B C6                     sub ax, r14w
007B9AB7  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
007B9ABE  90                              nop
007B9ABF  45 33 C0                        xor r8d, r8d
007B9AC2  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
007B9AC9  49 8B CC                        mov rcx, r12
007B9ACC  E8 4F 8E 17 00                  call 0x140932920
007B9AD1  4C 8B C0                        mov r8, rax
007B9AD4  48 85 C0                        test rax, rax
007B9AD7  74 49                           je 0x1407b9b22
007B9AD9  44 89 33                        mov dword ptr [rbx], r14d
007B9ADC  8B 48 04                        mov ecx, dword ptr [rax + 4]
007B9ADF  89 4B 04                        mov dword ptr [rbx + 4], ecx
007B9AE2  8B 88 E0 00 00 00               mov ecx, dword ptr [rax + 0xe0]
007B9AE8  89 4B 08                        mov dword ptr [rbx + 8], ecx
007B9AEB  8B 88 EC 00 00 00               mov ecx, dword ptr [rax + 0xec]
007B9AF1  89 4B 0C                        mov dword ptr [rbx + 0xc], ecx
007B9AF4  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
007B9AF7  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
007B9AFA  8B 88 D0 00 00 00               mov ecx, dword ptr [rax + 0xd0]
007B9B00  89 4B 14                        mov dword ptr [rbx + 0x14], ecx
007B9B03  8B 80 C8 00 00 00               mov eax, dword ptr [rax + 0xc8]
007B9B09  89 43 1C                        mov dword ptr [rbx + 0x1c], eax
007B9B0C  41 8B 80 D4 00 00 00            mov eax, dword ptr [r8 + 0xd4]
007B9B13  89 43 18                        mov dword ptr [rbx + 0x18], eax
007B9B16  33 D2                           xor edx, edx
007B9B18  49 8B C8                        mov rcx, r8
007B9B1B  E8 40 A6 24 00                  call 0x140a04160
007B9B20  EB 08                           jmp 0x1407b9b2a
007B9B22  C7 44 24 20 96 02 00 C0         mov dword ptr [rsp + 0x20], 0xc0000296
007B9B2A  E8 81 3D AA FF                  call 0x14025d8b0
007B9B2F  EB 5C                           jmp 0x1407b9b8d
007B9B31  41 83 FF 04                     cmp r15d, 4
007B9B35  74 07                           je 0x1407b9b3e
007B9B37  B8 04 00 00 C0                  mov eax, 0xc0000004
007B9B3C  EB 60                           jmp 0x1407b9b9e
007B9B3E  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
007B9B46  48 85 D2                        test rdx, rdx
007B9B49  75 07                           jne 0x1407b9b52
007B9B4B  B8 30 00 00 C0                  mov eax, 0xc0000030
007B9B50  EB 4C                           jmp 0x1407b9b9e
007B9B52  8B 12                           mov edx, dword ptr [rdx]
007B9B54  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
007B9B5B  45 33 C0                        xor r8d, r8d
007B9B5E  49 8B CC                        mov rcx, r12
007B9B61  E8 BA 8D 17 00                  call 0x140932920
007B9B66  48 85 C0                        test rax, rax
007B9B69  74 24                           je 0x1407b9b8f
007B9B6B  8B B0 F0 00 00 00               mov esi, dword ptr [rax + 0xf0]
007B9B71  33 D2                           xor edx, edx
007B9B73  48 8B C8                        mov rcx, rax
007B9B76  E8 E5 A5 24 00                  call 0x140a04160
007B9B7B  48 85 DB                        test rbx, rbx
007B9B7E  74 02                           je 0x1407b9b82
007B9B80  89 33                           mov dword ptr [rbx], esi
007B9B82  48 85 FF                        test rdi, rdi
007B9B85  74 06                           je 0x1407b9b8d
007B9B87  C7 07 04 00 00 00               mov dword ptr [rdi], 4
007B9B8D  EB 0B                           jmp 0x1407b9b9a
007B9B8F  B8 25 02 00 C0                  mov eax, 0xc0000225
007B9B94  EB 08                           jmp 0x1407b9b9e
007B9B96  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007B9B9A  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
007B9B9E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
007B9BA3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
007B9BA8  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
007B9BAD  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
007B9BB2  48 83 C4 40                     add rsp, 0x40
007B9BB6  41 5F                           pop r15
007B9BB8  41 5E                           pop r14
007B9BBA  41 5D                           pop r13
007B9BBC  C3                              ret
007B9BBD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmiQueryTraceInformation(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (64);
    v_r13 = 0;
    *(unsigned int *)(v_rsp - 56) = 0;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    if (a4 != 0) {
        *(unsigned int *)(a4) = 0;
    }
    if (((unsigned int)((unsigned int)(a1))) > 7) goto loc_007B977E;
    if (((unsigned int)((unsigned int)(a1))) == 7) goto loc_007B96DB;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_007B965B;
    v_r10 = (unsigned int)(((unsigned int)(a1)) - (1));
    if (condition_is_equal) goto loc_007B95E2;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9590;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9530;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B94D4;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B94C7;
    if (((unsigned int)(v_r10)) != 1) goto loc_007B97C0;
    v_stack_m34 = 0;
    if (((unsigned int)((unsigned int)(a3))) < ((unsigned int)(v_r10 + 7))) goto loc_007B94BD;
    if (a2 == 0) goto loc_007B94BD;
    v_stack_m34 = 0;
loc_007B942F:
    v_stack_p28 = (unsigned int)((unsigned int)((unsigned int)(v_r10)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))))) >= (*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 16))) goto loc_007B9492;
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(result + 832), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))), a3, a4);
    if (result == 0) goto loc_007B948D;
    v_stack_p28 = (unsigned int)(0 + 1);
    a2 = ((unsigned int)((unsigned int)(0 + 1))) << (3);
    if (a2 <= ((unsigned int)(a3))) {
        a2 = (unsigned int)((unsigned int)((unsigned int)(v_r10)));
        a1 = 0;
        *(unsigned __int64 *)(a2 + a1 * 8) = a2;
    }
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, result, a4);
    v_stack_m34 = (unsigned int)((unsigned int)(a5));
loc_007B948D:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + 1);
    goto loc_007B942F;
loc_007B9492:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(a5)))) << (3);
    a1 = (unsigned int)(v_stack_m38);
    if (a2 > ((unsigned int)(a3))) { a1 = 261; }
    v_stack_m38 = a1;
    if (a4 == 0) goto loc_007B9B8D;
    *(unsigned int *)(a4) = (unsigned int)(a2);
    goto loc_007B9B8D;
loc_007B94BD:
    goto loc_007B9B9E;
loc_007B94C7:
    v_stack_m38 = 0xC0000003ULL;
    goto loc_007B9B8D;
loc_007B94D4:
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B94E8;
    goto loc_007B9B9E;
loc_007B94E8:
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(result + 832), a3 + 1, a3, a4);
    if (result == 0) goto loc_007B9526;
    v_stack_m28 = (unsigned int)(*(unsigned int *)(result));
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, a4);
    if (0 != 0) {
        *(unsigned __int64 *)(a2) = (unsigned int)(*(unsigned int *)(result));
    }
    if (a4 == 0) goto loc_007B9B8D;
    *(unsigned int *)(a4) = 8;
    goto loc_007B9B8D;
loc_007B9526:
    goto loc_007B9B9E;
loc_007B9530:
    if (((unsigned int)((unsigned int)(a3))) >= 4) goto loc_007B9540;
    goto loc_007B9B9E;
loc_007B9540:
    if (a5 != 0) goto loc_007B9557;
    goto loc_007B9B9E;
loc_007B9557:
    v_stack_m28 = *(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8);
    if (*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8) == 0) goto loc_007B9586;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)) == ((unsigned int)(0xFFFFFFFFULL))) goto loc_007B9586;
    result = (*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)) >> (16);
    if (0 == 0) goto loc_007B96BC;
    *(unsigned int *)(a2) = (unsigned int)((unsigned __int8)(result));
    goto loc_007B96BC;
loc_007B9586:
    goto loc_007B9B9E;
loc_007B9590:
    if (((unsigned int)((unsigned int)(a3))) >= 4) goto loc_007B95A0;
    goto loc_007B9B9E;
loc_007B95A0:
    if (a5 != 0) goto loc_007B95B7;
    goto loc_007B9B9E;
loc_007B95B7:
    v_stack_m28 = *(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8);
    if (*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8) == 0) goto loc_007B95D8;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)) == ((unsigned int)(0xFFFFFFFFULL))) goto loc_007B95D8;
    result = (*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)) >> (32);
    goto loc_007B96B5;
loc_007B95D8:
    goto loc_007B9B9E;
loc_007B95E2:
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B95F6;
    goto loc_007B9B9E;
loc_007B95F6:
    if (a5 != 0) goto loc_007B960D;
    goto loc_007B9B9E;
loc_007B960D:
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000030ULL))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xC0000030ULL))))) < (*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 16))) goto loc_007B9627;
    goto loc_007B9B9E;
loc_007B9627:
    v_stack_m28 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))));
    if ((unsigned int)((unsigned int)(0xC0000008ULL)) == 0) {
        a1 = 0xFFFFULL;
    }
    v_stack_m28 = (unsigned __int16)(a1);
    result = (unsigned int)(0xC0000008ULL);
    if (0 != 0) {
        result = v_stack_m28;
        *(unsigned __int64 *)(a2) = result;
    }
    if (a4 == 0) goto loc_007B9B8D;
    *(unsigned int *)(a4) = 8;
    goto loc_007B9B8D;
loc_007B965B:
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_007B966B;
    goto loc_007B9B9E;
loc_007B966B:
    if (a5 != 0) goto loc_007B9682;
    goto loc_007B9B9E;
loc_007B9682:
    v_stack_m28 = *(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8);
    if (*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8) == 0) goto loc_007B96D1;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)) == ((unsigned int)(0xFFFFFFFFULL))) goto loc_007B96D1;
    v_stack_p28 = (unsigned int)((unsigned __int16)(*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)));
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)((unsigned int)(0xC0000030ULL) + 8)))) < (*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 16))) goto loc_007B96B5;
    goto loc_007B9B9E;
loc_007B96B5:
    if (0 != 0) {
        *(unsigned int *)(a2) = (unsigned int)((unsigned int)(0xC0000008ULL));
    }
    if (a4 == 0) goto loc_007B9B8D;
    *(unsigned int *)(a4) = 4;
    goto loc_007B9B8D;
loc_007B96D1:
    goto loc_007B9B9E;
loc_007B96DB:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007B972C;
    if ((unsigned __int16)(*(unsigned __int16 *)(a5)) == 0) goto loc_007B972C;
    result = *(unsigned __int16 *)(a5);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a5 + 8)))) != 0) {
        result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(a5 + 8), a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a5 + 8) + result * 1) > result) goto loc_007B972A;
    if ((*(unsigned __int64 *)(a5 + 8) + result * 1) < (*(unsigned __int64 *)(a5 + 8))) {
        result = *(unsigned __int8 *)(result);
    }
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B9740;
    goto loc_007B9B9E;
loc_007B9740:
    v_stack_m28 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))));
    result = EtwQueryTraceHandleByLoggerName(a5, v_stack_m28, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (sign_flag) goto loc_007B9B9E;
    if (0 == 0) goto loc_007B9516;
    *(unsigned __int64 *)(a2) = v_stack_m28;
    goto loc_007B9516;
loc_007B977E:
    v_r10 = (unsigned int)((v_r10) - (8));
    if (condition_is_equal) goto loc_007B9B31;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9A3F;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9952;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B98FF;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9860;
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_equal) goto loc_007B9815;
    if (((unsigned int)(v_r10)) == 2) goto loc_007B97CA;
loc_007B97C0:
    goto loc_007B9B9E;
loc_007B97CA:
    if (a4 != 0) {
        *(unsigned int *)(a4) = 8;
    }
    if ((*(unsigned __int8 *)(v_rip + 7625381)) > 1) goto loc_007B97EB;
    goto loc_007B9B9E;
loc_007B97EB:
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B97FA;
    goto loc_007B9B9E;
loc_007B97FA:
    if (0 != 0) goto loc_007B9809;
    goto loc_007B9B9E;
loc_007B9809:
    goto loc_007B9945;
loc_007B9815:
    if (a4 != 0) {
        *(unsigned int *)(a4) = 8;
    }
    if ((*(unsigned __int8 *)(v_rip + 7625306)) > 1) goto loc_007B9836;
    goto loc_007B9B9E;
loc_007B9836:
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B9845;
    goto loc_007B9B9E;
loc_007B9845:
    if (0 != 0) goto loc_007B9854;
    goto loc_007B9B9E;
loc_007B9854:
    goto loc_007B9945;
loc_007B9860:
    if (a4 != 0) {
        *(unsigned int *)(a4) = 120;
    }
    if ((*(unsigned __int8 *)(v_rip + 7625227)) > 1) goto loc_007B9885;
    goto loc_007B9B9E;
loc_007B9885:
    if (((unsigned int)((unsigned int)(a3))) == 120) goto loc_007B9895;
    goto loc_007B9B9E;
loc_007B9895:
    if (0 != 0) goto loc_007B98A4;
    goto loc_007B9B9E;
loc_007B98A4:
    *(unsigned __int64 *)(v_stack_m28) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m28 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m28 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m28 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m28 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m28 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m28 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m28 + 112) = v_xmm0;
    goto loc_007B9948;
loc_007B98FF:
    if (a4 != 0) {
        *(unsigned int *)(a4) = 8;
    }
    if ((*(unsigned __int8 *)(v_rip + 7625072)) > 1) goto loc_007B9920;
    goto loc_007B9B9E;
loc_007B9920:
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B992F;
    goto loc_007B9B9E;
loc_007B992F:
    if (0 != 0) goto loc_007B993E;
    goto loc_007B9B9E;
loc_007B993E:
loc_007B9945:
    *(unsigned __int64 *)(v_stack_m28) = v_rip + 7007075;
loc_007B9948:
    v_stack_m38 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))));
    goto loc_007B9B8D;
loc_007B9952:
    v_stack_m20 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))));
    v_r14 = 0;
    v_stack_m30 = 0;
    if (((unsigned int)((unsigned int)(a3))) == 8) goto loc_007B996E;
    goto loc_007B9B9E;
loc_007B996E:
    if (a5 != 0) goto loc_007B9985;
    goto loc_007B9B9E;
loc_007B9985:
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(unsigned __int64 *)(result + 832), (unsigned int)(*(unsigned int *)(a5)), a3, a4);
    if (result == 0) goto loc_007B9A35;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8442069)));
    v_stack_m30 = 0;
loc_007B99BD:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8442069))))) goto loc_007B9A1A;
    if ((*(unsigned __int64 *)(result + 1360)) != (*(unsigned __int64 *)(v_rip + 8442071))) goto loc_007B99EA;
    result = KeGetPrcb(0, (unsigned int)(*(unsigned int *)(a5)), a3, a4);
    result = (*(unsigned __int64 *)(result + 35752)) + (320);
    goto loc_007B99F8;
loc_007B99EA:
    result = (0) << (6);
    result = (result) + (*(unsigned __int64 *)(0 + 4416));
loc_007B99F8:
    v_r13 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10))))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + (unsigned int)(a5) * 8));
    v_stack_m20 = v_r13;
    v_r15 = (unsigned int)((0) + (1));
    v_stack_m30 = (unsigned int)(v_r15);
    goto loc_007B99BD;
loc_007B9A1A:
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, a4);
    if (0 == 0) goto loc_007B9516;
    *(unsigned __int64 *)(a2) = v_r13;
    goto loc_007B9516;
loc_007B9A35:
    goto loc_007B9B9E;
loc_007B9A3F:
    if (a5 != 0) goto loc_007B9A56;
    goto loc_007B9B9E;
loc_007B9A56:
    if (a4 != 0) goto loc_007B9A65;
    goto loc_007B9B9E;
loc_007B9A65:
    *(unsigned int *)(a4) = 32;
    if (((unsigned int)(v_r15)) >= 32) goto loc_007B9A7C;
    goto loc_007B9B9E;
loc_007B9A7C:
    if (0 != 0) goto loc_007B9A8B;
    goto loc_007B9B9E;
loc_007B9A8B:
    v_stack_m28 = *(unsigned __int64 *)((unsigned int)(0xC00000F0ULL));
    v_stack_p28 = (unsigned int)((unsigned __int16)(*(unsigned __int64 *)((unsigned int)(0xC00000F0ULL))));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(result, (unsigned int)(a5), a3, a4);
    if (result == 0) goto loc_007B9B22;
    *(unsigned int *)(a2) = 1;
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    *(unsigned int *)(a2 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 224)));
    *(unsigned int *)(a2 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 236)));
    *(unsigned int *)(a2 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    *(unsigned int *)(a2 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 208)));
    *(unsigned int *)(a2 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 200)));
    *(unsigned int *)(a2 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 212)));
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, result, a4);
    goto loc_007B9B2A;
loc_007B9B22:
    v_stack_m38 = 0xC0000296ULL;
loc_007B9B2A:
    result = KeLeaveCriticalRegion(result, a2, result, a4);
    goto loc_007B9B8D;
loc_007B9B31:
    if (((unsigned int)(v_r15)) == 4) goto loc_007B9B3E;
    goto loc_007B9B9E;
loc_007B9B3E:
    if (a5 != 0) goto loc_007B9B52;
    goto loc_007B9B9E;
loc_007B9B52:
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(result, (unsigned int)(*(unsigned int *)(a5)), a3, a4);
    if (result == 0) goto loc_007B9B8F;
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, a4);
    if (0 != 0) {
        *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 240)));
    }
    if (a4 != 0) {
        *(unsigned int *)(a4) = 4;
    }
    goto loc_007B9B9A;
loc_007B9B8F:
    goto loc_007B9B9E;
loc_007B9B9A:
loc_007B9B9E:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t WmiQueryTraceInformation(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (64);
    local_r13 = 0;
    *(uint32_t *)(local_rsp - 0x38) = 0;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 0;
    }
    if (((uint32_t)((uint32_t)(Arg1))) > 7) goto loc_007B977E;
    if (((uint32_t)((uint32_t)(Arg1))) == 7) goto loc_007B96DB;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_007B965B;
    local_r10 = (uint32_t)(((uint32_t)(Arg1)) - (1));
    if (condition_is_equal) goto loc_007B95E2;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9590;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9530;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B94D4;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B94C7;
    if (((uint32_t)(local_r10)) != 1) goto loc_007B97C0;
    v_stack_m34 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) < ((uint32_t)(local_r10 + 7))) goto loc_007B94BD;
    if (Arg2 == 0) goto loc_007B94BD;
    v_stack_m34 = 0;
loc_007B942F:
    v_stack_p28 = (uint32_t)((uint32_t)((uint32_t)(local_r10)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))))) >= (*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10))) goto loc_007B9492;
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(result + 0x340), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))), Arg3, Arg4);
    if (result == 0) goto loc_007B948D;
    v_stack_p28 = (uint32_t)(0 + 1);
    Arg2 = ((uint32_t)((uint32_t)(0 + 1))) << (3);
    if (Arg2 <= ((uint32_t)(Arg3))) {
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(local_r10)));
        Arg1 = 0;
        *(uint64_t *)(Arg2 + Arg1 * 8) = Arg2;
    }
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, result, Arg4);
    v_stack_m34 = (uint32_t)((uint32_t)(Arg5));
loc_007B948D:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + 1);
    goto loc_007B942F;
loc_007B9492:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) << (3);
    Arg1 = (uint32_t)(v_stack_m38);
    if (Arg2 > ((uint32_t)(Arg3))) { Arg1 = 261; }
    v_stack_m38 = Arg1;
    if (Arg4 == 0) goto loc_007B9B8D;
    *(uint32_t *)(Arg4) = (uint32_t)(Arg2);
    goto loc_007B9B8D;
loc_007B94BD:
    goto loc_007B9B9E;
loc_007B94C7:
    v_stack_m38 = 0xC0000003ULL;
    goto loc_007B9B8D;
loc_007B94D4:
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B94E8;
    goto loc_007B9B9E;
loc_007B94E8:
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(result + 0x340), Arg3 + 1, Arg3, Arg4);
    if (result == 0) goto loc_007B9526;
    v_stack_m28 = (uint32_t)(*(uint32_t *)(result));
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, Arg4);
    if (0 != 0) {
        *(uint64_t *)(Arg2) = (uint32_t)(*(uint32_t *)(result));
    }
    if (Arg4 == 0) goto loc_007B9B8D;
    *(uint32_t *)(Arg4) = 8;
    goto loc_007B9B8D;
loc_007B9526:
    goto loc_007B9B9E;
loc_007B9530:
    if (((uint32_t)((uint32_t)(Arg3))) >= 4) goto loc_007B9540;
    goto loc_007B9B9E;
loc_007B9540:
    if (Arg5 != NULL) goto loc_007B9557;
    goto loc_007B9B9E;
loc_007B9557:
    v_stack_m28 = *(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8);
    if (*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8) == 0) goto loc_007B9586;
    if ((*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)) == ((uint32_t)(0xFFFFFFFFULL))) goto loc_007B9586;
    result = (*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)) >> (16);
    if (0 == 0) goto loc_007B96BC;
    *(uint32_t *)(Arg2) = (uint32_t)((uint8_t)(result));
    goto loc_007B96BC;
loc_007B9586:
    goto loc_007B9B9E;
loc_007B9590:
    if (((uint32_t)((uint32_t)(Arg3))) >= 4) goto loc_007B95A0;
    goto loc_007B9B9E;
loc_007B95A0:
    if (Arg5 != NULL) goto loc_007B95B7;
    goto loc_007B9B9E;
loc_007B95B7:
    v_stack_m28 = *(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8);
    if (*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8) == 0) goto loc_007B95D8;
    if ((*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)) == ((uint32_t)(0xFFFFFFFFULL))) goto loc_007B95D8;
    result = (*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)) >> (32);
    goto loc_007B96B5;
loc_007B95D8:
    goto loc_007B9B9E;
loc_007B95E2:
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B95F6;
    goto loc_007B9B9E;
loc_007B95F6:
    if (Arg5 != NULL) goto loc_007B960D;
    goto loc_007B9B9E;
loc_007B960D:
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000030ULL))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC0000030ULL))))) < (*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10))) goto loc_007B9627;
    goto loc_007B9B9E;
loc_007B9627:
    v_stack_m28 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))));
    if ((uint32_t)((uint32_t)(0xC0000008ULL)) == 0) {
        Arg1 = 0xFFFFULL;
    }
    v_stack_m28 = (uint16_t)(Arg1);
    result = (uint32_t)(0xC0000008ULL);
    if (0 != 0) {
        result = v_stack_m28;
        *(uint64_t *)(Arg2) = result;
    }
    if (Arg4 == 0) goto loc_007B9B8D;
    *(uint32_t *)(Arg4) = 8;
    goto loc_007B9B8D;
loc_007B965B:
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_007B966B;
    goto loc_007B9B9E;
loc_007B966B:
    if (Arg5 != NULL) goto loc_007B9682;
    goto loc_007B9B9E;
loc_007B9682:
    v_stack_m28 = *(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8);
    if (*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8) == 0) goto loc_007B96D1;
    if ((*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)) == ((uint32_t)(0xFFFFFFFFULL))) goto loc_007B96D1;
    v_stack_p28 = (uint32_t)((uint16_t)(*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)));
    if (((uint32_t)((uint16_t)(*(uint64_t *)((uint32_t)(0xC0000030ULL) + 0x8)))) < (*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10))) goto loc_007B96B5;
    goto loc_007B9B9E;
loc_007B96B5:
    if (0 != 0) {
        *(uint32_t *)(Arg2) = (uint32_t)((uint32_t)(0xC0000008ULL));
    }
    if (Arg4 == 0) goto loc_007B9B8D;
    *(uint32_t *)(Arg4) = 4;
    goto loc_007B9B8D;
loc_007B96D1:
    goto loc_007B9B9E;
loc_007B96DB:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007B972C;
    if ((uint16_t)(*(uint16_t *)(arg5)) == 0) goto loc_007B972C;
    result = *(uint16_t *)(arg5);
    if (((1) & ((uint8_t)(*(uint64_t *)(arg5 + 0x8)))) != 0) {
        result = ExRaiseDatatypeMisalignment(*(uint64_t *)(arg5 + 0x8), Arg2, Arg3, Arg4);
    }
    if ((*(uint64_t *)(arg5 + 0x8) + result * 1) > result) goto loc_007B972A;
    if ((*(uint64_t *)(arg5 + 0x8) + result * 1) < (*(uint64_t *)(arg5 + 0x8))) {
        result = *(uint8_t *)(result);
    }
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B9740;
    goto loc_007B9B9E;
loc_007B9740:
    v_stack_m28 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))));
    result = EtwQueryTraceHandleByLoggerName(Arg5, v_stack_m28, Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (sign_flag) goto loc_007B9B9E;
    if (0 == 0) goto loc_007B9516;
    *(uint64_t *)(Arg2) = v_stack_m28;
    goto loc_007B9516;
loc_007B977E:
    local_r10 = (uint32_t)((local_r10) - (8));
    if (condition_is_equal) goto loc_007B9B31;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9A3F;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9952;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B98FF;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9860;
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_equal) goto loc_007B9815;
    if (((uint32_t)(local_r10)) == 2) goto loc_007B97CA;
loc_007B97C0:
    goto loc_007B9B9E;
loc_007B97CA:
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 8;
    }
    if ((*(uint8_t *)(v_rip + 0x745AA5)) > 1) goto loc_007B97EB;
    goto loc_007B9B9E;
loc_007B97EB:
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B97FA;
    goto loc_007B9B9E;
loc_007B97FA:
    if (0 != 0) goto loc_007B9809;
    goto loc_007B9B9E;
loc_007B9809:
    goto loc_007B9945;
loc_007B9815:
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 8;
    }
    if ((*(uint8_t *)(v_rip + 0x745A5A)) > 1) goto loc_007B9836;
    goto loc_007B9B9E;
loc_007B9836:
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B9845;
    goto loc_007B9B9E;
loc_007B9845:
    if (0 != 0) goto loc_007B9854;
    goto loc_007B9B9E;
loc_007B9854:
    goto loc_007B9945;
loc_007B9860:
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 120;
    }
    if ((*(uint8_t *)(v_rip + 0x745A0B)) > 1) goto loc_007B9885;
    goto loc_007B9B9E;
loc_007B9885:
    if (((uint32_t)((uint32_t)(Arg3))) == 120) goto loc_007B9895;
    goto loc_007B9B9E;
loc_007B9895:
    if (0 != 0) goto loc_007B98A4;
    goto loc_007B9B9E;
loc_007B98A4:
    *(uint64_t *)(v_stack_m28) = v_xmm0;
    *(uint64_t *)(v_stack_m28 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m28 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m28 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m28 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m28 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m28 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_m28 + 0x70) = v_xmm0;
    goto loc_007B9948;
loc_007B98FF:
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 8;
    }
    if ((*(uint8_t *)(v_rip + 0x745970)) > 1) goto loc_007B9920;
    goto loc_007B9B9E;
loc_007B9920:
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B992F;
    goto loc_007B9B9E;
loc_007B992F:
    if (0 != 0) goto loc_007B993E;
    goto loc_007B9B9E;
loc_007B993E:
loc_007B9945:
    *(uint64_t *)(v_stack_m28) = v_rip + 7007075;
loc_007B9948:
    v_stack_m38 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))));
    goto loc_007B9B8D;
loc_007B9952:
    v_stack_m20 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))));
    local_r14 = 0;
    v_stack_m30 = 0;
    if (((uint32_t)((uint32_t)(Arg3))) == 8) goto loc_007B996E;
    goto loc_007B9B9E;
loc_007B996E:
    if (Arg5 != NULL) goto loc_007B9985;
    goto loc_007B9B9E;
loc_007B9985:
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(*(uint64_t *)(result + 0x340), (uint32_t)(*(uint32_t *)(arg5)), Arg3, Arg4);
    if (result == 0) goto loc_007B9A35;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x80D0D5)));
    v_stack_m30 = 0;
loc_007B99BD:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x80D0D5))))) goto loc_007B9A1A;
    if ((*(uint64_t *)(result + 0x550)) != (*(uint64_t *)(v_rip + 0x80D0D7))) goto loc_007B99EA;
    result = KeGetPrcb(0, (uint32_t)(*(uint32_t *)(arg5)), Arg3, Arg4);
    result = (*(uint64_t *)(result + 0x8BA8)) + (320);
    goto loc_007B99F8;
loc_007B99EA:
    result = (0) << (6);
    result = (result) + (*(uint64_t *)(0 + 0x1140));
loc_007B99F8:
    local_r13 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10))))) + (*(uint64_t *)(*(uint64_t *)(result + 0x8) + (uint32_t)(arg5) * 8));
    v_stack_m20 = local_r13;
    local_r15 = (uint32_t)((0) + (1));
    v_stack_m30 = (uint32_t)(local_r15);
    goto loc_007B99BD;
loc_007B9A1A:
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, Arg4);
    if (0 == 0) goto loc_007B9516;
    *(uint64_t *)(Arg2) = local_r13;
    goto loc_007B9516;
loc_007B9A35:
    goto loc_007B9B9E;
loc_007B9A3F:
    if (Arg5 != NULL) goto loc_007B9A56;
    goto loc_007B9B9E;
loc_007B9A56:
    if (Arg4 != 0) goto loc_007B9A65;
    goto loc_007B9B9E;
loc_007B9A65:
    *(uint32_t *)(Arg4) = 32;
    if (((uint32_t)(local_r15)) >= 32) goto loc_007B9A7C;
    goto loc_007B9B9E;
loc_007B9A7C:
    if (0 != 0) goto loc_007B9A8B;
    goto loc_007B9B9E;
loc_007B9A8B:
    v_stack_m28 = *(uint64_t *)((uint32_t)(0xC00000F0ULL));
    v_stack_p28 = (uint32_t)((uint16_t)(*(uint64_t *)((uint32_t)(0xC00000F0ULL))));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(result, (uint32_t)(Arg5), Arg3, Arg4);
    if (result == 0) goto loc_007B9B22;
    *(uint32_t *)(Arg2) = 1;
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xE0)));
    *(uint32_t *)(Arg2 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xEC)));
    *(uint32_t *)(Arg2 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    *(uint32_t *)(Arg2 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xD0)));
    *(uint32_t *)(Arg2 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC8)));
    *(uint32_t *)(Arg2 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xD4)));
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, result, Arg4);
    goto loc_007B9B2A;
loc_007B9B22:
    v_stack_m38 = 0xC0000296ULL;
loc_007B9B2A:
    result = KeLeaveCriticalRegion(result, Arg2, result, Arg4);
    goto loc_007B9B8D;
loc_007B9B31:
    if (((uint32_t)(local_r15)) == 4) goto loc_007B9B3E;
    goto loc_007B9B9E;
loc_007B9B3E:
    if (Arg5 != NULL) goto loc_007B9B52;
    goto loc_007B9B9E;
loc_007B9B52:
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(result, (uint32_t)(*(uint32_t *)(arg5)), Arg3, Arg4);
    if (result == 0) goto loc_007B9B8F;
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, Arg4);
    if (0 != 0) {
        *(uint32_t *)(Arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xF0)));
    }
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = 4;
    }
    goto loc_007B9B9A;
loc_007B9B8F:
    goto loc_007B9B9E;
loc_007B9B9A:
loc_007B9B9E:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m38);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B9370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
