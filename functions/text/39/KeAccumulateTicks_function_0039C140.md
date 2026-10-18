# KeAccumulateTicks

- RVA: `0x0039C140`–`0x0039C84F` (길이 `1,807` bytes)
- VA: `0x000000014039C140`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081974`
- 디코드: `415`개 명령, `1,807/1,807` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x0039C168` → [KiCheckForTimerExpiration](KiCheckForTimerExpiration_function_0039C860.md) (function, `0x0039C860`)
- `0x0039C24B` → [KdPollBreakIn](KdPollBreakIn_function_0039CE80.md) (function, `0x0039CE80`)
- `0x0039C2B1` → [KiRequestSoftwareInterrupt](../25/KiRequestSoftwareInterrupt_function_00250950.md) (function, `0x00250950`)
- `0x0039C370` → [KiDpcWatchdogCounterReset](KiDpcWatchdogCounterReset_function_0039D6A0.md) (function, `0x0039D6A0`)
- `0x0039C3DE` → [KiDpcWatchdogCounterReset](KiDpcWatchdogCounterReset_function_0039D6A0.md) (function, `0x0039D6A0`)
- `0x0039C3F7` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x0039C4C7` → [EtwTraceDpcProfilingStackBegin](../44/EtwTraceDpcProfilingStackBegin_function_0044F25C.md) (function, `0x0044F25C`)
- `0x0039C4ED` → [EtwTraceDpcProfilingStackBegin](../44/EtwTraceDpcProfilingStackBegin_function_0044F25C.md) (function, `0x0044F25C`)
- `0x0039C4FA` → [KiDpcWatchdogCaptureStack](../44/KiDpcWatchdogCaptureStack_function_0044F124.md) (function, `0x0044F124`)
- `0x0039C508` → [EtwTraceDpcProfilingStack](../44/EtwTraceDpcProfilingStack_function_0044F1CC.md) (function, `0x0044F1CC`)
- `0x0039C5D5` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0039C629` → [KiCheckKeepAlive](../30/KiCheckKeepAlive_function_00305058.md) (function, `0x00305058`)
- `0x0039C69D` → [HvlInvokeHypervisorDebugger](../44/HvlInvokeHypervisorDebugger_function_0044F32C.md) (function, `0x0044F32C`)
- `0x0039C6D7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0039C75E` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0039C7AA` → [KiResetGlobalDpcWatchdogProfiler](../4F/KiResetGlobalDpcWatchdogProfiler_function_004FAEF8.md) (function, `0x004FAEF8`)
- `0x0039C7BB` → [KiDpcWatchdogCounterReset](KiDpcWatchdogCounterReset_function_0039D6A0.md) (function, `0x0039D6A0`)
- `0x0039C7D9` → [KiDeferDpcWatchdogViolation](../44/KiDeferDpcWatchdogViolation_function_0044F37C.md) (function, `0x0044F37C`)
- `0x0039C80A` → [HvlInvokeHypervisorDebugger](../44/HvlInvokeHypervisorDebugger_function_0044F32C.md) (function, `0x0044F32C`)
- `0x0039C826` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0039C845` → [DbgBreakPointWithStatus](../4F/DbgBreakPointWithStatus_function_004FE4E0.md) (function, `0x004FE4E0`)

### Direct callers
- [KiUpdateRunTime](KiUpdateRunTime_function_0039BB70.md) at `0x0039BC06`
- [sub_006DCEEE](../6D/Unknown_function_006DCEEE.md) at `0x006DD35E`

### Static image references
- `0x0039C16D` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x0039C1B9` → RVA `0x00FC6FF0` (`ALMOSTRO`; read)
- `0x0039C1C5` → RVA `0x00F233CC` (`.data`; read)
- `0x0039C223` → RVA `0x00F475F8` (`.data`; read)
- `0x0039C231` → RVA `0x00E66808` (`.data`; read)
- `0x0039C239` → RVA `0x00E0AA1C` (`.data`; read)
- `0x0039C242` → RVA `0x00F59CC8` (`.data`; read)
- `0x0039C29B` → RVA `0x00FC50C4` (`ALMOSTRO`; read)
- `0x0039C2BD` → RVA `0x00FC51A0` (`ALMOSTRO`; read)
- `0x0039C2F9` → RVA `0x00FC50C0` (`ALMOSTRO`; read)
- `0x0039C318` → RVA `0x00E0AC78` (`.data`; read/write)
- `0x0039C543` → RVA `0x00FC53C8` (`ALMOSTRO`; read)
- `0x0039C5E8` → RVA `0x00E6680C` (`.data`; read)
- `0x0039C5F0` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0039C5F7` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x0039C5FF` → RVA `0x00FC5006` (`ALMOSTRO`; read)
- `0x0039C609` → RVA `0x00E0AC78` (`.data`; write)
- `0x0039C623` → RVA `0x00E6680C` (`.data`; write)
- `0x0039C67D` → RVA `0x00FC6AF3` (`ALMOSTRO`; read)
- `0x0039C72D` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x0039C734` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x0039C76B` → RVA `0x00FC6E94` (`ALMOSTRO`; read)
- `0x0039C778` → RVA `0x00F475DC` (`.data`; read)
- `0x0039C7CB` → RVA `0x00F1090C` (`.data`; read)
- `0x0039C7F4` → RVA `0x00F4754C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0039C140  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0039C145  55                              push rbp
0039C146  56                              push rsi
0039C147  57                              push rdi
0039C148  41 56                           push r14
0039C14A  41 57                           push r15
0039C14C  48 83 EC 40                     sub rsp, 0x40
0039C150  8B F2                           mov esi, edx
0039C152  45 0F B6 F9                     movzx r15d, r9b
0039C156  8B 94 24 98 00 00 00            mov edx, dword ptr [rsp + 0x98]
0039C15D  41 8B F8                        mov edi, r8d
0039C160  48 8B D9                        mov rbx, rcx
0039C163  83 FA 04                        cmp edx, 4
0039C166  74 05                           je 0x14039c16d
0039C168  E8 F3 06 00 00                  call 0x14039c860
0039C16D  80 3D 21 A9 C2 00 00            cmp byte ptr [rip + 0xc2a921], 0
0039C174  48 8B 6B 08                     mov rbp, qword ptr [rbx + 8]
0039C178  44 0F BE B4 24 90 00 00 00      movsx r14d, byte ptr [rsp + 0x90]
0039C181  74 1B                           je 0x14039c19e
0039C183  F7 45 74 00 04 00 00            test dword ptr [rbp + 0x74], 0x400
0039C18A  75 12                           jne 0x14039c19e
0039C18C  8B 85 4C 04 00 00               mov eax, dword ptr [rbp + 0x44c]
0039C192  8D 0C 00                        lea ecx, [rax + rax]
0039C195  41 0B CE                        or ecx, r14d
0039C198  89 8D 4C 04 00 00               mov dword ptr [rbp + 0x44c], ecx
0039C19E  89 BB C0 38 00 00               mov dword ptr [rbx + 0x38c0], edi
0039C1A4  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
0039C1A9  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
0039C1B1  2B FE                           sub edi, esi
0039C1B3  0F 85 59 01 00 00               jne 0x14039c312
0039C1B9  39 3D 31 AE C2 00               cmp dword ptr [rip + 0xc2ae31], edi
0039C1BF  0F 85 93 00 00 00               jne 0x14039c258
0039C1C5  8B 05 01 72 B8 00               mov eax, dword ptr [rip + 0xb87201]
0039C1CB  83 F8 04                        cmp eax, 4
0039C1CE  0F 85 84 00 00 00               jne 0x14039c258
0039C1D4  EB 4D                           jmp 0x14039c223
0039C1D6  89 83 A4 2D 00 00               mov dword ptr [rbx + 0x2da4], eax
0039C1DC  8B 83 40 86 00 00               mov eax, dword ptr [rbx + 0x8640]
0039C1E2  8B CF                           mov ecx, edi
0039C1E4  89 83 A0 2D 00 00               mov dword ptr [rbx + 0x2da0], eax
0039C1EA  8B 93 5C 38 00 00               mov edx, dword ptr [rbx + 0x385c]
0039C1F0  8B C2                           mov eax, edx
0039C1F2  2B 83 B4 38 00 00               sub eax, dword ptr [rbx + 0x38b4]
0039C1F8  03 83 AC 38 00 00               add eax, dword ptr [rbx + 0x38ac]
0039C1FE  D3 E8                           shr eax, cl
0039C200  89 83 AC 38 00 00               mov dword ptr [rbx + 0x38ac], eax
0039C206  89 93 B4 38 00 00               mov dword ptr [rbx + 0x38b4], edx
0039C20C  8B 83 58 38 00 00               mov eax, dword ptr [rbx + 0x3858]
0039C212  85 C0                           test eax, eax
0039C214  75 75                           jne 0x14039c28b
0039C216  83 AB 54 86 00 00 01            sub dword ptr [rbx + 0x8654], 1
0039C21D  0F 84 C3 00 00 00               je 0x14039c2e6
0039C223  0F B6 0D CE B3 BA 00            movzx ecx, byte ptr [rip + 0xbab3ce]
0039C22A  84 C9                           test cl, cl
0039C22C  74 52                           je 0x14039c280
0039C22E  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0039C231  39 05 D1 A5 AC 00               cmp dword ptr [rip + 0xaca5d1], eax
0039C237  75 1F                           jne 0x14039c258
0039C239  80 3D DC E7 A6 00 00            cmp byte ptr [rip + 0xa6e7dc], 0
0039C240  74 38                           je 0x14039c27a
0039C242  80 3D 7F DA BB 00 00            cmp byte ptr [rip + 0xbbda7f], 0
0039C249  74 0D                           je 0x14039c258
0039C24B  E8 30 0C 00 00                  call 0x14039ce80
0039C250  84 C0                           test al, al
0039C252  0F 85 E8 05 00 00               jne 0x14039c840
0039C258  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
0039C260  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0039C265  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0039C26D  48 83 C4 40                     add rsp, 0x40
0039C271  41 5F                           pop r15
0039C273  41 5E                           pop r14
0039C275  5F                              pop rdi
0039C276  5E                              pop rsi
0039C277  5D                              pop rbp
0039C278  C3                              ret
0039C279  CC                              int3
0039C27A  84 C9                           test cl, cl
0039C27C  75 CD                           jne 0x14039c24b
0039C27E  EB C2                           jmp 0x14039c242
0039C280  80 3D 41 DA BB 00 00            cmp byte ptr [rip + 0xbbda41], 0
0039C287  75 A5                           jne 0x14039c22e
0039C289  EB CD                           jmp 0x14039c258
0039C28B  0F B7 8B BC 38 00 00            movzx ecx, word ptr [rbx + 0x38bc]
0039C292  F6 C1 03                        test cl, 3
0039C295  0F 85 7B FF FF FF               jne 0x14039c216
0039C29B  8B 05 23 8E C2 00               mov eax, dword ptr [rip + 0xc28e23]
0039C2A1  89 83 54 86 00 00               mov dword ptr [rbx + 0x8654], eax
0039C2A7  F6 C1 AF                        test cl, 0xaf
0039C2AA  75 0A                           jne 0x14039c2b6
0039C2AC  B2 02                           mov dl, 2
0039C2AE  48 8B CB                        mov rcx, rbx
0039C2B1  E8 9A 46 EB FF                  call 0x140250950
0039C2B6  8B 8B A8 38 00 00               mov ecx, dword ptr [rbx + 0x38a8]
0039C2BC  90                              nop
0039C2BD  8B 05 DD 8E C2 00               mov eax, dword ptr [rip + 0xc28edd]
0039C2C3  39 83 AC 38 00 00               cmp dword ptr [rbx + 0x38ac], eax
0039C2C9  0F 83 54 FF FF FF               jae 0x14039c223
0039C2CF  83 F9 01                        cmp ecx, 1
0039C2D2  0F 86 4B FF FF FF               jbe 0x14039c223
0039C2D8  8D 41 FF                        lea eax, [rcx - 1]
0039C2DB  89 83 A8 38 00 00               mov dword ptr [rbx + 0x38a8], eax
0039C2E1  E9 3D FF FF FF                  jmp 0x14039c223
0039C2E6  8B 05 D8 8D C2 00               mov eax, dword ptr [rip + 0xc28dd8]
0039C2EC  89 83 54 86 00 00               mov dword ptr [rbx + 0x8654], eax
0039C2F2  8B 83 A8 38 00 00               mov eax, dword ptr [rbx + 0x38a8]
0039C2F8  90                              nop
0039C2F9  3B 05 C1 8D C2 00               cmp eax, dword ptr [rip + 0xc28dc1]
0039C2FF  0F 83 1E FF FF FF               jae 0x14039c223
0039C305  FF C0                           inc eax
0039C307  89 83 A8 38 00 00               mov dword ptr [rbx + 0x38a8], eax
0039C30D  E9 11 FF FF FF                  jmp 0x14039c223
0039C312  80 7B 21 00                     cmp byte ptr [rbx + 0x21], 0
0039C316  74 0D                           je 0x14039c325
0039C318  80 05 59 E9 A6 00 FF            add byte ptr [rip + 0xa6e959], 0xff
0039C31F  0F 84 C3 02 00 00               je 0x14039c5e8
0039C325  45 84 F6                        test r14b, r14b
0039C328  0F 85 92 00 00 00               jne 0x14039c3c0
0039C32E  0F B6 43 20                     movzx eax, byte ptr [rbx + 0x20]
0039C332  33 F6                           xor esi, esi
0039C334  40 38 35 5A A7 C2 00            cmp byte ptr [rip + 0xc2a75a], sil
0039C33B  0F 85 C8 00 00 00               jne 0x14039c409
0039C341  01 BB 44 86 00 00               add dword ptr [rbx + 0x8644], edi
0039C347  3C 02                           cmp al, 2
0039C349  0F 84 E1 00 00 00               je 0x14039c430
0039C34F  80 7B 20 01                     cmp byte ptr [rbx + 0x20], 1
0039C353  0F 87 F9 02 00 00               ja 0x14039c652
0039C359  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0039C35D  01 B8 8C 02 00 00               add dword ptr [rax + 0x28c], edi
0039C363  41 80 FF 02                     cmp r15b, 2
0039C367  0F 83 F7 00 00 00               jae 0x14039c464
0039C36D  48 8B CB                        mov rcx, rbx
0039C370  E8 2B 13 00 00                  call 0x14039d6a0
0039C375  FF 83 EC 83 00 00               inc dword ptr [rbx + 0x83ec]
0039C37B  85 F6                           test esi, esi
0039C37D  0F 85 E7 00 00 00               jne 0x14039c46a
0039C383  80 3D 0B A7 C2 00 00            cmp byte ptr [rip + 0xc2a70b], 0
0039C38A  74 59                           je 0x14039c3e5
0039C38C  83 FF 08                        cmp edi, 8
0039C38F  0F 83 C0 00 00 00               jae 0x14039c455
0039C395  8B 8B 40 86 00 00               mov ecx, dword ptr [rbx + 0x8640]
0039C39B  2B 8B A0 2D 00 00               sub ecx, dword ptr [rbx + 0x2da0]
0039C3A1  6B C1 0F                        imul eax, ecx, 0xf
0039C3A4  8B CF                           mov ecx, edi
0039C3A6  01 83 A4 2D 00 00               add dword ptr [rbx + 0x2da4], eax
0039C3AC  8B 83 A4 2D 00 00               mov eax, dword ptr [rbx + 0x2da4]
0039C3B2  C1 E8 04                        shr eax, 4
0039C3B5  48 83 E9 01                     sub rcx, 1
0039C3B9  75 F7                           jne 0x14039c3b2
0039C3BB  E9 16 FE FF FF                  jmp 0x14039c1d6
0039C3C0  80 3D CE A6 C2 00 00            cmp byte ptr [rip + 0xc2a6ce], 0
0039C3C7  75 0C                           jne 0x14039c3d5
0039C3C9  01 BB 48 86 00 00               add dword ptr [rbx + 0x8648], edi
0039C3CF  01 BD DC 02 00 00               add dword ptr [rbp + 0x2dc], edi
0039C3D5  FF 83 EC 83 00 00               inc dword ptr [rbx + 0x83ec]
0039C3DB  48 8B CB                        mov rcx, rbx
0039C3DE  E8 BD 12 00 00                  call 0x14039d6a0
0039C3E3  EB 9E                           jmp 0x14039c383
0039C3E5  48 3B 6B 18                     cmp rbp, qword ptr [rbx + 0x18]
0039C3E9  74 A1                           je 0x14039c38c
0039C3EB  80 7B 20 01                     cmp byte ptr [rbx + 0x20], 1
0039C3EF  77 9B                           ja 0x14039c38c
0039C3F1  48 8B D3                        mov rdx, rbx
0039C3F4  48 8B CD                        mov rcx, rbp
0039C3F7  E8 A4 B7 EB FF                  call 0x140257ba0
0039C3FC  83 F8 08                        cmp eax, 8
0039C3FF  7D 8B                           jge 0x14039c38c
0039C401  01 BB 6C 86 00 00               add dword ptr [rbx + 0x866c], edi
0039C407  EB 83                           jmp 0x14039c38c
0039C409  3C 02                           cmp al, 2
0039C40B  0F 85 52 FF FF FF               jne 0x14039c363
0039C411  0F B6 83 BA 38 00 00            movzx eax, byte ptr [rbx + 0x38ba]
0039C418  84 C0                           test al, al
0039C41A  0F 84 43 FF FF FF               je 0x14039c363
0039C420  FF 83 5C 86 00 00               inc dword ptr [rbx + 0x865c]
0039C426  BE 01 00 00 00                  mov esi, 1
0039C42B  E9 33 FF FF FF                  jmp 0x14039c363
0039C430  0F B6 83 BA 38 00 00            movzx eax, byte ptr [rbx + 0x38ba]
0039C437  84 C0                           test al, al
0039C439  0F 84 10 FF FF FF               je 0x14039c34f
0039C43F  01 BB 4C 86 00 00               add dword ptr [rbx + 0x864c], edi
0039C445  BE 01 00 00 00                  mov esi, 1
0039C44A  FF 83 5C 86 00 00               inc dword ptr [rbx + 0x865c]
0039C450  E9 0E FF FF FF                  jmp 0x14039c363
0039C455  C7 83 A4 2D 00 00 00 00 00 00   mov dword ptr [rbx + 0x2da4], 0
0039C45F  E9 78 FD FF FF                  jmp 0x14039c1dc
0039C464  FF 83 AC 83 00 00               inc dword ptr [rbx + 0x83ac]
0039C46A  44 8B B3 40 87 00 00            mov r14d, dword ptr [rbx + 0x8740]
0039C471  41 8B F6                        mov esi, r14d
0039C474  8B 83 B4 83 00 00               mov eax, dword ptr [rbx + 0x83b4]
0039C47A  45 85 F6                        test r14d, r14d
0039C47D  0F 84 5D 03 00 00               je 0x14039c7e0
0039C483  44 3B F0                        cmp r14d, eax
0039C486  0F 87 54 03 00 00               ja 0x14039c7e0
0039C48C  85 F6                           test esi, esi
0039C48E  0F 84 98 03 00 00               je 0x14039c82c
0039C494  44 8B BB 5C 86 00 00            mov r15d, dword ptr [rbx + 0x865c]
0039C49B  44 8B AB AC 83 00 00            mov r13d, dword ptr [rbx + 0x83ac]
0039C4A2  45 3B FD                        cmp r15d, r13d
0039C4A5  45 8B E5                        mov r12d, r13d
0039C4A8  45 0F 47 E7                     cmova r12d, r15d
0039C4AC  41 3B F4                        cmp esi, r12d
0039C4AF  75 1B                           jne 0x14039c4cc
0039C4B1  8B 8B EC 83 00 00               mov ecx, dword ptr [rbx + 0x83ec]
0039C4B7  45 8B CD                        mov r9d, r13d
0039C4BA  45 8B C7                        mov r8d, r15d
0039C4BD  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
0039C4C5  8B D6                           mov edx, esi
0039C4C7  E8 90 2D 0B 00                  call 0x14044f25c
0039C4CC  45 85 F6                        test r14d, r14d
0039C4CF  74 21                           je 0x14039c4f2
0039C4D1  45 3B F7                        cmp r14d, r15d
0039C4D4  75 1C                           jne 0x14039c4f2
0039C4D6  8B 8B EC 83 00 00               mov ecx, dword ptr [rbx + 0x83ec]
0039C4DC  45 8B CD                        mov r9d, r13d
0039C4DF  45 8B C7                        mov r8d, r15d
0039C4E2  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0039C4EA  41 8B D7                        mov edx, r15d
0039C4ED  E8 6A 2D 0B 00                  call 0x14044f25c
0039C4F2  41 3B F4                        cmp esi, r12d
0039C4F5  77 16                           ja 0x14039c50d
0039C4F7  48 8B CB                        mov rcx, rbx
0039C4FA  E8 25 2C 0B 00                  call 0x14044f124
0039C4FF  8B 8B EC 83 00 00               mov ecx, dword ptr [rbx + 0x83ec]
0039C505  41 8B D4                        mov edx, r12d
0039C508  E8 BF 2C 0B 00                  call 0x14044f1cc
0039C50D  45 33 FF                        xor r15d, r15d
0039C510  83 FE 20                        cmp esi, 0x20
0039C513  0F 82 C6 00 00 00               jb 0x14039c5df
0039C519  D1 EE                           shr esi, 1
0039C51B  44 3B E6                        cmp r12d, esi
0039C51E  41 0F 94 C7                     sete r15b
0039C522  8B 83 CC 38 00 00               mov eax, dword ptr [rbx + 0x38cc]
0039C528  48 8D B3 5C 86 00 00            lea rsi, [rbx + 0x865c]
0039C52F  8B 16                           mov edx, dword ptr [rsi]
0039C531  48 8B CE                        mov rcx, rsi
0039C534  85 C0                           test eax, eax
0039C536  74 08                           je 0x14039c540
0039C538  3B D0                           cmp edx, eax
0039C53A  0F 83 9D 01 00 00               jae 0x14039c6dd
0039C540  44 8B 09                        mov r9d, dword ptr [rcx]
0039C543  4C 8D 1D 7E 8E C2 00            lea r11, [rip + 0xc28e7e]
0039C54A  8B 8B A8 83 00 00               mov ecx, dword ptr [rbx + 0x83a8]
0039C550  33 F6                           xor esi, esi
0039C552  44 8B 83 AC 83 00 00            mov r8d, dword ptr [rbx + 0x83ac]
0039C559  45 33 F6                        xor r14d, r14d
0039C55C  8B 93 60 86 00 00               mov edx, dword ptr [rbx + 0x8660]
0039C562  45 33 E4                        xor r12d, r12d
0039C565  45 33 ED                        xor r13d, r13d
0039C568  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
0039C56F  45 33 D2                        xor r10d, r10d
0039C572  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0039C577  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0039C57C  85 C9                           test ecx, ecx
0039C57E  74 2A                           je 0x14039c5aa
0039C580  8B C1                           mov eax, ecx
0039C582  D1 E8                           shr eax, 1
0039C584  44 3B C0                        cmp r8d, eax
0039C587  40 0F 94 C6                     sete sil
0039C58B  44 3B C1                        cmp r8d, ecx
0039C58E  72 1A                           jb 0x14039c5aa
0039C590  41 BE 01 00 00 00               mov r14d, 1
0039C596  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
0039C59B  45 8B E6                        mov r12d, r14d
0039C59E  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
0039C5A3  44 8B E9                        mov r13d, ecx
0039C5A6  45 8D 56 01                     lea r10d, [r14 + 1]
0039C5AA  85 D2                           test edx, edx
0039C5AC  74 09                           je 0x14039c5b7
0039C5AE  44 3B CA                        cmp r9d, edx
0039C5B1  0F 83 A6 00 00 00               jae 0x14039c65d
0039C5B7  45 85 F6                        test r14d, r14d
0039C5BA  0F 85 BD 00 00 00               jne 0x14039c67d
0039C5C0  41 0B F7                        or esi, r15d
0039C5C3  0F 84 BA FD FF FF               je 0x14039c383
0039C5C9  48 8D 8B D8 8A 00 00            lea rcx, [rbx + 0x8ad8]
0039C5D0  45 33 C0                        xor r8d, r8d
0039C5D3  33 D2                           xor edx, edx
0039C5D5  E8 76 B6 E6 FF                  call 0x140207c50
0039C5DA  E9 A4 FD FF FF                  jmp 0x14039c383
0039C5DF  41 83 FC 10                     cmp r12d, 0x10
0039C5E3  E9 36 FF FF FF                  jmp 0x14039c51e
0039C5E8  44 0F B6 05 1C A2 AC 00         movzx r8d, byte ptr [rip + 0xaca21c]
0039C5F0  48 8D 35 49 C6 C2 00            lea rsi, [rip + 0xc2c649]
0039C5F7  8B 0D 83 A4 C2 00               mov ecx, dword ptr [rip + 0xc2a483]
0039C5FD  33 D2                           xor edx, edx
0039C5FF  0F B6 05 00 8A C2 00            movzx eax, byte ptr [rip + 0xc28a00]
0039C606  45 8B E0                        mov r12d, r8d
0039C609  88 05 69 E6 A6 00               mov byte ptr [rip + 0xa6e669], al
0039C60F  4A 8B 34 C6                     mov rsi, qword ptr [rsi + r8*8]
0039C613  41 FF C0                        inc r8d
0039C616  44 3B C1                        cmp r8d, ecx
0039C619  41 0F B6 C0                     movzx eax, r8b
0039C61D  48 8B CE                        mov rcx, rsi
0039C620  0F 42 D0                        cmovb edx, eax
0039C623  88 15 E3 A1 AC 00               mov byte ptr [rip + 0xaca1e3], dl
0039C629  E8 2A 8A F6 FF                  call 0x140305058
0039C62E  84 C0                           test al, al
0039C630  0F 84 EF FC FF FF               je 0x14039c325
0039C636  83 BE A0 83 00 00 00            cmp dword ptr [rsi + 0x83a0], 0
0039C63D  0F 84 A4 01 00 00               je 0x14039c7e7
0039C643  C7 86 A0 83 00 00 00 00 00 00   mov dword ptr [rsi + 0x83a0], 0
0039C64D  E9 D3 FC FF FF                  jmp 0x14039c325
0039C652  01 BB 50 86 00 00               add dword ptr [rbx + 0x8650], edi
0039C658  E9 06 FD FF FF                  jmp 0x14039c363
0039C65D  45 33 E4                        xor r12d, r12d
0039C660  C7 84 24 98 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x98], 1
0039C66B  4D 8B E9                        mov r13, r9
0039C66E  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0039C673  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
0039C678  45 8D 54 24 03                  lea r10d, [r12 + 3]
0039C67D  80 3D 6F A4 C2 00 00            cmp byte ptr [rip + 0xc2a46f], 0
0039C684  0F 84 AA 01 00 00               je 0x14039c834
0039C68A  0F 31                           rdtsc
0039C68C  48 C1 E2 20                     shl rdx, 0x20
0039C690  41 8B CA                        mov ecx, r10d
0039C693  48 0B C2                        or rax, rdx
0039C696  33 D2                           xor edx, edx
0039C698  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0039C69D  E8 8A 2C 0B 00                  call 0x14044f32c
0039C6A2  80 3D 4F AF BA 00 00            cmp byte ptr [rip + 0xbaaf4f], 0
0039C6A9  0F 85 BC 00 00 00               jne 0x14039c76b
0039C6AF  83 BC 24 98 00 00 00 00         cmp dword ptr [rsp + 0x98], 0
0039C6B7  0F 85 0E 01 00 00               jne 0x14039c7cb
0039C6BD  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0039C6C2  4D 8B C5                        mov r8, r13
0039C6C5  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
0039C6CA  49 8B D4                        mov rdx, r12
0039C6CD  B9 33 01 00 00                  mov ecx, 0x133
0039C6D2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0039C6D7  E8 84 0F 16 00                  call 0x1404fd660
0039C6DC  CC                              int3
0039C6DD  4C 8B 8B D0 38 00 00            mov r9, qword ptr [rbx + 0x38d0]
0039C6E4  4D 85 C9                        test r9, r9
0039C6E7  0F 84 53 FE FF FF               je 0x14039c540
0039C6ED  4C 8B 83 60 38 00 00            mov r8, qword ptr [rbx + 0x3860]
0039C6F4  4D 85 C0                        test r8, r8
0039C6F7  0F 84 43 FE FF FF               je 0x14039c540
0039C6FD  41 8B 41 48                     mov eax, dword ptr [r9 + 0x48]
0039C701  49 8D 48 18                     lea rcx, [r8 + 0x18]
0039C705  85 C0                           test eax, eax
0039C707  74 19                           je 0x14039c722
0039C709  48 8B 01                        mov rax, qword ptr [rcx]
0039C70C  49 39 41 40                     cmp qword ptr [r9 + 0x40], rax
0039C710  75 04                           jne 0x14039c716
0039C712  41 89 51 48                     mov dword ptr [r9 + 0x48], edx
0039C716  48 8D 8B 5C 86 00 00            lea rcx, [rbx + 0x865c]
0039C71D  E9 1E FE FF FF                  jmp 0x14039c540
0039C722  41 89 51 48                     mov dword ptr [r9 + 0x48], edx
0039C726  48 8B 01                        mov rax, qword ptr [rcx]
0039C729  49 89 41 40                     mov qword ptr [r9 + 0x40], rax
0039C72D  4C 33 05 1C AB C2 00            xor r8, qword ptr [rip + 0xc2ab1c]
0039C734  48 8B 05 3D A8 C2 00            mov rax, qword ptr [rip + 0xc2a83d]
0039C73B  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0039C73F  49 0F C8                        bswap r8
0039C742  4C 33 01                        xor r8, qword ptr [rcx]
0039C745  8B C8                           mov ecx, eax
0039C747  49 D3 C8                        ror r8, cl
0039C74A  49 8B C9                        mov rcx, r9
0039C74D  4C 33 C0                        xor r8, rax
0039C750  48 B8 77 72 DD F3 C7 C6 35 7E   movabs rax, 0x7e35c6c7f3dd7277
0039C75A  4C 0F AF C0                     imul r8, rax
0039C75E  E8 ED B4 E6 FF                  call 0x140207c50
0039C763  48 8B CE                        mov rcx, rsi
0039C766  E9 D5 FD FF FF                  jmp 0x14039c540
0039C76B  83 3D 22 A7 C2 00 00            cmp dword ptr [rip + 0xc2a722], 0
0039C772  0F 85 37 FF FF FF               jne 0x14039c6af
0039C778  80 3D 5D AE BA 00 00            cmp byte ptr [rip + 0xbaae5d], 0
0039C77F  0F 85 2A FF FF FF               jne 0x14039c6af
0039C785  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
0039C78C  85 C0                           test eax, eax
0039C78E  74 02                           je 0x14039c792
0039C790  CD 2C                           int 0x2c
0039C792  45 85 F6                        test r14d, r14d
0039C795  74 02                           je 0x14039c799
0039C797  CD 2C                           int 0x2c
0039C799  85 C0                           test eax, eax
0039C79B  74 12                           je 0x14039c7af
0039C79D  48 8B CB                        mov rcx, rbx
0039C7A0  C7 83 5C 86 00 00 00 00 00 00   mov dword ptr [rbx + 0x865c], 0
0039C7AA  E8 49 E7 15 00                  call 0x1404faef8
0039C7AF  45 85 F6                        test r14d, r14d
0039C7B2  0F 84 08 FE FF FF               je 0x14039c5c0
0039C7B8  48 8B CB                        mov rcx, rbx
0039C7BB  E8 E0 0E 00 00                  call 0x14039d6a0
0039C7C0  FF 83 EC 83 00 00               inc dword ptr [rbx + 0x83ec]
0039C7C6  E9 F5 FD FF FF                  jmp 0x14039c5c0
0039C7CB  8B 05 3B 41 B7 00               mov eax, dword ptr [rip + 0xb7413b]
0039C7D1  85 C0                           test eax, eax
0039C7D3  0F 8E E4 FE FF FF               jle 0x14039c6bd
0039C7D9  E8 9E 2B 0B 00                  call 0x14044f37c
0039C7DE  EB BD                           jmp 0x14039c79d
0039C7E0  8B F0                           mov esi, eax
0039C7E2  E9 A5 FC FF FF                  jmp 0x14039c48c
0039C7E7  80 3D 05 A3 C2 00 00            cmp byte ptr [rip + 0xc2a305], 0
0039C7EE  0F 84 4F FE FF FF               je 0x14039c643
0039C7F4  8B 05 52 AD BA 00               mov eax, dword ptr [rip + 0xbaad52]
0039C7FA  A8 03                           test al, 3
0039C7FC  0F 85 41 FE FF FF               jne 0x14039c643
0039C802  49 8B D4                        mov rdx, r12
0039C805  B9 01 00 00 00                  mov ecx, 1
0039C80A  E8 1D 2B 0B 00                  call 0x14044f32c
0039C80F  0F B6 15 F0 87 C2 00            movzx edx, byte ptr [rip + 0xc287f0]
0039C816  4C 8B CE                        mov r9, rsi
0039C819  45 33 C0                        xor r8d, r8d
0039C81C  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0039C821  B9 01 01 00 00                  mov ecx, 0x101
0039C826  E8 35 0E 16 00                  call 0x1404fd660
0039C82B  CC                              int3
0039C82C  45 33 FF                        xor r15d, r15d
0039C82F  E9 EE FC FF FF                  jmp 0x14039c522
0039C834  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
0039C83B  E9 59 FF FF FF                  jmp 0x14039c799
0039C840  B9 01 00 00 00                  mov ecx, 1
0039C845  E8 96 1C 16 00                  call 0x1404fe4e0
0039C84A  E9 09 FA FF FF                  jmp 0x14039c258
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeAccumulateTicks(__int64 a1, int a2, int a3, unsigned __int8 a4, unsigned __int8 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p98;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (64);
    if (((unsigned int)((unsigned int)(a6))) != 4) {
        result = KiCheckForTimerExpiration(a1, (unsigned int)(a6), a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 12757281)) == 0) goto loc_0039C19E;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 116)) & (0x400ULL)) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1100);
        a1 = result + result * 1;
        a1 = (unsigned int)((a1) | ((unsigned int)((__int8)(a5))));
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 1100) = (unsigned int)(a1);
    }
    *(unsigned int *)(a1 + 14528) = (unsigned int)((unsigned int)(a3));
    v_stack_p10 = v_r12;
    v_stack_p18 = v_r13;
    v_rdi = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)((unsigned int)(a2))));
    if (condition_is_not_equal) goto loc_0039C312;
    if ((*(unsigned int *)(v_rip + 12758577)) != ((unsigned int)(v_rdi))) goto loc_0039C258;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12087809)))) != 4) goto loc_0039C258;
    goto loc_0039C223;
loc_0039C1D6:
    *(unsigned int *)(a1 + 11684) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12087809)));
loc_0039C1DC:
    *(unsigned int *)(a1 + 11680) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 34368)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 14428))))) - (*(unsigned int *)(a1 + 14516)));
    result = (unsigned int)((result) + (*(unsigned int *)(a1 + 14508)));
    result = (unsigned int)((result) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    *(unsigned int *)(a1 + 14508) = (unsigned int)(result);
    *(unsigned int *)(a1 + 14516) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 14428)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 14424))) != 0) goto loc_0039C28B;
loc_0039C216:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 14424))) == 0) goto loc_0039C2E6;
loc_0039C223:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12235726)) == 0) goto loc_0039C280;
loc_0039C22E:
    if ((*(unsigned int *)(v_rip + 11314641)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36))))) goto loc_0039C258;
    if ((*(unsigned __int8 *)(v_rip + 10938332)) == 0) goto loc_0039C27A;
loc_0039C242:
    if ((*(unsigned __int8 *)(v_rip + 12311167)) == 0) goto loc_0039C258;
loc_0039C24B:
    result = KdPollBreakIn(*(unsigned __int8 *)(v_rip + 12235726), (unsigned int)(*(unsigned int *)(a1 + 14428)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0039C840;
loc_0039C258:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0039C27A:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12235726)) != 0) goto loc_0039C24B;
    goto loc_0039C242;
loc_0039C280:
    if ((*(unsigned __int8 *)(v_rip + 12311105)) != 0) goto loc_0039C22E;
    goto loc_0039C258;
loc_0039C28B:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_p20 + 14524))) & (3)) != 0) goto loc_0039C216;
    *(unsigned int *)(v_stack_p20 + 34388) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12750371)));
    result = (unsigned int)(*(unsigned int *)(v_rip + 12750371));
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_p20 + 14524))) & (175)) == 0) {
        a2 = 2;
        a1 = v_stack_p20;
        result = KiRequestSoftwareInterrupt(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_stack_p20 + 14508)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12750557))))) goto loc_0039C223;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 14504)))) <= 1) goto loc_0039C223;
    *(unsigned int *)(v_stack_p20 + 14504) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 14504)) - 1);
    goto loc_0039C223;
loc_0039C2E6:
    *(unsigned int *)(v_stack_p20 + 34388) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12750296)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 14504)))) >= (*(unsigned int *)(v_rip + 12750273))) goto loc_0039C223;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 14504))) + 1);
    *(unsigned int *)(v_stack_p20 + 14504) = (unsigned int)(result);
    goto loc_0039C223;
loc_0039C312:
    if ((*(unsigned __int8 *)(v_stack_p20 + 33)) == 0) goto loc_0039C325;
    if ((*(unsigned __int8 *)(v_stack_p20 + 33)) == 0) goto loc_0039C5E8;
loc_0039C325:
    if ((unsigned __int8)((__int8)(a5)) != 0) goto loc_0039C3C0;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 12756826)) != 0) goto loc_0039C409;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 32))) == 2) goto loc_0039C430;
loc_0039C34F:
    if ((*(unsigned __int8 *)(v_stack_p20 + 32)) > 1) goto loc_0039C652;
loc_0039C363:
    if (a4 >= 2) goto loc_0039C464;
    result = KiDpcWatchdogCounterReset(v_stack_p20, a2, a3, a4);
    if (0 != 0) goto loc_0039C46A;
loc_0039C383:
    if ((*(unsigned __int8 *)(v_rip + 12756747)) == 0) goto loc_0039C3E5;
loc_0039C38C:
    if (((unsigned int)(v_rdi)) >= 8) goto loc_0039C455;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 34368))) - (*(unsigned int *)(v_stack_p20 + 11680)));
    result = (unsigned int)((result) * ((unsigned int)(a1)));
loc_0039C3B2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 11684))) >> (4));
    a1 = ((unsigned int)((unsigned int)(v_rdi))) - (1);
    if (condition_is_not_equal) goto loc_0039C3B2;
    goto loc_0039C1D6;
loc_0039C3C0:
    if ((*(unsigned __int8 *)(v_rip + 12756686)) == 0) {
    }
    result = KiDpcWatchdogCounterReset(v_stack_p20, a2, a3, a4);
    goto loc_0039C383;
loc_0039C3E5:
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(v_stack_p20 + 24))) goto loc_0039C38C;
    if ((*(unsigned __int8 *)(v_stack_p20 + 32)) > 1) goto loc_0039C38C;
    result = KiQueryEffectivePriorityThread(*(unsigned __int64 *)(a1 + 8), v_stack_p20, a3, a4);
    if (((unsigned int)(result)) >= 8) goto loc_0039C38C;
    goto loc_0039C38C;
loc_0039C409:
    if (((unsigned __int8)(result)) != 2) goto loc_0039C363;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 14522)) == 0) goto loc_0039C363;
    goto loc_0039C363;
loc_0039C430:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p20 + 14522)) == 0) goto loc_0039C34F;
    goto loc_0039C363;
loc_0039C455:
    *(unsigned int *)(v_stack_p20 + 11684) = 0;
    goto loc_0039C1DC;
loc_0039C464:
loc_0039C46A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624))) == 0) goto loc_0039C7E0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33716))))) goto loc_0039C7E0;
loc_0039C48C:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624))))) == 0) goto loc_0039C82C;
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708))))) { v_r12 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396))); }
    result = (unsigned int)(*(unsigned int *)(v_stack_p20 + 33716));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))))) == ((unsigned int)(v_r12))) {
        a1 = *(unsigned int *)(v_stack_p20 + 33772);
        a4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708)));
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
        v_stack_p20 = 0;
        a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))));
        result = EtwTraceDpcProfilingStackBegin(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624))) == 0) goto loc_0039C4F2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396))))) {
        a1 = *(unsigned int *)(v_stack_p20 + 33772);
        a4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708)));
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
        v_stack_p20 = 1;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
        result = EtwTraceDpcProfilingStackBegin(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))))) <= ((unsigned int)(v_r12))) {
        a1 = v_stack_p20;
        result = KiDpcWatchdogCaptureStack(a1, a2, a3, a4);
        a1 = *(unsigned int *)(v_stack_p20 + 33772);
        a2 = (unsigned int)(v_r12);
        result = EtwTraceDpcProfilingStack(a1, a2, a3, a4);
    }
    v_r15 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624)))))) < 32) goto loc_0039C5DF;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34624))))) >> (1));
loc_0039C51E:
    v_r15 = (((unsigned int)(v_r12)) == ((unsigned int)(v_rsi))) ? 1 : 0;
loc_0039C522:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 14540))) == 0) goto loc_0039C540;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 14540))))) goto loc_0039C6DD;
loc_0039C540:
    v_rsi = 0;
    v_r14 = 0;
    v_r12 = 0;
    v_r13 = 0;
    v_stack_p98 = 0;
    v_r10 = 0;
    v_stack_p30 = 0;
    v_stack_p70 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33704))) == 0) goto loc_0039C5AA;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33704))))) >> (1));
    v_rsi = (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708)))) == ((unsigned int)(result))) ? 1 : 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33708)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33704))))) {
        v_r14 = 1;
        v_stack_p70 = 0;
        v_r12 = (unsigned int)(v_r14);
        v_stack_p30 = v_rip + 12750462;
        v_r13 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 33704)));
        v_r10 = v_r14 + 1;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34400))) == 0) goto loc_0039C5B7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 34400))))) goto loc_0039C65D;
loc_0039C5B7:
    if ((unsigned int)(v_r14) != 0) goto loc_0039C67D;
loc_0039C5C0:
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(v_r15)));
    if (condition_is_equal) goto loc_0039C383;
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(v_stack_p20 + 35544, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
    goto loc_0039C383;
loc_0039C5DF:
    goto loc_0039C51E;
loc_0039C5E8:
    a2 = 0;
    *(unsigned __int8 *)(v_rip + 10937961) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 12749312));
    a3 = (unsigned int)((*(unsigned __int8 *)(v_rip + 11313692)) + 1);
    if (a3 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12756099))))) { a2 = (unsigned int)((unsigned __int8)(a3)); }
    *(unsigned __int8 *)(v_rip + 11313635) = (unsigned __int8)(a2);
    result = KiCheckKeepAlive(*(unsigned __int64 *)(v_rip + 12764745 + *(unsigned __int8 *)(v_rip + 11313692) * 8), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
    if ((unsigned __int8)(result) == 0) goto loc_0039C325;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12764745 + *(unsigned __int8 *)(v_rip + 11313692) * 8) + 33696)) == 0) goto loc_0039C7E7;
loc_0039C643:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12764745 + *(unsigned __int8 *)(v_rip + 11313692) * 8) + 33696) = 0;
    goto loc_0039C325;
loc_0039C652:
    goto loc_0039C363;
loc_0039C65D:
    v_r12 = 0;
    v_stack_p98 = 1;
    v_stack_p30 = a2;
    v_stack_p70 = v_rip + 12750462;
loc_0039C67D:
    if ((*(unsigned __int8 *)(v_rip + 12756079)) == 0) goto loc_0039C834;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = 0;
    v_stack_p38 = result;
    result = HvlInvokeHypervisorDebugger((unsigned int)((unsigned int)(v_r12 + 3)), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)));
    if ((*(unsigned __int8 *)(v_rip + 12234575)) != 0) goto loc_0039C76B;
loc_0039C6AF:
    if (a6 != 0) goto loc_0039C7CB;
loc_0039C6BD:
    v_stack_p20 = v_stack_p70;
    result = KeBugCheckEx(307, 0, (unsigned int)(*(unsigned int *)(v_stack_p20 + 34396)), v_stack_p30);
loc_0039C6DD:
    if (*(unsigned __int64 *)(v_stack_p20 + 14544) == 0) goto loc_0039C540;
    if (*(unsigned __int64 *)(v_stack_p20 + 14432) == 0) goto loc_0039C540;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 14544) + 72))) == 0) goto loc_0039C722;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 14544) + 64)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 14432) + 24))) {
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 14544) + 72) = 0;
    }
    goto loc_0039C540;
loc_0039C722:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 14544) + 72) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 14544) + 64) = *(unsigned __int64 *)(v_stack_p20 + 34396);
    a3 = (*(unsigned __int64 *)(v_stack_p20 + 14432)) ^ (*(unsigned __int64 *)(v_rip + 12757788));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_stack_p20 + 34396));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_rip + 12757053));
    a3 = (a3) * (*(unsigned __int64 *)(v_rip + 12757053));
    result = KeInsertQueueDpc(*(unsigned __int64 *)(v_stack_p20 + 14544), *(unsigned __int64 *)(v_stack_p20 + 8), a3, *(unsigned __int64 *)(v_stack_p20 + 14544));
    goto loc_0039C540;
loc_0039C76B:
    if ((*(unsigned int *)(v_rip + 12756770)) != 0) goto loc_0039C6AF;
    if ((*(unsigned __int8 *)(v_rip + 12234333)) != 0) goto loc_0039C6AF;
    if ((unsigned int)((unsigned int)(a6)) != 0) {
    }
    if ((unsigned int)(v_r14) != 0) {
    }
    result = (unsigned int)(a6);
    if ((unsigned int)((unsigned int)(a6)) != 0) {
        a1 = v_stack_p20;
        *(unsigned int *)(v_stack_p20 + 34396) = 0;
        result = KiResetGlobalDpcWatchdogProfiler(a1, *(unsigned __int64 *)(v_stack_p20 + 8), a3, *(unsigned __int64 *)(v_stack_p20 + 14544));
    }
    if ((unsigned int)(v_r14) == 0) goto loc_0039C5C0;
    result = KiDpcWatchdogCounterReset(v_stack_p20, *(unsigned __int64 *)(v_stack_p20 + 8), a3, *(unsigned __int64 *)(v_stack_p20 + 14544));
    goto loc_0039C5C0;
loc_0039C7CB:
    if (condition_is_less_or_equal) goto loc_0039C6BD;
    result = KiDeferDpcWatchdogViolation(v_stack_p20, *(unsigned __int64 *)(v_stack_p20 + 8), a3, *(unsigned __int64 *)(v_stack_p20 + 14544));
    goto loc_0039C79D;
loc_0039C7E0:
    goto loc_0039C48C;
loc_0039C7E7:
    if ((*(unsigned __int8 *)(v_rip + 12755717)) == 0) goto loc_0039C643;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12234066)))) & (3)) != 0) goto loc_0039C643;
    result = HvlInvokeHypervisorDebugger(1, 0, a3, *(unsigned __int64 *)(v_stack_p20 + 14544));
    a3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(257, *(unsigned __int8 *)(v_rip + 12748784), a3, (unsigned int)((unsigned int)(result)));
loc_0039C82C:
    v_r15 = 0;
    goto loc_0039C522;
loc_0039C834:
    goto loc_0039C799;
loc_0039C840:
    result = DbgBreakPointWithStatus(1, *(unsigned __int8 *)(v_rip + 12748784), a3, (unsigned int)((unsigned int)(result)));
    goto loc_0039C258;
}
```

## 5. (Beta) C Style

```c
int64_t KeAccumulateTicks(void *Arg1, int32_t Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p70;
    uint32_t v_stack_p98;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (64);
    if (((uint32_t)((uint32_t)(Arg6))) != 4) {
        result = KiCheckForTimerExpiration(Arg1, (uint32_t)(Arg6), Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xC2A921)) == 0) goto loc_0039C19E;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x74)) & (0x400ULL)) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x44C);
        Arg1 = result + result * 1;
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)((int8_t)(Arg5))));
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x44C) = (uint32_t)(Arg1);
    }
    *(uint32_t *)(arg1 + 0x38C0) = (uint32_t)((uint32_t)(Arg3));
    v_stack_p10 = local_r12;
    v_stack_p18 = local_r13;
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)((uint32_t)(Arg2))));
    if (condition_is_not_equal) goto loc_0039C312;
    if ((*(uint32_t *)(v_rip + 0xC2AE31)) != ((uint32_t)(local_rdi))) goto loc_0039C258;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB87201)))) != 4) goto loc_0039C258;
    goto loc_0039C223;
loc_0039C1D6:
    *(uint32_t *)(arg1 + 0x2DA4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB87201)));
loc_0039C1DC:
    *(uint32_t *)(arg1 + 0x2DA0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8640)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x385C))))) - (*(uint32_t *)(arg1 + 0x38B4)));
    result = (uint32_t)((result) + (*(uint32_t *)(arg1 + 0x38AC)));
    result = (uint32_t)((result) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    *(uint32_t *)(arg1 + 0x38AC) = (uint32_t)(result);
    *(uint32_t *)(arg1 + 0x38B4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x385C)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3858))) != 0) goto loc_0039C28B;
loc_0039C216:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3858))) == 0) goto loc_0039C2E6;
loc_0039C223:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xBAB3CE)) == 0) goto loc_0039C280;
loc_0039C22E:
    if ((*(uint32_t *)(v_rip + 0xACA5D1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24))))) goto loc_0039C258;
    if ((*(uint8_t *)(v_rip + 0xA6E7DC)) == 0) goto loc_0039C27A;
loc_0039C242:
    if ((*(uint8_t *)(v_rip + 0xBBDA7F)) == 0) goto loc_0039C258;
loc_0039C24B:
    result = KdPollBreakIn(*(uint8_t *)(v_rip + 0xBAB3CE), (uint32_t)(*(uint32_t *)(arg1 + 0x385C)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0039C840;
loc_0039C258:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0039C27A:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xBAB3CE)) != 0) goto loc_0039C24B;
    goto loc_0039C242;
loc_0039C280:
    if ((*(uint8_t *)(v_rip + 0xBBDA41)) != 0) goto loc_0039C22E;
    goto loc_0039C258;
loc_0039C28B:
    if ((((uint8_t)(*(uint16_t *)(v_stack_p20 + 0x38BC))) & (3)) != 0) goto loc_0039C216;
    *(uint32_t *)(v_stack_p20 + 0x8654) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC28E23)));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC28E23));
    if ((((uint8_t)(*(uint16_t *)(v_stack_p20 + 0x38BC))) & (175)) == 0) {
        Arg2 = 2;
        Arg1 = v_stack_p20;
        result = KiRequestSoftwareInterrupt(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_stack_p20 + 0x38AC)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC28EDD))))) goto loc_0039C223;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38A8)))) <= 1) goto loc_0039C223;
    *(uint32_t *)(v_stack_p20 + 0x38A8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38A8)) - 1);
    goto loc_0039C223;
loc_0039C2E6:
    *(uint32_t *)(v_stack_p20 + 0x8654) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC28DD8)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38A8)))) >= (*(uint32_t *)(v_rip + 0xC28DC1))) goto loc_0039C223;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38A8))) + 1);
    *(uint32_t *)(v_stack_p20 + 0x38A8) = (uint32_t)(result);
    goto loc_0039C223;
loc_0039C312:
    if ((*(uint8_t *)(v_stack_p20 + 0x21)) == 0) goto loc_0039C325;
    if ((*(uint8_t *)(v_stack_p20 + 0x21)) == 0) goto loc_0039C5E8;
loc_0039C325:
    if ((uint8_t)((int8_t)(Arg5)) != 0) goto loc_0039C3C0;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0xC2A75A)) != 0) goto loc_0039C409;
    if (((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x20))) == 2) goto loc_0039C430;
loc_0039C34F:
    if ((*(uint8_t *)(v_stack_p20 + 0x20)) > 1) goto loc_0039C652;
loc_0039C363:
    if (Arg4 >= 2) goto loc_0039C464;
    result = KiDpcWatchdogCounterReset(v_stack_p20, Arg2, Arg3, Arg4);
    if (0 != 0) goto loc_0039C46A;
loc_0039C383:
    if ((*(uint8_t *)(v_rip + 0xC2A70B)) == 0) goto loc_0039C3E5;
loc_0039C38C:
    if (((uint32_t)(local_rdi)) >= 8) goto loc_0039C455;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8640))) - (*(uint32_t *)(v_stack_p20 + 0x2DA0)));
    result = (uint32_t)((result) * ((uint32_t)(Arg1)));
loc_0039C3B2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x2DA4))) >> (4));
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) - (1);
    if (condition_is_not_equal) goto loc_0039C3B2;
    goto loc_0039C1D6;
loc_0039C3C0:
    if ((*(uint8_t *)(v_rip + 0xC2A6CE)) == 0) {
    }
    result = KiDpcWatchdogCounterReset(v_stack_p20, Arg2, Arg3, Arg4);
    goto loc_0039C383;
loc_0039C3E5:
    if ((*(uint64_t *)(arg1 + 0x8)) == (*(uint64_t *)(v_stack_p20 + 0x18))) goto loc_0039C38C;
    if ((*(uint8_t *)(v_stack_p20 + 0x20)) > 1) goto loc_0039C38C;
    result = KiQueryEffectivePriorityThread(*(uint64_t *)(arg1 + 0x8), v_stack_p20, Arg3, Arg4);
    if (((uint32_t)(result)) >= 8) goto loc_0039C38C;
    goto loc_0039C38C;
loc_0039C409:
    if (((uint8_t)(result)) != 2) goto loc_0039C363;
    if ((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x38BA)) == 0) goto loc_0039C363;
    goto loc_0039C363;
loc_0039C430:
    if ((uint8_t)(*(uint8_t *)(v_stack_p20 + 0x38BA)) == 0) goto loc_0039C34F;
    goto loc_0039C363;
loc_0039C455:
    *(uint32_t *)(v_stack_p20 + 0x2DA4) = 0;
    goto loc_0039C1DC;
loc_0039C464:
loc_0039C46A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740))) == 0) goto loc_0039C7E0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83B4))))) goto loc_0039C7E0;
loc_0039C48C:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740))))) == 0) goto loc_0039C82C;
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC))))) { local_r12 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C))); }
    result = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83B4));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))))) == ((uint32_t)(local_r12))) {
        Arg1 = *(uint32_t *)(v_stack_p20 + 0x83EC);
        Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC)));
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
        v_stack_p20 = 0;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))));
        result = EtwTraceDpcProfilingStackBegin(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740))) == 0) goto loc_0039C4F2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C))))) {
        Arg1 = *(uint32_t *)(v_stack_p20 + 0x83EC);
        Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC)));
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
        v_stack_p20 = 1;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
        result = EtwTraceDpcProfilingStackBegin(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))))) <= ((uint32_t)(local_r12))) {
        Arg1 = v_stack_p20;
        result = KiDpcWatchdogCaptureStack(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint32_t *)(v_stack_p20 + 0x83EC);
        Arg2 = (uint32_t)(local_r12);
        result = EtwTraceDpcProfilingStack(Arg1, Arg2, Arg3, Arg4);
    }
    local_r15 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740)))))) < 32) goto loc_0039C5DF;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8740))))) >> (1));
loc_0039C51E:
    local_r15 = (((uint32_t)(local_r12)) == ((uint32_t)(local_rsi))) ? 1 : 0;
loc_0039C522:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38CC))) == 0) goto loc_0039C540;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x38CC))))) goto loc_0039C6DD;
loc_0039C540:
    local_rsi = 0;
    local_r14 = 0;
    local_r12 = 0;
    local_r13 = 0;
    v_stack_p98 = 0;
    local_r10 = 0;
    v_stack_p30 = 0;
    v_stack_p70 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83A8))) == 0) goto loc_0039C5AA;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83A8))))) >> (1));
    local_rsi = (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC)))) == ((uint32_t)(result))) ? 1 : 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83AC)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83A8))))) {
        local_r14 = 1;
        v_stack_p70 = 0;
        local_r12 = (uint32_t)(local_r14);
        v_stack_p30 = v_rip + 12750462;
        local_r13 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x83A8)));
        local_r10 = local_r14 + 1;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8660))) == 0) goto loc_0039C5B7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x8660))))) goto loc_0039C65D;
loc_0039C5B7:
    if ((uint32_t)(local_r14) != 0) goto loc_0039C67D;
loc_0039C5C0:
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(local_r15)));
    if (condition_is_equal) goto loc_0039C383;
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(v_stack_p20 + 35544, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
    goto loc_0039C383;
loc_0039C5DF:
    goto loc_0039C51E;
loc_0039C5E8:
    Arg2 = 0;
    *(uint8_t *)(v_rip + 0xA6E669) = (uint8_t)(*(uint8_t *)(v_rip + 0xC28A00));
    Arg3 = (uint32_t)((*(uint8_t *)(v_rip + 0xACA21C)) + 1);
    if (Arg3 < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2A483))))) { Arg2 = (uint32_t)((uint8_t)(Arg3)); }
    *(uint8_t *)(v_rip + 0xACA1E3) = (uint8_t)(Arg2);
    result = KiCheckKeepAlive(*(uint64_t *)(v_rip + 0xC2C649 + *(uint8_t *)(v_rip + 0xACA21C) * 8), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
    if ((uint8_t)(result) == 0) goto loc_0039C325;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xC2C649 + *(uint8_t *)(v_rip + 0xACA21C) * 8) + 0x83A0)) == 0) goto loc_0039C7E7;
loc_0039C643:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xC2C649 + *(uint8_t *)(v_rip + 0xACA21C) * 8) + 0x83A0) = 0;
    goto loc_0039C325;
loc_0039C652:
    goto loc_0039C363;
loc_0039C65D:
    local_r12 = 0;
    v_stack_p98 = 1;
    v_stack_p30 = Arg2;
    v_stack_p70 = v_rip + 12750462;
loc_0039C67D:
    if ((*(uint8_t *)(v_rip + 0xC2A46F)) == 0) goto loc_0039C834;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = 0;
    v_stack_p38 = result;
    result = HvlInvokeHypervisorDebugger((uint32_t)((uint32_t)(local_r12 + 3)), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)));
    if ((*(uint8_t *)(v_rip + 0xBAAF4F)) != 0) goto loc_0039C76B;
loc_0039C6AF:
    if (Arg6 != 0) goto loc_0039C7CB;
loc_0039C6BD:
    v_stack_p20 = v_stack_p70;
    result = KeBugCheckEx(307, 0, (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x865C)), v_stack_p30);
loc_0039C6DD:
    if (*(uint64_t *)(v_stack_p20 + 0x38D0) == 0) goto loc_0039C540;
    if (*(uint64_t *)(v_stack_p20 + 0x3860) == 0) goto loc_0039C540;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x38D0) + 0x48))) == 0) goto loc_0039C722;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x38D0) + 0x40)) == (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x3860) + 0x18))) {
        *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x38D0) + 0x48) = 0;
    }
    goto loc_0039C540;
loc_0039C722:
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x38D0) + 0x48) = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x38D0) + 0x40) = *(uint64_t *)(v_stack_p20 + 0x865C);
    Arg3 = (*(uint64_t *)(v_stack_p20 + 0x3860)) ^ (*(uint64_t *)(v_rip + 0xC2AB1C));
    Arg3 = (Arg3) ^ (*(uint64_t *)(v_stack_p20 + 0x865C));
    Arg3 = (Arg3) ^ (*(uint64_t *)(v_rip + 0xC2A83D));
    Arg3 = (Arg3) * (*(uint64_t *)(v_rip + 0xC2A83D));
    result = KeInsertQueueDpc(*(uint64_t *)(v_stack_p20 + 0x38D0), *(uint64_t *)(v_stack_p20 + 0x8), Arg3, *(uint64_t *)(v_stack_p20 + 0x38D0));
    goto loc_0039C540;
loc_0039C76B:
    if ((*(uint32_t *)(v_rip + 0xC2A722)) != 0) goto loc_0039C6AF;
    if ((*(uint8_t *)(v_rip + 0xBAAE5D)) != 0) goto loc_0039C6AF;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) {
    }
    if ((uint32_t)(local_r14) != 0) {
    }
    result = (uint32_t)(Arg6);
    if ((uint32_t)((uint32_t)(Arg6)) != 0) {
        Arg1 = v_stack_p20;
        *(uint32_t *)(v_stack_p20 + 0x865C) = 0;
        result = KiResetGlobalDpcWatchdogProfiler(Arg1, *(uint64_t *)(v_stack_p20 + 0x8), Arg3, *(uint64_t *)(v_stack_p20 + 0x38D0));
    }
    if ((uint32_t)(local_r14) == 0) goto loc_0039C5C0;
    result = KiDpcWatchdogCounterReset(v_stack_p20, *(uint64_t *)(v_stack_p20 + 0x8), Arg3, *(uint64_t *)(v_stack_p20 + 0x38D0));
    goto loc_0039C5C0;
loc_0039C7CB:
    if (condition_is_less_or_equal) goto loc_0039C6BD;
    result = KiDeferDpcWatchdogViolation(v_stack_p20, *(uint64_t *)(v_stack_p20 + 0x8), Arg3, *(uint64_t *)(v_stack_p20 + 0x38D0));
    goto loc_0039C79D;
loc_0039C7E0:
    goto loc_0039C48C;
loc_0039C7E7:
    if ((*(uint8_t *)(v_rip + 0xC2A305)) == 0) goto loc_0039C643;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAAD52)))) & (3)) != 0) goto loc_0039C643;
    result = HvlInvokeHypervisorDebugger(1, 0, Arg3, *(uint64_t *)(v_stack_p20 + 0x38D0));
    Arg3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(257, *(uint8_t *)(v_rip + 0xC287F0), Arg3, (uint32_t)((uint32_t)(result)));
loc_0039C82C:
    local_r15 = 0;
    goto loc_0039C522;
loc_0039C834:
    goto loc_0039C799;
loc_0039C840:
    result = DbgBreakPointWithStatus(1, *(uint8_t *)(v_rip + 0xC287F0), Arg3, (uint32_t)((uint32_t)(result)));
    goto loc_0039C258;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x2DA0` | `32` | `R` |
| `Arg1` | `+ 0x2DA0` | `32` | `W` |
| `Arg1` | `+ 0x2DA4` | `32` | `R` |
| `Arg1` | `+ 0x2DA4` | `32` | `R/W` |
| `Arg1` | `+ 0x2DA4` | `32` | `W` |
| `Arg1` | `+ 0x3858` | `32` | `R` |
| `Arg1` | `+ 0x385C` | `32` | `R` |
| `Arg1` | `+ 0x3860` | `64` | `R` |
| `Arg1` | `+ 0x38A8` | `32` | `R` |
| `Arg1` | `+ 0x38A8` | `32` | `W` |
| `Arg1` | `+ 0x38AC` | `32` | `R` |
| `Arg1` | `+ 0x38AC` | `32` | `W` |
| `Arg1` | `+ 0x38B4` | `32` | `R` |
| `Arg1` | `+ 0x38B4` | `32` | `W` |
| `Arg1` | `+ 0x38BA` | `8` | `R` |
| `Arg1` | `+ 0x38BC` | `16` | `R` |
| `Arg1` | `+ 0x38C0` | `32` | `W` |
| `Arg1` | `+ 0x38CC` | `32` | `R` |
| `Arg1` | `+ 0x38D0` | `64` | `R` |
| `Arg1` | `+ 0x83A8` | `32` | `R` |
| `Arg1` | `+ 0x83AC` | `32` | `R` |
| `Arg1` | `+ 0x83AC` | `32` | `R/W` |
| `Arg1` | `+ 0x83B4` | `32` | `R` |
| `Arg1` | `+ 0x83EC` | `32` | `R` |
| `Arg1` | `+ 0x83EC` | `32` | `R/W` |
| `Arg1` | `+ 0x8640` | `32` | `R` |

추가 오프셋 14개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039C140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
