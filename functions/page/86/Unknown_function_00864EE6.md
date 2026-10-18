# sub_00864EE6

- RVA: `0x00864EE6`–`0x008653DB` (길이 `1,269` bytes)
- VA: `0x0000000140864EE6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BA6C`
- 디코드: `325`개 명령, `1,269/1,269` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00864F4B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00864F79` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00864F92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00864FAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00864FC0` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00865008` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00865123` → [PspRemoveQuotaBlock](../9D/PspRemoveQuotaBlock_function_009DAA00.md) (function, `0x009DAA00`)
- `0x0086512D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086515B` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x0086518C` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x008651BD` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x008651EE` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x008652F6` → [PspRemoveQuotaBlock](../9D/PspRemoveQuotaBlock_function_009DAA00.md) (function, `0x009DAA00`)
- `0x00865300` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086532E` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x00865362` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x00865393` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x008653C7` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x008653D1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00864FF5` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00865028` → RVA `0x00FC7350` (`ALMOSTRO`; read)
- `0x00865063` → RVA `0x00FC7358` (`ALMOSTRO`; read)
- `0x008650A2` → RVA `0x00FC7360` (`ALMOSTRO`; read)
- `0x008650E1` → RVA `0x00FC7368` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00864F4B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00864F79` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00864F92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00864FAF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00864FC0` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00865008` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0086512D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086515B` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x0086518C` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x008651BD` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x008651EE` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x00865300` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086532E` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x00865362` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x00865393` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x008653C7` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`PAGE` → `.text`)
  - `0x008653D1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **17**
  - `0x00864EF2` → [sub_00864C3A + 0x104](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F0B` → [sub_00864C3A + 0x35](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F62` → [sub_00864C3A + 0x80](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F73` → [sub_00864C3A + 0x80](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F7E` → [sub_00864C3A + 0x80](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F8A` → [sub_00864C3A + 0x173](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864F9B` → [sub_00864C3A + 0x173](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864FA7` → [sub_00864C3A + 0x17C](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864FB8` → [sub_00864C3A + 0x17C](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864FCF` → [sub_00864C3A + 0x100](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00864FE8` → [sub_00864E32 + 0x74](Unknown_function_00864E32.md) (`tail-transfer`)
  - `0x00865011` → [sub_00864C3A + 0x15C](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x0086501B` → [sub_00864C3A + 0x19A](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00865023` → [sub_00864E32 + 0x50](Unknown_function_00864E32.md) (`tail-transfer`)
  - `0x00865132` → [sub_00864C3A + 0x155](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x00865305` → [sub_00864C3A + 0xFC](Unknown_function_00864C3A.md) (`tail-transfer`)
  - `0x008653D6` → [sub_00864E32 + 0x79](Unknown_function_00864E32.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00864EE6  8B 4D 68                        mov ecx, dword ptr [rbp + 0x68]
00864EE9  41 BF FF FF FF FF               mov r15d, 0xffffffff
00864EEF  8B 45 6C                        mov eax, dword ptr [rbp + 0x6c]
00864EF2  E9 47 FE FF FF                  jmp 0x140864d3e
00864EF7  48 8B C2                        mov rax, rdx
00864EFA  4C 8B EB                        mov r13, rbx
00864EFD  83 E0 3F                        and eax, 0x3f
00864F00  0F B6 84 28 80 FF F0 00         movzx eax, byte ptr [rax + rbp + 0xf0ff80]
00864F08  4C 2B E8                        sub r13, rax
00864F0B  E9 5F FD FF FF                  jmp 0x140864c6f
00864F10  48 89 08                        mov qword ptr [rax], rcx
00864F13  4C 8D B5 B8 00 00 00            lea r14, [rbp + 0xb8]
00864F1A  48 89 41 08                     mov qword ptr [rcx + 8], rax
00864F1E  41 0F 0D 0E                     prefetchw byte ptr [r14]
00864F22  49 8B 06                        mov rax, qword ptr [r14]
00864F25  48 8B C8                        mov rcx, rax
00864F28  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00864F2C  48 83 F9 10                     cmp rcx, 0x10
00864F30  B9 00 00 00 00                  mov ecx, 0
00864F35  48 8D 50 F0                     lea rdx, [rax - 0x10]
00864F39  48 0F 46 D1                     cmovbe rdx, rcx
00864F3D  A8 02                           test al, 2
00864F3F  75 7C                           jne 0x140864fbd
00864F41  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
00864F46  75 75                           jne 0x140864fbd
00864F48  49 8B CE                        mov rcx, r14
00864F4B  E8 B0 C6 A7 FF                  call 0x1402e1600
00864F50  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00864F59  90                              nop
00864F5A  66 83 81 E6 01 00 00 01         add word ptr [rcx + 0x1e6], 1
00864F62  0F 85 52 FD FF FF               jne 0x140864cba
00864F68  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
00864F6F  90                              nop
00864F70  48 39 00                        cmp qword ptr [rax], rax
00864F73  0F 84 41 FD FF FF               je 0x140864cba
00864F79  E8 02 DD A7 FF                  call 0x1402e2c80
00864F7E  E9 37 FD FF FF                  jmp 0x140864cba
00864F83  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00864F87  48 85 C9                        test rcx, rcx
00864F8A  0F 84 1D FE FF FF               je 0x140864dad
00864F90  33 D2                           xor edx, edx
00864F92  E8 D9 D8 31 00                  call 0x140b82870
00864F97  4D 89 7E 10                     mov qword ptr [r14 + 0x10], r15
00864F9B  E9 0D FE FF FF                  jmp 0x140864dad
00864FA0  49 8B 4D 00                     mov rcx, qword ptr [r13]
00864FA4  48 85 C9                        test rcx, rcx
00864FA7  0F 84 09 FE FF FF               je 0x140864db6
00864FAD  33 D2                           xor edx, edx
00864FAF  E8 BC D8 31 00                  call 0x140b82870
00864FB4  4D 89 7D 00                     mov qword ptr [r13], r15
00864FB8  E9 F9 FD FF FF                  jmp 0x140864db6
00864FBD  49 8B CE                        mov rcx, r14
00864FC0  E8 0B E9 9F FF                  call 0x1402638d0
00864FC5  EB 81                           jmp 0x140864f48
00864FC7  41 BF FF FF FF FF               mov r15d, 0xffffffff
00864FCD  8B C8                           mov ecx, eax
00864FCF  E9 66 FD FF FF                  jmp 0x140864d3a
00864FD4  FF 41 20                        inc dword ptr [rcx + 0x20]
00864FD7  49 8B 88 48 08 00 00            mov rcx, qword ptr [r8 + 0x848]
00864FDE  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00864FE1  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00864FE5  66 39 01                        cmp word ptr [rcx], ax
00864FE8  0F 82 B8 FE FF FF               jb 0x140864ea6
00864FEE  FF 41 20                        inc dword ptr [rcx + 0x20]
00864FF1  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00864FF5  48 8D 0D 54 D8 31 00            lea rcx, [rip + 0x31d854]
00864FFC  48 3B C1                        cmp rax, rcx
00864FFF  48 8B CA                        mov rcx, rdx
00865002  0F 85 C9 03 00 00               jne 0x1408653d1
00865008  E8 43 D8 31 00                  call 0x140b82850
0086500D  4C 89 7B 20                     mov qword ptr [rbx + 0x20], r15
00865011  E9 80 FD FF FF                  jmp 0x140864d96
00865016  BA 4F 62 6A 54                  mov edx, 0x546a624f
0086501B  E9 B4 FD FF FF                  jmp 0x140864dd4
00865020  45 33 FF                        xor r15d, r15d
00865023  E9 5A FE FF FF                  jmp 0x140864e82
00865028  0F B6 05 21 23 76 00            movzx eax, byte ptr [rip + 0x762321]
0086502F  45 33 FF                        xor r15d, r15d
00865032  24 03                           and al, 3
00865034  3C 01                           cmp al, 1
00865036  75 2B                           jne 0x140865063
00865038  49 8B 56 50                     mov rdx, qword ptr [r14 + 0x50]
0086503C  45 8B CF                        mov r9d, r15d
0086503F  4D 8B 46 40                     mov r8, qword ptr [r14 + 0x40]
00865043  48 85 D2                        test rdx, rdx
00865046  49 8B 4E 48                     mov rcx, qword ptr [r14 + 0x48]
0086504A  41 0F 95 C1                     setne r9b
0086504E  49 03 C8                        add rcx, r8
00865051  0F 85 E0 00 00 00               jne 0x140865137
00865057  45 8B C7                        mov r8d, r15d
0086505A  48 85 D2                        test rdx, rdx
0086505D  0F 85 F3 00 00 00               jne 0x140865156
00865063  0F B6 05 EE 22 76 00            movzx eax, byte ptr [rip + 0x7622ee]
0086506A  49 8D 96 80 00 00 00            lea rdx, [r14 + 0x80]
00865071  24 03                           and al, 3
00865073  3C 01                           cmp al, 1
00865075  75 2B                           jne 0x1408650a2
00865077  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
0086507B  45 8B D7                        mov r10d, r15d
0086507E  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
00865082  4D 85 C9                        test r9, r9
00865085  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
00865089  41 0F 95 C2                     setne r10b
0086508D  49 03 C8                        add rcx, r8
00865090  0F 85 CF 00 00 00               jne 0x140865165
00865096  4D 8B C7                        mov r8, r15
00865099  4D 85 C9                        test r9, r9
0086509C  0F 85 E2 00 00 00               jne 0x140865184
008650A2  0F B6 05 B7 22 76 00            movzx eax, byte ptr [rip + 0x7622b7]
008650A9  49 8D 96 00 01 00 00            lea rdx, [r14 + 0x100]
008650B0  24 03                           and al, 3
008650B2  3C 01                           cmp al, 1
008650B4  75 2B                           jne 0x1408650e1
008650B6  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
008650BA  45 8B D7                        mov r10d, r15d
008650BD  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
008650C1  4D 85 C9                        test r9, r9
008650C4  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
008650C8  41 0F 95 C2                     setne r10b
008650CC  49 03 C8                        add rcx, r8
008650CF  0F 85 C1 00 00 00               jne 0x140865196
008650D5  4D 8B C7                        mov r8, r15
008650D8  4D 85 C9                        test r9, r9
008650DB  0F 85 D4 00 00 00               jne 0x1408651b5
008650E1  0F B6 05 80 22 76 00            movzx eax, byte ptr [rip + 0x762280]
008650E8  49 8D 96 80 01 00 00            lea rdx, [r14 + 0x180]
008650EF  24 03                           and al, 3
008650F1  3C 01                           cmp al, 1
008650F3  75 2B                           jne 0x140865120
008650F5  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
008650F9  45 8B D7                        mov r10d, r15d
008650FC  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
00865100  4D 85 C9                        test r9, r9
00865103  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
00865107  41 0F 95 C2                     setne r10b
0086510B  49 03 C8                        add rcx, r8
0086510E  0F 85 B3 00 00 00               jne 0x1408651c7
00865114  4D 8B C7                        mov r8, r15
00865117  4D 85 C9                        test r9, r9
0086511A  0F 85 C6 00 00 00               jne 0x1408651e6
00865120  49 8B CE                        mov rcx, r14
00865123  E8 D8 58 17 00                  call 0x1409daa00
00865128  33 D2                           xor edx, edx
0086512A  49 8B CE                        mov rcx, r14
0086512D  E8 3E D7 31 00                  call 0x140b82870
00865132  E9 58 FC FF FF                  jmp 0x140864d8f
00865137  48 85 D2                        test rdx, rdx
0086513A  74 11                           je 0x14086514d
0086513C  4D 8B C7                        mov r8, r15
0086513F  49 8B C7                        mov rax, r15
00865142  4D 87 46 48                     xchg qword ptr [r14 + 0x48], r8
00865146  49 87 46 40                     xchg qword ptr [r14 + 0x40], rax
0086514A  4C 03 C0                        add r8, rax
0086514D  4D 85 C0                        test r8, r8
00865150  0F 84 04 FF FF FF               je 0x14086505a
00865156  49 8B D6                        mov rdx, r14
00865159  33 C9                           xor ecx, ecx
0086515B  E8 64 AE B2 FF                  call 0x14038ffc4
00865160  E9 FE FE FF FF                  jmp 0x140865063
00865165  4D 85 C9                        test r9, r9
00865168  74 11                           je 0x14086517b
0086516A  4D 8B C7                        mov r8, r15
0086516D  49 8B C7                        mov rax, r15
00865170  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
00865174  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
00865178  4C 03 C0                        add r8, rax
0086517B  4D 85 C0                        test r8, r8
0086517E  0F 84 15 FF FF FF               je 0x140865099
00865184  45 8B CA                        mov r9d, r10d
00865187  B9 01 00 00 00                  mov ecx, 1
0086518C  E8 33 AE B2 FF                  call 0x14038ffc4
00865191  E9 0C FF FF FF                  jmp 0x1408650a2
00865196  4D 85 C9                        test r9, r9
00865199  74 11                           je 0x1408651ac
0086519B  4D 8B C7                        mov r8, r15
0086519E  49 8B C7                        mov rax, r15
008651A1  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
008651A5  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
008651A9  4C 03 C0                        add r8, rax
008651AC  4D 85 C0                        test r8, r8
008651AF  0F 84 23 FF FF FF               je 0x1408650d8
008651B5  45 8B CA                        mov r9d, r10d
008651B8  B9 02 00 00 00                  mov ecx, 2
008651BD  E8 02 AE B2 FF                  call 0x14038ffc4
008651C2  E9 1A FF FF FF                  jmp 0x1408650e1
008651C7  4D 85 C9                        test r9, r9
008651CA  74 11                           je 0x1408651dd
008651CC  4D 8B C7                        mov r8, r15
008651CF  49 8B C7                        mov rax, r15
008651D2  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
008651D6  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
008651DA  4C 03 C0                        add r8, rax
008651DD  4D 85 C0                        test r8, r8
008651E0  0F 84 31 FF FF FF               je 0x140865117
008651E6  45 8B CA                        mov r9d, r10d
008651E9  B9 03 00 00 00                  mov ecx, 3
008651EE  E8 D1 AD B2 FF                  call 0x14038ffc4
008651F3  E9 28 FF FF FF                  jmp 0x140865120
008651F8  0F B6 05 51 21 76 00            movzx eax, byte ptr [rip + 0x762151]
008651FF  45 33 DB                        xor r11d, r11d
00865202  24 03                           and al, 3
00865204  3C 01                           cmp al, 1
00865206  75 2B                           jne 0x140865233
00865208  49 8B 56 50                     mov rdx, qword ptr [r14 + 0x50]
0086520C  45 8B CB                        mov r9d, r11d
0086520F  4D 8B 46 40                     mov r8, qword ptr [r14 + 0x40]
00865213  48 85 D2                        test rdx, rdx
00865216  49 8B 4E 48                     mov rcx, qword ptr [r14 + 0x48]
0086521A  41 0F 95 C1                     setne r9b
0086521E  49 03 C8                        add rcx, r8
00865221  0F 85 E3 00 00 00               jne 0x14086530a
00865227  45 8B C3                        mov r8d, r11d
0086522A  48 85 D2                        test rdx, rdx
0086522D  0F 85 F6 00 00 00               jne 0x140865329
00865233  0F B6 05 1E 21 76 00            movzx eax, byte ptr [rip + 0x76211e]
0086523A  49 8D 96 80 00 00 00            lea rdx, [r14 + 0x80]
00865241  24 03                           and al, 3
00865243  3C 01                           cmp al, 1
00865245  75 2B                           jne 0x140865272
00865247  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
0086524B  45 8B D3                        mov r10d, r11d
0086524E  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
00865252  4D 85 C9                        test r9, r9
00865255  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
00865259  41 0F 95 C2                     setne r10b
0086525D  49 03 C8                        add rcx, r8
00865260  0F 85 D5 00 00 00               jne 0x14086533b
00865266  4D 8B C3                        mov r8, r11
00865269  4D 85 C9                        test r9, r9
0086526C  0F 85 E8 00 00 00               jne 0x14086535a
00865272  0F B6 05 E7 20 76 00            movzx eax, byte ptr [rip + 0x7620e7]
00865279  49 8D 96 00 01 00 00            lea rdx, [r14 + 0x100]
00865280  24 03                           and al, 3
00865282  45 33 DB                        xor r11d, r11d
00865285  3C 01                           cmp al, 1
00865287  75 2B                           jne 0x1408652b4
00865289  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
0086528D  45 8B D3                        mov r10d, r11d
00865290  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
00865294  4D 85 C9                        test r9, r9
00865297  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
0086529B  41 0F 95 C2                     setne r10b
0086529F  49 03 C8                        add rcx, r8
008652A2  0F 85 C4 00 00 00               jne 0x14086536c
008652A8  45 8B C3                        mov r8d, r11d
008652AB  4D 85 C9                        test r9, r9
008652AE  0F 85 D7 00 00 00               jne 0x14086538b
008652B4  0F B6 05 AD 20 76 00            movzx eax, byte ptr [rip + 0x7620ad]
008652BB  49 8D 96 80 01 00 00            lea rdx, [r14 + 0x180]
008652C2  24 03                           and al, 3
008652C4  3C 01                           cmp al, 1
008652C6  75 2B                           jne 0x1408652f3
008652C8  4C 8B 4A 50                     mov r9, qword ptr [rdx + 0x50]
008652CC  45 8B D3                        mov r10d, r11d
008652CF  4C 8B 42 40                     mov r8, qword ptr [rdx + 0x40]
008652D3  4D 85 C9                        test r9, r9
008652D6  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
008652DA  41 0F 95 C2                     setne r10b
008652DE  49 03 C8                        add rcx, r8
008652E1  0F 85 B9 00 00 00               jne 0x1408653a0
008652E7  4D 8B C3                        mov r8, r11
008652EA  4D 85 C9                        test r9, r9
008652ED  0F 85 CC 00 00 00               jne 0x1408653bf
008652F3  49 8B CE                        mov rcx, r14
008652F6  E8 05 57 17 00                  call 0x1409daa00
008652FB  33 D2                           xor edx, edx
008652FD  49 8B CE                        mov rcx, r14
00865300  E8 6B D5 31 00                  call 0x140b82870
00865305  E9 2C FA FF FF                  jmp 0x140864d36
0086530A  48 85 D2                        test rdx, rdx
0086530D  74 11                           je 0x140865320
0086530F  4D 8B C3                        mov r8, r11
00865312  49 8B C3                        mov rax, r11
00865315  4D 87 46 48                     xchg qword ptr [r14 + 0x48], r8
00865319  49 87 46 40                     xchg qword ptr [r14 + 0x40], rax
0086531D  4C 03 C0                        add r8, rax
00865320  4D 85 C0                        test r8, r8
00865323  0F 84 01 FF FF FF               je 0x14086522a
00865329  49 8B D6                        mov rdx, r14
0086532C  33 C9                           xor ecx, ecx
0086532E  E8 91 AC B2 FF                  call 0x14038ffc4
00865333  45 33 DB                        xor r11d, r11d
00865336  E9 F8 FE FF FF                  jmp 0x140865233
0086533B  4D 85 C9                        test r9, r9
0086533E  74 11                           je 0x140865351
00865340  4D 8B C3                        mov r8, r11
00865343  49 8B C3                        mov rax, r11
00865346  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
0086534A  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
0086534E  4C 03 C0                        add r8, rax
00865351  4D 85 C0                        test r8, r8
00865354  0F 84 0F FF FF FF               je 0x140865269
0086535A  45 8B CA                        mov r9d, r10d
0086535D  B9 01 00 00 00                  mov ecx, 1
00865362  E8 5D AC B2 FF                  call 0x14038ffc4
00865367  E9 06 FF FF FF                  jmp 0x140865272
0086536C  4D 85 C9                        test r9, r9
0086536F  74 11                           je 0x140865382
00865371  4D 8B C3                        mov r8, r11
00865374  49 8B C3                        mov rax, r11
00865377  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
0086537B  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
0086537F  4C 03 C0                        add r8, rax
00865382  4D 85 C0                        test r8, r8
00865385  0F 84 20 FF FF FF               je 0x1408652ab
0086538B  45 8B CA                        mov r9d, r10d
0086538E  B9 02 00 00 00                  mov ecx, 2
00865393  E8 2C AC B2 FF                  call 0x14038ffc4
00865398  45 33 DB                        xor r11d, r11d
0086539B  E9 14 FF FF FF                  jmp 0x1408652b4
008653A0  4D 85 C9                        test r9, r9
008653A3  74 11                           je 0x1408653b6
008653A5  4D 8B C3                        mov r8, r11
008653A8  49 8B C3                        mov rax, r11
008653AB  4C 87 42 48                     xchg qword ptr [rdx + 0x48], r8
008653AF  48 87 42 40                     xchg qword ptr [rdx + 0x40], rax
008653B3  4C 03 C0                        add r8, rax
008653B6  4D 85 C0                        test r8, r8
008653B9  0F 84 2B FF FF FF               je 0x1408652ea
008653BF  45 8B CA                        mov r9d, r10d
008653C2  B9 03 00 00 00                  mov ecx, 3
008653C7  E8 F8 AB B2 FF                  call 0x14038ffc4
008653CC  E9 22 FF FF FF                  jmp 0x1408652f3
008653D1  E8 FA 56 E5 FF                  call 0x1406baad0
008653D6  E9 D0 FA FF FF                  jmp 0x140864eab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00864EE6(__int64 a1, __int64 a2, __int64 a3)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_00864EE6(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00864EE6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
