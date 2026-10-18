# ExpWorkQueueManagerThread

- RVA: `0x00AF6D60`–`0x00AF7318` (길이 `1,464` bytes)
- VA: `0x0000000140AF6D60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5544`
- 디코드: `371`개 명령, `1,464/1,464` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AF6DA7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF6DCB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AF6DE3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AF6DFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF6E1A` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x00AF6E4E` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x00AF6EAF` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x00AF6F34` → [KeTimeOutQueueWaiters](../../text/34/KeTimeOutQueueWaiters_function_0034FB58.md) (function, `0x0034FB58`)
- `0x00AF6FB0` → [ExpNewThreadNecessary](../../text/33/ExpNewThreadNecessary_function_0033FAF0.md) (function, `0x0033FAF0`)
- `0x00AF6FF8` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00AF700C` → [ExpCreateWorkerThread](../9E/ExpCreateWorkerThread_function_009ECEFC.md) (function, `0x009ECEFC`)
- `0x00AF709D` → [ExpPartitionCreatePoolDelayed](ExpPartitionCreatePoolDelayed_function_00AF6B38.md) (function, `0x00AF6B38`)
- `0x00AF70E0` → [ExpNewThreadNecessary](../../text/33/ExpNewThreadNecessary_function_0033FAF0.md) (function, `0x0033FAF0`)
- `0x00AF70F0` → [ExpCreateWorkerThread](../9E/ExpCreateWorkerThread_function_009ECEFC.md) (function, `0x009ECEFC`)
- `0x00AF71CE` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (function, `0x0022FFD0`)
- `0x00AF71ED` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF7201` → [KeQueryNodeActiveAffinityEx](../../text/25/KeQueryNodeActiveAffinityEx_function_00256740.md) (function, `0x00256740`)
- `0x00AF7217` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (function, `0x00305230`)
- `0x00AF7228` → [KeSetUserAffinityThread](../../text/2C/KeSetUserAffinityThread_function_002CFA2C.md) (function, `0x002CFA2C`)
- `0x00AF7273` → [ExpGetNodeSubQueueConcurrencyCount](../../text/65/ExpGetNodeSubQueueConcurrencyCount_function_0065A534.md) (function, `0x0065A534`)
- `0x00AF7286` → [KeSetMaximumCountPriQueue](../../text/5C/KeSetMaximumCountPriQueue_function_005CA9C4.md) (function, `0x005CA9C4`)
- `0x00AF72B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF72C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF72D7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AF7312` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AF6D86` → RVA `0x00E0A740` (`.data`; read)
- `0x00AF6E1F` → RVA `0x00E0EBCC` (`.data`; read)
- `0x00AF6EEC` → RVA `0x00EFAA0C` (`.data`; read)
- `0x00AF6FBB` → RVA `0x00EFAA90` (`.data`; read)
- `0x00AF6FE0` → RVA `0x007CF7D0` (`ExpIoPoolDeadlockWorker`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00AF6DA7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF6DCB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AF6DE3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AF6DFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF6E1A` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (`PAGE` → `.text`)
  - `0x00AF6E4E` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (`PAGE` → `.text`)
  - `0x00AF6EAF` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (`PAGE` → `.text`)
  - `0x00AF6F34` → [KeTimeOutQueueWaiters](../../text/34/KeTimeOutQueueWaiters_function_0034FB58.md) (`PAGE` → `.text`)
  - `0x00AF6FB0` → [ExpNewThreadNecessary](../../text/33/ExpNewThreadNecessary_function_0033FAF0.md) (`PAGE` → `.text`)
  - `0x00AF6FF8` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
  - `0x00AF70E0` → [ExpNewThreadNecessary](../../text/33/ExpNewThreadNecessary_function_0033FAF0.md) (`PAGE` → `.text`)
  - `0x00AF71CE` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (`PAGE` → `.text`)
  - `0x00AF71ED` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF7201` → [KeQueryNodeActiveAffinityEx](../../text/25/KeQueryNodeActiveAffinityEx_function_00256740.md) (`PAGE` → `.text`)
  - `0x00AF7217` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (`PAGE` → `.text`)
  - `0x00AF7228` → [KeSetUserAffinityThread](../../text/2C/KeSetUserAffinityThread_function_002CFA2C.md) (`PAGE` → `.text`)
  - `0x00AF7273` → [ExpGetNodeSubQueueConcurrencyCount](../../text/65/ExpGetNodeSubQueueConcurrencyCount_function_0065A534.md) (`PAGE` → `.text`)
  - `0x00AF7286` → [KeSetMaximumCountPriQueue](../../text/5C/KeSetMaximumCountPriQueue_function_005CA9C4.md) (`PAGE` → `.text`)
  - `0x00AF72B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF72C8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF72D7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00AF7312` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF6D60  48 8B C4                        mov rax, rsp
00AF6D63  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00AF6D67  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00AF6D6B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00AF6D6F  55                              push rbp
00AF6D70  41 54                           push r12
00AF6D72  41 55                           push r13
00AF6D74  41 56                           push r14
00AF6D76  41 57                           push r15
00AF6D78  48 8D A8 48 FF FF FF            lea rbp, [rax - 0xb8]
00AF6D7F  48 81 EC 90 01 00 00            sub rsp, 0x190
00AF6D86  48 8B 05 B3 39 31 00            mov rax, qword ptr [rip + 0x3139b3]
00AF6D8D  48 33 C4                        xor rax, rsp
00AF6D90  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00AF6D97  48 8B D9                        mov rbx, rcx
00AF6D9A  33 D2                           xor edx, edx
00AF6D9C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF6DA1  41 B8 08 01 00 00               mov r8d, 0x108
00AF6DA7  E8 94 FE BC FF                  call 0x1406c6c40
00AF6DAC  BE 01 00 00 00                  mov esi, 1
00AF6DB1  BF 45 78 57 6C                  mov edi, 0x6c577845
00AF6DB6  44 8B C7                        mov r8d, edi
00AF6DB9  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
00AF6DBE  45 33 E4                        xor r12d, r12d
00AF6DC1  44 8D 76 3F                     lea r14d, [rsi + 0x3f]
00AF6DC5  41 8B CE                        mov ecx, r14d
00AF6DC8  8D 56 0F                        lea edx, [rsi + 0xf]
00AF6DCB  E8 20 B3 08 00                  call 0x140b820f0
00AF6DD0  4C 8B F8                        mov r15, rax
00AF6DD3  8D 46 1F                        lea eax, [rsi + 0x1f]
00AF6DD6  4D 85 FF                        test r15, r15
00AF6DD9  74 29                           je 0x140af6e04
00AF6DDB  44 8B C7                        mov r8d, edi
00AF6DDE  8B D0                           mov edx, eax
00AF6DE0  41 8B CE                        mov ecx, r14d
00AF6DE3  E8 08 B3 08 00                  call 0x140b820f0
00AF6DE8  4C 8B E0                        mov r12, rax
00AF6DEB  48 85 C0                        test rax, rax
00AF6DEE  74 07                           je 0x140af6df7
00AF6DF0  C6 44 24 41 00                  mov byte ptr [rsp + 0x41], 0
00AF6DF5  EB 0D                           jmp 0x140af6e04
00AF6DF7  33 D2                           xor edx, edx
00AF6DF9  49 8B CF                        mov rcx, r15
00AF6DFC  E8 6F BA 08 00                  call 0x140b82870
00AF6E01  45 33 FF                        xor r15d, r15d
00AF6E04  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF6E0D  BA 0C 00 00 00                  mov edx, 0xc
00AF6E12  48 8B C8                        mov rcx, rax
00AF6E15  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AF6E1A  E8 51 D5 8C FF                  call 0x1403c4370
00AF6E1F  8B 05 A7 7D 31 00               mov eax, dword ptr [rip + 0x317da7]
00AF6E25  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
00AF6E2C  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
00AF6E32  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00AF6E37  48 83 4C 24 50 FF               or qword ptr [rsp + 0x50], 0xffffffffffffffff
00AF6E3D  4C 69 C0 80 96 98 00            imul r8, rax, 0x989680
00AF6E44  49 C1 F8 02                     sar r8, 2
00AF6E48  49 8B D0                        mov rdx, r8
00AF6E4B  48 F7 DA                        neg rdx
00AF6E4E  E8 8D 9A 8A FF                  call 0x1403a08e0
00AF6E53  8B 05 73 7D 31 00               mov eax, dword ptr [rip + 0x317d73]
00AF6E59  48 69 C0 80 96 98 00            imul rax, rax, 0x989680
00AF6E60  45 32 F6                        xor r14b, r14b
00AF6E63  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AF6E68  48 8D 43 10                     lea rax, [rbx + 0x10]
00AF6E6C  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00AF6E70  48 8D 43 28                     lea rax, [rbx + 0x28]
00AF6E74  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00AF6E78  48 8D 43 68                     lea rax, [rbx + 0x68]
00AF6E7C  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00AF6E83  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00AF6E88  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00AF6E8E  48 8D 55 70                     lea rdx, [rbp + 0x70]
00AF6E92  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AF6E98  45 33 C9                        xor r9d, r9d
00AF6E9B  45 32 ED                        xor r13b, r13b
00AF6E9E  44 8B C6                        mov r8d, esi
00AF6EA1  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00AF6EA6  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00AF6EAB  41 8D 49 03                     lea ecx, [r9 + 3]
00AF6EAF  E8 5C 62 71 FF                  call 0x14020d110
00AF6EB4  85 C0                           test eax, eax
00AF6EB6  0F 84 93 01 00 00               je 0x140af704f
00AF6EBC  83 E8 01                        sub eax, 1
00AF6EBF  0F 84 93 00 00 00               je 0x140af6f58
00AF6EC5  83 F8 01                        cmp eax, 1
00AF6EC8  0F 85 59 02 00 00               jne 0x140af7127
00AF6ECE  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00AF6ED3  33 FF                           xor edi, edi
00AF6ED5  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF6ED9  33 F6                           xor esi, esi
00AF6EDB  39 B0 58 03 00 00               cmp dword ptr [rax + 0x358], esi
00AF6EE1  76 64                           jbe 0x140af6f47
00AF6EE3  0F B7 00                        movzx eax, word ptr [rax]
00AF6EE6  8D 14 C7                        lea edx, [rdi + rax*8]
00AF6EE9  48 8B 03                        mov rax, qword ptr [rbx]
00AF6EEC  0F AF 15 19 3B 40 00            imul edx, dword ptr [rip + 0x403b19]
00AF6EF3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AF6EF7  03 D6                           add edx, esi
00AF6EF9  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00AF6EFD  B9 00 00 00 00                  mov ecx, 0
00AF6F02  A8 01                           test al, 1
00AF6F04  48 0F 44 C8                     cmove rcx, rax
00AF6F08  48 85 C9                        test rcx, rcx
00AF6F0B  74 2C                           je 0x140af6f39
00AF6F0D  44 8B 81 C8 02 00 00            mov r8d, dword ptr [rcx + 0x2c8]
00AF6F14  41 0F BA E0 0E                  bt r8d, 0xe
00AF6F19  72 1E                           jb 0x140af6f39
00AF6F1B  83 79 04 00                     cmp dword ptr [rcx + 4], 0
00AF6F1F  75 18                           jne 0x140af6f39
00AF6F21  41 81 E0 FF 3F 00 00            and r8d, 0x3fff
00AF6F28  44 2B 81 CC 02 00 00            sub r8d, dword ptr [rcx + 0x2cc]
00AF6F2F  74 08                           je 0x140af6f39
00AF6F31  49 8B D6                        mov rdx, r14
00AF6F34  E8 1F 8C 85 FF                  call 0x14034fb58
00AF6F39  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF6F3D  FF C6                           inc esi
00AF6F3F  3B B0 58 03 00 00               cmp esi, dword ptr [rax + 0x358]
00AF6F45  72 9C                           jb 0x140af6ee3
00AF6F47  BE 01 00 00 00                  mov esi, 1
00AF6F4C  03 FE                           add edi, esi
00AF6F4E  83 FF 08                        cmp edi, 8
00AF6F51  7C 82                           jl 0x140af6ed5
00AF6F53  E9 CA 01 00 00                  jmp 0x140af7122
00AF6F58  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00AF6F5D  33 FF                           xor edi, edi
00AF6F5F  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF6F63  45 33 F6                        xor r14d, r14d
00AF6F66  44 39 B0 58 03 00 00            cmp dword ptr [rax + 0x358], r14d
00AF6F6D  0F 86 C8 00 00 00               jbe 0x140af703b
00AF6F73  0F B7 00                        movzx eax, word ptr [rax]
00AF6F76  8D 14 C7                        lea edx, [rdi + rax*8]
00AF6F79  48 8B 03                        mov rax, qword ptr [rbx]
00AF6F7C  0F AF 15 89 3A 40 00            imul edx, dword ptr [rip + 0x403a89]
00AF6F83  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AF6F87  41 03 D6                        add edx, r14d
00AF6F8A  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00AF6F8E  40 84 C6                        test sil, al
00AF6F91  BE 00 00 00 00                  mov esi, 0
00AF6F96  48 0F 44 F0                     cmove rsi, rax
00AF6F9A  8B 86 C0 02 00 00               mov eax, dword ptr [rsi + 0x2c0]
00AF6FA0  3B 86 C4 02 00 00               cmp eax, dword ptr [rsi + 0x2c4]
00AF6FA6  75 7A                           jne 0x140af7022
00AF6FA8  BA FF 3F 00 00                  mov edx, 0x3fff
00AF6FAD  48 8B CE                        mov rcx, rsi
00AF6FB0  E8 3B 8B 84 FF                  call 0x14033faf0
00AF6FB5  33 C9                           xor ecx, ecx
00AF6FB7  84 C0                           test al, al
00AF6FB9  74 67                           je 0x140af7022
00AF6FBB  8B 05 CF 3A 40 00               mov eax, dword ptr [rip + 0x403acf]
00AF6FC1  A8 02                           test al, 2
00AF6FC3  0F 85 35 03 00 00               jne 0x140af72fe
00AF6FC9  8D 41 01                        lea eax, [rcx + 1]
00AF6FCC  3B F8                           cmp edi, eax
00AF6FCE  75 32                           jne 0x140af7002
00AF6FD0  38 4C 24 41                     cmp byte ptr [rsp + 0x41], cl
00AF6FD4  75 2C                           jne 0x140af7002
00AF6FD6  41 89 07                        mov dword ptr [r15], eax
00AF6FD9  8D 51 03                        lea edx, [rcx + 3]
00AF6FDC  49 89 77 08                     mov qword ptr [r15 + 8], rsi
00AF6FE0  48 8D 05 E9 87 CD FF            lea rax, [rip - 0x327817]
00AF6FE7  49 89 0C 24                     mov qword ptr [r12], rcx
00AF6FEB  49 8B CC                        mov rcx, r12
00AF6FEE  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
00AF6FF3  4D 89 7C 24 18                  mov qword ptr [r12 + 0x18], r15
00AF6FF8  E8 23 25 80 FF                  call 0x1402f9520
00AF6FFD  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
00AF7002  48 8D 93 14 01 00 00            lea rdx, [rbx + 0x114]
00AF7009  48 8B CE                        mov rcx, rsi
00AF700C  E8 EB 5E EF FF                  call 0x1409ecefc
00AF7011  85 C0                           test eax, eax
00AF7013  45 0F B6 ED                     movzx r13d, r13b
00AF7017  BE 01 00 00 00                  mov esi, 1
00AF701C  44 0F 48 EE                     cmovs r13d, esi
00AF7020  EB 05                           jmp 0x140af7027
00AF7022  BE 01 00 00 00                  mov esi, 1
00AF7027  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF702B  44 03 F6                        add r14d, esi
00AF702E  44 3B B0 58 03 00 00            cmp r14d, dword ptr [rax + 0x358]
00AF7035  0F 82 38 FF FF FF               jb 0x140af6f73
00AF703B  03 FE                           add edi, esi
00AF703D  3B FE                           cmp edi, esi
00AF703F  0F 8E 1A FF FF FF               jle 0x140af6f5f
00AF7045  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00AF704A  E9 E1 00 00 00                  jmp 0x140af7130
00AF704F  8B 83 10 01 00 00               mov eax, dword ptr [rbx + 0x110]
00AF7055  85 C0                           test eax, eax
00AF7057  0F 85 52 02 00 00               jne 0x140af72af
00AF705D  33 FF                           xor edi, edi
00AF705F  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AF7063  33 F6                           xor esi, esi
00AF7065  39 B2 58 03 00 00               cmp dword ptr [rdx + 0x358], esi
00AF706B  0F 86 A1 00 00 00               jbe 0x140af7112
00AF7071  44 8D 76 01                     lea r14d, [rsi + 1]
00AF7075  0F B7 02                        movzx eax, word ptr [rdx]
00AF7078  48 8B 0B                        mov rcx, qword ptr [rbx]
00AF707B  44 8D 04 C7                     lea r8d, [rdi + rax*8]
00AF707F  44 0F AF 05 85 39 40 00         imul r8d, dword ptr [rip + 0x403985]
00AF7087  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00AF708B  44 03 C6                        add r8d, esi
00AF708E  4E 8B 04 C0                     mov r8, qword ptr [rax + r8*8]
00AF7092  45 84 C6                        test r14b, r8b
00AF7095  74 14                           je 0x140af70ab
00AF7097  44 8B CE                        mov r9d, esi
00AF709A  44 8B C7                        mov r8d, edi
00AF709D  E8 96 FA FF FF                  call 0x140af6b38
00AF70A2  85 C0                           test eax, eax
00AF70A4  79 05                           jns 0x140af70ab
00AF70A6  45 8A EE                        mov r13b, r14b
00AF70A9  EB 54                           jmp 0x140af70ff
00AF70AB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF70AF  0F B7 08                        movzx ecx, word ptr [rax]
00AF70B2  48 8B 03                        mov rax, qword ptr [rbx]
00AF70B5  8D 14 CF                        lea edx, [rdi + rcx*8]
00AF70B8  0F AF 15 4D 39 40 00            imul edx, dword ptr [rip + 0x40394d]
00AF70BF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AF70C3  03 D6                           add edx, esi
00AF70C5  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00AF70C9  B9 00 00 00 00                  mov ecx, 0
00AF70CE  41 84 C6                        test r14b, al
00AF70D1  48 0F 44 C8                     cmove rcx, rax
00AF70D5  48 85 C9                        test rcx, rcx
00AF70D8  74 25                           je 0x140af70ff
00AF70DA  8B 91 D4 02 00 00               mov edx, dword ptr [rcx + 0x2d4]
00AF70E0  E8 0B 8A 84 FF                  call 0x14033faf0
00AF70E5  84 C0                           test al, al
00AF70E7  74 16                           je 0x140af70ff
00AF70E9  48 8D 93 14 01 00 00            lea rdx, [rbx + 0x114]
00AF70F0  E8 07 5E EF FF                  call 0x1409ecefc
00AF70F5  85 C0                           test eax, eax
00AF70F7  45 0F B6 ED                     movzx r13d, r13b
00AF70FB  45 0F 48 EE                     cmovs r13d, r14d
00AF70FF  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AF7103  41 03 F6                        add esi, r14d
00AF7106  3B B2 58 03 00 00               cmp esi, dword ptr [rdx + 0x358]
00AF710C  0F 82 63 FF FF FF               jb 0x140af7075
00AF7112  BE 01 00 00 00                  mov esi, 1
00AF7117  03 FE                           add edi, esi
00AF7119  83 FF 08                        cmp edi, 8
00AF711C  0F 8C 3D FF FF FF               jl 0x140af705f
00AF7122  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00AF7127  45 84 F6                        test r14b, r14b
00AF712A  0F 85 A3 00 00 00               jne 0x140af71d3
00AF7130  45 33 C0                        xor r8d, r8d
00AF7133  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF7137  45 33 C9                        xor r9d, r9d
00AF713A  44 39 88 58 03 00 00            cmp dword ptr [rax + 0x358], r9d
00AF7141  76 64                           jbe 0x140af71a7
00AF7143  0F B7 00                        movzx eax, word ptr [rax]
00AF7146  41 8D 14 C0                     lea edx, [r8 + rax*8]
00AF714A  48 8B 03                        mov rax, qword ptr [rbx]
00AF714D  0F AF 15 B8 38 40 00            imul edx, dword ptr [rip + 0x4038b8]
00AF7154  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AF7158  41 03 D1                        add edx, r9d
00AF715B  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00AF715F  B9 00 00 00 00                  mov ecx, 0
00AF7164  40 84 C6                        test sil, al
00AF7167  48 0F 44 C8                     cmove rcx, rax
00AF716B  8B 81 C0 02 00 00               mov eax, dword ptr [rcx + 0x2c0]
00AF7171  89 81 C4 02 00 00               mov dword ptr [rcx + 0x2c4], eax
00AF7177  8B 81 C8 02 00 00               mov eax, dword ptr [rcx + 0x2c8]
00AF717D  25 FF 3F 00 00                  and eax, 0x3fff
00AF7182  3B 81 D4 02 00 00               cmp eax, dword ptr [rcx + 0x2d4]
00AF7188  7D 05                           jge 0x140af718f
00AF718A  45 84 ED                        test r13b, r13b
00AF718D  74 03                           je 0x140af7192
00AF718F  44 8A F6                        mov r14b, sil
00AF7192  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF7196  44 03 CE                        add r9d, esi
00AF7199  44 3B 88 58 03 00 00            cmp r9d, dword ptr [rax + 0x358]
00AF71A0  72 A1                           jb 0x140af7143
00AF71A2  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00AF71A7  44 03 C6                        add r8d, esi
00AF71AA  44 3B C6                        cmp r8d, esi
00AF71AD  7E 84                           jle 0x140af7133
00AF71AF  45 84 F6                        test r14b, r14b
00AF71B2  74 1F                           je 0x140af71d3
00AF71B4  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AF71BA  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00AF71BE  41 B9 A0 00 00 00               mov r9d, 0xa0
00AF71C4  45 33 C0                        xor r8d, r8d
00AF71C7  48 C7 C2 80 69 67 FF            mov rdx, 0xffffffffff676980
00AF71CE  E8 FD 8D 73 FF                  call 0x14022ffd0
00AF71D3  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
00AF71D8  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00AF71DD  33 D2                           xor edx, edx
00AF71DF  C7 44 24 60 01 00 20 00         mov dword ptr [rsp + 0x60], 0x200001
00AF71E7  41 B8 00 01 00 00               mov r8d, 0x100
00AF71ED  E8 4E FA BC FF                  call 0x1406c6c40
00AF71F2  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00AF71F6  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AF71FB  45 33 C0                        xor r8d, r8d
00AF71FE  0F B7 09                        movzx ecx, word ptr [rcx]
00AF7201  E8 3A F5 75 FF                  call 0x140256740
00AF7206  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00AF720B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF7210  48 8B 97 28 02 00 00            mov rdx, qword ptr [rdi + 0x228]
00AF7217  E8 14 E0 80 FF                  call 0x140305230
00AF721C  85 C0                           test eax, eax
00AF721E  75 0D                           jne 0x140af722d
00AF7220  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AF7225  48 8B CF                        mov rcx, rdi
00AF7228  E8 FF 87 7D FF                  call 0x1402cfa2c
00AF722D  33 F6                           xor esi, esi
00AF722F  44 8D 6E 01                     lea r13d, [rsi + 1]
00AF7233  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF7237  33 FF                           xor edi, edi
00AF7239  39 B8 58 03 00 00               cmp dword ptr [rax + 0x358], edi
00AF723F  76 59                           jbe 0x140af729a
00AF7241  0F B7 00                        movzx eax, word ptr [rax]
00AF7244  41 BE 00 00 00 00               mov r14d, 0
00AF724A  8D 14 C6                        lea edx, [rsi + rax*8]
00AF724D  48 8B 03                        mov rax, qword ptr [rbx]
00AF7250  0F AF 15 B5 37 40 00            imul edx, dword ptr [rip + 0x4037b5]
00AF7257  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AF725B  03 D7                           add edx, edi
00AF725D  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00AF7261  41 84 C5                        test r13b, al
00AF7264  4C 0F 44 F0                     cmove r14, rax
00AF7268  4D 85 F6                        test r14, r14
00AF726B  74 1E                           je 0x140af728b
00AF726D  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00AF7271  8B D7                           mov edx, edi
00AF7273  E8 BC 32 B6 FF                  call 0x14065a534
00AF7278  41 39 86 98 02 00 00            cmp dword ptr [r14 + 0x298], eax
00AF727F  74 0A                           je 0x140af728b
00AF7281  8B D0                           mov edx, eax
00AF7283  49 8B CE                        mov rcx, r14
00AF7286  E8 39 37 AD FF                  call 0x1405ca9c4
00AF728B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AF728F  41 03 FD                        add edi, r13d
00AF7292  3B B8 58 03 00 00               cmp edi, dword ptr [rax + 0x358]
00AF7298  72 A7                           jb 0x140af7241
00AF729A  41 03 F5                        add esi, r13d
00AF729D  83 FE 08                        cmp esi, 8
00AF72A0  7C 91                           jl 0x140af7233
00AF72A2  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00AF72A7  41 8B F5                        mov esi, r13d
00AF72AA  E9 D9 FB FF FF                  jmp 0x140af6e88
00AF72AF  4D 85 FF                        test r15, r15
00AF72B2  74 0A                           je 0x140af72be
00AF72B4  33 D2                           xor edx, edx
00AF72B6  49 8B CF                        mov rcx, r15
00AF72B9  E8 B2 B5 08 00                  call 0x140b82870
00AF72BE  4D 85 E4                        test r12, r12
00AF72C1  74 0A                           je 0x140af72cd
00AF72C3  33 D2                           xor edx, edx
00AF72C5  49 8B CC                        mov rcx, r12
00AF72C8  E8 A3 B5 08 00                  call 0x140b82870
00AF72CD  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00AF72D4  48 33 CC                        xor rcx, rsp
00AF72D7  E8 64 53 BB FF                  call 0x1406ac640
00AF72DC  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
00AF72E4  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00AF72E8  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00AF72EC  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00AF72F0  49 8B E3                        mov rsp, r11
00AF72F3  41 5F                           pop r15
00AF72F5  41 5E                           pop r14
00AF72F7  41 5D                           pop r13
00AF72F9  41 5C                           pop r12
00AF72FB  5D                              pop rbp
00AF72FC  C3                              ret
00AF72FD  CC                              int3
00AF72FE  45 33 C9                        xor r9d, r9d
00AF7301  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AF7306  48 8B D0                        mov rdx, rax
00AF7309  B9 63 01 00 00                  mov ecx, 0x163
00AF730E  45 8D 41 02                     lea r8d, [r9 + 2]
00AF7312  E8 49 63 A0 FF                  call 0x1404fd660
00AF7317  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWorkQueueManagerThread(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m177;
    unsigned __int8 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int8 v_stack_m190;
    unsigned __int8 v_stack_m198;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 3226035)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 184 + 136) = result;
    a2 = 0;
    result = memset(v_stack_m158, a2, 264, a4);
    v_stack_m177 = 1;
    v_r12 = 0;
    result = ExAllocatePool2((unsigned int)((unsigned int)(1 + 63)), 1 + 15, (unsigned int)((unsigned int)((unsigned int)(0x6C577845ULL))), a4);
    if (result == 0) goto loc_00AF6E04;
    result = ExAllocatePool2((unsigned int)((unsigned int)(1 + 63)), (unsigned int)((unsigned int)(1 + 31)), (unsigned int)((unsigned int)((unsigned int)(0x6C577845ULL))), a4);
    if (result == 0) goto loc_00AF6DF7;
    v_stack_m177 = 0;
    goto loc_00AF6E04;
loc_00AF6DF7:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)((unsigned int)(0x6C577845ULL))), a4);
    v_r15 = 0;
loc_00AF6E04:
    v_stack_m160 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeSetActualBasePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 12, (unsigned int)((unsigned int)((unsigned int)(0x6C577845ULL))), a4);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(0x6C577845ULL)))) * ((unsigned int)(*(unsigned int *)(v_rip + 3243431)));
    a3 = (a3) >> (2);
    a2 = -(a3);
    result = KeSetTimer2(a1 + 128, a2, a3, v_stack_m170);
    result = ((unsigned int)(*(unsigned int *)(v_rip + 3243379))) * ((unsigned int)(*(unsigned int *)(v_rip + 3243379)));
    v_r14 = 0;
    v_stack_m170 = result;
    *(unsigned __int64 *)(v_rsp - 184 + 112) = a1 + 16;
    *(unsigned __int64 *)(v_rsp - 184 + 120) = a1 + 40;
    *(unsigned __int64 *)(v_rsp - 184 + 128) = a1 + 104;
    v_stack_m178 = 0;
loc_00AF6E88:
    a4 = 0;
    v_r13 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 1;
    result = KeWaitForMultipleObjects(a4 + 3, v_rsp - 184 + 112, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_00AF704F;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF6F58;
    if (((unsigned int)(result)) != 1) goto loc_00AF7127;
    v_rdi = 0;
loc_00AF6ED5:
    v_rsi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856)) <= 0) goto loc_00AF6F47;
loc_00AF6EE3:
    a2 = (unsigned int)((v_rdi + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4209433)));
    a2 = (unsigned int)((a2) + (0));
    a1 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8))) & (1)) == 0) { a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8); }
    if (a1 == 0) goto loc_00AF6F39;
    if (condition_is_below) goto loc_00AF6F39;
    if ((*(unsigned int *)(a1 + 4)) != 0) goto loc_00AF6F39;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 712))) & (0x3FFFULL));
    a3 = (unsigned int)((a3) - (*(unsigned int *)(a1 + 716)));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8);
    if (!(condition_is_equal)) {
        a2 = v_stack_m170;
        result = KeTimeOutQueueWaiters(a1, a2, a3, a4);
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856))) goto loc_00AF6EE3;
loc_00AF6F47:
    v_rdi = (unsigned int)((v_rdi) + (1));
    if (((unsigned int)(v_rdi)) < 8) goto loc_00AF6ED5;
    goto loc_00AF7122;
loc_00AF6F58:
    v_stack_m178 = 0;
    v_rdi = 0;
loc_00AF6F5F:
    v_r14 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856)) <= 0) goto loc_00AF703B;
loc_00AF6F73:
    a2 = (unsigned int)((v_rdi + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4209289)));
    a2 = (unsigned int)((a2) + (0));
    v_rsi = 0;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8)))) == 0) { v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8); }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 704)))) != (*(unsigned int *)(v_rsi + 708))) goto loc_00AF7022;
    result = ExpNewThreadNecessary(v_rsi, (unsigned int)(0x3FFFULL), a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00AF7022;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4209359)))) & (2)) != 0) goto loc_00AF72FE;
    if (0 != ((unsigned int)(a1 + 1))) goto loc_00AF7002;
    result = a1 + 1;
    if (v_stack_m177 == 0) {
        *(unsigned int *)(v_r15) = (unsigned int)(a1 + 1);
        a2 = a1 + 3;
        *(unsigned __int64 *)(v_r15 + 8) = v_rsi;
        result = v_rip - 3307543;
        *(unsigned __int64 *)(result) = 0;
        a1 = result;
        *(unsigned __int64 *)(result + 16) = result;
        *(unsigned __int64 *)(result + 24) = 0;
        result = ExQueueWorkItem(a1, a2, a3, a4);
        v_stack_m177 = 1;
    }
    result = ExpCreateWorkerThread(v_rsi, a1 + 276, a3, a4);
    v_r13 = 0;
    if (sign_flag) { v_r13 = 1; }
    goto loc_00AF7027;
loc_00AF7022:
loc_00AF7027:
    v_r14 = (unsigned int)((v_r14) + (1));
    if (((unsigned int)(v_r14)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856))) goto loc_00AF6F73;
loc_00AF703B:
    v_rdi = (unsigned int)((v_rdi) + (1));
    if (((unsigned int)(v_rdi)) <= 1) goto loc_00AF6F5F;
    goto loc_00AF7130;
loc_00AF704F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 272))) != 0) goto loc_00AF72AF;
    v_rdi = 0;
loc_00AF705F:
    v_rsi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856)) <= 0) goto loc_00AF7112;
loc_00AF7075:
    a3 = (unsigned int)((v_rdi + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4209029)));
    a3 = (unsigned int)((a3) + (0));
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a3 * 8)))) == 0) goto loc_00AF70AB;
    result = ExpPartitionCreatePoolDelayed(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 8), 0, 0);
    if (!sign_flag) goto loc_00AF70AB;
    goto loc_00AF70FF;
loc_00AF70AB:
    a2 = (unsigned int)((v_rdi + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4208973)));
    a2 = (unsigned int)((a2) + (0));
    a1 = 0;
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8)))) == 0) { a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8); }
    if (a1 == 0) goto loc_00AF70FF;
    result = ExpNewThreadNecessary(a1, (unsigned int)(*(unsigned int *)(a1 + 724)), 0, 0);
    v_r13 = (unsigned __int8)(v_rsi + 1);
    if ((unsigned __int8)(result) != 0) {
        a2 = a1 + 276;
        result = ExpCreateWorkerThread(a1, a2, 0, 0);
        v_r13 = (unsigned __int8)((unsigned __int8)(v_rsi + 1));
        if (sign_flag) { v_r13 = (unsigned int)(v_rsi + 1); }
    }
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi + 1)));
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856))) goto loc_00AF7075;
loc_00AF7112:
    v_rdi = (unsigned int)((v_rdi) + (1));
    if (((unsigned int)(v_rdi)) < 8) goto loc_00AF705F;
loc_00AF7122:
loc_00AF7127:
    if ((unsigned __int8)(v_stack_m178) != 0) goto loc_00AF71D3;
loc_00AF7130:
    a3 = 0;
loc_00AF7133:
    a4 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856)) <= 0) goto loc_00AF71A7;
loc_00AF7143:
    a2 = (unsigned int)((a3 + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4208824)));
    a2 = (unsigned int)((a2) + (0));
    a1 = 0;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8)))) == 0) { a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8); }
    *(unsigned int *)(a1 + 708) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 704)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 712))) & (0x3FFFULL));
    if (((unsigned int)(result)) >= (*(unsigned int *)(a1 + 724))) goto loc_00AF718F;
    v_r14 = v_stack_m178;
    if ((unsigned __int8)(v_r13) != 0) {
        v_r14 = 1;
    }
    a4 = (unsigned int)((a4) + (1));
    if (((unsigned int)(a4)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856))) goto loc_00AF7143;
    v_stack_m178 = (unsigned __int8)(v_r14);
loc_00AF71A7:
    a3 = (unsigned int)((a3) + (1));
    if (((unsigned int)(a3)) <= 1) goto loc_00AF7133;
    result = *(unsigned __int64 *)(a1 + 8);
    if ((unsigned __int8)(v_r14) != 0) {
        a1 = a1 + 40;
        a4 = 160;
        a3 = 0;
        a2 = 0xFFFFFFFFFF676980ULL;
        result = KeSetCoalescableTimer(a1, a2, a3, a4);
    }
    a2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, a2, 256, a4);
    a3 = 0;
    result = KeQueryNodeActiveAffinityEx(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)), v_stack_m158, a3, a4);
    result = KeIsEqualAffinityEx(v_stack_m158, *(unsigned __int64 *)(v_stack_m160 + 552), a3, a4);
    if ((unsigned int)(result) == 0) {
        a2 = v_stack_m158;
        a1 = v_stack_m160;
        result = KeSetUserAffinityThread(a1, a2, a3, a4);
    }
    v_rsi = 0;
loc_00AF7233:
    v_rdi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856)) <= 0) goto loc_00AF729A;
loc_00AF7241:
    a2 = (unsigned int)((v_rsi + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)) * 8) * (*(unsigned int *)(v_rip + 4208565)));
    a2 = (unsigned int)((a2) + (0));
    v_r14 = 0;
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8)))) == 0) { v_r14 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) + a2 * 8); }
    if (v_r14 == 0) goto loc_00AF728B;
    result = ExpGetNodeSubQueueConcurrencyCount(*(unsigned __int64 *)(a1 + 8), 0, a3, a4);
    if ((*(unsigned int *)(v_r14 + 664)) != ((unsigned int)(result))) {
        a2 = (unsigned int)(result);
        a1 = v_r14;
        result = KeSetMaximumCountPriQueue(a1, a2, a3, a4);
    }
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rsi + 1)));
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 856))) goto loc_00AF7241;
loc_00AF729A:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi + 1)));
    if (((unsigned int)(v_rsi)) < 8) goto loc_00AF7233;
    goto loc_00AF6E88;
loc_00AF72AF:
    result = *(unsigned __int64 *)(a1 + 8);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 184 + 136)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00AF72FE:
    a4 = 0;
    v_stack_m170 = a1;
    result = KeBugCheckEx(355, result, a4 + 2, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWorkQueueManagerThread(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m177;
    uint8_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint8_t v_stack_m190;
    uint8_t v_stack_m198;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x3139B3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xB8 + 0x88) = result;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 264, a4);
    v_stack_m177 = 1;
    local_r12 = 0;
    result = ExAllocatePool2((uint32_t)((uint32_t)(1 + 63)), 1 + 15, (uint32_t)((uint32_t)((uint32_t)(0x6C577845ULL))), a4);
    if (result == 0) goto loc_00AF6E04;
    result = ExAllocatePool2((uint32_t)((uint32_t)(1 + 63)), (uint32_t)((uint32_t)(1 + 31)), (uint32_t)((uint32_t)((uint32_t)(0x6C577845ULL))), a4);
    if (result == 0) goto loc_00AF6DF7;
    v_stack_m177 = 0;
    goto loc_00AF6E04;
loc_00AF6DF7:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x6C577845ULL))), a4);
    local_r15 = 0;
loc_00AF6E04:
    v_stack_m160 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeSetActualBasePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 12, (uint32_t)((uint32_t)((uint32_t)(0x6C577845ULL))), a4);
    a3 = ((uint32_t)((uint32_t)((uint32_t)(0x6C577845ULL)))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x317DA7)));
    a3 = (a3) >> (2);
    Arg2 = -(a3);
    result = KeSetTimer2(Arg1 + 128, Arg2, a3, v_stack_m170);
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x317D73))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x317D73)));
    local_r14 = 0;
    v_stack_m170 = result;
    *(void **)(local_rsp - 0xB8 + 0x70) = Arg1 + 16;
    *(void **)(local_rsp - 0xB8 + 0x78) = Arg1 + 40;
    *(void **)(local_rsp - 0xB8 + 0x80) = Arg1 + 104;
    v_stack_m178 = 0;
loc_00AF6E88:
    a4 = 0;
    local_r13 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 1;
    result = KeWaitForMultipleObjects(a4 + 3, local_rsp - 184 + 112, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_00AF704F;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF6F58;
    if (((uint32_t)(result)) != 1) goto loc_00AF7127;
    local_rdi = 0;
loc_00AF6ED5:
    local_rsi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358)) <= 0) goto loc_00AF6F47;
loc_00AF6EE3:
    Arg2 = (uint32_t)((local_rdi + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x403B19)));
    Arg2 = (uint32_t)((Arg2) + (0));
    Arg1 = 0;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8))) & (1)) == 0) { Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8); }
    if (Arg1 == NULL) goto loc_00AF6F39;
    if (condition_is_below) goto loc_00AF6F39;
    if ((*(uint32_t *)(arg1 + 0x4)) != 0) goto loc_00AF6F39;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C8))) & (0x3FFFULL));
    a3 = (uint32_t)((a3) - (*(uint32_t *)(arg1 + 0x2CC)));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8);
    if (!(condition_is_equal)) {
        Arg2 = v_stack_m170;
        result = KeTimeOutQueueWaiters(Arg1, Arg2, a3, a4);
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358))) goto loc_00AF6EE3;
loc_00AF6F47:
    local_rdi = (uint32_t)((local_rdi) + (1));
    if (((uint32_t)(local_rdi)) < 8) goto loc_00AF6ED5;
    goto loc_00AF7122;
loc_00AF6F58:
    v_stack_m178 = 0;
    local_rdi = 0;
loc_00AF6F5F:
    local_r14 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358)) <= 0) goto loc_00AF703B;
loc_00AF6F73:
    Arg2 = (uint32_t)((local_rdi + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x403A89)));
    Arg2 = (uint32_t)((Arg2) + (0));
    local_rsi = 0;
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8)))) == 0) { local_rsi = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8); }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x2C0)))) != (*(uint32_t *)(local_rsi + 0x2C4))) goto loc_00AF7022;
    result = ExpNewThreadNecessary(local_rsi, (uint32_t)(0x3FFFULL), a3, a4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00AF7022;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x403ACF)))) & (2)) != 0) goto loc_00AF72FE;
    if (0 != ((uint32_t)(Arg1 + 1))) goto loc_00AF7002;
    result = Arg1 + 1;
    if (v_stack_m177 == 0) {
        *(uint32_t *)(local_r15) = (uint32_t)(Arg1 + 1);
        Arg2 = Arg1 + 3;
        *(uint64_t *)(local_r15 + 0x8) = local_rsi;
        result = v_rip - 3307543;
        *(uint64_t *)(result) = 0;
        Arg1 = result;
        *(uint64_t *)(result + 0x10) = result;
        *(uint64_t *)(result + 0x18) = 0;
        result = ExQueueWorkItem(Arg1, Arg2, a3, a4);
        v_stack_m177 = 1;
    }
    result = ExpCreateWorkerThread(local_rsi, Arg1 + 276, a3, a4);
    local_r13 = 0;
    if (sign_flag) { local_r13 = 1; }
    goto loc_00AF7027;
loc_00AF7022:
loc_00AF7027:
    local_r14 = (uint32_t)((local_r14) + (1));
    if (((uint32_t)(local_r14)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358))) goto loc_00AF6F73;
loc_00AF703B:
    local_rdi = (uint32_t)((local_rdi) + (1));
    if (((uint32_t)(local_rdi)) <= 1) goto loc_00AF6F5F;
    goto loc_00AF7130;
loc_00AF704F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x110))) != 0) goto loc_00AF72AF;
    local_rdi = 0;
loc_00AF705F:
    local_rsi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358)) <= 0) goto loc_00AF7112;
loc_00AF7075:
    a3 = (uint32_t)((local_rdi + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x403985)));
    a3 = (uint32_t)((a3) + (0));
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + a3 * 8)))) == 0) goto loc_00AF70AB;
    result = ExpPartitionCreatePoolDelayed(*(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x8), 0, 0);
    if (!sign_flag) goto loc_00AF70AB;
    goto loc_00AF70FF;
loc_00AF70AB:
    Arg2 = (uint32_t)((local_rdi + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x40394D)));
    Arg2 = (uint32_t)((Arg2) + (0));
    Arg1 = 0;
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8)))) == 0) { Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8); }
    if (Arg1 == NULL) goto loc_00AF70FF;
    result = ExpNewThreadNecessary(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x2D4)), 0, 0);
    local_r13 = (uint8_t)(local_rsi + 1);
    if ((uint8_t)(result) != 0) {
        Arg2 = Arg1 + 276;
        result = ExpCreateWorkerThread(Arg1, Arg2, 0, 0);
        local_r13 = (uint8_t)((uint8_t)(local_rsi + 1));
        if (sign_flag) { local_r13 = (uint32_t)(local_rsi + 1); }
    }
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi + 1)));
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358))) goto loc_00AF7075;
loc_00AF7112:
    local_rdi = (uint32_t)((local_rdi) + (1));
    if (((uint32_t)(local_rdi)) < 8) goto loc_00AF705F;
loc_00AF7122:
loc_00AF7127:
    if ((uint8_t)(v_stack_m178) != 0) goto loc_00AF71D3;
loc_00AF7130:
    a3 = 0;
loc_00AF7133:
    a4 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358)) <= 0) goto loc_00AF71A7;
loc_00AF7143:
    Arg2 = (uint32_t)((a3 + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x4038B8)));
    Arg2 = (uint32_t)((Arg2) + (0));
    Arg1 = 0;
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8)))) == 0) { Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8); }
    *(uint32_t *)(arg1 + 0x2C4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C0)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C8))) & (0x3FFFULL));
    if (((uint32_t)(result)) >= (*(uint32_t *)(arg1 + 0x2D4))) goto loc_00AF718F;
    local_r14 = v_stack_m178;
    if ((uint8_t)(local_r13) != 0) {
        local_r14 = 1;
    }
    a4 = (uint32_t)((a4) + (1));
    if (((uint32_t)(a4)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358))) goto loc_00AF7143;
    v_stack_m178 = (uint8_t)(local_r14);
loc_00AF71A7:
    a3 = (uint32_t)((a3) + (1));
    if (((uint32_t)(a3)) <= 1) goto loc_00AF7133;
    result = *(uint64_t *)(arg1 + 0x8);
    if ((uint8_t)(local_r14) != 0) {
        Arg1 = Arg1 + 40;
        a4 = 160;
        a3 = 0;
        Arg2 = 0xFFFFFFFFFF676980ULL;
        result = KeSetCoalescableTimer(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, Arg2, 256, a4);
    a3 = 0;
    result = KeQueryNodeActiveAffinityEx(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)), v_stack_m158, a3, a4);
    result = KeIsEqualAffinityEx(v_stack_m158, *(uint64_t *)(v_stack_m160 + 0x228), a3, a4);
    if ((uint32_t)(result) == 0) {
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m160;
        result = KeSetUserAffinityThread(Arg1, Arg2, a3, a4);
    }
    local_rsi = 0;
loc_00AF7233:
    local_rdi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358)) <= 0) goto loc_00AF729A;
loc_00AF7241:
    Arg2 = (uint32_t)((local_rsi + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8)) * 8) * (*(uint32_t *)(v_rip + 0x4037B5)));
    Arg2 = (uint32_t)((Arg2) + (0));
    local_r14 = 0;
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8)))) == 0) { local_r14 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x8) + Arg2 * 8); }
    if (local_r14 == 0) goto loc_00AF728B;
    result = ExpGetNodeSubQueueConcurrencyCount(*(uint64_t *)(arg1 + 0x8), 0, a3, a4);
    if ((*(uint32_t *)(local_r14 + 0x298)) != ((uint32_t)(result))) {
        Arg2 = (uint32_t)(result);
        Arg1 = local_r14;
        result = KeSetMaximumCountPriQueue(Arg1, Arg2, a3, a4);
    }
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rsi + 1)));
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x358))) goto loc_00AF7241;
loc_00AF729A:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi + 1)));
    if (((uint32_t)(local_rsi)) < 8) goto loc_00AF7233;
    goto loc_00AF6E88;
loc_00AF72AF:
    result = *(uint64_t *)(arg1 + 0x8);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0xB8 + 0x88)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_00AF72FE:
    a4 = 0;
    v_stack_m170 = Arg1;
    result = KeBugCheckEx(355, result, a4 + 2, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x110` | `32` | `R` |
| `Arg1` | `+ 0x114` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF6D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
