# KiScanSharedReadyThreads

- RVA: `0x0046F120`–`0x0046F67A` (길이 `1,370` bytes)
- VA: `0x000000014046F120`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ABC34`
- 디코드: `339`개 명령, `1,370/1,370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0046F247` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0046F37C` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0046F39C` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0046F404` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0046F419` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0046F4A3` → [KiDeferredReadyThread](../39/KiDeferredReadyThread_function_00398640.md) (function, `0x00398640`)
- `0x0046F4CE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0046F4DD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0046F524` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0046F5A5` → [KiReadGuestSchedulerAssistPriority](../30/KiReadGuestSchedulerAssistPriority_function_00304BE4.md) (function, `0x00304BE4`)
- `0x0046F5C8` → [KiRemoveThreadFromSharedReadyQueue](../20/KiRemoveThreadFromSharedReadyQueue_function_002019B0.md) (function, `0x002019B0`)
- `0x0046F5D4` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0046F628` → [KiSetPriorityBoost](../39/KiSetPriorityBoost_function_00398A40.md) (function, `0x00398A40`)
- `0x0046F649` → [EtwTraceAntiStarvationBoost](../64/EtwTraceAntiStarvationBoost_function_0064F568.md) (function, `0x0064F568`)

### Direct callers
- [KiNormalPriorityReadyScan](../21/KiNormalPriorityReadyScan_function_0021B400.md) at `0x0021B43C`
- [sub_0021C284](../21/Unknown_function_0021C284.md) at `0x0021C4A3`

### Static image references
- `0x0046F16E` → RVA `0x00FC508C` (`ALMOSTRO`; read)
- `0x0046F176` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0046F1B2` → RVA `0x00FC511C` (`ALMOSTRO`; read)
- `0x0046F1B9` → RVA `0x00FC52A4` (`ALMOSTRO`; read)
- `0x0046F282` → RVA `0x00FC509C` (`ALMOSTRO`; read)
- `0x0046F288` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x0046F2A5` → RVA `0x00FC50CC` (`ALMOSTRO`; read)
- `0x0046F45D` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0046F4C4` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0046F579` → RVA `0x00FC6C4C` (`ALMOSTRO`; read)
- `0x0046F595` → RVA `0x00FC51C0` (`ALMOSTRO`; read)
- `0x0046F635` → RVA `0x00FC6B08` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x0046F19E` → [sub_006F3522](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F212` → [sub_006F3522 + 0xA0](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F223` → [sub_006F3522 + 0x79](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F24F` → [sub_006F3522 + 0x79](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F3F5` → [sub_006F3522 + 0x60](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F4EF` → [sub_006F3522 + 0x40](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F500` → [sub_006F3522 + 0x19](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F52C` → [sub_006F3522 + 0x19](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F56A` → [sub_006F3522 + 0x49](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F574` → [sub_006F3522 + 0x49](../6F/Unknown_function_006F3522.md) (`tail-transfer`)
  - `0x0046F65D` → [sub_006F3522 + 0xA9](../6F/Unknown_function_006F3522.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0046F120  48 8B C4                        mov rax, rsp
0046F123  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
0046F127  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0046F12B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0046F12F  55                              push rbp
0046F130  53                              push rbx
0046F131  56                              push rsi
0046F132  57                              push rdi
0046F133  41 54                           push r12
0046F135  41 55                           push r13
0046F137  41 56                           push r14
0046F139  41 57                           push r15
0046F13B  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0046F13F  48 81 EC 88 00 00 00            sub rsp, 0x88
0046F146  41 8A C0                        mov al, r8b
0046F149  45 33 C9                        xor r9d, r9d
0046F14C  4C 89 4D F7                     mov qword ptr [rbp - 9], r9
0046F150  0F 57 C0                        xorps xmm0, xmm0
0046F153  4C 8D 42 40                     lea r8, [rdx + 0x40]
0046F157  48 8B DA                        mov rbx, rdx
0046F15A  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
0046F15E  84 C0                           test al, al
0046F160  74 41                           je 0x14046f1a3
0046F162  44 0F B6 AA C4 02 00 00         movzx r13d, byte ptr [rdx + 0x2c4]
0046F16A  41 8D 79 08                     lea edi, [r9 + 8]
0046F16E  44 0F AF 2D 16 5F B5 00         imul r13d, dword ptr [rip + 0xb55f16]
0046F176  0F BA 25 BA 79 B5 00 15         bt dword ptr [rip + 0xb579ba], 0x15
0046F17E  44 8A BA C3 02 00 00            mov r15b, byte ptr [rdx + 0x2c3]
0046F185  89 7D DB                        mov dword ptr [rbp - 0x25], edi
0046F188  0F 82 C6 00 00 00               jb 0x14046f254
0046F18E  44 89 4D FF                     mov dword ptr [rbp - 1], r9d
0046F192  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0046F198  0F 83 6E 02 00 00               jae 0x14046f40c
0046F19E  E9 7F 43 28 00                  jmp 0x1406f3522
0046F1A3  F7 05 8B 79 B5 00 00 00 00 0C   test dword ptr [rip + 0xb5798b], 0xc000000
0046F1AD  BF 01 00 00 00                  mov edi, 1
0046F1B2  44 8B 25 63 5F B5 00            mov r12d, dword ptr [rip + 0xb55f63]
0046F1B9  44 8B 2D E4 60 B5 00            mov r13d, dword ptr [rip + 0xb560e4]
0046F1C0  44 8A BA C2 02 00 00            mov r15b, byte ptr [rdx + 0x2c2]
0046F1C7  89 7D DB                        mov dword ptr [rbp - 0x25], edi
0046F1CA  44 89 65 D7                     mov dword ptr [rbp - 0x29], r12d
0046F1CE  0F 85 5D 03 00 00               jne 0x14046f531
0046F1D4  0F BA 25 5C 79 B5 00 15         bt dword ptr [rip + 0xb5795c], 0x15
0046F1DC  0F 83 07 02 00 00               jae 0x14046f3e9
0046F1E2  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
0046F1E6  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0046F1EA  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
0046F1EE  90                              nop
0046F1EF  48 87 13                        xchg qword ptr [rbx], rdx
0046F1F2  48 85 D2                        test rdx, rdx
0046F1F5  0F 85 1A 02 00 00               jne 0x14046f415
0046F1FB  8B 73 08                        mov esi, dword ptr [rbx + 8]
0046F1FE  81 E6 FE 7F 00 00               and esi, 0x7ffe
0046F204  0F 85 6F 03 00 00               jne 0x14046f579
0046F20A  0F BA 25 26 79 B5 00 15         bt dword ptr [rip + 0xb57926], 0x15
0046F212  0F 83 AA 43 28 00               jae 0x1406f35c2
0046F218  0F 0D 4D C7                     prefetchw byte ptr [rbp - 0x39]
0046F21C  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0046F220  48 85 C0                        test rax, rax
0046F223  0F 85 72 43 28 00               jne 0x1406f359b
0046F229  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0046F22D  48 8D 45 C7                     lea rax, [rbp - 0x39]
0046F231  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
0046F236  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F23A  48 3B C1                        cmp rax, rcx
0046F23D  0F 84 2B 04 00 00               je 0x14046f66e
0046F243  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F247  E8 54 88 DA FF                  call 0x140217aa0
0046F24C  45 33 C9                        xor r9d, r9d
0046F24F  E9 47 43 28 00                  jmp 0x1406f359b
0046F254  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
0046F258  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0046F25C  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
0046F260  90                              nop
0046F261  48 87 13                        xchg qword ptr [rbx], rdx
0046F264  48 85 D2                        test rdx, rdx
0046F267  0F 85 93 01 00 00               jne 0x14046f400
0046F26D  8B 73 08                        mov esi, dword ptr [rbx + 8]
0046F270  81 E6 00 03 00 00               and esi, 0x300
0046F276  0F 84 6B 02 00 00               je 0x14046f4e7
0046F27C  8B 05 9A 5E B5 00               mov eax, dword ptr [rip + 0xb55e9a]
0046F282  8B 15 14 5E B5 00               mov edx, dword ptr [rip + 0xb55e14]
0046F288  0F AF 15 09 5E B5 00            imul edx, dword ptr [rip + 0xb55e09]
0046F28F  89 45 D7                        mov dword ptr [rbp - 0x29], eax
0046F292  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0046F29C  C7 45 F3 0B 00 00 00            mov dword ptr [rbp - 0xd], 0xb
0046F2A3  8B 00                           mov eax, dword ptr [rax]
0046F2A5  2B 05 21 5E B5 00               sub eax, dword ptr [rip + 0xb55e21]
0046F2AB  89 55 EF                        mov dword ptr [rbp - 0x11], edx
0046F2AE  41 0F B6 CF                     movzx ecx, r15b
0046F2B2  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
0046F2B5  D3 CE                           ror esi, cl
0046F2B7  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
0046F2BA  4C 89 4D F7                     mov qword ptr [rbp - 9], r9
0046F2BE  0F BC C6                        bsf eax, esi
0046F2C1  0F BB C6                        btc esi, eax
0046F2C4  89 45 07                        mov dword ptr [rbp + 7], eax
0046F2C7  89 75 0B                        mov dword ptr [rbp + 0xb], esi
0046F2CA  8B 75 7F                        mov esi, dword ptr [rbp + 0x7f]
0046F2CD  8D 14 01                        lea edx, [rcx + rax]
0046F2D0  83 E2 1F                        and edx, 0x1f
0046F2D3  8B C2                           mov eax, edx
0046F2D5  48 C1 E0 04                     shl rax, 4
0046F2D9  49 03 C0                        add rax, r8
0046F2DC  89 55 DF                        mov dword ptr [rbp - 0x21], edx
0046F2DF  4C 8B F0                        mov r14, rax
0046F2E2  48 8B 38                        mov rdi, qword ptr [rax]
0046F2E5  4C 8D BF 28 FF FF FF            lea r15, [rdi - 0xd8]
0046F2EC  41 8A C9                        mov cl, r9b
0046F2EF  41 F7 47 78 00 00 40 00         test dword ptr [r15 + 0x78], 0x400000
0046F2F7  48 8B 3F                        mov rdi, qword ptr [rdi]
0046F2FA  0F 85 A0 02 00 00               jne 0x14046f5a0
0046F300  44 8B E6                        mov r12d, esi
0046F303  45 2B A7 B4 01 00 00            sub r12d, dword ptr [r15 + 0x1b4]
0046F30A  45 85 E4                        test r12d, r12d
0046F30D  0F 8F AC 02 00 00               jg 0x14046f5bf
0046F313  84 C9                           test cl, cl
0046F315  0F 85 A4 02 00 00               jne 0x14046f5bf
0046F31B  44 8B 65 D7                     mov r12d, dword ptr [rbp - 0x29]
0046F31F  41 FF CC                        dec r12d
0046F322  44 89 65 D7                     mov dword ptr [rbp - 0x29], r12d
0046F326  49 3B FE                        cmp rdi, r14
0046F329  74 0D                           je 0x14046f338
0046F32B  45 85 ED                        test r13d, r13d
0046F32E  74 08                           je 0x14046f338
0046F330  8B 55 DF                        mov edx, dword ptr [rbp - 0x21]
0046F333  45 85 E4                        test r12d, r12d
0046F336  75 AD                           jne 0x14046f2e5
0046F338  8B 75 0B                        mov esi, dword ptr [rbp + 0xb]
0046F33B  44 89 6D E7                     mov dword ptr [rbp - 0x19], r13d
0046F33F  85 F6                           test esi, esi
0046F341  0F 85 A6 02 00 00               jne 0x14046f5ed
0046F347  0F BA 25 E9 77 B5 00 15         bt dword ptr [rip + 0xb577e9], 0x15
0046F34F  0F 83 A5 00 00 00               jae 0x14046f3fa
0046F355  0F 0D 4D C7                     prefetchw byte ptr [rbp - 0x39]
0046F359  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0046F35D  48 85 C0                        test rax, rax
0046F360  75 22                           jne 0x14046f384
0046F362  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0046F366  48 8D 45 C7                     lea rax, [rbp - 0x39]
0046F36A  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
0046F36F  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F373  48 3B C1                        cmp rax, rcx
0046F376  74 2C                           je 0x14046f3a4
0046F378  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F37C  E8 1F 87 DA FF                  call 0x140217aa0
0046F381  45 33 C9                        xor r9d, r9d
0046F384  48 8D 48 08                     lea rcx, [rax + 8]
0046F388  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
0046F38C  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
0046F390  48 8B C2                        mov rax, rdx
0046F393  48 87 01                        xchg qword ptr [rcx], rax
0046F396  32 C2                           xor al, dl
0046F398  A8 04                           test al, 4
0046F39A  74 08                           je 0x14046f3a4
0046F39C  E8 7F 88 DA FF                  call 0x140217c20
0046F3A1  45 33 C9                        xor r9d, r9d
0046F3A4  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
0046F3A8  8B 7D DB                        mov edi, dword ptr [rbp - 0x25]
0046F3AB  4D 85 F6                        test r14, r14
0046F3AE  75 7A                           jne 0x14046f42a
0046F3B0  45 85 E4                        test r12d, r12d
0046F3B3  0F 84 9A 02 00 00               je 0x14046f653
0046F3B9  45 85 ED                        test r13d, r13d
0046F3BC  0F 84 91 02 00 00               je 0x14046f653
0046F3C2  8A 4D 77                        mov cl, byte ptr [rbp + 0x77]
0046F3C5  84 C9                           test cl, cl
0046F3C7  0F 84 A1 02 00 00               je 0x14046f66e
0046F3CD  40 88 BB C3 02 00 00            mov byte ptr [rbx + 0x2c3], dil
0046F3D4  48 81 C4 88 00 00 00            add rsp, 0x88
0046F3DB  41 5F                           pop r15
0046F3DD  41 5E                           pop r14
0046F3DF  41 5D                           pop r13
0046F3E1  41 5C                           pop r12
0046F3E3  5F                              pop rdi
0046F3E4  5E                              pop rsi
0046F3E5  5B                              pop rbx
0046F3E6  5D                              pop rbp
0046F3E7  C3                              ret
0046F3E8  CC                              int3
0046F3E9  44 89 4D 03                     mov dword ptr [rbp + 3], r9d
0046F3ED  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0046F3F3  73 2C                           jae 0x14046f421
0046F3F5  E9 88 41 28 00                  jmp 0x1406f3582
0046F3FA  F0 4C 21 0B                     lock and qword ptr [rbx], r9
0046F3FE  EB A4                           jmp 0x14046f3a4
0046F400  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F404  E8 A7 8A DE FF                  call 0x140257eb0
0046F409  45 33 C9                        xor r9d, r9d
0046F40C  4C 8D 43 40                     lea r8, [rbx + 0x40]
0046F410  E9 58 FE FF FF                  jmp 0x14046f26d
0046F415  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F419  E8 92 8A DE FF                  call 0x140257eb0
0046F41E  45 33 C9                        xor r9d, r9d
0046F421  4C 8D 43 40                     lea r8, [rbx + 0x40]
0046F425  E9 D1 FD FF FF                  jmp 0x14046f1fb
0046F42A  44 8B 65 7F                     mov r12d, dword ptr [rbp + 0x7f]
0046F42E  8B 7D EF                        mov edi, dword ptr [rbp - 0x11]
0046F431  8B 5D F3                        mov ebx, dword ptr [rbp - 0xd]
0046F434  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
0046F438  49 8D B6 28 FF FF FF            lea rsi, [r14 - 0xd8]
0046F43F  44 88 4D 7F                     mov byte ptr [rbp + 0x7f], r9b
0046F443  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
0046F447  45 8B F9                        mov r15d, r9d
0046F44A  4D 8B 36                        mov r14, qword ptr [r14]
0046F44D  48 89 4D 0F                     mov qword ptr [rbp + 0xf], rcx
0046F451  F0 48 0F BA 6E 40 00            lock bts qword ptr [rsi + 0x40], 0
0046F458  73 19                           jae 0x14046f473
0046F45A  41 FF C7                        inc r15d
0046F45D  44 85 3D 48 5E B5 00            test dword ptr [rip + 0xb55e48], r15d
0046F464  74 5E                           je 0x14046f4c4
0046F466  F3 90                           pause
0046F468  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
0046F46C  48 85 C0                        test rax, rax
0046F46F  74 E0                           je 0x14046f451
0046F471  EB E7                           jmp 0x14046f45a
0046F473  44 0F BE BE C3 00 00 00         movsx r15d, byte ptr [rsi + 0xc3]
0046F47B  41 8B C4                        mov eax, r12d
0046F47E  2B 86 B4 01 00 00               sub eax, dword ptr [rsi + 0x1b4]
0046F484  85 C0                           test eax, eax
0046F486  0F 8F 7F 01 00 00               jg 0x14046f60b
0046F48C  4C 89 4E 40                     mov qword ptr [rsi + 0x40], r9
0046F490  44 38 4D 7F                     cmp byte ptr [rbp + 0x7f], r9b
0046F494  0F 85 9B 01 00 00               jne 0x14046f635
0046F49A  45 33 C0                        xor r8d, r8d
0046F49D  48 8B D6                        mov rdx, rsi
0046F4A0  49 8B CD                        mov rcx, r13
0046F4A3  E8 98 91 F2 FF                  call 0x140398640
0046F4A8  45 33 C9                        xor r9d, r9d
0046F4AB  4D 85 F6                        test r14, r14
0046F4AE  75 88                           jne 0x14046f438
0046F4B0  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
0046F4B4  8B 7D DB                        mov edi, dword ptr [rbp - 0x25]
0046F4B7  44 8B 6D E7                     mov r13d, dword ptr [rbp - 0x19]
0046F4BB  44 8B 65 D7                     mov r12d, dword ptr [rbp - 0x29]
0046F4BF  E9 EC FE FF FF                  jmp 0x14046f3b0
0046F4C4  8B 05 EE 75 B5 00               mov eax, dword ptr [rip + 0xb575ee]
0046F4CA  A8 40                           test al, 0x40
0046F4CC  74 98                           je 0x14046f466
0046F4CE  E8 BD FF E9 FF                  call 0x14030f490
0046F4D3  45 33 C9                        xor r9d, r9d
0046F4D6  84 C0                           test al, al
0046F4D8  74 8C                           je 0x14046f466
0046F4DA  41 8B CF                        mov ecx, r15d
0046F4DD  E8 7E FF E9 FF                  call 0x14030f460
0046F4E2  45 33 C9                        xor r9d, r9d
0046F4E5  EB 81                           jmp 0x14046f468
0046F4E7  0F BA 25 49 76 B5 00 15         bt dword ptr [rip + 0xb57649], 0x15
0046F4EF  0F 83 6D 40 28 00               jae 0x1406f3562
0046F4F5  0F 0D 4D C7                     prefetchw byte ptr [rbp - 0x39]
0046F4F9  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0046F4FD  48 85 C0                        test rax, rax
0046F500  0F 85 35 40 28 00               jne 0x1406f353b
0046F506  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0046F50A  48 8D 45 C7                     lea rax, [rbp - 0x39]
0046F50E  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
0046F513  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F517  48 3B C1                        cmp rax, rcx
0046F51A  0F 84 AD FE FF FF               je 0x14046f3cd
0046F520  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0046F524  E8 77 85 DA FF                  call 0x140217aa0
0046F529  45 33 C9                        xor r9d, r9d
0046F52C  E9 0A 40 28 00                  jmp 0x1406f353b
0046F531  44 39 89 50 8E 00 00            cmp dword ptr [rcx + 0x8e50], r9d
0046F538  0F 84 96 FC FF FF               je 0x14046f1d4
0046F53E  48 8B 82 D0 02 00 00            mov rax, qword ptr [rdx + 0x2d0]
0046F545  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
0046F549  48 8B 8A C8 02 00 00            mov rcx, qword ptr [rdx + 0x2c8]
0046F550  48 23 C8                        and rcx, rax
0046F553  F3 48 0F B8 C1                  popcnt rax, rcx
0046F558  85 C0                           test eax, eax
0046F55A  0F 84 74 FC FF FF               je 0x14046f1d4
0046F560  8B 0D D2 75 B5 00               mov ecx, dword ptr [rip + 0xb575d2]
0046F566  0F BA E1 1B                     bt ecx, 0x1b
0046F56A  0F 83 FB 3F 28 00               jae 0x1406f356b
0046F570  44 0F AF E8                     imul r13d, eax
0046F574  E9 F2 3F 28 00                  jmp 0x1406f356b
0046F579  8B 05 CD 76 B5 00               mov eax, dword ptr [rip + 0xb576cd]
0046F57F  89 45 EF                        mov dword ptr [rbp - 0x11], eax
0046F582  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0046F58C  C7 45 F3 0F 00 00 00            mov dword ptr [rbp - 0xd], 0xf
0046F593  8B 00                           mov eax, dword ptr [rax]
0046F595  2B 05 25 5C B5 00               sub eax, dword ptr [rip + 0xb55c25]
0046F59B  E9 0E FD FF FF                  jmp 0x14046f2ae
0046F5A0  33 D2                           xor edx, edx
0046F5A2  49 8B CF                        mov rcx, r15
0046F5A5  E8 3A 56 E9 FF                  call 0x140304be4
0046F5AA  41 3B 87 00 04 00 00            cmp eax, dword ptr [r15 + 0x400]
0046F5B1  8B 55 DF                        mov edx, dword ptr [rbp - 0x21]
0046F5B4  0F 95 C1                        setne cl
0046F5B7  45 33 C9                        xor r9d, r9d
0046F5BA  E9 41 FD FF FF                  jmp 0x14046f300
0046F5BF  44 8B C2                        mov r8d, edx
0046F5C2  48 8B CB                        mov rcx, rbx
0046F5C5  49 8B D7                        mov rdx, r15
0046F5C8  E8 E3 23 D9 FF                  call 0x1402019b0
0046F5CD  49 8B D7                        mov rdx, r15
0046F5D0  48 8D 4D F7                     lea rcx, [rbp - 9]
0046F5D4  E8 37 1D D9 FF                  call 0x140201310
0046F5D9  45 33 C9                        xor r9d, r9d
0046F5DC  45 85 E4                        test r12d, r12d
0046F5DF  0F 8E 36 FD FF FF               jle 0x14046f31b
0046F5E5  41 FF CD                        dec r13d
0046F5E8  E9 2E FD FF FF                  jmp 0x14046f31b
0046F5ED  45 85 ED                        test r13d, r13d
0046F5F0  0F 84 51 FD FF FF               je 0x14046f347
0046F5F6  8B 4D 0F                        mov ecx, dword ptr [rbp + 0xf]
0046F5F9  4C 8D 43 40                     lea r8, [rbx + 0x40]
0046F5FD  45 85 E4                        test r12d, r12d
0046F600  0F 85 B8 FC FF FF               jne 0x14046f2be
0046F606  E9 3C FD FF FF                  jmp 0x14046f347
0046F60B  44 3B FB                        cmp r15d, ebx
0046F60E  0F 8D 78 FE FF FF               jge 0x14046f48c
0046F614  4C 8B 4D 0F                     mov r9, qword ptr [rbp + 0xf]
0046F618  44 8B C3                        mov r8d, ebx
0046F61B  48 8B D6                        mov rdx, rsi
0046F61E  C6 45 7F 01                     mov byte ptr [rbp + 0x7f], 1
0046F622  33 C9                           xor ecx, ecx
0046F624  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0046F628  E8 13 94 F2 FF                  call 0x140398a40
0046F62D  45 33 C9                        xor r9d, r9d
0046F630  E9 57 FE FF FF                  jmp 0x14046f48c
0046F635  8B 05 CD 74 B5 00               mov eax, dword ptr [rip + 0xb574cd]
0046F63B  A8 01                           test al, 1
0046F63D  0F 84 57 FE FF FF               je 0x14046f49a
0046F643  41 8B D7                        mov edx, r15d
0046F646  48 8B CE                        mov rcx, rsi
0046F649  E8 1A FF 1D 00                  call 0x14064f568
0046F64E  E9 47 FE FF FF                  jmp 0x14046f49a
0046F653  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
0046F656  8A 4D 77                        mov cl, byte ptr [rbp + 0x77]
0046F659  FF C0                           inc eax
0046F65B  84 C9                           test cl, cl
0046F65D  0F 84 68 3F 28 00               je 0x1406f35cb
0046F663  83 F8 09                        cmp eax, 9
0046F666  0F 46 F8                        cmovbe edi, eax
0046F669  E9 57 FD FF FF                  jmp 0x14046f3c5
0046F66E  40 88 BB C2 02 00 00            mov byte ptr [rbx + 0x2c2], dil
0046F675  E9 5A FD FF FF                  jmp 0x14046f3d4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiScanSharedReadyThreads(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p20;

    *(unsigned __int8 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = v_xmm0;
    if (a3 == 0) goto loc_0046F1A3;
    v_r13 = (unsigned int)((*(unsigned __int8 *)(a2 + 708)) * (*(unsigned int *)(v_rip + 11886358)));
    *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)(a4 + 8);
    if (condition_is_below) goto loc_0046F254;
    *(unsigned int *)(v_rsp - 95 - 1) = 0;
    if (condition_is_above_or_equal) goto loc_0046F40C;
loc_0046F1A3:
    *(unsigned int *)(v_rsp - 95 - 37) = 1;
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11886435)));
    if (((*(unsigned int *)(v_rip + 11893131)) & (0xC000000ULL)) != 0) goto loc_0046F531;
loc_0046F1D4:
    if (condition_is_above_or_equal) goto loc_0046F3E9;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = a2;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    if (v_rsp - 95 - 57 != 0) goto loc_0046F415;
loc_0046F1FB:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & (0x7FFEULL));
    if (condition_is_not_equal) goto loc_0046F579;
    if ((v_rsp - 95 - 57) == (v_rsp - 95 - 57)) goto loc_0046F66E;
    result = KxWaitForLockChainValid(v_rsp - 95 - 57, v_rsp - 95 - 57, a2 + 64, a4);
    a4 = 0;
loc_0046F254:
    *(unsigned __int64 *)(v_rsp - 95 - 49) = a2;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    if (v_rsp - 95 - 57 != 0) goto loc_0046F400;
loc_0046F26D:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & (768));
    if (condition_is_equal) goto loc_0046F4E7;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11886100))) * (*(unsigned int *)(v_rip + 11886089)));
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11886234)));
    *(unsigned int *)(v_rsp - 95 - 13) = 11;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rip + 11886234))))) - (*(unsigned int *)(v_rip + 11886113)));
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)(a2);
loc_0046F2AE:
    *(unsigned int *)(v_rsp - 95 + 15) = (unsigned int)((unsigned __int8)(*(unsigned __int8 *)(a2 + 706)));
    *(unsigned int *)(v_rsp - 95 + 127) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 95 - 9) = 0;
loc_0046F2BE:
    *(unsigned int *)(v_rsp - 95 + 7) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 95 + 11) = (unsigned int)(v_rsi);
    a2 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 706)) + result * 1) & (31));
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    result = (result) + (a2 + 64);
    *(unsigned int *)(v_rsp - 95 - 33) = (unsigned int)(a2);
loc_0046F2E5:
    if (((*(unsigned int *)(*(unsigned __int64 *)(result) - 216 + 120)) & (0x400000ULL)) != 0) goto loc_0046F5A0;
loc_0046F300:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127))))) - (*(unsigned int *)(*(unsigned __int64 *)(result) - 216 + 436)));
    if (condition_is_greater) goto loc_0046F5BF;
    if (0 != 0) goto loc_0046F5BF;
loc_0046F31B:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 41))) - 1);
    *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)(v_r12);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result))) == result) goto loc_0046F338;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11886820))) == 0) goto loc_0046F338;
    if ((unsigned int)(v_r12) != 0) goto loc_0046F2E5;
loc_0046F338:
    *(unsigned int *)(v_rsp - 95 - 25) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11886820)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 11))) != 0) goto loc_0046F5ED;
loc_0046F347:
    if (condition_is_above_or_equal) goto loc_0046F3FA;
    if (*(unsigned __int64 *)(v_rsp - 95 - 57) != 0) goto loc_0046F384;
    if ((v_rsp - 95 - 57) == (v_rsp - 95 - 57)) goto loc_0046F3A4;
    result = KxWaitForLockChainValid(v_rsp - 95 - 57, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)), a2 + 64, a4);
    a4 = 0;
loc_0046F384:
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rsp - 95 - 49)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 - 49))));
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rsp - 95 - 49), a2 + 64, a4);
        a4 = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 9) != 0) goto loc_0046F42A;
loc_0046F3B0:
    if ((unsigned int)(v_r12) == 0) goto loc_0046F653;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11886820))) == 0) goto loc_0046F653;
loc_0046F3C5:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 + 119)) == 0) goto loc_0046F66E;
loc_0046F3CD:
    *(unsigned __int8 *)(a2 + 707) = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 37)));
loc_0046F3D4:
    v_rsp = (v_rsp) + (136);
    return result;
loc_0046F3E9:
    *(unsigned int *)(v_rsp - 95 + 3) = 0;
    if (condition_is_above_or_equal) goto loc_0046F421;
loc_0046F3FA:
    goto loc_0046F3A4;
loc_0046F400:
    result = KxWaitForLockOwnerShip(v_rsp - 95 - 57, *(unsigned __int64 *)(v_rsp - 95 - 49), a2 + 64, a4);
    a4 = 0;
loc_0046F40C:
    goto loc_0046F26D;
loc_0046F415:
    result = KxWaitForLockOwnerShip(v_rsp - 95 - 57, *(unsigned __int64 *)(v_rsp - 95 - 49), a2 + 64, a4);
    a4 = 0;
loc_0046F421:
    goto loc_0046F1FB;
loc_0046F42A:
loc_0046F438:
    *(unsigned __int8 *)(v_rsp - 95 + 127) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 72);
loc_0046F451:
    if (condition_is_above_or_equal) goto loc_0046F473;
loc_0046F45A:
    v_r15 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 11886152)) & ((unsigned int)(v_r15))) == 0) goto loc_0046F4C4;
loc_0046F466:
loc_0046F468:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 64) == 0) goto loc_0046F451;
    goto loc_0046F45A;
loc_0046F473:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127))))) - (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 436)));
    if (condition_is_greater) goto loc_0046F60B;
loc_0046F48C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 64) = 0;
    if ((*(unsigned __int8 *)(v_rsp - 95 + 127)) != 0) goto loc_0046F635;
loc_0046F49A:
    a3 = 0;
    result = KiDeferredReadyThread(*(unsigned __int64 *)(v_rsp - 95 + 103), *(unsigned __int64 *)(v_rsp - 95 - 9) - 216, a3, a4);
    a4 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9)) != 0) goto loc_0046F438;
    goto loc_0046F3B0;
loc_0046F4C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11892206)))) & (64)) == 0) goto loc_0046F466;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rsp - 95 + 103), *(unsigned __int64 *)(v_rsp - 95 - 9) - 216, a3, a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0046F466;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)))), *(unsigned __int64 *)(v_rsp - 95 - 9) - 216, a3, a4);
    a4 = 0;
    goto loc_0046F468;
loc_0046F4E7:
    if ((v_rsp - 95 - 57) == (v_rsp - 95 - 57)) goto loc_0046F3CD;
    result = KxWaitForLockChainValid(v_rsp - 95 - 57, *(unsigned __int64 *)(v_rsp - 95 - 9) - 216, a3, a4);
    a4 = 0;
loc_0046F531:
    if ((*(unsigned int *)(v_rsp - 95 - 57 + 36432)) == 0) goto loc_0046F1D4;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 712)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 720) + 80));
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 720) + 80)) == 0) goto loc_0046F1D4;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 25))) * ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 720) + 80))));
loc_0046F579:
    *(unsigned int *)(v_rsp - 95 - 17) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11892429)));
    *(unsigned int *)(v_rsp - 95 - 13) = 15;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rip + 11892429))))) - (*(unsigned int *)(v_rip + 11885605)));
    goto loc_0046F2AE;
loc_0046F5A0:
    a2 = 0;
    result = KiReadGuestSchedulerAssistPriority((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)), a2, a3, a4);
    a1 = (((unsigned int)(result)) != (*(unsigned int *)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)) + 1024))) ? 1 : 0;
    a4 = 0;
    goto loc_0046F300;
loc_0046F5BF:
    result = KiRemoveThreadFromSharedReadyQueue(*(unsigned __int64 *)(v_rsp - 95 + 111), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))), a4);
    result = KiInsertDeferredReadyList(v_rsp - 95 - 9, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))), a4);
    a4 = 0;
    if (condition_is_less_or_equal) goto loc_0046F31B;
    v_r13 = (unsigned int)((v_r13) - 1);
    goto loc_0046F31B;
loc_0046F5ED:
    if ((unsigned int)(v_r13) == 0) goto loc_0046F347;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 41))) != 0) goto loc_0046F2BE;
    goto loc_0046F347;
loc_0046F60B:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)))) >= ((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 111)))) goto loc_0046F48C;
    *(unsigned __int8 *)(v_rsp - 95 + 127) = 1;
    a1 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 37)));
    result = KiSetPriorityBoost(a1, *(unsigned __int64 *)(v_rsp - 95 - 9) - 216, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 111))), *(unsigned __int64 *)(v_rsp - 95 + 15));
    a4 = 0;
    goto loc_0046F48C;
loc_0046F635:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11891917)))) & (1)) == 0) goto loc_0046F49A;
    result = EtwTraceAntiStarvationBoost(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216, (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 - 9) - 216 + 195)))), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 111))), a4);
    goto loc_0046F49A;
loc_0046F653:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))) + 1);
    v_rdi = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 37));
    if (((unsigned int)(result)) <= 9) { v_rdi = (unsigned int)(result); }
    goto loc_0046F3C5;
loc_0046F66E:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 95 + 111) + 706) = (unsigned __int8)(v_rdi);
    goto loc_0046F3D4;
}
```

## 5. (Beta) C Style

```c
int64_t KiScanSharedReadyThreads(void *Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p20;

    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = v_xmm0;
    if (Arg3 == 0) goto loc_0046F1A3;
    local_r13 = (uint32_t)((*(uint8_t *)(arg2 + 0x2C4)) * (*(uint32_t *)(v_rip + 0xB55F16)));
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)(Arg4 + 8);
    if (condition_is_below) goto loc_0046F254;
    *(uint32_t *)(local_rsp - 0x5F - 0x1) = 0;
    if (condition_is_above_or_equal) goto loc_0046F40C;
loc_0046F1A3:
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = 1;
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB55F63)));
    if (((*(uint32_t *)(v_rip + 0xB5798B)) & (0xC000000ULL)) != 0) goto loc_0046F531;
loc_0046F1D4:
    if (condition_is_above_or_equal) goto loc_0046F3E9;
    *(void **)(local_rsp - 0x5F - 0x31) = Arg2;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    if (local_rsp - 95 - 57 != 0) goto loc_0046F415;
loc_0046F1FB:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x8))) & (0x7FFEULL));
    if (condition_is_not_equal) goto loc_0046F579;
    if ((local_rsp - 95 - 57) == (local_rsp - 95 - 57)) goto loc_0046F66E;
    result = KxWaitForLockChainValid(local_rsp - 95 - 57, local_rsp - 95 - 57, Arg2 + 64, Arg4);
    Arg4 = 0;
loc_0046F254:
    *(void **)(local_rsp - 0x5F - 0x31) = Arg2;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    if (local_rsp - 95 - 57 != 0) goto loc_0046F400;
loc_0046F26D:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x8))) & (768));
    if (condition_is_equal) goto loc_0046F4E7;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB55E14))) * (*(uint32_t *)(v_rip + 0xB55E09)));
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB55E9A)));
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = 11;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xB55E9A))))) - (*(uint32_t *)(v_rip + 0xB55E21)));
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)(Arg2);
loc_0046F2AE:
    *(uint32_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)((uint8_t)(*(uint8_t *)(arg2 + 0x2C2)));
    *(uint32_t *)(local_rsp - 0x5F + 0x7F) = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = 0;
loc_0046F2BE:
    *(uint32_t *)(local_rsp - 0x5F + 0x7) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x5F + 0xB) = (uint32_t)(local_rsi);
    Arg2 = (uint32_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x2C2)) + result * 1) & (31));
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    result = (result) + (Arg2 + 64);
    *(uint32_t *)(local_rsp - 0x5F - 0x21) = (uint32_t)(Arg2);
loc_0046F2E5:
    if (((*(uint32_t *)(*(uint64_t *)(result) - 0xD8 + 0x78)) & (0x400000ULL)) != 0) goto loc_0046F5A0;
loc_0046F300:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F))))) - (*(uint32_t *)(*(uint64_t *)(result) - 0xD8 + 0x1B4)));
    if (condition_is_greater) goto loc_0046F5BF;
    if (0 != 0) goto loc_0046F5BF;
loc_0046F31B:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x29))) - 1);
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)(local_r12);
    if ((*(uint64_t *)(*(uint64_t *)(result))) == result) goto loc_0046F338;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB560E4))) == 0) goto loc_0046F338;
    if ((uint32_t)(local_r12) != 0) goto loc_0046F2E5;
loc_0046F338:
    *(uint32_t *)(local_rsp - 0x5F - 0x19) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB560E4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0xB))) != 0) goto loc_0046F5ED;
loc_0046F347:
    if (condition_is_above_or_equal) goto loc_0046F3FA;
    if (*(uint64_t *)(local_rsp - 0x5F - 0x39) != 0) goto loc_0046F384;
    if ((local_rsp - 95 - 57) == (local_rsp - 95 - 57)) goto loc_0046F3A4;
    result = KxWaitForLockChainValid(local_rsp - 95 - 57, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)), Arg2 + 64, Arg4);
    Arg4 = 0;
loc_0046F384:
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rsp - 0x5F - 0x31)) ^ ((uint8_t)(*(uint64_t *)(local_rsp - 0x5F - 0x31))));
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rsp - 0x5F - 0x31), Arg2 + 64, Arg4);
        Arg4 = 0;
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x9) != 0) goto loc_0046F42A;
loc_0046F3B0:
    if ((uint32_t)(local_r12) == 0) goto loc_0046F653;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB560E4))) == 0) goto loc_0046F653;
loc_0046F3C5:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x5F + 0x77)) == 0) goto loc_0046F66E;
loc_0046F3CD:
    *(uint8_t *)(arg2 + 0x2C3) = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x25)));
loc_0046F3D4:
    local_rsp = (local_rsp) + (136);
    return result;
loc_0046F3E9:
    *(uint32_t *)(local_rsp - 0x5F + 0x3) = 0;
    if (condition_is_above_or_equal) goto loc_0046F421;
loc_0046F3FA:
    goto loc_0046F3A4;
loc_0046F400:
    result = KxWaitForLockOwnerShip(local_rsp - 95 - 57, *(uint64_t *)(local_rsp - 0x5F - 0x31), Arg2 + 64, Arg4);
    Arg4 = 0;
loc_0046F40C:
    goto loc_0046F26D;
loc_0046F415:
    result = KxWaitForLockOwnerShip(local_rsp - 95 - 57, *(uint64_t *)(local_rsp - 0x5F - 0x31), Arg2 + 64, Arg4);
    Arg4 = 0;
loc_0046F421:
    goto loc_0046F1FB;
loc_0046F42A:
loc_0046F438:
    *(uint8_t *)(local_rsp - 0x5F + 0x7F) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x48);
loc_0046F451:
    if (condition_is_above_or_equal) goto loc_0046F473;
loc_0046F45A:
    local_r15 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xB55E48)) & ((uint32_t)(local_r15))) == 0) goto loc_0046F4C4;
loc_0046F466:
loc_0046F468:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x40) == 0) goto loc_0046F451;
    goto loc_0046F45A;
loc_0046F473:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F))))) - (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x1B4)));
    if (condition_is_greater) goto loc_0046F60B;
loc_0046F48C:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x40) = 0;
    if ((*(uint8_t *)(local_rsp - 0x5F + 0x7F)) != 0) goto loc_0046F635;
loc_0046F49A:
    Arg3 = 0;
    result = KiDeferredReadyThread(*(uint64_t *)(local_rsp - 0x5F + 0x67), *(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, Arg3, Arg4);
    Arg4 = 0;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9)) != 0) goto loc_0046F438;
    goto loc_0046F3B0;
loc_0046F4C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB575EE)))) & (64)) == 0) goto loc_0046F466;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(local_rsp - 0x5F + 0x67), *(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, Arg3, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_0046F466;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)))), *(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, Arg3, Arg4);
    Arg4 = 0;
    goto loc_0046F468;
loc_0046F4E7:
    if ((local_rsp - 95 - 57) == (local_rsp - 95 - 57)) goto loc_0046F3CD;
    result = KxWaitForLockChainValid(local_rsp - 95 - 57, *(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, Arg3, Arg4);
    Arg4 = 0;
loc_0046F531:
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x39 + 0x8E50)) == 0) goto loc_0046F1D4;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x2C8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x2D0) + 0x50));
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x2D0) + 0x50)) == 0) goto loc_0046F1D4;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x19))) * ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0x2D0) + 0x50))));
loc_0046F579:
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB576CD)));
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = 15;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xB576CD))))) - (*(uint32_t *)(v_rip + 0xB55C25)));
    goto loc_0046F2AE;
loc_0046F5A0:
    Arg2 = 0;
    result = KiReadGuestSchedulerAssistPriority((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)), Arg2, Arg3, Arg4);
    Arg1 = (((uint32_t)(result)) != (*(uint32_t *)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)) + 0x400))) ? 1 : 0;
    Arg4 = 0;
    goto loc_0046F300;
loc_0046F5BF:
    result = KiRemoveThreadFromSharedReadyQueue(*(uint64_t *)(local_rsp - 0x5F + 0x6F), (int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))), Arg4);
    result = KiInsertDeferredReadyList(local_rsp - 95 - 9, (int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))), Arg4);
    Arg4 = 0;
    if (condition_is_less_or_equal) goto loc_0046F31B;
    local_r13 = (uint32_t)((local_r13) - 1);
    goto loc_0046F31B;
loc_0046F5ED:
    if ((uint32_t)(local_r13) == 0) goto loc_0046F347;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x29))) != 0) goto loc_0046F2BE;
    goto loc_0046F347;
loc_0046F60B:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)))) >= ((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x6F)))) goto loc_0046F48C;
    *(uint8_t *)(local_rsp - 0x5F + 0x7F) = 1;
    Arg1 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x25)));
    result = KiSetPriorityBoost(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x6F))), *(uint64_t *)(local_rsp - 0x5F + 0xF));
    Arg4 = 0;
    goto loc_0046F48C;
loc_0046F635:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB574CD)))) & (1)) == 0) goto loc_0046F49A;
    result = EtwTraceAntiStarvationBoost(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 216, (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x9) - 0xD8 + 0xC3)))), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x6F))), Arg4);
    goto loc_0046F49A;
loc_0046F653:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))) + 1);
    local_rdi = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x25));
    if (((uint32_t)(result)) <= 9) { local_rdi = (uint32_t)(result); }
    goto loc_0046F3C5;
loc_0046F66E:
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x6F) + 0x2C2) = (uint8_t)(local_rdi);
    goto loc_0046F3D4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8E50` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x2C2` | `8` | `R` |
| `Arg2` | `+ 0x2C3` | `8` | `R` |
| `Arg2` | `+ 0x2C4` | `8` | `R` |
| `Arg2` | `+ 0x2C8` | `64` | `R` |
| `Arg2` | `+ 0x2D0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046F120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
